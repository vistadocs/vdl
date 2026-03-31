---
title: PRS*4*133 Release Notes - Comp Time
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Comp Time
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4*133
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - hours
  - time
  - comp
  - credit
  - patch
  - table
  - contents
  - periods
  - balance
  - paid
page_count: 0
word_count: 1488
section_count: 8
table_count: 0
figure_count: 3
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p133_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p133_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Upgrade ETA For Telework

Release Notes

![](prs-4-133-release-notes-comp-time/001.png)

Upgrade ETA for Telework  
Patch PRS\*4.0\*133

March 2012

Product Development (PD)

Revision History

<table>
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
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

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
  - [Changes to the Pay Period Display](#changes-to-the-pay-period-display)
  - [Changes to the Comp Time/Credit Hours Balance Display](#changes-to-the-comp-timecredit-hours-balance-display)
  - [Changes to the Supervisory Approvals Function](#changes-to-the-supervisory-approvals-function)
- [Support Information](#support-information)
This patch introduces changes to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software for the Upgrade ETA for Telework Project (Increment 1). These changes revise the expiration of compensatory (“comp”) time and credit hours from eight to 26 pay periods. The changes also enable VA to report employee telework days/hours to Central PAID. This will enable VA to satisfy the requirements of the Presidential Mandate for reporting telework days/hours, to meet VA telework goals, and to enable reliable reporting for the OMB and OPM annual Telework Call for Data. Additionally, the patch will enable employees to view their comp time/credit hours balances for the preceding 26 pay periods.
Currently VistA PAID ETA receives up to eight individual pay period comp time/credit hours balances from AITC, and calculates an expiration date based on seven pay periods. After this patch is implemented, VistA PAID ETA will display a subtotal of comp time/credit hours earned over the past 26 pay periods. In cases where comp time/credit hours were earned during the interval of the preceding nine to 26 pay periods, VistA PAID ETA will report the actual hours and expiration for each of the oldest eight pay periods, with the remaining balances from the ninth through the most recently earned as a subtotal. The patch also enables supervisors to view comp time/credit hours balances for their direct reports.

## Patch Nomenclature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Release Date: March 2012
- Patch Name: PRS\*4.0\*133
- Summary: This patch introduces the functionality changes that must be made to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software to implement the expansion of Comp Time/Credit Hours expiration from 8 pay periods to 26 pay periods. Please refer to the PRS\*4.0\*133Release Notes for more information.

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <span id="_Toc317154801" class="anchor"></span>Release Date: August 2012
- Patch Name: PRS\*4.0\*132

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

Figure 1: VistA PAID/ETA report options modified by this patch.

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

Figure 2: Original screen.

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

Figure 3: Modified screen.

## Changes to the Supervisory Approvals Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this patch is installed, VistA PAID/ETA uses the sum of the balances from the preceding eight pay periods to calculate employees’ total available comp time/credit hours balances. However, employees may have balances in more than eight individual pay periods, possibly as many as 26 pay periods. In these cases, employees’ comp time/credit hours balances are understated on the Supervisor report.

After the patch is installed, the Supervisory Approvals \[PRSA SUP CERT\] option displays the correct comp time/credit hours balance from the COMPTIME/CREDIT HRS BALANCE field (#496) in the PAID EMPLOYEE file (450). This field contains the unused balance of all comp time/credit hours earned over the preceding 26 pay periods.

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing the patch will be supported by the Product Development team which performed the development. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any patch-related issues. At the end of this 30 day period, assistance with patch-related issues will be addressed through the Help Desk and Remedy tickets if needed.