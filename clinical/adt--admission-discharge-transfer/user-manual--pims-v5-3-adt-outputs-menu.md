---
title: PIMS Version 5.3 User Manual - ADT Outputs Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: ADT Outputs Menu
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
description: - [PIMS V. 5.3 ADT Module User Manual ADT Outputs Menu](#pims-v-53-adt-module-user-manual-adt-outputs-menu) Overview 10/10 Print ADT Third Party Output Menu > Patient Review Document > Review Document by Admission Range > Veteran Patient Insurance Information AMIS Reports Menu > AMIS 334-341 Reports
audience: 
keywords: 
  - report
  - date
  - patient
  - patients
  - disposition
  - test
  - whose
  - amis
  - means
  - listing
page_count: 0
word_count: 11579
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 7
revision_newest: 04/28/21
revision_oldest: 11/18/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adto_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adto_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

# PIMS V. 5.3 ADT Module User Manual ADT Outputs Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PIMS V. 5.3 ADT Module User Manual ADT Outputs Menu](#pims-v-53-adt-module-user-manual-adt-outputs-menu)
Overview
10/10 Print
ADT Third Party Output Menu
> Patient Review Document
> Review Document by Admission Range
> Veteran Patient Insurance Information
AMIS Reports Menu
> AMIS 334-341 Reports
> AMIS 345-346 Reports
> AMIS 401-420 Reports
Bed Availability
Disposition Outputs Menu
> Disposition Time Processing Statistics
> Log of Dispositions
> Summary of Dispositions
Enrollment Reports
> Enrolled Veterans Report
> Pending Applications for Enrollment
> Enrollees by Status, Priority, Preferred Facility
> Upcoming Appointments without Enrollment
> EGT Impact Report
> Non-Treating Preferred Facility Clean up
> Former OTH Patient Eligibility Change Report
> Former OTH Patient Detail Report
Gains and Losses (G&L Sheet)
Inconsistent Data Elements Report
Inpatient/Lodger Report Menu
> Absence List
> ASIH Listing
> Current Lodger List
> Female Inpatient List (Current)
> Historical Female Inpatient List
> Historical Inpatient Listing
> Inpatient Listing
> Inpatient Roster
> Insurance List of UNKNOWNs for Inpatients
> Lodgers for a Date Range
> Patient Movement List
> Religion List for Inpatients
> Seriously Ill Inpatient Listing
> Treating Specialty Inpatient Information
Means Test Outputs
> Duplicate Spouse/Dependent SSN Report
> Hardship Review Date
> List Required/Pending Means Tests
> Means Test Indicator of 'U' Report
> Means Test Specific Income Amount Report
> Means Test Specific Income Less Threshold Report
> Means Test w/Previous Year Threshold
> Patients Who Have Not Agreed To Pay Deductible
> Required Means Test At Next Appointment
N/T Radium Treatment Pending Verification List
Pending/Open Disposition List
Print Patient Label
Scheduled Admission Statistics
Scheduled Admissions List
Treating Specialty Print
VBC Form By Admission Date
VBC Form for Specific Patient
Waiting List Output
Z07 Build Consistency Check
Revision History
Initiated on 11/18/04
| Date | Description (Patch \# if applic.)                                                                                                                                                                                         | Project Manager | Technical Writer |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------|
| 04/28/21 | DG\*5.3\*1034: Updated Former OTH Patient Eligibility Change Report and Former OTH Patient Detail Reports under Enrollment Reports Menu option to include patient’s Episodes of Care (Oupatient,Inpatient, and Prescriptions) | VA PM               | Liberty IT Solutions |
| 10/25/18 | DG\*5.3\*958 – Updated the "<u>Religion List for Inpatients</u>" section to note that the Patient ID# is now only the last four digits of the SSN.                                                                            | REDACTED            | REDACTED             |
| 8/14/08  | Minor Formatting Changes                                                                                                                                                                                                      | REDACTED            | REDACTED             |
| 7/11/07  | DG\*5.3\*653 – Enrollment VistA Changes Release 1 (EVC R1) – Added Z07 Build Consistency Check option                                                                                                                         | REDACTED            | REDACTED             |
| 8/12/05  | DG\*5.3\*624 – 10-10EZ 3.0 Enhancements                                                                                                                                                                                       | REDACTED            | REDACTED             |
| 1/20/05  | Added documentation for Non-Treating Preferred Facility Clean up and Duplicate Spouse/Dependent SSN Report options                                                                                                            |                     | REDACTED             |
| 11/18/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data                                                                                                                                                           | REDACTED            | REDACTED             |
Overview
The ADT Outputs Menu provides the software necessary to produce a variety of reports related to the admission, discharge, transfer function. The following is a brief description of the options included in this menu.
10/10 Print
This option is used to print 10-10 forms for patients previously registered for care. If data for the patient does not exist in the VISTA patient database, a message displays informing the user that the forms will not be printed.
ADT Third Party Output Menu
> Patient Review Document
> This option is used to print Third Party Review Form by patient name and admission date specifications.
> Review Document by Admission Range
> This option is used to print Third Party Review Form for each patient admitted within a specified date range.
> VETERAN Patient Insurance Information
> This option provides insurance information on veteran patients.
AMIS Reports Menu
> AMIS 334-341 REPORTS
> This option is used to print the AMIS segments that record admission-discharge-transfer activity.
> AMIS 345-346 REPORTS
> This option is used to print the AMIS segments that record the activity of the VA Nursing Home Units and Domiciliary Units.
> AMIS 401-420 REPORTS
> This option is used to sort and print patient registrations by veteran category and disposition type.
Bed Availability
This option provides a list of available rooms/beds on selected ward(s).
Overview
Disposition Outputs Menu
> Disposition Time Processing Statistics
> This option provides a statistical breakdown by disposition action of the number of patients dispositioned within various time frames.
> Log of Dispositions
> This option provides a listing of patient disposition records within a specified time frame. All dispositions may be included or just those pending.
> SUMMARY OF DISPOSITIONS
> This option provides a summary report by disposition action of the number of 10/10 visits, unscheduled visits, and applications without exam.
ENROLLMENT REPORTS
> ENROLLED VETERANS REPORT
> This option is used to produce the enrolled veterans report, which contains a summary of the number of patients in each enrollment priority group.
> pENDING APPLICATIONS FOR ENROLLMENT
> This option is used to generate a list of patients with enrollment statuses of unverified and pending for selected facilities within a specified date range.
> ENROLLEES BY STATUS, PRIORITY, PREFERRED FACILITY
> This option is used to produce a report that provides counts of patients by preferred facility, enrollment status, and enrollment priority.
> UPCOMING APPOINTMENTS WITHOUT ENROLLMENT
> This option is used to generate a report of patients with future appointments who are not enrolled and do not have pending enrollment applications.
> EGT IMPACT REPORT
> This option provides four separate reports concerning veterans who are affected by an EGT change.
> NON-TREATING PREFERRED FACILITY CLEAN UP
> This option is used to identify all patients that have a non-treating preferred facility on file.
> FORMER OTH PATIENT ELIGIBILITY CHANGE REPORT
> This option is used to identify all Former Service Members whose has been adjudicated by VBA.
> FORMER OTH PATIENT DETAIL REPORT
> This option provides current eligibility and episodes of care (outpatient, inpatient, and prescriptions) provided to Former Service Members with Other Than Honorable during pending VBA adjudication period.
Overview
GAINS & LOSSES (G&L) SHEET
This option is used to generate the daily Gains and Losses Sheet, Bed Status Report, and Treating Specialty Report.
INCONSISTENT DATA ELEMENTS REPORT
This option is used to generate a report of patients identified by the Consistency Checker as having inconsistent/unspecified data in their records.
INPATIENT/LODGER REPORT MENU
> ABSENCE LIST
> This option provides a listing of all active patients who are absent from the facility on a selected date.
> ASIH LISTING
> This option provides a listing of patients who are residents of the Nursing Home Care Unit or Domiciliary Unit, currently absent sick in hospital.
> CURRENT LODGER LIST
> This option is used to produce a listing of inpatients who are lodgers.
> FEMALE INPATIENT LIST (CURRENT)
> This option provides a list of current female inpatients.
> HISTORICAL FEMALE INPATIENT LIST
> This option provides a list of female inpatients for a selected date in the past.
> HISTORICAL INPATIENT LISTING
> This option provides a list of inpatients for a selected date in the past.
> INPATIENT LISTING
> This option provides a list of current inpatients.
> INPATIENT ROSTER
> This option provides a listing of patients by ward.
> INSURANCE LIST OF UNKNOWNS FOR INPATIENTS
> This option lists the inpatients who have "Unknown" or no answer in their insurance file.
> LODGERS FOR A DATE RANGE
> This option is used to produce a listing of lodgers for a specified date range.
Overview
> PATIENT MOVEMENT LIST
> This option lists all patient movements from a specified date/time in the past (not more than 5 days ago) to the current date.
> RELIGION LIST FOR INPATIENTS
> This option lists the inpatients and their religious affiliations.
> SERIOUSLY ILL INPATIENT LISTING
> This option provides a list of patients currently on the Seriously Ill List.
> TREATING SPECIALTY INPATIENT INFORMATION
> This option is used to generate outputs containing treating specialty inpatient information for a specified date.
MEANS TEST OUTPUTS
> DUPLICATE SPOUSE/DEPENDENT SSN REPORT
> This option is used to generate a listing of spouse/dependent with no SSN or same as veteran and also spouse/dependent with the same SSN as another spouse/dependent.
> HARDSHIP REVIEW DATE
> This option is used to generate a listing of patients whose hardship review date falls within a selected date range.
> LIST REQUIRED/PENDING MEANS TESTS
> This option provides a printout of patients in need of Means Testing or whose Means Tests are pending adjudication.
> MEANS TEST INDICATOR OF 'U' REPORT
> This option is used to list PTF records, within a specified date range, for which Means Test have not been done or not been completed.
> Means Test SPECIFIC INCOME AMOUNT REPORT
> The Means Test Specific Income Amount Report is used to print veteran information for those who reported a specific dollar amount.
> Means Test SPECIFIC INCOME LESS THRESHOLD REPORT
> The Means Test Specific Income Less Threshold Report is used to print veteran information for those whose income fell below the threshold amount by a specified dollar amount.
Overview
> Means Test w/Previous Year Threshold
> This option generates a listing of patients that have had a Means Test using the prior year thresholds as the current year thresholds were not yet available.
> Patients Who Have Not Agreed To Pay Deductible
> This option generates a listing of patients who have not agreed to pay the Means Test deductible.
> Required Means Test At Next Appointment
> This option generates a listing of patients who will require a new Means Test at their next appointment.
N/T RADIUM TREATMENT PENDING VERIFICATON LIST
This option generates a listing of patients who claim to have received Nose and/or Throat Radium Treatment while in the military and whose claims are pending verification.
PENDING/OPEN DISPOSITION LIST
This option provides a printout of open and pending dispositions within a specified date range of registrations.
PRINT PATIENT LABEL
This option prints patient labels containing the patient name, social security number, date of birth and (optionally) the inpatient location (ward/room#). These labels may be affixed to medical record forms in lieu of using the current embossed cards to imprint this information.
SCHEDULED ADMISSION STATISTICS
This option provides a statistical report by cancellation reason of cancelled admissions within a specified date range. The report is broken down by ward/treating specialty.
SCHEDULED ADMISSIONS LIST
This option provides a printout of active and/or cancelled scheduled admissions within a specified date range.
TREATING SPECIALTY PRINT
This option provides a report of Treating Specialties broken down by specified fields.
VBC FORM BY ADMISSION DATE
This option provides a printout of Veterans Assistance Records for admitted patients within a specified date range.
VBC FORM FOR SPECIFIC PATIENT
This option provides a printout of Veterans Assistance Records for specified patients.
WAITING LIST OUTPUT
This option provides a current list of patients on the waiting list.
Z07 BUILD CONSISTENCY CHECK
This option is used to test for inconsistencies which will prevent a Z07 message from being sent. The check is done per patient and will notify the user if inconsistencies are found. For details on the inconsistencies found, run the Inconsistent Data Elements Report in the ADT Outputs Menu.
10/10 Print
The 10/10 Print option is used to print the 10-10EZ/R forms for patients whether or not they’ve previously been registered for care. The 10-10EZ form is an Application for Health Benefits. The 10-10EZR form is an Application for Health Benefits Renewal. Both forms include several types of information (demographic, insurance, employment, and financial) about a patient. Since the financial information that is printed on the 10-10EZ or 10-10EZR form is taken from a means test associated to the patient and since a patient may have several means test entries during his/her course of care, the ‘PRINT 10-10EZ?’ and ‘PRINT 10-10EZR?’ prompts will present a selection list of means test entries associated with the patient. The selection list of means test entries will contain future Means Tests and future Co-Pay Exemption Tests that are not Primary. The selection list will also contain the most current Means Test, Co-Pay Exemption Test, and LTC Co-Pay Exemption Test that are Primary.
If data for the patient does not exist in the V*IST*A patient database, a message displays informing the user that the forms will not be printed.
*Please note: To print the 10-10EZR form, you must first answer “No” or “N” to the question, “Print 10-10EZ? Yes//”.*
Specific printers may be designated to automatically print most of this form through the MAS Parameter Entry/Exit option. A YES entry at the “Ask Device in Registration” parameter will force the DEVICE prompt at the beginning of registration the first time through and set the 10/10EZ form to print to that device. This takes precedence over all devices defined as default printers or closest printer.
Whether or not the health summary prompts appear in this option will depend on your site running the Health Summary package V. 2.5 (Patch \#3 or higher) and how the MAS health summary site specific parameters are set.
You also have the ability to print patient data cards through this option. The “Ask EMBOSS at Registration” site parameter must be set to YES in order for the data card prompts to appear here. With the installation of the Veteran Identification Card (VIC) software, the prompt “Download VIC data?” has been added which allows you to download the selected patient’s demographic data to the photo capture station. The existing “EMBOSS DATA CARD?” prompt has been changed to “EMBOSS (OLD) DATA CARD?”
Whether or not the encounter form prompts appear in this option will depend on how the MAS encounter form site parameters are set at your facility. At multidivisional facilities, the primary facility will be listed on the forms.
ADT Third Party Output MenuPatient Review Document
The Patient Review Document option is used to print the Third Party Review Form by patient name and admission date specifications. This form is used in connection with veteran patients admitted to the hospital who have private medical insurance. The form provides patient's name, patient ID#, admission date, diagnoses, and ward location. Insurance information provided includes insurance company name, address and phone number, policy number, and group number. The insurance data is not displayed if the insurance has expired.
The form is then divided into four sections. Section one concerns pre-admission certification. It shows whether or not pre-admission certification is required. If required, it provides information concerning the decision made by the insurance company regarding the admission including: number of days certified, whether medical information is insufficient, whether outpatient care is more appropriate, etc. Section two concerns the need for a second surgical opinion, if required, and results of the second opinion. Section three provides information concerning the length of stay review: if further stay was approved or if disapproved, the reasons for denial. Section four shows bill status; denied in full, denied in part, or paid in full. If denied, the reasons for denial are given. The bill number is also shown.
After the patient name is entered, the system checks the file for admissions. If the patient has had past admissions or is currently an active patient, you will be asked to select the admission date for which you wish to see the report. If none is selected, scheduled admissions will be checked. If there are scheduled admissions on file, the Third Party Review Form printed will be for the next scheduled admission date.
ADT Third Party Output MenuReview Document by Admission Range
The Review Document by Admission Range option is used to print the ADT Third Party Review Form by admission date specifications. This form is used in connection with veteran patients admitted to the hospital who have private medical insurance. The form provides patient's name, patient ID#, admission date, diagnoses, and ward location. Insurance information provided includes insurance company name, address and phone numbers, policy number, and group number. The insurance data is not displayed if the insurance has expired.
The form is then divided into four sections. Section one concerns pre-admission certification. It shows whether or not pre-admission certification is required. If required, it provides information concerning the decision made by the insurance company regarding the admission including: number of days certified, whether medical information is insufficient, whether outpatient care is more appropriate, etc. Section two concerns the need for a second surgical opinion, if required, and results of the second opinion. Section three provides information concerning the length of stay review: if further stay was approved or if disapproved, the reasons for denial. Section four shows bill status; denied in full, denied in part or paid in full. If denied, the reasons for denial are given. The bill number is also shown.
The report is sorted sequentially by admission date. Depending on the number of applicable admissions and the size of the date range specified, this report could be time-consuming. You may choose to queue the report to print during off-hours. The output should be generated at a 132 column margin width.
If you accept the default at the first prompt, the printout will start with the first admission date and go to the last.
ADT Third Party Output MenuVeteran Patient Insurance Information
The Veteran Patient Insurance Information option provides insurance information on veteran inpatients. This includes such information as insurance company, insurance number, group number, and insurance expiration date. Medical information is also shown. Dates of admission and discharge and status of the PTF Records are provided. The report is broken down by patient with information on length of stay for each bedsection, diagnoses, and diagnostic codes. The total length of stay is shown with the primary diagnosis.
The form indicates whether or not the policy shown will reimburse the VA for the cost of medical care. If the REIMBURSE field of the INSURANCE COMPANY file is set to NO for any of the companies that cover the applicant, an asterisk (\*) will be shown next to the insurance company name and the following message will appear:
\* - Insurer may not reimburse!!
All of this information is used in billing the insurance companies for the cost of the veteran's care.
The report may be sorted sequentially by discharge or admission date. You will be prompted for a date range and device. Depending on the number of applicable admissions and the size of the date range specified, generation of this report could be time-consuming. You may choose to queue the report to print during off-hours.
AMIS Reports MenuAMIS 334-341 Reports
The AMIS 334-341 Reports option is used to print the AMIS segments that record admission-discharge-transfer activity. AMIS stands for Automated Management Information System. It is a general system of computer programs used to process management reports.
The general title that applies to each segment is VA Hospital Inpatient Service. The subtitle of each segment is the specific service being reported. Facilities will only report on segments for which they have a corresponding service. The subtitle for each segment is as follows.
334 - Psychiatry 335 - Intermediate Medicine
336 - Medicine 337 - Neurology
338 - Rehabilitation Med 339 - Blind Rehabilitation
340 - Spinal Cord Injury 341 - Surgery
The report is selected by date (month/year) and each segment is printed as a separate report. The MAS System Status, which may be displayed whenever you enter the ADT Menu, will show you the last run date for AMIS 334-341. Each report provides such information as number of total admissions, transfers in, deaths, transfers out, female patients remaining, operating beds, patient days of care, bed occupants at end of month, days of authorized absence, etc. At a multi-divisional facility, the numbers for each division will be listed separately.
The segment balancing routine is displayed at the end of each segment report. The system will display an informational message if the segment is out of balance. Informational messages will also be displayed if beginning/ending of month statistics are missing for any applicable ward.
If a default code sheet printer has been specified through MAS parameters, you may generate the code sheets through this option providing segments are balanced.
AMIS Reports MenuAMIS 345-346 Reports
The AMIS 345-346 Reports option is used to print the AMIS segments that record the activity of the VA Nursing Home Units and Domiciliary Units. AMIS stands for Automated Management Information System. It is a general system of computer programs used to process management reports.
Segment 345 reports on Nursing Home Unit activity. Segment 346 reports the same information for the Domiciliary Unit. Some of the information provided includes admissions after rehospitalization greater than 30 days, all other admissions, discharges, deaths, absent bed occupants, those patients absent-sick-in-hospital, female patients remaining, patient days of care, and days of authorized absence less than 96 hours. At a multidivisional facility, the numbers for each division will be listed separately.
The report is selected by date (month/year) and each segment is printed as a separate report. The MAS System Status, which may be displayed whenever you enter the ADT Menu, will show the last run date for AMIS 345-346.
The segment balancing routine is displayed at the end of each segment report. The system will display an informational message if the segment is out of balance. Informational messages will also be displayed if beginning/ending of month statistics are missing for any applicable ward.
If a default code sheet printer has been specified through the MAS parameters, you may generate the code sheets through this option providing segments are balanced.
AMIS Reports MenuAMIS 401-420 Reports
The AMIS 401-420 Report option is used to generate or reprint the AMIS 401-420 series report for a selected month/year. AMIS stands for Automated Management Information System. It is a general system of computer programs used to process management reports.
The AMIS 401-420 series report is a breakdown of applications for care (registrations) by veteran category and disposition grouping. Only registrations for veteran patients are included on this report. The 401-420 AMIS series correspond to the twenty veteran categories.
While running the report, the system searches for open and pending dispositions. The report will not run if open dispositions exist. You will receive a MailMan message advising of such and, rather than the report printing on the device specified, a listing of "Pending/Open Dispositions" will print. If pending dispositions exist, the report will run placing these dispositions in the "pending" disposition category.
When generating the report for the first time for a selected month/year, the system tabulates the data - which takes roughly one hour per 1500 applications. You may also reprint a previously generated report or regenerate it. Whenever generating or regenerating the report, you will be given the opportunity to include a patient list with it. This lists all patients whose registration data was used to formulate the report. For each patient, the following information will be provided.
- AMIS Segment
- Last four digits of Social Security Number
- Registration Date/Time
- Benefit
- Registration Eligibility Code
- The block number(s) under which they have an entry (which in some cases may be multiple)
- Disposition Type
AMIS Reports MenuAMIS 401-420 Reports
This patient listing may be very helpful in interpreting the data given in the report as it indicates the actual blocks in which each patient is entered. Patients with disposition types falling in blocks 1-10 will only have one entry. Patients having Ineligible Disposition Types (blocks 11-15) will have one corresponding entry in blocks 16-19 and another in blocks 20-21 for a total of 3 entries. Patients having a Treatment Modality Unavailable disposition type, blocks 22-25, will have one corresponding entry in blocks 26-29 for a total of two entries. Patients having a Low Priority Disposition Type, blocks 30-33, will have a corresponding entry in blocks 34-37 for a total of two entries.
If a default code sheet printer has been specified through the MAS parameters, you may generate the code sheets through this option providing segments are balanced.
To reflect the elimination of Category B as a Means Test category, AMIS Segment 419 has had the INACTIVATION DATE field of the AMIS SEGMENT file set to October 1, 1991. If the last day of the AMIS month/year being printed is on or after the inactivation date, Segment \#419 will not print. For dates prior to the inactivation date, Segment \#419 will continue to print.
Division prompts will appear at multidivisional facilities, and if you are printing a report for which the totals have previously been generated.
Information providing further explanation of how the data is tabulated can be found at the end of this option documentation.
AMIS Reports MenuAMIS 401-420 Reports
The following is an example of the MailMan message generated when open/pending dispositions are found while running the report.
MailMan message for ADTEMPLOYEE,ONE
Printed at VAMC-SAN DIEGO 17 AUG 88 14:04
SUBJ: PENDING/OPEN DISPOSITIONS, MONTH OF 'AUG 1988' 17 AUG 88 14:06 12 Lines
From: POSTMASTER (Sender: ADTEMPLOYE,ONE) in 'IN' basket. \*\*NEW\*\*
-------------------------------------------------------------------------
I've accomplished a preliminary search of your database in preparation for generation of the AMIS 401-420 series reports for the range shown above. In this search there were "open" dispositions found which caused the actual generation of the report to cease. There were, possibly, some "pending" dispositions found also. Although these do not stop the report from generating every effort should be made to properly disposition these registrations also. A listing of these open/pending dispositions should have printed for your use in properly dispositioning them. If you can't locate this list there is an option available to regenerate this listing without generating the report.
Number of PENDING Dispositions found: 0
Number of OPEN Dispositions found : 1
AMIS Reports MenuAMIS 401-420 ReportsHOWBLOCKPLACEMENTOFDATAISDETERMINED
BLOCK 01 - The total number of applications which were received.
BLOCK 02 - Patients whose AMIS 401-420 DISPOSITION GROUP is "Hosp Admit".
BLOCK 03 - Patients whose AMIS 401-420 DISPOSITION GROUP is "Hosp W/L".
BLOCK 04 - Patients whose AMIS 401-420 DISPOSITION GROUP is "NHCU Admit".
BLOCK 05 - Patients whose AMIS 401-420 DISPOSITION GROUP is "NHCU W/L".
BLOCK 06 - Patients whose AMIS 401-420 DISPOSITION GROUP is "Dom Admit".
BLOCK 07 - Patients whose AMIS 401-420 DISPOSITION GROUP is "Dom W/L".
BLOCK 08 - Patients whose AMIS 401-420 DISPOSITION GROUP is "OP Care Rec". Also includes patients who have been dispositioned to something other than "Ineligible", "Low Priority" or "Trt Mo Unavail" but whose AMIS 401-420 DISPOSITION GROUP is one of the following:
a\. Community
b\. Fee Basis
c\. Other
d\. OP Care Rec
e\. Other VA
BLOCK 09 - Patients whose AMIS 401-420 DISPOSITION GROUP is "No Care Req".
BLOCK 10 - Patients whose AMIS 401-420 DISPOSITION GROUP is "Cancel".
BLOCK 11 - Patients whose disposition type is one of the two ineligible types and who have a TYPE OF CARE APPLIED FOR of DENTAL.
AMIS Reports MenuAMIS 401-420 ReportsHOWBLOCKPLACEMENTOFDATAISDETERMINED
BLOCK 12 - Patients whose disposition type is one of the two ineligible types and who have a TYPE OF CARE APPLIED FOR of PLASTIC SURGERY.
BLOCK 13 - Patients whose disposition type is one of the two ineligible types and who have a TYPE OF CARE APPLIED FOR of STERILIZATION.
BLOCK 14 - Patients whose disposition type is one of the two ineligible types and who have a TYPE OF CARE APPLIED FOR of PREGNANCY.
BLOCK 15 - Patients whose disposition type is one of the two ineligible types and whose TYPE OF CARE APPLIED FOR is not DENTAL, PLASTIC SURGERY, STERILIZATION or PREGNANCY.
BLOCK 16 - Patients whose disposition type is one of the two ineligible types and whose TYPE OF BENEFIT APPLIED for is HOSPITAL.
BLOCK 17 - Patients whose disposition type is one of the two ineligible types and whose TYPE OF BENEFIT APPLIED FOR is NURSING HOME.
BLOCK 18 - Patients whose disposition type is one of the two ineligible types and whose TYPE OF BENEFIT APPLIED FOR is DOMICILIARY.
BLOCK 19 - Patients whose disposition type is one of the two ineligible types and whose TYPE OF BENEFIT APPLIED FOR is other than HOSPITAL, NURSING HOME or DOM.
BLOCK 20 - Patients whose disposition type is INELIGIBLE-DISP COMMUNITY. The AMIS 401-420 DISPOSITION GROUP must be defined as COMMUNITY otherwise this will be counted in Block 21.
BLOCK 21 - Patients whose disposition type is INELIGIBLE-DISP OTHER. The AMIS 401-420 DISPOSITION GROUP must be defined as OTHER. If the AMIS 401-420 DISPOSITION GROUP is defined as COMMUNITY these dispositions will count in Block 20.
BLOCK 22 - Patients whose disposition type is one of the four Trt Mod Unavail types whose TYPE OF BENEFIT APPLIED FOR is "HOSPITAL".
AMIS Reports MenuAMIS 401-420 ReportsHOWBLOCKPLACEMENTOFDATAISDETERMINED
BLOCK 23 - Patients whose disposition type is one of the four Trt Mod Unavail types whose TYPE OF BENEFIT APPLIED FOR is NURSING HOME.
BLOCK 24 - Patients whose disposition type is one of the four Trt Mod Unavail types whose TYPE OF BENEFIT APPLIED FOR is DOMICILIARY.
BLOCK 25 - Patients whose disposition type is one of the four Trt Mod Unavail types whose TYPE OF BENEFIT APPLIED FOR is other than HOSPITAL, NURSING HOME or DOMICILIARY.
BLOCK 26 - Patients whose disposition type is TRT MOD UNAVAIL-DISP COMMUNITY. The AMIS 401-420 DISPOSITION GROUP must be defined as COMMUNITY since block placement is based on this data element.
BLOCK 27 - Patients whose disposition type is TRT MOD UNAVAIL-DISP OTHER VA. The AMIS 401-420 DISPOSITION GROUP must be defined as OTHER VA since block placement is based on this data element.
BLOCK 28 - Patients whose disposition type is TRT MOD UNAVAIL-DISP FEE BASIS. The AMIS 401-420 DISPOSITION GROUP must be defined as FEE BASIS since block placement is based on this data element.
BLOCK 29 - Patients whose disposition type is TRT MOD UNAVAIL-DISP OTHER. The AMIS 401-420 DISPOSITION GROUP must be defined as OTHER since block placement is based on this data element.
BLOCK 30 - Patients whose disposition type is one of the four Low Priority types whose TYPE OF BENEFIT APPLIED FOR is HOSPITAL.
BLOCK 31 - Patients whose disposition type is one of the four Low Priority types whose TYPE OF BENEFIT APPLIED FOR is NURSING HOME.
BLOCK 32 - Patients whose disposition type is one of the four Low Priority types whose TYPE OF BENEFIT APPLIED FOR is DOMICILIARY.
AMIS Reports MenuAMIS 401-420 ReportsHOWBLOCKPLACEMENTOFDATAISDETERMINED
BLOCK 33 - Patients whose disposition type is one of the four Low Priority types whose TYPE OF BENEFIT APPLIED FOR is other than HOSPITAL, NURSING HOME or DOMICILIARY.
BLOCK 34 - Patients whose disposition type is LOW PRIORITY-DISP COMMUNITY. The AMIS 401-420 DISPOSITION GROUP must be defined as COMMUNITY since block placement is based on this data element.
BLOCK 35 - Patients whose disposition type is LOW PRIORITY-DISP OTHER VA. The AMIS 401-420 DISPOSITION GROUP must be defined as OTHER VA since block placement is based on this data element.
BLOCK 36 - Patients whose disposition type is LOW PRIORITY-DISP FEE BASIS. The AMIS 401-420 DISPOSITION GROUP must be defined as FEE BASIS since block placement is based on this data element.
BLOCK 37 - Patients whose disposition type is LOW PRIORITY-DISP OTHER. The AMIS 401-420 DISPOSITION GROUP must be defined as OTHER since block placement is based on this data element.
BLOCK 38 - Patients whose disposition type is PENDING DETERMINATION. The AMIS 401-420 DISPOSITION GROUP must be defined as PENDING since block placement is based on this data element.
BLOCK 39 - Patients whose disposition type is REFUSED TO PAY DEDUCTIBLE. This AMIS 401-420 DISPOSITION GROUP must be defined as REFUSED TO PAY since block placement is based on this data element. This count is displayed on segment 420 only.
BLOCK 40 - Regardless of disposition type, registration type, etc. the total number of patients who were registered with a NON-VETERAN eligibility code will be displayed in this block - segment 420 only.
AMIS Reports MenuAMIS 401-420 ReportsDETERMINATIONOFSEGMENTONWHICHAREGISTRATIONWILLFALL
a\. If patient is registered with a service connected eligibility code:
1\) If service connected percentage not specified, place on segment 412
(Other SC).
2\) If service connected percentage is NOT a number divisible by 10 and is
NOT 0%, place on SEGMENT 412 (Other SC). Example would be a 25%
SC veteran.
3\) Place on Segment 401-411 based on service connected percentage of
100, 90, 80, 70, 60, 50, 40, 30, 20, 10 or 0 as appropriate.
b\. If patient is registered with a non-veteran eligibility code, place on SEGMENT 420 (MT Copay Required).
c\. If patient is registered with eligibility code PRISONER OF WAR, place on SEGMENT 413 (Former Prisoners of War).
d\. If either the EXPOSED TO AGENT ORANGE or EXPOSED TO RADIATION prompts are answered YES, place on SEGMENT 414 (Agent Orange/Ionizing Radiation).
e\. If patient is registered with eligibility code of either MEXICAN BORDER PERIOD or WORLD WAR I, place on SEGMENT 415 (World War I).
f\. If patient is registered with eligibility code of NSC, VA PENSION, place on SEGMENT 416 (VA Pensioner).
g\. If during the registration process the user indicates that the patient is eligible for MEDICAID, place on SEGMENT 417 (Medicaid).
h\. If none of the above conditions are met, then check the MEANS TEST file at the time the report is actually generated and determine segment placement (418-420) as follows: if patient met any of the above criteria, the segment of placement is stored at the time of disposition (or whenever the disposition log is edited) and used when generating the report.
AMIS Reports MenuAMIS 401-420 ReportsDETERMINATIONOFSEGMENTONWHICHAREGISTRATIONWILLFALL
When checking the MEANS TEST file, the date which occurred nearest to (but not after) the registration date/time will be used for classification purposes.
1\) If patient is NOT in the means test file, place on SEGMENT 418
(MT Copay Exempt).
2\) If there was no means test applied prior to the disposition date/time, place
on SEGMENT 418 (MT Copay Exempt).
\*\*3) If the patient is identified as CATEGORY B, place on SEGMENT 419
(Category B).
4\) If the patient is identified as MT Copay Required or the means test is
PENDING ADJUDICATION, place on SEGMENT 420 (MT Copay
Required).
5\) If the patient is identified as MT Copay Exempt, REQUIRED or MEANS
TEST NO LONGER REQUIRED, place on SEGMENT 418 (MT Copay
Exempt).
\*\*To reflect the elimination of Category B as a Means Test category, AMIS Segment 419 had had the INACTIVATION DATE field of the AMIS SEGMENT file set to October 1, 1991. If the last day of the AMIS month/year being printed is on or after the inactivation date, Segment \#419 will not print. For dates prior to the inactivation date, Segment \#419 will continue to print.
Bed Availability
The Bed Availability option produces a listing of available beds. You may choose to see the bed availability for a single ward (abbreviated listing) or multiple wards or services (expanded listing). You can choose to have the room-bed description displayed on either listing.
The expanded report can be sorted by ward or service. One, many, or all wards/services may be selected. The user may also select to have the report show future scheduled admissions and/or lodgers. If there are no beds available on a selected ward/service, a message stating this will be displayed.
Disposition Outputs MenuDisposition Time Processing Statistics
This option provides a printout of registration/disposition time statistics for a given period.
The report is sorted by disposition action, listing the number of patients dispositioned for each action and the average processing time per disposition. It is further broken down to show the number of dispositions within 1 hour, 2 hours, 8 hours, 24 hours, 48 hours, 72 hours, 7 days, 30 days, and over 30 days of registration.
This report includes neither applications without an examination, applications for nursing, domiciliary, or dental care nor does it include undispositioned registrations. You may, however, choose to print a listing of undispositioned registrations for the selected time period. This report includes patient name, SSN, division, and registration date/time.
At multidivisional sites, a summary table showing the totals for each division is provided. If there are patients not associated with any division, those patients will print on a separate page with a heading of UNSPECIFIED.
Disposition Outputs MenuLog of Dispositions
The Log of Dispositions option provides a report of patient disposition records.
The report may either be produced for all dispositions (open and closed dispositions within a specified log-in date range) or "in process" dispositions. "In process" shows open dispositions only. The report will be sorted by log-in date/time.
If you are at a multidivisional facility, you may select to have the report broken down by division.
If you choose all dispositions and a lengthy date range, it may be best to queue production for off-hours.
Disposition Outputs MenuSummary of Dispositions
The Summary of Dispositions option provides a report of dispositions by disposition type for a selected date range.
The report will show the number of dispositions in the 10-10 visits, unscheduled visits, and applications without exam categories by disposition type. Totals will also be provided.
If you are at a multidivisional facility, the report will be separated by division.
Enrollment ReportsEnrolled Veterans Report
This option is used to produce the Enrolled Veterans Report. The report contains a summary of the number of patients in each enrollment priority group and includes the enrollment category (Enrolled, Not Enrolled, and In Process)
The only prompt is for device.
For information about how a veteran's priority is derived, please refer to the Enrollment Priority Algorithm section found in the ADTBE.pdf file.
Enrollment ReportsPending Applications for Enrollment
The Pending Applications for Enrollment option is used to generate a list of patients with enrollment statuses of *Unverified* and *Pending* for selected facilities within a specified date range. The report is sorted by preferred facility and enrollment status. Patients are listed chronologically by appointment date.
You are prompted to select a date range, the facilities you want to include in the report, and a device. If you print the report to include ALL facilities, the report will include only selected institutions as determined by the patients' chosen preferred facility.
Enrollment ReportsEnrollees by Status, Priority, Preferred Facility
The Enrollees by Status, Priority, Preferred Facility option is used to produce a report that provides counts of patients by preferred facility, enrollment status, and enrollment priority.
The report is divided into two parts, Summary Statistics and Patient Listing. The Patient Listing portion of the report will only be printed if you choose to include the list of selected patients. You may select one/many/all enrollment statuses and enrollment priorities if you include the list of patients. Otherwise all applicable statuses and priorities will be included in the report.
If you choose to include the list of patients, the following patient-specific information will be displayed.
- name
- SSN
- date of birth
- enrollment status
- enrollment priority
- enrollment date
- end date
- enrollment category
Enrollment ReportsUpcoming Appointments without Enrollment
The Upcoming Appointments without Enrollment option is used to generate a report of patients with future appointments who are not enrolled and do not have pending enrollment applications.
You are prompted to enter a date range in the future. You can sort by all clinics, all clinics in a particular division(s), or individual clinics. For patients with multiple appointments, you may choose to list only the first appointment or to list all appointments.
Enrollment ReportsEGT Impact Report
After the EGT change is received at the medical center and the MailMan bulletin has been sent to notify staff of the changes, a process is needed to allow the staff to determine which specific veterans may be affected by the EGT change. Four separate reports which may be generated through this option provide this information.
Sort criteria includes *preliminary* reports or *actual* reports.
- If preliminary is selected, the output is calculated based on a comparison of the EGT setting and the veteran’s enrollment priorities as recorded in VISTA.
- If actual is selected, the output is calculated based on a comparison of the EGT setting and the veteran’s enrollment priorities as provided by HEC and recorded in VISTA.
Sort criteria includes *summary* reports or *detail* reports.
- If summary is selected, the output provides a count, by enrollment priority, of those patients potentially affected (preliminary) or actually affected (actual) by the EGT change.
- If detailed is selected, the output provides patient specific information and enrollment information. The selection of actual or preliminary is a key factor in this output. The user may choose to include future appointments in the detailed reports.
*EGT Preliminary Summary Impact Report* - This report provides a preliminary, summarized count of patients who are potentially affected by the EGT change.
*EGT Preliminary Detailed Impact Report* - This report provides a preliminary, detailed count of patients who are potentially affected by the EGT change and includes patient information and enrollment information.
*EGT Actual Summary Impact Report* - This report provides a count of patients who are actually affected by the EGT change.
*EGT Actual Detailed Impact Report* - This report provides a detailed count of patients who are actually affected by the EGT change and includes patient information and enrollment information.
Enrollment ReportsNon-Treating Preferred Facility Clean Up
This process will find all patients that have a non-treating preferred facility on file. All identified patients will need to have their preferred facility changed to a valid treating facility.
The clean up process will compile the patient data. It looks at every patient in the PATIENT file (#2). A summary MailMan message will be sent to you when the compile is complete.
You will need to return to this option to print the detail report within 30 days to avoid recompiling.
> **NOTE:** The system will purge the compiled data after 30 days!
Enrollment ReportsFormer OTH Patient Eligibility Change Report
This option is used to identify Former Service Members whose Primary Eligibility changed from EXPANDED MH CARE NON-ENROLLEE to a new Primary Eligibility as determined by VBA.
Former OTH Patient Detail Report
This report is used by the BAS/HAS (VAMC) and billing staff to review current eligibility,past episodes of care (outpatient and inpatient) and prescriptions provided to Former Service Member with Other Than Honorable discharge and determine whether they should be back-billed for treatments occurred during pending VBA adjudication period based on VBA outcomes.
Gains and Losses (G&L) Sheet
The Gains and Losses (G&L) Sheet option is used to generate the daily Gains and Losses Sheet, Bed Status Report, and Treating Specialty Report for the medical center. A display of how the G&L parameters are set at your facility appears after the option is selected.
The first portion of this report (Gains and Losses Sheet) provides information concerning patient movement for the date selected. It shows all gains (admissions, transfers in from other facilities, returns from authorized and unauthorized absence) and losses (discharges, transfers out, and deaths). Interward transfers are counted as both a gain and loss. It also displays lodger checkins/checkouts. Admission type (direct, ambulatory care, etc.) and discharge type (regular, service connected, non-service connected, etc.) are specified. Applicable patient names, social security numbers, and ward locations are listed under the appropriate sections. The total number in each category is displayed next to the heading. Nursing home totals may be listed separately. Corrections to previous G&L Sheets may also appear in this portion of the report.
Footnotes which may appear on the G&L include the following. They will only appear if there is an applicable patient for the day the G&L is printed.
\+ Third Party Reimbursement Candidate
> a MT Copay Exempt veteran
> c MT Copay Required veteran
> g GMT Copay Required veteran
> r Current Means Test Required but not Completed
> \# Discharge within 48 hours of admission
The plus sign (+) appears if the patient has private medical insurance and the REIMBURSE field in the INSURANCE COMPANY file is not set to NO. If the patient has multiple insurance policies, the indicator will appear even if only one policy has the REIMBURSE field not set to NO.
Whether or not information concerning patients on authorized absence and patients on pass less than 96 hours appears on the G&L Sheet will depend on how the site parameters are set at your facility. The parameters may also be set to print your nursing home, domiciliary, and medical center data on separate sheets. At multidivisional facilities, the parameters may be set differently for each division. A separate G&L Sheet will be printed for each division at multidivisional facilities.
Gains and Losses (G&L) Sheet
The Bed Status report is the second portion of the G&L Sheet. While the first portion provides actual patient names, this section provides only statistical information. Each ward in the service is listed with the following information: bed section, number of patients previously reported, gains, losses, number of patients remaining, those on pass, authorized absence, unauthorized absence and absent-sick-in hospital, vacant beds, beds out of service, operating beds, number over capacity, authorized beds, cumulative occupancy rate, and cumulative patient days. The totals for each service are shown as well as a grand total line. Nursing Home Unit totals may be listed separately.
The Bed Status report portion of the G&L Sheet lists the planned and actual cumulative ADC (Average Daily Census) for the medical center, nursing home unit, and domiciliary unit (if applicable). Cumulative totals for admissions, discharges, interward transfers, interservice transfers, and patient days are listed for each service for the last fiscal year and current fiscal year. A grand total line may also be shown. Elapsed fiscal days are displayed.
The G&L sheet has been enhanced by adding a third portion - an output that displays statistical data in terms of treating specialty. This Treating Specialty Report (TSR) reflects inpatient activity by the actual treating specialty assigned to each patient movement. Proper crediting of workload regarding "boarders" will now take place as the credit will be to treating specialty as opposed to a ward location.
Each facility treating specialty in each service is listed with the following information: previous patients remaining, gains, losses, current patients remaining, those on pass, authorized absence, unauthorized absence and absent-sick-in hospital, average daily census, and cumulative patient days of care. The totals for each service are shown as well as a grand total line. Nursing Home Unit totals may be listed separately.
Gains and Losses (G&L) Sheet
In addition to generating the G&L Sheet, this option is also used to enter the projected figures for cumulative and monthly planned ADC. At multidivisional facilities, these prompts will appear for each division. At the beginning of each fiscal year, the projected figures for cumulative planned ADC are entered at each of the following prompts.
CUM PLANNED ADC
\*CUM PLANNED NH ADC
\*CUM PLANNED DOM ADC
At the beginning of each month, the projected figures for monthly planned ADC are entered at each of the following prompts.
MONTHLY PLANNED ADC
\*MONTHLY PLANNED NH ADC
\*MONTHLY PLANNED DOM ADC
These figures will subsequently appear as defaults at these prompts each time the report is run. The user may then default through these prompts to print the G&L Sheet.
When running the G&L for T-l (yesterday), the user will be asked "TRANSMIT OVERDUE ABSENCE BULLETIN?" if a mail group has been specified for OVERDUE ABSENCES GROUP in the Bulletin Selection option. If YES is answered, a background job will run which will look at all inpatients and determine: 1) have they been on pass more than 4 days 2) have they been on authorized absence more than 30 days (NHCU/DOM) 3) have they been on authorized absence more than 14 days (VAMC) 4) have they been on unauthorized absence more than 30 days. If any of these conditions are met, a message will be transmitted to the mail group selected by the facility showing those patients now overdue.
Provided at the end of this option documentation is an explanation of system messages which may appear while using this option and an explanation of the columns on the Bed Status Report portion of the G&L Sheet.
\*Only applies to facilities with nursing home and/or domiciliary units.
Gains and Losses (G&L) Sheet
1\) If a G&L Sheet is printing at the time this option is called, the following message will be displayed and you will be exited from the option.
"G&L is already running started at {date and time}"
2\) If the "Recalculate G&L Cumulative Totals" function is running at the time this option is called, the following message will be displayed and you will be exited from the option.
"Recalc is running and currently processing on {date}
Do you wish to print G&L anyway?"
3\) If the G&L Sheet has not been run in the last 7 days at the time this option is called, the following message will be displayed and you will be exited from the option. Utilize the Recalculate G&L Cumulative Totals option.
"G&L has not been run in last week use recalc first"
4\) If you enter a date to print the G&L before the date defined in EARLIEST DATE FOR G&L MAS parameter, the following message will be displayed.
"Date entered is too early, Earliest date allowed is {date}"
5\) If ward census has not been collected for date selected, the following message will appear after the site name.
"WHAT WAS THE CENSUS ON {date}?"
Gains and Losses (G&L) Sheet
The following are the formulas and/or manner derived for the G&L/BSR columns.
<u>Column</u> <u>Title</u> <u>Formula and/or Manner Derived</u>
1 Ward NAME field (#.01) of the Ward Location file (#42). 7
characters displayed out of 2-30 allowed.
2 Bed Section BEDSECTION field (#.02) of the Ward Location file (#42).
10 characters displayed out of 2-10 allowed.
3 Prev Rem. PATIENTS REMAINING field (#1) of the Census file (#41.9).
\[prior day patients remaining on this ward as of midnight\]
4 Gain GAINS-TOTALS \[CUM\] field (#28) of the CENSUS file (#41.9)
(current census day) minus GAINS-TOTALS \[CUM\] field (#28)
(prior census day).
5 Loss CUM LOSSES field (#24) of the CENSUS file (#41.9) (current
census day) minus CUM LOSSES field (#24) (prior census day).
6 Pt's Rem. PATIENTS REMAINING field (#1) of the Census file (#41.9)
(current census day). \[Prev Rem. (prior census day) plus Gains
minus Losses (current census day).\]
7 Pass PATIENTS ON AA\<96 field (#105) of the Census file (#41.9).
\[Patients on PASS as of that day - notcumulative.\]
8 AA PATIENTS ON AUTHORIZED ABSENCE field (#106) of the
Census file (#41.9). \[Number of patients on AA on that census
day - not cumulative.\]
9 UA UNAUTHORIZED ABSENCE field (#107) of the Census file
(#41.9). \[Number of patients on UA on that census day - notcumulative.\]
10 ASIH ASIH field (#108) of the Census file (#41.9). \[Number of patients
on ASIH on that census day - notcumulative.\]
11 Vacant Beds OPERATING BEDS field (#102) of the Census file (#41.9)
(current census day) minus PATIENT REMAINING (#1) field
(current census day). \[opposite of over capacity.\]
12 Beds OOS BEDS OUT OF SERVICE field (#109) of Census file (#41.9). This
field is populated when the user enters a bed out of service through
Bed Out-of-Service Date Enter/Edit option found under Supervisor
ADT menu.
Gains and Losses (G&L) Sheet
<u>Column</u> <u>Title</u> <u>Formula and/or Manner Derived</u>
13 Oper Beds OPERATING BEDS field (#102) of Census file (#41.9).
\[\*\* Computed - NOT user editable \*\*\] \[AUTHORIZED BEDS
field (#110) minus BEDS OUT OF SERVICE field (#109) of the
Census file (#41.9)\]
14 Over Cap. PATIENTS REMAINING field (#1) minus OPERATING
Beds BEDS field (#102) of the Census file (#41.9).
\[opposite of vacant beds\]
15 Auth Beds AUTHORIZED BEDS field (#110) of the Census file (#41.9). This
figure is entered based on hospital beds that have been authorized
by VA Central Office for a particular facility.
16 Cum ADC CUM PATIENT DAYS OF CARE field (#2) of the Census file
(#41.9) divided by days in service (days into fiscal year minus out
of service days).
17 Cum Occ. CUM PATIENT DAYS OF CARE field (#2) of the Census file
Rate (#41.9) divided by CUM BEDS field (#3) multiplied by 100.
18 Cum Patient CUM PATIENT DAYS OF CARE field (#2) of the Census file
Days (#41.9). Continually add each day's PATIENT DAYS OF CARE,
e.g., if yesterday's CUM PATIENT DAYS OF CARE is 1300, and
today's PATIENT DAYS OF CARE is 500, the CUM PATIENT
DAYS OF CARE for today would equal 1800.
Inconsistent Data Elements Report
The Inconsistent Data Elements Report option generates a report of patients identified by the Consistency Checker as having inconsistent/unspecified data in their records for a selected date range. This report contains entries in the INCONSISTENT DATA file (#38.5).
The Consistency Checker must be turned ON at your site in order to run this report.
You must elect to run this report on a specified date for either patient admission date, identification date (date inconsistent/unspecified data were identified), or patient registration date. You must choose to sort the output either alphabetically by patient name or numerically by terminal digit (last number in the patient’s SSN). You can generate a list of inconsistencies found during registration or Z07 message build, or a list of all inconsistencies found. The report requires 132-column output.
The output includes:
- Report title, page number, and date
- Patient name, home phone number, and SSN
- Last day identified, admitted, or registered (depending on your selection)
- Last edited by
- List of inconsistent/missing data elements, sorted by patient
Inpatient/Lodger Report MenuAbsence List
The Absence List option provides a listing of all inpatients who are absent from the medical center on a particular date on pass, authorized absence, or unauthorized absence. Patient names are listed alphabetically by last name along with patient ID#, type of absence, date patient left, date of return, and ward location.
At multidivisional facilities, the report is separated by division.
Inpatient/Lodger Report MenuASIH Listing
The ASIH (absent sick in hospital) Listing option provides a listing of patients, for a selected date, who are residents of the Nursing Home Care Unit or Domiciliary Unit but who are currently hospitalized on an acute care ward. Patients are listed alphabetically. Patient ID number, date placed on the ASIH List, and current ward location are also provided.
At multidivisional facilities, the report will be sorted by division.
Inpatient/Lodger Report MenuCurrent Lodger List
The Current Lodger List option is used to produce a listing of lodger patients. At multidivisional facilities, a listing may be printed for one/many/ all divisions.
The list may be generated for one/many/all wards and you may request the listing to include lodgers at another facility. This list is generated in chronological order by check-in date within each ward.
Information on the output will include: patient name, short ID, date the lodger checked in, bed assignment, reason for lodger status, and any additional comments. The listing should be printed at 132 columns.
Inpatient/Lodger Report MenuFemale Inpatient List (Current)
The Female Inpatient List (Current) option provides a listing of females who are currently inpatients in the medical center. The only prompts are for device.
The Female Inpatient List is usually sorted alphabetically by name and will include patient ID#, ward location, room-bed, and date admitted. Supervisors may change the format of this report by selecting a template through the Template Selection option of the ADT System Definition Menu. At multidivisional facilities, the report will be broken out by division.
Inpatient/Lodger Report MenuHistorical Female Inpatient List
The Historical Female Inpatient List option is used to provide a listing of female inpatients for a specific day in the past.
The listing is usually sorted by name and will include patient ID#, ward, room-bed, and date admitted. The Supervisor may choose to change the format of the output by choosing a template through the Template Selection option of the ADT System Definition Menu.
At multidivisional facilities, the report will be broken out by division.
Inpatient/Lodger Report MenuHistorical Inpatient Listing
The Historical Inpatient Listing option is used to provide a listing of inpatients for a specified date.
Patients are listed in alphabetical order by ward and you may choose all wards or a range of wards. The report will include patient name, PT ID#, date admitted, last transfer date, date of discharge, and pass status. If you are at a multidivisional facility, the report will be broken out by division. Subcounts for each ward will be given and cumulative subcounts per division will be noted. A total count is also provided.
Note that such a report may be time consuming to run and you may opt to produce this report during off-hours depending on the size of your database and the range of your specifications.
Inpatient/Lodger Report MenuInpatient Listing
The Inpatient Listing option provides a listing of current inpatients.
The report may be sorted by patient name or ward. You may select the report with a ward breakout which will print all interward transfers during this admission. If ward breakout is not selected, only the current ward will be shown. If ward breakout is selected, you may also elect to have the listing generated with a DRG breakout. The message "No DRG can be calculated" will appear when there is not enough information to allow for DRG calculation.
The figure listed on the report after "TOTAL" in the Ward Location column indicates the cumulative movements of that single patient. For patients who are currently ASIH, only the transfers which occurred during this ASIH admission will be listed.
Information which may be provided on the output includes patient ID#, admission/transfer date, ward location, length of stay, and days on authorized absence, pass, unauthorized absence, and ASIH. DRG information may include average LOS, trim values, etc.
Note that such a report may be time-consuming to run and you may opt to produce this report during off-hours depending on the size of your database and the ranges specified.
If DRG breakout is selected, the output should be generated at a 132 column margin width.
Inpatient/Lodger Report MenuInpatient Roster
The Inpatient Roster option generates a listing of current inpatients by ward or provider. If sorted by ward, the report may be run for one/many/all divisions and one/many/all wards. Selected wards must be associated with selected divisions at multidivisional facilities. If sorted by provider, the report may be run for one/many/all providers. Sorting by provider, you will be further prompted for primary physician, attending physician, or either. If either is chosen, the report will list a patient entry if the provider is either the attending or primary physician. This could result in a given patient potentially being listed twice; once under his attending physician and once under his primary physician. A secondary sort is by room number or patient name.
The following information may be displayed for each patient on the listing: name, ID, age, admission date, number of days hospitalized, ward, room-bed, primary physician, attending physician, treating specialty, and current Means Test status.
The user may choose how many copies to print and may request the report be double spaced. The report requires printing at 132 column output.
Inpatient/Lodger Report MenuInsurance List of UNKNOWNs for Inpatients
The Insurance List of UNKNOWNs for Inpatients option is used to produce a list of active patients with unknown or unanswered insurance data.
You may choose to display the report for a date range or the current date. You may also choose to include service-connected inpatients.
The report will list the patients in alphabetical order and will include the following information: patient ID#, date of birth, the date and time of admission, and whether or not the patient is a veteran and/or service connected. A patient will appear on the list if either the information was unknown or the prompt was left unanswered by the user at the time the insurance data was being entered into the system. A "#" is used to distinguish the patients whose insurance data was unanswered from those whose information was unknown.
If you are at a multidivisional facility, the report will be sorted by division. A totals page for the entire medical center is also provided.
<u>  
</u>Inpatient/Lodger Report MenuLodgers for a Date Range
The Lodgers for a Date Range option is used to produce a listing of lodger patients at your facility for a specified date range. At multidivisional facilities, a listing may be printed for one/many/all divisions.
The list may be generated for one/many/all wards and you may request the listing to include lodgers at another facility. The report will be generated in chronological order by check-in date within each ward.
Information on the output will include: patient name, short ID, date the lodger checked in, bed assignment, reason for lodger status and, if applicable, the date the lodger checked out, length of stay, disposition, and any comments. The listing should be printed at 132 columns.
Inpatient/Lodger Report MenuPatient Movement List
The Patient Movement List option is used to produce a listing of all patient movements from a specified date/time in the past to the current date. The starting date for this list cannot be more than five days in the past. The report will include all admissions, discharges, and transfers that occurred within the designated time frame. This listing will be generated in chronological order by admission/ discharge/transfer date. If a time is not entered, all movements for the selected date range will be displayed.
Data supplied on this listing will include: date range of report, patient name and ID#, date/time of movement, and the “to and from” locations.
<u>  
</u>Inpatient/Lodger Report MenuReligion List for Inpatients
The Religion List for Inpatients option is used to produce a list of inpatients with their religious affiliations.
You will be asked to choose whether to display the report for a date range or current date. If you select date range, the report will display all patients that were admitted to the medical center during the range of dates you specify. If you select current date, the report will display only those patients who are currently inpatients.
You may list the report by religion or ward. You may choose to include those patients whose religion is “not specified”. If the report is listed by religion, the major sort is by religion and within each religion the patient names are sorted by ward. Each religion is printed on a separate page. If the report is listed by ward, the major sort is by ward and within each ward the patient names are further sorted by religion. Each ward is printed on a separate page.
In addition to the patients' religion and ward, the following information will be included in this report: room number, patient name, patient ID# (last four digits of the patient's SSN), and the date and time of admission.
If you are at a multidivisional facility, the report will also be sorted by division.
Inpatient/Lodger Report MenuSeriously Ill Inpatient Listing
The Seriously Ill Inpatient Listing option provides a listing of those patients currently on the Seriously Ill List.
The report is sorted by name and includes patient ID#, ward location, room-bed, religious preference, and the date that the patient was entered on the Seriously Ill List. The Supervisor may change the format of this report through the Template Selection option of the ADT System Definition Menu, if desired.
If you are at a multidivisional facility, the report will be separated by division.
Inpatient/Lodger Report MenuTreating Specialty Inpatient Information
The Treating Specialty Inpatient Information option is used to generate outputs containing treating specialty inpatient information for a specified date. Three separate reports may be generated.
The patient listing by ward and patient listing by treating specialty reports print individual patient information such as name, ID, admission date, last facility treating specialty (for listing by ward), inpatient ward (for listing by treating specialty), last treating specialty service, and absences. Subcounts and totals are included.
The patient count by treating specialty report prints the subcounts and totals for each facility treating specialty by division. Other than information on absences, individual patient information is not provided.
Depending on your facility and the reports selected, this output could be quite lengthy. You may wish to queue it for off-hours.
When printed, each report will begin on a separate page.
Means Test OutputsDuplicate Spouse/Dependent SSN Report
This option is used to generate a listing of 1) spouses/dependents for which there is not a social security number listed or that show the same social security number as the veteran and 2) spouses/dependents for which the social security number is the same as that of another spouse or dependent.
The first part of the report contains the veteran’s name and SSN and the name, SSN, and relationship of the spouse/dependent sorted by veteran’s SSN. The second part of the report contains the name, SSN, and relationship of the spouse/dependent and the veteran’s SSN for each spouse/dependent sorted by spouse/dependent SSN.
If the veteran has a date of death or their last inpatient appointment is more than 3 years ago from the date the report is generated, they will not be included.
Facilities are required to generate these reports on a regular basis and to initiate corrective action for duplicate entries and for those cases where no SSN is found on file. Corrective action may include contacting the veteran and/or the spouse/
dependent to obtain the correct SSN.
Means Test OutputsHardship Review Date
The Hardship Review Date option is used to generate a listing of patients for a selected date range, whose hardship review date falls within that range. Hardship exemptions are usually reviewed annually.
The output includes the date range, report run date, patient name, patient ID, and hardship review date.
Means Test OutputsList Required/Pending Means Tests
The List Required/Pending Means Tests option is used to generate a listing of patients who either require Means Testing or whose Means Tests are pending adjudication. The patient name, patient ID number, Means Test source, and date of test are provided. The patients are listed in alphabetical order on the output.
You will be prompted for the Means Test status (REQUIRED or PENDING ADJUDICATION), a date range, and a device.
Means Test OutputsMeans Test Indicator of 'U' Report
The Means Test Indicator of 'U' Report option is used to list PTF records, within a specified date range, for which the Means Test is not done or not completed. The system searches every PTF record for each patient in the date range selected for a Means Test indicator of 'U'. It then determines, by looking at the patient record in the PATIENT file, if the indicator should still be 'U'. If so, these patients are listed on the report. If not, the system updates the Means Test indicator to the appropriate value in the PTF record and these patients will not appear on this report.
The user may choose to run the report for either a discharge date range or admission date range. The report can be sorted by patient last name or terminal digit (social security number). Information provided includes patient name and social security number, PTF number, and applicable date of test. This date is the Means Test date that is used to determine the Means Test indicator, as it may be possible to have more than one Means Test date for a single admission.
The system looks for the closest Means Test date previous to the discharge date for the applicable date of test. If there is no discharge date, it will search for the closest test date previous to the admission date. If no test date is found, the date shown on the report in the applicable date of test column will be the admission date if admission date range is chosen and the discharge date if discharge date range is chosen. These dates are signified on the report by a double asterisk (\*\*).
Means Test OutputsMeans Test Specific Income Amount Report
The Means Test Specific Income Amount Report is used to print veteran information for those who reported a specific dollar amount. The user will be asked for a date range and an income range.
The output includes veteran name, social security number, income amount, and the date the Means Test was completed.
Means Test OutputsMeans Test Specific Income Less Threshold Report
The Means Test Specific Income Less Threshold Report is used to print veteran information for those whose income fell below the threshold amount by a specified dollar amount. The user will be asked to enter a dollar range.
The output includes veteran name, social security number, dollars below threshold, and Means Test completion date/time.
Means Test OutputsMeans Test w/Previous Year Threshold
The Means Test w/Previous Year Threshold option is used to generate a listing of patients, for a selected date range, that have had a Means Test using the prior year thresholds, as the current year thresholds were not yet available.
The output includes the date range, report run date, patient name, patient ID, and date of test.
Means Test OutputsPatients Who Have Not Agreed to Pay Deductible
The Patients Who Have Not Agreed to Pay Deductible option is used to generate a listing of "active" patients, for a selected date range, who have not agreed to pay the Means Test deductible. Active includes any dispositions, patient movements, or clinic appointments 365 days back from the beginning date of the date range. Future clinic appointments and scheduled admissions are also checked.
The output includes the date range, report run date, patient name, Means Test status, patient ID, Means Test source, and whether occurrence found was in the past, future, or in house. In house is a current inpatient, past is within the selected date range, and future is after the current date/time.
Means Test OutputsRequired Means Test At Next Appointment
The Required Means Test At Next Appointment option is used to generate a listing of patients, for a selected date range, who will require a new Means Test at their next appointment.
You may select to report one/many/all divisions and one/many/all clinics. The output includes the date range, report run date, clinic name, division, patient name, patient ID, appointment date/time, appointment type, Means Test status, and date of incomplete Means Test.
N/T Radium Treatment Pending Verification List
This option is used to generate a list of patients who claim to have received Nose and/or Throat Radium Treatment while in the military, and whose claims are pending either the documentation verification or the verification of diagnosis of head and/or neck cancer. The list can be sorted alphabetically by patient name or by the date/time the claim was entered.
The first section of the list contains patient names that are pending documentation verification. The second section of the list contains patient names that have verified documentation, but are pending verification of a diagnosis of head and/or neck cancer.
Information provided in the report includes the following.
SSN Social Security Number
NT Yes/No/Unknown - Does the patient claim to have received nose and/or
throat radium treatment while in the military?
AVI Yes/No - Did the patient serve as an aviator in the military before 1/31/55?
SUB Yes/No - Did the patient have submarine training in the military before
1/1/65?
Pending/Open Disposition List
This option is used to print a list of open and pending dispositions (excluding unscheduled visits) within a specified range of registration dates.
Each patient registration for care must receive a corresponding disposition. A disposition shows the final outcome of the registration; whether the patient was admitted, treated and released, scheduled for a return visit, etc. An open disposition is a registration which has not received a disposition. A pending disposition is a registration which was dispositioned with a disposition type of PENDING DETERMINATION.
Your system uses the data gathered through the registration and disposition processes to compile the AMIS 401-420 series reports. You will not be able to run this AMIS report if you have open dispositions within the date range specified. Also, you will not be able to reregister these patients until these open dispositions are dispositioned. If you have pending dispositions, the AMIS 401-420 report will run, however these dispositions will appear in the PENDING block of the report.
The output is sorted alphabetically by patient last name. For each patient, it will include the patient ID#, date/time of the registration, application type (benefit applied for), and whether it is open or pending.
If you are at a multidivisional facility, each division will be reported separately.
Print Patient Label
The new Veteran Identification Card, provided by the VIC Card Replacement project, does not allow for the embossing of protected health information. The Print Patient Label option was created to allow printing of labels containing that protected information; patient name, social security number, and date of birth. An optional fourth line contains the patient’s inpatient location (ward and room \#). The labels may then be affixed to medical record forms in lieu of using the embossed cards to imprint the information.
If you choose to print the inpatient location on the label and the patient is not an inpatient, the label will read “Ward: UNKNOWN”.
The option supports plain text printing to dot matrix and laser printers by prompting for the number of lines that the label stock can contain. In addition, bar code labels printers, such as Zebra and Intermec, are supported on systems that have the appropriate Kernel patch installed (XU\*8\*205).
An example of how the label may appear is provided below.
![](pims-version-5-3-user-manual-adt-outputs-menu/001.png)
Scheduled Admission Statistics
The Scheduled Admission Statistics option is used to generate statistics, for a specified date range, for patients scheduled for admission versus those which were cancelled. The report is broken down by ward/treating specialty showing the total number of scheduled admissions and total cancellations. Cancellations are further broken down by reason for cancellation. The cancelled scheduled admissions are categorized by the entries in other options such as Cancel a Scheduled Admission, Death Entry, and Gains and Losses (G&L) Sheet. Subtotals are provided for each ward/treating specialty.
At multidivisional facilities, a separate report will print for each division.
Scheduled Admissions List
This option provides a printout of scheduled admissions within a selected date range. The user has the option of producing reports listing future scheduled admissions which have been cancelled, future scheduled admissions which are still active, or both. The report is sorted chronologically by date of scheduled admission.
Information provided in the report includes division name, patient's name, last four digits of social security number, phone number, reservation date, treating specialty or ward location, care provider, whether or not the patient is to undergo surgery, the scheduled admission's status, etc. At multidivisional facilities, the report will be broken down by division.
The output format of this option may be changed by substituting a local template in place of the distributed template through the Supervisor ADT Menu option, Template Selection.
Treating Specialty Print
The Treating Specialty Print option provides a listing of treating specialties for your medical center. Information which may be provided includes facility treating specialty name, effective date, active status (YES/NO), treating specialty, providers, service, and abbreviation.
The EFFECTIVE DATE and ACTIVE? fields will be displayed for both the facility treating specialties (NAME column on the report) and the associated treating specialties from the SPECIALTY file (SPECIALTY column on the report).
The report can be sorted by one or more fields. (Consult the VA FileMan user manual for information on sorting techniques, if necessary.)
Depending on the sort specifications you have selected, the following prompt may appear: “Store in ‘SORT’ Template”. If this prompt does appear and you wish to set up a sort template, please refer to the VA FileMan user manual for further assistance with sort templates.
Depending on the ranges you specify and the size of your database, the report may be quite lengthy. You may wish to queue the report to run during off-hours.
VBC Form By Admission Date
This option provides a printout of the Veterans Assistance Unit Record for each veteran patient admitted within a specified date range. Records will be printed alphabetically by name. The Veterans Assistance Unit Record replaces the card used by the Veterans Benefits Counselor (VBC).
The following information is included on the form: patient name, DOB, patient ID#, claim \#, address, confidential address (if applicable), service data, admission data, monetary benefits, SC disabilities (if applicable), POW status, marital status, and Means Test category.
The bottom of the form provides space for the counselor to keep a record of the veteran's visits to his/her office.
VBC Form for Specific Patient
This option generates a printout of the Veterans Assistance Unit Record for a specific veteran patient or for a group of patients (up to 15). Records are printed alphabetically by name. The Veterans Assistance Unit Record replaces the card used by the Veterans Benefits Counselor (VBC).
The following information is included on the form: patient name, DOB, patient ID#, claim \#, address, confidential address (if applicable), service data, admission data, monetary benefits, SC disabilities (if applicable), POW status, marital status, and Means Test category.
The bottom of the form provides space for the counselor to keep a record of the veteran's visits to his/her office.
The Veterans Assistance Unit Record would be printed for every patient on the list.
<u>  
</u>Waiting List Output
The Waiting List Output option is used to generate a listing of those patients entered through the Waiting List Entry/Edit option who are currently awaiting future admission. The only prompts are for device selection.
The report will include the patient's name, priority group number, bedsection the patient is applying to, treating specialty, date/time of application, and whether or not the patient is service connected. At multidivisional facilities, the report will be separated by division.
Z07 Build Consistency Check
The Z07 Build Consistency Check option is used to print a report of inconsistent/missing data elements for a user-specified patient, and identify inconsistencies that prevent an HL7 Z07 Full Data Transmission message from being sent to the HEC.
For additional details on the inconsistencies found, run the Inconsistent Data Elements Report in the ADT Outputs Menu. For a complete list of possible inconsistencies, look at the documentation for the Determine Inconsistencies to Check/Don’t Check in the Supervisor ADT User Manual.
The output includes:
- Report title, including patient name and SN
- Patient name and SSN
- List of inconsistent/missing data elements found for the specified patient
