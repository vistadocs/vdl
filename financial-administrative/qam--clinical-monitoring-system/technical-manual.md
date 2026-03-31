---
title: Clinical Monitoring System Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: QAM
app_name: Clinical Monitoring System
section: FIN
app_status: active
pkg_ns: QAM
patch_ver: 1
patch_id: QAM*1
group_key: "QAM:QAM:1"
file_numbers: []
security_keys: []
menu_options: 1
description: - [# Introduction / Package-Wide Variables](#introduction-package-wide-variables) - [# Implementation and Maintenance](#implementation-and-maintenance) - [# Routines](#routines) - [Routine List](#routine-list) - [Callable Routines](#callable-routines) - [# Files](#files) - [File List](#file-list) -
audience: 
keywords: 
  - class
  - table
  - monitor
  - even
  - contents
  - condition
  - time
  - options
  - style
  - width
page_count: 0
word_count: 8103
section_count: 20
table_count: 26
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 2/23/09
revision_oldest: 2/23/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmtm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cmtm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=32"
---

![](clinical-monitoring-system-version-1-technical-manual/001.png)

Clinical Monitoring System V. 1.0Technical ManualSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 2/23/09

| Date    | Description (Patch \# if applic.) | Project Manager | Technical Writer |
|---------|-----------------------------------|-----------------|------------------|
| 2/23/09 | Reformatted Manual                |                 | REDACTED         |

Table of Contents

# # Introduction / Package-Wide Variables


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction / Package-Wide Variables](#introduction-package-wide-variables)
- [# Implementation and Maintenance](#implementation-and-maintenance)
- [# Routines](#routines)
  - [Routine List](#routine-list)
  - [Callable Routines](#callable-routines)
- [# Files](#files)
  - [File List](#file-list)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
  - [Cross-References](#cross-references)
- [Exported Options](#exported-options)
  - [The following are the steps you may take to obtain information about menus and exported options concerning the Clinical Monitoring System package.](#the-following-are-the-steps-you-may-take-to-obtain-information-about-menus-and-exported-options-concerning-the-clinical-monitoring-system-package)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Options](#exported-options-1)
- [Archiving and Purging](#archiving-and-purging)
  - [At the present time, there is no provision for archiving records, as no determination has yet been made as to how long records should be retained. If the user wishes to delete records in the FALL OUT file (#743.1), the MONITOR HISTORY file (#743.2), or the AUTO ENROLL RUN DATE file (#743.6), there are options available to delete a range of records from these files. For more information see the Purge Menu options in the Clinical Monitoring System User Manual.](#at-the-present-time-there-is-no-provision-for-archiving-records-as-no-determination-has-yet-been-made-as-to-how-long-records-should-be-retained-if-the-user-wishes-to-delete-records-in-the-fall-out-file-7431-the-monitor-history-file-7432-or-the-auto-enroll-run-date-file-7436-there-are-options-available-to-delete-a-range-of-records-from-these-files-for-more-information-see-the-purge-menu-options-in-the-clinical-monitoring-system-user-manual)
- [Programmer Options and Entry Points](#programmer-options-and-entry-points)
  - [This section has been designed as an aid to the IRM programmer. It discusses the Monitoring System Programmer Menu options and how new modules may be added to the package.](#this-section-has-been-designed-as-an-aid-to-the-irm-programmer-it-discusses-the-monitoring-system-programmer-menu-options-and-how-new-modules-may-be-added-to-the-package)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
  - [Internal Relations](#internal-relations)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
  - [XINDEX](#xindex)
  - [Inquire to Options File](#inquire-to-options-file)
  - [Print Options File](#print-options-file)
  - [List File Attributes](#list-file-attributes)
- [Security](#security)
  - [Security Keys](#security-keys)
  - [FileMan Access Codes](#fileman-access-codes)
- [Glossary](#glossary)
The Clinical Monitoring System package is a fully integrated system which is compatible with Version 7.0 or later of Kernel and Version 19 or later of VA FileMan. The NEW PERSON file (#200) is required.
The heart of the Clinical Monitoring System package is in building monitors using conditions and groups for the auto enrollment of patients.
The main function of this software is to capture data for patients meeting specified conditions. All monitors within the framework of this software are ultimately based upon patient related data. In order to capture data, you create monitors that run nightly. These nightly runs "auto enroll" (or capture) the patients defined by the monitors.
This system looks at what happened yesterday in VistA. It can capture such items as ward, treating specialty, SSN, age, etc. For a more extensive list of items that may be captured, use the Data Element File Inquire option within the Outputs Menu of the Monitoring System Manager Menu. Data elements available for capture vary depending on the conditions you select when building monitors.
Conditions are provided with the Clinical Monitoring System package. Examples of conditions include ON WARD, READMISSION, MAS MOVEMENT TYPE, PREVIOUS DISCHARGE, etc. You may use the Condition File Inquire option to obtain information on selected/all conditions. The information provided will describe the condition; tell you what questions will be asked when using a condition; tell you when you must define a group for the condition, and list the other data that is available for capture.
Each condition chosen for a monitor brings up a set of questions pertaining to it. For example, if you choose the AGE condition, you will be asked age ranges. Some conditions require a group be defined such as a group of wards, drug classes, MAS movement types, etc. With each condition used, there is a list of other data that can be captured when a patient becomes a fall out that might include items such as ward, admission date, attending, etc.
Patients captured by the monitors are called "fall outs". The monitors can be queued to run nightly, or manually run, one or more at a time. Each monitor has an "ON/OFF" switch, an "UNDER CONSTRUCTION" or "FINISHED" status, and START and STOP dates so that running it can be tightly controlled.
Software Features
- Provides the user with the ability to design a monitor that will auto enroll cases that meet the user's defined criteria/conditions from VistA.
- Allows the user to set time frames for computing percentages and tracking findings between time frames.
- Has the ability to alert users when important thresholds or dates are met.
- Provides the site a mechanism to add site-developed conditions and data elements and routines such as site-designed worksheets. MUMPS programming is a required part of site-specific enhancement.
- Provides mechanisms for tightly controlling the disk space and CPU time resources used by the Clinical Monitoring System.
- Allows the user to manually enter cases.
Package-Wide Variables
No variables are used package wide.

# # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At implementation the Site Parameters Edit option in the Monitoring System Manager Menu is used to set up the following site-specific data. See the Site Parameters Edit option documentation in the Clinical Monitoring System User Manual for more specific information.

- The day the weekly time frame begins. This is the day of the week that should begin each weekly time frame. Generally, this would be Sunday.
- The use of the "contains" operator ( \[ ) in the group edit. Do you want to allow the users the ability to build groups using the contains operator?
- The fields that control the manual run of auto enroll. This includes answering how many days can be run at one time, how much time should separate each run, and what time during the day the manual run can be done.
- The device on which auto enroll reports will print.

It is also necessary to queue the daily auto enrollment runs using the Task Manager option, Schedule/Unschedule Options. The option QAM TASKED AUTO ENROLL RUN should be scheduled to run daily, after midnight, and at a time of low activity.

# # Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain a listing of the routines contained in the Clinical Monitoring System package.

1\. Programmer Options Menu

2\. Routine tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: QAM\*

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the present time no other packages have requested formal entry points into the Clinical Monitoring System package. No "protected" entry points are defined.

# # Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>FILE \#</u> <u>FILE NAME</u> <u>GLOBAL</u>

743 QA MONITOR ^QA(743,

743.1 FALL OUT ^QA(743.1,

743.2 MONITOR HISTORY ^QA(743.2,

743.3 CONDITION ^QA(743.3,

743.4 DATA ELEMENT ^QA(743.4,

743.5 GROUP ^QA(743.5,

743.6 AUTO ENROLL RUN DATE ^QA(743.6,

743.91 RATIONALE ^QA(743.91,

743.92 TIME FRAME ^QA(743.92,

The following are the steps you may take to obtain information concerning the files and templates contained in the Clinical Monitoring System package.

## File Flow (Relationships between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: Print Template

Sort Template

Input Template

List Template

4\. Sort by: Name

5\. Start with name: QAM to QAMZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

## Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QA MONITOR File (#743)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743,.01</td>
<td>CODE</td>
<td><p>B</p>
<p>BU</p></td>
<td><p>Required.</p>
<p>Upper case B xref.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.02</td>
<td>TITLE</td>
<td><p>C</p>
<p>CU</p></td>
<td><p>Title look-up.</p>
<p>Upper case C xref.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743,1</td>
<td>SERVICE</td>
<td>ASRV</td>
<td>Used by the Monitor Description Report.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.04,.01</td>
<td>RATIONALE</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.01,.01</td>
<td>CONDITION</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.01,1</td>
<td>CONTRIBUTES TO SAMPLE</td>
<td>AS</td>
<td>Used by the input transform and executable help on the SAMPLE RELATIONSHIP field.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.06,.01</td>
<td>OTHER DATA TO CAPTURE</td>
<td>B</td>
<td>Required.</td>
</tr>
</tbody>
</table>

Cross-ReferencesFALL OUT File (#743.1)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.1,.01</td>
<td>PATIENT</td>
<td><p>B</p>
<p>AA1</p>
<p>AB1</p></td>
<td><p>Required.</p>
<p>Used by several reports for sorting and auto enroll for duplicate checking.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.1,.02</td>
<td>MONITOR</td>
<td><p>AA2</p>
<p>AB2</p>
<p>C</p></td>
<td><p>Same as AA1.</p>
<p>Same as AB1.</p>
<p>Monitor look-up.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.1,.03</td>
<td>EVENT DATE</td>
<td><p>AA3</p>
<p>AB3</p></td>
<td><p>Same as AA1.</p>
<p>Same as AB1.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.11,.01</td>
<td>DATA ELEMENT</td>
<td><p>AA3</p>
<p>AB3</p>
<p>AD1</p></td>
<td><p>Same as AA1.</p>
<p>Same as AB1.</p>
<p>Used by Ad Hoc reports for sorting.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.11,.02</td>
<td>ACTUAL DATA</td>
<td><p>B</p>
<p>AD2</p></td>
<td><p>Required.</p>
<p>Same as AD1</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.1,.04</td>
<td>DATE RECORD CREATED</td>
<td>ADRC</td>
<td>Used by auto enroll to count manually entered fall outs.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.1,100</td>
<td>AUDIT</td>
<td>AUDIT</td>
<td>Audit file trigger.</td>
</tr>
</tbody>
</table>

MONITOR HISTORY File (#743.2)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.2,.01</td>
<td>MONITOR</td>
<td><p>B</p>
<p>AA1</p></td>
<td><p>Required.</p>
<p>Used to determine the correct entry when updating the Monitor History file.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.2,.02</td>
<td>START DATE</td>
<td>AA2</td>
<td>Same as AA1.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.2,.03</td>
<td>END DATE</td>
<td>AA3</td>
<td>Same as AA1.</td>
</tr>
</tbody>
</table>

Cross-ReferencesCONDITION File (#743.3)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.3,.01</td>
<td>NAME</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.34,.01</td>
<td>DATA ELEMENT</td>
<td><p>B</p>
<p>AELEM</p></td>
<td><p>Required.</p>
<p>Used by the screen on the OTHER DATA TO CAPTURE multiple.</p></td>
</tr>
</tbody>
</table>

DATA ELEMENT File (#743.4)

| File, Field \# | Field Name        | X-Ref | Description |
|----------------|-------------------|-------|-------------|
|                |                   |       |             |
| 743.4,.01      | NAME              | B     | Required.   |
|                |                   |       |             |
| 743.42,.01     | DICTIONARY NUMBER | B     | Required.   |

GROUP File (#743.5)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.5,.01</td>
<td>NAME</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.5,.02</td>
<td>PARENT FILE</td>
<td>C</td>
<td>Parent File look-up.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.51,.01</td>
<td>GROUP MEMBER</td>
<td><p>B</p>
<p>AB</p></td>
<td><p>Required.</p>
<p>Group Member internal entry number cross reference.</p></td>
</tr>
</tbody>
</table>

AUTO ENROLL RUN DATE File (#743.6)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.6,.01</td>
<td>RUN DATE</td>
<td>B</td>
<td>Required.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.61,.01</td>
<td>MONITOR</td>
<td><p>B</p>
<p>AM</p></td>
<td><p>Required.</p>
<p>Used by the Auto Enroll Run Dates File Purge option.</p></td>
</tr>
</tbody>
</table>

Cross-ReferencesRATIONALE File (#743.91)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.91,.01</td>
<td>NAME</td>
<td><p>B</p>
<p>BU</p></td>
<td><p>Required.</p>
<p>Upper case B xref.</p></td>
</tr>
</tbody>
</table>

TIME FRAME File (#743.92)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>File, Field #</th>
<th>Field Name</th>
<th>X-Ref</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743.92,.01</td>
<td>NAME</td>
<td><p>B</p>
<p>BU</p></td>
<td><p>Required.</p>
<p>Upper case B xref.</p></td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The following are the steps you may take to obtain information about menus and exported options concerning the Clinical Monitoring System package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Programmers Options

2\. Menu Management Menu

3\. Display Menus and Options Menu

4\. Diagram Menus

5\. Select User or Option Name: QAM Main Menu

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: OPTION

4\. Sort by: Name

5\. Start with name: QAM to QAMZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## At the present time, there is no provision for archiving records, as no determination has yet been made as to how long records should be retained. If the user wishes to delete records in the FALL OUT file (#743.1), the MONITOR HISTORY file (#743.2), or the AUTO ENROLL RUN DATE file (#743.6), there are options available to delete a range of records from these files. For more information see the Purge Menu options in the Clinical Monitoring System User Manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although VA FileMan can be used to delete records in any of the Clinical Monitoring System files, they are set up with "@" access at the delete level to prevent users from doing this. It is strongly urged that the IRM staff not delete records because it may have an adverse effect on the auto enroll portion of the Clinical Monitoring System.

# Programmer Options and Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This section has been designed as an aid to the IRM programmer. It discusses the Monitoring System Programmer Menu options and how new modules may be added to the package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Application Group Edit

This option pertains to the Group Edit option. The user can only create groups from files that are in the QAM application group. The Clinical Monitoring System comes with a set of default files to be added to the QAM application group. See the Section on External Relations for a list of these default files. This option allows the programmer to add new (and remove old) files from the QAM application group at any time.

- Creating a New Condition

Conditions are MUMPS routines that produce lists of patients who meet some user-defined criteria. If you wish to add new conditions to the Clinical Monitoring System, you will have to write your own custom MUMPS routine. After the condition code is finished, the new condition must be added to the Condition file (#743.3). See the next section for more information on the Condition file. The MUMPS routine that makes up the condition generally has two entry points. One entry point scans V*IST*A and produces the list of patients. This is the CONDITION entry point. The second entry point optionally asks the user questions that will narrow down the scope of the condition. This is the PARAMETER entry point.

*The Parameter Entry Point*

This section of the condition's code asks the user questions that will narrow down the scope of the condition (e.g., upper/lower age limits on the age condition). Some conditions may not need parameters, such as the death condition. The first step is to determine the number and data types of the parameters. The first variable that should be set is shown below.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>QAMPARAM</th>
<th><p>This variable contains the intended storage location of the parameter. There are five locations available for storage of parameters in the QA Monitor file (#743): P1, P2, P3, P4, P5 (Fields: 743.01,10 -&gt; 50 PARAMETER 1 -&gt; 5). These locations are each a maximum of 245 characters in length and are each stored on their own nodes. For example, to set up the first parameter you would:</p>
<p>SET QAMPARAM="P1"</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Editing of the parameters should support full VA FileMan editing conventions, (i.e., defaults, add, edit, delete, and error handling). There are two entry points provided to perform the edit of the parameters.

| DO EN2^QAMUTL     | This entry point should be used if the parameter is a pointer to an entry in a file and the look-up requires a screen (DIC("S")). This call does a DO ^DIC look-up and uses all the variables a standard DIC look-up would use. To provide help the DIR("?"), DIR("??"), and DIR("?",1-n) variables may also be set. If these variables are used, they should be set in the same way they would be used in a DIR call. |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DO EN3^QAMUTL | This entry point should be used if the parameter does not require a screened look-up on a file. This call does a DO ^DIR call and uses all the variables a standard DIR call would use.                                                                                                                                                                                                                                |

For more information on the variables used by the DO ^DIC and DO ^DIR calls see the <u>VA FileMan Programmer's Manual</u>.

The variables returned from these calls are as follows.

| DIRUT | DIRUT will be defined if the user up-arrowed or timed out. If DIRUT is defined (\$D(DIRUT)) the variable Y should be set to minus one and you should exit the program. |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       |                                                                                                                                                                        |
| Y | Y is the result of a call to one of these entry points. If Y is null or minus one the call failed (i.e., up arrow out, time out).                                      |

Other variables may also be returned from these calls depending upon the variables that are passed to them. For example, if DIC(0)\["Z" the variables Y(0) and Y(0,0) will be returned.

If there is no \$DATA(DIRUT) and Y follows null and is not minus one you should set the parameter into its storage location (Fields: 743.01,10 -\> 50 PARAMETER 1 -\> 5). An example is shown below.

SET ^QA(743,QAMD0,"COND",QAMD1,QAMPARAM)=parameter data

The parameter data may be from 1-245 characters in length. There is no set format for the parameter data. Its format is determined by how you write your condition and what kind of data you are saving.

To track down the meaning/format of preexisting parameter nodes in the QA Monitor file (#743) you should first determine which condition the parameter belongs to. Once the condition is known, you should do an inquire on the Condition file (#743.3) and look for the PARAMETER CODE field (#2). This field will tell you the MUMPS routine entry point of the parameter edit code. By reading the code in this entry point the meaning/format of a parameter can be determined.

The variables QAMD0 and QAMD1 will always be defined as the pointers to the correct storage location. (These variables should NOT be changed.) The "parameter data" may be stored in any format which is most convenient. One of the most commonly used forms is: Pointer to Data ^ External Format of Data.

If all the parameters were answered by the user, the variable Y should be killed when exiting the parameter code. If the user up arrowed out of the parameter edit, the variable Y should be set to minus one (-1) when exiting the parameter code.

A simple block diagram of the parameter code is shown below.

P1 ;

SET QAMPARAM="P1" ; First parameter.

SET appropriate DIC/DIR variables ; Set needed variables.

DO EN2 or EN3 ^QAMUTL ; Call the appropriate

; editing routine.

IF \$DATA(DIRUT) SET Y=-1 QUIT ; Check the error flag.

IF Parameter_data\]"" SET ^QA(743,QAMD0,"COND",

QAMD1,QAMPARAM)=Parameter_data

P2 ;

SET QAMPARAM="P2" ; Second parameter.

SET appropriate DIC/DIR variables ; Set needed variables.

DO EN2 or EN3 ^QAMUTL ; Call the appropriate

; editing routine.

IF \$DATA(DIRUT) SET Y=-1 QUIT ; Check the error flag.

IF Parameter_data\]"" SET ^QA(743,QAMD0,"COND",

QAMD1,QAMPARAM)=Parameter_data

P3 ;

.

.

.

EXIT ;

KILL Y

QUIT

*The Condition Entry Point*

This part of the condition routine produces the list of patients who meet the criteria of the condition and the user entered parameters. There is no set format for this entry point since the data it will be scanning to produce the list will be different in every case. There is a set format for the list of patients that is produced.

This node should be defined for every patient who falls out for this condition.

SET ^UTILITY(\$J,"QAM CONDITION",QAMD1,Dfn,Date/Time)=D0^D1^D2^...

This node should be defined only if the patient who fell out for this condition contributes to the over all sample size.

SET ^UTILITY(\$J,"QAM CONDITION",QAMD1,Dfn)=""

Explanation of the variables.

| Input Variables  |                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  |                                                                                                                                                                                                         |
| QAMDO        | The internal entry number of a record in the QA Monitor file (#743). This variable should NOT be changed.                                                                                               |
|                  |                                                                                                                                                                                                         |
| QAMD1        | The internal entry number of a record in the Condition multiple in the QA Monitor file (#743). This variable should NOT be changed.                                                                     |
|                  |                                                                                                                                                                                                         |
| QAMTODAY     | The date which auto enroll is scanning. This date is in VA FileMan format. This variable should NOT be changed.                                                                                         |
|                  |                                                                                                                                                                                                         |
| QAMZERO      | The zero node of a monitor in the QA Monitor file (#743), (i.e., ^QA(743,QAMD0,0)). This variable should NOT be changed.                                                                                |
|                  |                                                                                                                                                                                                         |
| QAMONE       | The one node of a monitor in the QA Monitor file (#743), (i.e., ^QA(743,QAMD0,1)). This variable should NOT be changed.                                                                                 |
|                  |                                                                                                                                                                                                         |
| Condition Output | \[In ^UTILITY(\$J,"QAM CONDITION",...\]                                                                                                                                                                 |
|                  |                                                                                                                                                                                                         |
| Dfn          | This is a variable that is a pointer to a record in the Patient file (#2).                                                                                                                              |
|                  |                                                                                                                                                                                                         |
| Date/Time    | This is a variable that is a VA FileMan date/time. This date/time will be used as the date of the event, for example, admission date, date of death, date of lab test, etc.                             |
|                  |                                                                                                                                                                                                         |
| D0^D1^D2^... | These represent pointers to the data that was found to meet the criteria of the condition. If the condition was SEX, this string would simply be a top level pointer to the Patient file (#2) ("Dfn^"). |

For examples of conditions, see the source code of the QAMC\* routines online.

Once a new condition has been created, it must be added to the condition file (#743.3) in order to be selectable by the user.

- Condition File Edit

Allows the programmer to add new conditions to the Condition file (#743.3).

Select CONDITION: NEW CONDITION

ARE YOU ADDING 'NEW CONDITION' AS A NEW CONDITION (THE 24TH)? YES (YES)

NAME: NEW CONDITION// \<RET\>

AUTO ENROLL CONDITION: YES

Answer YES if this condition can be used to auto enroll patients into the fall out file (#743.1).

DESCRIPTION:

1\>This is a description of what the condition does and what

2\>parameters the user will be prompted for.

3\>

EDIT Option:

Select DATA ELEMENT: Data Element

The data elements selectable by the user are dependent on the entries in this multiple. Only data elements that are pointed to by the D0^D1^D2^...string should be entered in this multiple. (The D0^D1^D2^... string is returned by the condition. See the previous chapter for an explanation of this string.)

CONDITION CODE: D TAG1^ROUTINE

This is the entry point that produces a list of patients who meet the condition and its parameters.

PARAMETER CODE: D TAG2^ROUTINE

This is the entry point that asks the user any parameters associated with the condition, (e.g., upper/lower limits for age). This field may not be needed for some conditions, (e.g., death).

- Data Element File Edit

Allows the programmer to add new data elements to the Data Element file (#743.4) for capture. Note that data elements can be added to a monitor at any time, but the program will not retroactively capture this data.

Select DATA ELEMENT: NO-SHOW/CANCEL DATE/TIME

The data element name need not match the field name.

NAME: AGE// \<RET\>

ARE YOU ADDING 'AGE 2' AS A NEW DATA ELEMENT (THE 65TH)? Y (YES)

DATA ELEMENT PARENT FILE: 2 PATIENT

NAME: NO-SHOW/CANCEL DATE/TIME// \<RET\>

PARENT FILE: PATIENT// (No Editing)

(SUB) DICT. \#: 2.9 PATIENT FILE

(SUB) FIELD \#: 15 NO-SHOW/CANCEL DATE/TIME

These two prompts ask where the field is in the data dictionary. When the field and (sub) dictionary numbers are entered, the option will compute the path to the field.

Building path to data element.

=============================================================================

ELEMENT: NO-SHOW/CANCEL DATE/TIME FILE: PATIENT

DD LEVEL FIELD \# DD NUMBER

1 1900 2

2 15 2.98

=============================================================================

The following DIR() fields are used when the user is manually entering fall out data. The format of the data in these fields is the same as that for any DO ^DIR call. See the <u>VA FileMan Programmers Manual</u> for more information on these variables.

DIR(0): DO^::ETXR \<RET\>

DIR(A): \<RET\>

DIR(A,#): \<RET\>

1\> \<RET\>

DIR(B): \<RET\>

DIR(T): \<RET\>

DIR(?): Enter the date/time the appointment wasmarked as a no-show or was cancelled.

DIR(?,#): \<RET\>

1\> \<RET\>

DIR(??): \<RET\>

DIR OUTPUT TRANSFORM: X ^DD("DD")

This MUMPS field takes the output of the DO ^DIR call and sets the variable Y equal to the external form of the data.

CODE TO CREATE DATA POINTERS: S QAMDTPT(1)=QAMDFN,QAMDTPT(2)=+\$O(^DPT(QAMDFN,"S",QAMEVENT-.0000001))

This field takes the variables QAMDFN (Patient file pointer) and QAMEVENT (event date/time) and, through MUMPS code, produces a set of pointers (QAMDTPT(1-n)) to the record that contains the desired data. These pointers are used to compute a default value for the data element being edited.

Select DATA ELEMENT: \<RET\>

- Monitor File Edit

This is the only place where the status of a monitor can be changed from "Finished" back to "Under Construction" so the user can do further editing to the monitor. It also allows editing of certain programmer specific fields in the QA Monitor file (#743). It is used when adding routines such as worksheets to a specific monitor.

Select MONITOR: PSY-1

LOS ON SUBSTANCE ABUSE FINISHED

Checking monitor...

> **WARNING:** SAMPLE RELATIONSHIP not specified

> **WARNING:** TIME FRAME not specified

> **WARNING:** THRESHOLD not specified

\*ERROR\*: START DATE not specified

All errors must be corrected in order for this monitor to run !!

The monitor is first checked for correctness. All errors must be fixed in order for the monitor to run. Warnings alert you to potential problems.

MONITOR STATUS: FINISHED//

The MONITOR STATUS may be changed to UNDER CONSTRUCTION at this prompt. Monitors that are UNDER CONSTRUCTION allow for the editing of the conditions, relationships, and various other monitor control fields. This prompt will not appear if errors were found in the monitor.

CODE: PSY-1//

TITLE: LOS ON SUBSTANCE ABUSE Replace

SERVICE: PSYCHIATRY//

STANDARD OF CARE:

1\>This is the std. of care for this monitor. It is not a required

2\>field, so it can be bypassed.

EDIT Option:

CLINICAL INDICATOR:

1\>Enter the clinical indicator of care here. this also is not

2\>a required field, so it can be bypassed.

EDIT Option:

Select RATIONALE: Other//

RATIONALE: Other//

EXPLAIN RATIONALE:

1\>this monitor is looking at the adequacy of discharge planning

2\>for those patients whose stays exceed the designated 28 days.

EDIT Option:

Select RATIONALE:

Select OTHER DATA TO CAPTURE: WARD LOCATION//

PRINT DAILY FALL OUT LIST: YES//

PRINT DAILY WORKSHEETS: NO//

BULLETIN WHEN THRESHOLD MET: YES//

BULLETIN AT END OF TIME FRAME: YES//

BULLETIN WHEN ALERT LEVEL MET: YES//

BULLETIN MAIL GROUP: QA DAD//

WORKSHEET ROUTINE: DO TAG^ROUTINE

SPECIAL FUNCTIONS ROUTINE: DO TAG^ROUTINE

START DATE: JUL 17,1991

END DATE:

ON/OFF SWITCH: ON

Checking monitor...

> **WARNING:** SAMPLE RELATIONSHIP not specified

> **WARNING:** TIME FRAME not specified

> **WARNING:** THRESHOLD not specified

No errors found.

The monitor is again checked for correctness. If any errors are found, the monitor status prompt will not appear

MONITOR STATUS: FINISHED//

Select MONITOR:

The WORKSHEET and SPECIAL FUNCTIONS routines are programmer written MUMPS routines that can produce fall out worksheets and perform other functions. These two routines are executed after the data is stored in the Fall Out file (#743.1), after the MONITOR history file (#743.2) has been updated, and after any bulletins have been sent. The worksheet routine will execute first then the special functions routine will execute. These routines should pull all the data they require from the Fall Out file and the Monitor History file.

- Creating a New Time Frame

A time frame is the period over which the Clinical Monitoring System aggregates data in the Monitor History file (#743.2). Several time frames are exported with the package: Daily, Weekly, Monthly, Quarterly, Semi-Annually, Annually, Fiscal Yearly, and Fiscal Semi-Annually.

To create a new time frame, the programmer must write a MUMPS routine that accepts the following input variable.

| QAMTODAY | The date that auto enroll is scanning in V*IST*A for fall outs. This date is in VA FileMan format. This variable should NOT be changed. |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------|

The time frame routine should return the following output variables.

| QAMSTART   | The starting date of the time frame in VA FileMan format. If the time frame was MONTHLY and QAMTODAY is equal to 2930418 (April 18, 1993), the time frame routine should return QAMSTART equal to 2930401 (April 1, 1993). |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            |                                                                                                                                                                                                                            |
| QAMEND | The ending date of the time frame in VA FileMan format. If the time frame was MONTHLY and QAMTODAY is equal to 2930418 (April 18, 1993), the time frame routine should return QAMEND equal to 2930430 (April 30, 1993).    |

For examples of time frames, see the EN1-8 entry points in the QAMTIME0 routine. An example of the Quarterly time frame code from QAMTIME0 is shown below.

EN4 ; \*\*\* QUARTERLY

S QAM=\$E(QAMTODAY,4,5),QA=\$E(QAMTODAY,1,3)

I QAM'\>3 S QAMSTART=QA\_"0101",QAMEND=QA\_"0331" Q

I QAM'\>6 S QAMSTART=QA\_"0401",QAMEND=QA\_"0630" Q

I QAM'\>9 S QAMSTART=QA\_"0701",QAMEND=QA\_"0930" Q

S QAMSTART=QA\_"1001",QAMEND=QA\_"1231"

Q

Once a new time frame has been created, it must be added to the Time Frame file (#743.92) in order to be selected by the user.

- Time Frame Edit

Allows the programmer to add new or change old time frames.

Select TIME FRAME: Fortnightly

ARE YOU ADDING 'Fortnightly' AS A NEW TIME FRAME (THE 9TH)? YES (YES)

NAME: Fortnightly// \<RET\>

START/END DATE CODE: D TAG^ROUTINE

This is the entry point to the time frame routine created by the programmer.

Select TIME FRAME: \<RET\>

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The package points to the following VistA files.

<u>FILE</u> <u>USAGE</u>

| 2     | PATIENT                           | Used by the FALL OUT file (#743.1).                                                                                                                                   |
|-------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       |                                   |                                                                                                                                                                       |
| 3.8   | MAIL GROUP                        | Used by the QA MONITOR file (#743) to determine where the automatic bulletins should be sent.                                                                         |
|       |                                   |                                                                                                                                                                       |
| 49    | SERVICE / SECTION                 | Used by the QA MONITOR file (#743) to determine who the monitor belongs to.                                                                                           |
|       |                                   |                                                                                                                                                                       |
| 740   | QUALITY ASSURANCE SITE PARAMETERS | Used to store the Clinical Monitoring System site parameters.                                                                                                         |
|       |                                   |                                                                                                                                                                       |
| 740.5 | QA AUDIT                          | Used to store the name of user, date of action and type of action for each and every entry made by the user or auto enroll. Pointed to by the FALL OUT file (#743.1). |

The following files are used by the various conditions.

2 PATIENT

37 DISPOSITION

42 WARD LOCATION

44 HOSPITAL LOCATION

45 PTF

45.7 FACILITY TREATING SPECIALTY

49 SERVICE / SECTION

50 DRUG

50.605 VA DRUG CLASS

52 PRESCRIPTION

55 PHARMACY PATIENT

80 ICD DIAGNOSIS

80.1 ICD OPERATION/PROCEDURE

405 PATIENT MOVEMENT

405.2 MAS MOVEMENT TYPE

405.3 MAS MOVEMENT TRANSACTION TYPE

409.1 APPOINTMENT TYPE

615.2 SECLUSION / RESTRAINT

615.5 S/R REASONS

615.6 S/R CATEGORY

*DBIA Agreements*

The following are the steps you may take to obtain database integration agreements for the Clinical Monitoring System package.

DBIA AGREEMENTS - CUSTODIAL PACKAGE

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Custodial Package Menu

5\. Active by Custodial Package Option

6\. Select Package Name: CLINICAL MONITORING SYSTEM

DBIA AGREEMENTS - SUBSCRIBER PACKAGE

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Subscriber Package Menu

5\. Print Active by Subscriber Package Option

6\. Start with subscriber package: QAM to QAMZ

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The package is designed to allow for tailoring of menus for particular users. This is to be determined by the QM ADPAC at each site, based on how the components of the QM task are assigned. The Monitoring System Manager Menu options are intended for use by the QM ADPAC. The QA Programmer Menu is intended for the IRM support person. All other menus and their options may stand alone.

Field \#51 in the QA Monitor file (#743) serves a dual purpose. If the THRESHOLD (field \#52) is entered as a percentage the prompt for Field \#51 will be MINIMUM SAMPLE, the field name. If the threshold is entered as a pure numeric the prompt for Field \#51 will be PRE-THRESHOLD ALERT LEVEL, the field title. For percent thresholds, Field \#51 defines the minimum sample size (denominator) that must be reached before threshold checking occurs. For numeric thresholds Field \#51 may be used with the BULLETIN WHEN MIN SAMPLE/ALERT LEVEL MET field (#61) (set to YES) as a pre-threshold notification.

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure Clinical Monitoring (CM) technical documentation. On-line technical documentation pertaining to the CM software, in addition to that which is located in the help prompts and on the help screens which are found throughout the CM package, may be generated through utilization of several KERNEL options. These include but are not limited to: XINDEX, Menu Management Inquire Option File, Print Option File, and FileMan List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the VistA Kernel Reference Manual.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the CM package, specify the following namespace at the "routine(s) ?\>" prompt: QAM\*.

CM initialization routines which reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the CM namespace should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

## Inquire to Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu Manager option provides the following information about a specified option(s): option name, menu text, option description, type of option, and lock (if any). In addition, all items on the menu are listed for each menu option.

To secure information about CM options, the user must specify the name or namespace of the option(s) desired. QAM is the namespace associated with the CM package.

## Print Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of CM options, the following option namespace should be specified: QAM.

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Monitoring System does not use any special locks or keys.

## FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of recommended VA FileMan access codes associated with each file contained in the CM package. This list may be used to assist in assigning users appropriate VA FileMan access codes.

File File DD RD WR DEL LAYGO AUDIT

<u>Number</u> <u>Name</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>access</u>

740 QUALITY ASSURANCE

SITE PARAMETERS @

740.1 AD HOC MACRO @ @ @

740.5 QA AUDIT @ @ @ @ @ @

743 QA MONITOR @ @

743.1 FALL OUT @ @

743.2 MONITOR HISTORY @ @

743.3 CONDITION @ @

743.4 DATA ELEMENT @ @

743.5 GROUP @ @

743.6 AUTO ENROLL RUN DATE @ @

743.91 RATIONALE @ @

743.92 TIME FRAME @ @

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Alert Level</th>
<th>The level at which a bulletin is sent announcing that this level (pre-threshold) has been met. This is only meaningful for non-percentile thresholds. See Bulletin when Min Sample/Alert Level Met.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Allow Duplicate Fall Outs</td>
<td>Answering YES to this question allows an event to fall out multiple times for the same patient within a given time frame. Answering NO will allow the event to fall out only once per patient per time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Auto Enroll Monitor</td>
<td>This field determines whether or not this is an auto enroll monitor. You should answer YES to this field only if this monitor can be auto enrolled. Your answer will determine which conditions you will be allowed to select.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Auto Run Auto Enroll</td>
<td>This refers to the nightly automatic runs that scan VistA for patients who meet the criteria of the monitors which are set up in the QA MONITOR file (#743).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin at End of Time Frame</td>
<td>Enter YES if a bulletin should be sent at the end of each time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin Mail Group</td>
<td>This field contains the name of the mail group that the threshold, minimum sample, and end of time frame bulletins will be sent to.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin when Min Sample/Alert Level Met</td>
<td>Enter YES if a bulletin should be sent when the minimum sample is met or when the alert level is met for non-percentile thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bulletin when Threshold Met</td>
<td>Enter YES if a bulletin should be sent when the threshold is met the first time within the time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Clinical Indicator</td>
<td>This word processing field defines the criteria necessary to meet the standard of care.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Code</td>
<td>This can either be free text or a predetermined list (of initial identifying letters or numbers) as defined by the site so that monitors can be grouped and easily retrieved by the service, section, etc.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Condition</td>
<td>A condition applies a True/False test on selected data elements in a patient's record. If the result of the test is true, that patient's record is captured for further processing.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Condition for Date of Event</td>
<td>Enter the condition number that should be used to capture the event date.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contributes to Sample</td>
<td>This field determines whether or not this condition contributes to the sample size (denominator). This affects how information is collected to determine the size of the sample (denominator).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>End Date</td>
<td>This field determines when the monitor should stop capturing data or when manual entry of data for this monitor is no longer allowed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Fall Out</td>
<td>A fall out is a patient who has been found to meet the criteria of a monitor. When a patient falls out a record is created in the FALL OUT file (#743.1) for that patient.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Fall Out Relationship</td>
<td>This field specifically states the relationship between the conditions entered by the user. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Group</td>
<td>A group is a list of similar items. An example would be a group of wards that are all psychiatry wards. Groups may have as many or as few group members as desired.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Hi/Lo Percent</td>
<td>If the user chooses "Hi", the threshold will be met when the percentage is calculated to be &gt;= to the threshold. If the user chooses "Lo", the threshold will be met when the percentage is calculated to be &lt;= the threshold. Hi/Lo is only meaningful for percent thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Manually Run Auto Enroll</td>
<td>Used to manually queue the auto enroll batch job. This option is used to run the auto enroll if one or more days in the past was missed due to down time.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Minimum Sample</td>
<td>This field defines the minimum sample size (denominator) that must be reached before threshold checking occurs. Minimum sample is meaningful only for percent thresholds.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Monitor</td>
<td>A monitor is made up of a set of conditions (criteria) and the relationships among those conditions. Monitors scan VistA on a nightly basis for patients who meet the monitor’s criteria.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Monitor Status</td>
<td><p>Answer FINISHED to this field only when you are sure you are completely finished entering/editing/</p>
<p>building this monitor. Once you answer FINISHED, you will no longer be able to edit selected monitor fields.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>On/Off Switch</td>
<td>This field controls whether or not a monitor is active. For an auto enroll monitor to capture data, this switch must be turned on. For a manual entry monitor to be selectable, the switch must be turned on. When you wish to stop using a monitor, this switch should be turned off.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Data to Capture</td>
<td>When a patient meets the conditions of the monitor and falls out, the other data to capture entries define which data elements in the patient's record should be collected.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td>Parameters further narrow down the definition of a condition. The format of a parameter is determined by the condition.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Print Daily Fall Out List</td>
<td>This field determines whether or not a generic list of all fall outs, sorted by monitor, is printed daily.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Print Daily Worksheets</td>
<td>This field determines whether worksheets are printed daily for all fall outs for this monitor. For this to work, the worksheet must first be created by a programmer and linked to the monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>QM</td>
<td>Quality Management</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>QM Coordinator</td>
<td>An individual tasked with the oversight of QM activities in the medical center.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Rationale</td>
<td>This field defines the rationale for the use of this monitor. You may select all that apply. (high volume, high risk, problem prone, other)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sample Relationship</td>
<td>Enter the relationships among the conditions. This field specifically states the relationship between the conditions that contribute to the sample size. The user may use &amp; (and), ! (or), ' (not), and parentheses () to specify the relationship.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sample Size</td>
<td>The total number of patient records scanned by a monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Service</td>
<td>This field will allow the manager to track what monitors are currently being used by each service. The service entered has nothing to do with the conditions chosen or what data is auto enrolled.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Standard of Care</td>
<td>This word processing field defines the standard of care to be monitored.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Start Date</td>
<td>This field determines when the monitor should start to capture data or when manual entry of data for this monitor may begin.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Threshold</td>
<td>Threshold defines the number or percentage of fall outs after which some specific action will occur.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Time Frame</td>
<td>Time frame is the period of time over which the program begins capturing data and then sums up the data to start all over again with the beginning of the next similar time frame.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Title</td>
<td>This is a short free text name determined by the user for this monitor.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>
