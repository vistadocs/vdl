---
title: SD*5.3*297 Unassigned Inactive Primary Care Physician Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Unassigned Inactive Primary Care Physician
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*297
group_key: "PCMM:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/001.png)
audience: 
keywords: 
  - pcmm
  - patient
  - provider
  - patients
  - care
  - primary
  - inactivation
  - team
  - position
  - date
page_count: 0
word_count: 4169
section_count: 12
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_p297_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_p297_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

Primary Care Management Module (PCMM)

Unassign Inactive Patient Primary Care Providers

RELEASE NOTES

Patch SD\*5.3\*297

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/001.png)

December 2006

TABLE OF CONTENTS

# I. Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [I. Introduction](#i-introduction)
- [II. Description of Functionality](#ii-description-of-functionality)
  - [GUI Changes](#gui-changes)
  - [Inactivation Messages](#inactivation-messages)
  - [Managing Inactivations](#managing-inactivations)
  - [PCMM Main Menu Option](#pcmm-main-menu-option)
  - [Team/Position Assignment/Re-Assignment Option](#teamposition-assignmentre-assignment-option)
  - [Patient Reactivation of an Automatically Inactivated Patient](#patient-reactivation-of-an-automatically-inactivated-patient)
- [III. Installation and Implementation](#iii-installation-and-implementation)
- [IV. Technical Information](#iv-technical-information)
  - [New Routine Summary](#new-routine-summary)
  - [Bulletins](#bulletins)
  - [Background Jobs](#background-jobs)
  - [Mail Groups](#mail-groups)
  - [Data Dictionary Modifications](#data-dictionary-modifications)
- [V. Acronyms and Definitions](#v-acronyms-and-definitions)
Patch SD\*5.3\*297 consists of new functionality and enhancements to a number of features in PCMM. It also addresses a significant number of NOIS or Remedy tickets, and puts mechanisms in place to enforce business rules in PCMM by inactivating patient/provider PCMM assignments determined to be invalid based on established business rules. This includes adherence to rules related to Person Class. These enhancements include associated changes to the graphical user interface (GUI).

# II. Description of Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three specific modifications, identified as critical, will be implemented in Patch SD\*5.3\*297, along with a significant number of feature enhancements, associated reports, and options.

The first modification will inactivate patients who have not seen their Primary Care provider(s) for specified lengths of time, from their Primary Care team and position/provider panels in PCMM. PCMM patients are assigned scheduled inactivation dates if their Primary Care team assignment has been established for 11 months and they have not been seen in those last 11 months by a provider assigned to the Primary Care Provider (PCP) or Associate Primary Care Provider (AP) positions assigned to the patient on their primary care team. After 30 days, these patients will be inactivated from their Team Position assignment if they still have not been seen. Similarly, PCMM patients that have been assigned to a Primary Care team for 12 months or longer and have not been seen within the last 23 months by a provider (assigned to the PCP or AP positions assigned to the patient on that team) will also be given scheduled inactivation dates. After 30 days, these patients will be inactivated from their Team & Position assignment if they still have not been seen. PCMM patients that have been identified for inactivation may have one 60-day extension on an individual basis. Reports will be available based on these new modifications. The inactivation timeframes may change if there have been changes to the provider assignment to the position during this period.

The second modification will provide for screening of staff that has been selected as a Primary Care Provider (PCP) or Associate Primary Care Provider (AP) to assure that only Physicians, Nurse Practitioners, Physician Assistants, and Residents/Interns (physicians) are designated as PCPs and APs in PCMM. Additionally, any current staff inappropriately identified in PCMM as a PCP or AP will be flagged and inactivated six months after installation of this patch. Reports and bulletins will communicate the flagging of these staff for potential inactivation. A separate report lists those staff members who were inactivated. Staff to be inactivated will receive a MailMan notification message regardless of settings on the message tab of the Primary Care Team Position Setup tab in the PCMM GUI.

The third enhancement will restrict the type of provider who may be selected as the PCP. Although the business rule states that only a Physician, a Nurse Practitioner, or Physician’s Assistant may be designated as a PCP, users have selected other provider types as PCP. It has become necessary to put limitations on who may be designated as PCPs. Restricting the provider type will improve data integrity and validity.

Other enhancements introduced by this patch include:

Functionality to schedule Providers, with a Person Class that is inconsistent with their PCMM Team position role, for inactivation 6 months after installation of SD\*5.3\*297. VistA text-based reports detail the automatic inactivation of patients and providers.

Mechanisms to assure that FTEE (Full Time Employee Equivalent) and Maximum Panel sizes are entered for each PCP and AP/PCP. FTEE and maximum Panel Size entries for APs and PCPs shall be required.

A new report called the “Direct PC FTEE and Panel Size Report” \[SC PCMM DIRECT PC FTEE\].

A mechanism to assure a total FTEE for each PC Provider does not exceed one (1.0) for both AP/PCPs and PCPs of Record. The FTEE cannot be greater than one for one institution or for all institutions with the first three digits of the institution number.

HL7 / Messaging enhancements:

- Enhancements introduced in order to meet new PCMM HL7 messaging requirements for the PCMM messages sent to the Austin Automation Center.
- Correct problem with date field.
- Prevent transmission of inactive provider data.
- Correct 608M error messages. A post installation routine will review existing PCMM 608M errors (Invalid Area of Specialization) and mark them for retransmission to the Austin Automation Center (AAC). These records will be corrected for erroneously sending inactive providers' information on the Provider Workload transmission prior to this patch.
- Add new fields to HL7 message for date a patient is flagged for inactivation, the date an extended inactivation is entered, the new date of inactivation for patients with an extended period before inactivation, and the actual date a patient is inactivated.
- Include a reason for the patient’s inactivation: inactive patient, death of patient, patient requested inactivation, or staff inactivated.
- Send date a provider is flagged for inactivation and date provider is inactivated by this patch, SD\*5.3\*297.
- Transmit AP/PCPs FTEE and “Maximum Allowed Panel size.”
- Transmit each patient’s Race and Ethnicity data to the Austin Automation Center (AAC) using the new Race/Ethnicity API to the Patient file and current PCMM Patient HL7 message. (DG\*5.3\*415, SD\*5.3\*254)

Entry and display of non-Primary Care teams and providers in VistA options is now available. Also, prevent removal of non-Primary Care wait list entries when a Primary Care team or provider is assigned to a patient on the wait list.

Addressing a significant number of NOIS and Remedy tickets

In addition, the ability to associate multiple Team Position Associated Clinics is included. The field has been changed to a multiple, and the post-init routine will populate this multiple with the current entry.

## GUI Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign Positions to a Team

Settings Tab

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/002.png)

Primary Care Team Position PCP

The position assignment of PCP is limited to Physicians, Nurse Practitioners (NP), and Physician’s Assistants (PA) only.

Additional instructions are displayed to assist in correctly setting the PCP, ACP, and Preceptor check boxes. The displayed instructions are based on the Role of the team position.

  
Primary Care Team Position PCP Associate

Only a Resident/Intern, NP, or PA shall be designated as an “Associate Provider” providing primary care.

Primary Care Team Position Preceptor

Only an attending Physician (MD or DO), NP or PA can be designated a Preceptor to Associate Primary Care Providers.

Patients for Position (text box)Allowed - The number of patients that should be assigned to this position. Users are not prevented from exceeding this number. <u>NOTE</u>: It is required that you enter a value in the “Patients for Position” field “Allowed” before you can save Resident/Intern, NP or PA as Primary Care Provider.

Actual - This is the number of patients that are currently assigned to this position. <u>NOTE</u>: If a provider other than an Attending, Resident/ Intern, PA or NP is selected, then both boxes A and B as well as “Allowed” under “Patients for Position” will not be selectable.

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/003.png)

User Class (lookup box)

This is the user class that must be used when selecting an individual to fill this position. <u>NOTE</u>: This field may be disabled at some sites.

  
Staff FTEE and Panel Size Entry Required for PCP/AP

New software enhancements assure that FTE (Full Time Equivalent) and Maximum Panel sizes are entered for each PCP and AP/PCP.

New software enhancements also assure a total FTE for each PC Provider does not exceed one (1.0) for both AP/PCPs and PCPs of Record. The FTE cannot be greater than one for one institution or for all institutions with the first three digits of the institution number.

STAFF/FTEE Window

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/004.png)

  
Associated Clinic TAB

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/005.png)

The application provides for entering and saving multiple Associated Clinics for Primary Care Providers and for Associate Primary Care Providers. If there is an existing clinic you wish to associate with this position, it should be entered here. The Associated Clinics will print on all PCMM reports with an associated clinic column or field.

Messages Tab Settings

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/006.png)

Notifications

The released PCMM patch and software will automatically select/check the “DO NOT SEND” option of the “Automatic Inactivations Notifications” line on the “Messages” tab for all active positions in PCMM at the time patch SD\*5.3\*297 is installed. \[Most providers do not want to receive these notifications per expert user feedback.\]

Selecting “TEAM,” POSITION,” or PRECEPTOR” on the “Automatic Inactivations Notifications” row of the “Messages” tab shall result in only designated staff receiving patient inactivation messages for only their patients and staff/provider inactivation messages for only their staff.

PCMM patch SD\*5.3\*297 does not overwrite or change users’ notification selections previously saved prior to the installation of this patch.

STAFF Assignment Display

![](sd-5-3-297-unassigned-inactive-primary-care-physician-release-notes/007.png)

Display Features: History and FTEE

When the user selects the “Staff/FTEE” icon on the “Primary Care Team Position Set Up” window in PCMM GUI after selecting a position, the system displays the currently active provider’s name highlighted in blue, the Effective date, Status Reason, and FTEE if there is one, as well as the history of assignments/unassignments.

Each time the FTEE is entered or edited, the value and the date of the entry or editing is now saved by the PCMM software, creating and maintaining a history of the FTEE for each provider.

Assignments - Staff, Positions, patients, and Team assignments now have a default date of the current date.

Inactivations - Staff, Positions, patients, and Team inactivations shall have a default date of T-1 (today minus one day.)

## Inactivation Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inactivation messages are addressed to the PCMM PATIENT/PROVIDER INACTIVATION mail group. PCMM Coordinators and others who will be monitoring inactivations should have membership in this group. Examples of the five new Bulletins are provided on the following pages:

Patients Scheduled for Inactivation from Primary Care Panel:

Subj: Patients Scheduled for Inactivation from Primary Care Panels \[#5404\]

12/20/05@09:43 33 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Patients scheduled for inactivation from their Primary Care team and

Primary Care Provider assignments appear below. Inactivation will

occur on the Scheduled Date for Inactivation date unless the patient

has a completed appointment encounter with their current Primary Care

Provider (PCP) or their Associate Primary Care Provider (AP) before

that date. The patient may be reactivated to their previous PCP and PC

team if they return for care.

VHA DIRECTIVE 2003-063, ACTIVE PATIENTS IN PCMM, establishes the rules for

PCMM automated inactivation of patients. The following is from that Directive.

Inactivation of primary care patients from a PCMM panel occurs under the

following circumstances:

\(2\) (a) The patient expires and

\(b\) Newly assigned patients (either newly-enrolled patients or patients who

have been re-assigned to a different provider) who have not been seen by

their PCP or Associate Provider (AP) and 12 months have passed since

the time of assignment to that provider. This provides every PCP a 1-year

grace period for seeing patients added to their panel (either newly-enrolled

patients or patients transferred from a different panel) before they are

inactivated. Patients must be seen by their PCP or AP within 12 months of

being assigned, or they need to be inactivated from the PCP's panel.

\(c\) Established patients that have been assigned to the PCP's panel for more

than 12 months, but have not been seen by their PCP or AP in the past 24 months

need to be inactivated.

\(3\) Patients appropriate for removal are to be identified and inactivated on

a regular basis.

With PCMM patch SD\*5.3\*297 installed, inactivations occur on the fifteenth

and the last day of the month.

Patients Scheduled for Inactivation from Primary Care panels

Date

Scheduled

Patient Name SSN Provider Team for Inactivation

------------------------------------------------------------------------------

INSTITUTION: ABCD VAMC

PATIENT, ONE 2222 PROVIDER, EIGHT BLUE TEAM 04/29/06

PATIENT, TWO 5555 PROVIDER, ELEVEN BLUE TEAM 04/29/06

Enter message action (in IN basket): Ignore//

  
Patients with Extended PCMM Inactivation Dates:

Subj: Patients With Extended PCMM Inactivation Dates \[#5405\] 12/20/05@09:43

39 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

By using the Extend Patients Inactivation Date option, these patients'

PCMM inactivation dates are now 60 days from their original inactivation date.

Inactivation will occur on the Date Scheduled for Inactivation unless the

patient has a completed appointment encounter with their current Primary

Care Provider (PCP) or their Associate Primary Care Provider (AP) before

that date.

VHA DIRECTIVE 2003-063, ACTIVE PATIENTS IN PCMM, establishes the rules for

PCMM automated inactivation of patients. The following is from that Directive.

Inactivation of primary care patients from a PCMM panel occurs under the

following circumstances:

\(2\) (a) The patient expires and

\(b\) Newly assigned patients (either newly-enrolled patients or patients who

have been re-assigned to a different provider) who have not been seen by

their PCP or Associate Provider (AP) and 12 months have passed since

the time of assignment to that provider. This provides every PCP a 1-year

grace period for seeing patients added to their panel (either newly-enrolled

patients or patients transferred from a different panel) before they are

inactivated. Patients must be seen by their PCP or AP within 12 months of

being assigned, or they need to be inactivated from the PCP's panel.

\(c\) Established patients that have been assigned to the PCP's panel for more

than 12 months, but have not been seen by their PCP or AP in the past 24 months

need to be inactivated.

\(3\) Patients appropriate for removal are to be identified and inactivated on

a regular basis.

With PCMM patch SD\*5.3\*297 installed, inactivations occur on the fifteenth

and the last day of the month.

Patients with Extended PCMM Inactivation Dates

Date

Scheduled for

Patient Name SSN Provider Team Inactivation

------------------------------------------------------------------------------

INSTITUTION: ABCD VAMC

PATIENT, FOUR 9999 PROVIDER, SEVEN BLUE TEAM 04/12/06

Enter message action (in IN basket): Ignore//

Patients Automated Inactivations from Primary Care Panels:

Subj: Patients Automated Inactivations from Primary Care Panels \[#5406\]

12/20/05@09:43 965 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Patients inactivated from their Primary Care team and Primary Care Provider

assignments appear below. The patient may be reactivated to their previous PCP

and PC team if they return for care.

VHA DIRECTIVE 2003-063, ACTIVE PATIENTS IN PCMM, establishes the rules for PCMM

automated inactivation of patients. The following is from that Directive.

Inactivation of primary care patients from a PCMM panel occurs under the

following circumstances:

\(2\) (a) The patient expires and

\(b\) Newly assigned patients (either newly-enrolled patients or patients who

have been re-assigned to a different provider) who have not been seen by

their PCP or Associate Provider (AP) and 12 months have passed since

the time of assignment to that provider. This provides every PCP a 1-year

grace period for seeing patients added to their panel (either newly-enrolled

patients or patients transferred from a different panel) before they are

inactivated. Patients must be seen by their PCP or AP within 12 months of

being assigned, or they need to be inactivated from the PCP's panel.

\(c\) Established patients that have been assigned to the PCP's panel for more

than 12 months, but have not been seen by their PCP or AP in the past 24 months

need to be inactivated.

\(3\) Patients appropriate for removal are to be identified and inactivated on

a regular basis.

With PCMM patch SD\*5.3\*297 installed, inactivations occur on the fifteenth

and the last day of the month.

Patients Automated Inactivations from Primary Care Panels

Date Reason

Patient Patient

Patient Name SSN Provider Team Inact Inact

-------------------------------------------------------------------------------

INSTITUTION: TEST VAMC

PATIENT,ONE 9736 PROVIDER,ONE TEST TEAM 08/08/05 NO APPT

PATIENT,NINETY 5894 PROVIDER,THIRTY TEST TEAM 05/17/04 DECEASED

Enter message action (in IN basket): Ignore//

Primary Care Providers Scheduled for Inactivation:Note: In the following example, patch SD\*5.3\*297 was installed on July 12, 2006.

When you run the report, the date your site installed patch SD\*5.3\*297 will be displayed.

Subj: Primary Care Providers Scheduled for Inactivation \[#5408\] 12/20/05@09:44

64 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

WARNING- The following primary care staff will be automatically

inactivated in PCMM software if a correct 'Person Class' and

'Provider Type' are not entered in the New Person File (#200) or

their role and position in the 'Position Setup' window is not

corrected to correspond with their 'Provider Type', 'Person

Class' and the Primary Care business rules stated below:

1\. Staff designated as Primary Care Providers (PCPs) in PCMM that

are not an Attending physician (Attending MD or Attending DO), NP

or PA, shall be inactivated from PCMM

2\. Staff designated as Associate Providers (APs) in PCMM, that are not

a Resident/Intern (Physician), NP or PA shall be inactivated in

PCMM

3\. All persons designated as an Associate Provider or Primary Care

Provider, who do not have the correct 'Provider Type' and 'Person

Class' entered in the New Person file (#200) in VistA, shall be

inactivated from their Primary Care positions in PCMM six months

after installation of patch SD\*5.3\*297 Date: JUL 12,2006.

4\. Please contact your PCMM Coordinator or Information Systems

to correct these problems

PRIMARY CARE PROVIDERS SCHEDULED FOR INACTIVATION

Provider's Assoc Team Person \# of Pts Sch Inac

Name Clinics Position Role Class Assigned Date

-------------------------------------------------------------------------------

INSTITUTION: TEST VAMC

PROVIDER,TWENTY INT AP INT INTERN (PHYSIC Allopathic and 2 01/31/06

PROVIDER,FIFTEEN INT AP ADM ADMIN COORDINA Allopathic and 0 01/31/06

PROVIDER,SEVENTEEN PHYS AS AD ADMIN COORDINA Physicians (M. 0 01/31/06

Enter message action (in IN basket): Ignore//

Primary Care Providers Inactivated:

Subj: Primary Care Providers Inactivated \[#5526\] 12/20/05@10:28 6 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PRIMARY CARE PROVIDERS INACTIVATED

Provider's Assoc Team Person \# of Pts Inac

Name Clinics Position Role Class Assigned Date

-------------------------------------------------------------------------------

Enter message action (in IN basket): Ignore//

## Managing Inactivations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inactivations are automatic, and are processed by the tasked job \[SCMC PCMM NIGHTLY TASK\] PCMM NIGHTLY TASK. Although the task runs each night, inactivations occur on the 15th and the last day of the month.

On demand reports for listing patient inactivations are available from the PATIENT REPORTS AND OPTIONS menu.

On demand reports for listing provider inactivations are available from the PROVIDER / POSITION REPORTS AND OPTIONS menu.

A patient’s inactivation may be extended once, for 60 days from the original inactivation date. If the patient does not complete an appointment encounter with their current Primary Care Provider (PCP) within the extension date, the inactivation occurs on the extended inactivation date. Extension of the patient inactivation date is available from the PATIENT REPORTS AND OPTIONS menu in VistA and from the PATIENT tab in the PCMM GUI.

## PCMM Main Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A number of new reports and options have been included in this patch. In addition, PCMM menus will be consolidated as a result of patch installation. A listing of menus and associated options are provided below:

PCMM Main Menu Option

PT PATIENT REPORTS AND OPTIONS ...

PR PROVIDER/POSITION REPORTS AND OPTIONS ...

TM TEAM REPORTS AND OPTIONS ...

HAR HISTORICAL ASSIGNMENT REPORTS ...

EWL EWL Wait List (Sch/PCMM) Menu ...

HL PCMM HL7 AND MAINTENANCE MENU ...

PT PATIENT REPORTS AND OPTIONS ...

AU Team/Position Assignment/Re-Assignment

DPA Detailed Patient Assignments

PAD Historical Patient Assignment Detail

PATA Patient Listing for Team Assignments

RE Patient Team Position Assignment Review

PTAL Historical Patient Position Assignment Listing

*SCHD Patients Scheduled for Inactivation from PC PanelsEXTD Patients with Extended Primary Care InactivationINAC Patients Automated Inactivations from PC Panels*

EXTP Extend Patient Inactivation Date

\* - Only users with the SC PCMM SETUP security key assigned to them will have access to the reports and option in *Italics*.

PR PROVIDER/POSITION REPORTS AND OPTIONS ...

EP PCMM Edit Practitioner in Position Assig. File

PD Practitioner Demographics

PP Practitioner's Patients

PRAL Historical Provider Position Assignment Listing

INCR PCMM Inconsistency Report

FTEE Direct PC FTEE and Panel Size Report

SSI Staff Sched for Inactivation

SI Staff Inactivated Report

TM TEAM REPORTS AND OPTIONS ...

ITP Individual Team Profile

TML Team Member Listing

TPL Team Patient Listing

SLT Summary Listing of Teams

TAS Historical Team Assignment Summary

HAR HISTORICAL ASSIGNMENT REPORTS ...

PAD Historical Patient Assignment Detail

PRAL Historical Provider Position Assignment Listing

PTAL Historical Patient Position Assignment Listing

TAS Historical Team Assignment Summary

EWL EWL Wait List (Sch/PCMM) Menu ...

1 Inquire Wait List (Sch/PCMM)

2 Enter/Edit Wait List (Sch/PCMM)

3 Disposition Wait List (Sch/PCMM) Entry

4 Wait List (Sch/PCMM) Reports ...

5 Wait List (Sch/PCMM) Parameter Enter/Edit

HL PCMM HL7 AND MAINTENANCE MENU ...

NT PCMM NIGHTLY TASK

AAC Retransmit one Patient or Provider

ECR PCMM Transmission Error Code Report

EP PCMM Transmission Error Processing

ER PCMM Transmission Error Report

## Team/Position Assignment/Re-Assignment Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VistA option determines a patient's Primary Care status. Based on status, it will prompt the user to select from the following choices:

- Assign patient to Primary Care (PC) or non-primary care team (if not currently assigned).
- Assign patient to PC or non-primary care Practitioner position (if assigned to a team, but not PC practitioner). User can perform a look-up by either position name or the current practitioner assigned to the position.
- Un-assign from team (if assigned to a PC or non-PC team). If patient is assigned to PC position, both the PC position and PC team will be unassigned.
- Un-assign from position
- While assigning/unassigning from a position: If the position has an Associated Clinic, the user will be prompted to enroll/discharge the patient from that Associated Clinic.

Limitations:

- Does not provide edit or delete functionality.
- Does not allow for re-assignment for patients with future PC assignments
- Requires that position has a practitioner currently assigned to it
- To overcome the above limitations, the PCMM GUI must be used.

## Patient Reactivation of an Automatically Inactivated Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Select Team Assignment Screen can be used to reactivate a patient who was automatically inactivated by the system.

- This functionality is accessed by clicking the Reactivate button
- The Reactivate button will be enabled if the patient had an automatic inactivation by the system.
- After clicking the Reactivate button a message box will appear showing the previously deactivated team and position and will confirm that you would like to reactivate the patient to the previous team and position
- Click Yes to confirm and reactivate the patient, which reactivates the original team and position assignment, keeping the original assigned date and removing the discharged date to reactivate the old assignment

# III. Installation and Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific information pertaining to the installation of this patch can be found in the patch description and section referred to as ‘INSTALLATION INSTRUCTIONS’ in patch SD\*5.3\*297.

# IV. Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCMCQK2

SCMCTSK1

SCMCTSK2

SCMCTSK3

SCMCTSK4

SCMCTSK5

SCMCTSK6

SCMCTSK7

SCMCTSK8

SCMCTSK9

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCMC PROVIDER INACTIVATION

## Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[SCMC PCMM NIGHTLY TASK\] PCMM NIGHTLY TASK

This option should be scheduled once a day. It reviews Patient team assignments and inactivates patients who have assignment dates greater than two years old and have not been seen in the last year.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM PATIENT/PROVIDER INACTIVATION

Group receives information on PCMM patient and provider inactivation. PCMM coordinators should be a member of this group.

## Data Dictionary Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PATIENT TEAM POSITION ASSIGNMENT (#404.43)

Added new fields

EXTEND AUTOMATIC INACTIVATION (#.13)

EXTENSION COMMENT (#.14)

DATE FLAGGED FOR INACTIVATION (#.15)

EXTENDED BY (#.16)

SCHEDULED INACTIVATION DATE (#.159)

DATE DISINACTIVATED (#.17)

STANDARD POSITION (#403.46) (This file comes with data)

ALLOWED TO BE PRIMARY CARE (#.03)

PERSON CLASS (#2) multiple

PCMM PARAMETER (#404.44)

SHORT INTERVAL EXPIRATION DATE (#18)

PC STAFF AUTO INACTIVATE DATE (#19)

TEAM AUTO INACTIVATE (#20)

POSITION ASSIGNMENT HISTORY (#404.52)

DATE FLAGGED FOR INACTIVATION (#.091)

INACTIVATED AUTOMATICALLY (#.11)

TEAM POSITION (#404.57)

AUTOMATIC INACTIVATION MESSAGE (#2.09)

PRECEPTOR INACTIVATION MESSAGE (#2.1)

ASSOCIATED CLINICS (#5) (multiple)

STAFF/POS INCONSISTENT REASON (#402)

# V. Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span class="smallcaps">Acronyms</span> | <span class="smallcaps">Definitions/Descriptions</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AAC                                     | Austin Automation Center -The central repository for National Care Patient Care Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| AP –Associate Provider                  | Associate Provider - is authorized to provide primary care, but cannot act as a Primary Care Provider. In PCMM, a Resident is designated as an Associate Provider. A Nurse Practitioner and/or Physician Assistant may be designated as an Associate Provider also. Every patient is to be assigned to a Primary Care Provider who coordinates the patient’s overall care. The Associate Provider on a Primary Care Team must be assigned to a Primary Care Provider.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CBOC                                    | Community Based Outpatient Clinic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CLERK                                   | Person who performs data entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CLINICAL SERVICE                        | A service defined at the Medical Center level, for example, Medicine, Surgery, Primary Care                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CONSULTS                                | When a patient is referred to a clinic on a one-time basis, he/she is not normally enrolled in that clinic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DATABASE                                | This refers to the information that is stored in your medical center’s computer program, e.g., patient information, service information, clinic information, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DSS                                     | Decision Support System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| FTEE                                    | Full Time Equivalent Employee                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| GUI                                     | Graphical User Interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| HL7                                     | Health Level 7 - ANSI standard for electronic data exchange in healthcare environments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PCMM Coordinator                        | The PCMM Coordinator is the staff member responsible for setup and maintenance of PCMM Teams, provider Positions, and patient assignments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MD- PHYSICIAN-PRIMARY CARE              | As a physician, incumbent's duties are to advise on, administer, supervise, or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. As a Primary Care practitioner, the incumbent provides the first point of assistance for a patient seeking care. Primary Care duties include: (1) Intake and initial needs assessment, (2) Health promotion and disease prevention, (3) Management of acute and chronic bio-psychosocial conditions, (4) Access to other components of health care, (5) Continuity, and (6) Patient and non-professional care giver education & training. (from IL 10-93-031, Under Secretary for Health's Letter) Can act as Primary Care Practitioner. |
| NPCD                                    | National Patient Care Database - is maintained in Austin and receives selected demographic and encounter-based clinical, diagnostic data form VA medical centers. This data enables a detailed analysis of VHA inpatient and outpatient health care activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| NP – Nurse Practitioner                 | Nurse Practitioner - Performs patient care duties in accordance with Scope of Practice under the supervision of a designated physician or physicians and Medical Center Policy. Duties include, but are not limited to, appropriate assessments, orders diagnostic tests and consultations as necessary, prescribes treatment interventions in accordance with established protocols, provides or arranges follow-up care, and provides health teaching and supportive counseling. Is authorized to act as a Primary Care Provider or Associate Provider. The ability to act as a Primary Care Provider is decided by individual facilities.                                                                                                                                                                                                                                                                   |
| PA – Physician Assistant                | Physician Assistant - Performs patient care duties in accordance with Scope of Practice under the supervision of a designated physician or physicians and Medical Center Policy. Duties include, but are not limited to, appropriate assessments, orders diagnostic tests and consultations as necessary, prescribes treatment interventions in accordance with established protocols, provides or arranges follow-up care, and provides health teaching and supportive counseling. Is authorized to act as a Primary Care Provider or Associate Provider. The ability to act as a Primary Care Provider is decided by individual facilities.                                                                                                                                                                                                                                                                  |
| PANEL                                   | A panel is a group of individual patients for which the Primary Care Provider has accepted primary care responsibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PATIENT SERVICES ASSISTANT              | Provides clerical and patient processing support to outpatient clinics, or other unit of a medical facility, in support of the care and treatment given to patients. This includes duties as receptionist, record-keeping duties, clerical duties related to patient care, and miscellaneous support to the medical staff of the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRIMARY CARE MANAGEMENT MODULE (PCMM)   | Primary Care Management Module - is the application for VA facilities to use for implementing primary care teams. Teams are created, positions associated with the teams are created, staff members are assigned to positions, and patients are assigned to the teams and positions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PCP                                     | Primary Care Provider - In PCMM, the Primary Care Provider is the position determined to be responsible for the coordination of the patient’s primary care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PERSON CLASS FILE                       | Consists of provider taxonomy developed by Health Care Finance Administration (HCFA). The taxonomy codifies provider type and provider area of specialization for all medical related providers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PHYSICIAN ASSISTANT                     | Performs patient care duties in accordance with Scope of Practice under the supervision of a designated physician or physicians and Medical Center Policy. Duties include, but are not limited to, diagnostic and therapeutic medical care and services, taking case histories, conducting physical examinations, and ordering lab and other studies. Physician Assistants also may carry out special procedures, such as giving injections or other medication, apply, or change dressings, or suturing minor lacerations. The ability to act as a Primary Care Practitioner is decided by individual facilities.                                                                                                                                                                                                                                                                                             |
| PHYSICIAN-PRIMARY CARE                  | As a physician, incumbent's duties are to advise on, administer, supervise, or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. As a Primary Care practitioner, the incumbent provides the first point of assistance for a patient seeking care. Primary Care duties include: (1) Intake and initial needs assessment, (2) Health promotion and disease prevention, (3) Management of acute and chronic biopsychosocial conditions, (4) Access to other components of health care, (5) Continuity, and (6) Patient and non-professional care giver education & training. (from IL 10-93-031, Under Secretary for Health's Letter) Can act as Primary Care Practitioner.  |
| PHYSICIAN-PSYCHIATRIST                  | As a physician, incumbent's duties are to advise on, administer, supervise, or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. The incumbent is also granted clinical privileges (by the appropriate governing Credentials committee) in regard to the practice of Psychiatry.                                                                                                                                                                                                                                                                                                                                                                                          |
| POSITION                                | Teams are comprised of one or more staff positions. Individual practitioners are assigned to a team position. A position is designated to serve certain roles in the overall primary care setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PRIMARY CARE                            | Primary care is the provision of integrated, accessible health care services by clinicians that are accountable for addressing a large majority of personal health care needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRIMARY CARE PROVIDER (PCP)             | In PCMM, the Primary Care Provider is the position determined to be responsible for the coordination of the patient’s primary care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RESIDENT (PHYSICIAN) INTERN             | Performs patient care duties in accordance with Medical Center Policy and is supervised by a Preceptor who can act as a Primary Care Practitioner. Duties include but may not be limited to completing history and physical examinations, obtaining blood and other specimens, and provision of patient medical care as permitted. The resident is an Associate Provider within a Primary Care Team. As a Resident, the incumbent is responsible for providing patient care as directed by the Preceptor. Cannot act as Primary Care Provider.                                                                                                                                                                                                                                                                                                                                                                 |
| ROLE                                    | A function or task of a staff member involved with the implementation, maintenance and continued success of primary care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TEAM                                    | Teams are groups of staff members organized for a certain purpose (e.g., Primary Care).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TEAM PROFILE                            | This is a screen within PCMM that shows the various characteristics of a particular team, e.g., number of patients allowed for enrollment, name, positions assigned, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VA                                      | Department of Veterans Affairs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VHA                                     | Veterans Health Administration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VistA                                   | Veterans Health Information Systems and Technology Architecture, formerly known as Decentralized Hospital Computer Program, encompass the complete information environment at VA medical facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |