---
title: PAID Version 4 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
security_keys: 
  - PRSA SIGN
  - PRSD PAID CODES
  - PRSE CORD
  - PRSE SUP
  - PRSE TRAIN
menu_options: 0
description: This manual is designed as a reference guide primarily for all programmers and Information Resources Management (IRM) technical personnel who will be supporting the Decentralized Hospital Computer Program's (DHCP) Personnel and Accounting Integrated Data (PAID) package. This manual provides programm
audience: 
keywords: 
  - class
  - employee
  - prsa
  - time
  - even
  - prse
  - routine
  - tour
  - leave
  - paid
page_count: 0
word_count: 18162
section_count: 1
table_count: 100
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1995
revision_count: 3
revision_newest: 3/8/2018
revision_oldest: 12/29/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Decentralized Hospital Computer Program

PERSONNEL AND ACCOUNTING INTEGRATED DATA(PAID)TECHNICAL MANUAL

August 1995

Hines IRM Field Office

Hines, Illinois

Preface

This manual is designed as a reference guide primarily for all programmers and Information Resources Management (IRM) technical personnel who will be supporting the Decentralized Hospital Computer Program's (DHCP) Personnel and Accounting Integrated Data (PAID) package. This manual provides programmers with the information necessary to support, troubleshoot and maintain the PAID software.

The PAID software has three major modules: Time and Attendance (T&A), Employee Master Record Downloads, and Education Tracking.

The scope of the T&A portion of the software has greatly increased with each succeeding version. All information is entered via a terminal for electronic storage and processing -- information that was previously "posted" on a paper time and attendance report. A series of computer routines will apply time and leave processing rules to the data entered and calculate the totals for the various hours worked and leave taken. The software will create the necessary 8B record for transmission to the Austin Automation Center (AAC).

The purpose of the T&A portion of the software is to create a paperless time and attendance system.

The target audience, in addition to timekeepers, includes Time and Leave Unit (T&L) supervisors who approve time and attendance reports, schedule or approve overtime and compensatory time (OT/CT), and approve leave requests for their T&Ls. Also, employees will be able to view their own leave balances and make electronic requests for leave (SF 71 - APPLICATION FOR LEAVE).

A secondary scope to the package: the establishment of a continuously updated employee master record database remains the same. Employee master record data from the AAC will be stored at the station and updated regularly whenever a change is made to an employee record via the AAC's On Line Data Entry (OLDE) system.

Payroll and Personnel users are the target audience for this functionality. They will be able to view, but not change this data in the DHCP system.

The purpose of the database is twofold. First, an accurate employee master record database at the station will eliminate, in a future version, the need for a biweekly 8B data download. Second, it gives the Payroll and Personnel users an employee database to aid them in their tasks.

It is important to note that Personnel users will not have access to T&A options and will not be able to alter any time and attendance report data. Also, timekeepers will not have access to employee master record data except leave balances of employees in the time and leave units that they have been assigned.

Table of Contents

Introduction

Implementation and Maintenance

Routine Descriptions

File List

Exported Options

Cross References

File Diagram (PRS)

Archiving and Purging

Callable Routines

External Relations

Internal Relations

Package-wide Variables

How to Generate On-line Documentation

National Package Security

Glossary

Revision History

Initiated on 12/29/04

