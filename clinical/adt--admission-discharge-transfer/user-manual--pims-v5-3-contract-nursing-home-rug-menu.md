---
title: PIMS Version 5.3 User Manual - Contract Nursing Home RUG Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Contract Nursing Home RUG Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: Each of the options found on the Contract Nursing Home RUG Menu works as its corresponding option on the RUG-II menu except only CNH PAIs are selectable. The CNH options should be used to create a Patient Assessment Instrument (PAI) for those patients receiving contract nursing home services. If the
audience: 
keywords: 
  - contents
  - date
  - table
  - record
  - patient
  - assessment
  - pais
  - admission
  - transfer
  - status
page_count: 0
word_count: 3386
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2009
revision_count: 1
revision_newest: 1/29/09
revision_oldest: 1/29/09
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_cnhr_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_cnhr_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

PIMS V. 5.3 ADT Module User Manual

Contract Nursing Home Rug Menu

![](pims-version-5-3-user-manual-contract-nursing-home-rug-menu/001.png)

January 2009

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
  - [Overview](#overview)
  - [Close a CNH PAI record](#close-a-cnh-pai-record)
  - [CNH PAI Edit](#cnh-pai-edit)
  - [Create A CNH PAI Record](#create-a-cnh-pai-record)
  - [Delete A CNH PAI Record](#delete-a-cnh-pai-record)
  - [Open A Closed Or Transmitted CNH PAI](#open-a-closed-or-transmitted-cnh-pai)
  - [Outputs Menu](#outputs-menu)
    - [Incomplete PAIS By Location](#incomplete-pais-by-location)
    - [PAIS For A Date Range](#pais-for-a-date-range)
    - [Record Status Report](#record-status-report)
    - [RUG-II Index](#rug-ii-index)
    - [Single PAI Print](#single-pai-print)
    - [RUG-II Grouper](#rug-ii-grouper)
    - [Test Grouper](#test-grouper)
  - [Close a CNH PAI Record](#close-a-cnh-pai-record-1)
  - [CNH PAI Edit](#cnh-pai-edit-1)
  - [Create a CNH PAI Record](#create-a-cnh-pai-record-1)
  - [Open a Closed or Transmitted CNH PAI](#open-a-closed-or-transmitted-cnh-pai-1)
  - [Outputs Menu](#outputs-menu-1)
    - [Incomplete PAIs by Location](#incomplete-pais-by-location-1)
    - [PAIs for a Date Range](#pais-for-a-date-range-1)
    - [Record Status Report](#record-status-report-1)
    - [RUG-II Index](#rug-ii-index-1)
    - [Single PAI Print](#single-pai-print-1)
  - [RUG-II Grouper](#rug-ii-grouper-1)
  - [Test Grouper](#test-grouper-1)
Revision History
Initiated on 1/29/09
|          |                                                                                                    |                                    |                                    |
|----------|----------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| Date | Description (Patch \# if applic.)                                                              | Project Manager                | Technical Writer               |
| 1/29/09  | Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC) | <span class="mark">Redacted</span> | <span class="mark">Redacted</span> |

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each of the options found on the Contract Nursing Home RUG Menu works as its corresponding option on the RUG-II menu except only CNH PAIs are selectable. The CNH options should be used to create a Patient Assessment Instrument (PAI) for those patients receiving contract nursing home services.
If the user holds the DG RUG SUPERVISOR key, the user is able to open, close, edit, or delete all PAIs from either the RUG-II options or the CNH PAI options. Modifications were made to the Outputs Menu options and the RUG-II Grouper option to allow both regular PAIs and CNH PAIs to be reflected in the reports from either menu. This occurs regardless of whether or not the user holds the above-mentioned key. Transmission to Austin will include CNH PAIs as well as regular PAIs. The option to transmit to Austin will remain only on the RUG-II menu. All of the same criteria must be met to transmit, with the exception that CNH PAIs will not include Bed Section data. CNH PAIs will automatically be transmitted when the user selects to transmit admission/transfer PAIs.
The following is a list of the Contract Nursing Home RUG Menu options and their comparable RUG-II Menu options.
CNH RUG Menu Option RUG-II Menu Option
Close a CNH PAI Record Close a PAI Record
CNH PAI Edit PAI Enter/Edit
Create a CNH PAI Record Create a PAI from Past Admission/Transfer
Delete a CNH PAI Record Delete a PAI
Open a Closed or Transmitted CNH PAI Open a Closed or Transmitted PAI
Outputs Menu Outputs Menu
RUG-II Grouper RUG-II Grouper
Test Grouper Test Grouper
The Resource Utilization Group-II, or RUG-II Model, is used to assess the levels of long-term patient care. Each time an admission and/or transfer occurs to a Nursing Home Care Unit (NHCU) or Intermediate Medicine ward, a Patient Assessment Instrument (PAI) is created by a background job. However, a PAI is not created when movement occurs between NHCUs or between Intermediate Medicine wards and no more than one PAI can be created per admission/transfer date. The PAI information is stored in the Patient Assessment File (PAF) until transmission to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).
All ward location prompts within the RUG-II options are screened by service. Only wards identified as providing intermediate medicine and/or nursing home care services will be allowed as responses.
Overview
The Test Grouper option will enable you to enter CNH PAI information and determine RUG-II grouping without storing the information.
The Incomplete PAIs by Location option should be run routinely for maximum benefit.
The following is a brief description of the major functions of each of the CNH RUG options.

## Close a CNH PAI record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to change the status of a CNH PAI from open to closed after it has been completed. Security key DG RUG CLOSE PAI is required to access this option.

## CNH PAI Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter data into a previously established CNH PAI or edit existing data.

## Create A CNH PAI Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to manually create a CNH PAI using an applicable admission/transfer date for the patient.

## Delete A CNH PAI Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to delete a CNH Patient Assessment Instrument.

## Open A Closed Or Transmitted CNH PAI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to change the CNH PAI status from CLOSED/TRANSMITTED to COMPLETE. The record may then be edited.

## Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Incomplete PAIS By Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a listing of all Patient Assessment Instrument (PAI) records for a selected date range with a status of incomplete.

### PAIS For A Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print Patient Assessment Instruments for a selected date range.

### Record Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to obtain a breakdown of the status of each PAI record for a specified date range.
Overview

### RUG-II Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to obtain a breakdown of RUGs by ward for a specified date range.

### Single PAI Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print out a single Patient Assessment Instrument for the selected patient.

### RUG-II Grouper

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display the calculated RUG-II Group, Clinical Category, ADL sum, and WWU for a completed PAI.

### Test Grouper

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to determine a RUG-II Group, ADL sum, Hierarchy Group, and WWU without storing the data.

## Close a CNH PAI Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables you to change a CNH Patient Assessment Instrument (PAI) status from OPEN to CLOSED.
A CNH PAI record must be CLOSED in order to be transmitted from the Patient Assessment File (PAF) to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). In order for a CNH PAI to be CLOSED, it must first have a status of COMPLETED and contain no errors.

## CNH PAI Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CNH PAI Edit option is used to enter data into a previously established CNH PAI or edit existing data. Only those CNH PAIs that have a status of COMPLETE or INCOMPLETE may be selected.
If the patient demographic information, ssn, sex, and date of birth, has not been previously entered, you will be prompted to complete those data items. This action updates the RUG-II PATIENT ASSESSMENT file but not the PATIENT file. All fields of a Patient Assessment Instrument must be completed with a valid entry in order for a RUG-II group to be determined and the data to be transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Each time an attempt is made to exit an incomplete PAI, the missing data items will be displayed, and you will be given the opportunity to complete editing.
You may enter double question marks (??) at most prompts for a detailed explanation of the field and what is required in answering the prompt.
The majority of the prompts appear with defaults. These are provided to reduce the number of keystrokes necessary to complete a PAI; however, you must accept the default at each prompt (by entering \<RET\>) or enter the correct value for it to be stored in the PAF file.
After all the questions have been answered, the system will determine the RUG-II Group, hierarchy group, Activities for Daily Living (ADL) sum, and the weighted work units (WWU) from the entered data.
Users who hold the security key DG RUG CLOSE PAI are afforded the opportunity to close the completed PAI through this option.
CNH PAI Edit
Consistency checks performed include:
IF THEN
TUBE FEEDING or PARENTERAL EATING = 5
FEEDING = YES
TUBE FEEDING or PARENTERAL EATING MUST NOT = 5
FEEDING = NO
TUBE FEEDING = YES TUBE FEEDING ROUTE MUST NOT = 1
For Therapy Levels
IF THEN
LEVEL = 1 DAYS = 0
HOURS/MINUTES = 0
LEVEL \> 1 DAYS \> 0
HOURS/MINUTES <u>\></u> 30 min.

## Create a CNH PAI Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Patient Assessment Instrument (PAI) record is established by the system through a background job each time an admission and/or transfer occurs to a NHCU or Intermediate Medicine Ward. However, there are times when a PAI must be created manually; for example, if the admission/transfer is entered two or more days after the background job is run or if a PAI is deleted in error. Through this option, you may create a CNH PAI using a valid past admission/ transfer date for the patient.
The system will prompt for the purpose of this assessment; whether it is for the semi-annual census or for an admission/transfer. If the assessment purpose is admission/transfer, it must be a date for which no other PAI has been created for that patient.
The admission/transfer date selected for admission/ transfer assessments must be on or after the last closeout date. It must be an admission/transfer to a ward whose service is Intermediate Medicine or Nursing Home care.
A PAI with a purpose of semi-annual can only be created with an assessment date within a month of the semi-annual census date. A PAI with an assessment purpose of admission/transfer can only be created for an admission/transfer within the current closeout cycle.
If both the selected admission date and transfer dates are applicable, the admission date will be listed as number 1 in the group to choose from followed by the transfer dates in reverse chronological order. If only transfer dates are applicable, they will be listed in reverse chronological order beginning at number 1. If only the admission date is applicable, the selected admission date will be listed as the only choice.
When the PAI has been successfully created, the message "ASSESSMENT RECORD CREATED" will appear, and the PAI will be assigned a status of INCOMPLETE.
Create a CNH PAI Record
The following is an explanation of the messages that may appear while utilizing the option.
1\) If survey purpose has been specified as Admission/Transfer and you enter an assessment date for which there already exists a PAF entry for that patient, the following message will be displayed.
"There is already a PAF entry for that date."
2\) If you select an admission date for which neither the admission date nor the transfer dates (if any) meet the date and service criteria specified on the preceding page, the following message will be displayed.
"NEITHER ADMISSION NOR TRANSFERS ARE TO INTERMEDIATE CARE OR NURSING HOME WARDS AFTER THE LAST CLOSEOUT."
3\) If an incorrect assessment date is entered, one of the following messages may appear.
"Assessment date must be within a month of the semi-annual census date"
OR
"The assessment date must not be before the date of admission/transfer in."
Delete a CNH PAI Record
Through this option, you may delete any CNH Patient Assessment Instrument (PAI) record prior to transmission to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Because PAIs are created through the RUG-II Background job, a PAI may be created that is not necessary (due to length of stay, etc.). This option would be used to delete such a PAI.
You may choose the PAF record to be deleted by patient name, SSN, or ward. If there is more than one PAI for this patient, you will be asked to choose the correct record for deletion.

## Open a Closed or Transmitted CNH PAI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open a Closed or Transmitted CNH PAI option is used to open a closed/transmitted CNH PAI and change the PAI status from CLOSED/TRANSMITTED to COMPLETE. This is necessary if you wish to edit a PAI record that has been closed/transmitted. After the record is opened, the CNH PAI Edit option should be used to edit the record.
Information such as the patient's date of birth, social security number, the assessment date and purpose, and whether the veteran is service connected or non-service connected will be displayed after the PAI record is selected.

## Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Incomplete PAIs by Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Incomplete PAIs by Location option is used to print a listing of Patient Assessment Instrument (PAI) records for a selected date range with a status of INCOMPLETE.
You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.
If the location of a patient is missing, that patient will be included in a listing which precedes this report.
Information provided for each incomplete instrument may include patient name and social security number, date of admission/transfer, and the assessment purpose (semi-annual census, admission/transfer, or contract nursing home). The date range selected and the date/time the report was printed is also shown. The report for each location selected will be printed on a separate page.
If you choose to display the report on the screen, you may up-arrow \<^\> at the end of any screen display to return to the menu.
It is recommended that this option be run on a frequent basis to ensure that all necessary PAIs are completed.
Outputs Menu

### PAIs for a Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PAIs for a Date Range option is used to print Patient Assessment Instruments for a selected date range. They may be sorted by assessment date or transfer/admission date.
You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.
Each PAI printed out is divided into 7 sections. Data items found in the first section may include assessment date, bed section, record status, and patient information such as sex, year of birth, and social security number. Remaining sections are Medical Treatments, Medical Events, Selected Diagnosis, Activities of Daily Living, Behaviors, and Specialized Services. Specialized Services include Rehabilitation Medicine Therapies and Chronic Respiratory Support.
Those question numbers of the PAI which are reserved fields and not displayed are listed at the bottom of the output.
Outputs Menu

### Record Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Record Status Report option is used to obtain a break-down, by location, of the status of each PAI record for a specified date range. You may choose to sort the report by assessment date or admission/transfer date.
You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.
Information provided for each PAI listed may include record status, patient name, social security number, assessment date/purpose, admission/transfer date, ADL sum, RUG, and Weighted Work Unit.
Outputs Menu

### RUG-II Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RUG-II Index report is used to obtain a breakdown of RUGs by location for a specified date range. You may choose to print contract nursing home PAIs, regular PAIs, or both. The report may be run for one, many, or all of each of the following data items: division (at multidivisional facilities), location, RUG II group, patient, and category. The output may be sorted by assessment or transfer/admission date.
The output produced by this option consists of histograms and a separate listing which may include location, RUG group, patient name, social security number, date of birth, assessment date/purpose, admission/transfer date, current status of patient, category, and WWU (weighted work unit). Patients absent from the location will be designated by two asterisks (\*\*) in the current status column. The histograms show the percentage of patients in each RUG group during the date range. One is printed for each location, and a cumulative histogram is provided to include all selected locations. If only one location is selected, only one histogram will be printed since the summary histogram would be identical to the one for the location.
If there are no matches found within the data selected, the following message will be displayed and you will be returned to the menu.
"\*\*\*RUG-II INDEX REPORTS--NO MATCHES FOUND\*\*\*"
Outputs Menu

### Single PAI Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Single PAI Print option is used to print out a single Patient Assessment Instrument for the selected patient. This output must be generated at a margin width of 132 columns.
The printout is divided into 7 sections. Data items found in the first section may include assessment date, bed section, record status, and patient information such as sex, year of birth, and social security number. Remaining sections are Medical Treatments, Medical Events, Selected Diagnosis, Activities of Daily Living, Behaviors, and Specialized Services. Specialized Services include Rehabilitation Medicine Therapies and Chronic Respiratory Support.
Those question numbers of the PAI which are reserved fields and not displayed are listed at the bottom of the output.
At the prompt, "Select PAF Name:", you may enter the PAF record number, the patient name, or the transmission date. If there is more than one PAI for the patient or date entered, they will be listed for selection.

## RUG-II Grouper

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display the RUG-II Group, ADL (Activity of Daily Living) Sum, WWUs (Weighted Work Units), and Hierarchy Group for a completed Patient Assessment Instrument (PAI) for a selected patient. If the PAI you choose has an INCOMPLETE status, no RUG-II Group can be determined and all incomplete fields will be listed.

## Test Grouper

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Test Grouper option allows the user to answer the Patient Assessment Instrument (PAI) questions and determine a RUG-II Group, Activities for Daily Living (ADL) sum, hierarchy group, and assigned weighted work units (WWU) based on the WWU values for the selected fiscal year. None of the information entered will be stored for later use.
The possible hierarchy groups (or categories) are heavy rehabilitation, special care, clinical complex, severe behavioral, and physical. The ADL sum is determined from the eating, transferring, and toileting questions.
The user may enter double question marks (??) at most prompts to obtain detailed information as to what is required in answering that question.
If there are any inconsistencies, they will be displayed and you will be prompted to correct them. Consistency checks performed include:
IFTHEN
TUBE FEEDING or PARENTERAL EATING = 5
FEEDING = YES
TUBE FEEDING or PARENTERAL EATING MUST NOT = 5
FEEDING = NO
TUBE FEEDING = YES TUBE FEEDING ROUTE MUST NOT = 1
WARD DEFINED SERVICE = BEDSECTION
CVD = NO ALL CVD RELATED QUESTIONS = 1
For Therapy Levels
IFTHEN
LEVEL = 1 DAYS = 0
HOURS/MINUTES = 0
LEVEL \> 1 DAYS \> 0
HOURS/MINUTES = or \> 30 min.
