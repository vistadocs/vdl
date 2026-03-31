---
title: PIMS Version 5.3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
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
description: Procedural and legislative changes historically have impacted the way Medical Administration Service completes tasks related to hospital operations. For version 5.3, this trend has continued. A number of enhancements, outlined in this overview, relate to needs based on changing VA Policies and Regul
audience: 
keywords: 
  - patient
  - date
  - report
  - appointment
  - edit
  - checkout
  - description
  - specialty
  - treating
  - clinic
page_count: 0
word_count: 18172
section_count: 0
table_count: 33
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1993
revision_count: 1
revision_newest: 11/18/04
revision_oldest: 11/18/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsrn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsrn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

Decentralized Hospital Computer Program

PIMSPATIENT INFORMATIONMANAGEMENT SYSTEM(formerly MAS)release notes

August 1993

Information Systems Center

Albany, New York

Table of Contents

Overview 1

> Checkout 1

> Provider Related Changes 2

> Gains and Losses Sheet 3

> Incomplete Record Tracking (IRT) 5

> Patient Treatment File (PTF) 5

> Means Test 7

> Registration 7

> Beneficiary Travel 8

> Other ADT Enhancements 9

> EDR 10

Beneficiary Travel 13

> Introduction 13

> New Options 13

> Changed Options 14

> Deleted Options 15

> New Routines 16

> Deleted Routines 16

> Suggested Routines for Mapping (DSM) 16

> File (DD) Changes 16

> New Files 17

> New Security Keys 17

> New Mail Groups 17

> New Bulletins 17

> E-Mail Reports 17

> Comments 18

Gains and Losses (G&L) 19

> Introduction 19

> New Options 19

> Changed Options 20

> Deleted Options 23

> New Routines 23

> Deleted Routines 23

> Suggested Routines for Mapping (DSM) 23

> File (DD) Changes 23

> New Files 26

> New Security Keys 26

> New Mail Groups 26

> New Bulletins 26

> E-Mail Reports 27

> Comments 27

Incomplete Records Tracking (IRT) 29

> Introduction 29

> New Options 29

> Changed Options 32

> Deleted Options 37

> New Routines 37

> Deleted Routines 38

> Suggested Routines for Mapping (DSM) 38

> File (DD) Changes 38

> New Files 40

> New Security Keys 40

> New Mail Groups 40

> New Bulletins 40

> E-Mail Reports 41

> Comments 41

Means Test 43

> Introduction 43

> New Options 43

> Changed Options 44

> Deleted Options 44

> New Routines 45

> Deleted Routines 45

> Suggested Routines for Mapping (DSM) 45

> File (DD) Changes 45

> New Files 45

> New Security Keys 46

> New Mail Groups 46

> New Bulletins 46

> E-Mail Notifications 46

> Comments 46

Patient Treatment File (PTF) 47

> Introduction 47

> New Options 49

> Changed Options 57

> Deleted Options 57

> New Routines 57

> Deleted Routines 57

> Suggested Routines for Mapping (DSM) 57

> File (DD) Changes 58

> New Files 59

> New Security Keys 60

> New Mail Groups 60

> New Bulletins 60

> E-Mail Reports 61

> Comments 61

Registration 63

> Introduction 63

> New Options 63

> Changed Options 63

> Deleted Options 68

> New Routines 68

> Deleted Routines 68

> Suggested Routines for Mapping (DSM) 68

> File (DD) Changes 68

> New Files 73

> New Security Keys 73

> New Mail Groups 73

> New Bulletins 73

> E-Mail Reports 73

> Comments 73

Scheduling 75

> Introduction 75

> Checkout Requirement 75

> Scheduling Outputs 75

> Stop Code Update 76

> Checkout 76

> Checkout Options/Actions 77

> Checkout Process 77

> Site Preparation 79

> Inform the Providers 79

> Operational Changes 79

> Parameter Set Up 80

> Disposition Related 80

> Other Site Parameters 81

> Workload Monitoring 82

> Appointment Lists and Routing Slips 83

> Nightly Job 85

> Appointment Management Reports 86

> Provider/DX Reports 86

> Appointment Management 87

> Technical Changes 88

> OPC Format 88

> Outpatient Encounter Data 90

> Other Changes 90

> Clinic Stop Code Update 90

> Patient Profile 91

> New Options/Actions 92

> Changed Options 98

> Deleted Options 106

> New Routines 106

> Deleted Routines 106

> Suggested Routines for Mapping (DSM) 107

> File (DD) Changes 107

> New Files 109

> New Security Keys 115

> New Mail Groups 115

> New Bulletins 115

> E-Mail Notifications 115

> Comments 115

Revision History

Initiated on 11/18/04

