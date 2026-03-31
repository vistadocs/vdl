---
title: VistA Scheduling Enhancement (VSE) GUI 1.7.1_User_Guide_Addendum
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: .1_User_Guide_Addendum
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 1.7
patch_id: SD*1.7
group_key: "SD:SD:1.7"
file_numbers: []
security_keys: []
menu_options: 0
description: Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Scheduling Graphical User Interface (VS GUI) module is the Windows GUI version of the Patient Information Management System (PIMS) Scheduling module. It provides appointment management functio
audience: 
keywords: 
  - span
  - view
  - contact
  - scheduling
  - vista
  - guide
  - addendum
  - patient
  - class
  - grid
page_count: 0
word_count: 1615
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 3
revision_newest: 09/09/2020
revision_oldest: 07/13/2020
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_1_7_1_user_guide_addendum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_1_7_1_user_guide_addendum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/001.png)

# VS GUI User Guide Addendum


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VS GUI User Guide Addendum](#vs-gui-user-guide-addendum)
  - [Revision History](#revision-history)
  - [List of Figures](#list-of-figures)
    - [Introduction](#introduction)
    - [System Summary](#system-summary)
    - [Key Feature Update in Version 1.7.1](#key-feature-update-in-version-171)
Release 1.7.1 Update

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date       | Revision | Description                                                                                                               | Author                             |
|------------|----------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 09/09/2020 | 1.2      | Updated install period, table of contents and list of figures.                                                            | <span class="mark">REDACTED</span> |
| 07/23/2020 | 1.1      | All changes accepted, updated Figure 3, 8, 9, and 12 with new screenshots, updated table of contents and list of figures. | <span class="mark">REDACTED</span> |
| 07/13/2020 | 1.0      | Created 1.7.1 Release Update Feature Documentation                                                                        | <span class="mark">REDACTED</span> |

Enter alt text for table.
## List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Scheduling Graphical User Interface (VS GUI) module is the Windows GUI version of the Patient Information Management System (PIMS) Scheduling module. It provides appointment management functions included in PIMS Scheduling, but with the added convenience and usability of a GUI.

#### Purpose

The Veterans Health Administration (VHA) Office of Veterans Access to Care (OVAC) requested an enterprise enhancement for the VS package that supports COVID-19 response. The enhancement reduces operating costs for VHA and improves operational efficiencies, resulting in patient-centered access to care, coordinated care, increased customer satisfaction, and the reduction of excessive cycle/wait time for scheduling patients.

#### Overview

VS GUI is a software module that allows schedulers to make appointments quickly by viewing multiple appointment request types and multiple clinics in one screen. A scheduler can easily view patient requests for service, find the next available open appointment, view the provider’s availability in multiple clinics, and track a patient’s appointment process. Refer to <span id="_bookmark8" class="anchor"></span>[System](\l) [Summary](#_bookmark8) for a more detailed description of VS GUI functionality.

#### Disclaimers

#### Software Disclaimers

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgment if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimers

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### Project References

#### Information

The VS GUI points of contact (POCs) include:
- <span class="mark">REDACTED</span>
VSE Resources
- Veterans Health Administration (VHA) VSE SharePoint: <span class="mark">REDACTED</span>
- [VA Software Document Library (VDL) – Scheduling (VSE manuals near the bottom):](https://www.va.gov/vdl/application.asp?appid=100)
- National Return to Clinic (RTC) Order: <span class="mark">REDACTED</span>

### System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSE project delivers a series of enhancements to legacy VistA Scheduling Version 5.3 via the VS GUI application.
This update is for the nationally released version 1.7.1, which includes VS GUI 1.7.1 R1 and VistA patch SD\*5.3\*745. At time of publishing, install period is projected for September 2020. This update includes the following:
- Ability to view Computerized Patient Record System (CPRS) consult tab details from Request Management (RM) Grid.
- Update Clinically Indicated Date (CID) labels to Patient Indicated Date (PID) throughout the application.
- Ability to save updated PID for an appointment previously cancelled by patient or no show.
- Addition of new cancellation reason “PANDEMIC” to use for COVID-19 related cancellations.
- Addition of columns to the RM grid displaying the number of contact attempts (phone) and the last date a letter contact attempt was made.
- Allow View Only users to access contact attempts screen.
- Realigning of RM grid to improve logic and increase real estate.

### Key Feature Update in Version 1.7.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ability to View CPRS Consult Tab Details from RM Grid

Schedulers can see the CPRS Consult tab detail as the View Request option for Consults. Right- click on a consult in the RM Grid and navigate to APPT/Veteran Disposition \> View Request. This will open consult details found in CPRS.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/002.png)
<span id="_Toc163222420" class="anchor"></span>Figure 1: Display CPRS Consult Tab Details.
This is the Consult View in VS GUI. This view is the top part of the consult view and the scheduler will easily see the PC Provider, Primary Eligibility, Requesting Provider and the Urgency.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/003.png)
<span id="_Toc163222421" class="anchor"></span>Figure 2: Patient Consult Detail Window – 1.
This bottom part of the Consult View will allow the scheduler to view the Status and the Facility Activity of the consult.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/004.png)
<span id="_Toc163222422" class="anchor"></span>Figure 3: Patient Consult Detail Window – 2.

#### Update CID Date Label to PID Throughout the Application

The CID date label has been updated to reflect PID in all views of the application. The CID/Preferred Date is replaced with PID Date in the following locations: RM Grid(headers), RM Grid(export), RM Grid(print), User Preferences, New APPT Request Window and View Request Window.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/005.png)
<span id="_Toc163222423" class="anchor"></span>Figure 4: CID Date Label Updated To PID in RM View.
When viewing the appointment request, CID has been changed to PID.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/006.png)
<span id="_Toc163222424" class="anchor"></span>Figure 5: CID Date Label Updated To PID in Appointment Request.

#### Ability to Save Updated PID for an Appointment Previously Cancelled by Patient or No Show

When rescheduling a previously cancelled by patient or no-show appointment, the scheduler will be able to enter a new PID date prior to rescheduling. In the past the scheduler would have no option to change the original date entered in the request after the initial cancellation.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/007.png)
<span id="_Toc163222425" class="anchor"></span>Figure 6: PID Can Be Updated To Reflect Change After Cancellation By Patient.

#### Addition of new cancellation reason “PANDEMIC” to use for COVID-19 related cancellations

Schedulers will now be able to choose PANDEMIC as a reason for cancellation. In the past the scheduler would have to choose “Other” and then type remarks as indicated by local/national guidelines.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/008.png)
<span id="_Toc163222426" class="anchor"></span>Figure 7: PANDEMIC As Cancellation Option.

#### Addition of Contact Attempt Column to RM Grid

Schedulers will now see the number of phone Contact Attempt (CA) and the date a CA letter was sent when viewing the RM Grid. The contact attempts view will show the attempted date/time, comments from the scheduler, and the name of the scheduler who entered them.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/009.png)
<span id="_Toc163222427" class="anchor"></span>Figure 8: Display Contact Attempt Information In The RM Grid.
To document new contact attempt information, select the requested patient’s name from the list in the request grid, right-click and from the dialog box select Contact Attempts. The Contact Attempt dialog box displays showing the request information about the patient and the option to enter Call or Letter contact attempt. When submitting the new contact attempt details the information will be displayed at the bottom of the new Contact Attempt screen and highlighted in Green.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/010.png)
<span id="_Toc163222428" class="anchor"></span>Figure 9: New Contact Attempt Entry Window.

