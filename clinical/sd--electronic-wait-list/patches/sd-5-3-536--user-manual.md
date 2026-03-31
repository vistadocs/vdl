---
title: SD 5.3 536 Recall Reminder User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: 536 Recall Reminder
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*536
group_key: "SD:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: This option allows a user to enter or edit a patient into the Recall Reminders file (#403.5) without using Appointment Management.
audience: 
keywords: 
  - recall
  - clinic
  - reminder
  - patient
  - date
  - clinics
  - table
  - contents
  - appointment
  - print
page_count: 0
word_count: 5337
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_536_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_536_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

![](sd-5-3-536-recall-reminder-user-guide/001.png)

Recall Reminder User GuidePIMS V. 5.3 Scheduling ModulePatch SD\*5.3\*536Patch OR\*3.0\*302September 2009

Office of Information and Technology (OI&T)

Office of Enterprise Development (OED)

Revision History

Initiated on 9/1/09

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>9/1/09</td>
<td><p>Patch SD*5.3*536 and</p>
<p>Patch OR*3.0*302- Recall Reminder</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [# Recall Reminder Main Menu](#recall-reminder-main-menu)
  - [Overview](#overview)
  - [Delete/Cancel Clinic Recall Entry](#deletecancel-clinic-recall-entry)
  - [Add/Edit Clinic Recall Patient](#addedit-clinic-recall-patient)
  - [Recall List Delinquencies](#recall-list-delinquencies)
  - [Recall List Deletions](#recall-list-deletions)
  - [Scheduled Recall Appointments](#scheduled-recall-appointments)
  - [Recall List w/Available Slots](#recall-list-wavailable-slots)
  - [Recall List Print](#recall-list-print)
  - [Clinic Recall Print Menu](#clinic-recall-print-menu)
  - [Recall Patient Inquiry](#recall-patient-inquiry)
  - [Manager menu for Recall Reminder](#manager-menu-for-recall-reminder)
    - [Convert Retired Providers/Clinic Recalls](#convert-retired-providersclinic-recalls)
    - [Enter/Edit Clinic Recall Site Params](#enteredit-clinic-recall-site-params)
    - [Edit/Add Recall Teams](#editadd-recall-teams)
    - [Enter/Edit Appt Types](#enteredit-appt-types)
    - [Edit/Add Clinic Recall Provider](#editadd-clinic-recall-provider)
    - [Enter/Edit Clinic Letters](#enteredit-clinic-letters)
- [# Setting Up Recall Reminder](#setting-up-recall-reminder)
  - [Prior to Set Up](#prior-to-set-up)
  - [Set up](#set-up)
- [Setting up Cards](#setting-up-cards)
- [Recall Reminder Display on CPRS Coversheet](#recall-reminder-display-on-cprs-coversheet)
- [Recall Reminder Action in Appointment Management](#recall-reminder-action-in-appointment-management)
The Recall Reminder software is designed to allow facilities to implement recall scheduling. The software creates a ‘holding’ area for patients who will need to return to a clinic in the future. This time period has been determined to be a visit greater than 90 to 120 days in the future. At the discretion of the provider, individual patients may be scheduled further into the future. Patients are entered into the software for the date they are to return. Recall Reminder parameters are set by each site to determine the number of days prior to the recall date the notification cards or letters should be printed. The card or letter will instruct the patient to contact the VA to schedule an appointment which will not be made in the VistA Scheduling system until the patient contacts their facility.
It is recommended that sites give consideration to the best way to implement Recall Reminder at their site in that doing so takes a significant amount of time to train staff and educate veterans. Sites may choose to bring up different areas; for example, dental clinics, primary care, surgical clinics, etc., one at a time, moving on to the next area after successful implementation of the previous area.
This software was first intended for Primary Care use but now is being used in many clinical areas. Multiple Recall Reminder entries can be created for one patient. The software allows a user to enter/edit Recall Reminder by using either a standalone option or Appointment Management. Additionally, the software includes the ability to establish divisions (not to be confused with Medical Center Divisions) as well as teams to assist in greater manageability of the program.
The software also includes a number of reports to identify patients who haven’t scheduled their appointment as well as reports that will assist sites in the management of Recall Reminder.
The option Recall List Delinquencies \[SDRR RECALL DELINQUENCIES\] is a valuable tool that must be run on a regular basis to identify patients who have been sent Recall Reminders but have not called the facility to schedule an appointment.

# # Recall Reminder Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADD/EDIT CLINIC RECALL PATIENT \[SDRR CARD ADD\]

This option allows a user to enter or edit a patient into the Recall Reminders file (#403.5) without using Appointment Management.

CLINIC RECALL PRINT MENU \[SDRR PRINT MENU\]

This menu allows users to print either clinic recall letters or cards for patients who have been entered into the Recall Reminders file (#403.5).

DELETE/CANCEL CLINIC RECALL ENTRY \[SDRR DELETE RECALL\]

This option allows users to change the status of a clinic recall.

MANAGER MENU FOR RECALL REMINDER \[SDRR MANAGER MENU\]

This menu is locked with the SDRR MANAGER key. It contains all options for setting up Recall Reminder.

> CONVERT RETIRED PROVIDERS/CLINIC RECALLS \[SDRR CONVERT ENTRIES\]

> This option allows users to convert clinic recall providers and clinics to a new provider if a provider leaves and there are Recall Reminders already scheduled.

> ENTER/EDIT CLINIC RECALL SITE PARAMS \[SDRR RECALL REMINDER PARAMS\]

> This option allows a site to set up parameters when implementing the Recall Reminder software.

> EDIT/ADD RECALL TEAMS \[SDRR ADD RECALL TEAM\]

> This option is used to add or edit team names for the Recall Reminder program.

> ENTER/EDIT APPT TYPES \[SDRR APPT TYPE\]

> Appt Types are used in viewing recall information on the CPRS cover sheet. This information also shows in the Recall Patient Inquiry option and other reports.

> EDIT/ADD CLINIC RECALL PROVIDER \[SDRR ADD RECALL PROVIDER\]

> This option allows sites to enter or edit Recall Reminder providers.

> ENTER/EDIT CLINIC LETTERS \[SDRR CLINIC LETTER\]

> This option is used to enter the letters if Recall Reminder has been set up with the notification type as Letter.

RECALL LIST DELETIONS \[SDRR RECALL DELETIONS\]

This option reports on the patients who were deleted from the Recall List by a clerk.

RECALL LIST DELINQUENCIES \[SDRR RECALL DELINQUENCIES\]

This option provides a report on the number of days each patient is delinquent. The user is asked for the recall date range, a set of clinics, and whether the report should break on clinic. It includes patients who have been sent Recall Reminders but have not called to schedule an appointment.

RECALL LIST PRINT \[SDRR PATIENT LIST\]

This menu allows users to print clinic recalls by division, clinic, or outpatient clinic recall teams. It will ask for a date range and must be queued to printers.

RECALL LIST W/AVAILABLE SLOTS \[SDRR RECALL LIST\]

This option is essentially the same report as that produced by the Recall List Print except it also reports on slot availability by month for each clinic. The user is asked for a date range, a set of clinics, and whether the report should page break on clinic.

RECALL PATIENT INQUIRY \[SDRR PATIENT INQUIRY\]

This option allows users to select a date range or a full patient inquiry.

SCHEDULED RECALL APPOINTMENTS \[SDRR RECALL APPOINTMENTS\]

This option lists the patient appointments which caused patients to drop off the recall list.

## Delete/Cancel Clinic Recall Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows for canceling recall entries, giving a reason why the entry has been cancelled, and editing/adding comments.

The example shown below is for a patient that has one Recall Reminder entry. If a patient has more than one Recall Reminder entry, a selection list will be provided.

Example

Select Clinic Recall Patient: RECALLPATIENT, ONE

Are you sure you want to delete: OPTOMETRY CLINIC? NO// YES

Select one of the following:

1 Failure to respond

2 Moved

3 Deceased

4 Doesn't want VA services

5 Received care at another VA

6 Other

Reason for Removal: 2 Moved

COMMENT: Follow-up after surgery Replace ... With Patient no longer in our area.\<RET\>

Replace \<RET\>

Patient no longer in our area.

\*\*\* Now Deleting Patient Recall \*\*\*

## Add/Edit Clinic Recall Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

There are two different ways of entering a patient into Recall Reminder. The first is an action item on Appointment Management called “Recall Reminder Action”. The second is this standalone option which allows the users who do not have Appointment Management to have access to the Recall Reminder software.

If the patient has no recalls on file, the following statement will be displayed: No Clinic Recall on file. If the patient already has Recall Reminder entries, they will be listed.

If a recall provider has been set up with the KEY field populated and users have not been assigned this key, they will see the message below. They are able to view the recall date to see if the card or letter has been sent but will not have access to edit the information.

\*\*YOU DO NOT HAVE ACCESS TO THIS ENTRY\*\*

PLEASE CHECK WITH YOUR ADPAC OR IRM TO GET THE PROPER SECURITY KEY

The fields prompted for in this option are described below.

RECALL DATE - date the provider has requested the patient to return

RECALL DATE (PER PATIENT) - date the patient would like to return or be sent a notice to return

PROVIDER - Recall Reminder provider

CLINIC - clinic this patient should be scheduled in for their future appointment

LENGTH OF APPT. - if the provider requests the patient may need an appointment longer than the standard appointment – the number of minutes for this appointment

TEST/APP. - different appointment types that display on the CPRS cover sheet and other reports, for informational purposes, indicating the reason for the appointment

FAST/NON-FASTING - has the provider requested fasting or non fasting lab to be done prior to the next scheduled appointment at that clinic?

COMMENT - free text comments can be added when it comes time to schedule an appointment for the patient

Add/Edit Clinic Recall PatientExample

Select PATIENT NAME: RECALLPATIENT,ONE

No Clinic Recall on file

\*Must have Recall Date, approved Recall Clinic, Recall Provider and Type of Recall

Do you have this information? NO// y YES

PATIENT NAME: RECALLPATIENT,ONE// \<RET\>

RECALL DATE: t+5 (MAR 22, 2009)

RECALL DATE (PER PATIENT): \<RET\>

PROVIDER: RECALLPROVIDER,ONE OD RED TEAM ACTIVE

CLINIC: dermATOLOGY (LOC)

LENGTH OF APPT.: \<RET\>

TEST/APP.: follOWUP FUP

FAST/NON-FASTING: \<RET\>

COMMENT: \<RET\>

## Recall List Delinquencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is used to display recall entries which are delinquent. These are patients who have been sent either a card or letter but have not called the VA to schedule an appointment. This report must be run on a regular basis and a telephone call must be made to assure the patient’s appointment has been made.

When selecting a Range of Clinics, the user will select the ‘from’ clinic and the ‘thru’ clinic. All clinics within that range will be selected. Multiple ranges may be selected. All or specific clinics may be selected by choosing the Individual Clinics selection.

The report displays the patient name, last four of SSN, home phone, work phone, recall date, number of days since the recall date, and the date the notice was sent. An asterisk (\*) in front of the reminder sent date indicates the patient has been sent two notices and has not yet scheduled an appointment.

Example

Select a time period and a set of clinics, and I’ll tell you all the patients who are on the Recall List for that time period at those clinics who’ve been sent reminders, but haven’t yet made an appointment.

First select the Recall Date range.

Enter start date: t-365 (NOV 15, 2007)

Enter end date: (11/15/2007 - 11/14/2008): 11/13/2008// \<RET\> (NOV 13, 2008)

Select Medical Center Division: All// \<RET\>

Now you’ll select the clinics.

Select one of the following:

R Range of Clinics

I Individual Clinics

S Stop Codes

Select Clinics by: i Individual Clinics

You’ll be able to use ranges and wild cards to select clinics.

You’ll even be able to deselect clinics.

Enter “?” to see how.

Select Clinic: ALL// Allergy RECALLPROVIDER,ONE

Another one (Select/De-Select): Anesthesia

Another one (Select/De-Select): \<RET\>Recall List DelinquenciesExample, cont.

Page break on clinic? YES// \<RET\> YES

DEVICE: HOME// \<RET\>

Nov 14, 2008 Recall Delinquency List, 11/15/07-11/13/08 Page 1

Reminder

Patient SSN Home Phone Work Phone Recall Days Sent

--------------------- ALLERGY RECALLPROVIDER,ONE ------------------------------

RECALLPATIENT, ONE 0000 (000)000-0000 000-000-0000 05/06/08 192 \*05/06/08

RECALLPATIENT, TWO 0000 (666)666-6666 (333)444-4939 05/13/08 185 05/06/08

Delinquent Patient Recalls: 2

Nov 14, 2008 Recall Delinquency List, 11/15/07-11/13/08 Page 2

Reminder

Patient SSN Home Phone Work Phone Recall Days Sent

--------------------- ANESTHESIA (No Default Provider) -------------------------

RECALLPATIENT,TEN 5667 (555)000-0000 555-55-0000 05/06/08 192 \*05/06/08

Delinquent Patient Recalls: 1

## Recall List Deletions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This report provides a list of all patients who were deleted from Recall Reminder but have not made an appointment.

The default dates are determined by the entries in the Recall Reminders Removed file (#403.56). This file is built as patients are removed from Recall Reminder. If there are no entries in this file a message stating “No Entries Have Been Deleted” will be displayed.

When selecting a Range of Clinics, the user will select the ‘from’ clinic and the ‘thru’ clinic. All clinics within that range will be selected. Multiple ranges may be selected. All or specific clinics may be selected by choosing the Individual Clinics selection.

Example

Select a time period and a set of clinics, and I'll tell you all the patients who were on the Recall List, but were deleted from the list by clerks.

First select the Recall Date range. The default dates are determined by the

entries in Recall Reminders Removed File.

Enter start date: (2/2/2007 - 8/13/2009): 2/2/2007// \<RET\> (FEB 02, 2007)

Enter end date: (2/2/2007 - 8/13/2009): 8/13/2009// \<RET\> (AUG 13, 2009)

Select Medical Center Division: All/ \<RET\>

Now you'll select the clinics.

Select one of the following:

R Range of Clinics

I Individual Clinics

S Stop Codes

Select Clinics by: I Individual Clinics

You'll be able to use ranges and wild cards to select clinics.

You'll even be able to deselect clinics.

Enter '?' at the prompt to see how.

Select Clinic: All// dermatology RECALLPROVIDER,ONE

Another one (Select/De-Select: \<RET\>

Page break on clinic? Yes// \<RET\> YES

DEVICE: HOME// \<RET\>Recall List DeletionsExample, cont.

Nov 14, 2008 Recall List Clerk Deletions, 2/2/07-8/13/09 Page 1

Reminder

Patient SSN Sent Recall Deleted Deleted by Reason

------- --- -------- ------ ------- ---------- ------

--------------------- DERMATOLOGY RecallProvider,One ------------------------------------

RECALLPATIENT,ONE 0000 04/14/08 05/05/08 05/06/08 RECALLCLERK,One FTR

Patient Recall List Deletions: 1

## Scheduled Recall Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This output is used to display Recall Reminder entries which have been removed because the patient has contacted the VA to schedule an appointment.

The default dates are determined by the entries in the Recall Reminders Removed file (#403.56). This file is built as patients are removed from Recall Reminder. If there are no entries in this file a message stating “No Entries Have Been Scheduled” will be displayed.

When selecting a Range of Clinics, the user will select the ‘from’ clinic and the ‘thru’ clinic. All clinics within that range will be selected. Multiple ranges may be selected. All or specific clinics may be selected by choosing the Individual Clinics selection.

The “Days Diff” displayed in the output are the number of days between the Recall Date and the Appointment Date.

Example

Select a time period and a set of clinics, and I'll tell you all the

patients who were on the Recall List, but were deleted from the list

because they've made appointments.

First select the Recall Date range. The default dates are determined by the

entries in Recall Reminders Removed File.

Enter start date: (2/2/2007 - 8/13/2009): 2/2/2007// \<RET\> (FEB 02, 2007)

Enter end date: (2/2/2007 - 8/13/2009): 8/13/2009// \<RET\> (AUG 13, 2009)

Select Medical Center Division: All// \<RET\>

Now you'll select the clinics.

Select one of the following:

R Range of Clinics

I Individual Clinics

S Stop Codes

Select Clinics by: I Individual Clinics

You'll be able to use ranges and wild cards to select clinics.

You'll even be able to deselect clinics.

Enter '?' at the prompt to see how.

Select Clinic: All// neurology RECALLPROVIDER,TWO

Another one (Select/De-Select: \<RET\>Scheduled Recall AppointmentsExample, cont.

Page break on clinic? Yes// \<RET\> YES

DEVICE: HOME// \<RET\>

Nov 14, 2008 Scheduled Recall Appointments, 2/2/07-8/13/09 Page 1

Reminder Days Appt

Patient SSN Sent Recall Appt Diff Made Other Info

------- --- -------- ------ ---- ---- ---- ----------

-------------------- Neurology RECALLPROVIDER,TWO -----------------------------------

RECALLPATIENT,ONE 0000 04/29/08 06/11/08 06/18/08 7 06/11/08 EEG Required

Scheduled Recall Appointments: 1

## Recall List w/Available Slots

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option lists patients in Recall Reminder and includes the number of open clinic slots available, breaking the report into a monthly view.

When selecting a Range of Clinics, the user will select the ‘from’ clinic and the ‘thru’ clinic. All clinics within that range will be selected. Multiple ranges may be selected. All or specific clinics may be selected by choosing the Individual Clinics selection.

Example

Select a time period and a set of clinics, and I'll tell you all the

patients who are on the Recall List for that time period at those clinics.

For each month, I'll also tell you how many slots are available in each clinic.

First select the Recall Date range.

Enter start date: (11/1/2008 - 11/15/2009): 11/1/2008// \<RET\> (NOV 01, 2008)

Enter end date: (11/1/2008 - 11/15/2009): 1/31/2009// \<RET\> (JAN 31, 2009)

Select Medical Center Division: All// \<RET\>

Now you'll select the clinics.

Select one of the following:

R Range of Clinics

I Individual Clinics

S Stop Codes

Select Clinics by: i Individual Clinics

You'll be able to use ranges and wild cards to select clinics.

You'll even be able to deselect clinics.

Enter '?' at the prompt to see how.

Select Clinic: All// adult DAY HEALTH CARE

Another one (Select/De-Select): \<RET\>

Page break on clinic? Yes// \<RET\> YES

DEVICE: HOME// \<RET\>Recall List w/Available SlotsExample, cont.

Nov 14, 2008 Future Recall Slots, 11/1/08-1/31/09 Page 1

Reminder Recall

Recall Sent Patient SSN Home Phone Entered by

------ -------- ------- --- ---------- ----------

--------------------------- ADULT CAY CARE HEALTH (No Default Provider) ------------

11/07/08 10/15/08 RECALLPATIENT,ONE 0000 (000)000-0000 RECALLCLERK,ONE

11/30/08 10/15/08 RECALLPATIENT,TWO 0000 (666)666-6666 RECALLCLERK,ONE

Nov 2008 Patient Recalls: 2 , Available Slots: 76 (11/15/08 through EOM)

## Recall List Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is used to print clinic recalls by division, clinic, or outpatient clinic recall teams by a user-selected date range. All or specific teams may be selected by choosing the Selected Teams selection.

Example

Select one of the following:

1 All Clinics

2 Selected Clinics

3 Selected Team

Please select what type of Clinic Recall List you are looking for: 1 All Clinics

Start with Recall Date First: t (NOV 14, 2008)

Recall Date Lasted: t+10 (NOV 24, 2008)

Select division: ALL// \<RET\>

\*\*\*This report requires 132 columns

DEVICE: HOME// \<RET\>

OUTPATIENT CLINIC RECALL LIST

For date range: NOV 14, 2008 to NOV 14, 2008

Date printed: NOV 14, 2008 Page: 1

Provider Recall Date Date CS Patient 1U4N Phone Entered by

Comments

--------------------------------------------------------------------------------------

Clinic: AUDIOLOGY

Provider: RECALLPROVIDER,ONE

NOV 14, 2008 NotSent RECALLPATIENT,ONE R0000 (000)000-0000 RECALLCLERK,ONE

If you have lab, take this letter to lab with you.

Daily Sub-Total for AUDIOLOGY - (1)

## Clinic Recall Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The option allows for reprinting Recall Reminder letters or cards and should only be used by the Recall Reminder Coordinator or specifically designated individual. There is a nightly job that will print the site’s cards or letters and when a card or letter is printed Recall Reminder keeps track of the date printed. This option is locked with the SDRR MANAGER security key.

It is recommended selection number 5 (Print Letters for Nonresponsive Patients) and/or 6 (Print Cards for Nonresponsive Patients) of this option be run twice a week. This option will identify patients who have not responded to their recall letter/card and will generate a second notification to be mailed to the patient.

Example

<u>Example 1</u> - Selecting a Recall Division set up to print Letters

What Clinic Recall Division will you be printing From: Test Letter

Select one of the following:

1 Print Letters by Clinic

2 Print Letters by Provider

3 Print Letters by Team

4 Print a Letter by Patient

5 Print Letters for Nonresponsive Patients

Please select what you are looking for:

Additional prompts vary, dependent on selection made above.

<u>Example 2</u> - Selecting a Recall Division set up to print Cards

What Clinic Recall Division will you be printing From: TESTING CARD

Select one of the following:

1 Print Cards by Division

2 Print Cards by Clinic

3 Print Cards by Provider

4 Print Cards by Team

5 Print a Card by Patient

6 Print Cards for Nonresponsive Patients

Please select what you are looking for:

Additional prompts vary, dependent on selection made above.

## Recall Patient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows sites to either view or print all Recall Reminders or a date range of entries for a patient.

Example

Select PATIENT NAME: RECALLPATIENT,ONE

Select one of the following:

R Range

A All

Do you want a (R)ange or (A)ll: All// \<RET\>

Do you want to print the profile? NO// \<RET\> (will only show on your screen)

DEVICE: HOME// A200 Right Margin: 80// \<RET\>

Patient Name: RECALLPATIENT,ONE Date of Birth: MAR 31,1942 Last4: 0000

ACTIVE RECALL REMINDERS

Clinic: TRI-CITIES NUTRITION/GROUP Recall Date: MAR 14, 2009

Provider: RECALLPROVIDER,ONE Appt/Type: FOLLOWUP

Fasting/NonFasting: YES

Appt Requested Length: 60 Date Reminder Sent: NOV 14, 2008

User who Entered: RECALLCLERK,ONE Patient Requested Dt: MAR 09, 2009

Date Second Reminder Sent:

Comments: TEST

Patient Name: RECALLPATIENT,ONE Date of Birth: MAR 31,1942 Last4: 0000

INACTIVE RECALL REMINDERS

Clinic: TRI-CITIES AFTERCARE GROUP Recall Date: MAY 05, 2008

Provider: RECALLPROVIDER,ONE Appt/Type: FOLLOWUP

Fasting/NonFasting:

Appt Requested Length: 60 Date Reminder Sent: NOTSENT

User who Entered: RECALLCLERK,ONE Patient Requested Dt:

Date Removed from Active File: MAY 06, 2008@08:40

Reason for Removal: FTR

User who Deleted Entry: RECALLCLERK,ONE

Comments: JUST TESTING

## Manager menu for Recall Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Convert Retired Providers/Clinic Recalls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

This option allows the Recall Reminder Coordinator, or others who hold the SDRR MANAGER security key, to convert provider or provider and clinic names associated with a recall entry. This may be used if a provider has an extended absence.

Providers may be assigned to multiple recall teams, so when a provider is selected, select the correct provider and team.

If the clinic name that the retiring provider has recalls assigned to is known, answer yes at the *Do you want to change Clinic names that the recall is pointed to* prompt if you would like to also change the Recall clinic.

Example

Select Retiring Provider: RECALLPROVIDER,ONE DW I

Select New Provider: RECALLPROVIDER,TWO

Do you want to change Clinic names that the recall is pointed to:? No// \<RET\>

Start with RECALL DATE: T (NOV 17, 2008)

End with RECALL DATE: T+365 (NOV 17, 2009)

\*\*\*\*You will be converting all Clinic Recalls for\*\*\*\*

RECALLPROVIDER,ONE -They will be converted to- RECALLPROVIDER,TWO

Manager menu for Recall Reminder

### Enter/Edit Clinic Recall Site Params

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

This is the primary option which determines how sites will be using Recall Reminder. When implementing Recall Reminder, parameters must be set up first. Sites will be prompted for the type of notification to be sent out to the patients, how many days ahead of the recall date notifications will be sent out, and how many days the system needs to look at to verify that a recall appointment has become a scheduled visit.

Clarification should be made that entry at the *Division Name* prompt is not an entry from the Medical Center Division file (#40.8). The parameter settings allow sites to set up “divisions” or “groupings” for easier manageability of different areas of a facility.

> **NOTE:** Entries should not be deleted.

Example

Select RECALL REMINDERS PARAMETERS DIVISION NAME: North Bend Letters

Are you adding 'NORTH BEND LETTERS' as

a new RECALL REMINDERS PARAMETERS (the 15TH)? No// YES

DIVISION NAME: NORTH BEND LETTERS// \<RET\>

\*\*Your Site can only select either CARDS or LETTERS\*\*

TYPE OF NOTIFICATION: ?

How should notification be sent?

Choose from:

L LETTERS

C CARDS

TYPE OF NOTIFICATION: L LETTERS

AUTO PRINT DAYS: ??

Please put in the number of days ahead of the Recall Reminder date that you would like to send out Notification.

AUTO PRINT DAYS: 14

CLEAN UP DAY SETTING: ??

A background job runs nightly to delete recall reminders from the RECALL REMINDERS file if an appointment has been scheduled for the patient at the requested clinic. The background job scans the scheduled appointments, and if an appointment has been scheduled within the CLEAN UP DAY SETTING number of days (before or after) of the requested appointment date, then the appointment is considered to have fulfilled the recall reminder request, and the recall reminder is deleted. A copy of the recall reminder record is added to the RECALL REMINDERS REMOVED file, and the DELETE REASON is set to APPT SCHEDULED.

CLEAN UP DAY SETTING: 45Manager menu for Recall Reminder

### Edit/Add Recall Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

This option allows a site to create recall teams. When implementing Recall Reminder, this step must be completed second. This is used for both assigning a printer location for a group of clinics and for some reports that print by team.

> **NOTE:** Entries should not be deleted.

Example

Select Recall Reminder Team: GREAT NORTH WEST

Are you adding 'GREAT NORTH WEST' as

a new RECALL REMINDERS TEAM (the 20TH)? No// YES

NAME: GREAT NORTH WEST// \<RET\>

ACTIVE/INACTIVE: A ACTIVE

PRINTER ASSIGN: PRT YELLOW

CLINIC RECALL PARAM: NORTH BEND LETTERSManager menu for Recall Reminder

### Enter/Edit Appt Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

Recall Appt types are used in viewing recall information on the CPRS cover sheet. The Recall Reminder Appt Type Synonym displays on the CPRS cover sheet.

When implementing Recall Reminder, this option must be done third. This information also shows in Recall Patient Inquiry and on other reports.

> **NOTE:** Entries should not be deleted.

Example

Select RECALL REMINDERS APPT TYPE NAME: 12 MONTHS

Are you adding '12 MONTHS' as

a new RECALL REMINDERS APPT TYPE (the 19TH)? No// Y (Yes)

RECALL REMINDERS APPT TYPE SYNONYM: 12M

NAME: 12 MONTHS// \<RET\>

SYNONYM: 12M// \<RET\>Manager menu for Recall Reminder

### Edit/Add Clinic Recall Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

This option is used to enter recall provider settings that will assist in using Recall Reminder. When implementing Recall Reminder, this option must be done fourth. This is a “pointer” to the New Person file (#200), but has other fields that help group the printing of recall reports and set local locks so some provider entries can only be viewed but not edited or cancelled.

At the *Division* prompt, enter the medical center division the provider is assigned to.

> **NOTE:** Entries should not be deleted.

Example

Select RECALL REMINDERS PROVIDERS: RECALLPROVIDER,TWO

Are you adding ‘RECALLPROVIDER,TWO' as

a new RECALL REMINDERS PROVIDERS (the 48TH)? No// Y (Yes)

RECALL REMINDERS PROVIDERS TEAM: GREAT NORTH WEST

RECALL REMINDERS PROVIDERS STATUS: A ACTIVE

PROVIDER: RECALLPROVIDER,TWO// \<RET\>

TEAM: GREAT NORTH WEST// \<RET\>

DIVISION: SPRINGFIELD

DIRECT PHONE: 111-111-0000

EXT.:11111

STATUS: ACTIVE// \<RET\>

KEY: ??

If this field is blank, then any clerk may view and enter/edit Recall Reminders for this provider. If this field contains a security key, then any clerk may view the recall reminders for this provider, but only clerks holding the security key may enter/edit them.

To add the provider to additional teams, quotation marks should be placed around the provider’s name, as shown below.

Select RECALL REMINDERS PROVIDERS: “RECALLPROVIDER,TWO”

Are you adding ‘RECALLPROVIDER,TWO' as

a new RECALL REMINDERS PROVIDERS (the 49TH)? No// Y (Yes)

Manager menu for Recall Reminder

### Enter/Edit Clinic Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Manager menu for Recall Reminder is locked with the SDRR MANAGER security key.

If Recall Reminder has been set up with the notification type of letter, letters must be entered using this option. The clinic may be referred to with this text or generic text format may be entered. Below is an example of text that may be entered.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Just a reminder, it's time to schedule your next follow-up appointment with your Primary Care provider.

Please call the following number MONDAY through FRIDAY between the hours of 8:30AM - 4:00 PM to schedule an appointment:

TOLL FREE: 1-800-000-0000 Ext. \*0000 or direct dial 1-800-666-6666 (For our deaf veteran population ONLY: There is a TTY phone available Toll Free

1-800-666-6666 ext. \*0000 or direct dial 1-800-666-6666)

Fill in the information below and keep as your reminder. Please have any lab work completed prior to appointment. If you have diabetes, bring your glucometer. If you have hypertension, bring your blood pressure readings.

APPOINTMENT DATE\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ TIME \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Thank you

VA Health Care System Primary Care Clinic

This generic text can be entered for all clinics using Recall Reminder or sites can set up letters for each clinic with proper clinic contact numbers if they are not using centralized scheduling.

Example

Select RECALL REMINDERS LETTERS CLINIC: OPTOMETRY…OK? Yes// \<RET\> (Yes)

CLINIC: OPTOMETRY// \<RET\>

LETTER TEXT:

This letter is to remind you to call for an optometry appointment at your earliest convenience.

Thank you.

VA Health Care System Eye Clinic

Edit? NO// \<RET\>

# # Setting Up Recall Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prior to Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before using Recall Reminder, sites will need to decide if they want to start immediately or pick a future date. Either way a start date must be chosen.

In the implementation of Recall Reminder, existing patient appointments for a clinic that will be using Recall Reminder must NOT be cancelled. Future appointments that have already been scheduled must be allowed to take place unless they are cancelled or rescheduled at the patient’s request. Clinic setups will need to be adjusted so no appointments can be scheduled more than 90 to 120 days into the future once the start date has been reached.

> **NOTE:** At the discretion of the provider, individual patients may be given appointments further into the future.

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

## Set up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below are the options and the order in which they should be used to implement Recall Reminder.

1.  Enter/Edit Clinic Recall Site Params \[SDRR RECALL REMINDER PARAMS\]

> Sites must establish their divisions, types of notifications, and other parameter settings needed to implement Recall Reminder.

2.  Edit/Add Recall Teams \[SDRR ADD RECALL TEAM\]

> This option will be used to set up teams, assign printers to the teams, and assign the team to the appropriate division.

3.  Edit/Add Clinic Recall Provider \[SDRR ADD RECALL PROVIDER\]

> Providers will be entered using this option, including assignment to teams and Medical Center Divisions. Phone numbers for providers may also be entered. If a decision is made to “lock” the provider, limiting editing or cancelling reminders assigned to the provider, a key established by the site will be entered using this option.

4.  Enter/Edit Appt Types \[SDRR APPT TYPE\]

> Appointment types which will appear on the CPRS cover sheet and other Recall Reminder reports are created with this option. These appointment types may be used to alert users as to what the appointment is for, i.e., 6 month follow-up, EKG, labs, etc.

5.  Enter/Edit Clinic Letters \[SDRR CLINIC LETTER\]

> This option is used to develop the letters assigned to clinics which will be printed and sent to veterans, reminding them to call and schedule their appointment.

# Setting up Cards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The postcards are 4x6, govt. FL22 preprinted with return address. One side of the postcard has the return address of the VA. The patient address information will be printed on this side by using Recall Reminder print options. Your facility will be responsible for replication of the information which is displayed on the back of the card.

The other side has information about calling in for the appointment. There is not to be any sensitive patient information included on this card. The wording on the back of the cards can be preprinted by an outside vendor or a site print shop. Below are examples of the wording and may be changed at each facility if desired. When using the cards, the only items that will print on the front of the cards is the patient's address information, FL if there is a fast lab, NFL if there are non-fasting labs, and \*\*## if the appointment is greater than 30 minutes. The print options will only print the front of the cards.

“\*\*\*Clinic names that reference medical specialties such as GU, Mental Health, Dermatology, etc., or diagnoses must not be included on a postcard.\*\*\*”

If your facility chooses to use cards, below are examples of information which can be preprinted on the back of the FL22.

BACK OF CARD

Example 1

Please Call one of the following

numbers to arrange an appointment that will be

convenient for you during the next month.

Example 2

It's that time again!

Please call (xxx) xxx-xxxx

Or toll free 1-800-xxx-xxxx ext. xxxx

Any weekday (9:00am-3:00pm) to schedule an appointment.

Date/time\_\_\_\_\_\_\_\_\_\_\_\_\_

# Recall Reminder Display on CPRS Coversheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the Recall Reminder display on the CPRS coversheet.

![](sd-5-3-536-recall-reminder-user-guide/002.png)

# Recall Reminder Action in Appointment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new action has been added to Appointment Management which allows those users who have Appointment Management to access Recall Reminder and add or edit recall entries.

![](sd-5-3-536-recall-reminder-user-guide/003.png)