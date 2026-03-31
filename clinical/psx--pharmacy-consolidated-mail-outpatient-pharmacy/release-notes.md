---
title: CMOP Version 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: "- [# RELEASE NOTES for CMOP V2.0](#release-notes-for-cmop-v20) - [Medical Center Release Notes:](#medical-center-release-notes) - [Intranet](#intranet) - [Mail—Additional Flexibility Added to Outpatient Pharmacy System Parameters](#mailadditional-flexibility-added-to-outpatient-pharmacy-system-param"
audience: 
keywords: 
  - cmop
  - mail
  - table
  - contents
  - release
  - transmission
  - status
  - modified
  - reports
  - local
page_count: 0
word_count: 1654
section_count: 13
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_2_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_2_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](cmop-version-2-release-notes/001.png)

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP)RELEASE NOTES

April 1997

V*IST*A Software Development

Clinical Ancillary Product Line

BLANK FOR 2-SIDED COPYING

# # RELEASE NOTES for CMOP V2.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# RELEASE NOTES for CMOP V2.0](#release-notes-for-cmop-v20)
  - [Medical Center Release Notes:](#medical-center-release-notes)
  - [Intranet](#intranet)
  - [Mail—Additional Flexibility Added to Outpatient Pharmacy System Parameters](#mailadditional-flexibility-added-to-outpatient-pharmacy-system-parameters)
  - [New MailMan Messages](#new-mailman-messages)
  - [Modified Options](#modified-options)
  - [Modified Menus](#modified-menus)
  - [Reports Option \[PSX REPORTS MENU\]](#reports-option-psx-reports-menu)
  - [Modified Reports](#modified-reports)
  - [New Reports](#new-reports)
  - [New Menus and Options](#new-menus-and-options)
  - [<u> Menus</u>](#u-menusu)
  - [<u>Options</u>](#uoptionsu)
> These release notes provide a brief description of the changes in version 2.0 of the Consolidated Mail Outpatient Pharmacy software package. In addition to the release notes, it is highly recommended that you also read the User, Installation, and Technical guides provided with version 2.0. These manuals have been rewritten to include essential information related to the enhancements and modifications described here.
> This version (2.0) of the Consolidated Mail Outpatient Pharmacy software package can only be run with a standard MUMPS operating system. It also requires the following VA software applications.

## Medical Center Release Notes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Remote Medical Center</u> <u>Minimum Version Required</u>

> Kernel 8.0

> MailMan 7.1

> VA FileMan 21.0

> National Drug File (NDF) 3.16

> Outpatient Pharmacy (OP) 6.0 *(must have patch number PSO\*6\*155, Seq. \#154)*

> The above software is not included in this package and MUST BE INSTALLED (including all released patches) PRIOR to the install of the CMOP V. 2.0 software to ensure complete functionality.

To ensure the integrity of all prescription data, the Consolidated Mail Outpatient Pharmacy software should ALWAYS function at Veterans Administration Medical Centers (VAMCs) with the Outpatient Pharmacy VERIFICATION turned ON.

## Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Documentation for this product can now be found on the intranet. You will find it at the following address:

> <span class="mark">REDACTED</span>

> This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals. Click on the Consolidated Mail Outpatient Pharmacy (CMOP) link and it will take you to the CMOP Homepage. You can also get there by going straight to the following address:

> <span class="mark">REDACTED</span>

> Remember to bookmark this site for future reference.

  
NEW FUNCTIONALITY for Medical Centers<u>Purge of CMOP Rx Queue \[PSXR PURGE\]</u>

> The purge of data contained in the CMOP RX QUEUE File (#550.1) has been modified. Instead of purging the data on acknowledgement of the transmission from the CMOP host facility, the data will be retained until the vendor automated dispensing equipment at the host has received the data. This has been done in preparation of the Disaster Recovery procedures which will be released in and enhancement patch to follow this release of CMOP V. 2.0.

<u>*ResubmitCMOP Rx* \[PSXR RESUBMIT\]</u>

> The *ResubmitCMOPRx* option is used to send an Rx back to the CMOP after it has been returned from the CMOP with a status of NOT DISPENSED. Users are required to hold the PSXRESUB security key to access this option.

> You may not resubmit if

1.  The NOT DISPENSED reason is Duplicate Fill.
2.  The fill does not have a CMOP status of NOT DISPENSED.
3.  The fill has already been resubmitted.
4.  The NOT DISPENSED fill is not the last fill in the Rx.

Select OPTION NAME: <u>CMOP Site</u> Manager Menu

Select CMOP Site Manager Menu Option: <u>RES</u>ubmit CMOP Rx

CMOP Prescription Resubmission Utility

Enter the Rx \# to resubmit: <u>15666</u>

You have chosen Rx \# 15666 to be resubmitted to the CMOP.

Do you want to continue? : (Y/N): NO// <u>Y</u>ES

RX# 15666 SUSPENDED FOR CMOP TRANSMISSION 02-18-97.

Enter the Rx \# to resubmit:

Select CMOP Site Manager Menu Option: <u>\<RET\></u><u>  
*Setup Auto-transmission* \[PSXR AUTO TRANSMIT\]</u>

> This option has been modified to include a system parameter, NUMBER OF DAYS TO TRANSMIT. This parameter indicates the number of days to transmit thru for an automatic data transmission. If this field is null or contains a zero the auto transmissions will select data through today as the default. If the field contains a number, n, from 1 to 10, transmission data will be selected for T+n days. The maximum NUMBER OF DAYS TO TRANSMIT is ten(10). Please note the CMOP system parameter, NUMBER OF DAYS TO TRANSMIT is different from the Outpatient site parameter, DAYS TO PULL FROM SUSPENSE. For example if the NUMBER OF DAYS TO TRANSMIT is two(2) and the DAYS TO PULL FROM SUSPENSE is seven(7) the transmission data will be selected for T+2 days. Once selected, for every patient in this date range, the software will then look ahead in RX SUSPENSE file \#52.5 for any Rx’s for these patients for the next seven days (T+7days). If the patients have Rx’s for this date range they will be added to the data transmission.

Example:

Select Transmission Menu Option: <u>S</u>etup Auto-transmission

Enter the date to start automatic processing: NOW// <u>\<RET\></u> (FEB 26, 1997@12:35)

Number of days to transmit thru: (0-10): 0// <u>10</u>

Enter rescheduling frequency (hours) for transmission: (1-96): <u>96</u>

Begin Automatic Transmissions : FEB 26, 1997@12:35

Rescheduling Frequency : 96 hours

Number of days to transmit through : 10

Is this correct? NO// <u>Y</u> YES

Select Transmission Menu Option: <u>\<RET\></u><u>*Reprint an Outpatient Label* \[PSO RXRPT\]</u>

> For version 2.0 all CMOP functionality has been removed from this Outpatient Pharmacy option. The standard Outpatient Pharmacy reprint functionality now applies. CMOP no longer exports modified OP options.

<u>Screen Profile Indicator for CMOP</u>

> OUTPATIENT PHARMACY PATCH PSO\*6\*155 added the following new CMOP functionality to the Rx screen profile:

1)  If the drug the Rx is written for is marked for transmission to CMOP, a \> sign will be appended to the Status code as in A\> where the Rx has a status of active and the drug is marked for CMOP.
2)  If the latest fill for the Rx has been transmitted to the CMOP, a new status code of T will be appended to the local status as in CT where the Rx is canceled but has been transmitted to the CMOP. This could happen if the Rx was canceled after the transmission. The new code reflects the transmission status, while the existing code C indicates it was canceled locally.

## Mail—Additional Flexibility Added to Outpatient Pharmacy System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy patch PSO\*6\*158 must be installed to complete the functionality of this option.

> This functionality allows the user-designated patient’s Rx’s from

1.  being filled by the CMOP and
2.  being mailed at all. In order to accomplish this goal, the following changes have been made.
1)  The MAIL field which is able to be edited in the *Update Patient Record* option, located on the *Outpatient Pharmacy Manager’s* menu, has been modified as follows:

EXISTING CODES "0" = Regular Mail

"1" = Certified Mail (formerly Registered)

NEW CODES "2" = DO NOT MAIL

"3" = Local - Regular Mail

"4" = Local - Certified Mail

> B\) A new field, MAIL CODE EXPIRATION DATE, has been added to this option. The MAIL CODE EXPIRATION DATE will be used to place limits on the Codes 2,3,4 only. If the expiration date is not present, the Mail code will remain in place until edited. If the expiration date is present and has expired, a default value of Regular Mail (0) will be used by the software, but the actual Mail field value in the file will not be changed. The expiration date will remain in the file until edited by a user. This is not a required field.

> C\) Mail codes \> 1 will prevent the associated patient’s Rx’s from being sent to the CMOP for dispensing.

> D\) If a Mail Code of 2 (DO NOT MAIL) is present, the Outpatient Rx label format is modified by replacing the CRITICAL MEDICAL SHIPMENT advisory with DO NOT MAIL. Also, the patient’s address on the return mail label is replaced with the last 6 digits of the patient’s SSN.

> E\) A Mail code of 4 (Local Certified) will cause Certified to be printed on the local labels.

Select Outpatient Pharmacy Manager Option: <u>UPDATE</u> Patient Record

Select Patient: <u>CMOPPATIENT,ONE</u> 02-09-37 000123456

CMOPPATIENT,ONE ID#: 000-12-3456

201 EVERY WHERE DRIVE DOB: FEB 9,1937

BONNY HIGHLANDS PKWY

SLIP 44

WELLINGTON PHONE:

ALABAMA 35555 ELIG:

WEIGHT(Kg): HEIGHT(cm):

DISABILITIES:

ALLERGIES:

ADVERSE REACTIONS:

SOCIAL SECURITY NUMBER: 000123456// <u>^</u>

\>\>PHARMACY PATIENT DATA\<\<

CAP: SAFETY// <u>\<RET\></u>

MAIL: DO NOT MAIL// <u>??</u>

This field is used to:

A\) Determine whether this patient's Rx's are to be sent to the CMOP, or

retained for local distribution. If 2-4 are selected, none of this

patient's Rx's will be transmitted to the CMOP.

B\) Select what the mail priority is. The CMOP choices are limited to (0)

REGULAR and (1) CERTIFIED. Local mail may be designated (3) LOCAL -

REGULAR or (4) LOCAL - CERTIFIED. The 'DO NOT MAIL' code (2) may be used

to ensure that the patient's Rx's are not mailed.

Choose from:

0 REGULAR MAIL

1 CERTIFIED MAIL

2 DO NOT MAIL

3 LOCAL - REGULAR MAIL

4 LOCAL - CERTIFIED MAIL

MAIL: DO NOT MAIL// <u>\<RET\></u>

DIALYSIS PATIENT: <u>\<RET\></u>

MAIL STATUS EXPIRATION DATE: <u>??</u>

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

This field places a time limit on the 'Do Not Mail', 'Local - Regular

Mail' and 'Local - Certified Mail' conditions in the 'MAIL' field.

If a date is placed in this field and the software detects that the date

the Rx is processed is greater than the date in the field (past the

expired date) a default value of 'Regular Mail' will be assumed for the

'MAIL' field.

> **NOTE:** The actual value of the 'MAIL' field will not be changed by the

software, but can only be modified by a user editing the 'MAIL' field.

MAIL STATUS EXPIRATION DATE: <u>T</u> (FEB 24, 1997)

NARRATIVE: <u>\<RET\></u>

PATIENT STATUS: SC// <u>^</u>  
CMOP Host Facility<u>CMOP Host Environment</u>

> This version (2.0) of Consolidated Mail Outpatient Pharmacy requires, at least, the following VA software applications. This software is not included in CMOP and must be installed (including all released patches) prior to the installation of the CMOP V. 2 software to ensure complete functionality.

> <u>Host Facility</u> <u>Minimum Version Required</u>

> Kernel 8.0

> MailMan 7.1

> VA FileMan 21.0

> National Drug File (NDF) 3.16

> Cost Functionality for CMOP Host Facilities has not been removed from this

> version as originally intended in the Functional Specifications Document.

> This functionality continues to be used by some facilities and will remain

> indefinitely.

## New MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The CMOP Recovery Message is sent whenever a failed CMOP transmission is detected. This message is simply a notification message that the last transmission did not complete. CMOP recovery procedures were initiated to reset the data so that it will be transmitted in the next transmission for that division.

Subj: CMOP Recovery Message BIRMINGHAM, AL. \[#3288\] 21 Feb 97 10:29 CST

11 Lines

From: \<POSTMASTER@BAB.ISC-BIRM.VA.GOV\> in 'IN' basket. Page 1

------------------------------------------------------------------------------

The last CMOP transmission did not complete properly. The data for this

transmission will be sent to the CMOP during the next transmission for

that division.

If you have scheduled auto transmissions for CMOP, please check to see

that they are still scheduled for the correct time.

This message is just a notification that problems were detected with the last

transmission and that the data was sent to the CMOP facility for processing.

If you are getting this message frequently, please contact your IRM staff.

Otherwise there is not anything that you need to do.

> 2\) The CMOP Remote Error Condition Notice message is generated by the release data acknowledgement filer process whenever release data cannot be filed in the remote medical center’s PRESCRIPTION file.

Subj: CMOP Remote Error Condition Notice \[#38939\] 11 Dec 96 14:11 5 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST,FOUR) in 'IN' basket. Page 1

------------------------------------------------------------------------------

The following prescriptions could not be filed at BIRMINGHAM, AL. due to listed error conditions.

TRANS \# RX \# FILL \# REMOTE ERROR

521-741 15648 0 RELEASE DATE ALREADY EXISTS

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of options modified for version 2.0. Both functionality and output from these options have been extensively modified. Please refer to the Consolidated Mail Outpatient Pharmacy User Manual for further explanation.

<u>*Transmission Review* \[PSX TRANSMISSION\] Locked:</u> PSXCMOPMGR

> This option is used to display the status of current transmissions. The user can print a summary of all statuses or a summary for each status. The following is an explanation of the statuses:

> S = Summary

> Q = Queued

> P = Processed

> C = Closed

> H = Hold

> L = Labels Printed

<u>*Display System Status* \[PSX SYSTEM STATUS\]</u>

This option displays a screen of information for use by the CMOP Site Manager to review the status of CMOP processes. Information includes statuses on the CMOP interface, nightly background jobs, etc. This data should be reviewed regularly to ensure all processes are running as scheduled.

Release Data Acknowledgments \> 24 hours OUTSTANDING is a notification that release data has been returned to a remote medical center and not acknowledged within 24 hours. Use the *Resend Release Data* option to resend the data to the medical center.

Rejected Orders OUTSTANDING is a notification that patient order(s) have been rejected by the vendor system. The *Rejected Messages Report* option should be used to print a report of these orders.

example follows on next page

Select CMOP System Management Menu Option: <u>D</u>isplay System Status

CMOP SYSTEM STATUS

Interface : STOPPED

Transmissions Queued : Nothing in the Queue

Last Order Processed : 521-3-12..........BIRMINGHAM (C).........Feb 26@10:16

Last Query Completed : \#3................7 Rx's.................Feb 26@10:16

\*\*\*\*\*Release Data Acknowledgments \> 24 hours OUTSTANDING\*\*\*\*\*

\*\*\*\*\*Rejected Orders OUTSTANDING\*\*\*\*\*

Background Process Last Ran Scheduled For

Release Data Filed in Master Database....Feb 26@12:17...........Feb 26@12:32

Database Purge.......................................Not Scheduled

Release File Purge.......................Feb 25@23:00...........Feb 26@23:00

Release Acknowledgement File Purge.......Feb 25@23:30...........Feb 26@23:30

## Modified Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menus are modified for version 2.0. Both functionality and output from these menus have been extensively modified. Please refer to the CMOP User Manual for further explanation.

*Interface Menu* \[PSX INTERFACE MENU\]

> This menu contains options which control the operations of the CMOP interface. When the user enters the *Interface Menu* the one of the following current statuses of the interface communication link is displayed.

> *Monitor CMOP Interface*

> *Start CMOP Interface*

> *Stop CMOP Interface*

> A All Transmissions Queued. Sends all transmissions in the queue to the vendor. The interface will NOT stop after all transmissions have been sent to the vendor system.

> S Single Transmission. Only sends the transmission selected to the vendor. The interface will stop when the transmission download has completed.

> P Prioritize Queue. Allows the user to establish a priority for sending transmissions to the vendor. The interface will NOT stop after all transmissions have been sent to the vendor.

> Q Query Request. Allows the user to initiate a query request. Once the query request is complete the interface stops.

## *Reports* Option \[PSX REPORTS MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Menu text for the *ReportsMenu* option has been changed to *Reports* \[PSX REPORTS MENU\].

## Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of reports which have been modified for version 2.0. Please review these changes in detail in the CMOP User Manual.

> *Facility Activity Report* \[PSX ACTIVITY\]

> *Transmission Report Summary* \[PSX SUMMARY\]

## New Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of new reports added to version 2.0. Please review the individual options, examples, and descriptions provided in detail in the CMOP User Manual.

> *Duplicate Release Data Report* \[PSX DUPLICATE RELEASE\]

> *Report of Release Data Returned* \[PSX RELEASE REPORT\]

> These reports are now included on the *Reports* sub-menu of the

> *CMOP System Management Menu*. Additionally, all other label/report

> printing options are now included on the *Reports* menu. The new

> menu structure for Reports is :

> *Transmission Report Summary*

> *Rejected Messages Report*

> *Unreleased Rx's Report*

> *Duplicate Release Data Report*

> *Facility Activity Report*

> *Turnaround Time Report*

> *Report of Release Data Returned*

> *Print Rejected Orders*

> *Print Transmission Labels*

> *Label Restart Utility*

> *Reprint Transmission Labels*

## New Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *CMOP System Management Menu* has been redesigned to group similar tasks together and simplify menu navigation for personnel. A number of system parameters have been added to allow the CMOP Host facility to customize package operations to provide more efficient management of the prescription data workload processed each day. New menus, *Operations Management* and *Archive CMOP Data*, and new options, *Resend Release Data to VAMCs*, and *System Parameter Enter/Edit* have been added in version 2.0.

## <u> Menus</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Operations Management* \[PSX OPERATIONS MANAGEMENT\]

> This option manages the day to day operations of the background procedures

> necessary for transmission data management.

> *Start/Stop Background Filer*

> *Nightly Purge of CMOP Database*

> *Nightly Purge of Release Data \

> *Purge of Release Messages\*\

> *Resend Release Data to VAMCs*

> *System Parameter Enter/Edit*\*Note: *Nightly Purge of Release Data* \[PSX PURGE RELEASE\]

> The menu text for this option has changed from Start/Stop Nightly Purge of Release Data to read Nightly Purge of Release Data.

\*\*Note: *Purge of Release Messages* \[PSX PURGE RELEASE MESSAGES\]

> The menu text for this option has changed from Start/Stop Nightly Purge of Release Messages to read Purge of Release Messages.

*Resend Release Data to VAMCs* \[PSX RELEASE DATA RECOVERY\]

> This option provides a report of all release data mail messages that are greater than 24 hours old. Users can select mail messages to resend to the medical center for filing.

## <u>Options</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*System Parameter Enter/Edit* \[PSX SITE PARAMETERS\]

> This option will display the current CMOP system parameter settings which can be edited by the user.

Select Operations Management Option: <u>SY</u>stem Parameter Enter/Edit

Query Request Interval: 45 min// <u>?</u>

This is the minimum time interval between query requests.

Enter the number in hour(s) and/or fractions of an hour interval.

Example: 1.25 = 12 hr 25 min, .30 = 30 min, 1 = 1 hr

Query Request Interval: 45 min// <u>\<RET\></u> ( 45 min)

Query Limit Request: 10000 Rx's// <u>?</u>

This is the maximum number of Rx's that will be accepted during a query request.

Query Limit Request: 10000 Rx's// <u>\<RET\></u>

Days to Retain Release Summary: 10 days// <u>?</u>

This is the number of days of Release Acknowledgements that will be retained in the file system. Maximum number of days is 10, minimum number of days is 0.

Days to Retain Release Summary: 10 days// <u>\<RET\></u>

Select Operations Management Option: <u>\<RET\></u>*Archive CMOP Data* \[PSX ARCHIVE\]

> The Archive CMOP Data menu has been added, a sub-menu consists of the original archive options as listed below:

> *Archive Monthly CMOP Data*

> *Purge Archived CMOP Data*

> *Retrieve Archived CMOP Data*