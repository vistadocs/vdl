---
title: DG*5.3*650 Patient Record Flags Phase III User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Patient Record Flags Phase III
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*650
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 3
description: Patient record flags are used to alert VHA medical staff and employees of patients whose behavior and characteristics may pose a threat either to their safety, the safety of other patients, or compromise the delivery of quality health care. These flag assignments are displayed during the patient loo
audience: 
keywords: 
  - flag
  - patient
  - record
  - category
  - assignment
  - flags
  - table
  - report
  - contents
  - prfs
page_count: 0
word_count: 5899
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_53_650_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_53_650_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

![](dg-5-3-650-patient-record-flags-phase-iii-user-guide/001.png)

Patient Record Flags Phase IIIUser Guide

DG\*5.3\*650

November 2006

Health Systems Design & Development (HSD&D)

Table of Contents

Introduction 1PRF Display on Patient Look-up 3Patient Record Flags Main Menu 5

Record Flag Reports Menu 7

Assignment Action Not Linked Report 7

Flag Assignment Report 8

Patient Assignments Report 9

Assignments Due for Review Report 10

Assignments Approved By Report 11

Assignments by Principal Investigator Report 12

> Record Flag Assignment 13

Record Flag Management 16

Record Flag Transmission Mgmt 18

Record Flag Transmission Errors 18

Record Flag Manual Query 19

Record Flag Enable Divisions 20

Appendix - VHA Directive 2003-048, National Patient Record Flags 21

Introduction

Patient record flags are used to alert VHA medical staff and employees of patients whose behavior and characteristics may pose a threat either to their safety, the safety of other patients, or compromise the delivery of quality health care. These flag assignments are displayed during the patient look-up process.

The use of patient record flags must be strictly controlled and implemented following the instruction provided in VA Directive 2003-048 (see Appendix).

The Patient Record Flags (PRF) software provides users with the ability to create, assign, inactivate, edit, produce reports, and view patient record flag alerts. Patient record flags are divided into Category I (national) and Category II (local) flags.

Category I flags are nationally approved and distributed by VHA nationally released software for implementation by all facilities. The Category I flag is shared across all known treating facilities for the patient utilizing VistA HL7 messaging.

Category II flags are locally established by individual VISNs or facilities. They are not shared between facilities.

PRF Display on Patient Look-up

The following is an example of the patient record flags assignment information displayed on patient look-up for those patients with flag assignments. Category I flags will be listed first with the category designation (Cat I or II) displayed. It is strongly recommended you answer YES to viewing the active patient record flag details, especially for behavioral flags, to view information which may be critical to patient and employee safety.

The primary facility is displayed in parenthesis following the divisional facility in the Owner Site and Originating Site fields.

Select Registration Menu Option: Load/Edit Patient Data

Select PATIENT NAME: adtpatient,one ADTPATIENT,ONE 2-3-20 000456789

1 YES NSC VETERAN

\>\>\> Active Patient Record Flag(s):

\<BEHAVIORAL\> CATEGORY I

Do you wish to view active patient record flag details? YES// \<RET\>

<u>Patient Record Flags Jun 05, 2003@07:22:55 Page: 1 of 4</u>

Patient: ADTPATIENT,ONE (000456789) DOB: 02/03/20

ICN: 5000000003V639492 CMOR: 1XXXXX

\<\<\< Active Patient Record Flag Assignments \>\>\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Flag Name: \<BEHAVIORAL\>

Category: I (NATIONAL)

Type: BEHAVIORAL

Assignment Narrative:

On 4/8/03, this veteran was disruptive and threatening toward numerous

staff. RECOMMEND: VA Police should be immediately called to standby

until they and the clinician decide that standby is no longer necessary.

Assignment Details:

Initial Assignment: May 20, 2003

Approved By: ADTAPPROVER,ONE

Next Review Date: May 20, 2005

Owner Site: XXXXX VAMC (UPSTATE NEW YORK HCS)

Originating Site: EL PASO VA HCS (EL PASO VA HCS)

Progress Note Linked: No

\+ Enter ?? for more actions

Select Action: Quit//

Patient Record Flags Main Menu

*Record Flag Reports Menu*

> *Assignment Action Not Linked Report*

> This option is used to display PRF assignment history actions that are not linked to a progress note.

> *Flag Assignment Report*

> This option is used to display all of the patient assignments for Category I flags, Category II flags, or both by date range.

> *Patient Assignments Report*

> This option is used to display all of the patient record flag assignments for a particular patient.

> *Assignments Due for Review Report*

> This option is used to display all of the patient assignments for Category I flags, Category II flags, or both that are due for review within a selected date range.

> *Assignments Approved By Report*

> This option is used to display all of the PRF assignment history actions for a single individual or all individuals who approved the assignment of patient record flags.

> *Assignments by Principal Investigator Report*

> This option is used to display all of the PRF assignment history actions for a single principal investigator or all principal investigators for a specified date range (research flags only).

*Record Flag Assignment*

This option is used to assign a flag(s) to a patient and to maintain those assignments.

*Record Flag Management*

This option is used to create and maintain patient record flags. These flags are then assigned to individual patients through the Record Flag Assignment option.

*  
Record Flag Transmission Mgmt*

> *Record Flag Transmission Errors*

