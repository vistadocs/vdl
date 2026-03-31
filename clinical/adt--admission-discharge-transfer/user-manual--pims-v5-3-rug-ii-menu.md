---
title: PIMS Version 5.3 User Manual - RUG-II Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: RUG-II Menu
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
description: "OverviewNOTE: Each of the options found on the Contract Nursing Home RUG Menu works as its corresponding option on this menu except only CNH PAIs are selectable. The CNH options should be used to create a Patient Assessment Instrument (PAI) for those patients receiving contract nursing home services"
audience: 
keywords: 
  - date
  - assessment
  - patient
  - admission
  - transfer
  - record
  - pais
  - group
  - status
  - selected
page_count: 0
word_count: 3669
section_count: 0
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 3
revision_newest: 1/29/09
revision_oldest: 11/18/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_rug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_rug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

PIMS V. 5.3 ADT Module User ManualRUG-IIMenu

Close a PAI Record

Create a PAI from Past Admission/Transfer

Delete a PAI

Open a Closed or Transmitted PAI

Outputs Menu

> Incomplete PAIs by Location

> PAIs for a Date Range

> Record Status Report

> RUG-II Index

> Single PAI Print

PAI Enter/Edit

RUG-II Grouper

Test Grouper

Transmission via VADATS

Revision History

Initiated on 11/18/04

|          |                                                                                                    |                                    |                                    |
|----------|----------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| Date | Description (Patch \# if applic.)                                                              | Project Manager                | Technical Writer               |
| 11/18/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data                                | <span class="mark">redacted</span> | <span class="mark">Redacted</span> |
| 8/14/08  | Minor Formatting Changes                                                                           | <span class="mark">Redacted</span> | <span class="mark">Redacted</span> |
| 1/29/09  | Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC) | <span class="mark">Redacted</span> | <span class="mark">Redacted</span> |
|          |                                                                                                    |                                    |                                    |

  
OverviewNOTE: Each of the options found on the Contract Nursing Home RUG Menu works as its corresponding option on this menu except only CNH PAIs are selectable. The CNH options should be used to create a Patient Assessment Instrument (PAI) for those patients receiving contract nursing home services.

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

The Test Grouper option will enable you to enter PAI information and determine RUG-II grouping without storing the information.

The Incomplete PAIs by Location option should be run routinely for maximum benefit.

> **NOTE:** Two RUG options, WWU Enter/Edit for RUG-II and RUG Semi-Annual Background Job can be found in the Supervisor ADT Menu.

The following is a brief description of the major functions of each of the RUG options.

CLOSE A PAI RECORD

This option is used to change the status of a PAI from open to closed after it has been completed. Security key DG RUG CLOSE PAI is required to access this option.

CREATE A PAI FROM PAST ADMISSION/TRANSFER

This option is used to manually create a PAI using an applicable admission/transfer date for the patient.

DELETE A PAI

This option is used to delete a Patient Assessment Instrument.

OPEN A CLOSED OR TRANSMITTED PAI

This option is used to change the PAI status from CLOSED/TRANSMITTED to COMPLETE. The record may then be edited.

OUTPUTS MENU

> INCOMPLETE PAIS BY LOCATION

> This option is used to print a listing of all Patient Assessment Instrument (PAI) records for a selected date range with a status of incomplete.

> PAIS FOR A DATE RANGE

> This option is used to print Patient Assessment Instruments for a selected date range.

Overview

> RECORD STATUS REPORT

> This option is used to obtain a breakdown of the status of each PAI record for a specified date range.

> RUG-II INDEX

> This option is used to obtain a breakdown of RUGs by ward for a specified date range.

> SINGLE PAI PRINT

> This option is used to print out a single Patient Assessment Instrument for the selected patient.

PAI ENTER/EDIT

This option is used to enter data into a previously established PAI or edit existing data.

RUG-II GROUPER

This option is used to display the calculated RUG-II Group, Clinical Category, ADL sum, and WWU for a completed PAI.

