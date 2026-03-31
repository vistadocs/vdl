---
title: PRS*4*132 Release Notes-Telework
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Telework
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4*132
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - telework
  - table
  - hours
  - contents
  - changes
  - timekeepers
  - paid
  - employee
  - scheduled
  - patch
page_count: 0
word_count: 1996
section_count: 13
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p132_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p132_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Upgrade ETA For Telework

Release Notes

![](prs-4-132-release-notes-telework/001.png)

Upgrade ETA for Telework  
Patch PRS\*4.0\*132

May 2012

Product Development (PD)

Revision History

<table>
<caption><p>Table 1:PAID Code Definitions</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 39%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1/15/2012</td>
<td>1.0</td>
<td>This first draft is based on the FORUM patch description and information from the ESE Testing Service Analysis Report for Increment 1. This covers Patch PRS*4.0*133.</td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>5/1/2012</td>
<td>1.1</td>
<td>This version is based on the FORUM patch description and information from the ESE Testing Service Analysis Report for Increment 2. This covers Patch PRS*4.0*132.</td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

Table 1:PAID Code Definitions

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Patch Nomenclature](#patch-nomenclature)
  - [Related Patches](#related-patches)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
- [Changes and Enhancements](#changes-and-enhancements)
  - [Changes to the Download Formats](#changes-to-the-download-formats)
  - [Changes to the Download Server](#changes-to-the-download-server)
  - [Changes to The PAID CODES File](#changes-to-the-paid-codes-file)
  - [Changes to the Payroll Functions](#changes-to-the-payroll-functions)
    - [PAID Codes](#paid-codes)
    - [Telework Status Code](#telework-status-code)
  - [Changes to the Timekeeper Functions](#changes-to-the-timekeeper-functions)
  - [Changes to the T&A Supervisor Functions](#changes-to-the-ta-supervisor-functions)
  - [Changes to the Employee Functions](#changes-to-the-employee-functions)
  - [Changes to the Time Card Decomposition Functions](#changes-to-the-time-card-decomposition-functions)
- [Support Information](#support-information)
This patch introduces changes to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software for the Upgrade ETA for Telework Project (Increment 2). These changes enable Veterans Affairs to report employee telework days/hours to Central PAID. This will enable VA to satisfy the requirements of the Presidential Mandate for reporting telework days/hours, to meet VA telework goals, and to enable reliable reporting for the OMB and OPM annual Telework Call for Data. Specifically, this patch introduces functionality updates to account for scheduled, unscheduled, and medical telework hours performed by VA employees.

## Patch Nomenclature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patch Name: PRS\*4.0\*132 (Upgrade PAID/ETA for Telework)
- Release Date: May 2012

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PRS\*4.0\*126 (PAID Enhancements for VANOD)

> NOTE: This patch must be installed before installing PRS\*4.0\*132

- Release Date: April 2012
- Summary: This patch implements new functionality within VistA PAID/ETA software version 4.0 to provide appropriate data to VANOD (Veterans Affairs Nursing Outcomes Database) in accordance with Public Law 107-135 and the OIG recommendation 4a (annual reporting requirement). The patch also includes minor modifications to existing ETA functionality to support the collection of data for the VANOD. Please refer to the FORUM patch description for more information.
- PRS\*4.0\*133 (Upgrade PAID/ETA for Comp Time)
  - Release Date: January 2012
  - Summary: This patch introduces the functionality changes that must be made to VistA PAID/ETA software version 4.0 to implement the expansion of Comp Time/Credit Hours expiration from eight pay periods to 26 pay periods. Please refer to the PRS\*4.0\*133 Release Notes or FORUM patch description for more information.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch revises an existing VistA PAID/ETA application. There are no new hardware compatibility requirements.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch revises an existing VistA PAID/ETA application. There are no new system specifications.

# Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch for Increment 2 includes changes and additions to VistA PAID/ETA functions, including:

1.  Download formats;
2.  The download server;
3.  The PAID CODES file;
4.  Payroll functionality;
5.  Timekeeper functionality;
6.  T&A Supervisor functionality;
7.  Employee functionality; and
8.  Time Card Decomposition functionality.

## Changes to the Download Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following download formats are updated to receive an indicator from AITC that identifies employee telework status:

1.  Initial
9.  Edit and Update

## Changes to the Download Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA PAID ETA download server is updated to store the telework indicator with the employee's record in the PAID EMPLOYEE file (#450).

## Changes to The PAID CODES File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PAID CODES file (#454) is updated to include an entry for the new telework code set as defined in Table 1.

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

Table 2: Decomposing Time Cards

## Changes to the Payroll Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PAID Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update PAID Codes \[PRSD UPDATE PAID CODES\] option is updated to enable Payroll staff to review the new telework PAID codes and their definitions.

### Telework Status Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are updated so Payroll staff can view employees’ telework status codes:

1.  Employee Inquiry \[PRSD 04 EMPLOYEE INQUIRY\]
10. Search Employee Entries \[PRSD 04 SEARCH EMPLOYEE FILES\]
11. Print Employee Entries \[PRSD 04 PRINT EMPLOYEE FILES\]

The List/Clear Prior Pay Period Corrections \[PRSA PAY PPC\] option is updated to enable Payroll staff to view, when viewing previously entered pay period corrections, the:

- telework tour of duty corrections;
- telework hours; and
- telework type.

## Changes to the Timekeeper Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Employee Tour of Duty \[PRSA TK TOUR-EDIT\] option is updated to enable:

1)  Timekeepers to view the Telework Indicator status code when using the screen mode.
2)  Timekeepers to enter, update, and delete tour of duty days as either (i) scheduled telework or (ii) medical telework when in screen mode.
3)  Timekeepers to enter (i) scheduled telework or (ii) medical telework for only those employees who are eligible for telework. (Eligibility for telework is established by the telework indicator in the PAID Employee file (#450).)
4)  For employees on a fixed Monday through Friday tour, timekeepers can enter screen mode and mark employees' tour of duty days as either
1)  scheduled telework or
2)  medical telework.

The Display Posted Data \[PRSA TPD\] option is updated to enable:

1)  Timekeepers to view the Telework Indicator status code.
2)  Timekeepers to view the scheduled telework (regular or medical).
3)  Timekeepers to view the actual telework hours poste(d).

The Display Employee Tour of Duty \[PRSA TK TOUR-DISP\] option is updated:

1)  Timekeepers can view the Telework Indicator status code.
2)  Timekeepers can view the scheduled telework (regular or medical).

The Post Employee Time \[PRSA TK POST\] option is updated:

1)  Timekeepers can enter the actual telework hours for eligible employees after posting employee time and leave data.
2)  Timekeepers can indicate whether telework hours are
1)  scheduled telework,
2)  medical telework, or
3)  ad hoc telework.
3)  Timekeepers can enter actual telework hours for each type of telework for a single day or tour of duty. For example, consider an eight hour scheduled telework tour with two hours of overtime. The timekeeper can enter eight hours scheduled telework and two hours of ad hoc telework, if applicable.
4)  Timekeepers are prompted to enter telework hours for only those employees who are eligible for telework based on the Telework Indicator in their PAID Employee file (#450). Eligible employees must have an eligible Telework Indicator status code in order to have telework hours posted to their timecard. (Telework Indicator status codes are listd in Table 1.)
5)  For scheduled teleworkers (regular or medical), timekeepers are provided with a default value for employees' scheduled telework hours (Equation 1).

