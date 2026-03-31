---
title: PAID Version 4 Release Notes
doc_type: RN
doc_label: Release Notes
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
menu_options: 0
description: The following enhancements were made to this version of Time and Attendance, Personnel and Accounting Integrated Data (PAID). There were no new enhancements to the Education Tracking portion.
audience: 
keywords: 
  - leave
  - employee
  - date
  - report
  - period
  - requests
  - payroll
  - employees
  - shows
  - selected
page_count: 0
word_count: 1705
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Decentralized Hospital Computer Program

PERSONNEL AND ACCOUNTINGINTEGRATED DATA(PAID)RELEASE NOTES

August 1995

Hines IRM Field Office

Hines, Illinois

Release Notes

The following enhancements were made to this version of Time and Attendance, Personnel and Accounting Integrated Data (PAID). There were no new enhancements to the Education Tracking portion.

Employee: 1. Leave Request:

a\. When entering leave requests, the employee must enter the estimated Number of Hours (number of days if leave is accrued in days) that the leave request covers. This value is no longer calculated for the user. If the employee bypasses the Number of Hours prompt, a message is displayed:

THE DATA COULD NOT BE FILED.

Page 1, ESTIMATED HOURS/DAYS is a required field

b\. When entering a leave request, a projected leave balance is calculated in the background. If the calculation returns a negative value, then the employee is warned with this message:

> **WARNING:** Your Leave Balance MAY go below zero!

c\. Three new types of leave were added for selection:

CB Family Care and Bereavement

AD Adoption

DL Donor Leave

d\. On exiting the Leave Request option, the employee has the chance to enter another request without returning to the menu.

Do you wish to enter another Leave Request? No//

2\. Edit Leave Request: This is a new option in the Employee Menu. Any requests that have not been posted are available for selection to edit.

3\. Display Leave Requests: Cancelled leave requests were dropped from the display.

4\. Leave Balance: This option now shows the balance as of the date shown on the screen.

5\. Display Leave Used: This is a new report that prints, for a selected date range, all leave taken.

Timekeeper: 1. If a leave request is entered for a date that was already posted, a bulletin is sent to all timekeepers for the T&L of the employee.

(Employee) has requested (Type of Leave) beginning (Date). That date has already been posted.

2\. If an attempt is made to alter a record after approval but before transmission, the timekeeper is alerted to call payroll.

Card in Payroll and not transmitted; request return of card.

3\. Posting/Tour Change:

a\. Timekeepers must enter a comment whenever entering a Prior Pay Period Adjustment.

b\. The compressed/flexitime code is now displayed whenever a tour change is made and can be set as desired.

4\. Family Friendly leave is now supported using new Types of Time which can be directly posted: CB is used for Family Care and Bereavement, AD for Adoption, and DL for Donor Leave. Prior to this version, more than one time remark could not be entered. With direct posting of family friendly leave, appropriate time remarks such as printed on the SF71 can be used.

5\. Edit OT/CT Request: This new option allows the editing of OT/CT requests if not yet posted.

6\. LWOP is automated for any employees that are paid in days for LWOP surrounding a Holiday. For instance, if the employee is on leave without pay (LWOP) on Friday, the following Monday is a holiday, and the employee is on LWOP on Tuesday, the decomposition automatically charges LWOP to the weekend as well as the holiday. Similarly, if an employee is on LWOP on Thursday, Friday is a holiday, and the employee is on LWOP on the following Monday, the decomposition automatically charges LWOP for the holiday as well as the weekend.

T&A Supervisor: 1. Supervisory Approvals: When leave is approved by the supervisor, a projected leave balance is displayed. The projected leave balance is calculated by taking the balance from the last pay period, subtracting all leave requests from that date to the date of leave, and adding any increments which may accrue during that period. If the projected balance value is negative, the supervisor receives a message.

> **WARNING:** Approval MAY result in a negative leave balance.

2\. Supervisors see messages when they sign on showing how many actions in each T&L need to be approved.

