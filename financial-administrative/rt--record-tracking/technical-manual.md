---
title: Record Tracking Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: RT
app_name: Record Tracking
section: FIN
app_status: active
pkg_ns: RT
patch_ver: 1
patch_id: RT*1
group_key: "RT:RT:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Orientation](#orientation) - [# Introduction](#introduction) - [# Functional Description](#functional-description) - [# Technical Overview](#technical-overview) - [Namespace Conventions](#namespace-conventions) - [Key Variables](#key-variables) - [Resource Requirements](#resource-requirements)
audience: 
keywords: 
  - record
  - records
  - tracking
  - table
  - contents
  - request
  - pull
  - routine
  - site
  - routines
page_count: 0
word_count: 7508
section_count: 23
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/30/09
revision_oldest: 3/30/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rttech.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rttech.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=53"
---

![](record-tracking-version-1-technical-manual/001.png)

Record Tracking V. 2.0Technical ManualNovember 1991

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/30/09

|          |                                       |                     |                      |
|----------|---------------------------------------|---------------------|----------------------|
| Date | Description (Patch \# if applic.) | Project Manager | Technical Writer |
| 3/30/09  | Reformatted Manual                    |                     | REDACTED             |

Table of Contents

# # Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Orientation](#orientation)
- [# Introduction](#introduction)
- [# Functional Description](#functional-description)
- [# Technical Overview](#technical-overview)
  - [Namespace Conventions](#namespace-conventions)
  - [Key Variables](#key-variables)
  - [Resource Requirements](#resource-requirements)
  - [External Relations](#external-relations)
  - [Internal Relations](#internal-relations)
  - [Integrity Checker](#integrity-checker)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
  - [TaskMan Considerations](#taskman-considerations)
  - [Bar Code Technology](#bar-code-technology)
- [Package Security](#package-security)
  - [Security Keys](#security-keys)
  - [Legal Requirements](#legal-requirements)
  - [FileMan Access Codes](#fileman-access-codes)
- [Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Compiled Template Routines](#compiled-template-routines)
  - [Compiled Cross-Reference Routines](#compiled-cross-reference-routines)
  - [Routines List with Descriptions](#routines-list-with-descriptions)
- [Files](#files)
  - [Main Globals and Files](#main-globals-and-files)
  - [Globals to Journal](#globals-to-journal)
  - [File Flow (Relationship between files)](#file-flow-relationship-between-files)
  - [File List](#file-list)
  - [Templates](#templates)
- [# Menu Diagram](#menu-diagram)
- [Site Configurable Features](#site-configurable-features)
- [Data Storage and Retention](#data-storage-and-retention)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
- [Installation Guide](#installation-guide)
- [Glossary](#glossary)
The Record Tracking Technical Manual has been divided into major sections for general clarity and simplification of the information being presented. This manual is intended to be a reference document. While the user is free to review the document from cover-to-cover, it is best used by selecting specific sections which contain the information sought for a particular need.
The Technical Overview Section contains the namespace conventions, key variables, resource requirements and any SACC exemptions/non-standard code. The Data Storage and Retention Section provides information on archiving and purging capabilities.
How To Use This Manual
The Record Tracking Technical Manual is provided in an Adobe Acrobat PDF (portable document format) file. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VistA Home Page, “Viewers” Directory.
Once you open the file, you may click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. You may print any or all pages of the file. Click on the “Print” icon and select the desired pages. Then click “OK”.

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The prompt availability of patient records is an essential ingredient in the delivery of quality medical care. Lack of access to vital patient history contained in these records may lead to life-threatening situations.

The VA Record Tracking system is a comprehensive software package, written to aid file activities in assuring optimum availability of these records to a broad range of users within and outside the facility. Functions which were previously done manually have been computerized, promoting greater efficiency, uniformity and accuracy. Demographic record information is now available on-line to a broad range of users, as well as a variety of reports which have been included to assist management in workload analysis and quality assurance.

The Record Tracking system uses VA FileMan, and integrates with the Radiology and MAS packages in performance of its functions. It has been designed such that it may be used in conjunction with bar code technology, further enhancing efficiency and accuracy.

This package was originally designed for use in tracking medical administration and/or radiology records. A great deal of flexibility has been built into the system so that it may be custom-tailored to meet the needs of practically any file activity. The VA Record Tracking package offers a complete system for the maintenance, control, and retirement of records.

# # Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Record Tracking Module has been created to aid file activities in the areas of maintaining and controlling patient records. However, this system offers a wide range of site configurable features and may be custom-tailored to meet practically any site's needs. Simultaneous installation of the Record Tracking package and the bar code label printers/readers is necessary in order to use this module to its fullest capacity; however, the package may be installed and running at those sites not yet equipped with the additional hardware and utilized at a reduced capacity.

The state-of-the art design of Record Tracking utilizes flat files throughout the package which construct a file structure that is easier to program, search, debug, and repair. Flat file structuring also enhances the package's interface with FileMan. Inclusion of purge routines for the Pull List, Requests, and Movement files in the initial release of Record Tracking attests to the manageable structure of this package.

Another feature of Record Tracking is the use of variable pointer data type fields. These variable pointers allow the value of a field to be taken from one or more files. A user with "laygo" access to any or all files may direct that access to, or acquire help for, any file by entering PREFIX.DATA to access a data type field or PREFIX.? for help. You may enter 'ORDER within the file definition to search files entries. All record requests go through FileMan and all edits are FileMan templates.

This is a comprehensive software package, providing for all aspects of records control and maintenance. There are six user menus and two site manager/application coordinator menus in support of this goal.

> TRANSACTION MENU

> REQUEST RECORDS MENU

> PULL LIST FUNCTIONS MENU

> RECORD INFORMATION MENU

> MANAGEMENT REPORTS MENU

> INACTIVATE RECORDS MENU

> SYSTEM DEFINITION MENU

> COMPUTER SITE MANAGER'S MENU

The Transaction Menu is basically dedicated to file room functions. The Request Records Menu supports requisitioning activities for individual records. The Pull List Functions Menu also supports record requisitioning activities; however, it provides the capability for an individual borrower to request multiple records at a time, thus creating a pull list. It interfaces with the Scheduling module, automatically creating pull lists for scheduled clinics. The Record Information Menu provides five record reports which may be displayed for specified patients. The Management Reports Menu provides ten reports which are useful in analyzing workload and identifying record control problems. The Inactivate Records Menu includes the options for record retirement tasks.

The System Definition and Computer Site Manager's Menus are provided for initialization and maintenance of the package and for defining site-specific parameters.

Two additional menus, Film Tracking Specific and MAS Specific Set-Up Menus, have been provided for users who routinely use both applications of Record Tracking (Radiology and Medical Administration) in their daily activities. For example, an MAS clinic clerk may need to request both Radiology and MAS records and view the record profiles of each. Ordinarily such a user would need to exit and re-enter Record Tracking in order to gain access to the other application. Assigning the user options from either of these menus will allow them to revert back and forth between applications without having to do this.

The functions within this system interact with one another affording greater control over records. For example, when a record is being checked into the file room the system will display a bulletin if pending requests exist for the record, if it has been flagged as missing, if loose filing exists, if the patient is currently an inpatient, or if it is being checked into a home file room other than its own. The user may elect to perform any necessary functions related to these bulletins without leaving the option he is working in.

# # Technical Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the Records Tracking package is RT.

## Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following variables are package-wide variables. Each time a file room menu is accessed these variables are "X" set in routine RTPSET. The local variable will be set in this routine to "MAS" or "RAD" depending on the current application. Each of these variables are subsequently killed in RTPSET upon leaving the menu. These variables are used extensively in the package to reduce global access overhead.

RTAPL

Contains application specific parameters, security keys, and defaults; located in the zero node of file 195.1

RTSYS

Contains application specific file room entry; located in the zero node of file 195.9

RTFR

Contains the overall parameter entry; located in the zero node of file 195.4

RTDIV

Division - institution pointer

> **NOTE:** The file room menus should not be nested.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPU TU's = <u>\# Patients Treated + OPT Visits</u>

400,000

Disk Space

Disk resource consumption is highly dependent upon the number of movements the site elects to keep on file before purging. A rough measure of disk consumption to place the package in an operational status would be 1 block per patient. For example, 50,000 patients would require approximately 50 megabytes.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record Tracking requires a minimum of FileMan v.18 and Kernel v.6.5.

Integration agreements between Record Tracking and Scheduling, Registration, and Radiology are on file in the DBA database on FORUM.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None of the Record Tracking package options have been designed to stand alone. Four variables are set upon entering the package and killed upon leaving which are used throughout all options.

## Integrity Checker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RTNTEG - generated by XTSUMBLD.

## SACC Exemptions/Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- RTAPL, RTFR, RTSYS, and RTDIV are package-wide variables.
- Request to do a kill of ^DD(195.9,0,"ACT") during pre-init.
- Request to allow the options "Print Labels for all Inpatients" and "Print Labels for all patients", which both print bar code labels, to be exempt from allowing the options to be queuable, as much manual manipulation is required during the printing.

## TaskMan Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RT SM-PURGE-AUTOMATIC option should be scheduled monthly via TaskMan after the purge parameters are set through the Purge Data option in the Computer Site Manager's Menu.

The RT SM-CLINIC-REQUEST option should be scheduled to run daily after 5pm. In the Record Tracking system Parameters file (#195.4), field 5 (BATCH RECORD,X-RAY REQUESTS) should be set to YES. Field 6 (BATCH REQUESTS CUTOFF) should be set to an appropriate number of days in the future to check clinic appointments. BATCH RECORD,X-RAY REQUESTS field should only be set to NO if you want future requests for records to be made through the TaskMan as appointments are made. Usually, this would just be for test purposes.

## Bar Code Technology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Technical Description*

Bar codes are comprised of a number of printed bars and intervening spaces. The widths and numbers of each are determined by the symbology used. Different symbologies exist for use by different applications. The specifications for the symbology prescribe the minimum width of the elements (both bars and spaces), the ratio of wide to narrow elements, printing tolerances (change in width due to printing process), the structure of the bar and space combinations depicting various characters, the bar/space combinations signifying beginning and end of message, and the clear area (quiet zone) before and after the bar code.

The bar code symbology used for Record Tracking is Code 39 (also known as Code 3 of 9, and 3 of 9 Code). Code 39 is used as the Health Industry Bar Code (HIBC) symbology. It is of variable length and used by most new applications.

Code 39 is an alphanumeric, bi-directional (can be read in either direction), self-checking code. Its data set consists of the digits 0-9, the alphabet in upper case letters, and 7 special characters (-,.,\$,/,+,% and space). Each character consists of 9 elements; 5 bars and 4 spaces. Three of the 9 elements are wide (Value 1), and six are narrow (Value 0). The \* is used for both start and stop characters.

Due to the strong self-checking factor of Code 39, a minimum number of substitution errors (whereby the data encoded in the symbol does not agree with the data read) can be anticipated. Using high quality scanning and printing equipment, you can expect 1 substitution error out of 3 million characters scanned. Generally, failure to read within the first few passes indicates a problem with the printed label, while substitution errors are more indicative of a reader problem. (The more passes needed to read a bar code, the higher the probability of error.)

*Hardware Connection*

Bar code readers may be connected using a variety of configurations. For Record Tracking it should be connected on-line between a host CPU and data terminal (CRT) via a standard RS-232C interface. Thus, the reader is "wedged" between the CPU and CRT.

*Encoded Message of Record Tracking Bar code Labels*

The encoded bar code message on record labels reflect the station number and the Record Tracking Record Number (separated by a slash). For informational purposes, social security numbers have not been used to identify records in Record Tracking as there is no way of uniquely identifying each of a patient's records; therefore, Record Tracking assigns a unique number to each record within it. That number, preceded by the station number, is encoded in the bar code message. For borrower labels, the message indicates the file number in which the borrower exists followed by the internal borrower number assigned by Record Tracking (separated by a slash). The request label message indicates the number of the request. Record Tracking uses a consecutive numbering system to assign a number to each request entered.

*Reading Bar code Labels*

The bar code reader converts the printed code into the equivalent of keystrokes. Generally, bar codes will be read by wanding a pen-like device over the bar code. Several factors contribute to proper scanning techniques.

> The reader should be held comfortably, as though it were a pen

> or pencil. It should be tilted slightly, perhaps 15 to 20

> degrees, perpendicular to the label.

> Scanning should be done at a constant speed using an arm

> motion, as though you were drawing a straight line through the

> center of the bar code. Scanning should begin and end in the

> quiet zone, which is the blank area before and after the bars.

> It may be accomplished in either direction.

> Only light pressure should be applied. Excessive pressure may

> damage the label and/or reader.

> Care should be taken not to drop the reader on the floor or

> table surface to prevent damage to the tip and internal optics.

> If it takes several passes to read different labels, dirt may

> have accumulated on the reader tip and cleaning is necessary.

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RT MAS-FR-STAFF

This key allows user to charge records to the MAS file room.

RT MAS-FR-SUPERVISOR

This key allows the MAS file room supervisor to cancel record requests, edit record requests, flag records as missing, remove the missing flag, and approve or disapprove the finding of a record by a user other than a supervisor. (The parameter allowing non-supervisors to find records must be set to do this.)

RT RAD-FR-STAFF

This key allows user to charge films to the Radiology file room.

RT RAD-FR-SUPERVISOR

This key has the same function in the Radiology application as the RT MAS-FR-SUPERVISOR security key has in the MAS application.

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known legal requirements associated with this package.

## FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security of the files associated with Record Tracking has been left as site configurable. Each site can determine the security on each file according to the needs of the various users. For example, a file such as the Reasons file, which is accessed infrequently and by only a select number of users, would probably be given a higher level of security than the Records file, which would be accessed frequently and by many users. Generally, the file security should correspond with the user's level of access to the package.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the following be mapped. Also map the routines generated by the compiled templates RTC\* and RTX\*.

RTB RTDPA\* RTINQ\* RTL1 RTPSET RTPSET1 RTQ\* RTRD RTRPT\* RTT\* RTUTL\*

It is strongly recommended that the following routine not be mapped: RTUTL5.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no general entry points in the package that can be called by other applications. Any applications wishing to interact with Record Tracking would need to negotiate a custom arrangement.

## Compiled Template Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Input Templates*

<u>FILE \#</u> <u>TEMPLATE NAME</u> <u>ROUTINES</u>

190 RT CHARGE ^RTCC\*

RT NEW RECORD ^RTCR\*

190.1 RT CHANGE REQUEST STATUS ^RTCS\*

RT REQUEST ^RTCU\*

190.3 RT MOVEMENT ^RTCM\*

194.2 RT PULL LIST ^RTCP\Print Templates*

<u>FILE \#</u> <u>TEMPLATE NAME</u> <u>ROUTINES</u>

190 RT HOME LOCATION ^RTCH\*

190.1 RT PENDING REQUESTS ^RTCX\*

190.2 RT MISSING ^RTCL\*

## Compiled Cross-Reference Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cross-reference templates have the namespace RTX\* and are as follows:

<u>FILE \#</u> <u>FILE NAME</u> <u>ROUTINES</u>

190 RECORDS RTXR\*

190.1 REQUESTED RECORDS RTXQ\*

190.3 RECORD MOVEMENT HISTORY RTXM\*

194.2 PULL LIST RTXP\*

195.9 BORROWERS/FILE AREAS RTXB\*

## Routines List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of routines for the Record Tracking system package, including a brief description of each function.

RT

Main driver for the Record Tracking (RT) package. Any option in the Record Tracking system can be accessed via his routine.

RTB

Entity lookup for variable pointer fields.

RTB1, RTB2

These routines provide assistance when choosing an entity.

RTDEL

This routine allows a record to be deleted if it is the only or last volume in a set. Any requests for the record, missing log entries, and all movement history log entries will also be deleted.

RTDPA

This routine will look up a selected record in the RECORDS file. If the record does not exist, then the routine provides for the creation of a new record.

RTDPA1

This routine creates a label for a record if the record does not have one already. If the record does not exist, this routine allows for the creation of a new record.

RTDPA2

This routine allows the user to see how many (if any) requests have been entered through the Records Tracking system for a given record. If no requests have been entered, the routine enables the creation of a new request.

RTDPA3, RTDPA32

These routines provide the ability to look up the identity of a particular record's borrower, or the number of records charged to a particular borrower if the borrower is still active and/or has not had privileges revoked.

RTDPA31

Screen logic for the BORROWERS/FILE AREAS file is contained in this routine.

RTIPRE

This routine is used in the pre-initialization process of the Record Tracking Package.

RTL

This routine runs the Label Function Menu.

RTL1, RTL2

These routines allow labels to be printed.

RTL3

This routine returns print field values for label format.

RTLDIV

This routine is used to print labels by division.

RTM

Record retirement options driver.

RTMAS

This routine is the driver for the MAS Specific Set-up Menu.

RTNQ

This routine runs the Record Information Menu.

RTNQ1

This routine traces the movement history of a record.

RTNQ2, RTNQ21

These routines provide all available information on any existing record or records. RTNQ21 provides specific record request information.

RTNQ3

This routine provides a listing of all transactions of a patient's record(s) for a given date range.

RTNQ4, RTNQ41

Expanded record inquiry including last admission, discharge.

RTNTEG

This routine is generated by the XTSUMBLD routine to calculate and store the total ASCII value of each routine in the package. This value can be used to check if routines have been altered and/or patched correctly.

RTP

This routine runs the Pull List Functions Menu.

RTP1

This routine runs the Designate Requests as 'Not Fillable', Cancel Request From Pull List, and Edit Pull List Comment options.

RTP2

This routine allows request selection in the Add Requests to Pull List option.

RTP3, RTP31

These routines run the Print Pull List(s) option.

RTP32

This routine provides a detailed non-fillable list of requested records.

RTP4, RTP41

These routines run the Charge Out Pull List Records option.

RTP40

This routine allows a pull list to be charged out to a holding area.

RTP5, RTP51

Multi-institution pull list print.

RTP6

This routine changes the names of pull lists when the corresponding hospital location name is edited.

RTPCAN

Allows all pull lists for a clinic to be cancelled.

RTPSET, RTPSET1

These routines allow options to set sign-on parameters such as applications and file rooms.

RTPURGE

This routine allows record movements, requests and pull lists to be purged by selectable limits.

RTQ

This routine runs most of the options under the Request Records Menu, including Request a Record, Edit a Request, Cancel a Request, Fill a Request, and Reprint a Request Notice.

RTQ1

This routine checks various precedents to make sure that the requested record is not flagged and that the borrower is authorized to request the record.

RTQ2

This routine provides a link to the Scheduling module of the MAS package. It allows pull lists and/or requests to be triggered from Scheduling when appointments are made or deleted.

RTQ3

This routine provides a link to the Admission, Discharge, Transfer module of the MAS package, enabling records to be requested from there.

RTQ4, RTQ41

These routines help in running the Fill a Request and Edit a Request options.

RTQ5

This routine allows a radiology record to be designated as a wet reading.

RTRAD

This routine is the driver for radiology-specific menu options.

RTRD

This is a utility routine for reading screen input. It provides a single interface for prompts, time outs, and "^" escape as per programming standards.

RTRPT, RTRPT3

These routines drive the Management Reports menu.

RTRPT1

This routine runs the Requests Pending for a Borrower option.

RTRPT2

This routine prints a report indicating the records that have been charged out by a borrower.

RTSM, RTSM3, RTSM4

These routines run the Computer Site Manager's Menu.

RTSM1

This routine is used for record initialization, sort global creation, and deletion.

RTSM2

This routine is used for input of record initialization parameters.

RTSM5

Checks one clinic for requests and initializes a corresponding pull list.

RTSM6, RTSM61

Runs option RT SM-CLINIC-REQUEST which allows the Automatic Clinic Request Initialization option to run via TaskMan if the proper parameters are set.

RTSM7

This routine runs with RTSM6 and checks for terminated users.

RTSM8, RTSM81

These routines generate record retirement pull lists.

RTSYS

This routine runs the System Definition Menu.

RTT

This routine is the driver for the Transaction Menu.

RTT1

This allows a record to be flagged as missing and acts as a utility for the Transaction Menu.

RTT11

This routine allows for multiple volume creation.

RTT12

This routine transfers requests to a selected record.

RTT2

This routine aids RTT in running the Charge-Out Records and Missing Records List options.

RTT21

Logic for pending check-in cutoff.

RTT3, RTT4

These are record transaction selection utilities.

RTTR

Transfer Records Menu driver.

RTTR1, RTTR11

These routines generate the request record transfer bulletin.

RTTR2

This routine generates the notice of transfer bulletin.

RTUTL

Utility for record type selection, institution lookup, queueing, device handling, and date selection.

RTUTL1

Utility for setting record movement entries, multiple processing lists, and displaying entities.

RTUTL2

Utility for print and display functions.

RTUTL3

Utility for data lookup functions.

RTUTL4

Utility for request displays.

RTUTL5

Utility used to recompile templates for the package. This routine should not be mapped.

RTUTL6

This routine generates the request cancellation bulletin.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Main Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The globals used in the Records Tracking package are ^RT, ^RTV, and ^DIC. ^DIC is used to store all non-volatile records. The main files associated with the Records Tracking package are the Records file and the Requested Records file.

## Globals to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each of these three dynamic globals - ^RT ^RTV ^DIC - should be journaled.

## File Flow (Relationship between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FILE FILE

<u>NUMBER</u> <u>NAME</u> <u>GLOBAL</u>

190 RECORDS ^RT(

190.1 REQUESTED RECORDS ^RTV(190.1,

190.2 MISSING RECORDS ^RTV(190.2,

190.3 RECORD MOVEMENT HISTORY ^RTV(190.3,

194.2 PULL LIST ^RTV(194.2,

194.4\* LABEL FORMAT ^DIC(194.4,

194.5\* LABEL PRINT FIELD ^DIC(194.5,

195.1\* RECORD TRACKING APPLICATION ^DIC(195.1,

195.2\* RECORD TYPES ^DIC(195.2,

195.3\* RECORD MOVEMENT TYPES ^DIC(195.3,

195.4\* RECORD TRACKING SYSTEM PARAMETERS ^DIC(195.4,

195.6\* REASONS ^DIC(195.6,

195.9 BORROWERS/FILE AREAS ^RTV(195.9,

\* File comes with data which will overwrite existing data, if so specified

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Input Templates*

<u>FILE \#</u> <u>TEMPLATE</u> <u>DESCRIPTION</u>

190 RT CHARGE Input data for a charge

RT NEW RECORD Input data for record creation

190.1 RT CHANGE REQUEST STATUS Change request status

RT EDIT REQUEST Change time of request

RT REQUEST Input data for request

190.2 RT FOUND Input data when record

declared found

RT MISSING Input data when record

declared missing

190.3 RT MOVEMENT Input data for a movement

194.2 RT CHANGE PULL LIST Change pull list status

STATUS

RT PULL LIST Input data for pull list

194.4 RT LABEL EDIT Change label format

194.5 RT PRINT FIELD SETUP Change label print field data

195.1 RT APPL SET-UP Input data for application parameters

RT APPL SET-UP Change application parameters

(SITE MGR)

195.2 RT PURGE PROFILE Edit parameters for purge

RT RETIREMENT PROFILE Edit parameters for record retire

RT TYPE SET-UP Edit record type parameters

<u>FILE \#</u> <u>TEMPLATE</u> <u>DESCRIPTION</u>

195.3 RT MOVEMENT SET-UP Edit type of movement parameters

195.4 RT OVERALL PARAMETERS Edit overall parameters

195.6 RT REASON SET-UP Edit reasons entries

195.9 RT ADMIT SET-UP Edit MAS parameters

(SITE MGR)

RT BORROWER SET-UP Edit borrower information

RT FILE ROOM SET-UP Edit file room parameters

RT FILE ROOM SET-UP Edit file room devices

(SITE MGR)

RT FILE ROOM/REMOTE Edit remote institution parameters

RT QUICK UPDATE Edit borrower information on charge out

*Print Templates*

<u>FILE \#</u> <u>TEMPLATE</u> <u>DESCRIPTION</u>

190 RT HOME LOCATION Prints record information

for loose filing, charged

records and overdue records

190.1 RT PENDING REQUESTS Prints pending requests

RT TIME STUDY Prints ad hoc statistics

190.2 RT MISSING Prints missing records list

195.2 RT PURGE PROFILE Displays record purge parameters

RT RETIREMENT PROFILE Displays record retirement parameters

195.9 RT FILE ROOM/REMOTE Displays remote institution parameters

*Sort Templates*

<u>FILE \#</u> <u>TEMPLATE</u> <u>DESCRIPTION</u>

190 RT CHARGED BY HOME Management report for charged

BY BOR records by home location,

borrower

RT CHARGED BY HOME Management report for charged

BY NAME records by home location, name

RT CHARGED BY HOME Management report for charged

BY TD records by home location,

terminal digit

RT HOME LIST BY BOR Management report for records

\- sort by home location,

borrower

RT HOME LIST BY NAME Management report for records

\- sort by home location, name

RT HOME LIST BY TD Management report for records

\- sort by home location,

terminal digit

RT LOOSE FILING Management report - sort

records with loose filing

RT OVER BY DIV BY BOR Management overdue records

report - sort by division and

borrower

RT OVER BY DIV BY NAME Management overdue records

report - sort by division and

name

RT OVER BY DIV BY TD Management overdue records

report - sort by division and

terminal digit

RT OVER BY HOME BY BOR Management overdue records

report - sort by home location

and borrower

RT OVER BY HOME BY NAME Management overdue records

report - sort by home location

and name

RT OVER BY HOME BY TD Management overdue records

report - sort by home location

and terminal digit

<u>FILE \#</u> <u>TEMPLATE</u> <u>DESCRIPTION</u>

190.1 RT PENDING REQUESTS Management pending request report -

sort by pending requests

RT TIME STUDY Management ad hoc statistics -

sort by date/time requested,

pull list, status, name, type

of record, volume

190.2 RT MISSING Management report for missing records

194.4 RT FORMATS Sort label formats by application

195.2 RT PURGE PROFILE Display record purge parameters -

sort by application, name

RT RETIREMENT PROFILE Display record retirement parameters -

sort by application, name

195.9 RT FILE ROOM/REMOTE Display remote institution -

sort by domain, name

# # Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record Tracking Total System Menu (RT OVERALL)

\|

----1 Transaction Menu -------------------------------CHG Charge-Out Records

\[RT TRANS-MENU\] \[RT TRANS-CHARGE-

\| OUT\]

\|

\|-------------------------------------------CHK Check-in Records

\| \[RT TRANS-CHECK-IN\]

\|

\|-------------------------------------------BAR Create a Label/

\| Record/Volume

\| \[RT TRANS-CREATE\]

\|

\|--------------------------------------------PT Patient Charge-Out

\| \[RT TRANS-PATIENT\]

\|

\|--------------------------------------------UP Update Record's

\| Attributes \[RT

\| TRANS-UPDATE\]

\|

\|---------------------------------------------- Delete a Record

\| \[RT TRANS-DELETE\]

\|

\|---------------------------------------------- Flag Record as

\| Missing \[RT

\| TRANS-MISSING\]

\|

\|---------------------------------------------- Inactivate/Reacti-

\| vate Records

\| \[RT TRANS-

\| INACTIVATE\]

\|

\|---------------------------------------------- Move Requests to

\| Last Volume \[RT

\| TRANS-MOVE-REQ-

\| LAST-VOL\]

\|

\|---------------------------------------------- Multiple New

\| Volume Creation

\| \[RT TRANS-NEW-VOL-

\| MULTI\]

\|

\|---------------------------------------------- New Volume

\| Creation \[RT

\| TRANS-NEW-VOL\]

\|

\|---------------------------------------------- Re-Charge

\| Records \[RT

\| TRANS-RE-CHARGE\]

\|-------------------- Transfer Records -------- Create Record/

Menu \[RT Volume for

TRANS-TRANSFER\] transferred Record

\| \[RT TRANSFER-CREATE\]

\|

\|-------------------- Request a Transfer

\| from another

\| Institution \[RT

\| TRANSFER-REQUEST\]

\|

\|-------------------- Return Transferred

\| Record \[RT

\| TRANSFER-BACK\]

\|

\|-------------------- Transfer Record

to another

Institution \[RT

TRANSFER-OUT\]

----2 Request Records Menu ------------------------------ Cancel a Request

\[RT RTQ-MENU\] \[RT RTQ-CANCEL\]

\|

\|---------------------------------------------- Designate Requests

\| as 'Not Fillable'

\| \[RT PULL-NOT

\| FILLABLE\]

\|

\|---------------------------------------------- Display Request

\| \[RT RTQ-DISPLAY\]

\|

\|---------------------------------------------- Edit a Request

\| \[RT RTQ-EDIT\]

\|

\|---------------------------------------------- Fill a Request

\| \[RT RTQ-FILL\]

\|

\|---------------------------------------------- Reprint a

\| Request Notice

\| \[RT RTQ-REPRINT\]

\|

\|---------------------------------------------- Request a Record

\[RT RTQ-REQUEST-REC\]

----3 Pull List Functions Menu -------------------------1 Create a Pull List

\[RT PULL-MENU\] \[RT PULL-CREATE\]

\|

\|---------------------------------------------2 Add Requests to

\| Pull List \[RT

\| PULL-ADD\]

\|

\|---------------------------------------------3 Charge Out Pull

\| List Records \[RT

\| PULL-CHARGE-OUT\]

\|

\|---------------------------------------------4 Pull List Date

\| Change \[RT

\| PULL-CHANGE-DATE\]

\|---------------------------------------------5 Entire Pull List

\| Cancellation \[RT

\| PULL-CANCEL-PULL

\| -LIST\]

\|

\|---------------------------------------------6 Cancel Request

\| from Pull List

\| \[RT PULL-CANCEL-

\| REQUEST\]

\|

\|---------------------------------------------7 Designate Requests

\| as 'Not Fillable'

\| \[RT PULL-NOT

\| FILLABLE\]

\|

\|---------------------------------------------8 Edit Pull List

\| Comment \[RT

\| PULL-COMMENT\]

\|

\|---------------------------------------------9 Print Pull List(s)

\| \[RT PULL-LIST-PRINT\]

\|

\|--------------------------------------------10 Special Multi-

\| Institution Prints

\| \[RT PULL-MULTI-

\| INSTITUTION\]

\|

\|--------------------------------------------11 Entire Pull List

Cancellation (all

dates) \[RT PULL-

CANCEL-PULL-ALL\]

----4 Record Information Menu --------------------------- Combination Data

\[RT INQ-MENU\] Trace \[RT INQ-COMBO-

TRACE\]

\|

\|---------------------------------------------- Expanded Record

\| Inquiry \[RT

\| INQ-MEDIUM\]

\|

\|---------------------------------------------- Record Inquiry

\| \[RT INQ-INQUIRY\]

\|

\|---------------------------------------------- Short Record Inquiry

\| \[RT INQ-SHORT\]

\|

\|---------------------------------------------- Trace Movement

History \[RT

INQ-TRACE\]

----5 Management ---------------------------------------- Ad hoc Request

Reports Menu Response Statistics

\[RT RPT-MENU\] \[RT RPT-REQUEST-

\| TIME\]

\|

\|---------------------------------------------- Charged Records

\| By Home Location

\| \[RT RPT-HOME-LIST\]

\|

\|---------------------------------------------- Inpatient Record

\| Location List

\| \[RT RPT-INPATIENT\]

\|

\|---------------------------------------------- Loose Filing Report

\| \[RT RPT-LOOSE\]

\|

\|---------------------------------------------- Missing Records List

\| \[RT RPT-MISSING\]

\|

\|---------------------------------------------- Overdue Records List

\| \[RT RPT-OVERDUE\]

\|

\|---------------------------------------------- Pending Request List

\| \[RT RPT-PENDING-

\| REQUEST

\|

\|---------------------------------------------- Records Charged

\| to a Borrower

\| \[RT RPT-BORROWERS\]

\|

\|---------------------------------------------- Requests Pending

\| for a Borrower

\| \[RT RPT-REQUEST-BY-

\| BORROWER\]

\|

\|---------------------------------------------- Retrieval Rate

Statistics \[RT

RPT-RETRIEVAL STATS\]

----6 System Definition Menu ---------------------------1 Application Set-up

\[RT SYS-MENU\] \[RT SYS-APPLICATION\]

\|

\|---------------------------------------------2 File Room Set-up

\| \[RT SYS-FILE ROOM\]

\|

\|---------------------------------------------3 Type of Record

\| Set-up \[RT

\| SYS-RECORD TYPE\]

\|

\|---------------------------------------------4 Reasons File Set-up

\| \[RT SYS-REASONS\]

\|

\|-------------------5 Label Functions --------1 Label Formatter

\| Menu \[RT \[RT LBL-FORMATTER\]

\| SYS-LABELS\]

\| \|

\| \|-------------------2 Test Label Format

\| \[RT LBL-TEST\]

\|---------------------------------------------6 Borrower Set-up

\| \[RT SYS-INDIVD-

\| BORROWERS\]

\|

\|---------------------------------------------7 Print Borrower

\| Barcode \[RT

\| SYS-PRINT-BOR\]

\|

\|---------------------------------------------8 Movement Type Set-up

\[RT SYS-MOVEMENT\]

----7 Inactivate ---------------------------------------1 Generate Record

Records Menu \[RT Retirement Pull

INACT-MENU\] Lists \[RT

\| INACT-PULL-CREATE\]

\|

\|---------------------------------------------2 Print Record

\| Retirement Pull

\| list \[RT

\| INACT-PULL-PRINT\]

\|

\|---------------------------------------------3 Designate

\| Retirement Requests

\| as 'Not Fillable'

\| \[RT INACT-PULL-NOT

\| FILLABLE\]

\|

\|---------------------------------------------4 Delete a Record

\| \[RT TRANS-DELETE\]

\|

\|---------------------------------------------5 Create a Label/

\| Record/Volume

\| \[RT TRANS-CREATE\]

\|

\|---------------------------------------------6 Charge Out/Transfer

\| Retirement Pull

\| Lists \[RT

\| INACT-PULL-CHARGE\]

\|

\|---------------------------------------------- Inactivate/Reacti-

\| vate Records \[RT

\| TRANS-INACTIVATE\]

\|

\|-------------------- Pull List Functions Menu

\[RT PULL-MENU\]

----- Computer Site ------------------------------------- Admitting Area Set-

Manager's Menu up (Site Mgr)

\[RT SM-MENU\] \[RT SM-ADMITTING\]

\|

\|---------------------------------------------- Application Set-up

\| (Site Mgr) \[RT

\| SM-APPL\]

\|

\|---------------------------------------------- File Room Set-up

\| (Site Mgr) \[RT

\| SM-FILE-ROOM\]

\|

\|---------------------------------------------- File Room/Remote

\| Set-up (Site Mgr)

\| \[RT SM-FILE-REMOTE\]

\|

\|---------------------------------------------- Imaging Area Set-up

\| (Site Mgr) \[RT

\| SM-REG-AREA\]

\|

\|-------------------- Initialization ---------- Barcode Labels for

\| Menu \[RT All Patients

\| SM-REC-MENU\] \[RT SM-REC-LABELS\]

\| \|

\| \|-------------------- Borrower

\| \| Initialization \[RT

\| \| SM-REC-BORROWERS\]

\| \|

\| \|-------------------- Clinic Request

\| \| Initialization

\| \| \[RT SM-REC-CLINIC-

\| \| REQUEST\]

\| \|

\| \|-------------------- Compile Terminal

\| \| Digit Sort Global

\| \| \[RT SM-REC-COMPILE-

\| \| TERM-DIGIT\]

\| \|

\| \|-------------------- Delete Terminal

\| \| Digit Sort Global

\| \| \[RT SM-REC-DELETE-

\| \| TERM-DIGIT\]

\| \|

\| \|-------------------- Initialize Records

\| \| (NO LABELS) \[RT

\| \| SM-REC-INIT\]

\| \|

\| \|-------------------- Inpatient Barcode

\| \| Labels Only \[RT

\| \| SM-REC-IN-PT\]

\| \|

\| \|-------------------- Single Clinic

\| Request

\| Initialization

\| \[RT SM-REC-1CLINIC-

\| REQUEST\]

\|---------------------------------------------- Purge Data \[RT

\| SM-PURGE-DATA\]

\|

\|---------------------------------------------- Re-Compile Templates

\| \[RT SM-RECOMP\]

\|

\|---------------------------------------------- Record Tracking

System Overall

Parameters \[RT

SM-OVERALL\]

----- Film Tracking Specific Menu ----------------------- Imaging Area Set-up

\[RT RAD-MENU\] \[RT RAD-REG-AREA\]

\|

\|---------------------------------------------- Jacket Profile \[RT

\| RAD-JACKET-PROFILE\]

\|

\|---------------------------------------------- Request Film Jackets

\| \[RT RAD-JACKET-REQUEST\]

----- MAS Specific Set-up Menu ----------------------RECH Re-charge a Chart

\[RT MAS-MENU\] \[RT MAS-RE-CHARGE\]

\|

\|------------------------------------------RTCR Chart Request \[RT

\| MAS-CHART-REQUEST\]

\|

\|---------------------------------------------- Admitting Area Chart

\| Request \[RT MAS-

\| ADMIT-CHART-REQUEST\]

\|

\|---------------------------------------------- Admitting Area Set-

\| up \[RT MAS-

\| ADMITTING\]

\|

\|---------------------------------------------- Create MAS Labels/

\| Records/Volumes \[RT

\| MAS-LABEL-PRINT\]

\|

\|---------------------------------------------- Fill Next Clinic

\| Request \[RT

\| MAS-FILL-NEXT\]

\|

\|---------------------------------------------- Profile of Charts

\[RT MAS-CHART-

PROFILE\]

# Site Configurable Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Records Tracking module has been designed so that it can be used in various applications; thus, there are many parameters associated with this package that can be set according to each site's specific needs. The System Definition menu and the Computer Site Manager's menu can each be used to set these different parameters. Certain fields of some of the files associated with the Records Tracking package may be affected by this. Included among these files are the Reasons file (195.6) , the Record Tracking System Parameters file (195.4), the Record Movement Types file (195.3), the Record Types file (195.2), the Record Tracking Application file (195.1), the Label Format file (194.4), and the Borrowers/File Areas file (195.9). The task of setting these parameters is generally performed at the time of initialization of the package, but the parameters can be changed at virtually any time after they have been set.

Record Tracking has a basic generic design and can be used to track almost any entity. This is due to the use of the variable pointer data type in the RECORDS file (190) and the BORROWERS/FILE AREAS file (195.9). An application can be defined using a different variable pointer for the RECORDS file to point to another entity like a "books" or "equipment" file. Additional BORROWERS file variable pointers may also be added. It is recommended the additional applications should NOT be added in the production Record Tracking environment with Medical Administration and Radiology applications.

Bar code labels come with a previously defined format. It is possible to change this format or to create an entirely new format to meet site specific needs; however, it is strongly recommended that existing label formats be left as they are. If the site finds it necessary to change or create label formats, then the new labels should be created. New label formats can be created through the Label Functions Menu. Specific instructions have been included in the Record Tracking User Manual.

Additional label print fields entries may be added to File \#194.5. To add the appropriate M code to the MUMPS CODE TO SET VARIABLE field (#100) requires programmer knowledge. Print fields are limited to fields in Record Tracking files or files pointed to by Record Tracking fields.

# Data Storage and Retention

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purging

The Record Tracking package allows for purging of pull list, record request, and movement log data. This is accomplished through the Purge Data option, Computer Site Manager's Menu. Purges are done by record type based on the specifications set up in the Type of Record Set-up option, System Definition Menu.

Archiving

There are currently no archiving capabilities within the Record Tracking package.

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure Record Tracking technical documentation. On-line technical documentation pertaining to the Record Tracking software, in addition to that which is located in the help prompts and on the help screens which are found throughout the Record Tracking package, may be generated through utilization of several KERNEL options. These include but are not limited to: %INDEX, Menu Manager Inquire to OPTION File and Print OPTIONS file and VA FileManager List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the DHCP Kernel Reference Manual.

%INDEX

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to DHCP Programming Standards. The %INDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references and external references. By running %INDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from DHCP Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run %INDEX for the Record Tracking package, specify the following namespaces at the 'routine(s) ?\>' prompt: RT\*.

Record Tracking initialization routines which reside in the UCI in which %INDEX is being run, as well as local routines found within the Record Tracking namespace, should be omitted at the 'routine(s) ?\>' prompt. To omit routines from selection, preface the namespace with a minus sign (-). Use an apostrophe (') to accomplish this in ISM. For Record Tracking, omit the following: RTC\*, RTX\*, RTI\*.

INQUIRE TO OPTION FILE

This Menu Manager option provides the following information about a specified option(s): option name, menu text, option description, type of option and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about Record Tracking options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the Record Tracking package is RT.

PRINT OPTIONS FILE

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of Record Tracking options, the following option namespace should be specified: RT.

LIST FILE ATTRIBUTES

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates and sort templates.

For a comprehensive listing of Record Tracking files, please refer to the File Section of this manual.

# Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and initialization instructions have been included with software distribution of the Record Tracking package. All RTINI\* routines are associated with the Pre- and Post-Initialization process.

Use the following chart as your basic guide when initially installing Record Tracking. It lists all necessary steps in chronological order, along with the appropriate menu/option used. Since many of the steps cannot be accomplished without those preceding it already being completed, it is important that these steps be performed in the order listed. The chart also indicates who generally is responsible for each function. You may wish to keep it handy during installation.

Unless otherwise specified, each of the functions listed must be performed for each application - if your site will be tracking both Radiology and Medical records, these functions must be performed twice. You will notice that Steps 13 and 14 each contain two entries since each entry refers to a different application.

<u>RESPONSIBILITY</u> <u>STEP</u> <u>FUNCTION</u> <u>MENU</u> <u>OPTION</u>

SITE MANAGER 1 Initialization Process Installation Guide which accompanied

tape

2 Recompile Templates Computer Site Re-Compile

Manager's Menu Templates

\*APPLICATION 3 Enter file room(s) System Definition File Room Set-up

COORDINATOR/ and associated Menu

SITE MANAGER parameters

APPLICATION 4 Set up barcode label System Definition Label Functions Menu

COORDINATOR formats to be used Menu Label Formatter

5 Define Record Types System Definition Type of Record

to be used Menu Set-up

6 Define application- System Definition Application Set-up

specific parameters Menu

SITE MANAGER 7 Initialize Records Computer Site Initialization Menu

Manager's Menu Initialize Records

(NO LABELS)

8 Compile Sort Global Computer Site Initialization Menu

Manager's Menu Compile Terminal

Digit Sort Global

<u>RESPONSIBILITY</u> <u>STEP</u> <u>FUNCTION</u> <u>MENU</u> <u>OPTION</u>

9 Print Record Barcode Computer Site Initialization Menu

Labels Manager's Menu Barcode Labels for

All Patients

10 Initialize Borrowers Computer Site Initialization Menu

Manager's Menu Borrower

Initialization

APPLICATION 11 Specify reasons to be System Definition Reasons File Set-up

COORDINATOR used in association Menu

with finding missing

records and cancellation

of requests

12 Define parameters for System Definition Borrower Set-up

individual borrowers Menu

(MAS 13 Enter Admitting MAS Specific Admitting Area

APPLICATION Area(s) and Set-up Menu Set-up

ONLY) associated parameters

(RADIOLOGY 13 Enter Imaging Area(s) Film Tracking Imaging Area

APPLICATION and associated Specific Menu Set-up

ONLY) parameters

SITE MANAGER

(MAS 14 Define default Computer Site Admitting Area Set-up

APPLICATION device(s) for Manager's Menu (Site Mgr)

ONLY) Admitting Area(s)

(RADIOLOGY 14 Define default Computer Site Imaging Area Set-up

APPLICATION device(s) for Manager's Menu (Site Mgr)

ONLY) Imaging Area(s)

15 Define system-wide Computer Site Application Set-up

application parameters Manager's Menu (Site Mgr)

16 Define default Computer Site File Room Set-up

device(s) and Manager's Menu (Site Mgr)

Security Keys for

file room(s)

17 Define Overall Computer Site Record Tracking

System Parameters Manager's Menu System Overall

Parameters

\*NOTE: The first file room must be defined by the Site Manager using the RT OVERALL Menu. Subsequent file rooms may be defined using the RT MAS/RAD SUPER Menu.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

bar code A label consisting of a number of printed bars and
label intervening spaces set up such that it is recognized
as that of a specific entity when read by a bar code
reader. Used to identify records, borrowers, and
requests in Record Tracking.
borrower A location, entity, or individual to whom records
are loaned. Within Record Tracking, this may be a
physician, employee, clinic, ward, hospital location,
other VA facility, or patient.
home A record's place of residence when it is not being
location borrowed; usually the file room.
movement The term relates to the various actions which may
type be performed on a record; charging out,
checking in, etc.
pull list A list of record requests needed at the same date/
time by a specific borrower.
record This term will generally relate to the patient's
medical record, administrative record, or radiology
record. Since Record Tracking may be applied to a
variety of tracking activities (such as a library),
it could also apply to the item or entity which is
tracked.
record Also known as the Record Identifier Number. This
number is a sequential number assigned to each record
within Record Tracking upon its creation. It is
unique to the record. The record may be accessed
by entering this number at any "Select Record"
prompt.
request The act of asking for a specific record. A request
label is generated indicating the record, time
needed and requestor, along with other pertinent
information. This label also contains a bar code
which may be wanded to fill the request and
charge it to the requestor.
retirement The retirement status indicates whether a record
status may or may not be retired from the file room after
an allotted period of inactivity. There are three
retirement statuses: OK TO RETIRE, TUMOR
REGISTRY, and TEACHING. Records are
considered OK TO RETIRE unless otherwise
specified through the Update Record's Attributes