> This option is used to review rejected PRF HL7 update messages and retransmit them.

> *Record Flag Manual Query*

> This option allows a user to query a selected treating facility for existing Category I Patient Record Flag (PRF) assignments for a selected patient.

*Record Flag Enable Divisions*

This option allows multi-divisional facilities to enable, disable, and view individual medical center divisions as patient record flag assignment owners.

Record Flag Reports Menu

### Assignment Action Not Linked Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display PRF assignment history actions that are not linked to a TIU progress note for a specified date range. You may choose to print the report for Category I flags, Category II flags, or both.

An example of the output is shown below.

PATIENT RECORD FLAGS

ASSIGNMENT ACTION NOT LINKED TO A PROGRESS NOTE REPORT Page: 1

Report Selected: Category II (Local)

DATE RANGE: 06/01/05 TO 10/15/05 Printed: Oct 15, 2005@11:03

------------------------------------------------------------------------------

CATEGORY: Category II (Local)

PATIENT SSN FLAG NAME ACTION ACTION DATE

------------------ ---------- --------------- ---------------- ---------

ADTPATIENT,ONE 666880015 APEX STUDY NEW ASSIGNMENT 06/29/05

CONTINUE 07/29/05

CONTINUE 08/29/05

CONTINUE 09/29/05

ADTPATIENT,TWO 666769873 APEX STUDY NEW ASSIGNMENT 10/13/05

Total Actions not Linked for Category II: 5

\<End of Report\>

Record Flag Reports Menu

### Flag Assignment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display all of the patient assignments for Category I flags, Category II flags, or both by date range. If you choose a single category, you may further choose to display the assignment report for a single flag or all flags of that category.

Information provided on the display for each flag includes patient name, social security number, date flag assigned, flag review date, flag status (active or inactive) and ownership site.

If you choose to print for both Category I and II flags, the total assignments for each category will be displayed as well as the combined total number of assignments.

An example of the output is shown below.

PATIENT RECORD FLAGS

FLAG ASSIGNMENT REPORT Page: 1

---------------------- Printed: May 05, 2005@14:54

CATEGORY: Category II (Local)

DATE RANGE: 01/01/05 TO 05/05/05

FLAG NAME: RESEARCH

PATIENT NAME SSN ASSIGNED REVIEW DT STATUS OWNING SITE

-------------------- --------- -------- -------- -------- --------------

ADTPATIENT,ONE 666456789 05/05/05 05/04/06 ACTIVE XXXXX

ADTPATIENT,TWO 000888767 04/17/05 04/16/06 ACTIVE XXXXX

Total Assignments for Flag: 2

\<End of Report\>

Record Flag Reports Menu

### Patient Assignments Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display all of the patient record flag assignments for a particular patient. You may choose to print the report for active flags, inactive flags, or both.

An example of the output is shown below.

PATIENT RECORD FLAGS

PATIENT ASSIGNMENTS REPORT Page: 1

Report Selected: Both (ACTIVE & INACTIVE) Printed: Oct 15, 2005@11:29

-----------------------------------------------------------------------------

Patient: ADTPATIENT,ONE 666-01-0122

FLAG NAME CATEGORY APPROVED BY ENTERED REVIEW DT STATUS OWNING SITE

--------------- --- ----------- -------- --------- -------- -----------

1 BEHAVIORAL I APPROVER,ONE 11/12/04 11/11/06 ACTIVE MASTER PATI

2 APEX STUDY II APPROVER,TWO 03/26/05 04/25/07 ACTIVE XXXXX

\<End of Report\>

Record Flag Reports Menu

### Assignments Due for Review Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display all of the patient assignments for Category I flags, Category II flags, or both that are due for review within a selected date range. If you choose a single category, you may further choose to display the review report for a single flag or all flags of that category.

Information provided on the display for each flag includes patient name, social security number, date flag assigned, flag review date, and whether or not the review notification mail message has been sent. Reviews that are past due are signified by an asterisk (\*) next to the date in the Review Date column.

If you choose to print for both Category I and II flags, the total number of assignments for review for each category will be displayed as well as the combined total number of assignments for review.

An example of the output is shown below.

PATIENT RECORD FLAGS

ASSIGNMENTS DUE FOR REVIEW REPORT Page: 1

--------------------------- Printed: May 05, 2005@14:57

CATEGORY: Category II (Local)

DATE RANGE: 01/01/05 TO 12/31/06

FLAG NAME: RESEARCH

PATIENT NAME SSN ASSIGNED REVIEW DT NOTIFICATION SENT

-------------------- --------- -------- --------- -----------------

ADTPATIENT,ONE 666456789 05/05/05 05/15/06 NO

ADTPATIENT,TWO 000990909 04/17/05 04/16/06 NO

Total Review Assignments for Flag: 2

> **NOTE:** " \* " indicates that review date is past due

\<End of Report\>

Record Flag Reports Menu

### Assignments Approved By Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display all of the PRF assignment history actions for a single individual or all individuals who approved the assignment of patient record flags. You may choose to print the report for Cat I flags, Cat II flags, or both; active flags, inactive flags, or both.

An example of the output is shown below.

PATIENT RECORD FLAGS

ASSIGNMENTS APPROVED BY REPORT Page: 1

Date Range: 06/01/05 to 10/15/05 Printed: Oct 15, 2005@11:09