T&L (unit) has (#) actions to certify.

3\. Pay Period Certification: Supervisors see a time decomposition when certifying timecards so that they know what types of time are being paid.

4\. List Prior Pay Period Exceptions: This option was added to the T&A Supervisor Menu. It allows a supervisor to list all exceptions from prior pay periods for a T&L.

5\. Employee Leave Balances: This option shows the balance as of the date shown on the screen.

6\. Employee Leave Pattern: This report shows all leave taken around scheduled off days by an employee for a selected date range. Supervisors can only see employees under T&Ls that are assigned to them.

7\. Employee Leave Requested: This report shows all future leave requested by one or all employees over a selected date range. Supervisors can only see employees under T&Ls that are assigned to them.

8\. Expenditures: This report shows all governmental cost for a selected T&L over one or all pay periods for a chosen year. Supervisors can only see employees under T&Ls that are assigned to them.

9\. Employee Overtime/CompTime Report: This report shows the overtime and compensation time taken by employees over one or all pay periods during a selected calendar year. Supervisors can only see employees under T&Ls that are assigned to them.

10\. Employee Prior Pay Period Adjustments: This report shows all audits for a selected T&L and date range. Supervisors can only see employees under T&Ls that are assigned to them.

11\. Employee Leave Used: This report prints all previous leave taken by employees for a selected T&L and date range. Users may only see employees under T&Ls assigned to them.

12\. Display OT/CT Requests: An estimated cost of OT, based upon the employee, is displayed in this option.

PDEMPLOYEE,ONE 000-00-0001

15-Jul-95 2 Hrs. OVERTIME (\$102.31) on T&L 102 Requested

PROJECT MUST BE COMPLETED BY MONDAY NEXT WEEK.

Overtime Approvers: 1. OT approvers receive messages when they sign on indicating that OT and/or Prior Pay Period Adjustments need approval.

PAID has (#) OT/CT/Prior Pay Period actions to approve.

2\. Supervisory Approvals: The OT approver can disapprove individual items while approving the remaining requests for a T&L.

3\. Display OT/CT Requests: This option shows all leave requests for each employee followed by an estimated grand total cost of overtime.

4\. Employee Leave Balances: This option shows the balance as of the date shown on the screen.

Payroll: 1. List Leave Requests and List OT/CT Requests: Two options were added to the Payroll Main Menu that allow payroll users to display leave and OT requests for a T&L.

2\. Clear Prior Pay Period Exceptions: This is a new option that allows Payroll to clear exceptions listed in File 458.5.

3\. Display Complete Request/Pay Period Records: This is a new menu that contains options which allow payroll to display all of the fields of Leave, OT/CT, Environmental Differential, and Pay Period records for an employee.

> a\. Display Leave Request: This option allows payroll to display all of the fields of a leave request.

> b\. Display OT/CT Request: This option allows payroll to display all of the fields of an OT/CT request showing exactly who approved certain actions and when they were approved.

> c\. Display Environmental Differential Request: This option allows payroll to display all of the fields of an Environmental differential Request.

> d\. Display Pay Period for Employee: This option allows payroll to display all of the fields of a pay period for an employee.

4\. Pay Plan C is now supported.

5\. Compressed/flexitime code is now a part of the 8B Stub record and is effective for that pay period.

6\. PAID T&L Report: This report displays or prints timekeepers, supervisors and their certifying T&L, and overtime supervisors.

7\. Expenditures: This report shows all governmental cost for a selected T&L over one or all pay periods for a chosen year.

8\. Employee Overtime/CompTime Report: This report shows the overtime and compensation time taken by employees over one or all pay periods during a selected calendar year.

9\. Employee Prior Pay Period Adjustments: This report shows all audits for a selected T&L and date range.

10\. Employee Leave Used: This report prints all previous leave taken by an employee over a selected date range.

Payroll Supervisor: 1. List Supervisors Certified by a T&L: This new option under the Payroll Supervisor Menu allows payroll to display all supervisors in other T&Ls which are approved by a selected T&L.

2\. Set Holiday Benefit Day: An enhancement to this option allows the payroll supervisor to set a benefit day for a past transmitted date.

3\. Automatic 8B Edit Checks: The 8B records are automatically subjected to edit checks prior to transmission. Any errors are displayed and the system asks if it should continue.

4\. Enter/Edit T&L System for T&L Unit: The T&L flag indicating which system is being used was eliminated and it is assumed that all T&Ls are being transmitted using the present enhanced system. This option was removed from the Payroll Supervisor Menu.

5\. Decomposition can now be done during a pay period without affecting the final decomp.

Human Resource: 1. Ad Hoc Report Generator: This option allows the HRM user to generate Ad Hoc reports using, 1) Basic Employee fields, 2) Title 38 Employee fields, 3) Physician & Dentist Fields, and 4) Followup Codes.

IRM: 1. Once your users no longer have any need for PAID V. 2.5 it may be de-installed by running the PRSIKIL routine. This routine will remove all PAID V. 2.5 files, routines, and options. Note: Please check with your payroll representative prior to running this routine.

2\. The decomposition logic now adds the compressed/flexitime code to the 8B STUB record. The decomposition gets the value from File 458 or, if that value is null, from the existing value in file ^PRSPC. It adds either a C, F, or space as the 32nd character position of the STUB record.

3\. New Person pointer in File 450: Field \#700 in the Paid Employee file has been changed from "OLD 450 IEN" to "NEW PERSON". This field will now be a pointer to the New Person file \#200. This field has been made uneditable by setting a 9 node in the DD equal to "^".

4\. PAID will no longer add new employees to the New Person file \#200. When a new employee is added to File 450, the "SSN" cross-reference in File 200 will be checked. If the SSN is found in File 200, the "NEW PERSON" pointer field in File 450 will be set to the IEN of the File 200 entry. If the SSN is not found in File 200, the following text will be appended to the "PAID statistics" message which is sent to the G.PAD mail group:

The following employees' SSNs could not be found in the NEW PERSON file.

They may need:

1\) To be added to the NEW PERSON file,

2\) To have their SSNs added to the NEW PERSON file or

3\) To have their SSNs corrected in the NEW PERSON file.

Please notify or forward this message to your IRM representative.

> In addition, PAID V. 4.0 contains a partial definition of the New Person file \#200. This partial definition will create a new field (PAID EMPLOYEE \#450) which is a pointer to the PAID Employee file \#450 and a new MUMPS cross-reference (AJ) on the SSN field \#9. These additions to the New Person file have been approved by the DBA and the Kernel developers.