Default scheduled telework hours (medical or regular) =  
( length of the tour ) - ( leave )

Equation 1: Default Scheduled Telework Hours

6)  For scheduled teleworkers, timekeepers can enter telework hours (ad hoc or medical) for any work hours posted outside the tour of duty.
7)  For unscheduled teleworkers, timekeepers are provided with a default value for employees' telework hours (Equation 2).

Default total telework hours =  
( length of the tour ) + ( overtime /comp time) - ( leave )

Equation 2: Default Total Telework Hours

8)  For unscheduled teleworkers, timekeepers can enter the type of telework (ad hoc or medical).
9)  Timekeepers are restricted to a value between zero hours and the default telework hours value defined in Equation 1 or Equation 2.
10) Full Time Physicians: Full time physicians work daily tours. They work the entire day or take leave for the entire day.
1)  Timekeepers can enter a day as telework days; and
2)  Timekeepers can enter telework as either scheduled telework, medical telework, or ad hoc telework.
11) There is no provision for timekeepers to provide a scheduled telework on secondary tours. Timekeepers can enter actual telework hours (medical or ad hoc) if they are applicable to secondary tours.
12) Intermittent Employees currently have no specified tour of duty. There is no provision for timekeepers to schedule telework hours for intermittent employees. Timekeepers can enter actual telework hours (medical or ad hoc) for intermittent employees.

