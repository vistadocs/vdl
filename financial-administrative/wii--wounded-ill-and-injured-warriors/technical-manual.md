---
title: WII Version 1.1 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
  - contents
  - facility
  - redacted
  - dfas
  - active
  - action
  - record
page_count: 0
word_count: 12635
section_count: 9
table_count: 1
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: February 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Wounded_Injured_and_Ill_Warriors/wii_1_1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Wounded_Injured_and_Ill_Warriors/wii_1_1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=178"
---

![](wii-version-1-1-technical-manual/001.png)

Line of Action (LOA) \#8

Pay Management

Interim Solution

TECHNICAL MANUAL

SECURITY GUIDE

February 2009

Office of Enterprise Development

INTENTIONALLY BLANK

Revision History

| Date               | Revision        | Page Number | Description                                                                  |
|--------------------|-----------------|-------------|------------------------------------------------------------------------------|
| August 2008        | Initial Version |             | Document created.                                                            |
| September 10,2008  | Version .2      | C1 to C155  | List of VA facilities added                                                  |
| September 23, 2008 | Version .3      | B1to B4     | GWOT LOA#8/DFAS extract                                                      |
| October 1, 2008    | Version .4      | 32          | Insert Product Security Section                                              |
| October 21, 2008   | Version .5      | F3          | Checksums                                                                    |
| January 2, 2009    | Version .6      | 8           | File Description Updates                                                     |
| January 10, 2009   | Version .7      | 9           | Remove real world name                                                       |
| January 15, 2009   | Version .8      | 1, 2        | Deleted reference to REDACTED, used -central collecting facility             |
|                    |                 | 4           | Replaced Figure 1 with similar figure used in BRD and Training Manual        |
|                    |                 | F 1- F      | Completed test site information and reformatted to Courier New               |
|                    |                 |             | Deleted Station List                                                         |
| January 22,2009    | Version .9      |             | Final draft version                                                          |
| January 26, 2009   |                 | Appendix E  | Patch description removed                                                    |
|                    |                 | 3           | Corrected text: WII ADT REVIEWER                                             |
|                    |                 |             | Added 508 compliant metadata tags                                            |
|                    |                 |             | File name changed to adhere to naming convention and font change to Ariel 12 |
| February 2, 2009   | Version 1.0     |             | Final version                                                                |

INTENTIONALLY BLANK

Table of Contents