#### Allow View Only Users to Access Contact Attempts Screen

View-Only users will have the ability to view when a patient was last contacted. The screen layout remains the same for View-Only users, but certain options will be grayed out. View only users cannot make any changes or submit any contact attempts. The figure below shows the drop down with “Contact Attempts” as an available option when the user right clicks on the request.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/011.png)
<span id="_Toc163222429" class="anchor"></span>Figure 10: RM Grid View For “View Only” Users.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/012.png)
<span id="_Toc163222430" class="anchor"></span>Figure 11: Contact Attempt View For “View Only” Users.

#### Realigning of RM grid to improve logic and increase real estate

There are changes to existing RM grid field titles and the default order which can be changed with the User Preferences option. Any changes from the default order can also be saved to the user’s personal preference.
1.  Updated headers for existing fields
    - Request Type = Request
    - CID/Preferred Date = PID
    - Entered/RR No Date = Entered
2.  The new default sort order of the RM Grid is as follows:
    - Request
    - Wait Time
    - Patient Name
    - SSN (*repositioned*)
    - CA Phone (Contact Attempts/Phone – *New Field*)
    - CA Letter (Contact Attempts/Letter – *New Field*)
    - MRTC
    - SCVisit
    - Telephone
    - Priority
    - PID
    - Entered
    - Requestor
    - Requested By
    - Clinic/Service
    - Comment

#### Validate VS GUI Version Matches Current Build Release

After the introduction of 1.7.0.1 VS GUI, if a user tries to login with the wrong version of VS GUI, the user will receive a popup message requiring them to install the latest VS GUI version.
![](vista-scheduling-enhancement-vse-gui-1-7-1-user-guide-addendum/013.png)
<span id="_Toc163222431" class="anchor"></span>Figure 12: Wrong VS GUI Version Error Message.
