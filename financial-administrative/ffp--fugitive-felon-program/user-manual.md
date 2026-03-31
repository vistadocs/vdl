---
title: Fugitive Felon Program (FFP) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: Fugitive Felon Program (FFP)
app_code: FFP
app_name: Fugitive Felon Program
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - felon
  - fugitive
  - report
  - flag
  - dgffp
  - date
  - table
  - contents
  - patient
  - software
page_count: 0
word_count: 2642
section_count: 9
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 8
revision_newest: 9/23/21
revision_oldest: 3/14/03
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fugitive_Felon/ffp_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fugitive_Felon/ffp_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=150"
---

![](fugitive-felon-program-ffp-user-manual/001.png)

fugitive felon program (FFP)

user manual

Patch DG\*5.3\*1056

September 2021

Health Systems Design & Development (HSD&D)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Related Manuals](#related-manuals)
- [Orientation](#orientation)
  - [User Responses](#user-responses)
- [Using the Software](#using-the-software)
  - [Accessing the Software](#accessing-the-software)
  - [Menu Diagram](#menu-diagram)
  - [Warning Display](#warning-display)
  - [Using the Menu Options](#using-the-menu-options)
    - [Fugitive Felon Program Main Menu \[DGFFP FUGITIVE FELON PROGRAM\]](#fugitive-felon-program-main-menu-dgffp-fugitive-felon-program)
    - [Set the Fugitive Felon Flag \[DGFFP SET FUGITIVE FELON FLAG\]](#set-the-fugitive-felon-flag-dgffp-set-fugitive-felon-flag)
    - [Clear the Fugitive Felon Flag \[DGFFP CLR FUGITIVE FELON FLAG\]](#clear-the-fugitive-felon-flag-dgffp-clr-fugitive-felon-flag)
    - [Fugitive Felon Status Reports \[DGFFP REPORT MENU\]](#fugitive-felon-status-reports-dgffp-report-menu)
    - [Fugitive Felon Alpha Report \[DGFFP ALPHA LIST\]](#fugitive-felon-alpha-report-dgffp-alpha-list)
    - [Fugitive Felon Status Report \[DGFFP STATUS REPORT\]](#fugitive-felon-status-report-dgffp-status-report)
    - [Cleared Fugitive Felon Flag Report \[DGFFP CLEARED STATUS RPT\]](#cleared-fugitive-felon-flag-report-dgffp-cleared-status-rpt)
    - [Fugitive Felon Inquiry \[DGFFP FFP INQUIRY\]](#fugitive-felon-inquiry-dgffp-ffp-inquiry)
- [Glossary](#glossary)
- [# Index](#index)
|          |                                                                                            |          |                 |
|----------|--------------------------------------------------------------------------------------------|----------|-----------------|
| Date     | Revision Description                                                                       | Author   | Project Manager |
| 3/14/03  | Initial Draft                                                                              | REDACTED |                 |
| 4/4/03   | Edits                                                                                      | REDACTED |                 |
| 4/25/03  | General Edits                                                                              | REDACTED |                 |
| 5/1/03   | Deleted Appendix and its references. Added Glossary                                        | REDACTED |                 |
| 6/25/03  | Added “Note” in Clear the Fugitive Felon Flag section                                      | REDACTED |                 |
| 12/15/04 | Updated to comply with SOP 192-352, Displaying Sensitive Data                              | REDACTED |                 |
| 6/24/05  | Updated warning display                                                                    | REDACTED | REDACTED        |
| 9/23/21  | Changed “Permanent Address:” to “Mailing Address:” on Fugitive Felon Inquiry Screen, p. 12 | REDACTED | REDACTED        |
Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Public Law (PL) 107-103, Section 505, prohibits provision of certain benefits to veterans or their dependents that are classified as fugitive felons. This law requires VA to provide current address information, upon written request, to any Federal, State, or local law enforcement official, if s/he

- Provides information required to fully identify the person
- Identifies the person as being a fugitive felon
- Certifies that apprehending such person is within the official duties of such official

This project software provides the following functionality for VHA implementation:

- Adds several fields to the V*IST*A Patient File to store the Fugitive Felon Flag and track when the flag was entered and removed
- Creates a new security key to control access to the Fugitive Felon Flag and the associated menu options
- Provides menu options that allow users to set and clear the Fugitive Felon Flag, and to print the various reports associated with the new fields
- Displays user alert from Scheduling and Registration options

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of Patch DG\*5.3\*1056 is to provide the functionality in support of PL 107-103, Section 505. The purpose of this manual is to provide instructions for using the menus and options exported with Patch DG\*5.3\*1056.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This user manual is the only formal user documentation being released with the Fugitive Felon Program software (Patch DG\*5.3\*1056).

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the examples in this manual, user responses are shown in bold type.

The \<ENTER\>symbol indicates that the user pressed the ENTER key on the keyboard.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fugitive Felon Program Main Menu is a standalone menu. Portions of the menu can only be accessed by holders of the DGFFP ACCESS security key.

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fugitive Felon Program Main Menu (DGFFP FUGITIVE FELON PROGRAM)

\|

\|

--------------------------------------------1 Set the Fugitive Felon Flag

\[DGFFP SET FUGITIVE FELON

FLAG\]

\*\*LOCKED: DGFFP ACCESS\*\*

--------------------------------------------2 Clear the Fugitive Felon Flag

\[DGFFP CLR FUGITIVE FELON

FLAG\]

\*\*LOCKED: DGFFP ACCESS\*\*

----3 Fugitive Felon Status Reports --------1 Fugitive Felon Alpha Report

\[DGFFP REPORT MENU\] \[DGFFP ALPHA LIST\]

\|

\|---------------------------------2 Fugitive Felon Status Report

\| \[DGFFP STATUS REPORT\]

\|

\|---------------------------------3 Cleared Fugitive Felon Flag

Report \[DGFFP CLEARED STATUS

RPT\]

--------------------------------------------4 Fugitive Felon Inquiry \[DGFFP

FFP INQUIRY\]

\*\*LOCKED: DGFFP ACCESS\*\*

## Warning Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The custom patient lookup in V*IST*A has been modified to display the following alert when a patient lookup is performed from a Scheduling or Registration package option and the FUGITIVE FELON FLAG has been set for the selected patient:

\*\*\* WARNING - FFP FLAG ACTIVE \*\*\*

PLEASE NOTIFY YOUR SUPERVISOR

You must press the ENTER key to continue past this message. Patient Lookups performed as a standalone query or from a package other than Scheduling or Registration will not display the alert.

## Using the Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Fugitive Felon Program Main Menu \[DGFFP FUGITIVE FELON PROGRAM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you begin, please note:*

You must hold the DGFFP ACCESS security key to access the Fugitive Felon Program Menu options other than the Status Reports.

*Use this option to:*

Access the Main Menu for the Fugitive Felon Program Menu options.

*How to use this option:*

Select an option from the Fugitive Felon Program Main Menu.

> 1 Set the Fugitive Felon Flag

> 2 Clear the Fugitive Felon Flag

> 3 Fugitive Felon Status Reports ...

> 1 Fugitive Felon Alpha Report

> 2 Fugitive Felon Status Report

> 3 Cleared Fugitive Felon Flag Report

> 4 Fugitive Felon Inquiry

> Select Fugitive Felon Program Main Menu Option:

### Set the Fugitive Felon Flag \[DGFFP SET FUGITIVE FELON FLAG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you begin, please note:*

You must hold the DGFFP ACCESS security key to access this option.

*Use this option to:*

Set the FUGITIVE FELON FLAG (#1100.01) in the PATIENT File (#2) and the associated support fields.

*How to use this option:*

1.  Select the patient for whom you want to set the Fugitive Felon Flag.
2.  The software displays the patient’s enrollment information.
3.  The software verifies that it will set the Fugitive Felon Flag and asks if you want to continue.
    1.  Enter YES to go to Step 4.
    2.  Enter NO to go to Step 5.
4.  The software asks if you want to process another felon entry.
    1.  Enter YES to go to Step 1.
    2.  Enter NO to go to Step 5.
5.  Return to the menu.

#### Example

Select Patient: FFPATIENT,ONE 1-1-60 000850001 NSC VETERAN

Enrollment Priority: GROUP 8c Category: IN PROCESS End Date:

\>\> This will set the Fugitive Felon Flag for FFPATIENT,ONE.

\>\> Continue with setting the flag? NO// YES

Process another felon entry? YES// NO

### Clear the Fugitive Felon Flag \[DGFFP CLR FUGITIVE FELON FLAG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you begin, please note:*

You must hold the DGFFP ACCESS security key to use this option.

*Use this option to:*

Remove the FUGITIVE FELON FLAG (#1100.01) from the PATIENT File, \#2.

*How to use this option:*

1.  Select the patient for whom you want to clear the Fugitive Felon Flag.
2.  The software displays the patient’s enrollment information.
3.  The software verifies that it will clear the Fugitive Felon Flag and asks if you want to continue.

> NOTE: An entry in the Remarks field for why the flag was cleared is required in order to proceed.

1.  Enter YES to go to Step 4.
2.  Enter NO to go to Step 5.
4.  The software asks if you want to process another felon entry.
    1.  Enter YES to go to Step 1.
    2.  Enter NO to go to Step 5.
5.  Return to the menu.

#### Example 

Select Patient: FFPATIENT,ONE 1-1-60 000850001 NSC VETERAN

\*\*\* WARNING - FFP FLAG ACTIVE \*\*\*

PLEASE NOTIFY YOUR SUPERVISOR

Enrollment Priority: GROUP 8c Category: IN PROCESS End Date:

\>\> This will clear the Fugitive Felon Flag for FFPATIENT,ONE.

\>\> Continue with clearing the flag? NO// YES

\>\> Enter a brief remark on why this flag is being cleared.

\>\> This is a required field.

--\> TESTING FOR USER DOCUMENTATION PURPOSES

Process another felon entry? YES// NO

### Fugitive Felon Status Reports \[DGFFP REPORT MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Use this option to:*

Access the Fugitive Felon Reports Menu options.

*How to use this option:*

Select an option from the Fugitive Felon Reports Menu.

1 Fugitive Felon Alpha Report

2 Fugitive Felon Status Report

3 Cleared Fugitive Felon Flag Report

### Fugitive Felon Alpha Report \[DGFFP ALPHA LIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Use this option to:*

Generate an alphabetical list of patients with the Fugitive Felon Flag currently set in the PATIENT File (#2). The output includes the following information:

- Report title, date range, print date, and page number
- Patient name and last four of SSN
- Date the flag was set
- Who entered the flag

*How to use this option:*

1.  The software asks if you want to print the report by date range. All flags set within that date range will be displayed. If no date range is selected, the report prints for all dates.
    1.  Enter YES to go to Step 2.
    2.  Enter NO to go to Step 4.
2.  The software prompts you to enter a beginning date for the report.
    1.  Enter a date to go to Step 3.
    2.  Press the ENTER key to go to Step 5.
3.  The software prompts you to enter an end date for the report.
    1.  Enter a date to go to Step 4.
    2.  Press the ENTER key to go to Step 5.
4.  The software prompts you to enter a device for printing the report.
5.  Return to the menu.

#### Example

Print report by date range? YES// \<ENTER\>

Enter beginning date for report: T-1M (JAN 11, 2003)

Enter end date for report: T (FEB 11, 2003)

DEVICE: HOME// \<ENTER\> UCX/TELNET

Fugitive Felon Alpha List

Report Date Range: Jan 11, 2003 to Feb 11, 2003

Print Date: Feb 11, 2003@12:01:58

Page: 1

Patient Name Entered Who Entered

=============================================================================

FFPATIENT,THREE (0003) 1/17/03 FFUSER,THREE

FFPATIENT,TWO (0002) 1/17/03 FFUSER,TWO

### Fugitive Felon Status Report \[DGFFP STATUS REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Use this option to:

Generate a report that lists veterans with the Fugitive Felon Flag set and displays current inpatient status and scheduled future appointments. The output includes the following information:

- Report title, date range, print date, and page number
- Patient name and last four of SSN
- Movement
- Movement Date
- Room, Bed, and Ward for inpatient
- Active scripts
- Clinic appointments

#### How to use this option:

1.  The software asks if you want to print the report by date range. All flags set within that date range will be displayed. If no date range is selected, the report prints for all dates.
    1.  Enter YES to go to Step 2.
    2.  Enter NO to go to Step 4.
2.  The software prompts you to enter a beginning date for the report.
    1.  Enter the start date of the report to go to Step 3.
    2.  Press the ENTER key to go to Step 5.
3.  The software prompts you to enter an end date for the report.
    1.  Enter the end date of the report to go to Step 4.
    2.  Press the ENTER key to go to Step 5.
4.  The software prompts you to enter a device for printing the report.
5.  Return to the menu.

Fugitive Felon Status Report

Report Date Range: Aug 20, 2002 to Feb 20, 2003

Print Date: Feb 20, 2003@11:17:32

Page: 1

Patient Name Movement Date Room/Bed

Ward Active Scripts?

Clinic Appointments

===============================================================================

Inpatient Listing

------------------

FFPATIENT,THREE (0003) ADMISSION Jan 17, 2003 501B3-A

12C PSYCH None

Outpatient Listing

------------------

FFPATIENT,TWO (0002)

None

### Cleared Fugitive Felon Flag Report \[DGFFP CLEARED STATUS RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Use this option to:*

Generate a report that shows those entries for which the Fugitive Felon Flag has been cleared. A brief remarks entry is required. The output includes the following information:

- Report title, date range, print date, and page number
- Patient name and last four of SSN
- Date Fugitive Felon Flag was entered and by whom
- Date Fugitive Felon Flag was cleared and by whom
- Brief remarks

#### How to use this option:

1.  The software asks if you want to print the report by date range. All flags set within that date range will be displayed. If no date range is selected, the report prints for all dates.
    1.  Enter YES to go to Step 2.
    2.  Enter NO to go to Step 4.
2.  The software prompts you to enter a beginning date for the report.
    1.  Enter the start date of the report to go to Step 3.
    2.  Press the ENTER key to go to Step 5.
3.  The software prompts you to enter an end date for the report.
    1.  Enter the end date of the report to go to Step 4.
    2.  Press the ENTER key to go to Step 5.
4.  The software prompts you to enter a device for printing the report.
5.  Return to the menu.

#### Example

Print report by date range? YES// \<ENTER\>

Enter beginning date for report: T-3M (DEC 25, 2002)

Enter end date for report: T (FEB 25, 2003)

\>\> This report requires a 132-column printer

DEVICE: HOME// \<ENTER\> UCX/TELNET

Cleared Fugitive Felon Status Report

Report Date Range: Dec 25, 2002 to Feb 25, 2003

Print Date: Feb 25, 2003@10:46:42

Page: 1

Patient Name Entered Who Entered

Cleared Who Cleared

=============================================================================

FFPATIENT,ONE (0001) 1/17/03 FFUSER,ONE

2/10/03 FFUSER,ONE

ENTERED IN ERROR

### Fugitive Felon Inquiry \[DGFFP FFP INQUIRY\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you begin, please note:*

- You must hold the DGFFP ACCESS security key to use this option.
- This option displays information in List Manager screen format. In addition to a new “PT Change Patient” action, the following actions are also available:

> \+ Next Screen \< Shift View to Left PS Print Screen

> \- Previous Screen FS First Screen PL Print List

> UP Up a Line LS Last Screen SL Search List

> DN Down a Line GO Go to Page ADPL Auto Display(On/Off)

> \> Shift View to Right RD Re Display Screen Q Quit

*Use this option to:*

View patient address and Fugitive Felon status information. The output includes the following information:

- Date and time
- Page number
- Patient name and SSN
- Tells if the flag is set, displays the date and time it was set, and by whom
- If the flag was cleared, displays the date and time it was cleared, and by whom
- Closing remarks
- Patient address information
- Future appointments for the selected patient

*How to use this option:*

1.  Select the name of the patient.
2.  The software displays the patient’s enrollment information. The Fugitive Felon Flag warning will display if the flag is set for the selected patient. You must press the ENTER key to continue past this warning.
3.  Page 1 of the Fugitive Felon Inquiry List Manager Screen displays patient name, SSN, and address information, in addition to flag status information.
4.  The “Select Action: Next Screen//” prompt appears at the bottom of the screen.
    1.  Press the ENTER key to go to Step 5.
    2.  Enter PT to go to Step 1.
    3.  Enter two question marks (??) to display more List Manager actions.
5.  Page 2 displays scheduled future appointments, if any, for the selected patient.
6.  The “Select Action: Quit//” prompt appears at the bottom of the screen.
    1.  Press the ENTER key to go to Step 7.
    2.  Enter PT to go to Step 1.
    3.  Enter two question marks (??) to display more List Manager actions.
7.  Return to the menu.

  
Fugitive Felon Inquiry \[DGFFP FFP INQUIRY\], continued

#### Example

Select PATIENT NAME: FFPATIENT,TWO FFPATIENT,TWO 1-1-60 000850002

NSC VETERAN

\*\*\* WARNING - FFP FLAG ACTIVE \*\*\*

PLEASE NOTIFY YOUR SUPERVISOR

Enter \<RETURN\> to continue. \<ENTER\>

<u>Fugitive Felon Inquiry Mar 13, 2003@17:12:47 Page: 1 of 2</u>

Patient: FFPATIENT,TWO (000-85-0002)

Fugitive Flag Set

Date Set: Jan 17, 2003 Set By: FFUSER,TWO

Date Cleared: Cleared By:

Closing Remark:

Mailing Address: Temporary Address:

================== ==================

1234 EDS RD

PLANO

TEXAS

75024

\+ Enter ?? for more actions

PT Change Patient

Select Action: Next Screen// \<ENTER\>

Fugitive Felon Inquiry Mar 14, 2003@11:49:35 Page: 2 of 2

Patient: FFPATIENT,TWO (000-85-0002)

Fugitive Flag Set

\+

Future Appointments:

====================

Enter ?? for more actions

PT Change Patient

Select Action: Quit// \<ENTER\> QUIT

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Acronym     | Description                                                            |
| FFP             | Fugitive Felon Program                                                     |
| Fugitive Felon  | An individual who is wanted by law enforcement in connection with a felony |
| NSC             | Non-Service Connected                                                      |
| PL              | Public Law                                                                 |
| SSN             | Social Security Number                                                     |
| VA              | Veterans Administration                                                    |
| VHA             | Veterans Health Administration                                             |
| V*IST*A | Veterans Health Information Systems and Technology Architecture            |

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Accessing the Software 3

C

Change to Patient Lookup 4

Clear the Fugitive Felon Flag 6

Cleared Fugitive Felon Flag Report 10

D

DGFFP ALPHA LIST 8

DGFFP CLEARED STATUS RPT 10

DGFFP CLR FUGITIVE FELON FLAG 6

DGFFP FFP INQUIRY 10

DGFFP FUGITIVE FELON PROGRAM 4

DGFFP REPORT MENU 7

DGFFP SET FUGITIVE FELON FLAG 5

DGFFP STATUS REPORT 9

F

Fugitive Felon Alpha Report 8

Fugitive Felon Inquiry 10

Fugitive Felon Program Main Menu 4

Fugitive Felon Status Report 9

Fugitive Felon Status Reports 7

I

Introduction 1

M

Menu Diagram 3

O

Overview 1

P

Purpose 1

R

Related Manuals 1

Revision History i

S

Set the Fugitive Felon Flag 5

U

Using the Menu Options 4

Using the Software 3

A

Accessing the Software 3

C

Change to Patient Lookup 4

Clear the Fugitive Felon Flag 6

Cleared Fugitive Felon Flag Report 10

D

DGFFP ALPHA LIST 8

DGFFP CLEARED STATUS RPT 10

DGFFP CLR FUGITIVE FELON FLAG 6

DGFFP FFP INQUIRY 10

DGFFP FUGITIVE FELON PROGRAM 4

DGFFP REPORT MENU 7

DGFFP SET FUGITIVE FELON FLAG 5

DGFFP STATUS REPORT 9

F

Fugitive Felon Alpha Report 8

Fugitive Felon Inquiry 10

Fugitive Felon Program Main Menu 4

Fugitive Felon Status Report 9

Fugitive Felon Status Reports 7

I

Introduction 1

M

Menu Diagram 3

O

Overview 1

P

Purpose 1

R

Related Manuals 1

Revision History i

S

Set the Fugitive Felon Flag 5

U

Using the Menu Options 4

Using the Software 3