---
title: VSE for Clinical Staff (VSECS) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VSE for Clinical Staff (VSECS)
app_code: SD
app_name: Scheduling
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: The Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Scheduling Enhancement for Clinical Staff (VSECS) module is a VA-internal web application that allows clinical staff to track patient appointments from check-in, through the clinic workflo
audience: 
keywords: 
  - span
  - class
  - vsecs
  - staff
  - clinical
  - guide
  - figure
  - daily
  - anchor
  - appointment
page_count: 0
word_count: 7560
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/vsecs_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/vsecs_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

![](vse-for-clinical-staff-vsecs-user-guide/001.png)

# VSE For Clinical Staff


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VSE For Clinical Staff](#vse-for-clinical-staff)
- [User Guide](#user-guide)
  - [Revision History](#revision-history)
  - [List of Figures](#list-of-figures)
    - [Introduction](#introduction)
    - [System Summary](#system-summary)
    - [User Access Levels](#user-access-levels)
    - [Getting Started](#getting-started)
    - [Using the Application](#using-the-application)
    - [Troubleshooting/Help Section](#troubleshootinghelp-section)
    - [Appendix](#appendix)

# User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version – 1.29

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Enter alt text for table. </caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 46%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/28/2024</td>
<td>1.29</td>
<td>Updated to add the new Arrived Column on the Daily Appointment List. Also added Arrived as a new Workflow Status selection on the Daily Workflow List.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>02/15/2024</td>
<td>1.28</td>
<td><p>Updated to add a filter function to the Insurance and Demographics columns of the Daily Appointment List.</p>
<p>Enables users to: undo marking a queue appointment complete; view a list of multiple appointments patients have for the day across all clinics; and, select and deselect column filters with more than three filter options.</p></td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>12/13/2023</td>
<td>1.27</td>
<td>Updated to add a filter function to Check-In Step column of Daily Appointment List. Reinstated sorting feature to Check-In Time column of Daily Appointment/Daily Workflow Lists.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>11/13/2023</td>
<td>1.26</td>
<td>Updated to add filter to columns for Check-In Times on the Daily Appointment/Daily Workflow Lists, and Pre-Check-In and eCheck-In on the Daily Appointment List.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/28/2023</td>
<td>1.25</td>
<td>Updated to display the Clinic List drop-down in alphabetical order.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>07/07/2023</td>
<td>1.24</td>
<td>Updated to implement the ability to provide system notifications to users.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>06/13/2023</td>
<td>1.23</td>
<td>Updated the Queue List to include the Memo Column</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>04/04/2023</td>
<td>1.22</td>
<td>Updated to show eCheck-Ins and Pre-Check-Ins completed count on the Daily Appointment and Daily Workflow Lists. Updated verbiage presented when attempting to delete a queue that still has patients in an incomplete status.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>03/20/2023</td>
<td>1.21</td>
<td>Updated document to remove the trash can icon from queuing so users cannot delete a patient from a queue</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>03/07/2023</td>
<td>1.20</td>
<td>Updated the document to update the phone number field under section 5.6</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>02/14/2023</td>
<td>1.19</td>
<td>Updated the document with section 5.6 on added messaging</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>02/07/2023</td>
<td>1.18</td>
<td>Updated the document to revise sections 5.4.1.1 and 5.4.1.3 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>02/03/2023</td>
<td>1.17</td>
<td>Updated the document to revise section 5.4 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>01/25/2023</td>
<td>1.16 (not published)</td>
<td>Updated the document with section 5.4 on queues</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>12/14/2022</td>
<td>1.15</td>
<td>Updated the document with section 5.2.2 Updates Check In and Check Out Status Logic</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>10/19/2022</td>
<td>1.14</td>
<td>Updated the document with section 5.7 Displays Checkout Time and Indicator.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>09/28/2022</td>
<td>1.13</td>
<td><p>Added section 6.3 Pop-up Message to Ensures Users are Running the Current Version.</p>
<p>Updated 6.1 Enhanced Error message section to include the new error message logic.</p></td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>09/21/2022</td>
<td>1.12</td>
<td>Updated document to include removal of insurance column for MANILA – RO 358.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>09/15/2022</td>
<td>1.11</td>
<td>Updated document to include sections 5.6 Display Number of Checked-In Appointments and 6.2 Reset Button</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>09/07/2022</td>
<td>1.10</td>
<td>Updated document to include section 5.1.3 Validating User Access to VistA Instances.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/30/2022</td>
<td>1.9</td>
<td>Updated document to include the following functionalities: Flag Legend and Toggle to Disable Notifications for Updated Appointments.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>08/22/2022</td>
<td>1.8</td>
<td>Updated document to include the following new functionalities: Display Fugitive Felon, Local/National &amp; Restricted Record Flags, and Enhanced Error Messages.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>08/10/2022</td>
<td>1.7</td>
<td>Updated Section 5.3 Daily Workflow List to include the Memo functionality.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="even">
<td>06/14/2022</td>
<td>1.6</td>
<td>Updated Section 5.4 Medication List and Pre-Visit Summary with Sensitive record pop-up page.</td>
<td><p>VSE PMO</p>
<p>Booz Allen Hamilton</p></td>
</tr>
<tr class="odd">
<td>05/12/2022</td>
<td>1.5</td>
<td>Updated the document with Test Patient Screenshots</td>
<td>VSE PMO</td>
</tr>
<tr class="even">
<td>03/03/2022</td>
<td>1.4</td>
<td>Accepted all recommended changes and finalized the document</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="odd">
<td>03/01/2022</td>
<td>1.3</td>
<td>Updated the document with Medications List, Pre-Visit Summary, and Alert Notifications.</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="even">
<td>02/08/2022</td>
<td>1.2</td>
<td>Final review/proofread and accepted all recommended changes</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="odd">
<td>01/28/2022</td>
<td>1.1</td>
<td>Developers Review</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
<tr class="even">
<td>12/30/2021</td>
<td>1.0</td>
<td>Baseline for VSECS</td>
<td><p>VSE PMO</p>
<p>Liberty IT Solutions</p></td>
</tr>
</tbody>
</table>

Enter alt text for table.
## List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) Scheduling Enhancement for Clinical Staff (VSECS) module is a VA-internal web application that allows clinical staff to track patient appointments from check-in, through the clinic workflow, and to a completed appointment.

#### Purpose

The Veterans Health Administration (VHA) Office of Integrated Veteran Care (IVC) requested VSE for Clinical Staff, a new web application to improve the overall Veteran check-in experience and reduce operating costs for VHA.

#### Overview

VSECS is a VA-internal web application that allows staff at VA clinics to manage appointment workflow at a clinic or set of clinics. Users can customize the application to display daily appointments for a specific group of clinics and save multiple personal clinic lists. Users can also view and update appointments by workflow status. Refer to [System Summary](#system-summary) for a more detailed description of VSE for Clinical Staff functionality.

#### Disclaimers

#### Software Disclaimers

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgment if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimers

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are consistent with the stated purpose of the VA.

#### Project References

#### Information

The VSECS points of contact (POCs) include:
> » OIT ESE - Scheduling Support
> » IVC – I&T PCI Technical POCs <span class="mark">– REDACTED</span>
> » Scheduling Technical Director <span class="mark">– REDACTED</span>
> » IVC - Innovation and Technology Division Business/Product Owner/Director <span class="mark">– REDACTED</span>
> » IVC - Innovation and Technology Division Program Manager <span class="mark">– REDACTED</span>
> » IVC - Innovation and Technology PCI Subject Matter Expert (SME) <span class="mark">– REDACTED</span>
VSECS Resources
- [VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=100)

#### Help Desk

Refer to [Section 6](#fugitive-felon-nationallocal-and-restricted-record-flags) for additional information.

### System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSE for Clinic Staff is a web-based, cloud-hosted application that assists with accessing and managing appointment workflow at a clinic or set of clinics. It consists of three primary functions: Daily Appointment List, Daily Workflow List, and Clinic List Management. The Daily Appointment List tracks appointments for all the clinics available under the Clinic List. The Daily Workflow List shows the current workflow status a patient is in and allows the user to track and change the status of the workflow. The Clinic List Management allows clinicians to group clinics into one manageable list.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSE for Clinical Staff is accessible to any VA network user who has a Personal Identity Verification (PIV) card and Identity and Access Management (IAM) account provisioned to a VistA station.
- Schedulers are required to have the SDECRPC Menu Option. All scheduling personnel should already have the menu option.
- Non-Schedulers, Nurses, and Providers are required to have SDECRPC Menu Option and SDECVIEW Key.
- Users needing access to the Queue Management tab must have SD SUPERVISOR Key assigned to them.
- Users must have SECONDARY MENU OPTIONS: VIAB WEB SERVICES OPTION to utilize patient search for queuing.

### Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the VSE for Clinical Staff application, the user follows these initial process steps:

#### Logging Into VSE For Clinical Staff

1.  To access VSECS, open either the Chrome or Edge browser and copy this hyperlink (<span class="mark">REDACTED</span>) into the address bar.
2.  A Login window displays; click “sign in with VA PIV Card” to sign in using your PIV.
![](vse-for-clinical-staff-vsecs-user-guide/002.png)
<span id="_Toc168050431" class="anchor"></span>Figure 1: Single Sign-On Internal (SSOi) Login.
3.  If login validation is successful, the VSE for Clinical Staff home page will be displayed.
![](vse-for-clinical-staff-vsecs-user-guide/003.png)
<span id="_Toc168050432" class="anchor"></span>Figure 2: VSECS Home Page.

### Using the Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes VSECS functions inside the Daily appointment list, Daily workflow list, and Clinic list management, and how to use these tools to create, edit, view, and track patient workflow status.

#### Clinic List Management

#### Create New Clinic List

Creating a Clinic List allows the clinicians to group clinics into one manageable list. The Clinic List drop-down will display in alphabetical order, with the default Clinic List at the top. If you have not created a Clinic List, the appointment list view and Workflow List will not be accessible. After successfully logging into VSECS, follow the steps below to create a new Clinic List:
1.  From the VSECS home page left navigation, click on Clinic List Management. If you have not created a Clinic List before it will redirect you to the Create Clinic List page, [Figure 4: Create a Clinic List](#_Ref91172301), to create a Clinic List. If you have created a Clinic List before, the Clinic List Management page displays with the list of Clinics as shown on [Figure 3: Clinic List Management](#_Ref94258625).
2.  From the Clinic List Management page, click on Create New Clinic List and the Create Clinic List page will be displayed as shown on [Figure 4: Create a Clinic List](#_Ref91172301).
![](vse-for-clinical-staff-vsecs-user-guide/004.png)
<span id="_Ref94258625" class="anchor"></span>Figure 3: Clinic List Management.
![](vse-for-clinical-staff-vsecs-user-guide/005.png)
<span id="_Ref91172301" class="anchor"></span>Figure 4: Create A Clinic List.
3.  On the Create Clinic List Page:
    1.  From the top, click on the Select Facility drop-down menu to choose a facility. The clinics under that facility will be populated inside the Add Clinics multi-text box on the bottom left corner.
![](vse-for-clinical-staff-vsecs-user-guide/006.png)
<span id="_Toc168050435" class="anchor"></span>Figure 5: Create Clinic List: Choosing A Facility.
2.  Enter a name for your Clinic List. If this is your first time creating a Clinic List, it will automatically become the default Clinic List. Select the Default Clinic List check box to set the new Clinic List as your default Clinic List. Note: There can only be one Default Clinic List.
![](vse-for-clinical-staff-vsecs-user-guide/007.png)
<span id="_Toc168050436" class="anchor"></span>Figure 6: Create Clinic List: Setting A Clinic List As Default.
3.  Type in the search bar to narrow down the Clinic List as shown below.
![](vse-for-clinical-staff-vsecs-user-guide/008.png)
<span id="_Toc168050437" class="anchor"></span>Figure 7: Create Clinic List: Searching For Clinics.
4.  The final step before creating the list is to add the clinics to your list. Select the list of clinics from left side and use the buttons to move the selection or everything across to the right. You can only add up to 50 clinics to your new list. Finally, click on the Create button to create the new Clinic List.
    ![](vse-for-clinical-staff-vsecs-user-guide/009.png)
<span id="_Toc168050438" class="anchor"></span>Figure 8: Create Clinic List Actions.
![](vse-for-clinical-staff-vsecs-user-guide/010.png)
<span id="_Toc168050439" class="anchor"></span>Figure 9: Create Clinic List: Adding Clinics To The New Clinic List.

#### Edit/Delete Personal Clinic List

Once a Clinic List has been created, it can be edited by adding or removing clinics from the List.
To edit a personal Clinic List:
1.  Navigate to the Clinic List Management Page to see a list of personal Clinic Lists.
![](vse-for-clinical-staff-vsecs-user-guide/011.png)
<span id="_Toc168050440" class="anchor"></span>Figure 10: Clinic List Management Page.
2.  Click the Edit button of the personal Clinic List you want to edit to display the Edit Clinic List Page. After making the changes, click the Save List button to save the changes to the personal Clinic List. Click the Back to List button to exit the Edit Clinic Page without making any changes to the Facility or Clinic Name of the list. NOTE: When moving the clinics from the left to the right side of the Clinic List it automatically saves the changes.
![](vse-for-clinical-staff-vsecs-user-guide/012.png)
<span id="_Toc168050441" class="anchor"></span>Figure 11: Editing A Clinic List.
3.  To delete a Clinic List, from the Clinic List Management Page, click the Delete button of a personal Clinic List. The Delete Clinic List Page displays asking if you want to delete the list. Click either the Delete List button or the Back To List button to cancel the action. NOTE: Your default personal Clinic List can’t be deleted; the Delete button is always disabled for that list.
![](vse-for-clinical-staff-vsecs-user-guide/013.png)
<span id="_Toc168050442" class="anchor"></span>Figure 12: Delete A Clinic List.

#### Validating User Access To VistA Instances

VSECS will validate a user’s clinic list access upon app load. Clinics that the user no longer has access to will be removed from the drop-down on the Daily Appointment List and Daily Workflow List. Additionally, the clinics the user no longer has access to will only be able to be deleted within the Clinic List Management page to indicate the user no longer has access to that clinic as shown below.
![](vse-for-clinical-staff-vsecs-user-guide/014.png)
<span id="_Toc168050443" class="anchor"></span>Figure 13: Example Of A User With No Access To The Clinic List.

#### Daily Appointment List

Once the clinic list is created, it will show up in the Daily Appointment List for the clinical staff to view and track.

#### Sorting

The Daily Appointment List displays all the appointments for that day for all the clinics you have under the Clinic List. It tracks patient attributes like Current Check-In Step, Pre-Check-In status, E-Check-In status, Demographics, and Insurance indicators.
Use the drop-down button to select a different Clinic List to see the clinics and appointments under those clinics. The up and down arrows next to the column headers allow you to sort based on the type of column.
> **NOTE:** The insurance column on the Daily Appointment List will not show for MANILA-RO Station ID 358.
![](vse-for-clinical-staff-vsecs-user-guide/015.png)
<span id="_Toc168050444" class="anchor"></span>Figure 14: The Sorting Buttons Available On The Daily Appointment List.

#### Filtering

Filtering is enabled in the Daily Appointment List for the Check-In Time, Patient, Current Check-In Step, Pre-Check-In Step, eCheck-In, Demographics, and Insurance columns. Columns with four or more filters allow users to select or deselect filter options when needed.
![](vse-for-clinical-staff-vsecs-user-guide/016.png)
<span id="_Toc168050445" class="anchor"></span>Figure 15: The Filtering Buttons Available On The Daily Appointment List.

#### Arrived Column On Daily Appointment List

The Daily Appointment List includes the Arrived Column sitting between the Appt Time and the Check-In Time Columns. This will allow staff to indicate that a patient has physically arrived at the clinic and is ready to be called back for their appointment. To apply this feature, see the Actions Column and reference the location pin icon. Once activated, that icon will be greyed out and the function is now disabled. Then, “Yes” will appear in the Arrived Column.
![](vse-for-clinical-staff-vsecs-user-guide/017.png)
<span id="_Toc168050446" class="anchor"></span>Figure 16: Highlighting The Arrived Column. Also Shows The Location Pin Icon Both The Activated (“Yes” Displayed Under Arrived) And Not Activated Status Under The Actions Column Of The Daily Appointment List.

#### Check-In Time Filtering 

By clicking on the Check-In Time filter button on the right side of the column, users can filter by Not Checked-In, Checked-In, and Checked Out in the Daily Appointment List.
![](vse-for-clinical-staff-vsecs-user-guide/018.png)
<span id="_Toc168050447" class="anchor"></span>Figure 17: Check-In Time Column With Pop-Up Showing Filtering Options On The Daily Appointment List.

#### Filtering In Patient Column

The Patient column of the Daily Appointment List allows users to filter by searching a patient’s name.
![](vse-for-clinical-staff-vsecs-user-guide/019.png)
<span id="_Toc168050448" class="anchor"></span>Figure 18: Patient Column With Filter Button Highlighted On The Daily Appointment List.

#### Filtering of Current Check-In Step Column

The Current Check-In Step column of the Daily Appointment List allows users to filter patients by their check in step.
![](vse-for-clinical-staff-vsecs-user-guide/020.png)
<span id="_Toc168050449" class="anchor"></span>Figure 19: Current Check-In Step Column With Filter Button On Daily Appointment List.

#### Pre-Check-In Filter

The Pre-Check-In column of the Daily Appointment List includes a filter to allow users to filter patients by their pre-check-in status.
![](vse-for-clinical-staff-vsecs-user-guide/021.png)
<span id="_Toc168050450" class="anchor"></span>Figure 20: Pre-Check-In Filter Button On The Daily Appointment List.

#### eCheck-In Filter

The eCheck-In column of the Daily Appointment List also includes a filter to allow users to filter patients by their echeck-in status.
![](vse-for-clinical-staff-vsecs-user-guide/022.png)
<span id="_Toc168050451" class="anchor"></span>Figure 21: eCheck-In Filter Button On The Daily Appointment List.

#### Demographics Filter

The Demographics column of the Daily Appointment List allows users to filter patients by demographics.
![](vse-for-clinical-staff-vsecs-user-guide/023.png)
<span id="_Toc168050452" class="anchor"></span>Figure 22: Demographics Filter Button On The Daily Appointment List.

#### Insurance Filter

The Insurance column of the Daily Appointment List allows users to filter patients' insurance status.
![](vse-for-clinical-staff-vsecs-user-guide/024.png)
<span id="_Toc168050453" class="anchor"></span>Figure 23: Insurance Filter Button On The Daily Appointment List.

#### Flag Legend Button

A Flag Legend button will be displayed on Appointments in the Daily Appointment List. The information shown when clicking on that button is explained in the [Fugitive Felon, National/Local, and Restricted Record Flags section](#fugitive-felon-nationallocal-and-restricted-record-flags) of this document.
![](vse-for-clinical-staff-vsecs-user-guide/025.png)
<span id="_Toc168050454" class="anchor"></span>Figure 24: Flag Legend Button On The Daily Appointment List Page.

#### Refresh Button

A Refresh Appointment List Button is included on the Daily Appointment List as a convenience for the users. Clicking that button engages the page to refresh.
![](vse-for-clinical-staff-vsecs-user-guide/026.png)
<span id="_Toc168050455" class="anchor"></span>Figure 25: Refresh Appointment List Button On The Daily Appointment List Page.

#### Printing The Daily Appointment List

To print your Daily Appointment List, click the Print button on the right corner of the Daily Appointment List table and you will be able to save the Daily Appointment List in PDF format.
![](vse-for-clinical-staff-vsecs-user-guide/027.png)
<span id="_Toc168050456" class="anchor"></span>Figure 26: Printing The Daily Appointment List In PDF Format.
![](vse-for-clinical-staff-vsecs-user-guide/028.png)
<span id="_Toc168050457" class="anchor"></span>Figure 27: Printed PDF Format Of The Daily Appointment List.

#### Check In And Check Out Status Logic

The Daily Appointment List will show if an appointment has been checked in and if an appointment has been fully checked out. Appointments that were checked in and checked out will display both statuses and times.
![](vse-for-clinical-staff-vsecs-user-guide/029.png)
<span id="_Toc168050458" class="anchor"></span>Figure 28: Daily Appointment List With The New Check In And Check Out Logic.
![](vse-for-clinical-staff-vsecs-user-guide/030.png)
<span id="_Toc168050459" class="anchor"></span>Figure 29: Not Checked In.
![](vse-for-clinical-staff-vsecs-user-guide/031.png)
<span id="_Toc168050460" class="anchor"></span>Figure 30: Checked In But Not Checked Out.
![](vse-for-clinical-staff-vsecs-user-guide/032.png)
<span id="_Toc168050461" class="anchor"></span>Figure 31: Checked Out With Act Req.
![](vse-for-clinical-staff-vsecs-user-guide/033.png)
<span id="_Toc168050462" class="anchor"></span>Figure 32: Completely Checked Out.
![](vse-for-clinical-staff-vsecs-user-guide/034.png)
<span id="_Toc168050463" class="anchor"></span>Figure 33: Completely Checked Out But Never Checked In.

#### Daily Workflow List

The Daily Workflow List Page shows a patient’s current workflow status and allows users to track and change the status of the workflow.

#### Sorting 

Appointments can be sorted based on Patient Name, Clinic, Appointment Time, Check-In Time, and Workflow Status. Sorting is done by simply clicking the up and down arrows.
![](vse-for-clinical-staff-vsecs-user-guide/035.png)
<span id="_Toc168050464" class="anchor"></span>Figure 34: Sorting A Daily Workflow List.

#### Filtering

Filtering is enabled in the Daily Workflow List on the Patient, Check-In Time, and Workflow Status columns. Columns with four or more filters allow users to select or deselect filter options when needed.
![](vse-for-clinical-staff-vsecs-user-guide/036.png)
<span id="_Toc168050465" class="anchor"></span>Figure 35: Filtering A Daily Workflow List.

#### Filtering In Patient Column

The Patient column of the Daily Workflow List allows users to filter by searching a patient’s name.
![](vse-for-clinical-staff-vsecs-user-guide/037.png)
<span id="_Toc168050466" class="anchor"></span>Figure 36: Patient Column With Filter Button Highlighted On The Daily Workflow List.

#### Check-In Time Filter

The Check-In Time column of the Daily Workflow List allows users to filter by clicking on the button on the right in that column. A pop-up box will display to let users filter by Not Checked-In, Checked-In, and Checked-Out.
![](vse-for-clinical-staff-vsecs-user-guide/038.png)
<span id="_Toc168050467" class="anchor"></span>Figure 37: Check-In Time Filter Engaged Showing A Pop-Up Box On A Daily Workflow List.

#### Workflow Status Filter

Records can be filtered based on the current workflow status. Click the Workflow Status Filter button on the right side of the Workflow Status column to display the workflow Filter modal window. From the modal window, users can filter their work list by workflow status by selecting the check boxes next to the workflow statuses.
![](vse-for-clinical-staff-vsecs-user-guide/039.png)
<span id="_Toc168050468" class="anchor"></span>Figure 38: Displaying Choices To Filter On Workflow Statuses.

#### Enable Select/Deselect All Functions For Filters With Over Three Options

A Select All option has been added to column filters that have more than three filter options to choose from.
![](vse-for-clinical-staff-vsecs-user-guide/040.png)
<span id="_Toc168050469" class="anchor"></span>Figure 39: Displaying The Select All Option Under Select Workflow Filters.

#### Arrived Status Added To Workflow Status Drop Down

The patient’s actual arrival status is shown under the Workflow Status Column. Any status other than Call, Call Again, and No Show will populate that Arrived Column with “Yes” reflected on the Daily Appointment List.
![](vse-for-clinical-staff-vsecs-user-guide/041.png)
<span id="_Toc168050470" class="anchor"></span>Figure 40: Highlighting “Arrived” Feature Under The Workflow Status Drop Down List.

#### Flag Legend Button

A Flag Legend button will be displayed on Appointments in the Daily Workflow List. Information shown when clicking on that button is explained in the [Fugitive Felon, National/Local, and Restricted Record Flags section](#fugitive-felon-nationallocal-and-restricted-record-flags) of this document.
![](vse-for-clinical-staff-vsecs-user-guide/042.png)
<span id="_Toc168050471" class="anchor"></span>Figure 41: Flag Legend Button On The Daily Workflow List.

#### Refresh Button

A Refresh Appointment List Button is included on the Daily Workflow List as a convenience for the users. Clicking that button engages the page to refresh.
![](vse-for-clinical-staff-vsecs-user-guide/043.png)
<span id="_Toc168050472" class="anchor"></span>Figure 42: Refresh Button On The Daily Workflow List.

#### Change A Workflow Status

To change a patient’s workflow status, from the Workflow Status column, click the drop-down arrow and select the new step. A pop-up page displays asking to confirm the changes. Click Accept and the workflow status will be updated.
![](vse-for-clinical-staff-vsecs-user-guide/044.png)
<span id="_Toc168050473" class="anchor"></span>Figure 43: Daily Workflow List – Select New Workflow Step.
![](vse-for-clinical-staff-vsecs-user-guide/045.png)
<span id="_Toc168050474" class="anchor"></span>Figure 44: Confirming A Workflow Status Change To “Needs Clerk.”
![](vse-for-clinical-staff-vsecs-user-guide/046.png)
<span id="_Toc168050475" class="anchor"></span>Figure 45: Daily Workflow List – New Workflow Status “Needs Clerk.”

#### Alert Notifications

Whenever a change to the Daily Workflow List occurs, an alert notification will be displayed on the taskbar. Even if the VSECS application is in the background, the alert notification still pops up on the taskbar informing the staff of the changes. Changes that trigger an alert include a new appointment in the list or workflow status change.
![](vse-for-clinical-staff-vsecs-user-guide/047.png)
<span id="_Toc168050476" class="anchor"></span>Figure 46: VSECS Alert Notification.
Similarly, if anything changes on the Daily Workflow List the affected row will be highlighted.
![](vse-for-clinical-staff-vsecs-user-guide/048.png)
<span id="_Toc168050477" class="anchor"></span>Figure 47: Patient On The Second Row Highlighted To Notify There Was A Recent Change To The Record.

#### Disable Notifications For Updated Appointments

The below toggle has been added to the Settings page to let users disable all Windows notifications and alerts for updated appointments.
![](vse-for-clinical-staff-vsecs-user-guide/049.png)
<span id="_Toc168050478" class="anchor"></span>Figure 48: Disable Window Alert/Notifications On Setting Page.

#### Memo Column 

#### Adding A Memo

Users can add a memo to a specific appointment by selecting “Add” under the Memo column for that appointment.
![](vse-for-clinical-staff-vsecs-user-guide/050.png)
<span id="_Toc168050479" class="anchor"></span>Figure 49: Memo Column.
A pop-up will appear for the Memo to be entered. The user can type in a memo and select “Add Memo.”
> **NOTE:** There is a 100-character max for memos.
![](vse-for-clinical-staff-vsecs-user-guide/051.png)
<span id="_Toc168050480" class="anchor"></span>Figure 50: Adding the New Memo To The Appointment.
The Memo will show up in the Memo column of the related appointment with a timestamp and the initials of the user who entered the memo.
![](vse-for-clinical-staff-vsecs-user-guide/052.png)
<span id="_Toc168050481" class="anchor"></span>Figure 51: The New Memo Will Show Under The 'Memo" Column.

#### Adding Multiple Memos To An Appointment 

Multiple memos can be added to the appointment. A user can repeat the process to add an additional memo. When there is more than one memo on an appointment, a new option will appear in the column named “More.” Only the most recent memo will show on the Daily Workflow list.
![](vse-for-clinical-staff-vsecs-user-guide/053.png)
<span id="_Toc168050482" class="anchor"></span>Figure 52: Additional Memos Can Be Added By Clicking The "Add" Button.
If a user selects more, a pop-up will appear to show all memos for that appointment.
![](vse-for-clinical-staff-vsecs-user-guide/054.png)
<span id="_Toc168050483" class="anchor"></span>Figure 53: Click The "More" Button Under The Memo Column To View All The Memos For The Appointment.

#### Check In And Check Out Status Logic

The Daily Workflow List will show if an appointment has been checked in and if an appointment has been fully checked out. Appointments that were checked in and checked out will display both statuses and times.
![](vse-for-clinical-staff-vsecs-user-guide/055.png)
<span id="_Toc168050484" class="anchor"></span>Figure 54: Daily Workflow List With The New Check In And Check Out Logic.

#### Queues

VSE for Clinical Staff Queuing functionality allows users to add Veterans to a queue regardless of whether they are in the VA system and where they do not have an appointment, so they can request services based on their arrival time.

#### Queue Management

Users that have SD SUPERVISOR Key assigned to them will have the Queue Management tab within VSECS. Select Queue Management to create a queue.
![](vse-for-clinical-staff-vsecs-user-guide/056.png)
<span id="_Toc168050485" class="anchor"></span>Figure 55: Queue Management Tab.
From the Queue Management page, a user with SD SUPERVISOR Key can create queues, or view, edit, and delete existing queues.
![](vse-for-clinical-staff-vsecs-user-guide/057.png)
<span id="_Toc168050486" class="anchor"></span>Figure 56: Queue Management Page.

#### Creating Queues

- Select “Create New Queue” on the Queue Management page.
- From the drop-down, select the applicable facility.
- Type in a name for the queue.
- Select “Create.”
> **NOTE:** Queue names must be greater than 3 characters, but less than 50.
![](vse-for-clinical-staff-vsecs-user-guide/058.png)
<span id="_Toc168050487" class="anchor"></span>Figure 57: Create Queue Page.
> **NOTE:** Users will be unable to create a duplicate queue from the Queue Management tab. If a user attempts to create a Queue with the same name as another they will see the below message.
![](vse-for-clinical-staff-vsecs-user-guide/059.png)
<span id="_Toc168050488" class="anchor"></span>Figure 58: Unable To Create A Duplicate Message.

#### Editing Queues

- Select “Edit” under the Actions column of the queue.
![](vse-for-clinical-staff-vsecs-user-guide/060.png)
<span id="_Toc168050489" class="anchor"></span>Figure 59: Editing Queue Management.
- Update the Queue Name as desired.
- Select “Update.”
![](vse-for-clinical-staff-vsecs-user-guide/061.png)
<span id="_Toc168050490" class="anchor"></span>Figure 60: Update Queue Page.

#### Deleting Queues

- Select “Delete” under the Actions column of the queue.
![](vse-for-clinical-staff-vsecs-user-guide/062.png)
<span id="_Toc168050491" class="anchor"></span>Figure 61: Deleting Queue Management.
- Select “Delete Queue.”
![](vse-for-clinical-staff-vsecs-user-guide/063.png)
<span id="_Toc168050492" class="anchor"></span>Figure 62: Delete Queue Pop-Up.
> **NOTE:** A queue can only be deleted if it does not have patients assigned to it, or if the patients that are assigned to the queue are all in a complete status. If a user attempts to delete a queue where these requirements are not met, they will receive the below notice.
![](vse-for-clinical-staff-vsecs-user-guide/064.png)
<span id="_Toc168050493" class="anchor"></span>Figure 63: Delete Queue Pop-Up If Requirements Not Met.

#### Utilizing Queues

All VSECS users have access to the Queue tab.
![](vse-for-clinical-staff-vsecs-user-guide/065.png)
<span id="_Toc168050494" class="anchor"></span>Figure 64: Queue List Page.
- From the Queue tab, select the applicable queue from the drop-down.
- Veterans in that Queue will appear.
![](vse-for-clinical-staff-vsecs-user-guide/066.png)
<span id="_Toc168050495" class="anchor"></span>Figure 65: Queue List Search Results.
- Users can select the check under Actions to mark the encounter as complete.
![](vse-for-clinical-staff-vsecs-user-guide/067.png)
<span id="_Toc168050496" class="anchor"></span>Figure 66: Action Items Check Icon.
- Once selected, the note under “Completion” will say “Yes,” and the check mark will be replaced with an undo button. The undo button is designed to reset the appointment status to not complete.
![](vse-for-clinical-staff-vsecs-user-guide/068.png)
<span id="_Toc168050497" class="anchor"></span>Figure 67: Completion Change.
![](vse-for-clinical-staff-vsecs-user-guide/069.png)
<span id="_Toc168050498" class="anchor"></span>Figure 68: Adding A Veteran to Queue.
- Use the Patient Search to add a Veteran who is already in the VA System.
> **NOTE:** Users must have SECONDARY MENU OPTIONS: VIAB WEB SERVICES OPTION to utilize patient search.
- For Veterans not in the VA System, users can manually type the Veteran’s name to add them to the queue.
![](vse-for-clinical-staff-vsecs-user-guide/070.png)
<span id="_Toc168050499" class="anchor"></span>Figure 69: Patient Search Lookup.
- If manually entered, select the icon to the right of the text box to add the Veteran to the queue.
![](vse-for-clinical-staff-vsecs-user-guide/071.png)
<span id="_Toc168050500" class="anchor"></span>Figure 70: Manually Entering.

#### Queue List Memos

A column for memos has been added to the Queue List page. The memo functionality mirrors the memo functionality that is currently in production on the Daily Workflow List.
Users can select “Add” in the memo column of the patient they need to add a memo. Once selected, the user will be presented with the below pop-up where they can type in the memo.
![](vse-for-clinical-staff-vsecs-user-guide/072.png)
<span id="_Toc168050501" class="anchor"></span>Figure 71: Add New Memo To Queue Pop-Up.
Select “Add Memo” and the page will refresh with the memo added.
![](vse-for-clinical-staff-vsecs-user-guide/073.png)
<span id="_Toc168050502" class="anchor"></span>Figure 72: Queue List With Added Memo Column.
The most recent memo will appear if multiple memos are added to the same patient. However, there will be a “More” button. If a user needs to see all memos for a patient, they can select More, and the memos will display in a pop-up as shown below.
![](vse-for-clinical-staff-vsecs-user-guide/074.png)
<span id="_Toc168050503" class="anchor"></span>Figure 73: View All Memos For Queue Pop-Up.

#### Action Column Icons

#### Viewing Current Day Appointments

VSECS gives users the ability to view whether a patient has multiple appointments for the current day, across all clinics.
![](vse-for-clinical-staff-vsecs-user-guide/075.png)
<span id="_Toc168050504" class="anchor"></span>Figure 74: Image Displaying The Current Day Appointments Button.

#### Viewing Medications List

VSECS gives users the ability to view the list of medications associated with the patient. This functionality is available on both the Daily Appointment List and Daily Workflow List.
To view the patient’s Medications List:
1.  Go to the Daily Appointment List/Daily Workflow List, from the Action column, click on the Medications button displayed on the left side of the Actions column.
    ![](vse-for-clinical-staff-vsecs-user-guide/076.png)
<span id="_Toc168050505" class="anchor"></span>Figure 75: Medications Button.
2.  If the record is sensitive, a Sensitive Record pop-up page displays asking if you want to proceed with viewing the Medication List. Click “Yes” to view the Medications List record or click “No” to go back to the Daily Appointment or Workflow List.
![](vse-for-clinical-staff-vsecs-user-guide/077.png)
<span id="_Toc168050506" class="anchor"></span>Figure 76: Sensitive Record Pop-Up Page.
3.  The Medications List page displays with the list of the patient’s medications.
![](vse-for-clinical-staff-vsecs-user-guide/078.png)
<span id="_Ref97045836" class="anchor"></span>Figure 77: Medication List Page.

#### Printing Pre-Visit Summary

This VSECS functionality allows the staff members the ability to print or save a PDF format of the Pre-Visit Summary for a patient to ensure patients are informed before their appointment. This functionality is available on both the Daily Appointment List and Daily Workflow List.
To print/save the patient’s Pre-Visit Summary,
1.  Go to the Daily Appointment List/Daily Workflow List, from the Action column, click on the Pre-Visit Summary button displayed on the right side of the Actions column.
    ![](vse-for-clinical-staff-vsecs-user-guide/079.png)
<span id="_Toc168050508" class="anchor"></span>Figure 78: Pre-Visit Summary Button.
2.  If the record is sensitive, a Sensitive Pre-Visit Summary Record pop-up page displays asking if you want to proceed with viewing the Pre-Visit Summary record. Click “Yes” to view the Pre-Visit Summary record or click “No” to go back to the Daily Appointment or Workflow List.
![](vse-for-clinical-staff-vsecs-user-guide/080.png)
<span id="_Toc168050509" class="anchor"></span>Figure 79: Sensitive Pre-Visit Summary Record Pop-Up Page.
3.  The Pre-Visit Summary Page is displayed on your default browser in a separate tab in PDF format where it can either be printed or saved.
![](vse-for-clinical-staff-vsecs-user-guide/081.png)
<span id="_Ref97048087" class="anchor"></span>Figure 80: Patient's Pre-Visit Summary.

#### Messaging

On the Daily Workflow and Daily Appointment lists, patients who have started the eCheck-in process meet the criteria for messaging and will have a message icon under the Actions column within their appointment row.
![](vse-for-clinical-staff-vsecs-user-guide/082.png)
<span id="_Toc168050511" class="anchor"></span>Figure 81: Image Showing The Added Message Icon Under The Actions Column.
When the message icon is selected for an appointment, a messaging page will then load for the patient in context. The Messages page includes the option to send the patient a message and displays messages that have previously been sent.
![](vse-for-clinical-staff-vsecs-user-guide/083.png)
<span id="_Toc168050512" class="anchor"></span>Figure 82: Message Page.
To send a message, the user will click the drop-down by Send Message. The drop-down will include two message types that can be sent to the patient: Check In Call Number or Check In Contact Attempt.
![](vse-for-clinical-staff-vsecs-user-guide/084.png)
<span id="_Toc168050513" class="anchor"></span>Figure 83: Send Message Drop-down Showing Check In Call Number Or Check In Contract Attempt.
Each message type has a text template pre-populated in the Standard Message field. Below is an example of the default message for each message type.
![](vse-for-clinical-staff-vsecs-user-guide/085.png)
<span id="_Toc168050514" class="anchor"></span>Figure 84: Check In Call Number With Default Message.
![](vse-for-clinical-staff-vsecs-user-guide/086.png)
<span id="_Toc168050515" class="anchor"></span>Figure 85: Check In Contact Attempt With Default Message.
The user will need to fill in the appropriate phone number in the Phone Number field under the Standard Message. This will insert the phone number into the text of the message. The standard message field cannot be edited.
The phone number field for Messaging includes a drop-down for country to account for international numbers.
![](vse-for-clinical-staff-vsecs-user-guide/087.png)
<span id="_Toc168050516" class="anchor"></span>Figure 86: Image Showing A Drop-Down For Countries To Account For International Numbers.
The phone number field for Messaging also includes a field for extensions.
![](vse-for-clinical-staff-vsecs-user-guide/088.png)
<span id="_Toc168050517" class="anchor"></span>Figure 87: Image Showing A Field For Phone Number Extensions.
Once the phone number has been entered in the phone number field, the user can hit the “Send” icon on the bottom left. The user will receive a confirmation pop-up when the message has been successfully sent.
![](vse-for-clinical-staff-vsecs-user-guide/089.png)
<span id="_Toc168050518" class="anchor"></span>Figure 88: Confirmation Pop-Up When The Message Has Been Successfully Sent.
Once the message has been successfully sent, the Messages page will display the message details once refreshed.
![](vse-for-clinical-staff-vsecs-user-guide/090.png)
<span id="_Toc168050519" class="anchor"></span>Figure 89: Messages Page Displaying The Message Details Once Refreshed Screenshot.

#### Fugitive Felon, National/Local, And Restricted Record Flags

Fugitive Felon, Local/National, and Restricted Record Flags will be displayed on Appointments in Daily Appointment List and Daily Workflow List. Hover your mouse over the flag icon below the patient’s name to see the type of flag the icon represents or click on an information symbol located on the right-hand side of the Daily Appointment List and Daily Workflow List. When selected, a pop-up appears with legend information regarding the flags as shown below.
![](vse-for-clinical-staff-vsecs-user-guide/091.png)
<span id="_Toc168050520" class="anchor"></span>Figure 90: Information Icon To Display Flag Legend.
![](vse-for-clinical-staff-vsecs-user-guide/092.png)
<span id="_Toc168050521" class="anchor"></span>Figure 91: Flag Legend.

#### Displays Number Of Checked-In Appointments, Count Of eCheck-In Complete And Pre-Check-In Complete

The number of Checked-in appointments will now show on the Daily Appointment and Daily Workflow List, along with the count of eCheck-ins and Pre-Check-ins completed.
![](vse-for-clinical-staff-vsecs-user-guide/093.png)
<span id="_Toc168050522" class="anchor"></span>Figure 92: Checked-In Appointments, eCheck-In, And Pre-Check-In Completed Indicators.

#### Displays Checkout Time And Indicator

The Daily Appointment List and Daily Workflow List show if an appointment has been checked out and the time of check out.
![](vse-for-clinical-staff-vsecs-user-guide/094.png)
<span id="_Toc168050523" class="anchor"></span>Figure 93: Check-Out/Check-In Time And Indicators.

### Troubleshooting/Help Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For any VSECS-related issues, contact the Enterprise Service Desk (ESD) or create a ticket through ServiceNow (SNOW)/YourIT service portal and assign the ticket to the Scheduling Support assignment group.

#### Enhanced Error Messages

The error message logic and verbiage have been updated to provide more information for users on the issue and potential resolution and to provide a link to a knowledge base article for further troubleshooting steps.
There are three different versions of the error message depending on the error received. The verbiage for each message is consistent except for the service associated with the error, the error itself, and the proper group to address in a YourIT ticket.
Below are the three services that can be associated with these errors and an example of the message format:
- VSE-CS
- IAM Service
- Local IT
![](vse-for-clinical-staff-vsecs-user-guide/095.png)
<span id="_Toc168050524" class="anchor"></span>Figure 94: Enhanced Error Message.

#### Reset Button

The Help page now has a Reset Session button that will remove cached and stored data to help resolve errors.
![](vse-for-clinical-staff-vsecs-user-guide/096.png)
<span id="_Toc168050525" class="anchor"></span>Figure 95: Reset Session And Reload VSECS.

#### Pop-Up Message To Ensure Users Are Running Current Version

If a user is not running the most current version of VSE-CS they will see the below notice. After selecting “Ok” the page will be refreshed and updated to the most current version.
![](vse-for-clinical-staff-vsecs-user-guide/097.png)
<span id="_Toc168050526" class="anchor"></span>Figure 96: Pop-Up Message Informing Users They Are Not Running The Latest Version Of VSECS.

#### System Notifications To Users

Users can see notifications about VSECS as they are in the web application. There are two types of notifications a user can see: Show Once or Offline.

#### Show Once

The show once notification will be used to keep users informed of information about VSECS that should not stop them from using the application. The message will display as below, and the user can select OK to continue using VSECS as normal. The message will only show once unless a user clears their local cache. In this case, it will show again.
![](vse-for-clinical-staff-vsecs-user-guide/098.png)
<span id="_Toc168050527" class="anchor"></span>Figure 97: Image Displaying An Example Of The Show Once Notification.

#### Offline

The offline notification will be used to inform users of a degradation or a different issue that has prompted VSECS to not be available. The offline notification is persistent and will not allow the user to click out of it. When the offline notification is showing, VSECS is not available to be used.
![](vse-for-clinical-staff-vsecs-user-guide/099.png)
<span id="_Toc168050528" class="anchor"></span>Figure 98: Image Displaying An Example Of The Offline Notification.

### Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Appendix A - Acronyms And Abbreviations

| Term  | Description                                                     |
|-------|-----------------------------------------------------------------|
| IAM   | Identity and Access Management                                  |
| PIV   | Personal Identity Verification                                  |
| SSOi  | Single Sign-On Internal                                         |
| VA    | Department of Veterans Affairs                                  |
| VHA   | Veterans Health Administration                                  |
| VistA | Veterans Health Information Systems and Technology Architecture |
| VS    | VistA Scheduling                                                |
| VSE   | VistA Scheduling Enhancements                                   |
| VSECS | VistA Scheduling Enhancements for Clinical Staff                |
