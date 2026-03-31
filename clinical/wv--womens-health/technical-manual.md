---
title: Women's Health Version 1 Technical Manual and Package Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: and Package Security Guide
app_code: WV
app_name: Womens Health
section: CLI
app_status: active
pkg_ns: WV
patch_ver: 1
patch_id: WV*1
group_key: "WV:WV:1"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Women’s Health (WH) software provides tracking functionality for procedures of particular interest to women patients (e.g., screening mammogram). The software provides a full range of breast and gynecologic cancer screening and tracking functions. The intended users of the software are primari
audience: 
keywords: 
  - blockquote
  - class
  - table
  - contents
  - even
  - chapter
  - colspan
  - style
  - width
  - notification
page_count: 0
word_count: 4247
section_count: 16
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=109"
---

> ![](women-s-health-version-1-technical-manual-and-package-security-guide/001.png)

WOMEN’S HEALTH

TECHNICAL MANUAL AND PACKAGE SECURITY GUIDE

September 1998

> Department of Veterans Affairs Software Service

Clinical Support Product Line

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
- [Chapter 1 Implementation and Maintenance](#chapter-1-implementation-and-maintenance)
  - [Description](#description)
  - [Main Features](#main-features)
  - [Patients, Procedures, and Notifications](#patients-procedures-and-notifications)
  - [Case Managers and the Program Manager](#case-managers-and-the-program-manager)
  - [The Basic Patient Management Loop](#the-basic-patient-management-loop)
  - [Treatment Need Due Date](#treatment-need-due-date)
  - [Procedure Complete by Date](#procedure-complete-by-date)
  - [Notification Complete by Date](#notification-complete-by-date)
  - [Summary](#summary)
  - [Installation of Software:](#installation-of-software)
- [Chapter 2 Routine Descriptions](#chapter-2-routine-descriptions)
  - [Routines to Map](#routines-to-map)
  - [Routine List with Descriptions](#routine-list-with-descriptions)
- [Chapter 3 File List and Related Information](#chapter-3-file-list-and-related-information)
  - [Package Default Definition](#package-default-definition)
- [Chapter 4 Exported Options](#chapter-4-exported-options)
- [Chapter 5 Archiving and Purging](#chapter-5-archiving-and-purging)
- [Chapter 6 Callable Routines](#chapter-6-callable-routines)
- [Chapter 7 External Relations](#chapter-7-external-relations)
- [Chapter 8 Internal Relations](#chapter-8-internal-relations)
- [Chapter 9 Package-wide Variables](#chapter-9-package-wide-variables)
- [Chapter 10 On-Line Documentation](#chapter-10-on-line-documentation)
- [Chapter 11 SACC Exemptions](#chapter-11-sacc-exemptions)
- [Chapter 12 Software Product Security](#chapter-12-software-product-security)
  - [Security Management.](#security-management)
  - [Security Features:](#security-features)
- [Glossary](#glossary)
> The Women’s Health Technical Manual and Package Security Guide has been developed for IRMS (Information Resource Management Service) and CIOFO (Chief Information Office Field Office) support personnel and contains technical information on the application. The content covers: software implementation and maintenance, routine descriptions, a file list, an exported option list, cross-references, archiving and purging, callable routines, external relations, package- wide variables, on-line documentation, and package security issues.
> This Women’s Health Technical Manual and Package Security Guide is one of three manuals associated with the application. Information discussing the functionality of the software's menus and options is found in the Women’s Health User Manual. Information critical to the successful installation of the software can be found in the Women’s Health Installation Guide.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Women’s Health (WH) software provides tracking functionality for procedures of particular interest to women patients (e.g., screening mammogram). The software provides a full range of breast and gynecologic cancer screening and tracking functions. The intended users of the software are primarily WH coordinators and case managers. Providers may use selected patient management and report options.

> This software is based on the Indian Health Service (IHS) Resource and Patient Management System (RPMS) Women’s Health software V. 2.0, and modified from suggestions provided by the V*IST*A Women’s Health Technical Advisory Group (TAG).

> Credit for the development of the V*IST*A WH software goes to the Indian Health Service and in particular, to <span class="mark">REDACTED</span> who is the original developer of the IHS software.

# Chapter 1 Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter provides guidelines for implementing the Women’s Health application. It is important to complete all of the steps contained in this chapter before assigning menu options to clinical staff.

> Women’s Health is found in the WV namespace. All routines, templates and options begin with WV. File numbers are in the range of 790 through 794 and are stored in the ^WV global.

## Main Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Women’s Health software is composed of three main modules: Patient Management, Management Reports, and Manager’s Functions.

> Patient Management is the portion of the software used to manage individual patient care, that is, their procedures, due dates and correspondence. Under the Patient Management menu it is possible to maintain patient data such as the date of the next PAP smear, colposcopy or mammogram, the patient's pregnancy and her EDC (due date), as well as the patient's current PAP regimen. It is also possible to track the patient's individual procedures: the date performed, the provider and clinic, the results or diagnosis, etc. Notifications (letters and phone calls) may also be tracked. A file of form letters has been included in the software, and these letters may be edited and personalized for a clinic's particular needs. Reminder letters can be queued months in advance of a future appointment, then printed and mailed out shortly before the tentative appointment.

> Management Reports is the portion of the software used to print epidemiological reports such as the number of women who received a mammogram for the selected time period, or the number of patients having abnormal PAP results during a selected time period. Under the Management Reports menu it is possible to produce lists of patients who are past their due dates for follow-up procedures. It is also possible to store program statistics by date for later comparison of program trends and progress.

> Manager’s Functions is that portion of the software that provides the ADPAC with a set of utilities for configuring the software to the specific needs of the site. It also provides utilities for other program needs, such as customizing tables, making special edits to patient data (e.g., pregnancy log, PAP regimen log), printing notification letters, running error reports, and documenting laboratory results. By using the File Maintenance options under the Manager’s Functions menu, it is possible to maintain site specific parameters such as the text of form letters, the types of notifications and their synonyms, how and when letters get printed, and several defaults relating to dates.

## Patients, Procedures, and Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are primarily three distinct data sets within the WH application and they can be categorized as patient, procedure, and notification related.

> Patients refer to the women in the program register. Data stored for each patient includes demographic data, the patient's case manager, the current or next cervical and breast treatment need and its due date, the patient's PAP regimen along with the date it began, and other data. This type of data is referred to as the patient's case data.

> Procedures refer to any of the diagnostic and therapeutic tests, exams, or other interventions tracked by the software. The table of procedure types includes PAP smear, colposcopy, mammogram, LEEP, cone biopsy, ECC, and others. The results or diagnosis associated with the gynecologic procedures are chosen from a table of Bethesda-consistent terminology.

> Mammogram results use the American College of Radiology (ACR) terminology.

> Notifications refer to any type of communication or correspondence with the patient, such as first, second and third letters, certified letters, phone calls, messages left, etc. Notifications, which take the form of letters, fall into two categories: results letters and reminder letters. Result letters inform the patient of the findings of a recent procedure and are queued to print immediately. Reminder letters inform the patient of the need to schedule her next appointment and are queued to print at some time several weeks or months in the future.

> Selected reports that look at the due dates of patients' treatment needs (using both the procedure and notification data sets) provide a comprehensive mechanism for guarding against losing patients to follow-up.

## Case Managers and the Program Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Every patient that is entered into the Women’s Health database (or ‘register’) is assigned a case manager. A case manager is a user of Women’s Health (a registered nurse, LPN, nurse practitioner, or a women veterans health coordinator) who is responsible for managing and tracking a woman's health care needs. This includes treatment planning, tracking of procedures, editing patient data, selecting appropriate letters, scanning for delinquent follow-up care, and more. A small clinic using Women’s Health may have only one case manager. Larger clinics and hospitals may have several. In some cases, the tasks associated with the software may be assigned to clerical personnel under on the supervision of a licensed care provider.

> The program manager or ADPAC is the person chiefly responsible for the setup and operation of the Women’s Health package at a given site. This person works with the IRM Service on the technical aspects of the software and performs maintenance tasks that require a more detailed understanding of the software than is required of case managers. At small sites, the program manager may also be the only case manager.

## The Basic Patient Management Loop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The function of the Women’s Health software is best understood in terms of the Basic Patient Management Loop (please refer to the flowchart in this section).

> The loop is a sequence of events that occur over and over again during a patient's health care cycle.

> This software uses the concept of procedures and notifications being open and closed. Procedures and notifications will become delinquent if they are not closed by the ‘Complete by (Date)’ field found in the notification and procedure screens. If a procedure or notification is not closed by its due date, this will be an indicator that the patient may be ‘lost’ to follow-up.

> Generally, a procedure is closed when the results or diagnosis for that procedure are entered. A notification is closed either at the time it is printed (as in the case of a results letter) or when the patient returns for her next appointment (as in the case of a reminder letter).

> An example of the Basic Patient Management Loop would be the following: A new patient arrives at the clinic for care. The patient's case data (PAP and MAM treatment needs, EDC, etc.) are entered into the Women’s Health program. A procedure is performed (such as a PAP smear). The procedure is entered into the computer, an accession number is assigned to the procedure, and the specimen is sent to a lab for diagnosis. After a period of days, results are returned from a lab and entered for the procedure and this procedure is then closed. At that time, one and possibly two separate notification letters are selected from the Purpose of Notification file. The first letter, a results letter, informs the patient of the results of the procedure. This letter is printed immediately. The second letter, a reminder letter, will advise the patient to call the clinic in order to schedule her next appointment. This second letter is queued to print one year later (assuming the PAP was normal). Twelve months later, in response to the reminder letter, the patient calls to schedule her next appointment. When she returns to the clinic for her next procedure, the Patient Management Loop begins again: procedure... results...results letter & reminder letter...call for an appointment...procedure.

> When the patient returns for a procedure, it is important to close the reminder letter that prompted her appointment; otherwise, the reminder letter will be left open and begin to show up as delinquent on the past due reports.

Basic Patient Management Loop

> As noted earlier, the reports that look for the due dates of patients' treatment needs (for procedures, and notifications) provide a comprehensive mechanism for guarding against losing patients to follow-up. The three sets of ‘due dates’ are as follows:

## Treatment Need Due Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Stored as part of each patient’s case data are breast treatment needs and gynecologic treatment needs. These needs are chosen from a table and given a due date, such as, ‘Routine PAP (by 7/1/95)’. The Women’s Health software offers a report that will display/print all of the patients with treatment needs past due.

## Procedure Complete by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A ‘Complete by Date’ is stored as part of each procedure a patient receives. When a procedure is first entered, it receives a status of ‘Open’. When the results of the procedure are returned and entered, the status is generally changed to ‘Closed’. If a procedure’s status remains ‘Open’ after its ‘Complete by Date’, the procedure will begin to display on reports that look for procedures that are past due.

## Notification Complete by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A ‘Complete by Date’ is stored as part of each notification a patient receives. When a notification is first entered, it receives a status of ‘Open’. If the notification is a result letter (to be printed immediately) or a phone call, it is generally given an outcome and a status of ‘Closed’. If the notification is a reminder letter, its status is left ‘Open’ until the patient’s next procedure is entered. If a notification’s status remains ‘Open’ after its ‘Complete by Date’, the notification will begin to display on reports that look for notifications that are past due.

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In summary, Women’s Health is largely a patient management tool for tracking the breast and gynecologic treatment needs of women, the procedures they receive, and the communications between healthcare staff and women regarding their treatment and follow-up. The software also provides some program-wide epidemiological reports which are of use to clinicians and program administrators.

## Installation of Software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the first version of the V*IST*A Women’s Health package. Some VA facilities are running the Indian Health Service Women’s Health software (namespace is BW, file range is 9002086- 9002086.93). This installation will copy the IHS data into the V*IST*A Women’s Health files. It will not change the IHS database and will remain as a legacy database until otherwise determined by the ADPAC and the women veterans coordinator.

1.  Setting up the software environment.

> Information Resource Management Services staff should install the software using the Installation Guide in a test environment prior to installing the software in the production (VAH) account. The following V*IST*A packages should reside in the environment where the Women’s Health application is to be installed:

1.  VA FileMan V. 21 or greater,
2.  Kernel V. 8.0 or greater,
3.  Kernel Toolkit V. 7.3 or greater,
4.  PIMS V. 5.3 or greater,
5.  Radiology/Nuclear Medicine V. 5.0 or greater (optional),
6.  MailMan V. 7.1 or greater.

> If Radiology/Nuclear Medicine V. 5.0 and patch RA\*5.0\*2 are installed patient mammograms can be automatically entered into the Women’s Health database.

> Data entered into the test environment CANNOT be transferred into the production environment. It is recommended that a limited amount of data be entered into the test directory in order for the user to become familiar with the application and to establish an acceptable training data base.

2.  Editing site configurable files.
    1.  The WV EDIT SITE PARAMETERS option edits the WV SITE PARAMETER (#790.02) file.
    2.  The WV ADD/EDIT REFERRAL SOURCE option edits the WV REFERRAL SOURCE (#790.07) file.
    3.  The WV EDIT DIAG TRANSLATION option edits the WV DIAGNOSTIC CODE TRANSLATION (#790.32) file.
    4.  The WV ADD/EDIT NOT PURPOSE&LETTER option edits the WV NOTIFICATION PURPOSE (#790.404) file.
    5.  The WV ADD/EDIT NOTIF OUTCOME option edits the WV NOTIFICATION OUTCOME (#790.405) file.
    6.  The WV ADD/EDIT CASE MANAGERS option edits the WV CASE MANAGER (#790.01) file.

> Review the above populated site configurable files. The options, which allow the application coordinator to edit the file's data, are all located in the File Maintenance Menu.

3.  Automatically loading files.

> At this time, the WV Patient (#790) file can be preloaded with the names of women patients from the Patient (#2) file. This may be done using the Automatically Load Patients option. The mammogram reports from the Radiology/Nuclear Medicine package may also be automatically loaded into the Women’s Health package by using the option Import Radiology/NM Exams. For further information on these options, refer to Chapter 2.

4.  Queueing TaskMan jobs.

> There are no options that need to be queued to run.

5.  Accessing menus.

> There are no security keys in this application.

6.  Assigning menus.

> The Women’s Health Menu \[WVMENU\] should be assigned to the ADPAC and the individual having primary responsibility for managing and editing data in this tracking package.

> The Patient Management \[WV MENU-PATIENT MANAGEMENT\] and Management Reports \[WV MENU-MANAGEMENT REPORTS\] should be assigned to all women’s health coordinators and case managers who have not been assigned the Women’s Health Menu option. These two options may also be assigned to appropriate clinicians and women’s health clinical directors as required.

> The Lab Data Entry Menu \[WV MENU-LAB DATA ENTRY\] should be assigned to laboratory personnel who may be assigned to enter cytology reports into the WH database.

7.  Printer issues.

> There are no special printer issues.

8.  Resource Requirements.

> The size of the table files that come with the package are insignificant. Data storage for the package is very roughly 2 megabytes per 1000 patients per year.

# Chapter 2 Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no routines that need to be mapped.

## Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is a list of routines associated with the Women’s Health package including pre- and post- init routines.

> WVBRDUP Called by option "WV BROWSE PROCEDURES DUPLICATE" to

> identify, list and browse possible duplicate procedures.

> WVBRNED Called by option "WV BROWSE NEEDS PAST DUE" to browse and edit patients with treatment needs past due.

> WVBRNED1 Display code for browsing treatment needs. Called by WVBRNED. WVBRNEDH Help text for selecting criteria when browsing treatment needs. Called by

> WVBRNED.

> WVBRNOT Called by option "WV BROWSE NOTIFICATIONS" to browse and edit notifications.

> WVBRNOT1 Display code for browsing notifications. Called by WVBRNOT. WVBRNOT2 Prompts for selection criteria when browsing notifications. Called by

> WVBRNOT.

> WVBRPCD Called by option "WV BROWSE PROCEDURES" to browse and edit procedures.

> WVBRPCD1 Display code for browsing procedures. Called by BRBRPCD. WVBRPCD2 Prompts for selection criteria in browsing procedures. Called by

> WVBRPCD.

> WVBRPCD3 Help prompts for browsing procedures. Called by BRBRPCD.

September 1998 Women’s Health V. 1.0 2.1

Technical Manual and Package Security Guide

> WVCMGR Called by option "WV ADD/EDIT CASE MANAGERS" to add and edit case managers.

> WVDIAG Called by option "WV PRINT RES/DIAG FILE" to print the results/diagnosis table file.

> WVDIAGS Add/edit/print/purge synonyms for WV Results/Diagnosis file. WVENV Environment check routine.

> WVEXPTRA Add mammograms to WH which were performed before WH was installed.

> WVFACE Display/print a fact sheet, using a PIMS supported routine call.. WVFMAN Calls to FileMan with pre- and post-call variable setting.

> WVGETALL Automatically loads women patients from the main patient file, limited by age.

> WVLAB Allows Lab users to add/edit a procedure to the WH database.

> WVLABLG Allows Lab users to display/print a list of WH procedures that were entered.

> WVLABLG1 Allows Lab users to display/print a list of WH procedures that were entered.

> WVLABLG2 Allows Lab users to display/print a list of WH procedures that were entered.

> WVLETDQ Called by option "WV PRINT QUEUED LETTERS" to print letters by "APRT" xref in ^WV(790.4,"APRT".

> WVLETPR Called by option "WV PRINT INDIVIDUAL LETTERS" to print a letter for a single individual (as opposed to all those queued).

> WVLOGO Displays login data. Gets version number from line 2 of this routine.

> WVMGRP Called by different options to edit a patient's pap regimen log and pregnancy log.

> WVNOTIF Called by different options to add/edit notifications.

> WVNOTIF1 Stuffs a normal letter for this patient. Called by WVNOTIF.

> WVPATE Patient case data edit, called by option "WV EDIT PATIENT CASE DATA".

> WVPATP Print a patient's case data.

> WVPOST Post-installation routine.

> WVPRE Pre-init routine to copy IHS data.

> WVPROC Called by various options to add/edit procedures.

> WVPROC1 Edit a procedure, also a follow-up screen. Called by WVPROC. WVPROF Called by option "WV PATIENT PROFILE" to display profile. WVPROF1 Setup and edit code for displaying patient profile. Called by WVPROF.

> WVPROF2 Retrieve and sort procedures, notifications, pap regimens, and pregnancies for patient profile. Called by WVPROF.

> WVPROF3 Display code for patient profile. Called by WVPROF1.

> WVPRPCD Display code for printing procedures. Entry points for printing individual procedures and all new procedures.

> WVPURP Add/edit/print notification purpose file entries, edit notification type synonyms, add/edit notification outcomes.

> WVRAD Edit/print WV mammogram diagnosis code translations file. WVRADWP Gets Radiology/Nuclear Medicine report data for display.

> WVRALINK Routine called by Radiology/Nuclear Medicine package when a Radiology/NM report is verified, unverified or deleted.

> WVREFUSE Adds/Enters/Manipulates procedure refusals.

> WVRPPCD Report containing procedures statistics; called by option "WV PRINT PROCEDURE STATS".

> WVRPPCD1 Display code for procedure statistics report. Called by WVRPPCD.

> WVRPPCD2 Report containing procedure statistics and collating code. Called by WVRPPCD.

> WVRPSCR This report will display screening rates for paps & mams. WVRPSCR1 Continuation of WVRPSCR.

> WVRPSCR2 Continuation of WVRPSCR1.

> WVRPSNP Called by option "WV PRINT SNAPSHOT" to display current or fiscal year to present day package indicators (e.g., \#patients, \#paps, \#mams, \#delinquent needs, etc.).

> WVRPSNP1 Continuation of WVRPSNP.

> WVRPSNPR Called by option "WV PRINT/RETRIEVE SNAPSHOT" to display a previous snapshot.

> WVRPST Prints the Sexual Trauma Summary report.

> WVSELECT Utility to prompt for multiple selections from a file and store them in a local array by calling program.

> WVSITE Called by option "WV EDIT SITE PARAMETERS" to edit site parameters.

> WVUTL1 Utility to handle patient demographics, needs, and regimens, and also display priority and procedure type.

> WVUTL1A Continuation of WVUTL1.

> WVUTL2 Utility to handle ZIS, mumps xrefs on normal/abnormal and on status. WVUTL3 Utility to handle asking date range, locks, DIR prompts, store/delete EDC,

> and store pap regimen.

> WVUTL4 Utility to handle default "COMPLETE BY" dates for notifications and procedures, status text, diagnosis text, normal value, colposcopy value, and margin value.

> WVUTL5 Utility to handle setting up variables, generate accession#, and title.

> WVUTL6 Utility to handle text for provider, procedure, hospital location, and institution. Compute default print date.

> WVUTL7 Utility to handle headers and trailers.

> WVUTL8 Utility to handle patient lookup, and select for report.

> WVYNOTP Routine generated by the “WV PRINT NOTIF PURPOSE&LETTER” print template.

# Chapter 3 File List and Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> File Number File Name Global

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 54%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>790</th>
<th></th>
<th>WV</th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th>^WV(790,</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>790.01</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>CASE MANAGER</p>
</blockquote></td>
<td>^WV(790.01,</td>
</tr>
<tr class="even">
<td>790.02</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>SITE PARAMETER</p>
</blockquote></td>
<td>^WV(790.02,</td>
</tr>
<tr class="odd">
<td>790.03</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>PAP REGIMEN</p>
</blockquote></td>
<td>^WV(790.03,</td>
</tr>
<tr class="even">
<td>790.04</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>PAP REGIMEN LOG</p>
</blockquote></td>
<td>^WV(790.04,</td>
</tr>
<tr class="odd">
<td>790.05</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>PREGNANCY LOG</p>
</blockquote></td>
<td>^WV(790.05,</td>
</tr>
<tr class="even">
<td>790.07</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>REFERRAL SOURCE</p>
</blockquote></td>
<td>^WV(790.07,</td>
</tr>
<tr class="odd">
<td>790.1</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>PROCEDURE</p>
</blockquote></td>
<td>^WV(790.1,</td>
</tr>
<tr class="even">
<td>790.2</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>PROCEDURE TYPE</p>
</blockquote></td>
<td>^WV(790.2,</td>
</tr>
<tr class="odd">
<td>790.3</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>REFUSALS</p>
</blockquote></td>
<td>^WV(790.3,</td>
</tr>
<tr class="even">
<td>790.31</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>RESULTS/DIAGNOSIS</p>
</blockquote></td>
<td>^WV(790.31,</td>
</tr>
<tr class="odd">
<td>790.32</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>DIAGNOSTIC CODE TRANSLATION</p>
</blockquote></td>
<td>^WV(790.32,</td>
</tr>
<tr class="even">
<td>790.4</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION</p>
</blockquote></td>
<td>^WV(790.4,</td>
</tr>
<tr class="odd">
<td>790.403</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATIN TYPE</p>
</blockquote></td>
<td>^WV(790.403,</td>
</tr>
<tr class="even">
<td>790.404</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION PURPOSE</p>
</blockquote></td>
<td>^WV(790.404,</td>
</tr>
<tr class="odd">
<td>790.405</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION OUTCOME</p>
</blockquote></td>
<td>^WV(790.405,</td>
</tr>
<tr class="even">
<td>790.5</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>CERVICAL TX NEED</p>
</blockquote></td>
<td>^WV(790.5,</td>
</tr>
<tr class="odd">
<td>790.51</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>BREAST TX NEED</p>
</blockquote></td>
<td>^WV(790.51,</td>
</tr>
<tr class="even">
<td>790.6</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>LETTER</p>
</blockquote></td>
<td>^WV(790.6,</td>
</tr>
<tr class="odd">
<td>790.71</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>SNAPSHOT REPORTS</p>
</blockquote></td>
<td>^WV(790.71,</td>
</tr>
<tr class="even">
<td>790.72</td>
<td></td>
<td>WV</td>
<td><blockquote>
<p>AGE RANGE DEFAULT</p>
</blockquote></td>
<td>^WV(790.72,</td>
</tr>
</tbody>
</table>

## Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE #</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>UP DATE DD</p>
</blockquote></th>
<th><blockquote>
<p>SEND SEC. CODE</p>
</blockquote></th>
<th><blockquote>
<p>DATA COMES W/FILE</p>
</blockquote></th>
<th><blockquote>
<p>SITE DATA</p>
</blockquote></th>
<th><blockquote>
<p>RSLV PTS</p>
</blockquote></th>
<th><blockquote>
<p>USER OVER RIDE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>790</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.01</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>CASE MANAGER</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.02</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>SITE PARAMETER</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.03</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PAP REGIMEN</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.04</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PAP REGIMEN LOG</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.05</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PREGNANCY LOG</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.07</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>REFERRAL SOURCE</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.1</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PROCEDURE</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.2</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>PROCEDURE TYPE</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.3</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>REFUSALS</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.31</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>RESULTS/DIAGNOSIS</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.32</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>DIAGNOSTIC CODE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>TRANSLATION</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.4</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.403</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATIN TYPE</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.404</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION PURPOSE</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.405</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION OUTCOME</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.5</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>CERVICAL TX NEED</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.51</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>BREAST TX NEED</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.6</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>LETTER</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.71</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>SNAPSHOT REPORTS</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.72</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>AGE RANGE DEFAULT</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Chapter 4 Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a menu diagram for Women’s Health.

> Women’s Health Menu (WVMENU)

> \|

> \|

> ---PM Patient -----------------------------------------PC Edit/Print

> Management \[WV Patient Case

> MENU-PATIENT Data \[WV EDIT

> MANAGEMENT\] PATIENT CASE

> \| DATA\]

> \|

> \|--------------------------------------------PP Patient Profile

> \| \[WV PATIENT

> \| PROFILE\]

> \|

> \|--------------------------------------------FS Print Patient

> \| Demographic Info

> \| (Face Sheet) \[WV

> \| PATIENT

> \| DEMOGRAPHIC

> \| INFO\]

> \|

> \|--------------------------------------------BD Browse Patients

> \| With Needs Past

> \| Due \[WV BROWSE

> \| NEEDS PAST DUE\]

> \|

> \|--------------------------------------------AP Add a NEW

> \| Procedure \[WV

> \| ADD A NEW

> \| PROCEDURE\]

> \|

> \|--------------------------------------------EP Edit a Procedure

> \| \[WV EDIT

> \| PROCEDURE\]

> \|

> \|--------------------------------------------BP Browse

> \| Procedures \[WV

> \| BROWSE

> \| PROCEDURES\]

> \|

> \|--------------------------------------------PR Print a

> \| Procedure \[WV

> \| PRINT A

> \| PROCEDURE\]

> \|

> \|-------------------------------------------HIS Add an

> \| HISTORICAL

> \| Procedure \[WV

> \| ADD AN

> \| HISTORICAL

> \| PROCEDURE\]

> \|

> \|--------------------------------------------RA Add a Refusal of

> \| Treatment \[WV

> \| REFUSED

> \| PROC-ADD\]

> \|

> \|--------------------------------------------RE Edit a Refusal

> \| of Treatment \[WV

> \| REFUSED

> \| PROC-EDIT\]

> \|

> \|--------------------------------------------AN Add a New

> \| Notification \[WV

> \| ADD A NEW

> \| NOTIFICATION\]

> \|

> \|--------------------------------------------EN Edit a

> \| Notification \[WV

> \| EDIT

> \| NOTIFICATION\]

> \|

> \|--------------------------------------------BN Browse

> \| Notifications

> \| \[WV BROWSE

> \| NOTIFICATIONS\]

> \|

> \|--------------------------------------------PL Print Individual

> \| Letters \[WV

> \| PRINT INDIVIDUAL

> \| LETTERS\]

> \|

> \|--------------------------------------------PQ Print Queued

> Letters \[WV PRINT QUEUED LETTERS\]

> ---MR Management --------------------------------------PS Procedure

> Reports \[WV Statistics

> MENU-MANAGEMENT Report \[WV PRINT

> REPORTS\] PROCEDURE STATS\]

> \|

> \|--------------------------------------------SN Snapshot of the

> \| Program Today

> \| \[WV PRINT

> \| SNAPSHOT\]

> \|

> \|--------------------------------------------RS Retrieve/Print

> \| Earlier

> \| Snapshots \[WV

> \| PRINT/RETRIEVE

> \| SNAPSHOT\]

> \|

> \|--------------------------------------------CR Compliance Rates

> \| for PAPs and

> \| MAMs \[WV PRINT

> \| COMPLIANCE

> \| RATES\]

> \|

> \|--------------------------------------------BP Browse Patients

> \| With Needs Past

> \| Due \[WV BROWSE

> \| NEEDS PAST DUE\]

> \|

> \|--------------------------------------------ST Sexual Trauma

> Summary Report \[WV SEXUAL TRAUMA SUMMARY\]

> ---MF Manager's -------------FM File Maintenance -----AEP Add/Edit a Functions \[WV Menu \[WV Notification

MENU-MANAGER'S MENU-FILE Purpose & Letter

FUNCTIONS\] MAINTENANCE\] \[WV ADD/EDIT NOT

> \| \| PURPOSE&LETTER\]

> \| \|

> \| \|

> \| \|-----------------PPL Print

> \| \| Notification

> \| \| Purpose & Letter

> \| \| File \[WV PRINT

> \| \| NOTIF

> \| \| PURPOSE&LETTER\]

> \| \|

> \| \|-----------------ESN Edit Synonyms

> \| \| for Notification

> \| \| Types \[WV EDIT

> \| \| NOTIF TYPE

> \| \| SYNONYM\]

> \| \|

> \| \|-----------------OUT Add/Edit

> \| \| Notification

> \| \| Outcomes \[WV

> \| \| ADD/EDIT NOTIF

> \| \| OUTCOME\]

> \| \|

> \| \|-----------------ESP Edit Site

> \| \| Parameters \[WV

> \| \| EDIT SITE

> \| \| PARAMETERS\]

> \| \|

> \| \|------------------CM Add/Edit Case

> \| \| Managers \[WV

> \| \| ADD/EDIT CASE

> \| \| MANAGERS\]

> \| \|

> \| \|------------------TR Transfer a Case

> \| \| Manager's

> \| \| Patients \[WV

> \| \| TRANSFER CASE

> \| \| MANAGER\]

> \| \|

> \| \|----------------AUTO Automatically

> \| \| Load Patients

> \| \| \[WV AUTOLOAD

> \| \| PATIENTS\]

> \| \|

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 52%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>|</p>
</blockquote></th>
<th><blockquote>
<p>| RAD</p>
</blockquote></th>
<th><blockquote>
<p>Import</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Radiology/NM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Exams [WV IMPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>RAD/NM EXAMS]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| PRD</p>
</blockquote></td>
<td><blockquote>
<p>Print</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Results/Diagnosi</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>s File [WV PRINT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>RES/DIAG FILE]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| ESR</p>
</blockquote></td>
<td><blockquote>
<p>Edit Synonyms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>for</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Results/Diagnose</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>s [WV EDIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>RES/DIAG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYMS]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| PSR</p>
</blockquote></td>
<td><blockquote>
<p>Print Synonyms</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>for</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Results/Diagnose</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>s [WV PRINT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>RES/DIAG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYMS]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| EDX</p>
</blockquote></td>
<td><blockquote>
<p>Edit Diagnostic</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Code Translation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>File [WV EDIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>DIAG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>TRANSLATION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| PDX</p>
</blockquote></td>
<td><blockquote>
<p>Print Diagnostic</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Code Translation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>File [WV PRINT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>DIAG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>TRANSLATION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>| RS</p>
</blockquote></td>
<td><blockquote>
<p>Add/Edit to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Referral Source</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>File [WV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ADD/EDIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REFERRAL SOURCE]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \|--------------------------------------------PQ Print Queued

> \| Letters \[WV

> \| PRINT QUEUED

> \| LETTERS\]

> \|

> \|-----------------MPM Manager's ------------PPE Patient Profile

> \| Patient Including Errors

> \| Management \[WV \[WV PATIENT

> \| MENU-MGR PATIENT PROFILE

> \| MGT\] W/ERRORS\]

> \| \|

> \| \|------------------PC Edit/Print

> \| \| Patient Case

> \| \| Data \[WV EDIT

> \| \| PATIENT CASE

> \| \| DATA\]

> \| \|

> \| \|-----------------HIS Add an

> \| \| HISTORICAL

> \| \| Procedure \[WV

> \| \| ADD AN

> \| \| HISTORICAL

> \| \| PROCEDURE\]

> \| \|

> \| \|-----------------DUP Browse

> \| \| Procedures for

> \| \| Possible

> \| \| Duplicates \[WV

> \| \| BROWSE

> \| \| PROCEDURES

> \| \| DUPLICATE\]

> \| \|

> \| \|-----------------PAL Edit PAP Regimen

> \| \| Log \[WV EDIT PAP

> \| \| REGIMEN LOG\]

> \| \|

> \| \|-----------------PRL Edit Pregnancy

> \| Log \[WV EDIT

> \| PREGNANCY LOG\]

> \|

> \|

> \|-----------------LDE Lab Data Entry --------AP Add(Accession) a

> Menu \[WV NEW Procedure

> MENU-LAB DATA \[WV LAB ADD A

> ENTRY\] NEW PROCEDURE\]

> \|

> \|------------------EA Edit Accessioned

> \| Procedure \[WV

> \| LAB EDIT

> \| ACCESSION\]

> \|

> \|------------------EP Edit a Procedure

> \| Result \[WV LAB

> \| EDIT PROCEDURE

> \| RESULT\]

> \|

> \|------------------PR Print a

> \| Procedure \[WV

> \| PRINT A

> \| PROCEDURE\]

> \|

> \|-----------------LOG Display/Print

> Daily Log \[WV LAB PRINT LOG\]

# Chapter 5 Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No provisions for archiving or purging have been made for this release and none are planned for the future.

# Chapter 6 Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no callable routines in this release.

# Chapter 7 External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Minimums of FileMan Version 21, Kernel Version 8.0, and PIMS V. 5.3 are required to run this package. Radiology/Nuclear Medicine V. 5.0 is optional.

> The user can view the DBIA’s (Database Integration Agreements) by going to the Integration Agreements Menu option under the DBA menu on FORUM.

# Chapter 8 Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The routines, files and options contained in this package are distributed as a unit. Any attempt to access the files or data, other than through the menu options, is discouraged.

# Chapter 9 Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no package-wide variables in this release.

# Chapter 10 On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Women’s Health is found in the WV namespace. All routines, templates and options begin with WV. File numbers are in the range of 790 through 794 and are stored in the ^WV global.

> The list of all exported files and their data dictionaries can be produced by using the VA FileMan Data Dictionary Utility option, List File Attributes. File relationships can be diagrammed by using the VA FileMan Data Dictionary Utility option, Map Pointer Relationships.

> Menu diagrams may be generated through the Menu Management option, Display Menus and Options. If detailed documentation is required on the application's options, it can be printed through the Menu Management option, Print Option File.

> The XINDEX routine prints a cross-reference listing of all local and global variable usage as well as other information of invaluable assistance in debugging.

> Throughout the application, on-line documentation is also provided at each user prompt. If you are unsure of what is being asked or how to reply during your dialogue with the computer, simply enter one or two question marks (? or ??) for help. The computer will respond with an explanation and then repeat the prompt.

# Chapter 11 SACC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no SACC exemptions in this package. All code is ANSI M Standard.

# Chapter 12 Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No additional security measures are to be applied other than those implemented through Menu Manager and the package routines.

> No additional licenses are necessary to run the software.

> Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

## Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mail groups and alerts.

> There are no mail groups or alerts in this software.

2.  Remote systems.

> The software does not transmit data to any remote systems.

3.  Archiving/Purging.

> Refer to chapter 5, Archiving and Purging, in this manual.

4.  Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.

5.  Interfacing.

> No specialized (non VA) interfaces are used or required by the application.

6.  Electronic signatures.

> Electronic signatures are not used by the application.

7.  Menus.

> There are no options of particular interest to the Information Security Officer (ISO).

8.  Security Keys.

> There are no security keys in this application.

9.  File Security.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NUMBER</p>
</blockquote></th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>GLOBAL NAME</p>
</blockquote></th>
<th><blockquote>
<p>DD ACC</p>
</blockquote></th>
<th><blockquote>
<p>RD ACC</p>
</blockquote></th>
<th><blockquote>
<p>WR ACC</p>
</blockquote></th>
<th><blockquote>
<p>DEL ACC</p>
</blockquote></th>
<th><blockquote>
<p>LAY ACC</p>
</blockquote></th>
<th><blockquote>
<p>AUDIT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>790</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PATIENT</td>
<td><blockquote>
<p>^WV(790,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.01</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>CASE MANAGER</td>
<td><blockquote>
<p>^WV(790.01,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.02</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>SITE PARAMETER</td>
<td><blockquote>
<p>^WV(790.02,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.03</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PAP REGIMEN</td>
<td><blockquote>
<p>^WV(790.03,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.04</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PAP REGIMEN LOG</td>
<td><blockquote>
<p>^WV(790.04,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.05</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PREGNANCY LOG</td>
<td><blockquote>
<p>^WV(790.05,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.07</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>REFERRAL SOURCE</td>
<td><blockquote>
<p>^WV(790.07,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.1</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PROCEDURE</td>
<td><blockquote>
<p>^WV(790.1,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.2</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PROCEDURE TYPE</td>
<td><blockquote>
<p>^WV(790.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.3</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>REFUSALS</td>
<td><blockquote>
<p>^WV(790.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.31</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>RESULTS/DIAGNOSIS</td>
<td><blockquote>
<p>^WV(790.31,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.32</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>DIAGNOSTIC CODE</td>
<td></td>
<td></td>
<td colspan="5"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>TRANSLATION</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.32,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.4,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.403</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATIN TYPE</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.403,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.404</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION PURPOSE</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.404,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.405</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION OUTCOME</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.405,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV CERVICAL TX NEED</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.5,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.51</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV BREAST TX NEED</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.51,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV LETTER</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.6,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.71</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV SNAPSHOT REPORTS</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.71,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.72</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV AGE RANGE DEFAULT</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.72,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
</tbody>
</table>

10. References.

> There are no special circulars or directives for this package.

11. Official Policies.

> There are no special official policies for this package.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
> ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as Women’s Health, PIMS, etc.
> Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of V*IST*A applications are the PIMS and Women’s Health application.
> Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
> ASAP Abbreviation for the phrase ‘as soon as possible’.
> Audit Trail/Logging Features The use of automated software procedures to determine if the security controls implemented for protection of computer systems are being circumvented and to identify the potential source of the security breach.
> Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
> Baud Rate The rate at which data is being transmitted or received from a computer. The baud rate is equivalent to the number of characters per second times 10.
> Block The unit of storage transferred to and from disk drives, typically 512, 1024, or 2048 bytes (characters).
> Boot The process of starting up the computer.
> Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
> Byte A unit of computer space usually equivalent to one character.
> Case Manager The person who is currently managing the women’s health care needs of a specific patient.
> CIOFO Chief Information Office Field Office, formerly known as Information Resource Management Field Office, and Information Systems Center.
> Contingency Plan A plan which assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
> CORE A collection of VA developed programs (specific to PIMS, Pharmacy Service, and Laboratory Service) which is run at VA Medical Centers.
> CPU Central Processing Unit, the heart of a computer system.
> CRT Cathode Ray Tube, similar to a TV monitor but used in computer systems for viewing data. Also called a Video Display Terminal (VDT).
> Cursor A visual position indicator (e.g., blinking rectangle or an underline) on a CRT that moves along with each character as it is entered from the keyboard.
> Data Dictionary A description of file structure and data elements within a file.
> Device A hardware input/output component of a computer system (e.g., CRT, printer). Disk A magnetic storage device used to hold information.
> Edit Used to change/modify data typically stored in a file. Field A data element in a file.
> File The M construct in which data is stored for retrieval at a later time. A computer record of related information (e.g., Patient file).
> File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/ search related data in a file; a data base.
> Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.
> Gynecologic Pertaining to the female reproductive tract.
> Hardware The physical or mechanical components of a computer system such as CPU, CRT, disk drives, etc.
> IRMS Information Resource Management Service.
> Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
> Kilobyte More commonly known as Kbyte or ‘K’. A measure of storage capacity equivalent to 1024 characters.
> LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
> Legacy System An outdated system used for data storage and retrieval.
> M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi- Programming System. This is the programming language used to write all V*IST*A applications.
> MailMan An electronic mail, teleconferencing, and networking system. MAM Abbreviation for Mammogram.
> Megabyte A measure of storage capacity; approximately 1 million characters. Abbreviated as Mbyte or Meg.
> Memory A storage area used by the computer to hold information.
> Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
> Menu Manager A part of the Kernel that allows each site to manage the various options or functions available to individual users.
> Modem An electronic device which converts computer signals to enable transmission through a telephone.
> Module A component of the Women’s Health software application that covers a single topic or a small section of a broad topic.
> Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application. The Women’s Health Package uses WV as its namespace.
> Operating System The innermost layer of software that communicates with the hardware. It controls the overall operation of the computer such as assigning places in memory, processing input and output. One of its primary functions is interpreting M computer programs into language the system can understand.
> Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions. For example, the WVMENU is the main menu for the Women’s Health application.
> Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within V*IST*A (e.g., the ADT and Women’s Health applications).
> PAP Abbreviation for PAP smear.
> Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
> Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
> Port An outlet in the back of the computer into which terminals can be connected. Printer A device for printing (on paper) data which is processed by a computer system.
> Procedure Accession# A number assigned to represent a specific procedure performed on a specific patient on a certain date (e.g., PS1998-43).
> Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
> Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
> Response Time The average amount of time the user must wait between the time the user responded to a question at the terminal and the time the system responds by displaying data and/or the next question.
> Restart/Recovery Procedures The actions necessary to restore a system's data files and computational capability after a system failure or penetration.
> \<RET\> Carriage return or Enter.
> Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
> Security Key A function which unlocks specific options and makes them accessible to an authorized user.
> Security System A part of Kernel that controls user access to the various computer applications.
> When a user signs-on, the security system determines the privileges of the user, assigns security keys, tracks usage, and controls the menus or options the user may access. It operates in conjunction with MenuMan.
> Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
> Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
> Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
> Subroutine A part of a program which performs a single function.
> Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
> Telecommunications Any transmission, emission, or reception of signs, signals, writing, images, sounds or other information by wire, radio, visual, or any electromagnetic system.
> Terminal A device used to send and receive data from a computer system (i.e., keyboard and CRT, or printer with a keyboard).
> UCI User Class Identifier. The major delimiter of information structure within the operating system.
> User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
> Utility An M program that assists in the development and/or maintenance of a computer system.
> VDT Video Display Terminal. Also called a Cathode Ray Tube (CRT).
> Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
> V*IST*A Veterans Health Information Systems and Technology Architecture.