|          |                                                                     |                 |                                    |
|----------|---------------------------------------------------------------------|-----------------|------------------------------------|
| Date     | Description (Patch \# if applic.)                                   | Project Manager | Technical Writer                   |
| 11/18/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data |                 | <span class="mark">redacted</span> |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |

Overview

Procedural and legislative changes historically have impacted the way Medical Administration Service completes tasks related to hospital operations. For version 5.3, this trend has continued. A number of enhancements, outlined in this overview, relate to needs based on changing VA Policies and Regulations, as well as user requests for enhancements.

> **NOTE:** There are three routines in the DGI\* namespace which should NOT be deleted after the installation of PIMS v5.3. DGIN, DGINP, and DGINPW are routines that are critical to the normal operation of the software. Programmers should note that these routines are in the process of being phased out. In the next release, the above DGI\* routines will no longer be supported.

DGIN is being replaced by DGPMHST.

DGINP is being replaced by DGRPDD1.

DGINPW is being replaced by DGPMSTAT.

Checkout

The scheduling module has been enhanced to resolve a number of administrative and regulatory data collection needs recently incorporated into the function and duties of Medical Administration Service. Collection of this data is incorporated into the new checkout functionality. For the facility to receive workload credit for encounters that occur on or after 10/1/93, it is required to complete this checkout process.

An outpatient encounter can be an appointment, a disposition, or an add/edit stop code.

New functionality is described below.

1\. The capability is provided to document, for each outpatient encounter, whether the treatment provided was for a service-connected condition. An answer to this question is required in order to receive OPC workload credit. This question will be asked for all service-connected veterans.

2\. For those patients who have (through registration) claimed exposure to Agent Orange, ionizing radiation or environmental contaminants, a provision is provided to document whether the treatment provided was related to Agent Orange, ionizing radiation or environmental contaminants exposure. An answer to this question is required.

3\. During the checkout process for appointments and dispositions, the ability to add/edit stop codes is provided. The user will not have to answer the "associated clinic" and "eligibility" prompts, as the system will automatically determine this information. If the stand-alone option is used, the associated clinic will need to be entered. Ambulatory procedures data will be collected via entry of a "900" stop code in the same manner as in the previous version.

4\. The ability to make follow-up appointments has been included in the checkout process. The user will not need to select the clinic or patient for the return appointment.

5\. Provider information may also be asked during the checkout process, depending on the setting of a site-specific parameter.

6\. The ability to collect data related to diagnoses for clinical and billing applications is available. Like provider information, diagnosis capture is optional. (At this time, the provider and diagnosis questions are not mandated by Central Office.)

7\. The Appointment Management option has had many new actions added, such as the ability to discharge a patient from a clinic. The scheduling release notes have detailed information on all the new and changed actions.

Provider Related Changes

1\. All places in PIMS where provider is currently prompted will now be prompted for both the Primary Care (Resident) and Attending Physicians.

2\. At the request of several users, sites are able to historically track providers due to the use of a new option that will allow entry of a different provider along with storage of the date and time the change was entered. Entry of this information will facilitate tracking of provider activity.

Gains and Losses Sheet

1\. For some time, the users/sites have been requesting a variation in the way the current Bed Status Report works. Users have requested a Treating Specialty G&L. One benefit with this new variation is the proper crediting of workload regarding "boarders", as the credit is to the treating specialty as opposed to a ward location. This will benefit hospital management, clinicians, utilization review, and billing personnel in tracking treating specialty movement activity along with aggregate statistics.

The Treating Specialty Report (TSR) is a statistical report appended to the traditional G&L. It will reflect inpatient activity by the actual treating specialty assigned to each patient movement. As the Bed Status Report (BSR) reflects the bed usage regardless of the treating specialty, the Treating Specialty Report captures the patients actual treating specialty regardless of the physical location.

Input requirements for proper functioning of the TSR include site-specific information that is also date-sensitive. The application manager/MAS ADPAC must enter or edit the number of patients remaining and patients on absences (PASS, AA, UA, ASIH) as of 9/30/92 to initialize the Treating Specialty Report (TSR), similarly to the way the wards are defined for the Bed Status Report (BSR). The initialization date also needs to be defined through the ADT System Definition menu.

There is a new option, Treating Specialty Inpatient Information, that will facilitate validation of the patients treating specialty. The ADPAC, Statistical Clerk, or the Medical Information Supervisor designee should run this option validating the information prior to attempting to initialize and/or generate the Treating Specialty Report (TSR). The Treating Specialty Report requires that you enter specific information for each treating specialty as of midnight on 9/30/92. This option provides the information to properly initialize the Treating Specialty Report. When the information has been validated, it should be entered through the Treating Specialty Set-up option. It is essential that the correct values be entered in order to print the correct FYTD information on the current Treating Specialty Report.

The following is a guide of suggested v5.3 pre-installation procedures for the MAS ADPAC, Statistical Clerk, or Medical Information Supervisor designee needed for the G&L Treating Specialty Report.

> A. Print out the following for 9/30/92.

> 1\. Treating Specialty Inpatient Information Reports

> Patient Listing by Ward

> Patient Listing by Treating Specialty

> Patient Counts by Treating Specialty

> 2\. G&L Bed Status Report

> 3\. Historical Inpatient Listing

> 4\. Absence List

> B. Compare the total number of patients remaining on PASS, AA, UA, and ASIH on the Bed Status Report with the totals on the Historical Inpatient Listing and the Absence List. If the Bed Status Report totals do not match the totals on the Historical Inpatient Listing and the Absence List, validate the information.

> Recalc the G&L.

> Reprint BSR.

> Redo Step B.

> C. Compare the Patient Listing by Ward with the Historical Inpatient Listing. Validate the Patient Listing by Ward patients, PASS, AA, UA, ASIH with the Historical Inpatient Listing and the Absence List.

> D. Validate the Patient Listing by Ward and the Patient Listing by Treating Specialty. Review for any patients with inappropriate treating specialty for their ward location. If there were any inappropriate individual treating specialties for patients, correct them.

> Reprint all Treating Specialty Inpatient Information Reports for 9/30/92.

> Redo Step C.

> E. Validate the Patient Counts by Treating Specialty with the totals on the Patient Listing by Treating Specialty for the patients remaining on PASS, AA, UA, and ASIH.

> F. Keep the Patient Counts by Treating Specialty to aid in initializing the Treating Specialty Report through the v5.3 Treating Specialty Set-up option under the ADT System Definition menu.

2\. A bulletin has been added that is sent to a user or a mail group when the Gains & Losses report auto recalculation job starts and finishes. This will allow the MAS ADPAC or IRM staff member to determine if the recalculation job finished should there be any discrepancies on the Bed Status Report.

Incomplete Record Tracking (IRT)

A number of enhancements were requested by the staff in Medical Record departments throughout the country. All user input has been extremely helpful to the developers and has improved the IRT module significantly. The enhancements are as follows.

1\. The ability to track all deficiencies in an incomplete record. The items were taken from VA Form 10‑2493, Record Review Checklist.

2\. All IRT records will require association with a hospital division. The module tracks responsible physician through completion of the record, as with existing deficiencies in the present version.

3\. Greater flexibility in regard to the print options in IRT has been provided. Examples include the ability to sort by event date, then physician, then type of report, then status, etc. A type of report that will involve short forms (discharges for admission of less than 48 hours) and any other reports that do not have to be dictated or transcribed is provided.

4\. Record Tracking capabilities have been added to the IRT module. The initial screen displays the Current Borrower for the records involved. Current Borrower information is included on the printouts. This will provide information to physicians and other involved personnel as to the location of the records in question.

5\. The ability to add or change Providers in order to more effectively track them will be available in both the IRT and Bed Control modules.

Patient Treatment File (PTF)

A number of enhancements to the PTF module have been incorporated in this version. These enhancements are related to both legislative changes and improvements in functionality and data storage. The enhancements are as follows.

1\. Improvement of the consistency edits in PTF have been accomplished by including all Austin Automation Center (AAC) PTF field edit checks in the module. The current AAC PTF field checks are defined in the <u>Processing Logic Specifications</u>, version 4.3, authored by the AAC. These edit checks are performed immediately after successful completion of the current PTF edit checks during the close out step (when the user tries to close the record). The actual record that is transmitted to the AAC is created at this point. The additional checks will analyze the record actually being transmitted so that the number of records rejected by the AAC will be minimized. In addition, the List Manager has been utilized to provide a list of errors discovered during the Austin edit process. An output that resembles the EAL (Error Analysis Listing) provided to the field by the AAC may be generated by PTF users in order to list all errors encountered. An enhancement to this output is the description of each error along with the associated error code. With these enhancements, the coder can thoroughly diagnose any problems with the record in question, correct any errors encountered, and continue with the Load/Edit process without leaving the Load/Edit PTF Data option. The new field edit checks have been included in the Validity Check of PTF Record option which is found in the Utilities menu.

2\. One enhancement related to legislative changes is the ability to document whether any bed section movement \<501\> screen is related to Agent Orange, ionizing radiation, or environmental contaminants. If any movement has been designated as related to AO/IR/EC, then the record and its associated treatment(s) will be considered related to AO/IR/EC. The questions and responses on the \<501\> screens are transmitted to Austin in both the \<501\> and the \<701\> record.

3\. Another addition to the functionality of the \<501\> screen in terms of suicide indicator relates to identification of whether the patient had a self-inflicted wound (intentional self-injury) versus a suicide attempt. This code is entered when the system prompts for a suicide indicator on the \<501\> screen.

4\. A major PTF enhancement in version 5.3 is the functionality associated with the ability to archive and purge PTF records. This process involves four distinct steps. The first step entails generating a list of all PTF records designated for archiving and purging for the selected date range. The second step involves review of the generated list. The option responsible for the review step will provide a report of records that should be omitted from the archiving/purging process. An option used to untag or deselect individual records will also be included at this point. Records that may have potential problems during the archiving/purging process will be identified here. The third step involves the actual archiving of the PTF record(s). The fourth and last step involves the actual purging of records. All records identified will be purged. Records that were not first successfully archived cannot be purged.

Means Test

1\. Collection of Means Test data is now mandatory for those NSC veterans claiming Agent Orange or ionizing radiation exposure. The user is able to enter this information in the same manner, via Means Test options, as for other NSC veterans. Veterans claiming AO/IR exposure will no longer be exempted from the Means Test.

2\. The Means Test screening will be done in both ADT and Scheduling. This will create new Means Tests, with the status of REQUIRED, on patients whose Means Test is greater than 365 days old.

3\. During both the check in and the checkout process, the Means Test Status will be displayed when using the Appointment Management option.

4\. Four new outputs related to Means Test information are provided in this release. One option will list all those active patients who have stated that they do not agree to pay the Means Test deductible. A patient is defined as being active if he or she has had any patient activity (in terms of dispositions, clinic appointments, scheduled admissions, or inpatient movements) within a user-specified date parameter. A second output produces a listing of patients that either presently require a Means Test or will require a Means Test at their next appointment. A third output will generate a listing of patients that have had a Means Test entered in a current year, but were categorized with the prior year's MT thresholds. This would occur if the new MT thresholds for the current year were not available. The fourth output will produce a listing of review dates of patients who have been designated as hardship cases.

Registration

1\. Users have requested the ability to enter and edit data to the Rated Incompetent? field. This has been provided via a prompt within the Load/Edit Patient Data option. It is located on Screen \#7 of the option display. Previously, this was accomplished through use of an option in the AMIE package.

2\. A single entry for Aid & Attendance/Housebound/VA Pension/VA Disability income amounts will replace present ones in the current version.

3\. The prompt for requesting medical records via the Record Tracking package during use of the Register a Patient option is available in the beginning of the Registration process.

4\. Data entered into the Claim Folder location field on Screen \#7 of the Load/Edit Patient Data option conforms to a specific format in order to interface properly with the AMIE package. It is no longer a free text entry.

5\. With this release, new consistency edits for SSN boundaries have been added. This will ensure that social security numbers outside the valid ranges (as specified by the Social Security Administration) will be rejected.

6\. Additional questions concerning Persian Gulf Theater service have been included in the Registration process. Some of the questions will include dates of service, whether or not the veteran is claiming exposure to environmental contaminants, and if so, the date they registered and their date of exam for that exposure.

7\. The ability to print a Health Summary report, Outpatient Drug Profile, or Pharmacy Action Profile along with the VA Form 10‑10 will be provided. A site parameter will allow the facility to make this enhancement available, if desired. This will provide the emergency care physician the ability to review current medications, past admissions, clinic visits, ancillary test results, etc.

Beneficiary Travel

1\. The Distance Enter/Edit option and associated entries has been modified in order to provide the ability to have multiple entries for departure and destination locations. This is in response to user requests that different distances be allowed from a single departure point to divisions or satellite clinics in different locations. This will provide a major improvement in the way the Beneficiary Travel module works for those facilities who are multidivisional.

2\. The Claim Enter/Edit option has also been modified to accommodate the need to allow different distances from the departure point to multiple divisions or satellite clinics as mentioned above.

3\. The current "Additional Information" prompt, which requires a YES/NO response, has been replaced with an "Additional Information/Remarks" prompt that is free text in nature. This enables BT Supervisors to enter remarks for those cases where claim departure locations are outside the facility's treatment area.

4\. Mileage for claim entries will check the zip code in the BENEFICIARY TRAVEL Distance file first, then the name of a city or town. This accommodates specific departure areas within a city or town. It will help facilitate the resolution of abbreviated, inconsistently spelled, and identically named cities or towns in different states.

Other ADT Enhancements

1\. Users are able to add attending and primary physicians during use of the Discharge a Patient option. The ability to enter these physicians will also work in conjunction with the Incomplete Records Tracking (IRT) module.

2\. Event Driven Reporting v1.5 was recently released in the EDR namespace. This software will now become part of PIMS v5.3 in the VAFED namespace. Along with the old functionality in EDR v1.5, there will be added functionality to capture outpatient events. A protocol is placed on the PIMS outpatient event driver which will collect all outpatient events. This information will then be bundled into an HL7 message and sent to the central system.

All the ZIP CODE fields in the Patient file will have an associated ZIP+4 field. These fields will accept either 5 or 9-digit numeric. The current 5-digit field will remain intact for those ancillary packages currently editing these fields (Pharmacy, Fee Basis, AMIE, HINQ, PDX, Social Work Service, Integrated Billing, and any site specific \[local\] modification templates that may exist). This will allow for the continued use of any input and output templates that utilize the zip code fields currently in the Patient File.

The computer-generated VAF 10-10, Application for Medical Benefits, will be modified to include the printing of the new ZIP+4 fields.

All registration screens and the Patient Inquiry Screen will be updated to allow viewing of the ZIP+4 entries.

All scheduling letters will be modified to print the new ZIP+4 fields for mail-out purposes.

When users of those ancillary packages, enter/edit the current 5-digit zip code fields, the corresponding ZIP+4 fields will be automatically updated to equal the 5-digit fields. Non-PIMS users, however, will not be able to enter/edit the last four digits of the 9-digit zip code field or be able to view it within their respective package menu options until such time as their software is modified. If a PIMS user enters a 9-digit zip code into the Patient file through Registration, it will remain intact UNLESS a non-PIMS user modifies the first five digits of the zip code through an ancillary package. In this case, the last four digits that were originally entered by the PIMS user will be erased and the correct/new 5-digit code will appear.

Six months from the mandated install date of the PIMS v5.3 (10/1/93), a second patch (approximately 3/1/94) will institute a mandated use of the new ZIP+4 fields. This will give everyone time to review and edit all input and output templates that may exist.

We felt that taking this phased-in project approach would give the medical centers ample time to adopt procedures for populating the new ZIP+4 fields, as well as not placing any mandates or deadlines on Medical Administration Service to have their current patient data base in compliance. We have spoken to the FIRMAC about this approach. It was agreed that by giving the sites a head start for populating the fields, giving them six months to modify any existing local templates or routines that utilize the current 5-digit fields, and giving the ancillary DHCP packages six

months to convert to the new format for future releases, would be beneficial to all.

Event Driven Reporting (EDR)

EDR relies on the MAS Movement Event Driver and the MAS Appointment Event Driver software to determine when an admission, discharge, transfer movement (or cancellation of one of these movements) or outpatient event occurs. This is the same software that Order Entry/Results Reporting and other DHCP packages use to determine when inpatient movement events occur. For the release of PTF records, EDR relies on a cross-reference in the PTF Release file.

When one of the events occurs, the EDR software is invoked. The EDR software captures the event data and stores it in the PIMS EDR Event file (#391.51). Once every twenty-four hours, a background EDR process (VAFED EDR process events) that is scheduled to run daily is invoked. This process interfaces with the DHCP Health Level Seven (HL7) package to convert the event data in the PIMS EDR Event file into a series of HL7 messages using the HL7 protocol. These HL7 messages are then loaded into one or more MailMan messages and sent to the appropriate addressee at the central system.

The following data related to each inpatient movement is captured.

Patient Name

Patient ID

Patient Date of Birth

Event Date/Time

Patient Class (Inpatient)

Patient Location (Ward-Room-Bed)

Attending Physician (Name and ID)

Treating Specialty

Unique Visit Number

Ward Service

Admission Date/Time

Source of Admission (Only applicable to admission movement)

Servicing Facility

At the time a PTF record is released, the preceding data is captured, along with the following additional data.

Type of PTF Record (Census or PTF)

Type of Discharge

Place of Discharge

Diagnosis Coding Method (ICD9)

Type of Diagnosis (Final)

Discharge Diagnoses

The following data related to each outpatient movement is captured.

Event Date

Facility Number

Clinic Stop Code

Provider

Diagnosis

CPT Codes

Patient ID (internal and external)

Patient Name

Patient Date of Birth

Patient SSN

Each event (admission, discharge, transfer, PTF release, outpatient) results in the capture and transmission (through MailMan) of approximately 350 characters of data on average. The data is captured and stored in the PIMS EDR Event file at the local site for approximately 24 hours. Once the data is transmitted, it is auto-matically purged from the PIMS EDR Event file. The number of inpatient events at a local site (and therefore the amount of data captured and transmitted) will be small. The amount of outpatient information captured will be moderate. The mail messages that are built may be purged approximately twenty-four hours after they are sent (once acknowledgment messages are received). Therefore, additional disk space consumed should be minimal.

The impact on CPU cycles when the data is captured and stored in the PIMS EDR Event file should be small but significant. The impact on CPU cycles will be more significant when the data is converted to HL7 messages, compiled into MailMan messages, and transmitted. Since this process is accomplished by a background task, the task may be scheduled to run when it will have the least impact.

For further information concerning EDR and the data that it transmits, see the

PIMS v5.3 Technical Manual, appendices B, C, D.

Beneficiary Travel

Introduction

This release of the Beneficiary Travel software has a significant change in the handling of the distance mileage between the patient's departure city and the medical division at which s/he is being seen. The BENEFICIARY TRAVEL distance file (#392.1) now allows the storing of a separate mileage value for each division by departure city. In addition, each division will have an associated most economical cost and remark field. This remark field contains free text information that will be displayed during the Claim Enter/Edit, prior to the mileage prompt. This field is only editable from within the Distance Enter/Edit option and displayed only in the Claim Enter/Edit option. This field will be specific to that departure city and division.

An incomplete data checker has also been added to the BENEFICIARY TRAVEL Distance file. Whenever the Distance Enter/Edit option is used, a message will be displayed for any missing state and zip code values, or any incomplete remarks fields (Additional Information field (#4) set true, and RemarkS field (#5) set to null). The user will then be asked if they want to fix any of the problems found.

Another change is the use of the zip code in the patient file (#2) in a first attempt to match the departure city in the BENEFICIARY TRAVEL Distance file. The software looks first for a city with a zip code that matches the first five digits of the patient's zip code. If found, a search will be made for the appropriate division and mileage. If a match on the zip cannot be made, then a match on the city's name will be made as before.

A new report option has been added. This report displays information for the reimbursable accounts (ALL OTHER and C&P EXAMS) only. This report displays in patient and claim date order, the patient's name, patient ID, claim date, the mileage amount payable, the deductibles, and the net payment. Costs are subtotaled and totaled by account type.

A. New Options

None

B. Changed Options

NAME: DGBT BENE TRAVEL REPORT

MENU TEXT: Report of Claim Amounts

DESCRIPTION: A new report option has been added for the Payable Claim's Statistics. This report will print the payments, deductibles, and subtotals and totals for the ALL OTHER and C&P claims by division, showing the patient's name, patient ID, and claim date, and any remarks entered in the BENEFI-CIARY TRAVEL claim file (#392). It is selectable by date range. If no data is found within the date range specified, the report header will be printed, and totals of zero will be printed along with a footnote stating that if zeros were printed, no data was found in the specified date range.

NAME: DGBT BENE TRAVEL DISTANCES

MENU TEXT: Distance Enter/Edit

DESCRIPTION: This option has been totally revamped, now permitting multiple division mileages for each departure city. When this option is entered, it first checks for any missing data in the BENEFICIARY TRAVEL Distance file. If no problems are found, a message stating no problems were found will be displayed, and you will be asked to enter a departure city for edit or entry. If any cities are missing their state field, you will be asked to enter the state directly. If they are missing their zip code field, the default mileage field is zero, or their Additional Information field is set to TRUE but the corresponding remarkS field is blank, a message will be displayed indicating problems were found and asking if you want to fix them. If you choose to fix them, you will be presented with an option to run a report for each problem showing the cities with incomplete data. If you run a report for which no problems were identified, nothing will be printed except a note stating that no data was found for that problem. After each report has been run, you will be asked which cities to fix. If there are no problems to fix, answer NO. If you choose not to fix any of the problems at this time, you will be asked for a departure city to edit or enter. See section M for additional information.

> When creating a new distance entry, the software will set the default division name to the primary MEDICAL CENTER NAME (Field \#12 of the MAS parameterS file). You will have the option of overriding this division in multidivisional centers. Non-multidivisional centers will have this division set for them. The mileage value entered for this division will be used as the default mileage for the departure city medical center if the software cannot match a division to the city during the Claim Enter/Edit. If the departure city of the patient is not in the BENEFICIARY TRAVEL distance file, you will have to enter the mileage value during the Claim Enter/Edit option.

There is now an additional information remarks field associated with each departure city-division entry. This field can only be edited in the Distance Enter/Edit option, and is displayed in the Claim Enter/Edit option. This allows the entry and display of whatever information or notes the DGBT Supervisor feels is necessary to present to the clerks doing the claim entries.

NAME: DGBT BENE TRAVEL SCREEN

MENU TEXT: Claim Enter/Edit

DESCRIPTION: Several changes to the prompts have been made to this option in order to bring the coding up to standards. From the user's perspective, the keyboard default responses have not changed. One change at the claim date/time selection is that instead of entering a "?" to display past claim dates, this version requires that you enter a "P" for past claims. The BT Claim Information \<Screen 1\> still accepts a RETURN as the default acceptance, but now a NO must be entered to quit instead of a QUIT.

In the Beneficiary Travel Claim Information \<Enter/Edit\> Screen, between the ATTENDANT/PAYEE and MILEAGE prompts, a message "Please wait, Checking mileage..." will appear and if any remarks have been entered in the remarks field of the BENEFICIARY TRAVEL Distance file for this division, they will be displayed as MILEAGE REMARKS: {remarks}. In addition, the ONE WAY/ROUND TRIP and MILEAGE/ONE WAY fields have been reversed so the MILEAGE/ONE WAY field is displayed first. If the departure city is in the BENEFICIARY TRAVEL Distance file, but the division is not, the default mileage for the city will be used and the MILEAGE REMARKS display will contain the message "DEFAULT MILEAGE USED" to alert the clerk.

C. Deleted Options

None

D. New Routines

DGBTDIST Beneficiary Travel Departure City Distance Enter/Edit

DGBTDST1 Beneficiary Travel Departure City Distance Enter/Edit, Cont.

DGBTE1A Beneficiary Travel Find Old Claims Part 2

DGBTEE2 Beneficiary Travel Enter/Edit, Cont.

DGBTEF1 Beneficiary Travel Update Parameters into Files

DGBTOA5 Beneficiary Travel Outputs Front End/Statistics

DGBTSRCH Search Routine for Incomplete Data

DGBTUTL Beneficiary Travel Utility Routines

E. Deleted Routines

None

F. Suggested Routines for Mapping (DSM)

None

G. File (DD) Changes

Beneficiary Travel Distance (#392.1)

Field 5 \*ADDITIONAL INFORMATION

This field is no longer supported and will be deleted at a future date. The information contained in this field has been transferred to Field 4 of the DIVISION MILEAGE multiple (#100) during the installation of PIMS v5.3.

Field 6 \*MOST ECON/PUBLIC TRANS. COST

This field is no longer supported and will be deleted at a future date. The information contained in this field has been transferred to Field 3 of the DIVISION MILEAGE multiple (#100) during the installation of PIMS v5.3.

Field 100 (Multiple) DIVISION MILEAGE

This is a new multiple for the BENEFICIARY TRAVEL distance file.

> Field .01 DIVISION NAME

> Field 2 MILEAGE ONE WAY

> Field 3 MOST ECONOMICAL COST

> Field 4 ADDITIONAL INFORMATION

> A YES or NO coded field checked to see if remarks (field \#5) exists.

> Field 5 REMARKS

> Free text field for remarks pertaining to this particular division.

H. New Files

None

I. New Security Keys

None

J. New Mail Groups

None

K. New Bulletins

None

L. E-Mail Reports

None

M. Comments

In the Distance Enter/Edit option, the suboption to correct problems will only be present when either a zip code, remarks field, or default mileage is missing. If none of these problems were found, you will be notified that no problems were found and then prompted for a departure city. The suboption offers a choice of which of the three problems to correct. When you select one, you will be asked if you want a report printed. NOTE: These reports are VA FileMan templates. If you select a report for which no problems were reported, you will not receive any report output, but will then be asked which city to update for the respective data. You will only receive report output when there is an actual problem, and therefore should not select a suboption for a problem unless it was identified when entering the Distance Enter/Edit option.

The prompt for updating missing data will only update the specific piece of data in question. It will not allow you to do corrections or updates to the distance data in general.

The ZIP+4 field will be printed, if present, in the address blocks of the VA Form 70-3542d. Additionally, the Zip+4 can also be entered into the BENEFICIARY TRAVEL CLAIM file during the Claim Enter/Edit option. This WILL NOT update the zip code in the patient file, only the zip code in the BENEFICIARY TRAVEL claim file.

VA Form 70-3542d has had four blank lines removed so it will now print on a laser printer without wrapping the last four lines to the next page. The content and layout of the form remain unchanged.

Gains and Losses (G&L)

Introduction

The term G&L is used to broadly cover the daily Gains and Losses Sheet and the statistical report related to patient movements in the medical centers. The statistical report of bed usage by patients, which is known as the Bed Status Report is not new. However, a new statistical report on the inpatient activity by treating specialty, the Treating Specialty Report (TRS) is being released in this version.

A. New Options

NAME: DGPM TS INPATIENT INFORMATION

MENU TEXT: Treating Specialty Inpatient Information

DESCRIPTION: The ADPAC, Statistical Clerk, or the Medical Information Supervisor designee should run this option. This option will print out lists with treating specialty inpatient information for a specific date. Three separate and different printouts can be generated. Patient Listing by Ward and the Patient Listing by Treating Specialty print the individual patient information, as well as the subcounts and totals. The Patient Listing by Wards is comparable in display format to the Historical Inpatient Listing. The Patient Count by Treating Specialty does not print out the individual patient information, but does print out the subcounts and totals for each facility treating specialty by division. To appropriately initialize the Treating Specialty Report, the data from the Patient Count by Treating Specialty for the date of 9/30/92 will need to be entered in the v5.3 Treating Specialty Set-up option. The utilization of this option for the date of 9/30/92 will provide the means to check the data necessary to initialize the current fiscal year's (FY93) statistics. It is essential that the correct values be entered, in order to print the correct FY to date information on the current Treating Specialty Report.

B. Changed Options

NAME: DG BULLETIN LOCAL

MENU TEXT: Bulletin Selection

DESCRIPTION: This option is located under the ADT System Definition menu. A new prompt, AUTO RECALC GROUP, has been added to this option. The option is used to specify the mail group to which you desire specific types of notification to be made. To provide notification whenever the G&L auto recalc starts and finishes, this prompt should be answered with the appropriate selection of a mail group. If no mail group is selected, no notification will be made.

NAME: DG G&L CHANGES VIEW

MENU TEXT: View G&L Corrections

DESCRIPTION: This option is located under the Supervisor ADT menu. The option is used to view changes in inpatient activity which were made to patients' admission records. This option now includes changes related to facility treating specialty transfers (e.g., FACILITY TS ENTERED, FACILITY TS DELETED, FACILITY TS DATE EDITED).

NAME: DG G&L INIT

MENU TEXT: Gains and Losses Initialization

DESCRIPTION: This option is located under the Supervisor ADT menu. The earliest date allowed to be entered for the G&L Initialization Date has been edited to be no earlier than 10/1/90. The help text for this option has also been modified to reflect this change.

NAME: DG G&L RECALC

MENU TEXT: Recalculate G&L Cumulative Totals

DESCRIPTION: This option is located under the Supervisor ADT menu. This option is used to update the cumulative totals after past patient movements have been recorded. The user specifies the date to correct from but the date selected cannot be before the date defined in the parameter, EARLIEST DATE FOR G&L. The prompt for recalculating patient days has been removed and will no longer be asked. The screen has been changed to display the Earliest Date for Treating Specialty Report. This will be displayed after the Earliest Date for G&L and before the Earliest Date to Recalculate.

NAME: DG G&L RECALCULATION AUTO

MENU TEXT: Auto-recalculation of G&L Statistics

DESCRIPTION: This queued option should run nightly as a background job. The bed status statistics and now the treating specialty statistics require this action to have accurate daily Bed Status and Treating Specialty Reports. This option uses the G&L Corrections file (#43.5) to determine what the oldest date for correction is and goes back to that date, updating the census data from that date to the current date.

NAME: DG G&L SHEET

MENU TEXT: Gains and Losses (G&L) Sheet

DESCRIPTION: This option is located under the ADT Outputs menu. The Gains and Losses (G&L) Sheet option is used to generate the daily Gains and Losses Sheet, the Bed Status Report, and now the Treating Specialty Report for your medical center.

The Treating Specialty Report is a separate statistical report; however, it is part of the overall G&L. The Treating Specialty Report (TSR) is new in v5.3. The Bed Status Report (BSR) is a statistical report of the patients' physical location regardless of the treating specialty. The Treating Specialty Report (TSR) is a report of inpatient activity by treating specialty and captures statistical data by actual treating specialty assigned to each patient movement regardless of the physical location.

The format of the Treating Specialty Report (TSR) is similar to the Bed Status Report (BSR) although the fields/columns relating to beds (e.g., Vacant Beds, Beds OOS, Operating Beds, Over Capacity Beds, Authorized Beds, Cumulative Occupancy Rate) are not present.

The screen you see when entering this option has changed. It now displays as follows.

\<\<\<GAINS & LOSSES SHEET/BED STATUS REPORT/TREATING SPECIALTY REPORT\>\>\>

The screen also has been edited to display the Earliest Date for Treating Specialty Report. This will be after the Earliest Date for G&L, and before the Earliest Date to Recalculate. If the parameter for the Treating Specialty Report Initialization Date (TSR INITIALIZATION DATE) has not been entered, UNKNOWN will be displayed instead of the date and no additional prompts asked in this option. If the parameter TSR INITIALIZATION DATE has been entered in the G&L Parameter Edit option, that date will be displayed. A new prompt will be asked (PRINT TREATING SPECIALTY REPORT?) after asking PRINT BED STATUS REPORT. It will display the LAST TREATING SPECIALTY REPORT TOTALS EXIST for a given date. It now says "Recalculate BSR/TSR totals?" instead of "Recalculate bed status totals?".

NAME: DG PARAMETER EDIT

MENU TEXT: MAS Parameter Enter/Edit

DESCRIPTION: This option is located under the ADT System Definition menu.

Under the division selection, the prompt NHCU/DOMM/HOSP G&L was changed to NHCU/DOM/HOSP G&L.

NAME: DG TREATING SETUP

MENU TEXT: Treating Specialty Set-up

DESCRIPTION: This option is located under the ADT System Definition menu. Several new prompts were added to this option. This option is used to define treating specialties for your medical center. The new prompts are necessary for the Treating Specialty Report (printed with/without the Gains and Losses Sheet and/or the Bed Status Report). This option will now ask for the medical center division (if multidivisional) and then the patients remaining and patients on absences (PASS, AA, UA, ASIH) as of 9/30/92. This additional information is needed to initialize the Treating Specialty Report, similar to the way the Ward Definition Entry/Edit option does this for the Bed Status Report.

NAME: DGPM G&L PARAMETER EDIT

MENU TEXT: G&L Parameter Edit

DESCRIPTION: This option is located under the ADT System Definition menu and locked with the DG SUPERVISOR key. A new prompt, TSR INITIALIZA-TION DATE, has been added. At this prompt, enter the date on which you wish to initialize your Treating Specialty Report. The date selected must be on or after Oct 1, 1992. The Treating Specialty Report census statistics will be calculated from this date. It is recommended that it be the beginning of the fiscal year to have appropriate statistics for fiscal year to date.

C. Deleted Options

None

D. New Routines

DGPMBSAB Auto Recalc Routine

DGPMTS Treating Specialty Inpatient Print

DGPMTSI Treating Specialty Inpatient Info

DGPMTSI1 Treating Specialty Inpatient Set

DGPMTSI2 Treating Specialty Inpatient Set

DGPMTSO Treating Specialty Inpatient Listing Output

DGPMTSO1 Treating Specialty Inpatient Listing by Ward

DGPMTSO2 Treating Specialty Inpatient Listing by TS

DGPMTSO3 Treating Specialty Inpatient Counts by TS

DGPMTSR Treating Specialty Report Print

DGPMTSR1 Treating Specialty Report Variables

DGPMTSR2 Treating Specialty Report Set

E. Deleted Routines

None

F. Suggested Routines for Mapping (DSM)

None

G. File (DD) Changes

MEDICAL CENTER DIVISION (#40.8)

> Field 6 NHCU/DOM/HOSP G&L

> The name of this field was edited from NHCU/DOMM/G&L. It is displayed in the MAS Parameter Entry/Edit option under the division section.

> Field 50 TREATING SPECIALTY (multiple)

> Field .03 BEGINNING TSR PATIENTS (new)

> This subfield contains the number of patients for the treating specialty on the Treating Specialty Report Initialization Date. This prompt is asked in the Treating Specialty Set-up option.

> Field .04 TSR ORDER (new)

> This subfield contains the order in which the treating specialties will print on the Treating Specialty Report. This prompt is asked in the Treating Specialty Set-up option.

> Field 10 CENSUS DATE (multiple)

> Field .03 PATIENT DAYS OF CARE \[CUM\]

> This subfield name was edited from PATIENT DATE OF CARE.

MAS PARAMETERS (#43)

> Field 10 EARLIEST DATE FOR G&L

> This field has been edited to allow the entry to be no earlier than October 1, 1990.

> Field 57 AUTO RECALC LAST STARTED

> The name of this field was edited from AUTO RECALC LAST RUN. It was changed to be more clear as to its purpose. This field is set during auto recalculation and used by the AUTO RECALC START/FINISH bulletin.

> Field 59 AUTO RECALC FINISHED (new)

> This field is set during the auto recalculation and used by the AUTO RECALC START/FINISH bulletin.

> Field 511 AUTO RECALC GROUP (new)

> This field is used in the Bulletin Selection option of the ADT System menu.

> Field 1000.01 G&L INITIALIZATION DATE

> This field contains the date on which you wish to initialize your Gains & Losses Sheet and Bed Status Report. The date selected must be on of after October 1, 1990. Bed Status statistics will be calculated from this date.

> Field 1000.05 \*TWO/THREE COLUMN DISPLAY (\* for deletion)

> This field is \* for deletion 18 months from version 5.3 since it has no current use nor has ever been used.

> Field 1000.07 RECALCULATE FROM

> This field contains the earliest date for which recalculation can be run. The input transform was edited for this field to prevent a date earlier than the G&L INITIALIZATION DATE (which was also edited to be not earlier than 10/1/90).

> Field 1000.11 TSR INITIALIZATION DATE (new)

> This field is entered through the G&L Parameter Edit option under the ADT System Definition menu and locked with the DG SUPERVISOR key. This field should contain the date on which to initialize the Treating Specialty Report. The date selected must be on or after October 1, 1992. The Treating Special Report census statistics will be calculated from this date. It is recommended that this date be the beginning of the fiscal year to have accurate fiscal year to date statistics.

G&L CORRECTIONS (#43.5)

> Field .02 TYPE OF CHANGE

> This field definition was changed from a set of codes to a pointer to a newly created file, G&L TYPE OF CHANGE (#43.61). This was necessary due to the additional entries needed for facility treating specialty type of changes.

PATIENT MOVEMENT (#405)

> Field .01 DATE/TIME

> Cross-reference: AGL1

> This MUMPS cross-reference was edited to respond to the facility treating specialty changes as it does for admissions, discharges and transfers. It utilizes the G&L Corrections routine (DGPMGLC) and creates entries in the G&L Corrections file (#43.5) as appropriate.

> Field .09 FACILITY TREATING SPECIALTY

> Cross-reference: AGL9 (new)

> This MUMPS cross-reference was added to trigger the G&L Corrections routine (DGPMGLC) to create an entry in the G&L Corrections file (#43.5). This is needed to set the recalc date for the Treating Specialty Report accuracy. If there is a facility treating specialty change (NOT just a provider change), the appropriate entry will be set in the G&L Corrections file (#43.5).

H. New Files

G&L TYPE OF CHANGE (#43.61)

> Field .01 NAME

> This file consists of a table of G&L type of changes. Previously, this was a set of codes in the G&L Corrections file (#43.5). The data in this file is distri-buted with the PIMS package and must NOT be altered in any way. There are currently 15 entries in this file (13-15 were not present in v5.2). The entries are as follows.

> 1 ADMISSION ENTERED

> 2 ADMISSION DELETED

> 3 ADMISSION DATE EDITED

> 4 TRANSFER ENTERED

> 5 TRANSFER DELETED

> 6 TRANSFER DATE EDITED

> 7 DISCHARGE ENTERED

> 8 DISCHARGE DELETED

> 9 DISCHARGE DATE EDITED

> 10 ADMISSION WARD EDITED

> 11 MOVEMENT TYPE EDITED

> 12 TRANSFER WARD EDITED

> 13 FACILITY TS ENTERED (new)

> 14 FACILITY TS DELETED (new)

> 15 FACILITY TS DATE EDITED (new)

I. New Security Keys

None

J. New Mail Groups

None

K. New Bulletins

AUTO RECALC START/FINISH

This bulletin will be generated if the AUTO RECALC GROUP field is appropriately filled in with a mail group name in the Bulletin Selection option under the ADT System Definition menu. It will send the following message to members of the mail group selected.

Date/Time Auto Recalc Started:

Date/Auto Recalc went back to:

Date/Time Auto Recalc Finished:

L. E-Mail Reports

None

M. Comments

Miscellaneous items corrected in v5.3 as a result of NOIS messages, etc.

1\. NOIS Message \#4211565, dated 6/11/92

When a patient is transferred to ASIH, the treating specialty that shows on the G&L did not indicate the ward treating specialty but the NHCU specialty.

2\. NOIS Message \#4414103, dated 12/29/92

The insurance indicator (+) on the G&L did not print if multiple insurances were listed, the last entry had expired, and another entry was active.

3\. NOIS Message \#4417605, dated 1/4/93

Elongated G&L Category Headings

4\. NOIS Message \#4464654, dated 2/26/93

Messages \#4465089, \#4466587, \#4466597

Multiple admissions for same day not showing on G&L, just the last one; but discharges were showing and the BSR statistics recorded properly.

5\. E3R \#1889, date submitted 1/27/93

Have the G&L Sheet show the Third Party Reimbursement Candidate symbol (+) for specialty transfers as is done for the other patient movements.

6\. NOIS Message \#4497994, dated 4/6/93

Cumulative occupancy rate on the primary location section of the Bed Status Report was incorrectly calculated (when there was only one ward location) compared to the cumulative occupancy rate on the main portion of the BSR.

Incomplete Records Tracking (IRT)

Introduction

This release of IRT with PIMS v5.3 will include many enhancements that should allow the users greater flexibility and efficiency when using the IRT package. This module now tracks all types of deficiencies, as well as those already being tracked (Discharge and Interim Summaries and OP Reports). The sites will have the ability to add their own deficiencies they wish to track to make this more site specific. The Physician for Deficiency will be tracked throughout the IRT process. The users will know who is responsible for the deficiency at various stages of the IRT entry through to its completion. The IRT package will now be more efficient and flexible for all sites that use it.

A. New Options

NAME: DGJ PHYS DEFICIENCY REPORT

MENU TEXT: Physician Deficiency Report

DESCRIPTION: This new option produces a list for the physicians of all the deficiencies that are not completed. This list can be sorted by physician, service/

specialty, and patient. It can be run for inpatients only, outpatients only, or both. Division is asked and the user can choose one, many, or all divisions. A beginning and ending date is asked for so that the report can be run for a particular date range. The report can also be run for one type of deficiency, many deficiencies, or all deficiencies that the facility tracks. The report displays the following information: physician, patient ID, admission date, deficiency, event date, status, borrower, phone/room, and date/time charged. The last three data elements have to do with Record Tracking and the present location of the medical record of the patient. These fields were added to the display so that the physicians could access the patient record easily and update their deficiencies in a more timely manner.

There is a prompt that asks the user if they would like to have the deficiencies under the Summary category listed if the patient has not yet been discharged. If the user answers YES to this prompt, those deficiencies will be displayed on the report. If the user answers NO, those deficiencies that are under the Summary category will not be displayed on this report until the patient has been discharged. All deficiencies under the other categories will always be on this report.

NAME: DGJ ADD/EDIT DEFICIENCY

MENU TEXT: Add a New/Edit Deficiency

DESCRIPTION: This option uses the list processor to display all the deficiencies and data elements on the screen in full view. (This option should be utilized before using the IRT package or the user will not be able to enter any deficiencies.) This option allows the user to update all deficiencies in the IRT TYPE OF DEFICIENCY file (#393.3). Upon entering this option, the user will see all of the deficiencies and data displayed on the screen. Each deficiency will be displayed under the category that it belongs to. The IRT TYPE OF DEFICIENCY file is transported with all the deficiencies that are included on the "Pink Sheet", VA form (10-2493) Record Review Checklist. This is the list of deficiencies you will see on the screen. The data elements that are displayed in this option are Deficiency Name, Track Deficiency, Standard Deficiency, and Category. Those deficiencies that have been highlighted are the ones that come with the file. Only the Deficiency Name and the Category are highlighted and uneditable by the user. The unhighlighted areas will be editable by the user. By running this option, the user will be turning on the deficiencies that their facility will track. When entering an IRT, only those deficiencies that have been turned on by answering YES to the Track Deficiency field will be choices for the user. When answering YES to the field Standard Deficiency?, the user is making that deficiency a standard deficiency for every admission. When the IRT background job is run nightly, IRT entries for each of the standard deficiencies will be created for the previous day's admissions.

At the bottom of the screen, there are three actions that can be taken against the list of deficiencies.

> EN - This allows the user to add a new deficiency to the IRT TYPE OF DEFICIENCY file. Upon entering the action, the user is prompted to enter a deficiency. Once provided, the user is asked for the following information about the deficiency: Abbreviation, Category, Track Deficiency (answering YES to this prompt will allow the facility to track this particular deficiency), and Standard Deficiency (answering YES to this prompt will consider this deficiency a standard one that all admissions will have). When the IRT background job is run, an IRT entry will be created for each standard deficiency for each previous day's admission.

> DE - This allows the user to edit an existing deficiency. If you choose to edit a deficiency that is highlighted (one sent with the IRT Type of Defi-ciency file) you will only be prompted for Tracking Deficiency and Standard Deficiency. If you are editing an unhighlighted deficiency (one that your facility specifically entered), you will have the ability to change the name. It also asks the Abbreviation, Category of the facility, Tracking Deficiency and Standard Deficiency prompts, displaying all the defaults.

> JC - This allows the user to jump to a specific category and edit the data under that category without going through the whole list.

> This option is locked by the DGJ SUPER security key.

NAME: DGJ IRT UPDATE STD. DEFIC.

MENU TEXT: IRT Update Std. Deficiencies

DESCRIPTION: This option gives the user the ability to run the IRT back-ground job for a specific date range. This option, when run, will create IRT entries for the standard deficiencies that have been selected by the site for the admissions that occurred within the date range chosen. This option will check to see if the admissions for the date range have previously been updated by the IRT background job, by checking a field that is set if the job was run previously. If the job for that particular admission has been run previously, duplicate updating will not occur. There is a report created by this option that is sent to a mail group chosen by each facility. This report lists the patients that have had short form discharges (less than 48 hours from admission) within the time frame of when this option was run. The facility should use the Bulletin Selection option under the ADT System Definition menu to set up the mail group which will receive this report. An IRT parameter must also be set up by the facility under the Set up IRT Parameters option before this option can be used. It is the STD. DEFIC. FOR SHORT FORMS? parameter. It is a YES/NO prompt. If the default is set to YES, this option will create standard deficiencies for short form admissions. If the default is set to NO, this option will not create standard deficiencies for the short form admissions. This option is locked by the DGJ SUPER security key.

NAME: DGJ IRT UPDATE (Background)

MENU TEXT: IRT Update Std. Def. Background Job

DESCRIPTION: This option is a background job that should be run nightly by the sites. It is recommended that the sites queue this option to run after midnight. This option will update the previous day's admissions with the standard deficiencies chosen by the sites, by creating an IRT entry for them. When this option is run nightly, and once the IRT entries for the standard deficiencies have been created, a field is populated in the PATIENT MOVEMENT file (#405) Field \#60.01 for the admission entry with the date that the background job was run for this admission. There is a report that is created by the IRT background job that is sent to a mail group chosen by each facility. This report lists the patients that have had short form discharges (less than 48 hours from admission) within the time frame of when the IRT background job was run. The facility should use the Bulletin Selection option under the ADT System Definition menu to set up the mail group which will receive this report. An IRT parameter must also be set up by the facility under the Set up IRT Parameters option before this option can be used. It is the STD. DEFIC. FOR SHORT FORMS? parameter. It is a YES/NO prompt. If the default is set to YES, the IRT background job will create standard deficiencies for short form admissions. If the default is set to NO, the IRT background job will not create standard deficiencies for the short form admissions.

B. Changed Options

NAME: DGJ IRT PARAMETERS

MENU TEXT: Set up IRT Parameters

DESCRIPTION: There have been two additional parameters added that must be set up through this option. The DEFAULT PHYS. FOR SIGNATURE prompt asks for the parameter default for the physician that is responsible for the signature of an IRT entry for the facility. The choices are primary or attending physician. The second parameter prompt, STD. DEFIC. FOR SHORT FORMS?, is a YES/NO parameter default. This parameter is checked by the IRT background job when creating standard deficiencies for short form discharges (patient is discharged less than 48 hours after admission). If the default is YES, standard deficiencies will be created for short forms. If the default is NO, standard deficiencies will not be created for short forms for that division.

NAME: DGJ IRT DELETE

MENU TEXT: Delete an IRT

DESCRIPTION: This option has changed in the look of the display screen due to the use of the List Processor utilities. Upon entering this option, you will be asked the division, patient, if inpatient or outpatient, and the admission for this patient. The screen will then display all of the deficiencies for this admission, incomplete as well as complete. The heading will include the name of the patient, admission date (if outpatient, it will state that in place of the admission date), and the patient ID. The data elements that are displayed on the screen for each deficiency are Deficiency, Physician Responsible for the deficiency, Status, Category, and Event Date. The screen displays the deficiencies by Category; listing the name of the Category, then the deficiencies in that Category below it. At the bottom of the screen, there are two actions that can be taken against the list of deficiencies. The EP action is the Expand action. This action will display all the IRT data for the chosen deficiency. The DL action allows the user to delete a deficiency that is listed on the screen. If the DL action is chosen for a deficiency, the screen will display the IRT data for that deficiency, then ask if you choose to delete this deficiency. If you enter \<??\> at any of the select prompts, help text will be provided. It will also display a hidden menu of standard actions that can be taken against these deficiencies. This option has been locked with the DGJ CLERK SUPER security key. This option will be made available to only those holding the key. It is recommended that this option be given to those that have the authority to delete IRT entries. This may be the supervisory clerk of the department.

NAME: DGJ IRT EDITCOMP

MENU TEXT: Edit a Complete IRT

DESCRIPTION: This option has changed in the look of the display screen due to the use of the List Processor utilities. Upon entering this option you will be asked the division, patient, if inpatient or outpatient, and the admission for this patient. The screen will then display all of the completed deficiencies for this admission: Reviewed (if facility reviews), Signed No Review (if the facility does not review), and Completed. The heading will include the name of the patient, admission date (if outpatient, it will state that in place of the admission date), and the patient ID. The data elements that are displayed on the screen for each deficiency are Deficiency, Physician Responsible for the deficiency, Status, Category, and Event Date. The screen displays the deficiencies by Category; listing the name of the Category, then the deficiencies in that Category below it. At the bottom of the screen, there are two actions that can be taken against the list of deficiencies. The EP action is the Expand action. This action will display all the IRT data for the chosen deficiency. The CE action allows the user to edit a completed deficiency that is listed on the screen. If the CE action is chosen, the screen will display the Enter/Edit screen for the completed IRT for that deficiency.

At the bottom of the screen will be a number of actions you can take against this completed IRT. Choosing action 1G will allow you to edit only the data under \#1 on the screen. Choosing 2G allows the editing of only data elements under \#2; 3G, only those elements under \#3; 4G, the comments section. By choosing EA, you have the ability to edit all of the data on the screen that is not for display only (indicated by an asterisk (\*)). If you enter \<??\> at any of the select prompts, help text will be provided. It will also display a hidden menu of standard actions that can be taken against these deficiencies. This option has been locked with the DGJ CLERK SUPER security key. This option will be made available to only those holding the key. It is recommended that this option be given to those that have the authority to edit a completed IRT entry. This may be the supervisory clerk of the department.

NAME: DGJ IRT ENTER/EDIT

MENU TEXT: Enter/Edit an IRT

DESCRIPTION: This option has changed in the look of the display screen due to the use of the List Processor utilities. Upon entering this option you will be asked the division, patient, if inpatient or outpatient, and the admission for this patient. The screen will then display all of the incomplete deficiencies for this admission; those Incomplete, Dictated, Transcribed, and Signed. The heading will include the name of the patient, admission date (if outpatient, it will state that in place of the admission date), and the patient ID. The data elements that are displayed on the screen for each deficiency are Deficiency, Physician Responsible for the deficiency, Status, Category, and Event Date. The screen displays the deficiencies by Category; listing the name of the Category, then the deficiencies in that Category below it. There are three new data elements that have been added to the Enter/Edit screen that have to do with Record Tracking and the present location of the medical record of the patient. These fields were added to the display so that the users could access the patient record easily and update deficiencies in a more timely manner. Those new data elements are borrower, phone/room, and date/time charged.

At the bottom of the screen are actions that can be taken against the list of deficiencies.

> The EN action will allow addition of a new deficiency. You will be prompted to select a category. If you enter \<??\>, a list of thirteen categories will be displayed for you to choose from. You will then be asked to select a deficiency. If you enter \<??\> at this prompt, a list of deficiencies for the category chosen will be displayed. Only those deficiencies that have been turned on by answering YES to "Track Deficiency" prompt of the Add a New/Edit Deficiency option will be displayed.

> Once those prompts have been answered, you are prompted for the information that is required for the IRT entry. Once all the data is completed, the IRT entry just created is redisplayed on the screen and you are automatically put into edit mode.

> The DE action allows the user to edit an already existing IRT entry. The screen will display the entire IRT entry chosen, and allow the user to edit all data that is not for display only (indicated by an asterisk (\*)). At the bottom of the screen will be a number of actions you can take against this IRT. Choosing action 1G will allow you to edit only the data under \#1 on the screen. Choosing 2G allows the editing of only data elements under \#2; 3G, only those elements under \#3; 4G, the comments section. By choosing EA, you have the ability to edit all of the data on the screen that is not for display only.

> The EP action is the Expand action. This action will display all the IRT data for the chosen deficiency. This option will take the place of the View an IRT option that is obsolete with this version.

> The TS action gives the user the ability to update the treating specialty and the primary and attending physicians. This option updates Bed Control if the treating specialty change is for a discharge summary. Since it is updating Bed Control, the user must hold the DGJ TS UPDATE security key in order to make changes to the treating specialty data for discharge summaries.

> The PT action allows the user to change a patient without exiting the Enter/Edit option, if the patient is within the same division. This allows for consecutive editing of patient data without exiting the option. The prompts that will be asked by this action are "Select Patient Name:" and "Display for (I)Inpatient,(O)Outpatient:". It will also ask for the admission for which you wish to update the deficiency. If you enter \<^\> at either of the above-mentioned prompts, the screen will bring you back to the screen of the previous patient.

> The DL action allows the user to delete a deficiency. By choosing this action from the initial enter/edit screen, the action will display a list of all the IRT entries for this admission (both completed and incomplete IRT entries). From this Delete an IRT List screen, the user can choose the DL action (Delete) or EP action (Expand). If the DL action is chosen for a deficiency, the screen will display the IRT record for that deficiency then ask if you wish to delete this deficiency. If you are a holder of the DGJ SUPER security key, you will have no problem using this option. If you do not hold this key, this option will have parentheses ( ) surrounding the action text. If you choose that action, the message "\>\>\> IRT Delete Menu may not be selected at this point" will appear on the screen and you will not be allowed to use this action.

> The JC action allows the user to jump to the category of their choosing on the display screen. When choosing this action, a prompt asking "Select Category you wish to move to:" will appear. The user will supply the name of the category they wish to jump to. Entering \<??\> at this prompt will list all the categories from which the user can choose. If a user selects a category that does not contain a deficiency for this admission, the message "This Category does not contain any deficiencies" will be displayed and the user will again be prompted to choose a category.

> The CE action allows the user to edit a completed deficiency. By choosing this action from the initial enter/edit screen, the action will display a list of all the completed IRT entries for this admission, encompassing those entries that have the status of Complete, Reviewed (for a facility that reviews), and Signed No Review (for those facilities that do not review). From this Edit a Completed IRT screen, the user can choose the CE action (Complete IRT Edit) or EP action (Expand). If the CE action is chosen, the screen will display the Enter/Edit screen for the completed IRT for that deficiency. At the bottom of the screen will be a number of actions you can take against this IRT. Choosing action 1G will allow you to edit only the data under \#1 on the screen. Choosing 2G allows the editing of only data elements under \#2; 3G, edit of only those elements under \#3; 4G, the comments section. By choosing EA, you have the ability to edit all of the data on the screen that is not for display only (indicated by an asterisk (\*)). If you are a holder of the DGJ SUPER security key, you will have no problem using this option. If you do not hold this key, this option will have parentheses ( ) surrounding the action text. If you choose that action, the message "\>\>\> Complete IRT Edit Menu may not be selected at this point" will appear on the screen and you will not be allowed to use this action.

NAME: DGJ IRT INCOMPLETE

MENU TEXT: Incomplete Reports Print

DESCRIPTION: There are new prompts in this option to allow greater flexibility on the reports. A beginning and ending date is asked so that the report can be run for a date range. The report can also be run for one type of deficiency, many deficiencies, or all deficiencies that the facility tracks. This option now displays borrower information.

NAME: DGJ IRT TRANS PROD

MENU TEXT: Transcription Productivity Report

DESCRIPTION: There are new prompts in this option to allow greater flexibility on the reports. A beginning and ending date is asked so that the report can be run for a date range. The report can also be run for one type of deficiency, many deficiencies, or all deficiencies that the facility tracks.

NAME: DGJ IRT UNDICTATED

MENU TEXT: Undictated Reports Print

DESCRIPTION: There are new prompts in this option to allow greater flexibility on the reports. A beginning and ending date is asked so that the report can be run for a date range. The report can also be run for one type of deficiency, many deficiencies, or all deficiencies that the facility tracks. This option now displays borrower information.

C. Deleted Options

NAME: DGJ IRT VIEW

MENU TEXT: View an IRT Record

REASON FOR DELETION: There is a new Expand action connected to the Enter/Edit option that allows the users to view a record without going to another option.

D. New Routines

DGJSUM

DGJBGJ

DGJBGJ1

DGJTEE2

DGJTEE3

DGJPDEF

DGJPDEF1

DGJPDEF2

DGJPDEF3

DGJTADD

DGJPAR1

DGJTHLP

DGJTVW3

E. Deleted Routines

DGJTECOM

F. Suggested Routines for Mapping (DSM)

None

G. File (DD) Changes

INCOMPLETE RECORDS (#393)

> Field .02 TYPE OF DEFICIENCY

> The name of this field has been changed. The old name was TYPE OF REPORT.

> Field .14 PHYSICIAN FOR DEFICIENCY

> This new field contains the name of the physician that is responsible for the deficiency at this status of the record. This field is constantly updated when the status of the IRT entry is changed.

> Field 20.01 COMMENTS

> This new field is a free text field that allows the user to enter any comments about the deficiency.

IRT TYPE OF DEFICIENCY (#393.3)

The name of this file has also changed. The old name was TYPE OF REPORT.

> Field .06 CATEGORY

> This new field contains the name of the category that the deficiency falls under.

> Field .07 TRACK DEFICIENCY

> This new field turns the tracking of the deficiency on or off. If YES or 1 is contained in this field, the deficiency will be tracked by the site. If NO or 0 is contained in this field, the facility will not track this deficiency, and it will not appear as a choice in any of the enter/edit options.

> Field .08 STANDARD DEFICIENCY?

> This new field tracks the deficiency as being a standard deficiency for the facility. If YES or 1 is contained in this field, this deficiency is considered a standard deficiency for the site. When the IRT background job is run, an IRT entry for the standard deficiencies will be created. If NO or 0 is contained in this field, this is not considered a standard deficiency and no IRT entry will be created for this deficiency when the IRT background job is run.

> Field .09 UNEDITABLE DEFICIENCY

> This new field is not seen by the user. It distinguishes the deficiencies that are transported with the IRT Type of Deficiency file. Those deficiencies are highlighted on the screen under the Add a New/Edit Deficiency option. This is the field that is checked for highlighting purposes.

MEDICAL CENTER DIVISION (#40.8)

> Field 100.1 DEFAULT PHYS. FOR SIGNATURE

> This new field contains the parameter default for the physician that is responsible for the signature of an IRT entry for the facility.

> Field 100.2 STD. DEFIC. FOR SHORT FORMS?

> This new field is a YES/NO parameter default. This parameter is checked by the IRT background job when creating standard deficiencies for short form discharges (patient is discharged less than 48 hours after admission). If the default is YES, standard deficiencies will be created for short forms. If the default is NO, standard deficiencies will not be created for short forms for that division.

MAS PARAMETERS (#43)

> Field 401 IRT BACKGROUND JOB LAST RUN

> This new field contains the date/time that the IRT background job was last run. This information is displayed on the MAS Status Screen.

> Field 513 IRT SHORT FORM LIST GROUP

> This new field stores the mail group that will be sent a bulletin when the IRT background job is run. This bulletin will contain a list of patients that have short form discharges (discharged less than 48 hours after admission) within the time frame the background job is run. This field can be set up through the Bulletin Selection option under the ADT System Definition menu.

PATIENT MOVEMENT (#405)

> Field 60.01 IRT BACKGROUND JOB RUN

> This field is populated by the IRT background job. The date/time that the background job was run for the admission is contained in this field.

H. New Files

TYPE OF CATEGORY (#393.41)

> Field .01 NAME

> This field contains the name of the category that a deficiency can fall under.

> Field .02 ABBREVIATION

> This field contains the abbreviation for the name of the category.

> Field .03 PRINT NAME

> This field contains the print name for the category. This field can be displayed on reports.

> Field .04 DISPLAY ORDER

> This field contains a number which is the order in which the category and its deficiencies are displayed on the Enter/Edit screens.

I. New Security Keys

DGJ CLERK SUPER

J. New Mail Groups

None

K. New Bulletins

None

L. E-Mail Reports

There is a report that is created by the IRT background job that is sent to a mail group chosen by each facility. This report lists the patients that have had short form discharges (less than 48 hours from admission) within the time frame of when the IRT background job was run. The facility should use the Bulletin Selection option under the ADT System Definition menu to set up the mail group to receive this report.

M. Comments

The IRT package now tracks the Physician for Deficiency for each IRT from start to completion of the IRT entry. This field will be displayed on all reports and all enter/edit screens. This value will change with each update of the status of the IRT. When the IRT is incomplete, the Physician for Deficiency will reflect the name of the Physician Responsible. Once dictated and transcribed, the Physician for Deficiency will reflect the name of the physician responsible for the signature. This is a new parameter with v5.3 that the sites must answer with either primary or attending physician. When the IRT is signed (if the facility reviews), the name of the Physician Responsible for the review will be the Physician for Deficiency.

Means Test

Introduction

With the release of PIMS v5.3, there have been some changes to the existing Means Test software and a number of new outputs.

A. New Options

NAME: DG MEANS TEST HARDSHIP REVIEW

MENU TEXT: Hardship Review Date

DESCRIPTION: This is an output of a selected date range of patients that have review dates during that time frame.

NAME: DG MEANS TEST DEDUCTIBLE

MENU TEXT: Patients Who Have Not Agreed To Pay Deductible

DESCRIPTION: This option will print a list of "active" patients that have not agreed to pay the deductible for a selected date range. This will look at dispositions, clinic appointments, scheduled admissions, and patient movements.

NAME: DG MEANS TEST PREV THRESHOLD

MENU TEXT: Means Test w/Previous Year Threshold

DESCRIPTION: This option prints a listing of patients that have had Means Tests using the prior year thresholds, when the current year thresholds are not yet available.

NAME: DG MEANS TEST FUTURE LIST

MENU TEXT: Required Means Test at Next Appointment

DESCRIPTION: This option will produce a listing of patients that will require a Means Test at their next appointment.

  
B. Changed Options

NAME: DG MEANS TEST ADD

MENU TEXT: Add a New Means Test

DESCRIPTION: Prior to adding a new Means Test, this will now allow you to print the selected patient's prior year's income (if available).

NAME: DG MEANS TEST CHANGE

MENU TEXT: Change a Patient's Means Test Category

DESCRIPTION: This option now has three new fields. If a patient's Means Test category is being changed from Category C to Category A, it will ask if this patient is a hardship case. If YES, it will ask the date on which a review of this hardship should take place and who approved the hardship.

NAME: DG MEANS TEST DELETE

MENU TEXT: Delete a Means Test

DESCRIPTION: The default to the question "Are you sure you want to delete the {date} test date?" has been changed to NO.

NAME: DG MEANS TEST VIEW EDITING

MENU TEXT: View Means Test Editing Activity

DESCRIPTION: In addition to the date, this option now captures the time of the editing.

C. Deleted Options

None

D. New Routines

DGMTO, DGMTO1 Active patients who have not agreed to pay deductible

DGMTOFA, DGMTOFA1 Listing of patients who will require a Means Test at their next appointment

DGMTOHD Hardship Review Date output

DGMTOPYT Means Test using prior year thresholds

DGMTREQB Means Test "required" bulletin

DGMTUTL Means Test Utilities

E. Deleted Routines

DGMTC0, DGMTC1, DGMTC2, DGMTCQ

F. Suggested Routines for Mapping (DSM)

DGMTA\*, DGMTCOR, DGMTDD\*, DGMTE\*, DGMTP\*, DGMTSC\*, DGMTU\*,

DGMTR, DGMTX\*G. File (DD) Changes

ANNUAL MEANS TEST (#408.31)

> Field .2 Hardship?

> This field is used to designate whether the Means Test is a hardship case.

> Field .21 Hardship Review Date

> If the Means Test is a hardship case, this field is used to track when the hardship should be reviewed.

> Field .22 Approved By

> If the Means Test has been designated as a hardship case, this field is used to store the person who approved the hardship waiver.

H. New Files

None

<u>  
</u>I. New Security Keys

None

J. New Mail Groups

None

K. New Bulletins

None

L. E-Mail Notifications

The following is a sample of the notification that will be sent if an appointment is made for a patient that requires a Means Test.

Subj: Patient: ADTPATIENT,ONE Means Test Required \[#149270\] 28 Apr 93 15:05 7 lines

From: POSTMASTER (Sender: ADTEMPLOYEE,ONE) in 'IN' basket. Page 1

------------------------------------------------------------------------------------

Action was taken on the following appointment out and the patient 'REQUIRES' a

means test.

Appointment: JAN 23, 1992@11:00

Action: CHECKED IN

Clinic: CARDIOLOGY

Entered By: ADTEMPLOYEE,ONE

Entered On: JAN 23, 1992

M. Comments

A mail group will need to be designated for the above E-Mail notification through the Bulletin Selection option of the Supervisor ADT menu, ADT System Definition submenu.

Highlighting has been added to the Means Test Screens.

There is a new field in the PATIENT file (#2) called LAST MEANS TEST. This field will contain the date of the last Means Test for a patient, if applicable.

Patient Treatment File (PTF)

Introduction

The changes to PTF in PIMS v5.3 involve two major enhancements and many legislative mandates.

The PTF module now has an archive/purge option that will enable a site to remove PTF records that are older than three fiscal years. These records will be permanently removed from the system. The second enhancement involves additional edits during the close out process in PTF. For PIMS v5.3, the Austin Edit checks performed on the PTF transmission will be included in the close out process of the Load/Edit PTF Data option. The mandates for PTF involve collecting additional information on the \<501\> screen to determine if the episode of care was related to Agent Orange, ionizing radiation, or environmental contaminants exposure. In addition, the Census dates for fiscal year 1993 will be installed with this release of PIMS v5.3.

The new PTF Archive/Purge option will enable a site to permanently remove old records from their data base. Currently, it is not possible to archive/purge a record that is not older than the current fiscal year minus three years. The List Manager was utilized to provide the user interface and facilitate the selection of PTF records to edit. This option will require coordination between the MAS ADPAC and IRM to complete the archive/purge process. Once records have been successfully archived to the appropriate medium, they can be purged from the system. Anytime before the purge, the user can abort the process without affecting the data base. Lastly, when selecting records for the archive/purge process, care should be given to select a manageable number of records and the appropriate medium for storage.

The current Austin Edits are defined in the Processing Logic Specifications version 4.3 from the Austin Automation Center. All of these edits will be incorporated into the PTF close-out process. To simulate the Austin edits, only the record generated for transmission will be used to validate the fields contained in the transmission. The assumption always has been that some of these edits are unnecessary due to VA FileMan (input transforms, screens, ...etc.). All edits will be implemented regardless of the possible redundancy with edits already present in the software. These new modules will be incorporated into PTF.

The Austin Edits will be activated after the current PTF edit checks during the close out process on the PTF Load/Edit \<701\> screen. The Austin Edits will be activated after the successful completion of the current edits.

The List Manager is used to display the errors detected during the Austin edit process. From the List Manager, it is possible to print a list of all errors encountered. This listing will resemble the EAL report generated by Austin. One addition to this report will be a description of the error along with its code. This will facilitate the correction process by eliminating the need to look up the definition of each error code. Once the listing is viewed, the coder can continue with the PTF load/edit process and correct the record. With the implementation described, the coder never leaves the PTF load/edit process during the addition checks and correction process.

The PTF mandates involve changes to the \<501\> and \<701\> screens and transmission records. In addition, all dates required for the annual Census will be loaded with the installation of PIMS v5.3. During the coding of the \<501\> screen, the Suicide Indicator has been expanded to ask for Self Inflicted Injury along with the two choices already present (Suicide Accomplished, Suicide Attempted). Lastly, on the \<501\> screen, if AO/IR/EC conditions are indicated, the coder will be prompted to determine if the episode of care was related to the exposure. These questions will be asked after the existing service connected question. The following additional information will be transmitted on the \<501\> and \<701\>.

Column Field

======== =======

\<501\> Record

121 Care related to Agent Orange?

122 Care related to Ionizing Radiation?

123 Exposed to Environmental Contaminants?

\<701\> Record

88 SC Indicator

89 Care related to Agent Orange?

90 Care related to Ionizing Radiation?

91 Exposed to Environmental Contaminants?

These questions will occur only if there is already an indication of AO/IR/EC and you are trying to determine if that particular care is related.

To be consistent with OPC, the format of the AO/IR/EC questions will be transmitted as follows.

Y for Yes

N for No

\<spaces for not required\> and no defaults will be supplied.

The SC indicator on the \<701\> will be transmitted as follows. This will be consistent with the indicator already present on the \<501\>.

1 for Yes

2 for No

If any of the movements described on the \<501\>s indicate AO exposure, the Means Test indicator will be transmitted as "AS". The existing MT indicator will not be changed, only the transmission.

The new Census dates are as follows.

Census Period Start Date: OCT. 1,1992

Census Period End Date: SEP. 30,1993 \[CENSUS DATE\]

Close-out Date: NOV. 1,1993

OK to transmit PTF: NOV. 22,1993

A new treating specialty has been added to satisfy VHA reporting requirements for Psychiatric Residential Rehabilitation and Treatment Programs (PRRTP). In addition, a new CDR account has been established for administrative purposes. The new treating specialty is PRRTP (77) and the CDR account is 1317. For more details, please refer to VHA Directive 10-92-060. The effective date for implementing the program is 10/1/93.

A. New Options

NAME: DGPT ARCHIVE/PURGE

MENU TEXT: PTF Archive/Purge

DESCRIPTION: The following is a sample of the screens involved with the new PTF Archive/Purge option. This option requires the DGPTFSUP security key.

> ADDING A NEW PTF ARCHIVE /PURGE TEMPLATE

> This requires the user to specify a date range to select records. The PTF file (#45) is then scanned by admission date for records meeting the search criteria. The following screen output shows the process.

> PTF Archive/Purge Template Apr 05, 1993 11:00:29 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// AT Add Template

> The oldest PTF record on file is from JUN 01, 1976@10:00

> Please enter the date to begin search: 6 1 88

> Please enter the date to end search: (6/1/88 - 9/30/90): 9 30 88

> EDIT A PTF ARCHIVE/PURGE TEMPLATE

> This process requires selection of an existing archive/purge template, then editing the template. The user has three options available to edit the template. These are Removing (RP) records, Selecting (SP) records, and a Detailed Inquiry (DI) option. By removing a record, you will remove it from the search template used in the archive process. Selecting will reactivate a previously removed record. No changes will become permanent until you exit the screen. The user will be prompted to make sure all changes should become permanent. Once a record has been removed from the search template, it is not possible to add it back in. The Detailed Inquiry option will give the user an opportunity to review the entire contents of the PTF record to help make the determination if a record should be archived/purged. The following screens demonstrate the Removing, Selecting, and Detailed Inquiry options.

> PTF Archive/Purge Template Apr 05, 1993 11:01:15 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 28 Active

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// ET=2

> EDIT PTF ARCHIVE/PURGE TEMPLATE, cont.

> PTF Archive/Purge Apr 05, 1993 11:03:08 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen//

> PTF Archive/Purge Apr 05, 1993 11:03:08 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen// RPRemove PTF Record(s)

> Select PTF Record(s): (1148-1166): 1152-1158

> EDIT PTF ARCHIVE/PURGE TEMPLATE, cont.

> PTF Archive/Purge Apr 05, 1993 11:04:20 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen//

> PTF Archive/Purge Apr 05, 1993 11:05:51 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen// SP Select PTF Record(s)

> Select PTF Record(s): (1148-1166): 1153-1157

> EDIT PTF ARCHIVE/PURGE TEMPLATE, cont.

> PTF Archive/Purge Apr 05, 1993 11:06:26 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> PTF Archive/Purge Apr 05, 1993 11:06:26 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen// DI PTF Detailed Inquiry

> Select PTF Record(s): (1148-1166): 1148

> EDIT PTF ARCHIVE/PURGE TEMPLATE, cont.

> PTF Detailed Inquiry Apr 05, 1993 11:08:06 Page: 1 of 3

> Patient Name: ADTPATIENT,ONE

> PTF record \#: 1148

> Admission Date: JUN 21, 1988@17:00

> Patient Name: ADTPATIENT,ONE PTF Record \#: 1148

> Admin Date: JUN 21, 1988@17:00 Disch Date: JUL 19, 1988@11:23

> Disch Specialty: NEUROLOGY Type of Dispos: REGULAR

> Disch Status: BED OCCUPANT Outpatient Treatment: NO

> ASIH Days: C&P Status:

> VA Auspices: NO Income:

> ICD CODES:

> 064. - VIR ENCEPH ARTHROPOD NEC

> Movement Dt: JUL 19, 1988@11:23

> Treated for SC condit: NO Treated for AO condit: NO

> Treated for IR condit: NO Treated for EC condit: NO

> + Enter ?? for more actions

> Select Action: Next Screen// QUIT

> PTF Archive/Purge Apr 05, 1993 11:09:17 Page: 1 of 3

> PTF Records Selected from JUN 01, 1988 thru SEP 30, 1988.

> Total Number of PTF records Selected: 28

> Status: ACTIVE

> <u>PTF \# Patient Name Adm Date/Time Dis Date/Time</u>

> \* 1148 ADTPATIENT,ONE Jun 21, 1988 17:00 Jul 19, 1988 11:23

> \* 1149 ADTPATIENT,TWO Jul 10, 1988 16:14 Aug 13, 1988 10:40

> \* 1152 ADTPATIENT,FOUR Jul 21, 1988 12:26 \<unknown\>

> \* 1153 ADTPATIENT,FIVE Jul 24, 1988 08:00 \<unknown\>

> \* 1154 ADTPATIENT,SIX Jul 25, 1988 13:01 Jul 26, 1988 13:40

> \* 1157 ADTPATIENT,SEVEN Aug 15, 1988 20:00 Aug 16, 1988 11:26

> \* 1158 ADTPATIENT,EIGHT Jul 28, 1988 Aug 15, 1988

> \* 1161 ADTPATIENT,NINE Aug 02, 1988 08:00 Aug 22, 1988 16:00

> \* 1164 ADTPATIENT,TEN Sep 13, 1988 11:02 May 22, 1989 16:49

> \* 1165 ADTPATIENT,THREE Sep 13, 1988 11:05 \<unknown\>

> \* 1166 ADTPATIENT,ELEVEN Sep 13, 1988 11:06 \<unknown\>

> + Enter ?? for more actions

> RP Remove PTF Record(s) SP Select PTF Record(s) DI PTF Detailed Inquiry

> Select Action: Next Screen// QUIT QUIT

> Should I make all changes permanent? NO// YES

> ARCHIVING/PURGING PTF RECORDS

> Once the PTF archive/purge template has been reviewed and edited, it is ready to be used to drive the archive/purge process. It is not possible to purge records before they have been archived. The archived data is placed into a word processing field to temporarily hold the data until it can be archived to an appropriate device (MAG-Tape, file, ... etc.). The following screens show how this process works.

> PTF Archive/Purge Template Apr 05, 1993 11:09:56 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Active

> Enter ?? for more actions

> AT Add Templat DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// RR Archive Records

> Select PTF Archive/Purge Template(s): (1-2): 2

> PTF Archive/Purge Template Apr 05, 1993 11:09:56 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Active

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// RR Archive Records

> Select PTF Archive/Purge Template(s): (1-2): 2

> \>\>\> Adding Archive data to PTF Archive/Purge History entry.

> \>\>\> Select Device for Archiving PTF Data.

> DEVICE: HOME//

> PTF Archive/Purge Template Apr 05, 1993 11:12:04 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Archived

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit//

> ARCHIVING/PURGING PTF RECORDS, cont.

> PTF Archive/Purge Template Apr 05, 1993 11:12:04 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Archived

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// PR Purge Records

> Select PTF Archive/Purge Template(s): (1-2): 2

> \>\>\> Adding Purge data to PTF Archive/Purge History entry.

> PTF Archive/Purge Template Apr 05, 1993 11:12:39 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Purged

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit//

> Lastly, once the records have been successfully archived/purged, it is possible to delete the entry in the PTF ARCHIVE/PURGE HISTORY file (#45.62).

> PTF Archive/Purge Template Apr 05, 1993 11:12:39 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> 2 Jun 01, 1988 Thru Sep 30, 1988 26 Purged

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit// DT Delete Template

> Select PTF Archive/Purge Template(s): (1-2): 2

> ARCHIVING/PURGING PTF RECORDS, cont.

> PTF Archive/Purge Template Apr 05, 1993 11:14:37 Page: 1 of 1

> <u>Date Range \# of Records Status</u>

> 1 Jan 01, 1987 Thru Jun 01, 1987 28 Active

> Enter ?? for more actions

> AT Add Template DT Delete Template PR Purge Records

> ET Edit Template RR Archive Records

> Select Action: Quit//B. Changed Options

None

C. Deleted Options

None

D. New Routines

|          |          |          |          |
|----------|----------|----------|----------|
| DGPT101  | DGPT101P | DGPT10CB | DGPT10S1 |
| DGPT401  | DGPT501  | DGPT501P | DGPT601  |
| DGPT701  | DGPT701P | DGPTAE   | DGPTAE01 |
| DGPTAE02 | DGPTAE03 | DGPTAE04 | DGPTAEE  |
| DGPTAEE1 | DGPTAEE2 | DGPTAPA  | DGPTAPA1 |
| DGPTAPA2 | DGPTAPA3 | DGPTAPA4 | DGPTAPP  |
| DGPTAPP1 | DGPTAPSL | DGPTLMU1 | DGPTLMU2 |
| DGPTLMU3 | DGPTLMU4 | DGPTLMU5 | DGPTLMU6 |
| DGPTSPQ  |          |          |          |

E. Deleted Routines

|        |        |     |     |
|--------|--------|-----|-----|
| DGYB\* | DGYJ\* |     |     |

F. Suggested Routines for Mapping (DSM)

|         |          |          |          |
|---------|----------|----------|----------|
| DGPTF   | DGPTF1   | DGPTF2   | DGPTF4\* |
| DGPTFD  | DGPTFJ   | DGPTFTR  | DGPTICD  |
| DGPTR\* | DGPTSU\* | DGPTTS\* | DGPTX\*  |

G. File (DD) Changes

PTF (#45)

> Field 50 501 Multiple

> Subfield 26 TREATED FOR AO CONDITION

> This field will indicate if this \<501\> movement was for an Agent Orange related condition. The data in this field will be transmitted in column 121 of the \<501\> record.

> Subfield 27 TREATED FOR IR CONDITION

> This field will indicate if this \<501\> movement was for a ionizing radiation related condition. The data in field will be transmitted in column 122 of the \<501\> record.

> Subfield 28 EXPOSED TO ENVIR CONTAMINANTS

> This field will indicate if this \<501\> movement was for an environmental contaminants related condition. This data in this field will be transmitted in column 123 of the \<501\> record.

> Field 79.25 TREATED FOR SC CONDITION

> This field will indicate if any of the \<501\> records indicate that care was for a service-connected related condition. The data in this field will be transmitted in column 88 of the \<701\> record.

> Field 79.26 TREATED FOR AO CONDITION

> This field will indicate if any of the \<501\> records indicate that care was for a Agent Orange related condition. The data in this field will be transmitted in column 89 of the \<701\> record.

> Field 79.27 TREATED FOR IR CONDITION

> This field will indicate if any of the \<501\> records indicate that care was for a ionizing radiation related condition. The data in this field will be transmitted in column 90 of the \<701\> record.

> Field 79.28 EXPOSED TO ENVIR CONTAMINANTS

> This field will indicate if any of the \<501\> records indicate that care was for a environmental contaminants related condition. The data in this field will be transmitted in column 91 of the \<701\> record.

H. New Files

PTF ARCHIVE/PURGE HISTORY (#45.62)

> Field .01 NAME

> This field contains the name of the archive/purge template. The name is automatically generated by the option based on the month/year selected for the archive/purge process.

> Field .02 ARCHIVE USER

> This field contains a pointer to the New Person file (#200) for the person who performed the archive of the PTF data.

> Field .03 ARCHIVE DATE

> This field contains the date/time the archive was performed. This field is updated by the archive option.

> Field .04 ARCHIVE STATUS

> This field indicates if the PTF data selected has been archived.

> Field .05 PURGE USER

> This field contains a pointer to the New Person file (#200) for the person who performed the purge of the PTF data.

> Field .06 PURGE DATE

> This field contains the date/time the purge was performed. This field is updated by the purge option.

> Field .07 PURGE STATUS

> This field indicates if the PTF data selected has been purged.

> Field .08 SEARCH TEMPLATE

> The data in this field contains a pointer to the Sort Template file (#.401). The sort template contains the entries selected for the PTF archive/purge process. Through the archive/purge options, the sort template is edited so that only the entries that should be archived/purged for the date range selected will be contained in the sort.

> Field .09 \# OF RECORDS

> The data in this field contains the total number of PTF records that will be processed through the archive/purge option for the date range selected. This number will be updated by the archive/purge options as the archive/purge template is edited.

> Field .1 START DATE

> This field contains the start date for the date range to archive/purge PTF records.

> Field .11 END DATE

> This field contains the end date for the date range to archive/purge PTF records.

> Field 100 ARCHIVE/PURGE DATA

> This field will contain the archive/purge data. The data should be written to a sequential device for storage.

PTF AUSTIN ERROR CODES (#45.64)

> Field .01 CODE

> This field contains the PTF Austin Error Codes. Each code begins with a digit corresponding to the record (101, 401, 601, 701) in which the error occurred.

> Field .02 DESCRIPTION

> This field contains a description of the error used for display purposes.

> Field .03 POSITION

> This field is used to indicate the position in the output stream where the error occurred. The position is used internally by the software for display purposes.

I. New Security Keys

None

J. New Mail Groups

None

K. New Bulletins

None

L. E-Mail Reports

None

M. Comments

None

Registration

Introduction

With this release, there are a number of cosmetic and detail changes that have been made to the Registration menu; however, the basic flow of the processes remain constant with the exception of the addition of the checkout process as part of the Registration Disposition process. (See the DG DISPOSITION APPLICATION and DG DISPOSITION EDIT under the Changed Options section of these release notes for more information regarding checkout.)

There are two sets of data conversions that occur during the installation of PIMS v5.3; the Claims Folder Location Conversion and the Monetary Benefit Amount Conversion. For each of these conversions, if the patient's data is not in the correct format, that patient's data will not be converted.

In order to aid users in correcting data prior to the conversion, two options were distributed as part of Patch DG\*5.2\*27 (Monetary Benefit Amounts Conversion Report and Claim Folder Location Conversion Report). These are located on the Pre-5.3 Set-up Menu (for ADPACs). These options generate reports which the user can use to identify those records that will not be converted. These two reports are sorted according to the recency of the patient's activity (registrations, appointments, etc.) in order to help the MAS ADPAC prioritize his/her efforts.

A.New Options

None

B.Changed Options

NAME: DG LOAD PATIENT DATA

MENU TEXT: Load/Edit Patient Data

DESCRIPTION: The changes described below also apply to the View Registration Data and the Register a Patient options. There have been several cosmetic changes and changes in the display fields with no data.

> HINQ: At the beginning of this option, the user is prompted to make a HINQ request. Prior to this, the money verified and service verified dates will be displayed. As part of the consolidation of monetary benefit amount fields, HINQ will be using the TOTAL ANNUAL VA CHECK AMOUNT field (see below).

> Screen \#1, 3, 4: The zip code fields now allow either 5 or 9 digit input.

> Screen \#5: The insurance data no longer captures the agent-specific information. The insurance display now includes insurance company, the policy \#, the group (group name, if entered, otherwise group number), holder, effective date, and expiration date.

> Screen \#6: There are two new sets of fields relating to service in Somalia and exposure to environmental contaminants (in Somalia or the Persian Gulf).

> Screen \#7: The service-connected related fields (P&T, Unemployable, and SC Award Date) are not displayed if the veteran is not service connected. Rated Incompetent is now asked on this screen; if this field is answered YES, the user is prompted for the DATE RULED INCOMPETENT (CIVIL) and the DATE RULED INCOMPETENT (VA).

> Screen \#8: In a change from MAS v5.2, the spouse will be considered to be "active" if s/he is a dependent during any time of the year. This will resolve the problem of entering burial expenses for a spouse in the Means Test module.

> Screen \#9: The software will prompt for spouse income if the spouse was a dependent at any time of the year. If the veteran was not married or separated on 12/31 of the year, income need not be entered for the spouse.

> The Claims Folder Location field is no longer a free text field. To enter data for this field, users may either enter the name or station number of the institution. This should make data entry quicker and guarantee that entries are usable by the AMIE package. As part of the PIMS v5.3 installation, the current field in the v5.2 field (#.312, a free text field) will be renamed to \*CLAIMS FOLDER LOCATION. A new field, CLAIMS FOLDER LOCATION (#.314, a pointer to the Institution file) will be used by PIMS instead.

> During the post init of PIMS v5.3, the Claims Folder Location conversion will populate this new field. Only those fields that are formatted according to the AMIE specification will be converted. To be convertible, Field \#.312 must begin with the station number of the Claims Folder Location. The data in the free text field will not be deleted as part of the PIMS v5.3 installation. Patch DG\*5.2\*27 has been sent to sites to help them identify those records that will not be converted with the PIMS v5.3 installation.

> The following monetary benefit fields no longer have corresponding dollar amount received fields: RECEIVING A&A BENEFITS?, RECEIVING HOUSEBOUND BENEFITS?, RECEIVING VA DISABILITY?, and RECEIVING A VA PENSION?. The current monetary benefit amount fields, AMOUNT OF AID & ATTENDANCE (#.3621); AMOUNT OF HOUSEBOUND (#.3622); AMOUNT OF VA DISABILITY (#.303); AMOUNT OF VA PENSION (#.3624), will be replaced by a new field, TOTAL ANNUAL VA CHECK AMOUNT (#.36295) which should contain the dollar value of the veteran's check from the VA. Note that the only way to delete the TOTAL ANNUAL VA CHECK AMOUNT is to answer NO to each of the four "in receipt of" monetary benefit fields.

> As part of the PIMS v5.3 post-init, Field \#.36295 will be populated by the value of one of the current monetary benefit amount fields (#.3621, \#.3622, \#.303, or \#.3624) if exactly one of them has a positive dollar amount. Those records which have two or more of these fields with a positive dollar amount will not be convertible and the new field will not be populated. No data will be deleted as part of this conversion. Patch DG\*5.2\*27 has been sent to sites to help them identify those records that will not be converted with the PIMS v5.3 installation.

> Note: The above change will not impact AMIE, because the AMIE software uses the "Receiving" questions and not the dollar amount. Also, any software that utilizes the supported ^VADPT call should not be negatively impacted since the MB^VADPT call will return the TOTAL ANNUAL VA CHECK AMOUNT where it previously returned the fields that it is replacing.

> The inconsistency checker has been modified to reflect the above changes. There is a new consistency check (MEDICAID NEEDS UPDATING) which is affected by an entry in the MAS PARAMETERS file (#43), DAYS TO UPDATE MEDICAID field (#46). If the user answered YES/NO to the "Do you want to edit Patient Data? YES//" prompt, the user will now be asked "Do you wish to return to Screen \#9 to enter missing Income Data? YES//".

NAME: DG REGISTER PATIENT

MENU TEXT: Register a Patient

> DESCRIPTION: The request for the medical record via the Record Tracking package is moved to the beginning of the registration process. The ability to print a Health Summary report, Outpatient Drug Profile, or Pharmacy Action Profile along with the VA Form 10-10 is provided. There are four new site parameters in the MAS Parameters file which allow the site to enable this enhancement, if desired.

NAME: DG CONSISTENCY PRINT

MENU TEXT: Inconsistent Data Elements Report

DESCRIPTION: The Inconsistent Data Elements Report is modified to include the initials of the clerk who last edited the registration.

NAME: DG PARAMETER ENTRY

MENU TEXT: MAS Parameter Entry/Edit

> DESCRIPTION: There are four new parameters added to control prompting for output of Drug Profiles and Health Summaries at the end of registration and during the 10/10 Print without New Registration option. There is a new parameter for affecting the consistency checker. See the descriptions for the new MAS PARAMETERS file fields. Also, the "Enter STOP CODE(S) at Disp." prompt has been moved from this screen to the Scheduling Parameters option. (For more details, see the Changed Options section of the Scheduling Release Notes.)

NAME: DG DISPOSITION APPLICATION

MENU TEXT: Disposition an Application

> DESCRIPTION: This option has been modified for checkout. Registrations (1010 and unscheduled) must be checked out to receive OPC workload credit. The first time through the checkout process, the user is taken through the interview process. The interview process consists of pertinent questions related to checking out the disposition. The first questions asked in the interview are any required classifications. The classifications include those questions related to whether or not the treatment was service connected, Agent Orange related, ionizing radiation related, or environmental contaminant related. These questions will only be asked if they are applicable to the patient. The user cannot up-arrow out of these questions unless the site has set a site parameter which permits up-arrowing. The classifications are then followed by provider, diagnosis, and stop codes based on site parameters. At the completion of the interview, the system will attempt to check the disposition out. If any required information is missing, the disposition will not be checked out. The user then has the option of viewing the Check Out screen. The disposition must be checked out to complete the disposition process.

> (See SD PARM PARAMETERS under the Changed Options section of the Scheduling Release Notes for more information regarding the up-arrow, provider, diagnosis, and stop code parameters.)

NAME: DG DISPOSITION EDIT

MENU TEXT: Disposition Log Edit

> DESCRIPTION: This option has been modified for checkout. Once a disposition has been checked out, the user will only be asked if s/he wants to see the Check Out screen. They will not be taken back through the interview process. (For more details on the disposition checkout process, see DG DISPOSITION APPLICATION option in this section of the release notes). When editing the status of a checked out disposition from "10/10 VISIT" or "UNSCHEDULED" to "APPLICATION WITHOUT EXAM", the user will be asked if s/he is sure since this type of change will delete all the checkout information entered for the disposition.

NAME: DG REGISTRATION 10/10 REPRINT

MENU TEXT: 10/10 Print without New Registration

> DESCRIPTION: The ability to print a Health Summary report, Outpatient Drug Profile, or Pharmacy Action Profile along with the VA Form 10-10 is provided. There are four new site parameters in the MAS Parameters file which allow the site to enable this enhancement, if desired. The automated 10-10 print was modified to reflect the revised 10-10 form. The use of the new ZIP+4 fields and the expansion of Question \#11 of Part V (Eligibility Status Data) are the main changes to the form.

NAME: DG PATIENT INQUIRY

MENU TEXT: Patient Inquiry

> DESCRIPTION: This has been reformatted to include the ZIP+4 functionality for the patient's permanent and temporary addresses.

NAME: DG CONSISTENCY PATIENT

MENU TEXT: Edit Inconsistent Data for a Patient

> DESCRIPTION: The consistency checker has been modified to reflect the changes in the Load/Edit Patient Data option (ZIP+4 functionality, TOTAL ANNUAL VA CHECK AMOUNT field, etc.)

NAME: DG REGISTRATION VIEW

MENU TEXT: View Registration Data

> DESCRIPTION: This option has been modified to reflect the changes in the Load/Edit Patient Data option.

C.Deleted Options

None

D.New Routines

DGREGDD DGREGDD1 DGRPDD1 DGRPU1 DG1010PA DGPMHST

DGPMSTAT

E.Deleted Routines

None

F.Suggested Routines for Mapping (DSM)

It is recommended that the following routines be mapped: DG10\*, DGINP, DGINPW, DGLOCK\*, DGREG\*, DGRP\*, DGSEC, DGUTL, DPTDUP, DPTLK\*, DGPMHST, DGPMSTAT, and VADPT\*. This includes the DGRPX\* routines which are generated by compiled templates.

G.File (DD) Changes

PATIENT (#2)

There are several new fields for entering either 5 or 9 digit zip code (ZIP+4). Each of these fields has an associated (old) ZIP CODE field. When the ZIP+4 field is entered/edited, the associated zip code field is updated with the first 5 digits of the ZIP+4. A similar mechanism updates the ZIP+4 fields when the zip code fields are modified. The ZIP+4 fields will accept either 5 or 9 numeric entries, with or without punctuation.

> Field .09 SOCIAL SECURITY NUMBER

> The input transform routine for this field has been modified to further restrict the allowable ranges of social security numbers.

> <u>  
> </u>Field .1112 ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's primary address.

> Field .12105 TEMPORARY ADDRESS ACTIVE?

> This field has been renamed from TEMPORARY ADDRESS ENTER/EDIT? to more closely represent its use.

> Field .12112 TEMPORARY ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's temporary address.

> Field .2201 E-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's emergency contact's address.

> Field .2202 D-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's designee's address.

> Field .2203 K2-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's secondary next of kin's address.

> Field .2204 E2-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's secondary emergency contact's address.

> Field .2205 EMPLOYER ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's employer's address.

> Field .2206 SPOUSE'S EMP ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's spouse's employer's address.

> Field .2207 K-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's next of kin's address.

> Field .290012 ZIP+4 (CIVIL)

> This is a new 5 or 9 digit zip code field. It is associated with the patient's civilian guardian's address.

> Field .29013 ZIP+4 (VA)

> This is a new 5 or 9 digit zip code field. It is associated with the patient's VA guardian's address.

> Field .312 \*CLAIM FOLDER LOCATION

> This field has been renamed and starred for deletion at a later date. This field is a free text field. The new field CLAIM FOLDER LOCATION (#.314) will populate this field with values per AMIE specifications (station number-name). In a similar fashion, entries into this field will populate Field \#.314, if the first 3 characters match station number in the site's Institution file (#4).

> Field .314 CLAIM FOLDER LOCATION

> This is a new field that is a pointer to the Institution file (#4).

> Field .322013 ENVIRONMENTAL CONTAMINANTS?

> This is a new field. Either the Persian Gulf Service? field (#.32201) or the Somalia Service Indicated? field (#.322016) must be answered YES for this field to be answered YES. A YES response to this field indicates that the patient has been exposed to environmental contaminants.

> Field .322014 ENVIR. CONT. REGISTRATION DATE

> This is a new field. The .322013 field must be answered YES for this field to be answered. Enter the date the patient was registered as having potential environmental contaminant conditions.

> Field .322015 ENVIR. CONT. EXAM DATE

> This is a new field. The .322013 field must be answered YES for this field to be answered. Enter the date that an examination for environmental contaminant related conditions occurred.

> Field .322016 SOMALIA SERVICE INDICATED?

> This is a new field. A YES response indicates that the patient served in Somalia.

> Field .322017 SOMALIA FROM DATE

> This is a new field. The .322016 field must be answered YES for this field to be answered. Enter the date Somalia service started.

> Field .322018 SOMALIA TO DATE

> This is a new field. The .322016 field must be answered YES for this field to be answered. Enter the date Somalia service ended.

> Field .3623 \*AMOUNT OF SOCIAL SECURITY

> This field is no longer supported and will be deleted with some future release.

> Field .3625 \*AMOUNT OF MILITARY RETIREMENT

> This field is no longer supported and will be deleted with some future release.

> Field .36295 TOTAL ANNUAL VA CHECK AMOUNT

> This is a new field containing the veteran's total annual VA check amount. This field replaces four fields: AMOUNT OF VA DISABILITY (#.303), AMOUNT OF AID & ATTENDANCE (#.3621), AMOUNT OF HOUSEBOUND (#.3622), and AMOUNT OF VA PENSION (#.3624). At least one of the following fields must be answered YES for a dollar amount to be entered into this field: RECEIVING VA DISABILITY? (#.3025), RECEIVING A&A BENEFITS? (#.36205), RECEIVING HOUSEBOUND BENEFITS (#.36215), or RECEIVING A VA PENSION? (#.36235). Setting each of these four fields to a value other than YES will delete this field.

> Field 1000 (Multiple) DISPOSITION LOG-IN DATE/TIME

> Subfield 38 A-ZIP+4

> This is a new 5 or 9 digit zip code field. It is associated with the patient's attorney's zip code.

DG SECURITY LOG (#38.1)

> Field 50 DATE/TIME RECORD ACCESSED

> Subfield 3 OPTION USED WHEN ACCESSED

> The name of this subfield has been changed to OPTION/PROTOCOL USED.

> This field has been changed from a pointer type field to File \# 19 OPTION file to a free text field. This field now stores the name of the option or protocol that was last used when a sensitive patient is accessed.

MEDICAL CENTER DIVISION (#40.8)

> Field 100.1 DEFAULT PHYS. FOR SIGNATURE

> This new field contains the parameter default for the physician that is responsible for the signature of an IRT entry for the facility.

> Field 100.2 STD. DEFIC. FOR SHORT FORMS?

> This new field is a YES/NO parameter default. This parameter is checked by the IRT background job when creating standard deficiencies for short form discharges (patient is discharged less than 48 hours after admission). If the default is YES, standard deficiencies will be created for short forms. If the default is NO, standard deficiencies will not be created for short forms for that division.

MAS PARAMETERS (#43)

> Field 42 PRINT HEALTH SUMMARY?

> This is a new field. This helps control the prompting for output at the end of registration and during the 10/10 Print without New Registration option. If this field is set to YES and the Health Summary package is loaded (v2.5, patch \#3 or greater), users will be prompted to print a Health Summary after they are prompted to print a 10-10.

> Field 43 DEFAULT HEALTH SUMMARY

> This is a new field. This helps control the prompting for output at the end of registration and during the 10/10 Print without New Registration option. This stores the default Health Summary type.

> Field 44 CHOICE OF DRUG PROFILE TYPE?

> This is a new field. This helps control the prompting for output at the end of registration and during the 10/10 Print without New Registration option. This will have no effect unless the PRINT DRUG PROFILES WITH 10-10 field is set to YES. If this field is set to YES, the user will be prompted to choose which type of Drug Profile they wish to print (Action or Informational). If this field is not set to YES and the user chooses to print a Drug Profile, the default type of drug profile will print.

> Field 45 DEFAULT TYPE OF DRUG PROFILE

> This is a new field. This helps control the prompting for output at the end of registration and during the 10/10 Print without New Registration option. This stores the default type of Drug Profile to be printed (Action or Informational). If this field has not been entered, Informational will be the default.

> Field 46 DAYS TO UPDATE MEDICAID

> This is a new field. After this number of days without updating the DATE MEDICAID LAST ASKED field, an inconsistency will be created. The default is 365 days.

> Field 401 IRT BACKGROUND JOB LAST RUN

> This new field contains the date/time that the IRT background job was last run. This information is displayed on the MAS Status Screen.

> Field 513 IRT SHORT FORM LIST GROUP

> This new field stores the mail group that will be sent a bulletin by the IRT background job when it is run. This bulletin will contain a list of patients that have short form discharges (discharged less than 48 hours after admission) within the time frame for which the background job is run. This field can be set up through the Bulletin Selection option under the ADT System Definition menu.

PATIENT MOVEMENT (#405)

> Field 60.01 IRT BACKGROUND JOB RUN

> This field is populated by the IRT background job. The date/time that the background job was run for the admission is contained in this field.

H.New Files

None

I.New Security Keys

None

J.New Mail Groups

None

K.New Bulletins

None

L.E-Mail Reports

None

M.Comments

In addition to the above changes, there were two significant enhancement patches to MAS v5.2 that altered the registration process; the Pharmacy Copay Exemption patch (DG\*5.2\*22) which added the ability to determine if certain veterans were exempt from the outpatient pharmacy copayment, and the Income Screen: Copy Old Financial Data patch (DG\*5.2\*21) which enabled users to copy the previous year's income data to the present in the income screen.

Scheduling

Introduction

The major change to the Scheduling module in v5.3 is the requirement that all outpatient encounters must be checked out in order to receive OPC workload credit.

1. Checkout Requirement

In v5.2, the requirement to check in all appointments was introduced to help solve over reporting when appointments were not cancelled or no-showed. In v5.3, checkout is being introduced to capture additional required information, such as whether the encounter was related to a service-connected disability. The site will also be able to collect other optional data, such as the provider and diagnosis for the encounter. (For more details, see Checkout section.)

The automated checkout will also help speed up current checkout procedures, like scheduling a follow-up appointment and adding stop codes and CPTs to the visit. This is possible because information for the current appointment can be used when scheduling the follow up, such as patient and clinic. Additionally, when a stop code or procedure is associated with an appointment, the information regarding appointment type, associated clinic, and eligibility for the appointment is automatically entered. In many cases, adding a stop code means only specifying the code.

Stop codes associated with an appointment or disposition do not need to be checked out. The required information for the stop code checkout is obtained from the associated appointment or disposition encounter.

2. Scheduling Outputs

Along with the requirement to check out encounters and capture required information, OPC software has been changed to transmit this data. (See Technical Changes section for more details.)

The following reports have been enhanced to include checkout information.

> appointment lists

> routing slips

> appointment management reports

A new option called Provider/Diagnosis Report has been added. This option allows the site to print provider and diagnosis information optionally captured during the checkout process.

3. Stop Code Update

This release also adds a number of new stop codes that can be used as of 10/1/93. A few stop codes have been inactivated as of 10/1/93. (For more details see Other Changes section.)

CheckOut

As mentioned above, all outpatient encounters on or after 10/1/93 must be checked out to receive OPC workload credit. Encounters not checked out will not be used during OPC generation and, as a result, will not be sent during OPC transmission.

The following types of outpatient encounters must be checked out.

> appointments

> stop code additions (add/edits)

> registrations (10/10 and unscheduled)

Exceptions: The following encounters do not have to be checked out.

> encounters while the patient is an inpatient

> encounters in non-count clinics

> "add/edits" associated with an appointment or disposition

> at this time, encounters associated with stop codes 104-170

> (These are stop codes for ancillary services, such as radiology \[#105\]. The information needed to check out these encounters is often not readily available.)

> **NOTE:** After 9/30/93, checking in appointments is no longer required. If the clerk checks out an appointment before 10/1/93, the site will receive workload credit even if the appointment is not checked in. In other words, a checkout is as good as a check in for appointments earlier than 10/1/93. When you check out an appointment before 10/1/93, the user is not prompted for any additional checkout information.

1. Checkout Options/Actions

The v5.3 software has been written so that the checkout process will be basically the same regardless of the type of encounter.

> For appointments, the clerk will use either the new Checkout action of the Appointment Management option or the Appointment Check In/Out option. Both options are on the Appointment menu.

> Selecting appointments to check out for both the new Checkout action and the checkout portion of Appointment Check In/Out option work much like check in functionality introduced in v5.2. However, the actual checkout process can be more involved than the check in process. The process is explained in detail below.

> If an appointment is made for a past date, the checkout process will automatically be invoked. The Make Appointment option, Make Appointment action of the Appointment Management option, and multiple booking options are affected.

> For adding stop codes, the checkout process will automatically be presented to the user as part of the Add/Edit Stop Code option and new Add/Edit action in the Appointment Management option.

> For dispositioning registrations, the Disposition a Registration and Edit a Disposition options both automatically present the checkout process to the user.

2. Checkout Process

The checkout "interview" process is broken down into the following four activities.

A. Requesting follow-up encounters  
B. Entering required information  
C. Entering optional informationD. Adding Stop Code and CPT codes

> A. Follow-up

> This part of the interview will only occur when the user is checking out an appointment. It allows the user to book a follow-up appointment for the patient. It is the first activity in the interview process. As a result, the clerk can accommodate the patient immediately without having the patient wait as current appointment information is entered.

> B. Required Information

> The information that is required by VACO to receive workload credit is entered into the system during this part of the interview. The following is a chart of the information that may be gathered and the criteria used to determine if it needs to be collected.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 36%" />
<col style="width: 23%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>#</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Classification Question</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Responses</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Criteria</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>1</strong></p>
</blockquote></td>
<td><blockquote>
<p>Encounter was for <strong>service-connected</strong> condition?</p>
</blockquote></td>
<td><blockquote>
<p>Yes or No</p>
<p>or Not Applicable</p>
</blockquote></td>
<td><blockquote>
<p>Patient's eligibility is service connected.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>2</strong></p>
</blockquote></td>
<td><blockquote>
<p>Encounter was related to exposure to <strong>Agent Orange</strong>?</p>
</blockquote></td>
<td><blockquote>
<p>Yes or No</p>
<p>or Not Applicable</p>
</blockquote></td>
<td><blockquote>
<p>Data indicates patient was exposed to <strong>Agent Orange</strong> and #1 was answered NO or was Not Applicable.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>3</strong></p>
</blockquote></td>
<td><blockquote>
<p>Encounter was related to exposure to <strong>ionizing radiation</strong>?</p>
</blockquote></td>
<td><blockquote>
<p>Yes or No</p>
<p>or Not Applicable</p>
</blockquote></td>
<td><blockquote>
<p>Data indicates patient was exposed to <strong>ionizing radiation</strong> and #1 was answered NO or was Not Applicable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>4</strong></p>
</blockquote></td>
<td><blockquote>
<p>Encounter was related to exposure to <strong>environmental contaminants</strong>?</p>
</blockquote></td>
<td><blockquote>
<p>Yes or No</p>
<p>or Not Applicable</p>
</blockquote></td>
<td><blockquote>
<p>Data indicates patient was exposed to <strong>environmental contaminants</strong> and #1 was answered NO or was Not Applicable. This question is also asked if the patient is an active duty non-veteran</p>
</blockquote></td>
</tr>
</tbody>
</table>

This information is being collected solely for the purpose of determining if the patient is receiving care in a mandatory or discretionary category. VHA was cited on an IG audit for not being able to determine if the SC patient (less than 50%) was being seen for a SC condition. Also, if patients were not being seen for a SC condition, was care a result of patient's exposure to Agent Orange, ionizing radiation or environmental contaminants. The IG has also recommended that the data captured be available in a national data base.

This information is also needed for billing purposes and will be used in a future version of the Integrated Billing package. IB needs to know if the encounter is service connected for all SC patients. As a result, the service-connected classification question will be asked for all encounters of SC veterans, even those greater than 50%.

> C. Optional Information

> The site has the option to collect provider and diagnosis information about the encounter. This data will be collected as part of the checkout interview after the required information is captured. By clinic and dispositions, the site can choose to 1) not collect the data, 2) collect it but not require it, 3) require data entry.

> D. Stop Codes & CPTs

> For appointments and dispositions, the site can also indicate that the clerk should be asked if there are any additional stop codes and/or CPT codes for the encounter. If they are asked and answered YES, then the familiar add/edit stop code functionality is presented to the user.

After the interview process has ended, the system will determine if all the necessary information is present. If so, the encounter is given a "checked out" status and the "check out completion date and time" is automatically entered by the system.

Finally, it is possible to add or change any of the checkout information. The Appointment Management option has separate actions that allow the clerk to edit each type of data, such as classification and provider. Also, the checkout action can be selected again and a profile of the data is presented. While viewing this profile screen, the clerk can edit the data using the appropriate individual action or an interview action can be selected. This action will guide the clerk through the same data capture process as the original interview.

SITE PREPARATION

In order to prepare for the checkout process, there are a number of steps that should be taken by the site.

1. Inform the Providers

Clinicians must be informed about the new requirement for service connected, Agent Orange, and other information.

2. Operational Changes

The site must develop a mechanism to inform the clinicians which encounters will require this information. The routing slips and the appointment lists have been modified to list the required data that is needed for each encounter. Your site may be able to use these reports to communicate each encounter's needs to the provider.

> **NOTE:** In the next version of the Integrated Billing package there will be an Encounter Form Utility that the site can use to help gather the required information.

3. Parameter Set Up

There are a number of new site and clinic parameters in v5.3 that the MAS ADPAC will need to enter to control the checkout process.

> A. SITE PARAMETERS

> Using the Scheduling Site Parameter option, the following parameters can be set to control the registration disposition checkout process.

Disposition Related

ASK STOP CODES ON DISPOSITION?:

During disposition, should the user be prompted for stop codes? If this field is set to YES, the user will be prompted for stop codes. If the status of the disposition is a 10/10 VISIT or UNSCHEDULED, the user will be prompted for stop codes during the checkout interview process. If the status of the disposition is APPLICATION WITHOUT EXAM, the user will be prompted for stop codes at the end of the disposition process.

If the status of the disposition is a 10/10 VISIT or UNSCHEDULED, the stop codes can also be entered through the Check Out screen. Those entered through the Check Out screen are automatically associated with the disposition.

> **NOTE:** This parameter is not new. It previously was part of the MAS Parameter Entry/Edit option.

ASK PROVIDER ON DISPOSITION: \<new parameter\>

When checking out a patient during disposition, should the user be prompted for provider? If this field is set to YES/REQUIRED, the user will be prompted for a selection during the checkout interview process. A selection must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for a selection during the checkout interview process. The provider does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for a selection during the checkout interview process. Regardless of how the parameter is set, a selection can be entered through the Check Out screen.

ASK DIAGNOSIS ON DISPOSITION: \<new parameter\>

When checking out a patient during disposition, should the user be prompted for diagnosis? (See ASK PROVIDER ON DISPOSITION for input explanation.)

> Other Site Parameters

ALLOW UP-ARROW OUT OF CLASSIFICATION:

Enter YES to allow users to up-arrow out of the classification questions (i.e., service connected, Agent Orange, etc.). NOTE: The classification questions are required for workload credit. Allowing the user to exit without answering these questions could result in additional work at a later time to track down the record and determine the answer to these questions. A site may want to allow up-arrowing initially; however, after the collecting of this information becomes a routine part of the outpatient encounter process, they will probably want to set this parameter to NO.

> B. CLINIC PARAMETERS

> Use the Set up a Clinic option to set these checkout related parameters.

ASK FOR CHECK IN/OUT TIME:

When checking in/out a patient for an appointment, should the user be prompted for date and time? If this field is set to YES, the user will be prompted for the date and time. The current date and time will be the default. If this field is set to NO or is not entered, the user will not be prompted and the current date and time will automatically be entered. If an appointment is scheduled retroactively, the system will use the date and time of the appointment as the check in/out time. This date/time will either be entered automatically or used as a default, depending upon how this parameter is set.

ASK PROVIDER AT CHECK OUT: \<new parameter\>

When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for provider? (See ASK PROVIDER ON DISPOSITION for input explanation.)

PROVIDER (multiple) \<new parameter\>

If the ASK PROVIDER AT CHECK OUT parameter is set to YES/REQUIRED or YES/NOT REQUIRED, the clinic set up process will allow the site to enter a list of provider names for that clinic. This list will automatically be presented to the user before the prompting for the provider during the checkout process. The user is not required to select a provider from this list but it is recommended that this list be supplied to cut down on the number of data entry errors.

To further help data entry, one of the providers entered can be designated as the DEFAULT PROVIDER. Only one provider can be designated as the default. This default provider will be the provider presented to the user at the "Select Provider:" prompt during checkout. It is not required to designate a default provider; however, it is highly recommended.

ASK DIAGNOSIS AT CHECK OUT: \<new parameter\>

When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for diagnosis? (See ASK PROVIDER ON DISPOSITION for input explanation.)

DIAGNOSIS (multiple) \<new parameter\>

If the ASK DIAGNOSIS AT CHECK OUT parameter is set to YES/REQUIRED or YES/NOT REQUIRED, the clinic set up process will allow the site to enter a list of diagnoses for that clinic. This list will automatically be presented to the user before the prompting for the diagnosis during the checkout process. The user is not required to select a diagnosis from this list but it is recommended that this list be supplied to cut down on the number of data entry errors.

To further help data entry, one of the diagnoses entered can be designated as the DEFAULT DIAGNOSIS. Only one diagnosis can be designated as the default. This default diagnosis will be the diagnosis presented to the user at the "Select Diagnosis:" prompt during checkout. It is not required to designate a default diagnosis; however, it is highly recommended.

ASK STOP CODES AT CHECK OUT: \<new parameter\>

When checking out a patient for an appointment, should the user be prompted for stop codes? If this field is set to YES, the user will be prompted for stop codes during the checkout interview process. If this field is set to NO or is not entered, the user will not be prompted for stop codes during the checkout interview process.

Stop codes can also be entered through the Check Out screen or the Appointment Management screen. They can either be entered as stand-alone add/edits or associated with an appointment.

> C. Providers In New Person File

> If your site decides to capture provider data as part of the checkout process, you may need to add nurses, social workers, etc. in the NEW PERSON file. If these providers are already in the file, make sure they all have the Provider key.

workload monitoring

In version 5.2, a series of management outputs were supplied to help the site manage the check in of appointments. For v5.3, theses same outputs have been enhanced to help monitor the checking out of all outpatient encounters. A new report has been added to allow monitoring provider and diagnostic information if the site chooses to capture this data.

1. Appointment Lists and Routing Slips

In v5.2, the ability to print barcodes on the appointment list was introduced. In v5.3, an indication of data required to check out the appointment has been added. The routing slips have been enhanced to print the same information. You can now also print routing slips for one, many, or all clinics. In previous versions, you had to print routing slips for all clinics.

The following is a sample of the appointment list indicating the data that will be required upon checkout.

> APPOINTMENTS FOR CARDIOLOGY CLINIC ON MON JUL 12, 1993 JUL 6, 1993

> APPOINT PATIENT NAME SSN LAB X-RAY EKG

> TIME TIME TIME TIME

> OTHER INFORMATION WARD LOCATION

> ROOM-BED

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 9:00 AM

> ADTPATIENT,ONE 000456789 8:40 AM

> \*\* Required for OPC Credit =\> AO IR EC \*\*

> 2:00 PM

> \*ADTPATIENT,TWO 666456789

> \*\* Required for OPC Credit =\> SC \*\*

The legend for the above "required" items is as follows.

SC Was encounter related to service-connected condition?

AO Was encounter related to exposure to Agent Orange?

IR Was encounter related to exposure to ionizing radiation?

EC Was encounter related to exposure to environmental contaminants?

The following is a sample of the new routing slip format.

> ADTPATIENT,ONE APPOINTMENT DATE

> 000-45-6789 07/12/93

> HOME ADDRESS

> ALBANY NEW YORK 12203

> PSA: UNKNOWN

> Service Connected: NO

> Disabilities: NONE STATED

> Health Insurance: YES

> Insurance Policy \# Group \# Holder

> --------- -------- ------- -------

> PRUDENTIAL 518 L518 APPLICANT

> \*\*CURRENT APPOINTMENTS\*\*

> TIME CLINIC LOCATION

> 8:40 AM XRAY

> 9:00 AM CARDIOLOGY 2ND FLOOR, RM 221

> List diagnosis \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> List any procedures performed during this clinic visit \_\_\_\_\_\_\_\_

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Was treatment related to Agent Orange Exposure? \_\_Yes \_\_No

> Was treatment related to Ionizing Radiation Exposure? \_\_Yes \_\_No

> Was treatment related to Environmental Contaminant Exposure? \_\_Yes \_\_No

> DATE PRINTED: 07/06/93

2. Nightly Job

The nightly job has been modified to present information regarding all outpatient encounters, not just appointments. The following is an example of the MailMan message that is produced.

> Subj: OUTPATIENT ENCOUNTER STATUS UPDATE \[#4585713\] 30 JUN 93 02:04

> From: \<POSTMASTER@<span class="mark">site</span>\> in 'IN' basket. Page 1

> --------------------------------------------------------------------

> The 'Outpatient Encounter' status update has been completed.

> Job STARTED Date/Time: JUN 30, 1993@02:00:23

> Job FINISHED Date/Time: JUN 30, 1993@02:03:59

> \*\*\* Update Summary \*\*\*

> Outpatient encounters from 06/29/93 to 06/29/93@2359:

> Division: <span class="mark">site</span>

> Appointments Total

> Clinic Requiring Action Appts Pct.

> ------ ---------------- ----- ------

> ADTPROVIDER, EIGHT 1 7 14.3%

> ADTPROVIDER, FIVE 3 13 23.1%

> ADTPROVIDER, FOUR (WALK- 1 22 4.5%

> ADTPROVIDER, NINE/PSYCHIATRY CLI 1 11 9.1%

> ADTPROVIDER, ONE 1 2 50.0%

> ADTPROVIDER, SEVEN., PH.D 1 5 20.0%

> ADTPROVIDER, SIX, MHC(PSYCHOLOG 2 5 40.0%

> ADTPROVIDER, THREE 2 14 14.3%

> ADTPROVIDER, TWO 1 2 50.0%

> CNH NURSE 7 7 100.0%

> INJECTIONS 1 1 100.0%

> LAB 1 11 9.1%

> OPTOMETRY 6 6 100.0%

> PULMONARY FUNCTION TEST 1 1 100.0%

> STRESS TEST 2 2 100.0%

> X-RAY 2 6 33.3%

> X-RAY, SPECIAL 2 3 66.7%

> ALL OTHER CLINICS 0 75 0.0%

> ------------- ---------------- ----- ------

> Clinic Totals 35 193 18.1%

> Add/Edits Total

> Stop Code Requiring Action Stops Pct.

> --------- ---------------- ----- ------

> ALL OTHER STOPS 0 30 0.0%

> --------------- ---------------- ----- ------

> Add/Edit Totals 0 30 0.0%

> Dispositions

> Requiring Action Total Pct.

> ---------------- ----- ------

> Dispositions 0 14 0.0%

> ============== =============== ===== ======

> DIVISION TOTAL 35 237 14.8%

> ============== =============== ===== ======

> FACILITY TOTAL 35 237 14.8%

3. Appointment Management Reports

Using the information from the nightly message, the site can produce a detailed listing of the encounters still requiring action using the Appointment Management Report option. This option is located on the Outputs menu of the Scheduling Manager's menu.

In v5.2, this report only covered appointments. In v5.3, this report not only covers all outpatient encounters, but will also indicate what required information is needed in order to check out the encounter. The following is a sample report.

Appointment Management Report Report Date: JUL 06, 1993@15:25 Page: 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Dates : 06/01/93 to 06/30/93 Division: ALBANY

Status : ACTION REQUIRED Clinic: INTERNAL MED (KAREN)

Sorted By: DIVISION, CLINIC, PATIENT Total: 4

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Patient Encounter Date/Time Means Test Eligibility Status

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ADTPATIENT,ONE 1183 06/08/93@08:00 SC, LESS THAN 50% ACTION REQUIRED

Missing: SC / Provider / Diagnosis /

ADTPATIENT,ONE 1183 06/08/93@08:00 SC, LESS THAN 50% ACTION REQUIRED

This encounter is associated with an appointment.

ADTPATIENT,TWO 5424 06/21/93@08:00 CAT C NON-SERVICE CONNECTED NO ACTION TAKEN

Missing: AO / IR / Diagnosis /

ADTPATIENT,TEN 3421 06/21/93@08:00 CAT C NON-SERVICE CONNECTED ACTION REQUIRED

Missing: EC

The legend for the above "Missing" items is as follows.

SC Was encounter related to service-connected condition?

AO Was encounter related to exposure to Agent Orange?

IR Was encounter related to exposure to ionizing radiation?

EC Was encounter related to exposure to environmental contaminants?

Provider Provider information is missing.

Diagnosis Diagnosis information is missing.

Notice the caption "This encounter is associated with an appointment." If an encounter has this indicator, the encounter does not need to be checked out. When the associated appointment (or disposition) is checked out, this encounter is also checked out. These are usually add/edit stop codes.

4. Provider/Dx Reports

The other major report enhancement is the Provider/Diagnosis Report. This is a new option under the same Outputs menu. This report allows the site to produce detail and statistical information regarding provider and diagnosis information. The site must choose to capture this data as part of the checkout process in order for this report to be meaningful. The option allows the user to specify sort order and select the desired providers, diagnosis, clinics, etc. The following is a sample report.

Provider/Diagnosis Report sorted by Provider and Diagnosis JUL 06, 1993 Page: 1

Inclusion Dates: Jun 01, 1993 to Jun 30, 1993

Division: TROY1

PATIENT ENCOUNTER DATE CLINIC/STOP CODE PROVIDER DX CODE

------------------- ------------------ -------------------- -------------- -------

ADTPATIENT,ONE 2202 Jun 02, 1993@10:00 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR

ADTPATIENT,TWO 8904 Jun 03, 1993@08:19 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR

ADTPATIENT,TEN 7964 Jun 03, 1993@14:00 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR

ADTPATIENT,TEN 7964 Jun 07, 1993@09:00 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR

ADTPATIENT,TEN 7964 Jun 09, 1993@16:53 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR

ADTPATIENT,SIX 1212 Jun 23, 1993@10:00 CARDIOLOGY ADTPROVIDER,ONE 786.6

316/ONCOLOGY/TUMOR 123.1

APPOINTMENT MANAGEMENT

In v5.2, the List Manager was introduced as part of the Scheduling package. This utility was first used in the Appointment Management option. It allows the user to view a list of appointments and then take action against those appointments without leaving the option. Initially, actions such as cancel, no-show, check in, and make were supplied. Also, there were a number of screen manipulation actions available. These included next screen, previous screen, print list, and many others.

With the new checkout requirement, there was need for more appointment related actions, such as checkout, classification edit, provider edit, and others. There have been many requests for additional actions, such as editing the patient's basic demographic and clinic enrollment data. However, there was no room for additional actions to be listed at the bottom of the screen. In order to make room for these new actions, the List Manager has been changed to not list the screen manipulation actions. They are still available but are "hidden", much like MailMan is always available at the menu prompt. To see a list of these actions, the user enters \<??\>.

The following are the scheduling specific actions available.

> CI Check In PT Change Patient CO Check Out

> UN Unscheduled Visit CL Change Clinic EC Edit Classification

> MA Make Appointment CD Change Date Range PR Provider Update

> CA Cancel Appointment EP Expand Entry DX Diagnosis Update

> NS No Show AE Add/Edit DE Delete Check Out

> DC Discharge Clinic RT Record Tracking

> AL Appointment Lists PD Patient Demographics

The following are the screen manipulation actions that are also available.

> \+ Next Screen FS First Screen SL Search List

> \- Previous Screen LS Last Screen ADPL Auto Display(On/Off)

> UP Up a Line GO Go to Page QU Quit

> DN Down a Line RD Re Display Screen

> \> Shift View to Right PS Print Screen

> \< Shift View to Left PL Print List

TECHNICAL CHANGES1. OPC Format

The required data collected as part of the checkout process will be transmitted to Austin and the Hines ISC for outpatient encounters occurring on or after 10/1/93.

The new OPC format is as follows.

FIELD POSITION

|      |                                                              |         |
|------|--------------------------------------------------------------|---------|
| 1\.  | DATE OF VISIT                                                | 1-6     |
|      | A. MONTH                                                     | (1-2)   |
|      | B. DAY                                                       | (3-4 )  |
|      | C. YEAR                                                      | (5-6)   |
| 2\.  | FACILITY NUMBER/SUFFIX                                       | 7-11    |
|      | A. FACILITY NUMBER                                           | (7-9)   |
|      | B. SUFFIX                                                    | (10-11) |
| 3\.  | SOCIAL SECURITY NUMBER                                       | 12-20   |
| 4\.  | BIRTH YEAR                                                   | 21-22   |
| 5\.  | ZIP CODE                                                     | 23-27   |
| 6\.  | SEX CODE                                                     | 28      |
| 7\.  | POW INDICATOR                                                | 29      |
| 8\.  | PERIOD OF SERVICE                                            | 30-31   |
| 9\.  | VETERAN ELIGIBILITY CODE                                     | 32      |
| 10\. | NON-VETERAN ELIGIBILITY CODE                                 | 33      |
| 11\. | PURPOSE OF VISIT                                             | 34      |
| 12\. | LOCATION OF VISIT                                            | 35      |
| 13\. | MEANS TEST INDICATOR                                         | 36-37   |
| 14\. | NUMBER OF DEPENDENTS                                         | 38-39   |
| 15\. | SPECIAL SURVEYS                                              | 40-46   |
|      | A. SERVICE VIETNAM                                           | 40      |
|      | B. EXPOSURE AGENT ORANGE                                     | 41      |
|      | C. EXPOSURE RADIATION                                        | 42      |
|      | D. BLANK                                                     | 43      |
|      | E. MEDICAL CARE REQUIRED                                     | 44      |
|      | F. BLANK                                                     | 45      |
|      | G. OTHER MEDICAL CARE                                        | 46      |
| 16\. | INCOME                                                       | 47-52   |
| 17\. | NAME                                                         | 53-66   |
| 18\. | FISCAL YEAR                                                  | 67-68   |
| 19\. | REGULAR CLINIC STOPS                                         |         |
|      | (NOTE: SEE ATTACHED LISTING FOR STOP CODES WHERE             |         |
|      | BLANKS WILL BE TRANSMITTED VERSUS THE QUESTIONS NOTED BELOW) |         |
|      |                                                              |         |
| A.   | STOP CODE FORMAT (1 - 15)                                    | 69-203  |
|      | \(1\) STOP CODE 1                                            | 69-71   |
|      | \(2\) FOR SC CONDITION?                                      | 72      |
|      | \(3\) FOR CONDITION RELATED TO AGENT ORANGE?                 | 73      |
|      | \(4\) FOR CONDITION RELATED TO IONIZING RADIATION?           | 74      |
|      | \(5\) EXPOSED TO ENVIRONMENTAL CONTAMINANTS?                 | 75      |
|      | \(6\) BLANK                                                  | 76      |
|      | \(7\) BLANK                                                  | 77      |

|      |                                                        |              |
|------|--------------------------------------------------------|--------------|
|      |                                                        |              |
| 20\. | SPECIAL SERVICES (CPT) DATA INPUT                      |              |
|      | (NOTE: WHEN THE "900" CODE IS ENTERED, THIS            |              |
|      | INFORMATION WILL TAKE THE PLACE OF AN ALLOWABLE STOP   |              |
|      | CODE IN THE SERIES OF 15 CODES THAT CAN BE TRANSMITTED |              |
|      | WITH EACH VISIT.)                                      |              |
|      |                                                        |              |
| A.   | SPECIAL SERVICES (CPT) DATA INPUT) 1 - 6               |              |
|      | \(1\) SPECIAL SERVICE CODE (900)                       | 3 CHARACTERS |
|      | \(2\) ASSOCIATED CLINIC (STOP CODE)                    | 3 CHARACTERS |
|      | \(a\) FOR SC CONDITION?                                |              |
|      | \(b\) FOR CONDITION RELATED TO AGENT ORANGE?           |              |
|      | \(c\) FOR CONDITION RELATED TO IONIZING RADIATION?     |              |
|      | \(d\) EXPOSED TO ENVIRONMENTAL CONTAMINANTS?           |              |
|      | \(e\) BLANK                                            |              |
|      | \(f\) BLANK                                            |              |
|      | \(3\) NUMBER OF CPT CODES TO FOLLOW                    | 1 CHARACTER  |
|      | \(4\) CPT CODE \#1                                     | 5 CHARACTERS |
|      | \(5\) CPT CODE \#2                                     | 5 CHARACTERS |
|      | \(6\) CPT CODE \#3                                     | 5 CHARACTERS |
|      | \(7\) CPT CODE \#4                                     | 5 CHARACTERS |
|      | \(8\) CPT CODE \#5                                     | 5 CHARACTERS |
|      |                                                        |              |
| 21\. | End of record indicator                                |              |

Responses for the questions regarding SC care, Agent Orange, etc., will be completed on applicable veterans as follows.

|               |                                      |
|---------------|--------------------------------------|
| STOP CODE | REQUIRED                         |
| 101           | YES                                  |
| 102           | YES                                  |
| 104-170       | NO                                   |
| 180           | YES                                  |
| 201-299       | YES                                  |
| 301-399       | YES                                  |
| 401-499       | YES                                  |
| 501-599       | YES                                  |
| 601-699       | YES                                  |
| 701-799       | YES                                  |
| 801-899       | YES                                  |
| 900           | \*See stop code of associated clinic |
| 999           | YES                                  |

  
2. Outpatient Encounter Data

As part of v5.3, a series of new files have been added to the Scheduling module to track and manage outpatient encounter information. The main file is the OUTPATIENT ENCOUNTER file (#409.68). This file will contain an entry for all checked out encounters. At this time, the file will not contain entries for future, cancelled, and no-show appointments.

If during the nightly status update process, it is determined that an encounter needs to be checked out but that action has not occurred, an entry is added to this file and given a status of ACTION REQUIRED. If the encounter is an appointment and it eventually is no-showed or cancelled, the entry will automatically be deleted.

The types of encounters stored in this file are appointments, credit stops, registration dispositions, and add/edit stop codes. NOTE: The data for these types of encounters is still stored in data structures in place before v5.3. The number of reports and other processes already using the older structures is too large to convert to the new structure at this time.

Other related data files containing encounter information are as follows. For more information, see section H - New Files.

OUTPATIENT CLASSIFICATION (#409.42) - service connected, Agent Orange, ionizing radiation, environmental contaminants

OUTPATIENT DIAGNOSIS (#409.43) - encounter diagnosis

OUTPATIENT PROVIDER (#409.44) - provider of care

OTHER CHANGES1. Clinic Stop Code Update

This release also modifies the CLINIC STOP file (#40.7) as follows.

New Clinic Stops

144 RADIONUCLIDE THERAPY

145 PHARM/PHYSIO NMP STUDIES

146 PET

215 SCI HOME CARE PROGRAM

319 GERIATRIC EVAL. & MGMT. (GEM)

320 ALZHEIMER'S/DEMENTIA CLINIC

321 GI ENDOSCOPY

322 WOMEN'S CLINIC

423 PROSTHETIC SERVICES

524 SEXUAL TRAUMA COUNSELING

573 RMS INCENTIVE THERAPY

574 RMS COMPENSATED WORK THERAPY

575 RMS VOCATIONAL ASSISTANCE

725 DOMICILIARY OUTREACH SERVICES

727 DOMICILIARY AFTERCARE - VA

> **NOTE:** These stop codes CANNOT be used UNTIL 10/1/93.

Inactivated Clinic Stops

511 NEUROBEHAVIORAL-INDIVIDUAL

559 NEUROBEHAVIORAL-GROUP

> **NOTE:** These stop codes CANNOT be used AFTER 9/30/93.

Clinic Stop Name Changes

202 RECREATION SERVICE to RECREATION THERAPY SERVICE

207 INCENTIVE THERAPY to RMS INCENTIVE THERAPY

208 COMPENSATED WORK THERAPY to RMS COMPENSATED WORK

THERAPY

213 VOCATIONAL ASSISTANCE to RMS VOCATIONAL ASSISTANCE

214 CORRECTIVE THERAPY to KINESIOTHERAPY

515 CWT/ILH INDIVIDUAL to CWT/TR-HCMI

518 CWT/ILH SUBSTANCE ABUSE to CWT/TR-SUBSTANCE ABUSE

2. Patient Profile

The Patient Profile MAS option under the Outputs menu has been modified to use the List Manager utility. This will allow the user to easily browse the MAS data using standard List Manager actions, such as "next" and "previous" screen. If desired, the user can also print the information. The following is a sample of the new patient profile screen. Notice that the Display Info action allows the user to view more detailed data about the patient.

> Patient Profile Jul 07, 1993 07:48:20 Page: 1 of 2

> Patient: ADTPATIENT,ONE (6789) 01/01/92 to 07/07/93 Outpatient

> Date of Birth: OCT 10, 1925 Marital Status: MARRIED

> Sex: MALE Religious Pref.: CATHOLIC

> SSN: 000456789 Occupation: DITCH DIGGER

> Current Means Test: REQUIRED

> Primary Eligibility: NSC

> Long ID: 000-45-6789 Short ID: 6789

> Other Eligibilities:

> COLLATERAL OF VET. VETERAN(Y/N): YES

> EMPLOYEE Type: NSC VETERAN

> + Enter ?? for more actions

> DI Display Info CP Change Patient CD Change Date Range

> Select Action: Next Screen// DI Display Info

> AE Add/Edits DD Dispositions

> AP Appointments MT Means Test

> DE Enrollments AL All

> Select Action:

  
A. New Options/Actions

NAME: SDAM PROVIDER/DIAGNOSIS REPORT

MENU TEXT: Provider/Diagnosis Report

DESCRIPTION: This new report sorts by division and outpatient encounter date. It also permits the selection of two additional sort levels by the user; provider, diagnosis, patient, clinic, or stop code. The printed report is formatted for 132 columns, so output to a terminal will wrap. The output contains the patient's name and last four digits of his/her SSN, the encounter date and time, clinic name and stop code, provider's and diagnostic codes. This report uses the Outpatient Encounter file (#409.68), Outpatient Provider file (#409.44), and the Outpatient Diagnosis file (#409.43).

NAME: SDCO APPT CHECK OUT

ITEM TEXT: Check Out

DESCRIPTION: This action permits the user to check out appointments through the Appointment Management screen. The first time through the checkout process, the user is asked if s/he wishes to make a follow-up appointment. The user is then taken through the checkout interview. The interview consists of pertinent questions related to checking out the appointment. The first questions asked in the interview are any required classifications. The classifications include those questions related to whether or not the treatment was service connected, Agent Orange related, ionizing radiation related, or environmental contaminant related. These questions will only be asked if they are applicable to the patient. The user cannot up-arrow out of these questions unless the site has set a site parameter which permits up-arrowing. The classifications are then followed by provider, diagnosis, and stop codes which are asked based on site parameters for the clinic. At the completion of the interview, the system will attempt to check the appointment out. If any required information is missing, the appointment will not be checked out. The user then has the option of viewing the Check Out screen.

The following is how the Check Out screen appears.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Check Out</strong> Jun 18, 1993 10:42:17 Page: 1 of 1</p>
<p>Patient: ADTPATIENT,ONE (6789) Clinic: CARDIOLOGY</p>
<p>Appointment Date/Time: Feb. 25, 1993 15:00 Checked Out: YES</p>
<p>CLASSIFICATION [Required]</p>
<p>1 Treatment for SC Condition: Not Applicable</p>
<p>2 Agent Orange Exposure : Not Applicable</p>
<p>3 Ionizing Radiation Exposure: YES</p>
<p>4 Environmental Contaminants : NO</p>
<p>PROVIDER [Required] DIAGNOSIS [Not Required]</p>
<p>1 ADTPROVIDER,ONE</p>
<p>Enter ?? for more actions</p>
<p>CD Check Out Date EC Edit Classification PD Patient Demographics</p>
<p>AP Appointment PR Provider Update RR Recharge Record</p>
<p>DC Discharge Clinic DX Diagnosis Update</p>
<p>AE Add/Edit IN Interview</p>
<p>Select Action: Next Screen//</p></td>
</tr>
</tbody>
</table>

All of the actions on the Check Out screen are available on the Appointment Management screen with the exception of the Check Out Date and Interview. As of 10/1/93, appointments must be checked out to receive workload credit.

> (See SDBUILD and SD PARM PARAMETERS under the Changed Options section of these release notes for more information regarding the provider, diagnosis, and stop code parameters.)

NAME: SDCO CHECK OUT DATE

ITEM TEXT: Check Out Date

DESCRIPTION: This action permits the user to change the checkout date/time associated with an appointment. If the appointment has already been checked in, the checkout date/time cannot be before the check in date/time.

NAME: SDCO CLINIC APPT

ITEM TEXT: Appointment

DESCRIPTION: This action permits the user to make a follow-up appointment for the patient from the Check Out screen.

NAME: SDCO DISCHARGE CLINIC

ITEM TEXT: Discharge Clinic

DESCRIPTION: This action permits the user to discharge a patient from a clinic. This action works the same as the existing Discharge from Clinic option.

NAME: SDCO ADD EDIT NEW

ITEM TEXT: Add/Edit

DESCRIPTION: This action permits the user to associate stop codes and CPTs with an appointment or disposition from the checkout menu. When a stop code or procedure is associated with an appointment, the information regarding appointment type, associated clinic, and eligibility for the appointment is automatically entered. Stop codes associated with an appointment or disposition do not need to be checked out. The required information for the stop code checkout is obtained from the associated appointment or disposition.

NAME: SDCO CLASSIFICATION

ITEM TEXT: Edit Classification

DESCRIPTION: This action permits the user to edit required classifications associated with regular appointments, stand-alone add/edits, and dispositions with a status of 10/10 VISIT or UNSCHEDULED. The classifications include those questions related to whether or not the treatment was service connected, Agent Orange related, ionizing radiation related or environmental contaminant related. These questions can only be answered if they are applicable to the patient and meet the criteria listed below.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Service</p>
<p>Connected</p>
</blockquote></td>
<td><blockquote>
<p>Asked for all service-connected veterans EXCEPT:</p>
<p>clinic stop codes 104-170</p>
<p>automatically YES for Class II Dental Apts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Agent Orange</p>
</blockquote></td>
<td><blockquote>
<p>Asked for all veterans who claim exposure EXCEPT:</p>
<p>clinic stop codes 104-170</p>
<p>SC LESS THAN 50% who say YES to service connected for the encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ionizing Radiation</p>
</blockquote></td>
<td><blockquote>
<p>Asked for all veterans who claim exposure EXCEPT:</p>
<p>clinic stop codes 104-170</p>
<p>SC LESS THAN 50% who say YES to service connected for the encounter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Environmental Contaminants</p>
</blockquote></td>
<td><blockquote>
<p>Asked for all veterans and who claim exposure and active duty non-veterans EXCEPT:</p>
<p>clinic stop codes 104-170</p>
<p>SC LESS THAN 50% who say YES to service connected for the encounter</p>
<p>Note: Active duty non-veterans include patients with an eligibility of Other Federal Agency and one of the following periods of service: Air Force - Active Duty, Army - Active Duty, Coast Guard - Active Duty, Navy, Marine - Active Duty, and Operation Desert Shield.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The classifications can also be edited through the Appointment Management Screen for appointments. All required classifications must be answered to complete the checkout process. The user is not allowed to up-arrow out of these questions unless the user has already answered these questions or the site has set the ALLOW UP-ARROW OUT OF CLASS. parameter to YES.

> When answering the service-connected classification, a \<?\> can be entered to obtain a list of the rated disabilities.

> (See SD PARM PARAMETERS under the Changed Options section of these release notes for more information regarding the ALLOW UP-ARROW OUT OF CLASS. parameter.)

NAME: SDCO PROVIDER

ITEM TEXT: Provider Update

DESCRIPTION: This action permits the user to add, edit, or delete providers associated with an appointment, a stand-alone add/edit, or disposition. In the Set up a Clinic option, providers associated with a particular clinic can be entered. These providers will then be displayed as help when initially updating the provider. A default provider can also be specified through the clinic parameters. The provider can also be updated through the Appointment Management screen provided the appointment has a checkout date/time. At the completion of the provider update, if the encounter has not already been checked out, the system will automatically attempt to check it out.

> (See SDBUILD under the Changed Options section of these release notes for more information regarding the provider parameter for setting up provider help for a clinic.)

NAME: SDCO DIAGNOSIS

ITEM TEXT: Diagnosis Update

DESCRIPTION: This action permits the user to add, edit, or delete diagnoses associated with an appointment, a stand-alone add/edit, or disposition. In the Set up a Clinic option, diagnoses associated with a particular clinic can be entered. These diagnoses will then be displayed as help when initially updating the diagnosis. A default diagnosis can also be specified through the clinic parameters. The diagnosis can also be updated through the Appointment Management screen provided the appointment has a checkout date/time. At the completion of the diagnosis update, if the encounter has not already been checked out, the system will automatically attempt to check it out.

> (See SDBUILD under the Changed Options section of these release notes for more information regarding the diagnosis parameter for setting up diagnosis help for a clinic.)

NAME: SDCO INTERVIEW

ITEM TEXT: Interview

DESCRIPTION: This action permits the user to answer all pertinent questions related to checking out an appointment, stand-alone add/edit, or disposition. The following questions could be asked as part of the interview.

> follow-up appointment which is only asked when checking out an appointment

> required classifications which include service connected, Agent Orange exposure, ionizing radiation exposure, and environmental contaminant exposure

> provider and diagnosis which are optionally asked based on site parameters for the clinic and disposition

> stop codes and procedures which are optionally asked based on site parameters for the clinic and disposition

> At the completion of the interview, if the encounter has not already been checked out, the system will automatically attempt to check it out.

> (See SDBUILD and SD PARM PARAMETERS under the Changed Options section of these release notes for more information regarding the provider, diagnosis, and stop code parameters.)

NAME: SDCO PATIENT DEMOGRAPHICS

ITEM TEXT: Patient Demographics

DESCRIPTION: This action permits the user to update a patient's permanent and temporary address. Patient demographics is also available through the Appointment Management screen.

NAME: SDAM RT MENU

ITEM TEXT: Record Tracking

DESCRIPTION: This menu protocol contains the record tracking actions available on the Appointment Management and Check Out screens.

NAME: SDAM RT MAS-CHART-PROFILE

ITEM TEXT: Profile of Charts

DESCRIPTION: MAS application specific inquiry for viewing records.

NAME: SDAM RT MAS-CHART-REQUEST

ITEM TEXT: Chart Request

DESCRIPTION: MAS application specific record request.

NAME: SDAM RT MAS-FILL-NEXT

ITEM TEXT: Fill Next Clinic Request

DESCRIPTION: Allows clinics to recharge charts to next clinic.

NAME: SDAM RT MAS-RE-CHARGE

ITEM TEXT: Recharge a Chart

DESCRIPTION: MAS application specific action for charging a chart to another borrower.

NAME: SDAM DELETE CHECK OUT

ITEM TEXT: Delete Check Out

DESCRIPTION: This action permits the user to delete the checkout for appointments with a checkout date/time. The user must hold the SD SUPERVISOR key to use this action. When the checkout is deleted, any classifications, providers, diagnoses, and stop codes associated with the appointment are also deleted.

B. Changed Options

NAME: SDAM APPT MGT

MENU TEXT: Appointment Management

DESCRIPTION: This option has been modified to include several new actions which are listed below. In addition to these new actions, the display type actions (i.e., next screen, previous screen) are still available, but are not listed on the screen. Help is available by entering \<??\> which will list all the available actions. In this release, when a clinic is selected, the appointments displayed for the selected date range will be those with No Action Taken or a combination status with "Action Required" appended on to it.

<u>Check Out Actions</u>

Check Out

Edit Classifications

Provider Update

Diagnosis Update

Delete Check Out

<u>Other Actions</u>

Discharge Clinic

Add/Edit

Recharge Record

Patient Demographics

NAME: SD APPT CHECK IN/OUT

MENU TEXT: Appointment Check-In/Check-Out

DESCRIPTION: This option has been modified to include checkout. The user will be prompted for either check in or checkout, depending on the appointment date and which action is required. Prior to 10/1/93, an appointment can either be checked in or checked out to receive workload credit. Effective 10/1/93, all appointments must be checked out to receive workload credit. The synonym has also been changed for this option from CI to CK.

> (See SDCO APPT CHECK OUT under the New Options/Actions section of these release notes for more information regarding the checkout process.)

NAME: SDADDEDIT

MENU TEXT: Add/Edit Stop Codes

DESCRIPTION: This option has been modified for checkout. When a stop code or procedure is associated with an appointment, the information regarding appointment type, associated clinic, and eligibility for the appointment is automatically entered. Stop codes associated with an appointment or disposition do not need to be checked out. The required information for the stop code checkout is obtained from the associated appointment or disposition encounter. Stop codes not associated with an appointment or disposition do need to be checked out.

NAME: SDAPPEND

MENU TEXT: Append Ancillary Test to Appt.

DESCRIPTION: This option has been modified for checkout. Ancillary tests cannot be added to an appointment that has been checked out. Instead the tests should be added using the Add/Edit stop code functionality. If an appointment has an ancillary test associated with it, an add/edit will automatically be created when the appointment is checked out.

NAME: SD CANCEL APPOINTMENT

MENU TEXT: Cancel Appointment

DESCRIPTION: This option has been modified for checkout. Appointments that have been checked out cannot be cancelled. The checkout must first be deleted, then the appointment can be cancelled. To delete the checkout requires the SD SUPERVISOR key.

NAME: SDI

MENU TEXT: Check-in/Unsched. Visit

DESCRIPTION: This option has been modified for checkout.

NAME: SDDELANCIL

MENU TEXT: Delete Ancillary Test for Appt.

DESCRIPTION: This option has been modified for checkout. Ancillary tests cannot be deleted from an appointment that has been checked out. Instead the tests should be deleted using the Add/Edit stop code functionality. If the appointment checkout is deleted, any add/edits associated with the appointment will automatically be deleted.

NAME: SDM

MENU TEXT: Make Appointment

DESCRIPTION: This option has been modified for checkout. When making a past appointment (prior to today), the appointment will be checked in or checked out based on the appointment date and which action is required. When making an appointment earlier on the same day, the user will be prompted for either check in or checkout, depending on the appointment date and whether or not checkout is required. Multiple appointment bookings are also affected.

NAME: SDNOSHOW

MENU TEXT: No-Shows

DESCRIPTION: This option has been modified for checkout. Appointments that have been checked out cannot be no-showed. The checkout must first be deleted, then the appointment can be no-showed. To delete the checkout requires the SD SUPERVISOR key.

NAME: SDGENAMISSAMP

MENU TEXT: Generate OPC File

DESCRIPTION: This option has been modified to capture the new classification information collected in checkout. The classification information includes whether or not the treatment was service connected, Agent Orange related, ionizing radiation related, or environmental contaminant related.

NAME: SD OPCDEL

MENU TEXT: OPC Delete Visit Code Sheet

DESCRIPTION: This option has been modified to capture the new classification information collected in checkout. The classification information includes whether or not the treatment was service connected, Agent Orange related, ionizing radiation related, or environmental contaminant related.

NAME: SD OPC DV OUTPUT

MENU TEXT: OPC Variable Length Record Output

DESCRIPTION: This option has been modified to print the new classification information collected in checkout. The classification information includes whether or not the treatment was service connected, Agent Orange related, ionizing radiation related, or environmental contaminant related.

NAME: SDLIST

MENU TEXT: Appointment List

DESCRIPTION: This option has been modified to indicate what required information is needed in order to check out the encounter and subsequently receive OPC credit.

NAME: SDAM RPT MANAGEMENT

MENU TEXT: Appointment Management Report

DESCRIPTION: This option has been modified to indicate what required information is needed in order to check out the encounter. If the encounter has the indicator "This encounter is associated with an appointment", the encounter does not need to be checked out. When the associated appointment or disposition is checked out, any associated encounters will also be checked out.

NAME: SDCLINIC

MENU TEXT: Clinic Profile

DESCRIPTION: This option has been modified to print the checkout clinic parameters.

NAME: SDPATIENT

MENU TEXT: Patient Profile MAS

DESCRIPTION: This option has been modified to use the List Manager utility. The following is a summary of the actions available using this option.

> DI - Display Info

> Allows selection of appointments, add/edits, enrollments, Means Test, and dispositions. Selection of ALL information is also available.

> AE - Add/Edits

> This will display information on add/edit appointments. You may select either all add/edits or add/edits for a specified stop code.

> AP - Appointments

> This will display information on appointments. You may select either all appointments or appointments for a specific clinic.

> DE - Enrollments

> This will display information on enrollments. You may select either all enrollments or enrollments to a specific clinic. You may select active enrollments only to either all or specified clinic.

> DD - Dispositions

> This will display information on dispositions. You may select all dispositions.

> MT - Means Test

> This will display information on Means Test. You may select either all Means Test information or a specified Means Test.

> AL - All

> This will display information on add/edits, appointments, enrollments, dispositions, and Means Test.

NAME: SD PARM PARAMETERS

MENU TEXT: Scheduling Parameters

DESCRIPTION: This option has been modified to include several new parameters for checkout.

> ALLOW UP-ARROW OUT OF CLASS.

> Enter YES to allow users to up-arrow out of the classification questions. The classification questions are required for workload credit. Allowing the user to exit without answering these questions could result in additional work at a later time to track down the record and determine the answer to these questions. This parameter effects appointments, stand-alone add/edits, and dispositions.

> ASK DIAGNOSIS ON DISPOSITION

> When checking out a patient during disposition, should the user be prompted for diagnosis? If this field is set to YES/REQUIRED, the user will be prompted for diagnosis during the checkout interview process. A diagnosis must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for diagnosis during the checkout interview process. The diagnosis does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for diagnosis during the checkout interview process. Regardless of how the parameter is set, the diagnosis can be entered through the Check Out screen.

> ASK PROVIDER ON DISPOSITION

> When checking out a patient during disposition, should the user be prompted for provider? If this field is set to YES/REQUIRED, the user will be prompted for provider during the checkout interview process. A provider must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for provider during the checkout interview process. The provider does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for provider during the checkout interview process. Regardless of how the parameter is set, the provider can be entered through the Check Out screen.

> ASK STOP CODES ON DISPOSITION?

> During disposition, should the user be prompted for stop codes? If this field is set to YES, the user will be prompted for stop codes. If the status of the disposition is a 10/10 VISIT or UNSCHEDULED, the user will be prompted for stop codes during the checkout interview process. If the status of the disposition is APPLICATION WITHOUT EXAM, the user will be prompted for stop codes at the end of the disposition process. If the status of the disposition is a 10/10 VISIT or UNSCHEDULED, the stop codes can also be entered through the Check Out screen. Those entered through the Check Out screen are automatically associated with the disposition.

NAME: SDBUILD

MENU TEXT: Set up a Clinic

DESCRIPTION: This option has been modified to include several new clinic set-up parameters which are used when checking out an appointment or a stand-alone add/edit.

> ASK FOR CHECK IN/OUT TIME \<modified parameter\>

> This parameter, which controls whether or not the date/time is automatically entered by the system or entered by the user, has been modified to include checkout.

> New Parameters

> ASK PROVIDER AT CHECK OUT

> When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for provider? If this field is set to YES/REQUIRED, the user will be prompted for provider during the checkout interview process. A provider must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for provider during the checkout interview process. The provider does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for provider during the checkout interview process. Regardless of how the parameter is set, the provider can be entered through the Check Out screen or the Appointment Management screen.

> PROVIDER

> Enter in this field the providers associated with this clinic. These providers will then be displayed when updating the provider through Appointment Management or Check Out to assist the user in entering the correct provider. A default provider can also be specified.

> ASK DIAGNOSIS AT CHECK OUT

> When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for diagnosis? If this field is set to YES/REQUIRED, the user will be prompted for diagnosis during the checkout interview process. A diagnosis must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for diagnosis during the checkout interview process. The diagnosis does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for diagnosis during the checkout interview process. Regardless of how the parameter is set, the diagnosis can be entered through the Check Out screen or the Appointment Management screen.

> DIAGNOSIS

> Enter in this field the diagnoses associated with this clinic. These diagnoses will then be displayed when updating the diagnosis through Appointment Management or Check Out to assist the user in entering the correct diagnosis. A default diagnosis can also be specified.

> ASK STOP CODES AT CHECK OUT

> When checking out a patient for an appointment, should the user be prompted for stop codes? If this field is set to YES, the user will be prompted for stop codes during the checkout interview process. If this field is set to NO or is not entered, the user will not be prompted for stop codes during the checkout interview process. Stop codes can also be entered through the Check Out screen or the Appointment Management screen. They can either be entered as stand-alone add/edits or associated with an appointment.

> STOP CODE MAIL GROUP

> This mail group receives the notifications generated by the automatic entry of stop codes in the Scheduling package. This lists errors only.

NAME: SDROUT

MENU TEXT: Routing Slips

DESCRIPTION: This option has been modified to print the classification questions. It has also been modified to print routing slips for one, many, or all clinics. In the prior version, one could only print routing slips for all clinics.

C. Deleted Options

NAME: SD APPT STATUS

MENU TEXT: Appointment Status Update in Event Driver

REASON FOR DELETION: This option exists as an action in the protocol file. Its existence in the option file was strictly for portability. Protocols are now transported independent of the option file.

NAME: SD OERR CANCEL APPT

MENU TEXT: Cancel Clinic Appt

REASON FOR DELETION: This option exists as an action in the protocol file. Its existence in the option file was strictly for portability. Protocols are now transported independent of the option file.

NAME: SD OERR MAKE APPT

MENU TEXT: Schedule Clinic Appt

REASON FOR DELETION: This option exists as an action in the protocol file. Its existence in the option file was strictly for portability. Protocols are now transported independent of the option file.

D. New Routines

|           |          |                                  |
|-----------|----------|----------------------------------|
| SDAMODO\* | SDCO\*   | SDPP\* (All are new except SDPP) |
| SDAMBAE6  | SDAMEVT0 | SDAMEVT2                         |
| SDAMEVT3  | SDAMEVT4 | SDAMEP4                          |
| SDAMEX1   | SDAM011  | SDAMQ3                           |
| SDAMQ4    | SDAMQ5   | SDC4                             |
| SDVLT     | SDV53\*  | SDVSIT\*                         |
| SDAMOS0   | SDAMOS1  | SDSTP\*                          |

E. Deleted Routines

|       |         |         |       |
|-------|---------|---------|-------|
| SDPP1 | SDV52PP | SDV52PT | SDI\* |

F. Suggested Routines for Mapping (DSM)

|           |        |          |          |
|-----------|--------|----------|----------|
| SDAMBAE\* | SDDIV  | SDROUT\* | SDM\*    |
| SDACS\*   | SDBT\* | SDM1T\*  | SDX\*    |
| SDAM\*    | SDUL\* | SDCO\*   | SDVSIT\* |

G. File (DD) Changes

MAS PARAMETERS (#43)

> Field 219 ASK PROVIDER ON DISPOSITION

> When checking out a patient during disposition, should the user be prompted for provider? If this field is set to YES/REQUIRED, the user will be prompted for provider during the checkout interview process. A provider must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for provider during the checkout interview process. The provider does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for provider during the checkout interview process. Regardless of how the parameter is set, the provider can be entered through the Check Out screen.

> Field 220 ASK DIAGNOSIS ON DISPOSITION

> When checking out a patient during disposition, should the user be prompted for diagnosis? If this field is set to YES/REQUIRED, the user will be prompted for diagnosis during the checkout interview process. A diagnosis must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for diagnosis during the checkout interview process. The diagnosis does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for diagnosis during the checkout interview process. Regardless of how the parameter is set, the diagnosis can be entered through the Check Out screen.

> Field 221 STOP CODE MAIL GROUP

> This group receives the bulletins generated by the automatic entry of stop codes in the Scheduling package. This bulletin generates errors only.

> Field 222 OPC FY94 FORMAT DATE

> This field indicates the date the new FY94 OPC format takes effect. Once v5.3 is released, this date will be 10/1/93. For Alpha and Beta testing, however, this date should be set before 10/1/93. If this field is blank, 10/1/93 is used by OPC generation.

> Field 223 DATE CHECK OUT REQUIRED

> This field indicates the date the site must start checking out appointments, stop code additions (add/edits), and registrations (1010 and unscheduled). Once v5.3 is released, this date will be 10/1/93. For Alpha and Beta testing, however, this date should be set before 10/1/93.

> Field 224 ALLOW UP-ARROW OUT OF CLASS.

> Enter YES to allow users to up-arrow out of the classification questions. The classification questions are required for workload credit. Allowing the user to exit without answering these questions could result in additional work at a later time to track down the record and determine the answer to these questions.

HOSPITAL LOCATION (#44)

> Field 26 ASK PROVIDER AT CHECK OUT

> When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for provider? If this field is set to YES/REQUIRED, the user will be prompted for provider during the checkout interview process. A provider must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for provider during the checkout interview process. The provider does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for provider during the checkout interview process. Regardless of how the parameter is set, the provider can be entered through the Check Out screen or the Appointment Management screen.

> Field 27 ASK DIAGNOSIS AT CHECK OUT

> When checking out a patient for an appointment or a stand-alone add/edit with an associated clinic, should the user be prompted for diagnosis? If this field is set to YES/REQUIRED, the user will be prompted for diagnosis during the checkout interview process. A diagnosis must be entered to complete the checkout process and receive workload credit. If this field is set to YES/NOT REQUIRED, the user will be prompted for diagnosis during the checkout interview process. The diagnosis does NOT have to be entered to complete the checkout process and receive workload credit. If this field is set to NO or is not entered, the user will not be prompted for diagnosis during the checkout interview process. Regardless of how the parameter is set, the diagnosis can be entered through the Check Out screen or the Appointment Management screen.

> Field 28 ASK STOP CODES AT CHECK OUT

> When checking out a patient for an appointment, should the user be prompted for stop codes? If this field is set to YES, the user will be prompted for stop codes during the checkout interview process. If this field is set to NO or is not entered, the user will not be prompted for stop codes during the checkout interview process. Stop codes can also be entered through the Check Out screen or the Appointment Management screen. They can either be entered as stand-alone add/edits or associated with an appointment.

> Field 2600 PROVIDER

> Enter the providers associated with this clinic. These providers will then be displayed when updating the provider through Appointment Management or checkout to assist the user in entering the correct provider.

> Field .01 PROVIDER

> Enter the providers associated with this clinic. These providers will then be displayed when updating the provider through Appointment Management or checkout to assist the user in entering the correct provider.

> Field .02 DEFAULT PROVIDER

> Enter YES in this field if the provider is the default for this clinic; otherwise, enter NO.

> Field 2700 DIAGNOSIS

> Enter the diagnoses associated with this clinic. These diagnoses will then be displayed when updating the diagnosis through Appointment Management or checkout to assist the user in entering the correct diagnosis.

> Field .01 DIAGNOSIS

> Enter the diagnoses associated with this clinic. These diagnoses will then be displayed when updating the diagnosis through Appointment Management or checkout to assist the user in entering the correct diagnosis.

> Field .02 DEFAULT DIAGNOSIS

> Enter YES in this field if the diagnosis is the default for this clinic; otherwise, enter NO.

H. New Files

The following new files should have the same security as the HOSPITAL LOCATION file (#44) or the SCHEDULING VISITS file (#409.5). This is usually "Dd" unless something different has been assigned locally.

> Outpatient Classification (#409.42)

> Outpatient Diagnosis (#409.43)

> Outpatient Provider (#409.44)

> Outpatient Encounter (#409.68)

OUTPATIENT CLASSIFICATION TYPE (#409.41)

This table file contains types of outpatient classifications. These include Service Connected, Agent Orange Exposure, Ionizing Radiation Exposure, and Environ-mental Contaminants Exposure. If an entry needs to be added, modified, or deleted, a patch will be issued instructing the site how to make the change. Otherwise, this table should not be edited in anyway by the site.

> Field .001 NUMBER

> Enter the internal entry number associated with this outpatient classification type.

> Field .01 NAME

> Enter the name of the outpatient classification type.

> Field .02 PROMPT

> Enter the prompt to be used when this outpatient classification is asked. If this field is not defined, the NAME field will be used. For example, this field might contain the following: "Was treatment for an SC condition".

> Technical Notes: This field is used as DIR("A") when prompting for outpatient

> classification.

> Field .03 INPUT TYPE

> Enter the input type to be used when this outpatient classification is asked.

> Technical Notes: This field is used as DIR(0) when prompting for outpatient classification.

> Field .04 DEFAULT

> Enter the default to be used when this outpatient classification is asked. For example, this field might contain the following if the input type is YES/NO: NO.

> Technical Notes: This field is used as DIR("B") when prompting for outpatient classification.

> Field .05 REQUIRED

> Enter whether or not a response is required when this outpatient classification is asked.

> Field .06 DISPLAY NAME

> Enter the text to be displayed on the Check Out screen.

> Field .07 ABBREVIATION

> Enter the abbreviation for the outpatient classification type. For example, AO for Agent Orange Exposure.

> Field 1 SCREEN

> Enter MUMPS code to be used as a screen to determine whether or not a patient should be asked this outpatient classification type.

> Technical Notes: The following variables are supported through the outpatient classification function calls.

> DFN Patient file IEN

> SDOE Outpatient Encounter file IEN \[Optional\]

> Field 2 INPUT PARAMETERS

> Enter the input parameters to be used when this outpatient classification is asked. For example, this field might contain the following if the input type is a SET: 1:MARRIED;2:SINGLE.

> Technical Notes: This field is used as DIR(0) when prompting for outpatient

> classification.

> Field 50 DESCRIPTION

> Enter the description associated with this outpatient classification type.

> Field 75 EFFECTIVE DATE

> Enter the effective date of the outpatient classification type.

> Field .01 EFFECTIVE DATE

> Enter the effective date of the outpatient classification type.

> Field .02 ACTIVE

> Enter whether or not the effective date of the outpatient classification is active.

OUTPATIENT CLASSIFICATION (#409.42)

This file contains outpatient classifications associated with outpatient encounters.

> Field .01 TYPE

> This field contains the outpatient classification type.

> Field .02 OUTPATIENT ENCOUNTER

> This field contains the outpatient encounter associated with this outpatient classification.

> Field .03 VALUE

> This field contains the value of this outpatient classification.

OUTPATIENT DIAGNOSIS (#409.43)

This file contains outpatient diagnoses associated with outpatient encounters.

> Field .01 DIAGNOSIS

> This field contains the outpatient diagnosis.

> Field .02 OUTPATIENT ENCOUNTER

> This field contains the outpatient encounter associated with this outpatient diagnosis.

OUTPATIENT PROVIDER (#409.44)

This file contains outpatient providers associated with outpatient encounters.

> Field .01 PROVIDER

> This field contains the outpatient provider.

> Field .02 OUTPATIENT ENCOUNTER

> This field contains the outpatient encounter associated with this outpatient provider.

OUTPATIENT CLASSIFICATION STOP CODE EXCEPTION (#409.45 )

This table file contains stop codes exempted from the outpatient classification questions. If an entry needs to be added, modified, or deleted, a patch will be issued instructing the site how to make the change. Otherwise, this table should not be edited in anyway by the site.

> Field .01 STOP CODE NUMBER

> Enter the clinic stop code exempted from the outpatient classification questions.

> Field 75 EFFECTIVE DATE

> Enter the effective date of the outpatient classification stop code exception.

> Field .01 EFFECTIVE DATE

> Enter the effective date of the outpatient classification stop code exception.

> Field .02 ACTIVE

> Enter whether or not the effective date of the outpatient classification stop code exception is active.

OUTPATIENT ENCOUNTER (#409.68)

This file contains all outpatient encounters since 10/1/93 that have been successfully checked out or need to be checked out. The types of encounters that caused entries to be added to this file are appointments, add/edit stop codes, and dispositions.

If the encounter needs to be checked out, it will have a status of PENDING ACTION. The site will not receive workload credit if the status remains PENDING ACTION. PENDING ACTION includes both ACTION REQUIRED and NO ACTION TAKEN statuses. If the encounter has been no-showed or cancelled, it will NOT be in this file.

Inpatient encounters will always have a status of INPATIENT APPOINTMENT. Appointments made for non-count clinics will always have a status of NON-COUNT.

> Field .01 DATE

> This field contains the date and time when an outpatient encounter occurred.

> Field .02 PATIENT

> This field contains the patient associated with the encounter.

> Field .03 CLINIC STOP CODE

> This field contains the clinic stop code associated with the outpatient encounter.

> Field .04 LOCATION

> This field contains the location (usually a clinic) where the encounter took place. This field is optional.

> Field .05 VISIT FILE ENTRY

> This field indicates the VISIT file entry associated with this encounter. This field is optional and will only be filled in if the site is running the Visit Tracking module.

> Field .06 PARENT ENCOUNTER

> This field associates the current encounter with a parent encounter. For example, if there are add/edit stop codes associated with an appointment, then all the add/edit encounter entries will have this parent field filled in with the appointment encounter. This relationship allows the checkout software to use the checkout information of the appointment for the add/edits.

> Field .07 CHECK OUT PROCESS COMPLETION

> This field indicates the checkout process has been successfully completed for this outpatient encounter.

> Field .08 ORIGINATING PROCESS TYPE

> This field indicates the type of process that created this encounter. The types are 1) appointment, 2) add/edit stop code, 3) disposition.

> Field .09 EXTENDED REFERENCE

> This field indicates the internal multiple entry of the originating process that created the encounter. NOTE: This field will eventually be deleted when the old encounter data structures are removed as part of the scheduling redesign.

> The reference mapping is as follows

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Originating</p>
<p>Process</p></td>
<td>Global Reference</td>
</tr>
<tr class="even">
<td>1 - appointments</td>
<td>^SC(&lt;LOCATION&gt;,"S",&lt;DATE/TIME&gt;,1,&lt;EXTERNAL REF&gt;)</td>
</tr>
<tr class="odd">
<td>2 - add/edits</td>
<td>^SDV(&lt;DATE/TIME&gt;,"CS",&lt;EXTERNAL REFERENCE&gt;)</td>
</tr>
<tr class="even">
<td>3 - dispositions</td>
<td>^DPT(&lt;PATIENT&gt;,"DIS",&lt;EXTERNAL REFERENCE&gt;)</td>
</tr>
<tr class="odd">
<td>4 - credit stop</td>
<td>^SC(&lt;LOCATION&gt;,"S",&lt;DATE/TIME&gt;,1,&lt;EXTERNAL REF&gt;)</td>
</tr>
</tbody>
</table>

> Field .1 APPOINTMENT TYPE

> This field contains the appointment type associated with the outpatient encounter.

> Field .11 MEDICAL CENTER DIVISION

> This field indicates the medical center division where the encounter took place.

> Field .12 STATUS

> This field indicates the status of the encounter. Future, no-showed, and cancelled appointments are not included in this file at the present time. Currently, the only possible statuses are the following.

> CHECKED OUT

> PENDING ACTION

> INPATIENT APPOINTMENT

> NON-COUNT

> Field .13 ELIGIBILITY OF ENCOUNTER

> This field contains the eligibility associated with the encounter.

<u>  
</u>I. New Security Keys

SD SUPERVISOR

This key will permit the user to perform various supervisor functions. Currently, this key is only attached to the Delete Check Out action.

J. New Mail Groups

None

K. New Bulletins

None

L. E-Mail Notifications

Stop Code Background Errors

This will be sent to the Stop Code mail group designated in the Scheduling parameters. It will be generated for any errors that occur when a package calls the utility to stuff stop codes in the Scheduling package.

M. Comments

See Introduction for comments.