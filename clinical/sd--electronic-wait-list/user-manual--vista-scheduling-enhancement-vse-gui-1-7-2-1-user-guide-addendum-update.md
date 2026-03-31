---
title: VistA Scheduling Enhancement (VSE) GUI 1.7.2.1.User Guide Addendum Update
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: .1. Addendum Update
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 1.7.2
patch_id: SD*1.7.2
group_key: "SD:SD:1.7.2"
file_numbers: []
security_keys: []
menu_options: 0
description: The Veterans Health Administration (VHA) Office of Veterans Access to Care (OVAC) requested an enterprise enhancement for the VS package that supports COVID-19 response. The enhancement reduces operating costs for VHA and improves operational efficiencies, resulting in patient-centered access to car
audience: 
keywords: 
  - span
  - scheduling
  - table
  - vista
  - class
  - update
  - guide
  - addendum
  - contents
  - enhancement
page_count: 0
word_count: 1707
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_1_7_2_1_user_guide_addendum_vdl.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_1_7_2_1_user_guide_addendum_vdl.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/001.png)

# VS GUI User Guide Addendum


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VS GUI User Guide Addendum](#vs-gui-user-guide-addendum)
  - [Revision History](#revision-history)
  - [List of Figures](#list-of-figures)
  - [### Introduction](#introduction)
    - [System Summary](#system-summary)
    - [Key Feature Updates in Version 1.7.2.1](#key-feature-updates-in-version-1721)
Release 1.7.2.1 Update

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Enter alt text for table. </caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/16/2020</td>
<td>1.3</td>
<td>Updated the document to reflect the new version of VS GUI 1.7.2.1.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/23/2020</td>
<td>1.2</td>
<td>All changes are accepted and Updated Section 3.2, table of contents and figures.</td>
<td><p>HSP</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/15/2020</td>
<td>1.1</td>
<td>Updated Section 3.1.3 and 3.2, Fixed bullets, Updated table of contents and figures.</td>
<td><p>HSP</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/06/2020</td>
<td>1.0</td>
<td>Created 1.7.2 Release Update Feature Documentation</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Enter alt text for table.
## List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Scheduling Graphical User Interface (VS GUI) module is the Windows GUI version of the Patient Information Management System (PIMS) Scheduling module. It provides appointment management functions included in PIMS Scheduling, but with the added convenience and usability of a GUI.

#### Purpose

The Veterans Health Administration (VHA) Office of Veterans Access to Care (OVAC) requested an enterprise enhancement for the VS package that supports COVID-19 response. The enhancement reduces operating costs for VHA and improves operational efficiencies, resulting in patient-centered access to care, coordinated care, increased customer satisfaction, and the reduction of excessive cycle/wait time for scheduling patients.

#### Overview

VS GUI is a software module that allows schedulers to make appointments quickly by viewing multiple appointment request types and multiple clinics in one screen. A scheduler can easily view patient requests for service, find the next available open appointment, view the provider’s availability in multiple clinics, and track a patient’s appointment process. Refer to <u>System Summary</u> for a more detailed description of VS GUI functionality.

#### Disclaimers

#### Software Disclaimers

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimers

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSE project delivers a series of enhancements to legacy VistA Scheduling Version 5.3 via the VS GUI application.

This update is for the nationally released version 1.7.2.1, which includes VS GUI 1.7.2.1 R1 and VistA patch SD\*5.3\*756. At time of publishing, install period is projected for December 2020. This update includes the following:

- Request Management (RM) Grid improvements:
  - New COVID-19 Priority column on the RM Grid, allowing users to sort and filter by the COVID-19 priority noted with Consult Toolbox.
  - *Transfer to EWL* menu option removed, as per VA mandate, so that VS GUI is not adding any requests to the Electronic Wait List (EWL).
  - Removed *EWL, VETERAN and RTC* from the request type filter in the query tool.
- A new browser window is auto launched when a video appointment is scheduled.
- New national hashtag options can be added when cancelling an appointment
  - National hashtags are static, creating consistent cancellation reasons across the Enterprise
  - Updates to national hashtags will be provided via VistA patches (updates)
- New local hashtag options for appointment cancellations can be customized through a VistA option (no patch required)
- Addition of warning message if user exceeds character limit in cancellation remarks.

### Key Feature Updates in Version 1.7.2.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### RM Grid improvements

#### New COVID-19 Priority Column

RM grid now includes a COVID-19 Priority column, which displays the priority as designated for the consult in CPRS. The scheduler will be able to view/sort with this option from the RM Grid.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/002.png)

<span id="_Toc57975542" class="anchor"></span>Figure 1: There is Now a COVID Priority Column.

#### Transfer to EWL Menu Option Removed

As per VA mandate VS GUI users will no longer have the option to Transfer to EWL, as the EWL is being discontinued. However, users will still be able to see EWL requests on the RM grid for as long as they exist.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/003.png)

<span id="_Toc57975543" class="anchor"></span>Figure 2: Transfer to EWL Menu option No Longer Available from the RM Grid

#### Removed EWL, VETERAN and RTC Filter

EWL, VETERAN and RTC filter options are removed and will no longer be available on the request type query filter. Appointment request type is for APPT and RTC request. Consult request type is for Consult and Procedure requests. PtCSch request type is for Recall requests.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/004.png)

<span id="_Toc57975544" class="anchor"></span>Figure 3: Currently Available Request Type Filters in the Query Tool.

#### Introduction of Cancellation Remarks 

This release includes standard cancellation remarks routinely used and determined at National and Local levels. Local remarks can be customized by scheduling supervisors and changed as needed.

> **NOTE:** Users must request LAYGO access to Fileman File \#409.88 SDEC CANCELLATION COMMENT to be able to add, edit or remove local cancellation reasons.

#### New National Hashtag Options

The national comment field is a dropdown picklist that allows the user to choose one item from the list of national comments. The tool tip will display when you hover over hashtag.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/005.png)

<span id="_Toc57975545" class="anchor"></span>Figure 4: Cancel Appointment Dialog Box, Dropdown Option to Select National Comment

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/006.png)

<span id="_Toc57975546" class="anchor"></span>Figure 5: Tool Tip for \#TELE# Displayed When You Hover Over It.

#### New Local Hashtag Options

The local comment field is a checkbox list control that allows the user to select multiple local comments. The scheduler can now choose a National Comment and then choose a Local Comment. If needed, they will also be able to type “free text” in the Remarks section.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/007.png)