TEST GROUPER

This option is used to determine a RUG-II Group, ADL sum, Hierarchy Group, and WWU without storing the data.

TRANSMISSION VIA VADATS

This option is used to transmit closed PAI records from the Patient Assessment File to certain domains. Security key DG RUG TRANSMISSION is required to access this option.

Close a PAI Record

This option enables you to change a Patient Assessment Instrument (PAI) status from OPEN to CLOSED.

A PAI record must be CLOSED in order to be transmitted from the Patient Assessment File (PAF) to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). In order for a PAI to be CLOSED, it must first have a status of COMPLETED and contain no errors.

Create a PAI from Past Admission/Transfer

A Patient Assessment Instrument (PAI) record is established by the system through a background job each time an admission and/or transfer occurs to a NHCU or Intermediate Medicine Ward. However, there are times when a PAI must be created manually; for example, if the admission/transfer is entered two or more days after the background job is run or if a PAI is deleted in error. Through this option, you may create a PAI using a valid past admission/ transfer date for the patient.

The system will prompt for the purpose of this assessment; whether it is for the semi-annual census or for an admission/transfer. If the assessment purpose is admission/transfer, it must be a date for which no other PAI has been created for that patient.

The admission/transfer date selected for admission/ transfer assessments must be on or after the last closeout date. It must be an admission/transfer to a ward whose service is Intermediate Medicine or Nursing Home care.

A PAI with a purpose of semi-annual can only be created with an assessment date within a month of the semi-annual census date. A PAI with an assessment purpose of admission/transfer can only be created for an admission/transfer within the current closeout cycle.

If both the selected admission date and transfer dates are applicable, the admission date will be listed as number 1 in the group to choose from followed by the transfer dates in reverse chronological order. If only transfer dates are applicable, they will be listed in reverse chronological order beginning at number 1. If only the admission date is applicable, the selected admission date will be listed as the only choice.

When the PAI has been successfully created, the message "ASSESSMENT RECORD CREATED" will appear, and the PAI will be assigned a status of INCOMPLETE.

The following is an explanation of the messages that may appear while utilizing the option.

1\) If survey purpose has been specified as Admission/Transfer and you enter an assessment date for which there already exists a PAF entry for that patient, the following message will be displayed.

"There is already a PAF entry for that date."

Create a PAI from Past Admission/Transfer

2\) If you select an admission date for which neither the admission date nor the transfer dates (if any) meet the date and service criteria specified on the preceding page, the following message will be displayed.

"NEITHER ADMISSION NOR TRANSFERS ARE TO INTERMEDIATE CARE OR NURSING HOME WARDS AFTER THE LAST CLOSEOUT."

3\) If an incorrect assessment date is entered, one of the following messages may appear.

"Assessment date must be within a month of the semi-annual census date"

OR

"The assessment date must not be before the date of admission/transfer in."

Delete a PAI

Through this option, you may delete any Patient Assessment Instrument (PAI) record prior to transmission to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Because PAIs are created through the RUG-II Background job, a PAI may be created that is not necessary (due to length of stay, etc.). This option would be used to delete such a PAI.

You may choose the PAF record to be deleted by patient name, SSN, ward, or bedsection. If there is more than one PAI for this patient, you will be asked to choose the correct record for deletion.

Open a Closed or Transmitted PAI

The Open a Closed or Transmitted PAI option is used to open a closed/transmitted PAI and change the PAI status from CLOSED/TRANSMITTED to COMPLETE. This is necessary if you wish to edit a PAI record that has been closed/

transmitted. After the record is opened, the PAI Enter/Edit option should be used to edit the record.

Information such as the patient's date of birth, social security number, the assessment date and purpose, and whether the veteran is service connected or non-service connected will be displayed after the PAI record is selected.

Outputs MenuIncomplete PAIs by Location

The Incomplete PAIs by Location option is used to print a listing of Patient Assessment Instrument (PAI) records for a selected date range with a status of INCOMPLETE.