-----------------------------------------------------------------------------

Approved By: ADTPROVIDER,ONE

Flag Name: BEHAVIORAL - Category I (National)

PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

================ ========== ============= ========= ========= =========

ADTPATIENT,ONE 666120565 NEW ASSIGNMENT 07/23/05 07/23/07 ACTIVE

ADTPATIENT,TWO 666769873 NEW ASSIGNMENT 08/11/05 08/11/07 ACTIVE

Approved By: ADTPROVIDER,TWO

Flag Name: BOB1 TEST LOCAL FLAG - Category II (Local)

PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

================ ========== ============= ========= ========= =========

ADTPATIENT,TEN 666880015 NEW ASSIGNMENT 09/29/05 10/09/05 ACTIVE

CONTINUE 09/29/05 10/09/05 ACTIVE

CONTINUE 09/29/05 10/09/05 ACTIVE

Approved By: ADTPROVIDER,TWO

Flag Name: BOB1 TEST LOCAL FLAG - Category II (Local)

PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

================ ========== ============= ========= ========= =========

ADTPATIENT,TEN 666880015 CONTINUE 09/29/05 10/09/05 ACTIVE

CONTINUE 09/29/05 10/09/05 ACTIVE

Flag Name: BOBS TIU TEST FLAG - Category II (Local)

PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

================ ========== ============= ========= ========= =========

ADTPATIENT,TWO 666769873 NEW ASSIGNMENT 08/11/05 08/11/07 ACTIVE

\<End of Report\>

Record Flag Reports Menu

### Assignments by Principal Investigator Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display all of the PRF assignment history actions for a single principal investigator or all principal investigators for a specified date range. You may choose to print the report for active flags, inactive flags, or both.

Investigators are associated with research type flags. For each flag listed on the report, all principal investigator names for that flag are displayed.

An example of the output is shown below.

PATIENT RECORD FLAGS

ASSIGNMENTS BY PRINCIPAL INVESTIGATOR REPORT Page: 1

Date Range: 10/01/05 to 10/18/05 Printed: Oct 18, 2005@10:57

Sorted By: (A)ll Principal Investigators

-----------------------------------------------------------------------------

Flag Name: RESEARCH STUDY - Category II (Local)

Principal Investigator: ADTINVESTIGATOR,ONE; ADTINVESTIGATOR,TWO

PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

================ ========== ================ ========= ========= ======

ADTPATIENT,ONE 000880015 NEW ASSIGNMENT 10/04/05 02/01/06 ACTIVE

ADTPATIENT,TEN 666223333 NEW ASSIGNMENT 10/08/05 04/05/06 ACTIVE

\<End of Report\>

Record Flag Assignment

The Record Flag Assignment option is used to assign a flag(s) to a patient and to maintain those assignments.

The "Review Date" field will display "N/A" (not applicable) when any of the following conditions exist:

- The most recent update to the PRF assignment was received from a remote system.
- The current PRF assignment status is Inactive.

All PRF Record Flags that are or will be assigned to a patient must be linked to a TIU Progress Note Title or you will be unable to proceed with this option.

You must hold the DGPF ASSIGNMENT security key to access this option.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. A description of the actions you may utilize in this option is provided below.

The following is an example of a Record Flag Assignment screen.

<u>RECORD FLAG ASSIGNMENT July 20, 2005@14:48:23 Page: 1 of 1</u>

Patient: ADTPATIENT,SIX (000456789) DOB: 02/03/20

ICN: 5888777773V639492 CMOR: XXXXX

<u>Flag Assigned Review Date Active Local Owner Site</u>

1 BEHAVIORAL 04/29/05 N/A YES NO Bath VAMC

2 RESEARCH 05/24/05 11/11/05 YES YES Upstate New York

Enter ?? for more actions

SP Select Patient EF Edit Flag Assignment

DA Display Assignment Details CO Change Assignment Ownership

AF Assign Flag

Select Action:Quit//

## Record Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## SP Select Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information provided on the selected patient includes social security number, Internal Control Number (ICN); Coordinating Master of Record (CMOR) site (site that is the authoritative source for the demographic fields); and date of birth. Flags assigned to the patient will be listed with the following data elements.

> Flag Name

> Assigned - Date flag was assigned.

> Review Date - Date flag will be up for review.

> Active - Is the flag active? Yes or No.

> Local - Is the flag local? Yes or No.

> Owner Site - Site that has ownership of the flag.

## DA Display Assignment Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used to display the following information on a selected flag assignment.

The "Approved By" field will display "Chief of Staff" if your site does not have ownership of the flag assignment. The Progress Note field will only be displayed if your site has assignment ownership.

> Flag Name

> Flag Type

Flag Category

> Assignment Status

> Date of Initial Assignment

> Last Review Date

> Next Review Date

> Owner Site

> Originating Site

> Flag Assignment Narrative

> Flag Assignment History

> Action

> Action Date

> Entered By

> Approved By

> Progress Note

> Action Comments

## Record Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## AF Assign Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used to assign a flag to a patient. Assigning a flag consists of entering the following fields. After completion, the data will be displayed for review before filing.

> Name of the flag (to see a list of the available flag names enter L.? for local flags and N.? for national flag)

> Owner Site

> Name of the individual who approved the assignment

> Narrative text (reason) for the assignment

> Review Date