<span id="_Toc57975547" class="anchor"></span>Figure 6: Cancel Appointment Dialog Box Showing the “COVID19” National Template was Selected, the “NEW COMMENT” Local Comment Checkbox was Selected, and the User Typed “Free Text Remarks” in the Remarks Box.

When schedulers look at the expanded entry, they will see the full cancel remark that is created by the drop-down selections and any additional free text added at the end of the remark. The selections and the remark will populate as one sentence in the “Cancel Remarks” section.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/008.png)

<span id="_Toc57975548" class="anchor"></span>Figure 7: Expanded Entry Dialog Box showing the cancel remark section that contains the choices made.

#### Cancelation Remark Warning Message 

When a user, typing a free text remark under the Remarks section of the cancel appointment dialog box, exceeds the character limit a warning message pop-up. As shown below on the Cancel Appointment Warning pop-up message, if the user clicks OK, the characters after 166 will be truncated. If the user clicks the Cancel button, they can edit the remarks.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/009.png)

<span id="_Toc57975549" class="anchor"></span>Figure 8: Warning Message Showing Due to the user Typing in Excess of the Character Limit.

#### Adding New Local Cancellation Hashtag

1.  From Supervisor Menu \[SDSUP\], select Create/Edit Local Cancellation Comments option.
2.  Select SDEC CANCELLATION COMMENT HASH TAG: ex. BAD WEATHER
3.  Enter Y when asked if this is a new SDEC CANCELLATION COMMENT
4.  Hash tag name will be displayed, hit enter
5.  Under “COMMENT TEXT” add desired Comment text.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/010.png)

<span id="_Toc57975550" class="anchor"></span>Figure 9: Add Local Cancellation Hashtag

#### Edit Local Cancellation Hashtag 

1.  From Supervisor Menu \[SDSUP\], select Create/Edit Local Cancellation Comments
2.  Select SDEC CANCELLATION COMMENT HASH TAG: type “??” to choose from the list of existing Hash tags
3.  From the list of hash tags, choose the hash tag you wish to edit and hit enter.
4.  The selected hash tag name will be displayed in the next line, hit enter or type the new Hash tag name.
    - The maximum number of characters allowed in the hash tag name is 30.
5.  The COMMENT TEXT shows the existing Text. Hit enter to keep it or “…” to make a change to the comment text.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/011.png)

<span id="_Toc57975551" class="anchor"></span>Figure 10: Edit Local Cancellation Hashtag

#### Virtual Care Manager Launch Page 

When scheduling an appointment into a VA Video Connect (VVC) Clinic, the VCM launch page will automatically open in the default browser.

![](vista-scheduling-enhancement-vse-gui-1-7-2-1-user-guide-addendum-update/012.png)

<span id="_Toc57975552" class="anchor"></span>Figure 11: VCM Launch Page