You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.

If the location of a patient is missing, that patient will be included in a listing which precedes this report.

Information provided for each incomplete instrument may include patient name and social security number, date of admission/transfer, and the assessment purpose (semi-annual census, admission/transfer, or contract nursing home). The date range selected and the date/time the report was printed is also shown. The report for each location selected will be printed on a separate page.

If you choose to display the report on the screen, you may up-arrow \<^\> at the end of any screen display to return to the menu.

It is recommended that this option be run on a frequent basis to ensure that all necessary PAIs are completed.

Outputs MenuPAIs for a Date Range

The PAIs for a Date Range option is used to print Patient Assessment Instruments for a selected date range. They may be sorted by assessment date or transfer/

admission date.

You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.

Each PAI printed out is divided into 7 sections. Data items found in the first section may include assessment date, bed section, record status, and patient information such as sex, year of birth, and social security number. Remaining sections are Medical Treatments, Medical Events, Selected Diagnosis, Activities of Daily Living, Behaviors, and Specialized Services. Specialized Services include Rehabilitation Medicine Therapies and Chronic Respiratory Support.

Those question numbers of the PAI which are reserved fields and not displayed are listed at the bottom of the output.

Outputs MenuRecord Status Report

The Record Status Report option is used to obtain a break-down, by location, of the status of each PAI record for a specified date range. You may choose to sort the report by assessment date or admission/transfer date.

You may choose to print contract nursing home PAIs, regular PAIs, or both. The records may be printed for one/many/all divisions (at multidivisional facilities), one/many/all wards, and one/many/all CNH locations.

Information provided for each PAI listed may include record status, patient name, social security number, assessment date/purpose, admission/transfer date, ADL sum, RUG, and Weighted Work Unit.

Outputs MenuRUG-II Index

The RUG-II Index report is used to obtain a breakdown of RUGs by location for a specified date range. You may choose to print contract nursing home PAIs, regular PAIs, or both. The report may be run for one, many, or all of each of the following data items: division (at multidivisional facilities), location, RUG II group, patient, and category. The output may be sorted by assessment or transfer/admission date.

The output produced by this option consists of histograms and a separate listing which may include location, RUG group, patient name, social security number, date of birth, assessment date/purpose, admission/transfer date, current status of patient, category, and WWU (weighted work unit). Patients absent from the location will be designated by two asterisks (\*\*) in the current status column. The histograms show the percentage of patients in each RUG group during the date range. One is printed for each location, and a cumulative histogram is provided to include all selected locations. If only one location is selected, only one histogram will be printed since the summary histogram would be identical to the one for the location.

If there are no matches found within the data selected, the following message will be displayed and you will be returned to the menu.

"\*\*\*RUG-II INDEX REPORTS--NO MATCHES FOUND\*\*\*"

Outputs MenuSingle PAI Print

The Single PAI Print option is used to print out a single Patient Assessment Instrument for the selected patient. This output must be generated at a margin width of 132 columns.

The printout is divided into 7 sections. Data items found in the first section may include assessment date, bed section, record status, and patient information such as sex, year of birth, and social security number. Remaining sections are Medical Treatments, Medical Events, Selected Diagnosis, Activities of Daily Living, Behaviors, and Specialized Services. Specialized Services include Rehabilitation Medicine Therapies and Chronic Respiratory Support.

Those question numbers of the PAI which are reserved fields and not displayed are listed at the bottom of the output.

At the prompt, "Select PAF Name:", you may enter the PAF record number, the patient name, or the transmission date. If there is more than one PAI for the patient or date entered, they will be listed for selection.

PAI Enter/Edit

The PAI Enter/Edit option is used to enter data into a previously established PAI or edit existing data. Only those PAIs that have a status of COMPLETE or INCOMPLETE may be selected.

