---
title: WII Version 1.1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: WII
app_name: Wounded Ill and Injured Warriors
section: FIN
app_status: active
pkg_ns: WII
patch_ver: 1.1
patch_id: WII*1.1
group_key: "WII:WII:1.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - even
  - table
  - active
  - facility
  - contents
  - entry
  - computer
  - dfas
  - duty
page_count: 0
word_count: 9133
section_count: 8
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Wounded_Injured_and_Ill_Warriors/wii_1_1_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Wounded_Injured_and_Ill_Warriors/wii_1_1_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=178"
---

![](wii-version-1-1-user-manual/001.png)

Line of Action (LOA) \#8Pay ManagementInterim SolutionWII USER MANUALVersion 1.1February 2009Department of Veterans AffairsOffice of Enterprise Development

Intentionally Blank

Revision History

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Page Number</td>
<td>Description</td>
</tr>
<tr class="even">
<td>August 2008</td>
<td>Initial Version</td>
<td></td>
<td>Document created.</td>
</tr>
<tr class="odd">
<td>September 26, 2008</td>
<td>Version 0.1</td>
<td></td>
<td>Overall edits</td>
</tr>
<tr class="even">
<td>December 18,2008</td>
<td>Version 0.2</td>
<td></td>
<td>Added screen shots from Training Manual</td>
</tr>
<tr class="odd">
<td rowspan="2">January 15, 2009</td>
<td rowspan="2">Version 0.3</td>
<td>1, 2</td>
<td><p>Deleted reference to REDACTED, used - central collecting</p>
<p>facility</p>
<p>facility</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>Replaced Figure 1 with similar figure used in BRD and Training Manual</td>
</tr>
<tr class="odd">
<td>January 21, 2009</td>
<td>1.0</td>
<td></td>
<td>LOA#* Pay Management WII User Manual January 2009</td>
</tr>
<tr class="even">
<td>January 29, 2009</td>
<td>1.1</td>
<td></td>
<td>Added 508 compliant metadata tags</td>
</tr>
</tbody>
</table>

Intentionally Blank

TABLE OF CONTENTS

1\. Introduction 1

1.1 Overview 1

1.2 Description of Process 2

1.3 Registration 5

1.3.1 Primary and Other Eligibility Code 5

1.3.2 Period of Service 5

1.4 Privacy and Release of Protected Information 5

2\. Operations 7

2.1 Option: \[WII Review ADT Events\] Review ADT Events 7

2.1.1 AP Approve Records 9

2.1.2 PL Print List 9

2.1.3 RM Remove Entry 9

2.1.4 EX Expand Eligibility 10

2.1.5 RV DFAS Approved Pending 12

2.1.6 AE Add Adm/Dischg to List 13

2.1.7 XX Deleted ADT Events 14

2.2 Completion Step 14

2.3 Instructions for Printing Activie Duty Admits/Discharges 15

3\. Glossary 16

TABLE OF FIGURES

Figure 1 Workflow Processes For VA Facility, Central Collection Facility

and DFAS 4

TABLE OF EXHIBITS

Exhibit 1 Active Duty Service Member – Admission/Discharge Pending Action List 8

Exhibit 2 Example of Selection of Remove Entry Of A Record 10

Exhibit 3 Example of the ADSM Pending Action List Screen Shot After Name

Removed 10

Exhibit 4 Expand Eligibility Screen Shot 11

Exhibit 5 Screen Shot Of Entries Flagged For Approval To Forwarding To DFAS 12

Exhibit 6 Screen Shot Of New Entry To The Pending Action List 13

Exhibit 7 Screen Shot Of Events Flagged Not To Transmit 14

Exhibit 8 Screen Shot Of Terminal Emulator For Print Functions 15

