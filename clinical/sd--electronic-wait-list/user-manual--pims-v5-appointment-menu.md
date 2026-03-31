---
title: PIMS Version 5 Appointment Menu User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Appointment Menu
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5
patch_id: SD*5
group_key: "SD:SD:5"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 37%\\" /> <col style=\\"width: 24%\\" /> <col style=\\"width: 25%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><strong>Date</strong></td> <td><strong>Description (Patch # if applic.)</strong></td> <td><strong>Project Manager</strong></td> <td>"
audience: 
keywords: 
  - appointment
  - clinic
  - patient
  - date
  - appointments
  - time
  - selected
  - team
  - request
  - mark
page_count: 0
word_count: 9013
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/appt.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/appt.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

PIMS V. 5.3 Scheduling Module User ManualAppointment Menu

Appointment Management

Appointment Check-in/Check-out

Add/Edit Stop Codes

Append Ancillary Test to Appt.

Cancel Appointment

Chart Request

Check-in/Unsched. Visit

Computer Generated Menu

> Computer Generated Appointment Type Listing

> Edit Computer Generated Appointment Type

> Batch Update Comp Gen Appt Type for C&Ps

> Stop Code Listing (Computer Generated)

Delete Ancillary Test for Appt.

Discharge from Clinic

Display Appointments

Edit Clinic Enrollment Data

Enrollment Review Date Entry

Find Next Available Appointment

Make Appointment

Make Consult Appointment

Multiple Appointment Booking

Multiple Clinic Display/Book

New Enrollee Appointment Request Management Menu

> Management Edit

> Call List

> Tracking Report

No-Shows

Team/Position Assignment/Re-Assignment

Revision History

Initiated on 05/13/05

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>5/15/20</td>
<td>DG*5.3*996 – Removed original appointment request date from NEAR Tracking Report (Detailed) (p. 39).</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/11/19</td>
<td>DG*5.3*978 – Updated description for MANAGEMENT EDIT in Overview section (p. 6); Added message and prompt for appointment request at enrolled patient’s preferred facility (p. 37); added original appointment request date to Call List detailed report fields (p. 38) and Tracking Report detailed report fields (p. 39).</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/09/14</td>
<td><p>SD*5.3*622 – Updated options:</p>
<p>Make Appointment, (p. <a href="#p30">31</a>)</p>
<p>Multiple Appointment Booking, (p. <a href="#p32">33</a>)</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/13/05</td>
<td><p>SD*5.3*398 – Updated options:</p>
<p>Appointment Management</p>
<p>No-Shows</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/31/06</td>
<td>SD*5.3*478 – Consult/Scheduling Appointment Link – updated Appointment Management option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/22/07</td>
<td>SD*5.3*466 - Ambulatory Care, Phase II enhancements</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/7/07</td>
<td>Replace Primary Care Team/Posn Assign or Unassign option with Team/Position Assignment/Re-Assignment option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/1/08</td>
<td>DG*5.3*779 – Added New Enrollee Appointment Management Menu to the Appointment Menu</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/29/09</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/31/09</td>
<td><p>SD*5.3*441 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<p>Changed <em>environmental contaminants</em> to <em>SW Asia Conditions</em></p>
<p>Added Project 112/SHAD Indicator</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

  
Overview

The Appointment Menu is designed to enable scheduling clerks to perform a variety of duties including making appointments, requesting charts, cancelling appointments, discharging patients from clinic, reviewing clinic enrollment, and adding/editing stop codes. The Appointment menu also contains the Computer Generated menu which consists of options utilized in conjunction with the capture of stop code workload by packages other than PIMS. At this time, this menu would only be added if a site has V. 4.0 of Radiology loaded and is capturing stop code workload from that package.

The following is a brief description of the options contained in the Appointment Menu.

APPOINTMENT MANAGEMENT

This option is used to view appointments for a selected patient or clinic and to execute appropriate action(s) against these appointments, such as check-in and cancel.

APPOINTMENT CHECK-IN/CHECK-OUT

This option is used to check-in/check-out appointments for a selected clinic and date.

ADD/EDIT STOP CODES

This option is used to add/edit stop codes which were not captured through scheduled or unscheduled visits or through registration.

APPEND ANCILLARY TEST TO APPT.

This option is used to append an ancillary test to an existing appointment.

CANCEL APPOINTMENT

This option is used to cancel scheduled clinic appointments (past or future), rebook them, and print the necessary associated letters.

CHART REQUEST

This option is used to request a patient's chart for review without actually scheduling the patient for an appointment.

Overview

CHECK-IN/UNSCHED. VISIT

This option is used to schedule in an unanticipated appointment (for current date or past date) or to record patient's arrival time (check-in time) for statistical purposes.

Computer Generated Menu

Other packages (such as Radiology) can add stop codes/occasions of service to the PCE/Scheduling database. When these are added, an attempt is made to determine the appointment type for the visit. If this is not possible, an appointment type of COMPUTER GENERATED will be assigned. This is not a valid appointment type and should be changed to the appropriate type. The Computer Generated Menu provides outputs to determine which visits will need to be updated and options whereby the appointment type may be changed.

> COMPUTER GENERATED APPOINTMENT TYPE LISTING

> This option is used to generate a listing of visits with an appointment type of COMPUTER GENERATED.

> EDIT COMPUTER GENERATED APPOINTMENT TYPE

> This option is used to edit those visits with an appointment type of COMPUTER GENERATED to a valid appointment type.

> BATCH UPDATE COMP GEN APPT TYPE FOR C&Ps

> This option automatically updates all visits (within the selected parameters) which have an appointment type of computer generated due to a C&P visit to the COMPENSATION AND PENSION appointment type.

> STOP CODE LISTING (COMPUTER GENERATED)

> This option is used to produce a listing of one/many/all stop codes which have been automatically added to the PCE/Scheduling database by other packages.

DELETE ANCILLARY TEST FOR APPT.

This option is used to delete an ancillary test for a specific appointment. Ancillary tests include lab, x-ray, and EKGs.

DISCHARGE FROM CLINIC

This option is used to discharge a patient from a clinic in which he/she is actively enrolled.

DISPLAY APPOINTMENTS

This option is used to produce a listing of a patient's appointments.

Overview

EDIT CLINIC ENROLLMENT DATA

This option is used to edit clinic enrollment data for a selected patient, enter a new enrollment, or discharge a patient from a clinic.

ENROLLMENT REVIEW DATE ENTRY

This option is used to enter the date when an NSC outpatient clinic enrollment has been reviewed.

FIND NEXT AVAILABLE APPOINTMENT

This option is used to make a quick search for the next available appointment in a selected clinic.

MAKE APPOINTMENT

This option allows designated personnel to schedule clinic appointments and to book ancillary appointments such as lab, x-ray, and EKG.

MAKE CONSULT APPOINTMENT

This option is a clone of the Make Appointment option except that it allows holders of the SC CONSULT security key to make appointments for patients who are designated as “restrict consults” through PCMM.

MULTIPLE APPOINTMENT BOOKING

This option is used to make multiple appointments for a patient on a consecutive day/week basis.

MULTIPLE CLINIC DISPLAY/BOOK

This option is used to schedule a patient to 2-4 different clinics for one particular date. All chosen clinics must have an available slot on at least one identical day.

Overview

New Enrollee Appointment Request Management Menu

This menu assists with tracking of new enrollees who request an appointment.

> Management Edit

> This option provides a means to make an appointment request for a newly enrolled Veteran, update the appointment request status and/or add request comments.

> Call List

> This option lists veterans who requested an appointment during enrollment and do not have an appointment scheduled yet.

> Tracking Report

> This report lists times between the enrollment date of a veteran requesting an appointment on the 1010EZ and the date the appointment was actually made.

NO-SHOWS

This option is used to enter no-shows into the system. No-shows are those patients who did not report for scheduled appointments without previously notifying the facility.

Team/PosITION AssignMENT/RE-assignMENT

This option is used to assign patients to and discharge patients from PCMM teams and associated positions for primary care assignments.

  
Appointment Management

The Appointment Management option is used to view appointments for a selected patient or clinic and to execute appropriate action(s) against these appointments, such as check in and check out.

If a patient is selected, all appointments for the selected patient within the designated time frame will be displayed. This option is also designed to allow you to wand the record tracking barcode on the patient's medical record in selecting a patient.

If an appointment is associated with a consult or procedure request, “Cons” displays next to the appointment.

The beginning date of the report range is determined by the Appt Search Threshold parameter in the Scheduling Parameters (today's date minus the parameter entry), and the ending date will be 999 days in the future.

If selecting a clinic, you will be prompted for the date range of the display. Only clinic appointments within the designated time frame and with a status of NO ACTION TAKEN or ACTION REQUIRED are displayed.

Following is a list of actions that may be accomplished through the Appointment Management Screen.

AE Add/Edit GF GAF Score

AL Appointment Lists MA Make Appointment

CA Cancel Appointment NS No Show

CD Change Date Range PC PC Assign or Unassign

CI Check In PD Patient Demographics

CL Change Clinic PR Provider Update

CO Check Out PT Change Patient

CP Procedure Update RT Record Tracking

DC Discharge Clinic TI Display Team Information

DE Delete Check Out UN Unscheduled Visit

DL Wait List Display WD Wait List Disposition

DX Diagnosis Update WE Wait List Entry

EC Edit Classification

The following warning will be displayed after entering a no-show or cancelled appointment for patients with a Bad Address indicator.

\*\*This patient has been flagged with a bad address indicator, no letter will be printed.

Appointment Management

When "Check Out" (CO) is selected from the Appointment Management Screen, you have the option to display the Checkout Screen which uses the same type of format as the Appointment Management Screen. By selecting certain actions, such as Unscheduled Visit, Make Appointment, and Cancel Appointment, you automatically access other scheduling options. When Record Tracking is selected, you automatically access the Record Tracking software.

Checkout requirements for outpatient encounters that are transmitted via Ambulatory Care Transmission to the National Patient Care Database (NPCD) in Austin are now also required for inpatient encounters.

The Edit Classification action permits you to edit required classifications associated with regular appointments and stand-alone add/edits. The classifications include those questions related to whether or not the treatment was for a service connected condition, or related to Agent Orange/ionizing radiation/SW Asia Conditions exposure, Military Sexual Trauma (MST), head and/or neck cancer, combat service, or Project 112/SHAD. These questions appear if they are applicable to the patient.

All required classifications must be answered to complete the checkout process. You are not allowed to up-arrow out of these questions unless they are already answered or your site has set the ALLOW '^' OUT OF CLASS. parameter in the Set up a Clinic option (Supervisor menu) to YES.

You may now make primary care team and position assignments/unassignments through this option. You may notice the term “ambiguous data” in relationship to primary care information. “Ambiguous data” means that an inconsistency has occurred. It can be displayed for the primary care provider, associate provider, and team fields.

In accordance with Veterans Health Administration (VHA) Directive 97-059, Global Assessment of Function (Axis V, a.k.a. GAF) Scores will now be collected for outpatients with appointments in a Mental Health clinic. GAF data will be passed to the Mental Health system through Mental Health-provided APIs.

The GAF Score (GF) action allows users who hold the appropriate security key to enter/edit GAF Score information. For a provider to be displayed at the “Provider determining GAF Score:” prompt, the provider *must* have the appropriate security key. (Refer to the Security Section of the PIMS V. 5.3 Technical Manual for information about security keys.) Any appointments which require a new GAF score will be displayed with an asterisk (\*) in the first column. When using the GAF Score (GF) action, you need to confirm all entries. The default is NO.

Appointment Management

GAF Scores apply only to those patients with appointments in a Mental Health Clinic. If the patient’s appointment is *not* in a Mental Health clinic, the GAF score will not be checked and you will not be prompted to enter it. The clinic is considered to be a Mental Health Clinic if the Clinic Stop Code begins with a “5” and it is *not* one of the following Clinic Stops:

526 TELEPHONE/SPECIAL PSYCHIATRY

527 TELEPHONE/GENERAL PSYCHIATRY

528 TELE/HOMELESS MENTALLY ILL

530 TELEPHONE/HUD-VASH

536 TELEPHONE/MH VOC ASSISTANCE

537 TELEPHONE/PSYCHOSOCIAL REHAB

542 TELEPHONE/PTSD

546 TELEPHONE/IPCC

579 TELEPHONE/PSYCHOGERIATRICS

The GAF score requirement is based on a 90-day review (based on TODAY and the date of the previous GAF score). If the previous GAF score is greater than 90 days old, a new GAF score will be required. If a new GAF score is required, the Appointment Management Check Out screen will display the previous GAF date and score in the third line of the header. If no new GAF is required, the third line will be blank. After check out, if a new GAF score is required, and you do not return to the check out screen, you will get a warning that a new GAF is needed for the patient.

  
Appointment Check-in/Check-out

The Appointment Check-in/Check-out option is used to check in or check out appointments for a selected clinic and date. It may also be used to edit the checked in/out date/time on file for an appointment or delete a checked in date/time when one has been entered in error. If you wish to edit the checkout date, use the Check Out Date action on the Checkout Screen.

When using the checkout function, you may be prompted through a checkout interview. Classification, provider, diagnosis, and procedure code information for the selected appointment can be added/updated. You will be asked if treatment was related to Military Sexual Trauma (MST) only if the selected patient’s MST status is “Yes”.

Checkout requirements for outpatient encounters that are transmitted via Ambulatory Care Transmission to the National Patient Care Database (NPCD) in Austin are now also required for inpatient encounters.

You have the option to display the Checkout Screen through this option. By selecting certain actions, such as Unscheduled Visit, Make Appointment, and Cancel Appointment, you automatically access other scheduling options. When Record Tracking is selected, you automatically access the Record Tracking software.

When processing is completed, you are prompted to select another patient, clinic, or date without having to leave the option.

This option is designed to allow input from either a CRT keyboard or a barcode reader. In order to use the barcode capabilities, the clinic's appointment list must be printed on a device that supports the printing of barcodes. If the patient barcode on the appointment list is missing or unreadable, you may use the record tracking barcode on the patient's medical record.

In accordance with Veterans Health Administration (VHA) Directive 97-059, Global Assessment of Function (Axis V) (a.k.a. GAF) Scores will now be collected for outpatients with appointments in a Mental Health clinic. All new GAF data will be passed to the Mental Health system through Mental Health provided APIs. Please refer to the Appointment Management option for information about entering GAF scores with the new GAF Score (GF) option.

Add/Edit Stop Codes

The Add/Edit Stop Codes option is used to add/edit procedure codes which were not captured through scheduled or unscheduled visits or through registration. Procedure codes may also be deleted through this option. A new encounter may be added or procedure code data may be added/edited for an existing encounter.

If applicable, the appropriate service connection and exposure questions for the selected patient are asked. You will also be prompted through a checkout interview in which providers, diagnoses, and procedure codes for the selected encounter may be added, edited, or deleted.

Append Ancillary Test to Appointment

This option allows you to append an ancillary test to an existing appointment. There are three types of tests for which appointments can be made through this option; lab, x-ray, and EKG. Any other test must be booked through its associated clinic.

The system will list all pending appointments for the selected patient. You may schedule one or more of the ancillary tests to the selected appointment. You may have only one entry for each test (i.e., one lab time, one EKG time, one x-ray time). Any time the appointment is subsequently listed, the ancillary tests scheduled here will also appear.

Ancillary tests cannot be added to an appointment that has been checked out. Tests should be added to checked out appointments using the Add/Edit Stop Code functionality. Also, if an appointment has an ancillary test associated with it, an add/edit is automatically created when the appointment is checked out.

Cancel Appointment

This option is used to cancel scheduled clinic appointments (past or future), rebook them, and print the necessary associated letters. Appointments cancelled through this option are deleted entirely from the HOSPITAL LOCATION file (#44), but not the PATIENT file (#2). Therefore, a record of such cancellations will only appear in the patient's profile or Look Up on Clerk Who Made Appointment option.

It is important to note that when determining whether an appointment is past or future, the system looks at the present date AND time. For example, if it is presently August 1, 1993@0800, an appointment for August 1, 1993@07:30 would be considered past while one for August 1, 1993@0815 would be future. Multiple appointments may be cancelled for a patient using this option.

The system will display the current status of each appointment. This display may help prevent the accidental cancellation of an appointment that actually occurred by showing those past appointments which have a status of CHECKED IN.

Appointments that have been checked out cannot be cancelled. The checkout must first be deleted (through the Appointment Management option) before the appointment can be cancelled. The SD SUPERVISOR key is required to delete a checkout.

Appointments to a prohibited access clinic may only be cancelled by that clinic's specified user(s).

The automatic rebook function has been included in this option. This function automatically searches for the next available appointment in the clinic from which the cancellation has been made and reschedules the patient in that time slot. Several factors apply to this function:

- START TIME FOR AUTO REBOOK parameter in Set Up a Clinic option of the Supervisor menu - An actual time (i.e., 10:00 AM) is specified in this parameter. The system will not rebook an appointment in a time slot prior to this time.
- MAX \# DAYS FOR AUTO REBOOK parameter in Set Up a Clinic option of the Supervisor menu - This parameter specifies the maximum number of days into the future beyond which rebooked appointments may not be made.

Cancel Appointment

- If auto rebooking of appointments has occurred while utilizing this option, the "Cancelled and Auto-Rebooked Report" will be generated. This report shows the new date/time of the rebooked appointments including the ancillary test time. There are three parameters that affect the auto-rebooking of appointments with associated ancillary tests. They are:

> OP LAB TEST START TIME

> OP EKG START TIME

> OP X-RAY START TIME

> If a time is entered at these parameters, the ancillary test time will not rebook before the start time specified in the parameter.

- Only one cancelled appointment per clinic may be rebooked. If you wish to rebook multiple appointments to the same clinic, you may do so through the Multiple Appointment Booking option on the Appointment Menu.
- When using this function to rebook cancelled appointments which were for future dates, you should be careful to specify a date where the new appointment will not occur earlier than the one which was just cancelled.

The default at the “In {clinic name} Start Rebooking From What Date” prompt has been set to TODAY + 10 to allow time (ten days) for patient notification of the rescheduled appointment. If you enter a date which is less than ten days into the future, the system will begin its search ten days beyond that date. For example, if you enter T+5, the search will actually begin at T+15.

The clinic(s) involved must have the appropriate letter type assigned through the Set Up a Clinic option for the “Do you wish to print letters for the cancelled appointment(s)? ” prompt to appear.

Chart Request

This option is used to request a patient's chart for review without actually scheduling the patient for an appointment. It could be used in a case where a physician has ordered lab tests for a particular patient and wishes to review those results in one week but not see the patient for another two weeks. You may enter multiple patients for any selected date. The patient need not be enrolled in the clinic; however, he or she must be actively registered at the facility.

No appointment is scheduled for the patient and no appointment letters are generated. The patient will appear on the clinic's file room list with no appointment time.

Check-in/Unsched. Visit

The Check-in/Unsched. Visit option is used to schedule in an unanticipated appointment (for current date or past date) or to record a patient's arrival time (check in time) for statistical purposes for existing and/or unscheduled appointments.

To add a new unscheduled appointment, the patient must be actively enrolled in the selected clinic. If the patient is not enrolled in the specified clinic, you will have the opportunity to either enroll or schedule the patient for a consultation.

you may also check out a patient using this option when adding a new unscheduled appointment. When you choose checkout, a checkout interview is displayed. Depending on how parameters are set at your site and classification criteria, the checkout interview may prompt you for provider, diagnosis, classification, and procedure code information. The default provider and diagnosis assigned to the clinic through the Set up a Clinic option (if any) appear as defaults. If all required information is entered, the appointment is automatically checked out.

If an unscheduled appointment is entered, you may print a routing slip for the visit. If you are entering the unscheduled appointment at the time it is actually occurring, you may be able to issue a request for the patient's records. This will only occur if your site is running the Record Tracking package and the clinic has been so defined in Record Tracking. A request notice is automatically printed on the appropriate file room printer.

If you use the Check-In function to process an unscheduled appointment for a patient who is determined to require a completed Means Test, you will receive a screen alert notifying you of the requirement and will not be allowed to check-out the appointment. The appointment will remain in the status of Action Required.

If while adding a new unscheduled appointment, you select a clinic where the clinic parameter, ASK FOR CHECK IN/OUT TIME, (Supervisor menu - Set Up a Clinic option) is set to YES, you will be prompted for a checked in/out date/time.

To schedule an appointment type of collateral, EMPLOYEE, or SHARING AGREEMENT requires the patient to be registered with a primary eligibility or other entitled eligibility of collateral, EMPLOYEE, or SHARING AGREEMENT. If the selected appointment type has subcategories, you will be asked to select the appropriate subcategory.

Any appointment made through this option will have a purpose of visit status of UNSCHEDULED VISIT.

Computer Generated MenuComputer Generated Appointment Type Listing

Other packages (such as Radiology) can add stop codes/occasions of service to the PCE/Scheduling database. When these are added, an attempt is made to determine the appointment type for the visit. If this is not possible, an appointment type of COMPUTER GENERATED will be assigned. This is not a valid appointment type and should be changed to the appropriate type. The Computer Generated Menu provides outputs to determine which visits will need to be updated and options whereby the appointment type may be changed.

The Computer Generated Appointment Type Listing option is used to generate a listing of visits with an appointment type of COMPUTER GENERATED for a selected date range. These visits must be updated to a valid appointment type through the Edit Computer Generated Appointment Type option for the clinic to receive workload credit.

The report may be run for one/many/all divisions (at multidivisional facilities) and one/many/all stop codes. The output will be sorted by stop code. Patients will be listed alphabetically within each stop code. The patient name, patient ID, visit date/time, and reason for COMPUTER GENERATED appointment type will be provided for each applicable visit. The total number of computer generated appointment types will be shown for each selected stop code.

Computer Generated MenuEdit Computer Generated Appointment Type

Other packages (such as Radiology) can add stop codes/occasions of service to the PCE/Scheduling database for workload credit. When these are added, an attempt is made to determine the appointment type for the visit. If this is not possible, an appointment type of COMPUTER GENERATED will be assigned. The Edit Computer Generated Appointment Type option is used to edit those visits with an appointment type of COMPUTER GENERATED to a valid appointment type.

You may select the scheduling visit entries by visit date, first initial of patient last name plus last four digits of SSN, patient name or SSN, or ALL entries. If entering SSN, use the NNNNNNNNN format (no spaces or dashes).

Computer Generated MenuBatch Update Comp Gen Appt Type for C&Ps

The Batch Update Comp Gen Appt Type for C&Ps option will automatically update all visits within the selected date range whose reason for having a COMPUTER GENERATED appointment type is "C&P" to the COMPENSATION AND PENSION appointment type.

If necessary, you should utilize the Computer Generated Appointment Type Listing and the Edit Computer Generated Appointment Type options of this menu before using this option. The Computer Generated Appointment Type Listing option will provide you with a list of those visits whose reason for having a COMPUTER GENERATED appointment type is "C&P". Any of these visits not related to a C&P visit should then be edited through the Edit Computer Generated Appointment Type option to reflect the appropriate appointment type.

The output generated by this option will list all applicable appointments which have been updated. The date/time and patient name for each visit is displayed. Total number of visits updated is also provided.

Computer Generated MenuStop Code Listing (Computer Generated)

The Stop Code Listing (Computer Generated) option is used to provide a listing of stop codes for a selected date range which have been added to the PCE/Scheduling database by packages other than Scheduling. Packages (such as Radiology) may add stop codes/occasions of service to the PCE/Scheduling database for workload credit.

The output may be run for one/many/all divisions (at multidivisional facilities) and one/many/all stop codes. The output will be sorted by stop code. Patients will be listed alphabetically within each stop code. The patient name, patient ID, and visit date/time will be provided for each applicable visit. The total number of computer generated stop codes will be shown for each selected code.

Delete Ancillary Test for Appointment

The Delete Ancillary Test for Appointment option is used to delete an ancillary test for a specific appointment. Ancillary tests include lab, x-ray, and EKGs. In order to delete these tests through this option, the test must have been scheduled in association with a clinic appointment.

Ancillary tests cannot be deleted from an appointment that has been checked out. The tests must first be deleted using the Add/Edit Stop Code functionality. Also, if the appointment checkout is deleted, any add/edits associated with that appointment are also automatically deleted.

Discharge from Clinic

The Discharge from Clinic option is used to discharge a patient from a clinic in which he/she is actively enrolled. You may discharge the patient from one/many/all clinics. If the patient has pending appointments in a selected clinic, those appointments must be cancelled before you would be able to discharge the patient from that clinic.

You may enter a reason for discharge (2-80 characters); however, this is not required in order to discharge the patient.

Once a date of discharge has been entered, the patient will be discharged from the clinic. If this was done in error, the user would need to utilize the Edit Clinic Enrollment Data option of the Appointment Menu to restore the patient to the clinic.

When you discharge a patient from a clinic using this option, a MailMan message will be sent to the applicable primary care team members who chose to receive Team Notifications if all of the following criteria are met.

- The clinic is associated to only one team.
- The patient is currently enrolled in the team.
- Auto-discharge for the team must be enabled.
- The patient is not assigned to a position on the team.

Display Appointments

This option is used to produce a listing of a patient’s appointments. The output will show the patient's name, social security number, appointment date and time, length of appointment, clinic, and date/time report printed.

The user may choose to print only pending appointments, or pending and past appointments within a specified date range. Past appointments with a NO-SHOW or CANCELLED status will be so displayed if previously entered. Past appointments with a status of NO ACTION TAKEN will also be displayed.

Edit Clinic Enrollment Data

This option allows the user to edit clinic enrollment data for a selected patient. The capability also exists to enter a new enrollment or discharge a patient from a clinic. You will not be able to enroll a patient who is designated as having “restricted consults” through PCMM unless you hold the SC CONSULT security key.

Enrollment information which may be edited through this option includes enrollment clinic, patient status (Opt or AC), review date, date of discharge, and reason for discharge.

When you enroll a patient in a new clinic using this option, the patient will be assigned to the primary care team if all of the following criteria are met. A MailMan message will be sent to the applicable team members who chose to receive Team Notifications.

- The clinic is associated to only one team.
- The patient is not currently enrolled in the team.
- Auto-enrollment for the team must be enabled.
- The team must be open. (Team Closed box not checked.)
- The patient must be a veteran if the team is a Primary Care team.

When you discharge a patient from a clinic using this option, the patient will be discharged from the associated primary care team if all of the following criteria are met. No mail message will be generated.

- The clinic is associated to only one team.
- The patient is currently enrolled in the team.
- Auto-discharge for the team must be enabled.
- The patient is not assigned to a position on the team.

When you delete a clinic enrollment using this option, you will be notified of the patient’s discharge from the associated team if all of the following criteria are met. No mail message will be generated.

- You enter “@” at the “Select ENROLLMENT CLINIC:” or “Select DATE OF ENROLLMENT:” prompts.
- The clinic is associated to only one team.
- The patient is currently enrolled in the team.
- Auto-discharge for the team must be enabled.
- The patient is not assigned to a position on the team.

Enrollment Review Date Entry

The Enrollment Review Date Entry option is used to enter the date when a NSC outpatient clinic enrollment has been reviewed. These enrollments are reviewed periodically (usually once a year) to assure the need for continuing treatment. The existence of this date will prevent the "review needed" message from printing on the appointment list for a period of one year from the review date entered.

You will be prompted for the clinic name, patient name, and review date. If you enter a patient whose enrollment did not require a review, one of several different messages may appear explaining why a review date is not needed.

Find Next Available Appointment

This option enables you to make a quick search for the next available appointment in a selected clinic. You can select multiple clinics or teams (up to a maximum of 20 for each).

If teams are selected, the associated clinics for positions on the selected teams are used. The output display includes all clinics that meet in the user-specified date range and that have the specified appointment length available.

The “Appointment Length Needed” prompt will only appear if the selected clinic is a variable length clinic. The appointment length must equal, or be a multiple of, the increment minutes per hour.

The availability pattern will be displayed for a maximum of 3 days of appointments for each selected clinic. This will repeat until you either discontinue the search or no other available date in the selected date range is found.

If you choose to make an appointment through this option, you will access the Make Appointment option. See that option documentation for assistance if necessary.

Make Appointment

The Make Appointment option allows designated personnel to schedule clinic appointments. It also allows for the booking of ancillary appointments such as lab, x-ray, and EKG. You may have only one entry for each test (i.e., one lab time, one EKG time, one x-ray time). In the case of prohibited clinics (so designated during clinic set-up), only those users with privileged access will be able to book appointments.

Any pending appointments the patient has for the selected clinic and/or other clinics can be displayed. If the patient is not enrolled in the selected clinic, you will have the opportunity to either enroll or schedule the patient for a consultation. You will not be able to make a consult appointment through this option for patients who are designated as “restrict consults” through the Primary Care Management Module (PCMM). If you hold the SC CONSULT security key, you may do this through the Make Consult Appointment option.

With PCMM loaded, when you enroll a patient in a new clinic using this option, a MailMan message will be sent to the applicable team members who chose to receive Team Notifications, if all of the following criteria are met.

- The clinic is associated to only one team.
- The patient is not currently enrolled in the team.
- Auto-enrollment for the team must be enabled.
- The team must be open. (Team Closed box not checked.)
- The patient must be a veteran if the team is a Primary Care team.

Numerous messages may be displayed while using this option depending on whether or not the slot requested is available. These include such information as patient already has an appointment on that date/time, clinic does not meet on that date, or appointment can't be made while clinic is inactivated. If an appointment will be an overbook, you are notified and allowed to overbook if so specified in the clinic set-up and if you hold the SDOB security key.

If you attempt to schedule a regular appointment for a patient who is determined to require a completed Means Test, you will receive a screen alert notifying you of the requirement and will not be allowed to proceed with scheduling of the appointment unless you hold the EAS MTOVERRIDE security key. Holders of that key will be allowed to proceed with the appointment process following the screen alert.

Make Appointment

If the appointment is made for the current date, the user may be able to issue a request for the patient's records. In order to do this, the Record Tracking package must be running at your site and the selected clinic must be defined in Record Tracking. Dependent on the clinic set-up, you may be allowed to request that previous x-ray results are sent to the clinic for the appointment. The option also provides the ability to view the selected clinic availability chart by entering an up-arrow \<^\> at the "Select PATIENT NAME" prompt. You may wish to see what slots are available in the clinic before actually enrolling the patient.

If the patient has an appointment on the exact date and time you are booking, you are given the opportunity to cancel the previously scheduled appointment and book the new one. As appointments are made in the clinic, the number of slots available per hour is decreased accordingly. If four slots are available at 8:00 and you book an hour long (60 minutes) appointment, the result would be:

PRIOR TO APP'T NEXT DISPLAY

\|8 \|9 \|8 \|9

\[4 4 4 4\|4 4 4 4\| \[3 3 3 3\|4 4 4 4\|

Overbooks are represented by ascending letters of the alphabet, and appointments booked for a time a clinic does not usually meet are represented by an asterisk \<\*\>. In the example below, the 9:30 slot has been overbooked once, the 10:00 slot twice and the 11:00 slot shows no appointments left (i.e., if an appointment were to be booked into the 11:00 slot, the next display would show an "A") and one of the 11:00 appointments is scheduled to go 15 minutes into the 12:00 slot, which is not a time the clinic usually meets.

\|8 \|9 \|10 \|11 \|12 \|1

\[4 3 3 2\|2 2 A A\|B B 1 1\|0 0 0 0\]\* \[....

If a clinic has been inactivated for a given period of time, the day(s) the clinic has been inactivated will not appear in the chart. A message will be displayed to indicate this.

If the appointment time is outside of the normal hours for the clinic and does not occur before the hour that the clinic display begins or ends, and you hold the overbook key, you will be asked if you wish to overbook. If the above conditions are true and you do not hold the overbook key, you will be told that no open slots are available for booking. Otherwise, the system will ask “WHEN??”, signifying that this time is not an allowable time to book an appointment.

  
Make Appointment

If the clinic is cancelled only for a portion of a day it is scheduled to meet, this will be represented in the display by "XXXs" printed in the cancelled time slots. The system will alert you with a message if you attempt to schedule during that time. For example, if a clinic meets from 8:00 to 12:00 and the clinic has been cancelled from 11:00 to 12:00, you would see:

\|8 \|9 \|10 \|11 \|12 \|

\[4 4 4 4\|4 4 4 4\|4 4 4 4\|XXXXXXX\|XXXXXXX\|

Entire days that have been cancelled will appear as follows:

\|8 \|9 \|10 \|11 \|12

\*\*\*CANCELLED\*\*\*

To schedule an appointment type of collateral, EMPLOYEE, or SHARING AGREEMENT requires the patient to be registered with a primary eligibility or other entitled eligibility of COLLATERAL, EMPLOYEE, or SHARING AGREE-MENT. If the selected appointment type has subcategories, you will be asked to select the appropriate subcategory. This will also occur in other options where you may make an appointment - Make Consult Appointment, Multiple Appointment Booking, etc.

If you schedule an appointment in the past, depending on how parameters are set at your site, you may be prompted for a checkout date/time, and a checkout interview may be displayed. The checkout interview may prompt for classification, provider, diagnosis, and procedure codes for the selected appointment.

If you enter a past appointment date after 10/1/93 but prior to today, the appointment is automatically checked out. If you enter a past appointment for today (for example, it is now August 1, 1996@0800 and you enter an appointment for T@07:30), you are prompted to select either check in or checkout. It is important to remember that date and time are considered when determining whether an appointment is past or future.

<span id="p30" class="anchor"></span>Make Appointment

A query is automatically sent to the Health Eligibility Center (HEC) when an appointment is scheduled through this option. This query will determine if a Means Test or Copay Exemption Test (with Income Screening information) has been completed for the veteran for a specified income year. The HEC will process the query, and if there is a completed Means Test or Copay Exemption Test (with Income Screening information), the HEC will transmit the Primary test and any Hardship determinations to the VAMC that sent the query.

During the creation of an appointment when the user reaches the following prompt and answers ‘YES’, the system pauses for 3 seconds to display the desired date for the appointment:

IS THIS A 'NEXT AVAILABLE' APPOINTMENT REQUEST? YES

APPOINTMENT DESIRED DATE: Nov 05, 2014 (display pauses for 3 seconds)

Calculating follow-up status.

. . .

Just before exiting the creation of an appointment, the user is given the opportunity to print the pre-appointment letter for the patient:

WANT TO PRINT THE PRE-APPOINTMENT LETTER? No//. If the user answers YES, then the DEVICE prompt is presented to print the letter. If there is no pre-appointment letter defined, no device prompt is presented to the user.

Make Consult Appointment

This option allows designated personnel to schedule clinic appointments. This is a clone of the Make Appointment option, except that it allows holders of the SC CONSULT security key to make appointments for patients who are designated as “restrict consults” through PCMM.

Patients are designated as “restrict consults” as a result of the following actions.

- Restrict Consults is checked on the Settings tab of the Team Profile screen for a team to which the patient is assigned.
- Restrict Consults for this Patient is checked during a Patient-Team Assignment.

You will be notified of the team assignments that created this designation. If you continue to make an appointment or enroll the patient in the clinic, a MailMan message will be sent to the applicable team members who chose to receive Consult Notifications.

If you need further help with this option, please refer to the Make Appointment option in this section.

<span id="p32" class="anchor"></span>Multiple Appointment Booking

The Multiple Appointment Booking option is used to make multiple appointments for a patient on a consecutive day/week basis. This capability eliminates the time-consuming scheduling of individual appointments to clinics such as Dialysis or Physical Therapy where the patient may report daily or weekly for a long period of time.

You may choose to book the appointments daily or weekly for as many days/weeks in advance as permissible through the clinic set-up. If you choose to book by day, the appointments will be booked for consecutive days. Saturdays and Sundays are optional. Advance booking by week allows you to book appointments on the same day of the week for consecutive weeks.

You may display any pending appointments the patient has for the selected clinic and/or other clinics. If the patient is not enrolled in the selected clinic, you will have the opportunity to either enroll or schedule the patient for a consultation.

The system may display numerous messages when utilizing this option depending on whether or not every slot requested is available. These include such information as patient already has an appointment on that date/time, clinic does not meet on that date, or appointment can't be made while clinic is inactivated. If an appointment will be an overbook, you will be notified and allowed to overbook if so specified in the clinic set-up and if you hold the SDOB security key. At the end of the option, the system lists each individual appointment scheduled and the total number of appointments made.

If you schedule an appointment in the past, depending on how parameters are set at your site, you may be prompted for a checkout date/time, and a checkout interview may be displayed. The checkout interview may prompt for classification, provider, diagnosis, and procedure codes for the selected appointment. The default provider and diagnosis assigned to the clinic through the Set up a Clinic option (if any) appear as defaults.

The system then automatically checks out that appointment. It is important to note that when determining whether an appointment is past or future, the system looks at the present date AND time. For example, if it is presently August 1, 1996@0800, an appointment for August 1, 1996@07:30 would be considered past while one for August 1, 1996@0815 would be future.

When using the option ‘EP’ (Expand Entry) for a given appointment in a series, the Desired Date field is displayed with the desired date for the appointment. The Desired Date for the initial appointment will reflect the Desired Date entered during the scheduling process. The subsequent appointments’ Desired Date will be set to the date of the appointment.

Multiple Appointment Booking

Ancillary tests for appointments booked through this option must be made through the Append Ancillary Test to Appt. option.

You may issue a request for the patient’s records if today's date and the appointment date are the same and the Record Tracking package is running at your site.

Multiple Clinic Display/Book

This option enables you to schedule a patient to between 2 and 4 different clinics for one particular date. All chosen clinics must have an available slot on at least one identical day, starting from the date the search begins to the earliest maximum date for future booking (the default date to end the search) or another selected end date. The earliest maximum date for future booking is defined in the clinic set-up.

You may enroll the patient in a selected clinic or schedule a consultation. Capability is also provided to include notification of scheduled ancillary tests, such as lab, x-ray or EKG, in the patient appointment letters. Depending on individual clinic set-up, you may be able to request previous x-rays be sent to the clinic.

The availability patterns for all of the selected clinics are displayed showing the first date (within the date range selected) an appointment may be scheduled. Each clinic pattern is then individually listed when booking into that clinic.

If overbooking is allowed in the selected clinic and you hold the SDOB security key, the following prompt appears whenever you attempt to schedule an appointment which is outside of the normal clinic hours, or all available time slots are filled.

OVERBOOK!...OK? NO//

If overbooking is not allowed in the selected clinic and/or you do not hold the SDOB security key, whenever you attempt to schedule an appointment that is outside of the normal clinic hours, or if all available time slots are filled, the following message is displayed:

WHEN??

For past appointments, you may also check the appointment in or out. If the ASK FOR CHECK IN/OUT TIME (Supervisor menu - Set Up a Clinic option) parameter is set to YES for the selected clinic, you are prompted for a check in/out date. When checkout is selected, a checkout interview may be displayed. Depending on how parameters are set at your site and classification criteria, the checkout interview may prompt you for provider, diagnosis, classification, and procedure code information for the visit. The default provider and diagnosis assigned to the clinic through the Set up a Clinic option (if any) appear as defaults.

Multiple Clinic Display/Book

It is important to note that when determining whether an appointment is past or future, the system looks at the present date AND time. For example, if it is presently August 1, 1993@0800, an appointment for August 1, 1993@07:30 would be considered past while one for August 1, 1993@0815 would be future.

If the Record Tracking package is running at your site and you make an appointment for the current date, you may issue a request for the patient’s records. If you answer yes at the prompt, a record request will be generated to the file room.

New Enrollee Appointment Request Management MenuManagement Edit

The Management Edit option provides a means to make an appointment request for a newly enrolled Veteran, update the appointment request status, and/or add appointment request comments.

Patients are removed from the Call List through this option by updating the status to *cancelled* or *filled*. When the status is updated to cancelled, the reason for cancellation must be entered in the COMMENT field.

The dates when the STATUS and COMMENT fields were last edited are displayed. The following fields are displayed and are not editable: Appointment request on 1010Ez and Appointment request date.

If a patient is selected who has not requested an appointment, an appointment request may be made if the patient is enrolled and the request is being made at the patient’s preferred facility. The following message and prompt are displayed:

PREFERRED FACILITY: ZZ DUP ALBANY.VA.GOV (500)

APPOINTMENT REQUEST ON 1010EZ: NO

Does the New Enrollee want an appt. with a VA doctor/provider

at ZZ DUP ALBANY.VA.GOV (500)?: NO//

If the appointment request is changed to “YES”, the appointment request date is prompted:

Date the Appointment Request Made?: //

Future dates may not be entered.

New Enrollee Appointment Request Management MenuCall List

The Call List option produces a report of those veterans who requested an appointment during enrollment and have yet to have that appointment scheduled. It provides a means to track the status of new enrollee appointment requests. The request will stay on the Call List until an appointment is made (filled) or the request is cancelled.

The only prompts are for report format (detailed or short) and device.

The short report includes the following fields: name, last four digits of social security number, appointment request date, appointment request status, residence phone \#, cellular phone \#.

The detailed report includes the fields found on the short report plus the following fields: original appointment request date (the date the VA was first notified the enrolling patient is requesting an appointment), appointment request comments, enrollment category, enrollment status, enrollment priority, combat vet status, combat vet end date.

The summary portion of the output displays the total number of veterans in each of the following statuses and appears on both the detailed and short formats.

> EWL (Electronic Wait List)

> In process/veteran contacted

> Pending Action

New Enrollee Appointment Request Management MenuTracking Report

The Tracking Report option provides managers with a report listing the times between the enrollment date of the veteran requesting an appointment and the date the appointment was scheduled (filled).

The only prompts are for report format (detailed or summary), appointment request start and end dates, and device.

The summary report displays the total number of veterans in each of the following statuses for the selected date range.

> EWL (Electronic Wait List)

> In process/veteran contacted

> Pending Action

> Cancelled

> Filled

The detailed report includes what is displayed in the summary report plus the following fields: patient last name, last four digits of social security number, appointment request date, appointment request status, scheduled appointment date, appointment request comments, enrollment priority/combat vet status, number of days between appointment requested and actual appointment date.

No-Shows

This option is used to enter no-shows into the system. No-shows are patients who did not report for scheduled appointments without previously notifying the facility. No-shows are entered by date with further breakdown by clinic and individual patient name. Several clinics/patients may be entered.

Appointments that have been checked out cannot be no-showed. The checkout must first be deleted, (through the Appointment Management option) before the appointment can be no-showed. The SD SUPERVISOR key is required to delete a checkout.

If there is only one appointment for the selected patient which meets the specified criteria and that appointment has not yet been checked in, the system will automatically no-show the appointment. However, if this one appointment has been checked in, it will be necessary for you to make a selection. This will prevent the accidental no-showing of an appointment that actually occurred. Also, if there are two or more appointments for the patient for the selected clinic on a specified date, you are prompted to select the correct one.

If a selected patient was previously entered as a no-show for the date and clinic you have chosen, the system displays a message and you have the opportunity to delete the no-show status. It is important to note that if the erased no-show was automatically rebooked, the rebooked appointment is not cancelled.

The option provides the ability to request all the no-shows that were just entered to be auto-rebooked and to have each clinic's assigned No-Show letter printed. Each clinic should have a No-Show letter assigned to it through the Set Up a Clinic option. You may print the letter for all selected clinics or for an individual clinic.

A list of those patients with a Bad Address indicator will print after the no-show letters have printed. Letters for those patients will not print.

The system will display a listing of the selected patients who have exceeded the maximum number of no-shows for the given clinic. These patients' records should be reviewed to see if they warrant discharge from clinic. If the patient was auto-rebooked, that appointment needs to be cancelled before discharge from clinic can be accomplished.

All no-shows should be entered into the system in a timely fashion and prior to running the AMIS Sample File for submission to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)), so that these visits are not counted as kept appointments.

No-Shows

If auto-rebooking of appointments has occurred while utilizing this option, a No-Show Auto-Rebook Report will be generated for each applicable clinic. This report shows the new date/time of the rebooked appointments including the ancillary test time. If an up-arrow \<^\> is entered at the DEVICE prompt, auto-rebooking of appointments will NOT take place.

There are three parameters that affect the auto-rebooking of appointments with associated ancillary tests. They are OP LAB TEST START TIME, OP EKG START TIME, and OP X-RAY START TIME. If these parameters contain a value, the ancillary test time will not rebook before the start time specified in the parameter.

Team/Position Assignment/Re-Assignment

The Team/Position Assignment/Re-Assignment option determines a patient's Primary Care status. This option is also available from the PCMM GUI - see note below. Based on status, it will prompt the user to select from the following choices:

- Assign patient to Primary Care (PC) or non-primary care team (if not currently assigned).
- Assign patient to PC or non-primary care Practitioner position (if assigned to a team, but not PC practitioner). User can perform a look-up by either position name or the current practitioner assigned to the position.
- Un-assign from team (if assigned to a PC or non-PC team). If patient is assigned to PC position, both the PC position and PC team will be unassigned.
- Un-assign from position
- While assigning/un-assigning from a position: If the position has an Associated Clinic, the user will be prompted to enroll/discharge the patient from that Associated Clinic.

> **NOTE:** This option must be used in the PCMM GUI if you need to:

- Edit or delete
- Re-assign patients with future PC assignments
- If the team position does not have a practitioner currently assigned to it