---
title: Record Tracking Version 1 User Manual
doc_type: UM
doc_label: User Manual
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
description: The Transaction Menu is the focal point of the Record Tracking package. Generally, it is dedicated to file room activities although select options may be given to other users on an as- needed basis. It supports the following functions.
audience: 
keywords: 
  - record
  - records
  - request
  - pull
  - borrower
  - contents
  - table
  - requests
  - patient
  - prompt
page_count: 0
word_count: 37051
section_count: 92
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2018
revision_count: 2
revision_newest: 05/03/2018
revision_oldest: 3/30/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rtuser1.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Record_Tracking/rtuser1.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=53"
---

![](record-tracking-version-1-user-manual/001.png)

Record Tracking V. 2.0User ManualNovember 1991(Revised May 2018)

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 3/30/09

|            |                                                                                                                                                                                                     |                                                             |                     |                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|---------------------|----------------------|
| Date   | Description (Patch \# if applic.)                                                                                                                                                               | Page                                                    | Project Manager | Technical Writer |
| 05/03/2018 | Patch RT\*2.0\*47 – Displays the last four digits of SSN when using the "Requests Pending for a Borrower" option, and changes the default response to the "ISSUE REQUEST FOR RECORDS" prompt to NO. | [<u>68</u>](#RT_2_47_SSN), [<u>160</u>](#RT_2_47_Def_Value) | REDACTED            | REDACTED             |
| 3/30/09    | Reformatted Manual                                                                                                                                                                                  | All                                                         |                     | REDACTED             |

Table of Contents

# # Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Orientation](#orientation)
- [# Introduction](#introduction)
- [# Functional Description](#functional-description)
- [# Package Management](#package-management)
- [Implementation Guide](#implementation-guide)
- [Transaction Menu](#transaction-menu)
  - [Overview](#overview)
  - [Charge-Out Records](#charge-out-records)
  - [Check-in Records](#check-in-records)
  - [Create a Label/Record/Volume](#create-a-labelrecordvolume)
  - [Patient Charge Out](#patient-charge-out)
  - [Update Record’s Attributes](#update-records-attributes)
  - [Delete a Record](#delete-a-record)
  - [Flag Record as Missing](#flag-record-as-missing)
  - [Inactivate/Reactivate Records](#inactivatereactivate-records)
  - [Move Requests to Last Volume](#move-requests-to-last-volume)
  - [Multiple New Volume Creation](#multiple-new-volume-creation)
  - [New Volume Creation](#new-volume-creation)
  - [Re-Charge Records](#re-charge-records)
  - [Transfer Records Menu](#transfer-records-menu)
    - [Create Record/Volume for transferred Record](#create-recordvolume-for-transferred-record)
    - [Request a Transfer from another Institution](#request-a-transfer-from-another-institution)
    - [Return Transferred Record](#return-transferred-record)
    - [Transfer Record to another Institution](#transfer-record-to-another-institution)
- [Request Records Menu](#request-records-menu)
  - [Overview](#overview-1)
  - [Cancel a Request](#cancel-a-request)
  - [Designate Requests As 'Not Fillable'](#designate-requests-as-not-fillable)
  - [Display Request](#display-request)
  - [Edit a Request](#edit-a-request)
  - [Fill a Request](#fill-a-request)
  - [Reprint a Request Notice](#reprint-a-request-notice)
  - [Request a Record](#request-a-record)
- [Pull List Functions Menu](#pull-list-functions-menu)
  - [Overview](#overview-2)
  - [Create a Pull List](#create-a-pull-list)
  - [Add Requests to Pull List](#add-requests-to-pull-list)
  - [Charge Out Pull List Records](#charge-out-pull-list-records)
  - [Pull List Date Change](#pull-list-date-change)
  - [Entire Pull List Cancellation](#entire-pull-list-cancellation)
  - [Cancel Request from Pull List](#cancel-request-from-pull-list)
  - [Designate Requests as ‘Not Fillable’](#designate-requests-as-not-fillable-1)
  - [Edit Pull List Comment](#edit-pull-list-comment)
  - [Print Pull List(s)](#print-pull-lists)
  - [Special Multi-Institution Prints](#special-multi-institution-prints)
  - [Entire Pull List Cancellation (all dates)](#entire-pull-list-cancellation-all-dates)
- [# Record Information Menu](#record-information-menu)
  - [Overview](#overview-3)
  - [Combination Data Trace](#combination-data-trace)
  - [Expanded Record Inquiry](#expanded-record-inquiry)
  - [Record Inquiry](#record-inquiry)
  - [Short Record Inquiry](#short-record-inquiry)
  - [Trace Movement History](#trace-movement-history)
- [Management Reports Menu](#management-reports-menu)
  - [Overview](#overview-4)
  - [Ad hoc Request Response Statistics](#ad-hoc-request-response-statistics)
  - [Charged Records by Home Location](#charged-records-by-home-location)
  - [Inpatient Record Location List](#inpatient-record-location-list)
  - [Loose Filing Report](#loose-filing-report)
  - [Missing Records List](#missing-records-list)
  - [Overdue Records List](#overdue-records-list)
  - [Pending Request List](#pending-request-list)
  - [Records Charged to a Borrower](#records-charged-to-a-borrower)
  - [Requests Pending for a Borrower](#requests-pending-for-a-borrower)
  - [Retrieval Rate Statistics](#retrieval-rate-statistics)
- [System Definition Menu](#system-definition-menu)
  - [Overview](#overview-5)
  - [Application Set-up](#application-set-up)
  - [File Room Set-up](#file-room-set-up)
  - [Type of Record Set-up](#type-of-record-set-up)
  - [Reasons File Set-up](#reasons-file-set-up)
  - [Label Functions Menu](#label-functions-menu)
    - [Label Formatter](#label-formatter)
    - [Test Label Formatter](#test-label-formatter)
  - [Borrower Set-up](#borrower-set-up)
  - [Print Borrower Barcode](#print-borrower-barcode)
  - [Movement Type Set-up](#movement-type-set-up)
- [Inactivate Records Menu](#inactivate-records-menu)
  - [Overview](#overview-6)
  - [Generate Record Retirement Pull Lists](#generate-record-retirement-pull-lists)
  - [Print Record Retirement Pull List](#print-record-retirement-pull-list)
  - [Designate Retirement Requests as ‘Not Fillable”](#designate-retirement-requests-as-not-fillable)
  - [Delete a Record](#delete-a-record-1)
  - [Create a Label/Record/Volume](#create-a-labelrecordvolume-1)
  - [Charge Out/Transfer Retirement Pull Lists](#charge-outtransfer-retirement-pull-lists)
  - [Inactivate/Reactivate Records](#inactivatereactivate-records-1)
  - [Pull List Functions Menu](#pull-list-functions-menu-1)
- [Computer Site Manager’s Menu](#computer-site-managers-menu)
  - [Overview](#overview-7)
  - [Admitting Area Set-up (Site Mgr)](#admitting-area-set-up-site-mgr)
  - [Application Set-up (Site Mgr)](#application-set-up-site-mgr)
  - [File Room Set-up (Site Mgr)](#file-room-set-up-site-mgr)
  - [File Room/Remote Set-up (Site Mgr)](#file-roomremote-set-up-site-mgr)
  - [Imaging Area Set-up (Site Mgr)](#imaging-area-set-up-site-mgr)
  - [Initialization Menu](#initialization-menu)
    - [Barcode Labels for All Patients](#barcode-labels-for-all-patients)
    - [Borrower Initialization](#borrower-initialization)
    - [Clinic Request Initialization](#clinic-request-initialization)
    - [Compile Terminal Digit Sort Global](#compile-terminal-digit-sort-global)
    - [Delete Terminal Digit Sort Global](#delete-terminal-digit-sort-global)
    - [Initialize Records (NO LABELS)](#initialize-records-no-labels)
    - [Inpatient Barcode Labels Only](#inpatient-barcode-labels-only)
    - [Single Clinic Request Initialization](#single-clinic-request-initialization)
  - [Purge Data](#purge-data)
  - [Re-Compile Templates](#re-compile-templates)
  - [Record Tracking System Overall Parameters](#record-tracking-system-overall-parameters)
- [Film Tracking Specific Menu](#film-tracking-specific-menu)
  - [Overview](#overview-8)
  - [Imaging Area Set-up](#imaging-area-set-up)
  - [Jacket Profile](#jacket-profile)
  - [Request Film Jackets](#request-film-jackets)
- [MAS Specific Set-up Menu](#mas-specific-set-up-menu)
  - [Overview](#overview-9)
  - [Re-Charge a Chart](#re-charge-a-chart)
  - [Chart Request](#chart-request)
  - [Admitting Area Chart Request](#admitting-area-chart-request)
  - [Admitting Area Set-up](#admitting-area-set-up)
  - [Create MAS Labels/Records/Volumes](#create-mas-labelsrecordsvolumes)
  - [Fill Next Clinic Request](#fill-next-clinic-request)
  - [Profile of Charts](#profile-of-charts)
- [Glossary](#glossary)
- [Index](#index)
- [Data Supplement](#data-supplement)
How to Use This Manual
The Record Tracking User Manual is provided in an Adobe Acrobat PDF (portable document format) file. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VistA Home Page, “Viewers” Directory.
Once you open the file, you may click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. You may print any or all pages of the file. Click on the “Print” icon and select the desired pages. Then click “OK”.

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The prompt availability of patient records is an essential ingredient in the delivery of quality medical care. Lack of access to vital patient history contained in these records may lead to life-threatening situations.

The VA Record Tracking system is a comprehensive software package, written to aid file activities in assuring optimum availability of these records to a broad range of users within and outside the facility. Functions which were previously done manually have been computerized, promoting greater efficiency, uniformity and accuracy. Demographic record information is now available on-line to a broad range of users as well as a variety of reports which have been included to assist management in workload analysis and quality assurance.

The system has been designed so that it may be used in conjunction with bar code technology, further enhancing efficiency and accuracy. The Record Tracking system uses VA FileManager, and integrates with the Radiology and PIMS packages in performance of its functions.

This package was originally designed for use in tracking Medical Administration and/or Radiology records. A great deal of flexibility has been built into the system so that it may be custom-tailored to meet the needs of practically any file activity.

Other related materials to this guide are the Record Tracking Technical Manual and the Record Tracking Monograph. The Record Tracking Technical Manual is mainly directed at the application coordinator and site manager to assist in initialization, parameter definition and maintenance of the system. The Record Tracking Monograph provides a brief synopsis of the Record Tracking system.

# # Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a comprehensive software package, providing for all aspects of records control and maintenance. There are six user menus and two site manager/application coordinator menus in support of this goal.

TRANSACTION MENU

REQUEST RECORDS MENU

PULL LIST FUNCTIONS MENU

RECORD INFORMATION MENU

MANAGEMENT REPORTS MENU

INACTIVATE RECORDS MENU

SYSTEM DEFINITION MENU

COMPUTER SITE MANAGER'S MENU

The Transaction Menu is basically dedicated to file room functions. It provides software in support of the following activities:

- Charge-out/Check-in of records
- Creation of new records/volumes
- Inactivation/Reactivation and deletion of records
- Printing of barcode labels (on a one-by-one basis)
- Transfer of records to other facilities
- Recharging records to other borrowers
- Flagging a record as "missing". This fires off a MailMan message to a specified mail group advising that the record is missing so users may search their areas for the record.
- Setting a "loose filing" indicator for a specified record. This causes a message to be displayed to any user who selects the record for transaction, advising that loose filing exists.

The Request Records Menu supports requisitioning activities for individual records. Requests may be entered for records needed at future date/times as well as immediately. Entry of these requests causes a request notice to be printed in the file room (or wherever specified through System Definition). File room personnel use the appropriate option to either fill the request, thereby charging the record out to the requestor, or deem the request as unfillable. This menu interfaces with the Scheduling module of the MAS package and Pull List Functions Menu. All record requests appearing on pull lists (entered either through the Scheduling module or the Pull List Functions Menu) may be accessed through this menu. When pending, past or present requests exist for a record, a message will be displayed if the record is selected for transaction.

The Pull List Functions Menu also supports record requisitioning activities; however, it provides the capability for an individual borrower to request multiple records at a time, thus creating a pull list. It interfaces with the Scheduling module automatically creating pull lists for scheduled clinics. These pull lists are printed on a regular basis, file room personnel fill the requests, and the records are supplied to the appropriate area.

The Record Information Menu provides five record reports which may be displayed for specified patients. These reports are useful in the location and retrieval of records and also provide informational tools for performance of other maintenance and control activities. One report provides a listing of past locations of a particular patient's records as well as the patient's past scheduled appointments and episodes of inpatient care. Another gives a chronological listing of past movements of a patient's record(s) (i.e. charge-out, check-in, transfer, etc.). The other three reports provide an on-line profile of what records exist for a patient and their current location.

The Management Reports Menu provides ten reports which are useful in analyzing workload and identifying record control problems. Management may immediately identify records charged out of the home file room, records charged out for inpatients, records for which loose filing exists, overdue records, pending requests, records charged to a specific borrower and pending requests for a specific borrower. A report is also provided which may be used to evaluate response times for record requests.

The purpose of the Inactivate Records Menu is to perform record retirement tasks. Many options on this menu are similar or identical to options on other menus; however, their purpose here is specific to record retirement.

The System Definition and Computer Site Manager's Menus are provided for initialization and maintenance of the package and for defining site-specific parameters.

The functions within this system interact with one another affording greater control over records. For example, when a record is being checked into the file room the system will display a bulletin if pending requests exist for the record, if it has been flagged as "missing", if loose filing exists, if the patient is currently an inpatient, or if it is being checked into a home file room other than its own. The user may elect to perform any necessary functions related to these bulletins without leaving the option he is working in.

# # Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no legal requirements associated with this package.

# Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Record Tracking module has been designed so that it can be used in various applications. There are many parameters associated with this package that can be set according to each site's specific needs. The System Definition Menu and the Computer Site Manager's Menu are used to set these parameters. Files associated with the Record Tracking package which may be affected by these parameters include the Reasons file (#195.6), the Record Tracking System Parameters file (#195.4), the Record Movement Types file (#195.3), the Record Types file (#195.2), the Record Tracking Application file (#195.1), the Label Format file (#194.4), and the Borrowers/File Areas file (#195.9). The task of setting these parameters is generally performed at the time of initialization of the package, but the parameters can be changed at virtually any time after they have been set. For more information, please refer to the System Definition and Computer Site Manager's Menus.

Three standard barcode labels are included in the Record Tracking package (record, request, and borrower). Under NO circumstances should the existing standard label formats be edited.

The site has the ability to create its own barcode label formats through the Label Functions Menu of the System Definition Menu. It is possible to change the format of site-created labels; however, it is strongly recommended that existing label formats be left as they are. If the site finds it necessary to change a site-created label format, a new label format should be created to incorporate the change(s).

# Transaction Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transaction Menu is the focal point of the Record Tracking package. Generally, it is dedicated to file room activities although select options may be given to other users on an as- needed basis. It supports the following functions.

- Charge-Out/Check-In of records from/to their home location (file room)
- Creation of new records/volumes and printing of barcode labels
- Inactivation/Reactivation and deletion of records
- Transfer of record to/from other facilities
- Recharging records from one borrower to another
- Changing the home location and/or retirement status of a record
- Setting of a LOOSE FILING INDICATOR to generate a message upon check-in of a record that loose filing exists for that record
- Flagging and removing a record as "missing" thereby generating a MailMan message to a specified mail group advising the record is missing.

The functions on this menu are integrated with one another as well as with others in the system, thereby permitting them to be performed within other options. For example, if a record flagged as missing were selected for check-in to a file room, the user would be prompted through the process of removing the missing flag without leaving the check-in option. (This would occur in accordance with the site parameters set forth.)

Below is a descriptive listing of the options on this menu.

CHARGE-OUT RECORDS - Used to record the borrowing of records from their home location by in-house users. Records the borrower of the record along with the date/time charged out.

CHECK-IN RECORDS - Used to record the return of borrowed records to their home location. Enters the home location as the borrower of the record along with the date/time of check-in.

CREATE A LABEL/RECORD/VOLUME - Used to create initial or additional records/volumes for a patient and print bar code labels for new or existing records.

PATIENT CHARGE-OUT - Used to record a patient as the borrower of their own record. Records the patient as the borrower as well as the date/time of charge-out.

UPDATE RECORD'S ATTRIBUTES - Used to enter changes to a record's home location and retirement status or to set a LOOSE FILING INDICATOR thus generating a message upon check-in of the record advising that loose filing exists.

DELETE A RECORD - Used to delete a record and all associated requests, movements, etc. from the Record Tracking system.

FLAG RECORD AS MISSING - Used for records identified as lost; such records may be flagged as missing thereby generating a mail message to a MailMan group (as defined through site parameters). Missing flags may also be removed through this option.

INACTIVATE/REACTIVATE RECORDS - Used to render a record unavailable/available for transaction within the Record Tracking system. Does not delete all associated information, merely prevents the record from being selected for transaction.

MOVE REQUESTS TO LAST VOLUME - Used when an additional volume of a patient's record has been created to move all requests from the last volume to the new one; i. e. Volume \#2 of a patient's medical record has just been created - this option would be used to move all requests for Volume \#1 to Volume \#2.

MULTIPLE NEW VOLUME CREATION - Allows creation of multiple additional volumes to an already existing record set. May be used after system initialization to create additional multiple volumes not created by the process.

NEW VOLUME CREATION - Allows creation of individual additional volumes to an already existing record set.

RE-CHARGE RECORDS - Used to record the transfer of charged out records from one in-house borrower to another.

TRANSFER RECORDS MENU

> Create Record/Volume for transferred Record - Used to create new records or additional volumes for records transferred from other VA facilities.

> Request a Transfer from another Institution - Used to generate a Request for Transfer of Veterans Records (Form 70-7216a). This form is used to request patient records from other VA facilities.

> Return Transferred Record - Used when a record which was transferred out to another VA medical center is returned to your facility. This option transfers back and reactivates a returned record.

> Transfer Record to another Institution - Used to transfer records to other VA facilities. You may generate a Notice of Transfer of Veterans Record (Form 70-7216a) through this option.

## Charge-Out Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to record necessary information when records are borrowed from their home file room by in-house users. Borrower information is displayed each time the associated Record Inquiry is accessed through the Record Tracking system. This option is intended primarily for charging records from a file room; however, it may also be used to recharge records when they are transferred to another borrower.

Use of the option is very straight-forward; a borrower is selected, record(s) are entered for chargeout, the system records the chargeout(s), either immediately or by queuing a background job, and the routine is complete. At the conclusion of a session, you may enter another borrower or exit the option. Borrowers and records may be entered via bar code label reader, keyboard entry, or a combination of both. Most often, you will probably use the bar code label reader as this is the fastest method.

Messages are displayed when the patient selected is an inpatient, there are pending requests for the record, the record has been flagged as missing, a loose filing indicator has been set for the record, the selected record is unavailable for transaction, the borrower is not an active borrower, etc. You may then be prompted to perform the necessary task associated with the record, patient or borrower. Through this option, records may also be automatically created when the patient name selected has no records in the Record Tracking system. These will be created according to site specifications.

Much of what occurs in this option depends upon your site's individual specifications made through the system definition. Security access may be a factor when dealing with missing records. Please refer to the Flag a Record as Missing option of this chapter for further detail.

## Check-in Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Check-in Records option is used to record the return of borrowed records to their home file room. The system records the record being returned as well as the date/time of return. The associated Short Record Inquiry will then reflect the home file room as the current borrower each time it is accessed through the Record Tracking system.

Records may be entered for check-in either by wanding the bar code label or entering the patient's name using standard conventions. The bar code reader is the fastest method and it is recommended you use it whenever possible, especially when checking in multiple records.

In order to maintain optimum control over records, the option has been designed to account for a variety of factors specific to the record selected. Messages may be displayed when the loose filing indicator has been set for a record, the patient is an inpatient, a missing flag has been set, pending requests exist, etc. You may be prompted to perform the necessary task associated with the record. Through this option records may be automatically created when no records exist within the Record Tracking system for the patient entered. These records will be created in accordance with your site's specifications.

This option is not locked; however, the MAS/RAD FR STAFF KEY may be a factor depending upon your site's specifications. A site definable feature allows file rooms to be secured. Only holders of the MAS/RAD FR STAFF KEY may enter such file rooms as borrowers of records.

## Create a Label/Record/Volume

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create a Label/Record/Volume option is used to print bar code labels and/or create new records or additional volumes for specified patients. You may use it to create records and associated bar code labels for patients new to the system or to create additional records/volumes and associated bar code labels for patients already in the system. You may also use it to print bar code labels for existing records. This option is not intended for initialization purposes, as it works on a patient-by-patient basis. The Computer Site Manager's Initialization Menu is provided for that purpose.

Only patients already in your database may be entered. For all patients, records will be created according to site parameters defined for the application (MAS/Radiology) you are working with.

For new patients, records will be created according to your site's specifications for initial record creation. For example, if you are creating a medical record for a new patient in MAS, and your site has defined administrative records "linked" with medical records through the Type of Record Set-up option in the System Definition Menu, the system would also automatically create an administrative record. This would apply only to patients not already in the system.

For patients already in the system, you may specify one record/volume at a time and will be given the opportunity to transfer pending requests for the record type being created to the newest volume.

For each record/volume created, the system will assign a record identifier number, prompt for home location and current borrower/file room, and print a bar code label.

## Patient Charge Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Charge-Out option is used to record a patient as the borrower of his/her own record(s). You may wish to use this option for patients carrying their x-rays to an outside physician. The system records the patient as the borrower of the record along with the date/time of charge-out, entering this information into the patient's movement history. This information is displayed each time the associated record inquiry or Short Record Inquiry is accessed through the system. You will also be given the opportunity to enter a comment pertaining to the charge-out if you wish. This comment will be displayed each time the patient's Short Record Inquiry is accessed through the system until such time as the record is checked back in.

The option provides for several other occurrences such as removal of missing flags and creation of records for patients not having any records in the system.

## Update Record’s Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update Record's Attributes option is used to make changes to the following specific record data: loose filing indicator, home location and retirement status. Each of these fields will already have a default value which has been assigned by the system (unless changes have previously been made). The first field will be the loose filing indicator which will have a default of NO. Its purpose is to inform users that loose filing (such as laboratory reports, progress notes, correspondence, etc.) exists for a specific record. When this field is set to YES, a message is displayed advising loose filing exists whenever the record is selected for check-in to its home location. It should be set back to NO after the loose filing has been entered into the record.

The home location is assigned to a record when it is created. The location assigned will be in accordance with site specifications. This may be changed through this option; however, the new home location entered must be set up through site specifications to handle the record type you are working with and also tied in with the application you are working with.

When records are created by the system, they are automatically assigned a retirement status of OK TO RETIRE. The REASON NOT TO RETIRE field is used to make changes to this status. This retirement status will be reflected on the Record Inquiry which should always be checked prior to retiring a record.

## Delete a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete a Record option is used to delete a record from the system. It is intended for use in those cases where a record was created erroneously or perhaps a multi-volume set is consolidated.

The system only allows deletion of most recent volumes of a record set; i.e., you will not be able to delete Volume 2 of a 6 volume set. Record entry may be made either by wanding of the bar code label or entry of the patient's name. Prior to deleting the record, you will be given the opportunity to move requests to the next lower volume number of the record type being deleted. When a record is deleted, all associated requests for the record, missing record log entries and movement history log entries are also deleted. A MailMan message will be generated advising the record has been deleted. This message goes to the same mail group that receives messages on missing or found records.

## Flag Record as Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Flag Record as Missing option is used to assist in locating records which have been deemed lost within a facility. Missing flags may be placed on (or removed from) such records through this option. When such a flag is placed on a record, a MailMan message is generated to a group of users specified through your site parameters. This message advises the record is missing, giving patient name, record type and volume number. Users may then search their work area for the missing record. The associated Record Inquiry will reflect the record as missing. Records which have been flagged as missing may not be processed through other options until the flag is removed.

In order to enter this option, you must hold the RT MAS/RAD-FR-SUPERVISOR key. Removal of a missing flag may be done through other options within the system and the action will vary depending upon site parameters. Site parameters for removal of a flag may be set in one of two ways; any user may remove a missing flag from a record when it is accessed through other options or only the holder of the RT MAS/RAD-FR-SUPERVISOR key may remove such a flag. This parameter is set for all record types within an application; therefore, the action may differ between record types within the same application.

When the parameter is set such that any user may remove a flag and a missing record is selected for processing, the user will be prompted through the process of removing the flag. The record will then be deemed "found pending supervisor approval". The supervisor (or designee) will review the finding and approve/disapprove the removal of the missing flag using this option. When a missing record is selected for which only a holder of the RT MAS/RAD-FR-SUPERVISOR key may remove the flag, a message will be displayed to the user advising that the record is missing, and no further processing will be allowed. The appropriate holder of the RT MAS/RAD-FR-SUPERVISOR key will receive a MailMan message advising that an attempt was made to process the record. The holder of the RT MAS/RAD-FR-SUPERVISOR key may then review the attempt and remove the flag using this option.

Flag Record as Missing

This is an example of the MailMan message which is generated when a record is flagged as missing. It is sent to all members of whatever mail group is specified to receive such messages through your RECORD TRACKING site parameters.

SUBJ: AN ADMINISTRATIVE RECORD has been flagged as MISSING 03 DEC 87 12:08 9 Lines

From: TWO,TEST (ALBANY ISC) in 'IN' basket.

-----------------------------------------------------------------------------

The following record has been flagged as missing:

Name : RTPATIENT, ONE

Type of Record : ADMINISTRATIVE RECORD

Volume : 1

If you find this record please call MEDICAL ADMINISTRATION or respond

to this message.

Thank you.

This is an example of the MailMan bulletin which is generated when a missing flag is removed from a record by a user other than one holding the FR SUPERVISOR KEY. This message is the same when a holder of the FR SUPERVISOR KEY approves the removal of a missing flag by another user, except the "STATUS of missing record" will be FOUND instead of FOUND/SUPERVISOR APPROVAL PENDING.

Subj: Missing ADMINISTRATIVE RECORD has been FOUND 08 Dec 87 10:16 12 Lines

From: TWO,TEST (ALBANY ISC) in 'IN' basket.

--------------------------------------------------------------------------

The MEDICAL RECORD (V1) for RTPATIENT,ONE (666456789) was found.

The following is information concerning the finding of the record:

-WHO entered the record as found : TWO,TEST

-BORROWER who had missing record : CORRESPONDENCE UNIT

-PHONE \#/Physical LOCATION : 234/22B

-WHEN was the record found : DEC 8, 1987 10:15

-STATUS of missing record : FOUND/SUPERVISOR APPROVAL PENDING

-MOVEMENT attempted when found : CHECK-IN

For more information use the 'Record Inquiry' option of the 'Record

Information' menu.

## Inactivate/Reactivate Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inactivate/Reactivate Records option is used to render a record unavailable/available for transaction within the Record Tracking system. It may be used when records are retired, or perhaps in those instances when it is necessary for a borrower to retain a record for an extended period of time (i.e., for research purposes). Such a record will not appear on the Overdue Records List.

Inactivation of a record makes it unavailable to other users to request, charge-out, check-in, re-charge, etc. It will, however, appear on the Record Inquiry option of the Record Information Menu as inactive.

Records may be inactivated as well as reactivated through this option. If you choose to inactivate the record, you will be prompted for a borrower to which the record should be inactivated. Your entry at this prompt may be a borrower who will be retaining the record for an extended period or your file room.

If you are retiring the record and wish to transfer it to the appropriate Record Processing Center, use the Transfer Records option of the Transaction Menu.

When a record is reactivated, it is automatically charged to the location associated with the user performing the reactivation; usually, its home file room.

Following selection of movement type and borrower (if applicable), you will be prompted to select the record. The system will only allow you to select a record appropriate to the movement type selected. In other words, you will not be permitted to inactivate an already inactive record. If record selection is made by entering the patient's name, only those records appropriate to the movement type selected will be displayed on the patient's Short Record Inquiry.

Multiple records may be entered during a session. Dependent upon the number entered and your site's parameters, they will either be inactivated/re-activated upon exiting the option or queued for action later.

## Move Requests to Last Volume

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to transfer all pending requests to the most recent volume when an additional volume has been added to a patient's record set.

You will be prompted for the desired record. Only active records may be selected; then, only the last volume of a multiple volume set may be selected for the patient entered. You will then be asked if you wish to transfer all pending record requests to that volume.

## Multiple New Volume Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multiple New Volume Creation option allows creation of multiple additional volumes to an already existing record set and transfer of pending requests to the latest volume created. For the most part, this option is intended for use in conjunction with your initialization process to create additional volumes for those patients having more than one volume of a record type. The initialization process only creates one volume of the record type(s) specified in the site parameters. This option allows you to create up to six additional volumes of a record type.

You may only create additional volumes of record types for which the patient already has Volume \#1. Should you wish to create Volume \#1 of a record type, you should use the Create a Label/Record/ Volume option of the Transaction Menu.

The home location and current borrower/file room will be prompted for each record created. Defaults, as defined through your site parameters, will be displayed for these fields. Following this, the system automatically assigns a record identifier number and prints a corresponding bar code label on the default device defined through your site parameters. You will then be prompted to transfer pending requests for the record type created to the latest volume.

## New Volume Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The New Volume Creation option is used to create individual additional volumes to a patient's already existing record set. You may wish to use it when the file room creates an additional folder for a patient or perhaps in conjunction with the system initialization process to create an additional volume not created during initialization. The Record Tracking initialization process only creates one volume of each record type specified through site parameters. If it is necessary to create initial records for a new patient or multiple additional volumes, the following options on the Transaction Menu should be used: Create a Label/Record/Volume or Multiple New Volume Creation.

The system will only accept record types for which the patient already has Volume \#1. The home location and current borrower/file room will then be prompted with your site's specified defaults displayed for acceptance. Record Tracking will automatically assign a Record Tracking identifier number and print a bar code label for the record created. You may transfer pending record requests for that record type to the last volume created.

## Re-Charge Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Re-Charge Records option is used to record transfer of those records charged from the file room from one borrower to another. It is for use with in-house borrowers only. Transfer of records to other institutions should be entered through the Transfer Records option. The system records the new borrower, location/phone and date/time of re-charge. This information is displayed each time the associated record inquiry is accessed through the Record Tracking system.

Upon exiting the option, the records will either be re-charged immediately or queued for re-charge depending upon site parameters and the number of records entered during the session.

Missing flags may be removed thru this option and records may be created for patients already in your database but having no records in the Record Tracking system. These will be created in accordance with site specifications for initial creation of records.

## Transfer Records Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Create Record/Volume for transferred Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create Record/Volume for transferred Record option is used to create new records or additional volumes for records received from another VA facility. You may use it to create records and associated bar code labels for patients new to the system or to create additional records/volumes and associated bar code labels for patients already in the system.

New records will be created according to your site's specifications for initial record creation. For example, if you are creating a new medical record for a patient in MAS and your site has defined administrative records "linked" with medical records through the Type of Record Set-up option in the System Definition Menu, the system would also automatically create an administrative record. This would apply only to records not already in the system.

For records already in the system, you may transfer pending requests for the record type being created to the newest volume.

For each record/volume created, the system will assign a record identifier number and a movement type of TRANSFER CREATE, prompt for a content descriptor (optional free text field 2-20 characters in length used to further describe the record), home location, and current borrower/file room.

Transfer Records Menu

### Request a Transfer from another Institution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Request a Transfer from another Institution option allows you to generate Form 70-7216a, "Request for and/or Notice of Transfer of Veterans Records". This form may be used to request patient records from a remote site. A remote site is any VA facility with which you exchange records.

You will be prompted to fill in only record information. Routing, remote mail group, and request notice printer information is defined by your site manager through the File Room/Remote Set-up option.

Once generated, the form is sent to the mail group and/or request printer at the remote site. A copy is also received by the requester via a MailMan bulletin.

Supplement

The following is a list of data fields from the Request for Transfer of Veterans Records form with a brief description. Only fields that require user input are shown.

1a Station Name

Name of station you wish to request records from. You may send the request to multiple sites; therefore, this prompt will repeat (1b, 1c, etc.) until a \<RET\> is entered. Corresponding routing information is entered automatically from the File Room/Remote Set-up option in the Computer Site Manager's Menu.

NAME (Last,First,Middle)

Name of patient for which you are requesting records. Claim number, SSN (5a) and service number (6) are entered automatically.

TYPE OF TRANSFER

Choose Temporary (default) or Permanent.

Transfer Claims Folder

YES/NO (default)

OTHER FOLDER TRANSFER

Enter the corresponding number(s) of the record types you wish to transfer.

Reason for Transfer or Remarks

Any remarks you wish to accompany the request. You are allowed two lines of free text.

Transfer Records Menu*Request a Transfer from another Institution*Adjudication Action pending

YES/NO (default)

Date

Date of request. You may select a past date. NOW is the default.

Check when copy 2 is sent to Telecom \[ \] UNIT

YES/NO

Transfer Records Menu

### Return Transferred Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Return Transferred Record option is used when a record which was transferred out to another VA medical center is returned to your facility. This option transfers back and reactivates a returned record in the Record Tracking system.

If you answered YES to the "Do you want to use the file room's default devices? No//" prompt upon entering the Record Tracking system and a default device is defined through your site's parameters, any bar code labels you choose to print will be printed to that device. Otherwise when you choose to print a bar code label, you will be prompted for a device.

Transfer Records Menu

### Transfer Record to another Institution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transfer Record to another Institution option is used to record the transfer of records to other VA facilities. You are allowed to enter a past date of transfer in order to update your records.

Once you have selected the institution you are transferring the records to, you are prompted to select the record(s) to be transferred. This prompt will repeat to allow you to transfer multiple records to the selected institution. At subsequent appearances of the "Select Record" prompt, you may enter a \<?\> for a list of records selected for transfer during this session. Any of the records displayed may be deleted by entering a minus sign \<-\> before the record number (-1342) at this prompt.

You also may generate a Notice of Transfer of Veterans Record (Form 70-7216a) through this option. This form will not be generated if you enter a past date of transfer. The 70-7216a is sent to members of the mail group and/or request printer at the remote site defined by your site manager through the File Room/Remote Set-up option. A copy is also received by the user performing the transfer function.

When completing the Notice of Transfer form, you will be prompted to enter the type of transfer, other folder type(s) you wish transferred, reason for transfer/remarks and the date of transfer. The station you are transferring the records to and the patient information is entered automatically by the system from your responses to previous prompts. Routing, remote mail group, and request notice printer information is defined by your site manager through the File Room/Remote Set-up option.

# Request Records Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Request Records Menu provides the software necessary for individual users of the system to request records from their file room. Through this menu, records may be requested and requests may be filled, cancelled, edited, designated as "Not Fillable", displayed and printed.

Requests for records may be entered for a current or future date. Requests entered for current date will be printed on the default request printer specified for the record's home location (file room). Requests entered for future times may be accessed by printing of the Pending Request List option of the Management Reports Menu.

The Request Records Menu interfaces with the Pull List Functions Menu. Each entry on a pull list is also considered an individual request and may be accessed as such through this menu.

The following is a descriptive listing of the options contained in this menu.

CANCEL A REQUEST - Allows requests which have previously been entered to be cancelled from the system. Users must hold the RT MAS/RAD-FR-SUPERVISOR key in order to cancel requests.

DESIGNATE REQUESTS AS 'NOT FILLABLE' - Used by file room personnel when they are unable to fill a request for a record, such as when the requested record is unavailable.

DISPLAY REQUEST - Used to display a request for a record on the screen.

EDIT A REQUEST - Used to edit the data in a previously entered record request.

FILL A REQUEST - Used by file room personnel to charge-out (fill) a requested record to the requestor.

REPRINT A REQUEST NOTICE - Used to reprint a record request label.

REQUEST A RECORD - Used to enter a request for a record into the system. The four statuses associated with requested records are as follow.

> CHARGED - Requested record has been charged to the requestor.

> CANCELLED - Record request has been cancelled.

> REQUESTED - Record request is still pending.

> NOT FILLABLE - Not possible to fill the request; i.e., the record is unavailable.

## Cancel a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancel a Request option is used to cancel a request for a patient's record. The user may cancel a single request, multiple requests or a range of requests for the same record. The request may be selected by patient name, request number or by wanding the request bar code label. If the request is selected by patient name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the requestable records for that patient in that application. After the desired record is selected, a request profile will be displayed for that record. This includes the current location of the record, the home file room of the record, recent pending requests, etc. If the request to be cancelled is selected by request number or by wanding the request bar code label, an abbreviated display will appear providing data specific to that request only.

Holders of the RT MAS/RAD-FR-SUPERVISOR security key may cancel requests made by other users in their application. Users not holding this security key may only cancel their own requests.

When a request is cancelled, a cancellation bulletin can be sent to a mail group, the file room request printer or both. This is defined through the Application Set-Up (Site Mgr) option.

## Designate Requests As 'Not Fillable'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Designate Requests as 'Not Fillable' option is used by file room personnel to specify requests for patients' records as not fillable. Conversely, requests with a status of not fillable may be changed to requested through this option. A request may not be fillable due to the record being charged to another borrower, record missing, etc.

Requests designated as not fillable will still appear on the Pending Request List, the Requests Pending for Borrowers List and will also still appear as a pending request under Request a Record option.

When request selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the patient's requestable records in that application. If a record has been inactivated or transferred out, it will not appear in the inquiry. After the record is selected, a request profile will be displayed for that record listing the requests which may be chosen. The user may designate a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number or by wanding the request bar code label, only the data associated with that particular request will be displayed.

## Display Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Request option is used to display the data associated with a particular request for a patient's record. The option has only one prompt, "Select Request". The user may enter the patient's name, the date of the request to be displayed, a back arrow (') plus request number or may wand the request bar code label.

If the request is selected by entering the patient's name and the patient has more than one record which has a pending request, the system will display a list of those records providing the following information: record type, patient's social security number and date of birth, record location, phone and room number. After the correct record is chosen, all the pending requests for that record will be displayed. Upon selecting the desired request, the data associated with that request will be displayed. This may include such information as patient name, date/time requested, user requesting record, date/ time record needed, requestor, request status, date/ time current status, user responsible for status, date request last printed, etc.

If the record selected has only one pending request or if the request is selected by any of the other available methods, the system will ask for confirmation that this is the desired request and then display the data associated with that request.

Following is a brief explanation of some of the data items which may appear in the request display:

Requestor borrower

User Requesting Record person actually making keyboard entry

Request Status Requested, not yet filled

Charged, request filled

Not Fillable

Cancelled

Pull List name and date of pull list where this

request appears

Parent Request request being displayed is in conjunction

with another request (parent) in

accordance with site parameters

## Edit a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit a Request option is used to edit data associated with a request for a patient's record. Only the date/time needed and requestor may be edited.

When request selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the patient's requestable records in that application. If a record has been inactivated or transferred out, it will not appear in the inquiry. After the record is selected, a request profile will be displayed for that record listing the requests which may be edited. Requests from pull lists and requests which have been printed may not be edited. The user may edit a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number, only the data associated with that particular request will be displayed.

Users with the RT MAS/RAD-FR-SUPERVISOR security key may edit requests made by other users within their application. Users not holding this security key will only be able edit their own requests.

## Fill a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fill a Request option is used by file room personnel to fill a request for a patient's record(s). The request may be selected by patient name, request number or by wanding the request bar code label.

When request selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the patient's requestable records in that application. If a record has been inactivated or transferred out, it will not appear in the inquiry. After the record is selected, a request profile will be displayed for that record listing the requests which may be filled. The user may fill a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number or by wanding the request bar code label, only the data associated with that particular request will be displayed and the request will be added to the list to be processed.

Deletion of a selected request is possible by entering a minus sign (-) and the request number at the appropriate prompt.

## Reprint a Request Notice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reprint a Request Notice option is used when it is necessary to reprint a request for a patient's record(s). The request may be selected by patient name, request number, or by wanding the request bar code label.

When request selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the patient's requestable records in that application. If a record has been inactivated or transferred out, it will not appear in the inquiry. After the record is selected, a request profile will be displayed for that record listing the requests which may be reprinted. The user may reprint a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number or by wanding the request bar code label, only the data associated with that particular request will be displayed.

## Request a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Request A Record option is used to enter a request for a patient's record. The user may request a single record, multiple records or a range of records for a patient. He/she may request the record for the current time or a date/time in the future. The person/location borrowing the record must be in the Borrower file.

Dependent on how the site parameter is set at your facility, the current borrower of a record may enter a request for that record for a future date. This may be done by wanding the record's bar code label or by keyboard entry. Use of the bar code label reader is the fastest and most accurate method of request.

When record selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the requestable records for that patient in that application. If a record type has been defined as unrequestable through your site parameters, it will not be displayed in the Short Record Inquiry. If the record requested has been inactivated or transferred out to another facility, it will not be displayed in the inquiry. Wanding the bar code label of an unrequestable record will result in the message, "No match found" being displayed. After the record(s) is selected, a request profile will be displayed for each record. This includes the current location of the record, the home file room of the record, recent pending requests, etc. A sequential request number is automatically assigned by the system for each record requested.

# Pull List Functions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pull List Functions Menu supports requisitioning of multiple records needed for the same date/time by the same borrower. Such a requisition is known as a pull list.

Within the Record Tracking system there are two types of pull lists; Ad Hoc Pull Lists and Clinic Pull Lists. Ad Hoc Pull Lists may be created through the Pull List Functions Menu on an as-needed basis. These may be used in both the Medical Administration application and the Radiology application. A variety of areas within your facility will probably want to use the Ad Hoc Pull Lists - Correspondence Unit, Research Service, Medical Information Section, etc.

Clinic Pull Lists are created automatically by the system as appointments are made through the Scheduling module. This occurs in accordance with your site parameters, which are usually set by the Application Coordinator and Site Manager. Assuming all these parameters have been set, the system will create these pull lists as appointments are scheduled to clinics. A separate pull list will be created for each clinic for each day it meets, listing appropriate record requests for the patients scheduled. When appointments are cancelled, the system also removes the corresponding requests from the pull list and, if rescheduled, places them on the new pull list. Each record listed on a pull list has a corresponding request which may be accessed through the Request Records Menu. The records requested will be in accordance with the specifications set forth for that clinic. One clinic may request all volumes of each patient's medical records, while another may only request the latest volume. Some clinics may request administrative records as well as medical records. Clinics may even request radiology records via these pull lists, if so defined. For instance, an Orthopedic Clinic may wish to routinely request radiology records for each patient seen. In this case, the system would create two pull lists; one for Medical Administration and one for Radiology. The Medical Administration Pull List would be known as the "parent". The specifications will vary from clinic to clinic.

It is necessary to print these pull lists through the Print Pull List(s) option on this menu. Your site may wish to print these lists on a daily basis, several days in advance of clinic meetings.

There are three statuses related to pull lists.

REQUESTED - This status indicates the records on the pull list have been requested, but not yet charged out. Also known as "pending".

CHARGED - This status indicates the pull list has been charged to the borrower for whom they were requested.

CANCELLED - This status indicates it is no longer necessary for the file room to pull the records on the pull list; it has been cancelled or deleted.

The following is a descriptive listing of the options contained in this menu.

CREATE A PULL LIST - Used to create ad hoc pull lists; those not associated with scheduled clinic appointments.

ADD REQUESTS TO PULL LIST - Used to enter additional requests to an already established pull list with a status of REQUESTED.

CHARGE OUT PULL LIST RECORDS - Used to charge out records on a pull list all at once. Records may first be specified as not fillable, then the remaining ones are charged to the specified borrower. All clinic lists for a given date may be done at once.

PULL LIST DATE CHANGE - Allows change of requesting date/time to an already established pull list.

ENTIRE PULL LIST CANCELLATION - Allows deletion of an entire pull list with a status of REQUESTED.

CANCEL REQUEST FROM PULL LIST - Used to remove individual record requests from an already established pull list with a status of REQUESTED.

DESIGNATE REQUESTS AS 'NOT FILLABLE' - Used to change status of individual requests on an already established pull list from/to REQUESTED or NOT FILLABLE.

EDIT PULL LIST COMMENT - Used to enter/edit comment on an already established pull list.

PRINT PULL LIST(S) - Used to print clinic and ad hoc pull lists.

SPECIAL MULTI-INSTITUTION PRINTS - Used by multi-divisional facilities to obtain a list of records which need to be moved between divisions for clinic purposes.

ENTIRE PULL LIST CANCELLATION (ALL DATES) - Used to cancel pull lists associated with a clinic which has been deactivated. This option will cancel all pull lists for a specified clinic.

## Create a Pull List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create a Pull List option is used to create ad hoc pull lists (those other than automatically created by the system for scheduled clinics). This is useful for areas in your facility which request multiple patient records routinely, such as Medical Information, Correspondence, Fee Basis, etc.

The system will automatically assign a pull list number which you may edit if you wish.

This option may be used several ways. You may restrict the record type and volumes to be requested. When this is done, all you need do is enter each patient's name. The system will automatically extract the appropriate record for each patient entering it onto the pull list. For example, this may be done should you wish to request only the latest volume of each patient's medical record. When used in this manner, the process runs fairly quickly since patient short record inquiries will not be displayed. Pull lists may also be set up such that different record types and/or volumes may be entered. The process may not be as quick, since short record inquiries will be displayed upon entry of patient names; however, this is useful when it is necessary to request a variety of record types and/or volumes within the same pull list.

Entry of records and borrowers may be made either via keyboard or wanding of bar code labels. When record types and volumes are restricted, the system only accepts wanding of applicable record labels. As with all other options, the system checks the availability of records wanded and the borrower status of all borrowers.

If the date/time needed is the current date, a separate request for each record will immediately print on the appropriate printer; otherwise, it is necessary to print your pull list at an appropriate later date/time.

## Add Requests to Pull List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add Requests to Pull List option is used to enter additional record requests to an established pull list. Additions can only be made to pull lists with a status of requested. Record selection can be made by patient name, record number or by wanding the appropriate record bar code label.

The site's system definition (for clinic pull lists) or pull list specifications (for ad hoc pull lists) determine if certain prompts will appear in this option. If a particular record has been defined with the selected borrower, that record type will be automatically selected to be added to the pull list when the patient's name is entered.

The option allows for deletion of requests; however, only requests entered during the current session can be deleted and only before these requests are filed. You may view a list of the records requested during the current session, view a list of the requests previously made for this pull list or both. Information provided on the previous requests include request number, patient name, last four digits of patient's social security number, record type/volume and request status. The option also provides the capability to cancel all the requests which have been added in the current session.

## Charge Out Pull List Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Charge Out Pull List Records option is used to charge out patient records from a pull list. After allowing for designation of any requests as not fillable, the remainder of the requests on the pull list may be charged out all at once. You may charge out a single clinic pull list or multiple clinic lists for the same date. Ad hoc pull lists can only be charged out individually. This option may also be used to change the status of requests from NOT FILLABLE to REQUESTED.

Records may also be charged out to a holding area. This allows file room personnel to pull records for a clinic 2 or 3 days before the clinic actually meets. These charts may be held in the file room, or elsewhere, until the day of the clinic. While being held, they would be considered "charged to a holding area". While charged to a holding area, the clinic pull list status, as well as the status of each individual request, remain requested and are not changed to CHARGED. To charge the records to the requestor, the charge out process would have to be repeated.

If you choose to charge out all clinic records for a particular date, the system will display a message advising you to print an update listing before charging out the records. This is to assure that all add on requests have been pulled.

## Pull List Date Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to change the date for which pull list records are requested. It may be used for both ad hoc pull lists as well as clinic pull lists. Since new pull lists are automatically created by the system when clinics are rescheduled, it will most likely be used for ad hoc pull lists. The pull list must have a status of REQUESTED.

The original date of these pull lists will then be shown in brackets on the left each time the pull list is called up.

## Entire Pull List Cancellation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As its name implies, this option is used to cancel entire pull lists. Associated pull lists are automatically cancelled by the system when a clinic is cancelled, hence this option applies mostly to ad hoc pull lists. Pull lists cancelled must have a status of REQUESTED and be for a future date.

You will be prompted for the name, number or date of the pull list to be cancelled, then for confirmation. A message will be displayed advising that the pull list has been cancelled at the conclusion of the session.

## Cancel Request from Pull List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancel Request from Pull List option is used to cancel a request for a patient's record from a pull list. Requests may only be cancelled from pull lists for a future date having a status of REQUESTED or NOT FILLABLE. The request may be selected by patient name, request number or by wanding the request bar code label. If the request is selected by patient name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the requestable records for that patient in that application. After the desired record is selected, a request profile will be displayed for that record. This includes the current location of the record, the home file room of the record, recent pending requests, etc. If the request to be cancelled is selected by request number or by wanding the request bar code label, an abbreviated display will appear providing data specific to that request only.

A question mark \<?\> entered at the "Select Request" prompt will display all the requests previously made for the selected pull list. Information provided in this display includes request number, patient name and last four digits of social security number, record type/volume and request status.

## Designate Requests as ‘Not Fillable’

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Designate Requests as 'Not Fillable' option is used by file room personnel to specify requests for patients' records as not fillable. Conversely, requests with a status of not fillable may be changed to requested through this option. A request may not be fillable due to the record being charged to another borrower, record missing, etc.

Requests designated as not fillable will still appear on the Pending Request List, the Requests Pending for Borrowers List and will also still appear as a pending request under Request a Record option.

When request selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the patient's requestable records in that application. If a record has been inactivated or transferred out, it will not appear in the inquiry. After the record is selected, a request profile will be displayed for that record listing the requests which may be chosen. The user may designate a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number or by wanding the request bar code label, only the data associated with that particular request will be displayed.

## Edit Pull List Comment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Pull List Comment option is used to add or edit comments to pull lists. Comments to an ad hoc pull list can be added when the pull list is created through the Create a Pull List option. Comments to a clinic pull list (which is created through the Scheduling module) can only be added here. The comments of both pull lists may be edited through this option.

Only pull lists with a status of requested for today's date or a date in the future may be selected when utilizing this option. The pull list may be selected by pull list name, pull list number or date records needed.

## Print Pull List(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Pull List(s) option is used to print clinic and ad hoc pull lists. Clinic pull lists are automatically created through the Scheduling module when clinic appointments are made. The clinic must be initialized through the Borrower Initialization and Borrower Set-up options in Record Tracking before the appointments are made in order to create a clinic pull list. Ad hoc pull lists are created through the Create a Pull List option in Record Tracking. Any pull list, other than one automatically created through Scheduling, would be considered an ad hoc pull list. A pull list number is automatically assigned to every pull list created.

Pull lists may be sorted in one of the following ways: terminal digit; clinic name, terminal digit; clinic name, appointment time; home location, terminal digit; or home location, clinic, terminal digit. If more than one clinic is to be printed and sorted by terminal digit, there will be no separation of appointments by clinic. Appointments for all the clinics involved will be listed together by terminal digit. Ad hoc pull lists can only be printed individually by terminal digit.

Pull lists may be printed to include all appointments, a short non-fillable list, a detailed non-fillable list or to include only updates to the list. Updates are requests that were added after the entire pull list was last printed. The detailed non-fillable printout is the same as the Tracking Data Trace Report obtained by using the Combination Data Trace option of the Record Information Menu. This traces the movements of a patient's records back to a particular date. The date used depends on how the Record Set-up site parameter, "# of Previous Movements to Retain", is set at your facility. If you chose to sort by clinic name - appointment type, you can only print to include all appointments or a short non-fillable list.

The pull list status (requested, charged, cancelled) will only appear on clinic pull lists that are sorted by other than terminal digit. The status of a pull list may be Requested even though the status of each request on that list is Charged. This may occur if the requests were filled through the Fill a Request option of the Request Records Menu. The status of the pull list will not change from Requested to Charged or Cancelled until the Charge Out Pull List Records or Entire Pull List Cancellation options are utilized.

Record borrowers may wish to use this option to view charged out pull lists to determine which requests were not fillable.

## Special Multi-Institution Prints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Special Multi-Institution Prints option is used at multi-divisional sites to obtain a list of records which need to be moved between divisions for clinic purposes. The user may choose to print only a list of the records to be sent to the other division, only a list of the records to be received at the user's division or both lists. After the requested date is selected, the system will search the clinic pull lists for that date for any applicable records. These clinic pull lists will be listed on the screen along with the pull list status of each.

The records listed on the output will be sorted by terminal digit (SSN). Information provided includes patient name, record type, request number and status of request, requestor and time record needed, the current location of the record and other requests for that record.

## Entire Pull List Cancellation (all dates)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Entire Pull List Cancellation (all dates) option is used to cancel all the pull lists for a clinic. Pull lists must have a status of Requested and be for a future date. This option could be utilized if a site wanted to permanently cancel a particular clinic. After the clinic has been selected and you are certain you want to delete all the pull lists, the system will display a message informing you of how many pull lists were cancelled for that clinic.

# # Record Information Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Record Information Menu is comprised of five reports which provide comprehensive information pertaining to the records of specified patients. This information is valuable to a broad range of Record Tracking users in the retrieval, control and maintenance of patient records.

The following is a list of the reports included in this menu and a brief description of each.

COMBINATION DATA TRACE - Provides a chronological listing of past record locations, clinic appointments and admission activities, as well as a listing of future scheduled clinic appointments for a specified patient.

EXPANDED RECORD INQUIRY - The Expanded Record Inquiry option provides a listing of all records for a specified patient. The information from the short record inquiry is displayed plus the patient's last admission and discharge and the last three clinic appointments.

RECORD INQUIRY - Provides a detailed listing of all records for a specified patient. The information includes the following, as applicable: type of record, volume \#, record \#, descriptor, current location, current phone, associated borrower, date charged, movement, responsible user, home location, home phone, inactive flag, retirement flag and last access method. This information may be viewed on-line or sent to a printer.

SHORT RECORD INQUIRY - Provides an abbreviated on-line listing of all records for a specified patient. For each record, the following is listed: record type, volume \#, current borrower, date charged, phone/room \# of current borrower. If the record has been inactivated or transferred to another facility, this will also be shown. This listing is also provided throughout the Record Tracking package whenever a patient name is entered for record transaction.

TRACE MOVEMENT HISTORY - Provides a chronological listing of record movements for a specified patient; i.e. check-in, charge-out, transfer, etc. The following information is listed: date charged, record/volume, borrower, type of movement, \# of days with current borrower.

## Combination Data Trace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a chronological listing of past record locations, clinic appointments and admission activities as well as a listing of future clinic appointments for a specified patient. It is used to view a patient's record activity.

The first section of the report contains a chronological listing of all future clinic appointments. All past activities are then listed chronologically by date/time (most recent first) back to whatever date you specify. You may track back as far as 999 days. If you specify a Trace Cut-Off Date which is prior to the date Record Tracking was initialized at your site, the report will include scheduling and admission activities prior to the initialization date but no record activities.

The second section allows a view of the patient's record activity back to the specified date. The date/time, record location, clinic/ward and action may be displayed for each entry.

Record movements may be purged at a site's discretion. Such purging is done according to record type. Generally, your Site Manager or Application Coordinator will perform these purges. Movements which have been purged will not be reflected on this report.

You will be prompted for the patient's name, cut-off date and a device.

## Expanded Record Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Expanded Record Inquiry option provides a listing of all records for a specified patient. The information from the short record inquiry is displayed plus the patient's last admission and discharge and the last three clinic appointments. This information is valuable to a wide range of users involved in the daily activities of record maintenance and retrieval.

For each of the patient's records the following will be listed (if applicable): type of record, volume no., record no., descriptor, current location, current phone, associated borrower, date assigned to current location, movement and responsible user. For further explanation of each item included in this report, see the list of data definitions provided at the end of the Record Inquiry option documentation.

You will be prompted for patient name and a device.

## Record Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a detailed report of demographic and request information pertaining to the records of a specified patient. This information is valuable to a wide range of users involved in the daily activities of record maintenance and retrieval.

The report is run for a specified patient and may include all of their records, all volumes of a specified record type or just one volume. It may be viewed on the screen or printed out.

For each of the patient's records the following will be listed (if applicable): type of record, volume no., record no., descriptor, current location, current phone, associated borrower, date assigned to current location, movement, responsible user, home location, home phone, inactive flag, retirement flag and last access method. A list of data definitions is provided at the end of this option documentation providing further explanation of each item included in this report.

The Record Request Profile is also provided which lists requests by status (pending, filled, cancelled or never filled) indicating the record, requestor, date needed, phone \#, requesting user and request number.

Data Definitions

Following is a list of definitions for each field appearing on the Record Inquiry. The fields are listed in the same order they appear on the report.

FIELD DEFINITION

TYPE OF RECORD Medical, administrative, master folder, chest films, etc. Entries in this

field will vary depending upon which application you are working

with; Medical Administration or Radiology.

VOLUME NO. This is the volume number of the record.

RECORD NO. This indicates the internal number assigned to the record by Record

Tracking (sometimes referred to as the record identifier number). Each

record within the system is assigned a number upon creation. This

number is unique to the record and may be entered wherever you see

the Select Record prompt.

DESCRIPTOR A brief description of the record as entered by the user who created it.

CURRENT LOCATION Current borrower of the record.

CURRENT PHONE Telephone number/location of the current borrower.

Record InquiryFIELD DEFINITION

ASSOCIATED BORROWER The entry in this field will be the name of an associated borrower, if

applicable. Depending upon your site's specifications, users may be

prompted to enter the name of an associated borrower when charging

out or recharging a record. This is generally used when the actual

borrower of the record is a location, such as a clinic or ward. The entry

should be the name of an actual person. This gives other users a name

to contact when inquiring about the record.

SINCE Date/time the record was charged to the current location.

MOVEMENT Last movement of the record; i.e., charge-out, check-in, etc. This

movement resulted in the record being charged to the current location.

RESPONSIBLE USER The user responsible for making the last movement of the record.

HOME LOCATION Location the record resides when not charged out; generally, the file

room.

HOME PHONE This indicates the telephone number/location on file of the home

location.

INACTIVE FLAG An entry will appear in this field if the record has been inactivated or

transferred; otherwise, it will be blank.

RETIREMENT FLAG Used to indicate whether a record may be retired. It should be checked

prior to retiring any record. The following entries may appear:

> TEACHING

> TUMOR REGISTRY

> OK TO RETIRE

All records are assumed OK TO RETIRE by the system unless an

actual entry has been made through the Update Record's Attributes

option. If an entry has never been made, this field will be blank on the

Record Inquiry rather than OK TO RETIRE.

LAST ACCESS METH This indicates the method used (either barcode or non-barcode) the last

time the record was accessed.

## Short Record Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides an abbreviated on-line listing of all records for a specified patient. It is the same listing which is displayed throughout the Record Tracking package when a patient name is keyboard entered rather than a barcode being wanded.

This option displays several lines of demographic data related to the patient. For each record (listed by record type), the volume number, current borrower, date/time charged to that borrower and phone/room of the borrower will be shown. Whenever a record is inactive (as a result of being transferred to another facility or inactivated) or charged to a borrower as a result of being on a pull list, it will be so annotated beneath the record. Associated borrowers may also be shown.

## Trace Movement History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Trace Movement History option provides a chronological listing of record movements (charge-out, check-in, etc.) for a specified patient.

The report lists each record movement in order of date/time of occurrence (most recent first) giving record/volume, borrower and type of movement as well as the date/time. It also includes a "# of days" column which indicates the number of days the borrower had that particular record prior to the next movement.

You may select to sort this listing in date order which will include all records together (mixed) or you may have it broken down separately by record (separate). When broken down by record, the listing will still be in chronological date order; however, each record/volume will be listed separately.

The listing may differ somewhat between sites depending upon purge parameters and movement types set up. You will only see the number of movements your site has specified should be kept in the system..

You will be prompted for a patient, how you want the output sorted (MIXED or SEPARATE), and a device.

# Management Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Management Reports Menu provides a variety of reports useful in analyzing workload and identifying problems in record control and maintenance activities.

The following is descriptive listing of the reports on this menu.

AD HOC REQUEST RESPONSE STATISTICS - A statistical report of file room response times to individual record requests.

CHARGED RECORDS BY HOME LOCATION - A listing of records assigned to a specified home location (file room).

INPATIENT RECORD LOCATION LIST - A listing of the whereabouts of all records of current inpatients. Includes inactive as well as transferred records.

LOOSE FILING REPORT - A listing of all records for which the loose filing indicator has been set to YES. This indicator is set in the Update Record's Attributes option on the Transaction Menu.

MISSING RECORDS LIST - A list of all records which have either been flagged as MISSING or FOUND PENDING SUPERVISOR APPROVAL.

OVERDUE RECORDS LIST - A listing of all records which are past due (as established by site parameters) in being returned to their home location.

PENDING REQUEST LIST - A listing of outstanding record requests not yet printed. May be run to include all clinic requests.

RECORDS CHARGED TO A BORROWER - A listing of records currently charged to a specified borrower. Includes \# of days overdue if applicable.

REQUESTS PENDING FOR A BORROWER - A listing of requests pending (as established by site parameters) for a specified borrower.

RETRIEVAL RATE STATISTICS - Provides a breakdown by request status of record requests associated with pull lists and provides a percentage of the number of requests filled.

## Ad hoc Request Response Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ad hoc Request Response Statistics option generates a report of file room response times to individual record requests within a specified date range.

The report pertains to those requests not associated with pull lists and with a status of either CHARGED, CANCELLED, or NOT FILLABLE. Pending requests are not included. It measures the number of minutes between the date/time requested and the date/time a final status was entered. It is sorted by date, request status, and by requesting date/time within each status. Each section of the report will contain the following for each applicable request:

> Request Number

> Patient Name

> Record Type/Volume

> Requestor

> Time Requested/Requesting User

> Time of Status/Responsible User

> \# Minutes (between date/time requested and date/time status was entered)

At the conclusion of each section, the following statistical data will be computed and displayed as appropriate:

> Total (# of minutes)

> Count (# of requests)

> Mean (Average \# of minutes)

> Minimum (# of minutes to respond)

> Maximum (# of minutes to respond)

> Deviation (indicates average fluctuation of responses from the mean - the higher the number, the wider the variation)

It is important to note that dependent upon the size of your database, the amount of requesting activity at your facility and the date range specified, this report may be quite lengthy. You may wish to consider running it during an off-tour.

You will be prompted for a beginning and ending date and a device.

## Charged Records by Home Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Charged Records by Home Location option provides a listing of records assigned to a specified home location (file room) and their current borrowers. It may be run to include ALL records assigned to the home location or just those currently charged out. It may be sorted by borrower, patient name or terminal digit.

For each record listed, the following information will be provided.

> Patient Name

> Social Security

> Record Type/Volume No.

> Record No.

> Current Borrower

> Phone/Room of Current Borrower

> Date/Time charged to current borrower

> \# of Days Overdue (if applicable)

Dependent upon the size of your database and the home location specified, this report may be quite lengthy - particularly if you chose to include ALL records assigned to the home location. You may wish to consider running this report during off hours.

## Inpatient Record Location List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Record Location List option provides a printout listing the location of all records belonging to current inpatients. All inactive as well as transferred out records are included in the report which may be run for all inpatients or for those with admission dates within a specified date range.

The report lists the following for each patient and record:

> Patient Name

> Social Security Number

> Ward Location

> Record \#

> Record Type

> Current Borrower

> Phone/Room of Current Borrower

> Associated Borrower (if applicable)

> Phone/Room of Associated Borrower

## Loose Filing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Loose Filing Report provides a listing of all records in your application for which loose filing exists. Specifically, the records listed will be those for which the Loose Filing Indicator in the Update Record's Attributes option, Transaction Menu, has been set to YES.

The report is sorted in terminal digit order and provides the following information for each record:

> Patient Name

> Social Security Number

> Record Type/Volume

> Record Number

> Name of Borrower to whom record is presently

> charged

> Phone/Room of Borrower

> Date/Time Charged

> Days Overdue (if applicable)

It should be noted that unless a record's loose filing indicator has been subsequently set to NO after the filing has been accomplished, it will appear on this list.

## Missing Records List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missing Records List option generates a listing of records in your application which are either flagged as missing (via the Flag a Record as Missing option, Transaction Menu) or have been found pending supervisor approval. Please refer to the Flag a Record as Missing option of this manual for a detailed explanation of these two statuses, if needed.

The report is sorted alphabetically by patient name with a section dedicated to each record. For each record, the following information is provided:

Patient Name

Social Security Number

Record Type/Volume

Status - either MISSING or FOUND/SUPE

Borrower History - Section listing all past borrowers (unless purged) with the following information:

\- Name of Borrower

\- Date/Time Charged

\- Whether the record was barcoded when charged to borrower

Date/time record was entered as missing

Person entering it as missing

Supervisor Comments (if any)

If the record has been found pending supervisor approval, the following information will also be provided:

Date/Time entered as found

Who entered it as found

Where it was found

User Comments (if any)

## Overdue Records List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Overdue Records List generates a printout of records in your application which are past due in being returned to their home location. It may be run for an institution (division) or home location. If run by institution, all home locations (file rooms) within the institution will be included on the report. You may further select to have the report sorted by borrower, patient name or terminal digit.

For each overdue record, the following will be listed:

> Patient Name

> Social Security Number

> Record Type/Volume

> Record \#

> Borrower

> Phone/Room of Borrower

> Date Charged to Borrower

> \# Days Overdue

The system computes and displays the total number of records overdue at the end of the report. If sorted by borrower, it will compute the total for each borrower as well as a grand total.

Determination of whether a record is overdue is based on site parameters and may vary between record types and movement types. These parameters are defined in the following two fields/options found on the System Definition Menu: OVERDUE RECORD CUTOFF field in the Type of Record Set-up option and the INCLUDE ON OVERDUE REPORT field found in the Movement Type Set-up option. Generally, records which have been inactivated, transferred to another site or flagged as missing are not included on the overdue list.

## Pending Request List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pending Request List option is used to print a list of pending requests for patient's records. Which requests appear will depend on how the Pending Request Cutoff site parameter is set at your facility for each record type. Requests that have been printed will not be displayed nor will any requests for dates past the date the printout is run. The requests are listed in alphabetical. You may include unfilled clinic requests on the report.

At multi-division facilities, the records on the list will be separated by division and displayed under the division with which they are associated.

Information provided on the display includes date of printout, patient name and last four digits of SSN, record type and number, current location, phone and room number of current location, request number, requestor, and date/time record needed. The total number of requests pending is also given.

The institution of the file room from which you are tracking records is automatically displayed after the option is selected.

You will be prompted for whether or not you want to include unfilled clinic requests on the list and a device.

## Records Charged to a Borrower

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Records Charged to a Borrower option is used to display a list of records currently charged to a particular borrower. The selected borrower must be in the BORROWER file. The records are listed in alphabetical order and are separated by record type.

The number (if any) that appears in the "Days Overdue" column of the display depends on how the Overdue Record Cutoff site parameter is set at your facility for each record type. This parameter is set to the number of days this record type may be borrowed from its home file room before being considered overdue.

Information provided in the output includes borrower's name, phone and room number, printout run date, record type, volume number, patient name, date record charged to this borrower and days overdue (if any). If there are no records charged to the selected borrower in the selected application, the system will display a message stating this.

## Requests Pending for a Borrower

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Requests Pending for a Borrower option is used to display a list of pending requests for patients' records for a particular borrower. The selected borrower must be in the BORROWER file. Which requests are displayed in the output will depend on how the Pending Request Cutoff site parameter is set at your facility. The requests are listed in alphabetical order and are separated by record type.

Information provided in the output includes borrower's name, phone and room number, printout run date, record type, volume number, patient name, <span id="RT_2_47_SSN" class="anchor"></span>last four digits of Social Security Number, date/time record needed and associated requests. If the request is part of a pull list, it is indicated as such by an asterisk (\*). If there are no requests pending for the selected borrower in the selected application, the system will display a message stating this.

## Retrieval Rate Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Retrieval Rate Statistics option provides a breakdown by request status of record requests associated with pull lists and provides a percentage of the number of requests filled. Based on the number of record requests and the number charged, the system will compute and display a retrieval rate percentage.

Reports (excluding single pull list) may be generated as detailed or summary. Detailed reports may be further sorted alphabetically or by division. The report may be run for a specified date range, a single day or a single pull list.

Detailed reports and single pull list reports will list the total number of record requests (exclusive of cancelled requests), \# charged, \# cancelled, \# not fillable and \# requested (still pending) for each pull list and a total page. The summary report consists of only the total page.

# System Definition Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below are general items you may wish to consider prior to setting up your application.

- Review the Record Tracking User Manual.
- What records do you wish to track? Only medical records or medical and administrative records? Only master jackets or all types of radiology records?
- What file room(s) do you wish to track records from? Do you wish to track records from inactive file rooms as well as active ones?
- What admitting/imaging areas should be included in your set-up? A Radiology department may have multiple imaging areas (i.e., Ultrasound, Nuclear Medicine, Diagnostic) and wish to track records from these areas separately. If this is the case, each must be defined in your system.
- Do you wish to use the standard label formats which accompany this package or format your own? (Samples of the standard labels may be viewed in the Label Formatter Section of this guide.)
- A major part of the installation process is the definition of record borrowers; i.e., clinics, wards, physicians, clinic clerks, other individuals, other areas, etc. There will probably be a number of borrowers in your system making this a time-consuming effort. It is very helpful if all borrowers are identified prior to commencing with this process.
- If you are installing Record Tracking for the MAS application, attention needs to be given to records which will be requested for clinics and the admitting area. For these areas, you should establish a general rule of thumb as to what records need to be routinely requested; i.e., the latest volume of the patient's medical record. This will be defined through the Application Set-up or Admitting Area Set-up options, as applicable. You should identify those clinics/admitting areas who will need other than the default records. Some clinics may require ALL volumes of a patient's medical record; x-rays may be required; if so, which x-rays should be requested for which clinics?
- As part of the initialization process, the Site Manager will perform a BORROWER INITIALIZATION (using the Borrower Initialization option, Computer Site Manager's Menu). This process looks at the Hospital Location, Ward Location, and NEW Person files, and places all "active" clinics, wards, and persons in the Borrower/File Areas file, making them eligible to become actual record borrowers. It is the first step in initializing borrowers. You may not wish to have ALL of these entries become actual borrowers in the Record Tracking system, however.
- In order to activate them as borrowers, they need to be defined through the Borrower Set-up option, taking into account the above considerations. Although you will have defined DEFAULT RECORDS TO BE REQUESTED through the Application Set-up or Admitting Area Set-up options, it is necessary to define the records needed for each of these types of borrowers when entering them in the Borrower Set-up option.
- Each individual who will be a borrower should also be defined by name through the Borrower Set-up; i.e., ward clerks, clinic clerks, secretaries, etc. As long as these individuals are part of the Person file, they may be activated as borrowers through this option. You may have certain areas of your facility which are not defined in either the Hospital Location, Ward Location or NEW Person files; i.e., Correspondence Unit, Medical Information Section, Details Clerk, etc. In order to enter areas such as these, it is necessary for them to be defined in the appropriate file. See your site manager to accomplish this task.
- How do you wish to handle printing of barcode labels? All at once or as patients report for care? If printed all at once, labels for inactive patients will be included in the run. (The system checks for expired patients and does not run labels for them.) The additional labels printed for inactive patients may outweigh the benefits of having your file room barcoded in the shortest amount of time.
- Who should receive what security keys?

You are now ready to begin defining the parameters for your application. You should begin with File Room Set-up.

> **NOTE:** The first file room must be defined with the site manager using the RT OVERALL Menu. Subsequent file rooms may be defined using the RT MAS/RAD SUPER Menu.

Upon entering the Record Tracking Menu (through RT OVERALL), a prompt for a file room will appear. This prompt should be disregarded (by entering a \<RET\>) as no file rooms yet exist.

## Application Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit application-specific parameters. Prior to defining the parameters in this option, you must have first completed defining parameters in the following System Definition options: File Room Set-up, Label Formatter (if you are not using the standard labels), and Type of Records Set-up.

This option is broken into four major categories. Two of these pertain to both the Radiology and Medical Administration applications; Application Parameter Set-up and Institution Parameters. Two additional categories are included in the MAS application which provide for definition of parameters related to record requests for clinics; Default MAS Record Requests for Clinics and Default Radiology Folder Requests for Clinics that Require Films.

*Field Descriptions{MAS/RAD} Application Parameter Set-Up*

DEFAULT RECORD Enter the type of record the system should initially

CREATION TYPE create for a patient in this application. All records

which have been defined as LINKED RECORDS to

this record type (through Type of Record Set-up) will

also be created.

PROFILE/REPORT This field allows you to specify the heading which

HEADER should appear on the Record Inquiry and Trace

Movement History reports (accessed through the

Record Information Menu). For example, MAS may

wish to enter Consolidated Health Record; Radiology

may wish to enter Film Jacket. If you are using

Record Tracking for other purposes (perhaps a library

setting), you would enter something more appropriate

to that setting.

BORROWER BARCODE Specify the type of barcode label (either the standard

FORMAT or one defined at your site) to be printed for borrowers

associated with this application. It is not necessary to

have barcode labels printed for borrowers in order for

the system to go live.

Application Set-up

*Default MAS Record Requests for Clinics*

Select MAS RECORD Specify the MAS record type(s) which should

automatically be requested for scheduled clinic

appointments to those clinics which require records;

i.e., medical folder.

MAS RECORD Your entry at "Select MAS RECORD" will appear as a

default. You may delete it (by entering \<@\>), enter a

different record type, or accept the default.

VOLUMES NEEDED Enter the volumes which should automatically be

requested for each clinic. Choose from ALL, LAST,

NONE.

*Default Radiology Folder Requests for Clinics that Require Films*

Select RADIOLOGY For clinics which also require films, specify each

FOLDER Radiology record type(s) which should automatically

be requested for scheduled clinic appointments. For

each entry in this field, the following two fields will

be prompted.

RADIOLOGY Your entry at "Select RADIOLOGY FOLDER" will

FOLDER appear as a default. You may delete it, enter a

different one, or accept the default.

VOLUMES Enter the volumes of this record type which should

NEEDED automatically be requested for each clinic. Choose

from ALL, LAST, NONE.

Application Set-up

*Institution Parameters*

Select INSTITUTION Enter the main institution name, number or

station number (from your Institution

file) associated with this application.

INSTITUTION Your entry at "Select INSTITUTION" will appear

as a default. If incorrect, you may select another

institution.

CENTRAL FILE ROOM Enter the central file room associated with this

application and institution. The system only allows

file rooms associated with this application and

institution through File Room Set-up.

DEFAULT PULL Specify the method by which pull lists should be

LIST SORT sorted for this application. Choose from:

'T'ERMINAL DIGITS

'C'LINIC NAME THEN TERMINAL DIGITS

'A'PPOINTMENT TIME

'H'OME LOCATION, THEN TERMINAL DIGIT

'D'ETAILED-HOME LOC, CLINIC, THEN TERMINAL DIGIT

Application Set-up

*Record Type Parameters Within {INSTITUTION}*

For each record type defined, define the following fields.

Select TYPE Enter each record type associated with this

OF RECORD application for this institution. For each entry made

in this field, the following three fields will be

prompted, returning you to this prompt upon

completion.

TYPE OF Your entry at "Select TYPE OF RECORD" will

RECORD appear as a default. You may accept the default,

enter the correct record type, or delete it.

DEFAULT Enter the home location the system should assign

HOME LOCATION to records when they are created initially. Generally,

this will be a file room. For example, you may wish

to enter your main MAS file room as the home location

for medical and administrative records.

DEFAULT Enter the borrower (from Borrowers/File AREA

INITIAL file) the system should automatically charge a record

BORROWER to when it is initially created for this application.

For example, if a patient's administrative and medical

folders are initially created by your Admitting area,

you may wish to assign the Admitting area as the

DEFAULT INITIAL BORROWER.

Application Set-up

*Clinic Initialization Request Parameters*

EXCLUDE Yes/No Set to yes if you wish to exclude in-

INPATIENTS patients with clinic appointments from pull lists.

Select EXCLUDE Any appointment type in the APPOINTMENT

APPOINTMENT TYPE file (#409.1) may be entered and

TYPES appointments for these types will not

appear on clinic pull lists.

CREATE RECORDS- Yes/No Set to NO if you do NOT wish to have a

CLINIC REQUESTS request, pull list and record created if a clinic

appointment is made for a patient with no record.

DEFAULT Borrower/File Area entry If this field contains a

SCHEDULED borrower, the Clinic Initializer will create a pull list

ADMISSIONS from entries in the SCHEDULED ADMISSION file.

Any entry in the SCHEDULED ADMISSION file that

does NOT have a corresponding ward or treating

specialty in the BORROWERS file will appear on this

*Record Retirement Parameters*

DEFAULT When records are charged out, they will be

RETIREMENT "inactivated" to this borrower with a movement type of

BORROWER TRANSFER RETIRE. The borrower entered here will show as the

default borrower at the "Select Record Retirement Borrower:" prompt in

the Charge Out/Transfer Retirement Pull Lists option of the Inactivate

Records Menu. Only borrowers from the BORROWERS/FILE AREA

file may be entered. This borrower will usually be a "federal record

center".

DEFAULT The record type that should be created when records are retired. The

PERPETUAL record type entered here will appear in the “Do you want to create

RECORD '{record type}' records from Pull list? Yes//" prompt in the Charge Out/

Transfer Retirement Pull Lists option of the Inactivate Records Menu.

## File Room Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit and define/update parameters for the file rooms in your application and associate them with the correct institution. Entries made here go into your HOSPITAL LOCATION file (#44) and are assigned a type of "F". They also become part of your Borrowers/File Areas file (#195.9). This option operates the same for both MAS and Radiology applications.

> **NOTE:** The first file room must be defined by the site manager using the RT Overall Menu. Subsequent file rooms may be defined using this option.*Field Descriptions*

Select File Room Enter the name of the file room. Multiple file rooms

may be entered for an application. For each file room

entered, the following fields will be prompted,

returning you to this prompt for subsequent entries.

You should enter all file rooms in your application

which will be associated with Record Tracking.

ARE YOU ADDING YES/NO - This will only be prompted if your entry

(File Room) AS at "Select File Room" was new.

A NEW HOSPITAL

LOCATION?

PHONE \# Enter the telephone number of the file room;

1-15 characters in length.

LOCATION/ROOM \# Enter the location/room \# of the file room.

RECORD SORT Enter the method by which this file room sorts

its records. Choose from:

'A'LPHA (Sorts records alphabetically)

'T'ERMINAL DIGITS (Sorts records by terminal digit of

social security number)

ACTION IF HOME Specify which action should be taken when the

IS DIFFERENT home file room of a record selected for transaction is

different from the one the user is associated with; i.e. a

radiology folder is selected for check-in to the MAS file

room. Choose from:

'N'O ACTION

'A'UTOMATICALLY CHANGE

'Q'UESTION THE USER ABOUT CHANGE

'D'ISPLAY WARNING ONLY

File Room Set-up

*Hospital Location File Parameters*

NAME Your entry at "Select File Room" will appear as a

default. You may rename the file room (answer must

be 2-30 characters in length) or accept the default by

entering \<RET\>. Unless you hold the necessary

FileMan access, you will be unable to delete a file

room. See your site manager if it is necessary to delete

a file room.

INSTITUTION Enter the institution number, name or station number

(from your Institution file) with which this file

room is associated.

## Type of Record Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter and define parameters for the record types associated with this application. This option operates the same for both the MAS and Radiology applications.

*Field Descriptions*

Select Record Type Enter the record type you wish to define. This is a

multiple field. For each entry in this field, the

following fields will be prompted, returning you to this

prompt until no more entries are made. You

should enter each record type (i e., medical,

administrative, master jacket, etc.) associated with

your application which will be tracked.

ARE YOU ADDING YES/NO - This will only be prompted if your entry

{Record/Type} AS at "Select Record Type" was new.

A NEW RECORD TYPE?

NAME Your entry at "Select Record Type" will appear

as a default. You may rename the record type (must

be 3-30 characters), delete it along with all associated

parameters by entering \<@\>, or accept the default.

ABBREVIATION Enter an abbreviation (if any) by which this record

type is known. Answer may be 1-3 characters in

length.

CAN RECORD BE YES/NO - Should users be allowed to enter

REQUESTED? requests for this record type?

IS RECORD YES/NO - If YES, record can only be charged

TEMPORARY out once.

ASK FOR CONTENT YES/NO - Should user be prompted to enter a

DESCRIPTOR? description of the contents of this record type

when it is created for a patient. This description

will be displayed beneath the record on record

inquiry.

Type of Record Set-up

MULTIPLE VOLUMES YES/NO - Can there be more than one volume

ALLOWED of this record type per patient?

DESCRIPTION Enter a description of the record type.

INQUIRY Specify (numerically) the order in which

DISPLAY ORDER this record type should appear on the record

inquiry. For example, specify 1 to have it appear

first; 2 to appear second, etc.

INACTIVATION Specify a date on which users will no longer be

DATE able to create this record type. After this date, it will

no longer be possible to create records of this type;

however, existing records will remain until they are

inactivated through the Inactivate/Reactivate Records

option. Leave blank if you wish no inactivation date.

*Label Format Specifications*

RECORD LABEL Specify the record label type (the standard or one

FORMAT defined at your site) which should be used for printing

labels associated with this record type.

REQUEST Specify the label type which should be used when

NOTICE FORMAT request labels are printed for requests of this record

type (as defined through Label Formatter).

*Cutoff/Purge Parameters*

PENDING Specify the number of days an unfilled request for

REQUEST CUTOFF this record type may remain in the system and

(days) considered pending before reverting to a status of

unfilled.

OVERDUE Specify the number of days this record type may

RECORD CUTOFF be borrowed from its home file room before being

(days) considered overdue and appearing on the Overdue

Records List.

Type of Record Set-up

BARCODE RENEWAL Specify the number of days required to consider

CUTOFF (days) reprinting a barcode label. This value is used to

determine if new barcodes should be printed with pull

lists. The date barcode last printed is compared with

this value and a new barcode is printed if it is "old". A

null value will disable printing barcodes with pull

lists.

PENDING CHECK-IN Specify the number of days a pending request will

CUTOFF (days) be displayed for a record when the record is being

checked-in. If not set, records with pending requests

are flagged depending on the PENDING REQUEST

CUTOFF parameter. If ZERO, pending requests will

not be flagged.

RETIRE RECORD Specify the number of days required for a record to

CUTOFF (days) have no activity before it is considered for retirement.

When record retirement pull lists are generated,

records with no activity for this amount of time are

added to the pull lists.

CURRENT This field is used to specify the earliest future

BORROWER date/time (in minutes) the current borrower of a

FUTURE REQUEST record may request that same record for the future.

TIME For example, Medical Clinic has Mr. Jones’ record

MINIMUM (minutes) today for an appointment and will be seeing him

again tomorrow. Should Medical Clinic request the

record for tomorrow or retain it in the clinic? In

making an entry in this field, you should consider your

entry at the previous prompt, OVERDUE RECORD

CUTOFF.

\# PREVIOUS Enter the number of previous movements

MOVEMENTS (i.e., charge-outs, check-ins, etc.) which should be

TO RETAIN retained for this record type. This is the number of

movements which will be shown on the Trace

Movement History, useful in searching for lost records.

Type of Record Set-up

REQUEST PURGE Enter the number of days requests (filled and

CUTOFF (days) pending) should be retained in the system (and

therefore displayed upon access) before being purged.

PULL LIST Enter the number of days pull lists should

PURGE CUTOFF (days) remain in the system before being purged.

OK TO PURGE YES/NO - It is advisable that an entry of NO be

DATA? made to this field until you are actually ready to begin

purging of data.

*Missing Record Control Parameter*

CONTROL OF If a record of this type is flagged as missing, who

FINDING RECORDS may remove the flag? Choose from:

'F'ILE ROOM SUPERVISOR ONLY (must hold FR

SUPERVISOR key)

'A'NY USER

*Other Records to Create When Initializing the {Record Type}*

Select LINKED Specify other record types (if any) which should

RECORDS also be created when this record type is initially

created for a patient. For example, you may wish to

have an administrative folder created when the

patient's first medical folder is created. The record

type specified must be defined in your application.

*File Rooms Allowed to Store {Record Type}*

Select FILE Specify the file room(s) (as defined in File Room

ROOM Set-up) which may store this record type. You will

return to this prompt repeatedly and should specify

ALL file rooms which will be storing this record type.

## Reasons File Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit allowable reasons for cancelling requests and missing records and associate them with the function for which they may be used. For example, you may wish to enter "Not Charged Out" as an allowable reason for a missing record. Entries made through this option will become part of your REASONS file (#195.6).

*Field Descriptions*

Select REASON Enter new or existing reason. This is a multiple field.

For each entry made in this field, the following fields

will be prompted, returning you to this prompt at

completion.

ARE YOU ADDING YES/NO - This will only be prompted if your entry

{Reason} AS A at "Select REASON" was new.

NEW REASON?

NAME Your entry at "Select Reason" will appear as a

default at this prompt. You may rename the reason,

delete it and all associated parameters, or accept the

default.

TYPE OF REASON Enter the function with which this reason is to be

associated. Choose from:

'C'ANCEL REQUEST - limits use of this reason to cancelling requests.

'M'ISSING RECORD - limits use of this reason to missing records.

'G'ENERAL - allows the reason to be used anywhere.

DESCRIPTION You may enter a free text explanation of the reason.

## Label Functions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Label Formatter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows design of your own barcode label formats. It is an optional step in the installation process as three standard label formats are included in the Record Tracking package (record, request, and borrower). Examples of the standard labels which accompany this package as well as a list of selectable fields for each label type format may be found at the end of this option documentation. It is recommended you use the standard label formats, as design of label formats is somewhat precarious. UNDER NO CIRCUMSTANCES SHOULD THE EXISTING STANDARD LABEL FORMATS BE EDITED.

Below is additional information on answering key prompts.

*Select FIELD*

Enter the name of the field corresponding to the first bit of information which will appear on the label. For each entry made at this prompt you will subsequently be prompted for a row, column, and title, returning to this prompt repeatedly until no more entries are made. Even though you are subsequently prompted for location of the information, it is important that actual entry be made in the order it will appear on the label. In some instances, failure to do so may result in an error in your format. In order to have the barcode printed on the label, you should select BARCODE FOR RECORD as a field. It is advisable that this be your last selection. The list of selectable fields will vary depending upon whether you are defining a record, borrower, or request label. You may enter a \<?\> at this prompt for a list of fields applicable to your label.

*NUMBER OF ROWS IN FORMAT*

Enter the total number of rows in your format. You should account for blank lines in your total. If you specified BARCODE FOR RECORD as one of your fields, increase your total by one. If you wish to include blank lines between the last line of data and the beginning of the barcode, enter a number correspondingly higher to the number of line feeds you desire. An error in your format will result if the number entered at this Step is too low to provide space for all the information specified.

Please follow the instructions closely, as failure to do so may result in an error in your format. At the conclusion of formatting, a sample will be displayed on the screen. No barcode will be shown. In order to actually test the label format with a barcode, you should use the Test Label Formatter option.

Label Functions Menu*Label Formatter*

Editing of your site-specific label format specifications is risky. It editing is necessary, it is recommended you delete the label format and begin again.

Compiled logic of the label format specified may be viewed through FileMan by inquiry to the Label Format file (#194.4).

Following is a list of selectable fields for each label type format.

<u>RECORD LABEL</u> <u>REQUEST LABEL</u> <u>BORROWER LABEL</u>

AGE AGE BARCODE FOR BORROWER

BARCODE FOR RECORD BARCODE FOR RECORD BORROWER'S LOCATION

CLAIM NUMBER BARCODE FOR REQUEST BORROWER'S PHONE

CURRENT DATE/TIME CLAIM NUMBER CURRENT DATE/TIME

DATE OF BIRTH CURRENT BORROWER/LOCATION FREE TEXT

FREE TEXT CURRENT DATE/TIME NAME

HOME LOCATION CURRENT PHONE \#

NAME CURRENT ROOM \#

RECORD \# DATE OF BIRTH

SERVICE CONNECTED FREE TEXT

SEX HOME LOCATION

SSN NAME

TYPE OF RECORD RECORD \#

VETERAN REQUEST \#

VOLUME NUMBER REQUEST COMMENT

REQUESTED DATE/TIME

REQUESTING USER

REQUESTOR

REQUESTOR'S INSTITUTION

REQUESTOR'S LOCATION

REQUESTOR'S PHONE

SERVICE CONNECTED

SEX

SSN

TYPE OF RECORD

VETERAN

VOLUME NUMBER

Label Functions Menu

### Test Label Formatter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Test Label Format option is used to print a label format with the barcode. The Label Formatter option allows design of barcode label formats but when generated no barcode is shown. This option should be used to test the label format with the barcode.

## Borrower Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter and define/update parameters of specific borrowers and associate them with the correct institution. As discussed in the overview of this section, you will need to define EACH borrower through this option. Please refer to that overview for further clarification. This option may also be used to revoke or inactivate a borrower's privileges.

*Field Descriptions*

Select Borrower Enter the borrower (from Borrowers/File Areas

File) for which you wish to define parameters. This is

a multiple field. For each entry made into this field,

the following three fields will be asked, returning you

to this prompt upon completion.

PHONE \# Enter borrower's phone number.

LOCATION/ROOM# Enter borrower's location or room \#.

BORROWING Enter borrower's borrowing privileges. Choose from:

PRIVILEGES

'N'ORMAL

'I'NACTIVATED

'R'EVOKED

*Hospital Location File Parameters*

NAME Your entry at "Select Borrower" will appear as a

default at this prompt. You may rename the borrower

or accept the default. Unless you hold the proper

FileMan access, you will be unable to delete a

borrower. See your site manager should this be

necessary.

INSTITUTION Enter the institution name, number or station number

this borrower is associated with.

Select SYNONYM You may enter a synonym for the borrower, if you

wish; i.e., GEN MED for General Medical clinic.

Borrower Set-up

The next four parameters will appear if the borrower is an admitting area/clinic in the MAS application or a file room/imaging area in the Radiology application.

*Record Request to be Made When Making an Appt or Registering a Pt*

REQUESTS FOR Enter the borrower's name to be associated with

WHICH BORROWER requests. Default will be your entry at "Select

Borrower".

ARE RECORDS YES/NO When appointments are scheduled in

REQUIRED? association with this borrower, are records required?

If YES, you will proceed through the next three

prompts.

Select RECORD Enter each record type which is needed in

TYPE NEEDED association with these appointments.

VOLUMES Enter what volumes of this record type will be

REQUIRED needed for scheduled appointments. Choose

from ALL, LAST, NONE.

*Scheduled Admissions Borrowers*

SCHEDULED YES/NO If YES, when an entry in the

ADMISSION SCHEDULED ADMISSIONS file has a type

BORROWER WARD and the ward location matches this

ward location borrower, a pull list will be

created for this ward location borrower

or associated borrower.

TREATING BORROWER/FILE AREA entry - If an entry in

SPECIALTY the SCHEDULED ADMISSIONS file has a type

TREATING SPECIALTY and the treating

specialty matches this borrower's treating

specialty, a pull list will be created for this

borrower or associated borrower.

## Print Borrower Barcode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print borrower barcode labels. The label printed will be the label type specified for borrowers in your Application Set-up.

You will be prompted to select a borrower. If the borrower selected appears in your Borrowers/File Areas file, the system will accept your entry and either display a message informing you the barcode label has been queued to print on your default device, or prompt you to select a device on which to print, depending upon the specifications outlined at your particular site. You may either select another borrower or enter a \<RET\> to return to the menu.

## Movement Type Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to change the parameters for the various movement types in your application. The option will operate the same for both the MAS and Radiology applications. Movement types may not be deleted.

*Field Descriptions*

Select MOVEMENT Enter the movement type you wish to define. You

TYPE may choose from a list of established movement types

for your application. Enter a \<?\> for a list.

NAME No editing allowed. Enter a \<RET\> to continue or \<^\>

to return to the first prompt.

DISPLAY MESSAGE Enter a message (if any) you wish to have displayed

when this movement type is taking place.

INCLUDE ON YES/NO - Should records involved in this movement

OVERDUE REPORT type be included on the Overdue Records Report?

# Inactivate Records Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Inactivate Records Menu is to perform record retirement tasks. Many options on this menu are similar or even identical to options in other menus; however, their purpose here is specific to record retirement.

Through this menu, record retirement pull lists are created and printed. Any records on the list that should not be retired are designated as not fillable. If there was a record on the list that did not actually exist, that record would be deleted. You would then create a perpetual record for each record on the pull list. The perpetual record would hold summary information you wish to retain once the record is retired. When all exceptions have been taken, the pull list is charged out or transferred. Records on the list are inactivated and transferred to the appropriate facility.

Below is a descriptive listing of the options on this menu.

Generate Record Retirement Pull Lists - Used to create record retirement pull lists. These pull lists are generated by scanning record movements. If there has been no movements within the record retirement window (number of days entered in the RETIRE RECORD CUTOFF field) and the record does not have a reason not to retire field set, a request for the record is added to the pull list.

Print Record Retirement Pull list - Used to print record retirement pull lists. Record retirement pull lists are used to find records to be retired and transferred to a record archive center, and as a guide for creating the perpetual record that is retained from the retired records.

Designate Retirement Requests As 'Not Fillable' - Used to designate requests on record retirement pull lists as not fillable (records you do not wish to retire). Requests with a status of not fillable may also be changed to requested through this option.

Delete a Record - Used to delete records in the Record Tracking system. Records are deleted when volumes are combined or when the actual corresponding record does not exist.

Create a Label/Record/Volume - The purpose of this option under the Inactivate Records Menu is to create a perpetual record in the Record Tracking system. A perpetual record is created to hold information you wish to retain when a record is retired.

Charge Out/Transfer Retirement Pull Lists - Used to charge out record retirement pull lists. The records will be inactivated and transferred to the appropriate facility for retired records.

Inactivate/Reactivate Records - Used to render a record unavailable/available. Inactivation of a record makes it unavailable to other users to request, charge-out, check-in, re-charge, etc.

PULL LIST FUNCTIONS MENU - See the Pull List Functions Menu Section.

## Generate Record Retirement Pull Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generate Record Retirement Pull Lists option is used to create record retirement pull lists. These pull lists are generated by selecting a range of terminal digits or by file number. Limiting the range by terminal digit is used to allow more manageable lists to be produced with the initial implementation. Later the job can be tasked to run periodically at a convenient interval.

A Record Retirement Profile is compiled and displayed, and you are given the opportunity to enter or edit the "Record Type Retirement Parameters" and the "Overall Retirement Parameters."

The OK TO RETIRE RECORDS? field must be set to YES in the record type parameters in order for the selected record type to be included on the pull list. No list is generated until the same field is set to YES in the overall parameters.

The pull list is generated by scanning the movements of records. If there has been no movements within the record retirement window (number of days entered in the RETIRE RECORD CUTOFF field) and the record does not have a reason not to retire field set, a request for the record will be added to a record retirement pull list.

The pull list names are created from the current location of the record and the first day of the next month; or, if there is no current location, the home location and the first day of the next month. If there is no current location or home location, a pull list is created with the name "unknown". The date is used only to combine lists and has no other significance.

## Print Record Retirement Pull List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option works much the same as the Print Pull List(s) option under the Pull List Functions Menu; however, only record retirement pull lists are printed. A pull list number is automatically assigned to every pull list created. Record retirement pull lists are used to find records to be retired and transferred to a record archive center, and as a guide for creating the perpetual record that is retained from the retired records.

Pull lists will generally be sorted by terminal digit or name. Other sorts are available but don't have much function for record retirement pull lists.

Pull lists may be printed to include all requests, a short non-fillable list, a detailed non-fillable list or only updates to the list. Updates are requests that were added after the entire pull list was last printed. If you chose to sort by clinic name - appointment type, you can only print to include all appointments or a short non-fillable list.

The pull list status (requested, charged, cancelled) will only appear on clinic pull lists that are sorted by other than terminal digit. The status of a pull list may be Requested even though the status of each request on that list is Charged. This may occur if the requests were filled through the Fill a Request option of the Request Records Menu. The status of the pull list will not change from Requested to Charged or Cancelled until the Charge Out Pull List Records or Entire Pull List Cancellation options are utilized.

Record borrowers may wish to use this option to view charged out pull lists to determine which requests were not fillable.

## Designate Retirement Requests as ‘Not Fillable”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to designate requests on record retirement pull lists as not fillable (for records you do not wish to retire). Requests with a status of not fillable may also be changed to requested through this option.

Requests designated as not fillable will still appear on the Pending Request List, the Requests Pending for Borrowers List, and will also still appear as pending requests under the Request a Record option.

When selection is made by entering a patient's name, the system displays a patient profile and lists the patient's requestable records in that application (MAS or Radiology). After the record is selected, a request profile will be displayed for that record listing the requests which may be chosen. The user may designate a single request, multiple requests or a range of requests for each patient selected.

If the request is selected by entering the request number or by wanding the request barcode label, only the data associated with that particular request will be displayed.

## Delete a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete a Record option is used to delete a record. Records are deleted when volumes are combined or when the actual corresponding record does not exist. If a record cannot be located or should not be retired, the request should be made "not-fillable" through the Designate Retirement Requests as 'Not Fillable' option.

The system only allows deletion of most recent volumes of a record set; therefore, you will not be able to delete Volume 2 of a 6 volume set. Record entry may be made either by wanding the barcode label or entering the patient's name. Prior to deleting the record, you will be given the opportunity to move requests to the next lower volume number of the record type being deleted.

When a record is deleted, all associated requests for the record, missing record log entries and movement history log entries are also deleted. A MailMan message will be generated advising that the record has been deleted. This message goes to the same mail group that receives messages on missing/found records.

## Create a Label/Record/Volume

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create a Label/Record/Volume option may be used to create all record types; however, the purpose of this option under the Inactivate Records Menu is to create a perpetual record in the Record Tracking system. This documentation addresses only perpetual records.

A perpetual record is created to hold information you wish to retain when a record is retired. Multiple volumes would not usually be allowed for this record type. This would be defined through your site's parameters. A record identifier number will be assigned for each record created.

This option may also be used to print existing barcode labels.

If your response was YES to the "Do you want to use the file room's default devices? No//" prompt upon entering the Record Tracking software and default printers were defined for the file room you selected, labels you print through this option will print to those default printers. If you answered NO or if no printers were defined, you may be prompted to select a device.

## Charge Out/Transfer Retirement Pull Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to charge out record retirement pull lists. The records will be inactivated and transferred to the appropriate facility for retired records. You will first be given the opportunity to designate any request that you do not wish to charge out as not fillable.

You may select a borrower (from your BORROWERS/FILE AREA file) to which you wish the record to be inactivated. The record will be inactivated with a movement type of TRANSFER RETIRE to the selected borrower. In addition, you may create a perpetual record from the pull list. A default borrower and perpetual record type may be defined through the Record Retirement Parameters in the Application Set-up option of the System Definition Menu.

This option may be used to change the status of requests from NOT FILLABLE to REQUESTED.

This option works the same as the Charge Out Pull List Records option of the Pull List Functions Menu. You may see prompts such as "Do you want to charge out records to a holding area? No//" which may not apply to retirement procedures.

## Inactivate/Reactivate Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inactivate/Reactivate Records option is used to render a record unavailable/

available for transaction within the Record Tracking system. It may be used when records are retired, or perhaps in those instances when it is necessary for a borrower to retain a record for an extended period of time (i.e., for research purposes). Such a record will not appear on the Overdue Records List.

Inactivation of a record makes it unavailable to other users to request, charge-out, check-in, re-charge, etc. It will, however, appear on the Record Inquiry option of the Record Information Menu as inactive.

Records may be inactivated as well as reactivated through this option. If you choose to inactivate the record, you will be prompted for a borrower to which the record should be inactivated. Your entry at this prompt may be a borrower who will be retaining the record for an extended period or your file room.

If you are retiring the record and wish to transfer it to the appropriate Record Processing Center, use the Transfer Records option of the Transaction Menu.

When a record is reactivated, it is automatically charged to the location associated with the user performing the reactivation; usually, its home file room.

Following selection of movement type and borrower (if applicable), you will be prompted to select the record. The system will only allow you to select a record appropriate to the movement type selected. In other words, you will not be permitted to inactivate an already inactive record. If record selection is made by entering the patient's name, only those records appropriate to the movement type selected will be displayed on the patient's Short Record Inquiry.

Multiple records may be entered during a session. Dependent upon the number entered and your site's parameters, they will either be inactivated/reactivated upon exiting the option or queued for action later.

## Pull List Functions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for these options may be found in the Pull List Functions Menu Section of the Record Tracking User Manual.

# Computer Site Manager’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to defining overall site parameters for Record Tracking, be sure all devices to be associated with Record Tracking are defined in your DEVICE file (#3.5). Determine who needs to receive bulletins regarding missing records and build a MISSING RECORD mail group. Prior to assigning menus to users, the DIVISION field of the NEW PERSON file (#200) must be defined for each user of Record Tracking. If you need to define a second request printer, see the Overview of the Initialization submenu contained in this menu for instruction.

Below is a brief description of the options contained in this menu.

ADMITTING AREA SET-UP (SITE MGR) - Used to enter/update barcode printers and input devices for each admitting area defined.

APPLICATION SET-UP (SITE MGR) - Used to customize the appearance of certain prompts and headers and associate them with the correct file for your application.

FILE ROOM SET-UP (SITE MGR) - Used to define printers, input devices and security keys for each file room.

FILE ROOM/REMOTE SET-UP (SITE MGR) - Used to define the domains, remote printers, mail groups and mail routing symbols for transmission of remote record requests or notice of transfers to other VA medical centers.

IMAGING AREA SET-UP (SITE MGR) - Used to enter/update barcode printers and input devices for each imaging area defined.

INITIALIZATION MENU - Contains all the options used by the site manager to set up the system prior to going live.

PURGE DATE - Used to purge pull list, requests, and movement logs data.

RE-COMPILE TEMPLATES - Allows Record Tracking templates to be recompiled on each CPU after running an init.

RECORD TRACKING SYSTEM OVERALL PARAMETERS - Used to define parameters used by all applications as well as some specific to the Radiology and MAS applications.

## Admitting Area Set-up (Site Mgr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/update barcode printers and input devices for each admitting area defined.

*Field Descriptions*

Select Admitting Enter the name of the admitting area being

Area defined/updated. This is a multiple field. For each

entry in this field, the following two fields will be

prompted, returning you to this prompt upon

completion. You should enter and define parameters

for each admitting area to be associated with your

application.

RECORD Enter the printer from your DEVICE file which will

BARCODE be used to print record barcode labels for this

PRINTER admitting area.

Select INPUT Enter the input devices which will be used to input

DEVICES data from this admitting area. This is a multiple field.

Entries at this prompt are optional; however, it is

recommended that devices be entered to prevent

routine users in these areas from being prompted for

their admitting area each time they sign into Record

Tracking.

## Application Set-up (Site Mgr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to define security key parameters, specify which mail group is to receive bulletins of missing records, customize the appearance of certain prompts and headers and associate them with the correct file for your application.

*Field Descriptions{MAS/RAD} Application Parameter Set-Up (Site Mgr)*

APPLICATION The current application will appear as a default. You

may rename it at this prompt, if you wish. You may

not change to a different application from this prompt.

Select SYNONYM Enter a synonym (3-30 characters) by which this

application may be known. For example, MAS for

Medical Administration Service.

SERVICE Enter the service (from service list) which is associated

with this application.

*Entity Parameters*

The Entity Parameters allow Record Tracking to be tailored around any application you chose. You may change the wording of application specific prompts to suit the needs of your application.

ENTITY SELECT This is used to enter the wording you wish to

PROMPT appear at entity select prompts. For example, the

MAS application may wish to enter PATIENT;

Radiology may wish to enter FILM. Thus "Select

PATIENT" or "Select FILM" would appear at each

entity prompt.

ENTITY DISPLAY This is used to enter the wording you wish to

HEADING appear on application specific headings. For example,

MAS may wish CONSOLIDATED HEALTH RECORD

to be displayed.

Application Set-up (Site Mgr)

Select ENTITY FILE Enter the name of the file in which the system

should search in accessing the entry at the entity

select prompt. For instance, if PATIENT was entered

at the entity select prompt, more than likely PATIENT

would be entered at this prompt to associate entries

with the PATIENT file.

*Borrower Parameters*

BORROWER SELECT This field may also be used to change the wording

PROMPT of the "Select Borrower" prompt. For example,

Radiology may wish to enter REVIEWER, thus "Select

REVIEWER" would be prompted.

Select BORROWER Enter the file which is to be associated with the

FILE entries made at borrower select prompts; i.e., ward,

institution, hospital location, new person. This is a

multiple field. You may enter more than one file to be

associated with the borrower select prompts. For each

entry, the following three fields will also be prompted,

returning you to this prompt upon completion.

ASK PHONE/ROOM YES/NO When this borrower is selected, should

users be prompted to update their phone/room?

ASK FOR YES/NO When borrowers are selected from this

ASSOCIATED file should users be prompted to enter an

BORROWER associated borrower? For instance, you may wish to

use this in the case of a ward being a borrower. You

may have users enter an individual's name as an

associated borrower.

SHOW CHARGED YES/NO When a borrower from this file is

RECORDS selected, should the system display all records

currently charged to that borrower?

Application Set-up (Site Mgr)

*Miscellaneous Parameters*

FILE ROOM Enter the appropriate staff key associated

STAFF KEY with this application. Choose from:

RT MAS-FR-STAFF

RT RAD-FR-STAFF

FILE ROOM Enter the appropriate file room supervisor key

SUPERVISOR KEY associated with this application. Choose from:

RT MAS-FR-SUPERVISOR

RT RAD-FR-SUPERVISOR

MISSING RECORD Enter the mail group which is to receive

MAIL GROUP bulletins of missing and deleted records.

CLINIC REQUESTS Enter the name of the mail group which

MAIL GROUP should receive the bulletin advising the Clinic

Initialization background job has run. This job may

be set to run daily through your Record Tracking

System Overall Parameters option to interface all

scheduled clinic appointments with record

requests/pull lists.

CANCELATION How you want the file room to be notified when

BULLETIN a record request is cancelled?

0 - not notified

1 - by bulletin to a mail group

2 - by printing bulletin on the file room's request printer

3 - both 1 and 2

CANCELATION If cancellation bulletin was selected at previous

MAIL GROUP prompt, the name of the mail group to receive bulletin.

TERMINATED Yes/No If set to YES and a user is terminated on

BORROWERS the system, the borrowing privileges of that user will

be revoked when the Clinic Request Initialization

Task runs at night.

CANCEL REQUESTS Yes/No If the previous parameter is set to YES

and this parameter is set to YES, all pending requests

for records by the terminated borrower will be

cancelled when the Clinic Request Initialization Task

runs at night.

## File Room Set-up (Site Mgr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to define printers, input devices and security keys for each file room associated with the respective applications. Assigning devices by file room allows file rooms to be assigned on entry to Record Tracking menus without requiring user selection.

*Field Descriptions*

Select FILE Enter the name of the file room for which you are

ROOM defining/updating parameters. This is a multiple

field. For each entry made, the following fields will

also be asked, returning you to this prompt upon

completion. You should enter each file room

previously defined.

*Printers Assigned to this File Room*

RECORD BARCODE Enter the printer from your Device file on which

PRINTER record barcodes are to be printed for this file room.

REQUEST NOTICE Enter the printer from your DEVICE file on which

PRINTER request notices should be printed. If more than one

device is required, see the overview of this section.

MANAGEMENT Enter the printer from your DEVICE file on which

REPORT PRINTER management reports should be printed for this file

room.

File Room Set-up (Site Mgr)

*CRTs Assigned to this File Room*

Select Enter the input devices from your DEVICE file

INPUT DEVICES which will be inputting data from this file room. Input

devices allow the system to determine the file room

when entering a record tracking option.

This function includes virtual devices; i.e.,

DECservers. Every device must have an entry in the

DEVICE file and the entry must be unique if there are

multiple file rooms. In the case where there is only

one file room, the LTA generic device entry may be

used.

*Security Key Needed to Select File Room*

WHICH SECURITY This field is used to secure a file room so that only

KEY IS NEEDED holders of the designated security key may enter

this file room as a borrower of a record. Choose from:

RT MAS-FR-STAFF

RT RAD-FR-STAFF

## File Room/Remote Set-up (Site Mgr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to define the domains, remote printers, mail groups and mail routing symbols for transmission of remote record requests or notice of transfers to other VA medical centers. When a request for records from another VAMC is generated, a bulletin will be sent by network mail to that site using the domain, request notice printer, and/or remote mail group for that site. If both the mail group and printer are defined, the bulletin will be sent to both. If neither are defined, the bulletin will not be sent to the remote site; however, it will be delivered locally to the user making the request.

A profile of known entries is displayed on entering the option for reference.

*Field DescriptionsRemote Institution Parameters*

Select INSTITUTION Enter the name of the remote institution for which you

are defining/updating parameters. For each entry

made, the following fields will also be asked, returning

you to this prompt upon completion.

DOMAIN Enter the valid DOMAIN file entry for the remote

institution.

REQUEST NOTICE Enter the printer from the remote site's DEVICE

PRINTER file where the system will print requests for records.

REMOTE MAIL Enter the name of the mail group (1-30

GROUP characters) at the remote site which will receive the

record request bulletin.

MAIL ROUTING Enter the standard mail routing symbol. It is not

SYMBOL used by network mail but is included for use with non-

electronic mail.

## Imaging Area Set-up (Site Mgr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/update barcode printers and input devices for each imaging area defined.

*Field Descriptions*

Select Reception/ Enter the name of the reception/viewing area being

Viewing Rack Area defined/updated. This is a multiple field. For each

entry in this field, the following two fields will be

prompted, returning you to this prompt upon

completion. You should enter and define parameters

for each imaging area to be associated with your

application.

RECORD Enter the printer from your DEVICE file which

BARCODE will be used to print record barcode labels for

PRINTER this imaging area.

Select INPUT Enter the input devices which will be used to

DEVICES input data from this imaging area. This is a multiple

field. Entries at this prompt are optional; however, it

is recommended that devices be entered to prevent

routine users in these areas from being prompted for

their imaging area each time they sign into Record

Tracking.

## Initialization Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initialization of records and borrowers is a very important phase to the initial installation process of Record Tracking. Several things need to be considered prior to embarking on this phase.

*Records Initialization/Printing of Barcode Labels*

Do you wish to print barcode labels for your entire database all at once? All inactive patients will be included; expired patients will not.

Patients with multiple volumes will need to be identified and those additional volumes created in the system later with barcode labels printed. The labels generated by the initialization process should be placed on Volume 1 since this is the volume with which the system will associate those labels.

You should use high quality labels that are large enough to allow white space (about 1 inch) around the barcode itself. It is recommended you use 2 15/16" X 5" labels.

Placement of the labels on records jackets is important. To minimize the chances of labels peeling back, placement should be as close to the center of the jacket as possible.

Record Tracking allows two Request Notice Printers and/or two Record Barcode Printers to be set up for a file room. To implement this, create two devices with the same names, ending the device name with "RTHG1" and "RTHG2" in your DEVICE file. To implement both Request Notice and Request Barcode dual printers, you would use names such as "Request RTHG1" and "Request RTHG2" or "Label RTHG1" and "Label RTHG2". When this is implemented, the patients with even social security numbers will print on one printer and odd social security numbers will print on the other. Add the device "xxxRTHG1" to the file room's Request Notice Printer or Record Barcode Printer parameter field using the Computer Site Manager's Menu, File Room Set-up (Site Mgr) option.

Initialization Menu

*Borrower Initialization*

During the borrower initialization process, all active clinics, wards and persons in the HOSPITAL LOCATION, WARD LOCATION, and NEW PERSON files will be initialized as borrowers. There may be other areas which you will want to also initialize. In order to do this, it will first be necessary to enter those areas into the appropriate file, assigning them a type of OTHER. Examples of such borrowers would be Correspondence Unit, Tumor Registry, Details Office, and Doctor's Reading Room.

Below is a listing of the characteristics used for some of the more common barcode printers.

*DATASOUTH*

In order to print barcodes with the DATASOUTH there are two functions that need to be set on the printer: l) function 2 set to 18 (the number of lines on the label) 2) function 70 set to 1 (enables barcode printing).

NAME: P-DATA SOUTH/220 BARCODE

FORM FEED: \#

PAGE LENGTH: 18

BACK SPACE: \$C(8)

DESCRIPTION: DS220 WITH BARCODE

BAR CODE OFF: \*94,"G",!,?6,"\*",X,"\*"

BAR CODE ON: \*94,"H08",\*94,"BXA"

*MT290*

The MT290 needs to have the barcode cartridge in place. Then program the printer at the panel so: l) unsecure mode (yes) 2) compressed print (yes) 3) double pass (no).

NAME: P-MT290 W/BARCODE

RIGHT MARGIN: 80

FORM FEED: \#,\*27,"\[18t"

PAGE LENGTH: 18

BACK SPACE: \$C(8)

DESCRIPTION: BARCODE FOR MT290

BAR CODE OFF: "\*",!!,?5,\$S(\$D(X):X,l:""),!

BAR CODE ON: \*26,\*32,"F5;001" \*25,\*20,"\*"

Initialization Menu

*FACIT*

The FACIT is ready to use as is.

NAME: P-FACIT

RIGHT MARGIN: 80

FORM FEED: \#,\*27,"\[18t"

PAGE LENGTH: 18

BACK SPACE: \$C(8)

DESCRIPTION: P-FACIT/SLAVE

BAR CODE OFF: \*12,!,?10,"\*",X,"\*",\*12

BAR CODE ON: \*27,\*50,\*50,\*27,\*53,\*52,\*26,\*39,\*79,"@"

Initialization Menu

### Barcode Labels for All Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Barcode Labels for All Patient option is used to print record barcode labels for all patients in your database. The process will also create records for those patients added to the system after record initialization has taken place; however, it should not be used without record initialization having been completed.

At multi-divisional facilities, you may specify for which division you want the labels to print. Labels may be printed in alphabetical or terminal digit order. Terminal digit order allows you to print a batch at a time whereas the alphabetical sort will perform the entire run all at once. In order to run by terminal digit, the Terminal Digit Sort Global must have been run.

In terminal digit sorting, digits of the SSN are grouped as follows:

REGIONAL TERTIARY SECONDARY TERMINAL

CODE DIGIT DIGIT DIGIT

435 15 00 23

The system works from right to left, looking at the terminal digit, the secondary digit, the tertiary digit, and lastly the regional code. Thus, 000 00 0123 would be printed before 000 00 0823. All patients with social security numbers in the PATIENT/RADIOLOGY PATIENT files would be included in this run with the exception of expired patients. It will take approximately 1 hour for every 1,000 patients.

Initialization Menu

### Borrower Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option initializes all active clinics, wards and providers in your Location and Provider files, placing them in the Borrowers/File Areas file.

IT IS IMPORTANT TO NOTE THAT ALL BORROWERS WILL STILL NEED TO BE ENTERED BY THE APPLICATION COORDINATOR THROUGH THE BORROWER SET-UP OPTION OF THE SYSTEM DEFINITION MENU.Initialization Menu

### Clinic Request Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option checks all clinic appointments and requests records/x-rays if required by the clinic set-up. The option is normally only used when your Automatic Clinic Initializer background job fails to run.

Initialization Menu

### Compile Terminal Digit Sort Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is a preliminary step prior to printing barcode labels. It is necessary if you plan to print them in terminal digit order, as it sets up the mechanism by which they will be sorted. It will take approximately 1 1/2 hours for 44,000 entries. This option can also be used to select a range of records for generating record retirement pull lists.

Initial utilization of this option

Do you wish to queue a job that will compile global? No// YES

Subsequent utilization of this option

The ^UTILITY ("RTDPTSORT") global already exists.

Compilation started: AUG 2, 1990@13:11

finished: AUG 2, 1990@13:13

Do you wish to queue a job that will compile global? No// YES

Initialization Menu

### Delete Terminal Digit Sort Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After initial printing, the Terminal Digit Sort global is no longer used by the system and may be deleted through this option.

Initialization Menu

### Initialize Records (NO LABELS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create the records which will be tracked by Record Tracking. Using patients in the Patient file or Radiology Patient file (depending upon the application for which you are initializing records) as a base, it will create records according to specifications made in your Application Set-up. One volume of each default record (Volume 1) and linked record (if defined) will be created for each patient in the appropriate file. Upon creation of these records, an entry is made in the Records file (#190) and the Record Movement History file (#190.3). It will be necessary to identify those patients having multiple volumes and create those records, along with their barcode labels, at a later date. This option does not print barcode labels.

Should it be necessary to restart this job, you may do so by accepting the default at the initial prompt ("Start at DFN") as the system will store the DFN corresponding to the last patient record created. You may wish to queue this job to run during off hours.

Initialization Menu

### Inpatient Barcode Labels Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Barcode Labels Only option is used to print record barcode labels for inpatients in your database. The process will also create records for those patients added to the system after record initialization has taken place; however, it should not be used without record initialization having been completed.

At multi-divisional facilities, you may specify for which division you want the labels to print. Labels may be printed in alphabetical or terminal digit order. Terminal digit order allows you to print a batch at a time whereas the alphabetical sort will perform the entire run all at once. In order to run BY terminal digit, the Terminal Digit Sort Global must have been run.

In terminal digit sorting, digits of the SSN are grouped as follows:

REGIONAL TERTIARY SECONDARY TERMINAL

CODE DIGIT DIGIT DIGIT

435 15 00 23

The system works from right to left, looking at the terminal digit, the secondary digit, the tertiary digit, and lastly the regional code. Thus, 000 00 0123 would be printed before 000 00 0823. All patients with social security numbers in the PATIENT/RADIOLOGY PATIENT files would be included in this run with the exception of expired patients. It will take approximately 1 hour for every 1,000 patients.

Initialization Menu

### Single Clinic Request Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Single Clinic Request Initialization option checks all appointments for the selected clinic and requests records/x-rays if required by the clinic set-up. This option is similar to the Clinic Request Initialization option except that it is run for a specific clinic. You may wish to use this if you have a clinic now requiring records which previously did not.

## Purge Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to purge certain data specific to Record Tracking. It is recommended purges not be performed the first month Record Tracking is live. After that, regular purging should be done. How often you purge will depend upon the amount of available disk space as well as the amount of activity in Record Tracking. Purges should be run on the same CPU as the RT and RTV globals and not at the same time the Automatic Clinic Initialization background job is being run. You may schedule regular purging through the TaskMan if you wish.

Purges are done by record type, based on the specifications set up in the Type of Record Set-up option of the System Definition Menu. For each record type, the following purge parameters will be set:

OK TO PURGE DATA?

PULL LIST PURGE CUTOFF (days)

REQUEST PURGE CUTOFF (days)

\# PREVIOUS MOVEMENTS TO RETAIN

Upon entering this option a purge profile will be displayed, reflecting the purge parameters set up for each record type. You will be given the opportunity to edit these if you wish, then prompted for which data should be purged (pull list, requests, movement logs). The data specified for purging through the Overall Purge Parameters will only be purged for those record types for which the OK TO PURGE DATA field has been set to YES. You may purge all data for all record types, or specify certain record types and data to be purged.

## Re-Compile Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows RT templates to be recompiled on each CPU after running an init. It will recompile the cross-reference templates in addition to the input and print templates used by FileMan. Input and print templates have the RTC\* namespace. Cross-reference templates have the RTX\* namespace and are as follows:

RECORDS FILE \#190 RTXR\*

REQUESTED RECORDS \#190.1 RTXQ\*

RECORD MOVEMENT HISTORY \#190.3 RTXM\*

PULL LIST \#194.2 RTXP\*

BORROWERS/FILE AREAS \#195.9 RTXB\*

## Record Tracking System Overall Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is the final step in the initialization process. An important aspect of this option is the interfacing of Record Tracking (Medical Administration and Radiology applications) with the Scheduling package, such that record requests are created for scheduled clinic appointments and placed on the appropriate pull list. This will be transparent to the user and may be accomplished in one of two ways. Record requests may either be created continually in the background as clinic appointments are scheduled, or you may schedule a background job to run once each evening. Scheduling a background job to run once each evening is the preferred method. This is done through TaskMan as well as via this option by setting the parameter BATCH RECORD/XRAY REQUESTS to YES. At the next prompt, BATCH REQUESTS CUTOFF (days), you will specify the number of days into the future the system should look at scheduled appointments and make corresponding record requests. This parameter should be set to a time span which will cover the lead time the file room will need to pull records. Each time this job runs, a MailMan message is generated to the mail group specified in the CLINIC REQUESTS MAIL GROUP field of the Application Set-up option, Computer Site Manager Menu. If this message is not received, the job should be run manually through the Clinic Request Initialization option of the Computer Site Manager Menu. The final step of this process is setting the INTERFACE STATUS to YES for each application.

*Field DescriptionsParameters Used by All Applications*

QUEUE THRESHOLD This applies to records selected for transaction

through options on the Transaction Menu; i.e.,

charge-out, check-in, etc. You should enter the

number of records which must be selected for

transaction in order for that transaction to be

queued to run, rather than accomplished at time

of entry thus possibly causing a system slowdown.

Enter a number between 0 and 9999. You may

wish to enter a low number to reduce slow down of

the system when large quantities of records are

selected for transaction. Two is recommended.

Record Tracking System Overall Parameters

OPERATING Enter the operating condition. Choose from:

CONDITIONS

'N'ORMAL

'E'MERGENCY (NORMAL COMPUTER DOWN) (if

set to "E" user will be prompted to enter a device each

time one is needed)

Under normal conditions, the system uses the

parameters set up in Files \#195.1, \#195.2, and \#195.9

to determine which input and printer devices to use.

Under emergency conditions, the system ignores all

the location parameters set up and prompts the user

for this information.

NULL QUEUING This field applies only when you will NOT be

DEVICE scheduling a background job to run each evening

to create record requests for scheduled clinic

appointments. (It should be left blank if you will be

scheduling a background job to run each night.) This

field allows you to define a queuing device (usually a

port) where queued jobs should be sent.

BATCH RECORD/ YES/NO Do you wish all record/x-ray requests to

XRAY REQUESTS be processed immediately or batched? YES to batch

requests, NO to process immediately. If YES, the next

prompt is used to specify the number of future days

into which the system should look when gathering

such record requests.

BATCH REQUESTS This field operates in conjunction with a scheduled

CUTOFF (days) job which will run each night where Record Tracking

looks at the Scheduling module to see what appointments

have been scheduled and makes the appropriate

record requests and places them on the appropriate pull lists.

At this prompt, you should enter the number of days into the future

the system should look (1-9). Automatic default is 5. An

associated MailMan message will be generated

advising that this job has run. If you do not receive

this message, you should run the Clinic Request

Initialization option on the Computer Site Manager

Menu.

Record Tracking System Overall Parameters

LABEL PRINTER This field has been provided to allow the label

COOLER printer to hang for a specified amount of time every

100 patients. You should enter the number of minutes

you wish the printer to hang before beginning again.

INSTITUTION/ This is the station number of the site. Once this

STATION NUMBER has been selected, it should never be changed as this

value is encoded in the barcodes for all records in the

system.

*MAS Parameters*

RECORD TYPE Enter the record type (as defined in Record Type

FOR MEDICAL Set-up) which should be created for the medical

RECORD record.

MAS INTERFACE This is the final step in initializing the MAS

STATUS application. When set to UP, the system will be

live. Choose from: 0-Down 1-Up.

*Film Jacket Tracking Parameters*

RECORD TYPE Enter the record type (as defined in Record Type

FOR MASTER Set-up) which should be created for the master

JACKET jacket.

RADIOLOGY This is the final step in initializing the Radiology

INTERFACE STATUS Application. When set to UP, the system will be

STATUS live. Choose from: 0-Down 1-Up.

A MailMan message will be generated each time the automatic CLINIC REQUEST INITIALIZATION job is run. It will be sent to the mail group specified through the CLINIC REQUESTS MAIL GROUP field of the Application Set-up option, Computer Site Manager' Menu.

# Film Tracking Specific Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Film Tracking Specific and MAS Specific Set-Up Menus have been provided for users who routinely use both applications of Record Tracking (Radiology and Medical Administration) in their daily activities. For example, an MAS clinic clerk may need to request both Radiology and MAS records and view the record profiles of each. Ordinarily such a user would need to exit and reenter Record Tracking in order to gain access to the other application. Assigning the user options from either of these menus will allow them to revert back and forth between applications without having to do this.

With the exception of the Fill Next Clinic Request and Admitting Area Chart Request options on the MAS Specific Set-Up Menu, the options in these menus appear elsewhere in Record Tracking; however they have been renamed here in order to be application specific. When a user calls up one of these options, the system automatically associates it with the correct application.

The Site Manager should note that this function is intended for users having a variety of Record Tracking options on their menu but not the RT Overall Menu. Users having the RT Overall Menu must specify an application upon entering Record Tracking and options from either of these two menus will then only work within their intended application.

Below is a brief description of each option contained in this menu.

IMAGING AREA SET-UP - Used to enter/edit and define/update parameters for each Radiology imaging area

JACKET PROFILE - Provides an abbreviated on-line listing of all Radiology records for a specified patient.

REQUEST FILM JACKETS - Used to enter a request for a patient's Radiology record.

## Imaging Area Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit and define/update parameters for each Radiology imaging area. Imaging areas entered through this option become part of your HOSPITAL LOCATION file (#44). They also become part of your Borrowers/File Areas file (#195.9).

*Field Descriptions*

Select Reception Enter name of new or existing imaging area for

Viewing/Rack Area which you wish to define or update parameters. This

is a multiple field. For each entry made into this

field, the following fields will also be prompted,

returning you to this prompt upon completion. You

should enter each imaging area which will be

associated with your application.

ARE YOU ADDING YES/NO - This prompt will only appear if your

{Imaging Area} entry at the previous prompt was a new entry.

AS A NEW HOSPITAL

LOCATION?

PHONE \# Enter the telephone number of this area.

LOCATION/ROOM \# Enter the location/room \# of this area.

BORROWING Enter the borrowing privileges of this area.

PRIVILEGES Choose from:

'N'ORMAL

'I'NACTIVATED

'R'EVOKED

*Hospital Location File Parameters*

NAME You may rename the imaging area at this prompt,

or accept the default and continue. Unless you hold

the proper FileMan access, you will be unable to delete

an imaging area. See your site manager should this

be necessary.

Imaging Area Set-up

INSTITUTION Institution (from your Institution file) with

which this imaging area is associated.

Select SYNONYM Enter the synonym by which this imaging area is

known.

*Record Request to be Made When Making an Appt or Registering a Pt*

REQUESTS FOR Borrower's name to be associated with requests

WHICH BORROWER from this area. Your entry at the first prompt will

appear as a default; however you may enter a different

one if you wish.

ARE RECORDS YES/NO - When patients report to this area, are

REQUIRED records required? If YES, you will proceed through

the following three prompts.

Select RECORD Enter each record type(s) which will be needed in

TYPE NEEDED association with visits. This is a multiple field, and

you may specify more than one record type.

RECORD TYPE Your entry at "Select RECORD TYPE NEEDED"

NEEDED will appear as a default. If incorrect you may enter

the correct record type at this prompt; otherwise, you

may accept the default by entering \<RET\>.

VOLUMES Enter the volumes of this record type which will be

REQUIRED required in association with these visits. Choose from:

'A'LL

'L'AST

'N'ONE

Imaging Area Set-up

*Scheduled Admissions Borrowers*

SCHEDULED YES/NO If YES, when an entry in the SCHEDULED

ADMISSION ADMISSIONS file has a type WARD and the ward

BORROWER location matches this ward location borrower, a pull

list will be created for this ward location borrower

or associated borrower.

TREATING BORROWER/FILE AREA entry If an entry in

SPECIALTY the SCHEDULED ADMISSIONS file has a type

TREATING SPECIALTY and the treating

specialty matches this borrower's treating

specialty, a pull list will be created for this

borrower or associated borrower.

## Jacket Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides an abbreviated on-line listing of all records for a specified patient. It is the same listing which is displayed throughout the Record Tracking package when a patient name is keyboard entered rather than a barcode being wanded.

This option displays several lines of demographic data related to the patient. For each record (listed by record type), the volume number, current borrower, date/time charged to that borrower and phone/room of the borrower will be shown. Whenever a record is inactive (as a result of being transferred to another facility or inactivated) or charged to a borrower as a result of being on a pull list, it will be so annotated beneath the record. Associated borrowers may also be shown.

## Request Film Jackets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Request Film Jackets option is used to enter a request for a patient's record. The user may request a single record, multiple records or a range of records for a patient. He/she may request the record for the current time or a date/time in the future. The person/location borrowing the record must be in the Borrower file.

Dependent on how the site parameter is set at your facility, the current borrower of a record may enter a request for that record for a future date. This may be done by wanding the record's barcode label or by keyboard entry. Use of the barcode label reader is the fastest and most accurate method of request.

When record selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the requestable records for that patient in that application. If a record type has been defined as unrequestable through your site parameters, it will not be displayed in the Short Record Inquiry. If the record requested has been inactivated or transferred out to another facility, it will not be displayed in the inquiry. Wanding the barcode label of an unrequestable record will result in the message, "No match found" being displayed. After the record(s) is selected, a request profile will be displayed for each record. This includes the current location of the record, the home file room of the record, recent pending requests, etc. A sequential request number is automatically assigned by the system for each record requested.

# MAS Specific Set-up Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Film Tracking Specific and MAS Specific Set-Up Menus have been provided for users who routinely use both applications of Record Tracking (Radiology and Medical Administration) in their daily activities. For example, an MAS clinic clerk may need to request both Radiology and MAS records and view the record profiles of each. Ordinarily such a user would need to exit and reenter Record Tracking in order to gain access to the other application. Assigning the user options from either of these menus will allow them to revert back and forth between applications without having to do this.

With the exception of the Fill Next Clinic Request and Admitting Area Chart Request options on the MAS Specific Set-Up Menu, the options in these menus appear elsewhere in Record Tracking; however they have been renamed here in order to be application specific. When a user calls up one of these options, the system automatically associates it with the correct application.

The Site Manager should note that this function is intended for users having a variety of Record Tracking options on their menu but not the RT Overall Menu. Users having the RT Overall Menu must specify an application upon entering Record Tracking and options from either of these two menus will then only work within their intended application.

Below is a brief description of each option contained in this menu.

RE-CHARGE A CHART - Used to record transfer of those records charged from the file room from one borrower to another.

CHART REQUEST - Used to enter a request for a patient's MAS record.

ADMITTING AREA CHART REQUEST - Used to request records from an MAS admitting area.

ADMITTING AREA SET-UP - Used to enter/edit and define/update parameters for each MAS admitting area.

CREATE MAS LABELS/RECORDS/VOLUMES - Used to print barcode labels and/or create new MAS records or additional volumes for a patient.

FILL NEXT CLINIC REQUEST - Allows filling of subsequent MAS record requests for patients having multiple appointments on the same day.

PROFILE OF CHARTS - Provides an abbreviated on-line listing of all MAS records for a specified patient.

## Re-Charge a Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Re-Charge a Chart option is used to record transfer of those records charged from the file room from one borrower to another. It is for use with in-house borrowers only. Transfer of records to other institutions should be entered through the Transfer Records option. The system records the new borrower, location/phone and date/time of recharge. This information is displayed each time the associated record inquiry is accessed through the Record Tracking system.

Upon exiting the option, the records will either be recharged immediately or queued for recharge depending upon site parameters and the number of records entered during the session.

Missing flags may be removed thru this option and records may be created for patients already in your database but having no records in the Record Tracking system. These will be created in accordance with site specifications for initial creation of records.

## Chart Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Chart Request option is used to enter a request for a patient's record. The user may request a single record, multiple records or a range of records for a patient. He/she may request the record for the current time or a date/time in the future. The person/location borrowing the record must be in the Borrower file.

Dependent on how the site parameter is set at your facility, the current borrower of a record may enter a request for that record for a future date. This may be done by wanding the record's bar code label or by keyboard entry. Use of the bar code label reader is the fastest and most accurate method of request.

When record selection is made by entering a patient's name, the system displays the Patient Profile and Short Record Inquiry. This inquiry is a list of the requestable records for that patient in that application. If a record type has been defined as unrequestable through your site parameters, it will not be displayed in the Short Record Inquiry. If the record requested has been inactivated or transferred out to another facility, it will not be displayed in the inquiry. Wanding the bar code label of an unrequestable record will result in the message, "No match found" being displayed. After the record(s) is selected, a request profile will be displayed for each record. This includes the current location of the record, the home file room of the record, recent pending requests, etc. A sequential request number is automatically assigned by the system for each record requested.

## Admitting Area Chart Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used in the Medical Administration application of Record Tracking to request records from an admitting area.

You will first be prompted for name of the patient whose records you are requesting. If your site has more than one admitting area (as defined through site parameters) you may also be prompted for the name of the admitting area from which you are requesting records. Based on the patient name entered and the record types to be requested for that admitting area (as defined through site parameters), the system will determine the appropriate records to request and home location (file room) from which to request them. A request notice will automatically print on the printer specified for the file room.

## Admitting Area Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit and define/update parameters for each MAS admitting area. Admitting areas entered through this option become part of your HOSPITAL LOCATION file (#44). They also become part of your Borrowers/File Areas file (#195.9).

*Field Descriptions*

Select Admitting Enter name of new or existing admitting area for

Area which you wish to define or update parameters. This

is a multiple field. For each entry made into this field,

the following fields will also be prompted, returning

you to this prompt upon completion. You should enter

each admitting area which will be associated with

your application.

ARE YOU ADDING YES/NO - This prompt will only appear if your entry

{Admitting Area} at "Select Admitting Area" was a new entry.

AS A NEW HOSPITAL

LOCATION?

PHONE \# Enter the telephone number of this area.

LOCATION/ROOM \# Enter the location/room \# of this area.

BORROWING Enter the borrowing privileges of this area.

PRIVILEGES Choose from:

'N'ORMAL

'I'NACTIVATED

'R'EVOKED

*Hospital Location File Parameters*

NAME Your entry at "Select Admitting Area" will appear as a

default. You may rename the admitting area or accept

the default and continue. Unless you hold the proper

FileMan access, you will be unable to delete an

admitting area. See your site manager should this be

necessary.

INSTITUTION Enter the institution (from your Institution file)

with which this admitting area is associated.

Admitting Area Set-up

Select SYNONYM Enter the synonym by which this admitting area is

known. For example, Reception might be a synonym

for your admitting area.

*Record Request to be Made When Making an Appt or Registering a Pt*

REQUESTS FOR Borrower's name to be associated with requests from

WHICH BORROWER this area. Your entry at "Select Admitting Area" will

appear as a default; however, you may enter a

different one if you wish.

ARE RECORDS YES/NO - When patients report to this area, are

REQUIRED records required? If YES, you will proceed through

the following three prompts.

Select RECORD Enter each record type(s) which will be needed in

TYPE NEEDED association with visits. This is a multiple field, and

you may specify more than one record type.

RECORD TYPE Your entry at "Select RECORD TYPE NEEDED" will

NEEDED appear as a default. If incorrect you may enter the

correct record type at this prompt; otherwise, you may

accept the default by entering \<RET\>.

VOLUMES Enter the volumes of this record type which will be

REQUIRED required in association with these visits. Choose from

ALL, LAST, NONE.

*Scheduled Admissions Borrowers*

SCHEDULED YES/NO If YES, when an entry in the SCHEDULED

ADMISSION ADMISSIONS file has a type WARD and the ward

BORROWER location matches this ward location borrower, a pull list will be

created for this ward location borrower or associated borrower.

TREATING BORROWER/FILE AREA entry If an entry in the

SPECIALTY SCHEDULED ADMISSIONS file has a type

TREATING SPECIALTY and the treating specialty

matches this borrower's treating specialty, a pull list

will be created for this borrower or associated borrower.

## Create MAS Labels/Records/Volumes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create MAS Labels/Records/Volumes option is used to print bar code labels and/or create new records or additional volumes for specified patients. You may use it to create records and associated bar code labels for patients new to the system or to create additional records/volumes and associated bar code labels for patients already in the system. You may also use it to print bar code labels for existing records. This option is not intended for initialization purposes, as it works on a patient-by-patient basis. The Computer Site Manager's Initialization Menu is provided for that purpose.

Only patients already in your database may be entered. For all patients, records will be created according to site parameters defined for the MAS application.

For new patients, records will be created according to your site's specifications for initial record creation. For example, if you are creating a medical record for a new patient in MAS, and your site has defined administrative records "linked" with medical records through the Type of Record Set-up option in the System Definition Menu, the system would also automatically create an administrative record. This would apply only to patients not already in the system.

For patients already in the system, you may specify one record/volume at a time and will be given the opportunity to transfer pending requests for the record type being created to the newest volume.

For each record/volume created, the system will assign a record identifier number, prompt for home location and current borrower/file room, and print a bar code label.

## Fill Next Clinic Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fill Next Clinic Request option is provided to allow filling of subsequent record requests for patients having multiple appointments on the same day.

You will be prompted to enter the patient's name. The system then displays a request profile of all the patient's record requests pending for the current date and prompts you to select the one(s) you wish to fill.

## Profile of Charts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides an abbreviated on-line listing of all records for a specified patient. It is the same listing which is displayed throughout the Record Tracking package when a patient name is keyboard entered rather than a bar code being wanded.

This option displays several lines of demographic data related to the patient. For each record (listed by record type), the volume number, current borrower, date/time charged to that borrower and phone/room of the borrower will be shown. Whenever a record is inactive (as a result of being transferred to another facility or inactivated) or charged to a borrower as a result of being on a pull list, it will be so annotated beneath the record. Associated borrowers may also be shown.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

abbreviation An accepted standard way of shortening responses.
The Record Tracking system accepts responses that
eliminate characters from the end of a word or phrase.
access The approach used to get at something, as in accessing
a menu. You most likely have been assigned access
codes which are necessary for you to enter the system.
Access may also indicate what functions you are
allowed to use; i.e. your level of access.
associated An individual associated with a location borrowing
borrower a record so that other users are given a name to
contact when inquiring about the record. For example,
if a ward were borrowing a patient's record, the
name of the ward administration coordinator might
be entered as an associated borrower.
bar code A label consisting of a number of printed bars and
label intervening spaces set up such that it is recognized
as that of a specific entity when read by a bar code
reader. Used to identify records, borrower and
requests in Record Tracking.
borrower A location, entity or individual to whom records
are loaned. Within Record Tracking, this may be a
physician, employee, clinic, ward, hospital location,
other VA facility or patient.
format The system specifications of what type of characters
should make up a response and how long it should
be.
function A job performed by the computer; i.e. in Record
Tracking, charging-out a record to a specific
borrower would be considered a function.
HELP menu A message or series of messages designed to aid the
user in making an appropriate response to a prompt.
A HELP menu is accessed by entering a question mark
\<?\> or marks \<??\> at the prompt.
home A record's place of residence when it is not being
location borrowed; usually the file room.
interactive A computer system that performs an immediate action
system based on the user's responses to the system prompts.
This involves a conversation between the computer
and the user.
loose filing A field in Record Tracking which may be set to YES
indicator for a specified record charged out of its home location
such that a message will be displayed upon
check-in of the record advising there is loose
filing for it.
military The standard method of recording time used by the
time United States Military. See conversion table at
the end of this glossary.
movement In Record Tracking, the term movement type relates
type to the various actions which may be performed on a
record; charging-out, checking-in, flagging as
missing are all considered movement types.
option An entity which performs a specific job/function
within a package whose name generally indicates the
job it performs. Options are grouped together
under submenus and main menus. In Record
Tracking, Charge-Out Records is an option.
prompt Messages on the screen which ask you to provide
information.
pull list In Record Tracking, a list of record requests
needed at the same date/time by a specific
borrower.
record In Record Tracking, this term generally relates to
the patient's medical record, administrative record
or radiology record. Since Record Tracking may be
applied to a variety of tracking activities (such
as a library), this term is used to specify the
item which is tracked by the system.
record no. Also known as the Record Identifier Number. This
is a sequential number assigned to each record
within Record Tracking upon its creation which is
unique to the record. This number may be entered at
any "Select Record" prompt to access that particular
record and is analogous to wanding the record’s
bar code label.
request In Record Tracking, the act of asking for a
specific record. A request label is usually
generated by this request which indicates the
record asked for, the time needed, the requestor
and other pertinent information. This label
also contains a bar code which may be wanded such
that the request is filled, thus the requested
record is charged to the requestor.
retirement In Record Tracking, the retirement status indicates
status whether or not a record may be retired from the
file room after the allotted period of inactivity.
There are three retirement statuses: OK TO RETIRE,
TUMOR REGISTRY and TEACHING. Records are
considered OK TO RETIRE by the system unless
otherwise specified through the Update Record's
Attributes option of the Transaction Menu.
\<RETURN\> The key which is pressed after each response to
or \<RET\> enter the response into the system and move to
the next prompt.
security A code assigned to each user identifying them
code specifically to the system and allowing them access
to the functions/options assigned to them.
security key Used in conjunction with locked options or functions.
Only holders of this key may perform these options/
functions. Used for options which perform a
sensitive task.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ad hoc Request Response Statistics
Add Requests to Pull List
Admitting Area Chart Request
Admitting Area Set-up
Admitting Area Set-up (Site Mgr)
Application Set-up
Application Set-up (Site Mgr)
Barcode Labels for All Patients
Borrower Initialization
Borrower Set-up
Cancel a Request
Cancel Request from Pull List
Charge Out Pull List Records
Charge Out/Transfer Retirement Pull Lists
Charge-Out Records
Charged Records by Home Location
Chart Request
Check-in Records
Clinic Request Initialization
Combination Data Trace
Compile Terminal Digit Sort Global
Computer Site Manager's Menu
Create a Label/Record/Volume
Create a Pull List
Create MAS Labels/Records/Volumes
Create Record/Volume for transferred Record
Delete a Record
Delete Terminal Digit Sort Global
Designate Requests as 'Not Fillable'
Designate Retirement Requests as 'Not Fillable'
Display Request
Edit a Request
Edit Pull List Comment
Entire Pull List Cancellation
Entire Pull List Cancellation (all dates)
Expanded Record Inquiry
Flag Record as Missing
File Room/Remote Set-up (Site Mgr)
File Room Set-up
File Room Set-up (Site Mgr)
Fill a Request
Fill Next Clinic Request
Film Tracking Specific Menu
Generate Record Retirement Pull Lists
Imaging Area Set-up
Imaging Area Set-up (Site Mgr)
Inactivate/Reactivate Records
Inactivate Records Menu
Initialization Menu
Initialize Records (NO LABELS)
Inpatient Barcode Labels Only
Inpatient Record Location List
Jacket Profile
Label Formatter
Label Functions Menu
Loose Filing Report
Management Reports Menu
MAS Specific Set-up Menu
Missing Records List
Move Requests to Last Volume
Movement Type Set-up
Multiple New Volume Creation
New Volume Creation
Overdue Records List
Patient Charge-Out
Pending Request List
Print Borrower Barcode
Print Pull List(s)
Print Record Retirement Pull list
Profile of Charts
Pull List Date Change
Pull List Functions Menu
Purge Data
Reasons File Set-up
Re-Charge a Chart
Re-Charge Records
Re-Compile Templates
Record Information Menu
Record Inquiry
Record Tracking System Overall Parameters
Records Charged to a Borrower
Reprint a Request Notice
Request a Record
Request a Transfer from another Institution
Request Film Jackets
Request Records Menu
Requests Pending for a Borrower
Retrieval Rate Statistics
Return Transferred Record
Special Multi-Institution Prints
Short Record Inquiry
Single Clinic Request Initialization
System Definition Menu
Test Label Format
Trace Movement History
Transaction Menu
Transfer Record to another Institution
Transfer Records Menu
Type of Record Set-up
Update Record's Attributes

# Data Supplement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of prompts with associated definitions and possible entries which occur in Record Tracking. Prompts are in bold print listed in alphabetical order, much as they will appear on the screen.

The most common defaults, when applicable, have been included in this Data Supplement. You may, however, note some discrepancies between those which appear on your screen and those in this supplement. This may be attributed to two factors; defaults to some prompts vary according to site parameters, and certain prompts may contain defaults in some options while not in others. It is important to note that whenever a default appears with a prompt on the screen, the entry of a \<RET\> will always signify its acceptance.

You should also note that entry of an up-arrow \<^\> may be used to abort processing. In some cases, a \<RET\> or NO may also be entered to abort processing. In each case, such an entry will either return you to the menu or to a prompt in the option from which you may abort or make another selection.

'ALL' INPATIENTS OR A 'RANGE' OF ADMISSIONS? RANGE//

This prompt appears when running the Inpatient Record Location List option of the Management Reports Menu. You are asked to specify whether you wish to run the list for all current inpatients or those admitted within a specified date range. You may enter:

> .\<RET\> or 'R'ANGE - you will subsequently be prompted for a date range

> .'A'LL

ARE YOU ADDING '{PULL LIST}' AS A NEW PULL LIST?

YES/NO This prompt appears in the Create a Pull List option of the Pull List Functions Menu asking you to confirm your previous entry as a new pull list.

ARE YOU SURE YOU WANT TO 'CHARGE OUT' THESE RECORDS? No//

YES/NO This prompt appears in the Charge Out Pull List Records option of the Pull List Functions Menu asking you to confirm whether you wish to charge out the selected pull list(s).

ARE YOU SURE YOU WANT TO CANCEL THIS PULL LIST? No//

YES/NO This prompt appears in the Entire Pull List Cancellation option of the Pull List Functions Menu asking you to confirm whether you wish to cancel the selected pull list.

ARE YOU SURE YOU WANT TO CANCEL THIS/THESE REQUESTS? No//

YES/NO This prompt appears in the Cancel a Request and Cancel Request From Pull List options of the Request Records and Pull List Functions Menus respectively, asking you to confirm whether you wish to cancel the selected request(s).

ARE YOU SURE YOU WANT TO CHANGE THE DATE THE RECORDS ARE NEEDED? No//

YES/NO This prompt appears in the Pull List Date Change option of the Pull List Functions Menu asking you to confirm whether you wish to change the date records on the selected pull list are needed.

ARE YOU SURE YOU WANT TO DELETE THIS RECORD? No//

YES/NO This prompt appears in the Delete a Record option of the Transaction Menu asking for confirmation that you wish to delete the selected record.

ARE YOU SURE YOU WANT TO FLAG THIS RECORD AS MISSING? No//

YES/NO This prompt appears in the Flag a Record as Missing option of the Transaction Menu asking you to confirm whether you wish to place a missing flag on the selected record.

ASSOCIATED BORROWER

This prompt may appear (depending upon your site parameters) in a number of options throughout Record Tracking after entry of the borrower of a record. Generally, it is used to enter the name of an individual who may be contacted when inquiries are made about the record when the actual borrower entered is a location (i.e., a clinic or a ward). For example, if the borrower is a ward, your entry at the associated borrower prompt would most likely be the Ward Administration Coordinator. The name entered must be in the Borrowers/File Areas file.

BEGINNING ADMISSION DATE/TIME

This prompt appears in the Inpatient Record Location List option of the Management Reports Menu when you elect to run the list within a range of admission dates rather than for all inpatients. Your entry at this prompt should be an admission date/time at which you wish the report to begin. Date/time entry should be made using a conventional date/time entry method.

BEGINNING DATE

This prompt appears in the Ad Hoc Request Response Statistics option of the Management Reports Menu in association with the specification of a date range in which to run the report. Your entry at this prompt should be the date/time at which the report should begin.

BORROWER

This prompt appears in the Create a Pull List option of the Pull List Functions Menu asking you to enter the borrower to whom the pull list will subsequently be charged. This should not be confused with the requestor (individual entering the requests/pull list). They may be the same in some cases. For example, John Clerk (the requestor) may create a pull list for the Correspondence Unit (the borrower). The borrower entered must be in the Borrowers/File Areas file. You may enter:

> .name of borrower

> .wand borrower barcode label

> .\<RET\> not allowed; an entry in this field is required in order to proceed

> .up-arrow \<^\> to abort processing; pull list will be deleted

CHOOSE REQUEST FROM LIST

This prompt appears in association with the display of a patient's request profile. You may select your request(s) by entering the corresponding number(s) from the left side of the display. You may enter:

> .a single number

> .several numbers separated by commas; i.e. 1,3,5

> .a range of numbers; i.e. 1-4

> .a combination of several numbers and a range; i.e. 1,3,4-7

COMMENT

This is a word processing field in the Request a Record option, Request Records Menu. You may enter a free text comment pertaining to the request. You may enter:

> .free text comment regarding request

> .\<RET\> to leave blank

COMMENTS

This is a word processing field which appears in the Create a Pull List and Edit Pull List Comment options of the Pull List Functions Menu. A free text comment may be entered pertaining to the selected pull list. You may enter:

> .free text comment regarding pull list

> .\<RET\> to leave blank

CREATE {RECORD TYPE} VOLUMES STARTING WITH \#{N}? No//

YES/NO This prompt appears in the Multiple New Volume Creation option of the Transaction Menu. The number inserted by the system {N} will be the next consecutive volume number of the specified record type for the patient with whom you are working.

CONTENT DESCRIPTOR

Depending upon your site parameters, this may be prompted when creating a record or updating its attributes. You may enter a brief description of the contents of the record at this prompt.

CURRENT BORROWER/FILE ROOM: {DEFAULT DEFINED THROUGH PARAMETERS}//

This prompt appears in the options Create a Label/Record/Volume and New Volume Creation options of the Transaction Menu. The default will be the default initial borrower specified in your site parameters. You may enter:

> .\<RET\> or up-arrow \<^\> to accept default; processing will continue

> .another borrower (from Borrowers/File Areas file)

DATE

This prompt appears in the Retrieval Rate Statistics option of the Management Reports Menu asking for a date for which to run the report.

DATE RECORDS NEEDED

This prompt appears in the option Create a Pull List of the Pull List Functions Menu. You are prompted to enter the date/time the records on the pull list will be needed by the borrower. An entry in this field is required in order to proceed.

DATE/TIME RECORD NEEDED: NOW//

This prompt appears in the Request a Record option of the Request Records Menu asking for the date/time the requested record is needed. You may accept the default or enter a different date/time record will be needed. You may enter:

> .\<RET\> to accept default of NOW (request label will be printed

> on default device)

> .a future date/time records are needed (request will be filed)

> .up-arrow \<^\> to abort; request will be deleted

DETAILED OR SUMMARY REPORT: S//

This prompt appears in the Retrieval Rate Statistics option of the Management Reports Menu asking if you want the report to include one overall stat total (summary) or break it out by pull list (detailed). You may enter:

> .\<RET\> or 'S'UMMARY

> .'D'ETAILED

DO YOU STILL WANT TO 'FILL' SELECTED REQUESTS? No//

YES/NO This prompt appears in the Fill a Request option of the Request Records Menu when an up-arrow \<^\> has been entered at the "Fill Which Request" prompt.

DO YOU STILL WISH TO '{CHARGE-OUT/CHECK IN/RE-CHARGE/TRANSFER-TRANSFER BACK/REQUEST}' SELECTED RECORDS? No//

YES/NO This prompt will appear in the following options when an up-arrow \<^\> is entered at the "Select Record" prompt AND a record(s) has already been entered (and accepted by the system) for processing: Charge Out Records, Check In Records, Re-Charge Records, Transfer Records of the Transaction Menu, and Request a Record of the Request Records Menu.

DO YOU WANT TO APPROVE/DISAPPROVE THE FINDING OF THE RECORD? No action//

This prompt appears when a user holding the FR SUPERVISOR KEY accesses a record which has been Found Pending Supervisor Approval. You may enter:

> .APPROVE - you will subsequently be prompted through the approval procedure

> .DISAPPROVE

DO YOU WANT TO CHANGE STATUS TO '{REQUESTED/NOT FILLABLE}'? YES//

YES/NO This prompt appears in the Designate Requests As 'Not Fillable' options of both the Request Records and Pull List Functions Menus, as well as the Charge Out Pull List Records option of the Pull List Functions Menu. It will be preceded by a message giving the current status of the selected request.

DO YOU WANT TO CHANGE THIS RECORD'S HOME LOCATION? No//

YES/NO This prompt appears in the Check In Records option of the Transaction Menu when the home location of a record selected for check-in is different from the location (file room) it is being checked into.

DO YOU WANT TO CHARGE OUT RECORDS TO A HOLDING AREA? No//

This prompt appears in the Charge Out Pull List Records option of the Pull List Functions Menu. You may enter:

> .\<RET\> or NO

> .YES - you will be prompted for the name of the holding area to which the records should be charged

DO YOU WANT TO CHECK IN THE RECORD TO THE NEW HOME FILE ROOM? NO//

YES/NO This prompt occurs in the option Update Record's Attributes of the Transaction Menu when the home location of a record has been changed.

DO YOU WANT TO CREATE {RECORD TYPE} VOL \# {N}? No//

YES/NO This prompt appears when creating new volumes/records in either Create a Label/Record/Volume or New Volume Creation options of the Transaction Menu. The number {N} inserted by the system will be the next consecutive volume number for the specified record type of the selected patient. You may enter:

> .\<RET\>, NO, or up-arrow \<^\> to abort processing

> .YES to create the record type and volume specified

DO YOU WANT TO FILL A PENDING REQUEST? No//

This prompt may appear in either the Charge-Out Records or Check-In Records option of the Transaction Menu when the selected record has a pending request for the current date. It will be preceded by a message advising of the pending request. The prompt will appear in the Charge-Out Records option only when the borrower is the same as the requestor of the record (and the request is for the current date). It appears in the Check-In Records option whenever the selected record has a pending request for the current date.

DO YOU WANT TO INCLUDE UNFILLED CLINIC REQUESTS? No//

YES/NO This prompt appears when using the Pending Request List option of the Management Reports Menu. When YES is answered, the list will include all pending requests associated with pull lists as well as individual record requests.

DO YOU WANT TO REMOVE THE 'MISSING' FLAG ON THIS RECORD? No//

YES/NO This prompt may appear when a record flagged as missing has been accessed. Its appearance will depend upon whether the user has the necessary access to remove a missing flag (as defined in your site parameters). If YES, you will be prompted through the process of removing the missing flag.

DO YOU WANT TO SEE MORE 'HELP' INFORMATION? No//

YES/NO This prompt appears in a variety of Record Tracking options after a \<?\> has been entered at a prompt asking if you wish to see additional HELP information.

DO YOU WANT TO USE THE FILE ROOM'S DEFAULT DEVICES? NO//

YES/NO This prompt appears if you have access to more than one file room in Record Tracking; i.e., application coordinators, supervisors, site managers, etc. Most users have access to only one file room which they are automatically dropped into upon entering Record Tracking. You will first be prompted for the file room from which you wish to track records, then this prompt will be displayed asking whether you wish to use the file room's default devices or specify your own printing devices when it is necessary to print a label or report.

DO YOU WISH TO CREATE A NEW RECORD OR VOLUME? No//

YES/NO This prompt appears in the Create a Label/Record/Volume option of the Transaction Menu. If YES, you will be prompted through the process of creating a new record/volume.

DO YOU WISH TO FIRST DESIGNATE SOME REQUESTS AS 'NOT FILLABLE'? No//

YES/NO This prompt appears in the option Charge Out Pull List Records of the Pull List Functions Menu giving you the opportunity to first designate certain requests on the pull list as not fillable. Records designated not fillable will not be charged to the pull list borrower when the pull list is charged out.

ENDING ADMISSION DATE/TIME

This prompt occurs when you elect to run the Inpatient Record Location List within a range of admission dates rather than for all inpatients. Your entry should reflect the admission date at which the report should end.

ENDING DATE

This prompt is associated with specification of a date range for which the Ad Hoc Request Response Statistics Report should be run. At this prompt, you should enter the ending date for which you wish the report to run.

ENTER NEW DATE

This prompt appears in the Pull List Date Change option of the Pull List Functions Menu asking for the new date which records on pull list are needed. You may enter a new date for which records are requested (must be in the future).

ENTER NEW PULL LIST NAME

This prompt appears in the Create a Pull List option of the Pull List Functions Menu. You may enter the name of pull list you are creating (may be 3-50 characters in length).

ENTER RESPONSE

This prompt appears in the Retrieval Rate Statistics option of the Management Reports Menu asking you to enter the method with which you wish to run the report. You may enter:

> .1 to run for a date range

> .2 to run for one day

> .3 to run for one pull list

ENTER THE LIST (HIGHEST) VOLUME TO CREATE, \#{N}//

This prompt appears in the Multiple New Volume Creation option of the Transaction Menu. The system will display a default sufficient to allow creation of one additional volume. You may create up to six additional volumes at a time. You may enter:

> .\<RET\> to accept the default

> .a number to indicate the highest volume you wish to create

FILL WHICH REQUEST

This prompt appears in the Fill a Request option of the Request Records Menu. You will be returned to it repeatedly during a session so that you may create a list of requests to be processed at the conclusion of the session. This is a versatile step within the option allowing various actions depending upon whether a list has yet been established. Note that the actions depend upon whether a list has yet been established, not whether requests have previously been entered during the session. The system must first accept these requests as valid prior to entering them on a list. Requests which have been cancelled, filled or are for inactive/deleted records will not be accepted by the system and not placed on the list. The actions surrounding the entry of \<RET\> or up-arrow \<^\> will vary depending upon what point you are at in the session. At any point during the session you may enter the following at this prompt:

> .patient name

> .request number you wish to fill

> .wand request label (if record is active and request has not yet been filled)

The following actions are also possible:

> Requests may be deleted from an established list by entering a minus sign \<-\> followed by the number of the request you wish to delete. You may first enter a \<?\> to get the number of the request you wish to delete.

> If a \<RET\> or up-arrow \<^\> are entered prior to a list being established, processing will be aborted.

> If a \<RET\> is entered after a list has been established, the requests will be filled (or queued for filling) and the session will end.

> If an up-arrow \<^\> is entered after a list has been established, you will be given the opportunity to abort processing (you will be prompted "Do you still want to 'fill' selected requests? No//").

FROM DATE

This prompt appears in the Retrieval Rate Statistics option of the Management Reports Menu asking for the beginning date of the date range for which you wish to run the report.

HOME LOCATION {CURRENT FILE ROOM}//

This prompt appears in the Create a Label/Record/Volume, Update Record's Attributes, and New Volume Creation options of the Transaction Menu. At this prompt, you are asked for the home location of the record selected (where it will reside when not charged out). You may enter:

> .\<RET\> to accept the default

> .another home location (must be a file room defined to store this record type)

> .up-arrow \<^\> to abort processing - If an up-arrow \<^\> is entered, the default will be assumed at this prompt as well as the next prompt “Current Borrower/File Room”.

HOW DO YOU WANT LIST SORTED? TERMINAL DIGITS//

This prompt appears in the Print Pull List(s) option of the Pull List Functions Menu. You are prompted for the method you wish the pull list to be sorted. You may enter:

> .\<RET\> to accept default

> .C to sort by clinic name, then terminal digit

> .A to sort by clinic name, then appointment time

HOW DO YOU WANT THE '{APPLICATION}' RECORDS SORTED? Mixed//

This prompt appears in the Trace Movement History option of the Record Information Menu. You may enter:

> .\<RET\> to accept default

> .'S'EPARATE to sort record type and volumes separately

HOW DO YOU WANT THE LISTING SORTED? Borrower//

This prompt appears in the Charged Records By Home Location and Overdue Records List options of the Management Reports Menu. You may enter:

> .\<RET\> or 'B'ORROWER

> .'N'AME to sort by patient name

> .'T'ERMINAL DIGIT

INCLUDE RECORDS CURRENTLY CHECKED INTO THE HOME LOCATION? No//

YES/NO This prompt appears in the Charged Records By Home Location option of the Management Reports Menu. If you choose to include those records currently checked into the home location (all records belonging to the specified home location will appear on the printout), you may wish to consider running this list during off-hours since it may be quite lengthy. Enter \<RET\> or NO to include only those records currently charged out of the home location.

INDICATE WHAT INFORMATION TO DISPLAY: All//

This prompt appears in the Record Inquiry option of the Record Information Menu. You may enter:

> .\<RET\> or 'A'LL to display record information for all of the selected patient's records

> .'T'YPE - you will subsequently be prompted to specify a record type

> .'V'OLUME - you will subsequently be prompted for the volume

INSTITUTION PROMPTS (of REQUESTOR, FILE ROOM, BORROWER, ETC.)

On occasion, you may be prompted for an institution in an option in which you would not normally expect to be. This generally occurs when there is a conflict between the user's institution (as defined in your site's Institution file) and the associated institution of the entry just made. The system will accept an entry at such a prompt and processing will continue; however, appearance of such a prompt may signify a potential problem and your site manager should be consulted.

ISSUE REQUEST FOR RECORDS? NO//

This prompt appears in the Admitting Area Chart Request option of the MAS Specific Set-up Menu and in the Appointment Management option. It also appears when registering a patient through the ADT (Admission-Discharge-Transfer) module<span id="RT_2_47_Def_Value" class="anchor"></span>. You may enter:

> .\<RET\> to accept the default value of No

> .YES if you wish to request the records from the file room - a request notice will print on the specified printer for the appropriate file room

LOOSE FILING INDICATOR

This prompt appears in the Update Record's Attributes option of the Transaction Menu and is used to notify file room personnel that loose filing exists for a record being checked into the file room. If YES is entered at this prompt, a message will be displayed when the record is checked into the file room advising of the loose filing. Necessary filing may then be accomplished prior to placing the patient's record back on the shelf. To turn this message off, this field must be set back to NO. You may enter:

> .YES

> .NO

> .\<RET\> - NO will be assumed

OK? YES//

This prompt appears often in Record Tracking and relates to your entry to the previous prompt. Essentially, the system is asking "Is this the selection you wish to make?". If the entry displayed is incorrect, it is advisable that an up-arrow \<^\> be entered rather than NO. Entry of NO will eventually return you to the previous prompt; however, the route by which it returns may be somewhat confusing. You may enter a \<?\> for a list of possible selections and make the correct entry. You may enter:

> .\<RET\> if correct

> .up-arrow \<^\> to return to the previous prompt

PRINT OVERDUE LIST FOR AN INSTITUTION OR HOME LOCATION? Institution//

This prompt appears in the Overdue Records List option of the Management Reports Menu. You are being prompted whether you wish to run the report for an entire institution (division) defined at your facility or a specific home location (file room). If run for one of your institutions, all home locations for that institution will be included on the report. You may enter:

> .\<RET\> to accept default institution

> .'H'OME LOCATION - you will subsequently be prompted for the home location

PULL LIST: {PULL LIST NAME}//

This prompt appears in the Create a Pull List option of the Pull List Functions Menu with the default being the name you entered at the beginning of the session. At this prompt, you are given the opportunity to edit or change the name of the pull list you are creating. You may enter:

> .\<RET\> if the name is correct

> .a new name (3-50 characters)

> .up-arrow \<^\> to abort processing; pull list will be deleted

PULL LIST NUMBER: {N}//

This prompt appears in the Create a Pull List option of the Pull List Functions Menu. It will appear with a default assigned by the system. This default will be the next consecutive number from the last entry made. If the last entry was out of sequence, the default will be consecutive to that entry. You may change the pull list number at this prompt if you wish. The system will not accept a number already used. You may enter:

> .\<RET\> to accept the default

> .another number (between 1 and 9999999)

REASON NOT TO RETIRE

This prompt appears in the Update Record's Attributes option of the Transaction Menu and is used to change the retirement status of a record. There are three possible retirement statuses as listed below. A record's retirement status is shown on its record inquiry which should always be checked prior to retiring a record. All records are assumed OK to retire unless otherwise specified through this field. At this prompt, you may enter:

> .\<RET\> to accept default (if there is one); if blank, the system will assume a retirement status of OK TO RETIRE

> .'T'EACHING to indicate record is used for teaching and should not be retired

> .'R' for TUMOR REGISTRY to indicate record is in the TUMOR REGISTRY and should not be retired

> .'O'K TO RETIRE

> .up-arrow \<^\>; present status will be assumed

REASON RECORD WAS MISSING

This prompt appears in the Flag a Record As Missing option of the Transaction Menu when removing a missing flag from a record. It may also appear in several other options when a missing record is selected for transaction and the user is prompted through the process of removing the missing flag. Your possible entries at this prompt are dependent upon the reasons established for use at your site. A \<?\> may be entered at this prompt and a list of acceptable reasons will be displayed from which you may select. Possible entries are:

> .reason record was missing (from list)

> .\<RET\> to leave blank

RECORD TYPE RESTRICTION

This prompt appears in the Create a Pull List option of the Pull List Functions Menu and may be used to designate a specific record type which should be requested for each patient subsequently entered; for example, you may wish to request only the latest volume of each patient's medical record. If this is the case, an entry in this field will streamline the session by eliminating the display of each patient's Short Record Inquiry and prompting for a selection upon entry of the patient's name. If you will be requesting a variety of record types and volumes, make no entry in this field. You may enter:

> .record type you wish to request on pull list (must be associated with your application)

> .\<?\> for a list of possible record types

> .\<RET\> to leave blank

> .up-arrow \<^\> to abort processing; pull list will be deleted

REQUESTING RECORD FOR WHICH BORROWER

This prompt appears in the Request a Record option of the Request Records Menu. The name of the borrower to which the record is to be charged should be entered at this prompt. The borrower must be active in your Borrowers/File Areas file. You may enter:

> .name of borrower

> .wand borrower's bar code label

REQUESTOR: {Name}

This prompt appears in the Edit a Request option of the Request Records Menu with a default of the previously entered requestor. At this prompt, you may change the requestor of the record. The requestor in this case is the same as the borrower to whom the record is to be charged. The requestor entered must be active in your borrowers/File Areas file. You may enter:

> .name of new requestor

> .\<RET\> or up-arrow \<^\>; default will be accepted

SELECT ADMITTING AREA

This prompt appears in the Admitting Area Chart Request option of the MAS Specific Menu when there is more than one admitting area defined in your site parameters. You are prompted for the name of the admitting area requesting the records. You may enter:

> .name of admitting area requesting record

> .\<?\> for a list from which to select

SELECT BORROWER

This prompt appears in a number of options in Record Tracking. It relates to the individual or location to which records are or will be charged. Your entry must be an active borrower in your Borrowers/File Areas file. You may enter:

> .name of borrower

> .\<?\> for a list from which to select

> .wand borrower's barcode label

SELECT DATE

This prompt appears in the Charge Out Pull List Records and Print Pull List(s) options of the Pull List Functions Menu. At this prompt, you should enter the date for which records on the pull list(s) being charged out or printed are requested.

SELECT HOLDING AREA

This prompt appears in the Charge Out Pull List Records option of the Pull List Functions Menu and is used when pull list records are being sent to a holding area prior to their going to the clinic or borrower for which they are requested. Your entry must be an active borrower in the Borrowers/File Areas file. You may enter:

> .name of holding area

> .\<?\> for a list from which to select

SELECT HOME LOCATION

This prompt appears in the Charged Records By Home Location and Overdue Records List options of the Management Reports Menu and is used to specify the home location for which you wish these reports to be run. You may enter:

> .name of home location

> .\<?\> for a list from which to select

SELECT INSTITUTION: {INSTITUTION}//

This prompt appears in the Overdue Records List option of the Management Reports Menu prompting you for the institution for which you wish to run the report. In this case, the term institution is synonymous with division. The prompt will only appear if more than one institution is defined at your site, and it will appear with a default which will be the institution associated with the user of the option. You may enter:

> .\<RET\> to accept the default

> .name of the institution for which you wish to run the report

SELECT LABEL DEVICE

Generally your site parameters will specify default label devices by label type for each file room and admitting area defined within your Record Tracking application. When it is necessary for a label to print, it will automatically print on the specified label device and this prompt will not appear. When no label device has been defined, this prompt will appear. Also, certain users have the ability to sign into Record Tracking and select the file room from which they wish to track records. Most users have access to one file room only. They are also prompted whether they wish to use that file room's default devices. If NO is answered, this prompt will appear whenever it is necessary for a label to print. If you are not one of these users and this prompt appears, it is recommended your application coordinator or site manager be notified to assure devices are defined in your site parameters.

This prompt may appear with a default. You may enter:

> .\<RET\> to accept default

> .device name/number as defined in your parameters on which to print

> .\<?\> for a list of devices from which to select

SELECT LABELS FROM LIST

This prompt appears in the Create a Label/Record/Volume option of the Transaction Menu. It will appear in conjunction with display of the selected patient's short record inquiry prompting you to select the record for which you wish to print a label. You may enter:

> .number of record from display for which you wish to print a bar code label

> .a range of numbers; i.e. 1-4

> .a combination of numbers separated by commas; i.e. 1,3,5

> .a combination of numbers separated by commas and a range; i.e. 1,3-5

> .\<RET\> or up-arrow \<^\> if you wish to create a new record or volume rather than print a bar code label

SELECT MISSING RECORD

This prompt appears in the Flag a Record As Missing option of the Transaction Menu asking you to specify the record you wish to flag as missing, remove missing flag from or approve/disapprove the finding of. You may enter:

> .wand the bar code label of the record

> .the Record Tracking identifier number

> .patient name

SELECT MOVEMENT TYPE

This prompt appears in the Inactive/Re-Activate Records and Transfer Records options of the Transaction Menu asking you to specify the action you wish to take. You may enter:

> .movement type you wish to make. Depending upon the option in which you are working, they may be:

> .'I'NACTIVATE

> .'R'EACTIVATE

> .TRANSFER BACK FROM OTHER VAMC

> .TRANSFER TO OTHER VAMC

> .\<?\> for a list of selectable movement types

SELECT NEW RECORD TYPE

This prompt appears in the Create a Label/Record/Volume option of the Transaction Menu asking you to specify the record type for which you wish to create a new or additional volume (i.e., master folder, medical record, administrative record, etc.). The possible selections will vary between sites and applications. You may enter:

> .record type for which you wish to create a new or additional volume (must be defined in your parameters)

> .\<?\> to view a list of possible selections

> .\<RET\> to return to the "Select PATIENT" prompt

SELECT PATIENT

This prompt appears in a number of options throughout Record Tracking asking you to enter the name of the patient whose records you wish to process or for whom you wish to view record information. The patient entered must already be in your database (Patient file) and in some cases must already have records in the Record Tracking system. Please refer to the appropriate option documentation, if needed, to ascertain whether the patient must have records in Record Tracking in order to be accepted.

SELECT PATIENT NAME

This prompt appears in the Patient Charge Out option of the Transaction Menu asking you to enter the name of the patient who is borrowing their own record. The patient must already be in your database. If they have no records in Record Tracking, the system will create them in accordance with your site parameters when the patient's name is entered at this prompt.

SELECT PULL LIST

This prompt appears throughout the Pull List Functions Menu asking you for the pull list with which you wish to work. In Charge Out Pull List Records and Print Pull List(s), it will appear with a default of ALL CLINIC LISTS. It also appears in the Retrieval Rate Statistics option of the Management Reports Menu asking for the pull list for which to run the report. You may enter:

> .pull list name

> .pull list number

> .date records are needed on pull list (a selection will be displayed)

> .\<RET\> if there is a default, it will be accepted; otherwise, processing will be aborted

It should be noted that if you are using the Print Pull List(s) option and wish to sort your pull list by other than terminal digits, a \<RET\> must be entered at this prompt (accepting the default of all) in order to subsequently be prompted for the method to sort the list; 'C'LINIC, 'A' to sort by clinic name then appointment time.

SELECT RECORD

This prompt appears in a number of Record Tracking options and is used to enter records for processing. The possible actions surrounding this prompt vary somewhat depending upon the option in which you are working. The action surrounding the entry of \<RET\> and up-arrow \<^\> also varies depending upon the option. In all cases, the following entries may be made whenever this prompt is displayed:

> .Record Tracking identifier number

> .wand record barcode label

> .patient name - patient's short record inquiry will subsequently be displayed from which you may select the appropriate record

The following options return you to this prompt repeatedly thereby allowing creation of a list of records which will be processed (or queued for processing) upon conclusion of the session: Charge Out Records, Check In Records, Inactivate/Reactivate Records, Re-Charge Records and Transfer Records of the Transaction Menu; Request a Record, Request Records Menu; and Create a Pull List and Add Records To Pull List of the Pull List Functions Menu. The following entries apply to these options:

> .If records have already been entered for processing during the session, they may be deleted from the list by entering a minus sign (-) plus the Record Tracking identifier number; i.e., -28. If you do not know the Record Tracking identifier number, you may first enter a \<?\> at this prompt and it will be displayed.

> .\<RET\> to signify the end of the session; records will be processed or queued for processing

The following options utilize this prompt for entering records for processing but do not return to it repeatedly allowing the creation of a list: Update Record's Attributes and Delete a Record of the Transaction Menu and Request a Record of the Request Records Menu. You may enter a record for processing as described above.

SELECT {PATIENT NAME}'S RECORDS FROM LIST

This prompt appears throughout Record Tracking in conjunction with display of the patient's short record inquiry. You may select from the short record inquiry those of the patient's records you wish to process. You may enter:

> .number(s) of records to be processed; you may enter a single number, several single numbers separated by commas, a range of numbers separated by a dash or a combination; i.e. 1,3,4 or 1-3, or 1-3,5,7

SELECT RECORD TRACKING APPLICATION

This prompt will appear for those users who have access to more than one Record Tracking application; i.e. site managers, application coordinators, etc. Most users have access to only one. At this prompt, you should enter the Record Tracking application in which you wish to work; MAS or Radiology.

SELECT RECORD TRACKING FILE ROOM

This prompt will appear for those users who have access to more than one Record Tracking file room; i.e. site managers, application coordinators, supervisors, managers. At this prompt, you should enter the name of the file room from which you wish to track records. This prompt may appear with a default. You may enter:

> .\<RET\> to accept the default

> .name of file room (as it appears in your parameters) from which you wish to track records

SELECT RECORD TYPE

This prompt appears in the Multiple New Volume Creation and New Volume Creation options of the Transaction Menu as well as the Record Inquiry option on the Record Information Menu and is used to specify the record type with which you wish to work; i.e. medical record, chest films, etc. Record types will vary between sites and applications. A question mark may be entered for a list from which to select.

SELECT REQUEST

This prompt appears in a number of Request Records and Pull List Functions Menu options and is used to designate the request with which you wish to work. You may enter the following at this prompt:

> .request number

> .wand request label

> .patient name - patient's request profile will subsequently be displayed from which you may select the appropriate request

SELECT TYPE OF LIST? ALL//

This prompt appears in the Print Pull List(s) option of the Pull List Functions Menu and is used to designate the information you wish to include on the pull list(s) being printed. You may enter:

> .\<RET\> to accept default; ALL requests will be printed

> .'N'ON-FILLABLE; only requests which have been designated NON-FILLABLE will be printed

> .'D'ETAILED NON-FILLABLE; all NON-FILLABLE requests will be printed along with the Combination Data Trace Report of the record which traces past record locations as well as future clinic appointments. (This report may also be obtained through the Combination Data Trace option of the Record Information Menu.)

SUPERVISOR COMMENTS

This prompt appears in the Flag a Record As Missing option of the Transaction Menu. It is a word processing field in which comments pertaining to the missing record may be entered. You may enter:

> .comment pertaining to missing record

> .\<RET\> to leave blank

TEMPORARY COMMENT:

This prompt appears in the Patient Charge-Out option of the Transaction Menu allowing you to enter a free text (2-75 characters) comment pertaining to the charge-out. This comment will appear on the patient's short record inquiry until such time as the system records the record as being returned. This comment is optional and may be left blank by entering a \<RET\>.

TO DATE:

This prompt appears in the Retrieval Rate Statistics option of the Management Reports Menu asking for an ending date in the date range for which you wish to run the report.

TRACE CUT-OFF DATE: T-l00//

This prompt appears in the Combination Data Trace option of the Record Information Menu and is used to specify how many days in the past you wish the report to compile record activities. Assuming the information has not been purged, you may track back as far as 999 days. You may enter:

> .\<RET\> to accept default; report will reflect the past 100 days of activity

> .another cut-off date (must be a past date)

TRANSFER INSTITUTION

This prompt appears in the Transfer Records option of the Transaction Menu and is used to designate the facility to which you are transferring records. You may enter:

> .name or number of institution to which you are transferring records (must be in your Institution file)

> .\<?\> for display of your Institution file from which you may select

TRANSFER REQUESTS TO VOLUME 'N'? NO//

YES/NO This is the final prompt in the Move Requests To Last Volume option of the Transaction Menu confirming whether you wish to transfer record requests to the volume entered.

<u>UPDATE BORROWER INFORMATION</u>

PHONE#

LOCATION/ROOM

Depending upon site parameters, this prompt may appear following selection of a borrower in a number of Record Tracking options. It is used to update the phone# and location of the selected borrower as it appears in the Borrowers/File Areas file. If the information is already in the file, these fields will appear with defaults and you may enter a \<RET\> to accept the defaults. You may also edit the current information.

VOLUMES REQUESTED: LATEST VOLUME//

This prompt appears in the Create a Pull List option of the Pull List Functions Menu and is used to specify what volumes you will be requesting on the pull list. You may enter:

> .\<RET\> to accept default (only the latest volume of the record type specified will be requested on the pull list)

> .'A'LL VOLUMES

> .up-arrow \<^\> to abort processing; pull list will be deleted

WHERE WAS THE RECORD FOUND

This prompt appears in the Flag a Record As Missing option of the Transaction Menu when removing a missing flag or when removing a missing flag from a record through another option. You may enter:

> .name of borrower/file area where record was found (must be in Borrowers/File Areas file)

> .\<RET\> or up-arrow \<^\> to abort processing; missing flag will not be removed

WOULD YOU LIKE TO PRINT A BARCODE LABEL? No//

This prompt appears in the Charge-Out Records and Check-In Records options of the Transaction Menu when a single record is selected from a patient's short record inquiry, rather than by wanding the bar code label or entering the record identifier number. This gives you the opportunity to print a barcode label, if the record does not already have one. Note that it will only appear when a single record is selected from a patient's short record inquiry (not multiple records). You may enter:

> .\<RET\> or NO

> .YES; barcode label will be printed on the appropriate default device or, if not defined in your site parameters, you will be prompted for a device on which to print