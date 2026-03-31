---
consolidated_title: "pait release notes"
app_code: PAIT
doc_type: release-note
master_source: "SD*5.3*333 PAIT Release Notes"
master_pub_date: March 2004
consolidated_from: 3 versions
prior_versions:
  - "SD*5.3*349 PAIT Release Notes"
  - "SD*5.3*376 PAIT Release Notes"
---

Patient Appointment Information Transmission (PAIT)

Release Notes and Installation Guide

*5.3*333

March 2004


Health Systems Design and Development

This page left blank intentionally

Revision History

| **Date**   |   **Revision** | **Description**              | **Author**   |
|------------|----------------|------------------------------|--------------|
| 1.28.2004  |           1    | Version 1                    | REDACTED     |
| 1.28.2004  |           1.1  | Revisions                    | REDACTED     |
| 1.29.2004  |           1.2  | Revisions                    | REDACTED     |
| 2.2.2004   |           1.3  | Revisions                    | REDACTED     |
| 2.3.2004   |           1.4  | Revisions                    | REDACTED     |
| 3.1.2004   |           1.5  | Revisions                    | REDACTED     |
| 3.2.2004   |           1.6  | EVS trouble shooting         | REDACTED     |
| 3.3.2004   |           1.7  | Revisions                    | REDACTED     |
| 3.4.2004   |           1.8  | Revisions                    | REDACTED     |
| 7.10.2006  |           1.9  | Corrections                  | REDACTED     |
| 7.12.2006  |           1.91 | Document Review              | REDACTED     |
| 12.4.2008  |           1.92 | Changes for patch SD*5.3*528 | REDACTED     |
| 1.5.2009   |           1.93 | Changes for patch SD*5.3*534 | REDACTED     |
|            |                |                              |              |
|            |                |                              |              |
|            |                |                              |              |
|            |                |                              |              |

This page left blank intentionally

Table of Contents

Introduction	7

Description of Functionality	7

Changes introduced with SD*5.3*333 patch	8

**Table VA087 -  Scheduling Event Reason	10**

**Table 0276 - Appointment Reason Codes	11**

**2.3.9 SCH Schedule Activity Information	11**

**Table VA0021 – Enrollment Priority	11**

**Table  0277 - Appointment Type Codes	12**

**Table AAC001 - Error Code Set	13**

Installation	14

Post Installation Instructions	18

User Options	23

MailMan Messages	24

Technical Information	25

**Initial Seeding Run Times:	27**

Appendix  A – HL7 Specifications	28

**Introduction	28**

**General	28**

**1.2 Message Content	28**

**1.2.0 Data Capture and Transmission	31**

**1.2.1 Batch Messages	32**

**1.2.2 Batch Acknowledgements	32**

**1.2.3 Lower Level Protocol	32**

**2  HL7 Control Segments	33**

**2.1 Message Definitions	33**

**2.2 Segment Table Definitions	33**

**2.3 Message Control Segments	33**

**2.3.1 MSH - Message Header Segment	34**

**2.3.2  BHS – Batch Header Segment	35**

**2.3.3 BTS - Batch Trailer Segment	36**

**2.3.4 PID - Patient Identification Segment	36**

**2.3.4 PID - Patient Identification Segment  (continued)	37**

**2.3.5 PV1 - Patient Visit Segment	37**

**2.3.7 AIP - Appointment Information - Personnel Resource Segment	40**

**2.3.8 AIL Appointment Information	41**

**2.3.9 SCH Schedule Activity Information	42**

**2.3.10 ZCL - VA-Specific Outpatient Classification Segment	43**

**2.3.11 ZEN - VA-Specific Enrollment Segment	43**

**2.3.12 ZSP - VA-Specific Service Period Segment	43**

**3.0 SUPPORTED AND USER-DEFINED HL7 TABLES	44**

**Table 0003 - Event type	44**

**Table 0004 – Patient Class	44**

**Table 0008 - Acknowledgment Code	44**

**Table 0076 - Message Type	44**

**Table 0216 - Patient Status Codes	45**

**Table 0276 - Appointment Reason Codes	45**

**Table  0277 - Appointment Type Codes	45**

**Table 0278 Filler Status Codes	46**

**Table VA01 - Yes/No	46**

**Table SD008 - Outpatient Classification Type	46**

**Table SD009 - Purpose of Visit &amp; Appointment Type	46**

**Table VA0021 – Enrollment Priority	47**

**Table VA087 -  Scheduling Event Reason	48**

**Table AAC001 - Error Code Set	48**

**Table VA088 – DSS ID and DSS Credit Stop	49**

**4.0 Appointment Selection Logic	59**

**4.1 Acknowledgement Processing Logic	61**

**4.2 Whole Batch Accept	62**

**4.3 Whole Batch Reject	62**

**4.4 Whole Batch Accept with Rejections	62**

**4.5 Rejected Appointments Processing	62**

**5.0 Messages Examples	64**

Appendix B - VistA Interface Engine Site I.P. Addresses	65

Appendix C – Trouble Shooting	66

**Mail Notifications	66**

**HL7 System Monitor	67**

**VistA Interface Engine	68**

**XTMP Global	68**

VistA Reporting	68

National Help Desk Reporting	78

VistA Communication Problems	82

## Introduction

This patch contains several enhancements, modifications and a fix to the Patient Appointment Information Transmission, originally released in patch SD*5.3*290. A post install routine will delete all previous seeding and update data from file 409.6 and a new seeding run will be activated.

Data from all pending appointments within the range 9.01.2002 to present and data for final appointments, that meet specified criteria, beginning 9.01.2003 will be wrapped in HL7 batch messages and transmitted to the Austin Automation Center (AAC).

This additional data supplements the existing Clinic Appointment Wait Time extracts 1 &amp; 2.  At this time those extracts should continue to be transmitted on the 5 th and 31 st of each month as originally designated in SD*5.3*193.  Further instructions will be provided when those transmissions will no longer be necessary.

The One –Time Option Queue from the Taskman Management menu will be used to start SD-PAIT TASKED TRANSMISSION on a scheduled date. Subsequent updating transmissions will be scheduled on 1 st and 15 th day of each month.  The frequency of transmission may change based on reporting needs.

## Description of Functionality

A bi-monthly  Taskman  job will collect and format data for HL7 batch transmission.

A set number of appointments, maximum of  5000,  is collected in a temporary file. This file is used to create a HL7 batch transmission.  After the batch data has been moved to the HL7 processing queue the temporary file is deleted and the process of generating data for transmission continues until all required data is generated and transmitted. The design allows for an immediate transmission after generation of partial data, and prevents the temporary file from becoming too large. The process is repeated until all required data is generated and transmitted.

