---
title: Nursing Version 4 Technical Manual and Package Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: and Package Security Guide
app_code: NUR
app_name: Nursing
section: CLI
app_status: active
pkg_ns: NUR
patch_ver: 4
patch_id: NUR*4
group_key: "NUR:NUR:4"
file_numbers: []
security_keys: []
menu_options: 0
description: > This is not a first version. Nursing is a component of the Department of Veterans Affairs VISTA. It is comprised of multiple modules (i.e., Administration, Clinical, Education, Performance Improvement, and Research). Program content for present and future software releases has been provided and pr
audience: 
keywords: 
  - blockquote
  - class
  - nursing
  - width
  - style
  - table
  - nurs
  - colspan
  - even
  - status
page_count: 0
word_count: 14487
section_count: 16
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs4_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs4_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=80"
---

> ![](nursing-version-4-technical-manual-and-package-security-guide/001.png)

NURSING

TECHNICAL MANUAL AND PACKAGE SECURITY GUIDE

April 1997

(Revised January 2000)

> Department of Veterans Affairs Technical Service

Clinical Applications Product Line

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
- [Chapter 1 Implementation and Maintenance](#chapter-1-implementation-and-maintenance)
  - [Description:](#description)
  - [Virgin Installation of Software:](#virgin-installation-of-software)
  - [Additional Information:](#additional-information)
  - [Recommendation:](#recommendation)
  - [Recommendation:](#recommendation-1)
  - [Non-Virgin Installation of software:](#non-virgin-installation-of-software)
  - [Site Configurable Files/Fields](#site-configurable-filesfields)
  - [Site Configurable Output](#site-configurable-output)
  - [Resource Requirements](#resource-requirements)
  - [Technical Errors](#technical-errors)
- [Chapter 2 Routine Descriptions](#chapter-2-routine-descriptions)
- [Chapter 3 File List and Related Information](#chapter-3-file-list-and-related-information)
  - [Nursing File Descriptions](#nursing-file-descriptions)
  - [Nursing Package Default Definition](#nursing-package-default-definition)
- [Chapter 4 Exported Options](#chapter-4-exported-options)
  - [Menu Options by Name](#menu-options-by-name)
- [Chapter 5 Cross-references](#chapter-5-cross-references)
- [Chapter 6 Archiving and Purging](#chapter-6-archiving-and-purging)
- [Chapter 7 Callable Routines](#chapter-7-callable-routines)
- [Chapter 8 External Relations](#chapter-8-external-relations)
- [Chapter 9 Internal Relations](#chapter-9-internal-relations)
- [Chapter 10 Package-wide Variables](#chapter-10-package-wide-variables)
- [Chapter 11 On-Line Documentation](#chapter-11-on-line-documentation)
- [Chapter 12 SAC Exemptions](#chapter-12-sac-exemptions)
- [Chapter 13 Software Product Security](#chapter-13-software-product-security)
  - [Security Management.](#security-management)
  - [Security Features:](#security-features)
- [Glossary](#glossary)
> The Nursing system is a component of the Department of Veterans Affairs V*IST*A (Veterans Health Information Systems and Technology Architecture). Upon completion, it will comprise software which can be used to:
1)  plan and document nursing care provided to the veteran patient,
2)  support nursing administration in its continuing endeavor to manage the largest VA hospital service,
3)  provide nursing performance improvement data to management, clinicians, and educators,
4)  aggregate data for the purpose of expanding the domain of nursing research, and
5)  support the efforts of nurse educators in providing education and training to staff and other audiences within their facilities.
> The Nursing Focus Group and nursing application developers designed this manual for the purpose of explaining the functionality of the package to nursing personnel and hospital IRMS (Information Resource Management Service) staff. This document will provide the nursing ADP coordinator and IRMS personnel with the information to resolve any operational issues and explain the flexibility of the software package.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is not a first version. Nursing is a component of the Department of Veterans Affairs V*IST*A. It is comprised of multiple modules (i.e., Administration, Clinical, Education, Performance Improvement, and Research). Program content for present and future software releases has been provided and prioritized by the Nursing Focus Group with the assistance of the Alpha/Beta test sites and the many colleagues who use the software on a daily basis.

> Administration:

1.  Personnel management information (demographic and professional data of nursing staff),
2.  Resource management/analysis tracking for reports on budgeting DRGs, overtime usage, patient care hours, supply equipment projections, and staffing hours, and
3.  Mandatory reports (i.e., AMIS 1106, AMIS 1106a, AMIS 1106b, Annual Report).

> Clinical:

1)  Patient classification,
2)  Patient assessment,
3)  Nursing care plans which are system focused and contain both nursing problems and medical diagnoses,
4)  Patient care assignments,
5)  Clinical protocols/guidelines for care,
6)  Patient education material,
7)  Discharge planning, and
8)  Other patient related medical record data.

> Education:

1)  Education reports (i.e., mandatory in-service attendance, continuing education attendance, authorized absence/funding analysis),
2)  Nursing service calendar (scheduling function), and
3)  Student affiliation information (i.e., scheduling of student clinical labs, affiliation agreements).

> Performance Improvement:

1)  QA problem tracking system,
2)  Infection control trends,
3)  Patient incident analysis,
4)  Employee accident analysis,
5)  Continuous care monitors (clinical data), and
6)  Administrative monitors (e.g., safety equipment).

> Research:

1)  Resource listing of VA nurse researchers, and
2)  Additional functionalities as defined by the Nursing Focus Group.

> Prior to implementing the software, review appropriate sections of this manual for new applications and modifications to previous releases. Also, if the Nursing software is not on-line at your facility, the nursing ADP coordinator, and all nursing personnel responsible for supporting the package, should pay special attention to the chapter on Package Management in this manual.

> Functional Description of Version 4.0:

> The nursing software includes the following functionalities:

> Administration:

1)  Tracks staff information including: personal/demographic data, previous professional experience, work assignments, grade, licensure, certification, professional education, end of probationary period, and military reserve status.
2)  Uses a Position Control file to monitor past, current, and future nursing positions, future vacancies, reason for vacancy, start/stop dates for the position, and the level of employee filling the position. When a registered nurse's assignment is changed, the professional experience in the staff record is automatically updated.
3)  Generates management reports on employees including: academic and professional degrees, grade statistics, age trends, gender trends, license renewals, certification statistics, active reservist lists, LPN and RN NPSB tracking, and proficiency tracking.
4)  Provides resource management reports on ward/service FTEE statistics as well as ward and bed section workload/variance reports. The option which prints current workload reports can generate data on both the current and next tours of duty.
5)  Accumulates daily statistics on the number of patients treated in the following bed sections: hemodialysis, drug/alcohol patients, recovery room and domiciliary.
6)  Generates daily, monthly, quarterly, and yearly AMIS Reports: 1106b (FTEE Budgeted/Actual), 1106 (Patient Classification), and 1106a (Manhours).
7)  Provides workload statistics based on AMIS data.
8)  Provides a telephone list of employees by service or location.
9)  Provides miscellaneous patient acuity reports.

Introduction

> Education:

1)  Tracks employee continuing education data.
2)  Prints an AA/Funding Requests Report which indicates money authorized for C.E. attendance by specified year.
3)  Tracks mandatory Inservice information for multiple years. Information on program attendance can be provided by last attendance date or for three full fiscal years. Deficiency reports are available for the current or past three fiscal years.

> Clinical:

1)  Contains a patient classification system which generates reports by bed section and ward.
2)  Includes nationally developed standard nursing care plans for initiating patient care plan generation.
3)  Allows nurses to generate a patient care plan based on patient problems, identified goals, and specified nursing interventions. The software accommodates evaluation and resolution dates for problems, identifies target and met dates for goals, and discontinuation dates for interventions/orders.
4)  Produces two types of assignment worksheets for each patient (brief and complete). The brief worksheet does not display selected care plan information.
5)  Contains an option for printing a ward census by room and provides information on current patient location.
6)  Generates reports for unclassified patients and provides a function for classifying unclassified patients only.
7)  Allows a staff nurse to update a patient's nursing ward location and/or nursing AMIS bed section to insure accurate patient classification entries.
8)  Allows users to enter vital signs, height, and weight on patients. Cumulative reports by patient or ward can be generated as well as latest patient information. A simulated graphic report of vital sign information is also provided.
9)  Allows users to generate Intake and Output reports, an End of Shift Report, and a Health Summary Report by patient or ward.

> Performance Improvement:

1)  Contains options for reviewing patient classification and tracking errors.
2)  Allows nursing QA staff and ADP coordinators to revise erroneous AMIS data.
3)  Tracks units with no manhours data.

> Package Management:

1)  Allows sites to modify data (e.g., service positions, salary, grade/step codes, certifications, nursing locations, tour of duty) in specified nursing files.
2)  Accommodates additional site-specific standard care plans.
3)  Provides special ADP coordinator functions for executing nursing options which affect patient acuity, manhours, FTEE status, etc., when TaskMan is off-line.
4)  Provides ADP coordinator options for admitting/transferring/discharging patients within the Nursing system when the PIMS System is off-line. This feature ensures that patient information will be updated and available to nursing providers. When the package is off-line due to the installation of a new version, the software will automatically update the patients in the Nursing system by admitting and discharging patients before the system is made available to the user.

> For additional information refer to the Release Notes and Installation Guide for Version 4.0.

> 4 Nursing V. 4.0 April 1997

# Chapter 1 Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The intent of this section is to outline a method for the nursing ADPAC to implement the application. It is important to read and fully understand this section before continuing.

## Virgin Installation of Software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following steps should be followed when the Nursing software is installed in an environment where no previous installation of the Nursing application has taken place. If a previous version of the Nursing application has been installed, refer to the Non-Virgin Installation of Software instructions found later in this chapter.

> Step 1: Setting up the software environment

> The Information Resources Management Service staff must install the software using the installation notes in either a test environment or the production (VAH) directory. Data entered into the test environment CANNOT be transferred into the production environment.

## Additional Information:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nursing V. 4.0 requires that the following V*IST*A packages must be loaded in order to fully use the package:

1.  VA FileMan V. 21 or greater,
2.  Kernel V. 8.0 or greater,
3.  Kernel Toolkit V. 7.3 or greater,
4.  PIMS V. 5.3 or greater,
5.  PAID V. 4.0 or greater (optional),
6.  Dietetics V. 4.6 or greater (optional),
7.  Health Summary V. 2.7 or greater (optional),
8.  Intake and Output V. 4.0,
9.  Vitals/Measurements V. 4.0,
10. Text Generator V. 3.0.

## Recommendation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A limited amount of data should be entered into the test directory so the users may become familiar with the application and to establish an acceptable training data base.

> The following steps MUST BE COMPLETED before the Nursing software can become operational.

> \*\*\*\*\*\*\*\*\*\*Steps 2 THRU 5 MUST BE COMPLETED IN EXACT ORDER\*\*\*\*\*\*\*\*\*\*

> Step 2: Associating nursing units with MAS wards

> A comparison listing of ALL nursing locations (units) and ALL MAS ward locations (i.e., MAS location contained in File \#42, the Ward Location file) must be compiled. This information will be required by the nursing application coordinator when entering data in the NURS Location (#211.4) file (refer to the Nursing User Manual, Maintenance of Administrative Site Files chapter). Information on File \#42 should be provided by either the PIMS application coordinator or the IRMS staff. The NURS Location file's data must account for all MAS ward names in File \#42. The data in the NURS Location file establishes a cross-reference file which is accessed in all modules of the Nursing software.

## Recommendation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create the following comparison table for all nursing units.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Nursing Location</th>
<th><blockquote>
<p>MAS Location</p>
</blockquote></th>
<th><blockquote>
<p>Explanation of Nursing and MAS Locations</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1E</td>
<td><blockquote>
<p>1E</p>
</blockquote></td>
<td><blockquote>
<p>No discrepancy in nursing and MAS terminology.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>1W</td>
<td><blockquote>
<p>1W, 1NW, 1S</p>
</blockquote></td>
<td><blockquote>
<p>Nursing 1W is divided into multiple MAS locations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ER</td>
<td></td>
<td><blockquote>
<p>The ER is NOT a MAS ward location. It is a designated nursing assignment location</p>
<p>only.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9S</td>
<td><blockquote>
<p>9W</p>
</blockquote></td>
<td><blockquote>
<p>9W is considered a single MAS location but 9M is comprised of two (2) nursing locations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MASONLY</td>
<td><blockquote>
<p>HALL, ANNEX, MARS</p>
</blockquote></td>
<td><blockquote>
<p>The MASONLY location is used for two (2) purposes:</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>1) To associate all closed or inactive MAS wards with a nursing location.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>2) To identify active MAS wards (with patients) where nursing has no patient care responsibility.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Nursing Location MAS Location Explanation of Nursing and MAS Locations

> Note: All MAS wards in File \#42 must be identified and associated with a nursing location in File \#211.4. In both of the examples, the Patient Care Status field of the MASONLY unit should be "inactive" and the Ward Status field should be "active".

> Note: MASONLY is pronounced "M-A-S-ONLY".

