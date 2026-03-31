---
title: ePrescribing Controlled Substances (ePCS) Graphical User Interface (GUI) Software Version 2.0 User Guide (Updated for PSO*7*731)
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: (Updated for PSO*7*731)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 2.0
patch_id: PSO*2.0
group_key: "PSO:PSO:2.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - epcs
  - span
  - table
  - figure
  - number
  - prescriber
  - contents
  - report
  - controlled
  - class
page_count: 0
word_count: 7737
section_count: 19
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_epcs_gui_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_epcs_gui_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

e-Prescribing Controlled Substances (ePCS)

Graphical User Interface (GUI)

Software Version 2.1

User Guide

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/001.png)

December 2023

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Ref130814778" class="anchor"></span>Table 1: Tier Support Contact Information</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 61%" />
<col style="width: 16%" />
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
<td>11/2023</td>
<td>1.2</td>
<td><p>Updates pertaining to PSO*7*731, removed all instances of Detox number:</p>
<ul>
<li><blockquote>
<p>Updated 4.1 <u>Step 3</u>. View the DEA Numbers</p>
</blockquote></li>
<li><blockquote>
<p>Updated steps in <u>4.1.1.2</u> <u>Edit a DEA Numbe</u>r</p>
</blockquote></li>
<li><blockquote>
<p>New screenshots for <u>Figure 12</u>, <u>Figure 16</u>, <u>Figure 17</u>, <u>Figure 19</u>, <u>Figure 20</u> and <u>Figure 22</u></p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>9/2023</td>
<td>1.1</td>
<td><p>Updates pertaining to PSO*7*735</p>
<ul>
<li><blockquote>
<p><u>References and Resources</u></p>
</blockquote></li>
<li><blockquote>
<p><u>Authentication via Personal Identification Verification</u></p>
</blockquote></li>
<li><blockquote>
<p><u>Changes to the DEA Prescribing Privileges Report</u></p>
</blockquote></li>
<li><blockquote>
<p><u>Acronyms and Abbreviations</u></p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>6/2023</td>
<td>1.0</td>
<td>Initial Publication for Patch PSO*7*545</td>
<td>Liberty IT Solutions</td>
</tr>
</tbody>
</table>

