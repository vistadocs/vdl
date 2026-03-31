---
title: PADP Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: NUPA
app_name: Patient Assessment Documentation Package (PADP)
section: CLI
app_status: active
pkg_ns: NUPA
patch_ver: 1
patch_id: NUPA*1
group_key: "NUPA:NUPA:1"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - nupa
  - consult
  - class
  - table
  - contents
  - assessment
  - care
  - even
  - health
  - patient
page_count: 0
word_count: 7855
section_count: 22
table_count: 8
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: January 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=193"
---

---
title: Patient Assessment Documentation Package (PADP)
---

C3-C1 Conversion Project

Package Status Update, January 2014:

This package’s status has been changed to Class 3 Software, and will no longer be supported nationally.

Technical Manual for NUPA Version 1.0

![](padp-version-1-technical-manual/001.png)

April 2012

Office of Information and Technology (OIT)

Office of Enterprise Development (OED)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date         | Version | Description                                                                                             | Author                             |
|--------------|---------|---------------------------------------------------------------------------------------------------------|------------------------------------|
| January 2014 |         | This package’s status has been changed to Class 3 Software, and will no longer be supported nationally. | <span class="mark">REDACTED</span> |
| April 2012   | 1.0     | Original release                                                                                        | <span class="mark">REDACTED</span> |
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Anonymous Software and Documentation](#anonymous-software-and-documentation)
  - [TASKMAN Option](#taskman-option)
  - [Delphi GUI Templates in Three (3) Executables](#delphi-gui-templates-in-three-3-executables)
    - [Admission – RN Assessment Template](#admission-rn-assessment-template)
    - [RN Reassessment Template](#rn-reassessment-template)
    - [Interdisciplinary Plan of Care Template](#interdisciplinary-plan-of-care-template)
  - [NUPA Parameters](#nupa-parameters)
    - [Parameter that cannot be edited](#parameter-that-cannot-be-edited)
    - [Parameters that control consults](#parameters-that-control-consults)
    - [Set up Consult Parameters](#set-up-consult-parameters)
    - [Parameters that control other options](#parameters-that-control-other-options)
- [File List and Related Information](#file-list-and-related-information)
  - [Files and Descriptions](#files-and-descriptions)
  - [File Security](#file-security)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [Menu Options and File Access needed](#menu-options-and-file-access-needed)
  - [Edit File NUPA PCE INFO](#edit-file-nupa-pce-info)
  - [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [Archiving](#archiving)
- [External Relationships](#external-relationships)
  - [Required Packages - Minimum](#required-packages-minimum)
  - [Database Integration Agreements](#database-integration-agreements)
- [Internal Relationships](#internal-relationships)
- [Additional Useful Information](#additional-useful-information)
  - [How to Obtain Technology Information](#how-to-obtain-technology-information)
  - [Globals](#globals)
  - [Inquire To Option File](#inquire-to-option-file)
  - [XINDEX](#xindex)
  - [Data Dictionaries Files](#data-dictionaries-files)
  - [List File Attributes](#list-file-attributes)
  - [KIDS Build and Install Print Options](#kids-build-and-install-print-options)
    - [Print Results of the Installation Process](#print-results-of-the-installation-process)
    - [Other Kernel Print Options](#other-kernel-print-options)
- [Cross References](#cross-references)
- [Software Product Security](#software-product-security)
- [Troubleshooting](#troubleshooting)
  - [Screen Resolution](#screen-resolution)
  - [How to Create a Menu Item to Delete Problems and Interventions from Interdisciplinary Care Plan](#how-to-create-a-menu-item-to-delete-problems-and-interventions-from-interdisciplinary-care-plan)
- [Glossary](#glossary)
- [Appendix A List of Health Factors Only for Admission Assessment](#appendix-a-list-of-health-factors-only-for-admission-assessment)
- [Appendix B List of Health Factors Only for Reassessment](#appendix-b-list-of-health-factors-only-for-reassessment)
- [Appendix C Assessment Contingency Note](#appendix-c-assessment-contingency-note)
- [Appendix D Reassessment Contingency Note](#appendix-d-reassessment-contingency-note)
Package Status Update, January 2014:
This package’s status has been changed to Class 3 Software, and will no longer be supported nationally.
In the Package file (#9.4), this application is known as Patient Assessment Documentation (PADP). The package namespace is NUPA. The PADP software application enables Registered Nurses (RNs) to document, in a standardized format, patient care during an inpatient stay. Although the content is standardized for use across the VA system, some parameters can be set to support the unique processes at individual medical centers.
PADP consists of a KIDS build, NUPA 1.0, and four (4) Delphi GUI templates in three executables.
PADP also adds to VistA new health factors, fourteen (14) files, thirty-six (36) parameters, and five (5) printouts.
Printouts
1.  The Daily Plan<sup>®</sup>  
    Nurse and patient collaborate on patient’s care for the day  
    Located in Interdisciplinary Plan of Care, view CP tab
2.  Plan of Care  
    Information shared among patient care staff and patient  
    Located in Interdisciplinary Plan of Care, view CP tab
3.  Discharge Plan  
    Post hospital care information shared by the staff and with the patient  
    Located in Interdisciplinary Plan of Care, view CP tab
4.  Belongings  
    List of belongings the patient brought into the medical center and disposition of the items  
    Located in Admission – RN Assessment/Admission - Nursing Data Collection
5.  Safe Patient Handling  
    Lists staff and equipment required to safely move/transfer patients  
    Located on the Function tab in Admission - RN Assessment, RN Reassessment, and Interdisciplinary Plan of Care, view CP tab
Benefits
- Standardized Documentation of Inpatient Care  
  PADP provides Registered Nurses a standardized format to document patient care that contains parameters that can be set to support the unique processes at individual medical centers.
- Links to Other Packages  
  PADP interfaces directly with several VistA applications, including Computerized Patient Record System (CPRS), Clinical Reminders, Consult Tracking, Mental Health Assessment, Vitals, and Patient Care Encounter (PCE). The linkage between the packages and PADP is transparent to users, but requires setup and coordination by the IRM office and the Clinical Coordinators. For technical information on the previously mentioned packages, refer to the technical and user manuals of the individual packages.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation and maintenance of PADP includes installation of the KIDS build, three (3) executables, and four (4) help files into a folder on a server and placement in CPRS on the Tools menu.

> **NOTE:** Objects also pull data into the templates from the Laboratory and other packages as read-only.

## Anonymous Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADP software and documentation files are available in the following names and formats:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 30%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Document File Description</th>
<th>File Names</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KIDS Build</p>
<p>Executable and Help files</p></td>
<td><p>NUPA_1_0.KID</p>
<p>NUPA.ZIP</p></td>
<td><p>ASCII</p>
<p>Binary</p></td>
</tr>
<tr class="even">
<td>PADP Installation Guide</td>
<td><p>NUPA1_0IG.DOCX</p>
<p>NUPA1_0IG.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP Technical Manual</td>
<td><p>NUPA1_0TM. DOCX</p>
<p>NUPA1_0TM.PDF</p></td>
<td></td>
</tr>
<tr class="even">
<td>PADP Admission – RN Assessment<br />
User Manual</td>
<td><p>NUPA1_0_AUM. DOCX</p>
<p>NUPA1_0_AUM.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP RN Reassessment<br />
User Manual</td>
<td><p>NUPA1_0_RUM. DOCX</p>
<p>NUPA1_0_RUM.PDF</p></td>
<td></td>
</tr>
<tr class="even">
<td>PADP Admission – Nursing Data Collection<br />
User Manual</td>
<td><p>NUPA1_0_DCUM. DOCX</p>
<p>NUPA1_0_DCUM.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP Interdisciplinary Plan of Care<br />
User Manual</td>
<td><p>NUPA1_0_IUM. DOCX</p>
<p>NUPA1_0_IUM.PDF</p></td>
<td></td>
</tr>
</tbody>
</table>

Retrieve these files via FTP from download.vista.med.va.gov, which transmits the files from the first available FTP server (preferred method). You can also retrieve the files directly from one of the following FTP sites:

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Documentation for NUPA Version 1.0 is also available on

VA Software Documentation Library in the Clinical Section  
<http://www4.va.gov/vdl/>

For complete installation instructions, refer to the *PADP Installation Guide*.

- The IRM support staff installs the KIDS build and then unzips the NUPA.ZIP file and places the files in a designated folder on an application server, i.e.: \\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment
- The files contained in the NUPA.ZIP are:
1.  Admassess.exe
2.  Admassess_Shift.exe
3.  Admassess_Careplan.exe
4.  Admassess_CRC.txt
5.  borlndmm.dll
6.  Nupa1_0um help DC.chm
7.  Nupa1_0um help R.chm
8.  Nupa1_0um help IPofC.chm
9.  Nupa1_0um help A.chm

## TASKMAN Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Schedule NUPA PURGE SAVED NOTES Option

1.  Information from notes saved for later: Nursing Admission Data Collection, RN Admission Assessment and RN Reassessment, is in the NUPA SAVED NOTES file (#1927.09).
6.  To purge the NUPA SAVED NOTES file (#1927.09) on a regular basis, the IRM staff must set up the purge option. This will purge any saved (unsigned) information older than five days.
7.  Queue option NUPA PURGE SAVED NOTES to run via Taskman’s Schedule/Unschedule Options (XUTM SCHEDULE) menu to run on a daily basis shortly after midnight.

Select OPTION to schedule or reschedule: NUPA PURGE SAVED NOTES       Purge Saved Notes Over 5 Days Old

         ...OK? Yes//   (Yes)

                        Edit Option Schedule

    Option Name: NUPA PURGE SAVED NOTES

    Menu Text: Purge Saved Notes Over 5 Days Ol          TASK ID: 2885947

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

  QUEUED TO RUN AT WHAT TIME: DEC 4,2009@00:30

 

DEVICE FOR QUEUED JOB OUTPUT:

 

 QUEUED TO RUN ON VOLUME SET:

 

      RESCHEDULING FREQUENCY: 1D

              TASK PARAMETERS:

            SPECIAL QUEUEING:

## Delphi GUI Templates in Three (3) Executables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Admission – RN Assessment Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admission – RN Assessment template can be set up as a single template or subdivided into two templates, resulting in two progress notes. As a single template, one progress note, the RN Admission Assessment note, is generated. The content of the note is the complete assessment including belongings, unit orientation and vital signs.

The executable, Admassess.exe, contains the Admission - RN Assessment template and the Admission - Nursing Data Collection template.

1.  Admission - RN Assessment  
    The note contains information that can be collected only by a registered nurse.
2.  Admission - Nursing Data Collection  
    The note contains information that can be collected by any nursing personnel: Belongings, Orientation to the Unit, and Vital Signs.

### RN Reassessment Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The executable, Admassess_Shift.exe, contains the RN Reassessment template.

RN Reassessment

The note allows RNs to document the condition of the patient on a regular basis and any time during the inpatient stay.

### Interdisciplinary Plan of Care Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Interdisciplinary Plan of Care provides a template for all patient care staff to enter problems, goals and interventions. It is accessible for each admission after the RN Admission Assessment note is uploaded and signed in VistA or CPRS.

The executable, Admassess_Careplan.exe, contains the Interdisciplinary Plan of Care template.

Interdisciplinary Plan of Care

The Interdisciplinary Plan of Care interfaces with admission and reassessment data, and allows additional information to be entered by the RN and other health care personnel (physicians, social workers, chaplain, etc.). All clinical staff can enter information into the Plan of Care. The Plan of Care can be printed and given to the patient when appropriate.

## NUPA Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are thirty-six (36) PADP parameters that are accessed through the \[XPAR EDIT PARAMETER\] option and are located in the PARAMETER DEFINITION FILE (#8989.51).

1 NUPA 508 508 Text

2 NUPA AUTOSAVE TIME Number of minutes until autosave

3 NUPA CHAPLAIN CONSULT Chaplain Consult

4 NUPA COLLECTION TABS TOO DISPLAY DATA COLLECTION TABS TOO?

5 NUPA COSIG FOR STUDENTS COSIG FOR STUDENTS

6 NUPA CURRENT MEDS DATES Dates back for current meds

7 NUPA DIAB NURSE CONSULT Diabetes Nurse Consult

8 NUPA DISCH PLAN CONSULT Discharge Planning consult name

9 NUPA HOME CARE CONSULT Home Care consult name

10 NUPA MAX HEIGHT Maximum height to allow

11 NUPA MAX WEIGHT Maximum weight to allow

12 NUPA MIN HEIGHT Minimum height to allow

13 NUPA MIN WEIGHT Minimum weight to allow

14 NUPA NURSE REHAB CONSULT Rehab consult name

15 NUPA NURSE REST CONSULT Nurse Restorative consult name

16 NUPA NUTRITION CONSULT Nutrition consult name

17 NUPA PCE TAB Display the PCE Tab

18 NUPA PRESSURE ULCER SITE Pressure ulcer site

19 NUPA PSA TEST DATANAME PSA Dataname

20 NUPA RESPIRATORY CONSULT Respiratory consult name

21 NUPA SAVE MORE THAN ONE NOTE Save more than one note?

22 NUPA SEND DIAB NURSE CONS Send Diabetes Nurse Consult

23 NUPA SEND DISCH PLAN CONSULT Send Discharge Planning Consult

24 NUPA SEND HOME CARE CONSULT Send Home Care Consult

25 NUPA SEND NURSE REHAB CONSULT Send Nurse Rehab consult

26 NUPA SEND NURSE REST CONSULT Send Nurse Rest. consult

27 NUPA SEND RESPIRATORY CONSULT Send respiratory consult

28 NUPA SEND TELEHEALTH CONSULT Send Telehealth Consult

29 NUPA SEND WOMENS H CONSULT Send Women's Health consult

30 NUPA SOCIAL WORK CONSULT Social Work consult name

31 NUPA SPEECH CONSULT Speech consult name

32 NUPA TABSAVE Number of tab switches before auto-save

33 NUPA TELEHEALTH CONSULT Telehealth Consult name

34 NUPA TIMEOUT Assessment Timeout

35 NUPA WOMENS HEALTH CONSULT Women's Health Consult name

36 NUPA WOUND CARE CONSULT Wound care consult

> **NOTE:** All required parameters must be set up before the PADP templates will open. If not, an error message notifies you that the parameter is not set up properly.

### Parameter that cannot be edited

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 NUPA 508 508 Text

### Parameters that control consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following parameters control consults that can be ordered from the PADP templates.

#### The following parameters control Required consults

NUPA CHAPLAIN CONSULT Chaplain Consult

NUPA NUTRITION CONSULT Nutrition consult name

NUPA PRESSURE ULCER SITE Pressure ulcer site

NUPA SOCIAL WORK CONSULT Social Work consult name

NUPA SPEECH CONSULT Speech consult name

NUPA WOUND CARE CONSULT Wound care consult

#### The following parameters control optional consults

The optional consults are controlled by the NUPA SEND parameters.

Controlling Consults

NUPA SEND DIAB NURSE CONS Send Diabetes Nurse Consult

NUPA SEND DISCH PLAN CONSULT Send Discharge Planning Consult

NUPA SEND HOME CARE CONSULT Send Home Care Consult

NUPA SEND NURSE REHAB CONSULT Send Nurse Rehab consult

NUPA SEND NURSE REST CONSULT Send Nurse Rest. consult

NUPA SEND RESPIRATORY CONSULT Send respiratory consult

NUPA SEND TELEHEALTH CONSULT Send Telehealth Consult

NUPA SEND WOMENS H CONSULT Send Women's Health consult

Optional Associated Consults

Enter the Associated Consult Specialty in the parameter for each Controlling Consult Parameter

you will use in your PADP templates.

NUPA DIAB NURSE CONSULT Diabetes Nurse Consult

NUPA DISCH PLAN CONSULT Discharge Planning consult name

NUPA HOME CARE CONSULT Home Care consult name

NUPA NURSE REHAB CONSULT Rehab consult name

NUPA NURSE REST CONSULT Nurse Restorative consult name

NUPA TELEHEALTH CONSULT Telehealth Consult name

NUPA WOMENS HEALTH CONSULT Women's Health Consult name

### Set up Consult Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up the parameters, perform the following steps.

1.  Review the consults in your system.
2.  Identify the consult specialties that you order via the notes: RN Admission Assessment and RN Reassessment.
3.  Access the PADP parameters using the Edit Parameter Values \[XPAR EDIT PARAMETER\] option.
1.  Select Menu Option: IR CPRS Configuration (IRM).
10. Select CPRS Configuration (IRM) Option: XX General Parameter Tools.
11. Select General Parameter Tools Option: <span class="mark">EP Edit Parameter Values</span>
4.  Parameters can be set at three levels: System, Division, or Location
5.  PADP first checks at the lowest level: Location, then Division, and lastly the System.
- If you are a single division medical center, set the parameter at System or Division level. Associate the System or Division with the appropriate consult.
- If there is only one consult for a Specialty for the entire system or division, set the parameter at the System or Division level. Associate the System or Division with the appropriate consult.
- If there is one consult for a Specialty per Division, set the parameter at the Division level. Associate each Division with the appropriate consult.
- If there is more than one consult per Specialty for a Division, like one social work consult for Med/Surg units and another one for Mental Health/Psych units, set the parameter at the Location (MAS bed section, ward) level. Associate each Location with the appropriate consult.

Examples

#### Set One Consult Service per Specialty in the System

Select PARAMETER DEFINITION NAME: NUPA CHAPLAIN CONSULT

NUPA CHAPLAIN CONSULT may be set for the following:

1 Division DIV \[choose from INSTITUTION\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 3 System

Select SYSTEM NAME: TEST.BRONX.MED.VA.GOV

---------- Setting NUPA CHAPLAIN CONSULT for System:

Consult name: CHAPLAIN

#### Set One Consult Service per Specialty per Division for Multi-division Sites

Select PARAMETER DEFINITION NAME: NUPA CHAPLAIN CONSULT

NUPA CHAPLAIN CONSULT may be set for the following:

1 Division DIV \[choose from INSTITUTION\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 1 Division

Select INSTITUTION NAME: Bronx VAMC DIVISION ONE

---------- Setting NUPA CHAPLAIN CONSULT for Division: BRONX VAMC ----------

Consult name: CHAPLAIN DIVISION ONE

You can set up another consult for another division in the system by setting up a second Chaplain Consult for VAMC Division Two. Use the same name for the consult as used in Division Two.

Select PARAMETER DEFINITION NAME: NUPA CHAPLAIN CONSULT

NUPA CHAPLAIN CONSULT may be set for the following:

1 Division DIV \[choose from INSTITUTION\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 1 Division

Select INSTITUTION NAME: Bronx VAMC DIVISION TWO

---------- Setting NUPA CHAPLAIN CONSULT for Division: BRONX VAMC ----------

Consult name: CHAPLAIN DIVISION TWO

#### Set One Consult Service per Specialty per Hospital Location

In many medical centers, there are no centralized services to manage specialties, like Social Work or Nutrition. Because each clinician works only with patients from assigned Nursing Units, ordered consults must go to a specific clinician to promote prompt response and safe patient care. This process is supported by the ability to set up consults services at the Hospital Locations associated with Nursing Units.

Example

There are two MAS hospital locations associated with the Nursing Unit Spinal Cord Units, 1D and 1E. Set the parameter for each MAS hospital location, so that patients in either Hospital Location generate the same consult service per specialty: NUTRITION INPT SCI.

Setting for Location: 1D:

Select PARAMETER DEFINITION NAME: NUPA NUTRITION CONSUSLT

NUPA NUTRITION CONSULT may be set for the following:

1 Division DIV \[choose from INSTITUTION\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 2 Location HOSPITAL LOCATION

Select HOSPITAL LOCATION NAME: 1D

-------------- Setting NUPA NUTRITION CONSULT for Location: 1D --------------

Consult name: NUTRITION INPT SCI

Setting for Location: 1E:

Select PARAMETER DEFINITION NAME: NUPA NUTRITION CONSULT

NUPA NUTRITION CONSULT may be set for the following:

1 Division DIV \[choose from INSTITUTION\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 2 Location HOSPITAL LOCATION

Select HOSPITAL LOCATION NAME: 1E

-------------- Setting NUPA NUTRITION CONSULT for Location: 1E --------------

Nutrition consult name: NUTRITION INPT SCI

When a Nutrition Consult is ordered for a patient on Nursing Unit SCI, a NUTRITION INPT SCI consult is ordered and displays on the CPRS Orders tab. No other inpatient nutritionist receives the consult alert, only the nutritionist associated with the consult NUTRITION INPT SCI.

### Parameters that control other options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUPA AUTOSAVE TIME Number of minutes until autosave

Value: Number of minutes of before an autosave will occur. Range 3-10.

NUPA COLLECTION TABS TOO

Allows display of the Orient and Vital Signs tabs in the Admission Assessment.

Enter “Y” or “N” in value field.

NUPA COSIG FOR STUDENTS

Require co-signatures for students:

Enter either “Y” or “N” in value field.

NUPA CURRENT MEDS DATES

Dates back for current meds: //

This is the number of days back to display the active meds. If you enter 45 days,

for example, the assessment will search for meds that were active from today to 45

days ago.

NUPA MAX HEIGHT

Maximum height to allow: //

This is the maximum height in inches that the nurses can enter into the Height field

on the Vitals tab.

NUPA MAX WEIGHT

Maximum weight to allow: //

This is the maximum weight in pounds that the nurses can enter into the Weight field

on the Vitals tab.

NUPA MIN HEIGHT

Minimum height to allow: //

This is the minimum height in inches that the nurses can enter into the Height field

on the Vitals tab.

Minimum weight to allow: //

This is the minimum weight in pounds that the nurses can enter into the Weight field

on the Vitals tab.

NUPA PRESSURE ULCER SITE

Value: vaww1.va.gov/nursing/docs/npuap_press_ulcer_stages_rev_2-07.doc

Linkage to website for pressure ulcer staging.

NUPA PSA TEST DATANAME

PSA Dataname:

This is the Data Name of the PSA (PROSTATE SPECIFIC ANTIGEN) test at your site. This

is found in ^DD(63.04), not in the Lab Test file (#60). For additional Lab information

refer to the Laboratory Package manuals located on the VA Software Documentation

Library in the Clinical Section: <http://www4.va.gov/vdl/> .

NUPA SAVE MORE THAN ONE NOTE

Value: // Enter either 'Y' or 'N' in value field.

Allows nurses to save notes on more than one patient in the RN Assessment and

Re-assessment.

NUPA TABSAVE

Number of tab switches before auto-save: //

Number of times that the user can switch tabs or pages before the program will

autosave their data. Default is 5. Range can be 5-20.

NUPA TIMEOUT

Assessment Timeout: //

Number in minutes that the program will time out after no action.

# File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUPA KIDS build installs the following files.

| Global          | Name                                        |
|-----------------|---------------------------------------------|
| ^NUPA(1927.09   | NUPA SAVED NOTES                            |
| ^NUPA(1927.2    | NUPA ASSESSMENT PROBLEMS                    |
| ^NUPA(1927.23   | NUPA PLAN DESCRIPTION TABS (including data) |
| ^NUPA(1927.24   | NUPA ASSESSMENT INTERVENTIONS               |
| ^NUPA(1927.3    | NUPA ASSESSMENT DESCRIPTIONS                |
| ^NUPA(1927.32   | NUPA PCE INFO                               |
| ^NUPA(1927.4    | NUPA CARE PLANS                             |
| ^NUPA(1927.401  | NUPA CARE PLAN PRESSURE ULCERS              |
| ^NUPA(1927.4011 | NUPA CARE PLAN SKIN ALT TYPES               |
| ^NUPA(1927.402  | NUPA CARE PLAN IVS                          |
| ^NUPA(1927.403  | NUPA CARE PLAN GI/GU DEVICES                |
| ^NUPA(1927.41   | NUPA COMPONENT ITEMS                        |
| ^NUPA(1927.5    | NUPA CARE PLAN TEXT CHANGE LOG              |
| ^NUPA(1927.6    | NUPA DISCHARGE PLANNING GOAL COMMENTS       |

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>File #</th>
<th>File Name</th>
<th>File Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1927.09</td>
<td>NUPA SAVED NOTES</td>
<td><p>The <strong>Nursing Admission Data Collection</strong>, <strong>RN Admission Assessment</strong>, and <strong>RN Reassessment</strong> notes are saved in this file while moving from tab to tab.</p>
<p>The <strong>Save and exit</strong> option stores this file.</p></td>
</tr>
<tr class="even">
<td>1927.2</td>
<td>NUPA ASSESSMENT PROBLEMS</td>
<td><p>Multidisciplinary problems are stored in this file.</p>
<p>This is the file from which you select problems while documenting patient care.</p></td>
</tr>
<tr class="odd">
<td>1927.23</td>
<td>NUPA PLAN DESCRIPTION TABS</td>
<td><p>Descriptions of the tabs to which problems are related, are stored in this file.</p>
<p>Example: CV (Cardiovascular) Chest Pain</p></td>
</tr>
<tr class="even">
<td>1927.24</td>
<td>NUPA ASSESSMENT INTERVENTIONS</td>
<td><p>Interventions for problems are stored in this file.</p>
<p>This is the file from which you select interventions while documenting patient care.</p></td>
</tr>
<tr class="odd">
<td>1927.3</td>
<td>NUPA ASSESSMENT DESCRIPTIONS</td>
<td>Descriptions of the various patient problems in nursing language are stored in this file.</td>
</tr>
<tr class="even">
<td>1927.32</td>
<td>NUPA PCE INFO</td>
<td><p>Before the Health Factors are loaded into PCE, they are stored in this file.</p>
<p>(This file is empty until Health Factors are loaded onto the system.)</p></td>
</tr>
<tr class="odd">
<td>1927.4</td>
<td>NUPA CARE PLANS</td>
<td>Interdisciplinary Care Plans are stored in this file.</td>
</tr>
<tr class="even">
<td>1927.401</td>
<td>NUPA CARE PLAN PRESSURE ULCERS</td>
<td>Skin pressure ulcer information is saved in this file.</td>
</tr>
<tr class="odd">
<td>1927.4011</td>
<td>NUPA CARE PLAN SKIN ALT TYPES</td>
<td>Skin alteration information is saved in this file.</td>
</tr>
<tr class="even">
<td>1927.402</td>
<td>NUPA CARE PLAN IVS</td>
<td>IV information is stored in this file.</td>
</tr>
<tr class="odd">
<td>1927.403</td>
<td>NUPA CARE PLAN GI/GU DEVICES</td>
<td>GI device information is stored in this file.</td>
</tr>
<tr class="even">
<td>1927.41</td>
<td>NUPA COMPONENT ITEMS</td>
<td>Various items related to available choices in the Care Plan are stored in this file.</td>
</tr>
<tr class="odd">
<td>1927.5</td>
<td>NUPA CARE PLAN TEXT CHANGE LOG</td>
<td>Changes made to the Care Plan are stored in this file; includes what changed, when it changed, and by whom it was changed.</td>
</tr>
<tr class="even">
<td>1927.6</td>
<td>NUPA DISCHARGE PLANNING GOAL COMMENTS</td>
<td>Discharge planning goal comments are stored in this file.</td>
</tr>
</tbody>
</table>

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table contains the security that is established for PADP files.

| File \#   | Name                                  | DD  | RD  | WR  | DEL | LAYGO | AUDIT |
|-----------|---------------------------------------|-----|-----|-----|-----|-------|-------|
| 1927.09   | NUPA SAVED NOTES                      | @   |     | @   | @   | @     | @     |
| 1927.2    | NUPA ASSESSMENT PROBLEMS              | @   |     | @   | @   | @     | @     |
| 1927.23   | NUPA PLAN DESCRIPTION TABS            | @   |     | @   | @   | @     | @     |
| 1927.24   | NUPA ASSESSMENT INTERVENTIONS         | @   |     | @   | @   | @     | @     |
| 1927.3    | NUPA ASSESSMENT DESCRIPTIONS          | @   |     | @   | @   | @     | @     |
| 1927.32   | NUPA PCE INFO                         | @   | Nn  | Nn  | Nn  | Nn    | @     |
| 1927.4    | NUPA CARE PLANS                       | @   |     | @   | @   | @     | @     |
| 1927.401  | NUPA CARE PLAN PRESSURE ULCERS        | @   |     | @   | @   | @     | @     |
| 1927.4011 | NUPA CARE PLAN SKIN ALT TYPES         | @   |     | @   | @   | @     | @     |
| 1927.402  | NUPA CARE PLAN IVS                    | @   |     | @   | @   | @     | @     |
| 1927.403  | NUPA CARE PLAN GI/GU DEVICES          | @   |     | @   | @   | @     | @     |
| 1927.41   | NUPA COMPONENT ITEMS                  | @   |     | @   | @   | @     | @     |
| 1927.5    | NUPA CARE PLAN TEXT CHANGE LOG        | @   |     | @   | @   | @     | @     |
| 1927.6    | NUPA DISCHARGE PLANNING GOAL COMMENTS | @   |     | @   | @   | @     | @     |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Namespace: NUPA

XUPRROU (List Routines) prints a list of any or all of the NUPA routines. This option is on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Example

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: list Routines

Routine Print

Want to start each routine on a new page: No// \[ENTER\]

routine(s) ? \> NUPA\*

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option, First Line Routine Print \[XU FIRST LINE PRINT\], to print a list of only the first line of each NUPA subset routine.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: First Line Routine Print

PRINTS FIRST LINES

routine(s) ? \>NUPA\*

All Routines? No =\> No

Routine: NUPABCL

Routine: NUPABCL1

Routine: NUPABCL2

Routine: NUPAOBJ

Routine: NUPAOBJ1

Routine: NUPAPI

Routine: NUPAPI1

Routine: NUPAPI2

Routine:

8 routines

NUPABCL ;PHOENIX/KLD; 7/1/99; ADMISSION ASSESSMENT BROKER CALL UTILITIES;

1/11/12 8:37 AM;;1.0;NUPA;;;Build 100

NUPABCL1;PHOENIX/KLD; 11/13/00; BROKER CALL UTILITIES RELATING TO THE

ADMISSION ASSESSMENT; 1/11/12 8:37 AM;;1.0;NUPA;;;Build 100

NUPABCL2;PHOENIX/KLD; 2/23/09; ADMISSION ASSESSMENT/CAREPLAN BROKER CALLS;

1/13/12 3:55 PM;;1.0;NUPA;;;Build 100

NUPAOBJ;PHOENIX/KLD; 6/23/09; PULL PATIENT INFO; 1/11/12 8:38 AM

;;1.0;NUPA;;;Build 100

NUPAOBJ1;PHOENIX/KLD; 6/23/09; PULL PATIENT INFO; 1/11/12 8:38 AM

;;1.0;NUPA;;;Build 100

NUPAPI;PHOENIX/KLD; 7/15/09; NUPA PRE & POST-INITS; 1/13/12 1:29 PM

;;1.0;NUPA;;;Build 100

NUPAPI1;PHOENIX/KLD; 7/15/09; NUPA POST-INIT; 1/13/12 1:29 PM

;;1.0;NUPA;;;Build 100

NUPAPI2;PHOENIX/KLD; 7/15/09; NUPA POST-INIT; 1/13/12 1:29 PM

;;1.0;NUPA;;;Build 100

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Options and File Access needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following NEW option is allocated to the clinical staff that will enter data into any of the four PADP templates. This should be assigned as a secondary menu option.

| Option                  | Option Name         | Description                                                                                 |
|-------------------------|---------------------|---------------------------------------------------------------------------------------------|
| NUPA Assessment GUI RPC | NUPA Assessment GUI | This option is assigned to all staff who will enter data into any of the four (4) templates |

8.  The following option is allocated to the IRM or to the CAC/ADPAC to set up files and parameters.

| Option          | Option Name          | Description                                     |
|-----------------|----------------------|-------------------------------------------------|
| Edit Parameters | XPAR Edit Parameters | This menu allows the editing of NUPA parameters |

9.  The following OPTIONAL access is allocated to the IRM or to the CAC/ADPAC to set up files for Clinical Reminders on the PCE tab in the Admission – RN Assessment template and the RN Reassessment Template.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 28%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Option Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enter/Edit File</td>
<td>FileMan access with Nn</td>
<td><p>This option allows the setup of Clinical Reminders on the PCE tab in the</p>
<ul>
<li><p>Admission – RN Assessment template</p></li>
<li><p>RN Reassessment template</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Edit File NUPA PCE INFO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Nursing Reminders are edited using NUPA PCE INFO file (#1927.32). This functionality is optional.

1.  If your site decides to use this functionality, the person entering the information needs access to FileMan and needs Nn to go into the File Manager Access Code field in the NEW PERSON file (#200) and will also need the following access added to file \#1927.32 -- Read, Write, Delete, and Laygo access.
10. At sites that do not authorize the CACs to use FileMan, an IT person must work with the CAC to complete the setup.

Examples that follow are from one medical center and are presented here only as an example.

Enter or Edit File Entries

Print File Entries

Search File Entries

Inquire to File Entries

List File Attributes

Select File Manager Option: ENTER or Edit File Entries

INPUT TO WHAT FILE: NUPA PCE INFO//

EDIT WHICH FIELD: ALL//

Example 1  
Advance Directives Education

Select NUPA PCE INFO NAME: Advance Directives Education

...OK? Yes// (Yes)

NAME: Advance Directives Education

ASK HAD: YES// (did the patient have it someplace else)

HAD HEALTH FACTOR: ADVANCE DIRECTIVES ADEQUATELY EDUCATED//

HAD EDUCATION TOPIC: ADVANCE DIRECTIVES//

ASK RECEIVED PREVIOUSLY: YES//

RECEIVED PREV HEALTH FACTOR: ADVANCE DIRECTIVES ADEQUATELY EDUCATED//

RECEIVED PREV EDUCATION TOPIC: ADVANCE DIRECTIVES//

RECEIVED PREV ASK DATE: YES//

RECEIVED PREV ASK LOC: YES//

ASK DECLINED: YES//

DECLINED HEALTH FACTOR: ADVANCE DIRECTIVE SCREENING REFUSED //

DECLINED EDUCATION TOPIC:

ASK N/A: YES//

N/A HEALTH FACTOR:

N/A EDUCATION TOPIC:

QUESTION TEXT:

Example 2  
Pain Education

Select ASSESSMENT REMINDER NAME: Pain Education

...OK? Yes// (Yes)

NAME: Pain Education//

ASK HAD: YES//

HAD HEALTH FACTOR: PHE PAIN RN ASSESSMENT//

HAD EDUCATION TOPIC: PAIN EDUCATION//

ASK RECEIVED PREVIOUSLY: YES//

RECEIVED PREV HEALTH FACTOR: PHE PAIN RN ASSESSMENT //

RECEIVED PREV EDUCATION TOPIC: PAIN EDUCATION//

RECEIVED PREV ASK DATE: YES//

RECEIVED PREV ASK LOC: YES//

ASK DECLINED: YES//

DECLINED HEALTH FACTOR: REFUSED//

DECLINED EDUCATION TOPIC: PAIN ED DECLINED//

ASK N/A: YES//

N/A HEALTH FACTOR: PAIN ED NOT APPLICABLE//

N/A EDUCATION TOPIC: PAIN ED NOT APPLICABLE//

QUESTION TEXT:

How it looks on the PADP template

1.  Click Resolve on the PCE DATA window.

![](padp-version-1-technical-manual/002.png)

Admission - RN Assessment, PCE DATA, PCE tab window

11. Click Resolve on the Resolve Reminder window.

![](padp-version-1-technical-manual/003.png)

Resolve Reminder window

Additional Examples

NAME: Basic Health Practices And Safety

  ASK HAD: YES

  HAD EDUCATION TOPIC: BASIC HEALTH PRACTICES AND SAFETY

  ASK DECLINED: YES

  DECLINED EDUCATION TOPIC: BASIC HEALTH PRACTICES AND SAFETY

  QUESTION TEXT: Health Practices And Safety

NAME: Inpt Plan of Care Tx & Services   ASK HAD: YES

  HAD EDUCATION TOPIC: PLAN OF CARE, TREATMENT, AND SERVICES

  ASK DECLINED: YES

  DECLINED EDUCATION TOPIC: PLAN OF CARE, TREATMENT, AND SERVICES

  QUESTION TEXT: Inpt Plan of Care Tx

NAME: Nutr Intervention, Diet, and Oral Health

  ASK HAD: YES

  HAD EDUCATION TOPIC: NUTRITION INTERVENTIONS, MODIFIED DIETS OR ORAL HEALTH

  ASK DECLINED: YES

  DECLINED EDUCATION TOPIC: NUTRITION INTERVENTIONS, MODIFIED DIETS OR ORAL HEALTH

  ASK N/A: YES

  N/A HEALTH FACTOR: NUTRITION INTERVENTIONS N/A

  QUESTION TEXT: Nutrition/Oral Health Education

## Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Remote Procedure Call ( RPC) is a procedure called from the client (the user’s workstation) communicating to the server (the M database). The nursing assessment templates require the following new RPCs to facilitate communication between the templates and the server.

1   NUPA CAREPLAN HISTORY 

     2   NUPA CAREPLAN PROBLEM HISTORY 

     3   NUPA CAREPLAN PROBS 

     4   NUPA DLOOK 

     5   NUPA DP COMMENT HISTORY 

     6   NUPA FILE           

     7  NUPA GET COMPONENTS 

     8  NUPA GET GI DEVICES 

     9  NUPA GET HEALTH FACTORS 

     10  NUPA GET IVS 

     11  NUPA GET PRESSURE ULCERS 

     12  NUPA GET SKIN ALT 

     13  NUPA INP MEDS LIST 

     14  NUPA LIST 

     15  NUPA LIST2 

     16  NUPA LOOKUP 

     17  NUPA LOOKUP TRY 2 

     18  NUPA NEW 

     19  NUPA NEW IF NONE 

     20  NUPA ORDER 

     21  NUPA PRINT 

     22  NUPA REASSESSMENT RADIOBUTTONS 

     23  NUPA REMINDERS COLLECT 

     24  NUPA REMINDERS GET 

     25  NUPA REMINDERS MANUAL 

     26  NUPA RUN OBJECT (\>1 LINE) 

     27  NUPA SCREEN 

     28  NUPA USER CLASS 

     29  NUPA WP GET

     30  NUPA WP SET 

     

A complete listing of RPCs is available under the DBA menu on FORUM.

MENU TEXT: NUPA Assessment TYPE: Broker (Client/Server)

CREATOR: DEVELOPER, ONE

DESCRIPTION: Required for people to use GUI routines for creating nursing notes.

XWB GET VARIABLE VALUE

TIU CREATE ADDENDUM RECORD

TIU CREATE RECORD

TIU DELETE RECORD

DDR DELETE ENTRY

ORWU DT

ORWU CLINLOC

ORWPCE SAVE

ORWDX SAVE

ORQQVI2 VITALS VALIDATE

ORWDAL32 ALLERGY MATCH

ORWDAL32 DEF

DG SENSITIVE RECORD ACCESS

DG SENSITIVE RECORD BULLETIN

ORWRP GET DEFAULT PRINTER

ORWU PARAM

ORQQPXRM REMINDER DETAIL

ORQQPXRM REMINDER INQUIRY

ORWTPP GETCOS

ORQQPX GET DEF LOCATIONS

GMV ADD VM

GMV MANAGER

ORPRF HASFLG

ORWDAL32 SAVE ALLERGY

NUPA CAREPLAN HISTORY 

 NUPA CAREPLAN PROBLEM HISTORY 

 NUPA CAREPLAN PROBS 

 NUPA DLOOK 

 NUPA DP COMMENT HISTORY 

 NUPA FILE           

 NUPA GET COMPONENTS 

 NUPA GET GI DEVICES 

 NUPA GET HEALTH FACTORS 

 NUPA GET IVS 

 NUPA GET PRESSURE ULCERS 

 NUPA GET SKIN ALT 

 NUPA INP MEDS LIST 

 NUPA LIST 

 NUPA LIST2 

 NUPA LOOKUP 

 NUPA LOOKUP TRY 2 

 NUPA NEW 

 NUPA NEW IF NONE 

 NUPA ORDER 

 NUPA PRINT 

 NUPA REASSESSMENT RADIOBUTTONS 

 NUPA REMINDERS COLLECT 

 NUPA REMINDERS GET 

 NUPA REMINDERS MANUAL 

 NUPA RUN OBJECT (\>1 LINE) 

 NUPA SCREEN 

 NUPA USER CLASS 

 NUPA WP GET

 NUPA WP SET

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving for the Patient Admission Assessment Package.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Packages - Minimum

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADP requires that the following software is installed and fully patched.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Package</th>
<th>Namespace</th>
<th>Minimum Version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td>2.0*5</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td><p>OR</p>
<p>OR</p></td>
<td><p>1.0.27.90</p>
<p>3.0*243</p></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>XM</td>
<td>8.0</td>
</tr>
<tr class="odd">
<td>Text Integration Utilities</td>
<td>TIU</td>
<td>1.0</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>DI</td>
<td>22.0</td>
</tr>
<tr class="odd">
<td>Vitals/Measurements</td>
<td>GMRV</td>
<td>5.0*22</td>
</tr>
<tr class="even">
<td>Adverse Reaction Tracking</td>
<td>GMRA</td>
<td>4.0*42</td>
</tr>
<tr class="odd">
<td>Consult Request Tracking</td>
<td>GMRC</td>
<td>3.0*1</td>
</tr>
<tr class="even">
<td>Remote Procedure Call</td>
<td>XWB</td>
<td>1.1*47</td>
</tr>
<tr class="odd">
<td><p>MHA DLL (Mental Health Assistant DLL)</p>
<p>Mental Health Assistant</p></td>
<td><p>YS*5.01*98</p>
<p>All YS* patches</p></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Care Encounter</td>
<td>PX</td>
<td>1</td>
</tr>
</tbody>
</table>

## Database Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers that allow the use of internal entry points or other software-specific features not available to the general programming public. A complete list of Integration Agreements (IAs)are under the DBA menu on FORUM.

Non-destructive, read-only component routines are written to present VistA ancillary package data.

The package interacts with, and extracts data from, many other VistA software packages. Permission to use data from the other packages is obtained by completing a written integration agreement with each of the other packages.

Select INTEGRATION REFERENCES: nupa

1 NUPA 5543 PATIENT ASSESSMENT DOCUM Controlled Subscription  
RPC's for NUPA in rtn: NUPABCL

2 NUPA 5544 PATIENT ASSESSMENT DOCUM Controlled Subscription

RPC's for NUPA in rtn: NUPABCL1

3 NUPA 5545 PATIENT ASSESSMENT DOCUM Controlled Subscription

RPC's for NUPA in rtn: NUPABCL2

4 NUPA 5569 PCE PATIENT CARE ENCOUNTER Controlled Subscription

HEALTH FACTORS FOR PADP

To obtain the current list of Integration Agreements to which PADP is a custodian, follow the example.

Select Integration Agreements Menu Option: 8 \<Enter\> Custodial Package Menu

1 ACTIVE by Custodial Package

2 Print ALL by Custodial Package

3 Supported References Print All

Select Custodial Package Menu Option: 1 \<Enter\> ACTIVE by Custodial Package

Select PACKAGE NAME: NUPA

DEVICE: HOME// \<Enter\> UCX DEVICE Right Margin: 80// \<Enter\>

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines, files or options within this VistA software, which cannot function independently.

# Additional Useful Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Obtain Technology Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace of Patient Admission Assessment is NUPA.

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADP uses the ^NUPA global. Use the Kernel option, List Global \[XUPRGL\], to print a list of the NUPA globals. This option is on the Programmer Options menu \[XUPROG\], which is a sub-menu of the Systems Manager Menu \[EVE\] option.

Example

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: LIST Global

Global ^NUPA \*

## Inquire To Option File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Inquire option \[XUINQUIRE\] provides information about a specified option(s).

- Option name
- Menu text
- Option description
- Type of option
- Lock (if any)

In addition, all items on an individual menu are listed for each menu option.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines.

XINDEX provides

- a summary of errors and warnings for routines that do not comply with VA programming standards and conventions
- a list of local and global variables and in which routines they are referenced
- a list of internal and external routine calls

XINDEX is invoked from programmer mode: D ^XINDEX.

When selecting routines, select XXX\* .

## Data Dictionaries Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The numberspaces for PADP files are 1927.09-1927.6.

- Use the VA FileMan DATA DICTIONARY UTILITIES, option \#8 (DILIST, List File Attributes), to print a list of these files.
- Depending on the FileMan template used to print the list, this option prints out all or part of the data dictionary for the PXRM files.

Example

\>D P^DI

VA FileMan 21.0

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: 1927

(1 entry)

GO TO WHAT FILE: 1927.5

Select LISTING FORMAT: STANDARD// \[Enter\]

DEVICE: PRINTER

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan List File Attributes option \[DILIST\] generates documentation about files and file structure. The *Standard* format allows you to view the Data Dictionary information for a specified file(s):

- File name and description
- Identifiers
- Cross-references
- Files that are pointed to by the file specified
- Files that point to the file specified
- Input templates
- Print templates

In addition, applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

The *Global Map* format of this option generates an output that lists all cross-references for the selected file, global location of each field in the file, input templates, print templates, and sort templates.

## KIDS Build and Install Print Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print a complete listing of package components, such as routines and options, exported with this software, use the KIDS Build File Print option.

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System menu

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Utilities

Build File Print

Install File Print

Convert Loaded Package for Redistribution

Display Patches for a Package

Purge Build or Install Files

Rollup Patches into a Build

Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities Option: Build File Print

Select BUILD NAME: NUPA\*1.0\*0

### Print Results of the Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print out the results of the installation process, use the KIDS Install File Print option.

Select Utilities Option: Install File Print

Select INSTALL NAME: NUPA\*1.0\*0

DEVICE: HOME// ;;999 ANYWHERE

### Other Kernel Print Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the Kernel Installation & Distribution (KIDS) options for routines, files, and so on, other Kernel options can be used to print technical information.

# Cross References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no non-standard or special cross-references.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security is handled by KERNEL. Only the sign-on and menu options mechanisms are utilized; no keys are necessary.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Screen Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Admission Assessment seems to be too big for the workstation, change the screen resolution using your workstation Display options.

## How to Create a Menu Item to Delete Problems and Interventions from Interdisciplinary Care Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan Version 22.0

1 Enter or Edit File Entries

Select OPTION: 1  ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: NUPA CARE PLANS//

EDIT WHICH FIELD: ALL// 30  INTERVENTIONS  (multiple)

   EDIT WHICH INTERVENTIONS SUB-FIELD: ALL//

THEN EDIT FIELD: 31  PROBLEMS  (multiple)

   EDIT WHICH PROBLEMS SUB-FIELD: ALL//

THEN EDIT FIELD: W !!,"Be sure to make an addendum to the IDPC note stating what is wrong."

THEN EDIT FIELD:

STORE THESE FIELDS IN TEMPLATE: NUPA DELETE PROBLEMS

  Are you adding 'NUPA DELETE PROBLEMS' as

    a new INPUT TEMPLATE? No// Y  (Yes)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADPAC</td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="even">
<td>ART</td>
<td>Adverse Reactions Tracking</td>
</tr>
<tr class="odd">
<td>BCE</td>
<td>Bar Code Expansion</td>
</tr>
<tr class="even">
<td>BCE-PPI</td>
<td>Bar Code Expansion-Positive Patient Identification</td>
</tr>
<tr class="odd">
<td>BCMA</td>
<td>Bar Code Medication Administration</td>
</tr>
<tr class="even">
<td>Belong</td>
<td>Belongings</td>
</tr>
<tr class="odd">
<td>CAC</td>
<td>Clinical Application Coordinator</td>
</tr>
<tr class="even">
<td>CIWA</td>
<td>Clinical Institute Withdrawal Assessment.--CIWA</td>
</tr>
<tr class="odd">
<td>Class 1 (C1)</td>
<td>Software produced inside of the Office of Enterprise Development (PD) organization</td>
</tr>
<tr class="even">
<td>Class 3 (C3)</td>
<td><p>Also known as Field Developed Software</p>
<p>Refers to all VHA software produced outside of the Office of Enterprise Development (PD) organization</p></td>
</tr>
<tr class="odd">
<td>CMS</td>
<td>Centers for Medicaid and Medicare Services</td>
</tr>
<tr class="even">
<td>COTS</td>
<td>Commercial Off the Shelf</td>
</tr>
<tr class="odd">
<td>CP</td>
<td>Care Plan</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>CV</td>
<td>Cardiovascular Assessment</td>
</tr>
<tr class="even">
<td>Delphi</td>
<td>Programming language used to develop the CPRS chart</td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>Data File Number</td>
</tr>
<tr class="even">
<td>DP</td>
<td>Discharge Planning</td>
</tr>
<tr class="odd">
<td>Educ</td>
<td>Educational Assessment</td>
</tr>
<tr class="even">
<td>Func</td>
<td>Functional Assessment</td>
</tr>
<tr class="odd">
<td>Gen Inf</td>
<td>General Information tab</td>
</tr>
<tr class="even">
<td>GI</td>
<td>Gastrointestinal Assessment</td>
</tr>
<tr class="odd">
<td>GU</td>
<td>Genitourinary Assessment</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="odd">
<td>ICD</td>
<td>International Classification of Diseases</td>
</tr>
<tr class="even">
<td>ICN</td>
<td>The patient’s national identifier, Integration Control Number</td>
</tr>
<tr class="odd">
<td>IDPA</td>
<td>Interdisciplinary Patient Assessment - involves multiple disciplines responsible for assessing the patient from their perspective and expertise.</td>
</tr>
<tr class="even">
<td>IDPC</td>
<td>Interdisciplinary Plan of Care - The entry of treatment plans by multiple disciplines to meet JCAHO requirements</td>
</tr>
<tr class="odd">
<td>IV</td>
<td>Intravenous</td>
</tr>
<tr class="even">
<td>IV Central</td>
<td>Central IV lines</td>
</tr>
<tr class="odd">
<td>IV Dialysis</td>
<td>IV Dialysis ports</td>
</tr>
<tr class="even">
<td>IV Periph</td>
<td>IV Peripheral lines</td>
</tr>
<tr class="odd">
<td>JCAHO</td>
<td>Joint Commission on Accreditation of Healthcare Organizations</td>
</tr>
<tr class="even">
<td>LPN</td>
<td>Licensed Practical Nurse</td>
</tr>
<tr class="odd">
<td>M/S</td>
<td>Musculoskeletal Assessment</td>
</tr>
<tr class="even">
<td>MAS</td>
<td>Medical Administration Service</td>
</tr>
<tr class="odd">
<td>MH</td>
<td>Mental Health Assessment</td>
</tr>
<tr class="even">
<td>MRSA</td>
<td>Methicillin-Resistant Staphylococcus Aureus</td>
</tr>
<tr class="odd">
<td>NAA</td>
<td>Nursing Admission Assessment</td>
</tr>
<tr class="even">
<td>Neuro</td>
<td>Neurological Assessment</td>
</tr>
<tr class="odd">
<td>NHIA</td>
<td>Nursing Healthcare Informatics Alliance</td>
</tr>
<tr class="even">
<td>NPAT</td>
<td>National Patient Assessment Templates</td>
</tr>
<tr class="odd">
<td>NUPA</td>
<td>Namespace assigned to the Patient Assessment Documentation Package (PADP) by Database Administrator</td>
</tr>
<tr class="even">
<td>OED</td>
<td>Office of Enterprise Development</td>
</tr>
<tr class="odd">
<td>OERR</td>
<td>Order Entry Results Reporting</td>
</tr>
<tr class="even">
<td>OIT</td>
<td>Office of Information and Technology</td>
</tr>
<tr class="odd">
<td>ONS</td>
<td>Office of Nursing Services</td>
</tr>
<tr class="even">
<td>Orient</td>
<td>Orientation to Unit</td>
</tr>
<tr class="odd">
<td>P/S</td>
<td>Psychosocial Assessment</td>
</tr>
<tr class="even">
<td>PADP</td>
<td>Patient Assessment Documentation Package</td>
</tr>
<tr class="odd">
<td>Pain</td>
<td>Pain Assessment</td>
</tr>
<tr class="even">
<td>PC</td>
<td>Plan of Care</td>
</tr>
<tr class="odd">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="even">
<td>PD</td>
<td>Product Development</td>
</tr>
<tr class="odd">
<td>PHR</td>
<td>Patient Health Record</td>
</tr>
<tr class="even">
<td>Prob</td>
<td>Problems/Interventions/Desired Outcomes tab in the RN Reassessment</td>
</tr>
<tr class="odd">
<td>Resp</td>
<td>Respiratory Assessment</td>
</tr>
<tr class="even">
<td>Rest (or Restr)</td>
<td>Restraints</td>
</tr>
<tr class="odd">
<td>RN</td>
<td>Registered Nurse</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Call</td>
</tr>
<tr class="odd">
<td>RSD</td>
<td>Requirements Specification Document</td>
</tr>
<tr class="even">
<td>Section 508</td>
<td>Under Section 508 of the Rehabilitation Act, as amended (29 U.S.C. 794d) Public Law 106-246 (http://va.gov/accessible) agencies must provide employees and members of the public who have disabilities access to electronic and information technology that is comparable to the access available to employees and members of the public who are not individuals with disabilities</td>
</tr>
<tr class="odd">
<td>Skin</td>
<td>Skin Assessment</td>
</tr>
<tr class="even">
<td>SNOMED – CT</td>
<td>Systemized Nomenclature of Medicine Clinical Terms</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td>Text Integration Utilities Program<br />
All text in CPRS is stored in TIU</td>
</tr>
<tr class="even">
<td>TJC</td>
<td>The Joint Commission</td>
</tr>
<tr class="odd">
<td>V/S</td>
<td>Vital Signs</td>
</tr>
<tr class="even">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td>VANOD</td>
<td>VA Nursing Outcomes Database</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td><p>Veterans Health Information Systems and Technology Architecture</p>
<p>An enterprise-wide information system built around an electronic health record used throughout the Department of Veterans Affairs medical system.</p></td>
</tr>
<tr class="odd">
<td>Vital Qualifiers</td>
<td><p>Provide detail in to the unit of measurement used with the vital signs.</p>
<p>Height in inches or centimeters?</p>
<p>Weight in pounds or kilograms?</p></td>
</tr>
</tbody>
</table>

# Appendix A List of Health Factors Only for Admission Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ONS = Office of Nursing ServiceAA = Admission Assessment

| Tab Content      |     | Health Factor                               |     | Category                             |     |
|------------------|-----|---------------------------------------------|-----|--------------------------------------|-----|
| General Info     |     | ONS AA GENERAL INFO NO RESPONSE             |     | ONS AA GENERAL INFO                  |     |
|                  |     | ONS AA MRSA INFO YES                        |     | ONS AA MRSA                          |     |
|                  |     | ONS AA MRSA INFO NO                         |     | ONS AA MRSA                          |     |
|                  |     | ONS AA MRSA SWAB AGREEMENT YES              |     | ONS AA MRSA                          |     |
|                  |     | ONS AA MRSA SWAB AGREEMENT NO               |     | ONS AA MRSA                          |     |
|                  |     | ONS AA MRSA SWAB YES                        |     | ONS AA MRSA                          |     |
|                  |     | ONS AA MRSA SWAB NO                         |     | ONS AA MRSA                          |     |
|                  |     | ONS AA INFECTION CONTROL ED YES             |     | ONS AA INFECT CONTROL                |     |
|                  |     | ONS AA INFECTION CONTROL ED NO              |     | ONS AA INFECT CONTROL                |     |
|                  |     | ONS AA IC UNDERSTANDING POOR                |     | ONS AA INFECT CONTROL                |     |
|                  |     | ONS AA IC UNDERSTANDING FAIR                |     | ONS AA INFECT CONTROL                |     |
|                  |     | ONS AA IC UNDERSTANDING GOOD                |     | ONS AA INFECT CONTROL                |     |
|                  |     | ONS AA PREFERRED LANGUAGE                   |     | ONS AA LANGUAGE                      |     |
| Restraints       |     | ONS AA RESTRAINT SUPPORTIVE                 |     | ONS AA RESTRAINTS                    |     |
|                  |     | ONS AA RESTRAINT RESTRICTIVE                |     | ONS AA RESTRAINTS                    |     |
|                  |     | ONS AA RESTRAINT DATE/TIME INITIATED        |     | ONS AA RESTRAINTS                    |     |
|                  |     | ONS AA RESTRAINT DATE/TIME DISCONTINUED     |     | ONS AA RESTRAINTS                    |     |
| Unit Orient      |     | ONS AA UNIT ORIENT NO                       |     | ONS AA UNIT ORIENT                   |     |
|                  |     | ONS AA UNIT ORIENT FOR PATIENT              |     | ONS AA UNIT ORIENT                   |     |
|                  |     | ONS AA UNIT ORIENT FOR SUPPORT PERSON       |     | ONS AA UNIT ORIENT                   |     |
| Education        |     | ONS AA ED ASSESS NO RESPONSE                |     | ONS AA EDUCATION                     |     |
| Pain             |     | ONS AA PAIN PROBLEM YES                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN PROBLEM NO                      |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN PROBLEM NO RESPONSE             |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN BEHAVIORS NONE                  |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN BEHAVIORS YES                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN GOAL ID LOC 1                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN GOAL ID LOC 2                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN GOAL ID LOC 3                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN GOAL ID LOC 4                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN GOAL ID LOC 5                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN SEVERITY ID LOC 1               |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN SEVERITY ID LOC 2               |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN SEVERITY ID LOC 3               |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN SEVERITY ID LOC 4               |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN SEVERITY ID LOC 5               |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN ACUTE LOC 1                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN ACUTE LOC 2                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN ACUTE LOC 3                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN ACUTE LOC 4                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN ACUTE LOC 5                     |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN CHRONIC LOC 1                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN CHRONIC LOC 2                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN CHRONIC LOC 3                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN CHRONIC LOC 4                   |     | ONS AA PAIN                          |     |
|                  |     | ONS AA PAIN CHRONIC LOC 5                   |     | ONS AA PAIN                          |     |
| Vascular Access  |     | ONS AA PERIPH IV \#1 DATE INSERTED          |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#2 DATE INSERTED          |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#3 DATE INSERTED          |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#4 DATE INSERTED          |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#5 DATE INSERTED          |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#1 DATE DISCONTINUED      |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#2 DATE DISCONTINUED      |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#3 DATE DISCONTINUED      |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#4 DATE DISCONTINUED      |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA PERIPH IV \#5 DATE DISCONTINUED      |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#1 DATE INSERTED       |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#2 DATE INSERTED       |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#3 DATE INSERTED       |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#4 DATE INSERTED       |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#5 DATE INSERTED       |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#1 DATE DISCONTINUED   |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#2 DATE DISCONTINUED   |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#3 DATE DISCONTINUED   |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#4 DATE DISCONTINUED   |     | ONS AA VASCULAR ACCESS               |     |
|                  |     | ONS AA CENTRAL LINE \#5 DATE DISCONTINUED   |     | ONS AA VASCULAR ACCESS               |     |
| Respiratory      |     | ONS AA RESP ASSESS NO RESPONSE              |     | ONS AA RESPIRATORY                   |     |
|                  |     | ONS TOBACCO USE FORMER LESS THAN 1Y         |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE FORMER 1Y-7Y                |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE FORMER GREATER THAN 7Y      |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE CURRENT                     |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO LIFETIME NON-USER               |     | ONS TOBACCO USE SCREEN               |     |
| Cardiovascular   |     | ONS AA CV ASSESS NO RESPONSE                |     | ONS AA CARDIOVASCULAR                |     |
| Neurological     |     | ONS AA NEURO ASSESS NO RESPONSE             |     | ONS AA NEUROLOGICAL                  |     |
|                  |     | ONS AA AUTONOMIC DYSREFLEXIA HX YES         |     | ONS AA NEUROLOGICAL                  |     |
|                  |     | ONS AA AUTONOMIC DYSREFLEXIA HX NO          |     | ONS AA NEUROLOGICAL                  |     |
| Gastrointestinal |     | ONS AA GI ASSESS NO RESPONSE                |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA BOWEL PROGRAM YES                    |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA SCREEN YES                 |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA SCREEN NO                  |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA NEW DX STROKE/HN CA/TBI    |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA MOD TEXT/EAT MANEUVERS     |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA CANT FOLLOW COMMANDS       |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA WET GURGLY VOICE           |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA DROOLING WHILE AWAKE       |     | ONS AA GASTROINTESTINAL              |     |
|                  |     | ONS AA DYSPHAGIA TONGUE DEVIATES FROM ML    |     | ONS AA GASTROINTESTINAL              |     |
| Genitourinary    |     | ONS AA GU ASSESS NO RESPONSE                |     | ONS AA GENITOURINARY                 |     |
|                  |     | ONS AA URINARY CATHETER DATE INSERTED       |     | ONS AA GENITOURINARY                 |     |
|                  |     | ONS AA URINARY CATHETER DATE REMOVED        |     | ONS AA GENITOURINARY                 |     |
| Musculoskeletal  |     | ONS AA MS ASSESS NO RESPONSE                |     | ONS AA MUSCULOSKELETAL               |     |
|                  |     | ONS AA MORSE FALL SCALE LOW RISK            |     | ONS AA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS AA MORSE FALL SCALE MODERATE RISK       |     | ONS AA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS AA MORSE FALL SCALE HIGH RISK           |     | ONS AA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS AA FALL HX WITH INJURY                  |     | ONS AA HX OF FALLING                 |     |
|                  |     | ONS AA FALL HX WITHOUT INJURY               |     | ONS AA HX OF FALLING                 |     |
|                  |     | ONS AA FALL HX UNKNOWN INJURY               |     | ONS AA HX OF FALLING                 |     |
|                  |     | ONS AA FALL HX WITH FRACTURE                |     | ONS AA HX OF FALLING                 |     |
|                  |     | ONS AA FALL HX WITHOUT FRACTURE             |     | ONS AA HX OF FALLING                 |     |
|                  |     | ONS AA MEDICATIONS - DIURETICS              |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - SEDATIVES              |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - OPIOIDS                |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - ANALGESICS             |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - HYPNOTICS              |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - ANTIHYPERTENSIVES      |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - ANTICOAGULANTS         |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - PSYCHOTROPICS          |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - ANTIDEPRESSANTS        |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - MULTIPLE               |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA MEDICATIONS - OTHER                  |     | ONS AA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS AA FALL UNIVERSAL PRECAUTION YES        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - EVAL ORTHOSTATSIS     |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE ED ON MEDS    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT-SUPPORT MD INSTRUCT     |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REVIEW MED/RISKS      |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PT ROUNDS Q 15 MIN    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PT ROUNDS Q 30 MIN    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PT ROUNDS Q 1 HOUR    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PT ROUNDS Q 2 HOURS   |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - OTHER                 |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REHAB RECOMMENDATION  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - HIP PROTECTORS        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - NURSE RESTORE EVAL    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REFER TO REHAB        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REINFORCE TRANS HELP  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - AMB AID ASSESSMENT    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - SAFE AMB DEVICE       |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - EVAL USE PT AMB AID   |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REHAB SELECT AMB AID  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - ED ON TRIPPING        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - BEDSIDE TOILETING     |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE EXIT ALARM    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE FLOOR MAT     |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE HELMET        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - HT ADJUST BED         |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - HIP PROTECTORS        |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - SAFE EXIT FROM BED    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE TRANS EQUIP   |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - REHAB TO ASSESS GAIT  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT-SUPPORT PT TOILETING    |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - DIVERSIONAL ACTIVITY  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - CLOSER TO RN STATION  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - OBSERVE Q 1 HOUR      |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - PROVIDE CLOCK/ CALEND |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - RE EDUCATE PT SAFETY  |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - WANDERING MONITOR     |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS AA FALL PREVENT - OTHER                 |     | ONS AA FALL PREVENTION INTERVENTIONS |     |
| Skin             |     | ONS AA SKIN ASSESS NO RESPONSE              |     | ONS AA SKIN                          |     |
|                  |     | ONS AA BRADEN SCALE 19 OR HIGHER            |     | ONS AA BRADEN SCALE                  |     |
|                  |     | ONS AA BRADEN SCALE 15–18                   |     | ONS AA BRADEN SCALE                  |     |
|                  |     | ONS AA BRADEN SCALE 13-14                   |     | ONS AA BRADEN SCALE                  |     |
|                  |     | ONS AA BRADEN SCALE 10-12                   |     | ONS AA BRADEN SCALE                  |     |
|                  |     | ONS AA BRADEN SCALE 9 OR LOWER              |     | ONS AA BRADEN SCALE                  |     |
|                  |     | ONS AA SKIN PATCHES YES                     |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PATCHES NO                      |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN COLOR                           |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN TEMPERATURE                     |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN MOISTURE                        |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN TURGOR                          |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - ABRASION              |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM -LACERATION             |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - BITE                  |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - BRUISING              |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - BURN                  |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - RASH                  |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - CRUSH INJURY          |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - PENETRATING           |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - PUNCTURE WOUND        |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - VASCULAR LESION       |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - SURGICAL INCISION     |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN PROBLEM - OTHER                 |     | ONS AA SKIN ASSESSMENT               |     |
|                  |     | ONS AA SKIN RISK - AMPUTEE                  |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - MULTIPLE SCLEROSIS       |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - QUADRAPLEGIA             |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - PARAPLEGIA               |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - DIABETES                 |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - NEUROLOGICAL DISEASE     |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - SPINAL CORD INJURY       |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN RISK - PARALYSIS                |     | ONS AA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS AA SKIN PU \#1 STAGE I                  |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#1 STAGE II                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#1 STAGE III                |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#1 STAGE IV                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#1 UNABLE TO STAGE          |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#1 SUSPECTED DEEP TISSUE    |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 STAGE I                  |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 STAGE II                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 STAGE III                |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 STAGE IV                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 UNABLE TO STAGE          |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#2 SUSPECTED DEEP TISSUE    |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 STAGE I                  |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 STAGE II                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 STAGE III                |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 STAGE IV                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 UNABLE TO STAGE          |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#3 SUSPECTED DEEP TISSUE    |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 STAGE I                  |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 STAGE II                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 STAGE III                |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 STAGE IV                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 UNABLE TO STAGE          |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#4 SUSPECTED DEEP TISSUE    |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 STAGE I                  |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 STAGE II                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 STAGE III                |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 STAGE IV                 |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 UNABLE TO STAGE          |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA SKIN PU \#5 SUSPECTED DEEP TISSUE    |     | ONS AA PRESSURE ULCER                |     |
|                  |     | ONS AA PU ED - IMP OF CHANGING POSITIONS    |     | ONS AA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS AA PU ED - MATERIAL ON ULCER PREVENT    |     | ONS AA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS AA PU ED - CAUSE/PREVENTION             |     | ONS AA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS AA PU ED - TX PLAN                      |     | ONS AA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS AA PU ED - OTHER                        |     | ONS AA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS AA SKIN INTERVENT - HOB 30 NOT EATING   |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - TRAPEZE PULL SHEET  |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT -ELEVATE HOB MEALS    |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - HOB ELE/RAISE KNEE  |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - OTHER               |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - CLEAN DRY SKIN      |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - CONDOM CATHETER     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - PROTECT OINTMENT    |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - FECAL COLLECTOR     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - OFFER BEDPAN/UR     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - TOILET SCHEDULE     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - TELL PT SEEK HELP   |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ACT AS TOLERATED    |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - SIT OOB TO 2 H      |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ROM                 |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ENCOURAGE MEALS     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - MONITOR INTAKE      |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - OFFER SUPPLEMENTS   |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ORAL CARE           |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - LIQ Q 2 H WHEN TURN |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - TRAY SET UP         |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - OTHER               |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ELEVATE HEELS       |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - ELBOW PADS          |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - SPECIALTY BED       |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - TURN REPOS Q 2 HR   |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - POSITION CHANGE     |     | ONS AA SKIN INTERVENTIONS            |     |
|                  |     | ONS AA SKIN INTERVENT - WHEELCHAIR CUSHION  |     | ONS AA SKIN INTERVENTIONS            |     |
| Psychosocial     |     | ONS AA P/S ASSESS NO RESPONSE               |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE VERBAL REPORTED                |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE PHYSICAL REPORTED              |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE FINANCIAL REPORTED             |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE SEXUAL REPORTED                |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE NEGLECT REPORTED               |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE VERBAL SUSPECTED               |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE PHYSICAL SUSPECTED             |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE NEGLECT SUSPECTED              |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ABUSE SUSPECTED BY PATIENT YES       |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDAL THOUGHTS YES                |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDAL THOUGHTS NO                 |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDAL THOUGHTS DECLINES TO ANSWER |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDE PRIOR ATTEMPT YES            |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDE PRIOR ATTEMPT NO             |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA SUICIDE PRIOR ATTEMPT DECL ANSW      |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA FEELING HOPELESS YES                 |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA FEELING HOPELESS NO                  |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA FEELING HOPELESS DECLINES ANSWER     |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ELOPEMENT SCREEN YES                 |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA ELOPEMENT SCREEN NO                  |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA WANDERING RISK - LEGAL GUARDIAN      |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA WANDERING RISK - LEGALLY COMMITTED   |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA WANDERING RISK - DANGER SELF/OTHERS  |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA WANDERING RISK - GRAVELY DISABLED    |     | ONS AA PSYCHOSOCIAL                  |     |
|                  |     | ONS AA WANDERING RISK - COGNITIVE ABILITY   |     | ONS AA PSYCHOSOCIAL                  |     |
| Mental Health    |     | ONS AA MH ASSESS - NO RESPONSE              |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - SPACE INVADED        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - EXCESSIVE NOISE      |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - ARGUMENTS            |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - SIGNIFICANT LOSES    |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - BEING HOMELESS       |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - NOT LISTENED TO      |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - HURT FEELINGS        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - PHYSICAL ABUSE       |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - SEXUAL ABUSE         |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - PAIN                 |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - LOSS CTRL ETOH/DRUGS |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - CANT GET WANTS MET   |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - NO POWER             |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - CANT PROBLEM SOLVE   |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - MONETARY ISSUES      |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - UNJUSTLY BLAMED      |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - TREATED UNFAIRLY     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - HEARING VOICES       |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - NOTHING UPSETTING    |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER ID - OTHER                |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER DECLINES TO ANSWER        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH TRIGGER UNABLE TO ANSWER          |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH UPSET DECLINES TO ANSWER          |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH UPSET ABLE TO CALM                |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH UPSET UNABLE TO CALM              |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - MUSIC                |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - TALKING W/OTHERS     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - EXERCISE/WALK        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - BODY POSITION        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - SEEK QUIET PLACE     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - DISTRACTION          |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - RELAX TECHNIQUES     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - SMOKING              |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - PACING               |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID- PRAYING               |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - MEDITATION           |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - MEDICATIONS          |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - SUBSTANCE USE        |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - SEXUAL ACTIVITIES    |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - SLEEP                |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - WATCH TV             |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - EAT                  |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - USE HUMOR            |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - READ                 |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - WRITE IN JOURNAL     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH CALMING ID - OTHER                |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH RESTRAINT NTF UNABLE TO ANSWER    |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH RESTRAINT NTF DECLINES ANSWER     |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH RESTRAINT NTF YES                 |     | ONS AA MENTAL HEALTH                 |     |
|                  |     | ONS AA MH RESTRAINT NTF NO                  |     | ONS AA MENTAL HEALTH                 |     |

# Appendix B List of Health Factors Only for Reassessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ONS = Office of Nursing ServiceRA = Reassessment

| Tab Content      |     | Health Factor                               |     | Category                             |     |
|------------------|-----|---------------------------------------------|-----|--------------------------------------|-----|
| General Info     |     | ONS RA GENERAL INFO NO RESPONSE             |     | ONS RA GENERAL INFO                  |     |
|                  |     | ONS RA MRSA INFO YES                        |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA INFO NO                         |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA SWAB AGREEMENT YES              |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA SWAB AGREEMENT NO               |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA TRANSFER SWAB YES               |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA TRANSFER SWAB NO                |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA TRANSFER SWAB REFUSED           |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA DISCHARGE SWAB YES              |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA DISCHARGE SWAB NO               |     | ONS RA MRSA                          |     |
|                  |     | ONS RA MRSA DISCHARGE SWAB REFUSED          |     | ONS RA MRSA                          |     |
|                  |     | ONS RA INFECTION CONTROL ED YES             |     | ONS RA INFECT CONTROL                |     |
|                  |     | ONS RA INFECTION CONTROL ED NO              |     | ONS RA INFECT CONTROL                |     |
|                  |     | ONS RA IC UNDERSTANDING POOR                |     | ONS RA INFECT CONTROL                |     |
|                  |     | ONS RA IC UNDERSTANDING FAIR                |     | ONS RA INFECT CONTROL                |     |
|                  |     | ONS RA IC UNDERSTANDING GOOD                |     | ONS RA INFECT CONTROL                |     |
|                  |     | ONS RA PREFERRED LANGUAGE                   |     | ONS RA LANGUAGE                      |     |
| Restraints       |     | ONS RA RESTRAINT SUPPORTIVE                 |     | ONS RA RESTRAINTS                    |     |
|                  |     | ONS RA RESTRAINT RESTRICTIVE                |     | ONS RA RESTRAINTS                    |     |
|                  |     | ONS RA RESTRAINT DATE/TIME INITIATED        |     | ONS RA RESTRAINTS                    |     |
|                  |     | ONS RA RESTRAINT DATE/TIME DISCONTINUED     |     | ONS RA RESTRAINTS                    |     |
| Unit Orient      |     | ONS RA UNIT ORIENT NO                       |     | ONS RA UNIT ORIENT                   |     |
|                  |     | ONS RA UNIT ORIENT FOR PATIENT              |     | ONS RA UNIT ORIENT                   |     |
|                  |     | ONS RA UNIT ORIENT FOR SUPPORT PERSON       |     | ONS RA UNIT ORIENT                   |     |
| Education        |     | ONS RA ED ASSESS NO RESPONSE                |     | ONS RA EDUCATION                     |     |
| Pain             |     | ONS RA PAIN YES                             |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN NO                              |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN NO RESPONSE                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN BEHAVIORS NONE                  |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN BEHAVIORS YES                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN BEHAVIORS WITH ACTIVITY         |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN BEHAVIORS DURING PROCEDURE      |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN BEHAVIORS AT REST               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN GOAL ID LOC 1                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN GOAL ID LOC 2                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN GOAL ID LOC 3                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN GOAL ID LOC 4                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN GOAL ID LOC 5                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN SEVERITY ID LOC 1               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN SEVERITY ID LOC 2               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN SEVERITY ID LOC 3               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN SEVERITY ID LOC 4               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN SEVERITY ID LOC 5               |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN ACUTE LOC 1                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN ACUTE LOC 2                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN ACUTE LOC 3                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN ACUTE LOC 4                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN ACUTE LOC 5                     |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN CHRONIC LOC 1                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN CHRONIC LOC 2                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN CHRONIC LOC 3                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN CHRONIC LOC 4                   |     | ONS RA PAIN                          |     |
|                  |     | ONS RA PAIN CHRONIC LOC 5                   |     | ONS RA PAIN                          |     |
| Vascular Access  |     | ONS RA PERIPH IV \#1 DATE INSERTED          |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#2 DATE INSERTED          |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#3 DATE INSERTED          |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#4 DATE INSERTED          |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#5 DATE INSERTED          |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#1 DATE DISCONTINUED      |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#2 DATE DISCONTINUED      |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#3 DATE DISCONTINUED      |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#4 DATE DISCONTINUED      |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA PERIPH IV \#5 DATE DISCONTINUED      |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#1 DATE INSERTED       |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#2 DATE INSERTED       |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#3 DATE INSERTED       |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#4 DATE INSERTED       |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#5 DATE INSERTED       |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#1 DATE DISCONTINUED   |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#2 DATE DISCONTINUED   |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#3 DATE DISCONTINUED   |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#4 DATE DISCONTINUED   |     | ONS RA VASCULAR ACCESS               |     |
|                  |     | ONS RA CENTRAL LINE \#5 DATE DISCONTINUED   |     | ONS RA VASCULAR ACCESS               |     |
| Respiratory      |     | ONS RA RESP ASSESS NO RESPONSE              |     | ONS RA RESPIRATORY                   |     |
|                  |     | ONS TOBACCO USE FORMER LESS THAN 1Y         |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE FORMER 1Y-7Y                |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE FORMER GREATER THAN 7Y      |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO USE CURRENT                     |     | ONS TOBACCO USE SCREEN               |     |
|                  |     | ONS TOBACCO LIFETIME NON-USER               |     | ONS TOBACCO USE SCREEN               |     |
| Cardiovascular   |     | ONS RA CV ASSESS NO RESPONSE                |     | ONS RA CARDIOVASCULAR                |     |
| Neurological     |     | ONS RA NEURO ASSESS NO RESPONSE             |     | ONS RA NEUROLOGICAL                  |     |
|                  |     | ONS RA AUTONOMIC DYSREFLEXIA HX YES         |     | ONS RA NEUROLOGICAL                  |     |
|                  |     | ONS RA AUTONOMIC DYSREFLEXIA HX NO          |     | ONS RA NEUROLOGICAL                  |     |
| Gastrointestinal |     | ONS RA GI ASSESS NO RESPONSE                |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA BOWEL PROGRAM YES                    |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA SCREEN YES                 |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA SCREEN NO                  |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA NEW DX STROKE/HN CA/TBI    |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA MOD TEXT/EAT MANEUVERS     |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA CANT FOLLOW COMMANDS       |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA WET GURGLY VOICE           |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA DROOLING WHILE AWAKE       |     | ONS RA GASTROINTESTINAL              |     |
|                  |     | ONS RA DYSPHAGIA TONGUE DEVIATES FROM ML    |     | ONS RA GASTROINTESTINAL              |     |
| Genitourinary    |     | ONS RA GU ASSESS NO RESPONSE                |     | ONS RA GENITOURINARY                 |     |
|                  |     | ONS RA URINARY CATHETER DATE INSERTED       |     | ONS RA GENITOURINARY                 |     |
|                  |     | ONS RA URINARY CATHETER DATE REMOVED        |     | ONS RA GENITOURINARY                 |     |
| Musculoskeletal  |     | ONS RA MS ASSESS NO RESPONSE                |     | ONS RA MUSCULOSKELETAL               |     |
|                  |     | ONS RA MORSE FALL SCALE LOW RISK            |     | ONS RA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS RA MORSE FALL SCALE MODERATE RISK       |     | ONS RA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS RA MORSE FALL SCALE HIGH RISK           |     | ONS RA MORSE FALL SCALE SCORE        |     |
|                  |     | ONS RA FALL HX WITH INJURY                  |     | ONS RA HX OF FALLING                 |     |
|                  |     | ONS RA FALL HX WITHOUT INJURY               |     | ONS RA HX OF FALLING                 |     |
|                  |     | ONS RA FALL HX UNKNOWN INJURY               |     | ONS RA HX OF FALLING                 |     |
|                  |     | ONS RA FALL HX WITH FRACTURE                |     | ONS RA HX OF FALLING                 |     |
|                  |     | ONS RA FALL HX WITHOUT FRACTURE             |     | ONS RA HX OF FALLING                 |     |
|                  |     | ONS RA MEDICATIONS - DIURETICS              |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - SEDATIVES              |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - OPIOIDS                |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - ANALGESICS             |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - HYPNOTICS              |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - ANTIHYPERTENSIVES      |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - ANTICOAGULANTS         |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - PSYCHOTROPICS          |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - ANTIDEPRESSANTS        |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - MULTIPLE               |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA MEDICATIONS - OTHER                  |     | ONS RA SECONDARY DIAGNOSIS           |     |
|                  |     | ONS RA FALL UNIVERSAL PRECAUTION YES        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - EVAL ORTHOSTATSIS     |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE ED ON MEDS    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - SUPPORT MD INSTRUCT   |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - REVIEW MED/RISKS      |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PT ROUNDS Q 15 MIN    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PT ROUNDS Q 30 MIN    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PT ROUNDS Q 1 HOUR    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PT ROUNDS Q 2 HOURS   |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - OTHER                 |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - REHAB RECOMMENDATION  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - HIP PROTECTORS        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - NURSE RESTORE EVAL    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - REFER TO REHAB        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - REINFORCE TRANS HELP  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - AMB AID ASSESSMENT    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - SAFE AMB DEVICE       |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT-EVAL USE PT AMB AID     |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT-REHAB SELECT AMB AID    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - ED ON TRIPPING        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - BEDSIDE TOILETING     |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE EXIT ALARM    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE FLOOR MAT     |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE HELMET        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - HT ADJUST BED         |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - HIP PROTECTORS        |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - SAFE EXIT FROM BED    |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE TRANS EQUIP   |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - REHAB TO ASSESS GAIT  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - SUPPORT PT TOILETING  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - DIVERSIONAL ACTIVITY  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - CLOSER TO RN STATION  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - OBSERVE Q 1 HOUR      |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - PROVIDE CLOCK/ CALEND |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - RE EDUCATE PT SAFETY  |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - WANDERING MONITOR     |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
|                  |     | ONS RA FALL PREVENT - OTHER                 |     | ONS RA FALL PREVENTION INTERVENTIONS |     |
| Skin             |     | ONS RA SKIN ASSESS NO RESPONSE              |     | ONS RA SKIN                          |     |
|                  |     | ONS RA BRADEN SCALE 19 OR HIGHER            |     | ONS RA BRADEN SCALE                  |     |
|                  |     | ONS RA BRADEN SCALE 15-18                   |     | ONS RA BRADEN SCALE                  |     |
|                  |     | ONS RA BRADEN SCALE 13-14                   |     | ONS RA BRADEN SCALE                  |     |
|                  |     | ONS RA BRADEN SCALE 10-12                   |     | ONS RA BRADEN SCALE                  |     |
|                  |     | ONS RA BRADEN SCALE 9 OR LOWER              |     | ONS RA BRADEN SCALE                  |     |
|                  |     | ONS RA SKIN PATCHES YES                     |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PATCHES NO                      |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN COLOR                           |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN TEMPERATURE                     |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN MOISTURE                        |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN TURGOR                          |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - ABRASION              |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - LACERATION            |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - BITE                  |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - BRUISING              |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - BURN                  |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - RASH                  |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - CRUSH INJURY          |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - PENETRATING           |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - PUNCTURE WOUND        |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - VASCULAR LESION       |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - SURGICAL INCISION     |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN PROBLEM - OTHER                 |     | ONS RA SKIN ASSESSMENT               |     |
|                  |     | ONS RA SKIN RISK - AMPUTEE                  |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - MULTIPLE SCLEROSIS       |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - QUADRAPLEGIA             |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - PARAPLEGIA               |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - DIABETES                 |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - NEUROLOGICAL DISEASE     |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - SPINAL CORD INJURY       |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN RISK - PARALYSIS                |     | ONS RA SKIN HIGH RISK FACTORS        |     |
|                  |     | ONS RA SKIN PU \#1 STAGE I                  |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#1 STAGE II                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#1 STAGE III                |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#1 STAGE IV                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#1 UNABLE TO STAGE          |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#1 SUSPECTED DEEP TISSUE    |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 STAGE I                  |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 STAGE II                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 STAGE III                |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 STAGE IV                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 UNABLE TO STAGE          |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#2 SUSPECTED DEEP TISSUE    |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 STAGE I                  |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 STAGE II                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 STAGE III                |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 STAGE IV                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 UNABLE TO STAGE          |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#3 SUSPECTED DEEP TISSUE    |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 STAGE I                  |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 STAGE II                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 STAGE III                |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 STAGE IV                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 UNABLE TO STAGE          |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#4 SUSPECTED DEEP TISSUE    |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 STAGE I                  |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 STAGE II                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 STAGE III                |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 STAGE IV                 |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 UNABLE TO STAGE          |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA SKIN PU \#5 SUSPECTED DEEP TISSUE    |     | ONS RA PRESSURE ULCER                |     |
|                  |     | ONS RA PU ED - IMP OF CHANGING POSITIONS    |     | ONS RA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS RA PU ED - MATERIAL ON ULCER PREVENT    |     | ONS RA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS RA PU ED - CAUSE/PREVENTION             |     | ONS RA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS RA PU ED - TX PLAN                      |     | ONS RA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS RA PU ED - OTHER                        |     | ONS RA PRESSURE ULCER-EDUCATION      |     |
|                  |     | ONS RA SKIN INTERVENT - HOB 30 OT EATING    |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - TRAPEZE PULL SHEET  |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ELEVATE HOB MEALS   |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - HOB ELE/RAISE KNEE  |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - OTHER               |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - CLEAN DRY SKIN      |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - CONDOM CATHETER     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - FECAL COLLECTOR     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - PROTECT OINTMENT    |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - OFFER BEDPAN/UR     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - TOILET SCHEDULE     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - TELL PT SEEK HELP   |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ACT AS TOLERATED    |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - SIT OOB TO 2 H      |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ROM                 |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ENCOURAGE MEALS     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - MONITOR INTAKE      |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - OFFER SUPPLEMENTS   |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ORAL CARE           |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - LIQ Q 2 H WHEN TURN |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - TRAY SET UP         |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - OTHER               |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ELEVATE HEELS       |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - ELBOW PADS          |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - SPECIALTY BED       |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - TURN REPOS Q 2 HR   |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - POSITION CHANGE     |     | ONS RA SKIN INTERVENTIONS            |     |
|                  |     | ONS RA SKIN INTERVENT - WHEELCHAIR CUSHION  |     | ONS RA SKIN INTERVENTIONS            |     |
| Psychosocial     |     | ONS RA P/S ASSESS NO RESPONSE               |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE VERBAL REPORTED                |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE PHYSICAL REPORTED              |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE FINANCIAL REPORTED             |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE SEXUAL REPORTED                |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE NEGLECT REPORTED               |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE VERBAL SUSPECTED               |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE PHYSICAL SUSPECTED             |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE NEGLECT SUSPECTED              |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ABUSE SUSPECTED BY PATIENT YES       |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDAL THOUGHTS YES                |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDAL THOUGHTS NO                 |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDAL THOUGHTS DECLINES TO ANSWER |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDE PRIOR ATTEMPT YES            |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDE PRIOR ATTEMPT NO             |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA SUICIDE PRIOR ATTEMPT DECL ANSW      |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA FEELING HOPELESS YES                 |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA FEELING HOPELESS NO                  |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA FEELING HOPELESS DECLINES ANSWER     |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ELOPEMENT SCREEN YES                 |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA ELOPEMENT SCREEN NO                  |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA WANDERING RISK - LEGAL GUARDIAN      |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA WANDERING RISK - LEGALLY COMMITTED   |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA WANDERING RISK - DANGER SELF/OTHERS  |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA WANDERING RISK - GRAVELY DISABLED    |     | ONS RA PSYCHOSOCIAL                  |     |
|                  |     | ONS RA WANDERING RISK - COGNITIVE ABILITY   |     | ONS RA PSYCHOSOCIAL                  |     |
| Mental Health    |     | ONA RA MH ASSESS NO RESPONSE                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - SPACE INVADED        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - EXCESSIVE NOISE      |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - ARGUMENTS            |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - SIGNIFICANT LOSES    |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - BEING HOMELESS       |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - NOT LISTENED TO      |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - HURT FEELINGS        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - PHYSICAL ABUSE       |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - SEXUAL ABUSE         |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - PAIN                 |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - LOSS CTRL ETOH/DRUGS |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - CANT GET WANTS MET   |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - NO POWER             |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - CANT PROBLEM SOLVE   |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - MONETARY ISSUES      |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - UNJUSTLY BLAMED      |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - TREATED UNFAIRLY     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - HEARING VOICES       |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - NOTHING UPSETTING    |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER ID - OTHER                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER DECLINES TO ANSWER        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH TRIGGER UNABLE TO ANSWER          |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH UPSET DECLINES TO ANSWER          |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH UPSET ABLE TO CALM                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH UPSET UNABLE TO CALM              |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - MUSIC                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - TALKING W/OTHERS     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - EXERCISE/WALK        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - BODY POSITION        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - SEEK QUIET PLACE     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - DISTRACTION          |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - RELAX TECHNIQUES     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - SMOKING              |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - PACING               |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID- PRAYING               |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - MEDITATION           |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - MEDICATIONS          |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - SUBSTANCE USE        |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - SEXUAL ACTIVITIES    |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - SLEEP                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - WATCH TV             |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - EAT                  |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - USE HUMOR            |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - READ                 |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - WRITE IN JOURNAL     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH CALMING ID - OTHER                |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH RESTRAINT NTF UNABLE TO ANSWER    |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH RESTRAINT NTF DECLINES ANSWER     |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH RESTRAINT NTF YES                 |     | ONS RA MENTAL HEALTH                 |     |
|                  |     | ONS RA MH RESTRAINT NTF NO                  |     | ONS RA MENTAL HEALTH                 |     |

# Appendix C Assessment Contingency Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-technical-manual/004.png)

During system downtimes, print a copy of the attached *Assessment Contingency Note* and use it to perform an *Admission RN Assessment*.

# Appendix D Reassessment Contingency Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-technical-manual/005.png)

During system downtimes, print a copy of the attached *Reassessment Contingency Note* and use it to perform an *RN Reassessment*.