## EF Edit Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used to continue a flag assignment, inactivate the assignment, or to designate that the assignment was entered in error. It can also be used to update the assignment narrative. You must enter the reason for editing the assignment. Note that Category I flag assignments may only be edited by the owner site.

## CO Change Assignment Ownership

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used to change the ownership of a record flag assignment. The ownership of Category I flags may be changed to any of the patient’s treating facilities and to any of the divisions enabled for ownership at multi-divisional sites. The ownership of Category II flags may be changed to any of the divisions enabled for ownership at multi-divisional sites. This action would be taken if the patient changed his primary VA care site or special circumstances arose that warranted the transfer of the flag.

Record Flag Management

The Record Flag Management option is used to create and maintain Category II patient record flags. It can also be used to display a list of Category I and II flags and the details for those flags.

You must hold the DGPF MANAGER security key to access this option.

This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. A description of the actions you may utilize in this option is provided below.

The following is an example of a Record Flag Management screen.

<u>RECORD FLAG MANAGEMENT May 05, 2003@14:40:52 Page: 1 of 1</u>

Flag Category: II (Local) Sorted By: Flag Name

<u>Flag Name Flag Type Flag Status</u>

1 CANCER PROTOCOL RESEARCH ACTIVE

2 DRUG SEEKING BEHAVIOR BEHAVIORAL ACTIVE

3 INFECTIOUS DISEASE CLINICAL ACTIVE

Enter ?? for more actions

CC Change Category DF Display Flag Detail EF Edit Record Flag

CS Change Sort AF Add New Record Flag

Select Action:Quit//

## CC Change Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Category I flags are displayed on the screen when the option opens. Currently there is only one national Category I flag (Behavioral) which is distributed with the software. Use this action to change the category of the flag list being viewed.

## CS Change Sort

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can choose to sort the flag list by flag name (alphabetically) or flag type. Flag types are distributed with the software and cannot be added to or edited.

## DF Display Flag Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used to display information about the selected flag such as flag name, type, category, status, TIU Progress Note Title, description, etc. The enter/edit history of the flag is a part of this display.

  
Record Flag Management

## AF Add New Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will allow you to enter a new Category II (local) patient record flag.

Entering a new flag consists of completing the following fields.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field</strong></td>
<td><h2 id="description">Description</h2></td>
</tr>
<tr class="even">
<td>Record Flag Name</td>
<td>Locally assigned name of the flag.</td>
</tr>
<tr class="odd">
<td>Status of the Flag</td>
<td>Active or Inactive</td>
</tr>
<tr class="even">
<td>Type of Flag</td>
<td>Clinical, Research, etc. Entries are distributed with the software.</td>
</tr>
<tr class="odd">
<td>Principal Investigator</td>
<td>This prompt will only appear if the flag type is RESEARCH. Enter the investigator(s) associated with this research flag.</td>
</tr>
<tr class="even">
<td>Review Frequency Days</td>
<td>Number of days that may elapse between reviews of this flag assignment. Flags must be reviewed at least every two years. A value of zero indicates that NO automatic review will occur.</td>
</tr>
<tr class="odd">
<td>Notification Days</td>
<td>Number of days prior to this flag assignment's review date that a notification is sent to the review group. A value of zero indicates that NO prior notification is required.</td>
</tr>
<tr class="even">
<td>Review Mail Group</td>
<td>Name of the mail group that will receive notification that this flag assignment is due for review. Mail group name must begin with DGPF. It is further recommended that locally-defined mail groups begin with DGPFZ.</td>
</tr>
<tr class="odd">
<td>Progress Note Title</td>
<td>Name of TIU Progress Note linked with the flag.</td>
</tr>
<tr class="even">
<td>Description of the Flag</td>
<td>A brief description of this patient record flag.</td>
</tr>
</tbody>
</table>

## EF Edit Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will allow you to edit the fields associated with a Category II(local) patient record flag. You must enter the reason for editing the flag. If you change the STATUS field from ACTIVE to INACTIVE, all patient record flag assignments associated with this flag will be inactivated.

Record Flag Transmission MgmtRecord Flag Transmission Errors

This option provides the means to review rejected PRF HL7 update messages and retransmit them. You may sort the list by patient name or date/time message received.

The view message action will display details of the selected message. Data items may include error received date/time, message control ID, flag name, owner site, assignment transmitted to, assignment transmission date/time, and rejection reasons.

The retransmit message action will retransmit all of the patient’s PRF assignment and history records to the site where the rejection message occurred.

You must hold the DGPF TRANSMISSIONS security key to access this option.

The following is an example of a Record Flag Transmission Errors screen.

<u>TRANSMISSION ERRORS Aug 02, 2005@13:16:01 Page: 1 of 1</u>

List Sorted By: Patient Name

<u>Patient Name SSN Received Transmitted To Owner Site .</u>

1 ADTPATIENT,ONE 2323 12/03/04 PORTLAND.VA.GOV DEVVPP.F0-ALBA

2 ADTPATIENT,TWO 0565 09/20/04 PALO ALTO. VA. GOV ZZ XXXXX

3 ADTPATIENT,SIX 0888 07/23/04 DEVVPP.F0-ALBA ZZ XXXXX

4 ADTPATIENT,TEN 4811 03/29/05 ZZ XXXXX DEVVPP.F0-ALBA