<span id="_Ref130814778" class="anchor"></span>Table 1: Tier Support Contact Information

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Guide](#organization-of-the-guide)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operations](#continuity-of-operations)
  - [Section 508 Compliance](#section-508-compliance)
    - [Screen Readers](#screen-readers)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
    - [Authentication via Personal Identity Verification](#authentication-via-personal-identity-verification)
  - [e-Prescribing Controlled Substances Main Menu](#e-prescribing-controlled-substances-main-menu)
    - [Icon Shortcuts](#icon-shortcuts)
    - [Menu Bar](#menu-bar)
  - [Exit System](#exit-system)
  - [Online Documentation](#online-documentation)
  - [Timeout Feature](#timeout-feature)
- [Using the Software](#using-the-software)
  - [Update Prescriber and DEA \# Information](#update-prescriber-and-dea-information)
  - [Reports](#reports)
    - [Reports Available to ePCS GUI Users](#reports-available-to-epcs-gui-users)
- [Troubleshooting](#troubleshooting)
  - [Access Issues](#access-issues)
  - [Log-On Issues](#log-on-issues)
  - [GUI Appears Distorted](#gui-appears-distorted)
    - [Example of Setting the Screen Resolution to 1920 x 1080](#example-of-setting-the-screen-resolution-to-1920-x-1080)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Glossary](#glossary)
The *e-Prescribing Controlled Substances (ePCS) Graphical User Interface User Guide* provides instructions for assigning, editing, and deleting controlled substance schedules in a graphical user interface (GUI) setting. The target audience for this manual includes users of the Pharmacy package, Automated Data Processing Application Coordinators (ADPAC), and other software users.
The ePCS GUI provides a consistent, event-driven, Windows® style user interface for ePCS. The Data Entry for Prescriber software provides a mechanism to add, edit, and delete Drug Enforcement Administration (DEA) Numbers for Department of Veterans Affairs (VA) prescribers, as well as to update the DEA controlled substance schedules for each DEA Number assigned.
The ePCS GUI uses Two-Factor Authentication (2FA) to ensure an audit trail is maintained for changes made to DEA Number-centric data.
The user must define the following items for every record in the DEA NUMBERS file (#8991.9):
- DEA Number: The unique number assigned to an individual, or the facility DEA Number assigned to an institution.
- Expiration Date: The date the DEA Number is no longer valid, as assigned by the DEA.
- Schedules: The drug schedules for which the provider is authorized to prescribe controlled substances.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ePCS GUI User Guide* is intended as an instructional guide for using the ePCS software. The user can use this manual in conjunction with the ePCS GUI online help option.

Screen displays may vary among different sites, and the data may not appear on the monitor exactly as shown in this manual. Although ePCS screens are subject to modification, the major menu options as they appear in this manual are fixed and are not subject to modification (except by the package developer).

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sub-paragraphs provide general information about how to use this document.

### Organization of the Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is organized into the following major sections:

Introduction — This section provides a brief description of the purpose of the user guide and an overview of the document’s structure and use.

System Summary — This section provides a general description of the system, written in non-technical terminology, the purpose for which the system is intended, the system configuration, data flows, user access, and continuity of operations.

Getting Started — This section provides a general walkthrough of the system from initiation through exit. The logical arrangement of the information enables functional personnel to understand the sequence and flow of the system.

Using the Software —This section serves as reference to the user, covering vital aspects of this tool.

Data Entry — ePCS is programmed to allow the user to update fields pertaining to a specific prescriber. In addition, users can add, edit, or delete records assigned to that prescriber which represent an assigned DEA Number and its associated schedules.

Reports — ePCS Reports are designed according to Pharmacy Benefits Management (PBM) specifications. Users have the option to preview a report on a monitor, or to send the output to a printer.

Troubleshooting — This section provides general troubleshooting advice on issues encountered by users.

Acronyms and Abbreviations — This section provides the user with a list of abbreviations and acronyms used throughout the document.

Glossary — This section provides the user with definitions of terms used throughout the document.

Index — Index of major topics of interest.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for ePCS.
- User uses ePCS to perform job duties.
- User has validated access to ePCS.
- User has completed any prerequisite training.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following disclaimers apply to all VA user documentation.

#### Software Disclaimer

This software was developed at the VA by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. The VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this guide does not constitute endorsement by the VA of the website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information found at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To avoid displaying sensitive information regarding patients and staff, the examples in this guide contain pseudonyms or scrambled data instead of real names. Patients and staff will be referred to as “EPCSPROV, ONE”, “EPCSPROV, TWO”, “EPCSUSER, ONE”, etc.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation related to ePCS v2.0 includes the following:

- *Installation Guide for the ePCS GUI*
- *Multi-DEA Pharmacy Enhancements PSO\*7\*545, PSJ\*5\*372, OR\*3\*499Deployment, Installation, Back-out, and Rollback Guide (DIBRG)*
- *Pharmacy Operational Updates (POU) PSO\*7.0\*735 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *Outpatient Pharmacy (PSO) Version 7.0 Technical Manual / Security Guide*
- *PSO\*7\*545 Patch Description (PD)*
- *PSO\*7\*735 Patch Description (PD)*

These documents can be found on the [VA Software Document Library (VDL)](https://www.va.gov/vdl/) website.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The three tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

Table 1 lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, role/associated tier level, organization, and contact information (email and phone number).

<table>
<caption><p><span id="_Ref130821014" class="anchor"></span>Table 2: Acronyms and Abbreviations</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Role</th>
<th>Org</th>
<th>Contact Info</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local ePCS Package Manager</td>
<td>Tier 0 Support</td>
<td>Veterans Health Administration (VHA)</td>
<td><p>ePCS Package Manager/Site Dependent</p>
<p>The Phone List can be found on the VA’s intranet site, contact page.</p></td>
</tr>
<tr class="even">
<td>Local Veterans Integrated Service Network (VISN) Coordinator</td>
<td>Tier 0 Support</td>
<td>VHA</td>
<td><p>Site Dependent</p>
<p>The Phone List can be found on the VA’s intranet site, contact page.</p></td>
</tr>
<tr class="odd">
<td>OIT National Service Desk</td>
<td>Tier 1 Support</td>
<td>OIT</td>
<td><p>National Service Desk</p>
<p>Incident Management Automated Notification Reporting (ANR) Tool.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref130821014" class="anchor"></span>Table 2: Acronyms and Abbreviations

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI is a VistA Class I system supporting PBM. The ePCS GUI provides auditing of changes made to DEA Number information for prescribers of controlled substances. The system uses two-factor authentication to meet DEA requirements, ensuring secure and traceable records are maintained.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the *Outpatient Pharmacy (PSO) Version 7.0 Technical Manual / Security Guide* for details related to system and site configuration.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI captures DEA schedule information for VA prescribers. In addition, any changes made to DEA-centric information are stored in a separate file, creating an audit trail of changes made to data pertaining to VA prescribers and their prescribed controlled substance authorizations.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security keys are assigned in VistA using the option Key Management main menu and then choosing the submenu Allocation of Security Keys.

The ePCS GUI requires the following security key for user access:

- XUEPCSEDIT: Gives a user access to the ePCS GUI. Prescribers should not have this key.

## Continuity of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site has a backup emergency plan in place in the event that the system goes down.

## Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 508 of the Rehabilitation Act Amendments of 1998 requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that the electronic and information technology enables persons with disabilities to have access to, and use of, information and data that is comparable to the access to and use of information and data by persons who are not individuals with disabilities, unless an undue burden would be imposed on the agency.

The Section 508 Accessibility Testing and Training Center (T&TC) was consulted and modifications to the GUI have been made to meet the requirements for Section 508 compliance. The ePCS GUI was designed to enable screen readers to accurately interpret information on the screens.

For more information on the VA Section 508 compliance efforts, please visit the Section 508 website.

### Screen Readers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ePCS has been evaluated for the accessibility of application content with multiple commercial screen readers. ePCS has been tested to ensure all screens work properly when a screen reader is active.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PBM ADPAC should use the following steps as a guide for setting up the ePCS GUI software.

1.  Select security keys.
- See Section 2.3 regarding User Access Levels for a description of ePCS security keys.
2.  Select required VistA settings.
- Users must be assigned the PSO EPCS GUI CONTEXT VistA menu option for the ePCS GUI to work.
3.  ePCS GUI setup is complete.
- Authorized users can update Prescriber and DEA number information using the Data Entry option and access controlled substance prescriber reports using the Reports option.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI is accessed through a desktop shortcut that points to the location of the ePCS GUI application (<span class="mark"></span>Figure 1). The executable file will be located on either a local or shared network drive. If the shortcut does not appear, refer to the *Installation Guide for the ePCS GUI*, or ask the local support staff for assistance.

<span id="_Ref130814621" class="anchor"></span>Figure 1: ePCS GUI Icon

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/002.png)

1.  Double-click the ePCS GUI shortcut to launch the application.

When the ePCS GUI is launched, a Personal Identity Verification (PIV) card with two-factor authentication is used to access the system.

### Authentication via Personal Identity Verification 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two-factor authentication adds a layer of security beyond a traditional username and password combination. The ePCS GUI obtains credentials from a combination of PIV card and Personal Identification Number (PIN). When the ePCS GUI is launched, it will attempt to use a PIV card for authentication.

> **NOTE:** If the PIN was used to access any Windows application within a site-defined period of time (e.g., 10 or 15 minutes), the PIN is cached; the user will be allowed access to the ePCS GUI without selecting a PIV certificate and re-entering the PIN.

1.  Select the desired PIV card certificate (Figure 2):

<span id="_Ref130814598" class="anchor"></span>Figure 2: PIV Certificate Selection

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/003.png)

4.  Enter the PIN and press the OK button (Figure 3):

<span id="_Ref130814579" class="anchor"></span>Figure 3: PIN Entry

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/004.png)

If PIV authentication is successful, the System Use Notification dialog will appear as shown in Figure 4. Press the OK button to complete the login process.

If PIV authentication fails, or the Cancel button is clicked, the prompt for Access and Verify codes will appear, as shown in Figure 5. Although the Access and Verify codes can be entered, access to the ePCS GUI will be denied; the PIV card and its associated PIN are required for access (Figure 6).

<span id="_Ref130814545" class="anchor"></span>Figure 4: System Use Notification

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/005.png)

<span id="_Ref144197776" class="anchor"></span>Figure 5: VistA Login Screen

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/006.png)

<span id="_Ref144197756" class="anchor"></span>Figure 6: Access Denied Window

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/007.png)

## e-Prescribing Controlled Substances Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS software contains two options, Data Entry and Reports, as shown in Figure 7. The user must hold the XUEPCSEDIT key to have access to the application. Users with the ORES key, signifying a provider, will not be able to use the ePCS GUI.

<span id="_Ref130814488" class="anchor"></span>Figure 7: Main Menu for the ePCS GUI

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/008.png)

### Icon Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The toolbar gives the user another way to navigate to the Data Entry and Reports options in the ePCS GUI. In addition, the user can display Topic Help or exit the application from the toolbar.

### Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI menu bar (Figure 8) enables the user to access shortcut commands.

<span id="_Ref130814466" class="anchor"></span>Figure 8: Main Menu Bar

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/009.png)

What the User Will See:

- Under the ePCS GUI title bar on the ePCS Main Menu, the menu bar presents the top-level commands (Figure 9).
- The File menu item enables the user to exit the application.
- The Function menu item on the main window provides access to:
- Data Entry
- Reports
- The Help menu item provides topic-specific help, or information about the ePCS GUI system.

<span class="mark"></span>Figure 9 displays the menu bar options with expanded menus.

<span id="_Ref130814383" class="anchor"></span>Figure 9: Main Menu Bar with Menus Expanded

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/010.png) ![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/011.png) ![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/012.png)

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the ePCS GUI main menu, click the Exit button to leave the ePCS GUI. Alternatively, from the same screen, users can go to File \> Exit, or click the Close window button (‘X’) in the top-right corner of the screen.

## Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online help is available throughout the entire ePCS GUI. To obtain online information for any screen, click the question mark button located on the toolbar ![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/013.png) or click the Topic Help button ![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/014.png) at the bottom-right corner of the screen. The information provided in the help menus corresponds to the information contained in this User Guide (Figure 10).

To obtain online information for a field, select that field and then press the \<F1\> key.

<span id="_Ref130814367" class="anchor"></span>Figure 10: Online Help Screen

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/015.png)

## Timeout Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI includes a timeout feature consistent with CPRS. A countdown screen will display a warning of the pending timeout of the application when the ePCS GUI application is idle for a user-defined amount of time. If the user takes no action, the application will close. Click the Do not close ePCS button to stay connected (<span class="mark"></span>Figure 11).

<span id="_Ref130814321" class="anchor"></span>Figure 11: ePCS Timeout Screen

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/016.png)

The amount of time for the timeout feature is user-defined at the application server level.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections provide instructions on how to use the ePCS GUI to perform tasks and functions in each of the two main areas: Update Prescriber andDEA \# Information and Controlled Substance Prescriber Reports.

## Update Prescriber and DEA \# Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Entry for Prescriber screen allows the user to update prescriber information and to add, edit, or delete DEA \# information for a selected prescriber.

After selecting the Update Prescriber and DEA \# Information option, the Data Entry for Prescriber screen will display (Figure 12).

<span id="_Ref130814305" class="anchor"></span>Figure 12: Data Entry for Prescriber Screen

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/017.png)

To use the Data Entry for Prescriber screen:

1.  Select a Prescriber.
- Begin by typing the last name of the prescriber whose record is to be updated. Additional information related to the prescriber is displayed to the right of the list, helping the user to differentiate between individuals with similar names.
5.  View/Edit Prescriber Information.
- After entering the desired selection criteria and clicking the Select button (or double-clicking the desired name), data are retrieved to populate the fields.

  NOTE: A message dialog (Figure 13) displays when the prescriber is not active. One or more reasons for not being active may be listed, including:
- The prescriber does not have an Access Code.
- The prescriber does not have a Verify Code.
- The prescriber is DISUSERed.
- The prescriber was terminated as of the date shown.

<span id="_Ref130814243" class="anchor"></span>Figure 13: Confirm Message Dialog

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/018.png)

> **NOTE:** A message dialog (Figure 14) appears when no DEA Numbers are found for the prescriber in the DEA NUMBERS file (#8991.9). Schedules found in the NEW PERSON file (#200) may be displayed by clicking the Yes button in the dialog. The provider has not been assigned any DEA Numbers but is still authorized to prescribe Controlled Substance medications. The record in the NEW PERSON file (#200) can be updated as shown in Figure 15.

<span id="_Ref130814262" class="anchor"></span>Figure 14: Confirm Dialog

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/019.png)

<span id="_Ref144294506" class="anchor"></span>Figure 15: Schedules from the NEW PERSON File

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/020.png)

- The Subject Alternative Name (SAN), Authorized to Write Med Orders? and Prescriber VA \# fields are populated and available for editing. If the prescriber has a Facility DEA \# in the NEW PERSON file (#200), that field is populated; however, the Facility DEA \# field cannot be changed through the ePCS GUI. In addition, any DEA Numbers already present in either the NEW PERSON file (#200) or the DEA NUMBERS file (#8991.9) are displayed as shown in Figure 16.

<span id="_Ref130824010" class="anchor"></span>Figure 16: Data Entry for Prescriber

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/021.png)

- Changing the values of the Subject Alternative Name, Authorized to Write Med Orders?, or Prescriber VA \# fields results in the Save Changes and Discard Changes buttons being enabled; the Add, Update and Delete buttons will be disabled as shown in Figure 17.

<span id="_Ref144208179" class="anchor"></span>Figure 17: Data Entry for Prescriber

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/022.png)

- Clicking the Save Changes button applies the updates to the database and enables DEA Numbers to be added, updated, or deleted. Figure 18 displays the Information popup detailing the update.

<span id="_Ref144208231" class="anchor"></span>Figure 18: Information Popup

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/023.png)

- Clicking the Discard Changes button restores the Subject Alternative Name, Authorized to Write Med Orders? and Prescriber VA \# fields to their values prior to the changes, and enables DEA Numbers to be added, updated, or deleted.
6.  View the DEA Numbers.
- The DEA Numbers assigned to the selected prescriber are shown in the table in the lower portion of the screen as shown in Figure 19. Each row displays the values stored for the DEA Number, Suffix, State, Expiration Date, and “Use for Inpatient Orders?” flag.

  NOTEs:
- Click the column header to sort the rows by that data element. The default is the DEA \# in ascending order and is indicated by a “^” to the left of the column header. The “v” indicates the column is sorted in descending order. Clicking a column which is already sorted toggles the order between ascending and descending.
- The Add, Update, and Delete buttons are disabled if changes to the prescriber’s data are pending. The Update and Delete buttons will be enabled only when the prescriber has DEA Numbers in the system.
- Clicking on a row highlights the DEA Number record, effectively selecting that row as a candidate for updating or deleting. Double-clicking a row has the same effect as selecting a row and clicking the Update button.

<span id="_Ref130822214" class="anchor"></span>Figure 19: DEA Numbers for a Selected Prescriber

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/024.png)

#### Entering Information to Add a DEA Number

The user can add a DEA Number assigned to a prescriber.

The following instructions take the user through the steps for entering a new DEA Number for the selected prescriber.

1.  From the Data Entry for Prescriber Screen
- Click the Add button (Figure 19) to launch the Add a DEA Number screen as shown in Figure 20.

<span id="_Ref130822175" class="anchor"></span>Figure 20: Add a DEA Number Detail Screen

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/025.png)

7.  Enter a DEA Number
- The DEA Number must consist of two letters followed by seven digits. The digits must satisfy the checksum requirement detailed in the data dictionary. The DEA Number must exist in the Department of Justice (DOJ) file.
- A DEA Number can be either an institutional type (used by multiple prescribers at a site) or an individual type (exclusive to one prescriber).

  NOTE: If the DEA Number is assigned to a different prescriber in the DOJ file, a confirmation dialog is displayed, prompting the user to continue or not (Figure 21).

<span id="_Ref130822271" class="anchor"></span>Figure 21: Confirm Popup

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/026.png)

8.  Enter a Suffix for an Institutional DEA Number
- A Suffix is required for an institutional DEA Number to determine who is using the DEA Number when prescribing controlled substances.
- The Suffix cannot be shared by multiple prescribers; it must be unique for each prescriber assigned to use the DEA Number.
- A Suffix must be three to ten alphanumeric characters and cannot contain the caret (^) symbol or any embedded spaces.
9.  Update the VistA Expiration Date (Only for Individual DEA Numbers)
- The Expiration Date for an institutional DEA Number cannot be changed; the value is set to the Expiration Date found in the DOJ record.
- The Expiration Date can be set in mm/dd/yy or mm/dd/yyyy format, or the value of ‘T’ (today) can be used. The ‘T’ can be followed by an integer value after a plus (+) or minus (-) sign to represent the number of days after or before today (e.g., ‘T+30’ is thirty days from the current date).
- The year cannot precede 2000.

  NOTE: Clicking the Mirror DOJ Date button automatically sets the VistA Expiration Date to the expiration date found on the DOJ server.
10. Use for Inpatient Orders? Flag
- An institutional DEA Number cannot be designated as use for inpatient orders.
- Only one individual DEA Number can be used for inpatient orders.
- If the prescriber has only one individual DEA Number, the Use for Inpatient Orders? box will be checked and will be disabled.
- If the prescriber has more than one individual DEA Number, checking the box for the new DEA Number sets the value to “No” for the existing designee.
11. Assign Controlled Substance Schedules
- The schedule boxes are checked initially based on the value in the DOJ record.
- All schedule boxes can be checked by checking the All Schedules checkbox. Subsequently unchecking any of the individual schedules unchecks the All Schedules box.
12. File the DEA Number
- Click the OK button to save the record.

#### Edit a DEA Number

The user can update an existing DEA Number assigned to a prescriber (Figure 22).

<span id="_Ref130822359" class="anchor"></span>Figure 22: Edit a DEA Number

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/027.png)

