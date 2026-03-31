---
title: DG*5.3*554/TIU*1*184/USR*1*27 Patient Record Flags Phase II Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*554
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 12
description: The Patient Record Flags Phase II patches (TIU\1\184, USR\1\27, DG\5.3\554), in conjunction with the CPRS GUI version 26 patch (OR\3\215), introduce changes and enhancements to the TIU – Text Integration Utilities V. 1.0 and Registration V. 5.3 packages in direct support of the Patient Record Flags
audience: 
keywords: 
  - flag
  - table
  - contents
  - record
  - assignment
  - action
  - patient
  - notes
  - link
  - dgpf
page_count: 0
word_count: 6947
section_count: 58
table_count: 15
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfii_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfii_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

![](dg-5-3-554-tiu-1-184-usr-1-27-patient-record-flags-phase-ii-release-notes/001.png)

Patient Record Flags Phase IIRelease Notes

### Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIU\*1\*184

DG\*5.3\*554

USR\*1\*27

### April 2006

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### ### ### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health Systems Design & Development (HSD&D)

# # Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Patches](#patches)
    - [April 2006](#april-2006)
    - [### ### ### Department of Veterans Affairs](#department-of-veterans-affairs)
- [# Preface](#preface)
- [# # Introduction - Patient Record Flags Phase II](#introduction-patient-record-flags-phase-ii)
  - [Overview](#overview)
- [Registration Package - Enhancements](#registration-package-enhancements)
  - [Overview](#overview-1)
  - [Modified Options](#modified-options)
  - [Record Flag Management option TIU Link](#record-flag-management-option-tiu-link)
  - [Record Flag Assignment option TIU Link](#record-flag-assignment-option-tiu-link)
  - [Active PRF Assignments display modification](#active-prf-assignments-display-modification)
  - [Edit Flag Assignment modification](#edit-flag-assignment-modification)
  - [Record Flag Management Screen Re-Display](#record-flag-management-screen-re-display)
  - [Record Flag Assignment Screen Re-Display](#record-flag-assignment-screen-re-display)
  - [New PRF Report Options](#new-prf-report-options)
  - [Record Flag Reports Menu](#record-flag-reports-menu)
    - [PRF Menu Diagram](#prf-menu-diagram)
  - [Assignment Action Not Linked Report](#assignment-action-not-linked-report)
  - [Patient Assignments Report](#patient-assignments-report)
  - [Assignments Approved By Report](#assignments-approved-by-report)
  - [Assignments by Principal Investigator Report](#assignments-by-principal-investigator-report)
- [Registration Package - Technical Information](#registration-package-technical-information)
  - [Overview](#overview-2)
  - [New Options](#new-options)
  - [DGPF ACTION NOT LINKED REPORT](#dgpf-action-not-linked-report)
  - [DGPF APPROVED BY REPORT](#dgpf-approved-by-report)
  - [DGPF PATIENT ASSIGNMENT REPORT](#dgpf-patient-assignment-report)
  - [DGPF PRINCIPAL INVEST REPORT](#dgpf-principal-invest-report)
  - [New / Modified Fields of the PRF Files](#new-modified-fields-of-the-prf-files)
  - [New Database Integration Agreements (DBIA)](#new-database-integration-agreements-dbia)
  - [DBIA (#4383) DGPF ASSIGNMENT LINK TIU PN](#dbia-4383-dgpf-assignment-link-tiu-pn)
  - [DBIA (#4384) DGPF FILE/DELETE TIU PN LINK](#dbia-4384-dgpf-filedelete-tiu-pn-link)
  - [DBIA (#4386) DGPF ASSOCIATED FLAG PN TITLE](#dbia-4386-dgpf-associated-flag-pn-title)
  - [DBIA (#4387) DGPF ASSIGNMENT TIU PN LINK](#dbia-4387-dgpf-assignment-tiu-pn-link)
  - [Modified Database Integration Agreements (DBIA)](#modified-database-integration-agreements-dbia)
  - [DBIA (#3860) DGPF PATIENT RECORD FLAG – ACTIVE ASSIGNMENT API](#dbia-3860-dgpf-patient-record-flag-active-assignment-api)
  - [New / Modified Routines](#new-modified-routines)
- [Text Integrated Utilities (TIU) - Enhancements](#text-integrated-utilities-tiu-enhancements)
  - [Overview](#overview-3)
  - [Setup](#setup)
  - [Modified Options](#modified-options-1)
  - [TEXT INTEGRATION UTILITIES (TIU)](#text-integration-utilities-tiu)
  - [New Options](#new-options-1)
  - [TEXT INTEGRATION UTILITIES (TIU)](#text-integration-utilities-tiu-1)
  - [Uploading PRF Notes](#uploading-prf-notes)
  - [OVERVIEW](#overview-4)
  - [PRF UPLOAD PARAMETERS](#prf-upload-parameters)
  - [PRF UPLOAD FILING ERRORS](#prf-upload-filing-errors)
  - [INTERDISCIPLINARY NOTES](#interdisciplinary-notes)
  - [GROUP NOTES](#group-notes)
  - [BUSINESS RULES](#business-rules)
- [Text Integrated Utilities (TIU) - Technical Information](#text-integrated-utilities-tiu-technical-information)
  - [Overview](#overview-5)
  - [TEXT INTEGRATION UTILITIES (TIU)](#text-integration-utilities-tiu-2)
  - [New / Modified Fields of the TIU Files](#new-modified-fields-of-the-tiu-files)
  - [COMPUTED FIELD PRF FLAG](#computed-field-prf-flag)
  - [COMPUTED FIELD PRF FLAG ACTION](#computed-field-prf-flag-action)
  - [New Database Integration Agreements (DBIA)](#new-database-integration-agreements-dbia-1)
  - [DBIA (4380)](#dbia-4380)
  - [DBIA (4839)](#dbia-4839)
  - [New / Modified Routines](#new-modified-routines-1)
- [Authorization/Subscription (USR) - Enhancements](#authorizationsubscription-usr-enhancements)
  - [Overview](#overview-6)
  - [New / Modified Options](#new-modified-options)
  - [NEW ACTION LINK TO FLAG (USR\1.0\27) patch](#new-action-link-to-flag-usr1027-patch)
- [Authorization/Subscription (USR) - Technical Information](#authorizationsubscription-usr-technical-information)
  - [Overview](#overview-7)
  - [NEW ACTION LINK TO FLAG (USR\1.0\27) patch](#new-action-link-to-flag-usr1027-patch-1)
Purpose of the Patch Release Notes:
This document describes the new features and functionality of the Patient Record Flags Phase II project distributed in patches USR\*1\*27, TIU\*1\*184, and DG\*5.3\*554. Additionally, this document includes a description of the technical components that are used for this project.
The Patient Record Flags Phase II software satisfies the requirement that all Patient Record Flag Assignments are linked to a Text Integration Utilities (TIU) Progress Note.
The CPRS GUI version 26 patch (OR\*3\*215) is being released separately in direct support of the Patient Record Flags Phase II project. This document does not contain the details of the new CPRS GUI 26 features and functionality.
[1.1 Overview [1](#overview)](#overview)
[7.1 Overview [33](#overview-7)](#overview-7)
[7.1.1 NEW ACTION LINK TO FLAG (USR\*1.0\*27) patch [33](#new-action-link-to-flag-usr1.027-patch-1)](#new-action-link-to-flag-usr1.027-patch-1)

# # # Introduction - Patient Record Flags Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Record Flags Phase II patches (TIU\*1\*184, USR\*1\*27, DG\*5.3\*554), in conjunction with the CPRS GUI version 26 patch (OR\*3\*215), introduce changes and enhancements to the TIU – Text Integration Utilities V. 1.0 and Registration V. 5.3 packages in direct support of the Patient Record Flags initiative.

Veterans Health Administration (VHA) mandated in the “National Patient Record Flags” Directive 2003-048 that TIU Progress Notes be created and linked to all Patient Record Flags (PRF) actions.

Both the TIU and Registration packages provide the following functionality needed to implement the Directive’s recommendations:

- The creation of a TIU Progress Note should be enforced by policy, not by software.
- Every Patient Record Flag Assignment History action should be linked to a TIU Progress Note.
- PRF Assignments can be created without a TIU Progress Note being written and signed at the time of the Record Flag Assignment to the patient.
- PRF Progress Notes can be viewed by anyone who has access to TIU Progress Notes.
- Reporting tools will provide a means of identifying those PRF Assignment actions that do not have a TIU Progress Note associated with them.

For additional information, refer to VHA Directive 2003-048 "National Patient Record Flags".

# Registration Package - Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the functionality being implemented within the Patient Record Flags module of the Registration package.

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Record Flag Management option TIU Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### The following enhancements have been made to the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option to link a TIU Progress Note Title to a specific Patient Record Flag:

- The PRF NATIONAL FLAG (#26.15) and PRF LOCAL FLAG (#26.11) files will have a new field added to contain the TIU Progress Note Title that is to be associated with each flag name.

> TIU PN TITLE

- The Category I (National) Flag, BEHAVIORAL, has been linked with the following TIU Progress Note Title by the patch install.

> PATIENT RECORD FLAG CATEGORY I

- The Category II (Local) Flag actions, Add New Record Flag and Edit Record Flag, will have a new user prompt added to link a Record Flag to a TIU Progress Note Title. Only TIU Progress Note Titles not currently linked to a Record Flag will be available as a selection when prompted for selecting a Progress Note Title.

> Enter the Progress Note Title:

> Important: All existing PRF Category II Record Flags must be edited using the Edit Record Flag action to associate a TIU Progress Note Title with the record flag. Until this is accomplished, no patient record flag assignments associated with the record flag can be entered or edited.

> Example:

> Select Action:Quit// AF Add New Record Flag

> Enter the Record Flag Name: TESTING FLAG

> Enter the Status of the Flag: ACTIVE// ACTIVE

> Enter the Type of the Flag: CLINICAL

> Enter the Review Frequency Days: 120

> Enter the Notification Days: 30

> Enter the Review Mail Group: DGPF BEHAVIORAL FLAG REVIEW

> Enter the Progress Note Title:??

> This field contains the Category II Progress Note Title that is

> associated with this Patient Record Flag.

> Choose from:

> PATIENT RECORD FLAG CATEGORY II – RESEARCH STUDY

> PATIENT RECORD FLAG CATEGORY II – RISK, FALL

> PATIENT RECORD FLAG CATEGORY II – INFECTIOUS DISEASE

> PATIENT RECORD FLAG CATEGORY II – RISK, WANDERING

> Enter the Progress Note Title: PATIENT RECORD FLAG CATEGORY II – RISK, FALL

> Enter the description for this new record flag:

- The Display Flag Detail action screen will display the TIU Progress Note Title currently linked with the National or Local Flag name.

> FLAG DETAILS Nov 24, 2004@13:18:53 Page: 1 of 1

> Flag Name: BEHAVIORAL Flag Status: ACTIVE

> Flag Name: BEHAVIORAL

> Flag Category: I (NATIONAL)

> Flag Type: BEHAVIORAL

> Flag Status: ACTIVE

> Review Freq Days: 730

> Notification Days: 60

> Review Mail Group: DGPF BEHAVIORAL FLAG REVIEW

> Progress Note Title: PATIENT RECORD FLAG CATEGORY I

> Flag Description:

> -----------------

> The purpose of this National Patient Record Flag is to alert VHA medical

> staff and employees of patients whose behavior or characteristics may pose a threat either to their safety, the safety of other patients, or

> compromise the delivery of quality health care.

> Application of National Patient Record Flags is coordinated through the

> Chief of Staff.

> This is a nationally distributed flag.

## Record Flag Assignment option TIU Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following enhancements have been made to the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option to provide for the displaying of a linked TIU Progress Note to a PRF Assignment History Action record:

- The ASSIGNMENT HISTORY FILE (#26.14) will have a new field added to store the TIU Progress Note that was created to link with the PRF assignment action.

> TIU PN LINK

- The Display Assignment Details action screen will display the following detail for the new Progress Note field as shown below:

> ASSIGNMENT DETAILS Nov 24, 2004@14:20:06 Page: 1 of 3

> Patient: ADTPATIIENT,ONE (000769873) DOB: 04/04/50

> ICN: 5000001383V161240 CMOR: ALBANY

> Flag Name: BEHAVIORAL

> Flag Type: BEHAVIORAL

> Flag Category: I (NATIONAL)

> Assignment Status: ACTIVE

> Initial Assignment: 08/11/04@12:37:39

> Last Review Date: 08/11/04

> Next Review Date: 08/11/06

> Owner Site: XXXXXXXXXXX

> Originating Site: XXXXXXXXXXX

> Record Flag Assignment Narrative:

> This patient displayed a knife during the interview process.

> =========================\<Assignment History\>====================

> 1\. Action: NEW ASSIGNMENT

> Action Date: 03/31/03@12:20:42

> Entered By: ADTPROVIDER,ONE

> Approved By: ADTPROVIDER,ONE

> Progress Note: PATIENT RECORD FLAG CATEGORY I

> Action Comments:

> ----------------

> New record flag assignment.

> Select Action:Quit//

> Note: If the screen display request is not from the Owner Site of the patient’s PRF Assignment, the “Progress Note:” field will not be included in the display screen.

## Active PRF Assignments display modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When performing a VistA Patient Lookup, the display of a patient’s Active PRF Assignment detail has been enhanced to include the following new detail line to indicate whether or not the PRF Assignment Action has been linked to a TIU Progress Note:

Progress Note Linked: YES/NO

The new detail line will not be displayed if the displaying site is not the Owner of the PRF Assignment.

Select PATIENT NAME: ADTPATIIENT,ONE 7-1-71 000792468 NO NSC VETERAN

\>\>\> Active Patient Record Flag(s):

\<BEHAVIORAL\> CATEGORY I

Do you wish to view active patient record flag details? YES//

...HMMM, LET ME THINK ABOUT THAT A MOMENT..

1\. Flag Name: \<BEHAVIORAL\>

Category: I (NATIONAL)

Type: BEHAVIORAL

Assignment Narrative:

Test string for assignment narrative data input.

Assignment Details:

Initial Assignment: Nov 25, 2003

Approved By: ADTPROVIDER,ONE

Next Review Date: May 31, 2004

Owner Site: 1ALBANY

Originating Site: 1ALBANY

Progress Note Linked: YES

Select Action:Next Screen// NEXT SCREEN

## Edit Flag Assignment modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Flag Assignment \[DGPF EDIT ASSIGNMENT\] action of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT MENU\] option has been modified to provide a new action code to be selected during the edit assignment data entry process.

The new Action code name is: Entered in Error

The new action code will be used when the User is prompted to “Select an assignment action:” during the Edit Flag Assignment action. The new action code will be available for selection by both Category I or Category II Patient Record Flag Assignments.

When the action code “Entered in Error” is selected, the user will be prompted to edit the assignment narrative, enter who approved the change, and enter the reason for editing the assignment prior to filing the update.

Record Flag Assignments marked with the action code of “Entered in Error” will be considered as an Inactive Patient Record Flag Assignment.

The edit assignment action code “Entered in Error” will not be presented as a selection for use by Category I (National) PRF Assignments until the patch install compliance date has been reached. This will prevent a potential problem of PRF Phase I sites rejecting the "Entered in Error" action code shared from a site that has installed the PRF Phase II software.

Category II (Local) PRF Assignments are not affected by this activation date.

The following is an example of the “Entered in Error” selection process:

Select Action:Quit// EF Edit Flag Assignment

Select Record Flag Assignment: (1-4): 1

Select one of the following:

C Continue Assignment

I Inactivate Assignment

E Entered in Error

Select an assignment action: E Entered in Error

Would you like to edit the assignment narrative? YES// YES

EDIT Option: Edit line: 1

1\>Patient assaulted Head Nurse.

Replace ... With THIS ASSIGNMENT WAS ENTERED IN ERROR for the patient.

Replace \<return key\>

Edit line: \<return key\>

EDIT Option: \<return key\>

Approved By: ADTPROVIDER,ONE

Enter the reason for editing this assignment:

1\> The wrong patient ID was entered by the data entry clerk.

2\>\< return key\>

EDIT Option: \<return key\>

Would you like to file the assignment changes? YES// YES

Updating the patient’s record flag assignment...

\>\>\> Assignment was filed successfully.

\>\>\> HL7 message sent...updating patient's sites of record.

## Record Flag Management Screen Re-Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following 2 screen Actions of the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] Option have been modified to provide the ability to redisplay the screen details prior to filing the PRF Flag Management data entry.

> DGPF RECORD FLAG MANAGEMENT

> AF Add New Record Flag

> EF Edit Record Flag

######### The following example is the RECORD FLAG MANAGEMENT option screen display:

######### 

> REVIEW OF ADD NEW RECORD FLAG DATA INPUT BEFORE FILING

> ------------------------------------------------------

> Flag Name: PANCREATITIS

> Flag Category: II (LOCAL)

> Flag Type: RESEARCH

> Flag Status: ACTIVE

> Review Frequency Days: 444

> Notification Days: 33

> Review Mail Group: DGPFZ SARS RESEARCH

> Progress Note Title: PATIENT RECORD FLAG CATEGORY II – TESTING FLAG

> Enter/Edit On: 1/14/2004@14:16:42

> Enter/Edit By: ADTEMPLOYEE,ONE

> Principal Investigator(s): ADTPROVIDER,ONE

> Flag Description:

> -----------------

> This flag is for monitoring pancreatitis.

> Reason For Flag Enter/Edit:

> ---------------------------

> New Local Patient Record Flag entered.

> Do you want to review again? NO// NO

> Would you like to file this new local record flag? YES// YES

> Filing the new local record flag...

> \>\>\> Local record flag was filed successfully.

> Enter RETURN to continue or '^' to exit:

## Record Flag Assignment Screen Re-Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following 3 screen Actions of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] Option have been modified to provide the ability to redisplay the screen details prior to filing the PRF Assignment data entry.

> DGPF RECORD FLAG ASSIGNMENT

> AF Assign Flag

> EF Edit Flag Assignment

> CO Change Assignment Ownership

> The following example is the RECORD FLAG ASSIGNMENT option screen display:

> REVIEW OF ASSIGN FLAG DATA INPUT BEFORE FILING

> ----------------------------------------------

> Patient Name: ADTPATIIENT,ONE

> Flag Name: BEHAVIORAL

> Flag Type: BEHAVIORAL

> Flag Category: I (NATIONAL)

> Assignment Status: ACTIVE

> Initial Assignment: 1/13/2004@13:57:05

> Last Review Date: N/A

> Next Review Date: 4/1/2005

> Owner Site: ALBANY

> Originating Site: ALBANY

> Assignment Action: NEW ASSIGNMENT

> Action Date: 1/13/2004@13:57:06

> Entered By: ADTEMPLOYEE,ONE

> Approved By: ADTPROVIDER,ONE

> Record Flag Assignment Narrative:

> ---------------------------------

> Patient was verbally abusive during an outpatient visit.

> Action Comments:

> ----------------

> New record flag assignment.

> Do you want to review again? NO// NO

> Would you like to file this new record flag assignment? YES// YES

> Updating the patient's record flag assignment...

> \>\>\> Assignment was filed successfully.

> Enter RETURN to continue or '^' to exit:

## New PRF Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Record Flag Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Four (4) new PRF report options have been added to the Record Flag Reports Menu \[DGPF RECORD FLAG REPORTS MENU\] option. This menu option is accessed through the master menu for the Patient Record Flags module, Patient Record Flags Main Menu \[DGPF PATIENT RECORD FLAGS MAIN MENU\]. The DGPF PRF ACCESS security key locks these menu options.

> NLR Assignment Action Not Linked Report

> PAR Patient Assignments Report

> BAR Assignments Approved By Report

> IAR Assignments by Principal Investigator Report

### PRF Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flags Main Menu

> \[DGPF RECORD FLAGS MAIN MENU\]

> \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|

> \|------RM Record Flag Reports Menu

> \| \[DGPF RECORD FLAG REPORTS MENU\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------NLR Assignment Action Not Linked Report

> \| \| \[DGPF ACTION NOT LINKED REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------FAR Flag Assignment Report

> \| \| \[DGPF FLAG ASSIGNMENT REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------PAR Patient Assignments Report

> \| \| \[DGPF PATIENT ASSIGNMENT REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------ADR Assignments Due For Review Report

> \| \| \[DGPF ASSIGNMENT DUE REVIEW RPT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------BAR Assignments Approved By Report

> \| \| \[DGPF APPROVED BY REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------IAR Assignments by Principal Investigator Report

> \| \| \[DGPF PRINCIPAL INVEST REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------FA Record Flag Assignment

> \| \[DGPF RECORD FLAG ASSIGNMENT\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------FM Record Flag Management

> \| \[DGPF RECORD FLAG MANAGEMENT\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------IRM PRF System Configuration

> \[DGPF PRF SYSTEM CONFIGURATION\]

> \*\*LOCKED: DGPF PRF CONFIG\*\*

## Assignment Action Not Linked Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Assignment Action Not Linked Report \[DGPF ACTION NOT LINKED REPORT\] can be accessed from the Record Flag Reports Menu option. This new option provides the ability to display or print all of the PRF History Assignment Actions that are not linked to a Progress Note.

Only PRF Assignment records that are owned by the current reporting site will be reported on. Users will have the ability to run the report by either or both Category I (National) or Category II (Local) PRF Assignments. The user can then enter a date range to limit the search for Record Flag Assignments. The DGPF PRF ACCESS security key locks this option.

## Patient Assignments Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Patient Assignments Report \[DGPF PATIENT ASSIGNMENT REPORT\] can be accessed from the Record Flag Reports Menu option. This new option provides the ability to display or print all Record Flag Assignments assigned to a specific patient. Users will have the ability to run the report by either/or both Active or Inactive status PRF Assignments the patient has been assigned to. The DGPF PRF ACCESS security key locks this option.

## Assignments Approved By Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Assignments Approved By Report \[DGPF APPROVED BY REPORT\] can be accessed from the Record Flag Reports Menu option. This new option provides the ability to display or print all of the Patient Record Flag Assignments for the person who Approved the assignment of the record flag for the patient. Users will have the ability to run the report by either a Single Approved By Person or All Approved By Persons. The user will then select to run the report by either or both Category I (National) or Category II (Local) PRF Assignments. The user will then select to run the report for either or both Active or Inactive status PRF Assignments the person has approved. The user can then enter a date range to limit the search for PRF Assignments. The DGPF PRF ACCESS security key locks this option.

## Assignments by Principal Investigator Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Assignments by Principal Investigator Report \[DGPF PRINCIPAL INVEST REPORT\] can be accessed from the Record Flag Reports Menu option. This new option provides the ability to display or print all of the PRF Assignments for a selected Principal Investigator.

Only Research Type record flags will have a Principal Investigator assigned for that flag. Users will have the ability to run the report by either a Single Principal Investigator or All Principal Investigators. The user will then select to run the report for either/or both Active or Inactive status PRF Assignments. The user can then enter a date range to limit the search for PRF Assignments. The DGPF PRF ACCESS security key locks this option.

# Registration Package - Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical information related to the Patient Record Flags Phase II (DG\*5.3\*554) patch. Complete details regarding this patch are found in the Patient Record Flags Phase II (DG\*5.3\*554) patch message generated from the National Patch Module (NPM) on Forum.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new report options have been added to the Record Flag Reports Menu \[DGPF RECORD FLAG REPORTS MENU\] option.

## DGPF ACTION NOT LINKED REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | DGPF ACTION NOT LINKED REPORT                                                                                                                                       |
| Menu Text   | Assignment Action Not Linked Report                                                                                                                                 |
| Description | This option will be used to display or print all of the PRF Assignments that are not linked to progress notes for any assignment history records of the Owner Site. |
| Type        | Run Routine                                                                                                                                                         |
| Package     | Registration                                                                                                                                                        |
| Routine     | EN^DGPFRAL                                                                                                                                                          |
| Lock        | DGPF PRF ACCESS                                                                                                                                                     |

## DGPF APPROVED BY REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | DGPF APPROVED BY REPORT                                                                                                                                                       |
| Menu Text   | Assignments Approved by Report                                                                                                                                                |
| Description | This option will be used to display or print all of the Patient Record Flag Assignments for the person who approved the assignment of the patient record flag to the patient. |
| Type        | Run Routine                                                                                                                                                                   |
| Package     | Registration                                                                                                                                                                  |
| Routine     | EN^DGPFRAB                                                                                                                                                                    |
| Lock        | DGPF PRF ACCESS                                                                                                                                                               |

## DGPF PATIENT ASSIGNMENT REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | DGPF PATIENT ASSIGNMENT REPORT                                                                                                           |
| Menu Text   | Patient Assignments Report                                                                                                               |
| Description | This option will be used to display or print all record flag assignments of a patient for either Category I or Category II Record Flags. |
| Type        | Run Routine                                                                                                                              |
| Package     | Registration                                                                                                                             |
| Routine     | EN^DGPFRPA                                                                                                                               |
| Lock        | DGPF PRF ACCESS                                                                                                                          |

## DGPF PRINCIPAL INVEST REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | DGPF PRINCIPAL INVEST REPORT                                                                                                                                                                                         |
| Menu Text   | Assignments by Principal Investigator Report                                                                                                                                                                         |
| Description | This new option will be used to display or print all of the Patient Record Flag Assignments for a Principal Investigator. Only Research Type record flags will have a Principal Investigator assigned for that flag. |
| Type        | Run Routine                                                                                                                                                                                                          |
| Package     | Registration                                                                                                                                                                                                         |
| Routine     | EN^DGPFRPI                                                                                                                                                                                                           |
| Lock        | DGPF PRF ACCESS                                                                                                                                                                                                      |

## New / Modified Fields of the PRF Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new field will be added to file (#26.15) PRF NATIONAL FLAG and file (#26.11) PRF LOCAL FLAG to store the IEN of the associated TIU PRF Progress Note Title.

A new field will be added to file (#26.14) PRF ASSIGNMENT HISTORY to store the IEN of the associated TIU PRF Progress Note when it is created in TIU.

The (#.03) ACTION field of the (#26.14) PRF ASSIGNMENT HISTORY file has a new Action code added to the current set of codes with a value and name of: 5:ENTERED IN ERROR

A new field will be added to the (#26.18) PRF PARAMETERS file to store the date that is used to restrict access to specific Patient Record Flags functionality in production environments until all sites have installed the PRF Phase II software.

The following is a list of new and modified fields being exported with this patch. Records in any of the Patient Record Flag files (#26.11 through \#26.18) should not be added, edited, or deleted except through the installation of national patches or use of the Patient Record Flag software that is part of Registration. Doing so would likely cause the Patient Record Flag database to become corrupted.

|           |                        |                             |                                                                                                                                                                                                  |
|-----------|------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File# | File Name          | Field \# / Name         | Description                                                                                                                                                                                  |
| 26.11     | PRF LOCAL FLAG         | (#.07) TIU PN TITLE         | This field contains the Category II Progress Note Title that is associated with this Patient Record Flag.                                                                                        |
| 26.14     | PRF ASSIGNMENT HISTORY | (#.03) ACTION               | This field contains the event that occurred to create the PRF ASSIGNMENT HISTORY record. Sample events are NEW ASSIGNMENT, CONTINUE, INACTIVATE, REACTIVATE and ENTERED IN ERROR.                |
|           |                        | (#.06) TIU PN LINK          | This field contains the IEN of the TIU Progress Note that is linked to this PRF Assignment History record. Integration Agreement \#4387.                                                         |
| 26.15     | PRF NATIONAL FLAG      | (#.07) TIU PN TITLE         | This field contains the Category I Progress Note Title that is associated with this Patient Record Flag.                                                                                         |
| 26.18     | PRF PARAMETERS         | (#6) PRF PHASE 2 ACTIVATION | This field contains the date that is used to restrict access to Specific Patient Record Flags functionality in production environments until all sites have installed the PRF Phase II software. |

## New Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new Database Integration Agreements (DBIA) have been added.

## DBIA (#4383) DGPF ASSIGNMENT LINK TIU PN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry point is available to external packages by Controlled Subscription to DBIA \#4383 only.

\$\$GETHTIU^DGPFAPI1(DFN,DGTITLE,TARGET_ROOT)

This function entry point is used to search for and retrieve specific data for a patient’s (active or inactive) Patient Record Flag Assignment. The TIU Progress Note Title IEN will be used to search for the patient assignment that is linked by the associated Patient Record Flag to that TIU Progress Note Title. If the request is not from the Owner Site of the Assignment, no data is returned. All Patient Record Flag data will be returned in a user named closed root array (local or global) that will contain multiple subscripts. This array is referred to as "TARGET_ROOT" in this text. Note that the TARGET_ROOT will be initialized (killed) before being used.

## DBIA (#4384) DGPF FILE/DELETE TIU PN LINK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry point is available to external packages by Controlled Subscription to DBIA \#4384 only.

\$\$STOTIU^DGPFAPI2(DFN,DGAIEN,DGHIEN,DGTIUIEN)

This function entry point is used to File (Link) the IEN of a TIU Progress Note of the TIU DOCUMENT file (#8925) to the TIU PN LINK Field (#.06) of the PRF ASSIGNMENT HISTORY file (#26.14).

## DBIA (#4386) DGPF ASSOCIATED FLAG PN TITLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This IA will document the fact that in the PRF LOCAL FLAG file (#26.11) and the PRF NATIONAL FLAG file (#26.15), there is a field called TIU PN TITLE (Field \#.07) which points to the TIU DOCUMENT DEFINITION file (#8925.1).

The Registration package requests permission to store a pointer to the NAME field (#.01) of the TIU DOCUMENT DEFINITION file (#8925.1).

## DBIA (#4387) DGPF ASSIGNMENT TIU PN LINK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This IA will document the fact that in the PRF ASSIGNMENT HISTORY file (#26.14), there is a field called TIU PN LINK (Field \#.06) which points to the TIU DOCUMENT file (#8925).

The Registration package requests permission to store the pointer IEN of a TIU PROGRESS NOTE to the PRF ASSIGNMENT HISTORY file (#26.14) field (#.06).

## Modified Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Database Integration Agreement (DBIA) has been modified.

## DBIA (#3860) DGPF PATIENT RECORD FLAG – ACTIVE ASSIGNMENT API 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry point is available to external packages by Controlled Subscription to DBIA \#3860 only.

\$\$GETACT^DGPFAPI(DGDFN,TARGET_ROOT)

This entry point is used to obtain only ACTIVE Patient Record Flag (PRF) Assignment information for a patient that can be used for Inquiry and Reporting purposes. All ACTIVE Patient Record Flag Assignments will be returned in a multiple subscripted local or global array, "TARGET_ROOT", as a closed root reference. Note that the TARGET_ROOT will be initialized (killed) before being used.

This DBIA enhancement will add the following two new data elements to the returned closed root reference array:

> 1\. The TIU PN TITLE (#.07) field of the Record Flag name in the PRF LOCAL FLAG (#26.11) or PRF NATIONAL FLAG (#26.15) file.

> 2\. The TIU PN LINK (#.06) field of the patient Assignment History record in the PRF ASSIGNMENT HISTORY (#26.14) file.

## New / Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine(s)</strong></td>
<td><strong>New/Modified</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>DGPFAA2</td>
<td>Modified</td>
<td>Functions and procedures to validate, store and retrieve PRF ASSIGNMENT (#26.13) file data.</td>
</tr>
<tr class="odd">
<td>DGPFAAH</td>
<td>Modified</td>
<td>Functions and procedures to validate, store and retrieve PRF ASSIGNMENT HISTORY (#26.14) file data.</td>
</tr>
<tr class="even">
<td><p>DGPFALF,</p>
<p>DGPFALF1</p></td>
<td>Modified</td>
<td>Functions and procedures to validate, store and retrieve PRF LOCAL FLAG (#26.11) file data.</td>
</tr>
<tr class="odd">
<td>DGPFANF</td>
<td>Modified</td>
<td>Function to retrieve PRF NATIONAL FLAG (#26.15) file data.</td>
</tr>
<tr class="even">
<td><p>DGPFAPI,</p>
<p>DGPFAPI1,</p>
<p>DGPFAPI2</p></td>
<td>Modified</td>
<td>Functions and procedures used by packages and modules external to the Patient Record Flags module.</td>
</tr>
<tr class="odd">
<td>DGPFDD</td>
<td>Modified</td>
<td>Trigger, executable help and output transform support functions and procedures for all Patient Record Flag files.</td>
</tr>
<tr class="even">
<td>DGPFHLL</td>
<td>Modified</td>
<td>Functions and procedures to store and retrieve PRF HL7 TRANSMISSION LOG (#26.17) file data.</td>
</tr>
<tr class="odd">
<td><p>DGPFLF3,</p>
<p>DGPFLF4,</p>
<p>DGPFLF5</p></td>
<td>Modified</td>
<td>Entry point for the DGPF EDIT FLAG action protocol.</td>
</tr>
<tr class="even">
<td>DGPFLF6</td>
<td>Modified</td>
<td>Support functions for the DGPF RECORD FLAG MANAGEMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLFD1</td>
<td>Modified</td>
<td>Entry point and display builder for DGPF FLAG DETAIL display List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMA2</td>
<td>Modified</td>
<td>Entry point for DGPF ASSIGN FLAG action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLMA3</td>
<td>Modified</td>
<td>Entry point for DGPF EDIT FLAG ASSIGNMENT action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMA4</td>
<td>Modified</td>
<td>Entry point for DGPF CHANGE ASSIGNMENT OWNERSHIP action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLMD1</td>
<td>Modified</td>
<td>Entry point for the DGPF ACTIVE ASSIGNMENTS List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMU1</td>
<td>Modified</td>
<td>Entry point and display builder for the DGPF ASSIGNMENT DETAIL display List Template.</td>
</tr>
<tr class="odd">
<td>DGPFPARM</td>
<td>Modified</td>
<td>PRF PARAMETER FILE (#26.18) field enter/edit utility routine.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine(s)</strong></td>
<td><strong>New/Modified</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p>DGPFRAB,</p>
<p>DGPFRAB1</p></td>
<td>New</td>
<td>Assignments Approved by Report prompts and builder.</td>
</tr>
<tr class="odd">
<td><p>DGPFRAL,</p>
<p>DGPFRAL1</p></td>
<td>New</td>
<td>Assignment Action Not Linked Report prompts and builder.</td>
</tr>
<tr class="even">
<td><p>DGPFRFA,</p>
<p>DGPFRFA1</p></td>
<td>Modified</td>
<td>Flag Assignment report prompts and builder.</td>
</tr>
<tr class="odd">
<td><p>DGPFRPA</p>
<p>DGPFRPA1</p></td>
<td>New</td>
<td>Patient Assignments Report prompts and builder.</td>
</tr>
<tr class="even">
<td><p>DGPFRPI</p>
<p>DGPFRPI1,</p>
<p>DGPFRPI2</p></td>
<td>New</td>
<td>Assignments by Principal Investigator Report prompts and builder.</td>
</tr>
<tr class="odd">
<td><p>DGPFUT,</p>
<p>DGPFUT2</p></td>
<td>Modified</td>
<td>General support functions and procedures used by all Patient Record Flags interfaces.</td>
</tr>
<tr class="even">
<td><p>DGPFUT3,</p>
<p>DGPFUT4,</p>
<p>DGPFUT5</p></td>
<td>New</td>
<td>These routines are used for re-displaying the Flag Management and Flag Assignment Add and Edit Action Screen Detail before filing the record entries.</td>
</tr>
<tr class="odd">
<td>DG53P554</td>
<td>New</td>
<td>This ENV/PRE/POST installation routine will file the National Category I Progress Note Title name, "PATIENT RECORD FLAG CATEGORY I" (pointer to the (#8925.1) TIU DOCUMENT DEFINITION file), into the (#26.15) PRF NATIONAL FLAG file, field (.07) TIU PN TITLE. (may be deleted after successful patch installation)</td>
</tr>
</tbody>
</table>

# Text Integrated Utilities (TIU) - Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the functionality being implemented by the TEXT INTEGRATION UTILITIES package.

PRF notes are required by policy whenever a PRF flag is assigned to document the reasons for the assignment. The Flag Assignment Action is entered first; then a new note is written and linked to the assignment action.

Patch TIU\*1\*184 together with DG\*5.3\*554 provides functionality to link notes to assignment actions, and TIU\*1\*184 ensures that every NEW PRF note is linked to a corresponding PRF Flag assignment action. Note that neither Registration nor TIU enforces the reverse, that every PRF Flag assignment action be linked to a new PRF note. Instead, flag assignment actions lacking linked notes appear in PRF Registration reports so that they can be followed up appropriately.

In addition to ensuring that every NEW PRF note is linked to a corresponding PRF Flag assignment action, TIU also provides an action to link existing, unlinked PRF notes (those created before the implementation of PRF II) to flag assignment actions. For this purpose, existing List Manager action LINK TO REQUEST has been changed to read: LINK TO OTHER APPLIC. Action LINK TO OTHER APPLIC appears on menus wherever action LINK TO REQUEST appeared before. The action is context-sensitive: it links a Consult Result to a Request, but links a PRF note to a flag. This action may also be used to correct PRF notes mistakenly linked to an incorrect flag action.

Authorization for linking or re-linking an existing PRF note to a flag is granted using ASU Business Rules for new USR action LINK TO FLAG, exported in patch USR\*1\*27.

Besides these new linking capabilities, this patch updates existing note actions such as Change Title, Reassign, TIU Upload, etc., to ensure that any NEW PRF notes are linked to Flag assignment actions.

## Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If setup is performed improperly, it could affect Patient Record Flags operation. Please review the Patient Record Flags Phase II Handbook for Test Sites distributed with test versions of TIU\*1\*184 and available on the VA Web at: http: <span class="mark">REDACTED</span>

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## TEXT INTEGRATION UTILITIES (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### The following enhancements have been made to the TEXT INTEGRATION UTILITIES option to link a PRF note to a specific Patient Record Flag Assignment action.

> CPRS GUI and TIU List Manager options to create new TIU documents have been modified to ensure that every NEW document with a PRF Title is linked to a corresponding PRF Flag assignment action. This includes TIU Upload options.

> CPRS GUI and TIU LM actions taken on existing notes such as Change Title, Reassign, etc., have been modified to ensure that any NEW PRF notes created in the process of changing existing notes are linked to Flag assignment actions.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## TEXT INTEGRATION UTILITIES (TIU) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIU provides a new action to link existing, unlinked PRF notes (those created before the implementation of PRF II) to flag assignment actions. This new action is performed using existing List Manager action LINK TO REQUEST, which now appears as action LINK TO OTHER APPLIC on menus wherever action LINK TO REQUEST appeared before. The action is available either directly or under submenu action ‘Link…’ on the following menus:

Text Integration Utilities (MRT) ... \[TIU MAIN MENU MRT\]

Progress Notes/Discharge Summary \[TIU\] ... \[TIU MAIN MENU CLINICIAN\]

Text Integration Utilities (MIS Manager) ... \[TIU MAIN MENU MGR\]

This action may also be used to correct PRF notes mistakenly linked to an incorrect flag action.

## Uploading PRF Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OVERVIEW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site intends to upload PRF notes, the site MUST set up new Upload parameters for Document Classes PATIENT RECORD FLAG CAT I and PATIENT RECORD FLAG CAT II.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

IMPORTANT WARNING

Do not upload PRF notes as Progress Notes, using the existing upload set-up

for Progress Notes. If your site plans to upload PRF notes, upload

parameters MUST be set explicitly for Document Classes PATIENT RECORD FLAG

CAT I and PATIENT RECORD FLAG CAT II. Failure to do so will result in PRF

notes which ARE NOT LINKED TO FLAGS and as new PRF notes, they will be considered

deficient since all newly created PRF notes are linked to flags in Phase II.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

It is NOT NECESSARY to include in the uploaded file the flag assignment history action the note should be linked to. Linking to the appropriate flag action is done automatically by PRF upload options. If the appropriate action cannot be determined, PRF upload options will create a filing error.

Notes for new assignments should upload without filing error as long as the notes are uploaded after the flag action is entered. However, notes for assignments with multiple actions will create a filing error if previous action(s) do not have linked notes.

## PRF UPLOAD PARAMETERS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for uploaded PRF notes to be linked to flags, upload parameters MUST be set explicitly for Document Classes PATIENT RECORD FLAG CAT I and PATIENT RECORD FLAG CAT II.

Upload parameters for PRF notes are nearly the same as for Progress Notes, with the exception of the following fields, which are populated upon installing TIU\*1\*184 by the post-install routine for 184:

\#4 UPLOAD LOOK-UP METHOD: D LOOKUP^TIUPUTPF

\#4.5 UPLOAD POST-FILING CODE: D FOLLOWUP^TIUPUTPF(TIUREC("#"))

\#4.8 UPLOAD FILING ERROR CODE: D PNFIX^TIUPFFIX

The site must enter the other parameters, including captions.

Here is an example of upload setup for Document Class PATIENT RECORD FLAG CAT II. (The setup for Document Class PATIENT RECORD FLAG CAT I is similar.)

DOCUMENT DEFINITION: PATIENT RECORD FLAG CAT II DOCUMENT CLASS

ABBREVIATION: PRF

LAYGO ALLOWED: YES

UPLOAD TARGET FILE: TIU DOCUMENT

Select TARGET TEXT FIELD: REPORT TEXT

UPLOAD LOOK-UP METHOD: D LOOKUP^TIUPUTPF

UPLOAD POST-FILING CODE: D FOLLOWUP^TIUPUTPF(TIUREC("#"))

UPLOAD FILING ERROR CODE: D PNFIX^TIUPFFIX

CAPTION: AUTHOR

ITEM NAME: DICTATING PROVIDER

FIELD NUMBER: 1202

LOOKUP LOCAL VARIABLE NAME:

TRANSFORM CODE:

EXAMPLE ENTRY: CPRSPROVIDER,ONE

CLINICIAN MUST DICTATE: YES

REQUIRED FIELD?: YES

CAPTION: DATE/TIME OF DICT

ITEM NAME: DICTATION DATE/TIME

FIELD NUMBER: 1307

LOOKUP LOCAL VARIABLE NAME: TIUDDT

TRANSFORM CODE:

EXAMPLE ENTRY: 5/16/97@09:25

CLINICIAN MUST DICTATE: NO

REQUIRED FIELD?: YES

CAPTION: LOCATION

ITEM NAME: PATIENT LOCATION

FIELD NUMBER: 1205

LOOKUP LOCAL VARIABLE NAME: TIULOC

TRANSFORM CODE:

EXAMPLE ENTRY: MEDICAL-CONSULT

CLINICIAN MUST DICTATE: YES

REQUIRED FIELD?: YES

CAPTION: SSN

ITEM NAME: PATIENT SSN

FIELD NUMBER: .02

LOOKUP LOCAL VARIABLE NAME: TIUSSN

TRANSFORM CODE: S X=\$TR(X,"-/","")

EXAMPLE ENTRY: 666-12-1234

CLINICIAN MUST DICTATE: YES

REQUIRED FIELD?: YES

CAPTION: TITLE

ITEM NAME: TITLE OF NOTE

FIELD NUMBER: .01

LOOKUP LOCAL VARIABLE NAME: TIUTITLE

TRANSFORM CODE:

EXAMPLE ENTRY: PATIENT RECORD FLAG CATEGORY II - RISK OF WANDERING

CLINICIAN MUST DICTATE: YES

REQUIRED FIELD?: YES

CAPTION: TRANSCRIBER

ITEM NAME: TRANSCRIBER

FIELD NUMBER: 1302

LOOKUP LOCAL VARIABLE NAME:

TRANSFORM CODE:

EXAMPLE ENTRY: K5420

CLINICIAN MUST DICTATE: NO

REQUIRED FIELD?: NO

CAPTION: VISIT/EVENT DATE

ITEM NAME: VISIT/EVENT DATE

FIELD NUMBER: .07

LOOKUP LOCAL VARIABLE NAME: TIUVDT

TRANSFORM CODE:

EXAMPLE ENTRY: 5/15/97@08:15

CLINICIAN MUST DICTATE: YES

REQUIRED FIELD?: YES

The header for the PATIENT RECORD FLAG CAT II DOCUMENT CLASS is now

defined as:

\$HDR: PATIENT RECORD FLAG CAT II

LOCATION: MEDICAL-CONSULT

AUTHOR: CPRSPROVIDER,ONE

DATE/TIME OF DICT: 5/16/97@09:25

EXPECTED COSIGNER: CPRSPROVIDER,TWO

SSN: 666-12-1234

VISIT/EVENT DATE: 5/15/97@08:15

TITLE: PATIENT RECORD FLAG CATEGORY II -

RISK OF WANDERING

TRANSCRIBER: K5420

\$TXT

PATIENT RECORD FLAG CAT II Text

\$EOM

Note that there is no caption for Linked Flag. Linking to the appropriate flag action is done automatically by PRF upload options. If the appropriate action cannot be determined, PRF upload options will create a filing error.

## PRF UPLOAD FILING ERRORS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there is only one appropriate flag action available to link the note to, for the uploaded title and patient, PRF upload code will link the uploaded note to that action. If there is no appropriate action available, or if there are multiple actions available, PRF upload options will create a filing error. (PRF notes cannot be created without a link under the new PRF PHASE II.)

If flag assignments were made before Phase II and notes have not been written for some of those actions, or existing notes have not been linked for actions, then uploading notes for these assignments will create filing errors. Also, uploading notes for assignments with multiple actions, for example assignments which have been continued after review, will generate filing errors if previous actions have not been linked to notes.

In cases where more than one action is available, the recipient may be able to determine from the date and text of the note which action to select and so resolve the alert. (The text of the note can be read from the buffer by replying NO when asked, Inquire to patient record?) In some cases, the author will need to be consulted.

Sites who intend to upload PRF notes should designate persons qualified to correctly link PRF notes as filing error recipients for PRF documents for those cases where notes could not be automatically linked. These persons must have authorization to enter PRF notes.

In cases where NO action is available, the author should be consulted. A new action may need to be entered or a different patient and/or title may need to be selected.

In cases where NO action is available, and it is not appropriate to enter a new flag action or to enter a different patient and/or PRF title, it may be necessary in consultation with the author to upload the note as a Progress Note with a Progress Note title. To do so, edit the buffer, change the Header to PROGRESS NOTES, change the title to some PN Title created for this purpose, (like UNLINKABLE FORMER PRF NOTES), and re-file the note. This will resolve the filing error, and the author, the filing error recipient, or MIS must then deal appropriately with the unsigned PN – change it back to a PRF title for which there are actions, change it to the appropriate PN title, or perhaps delete the note.

DO NOT change the header to PROGRESS NOTES unless you also change the title to a non-PRF PN title. Doing so would create an unlinked PRF note, and PRF Phase II does not permit the creation of unlinked PRF notes.

## INTERDISCIPLINARY NOTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRF notes must NOT be used as Interdisciplinary Notes, either as parent notes or as child notes.

## GROUP NOTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRF notes must NOT be used as Group Notes.

## BUSINESS RULES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In setting up, sites will need to write business rules for action LINK TO FLAG before users can link existing notes created before Phase II of PRF or re-link Patient Record Flag (PRF) notes that have been improperly linked.

Your rules will probably bear some resemblance to the rules for linking Consults; that is, for unsigned notes, authors should be permitted to re-link their own notes. Since this re-link action is only available in the List Manager, others should also be authorized to re-link unsigned notes when requested to do so by the author. For signed notes, re-linking should be reserved for a small group of users who are familiar with both TIU and Patient Record Flags and are qualified to correct chart documents. Retracted notes are automatically unlinked upon retraction and must never be re-linked.

Rules will need to be set for both PRF Document Classes: PATIENT RECORD FLAG CAT I and PATIENT RECORD FLAG CAT II.

Note that this authorization is required to link existing notes created before Phase II of PRF. It is NOT required to link new notes during note creation.

# Text Integrated Utilities (TIU) - Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical information related to the Patient Record Flags Phase II (TIU\*1.0\*184) patch.

PRF notes are required by policy, whenever a PRF flag is assigned, to document the reasons for the assignment. The Flag Assignment Action is entered first; then a new note is written and linked to the assignment action. Neither Registration nor TIU enforces the reverse, that every PRF Flag assignment action be linked to a new PRF note. Instead, flag assignment actions lacking linked notes appear in PRF Registration reports so that they can be followed up appropriately.

## TEXT INTEGRATION UTILITIES (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following List Manager actions are new or have been modified:

| Action                               | Commentary                                                                                                                                                                                                                                                                      |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link to Other Applic                     | Replaces Link to Request. Works differently for PRF notes than for Consults notes. Appears at the bottom of TIU document review screens or as a sub-action under the action Link. For PRF notes links a note to a PRF action or allows correction of an erroneous PRF link. |
| Link to Request                          | Changed to Link to Other Applic.                                                                                                                                                                                                                                                |
| Change Title, Reassign, TIU Upload, etc. | Modified to ensure that notes with PRF titles are linked to PRF assignment actions.                                                                                                                                                                                                 |

## New / Modified Fields of the TIU Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two computed fields. PRF FLAG is a computed field in TIU DOCUMENT DEFINITION file (#8925.1, .15) and PRF FLAG ACTION is a computed field in the TIU DOCUMENT file (#8925, 1407).

## COMPUTED FIELD PRF FLAG 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRF FLAG applies only to PRF titles. The PRF FLAG of a PRF title is the name of the Patient Record Flag associated with the title. (Notes cannot be written using a PRF title unless the title is associated with a flag and that flag is assigned to the given patient.)

If the title is not associated with a flag or the associated flag cannot be found, the field has value "?". If the Document Definition is not a title under Document Class PATIENT RECORD FLAG CAT I or PATIENT RECORD FLAG CAT II, the field has value NA for non-applicable.

Technical Note: Flags and their associations with titles are stored in file PRF LOCAL FLAG (#26.11) or in file PRF NATIONAL FLAG (#26.15).

## COMPUTED FIELD PRF FLAG ACTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRF FLAG ACTION applies only to PATIENT RECORD FLAG (PRF) notes. When a new flag is assigned to a given patient, or, after review, another action such as CONTINUE is taken on an existing flag assignment, a note must be written to document the clinical reasons for the action. Upon entry of the note, it is linked to the action it documents. Field PRF FLAG ACTION refers to this linked action.

The field contains the Date of the Action followed by the Name of the Action.

Example: 3/3/05 CONTINUE

If the PRF note is not linked to a flag action or the linked action date or name cannot be found, the field has value "?". If the note is not a PRF note (a note with a title under Document Class PATIENT RECORD FLAG CAT I or PATIENT RECORD FLAG CAT II), the field has value NA for non-applicable.

Technical Note: Flag Actions and their linked note entry numbers are stored in the PRF ASSIGNMENT HISTORY FILE (#26.14). The Date and Action are attributes of the Assignment History entry the note is linked to.

## New Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new Database Integration Agreement (DBIA) has been added.

## DBIA (4380) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry points are available to external packages by Controlled Subscription to DBIA \#4380 only.

\$\$GETLIST^TIUPRF(PRFCAT,TARGET)

Returns a list of titles (IEN^Name) from Category I, Category II, or both (depending on PRFCAT: 1=Category I, 2=Category II, 3=both.)

\$\$GETIEN^TIUPRF(TIUTTL)

Returns the IEN of the Document Definition corresponding to the input TITLE Name supplied.

\$\$GETTL^TIUPRF(TIUDA)

## DBIA (4839) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry points are available to external packages by Controlled Subscription to DBIA \#4839 only.

\$\$TIUPRFL^ISPFTTL(TITLEDA)

Returns a Boolean value if the TITLEDA is a PRF title.

## New / Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                |                  |                                                           |
|----------------|------------------|-----------------------------------------------------------|
| Routine(s) | New/Modified | Description                                           |
| TIUCNSLT       | Modified         | Consult code                                              |
| TIUEDI3        | Modified         | Additional Edit Code for notes                            |
| TIUFD          | Modified         | List Manager Document Definition display code             |
| TIUFHA1        | Modified         |                                                           |
| TIUFHA7        | Modified         |                                                           |
| TIUFHA8        | Modified         |                                                           |
| TIUFHLP1       | Modified         | More on-line help library                                 |
| TIUHELP        | Modified         | On-line help library                                      |
| TIUFL          | Modified         | Library of Modules and Functions for Document Definitions |
| TIUFLD         | Modified         | Modules and Functions for Document Definition display     |
| TIUFLF7        | Modified         |                                                           |
| TIULP          | Modified         |                                                           |

|                |                  |                                                |
|----------------|------------------|------------------------------------------------|
| Routine(s) | New/Modified | Description                                |
| TIUPEVNT       | Modified         | Event logger for upload/filer                  |
| TIUPFFIX       | New              | Resolve Upload Filing Errors for PRF Notes     |
| TIUPRF         | New              | API's for Patient Record Flags                 |
| TIUPRF1        | New              | Modules for Patient Record Flags               |
| TIUPRF2        | New              | RPCs for Patient Record Flags                  |
| TIUPRF3        | New              | More Modules for Patient Record Flags          |
| TIUPRFL        | New              | Library Functions for Patient Record Flags     |
| TIUPS184       | New              | Post-Install for Patient Record Flags II       |
| TIUPUTC        | Modified         | Document filer - captioned header              |
| TIUPUTPF       | New              | PRF Look-up Method for Upload                  |
| TIURB          | Modified         | More Review Screen Actions                     |
| TIURB2         | Modified         | More Review Screen Actions                     |
| TIURC1         | Modified         | Additional Review Screen Actions               |
| TIURD          | Modified         | Reassign actions                               |
| TIURE          | Modified         | Error handler actions for Upload               |
| TIURS1         | Modified         | Additional electronic signature (/es/) actions |
| TIUSRV         | Modified         | Silent server functions                        |
| TIUSRVP        | Modified         |                                                |
| TIUSRVP2       | Modified         |                                                |

# Authorization/Subscription (USR) - Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information related to the USR\*1\*27 patch.

## New / Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following enhancement has been made to the Authorization/Subscription Utility.

## NEW ACTION LINK TO FLAG (USR\*1.0\*27) patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### Patch USR\*1.0\*27 exports a new USR Action: LINK TO FLAG.

######### This action is used to grant permission to (re)-link existing flag documents to flag actions.

Business rules must be written granting permission to appropriate users before existing notes can be linked or re-linked. See patch description for USR\*1\*27 in the National Patch Module.

> **NOTE:** This permission is not required when linking notes during note creation.

# Authorization/Subscription (USR) - Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical information related to the USR\*1\*27 patch. Complete details regarding this patch are found in the NEW ACTION LINK TO FLAG (USR\*1.0\*27) patch message generated from the National Patch Module (NPM) on Forum.

## NEW ACTION LINK TO FLAG (USR\*1.0\*27) patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### The action LINK TO FLAG controls permission to link and re-link existing notes to flag actions.