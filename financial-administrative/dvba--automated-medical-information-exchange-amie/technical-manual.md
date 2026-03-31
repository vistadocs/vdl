---
consolidated_title: "amie technical manual"
app_code: DVBA
doc_type: technical-manual
master_source: "AMIE Version 2.7 Technical Manual (TM)"
master_pub_date: July 2022
consolidated_from: 2 versions
prior_versions:
  - "AMIE Version 2.7 Technical Manual"
---

**Automated Medical Information Exchange (AMIE)**

**Software Version 2.7**

**Technical Manual**

<!-- image -->

**July 2022**

**Department of Veterans Affairs (VA)**

**Office of Information and Technology (OIT)**

**Revision History**

| **Date**   |   **Revision** | **Description (Patch # if Applicable)**                                                                                                                                                                | **Author**          |
|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| 07/2022    |              3 | Manual reformatted to VA standards  Section 5.1 File List with Description – added CAPRI CLINICAL EFOLDER TRANSMISSIONS  Section 11.4 added FileMan access code - CAPRI CLINICAL EFOLDER TRANSMISSIONS | Booz Allen Hamilton |
| 10/2019    |                | Removed references to the DVBA C Purge 2507 option from pages 8 and 15 for patch DVBA*2.7*215                                                                                                          | REDACTED            |
| 1/2018     |                | Update the Queued Task section for changes associated with DVBA*2.7*203                                                                                                                                | REDACTED            |
| 1/2009     |                | Reformatted Manual                                                                                                                                                                                     | REDACTED            |

**Table of Contents**

1.	Introduction	1

1.1	7131/7132	1

1.2	2507 Compensation and Pension	1

1.3	Related Manuals	1

2.	General Information	2

2.1	Mail Groups	2

2.2	Elective Fee Basis and Health Summary Options	2

2.3	Resource Requirements	3

2.3.1	Global Growth of Existing Files	3

2.3.2	Global Growth from New Files	3

3.	Implementation and Maintenance	4

3.1	Queued Tasks	5

3.1.1	7131/7132	6

3.1.2	C&amp;P	6

4.	Routines	7

4.1	Routine List	8

4.2	Callable Routines	8

4.3	Routines to Map	8

5.	Files	8

5.1	File List with Descriptions	8

5.2	File Flow (Relationships Between Files)	9

5.3	Templates	9

5.3.1	VA List Manager Templates	10

5.3.2	VA List Manager Protocols	10

5.4	Globals to Journal	10

5.5	Cross-References	10

6.	Exported Options	11

6.1	Menu Diagram	11

7.	Archiving and Purging	12

7.1	Archiving	12

7.2	Purging	12

8.	External/Internal Relations	12

8.1	External Relations	12

8.1.1	Minimum Software Versions Required	12

8.1.2	External Options	13

8.1.3	Special Agreements for AMIE	13

8.1.4	Database Integration Agreements (DBIAs)	13

8.2	Internal Relations	14

9.	Package-wide Variables	14

9.1	Key Variables	14

10.	How to Generate Online Documentation	14

10.1	XIndex	14

10.2	List File Attributes	15

11.	Security	15

11.1	Security Management	15

11.2	General Security	15

11.3	Security Keys	15

11.4	FileMan Access Codes	16

12.	Glossary	17

## Introduction

The AMIE software automates the administrative procedures involved in sending medical information used in determining veteran benefit payments from the VA medical centers to the VA regional offices.

The AMIE software is composed of two separate modules:  7131/7132 and 2507 Compensation and Pension.  Each of these sections provides requesting, tracking, and reporting functions for the various requests entered.

### 7131/7132

VAF 21-7131 is a request for information.  The regional office can log into the appropriate VA medical center and request a number of reports for a veteran.  These include, but are not limited to, competency reports, admission reports, and asset information.  Items such as 21-Day Certificate and Notice of Discharge are automatically tracked and issued only when the event occurs.  At this point, they become a 7132, Notice of Discharge and 21-Day Certificate.

Multi-divisional medical centers may transfer portions of the 7131 request between their divisions.

### 2507 Compensation and Pension

A 2507 examination request is a request for specific examination(s) to be performed on a veteran to determine compensation or pension benefits.  The regional office has the ability to add a patient to the medical center's database if s/he does not exist there.  All aspects of the examination process from notifying MAS of the request to scheduling of the exams, transcribing the results, and forwarding the results to the RO are handled through AMIE.

Medical centers have the ability to transfer any exams they are unable to perform to other sites via MailMan messages.  The AMIE software at the receiving medical center takes the mail message and enters a 2507 request into that hospital's database.  Once these exams are completed, they are transferred back to the original medical center.

Both modules of AMIE generate a number of reports to provide medical center and regional office personnel with the status and timeliness of any request.  The AMIS 290 report monitors the progress of 2507 exams.

The AMIE software greatly reduces the time it takes to exchange patient information between the medical centers and regional offices.  It reduces the amount of paper forms, provides better monitoring of the exam process, and most importantly, allows the veteran to receive benefits due her/him in a more timely and efficient manner.

### Related Manuals

- AMIE Regional Office User Manual
- AMIE Medical Administration Service (MAS) User Manual
- AMIE Installation Guide
- AMIE Release Notes

## General Information

### Mail Groups

There are several mail groups which must be populated.  Medical Administration Service should make the assignments based on the actual duties and needs of personnel.

DVBA C 2507 CANCELLATION	Receives notices of cancellation of exams and/or

requests.

DVBA C 2507 EXAM READY	Receives notices that exams have been fully

transcribed and are ready for 	review and release.

DVBA C 2507 EXAM REOPENED	Receives notices that requests and exams have been

reopened to correct errors.

DVBA C EXAM ADDED	Receives notices that exams have been added to an

existing request.

DVBA C NEW C&amp;P VETERAN	Receives notices that new veterans have been added

to the Patient file 	(#2) for C&amp;P purposes; also

receives address change information.

### Elective Fee Basis and Health Summary Options

Option Name:	FBCNH AMIE

Option Text:	Report of Admissions/Discharges for CNH

Description:	Provides a listing of admissions and discharges from a community nursing home within a user-specified date range.

Option Name:	FBCNH ADMISSIONS &gt; 90 DAYS

Option Text:	CNH Stays in Excess of 90 Days

Description:	Provides a listing, for a specified date, of active community nursing home stays that exceed 90 days.

Option Name:	FBCNH DISPLAY EPISODE OF CARE

Option Text:	Display Episode of Care

Description:	Shows all patient movements for a nursing home stay until date of discharge.

Option Name:	GMTS HS ADHOC

Option Text:	Ad Hoc Health Summary

Description:	Generates an "Ad Hoc" Health Summary for specified patients.  The user defines his own Ad Hoc Health Summary structure for temporary use instead of selecting a pre-defined Health Summary type.

Option Name:	GMTS HS BY PATIENT

Option Text:	Patient Health Summary

Description:	Generates a Health Summary of a specified pre-defined Health Summary Type for a specified patient.

Option Name:	GMRD MAIN MENU REMOTE USER

Option Text:	Discharge Summary Remote User

Description:	Allows a remote user (e.g., VBA RO claims auditors) with the GMRD REMOTE USER security key to access completed (signed by the attending physician) discharge summaries on a read only, need-to-know basis.  It will display incomplete (unsigned) summaries if the user does not hold the security key.

These options may be given as secondary options to regional office personnel.  They are available in V. 3.0 of Fee Basis and V. 1.0 of Health Summary.

### Resource Requirements

- 2.4k per 2507 exam	.65k per 7131 request

- There are no unique devices needed for the AMIE software.
- It will be necessary for each regional office to have at least a modem or IDCU unit and a communication program to use with the modem.
- There is only a minor demand on space that will be taken up as a result of the post-init process.  No more than 10k will be used for new data.
- Usage of space may increase depending on the Days to Keep 2507 History purge parameter.

#### Global Growth of Existing Files

2507 REQUEST file (#396.3) growth will be negligible.

FORM 7131 file (#396) may average growth of .5k per record if your site is multidivisional and transfers four reports per request to different divisions.

2507 EXAM file (#396.4) will grow by .1k for each exam included on priority insufficient 2507 requests.

#### Global Growth from New Files

.2k per AMIE C&amp;P Exam Tracking Record

The 2507 INSUFFICIENT REASONS file (# 396.94) will require 2.6k and will not grow.

## ## 4 Implementation and Maintenance

Implementation includes setting up required parameters in the AMIE Site Parameter file (#396.1) and the required TaskMan options.  See the Archiving and Purging Section for purging requirements.

**AMIE SITE PARAMETER File Setup**

Use the Regional File Site Parameter Setup option on the AMIE Medical Administration Menu to set up the AMIE site parameter file (#396.1).  There can be only one entry in this file.

1)	Set up the regional offices that will be accessing your system.  If offices are not set up, Notices of Discharge or 21-Day Certificates will not be produced.  This field is a pointer to the institution file (#4), and as each Notice of Discharge is compiled, this field is checked to see if the veteran's claim folder location is one of the allowed offices.

2)	Set up the valid medical center divisions for your facility for the 7131/7132 part of the AMIE software.  We use the term "REMOTE SITE (7131)"; however, this refers to the parent hospital as well.  If this is not properly filled in, reports for new requests will not be generated.  Even if you have only one division (the hospital itself), this must be filled in.  Be sure to enter a valid printer name or number in the PRINTER NUMBER field.  Failure to do so will result in no reports being printed.  The device must previously exist in File #3.5.  Repeat this step for each remote 7131/7132 site.

3)	Edit the REMOTE SITE (2507) field for the C&amp;P part of the AMIE software.  This is a pointer to the medical center division file (#40.8).  The site selected must already be in the MEDICAL CENTER DIVISION file (#40.8).  The same warnings apply to this field as the REMOTE SITE (7131) field.  If this is not set up properly, the AMIE software will not function correctly.  Enter the printer for the remote site or parent hospital.  This is a free text pointer to the DEVICE file (#3.5).  The printer must already exist in the DEVICE file (#3.5).  Once the printer is entered, the program will automatically pull the "name" of the printer and echo it as "Stored internally as NNN".  This is a symbol commonly referred to as ION and it is used for queuing purposes by TaskMan.  Even if there are no remote clinics or divisions, this must be set up for the parent hospital.  Repeat this step for any additional remote C&amp;P sites.

4)	Set up the C&amp;P routing locations.  Enter any hospital location (pointer to File #44) which can be used for C&amp;P locations or clinics.  This would be those locations to which automatic lab and/or X-ray results would normally be routed.  This is a multiple field.  These locations will be used during the final printing of a C&amp;P request to screen lab and radiology results for those which were ordered for a C&amp;P exam.  If these locations are not set up, no lab or radiology results will be printed with the final C&amp;P exams.  When ordering lab and x-rays as part of the C&amp;P exam, the PATIENT LOCATION must be one of the entries here or the results will not be printed automatically.

5)	Answer the prompt RUN NEW REQUESTS ON SATURDAY?.  Answer YES to have Friday requests printed on Saturday or NO to have them printed on Monday or the first work day after Monday.  If this field is left unanswered, the report-producing programs will automatically assume a NO answer.

6)	Make sure that all of the regional office users have **only one** division assigned to them in the NEW PERSON file (#200).  This should be the station number of their regional office.  Failure to assign the correct division, or if multiple divisions are inadvertently assigned, will result in incorrect data being entered into the file.

7)	The AMIE software makes use of the server function available in the VA Kernel.  In conjunction with the servers, there is one server error bulletin: XQSERVER.  This bulletin will notify members of mail groups assigned to it of any server problems.  The AMIE software will not address any usage or other items related to this function.  It will be left up to the individual sites whether this bulletin is populated with mail groups.  It is recommended that the sites do so, since this bulletin could possibly report any problems with C&amp;P transfers.

8)	The Days to Keep 2507 History parameter has been initially set at 120 days.  The site may want to adjust this parameter to a higher number.  This will provide the regional office personnel the ability to link insufficient exams to the original 2507 request.  It will also allow the medical center to keep 2507 requests and the results for up to 999 days.

9)	Answer the 2507 INTEGRITY REPORT STATUS prompt according to the information you wish to be included on the report generated with the options Check C&amp;P File Integrity (TaskMan) and Check C&amp;P File Integrity.  Setting the parameter with a status of OPEN will tailor the report so that only "Pending, Reported" 2507 requests will be included.  If the parameter has a value of COMPLETED, only 2507 requests with a status of "Released to RO, not Printed" or "Completed, Printed by RO" will be included.  Setting the parameter with a value of ALL will report all 2507 requests regardless of status.  Setting the parameter with a value of OFF will prevent any 2507 requests from being reported.

10)	The APPT LINKING ENHANCED DIALOGUE prompt sets this parameter and allows the site to turn on/off prompts and warnings that will display when making C&amp;P appointments.  If this parameter is turned ON, AMIE will furnish prompts and warnings to assist the scheduling clerk in correctly linking 2507 requests with the appointments scheduled to complete those requests.  If this prompt is turned OFF, the additional prompts will not be displayed.  (When this parameter is OFF, the only prompt displayed while scheduling a C&amp;P appointment is a prompt for 2507 request selection.  This prompt will only be displayed when the veteran has more than one 2507 request with a "Pending, Reported" status.)

### Queued Tasks

The following options may be put on the TaskManager for the suggested times or may be scheduled according to the site's preference.  Failure to set them properly will inhibit the full benefits of the AMIE software.  The AMIE software does not save and restore the existing dates/times for these options during initialization.

#### 7131/7132

DVBA REGIONAL TASK

This option generates the new 7131 request list daily for MAS.  It must be run before the business day begins.  The output goes to the printer specified by MAS which is stored in the AMIE SITE PARAMETER file (#396.1).

DVBA 7132 TASKMAN

This option generates the Notices of Discharge for the regional office.  It must be run early in the morning, prior to normal business hours.

DVBA GENERATE 21-DAY CERTIF

This option generates and releases the 21-Day Certificates for the regional office at 12:05 a.m.

DVBA REGIONAL PURGING PROGRAM

This option is used to take care of the day-to-day purging of old data.  Parameters are set through the AMIE SITE PARAMETER file (#396.1).

DVBA AUTO FINALIZE 7131 TASK

This option finalizes requests without any operator intervention.

**NOTE:** With the exception of the purge option, all of the above 7131/7132 options must have a printer specified when they are set up on TaskManager.  The options will generate either the report or a notice that there was nothing to print.  If a printer is not specified, the task will not run.

#### C&amp;P

Please make note of the printer requirements of the following three C&amp;P options.  Only DVBA C CHECK 2507 INTEGRITY TM requires a printer through TaskMan.

DVBA C PRINT NEW C&amp;P REQ TM

This option generates the new C&amp;P requests daily for MAS.  It needs to be run before the business day begins.  It will print to the printer specified in the REMOTE SITE (2507) field in the AMIE SITE PARAMETER file (#396.1).

DVBA C CHECK 2507 INTEGRITY TM

This option examines the 2507 REQUEST file (#396.3) and checks for any missing data.  It should be scheduled to run daily after the new request report runs.  Any printer may be specified when setting this up.

**Servers**

Servers are options which may be directly addressed via MailMan.  These options are designated as "servers" in the Option file (#19).  When mail comes addressed to it, whatever action is designated in the option will be performed according to the server action.  Please refer to the VA MailMan documentation for more information on servers and their functions, if necessary.  An example of a server option follows.

D P^DI

Select OPTION: **ENTER** OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PATIENT// **19** OPTION          (5345 entries)

EDIT WHICH FIELD: ALL// **SERVER ACTION**

THEN EDIT FIELD: **SERVER AUDIT**

THEN EDIT FIELD: **SERVER BULLETIN**

THEN EDIT FIELD: **SERVER MAIL GROUP**

THEN EDIT FIELD: **SERVER REPLY**

THEN EDIT FIELD: **&lt;RET&gt;**

STORE THESE FIELDS IN TEMPLATE: **&lt;RET&gt;**

Select OPTION NAME: **DVBA C PROCESS MAIL MESSAGE** Process C&amp;P Mail Message

SERVER ACTION: RUN IMMEDIATELY// **?**

What do you want the menu system to do when a request for this server

option is received from the mail system.

CHOOSE FROM:

R        RUN IMMEDIATELY

Q        QUEUE SERVER ROUTINE

N        NOTIFY MAIL GROUP (DO NOT RUN)

I        IGNORE REQUESTS

SERVER ACTION: RUN IMMEDIATELY// **&lt;RET&gt;**

SERVER AUDIT: YES// **?**

Do you want all requests for this server, and results of those requests

logged?

CHOOSE FROM:

Y        YES

N        NO

SERVER AUDIT: YES// **&lt;RET&gt;**

SERVER BULLETIN: **&lt;RET&gt;**

SERVER MAIL GROUP: **&lt;RET&gt;**

SERVER REPLY: SEND REPLY IN ALL CASES// **&lt;RET&gt;**

## Routines

In accordance with VHA Directive 10-93-142 regarding security of software, the following routines and their accompanying checksums should not be modified locally.

DVBCAMI1	value	=	5901817

DVBCAMI2	value	=	12729591

DVBCAMI3	value	=	3088709

DVBCAMIS	value	=	5835381

DVBCCNNS	value	=	6465570

DVBCLKT2	value	=	7808623

DVBCLKTL	value	=	6998431

DVBCMKL2	value	=	9133939

DVBCMKLK	value	=	6462243

DVBCSDEV	value	=	742431

DVBCUTL2	value	=	16484712

DVBCUTL5	value	=	4812185

DVBCUTL6	value	=	5521630

DVBCUTL7	value	=	4066959

DVBCUTL8	value	=	5560283

### Routine List

Use the following steps to get a complete list of the routines in the AMIE software.

1. Programmer Options Menu
2. Routine Tools Menu
3. First Line Routine Print Option
4. Routine Selector: **DVBA*** , **DVBC***

### Callable Routines

There are no callable routines in the AMIE software.

### Routines to Map

There are no AMIE routines recommended for mapping.

## Files

Per VHA Directive 10-93-142 regarding security of software, some of the AMIE Data Dictionaries may not be modified.  The file descriptions of these files are so noted.

### File List with Descriptions

File #	File Name	Description	Global

31	DISABILITY	Contains the VA-recognized disability conditions as	^DIC(31,

CONDITION	used when rating for compensation/pension.

396	FORM 7131	Holds all requests for 7131 information.  See the cross-	^DVB(396,

references portion of this section re instructions on

reindexing 'AE' and 'AF' cross-references.

396.1	AMIE SITE	Holds the AMIE software-specific parameters for	^DVB(396.1,

PARAMETER	the site.

396.2	AMIE	Holds various parameters for specialized reporting in 	^DVB(396.2,

REPORT	the AMIE software.  (Used specifically when generating

and printing Notices of Discharge.)

396.21	CAPRI CLINICAL	This file will store transmission data from a CAPRI GUI	^DVB(396.21,

EFOLDER	User transmitting Clinical Documents

TRANSMISSIONS

396.3	2507	Holds all 2507 requests generated from regional office	^DVB(396.3,

REQUEST	personnel.

396.4	2507 EXAM	Contains all exams associated with 2507 requests.  	^DVB(396.4,

DO NOT EDIT THIS FILE.

396.5	2507	Holds all current reasons why a 2507 exam may be	^DVB(396.5,

CANCELLATION	cancelled.  DO NOT EDIT THIS FILE.

REASON

396.6	AMIE EXAM	Contains the current listing of all valid 2507 exams	^DVB(396.6,

that may be requested.  DO NOT EDIT THIS FILE.

396.7	2507 BODY 	Contains all body system names to which the 2507	^DVB(396.7,

SYSTEM	exams are related.

396.94	2507 INSUFFI-	Contains reasons an exam may be returned as	^DVB(396.94,

CIENT REASONS	insufficient.  DO NOT EDIT THIS FILE.

396.95	AMIE C&amp;P EXAM 	Used to keep historical information for C&amp;P exam 	^DVB(396.95,

TRACKING	appointments.  It is also used to adjust the total

processing time for 2507 requests.  DO NOT EDIT

THIS FILE.

Use the following steps to get information about the files and templates in the AMIE software.

### File Flow (Relationships Between Files)

1. VA FileMan Menu
2. Data Dictionary Utilities Menu
3. List File Attributes Option
4. Enter file number or range of file numbers.
5. Select Listing Format:  Standard
6. You will see what files point to the selected file(s).  To see what files the selected files point to, look for fields that say "POINTER TO".

### Templates

1. VA FileMan
2. Print File Entries Option
3. Output from what File:	Print Template

Sort Template

Input Template

List Template

4. Sort by: **Name**
5. Start with name: **DVBA** , **DVBC**
6. Within name, sort by: **&lt;RET&gt;**
7. First print field: **Name**

#### VA List Manager Templates

DVBA DISCHARGE TYPES	VA List Manager template used in the Discharge

Report option for selection of discharge types.

#### VA List Manager Protocols

DVBA ACCEPT DISCHARGE TYPES	Action to accept the list of discharge types in the

Discharge Report and Report for Pension and A&amp;A

options.

DVBA ADD DISCHARGE TYPE	Action to add discharge types to the discharge type

list.

DVBA CREATE DISCHARGE TYPE LIST	Action to create a new list of discharge types.

DVBA DELETE DISCHARGE TYPES	Action to delete discharge types from the discharge

types list.

DVBA DISCHARGE TYPES (Menu)	Menu that contains all of the protocols for this

functionality.

DVBA C&amp;P SCHD EVENT	Protocol that is hooked on to the appointment event

to link the AMIE and Scheduling software.

### Globals to Journal

It is highly recommended that you journal global ^DVB, as this contains information that concerns monetary benefits or adjudication information for the veteran.  It is not, however, recommended that you journal the new global ^DVBP, because the two new files stored in this global will not be changed by either the AMIE software or the sites.  (Refer to the Installation Steps section of the Installation Guide for additional information.)

### Cross-References

^DVB(396.3,"AF",Request Status, Regional Office,DA)

This cross-reference was built to remove the "D" cross-reference from the VA FileMan lookup.  It is on Field #17 and Field #2 of File #396.3.

^DVB(396.4,"APS",Patient IFN,Exam IFN,Exam status,DA)

This contains the patient's internal file number, the exam IFN, and the exam status.  It is set on three fields:  .02, .03, and .04.  Recross-referencing any one of these fields is sufficient to reindex the file.

^DVB(396.4,"APE",Patient IFN,Exam name,Request date,DA)

This contains the patient's internal file number, the exam name, and the request date.  It is set on two fields:  .02 and .03.  Recross-referencing any one of these fields is sufficient to reindex the file.

^DVB(396.6,"D",AMIE Worksheet #,DA)

This contains the AMIE work sheet number.  It is set on Field #.07.  Recross-referencing this field is sufficient to recreate the "D" cross-reference.

^DVB(396,"AC",Station # from Claim Folder Location,21 day Cert. Release Status,DA)

This cross-reference was built to remove the old "C" cross-reference from the VA FileMan lookup.  It is on Field #6.82 of File #396.  It is used to order the 21 day certs by release status and claim folder location.

^DVB(396,"AE",Rpt Transfer Dte,Division Rpt Transferred to,DA,Rpt Field #)

This contains the transfer date and division, the IEN, and the report field number.

^DVB(396,"AF",DA,Rpt Transfer Dte,Division Rpt Transferred to,Rpt Field #)

This contains the transfer date and division, the IEN, and the report field number.

To reindex either the "AE" or "AF" cross-reference, the following fields must be reindexed.

NOTICE OF DISCHARGE DIVISION	or	NOTICE OF DISCHARGE TRAN DATE

and

HOSPITAL SUMMARY DIVISION	or	HOSPITAL SUMMARY TRAN DATE

and

CERTIFICATE (21-DAY) DIVISION	or	CERTIFICATE (21-DAY) TRAN DATE

and

EXAM OF COND LISTED IN REMARKS	or	EXAM OF COND LISTED IN

DIVISION		REMARKS TRAN DATE

and

SPECIAL REPORT DIVISION	or	SPECIAL REPORT TRAN DATE

and

COMPETENCY REPORT DIVISION	or	COMPETENCY REPORT TRAN DATE

and

VA FORM 21-2680 DIVISION	or	VA FORM 21-2680 TRAN DATE

and

ASSET INFORMATION DIVISION	or	ASSET INFORMATION TRAN DATE

and

ADMISSION REPORT DIVISION	or	ADMISSION REPORT TRAN DATE

and

OPT TREATMENT RPT DIVISION	or	OPT TREATMENT RPT TRAN DATE

and

BEGINNING DATE/CARE DIVISION	or	BEGINNING DATE/CARE TRAN DATE

To complete reindexing of the "AE" cross-reference, one of the following fields must be indexed:  DATE OF REQUEST or DIVISION.

## Exported Options

### Menu Diagram

Take the following steps to obtain information about the menus for the AMIE software.

Programmers Options

Menu Management Menu

Display Menus and Options Menu

Diagram Menus

Select User or Option Name: **O.AMIE MASTER MENU**

## Archiving and Purging

### Archiving

There are no archiving capabilities in the AMIE software.

### Purging

The DVBA Regional Purging Program option deletes all FINALIZED requests which are older than the date set in the AMIE SITE PARAMETER file (#396.1).  It should normally be set to run daily on TaskMan, as it takes several minutes to run in programmer mode.  In addition to purging the FORM 7131 file (#396), it also purges the AMIE REPORT file (#396.2).

The amount of 7131 information purged by this program is determined by the number of days to keep history parameter set through the Regional File Site Parameter Setup option.  It is suggested to keep at least 30 days on file at all times, but no more than 120 days.  The NUMBER OF DAYS TO KEEP HISTORY field (#9) of the AMIE Site Parameter file (#396.1) will automatically keep 30 days of report data if no value is in that field.

While the AMIE software uses a very small amount of disk space, it is wise not to let the data accumulate if it is not needed by the hospital.

## External/Internal Relations

### External Relations

#### Minimum Software Versions Required

The following minimum software versions are required in order to install this version of AMIE.

VA FileMan V. 20.0

Kernel V. 7.1

MailMan V.7.1

Kernel Tool Kit V. 7.2

Lab V. 5.0

PIMS V. 5.3

HINQ V. 4.0

#### External Options

XMUSER - MailMan Menu (to facilitate the RO)

DG INPATIENT INQUIRY EXTENDED - Detailed Inpatient Inquiry

SDPATIENT - Patient Profile

#### Special Agreements for AMIE

The C&amp;P portion of AMIE needs to use LAYGO into the Patient file (#2) in two different areas:  the addition of new C&amp;P requests by the regional office, and via transfers of exams and requests to other sites.

As a result of this special need, and the benefit of increasing service to the veteran community, a special agreement exists between MAS and AMIE.  This agreement is as follows.

1)	LAYGO is permitted into File #2 via FileMan editing.  The fields entered are required and sufficient to prohibit errors in any monthly totals generated by the medical centers.

2)	Except for patient address information, editing of existing information in File #2 by regional office personnel is not allowed.  They are permitted to add new veterans, but cannot edit information that previously exists, other than the address information.  This also applies to existing information at remote transfer sites.  If the veteran already exists at the remote site, that record is used and no veteran information from the originating site is transferred.

3)	Whenever a new veteran is added to File #2 via the C&amp;P portion of AMIE, whether directly by the regional office or via transfer of a request and exams, a mail bulletin is generated to the members of the DVBA C NEW C&amp;P VETERAN mail group.  This bulletin alerts the medical center that a new veteran has been added for C&amp;P purposes.

#### Database Integration Agreements (DBIAs)

Take the following steps to get information about the DBIAs for the AMIE software.

Custodial Package

1. FORUM
2. DBA Menu
3. Integration Agreements Menu
4. Custodial Package Menu
5. Active by Custodial Package Option
6. Select Package Name: **AMIE**

Subscriber Package

1. FORUM
2. DBA Menu
3. Integration Agreements Menu
4. Subscriber Package Menu
5. Print Active by Subscribing Package
6. Start with subscribing package: **AMIE**

### Internal Relations

There are no programs or files that can function independently in the AMIE software.

## Package-wide Variables

There are no package-wide or special variables in the AMIE software.

### Key Variables

PNAM	Patient name

DFN	Internal ^DPT number

SSN	Social security number

CFLOC	Claim folder location

DCHGDT	Discharge date

ADMDT	Admission date

## How to Generate Online Documentation

This section describes some of the various methods by which users may secure AMIE technical documentation.  Online technical documentation pertaining to the AMIE software, in addition to that which is located in the help prompts, may be generated through utilization of several Kernel options.  These include %INDEX and VA FileMan List File Attributes.  Further information about other utilities which supply online technical documentation may be found in the Kernel Reference Manual.

### XIndex

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards.  The XINDEX output may include the following components:  compiles list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references.  By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the AMIE software, specify the following namespace at the "routine(s) ?&gt;" prompt:  DVBA* and DVBC*.  AMIE initialization routines which reside in the UCI in which XINDEX is being run, as well as compiled template routines found within the AMIE namespace, should be omitted at the "routine(s)?&gt;" prompt.  To omit routines from selection, preface the namespace with a minus sign (-).

### List File Attributes

This VA FileMan option allows the user to generate documentation pertaining to files and file structure.  Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s):  file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates.  In addition, the following applicable data is supplied for each field in the file:  field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.  For a comprehensive listing of AMIE files, please refer to the FILES section of this manual.

## Security

### Security Management

VA Directive 10-93-142 prohibits local modifications to VistA software.

### General Security

#### Remote Systems

The AMIE software does not transmit data to any remote systems.

#### Contingency Planning

Your facility should have a local contingency plan in the event of application problems in a live environment.  It should identify the procedure for maintaining functionality provided by the AMIE software in the event of system outage.

#### Interfacing

There are no special interfacing requirements for the AMIE software.

#### Electronic Signatures

The AMIE software does not use electronic signatures.

### Security Keys

Take the following steps to get information about the security keys used with the AMIE software.

1. VA FileMan Menu
2. Print File Entries Option
3. Output from what File: **SECURITY KEY**
4. Sort by:  Name
5. Start with name: **DVBA** to **DVBC**
6. Within name, sort by: **&lt;RET&gt;**
7. First print field: **Name**
8. Then print field: **Description**

**Note:** Some keys do not affect the menu operation.  This is due to some options having several different functions which are limited in scope by the key.  This limitation is done internally by the program being used.

### FileMan Access Codes

The following is a list of recommended VA FileMan access codes associated with each file contained in the AMIE software.

File	File	DD	RD	WR	DEL	LAYGO

Number	Name	Access	Access	Access	Access	Access

31	DISABILITY

CONDITION	@	D	@	@	@

396	FORM 7131	@	#	#	#	#

396.1	AMIE SITE

PARAMETER	@	#	#	@	@

396.2	AMIE REPORT	@	#	#	#	#

396.21              CAPRI CLINICAL	@	@	@	@	@

EFOLDER

TRANSMISSIONS

396.3	2507 REQUEST	@	#	#	#	#

396.4	2507 EXAM	@	#	#	#	#

396.5	2507 CANCELLATION

REASON	@	#	@	@	@

396.6	AMIE EXAM	@	#	@	@	@

396.7	2507 BODY SYSTEM	@	#	@	@	@

396.94	2507 INSUFFICIENT

REASONS	@	#	@	@	@

396.95	AMIE C&amp;P EXAM

TRACKING	@	#	#	#	#

## Glossary

21-Day Certificate	The 7132 issued to the regional office after a veteran has been hospitalized for a period of 21 days or more.

AMIE	Automated Medical Information Exchange

AMIE Work Sheet	A form used to aid the physician in the completion of a C&amp;P exam.  It provides instruction as to what medical information is required for a particular C&amp;P examination.

Body System	The systemic area of the human body to which a particular examination belongs.  This is in accordance with the definition in the C&amp;P Rating Specialist Guide at each regional office.

Bulletin	An electronic mail message generated whenever certain conditions are met while executing application programs.

C&amp;P	Compensation and Pension

C&amp;P Routing Location	An entry in the AMIE Site Parameter file (#396.1) which points to the Hospital Location file (#44).  Any locations entered are used to screen lab and radiology results for veterans when final C&amp;P information is printed.

Division	A field which is in each user's record and which denotes to what station the user belongs.  It is translated for program usage into the three digit station number of the hospital or the regional office.

Request	An electronic log of information needed by the regional office.

Routing Location	The medical center division (reference File #40.8) to which a request belongs and at which initial paperwork should be printed.

Transfer	The movement of an entire C&amp;P request or one or more exams of a request to another site for processing and subsequent return.

VBA	Veterans Benefits Administration

VHA	Veterans Healthcare Administration

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: AMIE Version 2.7 Technical Manual

### Compensation and Pension

A 2507 examination request is a request for specific examination(s) to be performed on a veteran to determine compensation or pension benefits.  The regional office has the ability to add a patient to the medical center's database if s/he does not exist there.  All aspects of the examination process from notifying MAS of the request to scheduling of the exams, transcribing the results, and forwarding the results to the RO are handled through AMIE.

Medical centers have the ability to transfer any exams they are unable to perform to other sites via MailMan messages.  The AMIE software at the receiving medical center takes the mail message and enters a 2507 request into that hospital's database.  Once these exams are completed, they are transferred back to the original medical center.

Both modules of AMIE generate a number of reports to provide medical center and regional office personnel with the status and timeliness of any request.  The AMIS 290 report monitors the progress of 2507 exams.

The AMIE software greatly reduces the time it takes to exchange patient information between the medical centers and regional offices.  It reduces the amount of paper forms, provides better monitoring of the exam process, and most importantly, allows the veteran to receive benefits due her/him in a more timely and efficient manner.

## ## Implementation and Maintenance

Implementation includes setting up required parameters in the AMIE Site Parameter file (#396.1) and the required TaskMan options.  See the Archiving and Purging Section for purging requirements.

**AMIE SITE PARAMETER File Setup**

Use the Regional File Site Parameter Setup option on the AMIE Medical Administration Menu to set up the AMIE site parameter file (#396.1).  There can be only one entry in this file.

1)	Set up the regional offices that will be accessing your system.  If offices are not set up, Notices of Discharge or 21-Day Certificates will not be produced.  This field is a pointer to the institution file (#4), and as each Notice of Discharge is compiled, this field is checked to see if the veteran's claim folder location is one of the allowed offices.

2)	Set up the valid medical center divisions for your facility for the 7131/7132 part of the AMIE software.  We use the term "REMOTE SITE (7131)"; however, this refers to the parent hospital as well.  If this is not properly filled in, reports for new requests will not be generated.  Even if you have only one division (the hospital itself), this must be filled in.  Be sure to enter a valid printer name or number in the PRINTER NUMBER field.  Failure to do so will result in no reports being printed.  The device must previously exist in File #3.5.  Repeat this step for each remote 7131/7132 site.

3)	Edit the REMOTE SITE (2507) field for the C&amp;P part of the AMIE software.  This is a pointer to the medical center division file (#40.8).  The site selected must already be in the MEDICAL CENTER DIVISION file (#40.8).  The same warnings apply to this field as the REMOTE SITE (7131) field.  If this is not set up properly, the AMIE software will not function correctly.  Enter the printer for the remote site or parent hospital.  This is a free text pointer to the DEVICE file (#3.5).  The printer must already exist in the DEVICE file (#3.5).  Once the printer is entered, the program will automatically pull the "name" of the printer and echo it as "Stored internally as NNN".  This is a symbol commonly referred to as ION and it is used for queuing purposes by TaskMan.  Even if there are no remote clinics or divisions, this must be set up for the parent hospital.  Repeat this step for any additional remote C&amp;P sites.

4)	Set up the C&amp;P routing locations.  Enter any hospital location (pointer to File #44) which can be used for C&amp;P locations or clinics.  This would be those locations to which automatic lab and/or X-ray results would normally be routed.  This is a multiple field.  These locations will be used during the final printing of a C&amp;P request to screen lab and radiology results for those which were ordered for a C&amp;P exam.  If these locations are not set up, no lab or radiology results will be printed with the final C&amp;P exams.  When ordering lab and x-rays as part of the C&amp;P exam, the PATIENT LOCATION must be one of the entries here or the results will not be printed automatically.

5)	Answer the prompt RUN NEW REQUESTS ON SATURDAY?.  Answer YES to have Friday requests printed on Saturday or NO to have them printed on Monday or the first work day after Monday.  If this field is left unanswered, the report-producing programs will automatically assume a NO answer.

6)	Make sure that all of the regional office users have **only one** division assigned to them in the NEW PERSON file (#200).  This should be the station number of their regional office.  Failure to assign the correct division, or if multiple divisions are inadvertently assigned, will result in incorrect data being entered into the file.

7)	The AMIE software makes use of the server function available in the VA Kernel.  In conjunction with the servers, there is one server error bulletin: XQSERVER.  This bulletin will notify members of mail groups assigned to it of any server problems.  The AMIE software will not address any usage or other items related to this function.  It will be left up to the individual sites whether this bulletin is populated with mail groups.  It is recommended that the sites do so, since this bulletin could possibly report any problems with C&amp;P transfers.

8)	The Days to Keep 2507 History parameter has been initially set at 120 days.  The site may want to adjust this parameter to a higher number.  This will provide the regional office personnel the ability to link insufficient exams to the original 2507 request.  It will also allow the medical center to keep 2507 requests and the results for up to 999 days.

9)	Answer the 2507 INTEGRITY REPORT STATUS prompt according to the information you wish to be included on the report generated with the options Check C&amp;P File Integrity (TaskMan) and Check C&amp;P File Integrity.  Setting the parameter with a status of OPEN will tailor the report so that only "Pending, Reported" 2507 requests will be included.  If the parameter has a value of COMPLETED, only 2507 requests with a status of "Released to RO, not Printed" or "Completed, Printed by RO" will be included.  Setting the parameter with a value of ALL will report all 2507 requests regardless of status.  Setting the parameter with a value of OFF will prevent any 2507 requests from being reported.

10)	The APPT LINKING ENHANCED DIALOGUE prompt sets this parameter and allows the site to turn on/off prompts and warnings that will display when making C&amp;P appointments.  If this parameter is turned ON, AMIE will furnish prompts and warnings to assist the scheduling clerk in correctly linking 2507 requests with the appointments scheduled to complete those requests.  If this prompt is turned OFF, the additional prompts will not be displayed.  (When this parameter is OFF, the only prompt displayed while scheduling a C&amp;P appointment is a prompt for 2507 request selection.  This prompt will only be displayed when the veteran has more than one 2507 request with a "Pending, Reported" status.)

### Queued Tasks

The following options may be put on the TaskManager for the suggested times or may be scheduled according to the site's preference.  Failure to set them properly will inhibit the full benefits of the AMIE software.  The AMIE software does not save and restore the existing dates/times for these options during initialization.

#### 7131/7132

DVBA REGIONAL TASK

This option generates the new 7131 request list daily for MAS.  It must be run before the business day begins.  The output goes to the printer specified by MAS which is stored in the AMIE SITE PARAMETER file (#396.1).

DVBA 7132 TASKMAN

This option generates the Notices of Discharge for the regional office.  It must be run early in the morning, prior to normal business hours.

DVBA GENERATE 21-DAY CERTIF

This option generates and releases the 21-Day Certificates for the regional office at 12:05 a.m.

DVBA REGIONAL PURGING PROGRAM

This option is used to take care of the day-to-day purging of old data.  Parameters are set through the AMIE SITE PARAMETER file (#396.1).

DVBA AUTO FINALIZE 7131 TASK

This option finalizes requests without any operator intervention.

**NOTE:** With the exception of the purge option, all of the above 7131/7132 options must have a printer specified when they are set up on TaskManager.  The options will generate either the report or a notice that there was nothing to print.  If a printer is not specified, the task will not run.

#### C&amp;P

Please make note of the printer requirements of the following three C&amp;P options.  Only DVBA C CHECK 2507 INTEGRITY TM requires a printer through TaskMan.

DVBA C PRINT NEW C&amp;P REQ TM

This option generates the new C&amp;P requests daily for MAS.  It needs to be run before the business day begins.  It will print to the printer specified in the REMOTE SITE (2507) field in the AMIE SITE PARAMETER file (#396.1).

DVBA C CHECK 2507 INTEGRITY TM

This option examines the 2507 REQUEST file (#396.3) and checks for any missing data.  It should be scheduled to run daily after the new request report runs.  Any printer may be specified when setting this up.

**Servers**

Servers are options which may be directly addressed via MailMan.  These options are designated as "servers" in the Option file (#19).  When mail comes addressed to it, whatever action is designated in the option will be performed according to the server action.  Please refer to the VA MailMan documentation for more information on servers and their functions, if necessary.  An example of a server option follows.

D P^DI

Select OPTION: **ENTER** OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PATIENT// **19** OPTION          (5345 entries)

EDIT WHICH FIELD: ALL// **SERVER ACTION**

THEN EDIT FIELD: **SERVER AUDIT**

THEN EDIT FIELD: **SERVER BULLETIN**

THEN EDIT FIELD: **SERVER MAIL GROUP**

THEN EDIT FIELD: **SERVER REPLY**

THEN EDIT FIELD: **&lt;RET&gt;**

STORE THESE FIELDS IN TEMPLATE: **&lt;RET&gt;**

Select OPTION NAME: **DVBA C PROCESS MAIL MESSAGE** Process C&amp;P Mail Message

SERVER ACTION: RUN IMMEDIATELY// **?**

What do you want the menu system to do when a request for this server

option is received from the mail system.

CHOOSE FROM:

R        RUN IMMEDIATELY

Q        QUEUE SERVER ROUTINE

N        NOTIFY MAIL GROUP (DO NOT RUN)

I        IGNORE REQUESTS

SERVER ACTION: RUN IMMEDIATELY// **&lt;RET&gt;**

SERVER AUDIT: YES// **?**

Do you want all requests for this server, and results of those requests

logged?

CHOOSE FROM:

Y        YES

N        NO

SERVER AUDIT: YES// **&lt;RET&gt;**

SERVER BULLETIN: **&lt;RET&gt;**

SERVER MAIL GROUP: **&lt;RET&gt;**

SERVER REPLY: SEND REPLY IN ALL CASES// **&lt;RET&gt;**