The following instructions take the user through the steps for updating the DEA Number for the selected prescriber.

1.  From the Data Entry for Prescriber Screen
- Click the Update button (or double-click a row) to launch the Edit DEA Number screen.
13. View the DEA Number
- The DEA Number cannot be changed when editing a record.
14. Update the Suffix for an Institutional DEA Number
- The Suffix for an institutional DEA Number is required, but the existing value can be changed.
- The Suffix cannot be shared by multiple prescribers; it must be unique for each prescriber assigned to use the DEA Number.
- A Suffix must be three to ten alphanumeric characters and cannot contain the caret (^) symbol or any embedded spaces.
15. Update the VistA Expiration Date
- The VistA Expiration Date for an institutional DEA Number cannot be changed; the value is set to the Expiration Date found in the DOJ record.
- The VistA Expiration Date can be set in mm/dd/yy or mm/dd/yyyy format, or the value of ‘T’ (today) can be used. The ‘T’ can be followed by an integer value after a plus (+) or minus (-) sign to represent the number of days after or before today (e.g., ‘T+30’ is thirty days from the current date).
- The year cannot precede 2000.

  NOTE: Clicking the Mirror DOJ Date button automatically sets the VistA Expiration Date to the expiration date found on the DOJ server.
16. Change the “Use for Inpatient Orders?” Designation
- An institutional DEA Number cannot be designated for use for inpatient orders.
- Only one individual DEA Number can be used for inpatient orders.
- If the prescriber has only one individual DEA Number, the Use for Inpatient Orders? box is checked and is disabled.
- If the prescriber has more than one individual DEA Number, checking the box for the new DEA Number sets the value to “No” for the existing designee.
17. Controlled Substance Schedules
- For institutional DEA Numbers, the schedules assigned are checked according to the values for the record in the NEW PERSON file (#200).
- For individual DEA Numbers, the schedules assigned are checked according to the values for the record in the DEA NUMBERS file (#8991.9).
- All schedule boxes can be checked by checking the All Schedules checkbox. Subsequently unchecking any of the individual schedules unchecks the All Schedules box.

  NOTE: Clicking the Mirror DOJ Schedules button automatically checks the boxes for the schedules associated with that DEA Number on the DOJ server.
18. File the DEA Number
- Click the OK button to save the record.

#### Delete a DEA Number

1.  Select a DEA Number from the Table
- A DEA Number can be removed from a prescriber by selecting the record and clicking the Delete button. If this is the only individual DEA Number for the prescriber and the Prescriber VA \# field is empty, the DEA Number will be removed, but the prescriber will no longer be able to prescribe controlled substances at the VA. If the record is marked “Use for Inpatient Orders?” and:
- Only one other individual DEA Number is assigned to the prescriber, the remaining DEA Number is automatically marked to be used for inpatient orders.
- More than two other individual DEA Numbers are assigned to the prescriber, the DEA Number cannot be deleted until another DEA Number is designated for use with inpatient orders.
- The screen will refresh to show the remaining DEA Numbers assigned to the prescriber (<span class="mark"></span>Figure 23).

<span id="_Ref130803638" class="anchor"></span>Figure 23: Confirm Popup

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/028.png)

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the reports available within the ePCS GUI.

Users can preview or print any report; some reports allow the user to export the report output to an MS Excel spreadsheet.

### Reports Available to ePCS GUI Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Five reports are available to ePCS GUI users.

- DEA Expiration Date Report;
- Print Prescribers with Privileges;
- Print DISUSER Prescriber with Privileges;
- Changes to the DEA Prescribing Privileges Report;
- Logical Access Control Audit Report.

What the User Sees

- A list of reports is available in the Select Report area (<span class="mark"></span>Figure 24).
- The DEA Expiration Date Report is the default selection when the Reports screen is launched; the corresponding selection criteria display on the right side of the screen.

<span id="_Ref130818647" class="anchor"></span>Figure 24: Reports Available to ePCS Users

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/029.png)

