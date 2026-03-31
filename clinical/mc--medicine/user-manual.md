---
title: Medicine Version 2.3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: MC
app_name: Medicine
section: CLI
app_status: active
pkg_ns: MC
patch_ver: 2.3
patch_id: MC*2.3
group_key: "MC:MC:2.3"
file_numbers: []
security_keys: []
menu_options: 9
description: 
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - class
  - edit
  - style
  - width
  - brief
  - procedures
  - consult
page_count: 0
word_count: 5539
section_count: 24
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc_2_3um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc_2_3um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=77"
---

> MEDICINE

> USER MANUAL

![](medicine-version-2-3-user-manual/001.png)

> September 1996

> Revised July 2014

Office of Information and Technology

Product Development

Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>July 2014</td>
<td>MC*2.3*43 MC*2.3*44</td>
<td><p>Word document created from PDF.</p>
<p>Updated Table of Contents</p>
<p>Updated for ICD-10 Patch MC*2.3*43 and Patch MC*2.3*44 as follows:</p>
<ul>
<li><blockquote>
<p>“&gt;Out of order: OUT OF ORDER” added to Rheumatology Line Enter/Edit Menu p. <a href="#p137">137</a></p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>September 1996</td>
<td>MC*2.3*8</td>
<td>Initial creation of document (PDF)</td>
<td></td>
</tr>
</tbody>
</table>

This page is intentionally left blank.

> Preface

> The Medicine package is used for entering, editing, printing medical test results, and storing the data according to Department of Veterans Affairs FileMan structures. Cardiology, Gastrointestinal, Pulmonary, Hematology, Pacemaker, Rheumatology and Generalized Procedure are the current modules. The system also allows the automated interface of some tests such as ECG.

> This User Manual is designed to provide the user with "how-to" information on the functions of the Medicine package. The actual screens used in the system are reproduced in the manual, with information on FileMan protocol, methods of data entry, and special terminology.

> If services are to receive only the documentation pertaining to their module, it is important to also include the Introduction, Summary of Patient Procedures, Problem Oriented Consult Menu, and Index sections.