Intentionally Blank

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Description of Process](#description-of-process)
  - [Registration](#registration)
    - [Primary and Other Eligibility Code](#primary-and-other-eligibility-code)
    - [Period of Service](#period-of-service)
  - [Privacy and release of protected information](#privacy-and-release-of-protected-information)
- [Operations](#operations)
  - [Option: \[WII Review ADT Events\] Review ADT Events](#option-wii-review-adt-events-review-adt-events)
    - [AP Approve Record](#ap-approve-record)
    - [PL Print List](#pl-print-list)
    - [RM Remove Entry](#rm-remove-entry)
    - [EX Expand Eligibility](#ex-expand-eligibility)
    - [RV DFAS Approved Pending](#rv-dfas-approved-pending)
    - [AE Add Adm/Dischg to list](#ae-add-admdischg-to-list)
    - [XX Deleted ADT Events](#xx-deleted-adt-events)
  - [Completion Step](#completion-step)
  - [Instructions for printing active duty admits/discharges](#instructions-for-printing-active-duty-admitsdischarges)
- [Glossary](#glossary)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is in response to the action item developed by the Wounded, Ill, and Injured Senior Oversight Committee, Support and Care for the Wounded - Task Force, under Line of Action (LOA) \#8 Pay Management, to develop a tool to provide accurate and timely personnel and health related data to the Defense Finance and Accounting Service (DFAS) supporting adequate maintenance of pay and entitlements for all wounded warriors. This document specifies the user's guide for an interim process to satisfy this requirement. It is envisioned that a future solution will be fully automated.

Currently, the Department of Defense’s (DoD) Wounded Warrior Pay Management Program (WWPMP) has identified pay issues for Active Duty Service Members who are admitted to non military medical treatment facilities due to combat-related injuries. Veterans Health Administration (VHA) often provides inpatient and outpatient health care services to Active Duty Service members. The Department of Defense/Defense Finance and Accounting Service (DoD/DFAS) has experienced difficulty in keeping accountability for this population and the lack of accurate accountability may adversely impact the pay of Service Members.

In the fall 2007, through a collaborative effort between Veterans Administration, VHA and DoD/DFAS, Veterans Affairs (VA) and VHA agreed to provide defined data elements to DFAS to facilitate tracking of Active Duty Service Members admitted to inpatient VA facilities. In February 2008 a Memorandum of Understanding (MOU) by and between VA and VHA and DoD/DFAS was executed. The MOU established the authorities and agreement for the exchange of information relating to admission to and discharge from inpatient VA health care facilities of Active Duty personnel.

Two (2) solutions were conceived during the conceptualization of how these requirements can be met. The first is the Interim solution, which can be put into service in a short period of time, but has the drawback of being more labor intensive, is the focus of this User Guide. The second solution, named the Future solution will eliminate all manual processes, sending the records to a central server which will collect and transmit them automatically to the DFAS on a periodic basis. The Future solution will not be started until the Interim Solution is implemented and analyzed.

The Interim Solution will be based on a weekly collection process at each VA inpatient facility, where Active Duty Service Members are admitted and discharged. For each VA inpatient facility, a list of Active Duty Service Members admitted to and discharged from that facility will be transmitted by secure email to a central collection facility in REDACTED, Oregon. Each facility’s transmission is collected into one list by designated VA personnel specifically trained to perform this function. The complete list of all Active Duty Service Members admitted to inpatient VA facilities is then transmitted to the DFAS via an encrypted email to a secure DFAS mailbox. The report will include the first name, middle name or initial, last name, social security number, admission date and time or discharge date and time and the facility identification number. The exact format can be found in the Technical Documentation.

It is assumed that the Interim Solution will be accomplished as follows:

A patch delivered to the Vista ADT software.

Training of designated VA personnel at each facility

A several week testing period.

## Description of Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Breakdown of tasks

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th>At the inpatient VA facility</th>
<th><p>1. Site will appoint a point of contact (POC) to manage the data, electronic files and emails, and submit the POC’s name and contact information to the HEC.</p>
<p>2. The facility POC will run a background job once a week. This job will collect data based on admissions and discharges that occurred during the collection period for patients with a primary or other eligibility of TRICARE, SHARING AGREEMENT or OTHER FEDERAL AGENCY. The qualifying entries are stored at the local facility in a Fileman file.</p>
<p>3. When the background job is completed, VistA will send a VistA email message to a local facility mail group (G.WII ADT REVIEWER) alerting members that the facility has entries requiring review and disposition, or no entries requiring action. Note: In the event that no entries are collected, the members of the mail group will still receive a bulletin alerting them that the background job ran and collected zero records.</p>
<p>4. The local POC will review and edit the data via the WII REVIEW ADT EVENTS menu option, adding or modifying active duty service members (SM) records, or deleting records of patients who are not active duty SM, as needed.</p>
<p>a. VA staff may need to investigate whether those on the list are active duty SM, or if there are known active duty admissions or discharges not included on the list. This may mean visiting wards and questioning a patient or representative, or contacting the patient after discharge to ascertain the status. Any admission from a military hospital or from overseas should be reviewed.</p>
<p>b. If the list is missing an entry the POC has the ability to add it to the record. Adding a record to the local facility list will bypass the eligibility requirements, therefore, the POC should add a record only when there is evidence to believe the background job missed it.</p>
<p>5. Once the POC assures that all of the entries are for active duty inpatient transactions and approves the entries at the local facility, the POC will release the list for transmission to the central collection facility.</p>
<p>6. The POC will list all SM names sent to DFAS on the disclosure spreadsheet and forward the completed spreadsheet to the site’s privacy officer.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>At the central collection facility</td>
<td><p>1. The receiving mail server will automatically unload the data from each facility and store the data in a single Fileman file.</p>
<p>2. A POC at the central collection facility site will use a Delphi tool to extract the data from the repository and place the data a newly created text (.txt) file.</p>
<p>3. The POC will send an Outlook message with the .txt file containing the data attached, and will send the comprehensive data to DFAS via secure email. Once the data has been sent to DFAS, those entries will be marked with a status of sent to DFAS and the date in which the files were sent. The list going to DFAS will only contain the data elements authorized by the MOU and that are requested by the coordinator in charge of this operation.</p></td>
</tr>
<tr class="even">
<td>At DFAS</td>
<td><p>1. DFAS will receive the secure email at the appropriate mail server.</p>
<p>2. DFAS will review the data and make the appropriate change status of active duty Service Members as defined in transmitted data.</p></td>
</tr>
</tbody>
</table>

Figure 1 illustrates the workflow diagram illustrates each of the listed steps.

![Figure 1. Workflow processes for VA Facility, Central Collecting Facility and DFAS](wii-version-1-1-user-manual/002.png)

*Figure 1. Workflow processes for VA Facility, Central Collecting Facility and DFAS*

## Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Registration and intake personnel at each VA health care facility will need to complete each of the required data fields during the admission or discharge transaction using Admission, Discharge Transfer (ADT) application. Accurate data entry at this time will allow VistA to run reports necessary for staff to use in determining which records need to transfer to DFAS for processing.

At the time of admission, VA staff should expect patients, or their representative, to identify themselves as active duty service members (SM), although there may be instances where this may not occur. Staff may need to ask upon admission or discharge process if the patient is active duty. Transfers from military hospitals and from overseas will most likely be active duty personnel. Whenever in doubt, ask.

Staff will enter information for the following data elements to determine the active duty status of the patient:

### Primary and Other Eligibility Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Type of Admission, select for Field Movement Type:

1 – DIRECT ADMISSION ACTIVE 2 – OPT-NSC ADMISSION ACTIVE

3 – OPT-SC ADMISSION ACTIVE 4 – A/C ADMISSION ACTIVE

5 – TRANSFERS IN ADMISSION ACTIVE 6 – NON-VETERAN ADMISSION ACTIVE

7 – WAITING LIST ADMISSION ACTIVE 8 – PBC ADMISSION ACTIVE

#### Source of Admission, the four below indicate active duty:

2B - MILITARY PERS NOT DIRECTLY FROM MILT HOSP HOSPITAL

2C - MILITARY PERS BY TRANSFER FROM A MILT HOSP HOSPITAL

4M - FROM MILITARY HOSP DOMICILIARY

7B - DIRECT ADM OF ACTIVE DUTY PERS FROM MILT HOSP CNH

### Period of Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Privacy and release of protected information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the release of information to DFAS is considered a disclosure under the HIPAA Privacy Rule, VHA must account for the release in its records. Before actually sending the information to the central collection site, the POC needs to capture the following information about individuals whose information is sent to DFAS:

Patient Name

Date of Disclosure

Description of Information disclosed

Purpose of Disclosure/authority to disclose

Name and Address of Person or Organization to whom the information is disclosed

A spreadsheet has been developed to allow for easy recording of this information. Because the process is designed to capture the same information on all applicable individuals, under the same authority and release it to the same recipient, the POC need only fill in the names of the individuals whose information is being disclosed and the date of the disclosure. Other fields should just be the same for every individual. More rows can be added to the form as needed, but the shaded cells should read the same in each row. NOTE: the cell for purpose and copy of written request will be adjusted to reflect the number of the directive once it is finalized.

Once completed, the POC should send the form the site’s Release of Information Office or Privacy Officer. Table 1 below depicts the spreadsheet.

|                                                                                                             |                    |                                                   |                                   |                         |                                                                               |                                   |
|-------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------|-----------------------------------|-------------------------|-------------------------------------------------------------------------------|-----------------------------------|
| Manual Accounting of Disclosures Spreadsheet                                                                |                    |                                                   |                                   |                         |                                                                               |                                   |
| WII Active Duty Admission/Discharge                                                                         |                    |                                                   |                                   |                         |                                                                               |                                   |
| \*\*\*\*\*FOR USE ONLY WITH THE DISCLOSURE OF ACTIVE DUTY ADMISSION DISCHARGE INFORMATION TO DFAS\*\*\*\*\* |                    |                                                   |                                   |                         |                                                                               |                                   |
|                                                                                                             |                    |                                                   |                                   |                         |                                                                               |                                   |
| Active Duty Patient Name                                                                                    | Date of Disclosure | Description of Information Disclosed              | Purpose of Disclosure             | Copy of Written Request | Name of Person or Organization                                                | Address of Person or Organization |
|                                                                                                             |                    | Name, SSN, Admission/ Discharge Date, Facility ID | Compliance with Directive 2008-XX | Directive 2008-XX       | DoD Wounded Warrior Pay Management Program/Defense Finance Accounting Service | Department of Defense             |
|                                                                                                             |                    | Name, SSN, Admission/ Discharge Date, Facility ID | Compliance with Directive 2008-XX | Directive 2008-XX       | DoD Wounded Warrior Pay Management Program/Defense Finance Accounting Service | Department of Defense             |

Table 1. Manual Accounting of Disclosures Spreadsheet

# Operations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interim solution involves the collection of local admissions and discharges from each facility and the consolidation of this data in a single repository for review and transmission to DFAS via a central data collection point.

Each facility POC will run a weekly background job that collects that week’s data based on admissions and discharges, for patients with a Primary or Other Eligibility of TRICARE, SHARING AGREEMENT or OTHER FEDERAL AGENCY. Upon completion of the background job, VistA will send an email message to the local WII ADT REVIEWER mail group alerting facility staff on whether there are entries requiring approval. The facility POC should ensure anyone needing to access this report or to the WII ADT EVENTS menu option is added as a member of the WII ADT REVIEWER mail group.

VistA will deliver the alerts via the users’ VA MailMan account. When the background job runs and finds no potential active duty admissions or discharges for the past week, staff will receive a message indicating there are no active duty admissions or discharges, a count of zero and the reporting period. VistA will send a different bulletin message when there are potential active duty admissions or discharges. This message will state that there are active duty admissions, reflect the number of potential active duty admissions or discharges needing review, the record count, and the time period of the report. Staff will now have to process those potential active duty cases. An appointed POC should have the WII Review ADT Events option added as a secondary menu option. Choose the WII REVIEW ADT EVENTS option and press \<Enter\>. The next screen will display the cases pending review. The following section describes reviewing these events.

## Option: \[WII Review ADT Events\] Review ADT Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REVIEW ADT EVENTS is a List Manager type option and utilizes the same functionality that is found in other VistA List Manager options. The initial screen displays the Pending Action List of Admission/Discharge events that are associated with active duty service members.

![Exhibit 1 Active Duty Service Member -- Admission/Discharges Pending Action List](wii-version-1-1-user-manual/003.png)

*Exhibit 1 Active Duty Service Member -- Admission/Discharges Pending Action List*

In addition to the pending cases to review, the option also offers various actions to aid staff in reconciling these cases. Additionally, the standard List Manager actions are available to navigate through the list.

The following actions are also available:

\+ Next Screen \< Shift View to Left PS Print Screen

\- Previous Screen FS First Screen PL Print List

UP Up a Line LS Last Screen SL Search List

DN Down a Line GO Go to Page ADPL Auto Display(On/Off)

\> Shift View to Right RD Re Display Screen Q Quit

The REVIEW ADT EVENTS has several specific user actions:

AP Approve Record EX Expand Eligibility XX Deleted ADT Events

PL Print List RV DFAS Approved Pending

RM Remove Entry AE Add Adm/Dischg to list

\*\* Note: The VA FAC field lists the entire station ID, whether the ID represents a parent station or multidivisional facility. Multidivisional sites should have a Point of Contact (POC) appointed for each division, with each POC reviewing and taking action for those cases listed for the POC’s site. So in the previous screenshot, there would only be one POC for VA FAC 402, but if it were a multidivisional facility, it might have been labeled 402AB, and in that case, there would be another POC for that division.

The WII Review ADT Events has several specific user actions that the facility POC can use to manage this data.

### AP Approve Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows for the selection of:

A single entry from the current displayed list

A range of entries from the current list i.e. (1-14)

Selected entries from the current list i.e. (3, 7, 11-14)

The selected entry(s) are flagged with a status of “approved” and removed from the current list.

### PL Print List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action prints a ‘^’delimited list of all entries from the current list for capture and importing into a spread

Select Action: Quit// PL Print List

NAME^SSN^ADMISSION DATE^DISCHARGE DATE^FACILITY \#

TEST,PATIENT A^000000001^04/21/2008@14:33^04/28/2008@14:14^402

TEST,PATIENT B^000000002^05/01/2008@13:08^05/02/2008@12:15^402

TEST,PATIENT C^000000003^05/02/2008@14:39^05/07/2008@15:00^402

Enter RETURN to continue or '^' to exit:

### RM Remove Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff may need to remove individuals who are clearly not active duty from the pending list. The POC can do this by entering RM Remove Entry at the Select Action: prompt, pressing \<Enter\> and entering the record number or numbers at the Select a number: prompt.

This action allows for the selection of:

A single entry from the current displayed list

A range of entries from the current list i.e. (1-14)

Selected entries from the current list i.e. (3, 7, 11-14)

The selected entries are flagged with a status of disapproved and removed from the current list.

![Exhibit 2 Example of selection of remove entry of a record](wii-version-1-1-user-manual/004.png)

*Exhibit 2 Example of selection of remove entry of a record*

![Exhibit 3 Example of the ADSM Pending Action List Screen Shot after name removed](wii-version-1-1-user-manual/005.png)

*Exhibit 3 Example of the ADSM Pending Action List Screen Shot after name removed*

### EX Expand Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows for the selection of a single entry on the current list, and opens a view of the eligibility information available for the person. Expand Eligibility provides basic patient information: the G and L date, movement type, primary eligibility, branch of service, and service entry and exit dates. Note this individual has no service exit date, which is an indicator that this patient may be active duty, but not definitive proof. If there is doubt, staff may need to inquire further.

![Exhibit 4 Expand Eligibility Screen Shot](wii-version-1-1-user-manual/006.png)

*Exhibit 4 Expand Eligibility Screen Shot*

### RV DFAS Approved Pending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will display list of all those entries that were flagged ‘approved’. It has the custom actions Expand Eligibility and Print List which function as described previously and an additional action of CS Roll Back Status to Pending that will move selected entries back to the Pending Action List.

![Exhibit 5 Screen Shot of Entries flagged for approval to forwarding to DFAS](wii-version-1-1-user-manual/007.png)

*Exhibit 5 Screen Shot of Entries flagged for approval to forwarding to DFAS*

### AE Add Adm/Dischg to list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows for the adding of an Admission/Discharge event that did not qualify the screening process to be automatically added to the list. The user is asked for an event date and can pick a new entry from a list of events for that date. The new entry appears on the list in “Patient Movement Number” order:

Select Action: Quit// AE Add Adm/Dischg to list

Select Admission/Discharge Date: MAY 02, 2008@09:00 MAY 02, 2008@09:00

1 5-2-2008@09:00:17 TEST,PATIENT D (000000004)

ADMISSION: DIRECT

2 5-2-2008@09:15:00 TEST,PATIENT Z (000000009)

DISCHARGE: OPT-SC

CHOOSE 1-2: 1 5-2-2008@09:00:17 TEST,PATIENT D (000000004)

ADMISSION: DIRECT

The list is updated with the new entry. This entry still will need the action Approve Record to be included with the entries forwarded through to DFAS.

![Exhibit 6 Screen Shot of new entry to the Pending Action List](wii-version-1-1-user-manual/008.png)

*Exhibit 6 Screen Shot of new entry to the Pending Action List*

### XX Deleted ADT Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will display the EVENTS FLAGGED NOT TO TRANSMIT list. This list is inclusive of ALL entries that have been flagged, not just this reporting cycle. It includes the Roll Back Status to Pending and Expand Eligibility actions previously described.

![Exhibit 7 Screen Shot of Events Flagged Not to Transmit](wii-version-1-1-user-manual/009.png)

*Exhibit 7 Screen Shot of Events Flagged Not to Transmit*

The “RV DFAS Approved Pending” and “XX Deleted ADT Events” list screens also have the action

CS Roll Back Status to Pending action. This action will roll back the event status to pending and place the on the pending action list for review.

## Completion Step

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the reviewer has completed reviewing events all entries that were flagged as approved will be transmitted to the VA central repository upon exiting the option. VistA will send the released list to the central collection facility via a secured VistA mail server.

The receiving mail server at the central collection facility automatically unloads the data from each facility and stores the consolidated data in a single Fileman file.

The authorized point of contact (POC) at the central collection facility has a Delphi tool to extract the data from the repository and copy it into an Outlook message, pasting the data into the message and sending the consolidated data to DFAS via PKI encryption.

The central collection facility POC will ensure those entries sent to DFAS are marked with a status of sent to DFAS and the date sent.

## Instructions for printing active duty admits/discharges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure the terminal emulator (Smarterm, KEA, or other software) is displaying the Pending Action List, or Admission/Discharges flagged Approval for forwarding to DFAS list, where you can use the PL Print List action item. From the terminal emulator menu, select Capture Incoming Data … from the Tools menu options. In this instance, Smarterm is the terminal emulator. KEA offers an identical process, but the screens looks slightly different.

Terminal emulator, Tools, Start Capture displays as:

![Exhibit 8 Screen shot of terminal emulator for print function](wii-version-1-1-user-manual/010.png)

*Exhibit 8 Screen shot of terminal emulator for print function*

The terminal emulator will display the Capture Incoming Data dialogue box. Select a location on the computer to save the file and type a file name in the File name: field. Click Save. The file will be in a text format.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>TERM</th>
<th>DEFINITION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ABBREVIATED RESPONSE</td>
<td>This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td>ACCESS CODE</td>
<td>A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. (See the term verify code in the Glossary.)</td>
</tr>
<tr class="odd">
<td>ADPAC</td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="even">
<td>APPLICATION COORDINATOR</td>
<td>Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</td>
</tr>
<tr class="odd">
<td>APPLICATION PACKAGE</td>
<td>In VistA, software and documentation that support the automation of a service, such as Laboratory or Pharmacy, within VA medical centers (see the term Package in the Glossary). The Kernel is like an operating system relative to other VistA applications.</td>
</tr>
<tr class="even">
<td>AUTO-MENU</td>
<td>An indication to Menu Manager that the current user’s menu items should be displayed automatically. When auto-menu is not in effect, the user must enter a question mark at the menu’s select prompt to see the list of menu items.</td>
</tr>
<tr class="odd">
<td>BEDSECTION</td>
<td>Also referred to as “Specialty” in this document. Specific services in a hospital have their own floors or rooms where patients can be admitted and monitored by that service. A patient is admitted to the hospital through a particular service, which has its own bedsection (i.e., SCI service has its own bedsection where care and treatment is administered to SCI patients).</td>
</tr>
<tr class="even">
<td>CARET</td>
<td>A symbol expressed as up caret (^), left caret (&lt;), or right caret (&gt;). In many M systems, a right caret is used as a system prompt and an up caret as an exiting tool from an option. Also known as the up-arrow symbol or shift–6 key.</td>
</tr>
<tr class="odd">
<td>COMMAND</td>
<td>A combination of characters that instruct the computer to perform a specific operation.</td>
</tr>
<tr class="even">
<td>COMMON MENU</td>
<td>Options that are available to all users. Entering two question marks at the menus select prompt s any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="odd">
<td>CONTROL KEY</td>
<td>The Control Key (Ctrl on the keyboard) performs a specific function in conjunction with another key. In word-processing, for example, holding down the Ctrl key and typing an A causes a new set of margins and tab settings to occur; Ctrl-S causes printing on the terminal screen to stop; Ctrl-Q restarts printing on the terminal screen; Ctrl-U deletes an entire line of data entry <u>before</u> the Return key is pressed.</td>
</tr>
<tr class="even">
<td>CROSS REFERENCE</td>
<td><p>An indexing method whereby files can include pre-sorted lists of entries as part of the stored database. Cross-references (x-refs) facilitate look-up and reporting.</p>
<p>A file may be cross-referenced to provide direct access to its entries in several ways. For example, VA FileMan allows the Patient file to be cross-referenced by name, social security number, and bed number. When VA FileMan asks for a patient, the user may then respond with the patient’s name, social security number, or his bed number. A cross-reference speeds up access to the file, both for looking up entries and for printing reports.</p>
<p>A cross-reference is also referred to as an index or cross-index.</p></td>
</tr>
<tr class="odd">
<td>CURSOR</td>
<td>A flashing image on your screen (generally a horizontal line or rectangle) that alerts you that the computer is waiting for you to make a response to an instruction (prompt).</td>
</tr>
<tr class="even">
<td>DATA</td>
<td>A representation of facts, concepts, or instructions in a formalized manner for communication, interpretation, or processing by humans or by automatic means. The information you enter for the computer to store and retrieve. Characters that are stored in the computer system as the values of local or global variables. VA FileMan fields hold data values for file entries.</td>
</tr>
<tr class="odd">
<td>DATA ATTRIBUTE</td>
<td>A characteristic of a unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="even">
<td>DATA DICTIONARY</td>
<td><p>The Data Dictionary is a global containing a description of what kind of data is stored in the global corresponding to a particular file. The data is used internally by FileMan for interpreting and processing files.</p>
<p>A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes); relationships to other files; and structure or design. Users generally review the definitions of a file’s elements or data attributes; programmers review the definitions of a file’s internal structure.</p></td>
</tr>
<tr class="odd">
<td>DATA DICTIONARY ACCESS</td>
<td>A user’s authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="even">
<td>DATA DICTIONARY LISTING</td>
<td>This is the printable report that shows the data dictionary. DDs are used by users and programmers.</td>
</tr>
<tr class="odd">
<td>DATA PROCESSING</td>
<td>Logical and arithmetic operations performed on data. These operations may be performed manually, mechanically, or electronically: sorting through a card file by hand would be an example of the first method; using a machine to obtain cards from a file would be an example of the second method; and using a computer to access a record in a file would be an example of the third method.</td>
</tr>
<tr class="even">
<td>DATABASE</td>
<td>A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file; a data collection has different data fields (e.g., patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="odd">
<td>DATABASE MANAGEMENT SYSTEM</td>
<td>A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="even">
<td>DATABASE, NATIONAL</td>
<td>A database, which contains data, collected or entered for all VHA sites.</td>
</tr>
<tr class="odd">
<td>DBA</td>
<td>Database Administrator, oversees package development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</td>
</tr>
<tr class="even">
<td>DBIA</td>
<td>Database Integration Agreement, a formal understanding between two or more VistA packages which describes how data is shared or how packages interact. The DBA maintains a list of DBIAs.</td>
</tr>
<tr class="odd">
<td>DBIC</td>
<td>Database Integration Committee. Within the purview of the DBA, the committee maintains a list of DBIC approved callable entry points and publishes the list on FORUM for reference by application programmers and verifiers.</td>
</tr>
<tr class="even">
<td>DEBUG</td>
<td>To correct logic errors or syntax errors or both types in a computer program. To remove errors from a program.</td>
</tr>
<tr class="odd">
<td>DEFAULT</td>
<td>A response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the enter (or return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="even">
<td>DELETE</td>
<td>The key on your keyboard (may also be called rubout or backspace on some terminals) which allows you to delete individual characters working backwards by placing the cursor immediately after the last character of the string of characters you wish to delete. The @ sign (uppercase of the 2 key) may also be used to delete a file entry or data attribute value. The computer asks “Are you sure you want to delete this entry?” to insure you do not delete an entry by mistake.</td>
</tr>
<tr class="odd">
<td>DELIMITER</td>
<td>A special character used to separate a field, record or string. VA FileMan uses the ^ character as the delimiter within strings.</td>
</tr>
<tr class="even">
<td>DEVICE</td>
<td>A peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="odd">
<td>DICTIONARY</td>
<td>A database of specifications of data and information processing resources. VA FileMan’s database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="even">
<td>DISK</td>
<td>The media used in a disk drive for storing data.</td>
</tr>
<tr class="odd">
<td>DISK DRIVE</td>
<td>A peripheral device that can be used to “read” and “write” on a hard or floppy disk.</td>
</tr>
<tr class="even">
<td>DOUBLE QUOTE (")</td>
<td>A symbol used in front of a Common option’s menu text or synonym to select it from the Common menu. For example, the five character string "TBOX" selects the User’s Toolbox Common option.</td>
</tr>
<tr class="odd">
<td>DSCC</td>
<td>Documentation Standards and Conventions Committee. Package documentation is reviewed in terms of standards set by this committee.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td>A local variable holding the user number that identifies the signed-on user.</td>
</tr>
<tr class="odd">
<td>DUZ(0)</td>
<td>A local variable that holds the File Manager Access Code of the signed-on user.</td>
</tr>
<tr class="even">
<td>ENCRYPTION</td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g., access/verify codes).</td>
</tr>
<tr class="odd">
<td>ENTER</td>
<td>Pressing the return or enter key tells the computer to execute your instruction or command or to store the information you just entered.</td>
</tr>
<tr class="even">
<td>ENTRY</td>
<td>A VA FileMan record. It is uniquely identified by an internal entry number (the .001 field) in a file.</td>
</tr>
<tr class="odd">
<td>EXPERT PANEL</td>
<td>Representative users from the field and Program Office who make recommendations for software development. The Expert Panels (EPs) report to and are formed by the ARGs.</td>
</tr>
<tr class="even">
<td>EXTRACTOR</td>
<td>A specialized routine designed to scan data files and copy or summarize data for use by another process.</td>
</tr>
<tr class="odd">
<td>FIELD</td>
<td>In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file’s data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</td>
</tr>
<tr class="even">
<td>FILE</td>
<td>A set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="odd">
<td>FILE MANAGER (VA FILEMAN)</td>
<td>The VistA’s Database Management System (DBMS). The central component of the Kernel that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="even">
<td>FOIA</td>
<td>The Freedom Of Information Act. Under the provisions of this public law, software developed within the VA is made available to other institutions, or the general public, at a nominal cost.</td>
</tr>
<tr class="odd">
<td>FORCED QUEUING</td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device rejects it and prompts the user to queue the task instead.</td>
</tr>
<tr class="even">
<td>FREE TEXT</td>
<td>The use of any combination of numbers, letters, and symbols when entering data.</td>
</tr>
<tr class="odd">
<td>GLOBAL VARIABLE</td>
<td>A variable that is stored on disk (M usage).</td>
</tr>
<tr class="even">
<td>GO-HOME JUMP</td>
<td>A menu jump that returns the user to the Primary menu presented at sign-on. It is specified by entering two up-arrows (^^) at the menu’s select prompt. It resembles the rubber band jump but without an option specification after the up-arrows.</td>
</tr>
<tr class="odd">
<td>HARDWARE</td>
<td>The physical equipment pieces that make up the computer system (e.g., terminals, disk drives, central processing units). The physical components of a computer system.</td>
</tr>
<tr class="even">
<td>HELP FRAMES</td>
<td>Entries in the HELP FRAME file that may be distributed with application packages to provide on-line documentation. Frames may be linked with other related frames to form a nested structure.</td>
</tr>
<tr class="odd">
<td>HELP PROMPT</td>
<td>The brief help that is available at the field level when entering one question mark.</td>
</tr>
<tr class="even">
<td>HINQ</td>
<td>Hospital INQuiry. A system that permits medical centers to query the Veterans Benefits Administration systems via the VADATS network.</td>
</tr>
<tr class="odd">
<td>HIS</td>
<td>Hospital Information Systems</td>
</tr>
<tr class="even">
<td>INPATIENT</td>
<td>A patient who has been admitted to a hospital in order to be treated for a particular condition.</td>
</tr>
<tr class="odd">
<td>KERNEL</td>
<td>A set of VistA software routines that function as an intermediary between the host operating system and the VistA application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.</td>
</tr>
<tr class="even">
<td>KEY</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td>KEYWORD</td>
<td>A word or phrase used to call up several codes from the reference files in the LOCAL LOOK-UP file. One specific code may be called up by several different keywords.</td>
</tr>
<tr class="even">
<td>LAYGO ACCESS</td>
<td>A user’s authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="odd">
<td>LINK</td>
<td>Non-specific term referring to ways in which files may be related (via pointer links). Files have links into other files.</td>
</tr>
<tr class="even">
<td>LOG IN/ON</td>
<td>The process of gaining access to a computer system.</td>
</tr>
<tr class="odd">
<td>LOG OUT/OFF</td>
<td>The process of exiting from a computer system.</td>
</tr>
<tr class="even">
<td>MAIL MESSAGE</td>
<td>An entry in the MESSAGE file. The VistA electronic mail system (MailMan) supports local and remote networking of messages.</td>
</tr>
<tr class="odd">
<td>MAILMAN</td>
<td>An electronic mail system that allows you to send and receive messages from other users via the computer.</td>
</tr>
<tr class="even">
<td>MENU</td>
<td>A list of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word “Select” and followed by the word “option” as in Select Menu Management option: (the menu’s select prompt).</td>
</tr>
<tr class="odd">
<td>MENU CYCLE</td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. Menu Manager keeps track of information, such as the user’s place in the menu trees, according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="even">
<td>MENU SYSTEM</td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td>MENU TEMPLATE</td>
<td>An association of options as pathway specifications to reach one or more final destination options. The final options must be executable activities and not merely menus for the template to function. Any user may define user-specific menu templates via the corresponding Common option.</td>
</tr>
<tr class="even">
<td>MENU TEXT</td>
<td>The descriptive words that appear when a list of option choices is ed. Specifically, the Menu Text field of the OPTION file. For example, User’s Toolbox is the menu text of the XUSERTOOLS option. The option’s synonym is TBOX.</td>
</tr>
<tr class="odd">
<td>NUMERIC FIELD</td>
<td>A response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="even">
<td>OPERATING SYSTEM</td>
<td>A basic program that runs on the computer, controls the peripherals, allocates computing time to each user, and communicates with terminals.</td>
</tr>
<tr class="odd">
<td>OPTION</td>
<td>An entry in the OPTION file. As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="even">
<td>OPTION NAME</td>
<td>The Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text “Menu Management”). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="odd">
<td>OUTPATIENT</td>
<td>A patient who comes to the hospital, clinic, or dispensary for diagnosis and/or treatment but does not occupy a bed.</td>
</tr>
<tr class="even">
<td>PACKAGE</td>
<td>The set of programs, files, documentation, help prompts, and installation procedures required for a given software application. For example, Laboratory, Pharmacy, and MAS are packages. A VistA software environment composed of elements specified via the Kernel’s Package file. Elements include files and associated templates, namespaced routines, and namespaced file entries from the Option, Key, Help Frame, Bulletin, and Function files. Packages are transported using VA FileMan’s DIFROM routine that creates initialization routines to bundle the files and records for export. Installing a package involves the execution of initialization routines that create the required software environment. Verified packages include documentation. As public domain software, verified packages may be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td>PASSWORD</td>
<td>A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user’s identity.</td>
</tr>
<tr class="even">
<td>PERIPHERAL DEVICE</td>
<td>Any hardware device other than the computer itself (central processing unit plus internal memory). Typical examples include card readers, printers, CRT units, and disk drives.</td>
</tr>
<tr class="odd">
<td>PHANTOM JUMP</td>
<td>Menu jumping in the background. Used by the menu system to check menu pathway restrictions.</td>
</tr>
<tr class="even">
<td>POINTER</td>
<td>A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward).</td>
</tr>
<tr class="odd">
<td>PRIMARY MENUS</td>
<td>The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by IRM. This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="even">
<td>PRINTER</td>
<td>A printing or hard copy terminal.</td>
</tr>
<tr class="odd">
<td>PRODUCTION ACCOUNT</td>
<td>The UCI where users log on and carry out their work, as opposed to the manager, or library, account.</td>
</tr>
<tr class="even">
<td>PROGRAM</td>
<td>A list of instructions written in a programming language and used for computer operations.</td>
</tr>
<tr class="odd">
<td>PROMPT</td>
<td>The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="even">
<td>QUEUING</td>
<td>Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). The Kernel’s Task Manager handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td>QUEUING REQUIRED</td>
<td>An option attribute that specifies that the option must be processed by TaskMan (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified time periods.</td>
</tr>
<tr class="even">
<td>READ ACCESS</td>
<td>A user’s authorization to read information stored in a computer file.</td>
</tr>
<tr class="odd">
<td>RECORD</td>
<td>A set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="even">
<td>RESOURCE</td>
<td>Sequential processing of tasks can be controlled through the use of resources. Resources are entries in the DEVICE file which must be allocated to a process(es) before that process can continue.</td>
</tr>
<tr class="odd">
<td>RETURN</td>
<td>On the computer keyboard, the key located where the carriage return is on an electric typewriter. It is used in VistA to terminate “reads.” Symbolized by &lt;RET&gt;.</td>
</tr>
<tr class="even">
<td>SCHEDULING OPTIONS</td>
<td>This is a technique of requesting that TaskMan run an option at a given time, perhaps with a given rescheduling frequency.</td>
</tr>
<tr class="odd">
<td>SCREEN</td>
<td>A CRT, monitor or video terminal</td>
</tr>
<tr class="even">
<td>SECONDARY MENUS</td>
<td>Options assigned to individual users to tailor their menu choices. If a user needs a few options in addition to those available on the Primary menu, the options can be assigned as secondary options. To facilitate menu jumping, secondary menus should be specific activities, not elaborate and deep menu trees.</td>
</tr>
<tr class="odd">
<td>SECURITY KEY</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td>SERVER</td>
<td>An entry in the OPTION file. An automated mail protocol that is activated by sending a message to a server at another location with the “S.server” syntax. This activity is specified in the OPTION file.</td>
</tr>
<tr class="odd">
<td>SET OF CODES</td>
<td>Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="even">
<td>SIGN-ON/SECURITY</td>
<td>The Kernel module that regulates access to the menu system. It performs a number of checks to determine whether access can be permitted at a particular time. A log of sign-ons is maintained.</td>
</tr>
<tr class="odd">
<td><p>SITE MANAGER/</p>
<p>IRM CHIEF</p></td>
<td>At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as liaison to the ISCs.</td>
</tr>
<tr class="even">
<td>SPACEBAR RETURN</td>
<td>You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="odd">
<td>SPECIAL QUEUING</td>
<td>An option attribute indicating that TaskMan should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="even">
<td>SPECIALTY</td>
<td>The particular subject area or branch of medical science to which one devotes professional attention.</td>
</tr>
<tr class="odd">
<td>SPOOLER</td>
<td><p>Spooling (under any system) provides an intermediate storage location for files (or program output) for printing at a later time.</p>
<p>In the case of VistA, the Kernel manages spooling so that the underlying OS mechanism is transparent. The Kernel subsequently transfers the text to the ^XMBS global for despooling (printing).</p></td>
</tr>
<tr class="even">
<td>STOP CODE</td>
<td>A number (i.e., a subject area indicator) assigned to the various clinical, diagnostic, and therapeutic sections of a facility for reporting purposes. For example, all outpatient services within a given area (e.g., Infectious Disease, Neurology, and Mental Hygiene—Group) would be reported to the same clinic stop code.</td>
</tr>
<tr class="odd">
<td>SYNONYM</td>
<td>A field in the OPTION file. Options may be selected by their menu text or synonym (see Menu Text).</td>
</tr>
<tr class="even">
<td>TASKMAN</td>
<td>The Kernel module that schedules and processes background tasks (also called Task Manager).</td>
</tr>
<tr class="odd">
<td>TEMPLATE</td>
<td>A means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file, print specifications are stored in the PRINT TEMPLATE file, and search or sort specifications are stored in the SORT TEMPLATE file.</td>
</tr>
<tr class="even">
<td>TERMINAL</td>
<td>May be either a printer or CRT/monitor/video terminal.</td>
</tr>
<tr class="odd">
<td>TIMED-READ</td>
<td>The amount of time a READ command waits for a user response before it times out.</td>
</tr>
<tr class="even">
<td>TREE STRUCTURE</td>
<td>A term sometimes used to describe the structure of an M array. This has the same structure as a family tree, with the root at the top and ancestor nodes arranged below according to their depth of subscripting. All nodes with one subscript are at the first level, all nodes with two subscripts at the second level, and so on.</td>
</tr>
<tr class="odd">
<td>TRIGGER</td>
<td>A type of VA FileMan cross reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="even">
<td>TYPE-AHEAD</td>
<td>A buffer used to store characters that are entered before the corresponding prompt appears. Type-ahead is a shortcut for experienced users who can anticipate an expected sequence of prompts.</td>
</tr>
<tr class="odd">
<td>UP-ARROW JUMP</td>
<td>In the menu system, entering an up-arrow (^) followed by an option name accomplishes a jump to the target option without needing to take the usual steps through the menu pathway.</td>
</tr>
<tr class="even">
<td>USER ACCESS</td>
<td><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="odd">
<td>USER INTERFACE</td>
<td>The way the package is presented to the user—issuing of prompts, help messages, menu choices, etc. A standard user interface can be achieved by using VA FileMan for data manipulation, the menu system to provide option choices, and VA FileMan’s Reader, the ^DIR utility, to present interactive dialogue.</td>
</tr>
<tr class="even">
<td>VA</td>
<td>The Department of Veterans Affairs, formerly called the Veterans Administration.</td>
</tr>
<tr class="odd">
<td>VA FILEMAN</td>
<td>A set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A package of on-line computer routines written in the M language which can be used as a stand-alone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer stored files.</td>
</tr>
<tr class="even">
<td>VERIFY CODE (SEE PASSWORD)</td>
<td>An additional security precaution used in conjunction with the Access Code. Like the Access Code, it is also 6 to 20 characters in length and, if entered incorrectly, will not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture, formerly Decentralized Hospital Computer Program of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages which undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
</tbody>
</table>
