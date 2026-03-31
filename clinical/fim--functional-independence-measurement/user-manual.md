---
title: Functional Independence Measurement (FIM) Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: FIM
app_name: Functional Independence Measurement
section: CLI
app_status: active
pkg_ns: FIM
patch_ver: 1
patch_id: FIM*1
group_key: "FIM:FIM:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC). The FIM is an 18-item, 7-level functional assessment
audience: 
keywords: 
  - class
  - table
  - contents
  - even
  - patient
  - functional
  - independence
  - manual
  - measurement
  - version
page_count: 0
word_count: 12596
section_count: 44
table_count: 18
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: May 2003
revision_count: 4
revision_newest: 2/21/2017
revision_oldest: 4/03/2003
docx_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Func_Indep_Meas/fim_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=134"
---

---
title: |
  ![](functional-independence-measurement-fim-version-1-user-manual/001.png)

  Functional Independence Measurement (FIM) User Manual

  ![](functional-independence-measurement-fim-version-1-user-manual/002.png)

  Version 1.0

  May 2003

  Department of Veterans Affairs

  VistA System Design and Development
---

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Related Manuals](#related-manuals)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [Online Help](#online-help)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [VistA Intranet](#vista-intranet)
- [Orientation](#orientation)
- [Overview](#overview)
  - [FIM Features](#fim-features)
  - [What FIM Will Do](#what-fim-will-do)
  - [What FIM Will Not Do](#what-fim-will-not-do)
  - [FIM Process Flow](#fim-process-flow)
  - [## Sign In to FIM](#sign-in-to-fim)
  - [Interface Notes](#interface-notes)
  - [Exit](#exit)
- [Getting Started](#getting-started)
  - [Patient Selection Window Overview](#patient-selection-window-overview)
  - [Selecting a Patient](#selecting-a-patient)
- [Main FIM Windows](#main-fim-windows)
  - [VISTA Sign-on Window](#vista-sign-on-window)
  - [Main FIM Window](#main-fim-window)
- [FIM Tabs](#fim-tabs)
  - [About Tabs](#about-tabs)
  - [Pt/Program Tab](#ptprogram-tab)
  - [Dates and Dx Tab](#dates-and-dx-tab)
  - [Admission Tab](#admission-tab)
  - [Interim Tab](#interim-tab)
  - [Discharge Tab](#discharge-tab)
  - [Notes Tab](#notes-tab)
  - [Goals Tab](#goals-tab)
  - [Finished Tab](#finished-tab)
  - [Follow Up Tab](#follow-up-tab)
- [Tools and Associated Terms](#tools-and-associated-terms)
  - [Scoring Key](#scoring-key)
  - [Progress Notes](#progress-notes)
  - [Check Box](#check-box)
  - [Date Field](#date-field)
  - [Drop-down List](#drop-down-list)
  - [Command Button](#command-button)
  - [Radio Button](#radio-button)
  - [Tab Key](#tab-key)
  - [Cancel](#cancel)
- [User Operation](#user-operation)
  - [Opening FIM](#opening-fim)
  - [Creating a Patient FIM Record](#creating-a-patient-fim-record)
  - [Editing a Record](#editing-a-record)
  - [Discharging a Patient in FIM](#discharging-a-patient-in-fim)
- [Appendix A](#appendix-a)
  - [Acronyms](#acronyms)
- [Appendix B](#appendix-b)
  - [Definitions](#definitions)
- [Appendix C](#appendix-c)
  - [References](#references)
- [Glossary](#glossary)
- [Index](#index)
|           |                                                |
|-----------|------------------------------------------------|
| Date      | Description                                    |
| 4/03/2003 | Created by <span class="mark">REDACTED</span>  |
| 4/22/2003 | Updates by <span class="mark">REDACTED</span>  |
| 5/02/2003 | Updates by <span class="mark">REDACTED</span>  |
| 2/21/2017 | Updates by <span class="mark">REDACTED</span>. |
TABLE OF CONTENTS

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the Austin Automation Center (AAC). The FIM is an 18-item, 7-level functional assessment designed to evaluate the amount of assistance required by a person with a disability to perform basic life activities safely and effectively.

There are five types of FIM assessments: admission, goals, interim, discharge, and follow-up.

The FIM assessments are used clinically to monitor the outcomes of rehabilitative care as required by the Joint Commission on the Accreditation of Health Care Organizations (JCAHO) and the Commission on the Accreditation of Rehabilitative Facilities (CARF). According to VHA Directive 2000-16, medical centers are mandated to measure and track rehabilitation outcomes on all new stroke, lower-extremity amputees, and traumatic brain injury (TBI) patients using the FIM.

Finally, the Performance Measurement Workgroup of the Department of Veterans Affairs Central Office (VACO) approved a Network Director Performance Measure for rehabilitation for FY03 that requires the collection of FIM data. FIM Version 1.0 should greatly ease the burden placed on rehabilitation professionals in the field who are working to comply with the new performance measure.

FIM provides a Graphic User Interface (GUI) front-end programmed in Delphi to allow multiple clinicians to input FIM data for a given patient. This documentation then becomes available in CPRS as a progress note with addendums and/or a completed consults. The GUI front-end gathers demographic data as well as other required data by FSOD from VistA, therefore, eliminating the need for the clinician search of VistA for the information and re-enter for FIM.

FIM data is then placed in a VistA FileMan file for Health Level Seven (HL7) transmission to the FSOD at ACC.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Health Administration (VHA) clinicians who document medical records as progress notes and/or responses to a consult.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Function Independence (FIM) Installation Guide, V.1.0Functional Independence (FIM) Technical Manual and Security Guide, V.1.0*

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA FIM software files and Installation and Implementation Guide (i.e., RMIM1_0IG.PDF) are available on the following Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directories.

|                |                                    |                                    |
|----------------|------------------------------------|------------------------------------|
| OIFO           | FTP Address                        | Directory                          |
|  Albany        | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Hines          | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| Salt Lake City | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

VistA FIM software and documentation are distributed as the following set of files:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File Name</td>
<td>Contents</td>
<td>Retrieval Format</td>
<td>File Size</td>
</tr>
<tr class="even">
<td>RMIM1_0.KID</td>
<td>KIDS build</td>
<td>ASCII</td>
<td>219,648 bytes</td>
</tr>
<tr class="odd">
<td>RMIM1_0.ZIP</td>
<td>FIM Executable</td>
<td>BINARY</td>
<td>1,121,792 bytes</td>
</tr>
<tr class="even">
<td>RMIM1_0IG.pdf<br />
RMIM1_0IG.doc</td>
<td>Installation Guide</td>
<td>BINARY</td>
<td><p>1,350 bytes</p>
<p>28,570 bytes</p></td>
</tr>
<tr class="odd">
<td>RMIM1_0TM.pdf<br />
RMIM1_0TM.doc</td>
<td>Technical Manual and Security Guide</td>
<td>BINARY</td>
<td><p>2,460 bytes</p>
<p>17,530 bytes</p></td>
</tr>
<tr class="even">
<td>RMIM1_0UM.pdf<br />
RMIM1_0UM.doc</td>
<td>User’s Manual</td>
<td>BINARY</td>
<td>19,350 bytes<br />
29,130 bytes</td>
</tr>
</tbody>
</table>

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions, procedures, and other information are available from the FIM online help file. To access the Help file, select Help\|Contents from the menu bar or press F1 while you have any FIM screen dialog open.

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user’s response in this manual is in bold type, but does not appear on the screen as bold. The bold part of the entry is the letter or letters that you must type so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the Return key (or the Enter key for some keyboards). Whenever the Return or Enter key should be pressed, you will see the symbol \<RET\> or \<Enter\>. This symbol is not shown but is implied if there is bold input.

Within the roll and scroll part of the system, Help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. You can find this information enclosed in brackets, for example, \[type ward name here\]*,* and will not appear on the screen.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|        |                                                                                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------|
| Symbol | Description                                                                                                       |
|        | Used to inform the reader of general information including references to additional reading material. See example |
|        | Used to caution the reader to take special notice of critical information.                                        |

Table 1: Documentation Symbol Descriptions

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online documentation for this product is available on the intranet at the following address: [www.va.gov/vdl](http://www.va.gov/vdl). This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the Clinical Case Registries link, and it will take you to the FIM documentation.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Overview section provides a brief description of the Functional Independence Measurement (FIM) application.

GettingStarted provides information on entering the FIM application through selecting patient data.

Main FIM Windows gives an overview of the two main views used to navigate within the FIM application.

FIM Tabs provides outlines on the tabs used within the FIM application to enter and send patient information.

Tools and Associated Terms describes the various keys used in FIM and provides brief explanations of terms used within FIM application.

User Operation section gives instructions and screen capture examples on using the FIM application.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## FIM Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIM application allows the following:

- Multiple clinicians can input FIM data for a patient.
- Integrates documents in CPRS as a progress note with addendums and/or a completed consults.
- Gathers demographic data, as well as other required data by FSOD from VistA eliminating the need for the clinician to search VistA for the information and re-enter for FIM.
- Provides a VistA FileMan file for HL7 transmission to the FSOD at ACC.

## What FIM Will Do

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measurement (FIM) application allows multiple clinicians (inter-disciplinary assessment) to complete a FIM assessment and document it in the medical record as a progress note and/or as a response to a consult. The FIM application transmits this data to FSOD in Austin and creates a FSOD case in the database.

If the “Send to FSOD” option is chosen after completing the FIM assessment (either at one time or by multiple addenda), this will fulfill the requirements of the Network Performance Measure.

The FIM application shows multi-disciplinary, inter-disciplinary, or trans-disciplinary patient assessment with a consistent assessment tool.

## What FIM Will Not Do

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FIM will not totally eliminate data entry or data management responsibilities for the FSOD coordinator. It will not fulfill the requirements of the VISN Performance measure if you don’t elect to send the data to the FSOD.

|     |                                                                                              |
|-----|----------------------------------------------------------------------------------------------|
|     | Writing a note in the medical record alone is not enough to fulfill the performance measure. |

FIM will not totally complete the FSOD case in Austin. Some data elements will still need to be completed in the FSOD, such as:

\#16 English Language

\#33 Admit From

\#34 Prehospital Living Setting

\#35 Prehospital Living With

\#36 Vocational Category

\#37 Vocational Effort

\#38 Discharged to Living Setting

\#39 Discharged to Living With

FIM will not allow you to save a note without a signature if you are sending the data to FSOD. The system does not complete bed service-CDR information on the continuum page.

FIM does not send data to NOMS or to the SCI Registry.

## FIM Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](functional-independence-measurement-fim-version-1-user-manual/003.png)

FIM Process Flow

## ## Sign In to FIM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you can sign in to FIM, you will need to use your PIV PIN or obtain an access code and a verify code. Typically, your Clinical Coordinator issues these codes.

Follow these steps to sign in:

1.  Double-click the FIM icon on your desktop. The VistA logo window and the VISTA Sign-on dialog will appear.
2.  If the Connect To dialog appears, click the down-arrow, select the appropriate account (if more than one exists), and click OK.
3.  Select your PIV credentials.
4.  Enter your PIV PIN.
5.  Type your access code into the Access Code field and press the Tab key.
6.  Type the verify code into the Verify Code field and either click the \<Enter\> or click OK.

> **NOTE:** You can also type the access code, followed by a semicolon, followed by the verify code. Once you have done this click the \<Enter\> or click OK.

## Interface Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here are some hints and tips to help you navigate in the application:

- If you are accustomed to using the keyboard exclusively, you can continue to do so with Windows. You can use the keyboard to select menus and menu items.
- To select a menu, you press the ALT key and then the letter in the menu title that is underlined. For example, to bring up the File menu, you press ALT + F because the F in File is underlined showing that it is the quick key.
- To select a menu item when the menu is displayed, you type the underlined letter of the desired menu item (rather than clicking with your mouse). Continuing the above example, if you had brought up the File menu and wanted to choose Select New Patient, you would then type n.
- The dots (ellipses) after a menu item or command button item indicate that another dialog box will open when you choose these items or buttons.

## Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select File \| Exit, if you have no unsigned orders or notes, the patient chart closes and you exit completely from FIM. If you have unsigned orders or notes, you will be prompted to save them before you can close FIM.

If you do have unsigned orders or notes, the Review/Sign Changes dialog box appears. Your ability to determine whether orders should be saved with a signature, do not require a signature, or can be saved without a signature (by checking the options at the bottom of the dialog) depends on the key you have been assigned and the kind of order.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Selection Window Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you log in to FIM, the Patient Selection window is the first thing to appear. You can type a patient's name, Social Security Number (SSN), or the first letter of the patient's last name and the last four digits of the patient's SSN (P5555) and press \<Ret\>.

If you want to cancel the transaction, click Cancel. If you want to select a new patient, go to File \| Select New Patient and the Patient Selection window appears

## Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To select a patient, you can type either part or all of their name or Social Security number. For example, you can use:

- The first letter of the patient's last name and the last four digit of the patient's Social Security number (P5555)
- The full Social Security number (with or without dashes). You can include a "P" as the last character (123-44-5555, 123445555, 123-44-5555s, or 12344555p)

When you stop typing, press \<Ret\> and FIM will use what you entered to search the patient list and bring up that part of the patient list. Highlight a possible match, and click OK to select the patient, or click Cancel to select another patient or exit.

If you select File \| Select New Patient:

1.  In the Patient Selection window, use one of the following methods to choose a patient:
7.  Type the patient's Social Security number with or without dashes (123-44-5555 or 123445555), or the full Social Security number with "P" as the last character (123-44-5555p, or 123445555p).
8.  Type all or part or all of the patient's name
9.  Type the first letter of the patient’s last name and the last four digit of the patient’s Social Security number (p5555).

FIM will try to match what you entered to a patient in the database and highlight that patient.

10. In the Patients List window, locate the patient's name (scrolling if necessary) and click it once.
11. Verify that the correct patient is highlighted. If the correct patient is highlighted, click OK. If the correct patient is not highlighted, scroll through to find the correct patient, highlight the name, and click OK.
12. When you click OK, FIM opens a popup window that says, "Do you wish to send your date to FSOD?"

> **NOTE:** You will only see the Confirm window if you have a key to populate the Functional Status and Outcomes Database (FSOD) database in the Austin Automation Center (ACC).

The patient's name and other information will appear after the Confirm window unless this record is considered sensitive.

# Main FIM Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VISTA Sign-on Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need an active PIV or an access code and verify code to log in to FIM. At the VISTA Sign-on window, type the access code, press Tab, enter the verify code, and press \<Enter\> or click OK. The Main FIM window opens.

## Main FIM Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Main FIM window provides tabs at the bottom of the window used to navigate within the FIM application. What is visible on your screen depends on the tab you select in the main window body. Depending on the tab you select, you may not see all tabs when you are working in that particular window.

# FIM Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access most windows in FIM, you click the appropriate tab at the bottom of the main window.

![](functional-independence-measurement-fim-version-1-user-manual/004.png)

Associated FIM Tabs

## Pt/Program Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PT/Program tab allows you to view and select additional patient information. You can view the patient's code, birth date, and address. You can also click the drop-down fields to select the patient's gender, ethnicity, and military status.

After you select a facility code, you have a choice to pick an existing episode (if one exits) or start a new episode.

## Dates and Dx Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dates and Dx tab allows you to enter dates for Therapy Start Date, Admission Class, and Therapy End Date. Once you enter a Discharge date and send the note, you will not be able to add data to the Admission, Interim, and Discharge assessments

- If you are only doing an admission, the Therapy End date should not be entered.
- For continuum care type, the label will be Therapy Start Date and Therapy End Date.
- For Acute and Sub Acute Care Types, the label will be Rehab Bed Unit Admission and Rehab Bed Unit Discharge.

## Admission Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you selected Admission assessment type, the Admission tab for FIM scores appears. You can enter FIM scores in the Admissions tab for a patient's ability to have self-care, sphincter control, transfers, locomotion, communication, and social cognition.

## Interim Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you selected Interim assessment type, the Interim tab for FIM scores appears. You can enter FIM scores in the Interim tab for a patient's ability to self-care, sphincter control, transfers, locomotion, communication, and social cognition.

## Discharge Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you selected Discharge assessment type, the Discharge tab for FIM scores appears. You can enter FIM scores in the Discharge tab for a patient's ability to self-care, sphincter control, transfers, locomotion, communication, and social cognition.

## Notes Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Notes tab allows you to enter additional information to the Progress Note. The Progress Notes are saved and appear for viewing the next time you update a note. The Case Notes are only for the FSOD record.

## Goals Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Goals tab includes score boxes for Self Care, Sphincter Control, Transfers, Locomotion, Communications, Expression, and Social Cognition, with subcategories for each.

When you enter the scores, FIM provides a Motor Subtotal and a Cognitive Subtotal, along with a Total Score (FIM Total Score). The Score Key button at the bottom of the window accesses the Score Key, which contains each score number and the associated rating explanation.

## Finished Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Finished tab displays the Progress Notes window with the patient's progress information. You can send the Progress Notes to VistA by clicking Send.

## Follow Up Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Follow Up tab includes score boxes for Self Care, Sphincter Control, Transfers, Locomotion, communications, Expression, and Social Cognition, with subcategories for each.

When you enter the scores, FIM provides a Motor Subtotal and a Cognitive Subtotal, along with a Total Score (FIM Total Score). The Score Key button at the bottom of the window accesses the Score Key, which contains each score number and the associated rating explanation.

# Tools and Associated Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Scoring Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you enter the patient's FIM Scores on the Goals tab, you may want to review the FIM Levels for each number. To do this, click the Scoring Key at the bottom of the window to display the FIM Levels Scoring Key popup.

## Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Progress Notes are contained in the window accessed by selecting the Finished tab.

## Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A checkbox toggles between a YES or NO, ON or OFF setting. Checkboxes are usually a square box containing a check mark or an X. Clicking the box or pressing the spacebar toggles the check box setting.

## Date Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Date fields are identified by "\_\_/\_\_/\_\_" or a date "mm/dd/yy". Often, date fields have an associated pop-up calendar. Double clicking with the mouse inside the date edit box, or tabbing to the edit box and then pressing the F2 key, displays the calendar. Clicking on the desired date, or using the arrow keys to move to a date and then pressing the spacebar, selects the date. Each component of the date (month/day/year) must consist of two characters (i.e., 02/02/96). The selected entry will not be effective until you tab off or exit from the date field.

## Drop-down List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A drop-down list is a box that contains an arrow on the right side. When clicking on the arrow, a vertical list of choices is displayed. You can select the entry you want by clicking the list entry. You cannot type in this box; only select an item from the list. Once an entry is selected, it cannot be deleted - only changed. If \<None\> is the last entry, selecting it will clear the list entry. If \<More\> is the last entry, selecting it will display additional entries. The selected entry will not be effective until you tab off or exit from the drop down list.

## Command Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Command button initiates an action. It is a rectangular box with a label that specifies what the button does. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.

## Radio Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Radio buttons appear in sets. Each button represents a single choice, and only one button may be selected at any one time. For example, MALE or FEMALE may be offered as choices through two radio buttons. Click in the button to select the item required.

## Tab Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the TAB key to move the cursor from field to field. Do not use the RETURN key. The RETURN key is usually reserved for the default command button or action (except in menu fields).

## Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This cancels the latest entry (up until the OK or SAVE button is selected).

# User Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide detailed instructions for performing the following:

Opening FIM

Creating a Patient FIM Record

Addendums in FIM to a FSOD note

Editing a Record

Screen captures accompany the instructions, providing visual representation to further assist and familiarize users with the FIM application.

## Opening FIM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the FIM application, perform the following:

1.  With CPRS open, go to the Tools menu and select FIM.

![](functional-independence-measurement-fim-version-1-user-manual/005.png)

CPRS Tools Menu

If you are passing parameters from the CPRS tools menu, you will not be prompted for patient selection.

![](functional-independence-measurement-fim-version-1-user-manual/006.png)

Patient Selection Prompt

If you change a patient in CPRS, FIM will alert you that the template will terminate.

![](functional-independence-measurement-fim-version-1-user-manual/007.png)

FIM Termination Message

Pressing OK will terminate FIM and return you to CPRS.

![](functional-independence-measurement-fim-version-1-user-manual/008.png)

CPRS Tools Menu

Again, select FIM, and the Connect To dialog appears.

![](functional-independence-measurement-fim-version-1-user-manual/009.png)

Connect To Dialog

13. Click OK.
14. Select your PIV credentials.

    ![](functional-independence-measurement-fim-version-1-user-manual/010.png)
15. Enter your PIV PIN.

![](functional-independence-measurement-fim-version-1-user-manual/011.png)

The VISTA Sign-on dialog appears.

![](functional-independence-measurement-fim-version-1-user-manual/012.png)

VISTA Sign-on Dialog

16. Enter the same Access Code and Verify Code as your log on to CPRS and click OK.

You now have the FIM application open and can access patient information.

## Creating a Patient FIM Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access patient information, perform the following:

1.  Enter a patient’s name, Social Security number, or the initial of their last name and the last four numbers of their Social Security number.

![](functional-independence-measurement-fim-version-1-user-manual/013.png)

Patient Identifier Screen

A Patient List dialog appears similar to the Patient Name selection point in DHCP.

![](functional-independence-measurement-fim-version-1-user-manual/014.png)

Patient List Dialog

17. Select the patient information you want and click OK.

![](functional-independence-measurement-fim-version-1-user-manual/015.png)

Confirm Message

The Confirm message appears, “Do you wish to send your data to FSOD?” If you choose No, a template to write a note in CPRS appears.

![](functional-independence-measurement-fim-version-1-user-manual/016.png)

Pt/Program Tab

By default, FIM opens with the Pt/Program tab enabled. The Pt/Program tab brings in demographic information from the patient file in VistA. You can edit the Gender, Marital Status, Ethnicity, and Military Status fields by using the drop down lists and selecting the necessary data. Address information is available by clicking the Pt Address button.

![](functional-independence-measurement-fim-version-1-user-manual/017.png)

Demographic Dialog

Clicking Return takes you back to the Pt/Program screen.

![](functional-independence-measurement-fim-version-1-user-manual/018.png)

Confirm Message

Again, the Confirm message appears, “Do you wish to send your data to FSOD?”

18. Click Yes.

The Pt/Program screen now appears with a Facility Code drop down list.

> **NOTE:** This screen only has the Pt/Program tab and no Assessment Type field. A correct facility code must be entered before other information tabs or Assessment Type field are enabled.

![](functional-independence-measurement-fim-version-1-user-manual/019.png)

Pt/Program Field

19. Select a facility code.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td>For most users, there will be only one facility code, which appears by default. But, some users do have more than one. These are as follows:<br />
Continuum of care for patients outside the bed service<br />
Acute Rehab Inpatient Bed Unit<br />
Subacute Rehab Inpatient Bed Unit.<br />
For those with bed services, it is important that the correct facility code is selected. If the wrong facility is selected, and the template is completed, there will be no opportunity to edit it later.</td>
</tr>
</tbody>
</table>

20. After selecting the necessary facility code, in the Select an Episode box, click Enter New Episode.

![](functional-independence-measurement-fim-version-1-user-manual/020.png)

Select an Episode Field

The Assessment Type becomes available as well as additional information tabs.

![](functional-independence-measurement-fim-version-1-user-manual/021.png)

Assessment Type Field

21. Select the appropriate assessment type. In this case, Admission FIM. There now is an additional tab available at the bottom. For each assessment type chosen, there will be a corresponding new tab available.
22. Click the Dates and Dx tab.

![](functional-independence-measurement-fim-version-1-user-manual/022.png)

Dates and Dx Tab

The Dates and Dx page appears. This page is critical for data entry. All fields in this are necessary to ensure that data can be sent to FSOD in Austin without difficulty.

|     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | You are in the Continuum of Care facility at this point. You need to complete the Therapy Start Date. This is the date that the initial assessment was made by rehab personnel, not the admission date to the hospital. The patient needs to be medically stable. For example, for an amputation patient, it is the date after amputation that the patient is seen. Similarly, for a stroke patient, it is the date after the stroke (when the patient is medically stable) when therapy begins. |

For bed services, the Impairment Group and Date of Onset are additionally important if the patient has the potential of moving from an acute service to bed Service. These fields also allow the assessments to be linked in Austin.

Note in the following screen capture that by choosing a bed service, the date headings change to Rehab Bed Unit Admission and Rehab Bed Unit Discharge rather than Therapy Start Date and Therapy End Date.

![](functional-independence-measurement-fim-version-1-user-manual/023.png)

Therapy Start Date

In the Dates and Dx, you can use the Therapy Start Date drop-down list to get a calendar to appear.

![](functional-independence-measurement-fim-version-1-user-manual/024.png)

Therapy Start Date Drop-down Calendar

23. Select the appropriate date, and it is entered automatically.

    ![](functional-independence-measurement-fim-version-1-user-manual/025.png)

Date Automatically Entered

By clicking the Program Interrupted box, you have the opportunity to enter interruptions in a case.

|     |                                                                                                                                                                                                                                                         |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | This should be relatively rare. It is not recommended that you use this feature unless there is a return date. If the case is interrupted, and the patient does not continue with additional treatment, the case needs to be discharged not interrupted |

![](functional-independence-measurement-fim-version-1-user-manual/026.png)

Program Interrupted Box

Clicking on the Ellipsis (three dots) next to the Impairment Group box opens the available impairment codes. Clicking on a code places the appropriate numbers in the Impairment Group box. Certain codes are not available, such as 1; therefore, you must pick 1.1, 1.2, 1.3, 1.4, or 1.9. If you choose a code that is not available, you will receive a message that tells you to select another code.

![](functional-independence-measurement-fim-version-1-user-manual/027.png)

Impairment Group Box

24. ![](functional-independence-measurement-fim-version-1-user-manual/028.png)Click Return.

Date of Onset

25. Select the down arrow next to the Date of Onset box. This is the date that the impairment occurred, for example the date of the stroke or the date of the amputation.
26. ![](functional-independence-measurement-fim-version-1-user-manual/029.png) Enter the appropriate date.

Date of Impairment

ASIA Impairment is only available if you select a Traumatic Spinal Cord Injury code - 4.2xxx. Most of the time this will be left blank.

27. Click the Admission tab.

This opens the page that allows entry of the FIM Scores. All or part of the scores may be completed.

![](functional-independence-measurement-fim-version-1-user-manual/030.png)

Entering FIM Scores

In the previous screen capture, only the Self Care scores were entered. The Subtotal and Total Score fields will only complete scores if all 18 FIM items are entered.

Clicking on the Scoring Key gives the definitions each FIM Score.

![](functional-independence-measurement-fim-version-1-user-manual/031.png)

FIM Score Definitions

28. Click Notes. This takes you to an area for entering free text notes. These notes will be seen in the CPRS progress note but will not be sent to the FSOD.

![](functional-independence-measurement-fim-version-1-user-manual/032.png)

Text Notes Screen

29. Click the Goals tab.

![](functional-independence-measurement-fim-version-1-user-manual/033.png)

Goals Tab

Goal scores for the patient for each of the FIM items can be entered here. All or part of the scores may be completed. Just as in the Admission tab, the Subtotal and Total Score fields will only complete scores if all 18 FIM items are entered

30. Click the Finished tab.

![](functional-independence-measurement-fim-version-1-user-manual/034.png)

Finished Tab

The Finished screen shows what the note will look like in CPRS. You can scroll down to see what the rest of the note looks like.

> Note: The FIM Measurement definitions are automatically entered into the first note as a guide for readers.

31. If the note is acceptable, click Send.

![](functional-independence-measurement-fim-version-1-user-manual/035.png)

Progress Note

You have the option to complete a consult with this note. You will only be asked this if you are authorized to complete consults. Also, this question is only asked if there are consults available for this patient.

![](functional-independence-measurement-fim-version-1-user-manual/036.png)

Confirm Progress Note

If you choose Yes, the Consult Selection dialog appears with a list of consults for the patient.

![](functional-independence-measurement-fim-version-1-user-manual/037.png)

Consult Selection Dialog

32. Choose the appropriate consult.

If you choose to complete, you will see a double entry in CPRS; one that resides with the consult, one that resides in TIU progress notes. When adding an addendum to the record, it is the progress note that will be addended, not the response to the consult.

You need to associate the note with an inpatient stay or an outpatient visit. The system defaults to Hospital Admissions.

![](functional-independence-measurement-fim-version-1-user-manual/038.png)

Hospital Admissions Screen

All past hospital admissions will be seen; therefore, if the patient is an inpatient, click the appropriate inpatient stay. Send to VISTA will be highlighted.

33. Click Send to VISTA.

![](functional-independence-measurement-fim-version-1-user-manual/039.png)

Send to VISTA Option

If the patient is coming to the bed service from an acute care service within the hospital, or you are seeing the patient after they were transferred between acute care services, the Inpatient unit displayed will not match the floor the patient is now on. The inpatient stay defaults to the admitting service or floor regardless of how many times the patient may have been transferred during the admission.

34. If your entry requires a co-signature, you will need to click New under Cosigner to designate a cosigner.

> If you choose Clinic Appointments, you will get a range of clinic appointments to choose from.

![](functional-independence-measurement-fim-version-1-user-manual/040.png)

Clinic Appointments Screen

35. You can change the date in the Date Range field. You can also create a new visit through the template. To do this, in the Visit Selection field, select New Visit and type in the first three characters of the clinic. A list of clinics appears.

![](functional-independence-measurement-fim-version-1-user-manual/041.png)

List of Clinics Screen

When you choose a clinic from the list, Send to VISTA becomes active.

> **NOTE:** This is an event historical visit, which does not require check out and is not billable. It is also counted differently than a true visit and not intended to be used for inpatients. You should probably always try to associate the note with a scheduled outpatient visit rather than choosing this option.

36. If the correct appointment is shown, select it and Click Send to VISTA.

The Sign Note dialogue box appears

![](functional-independence-measurement-fim-version-1-user-manual/042.png)

Sign Note Dialogue

37. Sign the note and click OK.

> **NOTE:** You have the option of canceling, but if you do, all information will be lost.

The Information dialog appears indicating that an e-mail will be sent to the FSOD Coordinator(s).

38. Click OK.

![](functional-independence-measurement-fim-version-1-user-manual/043.png)

E-mail Confirmation Message

The Confirm dialog appears asking, “Would you like to select another patient?”

![](functional-independence-measurement-fim-version-1-user-manual/044.png)

Confirm Dialog

For our purposes here, we would select No.

The following is an example of the e-mail that goes to the coordinators group. An additional response is added each time there is an addition to the FIM template.

![](functional-independence-measurement-fim-version-1-user-manual/045.png)

Example E-mail to Coordinators

To create an addendum in FIM to a FSOD note, you need to enter the FIM template the same way as described previously. When prompted, “Do you wish to send your data to FSOD?” select Yes.

When you select the facility, you will see an existing case in the Select an Episode field along with the Enter New Episode option. If you have multiple facilities, it is very important that the correct facility be selected in order to see the case that was entered earlier and for the data to link both in CPRS and in the FSOD.

![](functional-independence-measurement-fim-version-1-user-manual/046.png)

Addendums in FIM to a FSOD Note

Clicking on the existing case in the Select an Episode field opens the Assessment Type box.

![](functional-independence-measurement-fim-version-1-user-manual/047.png)

Assessment Type Box

1.  Select the Admission FIM.

![](functional-independence-measurement-fim-version-1-user-manual/048.png)

Admission Tab Enabled

> **NOTE:** An additional tab “Admission” becomes available.

Data in any of the boxes that was not previously filled in can be completed when entering an addendum.

> **NOTE:** In the Dates and Dx tab, previously entered data is visible (the grayed entries), but it cannot be changed.

![](functional-independence-measurement-fim-version-1-user-manual/049.png)

Previous Data Example

39. Select the Admission tab. The numbers that were previously completed are visible but not editable (again grayed out).

![](functional-independence-measurement-fim-version-1-user-manual/050.png)

Admission Tab

In the above screen, the scores have been completed. Once the final score is entered, the subtotal and total scores calculate.

> **NOTE:** There can be as many additions as needed to complete the scoring.

Free text notes can be added in the Notes tab. Notes entered previously are visible to the person adding to the note.

![](functional-independence-measurement-fim-version-1-user-manual/051.png)

Notes Tab

Goal scores are optional but can be added. If goals scores are added, they are sent to the FSOD.

![](functional-independence-measurement-fim-version-1-user-manual/052.png)

Goal Scores

Selecting the Finished tab allows you to see how the note will look in CPRS.

![](functional-independence-measurement-fim-version-1-user-manual/053.png)

Finished Tab

Finishing the note is the same as previously shown.

Clicking on Send button gives the option of completing a consult.

![](functional-independence-measurement-fim-version-1-user-manual/054.png)

Sign Note Dialog

40. Sign the note and click OK.

![](functional-independence-measurement-fim-version-1-user-manual/055.png)

E-mail Sent to FSOD Message

The Information dialog appears indicating that an e-mail will be sent to the FSOD Coordinator. This e-mail occurs each time that an addendum is added to a record that is being sent to FSOD.

41. Click OK.

![](functional-independence-measurement-fim-version-1-user-manual/056.png)

Reply to E-mail Example

The above screen shows the e-mail message that is generated. It is a reply to the initial e-mail.

## Editing a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Records can be edited in FIM. Several reasons for editing are as follows:

- A mistake is made in the scoring.
- A correction does not erase the note in CPRS; rather it creates an addendum to the existing note.
- New data can be sent to FSOD in Austin to update the record.

To edit a record, perform the following:

1.  Select the case that you want to edit.

![](functional-independence-measurement-fim-version-1-user-manual/057.png)

Select Patient Case

42. Select the episode of care and the assessment you want to change.

![](functional-independence-measurement-fim-version-1-user-manual/058.png)

Assessment Change

43. Choose the Admission tab

![](functional-independence-measurement-fim-version-1-user-manual/059.png)

Admission Tab

44. Go to Edit and select Edit.

> **NOTE:** This is only available to coordinators who have the coordinators key to the FIM Template.

![](functional-independence-measurement-fim-version-1-user-manual/060.png)

Edited FIM Scores

When Edit is selected, the previously grayed scores open and are editable. In this example, the bathing score have been changed from 1 to 2.

![](functional-independence-measurement-fim-version-1-user-manual/061.png)

Scoring Changes

|     |                                                                                           |
|-----|-------------------------------------------------------------------------------------------|
|     | It is recommended to write a note in the Notes tab to indicate the reason for the change. |

![](functional-independence-measurement-fim-version-1-user-manual/062.png)

Reason for Change Note

45. Select the Finished tab.

![](functional-independence-measurement-fim-version-1-user-manual/063.png)

Finished Tab

> **NOTE:** The bathing score has changed from 1 to 2. All the other items have remained the same.

46. Sign the note and click OK.

![](functional-independence-measurement-fim-version-1-user-manual/064.png)

Sign Note Dialog

The Information dialog appears indicating that an e-mail will be sent to the FSOD Coordinator.

47. Click OK.

![](functional-independence-measurement-fim-version-1-user-manual/065.png)

Information Dialog

## Discharging a Patient in FIM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To discharge a patient, enter in to the FIM application and perform the following:

1.  Select the case that you want to edit.

![](functional-independence-measurement-fim-version-1-user-manual/066.png)

Select Patient Case

48. After choosing the correct Facility Code and episode of care, choose the Discharge FIM assessment type.

![](functional-independence-measurement-fim-version-1-user-manual/067.png)

Discharge FIM Assessment Type

> **NOTE:** The Discharge tab is now available.

49. In the Dates and Dx field, enter the Therapy End Date for the case.

> **NOTE:** The discharge date is entered in the Therapy End date field for Continuum cases. Clicking the down arrow gives you a calendar. Click on the appropriate date. If you are not fully completing the 18 FIM items, leave the Therapy End Date or the Rehab Bed Unit Discharge blank. This should only be completed after all the scores on the Discharge tab have been filled in. This field is also called Rehab bed unit Discharge when entering data from an acute or sub-acute rehabilitation bed service.

Completing the Discharge (Therapy End Date) field closes the case from any further editing or addenda. Therefore, if only part of the discharge FIM score is sent with a discharge date, you cannot add any additional data to the template.

![](functional-independence-measurement-fim-version-1-user-manual/068.png)

Completing Discharge Date

When adding the Therapy End Date, you will receive a message that indicates that you will not be allowed to add to admission, interim or discharge assessments. Choose Yes to continue, but keep in mind that when you complete this note, no additional addenda or editing can take place in the CPRS template.

![](functional-independence-measurement-fim-version-1-user-manual/069.png)

Information Pop-up

50. In the Discharge field, complete the FIM scores.

![](functional-independence-measurement-fim-version-1-user-manual/070.png)

Complete FIM Scores

51. When you have completed the FIM scores in the Discharge tab, select the Finished tab to view how the note will look in CPRS.

![](functional-independence-measurement-fim-version-1-user-manual/071.png)

Finished Tab

52. The Confirm pop-up appears. If you are ready to send the note, click Yes.

![](functional-independence-measurement-fim-version-1-user-manual/072.png)

Confirm Pop-up

53. As in previous examples, you will need to sign the note and click OK.

![](functional-independence-measurement-fim-version-1-user-manual/073.png)

Sign Note Dialog

54. The Information pop-up appears informing you that an e-mail will be sent to the FSOD Coordinator. Click OK.

![](functional-independence-measurement-fim-version-1-user-manual/074.png)

Information Pop-up

The discharge of the patient is now complete.

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|               |                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAC           | Austin Automation Center                                                                                                                                                                                                     |
| ADPAC         | Automated Data Processing Application Coordinator                                                                                                                                                                            |
| API Interface | Application Program Interface                                                                                                                                                                                                |
| CARF          | Commission on the Accreditation of Rehabilitative Facilities                                                                                                                                                                 |
| CPRS          | Computerized Patient Record System                                                                                                                                                                                           |
| DBA           | Database Administrator, oversees package development with respect to DHCP/VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.               |
| DBIA          | Database Integration Agreement, a formal understanding between two or more DHCP packages, which describes how data is shared or how packages interact. The DBA maintains a list of DBIAs.                                    |
| DBIC          | Database Integration Committee. Within the purview of the DBA, the committee maintains a list of DBIC approved callable entry points and publishes the list on FORUM for reference by application programmers and verifiers. |
| DSCC          | Documentation Standards and Conventions Committee. Package documentation is reviewed in terms of standards set by this committee.                                                                                            |
| DUZ           | A local variable holding the user number that identifies the signed-on user.                                                                                                                                                 |
| DUZ(0)        | A local variable that holds the File Manager Access Code of the signed-on user.                                                                                                                                              |
| E3R           | Electronic Error and Enhancement Report                                                                                                                                                                                      |
| FIM           | Functional Independence Measure                                                                                                                                                                                              |
| FOIA          | The Freedom Of Information Act. Under the provisions of this public law, software developed within the VA is made available to other institutions, or the general public, at a nominal cost.                                 |
| FSOD          | Functional Status and Outcomes Database                                                                                                                                                                                      |
| GUI           | Graphic User Interface                                                                                                                                                                                                       |
| HINQ          | Hospital INQuiry. A system that permits medical centers to query the Veterans Benefits Administration systems via the VADATS network.                                                                                        |
| HIS           | Hospital Information Systems                                                                                                                                                                                                 |
| HL7           | Health Level 7                                                                                                                                                                                                               |
| ICD           | International Classification of Diseases                                                                                                                                                                                     |
| IDCU          | The Integrated Data Communications Utility which is a wide area network used by VA for transmitting data between VA sites.                                                                                                   |
| IFCAP         | Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement                                                                                                                                           |
| IHS           | Indian Health Service                                                                                                                                                                                                        |
| IHS           | Integrated Hospital System                                                                                                                                                                                                   |
| JCAHO         | Joint Commission on the Accreditation of Health Care Organizations                                                                                                                                                           |
| M (or MUMPS)  | Massachusetts University Multiple Programming System                                                                                                                                                                         |
| PCE           | Patient Care Encounter                                                                                                                                                                                                       |
| PM&R          | Physical Medicine and Rehab                                                                                                                                                                                                  |
| RPC           | Remote Procedure Call                                                                                                                                                                                                        |
| SRS           | Software Requirement Specifications                                                                                                                                                                                          |
| TIU           | Text Integration Utilities                                                                                                                                                                                                   |
| VA            | The Department of Veterans Affairs, formerly called the Veterans Administration.                                                                                                                                             |
| VistA         | Veterans Health Information System and Technology Architecture                                                                                                                                                               |
| WPB           | West Palm Beach VA Medical Center                                                                                                                                                                                            |

# Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                     |                                                                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Austin Automation Center            | Repository for databases located in Austin, Texas                                                                                                                                   |
| E3R                                 | The Electronic Error and Enhancement Report system is located on VA FORUM. The utility provides tools for entering, tracking and reporting Enhancement requests for VistA packages. |
| Patient Care Encounter              | VistA software package that helps sites collect, manage, and display outpatient workload data, including providers, procedures, and diagnostic codes.                               |
| Software Requirement Specifications | Document, which outlines the functionality requirements for a project.                                                                                                              |

# Appendix C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Medical Rehabilitation Outcomes for Stroke, Traumatic Brain Injury, and Lower Extremity Amputee Patients, VHA Directive 2000-16, June 5, 2000.
- Supporting Statement for Clearance of an Instrument for Implementation of a Prospective Payment System for Patients in Inpatient Rehabilitation Hospitals and Exempt Units, Information Collection Requirements in HCFA-10036sst, April 12, 2001
- 192-135 GUI Behaviors_Checklist
- 192-135 GUI Distribution, Update and Run Behaviors
- Graphical User Interface Standards and Conventions (GUI SAC)
- Website: [www.va.gov/vdl](http://www.va.gov/vdl)
- Website: <http://vista.med.va.gov/messaging/HL7/hl7_specifications.htm>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Abbreviated Response</td>
<td>This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Access Code</td>
<td>A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long. It can be numeric, alphabetic, or a combination of both, and is usually assigned by a site manager or application coordinator. (See the term verify code in the Glossary.)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Application Coordinator</td>
<td>Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Auto-menu</td>
<td>An indication to Menu Manager that the current user’s menu items should be displayed automatically. When auto-menu is not in effect, the user must enter a question mark at the menu’s select prompt to see the list of menu items.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Caret</td>
<td>A symbol expressed as up caret (^), left caret (&lt;), or right caret (&gt;). In many M systems, a right caret is used as a system prompt and an up caret as an exiting tool from an option. Also known as the up-arrow symbol or shift–6 key.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Command</td>
<td>A combination of characters that instruct the computer to perform a specific operation.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Common menu</td>
<td>Options that are available to all users. Entering two question marks at the menu’s select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="even">
<td>Control key</td>
<td>The Control Key (Ctrl on the keyboard) performs a specific function in conjunction with another key. In word-processing, for example, holding down the Ctrl key and typing an A causes a new set of margins and tab settings to occur; Ctrl-S causes printing on the terminal screen to stop; Ctrl-Q restarts printing on the terminal screen; Ctrl-U deletes an entire line of data entry <u>before</u> the Return key is pressed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Cross reference</td>
<td><p>An indexing method whereby files can include pre-sorted lists of entries as part of the stored database. Cross-references (x-refs) facilitate look-up and reporting.</p>
<p>A file may be cross-referenced to provide direct access to its entries in several ways. For example, VA FileMan allows the Patient file to be cross-referenced by name, social security number, and bed number. When VA FileMan asks for a patient, the user may then respond with the patient’s name, social security number, or his bed number. A cross-reference speeds up access to the file, both for looking up entries and for printing reports.</p>
<p>A cross reference is also referred to as an index or cross-index.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Cursor</td>
<td>A flashing image on your screen (generally a horizontal line or rectangle) that alerts you that the computer is waiting for you to make a response to an instruction (prompt).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Data</td>
<td>A representation of facts, concepts, or instructions in a formalized manner for communication, interpretation, or processing by humans or by automatic means. The information you enter for the computer to store and retrieve. Characters that are stored in the computer system as the values of local or global variables. VA FileMan fields hold data values for file entries.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Data attribute</td>
<td>A characteristic of a unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="odd">
<td>Data Dictionary</td>
<td><p>The Data Dictionary is a global containing a description of what kind of data is stored in the global corresponding to a particular file. The data is used internally by FileMan for interpreting and processing files.</p>
<p>A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file’s elements or data attributes; programmers review the definitions of a file’s internal structure.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Data dictionary access</td>
<td>A user’s authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Data dictionary listing</td>
<td>This is the printable report that shows the data dictionary. DDs are used by users and programmers.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Data processing</td>
<td>Logical and arithmetic operations performed on data. These operations may be performed manually, mechanically, or electronically: sorting through a card file by hand would be an example of the first method; using a machine to obtain cards from a file would be an example of the second method; and using a computer to access a record in a file would be an example of the third method.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Database</td>
<td>A set of data, consisting of at least one file, that is sufficient for a given purpose. The DHCP/VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file. A data collection has different data fields (e.g., patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Database management system</td>
<td>A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Database, national</td>
<td>A database which contains data collected or entered for all VHA sites.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Debug</td>
<td>To correct logic errors or syntax errors or both types in a computer program. To remove errors from a program.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Default</td>
<td>A response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the enter (or return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Delete</td>
<td>The key on your keyboard (may also be called rubout or backspace on some terminals) which allows you to delete individual characters working backwards by placing the cursor immediately after the last character of the string of characters you wish to delete. The @ sign (uppercase of the 2 key) may also be used to delete a file entry or data attribute value. The computer asks “Are you sure you want to delete this entry?” to insure you do not delete an entry by mistake.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Delimiter</td>
<td>A special character used to separate a field, record or string. VA FileMan uses the ^ character as the delimiter within strings.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Device</td>
<td>A peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Dictionary</td>
<td>A database of specifications of data and information processing resources. VA FileMan’s database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Disk</td>
<td>The media used in a disk drive for storing data.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Disk drive</td>
<td>A peripheral device that can be used to “read” and “write” on a hard or floppy disk.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Double quote (")</td>
<td>A symbol used in front of a Common option’s menu text or synonym to select it from the Common menu. For example, the five-character string "TBOX" selects the User’s Toolbox Common option.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Encryption</td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional that is, they only encode and the resulting data cannot be unscrambled (e.g., access/verify codes).</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Enter</td>
<td>Pressing the return or enter key tells the computer to execute your instruction or command or to store the information you just entered.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Entry</td>
<td>A VA FileMan record. It is uniquely identified by an internal entry number (the .001 field) in a file.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Etiology</td>
<td>The study or theory of the factors that cause disease and the method of their introduction to the host. The cause(s) or origin of a disease or disorder.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Extractor</td>
<td>A specialized routine designed to scan data files and copy or summarize data for use by another process.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Field</td>
<td>In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file’s data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>File</td>
<td>A set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>File Manager (VA fileman)</td>
<td>The Database Management System (DBMS). The central component of the Kernel that defines the way standard DHCP/VistA files are structured and manipulated.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Forced queuing</td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device rejects it and prompts the user to queue the task instead.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Free text</td>
<td>The use of any combination of numbers, letters, and symbols when entering data.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Global variable</td>
<td>A variable that is stored on disk (M usage).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Go-home jump</td>
<td>A menu jump that returns the user to the Primary menu presented at sign-on. It is specified by entering two up-arrows (^^) at the menu’s select prompt. It resembles the rubber band jump but without an option specification after the up-arrows.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Hardware</td>
<td>The physical equipment pieces that make up the computer system (e.g., terminals, disk drives, central processing units). The physical components of a computer system.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Health Services Research &amp; Development (HSR&amp;D)</td>
<td>Established in 1973 to assist in the search for the most cost-effective approaches to delivering quality health care to the nation's veterans through the support of health services research studies.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Help frames</td>
<td>Entries in the HELP FRAME file that may be distributed with application packages to provide on-line documentation. Frames may be linked with other related frames to form a nested structure.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Help prompt</td>
<td>The brief help that is available at the field level when entering one question mark.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Inpatient</td>
<td>A patient who has been admitted to a hospital in order to be treated for a particular condition.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>A set of software routines that function as an intermediary between the host operating system and the application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Key</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Keyword</td>
<td>A word or phrase used to call up several codes from the reference files in the LOCAL LOOK-UP file. One specific code may be called up by several different keywords.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>LAYGO access</td>
<td>A user’s authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Link</td>
<td>Non-specific term referring to ways in which files may be related (via pointer links). Files have links into other files.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Log in/on</td>
<td>The process of gaining access to a computer system.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Log out/off</td>
<td>The process of exiting from a computer system.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Mail message</td>
<td>An entry in the MESSAGE file. The DHCP electronic mail system (MailMan) supports local and remote networking of messages.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Mailman</td>
<td>An electronic mail system that allows you to send and receive messages from other users via the computer.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Manager account</td>
<td>A UCI that can be referenced by non-manager accounts such as production accounts. Like a library, the MGR UCI holds percent routines and globals (e.g., ^%ZOSF) for shared use by other UCIs.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Mandatory field</td>
<td>This is a field that requires a value. A null response is not valid.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Medical Care Cost Recovery (MCCR)</td>
<td>A VA project to collect data from entities, which owe payment to VA for care of patients. Also referred to by the acronym MCCR.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Menu</td>
<td>A list of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word “Select” and followed by the word “option” as in Select Menu Management option: (the menu’s select prompt).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Menu cycle</td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. Menu Manager keeps track of information, such as the user’s place in the menu trees, according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Menu system</td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Menu template</td>
<td>An association of options as pathway specifications to reach one or more final destination options. The final options must be executable activities and not merely menus for the template to function. Any user may define user-specific menu templates via the corresponding Common option.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Menu text</td>
<td>The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file. For example, User’s Toolbox is the menu text of the XUSERTOOLS option. The option’s synonym is TBOX.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Numeric field</td>
<td>A response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Operating system</td>
<td>A basic program that runs on the computer, controls the peripherals, allocates computing time to each user, and communicates with terminals.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Option</td>
<td>An entry in the OPTION file. As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Option Name</td>
<td>The Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text “Menu Management”). Options are namespaced according to DHCP conventions monitored by the DBA.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Outpatient</td>
<td>A patient who comes to the hospital, clinic, or dispensary for diagnosis and/or treatment but does not occupy a bed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Package</td>
<td>The set of programs, files, documentation, help prompts, and installation procedures required for a given software application.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Password</td>
<td>A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user’s identity.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Peripheral device</td>
<td>Any hardware device other than the computer itself (central processing unit plus internal memory). Typical examples include card readers, printers, CRT units, and disk drives.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Phantom jump</td>
<td>Menu jumping in the background. Used by the menu system to check menu pathway restrictions.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Pointer</td>
<td>A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Primary menus</td>
<td>The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by IRM. This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Printer</td>
<td>A printing or hard copy terminal.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Production account</td>
<td>The UCI where users log on and carry out their work, as opposed to the manager or library account.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Program</td>
<td>A list of instructions written in a programming language and used for computer operations.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Prompt</td>
<td>The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Queuing</td>
<td>Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). The Kernel’s Task Manager handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Queuing required</td>
<td>An option attribute that specifies that the option must be processed by TaskMan (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified time periods.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Read access</td>
<td>A user’s authorization to read information stored in a computer file.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Record</td>
<td>A set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Resource</td>
<td>Sequential processing of tasks can be controlled through the use of resources. Resources are entries in the DEVICE file, which must be allocated to a process(es) before that process can continue.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Return</td>
<td>On the computer keyboard, the key located where the carriage return is on an electric typewriter. It is used in to terminate “reads.” Symbolized by &lt;RET&gt;.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Scheduling Options</td>
<td>This is a technique of requesting that TaskMan run an option at a given time, perhaps with a given rescheduling frequency.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Screen</td>
<td>A CRT, monitor or video display terminal</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Secondary menus</td>
<td>Options assigned to individual users to tailor their menu choices. If a user needs a few options in addition to those available on the Primary menu, the options can be assigned as secondary options. To facilitate menu jumping, secondary menus should be specific activities, not elaborate and deep menu trees.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Security key</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Server</td>
<td>An entry in the OPTION file. An automated mail protocol that is activated by sending a message to a server at another location with the “S.server” syntax. This activity is specified in the OPTION file.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Set of codes</td>
<td>Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sign-on/security</td>
<td>The Kernel module that regulates access to the menu system. It performs a number of checks to determine whether access can be permitted at a particular time. A log of sign-ons is maintained.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Spacebar return</td>
<td>You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Special queuing</td>
<td>An option attribute indicating that TaskMan should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Specialty</td>
<td>The particular subject area or branch of medical science to which one devotes professional attention.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Spooler</td>
<td><p>Spooling (under any system) provides an intermediate storage location for files (or program output) for printing at a later time.</p>
<p>In the case of DHCP, the Kernel manages spooling so that the underlying OS mechanism is transparent. The Kernel subsequently transfers the text to the ^XMBS global for despooling (printing).</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Stop code</td>
<td>A number (i.e., a subject area indicator) assigned to the various clinical, diagnostic, and therapeutic sections of a facility for reporting purposes. For example, all outpatient services within a given area (e.g., Infectious Disease, Neurology, and Mental Hygiene—Group) would be reported to the same clinic stop code.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Synonym</td>
<td>A field in the OPTION file. Options may be selected by their menu text or synonym (see Menu Text).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Taskman</td>
<td>The Kernel module that schedules and processes background tasks (also called Task Manager).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Template</td>
<td>A means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file, print specifications are stored in the PRINT TEMPLATE file, and search or sort specifications are stored in the SORT TEMPLATE file.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Terminal</td>
<td>May be either a printer or CRT/monitor/video display terminal.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Timed-read</td>
<td>The amount of time a READ command waits for a user response before it times out.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Trigger</td>
<td>A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Type-ahead</td>
<td>A buffer used to store characters that are entered before the corresponding prompt appears. Type-ahead is a shortcut for experienced users who can anticipate an expected sequence of prompts.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Up-arrow jump</td>
<td>In the menu system, entering an up-arrow (^) followed by an option name accomplishes a jump to the target option without needing to take the usual steps through the menu pathway.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>User access</td>
<td><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>User interface</td>
<td>The way the package is presented to the user—issuing of prompts, help messages, menu choices, etc. A standard user interface can be achieved by using VA FileMan for data manipulation, the menu system to provide option choices, and VA FileMan’s Reader, the ^DIR utility, to present interactive dialogue.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VA Fileman</td>
<td>A set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A package of on-line computer routines written in the M language, which can be used as a stand-alone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer stored files.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Verify code</td>
<td>An additional security precaution used in conjunction with the Access Code. Like the Access Code, it is also 6 to 20 characters in length and, if entered incorrectly, will not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
AAC, 51
Admission tab, 9
ALT Key, 6
API Interface, 51
Application Program Interface, 51
Austin Automation Center, 51
Austin Automation Center (AAC), 1
C
cancel, 11
CARF, 1, 51
Case Notes, 9
checkbox, 10
Cognitive Subtotal, 10
Command button, 11
Commission on the Accreditation of Rehabilitative Facilities, 1, 51
Computerized Patient Record System, 1, 51
CPRS, 51
D
Date fields, 10
Dates and Dx tab, 9
Delphi, 1
Department of Veterans Affairs Central Office, 1
Discharge tab, 9
drop-down list, 11
E
E3R, 51
Electronic Error and Enhancement Report, 51
Enter Key, 2
F
F1, 2
FIM, 51
FIM Total Score, 10
Finished tab, 10
Follow Up, 10
FSOD, 51
Functional Independence Measure, 51
Functional Independence Measures, 1
Functional Independence Measures (FIM), 1
Functional Status and Outcomes Database, 51
Functional Status and Outcomes Database (FSOD), 1
FY03, 1
G
Goals tab, 10
Graphic User Interface, 1, 51
GUI, 1, 51
H
Health Level 7, 52
HL7, 1, 52
I
Interim tab, 9
J
JCAHO, 1, 52
Joint Commission on the Accreditation of Health Care Organizations, 1, 52
M
Massachusetts University Multiple Programming System, 52
Motor Subtotal, 10
MUMPS, 52
N
Notes tab, 9
P
Patient Care Encounter, 52
PCE, 52
Physical Medicine and Rehab, 52
PM&R, 52
Progress Notes, 9
PT/Program tab, 9
R
Radio button, 11
Remote Procedure Call, 52
Return Key, 2
RPC, 52
S
Scoring Key, 10
Software Requirement Specifications, 52
SRS, 52
T
TAB key, 11
TBI, 1
Text Integration Utilities, 52
The Department of Veterans Affairs, 52
TIU, 52
Total Score, 10
traumatic brain injury, 1
U
User access, 67
User interface, 67
V
VA, 52
VACO, 1
Verify code, 68
Veterans Health Administration, 1
Veterans Health Information System and Technology Architecture, 52
VHA, 1
VHA Directive 2000-16, 1
VistA, 52
VistA FileMan file for Health Level Seven, 1
W
West Palm Beach VA Medical Center, 52
WPB, 52