Enter ?? for more actions

CS Change Sort RM Retransmit Message

VM View Message

Select Action:Quit//

Record Flag Transmission MgmtRecord Flag Manual Query

This option allows a user to query a selected treating facility for existing Category I Patient Record Flag (PRF) assignments for a selected patient.

The option displays a list of all Category I PRF assignments found at the queried treating facility. You may then display the query result details for a selected assignment. Any Category I PRF assignment returned by the query that does not already exist at your facility is automatically added.

If active flag assignments already exist at your facility for the selected patient, they are displayed and you may choose to view the flag details before sending the query.

- The following is an example of the message displayed when the option successfully returns and files a PRF assignment that was missing at your facility.

> The following Category I Patient Record Flag Assignments

> were returned and filed on your system: BEHAVIORAL

- If no Category I flag assignments are found in the queried treating facility database for the selected patient, the following message is displayed.

> No Category I Patient Record Flag Assignments found for this patient at {site name}.

- The following message is displayed when the HL7 software has a problem communicating between the two facilities.

> The facility failed to respond to the query request.

The following is an example of a Record Flag Manual Query Results screen.

<u>RECORD FLAG QUERY RESULTS Apr 20, 2006@10:16:14 Page: 1 of 1</u>

Patient: ADTPATIENT,ONE (000004321) DOB: 01/01/45

ICN: 100123456 FACILITY QUERIED: ZZ XXXXX

<u>Flag Assigned Active \#Actions Owner Site</u>

1 BEHAVIORAL 02/03/05 YES 2 VISTARPM

Enter ?? for more actions

DR Display Query Result Details

Select Action:Quit//

Record Flag Enable Divisions

This option gives multi-divisional facilities the ability to enable/disable medical center divisions as a PRF owner site. Divisions are disabled by default.

Once a division has been enabled, disabling it will only be allowed if there are no active assignments associated with that division.

You may choose to view a list of medical center divisions for your site. Data items displayed may include medical center division, PRF assignment ownership (enabled/disabled), edited by, edit date/time, and active PRF assignments (Yes/No).

You must hold the DGPF MANAGER security key to access this option.

Appendix - VHA Directive 2003-048

## Department of Veterans Affairs VHA DIRECTIVE 2003-048

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Health AdministrationWashington, DC 20420 August 28, 2003

