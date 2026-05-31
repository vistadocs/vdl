---
title: SD*5.3*333 PAIT Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PAIT
app_name: Patient Appointment Info. Transmission
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*333
group_key: PAIT:SD:5.3
file_numbers:
- '1.2'
- '1.5'
- '2'
- '3'
- '7'
- '44'
- '99'
- '123'
- '409.6'
- '409.8'
- '1900'
security_keys: []
menu_options: 0
description: '| | | | | |-----------|--------------|--------------------------------|------------------------------------| | Date | Revision | Description | Author | | 1.28.2004 | 1.0 | Version 1 | REDACTED | | 1.28.2004 | 1.1 | Revisions | REDACTED | | 1.29.2004 | 1.2 | Revisions | REDACTED | | 2.2.2004 | 1.3 |...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 14498
section_count: 63
table_count: 61
figure_count: 0
appendix_count: 3
has_toc: false
is_stub: false
pub_date: March 2004
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Patient_Appointment_Info_Transmission/sd_53_p333_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Patient_Appointment_Info_Transmission/sd_53_p333_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=169
audit_applied: '2026-05-31'
master_source: SD*5.3*333 PAIT Release Notes
master_pub_date: March 2004
consolidated_from: 3 versions
prior_versions:
- SD*5.3*349 PAIT Release Notes
- SD*5.3*376 PAIT Release Notes
consolidated_title: pait release notes
---

![](sd-5-3-333-pait-release-notes/001.png)

Patient Appointment Information Transmission (PAIT)

Release Notes and Installation Guide

Patch SD\*5.3\*333

March 2004

VistA Health Systems Design and Development

This page left blank intentionally

Revision History

|           |              |                                |                                    |
|-----------|--------------|--------------------------------|------------------------------------|
| Date  | Revision | Description                | Author                         |
| 1.28.2004 | 1.0          | Version 1                      | <span class="mark">REDACTED</span> |
| 1.28.2004 | 1.1          | Revisions                      | <span class="mark">REDACTED</span> |
| 1.29.2004 | 1.2          | Revisions                      | <span class="mark">REDACTED</span> |
| 2.2.2004  | 1.3          | Revisions                      | <span class="mark">REDACTED</span> |
| 2.3.2004  | 1.4          | Revisions                      | <span class="mark">REDACTED</span> |
| 3.1.2004  | 1.5          | Revisions                      | <span class="mark">REDACTED</span> |
| 3.2.2004  | 1.6          | EVS trouble shooting           | <span class="mark">REDACTED</span> |
| 3.3.2004  | 1.7          | Revisions                      | <span class="mark">REDACTED</span> |
| 3.4.2004  | 1.8          | Revisions                      | <span class="mark">REDACTED</span> |
| 7.10.2006 | 1.9          | Corrections                    | <span class="mark">REDACTED</span> |
| 7.12.2006 | 1.91         | Document Review                | <span class="mark">REDACTED</span> |
| 12.4.2008 | 1.92         | Changes for patch SD\*5.3\*528 | <span class="mark">REDACTED</span> |
| 1.5.2009  | 1.93         | Changes for patch SD\*5.3\*534 | <span class="mark">REDACTED</span> |
|           |              |                                |                                    |
|           |              |                                |                                    |
|           |              |                                |                                    |
|           |              |                                |                                    |