> This page is intentionally left blank.
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Functional Description](#functional-description)
  - [Manuals](#manuals)
- [Orientation](#orientation)
  - [Manual Use](#manual-use)
  - [Package Conventions](#package-conventions)
  - [Screen Conventions](#screen-conventions)
  - [Enter/Edit Options](#enteredit-options)
  - [Electronic Signatures](#electronic-signatures)
  - [Release Control](#release-control)
- [Package Management](#package-management)
  - [Implementation](#implementation)
  - [Site Configuration Issues](#site-configuration-issues)
  - [Legal Requirements](#legal-requirements)
  - [Menu Distribution](#menu-distribution)
  - [Electronic Signature and Release Control](#electronic-signature-and-release-control)
  - [Release Control Options](#release-control-options)
- [Package Operation](#package-operation)
  - [CARDIOLOGY MODULE](#cardiology-module)
    - [Medicine Menu](#medicine-menu)
    - [Surgical Risk Analysis Options](#surgical-risk-analysis-options)
    - [Summary of Patient Procedures](#summary-of-patient-procedures)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu)
    - [Cardiology Management Menu](#cardiology-management-menu)
    - [Documentation Notes](#documentation-notes)
    - [Cath Lab Menu](#cath-lab-menu)
    - [ECG Menu](#ecg-menu)
    - [Echo Lab Menu](#echo-lab-menu)
    - [EP Lab Menu](#ep-lab-menu)
    - [Holter Lab Menu](#holter-lab-menu)
    - [Exercise Tolerance Test (ETT) Menu](#exercise-tolerance-test-ett-menu)
    - [Surgical Risk Analysis Menu](#surgical-risk-analysis-menu)
  - [GASTROINTESTINAL MODULE](#gastrointestinal-module)
    - [Documentation Notes](#documentation-notes-1)
    - [Endoscopic Procedure Menu](#endoscopic-procedure-menu)
    - [Non-Endoscopic Procedures](#non-endoscopic-procedures)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-1)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu-1)
    - [GI Management Menu](#gi-management-menu)
  - [PULMONARY MODULE](#pulmonary-module)
    - [Documentation Notes](#documentation-notes-2)
    - [Endoscopy Menu](#endoscopy-menu)
    - [Pulmonary Function Test Menu](#pulmonary-function-test-menu)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-2)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu-2)
    - [Pulmonary Management Menu](#pulmonary-management-menu)
  - [HEMATOLOGY MODULE](#hematology-module)
    - [Enter/Edit Hematology Procedures](#enteredit-hematology-procedures)
    - [Brief Enter/Edit](#brief-enteredit)
    - [Brief Report](#brief-report)
    - [Release Control](#release-control-1)
    - [Enter/Edit Hematology Procedures (Screen)](#enteredit-hematology-procedures-screen)
    - [Hematology Report](#hematology-report)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-3)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu-3)
    - [Image Capture](#image-capture)
    - [Brief Hematology Enter/Edit (Screen)](#brief-hematology-enteredit-screen)
    - [> Brief Hematology Screen 09/16/93](#brief-hematology-screen-091693)
  - [PACEMAKER MODULE](#pacemaker-module)
    - [Documentation Notes](#documentation-notes-3)
    - [Enter/Edit Menu (Line Entry)](#enteredit-menu-line-entry)
    - [Enter/Edit Menu for Screen Entry of Pacemaker](#enteredit-menu-for-screen-entry-of-pacemaker)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-4)
    - [Pacemaker Report Menu](#pacemaker-report-menu)
    - [Pacemaker Management Menu](#pacemaker-management-menu)
  - [RHEUMATOLOGY MODULE](#rheumatology-module)
    - [Diagnosis Edit for Rheumatology](#diagnosis-edit-for-rheumatology)
    - [Add New Visit/Display Patient Background Info.](#add-new-visitdisplay-patient-background-info)
    - [History Narrative Edit](#history-narrative-edit)
    - [Display Serial Laboratory Info (Screens 1-3 )](#display-serial-laboratory-info-screens-1-3)
    - [Display/Print Drug Treatment Print Program](#displayprint-drug-treatment-print-program)
    - [Health Assessment (HAQ) Edit](#health-assessment-haq-edit)
    - [Health/Physical History Edit (Screens 1-4 )](#healthphysical-history-edit-screens-1-4)
    - [Physical Examination Edit (Screens 1-5 )](#physical-examination-edit-screens-1-5)
    - [Death Admin Edit](#death-admin-edit)
    - [Print Menu](#print-menu)
    - [Line Enter/Edit Menu](#line-enteredit-menu)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu-4)
    - [Image Capture](#image-capture-1)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-5)
    - [Rheumatology Management Menu](#rheumatology-management-menu)
  - [GENERALIZED PROCEDURE MODULE](#generalized-procedure-module)
    - [Generalized Procedure Enter/Edit](#generalized-procedure-enteredit)
    - [Generalized Procedure Report](#generalized-procedure-report)
    - [Generalized Procedure Management](#generalized-procedure-management)
    - [Summary of Patient Procedures](#summary-of-patient-procedures-6)
    - [Problem Oriented Consult Menu](#problem-oriented-consult-menu-5)
    - [Image Capture](#image-capture-2)
    - [Brief Generalized Procedure Enter/Edit](#brief-generalized-procedure-enteredit)
    - [Brief Generalized Procedure Enter/Edit (Screen)](#brief-generalized-procedure-enteredit-screen)
    - [Brief Generalized Procedure Report](#brief-generalized-procedure-report)
  - [SUMMARY OF PATIENT PROCEDURES](#summary-of-patient-procedures-7)
    - [Summary of Patient Procedures by Date](#summary-of-patient-procedures-by-date)
    - [Summary of Patient Procedures by All Procedures](#summary-of-patient-procedures-by-all-procedures)
    - [Summary of Patient Procedures by One Procedure](#summary-of-patient-procedures-by-one-procedure)
  - [PROBLEM ORIENTED CONSULT MENU](#problem-oriented-consult-menu-6)
    - [Problem Oriented Consult Enter/Edit](#problem-oriented-consult-enteredit)
    - [Problem Oriented Consult Enter/Edit (Screen)](#problem-oriented-consult-enteredit-screen)
    - [Problem Oriented Consult Report](#problem-oriented-consult-report)
    - [Brief Enter/Edit of Problem Oriented Consult](#brief-enteredit-of-problem-oriented-consult)
    - [Brief Consult Edit/Enter Screen](#brief-consult-editenter-screen)
    - [Brief Consult Report](#brief-consult-report)
- [Glossary](#glossary)
- [Index](#index)
> The Medicine package is a VA FileMan/ MUMPS-based computer program to serve the needs of the Department of Veterans Affairs Medicine Service medical community. Medicine test results are organized to help physicians to manage patient data with greater ease and furnish reports and patient data on a timely basis. It is an important part of the Decentralized Hospital Computer Program (DHCP), making maximum use of the hospital data base.

## Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Medicine package is designed for entry, edit, and display of data from a large number of medical tests or procedures. Printed reports are available for all procedures.

> The modules currently included are Cardiology, Pulmonary, Gastrointestinal (GI), Hematology, Rheumatology, Pacemaker, and Generalized Procedure. Each module has a menu designed for entering, editing, and printing reports for various procedures/tests associated with that sub- specialty.

> The Medicine package has access to the DHCP Imaging System which allows digital images of procedures to be attached to patient records when run at a workstation. The Imaging system stores, retrieves, transmits, and displays digital images of conditions and procedures. It allows the physician to have access to a complete view of patient data which in turn can be electronically shared with consulting physicians. The Imaging system accesses DHCP data such as laboratory

> results, pharmacy prescriptions and other clinical information, and displays them along with images of medical procedures which have been performed. Information such as prior images or previous diagnostic reports can be integrated and presented as a single record. The Imaging options are only usable on a workstation.

> A Summary of Patient Procedures is provided on each menu. The option is documented in a separate section of the manual. This option allows a user to select a medical patient and obtain a listing of all procedures performed. The user can determine whether the data should be sorted by date or procedure. If sorted by procedure, the user has the option of choosing all procedures or a particular type of procedure. The user may select a particular procedure to view in detail.

> Problem Oriented Consult is another option that is common throughout the Medicine package. It is also documented in a separate section.

> Sub-specialty Management menus allow local control over various files such as Medications and

> Instruments.

## Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. The *Medicine User Manual* contains information relative to using the various options of the Medicine system modules. If services are to receive only the documentation pertaining to their module, it is very important to also include the Introduction, Summary of Patient Procedures, Problem Oriented Consult Menu, and Index sections.

> 2\. The *Medicine V 2.2 Technical Manual* contains information on the organizational structure and functions of the system routines.

> 3\. Since the Medicine package inter-relates so closely with other packages, other User documentation, such as Laboratory, Order Entry/Results Reporting, Pharmacy (National Drug File module), and Allergy Tracking, and DHCP Imaging System may be useful.

> 4\. Quick Reference Guides are available for the Brief Enter/Edit options of each module.

> 5\. The *Release Notes and Installation Guide* provide instructions for installing Medicine V. 2.2.

> 6\. The *Package Security Guide* is provided for the Information Security Officer (ISO).

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Manual Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual contains the screen displays found in the Enter/Edit (Screen) options, and descriptions of the fields. In general, discussion of a screen or subscreen follows the graphic representation of the screen. The following conventions are used in this manual.

> *Submenus:* Kernel V. 7.0 and higher automatically inserts three dots on the screen after a menu option that leads to a submenu. The documentation does not reflect this feature.

> *Return key:* The symbol \<RET\> refers to the return key.

> *Underline:* An underline is used in the manual to show those multiple fields that lead to subscreens. The underline does not appear on the computer screen.

## Package Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following conventions apply to both Line and Screen Edit/Enter options. Screen Enter/Edit options have additional conventions and enhancements which are discussed under Screen Conventions.

> *Return key:* The Return key tells the computer that you have finished with a prompt and are ready to go to the next prompt (whether or not you have entered any information). Every response you type must be followed by pressing the return key. In a word processing field, two returns are needed to

> tell the computer that you are done.

> *Upper/lower case:* User entries may be made in either upper case or lower case characters when using the Screen Enter/Edit mode. Line Enter/Edit options accept upper or lower case except when choosing an answer from a set of predetermined codes (i.e., Choose from "N" for Normal or "A" for Abnormal). Codes must be entered exactly.

> *Default answers:* For prompts containing a default answer or previously entered information (i.e., "Do you want to change the release status? N//" or "WT LBS: 165//"), the user may accept the default selection by entering a return or may type in a new answer followed by a return.

> *Deleting information:* Entering the at sign (@) in a field will delete information previously entered there.

> *CAUTION:* Using the at sign on the first field entry line of the first screen of a procedure will delete the entire procedure record.

> *Help at a menu:* A question mark (?) will show the menu, two question marks (??) will show the menu with technical information about the options, and three question marks (???) will give brief descriptions of the menu options

> *Help at a field:* A question mark (?) will give a help message, two question marks (??) will give additional information and/or a list from which to choose.

> If there is more than one selection for an entry, a list of all possible selections appears when two question marks are entered. The user can choose a selection by entering either the name or number of the selection. If a long entry is being entered from a list, only the first few letters of the entry need to be typed, as three letters are sufficient for entry identification. If an entry is ambiguous, a double question mark will appear, and the selection prompt is automatically reprinted.

> *Exiting:* An up-caret (^) signals the program that you want to exit whatever level you are at.

> Entering "^" at this level... Exits you to this level.

> Main Medicine menu Out of the package Module menu Main Medicine menu Procedure menu Module menu

> Field Procedure menu or Release Control Screen

> List of choices Field entry

## Screen Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Screens:* The screens are displayed in sequential order. Screen or keypad (KP) commands can be used to go back one screen or forward one screen. Entering a \<RET\> to complete the last field entry of the screen takes the user to the next screen. The user may not jump directly from the first screen to the fourth screen.

> Either the Screen Command or the Keypad Command mode can be used to navigate when using the

> Screen Enter/Edit options.

> *Help:* Screen Enter/Edit options have two additional ways to access Help messages. ^O or PF2 on the keypad allow the user to turn on automatic help. When automatic help is turned on, a message appears below the screen title which tells what type of help is being given (i.e., Current entries, Selection List, Set of Codes) . At each field, the help message for that field appears at the bottom of the screen. The user who wants only occasional help can use the same commands to turn automatic help off and use ^H or PF7 to get help for individual fields upon request.

> *Keypad Commands:* ^K will display the keypad commands (KP) at the bottom of the screen. When in this mode, you can easily switch to screen commands using the PF1 key in order to use the

> keypad for entering numbers.

> KEYPAD COMMANDS: (C)omputed, (M)ultiple, (W)ord processing, (R)ead only

> PF1 or ^T -- Toggle to Numberpad mode PF2 -- Turn on/off auto help

> KP1 -- Display Commands (current mode) KP7 -- Help

> KP5 -- Repaint the screen Down Arrow -- Next field KP6 -- Recall previous answer Right Arrow -- Previous Screen KP9 -- Delete data Left Arrow -- Next Screen

> The keypad commands work on terminals with extended keyboards that are set up for VT100 emulation or that have keypad, arrow keys, and PF keys mapped in the Terminal file. They do not work on Qume terminals.

> ![](medicine-version-2-3-user-manual/002.png)The PF keys are the four keys at the top of the number keypad. They may or may not be named PF on your keyboard (e.g., PF1 is often named Num Lock). The diagram below shows which key to use for each keypad command and also its screen command counterpart.

PF1

COMMAND

TOGGLE

^T

> PF2

AUTO

HELP

> ^O

> PF3

FIELD

> HELP

> ?

> PF4

FIELD

> HELP

> ??

7

HELP

^H

8 9

> DELETE

> DATA

> @

4

FIELD

JUMP

^(nn)

> 5

REPAINT

> SCREEN

> ^R

> 6

> RECALL

PREVIOUS

> SP\<RET\>

> PREVIOUS FIELD

\<

> 1 2

> Display

COMMANDS

> ^C

> 3

Exit

> ^

> PREVIOUS SCREEN

^U

NEXT FIELD

\<RET\>

NEXT SCREEN

> ^D

> Fig. 1: Keypad Commands

> *Screen Commands:* ^C will display the following commands at the bottom of the screen. While you must be in this mode in order to use the keypad for entering numbers, it is easy to toggle back and forth using the PF1 key.

> COMMANDS: (C)omputed, (M)ultiple, (W)ord processing, (R)ead only

> ^T or PF1 -- Toggle to Keypad mode ?//?? -- Field help

> ^O -- Turn on/off automatic help ^ -- Quit

> ^H -- Help Space bar\<RET\> -- Recall previous answer

> *Fields:* To go to a particular field line, enter "^" with the number of the desired field, as in "^6" or use the KP4 and the field number.

> *Field Codes:* Field entries have an (M) code, a (W) code, a (C) code, an (R) code, or no code following the field description.

> \(M\) Stands for a dictionary or multiple field, in which the possible choices for the field entry are listed when a "??" is entered on the field line. Note that a letter or number code appears with each choice, which may be entered on the line in lieu of the entire selection name.

> Some multiple fields have subscreens which include additional fields. These fields are identified in the documentation by an underline. The user will be moved automatically to a new screen and returned back to the main screen afterwards. Note that in this manual, only those multiples that are underlined have subscreens.

> At multiple fields, the most recent entry is displayed at the selection prompt. In order to view all entries made, enter a "?". The user may edit or view a particular entry by selecting it from the listed display. The underline does not appear on the computer screen.

> New entries may be added by typing in the entry at the selection prompt. At the "Are you adding a new entry?" query, enter a "Y" to continue with the new entry.

> \(W\) Stands for a word processor field. The user may type in any information desired in these fields, which have no character limit for entry. In addition, all word processor fields have an edit option, in which information may be changed for selected lines. The edit option has prompts for aiding the user.

> \(C\) Stands for a computed field, where the field entry is automatically calculated from information previously entered into other fields. A computed field cannot be edited directly. The fields from which the information is calculated must be edited. Computed fields appear as uneditable fields on the Enter/Edit screens.

> In line Enter/Edit mode, the calculations are done in the background and the field only appears on reports.

> \(R\) Stands for a "read-only" field, where information may be viewed but not edited. Read only fields appear in screen edit modes but not in line edit modes.

> *Blocked Fields:* In certain instances, a field name may be followed by asterisks (\*\*\*\*). The asterisks indicate that this field is not applicable to the particular procedure chosen. These fields cannot be edited.

> In general, using a "?" or "??" will enable the user to obtain help or information for most of the screen fields.

## Enter/Edit Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Most of the Medicine package modules present several Enter/Edit options. The screens and field descriptions in this manual are those encountered when the Enter New *procedure* (Screen) option is chosen, since this accesses all data fields while the Brief option does not. Brief screens are included but the field descriptions and subscreens are not repeated.

> The Brief Enter/Edit options (both line and screen), should be sufficient for most patient records. The other Enter/Edit options offer the capability for more complete reporting when this is needed.

> Line Enter/Edit is based on FileMan prompting of each field one at a time. Entering a "^" and partial field name allows the user to jump to those fields needing to be edited.

> Enter/Edit options in most modules of the Medicine package begin with the following Help message.

> TO ENTER A NEW PROCEDURE:

> Enter the date and time when the procedure was performed. TO EDIT AN EXISTING PROCEDURE:

> Enter the patient's name, last name first, or 1st initial of the last name and the last 4 digits of the social security number.

> A partial name may be entered or a release status.

> This will bring up all entries matching that part of the name.

> Or you may enter the date and time when the procedure was performed. This must be an exact match.

> Or enter a ? to choose from a list of procedures.

> Release Control is turned on. You can release the reports. You currently have the "MCKEYCARD" Key.

#### Locating Records

> The user is asked to "Select *procedure* Date/Time" or "Enter patient name or the date & time". If entering a new procedure, enter the date and time the procedure was performed.

> Select Procedure Date/Time:

> CARDIAC CATHETERIZATION MEDICAL PATIENT:

> Several ways of locating existing records for a department are shown in Table 1.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Enter:</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Choices presented:</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Date/Time</p>
<p>(12-17-1992@02:00:00)</p>
</blockquote></td>
<td><blockquote>
<p>Procedures performed on that date and time.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Date</p>
<p>(12-17-1992)</p>
</blockquote></td>
<td><blockquote>
<p>Procedures performed on the date entered.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Name (or part) (Vet or Veteran)</p>
</blockquote></td>
<td><blockquote>
<p>Records for patients with names beginning with the entered characters.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Last Initial and last</p>
<p>4 digits of the SSN</p>
</blockquote></td>
<td><blockquote>
<p>Record for particular patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>? or ??</p>
</blockquote></td>
<td><blockquote>
<p>Records on file for the department.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Space Bar</p>
</blockquote></td>
<td><blockquote>
<p>Last record viewed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>Records which have Draft status.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PD</p>
</blockquote></td>
<td><blockquote>
<p>Records which have Problem</p>
<p>Draft status.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RNV</p>
</blockquote></td>
<td><blockquote>
<p>Records which have been released not verified.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ROV</p>
</blockquote></td>
<td><blockquote>
<p>Records which have been released off-line verified.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RV</p>
</blockquote></td>
<td><blockquote>
<p>Records which have been released verified.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>Records which have been superseded.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Table 1: Locating existing records for a department

#### OE/RR Interface

> If your site has enabled Order Entry/Results Reporting (OE/RR), the following screen will appear.

> 0 Orders 02/08/94

> 14:22

> \*\*\*\*\*\*\*\*\*\* CARDIOLOGY (Catheterization) Requests for MEDPATIENT, ONE

> \*\*\*\*\*\*\*\*\*\*

> 000-11-1111 SEP 15,1939 (54)

> No consult/request orders found!

> \* END \*

> Select Action: ??

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Status: ' '</p>
</blockquote></td>
<td><blockquote>
<p>- active</p>
</blockquote></td>
<td><blockquote>
<p>'h' - on hold</p>
</blockquote></td>
<td><blockquote>
<p>'c' -</p>
</blockquote></td>
<td><blockquote>
<p>complete</p>
</blockquote></td>
<td><blockquote>
<p>'dc' -</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>discontinued</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>'p'</td>
<td><blockquote>
<p>- pending</p>
</blockquote></td>
<td><blockquote>
<p>'e' - expired</p>
</blockquote></td>
<td><blockquote>
<p>'i' -</p>
</blockquote></td>
<td><blockquote>
<p>incomplete</p>
</blockquote></td>
<td><blockquote>
<p>'s' -</p>
</blockquote></td>
</tr>
</tbody>
</table>

> scheduled

> Enter ??? at the 'Select Action: ' prompt to see action descriptions and

> HELP for "^^" jump capabilities.

> \+ Next Screen AD Add original request

> \- Previous Screen RC Received Request

> RD Redisplay Screen FR Forward Request

> CM Comment

> PS Print Consult Form

> DT Detailed Order Display AR Associate Results with

> Request

> RT Results Display CT Complete Request

> DC Discontinue Order

> SP Select New Patient DY Deny Request

> Q Quit

> Select Action: \<RET\>

#### Screens and Subscreens

> The screen-oriented Enter/Edit options display screens which must be accessed in order. The user can jump to other fields on the current screen or to the beginning of the next or previous screen, but not to specific fields on other screens. An entry in some multiple fields will lead directly to a subscreen. Upon completion of the subscreen, the user is returned to the screen and field of origination. Screen-oriented Enter/Edit options and Line Enter/Edit options for a procedure usually access the same fields and subfields. The documentation for each screen will reflect any differences.

> As an example, if the ECG procedure and the Enter New ECG (Screen) option are selected, the following screen appears.

> ELECTROCARDIOGRAM (SCREEN 1 of 2) 09/16/93

> 1 ECG DATE/TIME: .................

> 2 CARDIOLOGY PATIENT: ....................

> 3 ID : ..........

> 4 WARD/CLINIC: ......

> 5 HEIGHT (INCHES): ....

> 6 WEIGHT (LBS): ....

> 7 SYMPTOMS(M): ..............................

> 8 RISK FACTORS(M): ..............................

> 9 <u>HEART MEDS(M</u>): ..............................

> 10 SYSTOLIC BP: ....

> 11 DIASTOLIC BP: ....

> 12 VENT. RATE: ...

> 13 PR INTERVAL: ...

> 14 QRS DURATION: ...

> 15 QT : ...

> 16 QTC: ...

> 17 P AXIS: ...

> 18 R AXIS: ....

> 19 T AXIS: ....

> The cursor is automatically positioned at the first field entry, the ECG date. An entry is made for each field in succession, entering \<RET\> (return key) to leave one field and go to another. A particular field may be accessed by using "^" along with the field number. A \<RET\> may be used to skip a field in which no information will be entered. To leave the screen entirely, enter \<RET\> on the last line of the field, or enter "^D" on any field line.

> Several of the procedures contain subscreens. These screens are automatically displayed when an entry is made into a field that leads to a subscreen. An underline is used in the documentation to show these subscreen fields. For example, Field \#9, Heart Meds, is a subscreen field. When a medication is selected from the items listed for this field, the heart medication subscreen appears.

> HEART MEDICATION 09/16/93

> 1 HEART MEDS: ................

> 2 DOSE: ..........

> 3 FREQUENCY: ..........

> The program automatically returns to the original screen, when the last subscreen field is completed. After completing the first ECG screen, the second ECG screen is displayed.

> ELECTROCARDIOGRAM (SCREEN 2 of 2) 09/16/93

> 1 TYPE OF EKG: ..............

> 2 CONFIRMATION STATUS: ...........

> 3 <u>INTERPRETATION CODE (RHYTHM)(M):</u> ...................

> 4 <u>INTERPRETATION CODE (CONFIG)(M):</u> ....................

> 5 <u>INTERPRETATION CODE (PACING)(M):</u> .....................

> 6 INTERPRETED BY: ........................

> 7 COMPARISON: .........................................

> 8 SUMMARY: ..........................

> 9 COMMENT(W): .....

> 10 PROCEDURE SUMMARY: .....................................

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An electronic signature is a unique set of keystrokes that are entered to give on-line approval. In the Medicine package, it is used to maintain the integrity of reported procedure results. The provider uses an electronic signature to authorize the release of the information to other users of the package. Editing of a record prior to release is controlled by limiting access to the record. Once released, the record cannot be edited. Further information on electronic signature can be found in the *Kernel V.*

> *7.0 User Manual.*

## Release Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Release control keys are assigned by the local IRM and would usually be held by providers and others designated by the provider. Prior to release, a new patient procedure record can be edited or deleted by anyone. It is unavailable in report form to non-key holders until after the provider reviews it for accuracy and completeness and changes the status from Draft to Released. There are several levels of release control.

> Draft - Unless designated otherwise, all records have draft status once they are entered. A record with Draft status may be edited or deleted. An audit trail is kept of the last person to have edited the record. It is not released to non-key holders for viewing or printing in report form.

> Problem Draft - A record may be designated as Problem Draft if the information is incomplete or inaccurate. This label should alert the provider that there is some problem with the information that needs to be resolved. The record may be edited or deleted. An audit trail is kept of the last person to have edited the record. It is not released to non-key holders for viewing or printing in report form.

> Released Not Verified - This option is used when a record may need to be released before the information has been verified or when an authorized signature is not available. A record that has been released not verified can be marked for deletion, printed, or verified either on- or off-line at another time. An internal record is made of the person releasing the record. The local IRM may elect to remove this as an option.

> Released Off-line Verified - This option is used when the provider authorizes release of the record by signing a printed copy of the report rather than the on-line version. Another key holder is designated to make the electronic release. Both persons are recorded in the release record.

> Released On-line Verified - After reviewing a record on screen, the provider may choose to release it immediately. When this option is chosen, the provider must enter a pre- designated, unique code known as an electronic signature to authorize the release of

> the record. Once released, the record can no longer be edited or deleted and is available to all users in report form.

> Superseded - Occasionally, information in a verified record may need to be modified. A copy of the original record must be made using the Superseded option. The new copy is considered a draft which can be edited prior to release. The original record remains unchanged in the file. The manager controls availability of superseded records through an option on the Manager's menu. After superseding a record, the user is automatically put into Enter/Edit mode for the new record. The new record must be released either

> on-line or off-line at this time or it will be deleted and the old record will remain unchanged.

> As shown in Table 2, the status of a record and the key that a user holds will determine the functions the user will be able to perform.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 27%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>When the record</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>The holder of...</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>status is...</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>No keys can...</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Subspecialty</strong></p>
<p><strong>Provider Key can...</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Both the Manager Key and the Subspecialty Key can...</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DRAFT</p>
</blockquote></td>
<td><blockquote>
<p>Edit* Delete*</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PROBLEM DRAFT</p>
</blockquote></td>
<td><blockquote>
<p>Edit* Delete*</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RELEASED NOT VERIFIED</p>
<p>(Optional)</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>Mark for Deletion</p>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>Mark for Deletion</p>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RELEASED OFF-LINE VERIFIED</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RELEASED ON-LINE VERIFIED</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUPERSEDED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>View/Print</p>
<p>Allow View/Print</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Table 2: User functions based on release status and key.

> \*Preventing non-key holders from editing and deleting records should be handled by excluding edit and delete menu options from non-key holders.

> Upon completion of the last field of the last procedure screen and subscreens, the Release Control screen appears.

> \* \* \* Release Control \* \* \*

> Created on: DEC 30, 1993@15:03

> DATE: SEP 27, 1993

> MEDUSER, ONE

> Current Status: DRAFT as of DEC 30, 1993@15:03 by: MEDUSER, TWO

> Do you want to change the release status? N// YES

> \* \* \* Release Control \* \* \*

> Created on: DEC 30, 1993@15:03

> DATE: SEP 27, 1993

> MEDUSER, ONE

> Current Status: DRAFT as of DEC 30, 1993@15:03 by: MEDUSER, TWO

> Select one of the following:

> 1 Draft

> 2 Problem Draft

> 3 Released On-Line Verified

> 4 Released Off-line Verified

> 5 Released not Verified

> Please Select a New Status: 1// 5 Released not Verified

> \* \* \* Release Control \* \* \*

> Created on: DEC 30, 1993@15:03

> DATE: SEP 27, 1993

> MEDUSER, ONE

> Current Status: DRAFT as of DEC 30, 1993@15:03 by: MEDUSER, TWO

> New status: Released not Verified

> This option should be used with extreme CAUTION.

> You can be held accountable for releasing unverified procedure results

> Do you still want to continue? N// YES

> Since this record is Released Not Verified

> Do you want to mark this record for deletion? NO// YES

> Record has been updated with new release information

# Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Site application coordinators should refer to the *Medicine V. 2.2 Release Notes and Installation Guide* for information concerning the implementation sequence and an example of the Medicine package installation.

## Site Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The site manager must ensure that the following fields of the Terminal Type file (#3.2) are defined according to manufacturer's specifications to provide support for the screen-oriented editing routines.

> XY CRT

> ERASE TO END OF PAGE HIGH INTENSITY

> LOW INTENSITY

> NOTE: For VAX sites installing the Medicine package, it is recommended that terminals be set to form mode for proper forms control on slave printers.

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no legal requirements for the installation and use of the Medicine package.

#### Security Keys

> Security Keys for each module in the Medicine package allow the user to view, release and sign draft procedures within that module. A key is not needed to edit procedures in the draft mode. The MCMANAGER key allows the department head or assistant department head to view procedures that have been released not verified or that have been marked for deletion. It also allows control

> over viewing superseded records.

> The following Security keys should be assigned.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 31%" />
<col style="width: 46%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Module</p>
</blockquote></td>
<td><blockquote>
<p>User keys</p>
</blockquote></td>
<td><blockquote>
<p>Manager keys</p>
<p>(assigned to department heads and assistant department heads)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cardiology GI Pulmonary PFT Hematology</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYCARD MCKEYGI MCKEYPULM MCKEYPFT MCKEYHEM</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER MCMANAGER MCMANAGER MCMANAGER MCMANAGER</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Further information concerning security may be obtained from the "Implementation and

> Maintenance" section of the *Medicine Technical Manual* and the *Package Security Guide.*

## Menu Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user menus are distributed as follows: Cardiology: MCARUSER

> GI: MCARGIUSER

> Pulmonary: MCARPULMUSER Pacemaker: MCARPACEUSER Hematology: MCARHEMUSER Rheumatology: MCRHUSER Generalized Procedure: MCGENERIC Summary of Patient Procedures: MCARSUMMARY Enable/Disable OE/RR: MCORHOOK

## Electronic Signature and Release Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of electronic signature and release control is to give clinicians the ability to maintain data integrity. Release control and electronic signature allow the users of the Medicine package to have medical procedure records with a status of Draft, Problem Draft, Released Not Verified, Released Off-line Verified, Released On-line Verified or Superseded.

## Release Control Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Release Control options are now available in all modules except Pacemaker, and Rheumatology. These options require that the user hold the Manager's key and the specific Procedure key.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>In this Module...</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Find Release Control options here.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cardiology</p>
</blockquote></td>
<td><blockquote>
<p>Cath Lab Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ECG Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Echo Lab Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EP Lab Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Holter Lab Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Exercise Tolerance Test Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Gastrointestinal</p>
</blockquote></td>
<td><blockquote>
<p>GI Management Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pulmonary</p>
</blockquote></td>
<td><blockquote>
<p>Endoscopy Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Pulmonary Function Test Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hematology</p>
</blockquote></td>
<td><blockquote>
<p>Hematology Menu</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Table 3: Location of Release Control Option Menus

> The options are:

> 1 Turn On Release Control/Elec. Signature

> 2 Convert Old Records to Released Not Verified

> 3 Print Superseded Reports

> 4 Allow Printing of Superseded Reports

> 5 Print Reports that are Marked for Deletion

> 6 Status Report

> Turn On Release Control/Elec. Signature

> This is a one-time option that will turn on release control/electronic signature. This option should only be used by the manager of this department. Once this option is executed there is no way to turn it off. Once this is turned on the non-key holders will not be able to print a record until it is released.

> Convert Old Records to Released Not Verified

> This option will convert old records or records that do not have a release status to Released Not Verified. This option can only be used if release control/electronic signature is turned on. It allows the non-key holders to view the old records but not edit them. Before executing this option, turn on release control/electronic signature. All records upgraded using this option are assigned a status of Released Not Verified. If mass updating of records is not desirable, individual records may be updated by using the Enter/Edit option to assign them Draft Status. Records that already have a release control status will not be affected. The responsibility for upgrading old records should be assigned to only one person. A MailMan message will be sent to the person responsible for converting records that tells the record number, date, and status of the records converted.

> Print Superseded Reports

> This option will allow you to display or print a superseded report.

> Allow Printing of Superseded Reports

> This option is a switch that will allow or disallow the non-managers to view superseded records from the print options. By switching this option to on, superseded records can be viewed from the print option. By switching this option to off, superseded records will be removed from the print option.

> Print Reports that are Marked for Deletion

> This option will allow the manager to display or print reports that are marked for deletion.

> Status Report

> This option provides the manager with a report of procedures statuses. It allows the user to select a range of dates and allows either release statuses, Draft statuses or both.

> The release control previously used by Hematology and Pulmonary is now obsolete. Records which were given Released status in Medicine package V. 2.0 will be assigned Released Not Verified status. Records that had Non-Released status will be assigned Draft status.

> Further information on the Medicine package release control options can be found in the

> Introduction section of this manual.

# Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CARDIOLOGY MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Medicine Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> Choose the Cardiology Menu option from the main Medicine menu.

> Upon accessing the Cardiology module, the user is normally presented with the following screen display of menu options. This is the menu distributed with the package. However, it may be revised at each site.

> 1\. Cath Lab Menu

> 2\. ECG Menu

> 3\. Echo Lab Menu

> 4\. EP Lab Menu

> 5\. Holter Lab Menu

> 6\. Exercise Tolerance Test (ETT) Menu

> 7\. Surgical Risk Analysis Menu

> 8\. Summary of Patient Procedures

> 9\. Problem Oriented Consult Menu

> 10\. Cardiology Management Menu

### Surgical Risk Analysis Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgical Risk Analysis contains options which are used for generating a Cardiac Surgery Operative Risk Assessment Report. This report is generated by combining data entered through the Pre- Surgery Risk Analysis Enter/Edit option, and the Post-Surgery Risk Analysis Enter/Edit option. The Surgical Risk Analysis Report option is used to print the report.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of patient Procedures section of this manual.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult Menu is discussed in the Problem Oriented Consult Menu section of this manual.

### Cardiology Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains the options to allow local population of the Medication file, EP Intervention file, the ECG Transfer Record Delete, and the Holter Transfer Record Delete options. Note that in order to place a drug in the Cardiology Medication file, the drug must be present in the Hospital

> Formulary.

> 1 Cardiology Medication File Update

> 2 EP Intervention File Update

> Cardiology Medication File Update

> Select MEDICATION GENERIC NAME: ASPIRIN N/F

> ...OK? YES// Y (YES)

> Drug already marked as a CARDIOLOGY Drug. Do you wish to delete it? N// O

> EP Intervention File Update

> Select EP INTERVENTION NAME: ??

> This field identifies a list of EP interventions for use by the Atrial and Ventricular study files. This list is locally entered through the Cardiology Management menu.

> Select EP INTERVENTION NAME: -----

> ARE YOU ADDING ' ' AS A NEW EP INTERVENTION (THE 1ST)? Y (YES) NAME: -------//

### Documentation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options that are common to all procedure menus in the Cardiology module are documented in this section rather than being repeated for each procedure.

#### Line Enter/Edit options

> These options access the same fields (unless otherwise noted) as the Enter/Edit (Screen) options. Field, field order, and entry descriptions are the same. Only the Enter/Edit (Screen) options are shown.

#### Procedure Test Results

> The *procedure* Test Results option found on each procedure menu prints the report of the particular procedure done. The user is asked to enter the date and time of the procedure and the device on which to print. The report contains the information that was entered using the Enter/Edit (Screen or Line) option.

#### Brief Enter/Edit (Line)

> These options access the same fields (unless otherwise noted) as the Brief Enter/Edit (Screen) options. Only the Brief Enter/Edit (Screen) options are shown. The field descriptions for the brief screens are the same as for the corresponding field on the full screens and are not reshown.

#### Brief Procedure Report

> The Brief *procedure* Report prints a report of the information that was entered using the Brief Enter/Edit options. The user is asked to enter the date and time of the procedure and the device on which to print

#### Release Control

> Each Procedure menu in the Cardiology module has a Release Control Options menu. Use of these options is usually restricted by security keys given to clinical managers. A full description of the options can be found in the Orientation and the Package Management sections of this manual under Release Control.

### Cath Lab Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1 Enter/Edit Cath (Screen)

> 2 Cath Test Results

> 3 Line Entry/Edit of Cath Record

> 4 Image Capture

> 5 Brief Line Entry/Edit of Cath Record

> 6 Brief Enter/Edit Cath (Screen)

> 7 Brief Cath Report

> 8 Release Control Options (CATH)

#### Enter/Edit Cath Lab

> There are six major cardiology catheter lab screens, with several subscreens. Subscreens are shown following their parent screen.

> Cardiac Cath Lab (Screen 1 of 6)

> CARDIAC CATH LAB (SCREEN 1 of 6) 09/16/93

> 1 DATE/TIME: .................

> 2 PATIENT: ..............................

> 3 CATH NUMBER: .........

> 4 REFERRING PHYSICIAN/AGENCY: ..............................

> 5 WARD/CLINIC: ....................

> 6 WT LBS: .... 7 HT IN: .... 8 BODY SURFACE AREA(R): .....

> 9 SYMPTOMS(M): ..............................

> 10 RISK FACTORS(M): ..............................

> 11 HEART MEDICATIONS(M): ..............................

> 12 HISTORY(W): ..... 13 PHYSICAL EXAM(W): .....

> 14 INDICATION(M): ..............................

> 15 PROCEDURE(M): ..............................

> 16 TECH COMMENTS(W): .....

> 1\. This is the date and time the procedure was performed. If "@" is entered in the date field, the entire study is deleted.

> 2\. Patient name may be entered by social security number or by last name. The first letter of the last name with the last four numbers of the SS# may be entered, as this is a dictionary field. Any dictionary option may be accessed by name or number.

> 3\. A cardiac catheterization procedure number should be entered.

> 4\. A new physician or agency may be added here.

> 5\. Any valid hospital location may be entered here.

> 6\. The weight of the patient at the time of the procedure is stored here.

> 7\. Enter the height in inches at the time of the procedure.

> 8\. Body surface area is automatically calculated in square meters from \#6 and \#7.

> 9\. The (M) caption indicates that multiple entries may be entered. Only the last input entry is shown on the screen. Enter a "?" to display all multiple entries.

> 10\. This field contains the morbidity factors to which this patient is most susceptible.

> 11\. The heart medications subscreen (shown below Cardiac Cath Lab Screen 1 of 6), is explained below.

> 12\. The (W) caption indicates a word processor field. A "?" entry will give the options for editing in this field.

> 13\. This allows the user to enter data obtained from medical patient's physical examination.

> 14\. Enter the preliminary diagnosis prior to the catheterization procedure.

> 15\. This allows the user to enter multiple cardiac cath procedures.

> 16\. The cardiac cath technician enters comments pertaining to the procedure.

> Heart Medications Subscreen of Cardiac Cath Lab (Screen 1 of 6)

> HEART MEDICATIONS 09/16/93

> 1 HEART MEDICATIONS: ....................

> 2 DOSE: ............

> 3 FREQUENCY: ..........

> 1\. Enter the cardiac medication the patient is taking at the time of the procedure.

> 2\. Enter the dosage of cardiac medications given.

> 3\. Enter the time and frequency of administration. The cursor automatically returns to the

> Cardiac Cath Lab (Screen 1 of 6).

> Cardiac Cath Lab Screen (2 of 6)

> CARDIAC CATH LAB (SCREEN 2 of 6) 09/16/93

> 1 PREMEDICATION(M): ..............................

> 2 VASCULAR ACCESS(M): ..............................

> 3 FLUORO TIME (MIN.): .....

> 4 USE OF SHEATH: ..............................

> 5 RIGHT HEART CATHETER: ...............

> 6 <u>LEFT VENTRICULAR CATHETER(M):</u> ..............................

> 7 <u>RIGHT CORONARY CATHETER(M)</u>: ..............................

> 8 <u>LEFT CORONARY CATHETER(M):</u> ..............................

> 9 AORTOGRAPHY PROJECTION: ....

> 10 OTHER PROCEDURES AND COMMENTS(W): .....

> 11 PROTAMINE: ....................

> 12 <u>HEMODYNAMICS INTERVENTION(M):</u> ..................

> 1\. Premedication refers to the medication used prior to catheterization.

> 2\. Vascular access refers to the catheter entry site.

> 3\. Fluoro time refers to the combined X-ray time (0-99 with no decimal places).

> 4\. This defines the use of a sheath during cardiac catheterization.

> 5\. This allows the user to enter the specific right heart catheter used.

> 6\. Enter multiple left ventricular catheters used.

> An entry automatically takes the user to a subscreen. After an entry is made in the last subscreen field, the user is returned to the main screen. Fields \#7 and \#8 are also subscreen fields and operate similarly. The subscreens are shown on the following page.

> In line edit mode, this field is followed by the MITRAL REGURGITATION field that allows the user to note the presence of mitral regurgitation. the entry is chosen from a list.

> 7\. This allows the user to enter multiple right coronary catheters used.

> 8\. Enter multiple left coronary catheters used.

> 9\. Aortography projection refers to the position that the aortic root projection was made in (right or left). LAO refers to left anterior oblique, and RAO refers to right anterior oblique.

> 10\. Additional information pertaining to a specific injection, or to a cath lab procedure, may be entered here.

> 11\. Protamine refers to a post catheterization drug. The dosage is entered here.

> 12\. Hemodynamics intervention has a set of three subscreens. When the last entry is made on the first subscreen, the second subscreen is accessed, with the third screen being accessed last. When the last entry is made for the third screen, the user is returned to the original screen.

> Left Ventricular Catheter Subscreen of Cardiac Cath Lab (Screen 2 of 6)

> LEFT VENTRICULAR CATHETER 09/16/93

> 1 LEFT VENTRICULAR CATHETER: ..............

> 2 ADEQUATE: ..............................

> 1\. Enter multiple left ventricular catheters used. Enter "??" for a list of choices. Enter the code number for the correct selection. You will then be asked, "Are you adding a new left ventricular catheter? Yes//" . Respond with "Y" or \<RET\>.

> 2\. Enter the adequacy of the left ventricular catheter used. Enter "1" for adequate, "2" for poor, "3" for inadequate.

> Right Coronary Catheter Subscreen of Cardiac Cath Lab (Screen 2 of 6)

> RIGHT CORONARY CATHETER 09/16/93

> 1 RIGHT CORONARY CATHETER: .....................

> 2 ADEQUACY OF ENGAGEMENT: ....................

> 1\. Enter multiple right coronary catheters used. You will then be asked, "Are you adding a new right coronary catheter? Yes//" . Respond with "Y" or \<RET\>.

> 2\. Enter the adequacy of the right coronary catheter used.

> Left Coronary Catheter Subscreen of Cardiac Cath Lab (Screen 2 of 6)

> LEFT CORONARY CATHETER 09/16/93

> 1 LEFT CORONARY CATHETER: ...................

> 2 ADEQUACY OF ENGAGEMENT: ...

> 1\. This refers to the multiple left ventricular catheters used. You will then be asked, "Are you adding a new left coronary catheter? Yes//" . Respond with "Y" or \<RET\>.

> 2\. This allows the user to enter the adequacy of the left ventricular catheter used. Hemodynamics Intervention Subscreen 1 of Cardiac Cath Lab (Screen 2 of 6)

> HEMODYNAMICS (SCREEN 1 OF 3) 09/16/93

> 14 LA A WAVE: ...

> 1 <u>INTERVENTION:</u> .................. 15 LA V WAVE: ...

> 2 OTHER INTERV. COMMENTS(W): ..... 16 LA MEAN PRESSURE: ...

> 3 RA A WAVE: .... 17 LV PRE A: ...

> 4 RA V WAVE: .... 18 LV END DIASTOLIC (Z): ...

> 5 RA MEAN PRESSURE: ... 19 LV SYSTOLIC: ...

> 6 RV SYSTOLIC: ... 20 LV PRE A POST CONTRAST: ...

> 7 RV DIASTOLIC: ... 21 LV END DIAST (Z) POST CONTRAST: ...

> 8 PA SYSTOLIC: ... 22 LV SYSTOLIC POST CONTRAST: ...

> 9 PA DIASTOLIC: ... 23 AORTIC SYSTOLIC: ....

> 10 PA MEAN: ... 24 AORTIC DIASTOLIC: ....

> 11 PCW A WAVE: ... 25 AORTIC MEAN PRESSURE: ....

> 12 PCW V WAVE: ... 26 SVC PRESSURE: ....

> 13 PCW MEAN: ... 27 IVC MEAN PRESSURE: ....

> 1\. Intervention refers to the procedure undertaken by the physician.

> 2\. This is a word processing field for any additional remarks.

> 3\. RA A wave refers to the right atrial A wave pressure.

> 4\. RA V wave is the right atrial V wave pressure.

> 5\. RA mean pressure is measured in millimeters of mercury.

> 6\. RV systolic refers to right ventricle systolic pressure.

> 7\. RV diastolic is the right ventricle diastolic pressure.

> 8\. PA systolic refers to the pulmonary artery systolic pressure.

> 9\. PA diastolic refers to the pulmonary artery diastolic pressure.

> 10\. PA mean is the pulmonary artery mean pressure in millimeters of mercury.

> 11\. PCW A wave refers to pulmonary capillary A wave pressure.

> 12\. PCW V wave refers to pulmonary capillary V wave pressure.

> 13\. PCW mean refers to pulmonary capillary mean pressure.

> 14\. LA A wave refers to the left atrial A wave pressure.

> 15\. LA V wave refers to the left atrial V wave pressure.

> 16\. LA mean pressure is the left atrial mean pressure in millimeters of mercury.

> 17\. LV Pre A refers to the left ventricular pre-A wave pressure.

> 18\. LV end diastolic (Z) refers to the left ventricular end diastolic pressure.

> 19\. LV systolic refers to the left ventricular systolic pressure.

> 20\. LV Pre A post contrast refers to the left ventricular pre-A wave post contrast.

> 21\. LV end diastolic post contrast is the left ventricular end diastolic post contrast.

> 22\. LV systolic post contrast is the left ventricular systolic post contrast pressure.

> 23\. Aortic systolic refers to the aortic systolic pressure.

> 24\. Aortic diastolic refers to the aortic diastolic pressure.

> 25\. Aortic mean pressure is measured in millimeters of mercury.

> 26\. SVC pressure refers to the superior vena cava pressure.

> 27\. IVC mean pressure refers to inferior vena cava mean pressure.

> Hemodynamics Subscreen 2 of Cardiac Cath Lab (Screen 2 of 6)

> HEMODYNAMICS (SCREEN 2 OF 3) 09/16/93

> 1 C O, ASSUMED FICK, L/MIN: .....

> 2 C I, ASS FICK L/MIN/M2(C): ......

> 3 C O, THERMO, L/MIN: .......

> 4 C I, THERMO, L/MIN/M2(C): ......

> 5 C O, INDO GREEN, L/MIN: ....... 14 PULM RESIST: ....

> 6 C I, INDO GREEN, L/MIN/M2(C):...... 15 SYSTEMIC RESIST: ....

> 7 M V PEAK GRADIENT: .......

> 8 M V MEAN GRADIENT: .......

> 9 M V AREA: ....

> 10 A V PEAK GRADIENT: ......

> 11 A V MEAN GRADIENT: ......

> 12 A V AREA, CM2: ......

> 13 A V INDEX, CM2/M2(C): ......

> 1\. CO is cardiac output. Assumed fick is a method of performing cardiac output (2 decimal places)..

> 2\. CI refers to the cardiac index. This is a calculated field.

> 3\. Allows the entry of cardiac output assuming thermo is a method of measurement (2 decimal places)..

> 4\. This field is computed from the cardiac output assuming thermo is a method of measurement.

> 5\. Allows the entry of cardiac output assuming Indo Green is a method of measurement (2 decimal places)..

> 6\. This field is computed from the cardiac output assuming Indo Green is a method of measurement.

> 7\. MV, mitral valve peak gradient, should have two decimal places.

> 8\. The mitral valve mean gradient is entered in mm Mercury from 0-20 with two decimal places allowed.

> 9\. Mitral valve area should be entered in centimeters squared (2 decimal places)..

> 10\. AV, aortic valve peak gradient, allows for two decimal places.

> 11\. The aortic valve mean gradient entry is a number from 0-200 with two decimal places allowed.

> 12\. Aortic valve area is a number from 0-5 entered in centimeters squared with two decimal places allowed.

> 13\. AV Index is calculated from \#12 and the body surface area.

> 14 & 15 Enter the pulmonary and systemic resistance as a whole number from 0-2000.

> Hemodynamics Subscreen 3 of Cardiac Cath Lab (Screen 2 of 6)

> HEMODYNAMICS (SCREEN 3 OF 3) 09/16/93

> 1 SVC SATURATION: ....

> 2 IVC SATURATION: ....

> 3 RA SATURATION: ....

> 4 RV SATURATION: ....

> 5 PA SATURATION: .... 13 L-R SHUNT: .....

> 6 LA SATURATION: .... 14 R-L SHUNT: .....

> 7 LV SATURATION: ....

> 8 LV SATURATION POST CONTRAST: ....

> 9 AORTIC SATURATION: ....

> 10 SYSTEMIC FLOW: .....

> 11 PULMONARY FLOW: .....

> 12 P/S RATIO: .....

> 1-9. Saturation refers to the amount of oxygen in the blood sample at the following cardiac system locations.

> SVC - superior vena cava IVC - inferior vena cava RA - right atrial

> RV - right ventricular PA - pulmonary artery LA - left atrial

> LV - left ventricular

> LV Saturation Post Contrast - left ventricular post contrast

> Aortic - aortic

> 10\. Enter the blood flow on the left side of the cardiac system.

> 11\. Enter the blood flow on the right side of the cardiac system.

> 12\. P/S ratio refers to the pulmonary flow/systemic flow ratio. Systemic flow refers to blood flow on the left side of the cardiac system, and pulmonic to the flow on the right side.

> 13 & 14 L-R shunt and R-L shunt refer to abnormal flow where the interventricular septum, or atrial septum, is involved. These entries are in millimeters of mercury.

> The screen automatically returns to Cardiac Cath Lab (Screen 2 of 6) upon completion of the

> Hemodynamic Subscreen 3.

> Cardiac Cath Lab (Screen 3 of 6)

> CARDIAC CATH LAB (SCREEN 3 of 6) 09/16/93

> 1 RCA NORMALITY: ..............................

> 2 <u>RCA SEGMENT(M):</u> ..............................

> 3 RCA DISTAL VESSEL: ..............................

> 4 RCA COLLATERALS: ...........

> 5 <u>RCA ORIGIN OF COLLATERALS(M):</u> ..............................

> 1\. RCA Normality refers to right coronary artery normality.

> 2\. Allows the entering of multiple Right Coronary Artery Segments. If an abnormal diagnosis is entered, a subscreen is accessed.

> 3\. RCA Distal vessel refers to distal vessel abnormality.

> 4\. RCA collaterals refer to the flow of blood from a non-diseased to a diseased artery.

> 5\. RCA origin of collaterals refers to the origin point of the collateral vessel. This subscreen is shown below the RCA Segment subscreen. When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 3 of 6).

> RCA Segment Subscreen of Cardiac Cath Lab (Screen 3 of 6)

> RCA SEGMENT 09/16/93

> 1 RCA SEGMENT: ..............................

> 2 PERCENT NARROWING: ..............................

> 3 MORPHOLOGY: ..............................

> 1\. Identify the multiple right coronary artery segments.

> 2\. Enter percent narrowing of the RCA segment.

> 3\. Indicate the lesion morphology.

> RCA Origin of Collaterals Subscreen of Cardiac Cath Lab (Screen 3 of 6)

> RCA ORIGIN OF COLLATERALS 09/16/93

> 1 RCA ORIGIN OF COLLATERALS: ....................

> 2 RECEIVING VESSEL: ..............................

> 1\. RCA origin of collaterals refers to the origin point of the collateral vessel. This subscreen is shown below the RCA Segment subscreen. When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 3 of 6). Enter "??" at each field for a list of choices.

> 2\. This allows the user to enter the receiving vessel.

> CARDIAC CATH LAB (SCREEN 4 of 6) 09/16/93

> 1 LEFT MAIN CA NORMALITY: ..............................

> 2 <u>LMCA NARROWING(M):</u> ..............................

> 3 LAD NORMALITY: ..............................

> 4 <u>LAD SEGMENT(M):</u> ..............................

> 5 LAD DISTAL VESSELS: ..............................

> 6 LAD COLLATERALS: .......

> 7 <u>LAD ORIGIN OF COLLATERALS(M):</u> ..............................

> 8 CIRCUMFLEX NORMALITY: ..............................

> 9 <u>CIRCUMFLEX SEGMENT(M):</u> ..............................

> 10 CIRCUMFLEX DISTAL VESSEL: ..............................

> 11 CIRCUMFLEX COLLATERALS: .......

> 12 <u>CIR. ORIGIN OF COLLATERALS(M):</u> ..............................

> 1\. Refers to the normality or abnormality of the left main coronary artery.

> 2\. LMCA Narrowing is the percent of narrowing of the left main coronary artery and leads to the subscreen shown below.

> 3 LAD normality refers to the left anterior descending normality or abnormality.

> 4\. LAD Segment accesses a subscreen for entering multiple LAD coronary artery segments.

> 5\. LAD Distal Vessels offers choices on the condition of the LAD distal vessels.

> 6\. This allows the user to enter left anterior descending collateral vessels.

> 7\. LAD Origin of Collaterals provides a subscreen for entering further information.

> 8\. Circumflex Normality refers to the normality or abnormality information of the circumflex artery.

> 9\. Circumflex Segment accesses a subscreen for entering multiple circumflex artery segments.

> 10\. This allows the user to enter circumflex coronary artery distal vessels.

> 11\. Enter the circumflex coronary artery collaterals.

> 12\. CIR Origin of Collaterals leads to a subscreen for entering this information.

> LMCA Narrowing Subscreen of Cardiac Cath Lab (Screen 4 of 6)

> LMCA NARROWING 09/16/93

> 1 LMCA NARROWING: .......... 2 MORPHOLOGY: ............

> 1\. Allows entry of multiple left main coronary artery narrowing percentages.

> 2\. This allows the user to enter lesion morphology. Enter "??" for a list of choices. When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 4 of 6).

> LAD Segment Subscreen of Cardiac Cath Lab (Screen 4 of 6)

> LAD SEGMENT 09/16/93

> 1 LAD SEGMENT: ..............................

> 2 PERCENT NARROWING: .................

> 3 MORPHOLOGY: .........................

> 1\. Allows entering multiple LAD coronary artery segments affected.

> 2\. Enter the percentage of narrowing.

> 3\. This allows the user to enter the lesion morphology. Enter "??" for a list of choices. When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 4 of 6).

> LAD Origin of Collaterals Subscreen of Cardiac Cath Lab (Screen 4 of 6)

> LAD ORIGIN OF COLLATERALS 09/16/93

> 1 LAD ORIGIN OF COLLATERALS: .................

> 2 RECEIVING VESSEL: .....................

> 1\. Enter information concerning the origin of LAD Origin of Collaterals.

> 2\. This allows the user to enter the receiving vessel. A "??" will show choices of receiving vessels.

> When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 4 of 6).

> Circumflex Segment Subscreen of Cardiac Cath Lab (Screen 4 of 6)

> CIRCUMFLEX SEGMENT 09/16/93

> 1 CIRCUMFLEX SEGMENT: ..................

> 2 PERCENT NARROWING: ........... 3 MORPHOLOGY: ................

> 1\. Allows entering multiple Circumflex coronary artery segments affected.

> 2\. Enter the percent of narrowing.

> 3\. Enter the morphology.

> When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 4 of 6).

> CIR Origin of Collaterals Subscreen of Cardiac Cath Lab (Screen 4 of 6)

> CIR. ORIGIN OF COLLATERALS 09/16/93

> 1 ORIGIN OF COLLATERALS: ..............................

> 2 RECEIVING VESSEL: ..............................

> 1\. This allows the user to enter the circumflex origin of collaterals.

> 2\. Enter the receiving vessel. Entering "??" will give a list of choices.

> When the last field is completed, the user is returned to the Cardiac Cath Lab (Screen 4 of 6).

> CARDIAC CATH LAB (SCREEN 5 of 6) 09/16/93

> 1 FLUOROSCOPY(M): ...................................

> 2 DOMINANCE: ..................

> 3 BYPASS GRAFT?: ...........

> 4 BYPASS GRAFTS: .....

> 5 DISTAL ANASTOMOSIS(M): ..............................

> 6 ANGIOPLASTY SEGMENT(M): ..............................

> 7 LEFT VENTRICULOGRAPHY: ..................15 RESTING HEART RATE: ....

> 8 LEFT VENTRICULAR WALL MOTION(M): ..............................

> 9 MITRAL REGURGITATION: .............. 16 EDV: ....

> 10 THROMBUS ON LV GRAM: .... 17 ESV: .... 18 CARDIAC OUTPUT(R) ....

> 11 LV EJECTION FRACTION: ..............................

> 12 AORTOGRAPHY: ....

> 13 AORTIC ROOT: ........

> 14 SINUSES OF VALSALVA: .......................

> 1\. This field prompts for whether calcium was present during Fluoroscopy.

> 2\. Enter the dominant coronary tree.

> 3\. Indicate the presence of coronary bypass grafts.

> 4\. Indicate the number of coronary bypass grafts.

> 5\. Anastomosis refers to the origin of the bypass. An entry sends the user to the anastomosis subscreen.

> 6\. An entry in this field leads to an Inflation Pressures subscreen. When a final entry is made for the inflation pressure subscreen, the user is returned to the angioplasty subscreen, and then the cardiology catheter screen.

> 7\. This field is used to enter the performance of a left ventriculography.

> 8\. This allows the user to enter multiple LV wall motion normalities on a subscreen.

> 9\. Indicate the presence of mitral regurgitation.

> 10\. Thrombus on left ventriculogram refers to an abnormal density in the left ventricular cavity.

> 11\. LV ejection fraction refers to the overall function of the left ventricle.

> 12\. Aortography is a procedure for injecting dye into the aortic root.

> 13\. Aortic root field refers to the morphology, or diseased condition, of the aortic root.

> 14\. There are always either two or three sinuses of valsalva.

> 15\. This field identifies the patient's resting heart rate.

> 16\. This allows the user to enter the left ventricular diastolic volume.

> 17\. This allows the user to enter the left ventricular end systolic volume.

> 18\. This field computes the Angiographic Cardiac Output from the Resting Heart Rate, EDV, and ESV.

> The formula used is: Heart_Rate \* (EDV - ESV).

> Distal Anastomosis Subscreen of Cardiac Cath Lab (Screen 5 of 6)

> DISTAL ANASTOMOSIS 09/16/93

> 1 DISTAL ANASTOMOSIS: ..............................

> 2 PERCENTAGE LESION: .................

> 3 LOCATION OF LESION: ..............................

> 1\. This allows the user to enter multiple distal anastomosis.

> 2\. Indicate the percentage lesion of the distal anastomosis.

> 3\. Enter the location of the lesion of the distal anastomosis.

> Angioplasty Segment Subscreen of Cardiac Cath Lab (Screen 5 of 6)

> ANGIOPLASTY SEGMENT 09/16/93

> 1 SEGMENT IF ANGIOPLASTY DONE: ..............................

> 2 STARTING % OBSTRUCTION: .................

> 3 RESULTING % OBSTRUCTION: .................

> 4 STARTING GRADIENT: ....

> 5 RESULTING GRADIENT: ....

> 6 <u>INFLATION PRESSURE IN ATM(M):</u> ..............................

> 7 TOTAL INFLATION TIME (SEC.): ....

> 1\. Angioplasty segment refers to the PTCA, where a balloon catheter is inserted into a stenosed coronary artery in order to dilate it, so that an increase in blood flow may result.

> 2\. This allows the user to enter the starting percent obstruction.

> 3\. Enter the resulting percent obstruction.

> 4\. Indicate the starting gradient.

> 5\. Enter the resulting gradient.

> 6\. This allows the user to enter inflation pressure in ATM. An entry in field six of this screen leads to another subscreen, inflation pressure (shown below).

> 7\. Enter the total inflation time in seconds.

> Left Ventricular Wall Motion Subscreen of Cardiac Cath Lab (Screen 5 of 6)

> LEFT VENTRICULAR WALL MOTION 09/16/93

> 1 LEFT VENTRICULAR WALL MOTION: ...................

> 2 DESCRIPTION: ..............................

> 1\. The Left ventricular wall motion screen defines the segment of the left ventricular which is abnormal.

> 2\. Describe by codes, the left ventricular wall motion. The program returns to the angioplasty subscreen, and then to the cardiology catheter main screen.

> Inflation Pressures Subscreen of Angioplasty Subscreen

> INFLATION PRESSURES 09/16/93

> 1 INFLATION PRESSURE: ....

> 2 INFLATION TIME IN SEC.(M): ..............................

> 1\. Permits entry of inflation pressures.

> 2\. Enter the inflation time in seconds. When a final entry is made for this inflation pressure subscreen, the user returns to the angioplasty subscreen, and then to the cardiology catheter main screen.

> CARDIAC CATH LAB (SCREEN 6 of 6) 09/16/93

> 1 COMPLICATIONS(M): ..............................

> 2 INTERPRETATION: ..............................

> 3 CONCLUSIONS(W): .....

> 4 PLAN(W): .....

> 5 CARDIOLOGY FELLOW: ..............................

> 6 CARDIOLOGY STAFF: ..............................

> 7 CARDIOLOGY FELLOW-2ND: ..............................

> 8 CARDIOLOGY STAFF-2ND: ..............................

> 9 ID : .........

> 10 SUMMARY: ..........................

> 11 PROCEDURE SUMMARY: ..................................

> 1\. The user may enter multiple cardiac cath complications.

> 2\. This allows the user to enter the final interpretation of the cardiac cath

> 3\. Provide specific conclusions in reference to the cardiac cath

> 4\. Enter specific statements concerning the patient's management plan.

> 5\. The person entered here must be in the hospital provider file.

> 6\. Identify the primary physician in attendance.

> 7\. Enter the secondary cardiology fellow.

> 8\. Enter the secondary physician in attendance.

> 9\. This field contains the patient's identification number assigned by the medical facility. In most cases it is the person's social security number.

> 10\. Summary is a required field for entry. If no entry is made, the user will not be able to continue through the screen system.

> 11\. This field will be displayed in the summary areas of Order Entry/Results Reporting and Health

> Care Summaries.

#### Other Cardiac Cath Lab Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit Cath Record, Cath Test Results, Brief Cath Reports, and Release Control Options.

#### Image Capture

> The Image Capture option allows a procedure image to be captured and attached to a patient record. This option is only available to users at a workstation which has DHCP Imaging System installed. Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for Cardiology.

#### Brief Enter/Edit Cath (Screen)

> BRIEF CARDIAC CATH LAB 09/16/93

> 1 DATE/TIME:................. 2 MEDICAL PATIENT:.................

> 3 PROCEDURE(M):..............................

> 4 INDICATION(M):..............................

> 5 <u>INTERVENTION(M):</u>.................

> 6 <u>RCA SEGMENT(M):</u>..............................

> 7 <u>LMCA NARROWING(M):</u>..............................

> 8 <u>LAD SEGMENT(M):</u>..............................

> 9 <u>CIRCUMFLEX SEGMENT(M):</u>..............................

> 10 <u>ANGIOPLASTY SEGMENT(M):</u>..............................

> 11 LV EJECTION FRACTION:.... 12 COMPLICATION(M):........................

> 13 CONCLUSION(W):..... 14 PLAN(W):..... 15 SUMMARY:..........

> 16 PROCEDURE SUMMARY:................................................

> 17 CARDIOLOGY STAFF:...........

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Cardiac Cath screen previously displayed and in the Cardiology Quick Reference Guide.

### ECG Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Enter/Edit ECG (Screen)

> 2\. ECG Test Results

> 3\. Line ECG Entry/Edit

> 4\. Summary of Automated Records Transferred

> 5\. Brief Line ECG Entry/Edit

> 6\. Brief Enter/Edit ECG (Screen)

> 7\. Brief ECG Report

> 8\. Release Control Options (ECG)

> Note that the abbreviations ECG and EKG are interchangeable.

#### Enter/Edit ECG

> Electrocardiogram (Screen 1 of 2)

> ELECTROCARDIOGRAM (SCREEN 1 of 2) 09/16/93

> 1 ECG DATE/TIME: .................

> 2 CARDIOLOGY PATIENT: ....................

> 3 ID : .......... 4 WARD/CLINIC: ..............

> 5 HEIGHT (INCHES): ....

> 6 WEIGHT (LBS): ....

> 7 SYMPTOMS(M): ..............................

> 8 RISK FACTORS(M): ..............................

> 9 <u>HEART MEDS(M):</u> ..............................

> 10 SYSTOLIC BP: ....

> 11 DIASTOLIC BP: ....

> 12 VENT. RATE: ...

> 13 PR INTERVAL: ...

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 28%" />
<col style="width: 32%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>14 QRS DURATION: ...</p>
</blockquote></td>
<td><blockquote>
<p>15 QT : ...</p>
</blockquote></td>
<td><blockquote>
<p>16 QTC: ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17 P AXIS: ... 1</p>
</blockquote></td>
<td>8 R AXIS: ....</td>
<td><blockquote>
<p>19 T AXIS: ....</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The ECG interface allows information to be automatically transferred from the ECG Cart to the DHCP Medicine package. With the ECG interface, the technician can enter items 1-11 directly onto the ECG Cart. Fields 12-19 are gathered from the ECG leads and analyzed by the ECG Cart and then printed in the header data of the computerized ECG printout.

> 1\. Enter the date of the ECG procedure.

> 2\. Identify the patient in the medical file.

> 3\. This is the patient's identification number assigned by the medical facility. In most cases it is the person's social security number.

> 4\. Give the in-house patient address.

> 5-6 Enter the height of the patient in inches, and weight at the time of the procedure.

> 7\. Indicate the patient's physical complaints or symptoms.

> 8\. Choose the morbidity factors which this patient is most susceptible to in regards to this procedure.

> 9\. An entry in this field takes the user to a subscreen When the final subscreen entry is made, the user is returned to the ECG main screen.

> 10\. Enter the systolic blood pressure.

> 11\. Give the diastolic blood pressure.

> 12\. The ECG Cart stores the ventricular rate here.

> 13\. This shows ECG PR interval retrieved from the ECG machine.

> 14\. The ECG QRS duration is displayed.

> 15\. This shows the QT interval.

> 16\. The QTC interval is provided from the ECG Cart.

> 17\. Indicates the P axis.

> 18\. Shows the R axis.

> 19\. Confirms the T axis.

> Heart Medication Subscreen of Electrocardiogram (Screen 1 of 2)

> HEART MEDICATION 09/16/93

> 1 HEART MEDS: ..............................

> 2 DOSE: ..........

> 3 FREQUENCY: ..........

> 1\. Indicate the specific cardiac medication which the patient is taking.

> 2\. Specify the dosage for the cardiac medicine that the patient is taking.

> 3\. The time/number of times the patient is to take the cardiac medicine is noted in this field.

> Electrocardiogram (Screen 2 of 2)

> ELECTROCARDIOGRAM (SCREEN 2 of 2) 09/16/93

> 1 TYPE OF EKG: ..............

> 2 CONFIRMATION STATUS: ...........

> 3 <u>INTERPRETATION CODE (RHYTHM)(M):</u> ..............................

> 4 <u>INTERPRETATION CODE (CONFIG)(M):</u> ..............................

> 5 <u>INTERPRETATION CODE (PACING)(M):</u> ..............................

> 6 INTERPRETED BY: ........................

> 7 COMPARISON: ..............................................

> 8 SUMMARY: ..........................

> 9 COMMENT(W): .....

> 10 PROCEDURE SUMMARY: ................................

> 1\. Specifies the type of ECG performed here.

> 2\. This allows the user to enter the ECG confirmation status.

> 3-5 For the information code, enter a number or first letter. This will activate subscreens for entering further information. As many entries may be made as desired but each interpretation code must have a modifier. The three associated interpretation code subscreens are displayed on the following page.

> 6\. Identify the interpreting physician.

> 7\. Enter the ECG comparison statement.

> 8\. This field contains the gross evaluation of the results of this procedure.

> 9\. Make specific comments regarding the ECG.

> 10\. Answer must be 1-79 characters in length. This will appear on the "Summary of Patient

> Procedures".

> Interpretation Code Subscreens for Electrocardiogram (Screen 2 of 2)

> INTERPRETATION CODE (RHYTHM) 09/16/93

> 1 INTERPRETATION CODE (RHYTHM): ..............................

> 2 CODE MODIFIER: .................

> INTERPRETATION CODE (CONFIG) 09/16/93

> 1 INTERPRETATION CODE (CONFIG): ..............................

> 2 CODE MODIFIER: .................

> INTERPRETATION CODE (PACING) 09/16/93

> 1 INTERPRETATION CODE (PACING): ..............................

> 2 CODE MODIFIER: .................

> 1\. Enter the interpretation code specific to the screen (rhythm, config or pacing). As many entries may be made as desired, but each interpretation code must have a modifier.

> 2\. Describe the interpretation code (rhythm, config or pacing).

> Information On ECG Auto Screens

> Now that an interface is available directly from an ECG machine, care must be taken to ensure that data remains valid.

> After the technician runs the ECG, the results are stored in the database inside the ECG machine. The technician verifies that the data is valid and then sends it to be included in the DHCP database. As noted above, validity of this data must remain intact. The data on the ECG machine must match the data in DHCP Medicine package. Therefore, once it is in DHCP, the data received directly from the ECG machine cannot be changed.

> The ECG auto screens are available since other information is also needed to complete the DHCP record (e.g., Interpreted By, Comments, and Summary). The fields that have data from the ECG machine cannot be edited, but the fields necessary to have a complete DHCP ECG record can be.

> The main ECG Auto Screen is shown below. The Heart Meds, and Interpretation Code subscreens are the same as seen for the Electrocardiogram Screens 1 and 2 shown on the previous pages.

> ECG Screen (Addition To Automated Data)

> ECG SCREEN (ADDITION TO AUTOMATED DATA) 09/16/93

> 1 DATE/TIME(R): .................

> 2 MEDICAL PATIENT(R): ..............................

> 3 SYMPTOM(M): ..............................

> 4 RISK FACTOR(M): ..............................

> 5 <u>HEART MED(M):</u> ..............................

> 6 INTERPRETED BY: ..............................

> 7 COMPARISON STATEMENT: ...........................................

> 8 <u>INTERPRETATION CODE (RHYTHM)(M):</u> ..............................

> 9 <u>INTERPRETATION CODE (CONFIG)(M):</u> ..............................

> 10 <u>INTERPRETATION CODE (PACING)(M):</u> ..............................

> 11 COMMENT(W): .....

> 12 SUMMARY: ..........................

> 1\. This field identifies the specific EKG procedure.

> 2\. The patient's name is indicated.

> 3\. Relate the patient's physical complaints or symptoms.

> 4\. Specify the morbidity factors which this patient is most susceptible to in regards to this procedure.

> 5\. Document the cardiac medicines that the patient is taking at the time of this procedure

> (multiple).

> 6\. Identify the interpreting physician.

> 7\. Enter the ECG/EKG comparison statement.

> 8-10 For the information code, enter a number or first letter. This will activate subscreens for entering further information. As many entries may be made as desired but each interpretation code must have a modifier. The three associated interpretation code subscreens are displayed on the following page.

> 11\. Make specific comments regarding the ECG/EKG.

> 12\. Specify the gross evaluation of the results of this procedure.

> Heart Medication Subscreen of ECG Screen (Addition To Automated Data)

> HEART MED (ECG AUTO) 09/16/93

> 1 HEART MED:.............................. 2 DOSE:..........

> 3 FREQUENCY:..........

> 1\. Indicate the specific cardiac medication which the patient is taking at the time of the procedure.

> 2\. Specify the dosage for the cardiac medicine that the patient is taking.

> 3\. The time/number of times the patient is to take the cardiac medicine is noted in this field.

> Interpretation Code Subscreens for ECG Screen (Addition To Automated Data)

> INTERPRETATION CODE (RHYTHM) (ECG AUTO) 09/16/93

> 1 INTERPRETATION CODE (RHYTHM): ..............................

> 2 CODE MODIFIER: .................

> INTERPRETATION CODE (CONFIG) (ECG AUTO) 09/16/93

> 1 INTERPRETATION CODE (CONFIG): ..............................

> 2 CODE MODIFIER: .................

> INTERPRETATION CODE (PACING) (ECG AUTO) 09/16/93

> 1 INTERPRETATION CODE (PACING): ..............................

> 2 CODE MODIFIER: .................

> 1\. Enter the interpretation code specific to the screen (rhythm, config or pacing). As many entries may be made as desired, but each interpretation code must have a modifier.

> 2\. Describe the interpretation code (rhythm, config or pacing).

#### Other ECG Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit, ECG Test Results, Brief ECG Reports, and Release Control options.

#### Summary of Automated Records Transfer

> This option prints a report of the transfer of patient records from a data storage system to the DHCP system, with a listing of patient name, patient social security number, test date, transfer date, and transfer status. The patient name and social security number in the data storage system are checked against information in the DHCP system before transfer. Unsuccessful transfers due to invalid test date, failure to match patient name or social security number, or other causes are indicated on the summary report. Entries are listed according to the attempted transfer dates within a specified time period.

#### Brief Enter/Edit ECG (Screen)

> Brief Electrocardiogram Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 VENT. RATE:....

> 4 PR INTERVAL:....

> 5 QRS DURATION:....

> 6 QT:....

> 7 COMPARISON STATEMENT:......................................

> ............................................

> 8 AUTO-INSTRUMENT DIAGNOSIS(W):.....

> 9 SUMMARY:..........................

> 10 PROCEDURE SUMMARY:..........................................

> 11 INTERPRETED BY:..............................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Electrocardiogram screen previously displayed and in the Cardiology Quick Reference Guide.

### Echo Lab Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Enter/Edit Echo (Screen)

> 2\. Echo Test Results

> 3\. Line Entry/Edit of Echo Test

> 4\. Image Capture

> 5\. Brief Line Echo Entry/Edit

> 6\. Brief Enter/Edit Echo (Screen)

> 7\. Brief Echo Report

> 8\. Release Control Options (ECHO)

> *Enter/Edit Echo (Screen)*

> Echo Lab Menu

> 1\. Enter/Edit Echo (Screen)

> 2\. Echo Test Results

> 3\. Line Entry/Edit of Echo Test

> 4\. Image Capture

> 5\. Brief Line Echo Entry/Edit

> 6\. Brief Enter/Edit Echo (Screen)

> 7\. Brief Echo Report

> 8\. Release Control Options (ECHO)

#### Enter/Edit Echo (Screen)

> Echo Laboratory (Screen 1 of 4)

> ECHO LABORATORY (SCREEN 1 of 4) 09/16/93

> 1 DATE/TIME: .................

> 2 CARDIOLOGY PATIENT: ..............................

> 3 ID: .......... 4 WARD/CLINIC: ..................

> 5 WT LBS: .... 6 HT IN: ....

> 7 BODY SURFACE AREA(R): .....

> 8 RESTING SYSTOLIC BP: .... 9 RESTING DIASTOLIC BP: ....

> 10 RESTING HEART RATE: ....

> 11 RHYTHM: .....

> 12 STUDY QUALITY: ....

> 13 SYMPTOMS(M): ..............................

> 14 RISK FACTORS(M): ..............................

> 15 <u>MEDICATION(M)</u>: ..............................

> \| 16 STUDY TYPE(M): ..............................

> 1\. Indicate the date and time when the echo was taken.

> 2\. Identify the patient in the medicine file.

> 3\. Enter any site specific unique identification number for this ECHO test. There is no need to enter the SSN. SSN is already recorded for this ECHO.

> 4\. Indicate the medical patient's location in the facility.

> 5\. Give the patient's weight in pounds.

> 6\. Enter the patient's height in inches.

> 7\. Body surface area is automatically calculated from the weight and height.

> 8-10 Indicate the patient's resting systolic blood pressure, diastolic blood pressure, and heart rate.

> 11\. Enter the patient's current ECG/EKG rhythm.

> 12\. Establish the technical quality of the procedure.

> 13\. Itemize the patients symptoms listed on the procedure request form.

> 14\. Indicate the patient's risk factors listed on the procedure request form.

> 15\. An entry in the Medication field leads to a subscreen. Upon completion of the subscreen, the user is returned to Echo Laboratory (Screen 1 of 4).

> \|16. Enter the type(s) of echocardiographic study.

> Medication Subscreen of Echo Laboratory (Screen 1 of 4)

> MEDICATION 09/16/93

> 1 MEDS (CARDIOLOGY MEDICATION):..........................

> 2 DOSE:..........

> 3 FREQUENCY:..........

> 1\. Identify the specific medications.

> 2\. Enter the dosage of medication listed on the medical patient's request form.

> 3\. Indicate when/how often (frequency) medication is to be taken.

> Echo Laboratory (Screen 2 of 4)

> ECHO LABORATORY (SCREEN 2 of 4) 09/16/93

> 1 SEPTUM: ....

> 2 POSTERIOR WALL: ....

> 3 LT. ATRIUM: ....

> 4 AORTIC ROOT: ....

> 5 RT VENTRICLE: ....

> 6 ANT. RV WALL: ....

> 7 LT. VENT. DIASTOLE: ....

> 8 LT. VENT. SYSTOLE: ....

> 9 % FRACT. SHORTENING(C): .........

> 10 E-SEPT.: ....

> 11 EDV: ...... 12 ESV: ......

> 13 EF(C): .........

> 14 ESTIMATED EF: .... 15 ESTIMATED EF DESCRIPTOR: ....................

> 16 <u>REGIONAL WALL MOTION(M):</u> ..............................

> Fields \#1 - \#8 are patient specific.

> 1\. A septum is a wall within the heart. Enter the thickness of the inter ventricular septum in millimeters.

> 2\. The thickness of the left ventricular posterior wall is entered here.

> 3\. The diameter of the left atrium is entered here.

> 4\. The diameter of the aortic root, the major artery for conveying blood through the heart, is entered here.

> 5\. Enter the diameter of the right ventricular cavity.

> 6\. Enter the anterior right ventricular wall thickness.

> 7\. The left ventricular diastolic internal dimensions are entered here. The diastolic interval is when the heart is filled with blood.

> 8\. Enter the left ventricular systolic internal dimensions. The systolic interval is when blood is being pumped throughout the system.

> 9\. The percentage fractional shortening, based upon the left ventricular diameters, is automatically calculated.

> 10\. The E-sept is the distance between the E-point of the mitral valve and the left side of the interventricular septum.

> 11\. Enter the left ventricular end diastolic volume.

> 12\. Give the left ventricular end systolic volume.

> 13\. The ejection fraction is calculated from \#11 and \#12.

> 14\. Any estimated ejection fraction derived from other methods is entered here.

> 15\. The estimated ejection fraction descriptor pertains to observations derived from other methods.

> 16\. Enter multiple left ventricular regional wall abnormalities. Regional wall motion accesses a subscreen.

> Regional Wall Motion Subscreen of Echo Laboratory (Screen 2 of 4)

> REGIONAL WALL MOTION 09/16/93

> 1 REGIONAL WALL MOTION:..............................

> 2 MODIFIER:..................

> 1\. Identify multiple left ventricular regional wall abnormalities.

> 2\. Choose a descriptive code for type of regional wall abnormalities.

> Echo Laboratory (Screen 3 of 4)

> ECHO LABORATORY (SCREEN 3 of 4) 09/16/93

> 1 <u>DOPPLER VALVE REGURG(M):</u> ........................

> 2 AORTIC MAX VELOCITY: .... 15 MITRAL MEAN GRADIENT: ....

> 3 AORTIC MEAN VELOCITY: .... 16 MITRAL P 1/2: ....

> 4 AORTIC INTEGRAL : .... 17 MITRAL EST VALVE ORIFICE: ....

> 5 LVOT MAX VELOCITY: .... 18 PULMONIC MAX VELOCITY: ....

> 6 LVOT MEAN VELOCITY: .... 19 PULMONIC MEAN VELOCITY: ....

> 7 LVOT INTEGRAL: .... 20 PULMONIC INTEGRAL: ....

> 8 AORTIC MAX PRESSURE GRAD(C): ..... 21 PULM MAX PRESSURE GRAD(C): .....

> 9 AORTIC MEAN PRESSURE GRADIENT: .... 22 PULMONIC MEAN GRADIENT: ....

> 10 AORTIC EST. VALVE ORIFICE: .... 23 TRICUS DIAS MAX VEL (m/s): ....

> 11 MITRAL MAX VELOCITY: .... 24 TRICUS DIAS MAX PRESS GRAD: ....

> 12 MITRAL MEAN VELOCITY: .... 25 TRICUS REGURG SYS MAX VEL(m/s): ....

> 13 MITRAL INTEGRAL: .... 26 PA SYSTOLIC PRESSURE: .....

> 14 MITRAL MAX GRADIENT(C): .....

> 1\. This field leads to a subscreen for entering multiple doppler findings.

> 2\. The aortic valve max velocity is entered in meters per second(msec).

> 3\. Indicate the mean velocity in meters per second.

> 4\. Enter the aortic valve integral in centimeters.

> 5\. Enter Left ventricular overflow tract max relative velocity in meters per second.

> 6\. Indicate the left ventricular outflow tract mean velocity in meters per second.

> 7\. Enter the left ventricle outflow integral (cm/sec).

> 8\. The pressure gradient is automatically calculated from the aortic valve maximum velocity.

> 9\. The pressure value is in mm Hg.

> 10\. Enter the calculated aortic valve estimated orifice.

> 11,12 Enter the mitral valve maximum and mean velocities in meters per second.

> 13\. Specify the mitral valve calculated integral.

> 14\. The mitral maximum gradient is a calculated field.

> 15\. The mean gradient is in mm Hg.

> 16\. Enter the mitral valve pressure half-time in meters per second.

> 17\. Indicate this value in millimeters squared.

> 18-19 Enter the pulmonic valve maximum and mean relative velocities in meters per second.

> 20\. Give the pulmonic valve integral in millimeters.

> 21\. The pulmonic maximum pressure gradient is calculated from fields \#18.

> 22\. The mean gradient is entered in millimeters of mercury.

> 23\. The tricuspid maximum velocity is in meters per second.

> 24\. The pressure gradient is calculated from the tricus dias max vel in meters per second.

> 25\. Enter this information in millimeters.

> 26\. The pulmonary artery wedge pressure is measured in millimeters of mercury.

> Doppler Valve Regurg Subscreen of Echo Laboratory (Screen 3 of 4)

> DOPPLER VALVE REGURG 09/16/93

> 1 DOPPLER: ........... 2 SEVERITY: ........

> 1\. Indicate multiple doppler findings.

> 2\. Choose a descriptive code for type of doppler finding.

> Echo Laboratory (Screen 4 of 4)

> ECHO LABORATORY (SCREEN 4 of 4) 09/16/93

> 1 <u>FINDINGS(M):</u> ..............................

> 2 <u>DIAGNOSIS(M):</u>........................................

> 3 OTHER CONCLUSIONS(W): .....

> 4 CARDIOLOGY ATTENDING:........................

> 5 CARDIOLOGY FELLOW:........................

> 6 SUMMARY: ..........................

> 7 PROCEDURE SUMMARY: ............................................

> 1\. Multiple interpreted Echo findings can be entered.

> 2\. The user can identify multiple interpreted Echo diagnoses.

> 3\. Furnish additional comments on the findings and diagnosis fields.

> 4\. Identify the physician who interpreted the procedure.

> 5\. Identify the key members of the clinical staff assigned to follow this patient.

> 6\. Indicate the result of the Echo procedure.

> 7\. Enter the procedure summary information.

#### Other Echo Lab Options

> Please refer to Enter/Edit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit , Echo Test Results, Brief Echo Reports, and Release Control options.

#### Image Capture

> The Image Capture option allows a procedure image to be captured and attached to a patient record. This option is only available to users at a workstation with DHCP Imaging System installed.

> Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for Cardiology.

#### Brief Enter/Edit Echo (Screen)

> Brief Echo Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 SEPTUM:.... 4 POSTERIOR WALL:....

> 5 LT. VENT. DIASTOLE:.... 6 LT. VENT. SYSTOLE:....

> 7 REGIONAL WALL MOTION(M):..............................

> 8 FINDINGS(M):..............................

> 9 DIAGNOSIS(M):........................ 10 OTHER CONCLUSION(W):.....

> 11 SUMMARY:..........

> 12 PROCEDURE SUMMARY:.........................................

> 13 CARDIOLOGY ATTENDING:..............................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding Echo screen previously displayed and in the Cardiology Quick Reference Guide.

### EP Lab Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Enter/Edit EP (Screen)

> 2\. Results of EP Tests

> 3\. EP Line Entry/Edit

> 4\. Brief EP Line Entry/Edit

> 5\. Brief Enter/Edit EP (Screen)

> 6\. Brief EP Report

> 7\. Release Control Options (EP)

> This procedure has two main screens with several subscreens. At the end of the two main screens, a prompt will appear for accessing the Atrial Study and Ventricular Study Screens. The relationship of the subscreens to the main screens will be explained within the texts of the main screens, with special explanations being given for the more complex screens.

#### Enter/Edit EP (Screen)

> In Screen Enter/Edit mode, the user can branch immediately to enter "ATRIAL" and "VENTRICULAR" studies after selecting an Electrophysiology (EP) Date/Time. Enter an ^ at the first Electrophysiology field to access the Atrial Study screen. At the first Atrial Study field, enter

> \<RET\> to access the Ventricular Study screen.

> Electrophysiology Procedure (Screen 1 of 2)

> ELECTROPHYSIOLOGY (Screen 1 of 2) 09/16/93

> 1 DATE/TIME: ................. 2 Patient (R):...........

> 3 ID: .......... 4 WARD/CLINIC: ..........

> 5 SYMPTOM(M): ..............................

> 6 RISK FACTOR(M): ..............................

> 7 <u>HEART MEDICATION(M):</u> ..............................

> 8 HOSPITAL OF STUDY: ........................................

> 9 REASON FOR STUDY: .....................................

> 10 ARRHYTHMIA DX(M): ..............................

> 11 CARDIAC DX: .............................................

> 12 HX(W): .....

> 13 EJECTION FRACTION: ....

> 14 EJECTION FRACTION METHOD: ................

> 15 <u>HEART BLOCK(M):</u> ..............................

> 1\. Specify the date and time that the procedure was entered into the database.

> 2\. The patient name will be displayed in this field.

> 3\. This field contains the patient identifier.

> 4\. The patient's hospital location should be entered.

> 5\. Summarize the clinical signs of disease.

> 6\. Indicate the conditions which contribute to the overall percentages of disease.

> 7\. Upon making a selection, the heart medication subscreen is accessed.

> 8\. Identify the facility performing this procedure.

> 9\. Establish the specific reasons for the study.

> 10\. Arrhythmia DX refers to arrhythmia diagnosis.

> 11\. Cardiac DX refers to cardiac diagnosis.

> 12\. Summarize the relevant patient history.

> 13\. Ejection fraction refers to the overall function of the heart, expressed as a percentage.

> 14\. Enter the method used to obtain the ejection fraction here.

> 15\. Heart block is a multiple field. Upon making a selection, the heart block subscreen is accessed. The user is returned to Electrophysiology Procedure Screen 1 of 2 after the subscreen entries are completed.

> Heart Med EP Subscreen of Electrophysiology Procedure (Screen 1 of 2)

> HEART MED-EP 09/16/93

> 1 HEART MEDICATION: ................... 2 DOSE: ..........

> 3 FREQUENCY: ..........

> 1\. Identify the medication which has been prescribed for the patient.

> 2\. Enter dosage of medicine the patient is taking.

> 3\. Indicate time/number of times (frequency) patient should take medicine.

> Heart Block EP Subscreen of Electrophysiology Procedure (Screen 1 of 2)

> HEART BLOCK-EP 09/16/93

> 1 HEART BLOCK: ........................

> 2 UNDERLYING RHYTHM: ....................................

> 3 RESPONSE TO ATROPINE: ..................................

> 4 RESPONSE TO EXERCISE: ..................................

> 5 RESPONSE TO CAROTID MASSAGE: ...........................

> 1\. Define the state of heart block.

> 2\. Describe the rhythm associated with the particular block.

> 3\. Indicate the response to atropine.

> 4\. Enter the response to exercise.

> 5\. Indicate the response to carotid massage.

> Upon completing this screen, the user is returned to Screen 1.

> Electrophysiology Procedure (Screen 2 of 2)

> ELECTROPHYSIOLOGY (Screen 2 of 2) 09/16/93

> 1 <u>CAROTID STIMULATION(M):</u> ..............................

> 2 SVT-TYPE(M): ................

> 3 INTERPRETATION(W): .....

> 4 COMMENT(W): .....

> 5 FOLLOW UP(M): .........................

> 6 CARDIOLOGY STAFF: ..............................

> 7 CARDIOLOGY FELLOW: ..............................

> 8 CARDIOLOGY STAFF-2ND: ..............................

> 9 CARDIOLOGY FELLOW-2ND: ..............................

> 10 SUMMARY: ..........................

> 11 PROCEDURE SUMMARY: .........................................

> 1\. Indicate the episodes of carotid stimulation. This is a subscreen field.

> Upon completing the subscreen entries, the user is returned to this screen.

> 2\. SVT refers to supraventricular tachycardia.

> 3\. Enter the clinical interpretation.

> 4\. Summarize comments pertaining to the procedure.

> 5\. Indicate follow-up care/diagnostics.

> 6-9 Identify the specific participating clinical staff.

> 10\. This field is for the overall patient summary, not the carotid stimulation result which would be entered in the interpretation field (#3). Choose from N for Normal, A for Abnormal, or B for Borderline.

> 11\. This field provides input into the summary of patient procedures.

> At the end of this screen, the atrial study date/time prompt appears. This leads to the first Atrial Study screen. (Note: The Atrial Study screen will also appear if the user enters "^" in the Atrial EKG screen.)

> Carotid Stimulation Subscreen of Electrophysiology Procedure (Screen 2 of 2)

> CAROTID STIMULATION-EP 09/16/93

> 1 CAROTID STIMULATION: ...................

> 2 LONGEST PAUSE: ....

> 1\. Document the episodes of carotid stimulation.

> 2\. Describe the longest pause.

> Atrial Study (Screen 1 of 2)

> ATRIAL STUDY (SCREEN 1 OF 2) 09/16/93

> 1 DATE/TIME: .................

> 2 EP RECORD(R): .................

> 3 INTERVENTION: ...........................................

> 4 PREMEDICATION: ..............................

> 5 <u>EKG(M):</u> .................

> 6 ENTRY SITE: ..............................

> 7 RECORDING SITE: ..............................

> 8 PACING SITE: ........................

> 9 ATRIAL THRESHOLD (mA): .....

> 10 P-A INTERVAL: ....

> 11 A-H INTERVAL: ....

> 12 H-V INTERVAL: ....

> 13 <u>DRIVE CYCLE LENGTH(M):</u> ..............................

> 14 MAX 1:1 AV CONDUCTION: ....

> 1\. Indicate the specific Atrial Study by date and time.

> 2\. Identifies the electrophysiologic record.

> 3\. Describe the intervention associated with this procedure.

> 4\. Document the medication used prior to the start of this procedure.

> 5\. EKG is a multiple field. Entry of the date and time of the EKG for this study is required. An entry in this field takes the user to the Atrial Study EKG subscreen. Upon exiting that screen, the user is returned to the Atrial Study (Screen 1 of 2).

> 6\. Describe the catheter entry site used during this procedure.

> 7\. Indicate the catheter placement site.

> 8\. Identify the anatomical location of the pacing mechanism.

> 9\. Atrial threshold refers to the lowest amount of current which captures the atrium. Use milliamperes for this entry.

> 10\. This field refers to the distance from the earliest surface P wave to the lowest septal atrial activation.

> 11\. This field refers to the distance from the low septal to the earliest septal his activity.

> 12\. Indicate the H-V interval.

> 13\. Enter the drive cycle length in milliseconds. A subscreen will be accessed for entering the specific refractory periods.

> 14\. Max 1:1 A-V conduction refers to the shortest cycle length in milliseconds.

> Atrial Study EKG Subscreen of Atrial Study (Screen 1 of 2)

> ATRIAL STUDY EKG 09/16/93

> 1 DATE/TIME OF EKG: .................

> 2 RHYTHM(M): ..............................

> 3 ATRIAL CYCLE LENGTH: ....

> 4 VENTRICULAR CYCLE LENGTH: ....

> 5 QRS DURATION: ....

> 6 QRS AXIS: ....

> 7 P-R DURATION: ....

> 8 QT: ....

> 9 QTC (C): ....

> 10 INTERPRETATION: .......................................

> 1\. Enter the date and time for the EKG procedure.

> 2\. Rhythm refers to the regular underlying heart rhythm of the patient.

> 3\. Give the atrial cycle length.

> 4\. Enter the ventricular cycle length.

> 5\. Indicate the duration of the QRS wave.

> 6\. The QRS axis is entered here.

> 7\. Specify the P-R interval duration.

> 8\. Enter the QT axis.

> 9\. This field is computed from the QT information.

> 10\. The user enters information from tests in this field.

> Upon exiting this screen, the user is returned to the Atrial Study 1 screen.

> Drive Rate Subscreen of Atrial Study (Screen 1 of 2)

> DRIVE RATE-ATRIAL 09/16/93

> 1 DRIVE CYCLE LENGTH: ....

> 2 AERP: ....

> 3 AFRP: ....

> 4 ARRP: ....

> 5 AVERP: ....

> 6 AVFRP: ....

> 7 AVRRP: ....

> 8 HPERP: ....

> 9 HPFRP: ....

> 10 HPRRP: ....

> 1\. This field identifies the drive cycle length.

> 2\. AERP refers to Atrial Effective Refractory Period.

> 3\. AFRP refers to Atrial Functional Refractory Period.

> 4\. ARRP refers to Atrial Relative Refractory Period.

> 5\. AVERP refers to AV Nodal Effective Refractory Period.

> 6\. AVFRP refers to AV Nodal Functional Refractory Period.

> 7\. AVRRP refers to AV Nodal Relative Refractory Period.

> 8\. HPERP refers to His Purkinje Effective Refractory Period.

> 9\. HPFRP refers to His Purkinje Functional Refractory Period.

> 10\. HPRRP refers to His Purkinje Relative Refractory Period.

> Upon exiting this screen, the user is returned to the Atrial Study (Screen 1 of 2). Atrial Study (Screen 2 of 2)

> ATRIAL STUDY (SCREEN 2 OF 2) 09/16/93

> 1 WENCKE CYCLE LENGTH: ....

> 2 BLOCK SITE: ..............

> 3 TACHYCARDIA WINDOW: ..............................

> 4 TACHYCARDIA CYCLE LENGTH: ....

> 5 TACHYCARDIA MORPHOLOGY: ..........

> 6 PR INTERVAL: ....

> 7 RP INTERVAL: ....

> 8 RP/PR RATIO(C): ..........

> 9 ABERRATION: ......... 10 SACT: .... 11 CSART: ....

> 12 <u>BYPASS TRACT(M):</u> ..............................

> 13 <u>DISCHARGE DATE(M):</u> ........... 14 COMMENT(W): .....

> 15 CARDIOLOGY STAFF: ..............................

> 1\. Wencke cycle length refers to the longest cycle length associated with the A-V nodal Wencke block.

> 2\. This pertains to the block site.

> 3\. Enter the range of atrial coupling intervals (A1-A2) which create tachycardia, or fast heart rate. A1 and A2 refer to different stimulus times.

> 4\. Enter the cycle length in milliseconds.

> 5\. This field identifies the tachycardia morphology.

> 6\. Specify, in milliseconds, the time from high rate atrial electrogram to the earliest ventricular atrial as measured from the EP tape..

> 7\. Enter the time from the earliest ventricular to the high atrial electrogram (milliseconds) as measured from the EP tape.

> 8\. Computes the RP/PR ratio.

> 9\. Identify the aberration found in this study.

> 10\. SACT refers to sinal atrial conduction time in milliseconds.

> 11\. CSART refers to correct sinal atrial conduction time.

> 12\. Bypass tract is a multiple field. An entry in this field takes the user to the Bypass Tract- Atrial subscreen.

> 13\. Discharge Date is a multiple field accessing a subscreen.

> 14\. Enter comments and instructions pertinent to the patient's discharge.

> 15\. This field identifies the cardiology staff attending this procedure.

> Upon completion of this screen, the Ventricular Study screens will be automatically accessed.

> Bypass Tract Atrial Subscreen of Atrial Study (Screen 2 of 2)

> BYPASS TRACT-ATRIAL 09/16/93

> 1 BYPASS TRACT: .............................

> 2 CONDUCTION: .............

> 3 ARRHYTHMIA(M): ....

> 4 SHORTEST PRE-EXCITED R-R A FIB: ....

> 5 SHORTEST R-R POST ISUPREL: ....

> 6 LOCATION OF TRACT: .....................

> 7 V-HRA TIME: ....

> 8 ANTEGRADE ERP, BYPASS TRACT: ....

> 9 ANTEGRADE ERP, BYPASS ISUPREL: ....

> 10 RETROGRADE ERP, BYPASS TRACT: ....

> 11 RETROGRADE ERP, BYPASS ISUPREL: ....

> 1\. This field identifies the bypass tract.

> 2\. Describe the bypass tract conduction.

> 3\. This allows further explanation of the type of arrhythmia.

> 4\. Indicate the shortest pre-excited R to R (atrial fibrillation) interval, measured in milliseconds.

> 5\. Give the shortest pre-excited post isuprel, measured in milliseconds.

> 6\. Describe the location of tract.

> 7\. V-HRA time refers to the conduction time from ventricle to high right atrial.

> 8-9. ERP refers to the effective refractory period, measured in milliseconds. This is the longest coupling interval which fails to conduct through the bypass tract, from A1 to A2. A1 and A2 are different stimulus times.

> 10-11. These fields refer to the longest coupling interval which fails to conduct through the bypass tract. An entry in field 11 returns the user to Atrial Study (Screen 2 of 2).

> Discharge Date Subscreen of Atrial Study (Screen 2 of 2)

> DISCHARGE-ATRIAL 09/16/93

> 1 DISCHARGE DATE: .................

> 2 MEDICATION ON DISCHARGE: .......................

> 1\. Enter discharge date.

> 2\. Specify the patient's medications upon discharge.

> Ventricular Study (Screen 1 of 2)

> VENTRICULAR STUDY (SCREEN 1 OF 2) 09/16/93

> 1 DATE/TIME: .................

> 2 EP RECORD(R): .................

> 3 INTERVENTION: ..............................

> 4 PREMEDICATION: ..............................

> 5 <u>EKG(M):</u> .................

> 6 ENTRY SITE: ..............................

> 7 CATHETER PLACEMENT SITE: ..............................

> 8 PACING SITE: ............................

> 9 VENTRICULAR THRESHOLD: .....

> 10 <u>DRIVE CYCLE LENGTH(M):</u> ..............................

> 11 VIP(#REPETITIVE BEATS): .........

> 12 LAST 1:1 VIP: ....

> 13 V.T.?: ..............................

> 14 INITIATION SEQUENCE OF VT: ..................................................

> 1\. Indicate the date and time the procedure was entered into the database.

> 2\. This is the EP record identifier.

> 3\. Document any intervention necessary for this procedure.

> 4\. Specify the medication given before the procedure.

> 5\. EKG leads to a subscreen for entering specific information.

> 6-8 Identify the anatomical location of the catheter entry, the recording site and the pacing site.

> 9\. This field refers to the lowest current which captures the ventricle.

> 10\. Entering a drive cycle length for this field accesses a subscreen.

> 11\. Enter the number of repetitive ventricular responses on termination of ventricular burst pacing.

> 12\. Indicate the shortest pacing interval which results in a 1:1 ventricular capture. 1:1 is the correct ratio for an acceptable range (240-260).

> 13\. This refers to ventricular tachycardia.

> 14\. For initiation sequence, enter the stimulation protocol utilized to induce ventricular tachycardia.

> EKG Subscreen of Ventricular Study (Screen 1 of 2)

> EKG-VENTRICULAR STUDY 09/16/93

> 1 DATE/TIME OF EKG: .................

> 2 RHYTHM(M): ..............................

> 3 ATRIAL CYCLE LENGTH: ....

> 4 VENTRICULAR CYCLE LENGTH: ....

> 5 QRS DURATION: ....

> 6 QRS AXIS: ....

> 7 P-R DURATION: ....

> 8 QT: ....

> 9 QTC (C): ....

> 10 INTERPRETATION: ............................

> 1\. Indicate the date and time of the EKG .

> 2\. The underlying intrinsic rhythm of the patient should be entered here.

> 3&4 Enter the atrial and ventricle cycle lengths in milliseconds.

> 5&6 Give the QRS Duration interval and Axis.

> 7\. Indicate the P-R Duration interval.

> 8\. Specify the QT Axis.

> 9\. This field is computed from the QT information.

> 10\. This allows the user to enter information from the tests.

> Drive Cycle Length Subscreen of Ventricular Study (Screen 1 of 2)

> DRIVE RATE-VENTRICULAR 09/16/93

> 1 DRIVE CYCLE LENGTH: ....

> 2 1VES(#REPETITIVE BEATS): .........

> 3 VERP (1 VES): ....

> 4 2VES(#REPETITIVE BEATS): .........

> 5 VERP (2 VES): ....

> 6 3VES(#REPETITIVE BEATS): .........

> 7 VERP (3 VES): ....

> 1\. This field identifies the drive cycle length.

> 2\. 1VES refers to Ventricular Extrastimulus.

> 3\. VERP is the Ventricular Effective Refractory Period.

> 4\. 2VES refers to Ventricular Extrastimulus.

> 5\. VERP refers to Ventricular Effective Refractory Period.

> 6\. 3VES is the Ventricular Extrastimulus.

> 7\. VERP refers to Ventricular Effective Refractory Period.

> Ventricular Study (Screen 2 of 2)

> VENTRICULAR STUDY (SCREEN 2 OF 2) 09/16/93

> 1 DURATION OF VT/VF: ....

> 2 V-T AXIS: ..........

> 3 V-T CYCLE LENGTH: ....

> 4 V-T MORPHOLOGY: ...............

> 5 TERM. V-T: .......................

> 6 PACE OUT RATE OF V-T: ....

> 7 CARDIOVERSION: .........................................

> 8 <u>DISCHARGE DATE(M):</u> .................

> 9 COMMENT(W): .....

> 10 CARDIOLOGY STAFF: ..............................

> 1\. Indicate the total duration of ventricular tachycardia or ventricular fibrillation, measured in seconds.

> 2\. Enter the frontal plane of the QRS axis during ventricular tachycardia. Plane faces are right, left, right end superior, and normal.

> 3\. Identify the V-T cycle length.

> 4\. Specify the V-T morphology.

> 5\. Enter the interventions needed to terminate ventricular tachycardia.

> 6\. Make an entry only if pacing was used in field \#5. Use the pacing rate required to terminate ventricular tachycardia.

> 7\. Indicate the cardioversions and the cardioversion energy used.

> 8\. Discharge date is a subscreen field.

> 9\. This field is for entering the comments.

> 10\. Identify the cardiology staff assigned to this case.

> Discharge Date Subscreen of Ventricular Study (Screen 2 of 2)

> DISCHARGE DATE-VENTRICULAR STUDY 09/16/93

> 1 DISCHARGE DATE: .................

> 2 MEDICATION ON DISCHARGE: ...........................

> 1\. Indicate the discharge date.

> 2\. Enter the patient's medications upon discharge.

> Completing the entries will return the user to the second Ventricular Study screen.

#### Other EP Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit , EP Test Results, Brief EP Reports, and Release Control options.

#### Brief Electrophysiology Screen

> Brief Electrophysiology Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 REASON FOR STUDY:..............................

> 4 INTERPRETATION(W):..... 5 COMMENT(W):.....

> 6 CARDIOLOGY STAFF:..............................

> 7 CARDIOLOGY FELLOW:..............................

> 8 PROCEDURE SUMMARY:..............................

> Atrial Study and Ventricular Study can be edited after the Brief EP Screen. Descriptions of the fields and subscreens will be found under the corresponding Electrophysiology screen previously displayed and in the Cardiology Quick Reference Guide.

### Holter Lab Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Enter/Edit Holter (Screen)

> 2\. Holter test Results

> 3\. Line Entry/Edit of Holter

> 4\. Summary of Automated Records Transferred

> 5\. Brief Line Entry/Edit of Holter

> 6\. Brief Enter/Edit Holter (Screen)

> 7\. Brief Holter Report

> 8\. Release Control Options (Holter)

#### Enter/Edit Holter (Screen)

> Holter Procedure (Screen 1 of 4)

> HOLTER PROCEDURE (SCREEN 1 of 4) 09/16/93

> 1 DATE/TIME: .................

> 2 PATIENT: ..............................

> 3 PATIENT CATEGORY: ..........

> 4 WARD/CLINIC: ............ 15 APPOINTMENT DATE: .................

> 5 HT IN: ... 16 HOOK-UP BY: ..................

> 6 WT LBS: ... 17 RETURN DATE/TIME: .................

> 7 REQUESTED BY: ............... 18 HOLTER RUN NUMBER: .....

> 8 DATE REQUESTED: .................

> 9 REASON FOR STUDY(M): ................................

> 10 SYMPTOMS(M): ..............................

> 11 RISK FACTORS(M): ......................... 19 RECORDER NUMBER: .....

> 12 <u>HEART MEDS(M):</u> ........................ 20 BATTERY NUMBER: ...

> 13 APPROVED BY: ............... 21 MALFUNCTIONS: ...

> 14 DATE APPROVED: ................. 22 MALFUNCTION TYPE(W): .....

> 1\. Identify the specific Holter procedure by date/time.

> 2\. Indicate the patient's identification number assigned by the medical facility. In most cases it is the person's social security number.

> 3\. Define either inpatient or outpatient status.

> 4\. Identify the in-house address of the patient.

> 5-6 Enter the patient's height in inches, and weight at the time of the procedure.

> 7\. Identify the medical provider who ordered this procedure.

> 8\. Give the time/date the procedure was ordered.

> 9\. Enter the rationale for ordering this procedure.

> 10\. The symptoms and risk factors dictionaries are common to all procedures.

> 12\. An entry into the Heart Meds field leads to a subscreen.

> 13\. Identify the medical provider who approved the request for this procedure.

> 14\. The date of the actual request approval is entered here.

> 15\. The actual date of patient appointment is entered here.

> 16\. Identify the medical provider who physically initiated this procedure.

> 17\. This is the date the patient physically returns the Holter monitor.

> 18\. This is the facility generated procedure number.

> 19\. Identify the recorder used in this procedure.

> 20\. Specify the battery used in this procedure.

> 21\. Document whether any procedure malfunction occurred.

> 22\. Provide documentation or comments regarding the malfunction

> NOTE: Correct entry of all dates is important, as a check for the physician.

> Heart Meds Subscreen of Holter Procedure (Screen 1 of 4)

> HEART MEDS 09/16/93

> 1 HEART MEDS: ................. 2 DOSE: ..........

> 3 FREQUENCY: ..........

> 1\. Enter details concerning the specific medications used.

> 2\. Specify the amount of drug taken at any given time.

> 3\. Indicate the rate at which the prescribed dose is given.

> Upon completion of the subscreen the user is returned to Holter Procedure

> (Screen 1 of 4).

> Holter Procedure (Screen 2 of 4)

> HOLTER PROCEDURE (SCREEN 2 of 4) 09/16/93

> 1 SCANNED BY: .................. 11 QRS TOTAL: ......

> 2 SCANNED DATE: ................. 12 VPBS (VENT): .....

> 3 TAPE QUALITY: .......... 13 VPBS PERCENT (VENT)(C): .........

> 4 TOTAL HOURS: ... 14 AVE/HR: ....

> 5 READABLE HOURS: ... 15 MAX/HR: ....

> 6 AVERAGE HR: ... 16 ISOLATED VPBS (VENT): .....

> 7 MAX HR: ... 17 BIGEMINY (VENT):....

> 8 TIME MAX HR: ........ 18 COUPLETS (VENT): ....

> 9 MIN HR: ... 19 \# OF RUNS 3 OR MORE (VENT): .....

> 10 TIME MIN HR: ........ 20 BEATS IN RUNS (VENT): .....

> 21 BEATS LONGEST RUN (VENT): ....

> 22 BEATS FASTEST RUN (VENT): ....

> 23 BPM IN FASTEST RUN (VENT): ...

> 1\. Identify the medical provider who performed the Holter scan.

> 2\. Enter the date the scanning procedure was performed.

> 3\. Indicate the gross evaluation of the tape quality.

> 4\. Total hours refers to the total number of hours scanned.

> 5\. Document the length in hours of distortion free procedure readings.

> 6\. Indicate the average heart rate for the entire Holter session.

> 7\. Document the greatest heart rate that was monitored during this procedure.

> 8\. Specify the exact time at which maximum heart rate occurred.

> 9\. Enter the lowest heart rate that was monitored during this procedure.

> 10\. Give the time at which minimum heart rate occurred during this procedure.

> 11\. QRS refers to a wave on the EKG complex This is the total number of ventricular complexes generated (monitored) during this procedure.

> 12\. VPBS refers to ventricular premature beats.

> 13\. VPBS is calculated from \#11 and \#12.

> 14\. AVE/HR refers to the average ventricular premature beats per hour.

> 15\. Give the maximum number of ventricular ectopy monitored during any hour of this procedure.

> 16\. Enter the total number of isolated ventricular ectopy.

> 17\. Bigeminy refers to two VPBS occurring together, being followed by a normal beat.

> 18\. Couplets refers to two VPBS occurring without a normal beat following.

> 19\. Use this field for a VPBS run of three or more.

> 20\. This is the average number occurring in groups of 3 or more as monitored during this procedure.

> 21\. Document the longest streak of ventricular premature beats.

> 22\. This field refers to a run at a high heart rate.

> 23\. This field is used to enter the beats per minute in the fastest run.

> Holter Procedure (Screen 3 of 4)

> HOLTER PROCEDURE (SCREEN 3 of 4) 09/16/93

> 1 ATRIAL BEATS TOTAL: ......

> 2 ECTOPICS (ATR): ......

> 3 ECTOPICS PERCENT (ATR)(C): .........

> 4 AV/H (ATR): ...

> 5 MAX/H (ATR): ...

> 6 ISOLATED (ATR): ..... 14 PAUSES (SINUS): ...

> 7 BLOCKED APC (ATR): ..... 15 LONGEST SINUS PAUSE: ....

> 8 NUM. RUNS SVT (ATR): ... 16 PAUSES (VENT): ...

> 9 BTS IN RUNS (ATR): ... 17 LONGEST PAUSE (VENT): ....

> 10 BTS LONGEST RUN (ATR): ...

> 11 BTS FASTEST RUN (ATR): ...

> 12 BPM FASTEST RUN (ATR): ...

> 13 HEART BLOCK: ..................................

> 1\. This field is the sum of all P waves monitored during this procedure.

> 2\. Ectopic refers to abnormal atrial beats.

> 3\. Ectopics percent is automatically calculated from \#1 and \#2.

> 4\. AV/H refers to average per hour, Max/H refers to maximum per hour.

> 5\. Indicate the maximum number of atrial ectopy monitored during any hour of this procedure.

> 6\. Enter the total number of single atrial ectopy monitored during this procedure.

> 7\. Blocked APC refers to a blocked atrial premature contraction.

> 8\. Enter the number of runs for the super ventricular tachycardia.

> 9\. Give the average number of atrial ectopy occurring in groups of 3 or more as monitored during this procedure.

> 10\. This is the total number of supraventricular ectopy in the largest group monitored during this procedure.

> 11\. Indicate the fastest runs at a high heart rate.

> 12\. Enter the beats per minute at a high heart rate.

> 13\. Identify the degree of heart block monitored during this procedure.

> 14\. Indicate whether sinus pauses were monitored during this procedure.

> 15\. This is the length of the longest sinus pause monitored during this procedure in the range of .1 and 10 seconds.

> 16\. Indicate the occurrence of ventricular pauses monitored during this procedure.

> 17\. Identify the longest occurrence of ventricular pause monitored during this procedure in the range of .1 and 10 seconds.

> Holter Procedure (Screen 4 of 4)

> HOLTER PROCEDURE (SCREEN 4 of 4) 09/16/93

> 1 ST LEVEL: ......

> 2 ST LEVEL DEP/ELEV: ...........................

> 3 INTERPRETATION(W): .....

> 4 COMMENTS(W): .....

> 5 SUMMARY: ..........................

> 6 REVIEW DATE: .................

> 7 REVIEWED BY: ........................

> 8 PROCEDURE SUMMARY: ...................................

> 1\. This is the level of ST segment deviation from baseline monitored during this procedure in the range of 0 and 5 millimeters using 2 decimal digits.

> 2\. Enter the evaluation of ST segment deviation monitored during this procedure.

> 3\. Evaluate the patient's cardiac condition based on the information collected.

> 4\. Remark on the data collected in this procedure.

> 5\. Summarize the gross evaluation of the results of this procedure.

> 6\. Enter the date the review occurred.

> 7\. Identify the medical provider who reviewed this procedure.

> 8\. This field will be displayed on the Summary of Patient Procedures.

#### Other Holter Lab Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit , Holter Test Results, Brief Holter Reports, and Release Control options.

#### Automated Records Transfer

> This option prints a report of the transfer of patient records from a data storage system to the DHCP system, with a listing of patient name, patient social security number, test date, transfer date, and transfer status. The patient name and social security number in the data storage system are checked against information in the DHCP system before transfer. Unsuccessful transfers due to invalid test date, failure to match patient name or social security number, or other causes are indicated on the summary report. Entries are listed according to the attempted transfer dates within a specified time period.

#### Brief Enter/Edit Holter (Screen)

> Brief Holter Procedure Screen 09/16/93

> 1 HOOK-UP DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 REASON FOR STUDY(M):.............................................

> 4 OTHER INDICATIONS(W):..... 5 REVIEWED BY:.........................

> 6 MAX HR:.... 7 AVE/HR:.... 8 COUPLETS (VENT):....

> 9 NUM OF RUNS 3 OR MORE (VENT):.. 10 BEATS LONGEST RUN (VENT):....

> 11 BEATS FASTEST RUN (VENT):.... 12 AV/H (ATR):....

> 13 HEART BLOCK:....................................

> 14 LONGEST PAUSE (VENT):..... 15 ST LEVEL:......

> 16 ST LEVEL DEP/ELEV:........... 17 INTERPRETATION(W):.....

> 18 SUMMARY:..........................

> 19 PROCEDURE SUMMARY:............................................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding Holter screen previously displayed and in the Cardiology Quick Reference Guide.

### Exercise Tolerance Test (ETT) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Enter/Edit ETT (Screen)

> 2\. ETT Results

> 3\. Line Entry/Edit of ETT Test

> 4\. Brief Line Entry/Edit of ETT

> 5\. Brief Enter/Edit ETT (Screen)

> 6\. Brief ETT Report

> 7\. Release Control Options (ETT)

> The ETT, or Exercise Tolerance Test, screens may also be referred to as Stress Test, Treadmill Test, or Exercise Test.

#### Enter/Edit ETT (Screen)

> ETT (Screen 1 of 3)

> ETT (SCREEN 1 of 3) 09/16/93

> 1 DATE/TIME OF TEST: ................. 15 RESTING HR: ...

> 2 PATIENT: .............................. 16 RESTING SYS BP: ...

> 3 ID: .......... 17 RESTING DIAS BP: ...

> 4 WARD/CLINIC: ......................... 18 RESTING RPP(C): ........

> 5 WT LBS: .... 19 RESTING UPRIGHT HR: ...

> 6 DT/TIME OF APPT.: ................. 20 RESTING UPRIGHT SYS BP: ...

> 7 <u>HEART MEDS(M):</u> ......................... 21 RESTING UPRIGHT DIAS BP: ...

> 8 RESTING EKG(W): ..... 22 RESTING UPRIGHT RPP(C): ........

> 9 EKG TECHNICIAN: .................. 23 RESTING ST: ....

> 10 SYMPTOMS(M): ..............................

> 11 RISK FACTORS(M): ..............................

> 12 REF. MD: ................. 24 RESTING UPRIGHT ST: ....

> 13 ETT PROTOCOL: .................... 25 RESTING ST SLOPE: ....

> 14 HYPERVENT: .............................. 26 RESTING UPRIGHT ST SLOPE: ....

> 1\. Identify the precise Exercise Tolerance procedure by date and time.

> 2\. Identify the patient.

> 3\. Indicate the patient's identification number assigned by the medical facility. In most cases it is the person's social security number.

> A REASON FOR TEST field follows this field in the line edit mode. The entry is chosen from a set of codes which can be seen by typing ??.

> 4\. Enter the in-house patient location.

> 5\. This is the patient's weight in pounds at the time of this procedure.

> 6\. The actual date of the test is entered here. This serves as a comparison with the scheduling date.

> 7\. Heart Meds is a multiple field leading to a subscreen.

> 8\. This refers to a pre-exercise EKG test.

> 9\. Identify the staff member responsible for hooking up the patient.

> 10\. The symptoms field dictionary is common to all of the cardiology files, as is the risk factors dictionary.

> 11\. Select the morbidity factors which this patient is most susceptible to in regards to this procedure.

> 12\. Identify the referring physician.

> 13\. Protocol refers to the particular test administered to the patient.

> 14\. Hyperventilation refers to a period of rapid, deep breathing for a specified period. This should precede the test.

> 15-26 are pre-exercise parameters, 15-17 are supine (prone) parameters, and 19-22 are standing parameters.

> 15\. Indicate the resting/supine heart rate.

> 16\. Enter the resting/supine systolic blood pressure.

> 17\. Provide the resting/supine diastolic blood pressure.

> 18\. Resting RPP is a number based upon the resting heart rate and resting systolic pressure.

> 19\. Give the resting/upright heart rate.

> 20\. Enter the resting, upright systolic blood pressure.

> 21\. Indicate the resting/upright diastolic blood pressure.

> 22\. This field is automatically calculated based on the resting/upright heart rate and systolic pressure.

> 23\. Resting ST refers to the ST depression for the S and T waves.

> 24\. Enter the resting upright ST depression.

> 25\. Give the supine resting ST slope.

> 26\. Enter the standing resting ST slope.

> Heart Meds Subscreen of ETT (Screen 1 of 3)

> HEART MEDS 09/16/93

> 1 HEART MEDS(M): ..............................

> 2 DOSE: ..........

> 3 FREQUENCY: ..........

> 1\. This subscreen is for entering medications.

> 2\. Enter the dosage of the cardiac medicines that the patient is taking at the time of this procedure.

> 3\. Indicate the time and frequency at which the patient takes the medicine.

> Upon completion of the subscreen, the user is returned to the ETT (Screen 1 of 3).

> ETT (Screen 2 of 3)

> ETT (SCREEN 2 of 3) 09/16/93

> 1 CHEST PAIN TIME (MIN): .... 19 PK RPP(C): ........

> 2 CP TME SEC: .... 20 EX TIME MIN: ...

> 3 CP TIME TOTAL (C): ........ 21 EX TIME SEC: ....

> 4 CP MODIFIER: ............... 22 EX TIME(C): ........

> 5 ONSET CP HR: .... 23 PREDICTED HR(C): ........

> 6 ONSET CP SBP: .... 24 TIME ST - 1: .....

> 7 ONSET CP DBP: .... 25 TIME ST - 2: .....

> 8 ONSET CP ST: .... 26 % TARGET HR(C): ........

> 9 ONSET CP ST SLOPE: .... 27 REASON FOR STOPPING: ..............

> 10 ONSET CP RPP(C): ........ 28 ARRHYTHMIAS: ...................

> 11 PK HR: ... 12 PK SBP: ... 29 OTHER EKG CHANGES(W): .....

> 13 PK DBP: ... 14 PK EX MPH: ... 30 HEART RATE RESPONSE: ........

> 15 PK EX GRADE: .... 16 METS: .... 31 BLOOD PRESSURE RESP: ..................

> 17 PK ST: .... 18 PK ST SLOPE: ....32 TIME RETURN BASELINE ST: .......

> 1\. Enter the minutes portion of the time (0-20) that the patient experienced chest pain.

> 2\. Enter the seconds portion of the time (0-59) that the patient experienced chest pain (CP).

> 3\. This is the total time the patient experienced chest pain..

> 4\. Chest pain modifier refers to any pain which occurs before, during, or after the test periods and qualifies the type of chest pain that the patient experienced.

> 5\. Indicate the heart rate at the onset of chest pain.

> 6-7 Give the systolic and diastolic blood pressures at the onset of chest pain.

> 8-9 Enter the ST Depression at the onset of chest pain.

> 10\. RPP stands for rate/pressure product at the onset of chest pain.

> 11\. This maximum heart rate is for the peak exercise period.

> KILO POND METERS (KPM) and WATTS fields follow this field in the line edit mode. Identify the kilo pond meters and watts respectively.

> 12-13 Enter the peak systolic and diastolic blood pressures.

> 14\. This refers to the peak exercise mph for the treadmill.

> 15\. PK EX Grade refers to the maximum treadmill elevation.

> 16\. METS refers to maximum exercise tolerances (Metabolic Equivalents-1 MET=3.5ml of O2 resting).

> 17-18 Give the peak ST elevation and slope.

> 19\. This is the peak RPP calculated from fields 17 and 18.

> 20\. Specify the minutes portion of the elapsed time that exercise occurred.

> 21\. Enter the seconds portion of the elapsed time that exercise occurred.

> 22\. This field shows the total time in seconds calculated from fields 20 and 21.

> 23\. The predicted heart rate calculation is based upon the patient age.

> 24\. This ST time refers to the total time of ST depression at the maximum percentage of the predicted heart rate.

> 25\. This ST time refers to the total time of the ST slope.

> 26\. The percentage of target heart rate achieved is automatically calculated.

> 27\. Enter the rationale for terminating the procedure.

> 28\. Document the cardiac rhythm irregularity. Arrhythmias entered here may have occurred before, during, or after the test.

> 29\. Identify any irregularities.

> 30\. Enter the heart rate response.

> 31\. Systolic roll-over refers to a drop in the systolic blood pressure from the previous stage.

> 32\. This is the total time that the ST segment returned to the baseline rate.

> ETT (Screen 3 of 3)

> ETT (SCREEN 3 of 3) 09/16/93

> 1 INTERPRETATION: ..........

> 2 COMMENTS(W): .....

> 3 ATTN PHYS: ..................

> 4 COMPLICATIONS(M): ........................................

> 5 SUMMARY: ..........................

> 6 PROCEDURE SUMMARY: .....................................

> 1\. Interpretation is entered by code: "N" for normal; "A" for abnormal; and "B" for borderline.

> 2\. This comment is a word-processing field.

> 3\. Identify the patient's attending physician.

> 4\. Indicate any complications in this field.

> 5\. This field identifies the result of the ETT procedure.

> 6\. Answer must be 1-79 characters in length. This will appear on the "Summary of Patient

> Procedures."

#### Other ETT Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Cardiology for information about Line Enter/Edit , ETT Test Results, Brief ETT Reports, and Release Control options.

#### Brief Enter/Edit ETT (Screen)

> Brief Exercise Tolerance Test Screen 09/16/93

> 1 DATE/TIME OF TEST:.................

> 2 MEDICAL PATIENT:....

> 3 REASON FOR TEST:........................................

> 4 ETT PROTOCOL:.................... 5 PK HR:.... 6 PK EX MPH:....

> 7 PK EX GRADE:..... 8 METS:..... 9 PK ST:.... 10 EX TIME MIN:....

> 11 EX TIME SEC:.....

> 12 REASON FOR STOPPING:................................................

> 13 ARRHYTHMIAS:...................

> 14 BLOOD PRESSURE RESPONSE:..................

> 15 SUMMARY:..........................

> 16 PROCEDURE SUMMARY:................................................

> 17 EKG TECHNICIAN:.................. 18 ATTN PHYS:..................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Exercise Tolerance Test screen previously displayed and in the Cardiology Quick Reference Guide.

Surgical Risk Analysis

### Surgical Risk Analysis Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgical Risk Analysis menu has the following options:

> 1\. Pre-Surgery Risk Analysis Enter/Edit

> 2\. Post-Surgery Risk Analysis Enter/Edit

> 3\. Pre-Surgery Risk Analysis Enter/Edit(Screen)

> 4\. Post-Surgery Risk Analysis Enter/Edit(Screen)

> 5\. Surgical Risk Analysis Report

> The options for Pre-Surgery and Post-Surgery Risk Analysis are available in VA FileMan entry using Options 1 and 2. The data entry elements are identical for VA FileMan and screen entry.

#### Pre-Surgery Risk Analysis Enter/Edit (Screen)

> Using Option 3: Pre-Surgery Risk Analysis (Screen), the following screens appear.

> VA Cardiac Surgical Risk Assessment Program (Screen 1)

> VA CARDIAC SURGICAL RISK ASSESSMENT PROGRAM 09/16/93

> 1 DATE OF PHYSICIAN'S ESTIMATE:.................

> 2 PATIENT:..............................

> 3 HOSPITAL OF SURGERY:..............................

> 4 AGE:....

> 1\. Indicate the date of completion of physician's estimate of operative mortality.

> 2\. Identify the patient's name.

> 3\. Specify the hospital where surgery is to be performed.

> 4\. Enter the patient's age, between 15 and 99.

> II\. Clinical Data (Screen 2)

> II\. CLINICAL DATA 09/16/93

> 5 PTCA:........... 6 PRIOR MI:.................

> 7 PRIOR HEART SURGERY:.... 8 COPD:....

> 9 PERIPHERAL VASCULAR DISEASE:.. 10 CARDIOMEGALY BY CHEST X-RAY:....

> 11 NYHA FUNCTIONAL CLASS:.......................................

> 12 PULMONARY RALES:.... 13 CURRENT DIURETIC USE:....

> 14 CURRENT SMOKER:.... 15 CURRENT DIGITALIS USE:....

> 16 SERUM CREATININE (MG/DL):..... 17 I.V. NTG PREOPERATIVELY:....

> 18 UNSTABLE ANGINA:.... 19 PREOPERATIVE IABP:....

> 5\. This refers to percutaneous transluminal coronary artery angioplasty.

> 6\. Enter 1 for Did not occur, 2 for occurred within one week prior to surgery, 3 for occurred more than one week prior to surgery if two of the following occurred:

> a\) Typical Pain, b) Enzyme Rise and Fall, and c) New Q-waves on the electrocardiogram.

> 7\. "Yes" indicates any form of prior heart surgery performed through a thoracotomy during separate, preceding hospitalization.

> 8\. A "Yes" indicates chronic obstructive pulmonary disease resulting in functional disability, and/or hospitalization, and/or requiring bronchodilator therapy, and/or FEV1\>75% of predicted.

> 9\. "Yes" indicates obstruction of arteries to legs resulting in symptoms, and/or surgery, and/or angiographically demonstrated stenosis ≥ 50%.

> 10\. "Yes" indicates overall cardiac enlargement, and/or cardiothoracic ration ≥ 0.5 on chest x-ray within the 30 days preceding surgery.

> 11\. The following functional classes are defined :

> I - heart disease with no symptoms limiting activity

> II - slight limitation of physical activity by fatigue, dyspnea, or angina

> III - marked limitation of physical activity by fatigue, dyspnea, or angina, but no symptoms at rest

> IV - symptoms at rest and/or inability to carry out any physical activity without symptoms of dyspnea, fatigue, or angina

> 12\. "Yes" indicates rales heard at lung base(s) not clearing with cough and not due to pneumonic process within 2 weeks of surgery.

> 13\. "Yes" indicates use of any diuretic agent within 2 weeks preceding surgery.

> 14\. "Yes" indicates the patient is a current smoker.

> 15\. "Yes" indicates use of any digitalis preparation (Digoxin, Lanoxin, Digitoxin, etc.) within 2 weeks preceding surgery.

> 16\. The entry will be a number between 0 and 20, 1 decimal digit.

> 17\. "Yes" indicates I.V. Nitroglycerine given within 48 hours prior to surgery.

> 18\. "Yes" indicates angina occurring at rest or prolonged angina unresponsive to nitroglycerine.

> 19\. "Yes" indicates intra-aortic balloon pump (IABP) in use at some time during the 48 hours preceding surgery.

> III\. Cardiac Catheterization and Angiographic Data (Screen 3)

> III\. CARDIAC CATHETERIZATION AND ANGIOGRAPHIC DATA 09/16/93

> 20 LV END-DIASTOLIC PRESSURE:....

> 21 AORTIC SYSTOLIC PRESSURE:....

> 22 PA SYSTOLIC PRESSURE (MM HG):....

> 23 MEAN PA WEDGE PRESSURE (MM HG):....

> 24 LEFT MAIN CORONARY STENOSIS:....

> 25 NUMBER OF MAJOR CORONARIES:....

> 20\. LV End-Diastolic Pressure requires a value between 0 and 99, 0 decimal digits.

> 21\. Aortic Systolic Pressure requires a value between 0 and 300, 0 decimal digits.

> 22\. PA Systolic Pressure (MM HG) is a value between 0 and 150, 0 decimal digits.

> 23\. Mean PA Wedge Pressure (MM HG) requires a value between 0 and 99.

> The LV CONTRACTION SCORE field follows this field in the line enter/edit mode. It identifies the

> LV Contraction score.

> CHOOSE FROM:

> 1 I \> 0.54 Normal

> 2 II 0.45-0.54 Mild dysfunction

> 3 III 0.35-0.44 Moderate dysfunction

> 4 IV 0.25-0.34 Severe dysfunction

> 5 V \<0.25 Very severe dysfunction

> 0 ? unknown No LV study

> 24\. For Left Main Coronary Stenosis, give % reduction in luminal diameter of most severe stenosis (0-100).

> 25\. Number of major coronary arteries (LAD), right with PDA.

> Choose from 0-3

> IV\. Operative Risk Summary Data (Screen 4)

> IV\. OPERATIVE RISK SUMMARY DATA 09/16/93

> 26 PHYSICIAN'S ESTIMATE:........

> 27 GENERAL MEDICAL CONDITION:....

> 28 PRIORITY OF SURGERY:........

> 29 INTENDED OPERATIVE PROCEDURE:.................

> 26\. Type a Number between 0 and 100, 2 decimal digits indicating the physician's estimate of the patient's survival rate.

> 27\. General Medical Condition is a grade according to general nutrition, concomitant non- cardiac diseases, mental status, debility, etc. (0-2) for good, fair, and poor.

> 28\. Priority of Surgery has three choices. “Elective” indicates no alteration in surgical schedule, “Urgent” indicates surgery must be performed within 24-72 hrs, “Emergent” indicates surgery must be performed within 24 hours of diagnosis.

> 29\. Choose the intended operative procedure. The mortality for the patient is then estimated

> (i.e., The estimated mortality for VIRGINIA,JOHN Q. is 9.4%.) and printed at the completion of Post Surgical Risk Analysis Enter/Edit options.

> NOTE: This field is only available when entering a NEW Surgical Risk Analysis. It cannot be edited at a later time.

> This completes the Pre-Surgery Risk Analysis screens. The Post Surgery Risk Analysis screens and fields are numbered as a continuation of the Pre-Surgery Risk Analysis screens.

#### Post-Surgery Risk Analysis (Screen)

> V. Operative Data ( Screen 5, Part 1 of Post SRA)

> V. OPERATIVE DATA 09/16/93

> 30 VALVE REPAIR:.... 31 BYPASS GRAFTS WITH VEIN:....

> 32 BYPASS GRAFTS WITH ARTERY:.... 33 LV ANEURYSECTOMY OR PLICATION:...

> 34 GREAT VESSEL REPAIR W BYPASS:.... 35 AORTIC VALVE REPLACEMENT:....

> 36 MITRAL VALVE REPLACEMENT:.... 37 CARDIAC TRANSPLANT:....

> 38 TRICUSPID VALVE REPLACEMENT:.... 39 ELECTROPHYSIOLOGIC PROCEDURE:....

> 40 OTHER PROCEDURE(S)(M):..............................

> 30\. "Yes" indicates whether repair of any cardiac valve was performed with cardiopulmonary bypass with or without additional procedures.

> 31\. Enter the number of distal anastomoses constructed with vein grafts (0-9).

> 32\. Indicate the number of distal anastomoses constructed with an internal mammary artery (0-

> 4).

> 33\. "Yes" indicates resection or plication of left ventricular aneurysm with or without additional procedures.

> 34\. "Yes" indicates primary procedure was repair of aorta or other great vessels requiring left heart bypass with or without aortic valve replacement or CABG.

> 35\. "Yes" indicates aortic repair was performed with or without additional procedures.

> 36\. "Yes" indicates mitral valve replacement was performed with or without additional procedures.

> 37\. "Yes" indicates orthotopic or heterotopic transplant. Heart-lung transplant should be listed under "Other".

> 38\. "Yes" indicates tricuspid valve replacement was performed with cardiopulmonary bypass with or without additional procedures.

> 39\. Identify the electrophysiologic procedure.

> 40\. Enter any other procedures performed.

> V. Operative Data - B & C (Screen 5, Part 2 of Post SRA)

> V. OPERATIVE DATA - B. & C. 09/16/93

> 41 OPERATIVE DEATH:....

> 42 DATE OF OPERATIVE DEATH:.................

> 43 PERIOPERATIVE MYOCAR. INFARC.:.... 44 REOPERATION FOR BLEEDING:....

> 45 ENDOCARDITIS:.... 46 ON VENTILATOR (48 HRS OR MORE):....

> 47 RENAL FAILURE:.... 48 REPEAT CARDIOPULMONARY BYPASS:....

> 49 LOW CARDIAC OUTPUT:.... 50 COMA (24 HRS OR MORE):....

> 51 MEDIASTINITIS:.... 52 STROKE:....

> 41\. "Yes" indicates death from any cause within 30 days of surgery in or out of the hospital, or after 30 days if a direct result of a surgical complication.

> 42\. Enter the date of operative death.

> 43\. "Yes" indicates appearance of new or significantly widened Q-waves on postoperative electrocardiogram.

> 44\. "Yes" if any re-exploration of thorax for excessive bleeding during postoperative hospitalization.

> 45\. "Yes" indicates new onset of endocarditis diagnosed within the 30 days following surgery.

> 46\. For On Ventilator (48 hrs or more), "YES" indicates total duration of ventilator-assisted respiration during postoperative hospitalization if it was ≥ 48 hours.

> 47\. "Yes" indicates development or exacerbation of renal failure requiring initiation of dialysis during the postoperative hospitalization.

> 48\. "Yes" indicates any surgical procedure requiring cardiopulmonary bypass during post- operative hospitalization or within 30 days of initial operation.

> 49\. "Yes" indicates cardiac index \< 2.0 L/min/M2 for ≥ 6 hours postoperative or evidence of poor

> peripheral perfusion (e.g., IABP or sustained use of positive inotropic agents).

> 50\. "Yes" indicates significantly impaired level of consciousness (exclude transient disorientation or psychosis) for ≥ 48 hours during postoperative hospitalization.

> 51\. "Yes" indicates any infection below sternum during postoperative hospitalization or appearing within the 30 days following surgery.

> 52\. "Yes" indicates objective neurologic deficit lasting30 minutes

> with onset intra- or post-operatively.

#### Surgical Risk Analysis Report

> The Surgical Risk Analysis Report is compiled from the information entered for the pre-surgery and post-surgery menu options. The report is generated for a given patient.

> CARDIAC SURGERY RISK ASSESSMENT Pg 1

> PATIENT NAME: MEDPATIENT, ONE HOSPITAL: 688

> SSN: 000-23-4567 DATE OF SURGERY: 12/07/93

> II\. CLINICAL DATA

> PTCA: none recent

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 36%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Sex</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
<td><blockquote>
<p>Prior MI: &gt; 7 days of surg.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Age</p>
</blockquote></td>
<td><blockquote>
<p>69</p>
</blockquote></td>
<td><blockquote>
<p>Prior heart surgery</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COPD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>Peripheral vascular disease</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cardiomegaly(x-ray)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NYHA functional class</p>
</blockquote></td>
<td><blockquote>
<p>SYMPTOMS ON MORE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>THAN ORDINARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ACTIVITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pulmonary rales</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>Current diuretic use</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Current smoker</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>Current digoxin use</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Creatinine</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>IV NTG within 48 hr of surger</p>
</blockquote></td>
<td>y NO</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rest Angina</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>Preoperative use of IABP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> III\. CARDIAC CATHETERIZATION AND ANGIOGRAPHIC DATA

> LVEDP 13 mm Hg Lv Contraction Score (from contrast or

> Aortic systolic pressure 140 mm Hg radionuclide angiogram or 2D echo)

> \*PA systolic pressure mm Hg

> \*PAW mean pressure mm Hg Grade Ejection Fraction Definition

> \*patients having right heart cath Range

> I \> 0.54 Normal

> Percent left main stenosis 0% Number of other major coronary

> arteries (LAD, right with PDA, circumflex with marginals)

> with stenosis(es) =\> 50% 3

> IV\. OPERATIVE RISK SUMMARY DATA

> Physician's preoperative General medical condition: FAIR

> estimate of operative Surgical priority: ELECTIVE

> mortality 6.9%

> Intended procedure: Mitral Valve Replacement-with or without CABG

> CARDIAC SURGERY RISK ASSESSMENT Pg 3

> PATIENT NAME: MEDPATIENT, ONE HOSPITAL: 688

> SSN: 000-23-4567 DATE OF SURGERY: 12/07/93

> V. OPERATIVE DATA A.Procedure(s)

> Tricuspid valve replacement YES Electrophysiologic procedure YES Other(not checked above)

> ENDOCARDIAL RESECTION

> VENTRICULAR SEPTAL DEFECT REPAIR

> B.Operative Death NO Date of death

> C.Perioperative (30 day) Complications

> Perioperative MI NO Reoperation for bleeding NO Endocarditis NO On ventilator \> 48 hr NO

> Renal failure requiring dialysis NO repeat cardiopulmonary bypass NO Low cardiac output \> 6 hr NO Coma =\> 24 hr NO Mediastinitis NO Stroke NO

> This page is intentionally left blank.

## GASTROINTESTINAL MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

Choose the GI Menu option from the main Medicine menu.

Upon entering the GI Module, the user is normally presented with the following menu.

> 1 Endoscopic Procedure Menu

> 2 Non-Endoscopic Procedures

> 3 Summary of Patient Procedures

> 4 Problem Oriented Consult Menu

> 5 GI Management Menu

### Documentation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options that are common to all procedure menus in the Gastrointestinal module are documented in this section rather than being repeated for each procedure.

#### Line Enter/Edit options

> These options access the same fields (unless otherwise noted) as the Enter/Edit (Screen) options. Field, field order, and entry descriptions are the same. Only the Enter/Edit (Screen) options are shown.

#### Reports

> The Reports option found on each procedure menu prints the report of the particular procedure done. The user is asked to enter the date and time of the procedure and the device on which to print. The report contains the information that was entered using the Enter/Edit (Screen or Line) option.

#### Brief Enter/Edit

> These options access the same fields (unless otherwise noted) as the Brief Enter/Edit

> (Screen) options. Only the Brief Enter/Edit (Screen) options are shown. The field descriptions for the brief screens are the same as for the corresponding field on the full screens and are

> not reshown.

#### Brief Report

> The Brief Reports print a report of the information that was entered using the Brief Enter/Edit options. The user is asked to enter the date and time of the procedure and the device on which to print

#### Release Control

> The Release Control Options menu is found under the GI Management Menu. Use of these options is usually restricted by security keys given to clinical managers. A full description of the options can be found in the Orientation and the Package Management sections of this manual under Release Control.

### Endoscopic Procedure Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Endoscopic Procedure Menu has the following menu options.

> 1 Enter/Edit GI Procedure (Line)

> 2 Procedure Enter/Edit (Screen)

> 3 Endoscopic Report

> 4 Diagnosis Review/Revision

> 5 Recall List

> 6 Image Capture

> 7 Brief Enter/Edit GI Procedure

> 8 Brief Procedure Enter/Edit (Screen)

> 9 Brief Endoscopic Report

#### Enter/Edit GI Procedure - Procedure Enter/Edit

> The Enter/Edit GI Procedure option uses standard FileMan procedures to enter data. The Procedure Enter/Edit option is a screen entry function for the procedures in the Enter/Edit GI Procedures option. The information entered is identical.

> Different prompts will appear depending on the procedure chosen (i.e. Esophagogastroduodenoscopy (EGD), Endoscopic Retrograde Cholangiogram and Pancreatogram (ERC), Laparoscopy (LAP), Colonoscopy (COL)) and the answers to certain questions.

> The screens for the Procedure Enter/Edit option are used to illustrate procedure entry. To illustrate the screens, a LAP procedure has been selected.

> Prior to the display of the first screen, the appointment date/time and patient name and procedure are entered. The procedure entered here will determine the choices of fields to be edited in the following screens. Fields that are not appropriate to the procedure are seen on the screen but show a line of asterisks after the field name and do not allow editing. If the procedure chosen is LAP, the Preparation Diet field on screen 3 of 4 will appear as:

> 1\. PREPARATION DIET:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> If the procedure chosen is Colonoscopy, the same field appears as:

> 1\. PREPARATION DIET:................

> Response choices on fields designated as multiples are also determined by the procedure chosen (i.e., the Location Evaluated field presents different choices for LAP and Colonoscopy).

> After entering the procedure, an opportunity is provided for editing personal history information on the patient. Patient information concerning whether the patient has had a liver biopsy, heart disease, glaucoma, or allergies appears in this section. Any information entered here may be edited.

#### Updating Personal History Information

2 Procedure Enter/Edit (SCREEN)

Enter Date/Time of Procedure:

ARE YOU ADDING ..(date and time)..... AS A NEW ENDOSCOPY/CONSULT? Y (YES) ENDOSCOPY/CONSULT MEDICAL PATIENT: MEDPATIENT, ONE 09-15-39 000111111

> MILITARY RETIREE

> ENDOSCOPY/CONSULT PROCEDURE: LAP LAPARASCOPY ENDOSCOPY

> PERSONAL HISTORY INFORMATION

> MEDPATIENT, ONE SSN: 000-45-6789

History of Bleeding Disorder: Valvular Heart Disease:

Glaucoma:

History Comments:

Allergies/Adverse Reactions:

ASPIRIN

> Do you wish to edit the Personal History Information? NO// YES

#### GI Demographic Screen

> GI DEMOGRAPHIC DATA 02/03/94

> 1 NAME(R):

> 2 LIVER BIOPSY:....

> 3 VALVULAR HEART DISEASE:....

> 4 HISTORY OF BLEEDING DISORDER:....

> 5 GLAUCOMA:....

> 6 HISTORY COMMENTS:..................................................

> Enter Y(es) or N(o) to each condition. If only changes to the allergy information are needed, answer these questions with \<RET\>.

> Upon completion of the screen, one of the following messages will appear depending on whether or not the patient has allergies reported.

> This patient has no allergy/adverse reaction data.

> or

OBS/

> ADVERSE REACTION VERIFIED ALLER HIST

> ---------------- -------- ----- ---- FOOD/OTHER:

> ASPIRIN NO YES OBS Reactions: HIVES

#### Entering Allergies

> Enter Allergen:

> You may enter a new allergen or edit a previously entered one.

> (O)bserved or (H)istorical Allergy/Adverse Reaction:

> COMMENTS ON OBSERVED DATA:

Edit? NO//

> A comment regarding the nature of the allergy may be added. To edit an existing comment, enter

> "YES".

> Enter 'YES' if you wish to go into the editor.

> Enter 'NO' if you do not wish to edit at this time.

> Edit? NO//

> Select DATE/TIME CHART MARKED:

> The date must be in the past, and time is a required response.\_

> Select DATE/TIME ID BAND MARKED:

> Press return to continue, ^ to exit: \<RET\>

> A report similar to the following appears.

> PATIENT: MEDPATIENT, ONE ALLERGY/ADR: ASPIRIN

> ORIGINATOR: MEDUSER, TWO ORIGINATED: FEB 2, 1994@15:54

SIGN OFF: NO OBS/HIST: OBSERVED

OBSERVER: OBSERVED:

> MD NOTIFIED: CHART MARKED: FEB 1, 1994@18:53

> ID BAND MARKED:

COMMENTS:

SEVERITY:

> Would you like to sign off on this allergy/adverse reaction?

ADVERSE REACTION VERIFIED ALLER HIST

---------------- -------- ---- ----

> FOOD/OTHER:

> ASPIRIN NO YES OBS

> Reactions: HIVES

> Enter Allergen:

> A new allergen may be entered or existing allergens may be edited.

> Select Service/Specialty: ALL SERVICES//

> \*\*\*\*\*\*\*\*\*\*\*\* ALL SERVICES (Laparascopy) Requests for MEDPATIENT, ONE \*\*\*\*\*\*\*\*\*\*\*\*

> MEDPATIENT, ONE 000-45-6789 JUN 13,1945 (40)

> No consult/request orders found!

> \* END \*

> Select Action: QUIT

At the completion of editing the demographic data or allergies, the GI Procedure Enter/Edit

screen is automatically accessed.

#### Procedure Enter/Edit for GI Endoscopy

> Endoscopy (Screen 1 of 4)

ENDOSCOPY (SCREEN 1 of 4) 09/16/93

> 1 APPOINTMENT DATE/TIME:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 INDICATED THERAPY(M):..............................

> 4 SIGNS AND SYMPTOMS(M):..............................

> 5 DISEASE FOLLOWUP(M):..............................

> 6 FOLLOWUP DEVICE OR THERAPY (M):..............................

> 7 SURVEILLANCE(M):..............................

> 8 PROTOCOL:..................................................

> 9 EGD SIMPLE PRIMARY EXAM:...................................

> 10 LAB OR XRAY:..................................................

> 11 OCCULT BLOOD:..................................................

> 12 SPECIMEN COLLECTION:..................................................

> 13 INDICATION COMMENT:...........................................

> At least one of the indication fields (4-12) must have data entered in it in order to proceed.

> 1\. This is the date/time of the Endoscopy procedure.

> 2\. Identifies the name of the patient undergoing the procedure.

> 3\. Record the procedures which you believe you may perform at the time of the

> examination. This indicates the reason the procedure is to be performed. This field

> is called "INDICATION FOR PROCEDURE" in line edit mode. It is followed by a

> free text field called "INDICATION COMMENT" in the line edit mode.

> 4\. Establish the specific correlation between the symptoms and the Endoscopic findings.

> 5\. This field refers to the patient who is undergoing repeat procedure for the same

> (active) disease, such as follow-up on gastric ulcer healing. Used as an indication

> for procedure.

> 6\. Indicate the type of device or therapy, previously performed, which needs follow-up.

> Used as an indication for procedure.

> 7\. Identify the asymptomatic patient who is being re-examined because of old disease,

> such as prior colonic polyps. Used as an indication for procedure for GI Endoscopies.

> 8\. Specify whether this is a mandated endoscopy according to a pre-approved schedule.

> The name or number of the protocol should be entered here. Used as a GI Endoscopy indication for procedure.

> 9\. Explain whether a PDGE (Primary Diagnostic Gastrointestinal Endoscopy) was

> performed in place of an initial screening X-ray, for diagnostic purposes in an

> outpatient setting.

> 10\. Confirm if there is an abnormal X-ray or lab test suggesting the Endoscopy. Used as

> an indication for procedure for GI Endoscopies.

> 11\. Show whether occult blood is present in the stool. Used for GI Endoscopies.

> 12\. Substantiate that the procedure is performed to collect tissue or body fluid to

> perform other tests. Used as an indication for procedure for GI Endoscopies.

> 13\. Summarize the specific indications for procedure.

> Endoscopy (Screen 2 of 4)

> ENDOSCOPY (SCREEN 2 of 4) 09/16/93

> 1 INSTRUMENT(M):..............................

> 2 MEDICATION USED(M):..............................

> 3 ENDOSCOPIST:..............................

> 4 FELLOW:..............................

> 5 SECOND FELLOW:..............................

> 6 WHERE PERFORMED:..............................

> 7 WARD/CLINIC:..............................

> 8 TIME STARTED:....

> 9 TIME COMPLETED:....

> 10 URGENCY OF PROCEDURE:.........

> 1\. Indicate the Endoscopic instrument used for the procedure.

> 2\. Specify the type of medication administered for the procedure. Also record the dosage of the medication and the route of administration.

> 3\. Identify the provider who performed the procedure.

> 4\. Enter the name of a fellow who assisted on the procedure.

> 5\. Enter the name of a second fellow who assisted on the procedure.

> 6\. Give the hospital location where the procedure was performed.

> 7\. Indicate the in-house location of the patient.

> 8\. This field identifies the time the procedure was begun in 24 hour time, without punctuation. (Ex: 0800, 1630, etc.)

> 9\. This field identifies the time the procedure was completed in 24 hour time, without punctuation (Ex: 0800,1630, etc.)

> 10\. Specify whether the procedure was elective, urgent, or emergency.

> Medication Subscreen of GI Procedure (Screen 2 of 4)

MEDICATION 09/16/93

> 1 MEDICATION USED:..............................

> 2 DRUG DOSE ROUTE:.............

> 3 TOTAL DOSE (in mg.):.........

> 1\. Enter the specific medication used.

> 2\. A set of codes is used to record the route of administration for GI Endoscopies.

> 3\. Enter the total dosage in mg.

> This screen returns the user to GI Procedure Enter/Edit (Screen 2 of 4).

> GI Procedure Enter/Edit (Screen 3 of 4)

> GI ENDOSCOPY (SCREEN 3 of 4) 09/16/93

> 1 PREPARATION DIET:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 2 DIET COMMENT:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 3 BOWEL PREPARATION(M):\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 4 ENEMAS:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 5 PNEUMOPERITONEUM GAS(M):\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 6 SUMMARY:.............................

> 7 LOCATION EVALUATED(M):..............................

> 8 COMMON BILE DUCT SIZE (mm):.....

> 9 PANCREATIC DUCT SIZE (mm):....

> 10 DEPTH OF INSERTION:..............................

> 11 RESULTS(M):........................................

> 12 POST-PROC INSTRUMENT CLEANSING:.........

> 13 COMPLICATIONS(M):..............................

> Many of the fields on this screen will allow editing only if the field is appropriate to the procedure chosen.

> 1\. Preparation diet refers to oral intake (separate from the mechanical

> preparation of the colon listed under "Bowel Preparation" below). General categories

> of diet are selected from a set of codes and specifics of the diet itself are entered in the

> "Comment" field.

> 2\. Indicate the oral intake given for the preparation for a Colonoscopy.

> 3\. Record the laxative preparations given for a colonoscopy and the route by which it

> was given.

> 4\. Bowel preparation leads to a subscreen for entering the type of laxative

> preparations used for the procedure.

> 5\. Enter the type of pneumoperitoneum gas used and the method of pressure control for laparoscopy procedures.

> 6\. Specify whether the Endoscopy was Normal, Abnormal or Incomplete. This required

> field appears on the Summary of Patient Procedures.

> 7\. Location evaluated leads to two subscreens for entering details. In the line edit

> mode, this field is followed by a RESULTS field which identifies the results of the

> overall procedure.

> 8\. Give the size in millimeters of the common bile duct. Used for the ERCP Procedure.

> 9\. Enter the size in millimeters of the pancreatic duct. Used for ERCP

> procedures.

> 10\. This field indicates the extent of examination. This is a pointer to the Anatomy file.

> 11\. Record the results of the overall procedure. This field is labeled "Findings" for

> Pulmonary Endoscopies.

> 12\. Describe how the instruments were cleaned following the procedure. This is used for epidemiologic purposes.

> 13\. Indicate any complications encountered during the procedure or resulting from the procedure, and the result of the complication.

> Bowel Preparation Subscreen of GI Procedure Enter/Edit

> (Screen 3 of 4)

BOWEL PREPARATION 09/16/93

> 1 BOWEL PREPARATION:.................

> 2 ROUTE:......

1\. Indicate the type of laxative preparations used for the procedure.

2\. Enter the route (oral or rectal) by which the preparation was administered.

Pneumoperitoneum Gas

PNEUMOPERITONEUM GAS 09/16/93

> 1 PNEUMOPERITONEUM GAS:.....

> 2 PRESSURE CONTROL:.........

> 1\. Identify the type of Pneumoperitoneum Gas (Air,CO2,NO2, Other) used.

> 2\. Tell whether the pressure was controlled manually or automatically.

> Location Evaluated Subscreen 1 of GI Procedure Enter/Edit (Screen 3 of 4)

> LOCATION EVALUATED (SCREEN 1 OF 2)09/16/93

> 1 LOCATION EVALUATED:..............................

> 2 GROSS:....................

> 3 MODIFIER(M):..............................

> 4 MEASUREMENT:...............

> 5 TECHNIQUE(M):..............................

> 1\. Identify the anatomical location that was evaluated. Choices presented will be appropriate to the procedure chosen.

> 2\. Gross refers to an identifying descriptor of the finding of the anatomical location.

> Entering “?” provides a list to choose from.

> 3\. Modifier allows specific modifiers for the gross descriptor.

> 4\. This field identifies the size of the Gross finding (Ex: 4 cm; 4x3 cm; 4 cm high, etc.)

> 5\. Technique is a multiple field that identifies the specific technique used to evaluate the location. Upon completion of this field, a second Location Evaluated subscreen will appear.

> Location Evaluated Subscreen 2 of GI Procedure Enter/Edit (Screen 3 of 4)

LOCATION EVALUATED (SCREEN 2 OF 2) 09/16/93

> 1 STENT TYPE:....................... 2 STENT SIZE (FR):....

> 3 STENT LENGTH (mm):....

> 4 SPHINCTEROTOME USED:..............................

> 5 INCISION SIZE:.......

> 6 SAVARY BOUGIE DIAMETER:...............

> 7 HEATER PROBE: DURATION:....................

> 8 HEATER PROBE: POWER:...............

> 9 GASTROSTOMY TUBE USED:..............................

> 10 JEJUNOSTOMY TUBE INSERTED:..............................

> 11 IMPRESSION:.............................................

> 1\. This field identifies the type of stent used if "Insertion of Stent" is entered as a technique. Used for GI Endoscopies.

> 2\. Indicate the size (FR) of stent used if "Insertion of Stent" is entered as a technique. Used for GI Endoscopies.

> 3\. Enter the length of the stent used in millimeters if "Insertion of

> Stent" is entered as a technique. Used for GI Endoscopies.

> 4\. Identify the type of sphincterotome used if "Sphincterotomy" is entered as a technique. Used for GI Endoscopies.

> 5\. Enter the length of the incision made if "Sphincterotomy" is entered as a technique. Used for GI Endoscopies.

> 6\. Indicate the diameter of the savary bougie used if "Dilation By

> Savary Bougie" is entered as a technique. Used for GI procedures.

> 7\. Enter the length of time a heater probe is used if "Heater

> Probe Coagulation" is entered as a technique. Used for GI procedures.

> 8\. Indicate the power of the heater probe used if "Heater Probe

> Coagulation" is entered as a technique. Used for GI procedures.

> 9\. Identify the specific tube used if "Gastrostomy Tube Inserted" is entered as a technique. Used for GI procedures.

> 10\. Identify the specific tube used if "Jejunostomy Tube Inserted" is entered as a technique. Used for GI procedures.

> 11\. Enter findings for the location evaluated. The list of possible diagnoses is built from the entries in this field. If nothing is entered here, the only field that will appear for Diagnosis Entry will be Diagnosis/Diagnosis Supplement.

> Immediately after completion of Location Evaluated data, the screen returns to GI Procedure

> Enter/Edit Screen 3 of 4.

> Complications Subscreen of GI Procedure Enter/Edit (Screen 3 of 4)

COMPLICATIONS 09/16/93

> 1 COMPLICATIONS:...........................

> 2 COMP. RESULTS:...........................

> 1\. Identify any complications encountered during or resulting from the procedure.

> 2\. Indicate the result of the complication, ranging from "Required no therapy" to

"Resulting in death."

> GI Procedure Enter/Edit (Screen 4 of 4)

> GI ENDOSCOPY (SCREEN 4 of 4) 09/16/93

> 1 DISPOSITION(M):..............................

> 2 PRESCRIPTION GIVEN(M):..............................

> 3 INSTRUCTIONS TO PATIENT(W):.....

> 4 PROCEDURE SUMMARY:..........................................

> 1\. This field stores post-encounter dispositions modified by a date and a free text reason. An entry at the "Select Disposition" prompt leads to a subscreen. An entry of "Endoscopy Followup" will place this patient on the Recall List.

> 2\. This field stores the drug(s) and dosage(s) given as a post- encounter prescription.

> 3\. Describe the post-procedural instructions given to the patient.

> 4\. This field is for a free text summary of the Endoscopy (up to 79

> characters). This required field appears on the Summary of Patient Procedures.

> Disposition Subscreen of GI Procedure Enter/Edit (Screen 4 of 4)

DISPOSITION 09/16/93

> 1 DISPOSITION:........................

> 2 FINAL DISPOSITION DATE:.................

> 3 REASON:.........................................

> 1\. Enter the post-encounter disposition.

> 2\. Indicate the date of the disposition. This date may be in the

> future as in the case of Endoscopy Follow-Up entered as the disposition.

> 3\. Enter the reason for the disposition given.

> Prescription Subscreen of GI Procedure Enter/Edit (Screen 4 of 4)

PRESCRIPTION GIVEN 09/16/93

> 1 PRESCRIPTION GIVEN:.......................

> 2 DOSAGE:..............................

> 1\. Indicate the name of the formulary drug given as a post-encounter prescription.

> 2\. Specify the dosage of the prescribed drug.

#### Diagnosis Entry

> Immediately following the prompt, "Procedure Summary" on the GI Endoscopy (Screen 4 of

> 4), the Diagnosis generator is prompted.

> 1\. Primary Diagnosis: If entries have been made in the Location Evaluated field on Screen 2 and in the Impression field of the Location Evaluated subscreen, a list of possible diagnoses is generated from those impressions. The user is prompted to enter a primary diagnosis from the list. Once a user enters a diagnosis in this field, it CANNOT be changed or deleted. If an entry is made in this field a free text "Primary Diagnosis Impression" prompt is accessed.

> If no entries were made in the Impressions subfield of the Location Evaluated subscreen, the only Diagnosis Entry prompt that will appear is "Diagnosis/ Diagnosis Supplement"

> 2\. Secondary Diagnosis: The user is then shown the list of possible secondary diagnoses.

> This list is the original diagnosis list minus the diagnosis entered as the primary diagnosis. The user can enter "all" to enter the entire list as secondary diagnoses, or select a diagnosis from the list. Once a diagnosis from the list is entered as a secondary diagnosis, this diagnosis will be flagged in future displays (i.e., \*\*\*ENTERED\*\*\* will appear next to the diagnosis). A free text, "Secondary Diagnosis Impression" prompt will appear as each diagnosis is entered.

> 3\. The Diagnosis/Diagnosis Supplement field is used to enter a diagnosis that did not appear on the computer generated list, to amplify a previously entered diagnosis, or to modify previously entered diagnoses.

> 4\. Revised Diagnosis allows the user to revise the Primary Diagnosis.

#### Diagnosis Review/Revision

> This option allows the user to enter/edit/revise diagnoses. Use of this option is similar to that described above in the Diagnosis Entry description.

#### Other Endoscopic Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Gastrointestinal Module for information about Line Enter/Edit, Reports, Brief Reports, and Release Control options.

#### Recall List

> This list is generated from patients who have "Endoscopy Followup" entered in the Final Disposition Field in the Enter/Edit Option. The user can specify a procedure or range of procedures, a final disposition date (or range of dates), and a patient (or range of patients). The final report will be sorted by procedure, then by final disposition date, and finally by patient name.

#### Image Capture

> The GI Menu contains an Image Capture option which allows a procedure image to be attached to a patient record. This option is only available to users at a workstation. Further information on Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for GI.

#### Brief Procedure Enter/Edit (Screen)

> Brief Endoscopy Screen 09/16/93

> 1 APPOINTMENT DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 INDICATED THERAPY(M):..............................

> 4 SIGNS AND SYMPTOMS(M):..............................

> 5 DISEASE FOLLOWUP(M):..............................

> 6 FOLLOWUP DEVICE OR THERAPY(M):..............................

> 7 SURVEILLANCE(M):..............................

> 8 PROTOCOL:.................................................

> 9 EGD SIMPLE PRIMARY EXAM:.................................

> 10 LAB OR XRAY:................................................

> 11 OCCULT BLOOD:..................................................

> 12 SPECIMEN COLLECTION:..........................................

> 13 INDICATION COMMENT:........................................

> Brief Endoscopy Screen Two 09/16/93

> 14 ENDOSCOPIST:..............................

> 15 FELLOW:..............................

> 16 DIET COMMENT:..............................

> 17 PNEUMOPERITONEUM GAS(M):....

> 18 SUMMARY:......................

> 19 LOCATION EVALUATED(M):..............................

> 20 COMMON BILE DUCT SIZE (mm):.....

> 21 PANCREATIC DUCT SIZE (mm):....

> 22 DEPTH OF INSERTION:..............................

> 23 RESULTS(M):..............................

> 24 COMPLICATIONS(M):..............................

> 25 DISPOSITION(M):....

> Immediately following this screen, the Diagnosis entry generator is prompted.

> Descriptions of the fields and subscreens of these screen will be found under the corresponding GI Procedure screen previously displayed and in the GI Quick Reference Guide.

> Gastrointestinal Module

> Non-Endoscopic Procedure

### Non-Endoscopic Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1 Enter/Edit Non-Endoscopic Exams (Line)

> 2 Enter/Edit Non-Endoscopic Exams (Screen)

> 3 Non-Endoscopic Report

> 4 Brief Enter/Edit of Non-endo GI Procedure

> 5 Brief Non-Endo Enter/Edit (Screen)

> 6 Brief Non-Endoscopic Report

> Non-Endoscopic GI Procedure Screen

NON-ENDOSCOPIC GI PROCEDURE 09/16/93

> 1 APPOINTMENT DATE/TIME:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 ENDOSCOPIST:..............................

> 4 NON-ENDOSCOPIC PROCEDURE(M):..............................

> 5 SUMMARY:.............................

> 6 SUBJECTIVE(W):.....

> 7 OBJECTIVE(W):.....

> 8 ASSESSMENT(W):.....

> 9 PLANNED(W):.....

> 10 PROCEDURE SUMMARY:........................................

> 1\. Indicates the date/time of the Endoscopy procedure.

> 2\. Identifies the name of the patient undergoing the procedure.

> 3\. Give the name of the provider who performed the procedure.

> 4\. This field stores the procedure type for a non-endoscopic GI procedure.

> 5\. Indicate whether the Endoscopy was Normal, Abnormal or Incomplete. This required field appears on the Summary of Patient Procedures.

> 6-9 These fields are used to enter information in the Consult options and the Non-

> Endoscopic GI Procedure entry using the SOAP (Subjective, Objective, Assessment, Planned) format.

> 10\. This is a free text summary of the Endoscopy (up to 79 characters). This required

> field appears on the Summary of Patient Procedures.

> Gastrointestinal Module

> Non-Endoscopic Procedure

#### Brief Non-Endo Enter/Edit (Screen)

Brief NON-GI Procedure Screen 09/16/93

> 1 APPOINTMENT DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 ENDOSCOPIST:..................

> 4 NON-ENDOSCOPIC PROCEDURE(M):..............................

> 5 SUMMARY:......................

> 6 SUBJECTIVE(W):.....

> 7 OBJECTIVE(W):.....

> 8 ASSESSMENT(W):.....

> 9 PLANNED(W):.....

> 10 PROCEDURE SUMMARY:.............................................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> GI Procedure screen previously displayed and in the GI Quick Reference Guide.

#### Other Non Endoscopic Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Gastrointestinal Module for information about Line Enter/Edit, Reports, Brief Reports, and Release Control options.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult Menu is discussed in the Problem Oriented Consult Menu section of this manual.

> Gastrointestinal Module

> GI Management Menu

### GI Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These options allow the user to enter or edit an instrument or medication for a selected procedure. The current options are:

> 1 GI Medication Update

> 2 Endoscopic Instrument Enter/Edit

> 3 Sphincterotome Enter/Edit (used for ERC procedures)

> 4 Stent Enter/Edit (used for ERC procedures)

> 5 Gastrostomy Tube Enter/Edit

> 6 Jejunostomy Tube Enter/Edit

> 7 Release Control Options (GI)

> GI Medication Update allows the user to place a drug in the Medication file and mark/unmark it as a GI medication. Any medication added to this file must first be present in the hospital formulary.

> 2-6 These menus refer to instruments that must be entered into the database before they can be referred to during a procedure enter/edit.

> 3-6 These fields are accessed through the Location Evaluated field of GI Procedure Enter/Edit (Screen 3 of 4). They are actually shown on Location Evaluated subscreen of GI Procedure Enter/Edit (Screen 2 of 2).

> Endoscopic Instrument Enter/Edit is used for all procedures on GI Procedure Enter/Edit (Screen

> 2 of 4).

> Sphincterotome Enter/Edit is used for entering ERC procedures.

> Stent Enter/Edit is used to enter ERC procedures.

> Gastrostomy Tube Enter/Edit is used to enter Gastrostomy Tube information.

> Jejunostomy Tube Enter/Edit is used to enter Jejunostomy tube information.

> Release Control Options (GI) is described in the Orientation and the Package Management sections of this manual under Release Control.

## PULMONARY MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> When you choose the Pulmonary Menu option from the main Medicine menu, the following menu appears.

> 1 Endoscopy Menu

> 2 Pulmonary Function Test Menu

> 3 Summary of Patient Procedures

> 4 Problem Oriented Consult Menu

> 5 Pulmonary Management Menu

### Documentation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options that are common to all procedure menus in the Pulmonary module are documented in this section rather than being repeated for each procedure.

#### Line Enter/Edit options

> This option accesses the same fields (unless otherwise noted) as the Enter/Edit (Screen) option.

> Field, field order, and entry descriptions are the same. Only the Enter/Edit (Screen) option is shown.

#### Reports

> The Reports option found on each procedure menu prints the report of the particular procedure done. The user is asked to enter the date and time of the procedure and the device on which to print. The report contains the information that was entered using the Enter/Edit (Screen or Line) option.

#### Brief Enter/Edit

> This option accesses the same fields (unless otherwise noted) as the Brief Enter/Edit (Screen) option. Only the Brief Enter/Edit (Screen) option is shown. The field descriptions for the brief screens are

> the same as for the corresponding field on the full screens and are not reshown.

#### Brief Report

> The Brief Reports print a report of the information that was entered using the Brief Enter/Edit options. The user is asked to enter the date and time of the procedure and the device on which to print

#### Release Control

> Use of these options is usually restricted by security keys given to clinical managers. A full description of the options can be found in the Orientation and the Package Management sections of this manual under Release Control.

### Endoscopy Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Endoscopy Menu has the following menu options.

> 1 Endoscopy Enter/Edit

> 2 Endoscopy Enter/Edit (Screen)

> 3 Endoscopic Report

> 4 Diagnosis Review/Revision

> 5 Recall List

> 6 Image Capture

> 7 Brief Endoscopy Enter/Edit

> 8 Brief Endoscopy Enter/Edit (Screen)

> 9 Brief Pulmonary Report

> 10 Release Control Options (Pulmonary)

#### Endoscopy Enter/Edit

> The Endoscopy Enter/Edit options use either standard FileMan procedures or a screen-based entry system to enter data. The information entered is identical. The screen-based system is presented below.

> After entering the procedure, an opportunity is provided for editing personal history information on the patient. Patient information concerning whether the patient has had a liver biopsy, heart disease, glaucoma, or allergies appears in this section. Any information entered here may be edited.

#### Updating Personal History Information

> 2 Procedure Enter/Edit (SCREEN) Enter Date/Time of Procedure:

> ARE YOU ADDING ..(date and time)..... AS A NEW ENDOSCOPY/CONSULT? Y (YES) ENDOSCOPY/CONSULT MEDICAL PATIENT: MEDPATIENT, ONE 09-15-39 000456789

> MILITARY RETIREE

> ENDOSCOPY/CONSULT PROCEDURE: PULM PULMONARY ENDOSCOPY

> PERSONAL HISTORY INFORMATION

> MEDPATIENT, ONE SSN: 000-45-6789

> History of Bleeding Disorder: Valvular Heart Disease: Glaucoma:

> History Comments:

> Allergies/Adverse Reactions: ASPIRIN

> Do you wish to edit the Personal History Information? NO// YES

#### Demographic Screen

> GI DEMOGRAPHIC DATA 02/03/94

> 1 NAME(R)

> 2 LIVER BIOPSY:....

> 3 VALVULAR HEART DISEASE:....

> 4 HISTORY OF BLEEDING DISORDER:....

> 5 GLAUCOMA:....

> 6 HISTORY COMMENTS:..................................................

> Enter Y(es) or N(o) to each condition. If only changes to the allergy information are needed, answer these questions with \<RET\>.

> Upon completion of the screen, one of the following messages will appear depending on whether or not the patient has allergies reported.

> This patient has no allergy/adverse reaction data.

> or

OBS/

> ADVERSE REACTION VERIFIED ALLER HIST

> ---------------- -------- ----- ---- FOOD/OTHER:

> ASPIRIN NO YES OBS Reactions: HIVES

#### Entering Allergies

> Enter Allergen:

> You may enter a new allergen or edit a previously entered one.

> (O)bserved or (H)istorical Allergy/Adverse Reaction: COMMENTS ON OBSERVED DATA:

> Edit? NO//

> A comment regarding the nature of the allergy may be added. To edit an existing comment, enter "YES".

> \_

> Enter 'YES' if you wish to go into the editor.

> Enter 'NO' if you do not wish to edit at this time.

> Edit? NO//

> Select DATE/TIME CHART MARKED:

> The date must be in the past, and time is a required response.\_

> Select DATE/TIME ID BAND MARKED:

> Press return to continue, ^ to exit: \<RET\>

> A report similar to the one below appears.

> PATIENT: MEDPATIENT, ONE ALLERGY/ADR: ASPIRIN

> ORIGINATOR: MEDUSER, TWO ORIGINATED: FEB 2, 1994@15:54

> SIGN OFF: NO OBS/HIST: OBSERVED OBSERVER: OBSERVED:

> MD NOTIFIED: CHART MARKED: FEB 1, 1994@18:53

> ID BAND MARKED:

> COMMENTS: SEVERITY:

> Would you like to sign off on this allergy/adverse reaction?

> OBS/ ADVERSE REACTION VERIFIED ALLER HIST

> ---------------- -------- ----- ---- FOOD/OTHER:

> ASPIRIN NO YES OBS Reactions: HIVES

> Enter Allergen:

> A new allergen may be entered or existing allergens may be edited.

> The following is seen if OE/RR is turned on.

> Select Service/Specialty: ALL SERVICES//

> \*\*\*\*\*\*\*\*\*\*\*\* ALL SERVICES (Pulmonary) Requests for MEDPATIENT, ONE \*\*\*\*\*\*\*\*\*\*\*\* MEDPATIENT, ONE 000-45-6789 JUN 13,1945 (40)

> No consult/request orders found!

> \* END \*

> Select Action: QUIT

> At the completion of editing the demographic data or allergies, the Endoscopy Enter/Edit (Screen 1 of 2) is automatically accessed.

> Endoscopy Enter/Edit (Screen 1 of 2)

> ENDOSCOPY (SCREEN 1 of 2) 09/16/93

> 1 APPOINTMENT DATE/TIME:................. 2 PROCEDURE(R):..........

> 3 MEDICAL PATIENT(R):..............................

> 4 SIGNS AND SYMPTOMS(M):..............................

> 5 <u>COUGH(M):</u>..............................

> 6 <u>PNEUMONIA(M):</u>..............................

> 7 DISEASE EVALUATION(M):..............................

> 8 FOLLOWUP DEVICE OR THERAPY(M):..............................

> 9 OTHER FOLLOWUP DEVICE/THERAPY:........................................

> 10 INDICATED THERAPY(M):..............................

> 11 INSTRUMENT(M):..............................

> 12 <u>MEDICATION USED(M):</u>..............................

> 13 BRONCHOSCOPIST:..............................

> 14 FELLOW:..............................

> 15 SECOND FELLOW:..............................

> After the Appointment Date/Time, Procedure, and Patient Name have been entered an opportunity will be given to edit patient history information. Information concerning whether the patient has had heart disease, glaucoma, or allergies appears in this section. Any information entered here may be edited.

> 1\. This field contains the date/time of the Endoscopy procedure.

> 2\. Indicate the specific procedure performed, such as colonoscopy.

> 3\. Identifies the name of the patient undergoing the procedure.

> An INDICATION COMMENT field appears here in the line enter/edit mode. This free text field is used to enhance or add to the specific indications for procedure.

> 4\. Record the specific sign or symptom for performing the procedure.

> 5\. This field stores the type of cough the patient has and the duration of the cough. Used for Pulmonary Endoscopies.

> 6 Give the location of pneumonia and the dates during which the pneumonia occurred. This is used as an indication for Pulmonary Endoscopies.

> 7\. This field refers to the patient who is undergoing a repeat procedure for the same (active)

> disease, such as follow-up on gastric ulcer healing. Used as an indication for procedure.

> 8\. Record the type of device or therapy, previously performed, which needs follow-up. Used as an indication for procedure.

> 9\. This free text field is used to summarize the type of device or therapy, previously performed, which needs follow-up therapy. This can be used instead of, or in addition to, the pointed to list.

> 10\. Specify the therapeutic manipulations which may be performed at the time of the examination. This does not record the findings of the procedure, but rather the reason for which the procedure is performed. Used as an indication for procedure.

> 11\. Indicate the Endoscopic instrument used for the procedure.

> 12\. Identify the type of medication administered for the procedure. Also record the dosage of the medication and the route of administration.

> 13\. Identify the provider who performed the procedure.

> 14\. Give the name of a fellow who assisted on the procedure.

> 15\. Enter the name of a second fellow who assisted on the procedure.

> Cough Subscreen of Endoscopy Enter/Edit (Screen 1 of 2)

> COUGH 09/16/93

> 1 TYPE OF COUGH:.................

> 2 DURATION:..............................

> 1\. This field identifies the type of cough the patient has.

> 2\. This free text subfield indicates the duration of the cough.

> Pneumonia Subscreen of Endoscopy Enter/Edit (Screen 1 of 2)

> PNEUMONIA 09/16/93

> 1 LOCATION OF PNEUMONIA:..........

> 2 DATES:..............................

> 1\. Enter the anatomical location of the pneumonia.

> 2\. Dates of Pneumonia should be entered in the format "Starting date"-"Ending date".

> Medication Subscreen of Endoscopy Enter/Edit (Screen 1 of 2)

> MEDICATION 09/16/93

> 1 MEDICATION USED:..............................

> 2 DRUG DOSE ROUTE:..............

> 3 TOTAL DOSE (in mg.):.........

> 1\. Indicate the specific medication administered.

> 2\. Using the codes provided, identify the route of administration for

> GI Endoscopies.

> 3\. Enter the dosage of the prescribed medication.

> Endoscopy Enter/Edit (Screen 2 of 2)

> ENDOSCOPY (SCREEN 2 of 2) 09/16/93

> 1 WHERE PERFORMED:..............................

> 2 WARD/CLINIC:..............................

> 3 TIME STARTED:....

> 4 TIME COMPLETED:....

> 5 URGENCY OF PROCEDURE:.........

> 6 SUMMARY:.............................

> 7 <u>LOCATION EVALUATED(M):</u>..............................

> 8 <u>COMPLICATIONS(M):</u>..............................

> 9 <u>FINAL DISPOSITION(M):</u>..............................

> 10 <u>PRESCRIPTION GIVEN(M):</u>..............................

> 11 INSTRUCTIONS TO PATIENT(W):.....

> 12 PROCEDURE SUMMARY:......................................

> 1\. Enter the hospital location where the procedure was performed.

> 2\. Give the in-house location of the patient.

> 3&4 Indicate the time the procedure was begun and completed in 24 hour time, without punctuation. (EX: 0800, 1630, etc.)

> 5\. Specify whether the procedure was elective, urgent, or emergency.

> 6\. Document whether the Endoscopy was Normal, Abnormal or Incomplete.

> This required field appears on the Summary of Patient Procedures.

> 7 Identify the anatomical location evaluated and record findings for the location evaluated.

> The "Select RESULTS" prompt follows this field in the line edit/enter mode. This field identifies a result of the overall procedure.

> CHOOSE FROM:

> DIAGNOSIS ESTABLISHED MATERIAL SENT FOR CELL COUNTS MATERIAL SENT FOR CHEMISTRIES MATERIAL SENT TO MICROBIOLOGY NO DIAGNOSIS ESTABLISHED

> STILL PHOTOGRAPHS OBTAINED

> VIDEO IMAGE RECORDED

> 8\. Indicate any complications encountered during the procedure or resulting from the procedure, and the result of the complication.

> 9\. This field stores post-encounter dispositions modified by a date and a free text reason.

> 10\. Specify the drug(s) and dosage(s) given as a post- encounter prescription.

> 11\. This is a word processing field which summarizes post-procedural instructions given to the patient.

> 12\. This is a free text summary of the Endoscopy (up to 79 characters). This required field appears on the Summary of Patient Procedures.

> Location Evaluated Subscreen of Endoscopy Enter/Edit (Screen 2 of 2)

> LOCATION EVALUATED 09/16/93

> 1 LOCATION EVALUATED:..............................

> 2 GROSS:....................

> 3 MODIFIER(M):..............................

> 4 MEASUREMENT:...............

> 5 TECHNIQUE(M):..............................

> 6 IMPRESSION:.............................................

> 1\. Identify the anatomical location that was evaluated.

> 2\. Gross refers to an identifying descriptor of the finding of the anatomical location. Entering

> “?” provides a list to choose from.

> 3\. Modifier allows specific modifiers for the gross descriptor.

> 4\. This field identifies the size of the Gross finding (Ex: 4 cm; 4x3 cm; 4 cm high, etc.)

> 5\. Technique is a multiple field that identifies the specific technique used to evaluate the location.

> 6\. Enter findings for the location evaluated. The list of possible diagnoses is built from the entries in this field. If nothing is entered here, the only field that will appear for Diagnosis Entry will be Diagnosis/Diagnosis Supplement.

> Complications Subscreen of Endoscopy Enter/Edit (Screen 2 of 2)

> COMPLICATIONS 09/16/93

> 1 COMPLICATIONS:..........................

> 2 COMP. RESULTS:...........................

> 1\. Identify any complications encountered during the procedure or as a result of the procedure.

> 2\. Specify the result of the complication, ranging from "Required no therapy" to "Resulting in death."

> Final Disposition Subscreen of Endoscopy Enter/Edit (Screen 2 of 2)

> DISPOSITION 09/16/93

> 1 FINAL DISPOSITION:........................

> 2 FINAL DISPOSITION DATE:.................

> 3 REASON:...............................

> 1\. An entry of "Endoscopy Followup" at the Final Disposition prompt will place the patient on the recall list.

> 2\. Enter the date of the disposition. This date may be in the future as in the case of Endoscopy

> Follow-Up entered as the disposition.

> 3\. Identify the reason for the disposition given.

> Prescription Given Subscreen of Endoscopy Enter/Edit (Screen 2 of 2)

> PRESCRIPTION 09/16/93

> 1 PRESCRIPTION GIVEN:......................

> 2 DOSAGE:..............................

> 1\. Specify the name of the formulary drug given as a post-encounter prescription.

> 2\. Indicate the dosage of the prescribed drug.

#### Other Pulmonary Options

> Please refer to Enter/Exit options in the Orientation section of this manual and to Documentation Notes under Pulmonary Module for information about Line Enter/Edit, Reports, Brief Reports, and Release Control options.

#### Diagnosis Entry

> Immediately following the prompt, "Procedure Summary" on the Endoscopy (Screen 2 of 2), the Diagnosis generator is prompted. This information can also be entered using the Diagnosis Review/Revision option.

> 1\. Primary Diagnosis: If entries have been made in the Location Evaluated field on Screen 2 and in the Impression field of the Location Evaluated subscreen, a list of possible diagnoses is generated from those impressions. The user is prompted to enter a primary diagnosis from the list. Once a user enters a diagnosis in this field, it CANNOT be changed or deleted. If an entry is made in this field a free text "Primary Diagnosis Impression" prompt is accessed.

> If no entries were made in the Impressions subfield of the Location Evaluated subscreen, the only Diagnosis Entry prompt that will appear is "Diagnosis/ Diagnosis Supplement"

> 2\. Secondary Diagnosis: The user is then shown the list of possible secondary diagnoses. This list is the original diagnosis list minus the diagnosis entered as the primary diagnosis. The user can enter "all" to enter the entire list as secondary diagnoses, or select a diagnosis from the

> list. Once a diagnosis from the list is entered as a secondary diagnosis, this diagnosis will be flagged in future displays (i.e., \*\*\*ENTERED\*\*\* will appear next to the diagnosis). A free text, "Secondary Diagnosis Impression" prompt will appear as each diagnosis is entered.

> 3\. The Diagnosis/Diagnosis Supplement field is used to enter a diagnosis that did not appear on the computer generated list, to amplify a previously entered diagnosis, or to modify previously entered diagnoses.

> 4\. Revised Diagnosis allows the user to revise the Primary Diagnosis.

#### Recall List

> This list is generated from patients who have "Endoscopy Followup" entered in the "Final Disposition" field in the Enter/Edit Option. The user can specify a procedure or range of procedures, a final disposition date (or range of dates), and a patient (or range of patients). The final report will be sorted by procedure, next by final disposition date, and finally by patient name.

#### Image Capture

> The Pulmonary Menu contains an Image Capture option which allows a procedure image to be attached to a patient record. This option is only available to users at a workstation. Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for GI.

#### Brief Endoscopy Enter/Edit (Screen)

> Brief Pulmonary Screen 09/16/93

> 1 APPOINTMENT DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 SIGNS AND SYMPTOMS(M):..............................

> 4 <u>COUGH(M):</u>..............................

> 5 <u>PNEUMONIA(M):</u>..............................

> 6 DISEASE FOLLOWUP(M):..............................

> 7 FOLLOWUP DEVICE OR THERAPY(M):..............................

> 8 OTHER FOLLOWUP DEVICE/THERAPY:........................

> 9 INDICATED THERAPY(M):..............................

> 10 BRONCHOSCOPIST..............................

> 11 SUMMARY:......................

> 12 PROCEDURE SUMMARY:.........................................

> Immediately following the prompt, "Procedure Summary", the Diagnosis generator is prompted. The list of diagnoses presented is generated from the answers to the "Impressions" prompt on the Location Evaluated subscreen when using the Endoscopy Enter/Edit options.

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Pulmonary or Endoscopy screens previously displayed and in the Pulmonary Quick Reference Guide.

> Pulmonary Module

> Pulmonary Function Test

### Pulmonary Function Test Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options provided on the PFT menu are:

> 1 Enter/Edit PFT

> 2 Interpretation Enter/Edit

> 3 PFT Report

> 4 Enter/Edit PFT (Screen)

> 5 Brief PFT Enter/Edit

> 6 Brief PFT Enter/Edit (Screen)

> 7 Brief PFT Report

> 8 Release Control Options (PFT)

> The PFT Enter/Edit options use either standard FileMan procedures or a screen-based entry system to enter data. The information entered is identical. The screen-based system is presented below.

#### Enter/Edit PFT

> The Enter/Edit PFT option is used to enter the results of various tests. After a patient is selected; the date, patient weight and height, room barometric pressure, room temperature, smoking status, bronchodilator use, clinic and technician are entered. Information on various tests is then entered.

> The Enter/Edit PFT option and the Enter/Edit PFT (Screen) option access the same information and have the same descriptions. The screen entry method is shown in the documentation.

> PULMONARY FUNCTION TEST (SCREEN 1 OF 2) 01/27/03

> 1 DATE/TIME:DEC 31,2002@11:05

> 2 MEDICAL PATIENT:MEDPATIENT, TWO

> 3 HEIGHT (INCHES.TENTHS):...... 4 HEIGHT (CM):......

> 5 WEIGHT (POUNDS.TENTHS):...... 6 WEIGHT (KG):....

> 7 BAROMETRIC PRESSURE:600 8 ROOM TEMPERATURE (CENTIGRADE):35

> 9 TECHNICIAN:......................

> 10 USE RACE CORRECTIONS:.... <u>11 RACE CORRECTIONS FOR RACE TYPE:......</u>

> 12 SMOKER:YES 13 CURRENT BRONCHODILATOR:....

> 14 WARD/CLINIC:..............................

> 15 REFERRING PHYSICIAN:..............................

> 16 CONSULT DX(M):.............................. 17 VOLUME STUDY(M):....

> 18 FLOW STUDY MACHINE:.............. 19 PATIENT EFFORT:.........

> 20 FLOWS STUDY(M):..............................

> 21 DIFFUSING CAPACITY METHOD:.............

> 1\. Enter the date/time of the Pulmonary Function tests.

> 2\. Identify the patient's name.

> 3\. Specify height in inches and tenths of inches.

> 4\. Give the height in cm.

> 5\. Enter the weight in pounds and tenths of pounds.

> 6\. Give the weight in kg.

> 7\. This is the Barometric Pressure in Torr units at the time the PFT was done.

> 8\. Enter the room temperature at the time the PFT was done.

> 9\. Identify the technician who performed the PFT.

> 10\. This field allows the user to decide whether certain data should be race corrected. Used for

> Black or Oriental patients.

> 11\. This field allows the user to decide which race correction should be used if the patient has both race values of ASIAN and BLACK.

> 12\. Enter whether the patient is a smoker or a non-smoker.

> 13\. Tell whether the patient had used a Bronchodilator within 4 hours of the test.

> 14\. Indicate the ward if the patient is an inpatient, the clinic if the patient is an outpatient.

> 15\. Identify the physician who ordered the PFT.

> 16\. This is the diagnosis sent to the PFT lab by the referring physician.

> 17\. The subfields of this field hold the Volume Study data for the PFT.

> 18\. Identify the type of machine used for the Flow Study.

> 19\. This field indicates the patient effort: GOOD, EXCELLENT, or POOR.

> 20\. The subfields of this field Store data of the Flow Study done on the patient in this field.

> 21\. Identify the method used for the Diffusing Capacity (DLCO) Test.

> Pulmonary Function Test - Volume Study Subscreen

> PULMONARY FUNCTION TEST - VOLUME STUDY 09/16/93

> 1 VOLUME STUDY TYPE:..................

> 2 TLC:....... 3 VC:....... 4 FRC:...... 5 RV:......

> 6 NOTES:.........................................

> 1\. Enter the type of Volume Study done.

> 2\. Indicate the Total Lung Capacity measured.

> 3\. Give the measured Vital Capacity.

> 4\. Provide the measured Functional Residual Capacity.

> 5\. Indicate the measured Residual Volume.

> 6\. Provide notes on the current Volume Study.

> Pulmonary Function Test - Flows Study Subscreen

> PULMONARY FUNCTION TEST - FLOWS STUDY 09/16/93

> 1 FLOWS STUDY:..........................

> 2 FVC:...... 3 FEV1:....... 4 PF:.........

> 5 FEF25-75:......... 6 FEV1/FVC(C):........ 7 MVV:....

> 8 NOTES:............................................................

> 1\. Enter the type of Flow Study performed.

> 2\. Indicate the measured Forced Vital Capacity.

> 3\. Give the measured Forced Expired Volume in 1 second intervals.

> 4\. Enter the measured Peak Flow.

> 5\. Provide the measured Forced Expired Flow from 25 to 75 percent in Liters/Sec.

> 6\. This field is computed from the Forced Expired Volume divided by the Forced Vital capacity.

> 7\. Enter the Maximum Voluntary Ventilation in liters/minute.

> 8\. This field allows the entering of a note (up to 60 characters) on this Flow Study.

> Pulmonary Function Test (Screen 2 of 2)

> PULMONARY FUNCTION TEST (SCREEN 2 OF 2) 09/16/93

> 21 DLCO-SB:..... 22 <u>BLOOD GAS(M):</u>.....................

> 23 <u>SPECIAL STUDIES(M):</u>.................

> 21\. Indicate the measured Diffusing Capacity.

> 22\. This multiple field stores the data for the Arterial Blood Gas (ABG) Study.

> 23\. Enter the type of Special Study done.

> PFT Special Studies Subscreen of Pulmonary Function Test (Screen 2 of 2)

> PFT SPECIAL STUDIES (SCREEN 1 OF 2) 09/16/93

> 1 TYPE OF SPECIAL STUDY:.................

> Type \<CR\> to go to next screen or enter @ to delete

> this Special Study

> 1\. Enter the type of Special Study done. This field can be used to edit or change the type of Special Study without deleting the entry in the Special Studies field of Pulmonary Function Test (Screen 2 of 2). The type of study entered here determines the subscreen that will appear.

> Pulmonary Function Test - Blood Gas Subscreen

> PULMONARY FUNCTION TEST - BLOOD GAS 09/16/93

> 1 BLOOD GAS:.....................

> 2 HB:...... 3 pH:........ 4 pCO2:...... 5 pO2:......

> 6 O2HB:...... 7 COHB:..... 8 FiO2:........ 9 MHB:.....

> 10 NOTES:............................................................

> 11 PATIENT TEMPERATURE:.....

> 1\. Identify the type of Arterial Blood Gas Study done.

> 2\. Enter the measured Hemoglobin value.

> 3\. Indicate the measured pH level.

> 4\. Give the measured Arterial Carbon Dioxide Pressure in mm Mercury.

> 5\. Provide the measured Arterial Oxygen Pressure in mm Mercury..

> 6\. Enter the measured Hemoglobin Oxygen.

> 7\. Give the measured Carboxyhemoglobin Saturation.

> 8\. Indicate the fraction of Inspired Oxygen.

> 9\. Furnish the Methemoglobin Saturation.

> 10\. Enter up to a 60 character note describing the Arterial Blood Gas study.

> 11\. Specify the patient temperature in degrees Centigrade.

> PFT - Special Studies, Mechanics Subscreen

> PFT SPECIAL STUDIES (MECHANICS) 09/16/93

> 1 TYPE OF SPECIAL STUDY(R):.................

> 2 RESISTANCE,RAW:.....

> 3 RESISTANCE,SGAW:........

> 4 COMPLIANCE,CST:........

> 5 NOTES:.........................................

> 1\. Shows the type of Special Study done.

> 2\. Enter the Specific Airway Resistance in cm H2O/ liters per second. Used in the Mechanics

> Special Study.

> 3\. Indicate the Specific Airway Conductance in liters per second/cm H2O. Used in the

> Mechanics Special Study.

> 4\. Give the Static Compliance in liters/cm H2O. Used in the Mechanics Special Study.

> 5\. Enter notes describing the Special Study (up to 60 characters).

> PFT - Special Studies, Small Airways Subscreen

> PFT SPECIAL STUDIES (SMALL AIRWAY) 09/16/93

> 1 TYPE OF SPECIAL STUDY(R):.................

> 2 COMPLIANCE,CDYN:........

> 3 FEF50 HE-AIR:........

> 4 VISOV:.........

> 5 CV:........

> 6 CC:........

> 7 NOTES:.................................

> 1\. Shows the type of Special Study done.

> 2\. Indicate the Dynamic Compliance in liters/cm H2O. Used in the Small Airway Special

> Study.

> 3\. Provide the Maximum Expiratory at 50% of Vital Capacity breathing air in liters/second.

> Used in the Small Airway Special Study.

> 4\. Give the Lung Volume at which Helium & Air Flow Tracings meet in liters. Used in the

> Small Airway Special Study.

> 5\. Enter the Closing Volume in liters. Used in the Small Airway Special Study.

> 6\. Indicate the Closing Capacity in liters. Used in the Small Airway Special Study.

> 7\. Enter notes describing the Special Study (up to 60 characters).

> PFT - Special Studies, Exercise Subscreen

> PFT SPECIAL STUDIES (EXERCISE) 09/16/93

> 1 TYPE OF SPECIAL STUDY(R):.................

> 9 VO2 MAX:........

> 24 EXERCISE TESTING MODE:..............

> 25 REASON FOR STOPPING(M):..............................

> 26 OTHER REASON FOR STOPPING(W):.....

> 27 NOTES:............................................................

> 1\. Shows the type of Special Study done.

> 2\. Identify the maximum Expiratory Minute Ventilation at peak exercise in ml/beat. Used for the Exercise Special Study.

> 3\. Indicate the Breathing Reserve in liters. Used in the Exercise Special Study.

> 4\. Give the Resting Dead Space to Tidal Volume Ratio. Used in the Exercise Special Study.

> 5\. Specify the Maximum Dead Space to Tidal Volume Ratio. Used in the Exercise Special

> Study.

> 6\. Provide the Ventilatory Equivalent for Carbon Dioxide at Anaerobic Threshold. Used in the

> Exercise Special Study.

> 7\. Indicate the Expiratory Minute Ventilation at rest in ml/beat. Used in the Exercise Special

> Study.

> 8\. Enter the Oxygen Uptake at Rest in liters/minute. Used in the Exercise Special Study.

> 9\. Give the Oxygen Uptake at Peak Exercise in liters/minute. Used in the Exercise Special

> Study.

> 10\. Specify the Anaerobic Threshold in liters. Used in the Exercise Special Study.

> 11\. Tell the Heart Rate at Rest. Used in the Exercise Special Study.

> 12\. Indicate the Heart Rate at Peak Exercise in beats/minute. Used in the Exercise Special

> Study.

> 13\. Show the Oxygen Pulse Maximum in milliliters per beat. Used in the Exercise Special Study.

> 14\. Enter the Maximum Blood Pressure. Used in the Exercise Special Study.

> 15\. Specify whether the EKG was Normal or Abnormal. Used in the Exercise Special Study.

> 16\. Give the Respiratory Rate at Rest. Used in the Exercise Special Study.

> 17\. Enter the Respiratory Rate at Peak Exercise. Used in the Exercise Special Study.

> 18\. Indicate the Work Rate in Watts. Used in the Exercise Special Study.

> 19\. Furnish the Work Rate Increment/Work Rate Time Interval ratio in Watts per minute. Used in the Exercise Special Study.

> 20\. Specify the Maximum Treadmill Speed in MPH at Peak Exercise. Used in the Exercise

> Special Study.

> 21\. Enter the Maximum Treadmill Grade at Peak Exercise. Used in the Exercise Special Study.

> 22\. Give the Total Time in minutes of Exercise. Used in the Exercise Special Study.

> 23\. Specify the change in bicarbonate in mEq/l. Used in the Exercise Special Study.

> 24\. Identify the mode of testing used for an Exercise Special Study.

> 25\. Establish the Reason for Stopping an Exercise Special Study.

> 26\. Explain the Reason(s) for Stopping the Exercise Special Studies which are not in the

> REASON (MEDICINE) file.

> 27\. Enter notes on the Special Study.

> PFT - Special Studies, Maximum Pressures Subscreen

> PFT SPECIAL STUDIES (MAXIMUM PRESSURES) 09/16/93

> 2 PIMAX:....

> 3 NOTES:........................................

> 2\. Indicate the Maximum Inspiratory Pressure in cm H2O. Only element of the Maximum

> Pressures Special Study.

> 3\. Enter a note on the Special Study.

> PFT - Special Studies (Screen 2 of 2)

> PFT SPECIAL STUDIES (SCREEN 2 OF 2) 09/16/93

> EXERCISE STUDY DATA

> 31 VEMAX(BTPS):.... 32 BR:.......... 33 VD/VT REST:......

> 34 VD/VT MAX:...... 35 VE/VCO2, AT:........ 36 VE REST(BTPS):....

> 37 VO2 REST:........ 38 VO2 MAX:........ 39 AT:......... 40 HR REST:........

> 41 HR MAX:.... 42 VO2/HR:.......... 43 BP MAX:....... 44 EKG:........

> 45 RR REST:....... 46 RR MAX:....... 47 W MAX:......... 48 WRI/WRT:.........

> 49 MAX SPEED:....... 50 MAX GRADE:....... 51 TOTAL TIME:.....

> 52 HCO3 CHANGE:.... 53 EXERCISE TESTING MODE:..............

> 54 REASON FOR STOPPING(M):..............................

> 55 OTHER REASON FOR STOPPING(W):.....

> MAXIMUM PRESSURES STUDY DATUM: 56 PIMAX:....

> FOR ALL STUDIES:

> 57 NOTES:............................................................

> 31\. Identify the maximum Expiratory Minute Ventilation at peak exercise in ml/beat. Used for the Exercise Special Study.

> 32\. Enter the Breathing Reserve in liters. Used in the Exercise Special Study.

> 33\. Specify the Resting Dead Space to Tidal Volume Ratio. Used in the Exercise Special Study.

> 34\. Supply the Maximum Dead Space to Tidal Volume Ratio. Used in the Exercise Special

> Study.

> 35\. Furnish the Ventilatory Equivalent for Carbon Dioxide at Anaerobic Threshold. Used in the

> Exercise Special Study.

> 36\. Indicate the Expiratory Minute Ventilation at rest in ml/beat. Used in the Exercise Special

> Study.

> 37\. Indicate the Oxygen Uptake at Rest in liters/Minute. Used in the Exercise Special Study.

> 38\. Express the Oxygen Uptake at Peak Exercise in liters/minute. Used in the Exercise Special

> Study.

> 39\. Enter the Anaerobic Threshold in liters. Used in the Exercise Special Study.

> 40\. Identify the Heart Rate at Rest. Used in the Exercise Special Study.

> 41\. Furnish the Heart Rate at Peak Exercise in beats/minute. Used in the Exercise Special

> Study.

> 42\. Give the Oxygen Pulse Maximum in milliliters per beat. Used in the Exercise Special Study.

> 43\. Indicate the Maximum Blood Pressure. Used in the Exercise Special Study.

> 44\. Enter whether the EKG was Normal or Abnormal. Used in the Exercise Special Study.

> 45\. Enter the Respiratory Rate at Rest. Used in the Exercise Special Study.

> 46\. Give the Respiratory Rate at Peak Exercise. Used in the Exercise Special Study.

> 47\. Specify the Work Rate in Watts. Used in the Exercise Special Study.

> 48\. Express the Work Rate Increment/Work Rate Time Interval ratio in Watts per minute. Used in the Exercise Special Study.

> 49\. Indicate the Maximum Treadmill Speed in MPH at Peak Exercise. Used in the Exercise

> Special Study.

> 50\. Enter the Maximum Treadmill Grade at Peak Exercise. Used in the Exercise Special Study.

> 51\. Identify the Total Time in minutes of Exercise. Used in the Exercise Special Study.

> 52\. Indicate the change in bicarbonate IN mEq/l. Used in the Exercise Special Study.

> 53\. Enter the mode of testing used for an Exercise Special Study.

> 54\. Specify the Reason for Stopping an Exercise Special Study.

> 55\. Enter Reason(s) for Stopping the Exercise Special Studies which are not in the REASON (MEDICINE) file.

> 56\. Furnish the Maximum Inspiratory Pressure in cm H2O. Only element of the Maximum

> Pressures Special Study.

> 57\. Enter a note on the Special Study.

#### Other PFT Options

> Please refer to the Orientation section of this manual and to Documentation Notes under Pulmonary

> Module for information about Line Enter/Edit options, Brief Reports, and Release Control options.

> Interpretation Enter/Edit

#### Interpretation Enter/Edit

> The Interpretation Enter/Edit option is used to display the results of various pulmonary studies and enter interpretations. A section of this display is presented below.

> \*\*\*

> VOLUME INTERPRETATION

> UNITS PRED ACTUAL %PRED PREV1 PREV2 LCI HELIUM STUDY 3/8/90

> (NOTES): TESTING TESTING TESTING

> TLC L 6.96 5.00 71.9 13.23 5.35

> VC L 4.51 3.25 72.1 12.22 1.12

> FRC L 2.82 2.24 79.4 6.65 1.36

> RV L 2.01 1.74 86.6 7.22 1.25

> RV/TLC % 29 35

> AFTER EXERCISE 3/8/90 (NOTES): TESTING THIS OPTION

> TLC L 6.96 4.00 57.5 5.35

> VOLUME INTERPRETATION:

> 1\>

> FLOWS INTERPRETATION

> UNITS PRED ACTUAL %PRED PREV1 PREV2 LCI STANDARD STUDY 3/8/90

> (NOTES): TESTING 1

> MMF L/SEC 2.98 2.13 71.5 1.67

> FEV1/FVC % 72 72

> AFTER EXERCISE 3/8/90 (NOTES): TESTING FLOWS STUDY NOTES

> FEV1/FVC % 72 72

> PREDICTED VALUE FORMULAS USED

> TLC .0590\*HT-4.537 CRAPO '82

> VC .049\*HT-(.0216\*AGE)-3.59 CRAPO '81

> FRC .0360\*HT-(.0031\*AGE)-3.182 CRAPO '82

> RV .0197\*HT+(.0201\*AGE)-2.421 CRAPO '82

> FVC .049\*HT-(.0216\*AGE)-3.59 CRAPO '81

> FEV1 .0342\*HT-(.0255\*AGE)-1.578 CRAPO '81

> PF 2.63\*HT-(1.84\*AGE)+14.06/60 FERRIS '64

> FEF25-75 .0154\*HT-(.046\*AGE)+2.683 CRAPO '81

> MVV .924\*HT-(.82\*AGE)-10.7 LINDALL '67

> DLCO-SB .282\*HT-(.157\*AGE)-10.89 CRAPO '81

> COHB CORR. ACT\*(1+COHB) MORRIS '85

> HB CORR. HB+10.22/(1.7\*HB)\*ACT COTES '72

> NOTE: HT=height,WT=weight,ACT=actual measurement value

> After all data has been displayed, any computer generated interpretations will be displayed, and the user will have the option of accepting each interpretation.

> Example:

COMPUTER GENERATED INTERPRETATIONS: OBSTRUCTIVE DEFECT MAY BE PRESENT

ACCEPT THIS INTERPRETATION? YES///

> After all computer generated interpretations have been asked, the following prompts appear.

> FREE TEXT INTERPRETATION:

> 1\>

> COMMENTS AND RECOMMENDATIONS:

> 1\>

> Select INTERPRETATION BY:

> REVIEWED BY, SUMMARY,

> PROCEDURE SUMMARY,

> PFT Report

#### PFT Report

> This report presents a summary of all Pulmonary Function Tests performed on a given patient on a selected date. An example of this report is given below.

> Pg. 1 03/24/93 14:47

> CONFIDENTIAL PULMONARY FUNCTION TEST REPORT - Superseded Released On-Line Verified

> MEDPATIENT, ONE 000-45-6789 NOT INPATIENT DOB: 11/18/31

> PROCEDURE DATE/TIME: 04/11/86

> \- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

> SEX: M AGE:65 72 in/180.199999999999999998 lbAMBIENT: 24C/750T

> RACE: WHITE TECH: MEDUSER, THREE SMOKER CURRENT BRONCHODILATOR USE EFFORT:

> CONSULT DX: BRONCHITIS SUSPECTED BRONCHIAL ADENOMA SEEN

> ................................................................. ........

> UNITS PRED ACTUAL %PRED PREV1 PREV2 CI VOLUMES.......................................................... ........

> X-RAY PLANIMETRY 3/8/90 2/28/90 (NOTES): TESTING TESTING TESTING

> TLC L 7.19 5.00 69.6 13.23 5.58

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 21%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VC</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>4.76</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>3.25</p>
</blockquote></td>
<td><blockquote>
<p>68.3</p>
</blockquote></td>
<td><blockquote>
<p>12.22</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FRC</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>2.82</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2.24</p>
</blockquote></td>
<td><blockquote>
<p>79.4</p>
</blockquote></td>
<td><blockquote>
<p>6.65</p>
</blockquote></td>
<td><blockquote>
<p>1.78</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RV</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>2.39</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1.74</p>
</blockquote></td>
<td><blockquote>
<p>72.7</p>
</blockquote></td>
<td><blockquote>
<p>7.22</p>
</blockquote></td>
<td><blockquote>
<p>1.63</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RV/TLC</p>
</blockquote></td>
<td><blockquote>
<p>%</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>35</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> X-RAY PLANIMETRY

> (NOTES): TESTING THIS OPTION

> TLC L 7.19 4.00 55.7 5.58

> FLOWS............................................................ ........

> MACHINE:

> STANDARD STUDY 2/28/90 (NOTES): TESTING 1

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FVC</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>4.76</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>3.25</p>
</blockquote></td>
<td><blockquote>
<p>68.3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEV1</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>3.68</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2.32</p>
</blockquote></td>
<td><blockquote>
<p>63.1</p>
</blockquote></td>
<td>2.83</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PF</p>
</blockquote></td>
<td><blockquote>
<p>L/SEC</p>
</blockquote></td>
<td><blockquote>
<p>457.64</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2.32</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>279.44</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEF25-75</p>
</blockquote></td>
<td><blockquote>
<p>L/SEC</p>
</blockquote></td>
<td><blockquote>
<p>3.34</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2.13</p>
</blockquote></td>
<td><blockquote>
<p>63.9</p>
</blockquote></td>
<td>1.67</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEV1/FVC</p>
</blockquote></td>
<td><blockquote>
<p>%</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>77</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> AFTER EXERCISE 3/8/90 (NOTES): TESTING FLOWS STUDY NOTES

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FVC</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>4.76</p>
</blockquote></td>
<td><blockquote>
<p>3.25</p>
</blockquote></td>
<td><blockquote>
<p>68.3</p>
</blockquote></td>
<td><blockquote>
<p>3.44</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEV1</p>
</blockquote></td>
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>3.68</p>
</blockquote></td>
<td><blockquote>
<p>2.32</p>
</blockquote></td>
<td><blockquote>
<p>63.1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2.83</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PF</p>
</blockquote></td>
<td><blockquote>
<p>L/SEC</p>
</blockquote></td>
<td><blockquote>
<p>457.64</p>
</blockquote></td>
<td><blockquote>
<p>2.32</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>279.44</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEF25-7</p>
</blockquote></td>
<td>5 L/SEC</td>
<td><blockquote>
<p>3.34</p>
</blockquote></td>
<td><blockquote>
<p>2.19</p>
</blockquote></td>
<td><blockquote>
<p>65.7</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1.67</p>
</blockquote></td>
</tr>
</tbody>
</table>

> FEV1/FVC % 77

> DIFFUSION........................................................ ...........

> METHOD:

> DLCO-SB L 33.84

> Corrected DLCO for COHB: 36.46

> BLOOD GASES........................................................

> STUDY TYPE pH PaCO2 PaO2 O2HB COHB MHB HB FiO2 A-aO2 QS/QT (NORMAL) 7.36-7.44 36-44 80-100 .95-1.0 \<.03 0.0 29.35

> SUPPLEMENTAL 7.40 38 69 0.91 0.030 0.010 11.0 0.21 31 (NOTES): TESTING ABG NOTES

> UNITS PRED ACTUAL %PRED PREV1 PREV2

> SPECIAL STUDIES.......................................................... .......

> SMALL AIRWAY 3/8/90 2/28/90

> Cdyn L/cmH20 7.22

> FEF50 He-Air L/Sec 40.80 345.22 846.1

> PREDICTED VALUE FORMULAS USED

> TLC .0590\*HT-4.537 CRAPO '82

> VC .049\*HT-(.0216\*AGE)-3.59 CRAPO '81

> FRC .0360\*HT-(.0031\*AGE)-3.182 CRAPO '82

> RV .0197\*HT+(.0201\*AGE)-2.421 CRAPO '82

> FVC .049\*HT-(.0216\*AGE)-3.59 CRAPO '81

> FEV1 .0342\*HT-(.0255\*AGE)-1.578 CRAPO '81

> PF 2.63\*HT-(1.84\*AGE)+14.06/60 FERRIS '64

> FEF25-75 .0154\*HT-(.046\*AGE)+2.683 CRAPO '81

> MVV .924\*HT-(.82\*AGE)-10.7 LINDALL '67

> DLCO-SB .282\*HT-(.157\*AGE)-10.89 CRAPO '81

> COHB CORR. ACT\*(1+COHB) MORRIS '85

> HB CORR. HB+10.22/(1.7\*HB)\*ACT COTES '72

> INTERPRETATION................................................... ......... INTERPRETATION: RESTRICTIVE DEFECT MAY BE PRESENT

> COMMENTS AND RECOMMENDATIONS:

> INTERPRETED BY: COLORADO,ROLLIE REVIEWED BY: TEXAS,AUGIE

> \- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - R e p o r t R e l e a s e S t a t u s

> Current Date Person Who

> Report Status Last Changed Date of Report

> Status Changed The Status Entry Version

> ========================================================================

> \` PFT Report

#### Brief PFT Enter/Edit (Screen)

> Brief PFT Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 SUMMARY:.......................... 4 <u>VOLUME STUDY(M):</u>....

> 5 FLOWS STUDY(M):.... 6 <u>BLOOD GAS(M):</u>....

> 7 INTERPRETATION BY(M):..............................

> 8 COMP. GENERATED INTERPRETATION(M):..............................

> 9 FREE TEXT INTERPRETATION(W):.....

> 10 PROCEDURE SUMMARY:......................................

> Descriptions of the fields and subscreens for this screen will be found under the corresponding PFT Enter/Edit explained previously.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult Menu is discussed in the Problem Oriented Consult Menu section of this manual.

Pulmonary Module

Pulmonary Management Menu

### Pulmonary Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Pulmonary Management Menu provides the options needed for local control of files for specific use of the Pulmonary Module.

#### Pulmonary Medication Update

> This allows the user to place a drug in the Medication file and mark/unmark it as a pulmonary medication. Medications added to this file must first be present in the Hospital Formulary.

#### Pulmonary Instrument Enter/Edit

> The user can enter new instruments into this file, or edit those already there.

#### PFT Predicted Values Formulas

> Edit Predicted Value Formulas

> This allows the user to select his own set of correction and predicted value formulas as shown below.

> Select the Predicted Value Formula: ?

> Answer with PFT FORMULA TYPE

> Do you want the entire PFT FORMULA List? Y (Yes)

> Choose from:

> COHB ACT\*(1+COHB) MEDPATIENT '85

> COHB ACT\*(1+(COHB/100)) MEDPATIENT '85

> COHB ACT\*(1+(COHB/100)) MEDPATIENT '85

> DLCO-SB 2.2382-(.1111\*AGE)+(.160\*HT) MEDPATIENT '83 FEMALE

> DLCO-SB .282\*HT-(.157\*AGE)-10.89 MEDPATIENT '81 FEMALE

> DLCO-SB 12.9113-(.229\*AGE)+(.1672\*HT) MEDPATIENT '83 MALE

> DLCO-SB .410\*HT-(.21\*AGE)-26.31 MEDPATIENT '81 MALE

> DLCO-SB 2.2382-(.1111\*AGE)+(.0163\*HT) MEDPATIENT '83 FEMALE

> DLCO-SB 2.2382-(.1111\*AGE)+(.0163\*HT) MEDPATIENT '83 FEMALE

> FEF25-75 .024\*HT-(.030\*AGE)+.551 MEDPATIENT '75 FEMALE

> FEF25-75 .0204\*HT-(.038\*AGE)+2.133 MEDPATIENT '81 MALE FEV1 .0356\*HT-(.025\*AGE)-1.932 MEDPATIENT '71 FEMALE FEV1 .0342\*HT-(.0255\*AGE)-1.578 MEDPATIENT '81 FEMALE FEV1 .0368\*HT-(.032\*AGE)-1.26 MEDPATIENT '71 MALE

> FEV1 .0414\*HT-(.0244\*AGE)-2.190 MEDPATIENT '81 MALE FRC .0360\*HT-(.0031\*AGE)-3.182 MEDPATIENT '82 FEMALE FRC .081\*HT-(.017\*AGE)-7.11 MEDPATIENT '58 MALE

> FRC .032\*HT-2.94 MEDPATIENT ONE & TWO '66 MALE FRC .081\*HT-(1.792\*AGE)-7.11 MEDPATIENT '58 MALE

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 45%" />
<col style="width: 29%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FRC</p>
</blockquote></td>
<td><blockquote>
<p>.081*HT-(1.792*AGE)-7.11</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT '58</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FVC1</p>
</blockquote></td>
<td><blockquote>
<p>.065*H-(0.029*AGE)-5.459</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT MALE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HB</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>HB+10.22/(1.7*HB)*ACT MEDPATIENT '72</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MVV</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>.924*HT-(.82*AGE)-10.7 MEDPATIENT '67 F</p>
</blockquote></td>
<td><blockquote>
<p>EMALE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MVV</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1.356*HT-(1.26*AGE)-21.4 BOREN &amp; KOREY '66</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NONE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>.0216*HT+(.0207*AGE)-2.84 MEDPATIENT '82</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NONE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ACT-(.1*ACT)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NONE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ACT-(.08*ACT)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PF</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>2.63*HT-(1.84*AGE)+14.06/60 MEDPATIENT '64</p>
</blockquote></td>
<td><blockquote>
<p>FEMALE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PF 3.9\*HT-(3\*AGE)-49.36/60 MEDPATIENT '64 MALE

> RV .009\*AGE+(.032\*HT)-3.90 MEDPATIENT '58 FEMALE

> RV .0197\*HT+(.0201\*AGE)-2.421 MEDPATIENT '82 FEMALE

> RV .017\*AGE+(.027\*HT)-3.447 MEDPATIENT '58 MALE

> TLC .0795\*HT+(.0032\*AGE)-7.333 MEDPATIENT '82 MALE TLC .078\*HT-7.3 MEDPATIENT ONE & TWO '66 MALE

> TLC .78\*HT-7.30 MEDPATIENT ONE & TWO '66 MALE

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 23%" />
<col style="width: 37%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TLC,VC,FVC,FEV1,FRC,RV,FEF2575</p>
</blockquote></td>
<td><blockquote>
<p>ACT-(.132*ACT)</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT THREE &amp; FOUR '74</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TLC,VC,FVC,FEV1,FRC,RV,FEF2575</p>
</blockquote></td>
<td><blockquote>
<p>ACT-(.11*ACT)</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT THREE &amp; FOUR '74</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TLC,VC,FVC,FEV1,FRC,RV,FEF2575</p>
</blockquote></td>
<td><blockquote>
<p>PRED-(.132*PRED)</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT THREE &amp; FOUR '74</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TLC,VC,FVC,FEV1,FRC,RV,FEF2575 PRED-(.132\*PRED) MEDPATIENT THREE & FOUR '74

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 28%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VC, FVC</p>
</blockquote></td>
<td><blockquote>
<p>.046*HT-(.024*AGE)-2.852</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT '71</p>
</blockquote></td>
<td><blockquote>
<p>FEMALE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VC, FVC</p>
</blockquote></td>
<td><blockquote>
<p>.049*HT-(.0216*AGE)-3.59</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT '81</p>
</blockquote></td>
<td><blockquote>
<p>FEMALE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VC, FVC</p>
</blockquote></td>
<td><blockquote>
<p>.0592*HT-(.025*AGE)-4.241</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT '71</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VC, FVC</p>
</blockquote></td>
<td><blockquote>
<p>.06*HT-(.0214*AGE)-4.65</p>
</blockquote></td>
<td><blockquote>
<p>MEDPATIENT '81</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> You may enter a new PFT FORMULA, if you wish

> Answer must be 3-50 characters in length.

> Select the Predicted Value Formula: TLC

> 1 TLC .079\*HT-(.008\*AGE)-7.49 MEDPATIENT '58 FEMALE

> 2 TLC .0590\*HT-4.537 MEDPATIENT '82 FEMALE

> 3 TLC .094\*HT-(.015\*AGE)-9.167 MEDPATIENT '58 MALE

> 4 TLC .78\*HT-7.3/60 MEDPATIENT ONE AND TWO'66 MALE

> 5 TLC .0795\*HT+(.0032\*AGE)-7.333 MEDPATIENT '82 MALE

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: 1 .079\*HT-(.008\*AGE)-7.49 MEDPATIENT '58 FEMALE

> PFT FORMULA: .079\*HT-(.008\*AGE)-7.49 Replace \<RET\>

> TYPE: TLC// \<RET\>

> REFERENCE: GOLDMAN '58// ^

> Select the Predicted Value Formula: .079\*HT-(.008\*AGE)-7.49 MEDPATIENT '58

> FEMALE

> PFT FORMULA: .079\*HT-(.008\*AGE)-7.49 Replace \<RET\>

> TYPE: TLC// ?

> Answer must be 2-35 characters in length.

> TYPE: TLC// ??

> This field is used to indicate which elements of the PFT the formula applies to. For example, a TLC in this field would indicate that this formula is used for Total Lung Capacity predicted values. This field is used as a screen when the formula set is edited.

> TYPE: TLC// \<RET\>

> REFERENCE: MEDPATIENT '58// ??

> This field contains the name of the person developing the formula and the year in which it was developed.

> REFERENCE: MEDPATIENT '58// \<RET\>

> SEX TYPE: FEMALE// ??

> This field indicates whether the formula applies to male or female patients.

> Choose from:

> M MALE

> F FEMALE

> SEX TYPE: FEMALE// \<RET\>

> RACE TYPE: ??

> This field is used for doing race corrections on certain PFT elements. It indicates whether the formula for race correction applies to Black or Oriental patients.

> Choose from:

> B BLACK

> O ORIENTAL

> RACE TYPE: \<RET\>

> CI: ??

> This field identifies the confidence interval. It is subtracted from the predicted value to give a 95% confidence interval. Not all elements will have confidence intervals.

> CI: \<RET\>

> SEE: COEF. VAR. 11, R=.724 Replace ??

> This field identifies the standard error equivalent, ie the amount of variance in the formula.

> SEE: COEF. VAR. 11, R=.724 Replace \<RET\>

> METHOD: CLOSED CIRCUIT H2// ??

> This field identifies the method by which the formula was calculated.

> METHOD: CLOSED CIRCUIT H2// \<RET\>

> DEMOGRAPHICS: SOUTH AFRICA, RACIAL COMP. NOT SPEC.

> Replace ??

> This field identifies the type of demographics on which the study was done which resulted in the formula: ie, Black Males, White Females, etc.

> DEMOGRAPHICS: SOUTH AFRICA, RACIAL COMP. NOT SPEC.

> Replace \<RET\>

> SMOKERS INCLUDED: YES// ??

> This field identifies whether or not smokers were included in the study that resulted in the formula.

> Choose from:

> Y YES

> N NO

> SMOKERS INCLUDED: YES// \<RET\>

> ALTITUDE: MEDIAN 5760 FT.// ??

> This field identifies the altitude at which the study that resulted in the formula was done.

> ALTITUDE: MEDIAN 5760 FT.// \<RET\>

> Select the Predicted Value Formula: \<RET\>

> Associate Predicted Value Formulas

> Select PFT Predicted Values Formulas Option: 2 Associate Predicted Value Formulas

> Select the SEX for which the Predicted Value will be applied: MALE

> NAME: MALE// ??

> This field identifies the name for the set of formulas used to calculate predicted values and corrections. Current entries are Male and Female.

> NAME: MALE// \<RET\>

> TLC: .078\*HT-7.3// ??

> This field contains the formula used for calculating the predicted value of the 'Total Lung Capacity'.

> Choose from:

> .078\*HT-7.3 REFERENCE: MEDPATIENT ONE & TWO'66

> SEX: Male

> CI: 1.436 SEE: .87

> METHOD: CLOSED CIRCUIT HE & N2 WASHOUT

> DEMOGRAPHICS: VA COOP-MALE-RACIAL COMP. NOT SPEC.

> SMOKERS INCLUDED: YES ALTITUDE: MIXED

> .0795\*HT+(.0032\*AGE)-7.333 REFERENCE: MEDPATIENT '82

> SEX: Male

> CI: 1.609 SEE: .792

> METHOD: SINGLE BREATH HE DILUTION

> DEMOGRAPHICS: SALT LAKE, UTAH-WHITE

> SMOKERS INCLUDED: NO ALTITUDE: 1400M

> .094\*HT-(.015\*AGE)-9.167 REFERENCE: MEDPATIENT '58

> SEX: Male

> CI: SEE: COEF. VAR. 10, R=0.774

> METHOD: CLOSED CIRCUIT H2

> DEMOGRAPHICS: SOUTH AFRICA, RACIAL COMP. NOT SPEC.

> SMOKERS INCLUDED: YES ALTITUDE: MEDIAN 5760 FT.

> ^

> TLC: .078\*HT-7.3// \<RET\>

> VC: .06\*HT-(.0214\*AGE)-4.65// ??

> This field contains the formula for calculating the predicted value of the 'Vital Capacity'

> Choose from:

> .0592\*HT-(.025\*AGE)-4.241 REFERENCE: MEDPATIENT '71

> SEX: Male

> CI: 1.221 SEE: 0.74

> METHOD: STEADWELLS

> DEMOGRAPHICS: OREGON-WHITE

> SMOKERS INCLUDED: NO ALTITUDE: SEA LEVEL

> .06\*HT-(.0214\*AGE)-4.65 REFERENCE: CRAPO '81

> SEX: Male

> CI: SEE: 0.644

> METHOD: WATER SEAL

> DEMOGRAPHICS: UTAH-WHITE

> SMOKERS INCLUDED: NO ALTITUDE: 4200 FT

> .065\*H-(0.029\*AGE)-5.459 REFERENCE: MEDPATIENT SEX: Male

> CI: .777 SEE: 0.471

> METHOD: STEADWELLS

> DEMOGRAPHICS: ILLINOIS

> SMOKERS INCLUDED: ALTITUDE:

> ^

> VC: .06\*HT-(.0214\*AGE)-4.65// \<RET\> FVC: .06\*HT-(.0214\*AGE)-4.65// \<RET\> FRC: .032\*HT-2.94// \<RET\>

> RV: .019\*HT+(.0115\*AGE)-2.24// \<RET\> FEV1: .0414\*HT-(.0244\*AGE)-2.190// \<RET\> PF: 3.9\*HT-(3\*AGE)-49.36/60// \<RET\>

> FEF25-75: .0204\*HT-(.038\*AGE)+2.133// \<RET\>

> MVV: 1.356\*HT-(1.26\*AGE)-21.4// \<RET\>

> DLCO-SB: 12.9113-(.229\*AGE)+(.1672\*HT)// \<RET\>

> TLC,VC,FVC,FEV1 CORR.-BLACK: PRED-(.132\*PRED)// \<RET\>

> <u>TLC,VC,FVC,FEV1 CORR.-ORIENTAL:</u> ACT-(.11\*ACT)// \<RET\>

> FRC,RV CORR.-BLACK: PRED-(.132\*PRED)// \<RET\>

> FEF25-75 RACE CORR.-BLACK: PRED-(.132\*PRED)// \<RET\>

> MVV CORR.-BLACK: \<RET\>

> MVV CORR.-ORIENTAL: \<RET\>

> COHB CORRECTION: ACT\*(1+(COHB/100))// \<RET\>

> HB CORRECTION: HB+10.22/(1.7\*HB)\*ACT// \<RET\>

> Select the SEX for which the Predicted Value will be applied: \<RET\>

## HEMATOLOGY MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> Choose the Hematology Menu option from the main Medicine menu.

> Upon accessing the Hematology module, the user is generally presented with the following menu.

> 1 Enter/Edit Hematology Procedures

> 2 Enter/Edit Hematology Procedures (Screen)

> 3 Hematology Report

> 4 Summary of Patient Procedures

> 5 Problem Oriented Consult Menu

> 6 Image Capture

> 7 Brief Enter/Edit of Hematology Procedures

> 8 Brief Hematology Enter/Edit (Screen)

> 9 Brief Hematology Report

> 10 Release Control Options (Hematology)

### Enter/Edit Hematology Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is a FileMan based line entry system, used to enter Bone Marrow Aspirates (BMA) and Bone Marrow Biopsies (BMB). The screen entry option (option 2 or 8) covers the same information as its line entry counterpart (option 1 or 7).

### Brief Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option accesses the same fields (unless otherwise noted) as the Brief Enter/Edit (Screen) option. Only the Brief Enter/Edit (Screen) option is shown. The field descriptions for the brief screens are

> the same as for the corresponding field on the full screens and are not reshown.

### Brief Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Brief Reports print a report of the information that was entered using the any Enter/Edit options. The user is asked to enter the date and time of the procedure and the device on which to print

> Use of these options is usually restricted by security keys given to clinical managers. A full description of the options can be found in the Orientation and the Package Management sections of this manual under Release Control.

### Release Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter/Edit Hematology Procedures (Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hematology Enter/Edit (Screen 1 of 4)

> HEMATOLOGY ENTER/EDIT (SCREEN 1 of 4) 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 PROCEDURE(R):......... 4 ANATOMIC SITE:....................

> 5 WARD/CLINIC:..............................

> 6 PERFORMED BY:..............................

> 7 DATE PERFORMED:.................

> 8 APPROVED BY:..............................

> 9 APPROVAL DATE:.................

> 10 INDICATION(M):................... 11 OTHER INDICATION(W):.....

> 12 ORIGINAL CONSULT DATE:.................

> 13 PROVISIONAL DX(M):.............................................

> 14 PROVISIONAL DX REMARKS:.......................................

> 1\. Specify the time and date of entry.

> 2\. Identifies the medical patient's name.

> 3\. This field is a pointer to the procedure location file.

> 4\. This field is a pointer to the anatomy file.

> 5\. Give the in-house location of the patient.

> 6\. Identify the health care provider who performed this procedure.

> 7\. Enter the procedure date.

> 8\. Specify the health care provider who approved the results.

> 9\. Indicate the date on which the results were approved.

> 10\. Select an entry from the indication file.

> 11\. Summarize any other indications.

> 12\. Enter the date of consult.

> 13\. Provide the provisional diagnosis.

> 14\. Explain provisional diagnosis in this free text field

> Hematology Enter/Edit (Screen 2 of 4)

> HEMATOLOGY ENTER/EDIT (SCREEN 2 of 4) 09/16/93

> 1 NUMBER OF PIECES:.... 2 PIECE 1:.... 3 PIECE 2:.... 4 PIECE 3:....

> 5 PIECE 4:.... 6 PIECE 5:.... 7 FIXATIVE:........

> 8 BIOPSY COMMENTS:.........................................

> 9 DECALCIFICATION OF SPECIMEN:.... 10 SPECIMEN SUBMITTED FOR PLASTIC:....

> 11 CELLULARITY:......... 12 CELLULARITY MODIFIER:..........

> 13 M:E RATIO:...... 14 IRON STORES:.... 15 MEGAKARYOCYTES:.........

> 16 MEGAKARYOCYTES MODIFIER:..........

> 17 PERIPHERAL BLOOD SMEAR:.................................

> 18 DIFF(Y/N):....

> 1 Enter the number of pieces (1-5).

> 2-6 Enter the length in millimeters of each piece separately.

> 7\. Choose from F(Formalin), B (B-5), Z (Zenker's), C (Carnoy's).

> 8\. This is a free text field for entering any pertinent biopsy comments.

> 9\. Specify whether there is any decalcification of the specimen.

> 10\. Identify the specimen submitted for plastic field.

> 11\. Select one of a set of descriptors of the occurrence of cellularity.

> 12\. Select one of a set of adjectives used to further define cellularity.

> 13\. Give the M:E ratio.

> 14\. Choose from a set of positive values.

> 15\. Supply the megakaryocyte count.

> 16\. Enter the megakaryocyte count modifier.

> 17\. Document the results of the peripheral smear.

> 18\. A "Yes" answer will cause the fields 1-20 on the next screen (Hematology Enter/Edit Screen

> 3 of 4) to be required. A "No" answer will cause the curser to jump to field 21 of the that screen.

> Hematology Enter/Edit (Screen 3 of 4)

> HEMATOLOGY ENTER/EDIT (SCREEN 3 of 4) 09/16/93

> 1 NO. CELLS COUNTED:.... 2 NEUTROPHILS:...... 3 BANDS:......

> 4 METAMYELOCYTES:...... 5 MYELOCYTES:...... 6 PROMYELOCYTES:......

> 7 MYELOBLASTS:...... 8 EOSINOPHILS:...... 9 BASOPHILS:......

> 10 LYMPHOCYTES:...... 11 ORTHOCHROMATIC NORMOBLASTS:......

> 12 POLYCHROMATIC NORMOBLASTS:...... 13 BASOPHILIC NORMOBLASTS:......

> 14 PRONORMOBLASTS:...... 15 LYMPHOBLASTS:...... 16 PLASMA CELLS:......

> 17 MONOCYTES:...... 18 HISTIOCYTES:...... 19 OTHER CELL TYPE COUNT:....

> 20 OTHER CELL TYPE:..................................................

> 21 MICROSCOPIC DESCRIPTION(M):................................

> 22 MICRO DESCRIPTION REMARKS(W):.....

> 1\. Give the number of cells counted.

> 2\. Respond with the neutrophil count (0-100).

> 3\. Enter the number of bands found.

> 4-7 Supply the metamyelocyte, myelocyte, promyelocyte, and myeloblast counts.

> 8-10 Indicate the number of eosinophils, basophils, and lymphocytes found.

> 11\. Enter the normoblast count.

> 12-13 Indicate the polychromatic and basophilic normoblast counts.

> 14\. Give the pronormoblast count.

> 15\. Show the number of lymphoblasts found.

> 16-18 Supply the plasma cell, monocyte, histiocytes counts.

> 19-20 Identify the other cell type count and descriptor.

> 21\. Enter the microscopic description.

> 22\. Explain the micro description.

> The total of all the above cells should equal 100 or 200. If this total is anything other than 100 or

> 200, a message will appear alerting the user to this fact.

> Differential adds up to (total number of all cells entered)

> Hematology Enter/Edit (Screen 4 of 4)

> HEMATOLOGY ENTER/EDIT (SCREEN 4 of 4) 09/16/93

> 1 FINAL DIAGNOSIS(M):..............................

> 2 FINAL DIAGNOSIS REMARKS(W):.....

> 3 COMPLICATIONS(M):..............................

> 4 SUMMARY:..........................

> 5 PROCEDURE SUMMARY:.......................................

> 1\. Enter Medical diagnosis.

> 2\. Respond with diagnostic remarks.

> 3\. Explain document procedural difficulties.

> 4\. Summarize the results of this procedure.

> 5\. This summary appears on the Summary of Patient Procedures.

### Hematology Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option produces a printed report of a procedure entered through the Enter/Edit option. The user cannot print a report through this option until it is released from printing through the Release

> Report option of the Hematology Management options Menu.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult Menu is discussed in the Problem Oriented Consult Menu section of this manual.

### Image Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Hematology Menu contains an Image Capture option which allows a procedure image to be attached to a patient record. This option is only available to users at a workstation. Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for Generalized Procedures.

### Brief Hematology Enter/Edit (Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### > Brief Hematology Screen 09/16/93

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 PROCEDURE:..........

> 4 INDICATION(M):..............................

> 5 PROVISIONAL DX(M):..............................

> 6 CELLULARITY:.........

> 7 IRON STORES:....

> 8 MEGAKARYOCYTES:.........

> 9 FINAL DIAGNOSIS(M):..............................

> 10 SUMMARY:..........................

> 11 PROCEDURE SUMMARY:....................................

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Hematology screens previously displayed and in the Hematology Quick Reference Guide.

## PACEMAKER MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> Choose the Pacemaker Menu option from the main Medicine menu.

> Upon accessing the Pacemaker Module, the following menu is usually displayed.

> 1 Enter/Edit Menu (Line Entry)

> 2 Enter/Edit Menu (Screen Entry)

> 3 Summary of Patient Procedures

> 4 Report Menu

> 5 Pacemaker Management Menu

### Documentation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options that are common to all procedure menus in the Pacemaker module are documented in this section rather than being repeated for each procedure.

> Use of these options is usually restricted by security keys given to clinical managers. A full description of the options can be found in the Orientation and the Package Management sections of this manual under Release Control.

#### Release Control

### Enter/Edit Menu (Line Entry)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows full line entry or brief line entry. It accesses the same fields (unless otherwise noted) as the corresponding screen entry options. The field descriptions are the same as for the corresponding screen.

### Enter/Edit Menu for Screen Entry of Pacemaker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Pacemaker Enter/Edit Menu has the following options.

> 1 Combined Implant/Leads Enter/Edit

> 2 Generator Implant/Explant Enter/Edit

> 3 A-Lead Implant/Explant Enter/Edit

> 4 V-Lead Implant/Explant Enter/Edit

> 5 Surveillance Enter/Edit

> 6 Demographic Data Enter/Edit

> 7 Brief Generator Enter/Edit (Screen)

> 8 Brief A-Lead Imp/Exp Enter/Edit (Screen)

> 9 Brief V-Lead Imp/Exp Enter/Edit (Screen)

> 10 Brief Surveillance Enter/Edit (Screen)

> Combined Implant/Leads Enter/Edit

> This option is used to combine options 2, 3 and 4 and enter all data at once. Depending upon the answer to the "Type Of Lead" prompt (A, V, AV) only the appropriate questions for A and/or V leads will available. This option is not documented separately in this manual.

> Generator Implant Enter/Edit (Screen 1 of 2)

> GENERATOR IMPLANT ENTER/EDIT (SCREEN 1 of 2) 09/16/93

> 1 DATE/TIME OF IMPLANT:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 PACEMAKER MODEL:..............................

> 4 PACEMAKER SERIAL NUMBER:............ 5 PACING MODE:.....

> 6 HOSP WHERE IMPLANT OCCURRED:..............................

> 7 TRANSMITTER MODEL:..............................

> 8 LEADS (A,V,AV):...........

> 9 IMPLANTATION ETIOLOGY:..........................

> 10 FIRST SCHEDULED F/U VISIT:.................

> 11 NON-MAG RATE AT BEGIN-OF-LIFE:..... 12 MAGNET RATE AT BEGIN-OF-LIFE:.....

> 13 NON-MAG PULSE WIDTH AT B-O-L:...... 14 MAGNET PULSE WIDTH AT B-O-L:......

> 15 OTHER BEGIN-OF-LIFE INDICATOR:.........................

> 16 NON-MAG RATE AT END-OF-LIFE:..... 17 MAGNET RATE AT END-OF-LIFE:.....

> 18 NON-MAG PULSE WIDTH AT E-O-L:...... 19 MAGNET PULSE WIDTH AT E-O-L:......

> 1\. Enter the date and time of the generator implant. This allows analysis based on time.

> 2\. Identifies the patient.

> 3\. Identify the device by the manufacturer's production (model) name.

> 4\. Enter the serial number of the specific device.

> 5\. Define the operation established with the device.

> 6\. Specify the facility where the implant procedure was performed.

> 7\. Identify the transmitter by the manufacturer's production name.

> 8\. Describe the placement/type of conductors established (A, V, AV).

> 9\. Summarize historical patient data.

> 10\. Explain the circumstances of the primary visit.

> 11-12 Enter initial non-mag and magnet rates.

> 13-14 Give initial non-mag and magnet widths.

> 15\. Supply documentation on other initial findings.

> 16-17 Indicate terminal non-mag and magnet rates.

> 18-19 Identify terminal non-mag and magnet widths.

> Generator Implant Enter/Edit (Screen 2 of 2)

> GENERATOR IMPLANT ENTER/EDIT (SCREEN 2 of 2) 09/16/93

> 1 OTHER END-OF-LIFE INDICATOR:.........................

> 2 NO. PULSE GENERATORS:.... 3 DATE OF LAST PREVIOUS IMPLANT:.........

> 4 DATE OF INCIPIENT MALFUNCTION:.................

> 5 <u>PACING FAILURE (EKG)(M):</u>............... 6 EXPLANT DATE:...........

> 7 REASON FOR GENERATOR CHANGE:..................................

> 8 COMMENTS(W):.....

> 9 PROCEDURE SUMMARY:............................................

> 10 SUMMARY:.......... 11 ATTENDING PHYSICIAN:...............

> 12 FELLOW-1st:..............................

> 13 FELLOW-2nd:..............................

> 1\. Document other terminal parameters.

> 2\. Furnish the sequential value of this generator.

> 3\. Enter the date of the previous implantations.

> 4\. Give the date of malfunction.

> 5\. Enter pacing failures information.

> 6\. Provide the date of generator removal.

> 7\. Summarize the reasons for change.

> 8\. Furnish any other information or documentation pertinent to the procedure..

> 9\. This required summary (up to 79 characters) will appear on the Summary of Patient

> Procedures.

> 10\. This is a required summary of the implant (Abnormal, Borderline, Normal) and will appear on the Summary of Patient Procedures.

> 11-13 Enter the names of the attending Physician, 1st and 2nd Fellows..

> The explant data for the generator is also entered through this option. Whenever a user wishes only to enter explant data for the pacemaker, the user can reach the explant fields by calling up the generator by its implant date (or by patient name, which will list all implants performed on a patient) and then typing "^E" at the first prompt. Note that the Type of Lead field is a required field and the data in this field (i.e. A-Lead, V-Lead, or Both A and V Leads) is used to determine the set of questions asked in the Pacemaker Surveillance Enter/Edit option.

> Pacing Failure (EKG) Subscreen of Generator Implant Enter/Edit (Screen 2 of 2)

> PACING FAILURE (EKG) 09/16/93

> 1 PACING FAILURE (EKG):...............

> 2 DATE OF FAILURE:.................

> 1\. Document any pacing failures.

> 2\. Enter the date of failure.

> A-Lead Implant/Explant Enter/Edit (Screen 1 of 1)

> A LEAD IMPLANT ENTER/EDIT 09/16/93

> 1 DATE/TIME OF IMPLANT:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 A LEAD MODEL:.................... 4 A LEAD SERIAL NUMBER:............

> 5 A LEAD THRESHOLD IN VOLTS:..... 6 A LEAD THRESHOLD IN mA's AT .5:.....

> 7 A LEAD RESISTANCE (OHMS) AT 5V:......... 8 P WAVE AMPLITUDE (MV):.....

> 9 A LEAD PSA USED:..............................

> 10 EXPLANT DATE:.................

> 11 A LEAD EXPLANT REASON:.........................................

> 12 COMMENTS(W):.....

> 13 PROCEDURE SUMMARY:...........................................

> 14 SUMMARY:........

> 15 ATTENDING PHYSICIAN:..............................

> 16 FELLOW-1st:..............................

> 17 FELLOW-2nd:..............................

> This option is used to enter or edit data dealing with the implant or explant of Atrial Leads for a generator.

> 1\. Enter the date and time of the implant. This allows analysis based on time.

> 2\. Identifies the patient.

> 3\. Identify the device by the manufacturer's production (model) name.

> 4\. Give the serial number of the specific device.

> 5-6 Document the initial threshold parameters.

> 7\. Enter the A lead resistance (OHMS) at 5V.

> 8\. Specify the R wave amplitude (mV).

> 9\. Indicate the A Lead PSA used.

> 10 Enter the date of lead removal.

> 11\. Indicate reasons for explant rationale.

> 12\. Further explain reasons for removal.

> 13\. This field will be displayed on the medical procedure summary report.

> 14\. Summarize the results of the procedure.

> 15\. Enter the name of the attending physician.

> 16-17 Enter the names of the 1st and 2nd Fellows.

> V-Lead Implant/Explant Enter/Edit (Screen 1 of 1)

> V LEAD IMPLANT ENTER/EDIT 09/16/93

> 1 DATE/TIME OF IMPLANT:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 V LEAD MODEL:.................... 4 V LEAD SERIAL NUMBER:............

> 6 V LEAD THRESHOLD IN mA'S AT .5:..... 5 V LEAD THRESHOLD IN VOLTS:.....

> 7 V LEAD RESISTANCE (OHMS) AT 5V:......... 8 R WAVE AMPLITUDE (mV):.....

> 9 V LEAD PSA USED:..............................

> 10 EXPLANT DATE:.................

> 11 V LEAD EXPLANT REASON:........................................

> 12 COMMENTS(W):.....

> 13 PROCEDURE SUMMARY:...........................................

> 14 SUMMARY:........

> 15 ATTENDING PHYSICIAN:..............................

> 16 FELLOW-1st:..............................

> 17 FELLOW-2nd:..............................

> This option is used to enter or edit data dealing with the implanting or explanting of Ventricular

> Leads for a generator.

> 1\. Supply the date/time that the procedure was entered into the database.

> 2\. Identifies the patient.

> 3\. Give the model name of the V Lead Model.

> 4\. Enter the V Lead Serial number.

> 5\. Express the V Lead threshold in volts.

> 6\. Indicate the V lead threshold parameters.

> 7\. Provide the current rate parameter (OHMS) at 5V.

> 8\. Give the current rate parameter in mV.

> 9\. Identify the V Lead PSA used.

> 10\. Specify the explant date.

> 11\. Indicate the V lead explant rationale.

> 12\. Enter any comments pertaining to this procedure.

> 13\. This field is for display on the medicine procedure summary report.

> 14\. Provide a summary of the procedure.

> 15\. Enter the name of the attending physician.

> 16-17 Enter the names of the 1st and 2nd Fellows.

> Surveillance Enter/Edit

> This option is used to enter/edit follow-up and re-programming data for Pacemakers. The user

> selects the type of surveillance (Phone or Clinic). The user will be asked a more comprehensive set of questions if the surveillance is a "Clinic" surveillance. This option interacts with the Leads field of the Generator Implant file, such that if "A-Lead" is entered in the Leads field, no fields dealing with V-Lead information will be asked. Alternately, if the patient has "V-Lead" entered in the Leads field of the Generator Implant file, no fields dealing with A-Lead information will be asked. All fields will be asked if the patient has "Both A and V Leads" entered in the Leads field of the Generator Implant file.

> The Surveillance screens are combined A and V leads for a Clinic surveillance.

> Screens and descriptions given in this manual will be for the Clinic, Both A and V Leads since these are the most comprehensive. All fields asked in Single A or V Lead or Telephone screens are covered within these descriptions.

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 1 of 3)

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 1 of 3) 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT(R):..............................

> 3 CALLER:..............................

> 4 DATA GATHERING MODE(R):.........

> 5 PULSE INTERVAL (MSEC) WO MAG:.... 6 RATE WO MAG(C):.........

> 7 PULSE INTERVAL (MSEC) W MAG:.... 8 RATE W MAG(C):.........

> 9 A-V DELAY WO MAG (MSEC):.... 10 A-V DELAY W MAG (MSEC):....

> 11 BATTERY VOLTAGE:..... 12 RESISTANCE:.....

> 13 BASIC RHYTHM:..................................................

> 14 PERCENT OF PACED BEATS:.... 15 REPROGRAMMED RATE:.....

> 16 REPROG. UPPER RATE LIMIT:.... 17 REPROGRAMMED A-V DELAY (MSECS):....

> 18 REPROGRAMMED HYSTERESIS:.... 19 REPROGRAMMED PACING MODE:.....

> 20 REASON FOR REPROGRAMMING:....................................................

> 1\. Enter the date and time of the procedure.

> 2\. Identifies the Patient's name.

> 3\. Identify the surveillance operator.

> 4\. Defines the surveillance technique.

> 5-8 Indicate current rate parameters.

> 9-10 Enter current rhythm parameters.

> 11\. Give current battery voltage.

> 12\. Indicate the current ohms parameter.

> 13\. Enter the current rhythm.

> 14\. Provide the current rate of generator activity.

> 15-16 Document the rate adjustments.

> 17\. Indicate rhythm adjustments.

> 18\. Enter hysteresis adjustments.

> 19\. Specify any adjustment to device operations.

> 20\. Explain the adjustment rationale

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 2 of 3)

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 2 of 3) 09/16/93

> 1 PULSE WIDTH (ATRIAL-MSEC):.... 2 MEASURED A-LEAD AMPLITUDE (MV):.....

> 3 RATIO (T/L) (ATRIAL):...... 4 THRESHOLD WIDTH (ATRIAL):....

> 5 THRESHOLD AMPLITUDE (ATRIAL):.....

> 6 CAPTURE (ATRIAL):..............

> 7 SENSE (ATRIAL):.............. 8 REPR.PULSE WIDTH (ATRIAL-MSEC):....

> 9 REPROG. A-AMPLITUDE (VOLTS):.... 10 REPR.SENSITIVITY(ATRIAL-VOLTS):....

> 11 REPR.ATRIAL REFRACTORY PERIOD:.... 12 PULSE WIDTH (VENTRICLE-MSEC):....

> 13 MEASURED V-LEAD AMPLITUDE (MV):..... 14 RATIO (T/L) (VENTRICLE):......

> 15 THRESHOLD WIDTH (VENTRICLE):..... 16 THRESHOLD AMPLITUDE (VENT.):.....

> 17 CAPTURE (VENTRICULAR):..............

> 18 SENSE (VENTRICULAR):..............

> 19 REPR.PULSE WIDTH (VENT-MSEC):.... 20 REPROGR. V-AMPLITUDE (VOLTS):....

> 21 REPR.SENSITIVITY (VENTR.-MV):.... 22 REPR. VENT. REFRACTORY PERIOD:....

> 1\. Indicate pulse segment rate parameter.

> 2\. Enter atrial lead voltage.

> 3\. Specify the performance ratio.

> 4\. Provide the atrial threshold parameter.

> 5\. Enter the atrial voltage threshold.

> 6-7 Indicate atrial capture, and sense.

> 8\. Document pulse segment adjustment.

> 9-11 Specify atrial voltage, sense, and refraction adjustments.

> 12\. Give the pulse segment rate parameter.

> 13\. Indicate the ventricular lead voltage.

> 14\. Give the performance ratio.

> 15\. Enter the ventricular threshold.

> 16\. Indicate the ventricular voltage threshold.

> 17-18 Identify ventricular capture, and sense adjustments.

> 19\. Specify any pulse segment adjustments.

> 20-22 Document ventricular voltage, sense, and refraction adjustments.

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 3 of 3)

> Pacemaker Surveillance (Clinic, Both A&V Leads) (Screen 3 of 3) 09/16/93

> 1 FOLLOWUP COMMENT:............................................................

> 2 FAST OR SLOW CHECK:.......... 3 NEXT FOLLOW-UP DATE:.................

> 4 COMMENTS(W):..... 5 SUMMARY:..........

> 6 PROCEDURE SUMMARY:...........................................................

> 7 ATTENDING PHYSICIAN:..............................

> 8 FELLOW:..............................

> 1 Enter any pertinent follow-up comments.

> 2\. Identify whether this is a fast or slow check.

> 3\. Indicate the scheduled follow-up date.

> 4\. Enter any other comments.

> 5\. This required summary of the surveillance (Normal, Abnormal, or Borderline) will appear on the Summary of Patient Procedures.

> 6\. This is a required summary (1 to 79 characters) of the surveillance which will appear on the

> Summary of Patient Procedures.

> 7\. Enter the name of the attending physician.

> 8\. Enter the names of the 1st Fellow.

> Pacemaker Demographic Data Enter/Edit (Screen 1 of 1)

> PACEMAKER DEMOGRAPHIC DATA 09/16/93

> 1 NAME(R):..............................

> 2 PACING INDICATION(M):..............................

> 3 <u>RISK FACTOR (PACE)(M):</u>..............................

> 4 PSC STATUS:........................

> 5 TELEPHONE FOLLOWUP PROVIDED BY:.........................

> 6 DATE OF INITIAL IMPLANT:.................

> 7 INDICATION FOR FILE CLOSURE:............................

> 8 CAUSE OF DEATH:..................................

> 9 SUDDENNESS OF DEATH:..................................

> 10 DISCHARGE (PACEMAKER) REASON:.........................

> 11 DATE OF FILE CLOSURE:.................

> 12 REASON FOR FILE CLOSURE:.....................................

> This option is used to enter follow-up data on a patient. Under this option, the pacing indication, risk factor, PSC status, and telephone follow-up center are entered for a patient using a FileMan- based line entry system. The date of the initial pacemaker implant and information for patient file closure are also entered using this option.

> 1\. Displays the patient's name

> 2\. Indicate the medical rationale for electronic cardiac regulation.

> 3\. Select the morbidity factors which this patient is most susceptible to in regards to this procedure.

> 4\. Give the Pacemaker Surveillance Center status.

> 5\. Enter the location for a follow-up visit.

> 6\. Enter the date of implant.

> 7\. Supply the reason for the file to be closed.

> 8\. Identify the cause of death.

> 9\. Specify the reason for the sudden death.

> 10\. Indicate the rationale for the release of the patient.

> 11\. Give the date when the file is closed.

> 12\. Furnish an extended explanation for the file to be closed.

> Risk Factor (Pace) Subscreen of Pacemaker Demographic Data Enter/Edit

> (Screen 1 of 1)

> RISK FACTOR (PACE) 09/16/93

> 1 RISK FACTOR (PACE):........................................

> 2 DATE RISK FACTOR REPORTED:.................

> 1\. Enter the morbidity factors which this patient is most susceptible to in regards to this procedure.

> 2\. This "Date format" field documents the reporting of a hazard.

#### Brief Pacemaker Screens

> Brief Generator Enter/Edit (Screen)

> Brief Pacemaker Gen Screen 09/16/93

> 1 DATE/TIME OF IMPLANT:.................

> 2 MEDICAL PATIENT:..............................

> 3 PACEMAKER MODEL:..............................

> 4 PACEMAKER SERIAL NUMBER:............ 5 PACING MODE:.....

> 6 IMPLANTATION ETIOLOGY:..........................

> 7 NON-MAG RATE AT END-OF-LIFE:...... 8 MAGNET RATE AT END-OF-LIFE:......

> 9 DATE OF INCIPIENT MALFUNCTION:.................

> 10 <u>PACING FAILURE (EKG)(M):</u>....

> 11 REASON FOR GENERATOR CHANGE:.................................

> 12 PROCEDURE SUMMARY:..............................................

> 13 SUMMARY:..........

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Pacemaker screens previously displayed and in the Pacemaker Quick Reference Guide.

> Brief A-Lead and V-Lead Imp/Exp Enter/Edit (Screen)

> Brief A-Lead Screen 09/16/93

> 1 DATE/TIME OF IMPLANT:.................

> 2 MEDICAL PATIENT:..............................

> 3 A LEAD MODEL:..............................

> 4 A LEAD SERIAL NUMBER:............ 5 A LEAD THRESHOLD IN VOLTS:.....

> 6 A LEAD THRESHOLD IN mA's AT .5:.....

> 7 A LEAD RESISTANCE (OHMS) AT 5V:......... 8 P WAVE AMPLITUDE (MV):.....

> 9 EXPLANT DATE:.................

> 10 A LEAD EXPLANT REASON:............................

> 11 COMMENTS(W):.....

> 12 PROCEDURE SUMMARY:......................................

> 13 SUMMARY:........

> Descriptions of the fields and subscreens of this screen will be found under the corresponding A- Lead screens previously displayed and in the Pacemaker Quick Reference Guide. The Brief V-Lead screen is similar.

> Brief Pacemaker Surveillance Enter/Edit (Screen)

> Brief Pacemaker Surveillance Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 PULSE INTERVAL (MSEC) WO MAG:.... 4 PULSE INTERVAL (MSEC) W MAG:....

> 5 A-V DELAY WO MAG (MSEC):.... 6 A-V DELAY W MAG (MSEC):....

> 7 BASIC RHYTHM:..................................................

> 8 PERCENT OF PACED BEATS:.... 9 REPROGRAMMED RATE:......

> 10 REPROG. UPPER RATE LIMIT:.... 11 REPROGRAMMED A-V DELAY (MSECS):....

> 12 REPROGRAMMED HYSTERESIS:.... 13 REPROGRAMMED PACING MODE:.....

> 14 REASON FOR REPROGRAMMING:....................................................

> 15 PULSE WIDTH (ATRIAL-MSEC):...... 16 MEASURED A-LEAD AMPLITUDE (MV):......

> 17 CAPTURE (ATRIAL):.............. 18 SENSE (ATRIAL):..............

> 19 REPR.PULSE WIDTH (ATRIAL-MSEC):...... 20 REPROG. A-AMPLITUDE (VOLTS):.....

> 21 REPR.SENSITIVITY(ATRIAL-VOLTS):...... 22 REPR.ATRIAL REFRACTORY PERIOD:....

> Brief Pacemaker Surveillance Screen Two 09/16/93

> 23 PULSE WIDTH (VENTRICLE-MSEC):......

> 24 MEASURED V-LEAD AMPLITUDE (MV):......

> 25 CAPTURE (VENTRICULAR):..............

> 26 SENSE (VENTRICULAR):..............

> 27 REPR.PULSE WIDTH (VENT-MSEC):......

> 28 REPROGR. V-AMPLITUDE (VOLTS):.....

> 29 REPR.SENSITIVITY (VENTR.-MV):......

> 30 REPR. VENT. REFRACTORY PERIOD:....

> 31 PROCEDURE SUMMARY:...................................

> 32 SUMMARY:..........

> Descriptions of the fields and subscreens of this screen will be found under the corresponding

> Pacemaker Surveillance screens previously displayed and in the Pacemaker Quick Reference Guide.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

Pacemaker Report Menu

### Pacemaker Report Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon accessing the Pacemaker Report Menu, the following menu is usually presented.

> 1 Generator Report

> 2 A-Lead Report

> 3 V-Lead Report

> 4 Surveillance Report

> 5 Active Patient Report

> 6 Automated Transfer of Report to National Center

> 7 Brief Generator Report

> 8 Brief A-Lead Report

> 9 Brief V-Lead Report

> 10 Brief Surveillance Report

#### Generator Report

> This option generates a printed report from the information entered through the Generator

> Implant/Explant Enter/Edit option.

#### A-Lead Report

> This option generates a printed report from the information entered through the

> A-Lead Implant/Explant Enter/Edit option.

#### V-Lead Report

> This option generates a printed report from the information entered through the

> V-Lead Implant/Explant Enter/Edit option.

#### Surveillance Report

> This option generates a printed report from the information entered through the Pacemaker

> Surveillance Enter/Edit.

> NOTE: These four reports also contain a "Patient History" section in which is printed the information entered through the Risk Factor/Status/Closure Enter/Edit option.

#### Active Patient Report

> This option generates a report of all active Pacemaker patients. An active Pacemaker patient is defined as a patient with an implant who has a PSC status of "East PSC Follow-Up", "West PSC Follow-Up", or "Registry Only". This report contains the Patient name (alphabetically), SSN, Date of Birth, PSC Status, and the Date of Implant, Manufacturer, Model Number, and Serial Number for the generator and all leads. The report also shows the type of lead (A for Atrial or V for Ventricular) for each currently implanted lead.

> This report is designed for 132 characters. A warning message alerting the user to choose a 132 character device is displayed upon entering this option.

#### Automated Transfer of Report to National Center

> This report gathers information from the last generator implant, A-Lead and/or V-Lead implant(s), and surveillance recorded in the database, and loads this information into a MailMan message. The

> user selects the patient, enters the reason for transmission of the report (i.e. Patient registration, Pacemaker, Implant, etc.) from a list provided, selects the center to which the report will be sent (Eastern, Western, or both), and allows the user to select the time the report should be sent. A copy of the report is also transmitted to the user's "IN" basket.

#### Brief Reports

> Brief reports are available for the Generator, A-Lead, V-Lead, and Surveillance Brief Enter/Edit information. Less information appears on these reports than on the full reports.

Pacemaker Management Menu

### Pacemaker Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Certain files are updated through this option. At present, the following options appear when accessing this menu.

> 1 Pacemaker Equipment Update

> 2 Manufacturer's List Update

#### Pacemaker Equipment Update

> This option is used to add new Generators, Leads, Transmitters, and PSA analyzers. The person who holds this option will be prompted to enter the Name (or Model Number), the Type of Equipment

> (i.e. Generator, etc.), and the Manufacturer of the Equipment. This option also allows the user to enter a new manufacturer (and mnemonic for that manufacturer) into the Pacemaker Manufacturer file.

#### Manufacturer's List Update

> This option allows the user to enter a new manufacturer into the Pacemaker Manufacturer file. It is important that the user enter an abbreviation into the mnemonic field, since this field is printed on the Active Patient List.

## RHEUMATOLOGY MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> Choose the Rheumatology Menu option from the main Medicine menu. The Rheumatology Menu has the following menu options.

> 1 Diagnosis Edit

> 2 Add NEW visit/display Patient Background Info.

> 3 History Narrative Edit

> 4 Print Serial Laboratory Info.

> 5 Display/Print Drug Treatment Program

> 6 Health Assessment (HAQ) Edit

> 7 Health/Physical History Edit

> 8 Physical Examination Edit

> 9 Death Admin Edit

> 10 Print Menu

> 11 Line Enter/Edit Menu  
> <span id="p137" class="anchor"></span>\*\*\> Out of order:  OUT OF ORDER

> 12 Problem Oriented Consult Menu

> 13 Image Capture

> 14 Summary of Patient Procedures

> 15 Rheumatology Management Menu

### Diagnosis Edit for Rheumatology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Diagnosis Edit option is used to edit diagnosis data for a given patient on a selected date. More than one diagnosis may be edited for a patient. An example of the screen is given below.

> Rheumatology Patient Diagnosis Screen

> Rheumatology patient diagnosis 09/16/93

> 1 DATE/TIME(R):.................

> 2 RHEUMATOLOGY PATIENT(R):..............................

> 3 <u>DIAGNOSIS(M):</u>..............................

> 4 PROCEDURE SUMMARY:......................................

> 5 SUMMARY:.........

> 6 PRIMARY PROVIDER:..............................

> 1\. Specifies the date and time that the data is first entered into the database or when the data was collected.

> 2\. Identifies the patient in the medicine file.

> 3\. Enter the diagnosis.

> 4\. The Procedure Summary field must have an entry. The information is used in the Summary of Patient Procedures display.

> 5\. Choose a summary code.

> 6\. Enter the Primary Provider.

> Diagnosis Subscreen of the Rheumatology Patient Diagnosis Screen

> Rheumatology patient diagnosis 09/16/93

> 1 DIAGNOSIS:.......................

> 2 DATE OF SYMPTOM: .................

> 1\. This allows the user to enter a diagnosis.

> 2\. Enter the date this diagnosis was made.

### Add New Visit/Display Patient Background Info.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used for displaying information for a selected patient. The screen display for this option is given below.

> Rheumatology Patient Background Info (Page 1 of 1)

> Rheumatology patient background info (page 1 of 1).

> 1 PATIENT(R):MEDPATIENT, THREE SSN:000-45-6979

> 3 ADDRESS:875 N. MICHIGAN

> 4 ADDRESS:CHICAGO, IL

> 5 STATE:ILLINOIS 6 ZIP CODE:47611

> 7 PHONE NUMBER \[H\]:

> 8 PHONE NUMBER \[W\]:

> 9 DATE OF BIRTH:OCT 7,1954

> 10 SEX:MALE

> 11 RACE:ASIAN, BLACK OR AFRICAN AMERICAN

> 12 MARITAL STATUS:

> 13 EMPLOYMENT STATUS:

> 14 OCCUPATION:

> 1\. Identifies the patient in the medicine file.

> 2\. Displays the Social Security Number. If there is a P at the end of the SSN then it is a pseudo

> SSN.

> 3-4. Displays the patient's street address.

> 5\. Displays the state in which the patient resides.

> 6\. Displays the zip code for the city in which the patient resides.

> 7\. Displays the patient's home phone number including area code.

> 8\. Displays the patient's work phone number including area code.

> 9\. Displays the patient's date of birth.

> 10\. Displays the patient's gender.

> 11\. Displays the patient's race.

> 12\. Displays the patient's current marital status.

> 13\. Displays the patient's current employment status.

> 14\. Displays the patient's current occupation.

### History Narrative Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to view and edit a patient history. The screen display for this option is given below.

> Rheumatology Narrative History Screen (Page 1 of 1)

> Rheumatology Narrative History (page 1 of 1) 09/16/93

> 1 DATE/TIME(R):.................

> 2 PATIENT(R):.............................. 3 SSN(R):..........

> Wording processing:

> 4 PRESS RETURN TO EDIT:...

> 5 HISTORY NARRATIVE(W):.....

> 1\. Specifies the date and time that the data is first entered into the database or when the data was collected.

> 2\. Identifies the patient’s name.

> 3\. Indicates the patient's Social Security Number.

> 4\. Press the Return Key.

> 5\. Enter a history narrative.

### Display Serial Laboratory Info (Screens 1-3 )

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option displays information from the DHCP Lab package for a specified date. Rheumatology Laboratory Info (Screens 1-3)

> Pg. 1 10/20/94 09:31

> CONFIDENTIAL RHEUMATOLOGY REPORT

> MEDPATIENT, FOUR 000-55-5555 NOT INPATIENT DOB: 06/17/40

> PROCEDURE DATE/TIME: 07/27/94 14:15

> \- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PATIENT LABORATORY INFORMATION

> C H E M I S T R Y : S E R O L O G Y : Aldolase Anti-DNA Antibody Albumin Anti-skeletal muscle Alkaline phosphatase Anti-RNP

> Urea nitrogen Hepatitis B Antibody Calcium Hepatitis B Antigen Cholesterol Complement CH50

> CPK Cryoglobulins Creatinine Complement Glucose 80 Complement C4

> LDH HLA B27

> PO4 IGA SGOT IGG SPGT IGM

> Pg. 2 10/20/94 09:31

> Bilirubin, total Latex fixation

> Protein, total VDRL Uric acid

> A D D I T I O N A L

> C H E M I S T R Y : U R I N E Salicylate UR Glucose T-4 UR Protein T-3 RBC/HPF

> TSH WBC/HPF

> Sodium Granular/cast/lpf Choloride WBC/CASTS/LPF Bicarbonate Creatinine Clearance

> H E M A T O L O G Y : WBC

> HGB HCT

> Pg. 3 10/20/94 09:31

> Neutrophil Bands Lymphs Monocytes Eosino

> Baso Platelet Reticulocytes Westergren ESR Protrhombin time

> Partial thromboplastin

> IRON TIBC

### Display/Print Drug Treatment Print Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option presents general information about patient drug prescriptions.

> MEDPATIENT, ONE SSN: 000789123

> 50 IRVING ST N.W. DOB: 01-24-1920

> WASHINGTON. PHONE: 555-3333

> DISTRICT OF COLUMBIA 20010 ELG: NSC CANNOT USE SAFETY CAPS

> DISABILITIES:

> REACTIONS: UNKNOWN

> PATIENT HAS ARCHIVED PRESCRIPTIONS

### Health Assessment (HAQ) Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option reproduces the Health Assessment Questionnaire, which is completed by a new rheumatology patient when beginning treatment.

> Rheumatology Health Assessment Questionnaire (Screen 1 of 1)

> Rheumatology health assessment questionnaire (page 1 of 1) 09/16/93

> 1 DATE/TIME(R):.................

> 2 PATIENT(R):.............................. 3 SSN(R):..........

> 4 QUESTIONNAIRE DATE:.................

> 5 STUDY STATUS:....................

> 6 DRUG STUDY:...........

> 7 DRESSING AND GROOMING:.... 11 HYGIENE: ....

> 8 ARISING:.... 12 REACH: ....

> 9 EATING: .... 13 GRIP: ....

> 10 WALKING:.... 14 ACTIVITIES:....

> 15 PAIN SCALE:....

> 1\. Indicates the date and time that the data is first entered into the database or when the data was collected.

> 2\. Enter the patient name in the Medicine file.

> 3\. Gives the patient's Social Security Number.

> 4\. Enter the date the questionnaire was taken.

> 5\. Enter ?? to get a list of Study Status codes from which to choose.

> 6\. The entries are the numbers 1-8 corresponding to cohort types I through VIII.

> 7-15 Indicate the level of functionality for dressing, grooming, arising, eating, walking, hygiene, reaching, grip, activities, and pain. The fields 7,11-14 take a whole number code between 0 and 3. Fields 8-10, 15 takes a number from 0-3 with one decimal place.

### Health/Physical History Edit (Screens 1-4 )

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter a patient health/physical history. Rheumatology Patient History Pages 1-4

> Rheumatology patient history (page 1 of 4) 09/16/93

> 1 DATE/TIME(R):................. 2 PATIENT(R):..............................

> 3 SSN(R):..........

> HEAD,EYES,EARS,NOSE,MOUTH:

> 4 BLURRED VISION: ...

> 5 DRY EYES: ... MUSCULOSKETAL:

> 7 HEARING DIFFICULTIES: ... 16 JOINT PAIN: ...

> 8 MOUTH SORES: ... 17 JOINT SWELLING: ...

> 9 DRY MOUTH: ... 18 LOW BACK PAIN: ...

> 10 LOSS,CHANGE IN TASTE: ... 19 MUSCLE PAIN: ...

> 11 HEADACHE: ... 20 NECK PAIN: ...

> 12 DIZZINESS: ... 21 NUMBNESS OR TINGLING: ...

> 13 FEVER: ... 22 SWELLING OF LEGS: ...

> 14 NIGHT SWEATS: ... 23 WEAKNESS OF MUSCLES: ...

> 1\. Indicates the date and time that the data is first entered into the database or when the data was collected.

> 2\. Identifies the patient in the medicine file.

> 3\. Gives the patient's Social Security Number.

> Head, Eyes, Ears, Nose, Mouth:

> In the past six months, has the patient experienced (Yes/No):

> 4\. Blurring of vision

> 5\. Dry eyes

> 6\. Ringing in ears

> 7\. Hearing difficulties

> 8\. Mouth sores

> 9\. Dry mouth

> 10\. Loss, change in taste

> 11\. Headache

> 12\. Dizziness

> 13\. Fever

> 14\. Night Sweats

> Musculoskeletal:

> In the last six months, has the patient experienced (16-23 are Yes/No):

> 15\. Stiffness in the morning and how long (in hours)

> 16\. Joint pain

> 17\. Joint swelling

> 18\. Low back pain

> 19\. Muscle pain

> 20\. Neck pain

> 21\. Numbness or tingling

> 22\. Swelling of legs

> 23\. Weakness of muscles

> Rheumatology Patient History (Page 2 of 4)

> Rheumatology patient history (page 2 of 4) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> Chest,lung,and heart: Neurologic and Psychologic:

> 24 CHEST PAIN/TAKING DEEP BREATH:... 27 DEPRESSION: ...

> 25 SHORTNESS OF BREATH: ... 28 INSOMNIA: ...

> 26 WHEEZING(ASTHMA): ... 29 NERVOUSNESS: ...

> 30 SEIZURES OR CONVULSION: ...

> 31 TIREDNESS: ...

> 32 TROUBLE REMEMBERING/THINKING:...

> Chest, Lung, Heart:

> In the last six months, has the patient experienced (Yes/No):

> 24\. Chest pain/ taking deep breath

> 25\. Shortness of breath

> 26\. Wheezing

> Neurologic and Psychologic:

> In the last six months, has the patient experienced Yes/No):

> 27\. Depression

> 28\. Insomnia

> 29\. Nervousness

> 30\. Seizures or convulsions

> 31\. Tiredness

> 32\. Trouble remembering or thinking

> Rheumatology Patient History (Page 3 of 4)

> Rheumatology patient history (page 3 of 4) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> Gastrointestinal tract: Skin:

> 33 LOSS OF APPETITE: ... 45 EASY BRUISING: ...

> 34 DIFFICULTY SWALLOWING: ... 46 FACIAL SKIN TIGHTENING: ...

> 35 NAUSEA: ... 47 HIVES OR WELTS: ...

> 36 HEARTBURN,INDIGESTION,BELCHING:... 48 LOSS OF HAIR: ...

> 37 VOMITING: ... 49 ITCHING: ...

> 38 PAIN/DISCOMFORT UPPER ABDOMEN: ... 50 RASH: ...

> 39 JAUNDICE: ... 51 RASH OVER CHEEKS: ...

> 40 LIVER: .................. 52 SKIN COLOR CHANGE IN FINGER:...

> 41 PAIN/CRAMPS LOWER ABDOMEN: ... 53 SUN SENSITIVITY: ...

> 42 DIARRHEA(FREQUENT,WATERY): ...

> 43 CONSTIPATION: ...

> 44 BLK/TARRY STOOL(NOT FROM IRON):...

> Gastrointestinal Tract:

> In the last six months, has the patient experienced (33-39 and 41-44 are Yes/No):

> 33\. Loss of appetite

> 34\. Difficulty in swallowing

> 35\. Nausea

> 36\. Heartburn, indigestion, or belching

> 37\. Vomiting in the last 6 months.

> 38\. Pain/ discomfort in the upper abdomen

> 39\. Jaundice

> 40 Liver (Brief description)

> 41\. Pain/ cramps in the lower abdomen

> 42\. Diarrhea

> 43\. Constipation

> 44\. Black/tarry stools

> Skin:

> In the last six months, has the patient experienced (Yes/No):

> 45\. Easy bruising

> 46\. Facial skin tightening

> 47\. Hives or welts

> 48\. Loss of hair

> 49\. Itching

> 50\. Rash

> 51\. Rash over cheeks

> 52\. Skin color change in finger

> 53\. Sun sensitivity

> Rheumatology Patient History (Page 4 of 4)

> Rheumatology patient history (page 4 of 4) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> Genitourinary: Blood:

> 54 URINE PROTEIN: 60 LOW WHITE BLOOD COUNT: ...

> 55 BLOOD IN URINE: ... 61 LOW PLATELETS: ...

> 56 BURNING ON URINATION: ... 62 LOW RED BLOOD COUNT: ...

> 57 KIDNEY PROBLEMS: ..................

> Females Only: ... Males Only:

> 58 PREGNANT: 63 DISCHARGE FROM PENIS: ...

> Other: 64 IMPOTENCE: ...

> 59 OTHER: .................. 65 RASH/ULCERS ON PENIS: ...

> Genitourinary:

> Has the patient experienced (54-55 Yes/No):

> 54 Indicate whether the patient has had a history of urine protein

> 55\. Blood in the urine in the last six months

> 56\. Burning on urination in the last 6 months.

> 57 Kidney Problems (Brief description)

> Females Only (Yes/No):

> 58\. Is the patient pregnant? Other:

> 59\. Enter a brief description of a relevant condition which cannot be otherwise noted. Blood (Yes/No):

> 60\. Indicate presence of low white blood count.

> 61\. Indicate presence of low platelet count.

> 62\. Indicate presence of low red blood count.

> Males Only:

> In the last six months, has the patient experienced (Yes/No):

> 63\. Discharge from the penis

> 64\. Impotence

> 65\. Rash/ulcers on the penis

### Physical Examination Edit (Screens 1-5 )

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the entry of the degree of impairment or mobility for various physical functions.

> Physical Examination-Comprehensive Visit (Pages 1 of 5)

> Physical Examination-Comprehensive Visit(Pg 1 of 5) 09/16/93

> 1 DATE/TIME:................. 2 PATIENT(R):..............................

> 3 SSN(R): ..........

> General 12 LYMPH NODE ENLARGEMENT: ........

> 4 UVEITIS/IRITIS: ........ 13 MUSCLE TENDERNESS: ........

> 5 CONJUNCTIVITIS/EPISCLERITIS: ........ 14 MUSCLE WEAKNESS-DISTAL: ........

> 6 CATARACT: ........ 15 MUSCLE WEAKNESS-PROXIMAL:........

> 7 ORAL ULCERS: ........ 16 MUSCLE ATROPHY: ........

> 8 RALES: ........ 17 PSYCHOSIS: ........

> 9 PLEURAL RUB/CLINICAL PLEURISY:........ 18 ORGANIC BRAIN SYNDROME: ........

> 10 PLEURAL EFFUSION: ........ 19 MOTOR NEUROPATHY: ........

> 11 PERICARDIAL RUB/PERICARDITIS: ........ 20 SENSORY NEUROPATHY: ........

> 1\. Indicates the date and time that the data is first entered into the database or when the data was collected.

> 2\. Identifies the patient in the Medicine file.

> 3\. Shows the patient's Social Security Number.

> General:

> Indicate the degree or presence (0=None, 1=Mild, 2=Moderate, 3=Severe) of:

> 4\. Uveitis/iritis present.

> 5\. Conjunctivitis/episcleritis present.

> 6\. Cataract.

> 7\. Oral ulcers.

> 8\. Rales.

> 9\. Pleural rub.

> 10\. Pleural effusion.

> 11\. Pericardial rub.

> 12\. Lymph node enlargement.

> 13\. Muscle tenderness.

> 14\. Distal muscle weakness.

> 15\. Proximal muscle weakness.

> 16\. Muscle atrophy.

> 17\. Psychosis.

> 18\. Organic brain syndrome.

> 19\. Motor neuropathy.

> 20\. Sensory neuropathy.

> Physical Examination-Comprehensive Visit (Screen 2 of 5)

> Physical Examination-Comprehensive Visit(Pg 2 of 5) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> Skin 32 CUTANEOUS VASCULITIS: ........

> 38 KNUCKLE ERYTHEMA: ........

> 26 TELANGIECTASIS: ........ 39 SUBCUTANEOUS CALCIFICATIONS:........

> 27 SCLERODACTYLY: ........ 40 KERATODERMIA BLENNORRHAGICA:........

> 28 SCLERODERMA-EXTREMITY: ........ 41 DACTYLITIS: ........

> 29 SCLERODERMA-GENERALIZED:........ 42 NAIL PITTING: ........

> 30 MORPHEA: ........ 43 PSORIASIS: ........

> 31 DIGITAL ULCERS: ........ 44 HEEL PAIN: ........

> Skin:

> Indicate the degree (0=None, 1=Mild, 2=Moderate, 3=Severe) of:

> 21\. Rash-Malar

> 22\. Rash-Discoid

> 23\. Rash-JRA

> 24\. Rash-sle, non-malar present

> 25\. Rash-other present

> 26\. Telangiectasis

> 27\. Sclerodactyly

> 28\. Scleroderma of the extremity

> 29\. Scleroderma, generalized

> 30\. Morphea

> 31\. Digital ulcers

> 32\. Cutaneous vasculitis

> 33\. Palpable purpura

> 34\. Skin ulcers

> 35\. Erythema nodosum

> 36\. Periungual erythema

> 37\. Heliotrope eyelids

> 38\. Knuckle erythema

> 39\. Subcutaneous calcifications presently found

> 40\. Keratodermia blennorrhagia

> 41\. Impairment of dactylitis

> 42\. Nail pitting

> 43\. Psoriasis

> 44\. Impairment of heel pain

> Physical Examination-Comprehensive Visit (Screen 3 of 5)

> Physical Examination-Comprehensive Visit(Pg 3 of 5) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

H-LEFT:

H-RIGHT:

....

....

(10 cm BASE): ....

> 48 TOPHI: .... 55 CHEST EXPANSION: ....

> 49 TENOSYNOVITIS(TENDON RUBS):........ 56 OCCIPUT-WALL: ....

> 50 TEMPORAL ARTERY TENDERNESS:........ 57 FINGER-TO-PALM CREASE-LEFT: .....

> 51 COSTOCHONDRITIS: ........ 58 FINGER-TO-PALM CREASE-RIGHT:.....

> 59 INTERINCISOR DISTANCE: .... MISCELLANEOUS 60 SCHIRMER TEST: ....

> 61 FUNCTIONAL CLASS (ACR): .............

> 62 DISEASE SEVERITY-PAT. ESTIMATE:................

> 63 DISEASE SEVERITY-PHY. ESTIMATE:................

> Rheumatic

> Does the patient have (Yes/No):

> 45\. Symmetrical arthritis

> 46\. Sub-cutaneous nodules

> 47\. Synovial (Baker's) cyst

> 48\. Tophi

> 49\. Tenosynovitis (tendon rubs)

> 50\. Temporal artery tenderness

> 51\. Impairment of costochondritis

> Measurements

> Indicate:

> 52\. Left grip strength in millimeters of mercury

> 53\. Right grip strength in millimeters of mercury

> 54\. Results of the Schober test (with a 10 cm base)

> 55\. Expansion of chest between 0 and 12 cm

> 56\. Occiput - wall between 0 and 20 cm

> 57\. Left finger-to-palm crease

> 58\. Right finger-to-palm crease

> 59\. Interincisor distance, between 0 and 60 mm

> 60\. Results of Schirmer test, between 0 and 25 mm

> Miscellaneous

> 61\. Enter ACR functional class to indicate degree of impairment.

> 62\. Indicate the Pat. estimate of disease severity.

> 63\. Choose an estimate from the list.

> Physical Examination-Comprehensive Visit (Screen 4 of 5)

> Physical Examination-Comprehensive Visit(Pg 4 of 5) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> JOINT EXAMINATION

> Left Right

> 64 FINGERS-DIP LEFT: ........ 65 FINGERS-DIP RIGHT: ........

> 66 MCPS LEFT: ........ 67 MCPS RIGHT: ........

> 68 1ST CARPOMETACARPAL L:........ 69 1ST CARPOMETACARPAL R:........

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 51%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>70 WRIST LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 71 WRIST RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>72 ELBOW LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 73 ELBOW RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>74 SHOULDER LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 75 SHOULDER RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>76 TMJ LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 77 TMJ RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>78 COSTOCHONDRAL-LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 79 COSTOCHONDRAL-RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>80 SACROILIAC-LEFT:</p>
</blockquote></td>
<td><blockquote>
<p>........ 81 SACROILIAC-RIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>........</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Joint Examination Left and Right

> Indicate the degree (0=None, 1=Mild, 2=Moderate, 3=Severe) of impairment of:

> 64\. Fingers - dip left

> 65\. Fingers - dip right

> 66\. MCPS LEFT

> 67\. MCPS RIGHT

> 68\. First carpometacarpal left

> 69\. First carpometacarpal right

> 70\. Wrist left

> 71\. Wrist right

> 72\. Elbow left

> 73\. Elbow right

> 74\. Shoulder left

> 75\. Shoulder right

> 76\. TMJ left

> 77\. TMJ right

> 78\. Costochondral disease(left)

> 79\. Costochondral disease(right)

> 80\. Sacroiliac disease(left)

> 81\. Sacroiliac disease(right)

> Physical Examination-Comprehensive Visit (Screen 5 of 5)

> Physical Examination-Comprehensive Visit(Pg 5 of 5) 09/16/93

> 1 PATIENT(R):.............................. 2 SSN(R):..........

> JOINT EXAMINATION continuation

> Left Right

> 82 HIP LEFT: ........ 83 HIP RIGHT: ........

> 84 KNEE LEFT: ........ 85 KNEE RIGHT: ........

> 86 ANKLE LEFT: ........ 87 ANKLE RIGHT: ........

> 88 MTP LEFT: ........ 89 MTP RIGHT: ........

> 90 TOES-PIP LEFT:........ 91 TOES-PIP RIGHT:........

> 92 CERVICAL SPINE:........

> 93 THORACIC SPINE:........

> 94 LUMBAR SPINE: ........

> Joint Examination Left and Right continuation

> Indicate the degree (0=None, 1=Mild, 2=Moderate, 3=Severe) of impairment of:

> 82\. Hip left

> 83\. Hip right

> 84\. Knee left

> 85\. Knee right

> 86\. Ankle left

> 87\. Ankle right

> 88\. MTP left

> 89\. MTP right

> 90\. Toes - PIP left

> 91\. Toes - PIP right

> 92\. Cervical spine

> 93\. Thoracic spine disease

> 94\. Lumbar spine

### Death Admin Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter the status of a patient as alive, lost to follow-up, or dead. Rheumatology death - admin. (page 1 of 1)

> Rheumatology death - admin. (page 1 of 1) 09/16/93

> 1 DATE/TIME(R):.................

> 2 PATIENT(R):.............................. 3 SSN(R):..........

> 4 LOST OR DEATH STATUS:............

> 5 DEATH DATE:.................

> 6 DISEASE ACTIVITY COMPOSITE:....

> 7 AUTOPSY AVAILABLE:....

> 8 CAUSE OF DEATH:.......................

> 9 CHART TYPE:......................

> 10 OBSERVER:....

> 11 DEC NUMBER:....

> 12 VISIT NUMBER:....

> 1\. Indicates the date and time that the data was first entered into the database or when the data was collected.

> 2\. Identify the patient in the medicine file.

> 3\. Give the patient's Social Security Number.

> 4\. Select from one of the following codes: "0" For Clinic Alive, "1" For Clinic Loss, "2" For Clinic

> Dead.

> 5\. Enter the death date of patient.

> 6\. Indicate the patient's disease activity composite. Type a number between 1 and 100, using no decimal digits.

> 7\. Enter yes or no if autopsy is available.

> 8\. Select from one of the following codes: "1" for Not Rheum Dis, "2" for Rheum Dis, "3" for

> Rheum Dis Surgery, "4" for Rheum Dis Drug Toxicity.

> 9\. Select chart type for the patient from one of the following codes: "0" for HAQ, "1" for UNMARKED, RDC VI, OR R, "2" for RDC VIII, "3" for RDC IX, "4" for RDC X, "5" for RDC XI (1985), "6" for DEATH INFORMATION, "7" for DISCHARGE SUMMARY

> 10\. Enter the name of the provider who saw the patient.

> 11\. Enter the data entry clerk number (0-50).

> 12\. Enter the visit number. This field identifies sequentially numbered visits.

### Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Rheumatology Print Menu contains the following options.

> 1 Diagnosis Print

> 2 Background Information Print

> 3 History Narrative Print

> 4 Serial Laboratory Info. Print

> 5 Health Assessment (HAQ) Print

> 6 Health/Physical History Print

> 7 Physical Examination Print

> 8 Death Admin Print

> 9 Print All Report

> 10 Brief Rheumatology Report

> Select Print Menu Option:

> The information contained in the preceding Rheumatology menu options may be selected for printing using this option. An example from the first option, Diagnosis Print, is given below.

#### Diagnosis Print

> Pg. 1 03/24/93 14:47

> CONFIDENTIAL RHEUMATOLOGY REPORT - Superseded Released On-Line Verified

> MEDPATIENT, ONE 000-82-0008 NOT INPATIENT DOB: 11/18/31

> PROCEDURE DATE/TIME: 04/11/86

> \- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

> PROBLEM LIST

> MAR 29,1991 13:41

> PATIENT DATE DIAGNOSIS MEDPATIENT, ONE

### Line Enter/Edit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows FileMan-oriented entry for the same Rheumatology fields as the screen entry option.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult Menu is discussed in the Problem Oriented Consult Menu section of this manual.

### Image Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Rheumatology menu contains an Image Capture option which allows a procedure image to be attached to a patient record. This option is only available to users at a workstation. Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for Generalized Procedures.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

### Rheumatology Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Certain functions are reserved for the Rheumatology Supervisor(s) or their designees. These are handled through the Rheumatology Management Menu.

#### Rheumatology Medication file Update.

> Allows Rheumatology Medications to be Added/Entered/Deleted in the Medication file. The user cannot enter a drug into the patient's record unless it has been marked as a Rheumatology drug in this file. All drugs marked as Rheumatology drugs must be present on the hospital formulary.

#### Delete Rheumatology Visit

> The Delete Rheumatology Visit option lets a Rheumatology chief or manager delete a Rheumatology patient's record.

## GENERALIZED PROCEDURE MODULE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> 10 Workload Reporting Management

> Choose the Generalized Procedure Menu option from the main Medicine menu.

> The purpose of the Generalized Procedure module is to document any procedure that is either not covered elsewhere or that does not have the imaging option provided. Any service can use the Generalized Procedure module to attach images to a patient record.

> Options on the Generalized Procedure Menu are:

> 1 Generalized Procedure Enter/Edit

> 2 Generalized Procedure Enter/Edit (Screen)

> 3 Generalized Procedure Report

> 4 Summary of Patient Procedures

> 5 Problem Oriented Problem Oriented Consult Menu

> 6 Image Capture

> 7 Brief Generalized Procedure Enter/Edit

> 8 Brief Generalized Procedure Enter/Edit (Screen)

> 9 Brief Generalized Procedure Report

> 10 Generalized Procedure Management

### Generalized Procedure Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is a FileMan-oriented entry for the same Generalized Procedure fields as the screen entry option.

> Generalized Procedure Enter/Edit (Screen)

> For a new procedure, enter the date/time of the procedure, the patient name and subspecialty. To edit an existing procedure, enter the patient name or date/time of the procedure.

> GENERALIZED PROCEDURE 09/16/97

> 1 DATE/TIME(R):.................

> 2 MEDICAL PATIENT(R):..............................

> 3 PROCEDURE:.......... 4 INDICATION(W):.....

> 5 MEDICATIONS(M):..............................

> 6 PROVIDER/PHYSICIAN:..............................

> 7 TECHNIQUE(M):..............................

> 8 COMPLICATIONS(M):..............................

> 9 SUBJECTIVE(W):.............................

> 10 OBJECTIVE(W): .............................

> 11 ASSESSMENT/FINDINGS(W):.....

> 12 PLAN(W):.....

> 13 SUMMARY:......................

> 14 PROCEDURE SUMMARY:.........................................

> 1&2 These fields are an echo of the information entered to get the screen.

> 3\. Enter the name or synonym of the procedure.

> 4\. Enter a complete description of the indications for the procedure.

> 5\. Indicate the prescribed medication.

> 6\. Identify the Physician or Service.

> 7\. Enter the procedure with which this intervention is associated.

> 8\. Choose complications from the list provided when "?" is entered.

> 9\. Summarize the subjective findings.

> 10\. Summarize the objective findings.

> 11\. Describe the Assessment/Findings from the procedure.

> 12\. The detailed plan of treatment should be entered here.

> 13\. Choose from: A - Abnormal, N - Normal, I - Incomplete examination.

> 14\. This field provides input into the summary of patient procedures.

### Generalized Procedure Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following fields are printed on the report:

> PROCEUDRE: INDICATION: MEDICATIONS: PROVIDER/PHYSICIAN: TECHNIQUE: COMPLICATIONS: SUBJECTIVE:

> Generalized Procedure Module

> OBJECTIVE: ASSESSMENT/FINDINGS: PLAN:

> SUMMARY:

> PROCEDURE SUMMARY:

### Generalized Procedure Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains the management option for generalized procedures.

> 1 Procedures/Subspecialties Definition Enter/Edit

> 2 Turn On Release Control/Elec. Signature

> Procedures/Subspecialties Definition Enter/Edit allows you to enter new or edit the definition of procedures and subspecialties in the Procedure/Subspecialty file (#697.2). You enter a procedure Name (required entry of 2-10 characters), Print Name (required longer name for the procedure), whether it is a procedure or subspecialty, and CPT code (not required). This data then becomes available for selection at the GENERALIZED PROCEDURE/CONSULT SUBSPECIALTY prompt when entering a generalized procedure.

> Note: Once a procedure is entered, you cannot delete the procedure. Because the procedure cannot be deleted, if you make a mistake, it is suggested you change the name to an appropriate procedure name or name it something that indicates that the procedure should not be selected.

> A number of procedures/subspecialties were exported with the software. These are not editable.

> Turn On Release Control/Elec. Signature is a one-time option that will turn on Release Control/Electronic signature. This option should only be used by the Manager of your department. Once this option is executed there is no way to turn it off. Once this is turned on, the non-key holders will not be able to print a record until it is released.

### Summary of Patient Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Summary of Patient Procedures is discussed in the Summary of Patient Procedures section of this manual.

### Problem Oriented Consult Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem Oriented Consult menu is discussed in the Problem Oriented Consult Menu section of this manual.

### Image Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Generalized Procedure menu contains an Image Capture option which allows a procedure image to be attached to a patient record. This option is only available to users at a workstation. Further information on the capabilities of Imaging can be found in the Introduction section of this manual and in the DHCP Imaging System User Manuals for Generalized Procedures.

### Brief Generalized Procedure Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows FileMan-oriented entry for the same Generalized Procedure fields as the brief screen.

### Brief Generalized Procedure Enter/Edit (Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a new procedure, enter the date/time of the procedure, the patient name and subspecialty. To edit an existing procedure, enter the patient name or date/time of the procedure.

> Brief Generalized Procedure Screen 09/16/97

> 1 PROCEDURE DATE/TIME(R):.................

> 2 MEDICAL PATIENT(R):..............................

> 3 PROCEDURE:..............................

> 4 SUBJECTIVE(W):.....

> 5 OBJECTIVE(W):.....

> 6 ASSESSMENT/FINDINGS(W):.....

> 7 PROVIDER/PHYSICIAN:..............................

> 8 SUMMARY:..............................

> 9 PROCEDURE SUMMARY:..............................

> 1&2 These fields are an echo of the information entered to get the screen.

> 3\. Enter the procedure name or synonym.

> 4\. Summarize the subjective findings.

> 5\. Summarize the objective findings.

> 6\. Summarize the assessment and findings.

> 7\. Enter the provider name.

> 8\. Choose from: A - Abnormal, N - Normal, I - Incomplete examination.

> 9\. Enter the procedure summary.

### Brief Generalized Procedure Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Brief Generalized Procedure report prints the fields covered under Brief Generalized Procedure

> Enter/Edit (Screen).

## SUMMARY OF PATIENT PROCEDURES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Medicine Menu

> 1 Cardiology Menu

> 2 GI Menu

> 3 Pulmonary Menu

> 4 Hematology Menu

> 5 Pacemaker Menu

> 6 Rheumatology Menu

> 7 Generalized Procedure Menu

> 8 Summary of Patient Procedures

> 9 Enable/Disable OE/RR

> Choose Summary of Patient Procedures from the main Medicine menu.

> The Summary of Patient Procedures option allows screen display and printing of medical procedures performed on a patient. The listing may be sorted by date or by procedure.

> The user is first presented with the "PRINT BY DATE OR PROCEDURE (D/P) :D//" prompt. The user should enter a \<RET\> to sort by date, or a "P" \<RET\> to view by procedure.

> "Select MEDICAL PATIENT NAME:" is the next prompt. The user should select a patient.

### Summary of Patient Procedures by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Date Screen option is chosen, the user is prompted to enter a device. When a device is chosen, all of the procedures (i.e., ETT, Holter, etc.) will be listed by date and result, with the most recently performed procedure displayed first. Only eight procedures are displayed on the screen at any one time. At the bottom of the screen, the prompt "For Procedure Expansion 1-8 Or \<RET\> To Continue Display//” appears. Entering a sequence number, such as "9" or "17", will take the user to the next screen. When the second device prompt appears, the report should be sent to a printer.

> When a procedure is finished printing to the screen, the prompt "\*END\* Press Return to Continue" appears. A \<RET\> will place the user back at the Procedure Listing. Upon entering another number, the device prompt is displayed again to allow printing the procedure data. The user should enter “^” to exit the listing. If no number has been selected, then upon completion of the listing of procedures, the user will be returned to the main menu.

> PRINT BY DATE OR PROCEDURE (D/P): D// \<RET\>

> Select MEDICAL PATIENT NAME: MEDPATIENT, ONE 04-04-25 000563726

> DEVICE: HOME RIGHT MARGIN: 80// \<RET\>

> The following screen would then be displayed (only the first screen is shown)

> NAME: MEDPATIENT, ONE SSN: 000-56-3726 WARD: 3E (SUBSPECIALTY)/PROCEDURE DATE RESULTS

> -------------------------------------------------------------------------------

> 1 CARDIOLOGY/CVP LINE JUN 3,1997@15:53

> 2 VASCULAR/LAVAGE JUN 3,1997@11:11

> Acute alcoholic ...

> 3 VASCULAR/PARACENTESIS JUN 3,1997@10:06 ABNORMAL Ascites removed

> FOR PROCEDURE EXPANSION (1-3) OR \<RETURN\> TO CONTINUE DISPLAY//

> Note that the latest procedure performed on the patient is listed first.

### Summary of Patient Procedures by All Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Procedure Screen option is chosen, the "ALL//" prompt appears. Entering "?" will display a list of procedure selections (note that the patient has not necessarily had the procedures performed), while entering a return will give a list of all procedures performed on the patient.

> A prompt for procedure expansion is then displayed. For each type of procedure, all ECG results, all Echo results, and so on, are shown. The procedures are listed in alphabetical order. When the device prompt appears, any particular procedure already listed may be chosen. Using "^" after the double slash of the device prompt will take the user back to the main menu.

> PRINT BY DATE OR PROCEDURE (D/P): D//P

> Select Procedure: ALL//\<RET\>

> Select MEDICAL PATIENT NAME: MEDPATIENT, ONE 04-04-25 000563726

> DEVICE: HOME RIGHT MARGIN: 80// \<RET\>

> NAME: MEDPATIENT, ONE SSN: 000-56-3726 WARD: 3E (SUBSPECIALTY)/PROCEDURE DATE RESULTS

> -------------------------------------------------------------------------------

> 1 VASCULAR/PARAC JUN 4,1997@11:01 ABNORMAL

> 1300 cc ascites removed

> 2 VASCULAR/GENERIC PROCEDURE JUN 3,1997@11:11 ABNORMAL

> acute alcoholic ...

> 3 VASCULAR/PARAC JUN 3,1997@10:06 ABNORMAL Ascites removed

> FOR PROCEDURE EXPANSION (1-3) OR \<RETURN\> TO CONTINUE DISPLAY// \<RET\>

### Summary of Patient Procedures by One Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a user only wished to view one type of procedure on a patient, such as Paracentesis, the following sequence would be performed.

> PRINT BY DATE OR PROCEDURE (D/P): D//P

> Select Procedure: ALL// PARAC PARACENTESIS

> Select MEDICAL PATIENT NAME: MEDPATIENT, ONE 04-04-25 000563726

> DEVICE: HOME RIGHT MARGIN: 80// \<RET\>

> NAME: MEDPATIENT, ONE SSN: 000-56-3726 WARD: 3E

> Summary of Patient Procedures

> (SUBSPECIALTY)/PROCEDURE DATE RESULTS

> -------------------------------------------------------------------------------

> 1 VASCULAR/PARAC JUN 4,1997@11:01 ABNORMAL

> 1300 cc ascites removed

> 2 VASCULAR/PARAC JUN 3,1997@10:06 ABNORMAL Ascites removed

> FOR PROCEDURE EXPANSION (1-2) OR \<RETURN\> TO CONTINUE DISPLAY// \<RET\>

> Note that only the requested procedure is displayed, in reverse chronological order.

> In all of the above examples, if the user wished for an expansion of the procedure, he would simply enter the number for that procedure. A device prompt will then be displayed, allowing the user to send the expansion to a printer. The output from this report is similar to using the print option in the various modules. Once the Turn On Release Control/Elec. Signature option is turned on, the non-key holders will not be able to print a record until it is released.

> This page is intentionally left blank.

## PROBLEM ORIENTED CONSULT MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Problem Oriented Consult Menu options have the following options.

> 1\. Problem Oriented Consult Enter/Edit

> 2\. Problem Oriented Consult Enter/Edit (Screen)

> 3\. Problem Oriented Consult Report

> 4\. Brief Enter/Edit of Problem Oriented Consult

> 5\. Brief Consult Enter/Edit (Screen)

> 6\. Brief Consult Report

### Problem Oriented Consult Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module makes use of the FileMan word processing field type to enter comments in the S.O.A.P. (Subjective, Objective, Assessment, Plan) format. In addition to the word processing fields S.O.A.P., the user also enters the date/time of consult, patient name, consulting provider, a free text "indication" comment, consultation type, and a summary of consultation.

> The screen option for consult enter/edit presents the same information as the FileMan enter/edit.

### Problem Oriented Consult Enter/Edit (Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Problem Oriented Consult Menu Option: 2 Problem Oriented Consult Enter/Edit (Screen) ENTER DATE/TIME OF CONSULT: N OCT 20, 1994@09:08

> ARE YOU ADDING 'OCT 20, 1994@09:08' AS

> A NEW GENERALIZED PROCEDURE/CONSULT? Y (YES)

> GENERALIZED PROCEDURE/CONSULT DATE/TIME: OCT 20,1994@09:08 // GENERALIZED PROCEDURE/CONSULT MEDICAL PATIENT:

> CONSULT 09/16/93

> 1 DATE/TIME OF CONSULTATION(R):.................

> 2 MEDICAL PATIENT(R):..............................

> 3 CONSULTING DOCTOR(R):..............................

> 4 INDICATION COMMENT:.........................................

> 5 SUBJECTIVE(W):.....

> 6 OBJECTIVE(W):.....

> 7 ASSESSMENT(W):.....

> 8 PLANNED(W):.....

> 9 CONSULTATION TYPE:..............................

> 10 SUMMARY OF CONSULTATION:...............................

> 1\. This is the date and time of the consult.

> 2\. This field Identifies the patient by name.

> 3\. This field identifies the primary physician.

> 4\. This field is used in the Problem-Oriented Consult Enter/Edit and Print.

> 5\. Describe the subjective findings.

> 6\. Describe fully the objective findings.

> 7\. Enter an assessment of the findings.

> 8\. Enter a detailed plan of treatment.

> 9\. Indicate the type of consultation.

> 10\. Give a detailed summary of consultation.

### Problem Oriented Consult Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a printed report of information entered through the Consult Enter/Edit.

### Brief Enter/Edit of Problem Oriented Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is a FileMan-oriented entry for the same Problem Oriented Consult fields as the screen entry option.

### Brief Consult Edit/Enter Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Brief Consult Screen 09/16/93

> 1 DATE/TIME:.................

> 2 MEDICAL PATIENT:..............................

> 3 SUBJECTIVE(W):.....

> 4 OBJECTIVE(W):..... 5 ASSESSMENT/FINDINGS(W):.....

> Descriptions of the fields and subscreens of this screen will be found under the Consult screen previously displayed.

### Brief Consult Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option prints a Consult Report derived from the information entered using a Brief Enter/Edit option.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ACT Actual: The raw number (not predicted). A-Lead Implant/Explant A type of pacemaker lead.
> Anastomosis A formation of a passage between two normally distinct spaces or organs.
> Angioplasty PTCA (Percutanious transluminal coronary angioplasty), the instrumentation of a blood vessel to dilate stenotic coronary arteries.
> Aorta The largest vessel of the systemic arterial system. Arrhythmia Any variation from normal, regular cardiac rhythm. Atrial A term for the left and right upper chamber of the heart. Atropine A drug used to increase heart rate.
> Auto Instrument Interface Method of transferring information gathered using a medical device to the DHCP database.
> Automated Records Transfer (see Auto Instrument Interface)
> Bigeminy The occurrence of heart beats in pairs. BMA Bone marrow aspirates.
> BMB Bone marrow biopsies.
> Brief Screen or Report Use of a predetermined subset of fields for entering or retrieving procedure information.
> Cardiac Cath Test in which a tube is passed into the heart through a vein or artery.
> Circumflex A vessel in the left coronary artery anatomy.
> COHB Carboxhemaglobin: The amount of carbon monoxide combined with hemoglobin.
> Collateral An alternate channel of circulation.
> Diastolic A period of atrial and ventricular muscle relaxation.
> Draft Status Unless designated otherwise, all records have draft status once they are entered. A record with Draft status may be edited or deleted. It is not released to non-key holders for viewing in report form.
> ECG (EKG) A graphic record of the heart's action currents.
> Echo Echocardiogram; a test using ultrasound techniques to investigate the heart and great vessels and to diagnose cardiovascular lesions.
> Ectopic ECG complexes which are unusual in terms of timing or contour. Ejection Fraction The actual overall function of the heart, given as a percentage. EKG (ECG) A graphic record of the heart's action currents.
> Electronic Signature An electronic signature is a unique set of keystrokes that are entered to give on-line approval. In the Medicine package, it is used to maintain the integrity of reported procedure results.
> Endoscopic Procedure The examination of the interior of a canal or hollow viscus using an endoscope.
> EP Electrophysiology; test of the electrical phenomena associated with physiologic processes.
> ETT Exercise Tolerance Test; measures the heart's reaction under controlled levels of exercise.
> Fibrillation An arrhythmia characterized by total disorganization of atrial or ventricular electrical activity.
> Generalized Procedure In the Medicine package, any procedure for which there is not a specific module.
> Generator Implant/Explant A type of pacemaker.
> GI Gastrointestinal; Procedure relating to the stomach or intestines. Gradient The rate of change of pressure, or the pressure difference, across
> a heart valve.
> HB Heart beat.
> Hematology Medical specialty pertaining to the blood and blood forming tissues.
> Hemodynamics Study of dynamics of blood circulation.
> Holter Technique for long-term recording of select but fleeting changes in EKG signals.
> Indo Green A dye used to measure an excretory function. Isuprel A cardiac stimulant.
> Marked for Deletion A flag placed on records which should be deleted.
> Mitral The cardiac valve located between the left atrium and left ventricle.
> Morphology The shape or form of a P, QRS, or T wave.
> Non-Endoscopic Procedure The examination of the interior of a canal or hollow viscus without the use of an endoscope.
> OE/RR The DHCP Order Entry/Results Reporting package. Pacemaker An artificial regulator to control heart rhythm.
Glossary
> PFT Pulmonary Function Test; a test of lung functioning.
> Pred Predicted: A prediction based on a person's age, sex, weight, and race for any indices.
> Problem Draft Status A record may be designated as Problem Draft if the information is incomplete or inaccurate. This label should alert the provider
> that there is some problem with the information that needs to be resolved. The record may be edited or deleted. It is not released to non-key holders for viewing in report form.
> Procedure A test for or action relating to a medical diagnosis. Provider Any person providing care to a patient.
> Pulmonary A reference to the part of circulation supplied by the pulmonary artery.
> Pulmonary Function A test of lung functioning. Test (PFT)
> PVC Premature contraction of the ventricle.
> Refractory Period A period of resistance to treatment or stimulation.
> Release Control A method of controlling when and to whom procedure records are available.
> Released Not Used when a record is released before the
> Verified Status information has been verified or when an authorized signature is not available.
> Released Off-line The provider authorized release of the record by signing
> Verified Status a printed copy of the report rather than on-line. Another key holder is designated to make the electronic release. Both persons are recorded in the release record.
> Released On-line The provider has given on-line authorization for release
> Verified Status of the information.
> Rheumatology The study, diagnosis, and treatment of conditions affecting the musculoskeletal system.
> Septum The wall which separates the left and right atrium and the left and right ventricle.
> Shunt The passage of blood from one side of the heart to another through an abnormal opening.
> Sinus of Valsalva A dilation of the aorta or pulmonary artery. Stenosis A constriction or narrowing of a passage or orifice.
> Superseded Record The original of a previously released record which later required editing.
> Systemic A reference to the part of circulation supplied by the aorta. Tachycardia A fast heart rate.
> Thrombus A blood clot.
> TLC Total lung capacity. Wenckebach A form of partial heart block.
> Ventricular A term for the left or right lower chamber of the heart. V-Lead Implant/Explant A type of pacemaker lead.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *A*
> A-Lead Implant/Explant ........................................................................................................................ 126
> A-Lead Report ......................................................................................................................................... 133
> Active Patient Report ............................................................................................................................. 133
> Allergies .............................................................................................................................................. 76, 92
> Angioplasty Segment ................................................................................................................................ 32
> Atrial Study .................................................................................................................................. 49, 50, 51
> Automated Transfer of Report ............................................................................................................... 134
> *B*
> Blocked Fields ............................................................................................................................................. 6
> Blood Gas ................................................................................................................................................ 103
> Bowel Preparation .................................................................................................................................... 81
> Brief A-Lead and V-Lead ....................................................................................................................... 131
> Brief Consult Edit/Enter Screen ............................................................................................................ 162
> Brief Endoscopy Enter/Edit (Screen) ...................................................................................................... 98
> Brief Enter/Edit Cath (Screen) ................................................................................................................ 34
> Brief Enter/Edit ECG (Screen) ................................................................................................................ 40
> Brief Enter/Edit Echo (Screen) ................................................................................................................ 45
> Brief Generalized Procedure Enter/Edit ............................................................................................... 155
> Brief Generalized Procedure Report ..................................................................................................... 155
> Brief Hematology Enter/Edit (Screen) .................................................................................................. 122
> Brief Non-Endo Enter/Edit ...................................................................................................................... 87
> Brief Pacemaker Screens ....................................................................................................................... 131
> Brief PFT Enter/Edit (Screen) ............................................................................................................... 112
> Brief Procedure Enter/Edit (Screen) ....................................................................................................... 85
> Brief Reports ........................................................................................................................................... 134
> Bypass Tract Atrial .................................................................................................................................. 52
> *C*
> Cardiology ................................................................................................................................................. 19
> Cardiology Management Menu ............................................................................................................... 20
> Carotid Stimulation .................................................................................................................................. 48
> Circumflex Segment ................................................................................................................................. 30
> Combined Implant/Leads ....................................................................................................................... 124
> Complications ..................................................................................................................................... 82, 96
> Consult Screen ........................................................................................................................................ 161
> Cough ......................................................................................................................................................... 94
> *D*
> Death Admin Edit ................................................................................................................................... 150
> Default Answers ......................................................................................................................................... 3
> Delete Endoscopic Procedure ................................................................................................................. 115
> Deleting Information .................................................................................................................................. 3
> Demographic Data .................................................................................................................................. 130
> Demographic Screen ................................................................................................................................. 91
> Diagnosis Edit for Rheumatology .......................................................................................................... 137
> Diagnosis Print ....................................................................................................................................... 151
> Diagnosis Review/Revision ...................................................................................................................... 84
> Discharge Date ................................................................................................................................... 52, 55
> Display Serial Laboratory Info .............................................................................................................. 140
> Disposition ................................................................................................................................................ 83
> Distal Anastomosis ................................................................................................................................... 31
> Doppler Valve Regurg .............................................................................................................................. 44
> Draft Status ......................................................................................................................................... 11, 13
> Drive Cycle ................................................................................................................................................ 54
> Drive Rate ................................................................................................................................................. 50
> Drug Treatment Print Program ............................................................................................................ 141
> *E*
> ECG Auto Screens .................................................................................................................................... 37
> ECG Menu ................................................................................................................................................. 35
> ECG Screen ............................................................................................................................................... 38
> Echo ........................................................................................................................................................... 41
> Electronic Signature ........................................................................................................................... 11, 16
> Endoscopy ............................................................................................................................................ 78, 93
> Endoscopy Enter/Edit ............................................................................................................................... 91
> Endoscopy Menu ....................................................................................................................................... 90
> Enter/Edit Cath Lab ................................................................................................................................. 22
> Enter/Edit ECG ........................................................................................................................................ 35
> Enter/Edit Menu (Line Entry) ............................................................................................................... 123
> Enter/Edit Menu for Screen Entry of Pacemaker ................................................................................ 124
> Enter/Edit Options ..................................................................................................................................... 7
> Enter/Edit PFT ....................................................................................................................................... 100
> EP Lab Menu ............................................................................................................................................ 46
> Exercise ................................................................................................................................................... 104
> *F*
> Field Codes .................................................................................................................................................. 6
> Final Disposition ...................................................................................................................................... 97
> Flows Study ............................................................................................................................................. 102
> *G*
> Gastrostomy Tube Enter/Edit .................................................................................................................. 88
> Generalized Procedure Enter/Edit ........................................................................................................ 154
> Generalized Procedure Menu ................................................................................................................ 153
> Generalized Procedure Report ............................................................................................................... 154
> Generator Implant .................................................................................................................................. 124
> Generator Report .................................................................................................................................... 133
> GI Demographic Screen ........................................................................................................................... 76
> GI Management Menu ............................................................................................................................. 88
> GI Medication Update .............................................................................................................................. 88
> GI Procedure Enter/Edit .......................................................................................................................... 77
> *H*
> Health Assessment (HAQ) ..................................................................................................................... 141
> Health/Physical History Edit ................................................................................................................. 142
> Heart Block ............................................................................................................................................... 47
> Heart Medications .................................................................................................................. 23, 36, 38, 47
> Hematology Report ................................................................................................................................. 121
> History Narrative ................................................................................................................................... 139
> Holter ......................................................................................................................................................... 56
> *I*
> Image Capture ............................................................................................................ 85, 98, 121, 152, 155
> Inflation Pressures ................................................................................................................................... 32
> Interpretation Code ............................................................................................................................ 37, 39
> Interpretation Enter/Edit ...................................................................................................................... 108
> *J*
> Jejunostomy Tube Enter/Edit .................................................................................................................. 88
Index
> *K*
> Keypad Commands ..................................................................................................................................... 5
> *L*
> LAD Origin of Collaterals ........................................................................................................................ 30
> LAD Segment ............................................................................................................................................ 30
> Left Coronary Catheter ............................................................................................................................ 24
> Left Ventricular Catheter ........................................................................................................................ 24
> Left Ventricular Wall Motion .................................................................................................................. 32
> Legal Requirements ................................................................................................................................. 15
> LMCA Narrowing ..................................................................................................................................... 29
> Locating Records ..................................................................................................................................... 7, 8
> Location Evaluated ....................................................................................................................... 81, 82, 96
> *M*
> Manufacturer's List Update ................................................................................................................... 135
> Maximum Pressures ............................................................................................................................... 105
> MCARSUMMARY .................................................................................................................................... 16
> Mechanics ................................................................................................................................................ 103
> Medication ..................................................................................................................................... 42, 79, 95
> Menu Distribution .................................................................................................................................... 16
> *N*
> Non-Endoscopic Procedures ..................................................................................................................... 86
> *O*
> OE/RR Interface ......................................................................................................................................... 9
> Orientation .................................................................................................................................................. 3
> Other Endoscopic Options ........................................................................................................................ 84
> Other PFT Options ................................................................................................................................. 107
> Other Pulmonary Options ........................................................................................................................ 97
> *P*
> Pacemaker Equipment Update .............................................................................................................. 135
> Pacemaker Management Menu ............................................................................................................. 135
> Pacemaker Module ................................................................................................................................. 123
> Pacemaker Report Menu ........................................................................................................................ 133
> Pacemaker Surveillance ......................................................................................................................... 127
> Pacing Failure ......................................................................................................................................... 126
> Personal History ................................................................................................................................. 76, 91
> PF Keys ........................................................................................................................................................ 5
> PFT Predicted Values Formulas ............................................................................................................ 113
> PFT Report .............................................................................................................................................. 110
> Physical Examination Edit .................................................................................................................... 145
> Pneumonia ................................................................................................................................................ 94
> Pneumoperitoneum Gas ........................................................................................................................... 81
> Prescription ......................................................................................................................................... 83, 97
> Problem Draft ..................................................................................................................................... 11, 13
> Problem Oriented Consult Enter/Edit .................................................................................................. 161
> Problem Oriented Consult Enter/Edit (Screen) ................................................................................... 161
> Problem Oriented Consult Menu ........................................................................................................... 161
> Problem Oriented Consult Report ......................................................................................................... 162
> Procedure Test Results ............................................................................................................................ 21
> Pulmonary Function Test ...................................................................................................................... 100
> Pulmonary Instrument Enter/Edit ........................................................................................................ 113
> Pulmonary Management Menu ............................................................................................................. 113
> Pulmonary Medication Update .............................................................................................................. 113
> *Q*
> Qume Terminals ......................................................................................................................................... 5
> *R*
> RCA Origin of Collaterals ........................................................................................................................ 28
> RCA Segment ............................................................................................................................................ 28
> Recall List ........................................................................................................................................... 85, 98
> Regional Wall Motion ............................................................................................................................... 43
> Related Manuals ......................................................................................................................................... 2
> Release Control ........................................................................................... 11, 16, 17, 21, 74, 90, 118, 123
> Released Not Verified ......................................................................................................................... 11, 13
> Released Off-line Verified .................................................................................................................. 12, 13
> Released On-line Verified .................................................................................................................. 12, 13
> Reports ................................................................................................................................................ 73, 89
> Return Key .................................................................................................................................................. 3
> Rheumatology Management Menu ....................................................................................................... 152
> Rheumatology Medication File Update ................................................................................................ 152
> Rheumatology Menu .............................................................................................................................. 137
> Rheumatology Patient Background Info ............................................................................................... 138
> Rheumatology Print Menu ..................................................................................................................... 151
> Right Coronary Catheter ......................................................................................................................... 24
> Risk Factor .............................................................................................................................................. 130
> *S*
> Screen Commands ...................................................................................................................................... 5
> Screen Conventions .................................................................................................................................... 4
> Screens and Subscreens ........................................................................................................................... 10
> Site Configuration Issues ......................................................................................................................... 15
> Small Airways ......................................................................................................................................... 104
> Special Studies ........................................................................................................................................ 106
> Sphincterotome Enter/Edit ...................................................................................................................... 88
> Stent Enter/Edit ....................................................................................................................................... 88
> Subspecialty .............................................................................................................................................. 13
> Summary of Patient Procedures .................................................................................................. 1, 87, 157
> Superseded Records............................................................................................................................. 12, 13
> Surgical Risk Analysis ............................................................................................................................. 19
> Surveillance Report ................................................................................................................................ 133
> *U*
> Underline .................................................................................................................................................... 3
> Upper/lower Case ....................................................................................................................................... 3
> User Functions .......................................................................................................................................... 13
> *V*
> V-Lead Implant/Explant ........................................................................................................................ 127
> V-Lead Report ......................................................................................................................................... 133
> Ventricular Study ............................................................................................................................... 53, 54
> Volume Study .......................................................................................................................................... 101
