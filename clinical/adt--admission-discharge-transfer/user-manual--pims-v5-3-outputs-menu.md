---
title: PIMS Version 5.3 User Manual - Outputs Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Outputs Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 5
description: The Scheduling module of the PIMS Package is designed to assist in the set-up of clinics, scheduling of patients for clinic appointments, and the collection of an assortment of related workload data for reporting purposes. The Scheduling Outputs functionality provides the end-users with tools that p
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - report
  - clinic
  - health
  - mental
  - show
  - high
  - risk
  - patient
  - table
  - class
page_count: 0
word_count: 14308
section_count: 17
table_count: 13
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsschoutput.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsschoutput.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

![](pims-version-5-3-user-manual-outputs-menu/001.png)

Patient Information Management System (PIMS)Scheduling Outputs Menu Module SchedulingUSER MANUALVersion 5.3

April 2013

Office of Information and Technology (OIT)

This Page Left Bank Intentionally

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [Orientation](#orientation)
  - [Intended Audience](#intended-audience)
  - [Legal Requirements](#legal-requirements)
  - [Disclaimers](#disclaimers)
  - [## Documentation Conventions](#documentation-conventions)
  - [Documentation Navigation](#documentation-navigation)
  - [Assumptions](#assumptions)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [On-line Help System](#on-line-help-system)
  - [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
- [Documentation Website Locations](#documentation-website-locations)
- [Related Manuals](#related-manuals)
  - [VistA Documentation](#vista-documentation)
  - [General Support](#general-support)
- [Introduction](#introduction)
- [# Use of the Software](#use-of-the-software)
  - [SD\5.3\588 Patch - High Risk Mental Health Proactive Report](#sd53588-patch-high-risk-mental-health-proactive-report)
    - [New Options](#new-options)
    - [Modified Options](#modified-options)
  - [SD\5.3\578 Patch – High Risk Mental Health No Show Report](#sd53578-patch-high-risk-mental-health-no-show-report)
    - [New Options](#new-options-1)
  - [Outputs Menu](#outputs-menu)
    - [Appointment List](#appointment-list)
    - [Appointment Management Report](#appointment-management-report)
    - [Cancelled Clinic Report](#cancelled-clinic-report)
    - [Clinic Profile](#clinic-profile)
- [### Display Clinic Availability Report](#display-clinic-availability-report)
    - [Enrollments \> X Days](#enrollments-x-days)
    - [File Room List](#file-room-list)
    - [Future Appointments for Inpatients](#future-appointments-for-inpatients)
    - [Inpatient Appointment List](#inpatient-appointment-list)
    - [Management Report for Ambulatory Procedures](#management-report-for-ambulatory-procedures)
    - [No-Show Report](#no-show-report)
    - [Patient Profile MAS](#patient-profile-mas)
    - [Print Scheduling Letters](#print-scheduling-letters)
    - [Provider/Diagnosis Report](#providerdiagnosis-report)
    - [Radiology Pull List](#radiology-pull-list)
    - [Visit Rpt By Transmitted Opt Encounter](#visit-rpt-by-transmitted-opt-encounter)
    - [Workload Report](#workload-report)
  - [HRMHP No Show and Proactive Options & Features](#hrmhp-no-show-and-proactive-options-features)
  - [### High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\]](#high-risk-mh-no-show-adhoc-report-sd-mh-no-show-ad-hoc-report)
    - [High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]](#high-risk-mh-no-show-nightly-report-sd-mh-no-show-nightly-bgj)
    - [High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\]](#high-risk-mh-proactive-adhoc-report-sd-mh-proactive-ad-hoc-report)
    - [High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\]](#high-risk-mh-proactive-nightly-report-sd-mh-proactive-bgj-report)
- [Glossary](#glossary)
The following table displays the revision history for this document. Revisions to the documentation are based on patches, style updates, and new versions released to the field.
<span id="_Toc352927862" class="anchor"></span>Table 1.0 - Documentation Revision History
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 34%" />
<col style="width: 17%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td>REVISION DATES</td>
<td>PAGE #</td>
<td>DESCRIPTION</td>
<td>PROJECT MANAGER</td>
<td>TECHNICAL WRITER</td>
</tr>
<tr class="even">
<td>4/2013</td>
<td>All</td>
<td><p>Added Vista Scheduling Patch SD*5.3*588, which adds two new Proactive reports, SD MH PROACTIVE BGJ REPORT and SD MH PROACTIVE AD HOC REPORT.</p>
<p><strong>NOTE: These reports are not part of the Scheduling Outputs Menu, they are Stand-Alone Menu Options.</strong></p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/15/12</td>
<td></td>
<td><p>Added VistA Scheduling Patch SD*5.3*578. It contains options titled SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY BGJ. These Scheduling Report options appear in the primary and secondary menu options.</p>
<p>Added screen printouts for new options in this Version 5.3 release.</p>
<p>This manual has been updated to the latest Technical Publication Standards of OIT.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/14/08</td>
<td>NA</td>
<td>Minor Formatting Changes</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/7/07</td>
<td>NA</td>
<td>Removed Transitional Pharmacy Benefit Deferred Appt Record option</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/7/07</td>
<td>NA</td>
<td>Removed PCMM Reports Menu</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/14/06</td>
<td>NA</td>
<td>SD*5.3*266 – updated Appointment List option</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/25/06</td>
<td>NA</td>
<td>SD*5.3*487 - added documentation for Cancelled Clinic Report option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/9/06</td>
<td>NA</td>
<td>SD*5.3*410 - added documentation for revised No-Show Report option</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/12/05</td>
<td>NA</td>
<td>SD*5.3*377 – the Routing Slips report can now be sorted by Physical Location</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
Table Of Contents
<u>TABLES</u>
This Page Left Bank Intentionally

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling Module provides for efficient and accurate collection, maintenance and output of data that allows VA Medical Centers to provide timely and quality care to its patients.

The Scheduling Module is available on-line to a wide range of users throughout VA Medical Centers nationwide. It is integrated with the VA FileMan, which in turn allows the extraction of ad hoc reports by the following listed audiences.

Some of the Scheduling Outputs that may be generated include workload analysis reports, correspondence letters with notifications, information regarding cancellation of clinics/appointments, clinic set-up screens, and enrollment/ discharge of patients from clinics.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audiences are listed below:

| READERS/USERS                                               | AUDIENCE |
|-------------------------------------------------------------|----------|
| PRODUCT SUPPORT (PS) PERSONNEL                              | X        |
| INFORMATION RESOURCE MANAGEMENT (IRM)                       | X        |
| PRODUCT DEVELOPMENT (PD)—VISTA LEGACY DEVELOPMENT TEAMS     | X        |
| AUTOMATED DATA PROCESSING APPLICATION COORDINATOR (ADPACS)  | X        |
| HELP DESK PERSONNEL/INFORMATION TECHNOLOGY (IT) SPECIALISTS | X        |

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special legal requirements involved in the use of VistA software.

## Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides an overall explanation of how to use Scheduling software. Specifically, it describes the outputs of this software and the various options the User may choose. There are a myriad of reports that can be viewed and printed.

No attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA websites on the Internet and VA Intranet for a general orientation to VistA.

For example, go to the Office of Information & Technology (OIT) VistA Development VA Intranet website: <http://vista.med.va.gov>

| ![](pims-version-5-3-user-manual-outputs-menu/002.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you can find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## ## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material:

Various symbols/terms are used throughout the document to alert the reader to special information.

The following table gives a description of each of these symbols/terms:

<span id="_Toc352927863" class="anchor"></span>Table 2.0 - Documentation Symbol / Term Descriptions

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SYMBOL</strong></td>
<td><strong>DESCRIPTION</strong></td>
</tr>
<tr class="even">
<td>![](pims-version-5-3-user-manual-outputs-menu/003.png)</td>
<td><p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
<p>In most cases you will need this information, or at least it will make the installation smoother and more understandable. Please read each note <em>before</em> executing the steps that follow it!</p></td>
</tr>
<tr class="odd">
<td>![](pims-version-5-3-user-manual-outputs-menu/004.png)</td>
<td><strong>CAUTION, DISCLAIMER, or RECOMMENDATION:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
</tbody>
</table>

Descriptive text is presented in a proportional font (as represented by this font).

- "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User's responses to online prompts and some software code reserved/key words will be bold typeface and highlighted in yellow.

Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                                    |                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pims-version-5-3-user-manual-outputs-menu/005.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

Bold Typeface:

- All computer keys when referenced with a command (e.g., "press Enter" or "click OK").
- All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
- All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
- All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., "Enter the following command: CD xyz").

*Italicized Typeface:*

- Emphasis (e.g., do not proceed or you must do the following steps).
- All reference to computer dialogue or screen titles (e.g., "in the Add Entries dialogue…").
- All document or publication titles and references (e.g., "see the ABC Installation Guide").Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) must begin with either "000" or "666".

Patient and usernames are formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in LSRP test patient and usernames would be documented as follows: LSRPPATIENT, ONE; LSRPPATIENT, TWO; LSRPPATIENT, THREE; etc.

## Documentation Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Document Navigation—this document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add back and forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outputs menu applications described equips the User with the tools to produce a variety of scheduling-related reports and letters pertinent to procedures and follow ups.

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Scheduling User Manual is provided in Adobe Acrobat PDF (portable document format) files. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VistA Home Page, “Viewers” Directory.

Once you open the file, you may click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. You may print any or all pages of the file. Click on the “Print” icon and select the desired pages. Then click “OK”. Each menu file contains a listing of the menu, a brief description of the options contained therein, and the actual option documentation. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

## On-line Help System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements which provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". The HELP message will appear under the prompt, then the prompt will be repeated. For example, perhaps you see the prompt

> Sort by TREATING SPECIALTY:

And you need assistance so you answer enter "?" and the HELP message would appear.

> Sort by TREATING SPECIALTY:

CHOOSE FROM:

- SURGERY
- CARDIOLOGY
- 12 PSYCHIATRY

Sort by TREATING SPECIALTY:

For some prompts, the system will list the possible answers from which you may choose. Any time choices appear with numbers, the system will usually accept the number or the name. A HELP message may not be available for every prompt. If you enter a "?" or "??" at a prompt that does not have a HELP message, the system will repeat the prompt.

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acronyms are listed at:

- Refer to the following link <span class="mark">REDACTED</span> Refer to the following link <span class="mark">REDACTED</span>

# Documentation Website Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                  |                                                         |                                                                                            |
|----------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------|
| SITE                             | URL                                                     | DESCRIPTION                                                                                |
| National Clinical Reminders site | <span class="mark">REDACTED</span>                      | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VistA Document Library           | [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/) | Contains manuals for Scheduling and related applications.                                  |

# Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 35%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION NAME</th>
<th>FILE NAME</th>
<th>LOCATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders Installation and Setup Guide</td>
<td><p>PXRM_2_18_IG.PDF</p>
<p>PXRM_2_18_IG.doc</p></td>
<td><p>VDL</p>
<p>Clinical Reminders website</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>Scheduling Patch 578 Installation and Setup Guide</td>
<td><p>SD_5_3_578_IG.PDF</p>
<p>SD_5_3_578_IG.doc</p></td>
<td>Anonymous Directories</td>
</tr>
<tr class="odd">
<td>Registration Install Guide</td>
<td>DG_5_3_836_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
<tr class="even">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td>PXRM_2_24_IG.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>High Risk Mental Health Patient Project Release Notes</td>
<td>PXRM_2_24_RN.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Clinical Reminders Manager's Manual</td>
<td>PXRM_2_MM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Health Summary User Manual</td>
<td>HSUM_2_7_104_UM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Health Summary Technical Manual</td>
<td>HSUM_2_7_104_TM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Text Integration Utility User Manual</td>
<td>TIUUM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>CPRS User Guide: GUI Version</td>
<td>CPRSGUIUM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>CPRS Technical Manual: GUI Version</td>
<td>CPRSGUITM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>CPRS Technical Manual</td>
<td>CPRSLMTM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>PIMS Scheduling User - Manual Menus, Intro &amp; Orientation</td>
<td>PIMsSchIntro.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>DOCUMENTATION NAME</td>
<td>FILE NAME</td>
<td>LOCATION</td>
</tr>
<tr class="odd">
<td>PIMS Scheduling User Manual - Outputs Menu</td>
<td>PIMsSchOutput.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>PIMS Technical Manual</td>
<td>PIMSTM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Patient Record Flags User Guide</td>
<td>PatRecFlagUG.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Scheduling and Registration Installation Review Guide</td>
<td>SDDG_Install_Review.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
</tbody>
</table>

## VistA Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents must be read using the Adobe® Acrobat Reader, which is freely distributed by Adobe® Systems Incorporated at the following Website: <http://www.adobe.com/>. VistA documentation can also be downloaded from the Product Support (PS) anonymous directories:

Preferred Method download.VistA.med.va.gov

> **NOTE:** This method transmits the files from the first available FTP server.

- Albany OIFO - <span class="mark">REDACTED</span>
- Hines OIFO - <span class="mark">REDACTED</span>
- Salt Lake City OIFO - <span class="mark">REDACTED</span>

## General Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For support, site questions, and problems with the VistA software, please enter a National Remedy ticket to Scheduling (SD) or call the National Service Desk-Tuscaloosa at 1-888-596-4357 for assistance.
- Also, review the VDL Internet link for all released end-user documentation found at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling module of the PIMS Package is designed to assist in the set-up of clinics, scheduling of patients for clinic appointments, and the collection of an assortment of related workload data for reporting purposes. The Scheduling Outputs functionality provides the end-users with tools that produce a variety of reports and letters pertinent to Scheduling procedures.

Through Scheduling, necessary National Patient Care Database (NPCDB) workload is transparently collected and may be transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Scheduling is fully integrated with the VA FileMan, thus allowing the extraction of ad hoc reports by non-programming personnel.

Important features of the Scheduling module include clinic set-up and enrollment/discharge of patients from clinics. Outputs that may be generated include workload analysis reports and letters of notification regarding cancellation of clinics/appointments.

This Page Left Bank Intentionally

# # Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the Scheduling Menus, Intro, & Orientation User Manual provides instructions for the End-Users to successfully use the software with little or no assistance. It also list and describes the menus/options with examples to implement and use the software.

> **NOTE:** These reports are not part of the Scheduling Outputs Menu, they are Stand-Alone Menu Options

## SD\*5.3\*588 Patch - High Risk Mental Health Proactive Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SD\*5.3\*588 High Risk Mental Health Proactive Report patch assists the Mental Health professionals in the tracking of veterans with the High Risk for Suicide Patient Record Flag (PRF) who have appointments for the day. This patch consists of the following new enhancements:

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option

The new Ad Hoc proactive report will produce a list of patients with the high risk for suicide patient record flag that have scheduled appointments for a date range. It allows the user to enter dates into the future. The user will be asked to list only mental health appointments that are in the Reminder Location File or list all clinics both mental health and non- mental health. This report gives the user a bit more flexibility.

IRM staff will need to attach the High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff's discretion.

The High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option uses the Reminder Location File to check for Mental Health clinics.

Example: The new High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option is displaying the High Risk MH Proactive Adhoc Report.

Select OPTION NAME: SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

High Risk MH Proactive Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health Proactive Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/04/13// T

Select Ending Date: 04/04/13// T+10

Select division: ALL//

Sort the report by:

A All clinics

M Mental Health clinics only

Sort by: (A)ll clinics A//

Select Clinic: ALL//

This output requires 80 column output

Select Device: UCX/TELNET Right Margin: 80// ^

DEVISC1A1:MNTVLL 3d1\>Q

DEVISC1A1:MNTVLL\>D ^XQ1

Select OPTION NAME: XU USER START-UP User start-up event

User start-up event

DEVISC1A1:MNTVLL\>Q

DEVISC1A1:MNTVLL\>D ^XQ1

Select OPTION NAME: SD MH PROACTIVE

1 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

2 SD MH PROACTIVE BGJ REPORT High Risk MH Proactive Nightly Report

CHOOSE 1-2: 1 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

High Risk MH Proactive Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health Proactive Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/04/13// T

Select Ending Date: 04/04/13// T+10

Select division: ALL//

Sort the report by:

A All clinics

M Mental Health clinics only

Sort by: (A)ll clinics A//

Select Clinic: ALL//

This output requires 80 column output

Select Device: ;;99999 UCX/TELNET Right Margin: 80//

...SORRY, HOLD ON...

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 1

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ALBANY

1 TESTPATIENT,ONEXXXXX T1111 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/8/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/10/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/11/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/12/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 2

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ON THE HUDSON IN HISTORIC TROY

1 TESTPATIENT,TWOXXXX T0000 4/4/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/5/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/7/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/10/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/11/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/12/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

4/14/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 3

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: TROY1

1 TESTPATIENT,ONEXXXX T1111 4/4/2013@09:00 MENTAL HEALTH

4/5/2013@09:00 MENTAL HEALTH

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@09:00 MENTAL HEALTH

4/10/2013@09:00 MENTAL HEALTH

4/11/2013@09:00 MENTAL HEALTH

4/12/2013@09:00 MENTAL HEALTH

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 4

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

Totals Page

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Division/Clinic Appointment Totals

Division/CLinic Unique

Patients

ALBANY 1

ON THE HUDSON IN HISTORIC TROY 1

TROY1 1

#### High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option

This new option should be used if you need to re-create the same report that is created by the scheduled SDAM BACKGROUND JOB after midnight each night. The option lists the scheduled appointments for Mental Health Clinics for today.

This report should not be scheduled to run nightly as it is kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system. This report is sent in a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.

Future appointments will be listed on this report. The number of days of future appointments that is listed is defaulted to 30 days in the future. Parameter SD MH PROACTIVE DAYS has been added to store the number of days to list future appointments. This parameter can be edited, within the range of 1 to 30, by the user by using the Edit Parameter Values \[XPAR EDIT PARAMETER\] option, changing the System value.

This proactive background job report will produce a list of patients with the high risk for suicide patient record flag and who have scheduled appointments for today. This background job will produce a list of appointments (mental health clinics only) for those patients for the next day so that the Suicide Prevention Coordinators (SPC) can follow up and remind patients of their appointments for that day. The SPCs in the SD MH NO SHOW NOTIFICATION mail group will receive a mail message. All SPCs that need to receive this report should be a member of that mail group. The new option will kick off automatically every night with the running of the Scheduling Nightly Background Job.

IRM staff will need to attach the High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff's discretion.

The High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option uses the Reminder Location File to check for Mental Health clinics.

Example: The new High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option is displaying the High Risk MH Proactive Nightly Report.

Select OPTION NAME: SD MH PROACTIVE BGJ REPORT High Risk MH Proactive

Nightly Report

High Risk MH Proactive Nightly Report

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

This report option generates a mail message containing the

High Risk Mental Health Proactive Nightly Report which is sent only

to individuals in the SD MH NO SHOW NOTIFICATION mailgroup.

DEVISC1A1:MNTVLL\>D ^XM

All Baskets, New Priority messages: 43

\*=New/!=Priority.............Subject................Lines.From.......Read/Rcvd

!1572. IN \[126400\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1573. IN \[126401\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1574. IN \[126403\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1575. IN \[126404\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1576. IN \[126509\] 02/01/12 Pre-report National Flag 49 HRMH PRF GENERATE JOB

!1577. IN \[126510\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1578. IN \[126511\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1579. IN \[126512\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1580. IN \[126513\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1581. IN \[126514\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1582. IN \[126515\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1583. IN \[126516\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1584. IN \[126517\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1585. IN \[126518\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1586. IN \[126519\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1587. IN \[126520\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1588. IN \[126521\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1589. IN \[126522\] 02/01/12 Pre-report National Flag 12 HRMH PRF GENERATE JOB

!1590. IN \[126523\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1591. IN \[126524\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

VA MailMan 8.0 service for FIEUDMNDS.DDUD_CUEJ@ <span class="mark">REDACTED</span>

You last used MailMan: 03/18/13@11:46

You have 861 new messages.

Select MailMan Option: READ/MANAGE MESSAGES

Select message reader: Classic//

Read mail in basket: IN// (2343 messages, 861 new)

Last message number: 2343 Messages in basket: 2343 (861 new)

Enter ??? for help.

IN Basket Message: 1// 2344

Enter message action (in IN basket): Ignore// Print

Print recipient list? No// NO

DEVICE: HOME// ;;99999 UCX/TELNET

MailMan message for FJRURURU,RMRMRH OI&T STAFF

Printed at <span class="mark">REDACTED</span> 04/04/13@16:02

Subj: HRMH PROACTIVE NIGHTLY REPORT MESSAGE \# \[#136309\] 04/04/13@16:01

37 lines

From: POSTMASTER In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Division Totals

Division Unique

Patients

ALBANY 1

ON THE HUDSON IN HISTORI 1

TROY1 1

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 1

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ALBANY

1 TESTPATIENT,ONEXXXXX T0000 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 2

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ON THE HUDSON IN HISTORI

1 TESTPATIENT,TWOXXXXX T1111 4/4/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX

4/5/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 3

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: TROY1

1 TESTPATIENT,ONEXXXXX T0000 4/4/2013@09:00 MENTAL HEALTH

4/5/2013@09:00 MENTAL HEALTH

### Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option

This report will list the patients who have the patient record flag High Risk for suicide and No Show an appointment in a mental health or non-mental health clinic. The report will list the patient, emergency contacts, next of kin, future scheduled appointments, provider, and results. Mental Health clinics are face-to-face. Mental Health appointments are defined in the "VA-MH NO SHOW APPT CLINICS LL" Reminder Location List. The High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option is modified to include the following changes:

- The provider name is now displayed directly under the No Show appointment information, to keep everything connected.
- Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.
- Appointment line now displays information in two lines:
- line one: count, patient name, Patient ID 1st initial last name+last 4 ssn, appointment D/T, 30 character clinic name
- line two: appointment status abbreviation, appointment provider name.
- Patient ID is now 5 characters: First initial of last name + last 4 of SSN.
- 30-character Clinic name in both future and appointment data information.
- AM and PM removed from the date/time of appt.
- The report now displays the name of the Mental Health Treatment Coordinator (MHTC) and the name of the care team they are assigned to in parentheses.
- The results of the no show patient contact are also included.
- Results added for resolution: Reminder term and health factor Information.

This is the High Risk Mental Health AD Hoc No show Report entry point that the user can run to display the report. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments and results of attempts to contact the no showed patients. The user is asked for various sort criteria, a date range, divisions to display (one, many, all), and sort by Clinic, Reminder Location or Stop Codes (one, many, all).

Example: The modified High Risk MH No-Show Adhoc Report.

Select OPTION NAME: SD MH NO

1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

CHOOSE 1-2: 1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

High Risk MH No-Show Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health NO SHOW Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/08/13// T-6 (APR 02, 2013)

Select Ending Date: 04/08/13// T (APR 08, 2013)

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//

Select Number of days to List Future Appointments: 30//1

This output requires 80 column output

Select Device: ;;99999 UCX/TELNET Right Margin: 80//

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 1

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* DIVISION/CLINIC/STOP: ALBANY/D-PSYCHXXXXXXXXXXXXXXXXXXX/188

1 TESTPATIENT,ONEXXXX T0000 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXX

\*NS PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

2 TESTPATIENT,ONEXXXX T0000 4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

\*NS PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

3 TESTPATIENT,ONEXXXX T0000 4/8/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

\*NSA PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 2

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC/202

1 TESTPATIENT,TWO T1111 4/4/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX

\*NS PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

Results:

2 TESTPATIENT,TWO E4646 4/5/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

\*NSA PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

Results:

3 TESTPATIENT,TWO T1111 4/7/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

\*NS PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,THREE (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

Results:

4 TESTPATIENT,TWO T1111 4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

\*NAT PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 3

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: TROY1/MENTAL HEALTH/188

1 TESTPATIENT,ONEXXXX T0000 4/4/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

2 TESTPATIENT,ONEXXXX T0000 4/5/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

3 TESTPATIENT,ONEXXXX T0000 4/8/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (MARCIA TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 4

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

Totals Page

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Division/Clinic Appointment Totals

Division/Clinic Unique

NS NSA NAT Patients

ALBANY/D-PSYCHXXXXXXXXXXXXXXXXXXX 2 1 0 1

ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC 2 1 1 1

TROY1/MENTAL HEALTH 0 0 3 1

#### High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option

This option should be used if you need to re-create the same report that is created by the scheduled SDAM BACKGROUND JOB after midnight each night. The option lists the “NO-SHOW”, “NO-SHOW AUTO REBOOK”, or “No Action Taken” appointments for Mental Health Clinics for the previous day.

This report should not be scheduled to run nightly as it is kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system.

This report is sent in a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.

Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days to list future appointments for. This parameter can be edited, within the range of 1 to 30, by the user by using the option \[XPAR EDIT PARAMETER\] Edit Parameter Values changing the System value. The High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option was modified to include the following changes:

- The provider name is now displayed directly under the No Show appointment information, to keep everything connected.
- Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.
- Appointment line now displays information in two lines:
- line one: count, patient name, Patient ID 1st initial last name+last 4 ssn, appointment D/T, 30 character clinic name
- line two: appointment status abbreviation, appointment provider name.
- Patient ID is now 5 characters: First initial of last name + last 4 of SSN.
- 30-character Clinic name in both future and appointment data information.
- AM and PM removed from the date/time of appt.

The High Risk Mental Health No show Report entry point is called by the scheduling background job. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic.  It will list clinic default provider and future scheduled appointments. The user will not be asked any sort criteria. The report will be sent via email to those persons that are in the SD MH NO SHOW NOTIFICATION mail group.

Example: High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option is displaying a High Risk MH No-Show Nightly Report.

Select OPTION NAME: SD MH

1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

3 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

4 SD MH PROACTIVE BGJ REPORT High Risk MH Proactive Nightly Report

CHOOSE 1-4: 2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

High Risk MH No-Show Nightly Report

...EXCUSE ME, HOLD ON...

This report option generates a mail message containing the

High Risk Mental Health No Show Nightly Report which is sent

only to individuals in the SD MH NO SHOW NOTIFICATION mail group.

DEVISC1A1:MNTVLL 7f3\>D ^XM

All Baskets, New Priority messages: 43

\*=New/!=Priority.............Subject...............Lines.From........Read/Rcvd

!1572. IN \[126400\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1573. IN \[126401\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1574. IN \[126403\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1575. IN \[126404\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1576. IN \[126509\] 02/01/12 Pre-report National Flag 49 HRMH PRF GENERATE JOB

!1577. IN \[126510\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1578. IN \[126511\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1579. IN \[126512\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1580. IN \[126513\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1581. IN \[126514\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1582. IN \[126515\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1583. IN \[126516\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1584. IN \[126517\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1585. IN \[126518\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1586. IN \[126519\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1587. IN \[126520\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1588. IN \[126521\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1589. IN \[126522\] 02/01/12 Pre-report National Flag 12 HRMH PRF GENERATE JOB

!1590. IN \[126523\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1591. IN \[126524\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

VA MailMan 8.0 service for FXXXXXX.XERY_NEYD@ <span class="mark">REDACTED</span>

You last used MailMan: 04/04/13@16:01

You have 861 new messages.

Select MailMan Option: READ/MANAGE MESSAGES

Select message reader: Classic//

Read mail in basket: IN// (2345 messages, 861 new)

Last message number: 2345 Messages in basket: 2345 (861 new)

Enter ??? for help.

IN Basket Message: 1// 2345

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE \# \[#136421\] 04/08/13@11:00 18 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Division/Clinic Appointment Totals

Division/CLinic Unique

NS NSA NAT Patients

ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC 1 0 0 1

Printed at <span class="mark">REDACTED</span> 04/08/13@11:00

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE \# \[#136421\] 04/08/13@11:00 18 lines

From: POSTMASTER In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Division/Clinic Appointment Totals

Division/Clinic

Unique

NS NSA NAT Patients ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC 1 0 0 1

HIGH RISK MENTAL HEALTH NO SHOW NIGHTLY REPORT PAGE 1

By CLINIC for Appointments on 4/7/13 Run: 4/8/2013@10:59

\*STATUS: NS = No Show NSA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC/202

1 TESTPATIENT,TWO T0000 4/7/2013@08:00 LIZ'S MENTAL HEALTH CLINICXX

\*NS PHYSICIAN,ONE

Future Scheduled Appointments:

4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

4/10/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXXX

Enter message action (in IN basket): Ignore//

End reached. Begin again? No// NO

## SD\*5.3\*578 Patch – High Risk Mental Health No Show Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SD\*5.3\*578 High Risk Mental Health No Show Report patch provides two new MH NO SHOW Scheduling Reports, High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\]  and High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\], for use by Suicide Prevention Coordinators and other Mental Health professionals. The reports will support following up with High Risk for Suicide patients who missed a scheduled MH appointment.

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option

The new High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option will display all patients that no showed for their scheduled appointment for a Mental Health clinic. The user is asked for the date range and divisions to display and the report is sorted by Clinic, Mental Health only clinics or Stop Codes. The report will display patient contact information, Next of Kin, emergency contact, clinic default provider, Mental Health Team Coordinator (MHTC) (future release), future scheduled appointments and results of attempts to contact the no showed patients (future release).

#### High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option

The new High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] is called by the scheduling nightly background job Appointment Status Update \[SDAM BACKGROUND JOB\]. This report will display all patients that no showed for their scheduled appointment for a Mental Health clinic. This will be an abbreviated report, listing only Patient appointment information and future scheduled appointments for the patient. As this is a background job, the report will display for the day before, for all the divisions and mental health clinics in the facility. The report will be sent via email to members of the SD MH NO SHOW NOTIFICATION mail group. This report can also be run by calling the option High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]. Access to these two new options should be assigned to the appropriate personnel.

## Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling Outputs menu application provides the capability to produce a variety of reports and letters pertinent to Scheduling procedures. The following is a brief description of the options of the Scheduling Outputs Menu in Software Version 5.3.

<span id="_Toc352927864" class="anchor"></span>Table 3.0 - Scheduling Outputs Menu

| OPTION                                        | DESCRIPTION                                                                                                                                                                                                                                                                |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APPOINTMENT LIST                              | This option is used to generate appointment lists for one/many/all clinics for a specified date.                                                                                                                                                                           |
| APPOINTMENT MANAGEMENT REPORT                 | This option is used to print appointment lists that will help the site implement and manage the new appointment check in requirement.                                                                                                                                      |
| CANCELLED CLINIC REPORT                       | This option is used to generate a report to determine the number of cancelled clinic appointments for National Reporting purposes.                                                                                                                                         |
| CLINIC ASSIGNMENT LISTING                     | This option is used to monitor the size and composition of clinics. Over time, the listings can reflect clinic growth, shrinkage, etc.                                                                                                                                     |
| CLINIC LIST (DAY OF WEEK)                     | This option is used to generate a listing of all active clinics showing which days they meet and, if applicable, the days they will meet in the future.                                                                                                                    |
| CLINIC NEXT AVAILABLE APPT. MONITORING REPORT | This option provides an appointment monitoring tool which reflects the data collected for the access performance measure.                                                                                                                                                  |
| CLINIC PROFILE                                | This option is used to produce a profile of one/many/all clinics.                                                                                                                                                                                                          |
| DISPLAY CLINIC AVAILABILITY REPORT            | This option is used to provide a display of the clinic patterns for the clinics and date range selected. For each selected clinic, the option will print its clinic appointment pattern as well as a listing by appointment date/time of those patients who are scheduled. |
| ENROLLMENTS \> X DAYS                         | This option is used to produce a report showing all enrollments for a selected clinic which exceed a select number of days.                                                                                                                                                |
| FILE ROOM LIST                                | This option is used to generate a list of appointments for a specified day.                                                                                                                                                                                                |
| FUTURE APPOINTMENTS FOR INPATIENTS            | This option is used to produce a report that lists all patients admitted on a particular date that have pending appointments at the facility.                                                                                                                              |
| INPATIENT APPOINTMENT LIST                    | This option is used to produce a list of inpatients that have appointments scheduled for the facility's clinics.                                                                                                                                                           |
| MANAGEMENT REPORT FOR AMBULATORY PROCEDURES   | This option is used to print a statistical report of ambulatory procedures captured through the CPT coding of outpatient visits for a specified date range.                                                                                                                |
| NO-SHOW REPORT                                | This option is used to generate a report of all no-shows entered into the system for specified clinics.                                                                                                                                                                    |
| PATIENT PROFILE MAS                           | This option is used to generate a profile for a selected patient including demographic, clinic, eligibility and Means Test information.                                                                                                                                    |
| PRINT SCHEDULING LETTERS                      | This option is used to print any one of the following types of scheduling letters for a selected date range: Appointment Cancelled, Clinic Cancelled, No-Show or Pre-Appointment.                                                                                          |
| PROVIDER/DIAGNOSIS REPORT                     | This option is used to print a report of outpatient encounters for a selected date range sorting by Division and Outpatient Encounter Date. You also may choose two of the following additional sorts: Provider, Diagnosis, Patient, Clinic, or Stop Code.                 |
| RADIOLOGY PULL LIST                           | This option is used to generate a listing of all patients whose radiology reports/films are required for their scheduled appointments.                                                                                                                                     |
| ROUTING SLIPS                                 | This option is used to produce routing slips for one individual patient, all patients, or add-ons (patients scheduled for appointments since routing slips were last printed).                                                                                             |
| VISIT RPT BY TRANSMITTED OPT ENCOUNTER        | This option is used to generate a report providing encounter and visit information for a specified date range.                                                                                                                                                             |
| WORKLOAD REPORT                               | This option is used to generate a variety of reports showing clinic workload. These help in determining the kinds of activity within clinics during a specified date range.                                                                                                |

### Appointment List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appointment List option is used to generate appointment lists for one/many/all clinic(s) for a specified date.. At multidivisional facilities, one/many/all divisions may be specified. You may include only “count” clinics, “non-count” clinics, or both. All clinics chosen have to be associated with one of the selected divisions. Primary care assignment information may be included in the output if so desired.

You may specify the number of desired copies of the list. A separate list is produced for each designated clinic and appointments are listed chronologically by appointment time within each list.

The appointment list generated will include the name and date of the clinic, the run date, appointment time, patient name, phone number, and SSN. If applicable, the following data will also be provided: lab, x-ray, and EKG test times, ward location, room/bed, and other patient-specific information.

This may include service-connected percentage, patient being seen as collateral; patient is enrolled over a year and is a non-vet or NSC, chart requested and current Means Test status and date of the last test, or if there is an entry in the MEANS TEST file.

If a NSC patient has been enrolled for more than one year, a message will print to that effect asking that the patient be re-evaluated. Overbooks will be denoted by an asterisk (\*) beside the patient name.

A variety of messages, such as those regarding Means Test status and Copay Exemption status, are displayed when applicable.

If you are utilizing a device with barcode capabilities, you may choose to have the patient's SSN printed in barcode form. If wands are available at clinic locations, these barcodes may be used for patient check in and checkout.

A variety of messages, such as those regarding Means Test status, Copay Exemption status, and GAF Score are displayed when applicable.

### Appointment Management Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appointment Management Report option is used to print lists that will help your site implement and manage the appointment check in requirement.

You are first prompted for the date range you wish the report to cover. The date range must begin on 10/1/92 or later and end no later than the current date.

The statistics criterion you may choose includes “Statistics” or “Division(s) Only Statistics”. The report format selections include “Appointment Clinic” or “Stop Code”.

If "Statistics" is selected, you may then select one/many/all divisions and one/many/all clinics, or one/many all stop codes. A page will print for each division selected as well as a totals page for the medical center. If "Division(s) Only Statistics" is selected, you may print data for one/many/all divisions but individual clinics/stop codes cannot be chosen.

The data provided will be for all clinics/stop codes in the selected division(s). It should be noted that non-count clinics will be excluded.

After you have set the specifications for the report, you will be given an opportunity to edit your selections, if needed.

All reports should be queued to a printer at 132 columns. Once the output has been queued, it will be assigned an internal task number. This is the number you would use to identify the task to IRM service should problems occur.

### Cancelled Clinic Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancelled Clinic Report was created to aid the sites with the requirement to report the number of cancelled clinic appointments. This report prints in 132 column format.

The user will need to input a beginning date and an end date for the reporting period and select either the detail report or the summary report.

The detail report includes the Division, Status, Patient Name, SSN, Appointment Date, Clinic, Cancellation Date, and the User. The detail report is sorted by Division, Status, and then Clinic, with a subtotal for each Status within the Division, and then Total Cancellations for the report.

The codes for Status are:

- C Clinic Cancelled.
- CA Clinic Cancelled and Auto Re-Book
- PC Patient Cancelled
- PCA Patient Cancelled and Auto Re-Book

The summary report includes the Division, Clinic, Number of appointments cancelled by the clinic, Number of appointments cancelled by the clinic RB (re-booked), Number of appointments cancelled by the patient, and Number of appointments cancelled by the patient RB (re-booked).

The summary report is sorted on Division and then Clinic, with one line per Clinic within the Division, and then Total Cancellations for the report.

#### Clinic Assignment Listing 

The Clinic Assignment Listing option is used to monitor the size and composition of clinics. It is designed to be used as a management tool. Over time, the listings can reflect clinic growth, shrinkage, etc.

The listing may be sorted by clinic or stop code. You may choose all clinics/stop codes or an individual clinic/stop code. You may request only actively enrolled patients be included (those with future appointments) or you may include those patients plus those with no future appointments.

Patient specific information is provided including name, SSN, status, eligibility code, \# of days enrolled, date of last visit, date of next appointment, and age. Eligibility code totals and Means Test totals are also displayed.

Depending on the user selections, this report could be quite lengthy. You may wish to run it during off hours. This report should be printed at a 132 column margin width.

#### Clinic List (Day of Week) 

The Clinic List (Day of Week) option is used to generate a listing of all clinics showing which days they meet and, if applicable, the days they will meet in the future. All active clinics will be included and will be listed in alphabetical order.

At multidivisional facilities, you may choose the division for which to print the clinic list.

The running time for this report will be proportional to the number of clinics at your facility.

#### #### Clinic Next Available Appt. Monitoring Report

The Clinic Next Available Appt. Monitoring Report option has been provided as part of the functionality to extract data from each facility showing the waiting time in days for each clinic assigned specific stop codes. The report reflects the actual data (not an average) as of the date/time it is run. The clinics which appear on the report may be selected by division, clinic, or stop code.

The following is an explanation of the columns found on the report.

| MONITORING REPORT TOPIC   | EXPLANATION                                                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------|
| WAIT IN DAYS              | This is the number of calendar days until the first available appointment and does not count the date the report is run. |
| SLOTS PER OPEN DAY        | This is the number of slots (booked and not booked) found on the date the report is run.                                 |
| APPTS PER OPEN DAY        | This is the number of appointments (booked) found on the date the report is run.                                         |
| SLOTS TO FIRST AVAIL APPT | This is a count of the number of slots (booked and not booked) until the first available appointment.                    |
| APPTS TO FIRST AVAIL APPT | This is the number of slots (booked) until the first available (open) slot.                                              |
| OPEN DAYS TO FIRST APPT   | This is the number of clinic days until the first available appointment.                                                 |
| OPEN DAYS                 | Does the clinic meet on the date the report is run? 1=YES, 0=NO.                                                         |
| OVERBOOK RATE             | This is the percentage found when dividing the APPTS TO FIRST AVAIL APPT value by the SLOTS TO FIRST AVAIL APPT value.   |

### Clinic Profile 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic Profile option is used to produce a profile of one, many or all clinics. At multidivisional facilities, you may choose to generate the profile of clinics associated with one, many or all divisions. The clinics will be profiled as of the date the report is requested, providing the most current information available.

Some of the data elements included in each profile may be: clinic name, abbreviation (if any), telephone number and location of clinic, days clinic meets, start date, increments, hour display begins, appointment length, variable length, max overbooks/day, stop code, credit stop code, non-count clinic, access to clinic prohibited, and max \# days for future booking. Checkout parameters including default provider and diagnosis for each clinic are also displayed.

The following is a brief explanation of some of the data elements listed on the report.

| CLINIC PROFILE REPORT TOPIC | EXPLANATION                                                                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NON-COUNT CLINIC            | If answered YES, clinic will not impact on AMIS statistics.                                                                                                                                               |
| CREDIT STOP CODE            | Stop code that will be credited in addition to normal stop code if clinic is so specified.                                                                                                                |
| START DATE                  | Date clinic was initially set up.                                                                                                                                                                         |
| INCREMENTS                  | Number of slots per hour.                                                                                                                                                                                 |
| VARIABLE                    | Variable length appointments.                                                                                                                                                                             |
| PROHIBIT ACCESS TO CLINIC   | Indicates if the clinic is restricted to privileged users. If the clinic is temporarily or permanently inactivated, or is scheduled to be inactivated, this information will be displayed in the profile. |

# ### Display Clinic Availability Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Clinic Availability Report option provides a display of the clinic patterns for the clinics and date range selected. You may run it for all clinics and divisions within your facility, or you may specify individual divisions and clinics.

For each selected clinic, the option will print its clinic appointment pattern as well as a listing by appointment date/time of those patients who are scheduled. The SSN and the appointment length will be displayed for each patient.

The clinic appointment pattern shows the number of available slots, scheduled slots, and overbooks. A legend is included in the report which explains the symbols used.

Individual appointments cancelled through the Cancel Appointment option are re-incremented accordingly on the appropriate clinic availability pattern and do not appear on the listing of appointments. The clinic availability pattern does not take into account unscheduled visits or no-shows.

In order to get a true picture of the actual number of slots for a clinic, you should refer to the listing of patients beneath the clinic availability pattern. Unscheduled patient visits will always be listed.

To include no-shows and those patients who were scheduled in time slots for which the clinic availability was cancelled, the user must specify inclusion of no-shows and cancellations.

Patients who were cancelled due to cancellation of the entire clinic will be designated by a "\*".

### Enrollments \> X Days 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables you to produce a report showing all enrollments for a selected clinic that exceed a select number of days.

The report provides patient name, SSN, enrollment date, eligibility code, and patient status (OPT or AC). If a patient has pending appointments for the selected clinic, they will also be displayed.

If you are at a multidivisional facility, you will be able to produce this report for the division of your choice.

### File Room List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Room List option is used to generate a listing of appointments for a specified day. This listing may be by terminal digit order where all patients with appointments on that day will be consecutively listed, or the listing may be by clinic where a separate page will print out for each clinic.

Information provided includes the clinic name and date, date report printed, patient name and social security number, time of visit, and appointment type.

When a chart has been requested but no appointment is scheduled (such as may be done through the Chart Request option of the Appointment Menu), the appointment time and type will not appear on the file room list. When printed, each clinic will print on a separate page.

### Future Appointments for Inpatients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Through this option, you may produce a report that lists all patients admitted on a particular date that have pending appointments at the facility. The report is sorted alphabetically by patient name and includes the patient ID#, ward, scheduled appointment date/time and clinic.

Using this information, appointments may be kept, cancelled or rescheduled as necessary.

### Inpatient Appointment List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to produce a list of inpatients that have appointments scheduled for the facility's clinics. The listing is printed for a selected date range and may be run for all wards or an individual ward.

The following data items may be provided on the list: patient name, SSN, clinic, appointment date/time, ancillary appointments, and specific patient information.

### Management Report for Ambulatory Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Management Report for Ambulatory Procedures option allows you to print a statistical report of ambulatory procedures captured through the CPT coding of outpatient visits for a specified date range. You may print either a brief or expanded report.

The report may be sorted by clinic or service and may be printed for one/many/all clinics/services. Each clinic/service will print on a separate page and contain the following information: the selected date range, date printed, clinic/service name, the number of procedures and stops, the total number of patients, subtotals for male and female patients, and the average patient age. A final summary page of all selected clinics or services will be provided including the number of visits.

If you choose to print an expanded report, a "Summary of Procedures Performed" will be included for each service or clinic. This summary is sorted either by procedure or patient name and may be printed for one/many/all patients or procedures. Some of the data items which may be included in the summary are: the CPT code and brief description of the procedure; CPT modifier with brief description; the patient's name, social security number and age; the date and time the procedure was performed; the number of times the procedure was performed during the selected date range; and subtotals for veteran and non-veteran patients.

At multidivisional facilities, one/many/all divisions may be selected.

The report should be sent to a printer, as it was not designed to be displayed on the screen.

### No-Show Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The No-Show Report option generates a report of all no-shows entered into the system for specified clinics. The report can be run for one, many or all clinics.

A range of clinics may also be selected, such as all clinics whose names begin with the same letters. This will limit the number of keystrokes needed to choose those clinics.

The output can be generated for a date range or a single date. At multi-divisional facilities, you may print the report for a single division or all divisions.

The output is divided into two sections for each selected clinic with each section printing on a separate page.

- The first section lists the date of the clinic, the time of the no-show appointment, the patient's name and social security number, the clerk's name who entered the no-show, and the date/time rebooked if applicable.
- The second section lists the date of the clinic, the total number of no-shows, a breakdown of that total into rebooked/not rebooked appointments, and the percentage of the appointments that were no-shows for the selected clinic during that time period.

Lastly, a totals page is produced. This provides the same information found in the second section of the individual clinic reports except for ALL the selected clinics combined. The date and time run, page number, dates report covers, and appropriate division/clinic name appear on the top of each page of the individual clinic outputs.

You may choose to print the report for NO SHOWS ONLY or BOTH NO SHOWS & NO ACTION TAKEN. If you choose BOTH NO SHOWS & NO ACTION TAKEN, appointments with a status of NO ACTION TAKEN will be included in the report.

For appointments with this status, UNKNOWN will be displayed for CLERK. These appointments will also be included in the TOTAL NO-SHOWS W/NO REBOOK APPTS column of the totals page that prints at the end of each section of the report.

Please note that NON-COUNT clinics are included in the reporting process. If an appointment in a NON-COUNT clinic is in NO SHOW status, it will appear on both reports. If an appointment is left in NON-COUNT status, it appears on the BOTH NO SHOWS & NO ACTION TAKEN report because the system considers the NON-COUNT status to be the same as a NO ACTION TAKEN. For appointments left in a NON-COUNT status, the display for CLERK will be UNKNOWN.

- A table of contents is provided with this report if sent to a printer.
- Due to the processing sequence, this table prints at the end of the output. You may wish to insert this page at the beginning of the report.
- When generated, each clinic will print on a separate page.

### Patient Profile MAS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Profile MAS option is used to generate a complete profile for a patient or a profile for a specified date range. Information which may be accessed includes demographic, appointments, add/edits, dispositions, enrollments, means test, and team information.

You may utilize either the roll-and-scroll format or the List Manager format while using this option. The same information is available through both formats. To choose the List Manager format, answer NO at the “Do you want to print the profile?” Do you need the prompt?

The following are the available actions that may be selected.

| PATIENT PROFILE REPORT TOPIC | EXPLANATION                                                                                |
|------------------------------|--------------------------------------------------------------------------------------------|
| DISPLAY INFO                 | Allows you to display selected information to the screen.                                  |
| PRINT PROFILE                | Allows you to print selected information to a specified device.                            |
| CHANGE PATIENT               | Allows you to enter another patient without exiting the option.                            |
| CHANGE DATE RANGE            | Allows you to select another date range for the same patient without exiting the option.   |
| TEAM INFORMATION             | Allows you to display information for all teams to which the selected patient is assigned. |

### Print Scheduling Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print any one of the following types of scheduling letters for a selected date range.

- APPOINTMENT CANCELLED
- CLINIC CANCELLED
- NO-SHOW
- PRE-APPOINTMENT

You may choose to print the letter assigned to the clinic (through Set up a Clinic option) or another letter of the same type. If you choose to print an assigned letter and the selected clinics do not have letters of the corresponding type assigned to them, no letters will print for those clinics. If you choose to print a letter other than the letter assigned to the clinic(s), the letter you select will print for all selected patients and clinics.

For PRE-APPOINTMENT type letters - if ALL is entered at the “Select clinic” prompt, letters will not print for any clinics designated as non-count clinics.

If you wish to print letters for the majority of clinics, enter ALL at the “Select clinic” prompt. You will then be asked if you wish to exclude any clinics and, if so, to name those clinics. This action prevents having to enter numerous individual clinic names.

A list of those patients with a Bad Address indicator will print after requested letters have printed. Letters for those patients will not print.

### Provider/Diagnosis Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a report of outpatient encounters for a selected date range. The Provider/Diagnosis Report sorts by division and outpatient encounter date. You also may choose two of the following additional sorts: provider, diagnosis, patient, clinic, or stop code.

Data contained in the report includes patient name and last four digits of SSN, encounter date and time, clinic name and stop code, provider and diagnostic code. The report is formatted to print at 132 columns. Depending on your sort selections, you may wish to queue to print during non-peak hours.

The totals of this report will vary depending on how the site uses the add/edit stop code functionality. If additional stop codes are added through the AE (add/edit) action of the Appointment Management option, the stop code will be associated with the scheduled appointment's date/time. Depending on sort criteria, these entries may print on the Provider/Diagnosis Report and may/may not be included in the totals.

If additional stop codes are added through the menu option Add/Edit Stop Codes, the entries will have different times than the actual appointment. In this case, these entries will print on this report and be included in the totals. For example, a clerk needs to add/edit a stop code for 108.

Using the Add/Edit Stop Codes menu option, the referring clinic is entered as the Associated Clinic. When the Provider/Diagnosis report is generated for that clinic, it will count this stop code as workload.

In order for this report to be accurate, sites need to make the following adjustments:

- Add/edit stop codes only through the use of the AE action of the Appointment Management option.
- When using the Add/Edit Stop Codes option, change the procedure for Associated Clinic.

### Radiology Pull List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Radiology Pull List option is used to generate a listing of all patients whose radiology reports/films are required for their scheduled appointments. The report is run by date and sorted by terminal digit (SSN). The listing includes patient name, SSN, clinic name, and appointment date/time. Any appointments the patient has scheduled for later that same day will also be displayed.

Routing Slips The Routing Slips option is used to print routing slips for one individual patient, all patients, or add-ons (patients scheduled for appointments since routing slips were last printed).

The routing slips may be sorted to print by terminal digit, patient name, clinic name, or physical location. When sorted by clinic, one, many (limit 20), or all clinics may be included.

When sorted by physical location, if the PHYSICAL LOCATION field (#10) of the HOSPITAL LOCATION file (#44) record is not populated, then the generic value of “Not Defined” will be used so that it shows up on the report (and will sort accordingly, as if the physical location began with “N”).

If the slip is a reprint of a previous run, the original run date is also shown.

The routing slip shows the patient's rated disabilities and health insurance data, when applicable. Any future appointments are also listed (limited to the number that will fit on one page).

An area is provided to list the diagnoses and procedures performed during the clinic visits on that day and the classification questions are included when applicable.

A routing slip may be printed for a single patient even if there are no clinic visits scheduled for that patient on that day.

When all routing slips are printed, a total page will be provided showing the facility name, date and time the slips were printed, and the total number of slips printed.

### Visit Rpt By Transmitted Opt Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Visit Report by Transmitted Outpatient Encounter option provides a report which contains encounter and visit information. The report is divided into two sections. The first displays the transmission status of the encounters to the National Patient Care Data Base (NPCDB) for the selected date range.

Statuses include the following.

| VISIT REPORT TOPIC | EXPLANATION                      |
|--------------------|----------------------------------|
| WAITING            | WAITING TO BE TRANSMITTED        |
| TRANSMITTED        | TRANSMITTED BUT NOT ACKNOWLEDGED |
| ACKNOWLEDGED       | TRANSMITTED AND ACKNOWLEDGED     |

The second section consolidates those encounters into total visits. You may select to print either section or both sections.

Encounters are grouped by veteran eligibility and then by category of visit. Compensation and Pension is an appointment type and is included in the Category of Visit totals. This breakout is for information only.

A visit consists of all encounters for a patient for a day. Visits are counted by facility so if a patient has one encounter in one division, and another encounter in a different division, only one visit is counted.

At multi-divisional facilities, you will have the option of printing division and site totals or site total only.

### Workload Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Workload Report option is used to generate a variety of reports showing clinic workload, facilitating determination of the kinds of activity within clinics during a specified date range. It allows for comparison of clinic or stop code activity for a specified time frame between the selected year and the previous year.

After the user specifies a date range for the report, the system will verify that the outpatient encounter status update process has been performed for each date in the range. If any of the dates have not been processed by this update logic, the user will be warned and generation of the workload report will be allowed to continue. However, the user will be advised to run the report again, after the update process has been completed (Appointment Status Update option, Supervisor Menu), to obtain more accurate workload data.

The user has the ability to sort the report by clinic or stop code and clinic. A brief or expanded report may be selected. A brief report only generates the comparison of selected clinics or stop codes between the selected year and previous year, showing number of visits for each year, net change, and change percentage.

The expanded report includes the comparison (if desired) plus a summary of each clinic selected. Number of scheduled appointments, unscheduled appointments, inpatient appointments, and overbooks are some of the data elements displayed.

The user may choose to display the report for individual clinic meetings or a summary of the month. The patient names may/may not be displayed.

If the report is run by stop code, the add/edits may be included. Cancelled appointments will appear on this report if they were entered through either the Cancel Clinic Availability option or the Cancel Appointment option.

All appointments with a status of NO ACTION TAKEN will be included in the NO-SHOWS column of the report.

The total patients seen are calculated as follows:

Scheduled + Unscheduled + Inpatients + Overbooks + Add/Edits = Total Patients Seen

Depending on selected specifications, this report may be quite lengthy. You may choose to run the report during off hours. When printed, each clinic will appear on a separate page.

## HRMHP No Show and Proactive Options & Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Scheduling Reports are available when the High Risk Mental Health Patient – Reminder & Flag (HRMHP) project is installed at your site.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pims-version-5-3-user-manual-outputs-menu/006.png)</th>
<th><p>NOTE: The MH NO SHOW and the MH PROACTIVE reports are not part of the output menus.</p>
<p>IRM staff will need to assign these report options to the primary or secondary menu options of the Suicide Prevention Coordinator, Mental Health Treatment Coordinator, and other Mental Health Professionals.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>MH NO SHOW OPTIONS &amp; FEATURES</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>High Risk MH No-Show Adhoc Report [[SD MH NO SHOW AD HOC REPORT]</td>
<td><p>This Scheduling option provides a High Risk MH No-Show Adhoc Report for use by Suicide Prevention Coordinators and other Mental Health professionals.</p>
<p>This report supports following up with High Risk for Suicide patients who missed a scheduled MH appointment. It displays all patients that no-showed for their scheduled appointment.</p></td>
</tr>
<tr class="even">
<td>High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ]</td>
<td><p>This Scheduling option provides a High Risk MH No-Show Nightly Report. This report supports actions relating to following up with High Risk for Suicide patients that missed their MH appointment.</p>
<p>This report is generated at the end of the Scheduling Nightly Background Job (SDAM BACKGROUND JOB), and will be sent in a Mailman message to members of the SD MH NO SHOW NOTIFICATION mail group.</p>
<p>This report may also be run by calling the option High Risk MH No-Show Nightly Report.</p>
<p>Future appointments will list on this report. The number of days (quantity of future appointments) that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days to list future appointments for each patient on the report. This parameter can be edited by the user, within the range of 1 to 30, by using the option [XPAR EDIT PARAMETER] Edit Parameter Values.</p></td>
</tr>
<tr class="odd">
<td>High Risk MH Proactive Nightly Report [SD MH PROACTIVE BGJ REPORT]</td>
<td><p>This report is a background job that will list the daily appointments for patients with a High Risk for Suicide PRF.</p>
<p>This report will be kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system.</p>
<p>This report is sent in a mail message to members of the SD MH NO SHOW NOTIFICATION mail group.</p>
<p>Future appointments will be listed on this report. The number of days (of future appointments) is defaulted to 30 days in the future.</p>
<p>A new parameter SD MH PROACTIVE DAYS has been added to store the number of days to list future appointments for each patient on the report. This parameter can be edited by the user, within the range of 1 to 30, by using the option [XPAR EDIT PARAMETER] Edit Parameter Values.</p></td>
</tr>
<tr class="even">
<td>High Risk MH Proactive Adhoc Report [SD MH PROACTIVE AD HOC REPORT]</td>
<td><p>This Adhoc report option generates a proactive report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications.</p>
<p>This option generates the HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY CLINIC for Appointments Report that can be sorted by all clinics or by Mental Health clinics only. This report allows users to refine their report to their specifications.</p>
<p>This report display appointments for High Risk for Suicide patients that have appointments for today, by divisions for all patients with Patient Record Flag (PRF) High Risk for Suicide that have appointments in mental health clinics today, totals to show the number of unique patients by division, list patients alphabetically by division and by date/time of the appointment, and will also display national as well as local PRF activity.</p></td>
</tr>
<tr class="odd">
<td>High Risk MH No-Show Adhoc Report and High Risk MH No-Show Nightly Report</td>
<td><p>These reports supports following up with High Risk for Suicide patients who missed a scheduled MH appointment. It displays all patients that no-showed for their scheduled appointment.</p>
<p>The following information has been added to BOTH reports:</p>
<ul>
<li><p>The provider name is displayed directly underneath the No Show Appointment information</p></li>
<li><p>Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.</p></li>
<li><p>Appointment line now displays information in two lines:</p>
<ul>
<li><p>line one: count, patient name. Patient ID 1st initial last name + last 4 SSN, appointment D/T, 30 character clinic name</p></li>
<li><p>line two: appointment status abbreviation, appointment provider name</p></li>
</ul></li>
<li><p>Patient ID is now 5 characters: first initial of last name + last 4 of SSN</p></li>
<li><p>30-character Clinic name in both future and appointment data information</p></li>
<li><p>AM and PM removed from the date/time of appointment.</p></li>
</ul>
<blockquote>
<p>The following information has been added only to the High Risk MH No-Show Adhoc Report:</p>
</blockquote>
<ul>
<li><p>The report now displays the name of the Mental Health Treatment Coordinator (MHTC) and the name of the care team they are assigned to in parentheses</p></li>
<li><p>The results of the no show patient contact</p></li>
<li><p>Results added for resolution: Reminder term and health factor Information.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## ### High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This High Risk Mental Health No Show Ad Hoc Report is for use by Suicide Prevention Coordinators and other Mental Health professionals. It supports following up with High Risk for Suicide patients who missed a scheduled MH appointment.

The report displays patient contact information, next of kin, emergency contact, the assigned clinic provider, the Mental Health Treatment Coordinator (MHTC) and any new scheduled appointments. It shows Future scheduled appointments and results of attempts to contact the no showed patients.

This option will list by one, many or All stop codes / clinics or only Mental Health stop codes and clinics defined in the Reminder Location List file under the ‘VA-MH NO SHOW APPT CLINICS LL’ entry.

A series of user prompts will be asked to refine the report.

- The user will be asked to select a beginning and ending date; this lists the report within a certain date range.
- The division of interest will be asked of the user: The report can list by one, many or all divisions.
- The user will be asked to choose how the report should sort: by (M)ental Health Quick List, which will list only those clinics defined in the Reminder Location list, or by (C)linics or (S)top codes both of which will further prompt the user to refine the sort. If ?, ?? Is entered by the user, a help prompt will be displayed.
- If the user selects to sort by (S)top codes or ( C )linics, a prompt asking them to select stop codes/clinics by listing (A)ll stop codes/clinics, (mental health as well as non mental health) or (M)ental Health stop codes only (that are defined in the Reminder Location List) and are stop codes in the divisions chosen to list in this report. Both selections will allow the user to choose one, many, or all stop codes.
- A prompt asking the number of days in the future to list the Future scheduled appointment is asked and will list the future scheduled appointments that many days in the future.

When the report displays or prints:

- The division/Stop Code Name/Number will display on the report once for all patients who have no showed for that Stop Code and division. It will display again, when the stop code or division changes.
- A totals page will be displayed at the end of the report.
- The name of the MHTC and the name of the care team they are assigned to in parentheses.
- The provider name is displayed directly underneath the NO Show Appointment information, to keep everything connected.
- The results of the no show patient contact.
- Results for resolution: Reminder term and health factor information.

|                                                                                                                                          |                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pims-version-5-3-user-manual-outputs-menu/007.png) | Special Note: at the Select Stop Code prompt , the stop code may be selected by the stop code file number (as an example, selecting 188 below) or by the AMIS Reporting stop code ( 500 – 599 code numbers ). |

### High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient with a High Risk for Suicide Patient Record Flag (PRF) misses a Mental Health clinic appointment due to a no-show, an automatic nightly report is run that lists patients who have a MH clinic appointment with “NO-SHOW”, “NO-SHOW AUTO-REBOOK ,“ or “No Action Taken” status.

This report is generated at the end of the Scheduling Nightly Background job, and will be sent in a Mailman message to members of the mail group SD MH NO SHOW NOTIFICATION. All persons in this mail group will receive the High Risk MH No-Show Nightly Report that is generated from the scheduling nightly background job.

This option may be run manually if there is an error in running the nightly report. It will list patients for all mental health clinics/stop codes that are defined in the Remote location list “VA-MH NO SHOW APPT CLINICS LL.”

The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days to list future appointments for.

### High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The High Risk MH Proactive Adhoc Report option generates the new HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY CLINIC for Appointments Report that can be sorted by all clinics or by Mental Health clinics only.

The HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY CLINIC report is more flexible by allowing users to refine the report to their specifications. This new report display appointments for High Risk for Suicide patients that have appointments for today, by divisions for all patients with Patient Record Flag (PRF) High Risk for Suicide that have appointments in mental health clinics today, totals to show the number of unique patients by division, list patients alphabetically by division and by date/time of the appointment, and will also display national as well as local PRF activity.

### High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Report creates a listing of patients who are flagged as High Risk For Suicide and have Mental Health appointments for the day.

This report is generated at the end of the Scheduling Nightly Background job, and will be sent in a Mailman message to members of the mail group SD MH NO SHOW NOTIFICATION. All persons in this mail group will receive the High Risk MH Proactive NightlyReport. It will list patients for all mental health clinics/stop codes that are defined in the Remote location list “VA-MH NO SHOW APPT CLINICS LL.”

The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SDMH PROACTIVE DAYS has been added to store the number of days to list future appointments for.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also please refer to the following sites: National Acronym Directory at <http://vaww1.va.gov/Acronyms/>
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TERMS</strong></th>
<th><strong>DEFINITION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADD-ONS</td>
<td>Patients who have been scheduled for a visit after routing slips for a particular date have been printed.</td>
</tr>
<tr class="even">
<td>ALOS</td>
<td>Average Length of Stay</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="even">
<td>ANCILLARY</td>
<td>A test added to an existing appointment (i.e. lab, x-ray, EKG) test</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="even">
<td>ASU</td>
<td>Authorization/Subscription Utility</td>
</tr>
<tr class="odd">
<td>BILLINGS</td>
<td>Bills sent to veteran</td>
</tr>
<tr class="even">
<td>BRD</td>
<td>Business Requirements Document</td>
</tr>
<tr class="odd">
<td>CLINIC PULL LIST</td>
<td>A list of patients whose radiology/MAS records should be pulled from the file room for use in conjunction with scheduled clinic visits</td>
</tr>
<tr class="even">
<td>COLLATERAL</td>
<td>A visit by a non-veteran patient whose appointment is related to or visit associated with a service-connected patient's treatment.</td>
</tr>
<tr class="odd">
<td>COMPUTERIZED PATIENT RECORD SYSTEM (CPRS)</td>
<td>An integrated, comprehensive suite of clinical applications in VistA that work together to create a longitudinal view of the veteran’s Electronic Medical Record (EMR). CPRS capabilities include a Real Time Order Checking System, a Notification System to alert clinicians of clinically significant events, Consult/Request tracking and a Clinical Reminder System. CPRS provides access to most components of the patient chart.</td>
</tr>
<tr class="even">
<td>CPT</td>
<td>Current Procedural Terminology</td>
</tr>
<tr class="odd">
<td>CR</td>
<td>Clinical Reminders</td>
</tr>
<tr class="even">
<td>CST</td>
<td>Conversion Specification Templates</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td>Database Integration Agreement</td>
</tr>
<tr class="even">
<td>DRG</td>
<td>Diagnostic Related Group</td>
</tr>
<tr class="odd">
<td>GMTS</td>
<td>Health Summary namespace</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphic User Interface</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level Seven</td>
</tr>
<tr class="even">
<td>ICR</td>
<td>Integration Control Reference</td>
</tr>
<tr class="odd">
<td>IRT</td>
<td>Incomplete Records Tracking</td>
</tr>
<tr class="even">
<td>IVMH</td>
<td>Improve Veteran Mental Health</td>
</tr>
<tr class="odd">
<td>MEANS TEST</td>
<td>A financial report upon which certain patients' eligibility for care is based</td>
</tr>
<tr class="even">
<td>MENTAL HEALTH TREATMENT COORDINATOR (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one Mental Health treatment coordinator per patient and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH treatment coordinator’s responsibilities, see VHA Handbook 1160.1, “Uniform Mental Health Services in VA Medical Centers for Clinics,” page 3-4. Note: In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
</tr>
<tr class="odd">
<td>MH</td>
<td>Mental Health</td>
</tr>
<tr class="even">
<td>MHA3</td>
<td>Mental Health Assistant 3 package</td>
</tr>
<tr class="odd">
<td>MHTC</td>
<td>Mental Health Treatment Coordinator</td>
</tr>
<tr class="even">
<td>NO SHOW</td>
<td>A person who did not report for a scheduled clinic visit without prior notification to the medical center.</td>
</tr>
<tr class="odd">
<td>NON-COUNT</td>
<td>A clinic whose visits do not affect AMIS statistics.</td>
</tr>
<tr class="even">
<td>NSR</td>
<td>New Service Request</td>
</tr>
<tr class="odd">
<td>OE/RR</td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>OPC</td>
<td>Outpatient Clinic</td>
</tr>
<tr class="odd">
<td>OR</td>
<td>CPRS Order Entry/Results Reporting namespace</td>
</tr>
<tr class="even">
<td>PAF</td>
<td>Patient Assessment File; where PAI information is stored until transmission to Austin.</td>
</tr>
<tr class="odd">
<td>PAI</td>
<td>Patient Assessment Instrument</td>
</tr>
<tr class="even">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="odd">
<td>PCMM</td>
<td>Primary Care Management Module</td>
</tr>
<tr class="even">
<td>PRF</td>
<td>Patient Record Flag</td>
</tr>
<tr class="odd">
<td>PRINCIPAL MENTAL HEALTH PROVIDER (PMHP)</td>
<td>See MH Treatment Coordinator (MHTC)</td>
</tr>
<tr class="even">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="odd">
<td>PULL LIST</td>
<td>A list of patients whose radiology/PIMS records should be "pulled" from the file room for scheduled clinic visits</td>
</tr>
<tr class="even">
<td>PX</td>
<td>Patient Care Encounter namespace</td>
</tr>
<tr class="odd">
<td>PXRM</td>
<td>Clinical Reminders package namespace</td>
</tr>
<tr class="even">
<td>RAM</td>
<td>Resource Allocation Methodology</td>
</tr>
<tr class="odd">
<td>REMINDER DEFINITIONS</td>
<td>These are pre-defined sets of findings that are used to identify patient cohorts and reminder resolutions. The reminder is used for patient care and/or report extracts.</td>
</tr>
<tr class="even">
<td>REMINDER DIALOGS</td>
<td>These are pre-defined sets of text and findings that provide information to the CPRS GUI for collecting and updating appropriate findings while building a progress note.</td>
</tr>
<tr class="odd">
<td>REMINDER TERMS</td>
<td>Terms are used to map local findings to national findings, providing a method to standardize the findings for national use. These are also used for local grouping of findings for easier reference in reminders and are defined in the Reminder Terms file.</td>
</tr>
<tr class="even">
<td>ROUTING SLIP</td>
<td>When printed for a specified date, it shows the current appointment time, clinic, location, and stop code. It also shows future appointments.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td>Remote Procedure Calls</td>
</tr>
<tr class="even">
<td>RSD</td>
<td>Requirements Specification Document</td>
</tr>
<tr class="odd">
<td>RUG</td>
<td>Resource Utilization Group</td>
</tr>
<tr class="even">
<td>SBR</td>
<td>Suicide Behavior Report</td>
</tr>
<tr class="odd">
<td>SHARING AGREEMENT</td>
<td>Agreement or contract under which patients from other government agencies or private facilities are treated.</td>
</tr>
<tr class="even">
<td>SME</td>
<td>Subject Matter Expert</td>
</tr>
<tr class="odd">
<td>SPECIAL SURVEY</td>
<td>An ongoing survey of care given to patients alleging Agent Orange or Ionizing Radiation exposure. Each visit by such patients must receive "special survey dispositioning" which records whether treatment provided was related to their exposure. This data is used for Congressional reporting purposes.</td>
</tr>
<tr class="even">
<td>STOP CODE</td>
<td><p>A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit.</p>
<p>Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.</p></td>
</tr>
<tr class="odd">
<td>THIRD PARTY</td>
<td>Billings where a party other than the patient is billed</td>
</tr>
<tr class="even">
<td>TIU</td>
<td>Text Integration Utility</td>
</tr>
<tr class="odd">
<td>TSR</td>
<td>Treating Specialty Report</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Information System and Technology Architecture</td>
</tr>
</tbody>
</table>