This page left blank intentionally

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Description of Functionality](#description-of-functionality)
- [Changes introduced with SD\5.3\333 patch](#changes-introduced-with-sd53333-patch)
  - [## ## ## Table VA087 - Scheduling Event Reason](#table-va087-scheduling-event-reason)
  - [Table 0276 - Appointment Reason Codes](#table-0276-appointment-reason-codes)
  - [## SCH Schedule Activity Information](#sch-schedule-activity-information)
  - [Table VA0021 – Enrollment Priority](#table-va0021-enrollment-priority)
  - [Table 0277 - Appointment Type Codes](#table-0277-appointment-type-codes)
  - [6\. The logic of generating appointments from the update runs has been modified to start from scanning newly created records and then to update the previous pending appointments, if applicable. Also the last scanned date is the last date before the start of transmission, to avoid possible duplications.](#6-the-logic-of-generating-appointments-from-the-update-runs-has-been-modified-to-start-from-scanning-newly-created-records-and-then-to-update-the-previous-pending-appointments-if-applicable-also-the-last-scanned-date-is-the-last-date-before-the-start-of-transmission-to-avoid-possible-duplications)
  - [Table AAC001 - Error Code Set](#table-aac001-error-code-set)
- [Installation](#installation)
- [Post Installation Instructions](#post-installation-instructions)
- [User Options](#user-options)
- [MailMan Messages](#mailman-messages)
- [Technical Information](#technical-information)
  - [Initial Seeding Run Times:](#initial-seeding-run-times)
- [Appendix A – HL7 Specifications](#appendix-a-hl7-specifications)
  - [Introduction](#introduction-1)
  - [General](#general)
  - [Message Content](#message-content)
  - [Data Capture and Transmission](#data-capture-and-transmission)
  - [Batch Messages](#batch-messages)
  - [Batch Acknowledgements](#batch-acknowledgements)
  - [Lower Level Protocol](#lower-level-protocol)
  - [HL7 Control Segments](#hl7-control-segments)
  - [Message Definitions](#message-definitions)
  - [## Segment Table Definitions](#segment-table-definitions)
  - [## Message Control Segments](#message-control-segments)
  - [MSH - Message Header Segment](#msh-message-header-segment)
  - [BHS – Batch Header Segment](#bhs-batch-header-segment)
  - [BTS - Batch Trailer Segment](#bts-batch-trailer-segment)
  - [PID - Patient Identification Segment](#pid-patient-identification-segment)
  - [PID - Patient Identification Segment (continued)](#pid-patient-identification-segment-continued)
  - [PV1 - Patient Visit Segment](#pv1-patient-visit-segment)
  - [2.3.7AIP - Appointment Information - Personnel Resource Segment](#237aip-appointment-information-personnel-resource-segment)
  - [## AIL Appointment Information](#ail-appointment-information)
  - [SCH Schedule Activity Information](#sch-schedule-activity-information-1)
  - [ZCL - VA-Specific Outpatient Classification Segment](#zcl-va-specific-outpatient-classification-segment)
  - [ZEN - VA-Specific Enrollment Segment](#zen-va-specific-enrollment-segment)
  - [ZSP - VA-Specific Service Period Segment](#zsp-va-specific-service-period-segment)
  - [SUPPORTED AND USER-DEFINED HL7 TABLES](#supported-and-user-defined-hl7-tables)
  - [Table 0003 - Event type](#table-0003-event-type)
  - [Table 0004 – Patient Class](#table-0004-patient-class)
  - [Table 0008 - Acknowledgment Code](#table-0008-acknowledgment-code)
  - [Table 0076 - Message Type](#table-0076-message-type)
  - [Table 0216 - Patient Status Codes](#table-0216-patient-status-codes)
  - [Table 0276 - Appointment Reason Codes](#table-0276-appointment-reason-codes-1)
  - [Table 0277 - Appointment Type Codes](#table-0277-appointment-type-codes-1)
  - [Table 0278 Filler Status Codes](#table-0278-filler-status-codes)
  - [Table VA01 - Yes/No](#table-va01-yesno)
  - [Table SD008 - Outpatient Classification Type](#table-sd008-outpatient-classification-type)
  - [Table SD009 - Purpose of Visit & Appointment Type](#table-sd009-purpose-of-visit-appointment-type)
  - [Table VA0021 – Enrollment Priority](#table-va0021-enrollment-priority-1)
  - [Table VA087 - Scheduling Event Reason](#table-va087-scheduling-event-reason-1)
  - [Table AAC001 - Error Code Set](#table-aac001-error-code-set-1)
  - [## Table VA088 – DSS ID and DSS Credit Stop](#table-va088-dss-id-and-dss-credit-stop)
  - [Appointment Selection Logic](#appointment-selection-logic)
  - [Acknowledgement Processing Logic](#acknowledgement-processing-logic)
  - [Whole Batch Accept](#whole-batch-accept)
  - [Whole Batch Reject](#whole-batch-reject)
  - [Whole Batch Accept with Rejections](#whole-batch-accept-with-rejections)
  - [Rejected Appointments Processing](#rejected-appointments-processing)
  - [Messages ExamplesExample Batch Message with the Consult Request Date – SCH.11](#messages-examplesexample-batch-message-with-the-consult-request-date-sch11)
- [Appendix B - VistA Interface Engine Site I.P. Addresses](#appendix-b-vista-interface-engine-site-ip-addresses)
- [Appendix C – Trouble Shooting](#appendix-c-trouble-shooting)
  - [Mail Notifications](#mail-notifications)
  - [HL7 System Monitor](#hl7-system-monitor)
  - [VistA Interface Engine](#vista-interface-engine)
  - [XTMP Global](#xtmp-global)
  - [## VistA Reporting](#vista-reporting)
  - [National Help Desk Reporting](#national-help-desk-reporting)
  - [VistA Communication Problems](#vista-communication-problems)
This patch contains several enhancements, modifications and a fix to the Patient Appointment Information Transmission, originally released in patch SD\*5.3\*290. A post install routine will delete all previous seeding and update data from file 409.6 and a new seeding run will be activated.
Data from all pending appointments within the range 9.01.2002 to present and data for final appointments, that meet specified criteria, beginning 9.01.2003 will be wrapped in HL7 batch messages and transmitted to the Austin Automation Center (AAC).
This additional data supplements the existing Clinic Appointment Wait Time extracts 1 & 2. At this time those extracts should continue to be transmitted on the 5<sup>th</sup> and 31<sup>st</sup> of each month as originally designated in SD\*5.3\*193. Further instructions will be provided when those transmissions will no longer be necessary.
The One –Time Option Queue from the Taskman Management menu will be used to start SD-PAIT TASKED TRANSMISSION on a scheduled date. Subsequent updating transmissions will be scheduled on 1<sup>st</sup> and 15<sup>th</sup> day of each month. The frequency of transmission may change based on reporting needs.

# Description of Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A bi-monthly Taskman job will collect and format data for HL7 batch transmission.

A set number of appointments, maximum of 5000, is collected in a temporary file. This file is used to create a HL7 batch transmission. After the batch data has been moved to the HL7 processing queue the temporary file is deleted and the process of generating data for transmission continues until all required data is generated and transmitted. The design allows for an immediate transmission after generation of partial data, and prevents the temporary file from becoming too large. The process is repeated until all required data is generated and transmitted.

Follow up transmissions begin scanning appointment data created from the day following the last scanned date saved at the end of each transmission in the last Scanned Date field (# 1.2) of the PATIENT APPOINTMENT INFO LOG file. Appointment statuses of previously transmitted data is also checked for final status values, (see SCH.25 Filler Status in the Interface Appendix). Entries in file 409.6 sent with the final status will be deleted after an HL7 acknowledgement of the successful transmission is received.

# Changes introduced with SD\*5.3\*333 patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch contains significant enhancements, modifications and a fix to the Patient Appointment Information Transmission - PAIT. The majority of enhancements are related to message transmission and tracking.

The transmission process involves several steps and makes use of new technology – the VistA Interface Engine .

\- Transmission to a local VistA Interface Engine

\- Transmission to the clustered Interface Engine at the AAC

\- Transmission and conversion of data to the AAC to create SAS files

A thorough review of all steps and the quality of data pointed us to the

following enhancements, modifications and a fix:

1\. Utilization of the server functionality of VA Mailman and creation of

a server option on Forum that will receive PAIT and AAC messages related to transmission and acknowledgements. Selected data elements from transmission and acknowledgement messages are parsed and filed in the PAIT TRANSMISSION LOG file (# 409.8) hosted on Forum. Report options provide transmission verification and history for all VA sites.

Field Description

DATE/TIME the date/time a transmission mail message

> is received by the FORUM server option

> SD-PAIT-SERVER

MESSAGE TYPE this field records the type of message received:

> A - Site Batch acknowledgement

> B - Site Background job transmission completion

> M - Missing sites report FROM AAC

> T –Transmitted sites report from AAC

SITE NUMBER a unique three digits facility site number

LOG NUMBER the log entry number of the transmission;

> this is the run entry number of the

> PATIENT multiple field in file 409.6

RUN COMPLETION DATE the date/time of the completed

> transmission; this is the TRANSMISSION

> FINISHED field (#1.5) of 409.6 file

\# OF BATCHES the number of batch messages transmitted

> from the site.

\# OF APPOINTMENTS the number of appointments included in

> all created batches.

IP ADDRESS the IP address of the Vitria Interface

> Engine set up at the PAIT transmission

> site.

BATCHES GENERATED the number of HL7 messages generated by

> the PAIT transmissions and recorded in

> SD-PAIT Logical Link; this number may include

> batches from the previous transmissions.

BATCHES SENT the number of HL7 messages sent to the

> local Interface Engine and recorded in the

> SD-PAIT Logical Link.

STATUS the status indicated by a received

> Message A or B:

> A – status of the acknowledgement completion

> B – status of the SD-PAIT Logical Link at the end of transmission

HL7 MESSAGE ID This field records the HL7 Message ID of

received acknowledgement.

BATCH CONTROL ID This field records the HL7 Batch ID of

received acknowledgement.

RUN ACK STATUS the ACK Status - the number ACK's received

> by HL7 vs the number of messages (batches) sent .

ACKS COMPLETE this field is marked YES if all ACK's for

> a PAIT transmission are received.

2\. Detailed information related to each transmission will be permanently stored in file 409.6

Field Description

> 1.3 \# OF APPOINTMENTS

> 1.4 \# OF BATCHES

> 1.5 TRANSMISSION FINISHED

> 2 PATIENT \<-Mult \[409.69P

9 CLINIC - pointer to the HOSPITAL LOCATION file

3 BATCH TRACKING \<-Mult \[409.7A\]

01 BATCH CONTROL ID

02 BATCH CREATE DATE/TIME

03 MESSAGE CONTROL ID

04 APPLICATION ACK DATE/TIME

05 APPLICATION ACK TYPE

3.  New report options for the site to print both the Transmission Summary and Acknowledgement Summary.

4.. New option SD-PAIT MANUAL BATCH REJECT to be used if a batch was

not accepted by the AAC, was sent from VistA and the whole batch rejection

has not been received.

> Note: In a future enhancement it is anticipated to generate the whole batch rejection from the AAC, after comparison of batch control number ID, sent from VistA with received by the AAC.

5\. To enhance the quality of data the following changes are introduced:

> New components are added to SCH.11, SCH6, and SCH.7 segments of

> HL7 transmission.

## ## ## ## Table VA087 - Scheduling Event Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|        |                          |
|--------|--------------------------|
| VALUE  | DESCRIPTION              |
| CI     | Check-in                 |
| CO     | Check-out                |
| NS     | No Show                  |
| CC     | Cancel by clinic         |
| CP     | Cancel by patient        |
| COE    | Check-out by encounter   |
| NM     | No Match                 |
| CT | Cancelled Terminated |

CT is the Event Reason to finalize an appointment that was sent as pending and then, during the update process a new appointment is created for the same date and time. That situation caused the previous appointment record to be overridden by the new appointment record with a new creation date.

## Table 0276 - Appointment Reason Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                 |
|-------|-------------------------------------------------|
| VALUE | DESCRIPTION                                     |
| 1     | Next Ava. Appt. Indicated by User               |
| 2     | Next Ava. Appt. Indicated by Calculation        |
| 3     | Next Ava. Appt. Indicated by User & Calculation |
| 4     | Not Next Available with AutoRebook              |
| 5     | Not Next Available No AutoRebook                |
| 6     | Null (All others)                               |

Appointment Reason Code table includes new six values instead of the previous

"N" and "A" only. It will allow for more detailed sorting criteria, especially when

calculating the next available time.

## ## SCH Schedule Activity Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><strong>LEN</strong></td>
<td><strong>DT</strong></td>
<td><strong>R/O/C</strong></td>
<td><strong>RP/#</strong></td>
<td><strong>TBL#</strong></td>
<td><strong>ITEM#</strong></td>
<td><strong>ELEMENT NAME</strong></td>
<td><strong>VISTA DESCRIPTION</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>75</td>
<td>EI</td>
<td>R</td>
<td></td>
<td></td>
<td>00860</td>
<td>Placer Appointment ID</td>
<td>Sequential Number</td>
</tr>
<tr class="odd">
<td>11</td>
<td>200</td>
<td>TQ</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00884</td>
<td>Appointment Timing Quantity</td>
<td><p>In the following order:</p>
<p>Date Appt Created</p>
<p>Desired Date</p>
<p>Appt Date (time)</p>
<p>Checkout Date (time)</p>
<p>Cancellation Date (time)</p>
<p>Auto-rebook Date (time)</p>
<p>Resched Date(time)</p>
<p>Consult Request Date (time)</p></td>
</tr>
</tbody>
</table>

Resched (uled) Date (time) was added as the scheduled Appointment Date/Time of the appointment created as a continuation of previously canceled appointment. This components is always sent when the RS – Re-scheduled Appointment Type is identified. Including that new component will help to identify the follow-up appointments in the AAC.

Consult Request Date (time) was added as a new sequence identifying an optional date/time of the consultation if there is one associated with the appointment.

## Table VA0021 – Enrollment Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| 8     | Priority 8  |

The indicated change applies only to the table description, the indicated value was used before.

## Table 0277 - Appointment Type Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| O     | Outpatient  |

The indicated change applies only to the table description, the indicated value was used before.

## 6\. The logic of generating appointments from the update runs has been modified to start from scanning newly created records and then to update the previous pending appointments, if applicable. Also the last scanned date is the last date before the start of transmission, to avoid possible duplications.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message generated at the end of transmission will contain additional information.

Subj: 500 - PAIT BACKGROUND JOB \[#151708\] 01/23/04@11:32 lines

The PAIT job has completed - TASK \#: 60720 Log \#: 1 on 1/23/04@11:32

Pending appointments: 10054

Final appointments: 1534

-----------

Total appointments: 11588 Number of batches: 3

Fac Log Bch Appt \# Date finished IP Address Gen Sent Com R Com P Status

-----------------------------------------------------------------------

500\| 1\| 3\| 11588\|1/23/04@11:32\|10.88.63.68\| 7\| 6\| 6\| 6\| Enabled

This message will be sent also to S.SD-PAIT-<SERVER@FORUM.VA.GOV> and to the National Help Desk, if number of generated and sent batches indicates that there is potential problem in communication between VistA site and its local Interface Engine. In this situation additional warning messages may be sent.

7\. Error codes for a possible rejection have been evaluated, modified and added by the AAC. The increased number of error code forced us to use a pointer to the PCMM Error Code file with adding the codes related to the PAIT.

## Table AAC001 - Error Code Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                                                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                                                                                                                                                                        |
| 100   | PATIENT DFN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                           |
| 150   | CLINIC IEN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                            |
| 200   | BHS STATION NUMBER AND STA3N ARE NOT EQUAL                                                                                                                                                                                         |
| 250   | INVALID OR MISSING BHS STATION NUMBER                                                                                                                                                                                              |
| 300   | INVALID OR MISSING STA3N                                                                                                                                                                                                           |
| 350   | HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING.                                                                                                                                                                                    |
| 400   | DOB IS MISSING OR INVALID                                                                                                                                                                                                          |
| 450   | CREATE DATE OR APPT DATE IS MISSING                                                                                                                                                                                                |
| 500   | CREATION DATE IS BEFORE SEPTEMBER 1, 2002                                                                                                                                                                                          |
| 600   | RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT - Rescheduled date requires SCH.8 Appt type = 'RS' and vice versa                                                                                                              |
| 650   | CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT - Check out date requires either SCH.6 Event reason = 'CO' or 'COE'                                                                                                           |
| 700   | CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT - Cancellation date requires SCH.6 Event reason = 'CC' or 'CP' or 'NS'                                                                                                     |
| 750   | EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT - All SCH.6 Event reason codes, except 'CI' require SCH.25 Filler status to be 'F' Final and accordingly only 'CI' and NULL should have SCH.25 Filler status to be 'P' Pending |
| 800   | FILLER STATUS IS MISSING OR IS INVALID                                                                                                                                                                                             |
| 850   | ADMIT TYPE IS INVALID (table SD009)                                                                                                                                                                                                |
| R     | WHOLE BATCH REJECTED                                                                                                                                                                                                               |

R – Whole Batch Reject may be used with the manual batch rejection.

8\. Application acknowledgements will be recognized by messages sent both to a local SD-PAIT Mail Group and to S.SD-PAIT-<SERVER@FORUM.VA.GOV>

9\. New and updated SORT/PRINT TEMPLATES (See Technical Information).

10\. Independent reports, reflecting the transmission status, have been

developed both by the AAC and Messaging and Interface Services Team.

11\. Conversion data to HL7 formats have been verified and corrected.

12\. The Release Notes have been updated with additional, detailed, functional

and technical information.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch has POST INSTALL INSTRUCTIONS that must be completed.

Documentation, Release Notes & Installation Guide:

> SD_53_P333_RN.PDF

KIDS Host File:

SD_53_P333.KID

The preferred method is to FTP the file from:

download.vista.med.va.gov

which will transmit the files from the first available FTP server.

The files may also be downloaded directly from a particular FTP

location at the following locations.

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

This patch may be installed with users on the system. Installation will take less than 2 minutes.

> Use the 'LOAD A DISTRIBUTION' option on the KERNEL

> INSTALLATION & DISTRIBUTION menu. The host file name is

> SD_53_P333.KID. Answer YES to the question: 'Want to Continue with the

> Load? YES//'\]

> Review your mapped set. If any of the routines listed in the

> ROUTINE SUMMARY section are mapped, they should be removed

> from the mapped set at this time.

> From the Kernel Installation and Distribution System Menu, select

> the Installation menu.

> From this menu, you may elect to use the following options

> (when prompted for INSTALL NAME, enter SD\*5.3\*333):

> Backup a Transport Global – this option will create a backup

> message of any routines exported with the patch. It will NOT

> backup any other changes such as DDs or templates.

Compare Transport Global to Current System - this option will

allow you to view all changes that will be made when the patch

> is installed. It compares all components of the patch (routines,

> DDs, templates, etc.).

> Verify Checksums in Transport Global – this option will

allow you to ensure the integrity of the routines that are in

> the transport global.

> Print Transport Global – this option will allow you to view the

> components of the KIDS build.

> Use the Install Package(s) option and select the package SD\*5.3\*333.

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: SD\*5.3\*333 Loaded from Distribution MM/DD/YYYY

=\> SD\*5.3\*333

This Distribution was loaded on MM/DD/YYYY with header of

SD\*5.3\*333

It consisted of the following Install(s):

SD\*5.3\*333

Checking Install for Package SD\*5.3\*333

> Incoming Files:

> 404.472 PCMM HL7 ERROR CODE (including data)

> Note: You already have the 'PCMM HL7 ERROR CODE' File.

> I will OVERWRITE your data with mine.

> 409.6 PATIENT APPOINTMENT INFO LOG

> Note: You already have the 'PATIENT APPOINTMENT INFO LOG' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install Press Return.

> If routines were unmapped as part of step 2, they should be returned

> to the mapped set once the installation has run to completion.

> SD-PAIT REPORTS option is a stand alone menu and should be assigned to the appropriate users who monitor patient appointment wait times. SD-PAIT MANUAL TRANSMISSION should be assigned to an IRM staff member or HAS ADPAC.

Sample Installation:

Select Installation Option: INstall Package(s)

Select INSTALL NAME: SD\*5.3\*333 Loaded from Distribution 1/28/04@14:32:01

=\> SD\*5.3\*333

This Distribution was loaded on Jan 28, 2004@14:32:01 with header of

SD\*5.3\*333

It consisted of the following Install(s):

SD\*5.3\*333

Checking Install for Package SD\*5.3\*333

Incoming Files:

404.472 PCMM HL7 ERROR CODE (including data)

> **NOTE:** You already have the 'PCMM HL7 ERROR CODE' File.

I will OVERWRITE your data with mine.

409.6 PATIENT APPOINTMENT INFO LOG

> **NOTE:** You already have the 'PATIENT APPOINTMENT INFO LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// UCX/TELNET

Install Started for SD\*5.3\*333 :

Jan 28, 2004@14:37:19

Build Distribution Date: Jan 28, 2004

Installing Routines:

Jan 28, 2004@14:37:19

Installing Data Dictionaries:

Jan 28, 2004@14:37:20

Installing Data:

Jan 28, 2004@14:37:20

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

SD\*5.3\*333

─────────────────────────────────────────────────────────────────────────────

Installing PROTOCOL

Installing OPTION

Jan 28, 2004@14:37:21

Updating Routine file...

Updating KIDS files...

SD\*5.3\*333 Installed.

Jan 28, 2004@14:37:21

Install Message sent \#1852746

─────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

# Post Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run Post Init Routine SDP333P

From the programmer prompt run routine SDP333P

BAY\>D ^SDP333P

SD\*5.3\*333 POST INIT

Clean-Up file 409.6? NO// ?

ATTENTION: Answering 'YES' will delete all entries from file 409.6

(Patient Appointment Information Transmission). This is CORRECT

for a first installation of the patch. If you are re-installing the

patch and want to keep the entries in 409.6 answer 'NO'

If this is the first installation of the patch answer 'YES'

Clean-Up file 409.6? NO// YES

PAIT Clean-UP Task Submitted. Task number: nnnnn

Members of the SD-PAIT mail group will receive a notification message

when the clean-up job has completed.

Example Mail Message:

Subj: PAIT Clean-Up \[#152206\] 02/03/04@10:25 3 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

The PAIT Clean-Up, task \#nnnnn, from the post installation

of SD\*5.3\*333 has completed. You may resume post installation activities.

Enter message action (in IN basket): Ignore//

Post init routine, SDP333P, may be deleted after clean-up has completed.

Insure the SD-PAIT logical link is ENABLED:

Select HL7 Main Menu Option:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: SD-PAIT

This LLP has been enabled!

![](sd-5-3-333-pait-release-notes/002.png)

Edit the new SD-PAIT logical link:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Interface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL Link Edit

Select HL LOGICAL LINK NODE: SD-PAIT

![](sd-5-3-333-pait-release-notes/003.png)

![](sd-5-3-333-pait-release-notes/004.png)

Enter the TCP/IP ADDRESS of your VistA Interface Engine

See Appendix B to determine your sites I.P. Address for the Interface Engine.

Enter the TCP/IP PORT – 9270

![](sd-5-3-333-pait-release-notes/005.png)

> To begin the initial March 15<sup>th</sup> seeding run use Taskman option "One-time Option Queue" and select option SD-PAIT TASKED TRANSMISSION.

> When prompted 'Does this option need a DEVICE? NO//' press return.

> When prompted 'Enter Particular Volume set if needed:' press return.

> When prompted 'Requested Start Time: NOW//' press return. Optionally, you may elect to schedule the initial seeding run to begin during off peak hours.

The initial seeding run will be executed only once, on March 15, 2004.

![](sd-5-3-333-pait-release-notes/006.png)

> Using Taskman option Schedule/Unschedule Options schedule option SD-PAIT TASKED TRANSMISSION to run the 1<sup>st</sup> and 15<sup>th</sup> of every month. It is important to schedule the first tasked run to begin on 4.01.2004 (time is site selectable). This establishes the bi-monthly transmission schedule with the first transmission taking place on 4.01.2004

If your TASKED TRANSMISSION does not start on the 1<sup>st</sup> or 15<sup>th</sup> contact the National Help Desk (1 888 596 4357) before re-scheduling the transmission on a day other than the 1<sup>st</sup> or the 15<sup>th</sup>.

![](sd-5-3-333-pait-release-notes/007.png)

> A MailMan message addressed to the SD-PAIT mail group will confirm completion of the tasked job.

# User Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option "SD-PAIT REPORTS PAIT Reports Menu" provides four reports:

SD-PAIT PENDING Pending Transmissions

SD-PAIT REJECTED Rejected Transmissions

SD-PAIT ACK SUMMARY Acknowledgement Summary

SD-PAIT TRANSMISSION SUMMARY Transmission Summary

Pending Transmissions will list all transmitted HL7 messages whose status is Pending, but not designated as a future appointment. This report is a diagnostic tool useful for follow-up of inpatient appointments that have not been dispositioned.

Rejected Transmissions will list all transmitted HL7 messages that have been rejected by the AAC. The AAC will reject messages in which the data is not correctly formatted. Entries on this list warrant a review by the MAS ADPAC to validate patient demographic data.

Acknowledgement Summary lists all batches in Batch Control ID order. The report also indicates the Message Control ID, the Acknowledgement Date, and Acknowledgement Type.

Transmission Summary report may be used to determine the total number of patient appointment records, the run date, total number of batches, Batch Control ID, Message Control ID, and date/time stamp.

Option " SD-PAIT MANUAL TRANSMISSION Manual Startup PAIT Transmission" can be used to start a transmission if needed

# MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan notification messages are generated for two events.

1.  Background processing has completed:

<u>Legend:</u>

Fac - VistA Site Facility Number

Log - Run number

Bch - Number of generated batches

Appt \# - Number of Appointments

Date finished - Date/time when the transmission has finished

IP Address - IP Address of HL Logical Link "SD_PAIT"

Gen - Number of batches generated ( including previous transmissions)

Send - Number of all sent batches (including previous transmissions)

Com R - Number of Commit Ack Received

Com P - Number of Commit Ack Processed

Status - Status of 'SD-PAIT" link at the end of transmission

2\. Batch acknowledgement message from the AAC is received by the local HL7 package:

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SD\*5.3\*333 Imports the following components:POST-INIT ROUTINE

SDP333P (May be deleted after install)

FILES - updated

6.  PATIENT APPOINTMENT INFO LOG

> 404.472 PCMM HL7 ERROR CODE FILE

GLOBALS

^SDWL(409.6

^SCPT(404.472,

NEW AND MODIFIED PRINT TEMPLATES

SD-PAIT PAIT ACK SUMMARY

SD-PAIT PATIENT PENDING APPT

SD-PAIT REJECTED APPT

SD-PAIT TRANS SUMMARY

NEW AND MODIFIED SORT TEMPLATES

SD-PAIT PAIT ACK SOR

SD-PAIT PEND EXCL FUTURE

SD-PAIT REJECTED APPT

SD-PAIT TRANS SUMMARY

MAIL GROUP

SD-PAIT

MODIFIED ROUTINES

SDRPA00

SDRPA05

SDRPA06

SDRPA07

SDRPA08

NEW ROUTINE

SDRPA09

OPTIONS

SD-PAIT MANUAL TRANSMISSION

SD-PAIT TASKED TRANSMISSION

SD-PAIT REPORTS

SD-PAIT PENDING

SD-PAIT REJECTED

SD-PAIT TRANSMISSION SUMMARY

SD-PAIT ACK SUMMARY

PROTOCOLS

SD-PAIT-EVENT

SD-PAIT-SUBS

HL7 APPLICATION PARAMETERS

SD-AAC-PAIT

SD-SITE-PAIT

HL LOGICAL LINK

SD-PAIT

BACKGROUND JOB

SD-PAIT TASKED TRANSMISSION

SECURITY KEYS

NONE

BULLETINS

NO BULLETINS are generated with this patch. Please reference MAILMAN

NOTIFICATION MESSAGES listed above

## Initial Seeding Run Times:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## |                                    |                       |                    |                                 |              |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|------------------------------------|-----------------------|--------------------|---------------------------------|--------------|
| Site                           | Patients (File 2) | Batch Messages | Entries Added to file 409.6 | Run Time |
| <span class="mark">REDACTED</span> | 410,263               | 77                 | 380,795                         | 3.5 days     |
| <span class="mark">REDACTED</span> | 72,589                | 21                 | 102,425                         | 1 day        |
| <span class="mark">REDACTED</span> | 71,295                | 18                 | 88,933                          | 1 day        |
| <span class="mark">REDACTED</span> | 213,732               | 27                 | 133,397                         | 1.5 days     |

GLOBAL GROWTH

Each entry added to file 409.6 takes approximately 250 bytes. A medium to large site will require at least 120MB of available space on the volume set containing the ^SDWL(409.6 global to accommodate the initial seeding process.

HL7 messages generated by the seeding process take approximately 4 Mb per batch message. A medium to large site will generate 60 to 100 batches on the initial seeding run which corresponds to at least 240Mb of available space on the volume set containing the HL7 globals.

^XMTP globals are created and used to record acknowledgment processing and have been defined to remain in the system for three days.

^XTMP("SDRPA-"\_BATCHNUMBER, \[Diagnostics\]

# Appendix A – HL7 Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 Interface Specification for Patient Appointment Information Transmission

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface specification details the information needed for the Patient Appointment Information Transmission data reporting. This data transmission will be triggered by a TaskMan queued job in VistA. The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The formats of these messages conform to the Version 2.4 HL7 Interface Standards where applicable. HL7 custom message formats ("Z" segments) are used only when necessary.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below describes the data fields and HL7 mappings:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 34%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Data item</strong></td>
<td><strong>Length</strong></td>
<td><strong>Type</strong></td>
<td><strong>Definition</strong></td>
<td><strong>HL7</strong></td>
</tr>
<tr class="even">
<td>Integration Control Number</td>
<td>10</td>
<td>Alpha-numeric</td>
<td>ICN is a VHA wide internal key, uniquely assigned to each PATIENT. The ICN is a 10 digit.</td>
<td>PID.3</td>
</tr>
<tr class="odd">
<td>Patient's DFN</td>
<td>8</td>
<td>Numeric</td>
<td>The internal number of the patient from within the Patient file.</td>
<td>PID.3</td>
</tr>
<tr class="even">
<td>Patient's SSN</td>
<td>10</td>
<td>9 Numeric, 1 Alpha</td>
<td>The social security number or the generated pseudo SSN of the patient.</td>
<td>PID.19</td>
</tr>
<tr class="odd">
<td><p>Last Name</p>
<p>First Name</p>
<p>Middle Name</p></td>
<td>45</td>
<td>Text</td>
<td>The name of the patient. Held as three distinct names with a combined maximum length of 45 characters</td>
<td>PID.5</td>
</tr>
<tr class="even">
<td>Date Of Birth</td>
<td>8</td>
<td>Date</td>
<td>The date of birth of the patient.</td>
<td>PID.7</td>
</tr>
<tr class="odd">
<td>Current SC status</td>
<td>1</td>
<td>Text</td>
<td>Current service connected status, Y/N</td>
<td>ZSP.2</td>
</tr>
<tr class="even">
<td>Current SC percentage</td>
<td>3</td>
<td>Numeric</td>
<td>Current service connected percentage</td>
<td>ZSP.3</td>
</tr>
<tr class="odd">
<td>Date Appointment Created</td>
<td>8</td>
<td>Date</td>
<td>The date the appointment was created</td>
<td>SCH.11</td>
</tr>
<tr class="even">
<td>Desired Appointment Date</td>
<td>8</td>
<td>Date</td>
<td>The date the appointment was requested to take place.</td>
<td>SCH.11</td>
</tr>
<tr class="odd">
<td>Appointment Date</td>
<td>12</td>
<td>Date/time</td>
<td>The date the appointment was scheduled to be kept.</td>
<td>SCH.11</td>
</tr>
<tr class="even">
<td>Appointment status</td>
<td>3</td>
<td>Text</td>
<td>See table 0278</td>
<td>SCH.25</td>
</tr>
<tr class="odd">
<td>Next Available Request Flags</td>
<td>1</td>
<td>Numeric</td>
<td>See table 0276</td>
<td>SCH.7</td>
</tr>
<tr class="even">
<td>Cancellation Date</td>
<td>12</td>
<td>Date/time</td>
<td>If the appointment was cancelled by the clinic or the patient, the date of cancellation.</td>
<td>SCH.11</td>
</tr>
<tr class="odd">
<td>Reschedule Date</td>
<td>12</td>
<td>Date/time</td>
<td>The date an appointment was rescheduled for without auto-rebooking</td>
<td>SCH.11</td>
</tr>
<tr class="even">
<td>Auto-rebook Flag</td>
<td>1</td>
<td>Numeric</td>
<td>See table 0276</td>
<td>SCH.7</td>
</tr>
<tr class="odd">
<td>Auto-rebook Date</td>
<td>12</td>
<td>Date/time</td>
<td>Date of the auto-rebooked appointment</td>
<td>SCH.11</td>
</tr>
<tr class="even">
<td>New to Facility/Clinic Flag</td>
<td>1</td>
<td>Text</td>
<td>NTF if the patient did not have a prior appointment at this facility in the past 24 months. SHB otherwise.</td>
<td>PV2.24</td>
</tr>
<tr class="odd">
<td>Enrollment Priority</td>
<td>1</td>
<td>Alpha numeric</td>
<td>See table VA0021</td>
<td>ZEN</td>
</tr>
<tr class="even">
<td>Service Connection Condition Flag</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="odd">
<td>Agent Orange Exposure</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="even">
<td>Ionizing Radiation Exposure</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="odd">
<td>Environmental Contaminants</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="even">
<td>Military Sexual Trauma</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="odd">
<td>Head and/or Neck Cancer</td>
<td>1</td>
<td>Numeric</td>
<td>See table SD008</td>
<td>ZCL.2</td>
</tr>
<tr class="even">
<td>Clinic IEN Number</td>
<td>6</td>
<td>Numeric</td>
<td>Internal Identifier of the Hospital Location the appointment was scheduled for.</td>
<td>AIL.3.1</td>
</tr>
<tr class="odd">
<td>Clinic Name</td>
<td>30</td>
<td>Text</td>
<td>Name of Clinic from file 44</td>
<td>AIL.3.9</td>
</tr>
<tr class="even">
<td>DSS Identifier of Clinic</td>
<td>3</td>
<td>Numeric</td>
<td>Stop code of the Hospital Location file the appointment was scheduled for.</td>
<td>AIL.4</td>
</tr>
<tr class="odd">
<td>DSS Credit Stop of Clinic</td>
<td>3</td>
<td>Numeric</td>
<td>Credit stop code of the Hospital Location file</td>
<td>AIL.5</td>
</tr>
<tr class="even">
<td>Facility Number</td>
<td>6</td>
<td>Three digit numeric station number plus any modifiers</td>
<td>Station Number, field #99 from the Institution file</td>
<td>PV1.39</td>
</tr>
<tr class="odd">
<td>Provider</td>
<td></td>
<td>Text</td>
<td><p>IEN and name of provider associated with the</p>
<p>Hospital Location</p></td>
<td>AIP.3</td>
</tr>
<tr class="even">
<td>Check out Date</td>
<td>12</td>
<td>Date/time</td>
<td>Date of appointment checkout. It is considered to be a kept appointment.</td>
<td>SCH.11</td>
</tr>
<tr class="odd">
<td>Appointment Type</td>
<td>3</td>
<td>Alpha</td>
<td>See Table 0277</td>
<td>SCH.8</td>
</tr>
<tr class="even">
<td>Scheduling Event Reason</td>
<td>3</td>
<td>Alpha</td>
<td>See Table VA087</td>
<td>SCH.6</td>
</tr>
<tr class="odd">
<td>Admission Type</td>
<td>4</td>
<td>Numeric</td>
<td>See table SD009</td>
<td>PV1.4</td>
</tr>
<tr class="even">
<td>Consult Request Date</td>
<td>12</td>
<td>Date</td>
<td><p>The request date and time of the related consult if applicable – the DATE OF REQUEST field (#3) of the REQUEST/</p>
<p>CONSULTATION</p>
<p>file (#123).</p></td>
<td>SCH.11</td>
</tr>
</tbody>
</table>

> **NOTE:** If the appointment is SC (Service Connected) related then only MST and

Head and/or Neck cancer may be identified as well. All other classifications

can be claimed only if the appointment is not SC.

|           |                                                      |             |
|-----------|------------------------------------------------------|-------------|
| SIU   | SIU Message                                      | Section |
| BSH       | Batch Header                                         | 2.3.2       |
| {MSH      | Message Header                                       | 2.3.1       |
| SCH       | Schedule Activity Information                        | 2.3.9       |
| PID       | Patient Identification                               | 2.3.4       |
| PV1       | Patient Visit                                        | 2.3.5       |
| PV2       | Patient Visit                                        | 2.3.6       |
| \[{AIP}\] | Appointment information - personnel resource segment | 2.3.7       |
| {AIL}     | Appointment Information                              | 2.3.8       |
| \[{ZCL}\] | VA-Specific Outpatient Classification                | 2.3.10      |
| \[{ZEN}\] | VA Specific Enrollment                               | 2.3.11      |
| {ZSP}}    | VA-Specific Service Period                           | 2.3.12      |
| BTS       | Batch Trailer                                        | 2.3.3       |

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Taskman background job will be scheduled to run at specified intervals. The background job will collect and format data for HL7 batch transmission.

A determined number of appointments is generated into a temporary file. That file is sent to create HL7 transmission in a batch format. As soon as the batch is put into a queue, the temporary file is deleted and the process of generating data for transmission continues until all required data is generated and transmitted. That design allows for an immediate transmission after generation of a partial data, and prevents the temporary file from growing tremendously before it is sent for transmission. The process is repeated until all required data is generated and transmitted.

The follow up transmissions will be created as batch messages with all appointments made starting from the next date to the last scanned appointment creation date of the last transmission, and with previously sent appointments, if their statuses turn out to have one of the final values, see SCH.25. Filler Status in SIU Event Mapping Table. The previously sent appointments are evaluated for a possible final transmission from the Patient Transmission Info Log file (#409.6). Appointments entries in that file that were sent with the final status will be deleted after an acknowledgement of the successful transmission is received.

## Batch Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Batch messages will be used to transmit patient appointment information. Each batch message may contain up to 5000 messages. One message will represent one patient appointment.

## Batch Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each batch message sent will be acknowledged at the application level.

## Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCP/IP will be used.

## HL7 Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA and implemented in this transmission. The messages are presented separately and defined by category. Segments are also described.

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category there will be a list of HL7 standard segments or "Z" segments used for the message.

## ## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL \#), the element name, and the VistA description. Each segment is described in the following sections.

## ## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments which are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings will be as specified here, unless otherwise specified in that section.

## MSH - Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th><em>VISTA</em> DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<blockquote>
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = <strong>&amp;</strong> (ampersand)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td><p>When originating from facility:</p>
<blockquote>
<p><strong>SD-SITE-PAIT</strong></p>
</blockquote>
<p>When originating from ACC:</p>
<p><strong>SD-AAC-PAIT</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td><p>When originating from facility:</p>
<blockquote>
<p>Station's facility number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td><blockquote>
<p><strong>SD-AAC-PAIT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td><blockquote>
<p>200</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p><u>2 Components</u></p>
<ol type="1">
<li><p>Message type</p></li>
<li><p>Trigger event</p></li>
</ol></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Batch and sequence number automatically generated by <strong>VISTA</strong> HL7 Package</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Processing ID</td>
<td><strong>P</strong> (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Version ID</td>
<td><strong>2.4</strong> (Version 2.4)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Accept Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Application Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>USA</td>
</tr>
</tbody>
</table>

## BHS – Batch Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VISTA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Field Separator</td>
<td>Recommended value is <strong>^</strong></td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Encoding Characters</td>
<td><p>Delimiter values:</p>
<blockquote>
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = <strong>&amp;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Application</td>
<td><p>When originating from facility: <strong>SD-SITE-PAIT</strong></p>
<p>When originating from AAC:</p>
<blockquote>
<p><strong>SD-ACC-PAIT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Facility</td>
<td><p>When originating from facility:</p>
<p>Station's facility number</p>
<p>when originating from AAC: <strong>200</strong></p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Application</td>
<td><p>When originating from facility: <strong>SD-ACC-PAIT</strong></p>
<p>When originating from AAC:</p>
<blockquote>
<p><strong>SD-SITE-PAIT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Facility</td>
<td><p>When originating from facility:</p>
<blockquote>
<p>Station's facility number</p>
</blockquote>
<p>When originating from AAC: <strong>200</strong></p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Batch Creation Date/Time</td>
<td>Date and time batch message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Name/ID/Type</td>
<td><p>Components</p>
<ol type="1">
<li><p>Not used</p></li>
<li><p>P</p></li>
<li><p>SIU,S12</p></li>
<li><p>2.4</p></li>
</ol>
<p>5. AL</p>
<p>6. AL</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td>0008</td>
<td>Batch Comment</td>
<td><p><u>Components</u></p>
<ol type="1">
<li><p>Acknowledgement Code</p></li>
<li><p>Text Message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td><p>When originating from facility:</p>
<blockquote>
<p>Automatically generated by <strong>VISTA</strong> HL7 Package</p>
</blockquote>
<p>When Originating from AAC:</p>
<p>Acknowledgement msg #</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td><p>When originating from facility: Null</p>
<p>When originating from AAC:</p>
<blockquote>
<p>Batch Control ID of batch message being acknowledged</p>
</blockquote></td>
</tr>
</tbody>
</table>

## BTS - Batch Trailer Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME        | VISTA DESCRIPTION               |
|-----|-----|-----|-----|------|------|---------------------|---------------------------------|
| 1   | 10  | ST  |     |      |      | Batch Message Count | Number of messages within batch |
| 2   | 80  | ST  |     |      |      | Batch Comment       | Not used                        |
| 3   | 100 | CM  |     | Y    |      | Batch Totals        | Not used                        |

## PID - Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VISTA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>17</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Primary Long ID</td>
</tr>
<tr class="odd">
<td>3</td>
<td>21</td>
<td>CM</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Component</p>
<p>1. ICN</p>
<p>2. NULL</p>
<p>3. NULL</p>
<p>4. USVHA&amp;&amp;L</p>
<p>5. NI</p>
<p>Repetition</p>
<ol type="1">
<li><p>DFN</p></li>
<li><p>Null</p></li>
<li><p>Null</p></li>
<li><p>USVHA&amp;&amp;L</p></li>
<li><p>PI</p></li>
</ol></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td><p>Component</p>
<ol type="1">
<li><p>Family name</p></li>
<li><p>Given name</p></li>
<li><p>Middle initial</p></li>
<li><p>Suffix</p></li>
</ol></td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Sex</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td></td>
<td></td>
<td>Patient Alias</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Race</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Patient Address</td>
<td>Zip Code</td>
</tr>
</tbody>
</table>

## PID - Patient Identification Segment (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     |     |     |     |     |     |                            |                                             |
|-----|-----|-----|-----|-----|-----|----------------------------|---------------------------------------------|
| 12  | 4   | ID  |     |     |     | County Code                | Not used                                    |
| 13  | 40  | TN  |     |     |     | Phone Number - Home        | Not used                                    |
| 14  | 40  | TN  |     |     |     | Phone Number - Business    | Not used                                    |
| 15  | 25  | ST  |     |     |     | Language - Patient         | Not used                                    |
| 16  | 1   | ID  |     |     |     | Marital Status             | Not used                                    |
| 17  | 3   | ID  |     |     |     | Religion                   | Not used                                    |
| 18  | 20  | CK  |     |     |     | Patient Account Number     | Not used                                    |
| 19  | 16  | ST  |     |     |     | SSN Number - Patient       | Social security number and pseudo indicator |
| 20  | 25  | CM  |     |     |     | Driver's Lic Num - Patient | Not used                                    |
| 21  | 20  | CK  |     |     |     | Mother's Identifier        | Not used                                    |
| 22  | 1   | ID  |     |     |     | Ethnic Group               | Not used                                    |
| 23  | 25  | ST  |     |     |     | Birth Place                | Not used                                    |
| 24  | 2   | ID  |     |     |     | Multiple Birth Indicator   | Not used                                    |
| 25  | 2   | NM  |     |     |     | Birth Order                | Not used                                    |
| 26  | 3   | ID  |     |     |     | Citizenship                | Not used                                    |
| 27  | 60  | CE  |     |     |     | Veterans Military Status   | Not used                                    |

## PV1 - Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME              | VISTA DESCRIPTION                                        |
|-----|-----|-----|-----|------|------|---------------------------|----------------------------------------------------------|
| 1   | 4   | SI  |     |      |      | Set ID - Patient Visit    | Sequential Number                                        |
| 2   | 1   | ID  |     |      | 0004 | Patient Class             | Patient Class                                            |
| 3   | 12  | CM  |     |      |      | Assigned Patient Location | Not used                                                 |
| 4   | 4   | ID  |     |      | 0007 | Admission Type            | Refer to table SD009 (Purpose of Visit/Appointment Type) |
| 5   | 20  | ST  |     |      |      | Preadmit Number           | Not used                                                 |
| 6   | 12  | CM  |     |      |      | Prior Patient Location    | Not used                                                 |
| 7   | 60  | CN  |     |      |      | Attending Doctor          | Not used                                                 |
| 8   | 60  | CN  |     |      |      | Referring Doctor          | Not used                                                 |
| 9   | 60  | CN  |     |      |      | Consulting Doctor         | Not used                                                 |
| 10  | 3   | ID  |     |      |      | Hospital Service          | Not used                                                 |
| 11  | 12  | CM  |     |      |      | Temporary Location        | Not used                                                 |
| 12  | 2   | ID  |     |      |      | Preadmit Test Indicator   | Not used                                                 |
| 13  | 2   | ID  |     |      |      | Readmission Indicator     | Not used                                                 |
| 14  | 3   | ID  |     |      |      | Admit Source              | Not used                                                 |
| 15  | 2   | ID  |     |      |      | Ambulatory Status         | Not used                                                 |
| 16  | 2   | ID  |     |      |      | VIP Indicator             | Not used                                                 |
| 17  | 60  | CN  |     |      |      | Admitting Doctor          | Not used                                                 |
| 18  | 2   | ID  |     |      |      | Patient Type              | Not used                                                 |
| 19  | 15  | NM  |     |      |      | Visit Number              | Not used                                                 |
| 20  | 50  | CM  |     |      |      | Financial Class           | Not used                                                 |
| 21  | 2   | ID  |     |      |      | Charge Price Indicator    | Not used                                                 |
| 22  | 2   | ID  |     |      |      | Courtesy Code             | Not used                                                 |
| 23  | 2   | ID  |     |      |      | Credit Rating             | Not used                                                 |
| 24  | 2   | ID  |     |      |      | Contract Code             | Not used                                                 |

PV1 - Patient Visit Segment (continued)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME              | VISTA DESCRIPTION                          |
|-----|-----|-----|-----|------|------|---------------------------|--------------------------------------------|
| 25  | 8   | DT  |     |      |      | Contract Effective Date   | Not used                                   |
| 26  | 12  | NM  |     |      |      | Contract Amount           | Not used                                   |
| 27  | 3   | NM  |     |      |      | Contract Period           | Not used                                   |
| 28  | 2   | ID  |     |      |      | Interest Code             | Not used                                   |
| 29  | 1   | ID  |     |      |      | Transfer to Bad Debt Code | Not used                                   |
| 30  | 8   | DT  |     |      |      | Transfer to Bad Debt Date | Not used                                   |
| 31  | 10  | ID  |     |      |      | Bad Debt Agency Code      | Not used                                   |
| 32  | 12  | NM  |     |      |      | Bad Debt Transfer Amount  | Not used                                   |
| 33  | 12  | NM  |     |      |      | Bad Debt Recovery Amount  | Not used                                   |
| 34  | 1   | ID  |     |      |      | Delete Account Indicator  | Not used                                   |
| 35  | 8   | DT  |     |      |      | Delete Account Date       | Not used                                   |
| 36  | 3   | ID  |     |      |      | Discharge Disposition     | Not used                                   |
| 37  | 25  | CM  |     |      |      | Discharged to Location    | Not used                                   |
| 38  | 2   | ID  |     |      |      | Diet Type                 | Not used                                   |
| 39  | 7   | ID  |     |      |      | Servicing Facility        | Facility number or Facility number+ suffix |
| 40  | 1   | ID  |     |      |      | Bed Status                | Not used                                   |
| 41  | 2   | ID  |     |      |      | Account Status            | Not used                                   |
| 42  | 12  | CM  |     |      |      | Pending Location          | Not used                                   |
| 43  | 12  | CM  |     |      |      | Prior Temporary Location  | Not used                                   |
| 44  | 26  | TS  |     |      |      | Admit Date/Time           | Not used                                   |
| 45  | 26  | TS  |     |      |      | Discharge Date/Time       | Not used                                   |
| 46  | 12  | NM  |     |      |      | Current Patient Balance   | Not used                                   |
| 47  | 12  | NM  |     |      |      | Total Charges             | Not used                                   |
| 48  | 12  | NM  |     |      |      | Total Adjustments         | Not used                                   |
| 49  | 12  | NM  |     |      |      | Total Payments            | Not used                                   |
| 50  | 20  | CM  |     |      |      | Alternate Visit ID        | Not used                                   |

2.3.6 PV2 Patient Visit

| SEQ | LEN | DT | R/ | RP/# | TBL# | ITEM# | ELEMENT NAME                     | VISTA DESCRIPTION   |
|---------|---------|--------|--------|----------|----------|-----------|--------------------------------------|-------------------------|
| 1       | 80      | PL     | C      |          |          | 0011      | Prior Pending Location               | Not used                |
| 2       | 60      | CE     | O      |          |          | 0012      | Accommodation Code                   | Not used                |
| 3       | 60      | CE     | O      |          |          | 0013      | Admit Reason                         | Not used                |
| 4       | 60      | CE     | O      |          |          | 0014      | Transfer Reason                      | Not used                |
| 5       | 25      | ST     | O      |          |          | 0015      | Patient Valuables                    | Not used                |
| 6       | 25      | ST     | O      |          |          | 0016      | Patient Valuables Location           | Not used                |
| 7       | 2       | IS     | O      |          |          | 0017      | Visit User Code                      | Not used                |
| 8       | 26      | TS     | O      |          |          | 0018      | Expected Admit Date/Time             | Not used                |
| 9       | 26      | TS     | O      |          |          | 0019      | Expected Discharge Date/Time         | Not used                |
| 10      | 3       | NM     | O      |          |          | 0071      | Estimated Length of Inpatient Stay   | Not used                |
| 11      | 3       | NM     | O      |          |          | 0072      | Actual Length of Inpatient Stay      | Not used                |
| 12      | 50      | ST     | O      |          |          | 0073      | Visit Description                    | Not used                |
| 13      | 90      | XCN    | O      |          |          | 0074      | Referral Source Code                 | Not used                |
| 14      | 8       | DT     | O      |          |          | 0075      | Previous Service Date                | Not used                |
| 15      | 1       | ID     | O      |          |          | 0076      | Employment Illness Related Indicator | Not used                |
| 16      | 1       | IS     | O      |          |          | 0077      | Purge Status Code                    | Not used                |
| 17      | 8       | DT     | O      |          |          | 0078      | Purge Status Date                    | Not used                |
| 18      | 2       | IS     | O      |          |          | 0079      | Special Program Code                 | Not used                |
| 19      | 1       | ID     | O      |          |          | 0070      | Retention Indicator                  | Not used                |
| 20      | 1       | NM     | O      |          |          | 0071      | Expected Number of Insurance Plans   | Not used                |
| 21      | 1       | IS     | O      |          |          | 0072      | Visit Publicity Code                 | Not used                |
| 22      | 1       | ID     | O      |          |          | 0073      | Visit Protection Indicator           | Not used                |
| 23      | 90      | XON    | O      |          |          | 0074      | Clinic Organization Name             | Not used                |
| 24      | 2       | IS     | O      |          | 0216     | 0075      | Patient Status Code                  | New to Facility/ Clinic |
| 25      | 1       | IS     | O      |          |          | 0076      | Visit Priority Code                  | Not used                |
| 26      | 8       | DT     | O      |          |          | 0077      | Previous Treatment Date              | Not used                |
| 27      | 2       | IS     | O      |          |          | 0078      | Expected Discharge Disposition       | Not used                |
| 28      | 8       | DT     | O      |          |          | 0079      | Signature on File Date               | Not used                |
| 29      | 8       | DT     | O      |          |          | 0070      | First Similar Illness Date           | Not used                |
| 30      | 3       | IS     | O      |          |          | 0071      | Patient Charge Adjustment Code       | Not used                |
| 31      | 2       | IS     | O      |          |          | 0072      | Recurring Service Code               | Not used                |
| 32      | 1       | ID     | O      |          |          | 0073      | Billing Media Code                   | Not used                |
| 33      | 26      | TS     | O      |          |          | 0074      | Expected Surgery Date & Time         | Not used                |
| 34      | 2       | ID     | O      |          |          | 0075      | Military Partnership Code            | Not used                |
| 35      | 2       | ID     | O      |          |          | 0076      | Military Non-Availability Code       | Not used                |
| 36      | 1       | ID     | O      |          |          | 0077      | Newborn Baby Indicator               | Not used                |
| 37      | 1       | ID     | O      |          |          | 0078      | Baby Detained Indicator              | Not used                |

## 2.3.7AIP - Appointment Information - Personnel Resource Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 22%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O/C</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>ELEMENT NAME</th>
<th><strong>VISTA DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>00906</td>
<td>Set ID - AIP</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td></td>
<td>00763</td>
<td>Segment Action code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>XCN</td>
<td>C</td>
<td>Y</td>
<td></td>
<td>00913</td>
<td>Personnel Resource ID</td>
<td><p>Component</p>
<ol type="1">
<li><p>Provider IEN</p></li>
<li><p>Family name</p></li>
<li><p>Given name</p></li>
<li><p>Middle name or initial</p></li>
<li><p>Suffix</p></li>
</ol></td>
</tr>
<tr class="even">
<td>4</td>
<td>200</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>00907</td>
<td>Resource Role</td>
<td>Provider</td>
</tr>
<tr class="odd">
<td>5</td>
<td>200</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00899</td>
<td>Resource Group</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01202</td>
<td>Start Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>00891</td>
<td>Start Date/Time Offset</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>200</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>00892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used</td>
</tr>
</tbody>
</table>

## ## AIL Appointment Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><strong>LEN</strong></td>
<td><strong>DT</strong></td>
<td><strong>R/O/C</strong></td>
<td><strong>RP/#</strong></td>
<td><strong>TBL#</strong></td>
<td><strong>ITEM#</strong></td>
<td><strong>ELEMENT NAME</strong></td>
<td><strong>VISTA DESCRIPTION</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>00902</td>
<td>Set ID - AIL</td>
<td>Sequential Number</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>C</td>
<td></td>
<td></td>
<td>00763</td>
<td>Segment Action Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>3</td>
<td>90</td>
<td>PL</td>
<td>C</td>
<td></td>
<td></td>
<td>00903</td>
<td>Location Resource ID</td>
<td><p>Clinic Name</p>
<p>Components</p>
<blockquote>
<p>1.   Clinic IEN (20)</p>
<p>2.   Null</p>
<p>3.   Null</p>
<p>4.   Null</p>
<p>5.   Null</p>
<p>6.   Null</p>
<p>7.   Null</p>
<p>8.   Null</p>
<p>9.   Clinic name (60)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td>100</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>VA088</td>
<td>00904</td>
<td>Location Type</td>
<td><p>DSS ID</p>
<p>Components</p>
<ol type="1">
<li><p>DSS Clinic ID code (3)</p></li>
<li><p>Description (40)</p></li>
<li><p>'DSS Clinic ID" (13)</p></li>
</ol></td>
</tr>
<tr class="even">
<td>5</td>
<td>100</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA088</td>
<td>00905</td>
<td>Location Group</td>
<td><p>DSS credit stop</p>
<ol type="1">
<li><p>DSS credit stop code (3)</p></li>
<li><p>Description (40)</p></li>
<li><p>"DSS Credit Stop" (15)</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01202</td>
<td>Start Date/Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>00891</td>
<td>Start Date/Time Offset</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>8</td>
<td>200</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>00892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00893</td>
<td>Duration</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>10</td>
<td>200</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00894</td>
<td>Duration Units</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>11</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td></td>
<td></td>
<td>00895</td>
<td>Allow Substitution Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>12</td>
<td>200</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>00889</td>
<td>Filler Status Code</td>
<td>Not used</td>
</tr>
</tbody>
</table>

## SCH Schedule Activity Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><strong>LEN</strong></td>
<td><strong>DT</strong></td>
<td><strong>R/O/C</strong></td>
<td><strong>RP/#</strong></td>
<td><strong>TBL#</strong></td>
<td><strong>ITEM#</strong></td>
<td><strong>ELEMENT NAME</strong></td>
<td><strong>VISTA DESCRIPTION</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>75</td>
<td>EI</td>
<td>R</td>
<td></td>
<td></td>
<td>00860</td>
<td>Placer Appointment ID</td>
<td>Sequential Number</td>
</tr>
<tr class="odd">
<td>2</td>
<td>75</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>00861</td>
<td>Filler Appointment ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>3</td>
<td>5</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>00862</td>
<td>Occurrence Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>4</td>
<td>75</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>00863</td>
<td>Placer Group Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>5</td>
<td>200</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00864</td>
<td>Schedule ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>6</td>
<td>3</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA087</td>
<td>00883</td>
<td>Event Reason</td>
<td><p>Component</p>
<blockquote>
<p>Scheduling Event Reason codes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td>1</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0276</td>
<td>00866</td>
<td>Appointment Reason</td>
<td>Appointment Reason</td>
</tr>
<tr class="odd">
<td>8</td>
<td>3</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0277</td>
<td>00867</td>
<td>Appointment Type</td>
<td>Appointment Type Codes</td>
</tr>
<tr class="even">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00868</td>
<td>Appointment Duration</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>10</td>
<td>200</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01304</td>
<td>Appointment Duration Units</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>11</td>
<td>200</td>
<td>TQ</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00884</td>
<td>Appointment Timing Quantity</td>
<td><p>In the following order:</p>
<p>Date Appt Created</p>
<p>Desired Date</p>
<p>Appt Date (time)</p>
<p>Checkout Date (time)</p>
<p>Cancellation Date (time)</p>
<p>Auto-rebook Date(time)</p>
<p>Resched Date(time)</p></td>
</tr>
<tr class="odd">
<td>12</td>
<td>48</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>00874</td>
<td>Placer Contact Person</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>13</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>00875</td>
<td>Placer Contact Phone Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>14</td>
<td>106</td>
<td>XAD</td>
<td>O</td>
<td></td>
<td></td>
<td>00876</td>
<td>Placer Contact Address</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>15</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>00877</td>
<td>Placer Contact Location</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>16</td>
<td>38</td>
<td>XCN</td>
<td>R</td>
<td></td>
<td></td>
<td>00885</td>
<td>Filler Contact Person</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>17</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>00886</td>
<td>Filler Contact Phone Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>18</td>
<td>106</td>
<td>XAD</td>
<td>O</td>
<td></td>
<td></td>
<td>00887</td>
<td>Filler Contact Address</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>19</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>00888</td>
<td>Filler Contact Location</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>20</td>
<td>48</td>
<td>XCN</td>
<td>R</td>
<td></td>
<td></td>
<td>00878</td>
<td>Entered by Person</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>21</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>00879</td>
<td>Entered by Phone Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>22</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>00880</td>
<td>Entered by Location</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>23</td>
<td>75</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>00881</td>
<td>Parent Placer Appointment ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>24</td>
<td>75</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>00882</td>
<td>Parent Filler Appointment ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>25</td>
<td>200</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0278</td>
<td>00889</td>
<td>Filler Status Code</td>
<td>Appointment Status</td>
</tr>
</tbody>
</table>

## ZCL - VA-Specific Outpatient Classification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#  | VISTA ELEMENT NAME             |
|-----|-----|-----|-----|------|-------|--------------------------------|
| 1   | 4   | SI  | R   |      |       | SET ID                         |
| 2   | 2   | ID  | R   |      | SD008 | Outpatient Classification Type |
| 3   | 50  | ST  |     |      |       | Value                          |

## ZEN - VA-Specific Enrollment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | VISTA ELEMENT NAME  |
|-----|-----|-----|-----|------|--------|---------------------|
| 1   | 4   | SI  | R   |      |        | SET ID              |
| 2   | 8   | DT  |     |      |        | Not used            |
| 3   | 1   | ID  |     |      |        | Not used            |
| 4   | 1   | ID  |     |      |        | Not used            |
| 5   | 1   | ID  |     |      |        | Not used            |
| 6   | 60  | TX  |     |      |        | Not used            |
| 7   | 7   | ID  |     |      |        | Not used            |
| 8   | 7   | ID  |     |      |        | Not used            |
| 9   | 1   | ID  |     |      | VA0021 | ENROLLMENT PRIORITY |
| 10  | 8   | DT  |     |      |        | not used            |

## ZSP - VA-Specific Service Period Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | VISTA ELEMENT NAME           |
|-----|-----|-----|-----|------|------|------------------------------|
| 1   | 4   | SI  | R   |      |      | SET ID                       |
| 2   | 1   | ID  | R   |      | VA01 | Service Connected?           |
| 3   | 3   | NM  |     |      |      | Service Connected Percentage |
| 4   | 2   | ID  |     |      |      | NOT USED                     |
| 5   | 1   | ID  |     |      |      | NOT USED                     |

## SUPPORTED AND USER-DEFINED HL7 TABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table 0003 - Event type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                            |
|-------|----------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                |
| S12   | SIU/ACK - Notification of new appointment booking                          |
| S14   | SIU/ACK - Notification of appointment modification                         |
| S15   | SIU/ACK - Notification of appointment cancellation                         |
| S26   | SIU/ACK Notification that patient did not show up for schedule appointment |

## Table 0004 – Patient Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| I     | INPATIENT   |
| O     | OUTPATIENT  |
| U     | UNKNOWN     |

## Table 0008 - Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                           |
|-------|-------------------------------------------|
| VALUE | DESCRIPTION                               |
| AA    | APPLICATION ACKNOWLEDGMENT: ACCEPT        |
| AE    | APPLICATION ACKNOWLEDGMENT: ERROR         |
| AR    | APPLICATION ACKNOWLEDGMENT: REJECT        |
| MR    | APPLICATION ACKNOWLEDGMENT: MANUAL REJECT |
| CA    | ACCEPT ACKNOWLEDGMENT: COMMIT ACCEPT      |
| CE    | ACCEPT ACKNOWLEDGMENT: COMMIT ERROR       |
| CR    | ACCEPT ACKNOWLEDGMENT: COMMIT REJECT      |

The patch is prepared for 'AR' – THE WHOLE BATCH REJECTION but

It has not been expected to receive that code from the AAC at this time.

'MR' may be used instead.

## Table 0076 - Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                        |
|-------|------------------------|
| VALUE | DESCRIPTION            |
| SIU   | SIU MESSAGE            |
| ACK   | GENERAL ACKNOWLEDGMENT |

## Table 0216 - Patient Status Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|           |                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                                                   |
| NTF       | Patient did not have a prior appointment at this Facility in the past 24 months; New to parent and substation.    |
| SHB       | Patient did have a prior appointment at this parent and substation in the past 24 months; Registered here before. |
| OPN       | Patient did not have a prior appointment at this substation but was registered with parent station.               |

The patient status code indicates if a patient is new to the facility or not. Both the parent station and the substations are evaluated as the facility. The parent station is evaluated with the primary DSS ID only; the substation is evaluated with both DSS ID stop code and the DSS credit stop code. The patient is considered new to the facility if he/she did not have another scheduled appointment in the same facility during the previous 24 months. The facility's station number is determined from the Division (field \#3.5) of the clinic's Hospital Location file \#44 entry. The division is retrieved from the Medical Center Division file \#40.8 from which the Institution File Pointer field (#.07) is used to look up the Institution file \#4 entry where the Station Number field (#99) is stored.

## Table 0276 - Appointment Reason Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                 |
|-------|-------------------------------------------------|
| VALUE | DESCRIPTION                                     |
| 1     | Next Ava. Appt. Indicated by User               |
| 2     | Next Ava. Appt. Indicated by Calculation        |
| 3     | Next Ava. Appt. Indicated by User & Calculation |
| 4     | Not Next Available with AutoRebook              |
| 5     | Not Next Available No AutoRebook                |
| 6     | Null (All others)                               |

## Table 0277 - Appointment Type Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                  |
|-------|------------------|
| VALUE | DESCRIPTION      |
| AR    | Action required  |
| NAT   | No action taken  |
| F     | Future           |
| NC    | Non count        |
| NCF   | Non count future |
| ABK   | Auto re-book     |
| O     | Outpatient       |
| I     | Inpatient        |
| RS    | Re-schedule      |

## Table 0278 Filler Status Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| P     | Pending     |
| F     | Final       |

## Table VA01 - Yes/No

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| 0     | NO          |
| 1     | YES         |
| N     | NO          |
| Y     | YES         |
| U     | UNKNOWN     |

## Table SD008 - Outpatient Classification Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                            |
|-------|----------------------------|
| VALUE | DESCRIPTION                |
| 1     | AGENT ORANGE               |
| 2     | IONIZING RADIATION         |
| 3     | SERVICE CONNECTED          |
| 4     | ENVIRONMENTAL CONTAMINANTS |
| 5     | MILITARY SEXUAL TRAUMA     |
| 6     | HEAD AND/OR NECK CANCER    |

## Table SD009 - Purpose of Visit & Appointment Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|           |                      |                        |
|-----------|----------------------|------------------------|
| VALUE | PURPOSE OF VISIT | APPOINTMENT TYPE   |
| 0101      | C&P                  | COMPENSATION & PENSION |
| 0102      | C&P                  | CLASS II DENTAL        |
| 0103      | C&P                  | ORGAN DONORS           |
| 0104      | C&P                  | EMPLOYEE               |
| 0105      | C&P                  | PRIMA FACIA            |
| 0106      | C&P                  | RESEARCH               |
| 0107      | C&P                  | COLLATERAL OF VET.     |
| 0108      | C&P                  | SHARING AGREEMENT      |
| 0109      | C&P                  | REGULAR                |
| 0111      | C&P                  | SERVICE CONNECTED      |
| 0201      | 10-10                | COMPENSATION & PENSION |
| 0202      | 10-10                | CLASS II DENTAL        |
| 0203      | 10-10                | ORGAN DONORS           |
| 0204      | 10-10                | EMPLOYEE               |
| 0205      | 10-10                | PRIMA FACIA            |
| 0206      | 10-10                | RESEARCH               |
| 0207      | 10-10                | COLLATERAL OF VET.     |
| 0208      | 10-10                | SHARING AGREEMENT      |
| 0209      | 10-10                | REGULAR                |
| 0211      | 10-10                | SERVICE CONNECTED      |
| 0301      | SCHEDULED VISIT      | COMPENSATION & PENSION |
| 0302      | SCHEDULED VISIT      | CLASS II DENTAL        |
| 0303      | SCHEDULED VISIT      | ORGAN DONORS           |
| 0304      | SCHEDULED VISIT      | EMPLOYEE               |
| 0305      | SCHEDULED VISIT      | PRIMA FACIA            |
| 0306      | SCHEDULED VISIT      | RESEARCH               |
| 0307      | SCHEDULED VISIT      | COLLATERAL OF VET.     |
| 0308      | SCHEDULED VISIT      | SHARING AGREEMENT      |
| 0309      | SCHEDULED VISIT      | REGULAR                |
| 0311      | SCHEDULED VISIT      | SERVICE CONNECTED      |
| 0401      | UNSCHED. VISIT       | COMPENSATION & PENSION |
| 0402      | UNSCHED. VISIT       | CLASS II DENTAL        |
| 0403      | UNSCHED. VISIT       | ORGAN DONORS           |
| 0404      | UNSCHED. VISIT       | EMPLOYEE               |
| 0405      | UNSCHED. VISIT       | PRIMA FACIA            |
| 0406      | UNSCHED. VISIT       | RESEARCH               |
| 0407      | UNSCHED. VISIT       | COLLATERAL OF VET.     |
| 0408      | UNSCHED. VISIT       | SHARING AGREEMENT      |
| 0409      | UNSCHED. VISIT       | REGULAR                |
| 0411      | UNSCHED. VISIT       | SERVICE CONNECTED      |

Value denotes a combination of Purpose of Visit & Appointment Type, which is known as "Admission Type" for the purposes of data transmission. This table is used in processing the ACRP HL7 transmission.

*<u>Note:</u><u>It has been determined that PV1 segment can contain the 'empty' value for sequence P1.4 and it has to be treated as acceptable. That might happen when a new appointment is scheduled in place of a previously canceled appointment, and if the original appointment has been already transmitted by PAIT.</u>*

## Table VA0021 – Enrollment Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |             |
|-------|-------------|
| VALUE | DESCRIPTION |
| 1     | Priority 1  |
| 2     | Priority 2  |
| 3     | Priority 3  |
| 4     | Priority 4  |
| 5     | Priority 5  |
| 6     | Priority 6  |
| 7     | Priority 7  |
| 8     | Priority 8  |

## Table VA087 - Scheduling Event Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                        |
|-------|------------------------|
| VALUE | DESCRIPTION            |
| CI    | Check-in               |
| CO    | Check-out              |
| NS    | No Show                |
| CC    | Cancel by clinic       |
| CP    | Cancel by patient      |
| COE   | Check-out by encounter |
| NM    | No Match               |
| CT    | Cancelled Terminated   |

## Table AAC001 - Error Code Set 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                                                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                                                                                                                                                                        |
| 100   | PATIENT DFN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                           |
| 150   | CLINIC IEN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                            |
| 200   | BHS STATION NUMBER AND STA3N ARE NOT EQUAL                                                                                                                                                                                         |
| 250   | INVALID OR MISSING BHS STATION NUMBER                                                                                                                                                                                              |
| 300   | INVALID OR MISSING STA3N                                                                                                                                                                                                           |
| 350   | HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING.                                                                                                                                                                                    |
| 400   | DOB IS MISSING OR INVALID                                                                                                                                                                                                          |
| 450   | CREATE DATE OR APPT DATE IS MISSING                                                                                                                                                                                                |
| 500   | CREATION DATE IS BEFORE SEPTEMBER 1, 2002                                                                                                                                                                                          |
| 600   | RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT - Rescheduled date requires SCH.8 Appt type = 'RS' and vice versa                                                                                                              |
| 650   | CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT - Check out date requires either SCH.6 Event reason = 'CO' or 'COE'                                                                                                           |
| 700   | CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT - Cancellation date requires SCH.6 Event reason = 'CC' or 'CP' or 'NS'                                                                                                     |
| 750   | EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT - All SCH.6 Event reason codes, except 'CI' require SCH.25 Filler status to be 'F' Final and accordingly only 'CI' and NULL should have SCH.25 Filler status to be 'P' Pending |
| 800   | FILLER STATUS IS MISSING OR IS INVALID                                                                                                                                                                                             |
| 850   | ADMIT TYPE IS INVALID (table SD009)                                                                                                                                                                                                |
| R     | WHOLE BATCH REJECTED                                                                                                                                                                                                               |

R – whole batch reject may be currently generated only by manual batch rejection.

## ## Table VA088 – DSS ID and DSS Credit Stop 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please note that this table is updated yearly and the current set up should be evaluated.

|            |                                   |                  |             |               |                   |
|------------|-----------------------------------|------------------|-------------|---------------|-------------------|
| VALUE  | DESCRIPTION                   | Allow Either | Primary | Secondary | Inactive Date |
| 101        | EMERGENCY UNIT                    |                  |             | S             |                   |
| 102        | ADMITTING/SCREENING               | E                |             |               |                   |
| 103        | TELEPHONE TRIAGE                  |                  | P           |               |                   |
| 104        | PULMONARY FUNCTION                | E                |             |               |                   |
| 105        | X-RAY                             | E                |             |               |                   |
| 106        | EEG                               | E                |             |               |                   |
| 107        | EKG                               |                  | P           |               |                   |
| 108        | LABORATORY                        | E                |             |               |                   |
| 109        | NUCLEAR MEDICINE                  | E                |             |               |                   |
| 110        | CARDIOVASCULAR NUCLEAR MED        | E                |             |               | OCT 1,1998        |
| 111        | ONCOLOGICAL NUCLEAR MED           | E                |             |               | OCT 1,1998        |
| 112        | INFECTIOUS DISEASE NUCLEAR MED    | E                |             |               | OCT 1,1998        |
| 113        | RADIONUCLIDE TREATMENT            | E                |             |               | OCT 1,1998        |
| 114        | SING PHOTON EMISS TOMOGRAPHY      | E                |             |               | OCT 1,1998        |
| 115        | ULTRASOUND                        | E                |             |               |                   |
| 116        | RESPIRATORY THERAPY               | E                |             |               |                   |
| 117        | NURSING (2ND ONLY)                |                  |             | S             |                   |
| 118        | HOME TREATMENT SERVICES           |                  | P           |               |                   |
| 119        | COMM NURSING HOME FOLLOW-UP       | E                |             |               |                   |
| 120        | HEALTH SCREENING                  | E                |             |               |                   |
| 121        | RESIDENTIAL CARE (NON-MH)         | E                |             |               |                   |
| 122        | PUBLIC HEALTH NURSING             | E                |             |               |                   |
| 123        | NUTRITION/DIETETICS-INDIVIDUAL    | E                |             |               |                   |
| 124        | NUTRITION/DIETETICS-GROUP         | E                |             |               |                   |
| 125        | SOCIAL WORK SERVICE               | E                |             |               |                   |
| 126        | EVOKED POTENTIAL                  | E                |             |               |                   |
| 127        | TOPOGRAPHICAL BRAIN MAPPING       | E                |             |               |                   |
| 128        | PROLONGED VIDEO-EEG MONITORING    | E                |             |               |                   |
| 129        | HYPERTENSION SCREENING            | E                |             |               | OCT 1,1991        |
| 130        | CHOLESTEROL SCREENING             | E                |             |               | OCT 1,1991        |
| 131        | BREAST CANCER SCREENING           | E                |             |               | OCT 1,1991        |
| 132        | MAMMOGRAM                         | E                |             |               | OCT 1,1991        |
| 133        | CERVICAL CANCER SCREENING         | E                |             |               | OCT 1,1991        |
| 134        | PAP TEST                          | E                |             |               | OCT 1,1991        |
| 135        | COLORECTAL CANCER SCREENING       | E                |             |               | OCT 1,1991        |
| 136        | FOBT - GUIAC SCREENING            | E                |             |               | OCT 1,1991        |
| 137        | ALCOHOL COUNSELING - MED CARE     | E                |             |               | OCT 1,1991        |
| 138        | SMOKING CESSATION                 | E                |             |               | OCT 1,1991        |
| 139        | WEIGHT CONTROL                    | E                |             |               | OCT 1,1991        |
| 140        | PHYS FITNESS/EXERCISE COUNSEL     | E                |             |               | OCT 1,1991        |
| 141        | VET IMMUNIZATION                  | E                |             |               | OCT 1,1991        |
| 142        | COLORECTAL CA SCREEN DIG EXAM     | E                |             |               | OCT 1,1991        |
| 143        | PERSIAN GULF READJUST COUNSEL     | E                |             |               | JAN 1,1988        |
| 144        | RADIONUCLIDE THERAPY              | E                |             |               |                   |
| 145        | PHARM/PHYSIO NMP STUDIES          | E                |             |               |                   |
| 146        | PET                               | E                |             |               |                   |
| 147        | TELEPHONE/ANCILLARY               |                  | P           |               |                   |
| 148        | TELEPHONE/DIAGNOSTIC              |                  | P           |               |                   |
| 149        | RADIATION THERAPY TREATMENT       | E                |             |               |                   |
| 150        | COMPUTERIZED TOMOGRAPHY (CT)      | E                |             |               |                   |
| 151        | MAGNETIC RESONANCE IMAGING/MRI    | E                |             |               |                   |
| 152        | ANGIOGRAM CATHETERIZATION         | E                |             |               |                   |
| 153        | INTERVENTIONAL RADIOGRAPHY        | E                |             |               |                   |
| 154        | MEG (MAGNETOENCEPHALOGRAPHY)      | E                |             |               |                   |
| 155        | INFO ASSISTS TECHNOLOGY           | E                |             |               |                   |
| 160        | CLINICAL PHARMACY                 |                  |             | S             |                   |
| 161        | TRANSITIONAL PHARMACY             |                  | P           |               |                   |
| 163        | CHAPLAIN-CLINICAL SVCS-INDIV      | E                |             |               | OCT 1,2002        |
| 164        | CHAPLAIN-CLINICAL SVCS-GROUP      | E                |             |               | OCT 1,2002        |
| 165        | BEREAVEMENT COUNSELING            | E                |             |               |                   |
| 166        | CHAPLAIN SERVICE - INDIVIDUAL     | E                |             |               |                   |
| 167        | CHAPLAIN SERVICE - GROUP          | E                |             |               |                   |
| 168        | CHAPLAIN SERVICE - COLLATERAL     | E                |             |               |                   |
| 169        | TELEPHONE/CHAPLAIN                |                  | P           |               |                   |
| 170        | HBPC - PHYSICIAN                  |                  | P           |               |                   |
| 171        | HBPC - RN/RNP/PA                  |                  | P           |               |                   |
| 172        | HBPC - NURSE EXTENDER             |                  | P           |               |                   |
| 173        | HBPC - SOCIAL WORKER              |                  | P           |               |                   |
| 174        | HBPC - THERAPIST                  |                  | P           |               |                   |
| 175        | HBPC - DIETITIAN                  |                  | P           |               |                   |
| 176        | HBPC - CLINICAL PHARMACIST        |                  | P           |               |                   |
| 177        | HBPC - OTHER                      |                  | P           |               |                   |
| 178        | HBPC/TELEPHONE                    |                  | P           |               |                   |
| 179        | HOME TELEVIDEO CARE               |                  |             | S             |                   |
| 180        | DENTAL                            | E                |             |               |                   |
| 181        | TELEPHONE/DENTAL                  |                  | P           |               |                   |
| 185        | PHYS EXTND NP (NRS PRCNR) 2ND     |                  |             | S             |                   |
| 186        | PHYS EXTND PA (PHYS ASST) 2ND     |                  |             | S             |                   |
| 187        | PHYS EXTND CNS (CLN RN SPC)2ND    |                  |             | S             |                   |
| 190        | ADULT DAY HEALTH CARE             | E                |             |               |                   |
| 201        | PHYSICAL MED & REHAB SVC          | E                |             |               |                   |
| 202        | RECREATION THERAPY SERVICE        | E                |             |               |                   |
| 203        | AUDIOLOGY                         | E                |             |               |                   |
| 204        | SPEECH PATHOLOGY                  | E                |             |               |                   |
| 205        | PHYSICAL THERAPY                  | E                |             |               |                   |
| 206        | OCCUPATIONAL THERAPY              | E                |             |               |                   |
| 207        | PM&RS INCENTIVE THERAPY           | E                |             |               |                   |
| 208        | PM&RS COMPENSATED WORK THERAPY    | E                |             |               |                   |
| 209        | VIST COORDINATOR                  | E                |             |               |                   |
| 210        | SPINAL CORD INJURY                | E                |             |               |                   |
| 211        | AMPUTATION FOLLOW-UP CLINIC       | E                |             |               |                   |
| 212        | EMG - ELECTROMYOGRAM              | E                |             |               |                   |
| 213        | PM&RS VOCATIONAL ASSISTANCE       | E                |             |               |                   |
| 214        | KINESIOTHERAPY                    | E                |             |               |                   |
| 215        | SCI HOME CARE PROGRAM             | E                |             |               |                   |
| 216        | TELEPHONE/REHAB AND SUPPORT       |                  | P           |               |                   |
| 217        | BROS (BLIND REHAB O/P SPEC)       | E                |             |               |                   |
| 218        | CAT BLIND REHAB                   | E                |             |               |                   |
| 219        | TBI (TRAUMATIC BRAIN INJURY)      | E                |             |               |                   |
| 220        | VISOR (VISUAL IMPAIRMENT OUTPA    | E                |             |               |                   |
| 290        | OBSERVATION MEDICINE              |                  | P           |               |                   |
| 291        | OBSERVATION SURGERY               |                  | P           |               |                   |
| 292        | OBSERVATION PSYCHIATRY            |                  | P           |               |                   |
| 293        | OBSERVATION NEUROLOGY             |                  | P           |               |                   |
| 294        | OBSERVATION BLIND REHAB           |                  | P           |               |                   |
| 295        | OBSERVATION SPINAL CORD           |                  | P           |               |                   |
| 296        | OBSERVATION REHABILITATION        |                  | P           |               |                   |
| 301        | GENERAL INTERNAL MEDICINE         | E                |             |               |                   |
| 302        | ALLERGY IMMUNOLOGY                | E                |             |               |                   |
| 303        | CARDIOLOGY                        | E                |             |               |                   |
| 304        | DERMATOLOGY                       | E                |             |               |                   |
| 305        | ENDO./METAB (EXCEPT DIABETES)     | E                |             |               |                   |
| 306        | DIABETES                          | E                |             |               |                   |
| 307        | GASTROENTEROLOGY                  | E                |             |               |                   |
| 308        | HEMATOLOGY                        | E                |             |               |                   |
| 309        | HYPERTENSION                      | E                |             |               |                   |
| 310        | INFECTIOUS DISEASE                | E                |             |               |                   |
| 311        | PACEMAKER                         | E                |             |               |                   |
| 312        | PULMONARY/CHEST                   | E                |             |               |                   |
| 313        | RENAL/NEPHROL(EXCEPT DIALYSIS)    | E                |             |               |                   |
| 314        | RHEUMATOLOGY/ARTHRITIS            | E                |             |               |                   |
| 315        | NEUROLOGY                         | E                |             |               |                   |
| 316        | ONCOLOGY/TUMOR                    | E                |             |               |                   |
| 317        | COUMADIN CLINIC                   | E                |             |               |                   |
| 318        | GERIATRIC CLINIC                  | E                |             |               |                   |
| 319        | GERIATRIC EVAL. & MGMT. (GEM)     | E                |             |               |                   |
| 320        | ALZHEIMER'S/DEMENTIA CLINIC       | E                |             |               |                   |
| 321        | GI ENDOSCOPY                      | E                |             |               |                   |
| 322        | WOMEN'S CLINIC                    | E                |             |               |                   |
| 323        | PRIMARY CARE/MEDICINE             | E                |             |               |                   |
| 324        | TELEPHONE/MEDICINE                |                  | P           |               |                   |
| 325        | TELEPHONE/NEUROLOGY               |                  | P           |               |                   |
| 326        | TELEPHONE/GERIATRICS              |                  | P           |               |                   |
| 327        | MED MD PERFORM INVASVE OR PROC    |                  | P           |               |                   |
| 328        | MEDICAL/SURGICAL DAY UNIT MSDU    | E                |             |               |                   |
| 329        | MEDICAL PROCEDURE UNIT            | E                |             |               |                   |
| 330        | CHEMOTHERAPY PROC. UNIT-MED.      | E                |             |               |                   |
| 331        | PRE-BED CARE MD (MEDICINE)        | E                |             |               |                   |
| 332        | PRE-BED CARE RN (MEDICINE)        | E                |             |               |                   |
| 333        | CARDIAC CATHETERIZATION           | E                |             |               |                   |
| 334        | CARDIAC STRESS TEST/ETT           | E                |             |               |                   |
| 335        | PADRECC PARKINSON'SDISEASERECC    | E                |             |               |                   |
| 350        | GERIATRIC PRIMARY CARE            | E                |             |               |                   |
| 351        | ADVNCD ILLNESS COOR CARE(AICC)    | E                |             |               |                   |
| 370        | LTC SCREENING (2ND ONLY)          |                  |             | S             |                   |
| 401        | GENERAL SURGERY                   | E                |             |               |                   |
| 402        | CARDIAC SURGERY                   | E                |             |               |                   |
| 403        | ENT                               | E                |             |               |                   |
| 404        | GYNECOLOGY                        | E                |             |               |                   |
| 405        | HAND SURGERY                      | E                |             |               |                   |
| 406        | NEUROSURGERY                      | E                |             |               |                   |
| 407        | OPHTHALMOLOGY                     | E                |             |               |                   |
| 408        | OPTOMETRY                         | E                |             |               |                   |
| 409        | ORTHOPEDICS                       | E                |             |               |                   |
| 410        | PLASTIC SURGERY                   | E                |             |               |                   |
| 411        | PODIATRY                          | E                |             |               |                   |
| 412        | PROCTOLOGY                        | E                |             |               |                   |
| 413        | THORACIC SURGERY                  | E                |             |               |                   |
| 414        | UROLOGY                           | E                |             |               |                   |
| 415        | VASCULAR SURGERY                  | E                |             |               |                   |
| 416        | AMB SURGERY EVAL BY NON-MD        | E                |             |               |                   |
| 417        | PROSTHETICS/ORTHOTICS             | E                |             |               |                   |
| 418        | AMPUTATION CLINIC                 | E                |             |               |                   |
| 419        | ANESTHESIA PRE/POST-OP CONSULT    | E                |             |               |                   |
| 420        | PAIN CLINIC                       | E                |             |               |                   |
| 421        | VASCULAR LABORATORY               | E                |             |               |                   |
| 422        | CAST CLINIC                       | E                |             |               |                   |
| 423        | PROSTHETIC SUPPLY DISPENSED       | E                |             |               |                   |
| 424        | TELEPHONE/SURGERY                 |                  | P           |               |                   |
| 425        | TELEPHONE/PROSTHETICS/ORTHOTIC    |                  | P           |               |                   |
| 426        | WOMEN SURGERY                     | E                |             |               |                   |
| 427        | PRIMARY CARE/SURGERY              | E                |             |               | OCT 1,1997        |
| 428        | TELEPHONE/OPTOMETRY               |                  | P           |               |                   |
| 429        | OUTPATIENT CARE IN OR             |                  | P           |               |                   |
| 430        | CYSTO ROOM UNIT FOR OUTPATIENT    | E                |             |               |                   |
| 431        | CHEMOTHERAPY PROC. UNIT-SURG.     | E                |             |               |                   |
| 432        | PRE-BED CARE MD (SURGERY)         | E                |             |               |                   |
| 433        | PRE-BED CARE RN (SURGERY)         | E                |             |               |                   |
| 435        | SURGICAL PROCEDURE UNIT           | E                |             |               |                   |
| 436        | CHIROPRACTIC CARE IN MED CTR      | E                |             |               |                   |
| 449        | FITTING & ADJSTMNTS 2ND ONLY      |                  |             | S             |                   |
| 450        | COMPENSATION & PENSION            |                  |             | S             |                   |
| 451 to 456 | Local use                         |                  |             | S             |                   |
| 457        | TRANSPLANT                        |                  |             | S             |                   |
| 458 to 473 | Local use (delete 473 TBPPD SHOT) |                  |             | S             |                   |
| 474        | RESEARCH                          |                  |             | S             |                   |
| 475 to 479 | Local use                         |                  |             | S             |                   |
| 480        | COMPREHENSIVE FUNDOSCOPY          |                  |             | S             |                   |
| 481        | BRONCHOSCOPY                      |                  |             | S             |                   |
| 482 to 485 | Local use                         |                  |             | S             |                   |
| 501        | HOMELESS MENTALLY ILL OUTREACH    | E                |             |               | OCT 1,1994        |
| 502        | MENTAL HEALTH CLINIC - IND        | E                |             |               |                   |
| 503        | MH RESIDENTIAL CARE IND           | E                |             |               |                   |
| 504        | IPCC MEDICAL CENTER VISIT         | E                |             |               | APR 1,1997        |
| 505        | DAY TREATMENT-INDIVIDUAL          | E                |             |               |                   |
| 506        | DAY HOSPITAL-INDIVIDUAL           | E                |             |               |                   |
| 507        | DRUG DEPENDENCE-INDIVIDUAL        | E                |             |               | APR 1,1997        |
| 508        | ALCOHOL TREATMENT-INDIVIDUAL      | E                |             |               | APR 1,1997        |
| 509        | PSYCHIATRY-MD INDIVIDUAL          | E                |             |               |                   |
| 510        | PSYCHOLOGY-INDIVIDUAL             | E                |             |               |                   |
| 511        | NEUROBEHAVIORAL-INDIVIDUAL        | E                |             |               | OCT 1,1993        |
| 512        | PSYCHIATRY CONSULTATION           | E                |             |               |                   |
| 513        | SUBSTANCE ABUSE - INDIVIDUAL      | E                |             |               |                   |
| 514        | SUBSTANCE ABUSE - HOME VISIT      | E                |             |               |                   |
| 515        | CWT/TR-HCMI                       | E                |             |               | APR 1,1997        |
| 516        | PTSD - GROUP                      | E                |             |               |                   |
| 516        | PTSD - GROUP                      | E                |             |               |                   |
| 517        | CWT SUBSTANCE ABUSE               | E                |             |               | APR 1,1997        |
| 518        | CWT/TR-SUBSTANCE ABUSE            | E                |             |               | APR 1,1997        |
| 519        | SUBST USE DISORDER/PTSD TEAMS     | E                |             |               |                   |
| 520        | LONG-TERM ENHANCEMENT, INDIVID    | E                |             |               |                   |
| 521        | LONG-TERM ENHANCEMENT, GROUP      | E                |             |               |                   |
| 522        | HUD/VASH                          | E                |             |               |                   |
| 523        | OPIOID SUBSTITUTION               | E                |             |               |                   |
| 524        | ACTIVE DUTY SEX TRAUMA            | E                |             |               |                   |
| 525        | WOMEN'S STRESS DISORDER TEAMS     | E                |             |               |                   |
| 526        | TELEPHONE/SPECIAL PSYCHIATRY      | E                |             |               | APR 1,1997        |
| 527        | TELEPHONE/GENERAL PSYCHIATRY      |                  | P           |               |                   |
| 528        | TELE/HOMELESS MENTALLY ILL        |                  | P           |               |                   |
| 529        | HCHV/HMI                          |                  | P           |               |                   |
| 530        | TELEPHONE/HUD-VASH                |                  | P           |               |                   |
| 531        | MH PRIMARY CARE TEAM - IND        | E                |             |               |                   |
| 532        | PSYCHOSOCIAL REHAB - IND          | E                |             |               |                   |
| 533        | MH INTERVNTION BIOMED CARE IND    | E                |             |               |                   |
| 535        | MH VOCATIONAL ASSISTANCE - IND    | E                |             |               |                   |
| 536        | TELEPHONE/MH VOC ASSISTANCE       |                  | P           |               |                   |
| 537        | TELEPHONE/PSYCHOSOCIAL REHAB      |                  | P           |               |                   |
| 538        | PSYCHOLOGICAL TESTING             | E                |             |               |                   |
| 540        | PCT POST-TRAUMATIC STRESS-IND     |                  | P           |               |                   |
| 541        | PTSD POST-TRAUMATIC STRESS        | E                |             |               | JAN 1,1991        |
| 542        | TELEPHONE/PTSD                    |                  | P           |               |                   |
| 543        | TELEPHONE/ALCOHOL DEPENDENCE      | E                |             |               | APR 1,1997        |
| 544        | TELEPHONE/DRUG DEPENDENCE         | E                |             |               | APR 1,1997        |
| 545        | TELEPHONE/SUBSTANCE ABUSE         |                  | P           |               |                   |
| 546        | TELEPHONE/MHICM                   |                  | P           |               |                   |
| 547        | INTENSIVE SUBSTANCE ABUSE TRMT    | E                |             |               |                   |
| 550        | MENTAL HEALTH CLINIC-GROUP        | E                |             |               |                   |
| 551        | IPCC COMM CLN/DAY PROGRAM VST     | E                |             |               | APR 1,1997        |
| 552        | MENTAL HLT INT CASE MGT(MHICM)    |                  | P           |               |                   |
| 553        | DAY TREATMENT-GROUP               | E                |             |               |                   |
| 554        | DAY HOSPITAL-GROUP                | E                |             |               |                   |
| 555        | DRUG DEPENDENCE-GROUP             | E                |             |               | APR 1,1997        |
| 555        | DRUG DEPENDENCE-GROUP             | E                |             |               | APR 1,1997        |
| 556        | ALCOHOL TREATMENT-GROUP           | E                |             |               | APR 1,1997        |
| 557        | PSYCHIATRY - MD GROUP             | E                |             |               |                   |
| 558        | PSYCHOLOGY-GROUP                  | E                |             |               |                   |
| 559        | PSYCHOSOCIAL REHAB - GROUP        | E                |             |               |                   |
| 560        | SUBSTANCE ABUSE - GROUP           | E                |             |               |                   |
| 561        | PCT-POST TRAUMATIC STRESS-GRP     |                  | P           |               |                   |
| 562        | PTSD - INDIVIDUAL                 | E                |             |               |                   |
| 562        | PTSD - INDIVIDUAL                 | E                |             |               |                   |
| 563        | MH PRIMARY CARE TEAM - GROUP      | E                |             |               |                   |
| 564        | MH TEAM CASE MANAGEMENT           | E                |             |               |                   |
| 565        | MH MEDICAL CARE ONLY-GROUP        | E                |             |               |                   |
| 566        | MH RISK-FACTOR-REDUCTION ED GR    | E                |             |               |                   |
| 567        | MHICM GRP MTLHLTH INTSV CS MGT    |                  | P           |               |                   |
| 571        | READJUSTMENT COUNSELING-INDIV     | E                |             |               | JAN 31,1994       |
| 572        | READJUSTMENT COUNSELING-GROUP     | E                |             |               | JAN 31,1994       |
| 573        | MH INCENTIVE THERAPY - GROUP      | E                |             |               |                   |
| 574        | MH COMP WORK THERAPY (CWT) GRP    | E                |             |               |                   |
| 575        | MH VOCATIONAL ASSISTANCE-GRP      | E                |             |               |                   |
| 576        | PSYCHOGERIATRIC - INDIVIDUAL      | E                |             |               |                   |
| 577        | PSYCHOGERIATRIC CLINIC - GROUP    | E                |             |               |                   |
| 578        | PSYCHOGERIATRIC DAY PROGRAM       | E                |             |               |                   |
| 579        | TELEPHONE/PSYCHOGERIATRICS        |                  | P           |               |                   |
| 580        | PTSD DAY HOSPITAL                 | E                |             |               |                   |
| 581        | PTSD DAY TREATMENT                | E                |             |               |                   |
| 589        | NON-ACTIVE DUTY SEX TRAUMA        | E                |             |               |                   |
| 590        | COMM OUTREACH HOMELESS VETS       | E                |             |               |                   |
| 601        | ACUTE HEMODIAL TREATMENT          | E                |             |               | OCT 1,1990        |
| 602        | CHRON ASSISTED HEMODIAL TREAT     |                  | P           |               |                   |
| 603        | LIM SELF CARE HEMODIAL TREAT      |                  | P           |               |                   |
| 604        | HOME/SELF HEMODIAL TRAIN TREAT    |                  | P           |               |                   |
| 605        | ACUTE PERITONEAL DIAL TREAT       |                  | P           |               | OCT 1,1990        |
| 606        | CHRON ASSISTED PERIT DIALYSIS     |                  | P           |               |                   |
| 607        | LIM SELF CARE PERIT DIALYSIS      |                  | P           |               |                   |
| 608        | HOME/SELF PERIT DIALYSIS TRAIN    |                  | P           |               |                   |
| 610        | CONTRACT DIALYSIS                 |                  | P           |               |                   |
| 611        | TELEPHONE/DIALYSIS                |                  | P           |               |                   |
| 640        | SEND-OUT PROCS NOT FEE            |                  | P           |               |                   |
| 641        | SEND-OUT PROCS-DOD NOT FEE        |                  | P           |               |                   |
| 642        | SEND-OUT PROCS FEE                |                  | P           |               |                   |
| 650        | CONTRACT NURSING HOME DAYS        |                  | P           |               |                   |
| 651        | STATE NURSING HOME DAYS           |                  | P           |               |                   |
| 652        | STATE DOMICILIARY HOME DAYS       |                  | P           |               |                   |
| 653        | STATE HOSPITAL CARE               |                  | P           |               |                   |
| 654        | NON VA RESIDENTIAL CARE DAYS      |                  | P           |               |                   |
| 655        | COMMUNITY NON-VA CARE             |                  | P           |               |                   |
| 656        | DOD NON-VA CARE                   |                  | P           |               |                   |
| 657        | ASSIST LIVING VENDOR WORK         |                  | P           |               |                   |
| 660        | CHIROPRACTIC CARE OUTSIDE VA      |                  | P           |               |                   |
| 670        | ASSIST LIVING, VHA-PAID STAFF     |                  | P           |               |                   |
| 680        | HOME/COMMUN HEALTHCARE ASSESS     | E                |             |               |                   |
| 681        | VA-PAID HOME/COMMUN HEALTHCARE    |                  | P           |               |                   |
| 682        | VA-REFER HOME/COMMUN CARE PROV    |                  | P           |               |                   |
| 683        | NONVIDEO HOME TELEHEALTH MONIT    |                  | P           |               |                   |
| 684        | NONVIDEO HOME TELEHEALTH INTER    |                  |             | S             |                   |
| 690        | TELEMEDICINE                      |                  |             | S             |                   |
| 691        | PRE-EMP PHYS MILITRY PERSONNEL    | E                |             |               |                   |
| 692        | TELMD CNSLT SM STA 2ND ONLY       |                  |             | S             |                   |
| 693        | TELMD CNSLT NOT SM STA 2NDONLY    |                  |             | S             |                   |
| 701        | BLOOD PRESSURE CHECK              |                  |             | S             |                   |
| 702        | CHOLESTEROL SCREENING             |                  |             | S             | OCT 1,2002        |
| 703        | MAMMOGRAM (CAN BE PRIMARY)        | E                |             |               |                   |
| 704        | PAP TEST                          |                  |             | S             |                   |
| 705        | FOBT - GUIAC SCREENING            |                  |             | S             | OCT 1,2002        |
| 706        | ALCOHOL SCREENING                 |                  |             | S             |                   |
| 707        | SMOKING CESSATION                 |                  |             | S             |                   |
| 708        | NUTRITION                         |                  |             | S             | OCT 1,2002        |
| 709        | PHY FIT/EXERCISE COUNSELING       |                  |             | S             | OCT 1,2002        |
| 710        | INFLUENZA IMMUNIZATION            |                  |             | S             |                   |
| 711        | INJURY COUNSEL/SEAT BELT USAGE    |                  |             | S             | OCT 1,2002        |
| 712        | HEP C REGISTRY PATIENT            |                  |             | S             |                   |
| 713        | GAMBLING ADDICTION (2ND ONLY)     |                  |             | S             |                   |
| 714        | OTHER EDUCATION 2ND ONLY          |                  |             | S             |                   |
| 715        | ONGOING TRTMT (NON-MH) 2ND        |                  |             | S             |                   |
| 716        | POST SURG RTINE AFTRCARE 2ND      |                  |             | S             |                   |
| 725        | DOMICILIARY OUTREACH SERVICES     | E                |             |               |                   |
| 726        | DOM AFTERCARE - COMMUNITY         | E                |             |               |                   |
| 727        | DOMICILIARY AFTERCARE - VA        | E                |             |               |                   |
| 728        | DOMICILIARY ADM SCREENING SVCS    | E                |             |               |                   |
| 729        | TELEPHONE/DOMICILIARY             |                  | P           |               |                   |
| 730        | DOM GENERAL CARE                  | E                |             |               |                   |
| 731        | PRRTP GENERAL CARE                | E                |             |               |                   |
| 801        | IN-VISN, OTHER VAMC 2ND ONLY      |                  |             | S             |                   |
| 802        | OUT OF VISN, VA 2NDARY ONLY       |                  |             | S             |                   |
| 803        | COMMERCIAL 2NDARY ONLY            |                  |             | S             |                   |
| 900        | SPECIAL SERVICES                  | E                |             |               | OCT 1,1998        |
| 902        | COMPUTED TOMOGRAPHY SCANS         | E                |             |               | APR 1,1989        |
| 903        | RADIATION THERAPY                 | E                |             |               | APR 1,1989        |
| 904        | CHEMOTHERAPY                      | E                |             |               | MAR 1,1989        |
| 905        | AMBULATORY SURGERY SERVICES       | E                |             |               | APR 1,1989        |
| 906        | BLOOD/BLOOD PRODUCTS TRANS.       | E                |             |               | APR 1,1989        |
| 907        | NUCLEAR MAGNETIC RESONANCE        | E                |             |               | APR 1,1989        |
| 999        | EMPLOYEE HEALTH                   |                  | P           |               |                   |

## Appointment Selection Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>The initial run</u> of the Patient Appointment Information Transmission logic will review and select all pending patient appointments created one year prior to the run date. That date was determined to be Sep 1<sup>st</sup>, 2002. Additionally, pending appointments created since Sep 1<sup>st</sup> 2002 are submitted as well. There are two appointment statuses: pending and final. The appointment can be sent only once for a pending and once for a final status, for example, an appointment sent for the first time with a pending status will be sent again if its status is changed to final. An appointment with a final status, sent for the first time, will not be sent again.

The Patient Appointment Info Log file (#409.6) is created to track the transmitted appointments.

<u>On subsequent transmissions</u> all appointments with the Date Appointment Created after the prior transmission are added to the new transmission. The Patient Appointment Info Log file is examined for appointments whose statuses have changed from pending to final and they are also added to the new transmission by creating new entries in the Patient Appointment Info Log file. Those new entries are created with the Retention Flag field equals "N", corresponding to the Final status. The Retention Flag in the original entry is changed from "Y" to "S" – Sent as Final or to "R" – Sent as Rejected if the original entry was rejected.

The final or pending status of an appointment is determined by its associated primary and secondary identifiers, Defined as SCH6 Event Reason and SCH.8 Appt Type. Please note that all 'check-out (CO)' appointments are considered to be final, including those that are still 'action required (AR). That decision has been made on an assumption that the appointment is final when the 'check-out' process is initiated, meaning a patient is present for the appointment. The identifiers, SCH.6 Event Reason and SCH.8 Appointment Type, as well as pending versus final status, represented by SCH.25 Filler status, are mapped in the SIU Event Mapping Table.

The identifiers were determined to reflect the existing computed appointment status in VistA application. Additionally several new identifiers are defined, for allowing to trace continuity of canceled and rescheduled appointments, and for selecting proper appointments from the scheduled 'non-count' clinic group.

All update records should be Final and their previous base records, if any, should be Pending. With the update transmission you receive Pending and Final records but Finals may be new ones or updates to the previously sent Pending appointments. All new Pending records are generated starting from the last creation date from the previous transmission.

SIU Event Mapping Table

|               |                          |                              |                        |
|---------------|--------------------------|------------------------------|------------------------|
| SIU Event | SCH.25 Filler status | SCH.6 Event Reason       | SCH.8 Appt Type    |
| S12           | Pending                  | Check-in (CI)                | Action required (AR)   |
| S12           | Pending                  |                              | No Action Taken (NAT)  |
| S12           | Pending                  |                              | Future (F)             |
| S12           | Pending                  |                              | Non Count (NC)         |
| S12           | Pending                  |                              | Inpatient (I)          |
| S12           | Pending                  |                              | Non Count Future (NCF) |
| S26           | Final                    | No Show (NS)                 |                        |
| S26           | Final                    | No Show (NS)                 | Auto Rebook (ABK)      |
| S15           | Final                    | Cancelled by Clinic (CC)     | Re-schedule (RS)       |
| S 15          | Final                    | Cancelled by Clinic (CC)     |                        |
| S15           | Final                    | Cancelled by Clinic (CC)     | Auto Rebook (ABK)      |
| S15           | Final                    | Cancelled by Patient (CP)    | Re-schedule (RS)       |
| S15           | Final                    | Cancelled by Patient (CP)    |                        |
| S15           | Final                    | Cancelled by Patient (CP)    | Auto Rebook (ABK)      |
| S12 or S14    | Final                    | Check Out by Encounter (COE) | Non Count (NC)         |
| S12 or S14    | Final                    | No Match (NM)                | Non Count (NC)         |
| S12 or S14    | Final                    | Check-out (CO)               | Action required (AR)   |
| S12 or S14    | Final                    | Check-out (CO)               | Inpatient (I)          |
| S12 or S14    | Final                    | Check-out (CO)               | Out patient (O)        |
| S15           | Final                    | Cancelled Terminated (CT)    |                        |

The above table expresses all of the appointment attributes required for a given appointment state. Event reason and appointment type are interpreted as the primary and alternate identifiers.

<u>Auto Rebook (ABK) –</u> This appointment type represents an appointment that has been recently or originally rebooked. We may have appointments originally finalized in VistA as No Show with Auto Rebooking, but their status may be changed into any other status if No Show status is canceled in VistA. In this way the originally entered Auto Rebooking Date may be sent with different Event Reason and/or Appointment Type, not related to the Auto Rebooked Date.

<u>Re-scheduled (RS)</u> – This appointment type is assigned to each canceled appointment if another appointment for a clinic with the same DSS ID (stop code) was scheduled on the same date as the cancellation took place. That situation occurs very often when the auto-rebooking feature is not used. There is an assumption that the newly scheduled appointment is a continuation of the canceled one.

<u>Cancelled Terminated (CT)</u> – This is the Even Reason identifier used to finalize an appointment that was sent as pending and then, during the update process it has been determined that a new appointment is created for the same date and time. That situation causes the previous appointment record to be overridden by the new appointment record with a new creation date.

<u>Future (F</u>) – This Appointment Type applies to all appointments except created for

non-count Hospital Locations, that have Type: <u>Non Count Future (NCF).</u>

<u>Non-count clinic appointments.</u>

In the current VistA functionality, there are many non-count clinics that have scheduled appointments for valid patient care. Any site that is using Event Capture and/or the Surgery packages set up NON COUNT clinics for scheduled appointments. The encounters for these appointments are passed through a SEPARATE COUNT CLINIC with a status of CHECKED OUT. The process to capture those appointments has been established and it is described below.

<u>Non Count Future (NCF</u>) - Scheduled for non-count clinic for the future days starting from the next date to the running date

<u>Check Out By Encounter (COE)</u>. If there is an outpatient encounter entry with the Originating Process Type field (#.08) value equal 2 – Stop code Addition for the same date, and both DSS Clinic Id and DSS Credit Stop match in non-count and count clinic then COE is assigned to the appointment and the count clinic data is returned with this final transmission for this appointment.

<u>No Match (NM)</u> This Event Reason is assigned if a related outpatient encounter, see above, has not been found. If this appointment is evaluated for the first time it is not sent at all. It will be sent with its final status if it was sent before as pending.

<u>Non Count (NC)</u> – This Appt Type without any value of the Event Reason is sent if its scheduled date already passed but not more than 2 days. That time is left because of a possible delay in updating a potential matching encounter.

## Acknowledgement Processing Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acknowledgements are processed in enhanced mode, full two-phased commit. A commit acknowledgement is requested and processed automatically by the VistA HL7 application. Application acknowledgements from the receiving AAC application may generate three types of messages: whole batch accept, whole batch accept with rejections, and whole batch reject. That last type has not been generated at this time and instead the SD-PAIT Manual Batch Rejection may be used.

## Whole Batch Accept

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The batch message and all included messages are accepted by the receiving AAC application. Upon receipt of this message the sending VistA application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message. Internal cross-references are examined and those entries in which field \#4, RETENTION FLAG, do not equal "Y" ( For YES - to be sent when 'Final') are deleted from the file.

## Whole Batch Reject

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The batch message and all included messages may be rejected by manual rejection and in the future by the receiving AAC application. Upon receipt of this message the sending VistA application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message. Field \#7, ERROR MESSAGE, is updated with the rejection code "R". If Field \#4, RETENTION FLAG, equals "Y" ( For YES - to be sent when 'Final') entry updates are complete. The sending application will send those records again, even if they are final,,based on the rejection identified in the Error Message field (# 7).

If the RETENTION FLAG equals "N" (For NO - was sent as 'Final') then the RETENTION FLAG is changed to "Y", making that entry available for resending, and entry updates are complete. No entries in file 409.6 are deleted.

## Whole Batch Accept with Rejections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The batch message is accepted, but some individual messages are rejected by the receiving AAC application. Upon receipt of this message the sending VistA application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message. Individual message rejections are processed in the same fashion as a whole batch rejection and the remaining messages, those accepted, are processed as a whole batch accept.

Messages rejected individually may have the Error Message field (#7) updated with a pointer to one of rejection codes from table AAC001 –Error Code Set.

## Rejected Appointments Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All entries in the PATIENT APPOINTMENT INFO LOG that were marked as rejected by the Acknowledgement processing, are evaluated during transmission as follows.

1.  There is not a verification if the rejected entry was corrected. The acknowledgement sends a notification about rejects and if the rejection codes are listed, they should be corrected before the follow-up transmission. Option SD-PAIT REJECTED should be used to generate a report of rejected appointments. If only a rejection code of "R" code was entered, nothing has to be done because such a message means that the whole batch was rejected and all related appointments will be sent again.
2.  The rejected appointment is transmitted, again it does not matter if has been corrected or not, and a new entry is created in the PATIENT APPOINTMENT INFO LOG with the current appointment status. The original entry marked as rejected is updated with "R" – Resent as Rejected in the Retention Flag field.

## Messages ExamplesExample Batch Message with the Consult Request Date – SCH.11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BHS^~\|\\^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S12^5003236-1^D^2.4^^^AL^AL^USA

SCH^1^^^^^^4^NAT^^^\~\~~20030908\~\~~Date Appt Created\|\~\~\~\~\~~Desired Date\|\~\~~200309180800\~\~~Appt

Date\|\~\~\~\~\~~Checkout Date\|\~\~\~\~\~~Cancellation Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~\~\~\~~Resched

Date\|\~\~~200309010930\~\~~Consult Request Date^^^^^^^^^^^^^^P

PID^1^^""\~\~~USVHA&&L~NI\|7171938\~\~~USVHA&&L~PI^^WOLFIK~EDZIU^^19301212^^^^\~\~\~~19107^^^^^^^^2081212

30P

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^422\~\~\~\~\~\~\~~CECELIA'S CLINIC^402~CARDIAC SURGERY~DSS Clinic ID^418~AMPUTATION CLINIC~DSS

Credit Stop

ZEN^1^^^^^^^^5

ZSP^1^N^

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-2^D^2.4^^^AL^AL^USA

SCH^1^^^^^CC^3^RS^^^\~\~~20030829\~\~~Date Appt Created\|\~\~~20030829\~\~~Desired

Date\|\~\~~200308291330\~\~~Appt Date\|\~\~\~\~\~~Checkout Date\|\~\~~200308290940\~\~~Cancellation

Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~~200308291030\~\~~Resched Date\|\~\~~200308200820\~\~~Consult Request Date ^^^^^^^^^^^^^^F

PID^1^^""\~\~~USVHA&&L~NI\|7172069\~\~~USVHA&&L~PI^^YORTY~OUTPATIENT^^19710604^^^^\~\~\~~17042^^^^^^^^509

060471P

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^614\~\~\~\~\~\~\~~YORTY'S CLINIC^329~MEDICAL PROCEDURE UNIT~DSS Clinic ID^\~~DSS

Credit Stop

ZEN^1^^^^^^^^1

ZSP^1^Y^60

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-3^D^2.4^^^AL^AL^USA

SCH^1^^^^^CP^3^RS^^^\~\~~20030829\~\~~Date Appt Created\|\~\~~20030829\~\~~Desired

Date\|\~\~~200309010815\~\~~Appt Date\|\~\~\~\~\~~Checkout Date\|\~\~~200308290856\~\~~Cancellation

Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~~200309010815\~\~~Resched Date\|\~\~~200308010710\~\~~Consult Request Date ^^^^^^^^^^^^^^F

PID^1^^""\~\~~USVHA&&L~NI\|7172424\~\~~USVHA&&L~PI^^VILELLA~JOEY~ASHLEY~III~MR^^19490

416^^^^\~\~\~~33354^^^^^^^^244990005

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^NTF

AIL^1^^312\~\~\~\~\~\~\~~XXXXX^102~ADMITTING/SCREENING~DSS Clinic ID^104~PULMONARY FUNCTION~DSS Credit

Stop

ZSP^1^N^

BTS^3

Example Application Acknowledgement Message:

BHS^~\|\\^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20030918085247-0500^^~P~ACK\|S12~2.4~AL~NE^AA~^104^5001738

MSA^AA^5001738^

BTS^1

# Appendix B - VistA Interface Engine Site I.P. Addresses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should know IP address from your messaging team, to be entered with SD-PAIT Logical Link. This is address to send PAIT in HL7 format to your local VIE box.

# Appendix C – Trouble Shooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File 409.6 ( PATIENT APPOINTMENT INFO LOG) is populated with SDPAIT transmission records and is self maintaining. Entries are purged automatically when a final status appointment is transmitted and acknowledgements received. No user or programmer intervention is required.

Members of the SD-PAIT mail group will receive notifications when batch transmissions are complete. Mail group members will also be notified when acknowledgements to the batch messages are received.

## Mail Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If mail message notifications are not received by members of the SD-PAIT mail group check the following:

Insure the SD-PAIT link is active by doing the following from the HL7 Main Menu

Select HL7 Main Menu Option:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: SD-PAIT

This LLP has been enabled!

> ![](sd-5-3-333-pait-release-notes/008.png)

## HL7 System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All outgoing HL7 messages are sent over this link. You can verify activity on this link with the System Monitor Utility of the HL7 package:

> ![](sd-5-3-333-pait-release-notes/009.png)

In the example screen above the TO SEND column lists 12 messages and the SENT column 1. If your SENT column does not increment to match the TO SEND column it may be necessary to stop and then start the SD-PAIT link as mentioned above.

## VistA Interface Engine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

## XTMP Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A temporary snapshot of each record deleted by the HL7 acknowledgement processing logic is created in Global ^XTMP("SDRPA-"\_BATCHNUMBER,

You may view this global to confirm acknowledgement processing.

## ## VistA Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 indicates the reports that may be generated at each site after transmission has completed. By entering the first three letters of the desired report will initiate that report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Acknowledgement Summary</p>
<p>Pending Transmissions</p>
<p>Rejected Transmissions</p>
<p>Transmission Summary</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 1

Acknowledgement Summary:

The Acknowledgement Summary may be used to verify the batch numbers generated from a particular site (Figure 2). This report lists all batches in Batch Control ID order. The report also indicates the Message Control ID, the Acknowledgement Date, and Acknowledgement Type. The following Acknowledgement Types are indicated:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Application Accept - AA</p>
<p>Application Error - AE</p>
<p>Application Reject - AR</p>
<p>Manual Rejection - MR</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PAIT ACK SUMMARY FEB 27,2004 11:26 PAGE 1</p>
<p>APPLICATION ACK APPLICATION ACK</p>
<p>BATCH CONTROL ID MESSAGE CONTROL ID DATE/TIME TYPE</p>
<p>------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>TRANSMISSION FINISHED: FEB 20,2004 20:45</p>
<p>75611134952 75615626811 FEB 24,2004 08:38 APPLICATION ACCEPT</p>
<p>75611135142 75615627064 FEB 24,2004 08:39 APPLICATION ACCEPT</p>
<p>75611135273 75615627292 FEB 24,2004 08:40 APPLICATION ACCEPT</p>
<p>75611135591 75615627625 FEB 24,2004 08:41 APPLICATION ACCEPT</p>
<p>75611135943 75615628077 FEB 24,2004 08:42 APPLICATION ACCEPT</p>
<p>75611136242 75615628454 FEB 24,2004 08:43 APPLICATION ACCEPT</p>
<p>75611136597 75615628914 FEB 24,2004 08:44 APPLICATION ACCEPT</p>
<p>75611136841 75615629306 FEB 24,2004 08:45 APPLICATION ACCEPT</p>
<p>75611137250 75615629892 FEB 24,2004 08:46 APPLICATION ACCEPT</p>
<p>75611137757 75615630556 FEB 24,2004 12:49 APPLICATION ERROR</p>
<p>75611138197 75615631071 FEB 24,2004 12:50 APPLICATION ACCEPT</p>
<p>75611138675 75615631643 FEB 24,2004 12:50 APPLICATION ACCEPT</p>
<p>75611138981 75615632257 FEB 24,2004 12:51 APPLICATION ACCEPT</p>
<p>75611139225 75615632561 FEB 24,2004 12:52 APPLICATION ACCEPT</p>
<p>75611139441 75615632855 FEB 24,2004 12:53 APPLICATION ACCEPT</p>
<p>75611139687 75615633142 FEB 24,2004 12:54 APPLICATION ACCEPT</p>
<p>75611139729 75615633201 FEB 24,2004 12:54 APPLICATION ACCEPT</p>
<p>75611139775 75615633241 FEB 24,2004 12:55 APPLICATION ERROR</p>
<p>75611139829 75615633301 FEB 24,2004 12:56 APPLICATION ACCEPT</p>
<p>75611139855 75615633327 FEB 24,2004 12:56 APPLICATION ACCEPT</p>
<p>75611140007 75615633495 FEB 24,2004 12:57 APPLICATION ACCEPT</p>
<p>75611140038 75615633536 FEB 24,2004 12:58 APPLICATION ACCEPT</p>
<p>75611140066 75615633568 FEB 24,2004 12:59 APPLICATION ACCEPT</p>
<p>75611140072 75615633574 FEB 24,2004 13:00 APPLICATION ACCEPT</p>
<p>75611140100 75615633634 FEB 24,2004 13:00 APPLICATION ACCEPT</p>
<p>75611140118 75615633652 FEB 24,2004 13:01 APPLICATION ACCEPT</p>
<p>75611140124 75615633658 FEB 24,2004 13:02 APPLICATION ACCEPT</p>
<p>75611140140 75615633672 FEB 24,2004 13:02 APPLICATION ACCEPT</p>
<p>75611140150 75615633683 FEB 24,2004 13:03 APPLICATION ACCEPT</p>
<p>75611140160 75615633693 FEB 24,2004 13:04 APPLICATION ACCEPT</p>
<p>75611140170 75615633704 FEB 24,2004 13:04 APPLICATION ACCEPT</p>
<p>75611140176 75615633710 FEB 24,2004 13:05 APPLICATION ACCEPT</p>
<p>75611140188 75615633722 FEB 24,2004 13:05 APPLICATION ACCEPT</p>
<p>75611140190 75615633724 FEB 24,2004 13:05 APPLICATION ACCEPT</p>
<p>TRANSMISSION FINISHED: FEB 25,2004 16:02</p>
<p>75611182041 75615685674 FEB 26,2004 10:41 APPLICATION ACCEPT</p>
<p>75611182938 75615686799 FEB 26,2004 10:42 APPLICATION ERROR</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 2

> **NOTE:** AR – The whole batch rejection from the AAC has not been implemented at this time and will be future enhancement. Figure 2 shows acknowledgements received for two transmissions.

Pending Transmission:

The Pending Transmission report (Figure 3) is to be used by VistA sites only to take an action of finalizing appointments with the appointment scheduled date (APPT_DATE) already in the past. These records should be "Check Out" or Cancelled. This report lists all Patient Pending records by Date Appointment Made. A print of the report is not included due to sensitive information.

Rejected Transmission:

The Rejected Transmission report should be used to review and correct patient records that the AAC rejected. Rejections can occur due to incomplete dates, invalid site/facility codes not matching the site sending the information, etc. for a particular site (Figure 3). See table AAC001 - Error Code Set for rejection code definition.

The VistA should use this report for correcting their patient appointment records. Once the VistA has corrected the record it will be sent to the National Data Base in the next bi-monthly update run and loaded into the National Database. The correction of rejected records is the VistA site's responsibility.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>REJECTED TRANSMISSION LOG FEB 27,2004 11:34 PAGE 1</p>
<p>ERROR</p>
<p>PATIENT APPT DATE SHORT DESCRIPTION MESSAGE</p>
<p>CLINIC</p>
<p>-----------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>ERROR MESSAGE: 350</p>
<p>PUBLIC,JOHN Q OCT 6,2003 15:56 HL7 date is not in proper format or is missing 350</p>
<p>FLU SHOT CLINIC</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 3

> **NOTE:** The most commonly expected rejection codes are 350 and 200, see TABLE AAC001-Error Code Set. Error 350 is mostly caused by too old desired date of appointment, filed in VistA sub file 1900 of the Patient File.

Error 350

It has been also determined that in some situation the Rescheduled date has not acceptable date starting from 1800. That Rescheduled date is identified by PAIT if the following process:

1\. An appointment is canceled without re-booking.

2\. If there is another appointment created on the same day as the cancellation date, and for the same clinic there is an assumption that this is continuation of that scheduling, and that new scheduled date/time is included with the original appointment as the Reschedule Date.

3\. The first available appointment meeting criteria listed in 2. is processed.

4\. It came out that randomly some appointments have their scheduled date/time starting from 1800, and this date is causing rejection by the AAC as well.

5\. If you cannot find an '"odd" date with your original appointment you should look for "ADSAM" cross reference in the Patient file with the cancellation date and the patient DFN, to see what "odd" appointments were scheduled, and if so to remove them after evaluation what else needs to be done.

6\. Removal of that "odd" appointment would prevent the original appointment from being sent with The "bad", not acceptable Rescheduled Date.

Error 200

Error 200 indicates that an entry in the Hospital Location file \#44 is configured with the DIVISION field (3.5) pointing to a Medical Center Division entry whose Institution pointer conflicts with the facility station number.

Hint: Correct the Hospital Location entry's Division field (3.5) to point to the correct Medical Center Division, or correct the Institution pointer of the Medical Center Division.

Transmission Summary:

The Transmission Summary report may be used to determine the total number of patient appointment records, the run date, total number of batches, Batch Control ID, Message Control ID, and date/time stamp (Figure 4). It can be requested by EVS, National Help Desk and /or AAC for matching transmitted batches with those received. at the AAC.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TRANSMISSION SUMMARY FEB 27,2004 11:35 PAGE 1</p>
<p>LAST</p>
<p>SCANNED # OF</p>
<p>RUN DATE DATE APPOINTMENTS</p>
<p># OF BATCH CREATE</p>
<p>BATCHES BATCH CONTROL ID DATE/TIME MESSAGE CONTROL ID</p>
<p>----------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>FEB 20,2004 FEB 19,2004 165317</p>
<p>34 75611134952 FEB 20,2004 12:20 75615626811</p>
<p>75611135142 FEB 20,2004 12:36 75615627064</p>
<p>75611135273 FEB 20,2004 12:51 75615627292</p>
<p>75611135591 FEB 20,2004 13:09 75615627625</p>
<p>75611135943 FEB 20,2004 13:28 75615628077</p>
<p>75611136242 FEB 20,2004 13:42 75615628454</p>
<p>75611136597 FEB 20,2004 13:58 75615628914</p>
<p>75611136841 FEB 20,2004 14:14 75615629306</p>
<p>75611137250 FEB 20,2004 14:36 75615629892</p>
<p>75611137757 FEB 20,2004 14:59 75615630556</p>
<p>75611138197 FEB 20,2004 15:21 75615631071</p>
<p>75611138675 FEB 20,2004 15:42 75615631643</p>
<p>75611138981 FEB 20,2004 16:01 75615632257</p>
<p>75611139225 FEB 20,2004 16:18 75615632561</p>
<p>75611139441 FEB 20,2004 16:35 75615632855</p>
<p>75611139687 FEB 20,2004 16:51 75615633142</p>
<p>75611139729 FEB 20,2004 17:04 75615633201</p>
<p>75611139775 FEB 20,2004 17:17 75615633241</p>
<p>75611139829 FEB 20,2004 17:34 75615633301</p>
<p>75611139855 FEB 20,2004 17:48 75615633327</p>
<p>75611140007 FEB 20,2004 18:03 75615633495</p>
<p>75611140038 FEB 20,2004 18:17 75615633536</p>
<p>75611140066 FEB 20,2004 18:31 75615633568</p>
<p>75611140072 FEB 20,2004 18:44 75615633574</p>
<p>75611140100 FEB 20,2004 18:58 75615633634</p>
<p>75611140118 FEB 20,2004 19:13 75615633652</p>
<p>75611140124 FEB 20,2004 19:26 75615633658</p>
<p>75611140140 FEB 20,2004 19:36 75615633672</p>
<p>75611140150 FEB 20,2004 19:46 75615633683</p>
<p>75611140160 FEB 20,2004 19:56 75615633693</p>
<p>75611140170 FEB 20,2004 20:08 75615633704</p>
<p>75611140176 FEB 20,2004 20:25 75615633710</p>
<p>75611140188 FEB 20,2004 20:41 75615633722</p>
<p>75611140190 FEB 20,2004 20:45 75615633724</p>
<p>FEB 25,2004 FEB 24,2004 8405</p>
<p>2 75611182041 FEB 25,2004 15:22 75615685674</p>
<p>75611182938 FEB 25,2004 15:59 75615686799</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 4

FORUM Server Reporting

The intended audience for the remainder of the document is Office of Information staff and included for information purposes.

<u>EVS:</u>

On the FORUM server there is a menu for running and viewing the reports for

VistA totals, ACK message status, Missing Sites, and Transmitted Sites. These

reports may be used to monitor the seeding and bi-monthly updates. These reports

will indicate specific activity from each site. The following figure is the menu option

available on the FORUM server. Currently there are three more options, and that menu looks as follows:

Figure 1

Option 1 Completed Background Job Report

When the program completes at each VistA the "Completed Background Job Report" is populated with the number of patient appointment records that were transmitted to the National Database in Austin (Figure 2). Since the program sends this information in batches (5,000 records maximum) the total batch count is recorded. These two figures should be matched with the AAC Transmitted Site report (Option 4). If they do not match then there is reason to investigate the difference.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Sites - Completed Background Job FEB 27,2004 13:36 PAGE 1</p>
<p>SITE # OF # OF</p>
<p>NUMBER RUN COMPLETION DATE BATCHES APPOINTMENTS</p>
<p>---------------------------------------------------------------------------------------------------------------------------------------</p>
<p>656 FEB 20,2004 14:53 59 294917</p>
<p>756 FEB 21,2004 01:30 34 165317</p>
<p>659 FEB 21,2004 02:09 43 210278</p>
<p>649 FEB 22,2004 03:21 30 147223</p>
<p>649 FEB 25,2004 15:02 1 4985</p>
<p>756 FEB 25,2004 16:02 2 8405</p>
<p>656 FEB 26,2004 06:16 4 18691</p>
<p>659 FEB 26,2004 09:55 3 12708</p>
<p>--------</p>
<p>COUNT 8</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 2

> **NOTE:** The above table includes both seeding and the update transmission from four VistA sites.

In the case they do not match, the Vitria IE monitoring reports will provide information on whether or not the patient appointment records were received and passed along to the Austin Automation Center (AAC). Use the following URL, ID, and password to connect to Messaging and Interface System's site. The ID and password are case sensitive.

> URL: [<u>http://vhaaacviev4:8080/ciev/hbase</u>](http://vhaaacviev4:8080/ciev/hbase)

> ID =

> Password =

Check with your site's Information Resources Management (IRM) officer for access.

Option 2 All Ack's Received Report

The "All ACK's Received Report" indicates at the summary level the number of ACK messages processed for each site and the date the process was completed (Figure 3). There is a count figure that indicates the number of sites reported. If in the event the site's ACK message count do not match this can be an indicator that the AAC either did not receive the batch from VistA via the Vitria IE or AAC experienced a problem when processing the batch. In either case, the missing batch(es) will need to be identified and, at this time, the manual batch rejection initiated at the VistA site. To determine the missing batch(es) proceed to Option 5 to view the detailed ACK message status report and a related VistA site has to be contacted to run the Acknowledgement Summary report (VistA Reporting section) with Batch Control ID. They must be compared to the Batch Control ID's received by the AAC.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>All ACKs Received Report FEB 27,2004 13:40 PAGE 1</p>
<p>Site Run Completed Ack's</p>
<p>-------------------------------------------------------------------------</p>
<p>649 FEB 22,2004 30 of 30</p>
<p>649 FEB 25,2004 1 of 1</p>
<p>656 FEB 20,2004 59 of 59</p>
<p>656 FEB 26,2004 4 of 4</p>
<p>659 FEB 21,2004 43 of 43</p>
<p>659 FEB 26,2004 3 of 3</p>
<p>756 FEB 20,2004 34 of 34</p>
<p>756 FEB 25,2004 2 of 2</p>
<p>--------</p>
<p>COUNT 8</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 3

Option 3 Missing Sites Report

This option allows EVS and HSD&D to view which site transmissions were not received at the AAC during the seeding or specific update run. The report lists the sites that did not transmit by alphabetical order of Site Name.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Missing Site Report MAR 1,2004 15:23 PAGE 1</p>
<p>MISSING SITE</p>
<p># SITE NAME REPORT DATE</p>
<p>--------------------------------------------------------------------------------------------------------</p>
<p><mark>REDACTED</mark> ------------</p>
<p>COUNT 122</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 4

Option 4 Transmitted Sites Report

This report indicates the total number of patient appointment records and batch counts received at the AAC for each transmitted site along with the date received. This report should be used with "Completed Background Job Report" (Option 1) to determine if there are differences between what the VistA sites reported as transmitted and what the AAC reports as being received. In the case they do not match refer to the instructions outlined in Option 1.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Transmitted Sites Report MAR 1,2004 15:28 PAGE 1</p>
<p>SITE</p>
<p># SITE NAME TOTAL RECORDS TOTAL BATCHES REPORT DATE</p>
<p>--------------------------------------------------------------------------------------------------------------------</p>
<p><mark>REDACTED</mark></p>
<p>-------</p>
<p>COUNT 4</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 5

Option 5 ACK Status Report

The "ACK Status Report" indicates at the detail level the receipt of each ACK message for each site (Figure 6). The last detail ACK message record indicates whether the site's ACK message processing is complete ("Yes"). There is a sub count for each site indicating the number of ACK messages processed and count that indicates total ACK messages processed for all sites.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACK STATUS REPORT FEB 27,2004 13:41 PAGE 1</p>
<p>SITE ACKS</p>
<p>NUMBER RUN ACK STATUS COMPLETE DATE/TIME</p>
<p>------------------------------------------------------------------------------------------------------------------------------</p>
<p>649 1 of 30 FEB 24,2004 10:44</p>
<p>649 3 of 30 FEB 24,2004 11:56</p>
<p>649 4 of 30 FEB 24,2004 11:56</p>
<p>649 5 of 30 FEB 24,2004 11:56</p>
<p>649 6 of 30 FEB 24,2004 11:56</p>
<p>649 7 of 30 FEB 24,2004 11:56</p>
<p>649 8 of 30 FEB 24,2004 11:56</p>
<p>649 9 of 30 FEB 24,2004 11:56</p>
<p>649 10 of 30 FEB 24,2004 11:56</p>
<p>649 11 of 30 FEB 24,2004 11:56</p>
<p>649 12 of 30 FEB 24,2004 11:56</p>
<p>649 13 of 30 FEB 24,2004 11:56</p>
<p>649 14 of 30 FEB 24,2004 11:56</p>
<p>649 15 of 30 FEB 24,2004 11:56</p>
<p>649 16 of 30 FEB 24,2004 11:57</p>
<p>649 17 of 30 FEB 24,2004 11:57</p>
<p>649 18 of 30 FEB 24,2004 11:57</p>
<p>ACK STATUS REPORT FEB 27,2004 13:41 PAGE 2</p>
<p>SITE ACKS</p>
<p>NUMBER RUN ACK STATUS COMPLETE DATE/TIME</p>
<p>------------------------------------------------------------------------------------------------------------------------------</p>
<p>649 2 of 30 FEB 24,2004 11:57</p>
<p>649 19 of 30 FEB 24,2004 14:49</p>
<p>649 20 of 30 FEB 24,2004 14:49</p>
<p>649 21 of 30 FEB 24,2004 14:50</p>
<p>649 22 of 30 FEB 24,2004 14:51</p>
<p>649 23 of 30 FEB 24,2004 14:52</p>
<p>649 24 of 30 FEB 24,2004 14:52</p>
<p>649 25 of 30 FEB 24,2004 14:53</p>
<p>649 26 of 30 FEB 24,2004 14:53</p>
<p>649 27 of 30 FEB 24,2004 14:54</p>
<p>649 28 of 30 FEB 24,2004 14:54</p>
<p>649 29 of 30 FEB 24,2004 14:55</p>
<p>649 30 of 30 YES FEB 24,2004 14:55</p>
<p>--------</p>
<p>SUBCOUNT 30</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 6

> **NOTE:** An example in Figure 6 shows only one station. Please note that

Acknowledgements may be received in different order to the transmitted batches.

Each batch has a unique number making it easy to locate should a site's VistA count not equal the count from the AAC. Once the batch control number(s) are located the investigator will need to access the VistA site's Acknowledgement Summary report for the actual Batch Control ID(s) that will need to be manually rejected. The Austin Automation Center generate a summary report of batches received from all sites with a number of appointments and a number of rejections.

Option 6. Site Message History

You can follow up a history of PAIT for each site from its start to receiving acknowledgements.

Option 7. PAIT Summary Report

This report is a compilation of all messaging activity from VistA through VIE to the AAC, and gives the best overview of each PAIT activity.

## National Help Desk Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Missing Site Reporting

<u>From the AAC:</u>

One the 5<sup>th</sup> and 19<sup>th</sup> of every month the AAC will send to VHA National Help Desk an email message indicating those sites that the AAC did not receive patient appointment information transmissions. This report will include the site (facility) number and name. The corresponding report is also sent by the AAC to the Forum Server (see Option 3 in Forum Server Reporting).

![](sd-5-3-333-pait-release-notes/010.png)

<u>VHA National Help Desk</u>

Upon receipt of the email from "MVSMail" listing the sites that did not transmit (Missing Site Report) the VHA National Help Desk will enter a Remedy Ticket the sites that did not transmit. The Remedy Ticket should be assigned to EVS who will begin the investigation process.

<u>EVS</u>

EVS will act upon the receipt of the Remedy Ticket by running the Complete Background Job Report on the FORUM server. This report will indicate whether the site actually gathered data and passed it to the local Vitria IE machine. If the report indicates no activity from the site, EVS will contact the site to determine why the site did not run. Based on the reason, EVS may need to contact other groups to provide assistance. In the case the report indicates there was activity, EVS may need to access the M&IS URL to review the Vitria IE activity reports. The M&IS URL, ID, and password are:

> URL: [<u>http://vhaaacviev4:8080/ciev/hbase</u>](http://vhaaacviev4:8080/ciev/hbase)

> ID =

> Password =

> Check with your site's Information Resources Management (IRM) officer for access

![](sd-5-3-333-pait-release-notes/011.png)

There are two reports that indicate activity of patient appointment records being sent to the AAC. The first indicates activity at the VistA site's local Vitria IE (Remote Outgoing Batch Tallies). The report presents the Site ID, Name, Most Recent Date, and Batch Count.

![](sd-5-3-333-pait-release-notes/012.png)

The second report indicates the files transferred (FTP) to the mainframe at the AAC (File Uploads to MVS). This report demonstrates the Site(s) ID, Name, and Batch Count that were included in the file transfer. It should be noted that the batch count indicated in a file sent to the AAC may not be the total batch count for that site.

![](sd-5-3-333-pait-release-notes/013.png)

Examination of all files transferred will need to be performed and manually adding the batch counts for all files to determine if the site's total batch count matches the count on the FORUM server.

- If the reports on the FORUM server indicate the site did not generate batches EVS will need to contact the site to find the responsible person who can determine or explain why the program did not run.
- If the reports on the FORUM server indicate the site did generate batches but did not transmit and the Vitria IE reports do not indicate the site's activity, then EVS will need to contact M&IS for assistance..
- If the reports on the FORUM server and the Vitria IE reports indicate the site did transmit, then EVS will need to contact the AAC for assistance.

> **NOTE:** The primary trouble shooting to determine the problem in communications should be done by following directions in the Trouble Shooting chapter.

## VistA Communication Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA National Help Desk:

<span class="mark">REDACTED</span>

| <span class="mark">REDACTED</span> |
|------------------------------------|

Figure 2

The above message, Figure 2 shows that the communication with Vitria was not established at all and none of generated batches were transmitted.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: SD*5.3*376 PAIT Release Notes

## Combat Veteran Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Combat Veteran Eligibility is used to identify a Combat Veteran (CV) Status veteran seeking medical care for a specific date. CV eligibility will be determined as of the Appointment Creation Date. The following values for Combat Veteran Eligibility are:

- 1 (Yes) is sent if the patient was/is considered a combat veteran on the Appointment Creation Date;
- 0 (No) is sent if the patient wasn't/isn't considered a combat veteran on the Appointment Creation Date.

Combat Veteran Eligibility is now included in HL7 segment ZEL.

## Combat Veteran End Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Combat Veteran End Date represents the last day for combat veteran eligibility. The existence of a CV End Date indicates that a veteran has been CV eligible at some point in time. Even if the CV eligibility has expired, this date will still be present. Combat Veteran End Date is now included in HL7 segment ZEL

## Combat Veteran Indication 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Combat Veteran Indication signifies if an appointment is related to a CV illness/injury. During checkout or during the update of an appointment's classifications, the question is asked if the appointment was related to the veteran's CV status. The following values for Combat Veteran Indication are:

- 1 (Yes) is sent if the appointment was related to the veteran's CV status;
- 0 (No) is sent if the appointment was not related to the veteran's CV status.

The answer to this question is now included in a seventh repetition of the ZCL HL7 segment (VA Specific Classification).

## Combat History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Combat History data is retrieved and transmitted to calculate the waiting time experienced by service members recently returning from the war in Iraq. A new HL7 segment has been implemented (ZMH) to transmit this combat history data to the Austin Automation Center (AAC). Three repetitions of the ZMH segment will be used to transmit the following combat history information:

- Last Service Separation Date
- Combat Veteran Indicated - signifies if the individual was ever considered a Combat Veteran. Valid values are:
  - Y – yes
  - N - no
- Combat Service Location – the location where the individual was in combat. Valid values are:
  - WORLD WAR I
  - WORLD WAR II - EUROPE
  - WORLD WAR II - PACIFIC
  - KOREAN
  - VIETNAM
  - OTHER
  - PERSIAN GULF WAR
  - YUGOSLAVIA CONFLICT
- Persian Gulf Service – indicates if the individual served in the Persian Gulf. Valid values are:
  - Y – yes
  - N – no

## "Job Started" message on the Forum server. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message to the Forum server and a local SD-PAIT Mail Group will now be generated at the beginning of each site's PAIT transmission to confirm that the bi-monthly data collection process has begun. This start message also details the status of the SD-PAIT logical link and possible reason for any communications error. This message will be sent to the SD-PAIT mail group in the form of a MailMan message. The following is an example of this new Job Started message:

Subj: 500 - PAIT START JOB \[#1955884\] 09/21/04@12:11 3 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The PAIT job has started - TASK \#: 2717310

Site Started SD-PAIT status Task \#

500 \|3040921.121119 \|Enabled \|2717310

The local job completion message will stay as is, with subject 500 - PAIT BACKGROUND JOB, where 500 = station number.

## Post-installation updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approximately 50% of the sites did not receive initial seeding acknowledgement messages. Sites that did not receive HL7 acknowledgement (ACK) messages during the seeding process due to communication problems will be updated. A post-init routine, working as a driver, will identify a particular site where there is a need to execute the acknowledgement process, by retrieving rejected appointments from routines containing site-specific data only for sites with rejections. Not rejected appointments are processed as acknowledged.

There is a possibility that rejected appointments if originally sent as pending may have already been process.

## Clean up file PATIENT APPOINTMENT INFO LOG (#409.6).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Differences between the error report that the site can generate using option: SD-PAIT REJECTED \[Rejected Transmission\] and the error report coming from the AAC have been identified at some sites. The reason for the current differences is associated with acknowledgements not being received by some sites in a timely manner. Currently, the acknowledgement process initiates cleaning of the previously rejected entries in each site's PATIENT APPOINTMENT INFO LOG (#409.6) file. Patch SD\*5.3\*376 will perform a clean-up of all previous entries with the exception of those in pending status so that now the SD-PAIT REJECTED report and AAC Rejected Report will match.

## Outgoing & Upload Statistics Sent via MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Forum Server accepts and processes new completion messages from the VistA Interface Engine and Austin Automation Center. Outgoing batch and MVS upload statistics from the AAC webpage have been merged into mail messages and are transmitted to the Forum Server. The messages are processed and the data used to determine if the transmission process has been completed for each site.

Outgoing batch and MVS upload statistics provided on the AAC webpage will be incorporated into a MailMan message format and transmitted to individuals in the SD-PAIT mail group.

## Provider Name Subcomponent Modifications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, if a middle initial and/or a suffix were not identified, the transmitted HL7 AIP segment did not include '~' as the delimiter after the identified First and Last name subcomponents. Tilde (~) delimiters will now be included, even if there is no middle initial and/or no suffix identified. This is acceptable by HL7 standards but was modified on request of Austin Automation Center. For example:

- PROVIDERLAST,PROVIDERFIRST will be transmitted as: PROVIDERLAST~PROVIDERFIRST\~~
- PROVIDERLAST,PROVIDERFIRST K JR will be transmitted as: PROVIDERLAST~PROVIDERFIRST~K~JR
- PROVIDERLAST,PROVIDERFIRST K will be transmitted as: PROVIDERLAST~PROVIDERFIRST~K~
- PROVIDERLAST,PROVIDERFIRST JR will be transmitted as: PROVIDERLAST~PROVIDERFIRST\~~JR

## Interrupted Transmission Repair Process Fix.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For any repair needed to a previously interrupted, not completed transmission, (one where there is not a completion message for a site that had a "job started" message), a message is generated to the National Help Desk requesting a NOIS be created. An additional run must be started by the site to transmit the expected appointments for the current time period. A separate option, SD-PAIT Last Run Repair \[SD-PAIT REPAIR\] is available. This option must be run before the next transmission is started.

## Automated Verification on the Forum Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Manual checking of batches generated, transmitted, and received is required to ensure each site has completed the bi-monthly transmission. This is time consuming and will be automated. An automated process will be established on the Forum Server that alerts the National Help Desk when any stage of the transmission process fails.

To automate this functionality, new tasked background jobs will be scheduled to run on the Forum Server that incorporate elements from the Vista Interface Engine messaging team (VIE) and the AAC team. VistA IE is expected to report the number of batches received per site, and AAC is expected to report the number of batches received and a total of all received appointments. Any discrepancies with the VistA completion messages will generate warning messages to the National Help Desk

As each site starts and completes designated tasks, a status message will be sent to the Forum Server. Six background tasks will be initiated at scheduled intervals on the Forum Server to determine the status of PAIT at all sites, as follows.

| TASK           | Schedule 1                      | Schedule 2                       | Description                                                                                                                                                                           |
|--------------------|-------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAIT not started   | 12:01am 2<sup>nd</sup> day of month | 12:01am 16<sup>th</sup> day of month | Generates mail message to National Help Desk listing sites that did not start the scheduled PAIT.                                                                                         |
| Outgoing IE        | 09:00am 3<sup>rd</sup> day of month | 09:00am 17<sup>th</sup> day of month | Generates mail message to National Help Desk listing sites where the number of outgoing batches from VistA DOES NOT match the number of outgoing batches from the local interface engine. |
| PAIT not completed | 09:01am 3<sup>rd</sup> day of month | 09:01am 17<sup>th</sup> day of month | Generates mail message to National Help Desk listing sites that have not completed PAIT.                                                                                                  |
| NO ACKs            | 12:01am 4<sup>th</sup> day of month | 12:01am 18<sup>th</sup> day of month | Generates mail message to National Help Desk listing sites that have not received ANY HL7 acknowledgement messages.                                                                       |
| ACKs not completed | 12:01am 4<sup>th</sup> day of month | 12:01a 18<sup>th</sup> day of month  | Generates mail message to National Help Desk listing sites that have not received ALL HL7 acknowledgement messages.                                                                       |
| Uploaded MVS       | 09:00am 4<sup>th</sup> day of month | 09:00am 18<sup>th</sup> day of month | Generates mail message to National Help Desk listing sites where the number of outgoing batches from Vista, local interface engine, and AAC ftp to MVS mainframe DO NOT match.            |
| Job Complete       | 12 Noon 4<sup>th</sup> day of Month | 12 Noon 18<sup>th</sup> day of Month | Generates mail message to the National Help Desk listing sites where it compares the Job Complete messages on the Forum Server that DO NOT match AAC Transmitted Sites report.            |
|                    |                                     |                                      |                                                                                                                                                                                           |

### PAIT not started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: PAIT NOT STARTED

The following site(s) have not started the bi-monthly PAIT. Please initiate a NOIS for each site referencing the Interface Engine Module:

541 CLEVELAND VAMC

612 NORTHERN CALIFORNIA HCS

### PAIT not completed 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: PAIT NOT COMPLETED

The following site(s) have not completed the bi-monthly PAIT background job. Please initiate a NOIS for each site referencing the Interface Engine Module:

541 CLEVELAND VAMC

612 NORTHERN CALIFORNIA HCS

### NO ACKs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: NO ACKNOWLEGEMENTS

The following site(s) have not received ANY acknowledgement

messages for the bi-monthly PAIT. Please initiate a NOIS for

each site referencing the Interface Engine Module:

528 UPSTATE NEW YORK HCS

598 CENTRAL ARKANSAS HCS

ACKs Not Completed

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Monday, September 20, 2004 2:24 PM

To:

Subject: ACKNOWLEDGEMENTS NOT COMPLETE

The following site(s) have not received all acknowledgements for

the bi-monthly PAIT. Please initiate a NOIS for each site

referencing the Interface Engine Module:

541 CLEVELAND VAMC

612 NORTHERN CALIFORNIA HCS

657 ST. LOUIS MO VAMC-JC DIVISION

Outgoing IE

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Friday, September 17, 2004 9:16 AM

To:

Subject: OUTGOING IE COMPARE

The following sites batch message counts comparing the number sent

from Vista and the number sent from local Interface Engine do not match.

Please initiate a NOIS for each site listed referencing the Interface

Engine Module:

Site \# VISTA SENT OUTGOING IE SENT

528 25 26

557 4 8

589 22 23

603 7 8

629 8 9

679 3 16

#### MVS Upload

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Wednesday, September 22, 2004 1:16 PM

To:

Subject: MVS UPLOAD COMPARE

The following sites batch message counts comparing the number sent

from Vista and the number uploaded to MVS do not match. Please

initiate a NOIS for each site listed referencing the Interface

Engine Module:

Site \# VISTA SENT MVS UPLOADED

500 1

528 25 26

540 2 4

557 4 8

589 22 23

603 7 8

614 7 8

629 8 9

631 3 4

679 3 15

### Job Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From: POSTMASTER@FORUM.VA.GOV \[mailto:POSTMASTER@FORUM.VA.GOV\]

Sent: Wednesday, September 22, 2004 1:16 PM

To:

Subject: JOB COMPLETE COMPARE

The following sites Job Complete messages on the Forum server do not match the AAC Transmitted Sites report. Please initiate a NOIS for each site listed referencing the Interface Engine Module:

528 UPSTATE NEW YORK HCS

598 CENTRAL ARKANSAS HCS

## More Descriptive Completion Message Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

More descriptive message text will be added to the various completion message to better inform the user of transmission segment status' and determine the proper NOIS module to be alerted if a problem occurs. The following new text will be added to the MailMan completion message, when applicable:

- WARNING: TASK STOPPED BY USER, NEEDS TO BE RESTARTED. INITIATE a NOIS TO FOLLOW UP.
- SUCCESS: Transmission completed.
- WARNING: 10 out of 15 still have to be transmitted, please verify with the HL7 System Monitor.
- SD-PAIT Logical Link has to be started.
- Initiate a NOIS for VistA Interface Engine - communication problem.
- WARNING!!!: Transmission of run#: 12 has been repaired. Please create a NOIS to verify if the problem has been addressed
- WARNING!!!: Transmission communication problem, please review.

## Patient Class Evaluation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, only the Outpatient Encounter file (#409.68) is being used to determine the Patient Class. Sometimes, a NULL value is being transmitted (as 'U' – undetermined). Both the Visit (#9000010) and Outpatient Encounter files will now be examined to determine the appropriate Patient Class.

## Cleaning Process Performed at End of VistA Transmission Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cleaning process of the PATIENT APPOINTMENT INFO LOG file (#409.6) will be moved from the acknowledgement portion of processing to the end of the main transmission processing, and will be independent of the acknowledgements processing.

## Message for Not Allowing the Manual Transmission of PAIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the SD-PAIT TASKED TRANSMISSION is scheduled and the site attempts to run the SD-PAIT MANUAL TRANSMISSION option, the software completes a check prior to allowing the manual option to run in order to determine if the tasked job is scheduled; however, currently the code does not notify the user as to the reason it will not allow queuing.

If this situation occurs, an informational message will be displayed on the screen, immediately letting the user know why the manual transmission will not be run and also a MailMan message sent to the user explaining why queuing of the manual option: SD-PAIT MANUAL TRANSMISSION is not allowed.

The following is an example of this message received on the screen:

> Select OPTION NAME: SD-PAIT MANUAL TRANSMISSION Manual Startup PAIT Transmission

> Manual Startup PAIT Transmission

> You attempted to start PAIT outside the authorized transmission dates.

> Job has been terminated.

The following is an example of the MailMan message received by a user who tried to execute the manual transmission when the regular tasked transmission is scheduled:

> Subj: PAIT Transmission \[#1955781\] 09/17/04@13:50 3 lines

> From: POSTMASTER In 'IN' basket. Page 1 \*New\*

> -------------------------------------------------------------------------------

> USERLASTNAME,USER (DUZ=100106) attempted to start the PAIT transmission

> on Sep 17, 2004@13:50:39, outside the authorized transmission dates.

> The job has been cancelled

## Protection for Missing Entry in File \#409.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Protection will now be provided for a missing entry in the PATIENT APPOINTMENT INFO LOG file (#409.6) where an "AE" Retention Flag cross reference with a "Y" value exists, while scanning previously sent appointments.

If the entry does not exist, then the cross reference pointing to it will be deleted.

## Cancelled Appointments for Non-Count Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, if an appointment is created and then cancelled its status as a count or non-count clinic is not known. Now, additional verification is performed to determine the clinic type for canceled appointments, and if the clinic is 'NON-COUNT' it will receive 'NC' as its appointment type on the HL7 SCH message segment if it is not rescheduled, or an 'RSN' as its appointment type on the HL7 SCH message segment for appointments that are rescheduled.

## Identifying Appointments in HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option Patient HL7 Location \[SD-PAIT PATIENT HL7 LOCATION\] lists HL7 message number and sequence for a specified appointment date/time. This is useful for verification of generated and transmitted data for a particular appointment.

## Field Name Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of sub field \#2 of Patient field \#2 was changed from HL7 BATCH \# to HL7 MESSAGE ID.

Canceled Terminated Evaluation Modification

If an appointment is canceled and another one is scheduled for the same Appointment Date/Time, then the previous one's Event Reason will be Canceled Terminated, regardless of whether it was already canceled and transmitted in a previous run or if it was cancelled and transmitted in the current run with the new appointment that has the same Appointment Date/Time. This situation is automatically recognized when appointments have the same Appointment Date/Time, but different Creation Dates. The original Creation Date is retrieved from the PATIENT APPOINTMENT INFO LOG file 409.6, then overwritten in VistA by the Creation Date of the new appointment that has the same Appointment Date/Time.

### From: SD*5.3*349 PAIT Release Notes

## Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PAIT BACKGROUND JOB completion message was modified to include both Starting Date and the Last Scanned Date, and they are sent to the forum server to reflect more accurate status of the site transmission in the completion report.

## Patient Status Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modification to interpretation of the Patient Status Code.

Old version:

Table 0216 - Patient Status Codes

NTF (New To Facility)

Patient did not have a prior appointment at this facility in the past 24 months.

SHB (Seen Here Before)

Patient did have a prior appointment at this facility in the past 24 months.

The patient status code indicates if a patient is new to a facility or not. The patient

is new to the facility if he/she did not have another appointment in the same

facility during the last 24 months. The facility is determined from the Institution

file if there is a pointer to it from the Hospital Location file, through the Division pointer to the Medical Center Division, and its Institution pointer to the Institution file with its Station Number field (#99).

New version:

Table 0216 - Patient Status Codes

NSF (New to Parent and Sub Station)

Patient did not have a prior appointment at this Facility in the past 24 months

SHB (Registered Here Before)

Patient did have a prior appointment at this Parent and Sub Station in the past 24 months

OPN

Patient did not have a prior appointment at this Sub Station but was registered with Parent Station.

The patient status code indicates if a patient is new to a facility or not. Both the Parent Station and the Substations are evaluated as the facility. The parent Station is evaluated with the primary DSS ID only; the Substation is evaluated with both the DSS ID stop code and the DSS credit stop code. The patient is new to the facility if he/she did not have another scheduled appointment in the same facility during the last 24 months. The facility is determined from the Institution file if there is a pointer to it from the Hospital Location file through the pointer to the Medical Center Division from the Division field of the Hospital file.

Table 0216 - Patient Status Codes

|           |                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------|
| VALUE | DESCRIPTION                                                                                                     |
| NSF       | Patient did not have a prior appointment at this Facility in the past 24 months; New to Parent and Sub Station      |
| SHB       | Patient did  have a prior appointment at this Parent and Sub Station in the past 24 months; Registered Here Before. |
| OPN       | Patient did not have a prior appointment at this Sub Station but was registered with Parent Station.                |

## Sort Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sort Template: \[SD-PAIT PEND EXCL FUTURE\], used with option SD-PAIT PENDING has been modified to give users the ability to request a certain range of records sorted by the Appointment Date.

## Batch Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Batch Header of the HL7 acknowledgement message from station 200 was modified to request a commit acknowledgement from Vista HL7. The addition of the commit acknowledgement (CA) provides a receipt of message reception by Vista HL7 and improves internal tracking mechanisms.

BHS^~\|\\^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S12^5003236-1^D^2.4^^^AL^AL^USA

SCH^1^^^^^^4^NAT^^^\~\~~20030908\~\~~Date Appt Created\|\~\~\~\~\~~Desired Date\|\~\~~200309180800\~\~~Appt Date\|\~\~\~\~\~~Checkout Date\|\~\~\~\~\~~Cancellation Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~\~\~\~~Resched Date^^^^^^^^^^^^^^P

PID^1^^""\~\~~USVHA&&L~NI\|7171938\~\~~USVHA&&L~PI^^WOLFIK~EDZIU^^19301212^^^^\~\~\~~19107^^^^^^^^208121230P

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^422\~\~\~\~\~\~\~~CECELIA'S CLINIC^402~CARDIAC SURGERY~DSS Clinic ID^418~AMPUTATION CLINIC~DSS Credit Stop

ZEN^1^^^^^^^^5

ZSP^1^N^

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-2^D^2.4^^^AL^AL^USA

SCH^1^^^^^CC^3^RS^^^\~\~~20030829\~\~~Date Appt Created\|\~\~~20030829\~\~~Desired Date\|\~\~~200308291330\~\~~Appt Date\|\~\~\~\~\~~Checkout Date\|\~\~~200308290940\~\~~Cancellation Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~~200308291030\~\~~Resched Date^^^^^^^^^^^^^^F

PID^1^^""\~\~~USVHA&&L~NI\|7172069\~\~~USVHA&&L~PI^^YORTY~OUTPATIENT^^19710604^^^^\~\~\~~17042^^^^^^^^509060471P

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^614\~\~\~\~\~\~\~~YORTY'S CLINIC^329~MEDICAL PROCEDURE UNIT~DSS Clinic ID^\~~DSS

Credit Stop

ZEN^1^^^^^^^^1

ZSP^1^Y^60

MSH^~\|\\^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-3^D^2.4^^^AL^AL^USA

SCH^1^^^^^CP^3^RS^^^\~\~~20030829\~\~~Date Appt Created\|\~\~~20030829\~\~~Desired

Date\|\~\~~200309010815\~\~~Appt Date\|\~\~\~\~\~~Checkout Date\|\~\~~200308290856\~\~~Cancellation Date\|\~\~\~\~\~~Auto-rebook Date\|\~\~~200309010815\~\~~Resched Date^^^^^^^^^^^^^^F

PID^1^^""\~\~~USVHA&&L~NI\|7172424\~\~~USVHA&&L~PI^^VILELLA~JOEY~ASHLEY~III~MR^^19490

416^^^^\~\~\~~33354^^^^^^^^244990005

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^NTF

AIL^1^^312\~\~\~\~\~\~\~~XXXXX^102~ADMITTING/SCREENING~DSS Clinic ID^104~PULMONARY FUNCTION~DSS Credit Stop

ZSP^1^N^

BTS^3

## Batch Acknowledgement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The format of the Batch acknowledgement message was modified to conform to Vista HL7's proprietary formatting:

BHS^~\|\\^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSA^AE^5003

MSA^AE^5003-1^250

MSA^AE^5003-2^200

MSA^AE^5003-3^200

BTS^3

## Description of Error Codes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appointments sent via the Patient Appointment Information Transmission (PAIT) application can be rejected by the AAC, and if so they have specific error codes that may be found in the PCMM HL7 ERROR CODE file (#404.472). Rejected appointments can be listed by using the Rejected Transmissions \[SD-PAIT REJECTED\] option. The Rejected Transmission report should be used to review and correct patient appointment records that the AAC rejected.  Rejections can occur due to incomplete dates, invalid site/facility codes (ones that do not match the site of the sender), and for other reasons. For a particular site; see sample of REJECTED TRANSMISSION LOG report below. For a list of rejection codes and their definition see table AAC001 - Error Code Set in the SD\*5.3\*333 Release Notes. A site should use this report for correcting their patient appointment records.  Once the site has corrected the record it will be sent to the National Data Base in the next bi-monthly update run and loaded into the National Database.  The correction of rejected records is the VistA site's responsibility. If the rejected record is not corrected it is sent again by the PAIT application with the next scheduled or executed PAIT, and it may be rejected again.

 

### Error 100

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PATIENT DFN IS NOT NUMERIC OR IS MISSING:

> DFN, or internal entry number of a patient in the Patient File is missing or not a number. Most likely the result of a HL7 transmission formatting error. Requires no intervention or correction at site level the first time the error occurs. The record will be re-transmitted. If error persists initiate NOIS and/or call the National Help Desk.

### Error 150

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CLINIC IEN IS NOT NUMERIC OR IS MISSING:

> Clinic IEN, or internal entry number of the Clinic in Hospital Location File is missing or not a number. Most likely the result of a HL7 transmission formatting error. Requires no intervention or correction at site level the first time the error occurs. The record will be re-transmitted. If error persists initiate NOIS and/or call the National Help Desk.

### Error 200 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BHS STATION NUMBER AND STA3N ARE NOT EQUAL:

> Error 200 indicates that the Hospital Location of a particular appointment is set up with an Institution whose Station Number field doesn't match the sending facility number. The Institution is identified from the Medical Center Division file (# 40.8) pointed to by the Division field (# 3.5) of the Hospital Location file (#44). The first three digits of the station number have to match the sending VistA facility number. The site has to find if the Station Number in the Institution is incorrect or another Institution has to be set up with the Medical Center Division of the Hospital file. If the Institution field of the Medical Center Division file is not null it is treated as a designated location of that appointment. The PAIT retrieves the Institution and its Station Number, following the Division field pointing to the Medical Center Division file, and its Institution File Pointer field (# .07). IRM should direct this issue to whomever is responsible for set-up of the Hospital Location file. If the issue cannot be solved locally a Remedy ticket has to be initiated and/or the National Help Desk notified.

### Error 250

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INVALID OR MISSING BHS STATION NUMBER:

> HL7 site parameters are incorrect. Initiate NOIS and/or call the National Help Desk.

### Error 300 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INVALID OR MISSING STA3N:

> Error similar to 250. It indicates that the Station Number field (# 99) identified from the Institution is null or its first three characters do not match the facility 3 digits number. Allow the record to be re-transmitted. If error persists initiate NOIS and/or call the National Help Desk.

### Error 350

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING:

 

> Error 350 is mostly caused by too old desired date of appointment or bogus date of appointment itself, filed in VistA sub file 1900 of the Patient File. IRM has to address this issue consulting the Scheduling team. If no evidence can be found initiate NOIS and/or call the National Help Desk.

Example:

Error 350 would have to be evaluated by a person having programming access and authority to repair data. Please note the following examples:

\(1\) DFN 105723 error for 12/1/2004 \<= CORRECTED

^DPT(105723,"S",3041201.133,0) = 5142^^^^^^3^^^^^^^^^9^^^

3040315^^^^^0^O^0

^DPT(105723,"S",3041201.133,1) = 1200104^1 \<= incorrect date

^DPT(105723,"S",3041201.133,1) = 3041201^1 \<= corrected

\(2\) DFN 41221 error 10/11/2004

^DPT(41221,"S",3041011.1018,0) = 1072^C^^^^^3^^^^^34131

^^3031014.0845^11^9^^3413

1^3031014^^^^^0^O^0

^DPT(41221,"S",3041011.1018,1) = 3041011^1 \<= appears correct

^DPT(41221,"S",3041011.1018,"R") = error

from the Hospital Location file (#44)

^SC(1072,"S",3041011.1018,0) = 3041011.1018

^SC(1072,"S",3041011.1018,1,0) = ^44.003PA^^

You may have to look into a related appointment that was

made on the original appointment's cancellation

date, please see below:

Global ^DPT(41221,"S",1011103.1018

^DPT(41221,"S",1011103.1018,0) = 1072^^^^^^3^^^^^^^^^9^^^3031014

^^^^^0^^0

^DPT(41221,"S",1011103.1018,1) = 1011103^1

Patient DFN 41221 has appt. date 11/03/1801 - not correct.

\(3\) DFN 85462 error 12/2/2003 \<= CORRECTED

^DPT(85462,"S",3031202.13,0) = 1048^^^^^Y^3^^^^^^3031202

^^^9^^^3030915^15323851^^^^0^O^0

^DPT(85462,"S",3031202.13,1) = 1200203^0 \<= incorrect date

^DPT(85462,"S",3031202.13,1) = 3031202^0 \<= corrected

^DPT(5385215543,"S",1120303.13,0) = 4532^C^^^^^3^^^^^40347

^^3031105.1110^11^9^^40347^3031105^^^^^0^^0

^DPT(5385215543,"S",1120303.13,1) = 3031112^1

^DPT(5385215543,"S",1120303.13,"R") = error

from File \#44

^SC(4532,"S",1120303.13,0) = 1120303.13

^SC(4532,"S",1120303.13,1,0) = ^44.003PA^^

\(4\) DFN 42092 error 12/22/2003 CORRECTED

^DPT(42092,"S",3031222.14,0) = 5175^C^^^^^3^^^^^38323

^^3031124.1512^11^9^^38323^3031124^^^^^0^O^0

^DPT(42092,"S",3031222.14,1) = 1201203^1 \<= incorrect date

^DPT(42092,"S",3031222.14,"R") = WRONG DATE

^DPT(42092,"S",3031222.14,1) = 3031222^1 \<= corrected

### Error 400 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOB IS MISSING OR INVALID:

> Site staff should examine demographics of Patient for an invalid or missing date of birth and correct.

### Error 450 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CREATE DATE OR APPT DATE IS MISSING:

> Each generated appointment must have the Creation Date. Site should verify an entry in 409.6 file checking the DATE APPT MADE field. If that field exists, allow the record to be re-transmitted. If error persists initiate NOIS and/or call the National Help Desk.

### Error 500

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CREATION DATE IS BEFORE SEPTEMBER 1, 2002

> PAIT evaluates appointments based on the Creation Date before Sep 1<sup>st</sup> 2002. Site should verify an entry in 409.6 file checking the DATE APPT MADE field. If its value shows a date before Sep 1<sup>st</sup> 2002 initiate NOIS and/or call the National Help Desk, otherwise allow the record to be retransmitted and if the error persists initiate NOIS or/and call the National Help Desk.

### Error 600

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT

> Please refer to description of Appointment Type: RS – Rescheduled in chapter 4.0 Appointment Selection Logic of SD\*5.3\*333 Release Notes. If the Rescheduled Date was identified the Appointment Type must be 'RS'.

> No site intervention is required, initiate NOIS and/or call the National Help Desk.

### Error 650

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT

> The Event Reason: 'CO' or 'COE' require the Check Out Date to be included with

> a transmitted appointment. No site intervention is required, initiate NOIS and/or call the National Help Desk.

### Error 700

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT

> The Cancellation Date requires the Event Reason to be either 'CC', 'CP' , 'NS' or 'CT. Please refer to SIU Event Mapping Table in chapter 4.0 Appointment Selection Logic of SD\*5.3\*333 Release Notes. Appointment Type 'CT' may be also sent without the Cancellation Date if a new appointment that overrode the original one is still 'pending'. Initiate NOIS and/or call the National Help Desk if no solution is evident.

### Error 750

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT

> Review SIU Event Mapping Table in chapter 4.0 Appointment Selection Logic of SD\*5.3\*333 Release Notes to see the indicated relation. . Initiate NOIS and/or call the National Help Desk if no solution is evident.

### Error 800

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FILLER STATUS IS MISSING OR IS INVALID

Each appointment record must have the Filler Status that corresponds to either

'pending' or 'final' value. Initiate NOIS and/or call the National Help Desk.

### Error 850

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADMIT TYPE IS INVALID (table SD009)

Patch SD\*5.3\*446 was released with a new sequence - Admission Type, see below, to be accepted in Austin.

PV1 - Patient Visit Segment

----------------------------

SEQ LEN DT TBL# ELEMENT NAME VISTA DESCRIPTION

---------------------------------------------------------------------------------------------------------------

4 4 ID 0007 Admission Type Refer to Table SD009

(Purpose of Visit)

For a list of valid types see table SD009 - Purpose of Visit & Appointment Type in the SD\*5.3\*333 Release Notes.

Austin set up a new rejection code 850 - 'Admit type is invalid (table SD009)'

on their site that corresponds to the code in the PCMM HL7 ERROR CODE file (#404.472).

IF ADMIT_TYPE NOT IN ('0101','0102','0103','0104','0105','0106',

'0107','0108','0109','0111','0201','0202','0203','0204','0205',

'0206','0207','0208','0209','0211','0301','0302','0303','0304',

'0305','0306','0307','0308','0309','0311','0401','0402','0403',

'0404','0405','0406','0407','0408',

'0409','0411',' ')

THEN ERR_CODE = '850';

The report from the Rejected Transmissions \[SD-PAIT REJECTED\] option will list any entry with rejection code '850'. Like the other errors on that report, it needs to be investigated and the appointment retransmitted (in this case, the valid Purpose of Visit and Appointment Type need to be determined). Sites must not create their own local appointment types because ones not on the table will be rejected.

### Error "R"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WHOLE BATCH REJECTED:

> The whole batch rejection from the AAC has not been implemented at this time and will be future enhancement but a manual rejection may be implemented if needed. No action at all has to take place because there was a problem with accepting the whole batch. The batch will be retransmitted, no action is needed.

## Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message generated at the end of generated appointment batches in a VistA facility, and it will contain additional information regarding the Started and the Last Scanned Date:

> Subj: 656 - PAIT BACKGROUND JOB  \[#5277039\] 04/22/04@16:06  13 lines

> From: POSTMASTER  In 'IN' basket.   Page 1  \*New\*

> ----------------------------------------------------------------------- 

> The PAIT job has completed - TASK \#: 8949063 Log \#: 2 on 4/22/04@16:05

> Started: 4/22/04                        Last Scanned: 4/21/04

> Pending appointments:      33411

> Final appointments:        63586

>                        ----------

> Total appointments:        96997   Number of batches: 20

> Fac Log Bch Appt \#  Date finished  IP Address  Gen  Sent Com R Com P  Status

> -----------------------------------------------------------------------

> 656\|  2\| 20\|  96997\|4/22/04@16:05\|10.104.10.89\| 379\| 378\| 378\| 378\| Inactive

> WARNING: 1 out of 20 batches have to be still transmitted. This message might be generated when HL7 transmission is still in process.

## PAIT Trouble shooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful completion of the bi-monthly PAIT transmission, members of the SDPAIT mail group should receive a PAIT BACKGROUND JOB MailMan message confirming success. It is the site's responsibility to initiate a NOIS if this message is not received after the scheduled task finishes or if an error is found in the error log. The site should first check the error log, looking at the time when the PAIT task terminated, and call the <span class="mark">REDACTED</span>.

> All completion messages are also sent to the Forum server where HSD&D and EVS can verify that the reported transmission has finished. If an error or problem occurs, IRM should not start the next PAIT task until HSD&D or EVS staff review the problem and take or advise corrective action.
