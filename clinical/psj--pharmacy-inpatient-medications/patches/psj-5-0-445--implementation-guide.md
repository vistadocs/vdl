---
title: Methadone Ordering and Dispensing Implementation Guide (PSJ*5.0*445)
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: patch
doc_subject: 
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5.0
patch_id: PSJ*5.0*445
group_key: "PSJ:PSJ:5.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - prompt
  - take
  - home
  - clinic
  - table
  - contents
  - reports
  - opioid
  - desired
  - treatment
page_count: 0
word_count: 1556
section_count: 6
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/PSJ_5_P445_IMPL.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/PSJ_5_P445_IMPL.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Methadone Ordering and Dispensing

  Implementation Guide
---

![](methadone-ordering-and-dispensing-implementation-guide-psj-5-0-445/001.png)

March 2025

Office of Information and Technology (OI&T)

Revision History

| Date    | Description     | Author                |
|---------|-----------------|-----------------------|
| 03/2025 | Initial Release | CPRS Development Team |

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Scope](#scope)
  - [Dependencies](#dependencies)
  - [CPRS Updates](#cprs-updates)
  - [TIU Updates](#tiu-updates)
    - [Temporary protocols](#temporary-protocols)
  - [PSJ Updates](#psj-updates)
    - [New/Modified Files and Fields](#newmodified-files-and-fields)
    - [Modified Routines](#modified-routines)
    - [New Reports Menu \[PSJU REPORTS\]](#new-reports-menu-psju-reports)
    - [Marking a clinic as an Opioid Treatment Clinic](#marking-a-clinic-as-an-opioid-treatment-clinic)
This install guide includes general information regarding the implementation of the Opioid Treatment (OTP) Orders interface. The OTP Interface is being implemented in two releases. The first contains the patches OR\*3.0\*618, TIU\*1.0\*360, and PSJ\*5.0\*445.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OR\*3.0\*618 bundle of patches will allow sites to mark a clinic as an OTP clinic. In addition, sites that currently have an active OTP interface will be able to utilize a new dispensing report that will be available both in the Computerized Patient Record System (CPRS) Graphical User Interface (GUI) as well as the Reports Menu \[PSJU REPORTS\] in the Inpatient Medications V5.0.

## Dependencies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release requires a fully patched VistA system.

## CPRS Updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Opioid Treatment Program (OTP) Dispense Report is now available from the CPRS Reports tab when a clinic has been marked an Opioid Treatment Clinic.

To access the OTP Dispense Report in CPRS:

1.  Access CPRS with an account that has access to a clinic set as an Opioid Treatment Clinic.
2.  Select the desired patient.
3.  Click the Reports tab.
4.  Expand Clinical Reports \> Pharmacy \> OTP Dispense Report.
5.  Specify the date range.

![](methadone-ordering-and-dispensing-implementation-guide-psj-5-0-445/002.png)

## TIU Updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to view the opioid progress notes verify that a Methadone Administration note is set and that a specified user class can view the note.

To check if a Methadone Administration Note exists:

1.  Access the TIU Maintenance Menu, and then at the “Select TIU Maintenance Menu Option:” prompt, enter option 2: Document Definitions (Manager).
2.  At the “Select Document Definitions (Manager) Option:” prompt, enter option 1: Edit Document Definitions.
3.  At the “Selection Action:” prompt enter Jump to Document Def.
4.  At the “Select TIU DOCUMENT DEFINITION NAME:” prompt, enter METHADONE ADMINISTRATION.
5.  If a Methadone Administration note exists, it displays in the notes list. View the note to see the details.
    1.  At the “Select Action:” prompt, enter DETAIL.
    2.  At the “Select Entry:” prompt, enter the note number.

> The note displays.

> ![](methadone-ordering-and-dispensing-implementation-guide-psj-5-0-445/003.png)

6.  If a Methadone Administration note does not exist, create one.

To create a Methadone Administration Note:

1.  Access the TIU Maintenance Menu, and then at the “Select TIU Maintenance Menu Option:” prompt, enter option 2: Document Definitions (Manager).
2.  At the “Select Document Definitions (Manager) Option:” prompt, enter option 3: Create Document Definitions.
3.  At the “Selection Action:” prompt, enter Next Level.
4.  At the “Select CLINICAL DOCUMENTS:” prompt, enter option 2: PROGRESS NOTES.
5.  Find the document class that you want the new note title associated with. Arrow down until you see the document class.
6.  At the “Select Action:” prompt, enter NEXT LEVEL, and then enter the entry number associated with the desired document class. For example, to create the Methadone Administration Note under Medicine, enter its entry number (e.g., 34).
7.  At the “Select Action:” prompt, enter TITLE.
8.  At the “Select Action: TITLE//” prompt, enter the title of the note, METHADONE ADMINISTRATION NOTE.
9.  Configure the new note.
    1.  At the “CLASS OWNER:” Prompt, enter CLINICAL COORDINATOR.
    2.  At the “VHA ENTERPRISE STANDARD TITLE:” prompt, enter MEDICATION MGT NOTE.
    3.  At the “Ready to map LOCAL Title to VHA Enterprise Standard Title:” prompt, enter YES.
    4.  At the “Status:” prompt, enter ACTIVE.

To check and set the user’s class to view the Methadone Administration Note:

1.  Access the TIU Maintenance Menu, and then at the “Select TIU Maintenance Menu Option:” prompt, enter option 3: USR CLASS MANAGEMENT MENU.
2.  At the “Select User Class Management Option:” prompt, enter option 2: List Membership by User.
3.  At the “Select USER:” prompt, enter the desired user’s name.

> The User Classes for that user display.

4.  At the “Select Action:” prompt, enter Add.
5.  At the “Select USER CLASS:” prompt, enter CLINICAL COORDINATOR.

> Note: If a different user class was entered in the Methadone Administration Note creation, add that user class instead of CLINICAL COORDINATOR.

> Note: Repeat this process for each user that will need access to view the Methadone Administration Notes.

### Temporary protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIUAVATARMDM EVENT

This protocol receives and processes inbound messages from the Opioid Treatment Program (OTP) system. Dispense information is captured in file \#101.22.

TIUAVATARMDM SUB

This protocol subscriber handles MDM messages with an event type of T02. This protocol handles the creation of TIU process notes containing dispense information from the OTP system.

## PSJ Updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSJ\*5\*445 made the following modifications and changes.

### New/Modified Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File and fields associated with the Opioid Treatment Clinic option:

| File Name (Number)     | Field Name (Number)        | Patch Release |
|----------------------------|--------------------------------|-------------------|
| CLINIC DEFINITION (#53.46) | OPIOID TREATMENT CLINIC? (#10) | PSJ\*5.0\*445     |

### Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With patch PSJ\*5\*445, the following routines were modified to support the clinic definition changes:

- PSGFILD3

### New Reports Menu \[PSJU REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With patch PSJ\*5\*445, the following Reports Menu \[PSJU REPORTS\] option was added:

OTP Medication Dispense Report

Allows the user to print an OTP (Opioid Treatment Program) Medication Dispense Report by patient for a date range. The report shows whether a patient received medication in clinic or as a take-home dose within the date range selected. The report will also display the medication dispensed, the dose amount, the individual that dispensed the dose, and the time of the dispensed dose.

> **NOTE:** Site menu structure may differ.

To view the OTP Medication Dispense Reports Menu \[PSJU REPORTS\]:

1.  Access the Unit Dose Medications \[PSJU MGR\] menu.
2.  At the “Select Unit Dose Medications Option:” prompt, enter REPorts Menu.  
    The following report options display:

> 7 7 Day MAR  
> 14 14 Day MAR  
> 24 24 Hour MAR  
> AP1 Action Profile \#1  
> AP2 Action Profile \#2  
> OTP OTP Medication Dispense Report  
> AUthorized Absence/Discharge Summary  
> Extra Units Dispensed Report  
> Free Text Dosage Report  
> INpatient Stop Order Notices  
> Medications Due Worksheet  
> Patient Profile (Extended)

3.  At the “Select REPORTS MENU OPTION:” prompt, enter OTP.
4.  At the “Select PATIENT:” prompt, enter the patients name and requested information.  
    Example:  
    Select PATIENT: AAATESTECK,INPATIENT 9-21-35 000000123 YES  
    NO SC VETERAN

> Enrollment Priority: Category: IN PROCESS End Date:

5.  At the “Enter START Date: T-7//” prompt, enter the desired start date.  
    Example: 5/27/24 (MAY 27, 2024)
6.  At the “Enter END Date: T//” prompt, enter the desired end date.  
    Example: 6/23/24 (JUN 23, 2024)
7.  At the “Select output device:” prompt, enter TELNET PORT.

OTP MEDICATION DISPENSE REPORT for May 27, 2024 to Jun 23, 2024@23:59

Run Date: FEB 10, 2025@09:48

Page: 1

================================================================================

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|05/27/2024\|05/28/2024\|05/29/2024\|05/30/2024\|05/31/2024\|06/01/2024\|06/02/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|In Clinic \|Take Home \|Take Home \|Take Home \|Take Home \|Take Home \|

\| \|09:07 SP \| \| \| \| \| \|

\| \|METH LIQ \| \| \| \| \| \|

\| \|80MG \| \| \| \| \| \|

-------------------------------------------------------------------------------

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|06/03/2024\|06/04/2024\|06/05/2024\|06/06/2024\|06/07/2024\|06/08/2024\|06/09/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|In Clinic \|Take Home \|Take Home \|Take Home \|Take Home \|Take Home \|

\| \|09:14 SP \| \| \| \| \| \|

\| \|METH LIQ \| \| \| \| \| \|

\| \|60MG \*\* \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \|In Clinic \|Take Home \|Take Home \|Take Home \|Take Home \|Take Home \|

\| \|09:14 SP \| \| \| \| \| \|

\| \|METH LIQ \| \| \| \| \| \|

\| \|60MG \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \|In Clinic \|Take Home \|Take Home \|Take Home \|

\| \| \| \|09:30 TP \| \| \| \|

\| \| \| \|METH LIQ \| \| \| \|

\| \| \| \|100MG \*\* \| \| \| \|

-------------------------------------------------------------------------------

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|06/10/2024\|06/11/2024\|06/12/2024\|06/13/2024\|06/14/2024\|06/15/2024\|06/16/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|Take Home \|Take Home \|In Clinic \|Take Home \|Take Home \|Take Home \|

\| \| \| \|09:30 TP \| \| \| \|

\| \| \| \|METH LIQ \| \| \| \|

\| \| \| \|90MG \*\* \| \| \| \|

\| \| \| \| \| \| \| \|

\|Take Home \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\|Take Home \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

-------------------------- MEDICATION TO BE TAKEN ON: -------------------------

\| \| \| \| \| \| \| \|

\|06/17/2024\|06/18/2024\|06/19/2024\|06/20/2024\|06/21/2024\|06/22/2024\|06/23/2024 \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\|Take Home \|Take Home \|Take Home \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

\| \| \| \| \| \| \| \|

-------------------------------------------------------------------------------

\*\* LEGEND \*\*

================================================================================

Initial - Name Legend

SP - PHARMACIST,SIX

TP - PHARMACIST,TWO

BLANK SPACE - shows that no dispense information was received via the interface.

This can indicate the patient was a no-show for their appointment, no medication

was prescribed/dispensed, or that the interface failed to send the data.

\*\* - Asterisks indicate that Dispense Amount may have changed within the week.

================================================================================

### Marking a clinic as an Opioid Treatment Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default clinics are not set as Opioid Treatment Clinics. Each Opioid Treatment Clinic must be set individually.

To Set a Clinic Definition to Opioid Clinic:

1.  Access VistA, and then search for the SUPERVISOR’S MENU \[PSJU FILE\].
2.  At the “Select Supervisor’s Menu Option:”, enter PAR to view the Parameters Edit Menu.
3.  At the “Select Parameters Edit Menu:”, enter Clinic Definition.
4.  At the “Select CLINIC:” prompt, enter the desired clinic name, press \<Enter\>. Note: You may be prompted to confirm the clinic or to select the correct clinic if there are several choices.
5.  At the “NUMBER OF DAYS UNTIL STOP:” prompt, enter the desired value or accept the default (optional).
6.  At the “AUTO-DC IMO ORDERS:” prompt, enter the desired value or accept the default (optional).
7.  At the “SEND TO BCMA?” prompt enter the desired value.
8.  At the “Enter MISSING DOSE PRINTER:” prompt, enter the desired value or accept the default (optional).
9.  At the “PRE-EXCHANGE REPORT DEVICE:” prompt, enter the desired value or accept the default (optional).
10. At the “IMO DC/EXPIRED DAY LIMIT:” prompt, enter the desired value or accept the default (optional).
11. At the “CLINIC APPT DATE RANGE MIN:” prompt, enter the desired value or accept the default (optional).
12. At the “CLINIC APPT DATE RANGE MAX:” prompt, enter the desired value or accept the default (optional).
13. At the “OPIOID TREATMENT CLINIC?” prompt enter YES.