If the patient demographic information, ssn, sex, and date of birth, has not been previously entered, you will be prompted to complete those data items. This action updates the RUG-II PATIENT ASSESSMENT file but not the PATIENT file. All fields of a Patient Assessment Instrument must be completed with a valid entry in order for a RUG-II group to be determined and the data to be transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Each time an attempt is made to exit an incomplete PAI, the missing data items will be displayed, and you will be given the opportunity to complete editing.

You may enter double question marks (??) at most prompts for a detailed explanation of the field and what is required in answering the prompt.

The majority of the prompts appear with defaults. These are provided to reduce the number of keystrokes necessary to complete a PAI; however, you must accept the default at each prompt (by entering \<RET\>) or enter the correct value for it to be stored in the PAF file.

After all the questions have been answered, the system will determine the RUG-II Group, hierarchy group, Activities for Daily Living (ADL) sum, and the weighted work units (WWU) from the entered data.

Users who hold the security key DG RUG CLOSE PAI are afforded the opportunity to close the completed PAI through this option.

Consistency checks performed include:

IF THEN

TUBE FEEDING or PARENTERAL EATING = 5

FEEDING = YES

TUBE FEEDING or PARENTERAL EATING MUST NOT = 5

FEEDING = NO

TUBE FEEDING = YES TUBE FEEDING ROUTE MUST NOT = 1

PAI Enter/Edit

For Therapy Levels

IF THEN

LEVEL = 1 DAYS = 0

HOURS/MINUTES = 0

LEVEL \> 1 DAYS \> 0

> HOURS/MINUTES <u>\></u> 30 min.

RUG-II Grouper

This option is used to display the RUG-II Group, ADL (Activity of Daily Living) Sum, WWUs (Weighted Work Units), and Hierarchy Group for a completed Patient Assessment Instrument (PAI) for a selected patient. If the PAI you choose has an INCOMPLETE status, no RUG-II Group can be determined and all incomplete fields will be listed.

Test Grouper

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

<u>  
</u>Transmission via VADATS

The Transmission via VADATS option is used to electronically transmit CLOSED PAI records from the Patient Assessment File (PAF) to certain domains. The domains are locations set up to receive the transmissions. Most sites will only transmit to one domain - the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). However, it is possible to transmit data to more than one domain at the same time.

The records are selected for transmission by assessment date and purpose (admission/transfer or semi-annual census.) The assessment start date must be within current closeout cycle. Start date and end date must both be prior to 10/2/89 or both must be after 10/2/89. You cannot overlap the RUG17 conversion date.

The option generates a report of the PAI records that were not transmitted either through "errors" (i.e., records without a CLOSED status), because they were already transmitted, or those records with an assessment date prior to the admission/transfer date. The patient name and social security number, the assessment date, and record status are provided for each record listed. At the bottom of the report, the system will provide the number of records which were transmitted, the selected date range, and assessment purpose.

An electronic MailMan message is generated through the use of this option. The sender and members of the specified mail group will receive the message as NEW mail in their IN basket. The message will list all PAI records that were transmitted to Austin. A "Q"uery at this message will provide the MailMan transmission status of the message and the message number.

A confirmation MailMan message is sent from Austin to the designated mail group when the data has been received. This message will have an ID number which corresponds to the Local ID number of the first message. Each of the mail groups must be set up and populated. The name of the mail group must be the same as the name of the queue in order to receive confirmation messages.

If the transmit flags for all receiving users for the RUG-II domains are turned off at your facility, the following message will be displayed upon entering the option and you will be returned to the menu.

"Transmission is turned OFF for receiving domains in TRANSMISSION ROUTERS file"

Transmission via VADATS

This example shows the MailMan message which is sent to the designated mail group listing all records which were transmitted to Austin.

Subj: RUG-II TRANSMISSION, MESSAGE \# 1 31 Mar 89 08:33 6 Lines

From: POSTMASTER (Sender: ADTEMPLOYEE,ONE (TROY VAMC)) in 'IN' basket.\*\*NEW\*\*

