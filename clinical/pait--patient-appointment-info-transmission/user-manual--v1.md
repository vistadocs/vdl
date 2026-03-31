---
title: PAIT Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: PAIT
app_name: Patient Appointment Info. Transmission
section: CLI
app_status: active
pkg_ns: PAIT
patch_ver: 1
patch_id: PAIT*1
group_key: "PAIT:PAIT:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - pait
  - appointment
  - table
  - date
  - transmission
  - contents
  - patient
  - error
  - manual
  - span
page_count: 0
word_count: 5296
section_count: 13
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Appointment_Info_Transmission/pait_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Appointment_Info_Transmission/pait_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=169"
---

![](pait-version-1-user-manual/001.png)

Office of Information & Technology (OI&T)

VistA Maintenance Team

Patient Appointment Information Transmission (PAIT)

User Manual

March 2010

Document Tracking Page – Internal Use Only

Document Control Grid

| Document Owner | VistA Maintenance Team                                      |
|--------------------|-----------------------------------------------------------------|
| Document Title | Patient Appointment Information Transmission (PAIT) User Manual |
| Filename       | pait_user_manual.doc                                            |

Revision History Table

| Date | Description                                        | Project Manager                | Technical Writer               |
|----------|--------------------------------------------------------|------------------------------------|------------------------------------|
| 02/2016  | Per patch SD\*5.3\*639, disable PAIT HL7 Transmission. | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 03/2010  | Initial Version 1.0                                    | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

  
Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview of Patient Appointment Information Transmission](#overview-of-patient-appointment-information-transmission)
  - [Additional Reference](#additional-reference)
- [Appointment Selection and Transmission](#appointment-selection-and-transmission)
  - [Patient Status Codes](#patient-status-codes)
  - [Combat Veteran Information](#combat-veteran-information)
    - [Combat Veteran Eligibility](#combat-veteran-eligibility)
    - [Combat Veteran End Date](#combat-veteran-end-date)
    - [Combat Veteran Indication](#combat-veteran-indication)
    - [Combat Veteran History](#combat-veteran-history)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [Rejected Appointment Processing](#rejected-appointment-processing)
- [PAIT Options](#pait-options)
  - [Taskman PAIT Transmission \[SD-PAIT TASKED TRANSMISSION\]](#taskman-pait-transmission-sd-pait-tasked-transmission)
  - [Manual Startup PAIT Transmission \[SD-PAIT MANUAL TRANSMISSION\]](#manual-startup-pait-transmission-sd-pait-manual-transmission)
  - [PAIT Reports \[SD-PAIT REPORTS\]](#pait-reports-sd-pait-reports)
    - [Acknowledgement Summary \[SD-PAIT ACK SUMMARY\]](#acknowledgement-summary-sd-pait-ack-summary)
    - [Patient HL7 Location \[SD-PAIT PATIENT HL7 LOCATION\]](#patient-hl7-location-sd-pait-patient-hl7-location)
    - [Pending Transmissions \[SD-PAIT PENDING\]](#pending-transmissions-sd-pait-pending)
    - [Rejected Transmissions \[SD-PAIT REJECTED\]](#rejected-transmissions-sd-pait-rejected)
    - [Transmission Summary \[SD-PAIT TRANSMISSION SUMMARY\]](#transmission-summary-sd-pait-transmission-summary)
    - [Manual Batch Reject \[SD-PAIT MANUAL BATCH REJECT\]](#manual-batch-reject-sd-pait-manual-batch-reject)
    - [SD-PAIT Last Run Repair \[SD-PAIT REPAIR\]](#sd-pait-last-run-repair-sd-pait-repair)
- [Rejection Codes and Corrections](#rejection-codes-and-corrections)
  - [Error Code Set](#error-code-set)
- [Mail Messages](#mail-messages)
  - [Job Started](#job-started)
  - [PAIT Batch Acknowledgement](#pait-batch-acknowledgement)
  - [PAIT Completion Message](#pait-completion-message)
  - [Prevention of PAIT Manual Transmission](#prevention-of-pait-manual-transmission)

## Overview of Patient Appointment Information Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Appointment Information Transmission (PAIT) was developed and released in patch SD\*5.3\*290 to provide patient appointment wait time statistics to the national database in Austin, TX. An initial seeding routine scanned patient appointments created from September 1, 2002 to the date that Patch SD\*5.3\*290 was installed. The One-Time Option Queue from the TaskMan Management menu was used to start SD-PAIT TASKED TRANSMISSION on a scheduled date per site—each of the 128 sites at the time was assigned its own start date.

Patch SD\*5.3\*290 was released on November 26, 2003. Only Pending appointments were selected for the seeding process. Subsequent bimonthly PAITs update <span class="mark">REDACTED</span> data is wrapped in HL7 batch messages and transmitted to the <span class="mark">REDACTED</span>. This additional data supplements the existing Clinic Appointment Wait Time extracts 1 and 2. Transmissions should be scheduled on the 1<sup>st</sup> and 15<sup>th</sup> day of each month. The bi-monthly task will collect and format data for HL7 batch transmission.

PAIT enhances the process of collecting and storing appointment data for bi-monthly transmission to the AITC:

- Capturing selected data about the patient’s appointment eligibility including Combat Veteran and Military History
- Identifying the date and time services were desired, scheduled and provided
- Tracking and updating appointments through checkout, cancellation, rebooking, etc.

The intended audience for this manual includes hospital facility staff responsible for identifying and correcting rejected appointment data, scheduling the PAIT bimonthly transmission task, and anyone who wishes to understand PAIT options in VistA and the PAIT appointment collection and transmission process.

Starting April 1, 2015, the Veterans Health Administration Support Service Center (VSSC) no longer uses the patient appointment scheduling data that was sent from each VistA site, so the bimonthly PAIT data transmission to AITC is no longer needed and the transmission has been stopped with Scheduling patch SD\*5.3\*639.

Patch SD\*5.3\*639 release includes:

- Disables SD-PAIT logical Link in the HL LOGICAL LINK (#870) file.
- Unschedules SD-PAIT HL7 nightly background job \[SD-PAIT TASKED TRANSMISSION\].
- Places the following options ‘out of order’:
- SD-PAIT MANUAL BATCH REJECT
- SD-PAIT MANUAL TRANSMISSION
- SD-PAIT TASKED TRANSMISSION
- SD-PAIT REPAIR
- Inactivates SD-AAC-PAIT and SD-SITE-PAIT HL7 Application Parameters.

## Additional Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PAIT Technical Manual and the PAIT Release Notes provide additional information about PAIT. Term definitions can be found in the Glossary of the PAIT Technical Manual.

# Appointment Selection and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When PAIT was released (SD\*5.3\*290), the initial PAIT transmission sent all pending patient appointments created September 1 2002 or later to <span class="mark">REDACTED</span>. PAIT groups appointments into two states: Pending and Final. In normal processing, an appointment will be sent only once when it’s in a Pending state and once when it’s in a Final state. For example, an appointment sent for the first time in a Pending state will be sent again only if its status is changed to Final. An appointment with a Final status, sent for the first time, will not be sent again. However, if an appointment is rejected by <span class="mark">REDACTED</span> due to invalid or inconsistent data, it will be resent by every bimonthly task until it is accepted by <span class="mark">REDACTED</span>. If a batch is manually rejected in VistA, the entire batch will be resent in subsequent bimonthly tasks until it is accepted by <span class="mark">REDACTED</span>.

Entries in the Patient Appointment Info Log (file \#409.6) are created to track the transmitted appointments.

All updated records should be Final and their previous base records, if any, should be Pending. AITC receives both Pending and Final records. If an appointment is both created and finalized (i.e. canceled or checked in and/or checked out) between one transmission and the next, only the Final version of the data is transmitted. So, Finals may include appointments not previously transmitted and updates to previously transmitted Pending appointments.

PAIT uses standard HL7 event mapping, shown below in Table 1-1, to map Pending and Final appointment states to various combinations of event reasons and appointment types. PAIT uses Event Reason and Appointment Type as primary and secondary identifiers.

<span id="_Toc442774264" class="anchor"></span>Table 1-1: SIU Event Mapping Table

|                |                |                              |                        |
|----------------|----------------|------------------------------|------------------------|
| Event Code | Appt State | Event Reason             | Appt Type          |
| S12            | Pending        | Check-in (CI)                | Action Required (AR)   |
| S12            | Pending        |                              | No Action Taken (NAT)  |
| S12            | Pending        |                              | Future (F)             |
| S12            | Pending        |                              | Non-Count (NC)         |
| S12            | Pending        |                              | Inpatient (I)          |
| S12            | Pending        |                              | Non-Count Future (NCF) |
| S26            | Final          | No Show (NS)                 |                        |
| S26            | Final          | No Show (NS)                 | Auto Rebook (ABK)      |
| S15            | Final          | Cancelled by Clinic (CC)     | Re-schedule (RS)       |
| S 15           | Final          | Cancelled by Clinic (CC)     |                        |
| S15            | Final          | Cancelled by Clinic (CC)     | Auto Rebook (ABK)      |
| S15            | Final          | Cancelled by Patient (CP)    | Re-schedule (RS)       |
| S15            | Final          | Cancelled by Patient (CP)    |                        |
| S15            | Final          | Cancelled by Patient (CP)    | Auto Rebook (ABK)      |
| S12 or S14     | Final          | Check Out by Encounter (COE) | Non-Count (NC)         |
| S12 or S14     | Final          | No Match (NM)                | Non-Count (NC)         |
| S12 or S14     | Final          | Check-out (CO)               | Action required (AR)   |
| S12 or S14     | Final          | Check-out (CO)               | Inpatient (I)          |
| S12 or S14     | Final          | Check-out (CO)               | Out patient (O)        |
| S15            | Final          | Cancelled Terminated (CT)    |                        |

Items in Table 1-1 that are not directly identifiable through VistA appointment file attributes are explained below.

<u>Auto Rebook (ABK) –</u> PAIT assigns ABK status to an appointment with an Auto Rebooking Date if its status in VistA is ‘no show’ or ‘canceled’ by patient or clinic. This is designed to track appointment scheduling continuity. The originally entered Auto Rebooking Date may be sent with a different Event Reason and/or Appointment Type, unrelated to the Auto Rebooked Date.

<u>Re-scheduled (RS)</u> – This appointment type is assigned to each canceled appointment if another appointment for a clinic with the same DSS ID (stop code) was scheduled on the same date as the cancellation took place. That situation often occurs when the auto-rebooking feature is not used. PAIT assumes that the newly scheduled appointment is a reinstatement of the canceled one.

<u>Cancelled Terminated (CT)</u> – This is the Event Reason identifier used to finalize an appointment that was sent as Pending and then, with the next PAIT, it has been determined that a new appointment is created for the same date and time. In VistA, the previous appointment record is overwritten in VistA by the new appointment record with a new creation date.

If an appointment is canceled and another one is scheduled for the same Appointment Date/Time, the previous appointment’s Event Reason will be changed to Canceled Terminated. This will be done regardless of whether the appointment was already canceled and transmitted in a previous run or if it was canceled and transmitted in the current run with the new appointment that has the same Appointment Date/Time. This situation is automatically recognized when appointments have the same Appointment Date/Time, but different Creation Dates. The original Creation Date is retrieved from the Patient Appointment Info Log file (# 409.6). In VistA, the original creation date is overwritten by the Creation Date of the newly created appointment, scheduled for the same Appointment Date/Time.

<u>Future (F</u>) – This Appointment Type applies to all future appointments except those created for

Non-Count Hospital Locations that have Type: Non-Count Future (NCF).

<u>Non-Count Future (NCF</u>) – Scheduled for the future in a non-count clinic. In VistA, there are many non-count clinics that have scheduled appointments for valid patient care. Sites using Event Capture and/or Surgery configure non-count clinics for scheduled appointments. The encounters for these appointments are passed through a separate count clinic with a status of Checked Out.

<u>Non-Count (NC)</u> - For canceled appointments where the clinic is 'Non-Count' and the appointment was not rescheduled, the appointment type in the PAIT transmission will 'NC'.

<u>Check Out By Encounter (COE)</u> – If there is an Outpatient Encounter (file \#409.68) entry where the Originating Process Type (field \#.08) is 2 (Stop Code Addition) for the same date as the appointment, and the Stop Code Number (field \#8) and the Credit Stop Code (field \#2503) in the Hospital Location (file \#44) of the non-count and count clinics match, COE is assigned as the event reason of the appointment and the count clinic data is returned with the final transmission for this appointment.

<u>No Match (NM)</u> – This Event Reason is assigned if no outpatient encounter related to the appointment has been found. It will be sent with its Final status if there is an existing entry in the Patient Appointment Info Log (file \#409.6) indicating it was previously sent as Pending. If PAIT is evaluating the appointment for the first time, it will never be transmitted. An appointment with no matching Outpatient Encounter entry is a data inconsistency.

<u>Non-Count (NC)</u> – This Appointment Type, without any value for the Event Reason, is sent if an appointment’s scheduled date has passed by no more than two days but no action has been taken to update it in VistA. This time is allotted for possible delays in updating a potentially matching encounter.

## Patient Status Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient status code indicates whether a patient is new to a stop code within a facility or not. The parent station, substation, and stop codes of the clinic in the Hospital Location file (#44) are evaluated. The patient is new to the facility if he or she did not have another scheduled appointment within the facility and stop code during the last 24 months. The facility is determined from the Institution (file \#4) if there is a pointer to it from the Hospital Location (file \#44) through the pointer to the Medical Center Division from the Division (field \#3.5) of the Hospital Location file. Table 1-2 shows each Patient Status Code value and description.

<span id="_Toc442774265" class="anchor"></span>Table 1-2: Patient Status Codes

|           |                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------|
| Value | Description                                                                                                   |
| NSF       | Patient did not have a prior appointment at this facility in the past 24 months; new to parent and substation.    |
| SHB       | Patient did have a prior appointment at this parent and substation in the past 24 months; registered here before. |
| OPN       | Patient did not have a prior appointment at this substation but was registered with parent station.               |

## Combat Veteran Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software to support the Combat Veteran (CV) initiative was developed and introduced in a phased implementation strategy. The CV information included in PAIT is evaluated and transmitted based on the already released related patches and involves several criteria to determine CV Eligibility and subsequent classifications in the system.

Combat veteran data above is taken from the following VistA Patient file fields:

Combat Veteran End Date (field \#.5295)

Service Separation Date \[Last\] (field \#.327)

Combat Service Indicated (field \#.5291)

Combat Service Location (field \#.5292)

Persian Gulf Service (field \#.32201)

### Combat Veteran Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CV Eligibility is used to identify a CV veteran seeking medical care for a specific date and will be determined as of the Appointment Creation Date. The following values for CV Eligibility are:

- 1 (Yes) is sent if the patient was considered a CV on the Appointment Creation Date
- 0 (No) is sent if the patient was not considered a CV on the Appointment Creation Date
- U is sent if it was not possible to determine whether the patient was considered CV.

CV Eligibility is included in PAIT HL7 messages (also see ZEL segment documentation in the PAIT Technical Manual).

### Combat Veteran End Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CV End Date represents the last day for CV eligibility. The existence of a CV End Date indicates that a veteran was or is CV eligible. Even if the CV eligibility has expired, this date will still be present. CV End Date is included in PAIT HL7 messages (also see ZEL segment documentation in the PAIT Technical Manual).

### Combat Veteran Indication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CV Indication signifies whether an appointment is related to a CV illness/injury. Data entry indicating whether an appointment is related to the veteran’s CV status is done during checkout or update of an appointment’s classifications. Possible values for CV Indication are:

- 1 (Yes) is sent if the appointment was related to the veteran’s CV status
- 0 (No) is sent if the appointment was not related to the veteran’s CV status

CV Indication is included in PAIT HL7 messages (also see ZCL segment, seventh repetition, where this VA-specific classification is documented in the PAIT Technical Manual).

### Combat Veteran History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CV History data is retrieved and transmitted to calculate the wait time experienced by service members recently returning from the war in Iraq. CV History is included in PAIT HL7 messages. (See the PAIT Technical Manual, Table 5-2 regarding three repetitions of HL7 segment ZMH to encompass indication of CV history, last service location, indication of combat service in that location, and separation date.)

CV Indicated – signifies whether the patient was ever considered a Combat Veteran. Valid values are:

- Y – YES
- N – NO

Combat Service Location – Combat location code.

Indication of service in combat location - Valid values are:

- Y – YES
- N – NO

Last Service Separation Date

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Appointment Info Log (file \#409.6) in VistA contains PAIT activity information. On regular bimonthly transmissions, PAIT finds new appointments based on the Date Appt. Made (field \#20) (creation date) of the Appointment multiple (# 2.98) of the Patient file (# 2). If this date is later than the last transmission, the appointment is added to the new transmission. After finding all new appointments, PAIT examines the Patient Appointment Info Log for appointments that have changed from a Pending to a Final state, and adds them to the new transmission by creating new entries in the Patient Appointment Info Log with Retention Flag (field \# 4) of the Patient Multiple (# 409.629) set to “Y,” Final state. The Retention Flag in the original entry is changed from “Y” to “S” – Sent as Final with another entry, or to “R” – Resent because of rejection if the original entry was rejected.

# Rejected Appointment Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites are responsible for correcting rejected appointments. Entries in the Patient Appointment Info Log that were flagged as rejected by AITC acknowledgements should be identified by running the Rejected Transmissions \[SD-PAIT REJECTED\] report.

1.  AITC acknowledgements send rejection codes which should be addressed before the next transmission. If the rejection code is “R”, no action is required because the whole batch was rejected and all related appointments will be sent again in the next transmission.
2.  Rejected appointments will always be retransmitted in the next scheduled PAIT task regardless of whether the error has been corrected or not. When retransmitted, a new entry for each appointment will be created in the Patient Appointment Info Log (file \#409.6) with the appointment data and status. The original rejected entry’s Retention Flag (field \#4) will be updated to “R” – Resent because of rejection.

# PAIT Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of all PAIT options in Vista:

> 1 SD-PAIT ACK SUMMARY Acknowledgement Summary

> 2 SD-PAIT MANUAL BATCH REJECT Manual Batch Reject

> 3 SD-PAIT MANUAL TRANSMISSION Manual Startup PAIT Transmission

> 4 SD-PAIT PATIENT HL7 LOCATION Patient HL7 Location

> 5 SD-PAIT PENDING Pending Transmissions

> 6 SD-PAIT REJECTED Rejected Transmissions

> 7 SD-PAIT REPAIR SD-PAIT Last Run Repair

> 8 SD-PAIT REPORTS PAIT Reports Menu

> 9 SD-PAIT TASKED TRANSMISSION Taskman PAIT Transmission

10. SD-PAIT TRANSMISSION SUMMARY Transmission Summary

## *Taskman PAIT Transmission \[SD-PAIT TASKED TRANSMISSION\]*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">This option has been placed out of order with SD\*5.3\*639.</span>

Below is an example of the non-interactive tasked background option to schedule PAIT transmissions:

> Edit Option Schedule

> Option Name: SD-PAIT TASKED TRANSMISSION

> Menu Text: Taskman PAIT Transmission TASK ID:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> QUEUED TO RUN AT WHAT TIME: MAR 15,2007@19:00

> DEVICE FOR QUEUED JOB OUTPUT:

> QUEUED TO RUN ON VOLUME SET:

> RESCHEDULING FREQUENCY: 1M (1, 15)

> TASK PARAMETERS:

> SPECIAL QUEUEING: Persistent

## Manual Startup PAIT Transmission \[SD-PAIT MANUAL TRANSMISSION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">This option has been placed out of order with SD\*5.3\*639.</span>

This option may be used to start/queue PAIT manually.

> CHOOSE 1-2: 2 SD-PAIT MANUAL TRANSMISSION Manual Startup PAIT Transmission

> Manual Startup PAIT Transmission

> Queue to run:

This option should be used only to start an additional PAIT for the current scheduled run if the scheduled task fails to start, encounters an error before completing, or if other error conditions make it necessary to run PAIT manually.

This option can be used up to four days starting from the 1<sup>st</sup> or the 15<sup>th</sup> of each month. If attempted outside of this window, it will not start the PAIT job and the next transmission will automatically take place on the next scheduled PAIT date. The four-day restriction window is due to AITC’s processing requirements.

## PAIT Reports \[SD-PAIT REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All PAIT reports can be accessed through the PAIT Reports menu in Vista:

> Select PAIT Reports Menu Option: ?

> Acknowledgement Summary

> Patient HL7 Location

> Pending Transmissions

> Rejected Transmissions

> Transmission Summary

### Acknowledgement Summary \[SD-PAIT ACK SUMMARY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Acknowledgement Summary may be used to verify the batch numbers generated from a particular site. This report lists all batches in Batch Control ID order and indicates the Message Control ID, the Acknowledgement Date, and Acknowledgement Type. Table 4-1 shows the acknowledgement types and abbreviations used for this report.

<span id="_Toc442774266" class="anchor"></span>Table 4-1: Acknowledgement Types

| Acknowledgement Type | Code                |
|--------------------------|-------------------------|
| Application Accept       | AA See Technical Manual |
| Application Error        | AE See Technical Manual |
| Application Reject       | AR Not used             |
| Manual Rejection         | MR See Technical Manual |

PAIT ACK SUMMARY FEB 27, 2004 11:26 PAGE 1

> APPLICATION ACK APPLICATION ACK

BATCH CONTROL ID MESSAGE CONTROL ID DATE/TIME TYPE

----------------------------------------------------------------------------------------------

> TRANSMISSION FINISHED: FEB 20, 2004 20:45

75611134952 75615626811 FEB 24, 2004 08:38 APPLICATION ACCEPT

75611135142 75615627064 FEB 24, 2004 08:39 APPLICATION ACCEPT

75611135273 75615627292 FEB 24, 2004 08:40 APPLICATION ACCEPT

75611135591 75615627625 FEB 24, 2004 08:41 APPLICATION ACCEPT

75611135943 75615628077 FEB 24, 2004 08:42 APPLICATION ACCEPT

75611136242 75615628454 FEB 24, 2004 08:43 APPLICATION ACCEPT

75611136597 75615628914 FEB 24, 2004 08:44 APPLICATION ACCEPT

75611136841 75615629306 FEB 24, 2004 08:45 APPLICATION ACCEPT

75611137250 75615629892 FEB 24, 2004 08:46 APPLICATION ACCEPT

75611137757 75615630556 FEB 24, 2004 12:49 APPLICATION ERROR

75611138197 75615631071 FEB 24, 2004 12:50 APPLICATION ACCEPT

75611138675 75615631643 FEB 24, 2004 12:50 APPLICATION ACCEPT

75611138981 75615632257 FEB 24, 2004 12:51 APPLICATION ACCEPT

75611139225 75615632561 FEB 24, 2004 12:52 APPLICATION ACCEPT

75611139441 75615632855 FEB 24, 2004 12:53 APPLICATION ACCEPT

75611139687 75615633142 FEB 24, 2004 12:54 APPLICATION ACCEPT

75611139729 75615633201 FEB 24, 2004 12:54 APPLICATION ACCEPT

75611139775 75615633241 FEB 24, 2004 12:55 APPLICATION ERROR

75611139829 75615633301 FEB 24, 2004 12:56 APPLICATION ACCEPT

75611139855 75615633327 FEB 24, 2004 12:56 APPLICATION ACCEPT

75611140007 75615633495 FEB 24, 2004 12:57 APPLICATION ACCEPT

75611140038 75615633536 FEB 24, 2004 12:58 APPLICATION ACCEPT

75611140066 75615633568 FEB 24, 2004 12:59 APPLICATION ACCEPT

75611140072 75615633574 FEB 24, 2004 13:00 APPLICATION ACCEPT

*Note: APPLICATION ACCEPT (AA) will be listed only if the entire batch is accepted. If the batch is accepted with rejections, the acknowledgment type will be APPLICATION ERROR (AE).*

### Patient HL7 Location \[SD-PAIT PATIENT HL7 LOCATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be used to identify patient(s) records in the Patient Appointment Info Log file (# 409.6) with scheduled appointment date/times within a selected date range. It includes the HL7 message ID that can be used for troubleshooting.

> Patient HL7 Location

> \* Previous selection: APPT DATE from Jan 3, 2006 to Jan 3,2006@24:00

> START WITH APPT DATE: Jan 3, 2006// (JAN 03, 2006)

> GO TO APPT DATE: Jan 3, 2006// (JAN 03, 2006)

> DEVICE: UCX/TELNET Right Margin: 80//

> SD-PAIT PATIENT HL7 LOCATION JAN 27,2009 16:28 PAGE 1

> HL7

> PATIENT APPT DATE MESSAGE

> -------------------------------------------------------------------------------

> AJJDJFD,CNDFH JAN 3, 2006 13:00 500127809-13

*Note: “500127809” is the HL 7 message ID and “13” is the Sequence Number.*

### Pending Transmissions \[SD-PAIT PENDING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pending Transmission report can be used to identify past appointments that need to be checked out or canceled to finalize them for transmission. This report lists all Pending records by Date Appointment Made. If the listed appointments are not retransmitted, they will stay in the Patient Appointment Info Log file (# 409.6).

> Pending Transmissions

> START WITH APPT DATE: Jan 1, 2008// JAN 1 2007 (JAN 01, 2007)

> GO TO APPT DATE: LAST// JAN 1 2007 (JAN 01, 2007)

> DEVICE:

> PATIENT PENDING APPOINTMENT LOG JAN 27, 2009 17:21 PAGE 1

> PATIENT APPT DATE EVENT REASON APPOINTMENT CLINIC

> TYPE

> -------------------------------------------------------------------------------

> RETENTION FLAG: YES - to be sent when 'Final'

> DATE APPT MADE: FEB 1, 2007

> TWEWTWTE, SOLOMON NORRIS JR FEB 1, 2007 09:56 Check-in Action Required EVANS PC

### Rejected Transmissions \[SD-PAIT REJECTED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints all currently rejected appointments with error codes. If 'R' is printed instead of an error code, it means that the whole batch was manually rejected and no action is necessary because it will be transmitted with the next regularly scheduled PAIT task.

This report can be used to identify patient appointment records that need corrections. Once the VistA data is corrected, it will be retransmitted in the next bi-monthly task and loaded into the national database in Austin. Correcting rejected records is the site’s responsibility.

REJECTED TRANSMISSION LOG FEB 27, 2004 11:34 PAGE 1

ERROR

PATIENT APPT DATE SHORT DESCRIPTION MESSAGE

CLINIC

-------------------------------------------------------------------------------------------------

ERROR MESSAGE: 350

PUBLIC, JOHN Q OCT 6, 2003 15:56 HL7 date is not in proper format or is missing 350

FLU SHOT CLINIC

### Transmission Summary \[SD-PAIT TRANSMISSION SUMMARY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a detailed report for each transmission, with batch control IDs, message control IDs, and dates/times the batches were created. This option may be used for verification of batches received by AITC.

Transmission Summary

\* Previous selection: RUN DATE from Jan 1,2010 to Jan 27,2010@24:00

START WITH RUN DATE: Jan 1,2010// 021510 (FEB 15, 2010)

GO TO RUN DATE: LAST//

DEVICE: HOME Right Margin: 80//

PATIENT APPOINTMENT INFO LOG LIST FEB 16,2010 16:03 PAGE 1

LAST

SCANNED \# OF

RUN DATE DATE APPOINTMENTS

\# OF BATCH CREATE

BATCHES BATCH CONTROL ID DATE/TIME

MESSAGE CONTROL ID

--------------------------------------------------------------------------------

FEB 15,2010 FEB 14,2010 112253

23 636362443104 FEB 15,2010 17:06

636427129081

636362445061 FEB 15,2010 17:17

636427131066

636362446271 FEB 15,2010 17:26

636427132456

636362446987 FEB 15,2010 17:37

636427133210

636362447576 FEB 15,2010 17:46

636427133924

### Manual Batch Reject \[SD-PAIT MANUAL BATCH REJECT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">This option has been placed out of order with SD\*5.3\*639.</span>

This option allows users to 'reject' a previously created batch that must be retransmitted. The transmission date has to be entered to proceed with this option. Only batch control ID numbers that have not been acknowledged can be rejected. More that one batch number can be entered. After rejection, the records in the batch will be sent in the next transmission.

> Manual Batch Reject

> Select running date: JAN 23 JAN 23, 2009

> Correct Running Date?? Yes// (Yes)

> BATCH CONTROL ID: 44233574744

> BATCH CONTROL ID: 44233574742

> BATCH CONTROL ID: 44233574740 An acknowledged batch cannot be rejected

> Batch already Acknowledged!

> BATCH CONTROL ID:

> This job has been tasked

### SD-PAIT Last Run Repair \[SD-PAIT REPAIR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">This option has been placed out of order with SD\*5.3\*639.</span>

When an application error or system problem interrupts the PAIT task, the first step is to determine the cause of the error or problem and correct it. After correcting the problem, this option must be used to repair the interrupted transmission. Finally, the PAIT task must be started again.

> SD-PAIT Last Run Repair

> The repairing in progress...

> The last run number has been repaired, you may ONE TIME QUEUE the next one.

> Select OPTION NAME: SD-PAIT REPAIR SD-PAIT Last Run Repair

> NO ENTRY TO REPAIR! --- This message displays if the last run has

> already been repaired or there is nothing to be repaired

# Rejection Codes and Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Code Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses PAIT error codes that appear on the Rejected Transmissions report and explains in detail how to find and correct data that is causing the rejections. Table 5-1 provides a basic description of each numeric error code.

<span id="_Toc442774267" class="anchor"></span>Table 5-1: Error Code Set

|           |                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value | Description                                                                                                                                                                                                                    |
| 100       | Patient DFN is not numeric or is missing                                                                                                                                                                                           |
| 150       | Clinic IEN is not numeric or is missing                                                                                                                                                                                            |
| 200       | BHS station number and STA3N are not equal                                                                                                                                                                                         |
| 250       | Invalid or missing BHS station number                                                                                                                                                                                              |
| 300       | Invalid or missing STA3N                                                                                                                                                                                                           |
| 350       | HL7 date is not in proper format or is missing                                                                                                                                                                                     |
| 400       | DOB is missing or invalid                                                                                                                                                                                                          |
| 450       | Create date or appt date is missing                                                                                                                                                                                                |
| 500       | Creation date is before September 1, 2002                                                                                                                                                                                          |
| 600       | Rescheduled date and appt type are not in agreement - Rescheduled date requires SCH.8 Appt type = ‘RS’ and vice versa                                                                                                              |
| 650       | Check out date and event reason are not in agreement - Check out date requires either SCH.6 Event reason = ‘CO’ or ‘COE’                                                                                                           |
| 700       | Cancellation date and event reason are not in agreement - Cancellation date requires SCH.6 Event reason = ‘CC’ or ‘CP’ or ‘NS’                                                                                                     |
| 750       | Event reason and filler status are not in agreement - All SCH.6 Event reason codes, except ‘CI’ require SCH.25 Filler status to be ‘F’ Final and accordingly only ‘CI’ and Null should have SCH.25 Filler status to be ‘P’ Pending |
| 800       | Filler status is missing or is invalid                                                                                                                                                                                             |
| 850       | Admit type is invalid (Table 5-2)                                                                                                                                                                                                  |
| R         | Whole batch rejected                                                                                                                                                                                                               |

| *Note: R – whole batch rejected can be generated only by manual batch rejection by the site.* |
|---------------------------------------------------------------------------------------------------|

Error 100 – Patient DFN is not numeric or is missing:

DFN, or Internal Entry Number of a Patient in the Patient File, is missing or not numeric. This is most likely the result of a HL7 transmission formatting error. Requires no intervention or correction at site level the first time the error occurs. The record will be re-transmitted. If the error persists create a Remedy ticket and/or call the VA Service Desk (VASD).

Error 150 – Clinic IEN is not numeric or is missing:

Clinic IEN, or Internal Entry Number of the Clinic in the Hospital Location (file \#44) is missing or not numeric. This is most likely the result of an HL7 transmission formatting error and requires no intervention or correction by the site the first time the error occurs. The record will be re-transmitted, but if the error persists, initiate a Remedy ticket and/or call the VA Service Desk (VASD).

Error 200 – BHS station number and STA3N are not equal:

Error 200 indicates that the Hospital Location of a particular appointment is set up with an Institution whose Station Number field does not match the sending facility number. PAIT uses the Institution of the Medical Center Division file (# 40.8) entry pointed to by the Division field (# 3.5) of the Hospital Location file (#44). The site should first examine the appointment’s Hospital Location file entry to verify that its Division points to the correct Medical Center Division. Then verify that the Medical Center Division’s Institution File Pointer (field \#.07) is correct and that the 3-digit station number of the Institution (file \#4) entry that it points to matches the main facility station number. PAIT retrieves the Institution and its Station Number, following the Hospital Location’s Division field pointing to the Medical Center Division file, and its Institution File Pointer field (# .07). IRM should direct this issue to whoever is responsible for configuration of the Hospital Location file clinic entry. If the issue cannot be resolved locally, a Remedy ticket has to be initiated and/or the VASD notified.

Error 250 – Invalid or missing BHS station number:

HL7 site parameters are incorrect. Initiate Remedy ticket and/or call the VASD.

Error 300 – Invalid or missing STA3N:

This error is similar to Error 250. It indicates that the Station Number field (# 99) identified from the Institution is null or its first three characters do not match the facility’s three-digit number. This can occur if a clinic is configured with a Division that does not match the site’s main 3-digit station number. Allow the record to be re-transmitted. If the error persists, initiate a Remedy ticket and/or call the VASD.

Error 350 – HL7 date is not in proper format or is missing:

 

Error 350 is usually caused by a bogus desired date or appointment date in the Appointment Multiple (# 2.98) of the Patient File. A bogus date may appear on the detailed screens under Appointment Management and/or PCE. Error 350 may have to be evaluated by a person having programming access and authority to repair data. IRM should work with the Scheduling staff to repair existing appointment records in Vista. If no evidence of a bogus date can be found or if there is a question about how to address a bogus date, initiate a Remedy ticket and/or call the VASD. IRM staff can refer to the PAIT Technical Manual for more details on finding and repairing bogus dates.

Error 400 – DOB is missing or invalid:

Site staff should examine the patient’s demographics for an invalid or missing Date of Birth (DOB) and correct the problem.

Error 450 – Create date or appt date is missing:

Each transmitted appointment must have the appointment’s Creation Date. The site should find the entry with the appointment in the Patient Appointment Info Log (file \#409.6) and check the Date Appt Made (field \#8) under the Patient multiple (sub-field \#2). If there is a date in that field, allow the record to be re-transmitted. If not, make sure the Date Appt Made (field \#20) is populated correctly in the Appointment multiple (#2.98) of the Patient File (#2). If the error persists, initiate a Remedy ticket and/or call the VASD.

Error 500 – Creation date is before September 1, 2002:

PAIT evaluates appointments based on the Creation Date before September 1, 2002. Site should check the appointment’s entry in the Patient Appointment Info Log (file \#409.6) for the date in the Date Appt Made (field \#8) under the Patient multiple sub-field (# 2). If its value is a date before September 1, 2002, initiate a Remedy ticket and/or call the VASD, otherwise allow the record to be retransmitted.

Error 600 – Rescheduled date and appt type are not in agreement:

Refer to description of Appointment Type RS (Rescheduled) in the Appointment Selection and Transmission section of this manual. If there is a rescheduled date, the Appointment Type must be ‘RS.’ Site intervention is not recommended. Instead, a Remedy ticket should be initiated and/or the VASD should be called. The appointment data will have to be reviewed and updated.

Error 650 – Check out date and event reason are not in agreement:

The Event Reason: ‘CO’ or ‘COE’ require the Check-Out Date to be included with a transmitted appointment. No site intervention is required. Instead, a Remedy ticket should be initiated and/or the VASD should be called.

  
Error 700 – Cancellation date and event reason are not in agreement:

If there is a Cancellation Date the Event Reason must be either ‘CC,’ ‘CP,’ ‘NS,’ or ‘CT’. Refer to Table 1-1 for additional clarification on appointment attributes required for a given appointment state. Appointment Type ‘CT’ may be also sent without the Cancellation Date if a new appointment that overrode the original one is still ‘Pending.’ Initiate a Remedy ticket and/or call the VASD if no solution is evident.

Error 750 – Event reason and filler status are not in agreement:

Review Table 1-1 to see the allowable combinations of event reason and appointment type. Initiate a Remedy ticket and/or call the VASD if no solution is evident.

Error 800 – Filler status is missing or is invalid:

Each appointment record must have the Filler Status (state) that corresponds to either ‘Pending’ or ‘Final’ value. Initiate a Remedy ticket and/or call the VASD.

Error 850 – Admit type is invalid:

Only values for Purpose of Visit listed in table 5-2 will be accepted by AITC. The numeric code in the Value column denotes a combination of Purpose of Visit & Appointment Type.

<span id="_Toc442774268" class="anchor"></span>Table 5-2: Purpose of Visit and Appointment Type

|           |                      |                        |
|-----------|----------------------|------------------------|
| Value | Purpose of Visit | Appointment Type   |
| 0101      | C&P                  | Compensation & Pension |
| 0102      | C&P                  | Class II Dental        |
| 0103      | C&P                  | Organ Donors           |
| 0104      | C&P                  | Employee               |
| 0105      | C&P                  | Prima Facia            |
| 0106      | C&P                  | Research               |
| 0107      | C&P                  | Collateral of Vet      |
| 0108      | C&P                  | Sharing Agreement      |
| 0109      | C&P                  | Regular                |
| 0111      | C&P                  | Service Connected      |
| 0201      | 10-10                | Compensation & Pension |
| 0202      | 10-10                | Class II Dental        |
| 0203      | 10-10                | Organ Donors           |
| 0204      | 10-10                | Employee               |
| 0205      | 10-10                | Prima Facia            |
| 0206      | 10-10                | Research               |
| 0207      | 10-10                | Collateral of Vet.     |
| 0208      | 10-10                | Sharing Agreement      |
| 0209      | 10-10                | Regular                |
| 0211      | 10-10                | Service Connected      |
| 0301      | Scheduled Visit      | Compensation & Pension |
| 0302      | Scheduled Visit      | Class II Dental        |
| 0303      | Scheduled Visit      | Organ Donors           |
| 0304      | Scheduled Visit      | Employee               |
| 0305      | Scheduled Visit      | Prima Facia            |
| 0306      | Scheduled Visit      | Research               |
| 0307      | Scheduled Visit      | Collateral of Vet.     |
| 0308      | Scheduled Visit      | Sharing Agreement      |
| 0309      | Scheduled Visit      | Regular                |
| 0311      | Scheduled Visit      | Service Connected      |
| 0401      | Unsched. Visit       | Compensation & Pension |
| 0402      | Unsched. Visit       | Class II Dental        |
| 0403      | Unsched. Visit       | Organ Donors           |
| 0404      | Unsched. Visit       | Employee               |
| 0405      | Unsched. Visit       | Prima Facia            |
| 0406      | Unsched. Visit       | Research               |
| 0407      | Unsched. Visit       | Collateral of Vet.     |
| 0408      | Unsched. Visit       | Sharing Agreement      |
| 0409      | Unsched. Visit       | Regular                |
| 0411      | Unsched. Visit       | Service Connected      |

*Note: It has been determined that the ‘empty’ value for sequence P1.4 of the PV1 segment has to be treated as acceptable. That might happen when a new appointment is scheduled in place of a previously canceled appointment and the original appointment had been previously transmitted by PAIT.*

If the SD-PAIT REJECTED report includes any entry with rejection code 850, the Rejected Transmission report must be investigated to determine the Purpose of Visit and Appointment Type values of the appointment listed. Sites must not create their own local appointment types because any appointment created with a local type will be rejected.

Error “R” – Whole batch rejected:

Manual rejection may be done if needed, particularly if an expected application acknowledgement from AITC was not received. All appointments from the rejected batches will be retransmitted with the next PAIT and packed into new HL7 batches.

# Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages are generated and sent to the SD-PAIT Mail Group.

## Job Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message to the Forum Server and a local SD-PAIT Mail Group will be generated at the beginning of each site’s PAIT transmission to confirm that the bi-monthly data collection process has begun. This start message also details the status of the SD-PAIT logical link and possible reason for any communication errors. This message will be sent to the SD-PAIT mail group in the form of a MailMan message. The following is an example of this new Job Started message:

> Subj: 500 - PAIT START JOB \[#1955884\] 09/21/04@12:11 3 lines

> From: POSTMASTER In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> The PAIT job has started - TASK \#: 2717310

> Site Started SD-PAIT status Task \#

> 500 \|3040921.121119 \|Enabled \|2717310

*Note: If PAIT proceeds but the start message has not been received, determine whether the PAIT task was scheduled by an active user. If not, an active IRM staff member should reschedule it.*

## PAIT Batch Acknowledgement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message on the Forum Server indicating acknowledgement of the PAIT Batch will be sent to the SD-PAIT mail group in the form of a MailMan message. The following is an example of this PAIT Batch Acknowledgement message:

> Subj: PAIT BATCH ACKNOWLEGEMENT 50015153 \[#1955973\] 09/22/04@12:14 7 lines

> From: POSTMASTER In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> Station Number: 500

> Batch Control ID: 50015153

> Message ID: 50092733

> Log Entry: 2

> Run Date: Sep 21, 2004@12:11:30

> Status: Acknowledged - No Rejections

> 1 of 1 ACKs received for this run date

## PAIT Completion Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan completion message addressed to the SD-PAIT mail group will confirm completion of the tasked job. See the PAIT Technical Manual for additional information.

## Prevention of PAIT Manual Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">This option has been placed out of order with SD\*5.3\*639.</span>

When a facility attempts to run the Manual Startup PAIT Transmission \[SD-PAIT MANUAL TRANSMISSION\] option, the software determines if the tasked transmission job is already scheduled within the current transmission period, or if it is outside of the 4-day window for transmissions. Either of these conditions will prevent running the manual transmission. If the manual transmission is prevented, an informational message stating the reason is displayed on the screen immediately. A MailMan message is also sent, explaining why queuing of the manual option, SD-PAIT Manual Transmission, is not allowed.

The following is an example showing the message displayed on the screen:

> Select OPTION NAME: SD-PAIT Manual Transmission Manual Startup PAIT Transmission

> Manual Startup PAIT Transmission

> You attempted to start PAIT outside the authorized transmission dates.

> Job has been terminated.

Below is an example of the MailMan message sent to members of the SD-PAIT Mail Group when a manual transmission attempt is prevented.

> Subj: PAIT Transmission \[#1955781\] 09/17/04@13:50 3 lines

> From: POSTMASTER In 'IN' basket. Page 1 \*New\*

> -------------------------------------------------------------------------------

> USERLASTNAME, USER (DUZ=100106) attempted to start the PAIT transmission

> on Sep 17, 2004@13:50:39, outside the authorized transmission dates.

> The job has been cancelled