> Diagram: This schematic depicts the relationship between the NURS Location (211.4), the Hospital Location (#44) and the Ward Location (#42) files.

> HOSPITAL LOCATION

> .01 NAME

> .

> .

> .

> 42 WARD LOCATION FILE POINTER

> .

> .

> .

> NURS LOCATION

> .01 NAME

> .

> .

> .

> WARD LOCATION

1.  NAME

> .

> .

> .

> 44 HOSPITAL LOCATION FILE POINTER

> .

> .

> .

> 2 MAS WARD

> .01 MAS WARD

.

.

.

.

.

.

> The NURS Location file points to entries in the Hospital Location file from its (.01) name field.

> The entries in the Hospital Location file pointed to by the NURS Location file are not inserted by the PIMS software. They are added by the Nursing application, and have the characters NUR appended in front to identify them. Due to a special look up and output transform, the NUR characters do not appear to the user during VA FileMan look-ups on the NURS Location file.

> However, these characters will appear to the user on look-ups on the Hospital Location file. This pointer relationship has been built because of a decision made by the Data Base Integration Committee (DBIC) to reduce the number of free text location files.

> The NURS Location file points to entries in the Ward Location file from the MAS Ward (#.01) subfield of the MAS Ward (#2) field. These entries are the normal Ward Location file entries. This pointer relationship is needed by the Nursing software to identify the appropriate nursing location of a patient when the patient is admitted through ADT (the admission, discharge, transfer module of PIMS).

> The Hospital Location and Ward Location files point to each other via the Ward Location file pointer (#42) and Hospital Locations file pointer (#44) fields respectively. This pointer relationship was set up via a decision by the DBIC to relate these two files to each other.

> Example: This example shows how this pointer relationship is used for a typical set of locations.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 39%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NURS LOCATION</p>
</blockquote></th>
<th><blockquote>
<p>HOSPITAL LOCATION</p>
</blockquote></th>
<th><blockquote>
<p>WARD LOCATION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3AS</p>
</blockquote></td>
<td><blockquote>
<p>NURS 3AS 3A</p>
<p>3S</p>
</blockquote></td>
<td><blockquote>
<p>3A</p>
<p>3S</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The nursing location of 3AS points to the hospital location NUR 3AS from the Name (#.01) field and the ward locations 3A and 3S from the MAS Ward (#2) field. The hospital location NUR 3AS does not point to the Ward Location file. The hospital location 3A points to the ward location 3A and vice versa. The hospital location 3S points to the ward location 3S and vice versa.

> Step 3: Population of the NURS Parameters (#213.9) file.

> This file is edited through the Site Parameter File option which is located in the Administrative Site File Functions Menu. Detailed information on this file is found in the chapter on Maintenance of Administrative Site Files in the Nursing User Manual. There are several specific issues that you need to address in the Parameter file before you enter data in the NURS Location file:

1.  Define your facility as single vs. multi-divisional facility.
2.  Identify that your facility has organized under a product line structure.
3.  Enter the name of the CNO printer. The CNO printer is a device used to print specific tasked reports and should remain on-line at all times.
4.  Enter a professional percentage value which will represent the default percentage of professional personnel assigned to a unit. This parameter is used for the calculation of workload required staffing when the

> professional percentage field is not defined for a specific NURS Location file entry.

5.  Enter cutoff times for the day, evening, and night shift (preferably the end of each shift) which is used by the AMIS Acuity Batch Job as cutoff times

> for classification of patients for these shifts.

> Additional IRMS related package management information is contained later in this chapter.

> Step 4:Populate the Facility field of the NURS AMIS 1106 FTEE (#213.2) file

> Using the FTEE Service Budget (1106b) File, Edit option, update the Facility field of the NURS AMIS 1106 FTEE (#213.2) file by entering the names of the institutions (divisions) associated with your facility. The Administrative and Resource Management Reports use this file to display a list of institutions when a ‘?’ is entered at the Facility prompt. At this time you do not have to enter the FTEE associated with each facility or institution.

> Step 5: Add data to Product Line file through the Product Line File Edit option in

> the Administrative Site File Functions option. This file has been exported with one entry, Nursing, that may not be deleted by any user. The application coordinator must add additional entries to this file if management wants to assign staff and locations to product lines. Entries in this file may relate to true product lines (e.g., medicine, surgery, mental health, primary care), programs, or the traditional services (e.g., nursing, social work, pharmacy) to produce reports that are meaningful to the users.

> Step 6: Population of the NURS Location file (#211.4)

> This file is edited through the Nursing Location File, Edit option which is located in the Administrative Site File Functions Menu. The process for entering information into this file can be found in the Maintenance of Administrative Site Files chapter in the Nursing User Manual.

> When editing this file, consider the following:

1.  Enter data into the NURS Location file from the list of nursing locations compiled in Step 2 above.
    1.  If you are a multi-divisional facility, you must enter the name of the institution associated with the unit location. If you are a single facility, it is recommended that you enter the facility’s name at the Institution prompt.
    2.  If management wants reports by product line, enter the product line associated with the unit. Remember that the product line prompt does not display unless you have entered ‘yes’ in the NURS Parameter file product line field.
    3.  The Patient Care Status field should be INACTIVE for all units until a decision is made to bring the Nursing software up (i.e., actively use the software) on an individual unit. Only then should the Patient Care Status field be changed to ACTIVE using the Ward Activation Patient Update option. Before activating the status of this field, please review the information on the Ward Activation Patient Update option in the Maintenance of Clinical Site Files chapter.
    4.  All units, regardless of patient care status, must be entered into the Nursing Location file.
2.  When the NURS Location file is completed, enter the Ward Activation Patient Update option located in the Clinical Site File Functions menu. This option runs a background job which checks that all MAS wards have been: a) associated with a nursing locations(s), and b) cross-referenced. The software displays the message,

> Checking to see if every MAS Ward has a corresponding NURSING unit,

> and if no problem exists, the "Select UNIT:" prompt appears. The user may enter an up- arrow (^) here to exit the option until units are ready to be populated with patients (refer to Step 6 below). If this background job identifies non-associated MAS ward(s), it displays the ward name(s) and the user must identify a relationship with a nursing unit.

> Step 7: Population of the NURS Service Position file (#211.3)

> This file is edited through the Service Position File, Edit option which is located in the Administrative Site File Functions Menu. The process for entering information into this file can be found in the Maintenance of Administrative Site Files chapter in the Nursing User Manual. In setting up this file, the application coordinator should assign all none nursing employees to an appropriate product line and associate them with the service category of ‘other’. Staff in traditional nursing roles, such as, registered nurse and nursing assistant, may be assigned to any product line but should be given the service category of registered nurse, licensed practical nurse and nursing assistant. Data in this file must be entered prior to entering names into the NURS Staff (#210) file.

> Step 8: Population of the NURS Staff file (#210)

> This file is edited through the Staff Record Edit option, which is located in the Administration Records, Enter/Edit Menu. A detailed explanation for entering information into this file can be found in Section 2 of the Nursing User Manual. Before the process of entering nursing employee names into the NURS Staff (#210) file can begin, the names of all current employees must reside in the New Person (#200) file. There is a laygo parameter located in the NURS Site Parameter (#213.9) file (Nursing New Person File Access field) that can be turned on to permit the storing of new nursing staff names in File \#200. It is suggested that if this feature is turned on, IRMS staff provide training to the nursing application coordinator on procedures for entering new names into File \#200.

> Step 9: Population of the NURS Patient file (#214)

1.  Patients are admitted through the PIMS application, however, patients are not automatically admitted into the Nursing software until the following actions have been taken:
    1.  The editing of the NURS Location file (#211.4) has been completed (Step 3).
    2.  The Ward Activation Patient Update option has been run for a specific nursing location. This option kicks off a routine which automatically assigns patients to appropriate nursing units in the Nursing software. Once a unit has been activated, all subsequent hospital admissions and transfers to the activated unit(s) are updated in the nursing software.

> Note: The Patient Care Status field in the NURS Location file is changed to ACTIVE by the action of the option's routine. The process of patient movement on that ward continues until the unit is inactivated or until 6.2. (below) occurs.

2.  When either the nursing software or the PIMS software is down (unavailable to the user), patients are not triggered into the Nursing software. In these circumstances, a backup option, Admit/Transfer Patient (Nursing Package Only), has been provided. This option should be available to the nursing ADP coordinator and other key nursing staff on all tours of duty.

> When the PIMS software goes back on-line, the nursing application coordinator should run the Ward Deactivation Patient Update and the Ward Activation Patient Update options (in that order) to validate the patient census on all nursing units.

3.  When additional wards are added to the nursing application repeat the ward activation option. Multiple units may be activated at once.
4.  In Multiple CPUs:
    1.  The routines NURSCPL, NURSAMSG and NURSAWCK used in triggering the patient into the Nursing software, must reside in all CPUs using the PIMS software.
    2.  The UCI translation table (in each CPU) must contain the NUR\* and GMR\* Globals.
5.  When patients are initially admitted to a newly activated unit the following steps should be taken:
    1.  A MAS bed census be printed.
    2.  A nursing bed census be printed through the Ward Census Print (NURSPP- LOCWRD) option.
    3.  A comparison be made of patients residing on the ward from both reports. If discrepancies are present, correct them using the Admit/Transfer Patient (Nursing Package Only) option.

> Step 10: Populating other site configurable files

> Review the following files. The edit/modify options associated with these files are located in the Administrative Site File Functions, Clinical Site File Functions, and QI Site Files menus of the Nursing application. The process and purpose for entering and editing data in these files is described later in this Package Management section. The specific edit option is listed with the file.

> Administrative Site Files:

1.  NURS Pay Scale (#211.1) file

> Edit using the Load Grade/Step Codes option.

2.  NURS Clinical Background (#211.5) file

> Edit using the Clinical Background File, Edit option.

3.  NURS Tour of Duty (#211.6) file

> Edit using the Tour of Duty File, Edit option.

4.  NURS AMIS 1106b FTEE (#213.2) file

> Edit using the FTEE Service Budget (1106b) File, Edit option.

5.  NURS Privilege (#212.6) file

> Edit using the Privilege File Edit option.

6.  NURS Vacancy/Transferred Reasons (#211.9) file Edit using the Vacancy Reason File Edit option.
7.  NURS Certification (#212.2) file

> Edit using the Certification File, Edit option.

> Clinical Site File Functions:

8.  GMRV Vital Category (120.53) file

> Display entries using the Display Vitals/Category Qualifier Table option.

9.  GMRV Vital Qualifier (#120.52) file

> Edit using the Enter/Edit Vitals Qualifiers option.

10. GMRY Intake Items ( \#126.8) file Edit using the Intake Items option.
11. GMRY Input Type (#126.56) file Edit using the Intake Type option.
12. GMRY IV Catheter (#126.74) file Edit using the IV Catheter option.
13. GMRY IV DC'ed Reason (#126.76) file Edit using the IV DC'ed Reason option.
14. GMRY IV Site (#126.7) file Edit using the IV Site option.
15. GMRY IV Site Description (#126.72) file Edit using the IV Site Description option.
16. GMRY NUR IV Solution (#126.9) file Edit using the IV Solution option.
17. GMRY Output Subtype (#126.6) file Edit using the Output Subtype option.
18. GMRY Output Type (126.58) file Edit using the Output Type option.
19. GMRY NUR Shift/Other (126.95) file

> Edit using the Shift Starting Hour and Other Parameters option.

20. Aggregate Term (#124.2) file

> Edit using the Patient Plan of Care, Site Configuration option.

> QI Site Files:

21. NURQ Standard of Care/Practice (#151) file

> Edit using the QI Summary Standards of Care/Practice File option.

22. NURQ Frequency (#154) file

> Edit using the QI Summary Frequency File option.

23. NURQ Rationale (#153) file

> Edit using the QI Summary Rationale File option.

> Step 11: Tasking required background jobs

> Notify the Site Manager to QUEUE the following jobs via TaskMan:

1.  The NURAAM-ACU (Nursing Acuity/Separation-Activation Run) option is queued to run daily after midnight as a background job requiring no device selection.

> This option (NURAAM-ACU) must be queued to run after midnight, daily. This job totals acuity data for each unit for the night, day, and evening shifts and stores the data in the NURS 1106 Manhours (#213.4) file. This job also activates/ separates employees to/from active status based on the vacancy date in the NURS Position Control (#211.8) file. When this option fails to run to completion, an alert is sent to the NURS-ADP mail group and the option must be run manually from the Special Functions menu. Patient classification is no longer disabled when this option fails to run to completion. Night shift acuity totals are based on patient classifications entered between 00:01 and the cutoff time of the night shift as indicated in the NURS Parameter (#213.9) file. If no classifications are entered on the night shift, the latest classification for the patient's unit on the job run date is used. If there are no classifications on the patient's current unit, no acuity is counted for the night shift. Day shift acuity is based on classifications entered between 00:01 and 15:00 (3:00pm). If a patient is discharged/transferred between 14:45 and 15:00 (2:45 - 3:00pm) and has a current classification for the run date, the acuity is credited to the unit where the patient resided prior to the discharge or transfer. The evening shift acuity totals are based on patients in the hospital at midnight who have been classified any time during the day. When run manually, this job checks the last time it ran to completion and runs for all days between the last time it ran (noted in File \#213.9) and the day before the current day. The data generated by this job is used for the following reports:

- AMIS workload statistics and summary reports
- patient category total reports (AMIS and midnight)
- separation/activation report
- unclassified patients report (AMIS and midnight)
- current unclassified patient reports

> Data for the report, Workload Statistics Report (Current), is not dependent on the NURAAM- ACU option.

> Note: When this job is run and there are MAS ward locations that do not have a matching nursing location, the user will get a mail message. The sender of the message will be the name of the person who queued the job to run.

2.  The NURAMN-MANCK (Nursing Batch Job Status Check) option is queued to run daily at 06:00 hours as a background job requiring no device selection. If this option finds that the Nursing Acuity/Separation-Activation Run (NURAAM-ACU) did not run to completion, an alert is sent to the appropriate personnel in the NURS-ADP mail group. It is then necessary to run the Manual Nursing Acuity/Separation Run under the Special Functions menu.

> Step 12: Tasking optional background jobs

> The following optional reports may be queued (TO THE CNO PRINTER) at the discretion of the Nursing ADP Coordinator:

1.  The NURAAM-UNCBAT (Batch Run of Unclassified AMIS 1106 Patients) option prints the unclassified AMIS 1106 patient list. To run this option manually, use the Unclassified AMIS 1106 Patients option under the Special Functions menu.
2.  The NURAAM-MD-UNCBAT (Batch Run of Unclassified Midnight Patients) option prints the unclassified midnight patient list. To run this option manually, use the Unclassified Midnight Patients option under the Special Functions menu.
3.  The NURAED-BATSEP-QUEUE (TaskManager Activation/Separation Report option prints daily position control changes on employees. The data for the reports (unclassified AMIS 1106 patients, unclassified midnight patient and position control changes) are generated by the Nursing Acuity/Separation-Activation Run (NURAAM-ACU) option. The NURAED-BATSEP-QUEUE option should be queued to run approximately two (2) hours after the NURAAM-ACU option is scheduled to ensure availability of the required data. To run this option manually, use the Employee Activation/Separation Report option under the Special Functions menu.
4.  The NURAPR-RES-CURWKL-QUEUE (TaskManager Workload Statistic Report (Current) option prints current workload statistics information. To run this option manually, use the Workload Statistics Report (Current) option under the Resource Management Reports menu.
5.  Add appropriate members to the NURS-ADP mail group. When setting up this mail group make sure the TYPE field is marked PUBLIC. The members of the group are notified when:
    1.  The alert, NURS-CLASSIFICATION, is forwarded to the mail group NURS-ADP if the Nursing Acuity/Separation-Activation Run did not run or aborted prior to completion.
    2.  The alert NURS SEPARATION/ACTIVATION is forwarded to the mail group NURS-ADP if the Nursing Acuity/Separation-Activation Run did not run or aborted prior to completion. The alerts are sent when appropriate by the option, NURAMN- MANCK.

> Step 13: Printer issues

> The application's reports were designed to be used with the Kyocera F-800A laser printers, HP LaserJet III printers, and the HP LaserJet 4 printers, but they can also be printed on dot matrix printers. When using a programmable graphic laser printer the setups need to be checked, to insure the correct format on the printed page.

> The following special printer setup is for Kyocera type printers:

1.  Ensure the existence of a Kyocera entry in the Terminal Type file. This device compresses print and has a margin width of 132 characters. This entry may be exported by Kernel, or you may have to set up your own entry.
    1.  The Name (#.01) field should begin with the characters P-KYOCERA e.g., P- KYOCERA-P16. This is important as the software will not recognize the device as a Kyocera printer if this Terminal Type entry is not set up properly.
    2.  The Right Margin (#1) field must be 132.
2.  Create a Device file entry for the Kyocera printer.
    1.  The Name (#.01) field should contain the word KYOCERA. This isn't required, but will make selection of this device by users easier.
    2.  Sub-Type (#3) field should point to a Terminal Type entry that fits the characteristics defined above in (a-1).
    3.  Margin Width (#9) field should be 132.
3.  In the Kyocera printer, PRESCRIBE Macro Buffer Size (H0)=99. To reprogram your printer,
    1.  Type: !R! RES; FRPO H0, 99; EXIT; on your terminal/input device.
    2.  Print this code on your Kyocera printer (using appropriate print commands). This may be done through a mail message.
    3.  Turn off the printer for a few seconds, then place the printer back on line (by turning it on). The printer will then be ready to print the linear graphic reports (e.g., SF511).

> The following special printer setup is for HP LASERJET III, HP LASERJET 4 and HP LASERJET 5 printers:

1.  Ensure the existence of a HP LASERJET entry in the Terminal Type file. This device compresses print and has a margin width of 132 characters. This entry may be exported by Kernel, or you may have to set up your own entry.
    1.  The Name (#.01) field should begin with the characters P-HPLASER e.g., P-HPLASER- L180. This is important as the Vitals/Measurements software will not recognize the device as an HP LASERJET printer if this Terminal Type entry is not set up properly.
    2.  The Right Margin (#1) field must be 132.
2.  Create a Device file entry for the HP LASERJET printer.
    1.  The Name (#.01) field should contain the word HPLASER. This isn't required, but will make selection of this device by users easier.
    2.  Sub-Type (#3) field should point to a Terminal Type entry that fits the characteristics defined above in (b-1).
    3.  Margin Width (#9) field should be 132.
    4.  Suppress Form Feed at Close (#11.2) field should be set to YES.

> Note: If the printer is not set up correctly, it will affect the printed output. KYOCERA and HPLASER are key words in the routine to identify which printer is being used, and IRMS must edit the Device file so the word KYOCERA or HPLASER appears in the name of the device (e.g., KYOCERA-PORT).

> The IRMS staff should assign the CNO Printer in every CPU using the Nursing application.

> This printer is used to alert nursing management of unusual actions (e.g., Doe, John has not been admitted into the NURSING System by PIMS because the MAS ward does not have a corresponding NURSING LOCATION). The CNO Printer should be on-line and accessible at all times.

> Step 14: Package Management/Special Security Measures

1.  The nursing ADP coordinator(s) must be given the VA FileMan security code of "n". This access allows the application coordinator to view all nursing employee information.
2.  Assign an appropriate PAID Education Tracking key (PRSE SUP and PRSE TRAIN) to nursing personnel. The PRSE SUP key should be given to any nursing educator/instructor. The PRSE TRAIN key should be assigned to nursing staff (exclusive of management staff) who have nursing unit staff education responsibilities. Note: Only assign one key to each nursing employee.
3.  No additional security measures are required other than those implemented through Menu Manager and the package routines.
4.  No additional licenses are necessary to run the software.
5.  Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

> Step 15: Operating in multiple CPUs

> When operating the PIMS and nursing application in multiple CPUs refer to steps 6.4, 8, 9 and 10 above.

> Step 16: Assigning menus

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 46%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Menu</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Menu Text</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Staff Position</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NURS-SYS-MGR</p>
</blockquote></td>
<td><blockquote>
<p>Nursing System Manager's Menu</p>
</blockquote></td>
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ADP Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURS-ADM</p>
</blockquote></td>
<td><blockquote>
<p>Administrator's Menu</p>
</blockquote></td>
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Administration Staff</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURS-ED</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Educator's Menu</p>
</blockquote></td>
<td><blockquote>
<p>Nursing Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Staff</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURS-QA</p>
</blockquote></td>
<td><blockquote>
<p>QA Coordinator's Menu</p>
</blockquote></td>
<td><blockquote>
<p>Q.A. Coordinator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NURS-HN</p>
</blockquote></td>
<td><blockquote>
<p>Head Nurse's Menu</p>
</blockquote></td>
<td><blockquote>
<p>All Head Nurses</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURS-RN</p>
</blockquote></td>
<td><blockquote>
<p>Staff Nurse Menu</p>
</blockquote></td>
<td><blockquote>
<p>All Staff Nurses</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Non-Virgin Installation of software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow steps 1 through 16 under Virgin Installation of software (refer to page 1 of this chapter) to complete the installation of Version 4.0.

## Site Configurable Files/Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The NURS Parameters (#213.9) file.

> The data elements in the NURS Parameters file can be modified by the site. Below is a list of these data elements.

> <u>Field</u> 2

> 3

> 4

> TO THE NEW PERSON FILE 1: ACCESS

> TO THE NEW PERSON FILE

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 32%" />
<col style="width: 24%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>7.1</p>
</blockquote></th>
<th><blockquote>
<p>DAY SHIFT ACUITY TIME</p>
</blockquote></th>
<th><blockquote>
<p>military time of</p>
<p>4 characters in length</p>
</blockquote></th>
<th><blockquote>
<p>Time at which the acuity totals are calculated for the day shift for the Workload Statistics Report (Current).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7.2</p>
</blockquote></td>
<td><blockquote>
<p>EVENING SHIFT ACUITY TIME</p>
</blockquote></td>
<td><blockquote>
<p>military time of</p>
<p>4 characters in length.</p>
</blockquote></td>
<td><blockquote>
<p>Time at which the acuity totals are calculated for the evening shift for the Workload Statistics Report (Current).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7.3</p>
</blockquote></td>
<td><blockquote>
<p>NIGHT SHIFT ACUITY TIME</p>
</blockquote></td>
<td><blockquote>
<p>military time of</p>
<p>4 characters in length.</p>
</blockquote></td>
<td><blockquote>
<p>Time at which the acuity totals are calculated for the night shift for the Workload Statistics Report (Current).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>PROFESSIONAL PERCENTAGE</p>
</blockquote></td>
<td><blockquote>
<p>percentage from</p>
<p>1 to 100 with no decimal place</p>
</blockquote></td>
<td><blockquote>
<p>The percentage of professionals to non- professionals for a given nursing location. This value will be used if the corresponding field in the NURS Location File (#211.4) has no data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCT LINE</p>
</blockquote></td>
<td><blockquote>
<p>Y=Yes N=No</p>
</blockquote></td>
<td><blockquote>
<p>Indicates whether or not FTEE data in the NURS Position Control file (#211.8) is associated with product lines besides Nursing.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>MULTI-DIVISIONAL</p>
</blockquote></td>
<td><blockquote>
<p>Y=Yes N=No</p>
</blockquote></td>
<td><blockquote>
<p>Indicates whether or not the facility is multi- divisional.</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Prime Document Enter/Edit.

> The site may need to modify the content of the Nursing Care Plan (i.e., Patient Plan of Care) sent out with the Nursing package. To do this, the site would have to use the Patient Plan of Care, Site Configuration (NURCFE-CARE) option. The site will be able to make local modifications to the content of the prime document without having to worry about a subsequent release of that application overwriting them.

## Site Configurable Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no site configurable sort or print templates in Version 4.0 of the Nursing package. The sort and print templates in the package are not subject to modification. The nursing application coordinator has been given certain FileMan options, from which site specific outputs could be generated using Option 2 (PRINT FILE ENTRIES). Any additional templates created should be named with the following convention:

> NURS-Site Number (3 digit code assigned to each site)-Choose (P for print templates, S for sort templates)-Template name

> ex. NURS-578-P-MANDATORY INSERVICE (print template) NURS-578-S-STAFF SORT (sort template)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The minimal hardware requirements for the Nursing software are two CRTs and one printer per nursing location. In addition to this, the following statistics regarding the disk storage requirements of the Nursing software were compiled by the Alpha/Beta test sites.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 47%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Globals</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Type of Data</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Size</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DDs</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>340 blocks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NURSA</p>
</blockquote></td>
<td><blockquote>
<p>AMIS data classification</p>
</blockquote></td>
<td><blockquote>
<p>3-4 blocks/nursing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURC</p>
</blockquote></td>
<td><blockquote>
<p>Care plan data</p>
</blockquote></td>
<td><blockquote>
<p>location</p>
<p>2-12 blocks/patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NURQ</p>
</blockquote></td>
<td><blockquote>
<p>QI Summary</p>
</blockquote></td>
<td><blockquote>
<p>1-18 blocks/patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NURSF</p>
</blockquote></td>
<td><blockquote>
<p>Staff data</p>
</blockquote></td>
<td><blockquote>
<p>.86 blocks/staff</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 42%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Globals</u> NURSF(213.1</p>
</blockquote></th>
<th><blockquote>
<p><u>Type of Data</u> Nursing pointer files</p>
</blockquote></th>
<th><blockquote>
<p><u>Size</u></p>
<p>block size is dependent upon class of hospital:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Class I - 296 Class II - 256 Class III - 111 Class V - 98</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMR</p>
</blockquote></td>
<td><blockquote>
<p>Patient data for the Vitals/Measurements, and Intake and Output Modules</p>
</blockquote></td>
<td><blockquote>
<p>50-75 blocks/ patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRD</p>
</blockquote></td>
<td><blockquote>
<p>Static data for the Vitals/Measurements, and Intake and Output Modules</p>
</blockquote></td>
<td><blockquote>
<p>1200-1400 blocks depending on the global efficiency</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Routines</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>approx. 800k</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Technical Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ADT Functions of MAS System abort with \<NOSYS\> error.
    1.  When the CPU containing the Nursing system is down, the MAS system aborts with a

> \<NOSYS\> error. To correct this problem:

1.  Take the Nursing system off-line using the Nursing Offline/Online Switch in the NURS Parameters (#213.9) file.
2.  After the CPU is brought up again the Nursing system should be placed on-line, and all patient movements in MAS should be put into the Nursing system. The best way of updating the patient movements is to run the Ward Deactivation Patient Update (NURSPT-WRDINA) option followed by the Ward Activation Patient Update (NURSPT-WRDACT) option after placing the Nursing system on-line.
2.  User gets a warning message that the Nursing Acuity/Separation-Activation Run (NURAAM-ACU) option has not run to completion.
    1.  Four fields in the NURS Parameters file (#213.9) exist to help in debugging and recovery of errors encountered by this task (see Site Configurable Files/Fields).
        1.  Date AMIS Job Last Run Field (#6.1) - The date in this field is the date the Nursing Acuity/Separation-Activation Run (NURAAM-ACU) option last ran normally to completion.
        2.  AMIS Job Completion Field (#6.4) - This is a set of codes that denotes whether the last running of the NURAAM-ACU option ran to completion. One denotes the job finished normally, and zero denotes that the job terminated abnormally.
        3.  AMIS Ward Last Processed Field (#6.5) - This field contains an internal entry number in the NURS Location file (#211.4). This is the location that was last processed by the NURAAM-ACU option.
        4.  AMIS Patient Last Processed Field (#6.6) - This is an internal entry number in the Patient file (#2). This is the patient that was last processed by the NURAAM-ACU option.
    2.  The first thing that should be attempted is to run the Manual Nursing Acuity/Separation Run (NURAAM-ACUMAN) option. The fields referenced above, will cause the NURAAM-ACUMAN option to begin processing from where the NURAAM-ACU option left off.
    3.  If while running the NURAAM-ACUMAN option an error occurs, the Site Manager should check the following global node:

> ^DIC(213.9,1,"DATE")=A^B^0^0^^C^0^0^D^E^0^0^F

> where:

> A is the data in field 6.1 and should be equal to a FileMan date for today's date. B is the data in field 6.4 and should be equal to the number 1.

> C is the data in field 6.8 and should be equal to the number 1. D is the data in field 6.92 and should be equal to the number 1. E is the data in field 6.93 and should be equal to the number 1.

> F is the data in field 56. If there is a value in this field it means the acuity job is currently running or possibly errored out before completion.

> For example:

> ^DIC(213.9,1,"DATE") = 2970220^1^0^0^^1^0^0^1^1^0^0^

> The problem probably lies in bad data or cross-references in the NURS Patient file (#214) or NURS Classification file (#214.6) and should be repaired on an individual basis.

3.  Patients are not being automatically admitted to, or discharged in the Nursing package.
    1.  Check the ANURS cross-reference on field .1 of File 2. If it is not correctly defined, delete the erroneous data and correctly define the cross-reference using the following procedure in programmers mode:

> \>D KILLXREF^NURSCUTL

> \>D SETXREF^NURSCUTL

> The xref should appear as follows:

> ^DD(2,.1,1,IEN,0) = 2^ANURS^MUMPS

> ^DD(2,.1,1,IEN,1) = S %X=X,X="NURSCPL" X ^%ZOSF("TEST") S X=%X D:\$T EN1^NURSCPL

> ^DD(2,.1,1,IEN,2) = S %X=X,X="NURSCPL" X ^%ZOSF("TEST") S X=%X D:\$T EN2^NURSCPL

# Chapter 2 Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A listing of GMRY routines and their descriptions can be found in the Intake and Output Technical Manual and Package Security Guide.

> A listing of GMRV routines and their descriptions can be found in the Vitals/ Measurements Technical Manual and Package Security Guide.

> NUR Routines

> NURA ;HIRMFO/RM/JH/MD-ROUTINE TO CHECK FOR VERSION NUMBER, AND RUN NURS. ADMIN. MENU ;8/16/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA5A ;HIRMFO/MD,FT-SALARY REPORT FOR ENTIRE SERVICE ;8/8/96 12:42

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA5B ;HIRMFO/PC,RM,JH,MD,FT-INDIVIDUAL SALARY REPORTS ;5/7/96 10:57

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6A1 ;HIRMFO/JH/MD,FT-ACADEMIC DEGREE REPORT BY SVC. CATEGORY ;8/8/96 12:52

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6B1 ;HIRMFO/RM/YH,FT-AGE REPORT BY LOCATION BY CATEGORY ;8/8/96 13:02

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6B2 ;HIRMFO/RM/MD,FT-AGE REPORT BY LOCATION BY POSITION ;8/8/96 13:04

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6C1 ;HIRMFO/MD,FT-CATEGORY CERTIFICATION REPORT BY SVC. ;7/8/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6C2 ;HIRMFO/MD,FT-SERVICE POSITION CERTIFICATION REPORT ;8/8/96 13:09

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6D1 ;HIRMFO/MD,RM,FT-FTEE PROFILE BY SERVICE CATEGORY ;8/23/96 12:06

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6D2 ;HIRMFO/MD,RM,FT-FTEE PROFILE BY SERVICE POSITION ;8/24/96 10:29

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6E1 ;HIRMFO/JH/MD,FT-CATEGORY, GENDER REPORT BY SERVICE ;8/8/96 13:23

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6F1 ;HIRMFO/JH/MD,FT-GRADE PROFILE BY SERVICE CATEGORY ;8/8/96 13:25

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6G ;HIRMFO/MD,RM,FT-LICENSE PROFILE BY SERVICE CATEGORY ;8/23/96 09:34

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6H1 ;HIRMFO/JH/MD,FT-CATEGORY, MILITARY REPORT ;8/8/96 13:31

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6I1 ;HIRMFO/RM,JH,MD,FT-INDIVIDUAL NPSB REPORT ;8/8/96 13:34

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6I2 ;HIRMFO/MD,RM,FT-NPSB REPORT FOR ENTIRE SERVICE ;8/23/96 09:46

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6J1 ;HIRMFO/JH/MD,FT-NURSING EDUCATION PROFILE BY SVC. CATEGORY ;8/8/96 13:40

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6K1 ;HIRMFO/RM,JH,MD,FT-INDIVIDUAL PROFICIENCY REPORT ;8/8/96 13:14

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA6K2 ;HIRMFO/MD,FT-NURSING SERVICE PROFICIENCY REPORT BY SERVICE ;8/8/96 13:43

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA7A ;HIRMFO/MD,FT-HOME PHONE NUMBERS FOR ENTIRE STAFF ;8/8/96 13:45

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA7B ;HIRMFO/MD/RM/JH/MD,FT-HOME PHONE NUMBER(S) BY LOCATION ;8/8/96 13:48

> NURA7C ;HIRMFO/MD,FT-INDIVIDUAL PHONE NUMBER ;8/8/96 13:50

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9A1 ;HIRMFO/JH/MD,FT-ACADEMIC DEGREE REPORT BY SVC. CATEGORY AND LOCATION ;8/8/96 13:53

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9B1 ;HIRMFO/RM,FT-AGE REPORT BY LOCATION BY CATEGORY ;8/8/96 14:01

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9B2 ;HIRMFO/RM/YH,FT-AGE REPORT BY LOCATION BY POSITION ;8/9/96 10:02

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9C1 ;HIRMFO/MD,FT-SERVICE CATEGORY CERTIFICATION REPORT BY LOCATION

> ;8/9/96 10:04

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9C2 ;HIRMFO/MD,FT-SERVICE POSITION CERTIFICATION REPORT BY LOCATION

> ;8/9/96 10:13

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9D1 ;HIRMFO/MD,RM,FT-FTEE PROFILE BY LOCATION AND SERVICE CATEGORY

> ;8/9/96 10:16

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9D11 ;HIRMFO/MD-SORT ROUTINE FOR NS BUDGETED/ACTUAL FTEE BY WARD ;8/23/96 12:05

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9D2 ;HIRMFO/YH,MH,MD,RM,FT-FTEE PROFILE BY LOCATION AND SERVICE POSITION

> ;8/23/96 10:33

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9E1 ;HIRMFO/JH,FT-CATEGORY, GENDER REPORT BY LOCATION ;11/30/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9F1 ;HIRMFO/JH/MD-GRADE PROFILE BY SERVICE CATEGORY BY LOCATION ;7/10/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9G ;HIRMFO/MD,RM,FT-LICENSE PROFILE BY LOCATION ;8/9/96 10:50

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9H1 ;HIRMFO/JH/MD,FT-CATEGORY, MILITARY REPORT BY LOCATION ;8/9/96 11:08

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9I ;HIRMFO/MD,FT-NPSB REPORT BY LOCATION ;8/23/96 10:39

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9J1 ;HIRMFO/JH,FT-NURSING EDUCATION PROFILE BY LOCATION/SVC. CATEGORY

> ;8/9/96 11:10

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURA9K ;HIRMFO/MD,FT-NURSING SERVICE PROFICIENCY REPORT BY LOCATION ;8/9/96 09:14

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAE0 ;HIRMFO/RM,MD,FT-EDIT ACUITY TOTALS...AMIS 1106a ;8/14/96 09:35

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAE1 ;HIRMFO/RM-EDIT ACUITY TOTALS...AMIS A1106-cont. ;AUG 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAGS0 ;HIRMFO/RM,JH,MD-MULTIDIVISIONAL GENERIC SORT ROUTINE FOR ADMIN REPORTS ;11/18/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAGS1 ;HIRMFO/RM,MD-MULTIDIVISIONAL GENERIC SORT ROUTINE FOR ADMIN REPORTS

> ;11/18/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU0 ;HIRMFO/RM,MD-DRIVER FOR ACUITY COUNTS...AMIS 1106a ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU1 ;HIRMFO/RM/MD-DRIVER FOR ACUITY COUNTS...(cont.) ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU2 ;HIRMFO/RM/MD-BACKUP IF NURAAU0 NOT RUN...AMIS 1106a ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU3 ;HIRMFO/RM,MD-PURGE MODULE...AMIS A1106 ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU4 ;HIRMFO/MD-DRIVER FOR ACUITY COUNTS...(count) ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAAU5 ;HIRMFO/FT-Check if every MAS Ward has a Nursing Location ;1/7/97 11:41

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE0 ;HIRMFO/RM-PATIENT CLASSIFICATION DRIVER ;4/15/88

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE1 ;HIRMFO/RM/MD-PATIENT CLASSIFICATION DRIVER-cont ;11/4/87

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE2 ;HIRMFO/RM-PATIENT CLASSIFICATION MEDICAL/SURGICAL ;NOVEMBER 17, 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE3 ;HIRMFO/RM-PATIENT CLASSIFICATION FACTOR LISTS ;APRIL 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE4 ;HIRMFO/RM-PATIENT CLASSIFICATION PSYCHIATRIC ;NOVEMBER 17, 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE5 ;HIRMFO/RM-PATIENT CLASSIFICATION CRITICAL CARE ;08 Apr 86

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE6 ;HIRMFO/RM-PATIENT CLASSIFICATION EXTENDED CARE ;NOVEMBER 17, 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE7 ;HIRMFO/MD-RM-PATIENT CLASSIFICATION DRIVER-cont. ;6/6/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE8 ;HIRMFO/RM,FT-PATIENT CLASSIFICATION FACTOR CHECKS ;1/9/97 13:53

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACE9 ;HIRMFO/MD-PATIENT CLASSIFICATION MEDICAL (SCI) ;7/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACEW ;HIRMFO/RM,MD,FT-CLASSIFY PATIENTS ON A GIVEN WARD ;8/14/96 09:57

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACEW0 ;HIRMFO/RM,MD,FT-DRIVER CHECK FOR PATIENTS NOT CLASSIFIED BY WARD

> ;8/14/96 09:59

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACEW1 ;HIRMFO/RM-CHECK FOR PATIENTS NOT CLASSIFIED BY WARD...cont. ;MAY 1985

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACHDC ;HIRMFO/MD,FT-HEMODIALYSIS PATIENTS TO ACUITY TOTALS ;9/25/96 12:26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURACUIT ;HIRMFO/MD-ROUTINE TO REPAIR FUTURE ACUITY DATA FROM ERRONEOUS BATCH RUN

> ;;4.0;Nursing Service;;Jan 24, 1996

> NURADEG ;HIRMFO/JH,FT-LIST STAFFS' COMBINED NURSING AND ACADEMIC DEGREES

> ;11/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURADEG1 ;HIRMFO/JH,FT-COMBINED EDUCATIONAL REPORT BY LOCATION ;8/9/96 09:17

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURADEG2 ;HIRMFO/JH,FT-COMBINED EDUCATIONAL REPORT BY SERVICE ;6/14/94

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURADEG3 ;HIRMFO/JH-INDEVIDUAL, COMBINED EDUCATIONAL REPORT ;6/14/94

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURADMIN ;HIRMFO/JH/MD-GENERIC ADMINISTRATION PRINT SELECTION ROUTINE

> ;10/25/90

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAED0 ;HIRMFO/RM,JH,FT-MODULE TO EDIT NURS STAFF FILE ;8/23/96 10:41

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAED01 ;HIRMFO/RM-Cont. of NURAED0 routine ;2/26/92

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURAED1 ;HIRMFO/MD,RM-EDIT FOR POSITION ;1/23/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURAED2 ;HIRMFO/MD,RM-EDIT FOR POSITION ;1/24/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAED3 ;HIRMFO/RM,MD,FT-HELP ROUTINE FOR NURSING DATA ;8/9/96 12:33

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURAED4 ;HIRMFO/MD/RM-DATA ENTRY FOR POSITION ;10/15/90

> NURAED5 ;HIRMFO/MD-PROCESS POSITION MODIFICATIONS ;2/28/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAED6 ;HIRMFO/RM-DATA STORAGE TMP FOR THE POSITION EDIT ;7/11/90

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAED7 ;HIRMFO/MD-DATA STOREGE TMP FOR THE POSITION EDIT CONTINUED ;1/15/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAEDCK ;HIRMFO/RM-ROUTINE CALCULATES HIGHEST NURSING DEGREE ;SEPTEMBER 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAFSD ;HIRMFO/MD-EMPLOYEE ACT/SEP MANUAL AND TASKED REPORTS ;26 AUG 96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAGE ;HIRMFO/RM/MD,FT-PRINT MODULE FOR AGE PROFILE REPORT ;8/9/96 11:26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAGEN ;HIRMFO/JH,FT-GENERIC REPORT GENERATOR FOR ADMIN. part 1 ;8/9/96 11:28

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAGEN1 ;HIRMFO/JH/MD-GENERIC REPORT GENERATOR FOR ADMIN. part 2 ;7/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAGEN2 ;HIRMFO/JH/MD-GENERIC REPORT GENERATOR FOR ADMIN. part 2 ;MAR 95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURAKIL1 ;HIRMFO/MD-CONT CLEAN-UP 1/15/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURAKILL ;HIRMFO/MD,FT-CLEAN-UP ;8/9/96 09:28

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAMB1 ;HIRMFO/MD,FT-BATCH JOB TO UPDATE ACUITY RUN ;10/9/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAMB3 ;HIRMFO/MD-MANHOURS BATCH JOB STATUS ROUTINE ;FEB 89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAMH9 ;HIRMFO/JH,FT,MD-MANHOURS EXCEPTION REPORT ;8/26/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAMHE ;HIRMFO/MD,FT-NURSING MANHOURS ENTER/EDIT FUNCTION ;8/14/96 09:45

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURAMHU ;HIRMFO/MD-MANHOURS TMP ROUTINE ;3/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAMU3 ;HIRMFO/MD-EMPLOYEE ACT/SEP BATCH JOB 9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAPROD ;HIRMFO/MD-POPULATE POSITION CONTROL PRODUCT LINE

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAR110 ;HIRMFO/MD-PRINT MODULE FOR FTEE COMPARISON BY LOCATION ;6/6/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAR11A ;HIRMFO/MD-COMPARISON REPORT BY LOCATION ;8/23/96 10:43

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURAR1A ;HIRMFO/MD,FT-ACCUMULATES FTEE TOTALS AND RUNS SVC. AMIS 1106b REPORT ;9/18/96 16:57

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARCR0 ;HIRMFO/RM/RD-VIEW PRINT OF PATIENT CLASSIFICATION ;1/17/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARCR1 ;HIRMFO/MD,FT-CONTINUATION VIEW PRINT OF PATIENT CLASSIFICATION

> ;8/9/96 11:32

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARCRW ;HIRMFO/RM/MD/FT-VIEW PRINT PATIENT CLASSIFICATIONS BY WARD ;1/9/97 15:24

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARFBU ;HIRMFO/RM,MD,FT-AMIS REPORT 1106b...ENTER BUDGET FIGURES ;8/23/96 10:45

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARMC0 ;HIRMFO/MD-DRIVER TO PRINT MIDNIGHT ACUITY REPORTS 2/2/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARMH0 ;HIRMFO/RM/MD-DRIVER TO PRINT AMIS 1106 PATIENT CARE MANHOURS REPORTS ;2/17/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARMH1 ;HIRMFO/MD,RM,FT-CONTINUATION OF 1106 PATIENT CARE MANHOURS DRIVER PRINT ;8/9/96 11:34

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARMH2 ;HIRMFO/MD,FT-CONTINUATION OF DRIVER TO PRINT AMIS 1106 MANHOURS REPORTS ;8/9/96 12:40

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARNCT ;HIRMFO/RM/MD,FT-REPORT SHOWING NOT CLASSIFIED PATIENTS FOR HOSP. 2/2/96 ;8/9/96 11:35

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARPC0 ;HIRMFO/MD-DRIVER TO PRINT AMIS 1106 ACUITY REPORTS ;2/28/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARPC1 ;HIRMFO/RM/MD-PRINT AMIS 1106 ACUITY REPORTS (cont.) ;2/17/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARPC2 ;HIRMFO/MD-CONTINUATION OF DRIVER TO PRINT AMIS 1106 ACUITY REPORTS

> ;8/2/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARPC3 ;HIRMFO/MD,FT-CONTINUATION OF 1106 ACUITY REPORT DRIVER ;8/9/96 11:36

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARPC4 ;HIRMFO/MD-CONTINUATION OF DRIVER TO PRINT AMIS 1106 PATIENT CATEGORY TOTAL ;7/23/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARST ;HIRMFO/MD-GENERIC RESOURCE MANAGEMENT PRINT SELECTION ROUTINE ;JULY 1990

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL1 ;HIRMFO/RM,MD-(CURRENT) MANHOURS WORKLOAD STATISTICS REPORT ;7/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL2 ;HIRMFO/MD-(CURRENT) MANHOURS WORKLOAD STAT REPORT FOR HOSP. CON'T

> ;2/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL3 ;HIRMFO/MD,FT-CONTINUATION OF THE (CURRENT) WORKLOAD STATISTICS

> ;12/11/96 10:45

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL4 ;HIRMFO/MD-MANHOURS AMIS 1106a WORK LOAD STATISTICS ;9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL5 ;HIRMFO/MD-MANHOURS AMIS 1106a WORK LOAD STATISTICS CONT OF NURARWL4

> ;9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL6 ;HIRMFO/MD/-MANHOURS AMIS 1106a WORKLOAD STATISTICS CONT OF NURARWL5

> ;9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL7 ;HIRMFO/MD,FT-DAILY TOTAL ROUTINE FOR AMIS WORKLOAD STATISTICS REPORT ;9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL8 ;HIRMFO/MD-HOSPITAL TOTAL ROUTINE FOR WORKLOAD STATISTICS REPORTS

> ;9/20/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURARWL9 ;HIRMFO/MD-FACILITY TOTAL ROUTINE FOR WORKLOAD STATISTICS REPORTS

> ;6/6/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURASPL ;HIRMFO/MD-VIEW OF INDIVIDUAL STAFF POSITIONS

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURASPT ;HIRMFO/BL,RM,FT-VIEW/PRINT FOR THE INDIVIDUAL STAFF RECORD ;5/7/96 11:08

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURC ;HIRMFO/RM;JH-ROUTINE TO CHECK FOR VERSION NUMBER, AND RUN NURS. CLIN. MENU ;12/23/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCAS0 ;HIRMFO/RM,MD,RTK,FT-PATIENT CENSUS/ASSIGNMENT WORKSHEET WARD

> ;8/9/96 11:44

> NURCAS1 ;HIRMFO/MD/RM/MD-PATIENT PROBLEM/NURSING INTERVENTION PRINT ;10/2/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCAS2 ;HIRMFO/MD,FT-UTILITY(\$J) ARRAY BUILDER FOR ASSIGNMENT SHEET

> ;9/16/96 14:03

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCP1 ;HIRMFO/RM,RTK-STANDARD CARE PLAN, PRINT (main routine) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCP2 ;HIRMFO/RM-STANDARD CARE PLAN, PRINT (selection driver) ;1/23/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCP3 ;HIRMFO/RM-STANDARD CARE PLAN, PRINT (sort to get problems) ;3/9/92

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCP4 ;HIRMFO/RM,RTK-STANDARD CARE PLAN PRINT (print data) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPE ;HIRMFO/RM,RTK-NURSING CARE PLAN EDIT ;1/24/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU0 ;HIRMFO/RM-NURSING CARE PLAN UTILITIES ;1/28/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU1 ;HIRMFO/RM/MD-NURSING CARE PLAN UTILITIES (cont.) ;8/16/95

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU2 ;HIRMFO/RD/RM-NURSING CARE PLAN UTILITIES (cont.) ;10/30/90

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU3 ;HIRMFO/RD/RM,RTK/MD-NURSING CARE PLAN UTILITIES (cont.) ;8/16/95

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU4 ;HIRMFO/MD-NURSING CARE PLAN UTILITIES (cont.) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCCPU5 ;HIRMFO/RD/RM-NURSING CARE PLAN UTILITIES (cont.) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCES0 ;HIRMFO/YH,RM,FT,YH-END OF SHIFT REPORT PART 1/1 ;12/6/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCES01 ;HIRMFO/YH-END OF SHIFT REPORT PART 1/2 ;12/6/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCES1 ;HIRMFO/YH,MD,YH-END OF SHIFT REPORT PART 2 - NURSING CARE PROBLEM

> ;12/12/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCES2 ;HIRMFO/YH-END OF SHIFT REPORT PART 3 - ITEMIZED I/O DATA ;12/12/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCES3 ;HIRMFO/YH-END OF SHIFT REPORT PART 4 - INTRAVENOUS INFUSION

> ;12/12/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURCES4 ;HIRMFO/YH-END OF SHIFT - DIET ;12/12/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCES5 ;HIRMFO/YH-END OF SHIFT -VITAL/MEASUREMENT DATA ;12/5/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVE0 ;HIRMFO/RTK,RM-Nursing Care Plans Edit Report ;8/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVE1 ;HIRMFO/RTK,RM-Nursing Care Plans Edit Report ;8/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVE2 ;HIRMFO/RTK,RM/MD-Nursing Care Plans Edit Report ;8/16/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVE3 ;HIRMFO/RTK,RM/MD-Nursing Care Plans Edit Report ;8/16/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURCEVE4 ;HIRMFO/RM,RTK-EDE LINK TO GMRG ;8/23/93

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVE5 ;HIRMFO/RTK,RM-HIGHLIGHT EDITED CARE PLANS ;8/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCEVP0 ;HIRMFO/RTK,RM,MD-Nursing Care Plans Print Report ;8/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCHSUM ;HIRMFO/YH,RM-HEALTH SUMMARY REPORT BY NUR WARD/ROOM/PT ;3/29/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURCKIL1 ;HIRMFO/MD-CLEAN-UP ;1/15/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCKILL ;HIRMFO/MD,FT-CLEAN-UP ;8/9/96 09:30

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP0 ;HIRMFO/RM-NURSING CARE PLAN PATIENT EDIT ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP1 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT part 1 ;1/13/92

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP2 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT part 2 ;4/29/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP3 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT part 3 ;1/11/92

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP4 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT part 4 ;4/29/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP5 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT Part 1 ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP6 ;HIRMFO/JH-NURSING CARE PLAN DATA OUTPUT Part 2 ;9/18/89

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP7 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT Part 3 ;4/29/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP8 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT - PRINT ;4/29/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPP9 ;HIRMFO/JH/RM-NURSING CARE PLAN DATA OUTPUT Part 1 ;1/13/92

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPPS1 ;HIRMFO/RM,RK-NURSING CARE PLAN REPORT USING GENERIC SORT ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPPS2 ;HIRMFO/JH/RM-NURSING CARE PLAN DATABASE SEARCH part 2 ;4/17/92

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPPS3 ;HIRMFO/JH,RM-NURSING CARE PLAN DATABASE SEARCH part 3 ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCPPS4 ;HIRMFO/RM-NURSING CARE PLAN SEARCH Part 2 ;3/03/89

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCRL0 ;HIRMFO/RM,RTK-CARE PLAN RANK ORDER PRINT ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCRL1 ;HIRMFO/RM,RTK-RANK ORDER PRINT (CONT.) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCRL2 ;HIRMFO/RM-PT. CENSUS FOR CARE PLANS ;9/10/91

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCRL3 ;HIRMFO/RM-SELECT MULTIPLE NURSING LOCATION UTILITY ;9/11/91

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCRL4 ;HIRMFO/RM-CARE PLAN RANK ORDER PRINT (cont.) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCROP0 ;HIRMFO/RM,RTK-CARE PLAN RANK ORDER PRINT ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCROP1 ;HIRMFO/RM,RTK-RANK ORDER PRINT (CONT.) ;8/29/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURCROP2 ;HIRMFO/RM-CARE PLAN RANK ORDER PRINT ;12/23/93

;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCUT0 ;HIRMFO/MD,RM,FT-PATIENT SELECTION UTILITY BY WARD, ROOM OR SINGLE PATIENT ;9/16/96 14:06

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCUT1 ;HIRMFO/RM-UTILITIES FOR CLINICAL NURSING ;APR 4, 1994

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCVED0 ;HIRMFO/YH,MD,RM,FT-VITAL SIGNS EDIT SHORT FORM ;9/16/96 14:26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCVED1 ;HIRMFO/YH-LIST & SELECT VITAL MEASUREMENTS ;9/27/90

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCVED2 ;HIRMFO/MD,YH-VITAL SIGNS EDIT SHORT FORM ;11/27/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCVPR0 ;HIRMFO/YH,FT-VITALS/MEASUREMENTS RESULTS REPORTING ;9/16/96 14:27

> ;;4.0;NURSING SERVICE;;Mar 31, 1997;

> NURCVPR1 ;HIRMFO/YH-PATIENT VITALS/MEASUREMENTS REPORT UTILITY ;11/21/94

> NURCVUT0 ;HIRMFO/YH,RM,FT-PATIENT SELECTION UTILITY BY WARD, ROOM OR SINGLE PATIENT ;9/16/96 14:30

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCYED0 ;HIRMFO/YH,FT-PATIENT INTAKE/OUTPUT ENTER/EDIT ;9/16/96 14:31

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURCYRP0 ;HIRMFO/YH-PATIENT INTAKE/OUTPUT REPORTS ;2/25/91

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQEDT0 ;HIRMFO/MH,RM,YH-EDIT NURQ QI SUMMARY FILE, 217 ;1/22/97 15:30

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQEDT1 ;HIRMFO/MH,RM,YH-EDIT QI SUMMARY (#217) FILE ;1/22/97 15:28

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURQKILL ;HIRMFO/MD-CLEAN-UP ;11/23/94 12:32

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQRPT0 ;HIRMFO/RM,YH-ROUTINE TO PRINT 10 STEP REPORT ;1/22/97 15:28

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURQRPT1 ;HIRMFO/YH-QI SUMMARY REPORT, PART 2 ;4/22/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQRPT2 ;HIRMFO/YH-ROUTINE TO PRINT 10 STEP REPORT, PART 3 ;3/28/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQRPT3 ;HIRMFO/YH-ROUTINE TO PRINT 10 STEP REPORT, PART 4 ;3/21/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURQRPT4 ;HIRMFO/YH-ROUTINE TO PRINT 10 STEP REPORT, PART 5 ;5/13/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURQUTL ;HIRMFO/RM-QI SUMMARY UTILITIES ;4/24/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURQUTL1 ;HIRMFO/RM-QI SUMMARY UTILITIES ;1/22/97 15:26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURQUTL2 ;HIRMFO/YH-SURVEY STATISTICS PART 2 ;3/11/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURQUTL3 ;HIRMFO/RM,YH-SURVEY STATISTICS PART 1 ;4/22/96

;;4.0;NURSING SERVICE;;Mar 31, 1997

NURS ;HIRMFO/RM-ROUTINE TO CHECK FOR VERSION NUMBER, AND RUN NURSING MENU

> ;86/8/26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSACE0 ;HIRMFO/RM-PT. CENSUS FOR CARE PLANS ;6/24/92

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSACEN ;HIRMFO/RM,FT-PATIENT CENSUS CALCULATION ;4/30/96 15:42

> ;;4.0;NURSING SERVICE;;Mar 31, 1997;

> NURSADEL ;CISC/MD/MH-PURGE ROUTINE FOR FILES 214.6 - 214.7 ;12/07/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAFLL ;HIRMFO/RM,MD,FT-LOOKUP FOR FILE 211.4 ;10/10/96 13:03

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSAFU0 ;HIRMFO/RM,FT-SITE FILES Continued ;6/11/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSAFUD ;HIRMFO/RM,MD-SITE FILES UPDATE ;1/24/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAGP0 ;HIRMFO/MD,RM-GENERIC PROMPTS FOR ADMIN/EDUCATION REPORTS ;10/05/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAGP1 ;HIRMFO/MD,RM,FT-ADMINISTRATION/EDUCATION REPORT PROMPTS CONTINUED

> ;8/13/96 14:11

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAGP2 ;HIRMFO/MD-ADMINISTRATION/EDUCATION REPORT PROMPTS CONTINUED ;NOV 87

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAGP3 ;HISC/MD-MULTIPLE SERVICE CATEGORY SELECTION UTILITY

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAGS0 ;HIRMFO/RM,MD-SELECT MULTIPLE NURSING LOCATION UTILITY ;11/18/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSAGSP ;HIRMFO/MD-GENERIC SORT BY PROMPTS ;7/11/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAL0 ;HIRMFO/JM-DRIVER FOR EDIT,PRINT OPTIONS FOR THE LOCATION REASSIGNMENT OPTION NURSLO-MENU ;8/23/96 10:51

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSALE0 ;HIRMFO/RM-LOCATION FILE EDIT ROUTINE ;11/4/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSALED ;HIRMFO/RM,FT-LOCATION FILE EDIT ROUTINE ;6/11/89

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAMSG ;HIRMFO/RM,FPT-QUEUED MESSAGES TO THE CENT. NURS. OFFICE ;6/18/96 16:27

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAPCH ;HIRMFO/JH,RM,FT-CHECKS FOR PATIENTS ON ABSENCE ;4/30/96 16:37

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAPE0 ;HIRMFO/RM/JH-POSITION CONTROL/EXPERIENCE UTILITY ;5/1/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAPFU ;HIRMFO/RM/MD,FT-SITE PARAMETER FILE UPDATE ;4/18/96 15:14

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAUTL ;HIRMFO/MD/JH-SECURITY ROUTINE FOR THE NURSING ADMIN REPORTS ;9/7/90 12:59

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAWCK ;HIRMFO/RM-CHECK SO EVERY MAS WARD HAS A NURSING LOCATION ;AUGUST 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAWL0 ;HIRMFO/RM,FT-WORK LOAD STATISTICS ;8/9/96 11:53

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSAWL3 ;HIRMFO/MD,FT-WORK LOAD STATISTICS CONT OF NURSAWL0 ;8/9/96 11:54

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSBPO ;HIRMFO/MD-NURS POSITION CONTROL FILE BUDGETED FTEE EDIT ;JUN 90

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCEP ;HIRMFO/JH/MH/MD-LIST/REPAIR STAFF DISCREPANCIES BETWEEN FILES 210 & 211.8 ;9/19/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCEP1 ;HIRMFO/JH/MH-LIST/REPAIR STAFF DISCREPANCIES - CONT. ;3/23/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCPL ;HISC/RM-ADMISSION MODULE TO ADMIT PATIENT TO NURSING ;4/10/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCPLC ;HIRMFO/RM,FT-PATIENT CENSUS...WARD,INDIVIDUAL, AND HOSPITAL

> ;8/14/96 10:16

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCPLD ;HIRMFO/RM-DISCHARGE MODULE TO DISCHARGE PATIENT FROM NURSING

> ;SEPTEMBER 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCPLE ;HIRMFO/RM,FT-BACKUP BED CONTROL FOR NURSING SERVICE ;8/14/96 14:06

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCPLU ;HIRMFO/RM,FT-Create NURSING FILE AND XREFS ;8/14/96 10:22

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSCUTL ;HIRMFO/MD-RM-UTILITY ROUTINE FOR NURSING CLINICAL ;6/6/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997;

> NURSDD ;HIRMFO/RM-THIS ROUTINE PRINTS OUT DD'S FOR NURSING FILES ;12/30/87

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSDFFS ;HIRMFO/RM-FILE FIELD STRUCTURES FOR NURSING FILES ;AUGUST 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSDLOF ;HIRMFO/RM-ROUTINE TO PRINT OFF LIST OF FILES ;AUGUST 1986

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSDTMP ;HIRMFO/RM/MD-ROUTINE TO OUTPUT TEMPLATE LISTING FOR NURSING FILES

> ;12/30/87

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEP31 ;HIRMFO/JH,FT-NURSING MANDATORY INSERVICE CLASS DATA FOR THE LAST THREE YEARS ;8/9/96 12:04

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEP3I ;HIRMFO/GLB-INDIVIDUAL NURSING MANDATORY INSERVICE CLASS DATA FOR THE LAST THREE YEARS ;4/4/89 13:57

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPC0 ;HIRMFO/PC,FT-C.E.PROGRAM ATTENDANCE SUMMARY,PRINT CON'T 4/10/87

> ;8/9/96 12:52

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPC1 ;HIRMFO/MD,FT-AA/FUNDING REQUEST,PRINT (132 COLUMN REPORT) CON'T

> ;8/9/96 12:06

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPCA ;HIRMFO/PC,FT-AA/FUNDING REQUEST,PRINT (132 COLUMN REPORT) ;5/7/96 15:08

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPCP ;HIRMFO/MD,FT-C.E.PROGRAM ATTENDANCE SUMMARY,PRINT ;8/12/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPD0 ;HIRMFO/JH,RM-INDIVIDUAL M I DEFICIENCY BY EMPLOYEE NAME ;10/13/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPD1 ;HIRMFO/GLB-INCOMPLETE NURSING MANDATORY INSERVICE CLASS DATA PART 2 OF 2 ;4/19/89 09:37

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPD2 ;HIRMFO/JH,RM-INCOMPLETE NURS M I REPORT (BY CLASS) PART 1 OF 2

> ;10/13/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPD3 ;HIRMFO/MD-INCOMPLETE NURS M I REPORT (BY CLASS) PART 1 OF 2

> ;7/15/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPIN ;HIRMFO/MD-INDIVIDUAL INSERVICE RECORD PRINT ;1/5/89 16:10

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPL1 ;HIRMFO/MD,FT-TRAINING REPORT BY LOCATION ;8/9/96 12:14

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEPML ;HIRMFO/MD,FT-TRAINING REPORT BY LOCATION ;8/9/96 09:39

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSEXP ;HIRMFO/JH,MD,FT-CHECK AND CLEAN EXPERIENCE SUB-FILE IN FILE 210

> ;5/3/96 13:30

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSFILE ;HIRMFO/FT-Set Nursing File Security ;3/5/97 16:41

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSFMU ;HIRMFO/RM-NURSING FILEMAN ROUTINE ;10/05/95

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSHIGH ;HIRMFO/JH-LIST STAFF HIGHEST DEGREES ;4/21/94

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSKIL1 ;HIRMFO/MD-CLEAN-UP ;1/15/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSKILL ;HIRMFO/MD,FT-CLEAN-UP ;8/14/96 10:35

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSUT0 ;HIRMFO/MD,RM,FT-NURS STAFF FILE EDIT UTILITY ;8/8/96 09:36

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSUT1 ;HIRMFO/RM,MD-NURS POSITION CONTROL FILE EDIT UTILITY (CONT)

> ;2/26/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSUT2 ;HIRMFO/MD,RM,FT-UTILITIES FOR FILES 210 AND 211.8 ;01/06/97

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSUT3 ;HIRMFO/RM,MD-UTILITIES FOR FILES 210 AND 211.8 ;5/7/96

> ;;4.0;NURSING SERVICE;;Mar 31, 1997 NURSUT4 ;HIRMFO/RM-UTILITIES FOR FILE 213.9 ;5/17/93

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURSXECP ;HIRMFO/MD-NURSING DATA EXCEPTION REPORT ;AUG 93

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURXENV ;HIRMFO/FT-Environment Check for Nursing v4.0 ;1/21/97 14:26

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURXPRE ;HIRMFO/FT-Nursing Service v4.0 Pre-initialization routine ;1/21/97 14:58

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

> NURXPST ;HIRMFO/FT-Nursing Service v4.0 Post-Initialization Routine ;1/21/97 14:27

> ;;4.0;NURSING SERVICE;;Mar 31, 1997

# Chapter 3 File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Nursing File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NURS STAFF 210

> The Nursing Staff file contains information on nursing employees. Data includes staff demographics, title/position(s) held, FTEE, assignment locations, primary tour of duty, nursing grade/step code, salary, license information, emergency contact, dates employed, promotion date, Nursing Professional Standards Board/proficiency due dates, professional education, highest nursing and/or academic degree, faculty appointments, certification information, military experience, MI review group information, and medical center privileges.

> NURS PAY SCALE 211.1

> This file contains a list of nursing grade/step codes and their associated GS or Title 38 grade/step levels.

> \*NURS GRADE/STEP 211.2

> This file lists names of specific GS and Title 38 grade/step levels and their related salary.

> NURS SERVICE POSITION 211.3

> This file contains information on nursing 'service positions' and their related data (i.e., priority sequence numbers, AMIS position, service category).

> NURS LOCATION 211.4

> This file contains nursing information on all patient care areas and office locations specific to Nursing Service.

> NURS CLINICAL BACKGROUND 211.5

> This file lists areas of professional experience applicable to nursing employees.

> NURS TOUR OF DUTY 211.6

> This file contains a list of official tours of duty specific to Nursing Service.

> NURS AMIS POSITION 211.7

> This file contains nursing positions and associated field numbers as displayed on VA Form 10- 1106b (AMIS).

> NURS POSITION CONTROL 211.8

> This file tracks budgeted position within a service.

> NURS VACANCY/TRANSFERRED REASONS 211.9

> This file indicates reasons for position vacancies/transfers.

> NURS EDUCATION 212.1

> This file contains information which is used in determining the highest academic and/or nursing degree of nursing employees.

> NURS CERTIFICATION 212.2

> This file contains a list of nursing certifications and the related certifying organization/agency.

> NURS COLLEGE MAJOR 212.3

> This file contains a list of college majors.

> \*NURS MANDATORY INSERVICE 212.4

> Contains the titles of in-services which are considered mandatory by nursing. The file is pointed to by the NURS STAFF FILE (#210).

> \*NURS MI CLASS GROUP 212.42

> These are groupings of nursing mandatory in-services.

> NURS PRIVILEGE 212.6

> This file contains clinical privileges that may be assigned to nursing employees.

> NURS PRODUCT LINE 212.7

> This file contains a list of services/programs/product lines that are being tracked by Nursing.

> \*NURS AMIS 1106 CLASS 213.1

> This file contains patient acuity data specific to Nursing Service.

> NURS AMIS 1106B FTEE 213.2

> This file contains comparison FTEE data for Nursing (i.e., total budgeted/ceiling FTEE vs. actual FTEE).

> NURS AMIS WARD 213.3

> This file contains names of official nursing bed sections.

> NURS AMIS 1106 MANHOURS 213.4

> This file contains the AMIS 1106 Manhours data for the Nursing Service.

> NURS AMIS DAILY EXCEPTION REPORT 213.5

> This file holds the exception data for unclassified patients for the AMIS Acuity run. Data will be stored for thirty days before it is purged.

> NURS PARAMETERS 213.9

> This file contains various Nursing application site parameters.

> File List and Related Information

> NURS PATIENT 214

> This file contains the current nursing location, and nursing bed section, and selected admission information for a patient.

> NURS CLASSIFICATION 214.6

> This file contains classification information in a flat file format.

> NURS REVIEW CLASSIFICATION 214.7

> This file contains an audit of classification reviews in a flat file format.

> NURS BEDSIDE TERMINAL FILE 214.8

> This file links a specific patient to the bed-side terminal at their current room-bed location. This file is used for point of care only.

> NOTE: This file was developed as a Class III file and was never exported nationally.

> NURS CARE PLAN 216.8

> Data pertaining to the Patient Plan of Care for a particular patient.

> NURQ QI SUMMARY 217

> This file contains data relating to surveys, such as survey name, related indicators (questions) from the survey, key functions, data collection information, and possible actions to be taken. These records are used for tracking and reporting any indicators, including chart audits and discharge audits.

> NURQ STANDARDS OF CARE/PRACTICE 217.1

> This file contains a list of the facility's standards of care/practice.

> NURQ RATIONALE 217.2

> This file contains all of the rationale data used in the QI Summary reports.

> NURQ FREQUENCY 217.3

> This file contains frequency data used in editing the QI Summary records.

> \*NURS CONVERSION NAME CHANGE 219.7

> This file contains a mapping of option, routine, help frame, and bulletin names from the Nursing package prior to Version 2.5 to the Nursing package Version 2.5.

## Nursing Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 30%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE #</p>
</blockquote></th>
<th>NAME</th>
<th></th>
<th><blockquote>
<p>UP DATE DD</p>
</blockquote></th>
<th><blockquote>
<p>SEND SEC. CODE</p>
</blockquote></th>
<th><blockquote>
<p>DATA COMES W/FILE</p>
</blockquote></th>
<th><blockquote>
<p>SITE DATA</p>
</blockquote></th>
<th><blockquote>
<p>RSLV PTS</p>
</blockquote></th>
<th><blockquote>
<p>USER OVER RIDE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>210</p>
</blockquote></td>
<td>NURS</td>
<td><blockquote>
<p>STAFF</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.1</p>
</blockquote></td>
<td>NURS</td>
<td><blockquote>
<p>PAY SCALE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>211.2 *NURS GRADE/STEP</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>211.3 NURS SERVICE POSITION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>211.4 NURS LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>211.5 NURS CLINICAL BACKGROUND</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>211.6 NURS TOUR OF DUTY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>211.7 NURS AMIS POSITION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>211.8 NURS POSITION CONTROL</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>211.9 NURS VACANCY/TRANSFERRED</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>212.1 NURS EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>212.2 NURS CERTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>212.3 NURS COLLEGE MAJOR</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>212.4 *NURS MANDATORY INSERVICE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>212.42 *NURS MI CLASS GROUP</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>212.6 NURS PRIVILEGE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>212.7 NURS PRODUCT LINE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>213.1 *NURS AMIS 1106 CLASS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>213.2 NURS AMIS 1106B FTEE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>213.3 NURS AMIS WARD</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>213.4 NURS AMIS 1106 MANHOURS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>213.5 NURS AMIS DAILY EXCEPTION RE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>213.9 NURS PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>214 NURS PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>214.6 NURS CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>214.7 NURS REVIEW CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>216.8 NURS CARE PLAN</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>217 NURQ QI SUMMARY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>217.1 NURQ STANDARDS OF CARE/PRACT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>217.2 NURQ RATIONALE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>217.3 NURQ FREQUENCY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>219.7 *NURS CONVERSION NAME CHANGE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Chapter 4 Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Options by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: NURAAM-ACU

> MENU TEXT: Nursing Acuity/Separation-Activation Run

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option compiles the Patient Category Totals-AMIS 1106, the Patient Category Totals-Midnight Acuity, and the Employee Activation/Separation Reports.

> ROUTINE: EN1^NURAAU0 SCHEDULING RECOMMENDED: YES UPPERCASE MENU TEXT: NURSING ACUITY/SEPARATION-ACTI

> NAME: NURAAM-ACUEDT MENU TEXT: AMIS 1106 Acuity Edit

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option permits editing of the patient acuity data stored in NURS AMIS 1106 MANHOURS FILE (#213.4).

> ROUTINE: NURAAE0

> UPPERCASE MENU TEXT: AMIS 1106 ACUITY EDIT

> NAME: NURAAM-ACUMAN

> MENU TEXT: Manual Nursing Acuity/Separation Run

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Compiles the Patient Category Totals-AMIS 1106, Patient Category Totals- Midnight Acuity, and Employee Activation/Separation Reports when TaskMan is down. This option is a back-up for NURAAM-ACU.

> ROUTINE: NURAAU2 \*RESCHEDULING FREQUENCY: 1D UPPERCASE MENU TEXT: MANUAL NURSING ACUITY/SEPARATI

> NAME: NURAAM-MD-UNC

> MENU TEXT: Unclassified Midnight Patients

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: This option prints a daily listing of patients not classified by midnight. Data can be retrieved for the last 30 days.

> ENTRY ACTION: S NURTYPE=1 ROUTINE: EN2^NURAAU2 UPPERCASE MENU TEXT: UNCLASSIFIED MIDNIGHT PATIENTS

> NAME: NURAAM-MD-UNCBAT

> MENU TEXT: Batch Run of Unclassified Midnight Patients TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: This is an optional report, that the site may or may not wish to queue to run. This option should be queued at least 2 hours after the queuing of the NURAAM-ACU option. This option will print out the unclassified patients not counted by the NURAAM-ACU.

> ENTRY ACTION: S NURTYPE=1 ROUTINE: EN3^NURAAU2 UPPERCASE MENU TEXT: BATCH RUN OF UNCLASSIFIED MIDN

> NAME: NURAAM-UNC

> MENU TEXT: Unclassified AMIS 1106 Patients

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: This option prints a daily listing of patients not classified by 3 pm. Data can be retrieved for the last 30 days.

> ENTRY ACTION: S NURTYPE=0 ROUTINE: EN2^NURAAU2

> UPPERCASE MENU TEXT: UNCLASSIFIED AMIS 1106 PATIENT NAME: NURAAM-UNCBAT

> MENU TEXT: Batch Run of Unclassified AMIS 1106 Patients TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: This is an optional report, that the site may or may not wish to queue to run. This option should be queued at least 2 hours after the queuing of the NURAAM-ACU option. This option will print out the unclassified patients not counted by the NURAAM-ACU option.

> ENTRY ACTION: S NURTYPE=0 ROUTINE: EN3^NURAAU2 UPPERCASE MENU TEXT: BATCH RUN OF UNCLASSIFIED AMIS

> NAME: NURAED-BATSEP

> MENU TEXT: Employee Activation/Separation Report

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints an employee activation/separation report on demand or when queued by a user.

> ROUTINE: NURAFSD \*RESCHEDULING FREQUENCY: 1D UPPERCASE MENU TEXT: EMPLOYEE ACTIVATION/SEPARATION

> NAME: NURAED-BATSEP-QUEUE

> MENU TEXT: TaskManager Activation/Separation Report

> TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: This option is used to queue the activation/separation report to print daily at a time designated by the user. This option should be queued at least 2 hours after queuing of the NURAAM-ACU option.

> ENTRY ACTION: I \$D(ZTSK) S (NUROUT,NQSW,NURMDSW)=0,X="T-1" D ^%DT S NURSDATE=\$ S(+Y:Y,1:"") D EN9^NURSAGSP S:NURMDSW NURFAC=1 D:+NURSDATE START^NURAFSD

> SCHEDULING RECOMMENDED: YES

> UPPERCASE MENU TEXT: TASKMANAGER ACTIVATION/SEPARAT

> NAME: NURAED-MENU

> MENU TEXT: Administration Records, Enter/Edit

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A primary menu displaying options which edit administration data.

> ITEM: NURAED-STF-MENU ITEM: NURAED-STF-LOC ITEM: NURAMN-MANED

> TIMESTAMP: 56838,47812

> UPPERCASE MENU TEXT: ADMINISTRATION RECORDS, ENTER/

> NAME: NURAED-STF-ALL MENU TEXT: Edit All Employee Data TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit all of employee's data. ROUTINE: EN13^NURAED0

> UPPERCASE MENU TEXT: EDIT ALL EMPLOYEE DATA

> NAME: NURAED-STF-CERT MENU TEXT: National Certification TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's national certification data. ROUTINE: EN9^NURAED0

> UPPERCASE MENU TEXT: NATIONAL CERTIFICATION

> NAME: NURAED-STF-DEMO MENU TEXT: Demographic Data

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's demographic data (e.g., name, address, SSN, phone).

> ROUTINE: EN1^NURAED0 UPPERCASE MENU TEXT: DEMOGRAPHIC DATA

> NAME: NURAED-STF-EDUC MENU TEXT: Professional Education TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's professional education data. ROUTINE: EN7^NURAED0

> UPPERCASE MENU TEXT: PROFESSIONAL EDUCATION

> NAME: NURAED-STF-EXP MENU TEXT: Professional Experience TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's professional experience data. ROUTINE: EN8^NURAED0

> UPPERCASE MENU TEXT: PROFESSIONAL EXPERIENCE

> NAME: NURAED-STF-LIC MENU TEXT: License

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's licensing data.

> ROUTINE: EN4^NURAED0 UPPERCASE MENU TEXT: LICENSE

> NAME: NURAED-STF-LOC MENU TEXT: Location Edit, Employee TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Allows editing of location field in the NURS STAFF FILE (#210). ENTRY ACTION: D EN14^NURAED0 S NUROUT=\$S('\$D(XQUIT):0,XQUIT=1:1,1:0) D:'NUROUT

> ^NURAED1 S:'\$D(NURAES) NUROUT=1 W:'NUROUT ! S:'NUROUT DIE="^NURSF(210",DR=28.1, DA=+NURSDBA D:'NUROUT ^DIE D EN15^NURAED0 K NUROUT

> UPPERCASE MENU TEXT: LOCATION EDIT, EMPLOYEE

> NAME: NURAED-STF-MENU MENU TEXT: Staff Record Edit TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: Allows entry of demographic and other professional data into individual Nursing Service records. Data is used for VACO and hospital nursing reports.

> ITEM: NURAED-STF-DEMO SYNONYM: 1

> ITEM: NURAED-STF-PER SYNONYM: 2

> ITEM: NURAED-STF-STAT/POS SYNONYM: 3

> ITEM: NURAED-STF-LIC SYNONYM: 4

> ITEM: NURAED-STF-PROB SYNONYM: 5

> ITEM: NURAED-STF-NPSB SYNONYM: 6

> ITEM: NURAED-STF-EDUC SYNONYM: 7

> ITEM: NURAED-STF-EXP SYNONYM: 8

> ITEM: NURAED-STF-CERT SYNONYM: 9

> ITEM: NURAED-STF-MIL SYNONYM: 10

> ITEM: NURAED-STF-ALL SYNONYM: ALL

> EXIT ACTION: D EN15^NURAED0 ENTRY ACTION: D EN14^NURAED0 TIMESTAMP: 56830,56534 UPPERCASE MENU TEXT: STAFF RECORD EDIT

> NAME: NURAED-STF-MIL MENU TEXT: Military Status

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's previous military experience data.

> ROUTINE: EN10^NURAED0 UPPERCASE MENU TEXT: MILITARY STATUS

> NAME: NURAED-STF-NPSB MENU TEXT: Annual Review/NPSB

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's Nurse Professional Standards Board review data. ROUTINE: EN6^NURAED0 UPPERCASE MENU TEXT: ANNUAL REVIEW/NPSB

> NAME: NURAED-STF-PER MENU TEXT: Personnel Data

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's personnel data (e.g., VA start date, computation date).

> ROUTINE: EN2^NURAED0 UPPERCASE MENU TEXT: PERSONNEL DATA

> NAME: NURAED-STF-PROB MENU TEXT: Probationary Period/Promotion TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's data regarding probations or promotions. ROUTINE: EN5^NURAED0

> UPPERCASE MENU TEXT: PROBATIONARY PERIOD/PROMOTION

> NAME: NURAED-STF-STAT/POS MENU TEXT: Status and Position TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Edit employee's status and position.

> ROUTINE: EN3^NURAED0 UPPERCASE MENU TEXT: STATUS AND POSITION

> NAME: NURAED-TSK-BAT/SEP

> MENU TEXT: Task Manager Activation/Separation Report TYPE: action CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the option that should be tasked for the Staff Activation/Separation report to be printed daily via Task Manager.

> SCHEDULING RECOMMENDED: YES

> UPPERCASE MENU TEXT: TASK MANAGER ACTIVATION/SEPERA

> NAME: NURAFL-BFU

> MENU TEXT: FTEE Service Budget (1106b) File, Edit

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Permits entry of data on budgeted/ceiling FTEE for the service. This information will be used to generate the AMIS 1106b Report and must be updated.

> ROUTINE: NURARFBU

> UPPERCASE MENU TEXT: FTEE SERVICE BUDGET (1106B) FI

> NAME: NURAFL-CERT MENU TEXT: Certification File, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Permits a service to enter and modify the NURS CERTIFICATION FILE (#212.2).

> ROUTINE: EN5^NURSAFUD

> UPPERCASE MENU TEXT: CERTIFICATION FILE, EDIT

> NAME: NURAFL-CLBK

> MENU TEXT: Clinical Background File, Edit

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a service to enter and modify data in the NURS CLINICAL BACKGROUND FILE (#211.5). This file contains areas of professional practice in which RNs might be employed. The file is not limited to entries pertaining to

> clinical experience but can also contain data relevant to administration, education, data processing, etc.

> ROUTINE: EN6^NURSAFUD

> UPPERCASE MENU TEXT: CLINICAL BACKGROUND FILE, EDIT

> NAME: NURAFL-GS-COD MENU TEXT: Load Grade/Step Codes TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Permits the service to enter and modify the NURS PAY SCALE FILE (#211.1).

> ROUTINE: EN7^NURSAFUD

> UPPERCASE MENU TEXT: LOAD GRADE/STEP CODES

> NAME: NURAFL-PROD-LINE MENU TEXT: Product Line File Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to enter/edit entries in the NURS PRODUCT LINE file (#212.7).

> ROUTINE: EN6^NURSAFU0

> UPPERCASE MENU TEXT: PRODUCT LINE FILE EDIT

> NAME: NURAFL-SPO MENU TEXT: Service Position File, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows the service to enter and modify data in the NURS SERVICE POSITION FILE (#211.3).

> ROUTINE: EN3^NURSAFU0

> UPPERCASE MENU TEXT: SERVICE POSITION FILE, EDIT

> NAME: NURAFL-TOD MENU TEXT: Tour of Duty File, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows the service to enter and modify data in the NURS TOUR OF DUTY FILE (#211.6).

> ROUTINE: EN4^NURSAFU0

> UPPERCASE MENU TEXT: TOUR OF DUTY FILE, EDIT

> NAME: NURAFL-VAC MENU TEXT: Vacancy Reason File Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option provides edit capability for the NURS VACANCY/TRANSFERRED REASONS FILE (#211.9). New entries may also be added via this option.

> ROUTINE: EN5^NURSAFU0

> UPPERCASE MENU TEXT: VACANCY REASON FILE EDIT

> NAME: NURAMN-MANCK

> MENU TEXT: Nursing Batch Job Status Check

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option checks the status of the manhours, and NURSING Package batch jobs to see if they completed. If these jobs do not run to completion on a specific date or shift, a mail bulletin is sent to the

> NURS-ADP mail group. This job should be queued to run at least 2 hours after the NURAAM-ACU option runs and run with a rescheduling frequency of 1D.

> ROUTINE: EN1^NURAMB3 TIMESTAMP: 55433,49847 UPPERCASE MENU TEXT: NURSING BATCH JOB STATUS CHECK

> NAME: NURAMN-MANED MENU TEXT: Manhours Edit, AMIS 1106a

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows a nurse to enter daily RN, LPN, and NA manhours for the purpose of generating the AMIS 1106a Report.

> ROUTINE: EN1^NURAMHE

> UPPERCASE MENU TEXT: MANHOURS EDIT, AMIS 1106A

> NAME: NURAMN-STA

> MENU TEXT: Manhours Exception Print by Service

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option provides a report of all wards by shift that have no manhours data entered, for a specific date or date range, by service.

> ROUTINE: EN2^NURAMH9

> UPPERCASE MENU TEXT: MANHOURS EXCEPTION PRINT BY SE

> NAME: NURAMN-STA-LOC

> MENU TEXT: Manhours Exception Print by Location

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option provides a report, by user selected location, of dates and shifts which have no manhours data.

> ROUTINE: EN1^NURAMH9

> UPPERCASE MENU TEXT: MANHOURS EXCEPTION PRINT BY LO

> NAME: NURAPC-HEM

> MENU TEXT: Hemodialysis Patients, Classify/Count

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a R.N. to enter a patient's dialysis treatment into the AMIS count.

> ROUTINE: EN1^NURACHDC TIMESTAMP: 55448,31048 UPPERCASE MENU TEXT: HEMODIALYSIS PATIENTS, CLASSIF

> NAME: NURAPC-INDPT

> MENU TEXT: Classify Patients Individually

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a R.N. to classify patients individually. ROUTINE: EN1^NURACE0

> UPPERCASE MENU TEXT: CLASSIFY PATIENTS INDIVIDUALLY

> NAME: NURAPC-MENU MENU TEXT: Classification, Edit Patient TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: A menu displaying options for editing patient classification. ITEM: NURAPC-UNCWRD SYNONYM: 5

> ITEM: NURAPC-INDPT SYNONYM: 1

> ITEM: NURAPC-WRD SYNONYM: 2

> ITEM: NURAPC-HEM SYNONYM: 3

> ITEM: NURAPC-RECRM SYNONYM: 4

> TIMESTAMP: 56830,56534 TIMESTAMP OF PRIMARY MENU: 54075,47487 UPPERCASE MENU TEXT: CLASSIFICATION, EDIT PATIENT

> NAME: NURAPC-RECRM

> MENU TEXT: Recovery Room Patients, Classify/Count

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a R.N. to enter the number of patients present in the recovery room at midnight into the AMIS count.

> ROUTINE: EN2^NURACHDC

> UPPERCASE MENU TEXT: RECOVERY ROOM PATIENTS, CLASSI

> NAME: NURAPC-REVIND

> MENU TEXT: Individual Patient, Review/Edit

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a supervisory/QA R.N. to review the classification of patients on a given day; reclassification of an individual patient is also permitted.

> ROUTINE: EN2^NURACE0

> UPPERCASE MENU TEXT: INDIVIDUAL PATIENT, REVIEW/EDI

> NAME: NURAPC-REVWRD

> MENU TEXT: Ward, Review/Edit Classifications By

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows a supervisory/QA RN to review the classification of patients on a given day by ward. Reclassification of an individual patient is also permitted.

> ROUTINE: EN2^NURACEW

> UPPERCASE MENU TEXT: WARD, REVIEW/EDIT CLASSIFICATI

> NAME: NURAPC-UNCWRD MENU TEXT: Unclassified Patients, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Allows the R.N. to classify all unclassified patients residing on a specific ward on a given day.

> ROUTINE: EN2^NURACEW0

> UPPERCASE MENU TEXT: UNCLASSIFIED PATIENTS, EDIT

> NAME: NURAPC-WRD MENU TEXT: Classify Patients by Ward TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the editing of patient classifications by ward.

> ROUTINE: EN1^NURACEW

> UPPERCASE MENU TEXT: CLASSIFY PATIENTS BY WARD

> NAME: NURAPP-UNCLOC

> MENU TEXT: Current Unclassified Patient Print, by Location TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Prints a report of all unclassified patients on a specific ward for the current day.

> ROUTINE: EN1^NURACEW0

> UPPERCASE MENU TEXT: CURRENT UNCLASSIFIED PATIENT P

> NAME: NURAPP-WRDCLAS MENU TEXT: Classification Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Reports which list by ward current patient classifications. ROUTINE: NURARCRW

> UPPERCASE MENU TEXT: CLASSIFICATION REPORT

> NAME: NURAPR-ADGREE MENU TEXT: Academic Degree Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports summarizing the highest academic degree held by nursing personnel. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=1 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: ACADEMIC DEGREE REPORTS

> NAME: NURAPR-AGE MENU TEXT: Age Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports which provide a count of nursing personnel within specified age groups (age 18 and older). Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=2 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: AGE REPORTS

> NAME: NURAPR-CDGREE

> MENU TEXT: Comb. Acad./Nurs. Degree Reports

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints a combined academic and nursing report by location, service, or individual.

> Short Menu Text: COMB. ACAD./NURS. REPORTS ROUTINE: NURADEG

> UPPERCASE MENU TEXT: COMB. ACAD./NURS. DEGREE REPOR

> NAME: NURAPR-CERTF MENU TEXT: Certification Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports reflecting the national certifications held by registered nurses, the agency granting the certification, and the date of its expiration. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=3 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: CERTIFICATION REPORTS

> NAME: NURAPR-FTEE MENU TEXT: FTEE Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Statistical location and service reports which summarize FTEE. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=4 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: FTEE REPORTS

> NAME: NURAPR-GENDER MENU TEXT: Gender Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports which provide a count of employees by gender. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=5 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: GENDER REPORTS

> NAME: NURAPR-GRADE MENU TEXT: Grade Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports which summarize the number of employees within all grade levels. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=6 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: GRADE REPORTS

> NAME: NURAPR-HNMEN

> MENU TEXT: Administration Reports (Head Nurse)

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option is for printing all the head nurse reports. ITEM: NURAPR-RES SYNONYM: 4

> ITEM: NURAPR-PHONE SYNONYM: 2

> ITEM: NURAPR-STF SYNONYM: 3

> ITEM: NURAPR-LOC-SER SYNONYM: 1 TIMESTAMP: 56656,39480

> UPPERCASE MENU TEXT: ADMINISTRATION REPORTS (HEAD N

> NAME: NURAPR-LICENSE MENU TEXT: License Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports which summarize information on state licenses held by RNs, and LPNs/LVNs. Data includes employee name, social security number, expiration date of license, state issuing license, and professional license number.

> ENTRY ACTION: S ANS1=7 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: LICENSE REPORTS

> NAME: NURAPR-LOC-SER MENU TEXT: Administrative Reports TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints the administration location and service reports.

> ITEM: NURAPR-ADGREE SYNONYM: 1

> ITEM: NURAPR-AGE SYNONYM: 2

> ITEM: NURAPR-CERTF SYNONYM: 3

> ITEM: NURAPR-GENDER SYNONYM: 4

> ITEM: NURAPR-GRADE SYNONYM: 5

> ITEM: NURAPR-LICENSE SYNONYM: 6

> ITEM: NURAPR-MILITARY SYNONYM: 7

> ITEM: NURAPR-NPSB SYNONYM: 8

> ITEM: NURAPR-NDGREE SYNONYM: 9

> ITEM: NURAPR-PROF SYNONYM: 10

> ITEM: NURAPR-CDGREE SYNONYM: 11

> ROUTINE: EN^NURADMIN TIMESTAMP: 56830,56534 UPPERCASE MENU TEXT: ADMINISTRATIVE REPORTS

> NAME: NURAPR-MENU MENU TEXT: Administration Records, Print TYPE: menu CREATOR: POSTMASTER

> DISPLAY OPTION?: NO PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the primary menu option for all the administration output reports.

> ITEM: NURAPR-RES SYNONYM: 2

> ITEM: NURAPR-SAL SYNONYM: 3

> ITEM: NURAPR-STF SYNONYM: 4

> ITEM: NURAPR-STFLOC SYNONYM: 6

> ITEM: NURAPR-PHONE SYNONYM: 5

> ITEM: NURAPR-LOC-SER SYNONYM: 1 TIMESTAMP: 56656,39480

> UPPERCASE MENU TEXT: ADMINISTRATION RECORDS, PRINT

> NAME: NURAPR-MILITARY MENU TEXT: Military Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports summarizing the military experience of nursing employees. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=8 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: MILITARY REPORTS

> NAME: NURAPR-NDGREE MENU TEXT: Nursing Degree Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location and service reports summarizing the highest nursing

> degree held by registered nurses. Data may be sorted by service category or service position.

> ENTRY ACTION: S ANS1=10 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: NURSING DEGREE REPORTS

> NAME: NURAPR-NPSB MENU TEXT: NPSB Reports

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location, service, and individual reports of NPSB actions on nursing employees.

> ENTRY ACTION: S ANS1=9 ROUTINE: EN^NURADMIN UPPERCASE MENU TEXT: NPSB REPORTS

> NAME: NURAPR-PHONE MENU TEXT: Telephone Number Listings TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Menu displaying options for staff home telephone numbers. ITEM: NURAPR-PHONE-SER SYNONYM: 3

> ITEM: NURAPR-PHONE-LOC SYNONYM: 2

> ITEM: NURAPR-PHONE-IND SYNONYM: 1 TIMESTAMP: 56656,39467

> UPPERCASE MENU TEXT: TELEPHONE NUMBER LISTINGS

> NAME: NURAPR-PHONE-IND MENU TEXT: Individual Phone Number TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Displays the phone number(s) of an individual nursing employee. ROUTINE: NURA7C

> UPPERCASE MENU TEXT: INDIVIDUAL PHONE NUMBER

> NAME: NURAPR-PHONE-LOC

> MENU TEXT: Phone (Home) Numbers by Location

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A listing of employee home phone numbers by ward/location. ROUTINE: NURA7B

> UPPERCASE MENU TEXT: PHONE (HOME) NUMBERS BY LOCATI

> NAME: NURAPR-PHONE-SER

> MENU TEXT: Home Phone Number(s) For Entire Service

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Listing of home phone numbers for Nursing Service employees. ROUTINE: NURA7A

> UPPERCASE MENU TEXT: HOME PHONE NUMBER(S) FOR ENTIR

> NAME: NURAPR-PROF MENU TEXT: Proficiency Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location, service, and individual reports on actions taken to process the proficiencies/annual narratives of registered nurses.

> ENTRY ACTION: S ANS1=11 ROUTINE: EN^NURADMIN

> TIMESTAMP: 55432,48437 UPPERCASE MENU TEXT: PROFICIENCY REPORTS

> NAME: NURAPR-RES MENU TEXT: Resource Management Reports TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the primary menu for the resource management reports. ITEM: NURAPR-RES-UNCLAS SYNONYM: 1

> ITEM: NURAPR-RES-WRDCLAS SYNONYM: 2

> ITEM: NURAPR-RES-INDCLAS SYNONYM: 3

> ITEM: NURAPR-RES-PC SYNONYM: 4

> ITEM: NURAPR-RES-MANHR SYNONYM: 5

> ITEM: NURAPR-RES-AMISWKL SYNONYM: 6

> ITEM: NURAPR-RES-CURWKL SYNONYM: 7

> ITEM: NURAPR-RES-MDPC SYNONYM: 8

> ITEM: NURAPR-RES-FTEEC SYNONYM: 9

> ITEM: NURAPR-FTEE SYNONYM: 10 TIMESTAMP: 57005,57868

> UPPERCASE MENU TEXT: RESOURCE MANAGEMENT REPORTS

> NAME: NURAPR-RES-AMISWKL

> MENU TEXT: AMIS Workload Statistics Report

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Location and service reports that utilize manhours and acuity data from the NURS AMIS 1106 MANHOURS FILE (#213.4) to generate workload statistics for a user specified period between one and thirty days.

> ROUTINE: NURARWL4

> UPPERCASE MENU TEXT: AMIS WORKLOAD STATISTICS REPOR

> NAME: NURAPR-RES-CURWKL

> MENU TEXT: Workload Statistics Report (Current)

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Location and service reports which utilize data from the NURS AMIS 1106 MANHOURS FILE (#213.4) to calculate the current acuity and generate workload statistics.

> ROUTINE: NURARWL1 TIMESTAMP: 55446,33156 UPPERCASE MENU TEXT: WORKLOAD STATISTICS REPORT (CU

> NAME: NURAPR-RES-CURWKL-QUEUE

> MENU TEXT: TaskManager Workload Statistic Report (Projected) TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option can be scheduled to generate a current workload statistic report for the hospital at a time designated by a user.

> EXIT ACTION: K NURHOSP,NUROUT,NURPAGE,NURQUIT,NURSW1,NURSZAP,NURSHFT,NURY ENTRY ACTION: D EN1^NURARWL7 I \$D(ZTSK),'NUROUT D Q1^NURARWL1

> TIMESTAMP: 55446,33908

> UPPERCASE MENU TEXT: TASKMANAGER WORKLOAD STATISTIC

> NAME: NURAPR-RES-FTEEC

> MENU TEXT: FTEE Comparison (1106b) Report

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Location report similar to the AMIS 1106b Report which indicates ceiling (FTEE) and positions (FTEE) filled.

> ENTRY ACTION: S ANS1=1 ROUTINE: NURARST UPPERCASE MENU TEXT: FTEE COMPARISON (1106B) REPORT

> NAME: NURAPR-RES-INDCLAS

> MENU TEXT: Individual Patient Classification Reports TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Secondary patient classification menu displaying options for an individual patient's acuity data.

> ITEM: NURAPR-RES-INDCLAS-DT ITEM: NURAPR-RES-INDCLAS-WDT

> TIMESTAMP: 56656,39471

> UPPERCASE MENU TEXT: INDIVIDUAL PATIENT CLASSIFICAT

> NAME: NURAPR-RES-INDCLAS-DT

> MENU TEXT: Date/Time, Indiv. Classification Report By TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A report indicating an individual patient's daily classification (acuity) rating for a specific length of stay.

> ROUTINE: EN1^NURARCR0

> UPPERCASE MENU TEXT: DATE/TIME, INDIV. CLASSIFICATI

> NAME: NURAPR-RES-INDCLAS-WDT

> MENU TEXT: Ward & Date/Time, Indiv. Classification Report By TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A report indicating an individual patient's daily classification (acuity) rating for a specific length of stay on a specific ward/unit.

> ROUTINE: EN2^NURARCR0

> UPPERCASE MENU TEXT: WARD & DATE/TIME, INDIV. CLASS

> NAME: NURAPR-RES-MANHR MENU TEXT: Manhours Print

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Location and service reports which summarize the total RN, LPN, and NA patient care manhours worked. Reports can be generated for a daily, monthly, quarterly, or annual period.

> ROUTINE: NURARMH0 UPPERCASE MENU TEXT: MANHOURS PRINT

> NAME: NURAPR-RES-MDPC

> MENU TEXT: Patient Category Totals-Midnight Acuity Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: Location and service reports summarizing midnight patient category totals. Data can be generated for a daily, monthly, or quarterly period.

> EXIT ACTION: K NURTYPE ENTRY ACTION: S NURTYPE=1

> ROUTINE: NURARMC0 TIMESTAMP: 55745,57761 UPPERCASE MENU TEXT: PATIENT CATEGORY TOTALS-MIDNIG

> NAME: NURAPR-RES-PC

> MENU TEXT: Patient Category Totals-AMIS 1106 Reports TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: AMIS location and service reports which summarize patient category totals. Data can be generated for a daily, monthly or quarterly period.

> EXIT ACTION: K NURTYPE ENTRY ACTION: S NURTYPE=0 ROUTINE: NURARPC0

> UPPERCASE MENU TEXT: PATIENT CATEGORY TOTALS-AMIS 1

> NAME: NURAPR-RES-UNCLAS

> MENU TEXT: Current Unclassified Patient Print

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A service report listing all unclassified patients for the current day.

> ROUTINE: NURARNCT

> UPPERCASE MENU TEXT: CURRENT UNCLASSIFIED PATIENT P

> NAME: NURAPR-RES-UNCLAS-QUEUE

> MENU TEXT: TaskMan Current Unclassified Patient Report TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the Current Unclassified Patient Report to be generated by Task Man.

> EXIT ACTION: K NURQUEUE,NURQUIT ENTRY ACTION: D EN2^NURARWL7,Q1^NURARNCT TIMESTAMP: 55746,48741

> UPPERCASE MENU TEXT: TASKMAN CURRENT UNCLASSIFIED P

> NAME: NURAPR-RES-WKLSUM

> MENU TEXT: AMIS Workload Statistics Summary Report

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option provides an AMIS Workload Statistic Summary report by ward, and date.

> EXIT ACTION: K SUMSW ENTRY ACTION: S SUMSW=1 ROUTINE: NURARWL4

> UPPERCASE MENU TEXT: AMIS WORKLOAD STATISTICS SUMMA

> NAME: NURAPR-RES-WRDCLAS

> MENU TEXT: Daily Patient Classification Summary By Ward TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A ward report summarizing the classifications (acuities) of all patients on a given date and ward.

> ROUTINE: NURARCRW

> UPPERCASE MENU TEXT: DAILY PATIENT CLASSIFICATION S

> NAME: NURAPR-SAL MENU TEXT: Salary Reports TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option is for printing the administrative salary reports. ITEM: NURAPR-SAL-SER SYNONYM: 1

> ITEM: NURAPR-SAL-IND SYNONYM: 2

> ROUTINE: EN4^NURADMIN TIMESTAMP: 56656,39467 UPPERCASE MENU TEXT: SALARY REPORTS

> NAME: NURAPR-SAL-IND MENU TEXT: Individual Salary Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: A display of an individual employee's salary which is based on the current grade/step code found in the employee's staff record.

> ROUTINE: NURA5B

> UPPERCASE MENU TEXT: INDIVIDUAL SALARY REPORT

> NAME: NURAPR-SAL-SER

> MENU TEXT: Salary Report For Entire Service

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Report(s) indicating the current salary of nursing employees. The salary is based on the grade/step code found in the individual staff record of each employee.

> ROUTINE: NURA5A

> UPPERCASE MENU TEXT: SALARY REPORT FOR ENTIRE SERVI

> NAME: NURAPR-STF MENU TEXT: Staff Record Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Prints demographic and professional information on a specific nursing employee.

> ROUTINE: NURASPT UPPERCASE MENU TEXT: STAFF RECORD REPORT

> NAME: NURAPR-STFLOC

> MENU TEXT: Individual Staff Position/Location

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option displays data from all positions/assignments for an employee.

> EXIT ACTION: K NURSADD ENTRY ACTION: S NURSADD=1

> ROUTINE: NURASPL TIMESTAMP: 55069,45240 UPPERCASE MENU TEXT: INDIVIDUAL STAFF POSITION/LOCA

> NAME: NURCFE-CARE

> MENU TEXT: Patient Plan of Care, Site Configuration

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows a site to add or modify nursing care plan database entries.

> ROUTINE: EN1^NURCCPE TIMESTAMP: 55643,34045 UPPERCASE MENU TEXT: PATIENT PLAN OF CARE, SITE CON

> NAME: NURCFP-CARE

> MENU TEXT: Standard Patient Plan of Care Print

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option enables the user to verify or check any nursing care plan within the database. The user may selectively list or print, to any output device, any nursing care plan that was built into the database.

> ROUTINE: NURCCP1 TIMESTAMP: 55544,34273 UPPERCASE MENU TEXT: STANDARD PATIENT PLAN OF CARE

> NAME: NURCPE-CARE MENU TEXT: Patient Plan of Care, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option will allow a registered nurse to create or modify a patient's care plan.

> ROUTINE: EN1^NURCPP0 TIMESTAMP: 55427,53229 UPPERCASE MENU TEXT: PATIENT PLAN OF CARE, EDIT

> NAME: NURCPE-EVAL

> MENU TEXT: Evaluation/Target Date & Order Status Edit TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option will allow for the information about Nursing problems, Goals and Orders to be edited for a particular nursing care plan.

> ROUTINE: ENT1^NURCEVE0 TIMESTAMP: 55560,42818 UPPERCASE MENU TEXT: EVALUATION/TARGET DATE & ORDER

> NAME: NURCPE-I/O-DC REASON MENU TEXT: IV DC'ed Reason TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to edit reasons for discontinuing an IV in the GMRY IV DC'ED REASON file (#126.76).

> EXIT ACTION: K DIDEL,DLAYGO ENTRY ACTION: S (DIDEL,DLAYGO)=126.76 DIC {DIC}: GMRD(126.76, DIC(0): AEMQL

> DIE: GMRD(126.76, DR {DIE}: .01; UPPERCASE MENU TEXT: IV DC'ED REASON

> NAME: NURCPE-I/O-EDIT MENU TEXT: Intake/Output Data Entry Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: The Intake and Output module is a useful tool that provides an on- line tracking method for Intake and/or Output. The Intake and Output module also allows for Intravenous Therapy tracking as to fluids, IV starts and dressing changes.

> ITEM: NURCPE-I/O-INTAKE SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURCPE-I/O-OUTPUT SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURCPE-I/O-IV CARE SYNONYM: 3 DISPLAY ORDER: 3

> TIMESTAMP: 56656,39536

> UPPERCASE MENU TEXT: INTAKE/OUTPUT DATA ENTRY MENU

> NAME: NURCPE-I/O-FILE EDIT

> MENU TEXT: Configure I/O Files (ADP Coordinator Only) TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu is provided for the ADP coordinator to configure the following file entries: GMRY INPUT TYPE (#126.56), GMRY OUTPUT TYPE (#126.58), GMRY OUTPUT SUBTYPE (#126.6), GMRY IV SITE (#126.7), GMRY INTAKE ITEMS (#126.8), GMRY NUR IV SOLUTION (#126.9), GMRY NUR SHIFT/OTHER (#126.95), GMRY IV SITE DESCRIPTION (#126.72), GMRY IV CATHETER (#126.74) and GMRY IV DC'ED REASON (#126.76).

> ITEM: NURCPE-I/O-INPUT FILE1 SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURCPE-I/O-OUTPUT FILE1 SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURCPE-I/O-OUTPUT FILE2 SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: NURCPE-I/O-INTAKE ITEMS SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURCPE-I/O-IV SITE SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: NURCPE-I/O-IV SOL SYNONYM: 6 DISPLAY ORDER: 6

> ITEM: NURCPE-I/O-NURSHIFT SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: NURCPE-I/O-SITE DESCRP SYNONYM: 8 DISPLAY ORDER: 8

> ITEM: NURCPE-I/O-IV CATH SYNONYM: 9 DISPLAY ORDER: 9

> ITEM: NURCPE-I/O-DC REASON SYNONYM: 10 DISPLAY ORDER: 10

> TIMESTAMP: 56656,39541

> UPPERCASE MENU TEXT: CONFIGURE I/O FILES (ADP COORD

> NAME: NURCPE-I/O-INPUT FILE1 MENU TEXT: Intake Type TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option is used by the ADP coordinator to configure the NON-IV intake type entries for the GMRY INPUT TYPE file (#126.56). For example, PO, TUBE FEEDING, and OTHER are input types.

> EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=126.56

> DIC {DIC}: GMRD(126.56, DIC(0): AEMQL

> DIE: GMRD(126.56, DR {DIE}: .01;1; UPPERCASE MENU TEXT: INTAKE TYPE

> NAME: NURCPE-I/O-INTAKE MENU TEXT: Enter/Edit Patient Intake TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to enter or edit patient IV and NON-IV intake records.

> ROUTINE: EN2^NURCYED0

> UPPERCASE MENU TEXT: ENTER/EDIT PATIENT INTAKE

> NAME: NURCPE-I/O-INTAKE ITEMS MENU TEXT: Intake Items TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to enter items into the GMRY INTAKE ITEMS file (#126.8) pointed to by the GMRY PATIENT I/O FILE file (#126).

> EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=126.8

> DIC {DIC}: GMRD(126.8, DIC(0): AEMQL

> DIE: GMRD(126.8, DR {DIE}: .01;1;2 UPPERCASE MENU TEXT: INTAKE ITEMS

> NAME: NURCPE-I/O-IV CARE

> MENU TEXT: Start/Add/DC IV and Maintenance

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option contains seven protocols associated with intravenous therapy:

1.  Start IV - Starts a new IV line or heparin/saline lock/port.
2.  Solution: Replace/DC/Convert/Finish Solution - DC's the current solution, then replaces a new solution to the selected IV line or converts the IV according to the user's choice.
3.  Replace Same Solution - Replaces the same solution to a selected IV line.
4.  DC IV/Lock/Port and Site - Removes the IV/lock/port from a selected IV site and documents tubing changes.
5.  Care/Maintenance/Flush - Checks the site condition, and documents dressing, tubing changes and flushes.
6.  Add Additional Solution(s) - Adds additional solution(s) to an IV line without discontinuing an existing one.
7.  Restart DC'd IV - Restarts an IV which was discontinued due to infiltration or other reasons.
8.  Adjust Infusion Rate - Adjusts infusion rate for a selected IV.
9.  Flush - Flushes all IV line(s) for a selected infusion site. ROUTINE: EN3^NURCYED0 TIMESTAMP: 55528,49963 UPPERCASE MENU TEXT: START/ADD/DC IV AND MAINTENANC

> NAME: NURCPE-I/O-IV CATH MENU TEXT: IV Catheter TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to enter types of IV catheters into the GMRY IV CATHETER file (#126.74).

> EXIT ACTION: K DIDEL,DLAYGO ENTRY ACTION: S (DIDEL,DLAYGO)=126.74 DIC {DIC}: GMRD(126.74, DIC(0): AEMQL

> DIE: GMRD(126.74, DR {DIE}: .01; UPPERCASE MENU TEXT: IV CATHETER

> NAME: NURCPE-I/O-IV SITE MENU TEXT: IV Site TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to enter IV sites into the GMRY IV SITE file (#126.7). This information is used to track the IV insertion site and assist with documentation of the site's status and surrounding skin integrity.

> EXIT ACTION: K DIDEL,DLAYGO ENTRY ACTION: S (DIDEL,DLAYGO)=126.7 DIC {DIC}: GMRD(126.7, DIC(0): AEMQL

> DIE: GMRD(126.7, DR {DIE}: .01; UPPERCASE MENU TEXT: IV SITE

> NAME: NURCPE-I/O-IV SOL MENU TEXT: IV Solution TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: The ADP coordinator can enter IV solutions into the GMRY NUR IV SOLUTION file (#126.9) through this option. The IV solutions include admixtures, hyperals, intralipids, piggybacks and blood/blood products.

> EXIT ACTION: K DIDEL,DLAYGO ENTRY ACTION: S (DIDEL,DLAYGO)=126.9 DIC {DIC}: GMRD(126.9, DIC(0): AEMQL

> DIE: GMRD(126.9, DR {DIE}: .01;1;2 UPPERCASE MENU TEXT: IV SOLUTION

> NAME: NURCPE-I/O-NURSHIFT

> MENU TEXT: Shift Starting Hour and Other Parameters

> TYPE: edit CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: The shift starting hours stored in the GMRY NUR SHIFT/OTHER file (#126.95) are used to calculate the patient's total intake/output for night, day and evening shifts, respectively. The data type for hours can be entered "0800", "1600" and "2400". The heparin/saline default volume in milliliter (ml) for locks/ports is also kept in the file \#126.95.

> DIC {DIC}: GMRD(126.95, DIC(0): AMEQL

> DIE: GMRD(126.95, DR {DIE}: 1;2;3;4 UPPERCASE MENU TEXT: SHIFT STARTING HOUR AND OTHER

> NAME: NURCPE-I/O-OUTPUT MENU TEXT: Enter/Edit Patient Output TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to enter or edit patient output records.

> ROUTINE: EN1^NURCYED0

> UPPERCASE MENU TEXT: ENTER/EDIT PATIENT OUTPUT

> NAME: NURCPE-I/O-OUTPUT FILE1 MENU TEXT: Output Type TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option is provided for the ADP coordinator to configure the entries for the GMRY OUTPUT TYPE file (#126.58). URINE, STOOL and DRAINS, for example, are major output types.

> EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=126.58

> DIC {DIC}: GMRD(126.58, DIC(0): AMEQL

> DIE: GMRD(126.58, DR {DIE}: .01;1 UPPERCASE MENU TEXT: OUTPUT TYPE

> NAME: NURCPE-I/O-OUTPUT FILE2 MENU TEXT: Output Subtype TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to enter the entries for the GMRY OUTPUT SUBTYPE file (#126.6) pointed to by the GMRY PATIENT I/O FILE file (#126). VOID, FOLEY and STRAIGHT CATH, for example, are subtypes of

> URINE.

> EXIT ACTION: K DLAYGO ENTRY ACTION: S DLAYGO=126.6

> DIC {DIC}: GMRD(126.6, DIC(0): AEMQL

> DIE: GMRD(126.6, DR {DIE}: .01;1 UPPERCASE MENU TEXT: OUTPUT SUBTYPE

> NAME: NURCPE-I/O-SITE DESCRP MENU TEXT: IV Site Description TYPE: edit CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the ADP coordinator to enter IV site descriptions into the GMRY IV SITE DESCRIPTION file (#126.72). This information is used for documenting site maintenance.

> EXIT ACTION: K DIDEL,DLAYGO ENTRY ACTION: S (DIDEL,DLAYGO)=126.72 DIC {DIC}: GMRD(126.72, DIC(0): AEMQL

> DIE: GMRD(126.72, DR {DIE}: .01; UPPERCASE MENU TEXT: IV SITE DESCRIPTION

> NAME: NURCPE-VIT ADMISSION VM MENU TEXT: TPR B/P, Ht and Wt.

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter the following vital/measurements through a single option: temperature, pulse, respirations, blood pressure, height and weight.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN5^NURCVED2 TIMESTAMP: 55441,53044 UPPERCASE MENU TEXT: TPR B/P, HT AND WT.

> NAME: NURCPE-VIT BLOOD PRESSURE MENU TEXT: \*\*deleted\*\* OUT OF ORDER MESSAGE: OUT OF ORDER TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option permits users to enter data on a patient's blood pressure.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN4^NURCVED2 UPPERCASE MENU TEXT: \*\*DELETED\*\*

> NAME: NURCPE-VIT CAT/QUAL TABLE

> MENU TEXT: Display Vitals Category/Qualifier Table

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option displays categories/qualifiers table for blood pressure, temperature, pulse, respiration, weight and circumference/girth.

> ROUTINE: EN4^NURCVUT0

> UPPERCASE MENU TEXT: DISPLAY VITALS CATEGORY/QUALIF

> NAME: NURCPE-VIT CHANGE V/M D/T MENU TEXT: Change Date/Time Taken TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to enter vitals/measurements (on the same patient) for a different Date/Time.

> ROUTINE: EN7^NURCVED2

> UPPERCASE MENU TEXT: CHANGE DATE/TIME TAKEN

> NAME: NURCPE-VIT CIRCUMF/GIRTH MENU TEXT: Circumference/Girth TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter circumference/girth measurement.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2

> ROUTINE: EN11^NURCVED2 UPPERCASE MENU TEXT: CIRCUMFERENCE/GIRTH

> NAME: NURCPE-VIT CVP MENU TEXT: CVP (Central Venous Pressure) TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter central venous pressure measurement.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN12^NURCVED2

> UPPERCASE MENU TEXT: CVP (CENTRAL VENOUS PRESSURE)

> NAME: NURCPE-VIT EXT B/P

> MENU TEXT: Detailed B/P and Associated Pulse

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter detailed blood pressure and associated information. In addition to the numeric values of the blood pressure and pulse readings, the site/location where the blood pressure and pulse were taken (e.g., left arm vs right arm), the position of the patient (e.g., sitting, standing) and other qualifiers are documented.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN9^NURCVED2

> UPPERCASE MENU TEXT: DETAILED B/P AND ASSOCIATED PU

> NAME: NURCPE-VIT FILECONF

> MENU TEXT: Selected V/M Site File Functions

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu contains the following options: 1. Enter/Edit Vitals Qualifiers option is used to configure qualifiers in the GMRV Vital Qualifier

> file (#120.52) for vital types, blood pressure, for example. 2. Change Default Qualifiers for Temp./Pulse is used to change the default qualifier for temperature and pulse. 3. Display Vitals Category/Qualifier Table is used to print the categories/qualifiers table for each vital type.

> ITEM: NURCPE-VIT VMSITE SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURCPE-VIT VMQUALTY SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURCPE-VIT CAT/QUAL TABLE SYNONYM: 3 DISPLAY ORDER: 3

> TIMESTAMP: 56981,50672

> UPPERCASE MENU TEXT: SELECTED V/M SITE FILE FUNCTIO

> NAME: NURCPE-VIT HTWT MENU TEXT: \*\*deleted\*\* OUT OF ORDER MESSAGE: OUT OF ORDER TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows entry for height and weight measurements. EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN10^NURCVED2 UPPERCASE MENU TEXT: \*\*DELETED\*\*

> NAME: NURCPE-VIT O2SATURATION MENU TEXT: Pulse Oximetry

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter pulse oximetry.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN13^NURCVED2 UPPERCASE MENU TEXT: PULSE OXIMETRY

> NAME: NURCPE-VIT PULSE RADIAL MENU TEXT: Pulse

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter a patient's pulse rate. EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN3^NURCVED2 UPPERCASE MENU TEXT: PULSE

> NAME: NURCPE-VIT TPR MENU TEXT: TPR

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to enter temperature, pulse and respirations.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN1^NURCVED2 UPPERCASE MENU TEXT: TPR

> NAME: NURCPE-VIT TPR B/P MENU TEXT: TPR B/P

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows data entry of temperature, pulse, respiration and blood pressure.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN2^NURCVED2 UPPERCASE MENU TEXT: TPR B/P

> NAME: NURCPE-VIT TPR EXT B/P MENU TEXT: Temp, Detailed PR and B/P

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows data to be entered for temperature, pulse, respiration and detailed blood pressure. Detailed blood pressure captures the numeric value of both the systolic and diastolic pressures and also associates

1)  the site where the pressure was taken (e.g., left arm vs right arm), and
2)  the position of the patient when the reading was taken (e.g., sitting vs standing).

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN8^NURCVED2

> UPPERCASE MENU TEXT: TEMP, DETAILED PR AND B/P

> NAME: NURCPE-VIT TPRBW MENU TEXT: TPR, B/P and Wt.

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows data to be entered for temperature, pulse, respiration, blood pressure and weight.

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN4^NURCVED2 UPPERCASE MENU TEXT: TPR, B/P AND WT.

> NAME: NURCPE-VIT VMCONFIG MENU TEXT: User Configurable Combination TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to select types of Vitals/Measurements from the following list to enter the data.

> 1 T 2 P 3 R 4 B/P 5 Wt 6 Ht 7 Circumference/Girth 8 Pulse Oximetry 9 CVP (Central Venous Pressure)

> EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN14^NURCVED2

> UPPERCASE MENU TEXT: USER CONFIGURABLE COMBINATION NAME: NURCPE-VIT VMQUALTY

> MENU TEXT: Change Default Qualifiers for Temp./Pulse TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option is for the ADP coordinator to change default qualifiers for temperature/pulse in the GMRV Vital Category file (#120.53).

> ROUTINE: EN3^NURCVUT0

> UPPERCASE MENU TEXT: CHANGE DEFAULT QUALIFIERS FOR

> NAME: NURCPE-VIT VMSITE MENU TEXT: Enter/Edit Vitals Qualifiers TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option is for the ADP coordinator to configure the GMRV Vital Qualifier file (#120.52) entries.

> ROUTINE: EN2^NURCVUT0

> UPPERCASE MENU TEXT: ENTER/EDIT VITALS QUALIFIERS

> NAME: NURCPE-VIT WEIGHT MENU TEXT: Weight

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows users to document a patient's weight. EXIT ACTION: D EXITACT^NURCVED2 ENTRY ACTION: D ENTACT^NURCVED2 ROUTINE: EN6^NURCVED2 UPPERCASE MENU TEXT: WEIGHT

> NAME: NURCPE-VIT-EDIT

> MENU TEXT: Vitals/Measurements Data Entry

> TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This menu contains options which permit users to select the type of patient vitals/measurements to be entered.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 37%" />
<col style="width: 24%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th>ITEM: NURCPE-VIT</th>
<th><blockquote>
<p>TPR</p>
</blockquote></th>
<th>SYNONYM:</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>TPR B/P</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>PULSE RADIAL</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>ADMISSION VM</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>WEIGHT</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>CHANGE V/M D/T</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>TPR EXT B/P</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>EXT B/P</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>VMCONFIG</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>CIRCUMF/GIRTH</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>O2SATURATION</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>CVP</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>11</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ITEM: NURCPE-VIT</td>
<td><blockquote>
<p>TPRBW</p>
</blockquote></td>
<td>SYNONYM:</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DISPLAY ORDER:</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>EXIT ACTION: K</td>
<td><blockquote>
<p>NURSDBA,NURFLAG</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ENTRY ACTION: S NURFLAG=1 D ENTACT^NURCVED2 TIMESTAMP: 57037,47483

> UPPERCASE MENU TEXT: VITALS/MEASUREMENTS DATA ENTRY

> NAME: NURCPE-VIT-ERROR

> MENU TEXT: Edit a Vital/Measurement Entered in Error TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows users to correct errors in vitals/measurements. A new record is created, and the old record is marked as entered in error.

> ROUTINE: EN2^NURCVED0

> UPPERCASE MENU TEXT: EDIT A VITAL/MEASUREMENT ENTER

> NAME: NURCPP-ASSWRK MENU TEXT: Patient Assignment Worksheet TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option contains the various patient assignment sheet print options.

> ROUTINE: NURCAS0 TIMESTAMP: 54356,27898 UPPERCASE MENU TEXT: PATIENT ASSIGNMENT WORKSHEET

> NAME: NURCPP-CARE MENU TEXT: Patient Plan of Care, Print TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option displays the active patient problems or all problems associated with a particular patient upon user request.

> ROUTINE: EN1^NURCPPS1 TIMESTAMP: 55427,53262 TIMESTAMP OF PRIMARY MENU: 55425,63241

> UPPERCASE MENU TEXT: PATIENT PLAN OF CARE, PRINT

> NAME: NURCPP-EVAL

> MENU TEXT: Patient Problems to be Evaluated

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option will produce a report of all Nursing Problems for a particular patient that need to be evaluated by a certain date/time.

> ROUTINE: ENT1^NURCEVP0 TIMESTAMP: 55565,35540 UPPERCASE MENU TEXT: PATIENT PROBLEMS TO BE EVALUAT

> NAME: NURCPP-I/O-48HRS MENU TEXT: Print I/O Summary (48 Hrs)

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option summarizes patient intake/output for the previous day and today.

> ROUTINE: EN5^NURCYRP0

> UPPERCASE MENU TEXT: PRINT I/O SUMMARY (48 HRS)

> NAME: NURCPP-I/O-CURRENT

> MENU TEXT: Print I/O Summary (Midnight to Present)

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option summarizes current patient intake/output. ROUTINE: EN4^NURCYRP0

> UPPERCASE MENU TEXT: PRINT I/O SUMMARY (MIDNIGHT TO

> NAME: NURCPP-I/O-IVFLOW

> MENU TEXT: Intravenous Infusion Flow Sheet

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints intravenous flow sheets by ward, room or by

> patient.

> ROUTINE: EN7^NURCYRP0

> UPPERCASE MENU TEXT: INTRAVENOUS INFUSION FLOW SHEE

> NAME: NURCPP-I/O-SF511

> MENU TEXT: Expanded SF 511 Report (Itemized I/O)

> OUT OF ORDER MESSAGE: OUT OF ORDER TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints the patient vital measurements and itemized intake/output report in SF 511 Form format.

> ROUTINE: EN3^NURCYRP0

> UPPERCASE MENU TEXT: EXPANDED SF 511 REPORT (ITEMIZ

> NAME: NURCPP-I/O-SHIFT AND EVENT

> MENU TEXT: 24 Hours Itemized Shift Report

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option produces itemized patient intake and output reports by shift for a period of time as defined by the user.

> ROUTINE: EN6^NURCYRP0

> UPPERCASE MENU TEXT: 24 HOURS ITEMIZED SHIFT REPORT

> NAME: NURCPP-I/O-SUM

> MENU TEXT: Print I/O Summary by Patient (by Shift & Day(s)) TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option summarizes patient intake/output by major category and shift for a period of time as defined by the user.

> ROUTINE: EN1^NURCYRP0

> UPPERCASE MENU TEXT: PRINT I/O SUMMARY BY PATIENT (

> NAME: NURCPP-VIT-CUM MENU TEXT: Cumulative Vitals Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints a report containing vitals/measurement information for a patient over a given period of time.

> ROUTINE: EN4^NURCVPR0

> UPPERCASE MENU TEXT: CUMULATIVE VITALS REPORT

> NAME: NURCPP-VIT-DISP

> MENU TEXT: Latest Vitals Display for a Patient

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option displays on screen the latest vitals/measurements for a particular patient.

> ROUTINE: EN2^NURCVPR0

> UPPERCASE MENU TEXT: LATEST VITALS DISPLAY FOR A PA

> NAME: NURCPP-VIT-ERROR

> MENU TEXT: Print Vitals Entered in Error for a Patient TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints a report of all vitals/measurements entered in error for a particular patient for a given time span.

> ROUTINE: EN3^NURCVPR0

> UPPERCASE MENU TEXT: PRINT VITALS ENTERED IN ERROR

> NAME: NURCPP-VIT-SF511 MENU TEXT: V/M Graphic Reports

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints specific Vitals/Measurements graphic reports

> including the Vital Flow Sheet (SF511), the B/P Plotting Chart (SF512-A), the Weight Chart (VAF10-2614f), and the Pulse Oximetry/Respiration Graph (SF 512).

> ROUTINE: EN1^NURCVPR0 TIMESTAMP: 55427,53455 UPPERCASE MENU TEXT: V/M GRAPHIC REPORTS

> NAME: NURCPP-VIT-WARD MENU TEXT: Latest Vitals by Location TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option prints the latest vitals/measurements for all patients on a given location.

> ROUTINE: EN5^NURCVPR0

> UPPERCASE MENU TEXT: LATEST VITALS BY LOCATION

> NAME: NURCRP-CP RANK LISTING

> MENU TEXT: Rank Listing of Care Plan Data

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option will print a rank listing of care plan data over a date/time range for a particular group of nursing locations.

> ROUTINE: EN1^NURCRL0 TIMESTAMP: 55544,37502 UPPERCASE MENU TEXT: RANK LISTING OF CARE PLAN DATA

> NAME: NURQA-PT-10PRINT MENU TEXT: QI Summary, Print

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to print all of the QI Summary data for a particular survey, including the statistics for that survey.

> EXIT ACTION: Q ROUTINE: NURQRPT0

> TIMESTAMP: 55655,48686 UPPERCASE MENU TEXT: QI SUMMARY, PRINT

> NAME: NURQA-PT-ALL MENU TEXT: Edit All QI Summary Data TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to edit all the QI Summary data for a survey.

> EXIT ACTION: Q ROUTINE: EN8^NURQEDT1

> DIC(B): %^ TIMESTAMP: 55430,29413 UPPERCASE MENU TEXT: EDIT ALL QI SUMMARY DATA

> NAME: NURQA-PT-DATA MENU TEXT: Data

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit and analyze data for a survey.

> EXIT ACTION: Q ROUTINE: EN3^NURQEDT0

> DIC(0): AEMQL TIMESTAMP: 55430,29103 UPPERCASE MENU TEXT: DATA

> NAME: NURQA-PT-ESCP

> MENU TEXT: QI Summary Standards of Care/Practice File TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit standards of care and practice data.

> EXIT ACTION: Q

> ENTRY ACTION: I \$\$SURGENVR^NURQUTL1(2,1) N DA,DIC,DIE,DLAYGO,DR,X,Y F S DLAYG O=217.1,DIC="^NURQ(217.1,",DIC(0)="AEQL" W ! D ^DIC Q:+Y'\>0 S DA=+Y,DIE=DIC,DR= ".01;1;2" D ^DIE Q:\$D(Y)

> TIMESTAMP: 55536,28464

> UPPERCASE MENU TEXT: QI SUMMARY STANDARDS OF CARE/P

> NAME: NURQA-PT-FRE MENU TEXT: QI Summary Frequency File TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit frequency data (how often a survey is given).

> EXIT ACTION: Q

> ENTRY ACTION: I \$\$SURGENVR^NURQUTL1(2,1) N DA,DIC,DIE,DLAYGO,DR,X,Y F S DLAYG O=217.3,DIC="^NURQ(217.3,",DIC(0)="AEQL" W ! D ^DIC Q:Y'\>0 S DA=+Y,DIE=DIC,DR="

> .01" D ^DIE Q:\$D(Y) TIMESTAMP: 55536,38591

> UPPERCASE MENU TEXT: QI SUMMARY FREQUENCY FILE

> NAME: NURQA-PT-INDIC MENU TEXT: Performance Measures TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit the indicators related to a survey. The indicators are the questions from the survey.

> EXIT ACTION: Q ROUTINE: EN4^NURQEDT0 TIMESTAMP: 55430,29458

> UPPERCASE MENU TEXT: PERFORMANCE MEASURES

> NAME: NURQA-PT-KEYFUNC MENU TEXT: Important Functions TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit key functions (important aspects of care) involved in a survey.

> EXIT ACTION: Q ROUTINE: EN1^NURQEDT0

> TIMESTAMP: 55446,27356 UPPERCASE MENU TEXT: IMPORTANT FUNCTIONS

> NAME: NURQA-PT-MENU MENU TEXT: QI Summary Enter/Edit TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This menu allows the user to edit all data in the QI Summary records.

> ITEM: NURQA-PT-RESP SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURQA-PT-KEYFUNC SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURQA-PT-INDIC SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURQA-PT-DATA SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: NURQA-PT-ROFR SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: NURQA-PT-ALL SYNONYM: 8 DISPLAY ORDER: 8

> ITEM: NURQA-PT-OTHER SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: NURQA-PT-REFR SYNONYM: 6 DISPLAY ORDER: 6

> EXIT ACTION: Q TIMESTAMP: 56789,37781 UPPERCASE MENU TEXT: QI SUMMARY ENTER/EDIT

> NAME: NURQA-PT-OTHER MENU TEXT: Other QI Summary Data

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This is an extra option to cover any new field that might be added to the JCAHO requirements.

> EXIT ACTION: Q ROUTINE: EN8^NURQEDT0

> UPPERCASE MENU TEXT: OTHER QI SUMMARY DATA

> NAME: NURQA-PT-RAT MENU TEXT: QI Summary Rationale File TYPE: action CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit entries in the NURQ Rationale (217.2) file.

> EXIT ACTION: Q

> ENTRY ACTION: I \$\$SURGENVR^NURQUTL1(2,1) N DA,DIC,DIE,DLAYGO,DR,X,Y F S DLAYG O=217.2,DIC="^NURQ(217.2,",DIC(0)="AEQL" W ! D ^DIC Q:+Y'\>0 S DA=+Y,DIE=DIC,DR= ".01" D ^DIE Q:\$D(Y)

> UPPERCASE MENU TEXT: QI SUMMARY RATIONALE FILE

NAME: NURQA-PT-REFR MENU TEXT: References

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit the references for a survey.

> EXIT ACTION: Q ROUTINE: EN7^NURQEDT0 UPPERCASE MENU TEXT: REFERENCES

> NAME: NURQA-PT-RESP MENU TEXT: Disciplines

> TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to assign responsibility for a survey to a person or a specific group of people.

> EXIT ACTION: Q ROUTINE: EN5^NURQEDT0

> TIMESTAMP: 54992,27755 UPPERCASE MENU TEXT: DISCIPLINES

> NAME: NURQA-PT-ROFR MENU TEXT: Receiver of Results TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE X ACTION PRESENT: YES

> DESCRIPTION: This option allows the user to enter/edit the people or groups of people who received the results of the survey.

> EXIT ACTION: Q ROUTINE: EN2^NURQEDT0 UPPERCASE MENU TEXT: RECEIVER OF RESULTS

> NAME: NURQA-SITEFILE MENU TEXT: QI Site Files TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu allows the user to edit all data in the QI site files.

> ITEM: NURQA-PT-ESCP SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURQA-PT-FRE SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURQA-PT-RAT SYNONYM: 3

> TIMESTAMP: 57005,45436 UPPERCASE MENU TEXT: QI SITE FILES

> NAME: NURS-ADM MENU TEXT: Administrator's Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Main menu for nursing administrators. ITEM: NURSPP-MENU SYNONYM: 4

> DISPLAY ORDER: 4

> ITEM: NURAED-MENU SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURAPR-STFLOC SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: NURAPR-MENU SYNONYM: 2

> DISPLAY ORDER: 2

> ITEM: NURSE-PR-MENU SYNONYM: 3 DISPLAY ORDER: 3

> TIMESTAMP: 56656,39509

> UPPERCASE MENU TEXT: ADMINISTRATOR'S MENU

> NAME: NURS-ALL

> MENU TEXT: Nursing Features (all options)

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu is for the nursing application coordinator. It displays all enter/edit and print options specific to administration, clinical, education, quality assurance, and package site files.

> ITEM: NURAED-MENU SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURSPE-MENU SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: NURSPP-MENU SYNONYM: 6 DISPLAY ORDER: 6

> ITEM: NURSFL-MENU SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: NURSCL-MENU SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: NURAPR-MENU SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURSE-PR-MENU SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURSQE-MENU SYNONYM: 8 DISPLAY ORDER: 8

> ITEM: NURSSP-MENU SYNONYM: 11 DISPLAY ORDER: 11

> ITEM: NURSQA-PR-MENU SYNONYM: 9 DISPLAY ORDER: 9

> ITEM: NURQA-SITEFILE SYNONYM: 10 DISPLAY ORDER: 10

> TIMESTAMP: 56830,56530

> UPPERCASE MENU TEXT: NURSING FEATURES (ALL OPTIONS)

> NAME: NURS-COMP

> MENU TEXT: Position Control/Staff File Integrity Report TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option searches the Position Control File (#211.8) for staff who are not in the NURS Staff File (#210). If any is found, a listing is displayed to the terminal or can be queued to a printer. The user may selectively re-enter any of the staff with all required data.

> Short Menu Text: COMPARE F-211.8 AGAINST F-210 ROUTINE: NURSCEP

> UPPERCASE MENU TEXT: POSITION CONTROL/STAFF FILE IN

> NAME: NURS-ED MENU TEXT: Nursing Educator's Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Main menu for nursing education staff. ITEM: NURAPR-STFLOC SYNONYM: 2

> DISPLAY ORDER: 2

> ITEM: NURSE-PR-MENU SYNONYM: 1 DISPLAY ORDER: 1

> TIMESTAMP: 56656,39509 TIMESTAMP OF PRIMARY MENU: 54446,52679 UPPERCASE MENU TEXT: NURSING EDUCATOR'S MENU

> NAME: NURS-EXP

> MENU TEXT: NURS Staff Experience Integrity Check/Fix TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION:

> This option checks the integrity of the NURS STAFF Experience sub-file. The option will detect and correct the following discrepancies:

1.  Change pointer values in name field to appropriate free-text values.
2.  Delete corrupted entries containing no data or cross references.
3.  Restore the missing name field for entries with a "B" index entry.
4.  Convert lower case name data to uppercase.
5.  Delete entries not found in the NURS CLINICAL BACKGROUND File.
6.  Remove duplicate cross reference entries from the subfile.

> This option checks, cleans and re-crossreferences the Nurstaff Experience Sub-File.

> ROUTINE: NURSEXP

> UPPERCASE MENU TEXT: NURS STAFF EXPERIENCE INTEGRIT

> NAME: NURS-HN MENU TEXT: Head Nurse's Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Menu for head nurses.

> ITEM: NURSQE-REVCL-MENU SYNONYM: 5 DISPLAY ORDER: 5

> ITEM: NURSPE-MENU SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURSPP-MENU SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURAMN-MANED SYNONYM: 6 DISPLAY ORDER: 6

> ITEM: NURAPR-HNMEN SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURAMN-STA-LOC SYNONYM: 7 DISPLAY ORDER: 7

> ITEM: NURSE-PR-MENUHN SYNONYM: 3 DISPLAY ORDER: 3

> TIMESTAMP: 56656,39510 UPPERCASE MENU TEXT: HEAD NURSE'S MENU

> NAME: NURS-PURG MENU TEXT: Classification File Purge TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option deletes data from the 214.6 and 214.7 classification globals prior to the date specified by the user.

> ROUTINE: EN1^NURSADEL

> UPPERCASE MENU TEXT: CLASSIFICATION FILE PURGE

> NAME: NURS-QA MENU TEXT: QA Coordinator's Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Main menu for the QA coordinator. ITEM: NURSQP-MENU SYNONYM: 1

> ITEM: NURSQE-MENU SYNONYM: 2 TIMESTAMP: 56656,39500

> UPPERCASE MENU TEXT: QA COORDINATOR'S MENU

> NAME: NURS-RN MENU TEXT: Staff Nurse Menu TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Main menu for staff nurses.

> ITEM: NURSPE-MENU SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURSPP-MENU SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURAMN-MANED SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURSE-PR-MENURN SYNONYM: 3 DISPLAY ORDER: 3

> TIMESTAMP: 56656,39510 TIMESTAMP OF PRIMARY MENU: 54762,31247 UPPERCASE MENU TEXT: STAFF NURSE MENU

> NAME: NURS-SYS-MGR MENU TEXT: Nursing System Manager's Menu TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE E ACTION PRESENT: YES

> DESCRIPTION: Menu for the nursing ADP coordinator. ITEM: NURS-ADM SYNONYM: 1

> ITEM: NURS-HN SYNONYM: 3

> ITEM: NURS-ED SYNONYM: 4

> ITEM: NURSFM-MENU SYNONYM: 2

> ITEM: NURS-QA SYNONYM: 6

> ITEM: NURS-RN SYNONYM: 7

> ITEM: NURS-ALL SYNONYM: 5

> ENTRY ACTION: D ^NURS TIMESTAMP: 56999,57515 TIMESTAMP OF PRIMARY MENU: 54762,31247

> UPPERCASE MENU TEXT: NURSING SYSTEM MANAGER'S MENU

> NAME: NURSCL-MENU MENU TEXT: Clinical Site File Functions TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the main menu for editing information in the clinical site files.

> ITEM: NURCFP-CARE SYNONYM: 1

> ITEM: NURCFE-CARE SYNONYM: 2

> ITEM: NURSPT-WRDACT SYNONYM: 3

> ITEM: NURSPT-WRDINA SYNONYM: 4

> ITEM: NURCPE-VIT FILECONF SYNONYM: 5

> ITEM: NURCPE-I/O-FILE EDIT SYNONYM: 6 TIMESTAMP: 57013,52899

> UPPERCASE MENU TEXT: CLINICAL SITE FILE FUNCTIONS

> NAME: NURSE-PR-AAF

> MENU TEXT: AA/Funding Requests Report (132 Col)

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to print an authorized absence/funding requests report (132 column).

> ROUTINE: EN1^NURSEPCA TIMESTAMP: 55516,43165 UPPERCASE MENU TEXT: AA/FUNDING REQUESTS REPORT (13

> NAME: NURSE-PR-CES

> MENU TEXT: C.E. Training Attendance Summary Report (132 Col) TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows the user to print a continuing education program attendance summary report.

> ROUTINE: NURSEPCP

> UPPERCASE MENU TEXT: C.E. TRAINING ATTENDANCE SUMMA

> NAME: NURSE-PR-DEMP

> MENU TEXT: Individual Employee Deficiency Report

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates an individual mandatory training class

> deficiency report by calendar or fiscal year, for a nursing employee in an 80 or 132 column reporting format.

> ROUTINE: EN1^NURSEPD0 TIMESTAMP: 55594,48385 UPPERCASE MENU TEXT: INDIVIDUAL EMPLOYEE DEFICIENCY

> NAME: NURSE-PR-MENU

> MENU TEXT: Nursing Education Reports, Print

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu is a primary menu displaying options which print nursing education data.

> ITEM: NURSE-PR-MILOC SYNONYM: 1

> ITEM: NURSE-PR-MIND SYNONYM: 2

> ITEM: NURSE-PR-MI3LC SYNONYM: 3

> ITEM: NURSE-PR-MI3I SYNONYM: 4

> ITEM: NURSE-PR-MIDEF SYNONYM: 5

> ITEM: NURSE-PR-AAF SYNONYM: 7

> ITEM: NURSE-PR-DEMP SYNONYM: 6

> ITEM: NURSE-PR-CES SYNONYM: 8 TIMESTAMP: 56656,39513

> UPPERCASE MENU TEXT: NURSING EDUCATION REPORTS, PRI

> NAME: NURSE-PR-MENUHN

> MENU TEXT: Print Nursing Education Reports

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This is an education menu under the head nurse menu. ITEM: NURSE-PR-MILOC SYNONYM: 1

> ITEM: NURSE-PR-MIND SYNONYM: 2

> ITEM: NURSE-PR-MI3I SYNONYM: 3

> ITEM: NURSE-PR-MIDEF SYNONYM: 4

> ITEM: NURSE-PR-MI3LC SYNONYM: 5

> ITEM: NURSE-PR-DEMP SYNONYM: 6 TIMESTAMP: 56656,39513

> UPPERCASE MENU TEXT: PRINT NURSING EDUCATION REPORT

> NAME: NURSE-PR-MENURN

> MENU TEXT: Print Nursing Education Reports

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This is an education menu under the staff nurse menu. ITEM: NURSE-PR-DEMP SYNONYM: 1

> ITEM: NURSE-PR-MI3I SYNONYM: 2 TIMESTAMP: 56656,39513

> UPPERCASE MENU TEXT: PRINT NURSING EDUCATION REPORT

> NAME: NURSE-PR-MI3I

> MENU TEXT: Individual 3 Yr. Training Report

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates a 3 fiscal or calendar year report of attendance at mandatory, continuing education, other, ward/unit location or all types classes for a nursing employee in an 80 or 132 column reporting format.

> ROUTINE: EN1^NURSEP3I TIMESTAMP: 55529,28661 UPPERCASE MENU TEXT: INDIVIDUAL 3 YR. TRAINING REPO

> NAME: NURSE-PR-MI3LC MENU TEXT: 3 Yr. Training Report by Unit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates a 3 fiscal or calendar year report, by

> nursing location of attendance at mandatory, continuing education, other, ward/unit location or all types of classes in an 80 or 132 column reporting format.

> ROUTINE: EN1^NURSEP31

> UPPERCASE MENU TEXT: 3 YR. TRAINING REPORT BY UNIT

> NAME: NURSE-PR-MIDEF

> MENU TEXT: Mandatory Training Deficiency by Unit/Class TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates a fiscal or calendar year mandatory training class deficiency report, by nursing location, in an 80 or 132 column reporting format.

> ROUTINE: EN1^NURSEPD2

> UPPERCASE MENU TEXT: MANDATORY TRAINING DEFICIENCY

> NAME: NURSE-PR-MILOC MENU TEXT: Training Report by Unit/Class TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates a report of mandatory, continuing education, other, ward/unit location or all types of class attendance, by nursing location, for a user specified time period in an 80 or 132 column reporting format.

> ROUTINE: EN1^NURSEPML

> UPPERCASE MENU TEXT: TRAINING REPORT BY UNIT/CLASS

> NAME: NURSE-PR-MIND MENU TEXT: Individual Training Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option generates a report of mandatory, continuing education, other, ward/unit location, or all types of class attendance in an

> 80 or 132 column reporting format for a nursing employee for a user specified time period.

> ROUTINE: EN1^NURSEPIN TIMESTAMP: 55615,48381 UPPERCASE MENU TEXT: INDIVIDUAL TRAINING REPORT

> NAME: NURSFL-LOC MENU TEXT: Nursing Location File, Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Permits the service to enter and modify demographic information specific to ward/units, clinics, and other nursing assignment locations in the NURS LOCATION FILE (#211.4). This option also allows editing of the Budgeted FTEE information contained in the NURS POSITION CONTROL FILE (#211.8).

> ROUTINE: EN3^NURSAFUD TIMESTAMP: 55468,49909 TIMESTAMP OF PRIMARY MENU: 53582,52155

> UPPERCASE MENU TEXT: NURSING LOCATION FILE, EDIT

> NAME: NURSFL-MENU

> MENU TEXT: Administrative Site File Functions

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Primary menu displaying options which edit nursing site files. ITEM: NURAAM-ACUEDT SYNONYM: 1

> ITEM: NURAFL-CERT SYNONYM: 3

> ITEM: NURAFL-BFU SYNONYM: 4

> ITEM: NURAFL-GS-COD SYNONYM: 5

> ITEM: NURSFL-LOC SYNONYM: 6

> ITEM: NURAFL-SPO SYNONYM: 8

> ITEM: NURAFL-TOD SYNONYM: 9

> ITEM: NURSFL-SITE SYNONYM: 11

> ITEM: NURAFL-VAC SYNONYM: 10

> ITEM: NURSFL-PRIV SYNONYM: 2

> ITEM: NURSLO-PRINT SYNONYM: 7

> ITEM: NURAFL-CLBK SYNONYM: 12

> ITEM: NURAFL-PROD-LINE SYNONYM: 13

> TIMESTAMP: 56830,56534 TIMESTAMP OF PRIMARY MENU: 54191,51739 UPPERCASE MENU TEXT: ADMINISTRATIVE SITE FILE FUNCT

> NAME: NURSFL-PRIV MENU TEXT: Privilege File Edit TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows for the entry/edit of data in the NURS PRIVILEGE FILE (#212.6).

> ROUTINE: EN1^NURSAFU0 UPPERCASE MENU TEXT: PRIVILEGE FILE EDIT

> NAME: NURSFL-SITE MENU TEXT: Site Parameter File TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option will allow the user to update the NURS PARAMETERS FILE (#213.9).

> ROUTINE: NURSAPFU UPPERCASE MENU TEXT: SITE PARAMETER FILE

> NAME: NURSFM-DD'S MENU TEXT: List File Attributes TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: Prints data dictionaries for the nursing ADP coordinator. ROUTINE: EN4^NURSFMU

> UPPERCASE MENU TEXT: LIST FILE ATTRIBUTES

> NAME: NURSFM-INQUIRE MENU TEXT: Inquire to File Entries TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: The VA FileMan inquire option for the nursing ADP coordinator. ROUTINE: EN3^NURSFMU

> UPPERCASE MENU TEXT: INQUIRE TO FILE ENTRIES

> NAME: NURSFM-MENU

> MENU TEXT: VA FileMan (Nursing ADP Coordinator)

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Nursing ADP coordinator's VA FileMan options. ITEM: NURSFM-PRINT SYNONYM: 1

> ITEM: NURSFM-SEARCH SYNONYM: 2

> ITEM: NURSFM-INQUIRE SYNONYM: 3

> ITEM: NURSFM-DD'S SYNONYM: 4 TIMESTAMP: 56656,39507

> UPPERCASE MENU TEXT: VA FILEMAN (NURSING ADP COORDI

> NAME: NURSFM-PRINT MENU TEXT: Print File Entries TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: The VA FileMan print option for the nursing ADP coordinator. ROUTINE: EN1^NURSFMU UPPERCASE MENU TEXT: PRINT FILE ENTRIES

> NAME: NURSFM-SEARCH MENU TEXT: Search File Entries TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: The VA FileMan search option for the nursing ADP coordinator. ROUTINE: EN2^NURSFMU UPPERCASE MENU TEXT: SEARCH FILE ENTRIES

> NAME: NURSLO-PRINT

> MENU TEXT: Print Existing Location File Entries

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION:

> This option generates one of three reports:

1.  A 80 column Status/Bed section report which also indicates if active staff are assigned to a nursing unit.
2.  A 80 column Budgeted FTEE report.
3.  A 132 column report which combines Status/Bed section information with Budgeted FTEE and staff assignment information. This report and the 80 column Status/Bed section report reflect any discrepancies in the old/ new bedsection assignments.

> ROUTINE: EN2^NURSAL0 TIMESTAMP: 55468,49767 UPPERCASE MENU TEXT: PRINT EXISTING LOCATION FILE E

> NAME: NURSPE-LOC/BED

> MENU TEXT: Location/Bed Section, Edit Nursing

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option permits the user to correct the patient's NURSING ward location and NURSING AMIS bed section. Although all patient transfers are to be initiated through the ADT option, a R.N. might need this nursing option if: (1) ADT is down or (2) the nursing location must be changed. The AMIS bed section must be updated to reflect accurate AMIS patient classification statistics.

> ROUTINE: EN1^NURSCPLE

> UPPERCASE MENU TEXT: LOCATION/BED SECTION, EDIT NUR

> NAME: NURSPE-MENU MENU TEXT: Patient Care Data, Enter/Edit TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: A primary menu containing options which edit clinical data. ITEM: NURAPC-MENU

> ITEM: NURSPE-VIT-MENU ITEM: NURSPE-LOC/BED ITEM: NURCPE-CARE ITEM: NURCPE-I/O-EDIT ITEM: NURCPE-EVAL

> TIMESTAMP: 56789,37720

> UPPERCASE MENU TEXT: PATIENT CARE DATA, ENTER/EDIT

> NAME: NURSPE-VIT-MENU

> MENU TEXT: Vitals/Measurements Data Entry Menu

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu contains options which permit users to enter vitals/measurements or to correct errors in the records.

> ITEM: NURCPE-VIT-EDIT DISPLAY ORDER: 1

> ITEM: NURCPE-VIT-ERROR DISPLAY ORDER: 2 TIMESTAMP: 56838,48355

> UPPERCASE MENU TEXT: VITALS/MEASUREMENTS DATA ENTRY

> NAME: NURSPP-HLTHSUM MENU TEXT: Health Summary Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This option allows user to print the Health Summary reports by Nursing ward, room-bed for the selected ward, or by patient.

> ROUTINE: EN1^NURCHSUM TIMESTAMP: 55609,35473 UPPERCASE MENU TEXT: HEALTH SUMMARY REPORT

> NAME: NURSPP-I/O-MENU

> MENU TEXT: Intake/Output Results Reporting

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the main menu for all patient intake and output reports.

> ITEM: NURCPP-I/O-SUM SYNONYM: 1 DISPLAY ORDER: 1

> ITEM: NURCPP-I/O-CURRENT SYNONYM: 2 DISPLAY ORDER: 2

> ITEM: NURCPP-I/O-48HRS SYNONYM: 3 DISPLAY ORDER: 3

> ITEM: NURCPP-I/O-SHIFT AND EVENT SYNONYM: 4 DISPLAY ORDER: 4

> ITEM: NURCPP-I/O-IVFLOW SYNONYM: 5 DISPLAY ORDER: 5

> TIMESTAMP: 56656,39543

> UPPERCASE MENU TEXT: INTAKE/OUTPUT RESULTS REPORTIN

> NAME: NURSPP-LOCIND

> MENU TEXT: Location of Individual Patient, Print

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Prints location of individual patient. ROUTINE: EN3^NURSCPLE

> UPPERCASE MENU TEXT: LOCATION OF INDIVIDUAL PATIENT

> NAME: NURSPP-LOCWRD MENU TEXT: Ward Census, Print

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Prints ward census by room/bed number.

> ROUTINE: EN2^NURSCPLC UPPERCASE MENU TEXT: WARD CENSUS, PRINT

> NAME: NURSPP-MENU MENU TEXT: Patient Care Data, Print TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: A primary menu containing options which print clinical data. ITEM: NURAPP-WRDCLAS SYNONYM: 1

> ITEM: NURAPP-UNCLOC SYNONYM: 5

> ITEM: NURSPP-VIT-MENU SYNONYM: 7

> ITEM: NURSPP-LOCIND SYNONYM: 2

> ITEM: NURSPP-LOCWRD SYNONYM: 4

> ITEM: NURCPP-CARE SYNONYM: 6

> ITEM: NURCPP-ASSWRK SYNONYM: 3

> ITEM: NURSPP-I/O-MENU SYNONYM: 8

> ITEM: NURSPP-SHIFT SYNONYM: 9

> ITEM: NURSPP-HLTHSUM SYNONYM: 10

> ITEM: NURCPP-VIT-SF511 SYNONYM: 11

> ITEM: NURCPP-I/O-SF511 SYNONYM: 12

> ITEM: NURCPP-EVAL SYNONYM: 13 TIMESTAMP: 56830,56534

> UPPERCASE MENU TEXT: PATIENT CARE DATA, PRINT

> NAME: NURSPP-SHIFT MENU TEXT: End of Shift Report TYPE: run routine CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This report contains patient problems, latest vitals and intake/output information for a selected nursing tour.

> ROUTINE: EN1^NURCES0 UPPERCASE MENU TEXT: END OF SHIFT REPORT

> NAME: NURSPP-VIT-MENU

> MENU TEXT: Vitals/Measurements Results Reporting

> TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This is the main menu for all vitals/measurements reports. ITEM: NURCPP-VIT-DISP SYNONYM: 1

> ITEM: NURCPP-VIT-WARD SYNONYM: 2

> ITEM: NURCPP-VIT-CUM SYNONYM: 3

> ITEM: NURCPP-VIT-ERROR SYNONYM: 4 TIMESTAMP: 56656,39508

> UPPERCASE MENU TEXT: VITALS/MEASUREMENTS RESULTS RE

> NAME: NURSPT-ACT

> MENU TEXT: Admit/Transfer Pt. (Nursing Pkg. Only)

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option can directly admit a patient into the Nursing System. It is to be used only in the event that the MAS System does not automatically admit a patient into the Nursing System.

> ROUTINE: EN2^NURSCPLE

> UPPERCASE MENU TEXT: ADMIT/TRANSFER PT. (NURSING PK

> NAME: NURSPT-INAC

> MENU TEXT: Inactivate/Disch. Pt. (Nursing Pkg. Only) TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Inactivates a patient's record from the Nursing System and tracks discharge time from ward. This option does not replace the ADT (MAS) function.

> ROUTINE: EN1^NURSCPLD

> UPPERCASE MENU TEXT: INACTIVATE/DISCH. PT. (NURSING

> NAME: NURSPT-WRDACT

> MENU TEXT: Ward Activation Patient Update

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option sets the ward patient care status and the status of all patients assigned to the ward to ACTIVE.

> ROUTINE: EN1^NURSCPLU

> UPPERCASE MENU TEXT: WARD ACTIVATION PATIENT UPDATE

> NAME: NURSPT-WRDINA

> MENU TEXT: Ward Deactivation Patient Update

> TYPE: run routine CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: This option sets the ward patient care status and the status of all patients assigned to the ward to INACTIVE.

> ROUTINE: EN2^NURSCPLU

> UPPERCASE MENU TEXT: WARD DEACTIVATION PATIENT UPDA

> NAME: NURSQ-MENU MENU TEXT: Quality Assurance TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Menu for Quality Assurance edits and print. ITEM: NURSQE-MENU SYNONYM: 1

> DISPLAY ORDER: 1

> TIMESTAMP: 56656,39515 UPPERCASE MENU TEXT: QUALITY ASSURANCE

> NAME: NURSQA-PR-MENU MENU TEXT: Quality Performance Reports TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: This menu contains the quality performance reports. ITEM: NURQA-PT-10PRINT

> ITEM: NURCRP-CP RANK LISTING

> TIMESTAMP: 56789,37782

> UPPERCASE MENU TEXT: QUALITY PERFORMANCE REPORTS

> NAME: NURSQE-MENU MENU TEXT: QI Data, Enter/Edit TYPE: menu CREATOR: POSTMASTER

> PACKAGE: NURSING SERVICE

> DESCRIPTION: A primary menu displaying options which edit quality assurance data.

> ITEM: NURSQE-REVCL-MENU ITEM: NURAAM-ACUEDT ITEM: NURAMN-MANED ITEM: NURQA-PT-MENU

> TIMESTAMP: 56789,37779 UPPERCASE MENU TEXT: QI DATA, ENTER/EDIT

> NAME: NURSQE-REVCL-MENU

> MENU TEXT: Review/Edit Patient Classification

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A menu for displaying special review/edit options related to patient classification. This option is appropriate for supervisors and nursing quality assurance staff.

> ITEM: NURAPC-REVIND ITEM: NURAPC-REVWRD

> TIMESTAMP: 56656,39499

> UPPERCASE MENU TEXT: REVIEW/EDIT PATIENT CLASSIFICA

> NAME: NURSQP-CLAS-MENU

> MENU TEXT: Classification Reports, Patient

> TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A menu displaying options for printing non-AMIS patient classification data in the QA Coordinator's Menu.

> ITEM: NURAPR-RES-INDCLAS ITEM: NURAPR-RES-WRDCLAS ITEM: NURAPR-RES-UNCLAS

> TIMESTAMP: 56830,56534

> UPPERCASE MENU TEXT: CLASSIFICATION REPORTS, PATIEN

> NAME: NURSQP-MENU MENU TEXT: Print Reports TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: A menu displaying all print options for the QA Coordinator's Menu.

> ITEM: NURSQP-CLAS-MENU SYNONYM: 1

> ITEM: NURSPP-LOCIND SYNONYM: 2

> ITEM: NURSPP-LOCWRD SYNONYM: 3

> ITEM: NURCRP-CP RANK LISTING SYNONYM: 4

> ITEM: NURQA-PT-10PRINT SYNONYM: 5

> TIMESTAMP: 56789,37798 UPPERCASE MENU TEXT: PRINT REPORTS

> NAME: NURSSP-MENU MENU TEXT: Special Functions TYPE: menu CREATOR: POSTMASTER PACKAGE: NURSING SERVICE

> DESCRIPTION: Main menu for options used to run backup routines, add/delete patients, etc., to the Nursing System. This group of options should be assigned to the nursing ADP coordinator and other individuals responsible for the operation of the Nursing Package.

> ITEM: NURAAM-ACUMAN SYNONYM: 4

> ITEM: NURSPT-ACT SYNONYM: 1

> ITEM: NURSPT-INAC SYNONYM: 2

> ITEM: NURAAM-UNC SYNONYM: 5

> ITEM: NURAAM-MD-UNC SYNONYM: 7

> ITEM: NURAMN-STA SYNONYM: 6

> ITEM: NURAMN-STA-LOC SYNONYM: 8

> ITEM: NURAED-BATSEP SYNONYM: 3

> ITEM: NURS-COMP SYNONYM: 9

> TIMESTAMP: 56999,56722 UPPERCASE MENU TEXT: SPECIAL FUNCTIONS

# Chapter 5 Cross-references

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a complete listing of all cross-references and triggers for the nursing software, regular cross-references are included.

> ANURS cross-reference of field .1 of the Patient file.

> When a patient is admitted through the MAS software, the set logic of this cross-reference triggers the patient into the NURS Patient file with a status of active. When a patient is discharged through the MAS software, the kill logic of this cross-reference sets the status of the patient in the NURS Patient file to inactive.

> NURS STAFF (210) FILE

> EMPLOYEE NAME

> NAME: B

> DESCRIPTION: This is the main index on the NURS STAFF file on the Employee Name Field.

> STATUS

> NAME: AC

> DESCRIPTION: This index is used to identify the employee's status.

> GRADE/STEP CODE

> NAME: D

> DESCRIPTION: This index is used to identify the employee's grade/step.

> NATIONAL CERTIFICATION (210.024) SUB-FILE

> NATIONAL CERTIFICATION NAME: B

> DESCRIPTION: This is the main index on the National Certification subfile.

> \*MANDATORY INSERVICE PROGRAM (210.05) SUB-FILE

> \*DATE ATTENDED

> NAME: B

> DESCRIPTION: This is the main index on the 'Date Attended' field of the Mandatory Inservice Program subfile.

> NAME: AA

> DESCRIPTION: This index is an inverted time/date cross reference on the date attended subfile.

> \*CLASS

> NAME: C

> DESCRIPTION: This is a regular index on the class field of the mandatory in service program subfile.

> NAME: AA1

> DESCRIPTION: This is an inverted time/date cross-reference on the Date Attended subfile which is used to identify the latest date the class was attended.

> FACULTY APPOINTMENT (210.08) SUB-FILE

> TYPE OF APPOINTMENT NAME: B

> DESCRIPTION: This is the main index on the 'Type of Appointment' subfile.

> \*CONTINUING EDUCATION PROGRAM (210.12) SUB-FILE

> \*CONTINUING EDUCATION PROGRAM NAME: B

> DESCRIPTION: This is the main index for the 'Continuing Education Program' subfile.

> EXPERIENCE (210.13) SUB-FILE

> PROFESSIONAL EXPERIENCE NAME: B

> DESCRIPTION: This is the main index on the 'Professional Experience' subfile.

POSITION ENTRY

NAME: APE

> DESCRIPTION: This is a regular index on the Position Entry field of the Professional Experience sub-field.

> DATE OF PROMOTION (210.17) SUB-FILE

DATE OF PROMOTION NAME: B

> DESCRIPTION: This is the main index on the Date field of the Date of Promotion subfile of the NURS STAFF File.

NAME: C

> DESCRIPTION: This X-ref is an inverted time/date cross reference on the date of promotion subfile so that the latest promotion date can be easily obtained.

> NPSB (210.18) SUB-FILE

> DATE PROFICIENCY IS DUE NAME: B

> DESCRIPTION: This is the main index on the Date Proficiency is Due field of the NPSB subfile.

> PRIVILEGES (210.19) SUB-FILE

> PRIVILEGES

> NAME: B

> DESCRIPTION: This is the main index on the 'Privileges' subfile.

> NURS PAY SCALE (211.1) FILE

> GRADE/STEP CODE

> NAME: B

> DESCRIPTION: This is the main index on the NURS PAY SCALE file which references all grade/step code entries.

> \*GRADE/STEP

> NAME: C

> DESCRIPTION: This is an index that references grade/step entries.

> \*NURS GRADE/STEP (211.2) FILE

> GRADE/STEP

> NAME: B

> DESCRIPTION: This is the main index on the NURS Grade/Step file. It lists all the grade/step entries in the file.

> NAME: AC

> DESCRIPTION: This index lists the categories of entries in the NURS Grade/Step file.

> NURS SERVICE POSITION (211.3) FILE

ABBREVIATION

NAME: B

> DESCRIPTION: This is the main index on the NURS Service Position file. It lists the abbreviations for all service positions.

> NAME

> NAME: C

> DESCRIPTION: This index is on the name field (service position titles).

> PRIORITY SEQUENCE NAME: D

> DESCRIPTION: This index is on the priority sequence field which lists priority sequence numbers used in printing reports.

> SERVICE CATEGORY

> NAME: AC

> DESCRIPTION: This index is on the service category field.

> OTHER SERVICE CATEGORY NAME: E

> DESCRIPTION: This is a regular index of the Other Service Category.

> NAME: F

> DESCRIPTION: This is a MUMPs index which will provide a list of Other Service Category entries in the Nurs Service Position (211.3) file.

PRODUCT LINE

NAME: P

> DESCRIPTION: This is a regular cross-reference on the Product Line field.

> NURS LOCATION (211.4) FILE

> NAME

> NAME: B

> DESCRIPTION: This is the main index on the name field of the NURS Location

> file.

PRODUCT LINE

NAME: P

> DESCRIPTION: This is a regular cross-reference on the Product Line field.

> PATIENT CARE FLAG NAME: D

> DESCRIPTION: This is an index on the 'Patient Care Status' field and indicates the active or inactive patient care status of the nursing location.

> MAS WARD

> NAME: C

> DESCRIPTION: This is an index on the 'MAS Ward' field which lists ward locations that are associated with the nursing location.

> AMIS BED SECTION

> NAME: ABS

> DESCRIPTION: This mumps index identifies the nursing AMIS bedsection that has been associated with this MAS ward location.

> AMIS BED SECTION

> NAME: ABS1

> DESCRIPTION: This mumps index indicates the nursing AMIS bedsection that has been associated with this nursing location.

> NURS CLINICAL BACKGROUND (211.5) FILE

> DESCRIPTION

> NAME: B

> DESCRIPTION: This is the main index on the NURS Clinical Background file and lists the entries in the description field (i.e., descriptions of professional experience).

> NURS TOUR OF DUTY (211.6) FILE

TOUR OF DUTY

NAME: B

> DESCRIPTION: This is the main index on the NURS Tour of Duty file which lists the tour of duty times.

> NURS AMIS POSITION (211.7) FILE

> AMIS NUMBER

> NAME: B

> DESCRIPTION: This is the main index on the NURS AMIS Position file which lists the AMIS number entries.

> NURS POSITION CONTROL (211.8) FILE

> LOCATION

> NAME: B

> DESCRIPTION: This is the main index on the NURS Position Control file which lists nursing locations in the Hospital Location file.

> NAME: AA1

> DESCRIPTION: This is a mumps index on the Position Control file which indicates the location and service category associated with the location.

> SERVICE CATEGORY

> NAME: AA2

> DESCRIPTION: This mumps index indicates the location and the nursing service category associated with the location.

> NAME: SC

> DESCRIPTION: This is a mumps index on the 'Service Category' field which indicates the service category associated with each location.

> OCCUPANCY/TRANSFERRED DATE (211.82) SUB-FILE

> START/TRANSFER DATE NAME: B

> DESCRIPTION: This is the main index on the 'Start/Transfer Date' field of the Occupancy/Transferred Date subfile.

> NAME: ASD1

> DESCRIPTION: This is a mumps index that identifies entries for activation to the Nursing Acuity/Separation-Activation Run.

> NAME: ASDT

> DESCRIPTION: This mumps index is used to identify the starting date of all employee assignments.

> NAME: AA1

> DESCRIPTION: This mumps index identifies the employee, start/transfer date, and service position associated with each position control entry.

> EMPLOYEE

> NAME: C

> DESCRIPTION: This mumps index identifies the employee associated with each position control entry.

> NAME: C

> DESCRIPTION: This mumps index identifies the employees assigned to a location.

> NAME: ADAE

> DESCRIPTION: This mumps index identifies the primary service position and primary assignment for an employee.

> NAME: ASDT1

> DESCRIPTION: This mumps index identifies entries that are to be activated by the Nursing Acuity/Separation-Activation Run.

> NAME: AA2

> DESCRIPTION: This mumps index identifies position control file entries by employee, start/transfer date, and service position.

> SERVICE POSITION

> NAME: AD

> DESCRIPTION: This mumps index identifies position control entries by employee, and service position.

> NAME: AA3

> DESCRIPTION: This mumps index identifies position control entries by start/ transfer date, employee, and service position.

> NAME: APE

> DESCRIPTION: This mumps xref is used to update the experience multiple in the staff file by the Nursing Acuity/Separation-Activation Run.

> VACANCY DATE

> NAME: ASD2

> DESCRIPTION: This mumps index is used to identify entries that are to be deactivated by the Nursing Acuity/Separation-Activation Run.

> VACANCY REASON

> NAME: ASD3

> DESCRIPTION: This mumps index is used by the Nursing Acuity/Separation-Activation Run to update the experience multiple in the NURS Staff file with vacancy reason information when an assignment is deactivated.

> PRIMARY ASSIGNMENT NAME: AE

> DESCRIPTION: This mumps index is used to identify an employee's primary assignment.

> POSITION BUDGETED (211.83) SUB-FILE

> SERVICE POSITION NAME: B

> DESCRIPTION: This is the main index on the 'Service Position' field of the Budgeted Position subfile.

> NURS VACANCY/TRANSFERRED REASONS (211.9) FILE

> CODE

> NAME: B

> DESCRIPTION: This is the main index on the 'Code' field in the NURS Vacancy/

> Transferred Reasons file.

> DESCRIPTION

> NAME: C

> DESCRIPTION: This index is on the 'Description' field of the NURS Vacancy/ Transferred Reason file.

> NURS EDUCATION (212.1) FILE

> EDUCATION DESCRIPTION NAME: B

> DESCRIPTION: This is the main index on the NURS Education file and lists educational degree descriptions.

NURSING CODE

NAME: C

> DESCRIPTION: This index is on the 'Nursing Code' field and lists the code associated with an educational degree.

> NURS CERTIFICATION (212.2) FILE

ABBREVIATION

NAME: B

> DESCRIPTION: This is the main index of the NURS Certification file which lists certification abbreviations.

> NAME OF CERTIFICATION NAME: C

> DESCRIPTION: This index is on the 'Name of Certification' field.

> NURS COLLEGE MAJOR (212.3) FILE

> COLLEGE MAJOR DESCRIPTION NAME: B

> DESCRIPTION: This is the main index on the 'College Major Description' field of the NURS College Major file.

> \*NURS MANDATORY INSERVICE (212.4) FILE

> CLASS NAME

> NAME: B

> DESCRIPTION: This is the main index on the 'Class Name' field of the NURS Mandatory Inservice file.

REVIEW GROUP

NAME: C

> DESCRIPTION: This is the main index on the 'Review Group' field of the Review Group subfile.

> \*NURS MI CLASS GROUP (212.42) FILE

> NAME

> NAME: B

> DESCRIPTION: This is the main index on the 'Name' field of the NURS MI Class

> Group file.

> NURS PRIVILEGE (212.6) FILE

> NAME

> NAME: B

> DESCRIPTION: This in the main index on the 'Name' field of the NURS Privilege

> file.

> NURS PRODUCT LINE (212.7) FILE

> NAME

> NAME: B

> DESCRIPTION: This is the main index on the 'Name' field of the NURS Product Line

> file.

> \*NURS AMIS 1106 CLASS (213.1) FILE

> \*DATE/BED SECTION/WARD NAME: B

> DESCRIPTION: This is the main index on the 'Date/Bed Section/Ward' field of the NURS AMIS 1106 Class file.

> NAME: MON

> DESCRIPTION: This mumps index identifies monthly entries in the NURS AMIS 1106 Class file.

> NAME: QUA

> DESCRIPTION: This mumps index identifies yearly entries in the NURS 1106 AMIS Class file.

> NAME: MT

> DESCRIPTION: This mumps index purges monthly entries from the NURS AMIS 1106 Class file.

> NAME: QT

> DESCRIPTION: This mumps index purges quarterly entries for the NURS AMIS 1106 Class file.

> NAME: ABED

> DESCRIPTION: This mumps index sets nursing bedsection data in the NURS AMIS 1106 Class file.

> NAME: AWRD

> DESCRIPTION: This mumps index sets nursing location data in the NURS AMIS 1106 Class file.

> NAME: ARPT

> DESCRIPTION: This mumps index enters the report date into the NURS AMIS 1106 Class file.

> NAME: AWL

> DESCRIPTION: This mumps index indicates whether or not there are workload factors available for this entry.

> NAME: YR

> DESCRIPTION: This mumps index identifies yearly entries in the NURS AMIS 1106 Class file.

> NURS AMIS 1106B FTEE (213.2) FILE

> FACILITY

> NAME: B

> DESCRIPTION: This is the main index on the 'FACILITY' field of the NURS AMIS 1106B FTEE file.

> NURS AMIS WARD (213.3) FILE

> BED SECTION

> NAME: B

> DESCRIPTION: This is the main index on the 'Bed Section' field of the NURS AMIS Ward file.

> NURS AMIS 1106 MANHOURS (213.4) FILE

> DATE/SHIFT/WARD

> NAME: B

> DESCRIPTION: This is the main index on the 'Date/Shift/Ward' field of the NURS AMIS 1106 Manhours file.

> NAME: AMON

> DESCRIPTION: This mumps index identifies monthly entries in the NURS AMIS 1106B Manhours file by month and year.

> NAME: AQUA

> DESCRIPTION: This mumps index identifies quarterly entries in the NURS AMIS 1106 Manhours file by quarter and year.

> NAME: AYR

> DESCRIPTION: This mumps index identifies entries in the NURS AMIS 1106 Manhours file by year.

> ACUITY (213.41) SUB-FILE

> ACUITY BED SECTION NAME: B

> DESCRIPTION: This is the main index on the 'Acuity bed Section' field of the Acuity subfile in the NURS 1106 Manhours file.

> NURS AMIS DAILY EXCEPTION REPORT (213.5) FILE

> DATE

> NAME: B

> DESCRIPTION: This is the main index on the 'Date' field of the NURS Exception

> Report file.

> AMIS TYPE

> NAME: E

> DESCRIPTION: This index indicates the type of AMIS totals (3 PM or Midnight) that this entry references.

> PATIENT

> NAME: C

> DESCRIPTION: This index indicates the name of the unclassified patient referenced by this time/date.

> NURS LOCATION

> NAME: D

> DESCRIPTION: This index indicates the location where the patient was not classified on a specific time/date.

> STAFF EMPLOYEE (213.52) SUB-FILE

> STAFF EMPLOYEE

> NAME: B

> DESCRIPTION: This is the main index on the 'Staff Employee' field of the Staff Employee subfile in the NURS AMIS Daily Exception Report file.

> NURS PARAMETERS (213.9) FILE

> NAME

> NAME: B

> DESCRIPTION: This is the main index on the 'Name' field of the NURS Parameters

> file.

> \*MANHOURS BATCH JOB STATUS (213.9003) SUB-FILE

> \*DATE

> NAME: B

> DESCRIPTION: This is the main index on the date field of the Manhours Batch Job Status sub-field.

> NURS PATIENT (214) FILE

> NAME

> NAME: B

> DESCRIPTION: This is the main index on the 'Name' field of the NURS Patient file.

> ADMISSION STATUS

> NAME: AZ1

> DESCRIPTION: This mumps index identifies all active patients in the NURS Patient file.

> NAME: C

> DESCRIPTION: This is an index on the 'Status' field in the NURS Patient file.

> NURS LOCATION

> NAME: E

> DESCRIPTION: This index is on the 'NURS Location' field of the NURS Patient file.

> NAME: AF

> DESCRIPTION: This mumps index identifies active records in the NURS Patient file by patient name and NURS Location.

> NURS CLASSIFICATION (214.6) FILE

> CLASSIFICATION DATE/TIME NAME: B

> DESCRIPTION: This is the main index on the 'Classification Date/Time' field of the NURS Classification file.

> NAME: AZ1

> DESCRIPTION: This mumps index is an inverted time/date index which make the latest classification the first one accessed by sorting through this index.

> NAME: AZ2

> DESCRIPTION: This index separates true classification entries from DOM, hemodialysis, and recovery room counts.

> NAME

> NAME: C

> DESCRIPTION: This index is on the 'Name' field in the NURS Classification file.

> NAME: AA

> DESCRIPTION: This mumps index identifies the latest patient classification by name and date/time.

> NURS LOCATION

> NAME: E

> DESCRIPTION: This index is on the 'NURS Location' field in the NURS Classification file.

> NAME: AZ4

> DESCRIPTION: This mumps index separates DOM, Hemodialysis, and Recovery Room counts, from regular classification entries.

> COUNT

> NAME: AZ3

> DESCRIPTION: This mumps index separates the Hemodialysis and Recovery Room counts from regular classification entries.

> NURS REVIEW CLASSIFICATION (214.7) FILE

> REVIEW DATE/TIME NAME: B

> DESCRIPTION: This is the main index on the 'Review Date/Time' field of the NURS Review Classification file.

> NAME: AZ1

> DESCRIPTION: This mumps index is an inverted time/date index which make the latest entry reviewed the first entry accessed when using this index.

> NAME

> NAME: C

> DESCRIPTION: This index is on the 'Name' field in the NURS Review Classification

> file.

> NAME: AZ2

> DESCRIPTION: This mumps index make the latest review entry available by patient name, NURS Location, and review date/time.

> CLASSIFICATION REVIEWED NAME: AA

> DESCRIPTION: This mumps index indicates the review date/time of the latest classification for this patient.

> NURS CARE PLAN (216.8) FILE

> TEXT FILE ENTRY

> NAME: B

> DESCRIPTION: This is the main cross-reference on the Text File Entry field.

> NURSING PROBLEM LIST (216.81) SUB-FILE

> PROBLEM

> NAME: B

> DESCRIPTION: This is the main cross-reference on the problem field.

> EVALUATION DATE (216.82) SUB-FILE

> DATE/TIME ENTERED NAME: B

> DESCRIPTION: This is the main cross-reference evaluation date field.

> NAME: AA

> DESCRIPTION: This is an inverted time/date mumps cross-reference on the date field.

> NAME:

> DESCRIPTION: This cross-reference triggers an entry into the User Who Evaluated field of the Evaluation Date sub-file in the Nurs Care Plan (#216.8) file when the evaluation date is edited.

> PROBLEM

> NAME: AA1

> DESCRIPTION: This is an inverted time/date mumps cross-reference on the Problem field.

> TARGET DATE (216.83) SUB-FILE

> DATE/TIME ENTERED NAME: B

> DESCRIPTION: This is the main cross-reference on the Target date field.

> NAME: AA1

> DESCRIPTION: This is an inverted time/date mumps cross-reference on the Target Date field.

> NAME:

> DESCRIPTION: This cross-reference triggers and entry into the User Who Entered field of the Target Date sub-file in the Nurs Care Plan (#216.8) file when the Target Date field is edited.

> GOAL/EXPECTED OUTCOME NAME: AA2

> DESCRIPTION: This is an inverted time/date cross-reference on the goal/expected outcome field.

> ORDER INFO (216.84) SUB-FILE

> ORDER STATUS DATE/TIME NAME: B

> DESCRIPTION: This is the main cross-reference on the Order Status Date/Time field.

> NAME: AA

> DESCRIPTION: This is an inverted time/date mumps cross-reference on the Order Status Date/Time field.

> NAME:

> DESCRIPTION: This cross-reference triggers and entry into the User Modifying field of the Order Info sub-file in the NURS Care Plan (#216.8) file whenever the Order Status Date/Time field is edited.

> ORDERABLE

> NAME: AA1

> DESCRIPTION: This is an inverted time/date mumps cross-reference on the Orderable field.

> NURQ QI SUMMARY (217) FILE

> SURVEY

> NAME: B

> DESCRIPTION: This is the main cross-reference on the Survey field.

> LOCATION (217.04) SUB-FILE

> LOCATION

> NAME: B

> DESCRIPTION: This is the main cross-reference on the Location field.

> IMPORTANT FUNCTIONS (217.42) SUB-FILE

> IMPORTANT FUNCTIONS NAME: B

> DESCRIPTION: This is the cross-reference on the Important Functions field.

> STANDARDS OF CARE (217.421) SUB-FILE

> STANDARDS OF CARE NAME: B

> DESCRIPTION: This is the cross-reference on the Standards of Care field.

> STANDARDS OF PRACTICE (217.422) SUB-FILE

> STANDARDS OF PRACTICE NAME: B

> DESCRIPTION: This is the cross-reference on the Standards of Practice field.

> PERFORMANCE MEASURE (217.43) SUB-FILE

> PERFORMANCE MEASURE NAME: B

> DESCRIPTION: This is the main cross-reference on the Performance Measure field.

> NAME: F

> DESCRIPTION: This xref returns the entry in the Questions (.02) multiple of the QA Questions (#748.25) file.

> RATIONALE (217.431) SUB-FILE

> RATIONALE

> NAME: B

> DESCRIPTION: This is the cross-reference on the Rationale field.

> RECEIVER OF RESULTS (217.08) SUB-FILE

> RECEIVER OF RESULTS NAME: B

> DESCRIPTION: This is the cross-reference on the Receiver of Results field.

> NURQ STANDARDS OF CARE/PRACTICE (217.1) FILE

> NAME OF STANDARD NAME: B

> DESCRIPTION: This is the main cross-reference on the Name of Standard field.

> TYPE OF STANDARD NAME: C

> DESCRIPTION: This is the cross-reference on the Type of Standard field.

> NURQ RATIONALE (217.2) FILE

> RATIONALE

> NAME: B

> DESCRIPTION: This is the main cross-reference on the Rationale field.

> NURQ FREQUENCY (217.3) FILE

> FREQUENCY

> NAME: B

> DESCRIPTION: This is the main cross-reference on the Frequency field.

> \*NURS CONVERSION NAME CHANGE (219.7) FILE

> OLD NAME

> NAME: B

> DESCRIPTION: This is the main index on the Old Name field of the NURS Conversion Name Change file.

> TYPE

> NAME: C

> DESCRIPTION: This is a regular index on the type field of the NURS Conversion

> Name Change file.

# Chapter 6 Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Four types of data are currently archived/purged in Version 4.0 of the nursing software:

1.  Data in the \*NURS AMIS 1106 Class (#213.1) file, contains daily acuity counts that will be purged as follows:

> Presently the data in this file is of three types; daily, monthly, and quarterly. Daily data is retained for 30 days, monthly data is kept for four months, and quarterly is kept for five quarters. Purged data will be added to the next higher level of data.

2.  Data listed in the NURS AMIS Daily Exception Report file (#213.5) will be kept for 30 days. Data that is older than 30 days will be purged by the Nursing system.
3.  Data in the NURS Classification (#214.6) file and NURS Review Classification (#214.7) file should be kept on line for at least six months before purging.
4.  Data in the NURS AMIS 1106 Manhours (#213.4) file should be kept for at least three years before purging.

> Two determinations on what will be included as archiving in future releases have been included:

1.  For the NURS Staff file (#210), archiving will be based on the fiscal year; data will be kept for three years. All employees who leave within the first six months of the fiscal year will be included in the archiving data for that fiscal year. However, for those employees leaving Nursing Service after the first six months of the fiscal year, data will be carried over for the following fiscal year.
2.  For the NURS Patient file (#214), NURS Care Plan file (#216.8) data will be maintained for a time period of up to six months following the patient's discharge date.

# Chapter 7 Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no callable routines in the nursing software.

# Chapter 8 External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following external package relationships are necessary for Nursing Version 4.0 to fully function.
    1.  Kernel Version 8.0 or greater.
    2.  VA FileMan Version 21 or greater.
    3.  PIMS Version 5.3 or greater.
    4.  Kernel Toolkit Version 7.3 or greater.
    5.  PAID Version 4.0 or greater.
    6.  Vitals/Measurements Version 4.0 .
    7.  Intake and Output Version 4.0.
    8.  Text Generator Version 3.0.
    9.  Dietetics Version 4.6 or greater.
    10. Health Summary Version 2.7 or greater.
2.  Other Package Agreements:

> DBIA's where the Nursing package is the subscriber:

> 510 NAME: DISV

> CUSTODIAL PACKAGE: VA FILEMAN San Francisco SUBSCRIBING PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> READ access allowed.

> WRITE access allowed in routines ORGUEM, and ORUS1. An example of a set is S

> ^DISV(DUZ,"^ORD(101,")=+ORGMENU

> DELETE access allowed in ORUS1.

> UNWINDER Salt Lake City

> The Unwinder uses ^DISV(DUZ,"XQORM") to store the items that were selected for spacebar recall.

> READ and WRITE access to ^DISV(DUZ,"XQORM") allowed.

> LAB SERVICE Dallas

> Laboratory V 5.2 uses ^DISV(DUZ,"LRACC") and

> ^DISV(DUZ,"LRAN") to store items.

> An example is in routine LRACC at line LRACC+4: S:\$L(X)\>2 ^DISV(DUZ,"LRACC")=X S:X=" " X=\$S(\$D(^DISV(DUZ,"LRACC")): ^("LRACC"),1:"?")

> READ and WRITE access to ^DISV(DUZ,"LRACC") and

> ^DISV(DUZ,"LRAN" allowed.

> PROGRESS NOTES Salt Lake City READ access allowed.

> DISCHARGE SUMMARY Salt Lake City READ access allowed.

> HEALTH SUMMARY Salt Lake City READ access allowed.

> WRITE and DELETE access is allowed in routine GMTSORU1. An example of a set follows:

> \>\>\>\>\>GMTSORU1+8 W " " S ORTAB=\$X,J=1 I Y\>0 K

> ^DISV(DUZ,ORUS) D SDISV S ^DISV(DUZ,ORUS,0)=X,I =0 F

> J=1:1 S I=\$O(Y(I)) Q:I="" S X=\$P(Y(I),"^",3),^DISV(DUZ,ORUS)=+Y(I),^DISV(D

> UZ,ORUS,J)=X W:(\$X+\$L(X))\>(IOM-4) !?ORTAB W X," "

> CONSULT/REQUEST TR Salt Lake City READ access allowed.

> IFCAP Washington

> READ access allowed. The inventory package V5 uses the global ^DISV(DUZ,"PRCProutine name", and

> ^DISV(DUZ,globalnode, to allow the user to press the space bar to select the last response.

> WRITE access allowed. The reference to

> ^DISV(DUZ,"PRCProutine", is used to store non-fileman responses to the reader.

> NURSING SERVICE Chicago

> Read access "Till Otherwise Agreed". QUASAR Birmingham

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT: DISV(

> DESCRIPTION: TYPE: File

> Used to process 'space-bar return' on user input.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 916 NAME: DBIA916

> CUSTODIAL PACKAGE: VA FILEMAN San Francisco SUBSCRIBING PACKAGE: LAB SERVICE Dallas

> For duration of Lab Version 5.2: Blood Bank and Anatomic Pathology namespaced routines refer to

> ^DIC(FILE_NO.,0,"GL") to locate global nodes for data.

> INCOME VERIFICATIO Albany

> IVM stores a pointer to the FILE (#1) file in order to reference multiple files for storing data. We are requesting permission to make a direct reference to

> ^DIC(FILE_NO.,0,"GL") to find the global root for that file.

> NURSING SERVICE Chicago

> Nursing is granted READ access to

> ^DIC(file_number,0,"GL") in order to get the global root of a file. File_number is in the nursing package namespace.

> CLINICAL LEXICON U Salt Lake City

> Read only access for ^DIC(FN,0,"GL"), where FN is a file number, to verify the value of DIC prior to initiating the lookup (GMPTA4).

> POLICE & SECURITY Dallas

> DICRW+5^ESPFM, the reference to ^DIC(+Y,0,"GL") USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: VERSION: Fileman 20 FILE: ROOT: DIC(

> DESCRIPTION: TYPE: File

> GLOBAL REFERENCE:

> ^DIC(FILE_NO.,0,"GL")

> 1 GLOBAL NAME Direct Global Read

> A direct global read is performed on this node to determine the global root for a file.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 938 NAME: DBIA938

> CUSTODIAL PACKAGE: HEALTH SUMMARY Salt Lake City SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Entry points to use the Health Summary routine GMTSDVR to allow users to print a Health Summary.

> ROUTINE: GMTSDVR COMPONENT: ENX

> VARIABLES: DFN Input

> GMTSTYP Input

> GMTSPX2 Input

> GMTSPX1 Input

> Passes patient id.

> Defines the Health Summary report to be printed.

> Optional internal FileMan date for beginning date range.

> Optional internal FileMan date for ending date range.

> This entry point allows for direct printing of a Health Summary for a programmer-specified patient and device, without prompting for additional information. This entry point uses parameter passing. The format is ENX^GMTSDVR(DFN,GMTSTYP,GMTSPX2,GMTSPX1). GMTSPX2 and

> GMTSPX1 are optional date range variables. They allow the time limits to be overridden for components that use time limits. Thus, beginning and ending dates can be specified in order to get only data within that time range.

> COMPONENT: ENXQ

> VARIABLES: DFN Input

> GMTSTYP Input

> GMTSPX1 Input

> GMTSPX2 Input

> Patient ID.

> Defines Health Summary to print.

> Optional internal FileMan date for ending date range.

> Optional internal FileMan date for beginning date range.

> This call is for Queueing the Health Summary. GMTSPX1 and GMTSPX2 are optional date range variables. Both are required if a date range is desired.

> COMPONENT: SELTYP

> VARIABLES: GMTYP(0) Output

> GMTYP(1) Output

> Will be set to 1 if a type is selected and it contains components.

> The 1st piece will be set to the internal value of the health summary type. The 2nd piece will be set to the name of the health summary type.

> This entry point allows for a Health Summary type to be selected from file 142.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1376 NAME: NEW PERSON

> CUSTODIAL PACKAGE: KERNEL San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 200 ROOT: VA(200, DESCRIPTION: TYPE: File

> Nursing can access the New Person file as described in this DBIA.

> ^VA(200,D0,0)

> .01 NAME 0;1 Write w/Fileman

> Also LAYGO with FileMan and pointed to from Nurs Staff

> \(210\) file. This LAYGO access can be turned off by a site parameter in the Nursing software.

> Nursing also points to this file from the Employee Name (.01) field of the Nurs Staff

> \(210\) file. This pointer uses a DINUM relationship.

> ^VA(200,D0,1)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>SEX</p>
</blockquote></th>
<th>1;2</th>
<th>Write</th>
<th><blockquote>
<p>w/Fileman</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td>1;3</td>
<td>Write</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td>1;9</td>
<td>Write</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ^VA(200,D0,.11)

111. STREET ADDRESS 1 .11;1 Write w/Fileman
112. STREET ADDRESS 2 .11;2 Write w/Fileman
113. STREET ADDRESS 3 .11;3 Write w/Fileman
114. CITY .11;4 Write w/Fileman
115. STATE .11;5 Write w/Fileman
116. ZIP CODE .11;6 Write w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1377 NAME: WARD LOCATION

> CUSTODIAL PACKAGE: REGISTRATION Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 42 ROOT: DIC(42, DESCRIPTION: TYPE: File

> Nursing and Vitals/Measurements can access the Ward Location (42) file fields/cross-references as described in this DBIA.

> ^DIC(42,D0,

> .03 SERVICE 0;3 Direct Global Read

> Direct global access on the "B" cross-reference of the Ward Location

> \(42\) file is supported by this DBIA. ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1378 NAME: DGPM

> CUSTODIAL PACKAGE: REGISTRATION Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 405 ROOT: DGPM( DESCRIPTION: TYPE: File

> Nursing directly references the ^DGPM global. We would like permission to reference the following fields/cross-references using direct global reads:

1.  DATE/TIME
2.  TRANSACTION
3.  PATIENT

> .06 WARD LOCATION

> .14 ADMISSION/CHECK-IN MOVEMENT

> "AMV3" cross-reference "APMV" cross-reference "ATID1" cross-reference "ATID2" cross-reference "ATID3" cross-reference

> "CN" cross reference

> ^DGPM(D0,0)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 37%" />
<col style="width: 15%" />
<col style="width: 27%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>DATE/TIME</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct Global</th>
<th><blockquote>
<p>Read</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.02</p>
</blockquote></td>
<td><blockquote>
<p>TRANSACTION</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.06</p>
</blockquote></td>
<td><blockquote>
<p>WARD LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>0;6</p>
</blockquote></td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.14</p>
</blockquote></td>
<td><blockquote>
<p>ADMISSION/CHECK-IN</p>
</blockquote></td>
<td><blockquote>
<p>M 0;14</p>
</blockquote></td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ^DGPM('AMV3',

> Direct global read to the "AMV3" cross-reference.

> ^DGPM('APMV',

> Direct global read to the "APMV" cross-reference.

> ^DGPM('ATID1',

> Direct global read to the "ATID1" cross-reference.

> ^DGPM('ATID2',

> Direct global read to the "ATID2" cross-reference.

> ^DGPM('ATID3',

> Direct global read to the "ATID3" cross-reference.

> ^DGPM('CN',

> Direct global read to the "CN" cross-reference.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1380 NAME: ROOM-BED

> CUSTODIAL PACKAGE: REGISTRATION Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 405.4 ROOT: DG(405.4, DESCRIPTION: TYPE: File

> Nursing, Vitals/Measurements and Intake/Output have permission to access the following elements in the Room-Bed (405.4) file.

> ^DG(405.4,0) to test for existence of file. "W" cross-reference

> Direct global read of the NAME (.01) field.

> ^DG(405.4,0)

> Direct global reference of this node to check for existence of Room-Bed (405.4) file.

> ^DG(405.4,D0,0)

> .01 NAME 0;1 Direct Global Read

> ^DG(405.4,'W',

> Direct global read on the "W" cross-reference.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1381 NAME: GMRV VITAL MEASUREMENT

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 120.5 ROOT: GMR(120.5, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRV Vital Measurement (120.5) file.

> ^GMR(120.5,D0,0)

> .01 DATE/TIME VITALS TAK 0;1 Direct Global Read

> 2.1 RATE 0;8 Direct Global Read

> ^GMR(120.5,D0,2)

> 2 ENTERED IN ERROR 2;1 Direct Global Read

> ^GMR(120.5,'AA',

> Direct global read on the "AA" cross-reference.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1382 NAME: GMRV VITAL TYPE

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 120.51 ROOT: GMRD(120.51, DESCRIPTION: TYPE: File

> Nursing has permission to access the GMRV Vital Type (120.51) file.

> ^GMRD(120.51,D0,0)

> .01 NAME 0;1 Direct Global Read

> ^GMRD(120.51,'C',

> Direct global read on the "C" cross-reference.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1385 NAME: BRANCH OF SERVICE

> CUSTODIAL PACKAGE: REGISTRATION Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 23 ROOT: DIC(23, DESCRIPTION: TYPE: File

> Nursing has permission to access the Branch of Service (23) file as described in this DBIA.

> ^DIC(23,D0,0)

> .01 NAME 0;1 Direct Global Read

> Nursing also has permission to point to this file from the Military Status multiple in the Nurs Staff (210) file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1386 NAME: GMRG PARAMETERS

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 124.1 ROOT: GMRD(124.1, DESCRIPTION: TYPE: File

> Nursing has permission to access the GMRG Parameters (124.1) file fields described in this DBIA.

> ^GMRD(124.1,D0,1,D1,0)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>PACKAGE PARAMETERS</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct</th>
<th>Global</th>
<th><blockquote>
<p>Read</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>HIGHLIGHTING OFF</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ^GMRD(124.1,D0,1,D1,'P')

> 1 PRINT ROUTINE P;E1,245 Direct Global Read

> ^GMRD(124.1,D0,1,'B',

> Direct global read to "B" cross-reference on Package Parameters sub-file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1387 NAME: AGGREGATE TERM

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 124.2 ROOT: GMRD(124.2, DESCRIPTION: TYPE: File

> Nursing has permission to access the Aggregate Term (124.2) file fields described in this DBIA.

> ^GMRD(124.2,D0,0)

> ^

> ^GMRD(124.2,D0,1,'AC',

> Direct global read on the "AC" cross-reference of the Children sub-file.

> ^GMRD(124.2,D0,1,'B',

> Direct global read on the "B" cross-reference of the Children sub-file.

> ^GMRD(124.2,'AA',

> Direct global read on the "AA" cross-reference of the Aggregate Term (124.2) file.

> ^GMRD(124.2,'AKID',

> Direct global reference on the "AKID" cross-reference of the Aggregate Term (124.2) file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1388 NAME: TERM CLASSIFICATION

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 124.25 ROOT: GMRD(124.25, DESCRIPTION: TYPE: File

> Nursing has permission to access the Term Classification (124.25) file fields described in this DBIA.

> ^GMRD(124.25,'AA',

> Direct global reference on the "AA" cross-reference of the Term Classification file.

> ^GMRD(124.25,'B',

> Direct global reference on the "B" cross-reference of the Term Classification file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1389 NAME: GMR TEXT

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 124.3 ROOT: GMR(124.3, DESCRIPTION: TYPE: File

> Nursing has permission to access the GMR Text (124.3) file fields described in this DBIA.

> ^GMR(124.3,D0,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 40%" />
<col style="width: 11%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>TEXT BLOCK</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct Global Read</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.03</p>
</blockquote></td>
<td><blockquote>
<p>DATE CREATED</p>
</blockquote></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>AUTHOR</p>
</blockquote></td>
<td><blockquote>
<p>0;5</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>ENTERED IN ERROR</p>
</blockquote></td>
<td><blockquote>
<p>5;1</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5.1</p>
</blockquote></td>
<td><blockquote>
<p>DATE ENTERED IN ERRO</p>
</blockquote></td>
<td><blockquote>
<p>5;2</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5.2</p>
</blockquote></td>
<td><blockquote>
<p>USER ENTERING IN ERR</p>
</blockquote></td>
<td><blockquote>
<p>5;3</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
</tbody>
</table>

> Nursing can point to this file from the Nurs Care Plan (216.8) file. Nursing can access the ^GMR(124.3,D0,0) node to lock/unlock a record in the GMR Text (124.3) file.

> Nursing can access the "AA" cross-reference on the GMR Text file using direct global reads.

> ^GMR(124.3,D0,1,D1,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 40%" />
<col style="width: 12%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>SELECTION</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct Global Read</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>APPENDED/INTERNAL TE</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>ADDITIONAL TEXT</p>
</blockquote></td>
<td><blockquote>
<p>ADD;1</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
</tbody>
</table>

> Also direct global reads are supported for the "ALIST" and "B" cross-references of the Selection sub-file are supported.

> ^GMR(124.3,D0,1,D1,2,D2,

> .01 AUDIT TRAIL DATE/TIM 0;1 Direct Global Read

1.  MODIFICATION 0;2 Direct Global Read
2.  USER WHO MODIFIED 0;3 Direct Global Read

> Also a direct global read to the "AA" cross-reference of the Audit Trail sub-file is supported.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1390 NAME: GMRY PATIENT I/O FILE

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126 ROOT: GMR(126, DESCRIPTION: TYPE: File

> Nursing has permission to access the GMRY Patient I/O File (126) file fields described in this DBIA.

> ^GMR(126,D0,

> Direct global read on "B" cross-reference of GMRY Patient I/O File is supported.

> LAYGO is allowed to this file using a ^DIC lookup.

> ^GMR(126,D0,'IVM',D1,

> Direct global reference on the "B" cross-reference of the IV Maintenance sub-file is supported.

> ^GMR(126,D0,'IVM',D1,1,D2,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 40%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>MAINTENANCE DATE/TIM</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct</th>
<th>Global</th>
<th><blockquote>
<p>Read</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>SITE DESCRIPTION</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>TUBING CHANGED</p>
</blockquote></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>DRESSING CHANGED</p>
</blockquote></td>
<td><blockquote>
<p>0;4</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>ENTERED BY</p>
</blockquote></td>
<td><blockquote>
<p>0;5</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>SITE DC'ED</p>
</blockquote></td>
<td><blockquote>
<p>0;6</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Direct global reads of the "B" and "C" cross-references of the Maintenance sub-file are also supported.

> ^GMR(126,0)

> Direct global read to test for existence of the file is supported.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1391 NAME: GMRY NUR SHIFT/OTHER

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.95 ROOT: GMRD(126.95, DESCRIPTION: TYPE: File

> Nursing and Vitals/Measurements have permission to access the GMRY NUR Shift/Other file fields described in this DBIA.

> ^GMRD(126.95,D0,

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 28%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>NIGHT</p>
</blockquote></th>
<th>1;1</th>
<th>Direct Global</th>
<th><blockquote>
<p>Read</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DAY</p>
</blockquote></td>
<td>1;2</td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>EVENING</p>
</blockquote></td>
<td>1;3</td>
<td>Direct Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1394 NAME: GMRGED0

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to access the GMRGED0 routines as described in this DBIA.

> ROUTINE: GMRGED0 COMPONENT: EN3

> VARIABLES: DFN Input

> GMRGPDA Input

> GMRGRT Input

> GMRGOUT Output

> Patient file IEN.

> Entry in GMR Text (124.3) file of data to be edited.

> A two piece variable in format A^B, where A is the Aggregate Term (124.2) file IEN for prime document to be edited, i.e., Nursing Care Plan, and B is the text representation of the prime document.

> A flag indicating whether the user abnormally exited the input process, i.e., time-out or ^-out. 0 indicates normal processing, 1 indicates abnormal exit.

> This entry point allows the user to edit a Nursing Care Plan for a specified patient.

> COMPONENT: Q3

> VARIABLES: This entry cleans up variables used by the enter/edit patient data process of the Text Generator.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1395 NAME: GMRYED1

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to access the entry points described in this DBIA for the GMRYED1 routine.

> ROUTINE: GMRYED1 COMPONENT: INPUT

> VARIABLES: DFN Input

> GNUROP Input

> GMRHLOC Input

> GMROUT Both

> Patient IEN.

> Type of Input/Output/IV. Hospital Location file pointer.

> Switch that is set to 0 and returned if abnormal user exit.

> Allows user to enter/edit patient intake.

> COMPONENT: OUTPUT

> VARIABLES: DFN Input

> GNUROP Input

> GMRHLOC Input

> GMROUT Both

> Patient IEN.

> Type of data Input/Output/IV. Hospital Location (44) pointer.

> Switch to determine if user abnormally exits. Passed in with value of 0.

> Allows user to enter/edit patient Output.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1396 NAME: GMRYRP0

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to access the following entry points in the GMRYRP0 routine.

> ROUTINE: GMRYRP0 COMPONENT: EN1

> VARIABLES: GMRNUR Input

> This variable is set to one to indicate that this routine was called from an external package.

> This entry point prints an I/O Summary by Patient (by Shift & Day(s)).

> COMPONENT: EN4

> VARIABLES: GMRNUR Input

> This variable is set to one to indicate that this routine was called from an external package.

> This entry point prints an I/O Summary (Midnight to Present).

> COMPONENT: EN5

> VARIABLES: GMRNUR Input

> This variable is set to one to indicate that this routine was called from an external package.

> This entry point prints an I/O Summary (48 hours).

> COMPONENT: EN2

> VARIABLES: GMRNUR Input

> COMPONENT: Q

> This variable is set to one to indicate that this routine was called from an external package.

> This entry point prints the Patient I/O Summary Report for the previous day.

> VARIABLES: This entry point cleans up variables used by GMRYRP0 calls.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1397 NAME: GMRYED3

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry points described in this DBIA for the GMRYED3 routine.

> ROUTINE: GMRYED3 COMPONENT: LIST

> VARIABLES: DFN Input

> GNUROP Input

> GMRHLOC Input

> GMROUT Both

> Patient IEN.

> Type of Input/Output/IV.

> Hospital Location file (44) pointer.

> This variable indicates whether the user abnormally exited the input process. It is passed in with a value of 0.

> This entry point allows user to start/add/DC IV and maintenance.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1398 NAME: PRSE STUDENT EDUCATION TRACKING

> CUSTODIAL PACKAGE: EDUCATION TRACKING Washington SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Other EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 452 ROOT: PRSE(452, DESCRIPTION: TYPE: File

> Nursing has permission to access the PRSE Student Education Tracking (452) fields as described in this DBIA.

GLOBAL REFERENCE:

^PRSE(452,D0,

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 39%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>STUDENT NAME</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct</th>
<th>Global</th>
<th><blockquote>
<p>R/W</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>PROGRAM/CLASS TITLE</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td><blockquote>
<p>PRSE PROGRAM/CLASS L</p>
</blockquote></td>
<td><blockquote>
<p>0;16</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.4</p>
</blockquote></td>
<td><blockquote>
<p>PROGRAM/CLASS SUPPLI</p>
</blockquote></td>
<td><blockquote>
<p>6;2</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>PROGRAM/CLASS CATEGO</p>
</blockquote></td>
<td><blockquote>
<p>0;5</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>0;21</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>CONTACT HOURS</p>
</blockquote></td>
<td><blockquote>
<p>0;10</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9.1</p>
</blockquote></td>
<td><blockquote>
<p>C.E.U.s</p>
</blockquote></td>
<td><blockquote>
<p>0;6</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION</p>
</blockquote></td>
<td><blockquote>
<p>0;13</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>ENDING DATE</p>
</blockquote></td>
<td><blockquote>
<p>0;14</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13.5</p>
</blockquote></td>
<td><blockquote>
<p>PROGRAM/CLASS LOCATI</p>
</blockquote></td>
<td><blockquote>
<p>0;15</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL NON-LOCAL</p>
</blockquote></td>
<td><blockquote>
<p>6;1</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>HOURS A/A REQUESTED</p>
</blockquote></td>
<td><blockquote>
<p>0;17</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>HOURS A/A GRANTED</p>
</blockquote></td>
<td><blockquote>
<p>0;18</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ROUTINE/NON-ROUTINE</p>
</blockquote></td>
<td><blockquote>
<p>0;4</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>77</p>
</blockquote></td>
<td><blockquote>
<p>C.E.U. COMMENTS</p>
</blockquote></td>
<td><blockquote>
<p>5;0</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This is a word processing field which expands into the

> ^PRSE(452,D0,5, global reference.

> Also the following cross-references on the PRSE Student Education Tracking are permitted to be accessed:

> Xref Type of Access

> AA Direct global read/write AK Direct global read/write

> AL Direct global write

> B Direct global read/write CAT Direct global write

> CLAS Direct global write CLS Direct global write DAT Direct global write

7.  Direct global read/write
8.  Direct global write SER Direct global write SOR Direct global write

> Also supported are direct global reads of the ^PRSE(452,D0,0) and

> ^PRSE(452,D0,6) node, as well as direct global read/write of the

> ^PRSE(452,0) node.

> GLOBAL REFERENCE:

> ^PRSE(452,D0,3,D1,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 37%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>FUNDS REQUESTED</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct</th>
<th><blockquote>
<p>Global R/W</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT REQUESTED</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct</td>
<td><blockquote>
<p>Global R/W</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Also supported is direct global reads on ^PRSE(452,D0,3,D1) to \$Order through the multiple, direct global reads/writes of the

> ^PRSE(452,D0,3,0) node, direct global reads of ^PRSE(452,D0,3,D1,0), and direct global reads of the "B" cross-reference of the Funds Requested sub-file.

> GLOBAL REFERENCE:

> ^PRSE(452,D0,4,D1,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>FUNDS AUTHORIZED</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct Global</th>
<th><blockquote>
<p>R/W</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT AUTHORIZED</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Direct Global</td>
<td><blockquote>
<p>R/W</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Also supported is direct global reads on ^PRSE(452,D0,4,D1) to \$Order through the multiple, direct global read/write on the ^PRSE(452,D0,4,0) node, direct global reads of the ^PRSE(452,D0,4,D1,0) node, and direct global reads of the "B" cross-reference on the Funds Authorized

> sub-file.

> GLOBAL REFERENCE:

> ^PRSE(452,D0,1,D1,

> 8 OBJECTIVES Direct Global Read

> Also supported is direct global reads on ^PRSE(452,D0,1,D1) to \$Order through this word processing multiple and direct global reads on the nodes (i.e., PRSE(452,D0,1,DA,0)) that make up the lines of this word processing multiple.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1399 NAME: PRSE PROGRAM/CLASS

> CUSTODIAL PACKAGE: EDUCATION TRACKING Washington SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 452.1 ROOT: PRSE(452.1, DESCRIPTION: TYPE: File

> Nursing has permission to access the PRSE Program/Class fields specified in this DBIA.

> ^PRSE(452.1,D0,

> .01 PROGRAM CLASS/TITLE 0;1 Direct Global R/W

> 2 PRSE PROGRAM/CLASS L 0;3 Direct Global Read

4.  REQUIRED FREQUENCY 0;6 Direct Global R/W
5.  TYPE OF EDUCATION 0;7 Direct Global R/W
6.  SERVICE 0;8 Direct Global Write
7.  OPEN/CLOSED 0;9 Direct Global R/W

> Also supported are direct global read/writes to the ^PRSE(452.1,0) node, direct global read/writes on the "B" and "C" cross-references of the PRSE Program/Class file, and direct global read of the

> ^PRSE(452.1,D0,0) node.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1400 NAME: PRSE MANDATORY TRAINING (MI) CLASS GROUP CUSTODIAL PACKAGE: EDUCATION TRACKING Washington

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 452.3 ROOT: PRSE(452.3, DESCRIPTION: TYPE: File

> Nursing has permission to access the PRSE Mandatory Training (MI) Class Group file fields described in this DBIA.

> ^PRSE(452.3,D0,

1.  NAME 0;1 Direct Global R/W
2.  SERVICE 0;2 Direct Global Write

> Also included are direct global read/write of the ^PRSE(452.3,0) node, direct global read/write of the "B" cross-reference of the

> 452.3 file, and direct global write of the "D" cross-reference of the

> 452.3 file.

> ^PRSE(452.3,D0,1,D1,

> .01 MANDATORY CLASSES 0;1 Direct Global Write Also included here are direct global read/write of the

> ^PRSE(452.3,D0,1,0) node, direct global read/write of the "B"

> cross-reference of the Mandatory Classes sub-file, and direct global write of the "C" cross-reference of the Mandatory Classes sub-file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1401 NAME: PRSE PARAMETERS

> CUSTODIAL PACKAGE: EDUCATION TRACKING Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 452.7 ROOT: PRSE(452.7, DESCRIPTION: TYPE: File

> Nursing has permission to access the PRSE Parameters (452.7) file fields as described in this DBIA.

> ^PRSE(452.7,D0,

> 1 PRSE OFFLINE/ON-LINE OFF;1 Direct Global Read ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1402 NAME: PAID EMPLOYEE

> CUSTODIAL PACKAGE: PAID Washington SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 450 ROOT: PRSPC( DESCRIPTION: TYPE: File

> Nursing has permission to access the PAID Employee file fields as

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>described in</th>
<th><blockquote>
<p>this DBIA.</p>
</blockquote></th>
<th colspan="4" rowspan="2"></th>
</tr>
<tr class="odd">
<th>^PRSPC(D0,</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>EMPLOYEE NAME</p>
</blockquote></td>
<td><blockquote>
<p>0;1</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>0;9</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>SALARY DATE</p>
</blockquote></td>
<td><blockquote>
<p>0;28</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>SALARY</p>
</blockquote></td>
<td><blockquote>
<p>0;29</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>SEPARATION IND</p>
</blockquote></td>
<td><blockquote>
<p>1;33</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>458</p>
</blockquote></td>
<td><blockquote>
<p>COST CENTER/ORGANIZA</p>
</blockquote></td>
<td><blockquote>
<p>0;49</p>
</blockquote></td>
<td>Direct</td>
<td>Global</td>
<td><blockquote>
<p>Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Also included here are direct global reads of the "ACC" and "SSN" cross-references of the PAID Employee file, and direct global reads of the ^PRSPC(D0,0) and ^PRSPC(D0,1) nodes.

> ^PRSPC(D0,5,D1,

1.  MI REVIEW GROUP 0;1 Direct Global R/W
2.  DATE ASSIGNED 0;2 Direct Global Write Also included here are direct global read/write of the "B"

> cross-reference of the MI Review Group sub-file, direct global read/write of the ^PRSPC(D0,5,0) node, direct global read of

> ^PRSPC(D0,5,D1) to loop through the multiple, and direct global read of the ^PRSPC(D0,5,D1,0) node.

> ^PRSPC(D0,6,D1,

> .01 MANDATORY CLASS 0;1 Direct Global Read

> .03 DATE ASSIGNED 0;3 Direct Global Read

> Also included here are direct global reads of ^PRSPC(D0,6,D1) to

> \$Order through the multiple and direct global read of the

> ^PRSPC(D0,6,D1,0) node.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1403 NAME: PAID CODE FILES

> CUSTODIAL PACKAGE: PAID Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 454 ROOT: PRSP(454, DESCRIPTION: TYPE: File

> Nursing has permission to access the PAID Code Files file fields as described in this DBIA.

> ^PRSP(454,D0,'ORG',D1,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 18%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>CODE</p>
</blockquote></th>
<th>0;1</th>
<th>Direct Global Read</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td>0;2</td>
<td>Direct Global Read</td>
</tr>
</tbody>
</table>

> Also included here are direct global reads of the "B" and "C" cross-references of the Cost Center/Organization sub-file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1404 NAME: PAID COST CENTER/ORGANIZATION

> CUSTODIAL PACKAGE: PAID Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 454.1 ROOT: PRSP(454.1, DESCRIPTION: TYPE: File

> Nursing has permission to access the "B" cross-reference of the PAID Cost Center/Organization (454.1) file using direct global reads.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1407 NAME: FHWHEA

> CUSTODIAL PACKAGE: DIETETICS Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to call the ^FHWHEA routine as described in this DBIA.

> ROUTINE: FHWHEA COMPONENT: FHWHEA

> VARIABLES: GMTS1 Input

> 9999999-(End_Date_for_Order_Search)

> GMTS2 Input

> GMTSNDM Input UTILITY(\$J Output

> 0)=ST^EN^DIET^COM^TYPE

> 9999999-(Start_Date_for_Order_Search)

> Number of diets orders to be returned. Nursing sets this variable to 1.

> Only two nodes from the ^UTILITY(\$J are used by Nursing and are documented here.

> ^UTILITY(\$J,"DI",9999999-(Order_Start_Date), where ST=Order Start Date (FM

> format)

> format) text) text)

> EN=Order End Date (FM DIET=Patient's diet (free

> COM=Comments about diet (free

> TYPE=Type of Service for diet

> (Tray, Cafeteria, Dining Room)

> ),0)=TF^CD^PR^ST^QT^CC^KC^COM

> ^UTILITY(\$J,"TF",9999999-(D/T_of_Tubefeeding

> where TF=Date/time of tubefeeding (FM format)

> CD=Cancel date/time of tubefeeding (FM format)

> PR=Product used in tubefeeding (free text)

> ST=Strength of product used (1/4, 1/2, 3/4, FULL)

> QT=Quantity of product used

> (free text) (numeric)

> CC=Total CC's of tubefeeding KC=Total KCal's of

> tubefeeding (numeric)

> COM=Comments about tubefeeding (free text)

> This entry point returns information about Dietetics orders for a particular patient.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1408 NAME: PRSEUTL5

> CUSTODIAL PACKAGE: EDUCATION TRACKING Washington SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can use the PRSEUTL5 utility as described in this DBIA.

> ROUTINE: PRSEUTL5 COMPONENT: EN1(PRSED0) VARIABLES: PRSED0 Input

> Passed in via parameter passing, this variable is the IEN of the PAID Employee

> \(450\) file entry to be updated.

> This component will take the current MI review groups assigned to a PAID Employee (450) file entry and update the Mandatory Class multiple for that record.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1412 NAME: DD GLOBAL

> CUSTODIAL PACKAGE: VA FILEMAN San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> TEXT GENERATOR Chicago

> VITALS/MEASUREMENT Chicago

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: 0 ROOT: DD(

> DESCRIPTION: TYPE: File

> The Nursing, Vitals/Measurements, and Text Generator packages have been granted permission to access the DD global as defined in this DBIA. GLOBAL REFERENCE:

> ^DD(124.2,0,'DIK')

> Nursing and Text Generator have permission to kill this node to uncompiled cross-references on the Aggregate Term (124.2) file.

> GLOBAL REFERENCE:

> ^DD(file,field,

> .01 LABEL 0;1 Direct Global Read

> Nursing can direct global read the name of a field, and direct global read to loop through the ^DD global to get all of the fields for a particular Nursing file. file is in the range of the Nursing file number space assigned by the DBA, and field is a valid field number in file.

> .3 POINTER 0;3 Direct Global Read Nursing can access this field to decode a set of codes to its

> external format. file is in the range of the Nursing file number space assigned by the DBA, and field is a valid field number in file.

> .5 INPUT TRANSFORM 0;5,99 Direct Global Read Nursing can execute the input transform directly for its

> files/fields. file is in the range of the Nursing file number space assigned by the DBA, and field is a valid field number in file.

3.  'HELP'-PROMPT 3;E1,245 Direct Global Read

> Nursing can read the 'Help'-Prompt field for its files/fields. file is in the range of the Nursing file number space assigned by the DBA, and field is a valid field number in file.

4.  XECUTABLE 'HELP' 4;E1,245 Direct Global Read

> Nursing can read the Xecutable 'Help' for its files/fields. file is in the range of the Nursing file number space assigned by the DBA, and field is a valid field number in file.

8.  READ ACCESS (OPTIONA 8;E1,245 Direct Global Write

> The Text Generator and Vitals/Measurements can write the Read Access (Optional) for its files/fields. file is in the appropriate package numberspace as assigned by the DBA, and field is a valid field number for file.

9.  WRITE ACCESS (OPTION 9;E1,245 Direct Global Write

> The Text Generator and Vitals/Measurements can write the Write Access (Optional) for its files/fields. file is in the appropriate numberspace as assigned by the DBA, and field is a valid field number of file.

> 21 DESCRIPTION 21;0 Direct Global Read

> Nursing is allowed direct global read access to the Descriptions for fields to print them out. Also included here are the direct global read references to the ^DD(file,field,21, subtree that would be necessary to read this WP field. file is a valid number in the Nursing numbers space as assigned by the DBA, and field is a valid field number for file.

> GLOBAL REFERENCE:

> ^DD(file,field,1,xref_ien,

1.  SET STATEMENT 1;E1,245 Direct Global Read Nursing and the Text Generator are allowed to directly read the Cross-reference Set Statements for their package so they can be

> executed. file is a valid number in the appropriate number space as assigned by the DBA, field is a valid field number of file, and xref_ien is the cross-reference ien being used.

2.  KILL STATEMENT 2;E1,245 Direct Global Read Nursing and the Text Generator are allowed to directly read the

> Cross-reference Kill Statements for their package so they can be executed. file is a valid number in the appropriate number space as assigned by the DBA, field is a valid field number of file, and xref_ien is the cross-reference ien being used.

> Nursing and the Text Generator are allowed direct global read access to

> ^DD(file,field,1,xref_ien) in order to loop through the cross-reference multiple for their files, where file is in the package numberspace assigned by the DBA, field is a valid field in file, and xref_ien is the ien of the cross-reference for field in file.

> GLOBAL REFERENCE:

> ^DD(file,'SB',

> Nursing can direct global read the ^DD(file,"SB") cross-reference to determine the sub-files for a particular file/sub-file. file is a valid number in the Nursing numberspace as assigned by the DBA.

> GLOBAL REFERENCE:

> ^DD(124.21,0,'DIK')

> Vitals, Nursing & Text Generator have permission to kill off this node.

> GLOBAL REFERENCE:

> ^DD(124.2,0,'DIKOLD')

> Vitals, Nursing & Text Generator have permission to kill off this node.

> GLOBAL REFERENCE:

> ^DD(2,0,'IX','ANURS',2,.1)

> Nursing has permission to direct global kill/write this node when setting up the "ANURS" cross-reference in the Patient file. MAS has already approved this, see MailMessage \#18109934.

> GLOBAL REFERENCE:

> ^DD(2,.1,1,

> Nursing can direct global write the following nodes:

> ^DD(2,.1,1,xref_ien,0)="2^ANURS^MUMPS", ^DD(2,.1,1,xref_ien,1)="S

> %X=X,X=""NURSCPL"" X ^%ZOSF(""TEST"") S X=%X D:\$T EN1^NURSCPL",

> ^DD(2,.1,1,xref_ien,2)="S %X=X,X=""NURSCPL"" X ^%ZOSF(""TEST"") S X=%X

> D:\$T EN2^NURSCPL". xref_ien is the next available cross-reference ien for field .1. A direct global read is allowed on ^DD(2,.1,1,xref_ien) to loop through the xrefs of field .1. Nursing can direct global kill the ANURS cross-reference via a direct global kill of the

> ^DD(2,.1,1,xref_ien) node. xref_ien is ien of the ANURS xref (where

> \$P(^DD(2,.1,xref_ien,0),"^",2)="ANURS"). MAS has already approved this use of their file, ref. msg \#18109934.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1413 NAME: MARITAL STATUS

> CUSTODIAL PACKAGE: REGISTRATION Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 11 ROOT: DIC(11, DESCRIPTION: TYPE: File

> Nursing has permission to access the Marital Status (11) file as described in this DBIA.

> ^DIC(11,D0,

2.  MARITAL STATUS CODE 0;3 Direct Global Read ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1414 NAME: RELIGION

> CUSTODIAL PACKAGE: REGISTRATION Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 13 ROOT: DIC(13,

> DESCRIPTION: TYPE: File

> Nursing has permission to access the Religion (13) file as described in this DBIA.

> ^DIC(13,D0,

> .01 NAME 0;1 Direct Global Read ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1415 NAME: GMRYFLW0

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to access the following entry point in the GMRYFLW0 routine.

> ROUTINE: GMRYFLW0 COMPONENT: EN1

> VARIABLES: GMRNUR Input

> This variable is passed in with a value of 1 to indicate that the report is requested by the Nursing service.

> This entry point allows user to print the Intravenous Infusion Flow Sheet for a selected time range.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1416 NAME: HOSPITAL LOCATION

> CUSTODIAL PACKAGE: SCHEDULING Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: 44 ROOT: SC(

> DESCRIPTION: TYPE: File

> Nursing can access the Hospital Location (44) file as described in this DBIA.

> ^SC(D0,0)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th>NAME</th>
<th></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th><blockquote>
<p>Write w/Fileman</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Nursing has permission to LAYGO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>entries to the Hospital</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Location file using ^DIC.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>These entries will have a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Type=OTHER and Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Extension=NURSING.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Nursing has permission to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>delete entries in this file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>using ^DIK. The only entries</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>that can be deleted are those</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>with Type=OTHER, and Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Extension=NURSING.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>TYPE</td>
<td></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td><blockquote>
<p>Write w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.1</p>
</blockquote></td>
<td>TYPE</td>
<td><blockquote>
<p>EXTENSION</p>
</blockquote></td>
<td><blockquote>
<p>0;22</p>
</blockquote></td>
<td><blockquote>
<p>Write w/Fileman</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  INSTITUTION 0;4 Write w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1417 NAME: LOCATION TYPE

> CUSTODIAL PACKAGE: SCHEDULING Albany SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 40.9 ROOT: DIC(40.9, DESCRIPTION: TYPE: File

> Nursing can access the Location Type (40.9) file as described in this DBIA.

> ^DIC(40.9,0)

> 1 DESIGNATION 0;2 Direct Global Read

> Also allowed is direct global read access to the "C"

> cross-reference of the Designation field on the Location Type file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1418 NAME: GMRGED1

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can reference the GMRGED1 routine as described in this DBIA.

> ROUTINE: GMRGED1 COMPONENT: EN1

> VARIABLES: DFN Input

> GMRGPDA Input

> GMRGRT Input

> GMRGTERM Input

> GMRGVNAM Input

> GMRGVSSN Input

> GMRGVDOB Input

> GMRGVAGE Input

> GMRGVAMV Input

> GMRGVPRV Input

> Patient's IEN.

> Entry in GMR Text file for document where part will be edited.

> Two piece variable indicating prime document for this GMR Text (124.3) file entry. The first piece is the Aggregate Term file pointer of the prime document, the second piece is the text representation of the prime document.

> Term in which user will start editing patient data. This is starting point of the edit. The data for this variable is two-piece, where the first piece is the Aggregate Term file pointer of the term, and the second piece is the text representation of the term.

> Free text patient name. Patient SSN.

> Patient DOB.

> Patient age.

> IEN in Patient Movement file for current patient admission information, or null if patient not current inpatient.

> Patient provider for current patient admission information, or null if patient not current inpatient.

> =A^B^C,

> =D^E^F,

> GMRGVWRD Input

> GMRGVRBD Input

> GMRGVADT Input

> GMRGVDX Input

> GMRGTOP(0) Input

> GMRGTOP Input

> GMRGLVL Input

> GMRGLVL( Input

> GMRGTLVL Input

> GMRGSLVL Input TMP(\$J,'GM Input

> GMRGPRC Input

> Inpatient ward for current patient admission information, or null if patient not current inpatient.

> Patient room/bed for current patient admission information, or null if patient not current inpatient.

> Admission date/time for current patient admission information, or null if patient not current inpatient.

> Patient admitting diagnosis for current patient admission information, or null if patient not current inpatient.

> This is the current prime document for the level that has been jumped to. For this usage it is just +GMRGRT.

> GMRGTOP represents how many levels the user has jumped to. In this case Nursing just passes in 1.

> Current jump level being edited. In this case the value 1 is passed in.

> GMRGLVL(GMRGLVL)=Tree level for this jump-level.

> GMRGLVL(GMRGLVL,GMRGTLVL)=Stack level for this tree level for this jump-level. The GMRGLVL array can be used to address the

> ^TMP(\$J,"GMRGLVL", global. This application is passing in GMRGLVL(1)=1, and GMRGLVL(1,1)=1.

> Current tree level being processed. This application will pass in the value of 1.

> The current stack level being processed. This application passes in 1.

> This global maps the selections and how they were picked. Using GMRGLVL, GMRGTLVL, GMRGSLVL, and GMRGLVL( the

> order of items selected by the user, or what the user typed at each prompt can be determined.

> ^TMP(\$J,"GMRGLVL",GMRGLVL,GMRGTLVL,GMRGSLVL)

> where A is the Aggregate Term file entry of term processed, B is action to be performed (add, delete, edit internal text, etc.), and C is a flag whether to redisplay the frame (0) or not (1).

> ^TMP(\$J,"GMRGLVL",GMRGLVL,GMRGTLVL,GMRGSLVL)

> where D is the free text of the aggregate term being edited, E is the IEN in the Selection multiple of the GMR Text file that represents this term, and F is the appended/internal text currently entered for this term.

> This variable in represents what the user typed in. This variable has 3 pieces,

> GMRGPRC(0) Input

> GMRGTERM(0 Input

> GMRGSCRP Input

> GMRGSITE Input

> GMRGSITE(0 Input

> GMRGSITE(' Input

> GMRGSTAT Input

> GMRGIO('RV Input GMRGIO('RV Input GMRGIO('S' Input

> GMRGLIN('- Input

> GMRGLIN('\* Input GMRGUP Both

> GMRGNORD Both

> GMRGOUT Both

> A^B^C, where A is the IEN of the Aggregate Term the user selected, B is the action the user wants to take (add, delete, edit internal text, etc.), and C is whether the user indicated to redisplay the screen for this term or not.

> This variable contains three pieces, A^B^C, which contain data about the selection the user made. A is the free text of the Aggregate Term selected, B is the entry number of this term in the Selection multiple of the GMR Text file, and C is the appended/internal text stored for this selection.

> Zeroth node of the Aggregate Term file for the Aggregate Term used as a starting point.

> Current script being executed. This is passed in with a value of 0.

> The IEN in Package Parameters multiple of GMRG Parameters (124.1) file for the type of prime document being edited. In this case it would be the IEN for the NURSC entry.

> The zeroth node of the GMRGSITE entry in the Package Parameters multiple of the GMRG Parameters file.

> The "P"-node for the GMRGSITE entry in the Package Parameters multiple of the GMRG Parameters file.

> Information about the last audit trail entry for the Aggregate Term being edited. This is a three piece variable set by STAT^GMRGRUT0 utility.

> Reverse video off executable code for the current terminal used, if it exists.

> Reverse video on executable code for the current terminal used, if it exists.

> This is a flag indicating whether the current terminal supports reverse video on/off (1), or not (0).

> A string of "-"'s with length IOM. A string of "\*"'s with length IOM.

> This variable indicates whether the user hit \<CR\> to bypass last level (1), or not (0). It is passed in with value of 0.

> This variable indicates whether the user wishes to view this screen upon reentry (0), or not (1). It is passed in as 0.

> This variable indicates whether the user abnormally exited input (1), or not (0).

> GMRGSEL( Output

> The variable is passed in with value of 0.

> This entry also returns the current list of selections for the frame passed in by GMRGTERM. GMRGSEL(A)=B, where A is the selection number from the screen, and B is a three piece variable where the first piece is the Aggregate Term file IEN for the term represented by this selection, the second piece is the printable text of that Aggregate Term, and the third piece is a flag indicating whether the selection is currently active (1), or not (0).

> This entry point allows the user to edit only part of the prime document for a patient, and not the whole document.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1419 NAME: GMRGED2

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGED2 routine as described in this DBIA.

> ROUTINE: GMRGED2 COMPONENT: QP

> VARIABLES: GMRGTERM Input

> GMRGPDA Input

> GMRGSEL( Input

> GMRGTERM(0 Input

> GMRGOUT Input

> This variable represents the Aggregate Term of the frame being processed and has format A^B^C, where A is the Aggregate Term file IEN, B is the free text representation of this Aggregate Term, and C is the Selection multiple IEN in the GMR Text file for this entry.

> This is the GMR Text file entry for this frame.

> This is the current list of selections for the frame represented by GMRGTERM. GMRGSEL(A)=B, where A is the selection number from the screen, and B is a three piece variable where the first piece is the Aggregate Term file IEN for the term represented by this selection, the second piece is the printable text of that Aggregate Term, and the third piece is a flag indicating whether the selection is currently active (1), or not (0).

> The zeroth node of the Aggregate Term represented in GMRGTERM.

> Represents whether user abnormally exited processing of this frame (1), or not (0).

> This entry point will finish processing for a selection edited.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1420 NAME: GMRGEDB

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGEDB routine as described in this DBIA.

> ROUTINE: GMRGEDB COMPONENT: ADSEL

> VARIABLES: GMRGPDA Input

> GMRGPRC Input

> GMR Text (124.3) file entry.

> This is a three piece variable representing the Aggregate Term file entry. The first piece is the Aggrege Term file IEN, the second piece is the action the user wishes to perform on this aggregate term, and the final piece indicates whether the user wishes to redisplay this frame after processing it.

> This entry point will add a Selection multiple entry in the GMR Text file for an aggregate term if it does not exist already and then updates the Selection multiple to activate the selection.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1421 NAME: GMRGPNBL

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGPNBL routine as described in this DBIA.

> ROUTINE: GMRGPNBL COMPONENT: EN1

> VARIABLES: GMRGPDT Input

> GMRGPDA Input

> GMRGPAR Input GMRGPAR(0) Input

> TMP(\$J,'GM Output

> Date/time that view of data should be taken from.

> GMR Text file IEN.

> Aggregate Term file IEN from where to begin data display.

> A four piece variable A^B^C^D, where A indicates whether to show active plan data only (1), or to show both active/inactive data (0), B is the number of spaces to leave from right margin, C is the number of spaces to leave from left margin, and D is the subscript to be used by the package making the call in the return array.

> The ^TMP(\$J,"GMRGNAR", array is returned in the following format:

> ^TMP(\$J,"GMRGNAR",A,B,0)=^N, and

> ^TMP(\$J,"GMRGNAR",A,B,C)=D, where N is

> the number of lines of printable text, A is the package subscript passed in the GMRGPAR(0) parameter, B is the Aggregate

> Term IEN passed in the GMRGPAR parameter, C is a number between 1 and N, and D is a printable line of text.

> This entry point will return the printable text for an aggregate term and a particular GMR Text entry.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1422 NAME: GMRGRUT0

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can use the GMRGRUT0 routine as described in this DBIA.

> ROUTINE: GMRGRUT0 COMPONENT: STAT

> VARIABLES: GMRGST Input

> GMRGST(1) Input

> GMRGSTAT Output

> IEN of Selection multiple of GMR Text file.

> GMR Text file IEN.

> This is a three piece variable, A^B^C, where A is the IEN of the Audit Trail entry in the Audit Trail sub-file of the Selection sub-file of the GMR Text file, B is the date/time of the audit trail entry, and C is the modification done in this audit trail entry.

> Get the last audit trail entry for this Selection in the GMR Text file.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1423 NAME: GMRGRUT1

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to use the GMRGRUT1 routine as described in this DBIA.

> ROUTINE: GMRGRUT1 COMPONENT: FITLINE VARIABLES: GMRGPLN Input

> GMRGLEN Input GMRGPLN(0) Output

> GMRGPLN(1) Output

> Text to be printed.

> Length of line to fit text into.

> The line of text that fits into the specified length.

> The remainder of the text that did not fit on the line.

> This entry point takes text and a length of a line and returns the part of the text that will print in the line, broken at the last word, and the rest of the text not printed.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1424 NAME: GMRGRUT2

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGRUT2 routine as described in this DBIA.

> ROUTINE: GMRGRUT2 COMPONENT: EN1

> VARIABLES: GMRGXPRT Both

> GMRGXPRT(0 Input GMRGXPRT(1 Input

> Aggregate Term file IEN of term to be printed is passed in. If the GMRGXPRT(1) variable indicates to return text in GMRGXPRT, then GMRGXPRT will contain the printable text.

> Appended/Internal text to be printed with this aggregate term.

> Parameters customizing the print. This is a six piece variable, A^B^C^D^E^F, where A is the number of spaces to indent from left margin, B is the length of the line, C indicates whether to include the brackets for internal text (1) or not (0), D indicates whether to highlight this term (1) or not (0), E indicates whether to print the result (0), or return result in GMRGXPRT variable (1), and F indicates whether to hide text in

> \<\> brackets (1) or not (0).

> This entry point will take an aggregate term and return/print the printable version of it.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1425 NAME: GMRGRUT3

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGRUT3 routine as indicated in this DBIA.

> ROUTINE: GMRGRUT3 COMPONENT: EN1

> VARIABLES: GMRGRT Input

> DFN Input

> GMRGXPRT Input

> This variable represents the prime document to be screened for. This is a two-piece variable, A^B, where A is the Aggregate Term file IEN for the prime document, and B is the free text representation of the prime document.

> Patient file IEN.

> Parameters to customize lookup. This variable has three pieces, A^B^C, where A indicates whether to look at all (1) or only active (0) data, B indicates whether an entry can be added (1) or not (0), and

> GMRGPDA Output

> GMRGOUT Output

> C indicates whether an entry can be entered in error (1) or not (0).

> GMR Text file IEN.

> Flag indicating whether user abnormally exited lookup (1) or not (0).

> This entry point will select an entry from the GMR Text file.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1426 NAME: GMRGTGIF

> CUSTODIAL PACKAGE: TEXT GENERATOR Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRGTGIF routine as described in this DBIA.

> ROUTINE: GMRGTGIF COMPONENT: EN4

> VARIABLES: GMRGRT Input

> GMRGPK Input

> GMRGOUT Output

> This variable represents the prime document to be screened for. This is a two-piece variable, A^B, where A is the Aggregate Term file IEN for the prime document, and B is the free text representation of the prime document.

> Package reference to indicate which prime document is to be edited. NURSC represents Nursing Care Plan.

> Flag indicating whether user abnormally exited lookup (1) or not (0).

> This entry point allows the user to enter/edit data in the Aggregate Term file.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1430 NAME: GMRYRP1

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing has permission to access the NEXT entry point for the GMRYRP1 routine. Vitals/Measurements is allowed to use the entry STARTD for the GMRYRP1 routine.

> ROUTINE: GMRYRP1 COMPONENT: NEXT

> VARIABLES: GMRFIN Input

> GLASTDT Output

> GDTSTRT Output

> GNXTDT Output

> Date/time the current nursing shift ends.

> Date the day before the date stored in GMRFIN.

> Date the nursing shift starts.

> Date the day after the date stored in GDTSTRT.

> GMRNIT Output

> GDTFIN Output

> Time the nursing night shift starts. Date the nursing shift ends.

> This entry point is called to initialize variables required for the SETSIFT^GMRYRP2 call.

> COMPONENT: STARTD

> VARIABLES: DFN Input

> GMRSTRT Both

> GMRFIN Both

> GMROUT Both

> GRPT Input

> GMRNIT Input

> GMRDAY Input

> GMREVE Input

> Patient IEN.

> Input: Start date of information extract. Output: Start date_night shift start hour.

> Input: End date of information extract. Output: End date_evening shift end hour.

> Passed in with a value of 0. Returned a value of 1 if exited abnormally.

> Set to 5 to indicate that the data are requested the V/M Graphic Reports.

> Nursing night shift start hour defined in the GMRY NUR Shift/Other file (126.95).

> Nursing day shift start hour defined in the GMRY NUR Shift/Other file (126.95).

> Nursing evening shift start hour defined in the GMRY NUR Shift/Other file (126.95).

> This entry is called to set up the start date/time and end date/time of information extract according to the nursing shift starting hours defined in the GMRY NUR Shift/Other file (126.95).

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1431 NAME: GMRVDS0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the GMRVDS0 routine as described in this DBIA.

> ROUTINE: GMRVDS0 COMPONENT: EN2

> VARIABLES: This entry point allows user to print latest vital signs for a patient if the patient IEN is unknown.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1433 NAME: GMRYUT2

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point in the GMRYUT2 routine.

> ROUTINE: GMRYUT2

> COMPONENT: SELSITE VARIABLES: DFN Input

> GMRX Output

> Patient IEN.

> Local global containing the intravenous infusion site information.

> This entry point is called to extract all current intravenous infusion sites and the sites discontinued within the last 24 hours for the selected patient.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1435 NAME: GMRYRP2

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing and Vitals/Measurements can access the following entry points in the GMRYRP2 routine.

> ROUTINE: GMRYRP2 COMPONENT: SAVE

> VARIABLES: DA(1) Input

> II Input

> GMRSTRT Input

> GMRFIN Input

> TMP Output

> Pointer to the GMRY Patient I/O file (126).

> Passed in with a value of "IN" or "OUT" subscript of the GMRY Patient I/O file (126).

> Date/time the current nursing shift starts.

> Date/time the current nursing shift ends.

> ^TMP(\$J,"GMRY") global contains intake and output information for a selected patient.

> This entry call extracts the intake and output information and stores the data in ^TMP(\$J,"GMRY") for a selected patient.

> COMPONENT: SAVEIV

> VARIABLES: DA(1) Input

> GMRSTRT Input

> GMRFIN Input

> TMP Output

> Pointer to the Patient I/O file (126).

> Date/time the current nursing shift starts.

> Date/time the current nursing shift ends.

> ^TMP(\$J,"GMRY") global contains the patient intravenous infusion information.

> This entry call extracts patient intravenous infusion information and stores the data in ^TMP(\$J,"GMRY") global.

> COMPONENT: SETSIFT VARIABLES: GMRINDT Input

> GDTSTRT Input

> GDTFIN Input

> GLASTDT Input

> Date/time the I/O data was entered. Date the nursing shift starts.

> Date the nursing shift ends.

> Date the day before the current nursing shift ends.

> GSHIFT Output

> Value = "SH-1" night shift,

> = "SH-2" day shift,

> = "SH-3" evening shift.

> This entry is called to assign the nursing shift (night, day or evening) according to the date/time the I/O data was entered.

> COMPONENT: GMRYRP2 VARIABLES: DFN Input

> GMRSTRT Input

> GMRFIN Input

> Patient IEN.

> Start date for the information extract. End date for the information extract.

> This routine is called by the Vitals/Measurements to extract patient intake and output information entered within a selected date range.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1436 NAME: GMRYRP3

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing and Vitals/Measurements can access the following entry point in the routine GMRYRP3.

> ROUTINE: GMRYRP3 COMPONENT: REPORT1

> VARIABLES: GRPT Input

> GQ Input

> GQT Input

> GMROUT Both

> TMP Both

> GTOTLI Output

> GTOTLO Output

> GN(1) Output

> GN(2) Output

> GIN Output

> GOUT Output

> Type of intake/output report. Set GRPT =

10. for the Nursing End of Shift Report. Set GRPT = 5 for the V/M Graphic Reports.

> Passed in with a value of 0, required by the GMRYRP3 routine.

> Passed in with a value of 0, required by the GMRYRP3 routine.

> This variable indicates whether the user abnormally exited the process. It is passed in with a value of 0.

> ^TMP(\$J,"GMRY") contains the intake, output and intravenous infusion data for a patient. If the data is requested by the Vitals/Measurements, ^TMP(\$J,"GMR") is also used to store the aggregated information.

> Intake grand total. Output grand total.

> Number of intake types listed in the GMRY Input Type file (126.56).

> Number of output types listed in the GMRY Output Type file (126.58).

> Intake nursing shift total.

> GTOTIN Output

> GTOTOUT Output

> Output nursing shift total. Intake day total.

> Output day total.

> The Nursing End of Shift Report calls this entry point to aggregate the data obtained from the execution of SAVE^GMRYRP2 and ^GMRYRP2. The V/M Graphic Reports call this entry point to aggregate data obtained from the execution of STARTD^GMRYRP1, PT^GMRYUT0 and ^GMRYRP2.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1437 NAME: GMRYSE0

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point in the GMRYSE0 routine.

> ROUTINE: GMRYSE0 COMPONENT: EN1

> VARIABLES: GMRNUR Input

> This variable is passed in with a value of 1 to indicate that the report is requested by the Nursing Service.

> This entry point allows user to print the Patient Intake/Output 24 Hours Itemized Shift Report for a time range.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1438 NAME: GMRYSE3

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point in the GMRYSE3 routine.

> ROUTINE: GMRYSE3 COMPONENT: FITLINE

> VARIABLES: GMRLEN Input

> GTXT(0) Output

> GTXT(1) Both

> Number of characters for a line of text.

> The first n-words of the input text in the GTXT(1) that will fit in length GMRLEN.

> The rest of the text.

> This utility breaks a line of text into lines. The length of the new line is defined by user.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1439 NAME: GMRVDS1

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point in the GMRVDS1 routine as described in this DBIA.

> ROUTINE: GMRVDS1 COMPONENT: EN3

> VARIABLES: DFN Input

> TMP Input

> GMRVWLO Input

> Patient IEN.

> ^TMP(\$J,patient room-bed,patient name,DFN) global contains the patients for the report.

> Free text version of Nursing ward location.

> This entry point allows user to print the latest vital signs by a Nursing location.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1440 NAME: GMRVED0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry points described in this DBIA for the GMRVED0 routine.

> ROUTINE: GMRVED0 COMPONENT: EN3

> VARIABLES: DFN Input

> GMROUT Both

> GNUROP Input

> GMRVIDT Input

> GMRVHLOC Input

> GMRENTY Input

> GMRSTR Input

> Patient IEN.

> This variable indicates whether the user abnormally exited the input process. It is passed in with a value of 0.

> This variable is passed in with a value of 1 to indicates that the edit process is requested by the Nursing Service.

> The date/time the vitals/measurements were taken.

> Hospital Location file (44) pointer.

> The type of vitals/measurements to edit.

> The string of which vitals/measurements to edit, for example, "T;P;R;BP;WT;".

> This entry point allows user to enter vitals/measurements for a patient.

> COMPONENT: Q

> VARIABLES: This entry point is called to clean up the variables used by the GMRVED0.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1441 NAME: GMRVEE0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point described in this DBIA for the GMRVEE0 routine.

> ROUTINE: GMRVEE0 COMPONENT: EN2

> VARIABLES: DFN Input

> Patient IEN.

> This entry point allows user to edit a vital/measurement entered in error.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1442 NAME: GMRVER0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point described in this DBIA for the GMRVER0 routine.

> ROUTINE: GMRVER0 COMPONENT: EN1

> VARIABLES: This entry point allows user to print vitals/measurements entered in error for a patient.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1443 NAME: GMRVSAS0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point described in this DBIA for the GMRVSAS0 routine.

> ROUTINE: GMRVSAS0 COMPONENT: EN1

> VARIABLES: GMRVX Input

> GMRVX(0) Input

> GMRVX(1) Output

> This variable is passed in with a value of "T", "P", "R", "B" or "BP" as vital type code.

> This variable contains vital data for the screening.

> If the output value equals 0 - vital data within normal range. If the output value equals 1 - abnormal value defined in the GMRV Vitals Parameters file (125.57).

> This entry point is called for checking the abnormal vital/measurement.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1444 NAME: GMRVSC0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry points described in this DBIA for the GMRVSC0 routine.

> ROUTINE: GMRVSC0 COMPONENT: DATE

> VARIABLES: GMROUT Both

> GMRVSDT Output

> GMRVFDT Output

> This variable indicates whether the user abnormally exited the call. It is passed in with a value of 0.

> Start date/time of the date range. End date/time of the date range.

> This entry point allows user to define start date/time and end date/time for a date range.

> COMPONENT: EN5

> VARIABLES: DFN Input

> GMRX Input

> GMROUT Both

> GMRVSDT Input

> GMRVFDT Input

> GMRPG Input

> Patient IEN.

> Patient admission date/time.

> This variable indicates whether the user abnormally exited the report process. It is passed in with a value of 0.

> Start date/time of the date range. End date/time of the date range.

> This report page count is initialized with a value of 0.

> This entry point allows user to print cumulative vitals/measurements for a patient over a given date range.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1445 NAME: GMRVSR0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry points described in this DBIA for the GMRVSR0 routine.

> ROUTINE: GMRVSR0 COMPONENT: EN5

> VARIABLES: DFN Input

> GFLAG Input

> GMRDATE Input

> GMRVWLO Input

> Patient IEN.

> This variable is passed in with a value of 0 to indicate that the report is requested by the Nursing Service.

> This variable is passed in with a value of "start date/time^end date/time^type of graph".

> Nursing location free text.

> COMPONENT: Q2

> User can use this entry point to print V/M Graphic Reports, Vital Signs Record, B/P Plotting Chart or Weight Chart.

> VARIABLES: This entry point is called to clean up the variables used for the graphic reports.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1446 NAME: GMRVUT0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> This routine will return vital/measurement for a patient over a given date/time range.

> ROUTINE: GMRVUT0 COMPONENT: EN1

> VARIABLES: DFN Input

> GMRVSTR Input

> GMRVSTR(0) Input

> Patient IEN.

> Types of vitals/measurements desired. Use the abbreviations found in the GMRV Vital Type file (120.51). For multiple vitals, use the ; as a delimiter, for example, "T;P;R;BP;".

> This variable specifies which vital/measurement data will be returned. The variable has four pieces, A^B^C^D, where:

> A=Start date/time (FM format) of vital/measurement data to be returned.

> B=End date/time (FM format) of vital/measurement data to be returned.

> C=Number of occurrences (numeric) of vital/measurement data to be returned.

> D=Parameter to govern sort order of return array. The value of this

> piece can either be 0 or 1. If it is 0, the return data will be sorted

> by type, then by date/time entered.

> If it is 1, the return data will

> be sorted by date/time entered, then by type. See output variable

> ^UTILITY for more information.

> UTILITY Output

> vital/measurement type from GMRVSTR

> The output array is ^UTILITY(\$J,"GMRVD"). The subscripts of this array are governed by the 4th piece of the input variable GMRVSTR(0).

> If \$P(GMRVSTR(0),"^",4) is true, the return array will be:

> ^UTILITY(\$J,"GMRVD",RDT,TYP,IEN)=DATA

> If \$P(GMRVSTR(0),"^",4) is false, the return array will be:

> ^UTILITY(\$J,"GMRVD",TYP,RDT,IEN)=DATA

> In the above, the following abbreviations translate as follows:

> RDT = Reverse date/time vital/measurement was taken in format

> 9999999-(Date/time taken).

> TYP = Abbreviation of

variable.

> IEN = Entry in GMRV Vital/Measurement (120.5) file of this data.

> DATA = Data about this vital/measurement with the following format,

> ITE^QUAL^ABN^UNIT,

> GMRVSTR('L Input

> VDT^DFN^ITYP^EDT^LOC^USER^ISITE^RATE^IQUAL^S

> where:

> VDT = Date/time vital/measurement taken (FM format)

> DFN = IEN for patient in Patient file.

> ITYP = IEN for vital type in GMRV Vital Type file.

> EDT = Date/time vital/measurement entered (FM format)

> LOC = IEN for patient location in Hospital Location file.

> USER = User who entered data; IEN in New Person file.

> ISITE = IEN for site in GMRV Vital Site file.

> RATE = Rate for this vital/measurement (alphanumeric).

> IQUAL = IEN for quality in GMRV Vital Quality file.

> SITE = Site of vital/measurement (free text).

> QUAL = Quality of vital/measurement (free text).

> ABN = Flag indicating whether vital/measurement is abnormal.

> \* indicates abnormal, null indicates normal.

> UNIT = Units of measurement for rate when appropriate, e.g.

> Centigrade for temperature, Kg for weight and centimeter

> for height.

> This is an optional variable. It will be set to an ^ delimited list of Hospital Location Types, see Type (2) field of Hospital Location (44) file for a list of types. The first piece and last piece of the list must be null, i.e., ^C^M^.

> User can use this entry to gather patient vital/measurement data.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1447 NAME: GMRVUT2

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point described in this DBIA for the GMRVUT2 routine.

> ROUTINE: GMRVUT2 COMPONENT: SETU2

> VARIABLES: DFN Input

> GMRVSTR Input

> UTILITY Output

> Patient IEN.

> GMRVSTR(0) is passed in with a value of "^^1^1". GMRVSTR("T") is passed in with the abbreviation "WT" found in the GMRV Vital Type file (120.51). GMRVSTR("IEN") is passed in with a GMRV Vital Measurement file (120.5) pointer.

> GMRVSTR("R") is passed in with the date/time the weight was measured.

> The output array ^UTILITY(\$J,"GMRD") contains the desired patient weight.

> This entry is used to extract the last weight measurement for a patient.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1448 NAME: GMRVVS0

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry points described in this DBIA for the GMRVVS0 routine.

> ROUTINE: GMRVVS0 COMPONENT: EN1

> VARIABLES: DFN Input

> GFLAG Input

> GMROUT Both

> GMRNUR Input

> GMRSTRT Input

> GMRFIN Input

> Patient IEN.

> This variable is passed in with a value of 0 to indicate that the report is requested by the Nursing Service.

> This variable indicates whether the user abnormally exited the report process. It is passed in with a value of 0.

> This variable is set to a value of 0 to indicate that the process is requested by the Nursing Service.

> Start date/time for the report. End date/time for the report.

> This entry point is used to print the Expanded SF 511 Report (Itemized I/O).

> COMPONENT: DATE

> VARIABLES: GMROUT Both

> GMRSTRT Output

> GMRFIN Output

> This variable indicates whether the user abnormally exited the process. It is passed in with a value of 0.

> Start date/time user entered. End date/time user entered.

> COMPONENT: Q2

> User can use this entry to set up start date/time and end date/time for the report desired.

> VARIABLES: This entry point is called to clean up the variables used by the GMRVVS0 routine.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1458 NAME: GMRY IV DC'ED REASON

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.76 ROOT: GMRD(126.76, DESCRIPTION: TYPE: File

> Nursing has permission to access the following field in the GMRY IV DC'ed Reason (126.76) file.

> ^GMRD(126.76,D0,0)

> .01 NAME 0;1 Both R/W w/Fileman

> Nursing is allowed to LAYGO entries into the file using FileMan.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1459 NAME: GMRY OUTPUT SUBTYPE

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.6 ROOT: GMRD(126.6, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRY Output Subtype (126.6) file.

> ^GMRD(126.6,D0,0)

> .01 OUTPUT SUBTYPE 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

> 1 OUTPUT TYPE 0;2 Both R/W w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1460 NAME: GMRY INTAKE ITEMS

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.8 ROOT: GMRD(126.8, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRY Intake Items (126.8) file.

> ^GMRD(126.8,D0,0)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 17%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th>0;1</th>
<th><blockquote>
<p>Both R/W w/Fileman</p>
<p>Also Nursing is allowed to LAYGO entries into the file</p>
<p>using FileMan.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>VOLUME</p>
</blockquote></td>
<td>0;2</td>
<td><blockquote>
<p>Both R/W w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>INPUT TYPE</p>
</blockquote></td>
<td>1;0</td>
<td><blockquote>
<p>Both R/W w/Fileman</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3" rowspan="3"></td>
<td><blockquote>
<p>Also Nursing is allowed to</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAYGO into multiple using</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FileMan.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ^GMRD(126.8,D0,1,D1,0)

> .01 INPUT TYPE 0;1 Both R/W w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1461 NAME: GMRY IV SITE

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.7 ROOT: GMRD(126.7, DESCRIPTION: TYPE: File

> Nursing has permission to access the following field in the GMRY IV Site (126.7) file.

> ^GMRD(126.7,D0,0)

> .01 IV SITE 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1462 NAME: GMRY NUR IV SOLUTION

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.9 ROOT: GMRD(126.9, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRY NUR IV Solution (126.9) file.

> ^GMRD(126.9,D0,0)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 20%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>NAME</p>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
<p>0;2</p>
</blockquote></th>
<th><blockquote>
<p>Both R/W w/Fileman</p>
<p>Also Nursing is allowed to LAYGO entries into the file using FileMan.</p>
<p>Both R/W w/Fileman</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>VOLUME</p>
</blockquote></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td><blockquote>
<p>Both R/W w/Fileman</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1463 NAME: GMRY INPUT TYPE

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.56 ROOT: GMRD(126.56, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRY Input Type (126.56) file.

> ^GMRD(126.56,D0,0)

> .01 NAME 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

> 1 ORDER 0;2 Both R/W w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1464 NAME: GMRY IV SITE DESCRIPTION

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago

> SUBSCRIBING PACKAGE: NURSING SERVICE Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.72 ROOT: GMRD(126.72, DESCRIPTION: TYPE: File

> Nursing has permission to access the following field in the GMRY IV Site Description (126.72) file.

> ^GMRD(126.72,D0,0)

> .01 DESCRIPTION 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1465 NAME: GMRY IV CATHETER

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.74 ROOT: GMRD(126.74, DESCRIPTION: TYPE: File

> Nursing has permission to access the following field in the GMRY IV Catheter (126.74) file.

> ^GMRD(126.74,D0,0)

> .01 IV CATHETER TYPE/SIZ 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1466 NAME: GMRY OUTPUT TYPE

> CUSTODIAL PACKAGE: INTAKE/OUTPUT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 126.58 ROOT: GMRD(126.58, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the GMRY Output Type (126.58) file.

> ^GMRD(126.58,D0,0)

> .01 OUTPUT TYPE 0;1 Both R/W w/Fileman

> Also Nursing is allowed to LAYGO entries into the file using FileMan.

1.  ORDER 0;2 Both R/W w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1490 NAME: DEMOGRAPHIC REFERENCE FILE

> CUSTODIAL PACKAGE: SURVEY GENERATOR San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 748.2 ROOT: QA(748.2, DESCRIPTION: TYPE: File

> Nursing has permission to access the following field in the Demographic Reference File (748.2).

> ^QA(748.2,D0,0)

> .01 FILE NAME 0;1 Read w/Fileman

> Nursing has permission to Read this field with FileMan. Also, in a pre-init routine, Nursing has permission to LAYGO an entry into this file to set up the NURS Location (211.4) file entry.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1491 NAME: SURVEY

> CUSTODIAL PACKAGE: SURVEY GENERATOR San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 748 ROOT: QA(748, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the Survey (748) file.

> ^QA(748,D0,0)

> .01 NAME 0;1 Read w/Fileman

> ^QA(748,D0,1,D1,0)

2.  FILE 0;3 Read w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1492 NAME: SURVEY QUESTIONS

> CUSTODIAL PACKAGE: SURVEY GENERATOR San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 748.25 ROOT: QA(748.25, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the Survey Questions (748.25) file.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>^QA(748.25,D0,1,D1,0)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td><blockquote>
<p>QUESTION</p>
</blockquote></td>
<td><blockquote>
<p>0;1</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.015</p>
</blockquote></td>
<td><blockquote>
<p>QUESTION NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>0;2</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>.025</p>
</blockquote></td>
<td><blockquote>
<p>MULTIPLE CHOICE TYPE</p>
</blockquote></td>
<td><blockquote>
<p>0;3</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.027</p>
</blockquote></td>
<td><blockquote>
<p>NUMBER OF GRADIENTS</p>
</blockquote></td>
<td><blockquote>
<p>0;4</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>LEFT LIKERT LABEL</p>
</blockquote></td>
<td><blockquote>
<p>0;5</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>RIGHT LIKERT LABEL</p>
</blockquote></td>
<td><blockquote>
<p>0;6</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>LIKERT NUMBERIC DISP</p>
</blockquote></td>
<td><blockquote>
<p>0;7</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.05</p>
</blockquote></td>
<td><blockquote>
<p>QUESTION TEXT</p>
</blockquote></td>
<td><blockquote>
<p>2;0</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>^QA(748.25,D0,1,D1,3,D2,0)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.01</p>
<p>ROUTINE:</p>
</blockquote></td>
<td><blockquote>
<p>ANSWER</p>
</blockquote></td>
<td><blockquote>
<p>0;1</p>
</blockquote></td>
<td>Read</td>
<td><blockquote>
<p>w/Fileman</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1493 NAME: SURVEY RESPONSE DATA

> CUSTODIAL PACKAGE: SURVEY GENERATOR San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 748.3 ROOT: QA(748.3, DESCRIPTION: TYPE: File

> Nursing has permission to access the following fields in the Survey Response Data (748.3) file.

> ^QA(748.3,D0,0)

> ^

> ^ ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1914 NAME: GMRVALL0

> CUSTODIAL PACKAGE: GEN. MED. REC. - V Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> Nursing can access the following entry point described in this DBIA for GMRVED0 routine.

> ROUTINE: GMRVALL0 COMPONENT: LIST

> VARIABLES: GNUROP Input

> GMROUT Both

> GMRENTY Output

> GMRSTR Output

> This variable is passed in with a value of 1 to indicate that the edit process is requested by the Nursing Service.

> This variable indicates whether the user abnormally exited the vitals/measurements selection. It is passed in with a value of 0.

> The type of vitals/measurements to edit.

> The string of which vitals/measurements to edit, for example, "T;P;R;BP;".

> This entry point displays the vitals/measurements for the User Configurable Combination option. This option allows users to select types of vitals/measurements to edit.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1938 NAME: GMRVSITE

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

USAGE: Private APPROVED:

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Nursing package can use the DEFAULT and CHAR entry points in the GMRVSITE routine of the Vitals/Measurements package.

> ROUTINE: GMRVSITE COMPONENT: DEFAULT

> VARIABLES: The Change Default Qualifiers for Temp./Pulse \[NURCPE-VIT VMQUALITY\] option can call this entry point to change

> default qualifiers for temperature and pulse entries in the GMRV VITAL CATEGORY (#120.53) file.

> COMPONENT: CHAR

> VARIABLES: The Enter/Edit Vitals Qualifiers \[NURCPE-VIT VMSITE\] option can call this entry point to configure the GMRV VITAL QUALIFIER (#120.52) file entries.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1940 NAME: GMRVCAQU

> CUSTODIAL PACKAGE: VITALS/MEASUREMENT Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

USAGE: Private APPROVED:

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Nursing package can call EN1^GMRVCAQU in the Vitals/Measurements package.

> ROUTINE: GMRVCAQU COMPONENT: EN1

> VARIABLES: The Display Vitals Category/Qualifier Table \[NURCPE-VIT CAT/QUAL TABLE\] option can call this entry point to display a table of categories and qualifiers for various vitals/measurements (e.g., blood pressure).

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1984 NAME: FILE 452.6

> CUSTODIAL PACKAGE: EDUCATION TRACKING Washington SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

USAGE: Private APPROVED:

STATUS: Pending EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 452.6 ROOT: PRSE(452.6 DESCRIPTION: TYPE: File

> The Nursing Service package has permission to do a global read of the zero node of the PRSE SVC REASONS FOR TRAINING file (#452.6) and to print the first piece of that node (i.e., REASON FOR EMPLOYEE TRAINING) for its Nursing personnel education reports.

> GLOBAL REFERENCE:

> ^PRSE(452.6,DA,0)

> .01 REASON FOR EMPLOYEE 0;1 Direct Global Read

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1957 NAME: File Security Codes

> CUSTODIAL PACKAGE: VA FILEMAN San Francisco SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> GMRY GEN. MED. REC Chicago

> GEN. MED. REC. - V Chicago

> TEXT GENERATOR Chicago USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: 1 ROOT: DIC

> DESCRIPTION: TYPE: File

> The Gen. Med. Rec. - I/O (Intake and Output), Gen. Med. Red. - Vitals (Vitals/Measurements), Nursing Service and Text Generator packages have permission to set the security nodes (i.e., "DD", "RD", "DEL", "LAYGO", and "WR") in FILE 1 for those files within the package's number range. For example: S ^DIC(210,0,"DD")="@"

> Package Number Range

> ------- ------------

> Intake & Output 126-126.95

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Vitals/Measurements</p>
</blockquote></th>
<th><blockquote>
<p>120.5-120.57</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Nursing Service</p>
</blockquote></td>
<td><blockquote>
<p>210-219.7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Text Generator</p>
</blockquote></td>
<td><blockquote>
<p>124-124.3</p>
</blockquote></td>
</tr>
</tbody>
</table>

> With the next release of each package, the installation process will allow the site to change its file security codes to match the codes as they appear in the documentation. The site can answer YES to change their file security codes to match the package documentation or NO to leave them as is.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1964 NAME: GMRYCATH

> CUSTODIAL PACKAGE: GMRY GEN. MED. REC Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

USAGE: Private APPROVED:

STATUS: EXPIRES:

> DURATION: Till Otherwise Agr VERSION: DESCRIPTION: TYPE: Routine

> The Nursing Service package has permission to call the GMRYCATH routine in order to display or print its End of Shift report.

> ROUTINE: GMRYCATH COMPONENT: FINDCA

> VARIABLES: GSITE Input

> II Output

> DFN Input

> This is an array containing IV infusion location (e.g., LEFT WRIST). The NURCES2 routine passes the parameter GSITE by reference. For example:

> GSITE=LEFT WRIST

> The variable II is a single dimension array. It is the formal parameter associated with GSITE. Each subscripted element contains the value of the IV CATHETER TYPE/SIZE field from the GMRY PATIENT I/O FILE (#126) for a patient. It returns the name of the IV catheter for a given IV infusion location and patient.

> For example:

> GSITE("LEFT WRIST")=TRIPLE LUMEN

> The calling routine must have DFN defined.

> This entry point finds a catheter for a selected IV site.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1965 NAME: GMRYMNT

> CUSTODIAL PACKAGE: GMRY GEN. MED. REC Chicago SUBSCRIBING PACKAGE: NURSING SERVICE Chicago

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: DESCRIPTION: TYPE: Routine

> The Nursing Service package has permission to call the GMRYMNT routine in order to display or print its End of Shift report.

> ROUTINE: GMRYMNT COMPONENT: SELSITE

> VARIABLES: DFN Input

> GMRXY Output

> The calling routine must have DFN defined.

> Contains all current and discontinued IV

> sites used within the last 24 hours.

> This entry point extracts all current and discontinued IV sites used within the last 24 hours.

> DBIA's where the Nursing package is the custodian:

> 62 NAME: DBIA62

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: DSS EXTRACTS Birmingham

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 214.6 ROOT: NURSA(214.6, DESCRIPTION: TYPE: File

Subject to version 2.5 purge allowing 6 months data only.

> DSS uses the "B" cross reference on the CLASSIFICATION DATE/TIME field. Global: ^NURSA(214.6,"B",DATE,D0)

> ^NURSA(214.6,D0,0)

1.  CLASSIFICATION DATE/ 0;1 Read w/Fileman
2.  NAME 0;2 Read w/Fileman

> 1 CATEGORY 0;3 Read w/Fileman

3.  ENTERED BY 0;5 Read w/Fileman
4.  CLASSIFIER 0;6 Read w/Fileman
6.  NURS LOCATION 0;8 Read w/Fileman
7.  NURSING BED SECTION 0;9 Read w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 96 NAME: DBIA96

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: INTERIM MANAGEMENT Birmingham

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

1.  NURSING SERVICE Nursing Workload/AMIS 1106 DIRECT

> CALL TO YOUR ROUTINE Direct call to routine EN1^NURSAWL0 to print 'Nursing Workload/ AMIS 1106 Report'.

> NUR\*2.2\*20 will insure that the routine is there, ECT\*1.05\*2 will set up the proper global root before calling the routine.

2.  NURSING SERVICE Nursing Personnel Inquiry REFERENCING FIELDS FROM YOUR FILE IMS will determine global root by using

> ^DIC(210,0,"GL") and will then use a VA FileMan EN^DIQ call to display all fields in file 210 (Nurs Staff).

> Patch ECT\*1.05\*1 sets up the proper global root.

> ROUTINE: NURSAWL0 COMPONENT: EN1 VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 278 NAME: DBIA278

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: MENTAL HEALTH Dallas

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 211.6 ROOT: NURSF(211.6,

> DESCRIPTION: TYPE: File

> Mental Health V. 5.0 references the 'Nurs Tour of Duty' file:

> File \#211.6 - Nurs Tour of Duty

> Field \#.01 - Tour of Duty - ^NURSF(211.6,D0,0) piece 1 "B" X-Ref - Tour of Duty

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1409 NAME: NURS LOCATION

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: INTAKE/OUTPUT Chicago

> DSS EXTRACTS Birmingham USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 211.4 ROOT: NURSF(211.4, DESCRIPTION: TYPE: File

> Intake/Output can access the Nurs Location (211.4) file entry as described in this DBIA.

> ^NURSF(211.4,D0,

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 37%" />
<col style="width: 13%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>.01</p>
</blockquote></th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>0;1</p>
</blockquote></th>
<th>Direct Global Read</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT CARE FLAG</p>
</blockquote></td>
<td><blockquote>
<p>1;1</p>
</blockquote></td>
<td>Direct Global Read</td>
</tr>
</tbody>
</table>

> Direct global read of ^NURSF(211.4) is supported to check if the file exists.

> Direct global read of the "D" cross-reference of the NURS Location (211.4) file is supported.

> ^NURSF(211.4,D0,3,D1,

1.  MAS WARD 0;1 Direct Global Read

> Direct global read of ^NURSF(211.4,D0,3,D1) to \$Order through the multiple is supported.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 1410 NAME: NURS POSITION CONTROL

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: INTAKE/OUTPUT Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 211.8 ROOT: NURSF(211.8, DESCRIPTION: TYPE: File

> Intake/Output has permission to access the NURS Position Control (211.8) file as indicated in this DBIA.

> ^NURSF(211.8,D0,

2.  SERVICE CATEGORY 0;2 Direct Global Read

> Also direct global read access of the "D" cross-reference of file

> 211.8 is supported.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1411 NAME: NURS PATIENT

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: INTAKE/OUTPUT Chicago

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 214 ROOT: NURSF(214, DESCRIPTION: TYPE: File

> Intake/Output can access the NURS Patient (214) file as described in this DBIA.

> ^NURSF(214,D0,

> 2 NURS LOCATION 0;3 Direct Global Read

> Direct global read of the "AF" and "E" cross-references of the NURS Patient (214) file is supported.

> Direct global read of the ^NURSF(214,D0,0) node is also supported.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1529 NAME: DBIA1529

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: CONTROLLED SUBSTAN Birmingham

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 211.4 ROOT: NURSF(211.4, DESCRIPTION: TYPE: File

> This agreement will allow Controlled Substances Version 3.0 to use VA Fileman read access to the NURS LOCATION FILE (#211.4).

> ^NURSF(211.4,D0,0)

> .01 NAME 0;1 Read w/Fileman

> ^NURSF(211.4,D0,3,D1,0)

> .01 MAS WARD 0;1 Read w/Fileman ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1534 NAME: NURS CARE PLAN

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago

> SUBSCRIBING PACKAGE: TEXT GENERATOR Chicago USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Next Version VERSION: 3

> FILE: 216.8 ROOT: NURSC(216.8, DESCRIPTION: TYPE: File

> The Text Generator V3 has permission to delete entries in the NURS Care Plan (216.8) file.

> ^NURSC(216.8,D0,0

> Text Generator can delete entries in the NURS Care Plan (216.8) file using FileMan ^DIK.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 1877 NAME: DBIA1877

> CUSTODIAL PACKAGE: NURSING SERVICE Chicago SUBSCRIBING PACKAGE: DSS EXTRACTS Birmingham

> USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

> FILE: 213.3 ROOT: NURSF(213.3, DESCRIPTION: TYPE: File

> The DSS Extracts NURSING EXTRACT file (#727.805) contains a field, NURSING BEDSECTION, which is a pointer to the NURS AMIS WARD file (#213.3).

> ^NURSF(213.3,D0,0)

> .01 BED SECTION 0;1 Direct Global Read ROUTINE:

# Chapter 9 Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no internal relations for this package.

# Chapter 10 Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Package wide variables include NURSDBA, NURDA, and NURSSW.

# Chapter 11 On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Nursing software is found in the NUR namespace. All routines, templates, and options begin with the letters NUR. The file numbers are in the range of 210 through 219.9 and stored in the ^NUR\* globals.

> The list of all exported files can be produced by using the NURSFM-DD'S option.

> The XINDEX utility can be used as a cross-reference listing of all local and global variable usage as well as other information of invaluable assistance in debugging.

> On-line documentation is provided throughout the package through the use of the convention of one, two or three question marks.

> Menu Diagrams may be generated through MenuMan. File Diagrams may be generated through FileMan.

# Chapter 12 SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no SAC Exemptions for this package.

# Chapter 13 Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No additional security measures are to be applied other than those implemented through Menu Manager and the package routines.

> No additional licenses are necessary to run the software.

> Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mail groups and alerts.

> There is one mail group, NURS-ADP, which is associated with the application. The ADPAC should be a member of this mailgroup. An alert is sent to the members of the NURS-ADP mailgroup when the Nursing Acuity/Separation-Activation Run option does not run to completion.

2.  Remote systems.

> No data is sent to any remote system/facility database.

3.  Archiving/Purging.

> Refer to chapter 6, Archiving and Purging, in this manual.

4.  Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.

5.  Interfacing.

> No specialized (non-VA produced) products are embedded or required by this application.

6.  Electronic signatures.

> Electronic signatures are not used in this application.

7.  Menus.

> There are no options of particular interest to Information Security Officers (ISO's).

8.  Security Keys.

> No Security Keys are associated with this application.

9.  File Security.

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Nursing:</p>
</blockquote></th>
<th colspan="8"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>RD</p>
</blockquote></td>
<td><blockquote>
<p>WR</p>
</blockquote></td>
<td><blockquote>
<p>DEL</p>
</blockquote></td>
<td><blockquote>
<p>LAY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUMBER</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>GLOBAL NAME</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
<td><blockquote>
<p>ACC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>210</p>
</blockquote></td>
<td><blockquote>
<p>NURS</p>
</blockquote></td>
<td><blockquote>
<p>STAFF</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(210,</p>
</blockquote></td>
<td>@</td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.1</p>
</blockquote></td>
<td><blockquote>
<p>NURS</p>
</blockquote></td>
<td><blockquote>
<p>PAY SCALE</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.1,</p>
</blockquote></td>
<td>@</td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*NURS GRADE/STEP</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS SERVICE POSITION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.4,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS CLINICAL BACKGROUND</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.5,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS TOUR OF DUTY</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.6,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS AMIS POSITION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.7,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS POSITION CONTROL</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.8,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>211.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS VACANCY/TRANSFERRED</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(211.9,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.1,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>212.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS CERTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS COLLEGE MAJOR</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>212.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*NURS MANDATORY INSERVICE</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.4,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212.42</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*NURS MI CLASS GROUP</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.42,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>212.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS PRIVILEGE</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.6,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS PRODUCT LINE</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(212.7,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>213.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*NURS AMIS 1106 CLASS</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(213.1,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>213.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS AMIS 1106B FTEE</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(213.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>213.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS AMIS WARD</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(213.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>213.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS AMIS 1106 MANHOURS</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(213.4,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>213.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS AMIS DAILY EXCEPTION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(213.5,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>213.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>^DIC(213.9,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>214</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(214,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>214.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(214.6,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>214.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS REVIEW CLASSIFICATIO</p>
</blockquote></td>
<td><blockquote>
<p>^NURSA(214.7,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>216.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURS CARE PLAN</p>
</blockquote></td>
<td><blockquote>
<p>^NURSC(216.8,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>217</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURQ QI SUMMARY</p>
</blockquote></td>
<td><blockquote>
<p>^NURQ(217,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>217.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURQ STANDARDS OF CARE/PRA</p>
</blockquote></td>
<td><blockquote>
<p>^NURQ(217.1,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>217.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURQ RATIONALE</p>
</blockquote></td>
<td><blockquote>
<p>^NURQ(217.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>217.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURQ FREQUENCY</p>
</blockquote></td>
<td><blockquote>
<p>^NURQ(217.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>219.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*NURS CONVERSION NAME CHA</p>
</blockquote></td>
<td><blockquote>
<p>^NURSF(219.7,</p>
</blockquote></td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

10. References.

> There are no special reference materials for this package.

11. Official Policies.

> There are no special official policies for this package.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AA Authorized absence of staff member from duty.
> Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
> Acuity Patient classification or category rating from 1 through 5.
> Administration Schedule This is a common abbreviation for a schedule. A schedule is the frequency for which an action is to take place, such as every eight hours (Q8H) or every other day (QOD).
> ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as nursing, PIMS, etc.
> ADT Admission, Discharge, Transfer (PIMS option). AMIS Automated Management Information System.
> Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of V*IST*A applications are the PIMS and nursing modules.
> Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up storage space on the system.
> Audit Trail/Logging Features The use of automated software procedures to determine if the security controls implemented for protection of computer systems are being circumvented and to identify the potential source of the security breach.
> Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
> Baud Rate The rate at which data is being transmitted or received from a computer. The baud rate is equivalent to the number of characters per second times 10.
> Block The unit of storage transferred to and from disk drives, typically 512, 1024, or 2048 bytes (characters).
> Boot The process of starting up the computer.
> Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the data base.
> Byte A unit of computer space usually equivalent to one character.
> C.E. Continuing education.
> CIOFO Chief Information Office Field Office, formerly known as Information Resource Management Field Office, and Information Systems Center.
> CNO Central nursing office (e.g., CNO printer).
> Contingency Plan A plan which assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on a risk analysis for that system.
> CORE A collection of VA developed programs (specific to PIMS, Pharmacy Service, and Laboratory Service) which are run at VA Medical Centers.
> CPU Central Processing Unit, the core of a computer system.
> CRT Cathode Ray Tube, similar to a TV monitor but used in computer systems for viewing data. Also called a Video Display Terminal (VDT).
> Current Employee A nursing employee with the status of 'active' or 'intermittent' as identified in the NURS Staff (#210) file.
> Currently Employed See 'Current Employee'.
> Cursor A visual position indicator (e.g., blinking rectangle or an underline) on a CRT that moves along with each character as it is entered from the keyboard.
> Data Dictionary A description of file structure and data elements within a file.
> Device A hardware input/output component of a computer system (e.g., CRT, printer). Disk A magnetic storage device used to hold information.
> Edit Used to change/modify data typically stored in a file.
> EOD Enter on Duty. The date on which an individual began his/her employment.
> Field A data element in a file. For example, FTEE and SEX are fields in the NURS Staff file (#210).
> File An area were data is stored for retrieval at a later time. A computer record of related information (e.g., Staff (DB) File, Patient file, Prescription file).
> File Manager or FileMan Within this manual, File Manager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file; a data base.
> Focus Group Previously referred to as the Expert Panel, or SIUG (Special Interest User Group).
> A committee which advises programmers about the development of a particular system/package.
> FTEE Full time employee equivalent.
> Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk. In the nursing software, for example, nursing employee data is stored in one global, and patient data is stored in another global.
> GMRV This signifies the General Medical Record namespace assigned to the Vitals/Measurements application.
> GMRY This signifies the General Medical Record namespace assigned to the Intake and Output application.
> Grade/Step The salary grade and its related step.
> Hardware The physical or mechanical components of a computer system such as CPU, CRT, disk drives, etc.
> I&O Intake and Output.
> Intake /Output Type The type denotes from where the intake or output is derived, i.e., oral, intravenous, etc.
> IRMS Information Resource Management Service. IV Intravenously; by intravenous injection.
> Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
> Kilobyte More commonly known as Kbyte or K. A measure of storage capacity equivalent to 1024 characters.
> LAYGO An acronym for Learn As You Go. A technique used by FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
13. Formerly known as MUMPS. Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all V*IST*A applications.
    1.  Mandatory Inservice.
> MailMan An electronic mail, teleconferencing, and networking system.
> Megabyte A measure of storage capacity; approximately 1 million characters. Abbreviated as Mbyte or Meg.
> Memory A storage area used by the computer to hold information.
> Menu A set of options or functions available to users in editing, formatting, generating reports, etc.
> Menu Manager A part of the Kernel that allows each site to manage the various options or functions available to individual users.
> ML Milliliters; a unit of volume used in the Intake and Output application.
> Modem An electronic device which converts computer signals to enable transmission through a telephone.
> Module A component of the nursing software application that covers a single topic or a small section of a broad topic.
> Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. The namespace is used as the prefix for all routines and globals used by the application. The nursing software uses NUR as its namespace.
> NPSB Nurse Professional Standards Board.
> Nursing Unit A nursing location which is found in the NURS Location (#211.4) file.
> Operating System The innermost layer of software that communicates with the hardware. It controls the overall operation of the computer such as assigning places in memory, processing input and output. One of its primary functions is interpreting M computer programs into a language the system can understand.
> Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions. For example, the NURS-SYS-MGR is the main menu for the Nursing application.
> Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within V*IST*A (e.g., the ADT and Intake and Output applications).
> Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with verify code).
> Patient Plan of Care Previously referred to as Nursing Care Plans. The following is a list of terms related to Patient Plan of Care:
> Additional Text Appears as an individual selection for the five basic components of the care plan. It is free text, ranging from 1-245 characters and can be used to clarify or individualize a patient's plan of care. Additional Text does not highlight and no '\*\*' precedes it when selected. Example: ADDITIONAL TEXT: Hard of Hearing.
> Aggregate Term An aggregate term is an element. Throughout the hierarchy of Patient Plan of Care when a selection is made in the development of a patient care plan, that selection is an element/aggregate term. In the Patient Plan of Care site configuration file the same holds true. When prompted with "Select Term to Add," you are adding an element/aggregate term, to that level of the Patient Plan of Care hierarchy.
> Aggregate terms may be either a Frame or a Term. An example of an aggregate term may be any of the following: altered cardiovascular status, Goals/Expected Outcomes, A-line patent, PA line.
> Appended Text that is entered by the user at the end of an element to further clarify the context of the patient data. (For example, if you choose to append the text for SIGNS AND SYMPTOMS OF INFECTION, you could add the terms REDNESS, SWELLING, DRAINAGE, etc., for clarification.).
> Classification A characteristic assigned to one or more aggregate terms in order to link the proper contributing factor (Etiology, Goals/Expected Outcomes, Interventions or Related Factors) or parent (Patient Specific Problems). The TERM 'wine with meals' is an Intervention, therefore, the classification is ORDERABLE and is displayed with Treatment Interventions/Orders.
> Contributing Factor One of the 5 basic components of a patient plan of care. The 5 contributing factors are:
1.  Defining Characteristics
2.  Etiology/related and/or risk factors
3.  Goals/expected outcomes
4.  Intervention/orders
5.  Related problems.
> Defining Characteristics Subjective/objective signs and symptoms indicative of a condition corresponding to a given Nursing Diagnosis. It is a contributing factor as well as a classification for "Defining Characteristics".
> Element A component or an essential part. It can be a TERM or FRAME and comprises the selections used to create a Patient Plan of Care. Example: below the knee amputation or altered cardiovascular status.
> Frame This is an element that is general and allows specific items or elements to be selected. A frame contains more selections or terms. Example:
> +A-line (FRAME)
1.  Calibrate and monitor on Adm. & PRN (TERM)
2.  Maintain good position of extremity.
> Goal A classification used to identify a Goal and/or Expected Outcome. A goal can be measurable or the final outcome of a problem. When used as date for reference or action 'Met' is associated with it.
> Goal/Expected Outcome Has two purposes:
1.  It is a contributing factor (major level), as well as;
2.  A classification for the "contributing factor" Goals/Expected Outcomes.
> Internal Text This is text that can be entered by the user to clarify the meaning of an element. Left and right brackets, \[ \], indicate the user will be asked to insert additional text to clarify the element. E.g., V/S q\[ \]h, 4 is inserted and text appears as V/S q\[4\]h.
> Intervention The classification for the contributing factor 'Intervention/ Orders'. It links all orders or interventions. Previously, this was named Nursing Interventions.
> Lead Text See Glossary Term under Patient Plan of Care "Text".
> Max The maximum number of selections that can be selected under a frame. This is normally left blank, when creating a site specific Patient Plan of Care there is no limit to the selections that can be made.
> Min The minimum number of selections that can be selected under a frame. The number one (1) is always entered when creating a site specific Patient Plan of Care indicating that at least one (1) selection must be made or the frame will not be included in the care plan.
> Orderable A classification that is used to link a name and/or frame to Intervention/Order. Orderable allows you to track the date of initiation and the date of discontinuation.
> PPC Patient Plan of Care (Previously called Nursing Care Plan). Prime Document A classification for the highest level of PPC.
> Related Factor The classification for the contributing factor for Related Problems. Related Problem One of the 5 basic contributing factors of the PPC.
> Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site. The site configuration option allows ADP coordinators to add to "already existing" medical diagnoses/nursing problems.
> Tabular The output format for PPC in which the frame and/or document is displayed.
> There are 3 types of output format, but only tabular is used with PPC.
> Term An element used to designate a specific/singular thought or idea. Ex., calibrate and monitor on Adm. & PRN.
> Text Lead and trail text are fields which should be used to provide additional information to FRAMES and TERMS usually associated with Intervention/Orders and Nursing Goals/Outcomes. This information, though useful, might exceed the frame's or term's 60 character field.
1.  Lead Text (for Terms) An example of lead text: The aggregate term under an Intervention should be "assess, monitor and document respiratory rate during activities". The key intervention is "respiratory rate during activities" but for clarity you need to include assess, monitor, and document. Therefore, you can build the aggregate term "respiratory rate during activities" under the frame Intervention/Orders and place the text "assess, monitor, and document" into the lead text field.
2.  Trail Text (for Terms) Example: The aggregate term under Intervention might be "assess for signs of fatigue and weakness" but you also need to note that the patient should be monitored and that the information must be documented. Therefore, by adding; " monitor and document" as trail text to the aggregate term, the following intervention can be displayed on the care plan: "assess for signs of fatigue and weakness; monitor and document."
3.  Lead and/or Trail Text (for Frames): Lead and/or Trail Text can be used in a FRAME so that you do not have to keep typing the same word or phrase to TERMS listed under FRAME. Ex. When a user selects the FRAME "refer for appropriate consult", he/she is asked to select the appropriate consult(s). When the Care Plan is printed the word "specifically" is printed following the element. "Specifically" is listed as a Trail Text in the site configuration file. The print would look like "refer for appropriate consult specifically (Physical Therapy, Chaplain)".
> PIMS Patient Information Management System previously known as the MAS Package. PO Per orum; refers to an item consumed orally or through the mouth.
> Pointer A special type of FileMan data that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
> Port An outlet in the back of the computer into which terminals can be connected. Printer A device for printing (on paper) data which is processed by a computer system.
> Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
> Protocol A single entry point referencing multiple routine entry points to execute several inter related, required processes which perform specific functions. When multiple protocols are associated with a single procedure (i.e., intravenous lines or IV lines), they are found grouped under a single option.
> Purge The deletion of data from a file.
> Qualifier A word that gives a more detailed description of an item.
> Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
> Required Field A field which the user must complete by entering requested data.
> Response Time The average amount of time the user must wait between the time the user responded to a question at the terminal and the time the system responds by displaying data and/or the next question.
> Restart/Recovery Procedures The actions necessary to restore a system's data files and computational capability after a system failure or penetration.
> \<RET\> Carriage return.
> Routine A set of commands and arguments, created, stored, and retrieved as a single unit in M.
> Risk Analysis An analysis of system assets and vulnerabilities to establish an expected loss from certain events based on estimated probabilities of the occurrence of such events.
> Security Key A function which unlocks specific options and makes them accessible to an authorized user.
> Security System A part of Kernel that controls user access to the various computer applications. When a user signs-on, the security system determines the privileges of the user, assigns security keys, tracks usage, and controls the menus or options the user may access. It operates in conjunction with MenuMan.
> Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
> Service Category A term used within the nursing software to categorize employees into six generic groups:
1)  registered nurse
2)  licensed practical nurse
3)  nursing assistant
4)  clerical staff
5)  administrative officer/assistant
6)  other
> The sixth category, other, can be used when (a) the first (1-5) categories are inappropriate, and/or (b) the FTEE should not be included in the above five FTEE category counts.
> Service Position A term used within the nursing software to categorize employees based on job descriptions. Examples of service positions are: staff nurse, LPN 5, NA 4, supervisor, clerk typist, etc.
> Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
> Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
> Subroutine A part of a program which performs a single function.
> Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
> Telecommunications Any transmission, emission, or reception of signs, signals, writing, images, sounds or other information by wire, radio, visual, or any electromagnetic system.
> Terminal A device used to send and receive data from a computer system (i.e., keyboard and CRT, or printer with a keyboard).
> Type(s) of Training A specific category of training class or program as defined in the PAID Education Tracking module. The categories are defined as mandatory training, continuing education, other/miscellaneous, and ward/unit-location training.
> UCI User Class Identifier. The major delimiter of information structure within the operating system.
> User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
> Utility An M program that assists in the development and/or maintenance of a computer system. VDT Video Display Terminal. Also called a Cathode Ray Tube (CRT).
> Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
> V*IST*A Veterans Health Information Systems and Technology Architecture. Ward/Unit Location See Nursing Unit.
