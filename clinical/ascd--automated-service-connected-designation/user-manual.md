---
consolidated_title: "ascd user manual"
app_code: ASCD
doc_type: UM
master_source: "ASCD User Manual (PCE)"
master_pub_date: September 2007
consolidated_from: 2 versions
prior_versions:
  - "ASCD User Manual (Scheduling)"
---

---
title: |

  ![](ascd-user-manual-pce/001.png)

  Patient Care Encounter (PCE) V. 1.0 User Manual
---

August 1996Patch PX\*1.0\*184(Revised September 2007)

Health Program Support Office (HPSO)

Revision History

Initiated on 11/19/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 25%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Description (Patch # if applicable)</td>
<td>Project Manager</td>
<td>Technical Writer</td>
</tr>
<tr class="even">
<td>11/19/2004</td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data</td>
<td></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>03/17/2005</td>
<td><p>Manual updated to show changes with Patch PX*1*380</p>
<p>See section:</p>
<blockquote>
<p>Glossary – Clinic</p>
<p>Conforming Clinics</p>
<p>Non- Conforming Clinics</p>
</blockquote></td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>08/10/2005</td>
<td>Manual updated to show changes with patch PX*1*153: added option PCE Delete Encounters W/O Visit</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>9/05/2005</td>
<td>Manual updated to show changes with patch PX*1*124</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>7/10/2007</td>
<td>Manual updated to include clarification of PCE Encounter Data Entry- Supervisor role-PX*1*183</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>9/20/2007</td>
<td>Manual updated to show changes with patch PX*1.0*184 - Automated Service Connected Designation (ASCD)</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose and Benefits of PCE](#purpose-and-benefits-of-pce)
  - [Designing Encounter Forms](#designing-encounter-forms)
- [PX\1.0\184 – Automated Service Connected Designation (ASCD)](#px10184-automated-service-connected-designation-ascd)
- [Orientation](#orientation)
  - [Screen Display](#screen-display)
  - [Review Screens](#review-screens)
- [# Using PCE](#using-pce)
  - [PCE Data Entry Options](#pce-data-entry-options)
    - [### ### PCE Actions](#pce-actions)
    - [Adding and Editing Patient Care Encounters](#adding-and-editing-patient-care-encounters)
    - [Follow the steps in the next few pages to add, delete, or edit encounters.](#follow-the-steps-in-the-next-few-pages-to-add-delete-or-edit-encounters)
    - [Make Historical Encounter](#make-historical-encounter)
    - [Update Encounter](#update-encounter)
    - [How to Add or Edit the Checkout Interview](#how-to-add-or-edit-the-checkout-interview)
    - [Adding or Editing Directions to Patient's Home](#adding-or-editing-directions-to-patients-home)
- [PCE and Health Summary](#pce-and-health-summary)
- [Managing PCE](#managing-pce)
  - [PCE Menus and Options](#pce-menus-and-options)
    - [PCE IRM Main Menu](#pce-irm-main-menu)
    - [PCE Coordinator Menu](#pce-coordinator-menu)
    - [### ### ### Key Concepts](#key-concepts)
  - [PCE Site Parameters](#pce-site-parameters)
  - [PCE HS/RPT Parameter Menu](#pce-hsrpt-parameter-menu)
  - [PCE Site Parameters Edit Example](#pce-site-parameters-edit-example)
  - [## Table Maintenance](#table-maintenance)
    - [Editing the Education Topic file](#editing-the-education-topic-file)
  - [PCE Information Only](#pce-information-only)
  - [clinical reminders](#clinical-reminders)
  - [PCE Clinical Reports](#pce-clinical-reports)
    - [PCE Clinical Reports Menu](#pce-clinical-reports-menu)
  - [Select PCE Clinical Reports Option: LE Location Encounter Counts](#select-pce-clinical-reports-option-le-location-encounter-counts)
    - [Missing Data Report](#missing-data-report)
- [# Supplementary Material](#supplementary-material)
  - [Frequently Asked Questions](#frequently-asked-questions)
  - [Device Interface Error Reports](#device-interface-error-reports)
- [# Glossary](#glossary)
- [INDEX](#index)
- [Appendix A - Sample MDR Report](#appendix-a-sample-mdr-report)
Patient Care Encounter (PCE) helps sites collect, manage, and display outpatient encounter data (including providers, procedure codes, and diagnostic codes) in compliance with the 10/1/96 Ambulatory Care Data Capture mandate from the Undersecretary of Health.
PCE also helps sites document patient education, examinations, treatments, skin tests, and immunizations, as well as collect and manage other clinically significant data, such as defining Health Factors and Health Maintenance Reminders.
PCE data may come from several sources, including external data acquisition devices (such as mark sense scanners), provider interaction (through workstations or portable computers), or clerical data entry. PCE allows new types of data (such as immunizations and purpose of visit) to be entered and stored, which can be retrieved by patient, ward, or clinic. Information entered through PCE can be viewed on Health Summaries or other reports.

## Purpose and Benefits of PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration has determined that it must have adequate, accurate, and timely information about each ambulatory care encounter/service provided in order to enhance patient care and to manage our health care resources into the future. Effective October 1, 1996, VHA facilities are required to report each ambulatory encounter and/or ancillary service. Provider, procedure, and diagnosis information is included in the minimum data set that will be reported to the National Patient Care Data Base (NPCDB). The Ambulatory Data Capture Project was formed to coordinate the many software packages and their developers who support this effort.

*Goals of Ambulatory Data Capture Project*

- Capture purpose of visit/problem, diagnoses, procedures, and providers
- Develop a fast, accurate method for getting ambulatory care data into V*IST*A
- Return clinically relevant data back to the Clinician
- Make data available for workload reporting, DSS, research, MCCR, and other ongoing VHA needs

*Software necessary to support ADCP*

- Automated Information Collection System (AICS) and other capture solutions
- Patient Care Encounter
- Problem List
- Patient InformationManagement System
- National Patient Care Data Base

Patient Care Encounter (*PCE) ensures that every encounter has an associated provider(s), procedure code(s), and diagnostic code(s), in accordance with this mandate.*

PCE also helps fill a gap in current V*IST*A patient information by capturing other clinical data such as exams, health factors, immunizations, skin tests, treatments, and patient education, which can then be viewed on Health Summaries and other clinical reports, and can be used to produce clinical reminders on Health Summaries.

Functionality of PCE

Version 1.0 of PCE provides options that allow:

1.  Collection and management of outpatient encounter data.
2.  Presentation of outpatient encounter data through Health Summary components and Clinical Reports. Outpatient encounter data is captured through interactive and non-interactive interfaces.

*Interactive interfaces*

- Online data capture using a user interface developed with List Manager tools.
- Online data capture in which Scheduling integrates with PCE to collect checkout information.

*Non-interactive interfaces*

- PCE Device Interface, which supports the collection of encounter form data from scanners such as PANDAS, Pen-based Teleform, and Automated Information Collection System (AICS). The interface also supports workstation collection of outpatient encounter data.
- PCE application programming interface (API) which supports the collection of outpatient encounter data from ancillary packages such as Laboratory, Radiology, Text Integration Utility (TIU), and Computerized Patient Record System (CPRS).

  
Definitions

- Outpatient Visit: The visit of an outpatient to one or more units or facilities located in or directed by the provider maintaining the outpatient health care services (clinic, physician’s office, hospital/medical center) within one calendar day.
- Encounter: A contact between a patient and a provider who has primary responsibility for assessing and treating the patient at a given contact, exercising independent judgment. A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communications with a patient may be represented by a separate visit entry. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter.
- Episode of Care: Many encounters for the same problem can constitute an episode of care. An outpatient episode of care may be a single encounter or can encompass multiple encounters over a long period of time. The definition of an episode of care may be interpreted differently by different professional services even for the same problem. Therefore, the duration of an episode of care is dependent on the viewpoints of individuals delivering or reviewing the care provided.
- Ancillary Service/Occasion of Service: A specified instance of an act of service involved in the care of a patient or consumer which is not an encounter. These occasions of service may be the result of an encounter; for example, tests or procedures ordered as part of an encounter. A patient may have multiple occasions of service per encounter or per visit.
- Provider: The entity which furnishes health care to a consumer. This definition includes an individual or defined group of individuals who provide a defined unit of health care services (defined = codable) to one or more individuals at a single session.

  
Potential PCE Workflow

1. A provider has a patient encounter (appointment, walk-in, telephone call, mail conversation, etc.).

Materials available to provider:

- *Health Summary* with new components summarizing previous encounters, and a health reminders component based on clinical repository data
- *Encounter Form* (hard copy or workstation) with pre-defined terminology for the provider’s clinic/service type
- *PCE Clinical Reports*, Action Profile, Daily Order Summary, Lab Interim report, and *other*V*IST*A *reports.*2. The provider documents the encounter (on hard copy or online).

Types of data collected and stored in PCE:

*ProvidersDiagnosesCPT procedures providedImmunizations (CPT-mappable)Skin tests (CPT-mappable)Patient educationExams (non-CPT-mappable)Treatments (non-CPT-mappable)*3. Information from a hard copy encounter form is entered into V*IST*A by a data entry clerk or scanned via an interface utility.

4. Encounter form data that isn’t scanned or is scanned incorrectly can be entered or edited through the PCE data entry program described in this manual.
5. Providers can enter immunizations, patient education, or other pieces of clinical information through PCE.
6. Providers can view items entered into PCE on a Health Summary or customized report. If any of these items have been set up for clinical reminders, these reminders will appear on the patient's health summary.

  
Sources of Data

PCE data can be entered through many mechanisms, including:

- Scheduling (PIMS) check-out process
- AICS Encounter Forms
- PANDAS scanning system
- TELEFORM scanning system
- Imaging workstation
- Clinical Workstation

## Designing Encounter Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use AICS Encounter Forms with scanners or for direct data entry (either clinician or data entry clerk), you can design encounter forms for your hospital or clinic with the AICS Encounter Form generator. See the *AICS User Manual* for instructions about creating Encounter Forms.

XU\*8\*27 - New Person File Patch

As part of the October 1, 1996 mandate, VAMCs must collect provider information. The provider information reported is the "Person Class" defined for all providers associated with ambulatory care delivery.

To comply with this requirement, all VAMC providers must be assigned a Profession/Occupation code (Person Class) so that a Person Class can be associated with each ambulatory patient encounter by October 1.

Patch XU\*8\*27 has been developed to provide functionality that will enable you to assign Person Class information.

# PX\*1.0\*184 – Automated Service Connected Designation (ASCD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Service Connected Designation (ASCD) project automates the Service Connected decision for outpatient encounters using the mapped ICD/Rated Disability Codes at the time the clinician actually picks the ICD code for the outpatient encounter within the Patient Care Encounter (PCE) and Scheduling packages. 

In the current clinical work environment, providers are requested to designate at the point of care if a specific patient care encounter is service connected (SC) based on available disability rating information. This software will computerize the clinician’s process at each encounter, i.e. mark the encounter service-connected (SC) or non service-connected (NSC) as appropriate. Thus, when a provider or clinician chooses the diagnosis code for the encounter the system will automatically determine if the diagnosis is related to the veteran's established service connected conditions, and will likewise automatically make the proper SC/NSC determination for that encounter.

Modifications made to the outpatient checkout diagnosis entry process automates the response to the question "Was treatment for SC Condition?" for each diagnosis code. The question will not allow user entry and will be displayed briefly to the user with the ASCD answer.

The PCE Encounter Data Entry - Supervisor \[PXCE ENCOUNTER ENTRY SUPER\] option allows users to change the ASCD value which will be displayed as the default. This allows users to access encounters that are not set for review and are not accessible via the ASCD review options.

Modifications were made to the checkout screen under the section “Patient’s Service Connection and Rated Disabilities:” to display the RATED DISABILITY CODE number before the Rated Disabilities (VA) name.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Screen Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCE uses the List Manager utility which allows PCE to display a list of items in a screen format, with possible actions (add, edit, print) listed below. If the list is longer than one screen, the header and action portions of the screen remain stable, while the center display scrolls. So if there are too many patient encounters to fit within the scrolling portion of the screen, when you press the return key, that portion of the screen scrolls while the top and bottom stay unchanged.

<u>PCE Appointment List May 12, 1995 12:53:07 Page: 1 of 3</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 03/13/95 to 05/26/95

<u>Clinic Appt Date/Time Status</u>

1 Xyz Mar 27, 1995 08:00 Cancelled By Patient

2 Xyz Mar 27, 1995 09:00 No-show

3 Xyz Mar 27, 1995 09:30 Cancelled By Patient

4 Xyz Mar 27, 1995 10:00 No-show

5 Xyz Mar 28, 1995 08:30 Checked Out

6 Xyz Mar 28, 1995 08:50 No-show

+ + Next Screen - Prev Screen ?? More Actions

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Encounter CD Change Date Range DD Display Detail

AD Add Standalone Enc. EP Expand Appointment

AL Appointment Lists IN Check Out Interview QU Quit

Select Action: Quit// AD Add New Encounter

Without leaving the option, you can:

- browse through the list,
- select items that need action,
- take action on those items, or
- select other actions,

You select an action by typing the name or abbreviation at the “Select Action” prompt.

Actions may be preselected by typing the action abbreviation, then the number of the encounter on the list. For example, UE=1 will process entry 1 for Update Encounter

  
Other (hidden) Actions

If you enter two question marks (??) at the Select Item(s) prompt, you will see a list of other actions that you can use with PCE.

Select Item(s): Quit// ??

The following actions are also available:

\+ Next Screen FS First Screen SL Search List

\- Previous Screen LS Last Screen ADPL Auto Display(On/Off)

UP Up a Line GO Go to Page

DN Down a Line RD Re Display Screen SP Leave Update and

\> Shift View to Right PS Print Screen Select New Patient

\< Shift View to Left PL Print List

Press RETURN to continue or '^' to exit:

## Review Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCE provides several different perspectives for viewing encounter data. You can change to any of these views whenever you're at a "Select Action:" prompt.

- List by Appointment
- List by Encounter
- Select New Patient
- View by Clinic/Ward
- Change Date Range
- Display Detail
- Expand Appointment
- Appointment Lists

#### List by Appointment

Most encounters are associated with an appointment (the exceptions are Standalone Encounters, which are usually walk-ins, and Historical Encounters, which usually took place at another location). Therefore, you need to identify an appointment to associate encounter information with before you enter this information. You can change your view to List by Encounter if you wish to enter standalone or historical encounters. You can also change your default view (whether you see the Appointment List or the Encounter List when you enter PCE) through the option, PCE Parameters Add/Edit.

<u>PCE Appointment List Jul 26, 1996 08:07:20 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96 Total Appointment Profile

<u>Clinic Appt Date/Time Status</u>

1 Diabetes Clinic May 18, 1996 16:48 Action Req/Checked Out

2 Cardiology May 22, 1996 09:00 Checked Out

3 Diabetes Clinic Jun 22, 1996 11:00 Checked Out

4 Cardiology Jun 23, 1996 09:00 No Action Taken

5 Diabetes Clinic Jun 23, 1996 09:30 Checked Out

6 Diabetes Clinic Jul 23, 1996 10:00 No Action Taken

7 Cardiology Jul 25, 1996 09:00 Checked Out

<span class="mark">. + Next Screen - Prev Screen ?? More Actions .</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Encounter CD Change Date Range DD Display Detail

AD Add Standalone Enc. EP Expand Appointment

AL Appointment Lists IN Check Out Interview QU Quit

Select Action: Quit//

#### #### #### List by Encounter

<u>PCE Encounter List Jul 26, 1996 08:14:24 Page: 1 of 2</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96

<u>Encounter Clinic Clinic Stop</u>

1 07/26/96 07:56 DIABETES CLINIC 306 DIABETES

2 07/25/96 09:00 CARDIOLOGY 303 CARDIOLOGY

3 07/23/96 16:28 HAND 409 ORTHOPEDICS

4 06/22/96 09:00 CARDIOLOGY 303 CARDIOLOGY

5 06/22/96 11:00 DIABETES CLINIC 306 DIABETES

6 05/22/96 16:19 DIABETES CLINIC 306 DIABETES

<span class="mark">+ + Next Screen - Prev Screen ?? More Actions</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Next Screen//

*Select New Patient, View by Clinic, Change Date Range*

You can change to another patient, another Clinic, or to a different date range and start all over just by selecting one of these actions at any Select Action prompt.

#### *Display Detail*

<u>PCE Encounter List Jul 26, 1996 08:14:24 Page: 1 of 2</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96

<u>Encounter Clinic Clinic Stop</u>

1 07/26/96 07:56 DIABETES CLINIC 306 DIABETES

2 07/25/96 09:00 CARDIOLOGY 303 CARDIOLOGY

3 07/23/96 16:28 HAND 409 ORTHOPEDICS

4 06/22/96 09:00 CARDIOLOGY 303 CARDIOLOGY

5 06/22/96 11:00 DIABETES CLINIC 306 DIABETES

6 05/22/96 16:19 DIABETES CLINIC 306 DIABETES

<span class="mark">+ + Next Screen - Prev Screen ?? More Actions</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Next Screen//dd Display Detail

Select Encounter (1-22): 1

#### <u>Encounter Profile Jul 26, 1996 08:42:06 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: DIABETES CLINIC

Encounter Date 07/26/96 07:56 Clinic Stop: 306 DIABETES

<u>1 Encounter Date and Time: JUL 26, 1996@07:56:37</u>

Patient Name: PCEPATIENT,ONE

Hospital Location: DIABETES CLINIC

Clinic Stop: 306 DIABETES

Service Connected: NO

Combat Veteran: NO

Agent Orange Exposure: NO

Ionizing Radiation Exposure: NO

Persian Gulf Exposure: NO

Military Sexual Trauma: NO

Head and/or Neck Cancer: NO

<span class="mark">+ Next Screen - Prev Screen ?? More Actions</span>

EP Expand Entry

Select Action:Quit// ep Expand Entry

#### Expand Appointment 

This action lets you see an Expanded Profile for a selected patient appointment. Note that the top line says Page: 1 of 5, indicating that you should press ENTER after each screen display to see the entire expanded profile. To scroll back, press the minus (-) key.

<u>Expanded Profile Jul 26, 1996 08:48:51 Page: 1 of 5</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

Appointment \#: 1 Clinic: DIABETES CLINIC

<u>\*\*\* Appointment Demographics \*\*\*</u>

Name: PCEPATIENT,ONE Clinic: DIABETES CLINIC

ID: 000-45-6789 Date/Time: JUL 18, 1996@16:48

Status: ACTION REQ/CHECKED OUT

Purpose of Vst.: UNSCHEDULED

Length of Appt: 30 Appt Type: REGULAR

Lab: Elig of Appt: SC LESS THAN 50%

X-ray: Overbook: NO

EKG: Collateral Appt: NO

Other Info:

Enrolled in this clinic: YES OPT or AC: OPT

Enrollment Date/Time: JUN 04, 1995

<span class="mark">+ Enter ?? for more actions</span>

Select Action: Next Screen// \[ENTER\]

#### <u>Expanded Profile Jul 26, 1996 08:52:10 Page: 2 of 5</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

Appointment \#: 1 Clinic: DIABETES CLINIC

\+

<u>\*\*\* Appointment Event Log \*\*\*</u>

Event Date User

----- ---- ----

Appt Made JUL 18, 1996 PCEUSER,ONE

Check In

Check Out JUL 18, 1996@16:48 PCEUSER,ONE

Check Out Entered JUL 18, 1996@16:49:05

No-Show/Cancel

Checked Out:

Cancel Reason:

Cancel Remark:

Rebooked Date:

<span class="mark">+ Enter ?? for more actions</span>

Select Action: Next Screen// \[ENTER\]

<u>Expanded Profile Jul 26, 1996 08:52:10 Page: 3 of 5</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

<u>Appointment \#: 1 Clinic: DIABETES CLINIC</u>

\*\*\* Patient Information \*\*\*

Date of Birth: APR 01, 1944 ID: 000-45-6789

Sex: FEMALE Marital Status: SINGLE

Religious Pref.: UNKNOWN/NO PREFERENC

Primary Elig.: SC, LESS THAN 50% POS: VIETNAM ERA

Address: Phone:

321 S 3400 E

SALT LAKE CITY, UTAH 84105

Radiation Exposure: YES Status: NO INPT./LOD. ACT.

Prisoner of War: NO Last Admit/Lodger Date:

AO Exposure: YES Last Disch./Lodger Date:

<span class="mark">+ Enter ?? for more actions</span>

Select Action: Next Screen// \[ENTER\]

#### <u>Expanded Profile Jul 26, 1996 08:52:10 Page: 4 of 5</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

<u>Appointment \#: 1 Clinic: DIABETES CLINIC</u>

\*\*\* Check Out \*\*\*

CLASSIFICATION \[Required\]

1 Treatment for SC Condition: NO

2 Combat Veteran: NO

3 Agent Orange Exposure: YES

4 Ionizing Radiation Exposure: NO

5 Environmental Contaminants: NO

6 Military Sexual Trauma: NO

7 Head and/or Neck Cancer: NO

PROVIDER \[Required\] DIAGNOSIS \[Required\]

1 PCEPROVIDER,ONE+<span class="mark">Enter ?? for more actions</span>

Select Action: Next Screen// \[ENTER\]

#### <u>Expanded Profile Jul 26, 1996 08:52:10 Page: 5 of 5</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

<u>Appointment \#: 1 Clinic: DIABETES CLINIC</u>

\+

STOP CODES \[Not Required\]

Enter ?? for more actions

Select Action: Quit// \[ENTER\]

#### Appointment

This action gives you a list of possible appointment statuses and lets you change the appointments that will appear on the list, based on their statuses.

<u>PCE Appointment Jul 26, 1996 09:04:16 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96 Total Appointment Profile

<u>Clinic Appt Date/Time Status</u>

1 Diabetes Clinic Jul 18, 1996 16:48 Action Req/Checked Out

3 Cardiology Jul 22, 1996 09:00 Checked Out

4 Cardiology Jul 22, 1996 10:00 Checked Out

5 Diabetes Clinic Jun 22, 1996 11:00 Checked Out

7 Cardiology Jun 23, 1996 09:00 No Action Taken

11 Cardiology May 25, 1996 09:00 Checked Out

<span class="mark">+ Next Screen - Prev Screen ?? More Actions</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Encounter CD Change Date Range DD Display Detail

AD Add Standalone Enc. EP Expand Appointment

AL Appointment Lists IN Check Out Interview QU Quit

Select Action: Quit// AL Appointment Lists

Select List:Total Appt Profile// ?

CA Cancelled NA No Action Taken

CI Checked In NC Non Count Appointments

CO Checked Out NS No Shows

FU Future Appointments TA Total Appt Profile

IP Inpatient Appointments

Enter selection(s) by typing the name(s), number(s), or abbreviation(s).

Select List:Total Appt Profile// CO

<u>PCE Appointment List Jul 26, 1996 09:11:39 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

<u>Date range: 07/16/96 to 07/30/96 Checked Out Appointments</u>

Clinic Appt Date/Time Status

2 Cardiology Jul 22, 1996 09:00 Checked Out

4 Diabetes Clinic Jul 22, 1996 11:00 Checked Out

7 Diabetes Clinic Jun 24, 1996 09:00 Checked Out

8 Cardiology Jun 25, 1996 09:00 Checked Out

<span class="mark">+ Next Screen - Prev Screen ?? More Actions</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Encounter CD Change Date Range DD Display Detail

AD Add Standalone Enc. EP Expand Appointment

AL Appointment Lists IN Check Out Interview QU Quit

Select Action: Quit// \[ENTER\]

# # Using PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health Care Providers and data entry clerks primarily use PCE to enter or edit encounter data, to create clinical reminders to be viewed on Health Summaries, and to view or print clinical reports summarizing various information about patients in a clinic. This section describes how to perform these functions.

## PCE Data Entry Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Care Encounter lets you add information, edit information, or add a new encounter to a patient's database. When you enter the program through the PCE User Interface described in this manual, you first view a list of encounters for a patient (by appointment). Appointments are provided to the PCE program by the Checkout process of the Scheduling package.

After you select a particular view and the appointments or encounters are displayed on your screen, you can add or edit information.

PCE has four options for adding or editing encounter information.

*PCE Encounter Data Entry - Supervisor*

This option is for users who can document a clinical encounter in PCE, and can also delete any encounter entries, even though they are not the creator of the entries. This option is intended for the Coordinator for PCE and/or supervisor of the encounter data entry staff.

*PCE Encounter Data Entry*

This option is for users who can document a clinical encounter in PCE, but can only delete entries they have created. The data entered via this option includes visit information (where and when), and clinical data related to the visit: providers of care, problems treated, procedures and treatments done, and immunizations, skin tests, and patient education given

*PCE Encounter Data Entry and Delete*

This option is for users who can document a clinical encounter in PCE, and can also delete any encounter entries, even though they are not the creator of the entries. This option is on the Clinician menu.

*PCE Encounter Data Entry without Delete*

This option is for users who can document a clinical encounter in the PCE, but should not be able to delete any entries, including ones that they have created.

### ### ### PCE Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

"Actions" are the choices listed at the bottom of the PCE screens (following the shaded bar) which you can select, either to edit or add to the appointments or encounter shown in the top part of the screen, or to see a different view of that information.

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Encounter CD Change Date Range DD Display Detail

AD Add Standalone Enc. EP Expand Appointment

AL Appointment Lists IN Check Out Interview QU Quit

The following actions can be used at the Appointment List or Encounter List screens.

ADD STANDALONE ENC. - This action lets you add a new encounter not associated with a credit stop.

APPOINTMENT LISTS - This action allows you to change which appointments will be displayed based on their status. For example, you may change the display to list cancelled, checked in, checked out, future appointments, inpatient appointments, appointment where no action has been taken, non-count appointments, no show appointments, or all appointments.

CHANGE CLINIC - This action lets you change the display list of encounters based on hospital location. If the list includes encounters for all locations, you can select a new location and the list will be redisplayed with only encounters that relate to that location.

CHANGE DATE RANGE - This action allows you to change the date range used for displaying encounters or appointments. You may change the beginning and/or ending date.

CHECKOUT INTERVIEW - This action allows you to go through the interview questions for an encounter that is associated with an appointment. You may also edit additional information such as provider, diagnosis, and procedure. You may also edit an encounter that is associated with an appointment by entering the number associated with the item at the "Select Action" prompt or using the Update Encounter.

DISPLAY DETAIL - This action displays all available information related to one encounter for a selected appointment.

EXPAND APPOINTMENT - This action allows you to display all the patient demographics and appointment event log items that have been entered for a selected patient appointment. Expand Appointment displays information from the Scheduling package and not from PCE.

LIST BY ENCOUNTER - This action allows you to change the display from a list of appointments for this patient or clinic to a list of encounters for the same patient or clinic. There may be several encounters for one appointment.

LIST BY APPOINTMENT - This action allows you to change the display from a list of encounters for this patient or clinic to a list of appointments for the same patient or clinic. Not every appointment may have an encounter associated with it, so you can add encounters from this view.

MAKE HISTORICAL ENC - This action lets you add encounter information for an old encounter or one that took place at another hospital or clinic (VA or non-VA). Although you can't get workload credit for this kind of encounter, it can be used to help compute clinical reminders.

SELECT NEW PATIENT - This action allows you to change the display of encounters based on the patient. If you select a new patient, the display will include encounters or appointments for the selected patient.

UPDATE ENCOUNTER - This action lets you edit an encounter that is associated with an appointment. You may edit information such as provider, diagnosis, procedure, treatment, immunization, skin test, patient education, exams, and treatments, as well as date, service connection, and demographic data.

VIEW BY CLINIC - This action allows you to change the display of appointments or encounters based on a Clinic. For example, if your current list includes all appointments for a specified date range for the selected patient, and you want to display all appointments for a specific clinic, you may use this action to change the display to include appointments or encounters for the desired clinic.

QUIT - This action allows you to exit PCE and return to your menu.

> **NOTE:** You can add Health Summary, Problem List, and Progress Notes as actions to the PCE screens, to enable you to go directly to these programs. See the *PCE Installation Guide* for instructions.

### Adding and Editing Patient Care Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Follow the steps in the next few pages to add, delete, or edit encounters.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding New Encounters

Use the Add Standalone Enc. action to enter a new encounter which may or may not have an appointment associated with it.

1. Select the PCE Encounter Data Entry option and a patient or clinic.

Select PCE Clinician Menu Option: ENC PCE Encounter Data Entry and Delete

Select Patient or Clinic name: PCEPATIENT,ONE2. Select Add Standalone Enc at the Select Action prompt.

<u>PCE Encounter List Jul 26, 1996 07:46:56 Page: 1 of 2</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96

<u>Encounter Clinic Stop</u>

1 07/25/96 08:00 DIABETES CLINIC 306 DIABETES

2 07/25/96 09:00 CARDIOLOGY 303 CARDIOLOGY

3 07/23/96 16:28 HAND 409 ORTHOPEDICS

4 06/22/96 09:00 CARDIOLOGY 303 CARDIOLOGY

5 06/22/96 11:00 DIABETES CLINIC 306 DIABETES

6 05/19/96 15:07 CARDIOLOGY 303 CARDIOLOGY

<span class="mark">+ + Next Screen - Prev Screen ?? More Actions</span>

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Next Screen// AD Add Standalone Enc.

3. Enter the Encounter Date and Time and the Hospital Location where the encounter took place.

Encounter Date and Time: N (7/1/96 - 7/26/96):N (JUL 26, 1996@07:47:51)

Hospital Location: DIABETES CLINIC PCEPROVIDER,ONE

APPOINTMENT TYPE: REGULAR// \[ENTER\]  
4. Respond to the following classification prompts:

--- Classification --- \[Required\]

Was treatment for SC Condition? NO \<- Response automated\*

Was treatment related to Combat? YES// NO

Was treatment related to Agent Orange Exposure? NO

Was treatment related to Ionizing Radiation Exposure? NO

Was treatment related to Environmental Contaminant Exposure? NO

Was treatment related to Military Sexual Trauma? NO

Was treatment related to Head and/or Neck Cancer? NO*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*5. The screen displays the encounter data.

<u>PCE Update Encounter Jul 26, 1996 07:56:59 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: DIABETES CLINIC

Encounter Date 07/26/96 07:56 Clinic Stop: 306 DIABETES

<u>1 Encounter Date and Time: JUL 26, 1996@07:56:37</u>

<span class="mark">+ Next Screen - Prev Screen ?? More Actions</span>

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// \[ENTER\]

### Make Historical Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create encounters for patient visits that occurred at some time in the past (exact time may be unknown) or at some other location (possibly non-VA). Although these are not used for workload credit, they can be used for setting up the reminder maintenance system.

> **NOTE:** If month or day aren't known, historical encounters will appear on encounter screens or reports with zeroes for the missing dates; for example, 01/00/95 or 00/00/94.

*Steps to use this action:*1. Change to View by Encounters if you are in the Appointment View.2. Select the Make Historical Enc action at the Select Action prompt.

<u>PCE Encounter List Jul 26, 1996 07:46:56 Page: 1 of 2</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/16/96 to 07/30/96

<u>Encounter Clinic Clinic Stop</u>

1 07/25/96 08:00 DIABETES CLINIC 306 DIABETES

2 07/25/96 09:00 CARDIOLOGY 303 CARDIOLOGY

3 07/23/96 16:28 HAND 409 ORTHOPEDICS

4 06/22/96 09:00 CARDIOLOGY 303 CARDIOLOGY

5 06/22/96 11:00 DIABETES CLINIC 306 DIABETES

6 05/19/96 15:07 CARDIOLOGY 303 CARDIOLOGY

+ + Next Screen - Prev Screen ?? More Actions

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Next Screen// HI

This will create a historical encounter for documenting a clinical encounter only and will not be used by Scheduling, Billing or Workload credit.

Enter RETURN to continue or '^' to exit: \[ENTER\]2. Enter the date of the encounter and the time, if known.3. Enter the location where the encounter took place. If it happened at a non-VA hospital or clinic, type that name. Otherwise enter the name or number of the VA Medical Center or other facility.

Encounter Date and (optional) Time: 12/95 (DEC 1995)

Is this a VA location? N// \[ENTER\]

Non VA Location of Encounter: University Clinic

Comments:

4. (optional) Enter any comments that are needed to clarify the encounter.

### Update Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the Update Encounter action you can add or edit encounter information, either through the Edit an Item or Delete an Item actions, or by choosing one of the following:

*CPT (Procedure) Diagnosis (ICD9)Encounter ExamHealth Factors ImmunizationPatient Ed ProviderSkin testTreatment*NOTE: IRM or a Clinical Coordinator can change the items or categories available to choose from for many of these actions (Treatment, Patient Ed, Immunization, etc.) through the PCE Table Maintenance Menu. If you wish to define these items, check with your Coordinator.

*Follow the steps below to use Update Encounter.*1. Type the name of the patient or the clinic whose encounters you want to edit.

Select Patient or Clinic Name: PCEPATIENT,ONE2. A screen like this appears. Type UE at the “Select Action” prompt.

<u>PCE Encounter List Jul 25, 1996 07:41:25 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/15/96 to 07/29/96

<u>Encounter Clinic Clinic Stop</u>

1 07/22/96 11:08 CARDIOLOGY 303 CARDIOLOGY

+ Next Screen - Prev Screen ?? More Actions

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Quit// UE3. Select the appointment you wish to add items to or to edit.  
4. Select the number of the item to be edited or an action that will let you add or edit encounter information.

<u>PCE Update Encounter Jul 25, 1996 07:45:02 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

<u>Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY</u>

1 Encounter Date and Time: JUL 22, 1996@11:08:14

2 Provider: PCEPROVIDER,ONE PRIMARY

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// 4

#### #### Quick Tricks

After Diagnosis has been entered, if the Provider Narrative is an exact match, you can enter = and the diagnosis will be duplicated here.

The equals sign (=) can also be used as a shortcut when selecting an action plus encounters or appointments from a list in a single response (e.g., Select Action: ED=2).

UE=1 will process entry 1 for Update Encounter

*Edit an Item*

When you choose the action Edit an Item, you will be prompted item-by-item to enter information about a selected encounter.

*Steps to Edit an Item*1. Select UE from the PCE Encounter List screen.

<u>PCE Encounter List Jul 25, 1996 07:41:25 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: All

Date range: 07/15/96 to 07/29/96

<u>Encounter Clinic Clinic Stop</u>

1 07/22/96 11:08 CARDIOLOGY 303 CARDIOLOGY

+ Next Screen - Prev Screen ?? More Actions

UE Update Encounter SP Select New Patient VC View by Clinic

LI List by Appointment CD Change Date Range DD Display Detail

AD Add Standalone Enc. CC Change Clinic

HI Make Historical Enc. IN Check Out Interview QU Quit

Select Action: Quit// UE2. Select the encounter you wish to edit.3. Select ED from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 07:45:02 Page: 1 of 1</u>

<u>PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY</u>

<u>Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY</u>

1 Encounter Date and Time: JUL 22, 1996@11:08:14

2 Provider: PCEPROVIDER,ONE PRIMARY

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// ED4. Respond to each of the following prompts, as appropriate.

Select Entry(s) (1-5): 1-5

Provider: PCEPROVIDER,ONE// PCEPROVIDER,TWO

Is this Provider Primary: YES// \[ENTER\]

Is this Provider Attending: NO// y YES

ICD9 Code or Diagnosis: V70.3// \[ENTER\] V70.3 MED EXAM NEC-ADMIN PURP

...OK? Yes// \[ENTER\] (Yes)

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR ADMINISTRATIVE PURPOSES Replace \[ENTER\]

OTHER GENERAL MEDICAL EXAMINATION FOR ADMINISTRATIVE PURPOSES

Is this Diagnosis Primary: YES// \[ENTER\]

Modifier: \[ENTER\]

Encounter Provider: PCEPROVIDER,TWO

Comments: \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO \<- Response automated\*

CPT Code: 25066// \[ENTER\] BIOPSY FOREARM SOFT TISSUES

Select CPT MODIFIER: 22// \[ENTER\]

Provider Narrative: BIOPSY FOREARM SOFT TISSUES Replace SUSPICIOUS LUMP

Quantity: 1// \[ENTER\]

Diagnosis: MALIGNANT TUMOR

Principal Procedure: \[ENTER\]

Encounter Provider: PCEPROVIDER,ONE// PCEPROVIDER,TWO

Comments: \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO \<- Response automated\*

Education Topic: VA-TOBACCO USE SCREENING Replace \[ENTER\]

Level of Understanding: GOOD// GOOD

Encounter Provider: PCEPROVIDER,ONE// PCEPROVIDER,TWO

Comments: \[ENTER\]*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*5. The edited screen is then displayed.

<u>PCE Update Encounter Jul 25, 1996 08:09:16 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

<u>Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY</u>

1 Encounter Date and Time: JUL 22, 1996@11:08:14

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// \[ENTER\]

#### Delete an Item

*Steps to Delete an Item*1. Select UE from the PCE Encounter List screen.2. Select the encounter you wish to edit.3. Select DE from the PCE Update Encounter screen.

PCE Update Encounter Jul 25, 1996 08:14:43 Page: 1 of 1

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// de Delete an Item

Select Entry(s) (1-5): 1-54. Answer the following prompts to indicate which items you will delete.

Deleting Provider PCEPROVIDER,ONE PRIMARY ATTENDING

Are you sure you want to remove this entry? NO// \[ENTER\]

Deleting Diagnosis V70.3 MED EXAM NEC-ADMIN PURP

Are you sure you want to remove this entry? NO// \[ENTER\]

Deleting CPT 25066 BIOPSY FOREARM SOFT TISSUES

Are you sure you want to remove this entry? NO// \[ENTER\]

Deleting Patient Education VA-TOBACCO USE SCREENING

Are you sure you want to remove this entry? NO// YES

Deleting Encounter JUL 22, 1996@11:08:14 CARDIOLOGY CARDIOLOGY

Are you sure you want to remove this entry? NO// \[ENTER\]

5. The edited screen is then displayed.

<u>PCE Update Encounter Jul 25, 1996 08:16:02 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// \[ENTER\]

#### How to Add or Edit an Encounter

You can add an encounter for an appointment that doesn’t have an encounter associated with it, or edit an existing encounter.

*Steps to edit an Encounter*1. Select UE from the PCE Appointment List screen.2. Select EN from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// EN Encounter

3. Respond to the following prompts for the encounter, as appropriate.

Check out date and time: JUN 17,1996@09:00// \[ENTER\](JUN 17, 1996@09:00)

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? YES \<- Response automated\\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*  
4. If answer is NO to the last prompt above, you get additional prompts as shown below.

Check out date and time: MAY 23,1996@15:17//\[ENTER\](MAY 23, 1996@15:17)

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO// \<- Response automated\*

Was treatment related to Combat? YES// NO

Was treatment related to Agent Orange Exposure? n NO

Was treatment related to Ionizing Radiation Exposure? n NO

Was treatment related to Environmental Contaminant Exposure? n NO

Was treatment related to Military Sexual Trauma? n NO

Was treatment related to Head and/or Neck Cancer? n NO

*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*

#### How to Add or Edit a Provider

When you enter or edit a provider for an encounter, you will be prompted to enter whether the provider is Primary and/or Attending. The default provider entered at checkout is the primary provider.

*Steps to add or edit a Provider*1. Select UE, from the PCE Appointment List screen.2. Select the appointment and encounter you wish to edit.3. Select PR from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// PR Provider

4. Choose whether you want to edit or add and respond to the other prompts, as appropriate.

--- Provider ---

1 PCEPROVIDER,ONE PRIMARY ATTENDING

Enter 1-1 to Edit, or 'A' to Add: 1

Provider: PCEPROVIDER,ONE// \[ENTER\] PCEPROVIDER,ONE

Is this Provider Primary: YES// \[ENTER\]

Is this Provider Attending: YES// NO5. The edited screen is then displayed.

#### How to Add or Edit Diagnoses (ICD 9)

You can enter a diagnosis and/or an ICD-9 code for a patient’s encounter. You will be prompted to designate the diagnosis as primary or secondary. CIDC (Clinical Indicator Data Capture) has added functionality that displays patient Service Connected and Rated Disabilities for those SC patients. In addition, an optional Ordering/Resulting Diagnosis prompt asks “Is this Diagnosis Ordering, Resulting, or Both.” See NOTE in Step 3.

With functionality put in place by the Code Set Versioning project, only ICD Codes that are active for the encounter date and time will be available.

*Steps to add a Diagnosis*1. Select UE from the PCE Appointment List screen.2. Select DX from the PCE Update Encounter screen.The sample below is from PCE Data Entry, also note that these prompts are seen in the Appointment Manangement Check-Out option.

PCE Update Encounter Aug 21, 2003@15:57:33 Page: 1 of 1

PCEpatient,one 000-00-0001P Clinic: GENERAL MEDICINE AT ALBANY

Encounter Date 6/25/2003 10:00 Clinic Stop: 301 GENERAL INTERNAL MEDI

1 Encounter Date and Time: JUN 25, 2003@10:00

\+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// DX Diagnosis (ICD 9) \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 100%

Rated Disabilities: 5010 TRAUMATIC ARTHRITIS (10%-SC)

7913 DIABETES MELLITUS (0%-SC)

--- Diagnosis ---

1 891.0 OPEN WND KNEE/LEG/ANKLE

2 200.01 RETICULOSARCOMA HEAD

Enter 1-2 to Edit, or 'A' to Add: A \[ENTER\]3. Respond to the following prompts for the diagnosis, as appropriate.

Patient's Service Connection and Rated Disabilities:

SC Percent: 100%

Rated Disabilities: 5010 TRAUMATIC ARTHRITIS (10%-SC)

7913 DIABETES MELLITUS (0%-SC)

ICD9 Code or Diagnosis: 891.0// 891.0 891.0 OPEN WND KNEE/LEG/ANKLE

...OK? Yes// (Yes) \[ENTER\]

Provider Narrative: OPEN WOUND OF KNEE, LEG (EXCEPT THIGH), AND ANKLE, WITHOUT

MENTION OF COMPLICATION

Replace \[ENTER\]

OPEN WOUND OF KNEE, LEG (EXCEPT THIGH), AND ANKLE, WITHOUT MENTION OF COMPLICATI

ON \[ENTER\]

Is this Diagnosis Primary for the Encounter: YES// \[ENTER\]Is this Diagnosis Ordering, Resulting, or Both: RESULTING \[ENTER\] (See NOTE)

Injury Date and (optional) Time: \[ENTER\]

Modifier: FOLLOW UP \[ENTER\]

Encounter Provider: PCEprovider,one BM DOC \[ENTER\]

\[ Provider Narrative Category:\] \[ENTER\]

Comments: SEVERE HEADACHE \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO \<- Response automated\*

Was treatment related to Combat? YES// NO \[ENTER\]

Was treatment related to Agent Orange Exposure? NO// \[ENTER\]

Was treatment related to Ionizing Radiation Exposure? NO// \[ENTER\]

Was treatment related to Environmental Contaminant Exposure? NO// \[ENTER\]

Was treatment related to Military Sexual Trauma? NO// \[ENTER\]

Was treatment related to Head and/or Neck Cancer? NO// \[ENTER\]*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*NOTE: The Ordering/Resulting Diagnosis prompt is available for some application encounters (i.e., Surgery), that choose to distinguish between the ordering diagnosis and resulting diagnosis. This prompt is optional.

| If user chooses: | Integrated Billing (IB) can generate:                 |
|----------------------|-----------------------------------------------------------|
| Ordering             | Institutional claim UB92.                                 |
| Resulting            | Professional claim HCFA 1500.                             |
| Both                 | Institutional and Professional claims UB92 and HCFA 1500. |

When Ordering/Resulting Diagnosis is not entered, IB personnel must reseach the Provider’s documenation for Ordering and Resulting diagnosis information.

4. The edited screen is then displayed.

#### How to Add or Edit a CPT (Procedure)

When you choose CPT (Procedure) under Update Encounter, you will also be prompted to enter the Provider Narrative, Quantity, Diagnosis, Principal Procedure, Encounter Provider, and comments. With functionality put in place by the Code Set Versioning project, only CPT Codes that are active for the encounter date and time will be available.

One Primary diagnosis and up to seven Secondary diagnoses may be associated with a procedure as clinical indicators. The example below shows the association as it appears on the PCE Encounter Profile screen.

CPT Code: 76003 NEEDLE LOCALIZATION BY X-RAY

Order Reference: 13559999

Provider Narrative: RENAL CYST ABLATION

Quantity: 1

Ordering Provider: RNMprovider,one

Encounter Provider: RNMprovider,two

Primary Diagnosis: 246.2 CYST OF THYROID

1st Secondary Diagnosis: 362.54 MACULAR CYST OR HOLE

2nd Secondary Diagnosis: 364.63 PRIMARY CYST PARS PLANA

3rd Secondary Diagnosis: 364.64 EXUDAT CYST PARS PLANA

4th Secondary Diagnosis: 383.31 POSTMASTOID MUCOSAL CYST

5th Secondary Diagnosis: 478.26 CYST PHARYNX/NASOPHARYNX

6th Secondary Diagnosis: 522.8 RADICULAR CYST

7th Secondary Diagnosis: 577.2 PANCREAT CYST/PSEUDOCYST

*Steps to edit a CPT*1. Select UE from the PCE Appointment List screen.2. Select CP from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 02, 1999 08:24:21 Page: 1 of 1</u>

PCEoutpatient,two 000-00-0002 Clinic: CARDIOLOGY

Encounter Date 07/99/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEprovider,one PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// cp\[ENTER\] CPT (PROCEDURE)

Patient’s Service Connection and Rated Disabilities:SC Percent: 40%Rated Disabilities: 5257 KNEE CONDITION (20%-SC)5257 KNEE CONDITION (10%-SC)5003 DEGENERATIVE ARTHRITIS (10%-SC)3. Respond to the following prompts for the Procedure, as appropriate.

--- CPT ---

1 K0104 Cylinder tank carrier

Enter 1-1 to Edit, or 'A' to Add: A \[ENTER\]Patient's Service Connection and Rated Disabilities:SC Percent: 40%Rated Disabilities: 5257 KNEE CONDITION (20%-SC)5257 KNEE CONDITION (10%-SC)5003 DEGENERATIVE ARTHRITIS (10%-SC)

CPT Code: 82075 \[ENTER\] ASSAY OF BREATH ETHANOL

Select CPT MODIFIER: \[ENTER\]

Provider Narrative: BREATH TEST \[ENTER\]

Quantity: 1// 1 \[ENTER\]

Principal Procedure: YES

Ordering Provider: PCEprovider,one (RESIDENT) MFL 000A

Encounter Provider: PCEprovider,two (RESIDENT) MFL 000A

Provider Narrative Category: \[ENTER\]

Comments: TESTING CIDC \[ENTER\]Primary Diagnosis:303.01 \[ENTER\] AC ALCOHOL INTOX-CONTIN (w C/C)Diagnosis is Primary? P// PRIMARY\[ENTER\]

Provider Narrative: \[ENTER\]

ACUTE ALCOHOLIC INTOXICATION IN ALCOHOLISM, CONTINUOUS DRINKING BEHAVIOR

Diagnosis Modifier: \[ENTER\]

--- Classification --- \[Required\]

Was treatment for SC Condition? YES \<- Response automated\*

Was treatment related to Combat? YES// \[ENTER\]

Was treatment related to Agent Orange Exposure? y YES \[ENTER\]

Was treatment related to Ionizing Radiation Exposure? y YES \[ENTER\]

Was treatment related to Environmental Contaminant Exposure? y YES \[ENTER\]

Was treatment related to Military Sexual Trauma? y YES \[ENTER\]

Was treatment related to Head and/or Neck Cancer? NO// y YES \[ENTER\]

1st Secondary Diagnosis: \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 40%

Rated Disabilities: 5257 KNEE CONDITION (20%-SC)

5257 KNEE CONDITION (10%-SC)

5003 DEGENERATIVE ARTHRITIS (10%-SC)

CPT Code:

*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*4.The edited screen is then displayed.

<u>PCE Update Encounter Jul 02, 1999 08:24:21 Page: 1 of 1</u>

PCEoutpatient,two 000-00-0002 Clinic: TELEPHONE-PROSTHETICS

Encounter Date 10/00/2004 00:00 Clinic Stop: 999 TELEPHONE/PROSTHETICS

<u>1 Encounter Date and Time: OCT 00, 2004@00:00:00</u>

2 Provider: PCEprovider,one PRIMARY Physician/Physician/Osteopath/

3 ICD9 Code or Diagnosis: 303.01 AC ALCOHOL INTOX-CONTIN

Provider Narrative: ACUTE ALCOHOLIC INTOXICATION IN ALCOHOLISM, CONTINUOUS

DRINKING BEHAVIOR

Primary/Secondary Diagnosis for the Encounter: PRIMARY

4 ICD9 Code or Diagnosis: 716.26 ALLERG ARTHRITIS-L/LEG

Provider Narrative: ALLERGIC ARTHRITIS INVOLVING LOWER LEG

5 CPT Code: K0999 Cylinder tank carrier

Primary Diagnosis: 428.0 CONGEST HEART FAIL UNSPESIFIED

6 CPT Code: 82075 ASSAY OF BREATH ETHANOL

Provider Narrative: BREATH TEST

Primary Diagnosis: 303.01 AC ALCOHOL INTOX-CONTIN1st Secondary Diagnosis: 716.26 ALLERG ARTHRITIS-L/LEG<span class="mark">+ Next Screen - Prev Screen ?? More Actions</span>

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam 3M 3M Coding System

CP CPT (Procedure) HF Health Factors\[J Select Action: Quit//

#### How to Add or Edit Treatments

When you choose Treatment under Update Encounter, you will also be prompted to enter the Provider Narrative, How Many, Encounter Provider, and comments.

> **NOTE:** A Clinical Coordinator can change the items or categories available to choose from for Treatment through the PCE Table Maintenance Menu. If you wish to help define the Treatment list, check with your Coordinator.

*Steps to edit Treatment*1. Select UE from the PCE Appointment List screen.2. Select TR from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// TR3. Respond to the following prompts for the Treatment, as appropriate.

Treatment: Exercise

Provider Narrative: Circulatory Problems

How Many: 1// \[ENTER\]

Encounter Provider: PCEPROVIDER,FOUR// \[ENTER\] PCEPROVIDER,FOUR

Comments:\[ENTER\]4. The edited screen is then displayed.

#### How to Add or Edit an Immunization

When you choose Immunization under Update Encounter, you will also be prompted to enter the Provider, Series, Reaction, Repeat Contraindicated, ordering and administered times, and comments.

Immunizations are mapped to CPT codes. When an Immunization is entered, the user will be prompted for diagnoses which are associated with the mapped CPT code. If the diagnoses have not already appeared in the encounter, the user will be prompted for additional information to qualify the diagnosis such as modifiers, comments and SC/EI classifications.

> **NOTE:** A Clinical Coordinator can change the items or categories available to choose from for Immunization through the PCE Table Maintenance Menu. To help define the Immunization list, check with your Coordinator.

*Steps to add an Immunization*1. Select UE from the PCE Appointment List screen.2. Select IM from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEoutpatient,two 000-00-0002 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEprovider,one PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit//im Immunization \[ENTER\]

--- Immunization ---

Patient's Service Connection and Rated Disabilities:SC Percent: 100%Rated Disabilities: 5010 TRAUMATIC ARTHRITIS (10%-SC)7913 DIABETES MELLITUS (0%-SC)3. Respond to the following prompts for the immunization, as appropriate.

Immunization: TETANUS DIPTHERIA (TD-ADULT) \[ENTER\]

Encounter Provider: PCEprovider,one // ST.PETE (PHYSICIAN) PO 045A \[ENTER\]

Series: BOOSTER// BOOSTER \[ENTER\]

Reaction: FEVER// FEVER \[ENTER\]

Repeat Contraindicated: NO//\[ENTER\] NO (OK TO USE IN THE FUTURE)

Administered Date and (optional) Time: (8/18/2004 - 10/17/2004): 09172004 \[ENTER\] (SEP

17, 2004)

Comments: TESTING CIDC \[ENTER\]

Diagnosis: 276.6 \[ENTER\] FLUID OVERLOAD (w C/C)

Provider Narrative: \[ENTER\]

FLUID OVERLOAD DISORDER

Diagnosis Modifier: \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? YES \<- Response automated\*

Was treatment related to Combat? YES// \[ENTER\]

Was treatment related to Agent Orange Exposure? NO// \[ENTER\]

Was treatment related to Ionizing Radiation Exposure? NO// \[ENTER\]

Was treatment related to Environmental Contaminant Exposure? NO//\[ENTER\]

Was treatment related to Military Sexual Trauma? NO// \[ENTER\]

Was treatment related to Head and/or Neck Cancer? YES// \[ENTER\]Diagnosis 2:*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*4. The edited screen is then displayed.  

#### How to Add or Edit a Patient Ed

When you choose Patient Ed under Update Encounter, you will be prompted to enter the Education Topic, Level of Understanding, Encounter Provider, and Comments.

> **NOTE:** A Clinical Coordinator can change the items or categories available to choose from for Patient Ed through the PCE Table Maintenance Menu. If you wish to help define the Patient Education list, check with your Coordinator.

*Steps to add Patient Ed*1. Select UE from the PCE Appointment List screen.2. Select PE from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// PE Patient Ed

3. Respond to the following prompts for Patient Education.

Education Topic: Followup

Level of Understanding: 3 GOOD

Encounter Provider: PCEPROVIDER,ONE// \[ENTER\]

Comments: \[ENTER\]4. The edited screen is then displayed.

#### How to Add or Edit a Skin Test

When you choose Skin Test under Update Encounter, you will also be prompted to enter the Topic, Level of Understanding, and Encounter Provider.

When a Skin Test is entered, the user will be prompted for diagnoses which are associated with the mapped CPT code. If the diagnoses have not already appeared in the encounter, the user will be prompted for additional information to qualify the diagnosis such as modifiers, comments, and SC/EI classifications.

> **NOTE:** A Clinical Coordinator can change the items or categories available to choose from for Skin Tests through the PCE Table Maintenance Menu. If you wish to help define the Skin Test list, check with your Coordinator.

*Steps to add a Skin Test*1. Select UE from the PCE Appointment List screen.2. Select ST from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:99:21 Page: 1 of 1</u>

PCEoutpatient,two 000-00-0002 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEprovider,one PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// ST Skin Test \[ENTER\]  
3. Respond to the following prompts for Skin Tests, as appropriate.

--- Skin Test ---

1 CANDIDA

Enter 1-1 to Edit, or 'A' to Add: A \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 100%

Rated Disabilities: 5010 TRAUMATIC ARTHRITIS (10%-SC)

7913 DIABETES MELLITUS (0%-SC)

Skin Test: PPD \[ENTER\]

Reading in mm: N \[ENTER\]

Results: NEGATIVE \[ENTER\]

Administered Date and (optional) Time: (8/18/2004 - 10/17/2004): 09172004 \[ENTER\] (SEP

17, 2004)

Reading Date and (optional) Time: (8/18/2004 - 11/16/2004): 11162004 \[ENTER\] (NOV 16,

2004\)

Reader: PCEprovider,one \[ENTER\] ST.PETE (PHYSICIAN) PO 099A

Comments: Enter comments \[ENTER\]

Diagnosis: SKIN \[ENTER\]

1 SKIN 102.2 EARLY SKIN YAWS NEC

2 SKIN 112.3 CUTANEOUS CANDIDIASIS

3 SKIN 172.1 MALIG MELANOMA EYELID

4 SKIN 172.2 MALIG MELANOMA EAR

5 SKIN 172.3 MAL MELANOM FACE NEC/NOS

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 \[ENTER\] 102.2 EARLY SKIN YAWS NEC

Provider Narrative: \[ENTER\]

OTHER EARLY SKIN LESIONS OF YAWS

Diagnosis Modifier: \[ENTER\]

Patient's Service Connection and Rated Disabilities:

SC Percent: 80%

Rated Disabilities: 6013 GLAUCOMA (10%-SC)

5224 LOSS OF MOTION OF THUMB (10%-SC)

6100 IMPAIRED HEARING (25%-SC)

6260 TINNITUS (20%-SC)

5284 RESIDUALS OF FOOT INJURY (10%-SC)

5209 ELBOW CONDITION (10%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? YES \<- Response automated\*

Was treatment related to Combat? YES// \[ENTER\]

Was treatment related to Agent Orange Exposure? NO// \[ENTER\]

Was treatment related to Ionizing Radiation Exposure? NO// \[ENTER\]

Was treatment related to Environmental Contaminant Exposure? NO//\[ENTER\]

Was treatment related to Military Sexual Trauma? NO// \[ENTER\]

Was treatment related to Head and/or Neck Cancer? YES// \[ENTER\]

Diagnosis 2:

*\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*

#### How to Add or Edit an Exam

When you choose Exam under Update Encounter, you will also be prompted to enter the Topic, Level of Understanding, and Encounter Provider.

> **NOTE:** A Clinical Coordinator can change the items or categories available to choose from for Exams through the PCE Table Maintenance Menu. If you wish to help define the Exam list, check with your Coordinator.

*Steps to add an Exam*1. Select UE, from the PCE Appointment List screen.2. Select XA from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// XA Exam

3. Respond to the following prompts for Exams, as appropriate.

Exam: GENERAL EXAM

Results: ?

Choose from:

A ABNORMAL

N NORMAL

Results: NORMAL

Encounter Provider: PCEPROVIDER,TEN//\[ENTER\] PCEPROVIDER,TEN TP

Comments: \[ENTER\]

Exam: \[ENTER\]

4. The edited screen is then displayed.

#### How to Add or Edit Health Factors

When you choose Health Factors under Update Encounter, you will also be prompted to enter the Level/Severity and comments.

> **NOTE:** A Clinical Coordinator can change the items to choose from for Health Factors through the PCE Table Maintenance Menu. If you wish to help define the Health Factor list, check with your Coordinator.

*Steps to add a Health Factor*1. Select UE from the PCE Appointment List screen.2. Select HF from the PCE Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 08:24:21 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY ATTENDING

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// HF Health Factors

  
3. Respond to the following prompts for the Health Factor, as appropriate.

Health Factor: current smoker

Level/Severity: ?

Choose from:

M MINIMAL

MO MODERATE

H HEAVY/SEVERE

Level/Severity: hEAVY/SEVERE

Comments: Trying to quit

Health Factor: \[ENTER\]4. The edited screen is then displayed.

### How to Add or Edit the Checkout Interview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "Checkout Interview" which is done for all outpatients through the Scheduling package, can now also be done through PCE. You are prompted to enter Provider (and to designate if Primary Provider), Service-connection status\* (CPT codes, Diagnosis, etc. You may also designate if the Diagnosis should be added to the patient's Problem List.

*\*You will be prompted to enter Service-connection status within PCE Encounter Data Entry-Supervisor option ONLY.*

REMEMBER: Entering one or two question marks will provide help (including lists of acceptable CPT codes, Diagnoses) on how to respond to prompts. With functionality put in place by the Code Set Versioning project, only ICD and CPT Codes that are active for the encounter date and time will be available.

*Steps to add a Checkout Interview:*1. Select Checkout Interview from the Encounter or Appointment List screen or from the Update Encounter screen.

<u>PCE Update Encounter Jul 25, 1996 09:22:42 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY

<u>1 Encounter Date and Time: JUL 22, 1996@11:08:14</u>

2 Provider: PCEPROVIDER,ONE PRIMARY

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

Primary/Secondary Diagnosis: PRIMARY

4 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

5 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// IN Check Out Interview

2. Confirm or edit the checkout date and service-connection status.

--- Classification --- \[Required\]

Was treatment for SC Condition? YES \<- Response automated\\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*  
3. Enter the provider associated with the procedure performed during this encounter. (You can enter more than one provider and more than one procedure for each provider.)

PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY

\- - E N C O U N T E R P R O V I D E R S - -

No. PROVIDER

No PROVIDERS for this Encounter.

Enter PROVIDER: PCEPROVIDER,ONE

Is this the PRIMARY provider for this ENCOUNTER? YES// \[ENTER\]

<u>PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY</u>

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

Previous Entry: PCEPROVIDER,ONE

\- - E N C O U N T E R P R O V I D E R S - -

No. PROVIDER

1 PCEPROVIDER,ONE\* PRIMARY

Enter PROVIDER: \[ENTER\]

4. Enter the ICD code or Diagnosis and whether you want it added to the Problem List.

<u>PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY</u>

<u>ICD CODE: V70.3 --MED EXAM NEC-ADMIN PURP PRIMARY</u>

\- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -

<u>No. ICD DESCRIPTION PROBLEM LIST</u>

No DIAGNOSIS for this Encounter.

Enter Diagnosis : V70.3--MED EXAM NEC-ADMIN PURP

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES// \[ENTER\]

<u>PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY</u>

<u>ICD CODE: ...There is 1 PROVIDER associated with this encounter.</u>

Previous Entry: V70.3

\- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -

<u>No. ICD DESCRIPTION PROBLEM LIST</u>

1 V70.3\* MED EXAM NEC-ADMIN PURP PRIMARY

Enter NEXT Diagnosis :210

<u>PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY</u>

<u>ICD CODE: ...There is 1 PROVIDER associated with this encounter.</u>

Previous Entry: V70.3

<u>ITEM CODE DESCRIPTION 10 MATCHES</u>

1 210.0 BENIGN NEOPLASM OF LIP

2 210.1 BENIGN NEOPLASM OF TONGUE

3 210.2 BENIGN NEOPLASM OF MAJOR SALIVARY GLANDS

4 210.3 BENIGN NEOPLASM OF FLOOR OF MOUTH

5 210.4 BENIGN NEOPLASM OF OTHER AND UNSPECIFIED PARTS OF MOUTH

6 210.5 BENIGN NEOPLASM OF TONSIL

7 210.6 BENIGN NEOPLASM OF OTHER PARTS OF OROPHARYNX

8 210.7 BENIGN NEOPLASM OF NASOPHARYNX

9 210.8 BENIGN NEOPLASM OF HYPOPHARYNX

10 210.9 BENIGN NEOPLASM OF PHARYNX, UNSPECIFIED

Select a single 'ITEM NUMBER' or 'RETURN' to exit: 6

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES// NO

<u>PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY</u>

<u>ICD CODE: ...There is 1 PROVIDER associated with this encounter.</u>

Previous Entry: 210.5

\- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -

No. ICD DESCRIPTION PROBLEM LIST

1 210.5\* BENIGN NEOPLASM TONSIL

2 V70.3\* MED EXAM NEC-ADMIN PURP YES

Enter NEXT Diagnosis: \[ENTER\]

Would you like to add any Diagnoses to the Problem List? NO// YES

Select 1 or several Diagnoses (eg 1,3,4,7,3-6,2-5): 1,2

Enter PROVIDER associated with PROBLEM: PCEPROVIDER,ONE // \[ENTER\]

Select one of the following:

O ORDERING

R RESULTING

OR BOTH O&R

Is this Diagnosis Ordering or Resulting:: BOTH O&R//

Patient's Service Connection and Rated Disabilities:

SC Percent: 10%

Rated Disabilities: 6260 TINNITUS (10%-SC)

6100 IMPAIRED HEARING (0%-SC)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO \<- Response automated\\*Response will NOT be automated within the PCE Encounter Data Entry-Supervisor option, it will be defaulted and user can edit it.*5. Enter the Procedure (CPT code or procedure name).

You can enter the CPT code or CPT Category or description. A '\*' next to a procedure indicates that it was either added or edited during this session. You can also remove an existing CPT code for this encounter by entering 0 or @.

PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY

<u>- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -</u>

<u>No. CPT CODE QUANTITY DESCRIPTION PROVIDER</u>

No CPT CODES for this Encounter.

Enter PROCEDURE (CPT CODE): 25066 BIOPSY FOREARM SOFT TISSUES

6. Enter the modifiers and the number of times the procedure was administered.

Select CPT MODIFIER: 22 UNUSUAL PROCEDURAL SERVICES

How many times was this procedure performed: 1// \[ENTER\]

Enter PROVIDER associated with PROCEDURE: PCEPROVIDER,ONE // \[ENTER\]

The prompts will then recycle through PROCEDURE and PROVIDER to allow you to enter more, if necessary. Press ENTER to bypass these prompts when you don't wish to add more.

PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 22, 1996@11:08:14 CARDIOLOGY

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT: ...There is 1 PROCEDURE associated with this encounter.

\- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

<u>No. CPT CODE QUANTITY DESCRIPTION PROVIDER</u>

1 25066\* 1 BIOPSY FOREARM SOFT TISSUES PCEPROVIDER,ONE

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

Enter NEXT PROCEDURE (CPT CODE): \[ENTER\]

7. The Update Encounter screen is then redisplayed with the Checkout Interview information.

<u>PCE Update Encounter Jul 25, 1996 10:06:59 Page: 1 of 1</u>

PCEPATIENT,ONE 000-45-6789 Clinic: CARDIOLOGY

<u>Encounter Date 07/22/96 11:08 Clinic Stop: 303 CARDIOLOGY</u>

1 Encounter Date and Time: JUL 22, 1996@11:08:14

2 Provider: PCEPROVIDER,ONE PRIMARY

3 ICD9 Code or Diagnosis: V70.3 MED EXAM NEC-ADMIN PURP

Provider Narrative: OTHER GENERAL MEDICAL EXAMINATION FOR

ADMINISTRATIVE PURPOSES

4 ICD9 Code or Diagnosis: 210.5 BENIGN NEOPLASM TONSIL

Provider Narrative: BENIGN NEOPLASM OF TONSIL

Primary/Secondary Diagnosis: PRIMARY

5 CPT Code: 25066 BIOPSY FOREARM SOFT TISSUES

CPT Modifier: 22 UNUSUAL PROCEDURAL SERVICES

6 Education Topic: VA-TOBACCO USE SCREENING

+ Next Screen - Prev Screen ?? More Actions

ED Edit an Item TR Treatment DD Display Detail

DE Delete an Item IM Immunization DB Display Brief

EN Encounter PE Patient Ed IN Check Out Interview

PR Provider ST Skin Test QU Quit

DX Diagnosis (ICD 9) XA Exam

CP CPT (Procedure) HF Health Factors

Select Action: Quit// \[ENTER\]

### Adding or Editing Directions to Patient's Home

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Directions to Patient's Home Add/Edit option lets you enter directions to a patient's home, which can then be displayed on a Health Summary.

This feature is especially useful for Hospital-Based Home Care staff.

*Steps to add directions to patient's home:*1. Choose HOME from the main PCE menu.2. Select a patient name.3. If no directions have already been entered, type in free text at the prompt.NOTE: The screen editor you use in all your work will determine how you enter text.

Select PCE Coordinator Menu Option: home Directions to Patient's Home Add/Edit

Select PATIENT NAME: PCEPATIENT

1 PCEPATIENT,ONE 06-04-08 000456789 NON-VETERAN (OTHER)

2 PCEPATIENT,TWO 02-16-33 666000000 NSC VETERAN

CHOOSE 1-2: 1 PCEPATIENT,ONE 06-04-08 000456789 NON-VETERAN (OTHER)

LOCATION OF HOME:

1\>On the dock.

2\>

EDIT Option:\[ENTER\]

Select PATIENT NAME:\[ENTER\]4.To edit directions that were previously entered, select the edit option and proceed to edit according to the screen editor process you normally use.

Select PCE Coordinator Menu Option: home Directions to Patient's Home Add/Edit

Select PATIENT NAME: PCEPATIENT,EIGHT PCEPATIENT,EIGHT 09-12-44 666777888 SC VETERAN

LOCATION OF HOME:. . .

6\> WIER STREET. TURN LEFT ON WEIR STREET AND GO TO END.

7\> TO THE LEFT OF THE DEADEND IS A DIRT PATH.

8\> FOLLOW THIS PATH 1/4 MILES UNTIL YOU REACH A WHITE HOUSE.

EDIT Option: 8

REPLACE: WHITE WITH: GREEN REPLACE: \[ENTER\]

EDIT Option: \[ENTER\]

Select PATIENT NAME: \[ENTER\]Key Concepts

- Clinicians can add individual types of data (immunizations, patient education) through the PCE user interface.
- Clerks can add encounter form data that was incorrectly scanned or was missing.
- The equals sign (=) can be used as a shortcut when selecting an action plus encounters or appointments from a list (e.g., Select Action: ED=2).
- Information added to PCE can be viewed on the Health Summary or on PCE Clinical Reports.
- Information added to PCE can be used to generate clinical reminders that will appear on a patient's Health Summary.
- Each site can modify the choices available in PCE files for health factors, immunizations, patient education, etc.
- You can enter encounter information for an inexact time in the past or from another site through Make Historical Enc.
- Information entered through the Checkout Interview goes into the Scheduling package. The Checkout Interview information can also be entered directly through the Scheduling package. The dialogues, screens and resulting data are identical between the two packages.

# PCE and Health Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information such as Patient Education, Health Factors, and Immunizations, as well as clinical reminders about when these things are due, can be displayed on Health Summaries. Health Summary has special components designed to include these elements. See PCE Clinical Reports in this manual for setting up Clinical Reminders to appear on Health Summaries. An example of Health Summary with PCE components appears on the next page.

08/06/96 14:38

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CONFIDENTIAL PCE COMPONENTS SUMMARY \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PCEPATIENT,ONE 000-45-6789 DOB: 04/01/44

-------------------------- BDEM - Brief Demographics -------------------------------

Address: 321 S 3400 E Phone:

SALT LAKE CITY, UTAH 84105

Eligibility: SC LESS THAN 50% Age: 52

Sex: FEMALE

--------------------------- CR - Clinical Reminders --------------------------------

--NEXT-- --LAST--

Patient Education - Smoking DUE NOW unknown

Mammogram DUE NOW 8/94

-------------------------- OE - Outpatient Encounter -------------------------------

08/01/96 SALT LAKE DIABETES CLINIC SC LESS THAN 50%

Provider: PCEPROVIDER,ONE (S) PCEPROVIDER,TWO (S) PCEPROVIDER,SIX (S)

PCEPROVIDER,NINE (S)

Diagnosis: 309.81-PROLONG POSTTRAUM STRESS; EYE PROBLEM

371.53-GRANULAR CORNEA DYSTRPHY; narrative for diagnosis/problem

Procedure: 99212-OFFICE/OUTPATIENT VISIT, EST; Limited Exam (6-10 Min)

02/31/96 SALT LAKE CARDIOLOGY SC LESS THAN 50%

Provider: PCEPROVIDER,ONE (P)

Diagnosis: 334.0-FRIEDREICH'S ATAXIA

Procedure: 33200-INSERTION OF HEART PACEMAKER

----------------------------- IM - Immunizations -----------------------------------

PNEUMO-VAC B 06/10/96 SALT LAKE FEVER; DO NOT REPEAT

SABIN/OPV 1 04/22/96 SALT LAKE

--------------------- EDL - Education Latest (max 1 year) --------------------------

08/01/96 SALT LAKE VA-SUBSTANCE ABUSE - REFUSED

06/10/96 SALT LAKE VA-DIABETES MEDICATIONS - GOOD UNDERSTANDING

---------------------- EXAM - Exams Latest (max 1 year) ----------------------------

ABDOMEN EXAM 06/10/96 ABNORMAL SALT LAKE

GENERAL EXAM 08/01/96 NORMAL SALT LAKE

ORTHO EXAM 05/13/96 ABNORMAL SALT LAKE

-------------- HF - Health Factors (max 1 occurrence or 1 year) --------------------

TOBACCO

TOBACCO USER (HEAVY/SEVERE) 08/01/96

\* END \*

Press \<RET\> to continue, ^ to exit, or select component:

# Managing PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff and Clinical Coordinators manage PCE by assigning menus, setting site parameters, defining clinical reminders, setting up clinical reports, and modifying local tables containing patient education, health factors, and other items through the Table Maintenance options.

## PCE Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menus and options are exported with PCE:

### PCE IRM Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SP PCE Site Parameters Menu ...

TBL PCE Table Maintenance ...

INFO PCE Information Only ...

RM PCE Reminder Maintenance Menu ...

CR PCE Clinical Reports ...

HOME Directions to Patient's Home Add/Edit

CO PCE Coordinator Menu ...

CL PCE Clinician Menu

- Assign the *IRM Main Menu* or at least the first four options/menus to IRM staff or coordinators who will be responsible for setting up PCE, maintaining the entries in the PCE tables (such as Patient Education, Immunization, Treatments, etc.), and defining the clinical reminders/maintenance system for your site.
- Assign the *PCE Coordinator Menu* to the Application Coordinator who will use all of the PCE options.
- Assign the *PCE Clinician Menu* to clinicians who will be entering or editing data, who will use clinical reports, who need the PCE Information Only menu to see the basis for reminders, and who might add or edit directions to a patient's home for appearance on a health summary.
- Assign *Directions to Patient's Home Add/Edit* to anyone who needs to enter directions to a patient's home. This is especially useful for Hospital-Based Home Care staff (directions can be viewed on Health Summaries).

### PCE Coordinator Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE Coordinator Menu includes all of the user interface options as well as the options for file maintenance.

SUP PCE Encounter Data Entry - Supervisor

PCE PCE Encounter Data Entry

DEL PCE Encounter Data Entry and Delete

NOD PCE Encounter Data Entry without Delete

TBL PCE Table Maintenance ...

INFO PCE Information Only ...

ACT Activate/Inactivate Table Items ...

CED Education Topic Copy

DEWO PCE Delete Encounters W/O Visit

ED Education Topic Add/Edit

EX Examinations Add/Edit

HF Health Factors Add/Edit

IM Immunizations Add/Edit

SK Skin Tests Add/Edit

TR Treatments Add/Edit

INFO PCE Information Only ...

EDA Active Educ. Topic List - Detailed

EDL Education Topic List

EDI Education Topic Inquiry

EX Exam List

HF Health Factor List

IM Immunization List

SK Skin Test List

TR Treatment List

REPT PCE Clinical Reports ...

HOME Directions to Patient's Home Add/Edit

PARM PCE HS/RPT Parameter Menu ...

DIE PCE Device Interface Error Report

DISP PCE Edit Disposition Clinics

- Assign *Assign PCE Encounter Data Entry - Supervisor* to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries. This option also allows, contrary to all other PXCE Encounter Data Entry, users to display, and even modify ancillary encounters so it should be assigned with caution*.*
- Assign *PCE Encounter Data Entry* to data entry staff who can document a clinical encounter and who can delete their own entries.
- Assign *PCE Encounter Date Entry and Delete* to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries.
- Assign *PCE Encounter Data Entry without Delete* to users who can document a clinical encounter , but should not be able to delete any entries, including ones that they have created.

### ### ### ### Key Concepts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PCE menus and options are designed for two main types of users: 1) end users (clinicians and clerks) and 2) managers and coordinators.
- The end user options included data entry options and clinical reports.
- The manager and coordinator options include the maintenance menus and the site parameters set-up option.

## PCE Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE Site Parameters Menu on the PCE IRM Main Menu contains the *PCE HS/RPT Parameter menu, PCE Edit Disposition Clinics,* and *PCE Site Parameters Edit*.

PCE Site Parameters Menu

SITE PCE Site Parameters Edit

RPT PCE HS/RPT Parameter Menu ...

PRNT PCE HS/RPT Parameters Print

HS PCE HS Disclaimer Edit

RPT PCE Report Parameter Edit

DISP PCE Edit Disposition Clinics

*Option Descriptions*

PCE Site Parameters Edit

This option is used to edit entries in the PCE PARAMETERS file. The parameters that are set are used as the default controls for the user interface when it starts up. You can set your default view as Appointment or Encounter, and a range of dates.

PCE HS Disclaimer Edit

This option is used to specify a Site Reminder Disclaimer to be used by the Health Summary package whenever the Health Summary "Clinical Maintenance" and "Clinical Reminder" components are displayed in a Health Summary.

PCE HS/RPT Parameters Print

This option prints the current PCE Parameter definitions that are used by Health Summary and some of the PCE Reports.

PCE Report Parameter Edit

This option is used to define parameters that will be used by the PCE Report Module. The report edit option allows your site to specify which clinics in file 44 represent "Emergency Room" clinics, and what Lab tests from file 60 should be used for looking up patient data for Glucose, Cholesterol, LDL Cholesterol and HBA1C lab results. These fields are used by the reports Caseload Profile by Clinic, and Patient Activity by Clinic. To get a printout of current definitions in the PCE Parameters fields for these fields, use the PCE HS/RPT Parameters Print.

PCE Edit Disposition Clinics

This option is used to define which clinics are used as Administrative Dispositon Clinics.

## PCE HS/RPT Parameter Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE HS/RPT Parameter menu contains print and edit options for PCE fields related to the Health Summary package and PCE Reports module.

Use the print option to see what the current definition is for these fields.

PCE exports a disclaimer to appear on Health Summaries: Default Reminder Disclaimer:

The following disease screening, immunization, and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The appropriate utilization of these for your individual patients must be based on clinical judgment and the patient's current status.

If your site prefers to use a site-defined reminder disclaimer instead of the disclaimer distributed by PCE, use the HS Disclaimer Edit option to define your site's disclaimer text. This disclaimer will appear on the top of each display of Health Summary "Clinical Maintenance" and "Clinical Reminder" components.

Two PCE Clinical Reports*Caseload Profile by Clinic* and *Patient Activity by Clinic*track Critical Lab Values and Emergency Room Visits. The *PCE Report Parameter Edit* option allows your site to specify which clinics in Hospital Location file (#44) represent "Emergency Room" clinics and what tests from the Laboratory Test file (#60) should be used for looking up patient data for Glucose, Cholesterol, LDL Cholesterol and HBA1C lab results. (This is necessary since the Laboratory Test File is not standardized and each site may have customized it differently.)

## PCE Site Parameters Edit Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parameters that are set through this option are used as the default controls for the user interface when it starts up.

SITE PCE Site Parameters Edit

RPT PCE HS/RPT Parameter Menu ...

Select PCE Site Parameter Menu Option: site PCE Site Parameters Edit

Select PCE PARAMETERS ONE: 1

STARTUP VIEW: APPOINTMENT// ??

This is the default list that PCE Encounter Data Entry starts in for all

users.

Choose from:

V VISIT/ENCOUNTER

A APPOINTMENT

STARTUP VIEW: APPOINTMENT// v VISIT/ENCOUNTER

BEGINNING PATIENT DATE OFFSET: -30// \[ENTER\]

ENDING PATIENT DATE OFFSET: 2// \[ENTER\]

BEGINNING HOS LOC DATE OFFSET: -14// -30

ENDING HOS LOC DATE OFFSET: 2// \[ENTER\]

RETURN WARNINGS: YES// ?

Enter YES if you want the Device Interface to return warnings if there

are no diagnoses or procedures passed.

Choose from:

0 NO

1 YES

RETURN WARNINGS: YES// \[ENTER\]

Select PCE PARAMETERS ONE: \[ENTER\]PCE Edit Disposition Clinics

This option is used to define which clinics are used as Administrative Dispositon Clinics.

Select PCE Site Parameter Menu Option: PCE Edit Disposition Clinics

Select PCE PARAMETERS ONE: 1

Select DISPOSITION HOSPITAL LOCATIONS: 3A

Are you adding '3A' as

a new DISPOSITION HOSPITAL LOCATIONS (the 1ST for this PCE PARAMETERS)? Y Select DISPOSITION HOSPITAL LOCATIONS: \[ENTER\]

Select PCE PARAMETERS ONE: \[ENTER\]

  
Key Concepts

- Coordinators can set the parameters that are used as the default controls for the user interface when it starts up. You can set your default view as Appointment or Encounter, and also a range of dates.
- Coordinators can specify which clinics in file 44 represent "Emergency Room" clinics, and what Lab tests from file 60 should be used for looking up patient data for Glucose, Cholesterol, LDL Cholesterol and HBA1C lab results.
- PCE exports a disclaimer to appear on Health Summaries, stating that clinicians may use their professional discretion as to how they respond to clinical reminders. Each site may create a site-defined reminder disclaimer, using the HS Disclaimer Edit option. This disclaimer will appear on the top of each display of Health Summary "Clinical Maintenance" and "Clinical Reminder" components.

## ## Table Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Table Maintenance options let sites add or edit the items in the tables for Health Factors, Patient Education, Immunizations, Skin Tests, etc.

PCE Table Maintenance Menu

INFO PCE Information Only ...

ACT Activate/Inactivate Table Items ...

CED Education Topic Copy

DEWO PCE Delete Encounters W/O Visit

ED Education Topic Add/Edit

EX Examinations Add/Edit

HF Health Factors Add/Edit

IM Immunizations Add/Edit

SK Skin Tests Add/Edit

TR Treatments Add/Edit

Once these tables have been defined, the table entries will be selectable for encounter data entry (directly into PCE) or for encounter form definitions (AICS package). The patient information collected can be viewed on Health Summaries.

Use the "Inactive Flag" field to make an entry "INACTIVE" for selection in the encounter form definition process and the PCE encounter data entry process. If entries are to be included on the clinic's encounter form, the entries must first be defined in the appropriate file using this option. canning encounter forms with the AICS package will provide PCE with information stored in the V files.

These options may be used in conjunction with the "PCE Information Only" menu options to manage the contents of the files or tables supporting the Patient Care Encounter (PCE) package.

*Option Descriptions*

PCE Information Only

This is a menu of options that lists entries in the files/tables for patient education,

immunizations, skin tests, health factors and treatments.

Activate/Inactivate Table Items

This option is the main menu option that allows you to activate or inactivate the entries in the supporting tables. (e.g., Immunizations, Skin Tests, Education Topics)

Education Topic Copy

This option allows the user to copy an existing education topic into a new education topic entry in the Education Topics file (#9999999.09). The original education topic to be copied is selected first. If the topic is prefixed with "VA-", the "VA-" will be stripped off the name automatically. The new name must be unique. If the name is not unique, the user must enter a unique name for the new education topic.

PCE Delete Encounters W/O Visit

This option provides a tool for IRM to correct Encounters that have missing Visits. The missing Visits can cause a problem where the Encounters cannot be checked out. Under this menu option, there are 4 sub options described in detail in the text of patch PX\*1\*153:

BUILD will find the missing encounters based on date range entries,

REPORT will print the problem encounters per build,

FIX ALL will fix all the encounters that are indicated by the build, and

FIX INDIVIDUAL will fix encounters for one patient.

Education Topic Add/Edit

This option lets you create a new Education Topic or edit an Education Topic that was originally created at your site. Education topics distributed with the PCE package can be inactivated using the PCE "Activate/Inactivate Table Items" menu. Once an education topic is defined in this table, it should not be deleted if there are any encounter form definitions which are referencing the education topic, or if there is any patient encounter data which is referencing this education topic historically.

Examinations Add/Edit

This option allows you to create a new name to represent an examination type or edit an examination type that was originally created at your site. The examination types originally distributed by PCE are a breakdown of potential categories of exams within a Physical Exam. The exams distributed with the PCE package can be inactivated using the PCE "Activate/Inactivate Table Items" menu. Once exam names are defined in this table, they should not be deleted if there are any encounter form definitions referencing the exam name, or if there is any patient encounter data which may be referencing this exam historically.

Health Factors Add/Edit

This option allows the user to create a new Health Factor or edit a Health Factor that was originally created at your site. Health factors that are distributed with the PCE package can be inactivated using the PCE "Activate/Inactivate Table Items" menu. Once a health factor is defined in this table, it should not be deleted if there are any encounter form definitions which may be using the term, or if there is any patient encounter data which may be referencing this term historically.

Immunizations Add/Edit

This option allows a user to create a new Immunization type or edit an existing Immunization type that was originally created at your site. Immunizations that are distributed with the PCE package can be inactivated using the PCE "Activate/Inactivate Table Items" menu. Once an immunization is defined in this table, it should not be deleted if there are any encounter form definitions which may be referencing the immunization, or if there is any patient encounter data which may be referencing this term historically.

Skin Tests Add/Edit'

This option allows a user to create a new Skin Test table entry or edit a Skin Test table entry that was originally created at your site. Skin tests that are distributed with the PCE package can be inactivated using the PCE "Activate/ Inactivate Table Items" menu. Once a skin test is defined in this table, it should not be deleted if there are any encounter form definitions which may be referencing the skin test, or if there is any patient encounter data which may be referencing this skin test historically.

Treatments Add/Edit

This option allows a user to create a new Treatment or edit a Treatment that was originally created at your site. Treatments that are distributed with the PCE package can be inactivated using the PCE "Activate/Inactivate TAble Items" menu. Once a treatment is defined in this table, it should not be deleted if there are any encounter form defintions which may be referencing the treatment, or if there is any patient encounter data which may be referencing the treatment historically. .

### Editing the Education Topic file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select PCE Table Maintenance Option: PE Education Topic Add/Edit

Select Patient Education Option: ?

A Activate or Deactivate Topics

E Edit ONLY Active Topics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Patient Education Option: E Edit ONLY Active Topics

Select EDUCATION TOPICS NAME: SAMPLE 1 - LIFESTYLE ADAPTATIONS

NAME: SAMPLE 1 - LIFESTYLE ADAPTATIONS Replace

MNEMONIC: ??

answer must be 1-9 characters in length and must contain a "-" (ie

VA-DIET).

MNEMONIC: VA-DI

INACTIVE: ?

Choose from:

1 INACTIVE

INACTIVE:

PRINT NAME: A/S Lifestyle Adaptations Replace \[ENTER\]

Select ITEM: ?

Answer with ITEM

You may enter a new ITEM, if you wish Select an item which

represents a component of the education topic.

Answer with EDUCATION TOPICS NAME, or MNEMONIC

Key Concepts

- Coordinators add or edit the items in the tables for Health Factors, Patient Education, Immunizations, Skin Tests, etc.
- Entries in these tables can be selected when clinicians or clerks enter encounter data such as health factors or patient education.
- When coordinators or MCCR personnel create encounter forms through the AICS package, they can use entries from these tables as items to be checked off.
- The patient information collected based on these table definitions can be seen on Health Summaries.
- This menu also includes options to edit the Clinical Reminder/ Health Maintenance definitions, based on your site's clinical terminology in the tables. Once reminder criteria have been defined, they may be included in the Health Summary Type definitions for the "Clinical Reminder" and "Health Maintenance" Components.

## PCE Information Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a menu of options that lists entries in the files/tables for patient education, immunizations, skin tests, health factors and treatments.

PCE Information Only Menu

EDA Active Educ. Topic List - Detailed

EDL Education Topic List

EDI Education Topic Inquiry

EX Exam List

HF Health Factor List

IM Immunization List

SK Skin Test List

TR Treatment List

CM PCE Code Mapping List

These entries determine what clinical data will be collectable for these classes of clinical data.

PCE distributes immunizations and skin test table entries that also have a related CPT code. The relationship of an immunization or skin test to a CPT code is defined in the PCE Code Mapping file. The PCE Code Mapping file determines whether two entries should be made from one clinical data item entered. For example, if an immunization is entered into the V Immunization file, a CPT code is generated in the V CPT file for billing and workload. The mapping definition of the CPT relationship with the Immunization type is viewable from the PCE Code Mapping list option.

  
*Option Descriptions*

Active Educ. Topic List - Detailed

This lists the current detailed definition of the goals and standards defined for the active education topics.

Education Topic List

This option prints a brief list of ALL Education Topics using only two fields: Inactive Flag status and Topic Name.

Education Topic Inquiry

This option can be used to print the definition of a specific Education Topic definition.

Exam List

This option lists all of the exam names, with their Active Status, that are defined in the Exam file for use with PCE.

Health Factor List

This option lists the Health Factors by Category, with their Active Status, that have been defined in the Health Factor file for use with PCE.

Immunization List

This option lists all immunizations, with their Active Status, which have been defined in the Immunization file for use with PCE. NOTE: To see what CPT codes may be related to the immunization entries, print the PCE Code Mapping List.

Skin Test List

This option lists all skin tests, with their Active Status, that have been defined in the Skin Test file for use with PCE.

Treatment List

This option lists all treatments, with their active status, that have been defined in the Treatment file for use with PCE

PCE Code Mapping List

This option allows the user to see the mapping between CPT codes and a related entry in a PCE supporting file. For example, the CPT code 90732 is related to the Immunization file entry PNEUMOCCOCAL. PCE uses the code mapping relationships to populate multiple files from one data entry step. For example, an entry of PNEUMO-CCOCAL in the V Immunization file will also create a CPT entry, 90732 in the V CPT file which will then be passed to PIMS for use by IB, Workload, and DSS.

PCE Code Mapping List

PCE CODE MAPPING LIST MAY 24,1996 13:15 PAGE 1

ON/OFF

FROM FILE ENTRY TO RELATED SUPPORTING FILE ENTRY FLAG

-----------------------------------------------------------------------

CPT 86485 SK CANDIDA ON

CPT 86490 SK COCCI ON

CPT 86510 SK HISTOPLAS ON

CPT 86580 SK PPD ON

CPT 86585 SK TINE ON

CPT 90700 IMM DIP-TET-a/PERT ON

CPT 90701 IMM DIP.,PERT.,TET. (DPT) ON

CPT 90702 IMM DIPHTHERIA-TETANUS (DT-PEDS) ON

CPT 90703 IMM TETANUS TOXOID ON

CPT 90704 IMM MUMPS ON

CPT 90705 IMM MEASLES ON

CPT 90707 IMM MEASLES,MUMPS,RUBELLA (MMR) ON

CPT 90708 IMM MEASLES,RUBELLA (MR) ON

CPT 90709 IMM RUBELLA, MUMPS ON

Key Concepts

- Options on the Information Only menu list clinical terminology used in the PCE files/tables to represent patient education, immunizations, skin tests, health factors and treatments.

  The terminology in these tables determines what clinical data will be collectable for these classes of clinical data.
- The PCE Code Mapping List shows the mapping between CPT codes and related entries in other PCE supporting files. For example, if an immunization is entered into the V Immunization file, a CPT code is generated in the V CPT file for billing and workload.
- Options on this menu display definitions of PCE Reminders which may be selected for the PCE Clinical Reminder and PCE Clinical Maintenance components.

## clinical reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how you can use clinical reminders, along with related tools and technology, to help clinicians provide better patient care. It reviews the following:

- Relationships between PCE, encounter forms, health summaries, and clinical reminders.
- Encounters and encounter forms, along with the considerations you need to keep in mind when designing encounter forms.
- Health summaries
- Clinical reminders set-up
- Clinical reminders benefits

Overview*Where Does the Data for Reminders Come From?*

Clinical reminders depend upon patient clinical information collected from a variety of sources, using manual data entry, automated data capture tools, and/or ancillary service activities. The following table shows some of the sources of patient data for clinical reminders.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 51%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>User Source</strong></td>
<td><strong>Type of Data</strong></td>
<td><strong>Package</strong></td>
</tr>
<tr class="even">
<td><p>Checkout</p>
<p>Clerks</p></td>
<td><p>Encounter data on encounter form or Progress Note</p>
<p>Historical information noted on the encounter form</p></td>
<td><p>AICS, PCE, Scheduling</p>
<p>PCE</p></td>
</tr>
<tr class="odd">
<td>Practitioners</td>
<td><p>Encounter data on encounter form</p>
<p>Historical information</p>
<p>Vitals</p>
<p>Text notes are not usable directly by the reminders, but clinical reminders can make use of coded data extracted and manually entered</p></td>
<td><p>AICS, PCE</p>
<p>PCE</p>
<p>Vitals</p>
<p>Progress Notes, Discharge Summary or TIU</p></td>
</tr>
<tr class="even">
<td>Ward Clerks</td>
<td>Encounter data from Inpatient Stay</td>
<td>PIMS - ADT summary in PTF File</td>
</tr>
<tr class="odd">
<td>MCCR personnel</td>
<td>Data entered to complete an encounter for billing and workload credit</td>
<td>Scheduling, PCE</td>
</tr>
<tr class="even">
<td><p>Transcrip-</p>
<p>tionists</p></td>
<td>Transcribed text is not usable directly by the reminders, but clinical reminders can make us of coded data extracted and manually entered</td>
<td><p>Progress Notes - PCE</p>
<p>Radiology -PCE</p>
<p>Discharge Summaries - PCE and ADT</p>
<p>Cytopathology - PCE</p></td>
</tr>
<tr class="odd">
<td>Ancillary service practitioners</td>
<td>Record results from procedures and automatically update PCE upon verification of results.</td>
<td><p>Laboratory - PCE</p>
<p>Radiology - PCE</p>
<p>Surgery - PCE</p>
<p>Event Capture - PCE</p></td>
</tr>
</tbody>
</table>

*Manual Data Entry*

Manual data entry is one way to record patient care encounters. The data entered provides the when, why, what, and who information related to a patient encounter:

- Encounter location and date/time
- Diagnoses treated
- Procedures performed
- Practitioner(s)

Historical information about encounters can be entered using the *Encounter View* action in PCE data entry options to make the patient record more complete. Data capture requirements for historical data are minimal. The historical encounter data is not used for billing and workload. No provider is required and entering only a diagnosis or procedure is oka*y.* Immunizations, pap smears, mammograms, surgeries, etc., done elsewhere may now be recorded and used by the clinical reminders. This includes other VA Medical Centers and non-VA locations (Health Department, private office, etc.).

*Automated Data Capture*

Scanned encounter forms can be used to capture encounter data relevant to clinical reminders. If the reminders are to be accurate, the forms must capture the data they need.

It is a challenge to keep the forms as simple as possible while still meeting information capture requirements. This may be done by combining information such as immunizations and skin tests with other required preventive procedures and assigning appropriate CPT codes so they will be captured correctly.

There is no perfect encounter form. Everyone who uses these forms will have ideas about how to make them “perfect.” They need to be carefully designed to meet *most* of the users’ needs, while capturing information for workload and billing purposes. You can’t capture everything for everyone on one form.

*How do Clinical Reminders and Health Summary packages usethe data?*

Reminder items are added to health summary selection components for a given health summary type. When the health summary type is run, the Clinical Reminders software evaluates the patient’s data and returns the results to the health summary for display.

*Health Summary Reminder Components*

- *Clinical Reminder:* an abbreviated component indicating only what is due now.

> Name of reminder

> Date last done

> Date next due

> The clinical reminder displays on the health summary as follows:

> <u>Reminder Next Last Done</u>

> Mammogram 10/1/98 10/1/96

> Pap Smear Due Now Unknown

> Diabetic Eye Exam 10/1/98 10/1/97

- *Clinical Maintenance:* this component provides:

> 1\. Details about what was found from searching the *VIS*TA clinical data.

> 2\. Text related to the findings found or not found (as defined in the

> reminder). This includes taxonomies (ICD or CPT codes), health factors,

> and test results related to the reminder and computed findings (e.g., Body

> Mass Index).

> 3\. Final frequency and age range used for the reminder.

> The advantage of clinical maintenance over clinical reminders is that it

> includes related test results, health factors, and logic related to that

> reminder.

> Example of *clinical maintenance* as displayed on a health summary:

Reminder Next Last Done

Hemoglobin A1C 11/1/97 11/1/96

11/1/96 - Problem Diagnosis: 250-Diabetes

HbA1C required yearly for diabetic patients

11/1/96 Lab procedure: HbA1C; results 9.6%

Final frequency and age range used: 1 year for diabetic patients

Health summaries and reminder definitions can be tailored to suit clinicians’ needs. Some health summaries are defined by users themselves and some are designed for generic use. Many kinds of information can be displayed on a health summary. The user can define a reminder that is very detailed so that it could be used in place of a paper chart. Most sites use the health summary to supplement the paper chart, based on the clinic and provider’s preference for health summary content.

*Clinician’s Role in Clinical Reminders*

The clinician plays an important role in Clinical Reminders. He/she will be asked to assist the Clinical Coordinator in selecting which reminders to implement and in defining the clinical aspects of the Clinical Reminder Definition Worksheets, including:

- Baseline Age Findings
- Reminder Frequency
- Minimum and Maximum Age
- Health Factors, Taxonomies
- Related Lab and Radiology Tests
- Computed Findings.

Clinicians may also have clinical reminders customized for their needs.

The clinician also plays a major role by appropriately marking the reminder health topics on the encounter forms. As exams, tests, immunizations, screening, and education are given, the boxes must be marked so that the information can be entered into the computer by the clinician or clerk, or picked up by scanners and passed on to PCE to satisfy the clinical reminders.

*Historical encounters* can be entered for patient visits that occurred sometime in the past (exact time may be unknown) or at some other location (possibly non-VA). They are used to satisfy reminders and determine next date due.

Most important, clinicians will make use of clinical reminders and clinical maintenance to enhance patient care, by assuring timely completion of appropriate tests, immunizations, exams, screenings, and education.

*How does the Clinical Reminders software help to meet Clinical Guidelines, NCHP, performance indicators, and preventive medicine mandates?*

Make the most of your clinical reminders!

The National Center for Health Promotion (NCHP) has defined a set of 15 reminders that represent the minimum that sites must report on yearly to comply with Congressional law. The Ambulatory Care Expert Panel has defined 22 reminders that they recommend. The NCHP reminders are prefixed with VA-\* and the EP reminders with VA-. Any of these reminders that meet your site’s requirements may be used *as i*s. If your site requires a reminder that is not met by one of the distributed reminders, you can create your own. It is usually easiest to start by copying the existing reminder that is closest to what you want.

You may wish to review VHA Handbook 1101.8 Health Promotion and Disease Prevention Program (RCN 10-0666), VAMC Outpatient Performance Indications, and Clinical Guidelines as resource materials when deciding what reminders you need.

Create a Preventive Medicine Health Summary or add reminder and maintenance items to existing health summaries. You can print health summaries and provide them to clinicians for all scheduled visits, or show them how to view them on their computer monitors. A clinician may use the ADHOC health summary to review individual maintenance or reminder information.

When reviewers visit your medical center, make these summaries available to them. Feedback from reviewers who have used these health summaries during their reviews has been very positive.

PLEASE NOTE: Clinical reminders and clinical maintenance do *not* satisfy documentation requirements. Documentation supporting these reminders must still be made on progress notes, doctor’s orders, etc.

Implementing Clinical Reminders

Tips on how to get started with clinical reminders and clinical maintenance from a Clinical Coordinator’s perspective.

Clinical Reminders are created or modified by using a combination of PCE Table Maintenance options, Clinical Reminders Maintenance options, Taxonomy options, Health Summary Create/Modify Health Summary Type option, and AICS Encounter Form options.

*Follow the steps below, as applicable, to implement Clinical Reminders.*1. Ask IRMS staff to assign you the PCE Table Maintenance Menuand the PCE Reminder Maintenance Menu.

If you are a technical user, you may want to ask IRMS to add the PCE Reminder Test option as a secondary menu option.

2. Refer to Appendix A for clinical reminders guidelines and worksheets.

Gather the following:

Appendix A-1, Start-up Process for Implementing Reminders

Appendix A-3, Clinical Reminder Definition Worksheet

Appendix A-4, PCE Clinical Integration Worksheet

Copy of VA Performance Indicators

Copy of VHA Handbook 1101.8

Use a list of PCE Reminders/Maintenance items, health factors, and taxonomies for referral as you are working. The distributed reminders and taxonomies are listed in Appendixes A-8 and A-9. (Options to print these are located on the PCE Reminder Maintenance Menu, if you need more copies.)

3. Identify the reminders that your site wants to implement.

a\. Review reminder definitions with appropriate clinical staff and determine any reminders that will need editing.

- If you are going to use the distributed reminders *without* making any changes, you won’t need to copy them. For example, immunizations, skin tests, and blood pressures can be used as exported. If you wish to make changes (e.g., frequency, age range, health factors), copy the exported reminder and edit it.
- If no distributed reminder provides exactly what you require, you will need to create your own local reminder. It is usually easiest to start with the distributed reminder that is closest to your requirements. Copy it to a local reminder using the *Copy Reminder Item* option, and then edit the new reminder to meet your site’s needs. An example of copying and editing a reminders is at the end of this chapter.

> NOTE: The “VA-“ prefix designates the nationally distributed set. (Sites are not allowed to use the VA- prefix in the names of locally defined reminders.) Reminders with the “VA-\*” prefix represent the minimum requirements as defined by the National Center for Health Promotion (NCHP).

- You will always need to copy and edit the following reminders to add your specific laboratory or radiology test names:

> VA-\*: Breast Cancer Screen, \*Cholesterol Screen (M) and (F)

> VA-: Mammogram, PSA

> VA-\*: \*Cervical Cancer Screen, \*Colorectal Cancer Screen (FOBT), Colorectal Cancer Screen (Sig.), Hypertension Screen, Influenza, Immunization, Pneumococcal Vaccine, Tetanus Diphtheria Immunization, Weight and Nutrition Screen

> VA-: \*Pap Smear, \*FOBT, Flex sigmoidoscopy, Blood Pressure check, Influenza Vaccine, Pneumovax, PPD, Weight

> \* The Pap Smear and FOBT-type reminders don’t look at the laboratory test names at this time. However, a future lab patch is anticipated that will require you to enter the laboratory test name as you did for PSA and cholesterol reminders.

- The following screening and education reminders work “as is,” but you must activate the topics under the PCE Reminder Maintenance Menu. The Table Maintenance item should match one or more of the Target Result Findings items as listed in each reminder definition.

> VA-\*: Fitness and Exercise Screen, Problem Drinking Screen, Seat

> Belt and Accident Screen, and Tobacco Use Screen.

> VA-: Exercise Education, Alcohol Abuse Education, Seat Belt

> Education, Tobacco Education, Nutrition/Obesity Education,

> Advance Directives Education, Breast Exam, Breast Self Exam

> Education, Diabetic Eye Exam, Diabetic Foot Care Ed, Diabetic Foot

> Exam, Digital Rectal (Prostate) Exam

b\. Run enough copies of “Clinical Reminder Definition Worksheets”

(Appendix A-3) for the reminders you wish to edit.

c\. Complete a Clinical Definition Worksheet for each reminder you wish to change. This is where you define the reminder print name, description, type, target result finding file, timeframes, taxonomies, and health factors, etc.

d\. Get approval from your Medical Staff Executive Committee for your reminder definitions.

4. (optional) If a distributed taxonomy definition related to a reminder needs modification, do the following:

a\. Copy the taxonomy and then edit it, using the *Copy Taxonomy* option.

b\. Modify the reminder to reflect the newly created taxonomy, using the *Reminder Edit* option.

5. Use options on the PCE Table Maintenance Menu to enter any locally created education, examinations, health factors, immunizations, or skin tests.6. Coordinate the use of encounter forms (through the AICS package) with the use of Health Summary Clinical Maintenance components.

Make sure the relevant encounter forms contain all appropriate list bubbles for PCE data: Health factors, exams, immunizations, diagnosis, patient education, procedures, and skin tests.

7. Use the Health Summary package to activate clinical reminders and clinical maintenance components.

a\. Enable components through the Health Summary Maintenance Menu (GMTS IRM/ADPAC Maintenance Menu).

b\. Inactivate reminder topics you will not be using.

c\. Create a Preventive Medicine Health Summary to display reminders and health maintenance components, or add these components to existing health summaries. You can print copies and include them with the encounter form and chart for each visit, or your providers can view health summaries on their computers.

8. Inactivate reminders which will not be used, with the *Activate/Inactive Reminders* option.  
9. Test your reminders.

You can do this two ways:

a\. Run health summaries on patients you know have documented health factors or taxonomies.

b\. Use the *Reminder Test* option, a standalone option which technical users can use to see a programmer’s view of the results of a reminder for a patient. This option doesn’t affect any data; it provides debugging information. Check with your IRMS staff for availability..

10. Meet with users and explain Clinical Reminders, the use of the Preventive Medicine Health Summary, and the need for their continued documentation of progress notes, doctor’s orders, etc.11. Meet with appropriate staff to arrange for data validation to assure that:

a\. Encounter forms are being completed correctly

b\. Clerks are entering information that is marked on the encounter form (if using manual entry)

c\. Scanners are picking up information accurately (if scanning)

d\. Information is being passed to health summaries correctly

e\. Documentation in the patient’s medical record supports information displayed on the clinical reminders and clinical maintenance components

*Defining Clinical Terms with PCE Tables*

The PCE package provides options for defining terminology which your site can use to support capturing data for the reminders. The tables are categorized as follows:

> Education Topic Exam

> Health Factor Immunization

> Skin Test Treatment

With the exception of the table of Treatments, all of the table items are supplied in an activated state. (clinical reminders do not use Treatments). If there are choices that you don’t want your users to see and pick, you must deactivate them (with the PCE Table Maintenance *Activate/Inactivate Table Items* option).  
*PCE Reminder Maintenance Menu*Option Descriptions

List Reminder Definitions

Lists all of the Reminder/Maintenance item definitions.

Inquire About Reminder Item

Lists the definition of a selected reminder.

Add/Edit Reminder Item

Used to edit Reminder/Maintenance Item definitions.

Copy Reminder Item

Used to copy an existing reminder item definition into a new reminder item in the Reminder/Maintenance Item file (#811.9). Once the copy is completed, you will have the option of editing the new reminder.

Activate/Inactivate Reminders

Used to make reminders active or inactive with Health Summary.

List Reminder Types Logic

Lists the Reminder Types along with a summary of where the reminder's logic searches for data in V*IST*A to be used for the reminder type’s target patient findings.

List Taxonomy Definitions

Lists the current definition of taxonomies defined in the Taxonomy file which defines the coded values from ICD Diagnosis, ICD Operation/Procedures, or CPT codes that are a part of a clinical category (taxonomy). These taxonomy low and high range definitions are used by the Clinical Reminders logic to determine if a patient has coded values in the clinical files that indicate the patient is part of the taxonomy

Inquire about Taxonomy Item

Lists the current definition of a single taxonomy, including the same information as the Taxonomy List option.

Edit Taxonomy Item

Used to edit Taxonomy Item definitions.

Copy Taxonomy Item

Used to copy an existing taxonomy definition into a new entry in the Taxonomy file (#811.2). Once the taxonomy has been copied, you have the option of editing it.

Activate/Inactivate Taxonomies

This option allows you to activate/inactivate taxonomies.

*Reminder Test* \[PXRM REMINDER TEST\], a standalone option, provides the technical user with a tool that can facilitate the creation and debugging of reminder definitions. This option lets you run a reminder directly and see all the details. It is completely safe to use, and its impact on the system is no different than running a reminder through Health Summary. The use of this option is explained in detail in Appendix A-7.

Depending on a site’s preferences, IRMS can add this option to the Reminder

Maintenance menu or to a particular user’s secondary menus.

  
Copying and Editing a ReminderNOTE: Use one up-arrow (^) or two up-arrows (^^) to exit from the option. Two up-arrows (^^) are necessary to exit from some prompts (ones that are indented).

RL List Reminder Definitions

RI Inquire about Reminder Item

RE Add/Edit Reminder Item

RC Copy Reminder Item

RA Activate/Inactivate Reminders

RT List Reminder Types Logic

TL List Taxonomy Definitions

TI Inquire about Taxonomy Item

TE Edit Taxonomy Item

TC Copy Taxonomy Item

TA Activate/Inactivate Taxonomies

Select PCE Reminder Maintenance Menu Option: RC Copy Reminder Item

Select the reminder item to copy: FECAL OCCULT BLOOD TEST

PLEASE ENTER A UNIQUE NAME: LOCAL FECAL OCCULT BLOOD TEST

The original reminder FECAL OCCULT BLOOD TEST has been copied into LOCAL FECAL OCCULT BLOOD TEST.

Do you want to edit it now? YES

NAME: LOCAL FECAL OCCULT BLOOD TEST Replace \<Enter\>

REMINDER TYPE: LABORATORY TEST// \<Enter\>

PRINT NAME: Fecal Occult Blood Test Replace \<Enter\>

RELATED REMINDER GUIDELINE: VA-\*COLORECTAL CANCER SCREEN (FOBT) // \<Enter\>

INACTIVE FLAG: ?

Enter "1" to inactivate the reminder item.

Choose from:

1 INACTIVE

INACTIVE FLAG: \<Enter\>

REMINDER DESCRIPTION:

Fecal occult blood test due every year for patients ages 50 and older with

no dx of colorectal cancer.

This reminder is based on guidelines provided by the Ambulatory Care

Expert Panel. It also satisfies the "Colorectal Cancer Screen - FOBT"

guidelines specified in the "Guidelines for Health Promotion and Disease

Prevention", M-2, Part IV, Chapter 9.

EDIT? NO// \<Enter\>

TECHNICAL DESCRIPTION:. . .

. . .

Operation/Procedure file. If this taxonomy needs modification, copy the

taxonomy to a new taxonomy for your site, and make the appropriate

modifications.

Copy the reminder to a new reminder for your local site's modifications.

> **NOTE:** The Laboratory data is not available use in the reminder. When the

lab package begins passing CPT codes for fecal occult blood tests to PCE,

this reminder is ready to make use of the information.

EDIT? NO// \<Enter\>

Target Groups

DO IN ADVANCE TIME FRAME: 1M//\<Enter\>

SEX SPECIFIC: \<Enter\>

IGNORE ON N/A: ??

This field allows the user to stop reminders from being printed in the

"Clinical Maintenance" component of Health Summary if the reminder is

N/A. This is free text that can contain any combination of the

following codes:

Code Description

A N/A due to not meeting age criteria.

S N/A due to the wrong sex.IGNORE ON N/A: \<Enter\>

Baseline frequency age range set

Select REMINDER FREQUENCY: 0Y//\<Enter\>

REMINDER FREQUENCY: 0Y//\<Enter\>

MINIMUM AGE: 0//\<Enter\>

MAXIMUM AGE: 49//40

AGE MATCH TEXT:

Fecal Occult Blood Test (FOBT) not indicated in patients under 50.

EDIT? NO// YES

REPLACE 50 WITH 40 REPLACE \<Enter\>

EDIT Option: \<Enter\>

AGE NO MATCH TEXT:

No existing text

Edit? NO//\<Enter\>

Select REMINDER FREQUENCY: \<Enter\>

Target Findings

Select TARGET RESULT FINDINGS FILE: LABORATORY TEST//\<Enter\>

TARGET RESULT FINDINGS FILE: LABORATORY TEST//\<Enter\>

TARGET RESULT DESCRIPTION:

Identify all laboratory tests which represent Fecal Occult Blood tests in

the Target Result Findings Item multiple.

FOBT's may also be identified by defining a taxonomy in PCE Taxonomy that

identifies coded ranges of CPT or ICD Operation/Procedure codes that

represent this test.

EDIT? NO// \<Enter\>

Select TARGET RESULT FINDINGS ITEM: OCCULT BLOOD (STOOL)//\<Enter\>

TARGET RESULT FOUND TEXT:

No existing text

Edit? NO//

TARGET RESULT NOT FOUND TEXT:

No existing text

Edit? NO//

Taxonomy Findings

Select TAXONOMY: VA-COLORECTAL CA//\<Enter\>

TAXONOMY: VA-COLORECTAL CA//\<Enter\>

MINIMUM AGE: 30

MAXIMUM AGE: \<Enter\>

REMINDER FREQUENCY: 0Y//1Y

FOUND TEXT:

Patient known to have hx of colorectal cancer. Please verify appropriate

tx & f/u is ongoing.

NOT FOUND TEXT:

No hx of colorectal cancer on file - presumed no hx.

Edit? NO// \<Enter\>

RANK FREQUENCY: ??

This optional field is used to rank the frequency and age ranges that

are associated with this Taxonomy Finding.

This field is used for the situation 1) where more than one match is

found among Taxonomy Findings, and/or Health Factor Findings and/or

Computed Findings, and 2) where more than one of the Findings definitions

has its own age range and frequency. The rank is used to define a

priority or ranking that tells the reminder logic which age range and

frequency should take precedence when there are multiple results found.

The value which can be entered in the Rank field should be a number from

1 to 999, or blank. The highest ranking (priority) is number 1. When

there are multiple Findings found, the Finding with the highest rank will

be used to set the frequency and age range which are used to determine

when the reminder is due.

When the Rank field is blank (null) for this Taxonomy Finding, and also

blank for the Health Factor and Computed Findings definitions, the

reminder logic will use the frequency that will make the reminder occur

most often. For example, a Health Factor Finding has age range 25-50 with

a frequency of 6 months, and a Taxonomy Finding has age range 25-70 and a

frequency of 1 year. The Health Factor age and frequency would be used

for the reminder, since a 6 month interval is more frequent than 1 year

interval.

RANK FREQUENCY: \<Enter\>

USE IN DATE DUE CALC: ??

This optional field is used by the reminder logic to determine if the

date of a match on the Taxonomy Finding should be used to determine

the next date the reminder will be due. If there are multiple matches

among the Findings, and this Taxonomy Finding is the most recent

Finding, then the reminder date due will be calculated from the

encounter date of this Finding.

A blank in this field indicates the encounter date of the matched

Taxonomy Finding will NOT be used to determine the next date the

reminder will be due. The Taxonomy Finding encounter date and data WILL

however be displayed in the clinical maintenance component as

information.

This field is very useful for the situation when the Targeted Result

Findings AND this Taxonomy Finding should be used as valid patient

results satisfying the reminder.

Choose from:

1 YES

0 NO

USE IN DATE DUE CALC: \<Enter\>

USE IN APPLY LOGIC: ??

This optional field is used by the user to indicate that this Taxonomy

Finding should be included as part of the "Apply Logic". The Apply Logic

is used to determine whether or not a reminder should be applied (given)

to a patient. This is very useful for those situations where a reminder

should only be given to, or NOT given to patients with a particular

Taxonomy Finding, such as diabetes.

This "Use in Apply Logic" field can be defined with one of the following

coded values:

EQUATES TO BOOLEAN

CODE VALUE OPERATOR LOGIC

---- ----- -------------------

BLANK not included in Apply Logic (Use @ to delete value)

& AND &(Finding)

! OR !(Finding)

&' AND NOT &'(Finding)

!' OR NOT !'(Finding)

The code selected is used to create a default Boolean "Apply Logic"

string for this reminder. The Apply Logic string always initially

defaults to include (SEX)&(AGE), but will add &(Finding), !(Finding),

&'(Finding), or !'(Finding) to the string depending on the code in this

"Use in Apply Logic" field. If a more detailed definition of the Apply

Logic is required, then the "Apply Logic" field in the PCE REMINDER/

MAINTENANCE FILE (811.9) can be defined via FileMan. When the Apply

Logic is defined using FileMan, the "Use in Apply Logic" field will be

ignored by the reminder logic because the default "Apply Logic" is

overridden by the contents of the "Apply Logic" field. To reactivate the

default "Apply Logic", use FileMan to delete the contents of the "Apply

Logic" field.

Choose from:

& AND

! OR

&' AND NOT

!' OR NOT

USE IN APPLY LOGIC: \<Enter\>

Select TAXONOMY: \<Enter\>

TAXON GENERAL FOUND TEXT:

No existing text

Edit? NO//

TAXON GENERAL NOT FOUND TEXT:

No existing text

Edit? NO//

Health Factor Findings

Select HEALTH FACTOR FINDINGS ITEM: ACTIVATE FOBT CANCER SCREEN// \<Enter\>

HEALTH FACTOR FINDINGS ITEM: ACTIVATE FOBT CANCER SCREEN// \<Enter\>

MINIMUM AGE: \<Enter\>

MAXIMUM AGE: \<Enter\>

REMINDER FREQUENCY:

FOUND TEXT:

No existing text

Edit? NO// \<Enter\>

NOT FOUND TEXT:

No existing text

Edit? NO// \<Enter\>

RANK FREQUENCY:

USE IN DATE DUE CALC: \<Enter\>

USE IN APPLY LOGIC: \<Enter\>

Select HEALTH FACTOR FINDINGS ITEM:

HF GENERAL FOUND TEXT:

No existing text

Edit? NO// \<Enter\>

HF GENERAL NOT FOUND TEXT:

No existing text

Edit? NO// \<Enter\>

Computed Findings

Select ROUTINE: \<Enter\>

APPLY LOGIC: \<Enter\>

Select the reminder item to copy: \<Enter\>

RL List Reminder Definitions

RI Inquire about Reminder Item

RE Add/Edit Reminder Item

RC Copy Reminder Item

RA Activate/Inactivate Reminders

RT List Reminder Types Logic

TL List Taxonomy Definitions

TI Inquire about Taxonomy Item

TE Edit Taxonomy Item

TC Copy Taxonomy Item

TA Activate/Inactivate Taxonomies

Select PCE Reminder Maintenance Menu Option: \<Enter\>Health Summary Example

This example shows both clinical maintenance and clinical reminders components, so you can see the differences.

The clinical reminder component is an abbreviated compnent indicating only what is due now.

The clinical maintenance component provides:

- Details about what was found from searching the Vista clinical data
- Test related to the findings found or not found (as defined in the reminder)
- Final frequency and age range used for this reminder.

02/13/97 13:35

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CONFIDENTIAL TEST REMINDERS SUMMARY \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PCEPATIENT,ONE 000-45-6789 DOB: 08/18/24

-------------------- CM - Clinical Maintenance -------------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT-- --LAST--

Cholesterol Screen (Male) N/A

Patient's age (72) is greater than reminder maximum age of 65.

LAB: Date of last cholesterol test unknown.

Date of last cholesterol taxonomy (CPT) unknown.

Fecal Occult Blood Test 07/02/97 07/02/96

2/5/97 Health Factor: ACTIVATE FOBT CANCER SCREEN

7/2/96 Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

7/2/96 Encounter Procedure: 82270-TEST FECES FOR BLOOD

FOBT due 5 years after the last sigmoidoscopy.

Final Frequency and Age Range used: 1 year for ages 50 and older.

Flexisigmoidoscopy N/A

2/5/97 Health Factor: INACTIVATE SIGMOIDOSCOPY

7/2/96 Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

7/2/96 Encounter Procedure: 82270-TEST FECES FOR BLOOD

Final Frequency and Age Range used: 0Y - Not Indicated for ages 50

and older.

Exercise Education DUE NOW unknown

Final Frequency and Age Range used: 1 year for all ages.

Hypertension Detection DUE NOW unknown

Vitals: Date of last Vitals BP Measurement unknown.

Date of last ICD or CPT coded hypertension screen unknown.

Final Frequency and Age Range used: 2 years for all ages.

Influenza Immunization 07/02/97 07/02/96

7/2/96 Encounter Procedure: 90724-INFLUENZA IMMUNIZATION Influenza

vaccine due yearly in patients ages 65 and older.

Final Frequency and Age Range used: 1 year for ages 65 and older.

Pneumovax DONE 07/01/96

7/1/96 Encounter Procedure: 90732-PNEUMOCOCCAL IMMUNIZATION

Pneumovax due once for patients 65 and over.

Final Frequency and Age Range used: 99Y - Once for ages 65 and older.

Problem Drinking Screen DUE NOW unknown

Screen for alcohol problems yearly for all patients.

Final Frequency and Age Range used: 1 year for all ages.

Seat Belt and Accident Screen DUE NOW unknown

Seat belt education due yearly for all patients.

Final Frequency and Age Range used: 1 year for all ages.

Tobacco Use Screen DUE NOW unknown

Tobacco use screen due yearly for all ages.

No history of tobacco use screen on file. Please evaluate tobacco

use and educate if currently in use.

Final Frequency and Age Range used: 1 year for all ages.

Weight and Nutrition Screen DUE NOW unknown

Weight and Nutrition screen due yearly for all patients.

Final Frequency and Age Range used: 1 year for all ages.

----------------------- CR - Clinical Reminders -----------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT-- --LAST--

Exercise Education DUE NOW unknown

Hypertension Detection DUE NOW unknown

Problem Drinking Screen DUE NOW unknown

Seat Belt and Accident Screen DUE NOW unknown

Tobacco Use Screen DUE NOW unknown

Weight and Nutrition Screen DUE NOW unknown

\* END \*

Press \<RET\> to continue, ^ to exit component, or select component: ^Key Concepts

- Clinical Reminders on Health Summares furnish providers with timely information about their patients' health maintenance schedules.
- Providers can work with their local ADP coordinators to set up customized schedules based on local and national guidelines for patient education, immunizations, and other procedures.
- Options on the Clinical Reminder/Health Maintenance menu let you edit reminder and health maintenance definitions, based on your site's clinical terminology.
- A complete reminder definition includes associated components such as examinations, taxonomies, and health factors. Sites may define their own components to use in reminder defintions. A site may also create routines for computed findings where necessary. This makes reminders completely customizable by sites.
- Taxonomy entries define low and high range values from ICD Diagnosis, ICD Operation/Procedures, and CPT codes which are part of a clinical category (taxonomy).
- To alter a VA- prefixed reminder item, first copy it to a different name and then edit the reminder to reflect your site's requirements for the reminder.
- Once reminder criteria have been defined, they may be included in the Health Summary Type definitions for the Clinical Reminder and Health Maintenance components which will be displayed on Health Summaries.

## PCE Clinical Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE Clinical Reports options provide clinicians and managers with summary data about their patients, workload activity, and encounter counts. The reports extract data from various files in V*IST*A, including laboratory, pharmacy, and PIMS to create output reports which have been requested by physicians throughout the VA.

> **NOTE:** If the month or day aren't known for historical encounters, they will appear on encounter screens or reports with zeroes for the missing dates; for example, 01/00/95 or 00/00/94.

### PCE Clinical Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PA Patient Activity by Location

CP Caseload Profile by Clinic

ES PCE Encounter Summary

DX Diagnosis Ranked by Frequency

LE Location Encounter Counts

PE Provider Encounter Counts

*Option Descriptions*

Patient Activity by Clinic

This report provides a summary of patient data for one or more clinics as a measure of continuity of care.

Caseload Profile by Clinic

This report generates a profile of the patients in a clinic's caseload, given a selected date range. One or more clinics or a stop code may be selected to represent the caseload; it combines PCE encounter, Lab, Radiology, Outpatient Pharmacy, and Admissions data, with report areas of demographics, preventive medicine, quality of care markers, and utilization.

PCE Encounter Summary

This report provides a summary of PCE encounters based on the evaluation and management codes associated with encounters occurring within a selected date range. The representative period of time for the selected date range may be determined by clinical staff.

Diagnoses Ranked by Frequency

This report lists the most frequent diagnostic codes (ICD9) and the most frequent diagnostic categories.

Location Encounter Counts

This report counts PCE outpatient encounters in a date range by location. The location selection can be based on facility, hospital location(s), or clinic stop(s). The report can be run for all hospital locations or clinic stops in a facility or selected hospital locations or clinic stops.

Provider Encounter Counts

This report lists provider counts related to PCE outpatient encounters (in detailed or summary reports). The selection criteria includes facility, service category, provider, and date range. The facility criteria allows for selection of the facilities to be included on the report. The provider selection criteria allows for selection of all providers, primary providers, a list of individual providers, or the providers belonging to a list of provider classes. The date range specifies a time interval in which to look for encounters.

#### Patient Activity by Location

This report may be set up for hospital location or stop code. The report format is a summary of all selected locations. For each location, Scheduling data is used to identify patients whose appointments were either scheduled, unscheduled, cancelled, or are no-shows during the patient appointment date range. V*IST*A data for these patients is then examined for possible patient activities for admissions/discharges, emergency room encounters, and critical lab values during the patient activity date range. If any of these activities has occurred, data specific to the activity is reported along with the patient's address, phone, and future appointments that fall in the future appointment date range.

This report was developed as a measure of continuity of care. If a provider of record has his or her care-giving interrupted through clinical rotation, leave, reassignment, or for any other reason, this report may be used to get an update on patient activities in his/her caseload.

This report is also useful when care is not interrupted. Clinical staff may wish to review patient activity by clinic for events, which they might be unaware of.

Patient activities that are included in this report are:

*Admission/Discharge activities:*

All admissions and discharges within the selected date range are reported. If corresponding discharges exist for admissions, the discharges are shown, and vice versa; corresponding admissions are shown for discharges.

*Emergency Room Clinic activities:*

All Emergency Room stops within the selected date range are reported. Emergency Room visit date and time are displayed for all encounters with an identified Emergency Room stop. Emergency rooms are identified through the PCE PARAMETERS file. This data is entered by the clinical coordinator or IRM staff through the PCE Report Parameter Setup option.

*Critical Lab Values:*

All critical lab values reported within the selected date range are presented, along with a column to identify whether the value is critically high or critically low.

Select PCE Clinical Reports Option: Patient Activity Report

Select FACILITY: SALT LAKE CITY SALT LAKE CITY UT 660

Select another FACILITY: \<Enter\>

Select one of the following:

HA All Hospital Locations (with encounters)

HS Selected Hospital Locations

CA All Clinic Stops (with encounters)

CS Selected Clinic Stops

Determine patient activity for: HS// HA All Hospital Locations (with

encounters)

Want to start each location on a new page: Y// NO

Enter PATIENT APPOINTMENT BEGINNING DATE: 9/1/96 (SEP 01, 1996)

Enter PATIENT APPOINTMENT ENDING DATE: 9/30/96 (SEP 30, 1996)

Enter PATIENT ACTIVITY BEGINNING DATE: 9/1/96 (SEP 01, 1996)

Enter PATIENT ACTIVITY ENDING DATE: Apr 29, 1997// 9/30/96 (SEP 30, 1996)

Enter FUTURE APPOINTMENT BEGINNING DATE: Apr 29, 1997// \<Enter\> (APR 29,

1997\)

Enter FUTURE APPOINTMENT ENDING DATE: 12/30/97 (DEC 30, 1997)

DEVICE: HOME// \<Enter\> ANYWHERE RIGHT MARGIN: 80// \<Enter\>

Sorting appointments done

Sorting patient information done

Apr 29, 1997 3:03:05 pm Page 1

Criteria for Patient Activity Report

Location selection criteria: All Hospital Locations (with encounters)

Patient appointment date range: Sep 01, 1996 through Sep 30, 1996

Patient activity date range: Sep 01, 1996 through Sep 30, 1996

Future appointment date range: Apr 29, 1997 through Dec 30, 1997

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Location: ADMITTING AND SCREENING

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,ONE 000-45-6789

352 SW KENTWOOD RD SALT LAKE CITY UTAH 33452

Appointment criteria met:

9/30/96 14:30 ADMITTING AND SCREENING SCHEDULED VISIT

------------------------------ Inpatient Stays -----------------------

7/31/89 - present 4 WEST LOS: 2829

Last Tr. Specialty: PSYCHIATRY Last Prov:

Admitting Diagnosis: Disoriented

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Location: ADMITTING AND SCREENING

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,TEN 666-45-6789 412 555-5555

555 ENDLESS ST. PITTSBURGH PENNSYLVANIA 15206

Appointment criteria met:

9/23/96 09:00 ADMITTING AND SCREENING SCHEDULED VISIT

--------------------------- Emergency Room Visits -----------------------

9/25/96 11:30 DIABETES CLINIC

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,THREE 00-00-6788

22 3RD AVENUE SALT LAKE CITY UTAH 84112

Appointment criteria met:

9/ 2/96 09:00 ADMITTING AND SCREENING SCHEDULED VISIT

---------------------------- Critical Lab Values --------------------------

9/30/96 GLUCOSE 500 mg/dl

9/30/96 UREA NITROGEN 500 mg/dL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Location: CARDIOLOGY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,FOUR 666-99-2222

2237 E 1894 S Salt Lake City UTAH 84105

Appointment criteria met:

9/30/96 10:00 CARDIOLOGY SCHEDULED VISIT

--------------------------- Emergency Room Visits -----------------------

9/30/96 09:00 CARDIOLOGY CLINIC

Enter RETURN to continue or ‘^’ to exit:

Apr 29, 1997 3:03:05 pm Page 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Location: DIABETES CLINIC

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,SEVEN 000-88-9989

470 RANDOLPH ROAD SALT LAKE CITY UTAH 33595

Appointment criteria met:

9/24/96 09:00 DIABETES CLINIC SCHEDULED VISIT

---------------------------- Critical Lab Values ------------------------

9/30/96 GLUCOSE 500 mg/dl

9/30/96 UREA NITROGEN 500 mg/dL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Location: EYE CLINIC

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PCEPATIENT,EIGHT 666-12-1223

2122 S 5TH EAST SALT LAKE CITY UTAH 84108

Appointment criteria met:

9/18/96 13:00 EYE CLINIC SCHEDULED VISIT

Enter RETURN to continue or '^' to exit:

#### Caseload Profile by Clinic

This report generates a profile of the patients in a clinic's caseload for a selected date range. One or more clinics, or a stop code may be selected to represent the caseload. If stop code is selected, a report is generated for each clinic within that stop code. The percentage and overall mean are calculated based on the patient data for all of the clinics selected. Where only one clinic is selected, these values are not applicable.

> **NOTE:** There must be at least one PCE encounter within the selected date range for this report, even though there may be lab, radiology, and outpatient pharmacy occasions of service with the other timeframes (6 & 12 months).

This report combines PCE encounter, Lab, Radiology, Outpatient Pharmacy, and Admissions data. It provides a profile of the patients making up a clinic's caseload, over a representative period of time. Clinical staff will decide the appropriate date range. Report areas are demographics of clinic caseload, preventive medicine, quality of care markers, and utilization. Patient age, diagnosis, gender, Lab assay, RX, and procedure are all used to generate the patient profile.

There are three separate timeframes for the report:

SELECTED DATE RANGE

THE SIX (6) MONTHS PREVIOUS TO BEGINNING DATE

THE TWELVE (12) MONTHS PREVIOUS TO BEGINNING DATE

Search ranges are listed at the top of each report section.

DEMOGRAPHICS are based on the selected date range.

PREVENTIVE MEDICINE is based on 1) ICD9 codes recorded in PCE encounter diagnoses and 2) Radiology for the period 12 months previous to the beginning date.

QUALITY OF CARE MARKERS are based on Laboratory results, PCE encounter diagnoses, and scheduling data for the period six months previous to the beginning date.

UTILIZATION data is based on PCE encounters and outpatient pharmacy prescriptions for the period 12 months previous to the beginning date.

The six and twelve-month profiles probably won't change much month-to-month. How long the report takes to run varies according to the number of selected clinics, the number of encounters within that clinic, and the complexity of the patient data for any selected clinic.

*Technical Description:*

This option executes the Scheduling Package Clinic Workload (SET^SDCWL3) routines to identify patients whose appointments were either scheduled, unscheduled, cancelled, or no-shows during the selected date range.

Admissions are found by a call to IN5^VADPT for each date within the selected date range. Temporary storage of this data, for report purposes is at the global node ^TMP(\$J,"ADM",DFN,ADMISSION DATE). This node is set to discharge date^room-bed^street address^address line 2^city^state^zipcode^phone number.

Emergency clinics must be defined in field 801 of the PCE PARAMETERS file, which is a multiple pointing to the HOSPITAL LOCATION file. The ER clinic names are stored permanently at the global location: ^PX(815,D0,RR1,D1,0). A call is made to SDA^VADPT for stops occurring within the selected date range for the array of clinics listed at the above global location.

Laboratory data assessed for critical values is based on the Subfile 63.04 of the Lab DATA file (63), which stores results from Chemistry, Hematology, Toxicology, RIA, Serology, and others. Critical values are identified through a pattern match of a numeric value followed by a "\*". The global location read is ^LR(LRDFN,"CH",INVERSE LAB DATE, LAB TEST FIELD NUMBER). Piece one contains the result. Piece 2 indicates a critical value and if it is high or low (e.g. \*H).

Select PCE Clinical Reports Option: CP Caseload Profile by Clinic

Caseload Profile by Clinic

The overall mean values for this report will be for the clinic(s) selected

which had encounters during the selected date range.

Select clinic(s) by (H)OSPITAL LOCATION or CLINIC (S)TOP CODE: CLINIC STOP CODE

Select the CLINIC STOP code: DIABETES

Enter ENCOUNTER BEGINNING DATE: T-30 (JUN 29, 1996)

Enter ENCOUNTER ENDING DATE: Jul 29, 1996// \[ENTER\] (JUL 29, 1996)

DEVICE: HOME// \[ENTER\] VAX RIGHT MARGIN: 80//\[ENTER\]

Jul 29, 1996@11:21

Caseload Profile by Clinic

Clinic: DIABETES CLINIC

Compared to the mean of: DIABETES Clinic Stop

for 1 of 1 clinics with data

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CASELOAD DEMOGRAPHICS for Encounter date range \| Clinic \| Overall

Jun 29, 1996 to Jul 29, 1996 \| \# \| % \| Mean %

--------------------------------------------------------------------------------

Number of patient encounters 40 - -

Number of clinic sessions 17 - -

Number of patients per clinic session 2.4 - -

Median patient age in years 46 - -

Patients with: Coronary Artery Disease 0 0.0 0.0

Diabetes 0 0.0 0.0

Hypertension 0 0.0 0.0

Hyperlipidemia 0 0.0 0.0

Diabetes and Hypertension 0 0.0 0.0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PREVENTIVE MEDICINE (12 mos. prior to Jul 29, 1996)\| Clinic \|Overall

Jul 30, 1995 to Jul 29, 1996 \| \# \| % \| Mean %

--------------------------------------------------------------------------------

Patients who smoke. 0 0.0 0.0

Females \>50 who had a mammogram in the last year 0 0.0 0.0

(There were 1 females \>50 years of age).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUALITY OF CARE MARKERS (6 mos. prior to Jul 29, 1996) \| Clinic \|Overall

Jan 31, 1996 to Jul 29, 1996 \| \# \| Mean \#

--------------------------------------------------------------------------------

Average HBA1C of your patients with Diabetes N/A N/A

Patients with HBA1C\> 7% 0 0.0

Patients w/ Coronary Artery Disease who smoke 0 0.0

Ave. LDL for patients with Coronary Artery Disease N/A N/A

(0 of 0 pats. with CAD had no LDL results.)

Number of patients with: Glucose \>240 0 0.0

Cholesterol \>200 0 0.0

Either a Systolic bp \>160 or

Diastolic bp \> 90 0 0.0

Unscheduled encounters per patient. 0.0 0.0

Emergency Room encounters per patient. 0.0 0.0

Hospitalizations per patient. 0.2 0.2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

UTILIZATION DATA (12 months prior to Jul 29, 1996 \| Number \| Overall

Jul 30, 1995 to Jul 29, 1996 \| \# \| Mean \#

--------------------------------------------------------------------------------

Number of male patients 9 -

Number of female patients 4 -

Average number of encounters per patient 6.8 6.8

Average number of active outpt. medications per patient 0.0 0.0

Average pharmacy cost per patient \$ 0.0 0.0

Press RETURN to continue...

#### PCE Encounter Summary

This report provides a summary of PCE encounters based on the evaluation and management CPT codes associated with encounters occurring within a selected date range. The representative period of time for the selected date range may be determined by clinical staff.

This report may be run by Location or by Provider. Individual encounter totals are presented as line items on a 80 column report.

*Location criteria* can specify All Hospital Locations, Selected Hospital Locations, All Clinic Stops, or Selected Clinic Stops.

- *Hospital Locations*only encounters where the encounter's hospital location is the same as one of the selected hospital locations are used to generate the report.
- *Clinic Stops*only encounters where the encounter's clinic stop is the same as one of the selected clinic stops are used to generate the report.
- *Service Category*only encounters with the specified service category or categories are used to generate the report. This defaults to "AI" for Ambulatory encounters and clinic encounters where the patient had an inpatient status.

  *Provider criteria* can specify All Providers with encounters, Primary Providers with encounters, Selected Providers, or Selected Person Classes.
- *Providers*only encounters where one of the encounter providers is the same as one of the providers selected are used to generate the report.
- *Primary Providers*only encounters where one of the encounter providers is designated as a Primary provider are used to generate the report.

User may also select the Servise Categories and Encounter Types. The system will show the default Categories and types baces on the criteria the user selects.

Service Categories:

Example of a PCE Encounter Summary Report by Location

Jul 13, 2007 11:09:08 am Page 2

PCE Encounter Summary

Facility: DAYTON 552

LOCATION

E&M CATEGORIES NON NO TOT TOT UNIQ IN OUT

PCE: NEW EST CON OTH E&M CPT ENC VIS SSN PAT PAT

------------------------------------------------------------------------------

SCH: C&P 10-10 SCH UNS

================================================================================

PSYCHIATRY-MD INDIVIDUAL (509)

PCE: 0 0 0 0 4 0 4 3 1 0 3

------------------------------------------------------------------------------

SCH: 0 0 4 0

MHC AARONSON (509)

PCE: 0 0 0 0 4 0 4 3 1 0 3

------------------------------------------------------------------------------

SCH: 0 0 4 0

Enter RETURN to continue or '^' to exit:

Jul 13, 2007 11:09:12 am Page 3

PCE Encounter Summary

Facility: DAYTON 552

LOCATION

E&M CATEGORIES NON NO TOT TOT UNIQ IN OUT

PCE: NEW EST CON OTH E&M CPT ENC VIS SSN PAT PAT

------------------------------------------------------------------------------

SCH: C&P 10-10 SCH UNS

================================================================================

DAYTON 552 (totals)

PCE: 0 0 0 0 4 0 4 3 1 0 3

------------------------------------------------------------------------------

SCH: 0 0 4 0

GRAND TOTALS

PCE: 0 0 0 0 4 0 4 3 1 0 3

------------------------------------------------------------------------------

SCH: 0 0 4 0

End of the report. Press ENTER/RETURN to continue...

Example of a PCE Encounter Summary Report by Provider

Jul 13, 2007 8:56:55 am Page 1

PCE Encounter Summary

Facility: DAYTON 552

PROVIDER

E&M CATEGORIES NON NO TOT TOT UNIQ IN OUT

PCE: NEW EST CON OTH E&M CPT ENC VIS SSN PAT PAT

------------------------------------------------------------------------------

SCH: C&P 10-10 SCH UNS

================================================================================

AIHTLYNL,JEUDTSDLYL XARUHZD (Physicians (M.D. and...+Physician/Osteopath+

Internal Medicine)

PCE: 0 0 0 0 1 0 1 1 1 0 1

------------------------------------------------------------------------------

SCH: 0 0 1 0

BAXJE,BDZ (Respiratory, Rehabil...+Physical Therapist)

PCE: 0 0 0 0 1 1 2 2 2 0 2

------------------------------------------------------------------------------

SCH: 0 0 1 1

BLRZLYY,ZDJELHA L (Physicians (M.D. and...+Physician/Osteopath+Internal Medicine

)

PCE: 0 0 0 1 0 0 1 1 1 0 1

------------------------------------------------------------------------------

SCH: 0 0 0 0

BXUJEHUT,TLZRHA (Eye and Vision Servi...+Optometrist)

PCE: 0 0 0 0 3 0 1 1 1 0 1

------------------------------------------------------------------------------

SCH: 0 0 1 0

DUHP,ILQH (Behavioral Health an...+Social Worker+Clinical)

PCE: 0 0 0 0 0 1 1 1 1 0 1

------------------------------------------------------------------------------

SCH: 0 0 0 1

YLW,CLNTXY A (Allopathic and Osteo...+Resident, Allopathic...)

PCE: 0 0 0 1 0 0 1 1 1 0 1

------------------------------------------------------------------------------

SCH: 0 0 0 0

Enter RETURN to continue or '^' to exit:

Jul 13, 2007 8:56:55 am Page 2

PCE Encounter Summary

Facility: DAYTON 552

PROVIDER

E&M CATEGORIES NON NO TOT TOT UNIQ IN OUT

PCE: NEW EST CON OTH E&M CPT ENC VIS SSN PAT PAT

------------------------------------------------------------------------------

SCH: C&P 10-10 SCH UNS

================================================================================

DAYTON 552 (totals)

PCE: 2 16 1 31 179 24 218 167 40 15 152

------------------------------------------------------------------------------

SCH: 0 0 151 8

GRAND TOTALS

PCE: 2 16 1 31 179 24 218 167 40 15 152

------------------------------------------------------------------------------

SCH: 0 0 151 8

End of the report. Press ENTER/RETURN to continue...

#### Diagnosis Ranked by Frequency

This report produces two lists: most frequent diagnoses (ICD) and most frequent diagnostic categories. The list entries are ordered with the most frequent encounter diagnosis first. The most frequent diagnosis categories list is based on the ICD diagnostic category related to each diagnosis in the frequent diagnosis list.

The report can be generated using a number of different selection criteria:

- *Facility*select the facilities encounters to include in the report.
- *Primary Diagnoses only or All Diagnoses*if primary is selected then only primary diagnosis associated with an encounter will be included in the report. All diagnosis will include Primary and secondary diagnoses associated with an encounter.
- *Encounter Date Range*only encounters that fall within the specified date range are used to generate the report.
- *Number of most frequent diagnoses*this will determine how many diagnoses and diagnoses categories are listed on the report. For example, if 20 was input for this criteria, the report would list up to 20 of the most frequent diagnoses found associated with encounters. Diagnoses and diagnostic categories are ranked from most frequent to least frequent. If the encounters contained less than 20 different diagnoses, the report lists all the different diagnoses that were found.

The remaining criteria are optional for singling out diagnosis entries based on other encounter or patient data. You can accept the default "other" encounter/patient criteria which is all VA Clinic encounters (Service Category of "A" or "I") for all patients.

*Other encounter/patient report selection criteria:*

- *Service Category*only encounters with the specified service category or categories are used to generate the report. This defaults to "AI" for Ambulatory encounters and encounters at a clinic where the patient had an inpatient status.
- *Clinic Stop Code*only encounters with the specified list of clinic stop codes are used to generate the report.

  Provider criteria can specify All Providers, Primary Providers, Selected Providers, or Selected Provider Classes.
- *Providers*only encounters, where one of the encounter providers is the same as one of the providers selected, are used to generate the report.
- *Primary Providers*only encounters, where one of the encounter providers is designated as a Primary provider,are used to generate the report.
- *Provider class*only encounters, where one of the encounter providers has the same provider class as one of the providers classes selected, will be used to generate the report.
- *Patient Date of Birth Range*only encounters, where the patient's date of birth falls in the specified range, will be used to generate the report.
- *Patient Sex*only encounters, where the patient's sex matches the specified sex, are used to generate the report.

To include all encounters, ignoring all defaults for the other criteria, specify "A" for All Encounters at the Other criteria prompt.

Select PCE Clinical Reports Option: DX Diagnosis Ranked by Frequency

Select FACILITY: SALT LAKE CITY// \[ENTER\] UT 660

Select another FACILITY: \[ENTER\]

Select PRIMARY DIAGNOSIS ONLY (P) or ALL DIAGNOSES (A): P// P rimary Diagnosis Only

Enter ENCOUNTER BEGINNING DATE: T-30 (JUN 29, 1996)

Enter ENCOUNTER ENDING DATE: Jul 29, 1996// \[ENTER\] (JUL 29, 1996)

This report will include all VA clinic encounters for all patients

unless you modify the criteria. Do you want to modify the criteria?

Enter Y (YES) or N (NO) N// YES

Encounters may be selected by any combination of the following attributes:

1 Service Category

2 Clinic Stop Code

3 Provider

4 Age of Patient

5 Sex of Patient

6 All Encounters

Enter encounter selection attribute number(s) : (1-6): 1-3

Select SERVICE CATEGORIES: AI// ?

A AMBULATORY

H HOSPITALIZATION

I IN HOSPITAL

T TELECOMMUNICATIONS

E EVENT (HISTORICAL)

D DAILY HOSPITALIZATION DATA

X ANCILLARY PACKAGE DAILY DATA

Select SERVICE CATEGORIES: AI// \[ENTER\]  

Select CLINIC STOP: CARDIOLOGY

Select another CLINIC STOP: DIABETES

Select another CLINIC STOP: CARDIOLOGY

Select one of the following:

A All Providers

P Primary Providers

S Selected Providers

C Selected Provider Classes

Select ENCOUNTER PROVIDER CRITERIA: A// Primary Providers

Enter the maximum NUMBER OF DIAGNOSES to display in the report: 10// \[ENTER\]

DEVICE: HOME// \[ENTER\] VAX RIGHT MARGIN: 80// \[ENTER\]

Jul 29, 1996 12:22:30 pm Page 1

PCE Diagnosis Ranked by Frequency

Criteria for Frequency of Diagnoses Report

Encounter diagnoses: Primary Diagnosis Only

Encounter date range: Jun 29, 1996 through Jul 29, 1996

Selected Providers: Primary Providers

Selected clinics: YES

Patient age range: ALL

Patient sex: ALL

Service categories: AI

A - AMBULATORY

I - IN HOSPITAL

Maximum number of diagnoses to be displayed: 10

Facility: SALT LAKE CITY 660

Clinic Stop: CARDIOLOGY (143)

Total number of Encounters meeting the selection criteria: 54

Total number of Primary Diagnoses for these Encounters: 43

Diagnoses/Encounter ratio: 0.80

10 Most Frequent ICD Diagnoses:

Code Description Frequency

------ ------------------------------ ---------

1\. 401.1 BENIGN HYPERTENSION 10

2\. 100.0 LEPTOSPIROS ICTEROHEM 6

3\. V70.3 MED EXAM NEC-ADMIN PURP 4

4\. 440.20 ATHEROSCL, NAT ART EXTR, UNSP 3

5\. 321.0 CRYPTOCOCCAL MENINGITIS 3

6\. 223.0 BENIGN NEOPLASM KIDNEY 3

7\. 200.02 RETICULOSARCOMA THORAX 2

8\. 550.10 UNILAT ING HERNIA W OBST 1

Enter RETURN to continue or '^' to exit:

Jul 29, 1996 12:22:41 pm Page 3

PCE Diagnosis Ranked by Frequency

10 Most Frequent ICD Diagnoses:

Code Description Frequency

------ ------------------------------ ---------

9\. 402.00 MAL HYPERTEN HRT DIS NOS 1

10\. 224.0 BENIGN NEOPLASM EYEBALL 1

10 Most Frequent Diagnostic Categories:

Diagnostic Category Frequency

------------------------------ ---------

1\. CIRCULATORY SYSTEM 14

2\. NERVOUS SYSTEM 7

3\. INFECTIOUS & PARASITIC 6

4\. HEALTH STATUS FACTORS 4

5\. KIDNEY & URINARY TRACT 4

6\. MYELOPROLIFERATIVE,NEOPLASIA 2

7\. DIGESTIVE SYSTEM 2

8\. MENTAL DISEASES & DISORDERS 1

9\. FEMALE REPRODUCTIVE SYSTEM 1

10\. EAR, NOSE, MOUTH & THROAT 1

Facility: SALT LAKE CITY 660

Clinic Stop: DIABETES (146)

Total number of Encounters meeting the selection criteria: 21

Total number of Primary Diagnoses for these Encounters: 16

Diagnoses/Encounter ratio: 0.76

10 Most Frequent ICD Diagnoses:

Code Description Frequency

------ ------------------------------ ---------

1\. 250.01 DIABETES MELLI W/0 COMP TYP I 7

2\. 100.0 LEPTOSPIROS ICTEROHEM 2

3\. 333.0 DEGEN BASAL GANGLIA NEC 1

4\. 321.0 CRYPTOCOCCAL MENINGITIS 1

5\. 223.0 BENIGN NEOPLASM KIDNEY 1

6\. 333.1 TREMOR NEC 1

7\. 229.9 BENIGN NEOPLASM NOS 1

8\. 221.2 BENIGN NEOPLASM VULVA 1

9\. 100.81 LEPTOSPIRAL MENINGITIS 1

10 Most Frequent Diagnostic Categories:

Diagnostic Category Frequency

------------------------------ ---------

1\. ENDOCRINE,NUTRIT,METABOLIC 7

2\. NERVOUS SYSTEM 4

3\. INFECTIOUS & PARASITIC 2

4\. MYELOPROLIFERATIVE,NEOPLASIA 1

5\. FEMALE REPRODUCTIVE SYSTEM 1

6\. KIDNEY & URINARY TRACT 1

End of the report.

#### Provider Encounter Counts

This report provides the number of PCE outpatient encounters within an encounter date range, by provider. The user specifies report selection criteria and then chooses either a summary report or detailed report.

The report can be generated using a number of different selection criteria:

- *Facility*enter the names or numbers of the facilities whose encounters will be included in the report.
- *Encounter Date Range*only encounters that fall within the specified date range are used to generate the report.
- *Service Category*only encounters with the specified service category or categories are used to generate the report. This defaults to "AI" for Ambulatory encounters and clinic encounters where the patient had an inpatient status.

  *Provider criteria* can specify All Providers with encounters, Primary Providers with encounters, Selected Providers, or Selected Person Classes.
- *Providers*only encounters where one of the encounter providers is the same as one of the providers selected are used to generate the report.
- *Primary Providers*only encounters where one of the encounter providers is designated as a Primary provider are used to generate the report.
- *Person class*only encounters where one of the encounter providers has the same person class as one of the person classes selected are used to generate the report.

Person class selection is based on the PERSON CLASS file, used to support Ambulatory Care Reporting. Person Class entries are composed of three pieces:

- Occupation (required in class defintion)
- Specialty (optional)
- Sub-specialty (optional)

The legend for the service categories is included on the top of the report. For example, if on a particular day the provider had three ambulatory encounters and two telecommunications encounters, the string would be "AT" and the number of encounters would be five.

The summary report lists the total number of encounters for each provider.

Select PCE Clinical Reports Option: Provider Encounter Counts

Select FACILITY: SALT LAKE CITY// \[ENTER\] UT 660

Select another FACILITY: \[ENTER\]

Enter ENCOUNTER BEGINNING DATE: T-30 (JUN 29, 1996)

Enter ENCOUNTER ENDING DATE: Jul 29, 1996// \[ENTER\] (JUL 29, 1996)

Select SERVICE CATEGORIES: AI// \[ENTER\]

Select one of the following:

A All Providers

P Primary Providers

S Selected Providers

C Selected Provider Classes

Select ENCOUNTER PROVIDER CRITERIA: A// Primary Providers

Select PROVIDER: PCEPROVIDER,FOUR

Select another PROVIDER: PCEPROVIDER,FIVE

Select another PROVIDER:

Select one of the following:

S Summary

D Detail by clinic and date

Which type of report: S// \[ENTER\] Summary

DEVICE: HOME// \[ENTER\] VAX RIGHT MARGIN: 80// \[ENTER\]

Sorting encounters done

Jul 29, 1996 12:25:47 pm Page 1

PCE Provider Encounter Counts

Criteria for Provider Encounter Summary Report

Provider selection criteria: Selected Providers

Report date range: Jun 29, 1996 through Jul 29, 1996

Service categories: AI

A - AMBULATORY

I - IN HOSPITAL

Facility: SALT LAKE CITY 660

(Person Class)

Provider (Occupation+Specialty+Subspecialty) Encounters

----------------------------------------------------- ----------

PCEPROVIDER,ONE (Nursing Service+Nursing Administrato..) 3

PCEPROVIDER,TWO (Pharmacy Services) 6

PCEPROVIDER,SIX (Unknown) 15

PCEPROVIDER,NINE (Pharmacy Services) 10

PCEPROVIDER,TEN (Medical Services) 92

PCEPROVIDER,FOUR (Eye and Vision Services+Ophthalmic Med) 27

PCEPROVIDER,FIVE (Physician Assistant+Medical) 4

PCEPROVIDER,EIGHT(Physician) 7

Total facility encounters 164

Total encounters 164

End of the report

Selected Person Classes

This “Selected Person Classes” option lets you compile a report of selected Person Classes based on occupation, specialty, and/or sub-specialty. A wild card (\*) may be entered as a response for any of the Person Class pieces. For example, if you want a report on every provider from a specific specialty, occupation would be “\*,” specialty would be the specific specialty, and sub-specialty would be “\*.”

Select PCE Clinical Reports Option: PE Provider Encounter Counts

Select FACILITY: SALT LAKE CITY// \<Enter\> UT 660

Select another FACILITY:

Enter ENCOUNTER BEGINNING DATE: T-300 (APR 13, 1996)

Enter ENCOUNTER ENDING DATE: Feb 07, 1997//\<Enter\> (FEB 07, 1997)

Select SERVICE CATEGORIES: AI//\<Enter\>

Select one of the following:

A All Providers (with encounters)

P Primary Providers (with encounters)

S Selected Providers

C Selected Person Classes

Select ENCOUNTER PROVIDER CRITERIA: S// C Selected Person Classes

Select PERSON CLASS (OCCUPATION, SPECIALTY, SUBSPECIALTY)

Select OCCUPATION (enter \* for all, return to end selection): \*

The currently selected OCCUPATION is: \*

Select SPECIALTY (enter \* for all, return to change OCCUPATION): PHYSICALTHERAPIST

Select SUBSPECIALTY (enter \* for all): \*

Your Person Class Selection was:

OCCUPATION: \*

SPECIALTY: Physical Therapist

SUBSPECIALTY: \*

Is this selection correct? YES

The currently selected OCCUPATION is: \*

Select SPECIALTY (enter \* for all, return to change OCCUPATION): \<Enter\>

Select another PERSON CLASS OCCUPATION

Select OCCUPATION (enter \* for all, return to end selection): \<Enter\>

Select one of the following:

S Summary

D Detail by clinic and date

Which type of report: S// \<Enter\> Summary

DEVICE: HOME// \<Enter\> VAX RIGHT MARGIN: 70//\<Enter\>

Sorting encounters done

Feb 07, 1997 8:21:03 am Page 1

PCE Provider Encounter Counts

Criteria for Provider Encounter Summary Report

Provider selection criteria: Selected Person Classes

Report date range: Apr 13, 1996 through Feb 07, 1997

Service categories: AI

A - AMBULATORY

I - IN HOSPITAL

Selected Person Classes:

Occupation: \*

Specialty: Physical Therapist

Subspecialty: \*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Facility: SALT LAKE CITY 660

Person Class

Provider (Occupation+Specialty+Subspecialty) Encounters

--------------------------------------------------- ----------

PCEPROVIDER,TEN (Respiratory, Rehabil...+Physical 25

Therapist+Clinical Electrophys...)

PCEPROVIDER,SIX (Respiratory, Rehabil...+Physical 5

Therapist+Clinical Electrophys...)

\_\_\_\_

Total facility encounters 30

Total encounters 30

End of the report.

#### Location Encounter Counts

This report provides the number of PCE outpatient encounters within an encounter date range, by location.

The location report selection criteria can be based on facility, hospital location(s), or clinic stop(s). The selection criteria are:

- Facility select the facilities whose encounters are to be included in the report.
- Service Categoryonly encounters with the specified service category or categories are used to generate the report. This defaults to "AI" for Ambulatory encounters and clinic encounters where the patient had an inpatient status.
- Encounter Date Rangeonly encounters that fall within the specified date range are used to generate the report.

  *Location criteria* can specify All Hospital Locations, Selected Hospital Locations, All Clinic Stops, or Selected Clinic Stops.
- *Hospital Locations*only encounters where the encounter's hospital location is the same as one of the selected hospital locations are used to generate the report.
- *Clinic Stops*only encounters where the encounter's clinic stop is the same as one of the selected clinic stops are used to generate the report.

The report lists the number of encounters alphabetically by the location criteria selected.

## Select PCE Clinical Reports Option: LE Location Encounter Counts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select FACILITY: SALT LAKE CITY// \[ENTER\] UT 660

Select another FACILITY: \[ENTER\]

Select SERVICE CATEGORIES: AI// \[ENTER\]

Enter ENCOUNTER BEGINNING DATE: T-30 (JUN 29, 1996)

Enter ENCOUNTER ENDING DATE: Jul 29, 1996// \[ENTER\] (JUL 29, 1996)

Select one of the following:

HA All Hospital Locations

HS Selected Hospital Locations

CA All Clinic Stops

CS Selected Clinic Stops

Determine encounter counts for: HA// CA All Clinic Stops

DEVICE: HOME// \[ENTER\] VAX RIGHT MARGIN: 80//\[ENTER\]

Jul 29, 1996 12:24:33 pm Page 1

PCE Location Encounter Counts

Criteria for Clinic Encounter Count Report

Location selection criteria: All Clinic Stops

Encounter date range: Jun 29, 1996 through Jul 29, 1996

Service categories: AI

A - AMBULATORY

I - IN HOSPITAL

Facility: SALT LAKE CITY 660

Clinic Stop (Stop Code) No. of Encounters

------------------------------------ -----------------

ADMITTING/SCREENING (102) 3

CARDIOLOGY (303) 64

DIABETES (306) 48

GASTROENTEROLOGY (307) 1

GENERAL INTERNAL MEDICINE (301) 2

ORTHOPEDICS (409) 4

\_\_\_\_\_

Total facility encounters 122

Total encounters 122

End of the report.

  
Key Concepts

- You can produce reports for Caseload Profile by Clinic, Workload by Clinic, Frequency of Diagnoses, Location Encounter Counts, Provider Encounter Counts, Patient Activity by Clinic.
- All reports can be customized to show only specified date ranges, clinics, providers, types of encounters (cancelled, walk-ins, etc.), etc.
- The reports extract data from various files in V*IST*A, including laboratory, pharmacy, and PIMS to create output reports which have been requested by physicians throughout the VA.
- *Caseload Profile by Clinic* provides a measure of continuity of care. If a provider of record has his or her care-giving interrupted through clinical rotation, leave, reassignment, or for any other reason, this report may be used to get an update on patient activities in his/her caseload.
- *Workload by Clinic* provides a summary of clinic workload based on the evaluation and management codes associated with encounters.

### Missing Data Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missing Data Report (MDR) option is available from the PCE Coordinator menu. The MDR identifies CIDC data elements missing from PCE.

Who can use this report?

This report provides the HIMS (Health Information Management Systems) staff the ability to sort encounters missing CIDC data using a variety of specific data items. It allows the printing of two formats, statistics versus detail, in order to perform trending for possible follow-up with providers for education/training purposes.

> **NOTE:** The MDR must be printed to a 132 column device in order to view the entire data set.

See Appendix A for a sample MDR Report, sorted by Data Source.

# # Supplementary Material

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Helpful Hints

- The Automated Information Collection System (AICS) package includes a Print Manager that allows sites to define reports that should print along with the encounter forms. This can save considerable time preparing and collating reports for appointments. See the *Automated Information Collection System User Manual* for instructions.
- You can add Health Summary, Problem List, and Progress Notes as actions to PCE, to allow quick access to these programs. When you press the \[RETURN\] key at the quit prompts (or up-arrow out), you are automatically returned to PCE.
- Since problems can occur if you delete patients (the internal entry number of the file can be reassigned, causing discrepancies in the data), we recommend that you NOT delete any patients.
- If clinical reminders aren't showing up correctly on Health Summaries, see Appendix A-7 for troubleshooting information. (PXRMDEV is a routine that can be used to aid in the development and customization of reminders.)
- If you see zeroes instead of numbers on encounter dates (e.g., 00/00/95 or 01/00/96)on reports or encounter displaysthey are for Historical Encounters where the exact date is not known.
- *Shortcuts*

> After Diagnosis has been entered, if the Provider Narrative is an exact match, you can enter = and the diagnosis is duplicated.

> The equals sign (=) can also be used as a shortcut when selecting an action plus encounters or appointments from a list in a single response (e.g., Select Action: ED=2).

To quickly add or edit encounter information, select an appointment number at the first appointment screen.

## Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: What is the 10/1/96 mandate and how does PCE fit into it?

A: The Veterans Health Administration has determined that it must have adequate, accurate, and timely information about each ambulatory care encounter/service provided in order to enhance patient care and to manage our health care resources into the future. Effective October 1, 1996, VHA facilities are required to report each ambulatory encounter and/or ancillary service. Provider, procedure, and diagnosis information is included in the minimum data set that will be reported to the National Patient Care Data Base (NPCDB). The Ambulatory Data Capture Project (ADCP) was formed to coordinate the various V*IST*A packages involved in meeting this mandate.

Patient Care Encounter (*PCE) ensures that every encounter has an associated provider(s), procedure code(s), and diagnostic code(s), in accordance with this mandate.Software necessary to support ADCP*

- Automated Information Collection System (AICS) and other capture solutions
- Patient Care Encounter (including)

Visit Tracking v.2.0

Patch SD\*5.3\*27

Patch GMT\*2.7\*8

- Problem List
- Patient InformationManagement System
- National Patient Care Data Base.

*Other Patches involved in the 10/1/96 mandate*

|              |                                                                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Patch    | Description                                                                                                                                     |
| XU\*8\*27    | Person Class File and Utilities                                                                                                                     |
| IB\*2\*60    | Collects Type of Insurance, Passes active Ambulatory Surgery Procedure codes to PCE Enables entry of providers and diagnoses interactively into PCE |
| RA\*4.5\*4   | Interfaces with PCE to pass provider and procedure data for ambulatory Radiology/Nuclear Medicine encounters                                        |
| LR\*5.2\*127 | Interfaces with PCE to pass provider and procedure data for ambulatory Laboratory encounters                                                        |
| IBD\*2.1\*2  | AICS Manual Data Entry functionality                                                                                                                |
| GMRV\*3\*3   | Measurement Data collected via AICS passed through PCE Device Interface to Vitals/Measurement Pkg                                                   |
| SD\*5.3\*44  | Ambulatory Care Reporting Patch                                                                                                                     |

Q. How does PCE collect and report on diagnosis and procedures that are checked off on the DIAGNOSIS and CPT PROCEDURE tool kit boxes on Encounter Forms?

A: Items that are checked off in the above mentioned tool kit boxes are validated and stored by PCE into PCE files and then shared with other subscribing packages such as Scheduling.

- Two PCE Health Summary Components display diagnosis and procedure information: Outpatient Diagnosis and Outpatient Encounter.
- The Outpatient Diagnosis Component displays: the date of the encounter, the facility, the hospital location, the encounter eligibility, the provider(s), the diagnoses, ICD9 code, ICD9 text and Provider Narrative.
- The Outpatient Encounter component displays all the information included in the Outpatient Diagnosis component plus the procedure(s), CPT code, short description and Provider Narrative.
- If an immunization or skin test is collected by PCE through any of the four data collection interfaces PCE supports, data is stored in the procedure file and the Immunization or Skin Test file. Immunization or Skin Test information is included in the Outpatient Encounter component displays.
- In addition, there are separate PCE Skin Test and Immunization components which only display information specific to Skin Tests and Immunizations. The Immunization component displays immunization, series, date, facility, and reaction. The Skin Test component displays skin test, reading, results, reading date, facility.
- If you want to display Patient Education, treatments, examinations, and health factor information using the PCE Health Summary components, check the specific EF tool kit boxes. Otherwise that information is to be entered manually either through AICS manual data entry or PCE manual data entry.
- PCE also exports six clinical reports. Two of those reports display diagnosis data related to the numbers of patients associated with the identified diagnoses: *Caseload Profile by Clinic* and *Diagnosis Ranked by Frequency*.

Q: Explain how "Health Factors" in PCE and AICS are to be used and how this data may eventually be shared within a VISN. How are the level/severity modifiers (SEVERE, MOD and MIN) used in health factors when the health factors are not consistent with such quantification:

A: Here's a little background. The Indian Health Service used the Health Factors originally. The HEAVY, MODERATE, MINIMUM SEVERITY modifiers can be used with a health factor if clinicians wish to define their factors in a manner that makes these modifiers useful. They do not have to be used where they do not make sense.

- AICS allows encounter form designers to include health factors on their encounter forms, with or without these modifiers. The health factors that are checked off by clinicians can be captured via scanning and stored in the V Health Factor file.
- The initial set of health factor entries was defined by Indian Health Service. The SLC IRMFO added additional health factors based on feedback from a supporting clinical team, and the Ambulatory Care EP.
- The Health Summary package has a Health Factor component which showS the latest health factors for each health factor category. If modifiers were collected for the health factors, they would be displayed in this component. The PCE clinical reminders do not use the health factor modifier, though they *do* use the existence of a patient's health factor to modify the reminder criteria.
- The health factor information can be viewed as risk assessment or risk factor data which could provide useful information to guide the clinician as the care giver. For example, the PCE package includes a predefined clinical reminder for determing whether tobacco education needs to be given to the patient. The Health factors distributed with PCE include the Health factor category of TOBACCO and within that category of health factors is a factor for "LIFETIME NON-SMOKER." If a clinician had a patient who never has smoked or used any form of tobacco, the reminder will not come up for the patient if the health factor for "LIFETIME NON-SMOKER" has been captured off the encounter form.
- We expect to learn a lot about what clinicians really would like to do with health factors as the clinicians begin using them with the reminders.

## Device Interface Error Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE Device Interface Error Report lets you look up PCE device interface errors by Error Number, Error Date and Time, Encounter Date and Time, or by Patient Name.

Select PCE Coordinator Menu Option: die PCE Device Interface Error Report

Select one of the following:

ERN Error Number

PDT Processing Date and Time

EDT Encounter Date and Time

PAT Patient Name

Look up PCE device interface errors based on: ERN// Error Number

Enter the beginning error number: (1-4): 1// \[ENTER\]

Enter the ending error number: (1-4): 4// \[ENTER\]

DEVICE: HOME// \[ENTER\] VAX RIGHT MARGIN: 80// \[ENTER\]

May 24, 1996 4:10:05 pm Page 1

PCE Device Interface Error Report

Report based on Error Numbers 1 through 4.

---------------------------------------------------------------

Error Number: 1

Patient: PCEPATIENT,ONE 000-45-6789

Encounter date: May 06, 1996@14:53:17

Processing date: May 06, 1996@16:18:53

File: 9000010.07 (V POV) Field .04 (PROVIDER NARRATIVE)

Error message: Missing Required Fields

Node: 0

Original:

Updated: 2016^1026^^244^^^^^^^^S^^^^20

File: 9000010.07 (V POV) Field .04 (PROVIDER NARRATIVE)

Error message: Missing Required Fields

Node: 0

Original:

Updated: 2016^1026^^244^^^^^^^^S^^^^20

Error Number: 2

Patient: PCEPATIENT,ONE 000-45-6789

Encounter date: May 06, 1996@14:53:17

Processing date: May 06, 1996@16:38:59

File: 9000010.07 (V POV) IEN: 54 Field .04 (PROVIDER NARRATIVE)

Error message: Not Stored = 2X3

Node: 0 *ETC.*

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADCP

Ambulatory Data Capture Project. ADCP was formed to coordinate the various V*IST*A packages involved in meeting this mandate. AICS Automated Information Collection System, formerly Integrated Billing, the program that makes Encounter Forms.

Action

A functional process that a clinician or clerk uses in the PCE computer program. For example, “Update Encounter” is an action that allows the user to pick an encounter and edit information that was previously entered (either through PCE or the PIMS Checkout process), or add new information (such as an immunization or patient education).

Appointment

A scheduled meeting with a provider or at a clinic; can include several encounters with other providers or clinics for tests, procedures, etc.

Automated Service Connected Designation

The Automated Service Connected Designation (ASCD) project automates the Service Connected decision for outpatient encounters using the mapped ICD/Rated Disability Codes at the time the clinician actually picks the ICD code for the outpatient encounter within the Patient Care Encounter (PCE) and Scheduling packages. 

Checkout Process

Part of Medical Administration (the PIMS package), the checkout process can create appointments which are entered into the PCE component.

Clinic

An entry in the HOSPITAL LOCATION File \#44 with a TYPE=”C”. Clinics must have stop codes in compliance with their restriction type. (See: Conforming Clinics; Non-conforming Clinics).

Clinician

A doctor or other provider in the medical center who is authorized to provide patient care.

Conforming Clinics

Clinics that have stop codes in compliance with their restriction types. Stop codes are used in accordance to their assigned restriction types. Stops codes with restriction type 'P' can only be used in the primary stop code position. Stop codes with restriction type 'S' can only be used in the secondary stop code position. Stop codes with restriction type 'E' can be used in either the primary or secondary stop code position.

CPRS

Computerized Patient Record System, a clinical record system which integrates many V*IST*A packages to provide a common entry and data retrieval point for clinicians and other hospital personnel.

CPT

Common Procedure Terminology; a method for coding procedures a performed on a patient, for billing purposes.

CSV

Code Set Versioning. This package is mandated under the Health Information Portability and Accountability Act (HIPAA). It contains routines, globals and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD‑9‑CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, the applications below will allow users of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO)-established specific code that existed on that event date.

Encounter

Each patient meeting with a provider, during an appointment, by telephone, or as a walk-in. A patient can have multiple encounters for one appointment or during a single visit to a VAMC.

Encounter Form

A paper form used to display data pertaining to an outpatient visit and to collect additional data pertaining to that visit. The AICS package is automating encounter forms.

Episode of Care

Many encounters for the same problem can constitute an episode of care. An outpatient episode of care may be a single encounter or can encompass multiple encounters over a long period of time. The definition of an episode of care may be interpreted differently by different professional services even for the same problem. Therefore, the duration of an episode of care is dependent on the viewpoints of individuals delivering or reviewing the care provided.

Health Summary

A Health Summary is a clinically oriented, structured report that extracts many kinds of data from V*IST*A and displays it in a standard format. The individual patient is the focus of health summaries, but health summaries can also be printed or displayed for groups of patients. The data displayed covers a wide range of health-related information such as demographic data, allergies, current active medical problems, laboratory results, etc.

Indian Health Service (IHS)

IHS developed a computer program similar to VA’s V*IST*A, which contains Patient Care Component (PCC) from which PCE and many of its components were derived.

Inpatient Visit

Inpatient encounters include the admission of a patient to a VAMC and any clinically significant change related to treatment of that patient. For example, a treating specialty change is clinically significant, whereas a bed switch is not. The clinically significant visits created throughout the inpatient stay would be related to the inpatient admission visit. If the patient is seen in an outpatient clinic while an Inpatient, this is treated as a separate encounter.

Integrated Billing (IB)

A V*IST*A package responsible for identifying billable episodes of care, creating bills, and tracking the whole billing process through to the passing of charges to Accounts Receivable (AR). Includes the Encounter Form utility.

MCCR

Medical Care Cost Recovery, a V*IST*A entity which supports Integrated Billing and many data capture pilot projects related to PCE.

Non-conforming Clinics

Clinics with stop codes that do not comply with the assigned stop code restriction types of P=Primary, S=Secondary and E=Either.

NPCDB

National Patient Care Data Base, a database maintained in Austin which stores the minimum data set for all ambulatory care encounters.

Occasion of Service

A specified instance of an act of service involved in the care of a patient or consumer which is not an encounter. These occasions of service may be the result of an encounter; for example, tests or procedures ordered as part of an encounter. A patient may have multiple occasions of service per encounter or per visit.

Outpatient Visit

The visit of an outpatient to one or more units or facilities located in or directed by the provider maintaining the outpatient health care services (clinic, physician’s office, hospital/medical center) within one calendar day. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communications with a patient may be represented by a separate visit entry.

Person Class

An enhancement to the New Person file, XU\*8\*27 NEW PERSON File Patch (8/5/96), which enables all VAMC providers to be assigned a Profession/ Occupation code (Person Class) so that a Person Class can be associated with each ambulatory patient encounter by October 1, 1996.

Procedure (CPT)

A test or action done for or to a patient that can be coded with the CPT coding process.

Provider

A person who furnishes health care to a consumer; such as a professionally licensed practitioner who is authorized to operate a health care delivery facility. This definition includes an individual or defined group of individuals who provides a defined unit of health care services (defined = codable) to one or more individuals at a single session.

Stop Code

A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit. Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.

Visit

Each encounter with a provider during a patient’s appointment; can also be a telephone call or a walk-in.

Visit Tracking

A V*ist*A package which links patient-related information in a file structure that allows meaningful reporting and historically accurate categorization of patient events and episodes of care.

V*ist*A

Veterans Information System Technology Architecture

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding and Editing Patient Care Encounters 18
Automated Service Connected Designation (ASCD) 5
Clinical Reminders 73
Definitions 3
Editing the Education Topic file 69
Frequently Asked Questions 130
Functionality of PCE 2
Glossary 135
Health Summary Example 94
Introduction 1
Make Historical Encounter 20
Managing PCE 59
Key Concepts 61
Missing Data Report 128
Orientation 7
PCE Actions 16
PCE and Health Summary 57
PCE Clinical Reports
Caseload Profile by Clinic 104
Diagnosis Ranked by Frequency 112
Location Encounter Counts 125
Patient Activity by Location 100
PCE Encounter Summary 108
Provider Encounter Counts 119
PCE Clinical Reports 98
PCE Code Mapping List 72
PCE Coordinator Menu 60
PCE Data Entry Options 15
PCE HS/RPT Parameter Menu 63
PCE Information Only 70
PCE Information Only Menu 70
PCE IRM Main Menu 59
PCE Menus and Options 59
PCE Site Parameters 62
PCE Site Parameters Edit Example 64
Potential PCE Workflow 4
Purpose and Benefits of PCE 1
Review Screens 8
Screen Display 7
Sources of Data 5
Supplementary Material 129
Table Maintenance 66
Update Encounter
Adding or Editing Directions to Patient's Home 55
Delete an Item 27
Edit an Item 24
How to Add or Edit a CPT (Procedure) 36
How to Add or Edit a Patient Ed 43
How to Add or Edit a Provider 31
How to Add or Edit a Skin Test 44
How to Add or Edit an Encounter 29
How to Add or Edit an Exam 46
How to Add or Edit an Immunization 41
How to Add or Edit Diagnoses (ICD 9) 33
How to Add or Edit Health Factors 48
How to Add or Edit the Checkout Interview 50
How to Add or Edit Treatments 39
Quick Tricks 23
Update Encounter 22
Using PCE 15

# Appendix A - Sample MDR Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An example of the report, sorted by Data Source follows:

Sample MDR Report

By Clinic, Provider, and Date

AUG 8,2004 through NOV 16,2004

Page 1

Patient SSN Date/Time Enc. ID Created by User Defect

OUTPATIENT DIAG (BAY PINES)

Unknown

SORT VALUE: DATA SOURCE= RAD/NUC MED

NOV 03, 2004:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PCEpatient, One 000-00-0001 NOV 03, 2004@14:18 HMX8P-BAY PCEprovider, One Procedure: 73110 missing assoc. DXs

Diagnosis: 171.6 missing Service Conn

Diagnosis: 171.2 missing SC/EI

TOTAL DEFECTS FOR HMX8P-BAY: 1

TOTAL DEFECTS FOR OCT 25, 2004: 1

TOTAL ENCOUNTERS FOR OCT 25, 2004: 1

TOTAL DEFECTS FOR SORT VALUE - RAD/NUC MED: 3

TOTAL ENCOUNTERS FOR SORT VALUE - RAD/NUC MED: 1

TOTAL DEFECTS FOR Unknown: 3

TOTAL ENCOUNTERS FOR Unknown: 1

TOTAL DEFECTS FOR OUTPATIENT DIAG (BAY PINES): 3

TOTAL ENCOUNTERS FOR OUTPATIENT DIAG (BAY PINES): 1

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: ASCD User Manual (Scheduling)

## Automated Service Connected Designation Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Service Connected Designation Menu \[SDSC MENU\] option was added as a module to the Scheduling Manager's Menu \[SDMGR\] option. The menu options for ASCD should be distributed accordingly to personnel responsible for the management and administration of outpatient encounter check-out processing and review.

The ASCD options are as follows:

- ASCD Compile Parameter \[SDSC SITE PARAMETER\]
- ASCD Reports ... \[SDSC REPORTS\]
- Compile ASCD Encounters by Date Range \[SDSC COMPILE\]
- Edit ASCD Encounters by Date Range \[SDSC EDIT BY DATE\]
- Edit ASCD Encounters by ListMan \[SDSC EDIT LISTMAN\]
- Edit Single ASCD Encounter \[SDSC SINGLE EDIT\]
- Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]

### User Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three (3) types of User’s that are recognized and authorized to use the Automated Service Connected Designation Menu \[SDSC MENU\] option:

1.  <u>General Users</u>

    These users are not assigned a security key and can only see and review the encounters with a status of ‘NEW’. They can print the reports, which do not require a security key.
2.  <u>Clinical Reviewers</u>

    These users are assigned the SDSC CLINICAL security key. They can only see and review encounters with a status of ‘REVIEW’. They can print the reports, which do not require a security key.
3.  <u>Supervisors</u>

    These users are assigned the SDSC SUPER security key. They can see and review ALL encounters with a status of ‘NEW’, ‘REVIEW’, and ‘COMPLETED’. This security key should be restricted to only a few users who as supervisors have the ability to undo a change. Supervisors have access to all ASCD options.

### ### ### Automation of Diagnosis Code - (SC)/(NSC) Designation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Care Encounter (PCE) and Scheduling packages outpatient encounter data entry process for entering diagnosis codes has been enhanced to automate the service connected (SC) or non-service connected (NSC) decision-making.

The response to the service connected classification prompt "Was treatment for SC Condition?” has been automated for each diagnosis code entry. The question will not allow user entry and will be displayed briefly to the user with the ASCD answer. However, users can change the ASCD default value for encounters that are not set for review and are not accessible via the ASCD review options via the PCE Encounter Data Entry - Supervisor \[PXCE ENCOUNTER ENTRY SUPER\] option. The next service connected classification prompt will be presented for user input if applicable.

The patient’s mapped RATED DISABILITIES (VBA Code) and ICD9 codes in the DISABILITY CONDITION (#31) file are used to determine the SC/NSC response for outpatient encounters.

The Service Connected Classification status automation uses the following conditions:

- Outpatient Encounters
- Veteran is Service Connected and;
- The encounter eligibility is Service Connected and;
- The clinic is not a non-count clinic.

Encounter Check-out Diagnosis code enter/edit screen Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>Enter Diagnosis</mark> : 200.07</p>
<p>Reticulosarcoma involving spleen (ICD-9-CM 200.07)</p>
<p>Ok? YES// YES Reticulosarcoma involving spleen (ICD-9-CM 200.07)</p>
<p>&gt;&gt;&gt; Code : 200.07</p>
<p>Provider Narrative: RETICULOSARCOMA INVOLVING SPLEEN</p>
<p>RETICULOSARCOMA INVOLVING SPLEEN</p>
<p>Is this Diagnosis Primary for the Encounter: YES//</p>
<p>Is this Diagnosis Ordering, Resulting, or Both: BOTH O&amp;R</p>
<p>Modifier:</p>
<p>Encounter Provider: PCEPROVIDER,ONE// GTS</p>
<p>Is this provider Primary or Secondary? P// PRIMARY</p>
<p>Comments:</p>
<p><mark>Patient's Service Connection and Rated Disabilities:</mark></p>
<p>SC Percent: 75%</p>
<p><mark>Rated Disabilities:</mark> <mark>7014</mark> RAPID PULSE OF THE HEART (20%-SC) ◄ VBA DX CODE - 7014</p>
<p><mark>7706</mark> REMOVAL OF SPLEEN (100%-SC) ◄ VBA DX CODE - 7706</p>
<p>--- <mark>Classification</mark> --- [Required]</p>
<p><mark>Was treatment for SC Condition? NO</mark> ◄ Prompt and response display, no user interaction</p>
<p>Was treatment related to Combat? YES// NO</p>
<p>Was treatment related to Agent Orange Exposure? NO</p>
<p>Was treatment related to Ionizing Radiation Exposure? NO</p>
<p>Was treatment related to Environmental Contaminant Exposure? NO</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The RATED DISABILITY CODE numbers are now displayed before the Rated Disabilities (VA) name as shown above.

The response to the question "Was treatment for SC Condition?" will be automatically set to YES for any of the following conditions:

- The patient has rated disabilities and the encounter diagnosis code is a true match with the at least one diagnosis code associated with the rated disability code(s).
- The patient has rated disabilities and the encounter diagnosis code is a partial match with at least one (1) diagnosis code associated with a rated disability code.
- The patient is service connected with a percentage, but does NOT have any rated disabilities.
- The patient has rated disabilities but they are not mapped to any diagnosis codes.

The response to the question "Was treatment for SC Condition?" will be automatically set to NO for any of the following conditions:

- The patient has rated disabilities but the encounter diagnosis code does NOT match any of the diagnosis codes associated with the rated disabilities.
- If patient has multiple rated disabilities (mapped and not mapped) and the encounter diagnosis code does not match a diagnosis for the mapped rated disability.

## Compiling Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ASCD Compile Parameter \[SDSC SITE PARAMETER\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASCD Compile Parameter \[SDSC SITE PARAMETER\] menu option is used to set the number of days that the manual ‘Compile ASCD Encounters by Date Range’ \[SDSC COMPILE\] option will use as a start date when searching for outpatient encounters that may need additional review by the ASCD software. This value is also used in the ‘Compile Results Report’ \[SDSC CHECK COMPILE\] and ‘Manager Summary Report’ \[SDSC MANAGER SUMMARY REPORT\] to validate the beginning date.

The site parameter is set to 30 days when the SD\*5.3\*495 patch is installed. This option is LOCKED by the SDSC SUPER security key.

ASCD Compile Parameter Example

------------- Setting SDSC SITE PARAMETER for Division: ALBANY -------------

DAYS: 30//

### Compile ASCD Encounters by Date Range \[SDSC COMPILE\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gathers encounters that have been updated or encounters with late identified insurance by performing a search on the OUTPATIENT ENCOUNTER file (#409.68).

The start date of the compile is based on the number of days defined by the Site Parameter Definition \[SDSC SITE PARAMETER\] and is ran for a user specified date range. The option uses the rules listed under ‘Automation of Diagnosis Code: SC/NSC Designation’ to determine if the encounter should be added to the review file. This option can be run real-time or scheduled for a later time.

This option also purges and reports those records from the SDSC SERVICE CONNECTED CHANGES file (#409.48) when corresponding records do not exist in the OUTPATIENT ENCOUNTER file (#409.68).

The compile will NOT select any outpatient encounters where the patient does not have any 3rd party insurance.

- However, if auditing has been turned on for certain fields in the Patient File (#2); field .3192 COVERED BY HEALTH INSURANCE? and field .01 INSURANCE TYPE of the INSURANCE TYPE subfile (#.3121), the compile will check to see if above-mentioned fields have recently been changed to YES or a new insurance company has been added.

All outpatient encounters within a 24 month range will be checked for late identified insurance to see if there are any SC encounters which potentially may not be SC and may now be billable due to the addition of active insurance.

After completion of the compile, a MailMan message containing the results will be sent to members of the mail group, SDSC NIGHTLY TALLY.

MailMan Message Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ASCD Compile Numbers [#2012538] 02/20/07@15:48 20 lines</p>
<p>From: ASCD COMPILE In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>Date Range (Compile) - From: Feb 19, 2007 Thru: Feb 19, 2007</p>
<p>Date Range (Late Ins.) - None</p>
<p>Number of encounters Service Connected (Compile) : 0</p>
<p>Number of encounters Service Connected (Late Ins.) : 0</p>
<p>(Number SvcConn with a True Map) : 0</p>
<p>(Number SvcConn with a Partial Map) : 0</p>
<p>(Number SvcConn that don't Map to VBA) : 0</p>
<p>Number of encounters Not Service Connected : 0</p>
<p>Number of encounters that are Non-billable : 26</p>
<p>Number of encounters with Non-count Clinics : 2</p>
<p>Number of encounters with no diagnoses : 0</p>
<p>Number of encounters with other errors : 0</p>
<p>Number of encounters already evaluated : 30</p>
<p>---------------------------------------------------------------------------</p>
<p>Total Encounters Checked: 58</p>
<p>ASCD Late Insurance Check:</p>
<p>Auditing is not turned on for field COVERED BY HEALTH INSURANCE?</p>
<p>Auditing is not turned on for field INSURANCE TYPE</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Reviewing Encounters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Criteria for Flagging Encounters for Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The service connected status is automatically determined within Scheduling and PCE upon entry of the diagnosis if the encounter is SC eligible. Certain encounters are sent to the ASCD review file (#409.48) after all diagnosis codes have been entered for the encounter and it has been checked out. The following criteria is used to determine if the encounter will be sent for additional review.

The encounter WILL need additional review based on the following conditions:

- The patient has rated disabilities and one of the encounter diagnosis codes is a partial match with at least one (1) diagnosis code associated with a rated disability code.
- The patient is service connected with a percentage, but does NOT have any rated disabilities.
- The patient has rated disabilities but the entered encounter diagnosis codes do NOT match any diagnosis code associated with the rated disabilities.
- The patient has rated disabilities on file but they are not mapped to any diagnosis code at all.
- The patient has rated disabilities and the encounter *secondary* diagnosis code is a true match with a rated disability code.

The encounter WILL NOT need additional review based on the following conditions:

- The patient is non-billable for 1<sup>st</sup> and 3<sup>rd</sup> party.
- The patient has rated disabilities and the encounter *primary* diagnosis code is a true match with a rated disability code(s).

  A user with the PCE ENCOUNTER DATA ENTRY-SUPERVISOR option will have the ability to change the service connected value during data entry. ASCD will compute the SC value and it will be presented as a default. This option can be used to edit those encounters that are not sent for review.

#### Ancillary Package Encounters

Any outpatient encounter record sent to the Patient Care Encounter (PCE) system from an ancillary package for workload reporting will be reviewed using the same criteria detailed above.

However, it should be noted:

- Encounters will be flagged for review when the ASCD value is a true match but the originating value does not match the ASCD value.
- The original SC value will NOT change but the encounter will be flagged for additional review if the original SC value is different from the ASCD evaluation value.
- Ancillary packages will NOT be updated if value is changed after ASCD review. The following message will be displayed to users when they access an encounter that originated from an ancillary package:

> ► WARNING: This encounter came from another package. If it is changed it will not agree with what is in the originating package.

PLEASE NOTE: CPRS will be updated if SC/NSC value is changed after ASCD review.

#### Records Removed from the SDSC SERVICE CONNECTED CHANGES File (#409.48) 

Any outpatient encounter record that has been reviewed and was updated by adding a primary diagnosis code that has a true match with one of the patient’s rated disabilities will be deleted from the SDSC SERVICE CONNECTED CHANGES file (#409.48).

### Edit ASCD Encounters by Date Range \[SDSC EDIT BY DATE\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to review ASCD encounters one record at a time within a selected date range. The user will select encounters for a date range by division(s) and can choose to display only SC or NSC or all encounters they need to review.

Security Keys:

- SDSC SUPER users can review and edit encounters with a status of NEW, REVIEW and COMPLETED.
- SDSC CLINICAL users can review and edit encounters with a status of REVIEW.
- General users can review and edit encounters with a status of NEW.

For each encounter found the user may choose one of the following actions -

- Y (YES) to modify this encounter's Service Connected value. This enables the user

> to edit the diagnosis code(s) and change the value for the SC questions,

> where applicable. NOTE: *In order to set an encounter with multiple diagnoses to NSC and mark it as billable, ALL diagnoses would need to be changed to NO.*

- N (NO) to retain this encounter's Service Connected value. NO allows the user to

> accept the original SC determination entered for this encounter.

- S (SKIP) to skip this encounter and review it later. SKIP allows the user to move on

> to the next encounter to be edited. The skipped encounter will still be

> available for review at a later date.

- R (REVIEW) to flag this encounter for clinical review. REVIEW enables the user to

> send the encounter back to a clinical reviewer if the decision cannot easily

> be made as to whether this encounter is truly service connected or not.

Edit Encounter by Date Range Screen Display Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Automated Service Connected Designation Menu Option: EDIT</p>
<p>1 Edit ASCD Encounters by Date Range</p>
<p>2 Edit ASCD Encounters by ListMan</p>
<p>3 Edit Single ASCD Encounter</p>
<p>CHOOSE 1-3: 1 Edit ASCD Encounters by Date Range</p>
<p>Service Connected Encounters Review Selection</p>
<p>Select one of the following:</p>
<p>S Service Connected</p>
<p>N Non-Service Connected</p>
<p>A All</p>
<p>Which type do you want to review?: S// ervice Connected</p>
<p>Please enter START date: 05252007 (MAY 25, 2007)</p>
<p>Please enter END date: Jun 07, 2007// (JUN 07, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p>
<p>PMS,ONE (0001)</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>------------------------------------------------------------------------------</p>
<p>Encounter 2688352 is NOT marked as service connected.</p>
<p>Date of Encounter: 12/04/2006@10:00</p>
<p>Location: TELE-MH GREELEY/VETERAN</p>
<p>Primary Provider: PROVIDER,PRIMARY</p>
<p>Patient: PMS,ONE (0001) *SENSITIVE*</p>
<p>Patient is copay eligible.</p>
<p>Patient is not insured.</p>
<p>ASCD Evaluation: SC (no ICD9 match)</p>
<p>POVs/ICDs:</p>
<p>*SC* 380.15 CHR MYCOT OTITIS EXTERNA</p>
<p>780.6 FEVER</p>
<p>Rated Disabilities:</p>
<p>5209 ELBOW CONDITION (55%-SC)</p>
<p>6210 AUDITORY CANAL DISEASE (50%-SC)</p>
<p><mark>DO YOU WANT TO CHANGE THE SERVICE CONNECTION FOR THIS ENCOUNTER?</mark> <mark>?</mark></p>
<p>Enter:</p>
<p>'YES' to modify this encounter's Service Connected statuses.</p>
<p>'NO' to retain this encounter's Service Connected statuses.</p>
<p>'SKIP' to skip this encounter and review it later.</p>
<p>'REVIEW' to flag this encounter for clinical review.</p>
<p>Select one of the following:</p>
<p>Y YES</p>
<p>N NO</p>
<p>S SKIP</p>
<p>R REVIEW</p>
<p>DO YOU WANT TO CHANGE THE SERVICE CONNECTION FOR THIS ENCOUNTER? <mark>Y</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

(Continued…)

<span class="mark">PAT/APPT/CLINIC: PMS,ONE (0001) 12/04/2006@10:00 TELE-MH REELEY/VETERAN</span>

ICD CODE: ...There are 2 ICD CODES associated with this encounter.

<span class="mark">- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -</span>

<span class="mark">No. ICD DESCRIPTION PROBLEM LIST</span>

1 380.15 CHR MYCOT OTITIS EXTERNA <span class="mark">PRIMARY</span> ORDERING

SC:Y CV:NAO:NIR:NEC:N

2 780.6 FEVER RESULTING

SC:N CV:NAO:NIR:NEC:N

Enter Diagnosis : 1

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES//

Select one of the following:

O ORDERING

R RESULTING

OR BOTH O&R

Is this Diagnosis Ordering or Resulting:: // OR BOTH O&R

Patient's Service Connection and Rated Disabilities:

SC Percent: 60%

Rated Disabilities: 5209 ELBOW CONDITION (55%-SC)

6210 AUDITORY CANAL DISEASE (50%-SC)

--- <span class="mark">Classification</span> --- <span class="mark">\[Required\]</span>

Was treatment for SC Condition? YES// <span class="mark">NO</span> ◄ <span class="mark">Changed here</span>

Was treatment related to Combat? Yes// NO

Was treatment related to Agent Orange Exposure? NO

Was treatment related to Ionizing Radiation Exposure? NO

Was treatment related to Environmental Contaminant Exposure? NO

Enter <span class="mark">NEXT</span> Diagnosis :

Would you like to add any Diagnosis to the Problem List? NO//

\- - - - S o r y A b o u t T h e W a i t - - - -

This information is being stored or monitored by Scheduling

Integrated Billing, Order Entry, Registration, Prosthetics

PCE/Visit Tracking and Automated Med Information Exchange.

Performing Ambulatory Care Validation Checks.

No validation errors found!

(Continued…)

<span class="mark">PAT/APPT/CLINIC: PMS,ONE (0001) 12/04/2006@10:00 TELE-MH REELEY/VETERAN</span>

ICD CODE: ...There are 2 ICD CODES associated with this encounter.

<span class="mark">- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -</span>

<span class="mark">No. ICD DESCRIPTION PROBLEM LIST</span>

1 380.15 CHR MYCOT OTITIS EXTERNA <span class="mark">PRIMARY</span> ORDERING

SC:<span class="mark">N</span> CV:NAO:NIR:NEC:N

2 780.6 FEVER RESULTING

SC:N CV:NAO:NIR:NEC:N

Enter NEXT Diagnosis :

Would you like to add any Diagnoses to the Problem List? NO//

\- - - - S o r y A b o u t T h e W a i t - - - -

This information is being stored or monitored by Scheduling

Integrated Billing, Order Entry, Registration, Prosthetics

PCE/Visit Tracking and Automated Med Information Exchange.

Performing Ambulatory Care Validation Checks.

No validation errors found!

### Edit ASCD Encounters by ListMan \[SDSC EDIT LISTMAN\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to review multiple ASCD encounters for the selected date range and division(s), as well as the ability to choose which type they would like to display. This option displays the encounters using VistA List Manager format. The various types of encounter statuses displayed will be based on the security key assigned to the user (See section on ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\] for security keys).

Edit Encounter by Date Range Screen Display Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Automated Service Connected Designation Menu Option: EDIT</p>
<p>1 Edit ASCD Encounters by Date Range</p>
<p>2 Edit ASCD Encounters by ListMan</p>
<p>3 Edit Single ASCD Encounter</p>
<p>CHOOSE 1-3: 2 Review Encounters screen display List Manger Example:</p>
<p>Service Connected Encounters Review Selection</p>
<p>Select one of the following:</p>
<p>S Service Connected</p>
<p>N Non-Service Connected</p>
<p>A All</p>
<p>Which type do you want to review?: S// ervice Connected</p>
<p>Please enter START date: 05252007 (MAY 25, 2007)</p>
<p>Please enter END date: Jun 07, 2007// (JUN 07, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Continued: ListMan Display of Encounters Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>ASCD Jan 26, 2007@11:14:07 Page: 1 of 1</mark></p>
<p>The Service Connected status needs to be reviewed for the following encounters.</p>
<p>Selected Date Range: Oct 20, 2006 - Apr 04, 2007</p>
<p><mark>Encounter Enc Date Patient Status</mark></p>
<p>1 2688352 12/04/2006 PMS,ONE (0001) NEW</p>
<p>2 2688333 11/15/2006 PMS,TWO (0002) NEW</p>
<p>3 2688340 11/15/2006 PMS,THREE (0003) REVIEW</p>
<p>4 2688342 11/15/2006 PMS,FOUR (0004) REVIEW</p>
<p>5 2688346 12/01/2006 PMS,FIVE (0005) COMPLETED</p>
<p>6 2688344 12/05/2006 PMS,SIX (0006) COMPLETED</p>
<p>7 2688358 12/05/2006 PMS,SEVEN (0007) COMPLETED</p>
<p><mark>+ Enter ?? for more actions</mark></p>
<p>Review Encounter</p>
<p>Select Item(s): Next Screen// REV Review Encounter</p>
<p>Select Number to Review: (1-7): <mark>1 &lt;return&gt;</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Continued: Review Encounter Detail Display Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>Encounter Detail Apr 04, 2007@16:58:12 Page: 1 of 0</mark></p>
<p>Encounter 2688352 is NOT marked as service connected.</p>
<p>Date of Encounter: 12/04/2006@10:00</p>
<p>Location: TELE-MH GREELEY/VETERAN</p>
<p>Primary Provider: PROVIDER,PRIMARY</p>
<p>Patient: PMS,ONE (0001) *SENSITIVE*</p>
<p>Patient is copay eligible.</p>
<p>Patient is not insured.</p>
<p>ASCD Evaluation: SC (no ICD9 match)</p>
<p>POVs/ICDs:</p>
<p>*SC* 380.15 CHR MYCOT OTITIS EXTERNA</p>
<p>780.6 FEVER</p>
<p>Rated Disabilities:</p>
<p>5209 ELBOW CONDITION (55%-SC)</p>
<p>6210 AUDITORY CANAL DISEASE (50%-SC)</p>
<p><mark>Enter ?? for more actions</mark></p>
<p><mark>YES Modify SvcConnected Status</mark></p>
<p><mark>NO Retain SvcConnected Status</mark></p>
<p><mark>REV Flag for Clinical Review</mark></p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** For each encounter reviewed, users can choose one of three actions as described under the section ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\] option.

### Edit Single ASCD Encounter \[SDSC SINGLE EDIT\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to edit ASCD encounters one record at a time. User can enter a specific encounter \# , status or patient name. If patient name is entered, then a list of all encounters will be displayed for that patient.

The following user prompt is presented:

> Select OUTPATIENT ENCOUNTER:

For each encounter reviewed, users can choose one of three actions as described under the section ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\].

### Updates to Claims Tracking (Billing) After Encounter is Reviewed via ASCD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the SC/NSC determination is changed and if the encounter is already defined in Claims Tracking then the encounters Claims Tracking Entry is updated.

> ► The Reason Not Billable (RNB) of SC TREATMENT is either added or removed.

- If the encounter changed from NSC to SC and there is no RNB, then SC TREATMENT is added as the RNB.
- If the encounter changed from SC to NSC and the RNB is SC TREATMENT then its deleted.

> ► The Last Reviewed By is set to the ASCD user.

> ► The Billable Finding is set to either 'NSC TO SC' or 'SC TO NSC'.

If the encounter is not already in Claims Tracking then it will be added with the correct/update SC/NSC information from PCE when it is added.

PLEASE NOTE: Changing a patient’s status from Non-Service Connected (NSC) to Service Connected (SC) needs to be monitored to ensure any newly SC designated care has not been billed. If SC care has been billed, the bill needs to be cancelled.

### Compile ASCD Encounters on a Nightly Basis \[SDSC NIGHTLY COMPILE\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gathers encounters that have been updated or encounters with late identified insurance by performing a search on the OUTPATIENT ENCOUNTER file (#409.68). ONLY the previous day encounter records are searched.

This option is NOT interactive and must be scheduled to run daily. It is highly recommended you schedule the option after installing the ASCD software. This option is similar to the Compile ASCD Encounters by Date Range \[SDSC COMPILE\] Option.

### Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will purge ASCD encounters with a status of NEW where the encounter SC value equals the ASCD value of "NO" for a specified division(s) within a user specified date range.

Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. User may choose to print the report to a device so as to have a record of the encounters deleted. Users must have the SDSC SUPER key to run this option.

Purge ASCD NSC Encounters Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Please enter START date: 101106 (OCT 11, 2006)</p>
<p>Please enter END date: Jun 11, 2007// (JUN 11, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p>
<p>This option will permanently remove the outpatient encounters that are at a</p>
<p>NEW status when both the Encounter SC value and the ASCD value are 'NO' from</p>
<p>the SDSC SERVICE CONNECTED CHANGES file (#409.48).</p>
<p>Are you sure you want to continue? N// YES</p>
<p>DEVICE: HOME// UCX/TELNET Right Margin: 80//</p>
<p>Purge ASCD NSC Encounters PAGE: 1</p>
<p>For Encounters Dated 10/11/06 THRU 6/11/07 For Division: ALL</p>
<p>Encounter Date Encounter No. Patient Name Provider SC Val</p>
<p>-------------------------------------------------------------------------------</p>
<p>10/11/06@09:00 22148 PATIENT,ONE PROVIDER,ONE NO</p>
<p>11/8/06@08:00 22185 PATIENT,TWO PROVIDER,TWO NO</p>
<p>11/14/06@08:00 22189 PATIENT,TWO PROVIDER,ONE NO</p>
<p>12/7/06@08:30 22194 PATIENT,FOUR PROVIDER,SIX NO</p>
<p>12/13/06@10:00 22204 PATIENT,TEN PROVIDER,NINE NO</p>
<p>12/18/06@08:00 22206 PATIENT,TWENTY PROVIDER,EIGHT NO</p>
<p>Number of NSC Records Purged: 6 for ALL</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ASCD Reports \[SDSC REPORTS\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains all the reports related to the Automated Service Connected Designation module. All reports are accessible to users except the Manager Summary Report. This report is locked by the SDSC SUPER security key.

- ASCD Reports ... \[SDSC REPORTS\]
- Clinic Service Total Summary Report \[SDSC SERVICE TOTAL REPORT\]
- Compile Results Report \[SDSC CHECK COMPILE\]
- Estimated Recovered Costs Report \[SDSC RECOVERED REPORT\]
- First Party Billable Service Connected Report \[SDSC FIRST PARTY REPORT\]
- Manager Summary Report \[SDSC MANAGER SUMMARY REPORT\]
- Provider Service Connected Encounters Report \[SDSC PROVIDER REPORT\]
- Provider Total Summary Report \[SDSC PROVIDER TOTAL REPORT\]
- Service Connected Encounters Report \[SDSC ENC REPORT\]
- Third Party Billable Service Connected Report \[SDSC THIRD PARTY REPORT\]
- Unbilled/Billable Amount Report \[SDSC UNBILL AMT REPORT\]
- User Service Connected Encounters Report \[SDSC USER REPORT\]
- User Total Summary Report \[SDSC USER TOTAL REPORT\]

#### Clinic Service Total Summary Report \[SDSC SERVICE TOTAL REPORT\] 

This report prints the service connected changes by clinical service, M:MEDICINE; S:SURGERY; P:PSYCHIATRY; R:REHAB MEDICINE; N:NEUROLOGY; 0:NONE, under the following categories per that clinic service.

- Number of outpatient encounters where ASCD automatically matched the encounter diagnosis with at least one (1) diagnosis code associated with the patient’s rated disability codes (partial match) - VBA OK.
- Number of outpatient encounters set to Clinical Review - REVIEW
- Number of outpatient encounters marked as ‘Service Connected=YES’ but were changed to ‘Service Connected =NO’ - SC to NSC.
- Number of outpatient encounters marked as ‘Service Connected=NO’ but were changed to ‘Service Connected=YES’ – NSC to SC.
- Number of outpatient encounters marked as ‘Service Connected=YES’ or ‘Service Connected = No’ that were not changed.- SC KEPT.
- Number of outpatient encounters marked as ‘NEW’, which have not been reviewed yet.

Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. They will also able to select one or more clinical service(s).

Clinic Service Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Service Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 12/16/06 THRU 3/26/07 For Service: ALL</p>
<p>VBA OK REVIEW SC to NSC NSC to SC SC KEPT NEW</p>
<p>-------------------------------------------------------------------------------</p>
<p>MEDICINE</p>
<p>CLINIC ONE 0 1 0 0 1 10</p>
<p>MEDICINE SWO 0 0 0 0 0 1</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>Subtotal MEDICINE 0 1 0 0 1 11</p>
<p>SURGERY</p>
<p>BU-GEN SURG RAINSTEI 0 0 0 0 0 5</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>Subtotal SURGERY 0 0 0 0 0 5</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>TOTAL 0 1 0 0 1 16</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Compile Results Report \[SDSC CHECK COMPILE\] 

This report prints the reasons why encounters were not compiled into the SDSC SERVICE CONNECTED CHANGES file (#409.48). For a given date range, users can choose from a summary or detail format. The start date of the report is based on the value defined for the SDSC Site Parameter. The Detail reports provide the same information as the summary and additional information on only those encounters with diagnosis code related reasons.

Compile Results Report – (Summary) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Compile Results Report – Summary PAGE: 1</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p># Enc Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>1 A diagnosis fully matched a rated disability condition</p>
<p>3 No Diagnoses for this encounter</p>
<p>-------------------------------------------------------------------------------</p>
<p>4 TOTAL Encounters</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Compile Results Report – (Detail) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Compile Results Report – Summary PAGE: 1</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p># Enc Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>1 A diagnosis fully matched a rated disability condition</p>
<p>3 No Diagnoses for this encounter</p>
<p>-------------------------------------------------------------------------------</p>
<p>4 TOTAL Encounters</p>
<p>Compile Results Report - Detail</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p>Enc # Visit # Clinic Encounter Date/Time Patient Name</p>
<p>Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>2688336 2361624 CLINIC ONE 11/15/2006@09:00 PMS,ONE</p>
<p>A diagnosis fully matched a rated disability condition</p>
<p>2688337 2361625 CLINIC TWO 11/15/2006@09:00 PMS,TWO</p>
<p>No Diagnoses for this encounter</p>
<p>2688341 2361629 CLINIC THREE 11/15/2006@11:00 PMS,THREE</p>
<p>No Diagnoses for this encounter</p>
<p>2688343 2361631 CLINIC FOUR 11/15/2006@13:00 PMS,FOUR</p>
<p>No Diagnoses for this encounter</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Estimated Recovered Costs Report \[SDSC RECOVERED REPORT\] 

This report prints bills and payments for outpatient encounters where the Service Connected value has been changed from SC to NSC using the ASCD options.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. The report requires a 132 column format.

The Estimated Recovered Cost Report may not accurately reflect payments and reimbursements. One problem is due to the fact that the system can bill several outpatient co-payment charges on the same receivable in AR. Payments are applied to the outstanding balance of the receivable, not to specific charges that compose the receivable. So there is the possibility that there will be multiple encounters where the "Principal Bill" amount will be less than the "Principal Pay" amount. In addition, the Total First Party (paid) amount will be overstated, because there is the chance of counting the payment on a receivable more than once.

Estimated Recovered Costs Report Example:

Estimated Recovered Costs Report by Division: ALL Run Date: Oct 28, 2005@13:41:48 Page 1

Enc \# Patient Enc Date Change Date Auth Date Pay Date Prncpl Bill Prncpl Pay

------------------------------------------------------------------------------------------------

3514166 PMS,ONE (0001) 01/07/2004 09/23/2004 09/23/2004 15.00 0.00

------------------------------------------------------------------------------------------------

TOTAL FIRST PARTY: 15.00 0.00

3507193 PMS,TWO (0002) 01/02/2004 01/22/2004 350.13 0.00

3507266 PMS,THREE (0003) 01/02/2004 01/17/200 01/27/2004 46.73 22.38

3508792 PMS,FOUR (0004 ) 01/05/2004 09/23/2004 01/16/2004 94.47 0.00

3509818 PMS,FIVE (0005) 01/05/2004 09/23/2004 01/13/2004 02/02/2004 39.72 7.94

3510085 PMS,SIX (0006) 01/05/2004 01/10/2004 69.52 0.00

3511104 PMS,SEVEN (0007) 01/06/2004 09/23/2004 02/10/2004 46.73 0.00

-------------------------------------------------------------------------------------------------

THIRD PARTY TOTAL: 647.30 30.32

------------------------------------------------------------------------------------------------

TOTAL FOR BOTH: 662.30 30.32

TOTAL PAGE FOR 3 DIVISIONS

Estimated Recovered Costs Report by Division(s): KINGMAN CBOC,LAKE HAVASU CITY,COTTONWOOD,

Run Date: Oct 28, 2005@13:42:30 Page 2

Prncpl Bill Prncpl Pay

--------------------------------------------------------------------------------------------

FIRST PARTY TOTAL

COTTONWOOD 0.00 0.00

KINGMAN CBOC 0.00 0.00

LAKE HAVASU CITY 0.00 0.00

---------------------------------------------------------------------------------------------

THIRD PARTY TOTAL

COTTONWOOD 0.00 0.00

KINGMAN CBOC 46.73 22.38

LAKE HAVASU CITY 94.47 0.00

---------------------------------------------------------------------------------------------

TOTAL FOR BOTH FIRST AND THIRD PARTY

141.20 22.38

#### First Party Billable Service Connected Report \[SDSC FIRST PARTY REPORT\] 

This report prints information on any outpatient encounters that are potentially billable to first party (means test).

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

First Party Billable Service Connected Report Example:

OUTPATIENT ENCOUNTERS POTENTIALLY BILLABLE FOR CO-PAYS PAGE: 1

FOR ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

DATE PATIENT ENCOUNTER

01/07/2004@10:00 PMS,ONE (0001) 3514166

01/09/2004@13:00 PMS,TWO (0002) 3518457

\<End of Report\>

#### Manager Summary Report \[SDSC MANAGER SUMMARY REPORT\] 

This report prints totals for the following information pertaining to the ASCD outpatient encounters:

- \# of checked out encounters
- ASCD encounters that are potentially billable
- Encounters with rated disability codes
- SC was NOT changed
- Changed from SC to NSC
- Changed from NSC to SC
- Clinical Review
- Not editable
- Not yet processed

The report can be printed for a specified date range for one or more divisions and will search through ‘All’ checked out outpatient encounters or just the ‘Compiled ASCD Encounters Only’. Users provide a start date, which cannot be greater than the value defined for the SDSC Site Parameter. The end date can be any date beginning with the start date through current date. This report is LOCKED by the SDSC SUPER security key.

Managers Summary Report – (All) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Managers Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 For Division: ALL</p>
<p>------------------------------------------------------------------------------</p>
<p>All Checked Out Encounters: 57</p>
<p>ASCD Encounters that are potentially billable: 56</p>
<p>-------</p>
<p>Encounters verified with Rated Disability Codes: 28</p>
<p>Encounters where SC NOT changed: 4</p>
<p>Encounters where SC was changed to NSC: 0</p>
<p>Encounters where NSC was changed to SC: 1</p>
<p>Encounters sent to Clinical Review: 2</p>
<p>Encounters not editable: 0</p>
<p>Encounters not yet processed: 21</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Managers Summary Report – (Compiled) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Managers Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 For Division: ALL</p>
<p>-------------------------------------------------------------------------------</p>
<p>ASCD Encounters that are potentially billable: 56</p>
<p>-------</p>
<p>Encounters verified with Rated Disability Codes: 28</p>
<p>Encounters where SC NOT changed: 4</p>
<p>Encounters where SC was changed to NSC: 0</p>
<p>Encounters where NSC was changed to SC: 1</p>
<p>Encounters sent to Clinical Review: 2</p>
<p>Encounters not editable: 0</p>
<p>Encounters not yet processed: 21</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Provider Service Connected Encounters Report \[SDSC PROVIDER REPORT\] 

This report prints information regarding ASCD outpatient encounters and it is sorted by the primary provider for the encounter/visit.

The report can be printed using either a summary or detail format within a specified date range and one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

\* The ‘VBA SC’ column refers to whether any encounter diagnosis was matched to a diagnosis code associated with a rated disability code. Values are ‘YES’ or ‘NO’.

\*\* The ‘User SC’ column refers to the user assigned service connected value for an encounter based upon their review of the encounter. Values are ‘YES’, ‘NO’, or ‘TBD (to be determined)’.

Provider Service Connected Encounters Report – (Summary) Example:

> OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY PROVIDER PAGE: 1

> FOR ENCOUNTERS DATED 11/15/06 THRU 12/15/06 By Division: ALL

> ENCOUNTER DATE PATIENT NAME ENC \# VBA SC USER SC

> PROVIDER,ONE

> 11/15/2006@08:00 PMS,ONE(0001) 2688333 YES NO

> 11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

> 11/15/2006@13:00 PMS,THREE(0003) 2688342 YES NO

> Total: 3

> 11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

> 11/15/2006@13:00 PMS,THREE(0003) 2688342 YES NO

> Total: 3

> \<End of Report\>

Provider Service Connected Encounters Report – (Detail) Example:

OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY PROVIDER PAGE: 1

FOR ENCOUNTERS DATED 11/15/06 THRU 12/15/06 By Division: ALL

ENCOUNTER DATE PATIENT NAME ENC \# VBA SC USER SC

PROVIDER,ONE

11/15/2006@08:00 PMS,ONE (0001) 2688333 YES NO

POVs/ICDs:

780.6 FEVER

460\. ACUTE NASOPHARYNGITIS

Rated Disabilities:

7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

7913 DIABETES MELLITUS (20%-SC)

6013 GLAUCOMA (10%-SC)

6260 TINNITUS (10%-SC)

11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

POVs/ICDs:

780.6 FEVER

Rated Disabilities:

7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

7913 DIABETES MELLITUS (20%-SC)

6013 GLAUCOMA (10%-SC)

6260 TINNITUS (10%-SC)

Total: 2

\<End of Report\>

#### #### #### Provider Total Summary Report \[SDSC PROVIDER TOTAL REPORT\] 

This report prints totals of the ASCD encounters for the categories listed below per each provider:

- Number of outpatient encounters where ASCD automatically matched the encounter diagnosis with at least one (1) diagnosis associated patient’s rated disability codes (partial match) - VBA OK.
- Number of outpatient encounters marked as ‘Service Connected=YES’ but were changed to ‘Service Connected =NO’ - SC to NSC.
- Number of outpatient encounters marked as ‘Service Connected=NO’ but were changed to ‘Service Connected=YES’ – NSC to SC.
- Number of outpatient encounters marked as ‘Service Connected=YES’ or ‘Service Connected = No’ that were not changed.- SC KEPT.
- Number of outpatient encounters marked as ‘NEW’, which have not been reviewed yet.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Provider Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Provider Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 2/18/07 THRU 3/20/07 By Division: ALL</p>
<p>VBA OK SC to NSC NSC to SC SC KEPT NEW</p>
<p>-------------------------------------------------------------------------------</p>
<p>PROVIDER,ONE 0 0 0 0 2</p>
<p>------- ------- ------- ------- -------</p>
<p>TOTAL 0 0 0 0 2</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### #### Service Connected Encounters Report \[SDSC ENC REPORT\] 

This report prints details of the current status of each outpatient encounter found in the SDSC SERVICE CONNECTED CHANGES file (#409.48).

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Service Connected Encounters Report – (All) Example:

O/P ENCOUNTERS THAT ARE SERVICE CONNECTED & NON SERVICE CONNECTED PAGE: 1

ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

DATE PATIENT ENCOUNTER SC VALUE

10/04/2006@11:00 PIMS,SERCONVET RD (5434) 2688296 YES

POVs/ICDs:

V72.6 LABORATORY EXAMINATION

Rated Disabilities:

7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

7913 DIABETES MELLITUS (20%-SC)

6013 GLAUCOMA (10%-SC)

6260 TINNITUS (10%-SC)

10/04/2006@12:42 PMS,SC VET (7388) 2688291 NO

POVs/ICDs:

345.10 GEN CNV EPIL W/O INTR EP

355.8 MONONEURITIS LEG NOS

244.9 HYPOTHYROIDISM NOS

Rated Disabilities:

8045 TRAUMATIC BRAIN DISEASE (40%-SC)

5296 LOSS OF PART OF SKULL (10%-SC)

8045 TRAUMATIC BRAIN DISEASE (10%-SC)

\<End of Report\>

#### Third Party Billable Service Connected Report \[SDSC THIRD PARTY REPORT\] 

This report prints information on any ASCD encounters that are potentially billable to third party (insurance).

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Third Party Billable Service Connected Report Example:

OUTPATIENT ENCOUNTERS POTENTIALLY BILLABLE TO INSURANCE PAGE: 1

FOR ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

DATE PATIENT ENCOUNTER

01/05/2004@08:00 PMS, ONE (0001) 3508792

01/05/2004@08:30 PMS, TWO (0002) 3508961

01/05/2004@13:00 PMS, THREE (0003) 3510196

01/05/2004@13:30 PMS, FOUR(0004) 3509818

\<End of Report\>

#### #### Unbilled/Billable Amount Report \[SDSC UNBILL AMT REPORT\] 

This report prints Billing information for reviewed ASCD encounters ONLY, whose SC value was changed from ‘SC’ to ‘NSC’ and have not yet billed or whose SC value was changed from ‘NSC’ to ‘SC’, which have already been billed. Users holding the SDSC SUPER key will have the ability to print the Supervisor report, which prints the names of the last two editors of the ASCD encounter record.

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Unbilled/Billable Amount Report – (Regular) – (NSC to SC) Example:

Unbilled/Billable Amount Report – (Supervisor) – (SC to NSC) Example:

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### User Service Connected Encounters Report \[SDSC USER REPORT\] 

This report prints details or a summary of ASCD encounters sorted by the user who last edited the service connection information for the encounter.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

User Service Connected Encounters Report – (Summary) Example:

OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY USER PAGE: 1

FOR ENCOUNTERS DATED 1/2/04 THRU 3/1/04 By Division: ALL

ENCOUNTER DATE ENC \# VBA SC USER SC STATUS DATE LAST EDITED

PMS, ONE

01/02/2004@09:15 3507237 NO NO COMPLETED OCT 04, 2005

01/02/2004@09:40 3507200 NO NO COMPLETED OCT 28, 2005

01/02/2004@10:00 3507193 NO NO COMPLETED OCT 12, 2005

01/02/2004@10:00 3507266 NO NO COMPLETED OCT 13, 2005

01/02/2004@15:15 3507936 NO NO COMPLETED OCT 13, 2005

01/05/2004@08:00 3508792 NO NO COMPLETED OCT 13, 2005

01/05/2004@08:30 3508961 NO NO COMPLETED OCT 13, 2005

01/05/2004@08:30 3510088 NO NO COMPLETED OCT 28, 2005

01/05/2004@13:00 3510196 NO NO COMPLETED OCT 13, 2005

01/05/2004@13:00 3510326 NO NO COMPLETED OCT 04, 2005

01/05/2004@14:00 3509857 NO NO COMPLETED OCT 13, 2005

01/05/2004@14:30 3510085 NO NO COMPLETED OCT 13, 2005

Total: 12

\<End of Report\>

User Service Connected Encounters Report – (Detail) Example:

OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY USER PAGE: 1

FOR ENCOUNTERS DATED 1/1/04 THRU 11/12/04

ENCOUNTER DATE ENC \# VBA SC USER SC STATUS DATE LAST EDITED

PMS, ONE

01/02/2004@09:40 3507200 NO YES COMPLETED SEP 23, 2004

POVs/ICDs:

428.0 CONGEST HEART FAIL UNSPESIFIED

702.0 ACTINIC KERATOSIS

427.31 ATRIAL FIBRILLATION

276.8 HYPOPOTASSEMIA

Rated Disabilities:

6100 IMPAIRED HEARING (20%-SC)

5310 FOOT INJURY (10%-SC)

5318 GRP XVIII - PELVIC GIRDLE GRP 3 (10%-SC)

6260 TINNITUS (10%-SC)

5310 FOOT INJURY (10%-SC)

5314 THIGH MUSCLE INJURY (10%-SC)

Total: 1

\<End of Report\>

#### User Total Summary Report \[SDSC USER TOTAL REPORT\] 

This report prints totals of the ASCD encounters under the following categories per user:

- SET to REVIEW Number of outpatient encounters set to Clinical Review.
- SC to NSC Number of outpatient encounters marked as 'Service

Connected=YES' but were changed to 'Service Connected =NO'.

- NSC to SC Number of outpatient encounters marked as 'Service

Connected=NO' but were changed to 'Service Connected=YES'.

- SC KEPT Number of outpatient encounters marked as 'Service

Connected=YES' or 'Service Connected = No' that were not

changed.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

User Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>User Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 By Division: ALL</p>
<p>SET to REVIEW SC to NSC NSC to SC SC KEPT</p>
<p>-------------------------------------------------------------------------------</p>
<p>USER,ONE 1 2 3 2</p>
<p>USER,TWO 0 11 0 25</p>
<p>------- ------- ------- -------</p>
<p>TOTAL 1 13 3 27</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Updates to Claims Tracking (Billing) After Encounter is Reviewed via ASCD………………...15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of the Software 3

User Service Connected Encounters Report 29

User Total Summary Report 30

User Types 3