#### DEA Expiration Date Report

The DEA Expiration Date Report allows the user to display the report to the screen, or to print the output to a selected printer, for the selected report criteria (Figure 25).

1.  Select the CPRS System Access Value
- Choose Active to display only prescribers whose CPRS System Access is active.
- Choose DISUSERed / Terminated to display only prescribers whose CPRS System Access is *disusered* or *terminated.*
- Choose Both to display prescribers whose CPRS System Access is active or *disusered* / *terminated.*
2.  Select the Type of System Access Value
- Choose CPRS Providers Only to display only providers with access to CPRS.
- Choose All Eligible Providers to display all providers.
19. Select the Expiration Date Status Value
- Choose Expired to display only prescribers with a DEA Number whose expiration date is in the past.
- Choose No Expiration Date to display only prescribers with a DEA Number that does not have an expiration date.
- Choose Less than 30 Days to display only prescribers with a DEA Number which expires within 30 days.
- Choose Less than 90 Days to display only prescribers with a DEA Number which expires within 90 days.
20. Preview, Print or Cancel the Report
- Click the Preview button to launch a new window containing the report output based on the selection criteria.
- Click the Print button to open a dialog window allowing the user to direct the report output to a print device.
- Click the Cancel button to return the user to the ePCS GUI Main Menu.