The Posting/Tour Change \[PRSA TP POST\] option is updated for employees who are eligible for telework:

1)  Timekeepers can add or remove scheduled telework days, as shown in Table 1, when entering corrections to employees' tours of duty.
2)  Timekeepers can add, update, edit, and delete telework hours from daily time records when entering time posting corrections. (Timekeepers are limited to entering telework hours based on the same criteria described with the Post Employee Time option.)
3)  Timekeepers can edit the telework type (scheduled telework, medical telework, or ad hoc telework) when entering time posting corrections, also based on criteria described with the Post Employee Time option.

## Changes to the T&A Supervisor Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pay Period Certification \[PRSA SUP REV\] option is updated:

1)  Supervisors can view scheduled telework (regular or medical) and actual telework hours posted for each day of the pay period from within the existing Pay Period Certification option.
2)  Supervisors can view telework hours on the existing PAY PERIOD summary screen.

> **NOTE:** The certification option generates the 8B string in the background when a supervisor releases a timecard to payroll. The requirements for the 8B string are covered in a separate section.

The Supervisory Approvals \[PRSA SUP CERT\] option is updated:

1)  Supervisors can review and then approve, disapprove, or bypass changes to scheduled telework (regular or medical).
2)  Supervisors can review and then approve, disapprove, or bypass changes to telework hours posted for each day of the pay period from within the existing supervisory approval option.

The Display Employee Tour of Duty \[PRSA TK TOUR-DISP-SUP\] option is updated:

1)  Supervisors can view scheduled telework (medical or regular) within this option.

The Display Employee Pay Period \[PRSA TPD PP-SUP\] option is updated:

1)  Supervisors can view scheduled telework (medical or regular) on this report.
2)  Supervisors can view the posted telework hours on this report.

## Changes to the Employee Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Service Record Screen \[PRSD SERVICE RECORD SCREEN\] option is updated so employees can view their Telework Indicator status code (Table 1).

The Display Pay Period \[PRSA TPD PP-EMP\] option is updated:

1)  Employees can view their scheduled telework (medical or regular) on this report.
2)  Employees can view their posted telework hours on this report.

## Changes to the Time Card Decomposition Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Time cards can be decomposed using the options shown in Table 2.

| Option Text          | Option Name            | Associated Menu |
|--------------------------|----------------------------|---------------------|
| Pay Period Certification | \[PRSA SUP REV\]           | Supervisor          |
| Decompose Time           | \[PRSA PAY DECOMP\]        | Locally assigned    |
| T&L Decomposition Report | \[PRSA T&L DECOMP REPORT\] | Locally assigned    |

Table 3: 8B String Codes

The 8B string decomposition software is updated to report telework hours in the 8B string using the format CCNNX where CC is the two character 8B code, NN is the total number of whole hours in the week, and X represents the remaining quarter hours (0, 1, 2, or 3).

The new 8B codes are shown in Table 3.

| Code | Explanation                   |
|----------|-----------------------------------|
| TW       | Scheduled Telework Hours Week 1   |
| TX       | Scheduled Telework Hours Week 2   |
| TS       | Situational Telework Hours Week 1 |
| TT       | Situational Telework Hours Week 2 |
| TM       | Medical Telework Hours Week 1     |
| TN       | Medical Telework Hours Week 2     |

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing the patch will be supported by the Product Development team which performed the development. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any patch-related issues. At the end of this 30 day period, assistance with patch-related issues will be addressed through the Help Desk and Remedy tickets if needed.