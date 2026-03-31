---
title: SD 5.3 574 Technical and Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: patch
doc_subject: 574 Technical and
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*574
group_key: "SD:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - recall
  - clinic
  - sdrr
  - reminder
  - table
  - contents
  - routine
  - edit
  - outpatient
  - convert
page_count: 0
word_count: 4904
section_count: 19
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_574_tsg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_574_tsg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

![](sd-5-3-574-technical-and-security-guide/001.png)

Recall Reminder Technical &Security GuidePIMS V. 5.3 Scheduling ModulePatch SD\*5.3\*574May 2013

Office of Information and Technology (OI&T)

Office of Enterprise Development (OED)

Revision History

Initiated on 9/1/09

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>5/24/13</td>
<td>Patch SD*5.3*574</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/1/09</td>
<td><p>Patch SD*5.3*536 and</p>
<p>Patch OR*3.0*302 - Recall Reminder</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [# Implementation and Maintenance](#implementation-and-maintenance)
  - [Prior to Installation](#prior-to-installation)
  - [Namespace Conventions](#namespace-conventions)
  - [## ## Obsolete Options](#obsolete-options)
  - [Site Parameters](#site-parameters)
  - [## Conversion from Class III to Class I](#conversion-from-class-iii-to-class-i)
- [Files](#files)
  - [File List](#file-list)
  - [Template List](#template-list)
- [Routines](#routines)
  - [Routine List with Descriptions](#routine-list-with-descriptions)
- [Exported Options](#exported-options)
  - [Exported Security Keys](#exported-security-keys)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
    - [Integration References](#integration-references)
  - [Internal Relations](#internal-relations)
- [Callable Routines/Entry Points/Application Programmer Interfaces](#callable-routinesentry-pointsapplication-programmer-interfaces)
- [Mail Groups/Protocols](#mail-groupsprotocols)
  - [Mail Groups](#mail-groups)
  - [Protocols](#protocols)
- [Non-Applicable Components](#non-applicable-components)
  - [Archiving](#archiving)
  - [Cross-References](#cross-references)
  - [External Interfaces](#external-interfaces)
  - [Global Variables](#global-variables)
  - [Glossary](#glossary)
The Recall Reminder software is designed to allow facilities to implement recall scheduling. The software creates a ‘holding’ area for patients who will need to return to a clinic in the future. This time period has been determined to be a visit greater than 90 to 120 days in the future. At the discretion of the provider, individual patients may be scheduled further into the future. Patients are entered into the software for the date they are to return. Recall Reminder parameters are set by each site to determine the number of days prior to the recall date the notification cards or letters should be printed. The card or letter will instruct the patient to contact the VA to schedule an appointment which will not be made in the VistA Scheduling system until the patient contacts their facility.
It is recommended that sites give consideration to the best way to implement Recall Reminder at their site in that doing so takes a significant amount of time to train staff and educate veterans. Sites may choose to bring up different areas; for example, dental clinics, primary care, surgical clinics, etc., one at a time, moving on to the next area after successful implementation of the previous area.
This software was first intended for Primary Care use but now is being used in many clinical areas. Multiple Recall Reminder entries can be created for one patient. The software allows a user to enter/edit Recall Reminders by using either a standalone option or Appointment Management. Additionally, the software includes the ability to establish divisions (not to be confused with Medical Center Divisions) as well as teams to assist in greater manageability of the program. Please see the User Guide for additional information regarding setting up divisions when setting up site parameters.
The software also includes a number of reports to identify patients who haven’t scheduled their appointment as well as reports that will assist sites in the management of Recall Reminder.
The option Recall List Delinquencies \[SDRR RECALL DELINQUENCIES\] is a valuable tool that must be run on a regular basis to identify patients who have been sent Recall Reminders but have not called the facility to schedule an appointment.

# # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prior to Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before using Recall Reminder, sites will need to decide if they want to start immediately or pick a future date. Either way a start date must be chosen.

In the implementation of Recall Reminder, existing patient appointments for a clinic that will be using Recall Reminder must NOT be cancelled. Future appointments that have already been scheduled must be allowed to take place unless they are cancelled or rescheduled at the patient’s request. Clinic setups will need to be adjusted so no appointments can be scheduled more than 90 to 120 days into the future once the start date has been reached.

At the discretion of the provider, individual patients may be given appointments further into the future.

*<u>Choose to Begin Immediately</u>*

> *Advantages*

- Sites can immediately begin Recall Reminder on their start date.

> *Disadvantages*

- Extra work in setting up clinic area using Recall Reminder.
- New procedure can be confusing and sites should be prepared for it.

*<u>Choose to Begin at a Later Date</u>*

> *Advantages*

- More time and opportunity for patient and staff education.

> *Disadvantages*

- Can be confusing for staff to have existing appointments.

One very important word of advice – Choose a start date at least several months in the future and EDUCATE, ADVERTISE, and PUBLICIZE CHANGES to all staff and patients.

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the Recall Reminder software is SDRR.

## ## ## Obsolete Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recall Reminder software is a replacement for a Class III application called Clinic Recall which has a namespace of AXVC (older versions have a namespace of A687).

The following options (if your site has them) should be placed Out Of Order with a statement of “Replaced with Class I”. This should only be done once all conversions of the older Clinic Recall files have been successfully completed.

<u>AXVC Options</u>

Clinic Recall Menu Option \[AXVCLR CLINIC RECALL MENU\]

Print Clinic Recall Cards by Div \[AXVCLR RECALL PR CARD BY DIV\]

Print Clinic Recall Cards by Clinic \[AXVCLR RECALL PR CARD BY CLINIC\]

Print Clinic Recall Cards by Prov \[AXVCLR RECALL PRINT CARD\]

Print Clinic Recall Cards by Team \[AXVCLR RECALL PR CARD BY TM\]

Add/Edit Clinic Recall Patient \[AXVCLR RECALL CARD ADD\]

Edit/Add Clinic Recall Provider \[AXVCLR ADD RECALL PROVIDER\]

Edit/Add Recall Teams \[AXVCLR ADD RECALL TEAM\]

Inquire to Patient Recall \[AXVCLR RECALL CARD INQ\]

Recall List Print \[AXVCLR RECALL PRINT REPORT\]

<u>A687 Options</u>

Print Clinic Recall Cards \[A687 RECALL PRINT CARD\]

Add/Edit Clinic Recall Patient \[A687 RECALL CARD ADD\]

Edit/Add Clinic Recall Provider \[A687 ADD RECALL PROVIDER\]

Inquire to Patient Recall \[A687 RECALL CARD INQ\]

Recall List Print \[A687 RECALL PRINT REPORT\]

You may have these two additional options which will need to be placed out of order.

Clinic Recall Menu \[A687 CLINIC RECALL MENU\]

Print 2 Sided Clinic Recall Cards \[A687 RECALL PRINT CARD2\]

<u>Conversion Options</u>

The following options have been placed Out Of Order with SD\*5.3\*574 since all conversions of the Class III Outpatient Clinic Recall files should have been successfully completed.

Conversion Menu \[SDRR IRM MENU\]

Convert OUTPATIENT CLINIC RECALL PARAM

Convert OUTPATIENT CLINIC RECALL APPT TYPES

Convert OUTPATIENT CLINIC RECALL TEAM

Convert OUTPATIENT CLINIC RECALL PROVIDERS

Convert OUTPATIENT CLINIC RECALL

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several parameters associated with the Recall Reminder software that are site configurable. These parameters are to be set using options on the Manager menu for Recall Reminder \[SDRR MANAGER MENU\] which is locked with security key SDRR MANAGER.

The following is an example of the options used to set up Recall Reminder. For sites that have any version of Clinic Recall using the AXVC namespace, there are conversion options that will move the Class III file information into the national files. Please keep in mind if you are using an older version of Clinic Recall and have made local changes to those files, these changes will not be transferred over. Examples of the options used to convert the file entries are displayed later in this section.

1.  The conversion options have been placed Out of Order with SD\*5.3\*574, since all conversions of the Class III Outpatient Clinic Recall files should have been successfully completed.

The options used for the implementation of Recall Reminder are as follows.

Edit/Add Clinic Recall Provider \[SDRR ADD RECALL PROVIDER\]

Edit/Add Recall Teams \[SDRR ADD RECALL TEAM\]

Enter/Edit Appt Types \[SDRR APPT TYPE\]

Enter/Edit Clinic Letters \[SDRR CLINIC LETTER\]

Enter/Edit Clinic Recall Site Params \[SDRR RECALL REMINDER PARAMS\]

The options listed above should be performed in the following order.

1. Enter/Edit Clinic Recall Site Params \[SDRR RECALL REMINDER PARAMS\]

Select RECALL REMINDERS PARAMETERS DIVISION NAME: TEST LETTER

Are you adding 'TEST LETTER' as a new RECALL REMINDERS PARAMETERS (the 8TH)? No// Y (Yes)

DIVISION NAME: TEST LETTER//

\*\*Your Site can only select either CARDS or LETTERS\*\*

TYPE OF NOTIFICATION: LETTERS// ?

Choose from:

L LETTERS

C CARDS

TYPE OF NOTIFICATION: LETTERS//

AUTO PRINT DAYS:

(Enter the number of days prior to the recall date the notification cards/letters should be printed.)

CLEAN UP DAY SETTING:

(There is a tasked job that will check to see if a patient has made an appointment and, if so, will remove the patient from the Recall Reminders file (#403.5). This entry indicates the number of days before and after the requested appointment date the job will look at.)

> **NOTE:** Entry at the DIVISION prompt is not an entry from the Medical Center Division file (#40.8). The parameter settings allow sites to set up “divisions” or “groupings” for easier manageability of different areas of the facility.

2. Edit/Add Recall Teams \[SDRR ADD RECALL TEAM\]

Select Recall Reminder Team: PINKY TEAM

NAME: PINKY TEAM//

ACTIVE/INACTIVE: ACTIVE//

PRINTER ASSIGN: PRINTER1//

(Select the printer where notification cards/letters will be printed.)

CLINIC RECALL PARAM: TEST LETTER//

(Select the correct Recall Param division.)

3. Edit/Add Clinic Recall Provider \[SDRR ADD RECALL PROVIDER\]

Select RECALL REMINDERS PROVIDERS: TEST,ANOTHER TA IRM

Are you adding 'TEST,ANOTHER' as a new RECALL REMINDERS PROVIDERS (the 45TH)? No// Y (Yes)

RECALL REMINDERS PROVIDERS TEAM: PINKY TEAM

RECALL REMINDERS PROVIDERS STATUS: A ACTIVE

PROVIDER: TEST,ANOTHER//

TEAM: PINKY TEAM//

DIVISION:

(Select the Medical Center Division this provider is assigned to.)

DIRECT PHONE: XXX-XXX-XXXX

EXT.:

STATUS: ACTIVE//

KEY:

(May be used to control editing or canceling of Recall Reminders for this provider.)

4. Enter/Edit Appt Types \[SDRR APPT TYPE\]

Select RECALL REMINDERS APPT TYPE NAME: followup

NAME: FOLLOWUP//

SYNONYM: F//

(This is what displays on the CPRS cover sheet.)

5. Enter/Edit Clinic Letters \[SDRR CLINIC LETTER\]

Select RECALL REMINDERS LETTERS CLINIC: 1 TRI-CITIES AFTERCARE GROUP

Are you adding 'TRI-CITIES AFTERCARE GROUP' as a new RECALL REMINDERS LETTERS (the 2ND)? No// y (Yes)

CLINIC: TRI-CITIES AFTERCARE GROUP//

LETTER TEXT:

No existing text

Edit? NO//

## ## Conversion from Class III to Class I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been placed Out Of Order with SD\*5.3\*574 since all conversions of the Class III Outpatient Clinic Recall files should have been successfully completed.

Conversion Menu \[SDRR IRM MENU\]

Convert OUTPATIENT CLINIC RECALL PARAM

Convert OUTPATIENT CLINIC RECALL APPT TYPES

Convert OUTPATIENT CLINIC RECALL TEAM

Convert OUTPATIENT CLINIC RECALL PROVIDERS

Convert OUTPATIENT CLINIC RECALL

For any site using an older version of Clinic Recall with an AXVC namespace, options are available for converting Class III files to national Class I files.

The Conversion Menu \[SDRR IRM MENU\], containing the following options, can be used to move entries within Class III files to national Class I files. This menu is locked with the XUPROG security key.

These options must be performed in the order shown below. After each option is run, an e-mail will be sent to the programmer who ran the option giving information about how many entries were moved over. Once the e-mail has been read (and only after the e-mail has been read) run the next option.

1 Convert OUTPATIENT CLINIC RECALL PARAM \[SDRR CONVERSION PARAMS FILE\]

2 Convert OUTPATIENT CLINIC RECALL APPT TYPES \[SDRR CON RECALL APPT TYPES\]

3 Convert OUTPATIENT CLINIC RECALL TEAM \[SDRR CONVERSION TEAM FILE\]

4 Convert OUTPATIENT CLINIC RECALL PROVIDERS \[SDRR CONVERSION PROVIDER FILE\]

5 Convert OUTPATIENT CLINIC RECALL \[SDRR CONV OUTPATIENT RECALL\]

*Conversion E-mail Example 1*

Subj: SD\*5.3\*536 OUTPATIENT CLINIC TEAM FILE CONVERSION REPORT \[#8871853\] 03/11/08@07:52

22 lines

From: POSTMASTER In 'WASTE' basket. Page 1

-----------------------------------------------------------------------------

Patch: SD\*5.3\*536 RECALL REMINDER TEAM FILE CONVERSION PROCESSING

\*\*\*\*\*\*\*\*\*\*\*\*

The existing Class III file called OUPATIENT CLINIC RECALL TEAM (190004), which contains Clinic Recall Team Names have been converted to a new Class I file called Recall Reminder Team (403.55) which will provide the same functionality.

\*\*\*\*\*\*\*\*\*\*\*\*

SUMMARY OF PROCESSING RESULTS:

=================================

\<\<\< The Class III OUPATIENT CLINIC RECALL TEAM File Conversion has Completed. \>\>\>

DATE/TIME TASK STARTED: Mar 11, 2008 7:52:26 am

DATE/TIME TASK COMPLETED: Mar 11, 2008 7:52:26 am

TOTAL RECORDS CONVERTED: 17

\<END OF REPORT\>

*Conversion E-mail Example 2*

Subj: SD\*5.3\*536 OUTPATIENT CLINIC RECALL FILE CONVERSION REPORT \[#8871904\]

03/14/08@07:44 24 lines

From: POSTMASTER In 'WASTE' basket. Page 1

-----------------------------------------------------------------------------

Patch: SD\*5.3\*536 RECALL REMINDER FILE CONVERSION PROCESSING

\*\*\*\*\*\*\*\*\*\*\*\*

The existing Class III file called OUTPATIENT CLINIC RECALL (687065), which contains Clinic Recall ENTRIES have been converted to a new Class I file called Recall Reminder (403.5) which will provide the same functionality. If you have added any local site field to file 687065 they will not be moved over.

\*\*\*\*\*\*\*\*\*\*\*\*

SUMMARY OF PROCESSING RESULTS:

==============================

\<\<\< The Class III OUTPATIENT CLINIC RECALL PATIENT File Conversion has Completed. \>\>\>

DATE/TIME TASK STARTED: Mar 14, 2008 7:43:24 am

DATE/TIME TASK COMPLETED: Mar 14, 2008 7:44:24 am

DATE/TIME LAST RUN: Mar 11, 2008 11:20:48 am

TOTAL RECORDS CONVERTED: 10645

\<END OF REPORT\>

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>FILE \#</u> <u>FILE NAME</u> <u>GLOBAL</u>

403.5 RECALL REMINDERS ^SD(403.5

403.51 RECALL REMINDERS APPT TYPE ^SD(403.51

403.52 RECALL REMINDERS LETTERS ^SD(403.52

403.53 RECALL REMINDERS PARAMETERS ^SD(403.53

403.54 RECALL REMINDERS PROVIDERS ^SD(403.54

403.55 RECALL REMINDERS TEAM ^SD(403.55

403.56 RECALL REMINDERS REMOVED ^SD(403.56

## Template List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>FILE \#</u> <u>TEMPLATE NAME</u> <u>DESCRIPTION</u>

\#403.5 SDRREMARKS Allows for more comments when edit/delete Recall

\#403.5 SDRR RECALL CARD ADD Used to add Recall outside of Appointment Management

\#403.51 SDRR APPT TYPE Add/Edit Recall Appointment Types

\#403.52 SDRR ADD LETTERS Enter Recall Letters

\#403.53 SDRR PARAMS ENTER Add/Edit Recall Parameters

\#403.54 SDRR ADD PROVIDER Add/Edit Recall Provider

\#403.55 SDRR TEAM NAMES Add/Edit Recall Teams

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of the Recall Reminder routines with a brief description of each.

*SD\*5.3\*536*

SDRR1 SDRRCLR Event protocol

SDRR5 Remove and replace providers and clinics

SDRRC15 Post-Install for Patch SD\*5.3\*536 Convert Team File

SDRRC16 Env/Post-Install for Patch SD\*5.3\*536 Convert Params File

SDRRC17 Env/Post-Install for Patch SD\*5.3\*536 Convert Appt Types

SDRRC18 Env/Post-Install for Patch SD\*5.3\*536 Convert Providers

SDRRC20 Env/Post-Install for Patch SD\*5.3\*536 Convert Recall Patient File

SDRRCLR Reminder Recall clean-up

SDRRCLR2 Stand alone Recall enter/edit

SDRRCRR, SDRRCRR1, Clinic Recall list report

SDRRCRRP

SDRRDEL Delete/edit Recall Reminders

SDRRINQ, SDRRINQ1 Recall patient inquiry

SDRRISB Recall utility routine for printing

SDRRISRA Scheduled Recall Appointments

SDRRISRD Recall List Delinquencies

SDRRISRL Recall List w/Available Slots

SDRRISRU Recall Reminder Utilities

SDRRISRX Recall List Clerk Deletions

SDRRLRP Entry routine for manual printing of letters or cards

SDRROR Called within ORWCV routine

SDRRPXC Recall Reminder utilities

SDRRRECL Printing of letters manually

SDRRRECP Manual printing of cards

SDRRSEG3 Called within DGRPD for patient inquiry - (Activated with future patch)

SDRRSLC1 Manual printing of letters

SDRRSLCT Recall Reminder - Generic file entry selector

SDRRTSK, SDRRTSKI Nightly job for printing letters or cards

SDRRUTL, SDRRUTL1 Sort utility for printing of reports

*OR\*3.0\*302*

ORWCV Display of Recall Entries on CPRS Coversheet

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 26 new options exported with Recall Reminders V. 1.0.

NAME: SDRR ADD RECALL PROVIDER

MENU TEXT: Edit/Add Clinic Recall Provider

TYPE: edit

PACKAGE: SCHEDULING

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: This option will allow for enter/edit of Recall Reminder Providers.

EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=403.54

DIC {DIC}: SD(403.54, DIC(0): AEMQL

DIE: SD(403.54, DR {DIE}: \[SDRR ADD PROVIDER\]

UPPERCASE MENU TEXT: EDIT/ADD CLINIC RECALL PROVIDE

NAME: SDRR ADD RECALL TEAM

MENU TEXT: Edit/Add Recall Teams

TYPE: edit

PACKAGE: SCHEDULING

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: Will be used to add or edit team names for the Recall Reminder software.

EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=403.55

DIC {DIC}: SD(403.55, DIC(0): AEMQL

DIC(A): Select Recall Reminder Team:

DIE: SD(403.55, DR {DIE}: \[SDRR TEAM NAMES\]

UPPERCASE MENU TEXT: EDIT/ADD RECALL TEAMS

NAME: SDRR APPT TYPE

MENU TEXT: Enter/Edit Appt Types

TYPE: edit

PACKAGE: SCHEDULING

E ACTION PRESENT: YES

DESCRIPTION: Recall Appt types are used in viewing recall information on CPRS cover sheet. This information also shows during Recall Patient Inquiry and on reports. DELETION OF ENTRIES IS NOT ALLOWED.

ENTRY ACTION: S DLAYGO=403.51 DIC {DIC}: SD(403.51,

DIC(0): AEMQL DIE: SD(403.51,

DR {DIE}: \[SDRR APPT TYPE\]

UPPERCASE MENU TEXT: ENTER/EDIT APPT TYPES

NAME: SDRR CARD ADD

MENU TEXT: Add/Edit Clinic Recall Patient

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option allows users to enter or edit a patient into the Recall Reminder file without using Appointment Management.

ROUTINE: SDRRCLR2

UPPERCASE MENU TEXT: ADD/EDIT CLINIC RECALL PATIENT

NAME: SDRR CLEAN-UP

MENU TEXT: Clean Up Clinic Recall Entries

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option is a Recall Reminder option which should be queued to run after 10:00pm every night. It will check those patients in Recall Reminder against scheduled appointments and will delete a patient from Recall Reminder if the scheduled appointment date and clinic are within a number of days from the Recall Date. The Recall clinic must match the clinic that the patient has been scheduled for. If the clinic name is different, it will not delete the patient from the Recall Reminders file. The number of days is set within RECALL REMINDERS PARAMETERS.

ROUTINE: SDRRCLR

SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: CLEAN UP CLINIC RECALL ENTRIES

NAME: SDRR CLINIC LETTER

MENU TEXT: Enter/Edit Clinic Letters

TYPE: edit

PACKAGE: SCHEDULING

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: If you have setup a Clinic Recall entry with the Letter type as notification, you will need to enter the letter text using this option. You can refer to the clinic within the text or enter generic text format.

EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=403.52

DIC {DIC}: SD(403.52, DIC(0): AEMQL

DIE: SD(403.52, DR {DIE}: \[SDRR ADD LETTERS\]

UPPERCASE MENU TEXT: ENTER/EDIT CLINIC LETTERS

NAME: SDRR CONVERT ENTRIES

MENU TEXT: Convert Retired Providers/Clinic Recalls

TYPE: run routine

PACKAGE: SCHEDULING

LOCK: SDRR MANAGER

DESCRIPTION: This option will allow an approved user to convert Recall providers and clinics. If a provider leaves and there are Clinic Recalls already scheduled, you can convert these recalls to the new provider.

ROUTINE: SDRR5

UPPERCASE MENU TEXT: CONVERT RETIRED PROVIDERS/CLIN

NAME: SDRR DELETE RECALL

MENU TEXT: Delete/Cancel Clinic Recall Entry

TYPE: run routine

PACKAGE: SCHEDULING

E ACTION PRESENT: YES

DESCRIPTION: This option allows Recall Reminder entries to be cancelled or deleted.

ENTRY ACTION: S DIDEL=403.5

ROUTINE: SDRRDEL

DIC {DIC}: SD(403.5 DIC(0): AEMQ

UPPERCASE MENU TEXT: DELETE/CANCEL CLINIC RECALL EN

NAME: SDRR MANAGER MENU

MENU TEXT: Manager menu for Recall Reminder

TYPE: menu

PACKAGE: SCHEDULING

LOCK: SDRR MANAGER

DESCRIPTION: This menu will be locked with SDRR MANAGER key. This menu will house all options for setting up Recall Reminder.

ITEM: SDRR CONVERT ENTRIES SYNONYM: 1

DISPLAY ORDER: 1

ITEM: SDRR ADD RECALL TEAM SYNONYM: 3

DISPLAY ORDER: 3

ITEM: SDRR ADD RECALL PROVIDER SYNONYM: 5

DISPLAY ORDER: 5

ITEM: SDRR CLINIC LETTER SYNONYM: 6

DISPLAY ORDER: 6

ITEM: SDRR APPT TYPE SYNONYM: 4

DISPLAY ORDER: 4

ITEM: SDRR RECALL REMINDER PARAMS SYNONYM: 2

DISPLAY ORDER: 2

UPPERCASE MENU TEXT: MANAGER MENU FOR RECALL REMIND

NAME: SDRR PATIENT INQUIRY

MENU TEXT: Recall Patient Inquiry

TYPE: run routine

PACKAGE: SCHEDULING

E ACTION PRESENT: YES

DESCRIPTION: Allows for range or full patient inquiry.

ENTRY ACTION: K DIC

ROUTINE: EN^SDRRINQ

UPPERCASE MENU TEXT: RECALL PATIENT INQUIRY

NAME: SDRR PATIENT LIST

MENU TEXT: Recall List Print

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This menu allows users to print Recall Reminders by division, clinic, or Recall Reminder teams. It will ask for a date range and must be queued to a printer.

ROUTINE: SDRRCRR

UPPERCASE MENU TEXT: RECALL LIST PRINT

NAME: SDRR PRINT MENU

MENU TEXT: Clinic Recall Print Menu

TYPE: run routine

PACKAGE: SCHEDULING

LOCK: SDRR MANAGER

DESCRIPTION: This menu allows users to print either Recall Letters or Cards for patients who have been entered into the Recall Reminders file.

ROUTINE: SDRRLRP

UPPERCASE MENU TEXT: CLINIC RECALL PRINT MENU

NAME: SDRR RECALL APPOINTMENTS

MENU TEXT: Scheduled Recall Appointments

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option lists the patient appointments which caused patients to drop off the Recall List.

ROUTINE: EN^SDRRISRA

UPPERCASE MENU TEXT: SCHEDULED RECALL APPOINTMENTS

NAME: SDRR RECALL DELETIONS

MENU TEXT: Recall List Deletions

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option reports on the patients who were deleted from the Recall List by a clerk.

ROUTINE: EN^SDRRISRX

UPPERCASE MENU TEXT: RECALL LIST DELETIONS

NAME: SDRR RECALL DELINQUENCIES

MENU TEXT: Recall List Delinquencies

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option is essentially the same report as those produced by the two "Delinquent Recall" reports except it provides better control of clinic selection, and it reports on how many days delinquent each patient is. The user is asked for the recall date range, a set of clinics, and whether the report should break on clinic. It reports on patients who have been sent recall reminders, but haven't yet called to schedule an appointment.

ROUTINE: EN^SDRRISRD

UPPERCASE MENU TEXT: RECALL LIST DELINQUENCIES

NAME: SDRR RECALL LIST

MENU TEXT: Recall List w/Available Slots

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option is essentially the same report as that produced by the "Recall List Print" \[SDRR PATIENT LIST\] except it also reports on slot availability by month for each clinic. The user is asked for a date range, a set of clinics, and whether the report should page break on clinic. It reports on patients who are on the RECALL LIST.

ROUTINE: EN^SDRRISRL

UPPERCASE MENU TEXT: RECALL LIST W/AVAILABLE SLOTS

NAME: SDRR RECALL MAIN MENU

MENU TEXT: Recall Reminder Main Menu

TYPE: menu

PACKAGE: SCHEDULING

DESCRIPTION: Main menu for all Recall Reminder options. Some of the options are locked with SDRR MANAGER security key and should be assigned to the Recall Reminder coordinator.

ITEM: SDRR DELETE RECALL SYNONYM: 1

> DISPLAY ORDER: 1

ITEM: SDRR CARD ADD SYNONYM: 2

> DISPLAY ORDER: 2

ITEM: SDRR RECALL DELINQUENCIES SYNONYM: 3

> DISPLAY ORDER: 3

ITEM: SDRR RECALL DELETIONS SYNONYM: 4

> DISPLAY ORDER: 4

ITEM: SDRR RECALL APPOINTMENTS SYNONYM: 5

> DISPLAY ORDER: 5

ITEM: SDRR RECALL LIST SYNONYM: 6

> DISPLAY ORDER: 6

ITEM: SDRR PRINT MENU SYNONYM: 8

> DISPLAY ORDER: 8

ITEM: SDRR PATIENT INQUIRY SYNONYM: 9

> DISPLAY ORDER: 9

ITEM: SDRR MANAGER MENU SYNONYM: 10

> DISPLAY ORDER: 10

ITEM: SDRR PATIENT LIST SYNONYM: 7

> DISPLAY ORDER: 7

UPPERCASE MENU TEXT: RECALL REMINDER MAIN MENU

NAME: SDRR RECALL REMINDER PARAMS

MENU TEXT: Enter/Edit Clinic Recall Site Params

TYPE: edit

PACKAGE: SCHEDULING

E ACTION PRESENT: YES

X ACTION PRESENT: YES

DESCRIPTION: This option will allow a site to set up the Recall Reminder software.

EXIT ACTION: K DLAYGO

ENTRY ACTION: S DLAYGO=403.53

DIC {DIC}: SD(403.53, DIC(0): AEMQL

DIE: SD(403.53, DR {DIE}: \[SDRR PARAMS ENTER\]

UPPERCASE MENU TEXT: ENTER/EDIT CLINIC RECALL SITE

NAME: SDRR TASK JOB

MENU TEXT: Auto Print for Recall Reminder

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: This option should be queued to print every night. It does not need to be queued to a device.

ROUTINE: SDRRTSK

SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: AUTO PRINT FOR RECALL REMINDER

(When scheduling this job there is NO need to enter DEVICE FOR QUEUED JOB OUTPUT. This is determined by the printer name entered when setting up Recall Teams. ONLY printers that print 12 pitch should be selected for printing letters.)

NAME: SDRR TASK JOB CARD

MENU TEXT: Auto Print for Recall Reminder Cards

TYPE: run routine

DESCRIPTION: This option should be queued to print every night if your facility will be using Recall cards. It does not need to be queued to a device.

ROUTINE: SDRRTSK1

UPPERCASE MENU TEXT: AUTO PRINT FOR RECALL REMINDER

The following options have been placed Out Of Order with SD\*5.3\*574 since all conversions of the Class III Outpatient Clinic Recall files should have been successfully completed.

NAME: SDRR CON RECALL APPT TYPES

MENU TEXT: Convert OUTPATIENT CLINIC RECALL APPT TYPES

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: Convert OUTPATIENT CLINIC RECALL APPT TYPES to RECALL REMINDERS APPT TYPE.

ROUTINE: ENV^SDRRC17

UPPERCASE MENU TEXT: CONVERT OUTPATIENT CLINIC RECA

NAME: SDRR CONV OUTPATIENT RECALL

MENU TEXT: Convert OUTPATIENT CLINIC RECALL

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: Convert OUTPATIENT CLINIC RECALL to RECALL REMINDERS file.

ROUTINE: ENV^SDRRC20

UPPERCASE MENU TEXT: CONVERT OUTPATIENT CLINIC RECA

NAME: SDRR CONVERSION PARAMS FILE

MENU TEXT: Convert OUTPATIENT CLINIC RECALL PARAM

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: If there is an OUTPATIENT CLINIC RECALL PARAM file, will convert to RECALL REMINDERS PARAMETERS.

ROUTINE: ENV^SDRRC16

UPPERCASE MENU TEXT: CONVERT OUTPATIENT CLINIC RECA

NAME: SDRR CONVERSION PROVIDER FILE

MENU TEXT: Convert OUTPATIENT CLINIC RECALL PROVIDERS

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: Convert OUTPATIENT CLINIC RECALL PROVIDERS to RECALL REMINDERS PROVIDERS file.

ROUTINE: ENV^SDRRC18

UPPERCASE MENU TEXT: CONVERT OUTPATIENT CLINIC RECA

NAME: SDRR CONVERSION TEAM FILE

MENU TEXT: Convert OUTPATIENT CLINIC RECALL TEAM

TYPE: run routine

PACKAGE: SCHEDULING

DESCRIPTION: Convert OUTPATIENT CLINIC RECALL TEAM to RECALL REMINDERS TEAM.

ROUTINE: ENV^SDRRC15

UPPERCASE MENU TEXT: CONVERT OUTPATIENT CLINIC RECA

NAME: SDRR IRM MENU

MENU TEXT: Conversion Menu

TYPE: menu

LOCK: XUPROG

PACKAGE: SCHEDULING

DESCRIPTION: This menu has all items for converting older versions of Clinic Recall into the national version of Recall Reminder. Options should only be run once then put out of order.

ITEM: SDRR CONVERSION PARAMS FILE SYNONYM: 1

DISPLAY ORDER: 1

ITEM: SDRR CON RECALL APPT TYPES SYNONYM: 2

DISPLAY ORDER: 2

ITEM: SDRR CONVERSION TEAM FILE SYNONYM: 3

DISPLAY ORDER: 3

ITEM: SDRR CONVERSION PROVIDER FILE SYNONYM: 4

DISPLAY ORDER: 4

ITEM: SDRR CONV OUTPATIENT RECALL SYNONYM: 5

DISPLAY ORDER: 5

UPPERCASE MENU TEXT: CONVERSION MENU

## Exported Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one security key, SDRR MANAGER, exported with SD_5_3_P536. This key should be assigned to the Scheduling application coordinator. This key will lock SDRR MANAGER MENU and SDRR PRINT MENU.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*302 brings in the ability to view Recall Reminders within the appointment information on a patient’s cover sheet in CPRS. Patch OR\*3\*302 is part of the SD_5_3_P536 HFS file. Changes were made to routine ORWCV.

This software will function at both Medical Centers or Outpatient clinics and CBOCs. It works along with outpatient Appointment Manager.

This product is based on VistA Systems running the following versions of the software listed below.

1.  VA FileMan V. 22 or greater
2.  Kernel V. 8.0 or greater
3.  Kernel Toolkit V. 7.3 or greater
4.  Kernel RPC Broker V. 1.1 or greater
5.  PIMS (Patient Information Management System) V. 5.3 or greater (including):
    1.  Registration V. 5.3
    2.  Scheduling V. 5.3
6.  Order Entry V. 3.0 (CPRS (Computerized Patient Record System) V. 1.0  (GUI V. 27.77)) or greater

### Integration References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one Integration reference - Recall Reminder Change to ORWCV (#5195).

      5195     NAME: Recall Reminder Change to ORWCV

  CUSTODIAL PACKAGE: SCHEDULING                                

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING             

                        RECALL REMINDER MODULE

              USAGE: Private             ENTERED: MAY 7,2008

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                        TYPE: Routine

   These changes are required to show Recall Reminder information on the

  Cover sheet for all CPRS users. This is a view only NO input done. 

   

   ORWCV.INT VST+22          ;\*\*\*ADD CHANGES TO CALL COVER^SDRROR VST+23     

      D COVER^SDRROR DTLVST+14   I \$P(APPTINFO,";")="R" D RCDTL^SDRROR

   

   making two calls to SDRROR

   

   SDRR is a new namespace being used to move a Class III application

   (Clinic Recall) to a National Class I application called Reminder Recall

   (SDRR NAMESPACE). 

     ROUTINE: ORWCV

   COMPONENT:  SDRROR

   VARIABLES:  Used      BEG

   VARIABLES:  Used      END

   VARIABLES:  Used      DFN

           KEYWORDS: RECALL

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no internal relationships with this product.

# Callable Routines/Entry Points/Application Programmer Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDRROR Extracts data from RECALL REMINDERS (#403.5) file based on the criteria specified in the DFN input parameter. The data will be returned in a local array.

Input:

> DFN The internal entry number in the Patient file for the patient whose Recall Reminder data needs to be extracted.

# Mail Groups/Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDRR BAD ADDRESS

This mail group will receive messages for patients who have been scheduled in Recall Reminder but have a bad address flag set.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDRR EVENT Recall Reminder Action

This protocol will hang off the SDAM menu and is used for the RECALL REMINDER project. It will allow users to enter/edit information that has been stored in the RECALL REMINDERS file.

# Non-Applicable Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving functionality.

## Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no non-standard cross-references exported with SD_5_3_P536.KID.

## External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

External Interfaces is not applicable.

## Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no non-standard or global variables.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Glossary is not applicable.