<span id="_Ref130818674" class="anchor"></span>Figure 25: DEA Expiration Date Report Selection Criteria

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/030.png)

The DEA Expiration Date Report (Figure 26) includes the following fields:

- Term Date – The date the DEA Number expires. The source is the NEW PERSON file (#200), TERMINATION DATE field (#9.2).
- Name – The name of the prescriber to whom the DEA Number is assigned. The source is the NEW PERSON file (#200), NAME field (#.01).
- DEA – The DEA Number associated with the record. The source is the DEA NUMBERS file (#8991.9), DEA field (#.01).
- DEA Exp Dt – The expiration date of the record as found in the DOJ file. The source is the DEA NUMBERS file (#8991.9), EXPIRATION DATE field (#.04).
- Last Sign-On – The date the prescriber last signed in to VistA. The source is the NEW PERSON file (#200), LAST SIGN-ON DATE/TIME field (#202).
- Title – The title of the prescriber as found in the TITLE field (#8) of the NEW PERSON file (#200), which is a pointer to the NAME field (#.01) in the TITLE file (#3.1).
- Service/Section – The medical service or section to which the prescriber is assigned. The source is the NEW PERSON file (#200), SERVICE/SECTION field (#29).
- Remarks – Free text entered by the user.

After previewing the report, the user will have the option to print or close the report as shown in Figure 26.

<span id="_Ref130811365" class="anchor"></span>Figure 26: Report Preview — DEA Expiration Date Report

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/031.png)

#### Print Prescribers with Privileges

The Print Prescribers with Privileges report (Figure 27) displays all active users who have privileges to any of the controlled substance schedules II through V -and- have a DEA \# or VA \#. This report requires no selection criteria.

1.  Preview, Print, or Cancel the Report
- Click the Preview button to launch a new window containing the report output.
- Click the Print button to open a dialog window allowing the user to direct the report output to a print device.
- Click the Cancel button to return the user to the ePCS GUI Main Menu.

<span id="_Ref144800525" class="anchor"></span>Figure 27: Print Prescribers with Privileges Selection Criteria

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/032.png)

<span class="mark"></span>Figure 28 shows the output for the Print Prescribers with Privileges option. The report includes the following fields:

- Division - The site where the prescriber has privileges. The source is the INSTITUTION file (#4), NAME field (#.01).
- Name – The name of the prescriber to whom the DEA number is assigned. The source is the NEW PERSON file (#200), NAME field (#.01).
- DUZ – The DUZ associated with the prescriber. The source is the Internal Entry Number (IEN) of the record in the NEW PERSON file (#200).
- DEA \# – The DEA Number assigned to the prescriber. The source is the NEW PERSON file (#200), NEW DEA \#’S multiple (#53.21), DEA NUMBER field (#.01). An ‘(E)’ appended to the DEA \# indicates that the DEA \# is expired.
- VA# – The VA Number assigned to the provider. The source is the NEW PERSON file (#200), VA# field (#53.3).
- Inpat – Indicates whether or not this DEA Number will be used for inpatient orders. The source is the DEA NUMBERS file (#8991.9), USE FOR INPATIENT ORDERS? field (#.06).

After previewing the report, the user will have the option to print or close the report.

<span id="_Ref130811295" class="anchor"></span>Figure 28: Report Preview — Print Prescribers with Privileges

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/033.png)

#### Print DISUSER Prescriber with Privileges

The Print DISUSER Prescriber with Privileges report displays all DISUSER users who have privileges to any of the controlled substance schedules II through V -and- have a DEA \# or VA \#. This report requires no selection criteria, as shown in Figure 29.

1.  Preview, Print or Cancel the Report
- Click the Preview button to launch a new window containing the report output.
- Click the Print button to open a dialog window allowing the user to direct the report output to a print device.
- Click the Cancel button to return the user to the ePCS GUI Main Menu.

<span id="_Ref130820735" class="anchor"></span>Figure 29: Print DISUSER Prescriber with Privileges Selection Criteria

![Figure 30 shows the output for the Print DISUSER Prescriber with Privileges option. The report includes the following fields:](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/034.png)

*Figure 30 shows the output for the Print DISUSER Prescriber with Privileges option. The report includes the following fields:*

- Division - The site where the prescriber has privileges. The source is the INSTITUTION file (#4), NAME field (#.01).
- Name – The name of the prescriber to whom the DEA Number is assigned. The source is the NEW PERSON file (#200), NAME field (#.01).
- DUZ – The DUZ associated with the prescriber. The source is the Internal Entry Number (IEN) of the record in the NEW PERSON file (#200).
- DEA \# – The DEA Number assigned to the prescriber. The source is the NEW PERSON file (#200), NEW DEA \#’S multiple (#53.21), DEA NUMBER field (#.01). An ‘(E)’ appended to the DEA \# indicates that the DEA \# is expired.
- Termination Date – The date the provider’s privileges to prescribe controlled substances was terminated. The source is the DEA NUMBERS file (#8991.9), EXPIRATION DATE field (#.04).
- Inpat – Indicates whether or not this DEA Number will be used for inpatient orders. The source is the DEA NUMBERS file (#8991.9), USE FOR INPATIENT ORDERS? field (#.06).

After previewing the report, the user will have the option to print or close the report.

<span id="_Toc477526774" class="anchor"></span>Figure 30: Report Preview — Print DISUSER Prescriber with Privileges

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/035.png)

#### Changes to the DEA Prescribing Privileges Report

This option allows the user to display, print or export ePCS data for a specified date range.

Refer to Figure 31 to view the report selection screen.

1.  Select a date range
2.  Export, Preview, Print, Export or Cancel the Report
- Click the Export button to send the report output to a Microsoft Excel spreadsheet. The data can then be sorted and filtered using functionality found in Excel.
- Click the Preview button to launch a new window containing the report output based on the selection criteria.
- Click the Print button to open a dialog window allowing the user to direct the report output to a print device.
- Click the Cancel button to return the user to the ePCS GUI Main Menu.

<span id="_Ref130811135" class="anchor"></span>Figure 31: Changes to the DEA Prescribing Privileges Report Selection Criteria

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/036.png)

<span class="mark"></span>Figure 32 shows the output for the Changes to the DEA Prescribing Privileges Report option. The report includes the following fields:

- Division - The site where the prescriber has privileges. The source is the INSTITUTION file (#4), NAME field (#.01) based on the value in the NEW PERSON file (#200), DIVISION multiple (#16), DIVISION field (#.01).
- Name – The name of the prescriber for whom the information was modified. The source is the NEW PERSON file (#200), NAME field (#.01) based on the value in the XUEPCS DATA file (#8991.6), NAME field (#.01).
- Edited By – The name of the user who made the changes. The source is the NEW PERSON file (#200), NAME field (#.01), based on the value in the XUEPCS DATA file (#8991.6), EDITED BY field (#.02).
- Field Edited – The field that was changed. The source is the XUEPCS DATA file (#8991.6), FIELD EDITED field (#.03).
- Original Data – The value of the field prior to the change. The source is the XUEPCS DATA file (#8991.6), ORIGINAL DATA field (#.04).
- Edited Data – The value of the field after the update. The source is the XUEPCS DATA file (#8991.6), EDITED DATA field (#.05). If the FIELD EDITED indicates the field resides in the NEW PERSON file (#200), “(Source: File \#200)” will be appended to the value on the report.
- Date Edited – The date the information was changed. The source is the XUEPCS DATA file (#8991.6), DATE/TIME EDITED field (#.06).

When the last record is processed for a Division, a footer is printed which lists all divisions to which a user is defined. The source of that information is the INSTITUTION file (#4), NAME field (#.01) based on the NEW PERSON file (#200), DIVISION multiple (#16), DIVISION field (#.01).

After previewing the report, the user will have the option to export the output to an Excel spreadsheet, print the output, or close the report.

<span id="_Toc477526779" class="anchor"></span>Figure 32: Report Preview — Changes to the DEA Prescribing Privileges Report

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/037.png)

To export the data to an Excel spreadsheet, click the Export button. A progress bar, similar to that shown in Figure 33, will be displayed.

<span id="_Ref130810980" class="anchor"></span>Figure 33: Export Progress Bar

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/038.png)

When all rows are exported, the Excel spreadsheet opens. The data are displayed as shown in Figure 34.

<span id="_Ref130810834" class="anchor"></span>Figure 34: Changes to DEA Privileges Excel Spreadsheet

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/039.png)

#### Logical Access Control Audit Report

This option allows the user to display or print ePCS data for a specified date range. Refer to <span class="mark"></span>Figure 35 to view the report selection screen.

1.  Select a date range.
3.  Preview, Print or Cancel the Report
- Click the Preview button to launch a new window containing the report output based on the selection criteria.
- Click the Print button to open a dialog window allowing the user to direct the report output to a print device.
- Click the Cancel button to return the user to the ePCS GUI Main Menu.

<span id="_Toc477526645" class="anchor"></span>Figure 35: Logical Access Control Audit Report Selection Criteria

![Figure 36 shows the output for the Logical Access Control Audit Report option. The report includes the following fields:](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/040.png)

*Figure 36 shows the output for the Logical Access Control Audit Report option. The report includes the following fields:*

- SITE: The facility for which the access was changed. The source is the INSTITUTION file (#4), NAME field (#.01), based on the value in the OE/RR EPCS PARAMETERS file (#100.7), SITE NAME field (#.01).
- DIVISION: - The division where the prescriber has privileges. The source is the INSTITUTION file (#4), NAME field (#.01).
- USER – The name of the prescriber for whom the information was modified. The source is the AUDIT file (#1.1). For users whose access is enabled, the source is the OLD INTERNAL VALUE field (#2.1); for users whose access is disabled, the source is the NEW INTERNAL VALUE field (#3.1).
- Detail Line – Each detail line is comprised of:
- The action. The presence of the 2.1 node indicates the user access was enabled; the presence of the 3.1 node indicates the user access was disabled.
- The date and time the action occurred. The source is the AUDIT file (#1.1), DATE/TIME RECORDED field (#.02).
- The name of the person who changed the record. The source is the AUDIT file (#1.1), USER field (#.04).
- The option used to change the value. The source is the OPTION file (#19), NAME field (#.01), based on the value in the AUDIT file (#1.1), MENU OPTION USED field (#4.1).

After previewing the report, the user will have the option to print the output or close the report.

<span id="_Ref130819687" class="anchor"></span>Figure 36: Report Preview - Logical Access Control Audit Report

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/041.png)

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections present some typical problems experienced by end users and the corresponding resolutions.

## Access Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users need a PIV card with at least one valid certificate to use the ePCS GUI.

## Log-On Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS GUI is usually accessed through a desktop shortcut which points to the installation location. Ask the local support staff for assistance.

If the ePCS GUI launches and then disappears, or is not responding, make sure the IP address listed is correct and not blocked by firewall software for the system with which it is communicating. Local support staff is available to assist with issues.

## GUI Appears Distorted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the ePCS GUI display appears to be missing scrollbars, columns, or rows, ensure that the screen resolution is set to a minimum resolution of 1440 dpi x 900 dpi. Settings available will be dependent upon the user’s monitor size.

### Example of Setting the Screen Resolution to 1920 x 1080

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Right-click on the computer desktop to open the Desktop Context Menu shown in Figure 37.
2.  Select “Display settings” from the menu to see the window shown in Figure 38.

<span id="_Ref130810214" class="anchor"></span>Figure 37: Desktop Context Menu — Display Settings

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/042.png)

<span id="_Toc71276257" class="anchor"></span>Figure 38: Windows Display Resolution Settings

![](eprescribing-controlled-substances-epcs-graphical-user-interface-gui-software-ve/043.png)

21. Scroll down to view Scale and Layout settings.
22. Select 1920 x 1080 from the Display Resolution dropdown menu.

    NOTE: Depending on the user's version of Windows, this may look different.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark"></span>Table 2 lists the acronyms and abbreviations used throughout this document.

| Acronym  | Description                                                                                                                                                           |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2FA      | Two-Factor Authentication                                                                                                                                             |
| ADPAC    | Automated Data Processing Application Coordinator                                                                                                                     |
| CPRS     | Computerized Patient Record System                                                                                                                                    |
| DOJ      | Department of Justice                                                                                                                                                 |
| ePCS     | e-Prescribing Controlled Substances                                                                                                                                   |
| EPCSPROV | Name of contrived ePCS Prescriber                                                                                                                                     |
| FY       | Fiscal Year                                                                                                                                                           |
| GUI      | Graphical User Interface                                                                                                                                              |
| IEN      | Internal Entry Number                                                                                                                                                 |
| OIT      | Office of Information and Technology                                                                                                                                  |
| ORES     | A Security Key given to users that are authorized to write orders in the patient chart. A user with this key can verify patient orders using an electronic signature. |
| PBM      | Pharmacy Benefits Management                                                                                                                                          |
| PIN      | Personal Identification Number                                                                                                                                        |
| PIV      | Personal Identity Verification                                                                                                                                        |
| SSO      | Single Sign-on                                                                                                                                                        |
| VA       | Veterans Affairs                                                                                                                                                      |
| VAMC     | Veterans Affairs Medical Center                                                                                                                                       |
| VDL      | VA Software Document Library                                                                                                                                          |
| VHA      | Veterans Health Administration                                                                                                                                        |
| VISN     | Veterans Integrated Service Network                                                                                                                                   |
| VistA    | Veterans Health Information Systems and Technology Architecture                                                                                                       |

<span id="_Ref130819894" class="anchor"></span>Table 3: Glossary Terms

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists some of the terms used throughout this document.
| Term                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Computerized Patient Record System (CPRS) | Parameters are set up/maintained by the facility’s CPRS Coordinator/Clinical Application Coordinator (CAC).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ePCS GUI                                  | Software designed to provide a means to update the controlled substance schedules assigned to a prescriber.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Graphical User Interface (GUI)            | A type of display format that enables users to initiate applications and execute commands by selecting pictorial representations (icons) via a mouse or a keyboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Internal Entry Number (IEN)               | The number used to identify a record within a file. Every record has a unique internal entry number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Prescriber                                | The licensed individual prescribing medication to a patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Security Key                              | Security Keys set a layer of protection on the range of computing capabilities available with a particular software application. The availability of options is based on the level of system access granted to each user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Suffix                                    | A locally recognized three- to ten-character value assigned in conjunction with an institutional DEA Number. It allows the site to uniquely identify prescribers assigned the DEA Number for the facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verify Code                               | A secret password used along with the Access Code to provide secure user access to the VistA M Server. It is used by Kernel's Sign-on / Security system along with the Access code to validate the user's identity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VistA                                     | Veterans Health Information Systems and Technology Architecture (VistA) is the proprietary software developed for, and used by, the VHA to support its clinical and administrative functions at VA sites nationwide. It is comprised of both client- and server-based software. The client-based software is written in Java, Delphi Object Pascal, and other GUI-based languages; it runs on the Microsoft operating system. The server-based software is written in the M programming language and, via Kernel, runs on all major M implementations regardless of the vendor. It is comprised of integrated clinical, infrastructure, and financial/administrative software applications. This internally developed portfolio of applications is recognized as the most comprehensive integrated health information system in the United States. |
