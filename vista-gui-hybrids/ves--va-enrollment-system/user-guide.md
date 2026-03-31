---
consolidated_title: "user guide ves"
app_code: VES
doc_type: UG
master_source: "User Guide VES 6.15"
master_pub_date: December 2025
consolidated_from: 19 versions
prior_versions:
  - "User Guide VES 6.0"
  - "User Guide VES 6.1"
  - "User Guide VES 6.10"
  - "User Guide VES 6.11"
  - "User Guide VES 6.12"
  - "User Guide VES 6.13"
  - "User Guide VES 6.14.5"
  - "User Guide VES 6.14"
  - "User Guide VES 6.2.2"
  - "User Guide VES 6.2"
  - "User Guide VES 6.3"
  - "User Guide VES 6.4"
  - "User Guide VES 6.5"
  - "User Guide VES 6.6"
  - "User Guide VES 6.7.1"
  - "User Guide VES 6.7"
  - "User Guide VES 6.8"
  - "User Guide VES 6.9"
---

Veterans Health Administration (VHA) Enrollment System (VES) 6.15.0

# User Guide

<!-- image -->

December 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

**NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       |   Revision | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Author   |
|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 12/30/2025 |         54 | **VES 6.15.0**  added the following:  - Project References updated, pg. 3 - **Update Document Management Options - Tribal Attestation Documents** - **VES Enable 60-Day Pre-Term for Deferred Veterans** - **Remove Dollar Amount Restriction for Annual Check Amount** - **Expire Hardships** - **Allow Saving of Tribal Affiliation Start Date in VES when Veteran is Deceased** - **Effective Date for VHAP Carveouts**  - Person Search Tabs → Document Management → Search Documents - Person Search Tabs → Document Management → Upload Documents  - Person Search Tabs → Communications → Available for Mailing  - Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility (Add a Person) - Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility - Person Search Tabs → Eligibility → Edit Current Eligibility → Prisoner of War  - Person Search Tabs → Financials → Financial Hardship → Financial Hardship Overview  - Person Search Tabs → Demographics → Overview - Person Search Tabs → Overview - Person Search Tabs → Demographics → Personal → Personal History - Person Search Tabs → Demographics → Personal - Person Search Tabs → Demographics → Personal → Personal (Add a Person)  - Menu Bar → Reference → VHA Profile - Person Search Tabs → Eligibility → VHA Profiles | BAHTW    |

Artifact Rationale

A User Guide is a required end-user document if pertinent to your product. The project manager, as the authoritative source and in consultation with the technical writer, determines if a User Guide is a required artifact for the product. The purpose of this document is to assist the intended audience, which includes all users of the system, interface, or application described within the document, such as VistA end-users. It should be updated to reflect the contents of the most recently deployed software. The sections documented herein are required if applicable to your product; additional sections can also be added as needed. It contains both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly.

Table of Contents

1	Introduction	1

1.1	Purpose	1

1.2	Overview	1

1.2.1	Release Updates and Enhancements	1

1.2.2	Organization of the Manual	2

1.2.3	Assumptions	2

1.2.4	Installation, Maintenance, &amp; Monitoring	2

1.2.5	Disclaimers	2

1.2.5.1	Software Disclaimer	2

1.2.5.2	Documentation Disclaimer	3

1.2.6	References and Resources	3

2	System Summary	3

2.1	System Design Document	3

2.2	User Access Levels	3

2.3	ESM Application Information System Contingency Plan	3

2.4	ESM Project Artifacts (VDL)	4

3	Getting Started	4

3.1	VES Layout	4

3.2	VES Online Help	6

3.3	508 Compliance &amp; Accessibility	9

3.3.1	Accessibility Software	9

3.4	Standard Data Service (SDS) Lookup Tables	10

3.5	Exiting VES	10

3.6	Caveats and Exceptions	10

4	Significant Additions and Updates to VES Version 6.15.0	11

4.1.1	Person Search Tabs → Document Management → Search Documents	11

4.1.2	Person Search Tabs → Document Management → Upload Documents	11

4.2	VES Enable 60-Day Pre-Term for Deferred Veterans	12

4.2.1	Person Search Tabs → Communications → Available for Mailing	12

4.3	Remove Dollar Amount Restriction for Annual Check Amount	14

4.3.1	Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility (Add a Person)	14

4.3.2	Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility	14

4.3.3	Person Search Tabs → Eligibility → Edit Current Eligibility → Prisoner of War	15

4.4	Expire Hardships	16

4.4.1	Person Search Tabs → Financials → Financial Hardship → Financial Hardship Overview	16

4.5	Allow Saving of Tribal Affiliation Start Date in VES when Veteran is Deceased	16

4.5.1	Person Search Tabs → Demographics → Overview	16

4.5.2	Person Search Tabs → Overview	18

4.5.3	Person Search Tabs → Demographics → Personal → Personal History	20

4.5.4	Person Search Tabs → Demographics → Personal	22

4.5.5	Person Search Tabs → Demographics → Personal → Personal (Add a Person)	25

4.6	Effective Date for VHAP Carveouts	30

4.6.1	Menu Bar → Reference → VHA Profile	30

4.6.2	Person Search Tabs → Eligibility → VHA Profiles	30

List of Figures

Figure 1: Menu Bar	4

Figure 2: Summary with a Sensitive Record	5

Figure 3: Person Search Tabs	5

Figure 4: Summary and Main Screen on VES	5

Figure 5: Sorting Columns	6

Figure 6: System Help and Screen Help	6

Figure 7: SDS Lookup Table	10

Figure 8: Tribal Attestation Documents Section (Search)	11

Figure 9: Tribal Attestation Documents Section (Upload)	12

Figure 10: Added TERA Initial Letter	13

Figure 11: Added TERA Initial Letter (Final Letters)	13

Figure 12: Annual Check Amount Rules (Add a Person)	14

Figure 13: Annual Check Amount Rules	15

Figure 14: Annual Check Amount Rules (POW)	15

Figure 15: American Indian/Alaska Native Overview Updates	17

Figure 16: American Indian/Alaska Native Overview Updates 2	17

Figure 17: Updated Screenshot - Demographics Overview	18

Figure 18: American Indian/Alaska Native - Main Overview Updates	19

Figure 19: American Indian/Alaska Native - Main Overview Updates 2	19

Figure 20: Updated Screenshot - Main Overview	20

Figure 21: Updated Screenshot - Personal History	21

Figure 22: American Indian/Alaska Native Personal History	21

Figure 23: Updated Screenshot - Personal Section	22

Figure 24: Updated American Indian/Alaska Native Personal Tab Text Update	23

Figure 25: Updated American Indian/Alaska Native Personal Tab Text Update 2	24

Figure 26: Personal Add a Person Updated Screenshot	25

Figure 27: American Indian/Alaska Native Updates - Personal (Add a Person)	26

Figure 28: American Indian/Alaska Native Updates - Personal (Add a Person) 2	27

Figure 29: American Indian/Alaska Native Updates - Personal (Add a Person) 3	28

Figure 30: American Indian/Alaska Native Updates - Personal (Add a Person) 4	29

Figure 31: VHAP Carveout - Updated Text	30

Figure 32: VHA Profiles Assigned – Unselect to Unassign - Updated Text	31

Figure 33: VHAP Effective Date	31

Figure 34: Add VHAP Effective Date to E&amp;E Service	32

## Introduction

The Veterans Health Administration (VHA) Enrollment System (VES) is the primary Veterans Affairs (VA) system used to manage VA health benefits.

VES allows staff at the Health Eligibility Center (HEC), located in Atlanta, Georgia, to work more efficiently and determine patient eligibility in a timelier manner. Messaging with the VAMC (Department of Veterans Affairs Medical Center) allows for the adding and updating of beneficiary records to the enterprise enrollment system to be shared with the field.

VES is one component of the "system of systems" needed to implement the VistA/GUI Hybrids (formerly Health *e* Vet) REE (Registration, Eligibility &amp; Enrollment) environment.

VES’s two main functions are:

- Expert System (Messaging) provides a seamless bi-directional interface with external Veterans Health Administration (VHA) and non-VHA systems for data exchange of Veterans’ information.
- Workflow (Case Management) that provides authorized VHA case representatives at the HEC and VAMC with a web interface to easily track, maintain, and manage cases associated with Veteran benefits. HEC and VAMC staff utilize VES to manage these "cases" to completion so that verified Eligibility &amp; Enrollment can be determined.

### Purpose

The purpose of this user guide is to familiarize users with important features and navigational elements of the VES application.

### Overview

President George W. Bush established a task force for returning Global War on Terror (GWOT) heroes who resulted in enhancements that improved delivery of Federal services and benefits to GWOT service members and Veterans. Among recommendations associated with task force was to focus on enhancing delivery of services and information to GWOT service members and Veterans within existing authority and resource levels.

#### Release Updates and Enhancements

