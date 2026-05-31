---
title: PXRM*2*4 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PXRM
app_name: Clinical Reminders
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*4
group_key: PXRM:PXRM:2
file_numbers: []
security_keys:
- PROVIDER
- PXRM MANAGER
menu_options: 1
description: '- # Patch 4 Release Notes - Clinical Reminders V. 2.0 Patch 4 Documentation - Installation Notes - Reminder Disclaimer/Health Summary Patch - [CSUB...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 12445
section_count: 26
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: ''
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_4_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_4_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=60
audit_applied: '2026-05-31'
master_source: PXRM*2*4 Release Notes
master_pub_date: ''
consolidated_from: 3 versions
prior_versions:
- PXRM*2*12 Release Notes
- PXRM*2*6 Release Notes
consolidated_title: release notes
---

![](pxrm-2-4-release-notes/001.png)

Clinical Reminders

PXRM\*2.0\*4

Release NotesOctober 2006

VistA HSD&D

# # Patch 4 Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Patch 4 Release Notes](#patch-4-release-notes)
  - [Clinical Reminders V. 2.0 Patch 4 Documentation](#clinical-reminders-v-20-patch-4-documentation)
  - [Installation Notes](#installation-notes)
  - [Reminder Disclaimer/Health Summary Patch](#reminder-disclaimerhealth-summary-patch)
  - [CSUB Explanation](#csub-explanation)
  - [> When a Reminder Test is run, some elements of the FIEVAL array have a "CSUB" subscript. Example for an orderable item finding:](#when-a-reminder-test-is-run-some-elements-of-the-fieval-array-have-a-csub-subscript-example-for-an-orderable-item-finding)
  - [General Functionality Changes](#general-functionality-changes)
  - [Reminder Computed Findings](#reminder-computed-findings)
  - [Reminder Definitions](#reminder-definitions)
  - [## Reminder Dialogs](#reminder-dialogs)
  - [Reminder Evaluation](#reminder-evaluation)
  - [Reminder Exchange](#reminder-exchange)
  - [Reminder Extracts](#reminder-extracts)
  - [Reminder Location Lists](#reminder-location-lists)
  - [Reminder Patient Lists](#reminder-patient-lists)
  - [Reminder Reports](#reminder-reports)
  - [Reminder Sponsor](#reminder-sponsor)
  - [Reminder Taxonomies](#reminder-taxonomies)
  - [Reminder Terms](#reminder-terms)
  - [## Geriatric Extended Care (GEC)](#geriatric-extended-care-gec)
  - [MyHealtheVet](#myhealthevet)
  - [## ## CPRS V26 Reminder Changes](#cprs-v26-reminder-changes)
  - [Remedy Tickets resolved with Patch 4](#remedy-tickets-resolved-with-patch-4)
  - [E3Rs Resolved](#e3rs-resolved)
- [Appendix A: Appointment Computed Findings](#appendix-a-appointment-computed-findings)
  - [Available Appointment Data Fields](#available-appointment-data-fields)
  - [Example:](#example)
- [Appendix B: HL7 Logical Link Set-up](#appendix-b-hl7-logical-link-set-up)
Summary of fixes and enhancements (details are provided in the following pages):
- Removal of support for the old-style MRD findings
- Restoration and updates of the disclaimer in the Clinical Reminders Health Summary output
- New versions of the VA-HTN ASSSSMENT BP \>= 140/90, VA-HTN ASSESSMENT BP \>=160/100 reminder definition, and VA-MHV INFLUENZA reminders
- Six new computed findings
- Error trapping enhancements
- New function finding (DIFF_DATE)
- Changes to the frequency display for CANNOT BE DETERMINED (CNBD)
- New finding modifiers, INCLUDE VISIT DATA and USE START DATE
- USE COND IN FINDING SEACH changed to USE STATUS/COND IN SEARCH
- Major changes to the user interface for patient lists
- A new key, PXRM MANAGER, for patient list options
- Many improvements to Reminder Reports, including expanded types of patient data that can be included in the Demographic Report
- Corrections and enhancements to GEC dialogs and reports, including a new option, Restore or Merge Referrals, in the GEC reports menu
- Name and description changes for Reminder Extract Management options

## Clinical Reminders V. 2.0 Patch 4 Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                   |                             |
|-------------------|-----------------------------|
| Documentation | Documentation File name |
| Release Notes     | PXRM_2_4_RN.PDF             |
| Technical Manual  | PXRM_2_4_TM.PDF             |
| Clinician Guide   | PXRM_2_4_UM.PDF             |
| Manager Manual    | PXRM_2_4_MM.PDF             |

## Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PXRM\*2\*4 disables old-style MRDs. The pre-init for patch 4 checks all reminder definitions to see if any still use the old-style MRD. If so, the build won't install and a MailMan message is sent to the Clinical Reminders mail group, listing the reminder definitions containing the old-style MRDs. *Replace any usage of old-style MRDs with Function Findings before proceeding with the installation.*Example Install Error Message:

Patch PXRM\*2\*4 cannot be installed because some reminders are still using

the old-style MRD. A message is being sent to the reminders mailgroup that

lists the reminders still using the old-style MRD. Please replace the old-style

MRD with a function finding.

 

PXRM\*2.0\*4 Build will not be installed, Transport Global deleted!

               Oct 10, 2006@15:33:29
- Several file names are changed in patch 4. During the installation of PXRM\*2.0\*4, KIDS will point out that these files already exist with a different name:

810.2 REMINDER EXTRACT DEFINITION

\*BUT YOU ALREADY HAVE 'REMINDER EXTRACT PARAMETER' AS FILE \#810.2!

Shall I write over your REMINDER EXTRACT PARAMETER File? YES//

810.7 REMINDER EXTRACT COUNTING RULE

\*BUT YOU ALREADY HAVE 'REMINDER EXTRACT FINDING RULE' AS FILE \#810.7!

Shall I write over your REMINDER EXTRACT FINDING RULE File? YES//

810.8 REMINDER COUNTING GROUP

\*BUT YOU ALREADY HAVE 'REMINDER FINDING GROUP' AS FILE \#810.8!

Shall I write over your REMINDER FINDING GROUP File? YES//

Take the default of "YES" for each of the "Shall I write over your xxx " questions.

## Reminder Disclaimer/Health Summary Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The disclaimer was not being displayed on the Clinical Reminders Health Summary output, so changes were made to restore and improve the display of the disclaimer.

- A package that calls the Clinical Reminder evaluation API passes an argument that requests the return of the Disclaimer; a change to the way this argument works was made and this required a change to the Health Summary routine that calls for Clinical Reminder evaluation, requiring creation of Health Summary patch GMTS\*2.7\*75.
- The FileMan text formatter was replaced with the Clinical Reminders text formatter so that "\\" can be used to force line breaks. In the past, the text was formatted every time a Health Summary was run. A new field was added to the Clinical Reminders Parameter file that stores the formatted disclaimer, eliminating the need to format it each time a Health Summary is run.

## CSUB Explanation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > When a Reminder Test is run, some elements of the FIEVAL array have a "CSUB" subscript. Example for an orderable item finding:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FIEVAL(5,"CSUB","DURATION")=1774

> FIEVAL(5,"CSUB","ORDER")=3366^CA ULTRA^546;99RAP

> FIEVAL(5,"CSUB","RELEASE DATE")=3010917.1625

> FIEVAL(5,"CSUB","START DATE")=3010917

> FIEVAL(5,"CSUB","STATUS")=PENDING

> FIEVAL(5,"CSUB","STOP DATE")=

> FIEVAL(5,"CSUB","VALUE")=PENDING

> Each of the subscripts following "CSUB" may be used in a Condition (hence the abbreviation Condition SUBscript), such as: I V("DURATION")\>90

> The use of "CSUB" data has expanded beyond Condition statements – the new places where it may be used are described in this document.

## General Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When Clinical Reminders V.2.0 was released, it was announced that support for the old-style MRD would be removed in a patch; this is the patch that removes it. The pre-init will check all reminder definitions to see if any of them are still using the old-style MRD. If any of them are, the build will not install and a MailMan message listing the reminders that are still using the old-style MRD will be sent to the Clinical Reminders mail group. These will need to be removed before the build can be installed. Replace any usage of the old-style MRD with a Function Finding.
- The installation instructions for PXRM\*1.5\*18 did not contain instructions to delete PXRMP18E and PXRMP18I, so we are deleting them in this patch.
- A bug which made it impossible to exit from the option PXRM EDIT WEB SITES was fixed.
- "Edit" was changed to "Add/Edit" in the menu text for the following options:

| Option                 | Old Menu Text              | New Menu Test                  |
|----------------------------|--------------------------------|------------------------------------|
| PXRM COMPUTED FINDING EDIT | Reminder Computed Finding Edit | Add/Edit Reminder Computed Finding |
| PXRM SPONSOR EDIT          | Edit Reminder Sponsor          | Add/Edit Reminder Sponsor          |
| PXRM TAXONOMY EDIT         | Edit Taxonomy Item             | Add/Edit Reminder Taxonomy         |
| PXRM TERM EDIT             | Reminder Term Edit             | Add/Edit Reminder Term             |
| PXRM LOCATION LIST EDIT    | Edit Location List             | Add/Edit Reminder Location List    |

- CLASS, SPONSOR, REVIEW DATE, and EDIT HISTORY are standard fields and are stored in standard locations across the Clinical Reminders files. When the Location List file \#810.9 was created in V.2.0, only the CLASS field was created and it was not put in the standard location. To correct this, the data dictionary was changed to add the fields in the standard locations. The pre-init saves the original class values, and a post-init puts them in the correct location. The Location List editor and the print template for Location List Inquiry were changed to include all the fields.

> The same changes as described above were made for CLASS and REVIEW DATE fields of the SPONSOR file, \#811.6.

> The pre-init for PXRM\*2.0\*4 stores any existing CLASS and SPONSOR CLASS values in ^XTMP("PXRMLLCS") and ^XTMP("PXRMSPCS") so they can be restored to the correct location by the post-init. These ^XTMP globals can be deleted after a successful installation.

- When submitting jobs to TaskMan, the following prompt was used:

> Enter the date and time you want the job to start.

> It must be on or after 03/09/2006@06:49:14

This was changed to:

> Enter the date and time you want the job to start.

> It must be on or after 03/09/2006@06:49:14

> Start the task at:

- When a reminder mail group was defined, the line count for the error message was not being set. This was corrected. Remedy ticket \#136439.

## Reminder Computed Findings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- "RACE" was added as a CSUB subscript to the VA-RACE 2003 computed finding; this will give a list of all the races found for a patient, up to the number for OCCURRENCE COUNT. This list can be used in the CONDITION; for example:

> I (V("RACE","\*")\["WHITE")&(V("RACE","\*\*")\["INDIAN")

- If a document class and a note title were exactly the same and the document class had an IEN lower than the title IEN, then the progress note computed finding (VA-PROGRESS NOTE) used the document class IEN to look for a note which did not exist. This was changed so that it makes sure the IEN is for a title.
- The following additional CSUB data was added to the VA-PROGRESS NOTE computed finding:
- V("DISPLAY NAME")=Display name of TIU title.
- V("EPISODE BEGIN DATE/TIME")=String\_":"\_EPISODE BEGIN DATE/TIME

> where String is "Adm" for ward locations and "Visit" for all other location types. Date/time is in MM/DD/YY format.

- V("EPISODE END DATE/TIME")=String\_" "\_EPISODE END DATE/TIME where string is null if no date/time or "Dis: " if date/time exists. Date/time is in MM/DD/YY format
- V("HOSPITAL LOCATION")=External format of HOSPITAL LOCATION from TIU DOCUMENT file
- V("NUMBER OF IMAGES")=Number of images associated with TIU DOCUMENT Entry
- V("REQUESTING PACKAGE")=REQUESTING PACKAGE REFERENCE field from TIU DOCUMENT file (internal format)
- V("SUBJECT")=SUBJECT (OPTIONAL description) field from TIU DOCUMENT file (note that characters are limited to ensure that the returned string is not longer than 255 characters). (This piece was added with TIU\*1\*63)
- A number of national computed findings were setting the date of the finding to Today and this caused a problem when a reminder report was run with the Effective Date in the past. In this situation, the date of the computed finding should be the date entered for the Effective Date. The following computed findings were changed to correct this: VA-AGE, VA-DATE OF BIRTH, VA-DATE OF DEATH, VA-ETHNICITY, VA-RACE 2003, VA-RACE PRE 2003, VA-SEX, VA-VETERAN, VA-WH MAMMOGRAM IN WH PKG, VA-WH MAMMOGRAM ABNORMAL IN WH PKG, VA-PAP SMEAR ABNORMAL IN WH PKG, VA-WH PAP SMEAR IN LAB PKG, and VA-WH PAP SMEAR IN WH PKG.
- To make its function clearer, the computed finding VA-DISCHARGE DATE was renamed to VA-LAST SERVICE SEPARATION DATE.
- VA-DATE OF DEATH was changed so that the date of the finding is the date of death; previously the date of the finding was the evaluation date.
- The following new national computed findings are included in this patch:
- VA-APPOINTMENTS FOR A PATIENT (multiple) - Returns a list of appointments for a patient. The appointments can be filtered by a number of criteria which are documented in the Clinical Reminder Manager Manual.
- VA-PATIENTS WITH APPOINTMENTS (list) – Returns a list of patients with appointments; used for patient list-building. The appointments can be filtered using the same criteria as for VA-APPOINTMENTS FOR A PATIENT.
- VA-PATIENT TYPE (single) - Returns true if the TYPE field in the Patient file (file \#2) has a value and returns the Type of Patient (e.g. Active Duty, Veterans) as the value, which can be used in a Condition.
- VA-PTF HOSPITAL DISCHARGE DATE (multiple) - Returns a list of discharge dates from the PTF file. By default, fee basis and census records are not included, but can be included through the computed finding parameter.
- VA-REMINDER DEFINITION (single) - Evaluates a reminder definition and returns the reminder status as the value, which can be used in a Condition. The Status, Due Date, and the Last Done Date are returned as CSUB items so they can be used in a Condition.
- VA-TREATING FACILITY LIST (multiple) – Returns a list of treating facilities, i.e., systems that store data related to a patient.

## Reminder Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Editing

- Extensive changes were made to the STATUS LIST editing functionality; these are described in the updated Clinical Reminders Manager Manual.
- Editing of IGNORE ON N/A was moved from the Baseline section to the General Section.
- A change was made that allows term editing in Add/Edit Reminder Definition. In the past, this could only be done if the term was national.
- Checking for baseline age range overlap was moved from reminder evaluation to definition editing, to make reminder evaluation more efficient. This checking will still be done during reminder evaluation when the reminder test option is used. The post-init for PXRM\*2\*4 will check all reminder definitions for overlapping age ranges. Any definitions found to have overlapping age ranges will be listed during the install.
- Reminder edit was changed so that an age range can be entered for a frequency of 0Y.
- When a sponsor is added, a check is made to see if the sponsor class and the class of the file to which the sponsor is being added are the same. If they are different, a message to this effect is displayed. There was a bug in the output that caused the class to be displayed as null. This was corrected.
- A bug occurred when editing the CUSTOM DATE DUE string that would allow the string to be stored with lower-case characters, which could cause the date calculation to fail. This was corrected by making sure the string is always stored in upper-case, no matter what case the user has entered

Finding Modifiers

- A new finding modifier, INCLUDE VISIT DATA, was added. This modifier applies only to V file findings. The default value is "NO," but when it is set to "YES," the following CSUB data will be returned: COMMENTS, DATE VISIT CREATED, DFN, DSS ID, HLOC, HOSPITAL LOCATION, LOC. OF ENCOUNTER, OUTSIDE LOCATION, SERVICE CATEGORY, STATUS, STOP CODE, and VISIT.
- The finding modifier, USE COND IN FINDING SEARCH, was renamed to USE STATUS/COND IN SEARCH. When this field has a value of "YES," the STATUS LIST and/or CONDITION will be applied to each result in the date range. Only results that have a status on the list or for which the CONDITION is true will be retained. The maximum number to retain is specified by the OCCURRENCE COUNT.

> NOTE: If a finding has both a STATUS LIST and a CONDITION, the status check is made first; the CONDITION will be applied only if the finding passes the status check.

- A new finding modifier called USE START DATE was added; it applies only to findings that have a Start Date and a Stop Date. When USE START DATE is true, the Start Date will be used as the date of the finding. The default behavior for drug findings is to use the Stop Date as the date of the finding, while for orderable item findings, the default is to use the Start Date as the date of the finding. When USE START DATE is "YES," date-matching is now done based solely on the Start Date being in the date range defined by Beginning Date/Time and Ending Date/Time. When USE START DATE is "NO," date-matching is based on any overlap between the date range defined by Start Date and Stop Date and the date range defined by Beginning Date/Time and Ending Date/Time.

Function Findings

- The check of the subscripts used in Function Finding functions was enhanced. When the user types in a function string, the arguments for each function in the string are checked to make sure there are the correct number of arguments and the arguments are of the correct type.
- The following new functions were added:
- DIFF_DATE - Returns the absolute value of the difference in days between two findings.
- VALUE - Allows the comparison of CSUB values between different occurrences of the same finding and between different findings. It has the form VALUE(FINDING,OCCURRENCE,"CSUB"), where FINDING is the finding number, OCCURRENCE is the occurrence, and "CSUB" is the particular CSUB subscript to check. Using the orderable item example from above, you could check that the first occurrence had a duration greater than 30 days with the function string VALUE(5,1,"DURATION")\>30.
- A change was made so that any of the Clinical Reminder global variables (PXRMAGE, PXRMDOB, PXRMDOD, PXRMLAD, and PXRMSEX) can be used in a Function Finding.

Miscellaneous

- The input transform for Lab findings was allowing all types of Lab findings. This was changed so that it does not allow BB and WK data which are not indexed and cannot be used as reminder findings.
- The phrase "wildcard fist" was corrected to read "wildcard first." This is seen when working with status lists.
- The status check was changed to make it more efficient.
- Duration was added to the "CSUB" data list for orderable item and drug findings.
- At any prompt for a reminder definition, such as in reminder due reports or reminder list rules, if users typed "?" they saw the prompt:

> Answer with REMINDER DEFINITION NAME, or PRINT NAME, or USAGE, or FINDING ITEM"

> This was corrected so that now the prompt is:

> Answer with REMINDER DEFINITION NAME, or PRINT NAME

Definitions Distributed in PXRM\*2\*4

- The general resolution not found text in the VA-MST SCREENING reminder had a spelling error. The line:

> All veterans should be screened at least once is their lifetime for

> was changed to:

> All veterans should be screened at least once in their lifetime for

- The two national reminders, VA-HTN ASSESSMENT BP \>=140/90 and VA-HTN ASSESSMENT BP \>=160/100, were originally distributed with findings 19 through 26 as drug classes that were informational findings. Because these are drug classes, they add considerable processing time to the reminder evaluation. To speed up the reminder evaluation, these findings were removed.
- Also for VA-HTN ASSESSMENT BP \>=160/100, the reminder description was updated and Beginning Date was changed from T-3M to T-2Y for finding items 27 and 28. Finding item 28 was removed from the resolution logic.

## ## Reminder Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A misspelling in dialog help text was fixed:

> element/group should be replace or suppress

> was changed to:

> element/group should be replaced or suppressed

- The following informational message:

> Cannot modified lock group from a higher level view

> was changed to:

> Cannot modify lock group from a higher level view

- A problem with the user being able to delete dialog groups/elements from a National Reminder dialog was fixed.
- M errors occurred when adding a sequence number less than 0 or when adding an invalid sequence number such as "10-". Code to handle these cases was added so the M errors no longer occur.
- An undefined error that occurred when deleting a Replacement Element/Group from a Dialog element/group was fixed.
- If a term used in branching logic had a Condition that used one of the PXRM special variables, such as PXRMSEX, it would fail because the special variables were not being defined. The code was changed to make sure they are defined.

## Reminder Evaluation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In V.2.0, error trapping was added so that if a request to evaluate a non-existent reminder is made, a message is sent to the reminders mail group. The only information available to Clinical Reminders is the IEN of the non-existent reminder, so that is all that can be included in the message. In order to make it easier to track down what application is requesting the evaluation of a non-existent reminder; code was added to put an entry in the error trap. The error trap entry will contain the complete symbol table which should help in determining what application is calling for the evaluation of a non-existent reminder.
- For findings that have a Start Date and Stop Date, if the Stop Date is missing, then for evaluation purposes, the Stop Date is set to Today. The Duration function was using 0 instead of Today. This was corrected.
- A bug was found when building lists of orderable items that could have caused some orderable items without a Stop Date to be missed. This would occur if there was an orderable item that had a Stop Date immediately before or after the orderable item that did not have a Stop Date. This was corrected.
- The date range overlap calculation used for findings that have a start and stop date had an error: it would not correctly determine if the date ranges defined by beginning date-ending date and start date-stop date overlapped when BDT \> START DATE. This was corrected.
- The code for evaluation of drug class findings was rewritten to speed it up.
- For orderable items and non-VA meds that may not have a stop date, you could get a different result, depending on the value of the OCCURRENCE COUNT, because the search was not looking at all possible entries (as a result of the missing stop date). This was corrected.
- Drug class findings were only allowing for one occurrence of each drug in a drug class, even when the OCCURRENCE COUNT was greater than 1. This was corrected. Remedy ticket \#134199
- The output for VA Generic drug findings was adding an extra blank line; the extra blank line was removed.
- The evaluation date was always getting set to Today when an Effective Date other than today was entered. This was corrected.
- Symbolic date handling was changed so that it properly handles time.
- Reminder Test was changed to take an Effective Date so the user can easily see the results of an evaluation on a past date.
- Redundant display of cohort logic in the test option output was corrected.
- The reminder test option allowed the selection of reminders whose usage is "Reminder Patient List." Regular evaluation of patient list reminders generates errors, so a screen was added to prevent selection of patient list reminders.
- When there was a date of death for a patient, the reminder was still showing as applicable. This was corrected so that reminders are N/A for dead patients.
- When a CUSTOM DATE DUE was used, no age range information was being displayed in the Clinical Maintenance output. Display of age range information was added. Also, a check was added so that age range information is displayed only if the Patient Cohort Logic contains AGE. This applies both when a CUSTOM DATE DUE is used and when a regular date due calculation is done.
- A problem with the resolution date calculation was reported in Remedy ticket \#106498. This would happen if a regular finding was "anded" with a function finding in the resolution logic and the regular finding was true while the function finding was false. This was corrected.
- There was a bug in the resolution date calculation that caused it to return 0 instead of a non-zero date when the operator was "&" and one of the two dates was 0. It now returns the non-zero date.
- The general and summary resolution not found text was being displayed even if the reminder was N/A. This was corrected.
- The phrase "Frequency 0Y Not Indicated" was changed to "Frequency 0Y Not indicated."
- Several changes were made in response to PSI-05-099:

> If a frequency cannot be determined for a patient, the Status and Due Date will both be CNBD (CanNot Be Determined) and the frequency display that follows the status line will be:

> Frequency: Cannot be determined for this patient.

- The date due calculation was restructured and streamlined.
- The output code for a lab test was expecting the specimen to exist, which may not be true for a micro test. The code was changed to check for the existence of a specimen before trying to print it.
- During testing, the following situation was encountered: a test site had a reminder definition with a finding that is a term; the term is mapped to a taxonomy and a health factor, and a status list is defined at the definition level. During reminder evaluation, the status list was being applied to all the term findings, which was generating an error for the health factor, since health factors do not have a status. This code was changed to properly handle this situation.
- Store errors in FPDAT^PXRMVCPT were reported in Remedy ticket \#87364. The code was changed to prevent this. All the routines used in taxonomy evaluation were changed to make sure that a similar store error would not occur in them.
- When there were multiple occurrences in a taxonomy the output was not correct for the second and higher occurrence. In some cases, this would cause an undefined subscript error; this was corrected. Remedy ticket \#109645.
- The API used to get Mental Health data does not understand "\*" for the number of occurrences, so when USE STATUS/COND IN SEARCH was true, the lookup was failing. To get around this, a check was made for the limit being "\*" and if it occurs, it is replaced by 99.

## Reminder Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- During exchange install, a check was being made for a lab finding by doing a \["60"; this caused problems because file \#50.605 also contains "60" so the test for a lab panel was inappropriately being applied to a VA Drug Class finding. This was corrected by changing the test to "=60".
- Patch PSN\*4\*99 created several VA Drug Class entries with exactly the same name. When there were multiple entries with the same name, installation of a definition, term, or dialog via Reminder Exchange would fail, because FileMan could not resolve the pointer. Exchange has been changed so that now when there are multiple entries, the user is presented with the Name, the IEN, and any identifiers, and is asked to select the appropriate one to use. Whenever a packed reminder is selected for the IFE action, a warning will be issued for each component that does not have a unique .01.
- A display problem with Reminder dialogs that contain Branching Logic was fixed. The display of replacement elements was changed so that they will appear at the end of the list.

## Reminder Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The original version of extracts included test patients in the patient list and total count. This has been changed, so when the patient list is built, test patients will not be included unless the user specifies that they be included. This will make the extract counts slightly different; test patients were included in the N/A count, so this will change.
- The reminder evaluation loop used in extracts was restructured to make it run faster. Two test extracts run in approximately 2/3 of the time they previously required.
- The Hep C. EPI extract summary will now automatically be deleted from the local system after five years.
- The utilization count functionality was changed to count historical entries that were entered within the reporting period, even if the date of the visit is outside the reporting period. It was also changed to count all occurrences of every finding in a reminder term.
- The status for the Reminder Extracts was not showing up in the screen display for the Transmission History because the ACK messages coming from the Austin Automation Center were not correctly formatted; Austin corrected the format. The original storage location for Transmission Status is purged on a regular basis so Transmission Status was moved to a permanent location.
- In conjunction with the date changes described in the Patient List section symbolic beginning dates were changed from T to BDT in the following finding rules that are used for the QUERI extracts:

> VA-\*IHD QUERI 412 DIAGNOSIS

> VA-\*IHD QUERI ANCHOR VISIT

> VA-\*IHD QUERI DIAGNOSIS

> VA-\*IHD QUERI LIPID LOWERING MEDS

> VA-\*IHD QUERI QUALIFYING VISIT

> VA-\*MH QUERI QUALIFY MH VISIT

> VA-\*MH QUERI QUALIFY PC VISIT

- To make reminder extracts easier to understand, these changes were made:
  1.  Extensive new descriptions were added to the data dictionaries used for reminder extracts.
  2.  Some of the options, protocols, and List Manager templates were renamed.
  3.  A number of the fields were renamed.
  4.  The help text was updated.
  5.  The display of list rules was changed to make it easier to read.
  6.  The following file names were changed:

| File \# | Old Name                  | New Name                   |
|-------------|-------------------------------|--------------------------------|
| 810.2       | REMINDER EXTRACT PARAMETER    | reminder extract definition    |
| 810.7       | REMINDER EXTRACT FINDING RULE | REMINDER EXTRACT COUNTING RULE |
| 810.8       | REMINDER FINDING GROUP.       | REMINDER COUNTING GROUP        |

- During the install, KIDS will point out that these files already exist with a different name:

> 810.2 REMINDER EXTRACT DEFINITION

> \*BUT YOU ALREADY HAVE 'REMINDER EXTRACT PARAMETER' AS FILE \#810.2!

> Shall I write over your REMINDER EXTRACT PARAMETER File? YES//

> 810.7 REMINDER EXTRACT COUNTING RULE

> \*BUT YOU ALREADY HAVE 'REMINDER EXTRACT FINDING RULE' AS FILE \#810.7!

> Shall I write over your REMINDER EXTRACT FINDING RULE File? YES//

> 810.8 REMINDER COUNTING GROUP

> \*BUT YOU ALREADY HAVE 'REMINDER FINDING GROUP' AS FILE \#810.8!

> Shall I write over your REMINDER FINDING GROUP File? YES//

> Take the default of "YES" for each of the questions.

- Reminder Extract output was changed, so that the prompt "Transmit results to AAC" will not be displayed when running a local or a VISN level extract.

## Reminder Location Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Location List Inquiry was not displaying the list of Credit Stops to Exclude. They were added.
- Location List Edit was changed so the user cannot "^" out when the class of the Location List and class of the sponsor do not match. Jumping back to the previous field is now allowed during location list editing.
- Location List findings were modified to check the status of the appointment associated with the visit, to make sure it is valid. Only those visits with valid statuses are kept on the list. Statuses that are considered invalid are: CANCELLED BY CLINIC, CANCELLED BY CLINIC & AUTO RE-BOOK, CANCELLED BY PATIENT, CANCELLED BY PATIENT & AUTO-REBOOK, DELETED, NO ACTION TAKEN, NO-SHOW, and NO-SHOW & AUTO RE-BOOK. The same check is now used in reminder due reports, so lists made either way should be consistent.
- A new "special" Location List called VA-ALL LOCATIONS was created. When this Location List is used, the "AHL" index of the Visit file is searched to create a list of every hospital location for which one or more visits have been recorded. The list can be filtered, using a Condition, with things such as service category, stop code, and hospital location. Any of the "CSUB" data that is seen when INCLUDE VISIT FILE DATA is true may be used.
- The print template used for displaying the entire list of Location Lists was changed to make the output easier to read.

## Reminder Patient Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Major changes were made to the user interface for patient lists. Now when the Patient List option is selected, the user will see all the Patient Lists that they have access to. Additionally, the type of list (public or private) and the user's access (full or view) are displayed.
- In the past, a patient list was marked as private by storing the creator. This meant that no creator was stored for public lists. Several changes were made affecting this:
1.  A new field, TYPE, was added to file \#810.5. It is used to mark a list as public or private.
2.  The creator is now always stored and displayed.

> A user's access to a particular list is now determined by first checking the TYPE field to see if it is public or private. If it is public, then the user has full access. If it is private and the user is the creator, the user has full access. If the user is not the creator, then the list of authorized users is checked, and if the user is on the list, he or she has view access.

- Changes were made so that all the date input used when building a patient list can be in symbolic form like T-1Y.
- Beginning Date/time and Ending Date/time were added to the rule set sequence multiple, so each sequence in a rule set can have its own date range. The precedence of dates is as follows: term or definition \> list rule \> rule set.
- Changes were made to the way that dates are handled in patient list-building. Dates will be overridden according to the following order of precedence:

> List Build (LB) \< Rule Set (RS) \< Finding Rule (FR) \< Term/Definition (T/D)

> This is in contrast to the previous method in which the changes were cumulative.

- Symbolic dates that can be used in RSs and FRs are BDT=LBBDT and T=LBEDT. In terms and definitions only T can be used.
- If RS, FR, or T/D dates are null, they will be replaced by LB dates. RS, FR, or T/D dates are considered to be null if both the beginning and ending dates are null.
- If BDT is defined and EDT is null, then EDT will be set to T@23:59.
- If EDT is defined and BDT is null, then BDT will be set to the beginning of data.
- Whenever T is used in a reminder rule, it will take the value of the final ending date/time that is determined according to the order of precedence list above. Only the ending date applies to reminder rules, so a change was made so that only the ending date is prompted for when editing list rules that are reminder rules and rule sets, where the sequence finding is a reminder rule.
- The rule set display was changed so that when the rule is a reminder rule, only the ending date is displayed.
- A new action, TEST, was added to the List Rule Management Screen. This action applies only to rule sets; it shows how the rule set will be processed and the beginning and ending dates used for each of the findings in the terms or definitions used in the rule set.
- There was a logical error in term evaluation during rule set processing; if any of the findings mapped to the term were true, the term was being set to true. This violates the way terms normally work, where the term takes on the value of the most recent finding whether it is true of false. This was corrected
- Accumulation and building of the list of patient lists was moved from local arrays to globals to prevent store errors in the future as the number of lists at sites grows.
- A new key, PXRM MANAGER, was created. Holders of this key will have full access to all patient lists, including editing, deletion, and adding users.
- A list edit function was added to the Patient List Patients screen. The list creator can edit NAME and TYPE. Holders of the PXRM MANAGER KEY can edit NAME, CREATOR, and TYPE.
- The list delete functionality was changed so the user must either be the creator or hold the PXRM MANAGER key in order to delete a list.
- Code was added to ask the user whether or not to include dead and test patients on a patient list. The default is to not include them.
- Extensive changes were made to how patient list-building handles deceased patients, to bring it into complete alignment with the handling of deceased patients in reminder due reports.
  - Now if the "Include deceased patients on the list?" prompt is answered affirmatively, deceased patients will be included on the list.
  - If the response is "NO", the default, no deceased patients, will be included on the list.
  - QUERI extracts require that deceased patients who were alive sometime during the reporting period are included on the extract patient list. To be able to continue to support this requirement, in view of the above change, several additional changes were required. Two new fields, INCLUDE DECEASED PATIENTS and INCLUDE TEST PATIENTS, were added to the Extract Sequence Multiple of the Reminder Extract Definition file. The post-init sets INCLUDE DECEASED PATIENTS to true and INCLUDE TEST PATIENTS to false for all the QUERI extracts.
  - The national computed finding VA-DATE OF DEATH was changed so that the date of the finding is the date of date; previously the date of the finding was the evaluation date.
  - A new national term VA-DATE OF DEATH that is mapped to this computed finding was created. This term is used in the new national finding rule VA-FR-DATE OF DEATH. This finding rule can be used to remove patients who died before the start of the reporting period. This finding rule was added to all the QUERI rule sets. The computed finding VA-DATE OF BIRTH was changed so the date of the finding is the date of birth. The updated rule sets will be distributed via Reminder Exchange as part of patch 4. The name of the Exchange entry is VA-\*QUERI LIST RULE UPDATES.
- In the past, when a patient list was overwritten or deleted, the patients on the list were removed one at a time. This was replaced with a more efficient operation that kills the entire list of patients at once.
- A mechanism to document how a list was created was added. A word-processing field, CREATION DOCUMENTATION, was added to file \#810.5 as a place to store the information. Creation Documentation is viewable by selecting the DCD action on the main patient list screen. When a patient list is created by an extract, the Creation Documentation will be created automatically. Note that patient lists created prior to installing PXRM\*2.0\*4 will not have any information in this field.
- There was a bug in the display of reminder rules; it was not displaying the correct name for the reminder. This was corrected.
- The rule set error-checking that takes place before the rule set is evaluated was enhanced to look for more possible problems.
- The Copy Patient List action code was made more efficient.
- The Patient List menu was changed to display parentheses around the View User action, which signifies it is not selectable, if the patient list is a public list.
- Originally, when the Health Summary Individual action was selected, the user was prompted to select a list of patients, and then for each patient selected, was prompted to select the health summary to use. This was changed so that the user selects a list of patients and then selects a single health summary that will be used for all the selected patients.
- When a patient list was copied into an OE/RR Team, there was a bug that caused the wrong patients to be copied. This was fixed. Remedy ticket \#85633.
- A new field, AUTOMATICALLY PURGE, was added to Reminder Extract Summary file \#810.3 and Reminder Patient List file \#810.5. Each entry where this field is true will be automatically deleted whenever it is more than five years old. The init for PXRM\*2.0\*4 will set this field to true for all national Extract Summaries and Patient Lists. When users create a manual extract or a patient list, they will be prompted to enter a value for this field. All national extracts and patient lists created after installing PXRM\*2.0\*4 will have this field set to "YES".
- The field PRIMARY STATION in the patient list multiple of file \#810.5 was renamed to PCMM INSTITUTION to reflect what is really stored in the field.
- All references to Facility in the patient list display were changed to Institution. This better reflects what is actually stored; it is the Institution which is determined by finding the patient's PCMM Team and then the Institution for that Team. The display now will show the Institution name. It will continue to display the Institution IEN for lists built before PXRM\*2\*4.
- A print template was being used to display rule sets, which meant if a sequence was added out of order, it would display out of order. For example, a rule set with four steps has sequence 2 deleted and then added back. This display would look like this:

> Sequence: 001

> List Rule: FR-DIABETIC DIAGNOSIS

> Description: This is a taxonomy for diabetic diagnosis.

> Rule Type: FINDING RULE

> Reminder Term: DIABETIC DIAGNOSIS

> Operation: ADD PATIENT

> Sequence: 003

> List Rule: FR-BMI

> Description: Patient's BMI

> Rule Type: FINDING RULE

> Reminder Term: BMI

> Operation: INSERT FINDING

> Sequence: 004

> List Rule: FR-FINGERSTICK

> Description:

> Rule Type: FINDING RULE

> Reminder Term: FINGERSTICK, GLUCOSE

> Operation: INSERT FINDING

> Sequence: 002

> List Rule: VA-\*IHD QUERI ASSOCIATE PRIMARY CARE STATION

> Description: Associate primary facility.

> Rule Type: FINDING RULE

> Reminder Term: VA-IHD STATION CODE

> Operation: INSERT FINDING

- The print template was replaced with a routine, so the rule set will always be displayed in sequence order.
- If a reminder rule was selected for display/edit, there was a hard error; this was corrected. Here is an example of the error:

> <u>Display/Edit Rule Sep 23, 2005@15:03:11 Page: 0 of</u>

> S BEG=\$S(\$D(@VALMAR@(BEG,0)):BEG,1:0)

> ^

> \<SUBSCRIPT\>PAGE+1^VALM4

- There was a hard error when listing a rule set if one of the sequences did not have a list rule. This was corrected.
- A change was made to the date check to allow future dates. In conjunction with the new appointment computed findings described above, patient lists can be built based on future appointments.
- There was a bug for list-building, based on Problem List entries. When a list was built with the ending date in the past, chronic problems were not being included. This was corrected.
- There were several bugs for building patient lists for non-CH lab findings. These were corrected.
- The help for list rules and patient lists was improved.
- Toggling between sorting patient lists by name and by type (public or private) was not working, this was corrected.
- Deleting a list rule from a sequence in a rule set generated a subscript error. This was corrected.
- The Demographic Report was rewritten and the types of patient data that can be included were expanded; this includes most of the data that can be obtained from the following VADPT calls: ADD, DEM, ELIG, and IN, the choices now include:

> Select from the following address items:

> 1 - CURRENT ADDRESS

> 2 - PHONE NUMBER

> Select from the following future appointment items:

> 1 - APPOINTMENT DATE

> 2 – CLINIC

> Select from the following demographic items:

> 1 - SSN

> 2 - DATE OF BIRTH

> 3 - AGE

> 4 - SEX

> 5 - DATE OF DEATH

> 6 - REMARKS

> 7 - HISTORIC RACE

> 8 - RELIGION

> 9 - MARITAL STATUS

> 10 - ETHNICITY

> 11 – RACE

> Include the patient's preferred facility? N//

> Select from the following eligibility items:

> 1 - PRIMARY ELGIBILITY CODE

> 2 - PERIOD OF SERVICE

> 3 - % SERVICE CONNECTED

> 4 - VETERAN

> 5 - TYPE

> 6 - ELIGIBILITY STATUS

> 7 - CURRENT MEANS TEST

> Select from the following inpatient items:

> 1 - WARD LOCATION

> 2 - ROOM-BED

> 3 - ADMISSION DATE/TIME

> 4 - ATTENDING PHYSICIAN

- If a finding rule is added to a rule set with the insert operation, then any of the CSUB data associated with the term's finding will be available for inclusion on a demographic report. The name of the finding (FINDING NAME) will also be available.
- For patient lists created from a Reminder Due Report, the Patient Demographic Report can include reminder status, due date, and last done date for each reminder used in the report.
- Two problems with the display of patient names were identified:
1.  If there are two patients with exactly the same name, only one shows on the demographic report - the other is missing.
2.  If two patients have exactly the same name except for the middle initial (one with no MI and the other with one), then the order in which they display is different in the patient list and in the patient list with the demographics.

> Both of these problems were corrected.

- The delimited Patient Demographic Report was changed to allow the user to choose the delimiter.

## Reminder Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In support of the Scheduling redesign, Reminder Reports were changed to use a new Scheduling API to gather appointment data. At some point in the future, this API will be changed, so that instead of getting appointment data from the local VistA system, it will go across the VA WAN to get appointment data from a national Scheduling database. When this happens, users will probably see a slow-down in the reminder report processing. Also, the Scheduling API may return an error code stating that it could not gather data from the national database. If this happens, the reminder report will be canceled, the print task will be removed from TaskMan, and an error message will either display on the screen or be sent via MailMan to the requestor of the report, giving the error returned from the Scheduling API.
- Because of the potential for delay when the Scheduling API starts going across the VA network to retrieve appointment data, several changes were made in how Reminder Reports were evaluated. One of the major changes was to no longer do the prior encounter look-up by date range and then by location. The new code will build a list of appropriate locations and then use an index in the Visit file that is by location and date range. This change may affect the total number of patients on the report. The reason is the original report code used the facility assigned to the visit directly, while the new report code is using the facility assigned to the clinic that is associated with the visit. Over time, if a clinic moves from one facility to another facility, the report will evaluate the current facility that the clinic belongs to. This will definitely affect reports run against a service category of "E." This happens because when entering historical data in PCE, a clinic cannot be entered; instead the facility is picked by the user and is assigned to the visit. If that is the case, the historical visit will not be picked up for the report. This change should not have any effect on the actual evaluation process.
- The new Scheduling API is also used for detailed reports that display next appointments and for the previous encounter reports to check for no-shows.
- A problem with detailed retrospective reports returning the next appointment date based on the report end date and not the report run date was corrected. This could cause the next appointment date to be after the report end or before the report run date. For historical reports, the next appointment date is based on the date the report was run.
- Before patch 4, a deceased patient and/or test patient would be counted in the total number the report was run against. The evaluation status would always be N/A for these patients. With patch 4, there are two new prompts:

> "Include deceased patients on the list?" and

> "Include test patients on the list?"

> Unless the user answers yes for these prompts, deceased and test patients will not be included in the total number of patients the report is run against.

- Normally when a patient is deceased, the status of the reminder is automatically set to "N/A." A new flag for use in Reminder Reports was added that can be used to override this behavior and cause the status to be determined as usual. This change was made so that if the "Include deceased patients on the list?" prompt on a Reminder Due Report was answered as "yes," normal evaluation can be done.
- The problem with Reminder Due Reports freezing for an individual patient who is deceased was fixed.
- The Effective Date/Time was added to queued delimited reports.
- The following text was changed:

> WARNING - REMINDER COULD NOT BE DETERMINE; REPORT RESULTS MAY BE INCORRECT!

> Reminder: REMINDER NAME had a total of 1 evaluation errors.

> to

> WARNING - REMINDER STATUS COULD NOT BE DETERMINED; RESULTS MAY BE INCORRECT!

> Reminder:  REMINDER NAME had a total of 1 CNBD errors.

- To satisfy the concerns of the Database Administrator, the method of storing the list of service categories in a report template was changed from a set of codes to free text. The list of service categories that can be used was expanded to include all the service categories allowed in the Visit file. The post-init will automatically change the service categories in all existing Reminder Report Templates to the new format. *Please check the templates you regularly use to make sure the list of service categories is correct. Note that in the past the list was just letters, now it is a comma-separated list of letters.*
- When multiple hospital locations are selected and some of them do not have patients, the list of locations that do not have patients is displayed in this format:

> The following Location(s) had no patients selected

> OLDDOM (SALT LAKE CITY HCS)

> RAD ROOM (SALT LAKE CITY HCS)

> ULTRASOUND CLINIC (SALT LAKE CITY HCS)

> This information was not being displayed when the report was queued. The problem has been corrected.

- Location Lists and Sponsors were added to the Review Date Report.
- The misspelling "Efffective" in the prompt "Enter EFFECTIVE DUE DATE:" was corrected.
- There was a subscript error at MULT+32^PXRMXT, trying to setup service category, when a report template was based on future appointments. This was corrected.
- The prompt "Select an existing REPORT TEMPLATE or return to continue:" needed a space after the colon, the space was added.
- The problem with no patients being found for Reminder Due Reports, based on future appointments at selected hospital locations, was fixed.
- When the list of patients was based on an OE/RR team, patients who were not on the list were being included. This was corrected.
- The total number of patients on a summary individual patient report with multiple reminders was being calculated incorrectly. This was corrected.
- When a reminder due report was run by selected locations (hospital locations or clinic stops), the output of the selected list of locations was skipping the first entry in the list. Additionally, for stop codes, only the stop code was being printed. The output was changed so that the first entry is no longer skipped and the name of the clinic stop as well as the stop code is printed.
- When a Reminders Due Report was run using Clinic Groups and a Clinic Group did not have any patients, the output looked like this:

> The following Clinic Group(s) had no patients selected

> 1 A GROUP

> The number preceding the name is not necessary, so it was removed and the output now looks like this:

> The following Clinic Group(s) had no patients selected

> A GROUP

- In Reminders Due Reports, the check for duplicate facilities from file \#4 (Institution file) was being made based on the .01 name field, which is incorrect because there can be more than one entry with the exactly the same name. The duplicate check was changed to use the internal entry number.
- In Reminders Due Reports, when the number of applicable patients and the number of patients the report was run on was displayed, if there were no patients, the output was "0 patient." This was corrected to "0 patients."
- In the detailed report output, the line "patients have reminder due" was changed to "have the reminder due" since a detailed report has only one reminder.
- In a detailed report, when the Combined Facility prompt was answered "N" and the Combined Locations prompt was answered "Y", the next appointment would not display if the appointment location was not the same as the encounter location. This was corrected.
- The Reminders Due Detailed Report lists a count of patients on the output. If the number of patients exceeded 999, then the number ran into the patient's name

> 1834CRPATIENT,TEN (0666)           DUE NOW     N/A         None

> 1835CRPATIENT,FIFTEEN (6661)           DUE NOW     N/A         None

> 1836CRPATIENT,SIXTEEN (6666)         DUE NOW     N/A         None

> Room was made for the counter to go to 9999. When it gets to 10000, then it resets to 0 and starts over. The reset was used because of space issues.

> Date Due Last Done Next Appt

> -------- --------- ---------

> 9997 CRPATIENT,TEN (0666)          DUE NOW     N/A         None

> 9998 CRPATIENT,TWENTY (6661)          DUE NOW     N/A         None

> 9999 CRPATIENT,FORTY (6666)         DUE NOW     N/A         None

> 0 CRPATIENT,FIFTY (6663) DUE NOW N/A None

> 1 CRPATIENT,FIFTYFIVE (6661) DUE NOW N/A None

- "Disappearing" queued reminder reports continues to be a problem, so code was added to send a MailMan message if the report gets to the point where it is ready to start printing and the print task can't be started. This message will be sent to the Clinical Reminders mail group with information about what happened. This information should help in determining what is going wrong. If any sites get these messages, please send a copy to the Clinical Reminders developers.
- A check to look for patient lists and OE/RR Teams that do not contain patients when running a report from a template was added. Reminder reports will no longer allow the user to select patient lists and OE/RR Teams that do not contains patients.
- Reminder reports will now scan the reminders in a reminder category for reminders that do not exist on the system; a warning will be given if there are no reminders in the category. This check will happen when running a report from a template.
- In a delimited summary report "NONE" was sometimes appearing at the end of the line:

> 1;ABCDEF,GHIJK (000001234);DUE NOW;N/A;1/31/2006;NONE

> This signified that the patient is not an inpatient. This was changed, so now if the patient is an inpatient, the inpatient location is listed; otherwise it is blank.

- The intermediate data storage location for reminder due reports is made unique by using the date and time, to the second, when the report is started. When running a set of reminder due reports from report templates, a user was pasting answers to the input that is not stored in the report template so quickly that, in some cases, the time down to the second was identical for two of the reports in the set. This caused the two reports to use the same intermediate storage location, and the second report to destroy the intermediate data for the first report, causing errors that would prevent it from finishing. To prevent this problem, a one-second pause was added just before the time stamp is acquired, guaranteeing the uniqueness of the time stamps.
- A problem with incorrect patient counts for each location, when running a summary report against clinic locations, was corrected.
- As an aid in tracking down CNBD problems, a MailMan message with the subject "COULD NOT BE DETERMINED PATIENTS" will be generated and sent to the user who requested the report. The message will contain a list of patients who have a reminder evaluation status of CNBD. The file \#800 parameter MAXIMUM NUMBER OF INDEX ERRORS will be used to determine the maximum number of patients to display on the list.

## Reminder Sponsor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7

- There was a bug that would let a site create a Sponsor whose class was national and also produced a hard error when a Sponsor was deleted. These were both corrected.

## Reminder Taxonomies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Some incorrect CPT codes were removed from the taxonomy VA-WH BILATERAL MASTECTOMY; the corrected version is distributed as part of PXRM\*2.0\*4.
- When PATIENT DATA SOURCE was set to ALL, the search was not being done in all possible sources. This was corrected.
- An undefined error was occurring when trying to "^" jump during taxonomy editing. The undefined error was happening because jumping to an arbitrary field is not possible during taxonomy editing. The call to the FileMan routine used to do the editing was changed so that "^" is not allowed for jumping, but a single "^" will go back to the previous field.
- There was bug in taxonomy evaluation where it was trying to get Visit file information for Problem List entries. This was corrected.

## Reminder Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When editing a term, if the term has a sponsor, a check is made to ensure that the class of the term and the class of the sponsor are the same; if not, then the user is prompted again for the class and sponsor until the classes match. There was a bug where even if the class of the term and the class of the sponsor were the same, it was saying they did not match. This bug was corrected.
- Term edit was changed so that the user cannot "^" out when the Class of the term and Class of the sponsor do not match.
- A change was made so that if a term contains only drugs or orderable items, the field USE START DATE can be edited. Note that USE START DATE is available in both definitions and terms for all drug findings and orderable items.
- A new national term, VA-PCMM INSTITUTION, was created to be used as a finding rule. It serves the same function as VA-IHD STATION CODE, but its name makes it easier to understand its function. Whenever a finding rule using either of these terms is included in a rule set with the Insert operation, the patient's PCMM Institution will be included with the patient list. The PCMM Institution is determined by first finding the Institution (file \#4) entry for the patient's PCMM Team. If the Institution cannot be determined, the word NONE will be displayed.
- A site entered a Remedy ticket about a reminder not evaluating as expected. The finding in question was a term, so the debugger was used to see the details of how the term evaluated and it was found that everything was correct. Since the average Clinical Reminder Manager does not have programmer access, they cannot use the debugger to determine what is happening with a term. Therefore, an option was added to Reminder Test to show how all the findings for a term evaluated.
- The term finding modifier editing sequence was rearranged so it matches the sequence for definitions and term inquiry.
- In V.2.0, a change was made so that for terms used as findings in national reminders, the user could select a term and edit the findings on the term. This change introduced a bug that allowed the user to edit any of the findings in the reminder. The bug was corrected.
- The cross-reference on term findings for building the "enode" was never updated to the new form that was developed in V.2.0. (The enode is used for processing the term's findings.) This resulted in the enode not being built correctly for non-CH lab findings; other finding types were not affected. This was corrected. A section was added to the post-init to make sure all the definition and term lab enodes are set correctly.
- The computed finding parameter in reminder terms was not allowing the "^" character. This was fixed.
- There was a bug in term output when multiple occurrences of the same type of mapped finding were found. For example, if three occurrences were found, it would write three sets of output:

> Line 1

> Line 1

> Line 2

> Line 1

> Line 2

> Line 3

> This was corrected.

## ## Geriatric Extended Care (GEC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- An undefined error, \<UNDEFINED\>CALCMON+12\<\>PXRMG2M1, occurred when the scheduled event fired off at the beginning of each month. That has now been repaired.
- Several of the GEC Reports were not showing a complete list of patients or providers. This has now been corrected. The division and age of the patient has been added to some reports to help in identifying the patient.
- There is a new choice in the GEC reports menu that will give the sites the option to open a closed referral, merge two referrals, or close an open referral.
- The GEC Care Recommendation Dialog has been modified to allow more than one selection when a person wants to refer a patient to more than one location.
- A problem with the user being able to take some editing actions on GEC dialogs have been corrected, so the user is not able to copy or delete dialog groups from the GEC dialogs.
- Geriatric Extended Care Reports were not collecting the correct data. This was corrected.
- The email addresses of the remote members of mail group GEC NATIONAL ROLLUP are updated.
- As requested by the primary GEC stakeholder, several reminder dialog entries were moved from the Nursing Assessment GEC dialog to the Care Recommendation GEC dialog. A post-install routine changes several Health Factors from one GEC dialog to another.

## MyHealtheVet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MyHealtheVet requested a new combined output that returns both the summary and detailed output in a single call. A new routine, PXRMMHV, was created to support this.
- HealthGate was replaced with Healthwise in the web site URL information for the following reminders:

> VA-MHV CERVICAL CANCER SCREEN

> VA-MHV DIABETES FOOT EXAM

> VA-MHV DIABETES RETINAL EXAM

> VA-MHV HYPERTENSION

> VA-MHV INFLUENZA VACCINE

> VA-MHV MAMMOGRAM SCREENING

- The VA-MHV INFLUENZA reminder required two changes:
  - a frequency of 0Y for 49 and younger was added to the baseline and
  - a frequency of 1Y for all ages was added to the high-risk finding.

> Two Remedy tickets associated with this: \#118893 and \#113219.

## ## ## CPRS V26 Reminder Changes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reminder Error Trapping

With Clinical Reminders 2.0, CPRS will display an error message for any reminders that have an M error in the evaluation process.

> ![](pxrm-2-4-release-notes/002.png)

> ![](pxrm-2-4-release-notes/003.png)

Reminder Logic Error Trapping

With Clinical Reminders 2.0, CPRS will display an error for any reminders for which it can't determine the status.

> ![](pxrm-2-4-release-notes/004.png)

> ![](pxrm-2-4-release-notes/005.png)

Skin Test Changes

The PXRM Reading Prompt was changed to accept a Null Value.

NOIS UNY-0304-12585

> ![](pxrm-2-4-release-notes/006.png)

Vital Date/Time

Reminder Dialogs was changed to use the time a Vital was entered into a Dialog instead of the Appointment Time. NOIS HUN-0304-21713

> ![](pxrm-2-4-release-notes/007.png)

> ![](pxrm-2-4-release-notes/008.png)

Mental Health Test Dialogs

- Certain MH tests do not require a response to all questions, based on the patient's response to some of the questions. For example, in an AUDC test if the patient responds that she/he never drank, the other two questions do not need to be answered. If the patient answers "Never" to question one, the reminder dialog will evaluate the test as complete.

## Remedy Tickets resolved with Patch 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

68948, 84724, 85633, 85695, 87364, 89146, 89401, 89472, 89627, 90449, 90823, 90992, 91471, 91682, 92187, 92570, 92761, 92790, 92795, 92802, 92807, 92992, 93292, 93633, 94630, 95523, 98203, 100670, 101723, 105304, 106443, 106498, 109645, 111210, 111345, 113060, 113346, 118893, 122050, 122458, 123240, 123779, 124911, 125171, 127184, 131755, 132065, 132998, 133356, 133774, 134199, 136399, 136439, 138761, 142078, 149570, 153731

## E3Rs Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

15246 NEW FINDING TYPE - SCHEDULED APPOINTMENT

 15489 CHANGES TO REMINDER REPORT SELECTION CRITERIA (PXRM\*1.5\*6)

 15491 REPORTS:SELECT PAST DATE AS EFFECTIVE DATE

 15493 ADD MANAGEMENT OPTIONS FOR REMINDER REPORTS

 15533 ADD NEW FIELD TO REMINDER DEFN--REMINDER 'NOTES'

 15741 COLLAPSE/EXPAND RELATED DIALOG ELEMENTS AND GROUPS

 15758 SUPPRESS CHECKBOX & SEND TEXT TO NOTE (OR\*3\*173)

 15998 DUE REPORT BY PROVIDER

 16010 INCREASED DETAIL TO REPORTS

 16011 NEED FOR TIME AS A FINDING ATTRIBUTE

 16133 START STOP DATES

 16149 UTILIZE REMINDER DIALOGS AS COMPONENTS

 16675 UPDATE NATIONAL TAXONOMIES ANNUALLY

 16832 TEXT INPUT TO JUMP TO SELECTION ITEM

 16833 ADD CHOICE FOR 'ALL REQUIRED'--DIALOG GROUPS (OR\*3\*243)

 16929 COMBINED TEAM LIST REPORTS

 17158 ADDITIONAL REPORT

 17278 ENHANCE USE OF MRD

 17307 COLLATERALS SHOWING UP ON REPORTS

 17408 PRINT OPTION FOR DIALOG HIERARCHY (ListMan PL)

 17742 ALLERGY AS FINDING TYPE

 18024 FUTURE PENDING ORDERS

 18131 PATIENT LETTER-REMINIDER REPORTS

 18224 ADD PATIENT DEMOGRAPHIC OPTIONS TO REPORTS

 18248 PPD CHANGES FOR REMINDER DIALOGS

 18627 ASSIGN CLINICAL REMINDERS BY STOP CODE

 19360 RETAIN REMINDER INFO UPON PATIENT DEATH

 19485 CHANGE GEC REFERRAL DIALOG

 19488 OPEN CLOSED GEC REFERRAL

 19508 LIST FOREIGN ORDERABLE ITEMS IN REMINDER INSTALL

 19540 PATIENT LIST AND SS#

 19843 ADD ELIGIBILITY TO PATIENT DEMOGRAPHICS REPORT

# Appendix A: Appointment Computed Findings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following computed findings are being exported with Patch 4 (PXRM\*2.0\*4). They allow more detailed or specific appointment information to be used in cohort or resolution logic in reminder definitions. Use the COMPUTED FINDING PARAMETER in the findings editor to filter the results. See the descriptions and examples that follow for instructions on how to use these computed findings.

- VA-APPOINTMENTS FOR A PATIENT
- VA-PATIENTS WITH APPOINTMENTS
- VA-TREATING FACILITY LIST

NAME: VA-APPOINTMENTS FOR A PATIENT

ROUTINE: PXRMRDI

ENTRY POINT: PAPPL PRINT NAME: Appointments for a patient

TYPE: MULTIPLE

DESCRIPTION: This multiple occurrence computed finding returns a list of appointments for a patient in the specified date range. The COMPUTED FINDING PARAMETER can be used to filter the results. The values that can be used in the parameter are:

FLDS:F1,F2,... where F1,F2 are any of the possible integer ID values listed in the Available Appointment Data Fields table in the Computed Findings section of the Clinical Reminders Managers Manual. These specify what data associated with the appointment is to be returned; this data can be used in a CONDITION statement. Field number n will be the nth piece of the value. For example FLDS:1,16 would return the Appointment Date/Time in piece 1 and Date Appointment Made in piece 16. A condition such as I \$P(V,U,16)\>3060301 would be true if the date the appointment was made was after March 1, 2006. If FLDS is not specified then the value will be ID=1 (Appointment Date/Time) and ID=2 (Clinic IEN and Name).

STATUS sets a filter on the appointment status; only those appointments with status on the list will be returned. The possible values for STATUS are R (Scheduled/Kept), I (Inpatient), NS (No-show), NSR (No-show, Rescheduled), CP (Cancelled by Patient), CPR (Cancelled by Patient, Rescheduled), CC (Cancelled by Clinic), CCR (Cancelled by Clinic, Rescheduled), NT (No Action Taken).

If STATUS is not specified, the default is R,I.

LL:Reminder Location List specifies a list of locations so that only appointments for those locations will be returned. If LL is not specified, then appointments for all locations will be returned.

FLDS, STATUS, and LL are all optional and can be given in any order. Some examples:

FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

STATUS:CP,CC^FLDS:25

LL:DIABETIC LOCATION parameter is FLDS:F1,F2,...^STATUS:S1,S2,...^LL:LOCATION LIST.

CLASS: NATIONAL

NAME: VA-PATIENTS WITH APPOINTMENTS

ROUTINE: PXRMRDI

ENTRY POINT: APPL PRINT NAME: Patients with appointments

TYPE: LIST CLASS: NATIONAL

NAME: VA-TREATING FACILITY LIST

ROUTINE: PXRMRDI

ENTRY POINT: TFL PRINT NAME: Treating facility list

TYPE: MULTIPLE

DESCRIPTION: This multi-occurrence computed finding returns a list of treating facilities i.e., systems that store data related to a patient. The value for each entry is:

STATION NUMBER^NAME^DATE LAST TREATED^ADT/HL7 EVENT REASON^FACILITY TYPE

STATION NUMBER, NAME, and FACILITY TYPE are from the Institution file.

FACILITY TYPE is one of the entries found in the FACILITY TYPE file. ADT/HL7

EVENT REASON is a code from the ADT/HL7 EVENT REASON file. If there is no

ADT/HL7 EVENT REASON then DATE LAST TREATED will also be null.

Some examples of values that are returned:

"516^BAY PINES VAMC^^^VAMC"

"537^JESSE BROWN VAMC^3041122.110926^3^VAMC"

"552^DAYTON^3001113.092056^3^VAMC"

"556^NORTH CHICAGO VAMC^3050406.13^3^VAMC"

"578^HINES, IL VAMC^3020919.2324^3^VAMC"

"589^VA HEARTLAND - WEST, VISN 15^^^VAMC"

"636^VA NWIHS, OMAHA DIVISION^^^VAMC"

"673^TAMPA VAMC^3001215.1327^3^VAMC"

"695^MILWAUKEE VAMC^3030328.13^3^VAMC"

A CONDITION can be written that uses any of the pieces of the value. For example, a CONDITION to check that the FACILITY TYPE is VAMC would be: I \$P(V,U,5)="VAMC"

Since no date can be associated with an entry, the date of evaluation will be used.

CLASS: NATIONAL

## Available Appointment Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 28%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td><strong>FIELD NAME</strong></td>
<td><strong>DATA TYPE</strong></td>
<td><strong>Format/Valid Values</strong></td>
<td><strong>Description</strong></td>
<td><strong>Examples of Returned Data</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>APPOINTMENT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled Appointment Date/Time</td>
<td><p>3031215.113</p>
<p>3031201.0815</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>CLINIC IEN and NAME</td>
<td>TEXT</td>
<td>ID^name</td>
<td>Clinic IEN and name</td>
<td><p>150;CARDIOLOGY</p>
<p>32;BLOOD DONOR</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>APPOINTMENT STATUS</td>
<td>TEXT</td>
<td><p><strong>R (</strong>Scheduled/Kept)</p>
<p><strong>I</strong> (Inpatient)</p>
<p><strong>NS</strong> (No-Show)</p>
<p><strong>NSR</strong> (No-Show, Rescheduled)</p>
<p><strong>CP</strong> (Cancelled by Patient)</p>
<p><strong>CPR</strong> (Cancelled by Patient, Rescheduled)</p>
<p><strong>CC</strong> (Cancelled by Clinic)</p>
<p><strong>CCR</strong> (Cancelled by Clinic, Rescheduled)</p>
<p><strong>NT</strong> (No Action Taken)</p></td>
<td>The status of the appointment.</td>
<td><p>R;SCHEDULED/KEPT</p>
<p>I;INPATIENT</p>
<p>NS;N0-SHOW</p>
<p>NSR;NO-SHOW &amp; RESCHEDULED</p>
<p>CP;CANCELLED BY PATIENT</p>
<p>CPR;CANCELLED BY PATIENT &amp; RESCHEDULED</p>
<p>CC;CANCELLED BY CLINIC</p>
<p>CCR;CANCELLED BY CLINIC &amp; RESCHEDULED</p>
<p>NT;NO ACTION TAKEN</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>PATIENT DFN and NAME</td>
<td>TEXT</td>
<td>DFN;name</td>
<td>Patient DFN and Patient Name</td>
<td><p>34877;<mark>REDACTED</mark></p>
<p>455; <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>5</td>
<td>LENGTH OF APPOINTMENT</td>
<td>TEXT</td>
<td>NNN</td>
<td>The scheduled length of appointment, in minutes</td>
<td><p>20</p>
<p>60</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>COMMENTS</td>
<td>TEXT</td>
<td>free text</td>
<td>Any comments associated with the appointment</td>
<td>PATIENT NEEDS WHEELCHAIR</td>
</tr>
<tr class="even">
<td>7</td>
<td>OVERBOOK</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>"Y" if appointment is an overbook else "N"</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="odd">
<td>8</td>
<td>ELIGIBILITY OF VISIT IEN and NAME</td>
<td>TEXT</td>
<td>IEN;name</td>
<td>Eligibility code and name associated with the appointment</td>
<td><p>2;AID &amp; ATTENDANCE</p>
<p>7;ALLIED VETERAN</p>
<p>13;COLLATERAL OF VET.</p></td>
</tr>
<tr class="even">
<td>9</td>
<td>CHECK-IN DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>Date/time the patient checked in for the appointment</td>
<td>3031215.113</td>
</tr>
<tr class="odd">
<td>10</td>
<td>APPOINTMENT TYPE IEN and NAME</td>
<td>TEXT</td>
<td>IEN;name</td>
<td>Type of Appointment IEN and name</td>
<td><p>1;COMPENSATION &amp; PENSION</p>
<p>3;ORGAN DONORS</p>
<p>7;COLLATERAL OF VET.</p></td>
</tr>
<tr class="even">
<td>11</td>
<td>CHECK-OUT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>Date/time the patient checked out of the appointment</td>
<td>3031215.113</td>
</tr>
<tr class="odd">
<td>12</td>
<td>OUTPATIENT ENCOUNTER IEN</td>
<td>TEXT</td>
<td>NNN</td>
<td>The outpatient encounter IEN associated with this appointment</td>
<td>4578</td>
</tr>
<tr class="even">
<td>13</td>
<td>PRIMARY STOP CODE IEN and CODE</td>
<td>TEXT</td>
<td>IEN;code</td>
<td>Primary Stop code IEN and code associated with the clinic.</td>
<td>301;350</td>
</tr>
<tr class="odd">
<td>14</td>
<td>CREDIT STOP CODE IEN and CODE</td>
<td>TEXT</td>
<td>IEN;code</td>
<td>Credit Stop code IEN and code associated with the clinic.</td>
<td>549;500</td>
</tr>
<tr class="even">
<td>15</td>
<td>WORKLOAD NON-COUNT</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>"Y" if clinic is non-count else "N"</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="odd">
<td>16</td>
<td>DATE APPOINTMENT MADE</td>
<td>DATE</td>
<td>YYYMMDD</td>
<td>Date the appointment was entered into the Scheduling system</td>
<td>3031215</td>
</tr>
<tr class="even">
<td>17</td>
<td>DESIRED DATE OF APPOINTMENT</td>
<td>DATE</td>
<td>YYYMMDD</td>
<td>The date the clinician or patient desired for the scheduling of this appointment.</td>
<td>3031215</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 27%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td><strong>FIELD NAME</strong></td>
<td><strong>DATA TYPE</strong></td>
<td><strong>Format/Valid Values</strong></td>
<td><strong>Description</strong></td>
<td colspan="2"><strong>Examples of Returned Data</strong></td>
</tr>
<tr class="even">
<td>18</td>
<td>PURPOSE OF VISIT</td>
<td>TEXT</td>
<td>Code (1, 2, 3, or 4) and short description (C&amp;P, 10-10, SV, or UV)</td>
<td>The Purpose of Visit</td>
<td><p>1;C&amp;P</p>
<p>2;10-10</p>
<p>3;SV</p>
<p>4;UV</p></td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>EKG DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the EKG tests in conjunction with this appointment</td>
<td>3031215.083</td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>X-RAY DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the X-RAY in conjunction with this appointment</td>
<td>3031215.083</td>
<td></td>
</tr>
<tr class="odd">
<td>21</td>
<td>LAB DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the Lab tests in conjunction with this appointment</td>
<td>3031215.083</td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>STATUS</td>
<td>TEXT</td>
<td>Status Code, Status Description, Print Status, Checked In Date/Time, Checked Out Date/Time, and Admission Movement IFN</td>
<td>Status Information for the Visit.</td>
<td>8;INPATIENT APPOINTMENT;INPATIENT/CHECKED OUT;;3030218.1548;145844</td>
<td></td>
</tr>
<tr class="odd">
<td>23</td>
<td>X-RAY FILMS</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>"<strong>Y</strong>" if x-ray films are required at clinic else "<strong>N</strong>"</td>
<td><p>Y</p>
<p>N</p></td>
<td></td>
</tr>
</tbody>
</table>

## Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you want to limit the patient cohort for a reminder to APPOINTMENT DATE/TIME, CLINIC IEN and NAME, and DATE APPOINTMENT MADE, patients who kept their appointments, and were seen in a Diabetic clinic, you could specify this in the COMPUTED FINDING PARAMETER, as shown here.

Select Reminder Definition Management Option: Add/Edit Reminder Definition

Select Reminder Definition: diaB PTS (5Y) W/O DIAB EXAM (1Y) LOCAL

Select one of the following:

A All reminder details

G General

B Baseline Frequency

F Findings

FF Function Findings

L Logic

C Custom date due

D Reminder Dialog

W Web Addresses

Select section to edit: f Findings

Reminder Definition Findings

Choose from:

EX DIABETIC EXAM Finding \#: 2

TX VA-DIABETES Finding \#: 1

Select FINDING: VA-APPOINTMENTS FOR A PATIENT

Searching for a DRUG, (pointed-to by FINDING ITEM)

Searching for a EDUCATION TOPIC, (pointed-to by FINDING ITEM)

Searching for a EXAM, (pointed-to by FINDING ITEM)

Searching for a REMINDER LOCATION LIST, (pointed-to by FINDING ITEM)

Searching for a HEALTH FACTOR, (pointed-to by FINDING ITEM)

Searching for a IMMUNIZATION, (pointed-to by FINDING ITEM)

Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM)

Searching for a MENTAL HEALTH INSTRUMENT, (pointed-to by FINDING ITEM)

Searching for a ORDERABLE ITEM, (pointed-to by FINDING ITEM)

Searching for a RADIOLOGY PROCEDURE, (pointed-to by FINDING ITEM)

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

Searching for a REMINDER TAXONOMY, (pointed-to by FINDING ITEM)

Searching for a REMINDER TERM, (pointed-to by FINDING ITEM)

Searching for a SKIN TEST, (pointed-to by FINDING ITEM)

Searching for a VA DRUG CLASS, (pointed-to by FINDING ITEM)

Searching for a VA GENERIC, (pointed-to by FINDING ITEM)

Searching for a VITAL MEASUREMENT, (pointed-to by FINDING ITEM)

Searching for a DRUG

Searching for a EDUCATION TOPIC

Searching for a EXAM

Searching for a REMINDER LOCATION LIST

Searching for a HEALTH FACTOR

Searching for a IMMUNIZATION

Searching for a LABORATORY TEST

Searching for a MENTAL HEALTH INSTRUMENT

Searching for a ORDERABLE ITEM

Searching for a RADIOLOGY PROCEDURE

Searching for a REMINDER COMPUTED FINDING

VA-APPOINTMENTS FOR A PATIENT NATIONAL

...OK? Yes// (Yes)

Are you adding 'VA-APPOINTMENTS FOR A PATIENT' as

a new FINDINGS (the 3RD for this REMINDER DEFINITION)? No// Y (Yes)

Computed Finding Description:

This multiple occurrence computed finding returns a list of

appointments for a patient in the specified date range. The COMPUTED

FINDING PARAMETER can be used to filter the results. The values that

can be used in the parameter are:

FLDS:F1,F2,... where F1,F2 are any of the possible integer ID values

listed in the Available Appointment Data Fields table in the

Computed Finding section of the Clinical Reminders Managers Manual.

These specify what data associated with the appointment is to be

returned; this data can be used in a CONDITION statement. Field

number n will be the nth piece of the value. For example FLDS:1,16

would return the Appointment Date/Time in piece 1 and Date

Appointment Made in piece 16. A condition such as I

\$P(V,U,16)\>3060301 would be true if the date the appointment was

made was after March 1, 2006. If FLDS is not specified then the

value will be ID=1 (Appointment Date/Time) and ID=2 (Clinic IEN and

Name).

STATUS sets a filter on the appointment status; only those

appointments with status on the list will be returned. The possible

values for STATUS are R (Scheduled/Kept), I (Inpatient), NS

(No-show), NSR (No-show, Rescheduled), CP (Cancelled by Patient),

CPR (Cancelled by Patient, Rescheduled), CC (Cancelled by Clinic),

CCR (Cancelled by Clinic, Rescheduled), NT (No Action Taken).

If STATUS is not specified the default is R,I.

LL:Reminder Location List specifies a list of locations so that only

appointments for those locations will be returned. If LL is not

specified, then appointments for all locations will be returned.

FLDS, STATUS, and LL are all optional and can be given in any order.

Some examples:

FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

STATUS:CP,CC^FLDS:25

LL:DIABETIC LOCATION

Editing Finding Number: 3

FINDING ITEM: VA-APPOINTMENTS FOR A PATIENT//

REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

CONDITION: I \$P(V,U,16)\>3060301

CONDITION CASE SENSITIVE: N NO

USE COND IN FINDING SEARCH: Y YES

COMPUTED FINDING PARAMETER: FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

FOUND TEXT:

No existing text

Edit? NO//

NOT FOUND TEXT:

No existing text

Edit? NO//

Reminder Definition Findings

Choose from:

CF VA-APPOINTMENTS FOR A PATIENT Finding \#: 3

EX DIABETIC EXAM Finding \#: 2

TX VA-DIABETES Finding \#: 1

# Appendix B: HL7 Logical Link Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Turn on the Logical Link in the HL7 package

Before an HL7 message can be transmitted to Austin, each site must turn on the Logical Link in the HL7 package in their production account. Enter PXRM7 at the HL LOGICAL LINK prompt, and accept the default of "Background" as the method for running the receiver.

Select OPTION NAME: HL MAIN MENU HL7 Main Menu menu

Select HL7 Main Menu Option: Filer and Link Management Options

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the appropriate device. Select the node with which you want to communicate

Select HL LOGICAL LINK NODE: PXRM7-RECO

The LLP was last shutdown on DEC 03, 2003 15:07:47.

Select one of the following:

F FOREGROUND

B BACKGROUND

Q QUIT

Method for running the receiver: B// \<Enter\> ACKGROUND

Job was queued as 5282278.

Restart HL7 Logical Link

1.  HL Main Menu
2.  Filer and Link Management Options …
3.  SL Start/Stop Links
4.  Enter "PXRM7-RECO"
5.  Select "B" Background
6.  Monitor with System Link Monitor

Task Monthly Extracts

- The automatic monthly extract of QUERI information is initiated from the options PXRM EXTRACT VA-IHD QUERI and PXRM VA-MH QUERI. These are activated through TaskMan options.
- Use Schedule/Unschedule Options on the Taskman Management menu to schedule the PXRM VA-IHD QUERI and PXRM VA-MH QUERI options.

Task Automated Monthly Extracts

Select OPTION NAME: XUTM MGR Taskman Management menu

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: PXRM EXTRACT VA-IHD QUERI VA-IHD QUERI Extract run routine

Are you adding 'PXRM EXTRACT VA-IHD QUERI' as

a new OPTION SCHEDULING (the 50TH)? No// Y (Yes)

Edit Option Schedule

Option Name: PXRM EXTRACT VA-IHD QUERI

Menu Text: VA-IHD QUERI Extract TASK ID:

Catch up on Prior Extracts

1.  Run a manual extract or manual transmission for each month from Feb 2005 to the present to catch up
2.  Manual Catch-up of Missed Roll-Ups
3.  Use the Reminder Extract Management option to see what extract months have not run between February 2005 and November 2005 (the next automated run)
4.  Use the Manual Extract action to task each month not reported since 02/2005
5.  Use the Manual Transmission action to transmit extracts that have a "Not Transmitted" status

What automated extract period will run next?Catch-up Method A

This means that you run one extract after the other and that you need to wait for one to complete to run the next one – to keep updating the next extract period

1.  Run the prior extracts using the manual extract option
2.  Answer 'NO' to the prompt "Does this extract replace the scheduled extract?"
3.  Transmit the extracts manually
4.  Update the Next Monthly Period/Year in Fileman to be correct – e.g. update to M11/2005.

Catch-up Method B

- Using this method, you could run all your extracts at one time by queuing them
- Then update the next scheduled extract to the appropriate one; e.g., M11/2005

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PXRM*2*6 Release Notes

## Clinical Reminders PXRM\*2\*6 Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                         |                             |
|-------------------------|-----------------------------|
| Documentation       | Documentation File name |
| Release Notes           | PXRM_2_6_RN.PDF             |
| Install and Setup Guide | PXRM_2_6_IG.PDF             |
| User Manual             | PXRM_2_6_UM.PDF             |
| Manager Manual          | PXRM_2_6_MM.PDF             |

Patch PXRM\*2\*6 contains modifications to integrate the Clinical Reminders package with the new version of the Mental Package called MHA3. The Clinical Reminders package will support use of new mental health surveys, instruments, and forms for clinical collection, reminder evaluation, patient list building and reporting. These modifications will be distributed at the same time as YS\*5.01\*85.

This functionality is needed so that Clinical Reminders can be used to help sites meet the Performance Measure requirements related to a standardized set of Mental Health Instruments that will be available in the YS\*5.01\*85 patch. The standardized instruments are AUDC, BDI2, PHQ-2, PHQ9, and PC-PTSD.

## Modified National Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-Depression Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PHQ-2 & PHQ-9 in the dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-Iraq & Afghan Post Deploy Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use all MH tests (AUDC, PHQ-2, PC PTSD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Added more detailed branching logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-TBI Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Fixed selection problem; added done elsewhere 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-MHV Influenza Vaccine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Updated date for FY08

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New National Reminders

## VA-PTSD SCREENING 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Uses PC PTSD 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-ALCOHOL ABUSE SCREEN (AUDIT-C) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Uses AUDIT-C for all alcohol screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Provides a standard tool for education and counseling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Multiple branching logic reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NOTE: In order to use all of the dialog functionality available with MHA3 and PXRM\*2\*6, Version 27 of the CPRS GUI will need to be installed. This version isn't scheduled for release until later in the year.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Version 27 adds the ability to use a Mental Health DLL when a MH test is invoked from a reminder dialog. (YS_MHA.DLL is included with YS\*5.01\*85 and must be installed in the folder \Program Files\vista\\ Common Files on all workstations.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Additional dialog features available via CPRS 27 and MH DLL:
  - Result group messages
  - Require all items in a group
  - Improved MH test required functionality
- Improves progress note text over CPRS V26 for MH tests

See the section on Dialogs, later in the Release Notes, for more information about use of the Reminder Dialogs and Mental Health tests with CPRS 26 or CPRS 27 and the MH DLL.

## General Functionality Changes in PXRM\*2\*6 and GMTS\*2.7\*77

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes have been made in Clinical Reminders and Health Summary.

## Health Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

GMTS\*2.7\*77, bundled with PXRM\*2.0\*6, provides two new Health Summary Components to view administered mental health tests and scores:

- MHAL - MHA Administration List
- MHAS - MHA Score

Example: Health Summary with MHAL and MHAS components

10/29/2007 10:03

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CONFIDENTIAL AD HOC SUMMARY \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRPATIENT,FIVE 000-00-0005 DOB: 04/18/1985

1A(1&2)

---------------------------- MHAL - MHA Admin List ----------------------------

Date Instrument Ordered by Location

05/14/07 15:08 AUDC CRPROVIDER,THREE 1A(1&2)

05/14/07 15:08 PHQ9 CRPROVIDER,THREE 1A(1&2)

05/14/07 15:08 PHQ-2 CRPROVIDER,THREE 1A(1&2)

-------------------- MHAS - MHA Score (max 10 occurrences) --------------------

Date Instrument Raw Trans Scale

05/14/2007 15:08 PHQ-2 5 Total

05/14/2007 15:08 PHQ9 10 Total

05/14/2007 15:08 AUDC 2 Total

- END \*

## ## ## ## Reminder Definitions/Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To aid sites in making the conversion of Clinical Reminders to use MHA3, the post-init will convert all existing mental health findings to their MHA3 equivalent and MH SCALE values to the appropriate MHA3 scale. If the field MH SCALE is null, then the score for the first scale returned by MHA3 will be displayed in the Clinical Maintenance output.

> When MH SCALE has a value, it will set the value of V for use in a Condition. In other words, V will be the score according to the scale stored in MH SCALE. Another change is that score is now returned as raw score^transformed score. Thus, if your Condition uses the raw score, you will use +V or \$P(V,U,1) and if it uses the transformed score, use \$P(V,U,2). The post-init will convert V to +V in all existing national Conditions for MH findings.

> The entire set of scores has been made into a CSUB item in patch PXRM\*2\*6, so that any score or combination of scores can be used in a Condition. For example, the MH Test AUIR has scales 279 through 329; if you want to use the raw score for scale 300, then you can use +V("S",300).

> NOTE: Typing a "?" at the MH SCALE prompt will give you a list of all the scales available for the MH Test you have selected. It shows you both the scale number and the scale name. Because the scale number is much easier to use, it is the way we refer to scales in reminder definitions and terms.

> Responses to individual questions can also be used in a Condition. For example, if you want to test the response to question number 7, you would use V("R",7).

> NOTE: No national reminder definitions use MH findings, but those national terms that use MH findings will have correct values set for MH SCALE, and where applicable, the Condition will be updated also. These terms will be redistributed in patch PXRM\*2\*6.

- A new function finding function, NUMERIC, was added.

DESCRIPTION: The NUMERIC function returns the first numeric portion of any of the "CSUB" values for a finding. For example, if the COMMENT field of a health factor contains a numerical value, this function can be used to test it. If you want to check to see if the first numeric portion in the COMMENT field of finding 1 occurrence 1 is greater than 2, then the function finding would be:

 

 NUMERIC(1,1,"COMMENTS")\>2

 

> **NOTE:** OCCURRENCE COUNT for the finding must be equal to or greater than the occurrence(s) you want to use. 

- The primary provider DUZ was added to the data returned for a Visit file entry. If there is no primary provider, the value will be null. TYPE, HOSPITAL LOCATION, STOP CODE, and ENTERED BY were also added to the data returned for a Vitals entry.
- Clinical Reminders normally treats partial dates as follows: if the day is missing, it is assumed to be the first; if the month is missing, it is assumed to be January. When a Custom Date Due was used, this convention was not being followed. The code was changed to follow this convention.
- A typo in error message text for Vitals findings was corrected. The name of the global was GMRV(120.5; it was corrected to GMR(120.5.
- Processing of Location List findings was originally based on the AET Visit file index which includes Encounter Type. Encounter Type is not a required field; consequently any Visit file entries that do not have an Encounter Type will not be in this index and would be missed. The code was changed to use the AA index so no entries will be missed. As an added bonus, it turned out that using AA is faster than AET.
- When BEGINNING DATE/TIME and ENDING DATE/TIME were input as FileMan dates including time, the time was not being displayed in reminder inquiry. This was corrected.
- The MHV output for non-VA meds was producing an error when there was no stop date. This was corrected.
- There was a bug when editing terms in national reminder definitions. A list of terms to edit is presented and the user selects which term to edit. If the user selected terms 3, 5, and 7, they would actually get terms 1, 2, and 3 to edit. This was corrected.
- If a term contained multiple drug findings, the name of the most recent drug was being displayed for all the findings, even though the rest of the information such as start date and days supply was correct. The code was changed so that the correct drug name is displayed for each finding.
- For drug class or VA Generic findings that contain many drugs, it is possible that different drugs on the list may have the same pharmacy orderable item. When this was the case and non-VA meds were included in the search, multiple instances of the same non-VA med were being put on the list. To prevent this, a check was added to make sure the same instance was not already on the list before adding it.
- An undefined error associated with the status list when adding a reminder taxonomy as a finding item to either a reminder definition or a reminder term was fixed. To test this, the user would need to create a taxonomy that contains both Radiology CPT Codes and ICD9 Codes and the Patient Data Source is set to "All". Remedy \#168830 and \#177389.
- Building the drug status list was changed to use a new pharmacy encapsulation API instead of FileMan calls.
- Plus and minus were inadvertently left out of the list of permissible operators in Function Findings; they were added to the list.
- The selection display in reminder definition edit was changed to show if a definition has been inactivated.
- A site had a problem with a reminder because their default resolution logic (built from USE IN RESOLUTION LOGIC fields on the findings) allowed the reminder to be resolved solely by a function finding. Checking during reminder definition edit was added that will notify the user when this situation occurs.
- The definition and term inquiries displayed the old name of the field USE STATUS/COND IN SEARCH. These were corrected to use the new name.

## Reminder Dialog Changes (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Data Dictionary Changes

> The variable pointer for the Finding Item field was changed to point to the new MH file 601.71 instead of File \#601.

> PXRM\*2\*6 adds three new fields to the DD for 801.41. These fields will be used by Result Group/Elements and Dialog Elements.

> ^PXRMD(801.41,D0,50)= (#119) MH TEST \[1P:601.71\] ^ (#120) MH SCALE \[2N\] ^

> ^PXRMD(801.41,D0,51,0)=^801.41121P^^ (#121) RESULT GROUP SEQUENCE

> ^PXRMD(801.41,D0,51,D1,0)= (#.01) RESULT GROUP SEQUENCE \[1P:801.41\] ^

- MH Test is defined when creating/editing a Result Group. As of PXRM\*2\*6, all Result Groups must be mapped to a MH Test.

> MH Scale is defined when creating/editing a Result Group. The list of possible scales is based on the MH Test defined in field \#119. As of PXRM\*2\*6, all Result Groups need to be mapped to a MH Scale.

> Result Group Sequence is replacing the Result Group/Element field used when creating/editing a Dialog Element for a MH Test. With the new MH DLL in CPRS 27, it is now possible to evaluate multiple scores for each MH Test that contains multiple scales. In the past, we could only evaluate one score per test. With PXRM\*2\*6, only a Result Group can be assigned to a Dialog Element.

> Field (#55) RESULT GROUP/ELEMENT \[15P:801.41\] will be deleted from the 801.41 DD.

> Maximum Number of MH Questions has been added as a new field to file 800.

> ^PXRM(800,D0,MH)= (#17) MAXIMUM NUMBER OF MH QUESTIONS \[1N\] ^

- Pre and Post-Install

> All the National Result Groups and Result Elements will be re-released with PXRM\*2\*6. These have been updated to use the correct MH Test and the MH Scale.

> Seven new result groups will be released with PXRM\*2\*6.

> PXRM BRADEN RESULT GROUP

> PXRM MORSE FALL RESULT GROUP

> PXRM PCLC RESULT GROUP

> PXRM PCLM RESULT GROUP

> PXRM PHQ2 RESULT GROUP

> PXRM PHQ9 RESULT GROUP

> PXRM PTSD RESULT GROUP

> The PXRM AIMS RESULT ELEMENT 1 Progress note text has been modified to only display the total score of the AIMS test.

> The PXRM BDI RESULT GROUP has been marked disabled. Sites should use the PXRM BDI II RESULT GROUP instead of this result group.

> NOTE: The MH instrument BDI is being discontinued. The Beck Depression Inventory is an instrument in the Mental Health Assistant that has long been used for evaluating and monitoring depression.  For several years, MHA carried both the original version (BDI) and a newer, enhanced version (BDI2).  With the release of patch YS\*5.01\*85, the BDI will be inactivated, as the BDI2 is now the preferred version of this instrument. During the pre-init, any dialog elements using BDI will be changed to use BDI2.

> National Result Groups assigned to a dialog element will be moved to the new multiple "RESULT GROUP SEQUENCE" if the test assigned to the Result Group matches the MH Finding Item in the element. These items will be stored as the first position. Local Result Groups will not be moved because of the lack of MH Tests defined for the Result Groups. Any Result Group that is not moved should be displayed in a MailMan message stating the name of the Result Group and the Element.

- Result Element Editor

> A new field was added to the Result Group Editor "Informational Text"; this field allows the sites to add text to a pop-up warning in CPRS. (CPRS 27 and the MH DLL are needed to support this functionality). When CPRS is evaluating the Result Element progress note text, if the Result Element is true, the Informational Text defined in the Result Element will be returned to CPRS 27.

- Result Group Editor

> In the Result Group Editor, sites will be able to disable a Result Group. Sites will also be able to assign the MH Test and the MH Scale to the Result Group. Both an MH Test and a MH Scale are required before the Result Group can be used in CPRS. A disabled Result Group will not be used in CPRS.

> Several enhancements were made to result group editing. Result groups are screened to make sure they match the MH test. If the MH test is changed, any existing result groups are checked and if they do not match the MH finding, they are deleted.

- Dialog Element Editor

> When defining an MH finding item in a dialog element, the user will be able to assign multiple result groups to a dialog element. This is done to support the enhanced functionality of the MH DLL in CPRS 27. The list of Result Groups should be limited to Result Groups that have the same MH test as the MH finding Item, an MH Scale defined, and the Result Group is not disabled. When an MH test is defined in a dialog element, a check will be done to see if the test requires a license. If the test requires a license, a message will be displayed to the user stating "The question text will not appear in the progress note."

New Dialog Option

- A new option, Edit Number of MH Questions, has been added to the Reminder Parameters menu. This option allows the site to set the maximum number of questions an MH test can have and be administered via a Reminder Dialog. The default value when PXRM\*2\*6 is installed is 35. The user will not be able to select a MH test with a number of questions that exceeds the value defined in this option.

## ## Reminder Dialog Changes (CPRS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS_MHA.DLL is a new tool included with YS\*5.01\*85 that provides an interface to Clinical Reminders functions in CPRS27. As described in the YS\*5.01\*85 Installation Guide, this DLL must be deployed to \Program Files\vista\\ Common Files.

This DLL will replace the current MH functionality in reminder dialogs. The DLL will allow Reminder Dialogs to process *all* MH tests with no more than 100 questions. The maximum number of questions can be set by sites using the option "Edit Number of MH Questions" described in the preceding section. The question and answer text for the progress note, along with the score and scale for each MH test, will be returned by the MH DLL.

CPRS 26 has additional checks to avoid forcing the user to answer all the questions in the MH test if the test is considered resolved without answering all of the questions. This requires installation of PXRM\*2\*6 and YS\*5.01\*85 to work.

- Result Group Evaluation

How this works will depend on what combination of software you have installed:

- *CPRS 26 and PXRM\*2\*6*. PXRM\*2\*6 can contain multiple Result Groups; however, CPRS 26 is only expecting one Result Group per element. If the dialog element contains more than one dialog result group in the Result Group Sequence Multiple, only the first Result Group in the multiple will be sent to CPRS 26. The informational message can be defined in the Result Element; however, the Informational message will not display in CPRS 26. The Reminder Manager will be able to set up a dialog with MH Tests that do not work in CPRS 26. An error message "Error encountered loading MH Test Name" will be displayed in CPRS. The MH Test BOMC is an example of a test that can be defined in PXRM\*2\*6, but will not function correctly until CPRS 27 and the MH DLL.
- *CPRS 27 and PXRM\*2\*6 are installed, but the MH DLL is not running.* CPRS 27 will be able to handle a list of Result Groups. However, the original Result Group evaluation code will not be able to support dialog elements for Result Groups. The Result Group evaluation code will take the first Result Group in the list and will process this Result Group as the only Result Group for the dialog element. The informational message can be defined in the Result Element; however, the Informational message will not display in CPRS 26. The Reminder Manager will be able to set up a dialog containing MH Tests that do not work in CPRS 26. An error message "Error encountered loading MH Test Name" will be displayed in CPRS. The MH Test BOMC is an example of a test that can be defined in PXRM\*2\*6, but will not function correctly until CPRS 27 and the MH DLL.
- *CPRS 27, PXRM\*2\*6, and the MH DLL are running*. Once CPRS 27 is released and the MH DLL is running, everything is in place to support the new functionality. Each Result Group per dialog element will be evaluated against the score(s) for each scale returned from the DLL. The Informational Message will appear in CPRS 27, and MH Tests such as the BOMC will work with CPRS 27 and the MH DLL.

A new parameter to toggle the MH DLL on or off will be released with CPRS 27.

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP Edit Parameter Values

Select OPTION NAME: XPAR EDIT PARAMETER       Edit Parameter Values  
Edit Parameter Values  
                         --- Edit Parameter Values ---

 

Select PARAMETER DEFINITION NAME:    OR USE MH DLL   Use MH DLL?

 

-------- Setting OR USE MH DLL  for System: CPRS27.FO-SLC.MED.VA.GOV --------  
Use MH DLL?: YES//

 

When CPRS 27 is released nationally, this parameter will be set to Y.

## Reminder Extracts and Patient Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The format of the "Scheduled to Run:" date in Extract Summary was changed from a FileMan date to an external date.
- The List Manager Extract Summary display was changed to use the reminder print name if it exists. If it does not exist, then the .01 is used. This makes the name display in Extracts consistent with Clinical Maintenance and Reminder Reports.
- Previously, when a patient list was created, the first step was to initialize a stub in the Patient List file; the stub contained only the NAME and the CLASS. If there was an error populating the list and the stub was left, then only someone holding the PXRM MANAGER key could delete it. The stub initialization was changed so that it also inserts the CREATOR and sets the initial TYPE to be public. This makes it possible for the person who created the list to delete it if an error occurs that prevents normal completion of the list-building process.
- If a patient is on a patient list and for some reason the patient is later deleted from the Patient File, then running a Patient Demographic Report or a Health Summary would generate an error. Code was added to handle this problem.
- Dates shown in patient list creation documentation did not always match those displayed by the rule set test action. To correct this, a new routine was created, to be used for all patient list date calculation. Some of the basic date utility functions used throughout Clinical Reminders were optimized to get better performance.
- The setting of date ranges when building a patient list from a reminder definition was made consistent with the way it is done for terms.
- Code was added to catch problems with patient list build dates. The problems will be displayed in the list creation documentation.
- The list template PXRM PATIENT LIST PATIENTS had a bottom margin of 19 and consequently it could not display two of the actions. The bottom margin was changed to 18 so these actions would display.
- The display of Extract Definitions didn't show the fields INCLUDE DECEASED PATIENTS and INCLUDE TEST PATIENTS. If the value is NULL, then the display will show "NO."
- Changes were made so that if deceased and/or test patients are included on a patient list, they will be marked with a "D" or "T."
- When patient demographic report output was queued to p-message or a printer, the output never appeared. This was traced to incorrectly calling a Kernel queuing routine, which was corrected. Work on this also uncovered a problem in some VADPT routines that were not properly protecting variables, in particular % which is also used in the Kernel queuing routines. This may explain why some reminder report outputs have disappeared in the past. A Remedy ticket, \#183747, was filed for VADPT.
- All sequences in patient lists and extracts were converted from three-character free-text to a number between 1 and 999. Existing entries will be converted by the post-init.
- The display of patient list creation documentation was improved. The header was expanded to two lines so the entire name of the patient list can be seen. The list template right margin was changed to 132 so the entire display can be seen. The number of patients was moved to a separate line.
- The extract summary display was changed to make it easier to read.
- The list template PXRM PATIENT LIST is obsolete, so it was added to the build as "delete at site."
- The list template PXRM PATIENT LIST USER had incorrect caption information; it was corrected.
- Two problems that arose when running an extract against a reminder definition were repaired: 1) an undefined error when the reminder definition did not have a print name and 2) the reminder output was not stored in the correct sequence order.
- Extracts were changed to increment the patient list name created from an extract, if the extract is re-run for a previous period. The number at the end of the patient list will match the number at the end of the extract.
- Display of the operation was added to output for Rule Set Test.
- It was found that the SEQUENCE fields in Reminder Extract Definitions, Reminder Extract Counting Rules, Reminder Counting Groups, and Reminder List Rule Sets did not enforce uniqueness. In other words, there was nothing to prevent creation of a Rule Set with two number 1 sequences. A key that enforces uniqueness was added to each of these fields.
- The following list rule changes were made:

> VA-\*IHD QUERI 412 DIAGNOSIS

> Changed LIST RULE ENDING DATE from null to T

> VA-\*IHD QUERI LIPID LOWERING MEDS

> Changed LIST RULE ENDING DATE from null to T

> VA-\*IHD QUERI PTS WITH QUALIFY VISIT

> Changed LIST RULE ENDING DATE from T to BDT

## ## Miscellaneous

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The option, TIU Template Reminder Dialog Parameter, was added to the CPRS Configuration menu on the Reminder Managers Menu. It lets users edit the TIU TEMPLATE REMINDER DIALOG parameter while in Reminders options rather than going through the Parameters Menu.

## GEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- As requested by the primary GEC stakeholder, several reminder dialog entries were moved from the Nursing Assessment GEC dialog to the Care Recommendation GEC dialog. A post-install routine changes several Health Factors from one GEC dialog to another.

## Summary of Mental Health Instruments in Reminder Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Instruments with free-text responses can be administered in reminder dialogs once CPRS v27 is released (won't work in CPRS v26)
- With CPRS v27, pop-up messages can be added to provide directions based on result of MH instrument; for example, if PHQ-2 is positive, you need to complete a PHQ-9 now
- Clinical reminders includes a parameter that determines the length of a test that can be administered through reminder dialogs—defaults to 35 items
- Tests in reminder dialogs will follow restrictions set with MH security keys
- Tests that are restricted or require a license won't display questions/responses in progress note text
- Completing long tests through reminder dialogs is not recommended
- Patient-administered testing should be completed using the Secure Desktop functionality in MHA.

How does MHA help Integrated Care?

- Need Outcomes, using standardized tools, such as PHQ9
- Can begin using MHA to access and record assessment data for veterans in integrated care programs
- Can use MHA and clinical reminders to identify those patients in a "watchful waiting" phase, needing regular assessment
- How many veterans in integrated care clinics over the age of 65 endorsed suicidal ideation on PHQ9?
- Which veterans presenting with cardiac complaints have positive scores on Beck Anxiety Scale?
- What is the severity of depression seen in veterans enrolled in the pain clinic?

For Secure Patient Testing

- Patients can complete testing on computer, using Secure Desktop functionality

![](pxrm-2-6-release-notes/002.png)

- Logs computer off network when testing is completed. No other application can be accessed
- Secure Desktop must be installed on the PC (not run from server)
- Secure Desktop should only be installed on PC's that veterans will use to complete assessments in MHA

### From: PXRM*2*12 Release Notes

## Contents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [Clinical Reminders Enhancements in PXRM\*2\*12 2](#clinical-reminders-enhancements-in-pxrm212)
2.  [Bug fixes in PXRM\*2\*12 8](#bug-fixes-in-pxrm212-remedy-tickets-addressed)
[Remedy tickets addressed: 8](#bug-fixes-in-pxrm212-remedy-tickets-addressed)
3.  [GMTS\*2.7\*89 Description 11](#gmts2.789-description)
4.  [OR\*3\*295 Description 11](#or3295-description)
5.  [TIU\*1\*249 Description 12](#tiu1249-description)
[APPENDIX A: EXAMPLE OF DRUG CLASS UPDATE MESSAGES 13](#appendix-a-example-of-drug-class-update-messages)
[APPENDIX B: EXAMPLE OF DIALOG EXCHANGE ERRORS 14](#appendix-b-example-of-dialog-exchange-errors)
> ii Clinical Reminder Setup Guide 11/10/2009

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clinical Reminders patch PXRM\*2\*12 and bundled patches (GMTS\*2.7\*89, OR\*3\*295, TIU\*1\*249) contain modifications to improve reminder exchange tools, reminder due reports, and National Drug Class standardization. They also include changes to support pharmacy encapsulation so the reminder package will no longer have direct access to Pharmacy data. Initial changes to support standardization of reminder findings are incorporated.

> The PXRM\*2.0\*12 build is bundled with the following builds:

> ![](pxrm-2-12-release-notes/002.png)OR\*3.0\*295 – Contains OR bug fixes and changes to an API used by reminders. GMTS\*2.7\*89 – Supports new Reminder Exchange functionality, new Reminders components, and an enhancement to the TIU/HS Functionality

> ![](pxrm-2-12-release-notes/003.png) TIU\*1.0\*249 – Supports new Reminder Exchange functionality, changes to reminder dialogs, and improves the TIU ListManager Health Summary Object display.

### Clinical Reminders PXRM\*2\*12 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Documentation  | Documentation File name |
|--------------------|-----------------------------|
| Installation Guide | PXRM_2_12_IG.PDF            |
| Manager Manual     | PXRM_2_12_MM.PDF            |
| Release Notes      | PXRM_2_12_RN.PDF            |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td><p>Contains manuals, PowerPoint</p>
<p>presentations, and other information about Clinical Reminders</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrcpub</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>lic/default.aspx</u></a></td>
<td>This new committee will direct the development of new and revised national reminders</td>
</tr>
<tr class="odd">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for Clinical Reminders</p>
<p>and</p></td>
</tr>
</tbody>
</table>

### Clinical Reminders Enhancements in PXRM\*2\*12

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Drug Class Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Similarly to what was done for code set versioning, a new mechanism was created that will be triggered whenever a national drug class update takes place. All reminder definitions, dialogs, and terms will be searched to determine if any of them can potentially be affected by the drug class changes in the update. A MailMan message that describes what was found will be delivered to the Reminders mail group.

### New options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/004.png)Reminder Computed Finding Inquiry Check Reminder Dialog for invalid items Expand all Taxonomies

> Verify all taxonomy Expansions Finding Usage Report

### Reminder Component Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The formatting for the various reminder component inquiries was made as consistent as possible and a computed finding inquiry was added.

### Reminder Component Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following national Clinical Reminders components are new or updated and redistributed:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 42%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Name</strong></th>
<th><strong>Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RD</td>
<td>VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL</td>
<td><p>Added SUD; added text dialog element for local health summary object for prior AUDIT-C display; reversed order of feedback and advice; made nothing</p>
<p>required</p></td>
</tr>
<tr class="even">
<td>RD</td>
<td><p>VA-EMBEDDED FRAGMENTS RISK</p>
<p>EVALUATION</p></td>
<td>New*</td>
</tr>
<tr class="odd">
<td>RD</td>
<td><p>VA-IRAQ &amp; AFGHAN POST-DEPLOY</p>
<p>SCREEN</p></td>
<td>Added a FF to the cohort logic</td>
</tr>
<tr class="even">
<td>RD</td>
<td>VA-TBI SCREENING</td>
<td><p>Changed dialog to have documentation of</p>
<p>discussion of positive screen</p></td>
</tr>
<tr class="odd">
<td>RL</td>
<td>VA-OEF/OIF EXCLUSION STOPS</td>
<td>Added ultrasound stop code</td>
</tr>
<tr class="even">
<td>RM</td>
<td>VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL</td>
<td>Added SUD clinic visit exclusions</td>
</tr>
<tr class="odd">
<td>RM</td>
<td>VA-DEPRESSION SCREEN</td>
<td>Updated URLs and description.</td>
</tr>
<tr class="even">
<td>RM</td>
<td><p>VA-EMBEDDED FRAGMENTS RISK</p>
<p>EVALUATION</p></td>
<td>New *</td>
</tr>
<tr class="odd">
<td>RM</td>
<td><p>VA-IRAQ/AFGHAN POST</p>
<p>DEPLOYMENT SCREEN</p></td>
<td><p>Uses OEF/OIF in dialog and logic; updated</p>
<p>logic, fixed active duty problem</p></td>
</tr>
<tr class="even">
<td>RM</td>
<td>VA-MHV BMI</td>
<td>Removed &gt;, added text changes from NCP</td>
</tr>
<tr class="odd">
<td>RM</td>
<td><p>VA-MHV COLORECTAL CANCER</p>
<p>SCREEN</p></td>
<td>Added upper age limit</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 42%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>RM</th>
<th>VA-OEF/OIF MONITOR REPORTING</th>
<th><p>Removed dialog from this reporting</p>
<p>reminder.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RM</td>
<td>VA-TBI SCREENING</td>
<td><p>Changes to OEF/OIF in dialog and logic,</p>
<p>fixed active duty issue</p></td>
</tr>
<tr class="even">
<td>RT</td>
<td>VA-ACTIVE DUTY</td>
<td>Updated active duty term description</td>
</tr>
<tr class="odd">
<td>RT</td>
<td>VA-ALCOHOL NONE PAST 1YR</td>
<td><p>Removed MH test from term VA-</p>
<p>ALCOHOL NONE PAST 1YR</p></td>
</tr>
<tr class="even">
<td>RT</td>
<td>VA-IRAQ/AFGHAN SERVICE</td>
<td><p>Updated to include CFs for OEF/OIF</p>
<p>service that point to the patient file</p></td>
</tr>
<tr class="odd">
<td>RT</td>
<td>VA-MHV HIGH RISK FOR FLU</td>
<td>Updated to use new taxonomy</td>
</tr>
<tr class="even">
<td>RT</td>
<td><p>VA-MHV HIGH RISK FOR</p>
<p>PNEUMONIA</p></td>
<td>Updated to use new taxonomy</td>
</tr>
<tr class="odd">
<td>RX</td>
<td>VA-OEF/OIF MONITOR</td>
<td>New extract</td>
</tr>
<tr class="even">
<td>TX</td>
<td>VA-BREAST TUMOR</td>
<td><p>Changed description to include mass, pain,</p>
<p>abnormality</p></td>
</tr>
<tr class="odd">
<td>TX</td>
<td>VA-DEPRESSION</td>
<td>Updated to FY09 definition</td>
</tr>
<tr class="even">
<td>TX</td>
<td>VA-DEPRESSION OUTPT</td>
<td>Updated to FY09 definition</td>
</tr>
<tr class="odd">
<td>TX</td>
<td>VA-DIABETES</td>
<td>Added 250.91-250.93</td>
</tr>
<tr class="even">
<td>TX</td>
<td>VA-HIGH RISK FOR FLU</td>
<td>New</td>
</tr>
<tr class="odd">
<td>TX</td>
<td><p>VA-HIGH RISK FOR</p>
<p>FLU/PNEUMONIA</p></td>
<td>Inactivated</td>
</tr>
<tr class="even">
<td>TX</td>
<td>VA-HIGH RISK FOR PNEUMONIA</td>
<td>New</td>
</tr>
</tbody>
</table>

> \* Please provide the Embedded Fragment Surveillance Center (TEFSC) with contact information for the veteran's primary healthcare provider, or enter contact information for the VA medical center staff member deemed appropriate by your VA facility. The point of contact is the person that TEFSC will contact to help arrange for follow-up activities such as biomonitoring.

### General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/005.png) The right margin for Clinical Maintenance output was increased from 70 to 72. This prevents unnecessary wrapping that was sometimes occurring.

### Reminder Computed Findings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/006.png) New option: CFI - Reminder Computed Finding Inquiry

> o This new option allows a user to display the information about a computed finding in an easy-to- read format.

> ![](pxrm-2-12-release-notes/007.png) A new version of VA-BMI is included. The new version is a multi-occurrence computing finding, in contrast with the old version which was a single occurrence computed finding. It provides for more efficient date range searching and the ability to get more than one occurrence. The new multiple occurrence version of the computed finding VA-BMI was applying the date range criteria to both height and weight, in contrast to the single occurrence version which only applied it to weight. A change was made to only apply the date range criteria to the weight. The description was updated to include this information. Display of the date of the height date used in the calculation was added to the output.

> ![](pxrm-2-12-release-notes/008.png) Note that the changes to VA-BMI (only applying the date range criteria to the weight) also apply to the VA-BSA computed finding, because it uses the same routine to obtain matched weight and height measurements.

> ![](pxrm-2-12-release-notes/009.png) Note: Sites using the Bar Code Expansion handheld devices from Care Fusion will need to install Vitals patch GMRV\*5\*25 and the fix from Care Fusion to remove bad dates from the GMRV VITAL MEASUREMENT file before using these computed findings. Because these bad dates can cause problems with the VA-BMI and VA-BSA computed findings, GMRV\*5.0\*25 is a required build.

> ![](pxrm-2-12-release-notes/010.png) The description for the VA-COMBAT VET ELIGIBILITY computed finding was incorrect and has been corrected.

> ![](pxrm-2-12-release-notes/011.png) The VA-PROGRESS NOTE computed finding was changed so it can use either the TIU DOCUMENT DEFINITION title or IEN in the computed finding parameter.

> ![](pxrm-2-12-release-notes/012.png) VA-DATE FOR AGE is a new computed finding that uses the COMPUTED FINDING PARAMETER to pass an age in years and returns the date the patient will be that age as the date of the computed finding.

> ![](pxrm-2-12-release-notes/013.png) VA-EMPLOYEE is a new computed finding that returns true if the patient is an employee.

> ![](pxrm-2-12-release-notes/014.png) VA-ADMISSIONS FOR A DATE RANGE is a list type computed finding that can be used to build a list of patients who have been admitted in the specified date range.

> ![](pxrm-2-12-release-notes/015.png) VA-DISCHARGES FOR A DATE RANGE is a list type computed finding that can be used to build a list of patients who have been discharged in the specified date range.

> ![](pxrm-2-12-release-notes/016.png) VA-CURRENT INPATIENTS is a list type computed finding that can be used to build a list of all current inpatients.

> ![](pxrm-2-12-release-notes/017.png) CF VA-IS INPATIENT- This new computed finding will be true if the patient was/is an inpatient on the evaluation date. The following "CSUB" values will be available:

- ADMISSION DATE/TIME (FileMan format)
- ADMISSION TYPE
- ATTENDING PHYSICIAN
- DATE (FileMan format)
- PRIMARY PROVIDER
- TREATING SPECIALTY
- WARD LOCATION

### Reminder Definitions and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/018.png) A hint was added on how to add a second occurrence of a finding. The hint will be displayed when a double question mark is typed when editing the findings in a definition or a term.

> ![](pxrm-2-12-release-notes/019.png) Because of questions about checking for valid usage of TIU Objects, additional checking was added for anyplace a TIU Object can be used in a reminder definition. If an odd number of ―\|‖ characters is found, a warning will be issued. Note: an odd number of ―\|‖ characters in the text will cause TIU Object expansion to fail.

### Reminder Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/020.png) A new option "Check Reminder Dialog for invalid items" has been added to the Dialog Report Menu. This option scans the selected reminder dialog and all of its sub-components for possible problems that could affect the use of the reminder dialog in CPRS. The user can select every dialog type except Additional Prompts and Forced Values. The dialog checker report will check for the following items.

- Disabled dialog items in the selected dialog.
- Incomplete sequences in the selected dialog.
- All sub-items in the selected dialog are pointing to a valid entry on the system.
- All finding items, additional finding items, and orderable items are pointing to a valid entry on the system.
- Result groups are pointing to a valid MH Test and an MH scale has been defined for the result group.
- An odd number of ―\|‖ characters in a dialog text field. If this is the case it would not be possible to determine which part is a TIU Object.
- Progress Note Text and the Alternate Progress Note text fields have valid TIU Objects and TIU Template Fields.

> Example of output

> ![](pxrm-2-12-release-notes/021.png) A new cross-reference was added to file \#801.41: ^PXRMD(801.41,‖RG‖,X,DA(1),DA).

> ![](pxrm-2-12-release-notes/022.png) A problem was found with the dialog orphan report incorrectly displaying a dialog element only used as a replacement item. Result Groups were also showing in the dialog orphan report when the result group was assigned to a parent element.

> ![](pxrm-2-12-release-notes/023.png) It was possible for a user to delete a dialog element if it was only used as a replacement item. The user was also able to delete a result group even when it was being used. This has been fixed and the user should not be able to delete an element or a result group if it is assigned to another dialog element/group.

> ![](pxrm-2-12-release-notes/024.png) The dialog inquiry will now display the value for the patient specific field.

> ![](pxrm-2-12-release-notes/025.png) Changes were made to reminder dialog functionality to support data standardization of findings, the first of which will be Immunizations and Skin Tests:

> o The DISABLE field has been changed from a free-text field to a set of codes: 0 for NO

1.  for DISABLE AND SEND MESSAGE
2.  for DISABLE AND DO NOT SEND MESSAGE

> These codes will be used when loading a reminder dialog in CPRS. If an item is marked as DISABLE AND SEND MESSAGE, a MailMan message will be sent to the Clinical Reminder mail group.

### Reminder Evaluation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/026.png) Pharmacy reengineering requires that direct reads of the various pharmacy files be replaced by APIs.

> ![](pxrm-2-12-release-notes/027.png) Radiology patch RA\*5.0\*56 was released. This patch adds report status to the data returned by the radiology API Clinical Reminders uses, so the Clinical Maintenance output was changed so it now displays the report status. RA\*5.0\*56 was added as a required build.

> ![](pxrm-2-12-release-notes/028.png) Finding date was added as a CSUB data for all reminder finding types.

> ![](pxrm-2-12-release-notes/029.png) SYSTOLIC AND DIASTOLIC were added as CSUB data for the blood pressure finding.

> ![](pxrm-2-12-release-notes/030.png)RANK_DATE was added as a new function that can be used in a Custom Date Due.

### Reminder Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/031.png) Major enhancements were made to Reminder Exchange. The main change visible to users is the ability to select individual reminder file entries for packing. Now when the Create Exchange File Entry (CFE) action is selected, the user will be presented with the following selection list:

> Select from the following reminder files:

> REMINDER COMPUTED FINDINGS REMINDER COUNTING GROUP REMINDER DEFINITION REMINDER DIALOG

> REMINDER EXTRACT COUNTING RULE REMINDER EXTRACT DEFINITION REMINDER LIST RULE

> REMINDER LOCATION LIST REMINDER SPONSOR REMINDER TAXONOMY REMINDER TERM

> ![](pxrm-2-12-release-notes/032.png) Multiple items of different types can be selected for packing into a single Exchange File entry. In previous versions of Reminder Exchange, only reminder definitions could be selected; the packing included everything the definition needed to function, such as sponsor, findings, and dialog. In this new version of Reminder Exchange, this functionality has been extended. When a reminder file entry is selected from the above list, everything it needs to function will be included in the packed entry. For example, an extract definition could include reminder definitions and rule sets, which in turn have their own dependencies. Because of this, an Exchange file entry may contain components that were not expected. To help the user know what is being included as it is packing up an entry, Reminder Exchange will list every single component that is being included.

> ![](pxrm-2-12-release-notes/033.png) For reminder dialogs, selection of individual dialog items is now allowed; the user is no longer limited to packing up the entire dialog.

> ![](pxrm-2-12-release-notes/034.png) TIU/Health Summary Objects will be packed up if they are used in a reminder dialog that is being packed. The Health Summary Type will also be packed up if it does not contain local components and it does not contain the PROGRESS NOTES SELECTED component. A normal TIU Object will not be packed. If a TIU Object or Health Summary Type is not packed up, these items will appear in the list of components in the reminder exchange entries, but they will not be installable. Because of the packing order these items will be installed on the system after the dialog is installed on the system.

> ![](pxrm-2-12-release-notes/035.png) For TIU Objects, Health Summary Objects, Health Summary Types, and/or entries from the Order Dialog file (#101.41) that are not packed up, descriptive text has been added to the reminder exchange entry summary field, describing what is in the items that were not packed up. This should help the receiving sites re-create these items as needed.

> ![](pxrm-2-12-release-notes/036.png) Automated dialog error checking has been added. All dialogs that are on the list to be packed will be checked. Two levels of severity will be reported: WARNING and FATAL ERROR. Each error will give a detailed description of the problems that are found. A FATAL ERROR prevents the dialog from being packed; therefore the packing will abort. A WARNING will allow the packing to proceed.

> FATAL errors mean the dialog will not work and are caused by things such as a pointer to an item that does not exist.

> WARNING means the dialog will function, but possibly not as expected. For example, if the dialog contains a disabled item, a warning will be generated.

> The dialog checker will also check to make sure that dialog components contain items and will generate a fatal packing error if none exist.

> *See Examples in Appendix B.*

> ![](pxrm-2-12-release-notes/037.png) For dialogs that are auto-generated from a reminder definition, a check was added that will disable a dialog element/group if the finding item is inactive as a result of Data Standardization.

> ![](pxrm-2-12-release-notes/038.png) The formatting of the Exchange file entry installation display during a KIDS install was improved. It now shows the number, and if the text is too long to fit on one line, it will be broken into multiple lines instead of just wrapping.

> ![](pxrm-2-12-release-notes/039.png) Because hospital locations are not standardized, they are not transportable. A list of hospital locations that will not be transported is included in the Exchange file entry description.

### Reminder List Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- There are four possible views in list rule management: finding rule, patient list rule, reminder rule, and rule set. When switching between the views, the screen position was being carried over. For example, if you were in the rule set view and line 10 was at the top of the display and you switched into the reminder rule view, it would start at line 10. If there were less than 10 reminder rules, then the display would be blank. The code was changed to save the current position for each view, so that when a particular view is selected, the display will start at the last screen position of that view.

### Reminder Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A generalized finding usage report was created. The user inputs a list of findings to search for, and definitions, terms, and dialogs are searched to report where the findings are used. For findings that are from a standardized file, status and mapping information are included. A new option PXRM FINDING USAGE REPORT was created. It was added as an item to the PXRM REMINDER REPORTS menu.
- A new prompt called "Clinic Stops output" was added to reminder due reports. This prompt allows the user to select what type of output to display when running a reminder due report against selected clinic stops. For a detailed report, the user will have the option to display output either by Clinic Stops only (current output) or by Individual Clinics belonging to the clinic stops. For a summary report with the report totals set to either to "Individual Locations" or by Individual locations plus Totals by Facility," the user will have the same options as the detailed report and a third option of reporting the output by Clinic Stops and Individual Clinic(s).
- Another new option "Print percentages with the report output" has been added. If the user replies

> ―Y,‖ the following percentages will be displayed:

> %Applicable = Number Applicable/Total patient \* 100

> %Due = Number of Due/Number Applicable \* 100

> %Done = 100-%Due

> This field has also been added to the Reminder Report template functionality.

- A new field named Creator was added to report templates. This field is automatically populated when someone creates a reminder report template. It will be used to control edit accesses to the template. In order to edit a template a user must either be the creator or hold the PXRM MANAGER security key. If the user is not the creator or does not hold the PXRM MANAGER security key, they will not see the prompt to edit the template.
- When running a reminder report against multiple patient lists, the results of the report were printed out without the patient list name. Reminder reports were changed to display the patient list name with the patient list results.

### Reminder Taxonomies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ![](pxrm-2-12-release-notes/040.png) Two new options

- Verify all taxonomy Expansions (PXRM TAXONOMY EXPANSION VERIFY)

> Option for verifying the correctness of all taxonomy expansions

- Expand all Taxonomies (PXRM TAXONOMY EXPANSION ALL)

> This option can be used to rebuild all taxonomy expansions (Note the user must hold the PXRM MANAGER security key to use this option.)

> ![](pxrm-2-12-release-notes/041.png) As a result of problems reported with taxonomy expansion, listing of UPDATE^DIE error messages in taxonomy expansion was changed to use MES^XPDUTL so errors will be included in the Install file if taxonomy expansion is done as part of a KIDS install. Also the name and IEN of the taxonomy will be listed.

> ![](pxrm-2-12-release-notes/042.png) An error in taxonomy expansion was found and corrected. For CPT codes associated with a radiology procedure the expansion assumed there could only be one radiology procedure per CPT code. This is not the case; the same CPT code can be used with multiple radiology procedures.

> The expansion was changed to allow for multiple procedures per CPT code.

### Bug fixes in PXRM\*2\*12 Remedy tickets addressed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 231908 - PXRM\*2\*6 question

> 239704 - Display Inconsistent for VA-IRAQ&AFGHANISTAN POST DEPLOYMENT 239705- Documentation Conflict

> 240564 - Incorrect headers appearing in reports. pulling from incorrect field info from PCMM

> Associated Clinics

> 254537 - EDUC TOPIC with LINKED SUBTOPICS fails to take MAIN ed topic with IMPORT 270130 - TYPO in health factor name (Nat'l GEC IADL section)

> 287087 - TBI - OEF/OIF Reminders not resolving 288411 - OEF/OIF and TBI reminder not satisfying 291337 - OEF/OIF Report erroring

> 294762 - TBI won't turn off when NO IRAQ/AFGHAN svc entered 310801 - TBI Dialog slow.

> 312303 - BMI CF is not evaluating correctly when date range is entered and another BMI is calculated outside the Date Range

> 319821- Pt is "due" on OEF/OIF report but reminder does not show due for providers on cover sheet. 324324 - Branching logic problem in Iraq Reminder

> 335776 - When running a reminder report against multiple patient lists, the results of the report are printed out without the patient list name

> ![](pxrm-2-12-release-notes/043.png) If Installation History was selected for an entry that had never been installed and then Installation Details was selected, it generated an undefined error. This was fixed and now the user will see a ―no dates to select‖ message.

> ![](pxrm-2-12-release-notes/044.png) The main Reminder Exchange display was truncating seconds on date packed, so the right margin of the list template was increased from 80 to 84.

> ![](pxrm-2-12-release-notes/045.png) There was a bug in Reminder Exchange where occasionally the checksum of a packed component did not match the checksum of the file entry, even though the packed component came from that exact file entry. This was corrected.

> ![](pxrm-2-12-release-notes/046.png) If a Location List had a value in the field CREDIT STOPS TO EXCLUDE (LIST), the Location List referenced by this field was not automatically being packed-up. The packing routine was changed so it will be automatically be included.

> ![](pxrm-2-12-release-notes/047.png) Under certain conditions deletion of a Clinic Stop from a Location List was generating an extraneous node. The cross-references on CLINIC STOP and CREDIT STOP TO EXCLUDE were modified to eliminate this problem. Code was added to the post-init to clean up any bad nodes that may already exist.

> ![](pxrm-2-12-release-notes/048.png) The misspelling ―overwite‖ was corrected to ―overwrite‖. ![](pxrm-2-12-release-notes/049.png) A prompt in the patient demographic report was incorrect:

> Select from the following inpatient items:

1.  \- WARD LOCATION
2.  \- ROOM-BED
3.  \- ADMISSION DATE/TIME
4.  \- ATTENDING PHYSICIAN

> Enter your selection(s): (1-5):

> It was corrected to the following:

> Select from the following inpatient items:

1.  \- WARD LOCATION
2.  \- ROOM-BED
3.  \- ADMISSION DATE/TIME
4.  \- ATTENDING PHYSICIAN

> Enter your selection(s): (1-4):

> ![](pxrm-2-12-release-notes/050.png) It was reported with PXRM\*2\*6 that when running a detailed PCMM Provider report, the output was no longer reporting by provider, but by associated clinic. This has been changed to report by Provider instead of reporting by associated clinic.

> ![](pxrm-2-12-release-notes/051.png) A problem was found when running a reminder summary report against multiple locations and multiple facilities. If the report was set to report the output by each facility and if there was a location with the same name as each facility and the patient was seen at the different location, the patient would not be included in the count for the location after the first location was counted.

> ![](pxrm-2-12-release-notes/052.png) The display of the final frequency and age range in reminder test was modified to include what set the final frequency. It could be either from the baseline or a finding. Example:

> ^TMP(PXRMID,\$J,660004,"zFREQARNG")=0Y^^^Finding 1

> ![](pxrm-2-12-release-notes/053.png) When routine PXRMETCO was distributed in patch PXRM\*2\*6, it mistakenly had patch 4 on the second line; this was corrected.

> ![](pxrm-2-12-release-notes/054.png) The second line of PXRMEXLM was erroneously marked with patch 4 when it was released in patch

> 6\. The 4 has been removed.

> ![](pxrm-2-12-release-notes/055.png) Remedy Ticket 247577 highlighted some confusion with the meaning of a phrase in the code set expansion message. The phrase:

> The following are new CPT codes in the expansion for this taxonomy:

> was changed to:

> The following CPT codes were not in the previous expansion for this taxonomy:

> ![](pxrm-2-12-release-notes/056.png) There was a typo in the name of a GEC health factor GEC RECENT CHANGE IN IADL RX-NO. It was changed to GEC RECENT CHANGE IN IADL FX-NO. Remedy ticket \# HD0000000270130.

> ![](pxrm-2-12-release-notes/057.png) The variable pointer setup for reminder definitions and reminder terms incorrectly used the name EDUCATION TOPIC; it was changed to the correct name EDUCATION TOPICS.

> ![](pxrm-2-12-release-notes/058.png) For a number of years there have been reports that the output from Reminder Due Reports occasionally didn't show up. This problem was not reproducible and a number of things were done to try to find the cause. It appears that a possible cause might be that some sites have created aggressive cleanup routines to delete tasks that are not scheduled. This discovery led to a restructuring of reminder due reports. Previously, two tasks were created: the first assembled the data and the second produced the output. In order to not tie up the output device while the data was being assembled, the print job was not scheduled to run until the assembly job finished. In the new structure, the assembly and print job are combined, but the output device is not opened until the output is ready to print.

> ![](pxrm-2-12-release-notes/059.png) A problem with incorrect date ordering for multiple occurrences of a location list finding was corrected.

> ![](pxrm-2-12-release-notes/060.png) In the patient demographics report when only the phone number was selected and the patient had a confidential address in effect, the following error occurred: \$ZE=

> \<UNDEFINED\>GETPDATA+53^PXRMPDR \*DDATA("ADD",22,"LEN"). The problem was

> corrected.

> ![](pxrm-2-12-release-notes/061.png) A hard error was generated in reminder term inquiry if a health factor finding did not have a category. A change was made so that instead of the hard error, the category will be listed as UNDEFINED. The print template was updated so there is a space after ―No.‖

> ![](pxrm-2-12-release-notes/062.png) A problem was reported where if an active dialog element/group branched to a disabled dialog element, the original active dialog element/group was still showing in CPRS. To fix this, a national element named VA-DISABLE BRANCHING LOGIC REPLACEMENT ELEMENT will be distributed with patch 12. This element will be used as the replacement element if the branched-to element/group is marked disabled. This new element will display the following text in CPRS:

> "You have branched to a disabled element/group. Please contact the reminder manager to fix this dialog."

### GMTS\*2.7\*89 Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/063.png) This patch contains an enhancement to Health Summary Objects. Sites will now be able to overwrite the "No Data Available" message in the TIU/HS Object if the Health Summary Type does not return any data. This was done by adding a new field, OVERWRITE NO DATA, to the Health Summary Object file, file 142.5.

> ![](pxrm-2-12-release-notes/064.png) To override the no data available message, the SUPPRESS COMPONENTS WITHOUT DATA field must be set to "YES" and text must be defined in the OVERWRITE NO DATA AVAILABLE field. This text will replace the default message.

> ![](pxrm-2-12-release-notes/065.png) A new API (EN^GMTSDESC) has been created to display the definition of a Health Summary Type, Health Summary Object, and a Health Summary Component in a readable output. This API was created to support Clinical Reminders in posting a description of a Health Summary Type and Health Summary Objects when packing up a reminder dialog that contains a TIU/HS Object.

> ![](pxrm-2-12-release-notes/066.png) Two new national Health Summary Components are being released with this patch: Clinical Reminders Findings

> Clinical Reminders Last Done

> The Clinical Reminders Findings component works like the Clinical Maintenance components. However, it only lists the name of the reminder and the findings evaluation for the reminder. It does not display the status line and it does not list the frequency line.

> Clinical Reminders Last Done components display the reminder name and the last done date if the last done date is defined. If the last done date is unknown, the last done date will be blank.

> Neither of these components will list the header line

> ―--STATUS-- --DUE DATE LAST DONE—

> ![](pxrm-2-12-release-notes/067.png) Remedy ticket \#332249

> It was reported that a Health Summary Object or a Health Summary Type could not be modified if the user was not the owner and was trying to edit these files in the TIU/HS Object editor.

> Resolution: The TIU/HS Object editor was changed so that a user who holds the GMTSMGR security key can edit a Health Summary Object or a Health Summary Type, regardless of the owner.

### OR\*3\*295 Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/068.png) This patch fixes a problem with encounter data not being deleted when the user deletes an unsigned note. This problem was caused when the user wrote a note and entered encounter data for this note. If the user did not sign the note, then worked on other patient records in CPRS, and then went back to the patient with the unsigned note and deleted the note, the note would be deleted from the system.

> However, the encounter data would still show in PCE.

> ![](pxrm-2-12-release-notes/069.png) Remedy 276466: Custom Order View Not Working as Expected. After installation of CPRS 27, one site reported that the Custom Order View "Unverified by Clerk-All Services" was not working properly. The Outpatient Med Orders were not showing up even though they were within the specified date range. This patch fixes this issue so that the Outpatient Med Orders will show up properly.

### TIU\*1\*249 Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-12-release-notes/070.png) Several new APIs have been created to display the definition of TIU Object and TIU Template fields.

> These APIs will be used by the Clinical Reminder Exchange functionality.

> ![](pxrm-2-12-release-notes/071.png) A change was made to the TIU/HS List Manager Interface to display a Health Summary Object field OVERWRITE NO DATA MESSAGE. See the GMTS\*2.7\*89 patch description for more information on this field.

> ![](pxrm-2-12-release-notes/072.png) The parameter TIU TEMPLATE REMINDER DIALOGS was updated to work with the changes made to Reminder Dialogs in patch PXRM\*2\*12.

> ![](pxrm-2-12-release-notes/073.png) Remedy ticket \#332249

> It was reported that a Health Summary Object or a Health Summary Type could not be modified if the user was not the owner and was trying to edit these files in the TIU/HS Object editor.

> Resolution: The TIU/HS Object editor was changed so that a user who holds the GMTSMGR security key can edit a Health Summary Object or a Health Summary Type, regardless of the owner.