|          |                                                                                                                                                        |                 |                  |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------|
| Date     | Description (Patch \# if applic.)                                                                                                                      | Project Manager | Technical Writer |
| 12/29/04 | Updated to comply with SOP 192-352 Displaying Sensitive Data.                                                                                          |                 | REDACTED         |
| 12/29/04 | Pdf file checked for accessibility to readers with disabilities.                                                                                       |                 | REDACTED         |
| 3/8/2018 | Updated as part of changes for patch PRS\*4.0\*154, PAID Expenditures Report not working after VATAS. This includes fixing a typo on page [41](#typo). | REDACTED        | REDACTED         |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |
|          |                                                                                                                                                        |                 |                  |

Introduction

This package has three main functions. The primary function is the collection and transmission of Time and Attendance (T&A) Report data. The purpose of this function is to provide an electronic means by which biweekly payroll data can be collected, processed and transmitted to the Department of Veterans Affairs' Austin Automation Center (AAC) in Austin, Texas, for the generation of personnel payroll checks. The users accomplish their tasks with seven menus: Payroll Supervisor Menu, Payroll Main Menu, Timekeeper Main Menu, T&A Supervisor Menu, T&A OT/Supervisor Menu, Employee Inquiry/Reports Menu and Employee Menu. These menus are assigned to authorized users who are responsible for entering, processing or transmitting time and attendance report data to the AAC.

The secondary function is to receive and store employee master record data. The purpose of this function is to create an employee database which will be available to Payroll and Personnel users for viewing and local reporting needs. A regularly updated employee database will be used to create a paperless time and attendance report "stub" record (i.e., the first 32 characters of an 8B record). The users may view the employee master record data by means of two menus; the Employee Inquiry Menu (sub-menu) designed for Payroll users and the Employee Inquiry Reports/Menu designed for Personnel users.

The third function is a module that creates an Education Tracking database featuring programs or classes with multiple attendees and reasons for attending these programs or classes.

This database is made up of each individual employee's program or class attended and all associated data including: program or class name and supplier, type of media used for presentation, agency to place where employee or student is from, purpose of the training, a category or name for a desired grouping of program or classes, type of training (mandatory inservice, continuing education or other training), mandatory review group (if a required class), financial agency and cost (if government funded), accreditation board (if continuing education) and employee or student expense (if any or all funding is provided by the employee or student).

The AAC sends employee master record data to the station where it will be stored and updated regularly. The AAC will generate five types of employee data downloads. They are: Initial, Edit and Update, Payrun, Transfer, and Separation. This data will be transmitted through MailMan to the station where it will be stored in the PAID EMPLOYEE (#450) and/or PAID PAYRUN DATA (#459) file. Payroll users will be able to view payroll-related data in these two files. Personnel users will be able to look at personnel-related data in the PAID EMPLOYEE file, only.

In previous versions, an initial download containing the master records for all of the employees at the station arrived first to populate the PAID EMPLOYEE file. This download should occur only once, but may be sent again. Contact the PAID Development staff at the Hines ISC to request a transmission of an Initial download. An Edit and Update download is generated daily to modify employee master record data that has changed in the PAID EMPLOYEE file (e.g., promotions). A Payrun download is generated once per pay period and contains data which changes each pay period (e.g., year-to-date earnings). The PAID EMPLOYEE and PAID PAYRUN DATA files are modified with this download. A Transfer download is generated at the same time as the Payrun download and contains master record data of employees who are transferring into the station. A Separation download is generated at the same time as the Payrun download. A separated employee's master record is not deleted. Instead, the SEPARATION IND field (File 450, field \#80) in that record is set to the letter Y to indicate the employee is separated.

A prior version of this package eliminated the need to keypunch 8B records (VA Form 4-213) at VA facilities. Throughout this manual, there are references made to the processing of 8B records in relation to the T&A program. It should be noted, however, that there is not a physical 8B record. The term "8B record" has been used because it is a term familiar to Payroll users.

Implementation and Maintenance

There are no site-specific parameters for this package.

The Fiscal Service, Payroll Section Supervisor will decide who the users of the T&A options will be and the Site Manager will assign ACCESS and VERIFY codes for each user.

The T&A portion of the software recognizes six classes of users - Payroll Supervisor, Payroll Clerks, Timekeepers, Time and Leave Unit (T&L) Supervisors, Overtime Approvers and all other employees. Each class has its own main menu. A user's class is determined by the menu that is assigned. The Payroll Supervisor should instruct the Site Manager what T&A menu is assigned to a user.

Users of the T&A menus must have a value in the SSN field (#9) in the NEW PERSON file (#200) and that value must match the SSN value of an entry in the PAID EMPLOYEE file (#450) or the user cannot proceed any further.

In a previous version, only timekeepers were associated with a T&L in the T&L UNIT file (#455.5). The TIMEKEEPER field (#10) is a multiple that points to File 200. A SUPERVISOR field (#11) has been added to associate supervisors to a T&L and an OT/CT APPROVER field (#12) was added to associate approving officials for overtime and compensatory time to a T&L. Both of these fields are multiple entry type fields that point to File 200.

It is recommended that the MailMan messages generated for transmission to the AAC be saved in some MailMan basket for at least six months as a record of your actual transmission.

# Failsoft Procedures


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Failsoft Procedures](#failsoft-procedures)
- [Exemptions](#exemptions)
- [Options Not Assigned to Any Menu](#options-not-assigned-to-any-menu)
- [Security Keys](#security-keys)
- [Privacy Act Statement](#privacy-act-statement)
- [Additional Data Field Security for File 450](#additional-data-field-security-for-file-450)
- [Electronic Signatures](#electronic-signatures)
A double transmission of 8B messages can have dire consequences since AAC will 'add' the two records together and then reject them both. Therefore, careful checks should be made to ensure that only a single initial transmission takes place. It is conceivable that due to a global translation error, or corruption of the MailMan global, or for other reasons, it is desirable to re-build the MailMan messages. This is a dangerous operation unless one is assured that the original messages have not and will not be transmitted.
In the case of a disk or CPU failure, existing Failsoft procedures should be adequate. Recovery from a disk failure rarely takes more than two hours. In the case of a CPU failure, either repair of the CPU or movement to a different processor is generally accomplished in four hours or less.
A more serious problem can be the failure of the network system or the local mini-engine when repair times are uncertain. In order to deal with these contingencies, a routine exists which will produce a magnetic tape of the 8B records (actually, any device can be selected, but use of a magnetic tape is assumed). This routine does NOT reset the transmission flag (i.e., it does not mark the individual records as transmitted). Thus, use of the routine to prepare a tape does not preclude normal transmission should repairs be accomplished more quickly than expected.
To build a tape containing all 8B records:
D TAPE^PRSATAPE
Select Time & Attendance Records Pay Period: 93-01// \<RET\>
Select TAPE Device: enter a device name here
To read a tape containing 8B records and produce MailMan messages for transmission:
D MAIL^PRSATAPE
Select TAPE Device: enter a device name here
This entry point is used when a nearby station produces a tape and wishes to use your facility for transmission. Use of this option in no way affects your own database.

# Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changing DUZ(0):

Options 1 and 2 on the PRSD 04 EMPLOYEE INQUIRY MENU AND PRSD 05 EMPLOYEE INQUIRY MENU allow the user to create reports with FileMan's print and search options. The variable DUZ(0) is changed to the letters P, F or

PF and acts as a screen to control the fields a user may see.

Routine Descriptions

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 44%" />
</colgroup>
<tbody>
<tr class="odd">
<td>PRS8</td>
<td>Starts the time and attendance decomposition process.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8AC</td>
<td>Creates the DAY (DAY,"W") node. This node contains for each day of the pay period the activities concerning an employee's schedule.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8CR</td>
<td>Takes the information contained in the WK array and creates the 8B record that is transmitted to the AAC.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8CV</td>
<td>Called at the end of the time and attendance report decomposition process to clean up all remaining variables.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8DR</td>
<td>Determines whether or not the parameters necessary to decompose time are in existence.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8EX</td>
<td>Processes the 1 node of File 458 for each day. This node contains the exceptions to normal work hours.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8EX0</td>
<td>Decomposition, exceptions (continued).</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8HD</td>
<td>Determines when the holidays occur within a year.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8HR</td>
<td>Determines what type of hours, other than normal hours, were worked.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8MISC</td>
<td>Makes miscellaneous adjustments to the 8B character string sent to Austin.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8MSC0</td>
<td>Miscellaneous adjustments to the time and attendance report (continued).</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8MT</td>
<td>Determines mealtime for purposes of reducing premium pay.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8OC</td>
<td>Credits the appropriate time and attendance report categories for work performed while On-Call.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8OT</td>
<td>Determines whether overtime/compensatory time (OT/CT) was scheduled in advance of the work week for the date being processed.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8PP</td>
<td>Determines certain premium pays for an employee.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8SB</td>
<td>Computes Stand-By hours.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8ST</td>
<td>Breaks down the timeframes into 15 minute increments and then starts the processing of those increments.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8SU</td>
<td>Defines the DAY array in the ^TMP global along with other associated variables pertaining specifically to the employee and pay period being processed.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8TL</td>
<td>Decomposes time and attendance information for a specific T&amp;L and for a specific pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8TL1</td>
<td>Continuation of PRS8TL.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8UP</td>
<td>Collects time and attendance information related to weekly activity which is unrelated to actual time.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8UT</td>
<td>Utility functions associated with the decomposition process such as device selection.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8VW</td>
<td>Displays the results of the decomposition process.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8VW1</td>
<td>Continuation of PRS8VW.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8VW2</td>
<td>Continuation of PRS8VW.</td>
<td></td>
</tr>
<tr class="even">
<td>PRS8WE</td>
<td>Determines weekend (Saturday and Sunday) premium pay.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRS8WE2</td>
<td>Premium pay utilities.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSACED</td>
<td>Starts the 8B record edit checks process.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSACED1</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSACED2</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSACED3</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSACED4</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSACED5</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSACED6</td>
<td>Continuation of edit checks.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSADP</td>
<td>Displays the posted time and attendance information for an employee on a selected date.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSADP1</td>
<td>Continuation of PRSADP.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSADP2</td>
<td>Displays posted time and attendance information for an employee for the pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSADPA</td>
<td>Display complete data for Payroll.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAEDL</td>
<td>Lists environmental differential pay requests.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAEDR</td>
<td>Creates or cancels a request for environmental differential pay.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAEDS</td>
<td>Displays an environmental differential request.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAENE</td>
<td>Displays pay and leave entitlement eligibility for an employee.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAENT</td>
<td>Determines which pay entitlement string applies to an employee.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAENX</td>
<td>Displays the values of an entitlement table entry (File 457.5).</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAES</td>
<td>Prompts the user for an electronic signature code.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSALVB</td>
<td>Displays an employee's leave balances.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSALVE</td>
<td>Edit a leave request.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSALVL</td>
<td>Lists leave requests by date or employee.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSALVR</td>
<td>Creates a leave request.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSALVS</td>
<td>Displays leave requests.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSALVT</td>
<td>Calculates projected leave balances.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSALVU</td>
<td>Calculates leave lengths.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSALVX</td>
<td>Cancels a leave request.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAOTE</td>
<td>Edit an OT/CT request.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAOTL</td>
<td>Lists OT/CT requests.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAOTR</td>
<td>Creates OT/CT requests.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAOTS</td>
<td>Displays OT/CT requests by date.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAOTX</td>
<td>Approves OT/CT requests.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPAS</td>
<td>Displays the Privacy Act Statement at the top of a menu.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPEH</td>
<td>Allows timekeeper to set employee's holiday.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPEM</td>
<td>Allows time and attendance posting other than time and leave data such as LUMP SUM UNITS.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPEX</td>
<td>List pay period exceptions.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPPH</td>
<td>Utility subroutines for holidays.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPPO</td>
<td>Creates the next pay period entry in the TIME &amp; ATTENDANCE RECORDS file (#458).</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPPP</td>
<td>Processes time and attendance report from a prior pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPPQ</td>
<td>Displays time and attendance report data for prior pay periods.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPPU</td>
<td>Calculates all 14 dates within a pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPPX</td>
<td>Approves prior pay period changes.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPRE</td>
<td>Create a time and attendance report entry in the TIME &amp; ATTENDANCE RECORDS file (#458) for an employee for a pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAPRT</td>
<td>Returns a time and attendance report to the timekeeper.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAPT1</td>
<td>Displays the SPECIAL TOUR INDICATOR (#457.2), TYPE OF TIME (#457.3), and TIME REMARKS (#457.4) file entries.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSARPT2</td>
<td>Displays a list of time and attendance reports not yet reviewed by Payroll Section.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSASAL</td>
<td>Supervisor Alert utilities.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSASC</td>
<td>Supervisor certification of leave requests, OT/CT requests, environmental differential pay requests, tour changes, and prior pay period changes.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSASC1</td>
<td>Files supervisor approvals for leave requests, OT/CT requests, environmental differential pay request and tour changes.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSASC2</td>
<td>Posts environmental differential pay.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSASC3</td>
<td>Approves prior pay period actions.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSASR</td>
<td>Allows supervisor to certify time and attendance reports.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSASR1</td>
<td>Displays posted Veterans Canteen Service (VCS) commission sales and environmental differential pay.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSASU</td>
<td>Supervisor un-reviewed list.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATAPE</td>
<td>Failsafe program used to make a tape of 8B records which can be taken to another site for transmission to the AAC.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATD1</td>
<td>Create, display or edit a TOUR OF DUTY file (#457.1) entry.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATD2</td>
<td>List tours of duty a T&amp;L is permitted to use.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATE</td>
<td>Allows a timekeeper to enter or edit an approved tour of duty on an employee.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATE0</td>
<td>Edits tours of duty.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATE1</td>
<td>Displays changes in a tour of duty.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATE2</td>
<td>Displays an employee's tour(s) of duty.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATE3</td>
<td>Displays more detailed information on an employee's tour(s) of duty.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATE4</td>
<td>Allows the entry of a second tour of duty on the same day for an employee.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATE5</td>
<td>Checks to make sure that two tours of duty on the same day do not overlap.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATEV</td>
<td>Verifies tour of duty.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATH</td>
<td>Displays a transmission report of 8B records sent to the AAC for a pay period.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATIM</td>
<td>Converts am and pm hours into 24-hour format.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATL</td>
<td>Display and edit of T&amp;L UNIT file (#455.5) entries.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATP</td>
<td>Allows a timekeeper to post time and attendance report data on an employee.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATP0</td>
<td>Allows a timekeeper to post an employee as being absent.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATP1</td>
<td>Checks for errors in posted entry.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATP2</td>
<td>Checks for OT/CT and leave for a posted entry.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATPD</td>
<td>Lets Payroll clear prior pay period exceptions.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATPE</td>
<td>Checks for exceptions to posted time.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATPF</td>
<td>Stores prior pay period exceptions in the PRIOR PAY PERIOD EXCEPTIONS (#458.5) file.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATPG</td>
<td>Lists prior pay period exceptions to a time and attendance report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATPH</td>
<td>Exception utilities.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATPL</td>
<td>Displays tours of duty and exceptions for employees.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATPP</td>
<td>Allows timekeeper to post time to a prior pay period.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSATPX</td>
<td>Lists pay period exceptions.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSATVC</td>
<td>Post VCS commission sales.</td>
<td></td>
</tr>
<tr class="even">
<td><p>PRSAUD</p>
<p>PRSAUDP</p></td>
<td><p>Creates an audit record when a time and attendance report entry is changed.</p>
<p>Display employee pay period audit data.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAUTL</td>
<td>Checks user's SSN for a match between PAID EMPLOYEE (#450) and NEW PERSON (#200) files. Checks user's access to a T&amp;L Unit. Sets up TaskMan variables and calls TaskMan to queue tasks.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSAXMIT</td>
<td>Loads 8B records into mail messages and transmits to the AAC.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSAXSR</td>
<td>Creates the "stub" of an 8B record (i.e., the first 31 characters) that is transmitted to the AAC.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSD1150</td>
<td>Record of leave data.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSD450</td>
<td>Update pointers on SSN change.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDADD</td>
<td>Add new employees.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDAH</td>
<td>Ad Hoc Reports driver.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDAH1</td>
<td>Ad Hoc basic employee fields.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDAH2</td>
<td>Ad Hoc Title 38 fields.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDAH3</td>
<td>Ad Hoc Physician &amp; Dentist fields.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDAH4</td>
<td>Ad Hoc Report interface to 450.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDCOMP</td>
<td>Sums various earnings, benefits and leave values and stores those totals in the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDDL</td>
<td>Processes the Separation download.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDENG</td>
<td>Engineering API.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDERR</td>
<td>Checks for errors when a data download is processed.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU01</td>
<td>A table used to process the first line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU02</td>
<td>A table used to process the second line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU03</td>
<td>A table used to process the third line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU04</td>
<td>A table used to process the fourth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU05</td>
<td>A table used to process the fifth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU06</td>
<td>A table used to process the sixth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU07</td>
<td>A table used to process the seventh line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU08</td>
<td>A table used to process the eighth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU09</td>
<td>A table used to process the ninth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU10</td>
<td>A table used to process the tenth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDEU11</td>
<td>A table used to process the eleventh line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDEU12</td>
<td>A table used to process the twelfth line of the Edit and Update record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDFIL</td>
<td>Used to maintain the PAID CODE FILE (#454). Users may enter PAID codes and their descriptions.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDFOLL</td>
<td>Puts the Followup Date for a particular Followup Code into the correct field.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD01</td>
<td>A table used to process the first line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD02</td>
<td>A table used to process the second line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD03</td>
<td>A table used to process the third line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD04</td>
<td>A table used to process the fourth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD05</td>
<td>A table used to process the fifth line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD06</td>
<td>A table used to process the sixth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD07</td>
<td>A table used to process the seventh line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD08</td>
<td>A table used to process the eighth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD09</td>
<td>A table used to process the ninth line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD10</td>
<td>A table used to process the tenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD11</td>
<td>A table used to process the eleventh line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD12</td>
<td>A table used to process the twelfth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD13</td>
<td>A table used to process the thirteenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD14</td>
<td>A table used to process the fourteenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD15</td>
<td>A table used to process the fifteenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDLD16</td>
<td>A table used to process the sixteenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDLD17</td>
<td>A table used to process the seventeenth line of the Initial record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDMISC</td>
<td>Miscellaneous subroutines.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPR01</td>
<td>A table used to process the first line of the Payrun record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPR02</td>
<td>A table used to process the second line of the Payrun record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPR03</td>
<td>A table used to process the third line of the Payrun record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPR04</td>
<td>A table used to process the fourth line of the Payrun record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPR05</td>
<td>A table used to process the fifth line of the Payrun record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPR06</td>
<td>A table used to process the sixth line of the Payrun record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPR07</td>
<td>A table used to process the seventh line of the Payrun record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPR08</td>
<td>A table used to process the eighth line of the Payrun record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPRIN</td>
<td>A table used to clean out the old accounting data values from the PAID EMPLOYEE (#450) file before entering the new values which come with every Payrun download.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPRNT</td>
<td>Allows the users of the Fiscal or Personnel Employee Inquiry Menus to call VA FileMan's Print and Search options to query the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDPROC</td>
<td>Checks the PRS global at system startup time and processes any records that are in it.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDPTYP</td>
<td>Creates an entry for an employee by pay period in the PAID PAYRUN DATA (#459) file.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDRPT</td>
<td>Fiscal reports.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDSERV</td>
<td>The driver routine for processing the master record downloads.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDSET</td>
<td>Parses the master record into pieces and stores the data into the PAID EMPLOYEE (#450) and/or PAID PAYRUN DATA (#459) files.</td>
<td></td>
</tr>
<tr class="odd">
<td><p>PRSDSRC</p>
<p>PRSDSRC1</p>
<p>PRSDSRC2</p>
<p>PRSDSRP</p>
<p>PRSDSRP1</p></td>
<td><p>Strength report compilation.</p>
<p>Strength report compilation (continued).</p>
<p>Strength report compilation (continued).</p>
<p>Strength report print.</p>
<p>Strength report print (continued).</p></td>
<td></td>
</tr>
<tr class="even">
<td>PRSDSRP2</td>
<td>Strength report print (continued).</td>
<td></td>
</tr>
<tr class="odd">
<td><p>PRSDSRP3</p>
<p>PRSDSRS</p></td>
<td><p>Salary report print.</p>
<p>Service record screen.</p></td>
<td></td>
</tr>
<tr class="even">
<td>PRSDSTAT</td>
<td>Creates a mail message with statistics concerning the processing of a master record download and sends that message to the PAD mail group at the station.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDUTIL</td>
<td>PAID download utility sub-routines.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDV450</td>
<td>Displays an employee entry from the PAID EMPLOYEE (#450) file.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDV459</td>
<td>Displays an employee entry from the PAID PAYRUN DATA (#459) file.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDVTBL</td>
<td>Contains the tables needed to run the PRSDV450 routine.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDW450</td>
<td>Write employee data.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSDXREF</td>
<td>Executes any cross references on a field when a new value is set from a master record download.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSDYTD</td>
<td>Compute year-to-date totals.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSE</td>
<td>Routine to check for version number, and run Employee/ED Menu.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSECAL</td>
<td>Calendar of classes by service and date.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEDEL</td>
<td>Purge routine for files 452/452.8.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEDEL1</td>
<td>Edit/delete student record.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEDESC</td>
<td>Education Tracking file descriptions.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED0</td>
<td>Site file enter/edit driver Feb 93.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED1</td>
<td>Enter-edit student record.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED10</td>
<td>PRSE non-local C.E. attendance.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED12</td>
<td>PRSE non-local C.E. attendance update continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED13</td>
<td>Employee mandatory training Grp/Clas enter/edit.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED14</td>
<td>E/E MI attendance by multiple employees.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED2</td>
<td>Log employee attendance into tracking file.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED3</td>
<td>Attendance - class complete.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED4</td>
<td>Education file population.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED5</td>
<td>Employee edit attendance.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED6</td>
<td>Enter/edit class registration.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED7</td>
<td>PRSE non-local C.E. attendance update continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEED8</td>
<td>PRSE attendance update.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEED9</td>
<td>PRSE attendance update continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEEMP</td>
<td>Attendance RPT by service.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEEMP1</td>
<td>Individual inservice attendance report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEEMP2</td>
<td>Attendance report by service.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEKILL</td>
<td>Variable clean-up.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEMSG</td>
<td>Education tracking messages.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEPMC</td>
<td>Employee mandatory training group/class report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEPMD1</td>
<td>Incomplete Nursing mandatory inservice class data part 2 of 2.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEPMD4</td>
<td>Individual MI deficiency by employee name.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEPMD5</td>
<td>Incomplete employee MI report (by class) part 1 of 2.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEPMD6</td>
<td>Incomplete mandatory inservice class date part 2 of 2.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEPOL0</td>
<td>OLDE training coding report.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEPOL1</td>
<td>OLDE training coding report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEPRG0</td>
<td>Review group members report.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSERSTR</td>
<td>Class registration roster.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEUTL</td>
<td>Employee education report - utility.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEUTL1</td>
<td>Education global search utility.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEUTL2</td>
<td>Educational security routine.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEUTL3</td>
<td>Employee education report - utility.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEUTL4</td>
<td>Class assignment to mandatory training group.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSEUTL5</td>
<td>Update mandatory class mult from MI review group mult.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSEUTL6</td>
<td>Service selection from file 454.1.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSIKIL</td>
<td>Kill PAID 2.5 options &amp; routines.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSIPRE</td>
<td>Pre-initialization routine.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSIPST</td>
<td>Post-initialization routine.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSIPST1</td>
<td>Continuation of post-initialization.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSIPST2</td>
<td>Continuation of post-initialization.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSNTEG</td>
<td>The package checksums.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSNTEGO</td>
<td>The package checksums.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRASOR</td>
<td>Employee audit sort.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRAU1</td>
<td>Prior Pay Period audit report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRAU11</td>
<td>Prior Pay Period report continued.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSREX1</td>
<td>Individual Service expenditure report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSREX11</td>
<td>Expenditure report continued.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRL1</td>
<td>Employee leave usage report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRL11</td>
<td>Leave usage report continued.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRL12</td>
<td>Leave usage report continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRL2</td>
<td>Employee leave request report.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRL21</td>
<td>Leave request report continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRL4</td>
<td>Employee leave usage pattern.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRL41</td>
<td>Leave usage pattern continued.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRLL</td>
<td>Calculate leave length.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRLSOR</td>
<td>Leave report sorts.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSROSOR</td>
<td>OT/CT report sorts.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSROT1</td>
<td>Employee OT/CT report.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSROT11</td>
<td>OT/CT report continued.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRPSOR</td>
<td>Leave pattern sort.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRTLPR</td>
<td>Display print Tks, Supervisors, Approvers.</td>
<td></td>
</tr>
<tr class="even">
<td>PRSRUT0</td>
<td>Report utilities.</td>
<td></td>
</tr>
<tr class="odd">
<td>PRSRUTL</td>
<td>Report utilities.</td>
<td></td>
</tr>
</tbody>
</table>

File List

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE #</p>
<p>---------------</p></td>
<td><p>NAME</p>
<p>---------------------</p></td>
<td><p>DESCRIPTION</p>
<p>------------------------------------</p></td>
<td><p>DATA</p>
<p>COMES</p>
<p>WITH</p>
<p>FILE</p>
<p>---------------</p></td>
<td><p>MERGE</p>
<p>OR</p>
<p>OVER</p>
<p>WRITE</p>
<p>------------</p></td>
</tr>
<tr class="even">
<td>450</td>
<td>PAID EMPLOYEE</td>
<td>Contains master record data on all the station's employees.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450.11</td>
<td>PAID DOWNLOAD MESSAGE ERROR</td>
<td>Contains all master record download errors that occurred during the processing of a download. Purged after each download.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450.12</td>
<td>PAID DOWNLOAD MESSAGE</td>
<td>Contains a listing of all master record download messages that were received from the AAC for a download. Purged after each download.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>452</td>
<td>PRSE STUDENT EDUCATION TRACKING</td>
<td>Contains information on employee and non-employee attendance at continuing education and inservice programs.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>452.1</td>
<td>PRSE PROGRAM/ CLASS</td>
<td>Contains the names of continuing education and inservice programs used in the Education Tracking software.</td>
<td>NO</td>
<td>n/a</td>
</tr>
</tbody>
</table>

|       |                                        |                                                                                       |     |     |
|-------|----------------------------------------|---------------------------------------------------------------------------------------|-----|-----|
| 452.2 | PRSE EDUCATION PROGRAM/ CLASS SUPPLIER | Contains the names of companies or organiza-tions who supply the programs or classes. | NO  | n/a |

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE #</p>
<p>---------------</p></td>
<td><p>NAME</p>
<p>---------------------</p></td>
<td><p>DESCRIPTION</p>
<p>------------------------------------</p></td>
<td><p>DATA</p>
<p>COMES</p>
<p>WITH</p>
<p>FILE</p>
<p>---------------</p></td>
<td><p>MERGE</p>
<p>OR</p>
<p>OVER</p>
<p>WRITE</p>
<p>------------</p></td>
</tr>
<tr class="even">
<td>452.3</td>
<td><p>PRSE MAN-DATORY</p>
<p>TRAINING</p>
<p>(MI) CLASS GROUP</p></td>
<td>Contains groups of mandatory or required classes. For Nursing Service, this was known as Mandatory Inservice (MI). These groups can be for individual students or entire services.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>452.4</td>
<td>PRSE EDU-CATION PROGRAM/ CLASS CATEGORY</td>
<td>Contains information used to categorize related programs/classes. Entries in this file are not to be edited.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td>452.5</td>
<td>PRSE EDUCATION PRESENTA-TION MEDIA</td>
<td>Contains methods of presenting a program/ class.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td>452.51</td>
<td>PRSE EMPLOYEE PURPOSE OF TRAINING</td>
<td>Contains reasons for attending a program/ class.</td>
<td>YES</td>
<td>OVER WRITE</td>
</tr>
<tr class="even">
<td>452.6</td>
<td>PRSE SVC REASONS FOR TRAINING</td>
<td>Contains the service's reasons for individuals attending a program/ class.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>452.7</td>
<td>PRSE PARAME-TERS</td>
<td>Contains specific parameters used in the Education Tracking Application.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>452.8</td>
<td>PRSE EDUCA-TION REGIS-TRATION</td>
<td>Contains information on employee/student registration.</td>
<td>NO</td>
<td>n/a</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE #</p>
<p>---------------</p></td>
<td><p>NAME</p>
<p>---------------------</p></td>
<td><p>DESCRIPTION</p>
<p>------------------------------------</p></td>
<td><p>DATA</p>
<p>COMES</p>
<p>WITH</p>
<p>FILE</p>
<p>---------------</p></td>
<td><p>MERGE</p>
<p>OR</p>
<p>OVER</p>
<p>WRITE</p>
<p>------------</p></td>
</tr>
<tr class="even">
<td>452.9</td>
<td>PRSE EDUCATON ACCREDITA-TION ORGA-NIZATIONS</td>
<td>Contains information on organizations which accredit the continuing education programs.</td>
<td>YES</td>
<td>MERGE</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>454</td>
<td>PAID CODE FILES</td>
<td>Contains the PAID codes and their descriptions.</td>
<td>YES</td>
<td>MERGE</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>454.1</td>
<td><p>PAID COST CENTER/</p>
<p>ORGANIZA-TION</p></td>
<td>Contains the Cost Centers and Organizations used at the station.</td>
<td>YES</td>
<td>MERGE</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td>455.1</td>
<td>8B ERROR MESSAGE</td>
<td>Contains error messages corresponding to the various edit errors that may be detected during the processing and the checking of the 8B record entry.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>455.5</td>
<td>T&amp;L UNIT</td>
<td>Contains the list of T&amp;L units established by a station as well as the associated timekeepers, supervisors who approve OT/CT, and supervisors who sign time and attendance reports.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>457.1</td>
<td>TOUR OF DUTY</td>
<td>Contains a list of all tours of duty used by the station.</td>
<td>YES</td>
<td>MERGE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>457.2</td>
<td>SPECIAL TOUR INDICATOR</td>
<td>Contains a list of special processing conditions related to a tour of duty.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE #</p>
<p>---------------</p></td>
<td><p>NAME</p>
<p>---------------------</p></td>
<td><p>DESCRIPTION</p>
<p>------------------------------------</p></td>
<td><p>DATA</p>
<p>COMES</p>
<p>WITH</p>
<p>FILE</p>
<p>---------------</p></td>
<td><p>MERGE</p>
<p>OR</p>
<p>OVER</p>
<p>WRITE</p>
<p>------------</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td>457.3</td>
<td>TYPE OF TIME</td>
<td>Contains a list of types of work or leave time used in time and attendance report posting.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>457.4</td>
<td>TIME REMARKS</td>
<td>Contains entries used to indicate conditions related to a time segment posted to a time and attendance report.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>457.5</td>
<td>PAY ENTITLE-MENT</td>
<td>Contains a string of codes to indicate entitlement to specific types of time for different pay plan categories.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td>457.6</td>
<td>ENVIRON-MENTAL DIFFEREN-TIALS</td>
<td>Contains a list of valid environmental differentials which may be requested.</td>
<td>YES</td>
<td><p>OVER</p>
<p>WRITE</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>458</td>
<td>TIME &amp; ATTEND-ANCE RECORDS</td>
<td>Contains all data that appears on an employee's time and attendance report.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>458.1</td>
<td>LEAVE REQUESTS</td>
<td>Contains leave requests entered by employees.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>458.2</td>
<td>OT/CT REQUESTS</td>
<td>Contains all requests for OT/CT other than those scheduled as part of a tour of duty.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>458.3</td>
<td>ENVIRON-MENTAL DIFF. REQUESTS</td>
<td>Contains all Environmental Differential requests.</td>
<td>NO</td>
<td>n/a</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE #</p>
<p>---------------</p></td>
<td><p>NAME</p>
<p>---------------------</p></td>
<td><p>DESCRIPTION</p>
<p>------------------------------------</p></td>
<td><p>DATA</p>
<p>COMES</p>
<p>WITH</p>
<p>FILE</p>
<p>---------------</p></td>
<td><p>MERGE</p>
<p>OR</p>
<p>OVER</p>
<p>WRITE</p>
<p>------------</p></td>
</tr>
<tr class="even">
<td>458.5</td>
<td>PRIOR PP EXCEPTIONS</td>
<td>Contains data identifying prior pay period exceptions for employee time and attendance reports.</td>
<td>NO</td>
<td>n/a</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>459</td>
<td>PAID PAYRUN DATA</td>
<td>Contains accounting data on employees by pay period. A snapshot of an employee's earnings, deductions and leave usage for a pay period.</td>
<td>NO</td>
<td>n/a</td>
</tr>
</tbody>
</table>

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |

Exported Options

PRSA ED CAN

Cancel Envir. Diff. Request run routine

CAN^PRSAEDR

This option allows the user to cancel an environmental differential request.

PRSA ED LST

List Environment Diff. Requests run routine

TK^PRSAEDL

This option allows the user to list environmental differential requests

within a user specified time span for one or all employees of a Time and

Leave Unit. The requests may be sorted by employee or date of request.

PRSA ED LST-SUP

List Environment Diff. Requests run routine

SUP^PRSAEDL

This option lists Environmental Differential requests for a supervisor.

PRSA ED REQ

Envir. Diff. Request run routine

PRSAEDR

This option allows the user to enter an environmental differential request

for an employee. The date, from and to time, type of exposure, and

justification are entered.

PRSA ED/VCS

Envir. Diff./VCS Sales menu

PRSA ED REQ

PRSA ED CAN

PRSA ED LST

PRSA VC POST

This submenu allows the user to enter, cancel and list environmental

differential requests. Also, the user may post Veteran Canteen Service

commission sales.

PRSA EDIT

8B Edit Checks run routine

PRSACED

This option detects most of the 8B records that would be rejected by the

Austin Automation Center.

PRSA EMP MENU

Employee Menu menu

PRSA LV REQ

PRSA LV DISP

PRSA LV CAN

PRSA LV BAL-EMP

PRSD SERVICE RECORD SCREEN

PRSA TPD PP-EMP

PRSE-IND-REG

PRSA LV EDIT

PRSREM-LEV-USED

This menu allows the employee to enter, cancel and list his/her leave

requests. Also, the employee may list his/her leave balances.

PRSA EN EMP

Display Employee Entitlements run routine

PRSAENE

This option allows the user to select an employee and display his/her

entitlement to each type of time worked or leave earned/used.

PRSA EN TAB

Display Entitlement Table run routine

PRSAENX

This option deciphers the work/leave entitlement character string. It

displays the categories of work and leave and whether a value should be

entered in that category.

PRSA LV BAL-EMP

Leave Balances run routine

EMP^PRSALVB

Displays a list of the leave balances an employee has.

PRSA LV BAL-SUP

Employee Leave Balances run routine

SUP^PRSALVB

This option allows a user to view all leave balances for an employee he/she

supervises. Leave fields that have no value (i.e., null) are not listed.

PRSA LV BAL-TK

Employee Leave Balances run routine

TK^PRSALVB

This option allows a timekeeper to display leave balances for any employee

in an assigned T&L.

PRSA LV CAN

Cancel Leave Request run routine

PRSALVX

The employee enters a date and a list of all his/her leave requests from

that date onward are displayed. The employee is prompted to select a choice

from the list to cancel.

PRSA LV DISP

Display Leave Requests run routine

PRSALVS

The employee enters a date and a list of all his/her leave requests from

that date onward are displayed.

PRSA LV EDIT

Edit Leave Request run routine

PRSALVE

This option allows an employee to edit a leave request which begins on a day

that has yet to be posted.

PRSA LV LST

List Leave Requests run routine

TK^PRSALVL

This option allows the user to list leave requests for one or all employees.

The user enters a 'begin' date and an 'end' date. All leave requests for the

employee(s) chosen will be displayed. The list may be sorted by employee

name or date of leave request. The date, time, type of leave and any remarks

are listed.

PRSA LV LST-SUP

List Leave Requests run routine

SUP^PRSALVL

This option allows the user to list leave requests for one or all employees.

The user enters a 'begin' date and an 'end' date. All leave requests for the

employee(s) chosen will be displayed. The list may be sorted by employee

name or date of leave request. The date, time, type of leave and any remarks

are listed.

PRSA LV PAY

List Leave Requests run routine

PAY^PRSALVL

This option will allow Payroll to display leave requests for any time period

for any T&L.

PRSA LV REQ

Leave Request run routine

PRSALVR

This option allows an employee to make a request for leave (i.e.,

APPLICATION FOR LEAVE, SF 71). The employee must be entered in both the PAID

EMPLOYEE (#450) and NEW PERSON (#200) files and the social security numbers

must match.

PRSA OT APP

Approve OT/CT run routine

PRSAOTX

This option allows the user to approve an overtime or compensatory time

request.

PRSA OT CAN

Cancel OT Request run routine

CAN^PRSAOTR

This option allows the user to cancel an overtime/compensatory time request.

After selecting the employee, the user specifies a date to begin searching

for all such requests. That employee's requests are listed and the user

selects the one to cancel.

PRSA OT EDIT

Edit OT/CT Request run routine

PRSAOTE

This option allows the supervisor to edit an OT/CT request which has not yet

been posted.

PRSA OT LST

Display OT/CT Requests run routine

TK^PRSAOTL

This option allows a user to list overtime and compensatory time requests

for one or more employees. The user enters a 'begin' date and an 'end' date.

All leave requests for the employee(s) chosen will be displayed. The date,

number of hours, type of request and the justification for the request are

listed.

PRSA OT LST-SUP

Display OT/CT Requests run routine

SUP^PRSAOTL

This option allows a user to list overtime and compensatory time requests

for one or more employees. The user enters a 'begin' date and an 'end' date.

All leave requests for the employee(s) chosen will be displayed. The date,

number of hours, type of request and the justification for the request are

listed.

PRSA OT MENU

T&A OT/Supervisor Menu menu

PRSA SUP CERT

PRSA SUP REV

PRSA LV LST-SUP

PRSA LV BAL-SUP

PRSA OT LST-SUP

PRSA TPE ONE-SUP

PRSA TPE ALL-SUP

PRSA TK TOUR-DISP-SUP

PRSA TPD PP-SUP

PRSA TD LIST

PRSA ED LST-SUP

PRSA OT APP

PRSA SUP UNR

This option allows the user to perform supervisory T&A functions and approve

overtime.

PRSA OT PAY

List OT/CT Requests run routine

PAY^PRSAOTL

This option will allow payroll to list OT/CT requests.

PRSA OT REQ

Enter OT/CT Request run routine

PRSAOTR

This option allows the user to enter a request for an employee to work

overtime or compensatory time. After selecting the employee, the user enters

the date the work is to be performed, type of time worked, number of hours

to be worked, time and leave unit where the work will be performed, and the

justification for making this request.

PRSA PAY ASX

List Supervisors Certified by a T&L run routine

ASX^PRSATL

This option will list all supervisors who are certified by a particular T&L.

PRSA PAY AUD

Display Complete Request/Pay Period Records menu

PRSA PAY AUD-LV

PRSA PAY AUD-OT

PRSA PAY AUD-ED

PRSA PAY AUD-PP

This menu contains options which allow payroll to display all of the fields

of Leave, OT/CT, Environmental Differential, and Pay Period records for an

employee.

PRSA PAY AUD-ED

Display Environmental Differential Request run routine

ED^PRSADPA

This option allows payroll to display all of the fields of an Environmental

Differential Request.

PRSA PAY AUD-LV

Display Leave Request run routine

LV^PRSADPA

This option allows payroll to display all of the fields of a leave request.

PRSA PAY AUD-OT

Display OT/CT Request run routine

OT^PRSADPA

This option allows payroll to display all of the fields of an OT/CT Request.

PRSA PAY AUD-PP

Display Pay Period for Employee run routine

PP^PRSADPA

This option allows payroll to display all of the fields of a pay period for

an employee.

PRSA PAY CLR

Clear Prior Pay Period Exceptions run routine

PRSATPD

This option allows Payroll to clear exceptions listed in File 458.5.

PRSA PAY DECOMP

Decompose Time run routine

1^PRS8

The user selects a pay period and an employee. The data on that time card is

checked by a series of computer routines that apply payroll rules and builds

an 8B record that will be sent to the Austin Automation Center (AAC).

The pay period, employee name, social security number, time card "stub

record", and any data values that will be sent to the AAC are displayed.

PRSA PAY EXC

Pay Period Exceptions run routine

PRSAPEX

Displays a list of time card problems or questions for a pay period that

needs to be resolved. The name of the employee, day and date, and a short

description of the exception are displayed.

PRSA PAY MENU

Payroll Main Menu menu

PRSA PM POST

PRSA EN EMP

PRSA PAY EXC

PRSA PR

PRSA PE DISP

PRSA PAY PPE

PRSA PAY TD-MAN

PRSA PAY TL-MAN

PRSD 04 EMPLOYEE INQUIRY MENU

PRSA PP EMP

PRSA PAY PPC

PRSA TL EMP

PRSA SUP UNR-PAY

PRSA PAY CLR

PRSA LV PAY

PRSA OT PAY

PRSA PAY AUD

PRSRFI-PAID SYSTEM REPORTS

This menu contains options a Payroll Clerk needs to perform Time and

Attendance related tasks.

PRSA PAY MGR

Payroll Supervisor Menu menu

PRSA PP OPEN

PRSA PT MENU

PRSA XMIT

PRSA UNREVIEW LIST

PRSA TH

PRSA EDIT

PRSA TD EDIT

PRSA PAY MENU

PRSA TK EMP-HOL

PRSA PAY ASX

PRSA TL EDIT

This is the Payroll Supervisor's menu. The options on this menu allow the

user to perform the tasks needed to process a station's time cards.

PRSA PAY PPC

List/Clear Prior Pay Period Corrections run routine

PRSAPPP

This option allows Payroll to display or list the Prior Pay Period

Corrections that have been approved by the supervisor. If performed on a

CRT, the Payroll Clerk can indicate that the entry has been cleared and that

appropriate corrective OLDE actions have been taken.

PRSA PAY PPE

List Prior Pay Period Exceptions run routine

PAY^PRSATPG

Lists any unresolved problems with a prior pay period's time cards. The

employee's name, time and leave unit, date of the exception and a short

message are displayed.

PRSA PAY TD-MAN

Tour of Duty Management menu

PRSA TD DISP

PRSA TD LIST

This option is a submenu on the Payroll Main Menu. This submenu allows the

user to list Tours of Duty and to display information about any Tour of

Duty.

PRSA PAY TL-MAN

T&L Management menu

PRSA TL DISP

PRSA TP DAY LIST-PAY

This option is a submenu on the Payroll Main Menu. This submenu allows the

user to list Time and Leave Units (T&L) and display information about any

T&L.

PRSA PE DISP

Display Employee Pay Period run routine

PAY^PRSADP2

Displays the employee's name, all fourteen dates in the pay period, the

employee's scheduled tour(s) and any exceptions to the scheduled tour(s).

PRSA PM POST

Post Miscellaneous Data run routine

PRSAPEM

This option allows Payroll to enter time and attendance related data such as

Annual Leave Lump Sum values and a T&L change.

PRSA PP EMP

Create Employee Record for Pay Period run routine

PRSAPRE

This option will allow Payroll to create a time card entry for an employee

in the TIME AND ATTENDANCE RECORDS file (#458). The employee must exist as

an entry in the PAID EMPLOYEE file (#450).

PRSA PP OPEN

Open Next Pay Period run routine

PRSAPPO

This option allows Payroll to create a new pay period entry in the TIME AND

ATTENDANCE RECORDS file (#458) and creates a time card entry for each

employee within that pay period.

PRSA PR

Return Record to Timekeeper run routine

PRSAPRT

This option allows Payroll to return a time card to the Timekeeper for

correction and re-certification.

PRSA PT D1

Display Special Tour Indicator run routine

STID^PRSAPT1

This option displays a list of the special tour indicators, the type of time

associated with each indicator and the indicator's code.

PRSA PT D2

Display Type of Time Table run routine

TTD^PRSAPT1

This option displays a list of the various types of time that may be coded

on a time card. The code, a short description and a long description are

displayed for each entry.

PRSA PT D3

Display Time Remarks run routine

TRMD^PRSAPT1

This option displays a list of the various time remarks. For each time

remark, the code, its description and the applicable types of time

associated with it are displayed.

PRSA PT MENU

Payroll Table Maintenance menu

PRSA PT D1

PRSA PT D2

PRSA PT D3

PRSA EN TAB

This option is a submenu on the Payroll Supervisor Menu. The options on this

submenu allow the user to display Special Tour Indicators, Types of Time,

Time Remarks and Entitlement Table entries.

PRSA SUP ALERTS

Supervisor Alerts action

This action checks to see if there exist any pending PAID actions for any

T&L's for which the user is a supervisor.

PRSA SUP CERT

Supervisory Approvals run routine

PRSASC

This option displays any actions that need a supervisor's approval such as a

change in an employee's Tour of Duty. The supervisor is prompted to approve,

disapprove or cancel the request.

PRSA SUP MENU

T&A Supervisor Menu menu

PRSA SUP CERT

PRSA OT LST-SUP

PRSA LV LST-SUP

PRSA SUP REV

PRSA ED LST-SUP

PRSA TPE ALL-SUP

PRSA TPE ONE-SUP

PRSA TD LIST

PRSA TPD PP-SUP

PRSA TK TOUR-DISP-SUP

PRSA LV BAL-SUP

PRSA SUP UNR

PRSA SUP PPE

PRSRSU-PAID SYSTEM REPORTS

This is the Time and Leave Unit (T&L) supervisor's menu. The options on this

menu allow the user to perform the tasks needed to complete a T&L's time

cards.

PRSA SUP PPE

List Prior Pay Period Exceptions run routine

SUP^PRSATPG

This option will allow a supervisor to list all exceptions from prior pay

periods for a T&L of which the person is a supervisor.

PRSA SUP REV

Pay Period Certification run routine

PRSASR

This option will display each date within the pay period, the scheduled tour

for that date and any tour exceptions for each employee of each time and

leave unit the supervisor is responsible for certifying.

PRSA SUP UNR

List Un-Certified Employees run routine

SUP^PRSASU

This option will list all employees of a selected T&L Unit which have not

been certified (released to Payroll). For Day numbers less than 6, it will

default to the last Pay Period. Otherwise, it is the current Pay Period.

PRSA SUP UNR-PAY

List Un-Certified Employees run routine

PAY^PRSASU

This option will list all employees of a selected T&L Unit which have not

been certified (released to Payroll). For Day numbers less than 6, it will

default to the last Pay Period. Otherwise, it is the current Pay Period.

PRSA SUP UNR-TK

List Un-Certified Employees run routine

TK^PRSASU

This option will list all employees of a selected T&L Unit which have not

been certified (released to Payroll). For Day numbers less than 6, it will

default to the last Pay Period. Otherwise, it is the current Pay Period.

PRSA T&L DECOMP REPORT

T&L Decomposition Report run routine

PRS8TL

Allows the user to select one or more Time and Leave Units (T&Ls) for a pay

period and to decompose (create an 8B record) or merely list the time card

status.

PRSA TD DISP

Display Tour of Duty run routine

DISP^PRSATD1

This option will prompt the user to select an established tour of duty. It

will display the tour description, length of meal time, whether meal time is

subject to premium pay, whether the tour spans two calendar days, whether

the tour is available to all time and leave units, and the start/stop times

for each segment of the tour.

This option merely displays the tour information. You may not edit the tour

with this option.

PRSA TD EDIT

Enter/Edit Tour of Duty run routine

EDIT^PRSATD1

This option allows the user to create a new tour or to select an existing

tour. The user may enter the data for the new tour or edit the data on the

existing tour.

The user will be asked for the tour description, length of meal time,

whether the meal time is subject to premium pay, whether the tour spans two

calendar days, whether the tour is available to all time and leave units and

the start/stop times for each segment of the tour.

PRSA TD LIST

List Tours by T&L run routine

PRSATD2

The user is prompted to select a particular Time and Leave Unit (T&L) or ALL

Time and Leave Units. If a particular T&L is selected, then all the tours

associated with it are displayed. If ALL T&Ls are selected, then all Tours

of Duty will be displayed along with the T&Ls associated with the tour.

The tour number, start/stop times, number of hours in the tour, start/stop

times of the various segments of the tour, any special indicators for each

time segment and the T&L(s) associated with the tour are displayed.

PRSA TH

Transmission History run routine

PRSATH

This option will provide a summary of information concerning a selected pay

period including the number of records transmitted, the number of mail

messages sent, the number of mail messages acknowledged from Austin, the

clerk who transmitted the records and the date/time of data transmission to

Austin.

PRSA TK EMP-HOL

Set Holiday Benefit Day run routine

PRSAPEH

This option allows the Timekeeper to select an open posting date and mark

that date as a Holiday Benefit day so that HX and/or HW can be posted. It is

designed for use only in those cases where the automatic determination of

the holiday has selected an incorrect date or for those cases where a

part-time worker is unable to work because of a Holiday.

PRSA TK MEN-EMP

Employee Data menu

PRSA TPD

PRSA TPD PP

PRSA TK TOUR-DISP

PRSA TK TOUR-EDIT

PRSA LV BAL-TK

This option is a submenu. It allows a Timekeeper to display posted time card

data on an employee, enter/edit an employee's Tour of Duty and display an

employee's leave balances.

PRSA TK MENU

TimeKeeper Main Menu menu

PRSA OT REQ

PRSA TK POST

PRSA OT CAN

PRSA OT LST

PRSA LV LST

PRSA TPE ALL

PRSA TPE ONE

PRSA TP MENU

PRSA TD LIST

PRSA ED/VCS

PRSA TP DAY LIST

PRSA TPE PPE

PRSA TK MEN-EMP

PRSA SUP UNR-TK

PRSA OT EDIT

This is the Timekeeper's menu. The options on this menu allow the user to

post time and attendance data for Time and Leave Unit (T&L).

PRSA TK POST

Post Employee Time run routine

PRSATP

This option allows the Timekeeper to post time card data on employees. The

Timekeeper is prompted for a date and whether or not to post the employees

time cards in alphabetical order.

PRSA TK TOUR-DISP

Display Employee Tour of Duty run routine

TK^PRSATE2

This option allows the user to display the Tour(s) of Duty for an employee

for this pay period, the last one, or the next. The supervisor may choose

to see a brief or detailed display.

PRSA TK TOUR-DISP-SUP

Display Employee Tour of Duty run routine

SUP^PRSATE2

This option allows the user to display the Tour(s) of Duty for an employee

for this pay period, the last one, or the next. The supervisor may choose

to see a brief or detailed display.

PRSA TK TOUR-EDIT

Enter/Edit Employee Tour of Duty run routine

PRSATE

This option allows the user to enter or edit a Tour of Duty for an employee

for this pay period, the last one, or the next.

PRSA TL DISP

Display T&L Unit run routine

DISP^PRSATL

The user is prompted to select an existing time and leave unit. The

following data associated with the time and leave unit is displayed: name,

station number, Service/Section, whether the time and leave unit has

Saturday and Sunday premium pay, the timekeeper(s), supervisor(s), and the

overtime/compensatory time approver(s).

This option will display the data associated with the time and leave unit.

The user may not edit the data with this option.

PRSA TL EDIT

Enter/Edit T&L Unit run routine

EDIT^PRSATL

The user may create a new time and leave unit entry or edit an existing

entry. The user will be prompted to enter the three character code for the

time and leave unit, name, station number, Service/Section, whether the time

and leave unit is entitled to Saturday and Sunday premium pay, the

timekeeper(s), supervisor(s), and overtime/compensatory time approver(s). If

the time and leave unit has standby tours associated with it, then a value

should be entered for when the sleep time period will begin.

PRSA TL EMP

Change Employee T&L Unit run routine

EMP^PRSATL

This option allows Payroll to change the T&L Unit of an employee in File

450\. Change will be reflected in stub record of next pay transmission to

Austin.

PRSA TP DAY LIST

Daily T&L List run routine

TK^PRSATPL

The user is prompted to select an existing Time and Leave Unit (T&L) and a

posting date. The names of the employees in the T&L, their scheduled Tour of

Duty and any exceptions to the scheduled Tour of Duty are displayed.

PRSA TP DAY LIST-PAY

Daily T&L List run routine

PAY^PRSATPL

The user is prompted to select an existing Time and Leave Unit (T&L) and a

posting date. The names of the employees in the T&L, their scheduled Tour of

Duty and any exceptions to the scheduled Tour of Duty are displayed.

PRSA TP ENVIR. DIFF.

Environmental Differential run routine

PRSAEDR

This option allows the user to make changes to posted environmental

differential time card data on an employee's time card for a prior pay

period (a corrected time card).

PRSA TP MENU

Prior Pay Period Adjustments menu

PRSA TP ENVIR. DIFF.

PRSA TP VCS

PRSA TP POST

This option is a submenu. It allows the user to post time card changes for a

prior pay period.

PRSA TP POST

Posting/Tour Change run routine

PRSATPP

This option allows changes to be made to an employee's posted time card data

or Tour of Duty for a prior pay period (a corrected time card).

PRSA TP VCS

VCS Commission Sales run routine

PRP^PRSATVC

This option allows changes to be made to an employee's posted Veteran

Canteen Service commission sales data from a prior pay period (a corrected

time card).

PRSA TPD

Display Posted Data run routine

TK^PRSADP

This option allows the Timekeeper to select an employee and a posting date.

The employee's scheduled Tour of Duty and any exceptions to that tour will

be displayed.

PRSA TPD PP

Display Employee Pay Period run routine

TK^PRSADP2

This option allows the user to select an employee and a posting date. The

employee's scheduled Tour of Duty and any Tour of Duty exceptions for the

pay period for which the posting date belongs are displayed.

PRSA TPD PP-EMP

Display Pay Period run routine

EMP^PRSADP2

Option for an employee to display data of one of their own Pay Periods.

PRSA TPD PP-SUP

Display Employee Pay Period run routine

SUP^PRSADP2

Supervisor option to display pay Period data for an employee.

PRSA TPE ALL

Display Pay Period Exceptions run routine

TK1^PRSATPX

This option allows the user to list any time card problems for a selected

pay period. The name of the employee, date of the exception, and a short

message are displayed for the first day of the pay period to the posting

date chosen.

PRSA TPE ALL-SUP

Display Pay Period Exceptions run routine

SUP1^PRSATPX

This option allows the user to list any time card problems for a selected

pay period. The name of the employee, date of the exception, and a short

message are displayed for the first day of the pay period to the posting

date chosen.

PRSA TPE ONE

List Daily Exceptions run routine

TK0^PRSATPX

This option allows the user to list any time card problems for a date

selected. The name of the employee and a short message are displayed.

PRSA TPE ONE-SUP

List Daily Exceptions run routine

SUP0^PRSATPX

This option allows the supervisor to list any time card problems for a date

selected. The name of the employee and a short message are displayed.

PRSA TPE PPE

List Prior Pay Period Exceptions run routine

TK^PRSATPG

This option lists all time card exceptions for the previous pay period.

PRSA UNREVIEW LIST

Un-Transmitted Employees (All T&Ls) run routine

PRSARPT2

This option displays the name, T&L unit and status of all employees who had

no data entered by a Timekeeper or have not been certified or reviewed by

Payroll.

PRSA VC POST

Post VCS Commission Sales run routine

PRSATVC

This option allows the user to enter the dollar and cents amounts of

commission sales for Veteran Canteen Service pieceworkers.

PRSA XMIT

Transmit 8B Data to Austin run routine

PRSAXMIT

This option will transmit all 8B records that have been reviewed by Payroll

to the Austin Automation Center.

PRSD

Download Employee Data server

PRSDSERV

This server option receives employee master records and accounting data from

the Austin Automation Center and stores that data into the PAID EMPLOYEE

file (#450) and/or the PAID PAYRUN DATA file (#459).

PRSD 04 EMPLOYEE INQUIRY

Employee Inquiry run routine

EN2^PRSDV450

This option will allow designated Fiscal Service users to view PAID EMPLOYEE

file data.

PRSD 04 EMPLOYEE INQUIRY MENU

Employee Inquiry Menu menu

PRSD 04 PRINT EMPLOYEE FILES

PRSD 04 SEARCH EMPLOYEE FILES

PRSD 04 EMPLOYEE INQUIRY

PRSD 04 PAYRUN DATA INQUIRY

PRSD UPDATE PAID CODES

This option will allow the Fiscal user to access a menu of employee inquiry

options.

PRSD 04 PAYRUN DATA INQUIRY

Payrun Data Inquiry run routine

PRSDV459

This option will allow designated Fiscal Service users to view the PAID

PAYRUN DATA (#459) file.

PRSD 04 PRINT EMPLOYEE FILES

Print Employee Entries run routine

PRNT04^PRSDPRNT

This option will allow the Fiscal user to invoke the FileMan PRINT FILE

ENTRIES option for the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459)

files.

PRSD 04 SEARCH EMPLOYEE FILES

Search Employee Entries run routine

SRCH04^PRSDPRNT

This option will allow the Fiscal user to invoke the FileMan SEARCH FILE

ENTRIES option for the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459)

files.

PRSD 05 AD HOC REPORTS

Ad Hoc Report Generator run routine

PRSDAH

This option will allow the HRM user to generate four Ad Hoc reports: 1)

Basic Employee fields, 2) Title 38 Employee fields, 3) Physician & Dentist

Fields and 4) Followup Codes.

PRSD 05 CCORG EDIT

Enter/Edit Cost Center/Organization file edit

This option allows the user to enter/edit the data in the PAID COST

CENTER/ORGANIZATION file (#454.1).

PRSD 05 EMPLOYEE INQUIRY

Employee Inquiry run routine

EN1^PRSDV450

This option will allow designated Personnel Service employees to view

designated PAID EMPLOYEE (#450) file data.

PRSD 05 EMPLOYEE INQUIRY MENU

Employee Inquiry/Reports Menu menu

PRSD 05 PRINT EMPLOYEE FILE

PRSD 05 SEARCH EMPLOYEE FILE

PRSD 05 EMPLOYEE INQUIRY

PRSD UPDATE PAID CODES

PRSD 05 CCORG EDIT

PRSD COMPILE STRENGTH REPORT

PRSD PRINT STRENGTH REPORT

PRSD 05 AD HOC REPORTS

This option will allow the Personnel user to access a menu of employee

inquiry options.

PRSD 05 PRINT EMPLOYEE FILE

Print Employee Entries run routine

PRNT05^PRSDPRNT

This option will allow the Personnel user to invoke the FileMan PRINT FILE

ENTRIES option for the PAID EMPLOYEE (#450) file.

PRSD 05 SEARCH EMPLOYEE FILE

Search Employee Entries run routine

SRCH05^PRSDPRNT

This option will allow the Personnel user to invoke the FileMan SEARCH FILE

ENTRIES option for the PAID EMPLOYEE (#450) file.

PRSD COMPILE STRENGTH REPORT

Compile/Print Strength Report run routine

PRSDSRC

This option will compile the strength report statistics, store them in the

PAID COST CENTER/ORGANIZATION file and allow the user to print the strength

report.

PRSD PRINT STRENGTH REPORT

Print Strength Report run routine

PRSDSRP

This option will print a Strength Report as of the last compilation.

PRSD PROCESS PRS (STARTUP)

Process Unprocessed Download Data run routine

PROC^PRSDPROC

This option will process any leftover download data in the PRS global. This

option will automatically run at system startup.

PRSD SERVICE RECORD SCREEN

Service Record Screen run routine

PRSDSRS

This option displays an employee's Service Record Card information.

PRSD UPDATE PAID CODES

Update PAID Codes run routine

ENT^PRSDFIL

This option will allow the user to enter, edit or delete PAID codes and

their descriptions from the PAID CODE FILES (#454).

PRSE-ACC

Accrediting Organization run routine

EN5^PRSEED4

This option allows the user to enter or edit information in the Class

Accreditation Organizations file (#452.9).

PRSE-ATTEND

Enter/Edit Class Attendance run routine

EN1^PRSEED8

This option allows entry of class attendance in the PRSE Student Education

Tracking file (#452). This option documents attendance of participants in

current and past classes entered in the Program/Class file (#452.1),

PRSE-ATTENDANCE

Attendance Menu menu

PRSE-ATTEND

PRSE-NCEATTEND

PRSE-EE-EMP

PRSE-I-EMP

PRSE-MI-MULT

This menu contians options used to document attendance at past or present

classes. Information is stored in the PRSE Student Education Tracking file

(#452).

PRSE-C.E.

Enter/Edit Local Continuing Education run routine

EN4^PRSEED0

This option allows the creating and editing of continuing education classes

presented at the medical center.

PRSE-CLAS

Class File Edit run routine

EN1^PRSEED4

This option allows editing of classes in the PRSE Program/Class file

(#452.1).

PRSE-CLS-REG

Class Registration Enter/Delete run routine

EN1^PRSEED6

This option allows an individual to register students for a class.

PRSE-CORD

Package Coordinator Menu menu

PRSE-SITE

PRSE-PRT

PRSE-CLS-REG

PRSE-ATTENDANCE

PRSE-EE-CLAS-INFO

This menu contains options assigned to the Package Coordinator which prompt

the user to setup classes, register students, take class attendance, and

print various reports.

PRSE-DEMP

Service Mandatory Training (MI) Deficiency Report run routine

EN1^PRSEPMD5

This option allows the user to print a report of all the programs or classes

missed by an employee for a calendar year, a fiscal year, or selective

dates.

PRSE-EE-CLAS-INFO

Enter/Edit Class Information menu

PRSE-M.I.

PRSE-MIEX

PRSE-C.E.

PRSE-O.I.

PRSE-W.I.

This option allows the user to create and edit different types of classes

(e.g., mandatory training, continuing education, miscellaneous inservices,

and unit/location inservices) for registration and attendance. Entries are

stored in the PRSE Program/Class file (#452.1), and the PRSE Education

Registration file (#452.8).

PRSE-EE-EMP

Modify Past Class Information run routine

EN1^PRSEDEL1

This option allows a user to edit or delete all records in the Student

Education Tracking file (#452) for a specific class of a given date/time.

There are four pieces of data (i.e., Training Class, Program/Class Supplier,

Training Type, and Length) changes allowed and the system will automatically

update all student records that are associated with this class.

PRSE-EE-SVC

Service Reason run routine

EN6^PRSEED4

This option allows the user to edit the PRSE Svc Reasons for Training file

(#452.6).

PRSE-EMP

Service Training Report run routine

EN1^PRSEEMP

This option allows the user to print service reports on programs or classes

attended by employees. The reports can be printed by calendar year, fiscal

year, or selective dates.

PRSE-EMP-MI

Assign/Delete Training Groups for Staff/Services run routine

EN1^PRSEED13

This option allows assigning of employees or services to one or more

mandatory training (MI) groups, or individually required classes.

PRSE-FL-SITE

Enter/Edit Tracking Parameter File run routine

EN7^PRSEED4

This option allows the user to enter or edit data in the PRSE Parameter

file.

PRSE-I-EMP

Quick Attendance Update of Past/Purged Classes run routine

EN1^PRSEED1

This option allows the user to create and edit an employee record when past

classes were purged from the PRSE Program/Class file (#452.1).

PRSE-IND-CLS

Individual Training Report run routine

EN1^PRSEEMP1

This option allows an individual to view and print his/her own educational

record of attended courses.

PRSE-IND-DEMP

Individual Mandatory Training (MI) Deficiency run routine

EN1^PRSEPMD4

This option allows the user to review and print required classes not

attended by the employee. Courses not attended as required are designated

as deficiencies.

PRSE-IND-REG

Self Registration Enter/Edit run routine

EN1^PRSEED5

This option allows an employee to self register into a class of their

choice.

PRSE-INS-MENU

Education Tracking Instructor Menu menu

PRSE-CLS-REG

PRSE-ATTENDANCE

PRSE-PRT

PRSE-EE-CLAS-INFO

This is the main menu for Education Tracking Package instructors.

PRSE-IRM

IRM Menu menu

PRSE-STU-PURG

PRSE-FL-SITE

This menu contains the package site parameter option and a purge option for

the PRSE Student Education Tracking file (#452).

PRSE-M.I.

Enter/Edit Mandatory Training (MI/Brief) run routine

EN3^PRSEED0

This option allows editing of a mandatory inservice program/class which does

not contain information required for OLDE reporting requirements.

PRSE-MAN

Create Mandatory Training (MI) Groups run routine

EN3^PRSEED4

This option allows creating or editing of the PRSE Mandatory Training (MI)

Class Group file (#452.3).

PRSE-MI-LIST

Employee Mandatory Training Group/Class Report run routine

EN1^PRSEPMC

This report shows the mandatory training groups and classes associated with

an employee. The report may be printed for selected employees or all

employees in a given service. Data is printed from the PAID Employee file

(#450).

PRSE-MI-MULT

Quick Mandatory Training (MI) Update run routine

EN1^PRSEED14

This option allows an easy way to enter data for multiple Mandatory Training

\(MI\) classes and multiple employees who attended those classes.

PRSE-MIEX

Enter/Edit Mandatory Training (MI/Expanded) run routine

EN2^PRSEED0

This option allows the creation and editing of a mandatory training

program/class which contains information to complete OLDE reporting

requirements.

PRSE-NCEATTEND

Create Non-Local CE and Enter Attendance run routine

EN1^PRSEED10

This option allows the user to create and edit continuing education class

information for courses not presented at the medical facility. Attendance

for theses classes is entered through this option along with the cost and

leave information.

PRSE-O.I.

Enter/Edit Other/Miscellaneous Training run routine

EN6^PRSEED0

This option allows the user to create and edit miscellaneous training

programs/classes which are not categorized as required classes, continuing

education, or location specific classes.

PRSE-OLDE

OLDE Training Coding Report run routine

EN1^PRSEPOL0

This option prints a report of class information in OLDE coding order. The

report may be printed for all or selected employees in a specific service or

the entire facility. A date range is also prompted for. The report is

sorted by social security number.

PRSE-P-CAL

Class Registration Calendar Report run routine

EN1^PRSECAL

This option prints a listing of present and future classes by date or class

title.

PRSE-P-RSTR

Class Registration Roster Report run routine

EN1^PRSERSTR

This option prints a roster of students registered for a class session by

service, title, employee, and social security number.

PRSE-PRT

Reports Menu menu

PRSE-EMP

PRSE-P-RSTR

PRSE-P-CAL

PRSE-DEMP

PRSE-MI-LIST

PRSE-OLDE

PRSE-IND-CLS

PRSE-IND-DEMP

This menu allows the user to print class reports.

PRSE-SITE

Package Set-up Menu menu

PRSE-ACC

PRSE-EMP-MI

PRSE-CLAS

PRSE-MAN

PRSE-SOR

PRSE-SUP

PRSE-EE-SVC

This menu allows the user to enter or edit data in the software's site

files.

PRSE-SOR

Presentation Media run routine

EN4^PRSEED4

This option allows the user to enter or edit information in the PRSE

Education Presentation Media file (#452.5).

PRSE-STU-PURG

Purge Student Tracking File run routine

EN1^PRSEDEL

This option purges data from the PRSE Student Education Tracking file (#452)

for dates specified by the user.

PRSE-SUP

Presenter/Supplier run routine

EN2^PRSEED4

This option allows the user to enter or edit information in the PRSE

Education Program/Class Supplier file (#452.2).

PRSE-SYS-MGR

Education Tracking System Menu menu

PRSE-CORD

PRSE-IRM

PRSE-INS-MENU

This is the main menu for the Employee Education Tracking Module. All

options can be accessed through this menu.

PRSE-W.I.

Enter/Edit Ward/Unit-Location Training run routine

EN5^PRSEED0

This option allows the user to create and edit training programs/classes

associated with a specific medical facility location.

PRSR-SYSTEM-PAID REPORTS

Paid Resource Management Reports menu

PRSRFI-PAID SYSTEM REPORTS

PRSRSU-PAID SYSTEM REPORTS

PRSREM-LEV-USED

This is the main menu for all Paid Resource Management Reports.

PRSREM-LEV-USED

Display Leave Used run routine

EMP^PRSRL1

This option displays the leave used by an employee for a given date range.

PRSRFI-EXP

Expenditures run routine

FIS^PRSREX1

This report prints expenditures for one or more T&L(s), for one or all pay

periods during a <span id="typo" class="anchor"></span>chosen year. Sub-totals and Totals are also printed.

PRSRFI-LEV-USED

Employee Leave Used run routine

FIS^PRSRL1

This report prints all leave used by one or all employee(s) over a selected

date range.

PRSRFI-OT/CT

Employee Overtime/CompTime Report run routine

FIS^PRSROT1

This report prints the overtime and compensation time for one or more

T&L(s), for one or all employee(s), for one or all pay periods.

PRSRFI-PAID SYSTEM REPORTS

Employee Reports menu

PRSRFI-EXP

PRSRFI-LEV-USED

PRSRFI-OT/CT

PRSRFI-PPA-RPT

PRSRFI-T&L-RPT

This is the main menu for displaying or printing the Paid Resource Management Reports.

PRSRFI-PPA-RPT

Employee Prior Pay Period Adjustments run routine

FIS^PRSRAU1

This report prints the employee leave audit(s) for one or more T&L(s) over a

selected date range.

PRSRFI-T&L-RPT

Paid T&L Report run routine

FIS^PRSRTLPR

This option prints a T&L report for one (1) T&L or all T&L(s).

PRSRSU-EXP

Expenditures run routine

SUP^PRSREX1

This report prints expenditures for one (1) or all T&L(s) assigned to the

user, for one (1) or all pay periods for a chosen year. Sub-totals and

totals are also printed.

PRSRSU-LEV-MENU

Employee Leave Reports menu

PRSRSU-LEV-USED

PRSRSU-LEV-REQ

PRSRSU-LEV-PATR

This is the main menu for employee leave reports.

PRSRSU-LEV-PATR

Employee Leave Pattern run routine

SUP^PRSRL4

This report prints leave used by an employee showing a pattern over a

selected date range.

PRSRSU-LEV-REQ

Employee Leave Requested run routine

SUP^PRSRL2

This report prints all leave requested by one (1) or all employees under a

users T&L(s) over a selected date range.

PRSRSU-LEV-USED

Employee Leave Used run routine

SUP^PRSRL1

This report prints all leave used by one (1) or all employee(s) under a

users T&L over a selected date range.

PRSRSU-OT/CT

Employee Overtime/CompTime Report run routine

SUP^PRSROT1

This report prints the overtime and compensation time that an employee(s)

has taken over one pay period or all pay periods during a calendar year.

The employees T&L must be assigned to the user.

PRSRSU-PAID SYSTEM REPORTS

Paid Employee Reports (Sup) menu

PRSRSU-PPA-RPT

PRSRSU-EXP

PRSRSU-LEV-MENU

PRSRSU-OT/CT

This is the main option for displaying or printing the Paid Resource

Management Reports.

PRSRSU-PPA-RPT

Employee Prior Pay Period Adjustments run routine

SUP^PRSRAU1

This report prints the employee leave audit(s) for one or more T&L(s) over a

selected date range.

# Options Not Assigned to Any Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Process Unprocessed Download Data \[PRSD PROCESS PRS (STARTUP)\]

This option will process any leftover master record download data in the PRS global and will automatically run at system startup time.

Download Employee Data \[PRSD\]

This server option receives employee master record from the AAC and stores that data into the PAID EMPLOYEE (#450) and/or PAID PAYRUN DATA (#459) file.

Supervisor Alerts \[PRSA SUP ALERTS\]

This option is invoked by the sign-on security package and will display any requests requiring certification, in the case of supervisors, or any OT/CT requests or prior pay period adjustments requiring approval in the case of Approvers.

Decompose Time \[PRSA PAY DECOMP\]

This option allows the user to select a pay period and an employee. The data on that time and attendance report is checked by a series of computer routines that applies Payroll rules and builds an 8B record that will be sent to the Austin Automation Center (AAC). The pay period, employee's name, social security number, time and attendance "stub record", and any data values that will be sent to the AAC are displayed.

T&L Decomposition Report \[PRSA T&L DECOMP REPORT\]

This option allows the user to select one or more Time and Leave Units (T&Ls) for a pay period and to decompose (create an 8B record) or merely list the time and attendance status.

Cross References

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 46%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>-----------------</p></td>
<td><p>FIELD</p>
<p>--------------------------</p></td>
<td><p>X-REF</p>
<p>------------</p></td>
<td><p>DESCRIPTION</p>
<p>-----------------------------------------------------</p></td>
</tr>
<tr class="even">
<td>450</td>
<td>SSN</td>
<td>AC</td>
<td>Maintains pointers in both 200 and 450 files based on SSN.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450</td>
<td><p>COST CENTER/</p>
<p>ORGANIZATION</p></td>
<td>ACC</td>
<td>The COST CENTER/ORGANIZ-ATION value. Set for current employees only.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450</td>
<td>EMPLOYEE NAME</td>
<td>ATL1</td>
<td>By T&amp;L UNIT and by EMPLOYEE NAME within T&amp;L UNIT with the letters ATL concatenated to the T&amp;L value (e.g., ATL001). The ATL1 and ATL cross references create a single (ATL) cross reference. If either field value is changed, the ATL cross reference will be updated.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450</td>
<td>EMPLOYEE NAME</td>
<td>BS1</td>
<td>First letter of EMPLOYEE NAME concatenated with the last four digits of SSN. The BS and BS1 cross references create a single (BS) cross reference. If either field value is changed, the BS cross reference will be updated.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>450</td>
<td>T&amp;L UNIT</td>
<td>ATL</td>
<td>By T&amp;L UNIT and by EMPLOYEE NAME within T&amp;L UNIT.</td>
</tr>
</tbody>
</table>

|     |                 |     |                                                                                          |
|-----|-----------------|-----|------------------------------------------------------------------------------------------|
| 450 | SSN             | BS  | First letter of EMPLOYEE NAME concatenated with the last four digits of SSN.             |
| 450 | SSN             | SSN | Employee's Social Security Number (without dashes).                                      |
|     |                 |     |                                                                                          |
| 450 | MANDATORY CLASS | AMC | This is used by Education Tracking to find all individuals with a given MANDATORY CLASS. |
| 450 | MI REVIEW GROUP | ARG | This is used by Education Tracking to find all individuals with a given MI REVIEW GROUP. |

|        |             |        |                                                                                                                      |
|--------|-------------|--------|----------------------------------------------------------------------------------------------------------------------|
| 450    | OLD 450 IEN | OLDIEN | OLD 450 IEN field. The value of OLD 450 IEN is the Internal Entry Number prior to dinuming the 450 File to File 200. |
| 450.12 | TYPE        | C      | PAID Download Type-Date-Station Number-Sequence Number.                                                              |

|       |                            |          |                                                                                                                                                                                                          |
|-------|----------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 452   | STUDENT NAME               | AB       | Indicates the latest time/date a particular type of inservice class was taken. It includes the class type, the class, the \#200 File pointer for the employee, and the inverse start date for the class. |
| 452   | PROGRAM/ CLASS TITLE       | AC       | Indicates the latest time/date a particular type of inservice class was taken. It includes the class type, the class, the \#200 File pointer for the employee, and the inverse start date for the class. |
| 452   | BEGINNING DATE             | AD       | Indicates the latest time/date a particular type of inservice class was taken. It includes the class type, the class, the \#200 File pointer for the employee, and the inverse start date for the class. |
| 452   | STUDENT NAME               | AE       | Indexes continuing education classes by type (local/non-local).                                                                                                                                          |
| 452   | PROGRAM/ CLASS TITLE       | AF       | Indexes Student Tracking File entries by each class/date occurrence.                                                                                                                                     |
| 452   | PROGRAM/ CLASS TITLE       | AK       | This is used to look up each class which has been entered in the Education Tracking File.                                                                                                                |
| 452   | BEGINNING DATE             | AL       | Indexes Student Tracking File entries by class/date occurrence.                                                                                                                                          |
| 452   | PROGRAM/ CLASS TITLE       | CLS      | This is an inverted date MUMPS cross reference by class/date.                                                                                                                                            |
| 452   | BEGINNING DATE             | D        | This is an inverted date MUMPS cross reference by class/date.                                                                                                                                            |
| 452   | PROGRAM/ CLASS TITLE       | D1       | This is an inverted date MUMPS cross reference by class/date.                                                                                                                                            |
| 452   | PROGRAM/ CLASS TITLE       | E        | Indicates the latest time/date a particular type of inservice class was taken. It includes the class type, the class, the \#200 File pointer for the employee, and the inverse start date for the class. |
| 452   | BEGINNING DATE             | H        | Indexes Student Tracking File entries by beginning date.                                                                                                                                                 |
| 452   | LOCAL NON-LOCAL            | LOC1     | Indexes continuing education classes by type (local-non/local) employee, and internal entry number.                                                                                                      |
| 452   | TYPE OF EDUCATION          | F        | Indicates the latest time/date a particular type of inservice class was taken. It includes the class type, the class, the \#200 File pointer for the employee, and the inverse start date for the class. |
| 452   | TYPE OF EDUCATION          | LOC2     | Indexes continuing education classes by type (local-non/local) employee, and internal entry number.                                                                                                      |
| 452   | SERVICE/ SECTION/ LOCATION | SER      | Indexes Student Tracking File entries by employee service.                                                                                                                                               |
| 452.1 | TYPE OF EDUCATION          | C        | Used to sort/lookup inservice class types.                                                                                                                                                               |
| 452.1 | SERVICE                    | TRIG-GER | This trigger updates the sponsoring service field in the PRSE Education Registration File (452.8).                                                                                                       |

|         |                             |      |                                                                                |
|---------|-----------------------------|------|--------------------------------------------------------------------------------|
| 452.3   | MANDATORY CLASSES           | C    | Indexes mandatory training group entries by group/class name.                  |
| 452.3   | SERVICE                     | D    | By service; contains a pointer value for File 454.1.                           |
| 452.4   | PAID CODE                   | CODE | Index of Program Category File entries by PAID code.                           |
| 452.4   | SERVICE                     | SER  | Pointer to Service File (49).                                                  |
| 452.51  | PAID CODE                   | CODE | Indexes file entries by PAID code.                                             |
| 452.8   | CLASS NAME                  | AA01 | Indexes file entries by service/class.                                         |
| 452.8   | SPONSORING SERVICE/ SECTION | AA27 | Indexes file entries by service/class.                                         |
| 452.889 | START DATE/ TIME OF CLASS   | C    | MUMPS inverted time/date X-Ref placing latest date first.                      |
| 455.5   | OT/CT APPROVER              | AA   | By user of all T&L Units for which the user is an Overtime/Comp Time approver. |

|       |                                |     |                                                                         |
|-------|--------------------------------|-----|-------------------------------------------------------------------------|
| 455.5 | SUPERVISOR                     | AS  | By user of all T&L Units of which the user is a supervisor.             |
| 455.5 | T&L WHICH CERTIFIES SUPERVISOR | ASX | The T&L Unit which certifies a supervisor's time and attendance report. |

|       |                |     |                                                                                                                       |
|-------|----------------|-----|-----------------------------------------------------------------------------------------------------------------------|
| 455.5 | TIMEKEEPER     | AT  | By user of all T&L Units for which this user is a timekeeper.                                                         |
|       |                |     |                                                                                                                       |
| 457.1 | DESCRIPTION    | C   | Free text description of the tour of duty.                                                                            |
| 457.2 | NAME           | AC  | A form of a trigger and forces the internal number of the entry into the CODE field as data.                          |
| 457.2 | UPPERCASE NAME | C   | The NAME field value of the entry spelled out in uppercase letters. Triggered by the NAME field.                      |
|       |                |     |                                                                                                                       |
| 457.2 | CODE           | D   | The internal number of the entry.                                                                                     |
|       |                |     |                                                                                                                       |
| 457.4 | CODE           | C   | The internal number of the entry.                                                                                     |
|       |                |     |                                                                                                                       |
| 457.4 | UPPERCASE NAME | D   | The DESCRIPTION field value of the entry spelled out in uppercase letters. Triggered by the DESCRIPTION field.        |
| 457.5 | CODE           | AC  | The first 3 to 4 characters of a pay entitlement character string.                                                    |
| 458   | DATE 1         | AD1 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
| 458   | DATE 2         | AD2 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
| 458   | DATE 3         | AD3 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
| 458   | DATE 4         | AD4 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
| 458   | DATE 5         | AD5 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |

|     |         |      |                                                                                                                       |
|-----|---------|------|-----------------------------------------------------------------------------------------------------------------------|
| 458 | DATE 6  | AD6  | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 7  | AD7  | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 8  | AD8  | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 9  | AD9  | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 10 | AD10 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 11 | AD11 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |
|     |         |      |                                                                                                                       |
| 458 | DATE 12 | AD12 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference. |

|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
|-------|----------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 458   | DATE 13              | AD13 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference.                                                                                                                                                                                           |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458   | DATE 14              | AD14 | This allows a program to determine the pay period day number by looking up a specific date in the AD cross-reference.                                                                                                                                                                                           |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458   | PRIOR SCHEDULED TOUR | ATC  | This is set to indicate to the super-visor that a tour change has occurred and must be approved. In the special case where a prior tour has yet to be approved (& the cross-reference is already set) and a new change super-cedes the prior change, the cross-reference is not set as it has already been set. |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458   | STATUS               | AX   | This sets an AXR for requested correction entries, AXS for supervisor approved entries, and AXA for final approved entries.                                                                                                                                                                                     |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458.1 | FROM DATE            | AD1  | This uses the inverse of field 4 (the ending date) as a subscript, and this field (the starting date), as data.                                                                                                                                                                                                 |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458.1 | TO DATE              | AD2  | This uses the inverse of this field (the ending date) as a subscript, and field 2 (the starting date) as data.                                                                                                                                                                                                  |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458.1 | STATUS               | AR   | Only those entries with a status of R. No other status value is cross-referenced.                                                                                                                                                                                                                               |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458.1 | EMPLOYEE             | C    | The employee's internal entry number in File 450.                                                                                                                                                                                                                                                               |
|       |                      |      |                                                                                                                                                                                                                                                                                                                 |
| 458.2 | REQUESTED WORK DATE  | AD   | By employee, date and sequence \# for the OT/CT request.                                                                                                                                                                                                                                                        |

|       |           |     |                                                                                                     |
|-------|-----------|-----|-----------------------------------------------------------------------------------------------------|
| 458.2 | STATUS    | AR  | This is a cross-reference of only those entries with a status of R.                                 |
| 458.2 | STATUS    | AS  | This is a cross-reference of only those entries with a status of S.                                 |
| 458.2 | EMPLOYEE  | C   | The employee's internal entry number in File 450.                                                   |
| 458.3 | FROM DATE | AD  | By employee's internal entry number in File 450 and by reverse order of FROM DATE (FileMan format). |
|       |           |     |                                                                                                     |
| 458.3 | STATUS    | AR  | Only those entries with a status of R for requested.                                                |
|       |           |     |                                                                                                     |
| 458.3 | EMPLOYEE  | C   | The employee's internal entry number in File 450.                                                   |
| 458.5 | EMPLOYEE  | C   | The employee's internal entry number in File 450.                                                   |

|     |          |     |                                           |
|-----|----------|-----|-------------------------------------------|
| 459 | PAY DATE | AC  | The official pay date for the pay period. |

File Diagram (PRS)

Files included: 450 PAID EMPLOYEE

450.11 PAID DOWNLOAD MESSAGE ERROR

450.12 PAID DOWNLOAD MESSAGE

452 PRSE STUDENT EDUCATION TRACKING

452.1 PRSE PROGRAM/CLASS

452.2 PRSE EDUCATION PROGRAM/CLASS SUPPLIER

452.3 PRSE MANDATORY TRAINING (MI) CLASS GROUP

452.4 PRSE EDUCATION PROGRAM/CLASS CATEGORY

452.5 PRSE EDUCATION PRESENTATION MEDIA

452.51 PRSE EMPLOYEE PURPOSE OF TRAINING

452.6 PRSE SVC REASONS FOR TRAINING

452.7 PRSE PARAMETER

452.8 PRSE EDUCATION REGISTRATION

452.9 PRSE EDUCATION ACCREDITATION ORGANIZATIONS

454 PAID CODE FILES

454.1 PAID COST CENTER/ORGANIZATION

455.1 8B ERROR MESSAGE

455.5 T&L UNIT

457.1 TOUR OF DUTY

457.2 SPECIAL TOUR INDICATOR

457.3 TYPE OF TIME

457.4 TIME REMARKS

457.5 PAY ENTITLEMENT

457.6 ENVIRONMENTAL DIFFERENTIALS

458 TIME & ATTENDANCE RECORDS

458.1 LEAVE REQUESTS

458.2 OT/CT REQUESTS

458.3 ENVIRONMENTAL DIFF. REQUESTS

458.5 PRIOR PP EXCEPTIONS

459 PAID PAYRUN DATA

FILE (#) POINTER (#) FILE

POINTER FIELD TYPE POINTER FIELD FILE POINTED TO

--------------------------------------------------------------------------------

L=Laygo S=File not in set N=Normal Ref. C=Xref.

\*=Truncated m=Multiple v=Variable Pointer

---------------------

NEW PERSON (#200) \| \|

PAID EMPLOYEE ........ (N S )-\> \| 450 PAID EMPLOY\* \|

TIME & ATTENDANCE RE (#458.01) \| \|

EMPLOYEE ............. (N )-\> \| NEW PERSON \|-\> NEW PERSON

LEAVE REQUESTS (#458.1) \| \|

EMPLOYEE ............. (N C )-\> \| m MI REV:MI REV\* \|-\> PRSE MANDATORY \*

OT/CT REQUESTS (#458.2) \| \|

EMPLOYEE ............. (N C )-\> \| m MANDAT:MANDAT\* \|-\> PRSE PROGRAM/CL\*

ENVIRONMENTAL DIFF. (#458.3) \| \|

EMPLOYEE ............. (N C )-\> \| \|

PRIOR PP EXCEPTIONS (#458.5) \| \|

EMPLOYEE ............. (N C )-\> \| \|

PAID PAYRUN DATA (#459.01) \| \|

EMPLOYEE:NAME ........ (N )-\> \| \|

---------------------

---------------------

\| 452 PRSE STUDEN\* \|

\| STUDENT NAME \|-\> NEW PERSON

\| PROGRAM/CLASS \* \|-\> PRSE EDUCATION \*

\| PURPOSE OF TRA\* \|-\> PRSE EMPLOYEE P\*

\| ACCREDITING OR\* \|-\> PRSE EDUCATION \*

\| m SVC RE:SVC RE\* \|-\> PRSE SVC REASON\*

---------------------

---------------------

PAID EMPLOYEE (#450.0633) \| \|

MANDATORY CLASS ...... (N C )-\> \| 452.1 PRSE PROG\* \|

PRSE EDUCATION PROGR (#452.25) \| \|

PROGRAM/CLASS ........ (N )-\> \| SERVICE \|-\> PAID COST CENTE\*

PRSE MANDATORY TRAIN (#452.31) \| \|

M.I. PROG:MANDATORY C\* (N )-\> \| \|

PRSE EDUCATION PROGR (#452.42) \| \|

PROGRAM/CLASS ........ (N )-\> \| \|

PRSE EDUCATION REGIS (#452.8) \| \|

CLASS NAME ........... (N C L)-\> \| \|

---------------------

---------------------

\| 452.2 PRSE EDUC\* \|

\| STATE \|-\> STATE

\| PROGRA:PROGRA\* \|-\> PRSE PROGRAM/CL\*

---------------------

---------------------

PAID EMPLOYEE (#450.0632) \| \|

MI REVIEW GROUP ...... (N C )-\> \| 452.3 PRSE MAND\* \|

\| SERVICE \|-\> PAID COST CENTE\*

\| m M.I. P:MANDAT\* \|-\> PRSE PROGRAM/CL\*

---------------------

---------------------

PRSE STUDENT EDUCATI (#452) \| \|

PROGRAM/CLASS CATEGORY (N )-\> \| 452.4 PRSE EDUC\* \|

PRSE EDUCATION REGIS (#452.8) \| \|

CLASS CATEGORY ....... (N )-\> \| SERVICE \|-\> SERVICE/SECTION

\| USER \|-\> NEW PERSON

\| m PROGRA:PROGRA\* \|-\> PRSE PROGRAM/CL\*

---------------------

---------------------

PRSE EDUCATION REGIS (#452.8) \| \|

TYPE OF MEDIA ........ (N )-\> \| 452.5 PRSE EDUC\* \|

---------------------

---------------------

PRSE STUDENT EDUCATI (#452) \| \|

PURPOSE OF TRAINING .. (N )-\> \| 452.51 PRSE EMP\* \|

PRSE EDUCATION REGIS (#452.8) \| \|

PURPOSE OF CLASS ..... (N )-\> \| \|

---------------------

---------------------

PRSE STUDENT EDUCATI (#452.033) \| \|

SVC REASON ........... (N C )-\> \| 452.6 PRSE SVC \* \|

PRSE EDUCATION REGIS (#452.877) \| \|

SERVICE REASON FOR CLA\* (N C )-\> \| \|

---------------------

---------------------

\| 452.8 PRSE EDUC\* \|

\| CLASS NAME \|-\> PRSE PROGRAM/CL\*

\| TYPE OF MEDIA \|-\> PRSE EDUCATION \*

\| SPONSORING SER\* \|-\> PAID COST CENTE\*

\| ACCREDITING OR\* \|-\> PRSE EDUCATION \*

\| CLASS CATEGORY \|-\> PRSE EDUCATION \*

\| PURPOSE OF CLA\* \|-\> PRSE EMPLOYEE P\*

\| m SERVIC:SERVIC\* \|-\> PRSE SVC REASON\*

\| m STAR:STUD:STUD\* \|-\> NEW PERSON

---------------------

---------------------

PRSE STUDENT EDUCATI (#452) \| \|

ACCREDITING ORGANIZATI\* (N )-\> \| 452.9 PRSE EDUC\* \|

PRSE EDUCATION REGIS (#452.8) \| \|

ACCREDITING ORGANIZATI\* (N )-\> \| STATE \|-\> STATE

---------------------

---------------------

PRSE PROGRAM/CLASS (#452.1) \| \|

SERVICE .............. (N )-\> \| 454.1 PAID COST\* \|

PRSE MANDATORY TRAIN (#452.3) \| \|

SERVICE .............. (N C )-\> \| \|

PRSE EDUCATION REGIS (#452.8) \| \|

SPONSORING SERVICE/SEC\* (N C )-\> \| \|

PAID CODE FILES (#454.94) \| \|

COST CENT:DESCRIPTION\* (N )-\> \| \|

---------------------

---------------------

TOUR OF DUTY (#457.13) \| \|

ASSOCIATED T&L UNIT .. (N )-\> \| 455.5 T&L UNIT \|

\| SERVICE \|-\> SERVICE/SECTION

\| TIMEKE:TIMEKE\* \|-\> NEW PERSON

\| SUPERV:SUPERV\* \|-\> NEW PERSON

\| OT/CT :OT/CT \* \|-\> NEW PERSON

---------------------

---------------------

TIME & ATTENDANCE RE (#458.01) \| \|

EMPLOYEE:TMP 1 ....... (N )-\> \| 457.1 TOUR OF D\* \|

EMPLOYEE:TMP 2 ....... (N )-\> \| SPECIAL CODE-1 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 3 ....... (N )-\> \| SPECIAL CODE-2 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 4 ....... (N )-\> \| SPECIAL CODE-3 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 5 ....... (N )-\> \| SPECIAL CODE-4 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 6 ....... (N )-\> \| SPECIAL CODE-5 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 7 ....... (N )-\> \| SPECIAL CODE-6 \|-\> SPECIAL TOUR IN\*

EMPLOYEE:TMP 8 ....... (N )-\> \| m ASSOCI:ASSOCI\* \|-\> T&L UNIT

EMPLOYEE:TMP 9 ....... (N )-\> \| \|

EMPLOYEE:TMP 10 ...... (N )-\> \| \|

EMPLOYEE:TMP 11 ...... (N )-\> \| \|

EMPLOYEE:TMP 12 ...... (N )-\> \| \|

EMPLOYEE:TMP 13 ...... (N )-\> \| \|

EMPLOYEE:TMP 14 ...... (N )-\> \| \|

EMPLO:DAY \#:TOUR OF\* . (N )-\> \| \|

EMPLO:DAY \#:PRIOR S\* . (N C )-\> \| \|

EMPLO:DAY \#:SECOND \* . (N )-\> \| \|

---------------------

---------------------

TOUR OF DUTY (#457.1) \| \|

SPECIAL CODE-1 ....... (N )-\> \| 457.2 SPECIAL T\* \|

SPECIAL CODE-2 ....... (N )-\> \| \|

SPECIAL CODE-3 ....... (N )-\> \| \|

SPECIAL CODE-4 ....... (N )-\> \| \|

SPECIAL CODE-5 ....... (N )-\> \| \|

SPECIAL CODE-6 ....... (N )-\> \| \|

TIME & ATTENDANCE RE (#458.02) \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#1\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

EMPLO:DAY \#:TOUR \#2\* . (N )-\> \| \|

---------------------

---------------------

TIME & ATTENDANCE RE (#458.02) \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| 457.4 TIME REMA\* \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

EMPLO:DAY \#:WRK SPE\* . (N )-\> \| \|

---------------------

---------------------

TIME & ATTENDANCE RE (#458.01) \| \|

EMPLOYEE:ENTITLEMENT . (N )-\> \| 457.5 PAY ENTIT\* \|

---------------------

---------------------

TIME & ATTENDANCE RE (#458.01) \| \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| 457.6 ENVIRONME\* \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| \|

EMPLOYEE:ENVIR. DIFF\* (N )-\> \| \|

ENVIRONMENTAL DIFF. (#458.3) \| \|

TYPE OF EXPOSURE ..... (N )-\> \| \|

---------------------

---------------------

\| 458 TIME & ATTE\* \|

\| TRANSMITTING C\* \|-\> NEW PERSON

\| EMPLOY:EMPLOY\* \|-\> PAID EMPLOYEE

\| EMPLOY:APP. S\* \|-\> NEW PERSON

\| EMPLOY:ENTITL\* \|-\> PAY ENTITLEMENT

\| EMPLOY:VCS PO\* \|-\> NEW PERSON

\| EMPLOY:VCS AP\* \|-\> NEW PERSON

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOY:ENVIR.\* \|-\> ENVIRONMENTAL D\*

\| EMPLOYEE:TMP 1 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 2 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 3 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 4 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 5 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 6 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 7 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 8 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 9 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 10 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 11 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 12 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 13 \|-\> TOUR OF DUTY

\| EMPLOYEE:TMP 14 \|-\> TOUR OF DUTY

\| EMPL:DAY :TOUR\* \|-\> TOUR OF DUTY

\| EMPL:DAY :PRIO\* \|-\> TOUR OF DUTY

\| EMPL:DAY :SUPE\* \|-\> NEW PERSON

\| EMPL:DAY :TOUR\* \|-\> NEW PERSON

\| EMPL:DAY :SECO\* \|-\> TOUR OF DUTY

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :TOUR\* \|-\> SPECIAL TOUR IN\*

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :WRK \* \|-\> TIME REMARKS

\| EMPL:DAY :TIME\* \|-\> NEW PERSON

\| MESSAG:MESSAG\* \|-\> MESSAGE

---------------------

---------------------

\| 458.1 LEAVE REQ\* \|

\| EMPLOYEE \|-\> PAID EMPLOYEE

\| ENTERED BY \|-\> NEW PERSON

\| SUPERVISOR \|-\> NEW PERSON

\| EMPL:AUDI:PERS\* \|-\> NEW PERSON

\| EMPL:AUDI:CLEA\* \|-\> NEW PERSON

\| EMPL:AUDI:APPR\* \|-\> NEW PERSON

\| EMPL:AUDI:APP.\* \|-\> NEW PERSON

---------------------

---------------------

\| 458.2 OT/CT REQ\* \|

\| EMPLOYEE \|-\> PAID EMPLOYEE

\| ENTRY PERSON \|-\> NEW PERSON

\| SUPERVISOR \|-\> NEW PERSON

\| APPROVER \|-\> NEW PERSON

---------------------

---------------------

\| 458.3 ENVIRONME\* \|

\| EMPLOYEE \|-\> PAID EMPLOYEE

\| TYPE OF EXPOSU\* \|-\> ENVIRONMENTAL D\*

\| ENTERED BY \|-\> NEW PERSON

\| SUPERVISOR \|-\> NEW PERSON

---------------------

---------------------

\| 458.5 PRIOR PP \* \|

\| EMPLOYEE \|-\> PAID EMPLOYEE

\| CLEARING CLERK \|-\> NEW PERSON

---------------------

---------------------

\| 459 PAID PAYRUN\* \|

\| m EMPLOYEE:NAME \|-\> PAID EMPLOYEE

---------------------

Archiving and Purging

No archiving or purging capability exists for this version.

Callable Routines

No externally callable routines are presently supported.

External Relations

This version requires Kernel V. 7.0 or greater and VA FileMan V. 21 or greater.

PAID V. 4.0 has an Integration Agreement, DBIA1262, with Kernel to create a new field (PAID EMPLOYEE \#450) in the New Person file \#200.

All routines are essential to the function of this package. The alert feature requires Kernel V. 8 to operate but all other features are operable with earlier versions.

Internal Relations

The menus were designed for direct assignment. No single option from the menus should be assigned independently as some of the security features of the package are maintained by the menu structure.

Package-wide Variables

None.

How to Generate On-line Documentation

The namespace for this package is PRS. All globals, keys, options and routines begin with PRS.

The file range is 450 to 459.99. See the FILE LIST section for an exact listing of files. Data dictionaries for these files may be generated through Option 8 of VA FileMan (LIST FILE ATTRIBUTES).

On-line documentation for the package is provided throughout the program. At any time you become unsure of how to respond to a prompt, simply enter a question mark(s).

A file diagram for the package can be generated by invoking the routine DDMAP (i.e., D ^DDMAP).

National Package Security

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td>FILE NAME</td>
<td><p>D</p>
<p>D</p></td>
<td><p>R</p>
<p>E</p>
<p>A</p>
<p>D</p></td>
<td><p>W</p>
<p>R</p>
<p>I</p>
<p>T</p>
<p>E</p></td>
<td><p>D</p>
<p>E</p>
<p>L</p>
<p>E</p>
<p>T</p>
<p>E</p></td>
<td><p>L</p>
<p>A</p>
<p>Y</p>
<p>G</p>
<p>O</p></td>
</tr>
<tr class="even">
<td>450</td>
<td>PAID EMPLOYEE</td>
<td>@</td>
<td>#</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>450.11</td>
<td>PAID DOWNLOAD MESSAGE ERROR</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>450.12</td>
<td>PAID DOWNLOAD MESSAGE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452</td>
<td>PRSE STUDENT EDUCATION TRACKING</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>452.1</td>
<td>PRSE PROGRAM/CLASS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452.2</td>
<td>PRSE EDUCATION PROGRAM/CLASS SUPPLIER</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>452.3</td>
<td>PRSE MANDATORY TRAINING (MI) CLASS GROUP</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452.4</td>
<td>PRSE EDUCATION PROGRAM/CLASS CATEGORY</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>452.5</td>
<td>PRSE EDUCATION PRESENTATION MEDIA</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452.51</td>
<td>PRSE EMPLOYEE PURPOSE OF TRAINING</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>452.6</td>
<td>PRSE SVC REASONS FOR TRAINING</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452.7</td>
<td>PRSE PARAMETERS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>452.8</td>
<td>PRSE EDUCATION REGISTRATION</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>452.9</td>
<td>PRSE EDUCATION ACCREDITATION ORGANIZATIONS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>454</td>
<td>PAID CODE FILE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>454.1</td>
<td>PAID COST CENTER/ORGANIZATION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>455.1</td>
<td>8B ERROR MESSAGE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>455.5</td>
<td>T&amp;L UNIT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>457.1</td>
<td>TOUR OF DUTY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>457.2</td>
<td>SPECIAL TOUR INDICATOR</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>457.3</td>
<td>TYPE OF TIME</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td>FILE NAME</td>
<td><p>D</p>
<p>D</p></td>
<td><p>R</p>
<p>E</p>
<p>A</p>
<p>D</p></td>
<td><p>W</p>
<p>R</p>
<p>I</p>
<p>T</p>
<p>E</p></td>
<td><p>D</p>
<p>E</p>
<p>L</p>
<p>E</p>
<p>T</p>
<p>E</p></td>
<td><p>L</p>
<p>A</p>
<p>Y</p>
<p>G</p>
<p>O</p></td>
</tr>
<tr class="even">
<td>457.4</td>
<td>TIME REMARKS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>457.5</td>
<td>PAY ENTITLEMENT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>457.6</td>
<td>ENVIRONMENTAL DIFFERENTIALS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>458</td>
<td>TIME &amp; ATTENDANCE RECORDS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>458.1</td>
<td>LEAVE REQUESTS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>458.2</td>
<td>OT/CT REQUESTS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>458.3</td>
<td>ENVIRONMENTAL DIFF. REQUESTS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>458.5</td>
<td>PRIOR PP EXCEPTIONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>459</td>
<td>PAID PAYRUN DATA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     |                 |                                                                                                                                                                                                     |
|-----|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | PRSA SIGN       | This key is meant for Directors only. It allows Directors to sign their own time and attendance reports.                                                                                            |
|     | PRSD PAID CODES | This key allows the user to edit the various PAID CODE FILE (#454) entries. Personnel Service, Record Section and Fiscal Service, Payroll Section supervisors who request this key may be given it. |

|     |            |                                                                                                                                                                                           |
|-----|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | PRSE CORD  | This key allows the user to see data for all services. It also allows the user to register and enter attendance for anyone in an open or closed class regardless of service.              |
|     |            |                                                                                                                                                                                           |
|     | PRSE SUP   | This key allows the user to see data for his/her own service. It also allows the user to register and enter attendance for any individual in a closed class sponsored by his/her service. |
|     |            |                                                                                                                                                                                           |
|     | PRSE TRAIN | This key is meant for Nursing Service personnel only. It allows the user to see data only for his/her own Nursing location.                                                               |

# Privacy Act Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data stored in Files 450, 458, and 459 is subject to the Privacy Act.

# Additional Data Field Security for File 450

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each field in File 450 contains a node, ^DD(450,field number,8), that has either a capital letter P or F or both. The letter P means only Personnel Service employees may look at the field and the letter F means only Fiscal Service employees may look at the field. Both letters mean both Services may look at the field. When using the print or search options of the PRSD 04 EMPLOYEE INQUIRY MENU or PRSD 05 EMPLOYEE INQUIRY MENU, this node is checked before allowing the user to view the fields in File 450.

# Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Time and Attendance portion of the software requires an electronic signature to approve overtime/compensatory requests, leave requests, Veterans Canteen Service commission sales, environmental differential pay requests, tour of duty changes and Time and Attendance Report certification.

Glossary

|                  |                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAC              | Austin Automation Center                                                                                                                                                                                                                |
|                  |                                                                                                                                                                                                                                         |
| Access Code      | A unique sequence of characters assigned to the user by the System Manager. The access code (in conjunction with the verify code) is used by the computer to identify authorized users, and should not be revealed to any other person. |
|                  |                                                                                                                                                                                                                                         |
| Biweekly         | Two consecutive calendar weeks.                                                                                                                                                                                                         |
|                  |                                                                                                                                                                                                                                         |
| Data Dictionary  | A description of the file structure and data elements within a file.                                                                                                                                                                    |
|                  |                                                                                                                                                                                                                                         |
| Decomposition    | Process that applies coded payroll rules to posted time and attendance report data and creates an 8B record.                                                                                                                            |
|                  |                                                                                                                                                                                                                                         |
| DHCP             | Decentralized Hospital Computer Program.                                                                                                                                                                                                |
|                  |                                                                                                                                                                                                                                         |
| Download         | Used here to refer to data generated by the AAC and sent via MailMan to the station.                                                                                                                                                    |
|                  |                                                                                                                                                                                                                                         |
| Edit & Update    | A type of download used to update an employee's master record data in the PAID EMPLOYEE file (#450).                                                                                                                                    |
|                  |                                                                                                                                                                                                                                         |
| Exception Report | A report sent to the VA facilities by the AAC that lists rejected 8B Record data.                                                                                                                                                       |
|                  |                                                                                                                                                                                                                                         |
| Field            | A data element in a file.                                                                                                                                                                                                               |
|                  |                                                                                                                                                                                                                                         |
| Initial          | A type of download used to populate the PAID EMPLOYEE file (#450) with master record data.                                                                                                                                              |
|                  |                                                                                                                                                                                                                                         |
| MailMan          | The Department of Veterans Affairs electronic mail system.                                                                                                                                                                              |
|                  |                                                                                                                                                                                                                                         |
| Menu             | A set of options available to users to perform related tasks.                                                                                                                                                                           |
|                  |                                                                                                                                                                                                                                         |
| OLDE             | The AAC's On Line Data Entry data input system.                                                                                                                                                                                         |
|                  |                                                                                                                                                                                                                                         |
| Option           | A selection from a menu that performs a task.                                                                                                                                                                                           |
|                  |                                                                                                                                                                                                                                         |
| OT/CT            | Overtime or Compensatory time.                                                                                                                                                                                                          |
|                  |                                                                                                                                                                                                                                         |
| Pay Period       | A period of two consecutive calendar weeks that make up a payroll cycle. There are 26 pay periods per year.                                                                                                                             |
|                  |                                                                                                                                                                                                                                         |
| Package          | A set of MUMPS routines, files, documentation and installation procedures that support a specific function within DHCP.                                                                                                                 |
|                  |                                                                                                                                                                                                                                         |
| Payroll Clerk    | Employee of Fiscal Service, Payroll Section who is responsible for uniformity in the correct preparation and maintenance of time and attendance reports.                                                                                |
|                  |                                                                                                                                                                                                                                         |
| Payrun           | A type of download containing accounting data used to update the PAID EMPLOYEE (#450) and PAID PAYRUN DATA (#459) files.                                                                                                                |
|                  |                                                                                                                                                                                                                                         |
| Posting          | Entering data onto a time and attendance report.                                                                                                                                                                                        |
|                  |                                                                                                                                                                                                                                         |
| RET              | RETURN or ENTER key on a terminal keyboard.                                                                                                                                                                                             |
|                  |                                                                                                                                                                                                                                         |
| Separation       | A type of download used to mark an employee's entry in the PAID EMPLOYEE (#450) file as a separation (i.e., no longer an active employee at that station).                                                                              |
|                  |                                                                                                                                                                                                                                         |
| SF 71            | Application for Leave, Standard Form 71.                                                                                                                                                                                                |
|                  |                                                                                                                                                                                                                                         |
| Software         | A generic term referring to a related set of computer programs.                                                                                                                                                                         |
|                  |                                                                                                                                                                                                                                         |
| SSN              | Social Security Number.                                                                                                                                                                                                                 |
|                  |                                                                                                                                                                                                                                         |
| Stub record      | The first 31 characters of a Time and Attendance Report (VA Form 4-5631).                                                                                                                                                               |
|                  |                                                                                                                                                                                                                                         |
| T&A              | Time and Attendance.                                                                                                                                                                                                                    |
|                  |                                                                                                                                                                                                                                         |
| T&A Manager      | Has the responsibility of downloading and uploading the 8B Records (via MailMan), and ensuring all 8B Records are processed in a timely fashion.                                                                                        |
|                  |                                                                                                                                                                                                                                         |
| T&L              | Time and Leave Unit.                                                                                                                                                                                                                    |
|                  |                                                                                                                                                                                                                                         |
| Timekeeper       | Responsible for the preparation, maintenance, and timely submission of time and attendance reports for each affected employee whose record has been assigned to their jurisdiction.                                                     |
|                  |                                                                                                                                                                                                                                         |
| Transfer         | A type of download used to create an entry into the PAID EMPLOYEE (#450) file for an employee transferring into the station from another station.                                                                                       |
|                  |                                                                                                                                                                                                                                         |
| Transmit         | A process in which data is sent from one computer to another.                                                                                                                                                                           |
|                  |                                                                                                                                                                                                                                         |
| User             | A person who enters, edits, and/or retrieves data from a system.                                                                                                                                                                        |
|                  |                                                                                                                                                                                                                                         |
| VA Form 4-5631   | The TIME AND ATTENDANCE REPORT (i.e., timecard).                                                                                                                                                                                        |
|                  |                                                                                                                                                                                                                                         |
| Verify Code      | A unique security code which serves as a second level of security access. The user may change this code.                                                                                                                                |
|                  |                                                                                                                                                                                                                                         |
| VHA              | Veterans Health Administration.                                                                                                                                                                                                         |
|                  |                                                                                                                                                                                                                                         |
| 8B Record        | Employee information pertinent to the generation of biweekly payroll checks.                                                                                                                                                            |