-------------------------------------------------------------------------

924723847M19010702872062387500I11111111111 011111 1111 242211111010251010

2344312000000000000001200

993885774M19200710871063087500I11111122111 011112 1111 111111111101010101

1111100000000000000010000

992883775M19130723871071187500I11111111121 111211 1112 112111110101211111

1111100000000000000010000

Select MESSAGE Action: IGNORE (in IN basket)//

This example shows the MailMan message which is sent to the appropriate mail group when the transmission process is complete.

Subj: DP05775 PAF CONFIRMATION 4 APR 89 07:32 CDT 2 Lines

From: \<POSTMASTER@ <span class="mark">redacted</span> \> in 'IN' basket. \*\*NEW\*\*

-----------------------------------------------------------------

Ref: Your PAF message \#3215465 with Austin ID \#26577

MSC confirmation number is 1-25-01-011925.

Select MESSAGE Action: IGNORE (in IN basket)//

Each line of the original transmission represents a PAF Record and may be interpreted as follows.

--------------------------------------------------------------------------------------------------------------------------------------

999999999M19000731872073087500I11221111111 011111 1111233311113535101010

--------------------------------------------------------------------------------------------------------------------------------------

Transmission via VADATS

o Administrative Data constitutes the first 1 to 31 columns.

The first nine digits are the patient social security number.

The next column is for sex - M or F.

The next four digits are for birth year.

The next six digits, columns 15-20, represent the Assessment Date.

Column 21 is for Assessment Purpose: l=ADMISSION/TRANSFER, 2=SEMI-ANNUAL

CENSUS, 3=RESERVED.

Columns 22-27 represent the Date of Admission/Transfer In.

Your medical center/facility code number will be represented by the next three digits.

Column 31 is for Bed Section; I=Intermediate Medicine, N=NHCU.

o Columns 32-44 are for PAI Medical Treatment codes. l=NO, 2=YES. They are, respectively:

TRACHEOSTOMY CARE/SUCTIONING, SUCTIONING-GENERAL, OXYGEN,

RESPIRATORY CARE, TUBE FEEDING, PARENTERAL FEEDING, WOUND CARE,

CHEMOTHERAPY, TRANSFUSIONS, DIALYSIS/ APHORESIS, RADIATION THERAPY,

TUBE FEEDING ROUTE and one reserved field.

o Columns 45-53 are for Medical Events.

Column 45 is the Decubitis Level, assessed from 0 to 5. Next are the Medical Conditions,

columns 46-53: COMATOSE, DEHYDRATION, INTERNAL BLEEDING, STASIS ULCER,

TERMINALLY ILL and three reserved fields. Responses are either l=NO or 2=YES.

o Columns 54-61 are for Selected Diagnoses.

QUADRAPLEGIA, MULTIPLE SCLEROSIS, URINARY TRACT INFECTION and HEMIPLEGIA and four reserved fields. Responses are either l=NO or 2=YES.

o Columns 62-65 reflect the ADLs (Activities of Daily Living).

EATING, MOBILITY, TRANSFER and TOILETING. Assessment of these fields vary.

o Behaviors occupy columns 66-69.

VERBAL DISRUPTION, PHYSICAL AGGRESSION, DISRUPTIVE BEHAVIOR (Infantile or Socially Inappropriate) and HALLUCINATIONS. Assessment of these fields also vary.

o Columns 70-79 account for Special Services.

Rehabilitation Medicine Therapies, levels of therapy and the number of days received.

Assessment of these fields vary.

o Columns 80-99 account for the HOURS/MINUTES PER WEEK of each of the therapies.

o The Chronic Respiratory Support questions occupy columns 100-104.

CHRONIC VENTILATOR DEPENDENT (CVD), TIME SINCE BECOMING CVD, WEANING ATTEMPTS FREQUENCY, PNP\>-20CM AND VC\>15ML, and CAUSE FOR RESPIRATORY FAILURE. Assessment of these fields vary.