Follow up transmissions begin scanning appointment data  created from the day following the last scanned date saved at the end of each transmission in the last Scanned Date field (# 1.2) of the  PATIENT APPOINTMENT INFO LOG file. Appointment statuses of previously transmitted data is also checked for final status values, (see SCH.25 Filler Status in the Interface Appendix).  Entries in file 409.6 sent with the final status will be deleted after an HL7 acknowledgement of the successful transmission is received.

## Changes introduced with SD*5.3*333 patch

This patch contains significant enhancements, modifications and a fix to the Patient Appointment Information Transmission - PAIT. The majority of enhancements are related to message transmission and tracking.

The transmission process involves several steps and makes use of new technology – the VistA Interface Engine .

- Transmission to a local VistA Interface Engine

- Transmission to the clustered Interface Engine at the AAC

- Transmission and conversion of data to the AAC to create SAS files

A thorough review of all steps and the quality of data pointed us to the

following enhancements, modifications and a fix:

1.	Utilization of the server functionality of VA Mailman and creation of

a server option on Forum that will receive PAIT and AAC messages related to transmission and acknowledgements.  Selected data elements from transmission and acknowledgement messages are parsed and filed in the PAIT TRANSMISSION LOG file (# 409.8) hosted on Forum. Report options provide transmission verification and history for all VA sites.

Field			Description

DATE/TIME	 	the date/time a transmission mail message

is received by the FORUM server option

SD-PAIT **-** SERVER

MESSAGE TYPE	 this field records the type of message received:

A -  Site Batch acknowledgement

B -  Site Background job transmission completion

M - Missing sites report FROM AAC

T –Transmitted sites report from AAC

SITE NUMBER	a unique three digits facility site number

LOG NUMBER	the log entry number of the transmission;

this is the run entry number of the

PATIENT multiple field in file 409.6

RUN COMPLETION DATE	the date/time of the completed

transmission; this is the TRANSMISSION

FINISHED field (#1.5) of 409.6 file

# OF BATCHES			the number of batch messages transmitted

from the site.

# OF APPOINTMENTS		the number of appointments included in

all created batches.

IP ADDRESS			the IP address of the Vitria Interface

Engine set up at the PAIT transmission

site.

BATCHES GENERATED		the number of HL7 messages generated by

the PAIT transmissions and recorded in

SD-PAIT Logical Link; this number may include

batches from the previous transmissions.

BATCHES SENT			the number of HL7 messages sent to the

local Interface Engine and recorded in the

SD-PAIT Logical Link.

STATUS				the status indicated by a received

Message A or B:

A – status of the acknowledgement completion

B – status of the SD-PAIT Logical Link at the end of transmission

HL7 MESSAGE ID			This field records the HL7 Message ID of

received acknowledgement.

BATCH CONTROL ID		This field records the HL7 Batch ID of

received acknowledgement.

RUN ACK STATUS		the ACK Status - the number ACK's received

by HL7 vs the number of messages (batches) sent .

ACKS COMPLETE		this field is marked YES if all ACK's for

a PAIT transmission are received.

2. Detailed information related to each transmission will be permanently stored in file 409.6

Field		Description

1.3		# OF APPOINTMENTS

1.4		# OF BATCHES

1.5		TRANSMISSION FINISHED

2		PATIENT	&lt;-Mult [409.69P

9		CLINIC  - pointer to the HOSPITAL LOCATION file

3		BATCH TRACKING	&lt;-Mult [409.7A]

01		BATCH CONTROL ID

02		BATCH CREATE DATE/TIME

03		MESSAGE CONTROL ID

04		APPLICATION ACK DATE/TIME

05		APPLICATION ACK TYPE

3. New report options for the site to print both the Transmission Summary and Acknowledgement Summary.

4.. New option SD-PAIT MANUAL BATCH REJECT to be used if a batch was

not accepted by the AAC, was sent from  and the whole batch rejection

has not been received.

> **NOTE:** In a future enhancement it is  anticipated to generate the whole batch rejection from the AAC, after comparison of batch control number ID, sent                      from  with received by the AAC.

5.  To enhance the quality of data the following changes are introduced:

New components are added to SCH.11, SCH6, and SCH.7 segments of

HL7 transmission.

### ### ### ### Table VA087 -  Scheduling Event Reason

| VALUE   | DESCRIPTION              |
|---------|--------------------------|
| CI      | Check-in                 |
| CO      | Check-out                |
| NS      | No Show                  |
| CC      | Cancel by clinic         |
| CP      | Cancel by patient        |
| COE     | Check-out by encounter   |
| NM      | No Match                 |
| **CT**  | **Cancelled Terminated** |

**CT** is the Event Reason to finalize an appointment that was sent as pending and then, during the update process a new appointment is created for the same date and time. That situation caused the previous appointment record to be overridden by the new appointment record with a new creation date.

### Table 0276 - Appointment Reason Codes

|   VALUE | DESCRIPTION                                     |
|---------|-------------------------------------------------|
|       1 | Next Ava. Appt. Indicated by User               |
|       2 | Next Ava. Appt. Indicated by Calculation        |
|       3 | Next Ava. Appt. Indicated by User & Calculation |
|       4 | Not Next Available with AutoRebook              |
|       5 | Not Next Available No AutoRebook                |
|       6 | Null (All others)                               |

Appointment Reason Code table includes new six values instead of  the previous

“N” and “A” only.  It will allow for more detailed sorting criteria, especially when

calculating the next available time.

### ### SCH Schedule Activity Information

|   **SEQ** |   **LEN** | **DT**   | **R/O/C**   | **RP/#**   | **TBL#**   |   **ITEM#** | **ELEMENT NAME**            | **DESCRIPTION**                                                                                                                                                                                      |
|-----------|-----------|----------|-------------|------------|------------|-------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 |        75 | EI       | R           |            |            |       00860 | Placer Appointment ID       | Sequential Number                                                                                                                                                                                    |
|        11 |       200 | TQ       | O           | Y          |            |       00884 | Appointment Timing Quantity | In the following order:  Date Appt Created  Desired Date  Appt Date (time)  Checkout Date (time)  Cancellation Date (time)  Auto-rebook Date (time)  Resched Date(time)  Consult Request Date (time) |

**Resched** (uled) **Date  (time)** was added as the scheduled Appointment Date/Time of the appointment created as a continuation of previously canceled appointment. This components is always sent when the RS – Re-scheduled Appointment Type is identified. Including that new component will help to identify the follow-up appointments in the AAC.

**Consult Request Date (time)** was added as a new sequence identifying an optional date/time of the consultation if there is one associated with the appointment.

### Table VA0021 – Enrollment Priority

|   VALUE | DESCRIPTION   |
|---------|---------------|
|       8 | Priority 8    |

The indicated change applies only to the table description, the indicated value was used before.

### Table  0277 - Appointment Type Codes

| VALUE   | DESCRIPTION   |
|---------|---------------|
| O       | Outpatient    |

The indicated change applies only to the table description, the indicated value was used before.

### The logic of generating appointments from the update runs has been modified to start from scanning newly created records and then to update the previous pending appointments, if applicable. Also the last scanned date is the last date before the start of transmission, to avoid possible duplications.

The message generated at the end of transmission will contain additional information.

Subj: 500 - PAIT BACKGROUND JOB  [#151708] 01/23/04@11:32  lines

The PAIT job has completed - TASK #: 60720 Log #: 1 on 1/23/04@11:32

Pending appointments:        10054

Final appointments:           1534

-----------

Total appointments:          11588 Number of batches: 3

Fac Log Bch Appt #  Date finished  IP Address  Gen  Sent Com R Com P  Status

-----------------------------------------------------------------------

500|  1|  3|  11588|1/23/04@11:32|10.88.63.68|   7|    6|    6|    6| Enabled

This message  will be sent also to S.SD-PAIT- [SERVER@FORUM.VA.GOV](mailto:SERVER@FORUM.VA.GOV) and to the National Help Desk, if number of generated and sent batches indicates that there is potential problem in communication between  site and its local Interface Engine. In this situation additional warning messages may be sent.

7.	Error codes for a possible rejection have been evaluated, modified and added by the AAC. The increased number of error code forced us to use a pointer to the PCMM Error Code file with adding the codes related to the PAIT.

### Table AAC001 - Error Code Set

| VALUE   | DESCRIPTION                                                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 100     | PATIENT DFN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                           |
| 150     | CLINIC IEN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                            |
| 200     | BHS STATION NUMBER AND STA3N ARE NOT EQUAL                                                                                                                                                                                         |
| 250     | INVALID OR MISSING BHS STATION NUMBER                                                                                                                                                                                              |
| 300     | INVALID OR MISSING STA3N                                                                                                                                                                                                           |
| 350     | HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING.                                                                                                                                                                                    |
| 400     | DOB IS MISSING OR INVALID                                                                                                                                                                                                          |
| 450     | CREATE DATE OR APPT DATE IS MISSING                                                                                                                                                                                                |
| 500     | CREATION DATE IS BEFORE SEPTEMBER 1, 2002                                                                                                                                                                                          |
| 600     | RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT - Rescheduled date requires SCH.8 Appt type = ‘RS’ and vice versa                                                                                                              |
| 650     | CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT - Check out date requires either SCH.6 Event reason = ‘CO’ or ‘COE’                                                                                                           |
| 700     | CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT - Cancellation date requires SCH.6 Event reason = ‘CC’ or ‘CP’ or ‘NS’                                                                                                     |
| 750     | EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT - All SCH.6 Event reason codes, except ‘CI’ require SCH.25 Filler status to be ‘F’ Final and accordingly only ‘CI’ and NULL should have SCH.25 Filler status to be ‘P’ Pending |
| 800     | FILLER STATUS IS MISSING OR IS INVALID                                                                                                                                                                                             |
| 850     | ADMIT TYPE IS INVALID (table SD009)                                                                                                                                                                                                |
| R       | WHOLE BATCH REJECTED                                                                                                                                                                                                               |

R – Whole Batch Reject may be used with the manual batch rejection.

8.  Application acknowledgements will be recognized by messages sent both to a local SD-PAIT Mail Group and to S.SD-PAIT- [SERVER@FORUM.VA.GOV](mailto:SERVER@FORUM.VA.GOV)

9.  New and updated SORT/PRINT TEMPLATES (See Technical Information).

10.   Independent reports, reflecting the transmission status, have been

developed both by the AAC and Messaging and Interface Services Team.

11. Conversion data to HL7 formats have been verified and corrected.

12. The Release Notes have been updated with additional, detailed, functional

and technical information.

## Installation

This patch has **POST INSTALL INSTRUCTIONS** that must be completed.

Documentation, Release Notes &amp; Installation Guide:

SD\_53\_P333\_RN.PDF

KIDS Host File:

SD\_53\_P333.KID

The preferred method is to FTP the file from:

download.vista.med.va.gov

which will transmit the files from the first available FTP server.

The files may also be downloaded directly from a particular FTP

location at the following locations.

REDACTED

REDACTED

REDACTED

REDACTED

This patch may be installed with users on the system.  Installation will take less than 2 minutes.

Use the ‘LOAD A DISTRIBUTION’ option on the KERNEL

INSTALLATION &amp; DISTRIBUTION menu. The host file name is

SD\_53\_P333.KID.  Answer YES to the question: ‘Want to Continue with the

Load? YES//’]

Review your mapped set.  If any of the routines listed in the

ROUTINE SUMMARY section are mapped, they should be removed

from the mapped set at this time.

From the Kernel Installation and Distribution System Menu, select

the Installation menu.

From this menu, you may elect to use the following options

(when prompted for INSTALL NAME, enter SD*5.3*333):

Backup a Transport Global – this option will create a backup

message of any routines exported with the patch.  It will NOT

backup any other changes such as DDs or templates.

Compare Transport Global to Current System  - this option will

allow you to view all changes that will be made when the patch

is installed.  It compares all components of the patch (routines,

DDs, templates, etc.).

Verify Checksums in Transport Global – this option will

allow you to ensure the integrity of the routines that are in

the transport global.

Print Transport Global – this option will allow you to view the

components of the KIDS build.

Use the Install Package(s) option and select the package SD*5.3*333.

Select Installation Option: 6  Install Package(s)

Select INSTALL NAME:    SD*5.3*333   Loaded from Distribution MM/DD/YYYY

=&gt; SD*5.3*333

This Distribution was loaded on MM/DD/YYYY with header of

SD*5.3*333

It consisted of the following Install(s):

SD*5.3*333

Checking Install for *5.3*333

Incoming Files:

404.472   PCMM HL7 ERROR CODE  (including data)

> **NOTE:** You already have the 'PCMM HL7 ERROR CODE' File.

I will OVERWRITE your data with mine.

409.6     PATIENT APPOINTMENT INFO LOG

> **NOTE:** You already have the 'PATIENT APPOINTMENT INFO LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install	Press Return.

If routines were unmapped as part of step 2, they should be returned

to the mapped set once the installation has run to completion.

SD-PAIT REPORTS  option  is a stand alone menu and should be assigned to the appropriate users who monitor patient appointment wait times.  SD-PAIT MANUAL TRANSMISSION should be assigned to an IRM staff member or HAS ADPAC.

Sample Installation:

Select Installation Option: INstall Package(s)

Select INSTALL NAME: SD*5.3*333 Loaded from Distribution 1/28/04@14:32:01

=&gt; SD*5.3*333

This Distribution was loaded on Jan 28, 2004@14:32:01 with header of

SD*5.3*333

It consisted of the following Install(s):

SD*5.3*333

Checking Install for *5.3*333

Incoming Files:

404.472   PCMM HL7 ERROR CODE  (including data)

> **NOTE:** You already have the 'PCMM HL7 ERROR CODE' File.

I will OVERWRITE your data with mine.

409.6     PATIENT APPOINTMENT INFO LOG

> **NOTE:** You already have the 'PATIENT APPOINTMENT INFO LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   UCX/TELNET

Install Started for SD*5.3*333 :

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

SD*5.3*333

─────────────────────────────────────────────────────────────────────────────

Installing PROTOCOL

Installing OPTION

Jan 28, 2004@14:37:21

Updating Routine file...

Updating KIDS files...

SD*5.3*333 Installed.

Jan 28, 2004@14:37:21

Install Message sent #1852746

─────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100%    │             25             50             75               │

Complete  └────────────────────────────────────────────────────────────┘

Install Completed

## Post Installation Instructions

Run Post Init Routine SDP333P

From the programmer prompt run routine SDP333P

BAY&gt;D ^SDP333P

SD*5.3*333 POST INIT

Clean-Up file 409.6? NO// ?

ATTENTION:  Answering 'YES' will delete all entries from file 409.6

(Patient Appointment Information Transmission).  This is CORRECT

for a first installation of the patch.  If you are re-installing the

patch and want to keep the entries in 409.6 answer 'NO'

If this is the first installation of the patch answer 'YES'

Clean-Up file 409.6? NO// YES

PAIT Clean-UP Task Submitted.  Task number: nnnnn

Members of the SD-PAIT mail group will receive a notification message

when the clean-up job has completed.

Example Mail Message:

Subj: PAIT Clean-Up  [#152206] 02/03/04@10:25  3 lines

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

-------------------------------------------------------------------------------

The PAIT Clean-Up, task #nnnnn, from the post installation

of SD*5.3*333 has completed.  You may resume post installation activities.

Enter message action (in IN basket): Ignore//

Post init routine, SDP333P, may be deleted after clean-up has completed.

Insure the SD-PAIT logical link is **ENABLED** :

Select HL7 Main Menu Option:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM     Systems Link Monitor

FM     Monitor, Start, Stop Filers

LM     TCP Link Manager Start/Stop

SA     Stop All Messaging Background Processes

RA     Restart/Start All Links and Filers

DF     Default Filers Startup

SL     Start/Stop Links

PI     Ping (TCP Only)

ED     Link Edit

ER     Link Errors ...

Select Filer and Link Management Options Option: SL  Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device.  Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: SD-PAIT

This LLP has been enabled!

Edit the new SD-PAIT logical link:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Interface Developer Options

EA     Application Edit

EP     Protocol Edit

EL     Link Edit

VI     Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL  Link Edit

Select HL LOGICAL LINK NODE: SD-PAIT

Enter the TCP/IP ADDRESS of your  Interface Engine

See Appendix B to determine your sites I.P. Address for the Interface Engine.

Enter the  – 9270

To begin the initial March 15 th seeding run use Taskman option “One-time Option Queue” and select option SD-PAIT TASKED TRANSMISSION.

When prompted ‘Does this option need a DEVICE? NO//’ press return.

When prompted ‘Enter Particular Volume set if needed:’ press return.

When prompted ‘Requested Start Time: NOW//’ press return.  Optionally, you may elect to schedule the initial seeding run to begin during off peak hours.

**The initial seeding run will be executed only once, on March 15, 2004.**

Using Taskman option Schedule/Unschedule Options schedule option SD-PAIT TASKED TRANSMISSION to run the 1 st and 15 th of every month.  It is important to schedule the first tasked run to begin on 4.01.2004 (time is site selectable).  This establishes the bi-monthly transmission schedule with the first transmission taking place on 4.01.2004

If your TASKED TRANSMISSION does not start on the 1 st or 15 th contact the National Help Desk (1 888 596 4357) before re-scheduling the transmission on a day other than the 1 st or the 15 th .

A MailMan message addressed to the SD-PAIT mail group will confirm     completion of the tasked job.

## User Options

Option “SD-PAIT REPORTS       PAIT Reports Menu” provides four reports:

SD-PAIT PENDING                                       Pending Transmissions

SD-PAIT REJECTED                                     Rejected Transmissions

SD-PAIT ACK SUMMARY                            Acknowledgement Summary

SD-PAIT TRANSMISSION SUMMARY       Transmission Summary

Pending Transmissions will list all transmitted HL7 messages whose status is Pending, but not designated as a future appointment.  This report is a diagnostic tool useful for follow-up of inpatient appointments that have not been dispositioned.

Rejected Transmissions will list all transmitted HL7 messages that have been rejected by the AAC.  The AAC will reject messages in which the data is not correctly formatted.   Entries on this list warrant a review by the MAS ADPAC to validate patient demographic data.

Acknowledgement Summary  lists all batches in Batch Control ID order.  The report also indicates the Message Control ID, the Acknowledgement Date, and Acknowledgement Type.

Transmission Summary report may be used to determine the total number of patient appointment records, the run date, total number of batches, Batch Control ID, Message Control ID, and date/time stamp.

Option “ SD-PAIT MANUAL TRANSMISSION     Manual Startup PAIT Transmission” can be used to start a transmission if needed

## MailMan Messages

MailMan notification messages are generated for two events.

1. Background processing has completed:

Subj: 500 - PAIT BACKGROUND JOB  [#151708] 01/23/04@11:32  lines

The PAIT job has completed - TASK #: 60720 Log #: 1 on 1/23/04@11:32

Pending appointments:        10054

Final appointments:           1534

-----------

Total appointments:          11588 Number of batches: 3

Fac Log Bch Appt #  Date finished  IP Address  Gen  Sent Com R Com P  Status

-----------------------------------------------------------------------

500|  1|  3|  11588|1/23/04@11:32|10.88.63.68|   7|    6|    6|    6| Enabled

You may monitor HL7 message transmission using option Systems Link Monitor from the HL7 Main Menu and viewing link SD-PAIT

Legend:

Fac           -  Site Facility Number

Log           - Run number

Bch           - Number of generated batches

Appt #        - Number of Appointments

Date finished - Date/time when the transmission has finished

IP Address    - IP Address of HL Logical Link "SD\_PAIT"

Gen           - Number of batches generated ( including previous transmissions)

Send          - Number of all sent batches (including previous transmissions)

Com R         - Number of Commit Ack Received

Com P         - Number of Commit Ack Processed

Status        - Status of 'SD-PAIT" link at the end of transmission

2.  Batch acknowledgement message from the AAC is received by the local HL7 package:

Subj: PAIT BATCH ACKNOWLEGEMENT 442179  [#1407] 01/29/04@12:18  9 lines

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

-------------------------------------------------------------------------------

Station Number: 442

Batch Control ID: 442179

Message ID: 442179

Log Entry: 2

Run Date: Jan 29, 2004@10:02:27

Status: Acknowledged - with rejections

1 of 1 ACKs received for this run date

Use option SD-PAIT REJECTED  Rejected Transmissions to view the rejections.

Subj: PAIT BATCH ACKNOWLEGEMENT  [#9418309] 10/28/03@13:38  1 line

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

-----------------------------------------------------------------------------

Batch 64918243649 has been acknowledged.  There were no rejections.

## Technical Information

**SD*5.3*333 Imports the following components:**

**POST-INIT ROUTINE**

SDP333P  (May be deleted after install)

**FILES - updated**

- 409.6. PATIENT APPOINTMENT INFO LOG

404.472   PCMM HL7 ERROR CODE FILE

**GLOBALS**

^SDWL(409.6

^SCPT(404.472,

**NEW AND MODIFIED PRINT TEMPLATES**

SD-PAIT PAIT ACK SUMMARY

SD-PAIT PATIENT PENDING APPT

SD-PAIT REJECTED APPT

SD-PAIT TRANS SUMMARY

**NEW AND MODIFIED SORT TEMPLATES**

SD-PAIT PAIT ACK SOR

SD-PAIT PEND EXCL FUTURE

SD-PAIT REJECTED APPT

SD-PAIT TRANS SUMMARY

**MAIL GROUP**

SD-PAIT

MODIFIED ROUTINES

SDRPA00

SDRPA05

SDRPA06

SDRPA07

SDRPA08

**NEW ROUTINE**

SDRPA09

**OPTIONS**

SD-PAIT MANUAL TRANSMISSION

SD-PAIT TASKED TRANSMISSION

SD-PAIT REPORTS

SD-PAIT PENDING

SD-PAIT REJECTED

SD-PAIT TRANSMISSION SUMMARY

SD-PAIT ACK SUMMARY

**PROTOCOLS**

SD-PAIT-EVENT

SD-PAIT-SUBS

**HL7 APPLICATION PARAMETERS**

SD-AAC-PAIT

SD-SITE-PAIT

**HL LOGICAL LINK**

SD-PAIT

**BACKGROUND JOB**

SD-PAIT TASKED TRANSMISSION

**SECURITY KEYS**

NONE

**BULLETINS**

NO BULLETINS are generated with this patch.  Please reference MAILMAN

NOTIFICATION MESSAGES listed above

### Initial Seeding Run Times:

### | **Site**   |   **Patients (File 2)** |   **Batch Messages** |   **Entries Added to file 409.6** | **Run Time**   |
|------------|-------------------------|----------------------|-----------------------------------|----------------|
| REDACTED   |                 410,263 |                   77 |                           380,795 | 3.5 days       |
| REDACTED   |                  72,589 |                   21 |                           102,425 | 1 day          |
| REDACTED   |                  71,295 |                   18 |                            88,933 | 1 day          |
| REDACTED   |                 213,732 |                   27 |                           133,397 | 1.5 days       |

**GLOBAL GROWTH**

Each entry added to file 409.6 takes approximately 250 bytes.  A medium to large site will require at least 120MB of available space on the volume set containing the ^SDWL(409.6 global to accommodate the initial seeding process.

HL7 messages generated by the seeding process take approximately 4 Mb per batch message.  A medium to large site will generate 60 to 100 batches on the initial seeding run which corresponds to at least 240Mb of available space on the volume set containing the HL7 globals.

^XMTP globals are created and used to record acknowledgment processing and have been defined to remain in the system for three days.

^XTMP(“SDRPA-”\_BATCHNUMBER,      [Diagnostics]

## Appendix  A – HL7 Specifications

**HL7 Interface Specification for Patient Appointment Information Transmission**

### Introduction

This interface specification details the information needed for the Patient Appointment Information Transmission data reporting.  This data transmission will be triggered by a TaskMan queued job in .  The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

### General

The formats of these messages conform to the Version 2.4 HL7 Interface Standards where applicable.  HL7 custom message formats (“Z” segments) are used only when necessary.

### Message Content

The table below describes the data fields and HL7 mappings:

| **Data item**                      |   **Length** | **Type**                                              | **Definition**                                                                                                                              | **HL7**   |
|------------------------------------|--------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Integration Control Number         |           10 | Alpha-numeric                                         | ICN is a VHA wide internal key, uniquely assigned to each PATIENT. The ICN is a 10 digit.                                                   | PID.3     |
| Patient’s DFN                      |            8 | Numeric                                               | The internal number of the patient from within the Patient file.                                                                            | PID.3     |
| Patient’s SSN                      |           10 | 9 Numeric, 1 Alpha                                    | The social security number or the generated pseudo SSN of the patient.                                                                      | PID.19    |
| Last Name  First Name  Middle Name |           45 | Text                                                  | The name of the patient. Held as three distinct names with a combined maximum length of 45 characters                                       | PID.5     |
| Date Of Birth                      |            8 | Date                                                  | The date of birth of the patient.                                                                                                           | PID.7     |
| Current SC status                  |            1 | Text                                                  | Current service connected status, Y/N                                                                                                       | ZSP.2     |
| Current SC percentage              |            3 | Numeric                                               | Current service connected percentage                                                                                                        | ZSP.3     |
| Date Appointment Created           |            8 | Date                                                  | The date the appointment was created                                                                                                        | SCH.11    |
| Desired Appointment Date           |            8 | Date                                                  | The date the appointment was requested to take place.                                                                                       | SCH.11    |
| Appointment Date                   |           12 | Date/time                                             | The date the appointment was scheduled to be kept.                                                                                          | SCH.11    |
| Appointment status                 |            3 | Text                                                  | See table 0278                                                                                                                              | SCH.25    |
| Next Available Request Flags       |            1 | Numeric                                               | See table 0276                                                                                                                              | SCH.7     |
| Cancellation Date                  |           12 | Date/time                                             | If the appointment was cancelled by the clinic or the patient, the date of cancellation.                                                    | SCH.11    |
| Reschedule Date                    |           12 | Date/time                                             | The date an appointment was rescheduled for without auto-rebooking                                                                          | SCH.11    |
| Auto-rebook Flag                   |            1 | Numeric                                               | See table 0276                                                                                                                              | SCH.7     |
| Auto-rebook Date                   |           12 | Date/time                                             | Date of the auto-rebooked appointment                                                                                                       | SCH.11    |
| New to Facility/Clinic Flag        |            1 | Text                                                  | NTF if the patient did not have a prior appointment at this facility in the past 24 months.   SHB otherwise.                                | PV2.24    |
| Enrollment Priority                |            1 | Alpha numeric                                         | See table VA0021                                                                                                                            | ZEN       |
| Service Connection Condition Flag  |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Agent Orange Exposure              |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Ionizing Radiation Exposure        |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Environmental Contaminants         |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Military Sexual Trauma             |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Head and/or Neck Cancer            |            1 | Numeric                                               | See table SD008                                                                                                                             | ZCL.2     |
| Clinic IEN Number                  |            6 | Numeric                                               | Internal Identifier of the Hospital Location the appointment was scheduled for.                                                             | AIL.3.1   |
| Clinic Name                        |           30 | Text                                                  | Name of Clinic from file 44                                                                                                                 | AIL.3.9   |
| DSS Identifier of Clinic           |            3 | Numeric                                               | Stop code of the Hospital Location file the appointment was scheduled for.                                                                  | AIL.4     |
| DSS Credit Stop of Clinic          |            3 | Numeric                                               | Credit stop code of the Hospital Location file                                                                                              | AIL.5     |
| Facility Number                    |            6 | Three digit numeric station number plus any modifiers | Station Number, field #99 from the Institution file                                                                                         | PV1.39    |
| Provider                           |              | Text                                                  | IEN and name of provider associated with the  Hospital Location                                                                             | AIP.3     |
| Check out Date                     |           12 | Date/time                                             | Date of appointment checkout. It is considered to be a kept appointment.                                                                    | SCH.11    |
| Appointment Type                   |            3 | Alpha                                                 | See Table  0277                                                                                                                             | SCH.8     |
| Scheduling Event Reason            |           3  | Alpha                                                 | See Table VA087                                                                                                                             | SCH.6     |
| Admission Type                     |           4  | Numeric                                               | See table SD009                                                                                                                             | PV1.4     |
| Consult Request Date               |           12 | Date                                                  | The request date and time of the related consult if applicable – the DATE OF REQUEST field (#3) of the REQUEST/  CONSULTATION  file (#123). | SCH.11    |

> **NOTE:** If the appointment is SC (Service Connected) related then only MST and

Head and/or Neck cancer may be identified as well. All other classifications

can be claimed  only if the appointment is not SC.

| **SIU**   | **SIU Message**                                      | **Section**   |
|-----------|------------------------------------------------------|---------------|
| BSH       | Batch Header                                         | 2.3.2         |
| {MSH      | Message Header                                       | 2.3.1         |
| SCH       | Schedule Activity Information                        | 2.3.9         |
| PID       | Patient Identification                               | 2.3.4         |
| PV1       | Patient Visit                                        | 2.3.5         |
| PV2       | Patient Visit                                        | 2.3.6         |
| [{AIP}]   | Appointment information - personnel resource segment | 2.3.7         |
| {AIL}     | Appointment Information                              | 2.3.8         |
| [{ZCL}]   | VA-Specific Outpatient Classification                | 2.3.10        |
| [{ZEN}]   | VA Specific Enrollment                               | 2.3.11        |
| {ZSP}}    | VA-Specific Service Period                           | 2.3.12        |
| BTS       | Batch Trailer                                        | 2.3.3         |

### Data Capture and Transmission

A Taskman background job will be scheduled to run at specified intervals.  The background job will collect and format data for HL7 batch transmission.

A determined number of appointments is generated into a temporary file. That file is sent to create HL7 transmission in a batch format. As soon as the batch is put into a queue, the temporary file is deleted and the process of generating data for transmission continues until all required data is generated and transmitted. That design allows for an immediate transmission after generation of a partial data, and prevents the temporary file from growing tremendously before it is sent for transmission. The process is repeated until all required data is generated and transmitted.

The follow up transmissions will be created as batch messages with all appointments made starting from the next date to the last scanned appointment  creation date of the last transmission, and with previously sent appointments,  if their statuses turn out to have one of the final values, see SCH.25. Filler Status in SIU Event Mapping Table.  The previously sent appointments are evaluated for a possible final transmission from the Patient Transmission Info Log file (#409.6). Appointments entries in that file that were sent with the final status will be deleted after an acknowledgement of the successful transmission is received.

### Batch Messages

Batch messages will be used to transmit patient appointment information.  Each batch message may contain up to 5000 messages.  One message will represent one patient appointment.

### Batch Acknowledgements

Each batch message sent will be acknowledged at the application level.

### Lower Level Protocol

TCP/IP will be used.

### HL7 Control Segments

This section defines the HL7 control segments supported by  and implemented in this transmission.  The messages are presented separately and defined by category.  Segments are also described.

### Message Definitions

Each message is composed of segments.  Segments contain logical groupings of data.  Segments may be optional or repeatable.  A [ ] indicates the segment is optional, the { } indicates the segment is repeatable.  For each message category there will be a list of HL7 standard segments or "Z" segments used for the message.

### ### Segment Table Definitions

For each segment, the data elements are described in table format.  The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL #), the element name, and the  description.   Each segment is described in the following sections.

### ### Message Control Segments

This section describes the message control segments which are contained in message types described in this document.  These are generic descriptions.  Any time any of the segments described in this section are included in a message in this document, the  descriptions and mappings will be as specified here, unless otherwise specified in that section.

### MSH - Message Header Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#       | ELEMENT NAME                    |  DESCRIPTION                                                                                                                                                   |
|-------|-------|------|-------|--------|------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |        |            | Field Separator                 | Recommended value is  **^**  (caret)                                                                                                                           |
|     2 |     4 | ST   | R     |        |            | Encoding Characters             | Recommended delimiter values:  Component =  **~**  (tilde)  Repeat =  **&#124;**  (bar)  Escape =  **\**  (back slash)  Subcomponent =  **&amp;**  (ampersand) |
|     3 |    15 | ST   |       |        |            | Sending Application             | When originating from facility:  **SD-SITE-PAIT**  When originating from ACC:  **SD-AAC-PAIT**                                                                 |
|     4 |    20 | ST   |       |        |            | Sending Facility                | When originating from facility:  Station's facility number                                                                                                     |
|     5 |    30 | ST   |       |        |            | Receiving Application           | **SD-AAC-PAIT**                                                                                                                                                |
|     6 |    30 | ST   |       |        |            | Receiving Facility              | 200                                                                                                                                                            |
|     7 |    26 | TS   |       |        |            | Date/Time Of Message            | Not used                                                                                                                                                       |
|     8 |    40 | ST   |       |        |            | Security                        | Not used                                                                                                                                                       |
|     9 |     7 | CM   | R     |        | 0076  0003 | Message Type                    | 2 Components  1. Message type 2. Trigger event                                                                                                                 |
|    10 |    20 | ST   | R     |        |            | Message Control ID              | Batch and sequence number automatically generated by  HL7 Package                                                                                              |
|    11 |     1 | ID   | R     |        |            | Processing ID                   | **P**  (production)                                                                                                                                            |
|    12 |     8 | ID   | R     |        |            | Version ID                      | **2.4**  (Version 2.4)                                                                                                                                         |
|    13 |    15 | NM   |       |        |            | Sequence Number                 | Not used                                                                                                                                                       |
|    14 |   180 | ST   |       |        |            | Continuation Pointer            | Not used                                                                                                                                                       |
|    15 |     2 | ID   |       |        |            | Accept Acknowledgment Type      | (always acknowledge)                                                                                                                                           |
|    16 |     2 | ID   |       |        |            | Application Acknowledgment Type | (always acknowledge)                                                                                                                                           |
|    17 |     3 | ID   |       |        |            | Country Code                    |                                                                                                                                                                |

### BHS – Batch Header Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME                |  DESCRIPTION                                                                                                                      |
|-------|-------|------|-------|--------|--------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |        |        | Batch Field Separator       | Recommended value is  ^                                                                                                           |
|     2 |     4 | ST   | R     |        |        | Batch Encoding Characters   | Delimiter values:  Component =  **~**  (tilde)  Repeat =  **&#124;**  (bar)  Escape =  **\**  (back slash)  Subcomponent =  &amp; |
|     3 |    15 | ST   |       |        |        | Batch Sending Application   | When originating from facility:  **SD-SITE-PAIT**  When originating from AAC:  **SD-ACC-PAIT**                                    |
|     4 |    20 | ST   |       |        |        | Batch Sending Facility      | When originating from facility:  Station's facility number  when originating from AAC:  **200**                                   |
|     5 |    15 | ST   |       |        |        | Batch Receiving Application | When originating from facility:  **SD-ACC-PAIT**  When originating from AAC:  **SD-SITE-PAIT**                                    |
|     6 |    20 | ST   |       |        |        | Batch Receiving Facility    | When originating from facility:  Station's facility number  When originating from AAC:  **200**                                   |
|     7 |    26 | TS   |       |        |        | Batch Creation Date/Time    | Date and time batch message was created                                                                                           |
|     8 |    40 | ST   |       |        |        | Batch Security              | Not used                                                                                                                          |
|     9 |    20 | ST   |       |        |        | Batch Name/ID/Type          | Components  1. Not used 2. P 3. SIU,S12 4. 2.4  5.  6.                                                                            |
|    10 |    80 | ST   |       |        |   0008 | Batch Comment               | Components  1. Acknowledgement  Code 2. Text Message                                                                              |
|    11 |    20 | ST   |       |        |        | Batch Control ID            | When originating from facility:  Automatically generated by  HL7 Package  When  Originating from AAC:  Acknowledgement msg #      |
|    12 |    20 | ST   |       |        |        | Reference Batch Control ID  | When originating from facility: Null  When originating from AAC:  Batch Control ID of batch message being acknowledged            |

### BTS - Batch Trailer Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENT NAME        |  DESCRIPTION                    |
|-------|-------|------|-------|--------|--------|---------------------|---------------------------------|
|     1 |    10 | ST   |       |        |        | Batch Message Count | Number of messages within batch |
|     2 |    80 | ST   |       |        |        | Batch Comment       | Not used                        |
|     3 |   100 | CM   |       | Y      |        | Batch Totals        | Not used                        |

### PID - Patient Identification Segment

|   ## SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENT NAME             |  DESCRIPTION                                                                                                                       |
|----------|-------|------|-------|--------|--------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|        1 |     4 | SI   |       |        |        | Set ID - Patient ID      | Sequential Number                                                                                                                  |
|        2 |    17 | CK   |       |        |        | Patient ID (External ID) | Primary Long ID                                                                                                                    |
|        3 |    21 | CM   | R     |        |        | Patient ID (Internal ID) | Component  1.  ICN  2.  NULL  3.  NULL  4.  USVHA&amp;&amp;L  5.  NI  Repetition  1. DFN 2. Null 3. Null 4. USVHA&amp;&amp;L 5. PI |
|        4 |    12 | ST   |       |        |        | Alternate Patient ID     | Not used                                                                                                                           |
|        5 |    48 | PN   | R     |        |        | Patient Name             | Component  1. Family name 2. Given name 3. Middle initial 4. Suffix                                                                |
|        6 |    30 | ST   |       |        |        | Mother's Maiden Name     | Not used                                                                                                                           |
|        7 |    26 | TS   |       |        |        | Date of Birth            | Date of birth                                                                                                                      |
|        8 |     1 | ID   |       |        |        | Sex                      | Not used                                                                                                                           |
|        9 |    48 | PN   |       |        |        | Patient Alias            | Not used                                                                                                                           |
|       10 |     1 | ID   |       |        |        | Race                     | Not used                                                                                                                           |
|       11 |   106 | AD   |       |        |        | Patient Address          | Zip Code                                                                                                                           |

### PID - Patient Identification Segment  (continued)

|   12 |   4 | ID   |    |    |    |                            | Not used                                    |
|------|-----|------|----|----|----|----------------------------|---------------------------------------------|
|   13 |  40 | TN   |    |    |    | Phone Number - Home        | Not used                                    |
|   14 |  40 | TN   |    |    |    | Phone Number - Business    | Not used                                    |
|   15 |  25 | ST   |    |    |    | Language - Patient         | Not used                                    |
|   16 |   1 | ID   |    |    |    | Marital Status             | Not used                                    |
|   17 |   3 | ID   |    |    |    | Religion                   | Not used                                    |
|   18 |  20 | CK   |    |    |    | Patient Account Number     | Not used                                    |
|   19 |  16 | ST   |    |    |    | SSN Number - Patient       | Social security number and pseudo indicator |
|   20 |  25 | CM   |    |    |    | Driver's Lic Num - Patient | Not used                                    |
|   21 |  20 | CK   |    |    |    | Mother's Identifier        | Not used                                    |
|   22 |   1 | ID   |    |    |    | Ethnic Group               | Not used                                    |
|   23 |  25 | ST   |    |    |    | Birth Place                | Not used                                    |
|   24 |   2 | ID   |    |    |    | Multiple Birth Indicator   | Not used                                    |
|   25 |   2 | NM   |    |    |    | Birth Order                | Not used                                    |
|   26 |   3 | ID   |    |    |    | Citizenship                | Not used                                    |
|   27 |  60 | CE   |    |    |    | Veterans Military Status   | Not used                                    |

### PV1 - Patient Visit Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME              |  DESCRIPTION                                             |
|-------|-------|------|-------|--------|--------|---------------------------|----------------------------------------------------------|
|     1 |     4 | SI   |       |        |        | Set ID - Patient Visit    | Sequential Number                                        |
|     2 |     1 | ID   |       |        |   0004 | Patient Class             | Patient Class                                            |
|     3 |    12 | CM   |       |        |        | Assigned Patient Location | Not used                                                 |
|     4 |     4 | ID   |       |        |   0007 | Admission Type            | Refer to table SD009 (Purpose of Visit/Appointment Type) |
|     5 |    20 | ST   |       |        |        | Preadmit Number           | Not used                                                 |
|     6 |    12 | CM   |       |        |        | Prior Patient Location    | Not used                                                 |
|     7 |    60 | CN   |       |        |        | Attending Doctor          | Not used                                                 |
|     8 |    60 | CN   |       |        |        | Referring Doctor          | Not used                                                 |
|     9 |    60 | CN   |       |        |        | Consulting Doctor         | Not used                                                 |
|    10 |     3 | ID   |       |        |        | Hospital Service          | Not used                                                 |
|    11 |    12 | CM   |       |        |        | Temporary Location        | Not used                                                 |
|    12 |     2 | ID   |       |        |        | Preadmit Test Indicator   | Not used                                                 |
|    13 |     2 | ID   |       |        |        | Readmission Indicator     | Not used                                                 |
|    14 |     3 | ID   |       |        |        | Admit Source              | Not used                                                 |
|    15 |     2 | ID   |       |        |        | Ambulatory Status         | Not used                                                 |
|    16 |     2 | ID   |       |        |        | VIP Indicator             | Not used                                                 |
|    17 |    60 | CN   |       |        |        | Admitting Doctor          | Not used                                                 |
|    18 |     2 | ID   |       |        |        | Patient Type              | Not used                                                 |
|    19 |    15 | NM   |       |        |        | Visit Number              | Not used                                                 |
|    20 |    50 | CM   |       |        |        | Financial Class           | Not used                                                 |
|    21 |     2 | ID   |       |        |        | Charge Price Indicator    | Not used                                                 |
|    22 |     2 | ID   |       |        |        | Courtesy Code             | Not used                                                 |
|    23 |     2 | ID   |       |        |        | Credit Rating             | Not used                                                 |
|    24 |     2 | ID   |       |        |        | Contract Code             | Not used                                                 |

**PV1 - Patient Visit Segment (continued)**

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENT NAME              |  DESCRIPTION                               |
|-------|-------|------|-------|--------|--------|---------------------------|--------------------------------------------|
|    25 |     8 | DT   |       |        |        | Contract Effective Date   | Not used                                   |
|    26 |    12 | NM   |       |        |        | Contract Amount           | Not used                                   |
|    27 |     3 | NM   |       |        |        | Contract Period           | Not used                                   |
|    28 |     2 | ID   |       |        |        | Interest Code             | Not used                                   |
|    29 |     1 | ID   |       |        |        | Transfer to Bad Debt Code | Not used                                   |
|    30 |     8 | DT   |       |        |        | Transfer to Bad Debt Date | Not used                                   |
|    31 |    10 | ID   |       |        |        | Bad Debt Agency Code      | Not used                                   |
|    32 |    12 | NM   |       |        |        | Bad Debt Transfer Amount  | Not used                                   |
|    33 |    12 | NM   |       |        |        | Bad Debt Recovery Amount  | Not used                                   |
|    34 |     1 | ID   |       |        |        | Delete Account Indicator  | Not used                                   |
|    35 |     8 | DT   |       |        |        | Delete Account Date       | Not used                                   |
|    36 |     3 | ID   |       |        |        | Discharge Disposition     | Not used                                   |
|    37 |    25 | CM   |       |        |        | Discharged to Location    | Not used                                   |
|    38 |     2 | ID   |       |        |        | Diet Type                 | Not used                                   |
|    39 |     7 | ID   |       |        |        | Servicing Facility        | Facility number or Facility number+ suffix |
|    40 |     1 | ID   |       |        |        | Bed Status                | Not used                                   |
|    41 |     2 | ID   |       |        |        | Account Status            | Not used                                   |
|    42 |    12 | CM   |       |        |        | Pending Location          | Not used                                   |
|    43 |    12 | CM   |       |        |        | Prior Temporary Location  | Not used                                   |
|    44 |    26 | TS   |       |        |        | Admit Date/Time           | Not used                                   |
|    45 |    26 | TS   |       |        |        | Discharge Date/Time       | Not used                                   |
|    46 |    12 | NM   |       |        |        | Current Patient Balance   | Not used                                   |
|    47 |    12 | NM   |       |        |        | Total Charges             | Not used                                   |
|    48 |    12 | NM   |       |        |        | Total Adjustments         | Not used                                   |
|    49 |    12 | NM   |       |        |        | Total Payments            | Not used                                   |
|    50 |    20 | CM   |       |        |        | Alternate Visit ID        | Not used                                   |

**2.3.6 PV2 Patient Visit**

|   **SEQ** |   **LEN** | **DT**   | **R/**   | **RP/#**   |   **TBL#** |   **ITEM#** | **ELEMENT NAME**                     | **DESCRIPTION**         |
|-----------|-----------|----------|----------|------------|------------|-------------|--------------------------------------|-------------------------|
|         1 |        80 | PL       | C        |            |            |        0011 | Prior Pending Location               | Not used                |
|         2 |        60 | CE       | O        |            |            |        0012 | Accommodation Code                   | Not used                |
|         3 |        60 | CE       | O        |            |            |        0013 | Admit Reason                         | Not used                |
|         4 |        60 | CE       | O        |            |            |        0014 | Transfer Reason                      | Not used                |
|         5 |        25 | ST       | O        |            |            |        0015 | Patient Valuables                    | Not used                |
|         6 |        25 | ST       | O        |            |            |        0016 | Patient Valuables Location           | Not used                |
|         7 |         2 | IS       | O        |            |            |        0017 | Visit User Code                      | Not used                |
|         8 |        26 | TS       | O        |            |            |        0018 | Expected Admit Date/Time             | Not used                |
|         9 |        26 | TS       | O        |            |            |        0019 | Expected Discharge Date/Time         | Not used                |
|        10 |         3 | NM       | O        |            |            |        0071 | Estimated Length of Inpatient Stay   | Not used                |
|        11 |         3 | NM       | O        |            |            |        0072 | Actual Length of Inpatient Stay      | Not used                |
|        12 |        50 | ST       | O        |            |            |        0073 | Visit Description                    | Not used                |
|        13 |        90 | XCN      | O        |            |            |        0074 | Referral Source Code                 | Not used                |
|        14 |         8 | DT       | O        |            |            |        0075 | Previous Service Date                | Not used                |
|        15 |         1 | ID       | O        |            |            |        0076 | Employment Illness Related Indicator | Not used                |
|        16 |         1 | IS       | O        |            |            |        0077 | Purge Status Code                    | Not used                |
|        17 |         8 | DT       | O        |            |            |        0078 | Purge Status Date                    | Not used                |
|        18 |         2 | IS       | O        |            |            |        0079 | Special Program Code                 | Not used                |
|        19 |         1 | ID       | O        |            |            |        0070 | Retention Indicator                  | Not used                |
|        20 |         1 | NM       | O        |            |            |        0071 | Expected Number of Insurance Plans   | Not used                |
|        21 |         1 | IS       | O        |            |            |        0072 | Visit Publicity Code                 | Not used                |
|        22 |         1 | ID       | O        |            |            |        0073 | Visit Protection Indicator           | Not used                |
|        23 |        90 | XON      | O        |            |            |        0074 | Clinic Organization Name             | Not used                |
|        24 |         2 | IS       | O        |            |       0216 |        0075 | Patient Status Code                  | New to Facility/ Clinic |
|        25 |         1 | IS       | O        |            |            |        0076 | Visit Priority Code                  | Not used                |
|        26 |         8 | DT       | O        |            |            |        0077 | Previous Treatment Date              | Not used                |
|        27 |         2 | IS       | O        |            |            |        0078 | Expected Discharge Disposition       | Not used                |
|        28 |         8 | DT       | O        |            |            |        0079 | Signature on File Date               | Not used                |
|        29 |         8 | DT       | O        |            |            |        0070 | First Similar Illness Date           | Not used                |
|        30 |         3 | IS       | O        |            |            |        0071 | Patient Charge Adjustment Code       | Not used                |
|        31 |         2 | IS       | O        |            |            |        0072 | Recurring Service Code               | Not used                |
|        32 |         1 | ID       | O        |            |            |        0073 | Billing Media Code                   | Not used                |
|        33 |        26 | TS       | O        |            |            |        0074 | Expected Surgery Date & Time         | Not used                |
|        34 |         2 | ID       | O        |            |            |        0075 | Military Partnership Code            | Not used                |
|        35 |         2 | ID       | O        |            |            |        0076 | Military Non-Availability Code       | Not used                |
|        36 |         1 | ID       | O        |            |            |        0077 | Newborn Baby Indicator               | Not used                |
|        37 |         1 | ID       | O        |            |            |        0078 | Baby Detained Indicator              | Not used                |

### AIP - Appointment Information - Personnel Resource Segment

|   SEQ |   LEN | DT   | R/O/C   | RP/#   | TBL#   |   ITEM# | ELEMENT NAME                 | **DESCRIPTION**                                                                             |
|-------|-------|------|---------|--------|--------|---------|------------------------------|---------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R       |        |        |   00906 | Set ID - AIP                 | Sequential Number                                                                           |
|     2 |     3 | ID   | C       |        |        |   00763 | Segment Action code          | Not used                                                                                    |
|     3 |    80 | XCN  | C       | Y      |        |   00913 | Personnel Resource ID        | Component  1. Provider IEN 2. Family name 3. Given name 4. Middle name or initial 5. Suffix |
|     4 |   200 | CE   | R       |        |        |   00907 | Resource Role                | Provider                                                                                    |
|     5 |   200 | CE   | O       |        |        |   00899 | Resource Group               | Not used                                                                                    |
|     6 |    26 | TS   | C       |        |        |   01202 | Start Date/Time              | Not used                                                                                    |
|     7 |    20 | NM   | C       |        |        |   00891 | Start Date/Time Offset       | Not used                                                                                    |
|     8 |   200 | CE   | C       |        |        |   00892 | Start Date/Time Offset Units | Not used                                                                                    |

### ### AIL Appointment Information

|   **SEQ** |   **LEN** | **DT**   | **R/O/C**   | **RP/#**   | **TBL#**   |   **ITEM#** | **ELEMENT NAME**             | **DESCRIPTION**                                                                                                                                   |
|-----------|-----------|----------|-------------|------------|------------|-------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 |         4 | SI       | R           |            |            |       00902 | Set ID - AIL                 | Sequential Number                                                                                                                                 |
|         2 |         1 | ID       | C           |            |            |       00763 | Segment Action Code          | Not used                                                                                                                                          |
|         3 |        90 | PL       | C           |            |            |       00903 | Location Resource ID         | Clinic Name  Components  1.   Clinic IEN (20)  2.   Null  3.   Null  4.   Null  5.   Null  6.   Null  7.   Null  8.   Null  9.   Clinic name (60) |
|         4 |       100 | CE       | R           |            | VA088      |       00904 | Location Type                | DSS ID  Components  1. DSS Clinic ID code (3) 2. Description (40) 3. ‘DSS Clinic ID” (13)                                                         |
|         5 |       100 | CE       | O           |            | VA088      |       00905 | Location Group               | DSS credit stop  1. DSS credit stop code (3) 2. Description (40) 3. “DSS Credit Stop” (15)                                                        |
|         6 |        26 | TS       | C           |            |            |       01202 | Start Date/Time              | Not used                                                                                                                                          |
|         7 |        20 | NM       | C           |            |            |       00891 | Start Date/Time Offset       | Not used                                                                                                                                          |
|         8 |       200 | CE       | C           |            |            |       00892 | Start Date/Time Offset Units | Not used                                                                                                                                          |
|         9 |        20 | NM       | O           |            |            |       00893 | Duration                     | Not used                                                                                                                                          |
|        10 |       200 | CE       | O           |            |            |       00894 | Duration Units               | Not used                                                                                                                                          |
|        11 |        10 | IS       | C           |            |            |       00895 | Allow Substitution Code      | Not used                                                                                                                                          |
|        12 |       200 | CE       | C           |            |            |       00889 | Filler Status Code           | Not used                                                                                                                                          |

### SCH Schedule Activity Information

|   **SEQ** |   **LEN** | **DT**   | **R/O/C**   | **RP/#**   | **TBL#**   |   **ITEM#** | **ELEMENT NAME**             | **DESCRIPTION**                                                                                                                                                        |
|-----------|-----------|----------|-------------|------------|------------|-------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 |        75 | EI       | R           |            |            |       00860 | Placer Appointment ID        | Sequential Number                                                                                                                                                      |
|         2 |        75 | EI       | C           |            |            |       00861 | Filler Appointment ID        | Not used                                                                                                                                                               |
|         3 |         5 | NM       | C           |            |            |       00862 | Occurrence Number            | Not used                                                                                                                                                               |
|         4 |        75 | EI       | O           |            |            |       00863 | Placer Group Number          | Not used                                                                                                                                                               |
|         5 |       200 | CE       | O           |            |            |       00864 | Schedule ID                  | Not used                                                                                                                                                               |
|         6 |         3 | CE       | O           |            | VA087      |       00883 | Event Reason                 | Component  Scheduling  Event Reason codes.                                                                                                                             |
|         7 |         1 | CE       | O           |            | 0276       |       00866 | Appointment Reason           | Appointment Reason                                                                                                                                                     |
|         8 |         3 | CE       | O           |            | 0277       |       00867 | Appointment Type             | Appointment Type Codes                                                                                                                                                 |
|         9 |        20 | NM       | O           |            |            |       00868 | Appointment Duration         | Not used                                                                                                                                                               |
|        10 |       200 | CE       | O           |            |            |       01304 | Appointment Duration Units   | Not used                                                                                                                                                               |
|        11 |       200 | TQ       | O           | Y          |            |       00884 | Appointment Timing Quantity  | In the following order:  Date Appt Created  Desired Date  Appt Date (time)  Checkout Date (time)  Cancellation Date (time)  Auto-rebook Date(time)  Resched Date(time) |
|        12 |        48 | XCN      | O           |            |            |       00874 | Placer Contact Person        | Not used                                                                                                                                                               |
|        13 |        40 | XTN      | O           |            |            |       00875 | Placer Contact Phone Number  | Not used                                                                                                                                                               |
|        14 |       106 | XAD      | O           |            |            |       00876 | Placer Contact Address       | Not used                                                                                                                                                               |
|        15 |        80 | PL       | O           |            |            |       00877 | Placer Contact Location      | Not used                                                                                                                                                               |
|        16 |        38 | XCN      | R           |            |            |       00885 | Filler Contact Person        | Not used                                                                                                                                                               |
|        17 |        40 | XTN      | O           |            |            |       00886 | Filler Contact Phone Number  | Not used                                                                                                                                                               |
|        18 |       106 | XAD      | O           |            |            |       00887 | Filler Contact Address       | Not used                                                                                                                                                               |
|        19 |        80 | PL       | O           |            |            |       00888 | Filler Contact Location      | Not used                                                                                                                                                               |
|        20 |        48 | XCN      | R           |            |            |       00878 | Entered by Person            | Not used                                                                                                                                                               |
|        21 |        40 | XTN      | O           |            |            |       00879 | Entered by Phone Number      | Not used                                                                                                                                                               |
|        22 |        80 | PL       | O           |            |            |       00880 | Entered by Location          | Not used                                                                                                                                                               |
|        23 |        75 | EI       | O           |            |            |       00881 | Parent Placer Appointment ID | Not used                                                                                                                                                               |
|        24 |        75 | EI       | O           |            |            |       00882 | Parent Filler Appointment ID | Not used                                                                                                                                                               |
|        25 |       200 | CE       | R           |            | 0278       |       00889 | Filler Status Code           | Appointment Status                                                                                                                                                     |

### ZCL - VA-Specific Outpatient Classification Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   |  ELEMENT NAME                  |
|-------|-------|------|-------|--------|--------|--------------------------------|
|     1 |     4 | SI   | R     |        |        | SET ID                         |
|     2 |     2 | ID   | R     |        | SD008  | Outpatient Classification Type |
|     3 |    50 | ST   |       |        |        | Value                          |

### ZEN - VA-Specific Enrollment Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   |  ELEMENT NAME       |
|-------|-------|------|-------|--------|--------|---------------------|
|     1 |     4 | SI   | R     |        |        | SET ID              |
|     2 |     8 | DT   |       |        |        | Not used            |
|     3 |     1 | ID   |       |        |        | Not used            |
|     4 |     1 | ID   |       |        |        | Not used            |
|     5 |     1 | ID   |       |        |        | Not used            |
|     6 |    60 | TX   |       |        |        | Not used            |
|     7 |     7 | ID   |       |        |        | Not used            |
|     8 |     7 | ID   |       |        |        | Not used            |
|     9 |     1 | ID   |       |        | VA0021 | ENROLLMENT PRIORITY |
|    10 |     8 | DT   |       |        |        | not used            |

### ZSP - VA-Specific Service Period Segment

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   |  ELEMENT NAME                |
|-------|-------|------|-------|--------|--------|------------------------------|
|     1 |     4 | SI   | R     |        |        | SET ID                       |
|     2 |     1 | ID   | R     |        | VA01   | Service Connected?           |
|     3 |     3 | NM   |       |        |        | Service Connected Percentage |
|     4 |     2 | ID   |       |        |        | NOT USED                     |
|     5 |     1 | ID   |       |        |        | NOT USED                     |

### SUPPORTED AND USER-DEFINED HL7 TABLES

### Table 0003 - Event type

| VALUE   | DESCRIPTION                                                                |
|---------|----------------------------------------------------------------------------|
| S12     | SIU/ACK - Notification of new appointment booking                          |
| S14     | SIU/ACK - Notification of appointment modification                         |
| S15     | SIU/ACK - Notification of appointment cancellation                         |
| S26     | SIU/ACK Notification that patient did not show up for schedule appointment |

### Table 0004 – Patient Class

| VALUE   | DESCRIPTION   |
|---------|---------------|
| I       | INPATIENT     |
| O       | OUTPATIENT    |
| U       | UNKNOWN       |

### Table 0008 - Acknowledgment Code

| VALUE   | DESCRIPTION                               |
|---------|-------------------------------------------|
| AA      | APPLICATION ACKNOWLEDGMENT: ACCEPT        |
| AE      | APPLICATION ACKNOWLEDGMENT: ERROR         |
| AR      | APPLICATION ACKNOWLEDGMENT: REJECT        |
| MR      | APPLICATION ACKNOWLEDGMENT: MANUAL REJECT |
| CA      | ACCEPT ACKNOWLEDGMENT: COMMIT ACCEPT      |
| CE      | ACCEPT ACKNOWLEDGMENT: COMMIT ERROR       |
| CR      | ACCEPT ACKNOWLEDGMENT: COMMIT REJECT      |

The patch is prepared for ‘AR’ – THE WHOLE BATCH REJECTION  but

It has not been expected to receive that code from the AAC at this time.

‘MR’ may be used  instead.

### Table 0076 - Message Type

| VALUE   | DESCRIPTION            |
|---------|------------------------|
| SIU     | SIU MESSAGE            |
| ACK     | GENERAL ACKNOWLEDGMENT |

### Table 0216 - Patient Status Codes

| **VALUE**   | **DESCRIPTION**                                                                                                   |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| NTF         | Patient did not have a prior appointment at this Facility in the past 24 months; New to parent and substation.    |
| SHB         | Patient did have a prior appointment at this parent and substation in the past 24 months; Registered here before. |
| OPN         | Patient did not have a prior appointment at this substation but was registered with parent station.               |

The patient status code indicates if a patient is new to the facility or not. Both the parent station and the substations are evaluated as the facility. The parent station is evaluated with the primary DSS ID only; the substation is evaluated with both DSS ID stop code and the DSS credit stop code. The patient is considered new to the facility if he/she did not have another scheduled appointment in the same facility during the previous 24 months. The facility’s station number is determined from the Division (field #3.5) of the clinic’s Hospital Location file #44 entry. The division is retrieved from the Medical Center Division file #40.8 from which the Institution File Pointer field (#.07) is used to look up the Institution file #4 entry where the Station Number field (#99) is stored.

### Table 0276 - Appointment Reason Codes

|   VALUE | DESCRIPTION                                     |
|---------|-------------------------------------------------|
|       1 | Next Ava. Appt. Indicated by User               |
|       2 | Next Ava. Appt. Indicated by Calculation        |
|       3 | Next Ava. Appt. Indicated by User & Calculation |
|       4 | Not Next Available with AutoRebook              |
|       5 | Not Next Available No AutoRebook                |
|       6 | Null (All others)                               |

### Table  0277 - Appointment Type Codes

| VALUE   | DESCRIPTION      |
|---------|------------------|
| AR      | Action required  |
| NAT     | No action taken  |
| F       | Future           |
| NC      | Non count        |
| NCF     | Non count future |
| ABK     | Auto re-book     |
| O       | Outpatient       |
| I       | Inpatient        |
| RS      | Re-schedule      |

### Table 0278 Filler Status Codes

| VALUE   | DESCRIPTION   |
|---------|---------------|
| P       | Pending       |
| F       | Final         |

### Table VA01 - Yes/No

| VALUE   | DESCRIPTION   |
|---------|---------------|
| 0       | NO            |
| 1       | YES           |
| N       | NO            |
| Y       | YES           |
| U       | UNKNOWN       |

### Table SD008 - Outpatient Classification Type

|   VALUE | DESCRIPTION                |
|---------|----------------------------|
|       1 | AGENT ORANGE               |
|       2 | IONIZING RADIATION         |
|       3 | SERVICE CONNECTED          |
|       4 | ENVIRONMENTAL CONTAMINANTS |
|       5 | MILITARY SEXUAL TRAUMA     |
|       6 | HEAD AND/OR NECK CANCER    |

### Table SD009 - Purpose of Visit &amp; Appointment Type

|   **VALUE** | **PURPOSE OF VISIT**   | **APPOINTMENT TYPE**   |
|-------------|------------------------|------------------------|
|       0101  | C&P                    | COMPENSATION & PENSION |
|       0102  | C&P                    | CLASS II DENTAL        |
|       0103  | C&P                    | ORGAN DONORS           |
|       0104  | C&P                    | EMPLOYEE               |
|       0105  | C&P                    | PRIMA FACIA            |
|       0106  | C&P                    | RESEARCH               |
|       0107  | C&P                    | COLLATERAL OF VET.     |
|       0108  | C&P                    | SHARING AGREEMENT      |
|       0109  | C&P                    | REGULAR                |
|        0111 | C&P                    | SERVICE CONNECTED      |
|    0201     | 10-10                  | COMPENSATION & PENSION |
|       0202  | 10-10                  | CLASS II DENTAL        |
|       0203  | 10-10                  | ORGAN DONORS           |
|       0204  | 10-10                  | EMPLOYEE               |
|       0205  | 10-10                  | PRIMA FACIA            |
|       0206  | 10-10                  | RESEARCH               |
|       0207  | 10-10                  | COLLATERAL OF VET.     |
|       0208  | 10-10                  | SHARING AGREEMENT      |
|       0209  | 10-10                  | REGULAR                |
|        0211 | 10-10                  | SERVICE CONNECTED      |
|       0301  | SCHEDULED VISIT        | COMPENSATION & PENSION |
|       0302  | SCHEDULED VISIT        | CLASS II DENTAL        |
|       0303  | SCHEDULED VISIT        | ORGAN DONORS           |
|       0304  | SCHEDULED VISIT        | EMPLOYEE               |
|       0305  | SCHEDULED VISIT        | PRIMA FACIA            |
|       0306  | SCHEDULED VISIT        | RESEARCH               |
|       0307  | SCHEDULED VISIT        | COLLATERAL OF VET.     |
|       0308  | SCHEDULED VISIT        | SHARING AGREEMENT      |
|       0309  | SCHEDULED VISIT        | REGULAR                |
|        0311 | SCHEDULED VISIT        | SERVICE CONNECTED      |
|       0401  | UNSCHED. VISIT         | COMPENSATION & PENSION |
|       0402  | UNSCHED. VISIT         | CLASS II DENTAL        |
|       0403  | UNSCHED. VISIT         | ORGAN DONORS           |
|       0404  | UNSCHED. VISIT         | EMPLOYEE               |
|       0405  | UNSCHED. VISIT         | PRIMA FACIA            |
|       0406  | UNSCHED. VISIT         | RESEARCH               |
|       0407  | UNSCHED. VISIT         | COLLATERAL OF VET.     |
|       0408  | UNSCHED. VISIT         | SHARING AGREEMENT      |
|       0409  | UNSCHED. VISIT         | REGULAR                |
|        0411 | UNSCHED. VISIT         | SERVICE CONNECTED      |

Value denotes a combination of Purpose of Visit &amp; Appointment Type, which is known as “Admission Type” for the purposes of data transmission. This table is used in processing the ACRP HL7 transmission.

*Note:*

*It has been determined that PV1 segment can contain the ‘empty’ value for sequence P1.4 and it has to be treated as* ***acceptable*** *. That might happen when a new appointment is scheduled in place of a previously canceled appointment, and if the original appointment has been already transmitted by PAIT.*

### Table VA0021 – Enrollment Priority

|   VALUE | DESCRIPTION   |
|---------|---------------|
|       1 | Priority 1    |
|       2 | Priority 2    |
|       3 | Priority 3    |
|       4 | Priority 4    |
|       5 | Priority 5    |
|       6 | Priority 6    |
|       7 | Priority 7    |
|       8 | Priority 8    |

### Table VA087 -  Scheduling Event Reason

| VALUE   | DESCRIPTION            |
|---------|------------------------|
| CI      | Check-in               |
| CO      | Check-out              |
| NS      | No Show                |
| CC      | Cancel by clinic       |
| CP      | Cancel by patient      |
| COE     | Check-out by encounter |
| NM      | No Match               |
| CT      | Cancelled Terminated   |

### Table AAC001 - Error Code Set

| VALUE   | DESCRIPTION                                                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 100     | PATIENT DFN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                           |
| 150     | CLINIC IEN IS NOT NUMERIC OR IS MISSING                                                                                                                                                                                            |
| 200     | BHS STATION NUMBER AND STA3N ARE NOT EQUAL                                                                                                                                                                                         |
| 250     | INVALID OR MISSING BHS STATION NUMBER                                                                                                                                                                                              |
| 300     | INVALID OR MISSING STA3N                                                                                                                                                                                                           |
| 350     | HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING.                                                                                                                                                                                    |
| 400     | DOB IS MISSING OR INVALID                                                                                                                                                                                                          |
| 450     | CREATE DATE OR APPT DATE IS MISSING                                                                                                                                                                                                |
| 500     | CREATION DATE IS BEFORE SEPTEMBER 1, 2002                                                                                                                                                                                          |
| 600     | RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT - Rescheduled date requires SCH.8 Appt type = ‘RS’ and vice versa                                                                                                              |
| 650     | CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT - Check out date requires either SCH.6 Event reason = ‘CO’ or ‘COE’                                                                                                           |
| 700     | CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT - Cancellation date requires SCH.6 Event reason = ‘CC’ or ‘CP’ or ‘NS’                                                                                                     |
| 750     | EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT - All SCH.6 Event reason codes, except ‘CI’ require SCH.25 Filler status to be ‘F’ Final and accordingly only ‘CI’ and NULL should have SCH.25 Filler status to be ‘P’ Pending |
| 800     | FILLER STATUS IS MISSING OR IS INVALID                                                                                                                                                                                             |
| 850     | ADMIT TYPE IS INVALID (table SD009)                                                                                                                                                                                                |
| R       | WHOLE BATCH REJECTED                                                                                                                                                                                                               |

R – whole batch reject may be currently generated only by manual batch rejection.

### ### Table VA088 – DSS ID and DSS Credit Stop

Please note that this table is updated yearly and the current set up should be evaluated.

| **VALUE**   | **DESCRIPTION**                    | **Allow Either**   | **Primary**   | **Secondary**   | **Inactive Date**   |
|-------------|------------------------------------|--------------------|---------------|-----------------|---------------------|
| 101         | EMERGENCY UNIT                     |                    |               | S               |                     |
| 102         | ADMITTING/SCREENING                | E                  |               |                 |                     |
| 103         | TELEPHONE TRIAGE                   |                    | P             |                 |                     |
| 104         | PULMONARY FUNCTION                 | E                  |               |                 |                     |
| 105         | X-RAY                              | E                  |               |                 |                     |
| 106         | EEG                                | E                  |               |                 |                     |
| 107         | EKG                                |                    | P             |                 |                     |
| 108         | LABORATORY                         | E                  |               |                 |                     |
| 109         | NUCLEAR MEDICINE                   | E                  |               |                 |                     |
| 110         | CARDIOVASCULAR NUCLEAR MED         | E                  |               |                 | OCT 1,1998          |
| 111         | ONCOLOGICAL NUCLEAR MED            | E                  |               |                 | OCT 1,1998          |
| 112         | INFECTIOUS DISEASE NUCLEAR MED     | E                  |               |                 | OCT 1,1998          |
| 113         | RADIONUCLIDE TREATMENT             | E                  |               |                 | OCT 1,1998          |
| 114         | SING PHOTON EMISS TOMOGRAPHY       | E                  |               |                 | OCT 1,1998          |
| 115         | ULTRASOUND                         | E                  |               |                 |                     |
| 116         | RESPIRATORY THERAPY                | E                  |               |                 |                     |
| 117         | NURSING (2ND ONLY)                 |                    |               | S               |                     |
| 118         | HOME TREATMENT SERVICES            |                    | P             |                 |                     |
| 119         | COMM NURSING HOME FOLLOW-UP        | E                  |               |                 |                     |
| 120         | HEALTH SCREENING                   | E                  |               |                 |                     |
| 121         | RESIDENTIAL CARE (NON-MH)          | E                  |               |                 |                     |
| 122         | PUBLIC HEALTH NURSING              | E                  |               |                 |                     |
| 123         | NUTRITION/DIETETICS-INDIVIDUAL     | E                  |               |                 |                     |
| 124         | NUTRITION/DIETETICS-GROUP          | E                  |               |                 |                     |
| 125         | SOCIAL WORK SERVICE                | E                  |               |                 |                     |
| 126         | EVOKED POTENTIAL                   | E                  |               |                 |                     |
| 127         | TOPOGRAPHICAL BRAIN MAPPING        | E                  |               |                 |                     |
| 128         | PROLONGED VIDEO-EEG MONITORING     | E                  |               |                 |                     |
| 129         | HYPERTENSION SCREENING             | E                  |               |                 | OCT 1,1991          |
| 130         | CHOLESTEROL SCREENING              | E                  |               |                 | OCT 1,1991          |
| 131         | BREAST CANCER SCREENING            | E                  |               |                 | OCT 1,1991          |
| 132         | MAMMOGRAM                          | E                  |               |                 | OCT 1,1991          |
| 133         | CERVICAL CANCER SCREENING          | E                  |               |                 | OCT 1,1991          |
| 134         | PAP TEST                           | E                  |               |                 | OCT 1,1991          |
| 135         | COLORECTAL CANCER SCREENING        | E                  |               |                 | OCT 1,1991          |
| 136         | FOBT - GUIAC SCREENING             | E                  |               |                 | OCT 1,1991          |
| 137         | ALCOHOL COUNSELING - MED CARE      | E                  |               |                 | OCT 1,1991          |
| 138         | SMOKING CESSATION                  | E                  |               |                 | OCT 1,1991          |
| 139         | WEIGHT CONTROL                     | E                  |               |                 | OCT 1,1991          |
| 140         | PHYS FITNESS/EXERCISE COUNSEL      | E                  |               |                 | OCT 1,1991          |
| 141         | VET IMMUNIZATION                   | E                  |               |                 | OCT 1,1991          |
| 142         | COLORECTAL CA SCREEN DIG EXAM      | E                  |               |                 | OCT 1,1991          |
| 143         | READJUST COUNSEL                   | E                  |               |                 | JAN 1,1988          |
| 144         | RADIONUCLIDE THERAPY               | E                  |               |                 |                     |
| 145         | PHARM/PHYSIO NMP STUDIES           | E                  |               |                 |                     |
| 146         | PET                                | E                  |               |                 |                     |
| 147         | TELEPHONE/ANCILLARY                |                    | P             |                 |                     |
| 148         | TELEPHONE/DIAGNOSTIC               |                    | P             |                 |                     |
| 149         | RADIATION THERAPY TREATMENT        | E                  |               |                 |                     |
| 150         | COMPUTERIZED TOMOGRAPHY (CT)       | E                  |               |                 |                     |
| 151         | MAGNETIC RESONANCE IMAGING/MRI     | E                  |               |                 |                     |
| 152         | ANGIOGRAM CATHETERIZATION          | E                  |               |                 |                     |
| 153         | INTERVENTIONAL RADIOGRAPHY         | E                  |               |                 |                     |
| 154         | MEG (MAGNETOENCEPHALOGRAPHY)       | E                  |               |                 |                     |
| 155         | INFO ASSISTS TECHNOLOGY            | E                  |               |                 |                     |
| 160         | CLINICAL PHARMACY                  |                    |               | S               |                     |
| 161         | TRANSITIONAL PHARMACY              |                    | P             |                 |                     |
| 163         | CHAPLAIN-CLINICAL SVCS-INDIV       | E                  |               |                 | OCT 1,2002          |
| 164         | CHAPLAIN-CLINICAL SVCS-GROUP       | E                  |               |                 | OCT 1,2002          |
| 165         | BEREAVEMENT COUNSELING             | E                  |               |                 |                     |
| 166         | CHAPLAIN SERVICE - INDIVIDUAL      | E                  |               |                 |                     |
| 167         | CHAPLAIN SERVICE - GROUP           | E                  |               |                 |                     |
| 168         | CHAPLAIN SERVICE - COLLATERAL      | E                  |               |                 |                     |
| 169         | TELEPHONE/CHAPLAIN                 |                    | P             |                 |                     |
| 170         | HBPC - PHYSICIAN                   |                    | P             |                 |                     |
| 171         | HBPC - RN/RNP/PA                   |                    | P             |                 |                     |
| 172         | HBPC - NURSE EXTENDER              |                    | P             |                 |                     |
| 173         | HBPC - SOCIAL WORKER               |                    | P             |                 |                     |
| 174         | HBPC - THERAPIST                   |                    | P             |                 |                     |
| 175         | HBPC - DIETITIAN                   |                    | P             |                 |                     |
| 176         | HBPC - CLINICAL PHARMACIST         |                    | P             |                 |                     |
| 177         | HBPC - OTHER                       |                    | P             |                 |                     |
| 178         | HBPC/TELEPHONE                     |                    | P             |                 |                     |
| 179         | HOME TELEVIDEO CARE                |                    |               | S               |                     |
| 180         | DENTAL                             | E                  |               |                 |                     |
| 181         | TELEPHONE/DENTAL                   |                    | P             |                 |                     |
| 185         | PHYS EXTND NP (NRS PRCNR) 2ND      |                    |               | S               |                     |
| 186         | PHYS EXTND PA (PHYS ASST) 2ND      |                    |               | S               |                     |
| 187         | PHYS EXTND CNS (CLN RN SPC)2ND     |                    |               | S               |                     |
| 190         | ADULT DAY HEALTH CARE              | E                  |               |                 |                     |
| 201         | PHYSICAL MED & REHAB SVC           | E                  |               |                 |                     |
| 202         | RECREATION THERAPY SERVICE         | E                  |               |                 |                     |
| 203         | AUDIOLOGY                          | E                  |               |                 |                     |
| 204         | SPEECH PATHOLOGY                   | E                  |               |                 |                     |
| 205         | PHYSICAL THERAPY                   | E                  |               |                 |                     |
| 206         | OCCUPATIONAL THERAPY               | E                  |               |                 |                     |
| 207         | PM&RS INCENTIVE THERAPY            | E                  |               |                 |                     |
| 208         | PM&RS COMPENSATED WORK THERAPY     | E                  |               |                 |                     |
| 209         | VIST COORDINATOR                   | E                  |               |                 |                     |
| 210         | SPINAL CORD INJURY                 | E                  |               |                 |                     |
| 211         | AMPUTATION FOLLOW-UP CLINIC        | E                  |               |                 |                     |
| 212         | EMG - ELECTROMYOGRAM               | E                  |               |                 |                     |
| 213         | PM&RS VOCATIONAL ASSISTANCE        | E                  |               |                 |                     |
| 214         | KINESIOTHERAPY                     | E                  |               |                 |                     |
| 215         | SCI HOME CARE PROGRAM              | E                  |               |                 |                     |
| 216         | TELEPHONE/REHAB AND SUPPORT        |                    | P             |                 |                     |
| 217         | BROS (BLIND REHAB O/P SPEC)        | E                  |               |                 |                     |
| 218         | CAT BLIND REHAB                    | E                  |               |                 |                     |
| 219         | TBI (TRAUMATIC BRAIN INJURY)       | E                  |               |                 |                     |
| 220         | VISOR (VISUAL IMPAIRMENT OUTPA     | E                  |               |                 |                     |
| 290         | OBSERVATION MEDICINE               |                    | P             |                 |                     |
| 291         | OBSERVATION SURGERY                |                    | P             |                 |                     |
| 292         | OBSERVATION PSYCHIATRY             |                    | P             |                 |                     |
| 293         | OBSERVATION NEUROLOGY              |                    | P             |                 |                     |
| 294         | OBSERVATION BLIND REHAB            |                    | P             |                 |                     |
| 295         | OBSERVATION SPINAL CORD            |                    | P             |                 |                     |
| 296         | OBSERVATION REHABILITATION         |                    | P             |                 |                     |
| 301         | GENERAL INTERNAL MEDICINE          | E                  |               |                 |                     |
| 302         | ALLERGY IMMUNOLOGY                 | E                  |               |                 |                     |
| 303         | CARDIOLOGY                         | E                  |               |                 |                     |
| 304         | DERMATOLOGY                        | E                  |               |                 |                     |
| 305         | ENDO./METAB (EXCEPT DIABETES)      | E                  |               |                 |                     |
| 306         | DIABETES                           | E                  |               |                 |                     |
| 307         | GASTROENTEROLOGY                   | E                  |               |                 |                     |
| 308         | HEMATOLOGY                         | E                  |               |                 |                     |
| 309         | HYPERTENSION                       | E                  |               |                 |                     |
| 310         | INFECTIOUS DISEASE                 | E                  |               |                 |                     |
| 311         | PACEMAKER                          | E                  |               |                 |                     |
| 312         | PULMONARY/CHEST                    | E                  |               |                 |                     |
| 313         | RENAL/NEPHROL(EXCEPT DIALYSIS)     | E                  |               |                 |                     |
| 314         | RHEUMATOLOGY/ARTHRITIS             | E                  |               |                 |                     |
| 315         | NEUROLOGY                          | E                  |               |                 |                     |
| 316         | ONCOLOGY/TUMOR                     | E                  |               |                 |                     |
| 317         | COUMADIN CLINIC                    | E                  |               |                 |                     |
| 318         | GERIATRIC CLINIC                   | E                  |               |                 |                     |
| 319         | GERIATRIC EVAL. & MGMT. (GEM)      | E                  |               |                 |                     |
| 320         | ALZHEIMER'S/DEMENTIA CLINIC        | E                  |               |                 |                     |
| 321         | GI ENDOSCOPY                       | E                  |               |                 |                     |
| 322         | WOMEN'S CLINIC                     | E                  |               |                 |                     |
| 323         | PRIMARY CARE/MEDICINE              | E                  |               |                 |                     |
| 324         | TELEPHONE/MEDICINE                 |                    | P             |                 |                     |
| 325         | TELEPHONE/NEUROLOGY                |                    | P             |                 |                     |
| 326         | TELEPHONE/GERIATRICS               |                    | P             |                 |                     |
| 327         | MED MD PERFORM INVASVE OR PROC     |                    | P             |                 |                     |
| 328         | MEDICAL/SURGICAL DAY UNIT MSDU     | E                  |               |                 |                     |
| 329         | MEDICAL PROCEDURE UNIT             | E                  |               |                 |                     |
| 330         | CHEMOTHERAPY PROC. UNIT-MED.       | E                  |               |                 |                     |
| 331         | PRE-BED CARE MD (MEDICINE)         | E                  |               |                 |                     |
| 332         | PRE-BED CARE RN (MEDICINE)         | E                  |               |                 |                     |
| 333         | CARDIAC CATHETERIZATION            | E                  |               |                 |                     |
| 334         | CARDIAC STRESS TEST/ETT            | E                  |               |                 |                     |
| 335         | PADRECC PARKINSON'SDISEASERECC     | E                  |               |                 |                     |
| 350         | GERIATRIC PRIMARY CARE             | E                  |               |                 |                     |
| 351         | ADVNCD ILLNESS COOR CARE(AICC)     | E                  |               |                 |                     |
| 370         | LTC SCREENING (2ND ONLY)           |                    |               | S               |                     |
| 401         | GENERAL SURGERY                    | E                  |               |                 |                     |
| 402         | CARDIAC SURGERY                    | E                  |               |                 |                     |
| 403         | ENT                                | E                  |               |                 |                     |
| 404         | GYNECOLOGY                         | E                  |               |                 |                     |
| 405         | HAND SURGERY                       | E                  |               |                 |                     |
| 406         | NEUROSURGERY                       | E                  |               |                 |                     |
| 407         | OPHTHALMOLOGY                      | E                  |               |                 |                     |
| 408         | OPTOMETRY                          | E                  |               |                 |                     |
| 409         | ORTHOPEDICS                        | E                  |               |                 |                     |
| 410         | PLASTIC SURGERY                    | E                  |               |                 |                     |
| 411         | PODIATRY                           | E                  |               |                 |                     |
| 412         | PROCTOLOGY                         | E                  |               |                 |                     |
| 413         | THORACIC SURGERY                   | E                  |               |                 |                     |
| 414         | UROLOGY                            | E                  |               |                 |                     |
| 415         | VASCULAR SURGERY                   | E                  |               |                 |                     |
| 416         | AMB SURGERY EVAL BY NON-MD         | E                  |               |                 |                     |
| 417         | PROSTHETICS/ORTHOTICS              | E                  |               |                 |                     |
| 418         | AMPUTATION CLINIC                  | E                  |               |                 |                     |
| 419         | ANESTHESIA PRE/POST-OP CONSULT     | E                  |               |                 |                     |
| 420         | PAIN CLINIC                        | E                  |               |                 |                     |
| 421         | VASCULAR LABORATORY                | E                  |               |                 |                     |
| 422         | CAST CLINIC                        | E                  |               |                 |                     |
| 423         | PROSTHETIC SUPPLY DISPENSED        | E                  |               |                 |                     |
| 424         | TELEPHONE/SURGERY                  |                    | P             |                 |                     |
| 425         | TELEPHONE/PROSTHETICS/ORTHOTIC     |                    | P             |                 |                     |
| 426         | WOMEN SURGERY                      | E                  |               |                 |                     |
| 427         | PRIMARY CARE/SURGERY               | E                  |               |                 | OCT 1,1997          |
| 428         | TELEPHONE/OPTOMETRY                |                    | P             |                 |                     |
| 429         | OUTPATIENT CARE IN OR              |                    | P             |                 |                     |
| 430         | CYSTO ROOM UNIT FOR OUTPATIENT     | E                  |               |                 |                     |
| 431         | CHEMOTHERAPY PROC. UNIT-SURG.      | E                  |               |                 |                     |
| 432         | PRE-BED CARE MD (SURGERY)          | E                  |               |                 |                     |
| 433         | PRE-BED CARE RN (SURGERY)          | E                  |               |                 |                     |
| 435         | SURGICAL PROCEDURE UNIT            | E                  |               |                 |                     |
| 436         | CHIROPRACTIC CARE IN MED CTR       | E                  |               |                 |                     |
| 449         | FITTING & ADJSTMNTS 2ND ONLY       |                    |               | S               |                     |
| 450         | COMPENSATION & PENSION             |                    |               | S               |                     |
| 451 to 456  | Local use                          |                    |               | S               |                     |
| 457         | TRANSPLANT                         |                    |               | S               |                     |
| 458 to 473  | Local use  (delete 473 TBPPD SHOT) |                    |               | S               |                     |
| 474         | RESEARCH                           |                    |               | S               |                     |
| 475 to 479  | Local use                          |                    |               | S               |                     |
| 480         | COMPREHENSIVE FUNDOSCOPY           |                    |               | S               |                     |
| 481         | BRONCHOSCOPY                       |                    |               | S               |                     |
| 482 to 485  | Local use                          |                    |               | S               |                     |
| 501         | HOMELESS MENTALLY ILL OUTREACH     | E                  |               |                 | OCT 1,1994          |
| 502         | MENTAL HEALTH CLINIC -             | E                  |               |                 |                     |
| 503         | MH RESIDENTIAL CARE                | E                  |               |                 |                     |
| 504         | IPCC MEDICAL CENTER VISIT          | E                  |               |                 | APR 1,1997          |
| 505         | DAY TREATMENT-INDIVIDUAL           | E                  |               |                 |                     |
| 506         | DAY HOSPITAL-INDIVIDUAL            | E                  |               |                 |                     |
| 507         | DRUG DEPENDENCE-INDIVIDUAL         | E                  |               |                 | APR 1,1997          |
| 508         | ALCOHOL TREATMENT-INDIVIDUAL       | E                  |               |                 | APR 1,1997          |
| 509         | PSYCHIATRY-MD INDIVIDUAL           | E                  |               |                 |                     |
| 510         | PSYCHOLOGY-INDIVIDUAL              | E                  |               |                 |                     |
| 511         | NEUROBEHAVIORAL-INDIVIDUAL         | E                  |               |                 | OCT 1,1993          |
| 512         | PSYCHIATRY CONSULTATION            | E                  |               |                 |                     |
| 513         | SUBSTANCE ABUSE - INDIVIDUAL       | E                  |               |                 |                     |
| 514         | SUBSTANCE ABUSE - HOME VISIT       | E                  |               |                 |                     |
| 515         | CWT/TR-HCMI                        | E                  |               |                 | APR 1,1997          |
| 516         | PTSD - GROUP                       | E                  |               |                 |                     |
| 516         | PTSD - GROUP                       | E                  |               |                 |                     |
| 517         | CWT SUBSTANCE ABUSE                | E                  |               |                 | APR 1,1997          |
| 518         | CWT/TR-SUBSTANCE ABUSE             | E                  |               |                 | APR 1,1997          |
| 519         | SUBST USE DISORDER/PTSD TEAMS      | E                  |               |                 |                     |
| 520         | LONG-TERM ENHANCEMENT, INDIVID     | E                  |               |                 |                     |
| 521         | LONG-TERM ENHANCEMENT, GROUP       | E                  |               |                 |                     |
| 522         | HUD/VASH                           | E                  |               |                 |                     |
| 523         | OPIOID SUBSTITUTION                | E                  |               |                 |                     |
| 524         | ACTIVE DUTY SEX TRAUMA             | E                  |               |                 |                     |
| 525         | WOMEN'S STRESS DISORDER TEAMS      | E                  |               |                 |                     |
| 526         | TELEPHONE/SPECIAL PSYCHIATRY       | E                  |               |                 | APR 1,1997          |
| 527         | TELEPHONE/GENERAL PSYCHIATRY       |                    | P             |                 |                     |
| 528         | TELE/HOMELESS MENTALLY ILL         |                    | P             |                 |                     |
| 529         | HCHV/HMI                           |                    | P             |                 |                     |
| 530         | TELEPHONE/HUD-VASH                 |                    | P             |                 |                     |
| 531         | MH PRIMARY CARE TEAM -             | E                  |               |                 |                     |
| 532         | PSYCHOSOCIAL REHAB -               | E                  |               |                 |                     |
| 533         | MH INTERVNTION BIOMED CARE         | E                  |               |                 |                     |
| 535         | MH VOCATIONAL ASSISTANCE -         | E                  |               |                 |                     |
| 536         | TELEPHONE/MH VOC ASSISTANCE        |                    | P             |                 |                     |
| 537         | TELEPHONE/PSYCHOSOCIAL REHAB       |                    | P             |                 |                     |
| 538         | PSYCHOLOGICAL TESTING              | E                  |               |                 |                     |
| 540         | PCT POST-TRAUMATIC STRESS-IND      |                    | P             |                 |                     |
| 541         | PTSD POST-TRAUMATIC STRESS         | E                  |               |                 | JAN 1,1991          |
| 542         | TELEPHONE/PTSD                     |                    | P             |                 |                     |
| 543         | TELEPHONE/ALCOHOL DEPENDENCE       | E                  |               |                 | APR 1,1997          |
| 544         | TELEPHONE/DRUG DEPENDENCE          | E                  |               |                 | APR 1,1997          |
| 545         | TELEPHONE/SUBSTANCE ABUSE          |                    | P             |                 |                     |
| 546         | TELEPHONE/MHICM                    |                    | P             |                 |                     |
| 547         | INTENSIVE SUBSTANCE ABUSE TRMT     | E                  |               |                 |                     |
| 550         | MENTAL HEALTH CLINIC-GROUP         | E                  |               |                 |                     |
| 551         | IPCC COMM CLN/DAY PROGRAM VST      | E                  |               |                 | APR 1,1997          |
| 552         | MENTAL HLT INT CASE MGT(MHICM)     |                    | P             |                 |                     |
| 553         | DAY TREATMENT-GROUP                | E                  |               |                 |                     |
| 554         | DAY HOSPITAL-GROUP                 | E                  |               |                 |                     |
| 555         | DRUG DEPENDENCE-GROUP              | E                  |               |                 | APR 1,1997          |
| 555         | DRUG DEPENDENCE-GROUP              | E                  |               |                 | APR 1,1997          |
| 556         | ALCOHOL TREATMENT-GROUP            | E                  |               |                 | APR 1,1997          |
| 557         | PSYCHIATRY - MD GROUP              | E                  |               |                 |                     |
| 558         | PSYCHOLOGY-GROUP                   | E                  |               |                 |                     |
| 559         | PSYCHOSOCIAL REHAB - GROUP         | E                  |               |                 |                     |
| 560         | SUBSTANCE ABUSE - GROUP            | E                  |               |                 |                     |
| 561         | PCT-POST TRAUMATIC STRESS-GRP      |                    | P             |                 |                     |
| 562         | PTSD - INDIVIDUAL                  | E                  |               |                 |                     |
| 562         | PTSD - INDIVIDUAL                  | E                  |               |                 |                     |
| 563         | MH PRIMARY CARE TEAM - GROUP       | E                  |               |                 |                     |
| 564         | MH TEAM CASE MANAGEMENT            | E                  |               |                 |                     |
| 565         | MH MEDICAL CARE ONLY-GROUP         | E                  |               |                 |                     |
| 566         | MH RISK-FACTOR-REDUCTION ED GR     | E                  |               |                 |                     |
| 567         | MHICM GRP MTLHLTH INTSV CS MGT     |                    | P             |                 |                     |
| 571         | READJUSTMENT COUNSELING-INDIV      | E                  |               |                 | JAN 31,1994         |
| 572         | READJUSTMENT COUNSELING-GROUP      | E                  |               |                 | JAN 31,1994         |
| 573         | MH INCENTIVE THERAPY - GROUP       | E                  |               |                 |                     |
| 574         | MH COMP WORK THERAPY (CWT) GRP     | E                  |               |                 |                     |
| 575         | MH VOCATIONAL ASSISTANCE-GRP       | E                  |               |                 |                     |
| 576         | PSYCHOGERIATRIC - INDIVIDUAL       | E                  |               |                 |                     |
| 577         | PSYCHOGERIATRIC CLINIC - GROUP     | E                  |               |                 |                     |
| 578         | PSYCHOGERIATRIC DAY PROGRAM        | E                  |               |                 |                     |
| 579         | TELEPHONE/PSYCHOGERIATRICS         |                    | P             |                 |                     |
| 580         |                                    | E                  |               |                 |                     |
| 581         | PTSD DAY TREATMENT                 | E                  |               |                 |                     |
| 589         | NON-ACTIVE DUTY SEX TRAUMA         | E                  |               |                 |                     |
| 590         | COMM OUTREACH HOMELESS VETS        | E                  |               |                 |                     |
| 601         | ACUTE HEMODIAL TREATMENT           | E                  |               |                 | OCT 1,1990          |
| 602         | CHRON ASSISTED HEMODIAL TREAT      |                    | P             |                 |                     |
| 603         | LIM SELF CARE HEMODIAL TREAT       |                    | P             |                 |                     |
| 604         | HOME/SELF HEMODIAL TRAIN TREAT     |                    | P             |                 |                     |
| 605         | ACUTE PERITONEAL DIAL TREAT        |                    | P             |                 | OCT 1,1990          |
| 606         | CHRON ASSISTED PERIT DIALYSIS      |                    | P             |                 |                     |
| 607         | LIM SELF CARE PERIT DIALYSIS       |                    | P             |                 |                     |
| 608         | HOME/SELF PERIT DIALYSIS TRAIN     |                    | P             |                 |                     |
| 610         | CONTRACT DIALYSIS                  |                    | P             |                 |                     |
| 611         | TELEPHONE/DIALYSIS                 |                    | P             |                 |                     |
| 640         | SEND-OUT PROCS NOT FEE             |                    | P             |                 |                     |
| 641         | SEND-OUT PROCS-DOD NOT FEE         |                    | P             |                 |                     |
| 642         | SEND-OUT PROCS FEE                 |                    | P             |                 |                     |
| 650         | CONTRACT NURSING HOME DAYS         |                    | P             |                 |                     |
| 651         | STATE NURSING HOME DAYS            |                    | P             |                 |                     |
| 652         | STATE DOMICILIARY HOME DAYS        |                    | P             |                 |                     |
| 653         | STATE HOSPITAL CARE                |                    | P             |                 |                     |
| 654         | NON VA RESIDENTIAL CARE DAYS       |                    | P             |                 |                     |
| 655         | COMMUNITY NON-VA CARE              |                    | P             |                 |                     |
| 656         | DOD NON-VA CARE                    |                    | P             |                 |                     |
| 657         | ASSIST LIVING VENDOR WORK          |                    | P             |                 |                     |
| 660         | CHIROPRACTIC CARE OUTSIDE VA       |                    | P             |                 |                     |
| 670         | ASSIST LIVING, VHA-PAID STAFF      |                    | P             |                 |                     |
| 680         | HOME/COMMUN HEALTHCARE ASSESS      | E                  |               |                 |                     |
| 681         | VA-PAID HOME/COMMUN HEALTHCARE     |                    | P             |                 |                     |
| 682         | VA-REFER HOME/COMMUN CARE PROV     |                    | P             |                 |                     |
| 683         | NONVIDEO HOME TELEHEALTH MONIT     |                    | P             |                 |                     |
| 684         | NONVIDEO HOME TELEHEALTH INTER     |                    |               | S               |                     |
| 690         | TELEMEDICINE                       |                    |               | S               |                     |
| 691         | PRE-EMP PHYS MILITRY PERSONNEL     | E                  |               |                 |                     |
| 692         | TELMD CNSLT SM STA 2ND ONLY        |                    |               | S               |                     |
| 693         | TELMD CNSLT NOT SM STA 2NDONLY     |                    |               | S               |                     |
| 701         | BLOOD PRESSURE CHECK               |                    |               | S               |                     |
| 702         | CHOLESTEROL SCREENING              |                    |               | S               | OCT 1,2002          |
| 703         | MAMMOGRAM (CAN BE PRIMARY)         | E                  |               |                 |                     |
| 704         | PAP TEST                           |                    |               | S               |                     |
| 705         | FOBT - GUIAC SCREENING             |                    |               | S               | OCT 1,2002          |
| 706         | ALCOHOL SCREENING                  |                    |               | S               |                     |
| 707         | SMOKING CESSATION                  |                    |               | S               |                     |
| 708         | NUTRITION                          |                    |               | S               | OCT 1,2002          |
| 709         | PHY FIT/EXERCISE COUNSELING        |                    |               | S               | OCT 1,2002          |
| 710         | INFLUENZA IMMUNIZATION             |                    |               | S               |                     |
| 711         | INJURY COUNSEL/SEAT BELT USAGE     |                    |               | S               | OCT 1,2002          |
| 712         | HEP C REGISTRY PATIENT             |                    |               | S               |                     |
| 713         | GAMBLING ADDICTION (2ND ONLY)      |                    |               | S               |                     |
| 714         | OTHER EDUCATION 2ND ONLY           |                    |               | S               |                     |
| 715         | ONGOING TRTMT (NON-MH) 2ND         |                    |               | S               |                     |
| 716         | POST SURG RTINE AFTRCARE 2ND       |                    |               | S               |                     |
| 725         | DOMICILIARY OUTREACH SERVICES      | E                  |               |                 |                     |
| 726         | DOM AFTERCARE - COMMUNITY          | E                  |               |                 |                     |
| 727         | DOMICILIARY AFTERCARE - VA         | E                  |               |                 |                     |
| 728         | DOMICILIARY ADM SCREENING SVCS     | E                  |               |                 |                     |
| 729         | TELEPHONE/DOMICILIARY              |                    | P             |                 |                     |
| 730         | DOM GENERAL CARE                   | E                  |               |                 |                     |
| 731         | PRRTP GENERAL CARE                 | E                  |               |                 |                     |
| 801         | IN-VISN, OTHER VAMC 2ND ONLY       |                    |               | S               |                     |
| 802         | OUT OF  2NDARY ONLY                |                    |               | S               |                     |
| 803         | COMMERCIAL 2NDARY ONLY             |                    |               | S               |                     |
| 900         | SPECIAL SERVICES                   | E                  |               |                 | OCT 1,1998          |
| 902         | COMPUTED TOMOGRAPHY SCANS          | E                  |               |                 | APR 1,1989          |
| 903         | RADIATION THERAPY                  | E                  |               |                 | APR 1,1989          |
| 904         | CHEMOTHERAPY                       | E                  |               |                 | MAR 1,1989          |
| 905         | AMBULATORY SURGERY SERVICES        | E                  |               |                 | APR 1,1989          |
| 906         | BLOOD/BLOOD PRODUCTS TRANS.        | E                  |               |                 | APR 1,1989          |
| 907         | NUCLEAR MAGNETIC RESONANCE         | E                  |               |                 | APR 1,1989          |
| 999         | EMPLOYEE HEALTH                    |                    | P             |                 |                     |

### Appointment Selection Logic

The initial run of the Patient Appointment Information Transmission logic will review and select all pending patient appointments created one year prior to the run date. That date was determined to be Sep 1 st , 2002. Additionally, pending appointments created since Sep 1 st 2002 are submitted as well.  There are two appointment statuses: pending and final. The appointment can be sent only once for a pending and once for a final status, for example, an appointment sent for the first time with a pending status will be sent again if its status is changed to final.  An appointment with a final status, sent for the first time, will not be sent again.

The Patient Appointment Info Log file (#409.6) is created to track the transmitted appointments.

On subsequent transmissions all appointments with the Date Appointment Created after the prior transmission are added to the new transmission. The Patient Appointment Info Log file is examined for appointments whose statuses have changed from pending to final and they are also added to the new transmission by creating new entries in the Patient Appointment Info Log file.  Those new entries are created with the Retention Flag field equals “N”, corresponding to the Final status.  The Retention Flag in the original entry is changed from “Y” to “S” – Sent as Final or to “R” – Sent as Rejected if the original entry was rejected.

The final or pending status of an appointment is determined by its associated primary and secondary identifiers, Defined as SCH6 Event Reason and SCH.8 Appt Type.  Please note that all ‘check-out (CO)’ appointments are considered to be final, including those that are still ‘action required (AR). That decision has been made on an assumption that the appointment is final when the ‘check-out’ process is initiated,  meaning a patient is present for the appointment. The identifiers, SCH.6 Event Reason and SCH.8 Appointment Type, as well as pending versus final status, represented by SCH.25 Filler status, are mapped in the SIU Event Mapping Table.

The identifiers were determined to reflect the existing computed appointment status in  application.  Additionally several new identifiers are defined, for allowing to trace continuity of canceled and rescheduled appointments, and for selecting proper appointments from the scheduled ‘non-count’ clinic group.

All update records should be Final and their previous base records, if any, should be Pending. With the update transmission you receive Pending and Final records but Finals may be new ones or updates to the previously sent Pending appointments. All new Pending records are generated starting from the last creation date from the previous transmission.

**SIU Event Mapping Table**

| **SIU Event**   | **SCH.25 Filler status**   | **SCH.6 Event Reason**       | **SCH.8 Appt Type**    |
|-----------------|----------------------------|------------------------------|------------------------|
| S12             | Pending                    | Check-in (CI)                | Action required (AR)   |
| S12             | Pending                    |                              | No Action Taken (NAT)  |
| S12             | Pending                    |                              | Future (F)             |
| S12             | Pending                    |                              | Non Count (NC)         |
| S12             | Pending                    |                              | Inpatient (I)          |
| S12             | Pending                    |                              | Non Count Future (NCF) |
| S26             | Final                      | No Show (NS)                 |                        |
| S26             | Final                      | No Show (NS)                 | Auto Rebook (ABK)      |
| S15             | Final                      | Cancelled by Clinic (CC)     | Re-schedule (RS)       |
| S 15            | Final                      | Cancelled by Clinic (CC)     |                        |
| S15             | Final                      | Cancelled by Clinic (CC)     | Auto Rebook (ABK)      |
| S15             | Final                      | Cancelled by Patient (CP)    | Re-schedule (RS)       |
| S15             | Final                      | Cancelled by Patient (CP)    |                        |
| S15             | Final                      | Cancelled by Patient (CP)    | Auto Rebook (ABK)      |
| S12 or S14      | Final                      | Check Out by Encounter (COE) | Non Count (NC)         |
| S12 or S14      | Final                      | No Match (NM)                | Non Count (NC)         |
| S12 or S14      | Final                      | Check-out (CO)               | Action required (AR)   |
| S12 or S14      | Final                      | Check-out (CO)               | Inpatient (I)          |
| S12 or S14      | Final                      | Check-out (CO)               | Out patient (O)        |
| S15             | Final                      | Cancelled Terminated (CT)    |                        |

The above table expresses all of the appointment attributes required for a given appointment state.  Event reason and appointment type are interpreted as the primary and alternate identifiers.

Auto Rebook (ABK) – This appointment type represents an appointment that has been recently or originally rebooked. We may have appointments originally finalized in VistA as No Show with Auto Rebooking, but their status may be changed into any other status if No Show status is canceled in . In this way the originally entered Auto Rebooking Date may be sent with different Event Reason and/or Appointment Type, not related to the Auto Rebooked Date.

Re-scheduled (RS) – This appointment type is assigned to each canceled appointment if another appointment for a clinic with the same DSS ID (stop code) was scheduled on the same date as the cancellation took place. That situation occurs very often when the auto-rebooking feature is not used. There is an assumption that the newly scheduled appointment is a continuation of the canceled one.

Cancelled Terminated (CT) – This is the Even Reason identifier used to finalize an appointment that was sent as pending and then, during the update process it has been determined that a new appointment is created for the same date and time. That situation causes the previous appointment record to be overridden by the new appointment record with a new creation date.

Future (F ) – This Appointment Type applies to all appointments except created for

non-count Hospital Locations, that have Type: Non Count Future (NCF).

Non-count clinic appointments.

In the current  functionality, there are many non-count clinics that have scheduled appointments for valid patient care.  Any site that is using Event Capture and/or the Surgery packages set up NON COUNT clinics for scheduled appointments.  The encounters for these appointments are passed through a SEPARATE COUNT CLINIC with a status of CHECKED OUT. The process to capture those appointments has been established and it is described below.

Non Count Future (NCF )  -  Scheduled for non-count clinic for the future days starting from the next date to the running date

Check Out By Encounter (COE) . If there is an outpatient encounter entry with the Originating Process Type field (#.08) value equal 2 – Stop code Addition for the same date, and both DSS Clinic Id and  DSS Credit Stop match in non-count and count clinic then COE is assigned to the appointment and the count clinic data is returned with this final transmission for this appointment.

No Match (NM) This Event Reason is assigned if a related outpatient encounter, see above, has not been found. If this appointment is evaluated for the first time it is not sent at all. It will be sent with its final status if it was sent before as pending.

Non Count (NC) – This Appt Type without any value of the Event Reason is sent if its scheduled date already passed but not more than 2 days. That time is left because of a possible delay in updating a potential matching encounter.

### Acknowledgement Processing Logic

Acknowledgements are processed in enhanced mode, full two-phased commit.  A commit acknowledgement is requested and processed automatically by the  HL7 application.   Application acknowledgements from the receiving AAC application may generate three types of messages:  whole batch accept, whole batch accept with rejections, and whole batch reject. That last type has not been generated at this time and instead the SD-PAIT Manual Batch Rejection may be used.

### Whole Batch Accept

The batch message and all included messages are accepted by the receiving AAC application.  Upon receipt of this message the sending  application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message.  Internal cross-references are examined and those entries in which field #4, RETENTION FLAG, do not equal “Y”  ( For YES - to be sent when 'Final') are deleted from the file.

### Whole Batch Reject

The batch message and all included messages may be rejected by manual rejection and in the future by the receiving AAC application.  Upon receipt of this message the sending  application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message.  Field #7,  ERROR MESSAGE, is updated with the rejection code “R”.  If Field #4, RETENTION FLAG, equals “Y” ( For YES - to be sent when 'Final') entry updates are complete. The sending application will send those records again, even if they are final,,based on the rejection identified in the Error Message field (# 7).

If the RETENTION FLAG equals “N” (For NO - was sent as 'Final') then the RETENTION FLAG is changed to “Y”, making that entry available for resending, and entry updates are complete.  No entries in file 409.6 are deleted.

### Whole Batch Accept with Rejections

The batch message is accepted, but some individual messages are rejected by the receiving AAC application.  Upon receipt of this message the sending  application executes program logic to update entries in file 409.6, PATIENT APPOINTMENT INFO LOG, associated with the batch message.    Individual message rejections are processed in the same fashion as a whole batch rejection and the remaining messages, those accepted, are processed  as a whole batch accept **.**

Messages rejected individually may have the Error Message field (#7) updated with a pointer to one of rejection codes from table AAC001 –Error Code Set.

### Rejected Appointments Processing

All entries in the PATIENT APPOINTMENT INFO LOG  that were marked as rejected by the Acknowledgement processing, are evaluated during transmission as follows.

1. There is not a verification if the rejected entry was corrected. The acknowledgement sends a notification about rejects and if the rejection codes are listed, they should be corrected before the follow-up transmission.  Option SD-PAIT REJECTED should  be used to generate a report of rejected appointments.  If  only  a rejection code of “R” code was entered, nothing has to be done because such a message means that the whole batch was rejected and all related appointments will be sent again.

1. The rejected appointment is transmitted, again it does not matter if has been corrected or not, and a new entry is created in the PATIENT APPOINTMENT INFO LOG  with the current appointment status. The original entry marked as rejected is updated with “R” – Resent as Rejected in the Retention Flag field.

### Messages Examples

**Example Batch Message with the Consult Request Date – SCH.11**

BHS^~|\&amp;^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S12^5003236-1^D^2.4^^^AL^AL^USA

SCH^1^^^^^^4^NAT^^^~~~20030908~~~Date Appt Created|~~~~~~Desired Date|~~~200309180800~~~Appt

Date|~~~~~~Checkout Date|~~~~~~Cancellation Date|~~~~~~Auto-rebook Date|~~~~~~Resched

Date **|~~~200309010930~~~Consult Request Date** ^^^^^^^^^^^^^^P

PID^1^^""~~~USVHA&amp;&amp;L~NI|7171938~~~USVHA&amp;&amp;L~PI^^WOLFIK~EDZIU^^19301212^^^^~~~~19107^^^^^^^^2081212

30P

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^422~~~~~~~~CECELIA'S CLINIC^402~CARDIAC SURGERY~DSS Clinic ID^418~AMPUTATION CLINIC~DSS

Credit Stop

ZEN^1^^^^^^^^5

ZSP^1^N^

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-2^D^2.4^^^AL^AL^USA

SCH^1^^^^^CC^3^RS^^^~~~20030829~~~Date Appt Created|~~~20030829~~~Desired

Date|~~~200308291330~~~Appt Date|~~~~~~Checkout Date|~~~200308290940~~~Cancellation

Date|~~~~~~Auto-rebook Date|~~~200308291030~~~Resched Date **|~~~200308200820~~~Consult Request Date** ^^^^^^^^^^^^^^F

PID^1^^""~~~USVHA&amp;&amp;L~NI|7172069~~~USVHA&amp;&amp;L~PI^^YORTY~OUTPATIENT^^19710604^^^^~~~~17042^^^^^^^^509

060471P

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^614~~~~~~~~YORTY'S CLINIC^329~MEDICAL PROCEDURE UNIT~DSS Clinic ID^~~DSS

Credit Stop

ZEN^1^^^^^^^^1

ZSP^1^Y^60

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^5003236-3^D^2.4^^^AL^AL^USA

SCH^1^^^^^CP^3^RS^^^~~~20030829~~~Date Appt Created|~~~20030829~~~Desired

Date|~~~200309010815~~~Appt Date|~~~~~~Checkout Date|~~~200308290856~~~Cancellation

Date|~~~~~~Auto-rebook Date|~~~200309010815~~~Resched Date **|~~~200308010710~~~Consult Request Date** ^^^^^^^^^^^^^^F

PID^1^^""~~~USVHA&amp;&amp;L~NI|7172424~~~USVHA&amp;&amp;L~PI^^VILELLA~JOEY~ASHLEY~III~MR^^19490

416^^^^~~~~33354^^^^^^^^244990005

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^500

PV2^^^^^^^^^^^^^^^^^^^^^^^^NTF

AIL^1^^312~~~~~~~~XXXXX^102~ADMITTING/SCREENING~DSS Clinic ID^104~PULMONARY FUNCTION~DSS Credit

Stop

ZSP^1^N^

BTS^3

**Example Application Acknowledgement Message:**

BHS^~|\&amp;^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20030918085247-0500^^~P~ACK|S12~2.4~AL~NE^AA~^104^5001738

MSA^AA^5001738^

BTS^1

## Appendix B -  Interface Engine Site I.P. Addresses

You should know IP address from your messaging team, to be entered with SD-PAIT Logical Link. This is address to send PAIT in HL7 format to your local VIE box.

## Appendix C – Trouble Shooting

File 409.6 ( PATIENT APPOINTMENT INFO LOG) is populated with  SDPAIT transmission records and is self maintaining.  Entries are purged automatically when a final status appointment is transmitted and acknowledgements received.  No user or programmer intervention is required.

Members of the SD-PAIT mail group will receive notifications when batch transmissions are complete.  Mail group members will also be notified when acknowledgements to the batch messages are received.

### Mail Notifications

If mail message notifications are not received by members of the SD-PAIT mail group check the following:

Insure the SD-PAIT link is active by doing the following from the HL7 Main Menu

Select HL7 Main Menu Option:

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM     Systems Link Monitor

FM     Monitor, Start, Stop Filers

LM     TCP Link Manager Start/Stop

SA     Stop All Messaging Background Processes

RA     Restart/Start All Links and Filers

DF     Default Filers Startup

SL     Start/Stop Links

PI      Ping (TCP Only)

ED     Link Edit

ER     Link Errors ...

Select Filer and Link Management Options Option: SL  Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device.  Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: SD-PAIT

This LLP has been enabled!

### HL7 System Monitor

All outgoing HL7 messages are sent over this link.  You can verify activity on this link with the System Monitor Utility of  the HL7 package:

In the example screen above the TO SEND column lists 12 messages and the SENT column 1.  If your SENT column does not increment to match the TO SEND column it may be necessary to stop and then start the SD-PAIT link as mentioned above.

### Interface Engine

REDACTED

### XTMP Global

A temporary  snapshot of each record deleted by the HL7 acknowledgement processing logic is created in Global ^XTMP(“SDRPA-”\_BATCHNUMBER,

You may view this global to confirm acknowledgement processing.

### ### Reporting

Figure 1 indicates the reports that may be generated at each site after transmission has completed.  By entering the first three letters of the desired report will initiate that report.

Acknowledgement Summary

Pending Transmissions

Rejected Transmissions

Transmission Summary

Figure 1

Acknowledgement Summary:

The Acknowledgement Summary may be used to verify the batch numbers generated from a particular site (Figure 2).  This report lists all batches in Batch Control ID order.  The report also indicates the Message Control ID, the Acknowledgement Date, and Acknowledgement Type.  The following Acknowledgement Types are indicated:

Application Accept - AA

Application Error - AE

Application Reject - AR

Manual Rejection - MR

PAIT ACK SUMMARY                                                                                   FEB 27,2004  11:26    PAGE 1

APPLICATION ACK       APPLICATION ACK

BATCH CONTROL ID              MESSAGE CONTROL ID                   DATE/TIME                            TYPE

------------------------------------------------------------------------------------------------------------------------------------------------------------

TRANSMISSION FINISHED: FEB 20,2004  20:45

75611134952                                  75615626811                               FEB 24,2004  08:38     APPLICATION ACCEPT

75611135142                                  75615627064                               FEB 24,2004  08:39     APPLICATION ACCEPT

75611135273                                  75615627292                               FEB 24,2004  08:40     APPLICATION ACCEPT

75611135591                                  75615627625                               FEB 24,2004  08:41     APPLICATION ACCEPT

75611135943                                  75615628077                               FEB 24,2004  08:42     APPLICATION ACCEPT

75611136242                                  75615628454                               FEB 24,2004  08:43     APPLICATION ACCEPT

75611136597                                  75615628914                               FEB 24,2004  08:44     APPLICATION ACCEPT

75611136841                                  75615629306                               FEB 24,2004  08:45     APPLICATION ACCEPT

75611137250                                  75615629892                               FEB 24,2004  08:46     APPLICATION ACCEPT

75611137757                                  75615630556                               FEB 24,2004  12:49     APPLICATION ERROR

75611138197                                  75615631071                               FEB 24,2004  12:50     APPLICATION ACCEPT

75611138675                                  75615631643                               FEB 24,2004  12:50     APPLICATION ACCEPT

75611138981                                  75615632257                               FEB 24,2004  12:51     APPLICATION ACCEPT

75611139225                                  75615632561                               FEB 24,2004  12:52     APPLICATION ACCEPT

75611139441                                  75615632855                               FEB 24,2004  12:53     APPLICATION ACCEPT

75611139687                                  75615633142                               FEB 24,2004  12:54     APPLICATION ACCEPT

75611139729                                  75615633201                               FEB 24,2004  12:54     APPLICATION ACCEPT

75611139775                                  75615633241                               FEB 24,2004  12:55     APPLICATION ERROR

75611139829                                  75615633301                               FEB 24,2004  12:56     APPLICATION ACCEPT

75611139855                                  75615633327                               FEB 24,2004  12:56     APPLICATION ACCEPT

75611140007                                  75615633495                               FEB 24,2004  12:57     APPLICATION ACCEPT

75611140038                                  75615633536                               FEB 24,2004  12:58     APPLICATION ACCEPT

75611140066                                  75615633568                               FEB 24,2004  12:59     APPLICATION ACCEPT

75611140072                                  75615633574                               FEB 24,2004  13:00     APPLICATION ACCEPT

75611140100                                  75615633634                               FEB 24,2004  13:00     APPLICATION ACCEPT

75611140118                                  75615633652                               FEB 24,2004  13:01     APPLICATION ACCEPT

75611140124                                  75615633658                               FEB 24,2004  13:02     APPLICATION ACCEPT

75611140140                                  75615633672                               FEB 24,2004  13:02     APPLICATION ACCEPT

75611140150                                  75615633683                               FEB 24,2004  13:03     APPLICATION ACCEPT

75611140160                                  75615633693                               FEB 24,2004  13:04     APPLICATION ACCEPT

75611140170                                  75615633704                               FEB 24,2004  13:04     APPLICATION ACCEPT

75611140176                                  75615633710                               FEB 24,2004  13:05     APPLICATION ACCEPT

75611140188                                  75615633722                               FEB 24,2004  13:05     APPLICATION ACCEPT

75611140190                                  75615633724                               FEB 24,2004  13:05     APPLICATION ACCEPT

TRANSMISSION FINISHED: FEB 25,2004  16:02

75611182041                                  75615685674                               FEB 26,2004  10:41     APPLICATION ACCEPT

75611182938                                  75615686799                               FEB 26,2004  10:42     APPLICATION ERROR

Figure 2

> **NOTE:** AR – The whole batch rejection from the AAC has not been implemented at this time and will be future enhancement.  Figure 2 shows acknowledgements received for two transmissions.

Pending Transmission:

The Pending Transmission report (Figure 3) is to be used by  sites only to take an action of finalizing appointments with the appointment scheduled date (APPT\_DATE) already in the past.  These records should be “Check Out” or Cancelled.  This report lists all Patient Pending records by Date Appointment Made.  A print of the report is not included due to sensitive information.

Rejected Transmission:

The Rejected Transmission report should be used to review and correct patient records that the AAC rejected.  Rejections can occur due to incomplete dates, invalid site/facility codes not matching the site sending the information, etc. for a particular site (Figure 3). See table AAC001 - Error Code Set for rejection code definition.

The  should use this report for correcting their patient appointment records.  Once the  has corrected the record it will be sent to the National Data Base in the next bi-monthly update run and loaded into the National Database.  The correction of rejected records is the  site’s responsibility.

REJECTED TRANSMISSION LOG                                                                        FEB 27,2004  11:34    PAGE 1

ERROR

PATIENT                                               APPT DATE                      SHORT DESCRIPTION                           MESSAGE

CLINIC

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

ERROR MESSAGE: 350

PUBLIC,JOHN Q                            OCT  6,2003  15:56      HL7 date is not in proper format or is missing          350

FLU SHOT CLINIC

Figure 3

> **NOTE:** The most commonly expected rejection codes are 350 and 200, see TABLE  AAC001-Error Code Set.  Error 350 is mostly caused by too old desired date of appointment, filed in  sub file 1900 of the Patient File.

**Error 350**

It has been also determined that in some situation the Rescheduled date has not acceptable date starting from 1800. That Rescheduled date is identified by PAIT if the following process:

1. An appointment is canceled without re-booking.

2. If there is another appointment created on the same day as the cancellation date, and for the same clinic there is an assumption that this is continuation of that scheduling, and that new scheduled date/time is included with the original appointment as the Reschedule Date.

3. The first available appointment meeting criteria listed in 2. is processed.

4. It came out that randomly some appointments have their scheduled date/time starting from 1800, and this date is causing rejection by the AAC as well.

5. If you cannot find an '"odd" date with your original appointment you should look for "ADSAM" cross reference in the Patient file with the cancellation date and the patient DFN, to see what "odd" appointments were scheduled, and if so to remove them after evaluation what else needs to be done.

6. Removal of that "odd" appointment would prevent the original appointment from being sent with The "bad", not acceptable Rescheduled Date.

**Error 200**

Error 200 indicates that an entry in the Hospital Location file #44 is configured with the DIVISION field (3.5) pointing to a Medical Center Division entry whose Institution pointer conflicts with the facility station number.

Hint:  Correct the Hospital Location entry's Division field (3.5) to point to the correct Medical Center Division, or correct the Institution pointer of the Medical Center Division.

Transmission Summary:

The Transmission Summary report may be used to determine the total number of patient appointment records, the run date, total number of batches, Batch Control ID, Message Control ID, and date/time stamp (Figure 4). It can be requested by EVS, National Help Desk and /or AAC for matching transmitted batches with those received. at the AAC.

TRANSMISSION SUMMARY                                                                     FEB 27,2004  11:35    PAGE 1

LAST

SCANNED              # OF

RUN DATE               DATE         APPOINTMENTS

# OF                                  BATCH CREATE

BATCHES           BATCH CONTROL ID                DATE/TIME                     MESSAGE CONTROL ID

----------------------------------------------------------------------------------------------------------------------------------------------

FEB 20,2004        FEB 19,2004            165317

34                           75611134952                      FEB 20,2004  12:20                      75615626811

75611135142                      FEB 20,2004  12:36                      75615627064

75611135273                      FEB 20,2004  12:51                      75615627292

75611135591                      FEB 20,2004  13:09                      75615627625

75611135943                      FEB 20,2004  13:28                      75615628077

75611136242                      FEB 20,2004  13:42                      75615628454

75611136597                      FEB 20,2004  13:58                      75615628914

75611136841                      FEB 20,2004  14:14                      75615629306

75611137250                      FEB 20,2004  14:36                      75615629892

75611137757                      FEB 20,2004  14:59                      75615630556

75611138197                      FEB 20,2004  15:21                      75615631071

75611138675                      FEB 20,2004  15:42                      75615631643

75611138981                      FEB 20,2004  16:01                      75615632257

75611139225                      FEB 20,2004  16:18                      75615632561

75611139441                      FEB 20,2004  16:35                      75615632855

75611139687                      FEB 20,2004  16:51                      75615633142

75611139729                      FEB 20,2004  17:04                      75615633201

75611139775                      FEB 20,2004  17:17                      75615633241

75611139829                      FEB 20,2004  17:34                      75615633301

75611139855                      FEB 20,2004  17:48                      75615633327

75611140007                      FEB 20,2004  18:03                      75615633495

75611140038                      FEB 20,2004  18:17                      75615633536

75611140066                      FEB 20,2004  18:31                      75615633568

75611140072                      FEB 20,2004  18:44                      75615633574

75611140100                      FEB 20,2004  18:58                      75615633634

75611140118                      FEB 20,2004  19:13                      75615633652

75611140124                      FEB 20,2004  19:26                      75615633658

75611140140                      FEB 20,2004  19:36                      75615633672

75611140150                      FEB 20,2004  19:46                      75615633683

75611140160                      FEB 20,2004  19:56                      75615633693

75611140170                      FEB 20,2004  20:08                      75615633704

75611140176                      FEB 20,2004  20:25                      75615633710

75611140188                      FEB 20,2004  20:41                      75615633722

75611140190                      FEB 20,2004  20:45                      75615633724

FEB 25,2004  FEB 24,2004        8405

2                           75611182041                      FEB 25,2004  15:22                      75615685674

75611182938                      FEB 25,2004  15:59                      75615686799

Figure 4

FORUM Server Reporting

The intended audience for the remainder of the document is Office of Information staff and included for information purposes.

EVS:

On the FORUM server there is a menu for running and viewing the reports for

totals, ACK message status, Missing Sites, and Transmitted Sites. These

reports may be used to monitor the seeding and bi-monthly updates. These reports

will indicate specific activity from each site. The following figure is the menu option

available on the FORUM server. Currently there are three more options, and that menu looks as follows:

1      Completed Background Job Report

2      All Ack's Received Report

3      Missing Sites Report

4      Transmitted Sites Report

5      ACK Status Report

6      Site Message History

7      PAIT SUMMARY REPORT

Figure 1

Option 1	Completed Background Job Report

When the program completes at each VistA the “Completed Background Job Report” is populated with the number of patient appointment records that were transmitted to the National Database in  (Figure 2).  Since the program sends this information in batches (5,000 records maximum) the total batch count is recorded.  These two figures should be matched with the AAC Transmitted Site report (Option 4).  If they do not match then there is reason to investigate the difference.

Sites - Completed Background Job               FEB 27,2004  13:36    PAGE 1

SITE                                                                                    # OF                                 # OF

NUMBER            RUN COMPLETION DATE            BATCHES                APPOINTMENTS

---------------------------------------------------------------------------------------------------------------------------------------

656                           FEB 20,2004  14:53                             59                                294917

756                           FEB 21,2004  01:30                             34                                165317

659                           FEB 21,2004  02:09                             43                                210278

649                           FEB 22,2004  03:21                             30                                147223

649                           FEB 25,2004  15:02                               1                                    4985

756                           FEB 25,2004  16:02                               2                                    8405

656                           FEB 26,2004  06:16                               4                                  18691

659                           FEB 26,2004  09:55                               3                                  12708

--------

COUNT  8

Figure 2

> **NOTE:** The above table includes both seeding and the update transmission from four  sites.

In the case they do not match, the Vitria IE monitoring reports will provide information on whether or not the patient appointment records were received and passed along to the Austin Automation Center (AAC).  Use the following URL, ID, and password to connect to Messaging and Interface System’s site.  The ID and password are case sensitive.

URL: [http://vhaaacviev4:8080/ciev/hbase](http://vhaaacviev4:8080/ciev/hbase)

ID =

Password =

Check with your site’s Information Resources Management (IRM) officer for access.

Option 2	All Ack's Received Report

The “All ACK’s Received Report” indicates at the summary level the number of ACK messages processed for each site and the date the process was completed (Figure 3).  There is a count figure that indicates the number of sites reported.  If in the event the site’s ACK message count do not match this can be an indicator that the AAC either did not receive the batch from  via the Vitria IE or AAC experienced a problem when processing the batch.  In either case, the missing batch(es) will need to be identified and, at this time, the manual batch rejection initiated at the  site.  To determine the missing batch(es) proceed to Option 5 to view the detailed ACK message status report and a related  site has to be contacted to run the Acknowledgement Summary report (VistA Reporting section) with Batch Control ID.  They must be compared to the Batch Control ID’s received by the AAC.

All ACKs Received Report                       FEB 27,2004  13:40    PAGE 1

Site                    Run Completed            Ack's

-------------------------------------------------------------------------

649                       FEB 22,2004            30 of 30

649                       FEB 25,2004            1 of 1

656                       FEB 20,2004            59 of 59

656                       FEB 26,2004            4 of 4

659                       FEB 21,2004            43 of 43

659                       FEB 26,2004            3 of 3

756                       FEB 20,2004            34 of 34

756                       FEB 25,2004            2 of 2

--------

COUNT     8

Figure 3

Option 3	Missing Sites Report

This option allows EVS and HSD&amp;D to view which site transmissions were not received at the AAC during the seeding or specific update run.  The report lists the sites that did not transmit by alphabetical order of Site Name.

Missing Site Report                            MAR  1,2004  15:23    PAGE 1

MISSING SITE

# SITE NAME                                                   REPORT DATE

--------------------------------------------------------------------------------------------------------

REDACTED     ------------

COUNT     122

Figure 4

Option 4	Transmitted Sites Report

This report indicates the total number of patient appointment records and batch counts received at the AAC for each transmitted site along with the date received.  This report should be used with “Completed Background Job Report” (Option 1) to determine if there are differences between what the  sites reported as transmitted and what the AAC reports as being received.  In the case they do not match refer to the instructions outlined in Option 1.

Transmitted Sites Report                       MAR  1,2004  15:28    PAGE 1

SITE

# SITE NAME   TOTAL RECORDS    TOTAL BATCHES    REPORT DATE

--------------------------------------------------------------------------------------------------------------------

REDACTED

-------

COUNT     4

Figure 5

Option 5	ACK Status Report

The “ACK Status Report” indicates at the detail level the receipt of each ACK message for each site (Figure 6).  The last detail ACK message record indicates whether the site’s ACK message processing is complete (“Yes”).  There is a sub count for each site indicating the number of ACK messages processed and count that indicates total ACK messages processed for all sites.

ACK STATUS REPORT                              FEB 27,2004  13:41    PAGE 1

SITE                                                                                                       ACKS

NUMBER                       RUN      ACK STATUS                  COMPLETE  DATE/TIME

------------------------------------------------------------------------------------------------------------------------------

649                                  1 of 30                                                 FEB 24,2004  10:44

649                                  3 of 30                                                 FEB 24,2004  11:56

649                                  4 of 30                                                 FEB 24,2004  11:56

649                                  5 of 30                                                 FEB 24,2004  11:56

649                                  6 of 30                                                 FEB 24,2004  11:56

649                                  7 of 30                                                 FEB 24,2004  11:56

649                                  8 of 30                                                 FEB 24,2004  11:56

649                                  9 of 30                                                 FEB 24,2004  11:56

649                                10 of 30                                                 FEB 24,2004  11:56

649                                11 of 30                                                 FEB 24,2004  11:56

649                                12 of 30                                                 FEB 24,2004  11:56

649                                13 of 30                                                 FEB 24,2004  11:56

649                                14 of 30                                                 FEB 24,2004  11:56

649                                15 of 30                                                 FEB 24,2004  11:56

649                                16 of 30                                                 FEB 24,2004  11:57

649                                17 of 30                                                 FEB 24,2004  11:57

649                                18 of 30                                                 FEB 24,2004  11:57

ACK STATUS REPORT                              FEB 27,2004  13:41    PAGE 2

SITE                                                                                                       ACKS

NUMBER                       RUN      ACK STATUS                  COMPLETE  DATE/TIME

------------------------------------------------------------------------------------------------------------------------------

649                                 2 of 30                                                 FEB 24,2004  11:57

649                               19 of 30                                                 FEB 24,2004  14:49

649                               20 of 30                                                 FEB 24,2004  14:49

649                               21 of 30                                                 FEB 24,2004  14:50

649                               22 of 30                                                 FEB 24,2004  14:51

649                               23 of 30                                                 FEB 24,2004  14:52

649                               24 of 30                                                 FEB 24,2004  14:52

649                               25 of 30                                                 FEB 24,2004  14:53

649                               26 of 30                                                 FEB 24,2004  14:53

649                               27 of 30                                                 FEB 24,2004  14:54

649                               28 of 30                                                 FEB 24,2004  14:54

649                               29 of 30                                                 FEB 24,2004  14:55

649                               30 of 30           YES                               FEB 24,2004  14:55

--------

SUBCOUNT  30

Figure 6

> **NOTE:** An example in Figure 6 shows only one station. Please note that

Acknowledgements may be received in different order to the transmitted batches.

Each batch has a unique number making it easy to locate should a site’s  count not equal the count from the AAC. Once the batch control number(s) are located the investigator will need to access the  site’s Acknowledgement Summary report for the actual Batch Control ID(s) that will need to be manually rejected. The  generate a summary report of batches received from all sites with a number of appointments and a number of rejections.

Option 6. 	Site Message History

PAIT TRANSMISSION LOG LIST                     JUL 13,2006  09:39    PAGE 1

SITE

NUMBER    MESSAGE TYPE             DATE/TIME

--------------------------------------------------------------------------------

358       STARTED TRANSMISSION     JUL  1,2006  10:00

358       BACKGROUND JOB COMPLETE  JUL  1,2006  10:12

358       ACKNOWLEDGMENT           JUL 10,2006  13:59

402       STARTED TRANSMISSION     JUL  1,2006  04:00

402       BACKGROUND JOB COMPLETE  JUL  1,2006  04:48

402       ACKNOWLEDGMENT           JUL 10,2006  14:01

402       ACKNOWLEDGMENT           JUL 10,2006  14:01

402       ACKNOWLEDGMENT           JUL 10,2006  14:01

402       ACKNOWLEDGMENT           JUL 10,2006  14:01

402       ACKNOWLEDGMENT           JUL 10,2006  14:02

402       ACKNOWLEDGMENT           JUL 10,2006  14:02

402       ACKNOWLEDGMENT           JUL 10,2006  14:03

402       ACKNOWLEDGMENT           JUL 10,2006  14:03

You can follow up a history of PAIT for each site from its start to receiving acknowledgements.

Option 7. 	PAIT Summary Report

This report is a compilation of all messaging activity from  through VIE to the AAC, and gives the best overview of each PAIT activity.

### National Help Desk Reporting

Missing Site Reporting

From the AAC:

One the 5 th and 19 th of every month the AAC will send to VHA National Help Desk an email message indicating those sites that the AAC did not receive patient appointment information transmissions.  This report will include the site (facility) number and name.  The corresponding report is also sent by the AAC to the Forum Server (see Option 3 in Forum Server Reporting).

VHA National Help Desk

Upon receipt of the email from “MVSMail” listing the sites that did not transmit (Missing Site Report) the VHA National Help Desk will enter a Remedy Ticket the sites that did not transmit.  The Remedy Ticket should be assigned to EVS who will begin the investigation process.

EVS

EVS will act upon the receipt of the Remedy Ticket by running the Complete Background Job Report on the FORUM server.  This report will indicate whether the site actually gathered data and passed it to the local Vitria IE machine.  If the report indicates no activity from the site, EVS will contact the site to determine why the site did not run.  Based on the reason, EVS may need to contact other groups to provide assistance.  In the case the report indicates there was activity, EVS may need to access the M&amp;IS URL to review the Vitria IE activity reports.  The M&amp;IS URL, ID, and password are:

URL: [http://vhaaacviev4:8080/ciev/hbase](http://vhaaacviev4:8080/ciev/hbase)

ID =

Password =

Check with your site’s Information Resources Management (IRM) officer for access

There are two reports that indicate activity of patient appointment records being sent to the AAC.  The first indicates activity at the  site’s local Vitria IE (Remote Outgoing Batch Tallies).  The report presents the Site ID, Name, Most Recent Date, and Batch Count.

The second report indicates the files transferred (FTP) to the mainframe at the AAC (File Uploads to MVS).  This report demonstrates the Site(s) ID, Name, and Batch Count that were included in the file transfer.  It should be noted that the batch count indicated in a file sent to the AAC may not be the total batch count for that site.

Examination of all files transferred will need to be performed and manually adding the batch counts for all files to determine if the site’s total batch count matches the count on the FORUM server.

- If the reports on the FORUM server indicate the site did not generate batches  EVS will need to contact the site to find the responsible person who can determine or explain why the program did not run.
- If the reports on the FORUM server indicate the site did generate batches but did not transmit and the Vitria IE reports do not indicate the site’s activity, then EVS will need to contact M&amp;IS for assistance..
- If the reports on the FORUM server and the Vitria IE reports indicate the site did transmit, then EVS will need to contact the AAC for assistance.

> **NOTE:** The primary trouble shooting to determine the problem in communications should be done by following directions in the Trouble Shooting chapter.

### Communication Problems

VHA National Help Desk:

REDACTED

REDACTED

Figure 2

The above message, Figure 2 shows that the communication with Vitria was not established at all and none of generated batches were transmitted.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: SD*5.3*349 PAIT Release Notes

## PAIT Changes introduced with SD*5.3*349

### Background Job

The PAIT BACKGROUND JOB completion message was modified to include both    Starting Date and the Last Scanned Date, and they are sent to the forum server to reflect more accurate status of the site transmission in the completion report.

### Patient Status Code

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

The patient status code indicates if a patient is new to a facility or not.  Both the Parent Station and the Substations are evaluated as the facility. The parent Station is evaluated with the primary DSS ID only; the Substation is evaluated with both the DSS ID stop code and the DSS credit stop code. The patient is new to the facility if he/she did not have another scheduled appointment in the same facility during the last 24 months. The facility is determined from the Institution file if there is a pointer to it from the Hospital Location file through the pointer to the Medical Center Division from the Division field of the Hospital file.

Table 0216 - Patient Status Codes

| **VALUE**   | **DESCRIPTION**                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------|
| NSF         | Patient did not have a prior appointment at this Facility in the past 24 months; New to Parent and Sub Station      |
| SHB         | Patient did  have a prior appointment at this Parent and Sub Station in the past 24 months; Registered Here Before. |
| OPN         | Patient did not have a prior appointment at this Sub Station but was registered with Parent Station.                |

### Sort Template

The Sort Template: [SD-PAIT PEND EXCL FUTURE], used with option SD-PAIT PENDING has been modified to give users the ability to request a certain range of records sorted by the Appointment Date.

### Batch Header

The Batch Header of the HL7 acknowledgement message from station 200 was modified to request a commit acknowledgement from Vista HL7.  The addition of the commit acknowledgement (CA) provides a receipt of message reception by Vista HL7 and improves internal tracking mechanisms.

BHS^~|\&amp;^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S12^ **500** 3236-1^D^2.4^^^AL^AL^USA

SCH^1^^^^^^4^NAT^^^~~~20030908~~~Date Appt Created|~~~~~~Desired Date|~~~200309180800~~~Appt Date|~~~~~~Checkout Date|~~~~~~Cancellation Date|~~~~~~Auto-rebook Date|~~~~~~Resched Date^^^^^^^^^^^^^^P

PID^1^^""~~~USVHA&amp;&amp;L~NI|7171938~~~USVHA&amp;&amp;L~PI^^WOLFIK~EDZIU^^19301212^^^^~~~~19107^^^^^^^^208121230P

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ **500**

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^422~~~~~~~~CECELIA'S CLINIC^402~CARDIAC SURGERY~DSS Clinic ID^418~AMPUTATION CLINIC~DSS Credit Stop

ZEN^1^^^^^^^^5

ZSP^1^N^

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^ **500** 3236-2^D^2.4^^^^^

SCH^1^^^^^CC^3^RS^^^~~~20030829~~~Date Appt Created|~~~20030829~~~Desired Date|~~~200308291330~~~Appt Date|~~~~~~Checkout Date|~~~200308290940~~~Cancellation Date|~~~~~~Auto-rebook Date|~~~200308291030~~~Resched Date^^^^^^^^^^^^^^F

PID^1^^""~~~USVHA&amp;&amp;L~NI|7172069~~~USVHA&amp;&amp;L~PI^^YORTY~OUTPATIENT^^19710604^^^^~~~~17042^^^^^^^^509060471P

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ **500**

PV2^^^^^^^^^^^^^^^^^^^^^^^^SHB

AIP^1^^1934~PETERSON~JAMES~R^Provider

AIL^1^^614~~~~~~~~YORTY'S CLINIC^329~MEDICAL PROCEDURE UNIT~DSS Clinic ID^~~DSS

Credit Stop

ZEN^1^^^^^^^^1

ZSP^1^Y^60

MSH^~|\&amp;^SD-SITE-PAIT^500^SD-AAC-PAIT^200^^^SIU~S15^ **500** 3236-3^D^2.4^^^AL^AL^USA

SCH^1^^^^^CP^3^RS^^^~~~20030829~~~Date Appt Created|~~~20030829~~~Desired

Date|~~~200309010815~~~Appt Date|~~~~~~Checkout Date|~~~200308290856~~~Cancellation Date|~~~~~~Auto-rebook Date|~~~200309010815~~~Resched Date^^^^^^^^^^^^^^F

PID^1^^""~~~USVHA&amp;&amp;L~NI|7172424~~~USVHA&amp;&amp;L~PI^^VILELLA~JOEY~ASHLEY~III~MR^^19490

416^^^^~~~~33354^^^^^^^^244990005

PV1^1^U^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ **500**

PV2^^^^^^^^^^^^^^^^^^^^^^^^NTF

AIL^1^^312~~~~~~~~XXXXX^102~ADMITTING/SCREENING~DSS Clinic ID^104~PULMONARY FUNCTION~DSS Credit Stop

ZSP^1^N^

BTS^3

### Batch Acknowledgement

The format of the Batch acknowledgement message was modified to conform to Vista HL7’s proprietary formatting:

BHS^~|\&amp;^SD-AAC-PAIT^200^SD-SITE-PAIT^500^20040408140937^^~P~ACK~2.4~AL~NE^AE^200404-5003^5003

MSA^AE^5003

MSA^AE^5003-1^250

MSA^AE^5003-2^200

MSA^AE^5003-3^200

BTS^3

### Description of Error Codes:

Appointments sent via the Patient Appointment Information Transmission (PAIT) application can be rejected by the AAC, and if so they have specific error codes that may be found in the PCMM HL7 ERROR CODE file (#404.472). Rejected appointments can be listed by using the Rejected Transmissions [SD-PAIT REJECTED] option. The Rejected Transmission report should be used to review and correct patient appointment records that the AAC rejected.  Rejections can occur due to incomplete dates, invalid site/facility codes (ones that do not match the site of the sender), and for other reasons. For a particular site; see sample of REJECTED TRANSMISSION LOG report below. For a list of rejection codes and their definition see table AAC001 - Error Code Set in the SD*5.3*333 Release Notes. A site should use this report for correcting their patient appointment records.  Once the site has corrected the record it will be sent to the National Data Base in the next bi-monthly update run and loaded into the National Database.  The correction of rejected records is the VistA site’s responsibility. If the rejected record is not corrected it is sent again by the PAIT application with the next scheduled or executed PAIT, and it may be rejected again.

PATIENT APPOINTMENT INFO LOG LIST             SEP 9,2008  11:28    PAGE 1

PATIENT                         APPT DATE

ERROR

SHORT DESCRIPTION                                           MESSAGE

CLINIC

---------------------------------------------------------------------------

RETENTION FLAG: YES - to be sent when 'Final'

ERROR MESSAGE: 850

KING,FEB                      APR 29,2008  08:00

Admit type is invalid (table SD009)         			850

NEW CLINIC

#### Error 100

PATIENT DFN IS NOT NUMERIC OR IS MISSING:

DFN, or internal entry number of a patient in the Patient File is missing or not a number.  Most likely the result of a HL7 transmission formatting error.  Requires no intervention or correction at site level the first time the error occurs.  The record will be re-transmitted.  If error persists initiate NOIS and/or call the National Help Desk.

#### Error 150

CLINIC IEN IS NOT NUMERIC OR IS MISSING:

Clinic IEN, or internal entry number of the Clinic in Hospital Location File is missing or not a number.  Most likely the result of a HL7 transmission formatting error.  Requires no intervention or correction at site level the first time the error occurs.  The record will be re-transmitted.  If error persists initiate NOIS and/or call the National Help Desk.

#### Error 200

BHS STATION NUMBER AND STA3N ARE NOT EQUAL:

Error 200 indicates that the Hospital Location of a particular appointment is set up with an Institution whose Station Number field doesn’t match the sending facility number. The Institution is identified from the Medical Center Division file (# 40.8) pointed to by the Division field (# 3.5) of the Hospital Location file (#44). The first three digits of the station number have to match the sending  facility number. The site has to find if the Station Number in the Institution is incorrect or another Institution has to be set up with the Medical Center Division of the Hospital file. If the Institution field of the Medical Center Division file is not null it is treated as a designated location of that appointment. The PAIT retrieves the Institution and its Station Number, following the Division field pointing to the Medical Center Division file, and its Institution File Pointer field (# .07). IRM should direct this issue to whomever is responsible for set-up of the Hospital Location file. If the issue cannot be solved locally a Remedy ticket has to be initiated and/or the National Help Desk notified.

#### Error 250

INVALID OR MISSING BHS STATION NUMBER:

HL7 site parameters are incorrect.  Initiate NOIS and/or call the National Help Desk.

#### Error 300

INVALID OR MISSING STA3N:

Error similar to 250. It indicates that the Station Number field (# 99) identified from the Institution is null or its first three characters do not match the facility 3 digits number. Allow the record to be re-transmitted.  If error persists initiate NOIS and/or call the National Help Desk.

#### Error 350

HL7 DATE IS NOT IN PROPER FORMAT OR IS MISSING:

Error 350 is mostly caused by too old desired date of appointment or bogus date of appointment itself, filed in  sub file 1900 of the Patient File. IRM has to address this issue consulting the Scheduling team. If no evidence can be found initiate NOIS and/or call the National Help Desk.

Example:

Error 350 would have to be evaluated by a person having programming access and authority to repair data. Please note the following examples:

(1) DFN 105723 error for 12/1/2004    &lt;= CORRECTED

^DPT(105723,"S",3041201.133,0) = 5142^^^^^^3^^^^^^^^^9^^^

3040315^^^^^0^O^0

^DPT(105723,"S",3041201.133,1) = **1200104** ^1   &lt;= incorrect date

^DPT(105723,"S",3041201.133,1) = 3041201^1   &lt;= corrected

(2) DFN 41221 error 10/11/2004

^DPT(41221,"S",3041011.1018,0) = 1072^C^^^^^3^^^^^34131

^^3031014.0845^11^9^^3413

1^3031014^^^^^0^O^0

^DPT(41221,"S",3041011.1018,1) = 3041011^1    &lt;= appears correct

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

^DPT(41221,"S",1011103.1018,1) = **1011103** ^1

Patient DFN 41221 has appt. date 11/03/1801 - not correct.

(3) DFN 85462 error 12/2/2003    &lt;= CORRECTED

^DPT(85462,"S",3031202.13,0) = 1048^^^^^Y^3^^^^^^3031202

^^^9^^^3030915^15323851^^^^0^O^0

^DPT(85462,"S",3031202.13,1) = **1200203** ^0    &lt;= incorrect date

^DPT(85462,"S",3031202.13,1) = 3031202^0   &lt;= corrected

^DPT(5385215543,"S",1120303.13,0) = 4532^C^^^^^3^^^^^40347

^^3031105.1110^11^9^^40347^3031105^^^^^0^^0

^DPT(5385215543,"S",1120303.13,1) = 3031112^1

^DPT(5385215543,"S",1120303.13,"R") = error

from File #44

^SC(4532,"S",1120303.13,0) = 1120303.13

^SC(4532,"S",1120303.13,1,0) = ^44.003PA^^

(4) DFN 42092 error 12/22/2003     CORRECTED

^DPT(42092,"S",3031222.14,0) = 5175^C^^^^^3^^^^^38323

^^3031124.1512^11^9^^38323^3031124^^^^^0^O^0

^DPT(42092,"S",3031222.14,1) = 1201203^1    &lt;= incorrect date

^DPT(42092,"S",3031222.14,"R") = WRONG DATE

^DPT(42092,"S",3031222.14,1) = 3031222^1    &lt;= corrected

#### Error 400

DOB IS MISSING OR INVALID:

Site staff should examine demographics of Patient for an invalid or missing date of birth and correct.

#### Error 450

CREATE DATE OR APPT DATE IS MISSING:

Each generated appointment must have the Creation Date. Site should verify an entry in 409.6 file checking the DATE APPT MADE field. If that field exists, allow the record to be re-transmitted.  If error persists initiate NOIS and/or call the National Help Desk.

#### Error 500

CREATION DATE IS BEFORE SEPTEMBER 1, 2002

PAIT evaluates appointments based on the Creation Date before Sep 1 st 2002. Site should verify an entry in 409.6 file checking the DATE APPT MADE field. If its value shows a date before Sep 1 st 2002 initiate NOIS and/or call the National Help Desk, otherwise allow the record to be retransmitted and if the error persists initiate NOIS or/and call the National Help Desk.

#### Error 600

RESCHEDULED DATE AND APPT TYPE ARE NOT IN AGREEMENT

Please refer to description of Appointment Type: RS – Rescheduled in chapter 4.0 Appointment Selection Logic of SD*5.3*333 Release Notes. If the Rescheduled Date was identified the Appointment Type must be ‘RS’.

No site intervention is required, initiate NOIS and/or call the National Help Desk.

#### Error 650

CHECK OUT DATE AND EVENT REASON ARE NOT IN AGREEMENT

The Event Reason: ‘CO’ or ‘COE’ require the Check Out Date to be included with

a transmitted appointment. No site intervention is required, initiate NOIS and/or call the National Help Desk.

#### Error 700

CANCELLATION DATE AND EVENT REASON ARE NOT IN AGREEMENT

The Cancellation Date requires the Event Reason to be either ‘CC’, ‘CP’ , ‘NS’ or ‘CT. Please refer to SIU Event Mapping Table in chapter 4.0 Appointment Selection Logic of SD*5.3*333 Release Notes. Appointment Type ‘CT’ may be also sent without the Cancellation Date if a new appointment that overrode the original one is still ‘pending’. Initiate NOIS and/or call the National Help Desk if no solution is evident.

#### Error 750

EVENT REASON AND FILLER STATUS ARE NOT IN AGREEMENT

Review  SIU Event Mapping Table in chapter 4.0 Appointment Selection Logic of  SD*5.3*333 Release Notes to see the indicated relation. . Initiate NOIS and/or call the National Help Desk if no solution is evident.

#### Error 800

FILLER STATUS IS MISSING OR IS INVALID

Each appointment record must have the Filler Status that corresponds to either

‘pending’ or ‘final’ value. Initiate NOIS and/or call the National Help Desk.

#### Error 850

ADMIT TYPE IS INVALID (table SD009)

Patch SD*5.3*446 was released with a new sequence -  Admission Type, see below, to be accepted in Austin.

PV1 - Patient Visit Segment

----------------------------

SEQ    LEN     DT      TBL#   ELEMENT NAME       VISTA DESCRIPTION

---------------------------------------------------------------------------------------------------------------

4                 4       ID      0007   Admission Type                Refer to Table SD009

(Purpose of Visit)

For a list of valid types see table SD009 - Purpose of Visit &amp; Appointment Type in the SD*5.3*333 Release Notes.

Austin set up a new rejection code 850 - 'Admit type is invalid (table SD009)'

on their site that corresponds to the code in the PCMM HL7 ERROR CODE file (#404.472).

IF ADMIT\_TYPE NOT IN ('0101','0102','0103','0104','0105','0106',

'0107','0108','0109','0111','0201','0202','0203','0204','0205',

'0206','0207','0208','0209','0211','0301','0302','0303','0304',

'0305','0306','0307','0308','0309','0311','0401','0402','0403',

'0404','0405','0406','0407','0408',

'0409','0411',' ')

THEN ERR\_CODE = '850';

The report from the Rejected Transmissions [SD-PAIT REJECTED] option will list any entry with rejection code '850'. Like the other errors on that report, it needs to be investigated and the appointment retransmitted (in this case, the valid Purpose of Visit and Appointment Type need to be determined). Sites must not create their own local appointment types because ones not on the table will be rejected.

#### Error “R”

WHOLE BATCH REJECTED:

The whole batch rejection from the AAC has not been implemented at this time and will be future enhancement but a manual rejection may be implemented if needed. No action at all has to take place because there was a problem with accepting the whole batch. The batch will be retransmitted, no action is needed.

### Mail Message

The message generated at the end of generated appointment batches in a  facility, and it will contain additional   information regarding the Started and the Last Scanned Date:

Subj: 656 - PAIT BACKGROUND JOB  [#5277039] 04/22/04@16:06  13 lines

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

-----------------------------------------------------------------------

The PAIT job has completed - TASK #: 8949063 Log #: 2 on 4/22/04@16:05

**Started: 4/22/04                        Last Scanned: 4/21/04**

Pending appointments:      33411

Final appointments:        63586

----------

Total appointments:        96997   Number of batches: 20

Fac Log Bch Appt #  Date finished  IP Address  Gen  Sent Com R Com P  Status

-----------------------------------------------------------------------

656|  2| 20|  96997|4/22/04@16:05|10.104.10.89| 379| 378| 378| 378| Inactive

> **WARNING:** 1 out of 20 batches have to be still transmitted. This message might be generated when HL7 transmission is still in process.

### PAIT Trouble shooting

After successful completion of the bi-monthly PAIT transmission, members of the SDPAIT mail group should receive a PAIT BACKGROUND JOB MailMan message confirming success. It is the site’s responsibility to initiate a NOIS if this message is not received after the scheduled task finishes or if an error is found in the error log. The site should first check the error log, looking at the time when the PAIT task terminated, and call the REDACTED.

All completion messages are also sent to the Forum server where HSD&amp;D and EVS can verify that the reported transmission has finished. If an error or problem occurs, IRM should not start the next PAIT task until HSD&amp;D or EVS staff review the problem and take or advise corrective action.

### From: SD*5.3*376 PAIT Release Notes

## Changes Introduced with *5.3*376

The system features delivered with patch SD*5.3*376 include additional data extraction information (Combat Veteran and Military History ) for the National Database, automated verification tools for the Forum Server and software fixes that resolve problems as documented in National Online Information Sharing (NOIS).  The following paragraphs describe these changes in further detail.

### Combat Veteran Eligibility

Combat Veteran Eligibility is used to identify a Combat Veteran (CV) Status veteran seeking medical care for a specific date.  CV eligibility will be determined as of the Appointment Creation Date.  The following values for Combat Veteran Eligibility are:

- 1 (Yes) is sent if the patient was/is considered a combat veteran on the Appointment Creation Date;
- 0 (No) is sent if the patient wasn't/isn't considered a combat veteran on the Appointment Creation Date.

Combat Veteran Eligibility is now included in HL7 segment ZEL.

### Combat Veteran End Date

The Combat Veteran End Date represents the last day for combat veteran eligibility. The existence of a CV End Date indicates that a veteran has been CV eligible at some point in time. Even if the CV eligibility has expired, this date will still be present.  Combat Veteran End Date is now included in HL7 segment ZEL

### Combat Veteran Indication

Combat Veteran Indication signifies if an appointment is related to a CV illness/injury.  During checkout or during the update of an appointment’s classifications, the question is asked if the appointment was related to the veteran’s CV status.  The following values for Combat Veteran Indication are:

- 1 (Yes) is sent if the appointment was related to the veteran’s CV status;
- 0 (No) is sent if the appointment was not related to the veteran’s CV status.

The answer to this question is now included in a seventh repetition of the ZCL HL7 segment (VA Specific Classification).

### Combat History

Combat History data is retrieved and transmitted to calculate the waiting time experienced by service members recently returning from the war in .  A new HL7 segment has been implemented (ZMH) to transmit this combat history data to the Austin Automation Center (AAC).  Three repetitions of the ZMH segment will be used to transmit the following combat history information:

- Last Service Separation Date
- Combat Veteran Indicated - signifies if the individual was ever considered a Combat Veteran.  Valid values are:
    - Y – yes
    - N - no
- Combat Service Location – the location where the individual was in combat.  Valid values are:
    - WORLD WAR I
    - WORLD WAR II -
    - WORLD WAR II - PACIFIC
    - KOREAN
    - OTHER
    - WAR
    - CONFLICT
- Persian Gulf Service – indicates if the individual served in the .  Valid values are:
    - Y – yes
    - N – no

### "Job Started" message on the Forum server.

A message to the Forum server and a local SD-PAIT Mail Group will now be generated at the beginning of each site’s PAIT transmission to confirm that the bi-monthly data collection process has begun.  This start message also details the status of the SD-PAIT logical link and possible reason for any communications error.  This message will be sent to the SD-PAIT mail group in the form of a MailMan message.  The following is an example of this new Job Started message:

Subj: 500 - PAIT START JOB  [#1955884] 09/21/04@12:11  3 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

The PAIT job has started - TASK #: 2717310

Site   -PAIT status    Task #

500  |3040921.121119 |Enabled    |2717310

The local job completion message will stay as is, with subject 500 - PAIT BACKGROUND JOB, where 500 = station number.

### Post-installation updates

Approximately 50% of the sites did not receive initial seeding acknowledgement messages.  Sites that did not receive HL7 acknowledgement (ACK) messages during the seeding process due to communication problems will be updated. A post-init routine, working as a driver, will identify a particular site where there is a need to execute the acknowledgement process, by retrieving rejected appointments from routines containing site-specific data only for sites with rejections. Not rejected appointments are processed as acknowledged.

There is a possibility that rejected appointments if originally sent as pending may have already been process.

### Clean up file PATIENT APPOINTMENT INFO LOG (#409.6).

Differences between the error report that the site can generate using option: SD-PAIT REJECTED  [Rejected Transmission] and the error report coming from the AAC have been identified at some sites. The reason for the current differences is associated with acknowledgements not being received by some sites in a timely manner. Currently, the acknowledgement process initiates cleaning of the previously rejected entries in each site’s PATIENT APPOINTMENT INFO LOG (#409.6) file. Patch SD*5.3*376 will perform a clean-up of all previous entries with the exception of those in pending status so that now the SD-PAIT REJECTED report and AAC Rejected Report will match.

### Outgoing &amp; Upload Statistics Sent via MailMan

The Forum Server accepts and processes new completion messages from the VistA Interface Engine and .  Outgoing batch and MVS upload statistics from the AAC webpage have been merged into mail messages and are transmitted to the Forum Server.  The messages are processed and the data used to determine if the transmission process has been completed for each site.

Outgoing batch and MVS upload statistics provided on the AAC webpage will be incorporated into a MailMan message format and transmitted to individuals in the SD-PAIT mail group.

### Provider Name Subcomponent Modifications

Previously, if a middle initial and/or a suffix were not identified, the transmitted HL7 AIP segment did not include '~' as the delimiter after the identified First and Last name subcomponents.  Tilde (~) delimiters will now be included, even if there is no middle initial and/or no suffix identified.  This is acceptable by HL7 standards but was modified on request of . For example:

- PROVIDERLAST,PROVIDERFIRST will be transmitted as: PROVIDERLAST~PROVIDERFIRST~~
- PROVIDERLAST,PROVIDERFIRST K JR will be transmitted as: PROVIDERLAST~PROVIDERFIRST~K~JR
- PROVIDERLAST,PROVIDERFIRST K will be transmitted as: PROVIDERLAST~PROVIDERFIRST~K~
- PROVIDERLAST,PROVIDERFIRST JR will be transmitted as: PROVIDERLAST~PROVIDERFIRST~~JR

### Interrupted Transmission Repair Process Fix.

For any repair needed to a previously interrupted, not completed transmission, (one where there is not a completion message for a site that had a “job started” message), a message is generated to the National Help Desk requesting a NOIS be created.  An additional run must be started by the site to transmit the expected appointments for the current time period.  A separate option, SD-PAIT Last Run Repair [SD-PAIT REPAIR] is available.  This option must be run before the next transmission is started.

### Automated Verification on the Forum Server

Manual checking of batches generated, transmitted, and received is required to ensure each site has completed the bi-monthly transmission.  This is time consuming and will be automated.  An automated process will be established on the Forum Server that alerts the National Help Desk when any stage of the transmission process fails.

To automate this functionality, new tasked background jobs will be scheduled to run on the Forum Server that incorporate elements from the Vista Interface Engine messaging team (VIE) and the AAC team.  VistA IE is expected to report the number of batches received per site, and AAC is expected to report the number of batches received and a total of all received appointments.  Any discrepancies with the  completion messages will generate warning messages to the National Help Desk

As each site starts and completes designated tasks, a status message will be sent to the Forum Server.  Six background tasks will be initiated at scheduled intervals on the Forum Server to determine the status of PAIT at all sites, as follows.

| **TASK**           | **Schedule 1**              | **Schedule 2**               | **Description**                                                                                                                                                                             |
|--------------------|-----------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAIT not started   | 12:01am 2  nd  day of month | 12:01am 16  th  day of month | Generates mail message to National Help Desk listing sites that did not start the scheduled PAIT.                                                                                           |
| Outgoing IE        | 09:00am 3  rd  day of month | 09:00am 17  th  day of month | Generates mail message to National Help Desk listing sites where the number of  outgoing batches from VistA DOES NOT match the number of  outgoing batches from the local interface engine. |
| PAIT not completed | 09:01am 3  rd  day of month | 09:01am 17  th  day of month | Generates mail message to National Help Desk listing sites that have not completed PAIT.                                                                                                    |
| NO ACKs            | 12:01am 4  th  day of month | 12:01am 18  th  day of month | Generates mail message to National Help Desk listing sites that have not received ANY HL7 acknowledgement messages.                                                                         |
| ACKs not completed | 12:01am 4  th  day of month | 12:01a  18  th  day of month | Generates mail message to National Help Desk listing sites that have not received ALL HL7 acknowledgement messages.                                                                         |
| Uploaded MVS       | 09:00am 4  th  day of month | 09:00am 18  th  day of month | Generates mail message to National Help Desk listing sites where the number of outgoing batches from , local interface engine, and AAC ftp to MVS mainframe DO NOT match.                   |
| Job Complete       | 12 Noon 4  th  day of Month | 12 Noon 18  th  day of Month | Generates mail message to the National Help Desk listing sites where it compares the Job Complete messages on the Forum Server that DO NOT match AAC Transmitted Sites report.              |
|                    |                             |                              |                                                                                                                                                                                             |

#### PAIT not started

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: PAIT NOT STARTED

The following site(s) have not started the bi-monthly PAIT.  Please initiate a NOIS for each site referencing the Interface Engine Module:

541  VAMC

612  HCS

#### PAIT not completed

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: PAIT NOT COMPLETED

The following site(s) have not completed the bi-monthly PAIT background job.  Please initiate a NOIS for each site referencing the Interface Engine Module:

541  VAMC

612  HCS

#### NO ACKs

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Monday, September 20, 2004 2:02 PM

To:

Subject: NO ACKNOWLEGEMENTS

The following site(s) have not received ANY acknowledgement

messages for the bi-monthly PAIT.  Please initiate a NOIS for

each site referencing the Interface Engine Module:

528 UPSTATE  HCS

598  HCS

**ACKs Not Completed**

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Monday, September 20, 2004 2:24 PM

To:

Subject: ACKNOWLEDGEMENTS NOT COMPLETE

The following site(s) have not received all acknowledgements for

the bi-monthly PAIT. Please initiate a NOIS for each site

referencing the Interface Engine Module:

541  VAMC

612  HCS

657  MO VAMC-JC DIVISION

**Outgoing IE**

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Friday, September 17, 2004 9:16 AM

To:

Subject: OUTGOING IE COMPARE

The following sites batch message counts comparing the number sent

from  and the number sent from local Interface Engine do not match.

Please initiate a NOIS for each site listed referencing the Interface

Engine Module:

Site #    SENT   OUTGOING IE SENT

528           25             26

557            4              8

589           22             23

603            7              8

629            8              9

679            3             16

#### MVS Upload

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Wednesday, September 22, 2004 1:16 PM

To:

Subject: MVS UPLOAD COMPARE

The following sites batch message counts comparing the number sent

from  and the number uploaded to MVS do not match.  Please

initiate a NOIS for each site listed referencing the Interface

Engine Module:

Site #    SENT   MVS UPLOADED

500            1

528           25             26

540            2              4

557            4              8

589           22             23

603            7              8

614            7              8

629            8              9

631            3              4

679            3             15

#### Job Complete

From: POSTMASTER@FORUM.VA.GOV [mailto:POSTMASTER@FORUM.VA.GOV]

Sent: Wednesday, September 22, 2004 1:16 PM

To:

Subject: JOB COMPLETE COMPARE

The following sites Job Complete messages on the Forum server do not match the AAC Transmitted Sites report.  Please initiate a NOIS for each site listed referencing the Interface Engine Module:

528 UPSTATE  HCS

598  HCS

### More Descriptive Completion Message Text

More descriptive message text will be added to the various completion message to better inform the user of transmission segment status’ and determine the proper NOIS module to be alerted if a problem occurs.  The following new text will be added to the MailMan completion message, when applicable:

- WARNING: TASK STOPPED BY USER, NEEDS TO BE RESTARTED.  INITIATE a NOIS TO FOLLOW UP.

- SUCCESS: Transmission completed.

- WARNING: 10 out of 15 still have to be transmitted, please verify with the HL7 System Monitor.

- SD-PAIT Logical Link has to be started.

- Initiate a NOIS for VistA Interface Engine - communication problem.

- WARNING!!!: Transmission of run#: 12 has been repaired.  Please create a NOIS to verify if the problem has been addressed

- WARNING!!!: Transmission communication problem, please review.

### Appointment Selection Logic

It was discovered there are appointments with NULL creation dates being transmitted.  No appointment should have a NULL creation date.  NULL creation dates will now be filtered and checked against existing cross-references in the Patient file (#2), so that no appointments with a NULL creation date will be transmitted.

### Patient Class Evaluation

Currently, only the Outpatient Encounter file (#409.68) is being used to determine the Patient Class.  Sometimes, a NULL value is being transmitted (as ‘U’ – undetermined).  Both the Visit (#9000010) and Outpatient Encounter files will now be examined to determine the appropriate Patient Class.

### Cleaning Process Performed at End of  Transmission Task

The cleaning process of the PATIENT APPOINTMENT INFO LOG file (#409.6) will be moved from the acknowledgement portion of processing to the end of the main transmission processing, and will be independent of the acknowledgements processing.

### Message for Not Allowing the Manual Transmission of PAIT

When the SD-PAIT TASKED TRANSMISSION is scheduled and the site attempts to run the SD-PAIT MANUAL TRANSMISSION option, the software completes a check prior to allowing the manual option to run in order to determine if the tasked job is scheduled; however, currently the code does not notify the user as to the reason it will not allow queuing.

If this situation occurs, an informational message will be displayed on the screen, immediately letting the user know why the manual transmission will not be run and also a MailMan message sent to the user explaining why queuing of the manual option: SD-PAIT MANUAL TRANSMISSION is not allowed.

The following is an example of this message received on the screen:

Select OPTION NAME: SD-PAIT MANUAL TRANSMISSION       Manual Startup PAIT Transmission

Manual Startup PAIT Transmission

You attempted to start PAIT outside the authorized transmission dates.

Job has been terminated.

The following is an example of the MailMan message received by a user who tried to execute the manual transmission when the regular tasked transmission is scheduled:

Subj: PAIT Transmission  [#1955781] 09/17/04@13:50  3 lines

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

-------------------------------------------------------------------------------

USERLASTNAME,USER (DUZ=100106) attempted to start the PAIT transmission

on Sep 17, 2004@13:50:39, outside the authorized transmission dates.

The job has been cancelled

### Protection for Missing Entry in File #409.6

Protection will now be provided for a missing entry in the PATIENT APPOINTMENT INFO LOG file (#409.6) where an "AE" Retention Flag cross reference with a “Y” value exists, while scanning previously sent appointments.

If the entry does not exist, then the cross reference pointing to it will be deleted.

### Cancelled Appointments for Non-Count Clinics

Currently, if an appointment is created and then cancelled its status as a count or non-count clinic is not known.  Now, additional verification is performed to determine the clinic type for canceled appointments, and if the clinic is 'NON-COUNT' it will receive 'NC' as its appointment type on the HL7 SCH message segment if it is not rescheduled, or an ‘RSN’ as its appointment type on the HL7 SCH message segment for appointments that are rescheduled.

### Identifying Appointments in HL7 Messages

The new option Patient HL7 Location [SD-PAIT PATIENT HL7 LOCATION] lists HL7 message number and sequence for a specified appointment date/time.   This is useful for verification of generated and transmitted data for a particular appointment.

### Field Name Change

The name of sub field #2 of Patient field #2 was changed from HL7 BATCH # to HL7 MESSAGE ID.

**Canceled Terminated Evaluation Modification**

If an appointment is canceled and another one is scheduled for the same Appointment Date/Time, then the previous one’s Event Reason will be Canceled Terminated, regardless of whether it was already canceled and transmitted in a previous run or if it was cancelled and transmitted in the current run with the new appointment that has the same Appointment Date/Time.  This situation is automatically recognized when appointments have the same Appointment Date/Time, but different Creation Dates.  The original Creation Date is retrieved from the PATIENT APPOINTMENT INFO LOG file 409.6, then overwritten in  by the Creation Date of the new appointment that has the same Appointment Date/Time.
