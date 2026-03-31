---
title: VistA Imaging System TeleReader User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: VistA Imaging System TeleReader
app_code: MAG
app_name: VistA Imaging System
section: CLI
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
  - span
  - telereader
  - class
  - table
  - study
  - contents
  - vista
  - read
  - imaging
  - figure
page_count: 0
word_count: 3338
section_count: 17
table_count: 10
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_TeleReader_User_Manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_TeleReader_User_Manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

---
title: |
  ![](vista-imaging-system-telereader-user-manual/001.png)

  VistA Imaging System

  TeleReader User Manual

  February 2019
---

System Design and Development

VistA Imaging

TeleReader User Manual  
VistA Imaging February 2019  
Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Office of Enterprise Development.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Office of Enterprise Development  

Internet: <span class="mark">REDACTED</span>  
VA intranet: <span class="mark">REDACTED</span>

Revision History

| Date     | Description           | Author                                 |
|----------|-----------------------|----------------------------------------|
| Feb 2019 | Documentation Release | HPS Clinical Sustainment, Imaging Team |

<span id="_Toc535233214" class="anchor"></span>Table 1: List of Acronyms

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [Conventions](#conventions)
  - [Acronyms](#acronyms)
  - [Related Information](#related-information)
  - [<span class="mark">REDACTED</span>](#span-classmarkredactedspan)
  - [Getting Help](#getting-help)
- [Getting Started](#getting-started)
  - [Starting Work with TeleReader](#starting-work-with-telereader)
  - [Specialties Option Dialog](#specialties-option-dialog)
  - [Selection of Studies](#selection-of-studies)
  - [Study Details](#study-details)
  - [TeleReader Menus](#telereader-menus)
  - [Read List Days](#read-list-days)
  - [Remote Connections Status Bar](#remote-connections-status-bar)
  - [Unread List](#unread-list)
  - [Read List](#read-list)
- [Clinical Context Object Workgroup](#clinical-context-object-workgroup)
  - [CCOW Overview](#ccow-overview)
The TeleReader application provides a work list for local or remote imaging studies that are waiting to be read and interpreted by a qualified provider. The provider starts the TeleReader application, selects a study off the Unread List, and then is automatically directed to CPRS/Imaging to view the examination images and perform a diagnosis. Multiple users can display the Unread List, but only one user may lock/work on a single study at a time.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In compliance with Food and Drug Administration (FDA) and VA policies, authorization to use this software is contingent on the execution of a Site Agreement between the VistA Imaging Product Development group and the site where this software is installed.

In addition to any restrictions noted in the Site Agreement, the following restrictions apply.

| ![](vista-imaging-system-telereader-user-manual/002.png) | Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.                                                                                              |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-imaging-system-telereader-user-manual/003.png) | The FDA classifies VistA Imaging as a medical device. Unauthorized Modifications to VistA Imaging, including the TeleReader software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).                             |
| ![](vista-imaging-system-telereader-user-manual/004.png) | TeleReader is not intended for the primary interpretation of radiology exams or EKG waveforms. When TeleReader is installed on approved and properly maintained systems, primary interpretation of other image types is permissible by licensed practitioners at their discretion. |

<span id="_Toc526150526" class="anchor"></span>Table 2: Details Section Explanation

## Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses the following conventions:

- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate menu choices. For example: “Select File \| Open” means: “Click the File menu, and then select the Open option.”
- Keyboard key names are shown in bold and in brackets.
- When this document is used online, hyperlinks are indicated by blue text.
- Useful or supplementary information is shown in a Tip.
- Important or required information is shown in a Note.
- Critical information is indicated by: ![](vista-imaging-system-telereader-user-manual/005.png)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term   | Definition                                          |
|--------|-----------------------------------------------------|
| Acq    | acquisition                                         |
| CCOW   | Clinical Context Object Workgroup                   |
| Con \# | consult number                                      |
| CPRS   | Computerized Patient Record System                  |
| EKG    | Electrocardiograph                                  |
| FAQ    | Frequently Asked Questions                          |
| FDA    | Food and Drug Administration                        |
| HIPAA  | Health Insurance Portability and Accountability Act |
| HPS    | Health Product Support                              |
| ID     | Identification                                      |
| IFC    | Inter-Facility Consult                              |
| IRM    | Incident Response Message                           |
| QI     | Questionable Integrity                              |
| US     | United States of America                            |
| VA     | Department of Veteran Affairs                       |
<span id="_Toc526150527" class="anchor"></span>Table 3: File Menu Explanation

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For additional information about VistA Imaging TeleReader, see the following documents:

- Imaging System User Manual
- Imaging System Technical Manual
- Imaging System Installation Guide
- TeleReader Configurator User Guide

## <span class="mark">REDACTED</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Starting Work with TeleReader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user begins their work session, they should launch the TeleReader application first under Start \>\> VistA Imaging Programs\>\>VistA Imaging TeleReader.

CPRS and VistA Imaging Display will automatically be launched by the TeleReader application when the user selects a study from the worklist to view.

- CCOW will ensure all applications share the same patient context.
- Users may select the sites, specialties, and procedures they will be reading.

## Specialties Option Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Specialties Dialog allows the user to select specialties and procedures for reading. Only studies for the selected specialties and procedures will be listed. It also allows the user to decide what site they want to view studies from. See <u>Figure 1: Specialties Dialog</u>.

The dialog box shows the available acquisition sites in the left column, the specialties at those sites in the center column, and the procedures performed by those specialties in the right column. A check next to a procedure indicates studies will be listed from the site with the specialty that the procedure is in.

To quickly select or unselect all studies for a site, click on the checkbox next to the site. This will cause all specialties and all procedures to be selected for that site. If you do not want to see studies for all specialties and procedures in TeleReader, do not check the site checkbox.

To quickly select or unselect all procedures for a specialty, click on the checkbox next to the desired specialty. If you do not want to see studies for all procedures, then do not check the specialty checkbox. Instead check only the procedures that you would like on your Unread List.

A grayed-out checkbox indicates there is at least one associated specialty or procedure which is selected and at least one item which is not selected.

The Save button closes the Specialties dialog and saves your selected sites/specialty/procedures to VistA for future sessions.

The Close button closes the Specialties dialog and applies your changes for your current session but does not save your changes to VistA.

<span id="_Ref532459836" class="anchor"></span>Figure 1: Specialties Dialog

![](vista-imaging-system-telereader-user-manual/006.png)

If you do not have any specialties assigned you will receive a warning message. See <u>Figure 2: Specialties Warning Message</u>. Only approved and configured users may use TeleReader. You must be approved and TeleReader must be configured for you before you can Read studies. Users can see the images.

<span id="_Ref532459701" class="anchor"></span>Figure 2: Specialties Warning Message

![](vista-imaging-system-telereader-user-manual/007.png)

## Selection of Studies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main TeleReader window contains the remote connections status bar, the read and unread list of studies, details about studies, and a status bar. See <u>Figure 3: Section of Studies Menu</u>.

A study highlighted in:

- Red indicates the Urgency of that item is STAT and should be resulted quickly.
- Blue indicates that item has been *locked* by the current user.
- Black indicates that items *are unlocked* and can be resulted by the current user.
- Gray indicates items which the current user *cannot result* (either the item is locked *or* the current user is not logged into the reading site for that item) or the study is in a waiting status (for IFC consults) because the patient needs to be registered at the receiving facility.

When the user selects a study in the Read or Unread list, the details of that study are displayed at the bottom of the TeleReader. Studies in an “Unread” status can be locked by clicking on the Lock button. Clicking the Lock button causes the status of the study to change to “Locked” and the patient context for desktop applications to change to the selected patient. The study can then be read and resulted by viewing associated images in TeleReader and entering the result in CPRS. When resulted, studies move from the Unread List to the Read list.

The user can highlight any study in the Read or Unread list and then click the View button to view the images and information in the study using TeleReader and CPRS.

<span id="_Toc519857408" class="anchor"></span>Figure 3: Section of Studies Menu

![](vista-imaging-system-telereader-user-manual/008.png)

## Study Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the bottom of the TeleReader is a details section which contains more information about the selected study. If no study is selected, then no information will be displayed. See <u>Figure 4: Study Details Menu.</u>

<table>
<caption><p><span id="_Toc526150528" class="anchor"></span>Table 4: Options Menu Explanation</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient</td>
<td>The name of the patient for the study.</td>
</tr>
<tr class="even">
<td>Short ID</td>
<td>The short ID of patient (Patient’s last name and last four digits of SSN).</td>
</tr>
<tr class="odd">
<td>Reader</td>
<td>The reader who has locked the study (if the study is not locked then this field is empty.</td>
</tr>
<tr class="even">
<td>Acquisition Site</td>
<td>The site where the images were acquired.</td>
</tr>
<tr class="odd">
<td>Reading Site</td>
<td>The reading site to result the study.</td>
</tr>
<tr class="even">
<td>Consult Number</td>
<td>The consult number from the acquisition site.</td>
</tr>
<tr class="odd">
<td>IFC Number</td>
<td>The Inter-Facility consult number (if the consult is an inter-facility consult).</td>
</tr>
<tr class="even">
<td>Specialty</td>
<td>The specialty.</td>
</tr>
<tr class="odd">
<td>Procedure</td>
<td>The procedure.</td>
</tr>
<tr class="even">
<td>Status</td>
<td><p>The <em>status</em> of the study (Waiting, Unread, Locked, Read, Cancelled):</p>
<p><strong>Waiting</strong> means the consult has been sent by the acquisition site, but a response has not been received from the reading site.</p>
<p><strong>Unread</strong> means the study has not been resulted and no other user is in the process of resulting it.</p>
<p><strong>Locked</strong> indicates the study is in the process of being resulted by a user.</p>
<p><strong>Read</strong> means the study has been resulted.</p>
<p><strong>Cancelled</strong> indicates the study has been cancelled.</p></td>
</tr>
<tr class="odd">
<td>Urgency</td>
<td>The urgency of the study.</td>
</tr>
<tr class="even">
<td>Acquisition Start Time</td>
<td>The time when the acquisition of images began.</td>
</tr>
<tr class="odd">
<td>Last Image Acquired Time</td>
<td>The time when the last image was acquired.</td>
</tr>
<tr class="even">
<td>Number of Images</td>
<td>The number of images captured for this study.</td>
</tr>
</tbody>
</table>

<span id="_Toc526150528" class="anchor"></span>Table 4: Options Menu Explanation

To the right of the Study details are the Lock/Unlock button and the View button. The Lock/Unlock button will change based on the status of the study as details below:

- If the selected study is locked by the current user, the title of Lock/Unlock button will display as Unlock.
- If the selected study is locked by another user or is not available for reading by the current user, the Lock/Unlock button will be grayed out or inaccessible
- If the selected study can be locked and has status “Unread” then the title of Lock/Unlock button will display as Lock.

> Clicking the View button allows the user to view the patient information (set Patient Context) without locking the study.

<span id="_Toc519857409" class="anchor"></span>Figure 4: Study Details Menu

![](vista-imaging-system-telereader-user-manual/009.png)

If the selected item is for a patient who is not the patient in context, the following message will appear, ‘This is not the patient in context’. This message indicates to the user that if Display and/or CPRS are active, they could be displaying information about one patient while the details at the bottom of the TeleReader are for another patient (out of context). To put Display and CPRS into sync with TeleReader, select the study you wish to view and press the Lock or View button. See <u>Figure 5: Synchronizing Display and CPRS with TeleReader</u>.

<span id="_Ref532461805" class="anchor"></span>Figure 5: Synchronizing Display and CPRS with TeleReader

![](vista-imaging-system-telereader-user-manual/010.png)

## TeleReader Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TeleReader contains the following menus:

- File Menu (<u>Figure 6: File Menu</u>)
- Options Menu (<u>Figure 7: Options Menu</u>)
- Study Menu (<u>Figure 8: Study Menu</u>)
- Sort Column Menu (<u>Figure 9: Sort Column Menu</u>)
- Help Menu (<u>Figure 10: Help Menu</u>)

<span id="_Toc519857410" class="anchor"></span>Figure 6: File Menu

![](vista-imaging-system-telereader-user-manual/011.png)

| Title        | Description                                            |
|--------------|--------------------------------------------------------|
| Specialties  | Displays the Specialties dialog.                       |
| Refresh      | Refreshes the studies on the Read/Unread lists.        |
| Login        | Permits the user to login to their local VistA system. |
| Logout       | Permits the user to logout from VistA.                 |
| Remote Login | Enables the user to remotely login to a VistA server   |
| Exit         | Enables the user to exit the TeleReader application.   |

<span id="_Toc526150529" class="anchor"></span>Table 5: Study Menu Explanation

<span id="_Toc519857411" class="anchor"></span>

Figure 7: Options Menu

![](vista-imaging-system-telereader-user-manual/012.png)

<table>
<caption><p><span id="_Toc526150530" class="anchor"></span>Table 6: Sort Column Menu Explanation</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>View All Studies</td>
<td>When this option is checked, the TeleReader will display all studies available to the user. Not all studies may be able to be resulted by the user. If this option is not checked, then the TeleReader only displays the studies available for resulting by the user.</td>
</tr>
<tr class="even">
<td>Show Specialties Dialog at Startup</td>
<td><p>When this option is checked, the TeleReader will display the Specialties dialog when the user first logs into VistA. If this option is unchecked, the Specialties dialog will not appear if the user has at least one procedure active in VistA. If no procedures are stored in VistA, the Specialties dialog will appear.</p>
<p>This option is meant to allow users, who work with the same studies often, to not have to view the Specialties configuration dialog each time they login into TeleReader.</p></td>
</tr>
<tr class="odd">
<td>Auto Launch Display\CPRS</td>
<td>When this option is checked, the TeleReader will check to see if Display and CPRS are active. If either application is inactive, it will be launched and connected to the same database as the TeleReader. This option is checked by default.</td>
</tr>
<tr class="even">
<td>Read List Days</td>
<td>Allows the user to specify the number of days shown on the Read List. This value is not stored as a user preference and only remains in use if the TeleReader application remains open. (Read List Days will default to 7 days)</td>
</tr>
<tr class="odd">
<td>Save Settings Now</td>
<td>This feature will save the current user preference settings to VistA.</td>
</tr>
<tr class="even">
<td>Save Settings on Exit</td>
<td>This feature will save user preference settings to VistA when TeleReader closes or is disconnected from the current VistA system.</td>
</tr>
<tr class="odd">
<td>Fit Columns to Text</td>
<td>Adjusts the column widths on both the Read and Unread lists to ensure all text is visible.</td>
</tr>
<tr class="even">
<td>Fit Columns to Windows</td>
<td>Adjusts the column widths on both the Read and Unread lists to ensure all columns are visible in the window.</td>
</tr>
</tbody>
</table>

<span id="_Toc526150530" class="anchor"></span>Table 6: Sort Column Menu Explanation

<span id="_Toc519857412" class="anchor"></span>Figure 8: Study Menu

![](vista-imaging-system-telereader-user-manual/013.png)

| Title | Description                       |
|-------|-----------------------------------|
| Lock  | Lock or unlock the current study. |
| View  | View the current study.           |

<span id="_Toc526150531" class="anchor"></span>Table 7: Help Menu Explanation

<span id="_Toc519857413" class="anchor"></span>Figure 9: Sort Column Menu

![](vista-imaging-system-telereader-user-manual/014.png)

| Title         | Description                                                                     |
|---------------|---------------------------------------------------------------------------------|
| Status        | Sort the selected list by the status.                                           |
| Urgency       | Sort the selected list by the urgency.                                          |
| Reader        | Sort the selected list by the reader.                                           |
| Acq Site      | Sort the selected list by the acquisition site.                                 |
| Reading Site  | Sort the selected list by the reading site.                                     |
| Acq Con#      | Sort the selected list by the acquisition consult number.                       |
| IFC \#        | Sort the selected list by the inter-facility consult number.                    |
| Patient       | Sort the selected list by the patient.                                          |
| Last Image    | Sort the selected list by the last image acquired date.                         |
| \# Images     | Sort the selected list by the number of images.                                 |
| Complete Date | Sort the selected list by the completed date (only available on the Read List). |

<span id="_Toc526150532" class="anchor"></span>Table 8: Unread List Explanation

<span id="_Toc519857414" class="anchor"></span>Figure 10: Help Menu

![](vista-imaging-system-telereader-user-manual/015.png)

| Title                  | Description                                                                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TeleReader User Manual | This is a link to the current TeleReader User Manual installed with the TeleReader application. When selected, the User Manual will be opened in your browser. |
| About                  | This feature displays the About dialog containing information about this application.                                                                          |

<span id="_Toc526150533" class="anchor"></span>Table 9: Read List Explanation

## Read List Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, the Read list shows the last 7 days of studies. This number can be modified by using the Read List Days dialog. This dialog allows the user to specify the number of days on the Read list (0 days to 90 days). This value is not stored in VistA, and only applies during the current session. When the TeleReader is closed, this value will default back to 7 days. See <u>Figure 11: Read List Days Dialogue</u>.

The OK button closes the dialog, applies your new value and refreshes the Read list with the appropriate studies based on the selected value. The Cancel button closes the dialog without making any changes.

<span id="_Ref532462314" class="anchor"></span>Figure 11: Read List Days Dialogue

![](vista-imaging-system-telereader-user-manual/016.png)

## Remote Connections Status Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Connections Status Bar displays the status of all remote acquisition sites selected for reading using the Specialties Dialog. If the local site is a reading site, it will NOT appear in this status bar. Sites which are connected appear in green, while disconnected sites appear in red with a line through the site name.

If a site is disconnected, you can attempt to manually connect to it by clicking on the site name. Also, if there are one or more disconnected sites, a “Connect All” button will be available. If you click on that button, the TeleReader will attempt to connect all disconnected sites. A site might not connect if there is a network problem preventing communications with the site. See <u>Figure 12: Remote Connections Status Bar Menu.</u>

<span id="_Ref532462375" class="anchor"></span>Figure 12: Remote Connections Status Bar Menu

![](vista-imaging-system-telereader-user-manual/017.png)

## Unread List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unread List contains studies which have not been resulted. The Unread List contains the following columns. See <u>Figure 13: Unread List Column</u>.

<span id="_Toc519857416" class="anchor"></span>Figure 13: Unread List Column

![](vista-imaging-system-telereader-user-manual/018.png)

| Title        | Description                                                       |
|--------------|-------------------------------------------------------------------|
| Status       | The status of the study (Waiting, Unread, Locked, Read).          |
| Urgency      | The urgency of the study.                                         |
| Reader       | The initials of the reader (or blank if study is not being read). |
| Acq Site     | The acquisition site 3 letter abbreviation.                       |
| Reading Site | The reading site 3 letter abbreviation.                           |
| Acq Con \#   | The acquisition site's consult number.                            |
| IFC \#       | The inter-facility consult number.                                |
| Patient      | The name of the patient.                                          |
| Last Image   | The date the last image was captured for the study.               |
| \# Images    | The number of images captured for this study.                     |

<span id="_Toc535233223" class="anchor"></span>Table 10: Status Bar Explanation

## Read List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Read List contains studies which have been resulted or cancelled. This list contains studies for the last seven days. This value is the default, but can be changed to view days that exceed seven days. Users can use the View button to select the study on the Read List and view the study information and images. The Read List contains the following columns. See <u>Figure 14: Read List Days Column.</u>

<span id="_Ref532462478" class="anchor"></span>Figure 14: Read List Days Column

![](vista-imaging-system-telereader-user-manual/019.png)

| Title          | Description                                                       |
|----------------|-------------------------------------------------------------------|
| Status         | The status of the study (Waiting, Unread, Locked, Read).          |
| Urgency        | The urgency of the study.                                         |
| Reader         | The initials of the reader (or blank if study is not being read). |
| Acq Site       | The acquisition site 3 letter abbreviation.                       |
| Reading Site   | The reading site 3 letter abbreviation.                           |
| Acq Con \#     | The acquisition site's consult number.                            |
| IFC \#         | The inter-facility consult number.                                |
| Patient        | The name of the patient.                                          |
| Last Image     | The date the last image was captured for the study.               |
| \# Images      | The number of images captured for this study.                     |
| Completed Date | The date of completion.                                           |

Read List Days Menu ExplanationProvides the title and description of the Read List Days Menu Options

The Status Bar at the bottom of the TeleReader contains a button to view the message history, the three-letter abbreviation of the local site, and any importance messages about the status of the client. These messages include the status of the TeleReader and errors that have occurred in the TeleReader. Error messages should be reported to the Local Imaging Coordinator or support staff. See <u>Figure 15: Status Bar Menu</u>.

<span id="_Toc519857418" class="anchor"></span>Figure 15: Status Bar Menu

![](vista-imaging-system-telereader-user-manual/020.png)

| Title             | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| Message History   | The message history will display when selected.                   |
| Site Abbreviation | The three-letter site abbreviation.                               |
| Important Message | The current important message about the status of the TeleReader. |

Provides the title and description of the Status Bar menu options

# Clinical Context Object Workgroup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CCOW Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Context Object Workgroup (CCOW) is an HL7 standard for clinical context management which synchronizes applications so that they are mutually aware of common elements. TeleReader workstation is CCOW compliant and uses this standard to interface with CPRS, VistA Imaging TeleReader and other CCOW compliant applications.

When a clinician uses a CCOW compliant application (such as TeleReader) and starts another CCOW compliant application (such as CPRS) the second application will automatically sign on with the same user credentials. When the clinician views a study in TeleReader, it is automatically directed to CPRS and Clinical Display. CCOW will ensure all applications share the same patient context.