# NATIONAL PATIENT RECORD FLAGS


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Assignment Action Not Linked Report](#assignment-action-not-linked-report)
    - [Flag Assignment Report](#flag-assignment-report)
    - [Patient Assignments Report](#patient-assignments-report)
    - [Assignments Due for Review Report](#assignments-due-for-review-report)
    - [Assignments Approved By Report](#assignments-approved-by-report)
    - [Assignments by Principal Investigator Report](#assignments-by-principal-investigator-report)
  - [Record Flag Assignment](#record-flag-assignment)
  - [SP Select Patient](#sp-select-patient)
  - [DA Display Assignment Details](#da-display-assignment-details)
  - [Record Flag Assignment](#record-flag-assignment-1)
  - [AF Assign Flag](#af-assign-flag)
  - [EF Edit Flag Assignment](#ef-edit-flag-assignment)
  - [CO Change Assignment Ownership](#co-change-assignment-ownership)
  - [CC Change Category](#cc-change-category)
  - [CS Change Sort](#cs-change-sort)
  - [DF Display Flag Detail](#df-display-flag-detail)
  - [AF Add New Record Flag](#af-add-new-record-flag)
  - [EF Edit Record Flag](#ef-edit-record-flag)
  - [Department of Veterans Affairs VHA DIRECTIVE 2003-048](#department-of-veterans-affairs-vha-directive-2003-048)
- [NATIONAL PATIENT RECORD FLAGS](#national-patient-record-flags)
  - [ATTACHMENT A](#attachment-a)
- [STANDARDS FOR PATIENT RECORD FLAGS](#standards-for-patient-record-flags)
1. PURPOSE: This Veterans Health Administration (VHA) Directive outlines policy and guidance for the proper use of Patient Record Flags (PRFs).
2. BACKGROUND: PRF alerts VHA employees to patients whose behavior or characteristics may pose a threat either to their safety, the safety of other patients, or compromise the delivery of quality health care. PRF helps ensure the rights of all patients to receive confidential, safe, and appropriate health care and provides a safe work environment for employees.
a\. Health care workers experience the highest rate of injuries from work place assault in the United States. Health care is one of only two industries that have merited special attention from Occupational Safety and Health Administration (OSHA) (see subpars. 5a and 5b). In recognition, VHA has initiated a broad-based program of violence prevention, including performance monitors through the Office of the Deputy Under Secretary for Operations and Management. Efforts have included the redesign of the basic course “Prevention and Management of Disruptive Behaviors” and the development of new courses for geriatrics and other disciplines.
b\. The Joint Commission on Accreditation of Health Care Organizations (JCAHO) recently made patient violence and its prevention a focus of the Environment of Care Standards (see subpar. 5c).
c\. Recent studies have shown that The Department of Veterans Affairs (VA) health care facilities are not immune from these safety concerns (see subpars. 5d and 5e). The VA Office of Inspector General (OIG) in its report “Evaluation of VHA’s Policies and Practices for Managing Violent or Potentially Violent Psychiatric Patients” (6HI-A28-038, dated March 28, 1996) recommended that facilities communicate among themselves so that staff are aware of high-risk patients regardless of where in the VHA system they may seek health care (see subpar. 5f).
d\. Computer-based advisories that alert clinicians to a patient’s risk of violence have been in use for many years within some facilities (see subpar. 5g). However, for PRFs to assist in the prevention of adverse events when high-risk patients travel between facilities, it is important that all facilities follow uniform processes. The effectiveness of PRFs depends upon limiting their use to those unusual clinical risks that threaten health care safety and quality.
e\. The safety of patients and employees, the effectiveness of care, and the patient’s right to privacy need not be compromised by threats of violence. Risk of violence can be mitigated by recognition, assessment, documentation, and communication.
f\. <u>Definitions</u>
\(1\) Category I Behavioral National PRFs
\(a\) Category I Behavioral National PRFs are nationally approved and are to be used by all facilities. Category I PRFs describe patient behavior that may pose a threat to the safety of themselves, other patients, visitors, or employees. Category I PRFs also recommend specific behavioral limit setting or treatment-planning actions designed to reduce risk. A Category I PRF requires a documented history of violence or disruptive and/or threatening behavior in a health care setting or the documented presence of other factors that indicate a significant risk of violence. A Text Integrated Utility (TIU) Progress Note in the Computerized Patient Record System (CPRS) must accompany all Category I PRFs.
\(b\) Criteria for Category I PRFs may include, but are not limited to:
> <u>1</u>. A history of physical violence against patients or staff at a medical center or clinic.
> <u>2</u>. Documented acts of repeated violence against others.
> <u>3</u>. Credible verbal threats of harm against specific individuals, patients, staff, or VA property.
> <u>4</u>. Possession of weapons or objects used as weapons in a health care facility.
> <u>5</u>. A history of suicidal or parasuicidal behavior within health care facilities.
<u>6</u>. A history of repeated nuisance and disruptive or larcenous behavior that disrupts the environment of care.
> <u>7</u>. A history of sexual harassment toward patients or staff.
\(2\) Category II Local PRFs. Category II Local PRFs may be locally established by individual Veterans Integrated Service Networks (VISNs) or facilities. Category II PRFs may include patients who are enrolled in a research project or patients with documented drug-seeking behavior. The use of Category II PRFs should also be strictly limited to information that is essential for the delivery of safe and appropriate health care. A Text Integration Utility (TIU) Progress Note in the Computerized Patient Record System (CPRS) must also accompany all Category II PRFs.
3. POLICY: It is VHA policy that all facilities must immediately install the required patches (as they are available) and initiate facility-wide use of PRFs.
4\. ACTION
a\. <u>Deputy Under Secretary for Health for Operations and Management.</u> The Deputy Under Secretary for Health for Operations and Management (10N) is responsible for providing oversight to the VISNs to ensure that PRFs are appropriately implemented by the VISNs.
b\. <u>VISN Director.</u> The VISN Director, or designee (the Network Mental Health Committee or other comparable VISN group), is responsible for oversight and implementation of this Directive at the VISN level.
> c\. <u>Medical Facility Director.</u> The medical facility Director, or designee, is responsible for:
\(1\) Ensuring that Category I Behavioral PRFs are originated and accessible. Individual Networks and facilities determine whether optional Category II PRFs are to be used. *NOTE:Attachment A, Standards for PRFs, defines the standards for the origination of, and access to, both Category I and Category II PRFs.*
\(2\) Establishing a process for requesting, assigning, reviewing, and evaluating PRF.
\(3\) Establishing a plan to transition previous behavioral Veterans Health Information and Technology Architecture (VistA), CPRS, local Class III Advisories, and any other behavioral alerts or warnings system in use, to the VHA nationally released PRF software. After September 25, 2003, only PRF computerized advisories as described in Attachment A are approved for use. Each Category I Behavioral PRF assigned to a patient must be reviewed at least every 2 years; however, reviews may be appropriate any time that a patient’s violence risk factors change significantly, the patient requests a review, or for other appropriate reasons. *NOTE: It is suggested that existing Class III advisories be reviewed and assigned to the new PRF system in a manner that does not make them all come due for review at the same time. Existing advisories that are converted must fully meet the advisories of the PRF criteria.*
> \(4\) Installing patches DG\*5.3\*425, OR\*3\*173, TIU\*1\*165, and USR\*1\*24.
> \(5\) Training appropriate staff.
> \(6\) Evaluating the facility process to ensure that PRFs are assigned appropriately.
\(7\) Ensuring that each PRF is a patient's record is accompanied by a TIU Progress Note. The TIU titles utilized must be:
> \(a\) PRF Category I, and
> \(b\) PRF Category II.
> d\. <u>Chief of Staff (COS).</u> The COS is responsible for:
> \(1\) Instituting procedures to ensure that PRF and associated processes are ethical, effective, and reviewed as noted in this Directive.
> \(2\) Identifying a Disruptive Behavior Committee which reports to the COS.
> \(a\) The Disruptive Behavior Committee is responsible for:
<u>1</u>. Coordinating the treatment plan with appropriate clinicians responsible for the patient’s medical care.
> <u>2</u>. Implementing the standards in Attachment A.
> <u>3</u>. Collecting and analyzing incidents of patient disruptive, threatening, or violent behavior.
> <u>4</u>. Assessing the risk of violence in individual patients.
> <u>5</u>. Identifying system problems.
<u>6</u>. Identifying training needs relating to the prevention and management of disruptive behavior.
> <u>7</u>. Recommending to the COS other actions related to the problem of patient violence.
> \(b\) The Disruptive Behavior Committee needs to be comprised of:
<u>1</u>. A senior clinician chair who has knowledge of, and experience in, assessment of violence.
> <u>2</u>. A representative of the Prevention Management of Disruptive Behavior Program in the facility (see subpar. 5i).
> <u>3</u>. VA Police.
> <u>4</u>. Health Information Management Service.
> <u>5</u>. Patient Safety and/or Risk Management.
> <u>6</u>. Regional Counsel (ad hoc).
> <u>7</u>. Patient Advocate.
> <u>8</u>. Other members as needed with special attention to representatives of facility areas that are high risk for violence, e.g., emergency department, nursing home, and inpatient psychiatry.
> <u>9</u>. Clerical and Administrative support to accomplish the required tasks.
5. REFERENCES
a\. Appelbaum PS, Dimieri RJ. "Protecting Staff from Assaults by Patients: OSHA Steps In," <u>Psychiatric Services.</u> 46(4): 333-338, 1995.
b\. Guidelines for Preventing Workplace Violence for Health Care and Social Service Workers; U.S. Department of Labor, Occupational Safety and health Administration, OSHA 3148, 1996.
> c\. Environment of Care Guidebook, JCAHO, 1997.
d\. VA Suicide and Assaultive Behavior Task Force. Report of a Survey on Assaultive Behavior in VA Health Care Facilities; Feb. 15, 1995.
e\. Blow, FC; Barry, KL; et al. "Repeated Assaults by Patients in VA Hospital and Clinic Settings," <u>Psychiatric Services.</u> 50(3): 390-394: 1999.
f\. OIG Evaluation of VHA’s Policies and Procedures for Managing Violent and Potentially Violent Psychiatric Patients (Report No. 6HI-A28-038).
g\. Drummond, D, et al., "Hospital Violence Reduction in High-risk Patients, "<u>Journal of the American Medical Association (JAMA</u>). 261(17) 531-34, 1989.
h\. Secretary’s Letter to All VA Employees October 19, 2001 <span class="mark">REDACTED</span>
i\. VA Office of Occupational Safety and Health Intranet Site: \<<span class="mark">REDACTED</span>
<u>\></u> Includes links to the Prevention and Management of Disruptive Behavior (PMDB) VA training program.
> j\. Public Law 105-220, Section 508.
6. FOLLOW-UP RESPONSIBILITY: The Director, Mental Health Services (116) is responsible for the contents of this Directive. Questions may be addressed to 202-273-8434.
7. RESCISSIONS: None. This VHA Directive will expire August 31, 2008.
> Robert H. Roswell, M.D.
> Under Secretary for Health
Attachment
DISTRIBUTION: CO: E-mailed 8/28/03
FLD: VISN, MA, DO, OC, OCRO, and 200 - E-mailed 8/28/03
VHA DIRECTIVE 2003-048
August 28, 2003

## ATTACHMENT A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# STANDARDS FOR PATIENT RECORD FLAGS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. Background. A small but diverse group of patients who present with certain behavioral or clinical risk factors place special demands upon the health care system. It is both a privilege and a challenge for Department of Veterans Affairs (VA) health care employees and facilities to offer safe and appropriate care to patients who present with certain risk factors. The safety of these patients and the safety of staff that treat them can be enhanced when carefully designed Patient Record Flags (PRFs) immediately alert care providers to the presence of risk factors.

a\. Since some of the most challenging patients are nomadic and because a patient’s electronic health record is increasingly available to other facilities, it is essential that conventions for creating, supporting, and maintaining computerized advisories be made uniform throughout the VA health care system.

b\. PRFs should never be used to punish or to discriminate against patients; nor should they be constructed merely for staff convenience. The effectiveness of PRFs depends upon limiting their use to those unusual risks that threaten the safe delivery of health care. Threats to the effective use of PRFs are their misuse and their overuse.

c\. Providing an environment that is safe for patients, visitors, and employees is a critical factor in health care. The safety of patients and staff, as well as the effectiveness of care and patients’ right to privacy and dignity, need not be compromised by threats of violence or other risk factors. Risks associated with a history of violence and other risk factors can be limited when those risks are recognized and reported. Risks need to be addressed by an interdisciplinary clinical and threat assessment group and documented, when appropriate, in the patient's treatment plan. They must also be communicated in a standardized manner to those most at risk in an encounter with a “flagged” patient.

2. Procedures. Each facility must demonstrate its readiness to use PRFs in a manner consistent with the standards and protocols outlined in this Directive.

a\. As part of the patient health record, all PRF are under authority of the Chief of Staff at each facility and must be reviewed at least every 2 years. A reminder for upcoming review must be generated 60 days prior to the 2-year anniversary date of the PRF. *NOTE: PRFs must be accorded the same confidentiality and security as any other part of the heath record.*

b\. The Chief of Staff or designee, at each facility is responsible for identifying those employees authorized to initiate, enter, and access PRFs. The Chief of Staff, or designee, must ensure that only those employees with a demonstrated need to know are permitted access to PRF menu options.

c\. Access to viewing PRFs is recommended for employees who are likely to be the first to encounter a “flagged” patient, prior to or at the time of the patient's visit, since these employees are usually the most at risk from a violent patient. Access includes viewing the type of PRF and the narrative associated with it. Those who access a PRF are responsible for communicating the PRF advisory to doctors, nurses, and others who have a need to know. The following examples are medical center staff who have direct patient contact needing to view, or be made aware of, PRFs:

> \(1\) Emergency room clerks and receptionists,

> \(2\) Administrative Officer of the Day,

> \(3\) Pharmacists and pharmacy technicians,

> \(4\) VA police officers,

> \(5\) Enrollment clerks,

> \(6\) Social Work staff,

> \(7\) Triage and/or telephone care staff,

> \(8\) Ward and clinic clerks,

> \(9\) Insurance and billing staff

> \(10\) Receptionists,

> \(11\) Travel clerks,

> \(12\) Laboratory clerks and technicians,

> \(13\) All medical staff,

> \(14\) Patient advocates,

> \(15\) Nursing and unit supervisors,

> \(16\) Decedent Affairs Clerk,

> \(17\) Scheduling staff, and

> \(18\) Fee clerks.

d\. PRF software will be made available with the national release of Patches DG\*5.3\*425, OR\*3\*173, USR\*1\*24, TIU\*1\*165, and a Computerized Patient Record System (CPPRS) GUI executable. Although facilities may respond appropriately to PRFs transmitted from other facilities, only facilities that meet the following criteria need to enter new Category I PRFs.

> \(1\) The facility has developed a systematic approach to collecting reports involving incidents of disruptive, threatening, or violent behavior.

> \(2\) There is documented interdisciplinary review and threat assessment of patient behavior.

> \(3\) Documentation that supports the rationale for the patient advisory may be present in other systems of records. A Text Integration Utility (TIU) Progress Note needs to be entered at the same time as a Category I PRF. The TIU Progress Note needs to provide general guidance to PRF users and a brief summary of the rationale for a specific patient’s PRF.

> \(4\) Appropriate training of staff, that in the course of their duties must assess and document risk or threats as well as implement behavioral limits and treatment plans, will be documented.

> \(5\) A process exists for the review of each flag at least every 2 years. A review may be appropriate when: the risk factors change significantly, a patient with a PRF requests a review, or for other appropriate reasons as determined by the facility that established the flag.

> e\. PRFs serve only to preserve and enhance the safety and appropriateness of patient care*.*

f\. PRFs alert staff to a potential risk only. At each patient encounter, the examining physician or other clinician is responsible for making appropriate clinical decisions.

g\. Each facility must have clearly written definitions and criteria (that are consistent with this VHA Directive) for all Category I and Category II PRFs.

h\. PRFs need to be entered only by employees who have been trained in both the technical aspects of entry, the appropriate criteria, and in the conventions for security, format, and terminology.

i\. PRFs need to be free of redundant language, slanderous or inflammatory labels, and language that provides insufficient information or guidance for action.

j\. In order for PRFs to be effective, they need to be used only when necessary. Overuse dilutes their importance to staff. Each facility needs to exercise great care in establishing optional Category II PRFs. Only when there is a compelling safety or quality of care issue should additional PRF types be utilized. A PRF is not to be used for staff convenience or to address administrative concerns. Category II PRF types must adhere to the standards as spelled out in this attachment.

k. Patients may request an amendment to the presence or content of a PRF advisory through the facility privacy officer.

l\. The Deputy Under Secretary for Health for Operations and Management (10N) provides oversight to the VISNs to ensure that PRFs are appropriately implemented by the facilities.

m\. Responding to PRFs. Staff must respond appropriately to the appearance of PRFs.

n\. Origination of PRFs. All VISNs must establish processes for the origination of Category I PRFs.

\(1\) All facilities are required to implement and respond to Category I PRFs, regardless of which facility originated the flag.

\(2\) All facilities must participate in utilization of PRFs, regardless of the originating facility for any individual advisory or type of PRF advisory. <u>Only the nationally developed PRF software released by the Office of Information is to be utilized.</u>

o\. PRF Maintenance. The responsibility for ensuring the quality, timeliness, routine review, and documentation in support of a PRF advisory belongs to the originating facility.

\(1\) The advisory itself will reference the authorizing facility and the Chief of Staff or designee who can provide additional information about a specific PRF advisory. A facility that, in the course of providing care to a “flagged” patient, discovers new information that could influence the status of the advisory should not amend the original advisory, but needs to contact the originating facility with the pertinent information.

\(2\) The responsibility for maintenance of PRFs needs to be transferred when it appears that a flagged patient has relocated to a new facility. The originating facility needs to make available to the new facility, copies of all documents and records in support of the advisory.

> p\. PRF Training.

\(1\) Training must provide instruction on how to utilize PRF software on the assignment, continuation, inactivation, and review of flags.

\(2\) Training content must address:

\(a\) Various types of PRFs,

\(b\) Appropriate responses,

\(c\) PRF confidentiality, and

\(d\) Compliance with Public Law 105-220 Section 508 (see subpars. 5h and 5i).