---
title: PAID Version 4 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 1
description: Decentralized Hospital Computer Program (DHCP) Personnel and Accounting Integrated Data (PAID) Version 4.0 provides enhanced time and attendance for VA Medical Centers. Of over 190,000 employees in the Veterans Health Administration (VHA), there are more than 20,000 timekeepers and 30,000 supervisor
audience: 
keywords: 
  - blockquote
  - class
  - width
  - style
  - employee
  - time
  - even
  - table
  - tour
  - leave
page_count: 0
word_count: 58657
section_count: 25
table_count: 31
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Department of Veterans AffairsPersonnel and Accounting Integrated Data (PAID)User Manual

![](paid-version-4-user-manual/001.png)

Version 4.0March 2018Department of Veterans AffairsOffice of Information and Technology (OIT)Product Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Section 1: Time and Attendance (T&A)](#section-1-time-and-attendance-ta)
  - [Overview](#overview)
  - [Package Operation](#package-operation)
  - [Chapter 1. Package Management](#chapter-1-package-management)
  - [Chapter 2. Employee Menu](#chapter-2-employee-menu)
  - [Chapter 3. Payroll Main Menu](#chapter-3-payroll-main-menu)
  - [Chapter 4. Payroll Supervisor Menu](#chapter-4-payroll-supervisor-menu)
  - [Chapter 5. T&A Supervisor Menu](#chapter-5-ta-supervisor-menu)
  - [Chapter 6. T&A OT/Supervisor Menu](#chapter-6-ta-otsupervisor-menu)
  - [Chapter 7. Timekeeper Main Menu](#chapter-7-timekeeper-main-menu)
  - [Chapter 8. Employee Inquiry/Reports Menu](#chapter-8-employee-inquiryreports-menu)
  - [Glossary](#glossary)
- [Section 2. Education Tracking](#section-2-education-tracking)
  - [Chapter 1. Package Management](#chapter-1-package-management-1)
  - [Chapter 2: IRM and Package Set-up Menus](#chapter-2-irm-and-package-set-up-menus)
  - [Chapter 3: Enter Edit Class Information](#chapter-3-enter-edit-class-information)
  - [Chapter 4: Class Registration](#chapter-4-class-registration)
  - [Chapter 5: Attendance at Programs](#chapter-5-attendance-at-programs)
  - [Chapter 6: Reports](#chapter-6-reports)
  - [Glossary](#glossary-1)
- [Appendix A: Supplemental Information for Part-time Physicians (Patch PRS\4.0\93)](#appendix-a-supplemental-information-for-part-time-physicians-patch-prs4093)
- [Appendix B: Upgrade ETA For Telework (Increment 1-Comp Time Expiration Updates) (Patch PRS\4.0\133)](#appendix-b-upgrade-eta-for-telework-increment-1-comp-time-expiration-updates-patch-prs40133)
- [Introduction](#introduction)
  - [Patch Nomenclature](#patch-nomenclature)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
- [Changes and Enhancements](#changes-and-enhancements)
  - [Changes to the Pay Period Display](#changes-to-the-pay-period-display)
  - [Changes to the Comp Time/Credit Hours Balance Display](#changes-to-the-comp-timecredit-hours-balance-display)
  - [Changes to the Supervisory Approvals Function](#changes-to-the-supervisory-approvals-function)
- [Support Information](#support-information)
This manual is designed as a reference guide for Payroll supervisors, Payroll clerks, timekeepers, Time and Leave Unit supervisors, and overtime approving officials who will be using the Decentralized Hospital Computer Program (DHCP) Personnel and Accounting Integrated Data (PAID) package for the recording of payroll data. In fact, any employee with access to the DHCP system may use this package to make leave requests or view their own leave balances. The manual provides the users with the information necessary to view, enter, and edit time and attendance report data. The purpose of the time and attendance (T&A) portion of the software is to collect process and transmit data necessary to pay employees. The package allows all time and attendance report data to be posted via a terminal and applies coded payroll rules to “decompose” this posted data into an 8B record for transmission to the Austin Automation Center (AAC). The target audience includes all employees since any employee may have access to the station’s DHCP system and can make an electronic leave request. The hard copy time and attendance report has been eliminated.
The package includes a continuously updated employee master record database. Payroll and Personnel users are the target audience for this database. They are able to view, but not change this data. Employee master record data from the AAC is stored at the station and updated regularly. The purpose, scope and target audience for this portion of the software remains the same. The employee master record database rather than a biweekly 8B download is used to create a time and attendance report stub record.
The Education Tracking module documents employee and student participation at mandatory inservices, continuing education programs, ward inservices, and miscellaneous employee training. It has been designed for the Veterans Affairs’ Decentralized Hospital Computer Program (DHCP) to eliminate DHCP Class III education programs used in the Department of Veterans Affairs (DVA) facilities. This software can be implemented by all hospital services and although all service data is stored in a centralized database, no service can read another service’s records without the appropriate level of user access. This access is restricted through the use of software keys.
Table of Contents
Preface [3](#preface)
Section 1: Time and Attendance (T&A) [12](#section-1-time-and-attendance-ta)
Overview [15](#overview)
Package Operation [16](#package-operation)
Chapter 1. Package Management [17](#chapter-1.-package-management)
Edit Electronic Signature Codes [18](#edit-electronic-signature-codes)
Using Screens for Data Entry [19](#using-screens-for-data-entry)
Display/Edit Area [20](#displayedit-area)
Command Area [21](#command-area)
Pop-up Pages [21](#pop-up-pages)
Chapter 2. Employee Menu [22](#chapter-2.-employee-menu)
Leave Request [23](#leave-request)
Leave Balances [24](#leave-balances)
Display Leave Requests [25](#display-leave-requests)
Cancel Leave Request [26](#cancel-leave-request)
Service Record Screen [27](#service-record-screen)
Display Pay Period [29](#display-pay-period)
Self Registration Enter/Edit [30](#self-registration-enteredit)
Edit Leave Request [32](#edit-leave-request)
Display Leave Used [33](#display-leave-used)
Review FY Recess for 9 Month AWS Employee [34](#review-fy-recess-for-9-month-aws-employee)
Chapter 3. Payroll Main Menu [37](#chapter-3.-payroll-main-menu)
Pay Period Exceptions [38](#pay-period-exceptions)
Display Employee Pay Period [39](#display-employee-pay-period)
Return Record to Timekeeper [40](#return-record-to-timekeeper)
Display Employee Entitlements [41](#display-employee-entitlements)
Post Miscellaneous Data [42](#post-miscellaneous-data)
Tour of Duty Management [45](#tour-of-duty-management)
Display Tour of Duty [46](#display-tour-of-duty)
List Tours by T&L [48](#list-tours-by-tl)
T&L Management [50](#tl-management)
Display T&L Unit [51](#display-tl-unit)
Daily T&L List [52](#daily-tl-list)
List Prior Pay Period Exceptions [53](#list-prior-pay-period-exceptions)
Create Employee Record for Pay Period [55](#create-employee-record-for-pay-period)
Employee Inquiry Menu [56](#employee-inquiry-menu)
Print Employee Entries [57](#print-employee-entries)
Search Employee Entries [60](#search-employee-entries)
Employee Inquiry [63](#employee-inquiry)
Payrun Data Inquiry [65](#payrun-data-inquiry)
Update PAID Codes (General Updates) [66](#update-paid-codes-general-updates)
Update PAID Codes (Telework Indicators) [67](#update-paid-codes-telework-indicators)
List/Clear Prior Pay Period Corrections [69](#listclear-prior-pay-period-corrections)
Change Employee T&L Unit [70](#change-employee-tl-unit)
List Un-Certified Employees [71](#list-un-certified-employees)
Clear Prior Pay Period Exceptions [72](#clear-prior-pay-period-exceptions)
List Leave Requests [73](#list-leave-requests)
List OT/CT Requests [74](#list-otct-requests)
Display Complete Request/Pay Period Records [75](#display-complete-requestpay-period-records)
Display Leave Request [76](#display-leave-request)
Display OT/CT Request [77](#display-otct-request)
Display Environmental Differential Request [78](#display-environmental-differential-request)
Display Pay Period for Employee [79](#display-pay-period-for-employee)
Employee Reports [80](#employee-reports)
Expenditures [81](#expenditures)
Employee Overtime/Comp Time Report [82](#employee-overtimecomp-time-report)
Employee Prior Pay Period Adjustments [83](#employee-prior-pay-period-adjustments)
Employee Leave Used [85](#employee-leave-used)
PAID T&L Report [86](#paid-tl-report)
Review FY Recess for 9 Month AWS Employee [87](#review-fy-recess-for-9-month-aws-employee-1)
Display Employee Tour Hours [90](#display-employee-tour-hours)
Chapter 4. Payroll Supervisor Menu [92](#chapter-4.-payroll-supervisor-menu)
Open Next Pay Period [93](#open-next-pay-period)
Un-Reviewed Employees (All T&Ls) [94](#un-reviewed-employees-all-tls)
8B Edit Checks [95](#b-edit-checks)
Transmit 8B Data to Austin [96](#transmit-8b-data-to-austin)
Transmission History [97](#transmission-history)
Payroll Table Maintenance [98](#payroll-table-maintenance)
Display Special Tour Indicator [99](#display-special-tour-indicator)
Display Type of Time Table [100](#display-type-of-time-table)
Display Time Remarks [101](#display-time-remarks)
Display Entitlement Table [102](#display-entitlement-table)
Enter/Edit Tour of Duty [104](#enteredit-tour-of-duty)
Special Tour Indicators [117](#special-tour-indicators)
Enter/Edit T&L Unit [119](#enteredit-tl-unit)
Set Holiday Benefit Day [121](#set-holiday-benefit-day)
List Supervisors Certified by a T&L [122](#list-supervisors-certified-by-a-tl)
Payroll Main Menu [123](#payroll-main-menu)
Chapter 5. T&A Supervisor Menu [124](#chapter-5.-ta-supervisor-menu)
Supervisory Approvals [125](#supervisory-approvals)
Pay Period Certification [128](#pay-period-certification)
List Leave Requests [130](#list-leave-requests-1)
Employee Leave Balances [131](#employee-leave-balances)
Display OT/CT Requests [132](#display-otct-requests)
List Daily Exceptions [133](#list-daily-exceptions)
Display Pay Period Exceptions [134](#display-pay-period-exceptions)
Display Employee Tour of Duty [135](#display-employee-tour-of-duty)
List Environment Diff. Requests [139](#list-environment-diff.-requests)
List Un-Certified Employees [140](#list-un-certified-employees-1)
List Prior Pay Period Exceptions [141](#list-prior-pay-period-exceptions-1)
Employee Reports [142](#employee-reports-1)
Expenditures [143](#expenditures-1)
Employee Overtime/CompTime Report (OT/CT) [144](#employee-overtimecomptime-report-otct)
Employee Prior Pay Period Adjustments [145](#employee-prior-pay-period-adjustments-1)
Employee Leave Reports [147](#employee-leave-reports)
Employee Leave Used [148](#employee-leave-used-1)
Employee Leave Requested [149](#employee-leave-requested)
Employee Leave Pattern [150](#employee-leave-pattern)
Review FY Recess for 9 Month AWS Employee [152](#review-fy-recess-for-9-month-aws-employee-2)
Display Employee Tour Hours [155](#display-employee-tour-hours-1)
Chapter 6. T&A OT/Supervisor Menu [157](#chapter-6.-ta-otsupervisor-menu)
Approve OT/CT [158](#approve-otct)
Chapter 7. Timekeeper Main Menu [159](#chapter-7.-timekeeper-main-menu)
Post Employee Time [160](#post-employee-time)
Post Scheduled Tour of Duty [161](#post-scheduled-tour-of-duty)
Post Leave [162](#post-leave)
A\) Leave for the Entire Day [165](#leave-for-the-entire-day)
B\) Leave for Part of the Day [167](#leave-for-part-of-the-day)
C\) Leave During the Middle of the Day Which Includes Meal Time [169](#leave-during-the-middle-of-the-day-which-includes-meal-time)
D\) Combining Different Types of Leave in One Day [171](#combining-different-types-of-leave-in-one-day)
E\) Leave for Family Care and Bereavement, and Leave for Adoption [173](#leave-for-family-care-and-bereavement-and-leave-for-adoption)
F\) Donor Leave [175](#donor-leave)
Post OT/CT & Unscheduled Time [177](#post-otct-unscheduled-time)
Post Baylor Plan [181](#post-baylor-plan)
Post 9 Month AWS Employee [182](#post-9-month-aws-employee)
Post 36/40 AWS Plan [183](#post-3640-aws-plan)
Post for Holidays [184](#post-for-holidays)
Post for Daylight Savings Time [190](#post-for-daylight-savings-time)
Post Time for Doctors (Full Time & Part Time) [191](#post-time-for-doctors-full-time-part-time)
List Daily Exceptions [192](#list-daily-exceptions-1)
Display Pay Period Exceptions [193](#display-pay-period-exceptions-1)
Employee Data [194](#employee-data)
Display Posted Data [195](#display-posted-data)
Display Employee Pay Period [196](#display-employee-pay-period-1)
Display Employee Tour of Duty [197](#display-employee-tour-of-duty-1)
Enter/Edit Employee Tour of Duty [198](#enteredit-employee-tour-of-duty)
Employee Leave Balances [204](#employee-leave-balances-1)
Recess Enter/Edit for 9 Month AWS [205](#recess-enteredit-for-9-month-aws)
Available Actions [205](#available-actions)
The ListManager [207](#the-listmanager)
Display Employee Tour Hours [212](#display-employee-tour-hours-2)
List Leave Requests [214](#list-leave-requests-2)
Display OT/CT Requests [215](#display-otct-requests-1)
Enter OT/CT Request [216](#enter-otct-request)
Cancel OT Request [217](#cancel-ot-request)
Daily T&L List [218](#daily-tl-list-1)
List Tours by T&L [219](#list-tours-by-tl-1)
Daily T&L List [220](#daily-tl-list-2)
Prior Pay Period Adjustments [221](#prior-pay-period-adjustments)
Posting/Tour Change [222](#postingtour-change)
Environmental Differential [224](#environmental-differential)
VCS Commission Sales [225](#vcs-commission-sales)
Envir. Diff./VCS Sales [227](#envir.-diff.vcs-sales)
List Environment Diff. Requests [228](#list-environment-diff.-requests-1)
Envir. Diff. Request [229](#envir.-diff.-request)
Cancel Envir. Diff. Request [230](#cancel-envir.-diff.-request)
Post VCS Commission Sales [231](#post-vcs-commission-sales)
List Un-Certified Employees [233](#list-un-certified-employees-2)
Edit OT/CT Request [234](#edit-otct-request)
Chapter 8. Employee Inquiry/Reports Menu [235](#chapter-8.-employee-inquiryreports-menu)
Print Employee Entries [236](#print-employee-entries-1)
Search Employee Entries [237](#search-employee-entries-1)
Ad Hoc Report Generator [238](#ad-hoc-report-generator)
Basic Employee Fields [239](#basic-employee-fields)
Title 38 Employee Fields [242](#title-38-employee-fields)
Physician & Dentist Fields [243](#physician-dentist-fields)
Followup Code Fields [244](#followup-code-fields)
Employee Inquiry [245](#employee-inquiry-1)
Update PAID Codes [246](#update-paid-codes)
Enter/Edit Cost Center/Organization file [247](#enteredit-cost-centerorganization-file)
Compile/Print Strength Report [248](#compileprint-strength-report)
Print Strength Report [256](#print-strength-report)
Review FY Recess for 9 Month AWS Employee [257](#review-fy-recess-for-9-month-aws-employee-3)
Glossary [260](#glossary)
Section 2. Education Tracking [264](#section-2.-education-tracking)
Chapter 1. Package Management [265](#chapter-1.-package-management-1)
Chapter 2: IRM and Package Set-up Menus [284](#chapter-2-irm-and-package-set-up-menus)
Chapter 3: Enter Edit Class Information [312](#chapter-3-enter-edit-class-information)
Chapter 4: Class Registration [351](#chapter-4-class-registration)
Chapter 5: Attendance at Programs [359](#chapter-5-attendance-at-programs)
Chapter 6: Reports [386](#chapter-6-reports)
Glossary [414](#glossary-1)
Appendix A: Supplemental Information for Part-time Physicians (Patch PRS\*4.0\*93) [422](#appendix-a-supplemental-information-for-part-time-physicians-patch-prs4.093)
Appendix B: Upgrade ETA For Telework (Increment 1-Comp Time Expiration Updates) (Patch PRS\*4.0\*133) [514](#appendix-b-upgrade-eta-for-telework-increment-1-comp-time-expiration-updates-patch-prs4.0133)
1 Introduction [1](#introduction)
1.1 Patch Nomenclature [1](#patch-nomenclature)
1.2 Hardware Compatibility [1](#hardware-compatibility)
1.3 System Specifications [1](#system-specifications)
2 Changes and Enhancements [1](#changes-and-enhancements)
2.1 Changes to the Pay Period Display [1](#changes-to-the-pay-period-display)
2.2 Changes to the Comp Time/Credit Hours Balance Display [2](#changes-to-the-comp-timecredit-hours-balance-display)
2.3 Changes to the Supervisory Approvals Function [4](#changes-to-the-supervisory-approvals-function)
3 Support Information [5](#support-information)
> Revision History
<table>
<caption><p>Table :PAID Code Definitions</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 17%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Description (Patch # if applic.)</p>
</blockquote></th>
<th><blockquote>
<p>Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Technical Writer</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11/2008</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRS*4*117, Comp Time for Travel/Nurse Exec Special Pay</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/2007</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRS*4*112, Nurse Alternative Work Schedule (NAWS).</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>02/2007</p>
</blockquote></td>
<td><blockquote>
<p>Added Appendix A ‐ Supplemental Information for Part Time Physicians (Patch PRS*4.0*93)</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Pdf file checked for accessibility to readers with disabilities.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192‐ 352 Displaying Sensitive Data.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2/22/12</p>
</blockquote></td>
<td><blockquote>
<p>Added Appendix B to cover changes included in Patch PRS*4.0*133 (Upgrade ETA for Telework – Comp time); also updated formatting throughout. Document needs extensive additional formatting, editing, and software function description updates to achieve compliance with the latest PMAS templates. Document is not 408 compliant.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5/4/12</td>
<td><blockquote>
<p>Updated UM to cover changes included in Patch PRS*4.0*132. This includes updates to the Employee Menu: Service Record Screen, Display Pay Period; Payroll Main Menu &gt; Employee Inquiry Menu: Print Employee Entries, Search Employee Entries, List/Clear Prior Pay Period Corrections; T&amp;A Supervisor Menu: Supervisory Approvals, Pay Period Certification, Display Employee Tour of Duty, Display Employee Pay Period; Timekeeper Main Menu: Post Employee Time, Display Posted Data, Display Employee Pay Period, Display Employee Tour of Duty, Enter/Edit Employee Tour of Duty, Post/Tour Change; Employee Inquiry/Reports Menu. Also made other general changes to update typos and formatting errors associated with the last conversion from PDF to Microsoft Word.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3/8/2018</td>
<td>Updated to reflect changes from patch PRS*4.0*154, PAID Expenditures Report not working after VATAS. This includes updates to column headers in report examples in chapters 3 and 5. See pages <a href="#expenditures">3.42</a>, <a href="#expenditures-1">5.20</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>
Table :PAID Code Definitions

# Section 1: Time and Attendance (T&A)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Decentralized Hospital Computer Program (DHCP) Personnel and Accounting Integrated Data (PAID) Version 4.0 provides enhanced time and attendance for VA Medical Centers. Of over the 190,000 employees in the Veterans Health Administration (VHA), there are more than 20,000 timekeepers and 30,000 supervisors. Accurate timekeeping and timely Payroll are very important to employees and managers alike. In the past, the data transmission process to the Central PAID System was improved but the data collection and filing system did not change very much. The purpose of this version is to improve the time and attendance data collection methods and reduce the amount of work for timekeepers, Payroll clerks and supervisors. It will also provide a uniform and fair system which will reflect Payroll's policy for every employee across the country. The full implementation of this system will provide efficient time and attendance data collection, reduce errors in posting and processing, reduce the number of adjustments, and provide better service to the employees as well as management. This version also includes an education tracking module featuring programs or classes with multiple attendees and reasons for attending.

The Enhanced Time and Attendance System in the DHCP PAID Version 4.0 includes several functional components. There is an employee time management module, a Time and Leave Unit and tour management module for the Payroll office, a time posting module for the timekeepers, a time and leave certification module for the supervisors, and an overtime management system for the managers. This system does not alter any policies or requirements for time and attendance.

This system will do many functions for each employee of the VHA. The employee time management module provides on-line capability for employees to view their leave balances, request leave, and inquire the status of their leave requests. This access is limited to the employee. These records are kept on-line for three years. Any alterations of these records are automatically recorded. This allows the employee to better manage his/her own leave. It can also shorten the request approval time needed because of the on-line real time processing. The full implementation of this system will also give some employees basic computer skills that are otherwise not part of their jobs. The only possible variation, if the system is not fully implemented (i.e., not everyone has access to DHCP), will be that leave requests for those employees will be kept on a written form since timecards are no longer used.

For the Payroll offices, the time and attendance reports can now be totally accountable. This means that each time and attendance report is audited automatically. All exceptions will be recorded. Exceptions will not be forgotten by the system until all of the corrections are made. The full implementation of this system will drastically reduce the Payroll audit time required and will also ensure the financial integrity of the VHA Payroll process. It is also a tour management system. The system will allow only those legally established tours to be used by the appropriate Time and Leave Units. This further ensures the integrity of our Payroll process. Because of the above reasons, the Payroll turn-in time from each Time and Leave Unit can be delayed, and this will greatly reduce the adjustment time required by the current system. This not only saves time for Payroll offices in the medical centers but also saves a lot of adjustment work for the Central System. Since the adjustment system is a direct cash payment system, this will reduce the risk of error and increase the integrity of our process. Since this system will automatically code all the time elements and provide similar edit checks of the Central Pay System for each record, this will reduce the payrun rejection to practically nothing. It is our understanding that rejects will occur after the implementation of this system only if personnel actions are not filed on time. Therefore, it is imperative that ALL PERSONNEL ACTIONS BE PROCESSED ON TIME. If we can achieve this, the re-submission of rejected time and attendance reports can be eliminated. This also saves Central System the processing time required for these records. It is our estimate that one Payroll processing day can be saved.

There are over 20,000 timekeepers in the VHA trying to keep records for employees every day. There are more than 100 possible codes on the paper timecards currently. The timekeeper manual is written in such a way that frequent interpretations by the Payroll office are required to make certain that the correct code is written on the card. Therefore, to be a good timekeeper, one would require a lot of training. Timekeeper turnover rate is high. This presents Payroll offices with major problems. Inadequately trained timekeepers are a potential threat to the integrity of our Payroll process. This system eliminates almost all of the interpretation of Payroll rules and policies from the timekeepers. The only thing that timekeepers need to do with this system is post the correct time. There are fewer than a dozen time remarks codes that they need to know. If the system is fully implemented (i.e., with electronic leave requests), all leave requests presented will go automatically to the timekeepers to be posted. There is no need to continue with the paper leave requests. This also reduces the number of corrected time and attendance reports because of missing leave requests. If any posting errors are discovered before the reports are transmitted to the Central System, they can be returned to the timekeepers for corrections. All changes to a time and attendance report after forwarding to the next level are recorded.

Supervisors will have a much easier task in the approval or certification of their employees' time and leave requests. For example, in the past when supervisors approved leave, they probably had no idea as to the leave balance of requested employees. This system will provide the leave balance of each category of leave requested. When supervisors are ready to certify time and attendance reports, all 14 days of activities are presented in simple terms on a single screen for each employee in an alphabetical sequence. A single character of "Y" for each report and a final electronic signature will release the reports to Payroll. If there are any exceptions during the certification, they will be presented to the supervisors. One can hold those reports and correct them as needed. According to the supervisors at the test sites, this process does not take any longer than the paper system (some indicated it is shorter) and it is much easier to understand.

For the hospital management team, overtime management is always a challenge. The on-line process of overtime requests and approvals provides a potential means to have a better handle on overtime. This process will allow for the quick turnaround of requests and approvals. Currently, data is collected but a group of hospital managers is needed for further improvement on this part of the system.

We also provide a strength report for the medical centers. This report allows for customization of each hospital. By working with the Austin Automation Center, we have improved the data quality of the employee master file. This effort will be continued in order to satisfy our users.

Overall, DHCP PAID Version 4.0 will revolutionize the time and attendance data collection. It will provide an efficient and fair system for all VHA employees. It will empower employees as well as supervisors to better manage their time and attendance data. It strengthens the integrity and increases the accountability of the Payroll process.

The Education Tracking module creates a database which features the identification of educational programs and inservice training, allows the crediting of attendance at these educational offerings, and generates multiple reports.

The information associated with each class may include:

- Program or class name
- Supplier/presenter
- Type of media used in the presentation
- Location of training
- Purpose of training
- Category of program/class
- Type of training (mandatory inservice, continuing education, etc.)
- Mandatory review group (if a required class)
- Financial agency and cost
- Accreditation GROUP (for continuing education)
- Employer or student expense

The database information is used to complete VA FORM 5-4691 and to manually transmit data to the Austin Automation Center (AAC). The data tracked for this purpose includes: whether the training is financed by the government or the employee, the purpose or reason the employee received the training, whether the training was given by a federal agency or commercial vendor, the number of on- duty and off-duty hours of training, the length of the program or class, direct cost (e.g., tuition, books, supplies), indirect cost (e.g., transportation, lodging, and subsistence), the program category (information about the specific kind of training), program or class title, employee cost, the contact hours (the actual hours spent in class-calculate as on-duty and off duty hours) and whether the training was routine or non-routine.

The education tracking options provide on-line registration, class calendars, registration rosters, and record tracking of all programs or classes that an employee or student has taken. This employee record can be transferred from site to site.

The menu options provide the opportunity to enter a program or class with multiple attendees, saving input time and keyGROUP interaction. The main menu for this application is PRSE-SYS-MGR.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Decentralized Hospital Computer Program (DHCP) Personnel and Accounting Integrated Data (PAID) Version 4.0 provides enhanced time and attendance for VA Medical Centers. Of over 190,000 employees in the Veterans Health Administration (VHA), there are more than 20,000 timekeepers and 30,000 supervisors. Accurate timekeeping and timely Payroll are very important to employees and managers alike. In the past, the data transmission process to the Central PAID System was improved but the data collection and filing system did not change very much. The purpose of this version is to improve the time and attendance data collection methods and reduce the amount of work for timekeepers, Payroll clerks and supervisors. It will also provide a uniform and fair system which will reflect Payroll's policy for every employee across the country. The full implementation of this system will provide efficient time and attendance data collection, reduce errors in posting and processing, reduce the number of adjustments, and provide better service to the employees as well as management. This version also introduces an education tracking module featuring programs or classes with multiple attendees and reasons for attending.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bold print is used throughout this document to represent what you, the user, might enter as a response to a terminal prompt.

The \<RET\> symbol is used to designate the use of the return or enter key. You must press the return or enter key after typing your response. It is the computer's way of knowing that you have finished your response.

Help is always available. Type one question mark to get a help message. Typing two question marks will usually give the user a more detailed help message or a list of possible responses to choose from.

The up/down arrow keys may be used to advance through certain screens, i.e., Tour of Duty screen, Time and Leave Unit (T&L) screen, etc. Enter two question marks at any prompt for help or a list of choices, when entering data.

The ^ symbol is known as the up-arrow or caret. It is created by holding down the shift key and pressing the number 6 key. The up-arrow tells the computer you want to exit from whatever you are doing.

At times you will see a response generated by the program and followed by two slash marks (e.g., LASTNAME,FIRSTNAME//). This is called a default response. If the default response is the answer you want, then you need only press the return key. Otherwise, type the response you wish or type one or more question marks for a help message.

## Chapter 1. Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Employee master record data is available for viewing only by the employee and authorized individuals in Fiscal and Personnel Services with access to the system.

The Offices of Budget Finance and Information Resource Management and Personnel and Labor Relations have the responsibility for the policies and procedures which govern the Payroll and Personnel data used in this program. (See Veterans Health Administration (VHA) Circular, Distribution of Security Codes for DM&S ADP Systems Processing Sensitive Data, 10-89-2 (see updated version)). This circular defines procedures for the generation, distribution and handling of user access for all VHA systems which process sensitive data such as Payroll and Personnel information.

Privacy Act Statement

In accordance with the Office of Personnel Management and VA policies, this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

#### Edit Electronic Signature Codes

An electronic signature code is necessary to approve overtime and compensatory (OT/CT) requests, environmental differential pay requests, leave requests, Veterans Canteen Service (VCS) commission sales, tour of duty changes and to certify a time and attendance report.

If you already have an electronic signature code you may use it to perform your time and attendance duties. If you do not have one or wish to change your present one, you may create/change one yourself. The menu option to do this is on your secondary menu. It is called User's Toolbox. An example of how to create an electronic signature is provided below. The code can be any combination of letters or numbers and it must be at least six characters long. You can even use your DHCP ACCESS or VERIFY codes if you like. Like your ACCESS and VERIFY codes, you must not tell anyone what your electronic signature code is.

> Select T&A Supervisor Menu Option: TB \<RET\> User's Toolbox

> Display User Characteristics Edit Electronic Signature code Edit User Characteristics

> Menu Templates ... Spooler Menu ... TaskMan User

> User Help

> Select User's Toolbox Option: EDIT E \<RET\> Edit Electronic Signature code This option is designed to permit you to enter or change your Initials, Signature Block Information and Office Phone number. In addition, you are permitted to enter a new Electronic Signature Code or to change an existing code.

> INITIAL: EB// \<RET\>

> SIGNATURE BLOCK PRINTED NAME: PAIDUSER,ONE// \<RET\>

> SIGNATURE BLOCK TITLE: SECRETARY// \<RET\>

> OFFICE PHONE: (708)786-0000 \<RET\>

> Enter your Signature Code: SIGNATURE VERIFIED ENTER NEW SIGNATURE CODE:

> RE-ENTER SIGNATURE CODE FOR VERIFICATION:

> DONE

#### Using Screens for Data Entry

Until recently, data entry sessions in DHCP operated in a "scrolling" mode format only. In scrolling format, fields are displayed one after the other, line-by­ line, with each line rolling up and off the 24-line screen as the user hits the RETURN key.

This package uses the scrolling format AND a new, screen-oriented approach. With the screen-oriented format, up to 17 lines of data can be displayed and the data fields will not change positions on your terminal screen. Here is an

example of this new, screen-oriented approach (screens) to display and edit data. The bold type is a data value for the field listed to the left.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>VA TIME &amp; ATTENDANCE SYSTEM TIME &amp; LEAVE UNIT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><u>CODE</u>: NAME: <u>STATION #</u> SERVICE:</p>
</blockquote></td>
<td><blockquote>
<p><strong>103</strong></p>
<p><strong>TEST</strong></p>
<p><strong>123</strong></p>
<p><strong>ISC</strong></p>
</blockquote></td>
<td><blockquote>
<p>SECTION: <strong>DEVELOPMENT</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Time SleepTime Begins</u>: 10:00PM

> <u>Entitled Sat/Sun Premiums?</u> NO

> Select TIMEKEEPER: PAIDTIMEKPR,ONE Select SUPERVISOR: PAIDSUPERVISR,ONE Select OT/CT APPROVER: PAIDTIMEMGR,ONE Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: INSERT

Displaying and editing data with screens has advantages. You can:

1.  See several data fields displayed at one time,
2.  See data fields displayed in the same location, and
3.  Easily jump ahead or return to a field for correction.

There are two types of screens, Display and Edit. Display screens display data, but do not allow you to change any data. Edit screens display data and allow you to enter data and edit existing data. Each screen has two sections, a Display/Edit area and a Command area.

#### Display/Edit Area

The top portion of the Display/Edit area is a "header block" which displays a screen title and is for display only. From our example it is:

> VA TIME & ATTENDANCE SYSTEM TIME & LEAVE UNIT

The rest of the Display/Edit area shows data fields and their values. Edit screens allow data to be changed. Display screens merely display data with no editing allowed. The Display/Edit area from our example is:

> <u>CODE</u>: 103

> NAME: TEST

> <u>STATION \#</u> 123

> SERVICE: ISC SECTION: DEVELOPMENT

> <u>Time SleepTime Begins</u>: 10:00PM

> <u>Entitled Sat/Sun Premiums</u>? NO

> Select TIMEKEEPER: PAIDTIMEKPR,ONE Select SUPERVISOR: PAIDSUPERVISR,ONE Select OT/CT APPROVER: PAIDTIMEMGR,ONE

Your position on the screen is shown by a highlighted box (cursor). When you first enter a screen, the cursor will go to the first field where you may enter data. You can "navigate" through a screen by using several keys from your terminal's keyGROUP.

On your keyGROUP there are four arrow keys; left, right, up and down. The up arrow key will take you to the field above and the down arrow will take you to the field below where the cursor is. The left and right arrow keys move the cursor to the left or right within the same field.

The TAB key and RETURN key will move the cursor to the next field.

Type a caret (^) followed by a field name (e.g., ^SERVICE) and the cursor will move to that field.

Type a caret only and the cursor will move to the Command area.

To enter or edit data in a field, move the cursor to the field, type in the data value and press the RETURN key. Type one or more question marks for a help response. The help response will appear in the Command area (i.e., at the bottom of the screen).

#### Command Area

The Command area allows you to issue commands for exiting and saving changes. Messages and help text are also displayed in the Command area. The Command area from our example is:

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window.

> COMMAND: INSERT

When you type EXIT in the COMMAND field, you are asked if you wish to save any changes that you made. If you answer YES, the changes will be saved and then you will exit the screen. If you answer NO, the changes will not be saved and you will exit the screen.

If you type Save in the COMMAND field, your changes will be saved and you will

NOT exit the screen. You may then move the cursor back to a field and make more changes.

Type REFRESH in the COMMAND field if the screen display becomes garbled. This will "re-paint'" the screen to how it is supposed to look.

When you save changes, the data is checked for errors. If an error exists, the changes will NOT be saved and an error message will appear. You will then be able to edit your responses. You cannot save changes that have an error.

#### Pop-up Pages

Some data fields allow multiple values to be entered and saved. In our example a Time and Leave Unit may have more than one Timekeeper, Supervisor or Overtime/Compensatory Time Approving Official. When you wish to enter or edit a value in such a field, a "pop-up page" appears on the screen. A pop-up page is surrounded by lines that form a box on the screen. The pop-up page covers only a portion of the screen. After you have finished entering data in the pop-up page, it will disappear and the original page will remain. Unlike the other data fields, the pop-up page data fields make changes as entered. You exit a pop-up by typing CLOSE in the COMMAND field (CLOSE is the default).

## Chapter 2. Employee Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu is available to any employee with access to any DHCP application. It allows an employee to enter, cancel or display his/her requests for leave. The employee may also display his/her leave balances. DHCP ACCESS and VERIFY codes identify the employee to the system, causing only that employee's information to display. No employee may obtain access to another employee's data through this menu option.

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

PRIVACY ACT STATEMENT

In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

1 Leave Request

2 Leave Balances

3 Display Leave Requests

4 Cancel Leave Request

5 Service Record Screen

6 Display Pay Period

8 Edit Leave Request

9 Display Leave Used

10 Monthly Calendar

Select Employee Menu Option:

#### Leave Request

This option allows an employee to enter a request for leave (i.e., APPLICATION FOR LEAVE, SF 71). If the employee requests more leave than he/she has accumulated, a warning message will appear. (The leave for Family Care (CB) and Adoption (AD) will be deducted from the employee's Sick Leave (SL) by the Austin Automation Center.)

> Select Employee Menu Option: 1 \<RET\> Leave Request

> VA TIME & ATTENDANCE SYSTEM REQUEST FOR LEAVE

> PAIDTIMEKEEPR,ONE 000-00-0001

> <u>From Date</u>: JUL 05, 1995 \<RET\> <u>Time</u>: 08:00AM \<RET\>

> <u>To Date</u>: JUL 07, 1995 \<RET\> <u>Time</u>: 04:30PM \<RET\>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 7%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AL</p>
</blockquote></th>
<th><blockquote>
<p>Annual Leave</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>AA</p>
</blockquote></th>
<th><blockquote>
<p>Authorized Absence</p>
</blockquote></th>
<th><blockquote>
<p>CB</p>
</blockquote></th>
<th><blockquote>
<p>Family Care</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Sick Leave</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>Military Leave</p>
</blockquote></td>
<td><blockquote>
<p>AD</p>
</blockquote></td>
<td><blockquote>
<p>Adoption</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>Without Pay</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>Restored Annual Leave</p>
</blockquote></td>
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>Donor Leave</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CU</p>
</blockquote></td>
<td><blockquote>
<p>Compensatory</p>
</blockquote></td>
<td><blockquote>
<p>Time</p>
</blockquote></td>
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay Annual Leave</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <u>Type of Leave</u>: SL \<RET\> Sick Leave <u>Number of Hours</u>: 24

> Remarks: Outpatient Surgery \<RET\>

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field. COMMAND: ?? \<RET\> Press \<PF1\>H for help Insert Exit - Exit the form.

> Save - Save all changes made during the edit session.

> Refresh - Repaint the screen.

> COMMAND: E \<RET\>

> Save changes before leaving form (Y/N)? ?? \<RET\> Press \<PF1\>H for help

Insert

> Enter 'Y' to save before exiting.

> Enter 'N' or '^' to exit without saving.

> Press 'RETURN' to return to form.

> Save changes before leaving form (Y/N)? Y \<RET\>

> Do you wish to enter another Leave Request? No// N \<RET\>

#### Leave Balances

This option displays all of the leave that an employee has accrued. The values are current as of the date shown on the screen.

Compensatory Time (Comp Time): Time off in an amount equal to the overtime worked in lieu of overtime pay.

Restored Leave: Annual Leave that has been credited to a restored leave account (employee was prevented from using the leave due to illness or the exigencies of the service). This leave must be used during the next two leave years.

The number "4" in front of "Restored Leave" below means that the leave must be used by the end of calendar year 1994.

> Select Employee Menu Option: 2 \<RET\> Leave Balances

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> EMPLOYEE LEAVE BALANCES

> PAIDTIMEKEEPR,ONE 000-00-0001

> Balances are as of Sat 10-Dec-94

> Leave Group: 3

> Annual Leave Balance: 293.000

> Sick Leave Balance: 403.250

> Comp Time: 10.000 must be used by 24-Dec-94

> 4 Restored Leave: 40.000

> Press RETURN to Continue. \<RET\>

#### Display Leave Requests

With this option the employee enters a date and a list of all of his/her leave requests from that date onward is displayed. Cancelled leave requests will not show on the list.

> Select Employee Menu Option: 3 \<RET\> Display Leave Request

> VA TIME & ATTENDANCE SYSTEM LEAVE REQUESTS

> PAIDTIMEKEEPR,ONE 000-00-0001

> Begin with Date: T// \<RET\> (AUG 09, 1994)

> 08:00A 8-May-95 to 04:30P 12-May-95 40 hrs Annual Leave Cancelled

> Supr: Please wait until beginning of 1995 to request.

> 08:00A 15-Aug-94 to 04:30P 19-Aug-94 40 hrs Annual Leave Approved

> 08:00A 12-Aug-94 to 04:30P 12-Aug-94 8 hrs Annual Leave Approved

> Press RETURN to Continue. \<RET\>

#### Cancel Leave Request

With this option the employee enters a date and a list of all employees’ leave requests from that date onward is displayed. The employee is prompted to select a choice from the list to cancel.

> Select Employee Menu Option: 4 \<RET\> Cancel Leave Request

> VA TIME & ATTENDANCE SYSTEM CANCEL LEAVE REQUESTS

> PAIDTIMEKEEPR,ONE 000-00-0001

> Begin with Date: T// \<RET\> (AUG 22, 1994)

> 1 08:00A 31-Aug-94 to 04:30P 31-Aug-94 8 hrs Sick Leave Requested

> 2 08:00A 26-Aug-94 to NOON 26-Aug-94 4 hrs Annual Leave Requested

> 3 08:00A 22-Aug-94 to 04:30P 22-Aug-94 Annual Leave Requested

> Cancel Which Request \#? 2 ... done

#### Service Record Screen

Selecting this option will display all of the employee's current service record data.

> Select Employee Menu Option: 5 \<RET\> Service Record Screen

> ...HMMM, LET ME THINK ABOUT THAT A MOMENT...

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 34%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE,ONE</p>
</blockquote></th>
<th><blockquote>
<p>RECREATION</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0001</p>
</blockquote></td>
<td></td>
<td>T&amp;L: 100</td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> LAST PP: 04 SERVICE RECORD SCREEN PAGE 1

> ------------------------------------------------------------------------------

> OCCUPATION SERIES & TITLE.......NURSING ASSISTANT

> PAY PLAN........................GS/CA/SL/GW

> OCCUPATION SERIES CODE..........0621

> GRADE...........................04

> STEP............................02

> SALARY..........................28,922.00

> GAP/LOCALITY PAY AMT............3,587.00

> POSITION NUMBER.................03167A

> ASSIGNMENT......................NONE

> COMPETITIVE LEVEL...............X01

> DUTY BASIS......................FULL-TIME

> NORMAL HOURS....................80.00

> PAY BASIS.......................PER ANNUM

> PAY RATE DETERMINANT............REGULAR RATE

> FLSA............................NON-EXEMPT (COVERED)

> LABOR DIST CODE-1 COST CTR/ORG..8207:2125

> Press RETURN to continue: \<RET\>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE,ONE</p>
</blockquote></th>
<th><blockquote>
<p>RECREATION</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0001</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>T&amp;L: 100</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> LAST PP: 04 SERVICE RECORD SCREEN PAGE 2

> ------------------------------------------------------------------------------

> TYPE OF APPOINTMENT.............CAREER CONDITIONAL

> SUPERVISORY LEVEL...............0

> BUS CODE........................1272

> DATE OF BIRTH...................AUG 07, 1989

> SEX.............................MALE

> CITIZENSHIP.....................U.S. CITIZEN

> VETERANS PREFERENCE.............NONE

> EDUCATION.......................SOME HIGH SCHOOL

> FEGLI CODE......................Basic only

> HEALTH INSURANCE................111

> RETIREMENT CODE.................FERS

> PERF/PROFCY RATING CODE.........Fully Successful

> SERVICE COMPUTATION DATE........NOV 09, 2008

> STATION EOD.....................NOV 09, 2008

> TELEWORK INDICATOR..............Employee regularly teleworks three or more

days per work week.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 34%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE,ONE</p>
</blockquote></th>
<th><blockquote>
<p>RECREATION</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0001</p>
</blockquote></td>
<td></td>
<td>T&amp;L: 100</td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> LAST PP: 21 FOLLOWUPS PAGE 3

> ------------------------------------------------------------------------------

> ELIGIBLE FOR DRUG TESTING.......DT

> CONVERSION TO CAREER TENURE.....NOV 09, 2011

> FOLLOWUP CODE S\*................NOV 09, 2011

> ELIGIBLE FOR DRUG TESTING.......DT

> FOLLOWUP CODE 31................NOV 09, 2011

> FOLLOWUP CODE 43................NOV 09, 2011

> FOLLOWUP CODE 48................NOV 09, 2011

> Press RETURN to continue:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 34%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE,ONE</p>
</blockquote></th>
<th><blockquote>
<p>RECREATION</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0001</p>
</blockquote></td>
<td></td>
<td>T&amp;L: 100</td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> LAST PP: 21 THRIFT SAVINGS PLAN PAGE 4

> ------------------------------------------------------------------------------

> TSP STATUS......................ELIGIBLE

> TSP STATUS DATE.................JUN 07, 2009

> TSP SERVICE COMPU DATE..........NOV 09, 2008

> TSP ELIG........................JUN 01, 2009

> TSP VESTING.....................3

> TSP MASTER RECORD IND...........YES

> TSP GSF GOV BASIC CONTRIB.......11.09

> Press RETURN to continue:

#### Display Pay Period

With this option, the user can view his or her time and attendance record for a particular pay period. By entering any date within a pay period, the "scheduled tour" and "tour exceptions" (leave used, OT earned, etc.) will be displayed for each day within that pay period. Also, in this example, the employee is eligible for telework, and has worked telework hours, as indicated by the “Telework Ind:” label (the complete list of telework codes is shown in Table 1). The employee’s regularly scheduled tour of duty includes telework time on Thursday and Friday of each week. The “TW” column represents telework type: either “REG” (Regular Scheduled Telework) or “MED” (Medical Scheduled Telework).

> Select Employee Menu Option: 6 \<RET\> Display Pay Period

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE PAY PERIOD DATA

> Posting Date: 5/1 (MAY 01, 2012)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

PAIDEMPLOYEE,ONE T&L 110 Telework Ind: P XXX-XX-1114

Date TW Scheduled Tour Tour Exceptions

------------------------------------------------------------------------

Sun 6-May-12 Day Off

Mon 7-May-12 07:00A-03:30P

Tue 8-May-12 07:00A-03:30P

Wed 9-May-12 07:00A-03:30P

Thu 10-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 11-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 12-May-12 Day Off

Sun 13-May-12 Day Off

Mon 14-May-12 07:00A-03:30P

Tue 15-May-12 07:00A-03:30P

Wed 16-May-12 07:00A-03:30P

Thu 17-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 18-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 19-May-12 Day Off

Press RETURN to Continue.

| Code  | Definition                                                                                                                                                                                                                        |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P     | Employee regularly teleworks three or more days per pay period.                                                                                                                                                                   |
| R     | Employee regularly teleworks one or two days per pay period.                                                                                                                                                                      |
| S     | Employee regularly teleworks one day per month.                                                                                                                                                                                   |
| A     | Ad Hoc Telework. Employee teleworks only on an as-needed basis. This includes Continuity of Operations (COOP), National/Regional emergencies, situational basis (temporary), and Office of Workers Compensation-related telework. |
| X     | Position is suitable for telework and employee is eligible, but no telework agreement is in place.                                                                                                                                |
| Y     | Position is suitable for telework, but employee is not eligible to telework.                                                                                                                                                      |
| Z     | Position is not suitable for telework. This code is used only when the employee's position makes teleworking impossible.                                                                                                          |
| V     | Employee who is virtual.                                                                                                                                                                                                          |
| E     | Employee regularly teleworks three or more days per work week.                                                                                                                                                                    |
| Blank | Default. No telework code has been entered.                                                                                                                                                                                       |

Table 1: PAID Code Definitions

#### Self Registration Enter/Edit

This option allows an employee to self-register for a class. The user may self register for present or future classes, open classes that are sponsored by any service, closed classes within his/her own service, and mandatory classes that are required. An individual does not need to preregister for class attendance to be taken. Names of individuals that are registered for classes can be printed through the Class Registration Roster report.

> Select Employee Menu Option: 7 \<RET\> Self Registration Enter/Edit

> Select one of the following:

> R Class Registration Calendar Report

> S Student Registration

> Choose a Selection from the above choices: S \<RET\> Student Registration

> Select one of the following:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>Mandatory Training (MI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Continuing Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Other/Miscellaneous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Sort Parameter: M \<RET\> Mandatory Training (MI) CLASS NAME: ?? \<RET\>

> CHOOSE FROM:

> BASICS OF INTERPLANETARY SPACE TRAVEL RESEARCH

> INFECTION CONTROL NURSING

> CLASS NAME: I \<RET\> INFECTION CONTROL NURSING Select DATE: MAY 12, 1995// \<RET\> MAY 12, 1995

> Enter STUDENT NAME: PAIDEMPLOYEE,ONE \<RET\> PAIDEMPLOYEE,and ONE ISC SMART, EXNAME is currently Registered for this INFECTION CONTROL Class! Do you want to delete this record? NO// \<RET\> (NO)

> To add your name to the registration list:

> Enter STUDENT NAME: PAIDEMPLOYEE,THREE \<RET\> PAIDEMPLOYEE,THREE DENTAL Do you want to register PAIDEMPLOYEE,THREE - DENTAL for

> INFECTION CONTROL? YES// \<RET\> (YES)

To delete your name from the registration list:

> CLASS NAME: I \<RET\> INFECTION CONTROL NURSING Select DATE: MAY 12, 1995// \<RET\> MAY 12, 1995

> Enter STUDENT NAME: PAIDEMPLOYEE,TWO \<RET\> PAIDEMPLOYEE,TWO ISC PAIDEMPLOYEE,TWO is currently Registered for this INFECTION CONTROL Class! Do you want to delete this record? NO// Y \<RET\>

> PAIDEMPLOYEE,TWO \*\*DELETED\*\*

> Enter STUDENT NAME: ^ \<RET\>

#### Edit Leave Request

This option allows the employee to make changes to any request that the timekeeper has not posted.

> Select Employee Menu Option: 8 \<RET\> Edit Leave Request

> VA TIME & ATTENDANCE SYSTEM EDIT LEAVE REQUESTS

> PAIDTIMEKEEPR,ONE 000-00-0001

> 1 08:00A 14-Jul-95 to 04:30P 14-Jul-95 8 hrs Authorized Absence Requested

> Attending Seminar.

> 2 08:00A 11-Jul-95 to 12:30P 11-Jul-95 4.5 hrs Annual Leave Requested

> Lunch is 12:30P - 01:00P.

> 3 01:30P 10-Jul-95 to 04:30P 10-Jul-95 3 hrs Sick Leave Requested

> Edit Which Request \#? 1 \<RET\>

> VA TIME & ATTENDANCE SYSTEM REQUEST FOR LEAVE

> PAIDTIMEKEEPR,ONE 000-00-0001

> <u>From Date</u>: JUL 14, 1995 \<RET\> <u>Time</u>: 01:00PM \<RET\>

> <u>To Date</u>: JUL 14, 1995 \<RET\> <u>Time</u>: 04:30PM \<RET\>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 7%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AL</p>
</blockquote></th>
<th><blockquote>
<p>Annual Leave</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>AA</p>
</blockquote></th>
<th><blockquote>
<p>Authorized Absence</p>
</blockquote></th>
<th><blockquote>
<p>CB</p>
</blockquote></th>
<th><blockquote>
<p>Family Care</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Sick Leave</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>Military Leave</p>
</blockquote></td>
<td><blockquote>
<p>AD</p>
</blockquote></td>
<td><blockquote>
<p>Adoption</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>Without Pay</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>Restored Annual Leave</p>
</blockquote></td>
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>Donor Leave</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CU</p>
</blockquote></td>
<td><blockquote>
<p>Compensatory</p>
</blockquote></td>
<td><blockquote>
<p>Time</p>
</blockquote></td>
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay Annual Leave</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <u>Type of Leave</u>: AA \<RET\> Authorized Absence <u>Number of Hours</u>: 3.5

> Remarks: Attending Seminar \<RET\>

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

#### Display Leave Used

This option allows the employee to view all of his/her leave that has been used for a selected date range.

> Select Employee Menu Option: 9 \<RET\> Display Leave Used

> Report Beginning Date T//1/1/95 \<RET\> (JAN 01, 1995) Report Ending Date T//4/01/95 \<RET\> (APR 01, 1995)

> ..............................

> LEAVE USED SUMMARY DATE: 08/02/95 from: JAN 01, 1995 to APR 01, 1995

> for: PAIDEMPLOYEE,FOUR - IRM

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> \|PP \|DATE \|TYPE \|FROM \|TO \|LENGTH

> \|

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> \|26 \|Tue 3-Jan-95 \|Annual Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \|01 \|Tue 10-Jan-95 \|Sick Leave \|08:00A \|NOON \| 4.00 Hours

> \|

> \| \| \|Annual Leave \|12:30P \|04:30P \| 4.00 Hours

> \|

> \| \|Fri 13-Jan-95 \|Annual Leave \|08:00A \|08:30A \| 0.50 Hours

> \|

> \|03 \|Thu 9-Feb-95 \|Annual Leave \|08:00A \|11:30A \| 3.50 Hours

> \|

> \| \|Mon 13-Feb-95 \|Sick Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \|04 \|Mon 27-Feb-95 \|Annual Leave \|08:00A \|08:45A \| 0.75 Hours

> \|

> \| \|Tue 28-Feb-95 \|Sick Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \| \|Fri 3-Mar-95 \|Sick Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \|05 \|Tue 14-Mar-95 \|Sick Leave \|02:30P \|04:30P \| 2.00 Hours

> \|

> \|06 \|Wed 22-Mar-95 \|Annual Leave \|01:30P \|04:30P \| 3.00 Hours

> \|

> \| \|Fri 24-Mar-95 \|Annual Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \| \|Fri 31-Mar-95 \|Annual Leave \|03:30P \|04:30P \| 1.00 Hour

> \|

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> DHCP PAID REPORT L003 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

> Press Return/Enter to continue or "^" to quit. ^ \<RET\>

#### Review FY Recess for 9 Month AWS Employee

The PRSAWS9 Security Key is required to access this option.

This view only option displays the Recess Schedule for nurses on the 9 month/3 month alternate work schedule (AWS). To view a 9 month/3 month AWS Recess Schedule, enter the fiscal year or the nurse’s name.

Once the schedule is selected, you may enter actions at the “Select Action” prompt to navigate through the Recess Schedule, print the Recess Schedule and display a summary. Enter a double question mark (??) at this prompt for a list of all available actions.

Following is a list of actions available through this option with a brief description. The mnemonic for each action is shown in brackets \[ \] following the action name. Entering the mnemonic is the quickest way to select an action.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recess Hours Summary</p>
<p>[RS]</p>
</blockquote></td>
<td><blockquote>
<p>Enter RS to see a summary screen with recess totals. Be sure to scroll down to see the whole</p>
<p>report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Next Screen [+]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Previous Screen [-]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the previous screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Up a Line [UP]</p>
</blockquote></td>
<td><blockquote>
<p>Move up one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Down a Line [DN]</p>
</blockquote></td>
<td><blockquote>
<p>Move down one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Right [&gt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the right if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Left [&lt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the left if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>First Screen [FS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the first screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Last Screen [LS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the last screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Go to Page [GO]</p>
</blockquote></td>
<td><blockquote>
<p>Move to any selected page in the list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Re Display Screen [RD]</p>
</blockquote></th>
<th><blockquote>
<p>Redisplay the current screen.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print Screen [PS]</p>
</blockquote></td>
<td><blockquote>
<p>Print the header and the portion of the list currently displayed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print List [PL]</p>
</blockquote></td>
<td><blockquote>
<p>Print the list of entries currently displayed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Search List [SL]</p>
</blockquote></td>
<td><blockquote>
<p>Find selected text in list of entries.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Auto Display(On/Off) [ADPL]</p>
</blockquote></td>
<td><blockquote>
<p>Toggle the menu of actions to be displayed/not displayed automatically.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Quit [QU]</p>
</blockquote></td>
<td><blockquote>
<p>Exit the screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Employee Menu Option: Review FY Recess for 9 Month AWS Employee

> Select a Recess Schedule: 2007// \<RET\> PAIDemployee,One 2007 000-00-1111

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Recess</p>
</blockquote></th>
<th><blockquote>
<p>Schedule Viewer</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Jul 17, 2007@14:38:58</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1 of 4</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FY2007</p>
</blockquote></td>
<td><blockquote>
<p>Recess Week Viewer</p>
</blockquote></td>
<td><blockquote>
<p>for</p>
</blockquote></td>
<td><blockquote>
<p>9 month AWS with start</p>
</blockquote></td>
<td><blockquote>
<p>date 1</p>
</blockquote></td>
<td>0/01/06 (</td>
<td>pp 06-20)</td>
</tr>
</tbody>
</table>

> PAIDemployee,One XXX-XX-1111 T&L Unit: 140

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Oct 2006============

> 1 06-20 1 2 3 4 5 6 7 40.00

> 2 8 9 10 11 12 13 14

> 3 06-21 15 16 17 18 19 20 21

> 4 22 23 24 25 26 27 28

> 5 06-22 29 30 31 1 2 3 4 40.00

> =============Nov 2006============

> 6 5 6 7 8 9 10 11 7.00

> 7 06-23 12 13 14 15 16 17 18 40.00

> 8 19 20 21 22 23 24 25

> 9 06-24 26 27 28 29 30 1 2 40.00

> =============Dec 2006============

> 10 3 4 5 6 7 8 9

> 11 06-25 10 11 12 13 14 15 16

> 12 17 18 19 20 21 22 23

> 13 06-26 24 25 26 27 28 29 30

> 14 31 1 2 3 4 5 6

> +---------Enter ?? for more actions-------------------------------------------- RS Recess Hours Summary

> Select Action:Next Screen// rs Recess Hours Summary

> RECESS SCHEDULE SUMMARY Jul 17, 2007@14:39:01 Page: 1 of 1

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-1111 T&L Unit: 140

> --Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------

> 1 10/01/06 40.00 0.00

> 5 10/29/06 40.00 0.00

> 6 11/05/06 7.00 0.00

> 7 11/12/06 40.00 0.00

> 9 11/26/06 40.00 0.00

> 27 04/01/07 40.00 0.00

> 28 04/08/07 40.00 0.00

> ====== ====== Total Recess. Scheduled: 247.00 Posted: 0.00

> Total Weeks in AWS FY Schedule: 54.00

> Total available FY recess hrs: 540.00 (13.5 weeks) WARNING--Recess hours under scheduled: 293.00

> ----------WARNING--Recess hours are under scheduled: 293.00--------------------

## Chapter 3. Payroll Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options that a Payroll Clerk needs to perform time and attendance related tasks.

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

| 1 Exceptions and Corrections ...                   | Exceptions and Corrections ...                  |
|----------------------------------------------------|-------------------------------------------------|
| 2 Display Employee Pay Period                      | Display Employee Pay Period                     |
| 3 Return Record to Timekeeper                      | Return Record to Timekeeper                     |
| 4 Display Employee Entitlements                    | Display Employee Entitlements                   |
| 5 Post Miscellaneous Data                          | Post Miscellaneous Data                         |
| 6 Tour of Duty Management ...                      | Tour of Duty Management ...                     |
| 7 T&L Management ...                               | T&L Management ...                              |
| 8 Create Employee Record for Pay Period            | Create Employee Record for Pay Period           |
| 9 Employee Inquiry Menu ...                        | Employee Inquiry Menu ...                       |
| 10 Change Employee T&L Unit                        | Change Employee T&L Unit                        |
| 11 List Un-Certified Employees                     | List Un-Certified Employees                     |
| 12 List Leave Requests                             | List Leave Requests                             |
| 13 List OT and CT/CH Requests                      | List OT and CT/CH Requests                      |
| 14 Display Complete Request/Pay Period Records ... | Display Complete Request/Pay Period Records ... |
| 15 Employee Reports ...                            | Employee Reports ...                            |
| 16 PT Physician Menu ...                           | PT Physician Menu ...                           |
|                                                    |                                                 |
| Select Payroll Main Menu Option:                   |                                                 |

#### Pay Period Exceptions

This option displays a list of each employee's time and attendance reporting problems for a selected pay period that needs to be resolved. The name of the employee, T&L, day and date, and a short description of the exception are displayed.

Payroll offices should use this option throughout the pay period cycle to check timekeepers' progress. If time is not being posted or the exceptions are not being resolved promptly, the Payroll office should contact the timekeeper to assess the problem. We strongly suggest that this option be selected several times throughout the pay period until timekeepers become familiar with the system.

Similar to this option is "List Prior Pay Period Exceptions" which lists all exceptions for all records released to Payroll for all previous pay periods while this option lists only exceptions for a specific pay period.

> Select Payroll Main Menu Option: 1 \<RET\> Pay Period Exceptions

> Select PAY PERIOD: 93-03 \<RET\>

> Select T&L Unit (or ALL): 007 \<RET\>

> Select Device: Home// \<RET\> ANYWHERE Right Margin: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> Sun 7-Feb-93 to Sat 20-Feb-93

> PAIDEMPLOYEE,FIVE (007)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 6%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Fri</p>
</blockquote></th>
<th><blockquote>
<p>1-Jul-94</p>
</blockquote></th>
<th><blockquote>
<p>03:30P</p>
</blockquote></th>
<th><blockquote>
<p>SL</p>
</blockquote></th>
<th><blockquote>
<p>Requested but not Approved</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>6-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>01:30P</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>not Requested</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>9-Jul-94</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Time Posted</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PAIDEMPLOYEE,SIX (007)

> Mon 27-Jun-94 No Time Posted

> Fri 1-Jul-94 07:00A AL not Requested

> Tue 5-Jul-94 No Time Posted

> PAIDEMPLOYEE,SEVEN (007)

> Tue 28-Jun-94 No Time Posted

> Wed 29-Jun-94 No Time Posted

> Thu 30-Jun-94 No Time Posted

> Fri 1-Jul-94 No Time Posted

> Tue 5-Jul-94 No Time Posted

> Wed 6-Jul-94 No Time Posted

> Thu 7-Jul-94 No Time Posted

> Press RETURN to Continue. \<RET\>

#### Display Employee Pay Period

This option displays the employee's name, all 14 dates in the pay period, the employee's scheduled tour(s) of duty and any exceptions to the scheduled tour(s).

> Select Payroll Main Menu Option: 2 \<RET\> Display Employee Pay Period

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE PAY PERIOD DATA

> Select EMPLOYEE: PAIDEMPLOYEE,EIGHT \<RET\> 000-00-0008

> Select PAY PERIOD: 94-14 \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> PAIDEMPLOYEE,EIGHT T&L 100 000-00-0008

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 6%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Sun</p>
</blockquote></th>
<th><blockquote>
<p>10-Jul-94</p>
</blockquote></th>
<th><blockquote>
<p>Day Off</p>
</blockquote></th>
<th></th>
<th colspan="3" rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Mon</p>
</blockquote></th>
<th><blockquote>
<p>11-Jul-94</p>
</blockquote></th>
<th><blockquote>
<p>09:00A-05:30P</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>06:00P-08:00P</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th><blockquote>
<p>Scheduled Comp</p>
</blockquote></th>
<th><blockquote>
<p>Time</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Tue</p>
</blockquote></th>
<th><blockquote>
<p>12-Jul-94</p>
</blockquote></th>
<th><blockquote>
<p>09:00A-05:30P</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th><blockquote>
<p>06:00P-08:00P</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>Scheduled Comp</p>
</blockquote></th>
<th><blockquote>
<p>Time</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>13-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>09:00A-05:30P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>09:00A-NOON</p>
</blockquote></td>
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>SICK LV</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>06:00P-08:00P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>12:30P-05:30P</p>
</blockquote></td>
<td><blockquote>
<p>AL</p>
</blockquote></td>
<td><blockquote>
<p>ANNUAL LV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Scheduled Comp</p>
</blockquote></td>
<td><blockquote>
<p>Time</p>
</blockquote></td>
<td><blockquote>
<p>06:00P-08:00P</p>
</blockquote></td>
<td><blockquote>
<p>UN</p>
</blockquote></td>
<td><blockquote>
<p>UNAVAIL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>14-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>15-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>16-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td><blockquote>
<p>17-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mon</p>
</blockquote></td>
<td><blockquote>
<p>18-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>19-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>20-Jul-94</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>04:30P-06:30P</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td><blockquote>
<p>COMP ERND</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>08:30P-10:30P</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>OVERTIME</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to Continue. \<RET\>

> PAIDEMPLOYEE,EIGHT 000-00-0008

> Thu 21-Jul-94 08:00A-04:30P Fri 22-Jul-94 08:00A-04:30P Sat 23-Jul-94 Day Off

> Wed 13-Jul-94 09:00A SL Requested but not Approved

> Wed 13-Jul-94 12:30P AL Requested but not Approved

> Wed 20-Jul-94 04:30P CT Requested but pending Supervisor Approval

> Wed 20-Jul-94 08:30P OT Requested but pending Supervisor Approval

> Select EMPLOYEE: \<RET\>

#### Return Record to Timekeeper

This option allows Payroll to return a time and attendance report to the timekeeper for corrections. Once a time and attendance report has been corrected the supervisor must recertify the record and Payroll must then transmit or retransmit the record to Austin. This option should only be used if the intent is to transmit the corrected record to Austin. If it is too late to transmit the corrected record, do not use this option. The timekeeper must use the Prior Pay Period Adjustments option to make time and attendance report corrections.

> **NOTE:** Once a time and attendance report has been returned to the timekeeper, it must be recertified by the supervisor. This is true even if no changes have been made to the record.

> Select Payroll Main Menu Option: 3 \<RET\> Return Record to Timekeeper

> Select Pay Period: 92-23 \<RET\>

> Select Employee: PAIDEMPLOYEE,NINE \<RET\> 000-00-0009

> ... Returned to Timekeeper.

#### Display Employee Entitlements

This option allows the user to select an employee, a T&L Unit, and displays the employee's entitlement table. The entitlement table shows various types of premiums/benefits to which an employee is entitled (Yes) or not entitled (No). It will also show whether an employee's time is figured in hours (Hrs.) or Days. Every employee must have an entitlement table entry since these entitlements are used to calculate each employee's biweekly compensation.

> Select Payroll Main Menu Option: 4 \<RET\> Display Employee Entitlements

> Select T&L Unit: 101 \<RET\>

> Select Employee: PAIDEMPLOYEE,TEN \<RET\> 000-00-0010

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> EMPLOYEE PAY ENTITLEMENTS

> PAIDEMPLOYEE,TEN 000-00-0010

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 21%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>Regular Scheduled</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Hrs.</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>Hrs. &gt; 8 - 2</p>
</blockquote></th>
<th><blockquote>
<p>No</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Regular Unscheduled</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Hrs. &gt; 8 - 3</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reg.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hrs.</p>
</blockquote></td>
<td><blockquote>
<p>at</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Rate</p>
</blockquote></td>
<td><blockquote>
<p>- Day</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Holiday</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>- Day Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Reg.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hrs.</p>
</blockquote></td>
<td><blockquote>
<p>at</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Rate</p>
</blockquote></td>
<td><blockquote>
<p>- 2</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Holiday</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>- 2 No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reg.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hrs.</p>
</blockquote></td>
<td><blockquote>
<p>at</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Rate</p>
</blockquote></td>
<td><blockquote>
<p>- 3</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Holiday</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>- 3 No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Night Differential</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>- 2</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Holiday</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>Night Differential</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>- 3</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>On Call</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="13"><blockquote>
<p>Saturday Premium Yes Sleep Time No</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Sunday</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>- Day</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Comp. Time</p>
</blockquote></td>
<td><blockquote>
<p>Earned/Used</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Sunday</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>- 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Standby</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Sunday - 3 No Annual/Restored Leave Yes

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Overtime</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>- Day</p>
</blockquote></th>
<th><blockquote>
<p>Yes</p>
</blockquote></th>
<th><blockquote>
<p>Sick Leave</p>
</blockquote></th>
<th><blockquote>
<p>Yes</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Overtime</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>- 2</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>NonPay Annual Leave</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Overtime</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>- 3</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>AWOL/Susp/LWOP</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Hazardous Duty</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Military Leave</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Environmental Differential</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Authorized Absence</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Scheduled CB</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td colspan="2">No</td>
<td><blockquote>
<p>Non-Pay</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Travel OT</p>
</blockquote></td>
<td></td>
<td colspan="2">No</td>
<td><blockquote>
<p>Continuation of Pay</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Hrs.&gt;8 - Day</p>
<p>Press RETURN</p>
</blockquote></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
<td colspan="2"><p>No</p>
<p>Continue. <strong>&lt;RET&gt;</strong></p></td>
<td><blockquote>
<p>VCS Commission Sales</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Post Miscellaneous Data

This option allows Payroll to request a payment record or enter time and attendance report related data such as a T&L Unit change, Annual Leave lump sum that the employee has upon separation from the system, the expiration date of the separating employee's Annual Leave, a record of the employee's salary payments, information on withholding of Federal Income Tax, cost-of-living­ allowance information, and the last day of duty or transaction date for the employee.

Miscellaneous data can be entered any time up to the time of transmission. Posting miscellaneous data will automatically update 8B string if the record has already been sent to Payroll (certified).

> Select Payroll Main Menu Option: 5 \<RET\> Post Miscellaneous Data

> Select Pay Period: 93-01 \<RET\>

> Select Employee: PAIDEMPLOYEE1,ONE \<RET\> 000-00-0011

> VA TIME & ATTENDANCE SYSTEM

<table style="width:100%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 15%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>MISCELLANEOUS</p>
</blockquote></th>
<th><blockquote>
<p>DATA</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE1,ONE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>000-00-0011</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Station: 111</p>
<p>T&amp;L:</p>
<p>Pay Per: 93-01</p>
</blockquote></td>
<td><blockquote>
<p>Normal Hours: Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>Duty Basis: 1</p>
<p>Flextime:</p>
<p>FLSA: E</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Lump</p>
</blockquote></th>
<th><blockquote>
<p>Sum</p>
</blockquote></th>
<th><blockquote>
<p>Units:</p>
</blockquote></th>
<th><blockquote>
<p><strong>42 &lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>New T&amp;L Unit:</p>
</blockquote></th>
<th><blockquote>
<p><strong>100</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Lump</p>
</blockquote></td>
<td><blockquote>
<p>Sum</p>
</blockquote></td>
<td><blockquote>
<p>Units 2:</p>
</blockquote></td>
<td><blockquote>
<p><strong>2 &lt;RET&gt;</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Payment Record?</p>
</blockquote></td>
<td><blockquote>
<p><strong>Yes</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lump</p>
</blockquote></td>
<td><blockquote>
<p>Sum</p>
</blockquote></td>
<td><blockquote>
<p>Units 3:</p>
</blockquote></td>
<td><blockquote>
<p><strong>12 &lt;RET&gt;</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Opt. W/H Tax?</p>
</blockquote></td>
<td><blockquote>
<p><strong>Yes</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lump</p>
</blockquote></td>
<td><blockquote>
<p>Sum</p>
</blockquote></td>
<td><blockquote>
<p>Exp. Date:</p>
</blockquote></td>
<td><blockquote>
<p><strong>T &lt;RET&gt;</strong> FE</p>
</blockquote></td>
<td>B 10,1993</td>
<td><blockquote>
<p>Exclude Foreign</p>
</blockquote></td>
<td><blockquote>
<p>COLA? <strong>Yes</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> 8B Day Number: 043 \<RET\>

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window.

> COMMAND: EXIT \<RET\> INSERT Save changes before leaving form (Y/N)? Y \<RET\>

> Save changes before leaving form (Y/N)? N \<RET\>

> Form Not Saved!

Use up/down arrow keys or the return key to advance thru the screen. Enter one or two question marks (??) at any prompt to receive help or a list of choices. Examples of choices for each prompt are as follows:

> Lump Sum Units: ?? \<RET\>

> ----------------------------------------------------------------------------

> The number of hours or days of annual leave a day shift employee has when

> separating.

> Press \<PF1\>H for help INSERT

> Lump Sum Units 2: ?? \<RET\>

> ----------------------------------------------------------------------------

> The number of hours or days of annual leave a second shift employee has when

> separating.

> Press \<PF1\>H for help INSERT

> Lump Sum Units 3: ?? \<RET\>

> ----------------------------------------------------------------------------

> The number of hours or days of annual leave a third shift employee has when

> separating.

> Press \<PF1\>H for help INSERT

> Lump Sum Exp. Date: ?? \<RET\>

> ----------------------------------------------------------------------------

> The date the separating employee's annual leave will expire.

> Examples of Valid Dates:

> JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

> T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

> T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

> If the year is omitted, the computer uses the CURRENT YEAR.

> Press \<PF1\>H for help INSERT

> New T&L Unit: ?? \<RET\>

> ----------------------------------------------------------------------------

> ANSWER WITH T&L UNIT CODE

> DO YOU WANT THE ENTIRE 16-ENTRY T&L UNIT LIST? Y \<RET\>

> ----------------------------------------------------------------------------

> 100

> 101

> 102

> 103

> 111

> Press RETURN to continue, '^' to exit:

> New T&L Unit: ?? \<RET\>

> ----------------------------------------------------------------------------

> ANSWER WITH T&L UNIT CODE

> DO YOU WANT THE ENTIRE 16-ENTRY T&L UNIT LIST? N \<RET\>

> ----------------------------------------------------------------------------

This field will be coded only to change the employee's time and leave unit.

> Press \<PF1\>H for help INSERT

> Payment Record? ?? \<RET\>

> ----------------------------------------------------------------------------

> Indicates Payroll has requested a current "Record of Salary Payments" for

> this employee.

> Choose from:

> Y YES

> N NO

> Press \<PF1\>H for help INSERT

> Opt. W/H Tax? ?? \<RET\>

> ----------------------------------------------------------------------------

> Indicates the employee elects the optional method of withholding Federal

> income tax from the lump-sum payment.

> Choose from:

> Y YES

> N NO

> Press \<PF1\>H for help INSERT

> Exclude Foreign COLA? ?? \<RET\>

> ----------------------------------------------------------------------------

> Indicates the exclusion of a foreign cost-of-living-allowance from the

> employee's lump-sum payment.

> Choose from:

> Y YES

> N NO

> Press \<PF1\>H for help INSERT

> 8B Day Number: ? \<RET\>

> ----------------------------------------------------------------------------

> Answer must be 3 digits in length and between 001 and 366.

> 8B Day Number: ?? \<RET\>

> ----------------------------------------------------------------------------

> Indicates the day number of the last day of duty or date of effectiveness of

> the transaction for this employee.

> Press \<PF1\>H for help INSERT

The "day number" that this prompt is referring to is the "day number" of the calendar year (i.e., Jan 1 is day number 001, Jan 2 is day number 002, etc.).

#### Tour of Duty Management

This option is a submenu on the Payroll Main Menu. It allows the user to list tours of duty and to display information about any tour of duty.

> Select Payroll Main Menu Option: 6 \<RET\> Tour of Duty Management

> 1 Display Tour of Duty

> 2 List Tours by T&L

#### Display Tour of Duty

This option will prompt the user to select an established tour of duty. It will display the tour description, length of meal time, whether meal time is subject to premium pay, whether the tour spans two calendar days, whether the tour is available to all T&L Units, the start/stop times for each segment of the tour, and if applicable, the special tour indicator that is associated with a particular start/stop time.

This option merely displays the tour information. You may not edit the tour with this option.

> Select Tour of Duty Management Option: 1 \<RET\> Display Tour of Duty

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> Select TOUR OF DUTY: ?? \<RET\>

> CHOOSE FROM:

> 1 DAY OFF

> 2 DAILY TOUR

> 3 INTERMITTENT-DAYS

> 4 INTERMITTENT-HOURS

> 9 08:00A-04:30P

> 10 07:00A-03:30P

> 11 08:00A-10:00A

> 12 07:30A-04:00P

> 14 08:00A-11:00A

> 15 07:45A-04:15P (5P-6P OC)

> 16 04:00A-12:30P

> 17 09:00P-05:30A

> 18 04:00A-NOON

> 19 08:00P-08:00P

> 20 11:30P-07:30A

> 22 08:00A-09:00A

> 23 08:00A-03:30P

> 24 09:00A-03:30P

> 25 10:00A-NOON

> 26 01:00P-04:00P

> 28 07:00P-MID

> '^' TO STOP: ^ \<RET\>

> Select TOUR OF DUTY: 19 \<RET\>

Meal: 0

Meal: 0

Meal: 0

Meal: 0

Meal: 30

Meal: 30

Meal: 0

Meal: 30

Meal: 0

Meal: 30

Meal: 30

Meal: 30

Meal: 30

Meal: 0

Meal: 0

Meal: 0

Meal: 30

Meal: 30

Meal: 0

Meal: 0

Meal: 0

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 08:00P-08:00P Description:

> <u>Meal Time</u>: 0 Meal on Premium Time?

> All T&Ls? NO Two-Day Tour? YES START STOP CODE

> 1 08:00P 08:00P

> 2

> 3

> 4

> 5

> 6

> 7

> Exit Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT \<RET\> INSERT

#### List Tours by T&L

With this option the user is prompted to select a particular Time and Leave Unit (T&L) or ALL T&L Units. If a particular T&L is selected, then all the tours associated with it are displayed. If ALL T&Ls are selected, then all tours of duty will be displayed along with the T&Ls associated with the tour.

The tour number, tour name, number of hours in the tour, start/stop times of the various segments of the tour, any special indicators for each time segment and the T&L(s) associated with the tour are displayed.

> Select Tour of Duty Management Option: 2 \<RET\> List Tours by T&L Select T&L Unit (or ALL): 101 \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> 19-Jul-94 T & L T O U R L I S T Page 1

> 101

> \# Tour Hrs. Segment Special Indicator

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>15</p>
</blockquote></th>
<th><blockquote>
<p>07:45A-04:15P</p>
</blockquote></th>
<th><blockquote>
<p>(5P-6P</p>
</blockquote></th>
<th><blockquote>
<p>OC)</p>
</blockquote></th>
<th><blockquote>
<p>8.00</p>
</blockquote></th>
<th><blockquote>
<p>07:45A-04:15P</p>
<p>05:00P-06:00P On-Call</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>8.00</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-08:00A</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>24.00</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-08:00A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>140</p>
</blockquote></td>
<td><blockquote>
<p>08:30A-05:00P</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>8.00</p>
</blockquote></td>
<td><blockquote>
<p>08:30A-05:00P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DAILY TOUR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>DAY OFF</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to Continue. ^ \<RET\>

> Select T&L Unit (or ALL): ALL \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE

> 24-Aug-94 T & L T O U

RIGHT MARGIN: 80// \<RET\>

> \# Tour Hrs.

> 339 00:15A-08:00A On Call 0.00

> T&Ls: All

> 26 01:00P-04:00P 3.00

> T&Ls: All

> 111 01:00P-05:00P 4.00

> T&Ls: All

> 251 01:00P-09:00P 8.00

> T&Ls:

> Press RETURN to Continue. ^ \<RET\>

01:00P-04:00P

01:00P-05:00P

01:00P-09:00P

#### T&L Management

This option is a submenu on the Payroll Main Menu. It allows the user to list Time and Leave Units (T&L) and display information about any T&L.

> Select Payroll Main Menu Option: 7 \<RET\> T&L Management

> 1 Display T&L Unit

> 2 Daily T&L List

#### Display T&L Unit

With this option the user is prompted to select an existing Time and Leave Unit (T&L); and the last entered timekeeper, supervisor, and OT/CT approver will be displayed. Enter one or two question marks (??) at the timekeeper, supervisor, and OT/CT approver prompts to see additional timekeepers, etc., for that T&L.

This option will display data associated with the T&L that the user may not edit. Use up/down arrow keys to advance thru the screen and to the command prompt.

> Select T&L Management Option: 1 \<RET\> Display T&L Unit

> VA TIME & ATTENDANCE SYSTEM TIME & LEAVE UNIT

> Select T&L Unit: 103 \<RET\>

> VA TIME & ATTENDANCE SYSTEM TIME & LEAVE UNIT

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>CODE</u>:</p>
</blockquote></th>
<th><blockquote>
<p>103</p>
</blockquote></th>
<th></th>
<th colspan="2" rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NAME: <u>STATION #</u></p>
</blockquote></th>
<th><blockquote>
<p>ONCALL AND</p>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>STANDBY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SERVICE:</p>
</blockquote></td>
<td><blockquote>
<p>NURSING</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SECTION:</p>
</blockquote></td>
<td><blockquote>
<p>ISC DEV</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Time SleepTime Begins</u>: 11:00P <u>Entitled Sat/Sun Premiums?</u> YES

> Select TIMEKEEPER: PAIDTIMEKEEPR,TWO Select SUPERVISOR: PAIDSUPERVISR,TWO Select OT/CT APPROVER: PAIDSUPERVISR,TWO Exit Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT \<RET\> INSERT

#### Daily T&L List

With this option the user is prompted to select an existing Time and Leave Unit (T&L) and a posting date. The names of the employees in the T&L, their scheduled tour of duty and any exceptions to the scheduled tour of duty are displayed.

> Select T&L Management Option: 2 \<RET\> Daily T&L List

> Select T&L Unit: 100 \<RET\>

> Posting Date: T-1// ?? \<RET\>

> Examples of Valid Dates:

> JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

> T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

> T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

> If the year is omitted, the computer assumes a date in the PAST.

> Enter a date which is less than or equal to APR 15, 1993. Posting Date: T-1// T \<RET\> Jan 25, 1993

> Select Device: Home// \<RET\> ANYWHERE Right Margin: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> Mon 25-Jan-93 for T&L 100

> Employee Scheduled Tour Tour Exceptions

> ------------------------------------------------------------------------------

> PAIDEMPLOYEE1,TWO 08:00A-04:30P Unposted

> PAIDEMPLOYEE1,THREE Day Off

> PAIDEMPLOYEE1,FOUR 03:30P-MID Unposted

> MID-00:15A

> Scheduled Overtime

> PAIDEMPLOYEE1,FIVE 08:00A-04:30P

> PAIDEMPLOYEE1,SIX Day Off

> PAIDEMPLOYEE1,SEVEN Day Off

> Press RETURN to Continue. \<Ret\>

#### List Prior Pay Period Exceptions

This option lists all time and attendance report exceptions for all records released to Payroll and/or transmitted for all previous pay periods.

Similar to this option is "Display Pay Period Exceptions" which lists all exceptions for a specific pay period.

> Select Payroll Main Menu Option: 8 \<RET\> List Prior Pay Period Exceptions

> Select T&L Unit (or ALL): ALL \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> PRIOR PAY PERIOD EXCEPTIONS

> 25-Aug-94

> PAIDEMPLOYEE1,EIGHT (043)

> 26-Jul-94 04:30P AL not Requested

> PAIDEMPLOYEE1,NINE (043)

> 31-Jul-94 MID OT not Requested

> PAIDEMPLOYEE2,TEN (043)

> 31-Jul-94 08:00P OT not Requested

> 1-Aug-94 07:00A AL not Requested

> PAIDEMPLOYEE2,ONE (043)

> 1-Aug-94 04:30P OT Supervisor Approved but pending Director Approval

> PAIDEMPLOYEE2,TWO (043)

> 25-Jul-94 08:00A AL not Requested

> Press RETURN to Continue. \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 2

> PRIOR PAY PERIOD EXCEPTIONS

> 25-Aug-94

> PAIDEMPLOYEE2,TWO (043)

> 29-Jul-94 02:30P SL not Requested

> PAIDEMPLOYEE2,THREE (044)

> 18-Feb-93 08:00A CU not Requested

> 9-Feb-93 07:30P CT Posted exceeds Requested Hours

> PAIDEMPLOYEE2,FOUR (044)

> 9-Feb-93 08:30P TV Posted outside of Tour Hours

> 10-Feb-93 06:00P TV Posted outside of Tour Hours

> PAIDEMPLOYEE2,FIVE (044)

> 25-Jan-93 03:30P AL not Requested

> PAIDEMPLOYEE2,SIX (044)

> Press RETURN to Continue. ^ \<RET\>

#### Create Employee Record for Pay Period

This option will allow Payroll to create a time and attendance report entry for a new employee or an employee returning to duty from Extended LWOP. The employee must exist in the PAID EMPLOYEE (#450) file.

> Select Payroll Main Menu Option: 9 \<RET\> Create Employee Record for Pay

> Period

> Select PAY PERIOD: 92-24 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE2,SEVEN \<RET\> Warning: Separation Indicator is not N. Warning: No T&L Unit has been specified.

> OK to Create Record for this Employee? Y \<RET\>

> Select T&L UNIT CODE: 100 \<RET\>

> Pay Period opened for this Employee. Select EMPLOYEE: \<RET\>

#### Employee Inquiry Menu

This option allows the Fiscal user to access a menu of employee inquiry options to view employee data in the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.

> Select Payroll Main Menu Option: 10 \<RET\> Employee Inquiry Menu

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Print Employee Entries</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Search Employee Entries</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Employee Inquiry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Payrun Data Inquiry</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Update PAID Codes</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Print Employee Entries

This option allows the Fiscal user to print data from the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.

> Select Employee Inquiry Menu Option: 1 \<RET\> Print Employee Entries

> Select FILE: PAID EMPLOYEE// \<RET\>

> Include separated employees? NO// \<RET\> (NO) Separated employees will not be included.

> SORT BY: EMPLOYEE NAME// \<RET\>

> START WITH EMPLOYEE NAME: FIRST// \<RET\>

> FIRST PRINT FIELD: ?? \<RET\>

> CHOOSE FROM:

> '^' TO STOP: ^ \<RET\>

> TYPE '&' IN FRONT OF FIELD NAME TO GET TOTAL FOR THAT FIELD,

> '!' TO GET COUNT, '+' TO GET TOTAL & COUNT, '#' TO GET MAX & MIN,

> '\]' TO FORCE SAVING PRINT TEMPLATE

> YOU CAN FOLLOW FIELD NAME WITH ';' AND FORMAT SPECIFICATION(S)

> THEN PRINT FIELD: 13 \<RET\> GRADE

> THEN PRINT FIELD: 28 \<RET\> SALARY

> THEN PRINT FIELD: \<RET\>

> HEADING: PAID EMPLOYEE SEARCH Replace \<RET\>

> DEVICE: \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> PAID EMPLOYEE SEARCH AUG 25,1994 14:53 PAGE 1

> EMPLOYEE NAME GRADE SALARY

> ------------------------------------------------------------------------------

> PAIDEMPLOYEEA,ONE PAIDEMPLOYEEAA,TWO PAIDEMPLOYEEAB,THREE PAIDEMPLOYEEAC,FOUR PAIDEMPLOYEEAD,FIVE PAIDEMPLOYEEB,ONE PAIDEMPLOYEEBA,TWO PAIDEMPLOYEEBB,THREE PAIDEMPLOYEEBC,FOUR PAIDEMPLOYEEBD,FIVE PAIDEMPLOYEEBE,SIX PAIDEMPLOYEEBF,SEVEN PAIDEMPLOYEEBG,EIGHT PAIDEMPLOYEEBH,NINE PAIDEMPLOYEEBI,TEN PAIDEMPLOYEEBJ,ELEVEN

> PAID EMPLOYEE SEARCH EMPLOYEE NAME

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 16%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEEBK,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>14</p>
</blockquote></th>
<th><blockquote>
<p>61887.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEEBL,THIRTEEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEEBM,FOURTEEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEEBN,FIFTEEN</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>50089.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEEBO,SIXTEEN</p>
</blockquote></td>
<td><blockquote>
<p>99</p>
</blockquote></td>
<td><blockquote>
<p>109086.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEEBP,SEVENTEEN</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>27950.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEEC,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEECA,TWO</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>120000.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEECB,THREE</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>27950.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEECC,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEECD,FIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEECE,SIX</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>60070.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEECF,SEVEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>PAIDEMPLOYEECG,EIGHT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEECH,NINE</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>61887.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEECI,TEN</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>27950.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><strong>^ &lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> 32 MATCHES FOUND.

> Select FILE: PAID EMPLOYEE// ?? \<RET\>

> CHOOSE FROM:

> 450 PAID EMPLOYEE

> 459 PAID PAYRUN DATA

> Select FILE: PAID EMPLOYEE// 459 \<RET\> PAID PAYRUN DATA SORT BY: PAY PERIOD// \<RET\>

> START WITH PAY PERIOD: FIRST// \<RET\>

> FIRST PRINT FIELD: 1 \<RET\> EMPLOYEE (multiple)

> FIRST PRINT EMPLOYEE SUB-FIELD: .01 \<RET\> NAME

> THEN PRINT EMPLOYEE SUB-FIELD: 76 \<RET\> SICK LEAVE USED CPPD

> THEN PRINT EMPLOYEE SUB-FIELD: \<RET\>

> THEN PRINT FIELD: \<RET\>

> HEADING: PAID PAYRUN DATA LIST Replace \<RET\>

> DEVICE: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> PAID PAYRUN DATA LIST AUG 25,1994 16:46 PAGE 1

> SICK

> LEAVE

> USED

> NAME CPPD

> ------------------------------------------------------------------------------

> PAY PERIOD: 93-12

> PAIDEMPLOYEE2,EIG 4.00

> PAIDEMPLOYEE2,NINE 6.00

> PAIDEMPLOYEE3,TEN 12.00

> PAIDEMPLOYEE3,ONE 1.50

> PAIDEMPLOYEE3,TWO

> PAIDEMPLOYEE3,THREE 6.50

> Select FILE: PAID EMPLOYEE// ^ \<RET\>

As of July 2012, a new field, “TELEWORK INDICATOR,” can be added to the report. This field displays the employees’ telework status, as shown:

PAID EMPLOYEE SEARCH JUN 10,2012 13:38 PAGE 1

EMPLOYEE

NAME TELEWORK ASSIGNMENT GRADE

-------------------------------------------------------------------------------

REDACTED Employee regularly teleworks three or more days per pay period.

NONE 12

REDACTED

> Position is suitable for telework and employee is eligible, but no telework agreement in place.

> NONE 14

#### Search Employee Entries

This option allows the Fiscal user to search for data from the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.

> Select Employee Inquiry Menu Option: 2 \<RET\> Search Employee Entries

> Select FILE: PAID EMPLOYEE// \<RET\>

> Include separated employees? NO// \<RET\> (NO) Separated employees will not be included.

> -A- SEARCH FOR PAID EMPLOYEE FIELD: ?? \<RET\>

> CHOOSE FROM:

> '^' TO STOP: ^ \<RET\>

> -A- SEARCH FOR PAID EMPLOYEE FIELD: 13 \<RET\> GRADE

> -A- CONDITION: ?? \<RET\>

> CHOOSE FROM:

> 1 NULL

> 2 CONTAINS

> 3 MATCHES

> 4 LESS THAN

> 5 EQUALS

> 6 GREATER THAN

> YOU CAN NEGATE ANY OF THESE CONDITIONS BY PRECEDING THEM WITH "'" OR "-" SO THAT "'NULL'" MEANS "NOT NULL"

> -A- CONDITION: 5 \<RET\> EQUALS

> -A- EQUALS: 12 \<RET\>

> -B- SEARCH FOR PAID EMPLOYEE FIELD: \<RET\>

> IF: A// \<RET\> GRADE EQUALS 12

> STORE RESULTS OF SEARCH IN TEMPLATE: \<RET\>

> SORT BY: EMPLOYEE NAME// \<RET\>

> START WITH EMPLOYEE NAME: FIRST// \<RET\>

> FIRST PRINT FIELD: .01 \<RET\> EMPLOYEE NAME

> THEN PRINT FIELD: 13 \<RET\> GRADE

> THEN PRINT FIELD: \<RET\>

> HEADING: PAID EMPLOYEE SEARCH Replace \<RET\>

> DEVICE: \<RET\> ANYWHERE RIGHT MARGIN: \<RET\> PAID EMPLOYEE SEARCH

> PAID EMPLOYEE SEARCH FEB 16,1993 14:58 PAGE 1

> EMPLOYEE NAME GRADE

> -----------------------------------------------------------------------------

> PAIDEMPLOYEE3,FOUR 12

> PAIDEMPLOYEE3,FIVE 12

> PAIDEMPLOYEE3,SIX 12

> PAIDEMPLOYEE3,SEVEN 12

> PAIDEMPLOYEE3,EIGHT 12

> 5 MATCHES FOUND.

As of July 2012, a new field, “TELEWORK INDICATOR,” can be used in the search criteria. This field displays a brief description of the employees’ telework indicators, as shown:

PAID EMPLOYEE SEARCH JUN 10,2012 13:38 PAGE 1

EMPLOYEE TELEWORK

NAME INDICATOR

-------------------------------------------------------------------------------

REDACTED Employee regularly teleworks three or more days per pay period.

REDACTED

> Position is suitable for telework and employee is eligible, but no telework agreement in place.

#### Employee Inquiry

This option allows designated Fiscal Service users to view PAID EMPLOYEE file data.

> Select Employee Inquiry Menu Option: 3 \<RET\> Employee Inquiry

> Select EMPLOYEE: PAIDEMPLOYEE3,NINE \<RET\> 000-00-0039

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 34%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE3,NINE</p>
</blockquote></th>
<th><blockquote>
<p>CHIEF OF STAFF</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0039</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
</tr>
</tbody>
</table>

> -----------------------------------------------------------------------------

> 1 POSITION INFORMATION

> 2 PERSONAL INFORMATION

> 3 VERIFICATION OF EMPLOYMENT

> 4 PAY INFORMATION

> 5 BENEFITS

> 6 EARNINGS

> 7 FEDERAL/STATE/CITY TAXES

> 8 DEDUCTIONS/ALLOTMENTS

> 9 LEAVE

> 10 SEPARATED EMPLOYEE INFORMATION

> 11 VCS

> Select a number: 3// \<RET\>

> DEVICE: \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> ...SORRY, JUST A MOMENT PLEASE...

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 36%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE3,NINE</p>
</blockquote></th>
<th><blockquote>
<p>CHIEF OF STAFF</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0039</p>
</blockquote></td>
<td></td>
<td>T&amp;L:</td>
</tr>
</tbody>
</table>

> -----------------------------------------------------------------------------

> LAST PP: 17 VERIFICATION OF EMPLOYMENT PAGE 1

> -----------------------------------------------------------------------------

> PAY PLAN L

> OCCUPATION SERIES & TITLE 066106 PHARMACY TECHNICIAN

> GRADE 05

> STEP 09

> SALARY 21,501.00

> GROSS PAY YTD 8,240.00

> TYPE OF APPOINTMENT 1 CAREER

> PAY BASIS 1 PER ANNUM

> DUTY BASIS 1 FULL-TIME

> NORMAL HOURS 50

> 8B NORMAL HOURS 50.00

> FTE EQUIVALENT 1.00

> SERVICE COMPUTATION DATE JAN 29, 1976

> STATION EOD APR 21, 1991

> ACCESSION/SEPARATION CODE S

> VA STATION TRANSFERRED FROM 999

> Press RETURN to continue: \<RET\>

Only data for "Verification of Employment" will be displayed here. Choose other options as desired.

#### Payrun Data Inquiry

This option allows designated Fiscal Service users to view the PAID PAYRUN DATA (#459) file.

> Select Employee Inquiry Menu Option: 4 \<RET\> Payrun Data Inquiry

> Select PAID PAYRUN DATA PAY PERIOD: 93-12 \<RET\>

> Select EMPLOYEE NAME: PAIDEMPLOYEE4,TEN \<RET\> 000-00-0040

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 29%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE4,TEN</p>
</blockquote></th>
<th><blockquote>
<p>VCS</p>
</blockquote></th>
<th><blockquote>
<p>DUTY STATION: 111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-00-0040</p>
</blockquote></td>
<td></td>
<td>T&amp;L:</td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> PAY PERIOD: 93-12

> 1 General Information

> 2 Earnings

> 3 Deductions

> 4 Leave

> Select a number: 1 \<RET\>

> DEVICE: \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> PAIDEMPLOYEE4,TEN VCS DUTY STATION: 111

> 000-00-0040 T&L:

> ----------------------------------------------------------------------------

> PAY PERIOD: 93-12 GENERAL INFORMATION PAGE 1

> -----------------------------------------------------------------------------

> PAY PLAN E ES GRADE 00

> STEP 04

> DUTY BASIS 1 FULL-TIME

> 8B NORMAL HOURS 80

> SALARY 27,360.72

> Press RETURN to continue: \<RET\>

Choose above options 2 thru 4 as desired. Only data for "General Information" will be shown here.

#### Update PAID Codes (General Updates)

This option allows the user to enter, edit or delete PAID codes and their descriptions from the PAID CODE FILES (#454). The user must have the PRS PAID CODE KEY or this option will not appear.

> Select Employee Inquiry Menu Option: 5 \<RET\> Update PAID Codes

> Select FILE: ?? \<RET\>

> CHOOSE FROM:

> 1 OCCUPATION SERIES/TITLE

> 3 PERFORMANCE/PROFICIENCY RATING

> 5 PAY BASIS

> 6 VETERANS PREFERENCE

> 7 TYPE OF APPOINTMENT

> 8 EDUCATION

> 11 FEGLI

> 13 ACADEMIC TITLE

> 14 PAY RATE DETERMINANT

> 18 COUNTRY

> 19 SPECIAL PAY AGREEMENT

> 20 NO AGREEMENT REASON

> 21 PRIOR VA EXPERIENCE

> 22 POSITION PREFERENCE

> 23 GEOGRAPHICAL PREFERENCE

> 24 FOLLOWUP CODE

> 26 SEX

> 27 CITIZENSHIP

> 31 FUNCTIONAL CODE

> 33 FLSA CODE

> 34 DUTY BASIS

> '^' TO STOP: ^ \<RET\>

> Select FILE: 3 \<RET\> PERFORMANCE/PROFICIENCY RATING

> Select PERFORMANCE/PROFICIENCY RATING CODE: A \<RET\> OUTSTANDING CODE: A// \<RET\>

> DESCRIPTION: OUTSTANDING// \<RET\>

> Select PERFORMANCE/PROFICIENCY RATING CODE: \<RET\>

> Select FILE: \<RET\>

#### Update PAID Codes (Telework Indicators)

This option allows the user to view telework indicators and descriptions from the PAID CODE FILES (#454). The user must have the PRS PAID CODE KEY or this option will not be available.

PRIVACY ACT STATEMENT

In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

1 Print Employee Entries

2 Search Employee Entries

3 Employee Inquiry

4 Payrun Data Inquiry

5 Update PAID Codes

6 View Labor Distribution(s)

Select Employee Inquiry Menu Option: 5 Update PAID Codes

Select FILE: 454 TELEWORK INDICATOR

Select TELEWORK INDICATOR TELEWORK CODE: ?

Answer with TELEWORK INDICATOR TELEWORK CODE

Choose from:

A

E

P

R

S

V

X

Y

Z

You may enter a new TELEWORK INDICATOR, if you wish

Answer must be 1 character in length.

Select TELEWORK INDICATOR TELEWORK CODE: P

TELEWORK CODE: P//

DESCRIPTION: Employee regularly teleworks three or more days per pay period.

The PAID CODES file (#454) includes an entry for the new telework code set as defined in Table 1.

| Eligible Code | Code Definition                                                                                                                                                                                                                   | To Track |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| P             | Employee regularly teleworks three or more days per pay period.                                                                                                                                                                   | Yes      |
| R             | Employee regularly teleworks one or two days per pay period.                                                                                                                                                                      | Yes      |
| S             | Employee regularly teleworks one day per month.                                                                                                                                                                                   | Yes      |
| A             | Ad Hoc Telework. Employee teleworks only on an as-needed basis. This includes Continuity of Operations (COOP), National/Regional emergencies, situational basis (temporary), and Office of Workers Compensation-related telework. | Yes      |
| X             | Position is suitable for telework and employee is eligible, but no telework agreement is in place.                                                                                                                                | No       |
| Y             | Position is suitable for telework, but employee is not eligible to telework.                                                                                                                                                      | No       |
| Z             | Position is not suitable for telework. This code is used only when the employee's position makes teleworking impossible.                                                                                                          | No       |
| V             | Employee who is virtual.                                                                                                                                                                                                          | No       |
| E             | Employee regularly teleworks three or more days per work week.                                                                                                                                                                    | Yes      |
| Blank         | Default. No telework code has been entered.                                                                                                                                                                                       | No       |

#### List/Clear Prior Pay Period Corrections

This option allows the user to list and/or clear time and attendance report corrections for all previous pay periods. The user may select "All" or a specific T&L to view data. After corrected data has been sent to the Austin Automation Center, the user may answer "yes" at the "Clear Correction" prompt, so as to clear the data.

> Select Payroll Main Menu Option: 11 \<RET\> List/Clear Prior Pay Period

> Corrections

> VA TIME & ATTENDANCE SYSTEM PRIOR PAY PERIOD CORRECTIONS

> Select T&L Unit (or ALL): ALL \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET

> PAIDEMPLOYEE4,ONE 000-00-0041

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Station:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Normal Hours:</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
</blockquote></th>
<th><blockquote>
<p>Duty Basis: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>T&amp;L:</p>
</blockquote></td>
<td><blockquote>
<p>043</p>
</blockquote></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>Flextime:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>93-02</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA: N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> -----------------------------------------------------------------------------

> \* \* \* Prior Data \* \* \*

> VCS Commission Sales

> Sun Mon Tue Wed Thu Fri Sat Total

> Week 1 0.00

> Week 2

0.00

> -----------------------------------------------------------------------------

> \* \* \* Corrected Data \* \* \*

> VCS Commission Sales

> Sun Mon Tue Wed Thu Fri Sat Total

> Week 1 50.00 50.00 50.00 50.00 50.00 50.00 50.00 350.00

> Week 2 50.00 50.00 50.00 50.00 50.00 50.00 50.00 350.00

> -----------------------------------------------------------------------------

> Clear Correction? No \<RET\>

#### Change Employee T&L Unit

This option allows the user to change an employee's T&L Unit immediately (as soon as the employee transfers to another T&L), as opposed to waiting until the beginning of the next pay period. The user will enter the new T&L at the "T&L Unit" prompt.

> Select Payroll Main Menu Option: 12 \<RET\> Change Employee T&L Unit

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 15%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select EMPLOYEE: <strong>PAIDEMPLOYEE4,TWO</strong></p>
<p>T&amp;L UNIT: 043// <strong>101 &lt;RET&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>000-00-0042</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select EMPLOYEE: <strong>PAIDEMPLOYEE4,TWO</strong></p>
<p>T&amp;L UNIT: 101// <strong>&lt;RET&gt;</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></td>
<td><blockquote>
<p>000-00-0042</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### List Un-Certified Employees

This allows the user to list the status of the time and attendance reports for the current pay period by selecting a specific T&L. It shows the employees that have not been released to Payroll. Similar to this option is "Un-Certified Employees ­ All T&Ls" which lists the time and attendance reports of employees of all T&Ls.

> Select Payroll Main Menu Option: 13 \<RET\> List Un-Certified Employees

> VA TIME & ATTENDANCE SYSTEM Page 1

> UN-CERTIFIED EMPLOYEES

> Select T&L Unit: 902 \<RET\>

> 902 INFORMATION SERVICES CENTER Sun 4-Apr-93 to Sat 17-Apr-93

> 000-00-0043 PAIDEMPLOYEE4,THREE

> 000-00-0044 PAIDEMPLOYEE4,FOUR

> 000-00-0045 PAIDEMPLOYEE4,FIVE

> 000-00-0046 PAIDEMPLOYEE4,SIX

> 000-00-0047 PAIDEMPLOYEE4,SEVEN

> 000-00-0048 PAIDEMPLOYEE4,EIGHT

> 000-00-0049 PAIDEMPLOYEE4,NINE

> 000-00-0050 PAIDEMPLOYEE5,TEN

> 000-00-0051 PAIDEMPLOYEE5,ONE

> 000-00-0052 PAIDEMPLOYEE5,TWO

#### Clear Prior Pay Period Exceptions

With this option the user is able to clear all time and attendance report exceptions for all records released to Payroll and/or transmitted for all previous pay periods (exceptions listed in File 458.5).

> Select Payroll Main Menu Option: 14 \<RET\> Clear Prior Pay Period Exceptions

> Select T&L Unit (or ALL): ALL \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> PRIOR PAY PERIOD EXCEPTIONS

> 17-Jul-95

> PAIDEMPLOYEE5,THREE

> 12-Feb-93 08:00P OT Posted exceeds Requested Hours

> Clear Prior Pay Period Exception? No \<RET\>

#### List Leave Requests

This option allows Payroll users to display leave requests for a specific T&L.

> Select Payroll Main Menu Option: 15 \<RET\> List Leave Requests

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE (or RETURN for all): \<RET\> Begin with Date: 1/1/95 \<RET\> (JAN 01, 1995) End with Date: 7/1/95 \<RET\> (JUL 01, 1995) Sort by: (E=Employee D=Date) E// \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 100 LEAVE REQUESTS

> From 1-Jan-95 to 1-Jul-95

> PAIDEMPLOYEE5,FOUR 000-00-0054

> 08:00A 10-Jan-95 to 04:30P 10-Jan-95 8 hrs Annual Leave Approved

> TEST CASE

> 08:00A 1-Jun-95 to 03:00P 5-Jun-95 22.50 hrs Annual Leave Requested

> 08:00A 2-Jun-95 to 04:30P 2-Jun-95 8 hrs Annual Leave Requested

> 08:00A 5-Jun-95 to 09:00A 5-Jun-95 1 hrs Authorized Absence Requested

> XXXX

> 08:00A 12-Jun-95 to 04:30P 12-Jun-95 8 hrs Annual Leave Requested

> 08:00A 27-Jun-95 to 10:00A 27-Jun-95 2 hrs Annual Leave Requested

> 08:00A 27-Jun-95 to 10:00A 27-Jun-95 2 hrs Annual Leave Requested

> Press RETURN to Continue. \<RET\>

#### List OT/CT Requests

This option allows Payroll users to display a list of OT/CT requests for a specific T&L.

> Select Payroll Main Menu Option: 16 \<RET\> List OT/CT Requests

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE (or RETURN for all): \<RET\> Begin with Date: 7/1/94 \<RET\> (JUL 01, 1994) End with Date: 7/1/95 \<RET\> (JUL 01, 1995)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 100 OT/CT REQUESTS

> From 1-Jul-94 to 1-Jul-95

> PAIDEMPLOYEE5,FIVE 000-00-0055

> 8-Oct-94 5 Hrs. OVERTIME on T&L 100 Requested

> NEED MONEY

> PAIDEMPLOYEE5,SIX 000-00-0056

> 8-Oct-94 5 Hrs. OVERTIME on T&L 100 Cancelled

> NEED THE MONEY

> Supr: DONT DO IT

> Press RETURN to Continue. \<RET\>

#### Display Complete Request/Pay Period Records

This option allows the user to display all of the fields of leave, OT/CT requests, Environmental Differential, and Pay Period records for an employee.

> Select Payroll Main Menu Option: 17 \<RET\> Display Complete Request/Pay

> Period Records

> 1 Display Leave Request

> 2 Display OT/CT Request

> 3 Display Environmental Differential Request

> 4 Display Pay Period for Employee

#### Display Leave Request

This option allows the user to display all of the fields of a leave request.

> Select Display Complete Request/Pay Period Records Option: 1 \<RET\> Display

> Leave Request

> Select EMPLOYEE: 73 \<RET\> 07-14-95

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> SEQUENCE \#: 73 EMPLOYEE: PAIDEMPLOYEE5,SEVEN

> FROM DATE: JUL 14, 1995 FROM TIME: 02:00P

> TO DATE: JUL 14, 1995 TO TIME: 04:30P

> TYPE OF LEAVE: Authorized Absence REMARKS: ATTENDING SEMINAR

> STATUS: Requested ENTERED BY: PAIDEMPLOYEE5,SEVEN

> DATE/TIME ENTERED: JUL 11, 1995@13:54:49

> ESTIMATED HOURS/DAYS: 2.5 DAYS OR HOURS: HOURS

#### Display OT/CT Request

With this option, the user can display all of the fields of an OT/CT request showing exactly who approved certain actions and when they were approved.

> Select Display Complete Request/Pay-Period Records Option: 2 \<RET\> Display

> OT/CT Request

> Select EMPLOYEE: 25 \<RET\> 04-21-94

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SEQUENCE #: 25</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>EMPLOYEE: PAIDEMPLOYEE5,EIGHT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>REQUESTED WORK DATE: AP</p>
</blockquote></td>
<td>R 21,</td>
<td><blockquote>
<p>1994</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF TIME: COMP TIME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HOURS REQUESTED: 3.25</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>JUSTIFICATION: DEADLINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATUS: Supr. App.</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>T&amp;L WORKED: 111</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ENTRY PERSON: PAIDSUPERVISR,THREE ENTRY DATE/TIME: MAY 13, 1994@10:15:41

> SUPERVISOR: PAIDSUPERVISR,THREE

> SUPR. ACTION DATE/TIME: MAY 26, 1994@08:07:20

> SUPR. ES: PAIDSUPERVISR,THREE

#### Display Environmental Differential Request

This option allows Payroll to display all of the fields of an Environmental Differential Request for an employee.

> Select Display Complete Request/Pay Period Records Option: 3 \<RET\> Display

> Environmental Differential Request

> Select EMPLOYEE: 26 \<RET\> 02-16-93

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> SEQUENCE \#: 26 EMPLOYEE: PAIDTIMEKEEPR,THREE

> FROM DATE: FEB 16, 1993 FROM TIME: 03:30P

> MEAL TIME: 0 TO TIME: 04:30P

> TYPE OF EXPOSURE: SECOND-HAND SMOKE JUSTIFICATION: SMOKESTACK

> STATUS: Cancelled ENTERED BY: PAIDSUPERVISR,THREE

> DATE/TIME ENTERED: MAR 15, 1994@14:04:57

#### Display Pay Period for Employee

This option allows the user to display all of the fields of a pay period for a selected employee.

> Select Display Complete Request/Pay-Period Records Option: 4 \<RET\> Display

> Pay Period for Employee

> Select EMPLOYEE: PAIDTIMEKEEPR,THREE \<RET\> 000-00-0003

> Select PAY PERIOD: 95-03 \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EMPLOYEE: PAIDTIMEKEEPR,THREE</p>
</blockquote></th>
<th><blockquote>
<p>STATUS: TIMEKEEPER</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CUR. PP COMPRESSED INDICATOR: None</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY #: 1</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: DAY OFF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY #: 2</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: 08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOUR LENGTH: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR #1 SCH START TIME-1: 08:00A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TOUR #1 SCH STOP TIME-1: 04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY #: 3</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: 08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOUR LENGTH: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR #1 SCH START TIME-1: 08:00A</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TOUR #1 SCH STOP TIME-1: 04:30P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY #: 4</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: 08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOUR LENGTH: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR #1 SCH START TIME-1: 08:00A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TOUR #1 SCH STOP TIME-1: 04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY #: 5</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: 08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOUR LENGTH: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR #1 SCH START TIME-1: 08:00A</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TOUR #1 SCH STOP TIME-1: 04:30P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY #: 6</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: 08:00A-04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOUR LENGTH: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR #1 SCH START TIME-1: 08:00A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TOUR #1 SCH STOP TIME-1: 04:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY #: 7</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: DAY OFF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY #: 8</p>
</blockquote></td>
<td><blockquote>
<p>TOUR OF DUTY: DAY OFF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter RETURN to continue or '^' to exit: \<RET\>

> DAY \#: 9

> TOUR LENGTH: 8

> TOUR \#1 SCH STOP TIME-1: 04:30P

> DAY \#: 10

> TOUR LENGTH: 8

> TOUR \#1 SCH STOP TIME-1: 04:30P

> DAY \#: 11

> TOUR LENGTH: 8

> TOUR \#1 SCH STOP TIME-1: 04:30P

> DAY \#: 12

> TOUR LENGTH: 8

> TOUR \#1 SCH STOP TIME-1: 04:30P

> DAY \#: 13

> TOUR LENGTH: 8

> TOUR \#1 SCH STOP TIME-1: 04:30P

> DAY \#: 14

TOUR OF DUTY: 08:00A-04:30P

TOUR \#1 SCH START TIME-1: 08:00A

TOUR OF DUTY: 08:00A-04:30P

TOUR \#1 SCH START TIME-1: 08:00A

TOUR OF DUTY: 08:00A-04:30P

TOUR \#1 SCH START TIME-1: 08:00A

TOUR OF DUTY: 08:00A-04:30P

TOUR \#1 SCH START TIME-1: 08:00A

TOUR OF DUTY: 08:00A-04:30P

TOUR \#1 SCH START TIME-1: 08:00A

TOUR OF DUTY: DAY OFF

#### Employee Reports

This options allows the user to display all employee reports for a selected employee.

> Select Payroll Main Menu Option: 18 \<RET\> Employee Reports

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Expenditures</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Employee Overtime/CompTime Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Employee Prior Pay Period Adjustments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Paid T&amp;L Report</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Expenditures

This option allows the user to view all governmental cost over one or all pay periods for a chosen year.

> Select Employee Reports Option: 1 \<RET\> Expenditures

> Select T&L Unit(s): 001 \<RET\>

> Enter YEAR: 95 \<RET\> (1995)

> Enter Pay Period (Return for all): 3 \<RET\>

> THIS REPORT SHOULD BE QUEUED ! DEVICE: HOME// \<RET\>

> EMPLOYEE COST FOR PAY PERIOD - 3 DATE: 08/11/95

> Year: 95

> BASE NIGHT HOLIDA O/TIME SUNDAY ON-CA REEMP SAT GROSS G/SHARE GROSS NAME PAY DIFF PAY PAY PAY PAY AWARDS ANNUIT PAY PAY BENEFITS COST

> ---------------------------------------------------------------------------------------------------------------

> PDEMP,C 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,D 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,E 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,F 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,G 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,H 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,I 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,J 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,K 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,L 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,M 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,N 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,O 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,P 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,R 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,S 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> -------- ---- ---- ---- ---- ---- ---- ---- ---- -------- ------- --------

> T&L 001

> Total: 27528.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 27528.00 4343.88 31871.88

> --------------------------------------------------------------------------------------------------------------- DHCP PAID REPORT E001 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 001

#### Employee Overtime/Comp Time Report

This option allows the user to display the OT/CT that an employee has taken over one or all pay periods during a selected calendar year.

> Select Employee Reports Option: 2 \<RET\> Employee Overtime/CompTime Report

> Select T&L: 902 \<RET\>

> Enter YEAR: 95 \<RET\> (1995)

> Enter employee name (Return for ALL): \<RET\>

> Enter Pay Period (Return for all in this yr.): \<RET\>

> THIS IS A 132 COLUMN REPORT!

> DEVICE: HOME// HOME \<RET\>

> EMPLOYEE OT/CT REPORT DATE" 04/27/95

> ![](paid-version-4-user-manual/002.png)![](paid-version-4-user-manual/003.png)![](paid-version-4-user-manual/004.png)![](paid-version-4-user-manual/005.png)![](paid-version-4-user-manual/006.png)![](paid-version-4-user-manual/007.png)![](paid-version-4-user-manual/008.png)![](paid-version-4-user-manual/009.png)![](paid-version-4-user-manual/010.png)![](paid-version-4-user-manual/011.png)![](paid-version-4-user-manual/012.png)![](paid-version-4-user-manual/013.png)Year: 95 T&L: 902

> P/P DATE NAME SSN GROSS PAY C/T USED C/T BAL O/T HRS O/T PAY

> 01 01/08/95 PDEMP,A 000-00-1000 1248.72 0.00 0.00 4.00 87.12

> PDEMP,B 000-00-2000 2491.08 0.00 0.00 12.00 287.88

> PDEMP,C 000-00-3000 1948.76 0.00 0.00 4.00 95.96

> PDEMP,D 000-00-4000 1403.50 0.00 0.00 9.00 202.70

> PDEMP,E 000-00-5000 2203.20 2.00 0.00 0.00 0.00

> ------- ---- ---- ------ ------- P/P-TotaLs: 9295.26 2.00 0.00 29.00 673.66

> ------- ---- ---- ------ ------- TOTALS: 9295.26 2.00 0.00 29.00 673.66

> 02 01/22/95 PDEMP,G 000-00-6000 1804.75 0.00 0.00 5.00 119.95

> PDEMP,H 000-00-7000 1172.49 0.00 0.00 0.50 10.89

> PDEMP,I 000-00-8000 1896.74 0.00 0.00 6.50 155.94

> PDEMP,J 000-00-9000 2238.48 0.00 0.00 32.75 785.68

> PDEMP,K 000-00-1100 1980.70 0.00 0.00 10.00 239.90

> ------- ---- ---- ------ -------- P/P-Totals: 9093.16 0.00 0.00 54.75 1312.36

> ------- ---- ---- ------ ------- TOTALS: 9093.16 0.00 0.00 54.75 1312.36

> DHCP PAID REPORT O001 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

> February 1996 PAID V. 4.0 User Manual 3.43

> Time & Attendance

#### Employee Prior Pay Period Adjustments

This option allows the user to view all audits over a selected date range.

> Select Employee Reports Option: 3 \<RET\> Employee Prior Pay Period

> Adjustments

> Select T&L: 902 \<RET\>

> Enter Beginning Date T//1/1/95 \<RET\> (JAN 01, 1995) Enter Ending Date T//4/28/95 \<RET\> (APR 28, 1995)

> THIS IS AN 80 COLUMN REPORT ! DEVICE: HOME// \<RET\> TERMINAL

> PRIOR PAY PERIOD ADJUSTMENT REPORT DATE: 04/28/95 from JAN 01, 1995 to APR 28, 1995

> for T&L 902

> \|---------------------\|------------\|-\|--\|------------\|------------\|------------\|

> \| \| TIMEKEEPER \| \| \| SUPERVISOR \| APPROVER \| PROCESSOR \|

> \| \|------------\| \| \|------------\|------------\|------------\|

> \|EMPLOYEE \|NAM\| DATE \|\*\|\*\*\|NAM\| DATE \|NAM\| DATE \|NAM\| DATE \|

> \|---------------------\|---\|--------\|-\|--\|---\|--------\|---\|--------\|---\|--------\|

> \|PAIDEMPLOYEE6,TEN \|PDT\|02-10-95\|T\|P \|PDS\|02/13/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,ONE \|PDT\|02-10-95\|T\|P \|PDS\|02/13/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,TWO \|PDT\|02-10-95\|T\|P \|PDS\|02/10/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,THREE \|PDT\|02-21-95\|T\|P \|PDS\|02/21/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,FOUR \|PDT\|02-21-95\|T\|P \|PDS\|02/22/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,FIVE \|PDT\|02-21-95\|T\|P \|PDS\|02/22/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,SIX \|PDT\|02-21-95\|T\|P \|PDS\|02/21/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,SEVEN \|PDT\|03-07-95\|T\|P \|PDS\|03/14/95\|PDA\|03/16/95\|PDP\|03/24/95\|

> \|PAIDEMPLOYEE6,EIGHT \|PDT\|03-14-95\|T\|P \|PDS\|03/20/95\|PDA\|03/20/95\|PDP\|03/21/95\|

> \|PAIDEMPLOYEE6,NINE \|PDT\|04-11-95\|T\|A \|PDS\|04/11/95\|PDA\|04/12/95\| \| \|

> \| \| \| \| \| \| \| \| \| \| \| \|

> \| \*TYPE: T=TIME V=VCS H=HAZARD/ENVIR DIFF \|

> \| \*\*STATUS: R=REQUESTED A=APPROVED P=PAYROLL PROCESSED D=DISAPPROVED \|

> \| X=CANCELLED S=SUPR. APPROVED \|

> \|---------------------\|------------\|-\|--\|------------\|------------\|------------\|

> DHCP PAID REPORT AU01 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

#### Employee Leave Used

This option allows the user to print all previous leave taken by one or all employees over a selected date range.

> Select Employee Reports Option: 4 \<RET\> Employee Leave Used

> Enter employee name: PAIDEMPLOYEE7,TEN \<RET\>

> Report Beginning Date T//T-300 \<RET\> (OCT 06, 1994) Report Ending Date T// \<RET\> (AUG 02, 1995)

> DEVICE: HOME// \<RET\> QUEUE TO PRINT ON

> ..

> LEAVE USED SUMMARY DATE: 08/02/95 from: OCT 06, 1994 to AUG 02, 1995

> for: PAIDEMPLOYEE7,TEN - FISCAL

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> \|PP \|DATE \|TYPE \|FROM \|TO \|LENGTH

> \|

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> \|24 \|Thu 1-Dec-94 \|Sick Leave \|11:00A \|01:00P \| 2.00 Hours

> \|

> \|02 \|Mon 23-Jan-95 \|Sick Leave \|08:00A \|04:30P \| 8.00 Hours

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| TOTALS: Sick Leave 10.00 Hours

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \| \| \| \| \| \|

> \|

> \|---\|--------------\|---------------------\|-------\|-------\|-------------------­

> \|

> DHCP PAID REPORT L003 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 100

> Press Return/Enter to continue. \<RET\>

#### PAID T&L Report

This option allows the user to display and print timekeepers, supervisors and their certifying T&L, and overtime supervisors.

> Select Employee Reports: 5 \<RET\> Paid T&L Report

> Select T&L Unit: 902 \<RET\>

> DEVICE: HOME// \<RET\> HOME

P A I D T & L R E P O R T DATE: 07/06/95

> \| \| \| CERT\|

> \|T&L \|TIMEKEEPER \|SUPERVISOR T&L \|O/T SUPERVISOR

> \|----\|----------------------\|---------------------------\|--------------------­

> \|902 \|PAIDTIMEKEEPR,FOUR \|PAIDSUPERVISR,FOUR 902 \|PAIDSUPERVISR1,SIX

> \| \|PAIDTIMEKEEPR,FIVE \|PAIDSUPERVISR,FIVE 902 \|PAIDSUPERVISR,NINE

> \| \|PAIDTIMEKEEPR,SIX \|PAIDSUPERVISR,SIX 902 \|PAIDSUPERVISR1,TWO

> \| \| \|PAIDSUPERVISR,SEVEN 902 \|PAIDSUPERVISR1,FIVE

> \| \| \|PAIDSUPERVISR,EIGHT 900 \|

> \| \| \|PAIDSUPERVISR,NINE 900 \|

> \| \| \|PAIDSUPERVISR,TEN 902 \|

> \| \| \|PAIDSUPERVISR1,ONE 902 \|

> \| \| \|PAIDSUPERVISR1,TWO 900 \|

> \| \| \|PAIDSUPERVISR1,THREE 902 \|

> \| \| \|PAIDSUPERVISR1,FOUR 902 \|

> \| \| \| \|

> \| \| \| \|

> \| \| \| \|

> \| \| \| \|

> \| \| \| \|

> \|----\|----------------------\|---------------------------\|--------------------­

> DHCP PAID REPORT T001 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

#### Review FY Recess for 9 Month AWS Employee

This view only option displays the Recess Schedule for nurses on the 9 month/3 month alternate work schedule (AWS). To view a 9 month/3 month AWS Recess Schedule, enter the T&L unit of the nurse. At the next prompt, enter the fiscal year or the nurse’s name.

Once the schedule is selected, you may enter actions at the “Select Action” prompt to navigate through the Recess Schedule, print the Recess Schedule and display a summary. Enter a double question mark (??) at this prompt for a list of all available actions.

Following is a list of actions with a brief description. The mnemonic for each action is shown in brackets \[ \] following the action name. Entering the mnemonic is the quickest way to select an action.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recess Hours Summary</p>
<p>[RS]</p>
</blockquote></td>
<td><blockquote>
<p>Enter RS to see a summary screen with recess totals. Be sure to scroll down to see the whole</p>
<p>report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Next Screen [+]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Previous Screen [-]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the previous screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Up a Line [UP]</p>
</blockquote></td>
<td><blockquote>
<p>Move up one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Down a Line [DN]</p>
</blockquote></td>
<td><blockquote>
<p>Move down one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Right [&gt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the right if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Left [&lt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the left if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>First Screen [FS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the first screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Last Screen [LS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the last screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Go to Page [GO]</p>
</blockquote></td>
<td><blockquote>
<p>Move to any selected page in the list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Re Display Screen [RD]</p>
</blockquote></td>
<td><blockquote>
<p>Redisplay the current screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Print Screen [PS]</p>
</blockquote></td>
<td><blockquote>
<p>Print the header and the portion of the list currently displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print List [PL]</p>
</blockquote></td>
<td><blockquote>
<p>Print the list of entries currently displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Search List [SL]</p>
</blockquote></td>
<td><blockquote>
<p>Find selected text in list of entries.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Auto Display(On/Off) [ADPL]</p>
</blockquote></td>
<td><blockquote>
<p>Toggle the menu of actions to be displayed/not displayed automatically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Quit [QU]</p>
</blockquote></td>
<td><blockquote>
<p>Exit the screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Employee Menu Option: Review FY Recess for 9 Month AWS Employee

> Select a Recess Schedule: 2007// \<RET\> PAIDemployee,One 2007 000-00-1111

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Recess</p>
</blockquote></th>
<th><blockquote>
<p>Schedule Viewer</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Jul 17, 2007@13:50:06</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1 of 4</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FY2007</p>
</blockquote></td>
<td><blockquote>
<p>Recess Week Viewer</p>
</blockquote></td>
<td><blockquote>
<p>for</p>
</blockquote></td>
<td><blockquote>
<p>9 month AWS with start</p>
</blockquote></td>
<td><blockquote>
<p>date 1</p>
</blockquote></td>
<td>0/01/06 (</td>
<td>pp 06-20)</td>
</tr>
</tbody>
</table>

> PAIDemployee,One XXX-XX-1111 T&L Unit: 140

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Oct 2006============

> 1 06-20 1 2 3 4 5 6 7 40.00

> 2 8 9 10 11 12 13 14

> 3 06-21 15 16 17 18 19 20 21

> 4 22 23 24 25 26 27 28

> 5 06-22 29 30 31 1 2 3 4 40.00

> =============Nov 2006============

> 6 5 6 7 8 9 10 11 7.00

> 7 06-23 12 13 14 15 16 17 18 40.00

> 8 19 20 21 22 23 24 25

> 9 06-24 26 27 28 29 30 1 2 40.00

> =============Dec 2006============

> 10 3 4 5 6 7 8 9

> 11 06-25 10 11 12 13 14 15 16

> 12 17 18 19 20 21 22 23

> 13 06-26 24 25 26 27 28 29 30

> 14 31 1 2 3 4 5 6

> +---------Enter ?? for more actions-------------------------------------------- RS Recess Hours Summary

> Select Action:Next Screen// rs Recess Hours Summary

> RECESS SCHEDULE SUMMARY Jul 17, 2007@13:50:11 Page: 1 of 1

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20)

> PAIDemployee,One XXX-XX-1111 T&L Unit: 140

> --Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------

> 1 10/01/06 40.00 0.00

> 5 10/29/06 40.00 0.00

> 6 11/05/06 7.00 0.00

> 7 11/12/06 40.00 0.00

> 9 11/26/06 40.00 0.00

> 27 04/01/07 40.00 0.00

> 28 04/08/07 40.00 0.00

> ====== ====== Total Recess. Scheduled: 247.00 Posted: 0.00

> Total Weeks in AWS FY Schedule: 54.00

> Total available FY recess hrs: 540.00 (13.5 weeks) WARNING--Recess hours under scheduled: 293.00

> ----------WARNING--Recess hours are under scheduled: 293.00-------------------- Select Action:Quit//

#### Display Employee Tour Hours

This option allows payroll staff to view any employee's tour of duty number, tour of duty hours, tour hours on each day and 8B normal hours. The Tour Hours column contains a total of any tour hours that fall on that day; therefore, two day tours will contribute hours to both days on which they fall.

Users can also choose to print the footnotes explaining the report headings.

> Select Employee Reports Option: Display Employee Tour Hours \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE,ONE \<RET\> 000-01-4202

> 000-01-4202

> Select PAY PERIOD: 08-08 \<RET\>

> Include report footnotes? N// y \<RET\> YES

> DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> VA TIME & ATTENDANCE REPORT for Payroll--NOV 07, 2008@09:08 p1

> Display Employee Tour Hours: PP 08-08 (13-Apr-08 thru 26-Apr-08)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EMPLOYEE NAME</p>
</blockquote></th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>8B NRM HRS</p>
</blockquote></th>
<th><blockquote>
<p>ToD HRS*</p>
</blockquote></th>
<th><blockquote>
<p>IEN 450</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>======================</p>
</blockquote></td>
<td><blockquote>
<p>===========</p>
</blockquote></td>
<td><blockquote>
<p>==========</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PAIDEMPLOYEE,ONE 000-01-4202 40 40 14202

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Day</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 1</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 2</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>---</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mon</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter RETURN to continue or '^' to exit: \<RET\>

> March 2018 PAID V. 4.0 User Manual 3.51

> Time & Attendance

> =================================================================

> FOOTNOTES TO REPORT HEADINGS

> ============================

> \*ToD HRS (Tour of Duty Hours) The total Tour of Duty hours that fall within the

> -------- two week pay period, beginning midnight Saturday. Hours that cross midnight from a tour that starts on the last day of a pay period will appear on the following pay period.

> .....................................................................

> \*Hours (DAILY TOUR HOURS) This column contains actual tour hours that fall

> ------ on that day from the 24 hour period beginning at midnight. A two day tour will contribute hours to each day the tour falls on. Hours

> that cross midnight from a tour that starts on the last day of a pay

> period will appear on the following pay period.

> .....................................................................

> \*ToD \# (Tour of Duty Number) The tour's entry number in the Tour

> ------ of Duty file (#457.1)

> .....................................................................

> Enter return to continue.

## Chapter 4. Payroll Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Payroll Supervisor's menu. The options on this menu allow the user to perform the tasks needed to process a station's time and attendance reports.

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Open Next Pay Period</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Un-Reviewed Employees (All T&amp;Ls)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>8B Edit Checks</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Transmit 8B Data to Austin</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Transmission History</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Payroll Table Maintenance ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Tour of Duty</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit T&amp;L Unit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Set Holiday Benefit Day</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>List Supervisors Certified by a T&amp;L</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Payroll Main Menu ...</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Open Next Pay Period

This option opens the new pay period for time and attendance report processing. This should be done by COB on the second Thursday of the current pay period. This allows timekeepers the maximum amount of time to post tours for the new pay period; also allows time for holidays to move backwards, if necessary, prior to posting. This option works like "Load 8B Data from Austin", except the records are created by this application and not transmitted from Austin via telecom mail messaging. This option populates the new pay period tour of duty files with the permanent tour of duty in the previous pay period. Any second tours are NOT carried over.

> Select Payroll Supervisor Menu Option: 1 \<RET\> Open Next Pay Period Do you wish to Open Pay Period 95-05 beginning 5-Mar-95 ? Y \<RET\> Moving Current Employees into Pay Period ... ..

> 228 Employee Records created.

#### Un-Reviewed Employees (All T&Ls)

This option allows the user to select the pay period and the T&L Unit (or ALL T&L Units) and displays the status of the employees. Payroll uses this option to track attendance data in relationship to the location of the record -- "Timekeeper" or "Payroll".

The "status" of the time and attendance reports will be "Timekeeper" until they are certified by the supervisor, then the status will be "Payroll". If time and attendance reports are returned to the timekeeper, the status will again be "Timekeeper". If time and attendance reports have been transmitted, they will not appear on the list.

> Select Payroll Supervisor Menu Option: 2 \<RET\> Un-Transmitted Employees (All

> T&Ls)

> Select TIME & ATTENDANCE RECORDS PAY PERIOD: 92-24// \<RET\>

> Select T&L Unit (or ALL): 100 \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 32%" />
<col style="width: 35%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Un-Transmitted</p>
</blockquote></th>
<th><blockquote>
<p>Employees for 92-24</p>
</blockquote></th>
<th><blockquote>
<p>NOV 25,1992@13:56:30</p>
</blockquote></th>
<th><blockquote>
<p>Page 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>T&amp;L</p>
</blockquote></td>
<td><blockquote>
<p>STATUS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> -----------------------------------------------------------------------------

#### 8B Edit Checks

This option detects most of the 8B records that would be rejected by the Austin Automation Center. This function is optional, but is strongly recommended that it be used. Only records that have been released to Payroll will go through the 8B edit checks when this option is selected.

> Select Payroll Supervisor Menu Option: 3 \<RET\> 8B Edit Checks

> Select T&L (or ALL): ALL \<RET\>

> Select TIME & ATTENDANCE RECORDS PAY PERIOD: 93-03// \<RET\>

> DEVICE: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> 000-00-0071 PAIDEMPLOYEE7,ONE 116

> AN010 NA200 PT320 AL010 US012 NR200 OE292 PH042 DE002

> PT + PH must equal Normal Hours unless FF is coded

> 000-00-0072 PAIDEMPLOYEE7,TWO 116

> NA200 OA272 NR200 OE272

> With Duty Basis 2, PT and PH must be coded unless the Pay Plan is L, M

> or N and the Normal Hours are 1

> Press RETURN to Continue. \<RET\>

#### Transmit 8B Data to Austin

This option will transmit all 8B records that have been reviewed by Payroll to the Austin Automation Center.

> Select Payroll Supervisor Menu Option: 4 \<RET\> Transmit 8B Data to Austin

> Select TIME & ATTENDANCE RECORDS PAY PERIOD: 93-03// \<RET\>

> Ready to Transmit to Austin? NO// YES \<RET\>

> Transmitting to Austin

> 502 Employees Processed

#### Transmission History

This option will provide a summary of information concerning a selected pay period including the number of records transmitted, the number of mail messages sent, the number of mail messages acknowledged from Austin, the clerk who transmitted the records and the date/time of data transmission to Austin.

> Select Payroll Supervisor Option: 5 \<RET\> Transmission History

> Select TIME & ATTENDANCE RECORDS PAY PERIOD: 93-03// \<RET\>

> Transmission History for Pay Period 03

> Transmitting Cl PAIDUSER,TWO

> Total Number of Messages for Transmission: 1

> Number of Messages Acknowledged by Austin: 1

> Press RETURN to Continue. \<RET\>

#### Payroll Table Maintenance

This option is a submenu on the Payroll Supervisor's Menu. The options on this submenu allow the user to display Special Tour Indicators, Types of Time, Time Remarks and Entitlement Table entries.

> Select Payroll Supervisor Menu Option: 6 \<RET\> Payroll Table Maintenance

> 1 Display Special Tour Indicator

> 2 Display Type of Time Table

> 3 Display Time Remarks

> 4 Display Entitlement Table

#### Display Special Tour Indicator

This option displays a list of the special tour indicators, the type of time associated with each indicator and the indicator's code.

> Select Payroll Table Maintenance Options: 1 \<RET\> Display Special Tour

> Indicator

> DEVICE: \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 27%" />
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SPECIAL</p>
</blockquote></th>
<th><blockquote>
<p>TOUR INDICATOR</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>JAN 28, 1993 11:18</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>TYPE</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OF</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td>TIME</td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> -----------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>No Premium Pay</p>
</blockquote></th>
<th><blockquote>
<p>RG</p>
</blockquote></th>
<th>8</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>On-Call</p>
</blockquote></td>
<td><blockquote>
<p>ON</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Phy/Den Core Hours</p>
</blockquote></td>
<td><blockquote>
<p>RG</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Scheduled</p>
</blockquote></td>
<td><blockquote>
<p>Comp Time</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduled</p>
</blockquote></td>
<td><blockquote>
<p>Overtime</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Shift 2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>RG</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift 3</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>RG</p>
</blockquote></td>
<td>7</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Standby</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SB</p>
</blockquote></td>
<td>4</td>
</tr>
</tbody>
</table>

#### Display Type of Time Table

This option displays a list of the various types of time that may be coded on a time and attendance report. The code, a short description and a long description are displayed for each entry.

> Select Payroll Table Maintenance Option: 2 \<RET\> Display Type of Time Table

> DEVICE: \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> TYPE OF TIME AUG 10,1995 11:38 PAGE 1

> SHORT

> CODE DESCRIPTION LONG DESCRIPTION

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AA</p>
</blockquote></th>
<th><blockquote>
<p>AUTH ABS</p>
</blockquote></th>
<th><blockquote>
<p>Authorized Absence</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AD</p>
</blockquote></td>
<td><blockquote>
<p>ADOPT</p>
</blockquote></td>
<td><blockquote>
<p>Adoption</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AL</p>
</blockquote></td>
<td><blockquote>
<p>ANNUAL LV</p>
</blockquote></td>
<td><blockquote>
<p>Annual Leave</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CB</p>
</blockquote></td>
<td><blockquote>
<p>FAM CARE</p>
</blockquote></td>
<td><blockquote>
<p>Family Care &amp; Bereavement</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>COP</p>
</blockquote></td>
<td><blockquote>
<p>Continuation of Pay</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td><blockquote>
<p>COMP ERND</p>
</blockquote></td>
<td><blockquote>
<p>Compensatory Time Earned</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CU</p>
</blockquote></td>
<td><blockquote>
<p>COMP USED</p>
</blockquote></td>
<td><blockquote>
<p>Compensatory Time Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>DONOR LV</p>
</blockquote></td>
<td><blockquote>
<p>Donor Leave</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HW</p>
</blockquote></td>
<td><blockquote>
<p>HOL WK</p>
</blockquote></td>
<td><blockquote>
<p>Holiday Worked</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HX</p>
</blockquote></td>
<td><blockquote>
<p>HOL EX</p>
</blockquote></td>
<td><blockquote>
<p>Holiday Excused</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>MIL LV</p>
</blockquote></td>
<td><blockquote>
<p>Military Leave</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>N/P A/L</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay Annual Leave</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NP</p>
</blockquote></td>
<td><blockquote>
<p>NON PAY</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ON</p>
</blockquote></td>
<td><blockquote>
<p>ON-CALL</p>
</blockquote></td>
<td><blockquote>
<p>On-Call</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>OVERTIME</p>
</blockquote></td>
<td><blockquote>
<p>Overtime</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TYPE OF TIME AUG 10,1995 11:38 PAGE 2

> SHORT

> CODE DESCRIPTION LONG DESCRIPTION

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 30%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>RG</p>
</blockquote></th>
<th><blockquote>
<p>REG TIME</p>
</blockquote></th>
<th><blockquote>
<p>Regular Scheduled Time</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>RES ANN LV</p>
</blockquote></td>
<td><blockquote>
<p>Restored Annual Leave</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SB</p>
</blockquote></td>
<td><blockquote>
<p>STANDBY</p>
</blockquote></td>
<td><blockquote>
<p>Standby</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>SICK LV</p>
</blockquote></td>
<td><blockquote>
<p>Sick Leave</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TR</p>
</blockquote></td>
<td><blockquote>
<p>TRAINING</p>
</blockquote></td>
<td><blockquote>
<p>Training</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TV</p>
</blockquote></td>
<td><blockquote>
<p>TRAVEL</p>
</blockquote></td>
<td><blockquote>
<p>Travel</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UN</p>
</blockquote></td>
<td><blockquote>
<p>UNAVAIL</p>
</blockquote></td>
<td><blockquote>
<p>Unavailable</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>LWOP</p>
</blockquote></td>
<td><blockquote>
<p>Leave Without Pay</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Display Time Remarks

This option displays a list of the various time remarks. For each time remark, the code, its description and the applicable types of time associated with it are displayed.

> Select Payroll Table Maintenance Option: 3 Display Time Remarks

> DEVICE: \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> REMARKS TABLE JUL 17,2007 11:52 PAGE 1

> CODE DESCRIPTION APPLICABLE TYPES OF TIME

> -----------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 21%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>SF71 on file</p>
</blockquote></th>
<th colspan="3"></th>
<th><blockquote>
<p>AL</p>
</blockquote></th>
<th><blockquote>
<p>AA</p>
</blockquote></th>
<th><blockquote>
<p>DL CU ML RL SL CB AD WP NL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>AWOL</p>
</blockquote></td>
<td colspan="3"></td>
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>On Suspension</p>
</blockquote></td>
<td colspan="3"></td>
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>AA Granted by</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Supr.</p>
</blockquote></td>
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Jury Duty</p>
</blockquote></td>
<td colspan="3"></td>
<td><blockquote>
<p>AA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>Shift Coverage</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>RG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>OT while in Travel</p>
</blockquote></td>
<td><blockquote>
<p>Status</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>OT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>OT/CT on Premium</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>T&amp;L</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td><blockquote>
<p>RG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Pre-Scheduled</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Tour Coverage</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CB - Non-Premium</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>T&amp;L</p>
</blockquote></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CB - Premium T&amp;L</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>CompTime--No</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>Remark</p>
</blockquote></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>Credit Hours</p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CU</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 17 OT/CT With Premiums OT CT RG HW

#### Display Entitlement Table

This option displays the various entitlement tables used in the PAID V. 4.0 package. An entitlement table displays the various types of premiums/benefits to which an employee is entitled (Yes) or not entitled (No) and whether an employee's time is figured in hours (Hrs.) or days.

Every employee must have an entitlement table, since these entitlements are used to calculate an employee's biweekly compensation. An employee's entitlement table is determined by a combination of various fields in the employee's master file. The three main fields are Pay Plan, Duty Basis, and FLSA (Fair Labor Standards Act) Indicator.

To see an entitlement table for a General Schedule (A), Full Time (1), Non- Exempt (N) employee, the user must enter the following at the "Select PAY ENTITLEMENT NAME:" prompt: A 1 N. In many instances other fields in combination with an employee's Pay Plan, Duty Basis, and FLSA Indicator are also considered in determining an employee's entitlements, such as Normal Hours, Premium Pay Indicator, Pay Basis, etc. Therefore, the user may be asked to make a selection based on other factors as in the example below.

> Select Payroll Table Maintenance Option: 4 Display Entitlement Table

> Select PAY ENTITLEMENT NAME: A 1 N

> 1 A 1 N

> 2 A 1 N NH\>80

> 3 A 1 N PPI=C

> 4 A 1 N PPI=R

> 5 A 1 N PPI=S

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 A 1 N

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> Name: A 1 N

PAY ENTITLEMENT TABLE

> Regular Scheduled Hrs. Hrs. \> 8 - 2 No Regular Unscheduled No Hrs. \> 8 - 3 No FF Reg. Sch. Hrs. Over 53 No Holiday - Day Yes Reserved for future use No Holiday - 2 No Recess Periods No Holiday - 3 No Night Differential - 2 Yes Holiday OT No Night Differential - 3 No On Call No Saturday Premium No Sleep Time No Sunday - Day Yes CompTime/CreditHrs Earn/Use Yes Sunday - 2 No Standby No Sunday - 3 No Annual/Restored Leave Yes Overtime - Day Yes Sick Leave Yes

> Payroll Supervisor Menu

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 10%" />
<col style="width: 38%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Overtime - 2</p>
</blockquote></th>
<th><blockquote>
<p>No</p>
</blockquote></th>
<th><blockquote>
<p>NonPay Annual Leave</p>
</blockquote></th>
<th><blockquote>
<p>No</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Overtime - 3</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>AWOL/Susp/LWOP</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hazardous Duty</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Military Leave</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Environmental Differential</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Authorized Absence</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduled CB OT</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Travel OT</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Continuation of Pay</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hrs. &gt;8 - Day</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>VCS Commission Sales</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to Continue.

#### Enter/Edit Tour of Duty

This option allows the user to create new tours or to edit existing tours. The creation (and assignment) of tours of duty is paramount in the proper execution of this package. Following is a list and description of the fields that should be completed when entering or editing a tour.

<u>Tour of Duty</u>: This is the name of the tour and is a mandatory field. This name is what the timekeeper will see when assigning a tour to an employee; therefore, it should be as descriptive as possible in the limited space. For instance, if you create two 03:30P-MID tours, where one is created for an employee who actually works those hours and the other is created for an employee who is on-call for those hours, the first tour should be 03:30P-MID and the second should be 03:30P­ MID (on-call).

<u>Tour Hours</u>: Same as Tour of Duty, however, this prompt allows you to edit the name. You are not allowed to delete a tour. However, tours can be inactivated. To inactivate a tour, remove all T&Ls that were assigned to it (see ALL T&Ls below).

<u>Description</u>: Payroll can enter a short description (3-30 characters in length) of the tour. This field is optional since the data will only be displayed with this option and the Payroll Main Menu option "Display Tour of Duty" and is for Payroll's use or information only.

<u>Meal Time</u>: This is a mandatory field. The length of the meal time must be entered in minutes (0, 15, 30, 45 or 60) to enable the system to properly deduct the meal period from the tour hours. For instance, if you have two tours from

08:00A-04:30P and the first tour has a 30 minute meal time while the second tour has a 60 minute meal time the system will recognize the first tour as eight hours long and the second tour as seven hours and 30 minutes long. If the tour has no meal time, Payroll must enter the number zero (0). The user will not be allowed to save the tour or exit the screen if this field is left blank.

<u>Meal on Premium Time</u>: Enter "yes" if the meal is eaten on premium time and "no" if it is eaten on non-premium time. Premium time is between 06:00P and 06:00A. If this field is left blank, it will automatically be set to "no". The system uses this field to determine, under certain circumstances, how lunch should be subtracted when computing night differential.

<u>All T&Ls</u>: The user should answer "yes" or "no" to this question. If this field is left blank, it will automatically be set to "no". If this question is answered with "yes", all T&L Units will be allowed to assign this tour to their employees. If "no" is entered the user will be shown a second screen (upon exiting the current one) at which time he/she will be able to enter individual T&L Units. (To inactivate a tour, make sure that "no" is answered to this question and all T&Ls associated with this tour are deleted.

<u>Two-Day Tour</u>: The user should answer "yes" or "no" to this question. If this is left blank, it will automatically be set to "no". For the purpose of answering this question, one day is considered to be a 24 hour period ending at midnight. A "yes" must be answered here for the system to work correctly if any part of the tour crosses midnight into another day (or 24 hour period). For example, let us assume that we have set up a tour with two segments (parts) where an employee will work from 03:30P-MID (segment one); then the employee will be on call from MID-08:00A (segment two). Since both of these segments are defined here as part of our tour and the second segment is in the next 24 hour period (crossed over midnight), this tour must be marked as a two-day tour. A "no" should be answered here if all segments are within a 24 hour period ending at midnight.

An example of this would be if we set up a tour with two segments where the employee would be on-call from MID-08:00A (segment one) and would work from 08:00A-04:30P (segment two). Since no part of either of the segments crosses over into another 24 hour period, this tour would not be considered a two-day tour.

The next three prompts are all related to a tour segment (or part). Each tour must have at least one segment but cannot have more than seven. Each segment of a tour must have a start time and stop time (code is optional but extremely important to the system in computing time and some premiums). Under no circumstances should the total hours of a tour exceed 24 consecutive hours.

<u>START</u>: The start time of one segment or one part of a tour (i.e., 08:00A).

<u>STOP</u>: The stop time of one segment or one part of a tour (i.e., 04:30P). Each start time must have a stop time, therefore, if this stop time is associated with the start time above, this tour segment would be 08:00A-04:30P).

<u>CODE</u>: This field is used to define "special features" of a tour segment by entering a Special Tour Indicator. If this code field is associated with the above start and stop times and this field is left blank, the system would assume that this is an 08:00A-04:30P tour and any employee assigned this tour would work those hours. However, if this code field is associated with the above start and stop times and we enter in a Special Tour Indicator of On-Call, the system would now assume that any employees this tour is assigned to would only be On-Call for those hours (see Special Tour Indicator definitions later in this section for a list of the available Special Tour Indicators and their descriptions). If the timekeeper edits a tour of duty after it has been assigned to an employee, the new characteristics of that tour of duty will only apply to the new employee that it has been assigned. (The new characteristics of that tour of duty will not apply to the employee that it was originally assigned.)

The following shows how to edit an already existing tour and all screens associated with that tour:

=

> Select Payroll Supervisor Menu Option: 7 \<RET\> Enter/Edit Tour of Duty

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> Select Tour of Duty: ?? \<RET\>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 17%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CHOOSE</p>
</blockquote></th>
<th><blockquote>
<p>FROM:</p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>07:00A-03:30P</p>
</blockquote></td>
<td><blockquote>
<p>Meal:</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>08:00A-10:00A</p>
</blockquote></td>
<td><blockquote>
<p>Meal:</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>07:30A-04:00P</p>
</blockquote></td>
<td><blockquote>
<p>Meal:</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>08:00A-11:00A</p>
</blockquote></td>
<td><blockquote>
<p>Meal:</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 15 07:45A-04:15P (5P-6P OC) Meal: 30

> YOU MAY ENTER A NEW TOUR OF DUTY, IF YOU WISH

> Answer must begin with format like 08:00A-04:30P; MID or NOON may also

> be used.

> Select TOUR OF DUTY: 10 \<RET\> 07:00A-03:30P Meal: 30

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> 7

> COMMAND: Press \<PF1\>H for help INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> <u>Meal Time</u>: 30 Meal on Premium Time? NO

> All T&Ls? NO Two-Day Tour? NO START STOP CODE

> 1 07:00A 03:30P

> 2

> 3

> 4

> 5

> 6

> 7

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT \<RET\> INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: 005 \<RET\>

> COMMAND: PRESS \<PF1\>H for help INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: 005

> ASSOCIATED T&L UNIT: 005 \<RET\>

> COMMAND: Press \<PF1\>H for help INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: 005

> ASSOCIATED T&L UNIT: 005

> Close Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: Close \<RET\> INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: ?? \<RET\>

> CHOOSE FROM:

> 005

> 100

> 111

> 105

> Press RETURN to continue, '^' to exit: ^ \<RET\>

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: 111 \<RET\>

> 111

...OK? YES// \<RET\>

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: 111 \<RET\>

> ASSOCIATED T&L UNIT: 111 \<RET\>

> Close Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: Close \<RET\> INSERT

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> <u>Tour Hours</u>: 07:00A-03:30P Description:

> Select ASSOCIATED T&L UNIT: \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT \<RET\>

> VA TIME & ATTENDANCE SYSTEM TOUR OF DUTY

> Select TOUR OF DUTY: ^ \<RET\>

The following is an example of entering a new tour.

> Select TOUR OF DUTY: 06:00A-03:30P \<RET\>

> ARE YOU ADDING '06:00A-03:30P' AS A NEW TOUR OF DUTY? Y \<RET\> (YES)

> VA TIME & ATTENDANCE SYSTEM

> TOUR OF DUTY

> Tour Hours: 06:00A-03:30P Description:

> Meal Time: 30 \<RET\> Meal on Premium Time? NO All T&Ls? NO Two-Day Tour? YES \<RET\>

> START STOP CODE

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p><strong>6A</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>3:30P</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p><strong>3:30P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>11:30P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>2 &lt;RET&gt;</strong> Scheduled Comp Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p><strong>11:30P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>6A</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>5 &lt;RET&gt;</strong> On-Call</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Exit</p>
</blockquote></td>
<td><blockquote>
<p>Save</p>
</blockquote></td>
<td><blockquote>
<p>Refresh</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: E \<RET\>

> Save Changes before leaving form (Y/N)? Y \<RET\> YES

#### Special Tour Indicators

When creating tours with special features such as tours with standby hours and scheduled overtime, the hours which reflect these special features need to have the special tour indicator placed in the code field. Typing a "?" in the code field will give you a list of the special tour indicators. Following are definitions of the tour indicators:

1.  Scheduled Overtime

This special tour indicator is used to indicate that a segment of overtime is part of the employee's normal tour of duty. By having this overtime established as part of the tour, this automatically entitles the employee to night differential pay for hours falling within the night differential time frame.

2\. Scheduled Compensatory Time

This special tour indicator is used to indicate that a segment of compensatory time is part of the employee's normal tour of duty. By having compensatory time established as part of the tour, this automatically entitles the employee to night differential compensation for hours falling within the night differential time frame.

3\. Phy/Den Core Hours - Part Time Physicians

This tour indicator is used for part time physicians with adjustable hours in order to distinguish between core and non-core hours. The functionality of adjustable hours for part time physicians is limited in this version of PAID.

4\. Standby - General Schedule and Per Annum Employees of the Veterans Canteen Service

By having the standby tour indicator established, this ensures that an employee who is officially scheduled to be on standby outside of his/her regularly scheduled duty hours is entitled to receive standby premium pay.

5\. On-Call - Nurses and General Schedule Employees Subject to On-Call Provisions of Title 38 (Premium Pay Code "W")

By having the on-call tour indicator established, this ensures that an employee who is officially scheduled to be on call outside of his/her regularly scheduled duty hours shall receive pay for each hour of on-call duty, except for such times as he/she may be called back to perform overtime work, at a pre-determined rate of his/her overtime pay. When called back to perform overtime work, an employee will receive overtime pay in accordance to subparagraph 105.05 of MP­6, Part V. On-call pay will be suspended during the period of actual overtime duty.

6\. SHIFT 2 - Wage Employees, Non Appointed Fund and Retail Clerical and Administrative Employees of Veterans Canteen Service, and Purchase and Hire Employees

This tour indicator must be used when creating a tour for employees who are entitled to Shift 2 differential. For the Shift 2 differential to be computed, this tour indicator must be used when creating the tour. For example, if a wage employee has a scheduled tour from 11:30A to 8:00P with no tour indicator specified, Shift 2 differential will not be computed (or reported) for this employee. However, if this tour is created with a Shift 2 tour indicator, Shift 2 differential will be computed and reported as appropriate.

7\. SHIFT 3 - Wage Employees, Non Appointed Fund and Retail Clerical and Administrative Employees of Veterans Canteen Service, and Purchase and Hire Employees

This tour indicator must be used when creating a tour for employees who are entitled to Shift 3 differential. Per MP-6, PART V, these employees are entitled to pay at a scheduled rate plus a differential of 10% of the scheduled rate for regularly scheduled non-overtime work when a majority (five or more of the regularly scheduled eight-hour shift) occurs between 11:00P and 8:00A. For the Shift 3 differential to be computed, this tour indicator must be used when creating the tour. For example, if a wage employee has a scheduled tour from MID-8:30A with no tour indicator specified, Shift 3 differential will not be computed (or reported) for this employee. However, if this tour is created with a Shift 3 tour indicator, Shift 3 differential will be computed and reported as appropriate.

8\. No Premium Pay

This tour indicator is used when no night differential, Saturday or Sunday premiums are to be paid for this segment. It is particularly useful for educational tours where the hours are for the convenience of the employee.

#### Enter/Edit T&L Unit

The user may use this option to add new Time and Leave Units (T&Ls) or to make changes to existing T&Ls. When exercising this option the user will see the screen depicted below.

<u>Code:</u> Will be prefilled from the previous screen which asked for the T&L. Name: Is an optional, free-text field where the user can put a description of the T&L.

<u>Station \#:</u> Is prefilled with the customer's station number. If your station services a cemetery or another VA site, the user may change the number in this field.

<u>Service:</u> Is an optional, Service/Section file which can be used to list the service this T&L belongs to, i.e., nursing.

<u>Section:</u> Is an optional, free-text field which can be used to define the part of a service the T&L belongs to, i.e., within Nursing Service, this unit could be CCU.

<u>Time SleepTime Begins:</u> T&Ls where stand-by hours are worked must have pre­

Defined sleep periods. The start time for those eight-hour periods must be defined here. This is not an optional field. It must, therefore, have a value. If there are no stand-by tours on this T&L, it is recommended that the user enter 10:00P.

<u>Entitled Sat/Sun Premiums?</u> Some T&L sections are closed on one or both of the weekend periods except for occasional overtime. Employees working overtime on those units are not entitled to Saturday or Sunday premium pay. If a T&L Code is assigned to a unit such as Fiscal Service, Personnel Service and in most instances, O.R., answer "no" at this prompt.

<u>Select Timekeeper, Supervisor, OT/CT Approver:</u> These prompts work on the same concept. Each field may have more than one person designated as timekeeper, supervisor or approver. The employee selected must be in the employee-file. That employee must have a master record that has been established.

If a supervisor is in the same T&L of the employees that he supervises, another supervisor MUST also be assigned to that T&L so as to approve his leave. In this case, the T&L which certifies the supervisor will be his own T&L. The user can also indicate a T&L other than the supervisor's T&L, in which case all approvals and certifications for the supervisor's leave, timecard, etc., will be done by a supervisor in the other T&L. This is usually the case with Service Chiefs.

If the user enters a three digit code that is not an existing T&L, the system will ask if you are creating a new one. This will allow you to put in a correct code if the first was in error. If you are adding a new one merely type "Y " \<RET\>.

> Select Payroll Supervisor Menu Option: 8 \<RET\> Enter/Edit T&L Unit

> VA TIME & ATTENDANCE SYSTEM TIME & LEAVE UNIT

> Select T&L Unit: 101 \<RET\>

> VA TIME & ATTENDANCE SYSTEM TIME & LEAVE UNIT

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 50%" />
<col style="width: 21%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>CODE</u>:</p>
</blockquote></th>
<th><blockquote>
<p>101</p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME: <u>STATION #</u></p>
</blockquote></td>
<td><blockquote>
<p>TEST1</p>
<p>111</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SERVICE:</p>
</blockquote></td>
<td><blockquote>
<p>INFORMATION SYSTEMS CENTER</p>
</blockquote></td>
<td><blockquote>
<p>SECTION:</p>
</blockquote></td>
<td><blockquote>
<p>SUPPORT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Time SleepTime Begins</u>: 10:00P <u>Entitled Sat/Sun Premiums?</u> YES

> Select TIMEKEEPER: PAIDTIMEKEEPR,SEVEN Select SUPERVISOR: PAIDSUPERVISR1,SEVEN Select OT/CT APPROVER: PAIDUSPERVISR1,EIGHT

> COMMAND: Press \<PF1\>H for help INSERT

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT \<RET\> INSERT

#### Set Holiday Benefit Day

This option allows the Payroll supervisor to set a benefit day for any date for which a time record exists.

> Select Payroll Supervisor Menu Option: 9 \<RET\> Set Holiday Benefit Day

> VA TIME & ATTENDANCE SYSTEM SET EMPLOYEE HOLIDAY

> Select T&L Unit: 100 \<RET\>

> Benefit Date: 12/26/94 \<RET\> (DEC 26, 1994)

> Select EMPLOYEE: PAIDEMPLOYEE7,THREE PAIDEMPLOYEE7,THREE 000-00-0073... done

#### List Supervisors Certified by a T&L

This option allows Payroll users to display all supervisors in other T&Ls which are approved by a selected T&L.

> Select Payroll Supervisor Menu Option: 10 \<RET\> List Supervisors Certified by a T&L

> Select T&L Unit: 100 \<RET\>

> Employees outside of this T&L who are Certified by this T&L:

> PAIDEMPLOYEE7,FOUR PAIDEMPLOYEE,FOUR

> Do you wish to Re-Build this Index? No//

#### Payroll Main Menu

Instructions for using this menu can be found under Payroll Main Menu, beginning with "Pay Period Exceptions" option.

> Select Payroll Supervisor Menu Option: 11 \<RET\> Payroll Main Menu

## Chapter 5. T&A Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Time and Leave Unit (T&L) Supervisor's menu and should be assigned to supervisors who are responsible for signing the time and attendance reports of one or more T&Ls. All options under this menu are the same as the options listed under the T&A OT/Supervisor's menu with an exception of Approve OT/CT. (See the T&A OT/Supervisor's menu to Approve OT/CT.)

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Supervisory Approvals</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Pay Period Certification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>List Leave Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Balances</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Display OT/CT Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>List Daily Exceptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Display Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Display Employee Tour of Duty</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Display Employee Pay Period</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>List Tours by T&amp;L</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>List Environment Diff. Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>List Un-Certified Employees</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>List Prior Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Employee Reports...</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Supervisory Approvals

This option lists each action (tour changes, leave and OT/CT requests) that a supervisor needs to review and certify, in alphabetical order by employee. Supervisors see messages when they sign on showing how many actions in each T&L need to be approved. The supervisor may, upon review, approve by typing the letter "A" at the prompt, disapprove by typing "D", cancel by typing "X", or ignore the action by pressing the return key. When leave is approved, a projected leave balance is calculated, and if that balance is negative, the supervisor receives a message. All items displayed must be acted upon by the supervisor before the end of the pay period. Some actions, when ignored, will not allow the employee's time to be passed on to Payroll and could result in a mis-payment or no payment at all.

The supervisor must have an electronic signature on file in order to Approve, Disapprove, or Cancel any request. See the Electronic Signature section of this manual for an example on how to create an electronic signature.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

Supervisors must act on each employee’s timecard by selecting an appropriate Disposition from the option list (Approve, Disapprove, Cancel, or Bypass).

> Select T&A Supervisor Menu Option: 1 \<RET\> Supervisory Approvals

VA TIME & ATTENDANCE SYSTEM

SUPERVISOR'S APPROVALS

PAIDEMPLOYEE,FNAME Telework Indicator: E 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex:

Tour Change

Date TW Scheduled Tour TW Permanent Tour Type

Sun 6-May-12 DAY OFF 03:30P-MID Perm

Mon 7-May-12 07:00A-03:30P 03:30P-MID Perm

Tue 8-May-12 07:00A-03:30P DAY OFF Perm

Wed 9-May-12 07:00A-03:30P 07:30A-04:00P Perm

Thu 10-May-12 REG 07:00A-03:30P 07:30A-04:00P Perm

Fri 11-May-12 REG 07:00A-03:30P 07:30A-04:00P Perm

Mon 14-May-12 07:00A-03:30P 07:30A-04:00P Perm

Tue 15-May-12 07:00A-03:30P 07:30A-04:00P Perm

Wed 16-May-12 07:00A-03:30P 03:30P-MID Perm

Thu 17-May-12 REG 07:00A-03:30P DAY OFF Perm

Fri 18-May-12 REG 07:00A-03:30P 07:30A-04:00P Perm

Sat 19-May-12 DAY OFF 03:30P-MID Perm

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass):

T&A Supervisor Menu

> Prior Pay Period Change

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Thu 4-Aug-94 04:00P-MID 04:00P-MID SL SICK LV

> Shift 2 SF71 on file

> Caught virus.

> Change Remarks: Employee called in for SL

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass): \<RET\>

> VA TIME & ATTENDANCE SYSTEM SUPERVISOR'S APPROVALS

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 40%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE7,SIX</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>000-00-0076</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
<p>T&amp;L: 111</p>
</blockquote></td>
<td><blockquote>
<p>Normal Hours: 80</p>
<p>Pay Plan: A</p>
</blockquote></td>
<td><blockquote>
<p>Duty Basis: 1</p>
<p>Comp/Flex:</p>
<p>FLSA: E</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 1-Mar-94 3 Hrs. COMP TIME on T&L 123 Requested

> WORKED LATE

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass): \<RET\>

> VA TIME & ATTENDANCE SYSTEM SUPERVISOR'S APPROVALS

> PAIDEMPLOYEE7,SEVEN 000-00-0077

> Station: 101 Normal Hours: 80 Duty Basis: 1

> T&L: 102 Pay Plan: A Comp/Flex:

FLSA: E

> 15-Jul-95 2 Hrs. OVERTIME (\$102.31) on T&L 102 Requested

> PROJECT MUST BE COMPLETED BY MONDAY NEXT WEEK.

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass): \<RET\>

> T&A Supervisor Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>VA TIME &amp; ATTENDANCE SYSTEM</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p>SUPERVISOR'S APPROVALS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PAIDEMPLOYEE7,EIGHT</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>000-00-0078</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td><blockquote>
<p>Normal Hours:</p>
</blockquote></td>
<td><blockquote>
<p>48</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Duty Basis: 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T&amp;L:</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Comp/Flex:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td>E</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SL Leave Balance:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>80.250 as of Sat 3-Sep-94</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SL Estimated Earnings:</p>
</blockquote></td>
<td><blockquote>
<p>46.000</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SL Estimated Usage:</p>
</blockquote></td>
<td><blockquote>
<p>1.500</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SL Projected Balance:</p>
</blockquote></td>
<td><blockquote>
<p>124.750</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 02:00P 10-Jul-95 to 03:30P 10-Jul-95 1.5 hrs Sick Leave Requested

> Requested: 10-Jul-95 8:52am

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass): SL Leave Balance: 80.250 as of Sat 3-Sep-94

> SL Projected Balance: 80.250

> 07:00A 1-Jan-94 to 03:00P 1-Jan-94 7.5 hrs Sick Leave Requested

> Requested: 10-Jul-95 12:28pm

> Disposition (A=Approve, D=Disapprove, X=Cancel, RETURN to bypass): A \<RET\>

> Enter Signature Code: ... signed. Approvals Queued

> **NOTE:** This option must be used at least once - just prior to the end of the Pay Period.

#### Pay Period Certification

This option will display each date within the pay period, the scheduled tour for that date and any tour exceptions for each employee of each T&L the supervisor is responsible for certifying. If no serious exceptions are encountered, the supervisor may release the timecard to Payroll, or elect to bypass certification at this time.

The title (header) and data will print on the same page if the supervisor has several T&Ls to review (i.e., supervisor does not have to select a T&L); however, if the supervisor has only one T&L to review, the header prints on a blank page and the data starts on the next page.

> Select T&A Supervisor Menu Option: 2 \<RET\> Pay Period Certification

> VA TIME & ATTENDANCE SYSTEM PAY PERIOD CERTIFICATION

> Select T&L Unit: 111 \<RET\>

> PAIDEMPLOYEE7,NINE 000-00-0079

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Sun</p>
</blockquote></th>
<th><blockquote>
<p>15-Nov-92</p>
</blockquote></th>
<th><blockquote>
<p>Day Off</p>
</blockquote></th>
<th colspan="3" rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Mon</p>
</blockquote></th>
<th><blockquote>
<p>16-Nov-92</p>
</blockquote></th>
<th><blockquote>
<p>07:30P-07:30A</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>17-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>CB</p>
</blockquote></td>
<td><blockquote>
<p>FAM CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>18-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>AD</p>
</blockquote></td>
<td><blockquote>
<p>ADOPT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>19-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>20-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>21-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td><blockquote>
<p>22-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mon</p>
</blockquote></td>
<td><blockquote>
<p>23-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>SICK LV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>24-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>SICK LV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>25-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>26-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>HX</p>
</blockquote></td>
<td><blockquote>
<p>HOL EX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>27-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>28-Nov-92</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to Continue.

When certifying timecards, supervisors will see a time decomposition so that they will know what types of time are being paid.

> PAY PERIOD SUMMARY

> PAIDEMPLOYEE7,NINE \[SSN: 000-00-0079\] Pay Period: 95-05

> -----------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 58%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Week</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Care and Bereavement</p>
</blockquote></th>
<th><blockquote>
<p>8.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Week</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Adoption</p>
</blockquote></td>
<td><blockquote>
<p>8.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Week</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Sick Leave</p>
</blockquote></td>
<td><blockquote>
<p>16.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Release to Payroll? YES \<RET\>

#### List Leave Requests

This option allows the user to list leave requests for one or more employees. The user enters a 'begin' date and an 'end' date. All leave requests for the employee(s) chosen will be displayed. When there is more than one employee, the list may be sorted by employee name or date of leave request. The date, time, type of leave, remarks, and status are listed.

> Select T&A Supervisor Menu Option: 3 \<RET\> List Leave Requests

> Select T&L Unit: 101 \<RET\>

> Select Employee (or RETURN for all): PAIDEMPLOYEE7,NINE \<RET\> 000-00-0079

> Begin with Date: T \<RET\> (AUG 15, 1994) End with Date: T+32 \<RET\> (SEPT 16, 1994) Sort by: (E=Employee D=Date) E// \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 101 LEAVE REQUESTS

> From 15-Aug-94 to 16-Sept-94

> PAIDEMPLOYEE7,NINE 000-00-0079

> 08:00A 16-Aug-94 to 04:30P 16-Aug-94 Sick Leave Approved

> SORE THROAT.

> 12:30P 31-Aug-94 to 04:30P 31-Aug-94 Annual Leave Cancelled

> 08:00A 04-Sept-94 to 04:30P 10-Sept-94 Military Leave Approved

> Press RETURN to Continue.

#### Employee Leave Balances

This option allows a user to view all leave balances for an employee that he/she supervises. The values are current as of the date shown on the screen. Leave fields that have no value (i.e., null) are not listed.

Compensatory Time (Comp Time): Time off in an amount equal to the overtime worked in lieu of overtime pay.

Restored Leave: Annual Leave that has been credited to a restored leave account (employee was prevented from using the leave due to illness or the exigencies of the service). This leave must be used during the next two leave years.

The number "4" in front of "Restored Leave" below means that the leave must be used by the end of calendar year 1994.

> Select T&A Supervisor Menu Option: 4 \<RET\> Employee Leave Balances

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDTIMEKEEPR,ONE \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> EMPLOYEE LEAVE BALANCES

> PAIDTIMEKEEPR,ONE 000-00-0001

> Balances are as of Sat 10-Dec-94

> Leave Group: 3

> Annual Leave Balance: 293.000

> Sick Leave Balance: 403.250

> Comp Time: 10.000 must be used by 24-Dec-94

> 4 Restored Leave: 40.000

> Press RETURN to Continue. \<RET\>

#### Display OT/CT Requests

This option allows the user to view the status of all overtime and compensatory time requests for the employees that are under his/her supervision. The status "Requested" means that the request has been entered into the system by the timekeeper; "Supr. App." means that the employee's supervisor has logged onto the system and approved the request. The status of "Cancelled" indicates that the timekeeper, employee's supervisor, or the Director/Director's Designee has cancelled the request. The status of "Disapproved" indicates that the employee's supervisor or the Director/Director's Designee has disapproved the request. The status of "Approved" indicates that the Director/Director's Designee has approved the request. An estimated cost of overtime is displayed with each request.

> Select T&A Supervisor Menu Option: 5 \<RET\> Display OT/CT Requests

> Select T&L Unit: 102 \<RET\>

> Select EMPLOYEE (or RETURN for all): \<RET\> Begin with Date: T \<RET\> (JUL 01, 1995) End with Date: T+23 \<RET\> (JUL 24, 1995)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 102 OT/CT REQUESTS

> From 01-Jul-95 to 24-Jul-95

> PAIDEMPLOYEE8,TEN 000-00-0080

> 01-Jul-95 5 Hrs. OVERTIME (\$372.66) on T&L 006 Requested

> To process backlog of phar. co-pay checks.

> 08-Jul-95 8.2 Hrs. OVERTIME (\$523.01) on T&L 006 Approved

> BACKLOAD

> PAIDEMPLOYEE8,ONE 000-00-0081

> 12-Jul-95 5 Hrs. OVERTIME (\$362.17) on T&L 006 Approved

> To process backlog of phar. co-pay checks.

> PAIDEMPLOYEE7,SEVEN 000-00-0077

> 15-Jul-95 2 Hrs. OVERTIME (\$102.31) on T&L 102 Requested

> PROJECT MUST BE COMPLETED BY MONDAY NEXT WEEK.

> Press RETURN to Continue. \<RET\>

#### List Daily Exceptions

This option allows the supervisor to list variations to an employee's authorized schedule, for a date selected. The name of the employee and a short message describing the variations are displayed. These variations or exceptions must be cleared, corrected or approved as the changes to the authorized schedule must be done before the employee's pay record can be released to the Austin Automation Center for payment. Attendance records with serious exceptions will not release to Payroll.

> Select T&A Supervisor Menu Option: 6 \<RET\> List Daily Exceptions

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1//T-5 \<RET\> (JUL 25, 1994)

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 111 EXCEPTIONS

> Mon 25-Jul-94

> PAIDEMPLOYEEBJ,ELEVEN

> 08:00A AL not Requested

> PAIDEMPLOYEEBL,THIRTEEN

> 11:00A OT not Requested

> PAIDEMPLOYEEBN,FIFTEEN

No Time Posted

> PAIDEMPLOYEECB,THREE

> 10:00P CU not Requested

> PAIDEMPLOYEECJ,ELEVEN

> 08:00A ML not Requested

> PAIDEMPLOYEECK,TWELVE

> 01:00P AL Requested but not Approved

> Press RETURN to Continue.

#### Display Pay Period Exceptions

This option is the same as "List Daily Exceptions", but displays a selected pay period. The name of the employee, day, date of the exception, and a short message are displayed. Beginning time is shown if employee tours are based upon hours rather than days.

Similar to this option is "List Prior Pay Period Exceptions" which lists all exceptions for all records released to Payroll for all previous pay periods, while this option lists all exceptions for a specific pay period.

> Select T&A Supervisor Menu Option: 7 \<RET\> Display Pay Period Exceptions

> Select T&L Unit: 101 \<RET\>

> Posting Date: T-1// \<RET\> (MAR 05, 1993)

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 101 EXCEPTIONS

> Sun 21-Feb-93 to Fri 5-Mar-93

> PAIDEMPLOYEE8,THREE

> Sun 21-Feb-93 09:00A OT Requested but pending Supervisor Approval

> Sun 21-Feb-93 11:00A OT Posted exceeds Requested Hours

> PAIDEMPLOYEE8,FOUR

> Mon 22-Feb-93 12:30P AL not Requested

> Tue 23-Feb-93 03:00P AL not Requested

> Wed 24-Feb-93 09:30A AL not Requested

> Thu 25-Feb-93 04:00P AA not Requested

> PAIDEMPLOYEE8,FIVE

> Tue 2-Mar-93 05:00P CT not Requested

> Wed 3-Mar-93 06:00A CT not Requested

> Thu 4-Mar-93 07:30A CT not Requested

#### Display Employee Tour of Duty

With this option, the supervisor is able to display the authorized tour of duty for a selected employee. The supervisor will be prompted to display the long or short version of the tour. Most tours have one segment and the short version is sufficient to display the entire tour. However, if a tour has built-in OT, stand-by, etc., then a long display is preferable since all segments of the tour will be displayed.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

Select T&A OT/Supervisor Menu Option: 8 Display Employee Tour of Duty

Select T&L Unit: 110 NHCU

C = Current Pay Period beginning 6-May-12

L = Last Pay Period beginning 22-Apr-12

N = Next Pay Period beginning 20-May-12

Which Pay Period? C //

Select Type of Display (S or L): SHORT//

Select EMPLOYEE: EMPL, PAIDEMPLOYEE1,ONE 111-11-1114

Select Device: HOME// HOME (CRT) Right Margin: 80//

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TOUR OF DUTY

PAIDEMPLOYEE1,ONE 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-10 Telework Indicator: E FLSA: N

TW Week 1 - 6-May-12 TW Week 2 - 13-May-12

Sun DAY OFF DAY OFF

Mon 07:00A-03:30P 07:00A-03:30P

Tue 07:00A-03:30P 07:00A-03:30P

Wed 07:00A-03:30P 07:00A-03:30P

Thu REG 07:00A-03:30P REG 07:00A-03:30P

Fri REG 07:00A-03:30P REG 07:00A-03:30P

Sat DAY OFF DAY OFF

Enter return to continue.

> SHORT or LONG Display? L \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE1,ONE \<RET\> PAIDEMPLOYEE1,ONE 1XX-XX-1114

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TOUR OF DUTY

PAIDEMPLOYEE1,ONE 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-10 Telework Indicator: E FLSA: N

TW Week 1 - 6-May-12 TW Week 2 - 13-May-12

Sun 03:30P-MID 03:30P-MID

MID-08:30A MID-08:30A

On-Call On-Call

Mon Day Off Day Off

Tue 03:30P-MID 03:30P-MID

MID-08:30A MID-08:30A

On-Call On-Call

Wed 03:30P-MID 03:30P-MID

MID-08:30A MID-08:30A

On-Call On-Call

Thu REG 03:30P-MID REG 03:30P-MID

MID-08:30A MID-08:30A

On-Call On-Call

Fri REG 03:30P-MID REG 03:30P-MID

MID-08:30A MID-08:30A

On-Call On-Call

Sat Day Off Day Off

Press RETURN to Continue.  
Display Employee Pay Period

This option allows the user to select an employee and a posting date. The employee's scheduled tour of duty and any tour of duty exceptions for the pay period for which the posting date belongs are displayed.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

> Select T&A Supervisor Menu Option: 9 \<RET\> Display Employee Pay Period

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE PAY PERIOD DATA

Select EMPLOYEE: PAIDEMPLOYEE1,ONE PAIDEMPLOYEE1,ONE 111-11-1114

Posting Date: 5/6 (MAY 06, 2012)

Select Device: HOME// HOME (CRT) Right Margin: 80//

PAIDEMPLOYEE1,ONE T&L 110 Telework Ind: E 1XX-XX-1114

Date TW Scheduled Tour Tour Exceptions

------------------------------------------------------------------------

Sun 6-May-12 Day Off

Mon 7-May-12 07:00A-03:30P

Tue 8-May-12 07:00A-03:30P

Wed 9-May-12 07:00A-03:30P

Thu 10-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 11-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 12-May-12 Day Off

Sun 13-May-12 Day Off

Mon 14-May-12 07:00A-03:30P

Tue 15-May-12 07:00A-03:30P

Wed 16-May-12 07:00A-03:30P

Thu 17-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 18-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 19-May-12 Day Off  
List Tours by T&L

This option allows the supervisor to view all tours of duty that have been authorized for use by the selected T&L Unit, listed with each T&L with the 'special indicator' showing scheduled overtime, scheduled compensatory time, more than one shift, standby, etc.

> Select T&A Supervisor Menu Option: 10 \<RET\> List Tours by T&L Select T&L Unit (or All): 150 \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> 2-Aug-94 T & L T O U R L I S T Page 1

> 150

> \# Tour Hrs. Segment Special Indicator

> 339 00:15A-08:00A On Call 0.00 00:15A-08:00A On-Call

> 26 01:00P-04:00P 3.00 01:00P-04:00P

> 111 01:00P-05:00P 4.00 01:00P-05:00P

> 236 01:00P-09:30P 8.00 01:00P-09:30P

> 324 01:15P-05:15P 4.00 01:15P-05:15P

> 329 01:15P-05:15P 4.00 01:15P-05:15P

> 331 01:15P-05:15P 4.00 01:15P-05:15P Press RETURN to Continue. ^ \<RET\>

#### List Environment Diff. Requests

This option allows the user to list environmental differential or hazardous duty requests within a specified time span for one or all employees of a T&L Unit. The requests may be sorted by employee or date of request.

> Select T&A Supervisor Menu Option: 11 \<RET\> List Environment Diff. Requests

> Select T&L Unit: 101 \<RET\>

> Select EMPLOYEE (or RETURN for all): \<RET\> Begin with Date: T \<RET\> (NOV 30, 1992) End with Date: T+30 \<RET\> (DEC 30, 1992) Sort by: (E=Employee D=Date) E// \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 101 ENVIRONMENTAL DIFFERENTIAL REQUESTS

> From 30-Nov-92 to 30-Dec-92

> PAIDEMPLOYEE8,SIX 000-00-0086

> 30-Nov-92 06:00A-04:30P ASBESTOS Envir. Diff. Approved

> REMOVAL IN BASEMENT OF BLD. 50

> 1-Dec-92 10:00A-04:30P RADIATION Envir. Diff. Approved

> DOING TESTS.

> 15-Dec-92 06:00A-04:30P TREE REMOVAL Envir. Diff. Approved

> BRANCHES COVERED SIDEWALK & STOP SIGN.

> Press RETURN to Continue.

#### List Un-Certified Employees

This allows the user to list the status of the time and attendance reports for the current pay period by selecting a specific T&L. It shows the employees that have not been released to Payroll. Similar to this option is "Un-Transmitted Employees - All T&Ls" which lists the time and attendance reports of employees of all T&Ls.

> Select T&A Supervisor Menu Option: 12 \<RET\> List Un-Certified Employees

> VA TIME & ATTENDANCE SYSTEM Page 1

> UN-CERTIFIED EMPLOYEES

> Select T&L Unit: 902 \<RET\>

> 902 INFORMATION SERVICES CENTER Sun 4-Apr-93 to Sat 17-Apr-93

> 000-00-0043 PAIDEMPLOYEE4,THREE

> 000-00-0044 PAIDEMPLOYEE4,FOUR

> 000-00-0045 PAIDEMPLOYEE4,FIVE

> 000-00-0046 PAIDEMPLOYEE4,SIX

> 000-00-0047 PAIDEMPLOYEE4,SEVEN

> 000-00-0048 PAIDEMPLOYEE4,EIGHT

> 000-00-0049 PAIDEMPLOYEE4,NINE

> 000-00-0050 PAIDEMPLOYEE5,TEN

> 000-00-0051 PAIDEMPLOYEE5,ONE

> 000-00-0052 PAIDEMPLOYEE5,TWO

#### List Prior Pay Period Exceptions

With this option the user is able to display all time and attendance report exceptions for all records released to Payroll and/or transmitted for all previous pay periods.

> Select T&A Supervisor Menu Option: 13 \<RET\> List Prior Pay Period

> Exceptions

> Select T&L Unit: 102 \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> PRIOR PAY PERIOD EXCEPTIONS

> 17-Jul-95

> PAIDEMPLOYEE5,THREE (102)

> 12-Feb-93 08:00P OT Posted exceeds Requested Hours

> PAIDEMPLOYEE,FOUR (102)

> 26-Jul-94 07:00A AL not Requested

#### Employee Reports

This option allows the supervisor to access employee reports options and display employee data.

> Select T&A Supervisor Menu Option: 14 \<RET\> Employee Reports

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Expenditures</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Employee Overtime/CompTime Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Employee Prior Pay Period Adjustments</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Reports ...</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Expenditures

This option allows the user to view all governmental costs over one or all pay periods for a chosen year. Totals are displayed for each pay period. Supervisor can only see employees that are under their assigned T&Ls.

> Select Employee Reports Option: 1 \<RET\> Expenditures

> Select T&L Unit(s): 001 \<RET\>

> Enter YEAR: 95 \<RET\> (1995)

> Enter Pay Period (Return for all): 3 \<RET\>

> THIS REPORT SHOULD BE QUEUED ! DEVICE: HOME// \<RET\>

> EMPLOYEE COST FOR PAY PERIOD 3 YEAR 95

> BASE NIGHT HOLIDA O/TIME SUNDAY ON-CA REEMP SAT GROSS G/SHARE GROSS NAME PAY DIFF PAY PAY PAY PAY AWARDS ANNUIT PAY PAY BENEFITS COST

> --------------------------------------------------------------------------------------------------------------

> PDEMP,A 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,B 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,C 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,D 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,E 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,F 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,G 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,H 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,I 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,J 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,K 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,L 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> PDEMP,M 1212.40 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1212.40 200.00 1412.40

> PDEMP,N 1360.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1360.00 300.00 1660.00

> PDEMP,O 2060.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2060.80 412.32 2473.12

> PDEMP,P 2248.80 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 2248.80 173.65 2422.45

> T&L 001

--------

---- ---- ---- ---- ---- ---- ---- ---- -------- ------- --------

> Total: 27528.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 27528.00 4343.88 31871.88

> --------------------------------------------------------------------------------------------------------------- DHCP PAID REPORT E001 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 001

#### Employee Overtime/CompTime Report (OT/CT)

This option allows the user to display OT/CT that an employee has taken over one or all pay periods during a selected calendar year. Supervisors are only able to see employees under T&Ls that are assigned to them.

> Select Employee Reports Option: 2 \<RET\> Employee Overtime/CompTime Report

> Select T&L: 902 \<RET\>

> Enter YEAR: 95 \<RET\> (1995)

> Enter employee name (Return for ALL): \<RET\> Enter Pay Period (Return for all in this yr.): \<RET\> THIS IS A 132 COLUMN REPORT !

> DEVICE: HOME// \<RET\> HOME

> EMPLOYEE OT/CT REPORT DATE: 04/27/95

> Year: 95 T&L: 902

> ![](paid-version-4-user-manual/014.png)![](paid-version-4-user-manual/015.png)![](paid-version-4-user-manual/016.png)![](paid-version-4-user-manual/017.png)![](paid-version-4-user-manual/018.png)![](paid-version-4-user-manual/019.png)![](paid-version-4-user-manual/020.png)![](paid-version-4-user-manual/021.png)![](paid-version-4-user-manual/022.png)![](paid-version-4-user-manual/023.png)![](paid-version-4-user-manual/024.png)![](paid-version-4-user-manual/025.png)![](paid-version-4-user-manual/026.png)P/P DATE NAME SSN GROSS PAY C/T USED C/T BAL O/T HRS O/T PAY

> 01 01/08/95 PDEMP8,SEVEN 000-00-0087 1248.72 0.00 0.00 4.00 87.12

> PDEMP8,EIGHT 000-00-0088 2491.08 0.00 0.00 12.00 287.88

> PDEMP8,NINE 000-00-0089 1948.76 0.00 0.00 4.00 95.96

> PDEMP9,TEN 000-00-0090 1403.50 0.00 0.00 9.00 202.70

> PDEMP9,ONE 000-00-0091 2203.20 2.00 0.00 0.00 0.00

> ------- ---- ---- ---- ------

> P/P-/Totals: 9295.26 2.00 0.00 29.00 673.66

> 02 01/22/95 PDEMP9,TWO 000-00-0092 1804.75 0.00 0.00 5.00 119.95

> PDEMP9,THREE 000-00-0093 1172.49 0.00 0.00 0.50 10.89

> PDEMP9,FOUR 000-00-0094 1896.74 0.00 0.00 6.50 155.94

> PDEMP9,FIVE 000-00-0095 2238.48 0.00 0.00 32.75 785.68

> PDEMP9,SIX 000-00-0096 1980.70 0.00 0.00 10.00 239.90

> ------- ---- ---- ----- -------

> P/P-Totals: 9093.16 0.00 0.00 54.75 1312.36

> DHCP PAID REPORT 0O01 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

> March 2018 PAID V. 4.0 User Manual 5.21

> Time & Attendance

#### Employee Prior Pay Period Adjustments

This option allows the user to view all audits of employees that are under their assigned T&Ls, over a selected date range.

> Select Employee Reports Option: 3 \<RET\> Employee Prior Pay Period Adjustments

> Select T&L: 902 \<RET\>

> Enter Beginning Date T//1/1/95 \<RET\> (JAN 01, 1995)

> Enter Ending Date T//4/28/95 \<RET\> (APR 28, 1995)

> THIS REPORT CAN BE QUEUED ! DEVICE: HOME// HYPER SPACE

> ...........................

> PRIOR PAY PERIOD ADJUSTMENT REPORT DATE: 04/28/95 from JAN 01, 1995 to APR 28, 1995

> for T&L 902

> \|---------------------\|------------\|-\|--\|------------\|------------\|------------\|

> \| \| TIMEKEEPER \| \| \| SUPERVISOR \| APPROVER \| PROCESSOR \|

> \| \|------------\| \| \|------------\|------------\|------------\|

> \|EMPLOYEE \|NAM\| DATE \|\*\|\*\*\|NAM\| DATE \|NAM\| DATE \|NAM\| DATE \|

> \|---------------------\|---\|--------\|-\|--\|---\|--------\|---\|--------\|---\|--------\|

> \|PAIDEMPLOYEE6,TEN \|PDT\|02-10-95\|T\|P \|PDS\|02/13/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,ONE \|PDT\|02-10-95\|T\|P \|PDS\|02/13/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,TWO \|PDT\|02-10-95\|T\|P \|PDS\|02/10/95\|PDA\|02/13/95\|PDP\|03/02/95\|

> \|PAIDEMPLOYEE6,THREE \|PDT\|02-21-95\|T\|P \|PDS\|02/21/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,FOUR \|PDT\|02-21-95\|T\|P \|PDS\|02/22/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,FIVE \|PDT\|02-21-95\|T\|P \|PDS\|02/22/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,SIX \|PDT\|02-21-95\|T\|P \|PDS\|02/21/95\|PDA\|02/22/95\|PDP\|03/07/95\|

> \|PAIDEMPLOYEE6,SEVEN \|PDT\|03-07-95\|T\|P \|PDS\|03/14/95\|PDA\|03/16/95\|PDP\|03/24/95\|

> \|PAIDEMPLOYEE6,EIGHT \|PDT\|03-14-95\|T\|P \|PDS\|03/20/95\|PDA\|03/20/95\|PDP\|03/21/95\|

> \|PAIDEMPLOYEE6,NINE \|PDT\|04-11-95\|T\|A \|PDS\|04/11/95\|PDA\|04/12/95\| \| \|

> \| \| \| \| \| \| \| \| \| \| \| \|

> \| \*TYPE: T=TIME V=VCS H=HAZARD/ENVIR DIFF \|

> \| \*\*STATUS: R=REQUESTED A=APPROVED P=PAYROLL PROCESSED D=DISAPPROVED \|

> \| X=CANCELLED S=SUPR. APPROVED \|

> \|---------------------\|------------\|-\|--\|------------\|------------\|------------\|

> DHCP PAID REPORT AU01 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

#### Employee Leave Reports

This option allows the supervisor to view all leave reports of one or all employees within the T&Ls that he/she is assigned to.

> Select Employee Reports Option: 1 \<RET\> Employee Leave Reports

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Employee Leave Used</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Requested</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Pattern</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Employee Leave Used

This option allows the supervisor to print, over a selected date range, all previous leave taken by one or all employees within the T&Ls that he/she is assigned to.

> Select Employee Leave Reports Option: 1 \<RET\> Employee Leave Used

> Select T&L Unit(s): 043 \<RET\>

> Report Beginning Date T//1/1/93 \<RET\> (JAN 01, 1993) Report Ending Date T// \<RET\> (AUG 21, 1995)

> THIS IS A 132 COLUMN REPORT. DEVICE: HOME// \<RET\>

> LEAVE USED SUMMARY DATE: 08/21/95 from JAN 01, 1993 to AUG 21, 1995

> --------------------------------------------------------------------------------------------- PP DATE EMPLOYEE SSN TYPE FROM TO LENGTH

> ---------------------------------------------------------------------------------------------

> 02 01/25/93 PDEMP9,SEVEN 000-00-0097 Sick Leave 04:30P 05:15P .75 H

> Annual Leave MID 01:00A 1.00 H

> 02/01/9 Sick Leave 11:00P 01:00A 2.00 H

> 26 12/31/93 PDEMP9,EIGHT 000-00-0098 Without Pay 07:00A 03:30P 8.00 H

> 15 07/25/94 PDEMP9,NINE 000-00-0099 Annual Leave 08:00A 04:30P 8.00 H

> 23 11/14/94 PDEMP9,SEVEN 000-00-0097 Annual Leave 08:00A 04:30P 8.00 H

> ---------------------------------------------------------------------------------------------

> DHCP PAID REPORT L004 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 043

#### Employee Leave Requested

This option enables to user to display all future leave that has been requested by one or all employees that are assigned to his/her T&L over a selected date range.

> Select Employee Leave Reports Option: 2 \<RET\> Employee Leave Requested

> Select T&L: 100 \<RET\>

> Enter employee name (Return for all): \<RET\>

> Report Beginning Date T//5/1/95 \<RET\> (MAY 01, 1995)

> Report Ending Date T//12/31/95 \<RET\> (DEC 31, 1995)

> THIS IS A 132-COLUMN REPORT!

> DEVICE: HOME// \<RET\> QUEUE TO PRINT ON

> E M P L O Y E E L E A V E R E Q U E S T L I S T DATE: 05/01/95 from MAY 01, 1995 to DEC 31, 1995

> FOR T&L: 100

> \|----------------\|----------------\|--------------\|--------\|------------------\|---------\|--------\|-------------------­

> \|

> \|FROM \|TO \|EMPLOYEE \|LENGTH \|TYPE LEAVE \|DATE-REQ \|DATE-APP\|APPROVING SUPERVISOR

> \|

> \|----------------\|----------------\|--------------\|--------\|------------------\|---------\|--------\|-------------------­

> \|

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>| | |</p>
</blockquote></th>
<th><blockquote>
<p>| |</p>
</blockquote></th>
<th><blockquote>
<p>| |</p>
</blockquote></th>
<th><blockquote>
<p>| |</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|05/01/95 01:00P |05/01/95 04:30P |PDEMP10,TEN</p>
</blockquote></td>
<td><blockquote>
<p>| 3.5 hrs|Sick Leave</p>
</blockquote></td>
<td><blockquote>
<p>|05/01/95 |</p>
</blockquote></td>
<td><blockquote>
<p>|PAIDSUPERVISR1,NINE|</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|05/01/95 01:00P |05/01/95 03:30P |PDEMP10,ONE</p>
</blockquote></td>
<td><blockquote>
<p>| 2.5 hrs|Sick Leave</p>
</blockquote></td>
<td><blockquote>
<p>|05/01/95 |</p>
</blockquote></td>
<td><blockquote>
<p>|PAIDSUPERVISR2,TEN |</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \|05/01/95 07:00A \|05/01/95 03:30P \|PDEMP10,TWO \| 8 hrs\|Sick Leave \|04/28/95 \|05/01/95\|PAIDSUPERVISR1,NINE\|

> \|

> \|05/01/95 08:00A \|05/04/95 04:30P \|PDEMP10,THREE \| 32 hrs\|Annual Leave \|12/12/94 \|12/15/94\|PAIDSUPERVISR2,ONE \|

> \|

> \|05/01/95 07:00A \|05/01/95 03:30P \|PDEMP10,FOUR \| 8 hrs\|Compensatory Time \|04/03/95 \|04/06/95\|PAIDSUPERVISR2,TWO \|

> \| \| \| \| \| \| \| \|

> \|05/02/95 07:15A \|05/02/95 03:45P \|PDEMP10,FIVE \| 8 hrs\|Annual Leave \|05/01/95 \| \|PAIDSUPERVISR2,THRE\|

> \| \| \| \| \| \| \| \|

> \|05/04/95 07:00A \|05/04/95 03:30P \|PDEMP10,SIX \| 8 hrs\|Annual Leave \|04/26/95 \|04/26/95\|PAIDSUPERVISR2,ONE \|

> \|

> \|05/04/95 08:00A \|05/08/95 04:30P \|PDEMP10,SEVEN \| 24 hrs\|Annual Leave \|04/28/95 \|04/28/95\|PAIDSUPERVISR2,THRE\|

> \|

> \|05/04/95 08:00A \|05/17/95 04:30P \|PDEMP10,EIGHT \| 80 hrs\|Annual Leave \|06/29/94 \|07/18/94\|PAIDSUPERVISR2,FOUR\|

> \|

> \|----------------\|----------------\|--------------\|---------------------------\|---------\|--------\|-------------------\|

> DHCP PAID REPORT L002 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 100

#### Employee Leave Pattern

This option allows the user to view all leave taken around scheduled off days by an employee. Supervisors can only see T&Ls that are assigned to them.

> Select Employee Leave Reports Option: 3 \<RET\> Employee Leave Pattern

> Select T&L: 902 \<RET\>

> Enter employee name: PAIDEMPLOYEE10,NINE \<RET\>

> Enter Beginning Date T// 1/1/94 \<RET\> (JAN 01, 1994) Enter Ending Date T// \<RET\> (APR 26, 1995)

> THIS IS AN 80 COLUMN REPORT.

> DEVICE: HOME// \<RET\> QUEUE TO PRINT ON

> EMPLOYEE LEAVE PATTERN DATE: 04/26/95 from: JAN 01, 1994 to APR 26, 1995

> for: PAIDEMPLOYEE10,NINE - ISC

> \|------\|----\|---------\|----\|-------\|-------\|--------\|--------------------------\|

> \|P/P \|DAY \|DATE \|TYPE\|FROM \|TO \|LENGTH \|COMMENT \|

> \|------\|----\|---------\|----\|-------\|-------\|--------\|--------------------------\|

> \|------\|----\|---------\|----\|-------\|-------\|--------\|--------------------------\| DHCP PAID REPORT L005 VA TIME & ATTENDANCE SYSTEM STATION: 111 / T&L: 902

#### Review FY Recess for 9 Month AWS Employee

This view only option displays the Recess Schedule for nurses on the 9 month/3 month alternate work schedule (AWS). To view a 9 month/3 month AWS Recess Schedule, enter the T&L unit of the nurse. At the next prompt, enter the fiscal year or the nurse’s name.

Once the schedule is selected, you may enter actions at the “Select Action” prompt to navigate through the Recess Schedule, print the Recess Schedule and display a summary. Enter a double question mark (??) at this prompt for a list of all available actions.

Following is a list of actions with a brief description. The mnemonic for each action is shown in brackets \[ \] following the action name. Entering the mnemonic is the quickest way to select an action.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recess Hours Summary</p>
<p>[RS]</p>
</blockquote></td>
<td><blockquote>
<p>Enter RS to see a summary screen with recess totals. Be sure to scroll down to see the whole</p>
<p>report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Next Screen [+]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Previous Screen [-]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the previous screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Up a Line [UP]</p>
</blockquote></td>
<td><blockquote>
<p>Move up one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Down a Line [DN]</p>
</blockquote></td>
<td><blockquote>
<p>Move down one line.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Right [&gt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the right if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shift View to Left [&lt;]</p>
</blockquote></td>
<td><blockquote>
<p>Move the screen to the left if the screen width is more than 80 characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>First Screen [FS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the first screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Last Screen [LS]</p>
</blockquote></td>
<td><blockquote>
<p>Move to the last screen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Go to Page [GO]</p>
</blockquote></td>
<td><blockquote>
<p>Move to any selected page in the list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Re Display Screen [RD]</p>
</blockquote></td>
<td><blockquote>
<p>Redisplay the current screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> T&A Supervisor Menu

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Print Screen [PS]</p>
</blockquote></td>
<td><blockquote>
<p>Print the header and the portion of the list currently displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print List [PL]</p>
</blockquote></td>
<td><blockquote>
<p>Print the list of entries currently displayed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Search List [SL]</p>
</blockquote></td>
<td><blockquote>
<p>Find selected text in list of entries.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Auto Display(On/Off) [ADPL]</p>
</blockquote></td>
<td><blockquote>
<p>Toggle the menu of actions to be displayed/not displayed automatically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Quit [QU]</p>
</blockquote></td>
<td><blockquote>
<p>Exit the screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Employee Reports Option: Review FY Recess for 9 Month AWS Employee

> Select T&L Unit: 221

> Select 9-month AWS Nurse: 2007

> 1 2007 PAIDemployee,One 2007 000-01-4309

> 2 2007 PAIDemployee,Two 2007 000-01-3045

> 3 2007 PAIDemployee,Three 2007 000-01-2715

> 4 2007 PAIDemployee,Four 2007 000-01-4274

> 5 2007 PAIDemployee,Five 2007 000-01-4275

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 PAIDemployee,One 2007 000-01-4309

> Recess Schedule Viewer Jul 17, 2007@14:43:45 Page: 1 of 4

> FY2007 Recess Week Viewer for 9 month AWS with start date 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> +Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Nov 2006============

> 6 5 6 7 8 9 10 11 8.00

> 7 06-23 12 13 14 15 16 17 18 10.50

> 8 19 20 21 22 23 24 25 40.25

> 9 06-24 26 27 28 29 30 1 2 24.75

> =============Dec 2006============

> 10 3 4 5 6 7 8 9 40.00

> 11 06-25 10 11 12 13 14 15 16 56.00

> 12 17 18 19 20 21 22 23 36.50

> 13 06-26 24 25 26 27 28 29 30 36.00

> 14 31 1 2 3 4 5 6 36.00

> =============Jan 2007============

> 15 07-01 7 8 9 10 11 12 13 36.00

> 16 14 15 16 17 18 19 20 36.00

> 17 07-02 21 22 23 24 25 26 27 36.00

> 18 28 29 30 31 1 2 3 36.00

> =============Feb 2007============

> +---------Enter ?? for more actions-------------------------------------------- RS Recess Hours Summary

> Select Action:Next Screen// rs Recess Hours Summary

> RECESS SCHEDULE SUMMARY Jul 17, 2007@14:44:16 Page: 1 of 2

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> --Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------

> 6 11/05/06 8.00 0.00

> 7 11/12/06 10.50 0.00

> 8 11/19/06 40.25 0.00

> 9 11/26/06 24.75 0.00

> 10 12/03/06 40.00 0.00

> 11 12/10/06 56.00 0.00

> 12 12/17/06 36.50 0.00

> 13 12/24/06 36.00 0.00

> 14 12/31/06 36.00 0.00

> 15 01/07/07 36.00 0.00

> 16 01/14/07 36.00 0.00

> 17 01/21/07 36.00 0.00

> 18 01/28/07 36.00 0.00

> 19 02/04/07 36.00 0.00

> 20 02/11/07 3.50 0.00

> ====== ======

> +---------WARNING--Recess hours are under scheduled: 68.50--------------------

> Select Action:Next Screen// \<RET\> NEXT SCREEN

> RECESS SCHEDULE SUMMARY Jul 17, 2007@14:45:09 Page: 2 of 2

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> +-Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------ Total Recess. Scheduled: 471.50 Posted: 0.00

> Total Weeks in AWS FY Schedule: 54.00

> Total available FY recess hrs: 540.00 (13.5 weeks) WARNING--Recess hours under scheduled: 68.50

> ----------Enter ?? for more actions-------------------------------------------- Select Action:Quit//

#### Display Employee Tour Hours

This option allows T&A Supervisors to view an employee's tour of duty number, tour of duty hours, tour hours on each day and 8B normal hours for a selected pay period within the T&L units assigned to them. The Tour Hours column contains a total of any tour hours that fall on that day; therefore, two day tours will contribute hours to both days on which they fall.

Supervisors can also choose to print the footnotes explaining the report headings.

> Select Employee Reports Option: Display Employee Tour Hours

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE,ONE \<RET\> 000-01-4202

> 0XX-XX-4202

> Select PAY PERIOD: 08-08 \<RET\>

> Include report footnotes? N// y \<RET\> YES

> DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> VA TIME & ATTENDANCE REPORT for T&A Supervisor--NOV 07, 2008@09:19 p1

> Display Employee Tour Hours: PP 08-08 (13-Apr-08 thru 26-Apr-08)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EMPLOYEE NAME</p>
</blockquote></th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>8B NRM HRS</p>
</blockquote></th>
<th><blockquote>
<p>ToD HRS*</p>
</blockquote></th>
<th><blockquote>
<p>IEN 450</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>======================</p>
</blockquote></td>
<td><blockquote>
<p>===========</p>
</blockquote></td>
<td><blockquote>
<p>==========</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PAIDEMPLOYEE,ONE 0XX-XX-4202 40 40 14202

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Day</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 1</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 2</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>---</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mon</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter RETURN to continue or '^' to exit: \<RET\>

> 5.32 PAID V. 4.0 User Manual March 2018

> Time & Attendance

> =================================================================

> FOOTNOTES TO REPORT HEADINGS

> ============================

> \*ToD HRS (Tour of Duty Hours) The total Tour of Duty hours that fall within the

> -------- two week pay period, beginning midnight Saturday. Hours that cross midnight from a tour that starts on the last day of a pay period will appear on the following pay period.

> .....................................................................

> \*Hours (DAILY TOUR HOURS) This column contains actual tour hours that fall

> ------ on that day from the 24 hour period beginning at midnight. A two day tour will contribute hours to each day the tour falls on. Hours

> that cross midnight from a tour that starts on the last day of a pay

> period will appear on the following pay period.

> .....................................................................

> \*ToD \# (Tour of Duty Number) The tour's entry number in the Tour

> ------ of Duty file (#457.1)

> .....................................................................

> Enter return to continue.

## Chapter 6. T&A OT/Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Time and Leave Unit (T&L) OT/Supervisor's menu and should be assigned to supervisors who approve overtime and compensatory time.

> **NOTE:** The “T&A OT/Supervisor” and “T&A Supervisor” options – except for *Approve OT/CT* – are the same.

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Supervisory Approvals</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Pay Period Certification</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>List Leave Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Leave Balances</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Display OT/CT Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>List Daily Exceptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Display Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Display Employee Tour of Duty</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Display Employee Pay Period</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>List Tours by T&amp;L</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>List Environment Diff. Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Approve OT/CT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>List Un-Certified Employees</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>List Prior Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Employee Reports ...</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Approve OT/CT

This option allows the Director or his/her designee to approve, disapprove, or cancel the use of overtime or compensatory time (comp time) and prior pay period corrections that have previously been approved by the supervisor. A message will appear indicating the need for approval. Individual items can be disapproved while approving remaining items. An estimated cost of overtime is displayed. The Director must have an electronic signature on file in order to approve, disapprove, or cancel the requests. See the Electronic Signature section of this manual for an example on how to create an electronic signature.

> Select T&A OT/Supervisor Menu Option: 12 \<RET\> Approve OT/CT VA TIME & ATTENDANCE SYSTEM

> OVERTIME/COMPTIME APPROVAL

> 100 INFORMATION SYSTEMS CENTER, DEVELOPMENT SECTION

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 47%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>8-Feb-93 PAIDEMPLOYEE11,TEN</p>
</blockquote></th>
<th><blockquote>
<p>3 Hrs. OVERTIME on T&amp;L 101</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>HINES TEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>9-Feb-93 PAIDEMPLOYEE11,TEN</p>
</blockquote></td>
<td><blockquote>
<p>1 Hrs. OVERTIME on T&amp;L 101</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>HINES TEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>3 10-Feb-93 PAIDEMPLOYEE11,TEN</p>
</blockquote></td>
<td><blockquote>
<p>1 Hrs. OVERTIME on T&amp;L 101</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>HINES TEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>4 11-Feb-93 PAIDEMPLOYEE11,TEN</p>
</blockquote></td>
<td><blockquote>
<p>1 Hrs. OVERTIME on T&amp;L 101</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>HINES TEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>5 13-Feb-93 PAIDEMPLOYEE11,TEN</p>
</blockquote></td>
<td><blockquote>
<p>5 Hrs. OVERTIME on T&amp;L 101</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>HINES TEST</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Estimated Cost of Overtime: $61.20</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Disposition (A=Approve, D=Disapprove, X=Dis. Line Item, RETURN to bypass): X

> \<RET\>

> Disapprove which Items: 4 \<RET\>

> Enter Signature Code: ... signed.

> No Prior Pay Period actions to certify.

## Chapter 7. Timekeeper Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options on this menu allow the timekeeper to post and review time and attendance data for the employees in the Time and Leave Units (T&Ls) that they are authorized to service.

The options with "..." attached to the end of the title string indicate that those options are submenu items (options that have menus attached). This will become clearer when option 4, "Employee Data..." is described.

The List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Post Employee Time</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>List Daily Exceptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Display Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Data ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>List Leave Requests</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Display OT/CT Requests</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Enter OT/CT Request</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Cancel OT Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Daily T&amp;L List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>List Tours by T&amp;L</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>List Prior Pay Period Exceptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Prior Pay Period Adjustments ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>Envir. Diff./VCS Sales ...</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>List Un-Certified Employees</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Edit OT/CT Request</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Post Employee Time

Timekeepers will use this option to record daily attendance information. Although it is the one option that will be used most, it cannot be exercised unless the employee has a Tour of Duty established. Establishing a Tour of Duty will be discussed in greater detail when we describe the Enter/Edit Employee Tour of Duty option on the Employee Data Menu.

When this option is selected, the system asks for a posting date and gives a default value of "T-1" which means today minus one, or yesterday. If posting for a date other than yesterday, enter a date, i.e., 4/9, 04-09, etc. The next prompt will ask if you would like to edit the T&A records in alphabetical order. Enter "yes" and the system will display (alphabetically) only those employees with a scheduled Tour of Duty for the selected day; which have not previously been posted. A "no" response will allow you to select an individual employee for posting.

If a leave request is entered for a date that was already posted, a bulletin is sent to all timekeepers for the T&L of the employee.

If an attempt is made to alter a record after approval but before transmission, the timekeeper is alerted to call Payroll.

In this section, we will discuss how to post the following:

1.  Post Scheduled Tour of Duty
2.  Post Leave (including Family Care and Bereavement, Adoption & Donor Leave)
3.  Post OT/CT & Unscheduled Time
4.  Post Baylor Plan
5.  Post 9 Month AWS Employee
6.  Post 36/40 AWS Plan
7.  Post Holidays
8.  Post for Daylight Savings Time
9.  Post Time for Doctors (Full Time & Part Time)

These subsections can only be accessed by choosing the "Post Employee Time" option.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

#### Post Scheduled Tour of Duty

If an employee only works his/her scheduled tour of duty, the posting for that time is straightforward. Below is an example on how to post a scheduled tour of duty for an employee.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

> Select TimeKeeper Main Menu Option: 1 Post Employee Time

> Select T&L Unit: 110 NHCU

> Posting Date: T-1//5/22/2012 (MAY 22, 2012)

> Would you like to edit the T & A RECORDs in alphabetical order? Yes// N (No)

> Select EMPLOYEE: PAIDEMPLOYEE, EMP1 PAIDEMPLOYEE, EMP1 111-11-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-11 Telework Indicator: E FLSA: N

Date TW Scheduled Tour Tour Exceptions

------------------------------------------------------------------------

Tue 22-May-12 07:00A-03:30P Unposted

Did Employee Only Work Scheduled Tour? Y

Enter Any Ad Hoc Telework Hours: (0-8): 0//

Enter '^' to bypass this employee.

Posting has now been completed for an employee that is only working his/her scheduled tour of duty.

#### Post Leave

Posting leave is dependent on when and how much leave is taken. The examples provided will demonstrate how to post leave for the following situations:

A\) Leave for the entire day

B\) Leave for part of the day

C\) Leave during the middle of the day which includes meal time

D\) Combining different types of leave in one day

E\) Leave for Family Care and bereavement; Leave for Adoption

F\) Donor Leave

Most types of leave used by employees require a request for the leave and/or supervisory approval of the leave. Request and/or approval can be accomplished either by the completion of an SF71 (Application for Leave), a time remarks code entered for the leave, or by the leave request being electronically entered and approved. Therefore, when leave is posted the timekeeper will be shown a prompt "Time Remarks Code". The options for "Time Remarks Code" vary, depending on the "Type of Time Code" that the user selects. Enter two question marks (??) at the "Time Remarks Code" prompt in order to view the following options. Definitions are as follows.

> AA Auth Abs

> Granted by Supr - 5: This code is used when the employee is on Authorized

> Absence from his/her duties. No electronic request is required.

> Jury Duty - 6: This code is used when the employee has been summoned for

> Jury Duty. The court summons will be used as authorization.

> SF71 on File - 1: This code is used with Adoption (AD), Annual Leave (AL), Authorized Absence (AA), Comp Time Used (CU), Donor Leave (DL), Family Care and Bereavement (CB), Military Leave (ML), Non-Pay Annual Leave (NL), Restored Annual Leave (RL), Sick Leave (SL), and Without Pay (WP). It indicates that an approved SF71 is on file and no electronic request is required.

> AD Adopt

> Adoption: Becoming legal parents of another's child (all activities necessary for completion of the adoption). This leave will be charged to the employee's Sick Leave by the Austin Automation Center.

> AL Annual Lv

> SF71 on File - 1: See above definition.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CB</p>
</blockquote></th>
<th><blockquote>
<p>Fam Care</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Family Care and Bereavement: Family Care - To care for a family member as a result of physical or mental illness. Bereavement - Death of a family member (attending funeral, and other arrangements necessitated by the death). This leave will be charged to the employee's Sick Leave by the Austin Automation Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>COP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Continuance of Pay: This code is used when the employee has been injured on the job and is on Continuation of Pay. No "Time Remarks Code" required.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CU</p>
</blockquote></td>
<td><blockquote>
<p>Comp Used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SF71 on File - 1: See definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>Donor Lv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>This code is used when the employee wants to serve as an organ or bone- marrow donor. This leave will be charged to Authorized Absence (AA) by the Austin Automation Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>Mil Lv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Military Leave - SF71 on File - 1: See definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>Non-Pay Annual Leave</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SF71 on File - 1: See definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NP</p>
</blockquote></td>
<td><blockquote>
<p>Non Pay</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>No "Time Remarks Code" required.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>Res Ann Lv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SF71 on File - 1: See definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Sick Lv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SF71 on File - 1: See definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>LWOP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>AWOL - 3: This code can be used for all employees that are absent without leave. No electronic request is required.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> On Suspension - 4: This code can be used for all employees. No electronic request is required.

> SF71 on File - 1: See definition.

#### Leave for the Entire Day

Below is an example of an employee whose tour of duty is MID-08:00A On-Call and 08:00A-04:30P and is on leave for the entire tour. If that employee needs to be available for on-call hours (even though he/she is on leave for the entire day), the timekeeper must delete "Unavailable for On-Call" that automatically appears on the screen.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 02, 1994)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE8,TWO \<RET\> PAIDEMPLOYEE8,TWO 000-00-0082

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE8,TWO 000-00-0082

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Tue 2-Aug-94 MID-08:00A Unposted

> On-Call

> 08:00A-04:30P

> Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\> Was Employee Absent the Entire Tour? Y \<RET\> Select TYPE OF TIME CODE: ?? \<RET\>

> CHOOSE FROM:

> AA AUTH ABS

> AD ADOPT

> AL ANNUAL LV

> CB FAM CARE

> CP COP

> CU COMP USED

> DL DONOR LV

> ML MIL LV

> NP NON PAY

> RL RES ANN LV

> SL SICK LV

> TR TRAINING

> TV TRAVEL

> WP LWOP

> Select TYPE OF TIME CODE: AA \<RET\> AUTH ABS TIME REMARKS CODE: ?? \<RET\>

> CHOOSE FROM:

> AA Granted by Supr. 5

> Jury Duty 6

> SF71 on file 1

> TIME REMARKS CODE: 5 \<RET\> AA Granted by Supr. 5

> Remarks: Seminar \<RET\>

#### Leave for Part of the Day

Assume that the tour of duty is 08:00A-04:30P with a 30 minute lunch at 1:00P. If an employee leaves at 01:00P, the time segment for his absence would be 01:30P­ 04:30P, not including the 30 minute lunch period.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 02, 1994)

> Would you like to edit the T & A RECORDS in alphabetical order? YES// NO

> \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE11,ONE \<RET\> PAIDEMPLOYEE11,ONE 000-00-0111

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,ONE 000-00-0111

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Station:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Normal Hours:</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
</blockquote></th>
<th><blockquote>
<p>Duty Basis:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>T&amp;L:</p>
</blockquote></td>
<td><blockquote>
<p>111</p>
</blockquote></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Flextime:</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Tue 2-Aug-94 08:00A-04:30P Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 39%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE11,ONE</p>
</blockquote></th>
<th><blockquote>
<p>VA</p>
</blockquote></th>
<th><blockquote>
<p>TIME &amp; ATTENDANCE SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>000-00-0111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Tour Beginning</p>
</blockquote></td>
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Tue 2-Aug-94</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Tour: 08:00A-04:30P

> START STOP TYPE OF TIME REMARKS CODE

> 1 01:30P 04:30P SL 1 \<RET\> SF71 on file

> 2

> 3

> 4

> 5

> 6

> 7

> Remarks: Dental app't \<RET\>

> Exit Save Refresh

> Enter a command or '^CAPTION to jump to a field in the current window. COMMAND: E \<RET\> INSERT Save changes before leaving form? (Y/N) Y \<RET\>

#### Leave During the Middle of the Day Which Includes Meal Time 

Assume that the scheduled tour of duty is 07:00A-03:30P with a 30 minute lunch at noon. If an employee is absent for a portion of a day, the timekeeper must key in segments of absence which allow for the meal time. For instance, an employee took leave from 11:00A-01:00P in the middle of his tour; the timekeeper would key in 11:00A-Noon in segment 1, and 12:30P-01:00P in segment 2, skipping the 30 minute lunch period.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 02, 1994)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE11,ONE \<RET\> PAIDEMPLOYEE11,ONE 000-00-0111

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,ONE 000-00-0111

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Station:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Normal Hours:</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
</blockquote></th>
<th><blockquote>
<p>Duty Basis:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>T&amp;L:</p>
</blockquote></td>
<td><blockquote>
<p>111</p>
</blockquote></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Flextime:</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Tue 2-Aug-94 07:00A-03:30P Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 47%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE11,ONE</p>
</blockquote></th>
<th><blockquote>
<p>VA TIME &amp; ATTENDANCE SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>000-00-0111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td><blockquote>
<p>Tour Beginning</p>
</blockquote></td>
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tour: 07:00A-03:30P</p>
</blockquote></td>
<td><blockquote>
<p>Tue 2-Aug-94</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> START STOP TYPE OF TIME REMARKS CODE

> 1 11:00A NOON SL 1 \<RET\> SF71 on file

> 2 12:30P 01:00P SL 1 \<RET\> SF71 on file

> 3

> 4

> 5

> 6

> 7

> Remarks: Dental app't

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: E \<RET\>

> Save changes before leaving form? (Y/N) Y \<RET\>

#### Combining Different Types of Leave in One Day

Assume that the scheduled tour of duty is 08:00A-04:30P. An employee can use more than one type of leave in the same day, if he/she chooses.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 02, 1994)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE11,ONE \<RET\> PAIDEMPLOYEE11,ONE 000-00-0111

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,ONE 000-00-0111

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Tue 2-Aug-94 08:00A-04:30P Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 47%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE11,ONE</p>
</blockquote></th>
<th><blockquote>
<p>VA TIME &amp; ATTENDANCE SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>000-00-0111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td><blockquote>
<p>Tour Beginning</p>
</blockquote></td>
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tour: 08:00A-04:30P</p>
</blockquote></td>
<td><blockquote>
<p>Tue 2-Aug-94</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> START STOP TYPE OF TIME REMARKS CODE

> 1 08:00A NOON AL 1 \<RET\> SF71 on file

> 2 12:30P 04:03P SL 1 \<RET\> SF71 on file

> 3

> 4

> 5

> 6

> 7

> Remarks: Appointments

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: E \<RET\>

> Save changes before leaving form? (Y/N) Y \<RET\>

#### Leave for Family Care and Bereavement, and Leave for Adoption

Below is an example of Family Care and Bereavement Leave (CB) being posted for an employee who requested leave to take care of a family member that underwent major surgery. If the employee had requested Leave for Adoption, the timekeeper would choose AD. Both kinds of leave will be deducted from the employee's Sick Leave by the Austin Automation Center.

> Select TimeKeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 043 \<RET\>

> Posting Date: T-1//1/5 \<RET\> (JAN 05, 1995)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE11,TWO \<RET\> PAIDEMPLOYEE11,TWO 000-00-0112

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,TWO 000-00-0112

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>043</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-26</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Thu 5-Jan-95 10:00A-06:30P Unposted

> Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\> Was Employee Absent the Entire Tour? Y \<RET\> Select TYPE OF TIME CODE: ?? \<RET\>

> Choose from:

> AA AUTH ABS

> AD ADOPT

> AL ANNUAL LV

> CB FAM CARE

> CP COP

> CU COMP USED

> DL DONOR LV

> ML MIL LV

> NP NON PAY

> RL RES ANN LV

> SL SICK LV

> TR TRAINING

> TV TRAVEL

> WP LWOP

> Select TYPE OF TIME CODE: CB \<RET\> FAM CARE TIME REMARKS CODE: ?? \<RET\>

> Choose from:

> SF71 on file 1

> TIME REMARKS CODE: 1 \<RET\> SF71 on file 1

> Remarks: To care for bedridden brother. \<RET\>

> Select EMPLOYEE: \<RET\>

#### Donor Leave

Following is an example of Donor Leave (DL) being posted for an employee who has requested leave to serve as an organ donor. This leave will be charged to Authorized Absence (AA) by the Austin Automation Center.

> Select TimeKeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 043 \<RET\>

> Posting Date: T-1//1/5 \<RET\> (JAN 05, 1995)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE11,THREE \<RET\> PAIDEMPLOYEE11,THREE 000-00-0113

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,THREE 000-00-0113

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>043</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-26</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Thu 5-Jan-95 08:00A-04:30P Unposted

> Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\> Was Employee Absent the Entire Tour? Y \<RET\> Select TYPE OF TIME CODE: ?? \<RET\>

> Choose from:

> AA AUTH ABS

> AD ADOPT

> AL ANNUAL LV

> CB FAM CARE

> CP COP

> CU COMP USED

> DL DONOR LV

> ML MIL LV

> NP NON PAY

> RL RES ANN LV

> SL SICK LV

> TR TRAINING

> TV TRAVEL

> WP LWOP

> Select TYPE OF TIME CODE: DL \<RET\> DONOR LV TIME REMARKS CODE: ?? \<RET\>

> Choose from:

> SF71 on file 1

> TIME REMARKS CODE: 1 \<RET\> SF71 on file 1

> Remarks: Employee will donate kidney. \<RET\>

> Select EMPLOYEE: \<RET\>

#### Post OT/CT & Unscheduled Time

In order for the PAID system to credit the proper premiums associated with an employee's overtime, the timekeeper will have to enter the correct "Time Remarks Code" when posting overtime for an employee. Below is a description of the different types of Time Remarks Codes.

<u>CB - Non-Premium T&L</u> should be used for all employees that are called back to work for a minimum of two hours on a T&L that does not have Saturday and Sunday premium pay, and no night differential.

<u>CB - Premium T&L</u> should be used for employees that are called back to work for a minimum of two hours on a T&L that has Saturday and Sunday premium pay and no night differential.

<u>OT While in Travel Status</u> should be used for Title 5 FLSA non-exempt employees when the employees are working overtime while in travel status (before or after their scheduled tours). This code should also be used if the employees are working during normal tour hours on a day off while in travel status.

<u>OT/CT on Premium T&L</u> should be used for all employees who are entitled to Saturday and Sunday premium but not night differential.

<u>OT/CT With Premiums</u> should be used for all employees who are entitled to receive Saturday/Sunday premium and night differential. All Saturday/Sunday hours posted with this code will receive Saturday/Sunday premium and all hours posted with this code between 6:00P-6:00A should receive night differential.

<u>Pre-Scheduled</u> should be used for GS employees only that do not have a premium code of E or F (not for Hybrid Title 38 employees) when OT has been scheduled in advance of the work week and employees should receive night differential during premium hours (6:00P-6:00A).

<u>Tour Coverage</u> is for full-time and part-time nurses only and Title 38 Hybrid employees. It should be used when nurses are called back to work and will be paid a minimum of two hours overtime, Saturday and Sunday premium pay, and night differential.

<u>Shift Coverage</u> should be used for part-time and intermittent nurses who will be paid night differential for hours worked (including Saturday and Sunday premium), and non-nurses who will be paid night differential from 6:00P- 6:00A. This indicator should also be used when posting Regular Unscheduled (RG) hours for part-time WG employees who will be paid shift differential for hours worked.

Assume that the following employee's tour of duty is 08:00A-04:30P. When posting OT/CT on employee's normal off day, lunch is NOT to be included. For example, the user would post 8:00A-Noon, and from 12:30P-4:30P if employee worked OT/CT from 8:00A-4:30P with a lunch. (If lunch is included, it will be added to the OT/CT with a message appearing, "OT posted exceeds requested hours".)

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select TimeKeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 03, 1994)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N \<RET\>

> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE11,ONE \<RET\> PAIDEMPLOYEE11,ONE 000-00-0111

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,ONE 000-00-0111

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Station:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Normal Hours:</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
</blockquote></th>
<th><blockquote>
<p>Duty Basis:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Flextime:</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------

> Wed 3-Aug-94 08:00A-04:30P Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

> PAIDEMPLOYEE11,ONE VA TIME & ATTENDANCE SYSTEM 000-00-0111

> Station: 111 Tour Beginning T&L: 111

> Wed 3-Aug-94

> Tour: 08:00A-04:30P

> START STOP TYPE OF TIME REMARKS CODE

> 1 04:30P 07:30P OT ?? \<RET\>

> 2

> 3

> 4

> 5

> 6

> 7

> Remarks:

> A pointer to the TIME REMARKS file (#457.4) which identifies a time remark with the type of time worked or leave taken for the first segment of the work day.

> CHOOSE FROM:

> CB - Non-Premium T&L 13

> CB - Premium T&L 14

> OT while in Travel Status 8

> OT/CT on Premium T&L 9

> Pre-Scheduled 11

> Tour Coverage 12

> Press \<PF1\>H for help INSERT

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 31%" />
<col style="width: 16%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE11,ONE</p>
</blockquote></th>
<th><blockquote>
<p>VA TIME &amp; ATTENDANCE</p>
</blockquote></th>
<th><blockquote>
<p>SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>000-00-0111</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td><blockquote>
<p>Tour Beginning</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>T&amp;L: 111</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Wed 3-Aug-94</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Tour: 08:00A-04:30P

> START STOP TYPE OF TIME REMARKS CODE

> 1 04:30P 07:30P OT 11 \<RET\> Pre-Scheduled

> 2

> 3

> 4

> 5

> 6

> 7

> Remarks: Completion of PAID

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: E \<RET\> INSERT Save changes before leaving form? (Y/N) Y \<RET\>

#### Post Baylor Plan

The Baylor Plan consists of two regularly scheduled 12-hour tours of duty that fall entirely within the period commencing at midnight Friday and ending at midnight the following Sunday. This plan is restricted to nurses who are appointed at VA health-care facilities under the provisions of 38 U.S.C. 4101(1) or 4114(a)(1)(A) and who are providing direct patient care. When employees within this plan work hours that extend their scheduled tour of duty, the timekeeper must post the time as overtime.

#### Post 9 Month AWS Employee

Nurses on the 9 Month AWS will be considered part time employees who will be scheduled to work 80 hours per pay period for 9 months of the year and will be on recess for the remaining 3 months. The periods of work do not have to be 9 contiguous months.

The nurse’s schedule will need to be reviewed and approved at the time the nurse goes onto the 9 Month AWS. Nurses working this AWS must be in pay plan M with duty basis (2) part-time and be FLSA code (E) exempt with normal hours of 80.. Note that before posting recess (RS) to the timecard, the timekeeper must enter the nurses recess periods using the Recess Enter/Edit for 9 Month AWS \[PRSA RECESS ENTER/EDIT\] option.

It is expected that the timekeeper will maintain the employee's tour and post a daily exception during periods of recess for the nurses on the 9-month AWS. Recess is only posted within the scheduled tour of duty.

The timekeeper may post the RS type of time code to indicate that the nurse was on recess the entire tour or that they were on recess for only a portion of the tour. The timekeeper may record periods of recess (RS) and periods of work during recess on the timecard of nurses working the 9 month/3 month AWS. Any work performed during the recess period should be posted as an exception along with recess exceptions. Postings of recess may be overlapped by postings of work, such as, comp time earned, overtime, unscheduled regular, etc. Nurses on the 9 Month AWS are not entitled to Holiday in Lieu of days.

> PAIDemployee,One T&L 200 0XX-XX-6000

> Date Scheduled Tour Tour Exceptions

> ------------------------------------------------------------------------ Sun 18-Feb-07 Day Off 07:00A-05:00P OT OVERTIME

> OT/CT With Premiums

> Mon 19-Feb-07 08:00A-04:30P 08:00A-04:30P RS RECESS Tue 20-Feb-07 08:00A-04:30P 08:00A-11:45A RS RECESS

> 11:45A-NOON AL ANNUAL LV SF71 on file

> 12:30P-04:30P AL ANNUAL LV SF71 on file

> Wed 21-Feb-07 08:00A-04:30P Thu 22-Feb-07 08:00A-04:30P Fri 23-Feb-07 08:00A-04:30P

> Sat 24-Feb-07 Day Off 07:00A-05:00P OT OVERTIME OT/CT With Premiums

> Sun 25-Feb-07 Day Off

> Mon 26-Feb-07 08:00A-04:30P 05:00P-06:00P OT OVERTIME Tue 27-Feb-07 08:00A-04:30P

> Wed 28-Feb-07 08:00A-04:30P Thu 1-Mar-07 08:00A-04:30P Fri 2-Mar-07 08:00A-04:30P

> Sat 3-Mar-07 Day Off 02:00A-10:00A OT OVERTIME OT/CT With Premiums

> 04:00P-MID OT OVERTIME OT/CT With Premiums

#### Post 36/40 AWS Plan

The 36/40 AWS consists of three regularly scheduled 12-hour tours of duty that fall entirely within the period commencing at midnight Sunday and ending at midnight the following Saturday. This plan is restricted to nurses who are appointed at VA health-care facilities under the provisions of 38 U.S.C. 4101(1) or 4114(a)(1)(A) and who are providing direct patient care. When employees within this plan work hours that extend their scheduled tour of duty, the timekeeper must post the time as overtime.

#### Post for Holidays

Timekeepers will not have to post any time if an employee does not work on a holiday. The PAID system will automatically post Holiday Excused (HX) for the employee.

If an employee works all or part of their tour on a holiday, the appropriate time will have to be posted.

When an employee is called in to work on a holiday and the working hours overlap with his/her regular tour, the timekeeper must make two separate postings. For example: The employee's tour is 08:00A-04:30P; he/she is called in to work for 1 1/2 hours from 07:00A to 08:30A, the timekeeper must code that the employee worked one hour OT from 07:00A-08:00A, and one-half hour Holiday Worked from 08:00A-08:30A.

If an employee is in the Non-Pay Status (LWOP or Non-Pay) on a holiday, the timekeeper must post this information.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

An example of an employee who works his/her entire regularly scheduled tour on a holiday is as follows:

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Posting Date: T-1// 7/4 \<RET\> (JUL 04, 1994)

> Would you like to edit the T & A RECORDs in alphabetical order? YES// N

> \<RET\> (NO)

> Select EMPLOYEE: PAIDEMPLOYEE8,TWO \<RET\> PAIDEMPLOYEE8,TWO 000-00-0082

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE8,TWO 000-00-0082

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-13</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Mon 4-Jul-94 08:00A-04:30P 08:00A-04:30P HX HOL EX Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? Y \<RET\>

Timekeeper Main Menu

> Select EMPLOYEE: PAIDEMPLOYEE8,TWO \<RET\> PAIDEMPLOYEE8,TWO 000-00-0082

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE8,TWO 000-00-0082

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-13</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Mon 4-Jul-94 08:00A-04:30P 08:00A-04:30P HW HOL WK Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? ^ \<RET\>

> Select EMPLOYEE: ^ \<RET\>

Below is an example of an employee who works only part of his/her tour of duty on a holiday.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 100 \<RET\>

> Posting Date: T-1// 1/18 \<RET\> (JAN 18, 1993)

> Would you like to edit the T & A RECORDS in alphabetical order? YES// NO

> \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE11,FOUR \<RET\> PAIDEMPLOYEE11,FOUR 000-00-0114

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,FOUR 000-00-0114

> Station: 111 Normal Hours: 80 Duty Basis: 1

> T&L: 100 Pay Plan: A Flextime:

> Pay Per: 93-01 FLSA: N

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Mon 18-Jan-93 08:00A-04:30P 08:00A-04:30P HX HOL EX

> Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 47%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PAIDEMPLOYEE11,FOUR</p>
</blockquote></th>
<th><blockquote>
<p>VA TIME &amp; ATTENDANCE SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>000-00-0114</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Station: 111</p>
</blockquote></td>
<td><blockquote>
<p>Tour Beginning</p>
</blockquote></td>
<td><blockquote>
<p>T&amp;L: 100</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Mon 18-Jan-93</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Tour: 08:00A-04:30P

> START STOP TYPE OF TIME REMARKS CODE

> 1 08:00A 04:30P HX

> 2 08:00A 10:00A HW \<RET\>

> 3

> 4

> 5

> 6

> 7

> Remarks: To complete project.

> ----------------------------------------------------------------------------

> Exit Save Refresh

> Enter a command or '^CAPTION to jump to a field in the current window. COMMAND: E \<RET\> INSERT Save changes before leaving form? (Y/N) Y \<RET\>

Below is an example of an employee who works before and after his/her scheduled tour of duty on a holiday.

The prompt, "Select T&L Unit" will only appear if the timekeeper has more than one T&L that he/she is responsible for.

> Select Timekeeper Main Menu Option: 1 \<RET\> Post Employee Time

> Select T&L Unit: 100 \<RET\>

> Posting Date: T-1// 2/15 \<RET\> (FEB 15, 1993)

> Would you like to edit the T & A RECORDS in alphabetical order? YES// NO

> \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE11,FIVE \<RET\> PAIDEMPLOYEE11,FIVE 000-00-0115

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE11,FIVE 000-00-0115

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Station:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Normal Hours:</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
</blockquote></th>
<th><blockquote>
<p>Duty Basis:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>T&amp;L:</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>Pay Plan:</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>Flextime:</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>93-03</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Mon 15-Feb-93 06:30A-05:00P 06:30A-05:00P HX HOL EX Enter '^' to bypass this employee.

> Did Employee Only Work Scheduled Tour? N \<RET\>

> Was Employee Absent the Entire Tour? N \<RET\>

> PAIDEMPLOYEE11,FIVE VA TIME & ATTENDANCE SYSTEM 000-00-0115

> Station: 111 Tour Beginning T&L: 100

> Mon 15-Feb-93

> Tour: 06:30A-05:00P

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>START</p>
<p>06:30A</p>
</blockquote></th>
<th><blockquote>
<p>STOP</p>
<p>05:00P</p>
</blockquote></th>
<th><blockquote>
<p>TYPE OF</p>
<p>HX</p>
</blockquote></th>
<th><blockquote>
<p>TIME</p>
</blockquote></th>
<th><blockquote>
<p>REMARKS CODE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p><strong>04:00P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>05:00P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>HW</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p><strong>05:00P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>07:00P</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>OT</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>11 &lt;RET&gt;</strong> Pre-Scheduled</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p><strong>05:30A</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>06:30A</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>OT</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Remarks: To complete project.

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: EXIT

#### Post for Daylight Savings Time

When Daylight Savings Time begins (first Sunday in April), employees that have regularly scheduled night tours will work seven hours and the timekeeper will charge them one hour of AL. If AL is not available, the charge will be LWOP. Employees that are on leave when the change occurs will be charged eight hours. When Central Standard Time begins (last Sunday in October), those employees will work nine hours and will be paid one hour OT.

#### Post Time for Doctors (Full Time & Part Time)

Administrative non duty days which fall within a period of approved leave of the same type (i.e., Annual Leave immediately before and after the administrative non duty days) are charged to the approved leave. Therefore, if a doctor's administrative non duty days are Saturday and Sunday and the doctor is on Annual Leave on Friday of week 2 of one pay period and on Monday of week 1 of the next pay period, the timekeeper must post the Annual Leave for Monday <u>before the attendance record is certified</u> for the first pay period for the administrative non duty days to also be charged to Annual Leave. This applies to Annual (AL), Restored Annual Leave (RL), Sick Leave (SL), Non Pay Annual Leave (NL), Continuation of Pay (CP), Authorized Absence (AA), and Leave Without Pay (WP). When one type of leave is taken before the day(s) off and another type is taken the day after, leave will not be charged for the non-duty days.

Leave Without Pay (WP) is automated for any LWOP surrounding a holiday. If the employee (who is paid in days) is on LWOP on Friday, the following Monday is a holiday, and the employee is on LWOP on Tuesday, the decomposition automatically charges LWOP to the weekend as well as the holiday. Similarly, if an employee is on LWOP on Thursday, Friday is a holiday, and the employee is on LWOP on the following Monday, the decomposition automatically charges LWOP for the holiday as well as the weekend.

> **NOTE:** Non Pay (NP) must be posted on Administrative Days Off, when applicable. Military Leave may need to be posted on Administrative Days Off, depending upon the orders.

In Lieu Time: Currently, this version of PAID requires manual tracking of "in lieu" days for doctors. VA Form 4-5631a (subsidiary timecard) will be needed in order to keep a record of "in lieu" days and compensatory time earned by doctors. Also, this version is limited in fully automating the Payroll system for part time physicians with adjustable work hours. VA Form 4-5631a will still be updated manually in order to keep track of leave for these physicians. After VA Form 4­5631a has been verified by the employee's supervisor, the unit timekeeper will then record the data in the PAID system.

#### List Daily Exceptions

This option allows the timekeeper to list any time and attendance report exceptions for a date selected. The name of the employee and a short message are displayed. The timekeeper should try to clear up these exceptions as soon as possible.

> Select Timekeeper Main Menu Option: 2 \<RET\> List Daily Exceptions

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// \<RET\> (AUG 03, 1994)

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 111 EXCEPTIONS

> Wed 3-Aug-94

> PAIDEMPLOYEE11,ONE

> 04:30P OT not Requested

> PAIDEMPLOYEE11,SIX

> 08:00A AA not Requested

> PAIDEMPLOYEE11,SEVEN

No Time Posted

> PAIDEMPLOYEE11,EIGHT

> 07:30A AL not Requested

> Press RETURN to Continue.^ \<RET\>

#### Display Pay Period Exceptions

This option allows the timekeeper to list any time and attendance report exceptions for a selected pay period. The name of the employee, date of the exception, and a short message are displayed. The user will only be shown the exceptions from the beginning of the pay period up to the chosen date. The timekeeper should try to clear up these exceptions as soon as possible.

> Select Timekeeper Main Menu Option: 3 \<RET\> Display Pay Period Exceptions

> Select T&L Unit: 111 \<RET\>

> Posting Date: T-1// 8/4 \<RET\> (AUG 04, 1994)

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 111 EXCEPTIONS

> Sun 24-Jul-94 to Sat 6-Aug-94

> PAIDEMPLOYEE11,NINE

> Mon 25-Jul-94 No Time Posted

> PAIDEMPLOYEE,EIGHT

> Mon 25-Jul-94 No Time Posted

> Fri 29-Jul-94 08:00A AL not Requested

> Tue 2-Aug-94 08:00A AA not Requested

> PAIDEMPLOYEE11,ONE

> Wed 3-Aug-94 04:30P OT not Requested

> PAIDEMPLOYEE12,TEN

> Tue 26-Jul-94 MID AL not Requested

> PAIDEMPLOYEE12,ONE

> Fri 29-Jul-94 04:00P WP not Requested

> Tue 2-Aug-94 11:30A AL Requested but not Approved

> PAIDEMPLOYEE12,TWO

> Tue 26-Jul-94 08:00A ML not Requested

> Press RETURN to Continue.^ \<RET\>

#### Employee Data

There are five Employee Data options associated with this menu selection. The display options allow the timekeeper to display on the screen, data which has been stored for a particular employee. All options will be discussed later. However, option 4, Enter/Edit Employee Tour of Duty, is the heart of the timekeeping system and timekeepers should exercise extreme care when executing this option.

> Select Timekeeper Main Menu Option: 4 \<RET\> Employee Data

> 1 Display Posted Data

> 2 Display Employee Pay Period

> 3 Display Employee Tour of Duty

> 4 Enter/Edit Employee Tour of Duty

> 5 Employee Leave Balances

#### Display Posted Data

This option allows the timekeeper to select an employee and a posting date. The employee's scheduled tour of duty and any exceptions to that tour will be displayed.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

Select Employee Data Option: 1 Display Posted Data

Select T&L Unit: 110 NHCU

Posting Date: T-1//6/15 (JUN 15, 2012)

Select EMPLOYEE: PAIDEMPLOYEE12,ONE PAIDEMPLOYEE12,ONE 111-11-1114

Select Device: HOME// HOME (CRT) Right Margin: 80//

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TIME AND ATTENDANCE DATA

PAIDEMPLOYEE12,ONE 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-12 Telework Indicator: E FLSA: N

Date TW Scheduled Tour Tour Exceptions

------------------------------------------------------------------------

Fri 15-Jun-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Press RETURN to Continue.

#### Display Employee Pay Period

Displays the employee's name, all 14 dates in the pay period, the employee's scheduled tour(s) and any exceptions to the scheduled tour(s). The timekeeper needs this data in order to verify posting.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE PAY PERIOD DATA

Select T&L Unit: 110 NHCU

Select EMPLOYEE: PAIDEMPLOYEE,BLUE PAIDEMPLOYEE,BLUE 111-11-1114

Posting Date: 5/6 (MAY 06, 2012)

Select Device: HOME// HOME (CRT) Right Margin: 80//

PAIDEMPLOYEE,BLUE T&L 110 Telework Ind: E 1XX-XX-1114

Date TW Scheduled Tour Tour Exceptions

------------------------------------------------------------------------

Sun 6-May-12 Day Off

Mon 7-May-12 07:00A-03:30P

Tue 8-May-12 07:00A-03:30P

Wed 9-May-12 07:00A-03:30P

Thu 10-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 11-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 12-May-12 Day Off

Sun 13-May-12 Day Off

Mon 14-May-12 07:00A-03:30P

Tue 15-May-12 07:00A-03:30P

Wed 16-May-12 07:00A-03:30P

Thu 17-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Fri 18-May-12 REG 07:00A-03:30P 8.00 Hours - Telework REG

Sat 19-May-12 Day Off

Select EMPLOYEE:

#### Display Employee Tour of Duty

This option allows the timekeeper to display the authorized tour of duty for a selected employee. The timekeeper will be prompted to display the long or short version of the tour. Most tours have one segment and the short version is sufficient to display the entire tour. However, if a tour has built-in OT, stand-by, etc., then a long display is preferable since all segments of the tour will be displayed.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

Select Employee Data Option: 3 Display Employee Tour of Duty

Select T&L Unit: 110 NHCU

C = Current Pay Period beginning 3-Jun-12

L = Last Pay Period beginning 20-May-12

N = Next Pay Period beginning 17-Jun-12

Which Pay Period? C // C

Select Type of Display (S or L): SHORT//

Select EMPLOYEE: PAIDEMPLOYEE,BLUE PAIDEMPLOYEE,BLUE 111-11-1114

Select Device: HOME// HOME (CRT) Right Margin: 80//

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TOUR OF DUTY

PAIDEMPLOYEE,BLUE 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-12 Telework Indicator: E FLSA: N

TW Week 1 - 3-Jun-12 TW Week 2 - 10-Jun-12

Sun DAY OFF DAY OFF

Mon 07:00A-03:30P 07:00A-03:30P

Tue 07:00A-03:30P 07:00A-03:30P

Wed 07:00A-03:30P 07:00A-03:30P

Thu REG 07:00A-03:30P REG 07:00A-03:30P

Fri REG 07:00A-03:30P REG 07:00A-03:30P

Sat DAY OFF DAY OFF

Enter return to continue.

#### Enter/Edit Employee Tour of Duty

This option is crucial to this system. If an employee's tour of duty is not correct, the employee's pay will not be correct. Therefore, it is strongly recommended that each timekeeper review the documentation in this section. It is imperative that the proper tour and/or tour with tour code combination be assigned to each type of employee (i.e., General Schedule, Wage Grade, Nurse, etc.) to ensure that the proper number of hours is being calculated for certain types of premium pay (i.e., shift differential, on-call pay, etc.) in which each employee is entitled. If an error is discovered and corrected in the employee’s scheduled tour of duty after time has been posted, all existing daily postings for days where the tour was changed will be erased. The timekeeper must re-post these days.

When a permanent tour of duty is established for an employee, it will not have to be done again unless the employee changes his/her tour of duty or transfers to another T&L Unit. Temporary changes can be made to an employee's tour of duty for a pay period that will not affect the employee's permanent tour of duty. For example, PAIDEMPLOYEE,ONE's normal schedule is Monday through Friday, 08:00A-04:30P; however, for two weeks PAIDEMPLOYEE,ONE is needed to cover the 07:00A-03:30P tour. The timekeeper will use this option to enter the new tour: The system will ask "Is this tour change Temporary or Permanent? P//". The timekeeper will respond to the prompt for Temporary and all posted data for that pay period will reflect the new tour. When the next pay period is opened, the employee's record will reflect the permanent tour.

The system will prevent timekeepers from saving a tour of duty if there are any days with overlapping tours. The software not only checks for overlaps within the pay period being edited, but also checks to ensure the pay period being edited does not overlap tours with the prior or next pay period. In all cases, when overlapping tours are found, the software will prevent you from saving the tour of duty.

Following are examples of the messages you will see when being prevented from saving tours with overlaps.

As of July 2012, the Telework Indicator code is displayed next to the employee’s name. The telework type code is displayed under the “TW” column, next to the date.

> ERROR: Current-PP 08-14, Day 7 Primary overlaps Day 6 Primary

> ERROR: Xmitted-PP 08-12, Day 10 Primary overlaps Day 11 Primary

Please note that overlaps which existed prior to this functionality being implemented with patch PRS\*4\*117 will remain in the system.

> **NOTE:** The timekeeper must enter tours of duty for the next pay period by COB on the second Thursday of the current pay period. If this is not done, the employees that have changing tours and rotating holidays will not be scheduled to be off on the correct holiday.

Following is an explanation of three tours that the timekeeper may choose: 1) A Two-day Tour; 2) A Tour that has Two or More Segments, and 3) Two Separate Tours on the Same Day:

<u>Two-Day Tour:</u> Any tour that includes periods of time on two different days. For example: Police officers who begin their tours at 11:00P and are off at 7:00am (the next morning). Some of the problems with such a tour involve scheduling. Supervisors must remember that 80 hours must be scheduled between midnight on Sunday and midnight on the last Saturday of that pay period. They must remember that if the employee begins his/her tour at 11:00P on the last Saturday of a pay period, there is one hour that's credited to the current pay period and seven hours credited to the next pay period. One less problem will exist with these tours, once a station has two pay periods in the system. If a station is ready to bring up a T&L that uses this type of tour, they must have at least one pay period in the system before the one that is going to be transmitted to Austin. The reason for this is that the portion of the tour that carried over from the previous pay period is not in the system. When assigning this tour to an employee, the timekeeper should assign it on the day that the tour begins, for instance, on Saturday. The Sunday tour would be either a day off or another tour that begins on Sunday. This is not to be confused with a second tour on the same day as indicated below. This is one tour on Saturday and one tour on Sunday.

<u>Tour That has Two or More Segments:</u> This is any tour that has two or more different types of time. For example: Segment one is 7:00am-3:30P with no special indicator; segment two is 3:30P-midnight with an indicator of on-call. A special note should be made at this point that the timekeeper must look at ALL segments of the tour to guarantee proper payment to the employee. For instance, use example number 1 above. If another employee had the same regular tour of 7:00am-3:30P, but the on-call tour was midnight-7:00am, Payroll would have to create a different tour showing the segments as midnight-7:00am on-call and 7:00-3:30 with no indicator.

<u>Two Separate Tours on the Same Day:</u> This tour is not to be confused with a tour covering two days. An employee has a scheduled tour of midnight-8:00am on Monday. That same employee also has a scheduled tour of 3:30P-midnight (also) on Monday. These are two separate and distinct tours, both BEGINNING on the same calendar day. The key words here are "beginning on the same calendar day". The tour is entered as follows:

> Select Employee Data Option: 4 \<RET\> Enter/Edit Employee Tour of Duty

> Select T&L Unit: 043 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE1,EIGHT PAIDEMPLOYEE1,EIGHT 000-00-0018

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TOUR OF DUTY

> PAIDEMPLOYEE1,EIGHT 0XX-XX-

> 0018

> Station: 111 Normal Hours: 80 Duty Basis:

> 1

> T&L: 043 Pay Plan: 1 Comp/Flex:

> 0

> Pay Per: 07-26 FLSA: N

> C = Current Pay Period beginning 23-Dec-07

> L = Last Pay Period beginning 9-Dec-07

> N = Next Pay Period beginning 6-Jan-08

> Which Pay Period? C // \<RET\>

> Is this tour change Temporary or Permanent? P// \<RET\> permanent

> Do you wish to enter a fixed Mon-Fri Tour? YES \<RET\>

> Select TOUR OF DUTY: 72 \<RET\> MID-08:00A Meal: 0 ... done

> Do you wish to enter a Second Tour for any Day? N// Y \<RET\>

> Warning: This second tour will be temporary and will not carry forward. For which Day (1-14) do you wish to enter a second Tour? 2 \<RET\>

> T&L on which Tour will be worked: 043// \<RET\>

> Select TOUR OF DUTY: 32 \<RET\> 03:30P-MID Meal: 30 ... done

> Warning: Normal Hours are 80; Tour Hours are 88

> Compressed Tour Indicator: None// \<RET\>

> Select EMPLOYEE: \<RET\>

The compressed/flexitour indicator is now displayed whenever a tour change is made and can be set as desired. The second tour may be deleted by selecting the same employee and entering the same answers as above. The following prompts show that it was deleted.

The following is an example of entering a permanent tour for the current pay period:

> For which Day (1-14) do you wish to enter a second Tour? 2 \<RET\> Existing Second Tour 03:30P-MID will be deleted. \<RET\>

> Select Employee Data Option: 4 \<RET\> Enter/Edit Employee Tour of Duty

> Select T&L Unit: 111 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE7,FIVE PAIDEMPLOYEE7,FIVE 000-00-0075

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TOUR OF DUTY

> PAIDEMPLOYEE7,FIVE 0XX-XX-

> 0075

> Station: 111 Normal Hours: 80 Duty Basis:

> 1

> T&L: 111 Pay Plan: 1 Comp/Flex:

> 0

> Pay Per: 07-26 FLSA: N

> C = Current Pay Period beginning 23-Dec-07

> L = Last Pay Period beginning 9-Dec-07

> N = Next Pay Period beginning 6-Jan-08

> Which Pay Period? C // \<RET\>

> Is this tour change Temporary or Permanent? P// \<RET\> permanent

> Do you wish to enter a fixed Mon-Fri Tour? Y \<RET\>

> Select TOUR OF DUTY: 10 \<RET\> 07:00A-03:30P Meal: 30 ... done

> Do you wish to enter a Second Tour for any Day? N// \<RET\>

> Compressed Tour Indicator: None// \<RET\>

> Select EMPLOYEE: \<RET\>

Following is an example of the sequence of events which will occur when entering a tour of duty for intermittent employees. Since there is no specific tour associated with this type of employee, the system will automatically set up the scheduled tour.

> Select Employee Data Option: 4 \<RET\> Enter/Edit Employee Tour of Duty

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 41%" />
<col style="width: 30%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select</p>
</blockquote></th>
<th><blockquote>
<p>T&amp;L Unit: <strong>111 &lt;RET&gt;</strong></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select</p>
</blockquote></td>
<td><blockquote>
<p>EMPLOYEE: <strong>PAIDEMPLOYEE7,FIVE</strong></p>
</blockquote></td>
<td><blockquote>
<p>PAIDEMPLOYEE7,FIVE</p>
</blockquote></td>
<td><blockquote>
<p>000-00-0075</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TOUR OF DUTY

> PAIDEMPLOYEE7,FIVE 0XX-XX-0075

> Station: 111 Normal Hours: 80 Duty Basis: 1

> T&L: 111 Pay Plan: 1 Flextime:

> Pay Per: 07-26 FLSA: N

> C = Current Pay Period beginning 23-Dec-07

> L = Last Pay Period beginning 9-Dec-07

> N = Next Pay Period beginning 6-Jan-08

> Which Pay Period? C // \<RET\>

> This is an Intermittent employee with no specified tour. Time records will now be updated to indicate this. ...done Select EMPLOYEE: ^ \<RET\>

Effective July 2012, employee tours of duty can be updated to include telework indicators. The following is an example of entering Regular Telework Hours for the current pay period on a permanent basis. Telework indicators are entered by typing “REG” (Regular) into the appropriate text box when scrolling through the employee schedule. Enter “Save” and hit Return to save the schedule changes. After entering these changes, timekeepers will be prompted to designate compressed tour indicators, if any.

Select Employee Data Option: 4 Enter/Edit Employee Tour of Duty

Select T&L Unit: 110 NHCU

Select EMPLOYEE: PAIDEMPLOYEE,ZERO PAIDEMPLOYEE,ZERO 111-11-1114

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TOUR OF DUTY

PAIDEMPLOYEE,ZERO 1XX-XX-1114

Station: 999 Normal Hours: 80 Duty Basis: 1

T&L: 110 Pay Plan: A Comp/Flex: 0

Pay Per: 12-12 Telework Indicator: E FLSA: N

C = Current Pay Period beginning 3-Jun-12

L = Last Pay Period beginning 20-May-12

N = Next Pay Period beginning 17-Jun-12

Which Pay Period? C //

Is this tour change Temporary or Permanent? P// ermanent

Do you wish to enter a fixed Mon-Fri Tour? YES

Do you wish to schedule any telework tours? YES

Select TOUR OF DUTY: 10 07:00A-03:30P Meal: 30 ... done

VA TIME & ATTENDANCE SYSTEM

EMPLOYEE TOUR OF DUTY

PAIDEMPLOYEE,ZERO Telework Indicator: E 1XX-XX-1114

TW Week 1 - 3-Jun-12 TW Week 2 - 10-Jun-12

<u>Sun</u> DAY OFFDAY OFF

<u>Mon</u> 07:00A-03:30P07:00A-03:30P

<u>Tue</u> 07:00A-03:30P07:00A-03:30P

<u>Wed</u> REG07:00A-03:30PREG07:00A-03:30P

<u>Thu</u> REG07:00A-03:30PREG07:00A-03:30P

<u>Fri</u> REG07:00A-03:30PREG07:00A-03:30P

<u>Sat</u> DAY OFFDAY OFF

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

#### #### Employee Leave Balances

This option allows the timekeeper to view an employee's Annual Leave, Sick Leave, Compensatory Time, and Restored Annual Leave (if any) balances on all employees that are in the T&L that he/she is responsible for.

> Select Employee Data Option: 5 \<RET\> Employee Leave Balances

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE12,SIX \<RET\> PAIDEMPLOYEE12,SIX 000-00-0126

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> PAIDEMPLOYEE12,SIX 122-55-0333

> Balances are as of Sat 29-Oct-94

> Leave Group: 3

> Annual Leave Balance: 293.000

> Sick Leave Balance: 403.250

> Comp Time: 10.000 must be used by 26-Nov-94

> 4 Restored Leave: 40.000

> Press RETURN to Continue.

#### Recess Enter/Edit for 9 Month AWS

This option provides timekeepers the ability to enter and edit Recess Schedules for nurses working a 9 month/3 month alternative work schedule (AWS). Timekeepers may only enter or edit Recess Schedules for nurses on the 9-month/3-month AWS for T&L units assigned to them. Timekeepers must have entered recess time on the schedule for any weeks in which they need to post recess time on the nurse’s timecard. The Post Employee Time option will check the schedule to ensure that some recess is scheduled before allowing the Recess (RS) type of time to be coded on the timecard.

When entering a new Recess Schedule, the date that the AWS becomes effective is required. If a date is entered that is not the first Sunday of the pay period, the software assumes the first Sunday of the pay period for the date you entered.

Only Recess Schedules for the current, next and last fiscal years may be entered and edited. This option uses ListManager Screens to display a list of weeks, in calendar format, from the first week of the AWS through the end of the fiscal year. The Recess Hours and Hours Posted are also displayed.

Available actions are displayed at the bottom of the ListManager Screen. Enter ?? at the “Select Action”: prompt for more ListManager actions, and a brief description of all actions. Enter HE (Help) for more detailed descriptions.

#### Available Actions

SE Select Recess Weeks

Enter SE at the “Select Action” prompt to select weeks, using the number in the left hand column of the list. You may select multiple weeks by entering week numbers separated by commas or spaces, and you may select a range of weeks by using a hyphen. For example: 3,6 or 3 6 to select weeks 3 and 6; or 1-3 to select weeks 1 through 3. You are then prompted for the hours to enter for all of the weeks you selected. If the weeks are in the past, the tour of duty hours stored in the employee’s timecard may be used by accepting the default of Yes to the “Set recess hours to current tour of duty hours? YES//” prompt. Alternatively, you can choose the employee’s current tour hours from the timecard as the recess hours or you may specify the recess hours for each week of the pay period for the weeks selected. In all cases, the recess hours specified are applied to all the weeks selected.

EH Edit Recess Hours

Enter EH at the “Select Action” prompt to select any of the weeks in the list by number. You will be prompted to enter the recess hours for each week that you selected.

CR Cancel Recess Weeks

Enter CR at the “Select Action” prompt to select any of the weeks in the list by number. Any recess hours from the selection will be removed.

NS Change AWS Start

Enter NS at the “Select Action” prompt to change the date the AWS schedule takes effect. This action will remove any Recess Scheduled during the fiscal year that occurs before the new start date. If you enter a date other than the first day of a pay period, the action will automatically set the AWS start date to the first day of the pay period in which the date you entered falls. The number of weeks available for recess is 25% of the weeks from the start date to the end of the fiscal year.

GH Recess Hours Summary

Enter GH at the “Select Action” prompt to see a summary screen with recess totals. Note: Be sure to scroll down to see the whole report.

HE Help

Enter HE at the “Select Action” prompt for more detailed help about the available actions.

SV Save Recess Schedule

Enter SV at the “Select Action” prompt to save any edits you have made to the schedule and continue editing.

EX Exit and Save Recess

Enter EX at the “Select Action” prompt to save any edits you have made to the schedule and exit the option.

QU Quit without Saving

Enter QU at the “Select Action” prompt to quit and not save any of the changes you made.

#### The ListManager

The ListManager is a tool that displays a list of items in a screen format and provides the following functionality:

- Browse through the list
- Select items that need action
- Take action against those items
- Select other ListManager actions without leaving the option

Actions(s) are entered by typing the name(s) or mnemonics(s) at the "Select Action" prompt. The mnemonic for each action appears in brackets \[ \]after the action name.

You can also select an action and entry number by using an equal sign (=).

- EH=1 Edits recess hours for week 1
- EH=3 4 5 Edits recess hours for week 3, 4, 5
- EH=1-3 Edits recess hours for week 1, 2, 3

In addition to the various actions available that are specific to this option, ListManager provides generic actions applicable to any ListManager screen. You may enter double question marks (??) at the "Select Action" prompt for a list of all actions available. Following is a list of the generic actions available.

| Action                        | Description                                                                  |
|-------------------------------|------------------------------------------------------------------------------|
|                               |                                                                              |
| Next Screen \[+\]             | Move to the next screen.                                                     |
|                               |                                                                              |
| Previous Screen \[-\]         | Move to the previous screen.                                                 |
|                               |                                                                              |
| Up a Line \[UP\]              | Move up one line.                                                            |
|                               |                                                                              |
| Down a Line \[DN\]            | Move down one line.                                                          |
|                               |                                                                              |
| Shift View to Right \[\>\]    | Move the screen to the right if the screen width is more than 80 characters. |
|                               |                                                                              |
| Shift View to Left \[\<\]     | Move the screen to the left if the screen width is more than 80 characters.  |
|                               |                                                                              |
| First Screen \[FS\]           | Move to the first screen.                                                    |
|                               |                                                                              |
| Last Screen \[LS\]            | Move to the last screen.                                                     |
|                               |                                                                              |
| Go to Page \[GO\]             | Move to any selected page in the list.                                       |
|                               |                                                                              |
| Re Display Screen \[RD\]      | Redisplay the current screen.                                                |
|                               |                                                                              |
| Print Screen \[PS\]           | Print the header and the portion of the list currently displayed.            |
|                               |                                                                              |
| Print List \[PL\]             | Print the list of entries currently displayed.                               |
|                               |                                                                              |
| Search List \[SL\]            | Find selected text in list of entries.                                       |
|                               |                                                                              |
| Auto Display(On/Off) \[ADPL\] | Toggle the menu of actions to be displayed/not displayed automatically.      |
|                               |                                                                              |
| Quit \[QU\]                   | Exit the screen.                                                             |

> Select Employee Data Option: Recess Enter/Edit for 9 Month AWS Select T&L Unit: 200

> Select AWS NURSE: PAIDemployee,One 000-11-6000

> Select one of the following:

> C Current FY2007 begins 10/01/06-has AWS start date 02/04/07

> N Next FY2008 begins 10/14/07-has no existing record. L Last FY2006 begins 10/02/05-has no existing record.

> Select fiscal year: C// \<RET\> current FY2007 begins 10/01/06-has AWS start date

> 02/04/07

> RECESS TRACKING VIEW/EDIT Jul 17, 2007@15:41:39 Page: 1 of 3

> FY2007 Recess Week Editor for 9 month AWS with start date 02/04/07 (pp 07-03) PAIDemployee,One XXX-XX-6000 T&L Unit: 200

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Feb 2007============

> 19 07-03 4 5 6 7 8 9 10

> 20 11 12 13 14 15 16 17

> 21 07-04 18 19 20 21 22 23 24

> 22 25 26 27 28 1 2 3

> =============Mar 2007============

> 23 07-05 4 5 6 7 8 9 10

> 24 11 12 13 14 15 16 17

> 25 07-06 18 19 20 21 22 23 24

> 26 25 26 27 28 29 30 31

> =============Apr 2007============

> 27 07-07 1 2 3 4 5 6 7

> 28 8 9 10 11 12 13 14

> 29 07-08 15 16 17 18 19 20 21

> 30 22 23 24 25 26 27 28

> +---------Enter ?? for more actions-------------------------------------------- SE Select Recess Weeks NS Change AWS Start SV Save Recess Schedule

> EH Edit Recess Hours GH Recess Hours Summary QU Quit without Saving CR Cancel Recess Weeks HE Help EX Exit and Save Recess Select Action: Next Screen// SE Select Recess Weeks

> Enter week numbers to set to recess: (19-54): 19-26

> Current tour of duty hours are as follows: Week 1 of pay period: 40

> Week 2 of pay period: 40

> Choose yes to mark recess weeks with current tour of duty hours for week 1 and 2.

> Set recess hours to current tour of duty hours? YES// \<RET\>

> RECESS TRACKING VIEW/EDIT Jul 17, 2007@15:41:53 Page: 1 of 3

> FY2007 Recess Week Editor for 9 month AWS with start date 02/04/07 (pp 07-03) PAIDemployee,One XXX-XX-6000 T&L Unit: 200

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Feb 2007============

> 19 07-03 4 5 6 7 8 9 10 40.00

> 20 11 12 13 14 15 16 17 40.00

> 21 07-04 18 19 20 21 22 23 24 40.00

> 22 25 26 27 28 1 2 3 40.00

> =============Mar 2007============

> 23 07-05 4 5 6 7 8 9 10 40.00

> 24 11 12 13 14 15 16 17 40.00

> 25 07-06 18 19 20 21 22 23 24 40.00

> 26 25 26 27 28 29 30 31 40.00

> =============Apr 2007============

> 27 07-07 1 2 3 4 5 6 7

> 28 8 9 10 11 12 13 14

> 29 07-08 15 16 17 18 19 20 21

> 30 22 23 24 25 26 27 28

> +---------Enter ?? for more actions-------------------------------------------- SE Select Recess Weeks NS Change AWS Start SV Save Recess Schedule

> EH Edit Recess Hours GH Recess Hours Summary QU Quit without Saving CR Cancel Recess Weeks HE Help EX Exit and Save Recess Select Action: Next Screen// GH Recess Hours Summary

> RECESS SCHEDULE SUMMARY Jul 17, 2007@15:41:56 Page: 1 of 1

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 02/04/07 (pp 07-03) PAIDemployee,One XXX-XX-6000 T&L Unit: 200

> --Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------

> 19 02/04/07 40.00 0.00

> 20 02/11/07 40.00 0.00

> 21 02/18/07 40.00 0.00

> 22 02/25/07 40.00 0.00

> 23 03/04/07 40.00 0.00

> 24 03/11/07 40.00 0.00

> 25 03/18/07 40.00 0.00

> 26 03/25/07 40.00 0.00

> ====== ====== Total Recess. Scheduled: 320.00 Posted: 0.00

> Total Weeks in AWS FY Schedule: 36.00

> Total available FY recess hrs: 360.00 (9 weeks) WARNING--Recess hours under scheduled: 40.00

> ----------WARNING--Recess hours are under scheduled: 40.00-------------------- Select Action:Quit// \<RET\> QUIT

> RECESS TRACKING VIEW/EDIT Jul 17, 2007@15:42:22 Page: 1 of 3

> FY2007 Recess Week Editor for 9 month AWS with start date 02/04/07 (pp 07-03) PAIDemployee,One XXX-XX-6000 T&L Unit: 200

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Feb 2007============

> 19 07-03 4 5 6 7 8 9 10 40.00

> 20 11 12 13 14 15 16 17 40.00

> 21 07-04 18 19 20 21 22 23 24 40.00

> 22 25 26 27 28 1 2 3 40.00

> =============Mar 2007============

> 23 07-05 4 5 6 7 8 9 10 40.00

> 24 11 12 13 14 15 16 17 40.00

> 25 07-06 18 19 20 21 22 23 24 40.00

> 26 25 26 27 28 29 30 31 40.00

> =============Apr 2007============

> 27 07-07 1 2 3 4 5 6 7

> 28 8 9 10 11 12 13 14

> 29 07-08 15 16 17 18 19 20 21

> 30 22 23 24 25 26 27 28

> +---------Enter ?? for more actions-------------------------------------------- SE Select Recess Weeks NS Change AWS Start SV Save Recess Schedule

> EH Edit Recess Hours GH Recess Hours Summary QU Quit without Saving CR Cancel Recess Weeks HE Help EX Exit and Save Recess Select Action: Next Screen// EH Edit Recess Hours

> Enter week numbers to set to recess: (19-54): 27

> Recess hours remaining to schedule: 40

> Enter recess hours for week 27: (0-72): 40// \<RET\>

> RECESS TRACKING VIEW/EDIT Jul 17, 2007@15:42:34 Page: 1 of 3

> FY2007 Recess Week Editor for 9 month AWS with start date 02/04/07 (pp 07-03) PAIDemployee,One XXX-XX-6000 T&L Unit: 200

> -Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Feb 2007============

> 19 07-03 4 5 6 7 8 9 10 40.00

> 20 11 12 13 14 15 16 17 40.00

> 21 07-04 18 19 20 21 22 23 24 40.00

> 22 25 26 27 28 1 2 3 40.00

> =============Mar 2007============

> 23 07-05 4 5 6 7 8 9 10 40.00

> 24 11 12 13 14 15 16 17 40.00

> 25 07-06 18 19 20 21 22 23 24 40.00

> 26 25 26 27 28 29 30 31 40.00

> =============Apr 2007============

> 27 07-07 1 2 3 4 5 6 7 40.00

> 28 8 9 10 11 12 13 14

> 29 07-08 15 16 17 18 19 20 21

> 30 22 23 24 25 26 27 28

> +---------Enter ?? for more actions-------------------------------------------- SE Select Recess Weeks NS Change AWS Start SV Save Recess Schedule

> EH Edit Recess Hours GH Recess Hours Summary QU Quit without Saving CR Cancel Recess Weeks HE Help EX Exit and Save Recess Select Action: Next Screen// EX Exit and Save Recess

> Changes Saved.

> Scheduled recess hours match hours available for recess. Enter return to continue.

#### Display Employee Tour Hours

This option allows timekeepers to view an employee's tour of duty number, tour of duty hours, tour hours on each day and 8B normal hours for a selected pay period within the T&L units assigned to them. The Tour Hours column contains a total of any tour hours that fall on that day, therefore, two day tours will contribute hours to both days on which they fall.

Timekeepers can also choose to print the footnotes explaining the report headings.

> Select Employee Data Option: Display Employee \<RET\> Display Employee Tour

> Hours

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE,ONE \<RET\> 000-01-4202

> 0XX-XX-4202

> Select PAY PERIOD: 08-08 \<RET\>

> Include report footnotes? N// YES \<RET\>

> DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> VA TIME & ATTENDANCE REPORT for Timekeeper--NOV 06, 2008@13:41 p1

> Display Employee Tour Hours: PP 08-08 (13-Apr-08 thru 26-Apr-08)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EMPLOYEE NAME</p>
</blockquote></th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>8B NRM HRS</p>
</blockquote></th>
<th><blockquote>
<p>ToD HRS*</p>
</blockquote></th>
<th><blockquote>
<p>IEN 450</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>======================</p>
<p>PAIDEMPLOYEE, ONE</p>
</blockquote></td>
<td><blockquote>
<p>===========</p>
<p>0XX-XX-4202</p>
</blockquote></td>
<td><blockquote>
<p>==========</p>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>=======</p>
<p>14202</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Day</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 1</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
<th><blockquote>
<p>ToD #*</p>
</blockquote></th>
<th><blockquote>
<p>Tour Week 2</p>
</blockquote></th>
<th><blockquote>
<p>Hours*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>---</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
<td><blockquote>
<p>-----------</p>
</blockquote></td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mon</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wed</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Thu</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fri</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>07:00P-MID</p>
</blockquote></td>
<td><blockquote>
<p>5.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Day Off</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter RETURN to continue or '^' to exit: \<RET\>

> =================================================================

> FOOTNOTES TO REPORT HEADINGS

> ============================

> \*ToD HRS (Tour of Duty Hours) The total Tour of Duty hours that fall within the

> -------- two week pay period, beginning midnight Saturday. Hours that cross midnight from a tour that starts on the last day of a pay period will appear on the following pay period.

> .....................................................................

> \*Hours (DAILY TOUR HOURS) This column contains actual tour hours that fall

> ------ on that day from the 24 hour period beginning at midnight. A two day tour will contribute hours to each day the tour falls on. Hours

> that cross midnight from a tour that starts on the last day of a pay period will appear on the following pay period.

> .....................................................................

> \*ToD \# (Tour of Duty Number) The tour's entry number in the Tour

> ------ of Duty file (#457.1)

> .....................................................................

> Enter return to continue.

#### List Leave Requests

This option allows the timekeeper to list leave requests for one or more employees. The timekeeper enters a 'begin' date and an 'end' date. All leave requests for the employee(s) chosen will be displayed. When there is more than one employee, the list may be sorted by employees' names or dates of leave requests. The date, time, type of leave, remarks, and status are listed.

> Select Timekeeper Main Menu Option: 5 \<RET\> List Leave Requests

> Select T&L Unit: 043 \<RET\>

> Select Employee(or RETURN for All): PAIDEMPLYEE12,SEVEN \<RET\> PAIDEMPLYEE12,SEVEN

> 000-00-00127

> Begin with Date: T \<RET\> (JAN 27, 1993) End with Date: T+6 \<RET\> (FEB 02, 1993) Sort by: (E=Employee D=Date) E// \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 043 LEAVE REQUESTS

> From 27-Jan-93 to 02-Feb-93

> PAIDEMPLYEE12,SEVEN 000-00-00127

> NOON 28-Jan-93 to 03:30P 28-Jan-93 Sick Leave Requested

> OUTPATIENT SURGERY

> 11:00A 29-Jan-93 to 02:00P 29-Jan-93 Annual Leave Approved

> CAR REPAIRS NEEDED

> 07:00A 1-Feb-93 to 03:30p 1-Feb-93 Authorized Absence Requested

> TO ATTEND A PAID MEETING

> 03:30P 2-Feb-93 to 05:30P 2-Feb-93 Compensatory Time Requested

> MUST COMPLETE PAID PROJECT

> Press RETURN to Continue. ^ \<RET\>

#### Display OT/CT Requests

This option allows a user to list overtime and compensatory time requests for one or more employees. The user enters a 'begin' date and an 'end' date. All requests for the employee(s) chosen will be displayed. The date, number of hours, type of request, the justification for the request, and status are listed.

> Select TimeKeeper Main Menu Option: 6 \<RET\> Display OT/CT Requests

> Select T&L Unit: 101 \<RET\>

> Select EMPLOYEE (or RETURN for All): PAIDEMPLOYEE12,EIGHT \<RET\>

> PAIDEMPLOYEE12,EIGHT 000-00-0128

> Begin with Date: T-1 \<RET\> (JAN 25, 1993) End with Date: T+2 \<RET\> (JAN 28, 1993)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Page 1

> T&L 101 OT/CT REQUESTS

> From 25-Jan-93 to 01-Feb-93

> PAIDEMPLOYEE12,EIGHT 000-00-0128

> 25-Jan-93 7 Hrs. OVERTIME on T&L 101 Approved

> MUST COMPLETE PROJECT TODAY!

> 28-Jan-93 3 Hrs. COMP TIME on T&L 101 Approved

> BEGIN SPECIAL PROJECT.

> 29-Jan-93 2 Hrs. COMP TIME on T&L 101 Requested

> TO COVER FOR EMPLOYEE THAT'S ON SL.

> 01-Feb-93 4 Hrs. OVERTIME on T&L 101 Disapproved

> SHORT OF FUNDS.

> Press RETURN to Continue. ^ \<RET\>

#### Enter OT/CT Request

This option must be used to obtain authorization for overtime and compensatory time (OT/CT). This will eliminate the need for VA Form 1098 (overtime & compensatory time request).

The timekeeper will select the employee, fill in the date that the overtime is being requested, type of time (overtime - OT or compensatory time - CT), and the number of hours needed. The system will ask under what T&L Unit the OT/CT will be worked. The timekeeper will also have to key in the justification.

When overtime or compensatory time is posted to an employee's time and attendance record, the system will check the OT/CT request file to determine if the request has been entered and the status of the request. If the request has not been entered (requested), certified by the supervisor, approved by the Director/Designee, or the total hours requested are less than the actual OT/CT hours posted, the system will view this as an errant condition and place it on the exceptions list. However, this will not stop the time and attendance record from being approved or transmitted.

> Select TimeKeeper Main Menu Option: 7 \<RET\> Enter OT/CT Requests

> Select T&L Unit: 102 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE12,NINE \<RET\> PAIDEMPLOYEE12,NINE 000-00-0029

> VA TIME & ATTENDANCE SYSTEM OVERTIME/COMP TIME REQUEST

> <u>Employee</u>: PAIDEMPLOYEE12,NINE

> <u>Requested Work Date</u>: T \<RET\> DEC 09,1992

> <u>Type of Time</u>: CT \<RET\> COMP TIME <u>Hours Requested</u>: 3 \<RET\>

> <u>T&L Worked</u>: 102

> <u>Justification</u>: Must complete project. \<RET\>

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: Exit \<RET\> INSERT Save changes before leaving form (Y/N)? Y \<RET\>

#### Cancel OT Request

This option allows the timekeeper to cancel an OC/CT request. After selecting the employee, the timekeeper specifies a date to begin searching for all such requests. That employee's requests are listed and the timekeeper selects the one to cancel. The only OC/CT requests that will be displayed for the timekeeper to cancel (with this option) are those with a status of "Requested", or approved requests with dates of today or in the future.

> Select Timekeeper Main Menu Option: 8 \<RET\> Cancel OT Request

> Select T&L Unit: 102 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE12,NINE \<RET\> 000-00-0029

> VA TIME & ATTENDANCE SYSTEM OT REQUEST

> PAIDEMPLOYEE12,NINE 000-00-0029

> Begin with Date: T// \<RET\> (DEC 09, 1992)

> 1 09-Dec-92 3 Hrs. COMP TIME on T&L 102 Requested

> Must complete project.

> Cancel Which Request \#? 1 \<RET\>

#### Daily T&L List

With this option the user is prompted to select an existing Time and Leave Unit (T&L) that he/she has been assigned, and a posting date. The names of all the employees in the T&L, their scheduled tour of duty and any tour exceptions to the scheduled tour of duty for that date are displayed.

> Select TimeKeeper Main Menu Option: 9 \<RET\> Daily T&L List

> Select T&L Unit: 101 \<RET\>

> Posting Date: T-1// \<RET\> (DEC 02, 1992)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Wed 2-Dec-92 for T&L 101

Page 1

> Employee Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------------

> PAIDEMPLOYEE,TEN 08:00A-04:30P

> PAIDEMPLOYEE13,TEN Day Off

> PAIDEMPLOYEE13,ONE 08:00A-03:30P 08:00A-03:30P SL SICK LV PAIDEMPLOYEE13,TWO 07:30A-04:00P 04:30P-08:30P OT OVERTIME PAIDEMPLOYEE11,SIX MID-08:00A

> PAIDEMPLOYEE12,NINE 09:00A-03:30P

> PAIDEMPLOYEE12,SIX 08:00A-NOON

> No Premium Pay

> 04:00P-08:00P

> No Premium Pay

> PAIDEMPLOYEE13,THREE Day Tour

> PAIDEMPLOYEE12,ONE 11:45P-MID Scheduled Overtime MID-08:00A

> Press RETURN to Continue. ^ \<RET\>

#### List Tours by T&L

With this option the user is prompted to select a particular Time and Leave Unit (T&L) or ALL T&L Units. If a particular T&L is selected, then all the tours associated with it are displayed. If ALL T&Ls are selected, then all tours of duty will be displayed along with the T&Ls associated with the tour.

> Select TimeKeeper Main Menu Option: 10 \<RET\> List Tours by T&L Select T&L Unit (or All): 101 \<RET\>

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> 3-Dec-92 T&L T O U R L I S T Page 1

> 101

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>#</p>
</blockquote></th>
<th><blockquote>
<p>Tour</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Hrs.</p>
</blockquote></th>
<th><blockquote>
<p>Segment</p>
</blockquote></th>
<th><blockquote>
<p>Special Indicator</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>65</p>
</blockquote></td>
<td><blockquote>
<p>04:30P-08:00A</p>
</blockquote></td>
<td><blockquote>
<p>SB</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>04:30P-08:00A</p>
</blockquote></td>
<td><blockquote>
<p>Standby</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>8.00</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-04:30P</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>66</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-08:00A</p>
</blockquote></td>
<td><blockquote>
<p>CB</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-08:00A</p>
</blockquote></td>
<td><blockquote>
<p>On-Call</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>148</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-04:30P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6.00</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-04:30P</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>113</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-05:00P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6.50</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-05:00P</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>151</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-05:00P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6.50</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-05:00P</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>62</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-06:00P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>8.00</p>
</blockquote></td>
<td><blockquote>
<p>10:00A-06:00P</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to Continue. ^ \<RET\>

#### Daily T&L List

With this option the user is prompted to select an existing Time and Leave Unit (T&L) that he/she has been assigned, and a posting date. The names of all the employees in the T&L, their scheduled tour of duty and any tour exceptions to the scheduled tour of duty for that date are displayed.

> Select TimeKeeper Main Menu Option: 9 \<RET\> Daily T&L List

> Select T&L Unit: 101 \<RET\>

> Posting Date: T-1// \<RET\> (DEC 02, 1992)

> Select Device: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM Wed 2-Dec-92 for T&L 101

Page 1

> Employee Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------------

> PAIDEMPLOYEE,TEN 08:00A-04:30P

> PAIDEMPLOYEE13,TEN Day Off

> PAIDEMPLOYEE13,ONE 08:00A-03:30P 08:00A-03:30P SL SICK LV PAIDEMPLOYEE13,TWO 07:30A-04:00P 04:30P-08:30P OT OVERTIME PAIDEMPLOYEE11,SIX MID-08:00A

> PAIDEMPLOYEE12,NINE 09:00A-03:30P

> PAIDEMPLOYEE12,SIX 08:00A-NOON

> No Premium Pay

> 04:00P-08:00P

> No Premium Pay

> PAIDEMPLOYEE13,THREE Day Tour

> PAIDEMPLOYEE12,ONE 11:45P-MID Scheduled Overtime MID-08:00A

> Press RETURN to Continue. ^ \<RET\>

#### Prior Pay Period Adjustments

Like Option 4 (Employee Data...), this option also has associated submenu option picks. This option will be used to make corrections to pay records processed in prior pay periods. It is what we formerly considered as corrected timecards.

> Select Timekeeper Main Menu Option: 12 \<RET\> Prior Pay Period Adjustments

> 1 Posting/Tour Change

> 2 Environmental Differential

> 3 VCS Commission Sales

#### Posting/Tour Change

This option can only be used to correct data which has already been processed through the Austin Automation Center. It will be used to cover an array of possible corrective actions. By selecting a posting date and an employee, the timekeeper can change the entire payment record for that day, post leave, remove leave that was posted in error, change the type of leave posted, pay OT, give CT, charge WOP, etc. The timekeeper MUST enter a comment at the "Corrected Time Card Remarks" prompt.

> Select Prior Pay Period Adjustments Option: 1 \<RET\> Posting/Tour Change

> Select T&L Unit: 111 \<RET\>

> Posting Date: 8/4 (AUG 04, 1994)

> Select EMPLOYEE: PAIDEMPLOYEE7,FIVE \<RET\> PAIDEMPLOYEE7,FIVE 000-00-0075

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE7,FIVE 000-00-0075

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Thu 4-Aug-94 04:00P-MID Unposted

> Shift 2

> Enter '^' to bypass this employee.

> Do you wish to change Scheduled Tour? N// N \<RET\>

> Did Employee Only Work Scheduled Tour? N \<RET\> Was Employee Absent the Entire Tour? Y \<RET\> Select TYPE OF TIME CODE: SL \<RET\> SICK LV TIME REMARKS CODE: ?? \<RET\>

> CHOOSE FROM:

> SF71 on file 1

> TIME REMARKS CODE: 1 \<RET\> SF71 on file 1

> Remarks: Caught virus.

> Corrected Time Card Remarks: Employee requested SL

> Select EMPLOYEE: PAIDEMPLOYEE7,FIVE \<RET\>

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDEMPLOYEE7,FIVE 000-00-0075

> Station: 111 Normal Hours: 80 Duty Basis: 1

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>T&amp;L:</p>
</blockquote></th>
<th><blockquote>
<p>111</p>
</blockquote></th>
<th><blockquote>
<p>Pay Plan:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Flextime:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Pay Per:</p>
</blockquote></td>
<td><blockquote>
<p>94-15</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FLSA:</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Date Scheduled Tour Tour Exceptions

> -----------------------------------------------------------------------­

> Thu 4-Aug-94 04:00P-MID 04:00P-MID SL SICK LV Shift 2 SF71 on file

> Caught virus.

> Enter '^' to bypass this employee. ^ \<RET\>

#### Environmental Differential

This option allows the user to post environmental differential time and attendance report data on an employee's time and attendance report for a prior pay period (a corrected time and attendance report). Payroll will have to manually correct the employee's pay.

> **NOTE:** When an employee is on a two-day tour and the environmental request starts on one day and ends on the next, two separate requests (one for each day) are necessary.

> Select Prior Pay Period Adjustments Option: 2 \<RET\> Environmental

> Differential

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE13,EIGHT \<RET\> PAIDEMPLOYEE13,EIGHT 000-00-0138

> VA TIME & ATTENDANCE SYSTEM ENVIRONMENTAL DIFFERENTIAL REQUEST

> <u>Employee</u>: PAIDEMPLOYEE13,EIGHT

> <u>Date</u>: 02/24/93 \<RET\> <u>From Time</u>: 08:00A \<RET\>

> <u>To Time</u>: 04:30P \<RET\>

> <u>Meal Time</u>: 30 \<RET\>

> <u>Type of Exposure</u>: HIV \<RET\>

> <u>Justification</u>: To care for patients \<RET\>

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: E \<RET\> INSERT Save changes before leaving form (Y/N)? Y \<RET\>

#### VCS Commission Sales

This option allows changes to be made to an employee's posted Veterans Canteen Service (VCS) commission sales data from a prior pay period. After selecting the T&L Unit, posting date, and employee, the previously posted VCS commission sales data for the entire pay period (containing the selected post date) will be displayed. Using the Return/Enter key and/or the up-down arrow keys to move through the screen, correct the sales amount for the proper week/day by reentering the new amount over the old amount. After all corrections have been made, exit and save the changes. Payroll must manually adjust the pieceworker's pay, after the prior pay period adjustment has been approved by both the supervisor and the OT/CT approver. The status of this adjustment can be checked by displaying the appropriate pay period (use the Display Employee Pay Period option) and checking the Status field on the Corrected T&A History (which will follow the pay period display). The status field will show either REQUESTED (entered by Timekeeper), SUPR. APPROVED (approved by supervisor), or APPROVED (approved by OT/CT Approver).

> Select Prior Pay Period Adjustments Option: 3 \<RET\> VCS Commission Sales

> Select T&L Unit: 100 \<RET\>

> Posting Date: 7/28 \<RET\> (JUL 28, 1994)

> Select EMPLOYEE: PAIDEMPLOYEE,TEN \<RET\> 000-00-0010

> VA TIME & ATTENDANCE SYSTEM VCS COMMISSION SALES

> PAIDEMPLOYEE,TEN 000-00-0010

> Sun 24-Jul-94 to Sat 6-Aug-94

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Sun</p>
</blockquote></th>
<th><blockquote>
<p>Mon</p>
</blockquote></th>
<th><blockquote>
<p>Tue</p>
</blockquote></th>
<th><blockquote>
<p>Wed</p>
</blockquote></th>
<th><blockquote>
<p>Thu</p>
</blockquote></th>
<th><blockquote>
<p>Fri</p>
</blockquote></th>
<th><blockquote>
<p>Sat</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Week 1</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p><strong>75.00</strong></p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Week 2</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> COMMAND: Press \<PF1\>H for help INSERT

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window.

> March 2018 PAID V. 4.0 User Manual 7.55

> COMMAND: E \<RET\>

> Save changes before leaving form (Y/N)? Y \<RET\>

> Corrected Time Card Remarks: Adjusted earnings for Wed - Week 1

#### Envir. Diff./VCS Sales

This option, like options 4 and 12, is a submenu option. It will be used to display, enter and cancel environmental/hazardous duty differential requests. It can be used to enter and edit VCS commission sales.

> Select TimeKeeper Main Menu Option: 13 \<RET\> Envir. Diff./VCS Sales

> 1 List Environment Diff. Requests

> 2 Envir. Diff. Request

> 3 Cancel Envir. Diff. Request

> 4 Post VCS Commission Sales

#### List Environment Diff. Requests

This option allows the user to list environmental differential or hazardous duty requests within a specified time span for one or all employees of a T&L Unit. The requests may be sorted by employee or date of request.

> **NOTE:** Environmental differential is applicable to WG employees, while hazardous duty is applicable to GS employees.

> Select Envir. Diff./VCS Sales Option: 1 \<RET\> List Environment Diff. Requests

> Select T&L Unit: 053 \<RET\>

> Select EMPLOYEE (or RETURN for all): \<RET\> Begin with Date: T \<RET\> (FEB 01, 1993) End with Date: T+27 \<RET\> (FEB 28, 1993) Sort by: (E=Employee D=Date) E// \<RET\>

> Select Device: HOME// \<RET\> ANYWHERE RIGHT MARGIN: 80// \<RET\>

> VA TIME & ATTENDANCE SYSTEM

> T&L 053 ENVIRONMENTAL DIFFERENTIAL REQUESTS

> FROM 01-Feb-93 to 28-Feb-93

> PAIDEMPLOYEE13,EIGHT 000-00-0138

> 01-Feb-93 06:00A-04:30P (Meal: 30) ASBESTOS Envir. Diff. Approved

> REMOVAL IN BASEMENT OF BLD. 50

> 19-Feb-93 06:00A-04:30P (Meal: 30) ASBESTOS Envir. Diff. Approved

> REMOVAL IN BASEMENT OF BLD. 50

> Press RETURN to Continue.

#### Envir. Diff. Request

This option allows the user to enter an environmental differential request for an employee. The date, from and to time, meal time, type of exposure, and justification must be entered. Like "Request OT/CT", this option allows the payment of environmental or hazardous duty pay. However, unlike "OT/CT Requests" option, this is a stand-alone item. An OT request is not acted upon until OT is posted. Because this option is generally associated with time within a tour of duty, this request drives the payment. It is necessary to cancel the request prior to approval if environmental differential or hazardous duty is not performed, since the request cannot be cancelled once it is approved.

> **NOTE:** When an employee is on a two-day tour and the environmental request starts on one day and ends on the next, two separate requests (one for each day) are necessary.

> Select Envir. Diff./VCS Sales Option: 2 \<RET\> Envir. Diff. Request

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE13,NINE \<RET\> 000-00-0139

> VA TIME & ATTENDANCE SYSTEM ENVIRONMENTAL DIFFERENTIAL REQUEST

> <u>Employee</u>: PAIDEMPLOYEE13,NINE

> <u>Date</u>: FEB 4, 1993 \<RET\> From Time: 08:00Am \<RET\>

> To Time: 04:30Pm \<RET\>

> <u>Meal Time</u>: 30 \<RET\>

> <u>Type of Exposure</u>: ASBESTOS \<RET\>

> <u>Justification</u>: REMOVAL FROM WALLS & CEILING \<RET\>

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window. COMMAND: Exit \<RET\> INSERT Save changes before leaving form (Y/N)? Y \<RET\>

#### Cancel Envir. Diff. Request

This option allows the user to cancel an environmental differential request - if the request has a status of "Requested". It must be executed if an employee does not perform the hazardous or environmental differential duty.

> Select Envir. Diff./VCS Sales Option: 3 \<RET\> Cancel Envir. Diff. Request

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE14,TEN \<RET\>000-00-0140 000-00-0140

> VA TIME & ATTENDANCE SYSTEM ENVIRONMENTAL DIFFERENTIAL REQUESTS

> PAIDEMPLOYEE14,T 000-00-0140

> Begin with Date: T//? \<RET\>

> Examples of Valid Dates:

> JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

> T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

> T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

> If the year is omitted, the computer assumes a date in the PAST.

> Enter a date which is less than or equal to JAN 21, 1993. Begin with Date: T// \<RET\> (JAN 21, 1993)

> 21-Jan-93 06:00A-04:30P (Meal: 30) ASBESTOS Envir. Diff. Requested

> REMOVAL IN BASEMENT OF BLD. 50

> 27-Jan-93 06:00A-04:30P (Meal: 30) ASBESTOS Envir. Diff. Requested

> REMOVAL IN BASEMENT OF BLD. 50

> Cancel Which Request \#? 1 \<RET\>

#### Post VCS Commission Sales

This option allows the user to enter the dollar and cents amounts of commission sales for Veterans Canteen Service pieceworkers. After selecting the T&L Unit, posting date, and employee, the VCS commission sales data for the entire pay period (containing the selected posting date) will be displayed. Using the return/enter key and/or the up/down arrow keys to move through the screen, enter the sales amount for the proper week/day. Days which have no sales amount may be left blank or 0 (zero) can be entered. After all amounts have been entered, exit and save the changes. Changes can be made to these amounts until the employee's time and attendance (T&A) record has been approved by the supervisor and released to Payroll. Payroll can return the T&A record to the timekeeper if additional changes are required but the supervisor will need to approve the T&A record again to release it back to Payroll. Once the employee's T&A record has been transmitted to the Austin Automation Center (AAC), corrections and/or changes to VCS sales must be done through the Prior Pay Period Adjustments option.

> Select Envir. Diff./VCS Sales Option: 4 \<RET\> Post VCS Commission Sales

> Select T&L Unit: 100 \<RET\>

> Posting Date: T-1// \<RET\> (FEB 20, 1993)

> Select Employee: PAIDEMPLOYEE14,ONE \<RET\> 000-00-0142

> VA TIME & ATTENDANCE SYSTEM VCS COMMISSION SALES

> PAIDEMPLOYEE14,ONE 000-00-0142

> Sun 7-Feb-93 to Sat 20-Feb-93

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Sun</p>
</blockquote></th>
<th><blockquote>
<p>Mon</p>
</blockquote></th>
<th><blockquote>
<p>Tue</p>
</blockquote></th>
<th><blockquote>
<p>Wed</p>
</blockquote></th>
<th><blockquote>
<p>Thu</p>
</blockquote></th>
<th><blockquote>
<p>Fri</p>
</blockquote></th>
<th><blockquote>
<p>Sat</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Week 1</p>
</blockquote></td>
<td><blockquote>
<p><strong>50.00</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>76.35</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>23.10</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>15.46</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>10.11</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>0.00</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>0.00</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Week 2</p>
</blockquote></td>
<td><blockquote>
<p><strong>89.98</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>25.00</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>23.00</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>14.76</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>999.99</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>0.00</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>0.00</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> COMMAND: Press \<PF1\>H for help INSERT

> Exit Save Refresh

> Enter a command or '^CAPTION' to jump to a field in the current window.

> COMMAND: E \<RET\>

> Save changes before leaving form (Y/N)? Y \<RET\>

#### List Un-Certified Employees

This allows the user to list the time and attendance reports for the current pay period by selecting a specific T&L. It shows the employees that have not been released to Payroll, as well as supervisors that are on this T&L but are certified by another T&L. Similar to this option is "Un-Transmitted Employees - All T&Ls" which lists the untransmitted employees of a particular T&L or all T&Ls, and shows whether or not they have been released to Payroll.

> Select Timekeeper Main Menu Option: 14 \<RET\> List Un-Certified Employees

> VA TIME & ATTENDANCE SYSTEM Page 1

> UN-CERTIFIED EMPLOYEES

> Select T&L Unit: 902 \<RET\>

> 902 INFORMATION SERVICES CENTER Sun 4-Apr-93 to Sat 17-Apr-93

> 000-00-0043 PAIDEMPLOYEE4,THREE

> 000-00-0044 PAIDEMPLOYEE4,FOUR

> 000-00-0045 PAIDEMPLOYEE4,FIVE

> 000-00-0046 PAIDEMPLOYEE4,SIX

> 000-00-0047 PAIDEMPLOYEE4,SEVEN

> 000-00-0048 PAIDEMPLOYEE4,EIGHT

> 000-00-0049 PAIDEMPLOYEE4,NINE

> 000-00-0050 PAIDEMPLOYEE5,TEN

> 000-00-0051 PAIDEMPLOYEE5,ONE

> 000-00-0052 PAIDEMPLOYEE5,TWO

#### Edit OT/CT Request

This option allows the user to edit OT/CT requests that are not yet posted. Below, the number of hours requested have been changed.

> Select TimeKeeper Main Menu Option: 15 \<RET\> Edit OT/CT Request

> Select T&L Unit: 100 \<RET\>

> Select EMPLOYEE: PAIDEMPLOYEE14,TWO \<RET\> PAIDEMPLOYEE14,TWO 000-00-0142

> VA TIME & ATTENDANCE SYSTEM OT/CT REQUESTS

> PAIDEMPLOYEE14,TWO 000-00-0142

> Begin with Date: T//1/1/95 \<RET\> (JAN 01, 1995)

> 1 25-Jul-95 4 Hrs. OVERTIME (\$78.36) on T&L 100 Supr. App.

> NEEED MONEY

> 2 28-Jul-95 3 Hrs. COMP TIME on T&L 100 Requested

> LOVE TO WORK.

> Edit Which Request \#? 2 \<RET\>

> VA TIME & ATTENDANCE SYSTEM OVERTIME/COMP TIME REQUEST

> Employee: PAIDEMPLOYEE14,TWO

> Requested Work Date: JUL 28,1995

> Type of Time: COMP TIME Hours Requested: 4 \<RET\> T&L Worked 100

> Justification: LOVE TO WORK. Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field. COMMAND: E \<RET\>

> Save changes before leaving form (Y/N)? Y \<RET\>

## Chapter 8. Employee Inquiry/Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the Human Resources Management (HRM) user to access a menu of employee inquiry options.

List and Display screens are provided to assist the user in the proper maintenance of employee attendance data. These screens can be used to review posted information, check schedules, leave balances, leave requests, overtime/compensatory time requests and status, etc.

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Print Employee Entries</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Search Employee Entries</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Ad Hoc Report Generator...</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Employee Inquiry</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Update PAID Codes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Cost Center/Organization file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Compile/Print Strength Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Print Strength Report</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Print Employee Entries

This option will allow the HRM user to invoke the FileMan PRINT FILE ENTRIES option for the PAID EMPLOYEE (#450) file.

> Select Employee Inquiry/Reports Menu Option: 1 \<RET\> Print Employee Entries

Data for this option will not be repeated here, but can be found under the Payroll Main Menu - Employee Inquiry Menu (submenu) - Print Employee Entries.

#### Search Employee Entries

This option will allow the HRM user to invoke the FileMan SEARCH FILE ENTRIES option for the PAID EMPLOYEE (#450) file.

> Select Employee Inquiry/Reports Menu Option: 2 \<RET\> Search Employee Entries

Data for this option will not be repeated here, but can be found under the Payroll Main Menu - Employee Inquiry Menu (submenu) - Search Employee Entries.

#### Ad Hoc Report Generator

This option allows the HRM user to generate ad hoc reports using basic employee fields, Title 38 employee fields, physician and dentist fields, and follow-up codes.

> Select Employee Inquiry/Reports Menu Option: 3 \<RET\> Ad Hoc Report

> Generator

> Select one of the following:

> 1 Basic Employee Fields

> 2 Title 38 Employee Fields

> 3 Physician & Dentist Fields

> 4 Followup Code Fields

#### Basic Employee Fields

This option allows the HRM user to print data from different employee fields for the ad hoc report. Four fields may be chosen. An asterisk appears by each field that has been selected to print.

> Select Ad Hoc Report Category: 1 \<RET\> Basic Employee Fields

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Enter RETURN to continue or '^' to exit: \<RET\>

> Sort selection \# 1 : ?? \<RET\>

> Select the major data element to sort by. Maximum of 4 sort fields allowed.

> Enter numeric 1 to 42, \<RETURN\> to end, ^ to exit. \<RET\>

> Sort selection \# 1 : 1 \<RET\> Employee Name

> Sort from: BEGINNING// \<RET\>

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Sort selection \# 2 : 19 \<RET\> Grade

> Sort from: BEGINNING//

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Sort selection \# 3 : 8 \<RET\> Sex

> Sort from: BEGINNING//

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Sort selection \# 4 : 28 \<RET\> TSP Status

> Sort from: BEGINNING//

> Maximum of 4 sort fields reached.

> =========== Basic Employee Fields Ad Hoc Report Generator =========== Print selection \# 1 : 1 \<RET\> Employee Name

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Print selection \# 2 : 19 \<RET\> Grade

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Print selection \# 3 : 8 \<RET\> Sex

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Print selection \# 4 : 28 \<RET\> TSP Status

> =========== Basic Employee Fields Ad Hoc Report Generator ===========

> Enter RETURN to continue or '^' to exit: Print selection \# 5 : \<RET\>

> Include separated employees? No// \<RET\> (No) Separated employees will not be included.

> Enter special report header, if desired (maximum of 60 characters). DEVICE: HYPER SPACE \<RET\> RIGHT MARGIN: 80// \<RET\>

> PAID EMPLOYEE SEARCH AUG 7,1995 14:25 PAGE 1

> Employee Name Grade Sex

> TSP Status

> ------------------------------------------------------------------------------

> PAIDEMPLOYEE14,THREE 08 FEMALE YES

> PAIDEMPLOYEE14,FOUR 07 MALE YES

> PAIDEMPLOYEE14,FIVE 09 MALE ELIGIBLE

> PAIDEMPLOYEE14,SIX 09 FEMALE YES

> PAIDEMPLOYEE14,SEVEN 10 MALE ELIGIBLE

> PAIDEMPLOYEE14,EIGHT 14 FEMALE INELIGIBLE

> PAIDEMPLOYEE14,NINE 09 FEMALE YES

#### Title 38 Employee Fields

This option allows the HRM user to print data from Title 38 employee fields for the ad hoc report. An asterisk appears by each field that has been selected to print.

Data from this option can be accessed by following the same steps as in the previous option, "Basic Employee Fields". Choose "Sort Selection," then select "Print Selection," and press \<RET\> to print list.

> Select Ad Hoc Report Category: 2 \<RET\> Title 38 Employee Fields

#### Physician & Dentist Fields

This option allows the HRM user to print data from physician and dentist fields for the ad hoc report. An asterisk appears by each field that has been selected to print.

Data from this option can be accessed by following the same steps as in the option, "Basic Employee Fields". Choose "Sort Selection," then select "Print Selection," and press \<RET\> to print list.

> Select Ad Hoc Report Category: 3 \<RET\> Physician & Dentist Fields

#### Followup Code Fields

This option allows the HRM user to print data from follow-up code fields for the ad hoc report. An asterisk appears by each field that has been selected to print.

Data from this option can be accessed by following the same steps as in the option, "Basic Employee Fields". Choose "Sort Selection," then select "Print Selection," and press \<RET\> to print list.

> Select Ad Hoc Report Category: 4 \<RET\> Followup Code Fields Fields

#### Employee Inquiry

This option will allow designated HRM employees to view designated PAID EMPLOYEE (#450) file data.

> Select Employee Inquiry/Reports Menu Option: 3 \<RET\> Employee Inquiry

Data for this option will not be repeated here, but can be found under the Payroll Main Menu - Employee Inquiry Menu (submenu) - Employee Inquiry.

#### Update PAID Codes

This option will allow the user to enter, edit or delete PAID codes and their descriptions from the PAID CODE FILES (#454).

> Select Employee Inquiry/Reports Menu Option: 4 \<RET\> Update PAID Codes

Data for this option will not be repeated here, but can be found under the Payroll Main Menu - Employee Inquiry Menu (submenu) - Update PAID Codes.

#### Enter/Edit Cost Center/Organization file

This option allows the user to enter/edit data in the PAID COST CENTER/ ORGANIZATION file (#454.1).

> Select Employee Inquiry/Reports Menu Option: 5 \<RET\> Enter/Edit Cost

> Center/Organization file

> Select PAID COST CENTER/ORGANIZATION NAME: ?? \<RET\>

> CHOOSE FROM:

> ACQUISITION & MATERIEL MANAGEM

> AMBULATORY CARE

> ANESTHESIOLOGY

> AUDIOLOGY/SPEECH PATHOLOGY

> BLIND REHAB

> BUILDING MANAGEMENT

> CANTEEN

> CHAPLAIN

> CHIEF OF STAFF

> DENTAL

> DERMATOLOGY

> DIETETICS

> DIRECTOR

> DOMICILIARY

> EDUCATION

> ENGINEERING

> FISCAL

> IRM

> ISC

> LABORATORY

> LIBRARY

> '^' TO STOP: ^ \<RET\>

> Select PAID COST CENTER/ORGANIZATION NAME: BLIND REHAB \<RET\>

> NAME: BLIND REHAB// \<RET\>

> MED CARE APPROPRIATED (Y/N?): YES// \<RET\>

> FTE CEILING: \<RET\>

> FTE MD CEILING: \<RET\>

> FTE RN CEILING: \<RET\>

> FTE LPN CEILING: \<RET\>

> FTE NA CEILING: \<RET\>

> Select PAID COST CENTER/ORGANIZATION NAME: \<RET\>

#### Compile/Print Strength Report

The strength report is a listing by service of counts and Full Time Equivalent (FTE) totals for various employee categories. These categories are:

> FTP Full Time Permanent PTP Part Time Permanent PTPFTE Part Time Permanent FTE FTT Full Time Temporary

> PTT Part Time Temporary PTTFTE Part Time Temporary FTE INT Intermittent

> SIS Stay-in-School/Summer Aid

> INTFTE Intermittent FTE

> SISFTE Stay-in-School/Summer Aid FTE TSR Trainees/Stipends/Residents TSRFTE Trainees/Stipends/Residents FTE LWOP Extended LWOP

> The strength report utilizes four options on the Employee Inquiry Menu:

> 4 Update PAID Codes

> 5 Enter/Edit Cost Center/Organization file

> 6 Compile/Print Strength Report

> 7 Print Strength Report

The use of these options requires the PRSD PAID CODES key. If the user requires these menu options, please request this key from your IRM representative.

In order to produce a strength report the user must first compile the strength report statistics. This can be done by means of the "Compile/Print Strength Report" option. Each time this option is run the strength report statistics will be recalculated. Compiling the strength report should take approximately five minutes. If you wish to run this job at a later time you may queue the job for later processing. When selecting a device be sure to request a right margin of at least 132. This report is not designed to be displayed on an 80-column screen. Reprints or additional copies of a compiled report can be obtained by means of the "Print Strength Report" option.

> Select Employee Inquiry/Reports Menu Option: 6 \<RET\> Compile/Print Strength

> Report

> Do you wish to queue this job? ?? \<RET\>

> Answer 'Y' if you wish this job to be run as a background job. Answer 'N' if you wish this job to be run interactively.

> Do you wish to queue this job? N \<RET\> (NO)........................ DEVICE: DEV-LASER(16)-LAND-132 \<RET\> DEVELOPMENT AREA - LANDSCAPING-132

> RIGHT MARGIN: 132// \<RET\>

> DO YOU WANT YOUR OUTPUT QUEUED? NO// Y \<RET\> (YES)

> Requested Start Time: NOW// \<RET\> (JUN 21, 1993@14:42) Request Queued!

> STRENGTH REPORT FOR PAIDEDSPONSOR,ONE COMPILATION DATE: OCT 25, 1994@08:03

> PAGE: 1 PRINT DATE: JUN 21, 1994@08:03

> SISFTE

> SERVICE CEILING FTP PTP PTPFTE FTT PTT PTTFTE INT SIS INTFTE TOT FTETOT VAR TSR TSRFTE LWOP

> NAME

> ---------------------------------------------------------------------------------------------

> ---------------------------------------------------------------------------------------------

> AMBULA­

> TORY CARE15.00 10 8 4.15 0 0 0.00 0 0 0.00 18 14.15 -0.85 0 0.00 0

> --------------------------------------------------------------------------------------------- ANESTHE­

> SIOLOGY

5.90

6 3 0.75

0 1 0.25 0

0 0.00 10

7.00

1.10 8

4.00 0

> --------------------------------------------------------------------------------------------- BLIND

> REHAB

1.00

1 0 0.00

0 0 0.00 0

0 0.00

1 1.00

0.00 1

0.50 0

> --------------------------------------------------------------------------------------------- CHIEF OF

> STAFF

6.00

2 2 1.76

0 0 0.00 0

0 0.00

4 3.76 -2.24 0

0.00 0

> ---------------------------------------------------------------------------------------------

> DENTAL

10.20

7 4 2.08

0 1 0.40 0

0 0.00 12

9.48 -0.72 6

3.00 0

> --------------------------------------------------------------------------------------------- EXTENDED

> CARE

7.70

2 7 3.71

0 1 0.63 0

0 0.00 10

6.34 -1.36 1

0.50 0

> ---------------------------------------------------------------------------------------------

> LAB

8.80

7 5 1.15

0 1 0.50 0

0 0.00 13

8.65 -0.15 6

3.00 0

> ---------------------------------------------------------------------------------------------

> MEDICAL

49.00

19 58

26.83

0 5 1.76 0

0 0.00

82 47.59 -1.41 88

44.00 0

> ---------------------------------------------------------------------------------------------

> MISC

0.00

1 0 0.00

0 0 0.00 0

0 0.00

1 1.00

1.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> NEUROLOGY 8.00

4 4 2.38

0 0 0.00 0

0 0.00

8 6.38 -1.62 9

4.50 0

> ---------------------------------------------------------------------------------------------

> NUCL MED

5.00

2 2 1.63

0 0 0.00 0

0 0.00

4 3.63 -1.37 2

1.00 0

> --------------------------------------------------------------------------------------------- OFFICE OF

> DIRECTOR

2.00

2 0 0.00

0 0 0.00 0

0 0.00

2 2.00

0.00 0

0.00 0

> --------------------------------------------------------------------------------------------- PHYCHIA­

> TRY

23.00

15 11

6.51

1 2 1.26 0

0 0.00

29 23.77

0.77 11

5.50 0

> ---------------------------------------------------------------------------------------------

> RADIOLOGY15.00 11 2

0.50

0 1 0.13 0

0 0.00

14 11.63 -3.37 1

0.50 0

> ---------------------------------------------------------------------------------------------

> REHAB MED 9.00

7 2 1.51

0 0 0.00 0

0 0.00

9 8.51 -0.49 7

3.50 0

> --------------------------------------------------------------------------------------------- SPINAL

> CORD INJ

6.00

5 0 0.00

1 0 0.00 0

0 0.00

6 6.00

0.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> SURGERY

19.40

1 41

18.26

0 5 2.52 0

0 0.00

47 21.78

2.38 45

22.50 0

> --------------------------------------------------------------------------------------------- TRAINING/

> CONT ED

1.00

1 0 0.00

0 0 0.00 0

0 0.00

1 1.00

0.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> ---------------------------------------------------------------------------------------------

> TOTAL 192.00 103 149

71.22

2 17

7.45 0

0 0.00 271 183.67 -8.33 185

92.50 0

> ---------------------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 37%" />
<col style="width: 17%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FTP</p>
</blockquote></th>
<th><blockquote>
<p>Full Time Permanent</p>
</blockquote></th>
<th><blockquote>
<p>SIS</p>
</blockquote></th>
<th><blockquote>
<p>Stay-in-School/Summer Aid</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PTP</p>
</blockquote></td>
<td><blockquote>
<p>Part Time Permanent</p>
</blockquote></td>
<td><blockquote>
<p>VAR</p>
</blockquote></td>
<td><blockquote>
<p>Variance (FTETOT-CEILING)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FTT</p>
</blockquote></td>
<td><blockquote>
<p>Full Time Temporary</p>
</blockquote></td>
<td><blockquote>
<p>TSR</p>
</blockquote></td>
<td><blockquote>
<p>Trainee/Stipend/Resident</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PTT</p>
</blockquote></td>
<td><blockquote>
<p>Part Time Temporary</p>
</blockquote></td>
<td><blockquote>
<p>LWOP</p>
</blockquote></td>
<td><blockquote>
<p>Extended Leave Without Pay</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INT</p>
</blockquote></td>
<td><blockquote>
<p>Intermittent</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> The following Cost Center/Organization codes are not associated with a service name and are being counted under the service name MISCELLANEOUS. They can be assigned a service name via the Update PAID Codes option by choosing the COST CENTER/ ORGANIZATION file, entering the CODE and entering a DESCRIPTION. You must then recompile the report via the Compile/Print

> Strength Report option. These codes will then be counted under the appropriate service name.

> 8017:0720

> 8045:1018

> PHYSICIAN STRENGTH REPORT FOR PAIDEDSPONSOR,ONE COMPILATION DATE: OCT 14, 1994@08:03

> PAGE: 2 PRINT DATE: OCT 14, 1994@08:03

> SISFTE

> SERVICE CEILING FTP PTP PTPFTE FTT PTT PTTFTE INT SIS INTFTE TOT FTETOT VAR TSR TSRFTE LWOP

> NAME

> ---------------------------------------------------------------------------------------------

> ---------------------------------------------------------------------------------------------

> MEDICAL

0.00

5 1 0.00

0 0 0.00 0

0 0.00

6 0.00

0.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> MISC

0.00

1 0 0.00

0 0 0.00 0

0 0.00

1 0.00

0.00 1

0.00 0

> ---------------------------------------------------------------------------------------------

> NURSING

10.00

3 0 0.00

0 0 0.00 0

0 0.00

3 0.00-10.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> PERSONNEL 0.00

1 0 0.00

0 0 0.00 0

0 0.00

1 0.00

0.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> REHAB MED 0.00

1 0 0.00

0 0 0.00 0

0 0.00

1 0.00

0.00 0

0.00 0

> ---------------------------------------------------------------------------------------------

> ---------------------------------------------------------------------------------------------

> TOTAL 10.00 11 1

0.00

0 0 0.00 0

0 0.00 12

0.00-10.00 1

0.00 0

> ---------------------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 36%" />
<col style="width: 18%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FTP</p>
</blockquote></th>
<th><blockquote>
<p>Full Time Permanent</p>
</blockquote></th>
<th><blockquote>
<p>SIS</p>
</blockquote></th>
<th><blockquote>
<p>Stay-in-School/Summer Aid</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PTP</p>
</blockquote></td>
<td><blockquote>
<p>Part Time Permanent</p>
</blockquote></td>
<td><blockquote>
<p>VAR</p>
</blockquote></td>
<td><blockquote>
<p>Variance (FTETOT-CEILING)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FTT</p>
</blockquote></td>
<td><blockquote>
<p>Full Time Temporary</p>
</blockquote></td>
<td><blockquote>
<p>TSR</p>
</blockquote></td>
<td><blockquote>
<p>Trainee/Stipend/Resident</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PTT</p>
</blockquote></td>
<td><blockquote>
<p>Part Time Temporary</p>
</blockquote></td>
<td><blockquote>
<p>LWOP</p>
</blockquote></td>
<td><blockquote>
<p>Extended Leave Without Pay</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INT</p>
</blockquote></td>
<td><blockquote>
<p>Intermittent</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> The following Cost Center/Organization codes are not associated with a service name and are being counted under the service name MISCELLANEOUS. They can be assigned a service name via the Update PAID Codes option by choosing the COST CENTER/ ORGANIZATION file, entering the CODE and entering a DESCRIPTION. You must then recompile the report via the Compile/Print

> Strength Report option. These codes will then be counted under the appropriate service name.

> 1101:0000

> 1101:1000

> 1200:0000

The service in which an employee is counted is based upon the employee's Cost Center/Organization (field \#458 in the PAID Employee file). The station's Cost Center/Organizational codes can be found via the "Update PAID Codes" option by selecting the "Cost Center/Organization" file. Each Cost Center/Organizational code should be associated with a service name or description. If the Cost Center/Organizational code does not have a description you may add one by selecting from the description list. The user may also change a code's description if it is to be associated with a different name.

1\) Naming a Cost Center/Organization

Any Cost Center/Organizations which appear on your listing as codes and not as names should be named. This can be done by doing the following:

> Select Employee Inquiry Reports Menu Option: 4 \<RET\> Update PAID Codes

> Select FILE: 94 \<RET\> COST CENTER/ORGANIZATION

> Select COST CENTER/ORGANIZATION CODE: 1200:3000 \<RET\>

> CODE: 1200:3000// \<RET\>

> DESCRIPTION: PAIDORG \<RET\>

> **NOTE:** More than one code may be associated with the same description.

If the preferred description is not in the description list, the user may enter a new description or edit an existing one by means of the Enter/Edit Cost Center/Organization file option. Once the user has named all of the Cost Center/Organizations the "Miscellaneous" service should not appear on the strength report.

2\) FTE Service Ceilings

Service ceilings can be added by means of the Enter/Edit Cost Center/Organization file option. The user may also add physicians' ceilings for those services which contain physicians. The Nursing Service may also have individual ceilings for RNs, LPNs and NAs. The service variance will be computed as TOTAL FTE - FTE CEILING.

3\) Customizing Your Strength Report

The strength report is designed to provide you with some flexibility in determining where your employees are counted. The strength report is divided into two sections: medical care appropriated services and medical care non-appropriated services. The user may determine where a service is counted by means of the Enter/Edit Cost Center/Organization file option by answering the question "MED CARE APPROPRIATED (Y/N?)". Medical care appropriated services will be listed first followed by medical care non-appropriated services.

If a particular Cost Center/Organizational code is not associated with the correct name (e.g., some stations may want certain codes to be counted under Chief of Staff while other stations may want the same codes to be counted under MAS), the user may change the service associated with a Cost Center/Organizational code by means of the "Update PAID Codes" option. (See example under "1" above.) By changing the DESCRIPTION of a Cost Center/Organization and recompiling the statistics, all of the employees with that code will now be counted under the new DESCRIPTION.

STRENGTH REPORT TROUBLESHOOTING

Problem: Ceiling values equal zero.

Cause: No ceiling values in the Cost Center/Organization file.

Solution: Enter the ceiling values via the Enter/Edit Cost Center/Organization file option, under Employee Inquiry Menu.

Problem: "Miscellaneous" service appears on strength report.

Cause: Cost Center/Organization codes are not associated with a service name.

Solution: Determine which Cost Center/Organization codes require names by printing a Cost Center/Organization list. Enter the Cost Center/Organization DESCRIPTION via the Update PAID Codes option, under Employee Inquiry Menu.

Problem: Strength report totals inaccurately.

Cause: Cost Center/Organization codes are associated with the wrong service name.

Solution: Enter the correct Cost Center/Organization DESCRIPTION via the

Update PAID Codes option under Employee Inquiry Menu.

Problem: Service does not appear on strength report.

Cause: No employee has this Cost Center/Organization code in their record

OR

Cost Center/Organization code is not associated with a service name

OR

The "MED CARE APPROPRIATED (Y/N?)" field has not been answered.

Solution: Enter the Cost Center/Organization DESCRIPTION via the Update PAID Codes option under Employee Inquiry Menu. Be sure that the "MED CARE APPROPRIATED (Y/N?)" field has been answered.

#### Print Strength Report

This option only prints the strength statistics of the PAID employee files, whereas the preceding option, "Compile/Print Strength Report", compiles AND prints the statistics. (After the strength statistics have been compiled, the "Print Strength Report" option may be used for printing at a later time.)

> Select Employee Inquiry/Reports Menu Option: 7 \<RET\> Print Strength Report

> DEVICE: DEV-LASER(16)-LAND-132 \<RET\> DEVELOPMENT AREA - LANDSCAPING-132

> RIGHT MARGIN: 132// \<RET\>

> DO YOU WANT YOUR OUTPUT QUEUED? NO// Y \<RET\> (YES)

> Requested Start Time: NOW// \<RET\> (JUN 21, 1993@14:42) Request Queued!

To view Strength Report, see option 6, Compile/Print Strength Report (Employee Inquiry Menu).

#### Review FY Recess for 9 Month AWS Employee

This view only option displays the Recess Schedule for nurses on the 9 month/3 month alternate work schedule (AWS). To view a 9 month/3 month AWS Recess Schedule, enter the fiscal year or the nurse’s name.

Once the schedule is selected, you may enter actions at the “Select Action” prompt to navigate through the Recess Schedule, print the Recess Schedule and display a summary. Enter a double question mark (??) at this prompt for a list of all available actions.

Following is a list of actions with a brief description. The mnemonic for each action is shown in brackets \[ \] following the action name. Entering the mnemonic is the quickest way to select an action.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Recess Hours Summary</p>
<p>[RS]</p></td>
<td><p>Enter RS to see a summary screen with recess totals. Be sure to scroll down to see the whole</p>
<p>report.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Next Screen [+]</td>
<td>Move to the next screen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Previous Screen [-]</td>
<td>Move to the previous screen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Up a Line [UP]</td>
<td>Move up one line.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Down a Line [DN]</td>
<td>Move down one line.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Shift View to Right [&gt;]</td>
<td>Move the screen to the right if the screen width is more than 80 characters.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Shift View to Left [&lt;]</td>
<td>Move the screen to the left if the screen width is more than 80 characters.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>First Screen [FS]</td>
<td>Move to the first screen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Last Screen [LS]</td>
<td>Move to the last screen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Go to Page [GO]</td>
<td>Move to any selected page in the list.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Re Display Screen [RD]</td>
<td>Redisplay the current screen.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Print Screen [PS]</td>
<td>Print the header and the portion of the list</td>
</tr>
</tbody>
</table>

|                               | currently displayed.                                                    |
|-------------------------------|-------------------------------------------------------------------------|
|                               |                                                                         |
| Print List \[PL\]             | Print the list of entries currently displayed.                          |
|                               |                                                                         |
| Search List \[SL\]            | Find selected text in list of entries.                                  |
|                               |                                                                         |
| Auto Display(On/Off) \[ADPL\] | Toggle the menu of actions to be displayed/not displayed automatically. |
|                               |                                                                         |
| Quit \[QU\]                   | Exit the screen.                                                        |

> Select Employee Inquiry/Reports Menu Option: Review FY Recess for 9 Month AWS Employee

> Select 9-month AWS Nurse: 2007

> 1 2007 PAIDemployee,One 2007 000-01-4309

> 2 2007 PAIDemployee,Two 2007 000-01-3045

> 3 2007 PAIDemployee,Three 2007 000-01-2715

> 4 2007 PAIDemployee,Four 2007 000-01-4274

> 5 2007 PAIDemployee,Five 2007 000-01-4275

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 1 PAIDemployee,One 2007 000-01-4309

> Recess Schedule Viewer Jul 17, 2007@14:43:45 Page: 1 of 4

> FY2007 Recess Week Viewer for 9 month AWS with start date 10/01/06 (pp 06-20)

> PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> +Week---PayPd-Sun Mon Tue Wed Thu Fri Sat-Recess: Scheduled--Certified---------

> =============Nov 2006============

> 6 5 6 7 8 9 10 11 8.00

> 7 06-23 12 13 14 15 16 17 18 10.50

> 8 19 20 21 22 23 24 25 40.25

> 9 06-24 26 27 28 29 30 1 2 24.75

> =============Dec 2006============

> 10 3 4 5 6 7 8 9 40.00

> 11 06-25 10 11 12 13 14 15 16 56.00

> 12 17 18 19 20 21 22 23 36.50

> 13 06-26 24 25 26 27 28 29 30 36.00

> 14 31 1 2 3 4 5 6 36.00

> =============Jan 2007============

> 15 07-01 7 8 9 10 11 12 13 36.00

> 16 14 15 16 17 18 19 20 36.00

> 17 07-02 21 22 23 24 25 26 27 36.00

> 18 28 29 30 31 1 2 3 36.00

> =============Feb 2007============

> +---------Enter ?? for more actions-------------------------------------------- RS Recess Hours Summary

> Select Action:Next Screen// rs Recess Hours Summary

> RECESS SCHEDULE SUMMARY Jul 17, 2007@14:44:16 Page: 1 of 2

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> --Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------

> 6 11/05/06 8.00 0.00

> 7 11/12/06 10.50 0.00

> 8 11/19/06 40.25 0.00

> 9 11/26/06 24.75 0.00

> 10 12/03/06 40.00 0.00

> 11 12/10/06 56.00 0.00

> 12 12/17/06 36.50 0.00

> 13 12/24/06 36.00 0.00

> 14 12/31/06 36.00 0.00

> 15 01/07/07 36.00 0.00

> 16 01/14/07 36.00 0.00

> 17 01/21/07 36.00 0.00

> 18 01/28/07 36.00 0.00

> 19 02/04/07 36.00 0.00

> 20 02/11/07 3.50 0.00

> ====== ======

> +---------WARNING--Recess hours are under scheduled: 68.50--------------------

> Select Action:Next Screen// \<RET\> NEXT SCREEN

> RECESS SCHEDULE SUMMARY Jul 17, 2007@14:45:09 Page: 2 of 2

> 9 Mo. AWS Recess Summary for FY2007 AWS Start Date: 10/01/06 (pp 06-20) PAIDemployee,One XXX-XX-4309 T&L Unit: 221

> +-Week-Begin Date------Sched Recess Hrs----TimeCard Certified------------------ Total Recess. Scheduled: 471.50 Posted: 0.00

> Total Weeks in AWS FY Schedule: 54.00

> Total available FY recess hrs: 540.00 (13.5 weeks) WARNING--Recess hours under scheduled: 68.50

> ----------Enter ?? for more actions-------------------------------------------- Select Action:Quit//

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AAC
> Access Code
> AL AN AU
> Biweekly
> CD
> Data Dictionary
> DHCP Download
> Edit & Update
> Exception Report
> Field
> Initial
> MailMan Menu Option OT/CT
Austin Automation Center
A unique sequence of characters assigned to the user by the System Manager. The access code (in conjunction with the verify code) is used by the computer to identify authorized users, and should not be revealed to any other person.
Total amount of Annual Leave for week TWO of the pay period.
Total amount of Annual Leave for week ONE of the pay period.
Total amount of Authorized Absence for week ONE of the pay period.
Two consecutive calendar weeks. Control Data field.
A description of the file structure and data elements within a file.
Decentralized Hospital Computer Program.
Used here to refer to data generated by the AAC and sent via
MailMan to the station.
A type of download used to update an employee's master record data in the PAID EMPLOYEE file (#450).
A report sent to the VA facilities by AAC that lists rejected
8B Record data.
A data element in a file.
A type of download used to populate the PAID EMPLOYEE
file (#450) with master record data.
The Department of Veterans Affairs electronic mail system. A set of options available to users to perform related tasks.
A selection from a menu that performs a task. Overtime or Compensatory time.
> Package Payroll Clerk Payrun
> RET Separation
> SF 71
> Software
> SSN T&A T&L
> Timekeeper
> Transfer
> Transmit
> User
> VA Form 4-5631
> Verification
A set of MUMPS routines, files, documentation and installation procedures that support a specific function within DHCP.
Employee of Fiscal Service, Payroll Section who is responsible for uniformity in the correct preparation and maintenance of time and attendance reports.
A type of download containing accounting data used to update the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.
RETURN or ENTER key on a terminal keyGROUP.
A type of download used to mark an employee's entry in the PAID EMPLOYEE (#450) file as a separation (i.e., no longer an active employee at that station).
Application for Leave, Standard Form 71.
A generic term referring to a related set of computer programs.
Social Security Number. Time and Attendance. Time and Leave Unit.
Responsible for the preparation, maintenance, and timely submission of time and attendance reports for each affected employee whose record has been assigned to their
jurisdiction.
A type of download used to create an entry into the PAID EMPLOYEE (#450) file for an employee transferring into the station from another station.
A process in which data is sent from one computer to another.
A person who enters, edits, and/or retrieves data from a system.
The TIME AND ATTENDANCE REPORT (i.e., timecard). To check the accuracy or to confirm the input entry of
known data.
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Verify Code</p>
</blockquote></th>
<th><blockquote>
<p>A unique security code which serves as a second level of security access. The user may change this code.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8B Record</p>
</blockquote></td>
<td><blockquote>
<p>Employee information pertinent to the generation of biweekly payroll checks.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Section 2. Education Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This module creates an Educational Tracking database which features the identification of educational programs and inservice training, allows the crediting of attendance at these educational offerings, and generates multiple reports.

The information associated with each class may include:

- Program or class name
- Supplier/presenter
- Type of media used in the presentation
- Location of training
- Purpose of training
- Category of program/class
- Type of training (mandatory inservice, continuing education, etc.)
- Mandatory review group (if a required class)
- Financial agency and cost
- Accreditation GROUP (for continuing education)
- Employer or student expense

The database information is used to complete VA FORM 5-4691 and to manually transmit data to the Austin Automation Center (AAC). The data tracked for this purpose includes: whether the training is financed by the government or the employee, the purpose or reason the employee received the training, whether the training was given by a federal agency or commercial vendor, the number of on- duty and off-duty hours of training, the length of the program or class, direct cost (e.g., tuition, books, supplies), indirect cost (e.g., transportation, lodging, and subsistence), the program category (information about the specific kind of training), program or class title, employee cost, the contact hours (the actual hours spent in class-calculate as on-duty and off duty hours) and whether the training was routine or non-routine.

The education tracking options provide on-line registration, class calendars, registration rosters, and record tracking of all programs or classes that an employee or student has taken. This employee record can be transferred from site to site.

The menu options provide the opportunity to enter a program or class with multiple attendees, saving input time and keyGROUP interaction. The main menu for this application is PRSE-SYS-MGR.

## Chapter 1. Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are several issues which the Application Coordinator and IRM staff need to be cognizant of when the Education Tracking module is initially installed. This section discusses these topics which include: New Person and PAID Employee file relationships, file descriptions, site configurable file entries, software warnings, package keys, unique legal requirements, data conversions, the concept of mandatory review groups, and general information on editing and deleting class records.

> 1\. The software environment

> The Education Tracking application must be installed in an environment with not less than:

> Kernel Version 7.1

> FileMan Version 20

> 2\. PAID files

> The following PAID files are exported with this software: PAID Employee file (#450)

> This file contains employee master record data that is sent to the station from the Austin Automation Center.

> PRSE Student Education Tracking file (#452)

> This file contains information on employee and non-employee attendance at continuing education and inservice programs. (Selected data is manually entered into the OLDE software).

> PRSE Program/Class file (#452.1)

> This file contains the names of all classes including local continuing

> education programs, mandatory/required classes, miscellaneous inservice programs, and nursing ward inservice used in the Education Tracking software. Non-local C.E. class names are not stored in this file.

> PRSE Education Program/Class Supplier file (#452.2)

> This file contains the names of an individual, companies, or organizations presenting or supplying the program(s).

> PRSE Mandatory Training (MI) Class Group file (#452.3)

> This file groups the names of mandated or required classes and associates these groups with a service, a category of staff or as hospital wide. In the Nursing software, these groups were previously known as review groups and the names were stored in the NURS MI Class Group file. These training groups can now be associated with individual persons or entire services.

> PRSE Education Program/Class Category file (#452.4)

> This file contains a listing of categories which is used to identify the type of program or training received. Editing of the file's entries is limited to the application's developers and is exported with the package. (Selected data is manually entered into the OLDE software).

> PRSE Education Presentation Media file (#452.5)

> This file contains a listing of class presentation formats.

> PRSE Employee Purpose of Training file (#452.51)

> This file contains a listing of purposes used in describing the reason for the training received. Editing of the file's entries is limited to the application's developers and is exported with the package. (Selected data is manually entered into the OLDE software).

> PRSE Svc Reasons for Training file (#452.6)

> This file contains the hospital service's reason or purpose for training received. Each service may add information to this file.

> PRSE Parameters file (#452.7)

> This file contains specific medical center parameters used in the Education

> Tracking software.

> PRSE Education Registration file (#452.8)

> This file contains information on student registration for individual classes.

> PRSE Education Accreditation Organizations file (#452.9)

> This file contains a list of organizations conferring CEUs or contact hours for (i. e., accrediting) continuing education programs. Data is exported through the software and local entries can be added.

> 3\. File population

> The following files are not exported with data and information must be entered into each file prior to using the software:

> a\. PRSE Education Program/Class Supplier (#452.2)

> b\. PRSE Education Presentation Media (#452.5)

> c\. PRSE Svc Reasons for Training (#452.6)

> These files are editable by the Application Coordinator and data should be added to the files after discussing the proposed entries with other service application coordinators. Refer to the chapter on Site Files for an explanation on entering data into these files.

> The software is also exported with the following populated files:

> a\. Employee Purpose Of Training (#452.51)

> b\. Education Program/Class Category (#452.4)

> Data contained in these two files is not to be edited through VA FileMan at the medical center. As additional categories are officially added by Central Office, the developers will export a patch to update these files.

> 4\. Menus

> The main option for the Education Tracking software is PRSE-SYS-MGR or the System Manager's Menu. This menu should be assigned to the Information Resource Management Service (IRMS) employee supporting the software.

> System Managers' Menu.

> 1 IRM Menu ...

> 2 Package Coordinator Menu ...

> 3 Education Tracking Instructor Menu ...

> The System Manager/designee should be solely responsible for executing any changes under the IRM Menu and needs to be familiar with the following menu.

> IRM Menu

> 1 Enter/Edit Tracking Parameter File

> 2 Purge Student Tracking File

> The Application Coordinator should also be knowledgeable of the information contained in the options of the IRM Menu.

> The Enter/Edit Tracking Parameter File option contains fields which: (1) place the software on-line/off-line, (2) store the facility name used in printing reports, and (3) turn on and off access to the New Person and the PRSE Education Program/ Class Supplier files. The Purge Student Tracking File option deletes information from the PRSE Student Education Tracking file based on a date indicated by the user. The purged data is only retrievable from a backup tape. Archiving to another medium is not available in this version.

> The PRSE Education Tracking Application Coordinator's primary menu consists of the following options:

> Package Coordinator Menu

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Information ...</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Enter/Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Attendance Menu ...</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 4 Reports Menu ...

> 5 Package Set-up Menu ...

> Functionally these options allow the creating and editing of class information, permit individual registration in classes, document attendance at classes, and print reports. Within the Package Coordinator Menu, there is a separate menu option which can be assigned to all medical facility staff so that they may register for appropriate classes and print their own education tracking reports. The last menu option, Package Set-up Menu, is used to edit the site configurable files.

> This menu option may be given to other application coordinators and appropriate staff as designated by the PRSE Education Tracking Application Coordinator.

> The Instructor's Menu option supplies the user with the tools to set up classes, register individuals for programs, credit program attendance, print reports.

> Education Tracking Instructor Menu

> 1 Enter/Edit Class Information ...

> 2 Class Registration Enter/Delete

> 3 Attendance Menu ...

> 4 Reports Menu ...

> 5\. Keys

> There are 3 keys that are part of the Education Tracking software. Each key allows the user to access different levels of data. The keys and their descriptions are as follows:

> 1\. PRSE CORD

> • Allows user to see data for all services.

> • Allows user to register and enter attendance for anyone in an open or closed class regardless of service.

> 2\. PRSE SUP

> • Allows user to see data only for their own service.

> • Allows user to register and enter attendance for any individual in a closed class sponsored by their service.

> 3\. PRSE TRAIN

> • Used only by Nursing Service personnel.

> • Allows user to see data only for their own nursing location.

> Any user having the Enter/Edit Class Attendance option can credit attendance

> for any individual at any open class. A user with no key sees only their own data. Refer to \#13 below for an explanation of open and closed classes.

> 6\. New Person and PAID Employee file relationships

> With the installation of PAID V. 3.1 certain key relationships have been set up between the New Person file (#200), and the PAID Employee file (#450). The names of all medical center employees used in the Education Tracking application have already been entered in both files. Also, the social security numbers have been matched between the two files. The last important relationship between the New Person file and the PAID Employee file is the service associated with the medical center employee. The PAID Employee file must have an entry in the Cost Center/Organization field (#458) to identify the employee's service. The Service/ Section field of the New Person File does not need to have an entry. Education tracking relies solely on the entry in the PAID Employee file except in the case of a non-employee.

> 7\. Identifying current and separated employees

> This module uses the Separation Ind field (#80) in the PAID Employee file to identify a current employee. Only current employees are reflected in the service and deficiency reports. The Separation Ind field's description states that the field identifies a separated employee and that separated employees have a value of Y (for yes). Current employees have a value of N (for no). This field should be set before the Cost Center/Organization field to insure that the PAID Employee file

> 'ACC' cross reference is created. If the Separation Ind is set after the Cost Center/Organization, you will need to re-enter the Cost Center/Organization eight digit code or use VA FileMan to re-index the 'ACC' cross reference on the Cost Center/Organization field.

> 8\. Non-Employee entries

> Non-employees (including WOC trainees, contract employees, and house staff not on the DVA payroll) may attend any of the medical center classes and have their attendance included in the tracking software. Also, the facility may register non- employees for courses prior to their attendance. The name of the individual will have to be stored in the New Person file either by IRM or through the Education Tracking application. The name of the non-employee can be added directly through the software if the PRSE New Person File Access, in the PRSE Parameters file, is turned on. A warning will appear when entering data on the new employee. A warning, depending upon the option you have entered, states:

> a\. Is (name of individual), being added to the NEW PERSON (#200) file as a

> NON-EMPLOYEE YES//

> b\. Do you want to credit (name of individual) - NON-EMPLOYEE for attending

> (name of class)

> If the PRSE New Person File Access is turned off, then the following warning will appear:

> New entries cannot be added to the New Person file from this option - Contact the Education Package Coordinator or IRM.

> Remember, if non-employees are to be tracked in this system, IRMS must either turn on the PRSE New Person File Access switch located in the PRSE Parameters file or make entries into the New Person file for non-employees.

> 9\. Mandatory training/review groups

> Required classes for individuals which are based on service or hospital requirements can be grouped or clustered together and designated as mandatory inservice (MI) review groups. For example, all employees must attend fire and safety classes, sexual harassment classes, etc. These classes can be combined under a MI review group called hospital-wide. Another example might be the grouping of all classes required for registered nurses (e.g., blood administration, CPR, infection control, obstructed airway) in Nursing Service through a MI review group called RN (for registered nurses only). The grouping of classes into MI review groups might be easier to assign than associating the classes individually with an employee. Mandatory review groups must be associated with any employee through the option, Assign/Delete Training Groups to Staff/Services \[PRSE-EMP-MI\]. The employee's MI review group data is stored in File \#450, field \#632. This relationship is not automatically built when new employees are entered into File \#450 or when staff is assigned to a different service. A report called, Employee Mandatory Training Group/Class Report \[PRSE-MI-LIST\] prints a list of MI groups and required classes associated with an employee. A relationship between MI review groups or required classes and non-employees cannot be established in this version.

> Note: If an employee is not assigned a mandatory training review group and/or a required class, the deficiency reports will indicate a compliance of 100%. In a future version, a message will print stating that the employee is not assigned to any review group or to any required class. It is suggested that all supervisors be given the Employee Mandatory Training Group/Class Report option for the purpose of identifying staff who are not assigned appropriate training review group(s) or required classes.

> 10\. Creating and editing classes

> Before creating a new class the user must first decide the appropriate category type for the class. The possible types are: (1) mandatory inservice, (2) continuing education (for on-station or off-station presentations), (3) other/miscellaneous, and (4) ward/unit location.

> Mandatory inservice should be used if attendance is required of a group of employees and it is given on a scheduled basis (e.g., annually, quarterly, every two years, one time only). The class can be assigned to one or more mandatory review groups. Either the Enter/Edit Mandatory Training (MI/Brief) \[PRSE-M.I.\] option or the Enter/Edit Mandatory Training (MI/Expanded) \[PRSE-MIEX\] option can be used. The expanded option has a few more fields to complete and should be used if the training attendance will be submitted to the PAID system by OLDE.

> Continuing education (C.E.) can be either local C.E. or non-local C.E. and usually refers to professional educational programs of a substantial nature used to meet accreditation or licensing requirements. The granting of continuing education units (CEU) or contact hours may be involved. Local C.E. information is documented through the option Enter/Edit Local Continuing Education \[PRSE­ C.E.\]. Please note that if the continuing education program was non-local, the program or class must be entered and edited through the Attendance Menu option, Create Non-Local CE and Enter Attendance \[PRSE-NCEATTEND\]. Refer to the glossary for a definition of local and non-local C.E.

> Other/miscellaneous is used for classes not meeting mandatory inservice or C.E. criteria. The largest number of classes will probably fall into this type. Supervisory and management training, classes to review new procedures or equipment, routine technical training are examples of this type. The option Enter/Edit Miscellaneous Training \[PRSE-O.I.\] is used to capture information on these

> programs.

> Ward/Unit location is used by Nursing Service to set up classes associated with a specific nursing unit that fall into the miscellaneous type described above. The Enter/Edit Ward/Unit-Location Training \[PRSE-W.I.\] option not only allows a user to store information about the class information but also permits the user to immediately (or at a later time) record attendance. If the class is established

> before the presentation so that the employee can register, this type should probably not be used.

> The names of classes can be 2-53 characters. The software contains a programming check to make sure that the name of the class is unique. If two titles are the same, the application will prompt you to enter a different name for the second entry.

> 11\. Initial class information set up

> There are certain fields which are displayed only once, i.e., when the coordinator is initially setting up the class. These fields are: class objectives, required frequency or interval for attending the class (if the class type is mandatory/ required class), length of the class (in hours), and the name of the service sponsoring the class. These fields do not appear after the first class entry is made because the data contained in these fields does not change frequently. The user may edit these fields for future classes by using the Class File Edit option (under Package Set-up Menu) which edits the class data stored in the PRSE Program/ Class Title file (#452.1) and the PRSE Education Registration file (#452.8). Editing class data will not affect classes which have been presented and attendance taken. These courses have been stored in the PRSE Student Education Tracking file (#452); therefore, changing specific class data will not change information on previously attended classes.

> 12\. Deleting and Editing Class (not employee) Information

> The name of a class and its identifying information which is stored in the PRSE Program/Class file (#452.1) may be deleted through the Class File Edit option \[PRSE-CLAS\] located in the Package Set-up menu. This excludes non-local C.E. class names which are not stored in File \#452.1. When a class is deleted or removed from the PRSE Program/Class file, the corresponding entry in the PRSE Education Registration file (#452.8) is also deleted.

> 13\. Editing and Deleting of Employee Class Information

> When employees have attended a class and certain information is in error (i.e., name of class, program class supplier, type of training class, and class length), the information can be changed for all the attendee's records residing in the PRSE Student Education Tracking file (#452). The use of the Modify Past Class Information option \[PRSE-I-EMP\] (under Attendance Menu) will correct all erroneous records associated with the class. Use of the Quick Attendance Update of Past/ Purged Classes option \[PRSE-I-EMP\] allows the users to make a copy of an

> existing class attendance record from the PRSE Student Education Tracking file (#452) and place another student's name on it. All class attendance is based on entries in the PRSE Program/Class file (452.1). If the class name is purged or deleted from that file, you cannot add a student's attendance through the Enter/ Edit Class Attendance option. Therefore, the Quick Attendance Update of Past/ Purged Classes option is used to document class attendance for a single new attendee without reentering it into the PRSE Program/Class file.

> 14\. Limiting class registration and multi-service attendance

> The software has the capability to control the opening or closing of a class for registration, limiting the number of registrants, and restricting the participation of employees from services.

> The Class Limit field is used to limit future class registration by either entering a

> 0 (zero) to close the class or a null value (blank) to open the class. A limit can be placed on the number that can register for a class session by entering a numeric value in the field. This information is otherwise summarized below:

> a\. 0 (zero) = closes the class to registration.

> b\. null (no field entry or value, blank) = opens the class to registration with no limitations on the number of registrants.

> c\. number from 1-999 = opens the class with a limitation on registration which is based on the numeric value in the field.

> The Open/Closed field is used to allow the presenting/sponsoring service to open or close the class to other services. If closed is entered as the value, other service employees will not be able to register for the class. In general, closed should be associated with a class when the class is established for a specific service's purpose. The class should be open if more than one service's employees may attend. For example if the Pathology Service is presenting a class to hematology section employees on operating a new machine to do blood counts, the class should probably be closed. However if Human Resources is presenting a class to supervisors on Labor Relations, the class would be set as open to make the class available to all services.

> 15\. Class III conversions

> Data stored in the Automated Training Tracking System (ATTS) application (Class III software) or any other Class III/locally developed education tracking software will not be converted by the Education Tracking software.

> 16\. Nursing V. 3.0 data conversion (after installation of Nursing V. 3.0)

> With the installation of the next version of the Nursing application, V. 3.0 staff training information will be removed from the Nursing files and stored in the appropriate PAID files.

> The following summarizes these changes:

> \(a\) In the NURS Staff file (#210), data previously found in fields 27 (Continuing Education Program) and 28 (Mandatory Inservice Program) will be stored in the PRSE Student Education Tracking file (#452).

> \(b\) Data previously stored in the NURS MI Class Group file (#212.42) will be found in the PRSE Mandatory Training (MI) Class Group file (#452.3).

> \(c\) Data previously stored in the NURS Mandatory Inservice file (#212.4)

> will be stored in the EDUCATION PROGRAM/CLASS TITLE file (#452.1).

> \(d\) In the NURS STAFF file, the MI Review Group field (#28.1) which previously pointed to the NURS MI CLASS GROUP file (#212.42) will display employee information found in the EDUCATION MI REVIEW GROUP file (#452.3).

> Nursing Service will assign a review group to a nursing employee through the Assign/Delete Training Groups to Staff/Services option \[PRSE-EMP-MI\]. The MI review group information associated with the nursing employee will be updated in both the PAID Employee (#450) and the NURS Staff (#210) files.

> Class start dates must be entered for those classes converted from the nursing software before the class is opened for registration. See section on Entering Dates within this chapter. Start dates can be entered through the following options:

> \(a\) Enter/Edit Mandatory Training (MI/Expanded) \[PRSE-MIEX\] (b) Enter/Edit Mandatory Training (MI/Brief) \[PRSE-M.I.\]

> \(c\) Enter/Edit Local Continuing Education \[PRSE-C.E.\]

> Editing of all data previously accomplished through the Nursing application is now done through the Education Tracking application.

> 17\. Special legal requirements for running the module

> There are no unique legal requirements for implementing this software module.

> Education Process

> (general)

> Enter data into site files

> Create classes

> Create Mandatory Inservice Training Groups and assign groups to employees

> Do you want to register students?

Yes

Register students

> No

> Take attendance

> Do you want to edit student's records?

Yes

Modify student's records

> No

> Print reports

> Quit

> Attendance Breakdown

Mandatory Training

(brief)

Mandatory Training

(expanded)

> Create classes and take attendance on the following types of classes

> Local Continuing

> Education

Non-local Continuing

> Education

> (take attendance and setup)

Other/Miscellaneous

Training

Ward/Unit-Location

Training

> (take attendance and setup)

> Take Attendance

> (general)

> Class Held

> Register students

> (optional)

> Do you want to just take attendance?

Yes

Enter/edit class attendance

> No

> Do you want to edit a specific record?

Yes

Quick attendance update of past/purged classes

> No

> Do you want to edit all records for a class?

Yes

Modify past class information

> No

> Do you want to edit mandatory classes only?

Yes

Quick mandatory training (MI) update

> No

> Quit

> Reports Breakdown

> Class Registration

> Calendar Report

> Class Registration

> Roster Report

> Service Mandatory Training (MI) Deficiency Report

> Service Training Report

> Reports

> Employee Mandatory Training Group/Class Report

> OLDE Training Coding

Report

> Individual Training

Report

> Individual Mandatory Training (MI) Deficiency

> IRM Menu

> IRM Menu

> (IRM)

> Enter/Edit Tracking Parameter File (IRM)Purge Student Tracking File (IRM)

> Package Coordinator Menu

> Package Coordinator Menu

> (Package Coordinator (PC))

> Enter/Edit Class Information Menu

> (PC, or Instructor)

> \*Enter/Edit Mandatory

> Training (Brief)

> \*Enter/Edit Mandatory

> Training (Expanded)

> \*Enter/Edit Local Continuing

> Education

> \*Enter/Edit Miscellaneous

> Training

> \*Enter/Edit Unit/Location

> Inservices

> Reports Menu

> (PC, or Instructor)

> \*Class Registration Calendar

> \*Class Registration Roster

> \*Service Mandatory Training

> \(MI\) Deficiency Report

> \*Service Training Report

\*Employee Mandatory Training

> Group/Class Report

> \*OLDE Training Coding Report

> \*Individual Training Report

\*Individual Mandatory Training

> \(MI\) Deficiency

> Class Registration Enter/Delete

> (PC, Instructor, or Employee)

> Attendance Menu (PC, Instructor, or Clerk)

> \*Enter/Edit Class Attendance

> \*Create Non-Local CE and

> Enter Attendance

> \*Modify Past Class Information

> \*Quick Attendance Update of

> Past/Purged Classes

> \*Quick Mandatory Training

> \(MI\) Update

> Package Set-up Menu

> (PC)

> \*Class File Edit

> \*Create Mandatory Training

> \(MI\) Groups

\*Assign/Delete Training Groups for Staff/Services

> \*Accrediting Organization

> \*Presentation Media

> \*Presenter/Supplier

> \*Service Reason

> Education Tracking Instructor Menu

> Education Tracking Instructor Menu (Instructor)

> Enter/Edit Class Information

> Menu

> (Instructor)

> \*Enter/Edit Mandatory

> Training (Brief)

> \*Enter/Edit Mandatory

> Training (Expanded)

> \*Enter/Edit Local Continuing

> Education

> \*Enter/Edit Miscellaneous

> Training

> \*Enter/Edit Unit/Location

> Training

> Class Registration Enter/Delete

> (Instructor, or Employee)

> Attendance Menu

> (Instructor, or Clerk)

> \*Enter/Edit Class Attendance

\*Create Non-Local CE and Enter

> Attendance

> \*Modify Past Class Information

> \*Quick Attendance Update of

> Past/Purged Classes

\*Quick Mandatory Training (MI) Update

> Reports Menu

> (Instructor)

> \*Class Registration Calendar

> Report

\*Class Registration Roster Report

> \*Service Mandatory Training

> \(MI\) Deficiency Report

> \*Service Training Report

> \*Employee Mandatory Training

> Group/Class Report

> \*OLDE Training Coding Report

> \*Individual Training Report

\*Individual Mandatory Training

> \(MI\) Deficiency

> File Diagram

> This is a diagram of the files for the Education Tracking software and their relationships to each other.

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 13%" />
<col style="width: 23%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File/Package: EMPLOYEE EDUCATION TRACKING</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Date: NOV 25,1994</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FILE (#)</p>
</blockquote></td>
<td><blockquote>
<p>POINTER</p>
</blockquote></td>
<td><blockquote>
<p>(#) FILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POINTER FIELD</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>POINTER FIELD</p>
</blockquote></td>
<td><blockquote>
<p>FILE POINTED TO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------------------------------------------------------------ L=Laygo S=File not in set N=Normal Ref. C=Xref.

> \*=Truncated m=Multiple v=Variable Pointer

> ------------------------------­

> \| 452 PRSE STUDENT EDUCATIO\* \|

> \| STUDENT NAME \|-\> NEW PERSON

> \| PROGRAM/CLASS CATEGORY \|-\> PRSE EDUCATION PROGRAM/CLASS CA\*

> \| PURPOSE OF TRAINING \|-\> PRSE EMPLOYEE PURPOSE OF TRAINI\*

> \| ACCREDITING ORGANIZATION \|-\> PRSE EDUCATION ACCREDITATION OR\*

> \| EMPLOYEE/ST:EMPLOYEE/ST\* \|-\> NEW PERSON

> \| m SVC REASON:SVC REASON \|-\> PRSE SVC REASONS FOR TRAINING

> ------------------------------­

> ------------------------------­ PAID EMPLOYEE (#450.0633) \| \| MANDATORY CLASS ................................ (N S C )-\> \| 452.1 PRSE PROGRAM/CLASS \| PRSE MANDATORY TRAIN (#452.31) \| \|

> M.I. PROGRAM/CLASS:MANDATORY CLASSES ........... (N )-\> \| SERVICE \|-\> PAID COST CENTER/ORGANIZATION PRSE EDUCATION PROGR (#452.42) \| \|

> PROGRAM/CLASS .................................. (N )-\> \| EMPLOYE:MI REVI:MI REVI\* \|-\> PRSE MANDATORY TRAINING (MI) CL\* PRSE EDUCATION REGIS (#452.8) \| \|

CLASS NAME ..................................... (N C L)-\> \| \|

> ------------------------------­

> ------------------------------­

> \| 452.2 PRSE EDUCATION PROG\* \|

> \| STATE \|-\> STATE

> ------------------------------­

> ------------------------------­ PAID EMPLOYEE (#450.0632) \| \| MI REVIEW GROUP ................................ (N S C )-\> \| 452.3 PRSE MANDATORY TRAI\* \|

> \| SERVICE \|-\> PAID COST CENTER/ORGANIZATION

> \| m M.I. PROGRA:MANDATORY C\* \|-\> PRSE PROGRAM/CLASS

> ------------------------------­

> ------------------------------­ PRSE STUDENT EDUCATI (#452) \| \| PROGRAM/CLASS CATEGORY ......................... (N )-\> \| 452.4 PRSE EDUCATION PROG\* \| PRSE EDUCATION REGIS (#452.8) \| \|

> CLASS CATEGORY ................................. (N )-\> \| m PROGRAM/CLA:PROGRAM/CLA\* \|-\> PRSE PROGRAM/CLASS

> ------------------------------­

> ------------------------------­ PRSE EDUCATION REGIS (#452.8) \| \| TYPE OF MEDIA .................................. (N )-\> \| 452.5 PRSE EDUCATION PRES\* \|

> ------------------------------­

> ------------------------------­ PRSE STUDENT EDUCATI (#452) \| \| PURPOSE OF TRAINING ............................ (N )-\> \| 452.51 PRSE EMPLOYEE PURP\* \| PRSE EDUCATION REGIS (#452.8) \| \| PURPOSE OF CLASS ............................... (N )-\> \| \|

> ------------------------------­

> ------------------------------­ PRSE STUDENT EDUCATI (#452.033) \| \| SVC REASON ..................................... (N C )-\> \| 452.6 PRSE SVC REASONS FO\* \| PRSE EDUCATION REGIS (#452.877) \| \| SERVICE REASON FOR CLASS ....................... (N C )-\> \| \|

> ------------------------------­

> ------------------------------­

> \| 452.8 PRSE EDUCATION REGI\* \|

> \| CLASS NAME \|-\> PRSE PROGRAM/CLASS

> \| TYPE OF MEDIA \|-\> PRSE EDUCATION PRESENTATION MED\*

> \| SPONSORING SERVICE/SECTI\* \|-\> PAID COST CENTER/ORGANIZATION

> \| ACCREDITING ORGANIZATION \|-\> PRSE EDUCATION ACCREDITATION OR\*

> \| CLASS CATEGORY \|-\> PRSE EDUCATION PROGRAM/CLASS CA\*

> \| PURPOSE OF CLASS \|-\> PRSE EMPLOYEE PURPOSE OF TRAINI\*

> \| m SERVICE REA:SERVICE REA\* \|-\> PRSE SVC REASONS FOR TRAINING

> \| m START D:STUDENT:STUDENT\* \|-\> NEW PERSON

> ------------------------------­

> ------------------------------­

------------------------------­

\> STATE

> Package Operation

> Descriptions:

> The chapters contained under Package Operation describe the sequence of steps used in:

> 1\. Setting up the module's medical center site files and purging old student education records.

> 2\. Creating educational program records for:

> • Mandatory/required classes.

> • Continuing education programs.

> • Classes presented on nursing units.

> • Miscellaneous inservices which cannot be categorized under the previous class types.

> 3\. Creating hospital-wide and service specific mandatory training groups which are also known as mandatory review groups.

> 4\. Associating training groups with hospital employees for the purpose of tracking attendance at required classes.

> 5\. Registering students for classes by an instructor, secretary, or the employee himself (self registration). This step is optional.

> 6\. Crediting program attendance at:

> • Required classes.

> • Local and non-local continuing education classes.

> • Nursing unit inservice programs.

> • Other classes which do not fall in the above categories.

> 7\. Editing attendance of past classes where the data might have been entered in error.

> 8\. Printing reports which include:

> • class calendars.

> • registration rosters.

> • required training deficiency reports by service and for an individual employee.

> • service training reports.

> • individual training reports.

> • a listing of required classes and mandatory review groups associated with an employee.

> • a report used to complete OLDE training data entry.

> Menu Display:

> Select Education Tracking System Menu Option: 2 Package Coordinator Menu

> 1 Enter/Edit Class Information ...

> 2 Class Registration Enter/Delete

> 3 Attendance Menu ...

> 4 Reports Menu ...

> 5 Package Set-up Menu ...

## Chapter 2: IRM and Package Set-up Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1. IRM Menu

> Description:

> This menu contains the package site parameter option and a purge option for the

> PRSE Student Education Tracking file (#452).

> Menu Display:

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>IRM Menu ...</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Package Coordinator Menu ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Education Tracking Instructor Menu ...</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Education Tracking System Menu Option: 1 IRM

> 1 Enter/Edit Tracking Parameter File

> 2 Purge Student Tracking File

> Enter/Edit Tracking Parameter File

> Description:

> This option allows the user to edit the PRSE Parameters file (#452.7). By using this option, the user can take the Education Tracking application off-line, allow new people to be entered into the New Person file (#200) automatically, or allow LAYGO into the PRSE Education Program/Class Supplier file (#452.2).

> Additional Information:

> This option should be assigned to IRM staff who possess the VA FileMan access of "@". If the user does not have this level of access, only the Station Name field can be edited.

> Menu Display:

> Select Education Tracking System Menu Option: 1 IRM Menu

> 1 Enter/Edit Tracking Parameter File

> 2 Purge Student Tracking File

> Screen Prints:

> Select IRM Menu Option: 1 Enter/Edit Tracking Parameter File

> NAME: ONE// (No Editing)

> STATION NAME: PAIDEDSPONSOR,ONE// ??

> This field should contain the station name or the desired default

> location for all locally presented training (e.g., VAMC HINES).

> STATION NAME: PAIDEDSPONSOR,ONE// \<RET\>

> PRSE OFFLINE/ON-LINE: ON-LINE// ??

> this switch will allow the Education Tracking Application to be taken

> off-line without bringing the entire system down.

> CHOOSE FROM:

> 1 OFF-LINE

> 0 ON-LINE

> PRSE OFFLINE/ON-LINE: ON-LINE// \<RET\>

> SUPPLIER/PRESENTER LAYGO: LAYGO ACCESS// ??

> This field allows IRM to turn on/off laygo access to the Supplier/

> Presenter File in the Education Tracking Application.

> Additional information on the Supplier/Presenter field can be found under each option explanation in Chapter 3.

> CHOOSE FROM:

> 1 LAYGO ACCESS

> 0 NO LAYGO ACCESS

> SUPPLIER/PRESENTER LAYGO: LAYGO ACCESS// \<RET\>

> NEW PERSON FILE ACCESS: NO ACCESS TO NEW PERSON FILE

> 2.4 PAID V. 4.0 User Manual March 2018

> // ??

> This field allows IRM to turn on/off access to the New Person File from

> the Education Tracking Application.

> CHOOSE FROM:

> 1 ACCESS TO NEW PERSON FILE

> 0 NO ACCESS TO NEW PERSON FILE

> NEW PERSON FILE ACCESS: NO ACCESS TO NEW PERSON FILE

> // \<RET\>

> Additional information on the purpose for this field is found in Chapter 1, Package Management, (under) 8. Non-Employee entries.

> Menu Access:

> The Enter/Edit Tracking Parameter File option is accessed through the IRM Menu option.

> Purge Student Tracking File

> Description:

> This option allows the user to purge old education records from the PRSE Student

> Tracking file (#452). The user can purge data from a specified date.

> Additional Information:

> One-time only classes are not purged by this option. Once the data is purged from the file, the data can only be restored from a backup.

> Menu Display:

> Select Education Tracking System Menu Option: 1 IRM Menu

> 1 Enter/Edit Tracking Parameter File

> 2 Purge Student Tracking File

> Screen Prints:

> Select IRM Menu Option: 2 Purge Student Tracking File

> Has IRM been contacted before purging data from file 452

> to insure that journaling of the ^PRSE global has been suspended? YES// ??

> ANSWER 'YES' or 'NO'

> Journaling of the ^PRSE global should be suspended before any data is purged from the PRSE Student Tracking file (#452).

> Has IRM been contacted before purging data from file 452

> to insure that journaling of the ^PRSE global has been suspended? YES// \<RET\>

> (YES)

> Start With DATE: OCT 31, 1991//??

> Enter a date which is less than or equal to OCT 27, 1994.

> The default date is approximately 156 weeks (3 years) prior to the current date.

> Start With DATE: OCT 31, 1991// \<RET\> (OCT 31, 1991)

> Are you sure you want to delete data prior to OCT 31, 1991? YES// ??

> ANSWER 'YES' OR 'NO':

> Are you sure you want to delete data prior to OCT 31, 1991? YES// \<RET\>

> Purging 452 data........

> Data is being purged at this time.

> Menu Access:

> The Purge Student Tracking File option is accessed through the IRM Menu option.

> 2. Package Set-up Menu

> Description:

> This menu allows the user to enter or edit data in the software's site files. These files have been created so that the medical facility can enter information specific to their organization on topics such as:

> 1\. Organizations that accredit programs attended by staff.

> 2\. Associating review groups and classes with employees and services.

> 3\. Editing class content found in the PRSE Student Education Tracking File

> (#452).

> 4\. Entering names of mandatory training groups which can be associated with specific services, staff positions, categories of personnel, and all hospital personnel.

> 5\. Media used in presenting the course content.

> 6\. Names of presenters and contractors associated with the programs.

> 7\. Specific reasons for hospital services requiring the classes.

> Menu Display:

> 1 IRM Menu ...

> 2 Package Coordinator Menu ...

> 3 Education Tracking Instructor Menu ...

> Select Education Tracking System Menu Option: 2 Package Coordinator Menu

> 1 Enter/Edit Class Information ...

> 2 Class Registration Enter/Delete

> 3 Attendance Menu ...

> 4 Reports Menu ...

> 5 Package Set-up Menu ...

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

> 1 Class File Edit

> 2 Create Mandatory Training (MI) Groups

> 3 Assign/Delete Training Groups for Staff/Services

> 4 Accrediting Organization

> 5 Presentation Media

> 6 Presenter/Supplier

> 7 Service Reason

> The following pages provide detailed information about entering and editing information contained in files accessed by the above options.

> Class File Edit

> Description:

> This option allows the user to edit certain data for classes (i.e., mandatory, local continuing education, ward/location, and other/miscellaneous) stored in the PRSE Program/Class file (#452.1) through the Enter/Edit Class Information option.

> Additional Information:

> Non-local C.E. classes cannot be edited through this option, but through the Create Non-Local CE and Enter Attendance option found in the Attendance menu. Users CANNOT ADD new class entries through this option. All new classes are added through the Enter/Edit Class Information option. Once a class

> is presented it can be deleted through this option by entering the @ sign at the first prompt after selecting the correct class. Classes should not be deleted unless the user is sure that it will not be presented again in the near future or the user

> wants the mandatory class to appear on the deficiency reports.

> When editing class information the Class Name field is automatically changed in the Education Registration file (#452.8). Editing class information or deleting a class will NOT affect information for employees whose attendance has been recorded. The records of past class attendance can be edited through the Attendance options.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: Forward jumping is not allowed in this option; backward jumping is allowed.

> Screen Prints:

> Select Package Set-up Menu Option: 1 Class File Edit

> Select CLASS: ?

> The class must be an existing class in the file. A user cannot enter a new entry into the PRSE Program/Class file.

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> 5W NAME IV PUMPS NURSING SERVICE

> 5W IVAC 4200 NURSING SERVICE

> FIRE SAFETY INFORMATION SYSTEMS CENTER

> FIRE SAFETY NURSING SERVICE

> '^' TO STOP: ^

> Select CLASS: 3W BIOETHICS NURSING SERVICE

> PROGRAM/CLASS TITLE: 3W BIOETHICS// ?

> Answer must be 2-53 characters in length

> This is the name of the class.

> PROGRAM/CLASS TITLE: 3W BIOETHICS// \<RET\>

> OBJECTIVE(S):

> This field is used to enter the class objectives and it is word-processing.

> EDIT Option: \<RET\>

> 1\>LEARN ABOUT BIOETHICS. EDIT Option: \<RET\>

> PRSE PROGRAM/CLASS LENGTH HRS: 8// ?

> Indicate the number of hours by typing a number between 0 and 9999.99, 2

> Decimal Digits.

> This is the class length in hours as reported to Austin.

> PRSE PROGRAM/CLASS LENGTH HRS: 8// \<RET\>

> Note: When the class type is mandatory inservice, the FREQUENCY field is displayed between the PRSE PROGRAM/CLASS LENGTH HRS field and the TYPE OF EDUCATION field.

> TYPE OF EDUCATION: Ward Inservice// ?

> CHOOSE FROM:

> M Mandatory Inservice

> C Continuing Education

> O Other Training

> W Ward Inservice

> TYPE OF EDUCATION: Ward Inservice// \<RET\>

> If this class was a mandatory inservice, a REQUIRED FREQUENCY prompt would have displayed before the TYPE OF EDUCATION prompt.

> SERVICE: ISC// ?

> Select Cost Center/Organization Code entry other than 'MISCELLANEOUS'

> ANSWER WITH PAID COST CENTER/ORGANIZATION NAME

> DO YOU WANT THE ENTIRE PAID COST CENTER/ORGANIZATION LIST? Y (YES) CHOOSE FROM:

> A & M MGT AMBULATORY CARE ANESTHESIOLOGY AUDIOLOGY

> BLIND REHAB BUILDING MGT CHAPLAIN

> CHIEF OF STAFF DENTAL DERMATOLOGY DIALYSIS DIETETICS

> .

> .

> .

> This field associates the class with a specific service.

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ?

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> This field indicates if the class is opened to individuals outside of the service. Closed programs will not be displayed to potential registrants from other services through the registration option.

> OPEN/CLOSED: CLOSED// OPEN Select CLASS: \<RET\>

> Menu Access:

> The Class File Edit is accessed through the Package Set-up Menu in the Package

> Coordinator Menu Option.

> Create Mandatory Training (MI) Groups

> Description:

> This option allows creating or editing of the PRSE Mandatory Training (MI) Class Group file (452.3) which contains information on and classes associated with mandatory inservice (MI) review groups.

> Additional Information:

> Required classes for individuals, based on service or hospital requirements, can be grouped or clustered together and designated as mandatory inservice (MI) review groups (also referred to as mandatory training/inservice or mandatory review groups). For example, all employees must attend fire and safety classes, sexual harassment classes, etc. These classes can be combined under a MI review group called hospital-wide. Another example might be the grouping of all classes required to be taken by registered nurses (e.g., blood administration, CPR, infection control, obstructed airway) in Nursing Service through a MI review group called RN (for registered nurses only). The grouping of classes into MI review groups might be easier to assign than associating the classes individually with an employee. Mandatory review groups may be associated with any employee through the option, Assign/Delete Training Groups for Staff/Services \[PRSE-EMP-MI\]. The MI review group data is stored in File \#450, field \#632. A report called, Employee Mandatory Training Group/Class Report \[PRSE-MI­ LIST\] prints a list of MI groups and required classes associated with an

> employee.

> Any individual assigned this option can create a MI review group. The user is not required to hold any PRSE key.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Package Set-up Menu Option: 2 Create Mandatory Training (MI) Groups

> Select MANDATORY TRAINING GROUP NAME: ?

> This is the name of a mandatory or required class group which may be associated with a service or a specific group of employees.

> ANSWER WITH EDUCATION M.I. REVIEW GROUP MI REVIEW GROUP

> DO YOU WANT THE ENTIRE PRSE MANDATORY TRAINING (MI) CLASS GROUP LIST? Y

> (YES)

> CHOOSE FROM:

> 120-FOOD HANDLERS DIETETICS

> ACLS NURSING SERVICE

> DIETICIAN DIETETICS

> LPN NURSING SERVICE

> MAS ADMINISTRATION

> OPERATING ROOM NURSING SERVICE

> ORTHO NURSING SERVICE

> PHARMACIST PHARMACY

> QUALITY MANAGEMENT NURSING SERVICE

> RN NURSING SERVICE

> RN DIALYSIS NURSING SERVICE

> RN/ICU NURSING SERVICE

> SYSTEM MANAGMENT IRM

> YOU MAY ENTER A NEW PRSE MANDATORY TRAINING (MI) CLASS GROUP, IF YOU WISH Answer must be 2-22 characters in length.

> Select MANDATORY TRAINING GROUP NAME: HOSPITAL GROUP

> ARE YOU ADDING 'HOSPITAL GROUP' AS

> A NEW PRSE MANDATORY TRAINING (MI) CLASS GROUP? Y (YES)

> NAME: HOSPITAL GROUP//

> SERVICE: NURSING SERVICE// ? The default value for the service shown after the

> service prompt is the service of the user entering the mandatory training group

> name.

> NOTE: Enter Miscellaneous after the service prompt if you want the MI Review group to apply across hospital services.

> Enter 'MISCELLANEOUS' if you want to designate this

> MI Review Group to be assigned as hospital wide.

> ANSWER WITH PAID COST CENTER/ORGANIZATION NAME

> DO YOU WANT THE ENTIRE 17-ENTRY PAID COST CENTER/ORGANIZATION LIST? Y (YES)

> CHOOSE FROM:

> ADMINISTRATION

> AMBULATORY CARE

> CHAIPLAIN

> DIETETIC

> ENGINEERING

> EXTENDED CARE

> .

> .

> .

> SERVICE: NURSING SERVICE// MISCELLANEOUS

> Select MANDATORY CLASSES: ?

> ANSWER WITH M.I. PROGRAM/CLASS MANDATORY CLASSES

> YOU MAY ENTER A NEW M.I. PROGRAM/CLASS, IF YOU WISH

> Enter program or class that is mandated by this group.

> Select only MI entries.

> Note: Only mandatory inservice classes can be selected at this prompt. The class must be created before it can be associated with a review group.

> From the following list, enter those classes you want to associate with the mandatory training group name, Hospital Group.

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE 341-ENTRY PRSE PROGRAM/CLASS LIST? Y (YES) CHOOSE FROM:

> ACQUISITION TRAINING ADP SECURITY BIOETHICS

> BLOOD ADMINISTRATION BLOOD-BORNE PATHOGENS CONSCIOUS SEDATION

> CONTINOUS QUALITY IMPROVEMENT FIRE AND SAFETY

> SEXUAL HARASSMENT

> Select MANDATORY CLASSES: SEXUAL HARASSMENT

> Select MANDATORY CLASSES: FIRE AND SAFETY

> Select MANDATORY CLASSES: \<RET\>

> The two classes, sexual harassment and fire and safety are now assigned to the

> Hospital mandatory training group.

> Select MANDATORY TRAINING GROUP NAME: \<RET\>

> Menu Access:

> The Creating Mandatory Training (MI) Groups option is accessed through the

> Package Set-up Menu in the Package Coordinator Menu Option.

> Assign/Delete Training Groups for Staff/Services

> Description:

> This option allows the assigning of employees or services to one or more mandatory training (MI) groups and/or required classes. The relationship between employee and review group(s) is not automatically built when new employees are entered into the Paid Employee file (File \#450) or when staff is assigned to a different service. The mandatory training/MI group and class data is stored in File \#450.

> Additional Information:

> The user has three approaches to assigning mandatory review groups and/or required classes to services and employees. After first creating the mandatory training (MI) groups, employees can then be assigned to or disassociated from review groups using the following paths. If all employees from more than one service are to be assigned, use the (M)ultiple Services - All Employees path. This would be the way to allocate Hospital Wide MI Groups to all employees. Use the (A)ll Employees For a Service choice to assign a MI Group to just one service. An example would be a group of classes on specific police subjects that is assigned to all Police and Security Service employees. If only some employees in a service are assigned to an MI group, use the (S)elected Service Employee path. The (S)elected Service Employee selection can also be used to add individual mandatory classes

> to individual employees. For instance if only two housekeeping aides are assigned to operate a special type of equipment requiring a yearly review of safety, this option would be used to add the class to only their PAID employee record. Employees cannot be assigned review groups which have no associated classes. Please note that unless an individual is assigned to a MI review group or associated with a required class, a deficiency report cannot be printed for the employee.

> Any user who has been given this option can assign a review group to employees or services. Information on the employee's MI review groups and other required classes can be printed through the Employee Mandatory Training Group/Class report found in the Reports menu.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter/Edit Tracking Parameter File

> Description:

> This option allows the user to edit the PRSE Parameters file (#452.7). By using this option, the user can take the Education Tracking application off-line, allow new people to be entered into the New Person file (#200) automatically, or allow LAYGO into the PRSE Education Program/Class Supplier file (#452.2).

> Additional Information:

> This option should be assigned to IRM staff who possess the VA FileMan access of "@". If the user does not have this level of access, only the Station Name field can be edited.

> Menu Display:

> Select Education Tracking System Menu Option: 1 IRM Menu

> 1 Enter/Edit Tracking Parameter File

> 2 Purge Student Tracking File

> Screen Prints:

> Select IRM Menu Option: 1 Enter/Edit Tracking Parameter File

> NAME: ONE// (No Editing) STATION NAME: PAIDORG// ??

> This field should contain the station name or the desired default location for all locally presented training (e.g., VAMC ORG).

> STATION NAME: PAIDORG// \<RET\>

> PRSE OFFLINE/ON-LINE: ON-LINE// ??

> this switch will allow the Education Tracking Application to be taken

> off-line without bringing the entire system down.

> CHOOSE FROM:

> 1 OFF-LINE

> 0 ON-LINE

> PRSE OFFLINE/ON-LINE: ON-LINE// \<RET\>

> SUPPLIER/PRESENTER LAYGO: LAYGO ACCESS// ??

> This field allows IRM to turn on/off laygo access to the Supplier/

> Presenter File in the Education Tracking Application.

> Additional information on the Supplier/Presenter field can be found under each option explanation in Chapter 3.

> CHOOSE FROM:

> 1 LAYGO ACCESS

> 0 NO LAYGO ACCESS

> SUPPLIER/PRESENTER LAYGO: LAYGO ACCESS// \<RET\>

> NEW PERSON FILE ACCESS: NO ACCESS TO NEW PERSON FILE

> This/These group(s) will be assigned by a background Job.

> Select one of the following:

> A (A)ll Employees For a Service

> M (M)ultiple Services - All Employees

> S (S)elected Service Employees

> Example 2. Assigning hospital-wide mandatory or required review groups to all employees in all services:

> This is an example of the process for assigning a hospital wide group to all services and all employees.

> Select ASSIGNMENT OPTION: M (M)ultiple Services - All Employees

> Select (M)ultiple Services - All Employees

> The following is a display of all hospital services from which you can select (all employees in) all services, a single service or a group of selected services.

> Select ASSIGNMENT OPTION: M (M)ultiple Services - All Employees

> 1\. A & M MGT 2.AMBULATORY CARE

> 3\. ANESTHESIOLOGY 4.AUDIOLOGY

> 5\. BLIND REHAB 6.CHIEF OF STAFF

> 7\. CHAPLAIN 8.DENTAL

> 9\. DERMATOLOGY 10.DIALYSIS

> 11\. DIETETICS 12.DOMICILIARY CARE

> 13\. EDUCATION 14.ENGINEERING

> 15\. ENVIRONMENTAL MGT. 16.FISCAL

> 17\. GENERAL COUNSEL 18.GERIATRIC RESEARCH

> 19\. IRM 20.ISC

> 21\. LABORATORY 22.LIBRARY

> 23\. MAS 24.MCCR

> 25\. MEDICAL 26.MEDICAL MEDIA

> 27\. MISCELLANEOUS 28.NATIONAL CEMETARY

> 29\. NEUROLOGY 30.NUCLEAR MEDICINE

> 31\. NURSING 32.NURSING HOME

> 33\. NURSING SERVICE 34.OFFICE OF DIRECTOR

> 35\. PERSONNEL 36.PHARMACY

> 37\. PROSTHETICS 38.PSYCHIATRY

> 39\. PSYCHOLOGY 40.QUALITY ASSURANCE

> \<\<More\>\> This is the end of the 1st page of service listings. The second page is

> continued below.

> Select SERVICE(S): \<RET\>

> Select SERVICE(S): 1-57 All services were selected. The user could have selected 58 to assign all services.

> Select one of the following:

> A (A)dd Group(s)

> D (D)elete Group(s)

> Select ACTION: A (A)dd Group(s)

> DATE ASSIGNED: TODAY// \<RET\> This is the date that the review groups are assigned to employees and appears only when groups or classes are added, not deleted, to the File \#450 records. The date information is used by the deficiency reports.

> 1\. HOSPITAL GROUP

> Select TRAINING Group(s) to be assigned: 1

> This/These group(s) will be assigned by a background Job

> Example 3. Adding and deleting mandatory or required review groups and individual required classes to an employee(s) within a service:

> Select one of the following:

> A (A)ll Employees For a Service

> M (M)ultiple Services - All Employees

> S (S)elected Service Employees

> Select ASSIGNMENT OPTION: S (S)elected Service Employees

> Select one of the following:

> A (A)dd Group(s)

> D (D)elete Group(s)

> E (E)nter/Edit Class(es)

> Example 3a. Associating mandatory review groups with an individual employee:

> Select ACTION: A (A)dd Group(s)

> Select Service: NURSING// \<RET\> The default is the value of the service associated with the user entering this option. You may change the name to reflect the appropriate service you wish to assign to review groups (if you hold the appropriate key).

> DATE ASSIGNED: TODAY// \<RET\> This is the date that the review groups are assigned to employees and appears only when groups or classes are added, not deleted, to the File \#450 records. The date information is used by the deficiency

> 3\. LPNS 4. NURSING ASSISTANT

> 5\. NURSING COORDINATORS 6. NURSE MANAGERS

> 7\. NURSE PRACTITIONERS 8. OPERATING ROOM

> 9\. QUALITY MANAGEMENT 10. RN

> 11\. RN DIALYSIS

> Select TRAINING Group(s) to be assigned: 6

> The review group Nurse Managers is now going to be assigned to 2 individuals.

> Select EMPLOYEE: PAIDEMPLOYEE15,TEN 000-00-0150

> Select Another Employee: PAIDEMPLOYEE15,ONE 000-00-0151

> Select Another Employee: \<RET\>

> The editing of this information is done in real time and is not tasked as the previous selections.

> If the review group has already been assigned, you will see the following display:

> LONG,BABS has already been assigned the Nurse Managers group!

> Select one of the following:

> A (A)ll Employees For a Service

> M (M)ultiple Services - All Employees

> S (S)elected Service Employees

> Example 3b. Disassociating review groups with an individual employee:

> Select ASSIGNMENT OPTION: S (S)elected Service Employees

> Select ACTION: D (D)elete Group(s)

> Select Service: NURSING// \<RET\> The default is the value of the service associated with the user entering this option. You may change the name to reflect the appropriate service you wish to assign to review groups (if you hold the appropriate key).

> 1\. CRITICAL CARE 2. HOSPITAL GROUP

> 3\. LPNS 4. NURSING ASSISTANT

> 5\. NURSING COORDINATORS 6. NURSE MANAGERS

> 7\. NURSE PRACTITIONERS 8. OPERATING ROOM

> 9\. QUALITY MANAGEMENT 10. RN

> 11\. RN DIALYSIS

> Select TRAINING Group(s) to be deleted: 6

> The review group Nurse Managers is now going to be deleted for 2 individuals.

> Select EMPLOYEE: PAIDEMPLOYEE15,TEN 000-00-0150

> Select Another Employee: PAIDEMPLOYEE15,ONE 000-00-0151

> Select Another Employee: \<RET\>

> The editing of this information is done in real time and is not tasked as the previous selections in Example 1 and 2.

> Select one of the following:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>(A)dd Group(s)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>(D)elete Group(s)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p>(E)nter/Edit Class(es)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 3c. Assigning individual classes to an individual employee(s):

> This path allows the user to enter/edit classes (not review groups) and associate them with an individual employee. If the class is a part of a review group assigned to the employee, the class cannot be deleted and a warning message

> displays indicating that the class cannot be deleted. Only independent classes not associated with review groups and assigned to an employee can be deleted.

> Select ACTION: E (E)nter/Edit Class(es)

> Select SERVICE: ISC// \<RET\> This default is the value of the service associated with the user entering this option. You may enter another service associated with the employees, and if you have the appropriate level of access.

> Select EMPLOYEE: PAIDEMPLOYEE15,TEN 000-00-0150

> Select Another Employee: \<RET\>

> LONG,BABS The name of the record the user is editing is displayed before the

> actual editing begins.

> Select MANDATORY CLASS: FIRE AND SAFETY// Entering a question mark first lists all classes assigned to the employee; second listing displays those additional classes you can assign. Enter the class you wish to link with this employee.

> Select MANDATORY CLASS: FIRE AND SAFETY// DEC DCL BASICS

> ...OK? YES// \<RET\> (YES)

> DATE ASSIGNED: TODAY// \<RET\> This is the date that the review groups are assigned to employees and appears only when groups or classes are added, not deleted, to the File \#450 records. The date information is used by the deficiency reports.

> The class is added to the PAID Employee file (#450).

> Example 3d. Deassigning individual classes associated with an employee(s):

> Select SERVICE: ISC// \<RET\> This default is the value of the service associated with the user entering this option. You may enter another service, if you have the appropriate level of access.

> Select EMPLOYEE: PAIDEMPLOYEE15,TEN 000-00-0150

> Select Another Employee: \<RET\>

> PAIDEMPLOYEE15,TEN

> Select MANDATORY CLSS: FIRE AND SAFETY// \<RET\>

> MANDATORY CLASS: FIRE AND SAFETY// @

> SURE YOU WANT TO DELETE THE ENTIRE MANDATORY CLASS? Y (YES)

> Select MANDATORY CLASS: \<RET\>

> Select one of the following:

> A (A)ll Employees For a Service

> M (M)ultiple Services - All Employees

> S (S)elected Service Employees

> If the FIRE AND SAFETY class belonged to a review group associated with the employee, the following display would have appeared.

> Select MANDATORY CLASS: FIRE AND SAFETY// \<RET\>

> MANDATORY CLASS: FIRE AND SAFETY// @

> This class belongs to a mandatory review group and may not be deleted??

> MANDATORY CLASS: FIRE AND SAFETY// \<RET\>

> Select MANDATORY CLASS: \<RET\>

> Select one of the following:

> A (A)ll Employees For a Service

> M (M)ultiple Services - All Employees

> S (S)elected Service Employees

> Menu Access:

> The Assign/Delete Training Groups for Staff/Services is accessed through the

> Package Set-up Menu in the Package Coordinator Menu Option.

> Accrediting Organization

> Description:

> This option allows the user to enter and edit information in the PRSE Class Accreditation Organizations (#452.9) file on accrediting organizations. Data stored in this file is demographic (e.g., organization name, address, and phone number).

> Additional Information:

> Information on national accrediting GROUPs has been pre-loaded into this file. When this file is updated in new versions of the application, a notice will be placed in the release notes so that the new data may be added during the application's installation with the application coordinator's approval.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Package Set-up Menu Option: 4 Accrediting Organization

> Select ACCREDITING ORGANIZATION: ?

> This field contains the name of the organization accrediting the program. The data in this file was preloaded with representative information from national organizations which are known for accrediting programs. Regional and local accrediting agencies should be added to this file.

> ANSWER WITH PRSE EDUCATION ACCREDITATION ORGANIZATIONS ACCREDITATION GROUP

> DO YOU WANT THE ENTIRE 60-ENTRY PRSE EDUCATION ACCREDITATION ORGANIZATIONS LIST? Y

> (YES) CHOOSE FROM:

> SOMEPLACE ASSN FOR OTOLARYNGOLOGY-HEAD & NECK SURGERY SOMEPLACE GROUP OF COLON/RECTAL SURGEONS

> SOMEPLACE GROUP OF EMERGENCY MEDICINE SOMEPLACE GROUP OF NEUROLOGICAL SURGERY SOMEPLACE GROUP OF OPTHALMOLOGY

> SOMEPLACE GROUP OF RADIOLOGY, INC SOMEPLACE GROUP OF THORACIC SURGERY SOMEPLACE COLLEGE OF RADIOLOGY

> SOMEPLACE COLLEGE OF SURGEONS SOMEPLACE DENTAL ASSOCIATION

> SOMEPLACE ORGANIZATION NURSE EXECUTIVES SAMPLE ACADEMY OF DERMATOLOGY

> SAMPLE ACADEMY OF MEDICAL ADMINISTRATORS SAMPLE ACADEMY OF NEUROLOGY

> SAMPLE ACADEMY OF OPTHAMOLOGY

> SAMPLE ACADEMY OF ORTHOPEDIC SURGEONS

> SAMPLE ACADEMY OF PEDIATRICS

> SAMPLE ACADEMY OF PHYSICIAN ASSISTANTS

> SAMPLE ASSOC OF BLOOD BANKS

> SAMPLE ASSOC OF CRITICAL CARE NURSES

> SAMPLE ASSOC OF HEALTH CARE CONSULTANTS

> SAMPLE ASSOC OF HOMES FOR THE AGING

> SAMPLE ASSOC OF NURSE ANESTHETISTS

> SAMPLE ASSOC OF NUTRITIONAL CONSULTANTS

> SAMPLE ASSOC OF OCCUPATIONAL HEALTH NURSES

> SAMPLE ASSOC OF ORAL/MAXILLOFACIAL SURGEONS

> SAMPLE ASSOC OF PASTORAL COUNSELORS

> SAMPLE ASSOCIATION FOR REHABILITATION THERAPY

> SAMPLE ASSOCIATION FOR RESPIRATORY CARE

> SAMPLE BLOOD COMMISSION

> SAMPLE GROUP OF ANESTHESIOLOGY

> SAMPLE GROUP OF DERMATOLOGY

> SAMPLE GROUP OF FAMILY PRACTICE

> SAMPLE GROUP OF INTERNAL MEDICINE

> SAMPLE GROUP OF MEDICAL SPECIALTIES

> SAMPLE GROUP OF NUCLEAR MEDICINE

> SAMPLE DENTAL ASSOCIATION

> SAMPLE DIABETES ASSOC

> SAMPLE HEART ASSOC

> SAMPLE HOSPITAL ASSOC

> SAMPLE LUNG ASSOC

> SAMPLE MEDICAL ASSOCIATION

> SAMPLE MEDICAL TECHNOLOGISTS

> SAMPLE NURSES ASSOCIATION

> SAMPLE ORTHOPEDIC ASSOC

> SAMPLE PHARMACEUTICAL ASSOC

> SAMPLE PHYSICAL THERAPY ASSOC

> SAMPLE PSYCHIATRIC ASSOC

> SAMPLE PSYCHOANALYTIC ASSOC

> SAMPLE PSYCHOLOGICAL ASSOC

> SAMPLE RED CROSS

> SAMPLE SOCIETY OF ANESTHESIOLOGISTS

> SAMPLE SOCIETY OF CLINICAL PATHOLOGISTS

> SAMPLE SOCIETY OF COLON/RECTAL SURGEONS

> SAMPLE SOCIETY OF HOSPITAL PHARMACISTS

> ASSOCIATION FOR PRACTIONERS IN INFECTION CONTROL

> INTRAVENOUS NURSES SOCIETY

> JCAHO

> NAACOG

> NATIONAL LEAGUE FOR NURSING

> WISH

YOU MAY ENTER A NEW PRSE EDUCATION ACCREDITATION ORGANIZATIONS, IF YOU

> Answer must be 3-50 characters in length

> This is an example of a local accrediting body entry.

> Select ACCREDITING ORGANIZATION: PAIDEDORG,ONE

> ARE YOU ADDING 'PAIDEDORG,ONE' AS

> A NEW PRSE EDUCATION ACCREDITATION ORGANIZATIONS (THE 61TH)? Y (YES)

> ACCREDITATION GROUP: PAIDEDORG,ONE Replace \<RET\>

> ADDRESS: ?

> Answer must be 3-30 characters in length

> Enter the address of the accrediting GROUP (3-30 chars). ADDRESS: 1234 WABASH

> ADDRESS2: ?

> Answer must be 3-30 characters in length.

> This field contains the second address for the accrediting organization.

> ADDRESS2: \<RET\>

> CITY: ?

> Answer must be 3-20 characters in length

> Enter the name of the city where the accreditation GROUP is located. CITY: ANYCITY

> STATE: ?

> ANSWER WITH STATE NUMBER, OR NAME, OR ABBREVIATION

> DO YOU WANT THE ENTIRE 62-ENTRY STATE LIST? N (NO)

> STATE: ANYSTATE

> ZIP CODE: ?

> Answer must be 5-11 characters in length

> This field contains the zip code of the accreditation GROUP.

> ZIP CODE: 66666

> TELEPHONE: ?

> Answer must be 4-15 characters in length

> Enter the telephone number of the accrediting GROUP. TELEPHONE: 555-1234

> Select ACCREDITING ORGANIZATION: \<RET\>

> Menu Access:

> The Accrediting Organization option can be accessed through the Package Set-up

> Menu in the Package Coordinator Menu option.

> Presentation Media

> Description:

> This option allows the user to enter or edit types of class media formats stored in the PRSE Education Presentation Media file (#452.5).

> Additional Information:

> Class information on the media formats used in presenting course material for expanded mandatory training, continuing education programs, miscellaneous classes, and ward/unit-location training is tracked in this application. Although the information is not contained in any reports in PAID V. 3.5, the alpha and beta test sites requested that this information be tracked for site specific VA FileMan reports and for reports contained in future versions of the software.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Package Set-up Menu Option: 5 Presentation Media

> Select PRESENTATION MEDIA: ?

> ANSWER WITH PRSE EDUCATION PRESENTATION MEDIA MEDIA SOURCE

> DO YOU WANT THE ENTIRE 20-ENTRY PRSE EDUCATION PRESENTATION MEDIA LIST? Y

> (YES)

> CHOOSE FROM:

> COMPUTER

> DEMO/LECTURE

> FILM

> HANDOUTS/DISCUSSION

> REFERENCE BOOKS

> WRITTEN MATERIALS

> YOU MAY ENTER A NEW PRSE EDUCATION PRESENTATION MEDIA, IF YOU WISH Answer must be 3-20 characters in length

> This field contains the method of media presentation, e.g., video, class room.

> Select PRESENTATION MEDIA: EDUCATION BOOK

> ARE YOU ADDING 'EDUCATION BOOK' AS

> A NEW PRSE EDUCATION PRESENTATION MEDIA (THE 21ST)? Y (YES)

> MEDIA SOURCE: EDUCATION BOOK// ?

> Answer must be 3-20 characters in length

> MEDIA SOURCE: EDUCATION BOOK// \<RET\>

> Select PRESENTATION MEDIA: \<RET\>

> Menu Access:

> The Presentation Media option is accessed through the Package Set-up Menu in the Package Coordinator Menu Option.

> Presenter Supplier

> Description:

> This option allows the user to enter/edit class presenter/supplier information which is stored in the PRSE Education Program/Class Supplier file (#452.2).

> Additional Information:

> The information listed in this file is associated with class/program records created by the options found under the Enter/Edit Class Information menu. Class presenter/supplier data can be found printed on the Individual Training and the Service Training Reports. Information on presenters who are not Department of Veterans Affairs (DVA) employees or training vendors is required on certain DVA training forms (excluding OLDE). Refer to the chapter on Enter Edit Class Information for form names.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Package Set-up Menu Option: 6 Presenter/Supplier

> Select PRESENTER/SUPPLIER: ?

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS SUPPLIER PRESENTER/SUPPLIER

> DO YOU WANT THE ENTIRE 71-ENTRY PRSE EDUCATION PROGRAM/CLASS SUPPLIER LIST? Y

> (YES)

> CHOOSE FROM:

> ACNS ED

> ACOS/EDUCATION

> AHA

> NAMEPLACE EDUCATIONAL TRAINING

> AUSTIN AUTOMATION CENTER

> NAME'S MEDICAL SUPPLIES

> SOMEONE'S EDUCATIONAL PROGRAMS

> EXNAME'S EDUCATIONAL MATERIALS

> DIETETIC SERVICE

> '^' TO STOP: ^

> YOU MAY ENTER A NEW PRSE EDUCATION PROGRAM/CLASS SUPPLIER, IF YOU WISH

> Answer must be 3-30 characters in length

> Enter the name of the vendor or supplier of this program (class).

> This is an example of adding a new supplier to the database.

> Select PRESENTER/SUPPLIER: PAIDEDORG,TWO

> ARE YOU ADDING 'PAIDEDORG,TWO' AS

> A NEW PRSE EDUCATION PROGRAM/CLASS SUPPLIER (THE 72ND)? Y (YES)

> PRESENTER/SUPPLIER: PAIDEDORG,TWO// ?

> Answer must be 3-30 characters in length

> Enter the name of the vendor or supplier of this program (class). PRESENTER/SUPPLIER: PAIDEDORG,TWO// \<RET\>

> ADDRESS: ?

> Answer must be 3-30 characters in length

> Enter the address of the person or vendor presenting the program. ADDRESS: 134 WATER ST

> ADDRESS2: ?

> Answer must be 3-30 characters in length.

> ADDRESS2: SUITE 417

> CITY: ?

> Answer must be 3-20 characters in length

> Enter the name of the city where the supplier/vendor is located. CITY: THECITY

> STATE: ?

> ANSWER WITH STATE NUMBER, OR NAME, OR ABBREVIATION

> DO YOU WANT THE ENTIRE 63-ENTRY STATE LIST? N (NO)

> STATE: THESTATE

> ZIP CODE: ?

> Answer must be 5-11 characters in length

> ZIP CODE: 60503

> TELEPHONE: ?

> Answer must be 4-15 characters in length

> Enter the supplier/vendor's telephone number. TELEPHONE: 555-4444

> Select PRESENTER/SUPPLIER: \<RET\>

> Menu Access:

> The Presenter Supplier option is accessed through the Package Set-up Menu in the Package Coordinator Menu Option.

> Service Reason

> Description:

> This option allows the user to enter or edit a service reason for each of the classes found in the PRSE Student Education Tracking file (#452). Data describing service reasons are stored in the PRSE Svc Reasons For Training file (#452.6).

> Additional Information:

> The purpose of entering service reasons for a class is to document one or more reasons for the service's sponsorship of the class. Two other related fields, purpose of class and class category, track information on VA Central Office required information associated with the class. Only one purpose of class or class category can be associated with a program. Since the service might use different terminology and multiple terms for describing the purpose for the class, the test sites requested that a service purpose field be included in the software. This field is found when editing brief mandatory training, expanded mandatory training,

> continuing education programs, miscellaneous classes, and ward/unit-location training.

> Menu Display:

> Select Package Coordinator Menu Option: 5 Package Set-up Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class File Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Mandatory Training (MI) Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Assign/Delete Training Groups for Staff/Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Accrediting Organization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Presentation Media</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Presenter/Supplier</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Service Reason</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Package Set-up Menu Option: 7 Service Reason

> Select SERVICE REASON: ?

> ANSWER WITH PRSE SVC REASONS FOR TRAINING

> DO YOU WANT THE ENTIRE 49-ENTRY PRSE SVC REASONS FOR TRAINING LIST? Y (YES)

> CHOOSE FROM:

> ANNUAL REVIEW

> CREDENTIALING

> ENHANCE SKILLS

> IMPROVE PRESENT PERFORMANCE

> MANDATORY SAFETY

> '^' TO STOP: ^

> YOU MAY ENTER A NEW PRSE SVC REASONS FOR TRAINING, IF YOU WISH

> Answer must be 2-72 characters in length

> You may enter a reason for giving this class.

> Select SERVICE REASON: DEVELOP NEW TECHNIQUES

> ARE YOU ADDING 'DEVELOP NEW TECHNIQUES' AS

> A NEW PRSE SVC REASONS FOR TRAINING (THE 50TH)? Y (YES)

> REASON FOR EMPLOYEE TRAINING: DEVELOP NEW TECHNIQUES Replace ?

> Answer must be 2-72 characters in length

> SVC REASON: DEVELOP NEW TECHNIQUES Replace \<RET\>

> Select SERVICE REASON: \<RET\>

> Menu Access:

> The Service Reason option is accessed through the Package Set-up Menu of the

> Package Coordinator Menu option.

## Chapter 3: Enter Edit Class Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> This chapter explains the options which create different types of classes and programs (e.g., mandatory training, local continuing education programs, miscellaneous classes and ward/unit-location inservices). These classes are used by the registration, attendance, and report options. Entries are stored in the PRSE Program/Class file (#452.1) and the PRSE Education Registration file (#452.8).

> Additional Information:

> Before a new hospital-wide class/program is entered in the application, a specific service must be designated to coordinate the package. When the initial class record is created for a hospital-wide class, a sponsoring service is identified. Only a user with the PRSE CORD key or a user holding the PRSE SUP key for the sponsoring service can add or change class dates for the hospital-wide class.

> Any user having the Enter/Edit Class Attendance option can enter attendance for a hospital-wide class. Hospital-wide classes by definition are open classes and can be associated with any class type (mandatory inservices, continuing education, etc.).

> Continuing education classes which are not directly sponsored by the medical facility, are considered non-local continuing education classes. Program information for these classes is entered in the software through the option, Create Non-Local CE and Enter Attendance.

> The Education Tracking module captures required information which is used to complete Standard Form 182 and VA Form 5-4691. The form information listed below summarizes the data which is tracked within this software. To assist you in identifying the form requiring the information, the form number has been printed after the colon.

> start date (time not required): 182

> ending date (time not required): 182, 5-4691 class hours on-duty: 182, 5-4691

> class hours off-duty: 182, 5-4691

> government or non-government funded: 182, 5-4691 sponsoring service: 182, 5-4691

> presenter/supplier: 182 program/class category: 182, 5-4691

> The following is a complete non-editable list of program categories

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> EEO COUNSELING SKILLS (Adm.) 45

> EEO TRAINING FOR SUPERVISORS (Sup.) 21

> ELECTRICAL (Trade/Craft) 70

> EMPLOYEE ASSISTANCE PROGRAM (Spe/Tec) 5H

> ENERGY CONSERVATION (Spe/Tec) 5K

> ENGINEERING 3B

> EXECUTIVE SEMINARS CENTERS (Exec.) 1A

> FEDERAL EXECUTIVE INSTITUTE (Exec.) 19

> FILING (Clerical) 67

> FINANCE (Adm.) 49

> GEN'L ORIENTATION TO GOV. OR VA (Trade/Craft) 80

> GRAMMAR (Basic Ed.) 91

> INTERAGENCY - OTHER (Exec.) 1B

> INTERAGENCY INST. FOR FEDERAL HEALTH CARE (Exec.) 13

> KEY PUNCH OPERATOR (Clerical) 65

> LEGAL 33

> LETTER WRITING (Adm.) 4E

> LIPREADING AND SIGN LANGUAGE (Basic Ed.) 93

> LOAN GUARANTY (Spe/Tec) 5D

> MED. ADMIN. SERVICE NATL. TRAINING PROG. (Adm.) 4D

> MEDICAL - DENTISTS 35

> MEDICAL - DIETITIANS 38

> MEDICAL - NURSES 36

> MEDICAL - OTHER PROF. ALLIED HEALTH FIELDS 39

> MEDICAL - PHYSICIANS 34

> MEDICAL - SOCIAL WORKERS 37

> MEDICAL EQUIP. MAINT. AND REPAIR (Trade/Craft) 71

> MEDICAL SUPPORT - FOOD SERVICE WORKER (Spe/Tec) 5A

> MEDICAL SUPPORT - NURSING ASSISTANT (Spe/Tec) 58

> MEDICAL SUPPORT - OTHER (Spe/Tec) 5B

> MEDICAL SUPPORT - SOCIAL WORK ASSISTANT (Spe/Tec) 59

> NON-GOVERNMENT EXECPT 1C, 1D, 1E (Exec.) 1F

> NON-MEDICAL EQUIP. MAINT./REPAIR (Trade/Craft) 72

> OTHER (Adm.) 4F

> OTHER (Basic Ed.) 95

> OTHER (Clerical) 69

> OTHER (Spe/Tec) 5M

> OTHER (Trade/Craft) 78

> PAINTING (Trade/Craft) 73

> PERSONNEL (Adm.) 42

> PLANNING (Adm.) 4C

> PLUMBING AND PIPEFITTING (Trade/Craft) 76

> POLICE SCIENCE (Spec.) 50

> POLICY AND LEGISLATION SEMINAR (Exec.) 12

> POLICY, PROGRAM AND MANAGEMENT ANALYSIS (Adm.) 4B

> PUBLIC OR BUSINESS ADMINISTRATION (Adm.) 41

> REMEDIAL READING (Basic Ed.) 90

> RESPONSIVENESS TRAINING (Spe/Tec) 5L

> SAFETY AND FIRE PROTECTION (Spe/Tec) 5J

> SCIENTIFIC 3A

> SECRETARIAL (Clerical) 62

> SELF-ASSESSMENT AND PLANNING (Exec.) 11

> SHORTHAND (Clerical) 64

> SMOKING CESSATION PROGRAM (Spe/Tec) 5G

> SUP. TRAINING, EXEMPT FROM 40/80 HR REQ. (Sup.) 2B

> SUPPLY AND PROCUREMENT (Spec.) 56

> SYSTEMS ANALYSIS (Adm.) 4A

> TELEPHONE TECHNIQUES (Clerical) 68

> THE BROOKINGS INSTITUTION (Exec.) 1E

> TRAIN./NEW EEO,WOMEN'S PROG/SPAN.SPEAK CORD. (Adm) 44

> TRAINING (Adm.) 43

> TRAINING OTHER THAN 21-25 TOWARD 40-HR REQ. (Sup.) 26

> TRAINING OTHER THAN 21-25 TOWARD 80-HR REQ. (Sup.) 28

> TYPING (Clerical) 63

> UNIVERSITY OR COLLEGE - OTHER (Exec.) 1D

> UNIVERSITY-BASED MID-MANAGEMENT (Exec.) 1C

> VA HEALTH CARE ADMINISTRATOR'S FORUM (Exec.) 14

> VA-OTHER (Exec.) 15

> VETERANS BENEFITS COUNSELING (Spe/Tec) 5E

> WELDING (Trade/Craft) 75

> purpose of class: 182, 5-4691

> The following is a complete non-editable list of class purposes exported in the software:

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> routine/non-routine: 5-4691

> Program Category Field

> The Program Category field provides information that will be used to enter required codes into the PAID system to record training information in the employee's personnel record. The program categories are grouped into broad sections that should make it easier to choose the most appropriate. The following explanations should be used to determine the correct selection:

> Executive and Management

> Education or training in the concepts, principles and theories of such subject matter as public policy formulation and implementation, management principles and practices, quantitative approaches to management, or management

> planning, organizing and controlling.

> Code Program Category

> 11 Self-Assessment and Planning Course

> 12 Policy and Legislation Seminar

> 13 Interagency Institute for Federal Health Care Executives

> 14 VA Health Care Secretary's Forum

> 15 VA - Other

> 16 Basic Training in Federal Labor-Management Relations

> 17 Contract Negotiations - Labor-Management Relations

> 18 Contract Administration - Labor-Management Relations

> 19 Federal Executive Institute

> 1A Executive Seminar Centers

> 1B Interagency - Other

> 1C University based Mid-Management Courses

> 1D University or College Course - Other

> 1E The Brookings Institute

> 1F Non-Government: Other than 1C, 1D and 1E

> Supervisory

> Education or training in supervisory principles and techniques in such subjects as personnel policies and practices (including EEO, merit promotion and labor relations), human behavior and motivation, communication processes in supervision, work planning, scheduling and review and performance evaluation.

> Code Program Category

> 2A Advanced Supervisory Training beyond initial basic training

> 2B Supervisory Training for employees for whom basic training is not required

> Legal, Medical, Scientific or Engineering

> Education or training in the concepts, principles, theories or techniques of such disciplines as law; medicine; the physical, biological, natural, social, or behavioral sciences; education; economics; mathematics and statistics; architecture; or engineering. Medicine applies to professional training in the field of medicine, nursing, dentistry and the allied health fields which are professional in nature, such as hematology and social work.

> Code Program Category

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 57%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>33</p>
</blockquote></th>
<th><blockquote>
<p>Legal</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>Physician</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>Dentist</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>Nurses</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>Social Workers</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>Dietitians</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>Other Professional Allied Health Fields</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Education or training in the concepts, principles and theories of such fields as public or business administration; personnel; training; equal employment opportunity; finance systems analysis; policy, program or management analysis; or planning.

> Code Program Category

> 41 Public or Business Administration

> 42 Personnel

> 43 Training

> 44 Training provided to new EEO, Federal Women's Program and

> Hispanic Employment Program Managers

> 45 Training to develop counseling skills and techniques necessary

> to resolve discrimination complaints informally and to understand the complaints procedure

> 46 Basic Training in Federal Labor Relation

> 47 Contract Negotiations in Federal Labor Relations

> 48 Contract Administration in Federal Labor Relations

> 49 Finance

> 4A Systems Analysis

> 4B Policy, Program or Management Analysis

> 4C Planning

> 4D Medical Administration National Training Program

> 4E Letter Writing

> 4F Other

> Specialty and Technical

> Training of a specialized or technical nature in the methods and techniques of

> such fields as police science; supply and procurement; computer programming; or medical, legal, or scientific support work. Medical support applies to training in allied health fields which are not professional in nature, e.g., nursing assistant and social work assistant.

> Code Program Category

> 50 Police Science

> 56 Supply and Procurement

> 57 Computer Programming

> 58 Nursing Assistant

> 59 Social Work Assistant

> 5A Food Service Worker

> 5B Medical Support - Other

> 5C Adjudication

> 5D Loan Guaranty

> 5E Veterans Benefits Counseling

> 5F Cardiopulmonary Resuscitation (CPR) Training

> 5G Smoking Cessation Program

> 5H Employee Assistance Program

> 5J Safety and Fire Protection

> 5K Energy Conservation

> 5L Responsiveness Training - Training on how to deal better with veterans, their families and dependents by being more sensitive to the feelings involved.

> n

> Training in the knowledge and skills of the following trades or crafts. Code Program Category

> 70 Electrical

> 71 Medical Equipment Repair and Maintenance

> 72 Maintenance and Repair (Other than Medical Equipment)

> 73 Painting

> 74 Carpentry

> 75 Welding

> 76 Plumbing - Pipefitting

> 77 Boiler - Air Conditioning Operation

> 78 Other

> Orientation

> Training of a general nature to provide an understanding of the organization and missions of the Federal Government and the VA or a broad overview and under­ standing of matters of public policy such as the policies relating to equal employment opportunity.

> Code Program Category

> 80 Orientation

> Adult Basic Education

> Education or training to provide basic competence in the following: Code Program Category

> 90 Remedial Reading

> 91 Grammar

> 92 Arithmetic

> 93 Lip Reading and Sign Language

> 94 Braille

> 95 Other

> Refer to Chapter 6 for information on the reports generated from the data entered through the options in this chapter after class attendance is taken.

> Menu Display:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

> 1 Enter/Edit Mandatory Training (MI/Brief)

> 2 Enter/Edit Mandatory Training (MI/Expanded)

> 3 Enter/Edit Local Continuing Education

> 4 Enter/Edit Other/Miscellaneous Training

> 5 Enter/Edit Ward/Unit-Location Training

> Menu Access:

> The Enter/Edit Class Information menu is accessed through the Package

> Coordinator Menu and the Education Tracking Instructor Menu.

> Enter/Edit Mandatory Training (MI/Brief) Description:

> This option allows the user to enter and edit a mandatory training class record which does not contain information required for OLDE reporting requirements. Class information is stored in the PRSE Program/Class file (#452.1) and the PRSE Education Registration file (#452.8).

> Additional Information:

> This option is used to capture basic information on mandatory or required inservices which is not going to be entered into OLDE. The OLDE prompts, program category and purpose, are not displayed through this option. The user should not add additional class dates through the Enter/Edit Mandatory Training (MI/Brief) option after the required OLDE class information has been entered (into the class record) through the Enter/Edit Mandatory Training (MI/Expanded) option. The Enter/Edit Mandatory Training (MI/Brief) option does not store the OLDE information in the PRSE Education Registration file when class data is updated through this option.

> A user should not enter attendance through the Quick Mandatory Training (MI) Update option when a class is established through this option. Attendance should be credited through the Enter/Edit Class Attendance option.

> Menu Display:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

> 1 Enter/Edit Mandatory Training (MI/Brief)

> 2 Enter/Edit Mandatory Training (MI/Expanded)

> 3 Enter/Edit Local Continuing Education

> 4 Enter/Edit Other/Miscellaneous Training

> 5 Enter/Edit Ward/Unit-Location Training

> Screen Prints:

> Select Enter/Edit Class Information Option: 1 Enter/Edit Mandatory Training

> (MI/Brief)

> Select CLASS NAME: ??

> CHOOSE FROM:

> 120-93-001-SANITATION NURSING SERVICE

> ACQUISITION TRAINING NURSING SERVICE

> ADMIN DUTIES NURSING SERVICE

> ADP SECURITY NURSING SERVICE

> ADVANCED LIFE SUPPORT NURSING SERVICE

> ADVANCED MUMPS INFORMATION SYSTEMS CENTER

> BASIC LIFE SUPPORT NURSING SERVICE

> EXPOSURE TO BLOOD PATHOGEN NURSING SERVICE FIRE SAFETY INFORMATION SYSTEMS CENTER

> '^' TO STOP: ^

> YOU MAY ENTER A NEW PRSE PROGRAM/CLASS, IF YOU WISH

> Answer must be 2-53 characters in length

> Select CLASS NAME: CARDIOPULMONARY RESUSCITATION

> ARE YOU ADDING 'CARDIOPULMONARY RESUSCITATION' AS A NEW PRSE PROGRAM/CLASS?

> Y (YES)

> PRSE PROGRAM/CLASS REQUIRED FREQUENCY: 1Y// ??

> This field indicates the mandatory frequency or interval for attending

> the class.

> CHOOSE FROM:

> 1M MONTHLY

> 3M QUARTERLY

> 6M TWICE YEARLY

> 1Y ONCE YEARLY

> 2Y EVERY TWO YEARS

> 3Y EVERY THREE YEARS

> 1T ONE TIME ONLY

> PRSE PROGRAM/CLASS REQUIRED FREQUENCY: 1Y// \<RET\> ONCE YEARLY

> PRSE PROGRAM/CLASS LENGTH HRS: ??

> The number of hours is entered as a number between 0 and 9999.99 and up to 2 decimal digits.

> This field indicates the class duration in hours reported to Austin.

> PRSE PROGRAM/CLASS LENGTH HRS: 4

> OBJECTIVE(S):

> This field is used to define the Program/Class objectives.

> 1\>LEARN BASICS OF CPR.

> 2\>\<RET\>

> EDIT Option: \<RET\>

> SERVICE: NURSING SERVICE// ??

> The service default is the name of the service associated with the user creating the class. This software is using the data stored in the Cost Center/Organization Code field of File \#450 to identify the service. When the class is created by a user assigned to one service and the class is to be associated with another service, enter the name of the sponsoring service after the // (double slash).

> This field associates the class with a specific service.

> CHOOSE FROM: A & M MGT AMBULATORY CARE ANESTHESIOLOGY AUDIOLOGY

> BLIND REHAB CHAPLAIN

> CHIEF OF STAFF DENTAL DERMATOLOGY DIALYSIS DIETETICS DOMICILIARY CARE

> EDUCATION ENGINEERING FISCAL

> GENERAL COUNSEL GERIATRIC RESEARCH IRM

> ISC LABORATORY

> '^' TO STOP: ^

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ??

> This field indicates if the class is opened to individuals outside of the

> service. Closed programs will not be displayed to potential registrants

> from other services.

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> OPEN/CLOSED: CLOSED// \<RET\> If this field entry was open individuals can register

> for this class when: a) the sponsoring service for the class is different from their own

> service, and b) the class type is mandatory/required and the individual is associated with the class through the Assign/Delete Training Groups for Staff/Services option.

> Select START DATE/TIME OF CLASS: JUN 07,1994// ??

> 06-07-1994 The date for the 1st class is the date the class was entered in

> the software. If the date is incorrect, enter a \<RET\> behind the // and at the next

> prompt enter the correct date.

> This is the scheduled start date/time for this program/class.

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 07,1994// \<RET\>

> START DATE/TIME OF CLASS: JUN 07,1994// T-4 (JUN 03,1994)

> ENDING DATE/TIME OF CLASS: ??

> This field contains the scheduled end date/time of this program/class.

> The time is optional.

> ENDING DATE/TIME OF CLASS: T-4 (JUN 03, 1994) PRESENTER/SUPPLIER: ??

> The Presenter/supplier field contains the name of the company or organization who

> supplied the materials for this class. This field looks up on two files: first, the New

> Person file; second, the PRSE Program/Class Supplier file.

> CHOOSE FROM: (Entries from the New Person file).

> PAIDEMPLOYEE15,TWO PAIDEMPLOYEE15,THREE PAIDEMPLOYEE15,FOUR PAIDEMPLOYEE15,FIVE PAIDEMPLOYEE15,SIX PAIDEMPLOYEE15,SEVEN

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins a selection of entries from the PRSE Education Program/ Class Supplier file.

> CHOOSE FROM: (Entries from the PRSE Education Program/Class Supplier file).

> ACOS/E SERVICE

> NAMEPLACE EDUCATIONAL TRAINING

> AUSTIN AUTOMATION CENTER

> NAMES' MED. EDUC. MATERIAL

> SOMEONE'S EDUCATIONAL PROGRAMS

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: ACOS/E SERVICE

> ACOS/E SERVICE

> Is this the one you want? NO// Y (YES)

> SPONSORING SERVICE: HINES ISC//?? The default value is derived from one of two places. When the presenter's name is found in the New Person file (#200), the default is obtained from the information entered in the Enter/Edit Tracking Parameter file (#452.7), specifically the Station Name field. When the presenter's name is found in the PRSE Education Program/Class Supplier file (#452.2), the default is the city and state of the supplier. The Sponsoring Service prompt does not appear if there is no entry in the Presenter/Supplier field.

> Answer must be 3-30 characters in length.

> This field contains the location where the Program/Class is to be held.

> SPONSORING SERVICE: HINES ISC// \<RET\>

> CLASS LIMIT: ?

> CHOOSE FROM:

> This field indicates the maximum number of students that may register for this class session. When this number is met, the user will be given a warning message which indicates that registration is closed.

> CLASS LIMIT: \<RET\> Registration is unlimited since the field is blank. If registration is not being automated through this software, also leave the field blank.

> Select START DATE/TIME OF CLASS: \<RET\>

> After the Start Date multiple has been set up with the required time frames, presenter/supplier, location and class limit, the following additional information is asked. This data is used for all instances of this class regardless of date.

> CLASS HRS DURING ON-DUTY TIME: 4// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> The default value is the class length rounded off to the nearest whole number. This field can also be defined as the number of classroom hours (rounded off to the nearest whole number) attributed to program training during an employee's tour of duty.

> CLASS HRS DURING ON-DUTY TIME: 4// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: 0// \<RET\> Type a Number between 0 and

> 9999, 0 Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> Select SERVICE REASON FOR CLASS: ??

> This field contains the service's reason for having an individual attend this program/class.

> CHOOSE FROM: ANNUAL REVIEW DECENTRALIZED INSERVICE DEVELOP NEW SKILLS DEVELOP NEW TECHNIQUES

> IMPROVE PRESENT PERFORMANCE MAKE UP CLASS

> MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> Select SERVICE REASON FOR CLASS: MANDATORY INSERVICE

> Select SERVICE REASON FOR CLASS: \<RET\>

> The software then permits the user to assign the new class to a mandatory review group associated with the service or to a hospital-wide review group (review groups assigned to the Miscellaneous Service).

> Prior to the following display, the software displays the mandatory training groups associated with the class (if any).

> This class may be assigned to the following Mandatory Training Groups.

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>5. NURSING COORDINATORS</p>
</blockquote></th>
<th><blockquote>
<p>6. NURSE MANAGERS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7. NURSE PRACTITIONERS</p>
</blockquote></td>
<td><blockquote>
<p>8. OPERATING ROOM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. QUALITY MANAGEMENT</p>
</blockquote></td>
<td><blockquote>
<p>10. RN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>11. RN DIALYSIS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select TRAINING Group(s) to be assigned: ?

> Make a selection from the screen display, a range of numbers can be selected by using a HYPHEN, multiple selections can be made by separating them by COMMAS, or '^' to exit.

> E.G. 1 1-2 1,3 1-2,4-5 1,3-4

> Are examples of valid selections

> This class may be assigned to the following Mandatory Training groups.

> Select TRAINING Group(s) to be assigned: 10

> This class has been added to the RN MI review group.

> Menu Access:

> The Enter/Edit Mandatory Training (MI/Brief) option is accessed through the Enter/Edit Class Information option of the Package Coordinator Menu and the Education Tracking Instructor Menu options.

> Enter/Edit Mandatory Training (MI/Expanded) Description:

> This option allows the user to enter or edit mandatory training classes and to store related class OLDE information through a single option. Class information is stored in the PRSE Education Registration file (#452.8), and the PRSE Program/Class Title file (#452.1).

> Additional Information:

> This option is invoked when the user intends to document class information which will be manually entered into the OLDE software at a future time. Data entered through Enter/Edit Mandatory Training (MI/Expanded) option will not be copied into the PRSE Education Registration file when the user updates class date information through the Enter/Edit Mandatory Training (MI/Brief) option.

> Menu Display:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Mandatory Training (MI/Brief)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Mandatory Training (MI/Expanded)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Local Continuing Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Other/Miscellaneous Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Enter/Edit Class Information Option: 2 Enter/Edit Mandatory Training

> (MI/Expanded)

> Select CLASS NAME: ??

> CHOOSE FROM:

> 118 EXPOSURE TO BLOOD PATHOGEN NURSING SERVICE

> ACLS NURSING SERVICE

> ACQUISITION TRAINING NURSING SERVICE

> ADMIN DUTIES NURSING SERVICE

> ADP SECURITY NURSING SERVICE

> ADVANCED LIFE SUPPORT NURSING SERVICE

> ADVANCED MUMPS INFORMATION SYSTEMS CENTER

> BASIC LIFE SUPPORT NURSING SERVICE

> FIRE SAFETY ENGINEERING SERVICE

> '^' TO STOP: ^

> YOU MAY ENTER A NEW PRSE PROGRAM/CLASS, IF YOU WISH

> Answer must be 2-53 characters in length

> Select CLASS NAME: CARDIOPULMONARY RESUSCITATION

> ARE YOU ADDING 'CARDIOPULMONARY RESUSCITATION' AS A NEW PRSE PROGRAM/CLASS?

> Y (YES)

> PRSE PROGRAM/CLASS REQUIRED FREQUENCY: 1Y// ??

> This field indicates the mandatory frequency or interval for attending the class.

> CHOOSE FROM:

> 1M MONTHLY

> 3M QUARTERLY

> 6M TWICE YEARLY

> 1Y ONCE YEARLY

> 2Y EVERY TWO YEARS

> 3Y EVERY THREE YEARS

> 1T ONE TIME ONLY

> PRSE PROGRAM/CLASS REQUIRED FREQUENCY: 1Y// \<RET\> ONCE YEARLY

> PRSE PROGRAM/CLASS LENGTH HRS: ??

> The number of hours is entered as a number between 0 and 9999.99 and up to 2 decimal digits.

> This field indicates the class duration in hours reported to Austin.

> PRSE PROGRAM/CLASS LENGTH HRS: 4

> OBJECTIVE(S):

> 1\>??

> Define the Program/Class objectives (word-processing).

> This field is used to define the Program/Class objectives.

> 1\>LEARN BASICS OF CPR.

> 2\>\<RET\>

> EDIT Option: \<RET\>

> SERVICE: NURSING SERVICE// ??

> The service default is the name of the service associated with the user creating the class. This software is using the data stored in the Cost Center/Organization

> Code field of File \#450 to identify the service. When the class is created by a user assigned to one service and the class is to be associated with another service, enter the name of the sponsoring service after the // (double slash).

> This field associates the class with a specific service. CHOOSE FROM:

> A & M MGT

> AMBULATORY CARE

> ANESTHESIOLOGY

> AUDIOLOGY

> BLIND REHAB

> CHAPLAIN

> CHIEF OF STAFF

> DENTAL

> DERMATOLOGY

> DIALYSIS

> DIETETICS

> DOMICILIARY CARE

> EDUCATION

> ENGINEERING

> FISCAL

> GENERAL COUNSEL

> GERIATRIC RESEARCH

> IRM

> LABORATORY

> '^' TO STOP: ^

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ??

> This field indicates if the class is opened to individuals outside of the

> service. Closed programs will not be displayed to potential registrants

> from other services.

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> OPEN/CLOSED: CLOSED// \<RET\> If this field entry was open individuals can

> register for this class when: a) the sponsoring service for the class is different

> from their own service, and b) the class type is mandatory/required and the individual is associated with the class through the Assign/Delete Training Groups for Staff/Services option.

> Select START DATE/TIME OF CLASS: JUN 07,1994// ??

> 06-07-1994 The date for the 1st class is the date the class was entered in

> the software. If the date is incorrect, enter a \<RET\> behind the // and at the next

> prompt enter the correct date.

> This is the scheduled start date/time for this program/class.

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 07,1994// \<RET\>

> START DATE/TIME OF CLASS: JUN 07,1994// T-4 (JUN 03,1994)

> ENDING DATE/TIME OF CLASS: T-4 (JUN 03, 1994) This field contains the

> scheduled end date/time of this program/class. Time is optional.

> PRESENTER/SUPPLIER: ??

> The Presenter/supplier field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> CHOOSE FROM: (Entries from the New Person file).

> PAIDEMPLOYEE15,TWO PAIDEMPLOYEE15,THREE PAIDEMPLOYEE15,FOUR PAIDEMPLOYEE15,FIVE PAIDEMPLOYEE15,SIX PAIDEMPLOYEE15,SEVEN

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins a selection of entries from the PRSE Education

> Program/Class Supplier file.

> CHOOSE FROM: (Entries from the PRSE Education Program/Class Supplier file).

> ACOS/E SERVICE

> NAMEPLACE EDUCATIONAL TRAINING

> Enter Edit Class Information

> AUSTIN AUTOMATION CENTER NAMES' MED. EDUC. MATERIAL SOMEONE'S EDUCATIONAL PROGRAMS

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: ACOS/E SERVICE

> ACOS/E SERVICE

> Is this the one you want? NO// Y (YES)

> SPONSORING SERVICE: HINES ISC//?? The default value is derived from one of

> two places. When the presenter's name is found in the New Person file (#200), the

> default is obtained from the information entered in the Enter/Edit Tracking Parameter file (#452.7), specifically the Station Name field. When the presenter's name is found in the PRSE Education Program/Class Supplier file (#452.2), the default is the city and state of the supplier. This Sponsoring Service prompt does not appear if the user does not enter a value into the Presenter/Supplier field.

> Answer must be 3-30 characters in length.

> This field contains the location where the Program/Class is to be held.

> SPONSORING SERVICE: HINES ISC// \<RET\>

> CLASS LIMIT: ?

> CHOOSE FROM:

> This field indicates the maximum number of students that may register for this class session. When this number is met, the user will be given a warning message which indicates that registration is closed.

> CLASS LIMIT: \<RET\> Registration is unlimited since the field is blank. If registration is not being automated through this software, also leave the field blank.

> Select START DATE/TIME OF CLASS: \<RET\>

> After the Start Date multiple has been set up with the required time frames, presenter/supplier, location and class limit, the following additional information is asked. This data is used for all instances of this class regardless of date.

> CLASS HRS DURING ON-DUTY TIME: 4// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> The default value is the class length rounded off to the nearest whole number.

> This field can also be defined as the number of classroom hours (rounded off to the nearest whole number) attributed to program training during an employee's tour

> of duty.

> CLASS HRS DURING ON-DUTY TIME: 4// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: 0// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> CLASS HRS DURING OFF-DUTY TIME: 0// \<RET\>

> Select SERVICE REASON FOR CLASS: ??

> This field contains the service's reason for having an individual attend this program/class.

> CHOOSE FROM: ANNUAL REVIEW DECENTRALIZED INSERVICE ENHANCE SKILLS

> MAKE UP CLASS MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> Select SERVICE REASON FOR CLASS: MANDATORY INSERVICE

> Select SERVICE REASON FOR CLASS: \<RET\>

> TYPE OF MEDIA: ??

> This is the type of media used to present this program or class.

> CHOOSE FROM: AUDIO TAPE LECTURE REFERENCE BOOKS SOFTWARE (CAI) VIDEO

> WRITTEN MATERIALS

> The information listed above can be expanded by entering additional media types through the option, Presentation Media which is located in the Package Set-up

> Menu.

> TYPE OF MEDIA: LECTURE PURPOSE OF CLASS: ?

> ANSWER WITH PRSE EMPLOYEE PURPOSE OF TRAINING PAID CODE

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> This field contains the reason this program/class is given; it is a required field. Refer to 3.1 for additional information.

> PURPOSE OF CLASS: NEW TECHNOLOGY CLASS CATEGORY: ??

> This field categorizes a specific class or program.

> CHOOSE FROM:

> ADJUDICATION (Spe/Tec) 5C

> ADVANCED SUPERVISORY TRAINING (Sup.) 2A

> ARITHMETIC (Basic Ed.) 92

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Adm.) 46

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Exec.) 16

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Sup.) 23

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> '^' TO STOP: ^

> This field categorizes a specific class or program; it is a required field. Refer to

> 3.1 for additional information.

> CLASS CATEGORY: 36 MEDICAL - NURSES 36

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// ?

> CHOOSE FROM:

> G GOVERNMENT FUNDED

> E EMPLOYEE FUNDED

> This field indicates if this class is government funded or not. Refer to page 3.1 for additional information.

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// \<RET\>

> CODE FOR OLDE: YES// ?

> CHOOSE FROM:

> Y YES

> N NO

> This field indicates whether or not this class record should be submitted to human resources for manual transmission to Austin, Texas after class attendance is taken.

> CODE FOR OLDE: YES// \<RET\>

> The following information is used in OLDE transmissions.

> ROUTINE/NON-ROUTINE: ??

> This field indicates whether or not the class enhances or does not

> enhance the employee's job qualifications.

> CHOOSE FROM:

> R ROUTINE

> N NON-ROUTINE

> ROUTINE/NON-ROUTINE: R ROUTINE

> The software then permits the user to assign the new class to a mandatory review group associated with the service or to a hospital-wide review group (review groups assigned to the Miscellaneous Service).

> Prior to the following display, the software displays the mandatory training groups associated with the class (if any).

> This class may be assigned to the following Mandatory Training Groups.

> Select TRAINING Group(s) to be assigned: ?

> Make a selection from the screen display, a range of numbers can be selected by using a HYPHEN, multiple selections can be made by separating them by COMMAS, or '^' to exit.

> E.G. 1 1-2 1,3 1-2,4-5 1,3-4

> Are examples of valid selections

> This class may be assigned to the following Mandatory Training groups.

> Select TRAINING Group(s) to be assigned: 9

> This class has been added to the RN MI review group.

> Menu Access:

> The Enter/Edit Mandatory Training (MI/Expanded) option is accessed through

> the Enter/Edit Class Information option of the Package Coordinator Menu and the

> Education Tracking Instructor Menu options.

> Enter/Edit Local Continuing Education

> Description:

> This option allows the user to create and edit a continuing education class presented at the medical center. Data is stored in the PRSE Education Registration file (#452.8), and the PRSE Program Class Title file (#452.1).

> Additional Information:

> The data edited by this option can be found on the Employee Training Reports after attendance is taken.

> Menu Display:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Mandatory Training (MI/Brief)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Mandatory Training (MI/Expanded)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Local Continuing Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit OtherMiscellaneous Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Enter/Edit Class Information Option: 3 Enter/Edit Local Continuing

> Education

> Select CLASS NAME: MAILMAN HELPFUL HINTS This is the name of the program or class. Answer must be 2-53 characters in length

> ARE YOU ADDING 'MAILMAN HELPFUL HINTS' AS A NEW PRSE PROGRAM/CLASS? Y (YES)

> PRSE PROGRAM/CLASS LENGTH HRS: ??

> The number of hours is entered as a number between 0 and 9999.99 and up to 2 decimal digits.

> This field indicates the class duration in hours reported to Austin.

> PRSE PROGRAM/CLASS LENGTH HRS: 3.25

> OBJECTIVE(S):

> 1\>??

> Define the Program/Class objectives (word-processing).

> This field is used to define the Program/Class objectives.

> 1\>LEARN HELPFUL HINTS ON HOW TO USE MAILMAN.

> 2\>\<RET\>

> EDIT Option: \<RET\>

> The service default is the name of the service associated with the user creating the class. The software is using the data stored in the Cost Center/Organization Code field of File \#450 to identify the service. When the class is created by a user assigned to one service and the class is to be associated with another service, enter the name of the sponsoring service after the // (double slash).

> SERVICE: NURSING SERVICE// ??

> This field associates the class with a specific service.

> CHOOSE FROM: A & M MGT AMBULATORY CARE ANESTHESIOLOGY AUDIOLOGY

> BLIND REHAB CHAPLAIN

> CHIEF OF STAFF DENTAL DERMATOLOGY DIALYSIS DIETETICS DOMICILIARY CARE EDUCATION ENGINEERING FISCAL

> GERIATRIC RESEARCH IRM

> LABORATORY

> '^' TO STOP: ^

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ??

> This field indicates if the class is opened to individuals outside of the

> service. Closed programs will not be displayed to potential registrants

> from other services.

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> OPEN/CLOSED: CLOSED// \<RET\> If this field entry was open, individuals outside the

> service could register for the class.

> Select START DATE/TIME OF CLASS: JUN 07,1994// ?

> ANSWER WITH START DATE/TIME OF CLASS:

> 06-07-1994 The date of the 1st class is the date the class was entered in the

> software. If the date is incorrect, enter a \<RET\> behind the // and at the next

> prompt enter the correct date.

> YOU MAY ENTER A NEW START DATE/TIME OF CLASS, IF YOU WISH

> Enter the date of this program or class, time is required if the

> class is to be tracked by personnel

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 07,1994// \<RET\>

> START DATE/TIME OF CLASS: JUN 07,1994// ?

> Enter Edit Class Information

> Enter the date of this program or class, time is required if the class is to be tracked by personnel

> START DATE/TIME OF CLASS: JUN 07,1994// \<RET\>

> ENDING DATE/TIME OF CLASS: T (JUN 07, 1994) This field contains the

> scheduled end date/time of this program/class. Time is optional.

> PRESENTER/SUPPLIER: ??

> The Presenter/supplier field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> CHOOSE FROM: PAIDEDPRESENTER,ONE PAIDEDPRESENTER,TWO PAIDEDPRESENTER,THREE PAIDEDPRESENTER,FOUR PAIDEDPRESENTER,FIVE

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins a selection of entries from the PRSE Education Program/Class Supplier file.

> CHOOSE FROM: ACOS/E SERVICE

> NAMEPLACE EDUCATIONAL TRAINING AUSTIN AUTOMATION CENTER NAMES' MED. EDUC. MATERIAL SOMEONE'S EDUCATIONAL PROGRAMS

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message displays:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message displays:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: PAIDEDPRESENTER,SIX

> Is this the one you want? NO// Y (YES)

> SPONSORING SERVICE: PAIDEDSPONSOR,ONE// ? The default value is derived from one of

> two places. When the presenter's name is found in the New Person file (#200), the

> default is obtained from the information entered in the Enter/Edit Tracking Parameter file (#452.7), specifically the Station Name field. When the presenter's name is found in the PRSE Education Program/Class Supplier file (#452.2), the default is the city and state of the supplier. The Sponsoring Service prompt does not appear if there is no entry in the Presenter/Supplier field.

> Answer must be 3-30 characters in length.

> This field contains the location where the Program/Class is to be held. SPONSORING SERVICE: PAIDEDSPONSOR,ONE// \<RET\>

> CLASS LIMIT: ?

> CHOOSE FROM:

> This field indicates the maximum number of students that may register for this class session. When this number is met, the user will be given a warning message which indicates that registration is closed.

> CLASS LIMIT: \<RET\> Registration is unlimited since the field is blank. If registration is not being automated through this software, also leave the field blank.

> Select START DATE/TIME OF CLASS: \<RET\>

> After the Start Date multiple has been set up with the required time frames, presenter supplier, location and class limit, additional information is asked. This data is used for all instances of this class regardless of date.

> ACCREDITING ORGANIZATION: ??

> This field contains the name of the organization accrediting the program.

> CHOOSE FROM: AACCN

> SAMPLE CRITICAL CARE NURSING SAMPLE DIETETIC ASSOCIATION SAMPLE MEDICAL ASSOCIATION SAMPLE NURSES ASSOCIATION SAMPLE RED CROSS

> DELAWARE NURSES ASSOCIATION ILLINOIS NURSES ASSOCIATION IOWA GROUP OF NURSING

> TEXAS NURSES ASSOCIATION

> ACCREDITING ORGANIZATION: SAMPLE NURSES ASSOCIATION

> CLASS HRS DURING ON-DUTY TIME: 3// ?

> Type a Number between 0 and 9999, 0 Decimal Digits

> The default value is the class length rounded off to the nearest whole number. This field can also be defined as the number of classroom hours (rounded off to the nearest whole number) attributed to program training during an employee's tour of duty.

> CLASS HRS DURING ON-DUTY TIME: 3// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: 0// \<RET\> Type a Number between 0 and

> 9999, 0 Decimal Digits. This field indicates the number of classroom hours for the

> program when an employee attends a program during off-duty time.

> CEUs: ?

> Type a Number between 0 and 30, 1 Decimal Digit

> Enter Edit Class Information

> This is the number of continuing education units associated with the class.

> CEUs: 3

> CONTACT HOURS: ?

> Type a Number between 0 and 9999.99, 2 Decimal Digits

> This field contains the number of contact hours associated with this program.

> CONTACT HOURS: 3

> Select SERVICE REASON FOR CLASS: ??

> This field contains the service's reason for having an individual attend this program/class.

> CHOOSE FROM: ANNUAL REVIEW DECENTRALIZED INSERVICE ENHANCE SKILLS

> IMPROVE PRESENT PERFORMANCE MAKE UP CLASS

> MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> Select SERVICE REASON FOR CLASS: ENHANCE SKILLS

> Select SERVICE REASON FOR CLASS: \<RET\>

> TYPE OF MEDIA: ??

> This is the type of media used to present this program or class.

> CHOOSE FROM: AUDIO TAPE CLASSROOM FILM

> HANDOUTS/DISCUSSION LECTURE/DEMO/ROLE

> The information listed above can be expanded by entering additional media types through the option, Presentation Media which is located in the Package Set-up Menu.

> TYPE OF MEDIA: LECTURE/DEMO/ROLE PURPOSE OF CLASS: ?

> CHOOSE FROM:

> ADULT BASIC EDUCATION 9

> DEVELOP NEW SKILLS 6

> EMPLOYEE FINANCED 10

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> This field contains the reason this program/class is given; it is a required field. Refer to 3.1 for additional information.

> PURPOSE OF CLASS: MEET FUTURE STAFFING NEEDS CLASS CATEGORY: ??

> This field categorizes a specific class or program.

> CHOOSE FROM:

> ADJUDICATION (Spe/Tec) 5C

> ADVANCED SUPERVISORY TRAINING (Sup.) 2A

> ARITHMETIC (Basic Ed.) 92

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Adm.) 46

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Exec.) 16

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Sup.) 23

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> '^' TO STOP: ^

> This field categorizes a specific class or program; it is a required field. Refer to 3.1 for additional information.

> CLASS CATEGORY: 36 MEDICAL - NURSES 36

> GOVERNMENT FUNDED: G// ?

> CHOOSE FROM:

> G GOVERNMENT FUNDED

> E EMPLOYEE FUNDED

> This field indicates if this class is government funded or not. Refer to 3.1 for additional information.

> GOVERNMENT FUNDED: G// \<RET\> GOVERNMENT FUNDED CODE FOR OLDE: YES// ?

> CHOOSE FROM:

> Y YES

> N NO

> This field indicates whether or not this class record should be submitted to personnel for transmission to Austin, Texas after class attendance is taken.

> CODE FOR OLDE: YES// Y YES

> The following information is used in OLDE transmissions.

> ROUTINE/NON-ROUTINE: ??

> This field indicates whether or not the class enhances or does not

> enhance the employee's job qualifications.

> CHOOSE FROM:

> R ROUTINE

> N NON-ROUTINE

> ROUTINE/NON-ROUTINE: R ROUTINE

> Menu Access:

> The Enter/Edit Local Continuing Education option is accessed through the Enter/Edit Class Information option of the Package Coordinator Menu and the Education Tracking Instructor Menu options.

> Enter/Edit Other/Miscellaneous Training

> Description:

> This option allows the entering and editing of miscellaneous training inservice classes which are not categorized as required classes, continuing education or location specific classes. Data is stored in the PRSE Education Registration file (#452.8), and the PRSE Program Class Title file (#452.1).

> Additional Information:

> The data edited by this option can be found on the Employee Training Reports after class attendance is taken.

> Screen Prints:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Mandatory Training (MI/Brief)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Mandatory Training (MI/Expanded)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Local Continuing Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Other/Miscellaneous Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Enter/Edit Class Information Option: 4 Enter/Edit Other/Miscellaneous

> Training

> Select CLASS NAME: ??

> CHOOSE FROM:

> BASIC MAILMAN IRM

> BASIC SUPERVISORY TRAINING NURSING SERVICE

> BUDGET PLANNING NURSING SERVICE

> CHEM JOURNAL LAB SERVICE

> COMPUTER TRAINING FOR NURSING NURSING SERVICE

> E-MAIL LAB SERVICE

> This is the name of the program or class. Select CLASS NAME: BASIC FILEMAN

> ARE YOU ADDING 'BASIC FILEMAN' AS A NEW PRSE PROGRAM/CLASS? Y (YES) PRSE PROGRAM/CLASS LENGTH HRS: ??

> This field indicates the class duration in hours reported to Austin.

> The number of hours is entered as a number between 0 and 9999.99 and up to 2 decimal digits.

> PRSE PROGRAM/CLASS LENGTH HRS: 4

> OBJECTIVE(S):

> 1\>??

> Define the Program/Class objectives (word-processing).

> This field is used to define the Program/Class objectives.

> 1\>INTRODUCTION TO BASIC

> 2\>\<RET\>

> EDIT Option: \<RET\>

> SERVICE: NURSING SERVICE// ??

> This field associates the class with a specific service.

> The service default is the name of the service associated with the user creating the class. This software is using the data stored in the Cost Center/Organization Code field of File \#450 to identify the service. When the class is created by a user assigned to one service and the class is to be associated with another service, enter the name of the sponsoring service after the // (double slash).

> CHOOSE FROM: A & M MGT AMBULATORY CARE ANESTHESIOLOGY AUDIOLOGY

> BLIND REHAB CHAPLAIN

> CHIEF OF STAFF DENTAL DERMATOLOGY DIALYSIS DIETETICS DOMICILIARY CARE EDUCATION ENGINEERING FISCAL

> GENERAL COUNSEL GERIATRIC RESEARCH IRM

> LABORATORY

> '^' TO STOP: ^

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ??

> This field indicates if the class is opened to individuals outside of the

> service. Closed programs will not be displayed to potential registrants

> from other services.

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> OPEN/CLOSED: CLOSED// OPEN Since the value for this field is open, individuals

> outside the service can register for the class.

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 7,1994// ??

> ANSWER WITH START DATE/TIME OF CLASS:

> 06-07-1994 The date of the 1st class is the date the class was entered in

> the software. If the date is incorrect, enter a \<RET\> behind the // and at the next

> prompt enter the correct date.

> This is the scheduled start date/time for this program/class.

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 7,1994// \<RET\>

> START DATE/TIME OF CLASS: JUN 7,1994// T-1 (JUN 6,1994)

> ENDING DATE/TIME OF CLASS: T-1 (APR 13, 1994) This field contains the

> scheduled end date/time of this program/class. Time is optional.

> PRESENTER/SUPPLIER: ??

> The Presenter/supplier field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> CHOOSE FROM: (Entries from the New Person file).

> PAIDEDPRESENTER,SEVEN PAIDEDPRESENTER,EIGHT PAIDEDPRESENTER,FIVE PAIDEDPRESENTER,NINE PAIDEDPRESENTER,TEN PAIDEDPRESENTER1,ONE PAIDEDPRESENTER1,TWO PAIDEDPRESENTER1,THREE

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins a selection of entries from the PRSE Education Program/Class Supplier file.

> CHOOSE FROM: (Entries from the PRSE Education Program/Class Supplier file).

> ACOS/EDUCATION AHA

> NAMEPLACE EDUCATIONAL TRAINING AUSTIN AUTOMATION CENTER NAMES' MED. EDUC. MATERIAL SOMEONE'S EDUCATIONAL PROGRAMS

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: PAIDEDPRESENTER1,FOUR

> Is this the one you want? NO// Y (YES)

> SPONSORING SERVICE: PAIDEDSPONSOR,ONE// ?? The default value is derived from one of two places. When the presenter's name is found in the New Person file (#200), the

> default is obtained from the information entered in the Enter/Edit Tracking Parameter file (#452.7), specifically the Station Name field. When the presenter's name is found in the PRSE Education Program/Class Supplier file (#452.2), the default is the city and state of the supplier. The Sponsoring Service prompt does not appear if there is no entry in the Presenter/Supplier field.

> Answer must be 3-30 characters in length.

> This field contains the location where the Program/Class is to be held.

> SPONSORING SERVICE: PAIDEDSPONSOR,ONE// \<RET\>

> CLASS LIMIT: ?

> CHOOSE FROM:

> This field indicates the maximum number of students that may register for this class session. When this number is met, the user will be given a warning message which indicates that registration is closed.

> CLASS LIMIT: \<RET\> Registration is unlimited since the field is blank. If registration is not being automated through this software, also leave the field blank.

> Select START DATE/TIME OF CLASS: \<RET\>

> After the Start Date multiple has been set up with the required time frames, presenter/supplier, location and class limit, additional information is asked. This data is used for all instances of this class regardless of date.

> CLASS HRS DURING ON-DUTY TIME: 4// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> The default value is the class length rounded off to the nearest whole number. This field can also be defined as the number of classroom hours (rounded off to the nearest whole number) attributed to program training during an employee's tour of duty.

> CLASS HRS DURING ON-DUTY TIME: 4// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: 0// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> CLASS HRS DURING OFF-DUTY TIME: 0// \<RET\>

> Select SERVICE REASON FOR CLASS: ??

> This field contains the service's reason for having an individual attend this program/class.

> CHOOSE FROM:

> ANNUAL REVIEW

> CLASS IS MANDATORY

> DECENTRALIZED INSERVICE

> DEVELOP NEW SKILL

> IMPROVE PRESENT PERFORMANCE

> MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> Select SERVICE REASON FOR CLASS: ENHANCE SKILLS Select SERVICE REASON FOR CLASS: \<RET\>

> TYPE OF MEDIA: CLASS ROOM// ??

> This is the type of media used to present this program or class.

> CHOOSE FROM: AUDIO TAPE CLASSROOM LECTURE DEMO/LECTURE

> HANDOUTS/DISCUSSION VIDEO

> The information listed above can be expanded by entering additional media types through the option, Presentation Media which is located in the Package Set-up Menu.

> TYPE OF MEDIA: CLASSROOM LECTURE PURPOSE OF CLASS: ?

> CHOOSE FROM:

> ADULT BASIC EDUCATION 9

> DEVELOP NEW SKILLS 6

> EMPLOYEE FINANCED 10

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> This field contains the reason this program/class is given; it is a required field. Refer to 3.1 for additional information.

> PURPOSE OF CLASS: DEVELOP NEW SKILLS CLASS CATEGORY: TRAINING (Adm.)// ??

> This field categorizes a specific class or program.

> CHOOSE FROM:

> ADJUDICATION (Spe/Tec) 5C

> ADVANCED SUPERVISORY TRAINING (Sup.) 2A

> ARITHMETIC (Basic Ed.) 92

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Adm.) 46

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Exec.) 16

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Sup.) 23

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> '^' TO STOP: ^

> This field categorizes a specific class or program; it is a required field. Refer to 3.1 for additional information.

> CLASS CATEGORY: 36 MEDICAL - NURSES 36

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// ?

> CHOOSE FROM:

> G GOVERNMENT FUNDED

> E EMPLOYEE FUNDED

> This field indicates if this class is government funded or not. Refer to 3.1 for additional information.

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// \<RET\> GOVERNMENT FUNDED CODE FOR OLDE: NO// ?

> CHOOSE FROM:

> Y YES

> N NO

> This field indicates whether or not this class should be submitted to human resources for transmission to Austin, Texas after class attendance is taken.

> CODE FOR OLDE: NO// Y YES

> The following information is used in OLDE transmissions.

> ROUTINE/NON-ROUTINE: ??

> This field indicates whether or not the class enhances or does not

> enhance the employee's job qualifications.

> CHOOSE FROM:

> R ROUTINE

> N NON-ROUTINE

> ROUTINE/NON-ROUTINE: R ROUTINE

> Menu Access:

> The Enter/Edit Other /Miscellaneous Training option is accessed through the Enter/Edit Class Information option of the Package Coordinator Menu and the Education Tracking Instructor Menu options.

> Enter/Edit Ward/Unit-Location Training

> Description:

> This option allows the user to create and edit inservice programs/classes associated with a specific medical center nursing location. Crediting attendance is also permitted. Data is stored in the PRSE Education Registration file (#452.8), and the PRSE Program Class Title file (#452.1).

> Additional Information:

> The data edited by this option can be found on the Employee Training Reports after attendance is taken.

> Menu Display:

> Select Package Coordinator Menu Option: 1 Enter/Edit Class Information

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Mandatory Training (MI/Brief)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Mandatory Training (MI/Expanded)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Local Continuing Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Other/Miscellaneous Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Enter/Edit Class Information Option: 5 Enter/Edit Ward/Unit-Location

> Training

> Select CLASS NAME: ??

> CHOOSE FROM:

> 3W BIOETHICS NURSING SERVICE

> 5W NAME IV PUMPS NURSING SERVICE

> 5W IVAC 4200 NURSING SERVICE

> 7E CHART AUDIT NURSING SERVICE

> 3W DIET MANUAL TRAINING ENGINEERING

> This is the name of the program or class. Select CLASS NAME: SICU UNIT SAFETY

> ARE YOU ADDING 'SICU UNIT SAFETY' AS A NEW PRSE PROGRAM/CLASS? Y (YES) PRSE PROGRAM/CLASS LENGTH HRS: ??

> The number of hours is entered as a number between 0 and 9999.99 and up to 2 decimal digits.

> This field indicates the class duration in hours reported to Austin.

> PRSE PROGRAM/CLASS LENGTH HRS: 2

> OBJECTIVE(S):

> 1\>??

> Define the Program/Class objectives (word-processing).

> This field is used to define the Program/Class objectives.

> 1\>LEARN SAFETY IN THE UNIT

> 2\>\<RET\>

> EDIT Option: \<RET\>

> SERVICE: NURSING SERVICE// ??

> This field associates the class with a specific service.

> The service default is the name of the service associated with the user creating the class. The software is using the data stored in the Cost Center/Organization Code field of File \#450 to identify the service. When the class is created by a user assigned to one service and the class is to be associated with another service, enter the name of the sponsoring service after the // (double slash).

> CHOOSE FROM: A & M MGT AMBULATORY CARE ANESTHESIOLOGY AUDIOLOGY

> BLIND REHAB CHAPLAIN

> CHIEF OF STAFF DENTAL DERMATOLOGY DIALYSIS DIETETICS DOMICILIARY CARE

> '^' TO STOP: ^

> SERVICE: NURSING SERVICE// \<RET\>

> OPEN/CLOSED: CLOSED// ??

> This field indicates if the class is opened to individuals outside of the

> service. Closed programs will not be displayed to potential registrants

> from other services.

> CHOOSE FROM:

> 1 CLOSED

> 0 OPEN

> OPEN/CLOSED: CLOSED// \<RET\> If this field entry was open, individuals outside the

> service could register for the class.

> Select START DATE/TIME OF CLASS: JUN 7,1994// ??

> 06-07-1994 The date of the 1st class is the date the class was entered in the

> software. If the date is incorrect, enter a \<RET\> behind the // and at the next

> prompt enter the correct date.

> This is the scheduled start date/time for this program/class.

> Enter the date of this program or class. Date (minimum of month/year) is required; entry of time is strongly suggested if the class is to be tracked by the calendar report.

> Select START DATE/TIME OF CLASS: JUN 7,1994// \<RET\>

> START DATE/TIME OF CLASS: JUN 7,1994// T-2 (JUN 05, 1994)

> ENDING DATE/TIME OF CLASS: T-2 (JUN 05,1994) This field contains the scheduled end date/time of this program/class. Time is optional.

> PRESENTER/SUPPLIER: ??

> The Presenter/supplier field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> CHOOSE FROM: (Entries from the New Person file).

> PAIDEDPRESENTER,SEVEN PAIDEDPRESENTER,EIGHT PAIDEDPRESENTER,FOUR PAIDEDPRESENTER,FIVE PAIDEDPRESENTER,NINE

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins the display of entries from the PRSE Education Program/Class Supplier file.

> CHOOSE FROM: (Entries from the PRSE Education Program/Class Supplier file).

> ACME ACOS/EDUCATION AHA

> AUSTIN AUTOMATION CENTER NAMES' MED. EDUC. MATERIAL SOMEONE'S EDUCATIONAL PROGRAMS

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: ACME

> ACME

> Is this the one you want? NO// Y (YES) CLASS LIMIT: ?

> CHOOSE FROM:

> 0 REGISTRATION CLOSED

> 1-999 REGISTRATION RESTRICTED TO NUMBER INDICATED (0 decimal digits)

> BLANK REGISTRATION UNLIMITED

> This field indicates the maximum number of students that may register for this class session. When this number is met, the user will be given a warning message which indicates that registration is closed.

> CLASS LIMIT: \<RET\> Registration is unlimited since the field is blank. If registration is not being automated through this software, also leave the field blank.

> Select START DATE/TIME OF CLASS: \<RET\>

> After the Start Date multiple has been set up with the required time frames, presenter/supplier, location and class limit, additional information is asked. This data is used for all instances of this class regardless of date.

> CLASS HRS DURING ON-DUTY TIME: 2// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> The default value is the class length rounded off to the nearest whole number. This field can also be defined as the number of classroom hours (rounded off to the nearest whole number) attributed to program training during an employee's tour of duty.

> CLASS HRS DURING ON-DUTY TIME: 2// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: 0// ?

> Type a Number between 0 and 9999, 0 Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> CLASS HRS DURING OFF-DUTY TIME: 0// \<RET\>

> Select SERVICE REASON FOR CLASS: ??

> This field contains the service's reason for having an individual attend this program/class.

> CHOOSE FROM:

> DECENTRALIZED INSERVICE

> DEVELOP NEW SKILLS

> IMPROVE PRESENT PERFORMANCE

> MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> Select SERVICE REASON FOR CLASS: DEVELOP NEW SKILLS Select SERVICE REASON FOR CLASS: \<RET\>

> Do you want to credit students for attending this class? YES// ??

> Answer YES or NO.

> Do you want to credit students for attending this class? YES// \<RET\> (YES) Select START DATE/TIME OF CLASS: ??

> CHOOSE FROM:

> 06-05-1994

> This is the scheduled start date/time of the class.

> Enter Edit Class Information

> Select START DATE/TIME OF CLASS: 6-5 JUN 5, 1994

> Select Student Name: ??

> CHOOSE FROM:

> PAIDEDPRESENTER,TWO 000000002

> PAIDEDPRESENTER,THREE 000000003

> PAIDEDPRESENTER,FOUR 000000004

> PAIDEDPRESENTER,FIVE 000000005

> PAIDEDPRESENTER,NINE 777655566

> '^' TO STOP: ^

> Select Student Name: PAIDEDPRESENTER,SIX 000-00-0006

> 1\. Example: Crediting attendance

> Do you want to credit PAIDEDPRESENTER,SIX - NURSING SERVICE for attending UNIT SAFETY? YES// \<RET\> (YES)

> PAIDEDPRESENTER,SIX UNIT SAFETY JUN 5, 1994

> The above display indicates that M. SOMEONE was given credit for the class.

> 2\. Example: Deleting attendance

> Enter the name of the person whose record you want to delete.

> Select Student Name: PAIDEMPLOYEE15,ONE 000000151

> PAIDEMPLOYEE15,ONE completed UNIT SAFETY on this date

> Do you want to delete this record? NO// \<RET\>

> If the user enters YES after the above prompt, the following message would appear:

> PAIDEMPLOYEE15,ONE \*\*DELETED\*\* Select Student Name: \<RET\>

> Menu Access:

> The Enter/Edit Ward/Unit-Location Training option is accessed through the Enter/Edit Class Information option of the Package Coordinator Menu and the Education Tracking Instructor Menu options.

Student Registration

## Chapter 4: Class Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> This chapter explains the options which allow potential program attendees to register for future classes as identified in the PRSE Program/Class file (#452.1) and the PRSE Education Registration file (#452.8). The two options which regulate class registration are Class Registration Enter/Delete and Self Registration Enter/Edit.

> Additional Information:

> Class names are displayed with the sponsoring service's name. Registration can only be processed when appropriate class dates have been associated with a class through one of the Enter/Edit Class Information Menu options. If the software does not recognize the class name, check the entries to see if a present or future date is associated with the class. Both registration options display a message when the maximum number of registrants (stored in the class limit field) has been reached. Crediting attendance at classes is done through the options found under the Attendance Menu option. Individuals do not have to be preregistered in a class for attendance to be credited.

> Menu Display:

> Select Education Tracking System Menu Option: 2 Package Coordinator Menu

> 1 Enter/Edit Class Information ...

> 2 Class Registration Enter/Delete

> 3 Attendance Menu ...

> 4 Reports Menu ...

> 5 Package Set-up Menu ...

> Menu Access:

> These two registration options are found in two different menus. The Class Registration Enter/Delete option is accessed through the Package Coordinator menu and the Education Tracking Instructor menu. The Self Registration Enter/Edit option is found in the Employee Menu.

> Student Registration

> Class Registration Enter/Delete

> Description:

> This option allows an individual to register students for classes. This option stores the names of the registrants in the PRSE Education Registration file (#452.8).

> Additional Information:

> A person can be registered for a class only if the class has a present or future date; registration for classes in the past is not allowed. Individuals do not need to be preregistered for a class in order for class attendance to be taken. The user holding the PRSE CORD key can see classes for all services (closed or open) and

> can register any person for any class regardless of service or class restrictions. Names of those individuals registered for classes can be printed through the

> Class Registration Roster report. The user holding the PRE SUP key can register any employee for a class sponsored by his/her service.

> Menu Display:

> Select Education Tracking System Menu Option: 2 Package Coordinator Menu

> 1 Enter/Edit Class Information ...

> 2 Class Registration Enter/Delete

> 3 Attendance Menu ...

> 4 Reports Menu ...

> 5 Employee Education Tracking Menu ...

> 6 Package Set-up Menu ...

> Screen Prints:

> Select Package Coordinator Menu Option: 2 Class Registration Enter/Delete

> Select one of the following:

> R Class Registration Calendar Report (Refer to the Reports section for an explanation of the Class Registration Calendar Report)

> S Student Registration

> Choose a Selection from the above choices: Student Registration

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> 4.2

PAID V. 4.0 User Manual March 2018

Student Registration

> A All

> Select Sort Parameter: ?

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> This field preselects the type of class for the purpose of decreasing the listing of classes displayed in the help. If this sort was not placed in the software, the listing of classes would be enormous and definitely not user friendly.

> Select Sort Parameter: Continuing Education

> CLASS NAME: ?

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR

> TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> Displayed below is a list of all classes which are open for registration based on the above class type.

> CHOOSE FROM:

> 5TH NURSING INFORMATICS NURSING SERVICE

> CLASS NAME: 5TH NURSING INFORMATICS NURSING SERVICE Select DATE: JUN 19, 1994// ?

> ANSWER WITH START DATE/TIME OF CLASS

> The class must have a present or future date to be able to register for it. If you want to add a new date, exit this option and enter a new date through the appropriate Enter/Edit Class Information Menu option. Remember that you must have the appropriate level of access to edit the class information.

> CHOOSE FROM:

> 06-19-1994

> Select DATE: JUN 19, 1994// \<RET\> JUN 19, 1994

> 1\. Adding a name to the registration list:

> Enter STUDENT NAME: ?

> ANSWER WITH STUDENT NAME

> The names displayed immediately before the New Person listing, are the names of individuals who have registered for the class.

> CHOOSE FROM:

> PAIDEDPRESENTER1,FIVE NURSING SERVICE

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE NEW PERSON LIST? Y (YES)

> CHOOSE FROM: PAIDPRESENTER,SEVEN PAIDEDPRESENTER,EIGHT PAIDEDPRESENTER,FOUR PAIDEDPRESENTER,FIVE PAIDEDPRESENTER,NINE

> '^' TO STOP: ^

> Enter STUDENT NAME: PAIDEMPLOYEE15,ONE

> Do you want to register PAIDEMPLOYEE15,ONE - NURSING SERVICE for 5TH NURSING INFORMATICS? YES// \<RET\> (YES)

> Enter STUDENT NAME: \<RET\> Additional names can be entered here.

> When the name of a registrant is not an employee (the name is not found in the PRSE Student Education Tracking file (#452)) and not previously entered in the New Person file (#200), the following information is displayed.

> Enter STUDENT NAME: PAIDEMPLOYEE15,EIGHT

> Is PAIDEMPLOYEE15,EIGHT, being added to the NEW PERSON (#200) File as a non VA

> employee? YES// \<RET\>

> NEW PERSON SSN: 000000158

> The software internally checks to see whether or not a social security number has been entered for the registrant. If there is none, the application prompts the user to enter the SSN. If the registrant was previously entered in the New Person file, the software would automatically allow the user to enter the name and register the individual. If the name is not in File \#200, the name of the individual must be placed in File \#200 and the name re-entered into the Class Registration Enter/ Delete option to register the individual.

> After the name of the individual is entered into File \#200, it must again be re­

> entered to register him for the class.

> Enter STUDENT NAME: PAIDEMPLOYEE15,EIGHT Or the user can enter space bar, return.

> Do you want to register PAIDEMPLOYEE15,EIGHT - NON Employee for 5TH NURSING INFORMATICS? YES// Y (YES)

> 2\. Deleting a name from the registration list:

> CLASS NAME: Enter the name of the class.

> Enter STUDENT NAME: ?

> ANSWER WITH STUDENT NAME

> The names displayed immediately before the New Person listing, are the names of individuals who have registered for the class.

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>CHOOSE FROM:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE15,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE15,NINE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE15,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE15,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>MISCELLANEOUS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE 611-ENTRY NEW PERSON LIST? N (YES)

> Enter STUDENT NAME: PAIDEMPLOYEE15,EIGHT

> PAIDEMPLOYEE15,EIGHT is currently Registered for this 5TH NURSING INFORMATICS Class!

> Do you want to delete this record? NO// YES (YES)

> PAIDEMPLOYEE15,EIGHT \*\* DELETED\*\* Enter STUDENT NAME: \<RET\>

> CLASS NAME: \<RET\>

> Menu Access:

> The Class Registration Enter/Delete option is accessed through the Package

> Coordinator Menu and the Education Tracking Instructor Menu options.

> Self Registration Enter/Edit

> Description:

> This option allows an employee to self register for a class. The data is stored in the

> PRSE Education Registration file (#452.8).

> Additional Information:

> Users may self register for any:

> 1\. Present/future class.

> 2\. Open class sponsored by any service.

> 3\. Closed class within their own service.

> 4\. Mandatory class that they are required to attend as indicated in the PAID Employee file (#450).

> Individuals do not need to preregister for class attendance to be taken. Names of those individuals registered for classes can be printed through the Class Registration Roster report.

> Menu Display:

> PRIVACY ACT STATEMENT

> In accordance with OPM and VA policies this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purposes. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

> 1 Leave Request

> 2 Leave Balances

> 3 Display Leave Requests

> 4 Cancel Leave Request

> 5 Service Record Screen

> 6 Display Pay Period

> 7 Self Registration Enter/Edit

> Select Employee Menu Option:

> Screen Prints:

> Select Employee Menu Option: 7 Self Registration Enter/Edit

> Select one of the following:

> R Class Registration Calendar Report (Refer to the Reports section for an explanation of the Class Registration Calendar Report)

> S Student Registration

> Choose a selection from the above choices: Student Registration

> Select one of the following:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>Mandatory Training (MI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Continuing Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Other/Miscellaneous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select a Training Type: ?

> The user must first select the type of class. If this sort was not placed in the software, the listing of classes in the help would be enormous and definitely not user friendly.

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other

> W Ward/Unit Training

> A All

> Select a Training Type: Continuing Education

> CLASS NAME: ?

> Displayed below is a list of all classes which are opened for registration based on the above class type.

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES) CHOOSE FROM:

> BASIC CPR NURSING SERVICE HALOGEN EXTINGUISHERS ENGINEERING SERVICE

> 1\. Adding your name to the registration list.

> CLASS NAME: HALOGEN EXTINGUISHERS ENGINEERING SERVICE Select DATE: APR 10, 1994// ?

> ANSWER WITH START DATE/TIME OF CLASS

> CHOOSE FROM:

> This is a listing of all dates associated with the class.

> 04-10-1994

> 05-22-1994

> 06-03-1994

> Select DATE: APR 10, 1994// \<RET\> APR 10, 1994

> Do you want to register PAIDEMPLOYEE15,ONE for HALOGEN EXTINGUISHERS? YES// ?

> Answer YES or NO.

> Do you want to register PAIDEMPLOYEE15,ONE for HALOGEN EXTINGUISHERS? YES// \<RET\>

> (YES)

> 2\. Deleting your name from the registration list.

> CLASS NAME: HALOGEN EXTINGUISHERS NURSING SERVICE Select DATE: APR 10, 1994// \<RET\> APR 10, 1994

> PAIDEMPLOYEE15,ONE is currently Registered for this HALOGEN EXTINGUISHERS Class!

> Do you want to delete this record? NO// Y (YES)

> PAIDEMPLOYEE15,ONE \*\*DELETED\*\*

> Menu Access:

> The Self Registration Enter/Edit option is accessed through the Employee Menu option.

## Chapter 5: Attendance at Programs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> This menu contains options used to document attendance at past or present classes. Information is stored in the PRSE Student Education Tracking file (#452).

> Additional Information:

> Refer to Chapter 3, Additional Information, for information on the different types of class records stored in File \#452. This menu also contains options which

> 1\. Track non-local continuing education data.

> 2\. Allow attendance to be taken on classes which have been purged from the

> PRSE Program/Class file (#452.1).

> 3\. Permit changes in the employee's Student Education Tracking file (#452)

> record.

> 4\. Edits (through a simplified operation) employee attendance at assigned mandatory training classes and enters the information in the employee's record (File \#452).

> Menu Display:

> Select Package Coordinator Menu Option: 3 Attendance Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Attendance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Non-Local CE and Enter Attendance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Modify Past Class Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Quick Attendance Update of Past/Purged Classes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Quick Mandatory Training (MI) Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Menu Access:

> The Attendance Menu option is accessed through the Package Coordinator Menu and the Education Tracking Instructor's Menu options.

> Enter/Edit Class Attendance

> Description:

> This option allows entry of class attendance in the PRSE Student Education

> Tracking file (#452).

> Additional Information:

> Attendance can only be taken for a class with a past or present date. Recording attendance at classes with future dates is not permitted. The data entered through this option can be found on multiple service and employee training reports. Users holding the PRSE CORD key can enter attendance for anyone regardless of service or class restrictions. The users holding the PRSE SUP key can credit attendance at any class sponsored by the user's service.

> Menu Display:

> Select Package Coordinator Menu Option: 3 Attendance Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Attendance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Non-local CE and Enter Attendance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Modify Past Class Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Quick Attendance Update of Past/Purged Classes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Quick Mandatory Training (MI) Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Attendance Menu Option: 1 Enter/Edit Class Attendance

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> Select a Training Type: ?

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> This field pre-selects the class type for the purpose of decreasing the listing of classes displayed in the help. If this sort was not placed in the software, the listing of classes would be enormous and definitely not user friendly.

> Select a Training Type: Mandatory Training (MI) Select CLASS: ?

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR

> TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> CHOOSE FROM:

> 138 EXPOSURE TO BLOOD PATHOGEN LABORATORY SERVICE

> ADP SECURITY NURSING SERVICE

> ADVANCED LIFE SUPPORT NURSING SERVICE

> ADVANCED MUMPS INFORMATION SYSTEMS CENTER

> ANNUAL REVIEW NURSING SERVICE

> BASIC LIFE SUPPORT NURSING SERVICE

> BCLS CERTIFICATION NURSING SERVICE

> BCLS INSTRUCTOR EVAL NURSING SERVICE

> BCLS INSTRUCTOR EXAM NURSING SERVICE

> BIOETHICS NURSING SERVICE

> BLOOD ADMINISTRATION NURSING SERVICE

> BLOOD-BORNE PATHOGENS NURSING SERVICE

> '^' TO STOP: ^

> Select CLASS: BASIC LIFE SUPPORT NURSING SERVICE

> Select START DATE/TIME OF CLASS: AUG 1, 1993// ?

> ANSWER WITH START DATE/TIME OF CLASS

> In order to take attendance for this class, the class must have a present or past date.

> CHOOSE FROM:

> 05-12-1993

> 08-01-1993

> Select START DATE/TIME OF CLASS: AUG 1, 1993// \<RET\> AUG 1, 1993

> 1\. Adding an attendance record to a person's file .

> Select Student Name: ?

> ANSWER WITH STUDENT NAME

> DO YOU WANT THE ENTIRE STUDENT NAME LIST? Y (YES)

> CHOOSE FROM:

> PAIDEMPLOYEE16,TEN NURSING SERVICE

> PAIDEMPLOYEE16,ONE NURSING SERVICE

> PAIDEMPLOYEE16,TWO NURSING SERVICE

> PAIDEMPLOYEE15,ONE NURSING SERVICE

> PAIDEMPLOYEE16,THREE NURSING SERVICE

> PAIDEMPLOYEE16,FOUR NURSING SERVICE

> PAIDEDPRESENTER,SIX NURSING SERVICE

> PAIDEMPLOYEE16,FIVE NURSING SERVICE

> The list of individuals displayed above have pre-registered for the class.

> Remember that an attendee does not have to pre-register for a class for attendance to be credited. The user must credit a person's attendance on an individual basis. You cannot enter attendance on a group basis.

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE 611-ENTRY NEW PERSON LIST? N (NO)

> Select Student Name: PAIDEMPLOYEE16,SIX 000000166

> Do you want to credit PAIDEMPLOYEE16,SIX - NURSING SERVICE for attending BASIC LIFE SUPPORT? YES// \<RET\> (YES)

> PAIDEMPLOYEE16,SIX BASIC LIFE SUPPORT AUG 1, 1993

> The previous message indicates that the attendance record was stored in the

> PRSE Education Tracking file.

> 2\. Deleting an attendance record from a person's file.

> Select Student Name: PAIDEMPLOYEE16,SIX 000000166

> PAIDEMPLOYEE16,SIX completed BASIC LIFE SUPPORT on this date. Do you want to delete this record? NO// Y (YES) PAIDEMPLOYEE16,SIX \*\*DELETED\*\*

> Select Student Name: \<RET\>

> Menu Access:

> The Enter/Edit Class Attendance option is accessed through the Attendance

> Menu option.

> Create Non-Local CE and Enter Attendance

> Description:

> This option allows the user to enter and edit continuing education class information for courses not presented at the medical center facility. Attendance for a class is entered through this option along with cost and leave data. The information is stored in the PRSE Student Education Tracking file (#452).

> Additional Information:

> This option is ONLY for non-local continuing education classes. Enter Local Continuing Education programs through the Enter/Edit Continuing Education option found in the Enter/Edit Class Information Menu option. The data edited by this option can be found on the service and individual training reports under class type continuing education.

> Menu Display:

> Select Package Coordinator Menu Option: 3 Attendance Menu

> 1 Enter/Edit Class Attendance

> 2 Create Non-Local CE and Enter Attendance

> 3 Modify Past Class Information

> 4 Quick Attendance Update of Past/Purged Classes

> 5 Quick Mandatory Training (MI) Update

> Screen Prints:

> Select Attendance Menu Option: 2 Create Non-local CE and Enter Attendance

> Select NON-LOCAL C.E. CLASS: ?

> The display lists only non-local continuing education class names.

> ANSWER WITH PRSE STUDENT EDUCATION TRACKING PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE STUDENT EDUCATION TRACKING LIST? Y (YES)

> CHOOSE FROM:

> AVI PUMP NURSING SERVICE

> BUDGET NURSING SERVICE

> LEADERSHIP SEMINAR NURSING SERVICE

> PACKAGE TESTING NURSING SERVICE

> SUMMER INSTITUTE IN NURSING INFORMATICS 93 NURSING SERVICE

> TX MEDICAL CENTER COLLABORATIVE PRECEPTOR PROG NURSING SERVICE

> UPDATE JCAHO COMMI NURSING SERVICE

> '^' TO STOP: ^

> Select NON-LOCAL C.E. CLASS: UPDATE JCAHO STANDARDS

> ARE YOU ADDING 'UPDATE JCAHO STANDARDS' AS A NEW CLASS? Y (YES)

> In order to take attendance for this class, the class must have a present or past date.

> Select CLASS DATE: T (APR 05, 1994) This field contains the scheduled start date/time for the class.

> ARE YOU ADDING 'APR 5, 1994' AS A NEW CLASS DATE? Y (YES)

> Select Student Name: ?

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME

> DO YOU WANT THE ENTIRE ENTRY NEW PERSON LIST? Y (YES)

> CHOOSE FROM:

> PAIDEMPLOYEE16,NINE

> PAIDEMPLOYEE16,SEVEN

> PAIDEMPLOYEE16,EIGHT

> PAIDEMPLOYEE15,SIX

> PAIDEMPLOYEE17,TEN

> '^' TO STOP: ^

> Select Student Name: PAIDEMPLOYEE15,ONE 000000151

> The next field contains the end date/time for the class. It defaults to the start date.

> ENDING DATE: APR 5, 1994// \<RET\> (APR 05, 1994)

> SOURCE OF TRAINING: NON-GOVERNMENT (e.g. Institution, Company or University)

> // ?

> CHOOSE FROM:

> 1 VA

> 2 INTERAGENCY

> 3 NON-GOVERNMENT (Designed for VA)

> 4 NON-GOVERNMENT (e.g. Institution, Company or University)

> 5 STATE OR LOCAL GOVERNMENT

> This field identifies the source of funding for the class. All classes default to NON­ GOVERNMENT (e.g. Institution, Company or University). The user may change this entry by selecting the correct number.

> SOURCE OF TRAINING: NON-GOVERNMENT (e.g. Institution, Company or University)

> // \<RET\>

> CLASS CATEGORY: ?

> This field categorizes a specific class or program. Refer to 3.1 for additional information.

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS CATEGORY PROGRAM CATEGORY, OR PAID CODE

> DO YOU WANT THE ENTIRE 91-ENTRY PRSE EDUCATION PROGRAM/CLASS CATEGORY LIST? Y

> (YES)

> CHOOSE FROM:

> ADJUDICATION (Spe/Tec) 5C

> ADVANCED SUPERVISORY TRAINING (Sup.) 2A

> ARITHMETIC (Basic Ed.) 92

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Adm.) 46

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Exec.) 16

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Sup.) 23

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> '^' TO STOP: ^

> CLASS CATEGORY: 36 MEDICAL - NURSES 36

> PURPOSE OF TRAINING: ?

> This field contains the reason this program/class is given. Refer to 3.1 for additional information.

> ANSWER WITH PRSE EMPLOYEE PURPOSE OF TRAINING PAID CODE

> DO YOU WANT THE ENTIRE 11-ENTRY PRSE EMPLOYEE PURPOSE OF TRAINING LIST? Y

> (YES)

> CHOOSE FROM:

> ADULT BASIC EDUCATION 9

> DEVELOP NEW SKILLS 6

> EMPLOYEE FINANCED 10

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> PURPOSE OF TRAINING: IMPROVE PRESENT PERFORMANCE 4

> PRSE PROGRAM/CLASS LENGTH HRS: ?

> Indicate class hours by typing a Number between 0 and 9999.99, 2 Decimal

> Digits.

> PRSE PROGRAM/CLASS LENGTH HRS: 2

> CLASS HRS DURING ON-DUTY TIME: 2// ?

> Indicate on duty hours by entering a Number between 0 and 9999, 0 Decimal

> Digits.

> The value entered into this field equates to the number of classroom hours for the program when an employee attends the class during on-duty time.

> CLASS HRS DURING ON-DUTY TIME: 2// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: ?

> Indicate off duty hours by entering a Number between 0 and 9999, 0

> Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> CLASS HRS DURING OFF-DUTY TIME: 0

> PRESENTER/SUPPLIER: ?

> This field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE 611-ENTRY NEW PERSON LIST? Y (YES)

> CHOOSE FROM: PAIDEMPLOYEE16,NINE PAIDEMPLOYEE16,SEVEN PAIDEMPLOYEE16,EIGHT PAIDEDPRESENTER,FIVE PAIDEDPRESENTER,NINE

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins the display of entries from the PRSE Education Program/Class Supplier file.

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS SUPPLIER PRESENTER/SUPPLIER

> DO YOU WANT THE ENTIRE 71-ENTRY PRSE EDUCATION PROGRAM/CLASS SUPPLIER LIST? Y

> (YES)

> CHOOSE FROM:

> ACME

> ACNS ED

> ACOS/E SERVICE

> ACOS/EDUCATION

> AHA

> NAMEPLACE EDUCATIONAL TRAINING

> YOU MAY ENTER A NEW PRSE EDUCATION PROGRAM/CLASS SUPPLIER, IF YOU WISH Answer must be 3-30 characters in length

> Enter the name of the vendor or supplier of this program (class). PRESENTER/SUPPLIER: ACME

> ACME

> Is this the one you want NO// YES (YES)

> SPONSORING SERVICE: PAIDEDORG,ONE// ?

> Answer must be 3-30 characters in length

> The default value for program/class location is obtained from the city and state demographic information associated with presenter/supplier stored in File 452.2.

> SPONSORING SERVICE: PAIDEDORG,ONE// \<RET?

> CODE FOR OLDE: NOT CODED// ?

> Please enter status of this program or class

> CHOOSE FROM:

> Y CODED

> N NOT CODED

> CODE FOR OLDE: NOT CODED// Y CODED

> GOVERNMENT FUNDED: GOVERNMENT FUNDED//

> CHOOSE FROM:

> G GOVERNMENT FUNDED

> E EMPLOYEE FUNDED

> This field indicates whether the class was government funded or not.

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// \<RET\>

> ROUTINE/NON-ROUTINE: NON-ROUTINE// ??

> This field indicates whether or not the class enhances or does not

> enhance the employee's job qualifications.

> CHOOSE FROM:

> R ROUTINE

> N NON-ROUTINE

> ROUTINE/NON-ROUTINE: NON-ROUTINE// R ROUTINE

> The following information is used in OLDE transmissions.

> ACCREDITING ORGANIZATION: ?

> ANSWER WITH PRSE EDUCATION ACCREDITATION ORGANIZATIONS

> ACCREDITATION GROUP

> DO YOU WANT THE ENTIRE 60-ENTRY PRSE EDUCATION ACCREDITATION ORGANIZATIONS

> LIST? Y

> (YES)

> CHOOSE FROM:

> AACCN

> SAMPLE CRITICAL CARE NURSING

> SAMPLE DIETETIC ASSOCIATION

> SAMPLE MEDICAL ASSOCIATION

> SAMPLE NURSES ASSOCIATION

> SAMPLE RED CROSS

> This is the name of the accrediting organization for this class.

> ACCREDITING ORGANIZATION: SAMPLE NURSES ASSOCIATION CONTACT HOURS: ?

> Type a Number between 0 and 9999.99, 2 Decimal Digits

> This field contains the number of contact hours associated with this class.

> CONTACT HOURS: 2

> C.E.U.s: ?

> Type a Number between 0 and 9999.9, 1 Decimal Digit

> C.E.U.s: 2

> Select SVC REASON: ?

> ANSWER WITH SVC REASON

> YOU MAY ENTER A NEW SVC REASON, IF YOU WISH

> ANSWER WITH PRSE SVC REASONS FOR TRAINING REASON FOR EMPLOYEE TRAINING

> DO YOU WANT THE ENTIRE 8-ENTRY PRSE SVC REASONS FOR TRAINING LIST? Y (YES)

> CHOOSE FROM:

> ANNUAL REVIEW

> CONTINUING EDUCATION

> DECENTRALIZED INSERVICE

> DEVELOP NEW SKILLS

> ENHANCE SKILLS

> IMPROVE PRESENT PERFORMANCE

> MAKE UP CLASS

> MANDATORY INSERVICE

> This field contains the service's reason for attending this class. The reasons listed

> in the above display can be edited and expanded through the Service Reason option

> (refer to Chapter 2 for additional information).

> Select SVC REASON: CONTINUING EDUCATION Select SVC REASON: ENHANCE SKILLS

> Select SVC REASON: \<RET\>

> Are you entering funding and A/A information into the student's record? NO// ?

> Answer YES or NO.

> Are you entering funding and A/A information into the student's record? NO// Y

> (YES)

> STUDENT EXPENSE: ?

> Type a Dollar Amount between 0 and 2000, 2 Decimal Digits.

> This is the amount, if any, incurred by this employee for a government sponsored program or class.

> STUDENT EXPENSE: 50

> DIRECT COST: ?

> Type a Dollar Amount between 0 and 9999.99, 2 Decimal Digits.

> This field contains the direct government cost (tuition, books, etc.) of the class. Refer to VA Form 5-4691, field 13.

> DIRECT COST: 65

> INDIRECT COST: ?

> Type a Dollar Amount between 0 and 9999.99, 2 Decimal Digits.

> This field contains the indirect government cost (travel, per diem) of the class. Refer to VA Form 5-4691, field 13.

> INDIRECT COST: 65

> HOURS A/A REQUESTED: ?

> Type a Number between 0 and 999, 0 Decimal Digits.

> This field contains the hours of authorized absence requested by an employee to attend a class.

> HOURS A/A REQUESTED: 2

> HOURS A/A GRANTED: ?

> Type a Number between 0 and 999, 0 Decimal Digits.

> This field contains the total hours of authorized absence granted to attend a class.

> HOURS A/A GRANTED: 2

> Select FUNDS REQUESTED: ?

> ANSWER WITH FUNDS REQUESTED

> YOU MAY ENTER A NEW FUNDS REQUESTED, IF YOU WISH

> CHOOSE FROM:

> A AIRFARE

> P PER DIEM

> R REGISTRATION

> H HOTEL

> T TRAVEL

> N NONE REQUESTED

> U TUITION

> B BOOKS/MATERIALS D DIRECT OTHER

> I INDIRECT OTHER

> This field indicates intended use of requested funds, (e.g., hotel, registration, etc.)

> Select FUNDS REQUESTED: R (REGISTRATION) AMOUNT REQUESTED: ?

> Type a Dollar Amount between 0 and 99999.99, 2 Decimal Digits.

> This field stores the total funding (dollar amount) requested by the employee.

> AMOUNT REQUESTED: 50

> Select FUNDS REQUESTED: \<RET\>

> Select FUNDS AUTHORIZED: ?

> ANSWER WITH FUNDS AUTHORIZED

> YOU MAY ENTER A NEW FUNDS AUTHORIZED, IF YOU WISH

> CHOOSE FROM:

> A AIRFARE

> P PER DIEM

> R REGISTRATION

> H HOTEL

> T TRAVEL

> N NONE REQUESTED

> U TUITION

> B BOOKS/MATERIALS

> D DIRECT OTHER

> I INDIRECT OTHER

> This field indicates intended use of authorized funds, (e.g., hotel, airfare).

> Select FUNDS AUTHORIZED: R (REGISTRATION) AMOUNT AUTHORIZED: ?

> Type a Dollar Amount between 0 and 99999.99, 2 Decimal Digits.

> This field stores the dollar amount authorized by a service to an employee.

> AMOUNT AUTHORIZED: 50

> Select FUNDS AUTHORIZED: \<RET\>

> C.E.U. COMMENTS:

> This is a word-processing field. Enter additional comments regarding program/funding.

> 1\>THIS CLASS SHOULD BE PRESENTED TO ALL NURSING SUPERVISORS.

> 2\>\<RET\>

> EDIT Option: \<RET\>

> EDUCATION UPDATE PAIDEMPLOYEE15,ONE APR 5, 1994

> The above display indicates that the record was stored in the PRSE Student

> Education file.

> Select Student Name: \<RET\> The name of another attendee may be entered at this prompt. The software allows the user to edit specific fields which might differ from the first person's record (e.g., accrediting organization, cost).

> Select NON-LOCAL C.E. CLASS: \<RET\>

> Menu Access:

> The Create Non-Local CE and Enter Attendance option is accessed through the

> Attendance Menu option.

> Modify Past Class Information

> Description:

> This option allows a user to edit or delete all records in the PRSE Student Education Tracking file (#452) for a specific class. There are four pieces of data (i.e., training class name, program/class supplier, training type, and the class length in hours) which the user can change and the system will automatically update all student records that are associated with this class.

> Additional Information:

> Data edited by this option can be found on the Individual Training and Service

> Training Reports.

> Menu Display:

> Select Package Coordinator Menu Option: 3 Attendance Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Attendance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Non-Local CE and Enter Attendance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Modify Past Class Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Quick Attendance Update of Past/Purged Classes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Quick Mandatory Training (MI) Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Attendance Menu Option: 3 Modify Past Class Information

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> Select A Training Type: ?

> This field pre-selects the type of class for the purpose of decreasing the listing of classes displayed in the help. If this sort was not placed in the software, the listing of classes would be enormous and definitely not user friendly.

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> Select a Training Type: Continuing Education

> Select TRAINING CLASS: ?

> This display lists both local and non-local continuing education classes.

> ANSWER WITH PRSE STUDENT EDUCATION TRACKING PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE STUDENT EDUCATION TRACKING LIST? Y (YES)

> CHOOSE FROM:

> ANNUAL PRACTIONER'S SEMINAR & CLAMBAKE NURSING SERVICE

> AVI PUMP NURSING SERVICE

> BUDGETS IN NURSING NURSING SERVICE

> CARING FOR THE GERIATRIC PATIENT NURSING SERVICE

> CLINICAL POTPOURRI NURSING SERVICE

> COURTEOUS INTERACTIONS NURSING SERVICE

> '^' TO STOP: ^

> Select TRAINING CLASS: COURTEOUS INTERACTIONS NURSING SERVICE TRAINING CLASS: COURTEOUS INTERACTIONS Replace ?

> This response can be free text.

> TRAINING CLASS: COURTEOUS INTERACTIONS Replace \<RET\>

> PRESENTER/SUPPLIER: ?

> This field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE 611-ENTRY NEW PERSON LIST? Y (YES)

> CHOOSE FROM: PAIDEMPLOYEE16,NINE PAIDEMPLOYEE16,SEVEN PAIDEMPLOYEE16,EIGHT PAIDEMPLOYEE15,SIX PAIDEMPLOYEE17,TEN

> '^' TO STOP: ^

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins the display of entries from the PRSE Education Program/ Class Supplier file.

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS SUPPLIER PRESENTER/SUPPLIER

> DO YOU WANT THE ENTIRE 71-ENTRY PRSE EDUCATION PROGRAM/CLASS SUPPLIER LIST? Y

> (YES)

> CHOOSE FROM:

> ACOS/E SERVICE

> ACOS/EDUCATION

> AHA

> NAMEPLACE EDUCATIONAL TRAINING

> NAME'S MEDICAL SUPPLIES

> SOMEONE'S EDUCATIONAL PROGRAMS

> EXNAME'S EDUCATIONAL MATERIALS

> DIETETIC SERVICE

> '^' TO STOP: ^

> YOU MAY ENTER A NEW PRSE EDUCATION PROGRAM/CLASS SUPPLIER, IF YOU WISH Answer must be 3-30 characters in length

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: PAIDEDPRESENTER,SIX

> Is this the one you want? NO//Y (YES) Select one of the following:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>Mandatory Training (MI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Continuing Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Other/Miscellaneous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This is the type of training, (e.g., mandatory training, continuing education, ward inservice, other inservice).

> SELECT A TRAINING TYPE: Continuing Education// \<RET\>

> PRSE PROGRAM/CLASS LENGTH HRS: ? This is the field which is going to be edited.

> Type a Number between 0 and 9999.99, 2 Decimal Digits.

> This is the length of the class in hours.

> PRSE PROGRAM/CLASS LENGTH HRS: 4

> ..

> Select TRAINING CLASS: \<RET\>

> Menu Access:

> The Modify Past Class Information option is accessed through the Attendance Menu option.

> Quick Attendance Update of Past/Purged Classes

> Description:

> This option allows the user to create and edit an employee record in the PRSE Student Education Tracking file (#452) when past classes are purged from the PRSE Program/Class file (452.1).

> Additional Information:

> This option is to be used when the name of the class is no longer found in the

> display list of the PRSE Program/Class file through either the Class File Edit option or the options found in the Enter Edit Class Information menu. The data edited by this option is reflected in appropriate service and individual training reports.

> Menu Display

> Select Package Coordinator Menu Option: 3 Attendance Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Attendance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Non-local CE and Enter Attendance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Modify Past Class Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Quick Attendance Update of Past/Purged Classes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Quick Mandatory Training (MI) Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Attendance Menu Option: 4 Quick Attendance Update of Past/Purged

> Classes

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> Select a Training Type: ?

> This field assists the user to pre-select the type of class for the purpose of decreasing the listing of classes displayed in the help. If this sort was not placed in the software, the listing of classes would be enormous and definitely not user friendly.

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training

> \(MI\) C Continuing Education

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> Select a Training Type: Continuing Education

> Select TRAINING CLASS: ?

> This display lists the local and continuing education classes.

> ANSWER WITH PRSE STUDENT EDUCATION TRACKING PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE STUDENT EDUCATION TRACKING LIST? Y (YES)

> CHOOSE FROM:

> 5TH NURSING INFORMATICS NURSING SERVICE

> AONE NURSING SERVICE

> BUDGETS IN NURSING NURSING SERVICE

> CARING FOR THE GERIATRIC PATIENT NURSING SERVICE

> CLINICAL POTPOURRI NURSING SERVICE

> COURTEOUS INTERACTIONS NURSING SERVICE

> CREATIVE WAYS OF TEACHING NURSING SERVICE

> DHCP BASIC USER NURSING SERVICE

> Select TRAINING CLASS: CLINICAL POTPOURRI NURSING SERVICE Select CLASS DATE: JUN 30, 1993// ?

> JUN 30, 1993

> This is the scheduled start date/time for the class.

> Select CLASS DATE: JUN 30, 1993// \<RET\> (JUN 30, 1993) Select Student Name: ?

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE NEW PERSON LIST? Y (YES)

> CHOOSE FROM: PAIDEMPLOYEE16,NINE PAIDEMPLOYEE16,SEVEN PAIDEMPLOYEE16,EIGHT PAIDEMPLOYEE15,SIX 000000156

> PAIDEMPLOYEE17,TEN

> '^' TO STOP: ^

> Select Student Name: PAIDEMPLOYEE15,ONE 000000151

> ENDING DATE: JUN 30, 1993// ?

> This is the scheduled end date/time for the class.

> ENDING DATE: JUN 30, 1993// \<RET\> (JUN 30, 1993) SOURCE OF TRAINING: VA// ?

> CHOOSE FROM:

> 1 VA

> 2 INTERAGENCY

> 3 NON-GOVERNMENT (Designed for VA)

> 4 NON-GOVERNMENT (e.g. Institution, Company or University)

> 5 STATE OR LOCAL GOVERNMENT

> This field identifies the source of funding for the class.

> SOURCE OF TRAINING: VA// \<RET\>

> CLASS CATEGORY: OTHER (Trade/Craft)// ?

5.17

> This field categorizes a specific class or program. Refer to page 3.1 for additional information.

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS CATEGORY PROGRAM CATEGORY, OR PAID CODE

> DO YOU WANT THE ENTIRE 91-ENTRY PRSE EDUCATION PROGRAM/CLASS CATEGORY LIST? Y

> (YES)

> CHOOSE FROM:

> ADJUDICATION (Spe/Tec) 5C

> ADVANCED SUPERVISORY TRAINING (Sup.) 2A

> ARITHMETIC (Basic Ed.) 92

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Adm.) 46

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Exec.) 16

> BASIC TRAINING IN FEDERAL LABOR-MGMT. REL. (Sup.) 23

> BOILER OR AIR COND. OPERATION (Trade/Craft) 77

> BRAILLE (Basic Ed.) 94

> CARPENTRY (Trade/Craft) 74

> COMPLETES 40-HOUR REQUIREMENT (Sup.) 27

> COMPLETES 80-HOUR REQUIREMENT (Sup.) 29

> COMPUTER OPERATING (Clerical) 66

> COMPUTER PROGRAMMING (Spec.) 57

> CONTRACT ADMINISTRATION (Adm.) 48

> CONTRACT ADMINISTRATION (Exec.) 18

> CONTRACT ADMINISTRATION (Sup.) 25

> CONTRACT NEGOTIATIONS (Adm.) 47

> CONTRACT NEGOTIATIONS (Exec.) 17

> CONTRACT NEGOTIATIONS (Sup.) 24

> CPR TRAINING (Spec/Tec) 5F

> DISABL.VET./HANDICAPPED/VIETNAM ERA EMPLOY. (Sup.) 22

> '^' TO STOP: ^

> CLASS CATEGORY: OTHER (Trade/Craft)// \<RET\> (OTHER (Trade/Craft))

> PURPOSE OF TRAINING: ?

> This field contains the reason this program/class is given. Refer to 3.1 for additional information.

> ANSWER WITH PRSE EMPLOYEE PURPOSE OF TRAINING PAID CODE CHOOSE FROM:

> ADULT BASIC EDUCATION 9

> DEVELOP NEW SKILLS 6

> EMPLOYEE FINANCED 10

> IMPROVE PRESENT PERFORMANCE 4

> MEET FUTURE STAFFING NEEDS 5

> MISSION OR PROGRAM CHANGE 1

> NEW TECHNOLOGY 2

> NEW WORK ASSIGNMENT 3

> ORIENTATION 8

> TRADE OR CRAFT APPRENTICESHIP 7

> PURPOSE OF TRAINING: NEW TECHNOLOGY 2

> PRSE PROGRAM/CLASS LENGTH HRS: 1// ?

> Indicate class hours by typing a Number between 0 and 9999.99, 2 Decimal

> Digits.

> This field contains the length of the class in whole hours.

> PRSE PROGRAM/CLASS LENGTH HRS: 1// \<RET\>

> CLASS HRS DURING ON-DUTY TIME: 1// ?

> Indicate on duty hours by entering a Number between 0 and 9999, 0 Decimal

> Digits.

> The value entered into this field equates to the number of classroom hours for the program when an employee attends the class during on-duty time.

> CLASS HRS DURING ON-DUTY TIME: 1// \<RET\>

> CLASS HRS DURING OFF-DUTY TIME: ?

> Indicate off duty hours by entering a Number between 0 and 9999, 0

> Decimal Digits.

> This field indicates the number of classroom hours for the program when an employee attends a program during off-duty time.

> CLASS HRS DURING OFF-DUTY TIME: \<RET\>

> PRESENTER/SUPPLIER: ?

> This field contains the company or organization who supplied the materials for this class. This field looks up on two files: first, the New Person file, second, the PRSE Program/Class Supplier file.

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME DO YOU WANT THE ENTIRE 611-ENTRY NEW PERSON LIST? Y (YES)

> CHOOSE FROM: PAIDEMPLOYEE16,NINE PAIDEMPLOYEE16,SEVEN PAIDEMPLOYEE16,EIGHT PAIDEMPLOYEE15,SIX PAIDEMPLOYEE17,TEN

> After the software lists the entries in the New Person file, the user can enter an up arrow (^) which begins the display of entries from the PRSE Education Program/ Class Supplier file.

> ANSWER WITH PRSE EDUCATION PROGRAM/CLASS SUPPLIER PRESENTER/SUPPLIER

> DO YOU WANT THE ENTIRE 72-ENTRY PRSE EDUCATION PROGRAM/CLASS SUPPLIER LIST? Y

> (YES)

> CHOOSE FROM:

> ACNS/E

> ACOS/E SERVICE

> AHA

> NAMEPLACE EDUCATIONAL TRAINING

> When laygo to the PRSE Education Program/Class Supplier file is turned on in the

> PRSE Parameters file, the following message will display:

> Enter the name of the vendor or supplier of this program (class).

> This field contains the name of the company or organization who supplied

> the program or class.

> The answer must be 3-30 characters in length.

> When laygo to the PRSE Education Program/Class Supplier file is turned off in the

> PRSE Parameters file, the following message will display:

> NEW ENTRIES CANNOT BE ADDED TO THE SUPPLIER/PRESENTER FILE FROM THIS OPTION CONTACT THE EDUCATION PACKAGE COORDINATOR OR IRM

> PRESENTER/SUPPLIER: PAIDEDPRESENTER,SIX

> Is this the one you want? NO// Y (YES)

> SPONSORING SERVICE: PAIDEDSPONSOR,TWO// ?

> Answer must be 3-30 characters in length.

> This field indicates where the class is being presented.

> SPONSORING SERVICE: PAIDEDSPONSOR,TWO// \<RET\>

> CODE FOR OLDE: NOT CODED// ?

> Please enter the status of this program or class.

> CHOOSE FROM:

> Y CODED

> N NOT CODED

> CODE FOR OLDE: NOT CODED// Y CODED

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// ?

> CHOOSE FROM:

> G GOVERNMENT FUNDED

> E EMPLOYEE FUNDED

> This field indicates if the class is government funded or not.

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// \<RET\>

> ROUTINE/NON-ROUTINE: NON-ROUTINE// ?

> Enter (R)outine if class does not enhance employee's job qualifications,

> or (N)on-Routine if the opposite is true.

> CHOOSE FROM:

> R ROUTINE

> N NON-ROUTINE

> ROUTINE/NON-ROUTINE: NON-ROUTINE

> ACCREDITING ORGANIZATION: ?

> ANSWER WITH PRSE EDUCATION ACCREDITATION ORGANIZATIONS

> ACCREDITATION GROUP

> DO YOU WANT THE ENTIRE 20-ENTRY PRSE EDUCATION ACCREDITATION ORGANIZATIONS

> LIST? Y

> (YES)

> CHOOSE FROM:

> AACCN

> SAMPLE CRITICAL CARE NURSING

> SAMPLE DIETETIC ASSOCIATION

> SAMPLE MEDICAL ASSOCIATION

> SAMPLE NURSES ASSOCIATION

> SAMPLE RED CROSS

> DELAWARE NURSES ASSOCIATION

> ILLINOIS NURSES ASSOCIATION

> IOWA GROUP OF NURSING

> JCAHO

> TEXAS NURSES ASSOCIATION

> This field contains the name of the organization accrediting the program.

> ACCREDITING ORGANIZATION: SAMPLE NURSES ASSOCIATION

> CONTACT HOURS: ?

> Type a Number between 0 and 9999.99, 2 Decimal Digits.

> This field contains the number of contact hours associated with the class.

> CONTACT HOURS: .5

> C.E.U.s: 1// ?

> Type a Number between 0 and 9999.9, 1 Decimal Digit.

> This is the number of continuing education units associated with this class.

> C.E.U.s: 1// \<RET\>

> Select SVC REASON: ?

> This field contains the service's reason for attending this class. The reasons listed in the above display can be edited and expanded through the Service Reason option (refer to Chapter 2 for additional information).

> ANSWER WITH SVC REASON: ENHANCE SKILLS

> YOU MAY ENTER A NEW SVC REASON, IF YOU WISH

> ANSWER WITH PRSE SVC REASONS FOR TRAINING REASON FOR EMPLOYEE TRAINING

> DO YOU WANT THE ENTIRE 7-ENTRY PRSE SVC REASONS FOR TRAINING LIST? Y (YES)

> CHOOSE FROM:

> ANNUAL REVIEW

> CONTINUE EDUCATION

> CREDENTIALING

> DECENTRALIZED INSERVICE

> DEVELOP NEW SKILLS

> ENHANCE SKILLS

> IMPROVE PRESENT PERFORMANCE

> MANDATORY INSERVICE

> Select SVC REASON: IMPROVE PRESENT PERFORMANCE

> Select SVC REASON: \<RET\>

> Are you entering funding and A/A information into the student's record? NO// ?

> Answer YES or NO.

> Are you entering funding and A/A information into the student's record? NO// Y

> (YES)

> STUDENT EXPENSE: ?

> Type a Dollar Amount between 0 and 2000, 2 Decimal Digits.

> This is the amount, if any, incurred by this employee for a government sponsored program or class.

> STUDENT EXPENSE: 20

> DIRECT COST: ?

> Type a Dollar Amount between 0 and 9999.99, 2 Decimal Digits.

> This field contains the direct government cost (tuition, books, etc.) of the class.

> DIRECT COST: 20

> INDIRECT COST: ?

> Type a Dollar Amount between 0 and 9999.99, 2 Decimal Digits.

> This field contains the indirect government cost (travel, per diem) of the class.

> INDIRECT COST: 20

> HOURS A/A REQUESTED: ?

> Type a Number between 0 and 999, 0 Decimal Digits.

> This field contains the hours of authorized absence requested by the employee to attend a class.

> HOURS A/A REQUESTED: 8

> HOURS A/A GRANTED: ?

> Type a Number between 0 and 999, 0 Decimal Digits.

> This field contains the total hours of authorized absence granted to attend a class.

> HOURS A/A GRANTED: 8

> Select FUNDS REQUESTED: ?

> ANSWER WITH FUNDS REQUESTED

> YOU MAY ENTER A NEW FUNDS REQUESTED, IF YOU WISH

> CHOOSE FROM:

> N NONE REQUESTED U TUITION

> B BOOKS/MATERIALS D DIRECT OTHER

> I INDIRECT OTHER

> This field indicates intended use of requested funds, e.g., hotel, registration, etc.

> Select FUNDS REQUESTED: R (REGISTRATION) AMOUNT REQUESTED: ?

> Type a Dollar Amount between 0 and 99999.99, 2 Decimal Digits.

> This field stores the total funding (dollar amount) requested by the employee.

> AMOUNT REQUESTED: 20

> Select FUNDS REQUESTED: \<RET\>

> Select FUNDS AUTHORIZED: ?

> ANSWER WITH FUNDS AUTHORIZED

> YOU MAY ENTER A NEW FUNDS AUTHORIZED, IF YOU WISH

> CHOOSE FROM:

> A AIRFARE

> P PER DIEM

> R REGISTRATION

> H HOTEL

> T TRAVEL

> N NONE REQUESTED

> U TUITION

> B BOOKS/MATERIALS

> D DIRECT OTHER

> I INDIRECT OTHER

> This field indicates intended use of authorized funds, e.g., hotel, airfare.

> Select FUNDS AUTHORIZED: R (REGISTRATION) AMOUNT AUTHORIZED: ?

> Type a Dollar Amount between 0 and 99999.99, 2 Decimal Digits.

> This field stores the dollar amount authorized by a service to an employee.

> AMOUNT AUTHORIZED: 20

> Select FUNDS AUTHORIZED: \<RET\>

> C.E.U. COMMENTS:

> This is a word-processing field.

> Enter additional comments regarding program/funding.

> 1\>INTERESTING SEMINAR ON PROVIDING CARE FOR THE NEW GENERAL SURGERY POST-OP.

> 2\>\<RET\>

> EDIT Option: \<RET\>

> CLINICAL POTPOURRI PAIDEMPLOYEE15,ONE JUN 30, 1993

> Select Student Name: \<RET\>

> Select TRAINING CLASS: \<RET\>

> Menu Access:

> The Quick Attendance Update of Past/Purged Classes is accessed through the

> Attendance Menu option.

> Quick Mandatory Training (MI) Update

> Description:

> This option allows an easy way to credit employee attendance at multiple mandatory training (MI) classes. The information displayed in this option is obtained from records in the PAID Employee file (#450) and the PRSE Student Education

> Tracking file (#452). Updated employee attendance is stored in the PRSE Student Education Tracking file (#452). This option should not be used for contract employees such as Fee Basis because the names of these individuals are not entered in the PAID Employee file.

> Additional Information:

> It is strongly suggested that the user create the required class through the Enter/ Edit Mandatory Training (MI Expanded) option and complete all fields including the Program Category and the Ending Date/Time fields. If program category has not been filed in, the Quick Mandatory Training (MI) Update option prompts the users to enter the program category.

> When a class is associated with a hospital-wide review group and the program category field has been completed, the program category data will be silently stuffed into the attendee's record when the employee is associated with the class. The program category is also silently stuffed into a person's record when the service creating the class is identical with the attendee's service entry in File 450. If the service associated with the class is different from the attendee's service (and the class is not associated with a hospital-wide review group), the software will prompt the user to enter a correct program category for the attendee. The software continues to store that program category entry until the service for another employee changes.

> Information on the mandatory inservice records created by this option can be found in the Service Mandatory Training (MI) Deficiency Report, the Service Training Report, the Individual Training Report, and the Individual Mandatory Training (MI) Deficiency Report. Attendance at required classes for contract employees should be entered through the Enter/Edit Class Attendance option.

> Menu Display:

> Select Package Coordinator Menu Option: 3 Attendance Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Class Attendance</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Create Non-Local CE and Enter Attendance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Modify Past Class Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Quick Attendance Update of Past/Purged Classes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Quick Mandatory Training (MI) Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Attendance Menu Option: 5 Quick Mandatory Training (MI) Update

> 1\. Example: Crediting attendance

> Date Class Attended: APR 7, 1994// \<RET\> (APR 07, 1994) Select Student Name: ?

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME

> DO YOU WANT THE ENTIRE NEW PERSON LIST? Y (YES)

> CHOOSE FROM:

> PAIDEMPLOYEE16,NINE 000000169

> PAIDEMPLOYEE16,SEVEN 000000167

> PAIDEMPLOYEE16,EIGHT 000000168

> PAIDEMPLOYEE15,SIX 000000156

> PAIDEMPLOYEE17,TEN 000000170

> .

> .

> .

> Select Student Name: PAIDEMPLOYEE16,EIGHT 000000168

> Enter any employee name.

> MANDATORY TRAINING CLASS DATE LAST ATTENDED

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 29%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1.</p>
</blockquote></th>
<th><blockquote>
<p>CPR</p>
</blockquote></th>
<th>OCT</th>
<th><blockquote>
<p>19,</p>
</blockquote></th>
<th><blockquote>
<p>1993</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><blockquote>
<p>OBSTRUCTED AIRWAY</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><blockquote>
<p>BLOOD ADMINISTRATION</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>FIRE SAFETY</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><blockquote>
<p>RADIATION HAZARD</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>INFECTION CONTROL</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7.</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ABUSE</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>PROTECTIVE DEVICES</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9.</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>DISTURBED BEHAVIOR</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11.</p>
</blockquote></td>
<td><blockquote>
<p>ADP SECURITY</p>
</blockquote></td>
<td>NOV</td>
<td><blockquote>
<p>9,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>ALL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Select TRAINING Class(es) to be added: ?

> Make a selection from the screen display, a range of numbers can be selected by using a HYPHEN, multiple selections can be made by separating them by COMMAS, select ALL or '^' to exit.

> E.G. 1 1-2 1,3 1-2,4-5 1,3-4 ALL Are examples of valid selections

> Select TRAINING Class(es) to be added: 1,3,4

> The following list denotes that the classes were recorded in the employee's PRSE Student Education File

> CPR PAIDEMPLOYEE16,EIGHT APR 7, 1994

> BLOOD ADMINISTRATION PAIDEMPLOYEE16,EIGHT APR 7, 1994

> FIRE SAFETY PAIDEMPLOYEE16,EIGHT APR 7, 1994

> Select Student Name: \<RET\>

> Date Class Attended: \<RET\>

> 2\. Example: Deleting attendance

> Date Class Attended: APR 7, 1994// \<RET\> (APR 07, 1994) Select Student Name: PAIDEMPLOYEE16,EIGHT 000000168

> Enter any employee name.

> MANDATORY TRAINING CLASS DATE LAST ATTENDED

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 29%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1.</p>
</blockquote></th>
<th><blockquote>
<p>CPR</p>
</blockquote></th>
<th>APR</th>
<th><blockquote>
<p>7,</p>
</blockquote></th>
<th><blockquote>
<p>1994</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><blockquote>
<p>OBSTRUCTED AIRWAY</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><blockquote>
<p>BLOOD ADMINISTRATION</p>
</blockquote></td>
<td>APR</td>
<td><blockquote>
<p>7,</p>
</blockquote></td>
<td><blockquote>
<p>1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>FIRE SAFETY</p>
</blockquote></td>
<td>APR</td>
<td><blockquote>
<p>7,</p>
</blockquote></td>
<td><blockquote>
<p>1994</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><blockquote>
<p>RADIATION HAZARD</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>INFECTION CONTROL</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7.</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ABUSE</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>PROTECTIVE DEVICES</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9.</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>DISTURBED BEHAVIOR</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11.</p>
</blockquote></td>
<td><blockquote>
<p>ADP SECURITY</p>
</blockquote></td>
<td>NOV</td>
<td><blockquote>
<p>9,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>ALL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Select TRAINING Class(es) to be added: 4

> SOMEONE,MICHELLE has completed FIRE SAFETY on APR 7, 1994

> Do you want to \[D\]elete or \[E\]dit this entry? D

> \*\* Entry Deleted\*\*

> Select Student Name: \<RET\>

> Date Class Attended: \<RET\>

> 3\. Example: Editing the attendance record

> Date Class Attended: APR 7, 1994// \<RET\> (APR 07, 1994) Select Student Name: PAIDEMPLOYEE16,EIGHT 000000168

> Enter any employee name.

> MANDATORY TRAINING CLASS DATE LAST ATTENDED

> ------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 29%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1.</p>
</blockquote></th>
<th><blockquote>
<p>CPR</p>
</blockquote></th>
<th>APR</th>
<th><blockquote>
<p>7,</p>
</blockquote></th>
<th><blockquote>
<p>1994</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><blockquote>
<p>OBSTRUCTED AIRWAY</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><blockquote>
<p>BLOOD ADMINISTRATION</p>
</blockquote></td>
<td>APR</td>
<td><blockquote>
<p>7,</p>
</blockquote></td>
<td><blockquote>
<p>1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>FIRE SAFETY</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><blockquote>
<p>RADIATION HAZARD</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>INFECTION CONTROL</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7.</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ABUSE</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>PROTECTIVE DEVICES</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9.</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>DISTURBED BEHAVIOR</p>
</blockquote></td>
<td>OCT</td>
<td><blockquote>
<p>19,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11.</p>
</blockquote></td>
<td><blockquote>
<p>ADP SECURITY</p>
</blockquote></td>
<td>NOV</td>
<td><blockquote>
<p>9,</p>
</blockquote></td>
<td><blockquote>
<p>1993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>ALL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Select TRAINING Class(es) to be added: 2

> PAIDEMPLOYEE16,EIGHT has completed FIRE SAFETY on APR 7, 1994

> Do you want to \[D\]elete or \[E\]dit this entry? E

> Any of the following field values can be edited by entering the correct information behind the //.

> BEGINNING DATE: APR 7, 1994// \<RET\>

> ENDING DATE: APR 7, 1994// \<RET\>

> CLASS CATEGORY: MEDICAL - NURSES// \<RET\>

> Select SVC REASON: MANDATORY TRAINING// \<RET\>

> PRSE PROGRAM/CLASS LENGTH HRS: 1// \<RET\>

> PROGRAM/CLASS LOCATION: PAIDEDSPONSOR,ONE// \<RET\>

> GOVERNMENT FUNDED: GOVERNMENT FUNDED// \<RET\>

> ROUTINE/NON-ROUTINE: ROUTINE// \<RET\>

> Select Student Name: \<RET\>

> Select Class Attended: \<RET\>

> Menu Access:

> The Quick Mandatory Training (MI) Update option is accessed through the

> Attendance Menu option.

## Chapter 6: Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> This menu allows the user to print class reports, education calendars, MI deficiency reports, registration rosters, and reports which list the employee's associated mandatory training groups and required classes. Data is stored in the PRSE Student Education Tracking file (#452) and the PRSE Education

> Registration file (#452.8).

> Additional Information:

> The data used in these reports was entered through the following options after registration or attendance was taken either through the Class Registration Enter/Delete option, the Enter/Edit Attendance option or an appropriate option listed below:

> 1\. Enter/Edit Mandatory Training (MI/Brief) option,

> 2\. Enter/Edit Mandatory Training (MI/Expanded) option,

> 3\. Enter/Edit Local Continuing Education option,

> 4\. Enter/Edit Other/Miscellaneous Training option,

> 5\. Enter/Edit Ward/Unit-Location option,

> 6\. Create Non-local CE and Enter Attendance option,

> 7\. Quick Attendance Update of Past/Purged Classes option,

> 8\. Modify Past Class Information option,

> 9\. Quick Mandatory Training (MI) Update option, and the

> 10\. Self Registration Enter/Delete

> Reports can be printed in either an 80 column or 132 column format. The 80 column format prints only the first 25 characters of the class name on the report. The 132 column format prints the entire class name on the report.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Menu Access:

> The Reports Menu option is accessed through the Package Coordinator Menu option and the Education Tracking Instructor Menu option.

> Class Registration Calendar Report

> Description:

> This option prints a listing of present and future classes by date or class title.

> Data used in this report is stored in the PRSE Education Registration file (#452.8).

> Additional Information:

> Classes with past dates will not show on this report.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 1 Class Registration Calendar Report

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: ?

> Enter a code from the list.

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: Calendar Year

> Select Calendar Year: 1994// ?

> This response must be a year i.e. 1990.

> Only present and future classes will show on this report. Classes with past dates will not appear.

> Select Calendar Year: 1994// \<RET\>

> This is an example of how to print a Class Registration Calendar Report sorted by

> Class Title:

> Select one of the following: D Date/Time

> C Class Title

> Select Sort Parameter(s): ?

> Enter a code from the list.

> Select one of the following: D Date/Time

> C Class Title

> Select Sort Parameter(s): Class Title

> Select SERVICE (Press Return for all Services): ?

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> ANSWER WITH PAID COST CENTER/ORGANIZATION NAME

> DO YOU WANT THE ENTIRE 56-ENTRY PAID COST CENTER/ORGANIZATION LIST? Y (YES)

> CHOOSE FROM:

> A & M MGT

> AMBULATORY CARE

> ANESTHESIOLOGY

> AUDIOLOGY

> BLIND REHAB

> CHAPLAIN

> CHIEF OF STAFF

> DENTAL

> DERMATOLOGY

> DIALYSIS

> DIETETICS

> DOMICILIARY CARE

> EDUCATION

> ENGINEERING

> FISCAL

> GENERAL COUNSEL

> '^' TO STOP: ^

> This is the service that is associated with the classes.

> Select SERVICE (Press Return for all Services): \<RET\>

> DEVICE: HOME// Enter appropriate device

> NOV 8, 1994 CLASS REGISTRATION CALENDAR PAGE: 1

> CLASS TITLE START DATE TYPE LENGTH LOCATION SERVICE

> --------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ADPAC CONFERANCE</p>
</blockquote></th>
<th><blockquote>
<p>11/12/94</p>
</blockquote></th>
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>.7</p>
</blockquote></th>
<th><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></th>
<th><blockquote>
<p>NURSING SERVICE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
<td><blockquote>
<p>11/18/94</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FIRE AND SAFETY REV</p>
</blockquote></td>
<td><blockquote>
<p>11/16/94</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>1.78</p>
</blockquote></td>
<td><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to continue or '^' to exit:

> This is an example of how to print a Class Registration Calendar Report sorted by date/time:

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: Calendar Year

> Select Calendar Year: 1994// \<RET\>

> Select one of the following: D Date/Time

> C Class Title

> Select Sort Parameter: Date/Time

> Select SERVICE (Press Return for all Services): \<RET\>

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> DEVICE: HOME// Enter appropriate device

> NOV 8, 1994 CLASS REGISTRATION CALENDAR PAGE: 1

> START DATE CLASS TITLE TYPE LENGTH LOCATION SERVICE

> --------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>11/12/94</p>
</blockquote></th>
<th><blockquote>
<p>ADPAC CONFERANCE</p>
</blockquote></th>
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>.7</p>
</blockquote></th>
<th><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></th>
<th><blockquote>
<p>NURSING SERVICE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11/16/94</p>
</blockquote></td>
<td><blockquote>
<p>FIRE AND SAFETY REV</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>1.78</p>
</blockquote></td>
<td><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11/18/94</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>PAIDEDSPONSOR,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NURSING SERVICE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to continue or '^' to exit:

> Menu Access:

> The Class Registration Calendar Report option is accessed through the Reports

> Menu option.

> Class Registration Roster Report

> Description:

> This option prints a list of students that are registered for any type of class. Non- local C.E. registration is the one exception since users cannot preregister for this type of class. Data is printed from the PRSE Education Registration file (#452.8).

> Additional Information:

> The data in this report is entered through the Class Registration option. This report can be used as a sign-in sheet for people attending the class. Blank lines are provided at the end of the report to assist with documenting last minute attendees. When no individual preregisters, the report still prints a sign-in sheet.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 2 Class Registration Roster Report

> CLASS NAME: ?

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE, OR

> TYPE OF EDUCATION

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> CHOOSE FROM:

> 5TH NURSING INFORMATICS NURSING SERVICE

> BIOETHICS NURSING SERVICE

> SICU ELECTRICAL SAFETY NURSING SERVICE

> TDC TEST NURSING SERVICE

> CLASS NAME: BIOETHICS NURSING SERVICE

> ...OK? YES// \<RET\> (YES)

> Select DATE: NOV 18, 1994// ?

> ANSWER WITH START DATE/TIME OF CLASS

> CHOOSE FROM:

> 11-18-1994

> Select DATE: NOV 18, 1994// \<RET\> NOV 18, 1994

> DEVICE: Enter appropriate device

> NOV 08, 1994 CLASS REGISTRATION ROSTER PAGE: 1

> NAME SSN SERVICE TITLE INITIALS\*

> --------------------------------------------------------------------------------

> BIOETHICS NOV 18, 1994

> PAIDEMPLOYEE15,EIGHT 000-00-0158 NURSING SERVICE ----­ PAIDEMPLOYEE16,SIX 000-00-0166 NURSING SERVICE COMPUTER SPECIA ----­ PAIDEMPLOYEE15,ONE 000-00-0151 NURSING SERVICE COMPUTER SPECIA ----­ PAIDEMPLOYEE16,TWO 000-00-0162 NURSING SERVICE COMPUTER SPECIA ----­ PAIDEMPLOYEE15,TEN 000-00-0150 NURSING SERVICE COMPUTER SPECIA ----­

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> ------------------------------ ----------- --------------- --------------- -----

> Press RETURN to continue or '^' to exit:

> \* Note: When the report is printed to a 132 column device, initials changes to

> signature.

> Menu Access:

> The Class Registration Roster Report option is accessed through the Reports Menu option.

> Service Mandatory Training (MI) Deficiency Report

> Description:

> This option allows the user to print a report of required classes not attended by the employee. Courses not attended as required are designated as deficiencies. Attendance data used to calculate this report is stored in the PRSE Student Education Tracking file. This data is checked against required classes located in the employee's record in File \#450 and the class information existing in the PRSE

> Program/Class file (#452.1). The MI class name must be found in File \#452.1. If the name has been deleted from this file then the MI class will never appear on this report.

> Additional Information:

> Attendance data used to calculate this report is entered through any of the several options which allow editing of mandatory or required inservice training. The report displays data for a fiscal or calendar year, for one or all hospital services, and for a single class or all classes. This option does not display projected deficiencies (i.e., those classes that technically are not yet identified as deficient but still have to be taken at a future time during the fiscal or calendar year). Only the names of current employees (as indicated in File \#450) are reflected in this report. The percentage of compliance for all MI classes is calculated through the following formula:

> <u>\# of individuals who attended all required MI classes assigned to the service</u>

> \# of individuals (in File \#450) assigned to a service and to an MI Class

> In calculating the percentage of compliance for review groups, the percentage is based on attendance at all classes. The individual is otherwise counted as deficient no matter how many classes were attended in the review group.

> If an individual class is selected, the percentage is calculated as follows:

> <u>\# of individuals who attended the selected class</u>

> \# of individuals (in File \#450) who are required to attend the selected class

> Note: If an employee is not assigned a mandatory training review group and/or a required class, the deficiency reports will indicate a compliance of 100%. In a future version, a message will print stating that the employee is not assigned to any review group or to any required class. It is suggested that all supervisors be given the Employee Mandatory Training Group/Class Report option for the purpose of identifying staff who are not assigned appropriate training review group(s) or required classes.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

> Reports

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 3 Service Mandatory Training (MI) Deficiency

> Report

> Select one of the following: C Calendar Year

> F Fiscal Year

> Select a Sort Parameter: ?

> Enter a code from the list.

> Select one of the following: C Calendar Year

> F Fiscal Year

> Select a Sort Parameter: Calendar Year

> Select Calendar Year: 1994// \<RET\> Enter a year for the printed report.

> Select SERVICE (Press Return for all Services): ?

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> ANSWER WITH PAID COST CENTER/ORGANIZATION NAME

> DO YOU WANT THE ENTIRE 66-ENTRY PAID COST CENTER/ORGANIZATION LIST? Y (YES)

> CHOOSE FROM:

> A & M MGT

> ACQUISITION & MATERIAL MGT

> ADMINISTRATION

> AMBULATORY CARE

> ANESTHESIOLOGY

> AUDIOLOGY/SPEECH PATHOLOGY

> BLIND REHAB

> CHAPLAIN

> CHIEF OF STAFF

> DENTAL

> DERMATOLOGY

> DIALYSIS

> DIETETICS

> DOMICILIARY CARE

> EDUCATION ENGINEERING EXTENDED CARE FISCAL

> '^' TO STOP: ^

> This is the service associated with the classes.

> Select SERVICE (Press Return for all Services): NURSING SERVICE Select TRAINING CLASS (Press return for all classes): ?

> Enter the name of the class.

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> CHOOSE FROM:

> 138-FIRE SAFETY

> ACLS

> ADP SECURITY

> ADVANCED LIFE SUPPORT

> BIOETHICS

> BLOOD ADMINISTRATION

> RESTRAINTS

> Select TRAINING CLASS (Press return for all classes): BIOETHICS DEVICE: HOME// Enter an appropriate device

> SERVICE MANDATORY TRAINING DEFICIENCY REPORT FOR CY 1994 NOV 8, 1994

PAGE: 1

> TITLE NAME CLASS

> --------------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 32%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Service: NURSING SERVICE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>% Compliance: 60</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PAIDEMPLOYEE17,ONE</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PAIDEMPLOYEE17,TWO</p>
</blockquote></td>
<td><blockquote>
<p>BIOETHICS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to continue or '^' to exit:

> This report indicates that two individuals who were required to attend the Bioethics class had not attended the class during calendar year 1994. Sixty percent of the individuals who were required to take the class have attended it.

> Menu Access:

> The Service Mandatory Training (MI) Deficiency Report option is accessed through the Reports Menu option.

> Service Training Report

> Description:

> This option allows the user to print service reports on programs or classes attended by employees. Data for the reports is stored in the Student Education Tracking file (#452).

> Additional Information:

> The data in this report is entered though any option which permits crediting class attendance. Reports display data for a fiscal/calendar year or a selected date range; for one or all hospital services; and for a single class or all classes. At the end of each report, the following information is provided:

> Class Total: The number of individuals who attended any (episode of a) class over a period of time.

> Service Total: The total number of individuals who attended any episode(s) of all classes over a period of time.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 4 Service Training Report

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: ?

> Enter a code from the list.

> Select one of the following:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>Calendar Year</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>Fiscal Year</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>Selected Date Range</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select a Sort Parameter: Calendar Year

> Select Calendar Year: 1994// ?

> Enter a year or time frame for the report. This response must be a year i.e. 1990. Select Calendar Year: 1994// \<RET\>

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education.

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> Select Sort Parameter: ?

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education.

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> This categorizes the classes by type of class. The user may also print all classes by selecting ALL.

> Select Sort Parameter: Mandatory Training (MI) Select SERVICE (Press Return for all Services): ?

> ANSWER WITH PAID COST CENTER/ORGANIZATION NAME

> DO YOU WANT THE ENTIRE PAID COST CENTER/ORGANIZATION LIST? Y (YES)

> CHOOSE FROM:

> A & M MGT

> ACQUISITION & MATERIAL MGT

> ADMINISTRATION

> AMBULATORY CARE

> ANESTHESIOLOGY

> AUDIOLOGY/SPEECH PATHOLOGY

> BLIND REHAB

> CHAPLAIN

> CHIEF OF STAFF

> DENTAL

> DERMATOLOGY

> DIALYSIS

> DIETETICS

> '^' TO STOP: ^

> This is the service associated with the classes.

> Select SERVICE (Press Return for all Services): NURSING SERVICE Select TRAINING CLASS (Press return for all classes): ?

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> CHOOSE FROM:

> 138-FIRE SAFETY

> ACLS

> ADP SECURITY

> BIOETHICS

> BLOOD ADMINISTRATION

> RESTRAINTS

> Select TRAINING CLASS (Press return for all classes): BIOETHICS DEVICE: HOME// Enter an appropriate device

> M.I. SERVICE TRAINING REPORT FOR CY 1994 NOV 8, 1994 PAGE: 1

Class

> Class Name Class Presenter Length

> Student Name Title

Date

> -------------------------------------------------------------------------------- Service: NURSING SERVICE

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 34%" />
<col style="width: 10%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BIOETHICS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>2.50</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE,SIX</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>OCT 28, 1994</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE17,THREE</p>
</blockquote></td>
<td><blockquote>
<p>RN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>OCT 28, 1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE17,FOUR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>OCT 27, 1994</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE17,FIVE</p>
</blockquote></td>
<td><blockquote>
<p>LPN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NOV 3, 1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE16,SIX</p>
</blockquote></td>
<td><blockquote>
<p>COMPUTER SPECIALIST</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>OCT 13, 1994</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE15,ONE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>MAR 31, 1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE16,TWO</p>
</blockquote></td>
<td><blockquote>
<p>RN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>MAR 31, 1994</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAIDEMPLOYEE16,TWO</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>OCT 19, 1994</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAIDEMPLOYEE1,FOUR</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>JAN 28, 1994</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Class Total: 9 Class Hours: 22.50

> Service Total: 9 Service Hours: 22.50

> Press RETURN to continue or '^' to exit:

> Menu Access:

> The Service Training Report option is accessed through the Reports Menu option.

> Employee Mandatory Training Group/Class Report

> Description:

> This option prints two reports: one which prints data by review group, and lists the members of each group; and a second report which shows the mandatory training groups and classes associated with an employee. The report may be printed for selected employees or all employees in a given service. Data is printed from the PAID Employee file (#450).

> Additional Information:

> The data in this report is entered in through the Create Mandatory Training (MI) Groups and the Assign/Delete Mandatory Training Groups for Staff/Services options found in the Package Set-up Menu. In printing the Employee Mandatory Training Group/Class Report, all individual MI classes assigned to an employee are printed after the mandatory training groups. The individual classes are found under the mandatory training group heading of Indv. Classes.

> Note: If an employee is not assigned a mandatory training review group and/or a required class, the deficiency reports will indicate a compliance of 100%. In a future version, a message will print stating that the employee is not assigned to any review group or to any required class. It is suggested that all supervisors be given the Employee Mandatory Training Group/Class Report option for the purpose of identifying staff who are not assigned appropriate training review group(s) or required classes.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 5 Employee Mandatory Training Group/Class Report

> Select one of the following:

> M Mandatory Training Group/Employee Report

> E Employee Mandatory Training Group/Class Report

> Select Option: ??

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training Group/Employee Report

> E Employee Mandatory Training Group/Class Report

> Data can be printed by review group or by employee.

> Example 1: Lists employees associated with a training/review group.

> Select Option: Mandatory Training Group/Employee Report

> Select REVIEW GROUP (Press RETURN for all): RN

> 1 RN

> 2 RN DIALYSIS

> 3 RN/CCC

> 4 RN/ICU

> 5 RN/PSYCH

> CHOOSE 1-5: 1

> DEVICE: HOME// Enter an appropriate device

> REVIEW GROUP MEMBERS Nov 08, 1994

PAGE: 1

> REVIEW GROUP GROUP MEMBER DATE ASSIGNED

> --------------------------------------------------------------------------------

> RN

> PAIDEMPLOYEE17,ONE JAN 01, 1994

> PAIDEMPLOYEE16,SIX JAN 01, 1994

> PAIDEMPLOYEE15,ONE JAN 01, 1994

> PAIDEMPLOYEE16,TWO JAN 01, 1994

> PAIDEMPLOYEE15,TEN JAN 01, 1994

> PAIDEMPLOYEE17,TWO JAN 01, 1994

> Select one of the following:

> M Mandatory Training Group/Employee Report

> E Employee Mandatory Training Group/Class Report

> Example 2: Lists the mandatory training/review groups associated with an employee.

> Select Option: Employee Mandatory Training Group/Class Report

> Select SERVICE: NURSING SERVICE// \<RET\> The default value is the user's service.

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> Select one of the following:

> A (A)ll Employees For a Service

> S (S)elected Service Employees

> You can select certain employees within a single service, or select an entire service.

> Select ASSIGNMENT OPTION: S (S)elected Service Employees

> Select EMPLOYEE: PAIDEMPLOYEE15,TEN 000-00-0150

> Select Another Employee: PAIDEMPLOYEE16,SIX 000-00-0166

> Select Another Employee: \<RET\>

> DEVICE: HOME// Enter an appropriate device

> EMPLOYEE MANDATORY TRAINING GROUP/CLASS REPORT NOV 08, 1994

> NURSING SERVICE

> EMPLOYEE REVIEW GROUP DATE ASSIGNED PROGRAM/CLASS PAGE: 1

> --------------------------------------------------------------------------------

> PAIDEMPLOYEE16,SIX

> HOSPITAL JAN 01, 1994

> JAN 01, 1994 FIRE SAFETY

> JAN 01, 1994 SEXUAL HARASSMENT I

> LPN JAN 01, 1994

> JAN 01, 1994 BIOETHICS

> JAN 01, 1994 BLOOD PATHOGEN

> JAN 01, 1994 CPR

> JAN 01, 1994 DISTURBED BEHAVIOR

> JAN 01, 1994 INFECTION CONTROL

> JAN 01, 1994 OBSTRUCTED AIRWAY

> JAN 01, 1994 PATIENT ABUSE

> JAN 01, 1994 RADIATION HAZARD

> INDV. CLASSES Separate MI classes assigned to the employee

> FEB 21, 1994 WORDPERFECT

> PAIDEMPLOYEE15,TEN

> HOSPITAL JAN 01, 1994

> JAN 01, 1994 FIRE SAFETY

> JAN 01, 1994 SEXUAL HARASSMENT I

> LPN JAN 01, 1994

> JAN 01, 1994 BIOETHICS

> JAN 01, 1994 BLOOD PATHOGEN

> JAN 01, 1994 CPR

> JAN 01, 1994 DISTURBED BEHAVIOR

> JAN 01, 1994 INFECTION CONTROL

> JAN 01, 1994 OBSTRUCTED AIRWAY

> JAN 01, 1994 PATIENT ABUSE

> JAN 01, 1994 RADIATION HAZARD

> Press RETURN to continue or '^' to exit:

> Menu Access:

> The Employee Mandatory Training Group/Class Report option is accessed through the Reports Menu option.

> OLDE Training Coding Report

> Description:

> This option prints a report of mandatory, continuing education, and other/miscellaneous class information by employee SSN in OLDE coding order. Ward/unit­ location classes are not considered appropriate for OLDE submission due to the length of the inservices (usually under one hour); these classes are not reflected on the completed OLDE report. The report may be printed for all or selected employees in a specific service or the entire facility. Data is printed from the PAID Employee file (#450) and the PRSE Student Education Tracking file (#452).

> Additional Information:

> This option prints a listing of student classes (targeted for OLDE data entry) sorted by the student's social security number.

> 1\. If a complete data report is chosen, only the classes with complete data print. Cost data, accrediting organization, and contact hour information is

> not captured nor displayed for mandatory and other/miscellaneous classes. It is presumed to be 0 or not applicable unless manually indicated on the report submitted to Human Resources. Fund category information is not collected

> in this version of the software.

> 2\. If an incomplete data report is chosen, only the classes with incomplete data print. The reports display essential information to correctly identify the record, e.g., (student) SSN, student name, program/class title, and the date the program/class ended. Only the missing data fields are displayed.

> The data in this report is entered in through any of the options under the Enter/ Edit Class Information Menu option, the Create Non-local CE and Enter Attendance option, the Quick Attendance Update of Past/Purged Classes and the Quick Mandatory Training (MI) Update option.

> It is suggested that the Complete Training Coding Report be printed by each service, reviewed and submitted to Human Resources. Staff within the Human Resources Service can be assigned the OLDE Training Coding Report option as necessary.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

> 1 Class Registration Calendar Report

> 2 Class Registration Roster Report

> 3 Service Mandatory Training (MI) Deficiency Report

> 4 Service Training Report

> 5 Employee Mandatory Training Group/Class Report

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Reports Menu Option: 6 OLDE Training Coding Report

> Example 1: A report of all employees for all services.

> Select SERVICE (Press Return for all Services): \<RET\>

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: c calendar Year

> Select Calendar Year: 1994// \<RET\>

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: ?

> 'Complete' will only print those records with full OLDE data.

> 'Incomplete' will only print those records without full OLDE data.

> Enter either 'Complete' or 'Incomplete'.

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: Incomplete records

> DEVICE: HOME// Enter an appropriate device

> OLDE TRAINING CODING REPORT NOV 08, 1994

> INCOMPLETE DATA FOR CALENDAR YEAR 1994 PAGE: 1

> --------------------------------------------------------------------------------

> SSN: 000000162

> Student Name: PAIDEMPLOYEE16,TWO - LABORATORY

> Prg/Cls Title: CPR (M)

> Date Prg/Cls Ended:

> Routine/Non-Routine:

> SSN: 000000171

> Student Name: PAIDEMPLOYEE17,ONE - NURSING SERVICE

> Prg/Cls Title: FIRE & SAFETY (M)

> Date Prg/Cls Ended: 10/31/94

> Routine/Non-Routine:

> SSN: 000000150

> Student Name: PAIDEMPLOYEE15,TEN - IRM

> Prg/Cls Title: WIRELESS LANS (C)

> Date Prg/Cls Ended: 05/02/94

> Cls Hrs On Duty:

> Routine/Non-Routine:

> Direct Cost:

> Indirect Cost:

> Student Expense:

> Contact Hours:

> .

> .

> .

> Additional records are printed for each employee within the service. The letter in the parentheses behind the program/class title name indicates the type of class, i.e., (M) = mandatory, (C) = continuing education, (O) = other/miscellaneous.

> Example 2: A report of all employees for a selected service.

> Select SERVICE (Press Return for all Services): LABORATORY

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> Select one of the following:

> A (A)ll Employees For a Service

> S (S)elected Service Employees

> Select ASSIGNMENT OPTION: A (A)ll Employees For a Service

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: c calendar Year

> Select Calendar Year: 1994// \<RET\>

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: ?

> 'Complete' will only print those records with full OLDE data.

> 'Incomplete' will only print those records without full OLDE data.

> Enter either 'Complete' or 'Incomplete'.

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: Incomplete records

> DEVICE: HOME// Enter an appropriate device

> OLDE TRAINING CODING REPORT NOV 08, 1994

> INCOMPLETE DATA FOR CALENDAR YEAR 1994 PAGE: 1

> --------------------------------------------------------------------------------

> SSN: 000000162

> Student Name: PAIDEMPLOYEE16,TWO - LABORATORY

> Prg/Cls Title: CPR (M)

> Date Prg/Cls Ended:

> Routine/Non-Routine:

> .

> .

> .

> Additional records are printed for each employee within the service. The letter in the parentheses behind the program/class title name indicates the type of class, i.e., (M) = mandatory, (C) = continuing education, (O) = other/miscellaneous.

> Example 3: A report of selected employees for a selected service:

> Select SERVICE (Press Return for all Services): NURSING SERVICE

> The Service prompt is displayed only when the user holds the PRSE CORD key. When the user holds the PRSE SUP key, the service defaults to the user's service and the prompt is not displayed.

> Select one of the following:

> A (A)ll Employees For a Service

> S (S)elected Service Employees

> You can select all the employees for a service, or single or multiple individual employees from a service.

> Select ASSIGNMENT OPTION: s (S)elected Service Employees

> Select EMPLOYEE: PAIDEMPLOYEE17,TWO 000000172

> Select Another Employee: PAIDEMPLOYEE17,ONE 000000171

> Select Another Employee: \<RET\>

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: c calendar Year

> Enter the year or time frame for the report.

> Select Calendar Year: 1994// \<RET\>

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: ?

> 'Complete' will only print those records with full OLDE data.

> 'Incomplete' will only print those records without full OLDE data.

> Enter either 'Complete' or 'Incomplete'.

> Select one of the following:

> C Complete records

> I Incomplete records

> Select records to print: Incomplete records

> DEVICE: HOME// Enter an appropriate device

> OLDE TRAINING CODING REPORT NOV 08, 1994

> INCOMPLETE DATA FOR CALENDAR YEAR 1994 PAGE: 1

> --------------------------------------------------------------------------------

> SSN: 000000172

> Student Name: PAIDEMPLOYEE17,TWO - NURSING SERVICE

> Prg/Cls Title: 10/18 NEW CLASS (M)

> Date Prg/Cls Ended:

> Routine/Non-Routine:

> SSN: 000000171

> Student Name: PAIDEMPLOYEE17,ONE - NURSING SERVICE

> Prg/Cls Title: BLOOD ADMINISTRATION (M)

> Date Prg/Cls Ended: 10/31/94

> Routine/Non-Routine:

> SSN: 000000171

> Student Name: PAIDEMPLOYEE17,ONE - NURSING SERVICE

> Prg/Cls Title: WORDPERFECT (C)

> Date Prg/Cls Ended: 11/01/94

> Direct Cost:

> Indirect Cost:

> Student Expense:

> Press Return To Continue or '^' to exit: \<RET\>

> Example 4: Completed Reports:

> Apply the same steps to print out a complete report. All appropriate fields will display with data. Refer to Additional Information for supplementary information.

> Menu Access:

> The OLDE Training Coding Report option is accessed through the Reports Menu option.

> Individual Training Report

> Description:

> This option allows an individual employee to view and print his/her own educational record of attended courses. Data is printed from the PRSE Student Education Tracking file.

> Additional Information:

> When the user holds the PRSE CORD key, he/she can print any individual's report. If the user holds the PRSE SUP key, she/he can print any student's record in the user's assigned service. When a user does not hold any key and enters the option, the Employee Name prompt does not appear and the report(s) generated will be for the employee executing the option. The data in this report is entered through any of the attendance options. At the end of an each report a count of the classes attended

> is displayed.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>Class Registration Calendar Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Class Registration Roster Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service Mandatory Training (MI) Deficiency Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Service Training Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Employee Mandatory Training Group/Class Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OLDE Training Coding Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Individual Training Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Individual Mandatory Training (MI) Deficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Screen Prints:

> Select Employee Education Tracking Menu Option: 7 Individual Training Report

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range

> Select a Sort Parameter: ?

> Enter a code from the list.

> Select one of the following: C Calendar Year

> F Fiscal Year

> S Selected Date Range Select a Sort Parameter: Calendar Year Select Calendar Year: 1994// ?

> This response must be a year i.e. 1994.

> This is the year or the time frame for the report.

> Select Calendar Year: 1994// \<RET\>

> Select one of the following:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>M</p>
</blockquote></th>
<th><blockquote>
<p>Mandatory Training (MI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>Continuing Education.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>Other/Miscellaneous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>Ward/Unit-Location Training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Sort Parameter: ?

> Enter a code from the list.

> Select one of the following:

> M Mandatory Training (MI) C Continuing Education.

> O Other/Miscellaneous

> W Ward/Unit-Location Training

> A All

> This categorizes the classes by type of class; you can print all reports by entering in

> A for ALL.

> Select Sort Parameter: Mandatory Training (MI)

> Select TRAINING CLASS (Press return for all classes): ?

> ANSWER WITH PRSE PROGRAM/CLASS PROGRAM/CLASS TITLE

> DO YOU WANT THE ENTIRE PRSE PROGRAM/CLASS LIST? Y (YES)

> CHOOSE FROM:

> 138-FIRE SAFETY

> ACLS

> ADP SECURITY

> ADVANCED LIFE SUPPORT

> BIOETHICS

> BLOOD ADMINISTRATION

> RESTRAINTS

> Select TRAINING CLASS (Press return for all classes): BIOETHICS

> Select Employee Name: ?

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME

> DO YOU WANT THE ENTIRE NEW PERSON LIST? Y (YES)

> CHOOSE FROM:

> PAIDEMPLOYEE16,NINE

> PAIDEMPLOYEE16,SEVEN

> PAIDEMPLOYEE16,EIGHT

> PAIDEMPLOYEE15,SIX 000000156

> Select Employee Name: PAIDEMPLOYEE15,ONE 000000151

> DEVICE: HOME// Enter an appropriate device

> INDIVIDUAL M.I. TRAINING REPORT FOR CY 1994 OCT 26, 1994 PAGE: 1

Class

> Class Name Class Presenter Length(Hrs.) Date

> ------------------------------------------------------------------------------------------------- Service: NURSING SERVICE Name:PAIDEMPLOYEE15,ONE Title:

> BIOETHICS 3.25 FEB 18, 1994

> Class Total: 1 Class Hours: 3.25

> Press Return To Continue or '^' to exit: \<RET\>

> The class total information reflects the total number of classes taken by the employee. The number of class hours indicates the total number of training hours associated with the employee.

> Menu Access:

> The Individual Training Report option is accessed through the Reports Menu and the Employee Menu options.

> Individual Mandatory Training (MI) Deficiency

> Description:

> This option allows the user to print required classes not attended by the employee. Mandatory or required courses not attended are designated as deficiencies. Data contained in this report is stored in the PRSE Student Education Tracking file (#452).

> Additional Information:

> The data in this report is entered through the several options which allow editing of mandatory or required inservice training. The report can display data for a fiscal or calendar year. This option does not display projected deficiencies (i.e., those classes that technically are not yet identified as deficient but still have to be taken at a future time during the fiscal or calendar year). The employee's attendance at MI classes is checked against required classes located in the employee's record in File

> \#450 and the class information existing in the PRSE Program/Class file (#452.1). The MI class name must be found in File \#452.1. If the name has been deleted from this file then the MI class will never appear on this report.

> When the user holds the PRSE CORD key, he/she can print any individual's report. If the user holds the PRSE SUP key, she/he can print any student's record in the user's assigned service. When a user does not hold any key and enters the option, the Employee Name prompt does not appear and the report(s) generated will be for the employee executing the option. The data in this report is entered through any of the attendance options associated with mandatory inservice training.

> Note: If an employee is not assigned a mandatory training review group and/or a required class, the deficiency reports will indicate a compliance of 100%. In a future version, a message will print stating that the employee is not assigned to any review group or to any required class. It is suggested that all supervisors be given the Employee Mandatory Training Group/Class Report option for the purpose of identifying staff who are not assigned appropriate training review group(s) or required classes.

> Menu Display:

> Select Package Coordinator Menu Option: 4 Reports Menu

> 1 Class Registration Calendar Report

> 2 Class Registration Roster Report

> 3 Service Mandatory Training (MI) Deficiency Report

> 4 Service Training Report

> 5 Employee Mandatory Training Group/Class Report

> 6 OLDE Training Coding Report

> 7 Individual Training Report

> 8 Individual Mandatory Training (MI) Deficiency

> Screen Prints:

> Select Employee Education Tracking Menu Option: 8 Individual Mandatory

> Training (MI) Deficiency

> Select one of the following: C Calendar Year

> F Fiscal Year

> Select a Sort Parameter: ?

> Enter a code from the list.

> Select one of the following:

> C Calendar Year

> F Fiscal Year

> Select a Sort Parameter: Calendar Year

> Select Calendar Year: 1994// \<RET\> This is the year for the report.

> Select EMPLOYEE NAME: ?

> ANSWER WITH NEW PERSON NAME, OR INITIAL, OR SSN, OR NICK NAME

> DO YOU WANT THE ENTIRE NEW PERSON LIST? Y (YES)

> CHOOSE FROM:

> PAIDEMPLOYEE15,SIX 000000156

> PAIDEMPLOYEE17,SIX 000000176

> PAIDEMPLOYEE17,SEVEN 000000177

> PAIDEMPLOYEE17,EIGHT 000000178

> PAIDEMPLOYEE17,NINE 000000179

> PAIDEMPLOYEE18,TEN 000000180

> PAIDEMPLOYEE18,ONE 000000181

> PAIDEMPLOYEE18,TWO 000000182

> .

> .

> .

> Select EMPLOYEE NAME: PAIDEMPLOYEE18,TWO 000000182

> DEVICE: HOME// Enter an appropriate device

> INDIVIDUAL M.I. DEFICIENCY REPORT BY LOCATION/CLASS FOR CY 1994 APR 5, 1994 PAGE: 1

> NAME TITLE SERVICE CLASS

> ---------------------------------------------------------------------------------------

> PAIDEMPLOYEE18,TWO NURSING CPR2

> SEXUAL HARASSMENT

> BLOOD ADMINISTRATION

> Press Return To Continue or '^' to exit: \<RET\>

> Menu Access:

> The Individual Training Report option is accessed through the Reports Menu and the Employee Education Tracking Menu options.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users of the system.
> Application A set of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of DHCP applications are the MAS and Education Tracking applications.
> Application The person responsible for implementing a set of computer
> Coordinator programs (software application) developed to support a specific functional area such as Education Tracking, MAS, etc.
> Approving Body This is a set of codes. It indicates whether the training is an
> (OLDE) approved continuing education activity.
> Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up storage space on the system.
> Attendance The act of being present in a class. Information on class attendance cannot be entered for future dates, only current and past dates. Registration is not a prerequisite.
> Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
> CE Continuing Education. This is a planned educational activity intended to build upon the educational and experiential base of a professional.
> CEU Continuing Education Unit. Ten contact hours of participation in an organized continuing education experience, under responsible leadership, capable of direction, and qualified
> instruction.
> Class Category Identifies broad types of training. The source of this field is form SF182. The data stored in this file should only be edited by a developer.
> Contact Hours This value is a number which identifies the number of hours
> (OLDE) actually spent in class. An hour is defined as a 50-60minute classroom or clinical instructional session.
|     |     |     |
|-----|-----|-----|
|     |     |     |
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Contingency Plan</p>
</blockquote></td>
<td><blockquote>
<p>A plan which assigns responsibility and defines procedures</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>for use of the backup/restart/recovery and emergency</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>preparedness procedures selected for the computer system</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>based on risk analysis for that system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Continuing</p>
</blockquote></td>
<td><blockquote>
<p>Classes that are held on the facility grounds, and</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Education (Local)</p>
</blockquote></td>
<td><blockquote>
<p>sponsored by the medical center or other organization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Typically there is no tuition, registration, or travel costs</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>involved for attendees.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Continuing</p>
</blockquote></td>
<td><blockquote>
<p>Classes that are held off site by an organization other than</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Education</p>
</blockquote></td>
<td><blockquote>
<p>the medical center. Typically there are tuition, registration,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(Non-local)</p>
</blockquote></td>
<td><blockquote>
<p>and/or travel costs involved for attendees.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Course Title</p>
</blockquote></td>
<td><blockquote>
<p>This is a free text field and is the name of the training course.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>(OLDE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cursor</p>
</blockquote></td>
<td><blockquote>
<p>A visual position indicator (e.g., blinking rectangle or an</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>underline) on a CRT that moves along with each character as</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>it is entered from the keyGROUP.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Data Dictionary</p>
</blockquote></td>
<td><blockquote>
<p>A description of file structure and data elements within a</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Date of Completion</p>
</blockquote></td>
<td><blockquote>
<p>A date field. The date an employee finished an instance of</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(OLDE)</p>
</blockquote></td>
<td><blockquote>
<p>training. If two courses are completed on the same date,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>then the date of completion for one of the courses must be</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>changed to any date that is within 5 days of the actual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>completion date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Direct Costs</p>
</blockquote></td>
<td><blockquote>
<p>This value is a number. It is the total dollar amount</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(OLDE)</p>
</blockquote></td>
<td><blockquote>
<p>expended in order to obtain or provide the training (e.g.,</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>tuition, books, supplies).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Device</p>
</blockquote></td>
<td><blockquote>
<p>A hardware input/output component of a computer system</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>(e.g., CRT, printer).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DHCP</p>
</blockquote></td>
<td><blockquote>
<p>Decentralized Hospital Computer Program.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit</p>
</blockquote></td>
<td><blockquote>
<p>Used to change/modify data typically stored in a file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Employee</p>
</blockquote></td>
<td><blockquote>
<p>An individual with an entry in the Paid Employee file (#450)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>at that medical facility where the class is being held.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Employee Cost</p>
</blockquote></td>
<td><blockquote>
<p>This is a set of codes. It identifies the estimated amount of</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(OLDE)</p>
</blockquote></td>
<td><blockquote>
<p>employee out-of-pocket expenses for government financed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>training only.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Expert Panel</p>
</blockquote></td>
<td><blockquote>
<p>Previously referred to as a SIUG (Special Interest User</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 49%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Group). A committee which advises programmers about the development of a particular system/package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>File</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>The MUMPS construct in which data is stored for retrieval at a later time. A computer record of related information (e.g., Education (DB) File, Patient file, Prescription file).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>File Manager or FileMan</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Within this manual, FileManager or FileMan is a reference to VA FileMan. A set of MUMPS routines used to enter, edit, print, and sort/search related data in a file; a data base.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Fund Category</p>
<p>(OLDE)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>This is a set of codes. It identifies the provider of the funds for the government financed funds.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Identifier</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A field associated with an item and for which values occur only once among all instances of that item. For example, a Social Security Number would be an identifier for a patient, since no two people have the same number, while the Date of Birth is not an identifier, since many patients may be born on the same date. Once the value of an identifier is indicated to the system, the information associated with that item can be retrieved.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Indirect Costs</p>
<p>(OLDE)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>This value is a number. It is the amount paid for transportation, lodging, and subsistence.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Inservice</p>
<p>Training</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Consists of activities intended to assist the professional to acquire, maintain, and/or increase competence in fulfilling the assigned responsibilities specific to the expectations of the employer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>An Information Systems Center where software is developed and software applications are provided user and technical support.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Laygo</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>An acronym for Learn As You Go. A technique used by FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data from one file to another.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mandatory</p>
<p>Inservice</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A class which is considered a required course at the medical center. Usually there is a requirement to take the class on a periodic basis (annually, every two years), but it could be taken one time only, e.g., New Employee Orientation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M.I.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Mandatory Inservice. Refer to Mandatory Inservice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M.I. Training</p>
<p>Group</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A group of classes which are considered required courses at the medical center.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
> M or MUMPS Massachusetts (General Hospital) Utility Multi-
> Programming System. This is the programming language used to write all VA DHCP applications.
> Menu A set of options or functions available to users in editing, formatting, generating reports, etc.
> Miscellaneous Classes that don't fit into any of the following categories: Training Mandatory Inservice, Continuing Education, or
> Unit/Location training (e.g., Health Summary Training, Mumps, etc.).
> Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. The namespace is used as the prefix for all routines and globals used by the application. The Education Tracking application uses PRSE as its namespace.
> Non-employee An individual who does not have an entry in the Paid Employee file (#450) at the facility where the class is being held. The person may be a federal employee at another facility, a student, or a visitor attending an educational presentation.
> Non-Routine This term is used to explain the effect of class information on job qualifications. When a class is identified as non-
> routine, the program/class information enhances job qualifications.
> Objective Training objective. A brief statement of course content and the outcomes expected.
> Off Duty Hours This value is a number. It indicates the duration of the
> (OLDE) training in the number of non-duty hours (hours in an off duty or nonwork status).
> OLDE On Line Data Entry. The process used by the Human Resources Management Service to enter certain training information into the PAID system in Austin, TX for inclusion in the employment records and the official personnel file (OPF).
> On Duty Hours This value is a number. It indicates the duration of the
> (OLDE) training in the number of on duty hours (hours in a work status).
> Option A routine that is invoked by the user to enter/edit data or print reports.
|     |     |     |
|-----|-----|-----|
|     |     |     |
> Other
> Training
> Package
> Password
> Pointer
> Printer
> Program
> Program Category
> (OLDE)
> Purpose of
> Training
> Purpose (OLDE) Queuing
> Registration
> Response Time
> \<RET\>
Classes that don't fit into any of the following categories: Mandatory Inservice, Continuing Education, or Unit/Location training (e.g., Health Summary Training, Mumps, etc.).
See application.
A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
A special type of File Manager data that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
A device for printing (on paper) data which is processed by a computer system.
A set of M commands and arguments, created, stored, and retrieved as a single unit using the M programming
language.
Set of codes. Identifies broad types of training and provides additional information about the specific kind of training.
The reason for the student's training. The source of this field is form SF182. Data stored in this file should only be edited by a developer.
A set of codes. Indicates why the employee received the training.
The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
The act of signing up for a class before actually attending the class. Information on registration cannot be entered for past dates, only current and future dates. The student does not need to be registered to attend the class.
The average amount of time the user must wait between the time he/she responded to a question at the terminal and the time the system responds by displaying data and/or the next question.
Carriage return.
> Routine
> Security Key
> Security System
> Sensitive
> Information
> Service
> Service Reason
> Site Configurable
> Software Subcode (OLDE) Source (OLDE)
1\. This term is used to explain the effect of class information on job qualifications. When a class is identified as routine, the program/class information does not enhance job qualifications. 2. In M, a computer program is called a
routine.
A function which unlocks specific options and makes them accessible to an authorized user (Refer to the Package Management chapter). In the Education Tracking system, the following keys have been added:
1\. PRSE CORD - This key allows the user to access data for all services.
2\. PRSE SUP - This key allows the user to access data only for his/her own service.
3\. PRSE TRAIN - This key allows the user to access data only for his/her own ward.
4\. A user having no assigned key can access their own data.
A part of Kernel that controls user access to the various computer applications. When a user signs-on, the security system determines the privileges of the user, assigns security keys, tracks usage, and controls the menus or options the
user may access. It operates in conjunction with Menu
Manager.
Any information which requires a degree of protection and which should be made available only to authorized users.
This is the hospital division where an employee works (e.g. Nursing, Dietetics, etc.). This is an entry in the Paid Employee file (#450).
The service's reason for presenting a particular class. Unlike Purpose of Training and Class Category data stored in the PRSE Svc Reasons for Training file (#452.6) can be edited by a designated user.
A term used to refer to features in the system that can be modified to meet the needs of each site.
A generic term referring to a related set of computer programs (e.g., Education Tracking).
A set of codes. Indicates whether the training is financed by the government or by the employee.
A set of codes. Indicates the source of the training received
(e.g., agency, commercial).
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Task Manager</p>
</blockquote></td>
<td><blockquote>
<p>A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See</p>
<p>Queuing.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tele­</p>
<p>communications</p>
</blockquote></td>
<td><blockquote>
<p>Any transmission, emission, or reception of signs, signals, writing, images, sounds or other information by wire, radio, visual, or any electromagnetic system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Terminal</p>
</blockquote></td>
<td><blockquote>
<p>A device used to send and receive data from a computer system (i.e., keyGROUP and CRT, or printer with a keyGROUP).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Ward/Unit- Location Training</p>
</blockquote></td>
<td><blockquote>
<p>Classes associated with a nursing ward or location only.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>User</p>
</blockquote></td>
<td><blockquote>
<p>A person who enters and/or retrieves data in a system, usually utilizing a CRT.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verify Code</p>
</blockquote></td>
<td><blockquote>
<p>A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeable with password.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix A: Supplemental Information for Part-time Physicians (Patch PRS\*4.0\*93)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contents

> Human Resources Personnel........................................................................... A-2

> New Options ................................................................................................. A-2

> PT Physician Menu................................................................................... A-2

> Employee Menu ............................................................................................. A-24

> Changed Options ........................................................................................ A-24

> New Options ............................................................................................... A-24

> PT Physician with Memorandum Menu ................................................ A-24

> Timekeepers Main Menu............................................................................... A-46

> Changed Options ........................................................................................ A-46

> New Options ............................................................................................... A-46

> PT Physician Menu................................................................................. A-46

> Payroll Main Menu ........................................................................................ A-56

> New Options ............................................................................................... A-56

> PT Physician Menu................................................................................. A-56

> Payroll Supervisor Menu............................................................................... A-64

> Changed Option.......................................................................................... A-64

> T&A Supervisor Menu ................................................................................... A-64

> Changed Options ........................................................................................ A-64

> New Options ............................................................................................... A-65

> PT Physician Menu................................................................................. A-65

> Data Supplement ........................................................................................... A-86

> PTP ESR DATA FILE DESCRIPTIONS .................................................. A-86

> WORK SUMMARY SCREEN DESCRIPTIONS ...................................... A-89

> Human Resources Personnel

> Human Resources Personnel

> New Options

> PT Physician Menu

> This new menu contains all of the options required for Human Resources personnel to process part-time physicians with a Memorandum of Service Level Expectations.

> Enter Memoranda

> This option allows Human Resources personnel to enter a Memorandum of Service

> Level Expectations for part-time physicians.

> Once you enter the employee’s name, information such as the employee’s SSN, and pay information are displayed. You are then prompted to enter the start date of the pay period (the end date is calculated automatically), the agreed hours, and any initial comments. An electronic signature code is required to complete the memorandum.

> The software will automatically assign the PRSP EMP security key to the part-time physician when a new memorandum is entered. This key provides access to the PT Physician With Memorandum Menu \[PRSP PTP MENU\].

![](paid-version-4-user-manual/027.png)Human Resources Personnel

> PAIDPTP,ONE 000·28·0001

> VA TIME &ATTENDANCE SYSTEM

> Enter PT Physician Memoranda

> Duty Basis: 2 FLSA: E Normal Hours: 10

> Date: 10/16 (OCT 16, 2005) Date: OCT 14, 2006

> reed Hours must be equally divisible by 26 Pay Periods.

> 5/13/05

> xxx.xx. 0001

Comp/Flex:

Station: 528

> /8 = 260, 1/4 = 520, 3/8 = 780, 1/2 = 1040, 5/8 = 1300, 3/4 = 1560, 7/8 = 1820

> 1040

> er Signature Code: ... signed.

> Human Resources Personnel

> Terminate Memoranda

> This option allows you to terminate a Memorandum of Service Level Expectations for part-time physicians in cases where the part-time physician is unable to fulfill their obligation or their employment with the VA is terminated.

> Once the employee name is entered, the memorandum is displayed.

> ![](paid-version-4-user-manual/028.png)

Human Resources Personnel

> ![](paid-version-4-user-manual/029.png)![](paid-version-4-user-manual/030.png)You are then asked if you want to terminate this memorandum. If you answer yes, you are prompted for the termination date which must be the last day of a pay period. You can also enter any comments in reference to the termination. An electronic signature code is required to complete the termination.

> Terminate Memoranda YIN: ? YES

> Termination date must be the last day of a pay period. rt Date: OCT 03, 2004 End Date: OCT 01, 2005

> Termination Date: 10/30/04 (OCT 30, 2004)

> Termi nation Comments: NEED NEW HOURS AGREEMENT

> Enter Signature Code: ... signed.

> Human Resources Personnel

> Delete Future Memoranda

> This option allows Human Resources personnel to delete a part-time physician's Memorandum of Service Level Expectations that has yet to begin. This option is used in cases where the part-time physician has decided not to enter into a memorandum with the VA.

> Since memoranda cannot overlap and there is a 6-month limit on entering future memoranda, there should only be one future memorandum at any one time.

> Future memoranda that start in a pay period that has not been opened, can be deleted without any other checks being made.

> If the memorandum being deleted starts in a pay period that has already been opened, the following rules apply.

> • If the payroll has already been processed for the first pay period of the part- time physician’s memorandum, the memorandum will have to be terminated and reconciled.

> • If the timecard has already been transmitted but the cut off window for transmitting timecards is still open, the Payroll Supervisor will have to determine if there is enough time to return the timecard, delete the memorandum, have the timekeeper post all of the tours with the correct time, re-certify the timecard and re-transmit the timecard before the window

> closes. If there is, they can return the timecard and delete the memorandum. If there isn’t enough time, the memorandum will have to be terminated and

> reconciled.

> • For timecards with a status of Payroll, the Payroll Supervisor will have to return it to the Timekeeper before they can delete the memorandum.

Human Resources Personnel

> Once the memorandum is deleted, the software checks each daily ESR. For any daily ESRs with a status of APPROVED, the timecard posting for that day is deleted.

> Once all of the necessary timecards entries have been deleted, the entire ESR

> record for the pay period will be deleted.

> ![](paid-version-4-user-manual/031.png)

> Human Resources Personnel

> Begin Reconciliation Process

> This option allows Human Resources personnel to review a part-time physician's Memorandum of Service Level Expectations and to determine what reconciliation actions will need to occur, based on the final hours worked by the part-time physician.

> After the physician’s name is entered, the summary of their memorandum and hours worked per pay period are displayed.

> One or more of the following reconciliation choices appear for selection.

> 1\. No reconciliation needed

> 2\. Pay VA for negative balance

> 3\. Pay Phy for positive balance

> The next screen allows you to choose whether to print a paper copy of the reconciliation information and deliver it to the part-time physician, or to forward an electronic version of it to the physician.

> A signature code is required to complete the process. The status of the memorandum is then updated from ACTIVE to RECONCILIATION STARTED.

![](paid-version-4-user-manual/032.png)![](paid-version-4-user-manual/033.png)Human Resources Personnel

SYSTEM

> PT Physician Begin Reconciliation Process

> Duty Basis• 2 FLSA• E Normal Hours• 40

> 5/5/05

> XXX-XX-0002

Comp/Flex•

Station• 528

> Memorandum & Leave

> Start Date• APR 18, 2004

> End Date• APR 16, 2005

> 26 of 26 PP 100.00% Hrs Completed = 100.00%

Status thru PP 05-07 Ending

> 1 Agreed Hours• 1040.00 1

> 1 Hours Worked• 1050.00 1

> 1 Carryover Hrs• 0.00 1

> 1 Total Hrs 1050.00 1

> This memorandum has ended

Sat 16-Apr-05

> LWOP Hrs•

> Non Pay Hrs• Off Target Hrs•

> Off Target %

> 0.00

> 0.00

10.00

> 0.96

> L Bal: 24_00 Approved future AL thru Leave Year: o_oo Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 0

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-08:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>04-14:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>04-20:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>04-26:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>05-06:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-09:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-15:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>50.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-10:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-16:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-11:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-17:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-12:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-18:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-24:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-04:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-13:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-19:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ![](paid-version-4-user-manual/034.png)

> ![](paid-version-4-user-manual/035.png)![](paid-version-4-user-manual/036.png)![](paid-version-4-user-manual/037.png)Human Resources Personnel

> Percent Completed: 100

> Off Target Hours: 10

> ff Target Percentage: .96

> Ending Status: Over

> Non Pay Hours: 0

> Without Pay Hours: 0

> Carryover Hours: 0.00

> imated Gross Amount Owed PTP: 498.20

> ss RETURN to continue:

![](paid-version-4-user-manual/038.png)![](paid-version-4-user-manual/039.png)Human Resources Personnel

> onciliation Options:

> Pay PT Phy for positive balance

> er Reconciliation Option:

> onciliation Comments:

> ignature:

Date:

> you 1ike to use a (H)ard copy or (E)1ectronic reconci1iation form: E Signature Code: ... signed.

> orandum Status updated to: RECONCILIATION STARTED

> Human Resources Personnel

> Reconcile Memoranda

> This option allows Human Resources personnel to review a part-time physician's Memorandum of Service Level Expectations and to complete the memorandum reconciliation, once the part-time physician has completed and signed the Begin Reconciliation Process form

> This option allows you to add the part-time physician’s comments if the reconciliation was handled on paper, and to add any additional comments.

> After you electronically sign the reconciliation, it will lock the memorandum so that no further changes can be made.

> ![](paid-version-4-user-manual/040.png)

![](paid-version-4-user-manual/041.png)![](paid-version-4-user-manual/042.png)![](paid-version-4-user-manual/043.png)Human Resources Personnel

> IDPTP,ONE · Memorandum Summary

> Periods have days with incomplete daily ESRs:

> to be completed before the memorandum can be reconciled. Percent Completed: 7.69

> Off Target Hours: ·2.50

> ff Target Percentage: ·12.50

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 31%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Non Pay</p>
</blockquote></th>
<th><blockquote>
<p>Hours:</p>
</blockquote></th>
<th><blockquote>
<p>0.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Without Pay</p>
</blockquote></td>
<td><blockquote>
<p>Hours:</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Carryover</p>
</blockquote></td>
<td><blockquote>
<p>Hours:</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> imated Gross Amount Owed VA: ·124.55

> Ending Status: Under

> ss RETURN to continue:

> ![](paid-version-4-user-manual/044.png)![](paid-version-4-user-manual/045.png)Human Resources Personnel

> onciliation Options:

> Pay VA for negative balance

> Reconciliation Choice: 1 Pay VA for negative balance

> Reconciliation Comments: Please bill me.

> er Reconciliation Option: 1 Pay VA for negative balance

> Final Reconciliation Comments:

> reconciliation for Chief of Staff approval ? YES

> lect Device: HOME// UCX/TELNET Right Margin: 80//

Human Resources Personnel

> Memoranda Report

> This option allows you to review a memorandum for a selected employee and pay period.

> After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

> VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

> Select PAY PERIOD: 04-21

> Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> The software displays all of the information related to the part-time physician's

> Memorandum of Service Level Expectations.

> Human Resources Personnel

> The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

> ![](paid-version-4-user-manual/046.png)![](paid-version-4-user-manual/047.png)!!! <span class="mark">VMS ·KEAI420</span> <span class="mark">f3</span>

> PP:04-21 VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> PAIDPTP,ONE

> 6114/05

XXX-XX-0001

> Pay Plan: L

> ![](paid-version-4-user-manual/048.png)L: 221

Duty Basis: 2

FLSA: E Normal Hours: 40

Comp/Flex: C

Station: 500

> Memorandum & Leave

> Start Date: OCT 03, 2004

> End Date: OCT 01, 2005

> 16 of 26 PP = 61.54% Hrs Completed = 57.68% Agreement will be met by

Status thru PP 05-10 Ending Sat 28-May-05

> I Agreed Hours: 1040.00 I LWOP Hrs: 1.00

> I Hours Worked: 581.75 I Non Pay Hrs: 0.00

> I Carryover Hrs: 0.00 I Off Target Hrs: -39.75

> I Total Hrs: 599.25 I Off Target%: -6.22

averaging 43.98 Hrs/PP during remainder of memo.

> Bal: 200.00 Approved future AL thru Leave Year: 0.00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 24

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-20:</p>
</blockquote></th>
<th><blockquote>
<p>41.50</p>
</blockquote></th>
<th><blockquote>
<p>04-26:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>05-06:</p>
</blockquote></th>
<th><blockquote>
<p>34.50</p>
</blockquote></th>
<th><blockquote>
<p>05-12:</p>
</blockquote></th>
<th><blockquote>
<p>05-18:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>46.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>29.25</p>
</blockquote></td>
<td><blockquote>
<p>05-13:</p>
</blockquote></td>
<td><blockquote>
<p>05-19:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>34.50</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-08:</p>
</blockquote></td>
<td><blockquote>
<p>36.75</p>
</blockquote></td>
<td><blockquote>
<p>05-14:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>20.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>39.50</p>
</blockquote></td>
<td><blockquote>
<p>05-09:</p>
</blockquote></td>
<td><blockquote>
<p>45.25</p>
</blockquote></td>
<td><blockquote>
<p>05-15:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-24:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-04:</p>
</blockquote></td>
<td><blockquote>
<p>42.00</p>
</blockquote></td>
<td><blockquote>
<p>05-10:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-16:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>46.50</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>26.00</p>
</blockquote></td>
<td><blockquote>
<p>05-11:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-17:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue:

Human Resources Personnel

> Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination,

> etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time as entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

> WARNING! If there are incomplete ESRs, DO NOT proceed with the reconciliation.

> ![](paid-version-4-user-manual/049.png)

> Human Resources Personnel

> Memoranda Expiring Within Date Range

> This option allows Human Resources personnel to identify a part-time physician’s Memorandum of Service Level Expectations that will expire within the specified date range, so that the appropriate paperwork to begin the memorandum renewal can be initiated.

> You have the option of entering an “Off By” percentage between 1 and 100. When entered, only memorandums that are off by more than the percentage you specify will be included. For example, if you enter 5, only memorandums within the date range you’ve selected and that are off by more than 5% will be included.

> ![](paid-version-4-user-manual/050.png)

![](paid-version-4-user-manual/051.png)![](paid-version-4-user-manual/052.png)Human Resources Personnel

> !!! <span class="mark">VMS - KEAI420</span> EJ

> AIDPTP,ONE

VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> 6/14/05

XXX-XX-0001

> ay Plan: 1

> L: 221

Duty Basis:

FLSA: N Normal Hours: 40

Comp/Flex: F

Station: 528

> Memorandum & Leave

> Start Date: SEP 05, 2004

> End Date: SEP 03, 2005

> 20 of 26 PP = 76.92% Hrs Completed = 80.65%

Status thru PP 05-10 Ending Sat 28-May-05

> I Agreed Hours: 1040.00 I LWOP Hrs:

> I Hours Worked: 833.50 I Non Pay Hrs:

> I Carryover Hrs: 0.00 I Off Target Hrs:

> I Total Hrs: 833.50 I Off Target%:

> 6.50

> 0.00

40.00

> 5.04

> Agreement will be met by

averaging 33.33 Hrs/PP during remainder of memo.

> Bal: 260.00 Approved future AL thru Leave Year: 88.00 Max carryover: 240 otential AL hours to be 1ost by JAN 07, 2006 excluding Approved AL: 60

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-18:</p>
</blockquote></th>
<th><blockquote>
<p>89.00</p>
</blockquote></th>
<th><blockquote>
<p>04-24:</p>
</blockquote></th>
<th><blockquote>
<p>48.00</p>
</blockquote></th>
<th><blockquote>
<p>05-04:</p>
</blockquote></th>
<th><blockquote>
<p>36.00</p>
</blockquote></th>
<th><blockquote>
<p>05-10:</p>
</blockquote></th>
<th><blockquote>
<p>0.00</p>
</blockquote></th>
<th><blockquote>
<p>05-16:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-19:</p>
</blockquote></td>
<td><blockquote>
<p>31.00</p>
</blockquote></td>
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>36.00</p>
</blockquote></td>
<td><blockquote>
<p>05-11:</p>
</blockquote></td>
<td><blockquote>
<p>35.50</p>
</blockquote></td>
<td><blockquote>
<p>05-17:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-20:</p>
</blockquote></td>
<td><blockquote>
<p>42.00</p>
</blockquote></td>
<td><blockquote>
<p>04-26:</p>
</blockquote></td>
<td><blockquote>
<p>48.00</p>
</blockquote></td>
<td><blockquote>
<p>05-06:</p>
</blockquote></td>
<td><blockquote>
<p>37.00</p>
</blockquote></td>
<td><blockquote>
<p>05-12:</p>
</blockquote></td>
<td><blockquote>
<p>4.00</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>38.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>36.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>36.00</p>
</blockquote></td>
<td><blockquote>
<p>05-13:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>43.00</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>44.00</p>
</blockquote></td>
<td><blockquote>
<p>05-08:</p>
</blockquote></td>
<td><blockquote>
<p>45.00</p>
</blockquote></td>
<td><blockquote>
<p>05-14:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>48.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>36.00</p>
</blockquote></td>
<td><blockquote>
<p>05-09:</p>
</blockquote></td>
<td><blockquote>
<p>65.00</p>
</blockquote></td>
<td><blockquote>
<p>05-15:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ![](paid-version-4-user-manual/053.png)ress RETURN to continue:

> ![](paid-version-4-user-manual/054.png)![](paid-version-4-user-manual/055.png)Human Resources Personnel

> !!! <span class="mark">VMS - KEAI420</span> EJ

> e following Pay Periods have days with incomplete daily ESRs:

> -08, 05-10, 05-12, 05-13

> Initial Comments: work on 10 hr day a week in the clinic ress RETURN to continue:

> ere were 1 PT Physician Memorandums expiring in the date range specified o were more than 5% off target.

> ![](paid-version-4-user-manual/056.png)

Human Resources Personnel

> Display Pay Period ESR

> ![](paid-version-4-user-manual/057.png)![](paid-version-4-user-manual/058.png)This option allows Human Resources personnel to review a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05·09

XXX-XX-0001

> Duty Basis: 2 FLSA: E Normal Hours: 40 Comp/Flex: C Station: 500 ,

> Incomplete Days: 6

> Tour Description Status

> Postings Time Code Meal Hours

> Remarks Code

> 1-May-05 DAY OFF PENDING

PENDING

PENDING

> ![](paid-version-4-user-manual/059.png)![](paid-version-4-user-manual/060.png)Human Resources Personnel

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 40

Incomplete Days: 6

Comp/Flex: C Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 09:30P-10:00P RG REG TIME 00:30

> 10: OOP-01: OOA RG REG TIME 03:00

> 4-May-05 10 07:00A-03:30P APPROVED

> 07:00A-NOON RG REG TIME 05:00

> NOON-01:00P AA AUTH ABS 30 00:30

> AA GRANTED BY SUPR.

> 01:00P-04:00P RG REG TIME 03:00

> PTP Remarks: TEST

PENDING APPROVED

![](paid-version-4-user-manual/061.png)Human Resources Personnel

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

> Duty Basis: 2 FLSA: E Normal Hours: 40

> Incomplete Days: 6

> Tour Description

XXX·XX-0001

> Comp/Flex: C

> Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 7-May-05 DAY OFF PENDING

> 07:00A-08:00A RG REG TIME 0 01:00

> 8-May-05 1 DAY OFF DAY OFF

> 9-May-05 10 07:00A-03:30P APPROVED

> 07:00A-03:30P AL ANNUAL LV 60 07:30

> SF71 ON FILE

> 10-May-05 1 DAY OFF DAY OFF

RTED

> Employee Menu

> Employee Menu

> Prior to this patch, all part-time physicians tracked their time and attendance on paper form VA Form 4-5631a, known as a Subsidiary Record. After this patch, the part-time physicians who elect to enter into a Memorandum of Service Level Expectations with the VA will track their time and attendance via an automated Electronic Subsidiary Record which will be stored within the VistA PAID/ETA software files.

> Changed Options

> Cancel Leave Request

> Approved leave is automatically posted to the ESR. This option was modified to remove such leave from the ESR when the employee cancels it.

> Edit Leave Request

> Approved leave is automatically posted to the ESR. This option was modified to remove such leave from the ESR when the leave is edited since editing revokes the supervisor’s approval of the leave.

> New Options

> PT Physician with Memorandum Menu

> The PT Physician With Memorandum Menu has been added to the existing Employee Menu, and contains the options used by part-time physicians with a Memorandum of Service Level Expectations to perform the necessary actions related to tracking of their Time and Attendance.

> This menu is only accessible to employees that hold the PRSP EMP key. This key is automatically assigned when Human Resources enters a memorandum for the employee.

> Electronic Subsidiary Record-Daily Enter/Edit

> This option displays the action pick list and two new screens that will allow the part-time physician to monitor the status of their Electronic Subsidiary Record (ESR) for a selected pay period, and to enter their time and attendance. The first screen is called the Work Summary Screen (WSS) and the second is called the ESR Data Entry Screen.

Employee Menu

> *Action Pick List*

> When the Electronic Subsidiary Record-Daily Enter/Edit option is first invoked, the software reviews the part-time physician’s memorandum and generates a pick list

> of items requiring their attention. The pick list contains the following types of actions in this order:

> 1\. Any prior memoranda that need to be reconciled.

> 2\. Any prior pay periods that have incomplete daily ESRs.

> 3\. The current pay period.

> 4\. The next pay period if it has been opened and if the part-time physician has an active memorandum covering this pay period.

> The following is an example of the action pick list that you might see upon entering this option.

> Select PT Physician With Memorandum Menu Option: 1 Electronic Subsidiary

> Record-Daily Enter/Edit

> 1\. Reconcile Prior Memorandum from OCT 05, 2003 TO OCT 02, 2004

> 2\. Edit ESR for prior pay period 04-18 \[Sun 5-Sep-04 - Sat 18-Sep-04\]

> 3\. Edit ESR for prior pay period 04-20 \[Sun 3-Oct-04 - Sat 16-Oct-04\]

> 4\. Edit ESR for prior pay period 04-21 \[Sun 17-Oct-04 - Sat 30-Oct-04\] Select an Item : (1-4): 1//

> Items selected from group 1 are covered later in this document.

> If the part-time physician selects any item from group 2, 3 or 4, the Work Summary

> Screen (WSS) screen is displayed.

> *The Work Summary Screen*

> Once an item is selected from group 2, 3, or 4, the Work Summary Screen for that item is displayed. Information such as the employee name, SSN, Station Number, Normal Hours, Duty Base, T&L, Pay Plan, and the last Pay Period processed are displayed, as well as memorandum and annual leave information, as of that pay period. (Please see the supplement at the end of this document for a description of all pertinent fields.)

> The days of the pay period are grouped by week, and are listed in order of the day number (not the date) for selection. Each day shows the ESR Daily Status and a listing of the various types of time recorded for this day, if any.

> When the pay period is opened, the system initially populates each ESR day with a status of either DAY OFF (if the employee does not have a scheduled tour for that day) or NOT STARTED (if the employee does have a scheduled tour for that day).

> March 2018 Appendix A - Supplemental Information for A-25

> Employee Menu

> Once you complete and sign the ESR for a particular day, the status is updated to one of the following.

> *PENDING* - the ESR day was modified and saved, but not signed.

> *SIGNED* - the ESR day was completed and signed.

> All days on the ESR with a scheduled tour, must be electronically signed by the physician. There may be circumstances when no work is performed and no leave is taken on a scheduled day. In this case, the physician electronically signs the day by selecting the day, and without entering any time on the ESR, saves the ESR day. When an ESR day is saved with no work or leave entered, you are prompted to sign the day.

> NOTE: The supervisor reviews ESR days that have been signed by a part-time physician. The supervisor can change the status of the day to either APPROVED or RESUBMIT. The APPROVED status indicates that no further action needs to be taken by the part-time physician. The RESUBMIT status indicates that the part- time physician should modify the data on the ESR and then re-sign it.

Employee Menu

> ![](paid-version-4-user-manual/062.png)![](paid-version-4-user-manual/063.png)![](paid-version-4-user-manual/064.png)Sample Work Summary Screen

> IDPTP,ONE

> P 1an: L

> &L: 028

Work Summary Screen for Part Time VA Physician

> Duty Basis: 2 FLSA: E Normal Hours: 10

> XXX-XX-0001

Comp/Flex:

Station: 528

> Memorandum & Leave Status thru PP 04-23 Ending

> Start Date: OCT 03, 2004 1 Agreed Hours: 260.00 1

> TERMINATED: OCT 30, 2004 I Hours Worked: 17.50 I

> 2 of 26 PP = 7.69% 1 Carryover Hrs: 0.00 1

> Hrs Completed= 6.73% 1 Total Hrs: 17.50 1

> This memorandum has ended

Sat 27-Nov-04

> LWOP Hrs: Non Pay Hrs:

> Off Target Hrs: Off Target %:

> 0.00

> 0.00

> -2.50

-12.50

> L Bal: 67.00 Approved future AL thru Leave Year: 0.00 Max carryover: 240

> Potential AL hours to be lost by Jan 07, 2006 excluding Approved AL: 0

> ESR Hours Week 1: 9.00 Week 2: 0.00 Total: 9.00

> Week 1 · Sun 3-0ct-04 Day Week 2 · Sun 10-0ct-04

> 1 Sun PENDING · RG 8 Sun DAY OFF

> 2 Mon DAY OFF 9 Mon DAY OFF

> 3 Tue DAY OFF 10 Tue DAY OFF

> 4 Wed DAY OFF 11 Wed DAY OFF

> 5 Thu RESUBMIT 000-666-0000 12 Thu RESUBMIT

> 6 DAY OFF 13 Fri RESUBMIT

> 7 DAY OFF 14 Sat NOT STARTED

> 1.14

> Employee Menu

> *The Daily Electronic Subsidiary Record (ESR)*

> Once you select a day, the Electronic Subsidiary Record (ESR) for that day is displayed. Up to seven separate entries may be made for each day. The part-time physician should enter the appropriate number of entries to accurately reflect the actual work performed during the course of the day.

> The time segments should be posted in chronological order whenever possible but the software will accept the postings in any order. For example, if and additional time segment needs to be added at a later date, it can be added to the end of the existing list of postings.

> The ESR Data Entry Screen includes employee information such as name, SSN, Station Number, Time and Leave Unit, the Tour Beginning Date, and if a tour has been assigned to the day, a summary of the tour’s start/stop times and meal time, if any. (Please see the supplement at the end of this document for a complete list of pertinent field descriptions.)

Employee Menu

> Following is a list of the data entry fields with a brief description

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>START</p>
</blockquote></th>
<th><blockquote>
<p>The time that an individual work or leave segment began.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>STOP</p>
</blockquote></td>
<td><blockquote>
<p>The time than an individual work or leave segment ended.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TYPE OF TIME</p>
</blockquote></td>
<td><blockquote>
<p>The type of time worked or leave taken. AA Authorized Absence</p>
<p>AD Adopt</p>
<p>AL Annual Leave</p>
<p>CB Family Care</p>
<p>CP Continuation of Pay (COP) DL Donor Leave</p>
<p>HX Holiday Excused</p>
<p>ML Military Leave</p>
<p>NL Non-pay Annual Leave</p>
<p>RG Regular Time</p>
<p>RL Restored Annual Leave</p>
<p>SL Sick Leave TR Training TV Travel</p>
<p>WP Leave Without Pay</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REMARKS CODE</p>
</blockquote></td>
<td><blockquote>
<p>A code which further describes the TYPE OF TIME entered. Only the appropriate REMARKS CODES that correspond to the TYPE OF TIME entered will be allowed. Enter a ? for a</p>
<p>list of the appropriate choices. (This field is optional.)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MEAL</p>
</blockquote></td>
<td><blockquote>
<p>Enter the best approximation of time for the meal during this work segment, in increments of 15 minutes. Meals may not be</p>
<p>longer than 60 minutes, so appropriate meal times are 15, 30,</p>
<p>45, and 60. Enter a 0 or leave the field blank to indicate that no meal was taken. When meals are taken, they must be</p>
<p>entered, even when they are not scheduled for that tour. Meals may be entered for periods of both regular hours and</p>
<p>leave. Entering the meal time will automatically deduct the meal from the total creditable hours in the work segment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HRS</p>
</blockquote></td>
<td><blockquote>
<p>This is a calculated field. The system will automatically enter the number of hours entered for each segment based on the</p>
<p>START, STOP, and MEAL times.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REMARKS</p>
</blockquote></td>
<td><blockquote>
<p>Any further comments you would like to enter. Any remarks entered here are seen by the supervisor when they review the</p>
<p>daily ESR. (This field is optional unless Authorized Absence is</p>
<p>entered.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Employee Menu

> As you make each entry, you can move to the next field on the form by entering a Tab or by pressing the Enter key. A question mark (?) may be entered at most fields for a list of possible entries and/or formats. For further information on using this type of edit screen, please refer to Chapter 1 of the [Personnel and Accounting Integrated Data (PAID)](http://www.va.gov/vdl/Financial_Admin.asp?appID=51) User Manual, which can be accessed from the VistA Documentation Library (VDL) web page at [www.va.gov/vdl/.](http://www.va.gov/vdl/)

> Up-arrow REMARKS (^REMARKS) allows you to jump to the REMARKS field. This field is free text and will allow up to 70 characters. These remarks are optional, but they may be helpful to the Supervisor as they review your daily ESRs. It is recommended that REMARKS be entered when the part-time physician deviates from their normally scheduled tour of duty of if they work on a day where they were not scheduled to work.

> The software allows you to skip to the COMMAND prompt by entering an up-arrow (^) in any field. You can automatically save the changes and skip directly to the electronic signature prompt by entering Num Lock and then E in any field.

> Once you have completed your daily ESR entries and navigated to the COMMAND prompt, enter SAVE or EXIT. If you enter EXIT without saving first, you will be asked if you wish to save your entries. Once you enter SAVE, you will be asked for an Electronic Signature. If you do not enter a signature, the ESR is given a status of PENDING, and you will see the following message:

> PENDING: changes were saved without signature.

Employee Menu

> Sample ESR

> Some of the fields will allow abbreviated entries. For example, you may enter 7A or

> ![](paid-version-4-user-manual/065.png)![](paid-version-4-user-manual/066.png)3P for a time. You may enter a question mark (?) at most fields for a description of acceptable formats and/or entries.

> our: 07:00A-06:00P Meal: 60

Tour Beginning

> Sat 16-0ct-04

XXX-XX-0001 I T&L: 028

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>START</p>
<p>07:00A</p>
</blockquote></th>
<th><blockquote>
<p>STOP</p>
<p>03:30P</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
<p>RG</p>
</blockquote></th>
<th><blockquote>
<p>OF</p>
</blockquote></th>
<th><blockquote>
<p>TIME</p>
</blockquote></th>
<th><blockquote>
<p>REMARKS</p>
</blockquote></th>
<th><blockquote>
<p>CODE</p>
</blockquote></th>
<th><blockquote>
<p>MEAL</p>
<p>30</p>
</blockquote></th>
<th><blockquote>
<p>HRS</p>
<p>08:00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
</tr>
</tbody>
</table>

> Called in to cover. Save Refresh

> command or 1 A 1 followed by a caption to jump to a specific field.

> ![](paid-version-4-user-manual/067.png)![](paid-version-4-user-manual/068.png)![](paid-version-4-user-manual/069.png)Employee Menu

> !!! VMS- KEA! 420 GJ(QJ(g)

> Ejle dit iew Iools Qptions t!elp

> Save Refresh

> era command or 1 " 1 followed by a caption to jump to a specific field.

> er your Current Signature Code: SIGNATURE VERIFIED ESR data saved with signature.

Employee Menu

> Extended Absence

> This menu contains options used to enter or maintain extended absence records. An extended absence is a future period of time when the part-time physician will not be performing work for the VA during a normally scheduled tour of duty and they are not planning on using an approved type of leave to cover their absence.

> An electronic signature code is required to use these options. An electronic signature code can be entered/edited through the Electronic Signature Code Edit option.

> *Enter Extended Absence*

> This option allows a part-time physician to specify a future period of time when they will not be performing work for the VA (extended absence). The software automatically changes the status to “Signed” for ESR days with a scheduled tour of duty, if those days are covered by the period of extended absence. Therefore, the physician does not need to manually update their ESR during their absence.

> You are prompted to enter a beginning and ending date for a new period of extended absence, as well as any remarks. An electronic signature code is required to complete the entry.

> Please see the sample screen provided under Edit Extended Absence.

> *Edit Extended Absence*

> This option allows the part-time physician to edit a previously entered extended absence. The software will automatically update the current and future days on the ESR as necessary. However, any ESR days that are prior to the current day will

> not be automatically modified when an extended absence is edited. An extended absence cannot be edited if its “To Date” is prior to the current day. A signature code is required to complete the edit.

> ![](paid-version-4-user-manual/070.png)![](paid-version-4-user-manual/071.png)![](paid-version-4-user-manual/072.png)![](paid-version-4-user-manual/073.png)Employee Menu

> file l;;dit iew !ools Qptions !::!elp

> VA TIME & ATTENDANCE SYSTEM EDIT EXTENDED ABSENCE

> 1\) MAR 14, 2005 to MAR 14, 2005 Status: ACTIVE

> working at Albany Med.

> Entered: MAR 14, 2005@14:12:16

> dit which extended absence \#?: (1-1): 1

> VA TIME & ATTENDANCE SYSTEM EDIT EXTENDED ABSENCE

> AIDPTP,ONE

> ROM DATE: ilrtf41Mm@

> 0 DATE: MAR 14,2005

> EMARKS: working at Albany Med.

Employee Menu

> ![](paid-version-4-user-manual/074.png)![](paid-version-4-user-manual/075.png)![](paid-version-4-user-manual/076.png)![](paid-version-4-user-manual/077.png)*Edited Screen*

> file l;;dit iew !ools Qptions !::!elp

> AIDPTP,ONE

> ROM DATE: MAR 14,2005

> 0 DATE: MAR 14,2005

VA TIME & ATTENDANCE SYSTEM EDIT EXTENDED ABSENCE

> REMARKS: Working at St. Peter's for the day.

> Save Refresh

> nter a command or '"' followed by a caption to jump to a specific field.

> Current Signature Code:

> Employee Menu

> *Cancel Extended Absence*

> This option allows the part-time physician to cancel a previously entered extended absence. The software will automatically update the current and future days on the ESR, as necessary. However, any ESR days that are prior to the current day will

> not be automatically modified when an extended absence is cancelled. An extended absence cannot be cancelled if its “To Date” is prior to the current day.

> ![](paid-version-4-user-manual/078.png)

Employee Menu

> *Display Extended Absence*

> This option allows you to display a list of extended absence records that end on or after a specified date. The timeframe of the absence, as well as any remarks, the status, and the dates entered and/or updated are displayed.

> ![](paid-version-4-user-manual/079.png)![](paid-version-4-user-manual/080.png)-----------------------------------------------------------------

> ![](paid-version-4-user-manual/081.png)<span class="mark">!!!</span> VMS · KEA! 420 \[Q)

> VA TIME & ATTENDANCE SYSTEM DISPLAY EXTENDED ABSENCE

> n with Date *Til* 1/1/05 (JAN 01. 2005)

> 31\. 2005 to JAN 31. 2005 Status• ACTIVE SICK - WILL MAKE UP ON 2/1

> Entered• JAN 31. 2005@07 01•30

> 14\. 2005 to MAR 16. 2005 Status ACTIVE

> ATTENDING SEMINAR AT LOCAL HOSPITAL

> Entered• MAR 14. 2005@09•17 49

> 21\. 2005 to MAR 25. 2005 Status• ACTIVE OFF WEEK - AT LOCAL HOSPITAL

> Entered• MAR 14. 2005@09•19•19 nter RETURN to continue or 'A' to exit•

> Employee Menu

> Display Pay Period ESR

> ![](paid-version-4-user-manual/082.png)![](paid-version-4-user-manual/083.png)This option displays a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05·09

XXX-XX-0001

> Duty Basis: 2 FLSA: E Normal Hours: 40 Comp/Flex: C Station: 500

> Incomplete Days: 6

> Tour Description Status

> Postings Time Code Meal Hours

> Remarks Code

> 1·May.05 DAY OFF PENDING

PENDING

PENDING

![](paid-version-4-user-manual/084.png)![](paid-version-4-user-manual/085.png)Employee Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 40

Incomplete Days: 6

Comp/Flex: C Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 09:30P-10:00P RG REG TIME 00:30

> 10: OOP-01: OOA RG REG TIME 03:00

> 4-May-05 10 07:00A-03:30P APPROVED

> 07:00A-NOON RG REG TIME 05:00

> NOON-01:00P AA AUTH ABS 30 00:30

> AA GRANTED BY SUPR.

> 01:00P-04:00P RG REG TIME 03:00

> PTP Remarks: TEST

PENDING APPROVED

> ![](paid-version-4-user-manual/086.png)Employee Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

> Duty Basis: 2 FLSA: E Normal Hours: 40

> Incomplete Days: 6

> Tour Description

XXX·XX-0001

> Comp/Flex: C

> Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 7-May-05 DAY OFF PENDING

> 07:00A-08:00A RG REG TIME 0 01:00

> 8-May-05 1 DAY OFF DAY OFF

> 9-May-05 10 07:00A-03:30P APPROVED

> 07:00A-03:30P AL ANNUAL LV 60 07:30

> SF71 ON FILE

> 10-May-05 1 DAY OFF DAY OFF

RTED

Employee Menu

> Display Memoranda

> This option displays information related to the part-time physician's Memorandum of Service Level Expectations. It includes fields that help to identify the part-time physician (name, SSN, T&L etc.) and a memorandum summary (Start/End dates, Agreed Hours, completion percentages etc.). This will be followed by a list of pay periods covered by the memorandum and the hours credited during each of these pay periods. If any Non-Pay or Leave Without Pay occurred during the memorandum, a list of the hours and the pay period in which they occurred will be displayed.

> If the memorandum has ended and the part-time physician has selected their reconciliation choice via the electronic form, their reconciliation choice and any reconciliation comments will be displayed.

> ![](paid-version-4-user-manual/087.png)

> Employee Menu

> Select Reconciliation Choice

> This option allows you to review a recently ended memorandum, and to select a reconciliation option. One or more of the following reconciliation choices might appear for selection.

> 1\. No reconciliation needed

> 2\. Pay VA for negative balance

> 3\. Pay Phy for positive balance

> The review screen is shown here. The next screen shows more information related to the memorandum and the reconciliation options.

> ![](paid-version-4-user-manual/088.png)

![](paid-version-4-user-manual/089.png)![](paid-version-4-user-manual/090.png)![](paid-version-4-user-manual/091.png)Employee Menu

> IDPTP,ONE · Memorandum Summary

> Periods have days with incomplete daily ESRs:

> to be completed before the memorandum can be reconciled. Percent Completed: 7.69

> Off Target Hours: ·2.5

> ff Target Percentage: -12.5

> Ending Status: Under

> Non Pay Hours: 0

> Without Pay Hours: 0

> Carryover Hours: 0.00

> imated Gross Amount Owed VA: -124.55

> ss RETURN to continue: I

> ![](paid-version-4-user-manual/092.png)![](paid-version-4-user-manual/093.png)Employee Menu

> onciliation Options:

> Pay VA for negative balance

> er Reconciliation Choice: 1 Pay VA for negative balance

> 's Reconciliation Comments: Please bill me.

> er Signature Code: ... signed.

> 1 Electronic Subsidiary Record·Daily Enter/Edit

> 2 Extended Absence ...

> 3 Display Pay Period ESR

> 4 Display Memoranda

> 5 Select Reconciliation Choice

> lect PT Physician With Memorandum Menu Option:

Employee Menu

> Timekeepers Main Menu

> Timekeepers Main Menu

> Changed Options

> Post Employee Time

> This option has been modified to prevent selection of a part-time physician with an active memorandum. The new option, Post PT Physician Time, must be used to post time for such employees.

> Enter/Edit Employee Tour of Duty

> This option has been modified to perform additional steps when a tour is changed for a part-time physician with an active memorandum. In addition to the normal step of removing any timecard postings on the changed day, the software will also reset the status of any daily ESR the part-time physician has already posted to RESUBMIT, so they will have to review and repost the information if necessary.

> New Options

> PT Physician Menu

> This menu contains all of the options that Timekeepers will need to monitor and post timecards for part-time physicians with a Memorandum of Service Level Expectations.

> Post PT Physician Time

> This option allows the timekeeper to post time card data for part-time physicians with a Memorandum of Service Level Expectations. Regular employee’s timecards cannot be selected using this option. This action should only be done at the direction of the T&L supervisor when the physician's Electronic Subsidiary Record (ESR) cannot be completed before time card certification for the pay period. Unscheduled regular time (RG) will only be tracked via the ESR and cannot be posted to the time card.

> Non Pay, AWOL, and On Suspension cannot be posted on the ESR. When appropriate, these must be posted directly on the timecard by the timekeeper. Furthermore, for a current pay period, the timekeeper will have to post these to the timecard after the ESR day has been approved. This is because approval of an ESR day for a timecard with timekeeper status (i.e., not yet certified) will repost the timecard and overwrite any previous postings for that day.

Timekeepers Main Menu

> If you are responsible for more than one T&L Unit, you are first prompted to select a T&L Unit. You are then prompted for a date, and whether or not to post the employees time cards in alphabetical order.

> REDACTED

> !'. <span class="mark">VMS·KEA! 420</span> flfl3

> Menu Option: 1 Post PT Physician Time

> 221

> osting Date: T-1//JUN 7 (JUN 07, 2005)

> edit the T & A RECORDs in alphabetical order? Yes// N (No) PAIDPTP,ONE 000-28-0001

> REDACTED

> Timekeepers Main Menu

REDACTED

> <span class="mark">MS- KEA• 420</span> I!IEJ

> VA TIME & ATTENDANCE SYSTEM EMPLOYEE TIME AND ATTENDANCE DATA

> PAIDPTP,ONE 000-28-0001

> Station: 528

> &L: 221

> Pay Per: 05-11

Normal Hours: 40

Pay Plan: 1

> Duty Basis: 1

Comp/Fl ex: 0

> FLSA: N

> Date Scheduled Tour Tour Exceptions

> Tue 7-Jun-05 08:00A-NOON Unposted

> Enter •A• to bypass this employee.

> Did Employee Only Work Scheduled Tour? N

> as Employee Absent the Entire Tour? Y

> Select TYPE OF TIME CODE: SL TIME REMARKS CODE:

SICK LV

> Remarks: Called in sick at end of pay period

> Select EMPLOYEE:

> REDACTED

> Display Pay Period ESR

> ![](paid-version-4-user-manual/094.png)![](paid-version-4-user-manual/095.png)This option displays a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05·09

XXX-XX-0001

> Duty Basis: 2 FLSA: E Normal Hours: 40 Comp/Flex: C Station: 500

> Incomplete Days: 6

> Tour Description Status

> Postings Time Code Meal Hours

> Remarks Code

> 1·May.05 DAY OFF PENDING

PENDING

PENDING

> ![](paid-version-4-user-manual/096.png)![](paid-version-4-user-manual/097.png)Timekeepers Main Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 40

Incomplete Days: 6

Comp/Flex: C Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 09:30P-10:00P RG REG TIME 00:30

> 10: OOP-01: OOA RG REG TIME 03:00

> 4-May-05 10 07:00A-03:30P APPROVED

> 07:00A-NOON RG REG TIME 05:00

> NOON-01:00P AA AUTH ABS 30 00:30

> AA GRANTED BY SUPR.

> 01:00P-04:00P RG REG TIME 03:00

> PTP Remarks: TEST

PENDING APPROVED

![](paid-version-4-user-manual/098.png)Timekeepers Main Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

> Duty Basis: 2 FLSA: E Normal Hours: 40

> Incomplete Days: 6

> Tour Description

XXX·XX-0001

> Comp/Flex: C

> Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 7-May-05 DAY OFF PENDING

> 07:00A-08:00A RG REG TIME 0 01:00

> 8-May-05 1 DAY OFF DAY OFF

> 9-May-05 10 07:00A-03:30P APPROVED

> 07:00A-03:30P AL ANNUAL LV 60 07:30

> SF71 ON FILE

> 10-May-05 1 DAY OFF DAY OFF

RTED

> Timekeepers Main Menu

> Display PP ESR Exceptions

> This option allows Supervisors to review daily ESR exceptions for part-time physicians with a Memorandum of Service Level Expectations. It can be used to verify that part-time physicians have completed each day within the pay period with a scheduled Tour of Duty and to monitor other work performed on scheduled days off.

> ![](paid-version-4-user-manual/099.png)

Timekeepers Main Menu

> Memoranda Report

> This option allows you to review a memorandum for a selected employee and pay period.

> After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

> VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

> Select PAY PERIOD: 04-21

> Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> The software displays all of the information related to the part-time physician's

> Memorandum of Service Level Expectations.

> Timekeepers Main Menu

> The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

> ![](paid-version-4-user-manual/100.png)![](paid-version-4-user-manual/101.png)!!! <span class="mark">VMS ·KEAI420</span> <span class="mark">f3</span>

> PP:04-21 VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> PAIDPTP,ONE

> 6114/05

XXX-XX-0001

> Pay Plan: L

> ![](paid-version-4-user-manual/102.png)L: 221

Duty Basis: 2

FLSA: E Normal Hours: 40

Comp/Flex: C

Station: 500

> Memorandum & Leave

> Start Date: OCT 03, 2004

> End Date: OCT 01, 2005

> 16 of 26 PP = 61.54% Hrs Completed = 57.68% Agreement will be met by

Status thru PP 05-10 Ending Sat 28-May-05

> I Agreed Hours: 1040.00 I LWOP Hrs: 1.00

> I Hours Worked: 581.75 I Non Pay Hrs: 0.00

> I Carryover Hrs: 0.00 I Off Target Hrs: -39.75

> I Total Hrs: 599.25 I Off Target%: -6.22

averaging 43.98 Hrs/PP during remainder of memo.

> Bal: 200.00 Approved future AL thru Leave Year: 0.00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 24

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-20:</p>
</blockquote></th>
<th><blockquote>
<p>41.50</p>
</blockquote></th>
<th><blockquote>
<p>04-26:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>05-06:</p>
</blockquote></th>
<th><blockquote>
<p>34.50</p>
</blockquote></th>
<th><blockquote>
<p>05-12:</p>
</blockquote></th>
<th><blockquote>
<p>05-18:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>46.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>29.25</p>
</blockquote></td>
<td><blockquote>
<p>05-13:</p>
</blockquote></td>
<td><blockquote>
<p>05-19:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>34.50</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-08:</p>
</blockquote></td>
<td><blockquote>
<p>36.75</p>
</blockquote></td>
<td><blockquote>
<p>05-14:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>20.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>39.50</p>
</blockquote></td>
<td><blockquote>
<p>05-09:</p>
</blockquote></td>
<td><blockquote>
<p>45.25</p>
</blockquote></td>
<td><blockquote>
<p>05-15:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-24:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-04:</p>
</blockquote></td>
<td><blockquote>
<p>42.00</p>
</blockquote></td>
<td><blockquote>
<p>05-10:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-16:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>46.50</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>26.00</p>
</blockquote></td>
<td><blockquote>
<p>05-11:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-17:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue:

Timekeepers Main Menu

> Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination,

> etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

> ![](paid-version-4-user-manual/103.png)

> Payroll Main Menu

> Payroll Main Menu

> New Options

> PT Physician Menu

> This new menu has been added to the existing Payroll Supervisor Menu. The PT Physician Menu contains all of the necessary options to allow the Payroll Supervisor to monitor the status of a part-time physician’s Memorandum of Service Level Expectations.

> Memoranda Report

> This option allows you to review a memorandum for a selected employee and pay period.

> After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

> VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

> Select PAY PERIOD: 04-21

> Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> The software displays all of the information related to the part-time physician's

> Memorandum of Service Level Expectations.

Payroll Main Menu

> The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

> ![](paid-version-4-user-manual/104.png)![](paid-version-4-user-manual/105.png)![](paid-version-4-user-manual/106.png)!!! <span class="mark">VMS ·KEAI420</span> <span class="mark">f3</span>

> PP:04-21 VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> PAIDPTP,ONE

> 6/14/05

XXX-XX-0001

> Pay Plan: L

> ![](paid-version-4-user-manual/107.png)L: 221

Duty Basis: 2

FLSA: E Normal Hours: 40

Comp/Flex: C

Station: 500

> Memorandum & Leave

> Start Date: OCT 03, 2004

> End Date: OCT 01, 2005

> 16 of 26 PP = 61.54% Hrs Completed = 57.68% Agreement will be met by

Status thru PP 05-10 Ending Sat 28-May-05

> I Agreed Hours: 1040.00 I LWOP Hrs: 1.00

> I Hours Worked: 581.75 I Non Pay Hrs: 0.00

> I Carryover Hrs: 0.00 I Off Target Hrs: -39.75

> I Total Hrs: 599.25 I Off Target%: -6.22

averaging 43.98 Hrs/PP during remainder of memo.

> Bal: 200.00 Approved future AL thru Leave Year: 0.00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 24

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-20:</p>
</blockquote></th>
<th><blockquote>
<p>41.50</p>
</blockquote></th>
<th><blockquote>
<p>04-26:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>05-06:</p>
</blockquote></th>
<th><blockquote>
<p>34.50</p>
</blockquote></th>
<th><blockquote>
<p>05-12:</p>
</blockquote></th>
<th><blockquote>
<p>05-18:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>46.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>29.25</p>
</blockquote></td>
<td><blockquote>
<p>05-13:</p>
</blockquote></td>
<td><blockquote>
<p>05-19:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>34.50</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-08:</p>
</blockquote></td>
<td><blockquote>
<p>36.75</p>
</blockquote></td>
<td><blockquote>
<p>05-14:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>20.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>39.50</p>
</blockquote></td>
<td><blockquote>
<p>05-09:</p>
</blockquote></td>
<td><blockquote>
<p>45.25</p>
</blockquote></td>
<td><blockquote>
<p>05-15:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-24:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-04:</p>
</blockquote></td>
<td><blockquote>
<p>42.00</p>
</blockquote></td>
<td><blockquote>
<p>05-10:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-16:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>46.50</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>26.00</p>
</blockquote></td>
<td><blockquote>
<p>05-11:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-17:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue:

> Payroll Main Menu

> Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination,

> etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

> ![](paid-version-4-user-manual/108.png)

Payroll Main Menu

> Display Pay Period ESR

> ![](paid-version-4-user-manual/109.png)![](paid-version-4-user-manual/110.png)This option allows you to review a part-time physician's ESR record for a selected pay period. Any pay period from a current or past memorandum may be selected.

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05·09

XXX-XX-0001

> Duty Basis: 2 FLSA: E Normal Hours: 40 Comp/Flex: C Station: 500

> Incomplete Days: 6

> Tour Description Status

> Postings Time Code Meal Hours

> Remarks Code

> 1·May.05 DAY OFF PENDING

PENDING

PENDING

> ![](paid-version-4-user-manual/111.png)![](paid-version-4-user-manual/112.png)Payroll Mall Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 40

Incomplete Days: 6

Comp/Flex: C Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 09:30P-10:00P RG REG TIME 00:30

> 10: OOP-01: OOA RG REG TIME 03:00

> 4-May-05 10 07:00A-03:30P APPROVED

> 07:00A-NOON RG REG TIME 05:00

> NOON-01:00P AA AUTH ABS 30 00:30

> AA GRANTED BY SUPR.

> 01:00P-04:00P RG REG TIME 03:00

> PTP Remarks: TEST

PENDING APPROVED

![](paid-version-4-user-manual/113.png) Payroll Main Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

> Duty Basis: 2 FLSA: E Normal Hours: 40

> Incomplete Days: 6

> Tour Description

XXX·XX-0001

> Comp/Flex: C

> Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 7-May-05 DAY OFF PENDING

> 07:00A-08:00A RG REG TIME 0 01:00

> 8-May-05 1 DAY OFF DAY OFF

> 9-May-05 10 07:00A-03:30P APPROVED

> 07:00A-03:30P AL ANNUAL LV 60 07:30

> SF71 ON FILE

> 10-May-05 1 DAY OFF DAY OFF

RTED

> Payroll Main Menu

> ESR Exceptions For Entire Memoranda

> This option generates a report that lists any part-time physician who has not yet completed an ESR for any pay period within their memorandum, allowing supervisors to identify and monitor incomplete daily ESRs.

> You can choose whether or not to include the current pay period in the report, and you may include all part-time physicians in the T&L, or enter individual part-time physicians.

> ![](paid-version-4-user-manual/114.png)

![](paid-version-4-user-manual/115.png)![](paid-version-4-user-manual/116.png)Payroll Main Menu

> VA TIME & ATTENDANCE SYSTEM

> ESR EXCEPTIONS FOR ENTIRE MEMORANDA

> Duty Basis: 2 FLSA: E Normal Hours: 10

Comp/Flex: Station: 528

> Memorandum & Leave Status thru PP 04-23 Ending

> Start Date: OCT 03, 2004 1 Agreed Hours: 260.00 1

> TERMINATED: OCT 30, 2004 I Hours Worked: 17.50 I

> 2of26PP= 7.69% ICarryoverHrs: 0.001

> Hrs Completed= 6.73% 1 Total Hrs: 17.50 1

> This memorandum has ended

Sat 27-Nov-04

> LWOP Hrs:

> Non Pay Hrs:

> Off Target Hrs:

> Off Target %:

> 0.00

> 0.00

> ·2.50

-12.50

> L Ba 1 : 67. 00 Approved future AL th ru Leave Year: 0. 00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 0

> \# Pay Period Date Status

> ....................................

> 1 04-20 OCT 03, 2004 PENDING OCT 07, 2004 PENDING OCT 14, 2004 PENDING OCT 15, 2004 PENDING OCT 16, 2004 PENDING

> Payroll Supervisor Menu

> Payroll Supervisor Menu

> Changed Option

> Open Next Pay Period

> This option was modified to initialize the ESR daily status and auto post holidays, leave, and extended absences to the ESR for the new pay period. It will also update the status of the memorandum from NOT STARTED to ACTIVE, if the pay period being opened is the first pay period covered by the memorandum.

> T&A Supervisor Menu

> Changed Options

> Supervisory Approvals

> This option was modified to automatically post an approved leave request to the ESR in an open pay period if the employee taking leave is a part-time physician with an active memorandum.

> If any portion of the leave request covers a future pay period that has not been opened yet, the appropriate ESR records will be automatically posted when the pay period is opened.

> If the leave request does not pass all of the necessary checks, it will not be posted to the ESR record.

> Pay Period Certification

> This option was modified to review the part-time physician's ESR and to update the various categories of hours worked in the PART-TIME PHYSICIAN MEMORANDUM (#458.7) file when the associated timecard is certified.

Payroll Supervisor Menu

> New Options

> PT Physician Menu

> This new menu has been added to the existing T&A Supervisor Menu. The PT Physician Menu contains all of the necessary options to allow the T&A and T&A OT Supervisor to monitor and maintain the part-time physician’s Memorandum of Service Level Expectations.

> Approve Signed ESRs

> The T&A supervisor is required to review each signed day of the part-time physician's ESR, and take one of the following actions.

> Approve - if the ESR day appears to be correct.

> Resubmit - if the physician needs to correct the ESR day.

> Bypass - to skip the day now and take action on it at a later time.

> The (A)pprove, (B)ypass or (R)esubmit actions may be applied to an individual day or to all the days listed.

> To take action on an individual day, select the day by entering its item number from the list and then enter the action you wish to apply to this day. If the Resubmit action is selected, you will also be prompted to enter a short text description like your phone number etc.

> Individual days that have been marked with an action will not be altered when you apply another action type to the remaining days in the list.

> Once you have completed your entries, an electronic signature code is required to complete the process.

> When the T&A Supervisor approves a signed day, this option attempts to update the part-time physician's timecard for that day. Updates to the timecard will be screened based on the status of the timecard and the effect of any potential update. If the timecard associated with the ESR day being approved has a status of TIMEKEEPER, then the approval action will always update the timecard.

> An individual ESR approval may be rejected if the following conditions are met.

> 1\. The timecard associated with the ESR day being approved has a status of

> Transmitted to Austin or Payroll.

> Payroll Supervisor Menu

> 2\. There is a discrepancy between the timecard and ESR. That is, if for any type of time, such as sick leave, annual leave, military leave, etc., the total number of hours posted to the timecard is not equal to the total number of hours posted to the ESR.

> 3\. The type of time discrepancy must also involve a type of time that is reported to the AAC. So, in general, the type of time—RG—Regular Hours, is not considered, since it is only posted to the ESR.

> If the first condition is met, then the software checks to determine if an ESR approval would result in an incorrect report to the AAC due to a discrepancy between the timecard and the ESR. To do this, total hours are calculated for all types of time that are recorded on the timecard and all the types of time that are on the ESR for a particular day. Next, the totals for each type of time are compared. If any of the total hours for a type of time, like sick leave, annual leave, holiday excused, military leave, etc., don't match; then the ESR cannot be approved, and a message is displayed to the supervisor, showing the type of time that does not

> match, and the total hours for that type of time.

> Following is an example of the type of message that could be displayed. It shows the discrepancies between the timecard hours and the ESR hours, followed by the ESR and timecard postings.

> ESR approval REJECTED for PAIDPTP,ONE on day 4 in PP 04-18.

> Time Discrepancies must be resolved. Timecard Status: TRANSMITTED TO AUSTIN Payroll must initiate corrected timecard or physician must resubmit ESR.

> ESR approval REJECTED for PAIDPTP,ONE on day 4 in PP 04-18.

> TIME DISCREPANCIES BETWEEN TIMECARD AND ESR

> Error Type of Time Timecard Hrs ESR Hrs

> -------------------------------------------------------------- LEAVE mismatch TR 0 1.5

> ESR POSTING

> Item Date Scheduled Tour Work/Leave Posted Hours Meal Status

> ---------------------------------------------------------------------- Wed 8-Sep-04 03:30P-MID Shift 2

> 04:00P-06:00P TRAINING 01:30 30

> 08:00A-09:00A REG TIME 01:00 Approved

> TIMECARD POSTING

> Date Scheduled Tour Tour Exceptions

> ------------------------------------------------------------ Wed 8-Sep-04 03:30P-MID

> Shift 2

Payroll Supervisor Menu

> There are three special cases:

> 1\. Since RG should not be posted on the timecard and only on the ESR, RG is generally ignored.

> 2\. Since WP with remarks On Suspension or AWOL can only be posted to the timecard, WP with these remarks is also ignored.

> 3\. Since on any day that NP is posted to the timecard there can be no work performed, a check is performed to make sure that there is no RG or any leave posted to the ESR when NP is on the timecard.

> The comparison does not consider start and stop times, specifically. E.g. A timekeeper may need to post around a lunch for leave during the middle of the day on the physician’s timecard. The timekeeper posts, 10a-noon Sick Leave then

> 12:30pm-2pm sick leave. The part-time physician then updates their ESR with 10a-

> 2:00pm Sick Leave and puts 30 minutes in the meal field. This would be o.k. since the total sick leave would be 3.5 hours in each case.

> ![](paid-version-4-user-manual/117.png)![](paid-version-4-user-manual/118.png)![](paid-version-4-user-manual/119.png)Payroll Supervisor Menu

> ay Per: 05·01

> AIDPTPIONE

> VA TIME & ATTENDANCE SYSTEM

Supervisory Review for Part Time Physicians in T&L: 028

> XXX·XX·0001 Incomplete Days: 0

> tern

Date Scheduled Tour Work/Leave Posted Hours Meal Status

> Wed 19·Jan·05 01:00P·04:00P Thu 20·Jan·05 01:00P·04:00P Sat 22·Jan·05 01:00P·05:00P

07:00A·04:00P

07:00A·04:00P

08:00A·03:00A

REG TIME REG TIME REG TIME

09:00 0

09:00 0

> 19:00

> (A)pproveI (B)ypassI (R)esubmit or enter an item

\#: 1 Wed

19·Jan·05

> Wed 19·Jan·05 01:00P·04:00P (A)pproveI (B)ypassI (R)esubmit: nter Remarks: 518·555·0000

07:00A·04:00P

> r Resubmit

REG TIME

09:00 0

Payroll Supervisor Menu

> ![](paid-version-4-user-manual/120.png)![](paid-version-4-user-manual/121.png)![](paid-version-4-user-manual/122.png)If all of the days in the list need to have the same action or if you have previously selected and marked all of the days that need to have a different action, you can then enter the necessary action to apply to the remaining days.

> !!! <span class="mark">VMS·KEA! 420</span> fllf3

> ay Per: 05·01

> AIDPTP 1 0NE

> VA TIME & ATTENDANCE SYSTEM

Supervisory Review for Part Time Physicians in T&L: 028

> xxx.xx.ooo1 Incomplete Days: 0

> tern Date

Scheduled Tour Work/Leave Posted

Hours Meal Status

> Wed 19·Jan·05 01:00P·04:00P Thu 20·Jan·05 01:00P·04:00P Sat 22·Jan·05 01:00P·05:00P

07:00A·04:00P

07:00A·04:00P

08:00A·03:00A

REG TIME REG TIME REG TIME

09:00 0

09:00 0

> 19:00

Resubmit

> (A)pproveI (B)ypassI (R)esubmit or enter an item#: Approve

> Payroll Supervisor Menu

> After each individual or group action has been entered, the software will update the

> ![](paid-version-4-user-manual/123.png)![](paid-version-4-user-manual/124.png)Status field.

> ay Per: 05-01

> AIDPTP,ONE

> VA TIME & ATTENDANCE SYSTEM

Supervisory Review for Part Time Physicians in T&L: 028

> xxx.xx.ooo1 Incomplete Days: 0

> tern Date Scheduled Tour Work/Leave Posted Hours Meal Status

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Wed 19-Jan-05 01:00P-04:00P</p>
</blockquote></th>
<th><blockquote>
<p>07:00A-04:00P</p>
</blockquote></th>
<th><blockquote>
<p>REG TIME</p>
</blockquote></th>
<th><blockquote>
<p>09:00 0</p>
</blockquote></th>
<th><blockquote>
<p>Resubmit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Thu 20-Jan-05 01:00P-04:00P</p>
</blockquote></td>
<td><blockquote>
<p>07:00A-04:00P</p>
</blockquote></td>
<td><blockquote>
<p>REG TIME</p>
</blockquote></td>
<td><blockquote>
<p>09:00 0</p>
</blockquote></td>
<td><blockquote>
<p>Approved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sat 22-Jan-05 01:00P-05:00P</p>
</blockquote></td>
<td><blockquote>
<p>08:00A-03:00A</p>
</blockquote></td>
<td><blockquote>
<p>REG TIME</p>
</blockquote></td>
<td><blockquote>
<p>19:00</p>
</blockquote></td>
<td><blockquote>
<p>Approved 1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> elect an item \#:

Payroll Supervisor Menu

> ![](paid-version-4-user-manual/125.png)![](paid-version-4-user-manual/126.png)![](paid-version-4-user-manual/127.png)You then see the Supervisory Action Summary, and are prompted for your electronic signature code to complete the approval process.

> !!! <span class="mark">VMS·KEA• 420</span> I!IEJ

> upervisory Action Summary

> 3 actions require your electronic signature before being committed to the database.

> 2 ESR record marked for approval. (signature required)

> 1 ESR records marked for resubmission. (signature required)

> 5 ESR records with no action.

> nter your Current Signature Code: SIGNATURE VERIFIED

> 1 Approve Signed ESRs

> 2 Memoranda Report

> 3 Display PP ESR Exceptions

> 4 ESR Exceptions For Entire Memoranda

> 5 Display Pay Period ESR

> 6 Unlock Daily ESR

> Payroll Supervisor Menu

> Memoranda Report

> This option generates a report which allows the supervisor to review a memorandum for a selected employee and pay period that can be used to monitor the status of the hours worked and leave taken since the memorandum began.

> After an employee has been selected, enter any pay period covered by the memorandum and then select a device.

> VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> Select EMPLOYEE: PAIDPTP,ONE 000-28-0001

> Select PAY PERIOD: 04-21

> Select Device: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

> The software displays all of the information related to the part-time physician's

> Memorandum of Service Level Expectations.

Payroll Supervisor Menu

> The first page of the report includes fields that help to identify the part-time physician (name, SSN, T&L, etc.), a memorandum summary (start/end dates, agreed hours, completion percentages, etc.), a listing of pay periods covered by the memorandum, and the hours credited during each of these pay periods.

> ![](paid-version-4-user-manual/128.png)![](paid-version-4-user-manual/129.png)!!! <span class="mark">VMS ·KEAI420</span> <span class="mark">f3</span>

> PP:04-21 VA TIME & ATTENDANCE SYSTEM DISPLAY PT PHYSICIAN MEMORANDA

> PAIDPTP,ONE

> 6114/05

XXX-XX-0001

> Pay Plan: L

> ![](paid-version-4-user-manual/130.png)L: 221

Duty Basis: 2

FLSA: E Normal Hours: 40

Comp/Flex: C

Station: 500

> Memorandum & Leave

> Start Date: OCT 03, 2004

> End Date: OCT 01, 2005

> 16 of 26 PP = 61.54% Hrs Completed = 57.68% Agreement will be met by

Status thru PP 05-10 Ending Sat 28-May-05

> I Agreed Hours: 1040.00 I LWOP Hrs: 1.00

> I Hours Worked: 581.75 I Non Pay Hrs: 0.00

> I Carryover Hrs: 0.00 I Off Target Hrs: -39.75

> I Total Hrs: 599.25 I Off Target%: -6.22

averaging 43.98 Hrs/PP during remainder of memo.

> Bal: 200.00 Approved future AL thru Leave Year: 0.00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 24

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04-20:</p>
</blockquote></th>
<th><blockquote>
<p>41.50</p>
</blockquote></th>
<th><blockquote>
<p>04-26:</p>
</blockquote></th>
<th><blockquote>
<p>40.00</p>
</blockquote></th>
<th><blockquote>
<p>05-06:</p>
</blockquote></th>
<th><blockquote>
<p>34.50</p>
</blockquote></th>
<th><blockquote>
<p>05-12:</p>
</blockquote></th>
<th><blockquote>
<p>05-18:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04-21:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-01:</p>
</blockquote></td>
<td><blockquote>
<p>46.00</p>
</blockquote></td>
<td><blockquote>
<p>05-07:</p>
</blockquote></td>
<td><blockquote>
<p>29.25</p>
</blockquote></td>
<td><blockquote>
<p>05-13:</p>
</blockquote></td>
<td><blockquote>
<p>05-19:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-22:</p>
</blockquote></td>
<td><blockquote>
<p>34.50</p>
</blockquote></td>
<td><blockquote>
<p>05-02:</p>
</blockquote></td>
<td><blockquote>
<p>40.00</p>
</blockquote></td>
<td><blockquote>
<p>05-08:</p>
</blockquote></td>
<td><blockquote>
<p>36.75</p>
</blockquote></td>
<td><blockquote>
<p>05-14:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-23:</p>
</blockquote></td>
<td><blockquote>
<p>20.00</p>
</blockquote></td>
<td><blockquote>
<p>05-03:</p>
</blockquote></td>
<td><blockquote>
<p>39.50</p>
</blockquote></td>
<td><blockquote>
<p>05-09:</p>
</blockquote></td>
<td><blockquote>
<p>45.25</p>
</blockquote></td>
<td><blockquote>
<p>05-15:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04-24:</p>
</blockquote></td>
<td><blockquote>
<p>30.00</p>
</blockquote></td>
<td><blockquote>
<p>05-04:</p>
</blockquote></td>
<td><blockquote>
<p>42.00</p>
</blockquote></td>
<td><blockquote>
<p>05-10:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-16:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04-25:</p>
</blockquote></td>
<td><blockquote>
<p>46.50</p>
</blockquote></td>
<td><blockquote>
<p>05-05:</p>
</blockquote></td>
<td><blockquote>
<p>26.00</p>
</blockquote></td>
<td><blockquote>
<p>05-11:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>05-17:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue:

> Payroll Supervisor Menu

> Following is the second page of the report. If there are any prior pay periods with incomplete ESRs, they will be listed next. If any Non-Pay or Leave Without Pay occurred during the memorandum, it will be listed next along with the pay period in which it occurred. Finally, any comments (Initial, Reconciliation, Termination,

> etc.), and related dates and times when actions were taken are displayed. If the memorandum has ended and the part-time physician has entered their reconciliation choice via the electronic form, their choice and any reconciliation comments will also be listed.

> ![](paid-version-4-user-manual/131.png)

Payroll Supervisor Menu

> Display PP ESR Exceptions

> This option allows Supervisors to review daily ESR exceptions for part-time physicians with a Memorandum of Service Level Expectations. It can be used to verify that part-time physicians have completed each day within the pay period with a scheduled Tour of Duty and to monitor other work performed on scheduled days off.

> ![](paid-version-4-user-manual/132.png)

> Payroll Supervisor Menu

> ESR Exceptions For Entire Memoranda

> This option generates a report that lists any part-time physician who has not yet completed an ESR for any pay period within their memorandum, allowing supervisors to identify and monitor incomplete daily ESRs.

> You can choose whether or not to include the current pay period in the report, and you may include all part-time physicians in the T&L, or enter individual part-time physicians.

> ![](paid-version-4-user-manual/133.png)

![](paid-version-4-user-manual/134.png)![](paid-version-4-user-manual/135.png)Payroll Supervisor Menu

> VA TIME & ATTENDANCE SYSTEM

> ESR EXCEPTIONS FOR ENTIRE MEMORANDA

> Duty Basis: 2 FLSA: E Normal Hours: 10

Comp/Flex: Station: 528

> Memorandum & Leave Status thru PP 04-23 Ending

> Start Date: OCT 03, 2004 1 Agreed Hours: 260.00 1

> TERMINATED: OCT 30, 2004 I Hours Worked: 17.50 I

> 2of26PP= 7.69% ICarryoverHrs: 0.001

> Hrs Completed= 6.73% 1 Total Hrs: 17.50 1

> This memorandum has ended

Sat 27-Nov-04

> LWOP Hrs:

> Non Pay Hrs:

> Off Target Hrs:

> Off Target %:

> 0.00

> 0.00

> ·2.50

-12.50

> L Ba 1 : 67. 00 Approved future AL th ru Leave Year: 0. 00 Max carryover: 240

> Potential AL hours to be lost by JAN 07, 2006 excluding Approved AL: 0

> \# Pay Period Date Status

> ....................................

> 1 04-20 OCT 03, 2004 PENDING OCT 07, 2004 PENDING OCT 14, 2004 PENDING OCT 15, 2004 PENDING OCT 16, 2004 PENDING

> Payroll Supervisor Menu

> Display Pay Period ESR

> This option allows the supervisor to review a part-time physician's ESR record. Any pay period from a current or past memorandum may be selected. If the next pay period has already been opened, it may also be selected.

> The T&A Supervisor selects a T&L Unit, a part-time physician and the date they need to unlock.

> VA TIME & ATTENDANCE SYSTEM UNLOCK DAILY ESR

> Select T&L Unit: 028

> Select EMPLOYEE: PAIDPTP,ONE PAIDPTP,ONE 000-28-0001

> Posting Date: 3/7/2005 (MAR 07, 2005)

> Once the posting date has been selected, the entire ESR for that pay period is displayed for the Supervisor to review and verify that they have selected the correct ESR day to unlock.

![](paid-version-4-user-manual/136.png)![](paid-version-4-user-manual/137.png)Payroll Supervisor Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2 FLSA: E Normal Hours: 40 Comp/Flex: C Station: 500

> Incomplete Days: 6

> Tour Description Status

> Postings Time Code Meal Hours

> Remarks Code

> 1-May-05 DAY OFF PENDING

> 2-May-05 10 07:00A-03:30P PENDING

> ue 3-May-05 DAY OFF PENDING

> ![](paid-version-4-user-manual/138.png)![](paid-version-4-user-manual/139.png)Payroll Supervisor Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 40

Incomplete Days: 6

Comp/Flex: C Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 09:30P-10:00P RG REG TIME 00:30

> 10: OOP-01: OOA RG REG TIME 03:00

> 4-May-05 10 07:00A-03:30P APPROVED

> 07:00A-NOON RG REG TIME 05:00

> NOON-01:00P AA AUTH ABS 30 00:30

> AA GRANTED BY SUPR.

> 01:00P-04:00P RG REG TIME 03:00

> PTP Remarks: TEST

PENDING APPROVED

![](paid-version-4-user-manual/140.png)Payroll Supervisor Menu

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 05-09

> Duty Basis: 2 FLSA: E Normal Hours: 40

> Incomplete Days: 6

> Tour Description

XXX·XX-0001

> Comp/Flex: C

> Station: 500

> Status

> Postings Time Code

Remarks Code

Meal Hours

> 7-May-05 DAY OFF PENDING

> 07:00A-08:00A RG REG TIME 0 01:00

> 8-May-05 1 DAY OFF DAY OFF

> 9-May-05 10 07:00A-03:30P APPROVED

> 07:00A-03:30P AL ANNUAL LV 60 07:30

> SF71 ON FILE

> 10-May-05 1 DAY OFF DAY OFF

RTED

> Payroll Supervisor Menu

> Unlock Daily ESR

> ![](paid-version-4-user-manual/141.png)![](paid-version-4-user-manual/142.png)This option allows Supervisors to select and unlock individual days in prior Pay Period ESRs, so the part-time physician can change or complete any incomplete daily ESRs.

> <span class="mark">MS ·KEA• 420</span> I!IEJ

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 04-20

> 5/17/05 .

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 10

Incomplete Days: 5

Comp/Flex: Station: 528

> Status

> 3-0ct-04

> Postings Time Code

> Remarks Code

DAY OFF

Meal Hours

APPROVED

> 4-0ct-04

> 5-0ct-04

> 6-0ct-04

> u 7-0ct-04

> Sup Remarks:

> 8-0ct-04

> 9-0ct-04

> 10-0ct-04

> 11-0ct-04

> e 12-0ct-04

> 07:00A-04:00P DAY OFF

> DAY OFF DAY OFF

> 1 DAY OFF

000-666-0000

> 1 DAY OFF

> 1 DAY OFF

> 1 DAY OFF

> 1 DAY OFF

> 1 DAY OFF

RG REG TIME

09:00

DAY OFF DAY OFF DAY OFF RESUBMIT

DAY OFF DAY OFF DAY OFF DAY OFF DAY OFF

![](paid-version-4-user-manual/143.png)![](paid-version-4-user-manual/144.png)![](paid-version-4-user-manual/145.png)Payroll Supervisor Menu

> <span class="mark">MS- KEA• 420</span> I!IEJ

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 04-20

> Duty Basis: 2 FLSA: E Normal Hours: 10

> Incomplete Days: 5

> Tour Description

> XXX-XX-0001

Comp/Flex:

Station: 528

> Status

> Sup Remarks:

> u 14-0ct-04

> 15-0ct-04

> 16-0ct-04

> Postings Time Code

> Remarks Code

> 1 DAY OFF

666-555-0000

> 1 DAY OFF

> 1 DAY OFF

> 90 07:00A-06:00P

Meal Hours

RESUBMIT RESUBMIT

RESUBMIT

NOT STARTED

> onfirm Unlock of OCT 06, 2004 (YIN): YES

> nter Remarks: 666-000-0000

> Payroll Supervisor Menu

> If you answer YES at the "Confirm Unlock'' prompt, a remarks prompt is displayed. The Supervisor may enter a short comment or phone number.

> ![](paid-version-4-user-manual/146.png)![](paid-version-4-user-manual/147.png)After the remarks are entered, the day is given a status of RESUBMIT.

> <span class="mark">MS ·KEA• 420</span> I!IEJ

> VA TIME & ATTENDANCE SYSTEM PT PHYSICIAN ESR FOR PP 04-20

> 5/17/05 .

XXX-XX-0001

> Duty Basis: 2

> Tour Description

> FLSA: E Normal Hours: 10

Incomplete Days: 6

Comp/Flex: Station: 528

> Status

> 3-0ct-04

> Postings Time Code

> Remarks Code

DAY OFF

Meal Hours

APPROVED

> 4-0ct-04

> 5-0ct-04

> 6-0ct-04

> Sup Remarks:

> u 7-0ct-04

> Sup Remarks:

> 8-0ct-04

> 9-0ct-04

> 10-0ct-04

> 11-0ct-04

> 07:00A-04:00P DAY OFF

> DAY OFF

> 1 DAY OFF

666-000-0000

> 1 DAY OFF

000-666-0000

> 1 DAY OFF

> 1 DAY OFF

> 1 DAY OFF

> 1 DAY OFF

RG REG TIME

09:00

DAY OFF DAY OFF RESUBMIT

RESUBMIT DAY OFF

DAY OFF

DAY OFF

DAY OFF

Payroll Supervisor Menu

> Payroll Supervisor Menu

> Data Supplement

> PTP ESR DATA FILE DESCRIPTIONS

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ESR START TIME</p>
</blockquote></td>
<td><blockquote>
<p>The time the part-time physician actually began work/leave.</p>
<p>Time may be entered in any of the following formats: 8A or 8a, 8:00A,</p>
<p>8:15A, 8:15AM or military time: 0800,</p>
<p>1300; or MID or 12M for midnight; NOON or 12N for noon. Time must be in quarter hours; e.g., 8A or 8:15A or 8:30A or 8:45A.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ESR STOP TIME</p>
</blockquote></td>
<td><blockquote>
<p>The time the part-time physician actually stopped work/leave.</p>
<p>Time may be entered in any of the following formats: 8A or 8a, 8:00A,</p>
<p>8:15A, 8:15AM or military time: 0800,</p>
<p>1300; or MID or 12M for midnight; NOON or 12N for noon. Time must</p>
<p>be in quarter hours; e.g., 8A or 8:15A</p>
<p>or 8:30A or 8:45A.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ESR TYPE OF TIME</p>
</blockquote></td>
<td><blockquote>
<p>The type of time worked/leave taken. Following are the choices displayed if</p>
<p>you enter a ?.</p>
<p>AA Authorized Absence</p>
<p>AD Adopt</p>
<p>AL Annual Leave</p>
<p>CB Family Care</p>
<p>HX Holiday Excused</p>
<p>DL Donor Leave</p>
<p>ML Military Leave</p>
<p>NL Non-pay Annual Leave</p>
<p>RG Regular Time</p>
<p>RL Restored Annual Leave</p>
<p>SL Sick Leave</p>
<p>WP Leave Without Pay</p>
</blockquote></td>
</tr>
</tbody>
</table>

Payroll Supervisor Menu

> PTP ESR DATA FILE DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESR SPECIAL CODE</p>
</blockquote></td>
<td><blockquote>
<p>A code which further describes the</p>
<p>TYPE OF TIME entered. Only the appropriate choices that correspond</p>
<p>to the TYPE OF TIME entered will</p>
<p>be allowed. Enter a ? for a list of the appropriate choices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESR MEAL TIME</p>
</blockquote></td>
<td><blockquote>
<p>The amount of time, if any, you took for a meal time.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAILY ESR REMARKS</p>
</blockquote></td>
<td><blockquote>
<p>Any further comments you would like to enter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESR DAILY STATUS</p>
</blockquote></td>
<td><blockquote>
<p>The status of the part-time physician's daily Electronic</p>
<p>Subsidiary Record (ESR). The</p>
<p>possible values are: NOT STARTED PENDING SIGNED RESUBMIT APPROVED</p>
<p>DAY OFF.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PT PHYSICIAN DATE/TIME STAMP</p>
</blockquote></td>
<td><blockquote>
<p>The Date and Time the part-time physician electronically signed their</p>
<p>daily ESR record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESR SUPERVISOR REMARKS</p>
</blockquote></td>
<td><blockquote>
<p>Comments entered by the Supervisor after they have marked a daily ESR</p>
<p>as RESUBMIT. This can be text up</p>
<p>to 17 characters.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Payroll Supervisor Menu

> PTP ESR DATA FILE DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESR DAY LAST SIGN METHOD</p>
</blockquote></td>
<td><blockquote>
<p>This field indicates how the current</p>
<p>ESR record was signed. If the employee signs the ESR day, then the status will be MANUAL POST. However, it is also possible for the software to sign the ESR day on</p>
<p>behalf of the employee based on some other action such as supervisor approval of an electronic leave request, or auto-posting of an extended absence, or auto-posting of holiday excused The possible values are:</p>
<p>MANUAL POST EXTENDED ABSENCE LEAVE REQUEST HOLIDAY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

Payroll Supervisor Menu

> WORK SUMMARY SCREEN DESCRIPTIONS

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMPLOYEE NAME</p>
</blockquote></td>
<td><blockquote>
<p>The employee’s name in the following format: LAST NAME followed by a</p>
<p>comma; FIRST NAME or INITIAL;</p>
<p>followed by a blank space; MIDDLE NAME or INITIAL; if applicable a</p>
<p>blank space, JR, SR or INITIAL.</p>
<p>Example:</p>
<p><strong>LASTNAME,FIRSTNAME MI JR</strong></p>
<p>No periods are placed after either initials or titles.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>STATION NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>The number assigned to a</p>
<p>Department of Veterans Affairs (VA) Installation for identification and</p>
<p>control purposes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T &amp; L UNIT</p>
</blockquote></td>
<td><blockquote>
<p>Time and Leave Unit. A number that identifies a specific group of</p>
<p>employees for time and leave tracking purposes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>The number used for identification and control purposes to refer to an</p>
<p>employee.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NORMAL HOURS</p>
</blockquote></td>
<td><blockquote>
<p>This field contains the number of normal hours an employee is</p>
<p>scheduled to work in a pay period</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DUTY BASIS</p>
</blockquote></td>
<td><blockquote>
<p>Code identifies the time basis that an employee is scheduled to work. An</p>
<p>employee may have a full-time (1),</p>
<p>part-time (2), intermittent (3) basis work schedule.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAY PLAN</p>
</blockquote></td>
<td><blockquote>
<p>Code identifies the pay system under which the employee's Compensation</p>
<p>is determined.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Payroll Supervisor Menu

> WORK SUMMARY SCREEN DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMPRESSED/FLEXITIME CODE</p>
</blockquote></td>
<td><blockquote>
<p>Indicates an employee is working a tour that is approved as a compressed</p>
<p>or flextime schedule. The field can be blank or coded with a "C" for</p>
<p>Compressed or "F" for flextime.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FLSA</p>
</blockquote></td>
<td><blockquote>
<p>Code identifies whether an employee is covered under the Fair Labor</p>
<p>Standards Act (FLSA) minimum wage and overtime provisions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANNUAL LEAVE CURRENT BALANCE</p>
</blockquote></td>
<td><blockquote>
<p>The annual leave balance this leave year to date.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAY PERIOD</p>
</blockquote></td>
<td><blockquote>
<p>This field contains the year-pay period in the form of YY-PP where</p>
<p>YY represents the year and PP</p>
<p>represents the pay period. This field reflects the pay period that was</p>
<p>selected by the part-time physician</p>
<p>from the action pick list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>START DATE</p>
</blockquote></td>
<td><blockquote>
<p>The Start Date of the part-time physician’s 364 Memorandum of</p>
<p>Service Level Expectations. The</p>
<p>Start Date will always be the first day of a pay period. The</p>
<p>memorandum will cover exactly 26</p>
<p>full pay periods.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>END DATE</p>
</blockquote></td>
<td><blockquote>
<p>The End Date of the part-time physician's 364 day Memorandum of</p>
<p>Service Level Expectations. The End</p>
<p>Date will always be the last day of a</p>
<p>Pay Period.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Payroll Supervisor Menu

> WORK SUMMARY SCREEN DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AGREED # OF HOURS</p>
</blockquote></td>
<td><blockquote>
<p>The number of hours that the part- time physician agreed to work during</p>
<p>their 364 day memorandum. This number must be equally divisible by</p>
<p>26.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL HOURS WORKED</p>
</blockquote></td>
<td><blockquote>
<p>The total hours worked by the part- time physician since the beginning of</p>
<p>their memorandum. This includes both scheduled tour hours and extra</p>
<p>hours worked.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AVE HRS/PP TO COMPLETE MEM</p>
</blockquote></td>
<td><blockquote>
<p>The average number of hours that the part-time physician will have to</p>
<p>work to meet the Agreed Hours in</p>
<p>their Memorandum of Service Level</p>
<p>Expectations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AGREED # OF HOURS</p>
</blockquote></td>
<td><blockquote>
<p>The number of hours that the part- time physician agreed to work during their 364 day memorandum. This</p>
<p>number must be equally divisible by</p>
<p>26 (the number of pay periods in a calendar year).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>% OF HOURS COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>The percentage of scheduled hours completed since the beginning of the</p>
<p>memorandum. This percentage</p>
<p>reflects any AWOL (Absent Without Leave) hours that might have occurred during the memorandum. This field would also include any Non Pay hours.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Payroll Supervisor Menu

> WORK SUMMARY SCREEN DESCRIPTIONS, cont.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BRIEF DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>% OFF TARGET</p>
</blockquote></td>
<td><blockquote>
<p>The percentage that the part-time physician is either ahead or behind</p>
<p>on meeting their Agreed Hours. This</p>
<p>percentage is based on the part-time physician's total Hours Worked and their Normal Hours per Pay Period.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix B: Upgrade ETA For Telework (Increment 1-Comp Time Expiration Updates) (Patch PRS\*4.0\*133)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces changes to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software for the Upgrade ETA for Telework Project (Increment 1 – Comp Time). These changes revise the expiration of compensatory (“comp”) time and credit hours from eight to 26 pay periods. Additionally, the patch will enable employees to view their comp time/credit hours balances for the preceding 26 pay periods.

Currently VistA PAID ETA receives up to eight individual pay period comp time/credit hours balances from AITC, and calculates an expiration date based on seven pay periods. After this patch is implemented, VistA PAID ETA will display a subtotal of comp time/credit hours earned over the past 26 pay periods. In cases where comp time/credit hours were earned during the interval of the preceding nine to 26 pay periods, VistA PAID ETA will report the actual hours and expiration for each of the oldest eight pay periods, with the remaining balances from the ninth through the most recently earned as a subtotal. The patch also enables supervisors to view comp time/credit hours balances for their direct reports.

## Patch Nomenclature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Release Date: September 2011
- Patch Name: PRS\*4.0\*133

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch revises an existing VistA PAID/ETA application. There are no new hardware compatibility requirements.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch revises an existing VistA PAID/ETA application. There are no new system specifications.

# Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch for Increment 1 includes changes to existing VistA PAID/ETA functions:

1.  The expiration for comp time/credit hours values is increased from eight to 26 pay periods;
2.  The comp time/credit hours pay period balance display includes additional information and the sorting method is changed; and
3.  The Supervisory Approvals function displays information consistent with the policy change.

## Changes to the Pay Period Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The policy for expiration of comp time/credit hours was revised effective February 18, 2007. The time period in which an employee may use comp time/credit hours was revised from eight to 26 periods. The time limit on the use of credit hours was eliminated. The restriction on carrying no more than 24 credit hours into the next pay period was not changed. Comp time/credit hours will continue to be stored in the same balance, and if necessary, ETA users will continue to manually track the portion of the balances that are credit hours.

After the policy for expiration of comp time rules was implemented, the Austin Automation Technology Center (AITC) was updated to support storing 26 pay periods of comp time. VistA PAID/ETA transmits comp time information to AITC each pay period. AITC was also updated to maintain the total balance of employees’ comp time/credit hours, and transmit that information to VistA PAID/ETA in the existing COMPTIME download field.

The value transmitted from AITC to VistA PAID/ETA each pay period is the current unused balance of comp time/credit hours earned over the preceding 26 pay periods. ETA stores this balance in the PAID EMPLOYEE file (#450) in the COMPTIME/CREDIT HRS BALANCE field (#496).

## Changes to the Comp Time/Credit Hours Balance Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 shows the options for displaying role-based comp time/credit hours balances and their expiration dates. All three options were modified as part of this patch, and the following roles were affected: (1) Employee, (2) Timekeeper, and (3) Supervisor.

Leave Balances \[PRSA LV BAL-EMP\]

Employee Leave Balances \[PRSA LV BAL-TK\]

Employee Leave Balances \[PRSA LV BAL-SUP\]

Figure : VistA PAID/ETA report options modified by this patch.

Currently VistA PAID/ETA receives eight individual comp time/credit hours balances for up to eight pay periods. This patch includes the following changes to the reports listed in :

1.  Includes total comp time/credit hours balance from the last 26 pay periods;
2.  Restructures the reports into columnar format;
3.  Includes the pay period in which the comp time/credit hours were earned, when available;
4.  Balances earned more than eight pay periods before the current pay period are summarized on the last line of the itemized comp time/credit hours listing; and
5.  The “Must be used by” dates are extended from eight to 26 pay periods.

Figure 2 and Figure 3 show what the application will look like before and after the patch is implemented, respectively:

Balances are as of Sat 12-Mar-11

Leave Group: 3

Annual Leave Balance: 686.000

Sick Leave Balance: 357.500

Comp Time/Credit Hours: 4.000 must be used by Dec 03, 2011

Comp Time/Credit Hours: 8.000 must be used by Dec 17, 2011

Comp Time/Credit Hours: 1.500 must be used by Dec 31, 2011

Comp Time/Credit Hours: 2.250 must be used by Jan 14, 2012

Comp Time/Credit Hours: 1.750 must be used by Feb 11, 2012

Comp Time/Credit Hours: 0.500 must be used by Feb 26, 2011

Comp Time/Credit Hours: 3.500 must be used by Apr 09, 2011

Comp Time/Credit Hours: 4.500 must be used by May 21, 2011

Figure : Original screen.

EMPLOYEE LEAVE BALANCES

PAID,EMPLOYEE A Leave Group: 3 nnn-nn-nnnn

Balances are as of Pay Period 11-17 (Sat 27-Aug-11)

Annual Leave Balance: 240.000

Sick Leave Balance: 1000.000

Comp Time/Credit Hours (CT/CH) Pay Period Balances

Pay Period Earned \# of Hours Must be used by

10-18 10.000 Sep 10, 2011

10-19 8.000 Sep 24, 2011

10-20 0.250 Oct 08, 2011

10-23 0.500 Nov 19, 2011

10-25 0.750 Dec 17, 2011

10-26 4.500 Dec 31, 2011

11-02 5.500 Jan 28, 2012

11-04 10.000 Feb 25, 2012

\*11-05 thru 11-17 22.750 Mar 10, 2012 thru Aug 25, 2012

-----------------------------------------------------------------

Total CT/CH Hours Balance: 62.250

PAID,EMPLOYEE A Leave Group: 3 nnn-nn-nnnn

\*The CT/CH balance of 22.750 hours earned between 11-05 and 11-17 will be

itemized in the report at least 8 pay periods in advance.

Restored Leave: 24.000

Use by end of leave year 2012 or forfeit.

Military Leave in hours: 8.00

END OF REPORT

Figure : Modified screen.

## Changes to the Supervisory Approvals Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this patch is installed, VistA PAID/ETA uses the sum of the balances from the preceding eight pay periods to calculate employees’ total available comp time/credit hours balances. However, employees may have balances in more than eight individual pay periods, possibly as many as 26 pay periods. In these cases, employees’ comp time/credit hours balances are understated on the Supervisor report.

After the patch is installed, the Supervisory Approvals \[PRSA SUP CERT\] option displays the correct comp time/credit hours balance from the COMPTIME/CREDIT HRS BALANCE field (#496) in the PAID EMPLOYEE file (450). This field contains the unused balance of all comp time/credit hours earned over the preceding 26 pay periods.

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing the patch will be supported by the Product Development team which performed the development. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any patch-related issues. At the end of this 30 day period, assistance with patch-related issues will be addressed through the Help Desk and Remedy tickets if needed.