Identify the roles for which this guide was written, and the job functions it addresses. Click the [link](https://ves.va.gov/esr/webhelp/esr_help_project.htm) to view current and past VES release updates and enhancements on the Online Help.

#### Organization of the Manual

This Quick Start User Guide contains the following:

- Introduction
- System Summary
- Getting Started
- Significant Additions and Updates to VES Version
- Troubleshooting

#### Assumptions

This quick start was written with the following assumed experience/skills of the audience:

- User has basic knowledge of VES (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for VES.
- User is using VES to do their job.
- User has validated access to VES.
- User has completed any prerequisite training.

#### Installation, Maintenance, &amp; Monitoring

Installation, maintenance, and monitoring of VES updates are performed at the Austin Information Technology Center (AITC) on the third Saturday of each month.

#### Disclaimers

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

This manual provides an overall explanation and functionality of Veterans Health Administration (VHA) Enrollment System (VES) 6.15.0.

<!-- image -->

DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

#### References and Resources

Refer to the following VES references:

- VES 6.15.0 Release Notes
- VES 6.15.0 Online Help

## System Summary

Users require group membership to access SharePoint and Teams’ links. To request access, contact the E&amp;E Program Management Office (PMO) or use the request access option at the SharePoint site and specify group membership.

### System Design Document

Please refer to the System Design Document (SDD). Please submit a [ServiceNow](https://yourit.va.gov/va) ticket to the NTL MNT EDB/ESR group for access to the SDD.

### User Access Levels

See the **Buttons/Admin** section where **User Accounts** , **Profiles** , **Roles** and **Capability Sets** explain the different user access levels of the VES.

### ESM Application Information System Contingency Plan

The Enrollment System Modernization (ESM) Application Information System Contingency Plan is stored in eMASS and is available upon request. Please submit a [ServiceNow](https://yourit.va.gov/va) ticket to the NTL MNT EDB/ESR group for access.

### ESM Project Artifacts (VDL)

Click the following [link](https://www.va.gov/vdl/section.asp?secid=4) to access the ESM Project Artifacts located in the VA Software Document Library (VDL). Scroll down to VA Enrollment System (VES) to access VES artifacts.

## Getting Started

### VES Layout

VES displays a beneficiary's record data. The "Menu Bar" and the "Person Search Tabs" provide access to various screens for viewing, updating, adding, and deleting information on VES.

Menu Bar

Menu Bar is where utility buttons for VES are located.

From the Menu Bar, users view Worklists, perform Veteran Merges, perform Health Level 7 (HL7), Community Care Network (CCN), Third-Party Administrator (TPA) and Military Service Data Sharing (MSDS) Message Searches, Load Registries, do an Undeliverable Mail Search, Generate/View Reports, Reference Thresholds/Enrollment Group Threshold (EGT) Settings, view Veterans Online Application (VOA) Re-submissions, Search and Add a New Person, and perform general Administrative functions such as enable or disable Veterans Community Care Eligibility (VCE) parameters.

<!-- image -->

Figure 1: Menu Bar

Summary

The Summary displays the beneficiary's Name, social security number (SSN), date of birth (DOB), date of death (DOD), Enrollment Status, Member ID (if available), and any other important information such as Open Work Items, Pending Merges, Sensitive Records, etc.

Sensitive Record information, if disclosed to the individual, may have serious adverse effects on the individual's mental or physical health. Such information may require explanation or interpretation by an intermediary or assistance in the information's acceptance and assimilation in order to preclude adverse impacts on the individual's mental or physical health.

<!-- image -->

Figure 2: Summary with a Sensitive Record

Person Search Tabs

Person Search Tabs are the area of the screen where the user may access the various kinds of information on record for the beneficiary to aid in determining his or her eligibility for enrollment in the VA healthcare system.

<!-- image -->

Figure 3: Person Search Tabs

The terms [Veteran](javascript:hhctrl.TextPopup('A%20veteran%20is%20a%20person%20who%20has%20served%20in%20the%20armed%20forces.','Arial,10',10,10,00000000,0xffffff)) , [beneficiary](javascript:hhctrl.TextPopup('A%20beneficiary%20is%20one%20that%20receives%20a%20benefit%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)) , [patient](javascript:hhctrl.TextPopup('A%20patient%20is%20one%20who%20receives%20medical%20attention,%20care,%20or%20treatment.','Arial,10',10,10,00000000,0xffffff)) , and [applicant](javascript:hhctrl.TextPopup('An%20applicant%20is%20one%20that%20applies%20for%20benefits%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)) are used interchangeably throughout VES. While not all applicants are Veterans or patients, not all applicants are beneficiaries either. Whether they are a Veteran, patient or beneficiary is determined AFTER the application for benefits is received and processed.

<!-- image -->

Figure 4: Summary and Main Screen on VES

**Sorting Columns**

<!-- image -->

For screens that contain listed data, ascending and descending sorting may be performed for any category by clicking on the category name or on the symbol . Re-clicking the category name or symbol re-sorts the previous sort.

<!-- image -->

Figure 5: Sorting Columns

**VES Online Help** is an Online Help system built in Adobe RoboHelp, an authoring and publishing tool. The VES Online Help delivers an output to VES users when clicking the context-sensitive help buttons, **System Help** or **Screen Help** .

### VES Online Help

<!-- image -->

In VES, you can obtain information about windows or dialogs clicking the context-sensitive help button available VES in the upper right-hand corner of the “System Help” and “Screen Help”.

**System Help:**

<!-- image -->

System Help is the top upper-right context-sensitive help button .

**Screen Help:**

<!-- image -->

Screen Help is the lower upper-right context-sensitive help button .

If you roll over the Help icons in VES, screen tips will appear distinguishing between “System Help” and “Screen Help”.

<!-- image -->

Figure 6: System Help and Screen Help

**VES Online Help Tool Bar**

To the left of the VES Online Help, above the table of contents pane, a tool bar contains ***Contents, Index, Search*** and ***Glossary*** links.

<!-- image -->

Table of Contents:

Contents displays an expanded table of contents.

<!-- image -->

<!-- image -->

- Collapse / Expand (,  )
<!-- image -->

<!-- image -->
- Topics () are categories of information in the VES Online Help. Clicking, you can view the contents of topic in the main screen located to the right.
<!-- image -->

Index:

Index displays a multi-level list of keywords and keyword phrases. These terms are associated with topics in the VES Online Help, and the keywords are intended to direct you to specific topics within the VES Online Help. Click the keyword to launch a topic from the TOC to the main screen. If the keyword is used with more than one topic, a list of topics displays under the keyword or keyword phrase in which the keyword or keyword phrase appears.

<!-- image -->

Search:

Search provides a way to explore the content of the VES Online Help and find matches to VES-defined words. Unlike Index that lists author-defined keywords such as terms, synonyms, and cross-references, Search lists words used within the content of topics. To find a topic in which the word appears, click the letter link to display the words that begin with the letter being searched for. Words that appear once are in bold. Words that appear in multiple topics are listed with numbers. Click on a number to display the topic in the right-hand pane in which the word appears.

<!-- image -->

Glossary:

Glossary provides a list of terms and definitions related to the subject-matter in VES. Click a letter in the top pane and see corresponding definitions that begin with the letter clicked in the lower pane.

The VES Online Help uses Adobe RoboHelp’s 2017 WebHelp as its output and is 508-compliant. The Online Help opens in your web browser as a new window.

**Other buttons and functions**

**Hide/Show the left pane**

Provides a larger viewing area of the open topic and hides the left pane.

Click the **Hide** link in the upper left side of the right pane to hide the left pane.

Click the **Show** link in the upper left side of the pane to show the left pane.

**Browser Toolbar**

Since there is not a browser toolbar at the top of the VES Online Help window, right-click within VES Online Help window and select either **Back** or **Forward** to go back and forward through the history of visited topics, print a topic, or perform other tasks available within the Windows context-sensitive commands.

The **Forward** command is only available if the **Back** command has been used first. At that point the **Forward** command becomes available.

The TOC on the left side of the VES Online Help can also be used to navigate throughout the VES Online Help.

**WebHelp Build Date**

Click the **Systems Parameters** topic to view the WebHelp Build Date. The build date is next to the topic title.

**Adjusting the main screen and TOC size**

Adjust the width and height of the main screen window by dragging the edges of the window in or out.

<!-- image -->

Adjust the width of the table of contents pane by pointing to the right edge of the left pane until the mouse pointer turns into a line with arrows on each end:   Drag the pane to the right or left with the left mouse button held down.

**Navigating Help Topics**

The following navigational techniques generally refer to the Online Help, where indicated, and not the written documentation:

**Links (Online Help)**

***** symbol indicates a required field in the Online Help.

<!-- image -->

symbol indicates a required field in the user guide.

<!-- image -->

symbol is displayed when a submitted field has an error.

<!-- image -->

symbol ("data changed") is displayed when a type of data has changed on the *History* , *Veteran Merge* , and user-related confirmation windows.

Indicates a note or item of special interest.

### 508 Compliance &amp; Accessibility

With every release, the Department of Veterans Affairs strives to improve accessibility in VES through the World Wide Web Consortium (W3C)’s Web Content Accessibility Guidelines (WCAG) 2.0, Levels A and AA.

<!-- image -->

<!-- image -->

<!-- image -->

It's important to mention that because Adobe RoboHelp displays a leveled hierarchy of contents through expanded and collapsed icons. VES users must click the collapsed icon to display contentsfor that section and re-click the expanded  icon to close the contents of that section.

Simple interface patterns that allow you to expand and collapse content can be helpful accessibility aids as they give users the choice of revealing content to read it, or bypassing the content, making page navigation more efficient for screen-reader users and people using the keyboard or alternative input devices.

#### Accessibility Software

The table below lists accessibility software used to assist disabled users with VES.

Table 1: Accessibility Software

| **Accessibility Software**    | **Description**                                                                                                                    | **Keyboard Shortcuts**                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| Jaws (Job Access with Speech) | Assists blind and visually impaired Veterans with reading screens on VES either with a text-to-speech output or a Braille display. | JAWS Keystrokes                             |
| ZoomText Magnifier / Reader   | Magnifies VES screens to varying levels and assists Veterans with screen reading.                                                  | ZoomText Tutorial                           |
| Dragon Naturally Speaking     | Through dictating VES functions, assists disabled Veterans with VES document downloads  and exports.                               | Dragon NaturallySpeaking User Documentation |

If you have questions or comments regarding Adobe RoboHelp 2022 accessibility, please contact the [Adobe Accessibility Team](https://www.adobe.com/accessibility/feedback.html) and provide feedback on their feedback form. For further information on Adobe accessibility, please refer to the following link:

[https://www.adobe.com/accessibility/508standards.html](https://www.adobe.com/accessibility/508standards.html)

### Standard Data Service (SDS) Lookup Tables

The SDS is a repository of enterprise-level reference tables. The SDS Lookup Tables contain information needed to define requirements and research the E&amp;E process. The SDS Lookup Tables page enables a user to view information about a specific table (for example, table name, code, description, active status, date when a code became inactive). VES uses SDS tables in several of its applications.

Users access the SDS Lookup Tables screen by clicking the Reference Tables link at the top right of any VES screen.

To display the SDS Lookup Tables:

1. Click the Reference Tables link and the SDS Lookup Tables page displays. SDS table and SDS History table names are listed in alphabetical order in the Navigation Bar.

Select an SDS table name from the navigation bar. The right panel displays the first five columns in the selected table and the Table Name contains a link for downloading the whole table as an Excel spreadsheet.   The Excel spreadsheet will display all the columns in the table.

<!-- image -->

Figure 7: SDS Lookup Table

*No data found for the selected table* displays if there is no data in an SDS Lookup Table.

### Exiting VES

To exit VES, click on the **Sign Out** link at the top of any page.

### Caveats and Exceptions

None.

## Significant Additions and Updates to VES Version 6.15.0

Please refer to VES 6.15.0 additions below in the Online Help.
Update Document Management Options - Tribal Attestation Documents

#### Person Search Tabs → Document Management → Search Documents

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                    |
|          2 | Click the  **Document Management**  section.                                                                               |
|          3 | Click the  **Search Documents**  section.                                                                                  |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 8: Tribal Attestation Documents Section (Search) |

#### Person Search Tabs → Document Management → Upload Documents

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                    |
|          2 | Click the  **Document Management**  section.                                                                               |
|          3 | Click the  **Upload Documents**  section.                                                                                  |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 9: Tribal Attestation Documents Section (Upload) |

### VES Enable 60-Day Pre-Term for Deferred Veterans

#### Person Search Tabs → Communications → Available for Mailing

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                       |
|          2 | Click the  **Communications**  section.                                                                                                                                       |
|          3 | Click the  **Available for Mailing**  section.                                                                                                                                |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 10: Added TERA Initial Letter  <!-- image -->  Figure 11: Added TERA Initial Letter (Final Letters) |

### Remove Dollar Amount Restriction for Annual Check Amount

#### Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                |
|          2 | Click the  **Eligibility**  section.                                                                                   |
|          3 | Click the  **Edit Current Eligibility**  section.                                                                      |
|          4 | Click the  **Edit Current Eligibility (Add a Person)**  section.                                                       |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 12: Annual Check Amount Rules (Add a Person) |

#### Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                              |
|------------|-----------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help. |
|          2 | Click the  **Eligibility**  section.                                                    |
|          3 | Click the  **Edit Current Eligibility**  section.                                       |
|          4 | Confirm the following information has been added:  <!-- image -->                       |

<!-- image -->

#### Person Search Tabs → Eligibility → Edit Current Eligibility → Prisoner of War

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                    |
|------------|---------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                       |
|          2 | Click the  **Eligibility**  section.                                                                          |
|          3 | Click the  **Edit Current Eligibility**  section.                                                             |
|          4 | Click the  **Prisoner of War**  section.                                                                      |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 14: Annual Check Amount Rules (POW) |

### Expire Hardships

#### Person Search Tabs → Financials → Financial Hardship → Financial Hardship Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                              |
|------------|-----------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help. |
|          2 | Click the  **Financials**  section.                                                     |
|          3 | Click the  **Financial Hardship**  section.                                             |
|          4 | Click the  **Financial Hardship Overview**  section                                     |
|          5 | Confirm the following information has been added:  <!-- image -->                       |

### Allow Saving of Tribal Affiliation Start Date in VES when Veteran is Deceased

#### Person Search Tabs → Demographics → Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                       |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                          |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                            |
|          3 | Click the  **Overview**  section.                                                                                                                                                                                                                                                |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 15: American Indian/Alaska Native Overview Updates  <!-- image -->  Figure 16: American Indian/Alaska Native Overview Updates 2  <!-- image -->  Figure 17: Updated Screenshot - Demographics Overview |

#### Person Search Tabs → Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                |
|          2 | Click the  **Overview**  section.                                                                                                                                                                                                                                                      |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure 18: American Indian/Alaska Native - Main Overview Updates  <!-- image -->  Figure 19: American Indian/Alaska Native - Main Overview Updates 2  <!-- image -->  Figure 20: Updated Screenshot - Main Overview |

#### Person Search Tabs → Demographics → Personal → Personal History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                        |
|          2 | Click the  **Demographics**  section.                                                                                                                                                          |
|          3 | Click the  **Personal**  section.                                                                                                                                                              |
|          4 | Click the  **Personal History**  section.                                                                                                                                                      |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 21: Updated Screenshot - Personal History  <!-- image -->  Figure 22: American Indian/Alaska Native Personal History |

#### Person Search Tabs → Demographics → Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                  |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                                     |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                       |
|          3 | Click the  **Personal**  section.                                                                                                                                                                                                                                                                           |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 23: Updated Screenshot - Personal Section  <!-- image -->  Figure 24: Updated American Indian/Alaska Native Personal Tab Text Update  <!-- image -->  Figure 25: Updated American Indian/Alaska Native Personal Tab Text Update 2 |

#### Person Search Tabs → Demographics → Personal → Personal (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|          3 | Click the  **Overview**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 26: Personal Add a Person Updated Screenshot  <!-- image -->  Figure 27: American Indian/Alaska Native Updates - Personal (Add a Person)  <!-- image -->  Figure 28: American Indian/Alaska Native Updates - Personal (Add a Person) 2  <!-- image -->  Figure 29: American Indian/Alaska Native Updates - Personal (Add a Person) 3  <!-- image -->  Figure 30: American Indian/Alaska Native Updates - Personal (Add a Person) 4 |

### Effective Date for VHAP Carveouts

#### Menu Bar → Reference → VHA Profile

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                    |
|          2 | Click the  **Menu Bar**  section.                                                                          |
|          3 | Click the  **Reference**  section.                                                                         |
|          4 | Click the  **VHA Profile**  section                                                                        |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 31: VHAP Carveout - Updated Text |

#### Person Search Tabs → Eligibility → VHA Profiles

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                          |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                             |
|          4 | Click the  **VHA Profiles**  section                                                                                                                                                                                                                             |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 32: VHA Profiles Assigned – Unselect to Unassign - Updated Text  <!-- image -->  Figure 33: VHAP Effective Date  <!-- image -->  Figure 34: Add VHAP Effective Date to E&amp;E Service |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: User Guide VES 6.8

### VES Communication History For Letters

#### Person Search Tabs → Communications → Previously Mailed

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                   |
|          2 | Click the  **Communications**  section.                                                                  |
|          3 | Click the  **Previously Mailed**  section                                                                |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure : Enable Communication History |

#### Communication → Previously Mailed → Letter Mailed on Behalf of Veteran → Status History

Confirm the following updates to the VES Enrollment System.

|   **Step** | **Action**                                                                                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Communication**  tab in the VHA Enrollment System (VES).                                                                                           |
|          2 | Click the  **Previously Mailed**  section.                                                                                                                      |
|          3 | Navigate to the  **Letter Mailed on Behalf of Veteran**  section and click the hyperlink under  **Name**  .                                                     |
|          4 | Navigate to the  **Status History**  section.                                                                                                                   |
|          5 | Confirm the panel includes the name of the requesting person or process under the new "Mailed By" column.  <!-- image -->  Figure : Previously Mailed/Mailed By |

#### VES VHAP Updates for SERVICE Act, TERA Indicator &amp; COMPACT Act

#### 4.2.1 Menu Bar  → Reference→ Core VHAPs

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu**  section on the table of contents on the Online Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|          2 | Click the  **Reference**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          3 | Click the  **Core VHAPs**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          4 | Confirm the following sections have been added and that the information is accurate:  **Veteran Full Med Benefits Tx and Rx Copay Req 8 (219) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx and Rx Copay Req 8 (219) Description  **Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216) Description  **Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217) Description  **Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description  <!-- image -->  Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description (con.)  **Veteran Full Med Benefits Tx and Rx Copay Exmt 6 (241) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt 6 (241) Description  **Veteran Full Med Benefits Tx and Rx Copay Req 6 (218) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx and Rx Copay Req 6 (218) Description  **Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description (con.)  **Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req 6 (242) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req 6 (242) Description  **Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215) Description  **Veteran Full Med Benefits Tx GMT and Rx Copay Req 6 (240) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx GMT and Rx Copay Req 6 (240) Description  **Veteran Full Med Benefits Tx GMT Copay Req and Copay Exmt 6 (239) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx GMT Copay Req and Copay Exmt 6 (239) Description  **Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220) Description  **Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221) Description:**  <!-- image -->  Figure : Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221) Description |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

#### 4.2.2 Person Search Tabs  → Eligibility → Primary and Secondary Eligibility Codes

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                          |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                              |
|          2 | Click the  **Eligibility**  section.                                                                                                                                |
|          3 | Click the  **Primary and Secondary Eligibility Codes**  section.                                                                                                    |
|          4 | Scroll down and confirm that the following excerpt has been added:  <!-- image -->  Figure : SERVICE ACT &amp; Recalculate Eligibility for Existing Veteran Records |

### VES Update SIGI Values &amp; 10-10EZ/EZR Forms

#### Person Search Tabs → Eligibility → Financials → Dependents → Add Edit Spouse→ Add Dependent Spouse

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                   |
|          2 | Click the  **Eligibility**  section.                                                                                     |
|          3 | Click the  **Financials**  section.                                                                                      |
|          4 | Click the  **Dependents**  section.                                                                                      |
|          5 | Click the  **Add Edit Spouse**  section.                                                                                 |
|          6 | Click the  **Add Dependent Spouse**  section.                                                                            |
|          7 | Confirm the  **Self-Identified Gender Identity**  dropdown is present:  <!-- image -->  Figure : SIGI Dropdown Help Text |

<!-- image -->

#### Person Search Tabs → Eligibility → Financials → Dependents → Add Edit Spouse→ Edit Dependent Spouse

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                   |
|          2 | Click the  **Eligibility**  section.                                                                                     |
|          3 | Click the  **Financials**  section.                                                                                      |
|          4 | Click the  **Dependents**  section.                                                                                      |
|          5 | Click the  **Add Edit Spouse**  section.                                                                                 |
|          6 | Click the  **Edit Dependent Spouse**  section.                                                                           |
|          7 | Confirm the  **Self-Identified Gender Identity**  dropdown is present:  <!-- image -->  Figure : SIGI Dropdown Help Text |

<!-- image -->

#### Financials → Dependents → ADD SPOUSE→ Self-Identified Gender Identity

Confirm the following updates to the VES Enrollment System.

|   **Step** | **Action**                                                                                                                       |
|------------|----------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Financial**  tab in the VHA Enrollment System (VES).                                                                |
|          2 | Click the  **Dependents**  section.                                                                                              |
|          3 | Click the  **ADD SPOUSE**  button.                                                                                               |
|          4 | Confirm the  **Self-Identified Gender Identity**  dropdown is present:  <!-- image -->  Figure : Self-Identified Gender Identity |

### From: User Guide VES 6.5

### Extend Combat Veteran Eligibility End Date

#### Person Search Tabs →  Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          2 | Click the  **Military Service**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          3 | Confirm the updated  **Military Service**  screen shot is correct and accurate. The Service Separation Date has been updated from 11/11/98 to 09/30/2013.  <!-- image -->  Figure : Service Separation Date (Military Service)  Confirm that the updated requirements text in the  **Combat Veteran Eligibility End Date**  section is accurate and correct. This text has been added to further detail the requirements for each priority group for the Combat Veteran Eligible population.  <!-- image -->  Figure : Updated Combat Veteran Eligibility End Date Help Text |

### Add Agent Orange and Ionizing Radiation Exposure Locations in VES

#### Person Search Tabs  → Eligibility → Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                  |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                    |
|          3 | Scroll down to the  **Reason Eligibility Status is Pending Verification**  information and verify that the included information is correct.  <!-- image -->  Figure : Reason Eligibility Status is Pending Verification |

#### Person Search Tabs  → Eligibility → Eligibility History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                  |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                    |
|          3 | Click the  **Eligibility History**  section.                                                                                                                                                                            |
|          4 | Scroll down to the  **Reason Eligibility Status is Pending Verification**  information and verify that the included information is correct.  <!-- image -->  Figure : Reason Eligibility Status is Pending Verification |

#### Person Search Tabs  → Eligibility → Current Eligibility → Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                         |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                                           |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                                                                                                   |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                                                                                                                                              |
|          5 | Scroll down to the  **Agent Orange Exposure Location**  definition and information and then to the  **Radiation Exposure Method**  definition and information directly below.                                                                                                                  |
|          6 | Confirm the added  **Agent Orange Exposure Location**  information and the added  **Radiation Exposure Method**  information and screen shots are correct and accurate.  <!-- image -->  Figure : Agent Orange Exposure Location List  <!-- image -->  Figure : Radiation Exposure Method List |
|          7 | Scroll down to the  **Reason Eligibility Status is Pending Verification**  information and verify that the included information is correct.  <!-- image -->  Figure 14: Reason Eligibility Status is Pending Verification                                                                      |
|          8 | Scroll down to the  **Eligibility Reason Status Codes**  table and verify that the included information is correct.  <!-- image -->  Figure 15: Eligibility Reason Status Codes                                                                                                                |

#### Person Search Tabs  → Eligibility → Current Eligibility → Edit Currently Eligibility (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                         |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                                           |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                                                                                                   |
|          4 | Click the  **Edit Current Eligibility (Add a Person)**  section.                                                                                                                                                                                                                               |
|          5 | Scroll down to the  **Agent Orange Exposure Location**  definition and information and then to the  **Radiation Exposure Method**  definition and information directly below.                                                                                                                  |
|          6 | Confirm the added  **Agent Orange Exposure Location**  information and the added  **Radiation Exposure Method**  information and screen shots are correct and accurate.  <!-- image -->  Figure : Agent Orange Exposure Location List  <!-- image -->  Figure : Radiation Exposure Method List |
|          7 | Scroll down to the  **Eligibility Reason Status Codes**  table and verify that the included information is correct.  <!-- image -->  Figure 18: Eligibility Reason Status Codes                                                                                                                |

#### Person Search Tabs  → Eligibility → Edit Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                                                             |
|          2 | Click the  **Eligibility**  tab.                                                                                                                                                                                                                     |
|          3 | Click the  **Edit Eligibility**  tab.                                                                                                                                                                                                                |
|          4 | Scroll down and click  **Other Eligibility Factors.**                                                                                                                                                                                                |
|          5 | Click the dropdown menu for  **Agent Orange Exposure Location.**                                                                                                                                                                                     |
|          6 | Confirm the added  **Agent Orange Exposure Locations**  are correct and confirm the updated  **Agent Orange Exposure Location**  screen shot is accurate.  <!-- image -->  Figure : Agent Orange Exposure Location Drop-Down Menu (Edit Eligibility) |

|   **Step** | **Action**                                                                                                                                                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                                              |
|          2 | Click the  **Eligibility**  tab.                                                                                                                                                                                                      |
|          3 | Click the  **Edit Eligibility**  tab.                                                                                                                                                                                                 |
|          4 | Scroll down and click  **Other Eligibility Factors.**                                                                                                                                                                                 |
|          5 | Click the dropdown menu for  **Radiation Exposure Method.**                                                                                                                                                                           |
|          6 | Confirm the added  **Radiation Exposure Methods**  are correct and confirm the updated  **Radiation Exposure Method**  screen shot is accurate.  <!-- image -->  Figure : Radiation Exposure Method Drop-Down Menu (Edit Eligibility) |

#### Person Search Tabs  → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                                                 |
|          2 | Click the  **Military Service**  tab.                                                                                                                                                                                                    |
|          3 | Scroll down to the  **Agent Orange Exposure Location.**                                                                                                                                                                                  |
|          4 | Confirm the added  **Agent Orange Exposure Locations**  and confirm the updated  **Agent Orange Exposure Location**  screen shot is accurate.  <!-- image -->  Figure : Agent Orange Exposure Location Drop-Down Menu (Military Service) |

|   **Step** | **Action**                                                                                                                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                                   |
|          2 | Click the  **Military Service**  tab.                                                                                                                                                                                      |
|          3 | Scroll down to the  **Radiation Exposure Method.**                                                                                                                                                                         |
|          4 | Confirm the added  **Radiation Exposure Methods**  and confirm the updated  **Radiation Exposure Methods**  screen shot is accurate.  <!-- image -->  Figure : Radiation Exposure Method Drop-Down Menu (Military Service) |

#### Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                           |
|          2 | Click the  **Military Service**  tab.                                                                                                                                                                              |
|          3 | Scroll down to the  **Military Service Episodes – HEC.**                                                                                                                                                           |
|          4 | Click “Delete” which will prompt the following pop-up:  <!-- image -->  Figure : MSE Information Deletion Pop-Up                                                                                                   |
|          5 | Click “OK” on the pop-up and then scroll down to the bottom and click the “Update” option. Confirm that the following pop-up will now appear:  <!-- image -->  Figure : MSE Information Deletion and Update Pop-Up |

#### Person Search Tabs  → Enrollment → Current Enrollment

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                      |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                          |
|          2 | Click the  **Enrollment**  tab.                                                                                                                                                                 |
|          3 | Click the  **Current Enrollment**  tab.                                                                                                                                                         |
|          4 | Scroll down to the  **Source of Enrollment**  section.                                                                                                                                          |
|          5 | Confirm the added  **Source of Enrollment**  information and screen shot are correct and accurate.  <!-- image -->  Figure : Agent Orange and Ionizing Radiation Factors (Source of Enrollment) |

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                      |
|          2 | Click the  **Enrollment**  tab.                                                                                                                                                                                                             |
|          3 | Click the  **Current Enrollment**  tab.                                                                                                                                                                                                     |
|          4 | Scroll down to the  **Enrollment Statuses**  section.                                                                                                                                                                                       |
|          5 | Confirm the added  **Pending; Proof of PACT Act**  information added to the Enrollment Status table and the provided screen shot are correct and accurate.  <!-- image -->  Figure : Pending; Proof of PACT Act (Enrollment Statuses Table) |

#### Person Search Tabs  → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                       |
|          2 | Click the  **Military Service**  tab.                                                                                                                                                                                                                                        |
|          3 | Scroll down to the  **Agent Orange**  &amp;  **Radiation Exposure Method**  sections.                                                                                                                                                                                        |
|          4 | Confirm the added  **Agent Orange**  &amp;  **Radiation Exposure Method**  information is correct and accurate.  <!-- image -->  Figure : Agent Orange Exposure Location List (Military Service)  <!-- image -->  Figure : Radiation Exposure Method List (Military Service) |

## Troubleshooting

### National Service Desk and Other Contacts

Table 2: Support Contact Information

| **Name**                  | **Org**   | **Contact Info**                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OIT National Service Desk | OIT       | - Agent Live Chat: Click the "Chat with us now" button in the lower right corner of the [yourIT Service portal](https://yourit.va.gov/va) to launch Abel the Chatbot and type “chat with agent” - Self-Service: [Create Incident](https://yourit.va.gov/va?id=sc_cat_item&sys_id=3f1dd0320a0a0b99000a53f7604a2ef9) - Phone: 855-673-4357 - TTY (hearing-impaired only): 844-224-6186 |
| VistA Patch Maintenance   | OIT       | Use the yourIT Service portal – A ServiceNOW (SNOW) ticket is entered and the ticket assigned to “PLM.HEALTH.HEALTHCAREADMIN”.                                                                                                                                                                                                                                                       |

### Browser &amp; Operating System Compatibility

VES is functional through Windows using Chrome or Edge.

Internet Explorer (IE) and Firefox are not supported browsers. Users who have permission to have Firefox should not be using it to access VES.

### From: User Guide VES 6.6

### Create new COMPACT Eligibility Rules for Registration Only and Pending Records

#### Person Search Tabs →  Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                  |
|          2 | Click the  **Overview**  section.                                                                                                                                                                       |
|          3 | Confirm the updated  **Overview**  screen shot is correct and accurate. The COMPACT Act Eligible Indicator information has been updated.  <!-- image -->  Figure : COMPACT Act Eligible Indicator Rules |

#### Person Search Tabs  → Eligibility → Primary and Secondary Eligibility Codes

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                       |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                           |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                             |
|          3 | Click the  **Primary and Secondary Eligibility Codes**  section.                                                                                                                                                                 |
|          4 | Scroll down to the "COMPACT Act Eligible" Secondary Eligibility Rule Scenarios section and verify that the updated table is correct.  <!-- image -->  Figure : "COMPACT Act Eligible" Secondary Eligibility Rule Scenarios Table |

#### Person Search Tabs  → Eligibility → Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                                                                                                                                                                                                    |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                                                                                                                                                                                                                                                                              |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                                                                                                                                                                                                                                                                                                                         |
|          5 | Scroll down to the  **Ineligible Reason: (Required if an Ineligible Date is entered)**  information and verify that the included information is correct.  **Removed Text**  : “When the user accepts the changes, the eligibility fields assign “COMPACT Act Eligible” with Code 24 (and abbreviation “COMPACT”), “Dishonorable VA or FFP” core VHAP, and a CCP VCE status of “Restricted” (R) or “Ineligible” (X).  <!-- image -->  Figure : Rules for Ineligible Reason |

### Change Indian Capability

#### Person Search Tabs →  Demographics → Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          3 | Click the  **Personal**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|          4 | Scroll down to the  **Indian**  section and verify that the included information is correct.  **Removed Text:**  - VES displays the Veteran's "Yes" or "No" response to the ARE YOU AN INDIAN? question from the 10-10EZ or 10-10EZR form. - Attestation Date, Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes" or "No". - Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes", and the Enrollment Status is VERIFIED. - A reversal does not remove the "Indian" status entirely.  <!-- image -->  Figure : Demographics (Indian) |
|          5 | Scroll down to the  **Attestation Date**  section (Directly underneath  **Indian**  ) and verify that the included information is correct:  <!-- image -->  Figure : Demographics (Attestation Date)                                                                                                                                                                                                                                                                                                                                                                                                                     |

#### Person Search Tabs → Demographics  → Personal → Personal (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|          3 | Click the  **Personal**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          4 | Click the  **Personal (Add a Person)**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|          5 | Scroll down to the  **Indian**  section and verify that the included information is correct.  **Removed Text:**  - VES displays the Veteran's "Yes" or "No" response to the ARE YOU AN INDIAN? question from the 10-10EZ or 10-10EZR form. - Attestation Date, Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes" or "No". - Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes", and the Enrollment Status is VERIFIED. - A reversal does not remove the "Indian" status entirely.  <!-- image -->  Figure : Demographics (Indian - Add a Person) |
|          6 | Scroll down to the  **Attestation Date**  section (Directly underneath  **Indian**  ) and verify that the included information is correct:  <!-- image -->  Figure : Demographics (Attestation Date)                                                                                                                                                                                                                                                                                                                                                                                                                                    |

#### Person Search Tabs → Demographics → Personal → Personal History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                    |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                      |
|          3 | Click the  **Personal**  section.                                                                                                                                                                                                                                          |
|          4 | Click the  **Personal History**  section.                                                                                                                                                                                                                                  |
|          5 | Confirm the following text was accurately removed.  <!-- image -->  Figure : Attestation Date (Personal History)  **Removed Text:**  - Reflects the "Application Stamp Date", the date the self-identified "Indian" question on the 1010EZ or 1010EZR form received by VA. |

### Allow "No Residential Address" Records in CC Eligibility File

#### Person Search Tabs → Demographics → Addresses → Residential Address

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click on the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                           |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                |
|          3 | Click the  **Addresses**  section.                                                                                                                                                                                                                                                                   |
|          4 | Click the  **Residential Addresses**  section.                                                                                                                                                                                                                                                       |
|          5 | Verify that the included information is correct.  <!-- image -->  Figure : Residential Address  **Removed Text:**  - Residential Address is required. The VES displays the error message "Residential Address is required" when attempting to complete a registration without a Residential Address. |

### VA Profile Demographics Push

#### Person Search Tabs → Eligibility →  VHA Profiles

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------|
|          1 | Click on the  **Person Search Tabs**  section on the table of contents on the Online Help.              |
|          2 | Click the  **Eligibility**  section.                                                                    |
|          3 | Click the  **VHA Profiles**  section.                                                                   |
|          4 | Scroll down to the  **View Historical VHA Profiles**  section towards the bottom of the page.           |
|          5 | Verify that the included information is correct.  <!-- image -->  Figure : View Historical VHA Profiles |

### VHAP Copay Effective Date

#### Person Search Tabs → Eligibility →  VHA Profiles

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                      |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click on the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                      |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                                            |
|          3 | Click the  **VHA Profiles**  section.                                                                                                                                                                                                                                                           |
|          4 | Verify that the included information is correct.  <!-- image -->  Figure : View Historical VHA Profiles  <!-- image -->  Figure : Copay Effective Date  <!-- image -->  Figure : VHA Profiles Change History Screenshot  Removed:  <!-- image -->  VHA Profiles Assigned – Unselect to Unassign |

#### Person Search Tabs  → Eligibility → Edit Eligibility

Confirm the following VES updates.

| **Step**   | **Action**                                                                                                                                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                     |
| 2          | Click the  **Eligibility**  tab.                                                                                                                                                             |
| 3          | Scroll down to the  **VHA Profiles**  and click “VIEW VHA PROFILES”.                                                                                                                         |
| 4          | Confirm the below screenshots are accurate.  <!-- image -->  Figure : VHA Profiles Update                                                                                                    |
| **5**      | Once the top screenshot is confirmed, click “VIEW HISTORICAL VHA PROFILES” and review that the following screenshot is correct.  <!-- image -->  Figure : VHA Profiles Change History Update |

## ## 6 Troubleshooting

### National Service Desk and Other Contacts

Table 2: Support Contact Information

| **Name**                  | **Org**   | **Contact Info**                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OIT National Service Desk | OIT       | - Agent Live Chat: Click the "Chat with us now" button in the lower right corner of the [yourIT Service portal](https://yourit.va.gov/va) to launch Abel the Chatbot and type “chat with agent” - Self-Service: [Create Incident](https://yourit.va.gov/va?id=sc_cat_item&sys_id=3f1dd0320a0a0b99000a53f7604a2ef9) - Phone: 855-673-4357 - TTY (hearing-impaired only): 844-224-6186 |
| VistA Patch Maintenance   | OIT       | Use the yourIT Service portal – A ServiceNOW (SNOW) ticket is entered and the ticket assigned to “PLM.HEALTH.HEALTHCAREADMIN”.                                                                                                                                                                                                                                                       |

### Browser &amp; Operating System Compatibility

VES is functional through Windows using Chrome or Edge.

Internet Explorer (IE) and Firefox are not supported browsers. Users who have permission to have Firefox should not be using it to access VES.

### From: User Guide VES 6.0

### Demographics screen field updates

Confirm the following Online Help updates.

\

|   **Step** | **Action**                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section from the table of contents to the left of the Online Help.                                                                                      |
|          2 | Click the  **Demographics**  section.                                                                                                                                                      |
|          3 | Click the  **Identity Traits**  topic.  <!-- image -->  Figure 8: Identity Traits screen                                                                                                   |
|          4 | Scroll down to the  **Race**  field. The following text and rules have been added:  <!-- image -->  Figure 9: Race field on Identity Traits screen  <!-- image -->                         |
|          5 | Scroll down to the  **Ethnicity**  field. The following text and rules have been added:  <!-- image -->  Figure 10: Ethnicity on Identity Traits screen  <!-- image -->                    |
|          6 | Click the  **Identity Traits (Add a Person)**  topic on the table of contents.  <!-- image -->  Figure 11: Identity Traits on Add a Person (AAP) screen                                    |
|          7 | Scroll down to the  **Race**  field. The following text and rules have been added:  <!-- image -->  <!-- image -->                                                                         |
|          8 | Scroll down to the  **Ethnicity**  field. The following text and rules have been added:  <!-- image -->  \  <!-- image -->                                                                 |
|          9 | Click the  **Personal**  section on the table of contents.                                                                                                                                 |
|         10 | Click the  **Personal**  topic.  <!-- image -->  Figure 12: Personal screen                                                                                                                |
|         11 | Scroll down to the  **Benefit Applied For**  field. The newly added text is as follows:  <!-- image -->  Figure 13: Benefit Applied For dropdown on the Personal screen  <!-- image -->    |
|         12 | Scroll down to the  **Marital Status**  field. The newly added text is as follows:  <!-- image -->  Figure 14: Marital Status dropdown on the Personal screen  <!-- image -->              |
|         13 | Scroll down to the  **Religion**  field. The newly added text is as follows:  <!-- image -->  Figure 15: Religion dropdown on the Personal screen  <!-- image -->                          |
|         14 | Click the  **Personal (Add a Person)**  topic on the table of contents.  <!-- image -->  Figure 16: Personal on Add a Person (AAP) screen                                                  |
|         15 | Scroll down to the  **Benefit Applied For**  field. The newly added note is as follows:  <!-- image -->  Figure 17: Benefit Applied For field on the Personal (AAP) screen  <!-- image --> |
|         16 | Scroll down to the  **Marital Status**  field. The newly added note is as follows:  <!-- image -->  Figure 18: Marital Status on the Personal (AAP) screen  <!-- image -->                 |
|         17 | Scroll down to the  **Religion**  field. The newly added note is as follows:  <!-- image -->  Figure 19: Religion field on the Personal (AAP) screen  <!-- image -->                       |

### Demographics and VA Profile

|   **Step** | **Action**                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents of the online help.                          |
|          1 | Click the  **Overview**  topic under the  **Demographics**  section.  RESULT: The  **Overview**  topic displays. |
|          2 | Scroll down to the  **Demographics and VA Profile**  dropdown link.                                              |
|          3 | Click the  **Demographics and VA Profile**  dropdown link. The following text ahas been added:  <!-- image -->   |

### Demographics Overview Subtab Order Change

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                              |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section from the table of contents to the left of the Online Help.                                                                                   |
|          2 | Click the  **Demographics**  section.                                                                                                                                                   |
|          3 | Click the  **Overview**  topic.                                                                                                                                                         |
|          5 | The Demographics Overview subtabs are the following order:  - Overview - Identity Traits - Personal - Addresses - Associates - Insurance <!-- image -->  <!-- image -->  <!-- image --> |

### CP&amp;E Veterans Health Administration Profile (VHAP) Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section from the table of contents to the left of the Online Help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|          2 | Click the  **Reference**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          3 | Click the  **VHA Profile**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|          4 | Click the  **Carveout VHAPs**  topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|          5 | The CP&amp;E VHAPs include:  - CHAMPVA Standard (108)  <!-- image -->  Figure 20: CHAMPVA VHAP  - Beneficiary Spina Bifida (109)  <!-- image -->  Figure 21: Beneficiary Spina Bifida VHAP  - Beneficiary Children of Women of Vietnam Veterans (110)  <!-- image -->  Figure 22: Beneficiary Children of Women of Vietnam Veterans VHAP  - Veteran Foreign Medical Program (122)  <!-- image -->  Figure 23: Veteran Foreign Medical Program VHAP  - CHAMPVA Caregiver (305)  <!-- image -->  Figure 24: CHAMPVA Caregiver VHAP  - Camp Lejeune Family (306)  <!-- image -->  Figure 25: Camp Lejeune Family VHAP  ***CHAMPVA Standard (108)***  <!-- image -->  ***Beneficiary Spina Bifida (109)***  <!-- image -->  ***Beneficiary Children of Women of Vietnam Veterans (110)***  <!-- image -->  ***Veteran Foreign Medical Program (122)***  <!-- image -->  ***Camp Lejeune Family (306)***  <!-- image -->  ***CHAMPVA Caregiver (305)***  <!-- image --> |

### Carveout VHAP Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section from the table of contents to the left of the Online Help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|          2 | Click the  **Reference**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          3 | Click the  **VHA Profiles**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|          4 | Click the  **Carveout VHAPs**  topic. The following updated Carveout VHAPs include:  - VA DoD Direct Resource Sharing Agreements (295)  <!-- image -->  Figure 26: VA DoD Direct Resource Sharing Agreements VHAP  - TRICARE (229)  <!-- image -->  Figure 27: TRICARE VHAP  - Active Duty (303)  <!-- image -->  Figure 28: Active Duty VHAP  - Joint Incentive Fund (304)  <!-- image -->  Figure 29: Joint Incentive Fund  ***VA DoD Direct Resource Sharing Agreements (295)***  <!-- image -->  ***TRICARE (229)***  <!-- image -->  ***Active Duty (303)***  <!-- image -->  ***Joint Incentive Fund (304)***  <!-- image --> |

### Enrollment updates: Application Signature Date and Application Method

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section from the table of contents to the left of the Online Help.                                                                                                                    |
|          2 | Click the  **Enrollment**  section.                                                                                                                                                                                      |
|          3 | Click the  **Enrollment**  topic. The following screen has been updated to continue displaying the following fields after “Add a Person” is complete:  - Application Signature Date - Application Method  <!-- image --> |
|          4 | Click the  **View Historical Enrollment**  topic under the  **Enrollment**  section on the table of contents of the Online Help.                                                                                         |
|          5 | Confirm the following fields have been added to the  **View Historical Enrollment**  screen.  - Application Signature Date - Application Method                                                                          |
|            | <!-- image -->                                                                                                                                                                                                           |

### Four New Self-Reported Registration Reasons

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                          |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section from the table of contents to the left of the Online Help.                                                                                                               |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                        |
|          4 | Click the  **Edit Current Eligibility**  topic.                                                                                                                                                                     |
|          5 | Scroll down to the  **Self-Reported Registration Only Reasons**  section. The following new reasons added include:  - 4 th Mission - Clinical Evaluation - HUD-VASH - Immunizations  <!-- image -->  <!-- image --> |
|            | Click back to the  **Current Eligibility**  section from the table of contents to the left of the Online Help.                                                                                                      |
|            | Click the  **Edit Current Eligibility (Add a Person)**  topic.                                                                                                                                                      |
|            | Scroll down to the  **Self-Reported Registration Only Reasons**  section. The following new reasons added include:  - 4 th Mission - Clinical Evaluation - HUD-VASH - Immunizations  <!-- image -->  <!-- image --> |

### “EHBD” Updated to “E&amp;E”

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------|
|          1 | <!-- image -->  Click the  **Search**  icon  from the table of contents to the left of the Online Help. |
|          2 | Type in “EHBD” the search field section.                                                                |
|          3 | Confirm “E&E” has been noted as the replacement for “EHBD”.                                             |

### Updated “Enrollment System” and “VES” to “Veterans Health Administration (VHA) Enrollment System (VES)” and “VES”

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | <!-- image -->  Click the  **Search**  icon  from the table of contents to the left of the Online Help.                                                                                                      |
|          2 | Type in “VES” the search field section. “Enrollment System” and “VES” has been replaced with “Veterans Health Administration (VHA)” and “VES” throughout the VES Online Help and VES quick start-user guide. |
|          3 | Click the  **VHA Enrollment System (VES)**  topic on the table of contents.                                                                                                                                  |
|          4 | Scroll down to the  **Overview**  section. The following sentence has been added detailing the renaming of “ES” to “VES”.  <!-- image -->                                                                    |

### National Service Desk and Other Contacts

Table 2: Support Contact Information

| **Name**                  | **Org**   | **Contact Info**                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OIT National Service Desk | OIT       | - Agent Live Chat: Click the "Chat with us now" button in the lower right corner of the [yourIT Service portal](https://yourit.va.gov/va) to launch Abel the Chatbot and type “chat with agent” - Self-Service: [Create Incident](https://yourit.va.gov/va?id=sc_cat_item&sys_id=3f1dd0320a0a0b99000a53f7604a2ef9) - Phone: 855-673-4357 - TTY (hearing-impaired only): 844-224-6186 |
| VistA Patch Maintenance   | OIT       | Use the yourIT Service portal – A ServiceNOW (SNOW) ticket is entered and the ticket assigned to the “NTL SUP Admin Team”.                                                                                                                                                                                                                                                           |

### Browser &amp; Operating System Compatibility

VES is functional through Windows using Chrome or Edge.

Internet Explorer (IE) and Firefox are not supported browsers. Users who have permission to have Firefox should not be using it to access VES.

### From: User Guide VES 6.14

### Update Document Management Options

#### Person Search Tabs → Document Management→ Search Documents

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                            |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                               |
|          2 | Click the  **Document Management**  section.                                                                                                                                                          |
|          3 | Click the  **Search Documents**  section.                                                                                                                                                             |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 8: Proof of Discharge Menu  <!-- image -->  Figure 9: Administration Menu  <!-- image -->  Figure 10: Tera Eligibility Menu |

#### Person Search Tabs → Document Management → Upload Documents

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                 |
|          2 | Click the  **Document Management**  section.                                                                                                                                                            |
|          3 | Click the  **Upload Documents**  section.                                                                                                                                                               |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 11: Proof of Discharge Menu  <!-- image -->  Figure 12: Administration Menu  <!-- image -->  Figure 13: Tera Eligibility Menu |

### Add and Change Letters

#### Person Search Tabs → Communications → Available for Mailing

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                      |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                         |
|          2 | Click the  **Communications**  section.                                                                                                                                                                                         |
|          3 | Click the  **Available for Mailing**  section.                                                                                                                                                                                  |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 14: VHA-EED Decision Notice Dishonorable  <!-- image -->  Figure 15: VHA-EED Updated Form Numbers  <!-- image -->  Figure 16: Eligible Letter Section |

#### Person Search Tabs → Eligibility → Current Eligibility → Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                 |
|          2 | Click the  **Eligibility**  section.                                                                                                                                    |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                            |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                       |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 17: Unlock Veteran Option  <!-- image -->  Figure 18: Reason for Unlock Request Dropdown Menu |

### Automate TERA Eligibility (Phase 2 of 3) - Cohort #3

#### Person Search Tabs → Military Service → Current Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                            |
|          2 | Click the  **Military Service**  section.                                                                                          |
|          3 | Click the  **Current Military Service**  section.                                                                                  |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 19: Cohort #3  <!-- image -->  Figure 20: TERA Indicator |

### Restrict SW Asia Conditions Eligibility

#### Person Search Tabs → Military Service → Current Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                       |
|------------|--------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.          |
|          2 | Click the  **Military Service**  section.                                                        |
|          3 | Click the  **Current Military Service**  section.                                                |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 21: SW Asia Conditions |

### Medicare Claim Number

#### Person Search Tabs → Demographics → Insurance → Add Medicare → Add/Update Insurance Carrier - Medicare

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                 |
|          2 | Click the  **Demographics**  section.                                                                                                                                   |
|          3 | Click the  **Insurance**  section.                                                                                                                                      |
|          4 | Click the  **Add Medicare**  section.                                                                                                                                   |
|          5 | Click the  **Add/Update Insurance Carrier - Medicare**  section.                                                                                                        |
|          6 | Confirm the following information has been added:  <!-- image -->  Figure 22: Medicare Claim Number (Part A)  <!-- image -->  Figure 23: Medicare Claim Number (Part B) |

#### 4.5.2

### From: User Guide VES 6.3

### CC Determination Date on screens:

#### Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                            |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                |
|          2 | Click the  **Overview**  section.                                                                                                                     |
|          3 | Scroll all the way down to the bottom of the  **Overview**  topic.                                                                                    |
|          4 | Confirm the updated  **Overview**  screen shot with the added  **CC Determination Date**  is correct and accurate.  <!-- image -->  Figure : Overview |

#### Community Care

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                             |
|          2 | Click the  **Eligibility**  section.                                                                               |
|          3 | Click the  **Community Care**  section.                                                                            |
|          4 | Scroll down to the  **CC Determination Date**  definition.                                                         |
|          5 | Confirm the added  **CC Determination Date**  definition and screen shot are correct and accurate.  <!-- image --> |

#### Community Care Determination

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                    |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                      |
|          3 | Click the  **Community Care**  section.                                                                                                                                                                   |
|          4 | Click the  **Community Care Determination**  topic (still under the  **Community Care**  section).                                                                                                        |
|          5 | Scroll down to the  **Community Care Outcome**  panel section.                                                                                                                                            |
|          6 | Scroll down to the  **CC Determination Date**  definition (under the  **Community Care Program Collateral VCEs**  table).                                                                                 |
|          7 | Confirm the added  **CC Determination Date**  definition is correct and accurate.  <!-- image -->                                                                                                         |
|          8 | Scroll down to the bottom of the topic.                                                                                                                                                                   |
|          9 | Confirm the updated  **Community Care Determination**  screen shot with the added  **CC Determination Date**  screen shot is correct and accurate.  <!-- image -->  Figure : Community Care Determination |

#### Community Care History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                          |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                              |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                |
|          3 | Click the  **Community Care**  section.                                                                                                                                                                             |
|          4 | Click the  **Community Care Determination History**  topic (still under the  **Community Care**  section).                                                                                                          |
|          5 | Scroll down to the  **Community Care Outcome**  panel section.                                                                                                                                                      |
|          6 | Confirm the added  **CC Determination Date**  definition is correct and accurate.  <!-- image -->                                                                                                                   |
|          7 | Scroll down to the bottom of the topic.                                                                                                                                                                             |
|          8 | Confirm the updated  **Community Care Determination History**  screen shot with the added  **CC Determination Date**  field is correct and accurate.  <!-- image -->  Figure : Community Care Determination History |

### Presumptive Psychosis on screens:

#### Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                 |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                    |
|          3 | Scroll down to the  **Eligibility**  screen shot.                                                                                                                                                       |
|          4 | Confirm the updated  **Eligibility**  screen shot with the added  **Clinical Evaluations**  and  **Clinical Determinations**  panels are correct and accurate.  <!-- image -->  Figure : Eligibility    |
|          5 | Navigate back to the Table of Contents.                                                                                                                                                                 |
|          6 | Click the  **Clinical Evaluations**  section (still under the  **Eligibility**  section).                                                                                                               |
|          7 | Confirm the added  **Clinical Evaluations**  topic is correct and accurate.  <!-- image -->                                                                                                             |
|          8 | Navigate back to the Table of Contents.                                                                                                                                                                 |
|          9 | Scroll down to the  **Clinical Determinations**  section (still under the  **Eligibility**  section).                                                                                                   |
|         10 | Click the  **Clinical Determinations**  topic (which has been renamed from “Other Eligibility Factors”).                                                                                                |
|         11 | Click the  **Clinical Determinations History**  section.                                                                                                                                                |
|         12 | Scroll down to the  **Presumptive Psychosis**  panel.                                                                                                                                                   |
|         13 | Confirm the text under  **Presumptive Psychosis**  is correct and accurate.  <!-- image -->                                                                                                             |
|         14 | Scroll down to the bottom of the topic.                                                                                                                                                                 |
|         15 | Confirm the updated  **Clinical Determination History**  screen shot with the added  **Presumptive Psychosis**  panel is correct and accurate.  <!-- image -->  Figure : Clinical Determination History |
|         16 | Navigate back to the table of contents.                                                                                                                                                                 |
|         17 | Click the  **View Clinical Determination**  topic (still under “Clinical Determinations”).                                                                                                              |
|         18 | Scroll down to the  **Presumptive Psychosis**  panel.                                                                                                                                                   |
|         19 | Confirm the added text for “Presumptive Psychosis” and notes are correct and accurate.  <!-- image -->                                                                                                  |
|         20 | Scroll down to the bottom of the topic.                                                                                                                                                                 |
|         21 | Confirm the updated  **Clinical Determination**  screen shot with the added  **Presumptive Psychosis**  panel is correct and accurate.  <!-- image -->  Figure : Clinical Determination                 |

#### Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                             |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                               |
|          3 | Click the  **Edit Current Eligibility**  section.                                                                                                                                                                  |
|          4 | Scroll down to the  **Presumptive Psychosis Screening**  definition (under  **Clinical Evaluations**  ).                                                                                                           |
|          5 | Confirm the added  **Presumptive Psychosis Screening**  definition is correct and accurate.  <!-- image -->                                                                                                        |
|          6 | Scroll down to the  **Presumptive Psychosis Category**  definition.                                                                                                                                                |
|          7 | Confirm the added  **Presumptive Psychosis Category**  definition is correct and accurate.  <!-- image -->                                                                                                         |
|          8 | Scroll down to the  **Rules…**  (under the  **Presumptive Psychosis Category**  definition).                                                                                                                       |
|          9 | Confirm the added  **Rules…**  and  **Note**  are correct and accurate.  <!-- image -->                                                                                                                            |
|         10 | Scroll down to the bottom of the  **Edit Current Eligibility**  topic.                                                                                                                                             |
|         11 | Confirm the updated  **Edit Current Eligibility**  screen shot with the added fields of “Presumptive Psychosis Screening” and “Presumptive Psychosis Category”.  <!-- image -->  Figure : Edit Current Eligibility |

#### Eligibility History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                         |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                                           |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                                                                                                   |
|          4 | Click the  **Eligibility History**  section.                                                                                                                                                                                                                                                   |
|          5 | Scroll down to the  **Clinical Evaluations**  panel.                                                                                                                                                                                                                                           |
|          6 | Confirm the text under  **Clinical Evaluations**  is correct and accurate.  <!-- image -->                                                                                                                                                                                                     |
|          7 | Scroll down to the  **Clinical Determinations**  panel.                                                                                                                                                                                                                                        |
|          8 | Confirm the text under  **Clinical Determinations**  has been renamed from “Other Eligibility Factors”.  <!-- image -->                                                                                                                                                                        |
|          9 | Scroll down to the bottom of the topic.                                                                                                                                                                                                                                                        |
|         10 | Confirm the updated  **Eligibility History**  screen shot with the added  **Clinical Evaluations panel**  , and the updated  **Clinical Determinations**  panel (renamed from “Other Eligibility Factors”) screen shot are correct and accurate.  <!-- image -->  Figure : Eligibility History |

#### Secondary Eligibility Codes

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                |
|          2 | Click the  **Eligibility**  section.                                                                                                   |
|          3 | Click the  **Primary and Secondary Eligibility Codes**  topic.                                                                         |
|          4 | Scroll down to the  **Clinical Evaluation**  secondary eligibility code definition.                                                    |
|          5 | Confirm the added text regarding the  **Clinical Evaluation**  carveout VHAP assignment below is correct and accurate.  <!-- image --> |
|          6 | Scroll down to the  **Presumptive Psychosis secondary eligibility code**  definition.                                                  |
|          7 | Confirm the text under “  **Presumptive Psychosis secondary eligibility code**  ” is correct and accurate.  <!-- image -->             |

### “Presumptive (38 USC 1702-38 CFR 17.109)” Carveout VHAP

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help.                                                 |
|          2 | Click the  **Reference**  section.                                                                                            |
|          3 | Click the  **Carveout VHAPs**  topic.                                                                                         |
|          4 | Scroll down to the  **Presumptive (38 USC 1702-38 CFR 17.109)**  carveout VHAP (profile code 135) definition.                 |
|          5 | Confirm the text for the  **Presumptive (38 USC 1702-38 CFR 17.109)**  carveout VHAP is correct and accurate.  <!-- image --> |

### “Clinical Evaluation” Carveout VHAP

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Still on the  **Carveout VHAPs**  topic, scroll down to the  **Clinical Evaluation**  carveout VHAP (profile code 308) definition. |
|          2 | Confirm the text for the  **Clinical Evaluation**  carveout VHAP is correct and accurate.  <!-- image -->                          |

### 1010 EZ / 1010 EZR 2022 Form Updates:

#### Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                              |
|------------|-----------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help. |
|          2 | Click the  **Overview**  topic.                                                         |
|          3 | Scroll down to the Indian field.                                                        |
|          4 | Confirm the added second bullet is correct and accurate.  <!-- image -->                |

#### Identity Traits

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                    |
|          2 | Click the  **Demographics**  section.                                                                                      |
|          3 | Click the  **Identity Traits**  topic.                                                                                     |
|          4 | Scroll down to the  **Self-Identified Gender Identity (SIGI)**  field definition.                                          |
|          5 | Confirm the updated  **Self-Identified Gender Identity (SIGI)**  field definition is correct and accurate.  <!-- image --> |
|          6 | Scroll down to the  **Race**  field definition.                                                                            |
|          7 | Confirm the updated  **Race**  field definition is correct and accurate.  <!-- image -->                                   |
|          8 | Scroll down to the  **Ethnicity**  field definition.                                                                       |
|          9 | Confirm the updated  **Ethnicity**  field definition is correct and accurate.  <!-- image -->                              |

#### Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                          |
|------------|-----------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.             |
|          2 | Click the  **Personal**  section (still under the  **Demographics**  section).                      |
|          3 | Scroll down to the  **Indian**  field definition.                                                   |
|          4 | Confirm the updated  **Indian**  field text is correct and accurate (third bullet).  <!-- image --> |

#### Financials

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                   |
|------------|----------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.      |
|          2 | Click the  **Financials**  section.                                                          |
|          3 | Scroll down to the “Print 1010EZ” and “Print 1010EZR” fields definition.                     |
|          4 | Confirm the updated text of both field definitions are correct and accurate.  <!-- image --> |

#### Enrollment

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                           |
|------------|------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.              |
|          2 | Click the  **Enrollment**  section (still under the  **Person Search Tabs**  section).               |
|          3 | Click the  **Veteran’s Online Application**  topic.                                                  |
|          4 | Confirm the updated  **Veteran’s Online Application**  text is correct and accurate.  <!-- image --> |

### Updated TPA Message Log description

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                             |
|------------|----------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help |
|          2 | Click the  **Eligibility**  section.                                                   |
|          3 | Click the  **Community Care**  section.                                                |
|          4 | Click the  **TPA Message Log**  topic.                                                 |
|          5 | Confirm the added note is correct and accurate.  <!-- image -->                        |

### Updated VCE Description

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                             |
|------------|----------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help           |
|          2 | Click the  **Admin**  section.                                                         |
|          3 | Click the  **VCE Parameter**  topic.  **Note:**  Veteran’s Choice Eligibility (VCE).   |
|          4 | Confirm the updated VCE Parameters definition is correct and accurate.  <!-- image --> |

### Updated COMPACT Act Error Message on UI description

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                       |
|          2 | Click the  **Eligibility**  section.                                                                                                                                         |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                 |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                            |
|          5 | Scroll down to the  **Non-Veteran Eligibility Codes**  section.                                                                                                              |
|          6 | Scroll down to the  **COMPACT Act (Override)**  radio button definition.  **Note:**  Veterans Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act of 2020. |
|          7 | Confirm the added  **COMPACT Act (Override)**  radio button definition is correct and accurate (located at the very bottom of topic).  <!-- image -->                        |

### From: User Guide VES 6.1

### U.S. Department of Housing and Urban Development-VA Supportive Housing (HUD-VASH) updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                          |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section.                                                                                                                                                                   |
|          2 | Click the  **Reference**  section.                                                                                                                                                                  |
|          3 | Click the  **VHA Profiles**  section.                                                                                                                                                               |
|          4 | Click the  **Carveout VHAP**  topic.                                                                                                                                                                |
|          5 | Scroll down to the very bottom carveout VHAP on the carveout VHAP table.  **HUD-VASH Restricted Care**  **Code: 307**  <!-- image -->                                                               |
|          6 | Navigate back to the table contents.                                                                                                                                                                |
|          7 | Click the  **Person Search Tabs**  section.                                                                                                                                                         |
|          8 | Click the  **Eligibility**  section.                                                                                                                                                                |
|          9 |                                                                                                                                                                                                     |
|         10 | Click the  **Edit Current Eligibility**  topic.                                                                                                                                                     |
|         11 | Confirm the new  **HUD-VASH**  field in the screen shot below.  <!-- image -->  Figure 8: HUD-VASH field on the Edit Current Eligibility screen                                                     |
|         12 | Scroll down to the  **HUD-VASH Non-Veteran Eligibility Code**  field. The following text and rules have been added:  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image --> |
|         13 | Navigate back to the table of contents.                                                                                                                                                             |
|         14 | Click the  **Edit Current Eligibility (Add a Person)**  topic (still under the  **Current Eligibility**  section).                                                                                  |
|         15 | Confirm the new  **HUD-VASH**  field on the screenshot below.  <!-- image -->  Figure 9: HUD-VASH field on the Edit Current Eligibility (AAP) screen                                                |
|         16 | Scroll down to the  **HUD-VASH Non-Veteran Eligibility Code**  field. The following text and rules have been added:  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image --> |
|         17 | Click the  **Person Search Tabs**  section from the table of contents to the left of the Online Help.                                                                                               |
|         18 | Click the  **Eligibility**  section                                                                                                                                                                 |
|         19 | Click the  **Primary and Secondary Eligibility Codes**  topic.                                                                                                                                      |
|         20 | Scroll down to the  **Non-Veteran Eligibility Codes**  section with a list of a 1-10.                                                                                                               |
|         21 | Confirm the added HUD-VASH text is correct as listed as number “10”.  <!-- image -->  Figure : HUD-VASH Non-Veteran Secondary Eligibility Code                                                      |
|         22 | Scroll down to the  **Secondary Eligibility Codes**  section. HUD-VASH has been added as number “9” under the “Non-Veteran Eligibility Codes” section:  <!-- image -->                              |

<!-- image -->

### Community Care Hardship Expiration Date

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section.                                                                                                                                            |
|          2 | Click the  **Admin**  section.                                                                                                                                               |
|          3 | Click the  **E&amp;E Service**  section.                                                                                                                                     |
|          4 | Click the  **E&amp;E Service**  topic.                                                                                                                                       |
|          5 | Scroll down to the very bottom of the  **E&amp;E Service**  topic. The following text and screen shot were added.  <!-- image -->  <!-- image -->  Figure : Hardship Expires |

### Organized Extract Reports into Their Own Section

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                  |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section.                                                                                                                                           |
|          2 | Click the  **Reports**  section.                                                                                                                                            |
|          3 | Click the  **Report Descriptions**  topic.                                                                                                                                  |
|          4 | Scroll down to the very bottom of the  **Report Descriptions**  topic until you reach “Extract Reports”. The following “Extract Reports” section was added:  <!-- image --> |

### OIT Homeless Program Report Extract

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                    |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section.                                                                                                                             |
|          2 | Click the  **Reports**  section.                                                                                                                              |
|          3 | Click the  **Report Descriptions**  topic.                                                                                                                    |
|          4 | Scroll down to the very bottom of the  **Report Descriptions**  topic until you reach “Extract Reports”. The following report text was added:  <!-- image --> |

### VES Auto-Locks Accounts Inactive 90-Days

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                        |
|------------|---------------------------------------------------------------------------------------------------|
|          1 | Click the  **VES Overview**  section.                                                             |
|          2 | Click the  **VES Inactive Accounts**  topic. The following report text was added:  <!-- image --> |

### Financials Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|          2 | Click the  **Financials**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          3 | Click the  **Financial Details**  topic. The following outdated text was removed from this topic:  ~~**Note:**~~  ~~The rules for setting GMT Copay Required or Pending Adjudication were changed beginning in calendar year 2010. This General Counsel ruling affected the Priority Group assigned to the Veteran.~~  ~~Effective July 24th, 2014, the setting for “GMT Copay Required” or “Pending Adjudication”, that had changed for those Veterans who met the Income and Net Worth ranges as described under the field “~~  ~~***Do you want to send this for Adjudication?***~~  ~~” below has been discontinued.~~  ~~Veterans who had very low income where the GMT Threshold is less than the MTT and the person's net income is less than or equal to the GMTT, yet their net income plus assets was greater than the Net Worth Threshold, will be placed in Priority Group 7 is also no longer valid as of July 24th, 2014.~~  ~~**Edit Financial Details (Income Year XXXX)**~~  ~~***Do you want to send this for Adjudication?: (Required)***~~  ~~*(Discontinued July 24th, 2014)*~~  ~~This displays only when after completing a current Means Test and the evaluation of total computed income, MT and GMT Thresholds. Threshold determines the means test status could be one of three statuses:~~  ~~When the GMT Threshold is greater than the MT Threshold and the user selects:~~  - ~~Yes - Outcome will be “MT Copay Required” or “GMT Copay Required”.~~ - ~~No - MT Status will be set to GMT Copay Required.~~  ~~or~~  ~~When the GMT Threshold is less than or equal to the MT Threshold and the user selects:~~  - ~~Yes - MT Status will be set to Pending Adjudication.~~ - ~~No - If Net Income is greater than the GMT Threshold, MT Status will be set to MT Copay Required.~~ - ~~No - If Net Income is less than or equal to the GMT Threshold, MT Status will be set to GMT Copay Required.~~  ~~**Assets**~~  ~~On the~~  ~~**Assets**~~  ~~panel, the following fields are now disabled as of the 5.13 release; September 2020. Users can no longer enter data into these fields:~~  - ~~Cash and Bank Account Balance~~ - ~~Land, Buildings Less Mortgage, and Liens~~ - ~~Other Property of Assets~~  ~~Disabling these fields prevents the supplemental adjudication question from being presented. The supplemental adjudication question is no longer required as part of the financial assessment process used to assign a Veteran’s enrollment priority group, copay responsibilities and other benefits and should no longer be presented in any financial assessment scenario. VES will hide the three fields when completing a new Income Test OR viewing a historical Income Test with no values (zero or no data). Existing records display read-only values (greater than zero only) in the three fields (“Cash and Bank Account Balance”, “Land, Buildings Less Mortgage, and Liens”, and “Other Property of Assets”) if they are on file for historical Income Tests.~~  ~~**Note:**~~  ~~VES users can enter a single “Income Test” each year for a record. The financial information entered as part of the “Income Test” will be used to automatically create a “Means Test” and/or “RX Copay/Pharmacy Test” depending on the type of financial testing that the Beneficiary is subject to.~~  - ~~Income Test: Single test entered in VES that is used to gather financial information.~~ - ~~Means Test: If a Beneficiary is subject to means testing, information from the income test is used to create a means test. The status of the means test determines if the Beneficiary will be required to make copayments for treatment.~~ - ~~RX Copay/Pharmacy Test: If a Beneficiary is subject to RX Copay/Pharmacy testing, information from the income test is used to create a RX Copay/Pharmacy test. The status of the RX Copay/Pharmacy test determines if the Beneficiary will be required to make copayments for prescription medications.~~ - ~~Long Term Care (LTC) Test: If a Beneficiary is subject to Long Term Care testing, a separate Long Term Care (LTC) test will be completed. The status of the Long Term Care test determines if the Beneficiary will be required to make copayments for long term care services.~~  ~~**Means Test Pending Adjudication Status Changes**~~  ~~The Means Test calculation is being updated to assure multiple things: (1) that new Means Tests are not put in a “Pending Adjudication” status forever, (2) that the Veteran is not placed in a priority group he or she does not qualify for; and (3) that the Veteran does not incorrectly appear to be waiting for adjudication of his or her means test. The outcome of these changes is that a new Means Test will no longer be placed in a “Pending Adjudication” status.~~  ~~**Debts (pre-Feb. 2005 format):**~~  ~~***$:***~~  ~~Here is where all debts are individually entered for the Veteran and Spouse only. Debt information is only collected for the pre-Feb 2005 Format Tests.~~  ~~This data is shared with VistA.~~  ~~***Rules...***~~  - ~~*Debts*~~ ~~must be a dollar amount 0 to 9999999.00.~~ - ~~*Debts*~~ ~~for a person cannot exceed the dollar amount in the asset type of Other Property or Assets amount for that same person.~~ |

### Add Spouse (Financials Update)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents of the VES Online Help.                                                                                                  |
|          2 | Click the  **Financials**  section.                                                                                                                                                          |
|          3 | Click the  **Dependents**  section.                                                                                                                                                          |
|          4 | Click the  **Add/Edit Spouse**  section.                                                                                                                                                     |
|          5 | Click the  **Add Spouse**  topic.                                                                                                                                                            |
|          6 | Confirm the added screen shots:  <!-- image -->  <!-- image -->  Figure 12: Add a Spouse (Before Registration)  <!-- image -->  <!-- image -->  Figure 13: Add a Spouse (After Registration) |
|          7 | Scroll down to the following updated fields and confirm if the definitions are correct and accurate.  <!-- image -->                                                                         |
|          8 | Scroll down to the following updated fields and confirm if the definitions are correct and accurate.  <!-- image -->                                                                         |
|          9 | Scroll down to the following updated fields and confirm if the definitions are correct and accurate.  <!-- image -->  <!-- image -->                                                         |

### VDL Definition

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **VES Overview**  section.                                                                                         |
|          2 | Click the  **Acronyms and Definitions**  topic.                                                                               |
|          3 | Click the “V” link located at the top of the topic.                                                                           |
|          4 | Scroll down to the “VA Software Document Library” definition. Confirm the definition is correct and accurate.  <!-- image --> |

### From: User Guide VES 6.7

### Section 101 to include all WWII Veterans

#### Person Search Tabs → Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                        |
|------------|-------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                            |
|          2 | Click the  **Eligibility**  section.                                                                              |
|          3 | Navigate to the  **COMPACT Act Eligible Indicator**  section and verify that the included information is correct. |
|          4 | <!-- image -->  Figure : COMPACT Act Eligible Indicator Overview                                                  |

#### Person Search Tabs → Eligibility → Primary and Secondary Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1   | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                    |
|        0.2 | Click the  **Eligibility**  section.                                                                                                                                                                                                                                       |
|        3   | Click the  **Primary and Secondary Eligibility Codes**  section.                                                                                                                                                                                                           |
|        4   | Navigate to the  **Veteran Primary Eligibility Codes**  section and verify that the included information is correct.                                                                                                                                                       |
|        5   | Navigate down to the  **Notes**  section and verify that the following information is accurate.  VES assigns  **Veteran Secondary Eligibility Codes**  :  Navigate down to the Non-Veteran Secondary Eligibility Codes section and verify that the information is correct. |
|        6   | <!-- image -->  Figure : Veteran Secondary Eligibility Codes                                                                                                                                                                                                               |
|        7   | <!-- image -->  Figure : Secondary Eligibility Scenarios                                                                                                                                                                                                                   |
|            | <!-- image -->  Figure : Secondary Eligibility Scenarios (cont.)                                                                                                                                                                                                           |
|        8   | <!-- image -->  Figure : Add Date Range to World War II Entry                                                                                                                                                                                                              |
|        9   | Navigate to the Compact Act Eligible Table and verify that the information is accurate.  <!-- image -->  Figure : COMPACT Act Eligible Table                                                                                                                               |

#### Person Search Tabs → Eligibility → Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                |
|------------|-----------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                    |
|          2 | Click the  **Eligibility**  section.                                                                      |
|          3 | Click the  **Edit Current Eligibility**  section.                                                         |
|          4 | Navigate to the  **COMPACT Act (Override)**  section and verify that the included information is correct. |
|          5 | <!-- image -->  Figure : COMPACT Act (Override) Rules                                                     |

#### Menu Bar → Reference → VHA Profiles → CORE VHAPs

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                    |
|------------|-----------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help                  |
|          2 | Click the  **Reference**  section.                                                            |
|          3 | Click the  **VHA Profiles**  section.                                                         |
|          4 | Navigate to the  **CORE VHAPs**  section and verify that the included information is correct. |
|          5 | <!-- image -->  Figure : Core VHAP Veteran Full Med Benefits                                  |

### Add an Uncharacterized Discharge Type

#### 4.2.1 Person Search Tabs  → Military Service → Military Service Episodes – HEC

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                  |
|------------|-------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                      |
|          2 | Click the  **Military Service**  section.                                                                   |
|          3 | Click the  **Military Service Episodes - HEC**  section.                                                    |
|          4 | Scroll down to the  **Discharge Type**  section.                                                            |
|          5 | Verify that the following information is accurate:  <!-- image -->  Figure : Uncharacterized Discharge Type |

### Z07 Consistency Checks

#### Person Search Tabs → Demographics → Personal → Personal (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                              |
|          2 | Click the  **Demographics**  section.                                                                                                                |
|          3 | Click the  **Personal**  section.                                                                                                                    |
|          4 | Click the  **Personal (Add a Person)**  topic.                                                                                                       |
|          5 | Verify that the following information is accurate:  <!-- image -->  <!-- image -->  Figure : Update to Claim Folder Number and Claim Folder Location |

#### Person Search Tabs → Demographics → Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                          |
|          2 | Click the  **Demographics**  section.                                                                                                                            |
|          3 | Click the  **Personal**  section.                                                                                                                                |
|          4 | Verify that the following screenshot has been accurately updated to remove the “Same as SSN” button:  <!-- image -->  Figure : Demographics - Removed SSN Button |

### From: User Guide VES 6.10

### VES Vietnam Service Episode Dates

#### Person Search Tabs → Military Service → Period of Service

Confirm the following Online Help updates.

|   Step | Action                                                                                                                                                              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                              |
|      2 | Click the  **Military Service**  section.                                                                                                                           |
|      3 | Click the  **Period of Service**  section                                                                                                                           |
|      4 | Confirm the following information was modified:  <!-- image -->  Figure : Automatic HEC Period of Service List  <!-- image -->  Figure : HEC Period of Service List |

### VES Change Rejected Enrollment Status to Deferred

#### Person Search Tabs → Eligibility→ Enrollment→ Current Enrollment

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                      |
|------------|-------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.         |
|          2 | Click the  **Eligibility**  section.                                                            |
|          3 | Click the  **Enrollment**  section.                                                             |
|          4 | Click the  **Current Enrollment**  section.                                                     |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure : Enrollment Statuses |

### ESM Enable Confidential Address

#### Person Search Tabs → Demographics → Addresses →Confidential Mailing Address

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                           |
|------------|----------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                              |
|          2 | Click the  **Demographics**  section.                                                                                |
|          3 | Click the  **Addresses**  section.                                                                                   |
|          4 | Click the  **Confidential Mailing Address**  section.                                                                |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure : Current Confidential Communication Types |

### TERA Updates for 10-10EZ, UI, VOA and Work Items

#### Person Search Tabs → Financials

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                      |
|          2 | Click the  **Financials**  section.                                                                          |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure : Print 1010EZ &amp; Print 1010EZR |

#### Person Search Tabs → Enrollment → Veteran’s Online Application

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                     |
|------------|----------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                        |
|          2 | Click the  **Enrollment**  section.                                                                            |
|          3 | Click the  **Veteran’s Online Application**  section.                                                          |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure : Veteran's Online Application (VOA) |

#### Person Search Tabs → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                          |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                                                                                                                                                                                             |
|          2 | Click the  **Military Service**  section.                                                                                                                                                                                                                                                                                                                           |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure : Agent Orange Exposure Location  <!-- image -->  Figure : TERA Indicator  <!-- image -->  Figure : TERA Indicator - Cohort 1-3  Confirm the screenshot has been updated (found at the bottom of the Military Service section):  <!-- image -->  Figure : Military Service Tab Screenshot |

<!-- image -->

### From: User Guide VES 6.12

### VES Electronic Health Record Modernization (EHRM) Confidential and Temporary Phone Number

#### Person Search Tabs → Demographics → Addresses → Add/Edit Address

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                    |
|          2 | Click the  **Demographics**  section.                                                                                                                      |
|          3 | Click the  **Addresses**  section.                                                                                                                         |
|          4 | Click the  **Add/Edit Address**  section.                                                                                                                  |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 8: Confidential Address &amp; Rule Updates  <!-- image -->  Figure 9: Phone Type |

### VES EHRM Automate Employee Only and Employee Veteran VHAPs

#### Menu Bar → Reference → VHA Profile → Carveout VHAPs

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help.                                                            |
|          2 | Click the  **Reference**  section.                                                                                                       |
|          3 | Click the  **VHA Profile**  section.                                                                                                     |
|          4 | Click the  **Carveout VHAPs**  section.                                                                                                  |
|          5 | Confirm the following information has been added:  <!-- image -->  Figure 10: Employee Only  <!-- image -->  Figure 11: Employee Veteran |

### VES Non-Medical Care Collection Fund (MCCF) Consolidated Patient Account Centers (CPAC) User Role and Member ID Label Update (Admin)

#### Person Search Tabs → Demographics → Identity Traits

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                      |
|------------|-------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.         |
|          2 | Click the  **Demographics**  section.                                                           |
|          3 | Click the  **Identity Traits**  section.                                                        |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 12: Member ID (EPIDI) |

#### Menu Bar → Veteran → Veteran Search (Person Search)

|   **Step** | **Action**                                                                                                                                                                        |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help.                                                                                                     |
|          2 | Click the  **Veteran**  section.                                                                                                                                                  |
|          3 | Click the  **Veteran Search (Person Search)**  section.                                                                                                                           |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 13: Member ID (EDIPI) - Veteran Search  <!-- image -->  Figure 14: Member ID (EDIPI) - Veteran Search 2 |

### From: User Guide VES 6.11

### VES Site Correlation (New ADD Treatment Facility button)

#### Person Search Tabs → Facility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                      |
|          2 | Click the  **Facility**  section.                                                                                                                                                                                                           |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure 8: Facility Add Button Option  Confirm the following text been removed from the Online Help:  <!-- image -->  Figure 9: Date &amp; Outpatient Days (Removed Text) |

### VES Enable Edit for Employer Details, Mother's Maiden Name and Place of Birth

#### Person Search Tabs → Financials→ Dependents→ Add/Edit Spouse→ Edit Dependent Spouse

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                 |
|          2 | Click the  **Financials**  section.                                                                                                                     |
|          3 | Click the  **Dependents**  section.                                                                                                                     |
|          4 | Click the  **Add/Edit Spouse**  section.                                                                                                                |
|          5 | Click the  **Edit Dependent Spouse**  section.                                                                                                          |
|          6 | Confirm the following information has been added:  <!-- image -->  Figure 10: Maiden Name Editable Fields  <!-- image -->  Figure 11: Employment Status |

### International Phone Numbers – Phase 1 Updates

#### Person Search Tabs → Demographics → Addresses

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                  |
|------------|---------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.     |
|          2 | Click the  **Demographics**  section.                                                       |
|          3 | Click the  **Addresses**  section.                                                          |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 12: Phone Numbers |

### Persian Gulf Deployed Indicator

#### Person Search Tabs → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                    |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                       |
|          2 | Click the  **Military Service**  section.                                                                                                                     |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure 13: Persian Gulf Indicator  <!-- image -->  Figure 14: Persian Gulf Indicator (VES) |

<!-- image -->

### From: User Guide VES 6.2

### "Enrollment System Community Care (ESCC)” to "VHA Enrollment System (VES) Integrated Veteran Care (IVC) Systems Impact (VES/IVC SI)" change

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                             |
|------------|----------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help |
|          2 | Click the  **Eligibility**  section.                                                   |
|          3 | Click the  **Community Care**  section.                                                |
|          4 | Click the  **VES/IVC SI Quality Report**  topic.                                       |
|          6 | Confirm “ESCC” has been removed from this report.                                      |

### “Expanded MH Care Non-Enrollee” field definition for Ineligible Records

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                  |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                      |
|          2 | Click the  **Eligibility**  section.                                                                                                                        |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                |
|          4 | Click the  **Edit Current Eligibility**  topic.                                                                                                             |
|          5 | Scroll down to the  **MH CARE NON-ENROLEE**  field.                                                                                                         |
|          6 | Confirm text is correct and accurate.  <!-- image -->                                                                                                       |
|          7 | Navigate back to the table of contents on the Online Help                                                                                                   |
|         10 | Click the  **Edit Current Eligibility (Add a Person)**  topic still under the  **Person Search Tabs**  section and under  **Current Eligibility**  section. |
|         11 | Scroll down to the  **MH CARE NON-ENROLEE**  field.                                                                                                         |
|         12 | Confirm the added text is correct and accurate.  <!-- image -->                                                                                             |

### Ineligible Reasons and Rules Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                    |
|          2 | Click the  **Eligibility**  section.                                                                                                      |
|          3 | Click the  **Current Eligibility**  section.                                                                                              |
|          4 | Scroll down to the  **VBA Query Status**  field.                                                                                          |
|          5 | Confirm the following text is correct and accurate:  <!-- image -->                                                                       |
|          6 | Navigate back to the Table of Contents.                                                                                                   |
|          7 | Click the  **Edit Current Eligibility**  topic (still under Current Eligibility)                                                          |
|          8 | Scroll down to the  **Self-Reported Registration Only Reason (Required)**  field.                                                         |
|          9 | Scroll down to  **CLINICAL EVALUATION**  in the bulleted list.  <!-- image -->                                                            |
|         10 | Scroll down to the  **Remove All Rated SC Disabilities**  button definition.                                                              |
|         11 | Confirm the added text is accurate and correct.  <!-- image -->                                                                           |
|         12 | Scroll down to the  **Reason Eligibility Status is Pending Verification**  field                                                          |
|         13 | Confirm the added NOTE is correct and accurate.  <!-- image -->                                                                           |
|         14 | Scroll down to the “Manual entry scenarios for service connected (SC) % and Ineligible information” text.                                 |
|         15 | Confirm the text is correct and accurate.  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image --> |
|         16 | Scroll down to the  **Ineligible Reason**  field.                                                                                         |
|         17 | Confirm the added “Other” ineligible reason is accurate and correct.  <!-- image -->                                                      |
|         18 | Please confirm the first three bullets for the Ineligible Reason “  **Rules…”**  are correct and accurate:  <!-- image -->                |
|         19 | Navigate back to the table of contents.                                                                                                   |
|         20 | Click the  **Primary and Secondary Eligibility Codes**  topic.                                                                            |
|         21 | Scroll down to  **Special Tx Authority Care**  (under Secondary Eligibility Codes)                                                        |
|         22 | Confirm the text is accurate and correct (#8 in the list).  <!-- image -->                                                                |
|         23 | Navigate back to the table of contents.                                                                                                   |
|         24 | Click the  **Overview**  section (still under Current Eligibility).                                                                       |
|         25 | Scroll down to “COMPACT ACT Eligibility” under the  **Update Current Eligibility:**  field.                                               |
|         26 | Confirm the added text is accurate and correct. Second, third and fourth bullet, plus the note under the fourth bullet.  <!-- image -->   |

### Core VHAP Updates: (Profile Codes: 222, 223, 225, 226, and 290)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                          |
|------------|-------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help        |
|          2 | Click the  **Reference**  section.                                                  |
|          3 | Click the  **VA Profile**  section.                                                 |
|          4 | Click the  **Core VHAPS**  topic (still under the  **VHA Profiles**  section)       |
|          5 | Scroll down to the  **Veteran Restricted Med Benefits**  (222) core VHAP.           |
|          6 | Confirm the text is correct and accurate.  <!-- image -->                           |
|          7 | Scroll down to the  **Non-Veteran Other Restricted Med Benefits**  (223) core VHAP. |
|          8 | Confirm the text is correct and accurate.  <!-- image -->                           |
|          9 | Scroll down to the  **Humanitarian**  (225) core VHAP.                              |
|         10 | Confirm the text is correct and accurate.  <!-- image -->                           |
|         11 | Scroll down to the  **Applicant in Process**  (226) core VHAP.                      |
|         12 | Confirm the text is correct and accurate.  <!-- image -->                           |
|         13 | Scroll down to the  **Ineligible**  (290) core VHAP.                                |
|         14 | Confirm the text is correct and accurate.  <!-- image -->                           |

### Clinical Evaluation Secondary Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                        |
|          2 | Click the  **Eligibility**  section.                                                                                          |
|          3 | Click the  **Primary and Secondary Eligibility**  topic still under the  **Eligibility**  Section (under Person Search Tabs). |
|          4 | Scroll down to the “Clinical Evaluation” secondary eligibility code (#9) under the  **Secondary Eligibility Code**  section   |
|          5 | Confirm the following text for “Clinical Evaluation” is correct and accurate, (#9):  <!-- image -->                           |

### “Application Date” label changed to “Application Received Date”

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                    |
|          2 | Click the  **Overview**  section.                                                                                                                         |
|          3 | Scroll down to the "Application Received Date” definition.                                                                                                |
|          4 | Confirm the “Application Received Date” definition is correct and accurate.  <!-- image -->                                                               |
|          5 | Scroll down to the  **Overview**  screen shot.                                                                                                            |
|          6 | Confirm the  **Overview**  screen shot has been updated to include “Application Received Date”.  <!-- image -->  Figure 8: Overview                       |
|          7 | Navigate back to the  **Person Search Tabs**  section on the table of contents on the Online Help                                                         |
|          8 | Click the  **Eligibility**  section.                                                                                                                      |
|          9 | Scroll down to the  **Eligibility**  screen shot.                                                                                                         |
|         10 | Confirm the  **Eligibility**  screen shot has been updated to include “Application Received Date”.  <!-- image -->                                        |
|         11 | Navigate back to the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                        |
|         11 | Click the  **Current Eligibility**  topic section.                                                                                                        |
|         12 | Scroll down to the "Application Received Date” definition.                                                                                                |
|         13 | Confirm the “Application Received Date” definition is correct and accurate.  <!-- image -->                                                               |
|         14 | Navigate back to the table of contents.                                                                                                                   |
|         15 | Click the  **Eligibility History**  topic, still under the  **Current Eligibility**  topic.                                                               |
|         16 | Scroll down to the "Application Received Date” definition.                                                                                                |
|         17 | Confirm the “Application Received Date” definition is correct and accurate.  <!-- image -->                                                               |
|         18 | Scroll down to the  **Eligibility History**  screen shot.                                                                                                 |
|         19 | Confirm the  **Eligibility History**  screen shot has been updated to include “Application Received Date”.  <!-- image -->  Figure 9: Eligibility History |
|         20 | Navigate back to the table of contents.                                                                                                                   |
|         21 | Click the  **Enrollment**  section.                                                                                                                       |
|         22 | Click the  **Cancelled/Declined/Override Enrollment (Includes Add a Person)**  topic.                                                                     |
|         23 | Confirm the  **Application Received Date**  field has been updated.  <!-- image -->                                                                       |
|         24 | Confirm the  **Enrollment**  screen shot has been updated to include “Application Received Date”.  <!-- image -->  Figure 10: Enrollment                  |
|         25 | Navigate back to the table of contents.                                                                                                                   |
|         26 | Click the  **Enrollment History**  topic, still under the  **Current Eligibility**  topic.                                                                |
|         27 | Confirm the  **Enrollment History**  screen shot has been updated to include “Application Received Date”.  <!-- image -->  Figure 11: Enrollment History  |

### From: User Guide VES 6.4

### Preferred Language Updates Screens

#### Demographics → Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          3 | Click the  **Personal**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          4 | Confirm the updated  **Personal**  screen shot with the removed  **Language Entry Date**  and check box are correct and accurate.  <!-- image -->  Figure 8: Personal History Screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|          5 | Confirm the  **Language Entry Date**  information has been removed:  Removed “Language Entry Date” information:  **Language Entry Date:**  This is the date the Veteran’s Preferred Language data was entered. The date can be entered manually or automatically.  **More...**  The initial value for the Language Entry Date field is blank.  **Language Entry Date scenarios:**  If no date is entered, then the value defaults to the current date upon a successful update.  If the user selects a value from the Preferred Language drop-down list, then the Language Entry Date field is blank, but can be edited. For example, if a Veteran enters his/her preferred language on a 10-10EZ form, the VES user should enter the date of the 10-10EZ form into the Language Entry Date field.  **Rules...**  The Language Entry Date cannot be a future date.  The Language Entry Date can be a date in the past. However, the date cannot be before the Veteran’s date of birth. |

#### Demographics → Personal (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          3 | Click the  **Personal (Add a Person)**  section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          4 | Confirm the updated  **Personal (Add a Person)**  screen shot with the removed  **Language Entry Date**  and check box are correct and accurate.  <!-- image -->  Figure 9: Personal History Screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          5 | Confirm the  **Language Entry Date**  information has been removed:  Removed “Language Entry Date” information:  **Language Entry Date:**  This is the date the Veteran’s Preferred Language data was entered. The date can be entered manually or automatically.  **More...**  The initial value for the Language Entry Date field is blank.  **Language Entry Date scenarios:**  If no date is entered, then the value defaults to the current date upon a successful update.  If the user selects a value from the Preferred Language drop-down list, then the Language Entry Date field is blank, but can be edited. For example, if a Veteran enters his/her preferred language on a 10-10EZ form, the VES user should enter the date of the 10-10EZ form into the Language Entry Date field.  **Rules...**  The Language Entry Date cannot be a future date.  The Language Entry Date can be a date in the past. However, the date cannot be before the Veteran’s date of birth. |

### Disable Date of Death

#### Demographics → Personal

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                   |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                    |
|          3 | Click the  **Personal**  section.                                                                                                                                                                        |
|          4 | Scroll down to the  **Date of Death**  definition and information.                                                                                                                                       |
|          5 | Confirm the added  **Date of Death**  information and screen shots are correct and accurate.  <!-- image -->  Figure : Modify Date of Death Help Text  <!-- image -->  Figure : Date of Death Rules Text |

#### Demographics → Personal (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                   |
|          2 | Click the  **Demographics**  section.                                                                                                                                                                    |
|          3 | Click the  **Personal (Add a Person)**  section.                                                                                                                                                         |
|          4 | Scroll down to the  **Date of Death**  definition and information.                                                                                                                                       |
|          5 | Confirm the added  **Date of Death**  information and screen shots are correct and accurate.  <!-- image -->  Figure : Modify Date of Death Help Text  <!-- image -->  Figure : Date of Death Rules Text |

### From: User Guide VES 6.2.2

### "COMPACT Act" (Override) Radio Button on Edit Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                       |
|          2 | Click the  **Eligibility**  section.                                                                                                                                         |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                 |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                            |
|          5 | Scroll down to the  **Non-Veteran Eligibility Codes**  section.                                                                                                              |
|          6 | Scroll down to the  **COMPACT Act (Override)**  radio button definition.  **Note:**  Veterans Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act of 2020. |
|          7 | Confirm the added  **COMPACT Act (Override)**  radio button definition is correct and accurate (located at the very bottom of topic).  <!-- image -->                        |
|          8 | Scroll down to the updated  **Edit Current Eligibility**  screen shot (bottom of topic).                                                                                     |
|          9 | Confirm the  **COMPACT Act (Override)**  radio button screen shot is correct and accurate.  <!-- image -->  Figure : COMPACT Act (Override) Radio Button                     |

### COMPACT Act Eligibility Rules Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Scroll down to the  **COMPACT Act Eligibility Rules**  section (still on the  **Edit Current Eligibility**  topic, and located below the  **COMPACT Act**  field definition). |
|          2 | Confirm the added  **COMPACT Act Eligibility Rule Scenarios**  are correct and accurate.  <!-- image -->  <!-- image -->                                                      |

### "Clinical Evaluation" Secondary Eligibility Rule Scenarios

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                           |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Scroll down to the “  **Clinical Evaluation**  ”  **Secondary Eligibility Rule Scenarios**  section (still on the  **Edit Current Eligibility**  topic, and located below the  **COMPACT Act Eligibility Rules**  ). |
|          2 | Confirm the added “  **Clinical Evaluation**  ”  **Secondary Eligibility Rule Scenarios**  are correct and accurate.  <!-- image -->  <!-- image -->                                                                 |

### COMPACT Act" (Override) Radio Button Disabled on Edit Current Eligibility (Add a Person (AAP))

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                       |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                         |
|          3 | Click the  **Current Eligibility**  section.                                                                                                                                                                                 |
|          4 | Click the  **Edit Current Eligibility**  section.                                                                                                                                                                            |
|          5 | Click the  **Edit Current Eligibility (Add a Person)**  topic.                                                                                                                                                               |
|          6 | Scroll down to the  **Non-Veteran Eligibility Codes**  section.                                                                                                                                                              |
|          7 | Scroll down to the  **COMPACT Act (Override)**  radio button definition.                                                                                                                                                     |
|          8 | Confirm the added  **COMPACT Act (Override)**  radio button definition is correct and accurate (located at the very bottom of topic).  <!-- image -->  <!-- image -->  Figure : COMPACT Act (Override) Disabled Radio Button |

### "COMPACT Act" Carveout VHAP

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help                               |
|          2 | Click the  **References**  section.                                                                        |
|          3 | Click the  **VHA Profiles**  section.                                                                      |
|          4 | Click the  **Carveout VHAPs**  topic.  **Note:**  Veteran's Health Administration Profile (VHAP).          |
|          6 | Scroll down to the  **COMPACT Act**  carveout VHAP (profile code 309) definition (last VHAP on the table). |
|          7 | Confirm the added  **COMPACT Act**  carveout VHAP definition is correct and accurate.  <!-- image -->      |

### VHAP Updates

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Scroll to the  **HUD-VASH Restricted Care**  VHAP (profile 307) (still on the  **Carveout VHAP**  topic from the previous section, and above the  **COMPACT Act Eligible**  carveout VHAP).  **Note:**  U.S. Department of Housing and Urban Development-VA Supportive Housing (HUD-VASH). |
|          2 | Confirm the  **HUD-VASH Restricted Care**  VHAP definition is correct and accurate.  <!-- image -->                                                                                                                                                                                        |
|          3 | Navigate back to the  **Menu Bar**  section on the table of contents on the Online Help                                                                                                                                                                                                    |
|          4 | Click the  **Core VHAPs**  topic under the  **Reference**  section, and the  **VHA Profiles**  section.                                                                                                                                                                                    |
|          5 | Scroll down to the  **Veteran Restricted Med Benefits**  VHAP (profile code 222).                                                                                                                                                                                                          |
|          6 | Confirm the  **Veteran Restricted Med Benefits**  VHAP definition is correct and accurate.  <!-- image -->                                                                                                                                                                                 |
|          6 | Scroll down to the  **Non-Veteran Other Restricted Med Benefits**  VHAP (profile 223).                                                                                                                                                                                                     |
|          7 | Confirm the  **Non-Veteran Other Restricted Med Benefits**  VHAP definition is correct and accurate.  <!-- image -->                                                                                                                                                                       |
|            | Scroll down to the  **Ineligible**  VHAP (profile 290).                                                                                                                                                                                                                                    |
|            | Confirm the  **Ineligible**  VHAP definition is correct and accurate.  <!-- image -->                                                                                                                                                                                                      |

### From: User Guide VES 6.7.1

### VES Change Combat Veteran Rules

#### Person Search Tabs → Eligibility → Current Eligibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                  |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                    |
|          3 | Click the  **Current Eligibility**  section                                                                                                                                                                             |
|          4 | Confirm the following sections have been removed:  Discharge Due to Disability  Military Disability Retirement  Agent Orange Exposure Location  Radiation Exposure Method  SW Asia Conditions  Camp Lejeune Eligibility |

#### Person Search Tabs → Eligibility → Current Eligibility → Current Eligibility (Add a Person)

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                                                                                                  |
|          2 | Click the  **Eligibility**  section.                                                                                                                                                                                    |
|          3 | Click the  **Current Eligibility**  section                                                                                                                                                                             |
|          4 | Click the  **Current Eligibility (Add a Person)**  section                                                                                                                                                              |
|          5 | Confirm the following sections have been removed:  Discharge Due to Disability  Military Disability Retirement  Agent Orange Exposure Location  Radiation Exposure Method  SW Asia Conditions  Camp Lejeune Eligibility |

#### Person Search Tabs → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                             |
|          2 | Click the  **Military Service**  section.                                                                                          |
|          3 | Confirm the following sections have been added and that the information is accurate:  <!-- image -->  Figure 8: CVE End Date Rules |

#### Person Search Tabs → Eligibility → Edit Eligibility → Other Eligibility Factors

|   **Step** | **Action**                                                                                                                                                                                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                                                                                                                                                                                       |
|          2 | Click the  **Eligibility**  tab.                                                                                                                                                                                                                                                                                                               |
|          3 | Click the  **Edit Eligibility**  tab.                                                                                                                                                                                                                                                                                                          |
|          4 | Scroll down and click  **Other Eligibility Factors.**                                                                                                                                                                                                                                                                                          |
|          5 | Confirm the removed information is not available and that the updated screen shot is accurate.  **Removed:**  Discharge Due to Disability  Military Disability Retirement  Agent Orange Exposure Location  Radiation Exposure Method  SW Asia Conditions  Camp Lejeune Eligibility  <!-- image -->  Figure 9: Other Eligibility Drop-Down Menu |

#### TERA Indicator

#### 4.2.1 Person Search Tabs  → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                              |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help                                                  |
|          2 | Click the  **Military Service**  section.                                                                                               |
|          3 | Confirm the following sections have been added and that the information is accurate:  <!-- image -->  Figure 10: TERA Indicator Updates |

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                      |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  option in the VHA Enrollment System (VES).                                                                                                        |
|          2 | Click the  **Military Service**  section.                                                                                                                                       |
|          3 | Scroll down to the Toxic Exposure Risk Activity section. and confirm the information is accurate:  <!-- image -->  Figure 11: Toxic Exposure Risk Activity Radio Button Options |

### From: User Guide VES 6.14.5

### VFMP

#### Person Search Tabs → VFMP Eligibility Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                           |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                              |
|          2 | Click the  **VFMP Eligibility Overview**  section.                                                                                                                   |
|          3 | Confirm all the added information to the new folders is accurate per the VFMP Requirements. Note: This is a completely new section and completely new tabs for VFMP. |

#### Person Search Tabs → Communications

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                           |
|------------|------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.              |
|          2 | Click the  **Communications**  section.                                                              |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure 8: Communications Overview |

#### Person Search Tabs → Communications → Comments

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                        |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                           |
|          2 | Click the  **Communications**  section.                                                                                                           |
|          3 | Click the  **Comments**  section.                                                                                                                 |
|          4 | Confirm all the added information to the new folders is accurate per the VFMP Requirements.  *Note: All folders under Comments are new sections.* |

#### Person Search Tabs → Communications → Correspondence

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                                                                        |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                                                                           |
|          2 | Click the  **Communications**  section.                                                                                                                                                           |
|          3 | Click the  **Correspondence**  section.                                                                                                                                                           |
|          4 | Confirm all the added information to the new folders is accurate per the VFMP Requirements.  *Note: Correspondence is a new section to house all the previous folders that fall under this list.* |

#### Person Search Tabs→ Demographics → Insurance Overview

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                     |
|------------|------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.        |
|          2 | Click the  **Demographics**  section.                                                          |
|          3 | Click the  **Insurance Overview**  section.                                                    |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 9: Pharmacy Coverage |

### 508 Keyboard Navigation

#### Troubleshooting → 508 Compliance &amp; Accessibility

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Troubleshooting**  section on the table of contents on the Online Help.                                    |
|          2 | Click the  **508 Compliance &amp; Accessibility**  section.                                                             |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure 10: Keyboard-Only User Accessibility Settings |

#### 4.2.2

### From: User Guide VES 6.9

### VES Ineligible Letters

#### Person Search Tabs → Communications → Available for Mailing

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                       |
|------------|----------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                          |
|          2 | Click the  **Communications**  section.                                                                                          |
|          3 | Click the  **Available for Mailing**  section                                                                                    |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure : 60-Day Pre-Term Letters and 1199 Eligibility Letters |

|   **Step** | **Action**                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search**  section on the table of contents on the Online Help.                                                                           |
|          2 | Click the  **Communications**  section.                                                                                                                      |
|          3 | Navigate to the  **Available for Mailing**  section.                                                                                                         |
|          4 | Confirm that the following information has been added:  <!-- image -->  Figure : Ineligible Letters  <!-- image -->  Figure : Ineligible Letters Description |

<!-- image -->

### VES TERA Verification Method

#### Person Search Tabs → Military Service

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                 |
|------------|--------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.    |
|          2 | Click the  **Communications**  section.                                                    |
|          3 | Confirm the following information has been added:  <!-- image -->  Figure : TERA Indicator |

<!-- image -->

### VES Veteran's Online Application (VOA)

#### Person Search Tabs → Eligibility → Registration

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                |
|------------|-----------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                   |
|          2 | Click the  **Eligibility**  section.                                                                      |
|          3 | Click the  **Registration**  section                                                                      |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure : VOA (Registration Only) Table |

### From: User Guide VES 6.13

### VBA Auto Registration to VES

#### Menu Bar → ESR Registration → Status History

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                     |
|------------|------------------------------------------------------------------------------------------------|
|          1 | Click the  **Menu Bar**  section on the table of contents on the Online Help.                  |
|          2 | Click the  **ESR Registration**  section.                                                      |
|          3 | Click the  **Status History**  section.                                                        |
|          4 | Confirm the following information has been added:  <!-- image -->  Figure 8: Auto Registration |

### VES Allow Edit to CC Determination Date

#### Person Search Tabs → Eligibility → Community Care→ Community Care Determination

Confirm the following Online Help updates.

|   **Step** | **Action**                                                                                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
|          1 | Click the  **Person Search Tabs**  section on the table of contents on the Online Help.                                                      |
|          2 | Click the  **Eligibility**  section.                                                                                                         |
|          3 | Click the  **Community Care**  section.                                                                                                      |
|          4 | Click the  **Community Care Determination**  section  **.**                                                                                  |
|          5 | Scroll to  **CC Determination Date**  and confirm the following information has been added:  <!-- image -->  Figure 9: CC Determination Date |