[Appendix B – Proposed Data Elements/File Layout for GWOT LOA#8/DFAS  
Extract for Interim Solution B-[1](#_Toc338214246)](#_Toc338214246)

INTENTIONALLY BLANK

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Description of Process](#description-of-process)
- [Technical Components](#technical-components)
  - [Routines](#routines)
    - [Mail Group Description](#mail-group-description)
    - [Options File Descriptions](#options-file-descriptions)
    - [Remote Procedures](#remote-procedures)
    - [Files Descriptions](#files-descriptions)
    - [Protocols Descriptions](#protocols-descriptions)
- [Data Elements](#data-elements)
  - [Format of Transmission To DFAS](#format-of-transmission-to-dfas)
    - [Facility Identification](#facility-identification)
    - [Status Field](#status-field)
    - [Admission Date](#admission-date)
    - [Admission Time](#admission-time)
    - [Last Name](#last-name)
    - [First Name](#first-name)
    - [Middle Initial](#middle-initial)
    - [Social Security Number](#social-security-number)
    - [Pseudo Social Security Number](#pseudo-social-security-number)
    - [Discharge Date](#discharge-date)
    - [Discharge Time](#discharge-time)
- [Software Product Security](#software-product-security)
  - [Archiving and Purging](#archiving-and-purging)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
This document is in response to the action item developed by the Wounded, Ill, and Injured Senior Oversight Committee, Support and Care for the Wounded - Task Force, under Line of Action (LOA) \#8 Pay Management, to develop a tool to provide accurate and timely personnel and health related data to the Defense Finance and Accounting Service (DFAS) supporting adequate maintenance of pay and entitlements for all wounded warriors. This document specifies the Technical and Security Guide for the Interim Solution which will satisfy this requirement. It is envisioned that a future solution will be fully automated and is described below.
Currently, the Department of Defense’s (DoD) Wounded Warrior Pay Management Program (WWPMP) has identified pay issues for Active Duty Service Members who are admitted to non military medical treatment facilities due to combat-related injuries. Veterans Health Administration (VHA) often provides inpatient and outpatient health care services to Active Duty Service members. The Department of Defense/Defense Finance and Accounting Service (DoD/DFAS) has experienced difficulty in keeping accountability for this population and the lack of accurate accountability may adversely impact the pay of Service Members.
In the fall 2007, through a collaborative effort between the Department of Veterans Affairs (VA), VHA and DoD/DFAS VA and VHA agreed to provide defined data elements to DoD/DFAS to facilitate tracking of Active Duty Service Members admitted to inpatient VA facilities. In February 2008 a Memorandum of Understanding (MOU) by and between VA and VHA and DoD/DFAS was executed. The MOU established the authorities and agreement for the exchange of information relating to admission to and discharge from inpatient VA health care facilities of Active Duty personnel. A copy of the executed MOU is enclosed in Appendix A. This agreement is consistent with and supports the mission of the VA/DoD Joint Executive Council to improve the quality, efficiency and effectiveness of the delivery of pay benefits to service members admitted to inpatient VA services.
There were two (2) solutions conceived during the conceptualization of how these requirements could be met. The first is the Interim solution, which can be put into service in a short period of time, but has the drawback of being more labor intensive. The Interim Solution is the focus of this Technical Manual and Security Guide. The second solution, named the Future solution will eliminate all manual processes, sending the records to a central server which will collect and transmit them automatically to the DoD/DFAS on a periodic basis. The Future solution will not be started until the Interim Solution is implemented and analyzed. The Interim Solution requires a weekly data collection process at each VA inpatient facility of Active Duty Service Members admitted and discharged. DoD/DFAS requires a complete list of all Active Duty patient admissions/discharges within the VA. Appendix B provides a detailed list of the data requirements. Each VA inpatient facility will transmitted its list of Active Duty inpatients by secure email to the central collection facility. The approved/released list is then sent to the VA collecting repository at the central collecting facility, via a secure Vista mail server. Each facility’s transmission is collected into one list by a VA coordinator specifically trained to perform this function. The list of all Active Duty Service Members admitted to or discharged from inpatient VA facilities is then transmitted to the DoD/DFAS via an encrypted email to a secure DoD/DFAS mailbox. This address has been provided to the VA and VHA by DoD/DFAS. The report, as defined in Appendix B and detailed in Section Format Transmissions to DFAS (page 24) will include the Active Duty Service Member’s first name, middle name or initial, last name, and social security number, and his/her admission date and time and/or discharge date and time and the facility identification number.
> **NOTE:** Facilities that do not have any admissions and/or discharges during the reporting period are required to submit an email stating that there were no admissions and/or discharges.
It is assumed that the Interim Solution will be accomplished as follows:
A patch delivered to the Vista ADT software.
Training of designated staff at each facility
Deployment of patch following a several week testing period.

## Description of Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section presents a brief description of the process that was created to collect Local Admissions and Discharges from each facility and collect the data in a single repository for transmission to DoD/DFAS.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th>At the inpatient VA facility</th>
<th><p>1. Site will appoint a point of contact (POC) to manage the data, electronic files and emails, and submit the POC’s name and contact information to the HEC.</p>
<p>2. The facility POC will run a background job once a week. This job will collect data based on admissions and discharges that occurred during the collection period for patients with a primary or other eligibility of TRICARE, SHARING AGREEMENT or OTHER FEDERAL AGENCY. The qualifying entries are stored at the local facility in a FileMan file.</p>
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
<td><p>1. The receiving mail server will automatically unload the data from each facility and store the data in a single FileMan file.</p>
<p>2. A POC at the central collection facility site will use a Delphi tool to extract the data from the repository and place the data a newly created text (.txt) file.</p>
<p>3. The POC will send an Outlook message with the .txt file containing the data attached, and will send the comprehensive data to DFAS via secure email. Once the data has been sent to DFAS, those entries will be marked with a status of sent to DFAS and the date in which the files were sent. The list going to DFAS will only contain the data elements authorized by the MOU and that are requested by the coordinator in charge of this operation.</p></td>
</tr>
<tr class="even">
<td>At DFAS</td>
<td><p>1. DFAS will receive the secure email at the appropriate mail server.</p>
<p>2. DFAS will review the data and make the appropriate change status of active duty SMs as defined in transmitted data.</p></td>
</tr>
</tbody>
</table>

Figure 1 illustrates the workflow of each of the above steps.

![Figure 1 Workflow diagram of the DoD/DFAS Report](wii-version-1-1-technical-manual/002.png)

*Figure 1 Workflow diagram of the DoD/DFAS Report*

A more detailed description of the processes at the VA Inpatient Facility is presented as follows:

A Background job is tasked to run once a week at each facility. This job collects data based on admissions and discharges that occurred during the collection period and the patient’s eligibility (TRICARE, SHARING AGREEMENT and OTHER FEDERAL AGENCY). The qualifying entries are stored at the local facility in the new WII ADMISSIONS DISCHARGES file (# 987.5).

When the background job has completed processing, a VistA Mailman message is sent to the WII ADT REVIEWER mail group (created during the install) alerting mail group members that the facility either has entries that need approving or that there are no entries to approve.

A point of contact at each facility reviews the data via the WII REVIEW ADT EVENTS option, which employs a List Manager User interface. The reviewer is provided a list of potential Active Duty patients.

Tools within the option provide the ability to expand the qualifying record (and review patient data to determine whether the patient is Active Duty or not), Approve the Record if the patient is Active Duty, or Remove the Entry if the patient is not. If the list is missing an entry the reviewer has the ability to add it to the list. Please note that Adding a record to the local facility list will bypass the eligibility requirements (eligibility of TRICARE, SHARING AGREEMENT and OTHER FEDERAL AGENCY. In addition, the ability to Print the List of potential patients, the list of “DFAS Approved Pending,” (patients flagged to transmit data) and “Deleted ADT Events” (patients removed from the list because they are not Active Duty) is also provided.

Once the entries are approved at the local facility the reviewer releases the list for transmission to a central repository by exiting the option. From there, the list is compiled and then provided to DFAS via a secure, encrypted process.

INTENTIONALLY BLANK

# Technical Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following general components are included in this section:

Routines (11)

Options (4)

Mail Group (1)

Remote Procedures (1)

Files (4) two (2) to be released nationally and all four (4) at the repository.

Protocols (11)

The following routines have been added in order to provide the functionality for the Interim Solution.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WIIACT4 Main collection routine to gather data from 405 and inserted into 987.5.

WIIADT1 Gathers data from 987.7 and moves it to the clipboard.

WIIELG Expanded Eligibility LM screen.

WIIGATD Moves data from 987.5 to the main collecting facility.

WIILM Main List manager routine.

WIILM01 Supporting routine for list manager.

WIILM02 WII List Manager Actions continued.

WIILM03 WII LM SCREEN FOR PENDING TRANSMISSION.

WIILM04 WII LM SCREEN FOR DISAPPROVED ADT EVENTS.

WIISERV Unloading routine called from the Server option WII ADT SERVER.

WIIPOST Post init to set up proper entry in file 987.6.

Check sum values new generated with CHECK1^XTSUMBLD

WIIACT4 value = 49548626

WIIADT1 value = 13382231

WIIELG value = 6625762

WIIGATD value = 8535177

WIILM value = 4620053

WIILM01 value = 15511369

WIILM02 value = 2080564

WIILM03 value = 6256776

WIILM04 value = 6401181

WIIPOST value = 1917839

WIISERV value = 8564416

Check sum values old generated with CHECK^XTSUMBLD

WIIACT4 value = 13037055

WIIADT1 value = 7041292

WIIELG value = 3673484

WIIGATD value = 3974621

WIILM value = 2341319

WIILM01 value = 7486459

WIILM02 value = 1382618

WIILM03 value = 3293727

WIILM04 value = 3457715

WIIPOST value = 1338326

WIISERV value = 3364619

### Mail Group Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: WII ADT REVIEWER

TYPE: private

ALLOW SELF

ENROLLMENT?: NO

MEMBER: XXXXXXX, XXXXXXXX X

DESCRIPTION: Members of this mail group will receive notifications that there are Active Duty patients that have been admitted or discharged to your facility. The data needs to be reviewed and marked as ready to transmit to the national collecting point. The option to review and mark entries is WII REVIEW ADT EVENTS.

ORGANIZER: XXXXXXX, XXXXXXXX X

### Options File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: WII ADT SERVER

MENU TEXT: WII ADT SERVER

TYPE: Server

CREATOR: XXXXXXX, XXXXXXXX X

DESCRIPTION: This server option receives the sending facilities data and inserts the data into either the WII ADT ALL SITES file (#987.7) or the WII STATION STATUS (#987.8) file. The WII ADT ALL SITES file contains the data that will be used for the data transmission to the DOD. WII STATION STATUS file is used to track the sending stations process.

ROUTINE: UNLOAD^WIISERV

SERVER ACTION: RUN IMMEDIATELY

SUPRESS BULLETIN: YES, SUPRESS IT

SERVER REPLY: NO REPLY (DEFAULT)

SAVE REQUEST: Save request in Postmaster basket

UPPERCASE MENU TEXT: WII ADT SERVER

This server option receives the sending facilities data and inserts the data into the WII ADT ALL SITES FILE (#987.7).

NAME: WII BUILD ADT EVENTS

MENU TEXT: WII Build ADT Events

TYPE: run routine

CREATOR: XXXXXXX, XXXXXXXX X

DESCRIPTION: This option is to be scheduled via Taskman to run once a week. This option will run the routine WIIACT4 line tag EN. This will insert qualifying entries into the WII ADMISSIONS DISCHARGES (#987.5) file. See the DD description for an expanded description.

ROUTINE: EN^WIIACT4

UPPERCASE MENU TEXT: WII BUILD ADT EVENTS

NAME: WII REVIEW ADT EVENTS

MENU TEXT: REVIEW ADT EVENTS

TYPE: run routine

DESCRIPTION: This is the option that contains all RPCs that will be used by the WII product. At the current time there is only one RPC item listed; WII ADT.

CREATOR: XXXXXXX, XXXXXXXX X

EXIT ACTION PRESENT: YES

DESCRIPTION: This option allows the facility reviewer to remove and to approve active duty patients’ movements that have occurred at your facility. Once the events are approved the data will be rolled up to your VISN.

EXIT ACTION: D ^WIIGATD

ROUTINE: EN^WIILM

UPPERCASE MENU TEXT: REVIEW ADT EVENTS

NAME: WII RPCS

MENU TEXT: WII ALL RPCS

TYPE: Broker (Client/Server)

CREATOR: XXXXXXX, XXXXXXXX X

DESCRIPTION: This is the option that contains all RPC’s that will be used by the WII product. At the current time there is only one RPC item listed; WII ADT.

RPC: WII ADT

UPPERCASE MENU TEXT: WII ALL RPCS

### Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: WII ADT

TAG: EN

ROUTINE: WIIADT1

RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION: This remote procedure is run from the Delphi GUI. It generates a list of all admissions and discharges that have been transferred to the main collection point. The GUI allows the user to select all entries that have not been sent to DEFAS or regenerate the list by a date. Data is extracted from the WII ADT ALL SITES FILE (#987.7).

INPUT PARAMETER: DATE

PARAMETER TYPE: WORD PROCESSING

MAXIMUM DATA LENGTH: 15

REQUIRED: YES

SEQUENCE NUMBER: 1

### Files Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sections presents the instructions related to the File Descriptions. Exhibit 1 presents the instructions in the actual test format.

Exhibit 1 File Descriptions Instructions in Test Format

REDACTED

![](wii-version-1-1-technical-manual/003.png)

![](wii-version-1-1-technical-manual/004.png)

![](wii-version-1-1-technical-manual/005.png)

![](wii-version-1-1-technical-manual/006.png)

REDACTED

REDACTED

REDACTED

![](wii-version-1-1-technical-manual/007.png)

![](wii-version-1-1-technical-manual/008.png)

![](wii-version-1-1-technical-manual/009.png)

![](wii-version-1-1-technical-manual/010.png)

REDACTED

![](wii-version-1-1-technical-manual/011.png)

![](wii-version-1-1-technical-manual/012.png)

### Protocols Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WII ADD ENTRY

NAME: WII ADD ENTRY

ITEM TEXT: Add Adm/Dischg to list

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to manually add an entry into the WII ADMISSIONS DISCHARGES file (#987.5) in the case that an admission or discharge did not get collected by the weekly back ground job (WII BUILD ADT EVENTS).

SYNONYM: WII

EXIT ACTION: S VALMBCK="R" D INIT^WIILM

ENTRY ACTION: D ADD^WIILM02

TIMESTAMP: 61248,32196

WII APPROVE

NAME: WII APPROVE

ITEM TEXT: Approve Record

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to approve entries that have been collected by the weekly back ground process (WII BUILD ADT EVENTS). The approved entries are sent to the repository when the user exits the WII REVIEW ADT option.

SYNONYM: WII

EXIT ACTION: S VALMBCK="R" D PAUSE^VALM1

ENTRY ACTION: D TR^WIILM01 TIMESTAMP: 61248,32196

WII DFAS STS 2 LIST

NAME: WII DFAS STS 2 LIST

ITEM TEXT: DFAS Approved Pending

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to review entries that have been selected for transmission to the repository.

SYNONYM: WII

EXIT ACTION: D CLEAN^VALM10,INIT^WIILM

ENTRY ACTION: D EN^WIILM03 TIMESTAMP: 61248,32196

WII DFAS STS 3 LIST

NAME: WII DFAS STS 3 LIST

ITEM TEXT: Deleted ADT Events

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to delete the approved entries off the approved listed.

SYNONYM: WII

EXIT ACTION: D CLEAN^VALM10,INIT^WIILM

ENTRY ACTION: D EN^WIILM04

WII EXPAND ENTRY

NAME: WII EXPAND ENTRY

ITEM TEXT: Expand Eligibility

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to expand the details of a single entry on the pending approval list.

SYNONYM: WII

EXIT ACTION: K ^TMP(\$J,"WIIELG") S VALMBCK="R"

ENTRY ACTION: D EX^WIILM02

WII LM MENU

NAME: WII LM MENU ITEM

TEXT: WII LIST MANAGER MENU

TYPE: menu

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol controls the main list manager menus displayed to the user. This protocol is called from the option WII REVIEW ADT EVENTS.

SYNONYM: WII

COLUMN WIDTH: 26 MNEMONIC WIDTH: 4

ITEM: WII REMOVE ENTRY MNEMONIC: RM

SEQUENCE: 3

ITEM: WII APPROVE MNEMONIC: AP

SEQUENCE: 1

ITEM: WII PRINT LIST MNEMONIC: PL

SEQUENCE: 2

ITEM: WII EXPAND ENTRY MNEMONIC: EX

SEQUENCE: 4

ITEM: WII ADD ENTRY MNEMONIC: AE

SEQUENCE: 6

ITEM: WII DFAS STS 2 LIST MNEMONIC: RV

SEQUENCE: 5

ITEM: WII DFAS STS 3 LIST MNEMONIC: XX

SEQUENCE: 7

HEADER: D SHOW^VALM MENU PROMPT: Select Action:

WII LM STS 2 MENU

NAME: WII LM STS 2 MENU

TYPE: menu

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol controls the rollback list manager menus displayed to the user. It is attached to the WII LM MENU protocol. The following protocols are included in this protocol.

SYNONYM: WII

COLUMN WIDTH: 36 MNEMONIC WIDTH: 4

ITEM: WII PRINT LIST MNEMONIC: PL

SEQUENCE: 3

ITEM: WII EXPAND ENTRY MNEMONIC: EX

SEQUENCE: 1

ITEM: WII PENDING RBCK MNEMONIC: CS

SEQUENCE: 2

HEADER: D SHOW^VALM MENU PROMPT: Select Action:

WII LM STS 3 MENU

NAME: WII LM STS 3 MENU

TYPE: menu

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol controls the Transmission Not Approved displayed to the user. This protocol is attached to the WII LM MENU protocol.

SYNONYM: WII

COLUMN WIDTH: 36 MNEMONIC WIDTH: 4

ITEM: WII PENDING RBCK MNEMONIC: CS

SEQUENCE: 1

ITEM: WII EXPAND ENTRY MNEMONIC: EX

SEQUENCE: 2

HEADER: D SHOW^VALM MENU PROMPT: Select Action:

WII PENDING RBCK

NAME: WII PENDING RBCK

ITEM TEXT: Roll Back Status to Pending

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII

LM STS 2 MENU. Its function allows users to roll back entries that have been selected to transmit to the repository but have yet been sent.

SYNONYM: WII

ENTRY ACTION: S VALMBCK="R" D PD^WIILM01

WII PENDING RBCK3

NAME: WII PENDING RBCK3

ITEM TEXT: Roll Back Status to Pending

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII LM STS 3 MENU. Its function allows users to roll back entries that have been flagged NOT to transmit

SYNONYM: WII

ENTRY ACTION: S VALMBCK="R" D PD3^WIILM01

WII PRINT LIST

NAME: WII PRINT LIST

ITEM TEXT: Print List

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to print the approved entries.

SYNONYM: WII

EXIT ACTION: S VALMBCK="R"

ENTRY ACTION: D PL^WIILM01

WII REMOVE ENTRY

NAME: WII REMOVE ENTRY

ITEM TEXT: Remove Entry

TYPE: action

CREATOR: XXXXXX,XXXXXX XXXX

PACKAGE: WOUNDED INJURED ILL WARRIORS

DESCRIPTION: This protocol is a list manager action item located on the WII REVIEW ADT EVENTS option. Its function allows users to remove entries from the list. Note that the entries are not deleted from the file but marked with a status of Transmission Not Approved.

SYNONYM: WII

EXIT ACTION: S VALMBCK="R" D PAUSE^VALM1

ENTRY ACTION: D RM^WIILM01

INTENTIONALLY BLANK

# Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Format of Transmission To DFAS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the format of the transmission of data to DoD/DFAS (Steps 9 and 10 of the workflow solution on the previous section. Also, a tabular format of this information is given in Appendix B. The VA will transmit groups of records to DoD/DFAS, each record will be terminated with a carriage return character. Each Record consists of 117 characters as defined below.

### Facility Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 1 to 6 (Alphanumeric), name is VAFacilityID

VAFacilityID is the identification of the VA facility where the Active Duty Service Member was treated.

Field Definition: Alphanumeric

VAFacilityID will contain three numerical values followed by zero to three alpha numeric characters (e.g., 999 or 999AB or 999A4)

Min Length = 3 characters

Max Length = 6 characters

Required

\*\* See station list

### Status Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 7 to 7 (Character), name is RecordStatusField

RecordStatusField is a VA field to communicate possible changes to a record in the data file.

Field Definition: Character

‘A’- Patient Name Change for SSN from last data file.

‘B’- Delete previously transmitted admission date record.

‘C’- Delete previously transmitted discharge date in record.

‘D’- Delete both admission and discharge record.

‘E’- Facility ID changed from previously transmitted record.

‘ ‘ - No change made to the record

Not Required

### Admission Date 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 8 to 17 (Date), field name is AdmitDate

AdmitDate is the Admission Date at the VA Facility.

Field Definition: Date

MM/DD/YYYY

2-digit month

2-digit day

4-digit year

‘ ‘ – No data available

MUST HAVE SLASHES FOR DATE

Required

### Admission Time 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 18 to 21, field name is AdmitTime

AdmitTime is the Admission Time at the VA Facility.

Field Definition: Numeric

VA Facility Local time hhmmssss (Military Time, e.g. 1345);

Admission time(s) prior to 1200 shall contain a leading zero (e.g. 0800)

0-24 hour(s)

0-59 minute(s)

‘ ‘ – No data available

Required

### Last Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 22 to 56, field name is LastName

LastName is the last name of the Patient/Active Duty Service Member.

Field Definition: Character

Max Length = 35 characters

Upper Case LAST NAME

All PUNCTUATION will be removed from ADSM name data

‘ ‘ = No data available

Not Required

### First Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 57 to 91, field name is FirstName

FirstName is the first name of the Patient/Active Duty Service Member.

Field Definition: Character

Max Length = 35 characters

Upper Case FIRST NAME

All PUNCTUATION will be removed from ADSM name data

‘ ‘ = No data available

Not Required

### Middle Initial

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 92 to 93, field name is MiddleInitial

MiddleInitial is the Middle Initial of the Patient/Active Duty Service Member.

Field Definition: Character

Max Length = 2 characters

Upper Case MIDDLE INITIAL

All PUNCTUATION will be removed from ADSM name data

‘ ‘ = No data available

Not Required

### Social Security Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 94 to 102, field name is SSN

SSN is the Social Security Name of the Patient/Active Duty Service Member.

Field Definition: Numeric

nnnnnnnnn

SSN will contain leading zeros

SSN will NOT contain hyphens

Required

### Pseudo Social Security Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 103 to 103, field name is PseudoSSNInd

PseudoSSNInd is the indicator for Pseudo Social Security Number of the Patient/Active Duty Service Member.

Field Definition: Character

‘P’ - Indicates that the SSN is a Pseudo SSN

‘ ‘ – Indicates that the SSN is NOT a Pseudo SSN

Not Required

### Discharge Date 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 104 to 113 (Date), field name is DischargeDate

DischargeDate is the Discharge Date from the VA Facility.

Field Definition: Date

MM/DD/YYYY

2-digit month

2-digit day

4-digit year

‘ ‘ – No data available

MUST HAVE SLASHES FOR DATE

Not Required

### Discharge Time 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record position 114 to 117 (Numeric), field name is DischargeTime

DischargeTime is the Discharge Time from the VA Facility.

Field Definition: Numeric

VA Facility Local time hhmmssss (Military Time, e.g. 1345);

Admission time(s) prior to 1200 shall contain a leading zero (e.g. 0800)

0-24 hour(s)

0-59 minute(s)

‘ ‘ – No data available

Not Required

INTENTIONALLY BLANK

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving functions associated with this package.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software does not use or require a specialized product.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No electronic signatures are used in this package.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no security keys associated with this package.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](wii-version-1-1-technical-manual/013.png)

INTENTIONALLY BLANK

<span id="_Toc337366901" class="anchor"></span>Appendix A - VA/DoD DFAS Memorandum of Understanding

![](wii-version-1-1-technical-manual/014.png)

REDACTED

<span id="_Toc338214246" class="anchor"></span>Appendix B – Proposed Data Elements/File Layout for GWOT LOA#8/DFAS Extract for Interim Solution

VHA has compiled a list of data elements, which will be included in the updated file layout for the GWOT LOA#8/DFAS extract, based on our discussion on August 11, 2008 meeting with DFAS. The table below outlines the proposed file layout for all the data elements included in the fixed format file.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 19%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>FIELD NAME</th>
<th>FIELD DEFINITION</th>
<th>FIELD DATA TYPE</th>
<th>FIELD LENGTH</th>
<th>REQUIRED (Y/N)</th>
<th><p>FIELD FORMAT VALUE(S)</p>
<p>LEFT JUSTIFIED FOR EACH FIELD NAME</p></th>
<th>POSITION(S)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VAFacilityID</td>
<td>Facility Identification</td>
<td>ALPHANUMERIC</td>
<td>6</td>
<td>Y</td>
<td><p>VAFacilityID will contain three numerical values followed by zero to three alpha numeric characters (e.g., 999 or 9999AB or 999A4)</p>
<p>VAFacilityID Min Length = 3 characters</p>
<p>VAFacilityID Max Length = 6 characters</p></td>
<td>1-6</td>
</tr>
<tr class="even">
<td>RecordStatusField</td>
<td>VA field to communicate possible changes to a record in the data file.</td>
<td>CHARACTER</td>
<td>1</td>
<td>N</td>
<td><p>‘A’- Patient Name Change for SSN from last data file.</p>
<p>‘B’- Delete previously transmitted admission date record.</p>
<p>‘C’- Delete previously transmitted discharge date in record.</p>
<p>‘D’- Delete both admission and discharge record.</p>
<p>‘E’- Facility ID changed from previously transmitted record.<br />
‘ ‘ – No change made to the record</p></td>
<td>7-7</td>
</tr>
<tr class="odd">
<td>AdmitDate</td>
<td>Admission Date</td>
<td>DATE</td>
<td>10</td>
<td>Y</td>
<td><p>MM/DD/YYYY</p>
<p>2-digit month</p>
<p>2-digit day</p>
<p>4-digit year</p>
<p>‘ ‘ – No data available</p>
<p>CAN HAVE SLASHES FOR DATE</p></td>
<td>8-17</td>
</tr>
<tr class="even">
<td>AdmitTime</td>
<td>Admission Time</td>
<td>NUMERIC</td>
<td>8</td>
<td>Y</td>
<td><p>VA Facility Local time (Military Time, e.g. 1345); Admission time(s) prior to 1200 shall contain a leading zero (e.g. 0800)</p>
<p>0-24 hour(s)</p>
<p>0-59 minute(s)</p>
<p>‘ ‘ – No data available</p></td>
<td>18-21</td>
</tr>
<tr class="odd">
<td>LastName</td>
<td>The last name of the patient/Active Duty Service Member (ADSM)</td>
<td>CHARACTER</td>
<td>35</td>
<td>N</td>
<td><p>Max Length = 35 characters,</p>
<p>Upper Case LAST NAME</p>
<p>All PUNCTUATION will be removed from ADSM name data</p>
<p>‘ ‘ = No data available</p></td>
<td>22-56</td>
</tr>
<tr class="even">
<td>FirstName</td>
<td>The first name of the patient/ Active Duty Service Member (ADSM)</td>
<td>CHARACTER</td>
<td>35</td>
<td>N</td>
<td><p>Max Length = 35 characters</p>
<p>Upper Case FIRST NAME</p>
<p>All PUNCTUATION will be removed from ADSM name data</p>
<p>‘ ‘ = No data available</p></td>
<td>57-91</td>
</tr>
<tr class="odd">
<td>MiddleInitial</td>
<td>The middle initial of the patient/ Active Duty Service Member (ADSM)</td>
<td>CHARACTER</td>
<td>2</td>
<td>N</td>
<td><p>Max Length = 2 characters</p>
<p>Upper Case MIDDLE INITIAL</p>
<p>All PUNCTUATION will be removed from ADSM name data</p>
<p>‘ ‘ = No data available</p></td>
<td>92-93</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Active Duty Service Member (ADSM) Social Security Number</td>
<td>NUMERIC</td>
<td>9</td>
<td>Y</td>
<td><p>nnnnnnnnn</p>
<p>SSN will contain leading zeros</p>
<p>SSN will NOT contain hyphens</p></td>
<td>94-102</td>
</tr>
<tr class="odd">
<td>PseudoSSNInd</td>
<td>Indicator for Pseudo Social Security Number (SSN)</td>
<td>CHARACTER</td>
<td>1</td>
<td>N</td>
<td><p>‘P’ - Indicates that the SSN is a Pseudo SSN</p>
<p>‘ ‘ – Indicates that the SSN is NOT a Pseudo SSN</p></td>
<td>103-103</td>
</tr>
<tr class="even">
<td>DischargeDate</td>
<td>Discharge Date</td>
<td>DATE</td>
<td>10</td>
<td>N</td>
<td><p>MM/DD/YYYY</p>
<p>2-digit month</p>
<p>2-digit day</p>
<p>4-digit year</p>
<p>‘ ‘ – No data available</p></td>
<td>104-113</td>
</tr>
<tr class="odd">
<td>DischargeTime</td>
<td>Discharge Time</td>
<td>NUMERIC</td>
<td>4</td>
<td>N</td>
<td><p>VA Facility Local Time (Military Time, e.g. 1345); Discharge time(s) prior to 1200 shall contain a leading zero (e.g.0800)</p>
<p>0-24 hour(s)</p>
<p>0-59 minute(s)</p>
<p>‘ ‘ – No data available</p></td>
<td>114-117</td>
</tr>
</tbody>
</table>

<span id="_Toc207493536" class="anchor"></span>

Appendix C - Approval to Host Central Repository at REDACTED

The following email documents the approval to host the Central Repository for ADSM admission/discharge information to/from VA inpatient facilities.

From: REDACTED. OI&T (REDACTED

Sent: Tuesday, August 19, 2008 12:57 PM

To: REDACTED; REDACTED; REDACTED,;

REDACTED.; REDACTED; REDACTED,

Subject: RE: The use of REDACTED for the interim solution repository

William-

It would be our pleasure to host the central collection point for this project.

If there is anything I or my staff can do to assist, please let me know.

REDACTED

-----Original Message-----

From: REDACTED

Sent: Tuesday, August 19, 2008 10:21 AM

To: REDACTED REDACTED; REDACTED.; REDACTED; REDACTED ; REDACTED,

Cc: REDACTED

Subject: The use of REDACTED for the interim solution repository

Good morning Mr. REDACTED,

The GWOT (The Global war on terrorism) team has been working on a class 3 product to assist the VA's obligation with one of the requirement's to the Dole Shalala report. One of the requirements is for the VA to report active duty admissions to the DOD. We have created a small product that will transfer data from all facilities to a central collection point and then from there it will be rolled up to the DOD.

We would like to use the REDACTED system as the central collection point. There should be no impact to the system and disk space is very minimal. We plan on moving the product through the proper channels to a Class 1 product. (This is an interim solution).

Why REDACTED? I have access to the REDACTED account; it is my home of record as a VISN 20 employee and seems like a nice fit to our needs. The product has a national assigned name space (WII). The tool is being testing at a Bay Pines test lab and will under go proper review before we move forward.

At this point this request has the blessing of Mr. REDACTED, Ms. REDACTED, Mr. REDACTED and Mr. REDACTED. Please let us know how you feel about this request.

I thank you for your time and consideration. If I can answer any questions please contact me at REDACTED

REDACTED

Detailed to the VA/DOD joint initiative:

Global War on Terrorism/Wounded Injured and ILL Operations Management, Office of Enterprise Development

REDACTED

<span id="_Toc207493538" class="anchor"></span>Appendix D - Attaching Data to Email As Attachment Approval

The following email from DFAS provides documentation to certify that admission/discharge data being sent to DFAS will be in the form of an attached email.

From: REDACTEDCIV DFAS \[REDACTED

Sent: Tuesday, August 19, 2008 9:10 AM

To: REDACTED

Subject: RE: VA test data file 0_14_08

Signed By: There are problems with the signature. Click the signature button for details.

Dave,

You are correct.

Thank you,

V/r

REDACTED

Wounded Warrior Pay Office

DFAS-IN

REDACTED

REDACTED

REDACTED

"Taking Care of Soldiers is My Business."

-----Original Message-----

From: REDACTED REDACTED

Sent: Tuesday, August 19, 2008 11:12 AM

To: REDACTED CIV DFAS; REDACTED CIV DFAS

Cc: REDACTED.; REDACTED CIV DFAS; REDACTED

Subject: RE: VA test data file 0_14_08

So it is safe to say that we are going to be sending the data in outlook

(with PKI) as an attachment of a text file correct?

REDACTED

Detailed to the VA/DOD joint initiative:

Global War on Terrorism/Wounded Injured and ILL

Operations Management, Office of Enterprise Development

REDACTED

INTENTIONALLY BLANK

<span id="_Toc496403768" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TERM</strong></th>
<th><strong>DEFINITION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACTIVE DUTY SERVICE MEMBER</td>
<td>A person who is actively serving in any one of the following branches of service - Army, Navy, Marine Corps, Air Force, Coast Guard, Public Health Service, and National Oceanic and Atmospheric Administration as well as select National Reserve and Guard.</td>
</tr>
<tr class="even">
<td>ADMISSION DATE</td>
<td>Date patient admitted to VA health care facility</td>
</tr>
<tr class="odd">
<td>ADMISSION TYPES</td>
<td><p>TYPE OF ADMISSION:</p>
<p>Directions to the VA staff include: Choose the type of movement this patient had. You will be selecting from active FACILITY MOVEMENT TYPES for which the TRANSACTION TYPE of this movement matches the TRANSACTION TYPE of the FACILITY MOVEMENT TYPE. For example, if you are admitting a patient, you will only be able to select active admission types.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>1 DIRECT ADMISSION ACTIVE</td>
</tr>
<tr class="even">
<td>2 OPT-NSC ADMISSION ACTIVE</td>
</tr>
<tr class="odd">
<td>3 OPT-SC ADMISSION ACTIVE</td>
</tr>
<tr class="even">
<td>4 A/C ADMISSION ACTIVE</td>
</tr>
<tr class="odd">
<td>5 TRANSFER IN ADMISSION ACTIVE</td>
</tr>
<tr class="even">
<td>6 NON-VETERAN ADMISSION ACTIVE</td>
</tr>
<tr class="odd">
<td>7 WAITING LIST ADMISSION ACTIVE</td>
</tr>
<tr class="even">
<td>8 PBC ADMISSION ACTIVE</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="even">
<td>ADT</td>
<td>Admission, Discharge &amp; Transfer</td>
</tr>
<tr class="odd">
<td>AITC</td>
<td>Austin Information Technology Center</td>
</tr>
<tr class="even">
<td>ANSI</td>
<td>American National Standards Institute</td>
</tr>
<tr class="odd">
<td>BHIE</td>
<td>Bi-directional Health Information Exchange</td>
</tr>
<tr class="even">
<td>BIDIRECTIONAL HEALTH INFORMATION EXCHANGE (BHIE)</td>
<td><p>The Bidirectional Health Information Exchange (BHIE) is a joint information technology data exchange initiative between the Department of Veterans Affairs (VA) and Department of Defense (DoD). BHIE permits VA and DoD clinicians to view electronic healthcare data from each other's systems, VA's Computerized Patient Record System (CPRS) and DoD's Composite Health Care System (CHCS).  The data is shared bidirectionally, in real time, for patients who receive care from both VA and DoD facilities.  Currently, the data that is made viewable bidirectionally using BHIE are as follows:</p>
<p>Outpatient pharmacy data</p>
<p>Allergy data</p>
<p>Patient identification correlation</p>
<p>Laboratory result data including surgical pathology reports, cytology and microbiology data, chemistry and hematology data</p>
<p>Lab orders data</p>
<p>Radiology reports</p>
<p>BHIE is implemented at select DoD military facilities and at all VA medical facilities.  BHIE permits DoD providers to view BHIE data from all VA medical facilities and VA to view BHIE data from the DoD facilities where BHIE is implemented.  VA and DoD are continuing to support the expansion of BHIE to additional DoD facilities.</p></td>
</tr>
<tr class="odd">
<td>BRANCH OF SERVICE</td>
<td><p>Below are the Branch of Service and their Codes used during the Registration process:</p>
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td>1</td>
<td>ARMY</td>
</tr>
<tr class="even">
<td>2</td>
<td>AIR FORCE</td>
</tr>
<tr class="odd">
<td>3</td>
<td>NAVY</td>
</tr>
<tr class="even">
<td>4</td>
<td>MARINE CORPS</td>
</tr>
<tr class="odd">
<td>5</td>
<td>COAST GUARD</td>
</tr>
<tr class="even">
<td>6</td>
<td>OTHER</td>
</tr>
<tr class="odd">
<td>7</td>
<td>MERCHANT SEAMAN</td>
</tr>
<tr class="even">
<td>9</td>
<td>USPHS</td>
</tr>
<tr class="odd">
<td>10</td>
<td>NOAA</td>
</tr>
<tr class="even">
<td>11</td>
<td>F.COMMONWEALTH</td>
</tr>
<tr class="odd">
<td>12</td>
<td>F.GUERILLA</td>
</tr>
<tr class="even">
<td>13</td>
<td>F.SCOUTS NEW</td>
</tr>
<tr class="odd">
<td>14</td>
<td>F.SCOUTS OLD</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="even">
<td>BRD</td>
<td>Business Requirements Document</td>
</tr>
<tr class="odd">
<td>CARET</td>
<td>A symbol expressed as up caret (^), left caret (&lt;), or right caret (&gt;). In many M systems, a right caret is used as a system prompt and an up caret as an exiting tool from an option. Also known as the up-arrow symbol or shift–6 key.</td>
</tr>
<tr class="even">
<td>CBO</td>
<td>Chief Business Office</td>
</tr>
<tr class="odd">
<td>CIO</td>
<td>Chief Information Office</td>
</tr>
<tr class="even">
<td>COMMAND</td>
<td>A combination of characters that instruct the computer to perform a specific operation.</td>
</tr>
<tr class="odd">
<td>COMMON MENU</td>
<td>Options that are available to all users. Entering two question marks at the menu’s select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="even">
<td>CROSS REFERENCE</td>
<td><p>An indexing method whereby files can include pre-sorted lists of entries as part of the stored database. Cross-references (x-refs) facilitate look-up and reporting.</p>
<p>A file may be cross-referenced to provide direct access to its entries in several ways. For example, VA FileMan allows the Patient file to be cross-referenced by name, social security number, and bed number. When VA FileMan asks for a patient, the user may then respond with either the patient’s name, social security number, or his bed number. A cross-reference speeds up access to the file, both for looking up entries and for printing reports.</p>
<p>A cross-reference is also referred to as an index or cross-index.</p></td>
</tr>
<tr class="odd">
<td>CSV</td>
<td>Comma Separated Value</td>
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
<td>DATA DICTIONARY (DD)</td>
<td><p>The Data Dictionary is a global containing a description of what kind of data is stored in the global corresponding to a particular file. The data is used internally by FileMan for interpreting and processing files.</p>
<p>A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file’s elements or data attributes; programmers review the definitions of a file’s internal structure.</p></td>
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
<td>A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file. A data collection has different data fields (e.g., patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="odd">
<td>DATABASE MANAGEMENT SYSTEM</td>
<td>A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="even">
<td>DATABASE, NATIONAL</td>
<td>A database that contains data collected or entered for all VHA sites.</td>
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
<td>A response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.</td>
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
<td>DFAS</td>
<td>Department of Defense Department of Financial and Accounting Services</td>
</tr>
<tr class="even">
<td>DICTIONARY</td>
<td>A database of specifications of data and information processing resources. VA FileMan’s database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="odd">
<td>DISCHARGE DATE</td>
<td>Date patient discharged from VA health care facility</td>
</tr>
<tr class="even">
<td>DISCHARGE TYPES</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>CONTINUED ASIH (OTHER FACILITY)</td>
</tr>
<tr class="even">
<td>DEATH</td>
</tr>
<tr class="odd">
<td>DEATH WITH AUTOPSY</td>
</tr>
<tr class="even">
<td>DISCHARGE FROM IMLTC/NHCU/DOM WHILE ASIH</td>
</tr>
<tr class="odd">
<td>DISCHARGE TO CNH</td>
</tr>
<tr class="even">
<td>FROM ASIH</td>
</tr>
<tr class="odd">
<td>IRREGULAR</td>
</tr>
<tr class="even">
<td>NON-BED CARE</td>
</tr>
<tr class="odd">
<td>NON-SERVICE CONNECTED (OPT-NSC)</td>
</tr>
<tr class="even">
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>OPT-SC</td>
</tr>
<tr class="even">
<td>REGULAR</td>
</tr>
<tr class="odd">
<td>TO DOM FROM HOSP</td>
</tr>
<tr class="even">
<td>TO IMLTC/NHCU FROM DOM</td>
</tr>
<tr class="odd">
<td>TO IMLTC/NHCU FROM HOSP</td>
</tr>
<tr class="even">
<td>TRANSFER OUT</td>
</tr>
<tr class="odd">
<td>VA IMLTC/NHCU TO CNH</td>
</tr>
<tr class="even">
<td>WHILE ASIH</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>DISK</td>
<td>The media used in a disk drive for storing data.</td>
</tr>
<tr class="even">
<td>DINUM</td>
<td>Is the unique line number in a record.</td>
</tr>
<tr class="odd">
<td>DoD</td>
<td>Department of Defense</td>
</tr>
<tr class="even">
<td>DOMICILIARY</td>
<td>Facility that provides care and living space for persons who cannot otherwise live independently. Domiciliaries do not provide skilled nursing services.</td>
</tr>
<tr class="odd">
<td>DOUBLE QUOTE (")</td>
<td>A symbol used in front of a Common option’s menu text or synonym to select it from the Common menu. For example, the five character string "TBOX" selects the User’s Toolbox Common option.</td>
</tr>
<tr class="even">
<td>DSCC</td>
<td>Documentation Standards and Conventions Committee. Package documentation is reviewed in terms of standards set by this committee.</td>
</tr>
<tr class="odd">
<td>DUZ</td>
<td>A local variable holding the user number that identifies the signed-on user.</td>
</tr>
<tr class="even">
<td>DUZ(0)</td>
<td>A local variable that holds the File Manager Access Code of the signed-on user.</td>
</tr>
<tr class="odd">
<td>ELIGIBILITY</td>
<td>Determination of a person's qualification for VA health care and related benefits.</td>
</tr>
<tr class="even">
<td>ELIGIBILITY CODE</td>
<td><p>Below are the Eligibility Codes used during the Registration process:</p>
<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 6%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>AID &amp; ATTENDANCE</th>
<th>2</th>
<th>VETERAN</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALLIED VETERAN</td>
<td>5</td>
<td>NON-VETERAN</td>
</tr>
<tr class="even">
<td>CHAMPUS</td>
<td>7</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>CHAMPVA</td>
<td>1</td>
<td>NON-VETERAN</td>
</tr>
<tr class="even">
<td>COLLATERAL OF VET.</td>
<td>2</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>DOM. PATIENT</td>
<td>6</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>EMPLOYEE</td>
<td>3</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>HOUSEBOUND</td>
<td>2</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>HUMANITARIAN EMERGENCY</td>
<td>6</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>MEXICAN BORDER WAR</td>
<td>2</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>NSC</td>
<td>5</td>
<td>VETERAN</td>
</tr>
<tr class="odd">
<td>NSC, VA PENSION</td>
<td>4</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>OTHER FEDERAL AGENCY</td>
<td>4</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>PRISONER OF WAR</td>
<td>2</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>PURPLE HEART RECIPIENT</td>
<td>2</td>
<td>VETERAN</td>
</tr>
<tr class="odd">
<td>REIMBURSABLE INSURANCE</td>
<td>8</td>
<td>NON-VETERAN</td>
</tr>
<tr class="even">
<td>SC LESS THAN 50%</td>
<td>3</td>
<td>VETERAN</td>
</tr>
<tr class="odd">
<td>SERVICE CONNECTED 50% to 100%</td>
<td>1</td>
<td>VETERAN</td>
</tr>
<tr class="even">
<td>SHARING AGREEMENT</td>
<td>7</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>TRICARE</td>
<td>7</td>
<td>NON-VETERAN</td>
</tr>
<tr class="even">
<td>VOLUNTEER</td>
<td>3</td>
<td>NON-VETERAN</td>
</tr>
<tr class="odd">
<td>WORLD WAR I</td>
<td>2</td>
<td>VETERAN</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>ENCRYPTION</td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g., access/verify codes).</td>
</tr>
<tr class="even">
<td>ENROLLEE</td>
<td><p>A Veteran that applies for enrollment in VA health care system and</p>
<p>who is not deceased, ineligible, cancel/declined or rejected enrollment status or fugitive felon status.</p></td>
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
<td>EXTRACTOR</td>
<td><p>A specialized routine designed to scan data files and copy or</p>
<p>summarize data for use by another process.</p></td>
</tr>
<tr class="even">
<td>FACILITY NAME</td>
<td>Identification of VA health care facility admitting patient</td>
</tr>
<tr class="odd">
<td>FIELD</td>
<td><p>In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file’s data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that</p>
<p>particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</p></td>
</tr>
<tr class="even">
<td>FILE</td>
<td>A set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="odd">
<td>FILE MANAGER (VA FILEMAN)</td>
<td><p>The Database Management System (DBMS). The central component</p>
<p>of the Kernel that defines the way standard VistA files are structured and manipulated.</p></td>
</tr>
<tr class="even">
<td>FORCED QUEUING</td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device rejects it and prompts the user to queue the task instead.</td>
</tr>
<tr class="odd">
<td>FREE TEXT</td>
<td>The use of any combination of numbers, letters, and symbols when entering data.</td>
</tr>
<tr class="even">
<td>FTP</td>
<td>File Transfer Protocol</td>
</tr>
<tr class="odd">
<td>G&amp;L</td>
<td>Gains &amp; Loses</td>
</tr>
<tr class="even">
<td>GLOBAL VARIABLE</td>
<td>A variable that is stored on disk (M usage).</td>
</tr>
<tr class="odd">
<td>GO-HOME JUMP</td>
<td>A menu jump that returns the user to the Primary menu presented at sign-on. It is specified by entering two up-arrows (^^) at the menu’s select prompt. It resembles the rubber band jump but without an option specification after the up-arrows.</td>
</tr>
<tr class="even">
<td>HAO</td>
<td>Health Administration Office</td>
</tr>
<tr class="odd">
<td>HEC</td>
<td>Health Eligibility Center</td>
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
<td>Hospital Inquiry</td>
</tr>
<tr class="odd">
<td>HIPAA</td>
<td>Health Insurance Portability and Accountability Act</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>Health Level 7</td>
</tr>
<tr class="odd">
<td>IM/LTC</td>
<td>Intermediate Medicine/Long Term Care</td>
</tr>
<tr class="even">
<td>INPATIENT</td>
<td>A patient who has been admitted to a hospital in order to be treated for a particular condition.</td>
</tr>
<tr class="odd">
<td>IT</td>
<td>Information Technology</td>
</tr>
<tr class="even">
<td>KERNEL</td>
<td>A set of software routines that function as an intermediary between the host operating system and the application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td>KEY</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td>KEYWORD</td>
<td>A word or phrase used to call up several codes from the reference files in the LOCAL LOOK-UP file. One specific code may be called up by several different keywords.</td>
</tr>
<tr class="odd">
<td>LAYGO ACCESS</td>
<td>A user’s authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="even">
<td>LINK</td>
<td>Non-specific term referring to ways in which files may be related (via pointer links). Files have links into other files.</td>
</tr>
<tr class="odd">
<td>LOA</td>
<td>Line of Action</td>
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
<td>MANDATORY FIELD</td>
<td>This is a field that requires a value. A null response is not valid.</td>
</tr>
<tr class="odd">
<td>MENU</td>
<td>A list of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word “Select” and followed by the word “option” as in Select Menu Management option: (the menu’s select prompt).</td>
</tr>
<tr class="even">
<td>MENU CYCLE</td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. Menu Manager keeps track of information, such as the user’s place in the menu trees, according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="odd">
<td>MENU SYSTEM</td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="even">
<td>MENU TEMPLATE</td>
<td>An association of options as pathway specifications to reach one or more final destination options. The final options must be executable activities and not merely menus for the template to function. Any user may define user-specific menu templates via the corresponding Common option.</td>
</tr>
<tr class="odd">
<td>MENU TEXT</td>
<td>The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file. For example, User’s Toolbox is the menu text of the XUSERTOOLS option. The option’s synonym is TBOX.</td>
</tr>
<tr class="even">
<td>MHS</td>
<td>Military Health System</td>
</tr>
<tr class="odd">
<td>MOU</td>
<td>Memorandum of Understanding</td>
</tr>
<tr class="even">
<td>MTF</td>
<td>Military Treatment Facility</td>
</tr>
<tr class="odd">
<td>NHCU</td>
<td>Nursing Home Care Unit</td>
</tr>
<tr class="even">
<td>NIPRNET</td>
<td>Unclassified but Sensitive Internet Protocol Router Network</td>
</tr>
<tr class="odd">
<td>NPCD</td>
<td>National Patient Care Database</td>
</tr>
<tr class="even">
<td>NSC</td>
<td>Non-Service Connected</td>
</tr>
<tr class="odd">
<td>NUMERIC FIELD</td>
<td>A response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="even">
<td>OEF/OIF</td>
<td>Operation Enduring Freedom/Operation Iraqi Freedom</td>
</tr>
<tr class="odd">
<td>OI&amp;T</td>
<td>Office of Information &amp; Technology</td>
</tr>
<tr class="even">
<td>OIFO</td>
<td>Office of Information Field Office</td>
</tr>
<tr class="odd">
<td>OPERATING SYSTEM</td>
<td>A basic program that runs on the computer, controls the peripherals, allocates computing time to each user, and communicates with terminals.</td>
</tr>
<tr class="even">
<td>OPTION</td>
<td>An entry in the OPTION file. As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="odd">
<td>OPTION NAME</td>
<td>The Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text “Menu Management”). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="even">
<td>PACKAGE</td>
<td>The set of programs, files, documentation, help prompts, and installation procedures required for a given software application.</td>
</tr>
<tr class="odd">
<td>PAD</td>
<td>Patient Administration &amp; Discharge</td>
</tr>
<tr class="even">
<td>PAS</td>
<td>Program Application Specialist</td>
</tr>
<tr class="odd">
<td>PASSWORD</td>
<td>A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user’s identity.</td>
</tr>
<tr class="even">
<td>PHI</td>
<td>Protected Health Information</td>
</tr>
<tr class="odd">
<td>PII</td>
<td>Personal Identifiable Information</td>
</tr>
<tr class="even">
<td>PIMS</td>
<td>Patient Information Management System</td>
</tr>
<tr class="odd">
<td>PKI</td>
<td>Public Key Infrastructure</td>
</tr>
<tr class="even">
<td>POC</td>
<td>Point of Contact</td>
</tr>
<tr class="odd">
<td>POINTER</td>
<td>A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward).</td>
</tr>
<tr class="even">
<td>PRIMARY MENUS</td>
<td>The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by IRM. This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="odd">
<td><p>PRIVACY ACT INFORMATION</p>
<p>(PAI)</p></td>
<td>Information covered by and protected under the Privacy Act of 1974.</td>
</tr>
<tr class="even">
<td>PRODUCTION ACCOUNT</td>
<td>The UCI where users log on and carry out their work, as opposed to the manager or library account.</td>
</tr>
<tr class="odd">
<td>PROGRAM</td>
<td>A list of instructions written in a programming language and used for computer operations.</td>
</tr>
<tr class="even">
<td>PROMPT</td>
<td>The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="odd">
<td>PROTECTED HEALTH INFORMATION (PHI)</td>
<td>PHI is individually-identifiable health information maintained in any form or medium. Note: PHI excludes employment records held by a covered entity in its role as an employer.</td>
</tr>
<tr class="even">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="odd">
<td>QUEUING</td>
<td>Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). The Kernel’s Task Manager handles the queuing of tasks.</td>
</tr>
<tr class="even">
<td>QUEUING REQUIRED</td>
<td>An option attribute that specifies that the option must be processed by TaskMan (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified time periods.</td>
</tr>
<tr class="odd">
<td>READ ACCESS</td>
<td>A user’s authorization to read information stored in a computer file.</td>
</tr>
<tr class="even">
<td>RECORD</td>
<td>A set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="odd">
<td>RESOURCE</td>
<td>Sequential processing of tasks can be controlled through the use of resources. Resources are entries in the DEVICE file which must be allocated to a process(es) before that process can continue.</td>
</tr>
<tr class="even">
<td>RETURN</td>
<td>On the computer keyboard, the key located where the carriage return is on an electric typewriter. It is used in to terminate “reads.” Symbolized by &lt;RET&gt;.</td>
</tr>
<tr class="odd">
<td>SCREEN</td>
<td>A CRT, monitor or video display terminal</td>
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
<td><p>SENSITIVE</p>
<p>E-MAIL</p></td>
<td><p>In accordance with VA Handbook 6500 and associated appendices any email message containing sensitive information, which includes all patient information must be secured. VistA email in MailMan is no longer considered secured; Refer to your Information Security Officer (ISO) for additional information.</p>
<p>MS Outlook or Exchange is not considered secured by the Office of Cyber Security; therefore, any emails sent via Outlook cannot contain patient information unless the message is secure utilizing encryption, PKI.</p></td>
</tr>
<tr class="odd">
<td>SERVER</td>
<td>An entry in the OPTION file. An automated mail protocol that is activated by sending a message to a server at another location with the “S.server” syntax. This activity is specified in the OPTION file.</td>
</tr>
<tr class="even">
<td>SET OF CODES</td>
<td>Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="odd">
<td>SIGN-ON/SECURITY</td>
<td>The Kernel module that regulates access to the menu system. It performs a number of checks to determine whether access can be permitted at a particular time. A log of sign-ons is maintained.</td>
</tr>
<tr class="even">
<td><p>SITE MANAGER/</p>
<p>IRM CHIEF</p></td>
<td>At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules.</td>
</tr>
<tr class="odd">
<td>SM</td>
<td>Service Member</td>
</tr>
<tr class="even">
<td>SOURCE OF ADMISSION</td>
<td><p>Below are the 4 Sources of Admission &amp; their Codes that directly relate to this project:</p>
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 61%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td>2B</td>
<td>Military Pers not directly from Military Hospital</td>
<td>Hospital</td>
</tr>
<tr class="even">
<td>2C</td>
<td>Military Pers by Transfer from a Military Hospital</td>
<td>Hospital</td>
</tr>
<tr class="odd">
<td>7B</td>
<td>Direct Admission of Active Duty Pers from Military Hospital</td>
<td>CNH</td>
</tr>
<tr class="even">
<td>4M</td>
<td>From Military Hospital Domiciliary</td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>SPACEBAR RETURN</td>
<td>You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="even">
<td>SPECIAL QUEUING</td>
<td>An option attribute indicating that TaskMan should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td>SPOOLER</td>
<td><p>Spooling (under any system) provides an intermediate storage location for files (or program output) for printing at a later time.</p>
<p>In the case of VistA, the Kernel manages spooling so that the underlying OS mechanism is transparent. The Kernel subsequently transfers the text to the ^XMBS global for despooling (printing).</p></td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="odd">
<td>STOP CODE</td>
<td>A number (i.e., a subject area indicator) assigned to the various clinical, diagnostic, and therapeutic sections of a facility for reporting purposes. For example, all outpatient services within a given area (e.g., Infectious Disease, Neurology, and Mental Hygiene—Group) would be reported to the same clinic stop code.</td>
</tr>
<tr class="even">
<td>SYNONYM</td>
<td>A field in the OPTION file. Options may be selected by their menu text or synonym (see Menu Text).</td>
</tr>
<tr class="odd">
<td>TASKMAN</td>
<td>The Kernel module that schedules and processes background tasks (also called Task Manager).</td>
</tr>
<tr class="even">
<td>TEMPLATE</td>
<td>A means of storing report formats; data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file, print specifications are stored in the PRINT TEMPLATE file, and search or sort specifications are stored in the SORT TEMPLATE file.</td>
</tr>
<tr class="odd">
<td>HEALTH INSURANCE PORTABILITY AND ACCOUNTABILITY ACT (HIPAA)</td>
<td>This statute provides for the improvement of the efficiency and effectiveness of health care systems, by encouraging the development of health information systems through the establishment of standards and requirements for the electronic transmission, privacy and security of certain health information. VHA must comply with the Privacy Rules when creating, maintaining, using and disclosing individually identifiable health information (IIHI).</td>
</tr>
<tr class="even">
<td>TIMED-READ</td>
<td>The amount of time a READ command waits for a user response before it times out.</td>
</tr>
<tr class="odd">
<td>TREE STRUCTURE</td>
<td>A term sometimes used to describe the structure of an M array. This has the same structure as a family tree, with the root at the top and ancestor nodes arranged below according to their depth of subscripting. All nodes with one subscript are at the first level, all nodes with two subscripts at the second level, and so on.</td>
</tr>
<tr class="even">
<td>TRIGGER</td>
<td>A type of VA FileMan cross reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="odd">
<td>TYPE-AHEAD</td>
<td>A buffer used to store characters that are entered before the corresponding prompt appears. Type-ahead is a shortcut for experienced users who can anticipate an expected sequence of prompts.</td>
</tr>
<tr class="even">
<td>UP-ARROW JUMP</td>
<td>In the menu system, entering an up-arrow (^) followed by an option name accomplishes a jump to the target option without needing to take the usual steps through the menu pathway.</td>
</tr>
<tr class="odd">
<td>USER ACCESS</td>
<td><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="even">
<td>USER INTERFACE</td>
<td>The way the package is presented to the user—issuing of prompts, help messages, menu choices, etc. A standard user interface can be achieved by using VA FileMan for data manipulation, the menu system to provide option choices, and VA FileMan’s Reader, the ^DIR utility, to present interactive dialogue.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>The Department of Veterans Affairs, formerly called the Veterans Administration.</td>
</tr>
<tr class="even">
<td>VA FILEMAN</td>
<td>A set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A package of on-line computer routines written in the M language which can be used as a stand-alone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer stored files.</td>
</tr>
<tr class="odd">
<td>VERIFY CODE (SEE PASSWORD)</td>
<td>An additional security precaution used in conjunction with the Access Code. Like the Access Code, it is also 6 to 20 characters in length and, if entered incorrectly, will not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="even">
<td>VETERAN</td>
<td><p>A person who served in the active military, naval, or air service, and who was discharged or released from under conditions other than dishonorable.</p>
<p>--------------------------------------------------------------</p>
<p>An individual who served their full obligation of Active Duty service in the military, or received an early discharge for a medical condition, hardship, reduction in force, or at the convenience of the military. Individuals who received dishonorable discharges or who were still on Active Duty at the time of the survey were not eligible.</p></td>
</tr>
<tr class="odd">
<td>VETERANS BENEFITS ADMINISTRATION (VBA)</td>
<td>Provides benefits and services to the veterans and their families in a responsive, timely and compassionate manner in recognition of their service to the Nation. VBA has 57 Regional Offices providing benefits and services to over 2.8 million veterans.</td>
</tr>
<tr class="even">
<td>VETERANS HEALTH ADMINISTRATION (VHA)</td>
<td>The largest direct health care delivery system in the country, providing care at over 800 locations to about five million veterans.</td>
</tr>
<tr class="odd">
<td>VETERANS HEALTH INFORMATION SYSTEMS AND TECHNOLOGY ARCHITECTURE (VistA)</td>
<td>VistA is an enterprise-wide, fully integrated, fully functional information system built around an electronic health record. It is easily customizable and can be configured to fit any type of healthcare organization, from clinics and medical practices to nursing homes and large hospitals. VistA has been named one of the best healthcare information systems in the nation by the Institute of Medicine.<br />
<br />
Developed by the Department of Veterans Affairs, the VistA healthcare information system supports the hospitals and clinics serving veterans throughout the US. VistA has been deployed in thousands of healthcare facilities, both domestic and international</td>
</tr>
<tr class="even">
<td>VETERANS INTEGRATED SERVICE NETWORK (VISN)</td>
<td>The 21 VISNs are integrated networks of health care facilities that provide coordinated services to veterans to facilitate continuity through all phases of healthcare and to maximize the use of resources. (Medical Care)</td>
</tr>
<tr class="odd">
<td>WIA</td>
<td>Wounded in Action</td>
</tr>
<tr class="even">
<td>WW</td>
<td>Wounded Warrior</td>
</tr>
<tr class="odd">
<td>WWPMP</td>
<td>Wounded Warrior Pay Management Program</td>
</tr>
</tbody>
</table>