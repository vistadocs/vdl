---
title: Women's Health Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
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
menu_options: 4
description: "<table> <colgroup> <col style=\\"width: 15%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 31%\\" /> <col style=\\"width: 21%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th><p>Patch/</p> <p>version</p></th> <th>Page</th> <th>Change Description</th> <th>Manager/"
audience: 
keywords: 
  - patient
  - procedure
  - contains
  - date
  - abnorm
  - edit
  - health
  - women
  - number
  - notification
page_count: 0
word_count: 35489
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: May 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=109"
---

WOMEN’S HEALTHUSER MANUAL

![](women-s-health-version-1-user-manual/001.png)

May 2023

Department of Veterans AffairsOffice of Information and Technology

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th><p>Patch/</p>
<p>version</p></th>
<th>Page</th>
<th>Change Description</th>
<th>Manager/Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/2023</td>
<td>WV*1.0*28</td>
<td><p><a href="#basic_patient_mgr_loop_picture">6</a></p>
<p>Various</p></td>
<td><p>Updated the Basic Patient Management Loop image</p>
<p>Update Title page, footers, dates, etc.</p></td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>9/2021</td>
<td>WV*1.0*26</td>
<td><p>23</p>
<p>23-24</p>
<p>23-24<br />
<br />
<br />
26</p>
<p><a href="#EPP_1">26</a>, <a href="#EPP_2">29</a>, <a href="#EPP_3">114</a></p>
<p>58</p>
<p><a href="#Entered_in_Error_1">60</a>, <a href="#Entered_in_Error_2">66</a>, <a href="#Entered_in_Error_3">74</a>, <a href="#Entered_in_Error_4">86</a>, <a href="#Entered_in_Error_5">91</a><br />
<br />
<br />
<br />
<a href="#Follow_Up_Date_1">61</a>, <a href="#Follow_Up_Date_2">66</a><br />
<br />
<br />
<br />
<br />
<br />
82</p></td>
<td><p>Added two new fields: <a href="#two_new_fields">"Default reasons why pregnancy or lactation status was entered in error" and "TIU Ancillary Data Message".</a><br />
<br />
Deleted the <a href="#deleted_the_instructions">"edit CPRS specific parameters" and "edit and delete a CPRS Cover Sheet Women's Health hyperlink"</a> instructions</p>
<p>and screenshots.<br />
<br />
Added a <a href="#deleted_the_instructions">“WV Edit Package Parameters”</a> section<br />
<br />
Deleted the <a href="#deleted_you_have_pending_alerts">“You have pending alerts”</a> message<br />
<br />
Added the EPP option to three screenshots (links are on the page numbers)<br />
<br />
Added the <a href="#BRMRI_BTB_BTS_BTU">BRMRI, BTB, BTS and BTU</a> procedures to the list<br />
<br />
Added the “Entered in Error” code to the Status field on several pages (links are on the page numbers)<br />
<br />
Updated the Follow Up Item popup: Removed “Date” from “Date/Time” and added the “Follow up Date” (links are on the page numbers)<br />
<br />
<br />
Added <a href="#Secure_Messaging_Pact_PC_to_Notify">PACT/PC TO NOTIFY and SECURE MESSAGING</a> to the list of Women's Health notifications</p></td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>9/2020</td>
<td>WV*1.0*24</td>
<td>various</td>
<td><p>Update Title page, footers, dates, etc.</p>
<p>Replaced table of contents</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/2020</td>
<td>WV*1.0*24</td>
<td><p><a href="#manager_func_added_lactation_data">3</a></p>
<p><a href="#Maternity_care_coordinator_definition">4</a></p>
<p><a href="#MCC_edit_menu_option">8</a></p>
<p><a href="#WV_menu_update">10</a></p>
<p><a href="#CPRS_specific_parameters"><strong>Error! Bookmark not defined.</strong></a></p>
<p><a href="#wv-addedit-mat-care-coors">23</a></p>
<p><a href="#wv-transfer-mat-care-coor">28</a></p>
<p><a href="#MCC_field_definition">45</a></p>
<p><a href="#WV_Patient_profile_MCC_definition">49</a></p>
<p><a href="#WV_124_pregnancy_status_remove_codes">49</a></p>
<p><a href="#WV_124_move_Complete_by_date">59</a></p>
<p><a href="#WV_124_add_proc_status_move">59</a></p>
<p><a href="#Follow_Up_Date_1">60</a></p>
<p><a href="#Follow_Up_Date_1">60</a></p></td>
<td><p><a href="#manager_func_added_lactation_data">Added several items where lactation data is also included.</a></p>
<p><a href="#Maternity_care_coordinator_definition">Added information about Maternity Care Coordinators and their job.</a></p>
<p><a href="#MCC_edit_menu_option">Added a reference to a new WV ADD/EDIT CASE MANAGERS menu option</a></p>
<p><a href="#WV_menu_update">Updated the WV MENU</a>.</p>
<p><a href="\l">Added information on CPRS-specific parameters for Women’s Health: Reasons for Status Entered in Error,</a></p>
<p><a href="\l">TIU Ancillary Data Message, and Cover Sheet Web Sites.</a></p>
<p><a href="#wv-addedit-mat-care-coors">Added a section on how to Add or Inactivate a Maternity Care Coordinator (MCC).</a></p>
<p><a href="#wv-transfer-mat-care-coor">Added information on transferring patients from one MCC to another MCC</a></p>
<p><a href="#MCC_field_definition">Added a definition of Maternity Care Coordinator</a></p>
<p><a href="#WV_Patient_profile_MCC_definition">Added a definition of a MCC in the WV Patient Profile</a></p>
<p><a href="#WV_124_pregnancy_status_remove_codes">Removed a sentence about the codes for pregnancy status</a></p>
<p><a href="\l">Moved the definition of Complete by (date)</a></p>
<p><a href="\l">Moved the Add a New Procedure field STATUS to a new location.</a></p>
<p><a href="#Follow_Up_Date_1">Added information about a field called Follow Up Item.</a></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>June 2020</td>
<td>WV*1.0*24</td>
<td><p><a href="#WV_124_Outside_report_add_proc">61</a></p>
<p><a href="#WV_124_edit_proc_status_move">65</a></p>
<p><a href="#Follow_Up_Date_2">65</a></p>
<p><a href="#WV_124_move_Complete_by_date_edit_proc">65</a></p>
<p><a href="#WV_124_Outside_report_edit_proc">66</a></p>
<p><a href="#WV_124_outcome_add_new_notif">84</a></p>
<p><a href="#WV_124_WHO_CONTACTED_add_new_notif">86</a></p>
<p><a href="#WV_124_CONTACTED_DATE_add_new_notif">86</a></p>
<p><a href="#WV_124_WHO_CONTACTED_edit_notif">90</a></p>
<p><a href="#WV_124_CONTACTED_DATE_edit_notif">90</a></p>
<p><a href="#edit-pregnancylactation-status-data">123</a></p>
<p><a href="#editprint-patient-case-data-2">140</a></p></td>
<td><p><a href="#WV_124_Outside_report_add_proc">Added a definition of the Outside Report field under Add a New Procedure</a></p>
<p><a href="#WV_124_edit_proc_status_move">Moved the Status field</a></p>
<p><a href="#Follow_Up_Date_2">Added description of Follow Up Item field</a></p>
<p><a href="#WV_124_move_Complete_by_date_edit_proc">Moved a Complete by (Date) field.</a></p>
<p><a href="#WV_124_Outside_report_edit_proc">Added a description of the Outside Report field under Edit a Procedure</a></p>
<p><a href="#WV_124_outcome_add_new_notif">Moved the Outcome field under the WV ADD A NEW NOTIFICATION</a></p>
<p><a href="#WV_124_WHO_CONTACTED_add_new_notif">Added a definition of the WHO CONTACTED field under Add a New Notification</a></p>
<p><a href="#WV_124_CONTACTED_DATE_add_new_notif">Added a definition of the DATE CONTACTED field under Add a New Notification</a></p>
<p><a href="#WV_124_WHO_CONTACTED_edit_notif">Added a definition of the WHO CONTACTED field under Edit a Notification</a></p>
<p><a href="#WV_124_CONTACTED_DATE_edit_notif">Added a description of DATE CONTACTED field under edit a notification</a></p>
<p><a href="#edit-pregnancylactation-status-data">Changed WV EDIT PREGNANCY LOG to WV EDIT PREG/LAC STATUS DATA and made changes to some fields and added a new field description</a></p>
<p><a href="#editprint-patient-case-data-2">Redid the capture for the EDIT/PRINT PATIENT CASE Data</a></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/2007</td>
<td></td>
<td></td>
<td>Patch WV*1.0*22 released. Changed the inactivated CPT codes on page 36, and the sensitive information displayed within captures on pages 151-154.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/2000</td>
<td></td>
<td></td>
<td>Patch WV*1.0*9 released.</td>
<td></td>
</tr>
<tr class="even">
<td>10/1999</td>
<td></td>
<td></td>
<td>Patch WV*1.0*7 released.</td>
<td></td>
</tr>
<tr class="odd">
<td>5/1999</td>
<td></td>
<td></td>
<td>Patch WV*1.0*6 released.</td>
<td></td>
</tr>
<tr class="even">
<td>3/1999</td>
<td></td>
<td></td>
<td>Patch WV*1.0*5 released.</td>
<td></td>
</tr>
<tr class="odd">
<td>12/1998</td>
<td></td>
<td></td>
<td>Patch WV*1.0*3 released.</td>
<td></td>
</tr>
<tr class="even">
<td>12/1998</td>
<td></td>
<td></td>
<td>Originally released.</td>
<td></td>
</tr>
</tbody>
</table>

### Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Women’s Health User Manual has been developed for women veterans coordinators, health care managers, clinical staff, IRMS (Information Resource Management Service), and CIOFO (Chief Information Office Field Office) support personnel for the purpose of describing the implementation and use of the application. The content covers: software implementation, site configurable file maintenance, and functional use of each option.

This Women’s Health User Manual is one of three manuals associated with the application. Technical information and package security issues are found in the Women’s Health Technical Manual and Package Security Guide. Information critical to the successful installation of the software can be found in the Women’s Health Installation Guide.

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Revision History](#revision-history)
    - [Preface](#preface)
- [# Introduction](#introduction)
    - [Chapter 1 Implementation and Maintenance](#chapter-1-implementation-and-maintenance)
    - [Chapter 2 File Maintenance Menu](#chapter-2-file-maintenance-menu)
    - [WV ADD/EDIT NOT PURPOSE&LETTER](#wv-addedit-not-purposeletter)
    - [### Add/Edit a Notification Purpose & Letter](#addedit-a-notification-purpose-letter)
    - [WV PRINT NOTIF PURPOSE&LETTER](#wv-print-notif-purposeletter)
    - [#### Print Notification Purpose & Letter File](#print-notification-purpose-letter-file)
    - [WV EDIT NOTIF TYPE SYNONYM](#wv-edit-notif-type-synonym)
    - [Edit Synonyms for Notification Types](#edit-synonyms-for-notification-types)
    - [WV ADD/EDIT NOTIF OUTCOME](#wv-addedit-notif-outcome)
    - [#### Add/Edit Notification Outcomes](#addedit-notification-outcomes)
    - [WV EDIT SITE PARAMETERS](#wv-edit-site-parameters)
    - [Edit Site Parameters](#edit-site-parameters)
    - [WV ADD/EDIT CASE MANAGERSAdd/Edit Case Managers](#wv-addedit-case-managersaddedit-case-managers)
    - [WV ADD/EDIT MAT CARE COORS](#wv-addedit-mat-care-coors)
    - [WV TRANSFER CASE MANAGER](#wv-transfer-case-manager)
    - [WVTRANSFER MAT CARE COOR](#wvtransfer-mat-care-coor)
    - [WV AUTOLOAD PATIENTSAutomatically Load Patients](#wv-autoload-patientsautomatically-load-patients)
    - [Chapter 3 Package Operation](#chapter-3-package-operation)
    - [Chapter 4 Patient Management Menu](#chapter-4-patient-management-menu)
    - [Chapter 5 Management Reports Menu](#chapter-5-management-reports-menu)
    - [Chapter 6 Manager's Functions Menu](#chapter-6-managers-functions-menu)
    - [Chapter 7 Manager’s Patient Management Menu](#chapter-7-managers-patient-management-menu)
    - [Chapter 8 Lab Data Entry Menu](#chapter-8-lab-data-entry-menu)
    - [Appendix A - Results/Diagnosis File by Procedure](#appendix-a-resultsdiagnosis-file-by-procedure)
    - [Appendix B - Examples of Major Screen Edits](#appendix-b-examples-of-major-screen-edits)
    - [[^88]Appendix C - Other Useful Information](#88appendix-c-other-useful-information)
    - [Glossary](#glossary)
    - [Index](#index)
The Women’s Health (WH) software provides tracking functionality for procedures of particular interest to women patients (e.g., screening mammogram). The software provides a full range of breast and gynecologic cancer screening and tracking functions. The intended users of the software are primarily WH coordinators and case managers. Providers may use selected patient management and report options.
This software is based on the Indian Health Service (IHS) Resource and Patient Management System (RPMS) Women’s Health software V. 2.0, and modified from suggestions provided by the V*IST*A Women’s Health Technical Advisory Group (TAG).
Credit for the development of the V*IST*A WH software goes to the Indian Health Service and in particular, to <span class="mark">REDACTED</span> who is the original developer of the IHS software.
<span id="_Toc117589083" class="anchor"></span>

### Chapter 1 Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description
This chapter provides guidelines for implementing the Women’s Health application. It is important to complete all the steps contained in this chapter before assigning menu options to clinical staff.
Women’s Health is found in the WV namespace. All routines, templates and options begin with WV. File numbers are in the range of 790 through 794 and are stored in the ^WV global.

######## Main Features

The Women’s Health software is composed of three main modules: Patient Management, Management Reports, and Manager’s Functions.
Patient Management is the portion of the software used to manage individual patient care, that is, their procedures, due dates, and correspondence. Under the Patient Management menu, it is possible to maintain patient data such as the date of the next PAP smear, colposcopy, or mammogram, as well as the patient's current PAP regimen. It is also possible to track the patient's individual procedures: the date performed, the provider and clinic, the results or diagnosis, etc. Notifications (letters and phone calls) may also be tracked. A file of form letters has been included in the software, and these letters may be edited and personalized for a clinic's particular needs. Reminder letters can be queued months in advance of a future appointment, then printed and mailed out shortly before the tentative appointment.
Management Reports is the portion of the software used to print epidemiological reports such as the number of women who received a mammogram for the selected time period, or the number of patients having abnormal PAP results during a selected time period. Under the Management Reports menu, it is possible to produce lists of patients who are past their due dates for follow-up procedures. It is also possible to store program statistics by date for later comparison of program trends and progress.
Manager’s Functions is that portion of the software that provides the ADPAC with a set of utilities for configuring the software to the specific needs of the site. It also provides utilities for other program needs, such as customizing tables, making special edits to patient data (e.g., pregnancy <span id="manager_func_added_lactation_data" class="anchor"></span>and lactation data, PAP regimen log), printing notification letters, running error reports, and documenting laboratory results. By using the File Maintenance options under the Manager’s Functions menu, it is possible to maintain site specific parameters such as the text of form letters, the types of notifications and their synonyms, how and when letters get printed, and several defaults relating to dates.

#### Patients, Procedures, and Notifications

There are primarily three distinct data sets within the WH application and they can be categorized as patient, procedure, and notification related.
Patients refer to the women in the program register. Data stored for each patient includes demographic data, the patient's case manager, the current or next cervical and breast treatment need and its due date, the patient's PAP regimen along with the date it began, and other data. This type of data is referred to as the patient's case data.
Procedures refer to any of the diagnostic and therapeutic tests, exams, or other interventions tracked by the software. The table of procedure types includes PAP smear, colposcopy, mammogram, LEEP, cone biopsy, ECC, and others. The results or diagnosis associated with the gynecologic procedures are chosen from a table of Bethesda-consistent terminology. Mammogram results use the American College of Radiology (ACR) terminology.
Notifications refer to any type of communication or correspondence with the patient, such as first, second and third letters, certified letters, phone calls, messages left, etc. Notifications, which take the form of letters, fall into two categories: results letters and reminder letters. Result letters inform the patient of the findings of a recent procedure and are queued to print immediately. Reminder letters inform the patient of the need to schedule her next appointment and are queued to print at some time several weeks or months in the future.
Selected reports that look at the due dates of patients' treatment needs (using both the procedure and notification data sets) provide a comprehensive mechanism for guarding against losing patients to follow-up.

#### #### #### Case Managers, Maternity Care Coordinators, and the Program Manager

Every patient that is entered into the Women’s Health database (or ‘register’) is assigned a case manager. A case manager is a user of Women’s Health (a registered nurse, LPN, nurse practitioner, or a women veterans health coordinator) who is responsible for managing and tracking a woman's health care needs. This includes treatment planning, tracking of procedures, editing patient data, selecting appropriate letters, scanning for delinquent follow-up care, and more. A small clinic using Women’s Health may have only one case manager. Larger clinics and hospitals may have several. In some cases, the tasks associated with the software may be assigned to clerical personnel under the supervision of a licensed care provider.
The <span id="Maternity_care_coordinator_definition" class="anchor"></span>Maternity Care Coordinator (MCC) functions as a liaison between the patient, the non-VA provider, and the VA facility. This person is responsible for monitoring the delivery of care, coordinating such care, and tracking outcomes of services that have been furnished through maternity purchased care.
The program manageror ADPAC is the person chiefly responsible for the setup and operation of the Women’s Health package at a given site. This person works with the IRM Service on the technical aspects of the software and performs maintenance tasks that require a more detailed understanding of the software than is required of case managers. At small sites, the program manager may also be the only case manager.

####### The Basic Patient Management Loop

The function of the Women’s Health software is best understood in terms of the Basic Patient Management Loop (please refer to the flowchart in this section).
The loop is a sequence of events that occur over and over again during a patient's health care cycle.
This software uses the concept of procedures and notifications being open and closed. Procedures and notifications will become delinquent if they are not closed by the ‘Complete by (Date)’ field found in the notification and procedure screens. If a procedure or notification is not closed by its due date, this will be an indicator that the patient may be ‘lost’ to follow-up. Generally, a procedure is closed when the results or diagnosis for that procedure are entered. A notification is closed either at the time it is printed (as in the case of a results letter) or when the patient returns for her next appointment (as in the case of a reminder letter).
An example of the Basic Patient Management Loop would be the following: A new patient arrives at the clinic for care. The patient's case data (PAP and MAM treatment needs, etc.) are entered into the Women’s Health program. A procedure is performed (such as a PAP smear). The procedure is entered into the computer, an accession number is assigned to the procedure, and the specimen is sent to a lab for diagnosis. After a period of days, results are returned from a lab and entered for the procedure and this procedure is then closed. At that time, one and possibly two separate notification letters are selected from the Purpose of Notification file. The first letter, a results letter, informs the patient of the results of the procedure. This letter is printed immediately. The second letter, a reminder letter, will advise the patient to call the clinic in order to schedule her next appointment. This second letter is queued to print one year later (assuming the PAP was normal). Twelve months later, in response to the reminder letter, the patient calls to schedule her next appointment. When she returns to the clinic for her next procedure, the Patient Management Loop begins again: procedure... results...results letter & reminder letter...call for an appointment...procedure.
When the patient returns for a procedure, it is important to close the reminder letter that prompted her appointment; otherwise, the reminder letter will be left open and begin to show up as delinquent on the past due reports.
<span id="basic_patient_mgr_loop_picture" class="anchor"></span>![](women-s-health-version-1-user-manual/002.png)  
As noted earlier, the reports that look for the due dates of patients' treatment needs (for procedures, and notifications) provide a comprehensive mechanism for guarding against losing patients to follow-up. The three sets of ‘due dates’ are as follows:
1) Treatment Need Due Date
Stored as part of each patient’s case data are breast treatment needs and gynecologic treatment needs. These needs are chosen from a table and given a due date, such as, ‘Routine PAP (by 7/1/95)’. The Women’s Health software offers a report that will display/print all of the patients with treatment needs past due.
2) Procedure Complete by Date
A ‘Complete by Date’ is stored as part of each procedure a patient receives. When a procedure is first entered, it receives a status of ‘Open’. When the results of the procedure are returned and entered, the status is generally changed to ‘Closed’. If a procedure’s status remains ‘Open’ after its ‘Complete by Date’, the procedure will begin to display on reports that look for procedures that are past due.
3) Notification Complete by Date
A ‘Complete by Date’ is stored as part of each notification a patient receives. When a notification is first entered, it receives a status of ‘Open’. If the notification is a result letter (to be printed immediately) or a phone call, it is generally given an outcome and a status of ‘Closed’. If the notification is a reminder letter, its status is left ‘Open’ until the patient’s next procedure is entered. If a notification’s status remains ‘Open’ after its ‘Complete by Date’, the notification will begin to display on reports that look for notifications that are past due.

######## Summary

In summary, Women’s Health is largely a patient management tool for tracking the breast and gynecologic treatment needs of women, the procedures they receive, and the communications between healthcare staff and women regarding their treatment and follow-up. The software also provides some program-wide epidemiological reports which are of use to clinicians and program administrators.
Installation of Software:
This is the first version of the V*IST*A Women’s Health package. Some VA facilities are running the Indian Health Service Women’s Health software (namespace is BW, file range is 9002086-9002086.93). This installation will copy the IHS data into the V*IST*A Women’s Health files. It will not change the IHS database and will remain as a legacy database until otherwise determined by the ADPAC and the women veterans coordinator.
1\. Setting up the software environment.
Information Resource Management Services staff should install the software using the Installation Guide in a test environment prior to installing the software in the production (VAH) account. The following V*IST*A packages should reside in the environment where the Women’s Health application is to be installed:
> a\. VA FileMan V. 21 or greater,
> b\. Kernel V. 8.0 or greater,
> c\. Kernel Toolkit V. 7.3 or greater,
> d\. PIMS V. 5.3 or greater,
> e\. Radiology/Nuclear Medicine V. 5.0 or greater (optional),
> f\. MailMan V. 7.1 or greater.
> If Radiology/Nuclear Medicine V. 5.0 and patch RA\*5.0\*2 are installed patient mammograms can be automatically entered into the Women’s Health database.
Data entered into the test environment CANNOT be transferred into the production environment. It is recommended that a limited amount of data be entered into the test directory in order for the user to become familiar with the application and to establish an acceptable training data base.
2.  Editing site configurable files.
> a\. The WV EDIT SITE PARAMETERS option edits the WV SITE PARAMETER (#790.02) file.
b\. The WV ADD/EDIT REFERRAL SOURCE option edits the WV REFERRAL SOURCE (#790.07) file.
> c\. The WV EDIT DIAG TRANSLATION option edits the WV DIAGNOSTIC CODE TRANSLATION (#790.32) file.
> d\. The WV ADD/EDIT NOT PURPOSE&LETTER option edits the WV NOTIFICATION PURPOSE (#790.404) file.
> e\. The WV ADD/EDIT NOTIF OUTCOME option edits the WV NOTIFICATION OUTCOME (#790.405) file.
> f\. The WV ADD/EDIT CASE MANAGERS option edits the WV CASE MANAGER (#790.01) file.
> g\. The <span id="MCC_edit_menu_option" class="anchor"></span>WV ADD/EDIT MAT CARE COORS option edits the WV MATERNITY CARE COORDINATOR (#790.011) file.
Review the above populated site configurable files. The options, which allow the application coordinator to edit the file's data, are all located in the File Maintenance Menu.
3\. Automatically loading files.
At this time, the WV Patient (#790) file can be preloaded with the names of women patients from the Patient (#2) file. This may be done using the Automatically Load Patients option. The mammogram reports from the Radiology/Nuclear Medicine package may also be automatically loaded into the Women’s Health package by using the option Import Radiology/NM Exams. For further information on these options, refer to Chapter 2.
4\. Queueing TaskMan jobs.
There are no options that need to be queued to run.
5\. Accessing menus.
There are no security keys in this application.
6\. Assigning menus.
The Women’s Health Menu \[WVMENU\] should be assigned to the ADPAC and the individual having primary responsibility for managing and editing data in this tracking package.
The Patient Management \[WV MENU-PATIENT MANAGEMENT\] and Management Reports \[WV MENU-MANAGEMENT REPORTS\] should be assigned to all women’s health coordinators and case managers who have not been assigned the Women’s Health Menu option. These two options may also be assigned to appropriate clinicians and women’s health clinical directors as required.
The Lab Data Entry Menu \[WV MENU-LAB DATA ENTRY\] should be assigned to laboratory personnel who may be assigned to enter cytology reports into the WH database.
7\. Printer issues.
There are no special printer issues.
8\. Resource Requirements.
The size of the table files that come with the package are insignificant. Data storage for the package is very roughly 2 megabytes per 1000 patients per year.

### Chapter 2 File Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-FILE MAINTENANCEFile Maintenance Menu
Several features of Women’s Health can be customized by the ADPAC. These features include such items as the text of form letters, the types of notifications and their synonyms, how and when letters get printed, several defaults relating to dates, and options that appear on some menus.
All of these setup options are located under the File Maintenance Menu of the Manager’s Functions menu. It is recommended that the ADPAC examine all of the options listed in this section before utilizing the software for live patient data. Periodically, these options should be re-examined for the purpose of fine tuning the software to the needs of the site.
After customizing your maintenance files, you may wish to run the option Automatically Load Patients \[WV AUTOLOAD PATIENTS\] to initially populate your WV Patient (#790) file. For more details concerning this option please refer to the option description under the Automatically Load Patients option in this chapter.
Also, you may wish to run the option Import Radiology/NM Exams \[WV IMPORT RAD/NM EXAMS\] to initially populate your WV Procedure (#790.1) file with mammograms performed recently at your facility. You may automatically add mammograms performed within the last three years. For more details concerning this option please refer to the option description under the Import Radiology/NM Exams option in this chapter.
In the menu on the next page, the top group of options relates to notifications, the middle group addresses package-wide parameters, and the bottom group relates to procedures and their results.
Menu Display:
Select OPTION NAME: WV MENU-FILE MAINTENANCE File Maintenance Menu
> WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* HINES DEVELOPMENT
> ===========================
> <span id="WV_menu_update" class="anchor"></span>AEP Add/Edit a Notification Purpose & Letter
> PPL Print Notification Purpose & Letter File
> ESN Edit Synonyms for Notification Types
> OUT Add/Edit Notification Outcomes
> ESP Edit Site Parameters
> CM Add/Edit Case Managers
> MCC Add/Edit Maternity Care Coordinators
> TRCM Transfer a Case Manager's Patients
> TRMC Transfer a Maternity Care Coordinator's Patients
> AUTO Automatically Load Patients
> RAD Import Radiology/NM Exams
> PRD Print Results/Diagnosis File
> ESR Edit Synonyms for Results/Diagnoses
> PSR Print Synonyms for Results/Diagnoses
> EDX Edit Diagnostic Code Translation File
> PDX Print Diagnostic Code Translation File
> RS Add/Edit to Referral Source File
> PAP Link Pap Smear with SNOMED Codes
> **NOTE:** The option Add Sexual Trauma Data to MST Module was added to this menu by patch WV\*1\*11 in June 2000, and then this option was removed by patch WV\*1\*14 in April 2001.

### WV ADD/EDIT NOT PURPOSE&LETTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Add/Edit a Notification Purpose & Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While notifications may be phone calls or conversations, most notifications will be letters and most of the customizable parameters relate to notifications in the form of letters.
This option allows the ADPAC to add or edit purposes of notification, for example, ‘PAP Result Normal’ or ‘PAP, Annual Due’. Each purpose of notification can have its own form letter, for example, the form letter for ‘PAP Result Normal’ would include a body of text informing the patient that the results of her recent PAP test were normal. When printed, the form letter automatically includes the patient’s name and address information. The position of the name and address can be adjusted in order to have that information appear in the window of a windowed envelope.
[^1]The patient’s name, address, and SSN will appear automatically within the letter at the places demarcated by the vertical bars “\|\|” (e.g., \|SSN\|) when the letter is printed. This information is obtained from the WV PATIENT file (#790). If you do not wish to have a certain piece of information displayed in the letter, you should edit the text of the letter and remove that field name (e.g., SSN) and the vertical bars that surround it.
Other information that appears in the letter is the clinic name and address. This information is typed within quotes. You should edit the text between the quotes to display the correct clinic name and address (Note: Leave the quotes). If you plan on printing your letters on paper that contains a letterhead you will want to remove altogether the lines containing the clinic name and address.
The field \|NOWRAP\| should be left as is. This permits the text of the letter to be printed as it appears on the terminal screen. Other fields may be deleted if not desired. For example, \|TODAY\| and \|NOW\| will print out the current date and date/time respectively. Future appointments may be included to print in a notification letter by typing the text “\|APPOINTMENTS\|” (without the quotes) in the text of the letter.
Because of the specific syntax of the fields and the possibility of corrupting them during edits, a recovery utility has been provided. The program to edit a purpose of notification always asks first if you wish to replace the existing form letter with a ‘generic sample letter’. Answering ‘Yes’ to that question will replace the existing form with a generic sample letter, which includes all of the original fields in their proper syntax.
Once the purpose has been selected and the generic letter question answered,
the ‘Edit Notification Purpose & Letter’ screen appears. Notification purpose data is stored in the WV Notification Purpose (#790.404) file.
Field Descriptions:Purpose of Notification:
This field contains the reason for the notification (e.g., the results of a test, reminder to schedule a procedure). This should be brief but descriptive enough to identify it uniquely. NOTE: This field cannot be changed because previous notifications from this purpose would become inaccurate. If the Purpose field is incorrect, make this purpose ‘Inactive’ (see next field), and then create a new purpose of notification with the correct purpose name.
Active:
This field describes whether or not the purpose of notification may be selected. ‘Yes’ means the purpose may be selected, ‘No’ means the purpose may not be selected. This is to eliminate the clutter of unused notifications.
Synonym:
This field stores an abbreviation or short synonym for the notification type. For example, ‘LF’ for ‘Letter, First’.
Priority:
This field associates a priority with the notification. The priority choices are: urgent, ASAP, and routine. These priorities are used within the Browse Notifications options to print a list of notifications by priority.
Form Letter:
This field stores the text of the form letter for this purpose of notification. NOTE: To navigate to this field you must place the cursor at the Priority field and then press the TAB key, then RETURN.
Result or Reminder:
This field contains a code (1 = Result, 2 = Reminder), used to determine a print date for the letter. A notification identified as a result is queued to print immediately and a reminder is queued to print on a future date.
Associate with BR/CX:
This field has a 2-fold purpose. It identifies that the notification letter is associated with cervical or breast treatment needs, and also determines a default print date based on the treatment need type. The value of this field is a set of codes (BR for breast Tx need, CX for cervical Tx need). If a clinician does not want to automatically queue a letter to print, the field may be left blank.
[^2]Breast Treatment Need
Use this field to assign a breast treatment need from the WV BREAST TX NEED file (#790.51) to this particular purpose of notification. When a Clinical Reminder uses this purpose of notification to result a patient’s breast procedure, the breast treatment need linked to this purpose of notification will be automatically assigned to the patient in the WV PATIENT file (#790).
Breast Treatment Due Date
This field is the amount of time to add to the current date or the procedure date to calculate a new breast treatment due date. The value should be a number followed by “D”, “M” or “Y” (without the quotes). D indicates days. M indicates months. Y indicates years. When a Clinical Reminder uses this purpose of notification to result a patient’s breast procedure, the new treatment due date will be automatically assigned to the patient in the WV PATIENT file (#790).
Cervical Treatment Need
Use this field to assign a cervical treatment need from the WV CERVICAL TX NEED file (#790.5) to this particular purpose of notification. When a Clinical Reminder uses this purpose of notification to result a patient’s cervical procedure, the cervical treatment need linked to this purpose of notification will be automatically assigned to the patient in the WV PATIENT file (#790).
Cervical Treatment Due Date
This field is the amount of time to add to the current date or the procedure date to calculate a new cervical treatment due date. The value should be a number followed by “D”, “M” or “Y” (without the quotes). D indicates days. M indicates months. Y indicates years. When a Clinical Reminder uses this purpose of notification to result a patient’s cervical procedure, the new treatment due date will be automatically assigned to the patient in the WV PATIENT file (#790).

### WV PRINT NOTIF PURPOSE&LETTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### #### Print Notification Purpose & Letter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints out all of the purposes of notifications and their field values (active, synonym, priority, etc.) along with the form letter. When trying to sort out and edit all the purposes of notifications as a coherent group, you may find it easier to print them out on paper (using this option) and work from a printed hard copy. The following is a sample form letter. Notification purpose data is stored in the WV Notification Purpose (#790.404) file.
NOTIFICATION PURPOSE & LETTER LIST AUG 13,1998 11:09 PAGE 1
------------------------------------------------------------------------------
PURPOSE: COLP Abnormal, need further TX SYNONYM:
PRIORITY: URGENT ACTIVE: YES
BR or CX: CERVICAL TX
LETTER: RESULT
[^3]BR TX NEED: BR TX DUE DATE:
CX TX NEED: Follow-up PAP CX TX DUE DATE: 3 Months
Women's Health Clinic
7 Your Street
Your City, ST 77777
AUG 13,1998
SSN: \|SSN#\|
\|\$P(NAME,",",2)\| \|\$P(NAME,",")\|
[^4]\|COMPLETE ADDRESS\|
\- - - -
Dear Ms. \|\$P(NAME,",",1)\|,
The results of your recent Pap smear are something, something.
This is the body of the letter and should be edited to say what
you want for this Purpose of Notification.
It may go on to say: Your next something will be due one year from
now. At that time we will mail you a reminder letter, or you may
schedule the appointment yourself by calling our Family Medicine
Clinic at 777-7777 or our Women's Clinic at 777-7777.
Sincerely,
WHNURSE, ONE
Women's Health Program
phone: 555-7777
printed: AUG 13,1998@11:09:27

### WV EDIT NOTIF TYPE SYNONYM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Synonyms for Notification Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notification types are letters, phone calls, messages, conversations, etc. It is possible to assign synonyms to each type using this option. For example, ‘Letter First’ might be given a synonym of ‘LF’, ‘Letter Second’, ‘LS’, and so on. This simply provides a user-defined quick method of selecting the desired type. Notification type data is stored in the WV Notification Type (#790.403) file.
Field Descriptions:Notification Type:
This field contains types of notifications which indicate how patients were informed about test and procedure results, and treatment needs. For example, Contact PHN (primary health nurse), conversation with patient, consult, or 2<sup>nd</sup> phone call.
Synonym:
This field stores an abbreviation or short synonym for the notification type. For example, ‘LF’ for ‘Letter, First’.

### WV ADD/EDIT NOTIF OUTCOME

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### #### Add/Edit Notification Outcomes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each notification, whether it is a letter, phone call, or other notification topic, may be given an ‘Outcome’. Outcomes such as ‘Declined Tx’ and ‘Scheduled appt for PAP’ come pre-loaded with the software. Using this option, it is possible to add other, user-defined outcomes such as ‘Referred to County Hospital’.
It is also possible to make an outcome ‘Inactive’ if you do not use it and do not wish to have it display in the list of available outcome choices. Notification outcome data is stored in the WV Notification Outcome (#790.405) file.
Field Descriptions:Outcome:
This field contains the terms describing a notification outcome. An outcome may be a goal or an event (e.g., PAP normal letter sent, provider consult, CBE refused, scheduled appt for MAM).
Active:
This field contains a set of codes (1 = Yes, 0 = No) used to display or hide an entry in a selection list. If the field is active and contains a ‘1’ or yes, users of this package can select the entry.

### WV EDIT SITE PARAMETERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Site Parameters option allows the ADPAC to edit several parameters specific to the clinic or hospital where the software is being used. There are 5 pages (or screens) of parameters. After selecting a site (or facility), the screen for page 1 appears. Site parameter data is stored in the WV Site Parameter (#790.02) file.
> **NOTE:** To access CPRS parameter, the user would select ESP or Edit Site Parameters. Then when the dialog appears to edit those parameters, select the up arrow and type E and press \<Enter\>. The information on these parameters is further down in this section.
Field Descriptions:Site/Facility Name:
This is the name of the facility, division, and/or community-based outpatient clinic requiring separate site parameters. If all divisions are using the same site parameters, then enter the name of the primary or lead facility.
Default Case Manager:
This is the name of the case manager or the individual that will be used to initially seed the patient's record. Although the patient's care management can be transferred to another individual, this name is used as the default to deter loss of this patient's treatment needs within the facility and database. Pointer to the WV Case Manager (790.01) file.
Ask Case Manager:
This field is used to display or hide a question asking users if they want to select a particular case manager within the report option, Browse Patients With Needs Past Due. If there is only one case manager at the facility(s), the answer should be no.
Autoqueue Normal PAP Letters:
This field stores a code (0 = No, 1 = Yes) that displays or hides the prompt: "QUEUE a PAP Result Normal letter to be sent to this patient?". This question displays after the user exits either Add a NEW Procedure or Edit a Procedure option and after the results of a PAP smear procedure have been entered into the patient's record. The results/diagnosis must be considered normal.
PAP Result Normal Letter:
This field stores the name of the PAP letter that is printed when the user answers, Yes, to the prompt: "QUEUE a PAP Result Normal letter to be sent to this patient?" after the procedures results have been entered into a patient's record.
Autoqueue Normal MAM Letters:
This field stores a code (0 = No, 1 = Yes) that displays or hides the prompt: "QUEUE a MAM Result Normal letter to be sent to this patient?". This question displays after the user exits either Add a NEW Procedure or Edit a Procedure option and after the results of a mammogram procedure have been entered into the patient's record. The results/diagnosis must be considered normal.
MAM Result Normal Letter:
This field stores the name of the MAM letter that is printed when the user answers, YES, to the prompt: "QUEUE a MAM Result Normal letter to be sent to this patient?" after the procedures results have been entered into a patient's record.
Default \#days to print Letters:
[^5]Allows the ADPAC to set the default number of days, prior to a patient’s cervical and breast treatment needs due date, reminder letters (notifications) should be printed. For example:
Notification Print Date: 11/1/2000
Default \# Days: 30
30 days before 11/1/2000, the letter will be printed.
[^6]Update Result/Dx Field:
This field indicates if the RESULTS/DIAGNOSIS field of the WV PROCEDURE file (790.1) should be updated from a Clinical Reminder. Answer YES if you want Clinical Reminders to be able to update the RESULTS/DIAGNOSIS field in a WV PROCEDURE file (790.1) entry. Answer NO if Clinical Reminders should not update the RESULTS/DIAGNOSIS field.
Update Treatment Needs:
This field indicates if the patient’s breast and cervical treatment needs and treatment due dates should be updated in the WV PATIENT file (#790) from a Clinical Reminder. Answer YES if the patient’s treatment need and due date values can be updated from a Clinical Reminder. Answer NO if the treatment need and due date values should not be updated from a Clinical Reminder.
Import Mammograms from Radiology:
This field is used to automatically import and store mammography reports, from the Radiology/Nuclear Medicine package, in the Women's Health database.
> **NOTE:** The Radiology/Nuclear Medicine patch RA\*5.0\*2 must be installed to use this functionality.
Status Given to Imported Mammograms:
This field automatically stores a default status (O = Open; C = Closed) in the procedure edit screens when mammography reports are imported from the Radiology/Nuclear Medicine application.
[^7]Include ALL Non-Veterans:
This field indicates whether or not procedure data transmitted from the Radiology/NM package for non-veterans will be accepted in the Women's Health package.
Answer YES to accept radiology procedure data for ALL non-veterans.
Answer NO to not accept radiology procedure data for any non-veterans.
To accept data for some (but not all) non-veterans, answer NO and then enter the eligibility code(s) you wish to track.
Leaving this answer blank is the same as YES.
Eligibility Codes:
Facilities that do not want to track radiology procedure data for ALL non-veterans may select the eligibility codes of those non-veteran patients they do wish to track.
[^8]Import Test from Laboratory:
This field indicates whether or not to automatically import lab test data from the Laboratory package, into the Women's Health database.
> **NOTE:** The Lab patch LR\*5.2\*231 must be installed to use this functionality.
[^9]Include ALL Non-Veterans:
This field indicates whether or not lab test data transmitted from the Laboratory package for non-veterans will be accepted in the Women's Health package.
Answer YES to accept lab test data for ALL non-veterans.
Answer NO to not accept lab test data for any non-veterans.
To accept data for some (but not all) non-veterans, answer NO and then enter the eligibility code(s) you wish to track.
Leaving this answer blank is the same as YES.
Eligibility Codes:
Facilities that do not want to track radiology procedure data for ALL non-veterans may select the eligibility codes of those non-veteran patients they do wish to track.
After answering the page 2 site parameters, the cursor will drop to the Command Line. Selecting a ‘N’ (for Next page) at the command prompt will display page 3. Pages 3, 4 and 5 all concern setting the parameters for each of the 27 procedure types.
Procedure Type:
This is not an editable field. It simply lists all of the procedure types that are available for tracking in the Women’s Health package.
Active:
If users should NOT be allowed to select a specific procedure type when entering new procedures at this site, then enter ‘No’ to make it ‘Inactive’ or unselectable. Enter ‘Yes’ to make the procedure type ‘Active’.
Days Delinquent:
Enter the default number of days that a specific procedure will be allowed to remain ‘Open’ before being marked as ‘Delinquent’.
Pages 4-6 of the ‘Edit Site Parameters’ screen are similar to page 3 and permit the configuration of the remaining procedure types.
Default reasons why pregnancy or lactation status data was entered in error:
This parameter stores a set of predefined reasons that are presented to the user when he/she is marking a pregnancy or lactation status as entered in error. This message displays only when marking an Entered in Error status on the Women’s Health panel on the CPRS Coversheet.
TIU Ancillary Data Message:
This field stores text that is displayed to a Text Integration Utilities (TIU) user when that user deletes, retracts or reassigns a document that has pregnancy or lactation status data associated with it. It reminds the TIU user of local site procedures concerning clean-up of the document’s associated pregnancy and/or lactation status data.
<span id="deleted_the_instructions" class="anchor"></span>
WV EDIT PACKAGE PARAMETERS
Edit Package Parameters
The Edit Package Parameters option allows the ADPAC to edit several parameters specific to the Women’s Health Package, regardless of hospital location.
Coversheet Websites:
This parameter stores website names and hyperlinks that are displayed to the user when he/she right-clicks on the Women’s Health panel on the CPRS Coversheet.
Women's Health Mailgroup:
This parameter stores the mail group any mailman generated by the Women’s Package should be sent to. If no mail group is defined, the mailman message will be sent to the OR CACS mail group.
Breast Image Term Linking:
This parameter stores the list of Reminder Terms used to map a Radiology Procedure to a Women’s Health Procedure entry.
If a site set a value at the System or Division level, it must include the entries defined at the Package level.
Sequence Value
-------- -----
1 VA-WH MAMMOGRAM SCREENING CODES
2 VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
3 VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
4 VA-WH MRI BREASTS CODES
5 VA-WH ULTRASOUND BREAST CODES
6 VA-WH BREAST TOMOSYNTHESIS BILAT
7 VA-WH BREAST TOMOSYNTHESIS SCREENING
8 VA-WH BREAST TOMOSYNTHESIS UNILAT

### WV ADD/EDIT CASE MANAGERSAdd/Edit Case Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit Case Managers option allows case managers to be selected from the New Person (#200) file. If a person you wish to add as a case manager cannot be selected, contact your site manager. Under this option a case manager may also be inactivated by entering a date at the ‘Date Inactivated: ‘ prompt. A case manager who has been inactivated cannot be assigned to patients because the person does not appear in the selection list in the Edit/Print Patient Case Data option. Case manager data is stored in the WV Case Manager (#790.01) file.
Field Descriptions:Case Manager:
This field contains the name of a WH case manager assigned to manage women’s health needs.
Date Inactivated:
[^10]This date field is used to indicate when a person is no longer recognized as a case manager. A future date may be entered here. The case manager remains as an active selection until the date in the field is in the past.

### WV ADD/EDIT MAT CARE COORS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu option enables the appropriate users to add or edit individuals as Maternity Care Coordinators (MCCs). Maternity care coordinators are assigned to pregnant female patients to coordinate their maternity care.
To add a Maternity Care Coordinator (MCC), use these steps:
1.  To add an MCC, select the WV MENU-FILE MAINTENANCE (File Maintenance Menu).
2.  Type MCC and press \<Enter\>.
3.  At the Select MATERNITY CARE COORDINATOR prompt, type the name of the person you want to add and press \<Enter\>.
4.  When asked if you are adding that person as a new Maternity Care Coordinator, type Y and press \<Enter\>.
5.  At the Date Inactivated prompt, you can add a date in the future by typing the appropriate date or do not enter a date and press \<Enter\>.
6.  At this point, you may add another user as an MCC or exit this menu.
    <span class="mark">  
    </span>
> WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* CAMP MASTER
> AEP Add/Edit a Notification Purpose & Letter
> PPL Print Notification Purpose & Letter File
> ESN Edit Synonyms for Notification Types
> OUT Add/Edit Notification Outcomes
> ESP Edit Site Parameters  
> <span id="EPP_1" class="anchor"></span>EPP Edit Package Parameters
> CM Add/Edit Case Managers
> MCC Add/Edit Maternity Care Coordinators
> TRCM Transfer a Case Manager's Patients
> TRMC Transfer a Maternity Care Coordinator's Patients
> AUTO Automatically Load Patients
> RAD Import Radiology/NM Exams
> PRD Print Results/Diagnosis File
> ESR Edit Synonyms for Results/Diagnoses
> PSR Print Synonyms for Results/Diagnoses
> EDX Edit Diagnostic Code Translation File
> PDX Print Diagnostic Code Translation File
> RS Add/Edit to Referral Source File
> PAP Link Pap Smear with SNOMED Codes
> \<CPM\> Select File Maintenance Menu \<TEST ACCOUNT\> Option: MCC Add/Edit Maternit
> y Care Coordinators
> \* \* \* WOMEN'S HEALTH: ADD/EDIT MATERNITY CARE COORDINATORS \* \* \*
> Select MATERNITY CARE COORDINATOR: PROVIDER,SIXTYFOUR NEW YORK
> 10BA1/ADP Scholar Extraordinaire
> ...OK? Yes// N (No)
> PROVIDER
> 1 PROVIDER,CONSULT ONE COP COMPUTER SPECIALIST
> 2 PROVIDER,CONSULT TWO CTP COMPUTER SPECIALIST
> 3 PROVIDER,EIGHT AG 10BA1/ADP Scholar Extraordinaire
> 4 PROVIDER,EIGHTEEN 10BA1/ADP Scholar Extraordinair
> e
> 5 PROVIDER,EIGHTY ZL 10BA1/ADP Scholar Extraordinair
> e
> Press \<Enter\> to see more, '^' to exit this list, OR
> CHOOSE 1-5:
> 6 PROVIDER,EIGHTYEIGHT 10BA1/ADP Scholar Extraordin
> aire
> 7 PROVIDER,EIGHTYFIVE 10BA1/ADP Scholar Extraordina
> ire
> 8 PROVIDER,EIGHTYFOUR 10BA1/ADP Scholar Extraordina
> ire
> 9 PROVIDER,EIGHTYNINE 10BA1/ADP Scholar Extraordina
> ire
> 10 PROVIDER,EIGHTYONE 10BA1/ADP Scholar Extraordinai
> re
> Press \<Enter\> to see more, '^' to exit this list, OR
> CHOOSE 1-10: 9 PROVIDER,EIGHTYNINE 10BA1/ADP Scholar Extrao
> rdinaire
> Are you adding 'PROVIDER,EIGHTYNINE' as
> a new WV MATERNITY CARE COORDINATOR (the 10TH)? No// Y (Yes)
> DATE INACTIVATED: T+365 (JAN 08, 2020)
To edit (inactivate) a Maternity Care Coordinator (MCC), use these steps:
1.  To add an MCC, select the WV MENU-FILE MAINTENANCE (File Maintenance Menu).
7.  Type MCC and press \<Enter\>.
8.  At the Select MATERNITY CARE COORDINATOR prompt, type the name of the person you want to inactivate and press \<Enter\>.
9.  When asked if you are adding that person as a new Maternity Care Coordinator, type Y and press \<Enter\>.
10. At the DATE INACTIVATED prompt, type the appropriate date (you can also use relative dates such as T for Today, or T-30 for 30 days ago) and press \<Enter\>.
> Below is an example of how to inactive a user. Note that the user Nurse, Twenty-Three’s Inactivation date changes.
> \* \* \* WOMEN'S HEALTH: ADD/EDIT MATERNITY CARE COORDINATORS \* \* \*
> Select MATERNITY CARE COORDINATOR: ??
> Choose from:
> PROVIDER,SIXTYFOUR DATE INACTIVATED: OCT 04, 2021
> PROVIDER,EIGHTYTWO
> PROVIDER,EIGHTYNINE DATE INACTIVATED: JAN 08, 2020
> NURSE,FIFTEEN
> NURSE,EIGHTEEN
> NURSE,TWENTY-THREE DATE INACTIVATED: FEB 16, 2023
> CPRSPROVIDER,THREE
> You may enter a new WV MATERNITY CARE COORDINATOR, if you wish
> This field contains the name of the Women's Health maternity care
> coordinator. Maternity care coordinators are assigned to pregnant female
> patients to coordinate their maternity care.
> Select MATERNITY CARE COORDINATOR: NURSE,TWENTY-THREE NT
> NURSE
> ...OK? Yes// (Yes)
> DATE INACTIVATED: FEB 16, 2023
> DATE INACTIVATED: FEB 16,2023// T (JAN 08, 2019)
> \* \* \* WOMEN'S HEALTH: ADD/EDIT MATERNITY CARE COORDINATORS \* \* \*
> Select MATERNITY CARE COORDINATOR: ?
> Answer with WV MATERNITY CARE COORDINATOR NAME
> Do you want the entire WV MATERNITY CARE COORDINATOR List? Y (Yes)
> Choose from:
> PROVIDER,SIXTYFOUR DATE INACTIVATED: OCT 04, 2021
> PROVIDER,EIGHTYTWO
> PROVIDER,EIGHTYNINE DATE INACTIVATED: JAN 08, 2020
> NURSE,FIFTEEN
> NURSE,EIGHTEEN
> NURSE,TWENTY-THREE DATE INACTIVATED: JAN 08, 2019
> CPRSPROVIDER,THREE

### WV TRANSFER CASE MANAGER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Transfer a Case Manager’s Patients

The purpose of this utility is to aid in the transfer of a case manager’s patients to another case manager, (e.g., when there is a turnover in staff). The program will ask you for the name of the old case manager and then prompt the user to enter the name of a new case manager. All patients who were previously assigned to the old case manager will be reassigned to the new case manager.
If the new case manager you are looking for cannot be selected, the person might have to be added to the file of case managers or have their inactive status changed through the Add/Edit Case Managers option. Case manager data is stored in the WV Case Manager (#790.01) file.
Field Descriptions:Old Case Manager:
This field contains the name of a person who is currently managing the women’s health care needs of this patient.
New Case Manager:
This field contains the name of a person who will be managing the women’s health care needs of this patient.

### WVTRANSFER MAT CARE COOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this utility is to aid in the transfer of all of one Maternity Care Coordinator's patients to another Maternity Care Coordinator (MCC), such as when there is a turnover in staff. The program will ask you for an "OLD" Maternity Care Coordinator and then for a "NEW" Maternity Care Coordinator. All patients who were previously assigned to the "OLD" Maternity Care Coordinator will be reassigned to the "NEW" Maternity Care Coordinator.
If the "NEW" Maternity Care Coordinator you are looking for cannot be selected, that person must first be added to the file of Maternity Care Coordinators by using the "Add/Edit Maternity Care Coordinators" option.
To transfer patients from one MCC to another, use these steps:
1.  To add transfer patients from MCC to another, select the WV MENU-FILE MAINTENANCE (File Maintenance Menu).
2.  Type TRMC and press \<Enter\>.
3.  At the Select OLD MATERNITY CARE COORDINATOR prompt, type the name of the MCC from which you want to transfer patients press \<Enter\>. Or you can type ?? to get a list of MCCs.
4.  At the Select NEW MATERNITY CARE COORDINATOR prompt, type the name of the MCC to receive the patients and press \<Enter\>.
    The patients should be transferred.
> Example of transferring patients from one MCC to another MCC.
> WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* CAMP MASTER
> AEP Add/Edit a Notification Purpose & Letter
> PPL Print Notification Purpose & Letter File
> ESN Edit Synonyms for Notification Types
> OUT Add/Edit Notification Outcomes
> ESP Edit Site Parameters  
> <span id="EPP_2" class="anchor"></span>EPP Edit Package Parameters
> CM Add/Edit Case Managers
> MCC Add/Edit Maternity Care Coordinators
> TRCM Transfer a Case Manager's Patients
> TRMC Transfer a Maternity Care Coordinator's Patients
> AUTO Automatically Load Patients
> RAD Import Radiology/NM Exams
> PRD Print Results/Diagnosis File
> ESR Edit Synonyms for Results/Diagnoses
> PSR Print Synonyms for Results/Diagnoses
> EDX Edit Diagnostic Code Translation File
> PDX Print Diagnostic Code Translation File
> RS Add/Edit to Referral Source File
> PAP Link Pap Smear with SNOMED Codes
> \<CPM\> Select File Maintenance Menu \<TEST ACCOUNT\> Option: TRMC Transfer a Mater
> nity Care Coordinator's Patients
> \* \* \* WOMEN'S HEALTH: TRANSFER A MATERNITY CARE COORDINATOR'S PATIENTS \* \* \*
> The purpose of this utility is to aid in the transfer of all of one
> Maternity Care Coordinator's patients to another Maternity Care
> Coordinator, such as when there is a turnover in staff.
> The program will ask you for an "OLD" Maternity Care Coordinator
> and then for a "NEW" Maternity Care Coordinator. All patients who
> were previously assigned to the "OLD" Maternity Care Coordinator
> will be reassigned to the "NEW" Maternity Care Coordinator.
> If the "NEW" Maternity Care Coordinator you are looking for cannot
> be selected, that person must first be added to the file of
> Maternity Care Coordinators by using the "Add/Edit Maternity Care
> Coordinators" option.
> Select OLD MATERNITY CARE COORDINATOR: ??
> Choose from:
> PROVIDER,SIXTYFOUR DATE INACTIVATED: OCT 04, 2021
> PROVIDER,EIGHTYTWO
> PROVIDER,EIGHTYNINE DATE INACTIVATED: JAN 08, 2020
> NURSE,EIGHT DATE INACTIVATED: APR 10, 2015
> NURSE,NINE DATE INACTIVATED: JUL 25, 2016
> NURSE,FIFTEEN
> NURSE,EIGHTEEN
> NURSE,TWENTY-THREE DATE INACTIVATED: JAN 08, 2019
> CPRSPROVIDER,THREE
> Select OLD MATERNITY CARE COORDINATOR: PROVIDER,EIGHTYNINE
> 10BA1/ADP Scholar Extraordinaire DATE INACTIVATED: JAN 08, 2020
> Select NEW MATERNITY CARE COORDINATOR: NURSE,EIGHTEEN NE
> NURSE
> All patients currently assigned to: PROVIDER,EIGHTYNINE
> will be reassigned to.............: NURSE,EIGHTEEN
> Do you wish to proceed?
> Enter Yes or No? YES
> 8 patients transferred from PROVIDER,EIGHTYNINE to NURSE,EIGHTEEN.

### WV AUTOLOAD PATIENTSAutomatically Load Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^11]This utility examines the main patient database (File \#2) for women veterans seen at a facility within a selected date range, who are over a selected age, and adds them to the Women’s Health database.
[^12]Women already in the Women’s Health database will not be added twice. Women who are deceased will not be added. Women who are veterans or have an eligibility code selected by the user will be added. Women added to the Women’s Health database will be given breast and gynecologic treatment needs of ‘Undetermined’, with no due dates.
This utility may be run at any time, and as often as desired. It may be useful to run it on a monthly basis in order to pick up new women who were added to the main patient database since this option was last run. NOTE: New patients are NOT added to the database without running the option.
[^13]Before the program begins, you will be prompted for an age below which patients should not be added, a start date of patient activity, an end date of patient activity, selected eligibility codes to include other patients, and a device. Patients not having a visit or admission between the start and end dates of patient activity will not be added to the file. These dates can be no more than 3 years prior to today’s date. The name, SSN, date of birth, age, veteran status, and eligibility code for each patient added to the Women’s Health database will be displayed on the device. This device may be a printer, or you may simply display the data on your screen. If the device you select is a printer, it may be preferable to ‘queue’ the job, in order to free up your terminal. See your computer site manager for assistance with queuing jobs.
> **WARNING:** The first time this utility is run, it may add several thousand patients to the Women’s Health database. It may take several minutes or even hours to run, depending on the size of the database and speed of the computer. Subsequent runs should be much quicker. You may type ‘^’ at any time to quit before the program begins.
Report Description:Name:
This field contains the name of the patient.
SSN:
This field contains the social security number of the patient.
Date of Birth:
This field contains the date of birth for the patient.
Status:
This field contains the status of Added or Failed. Added means the patient was successfully added to File 790, failed means the patient was not successfully added to File 790.
[^14]Age:
This field contains the age of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
Eligibility Code:
This field contains the eligibility code of the patient.
WV IMPORT RAD/NM EXAMSImport Radiology/NM Exams
[^15]This option searches the Radiology/Nuclear Medicine database for all WH patients who had a mammogram or breast/pelvic/vaginal ultrasound exam (CPT codes are 77055, 77056, 77057, 76645, 76830 and 76856) during the date range you select. These procedures and patients will be added to the WH database if not already there.
The job is queued as a background task so as to free up your terminal to do other work. You will receive a mail message when the job is done. The mail message will contain a count of the number of procedures and patients added.
[^16]This option asks you to select a start date, end date, the status of the procedures to be added to the WV Procedure (#790.1) file, whether to include patients by eligibility code, and which eligibility codes to include. Since these are past (old) procedures, you will probably want to mark them as ‘Closed’.
> **NOTE:** Please read the Edit Diagnostic Code Translation File option description before running this option.
The following information is included by this option.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
MAM Unilateral: Left or Right:
This field indicates whether this unilateral mammogram is left or right.
Health Care Facility:
This field identifies the name of the health care facility where this procedure was performed.
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed.
Date of Procedure:
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
Status:
This field contains the status (set of codes: O = Open, C = Closed). The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
WV PRINT RES/DIAG FILE

#### Print Results/Diagnosis File

[^17]For each procedure type in women’s health, only certain results or diagnoses may be selected. The Print Results Diagnosis File option displays results/diagnoses information in three lists within the report output.
The first listing displays the procedure types alphabetically and includes the results/diagnoses associated with each procedure type. The priority and normal value for each result/diagnosis are displayed.
The second listing displays the results/diagnoses sorted by priority. The priority and normal value for each result/diagnosis are displayed.
The third listing displays results/diagnoses sorted alphabetically. The priority, normal value and procedure type associated with the result/diagnosis are displayed.
These results/diagnoses correspond with the Bethesda Classification system for PAP smears and the American College of Radiology for mammograms. Results/diagnosis data is stored in the WV Results/Diagnosis (#790.31) file.
Report Description:Procedure:
[^18]This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure Type (#790.2) file.
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Priority:
This field stores an arbitrary number used to prioritize the results or diagnosis term. The range is from 1-90 with 90 being defined as normal or no results, and 1 being the highest priority.
Normal:
This field tells whether the results of the procedure were normal or abnormal. This information is used in autoqueueing normal result letters.
[^19]Associated Procedures:
This field displays the name of the procedure associated with the result/diagnosis.
WV EDIT RES/DIAG SYNONYMSEdit Synonyms for Results/Diagnoses
You may enter a synonym for each procedure type result/diagnosis. The synonym will allow the result/diagnosis to be called up by typing only a few unique characters. Synonyms should be unique and less than 6 characters. For example, ‘C1’ might be used for CIN I/mild dysplasia; ‘C2’ for CIN II/moderate dysplasia; ‘C3’ for CIN III/severe dysplasia, and so on. Each procedure type diagnosis or result may have up to two synonyms. Results/diagnosis data is stored in the WV Results/Diagnosis (#790.31) file.
Field Descriptions:Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Synonym 1:
This field contains a 1-9 character long abbreviation for the result/diagnosis. A facility may add/edit/delete a synonym to suit its needs.
Synonym 2:
This field contains an additional 1-9 character long abbreviation for the result/diagnosis. A facility may add/edit/delete a synonym to suit its needs.
WV PRINT RES/DIAG SYNONYMSPrint Synonyms for Results/Diagnoses
The Print Synonyms for Results/Diagnosis File option lists in tabular form all of the procedure type synonyms and their corresponding results/diagnoses.
Report Description:Synonym 1:
This field contains a 1-9 character long abbreviation for the result/diagnosis. A facility may add/edit/delete a synonym to suit its needs.
Synonym 2:
This field contains an additional 1-9 character long abbreviation for the result/diagnosis. A facility may add/edit/delete a synonym to suit its needs.
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
WV EDIT DIAG TRANSLATIONEdit Diagnostic Code Translation File
When mammograms are imported from the Radiology/Nuclear Medicine package, the diagnoses they are given in the Radiology/Nuclear Medicine package must be matched with the corresponding diagnoses in the Women’s Health package. This option allows you to correctly match the diagnoses between the two packages. The first prompt allows you to select a Women’s Health diagnosis; the second prompt allows you to select the corresponding radiology diagnostic code. Diagnostic code translation data is stored in the WV Diagnostic Code Translation (#790.32) file.
Field Descriptions:Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Women’s Health Diagnosis:
This field contains women’s health results/diagnosis terms relating to radiology procedures. Pointer to the WV Results/Diagnosis (#790.31) file.
Radiology Diagnostic Code:
This field contains the Radiology Diagnostic Code associated with a woman’s health results/diagnosis. Pointer to the Diagnostic Codes (#78.3) file.
WV PRINT DIAG TRANSLATION

#### Print Diagnostic Code Translation File

The Print Diagnostic Code Translation File option lists all of the Women’s Health mammogram diagnoses followed by the corresponding radiology diagnostic codes. Diagnostic code translation data is stored in the WV Diagnostic Code Translation (#790.32) file.
Report Description:Women’s Health:
This field contains women’s health results/diagnosis terms relating to radiology procedures. Pointer to the WV Results/Diagnosis (#790.31) file.
Radiology:
This field contains the Radiology Diagnostic Code associated with a woman’s health results/diagnosis. Pointer to the Diagnostic Codes (#78.3) file.
WV ADD/EDIT REFERRAL SOURCEAdd/Edit to Referral Source File
This option allows the user to add or edit referral sources and determine whether they are active or inactive. Referral source data is stored in the WV Referral Source (#790.07) file.
Field Descriptions:Referral Source Name:
This field contains a referral source used to describe how the patient was referred to the Women’s Health Program. The source can be a clinic, a special event (e.g., health fair), newspaper advertisement, or individual (such as a primary provider, self, other patient).
Status:
This field stores a set of codes (1 = Active, 0 = Inactive) used to display or hide an entry in a selection list. If the field is active, users of this package can select the entry.
[^20]WV PAP SMEAR SNOMED CODESLink Pap Smear with SNOMED Codes
Use this option to identify Morphology and Topography entries and their associated SNOMED codes used in the Lab package when resulting a Pap Smear test. When the results of a lab test are verified, the SNOMED codes used in that test will be compared to the SNOMED codes identified here to determine if the test was a pap smear. Code data is stored in the WV Procedure Type (#790.2) file.
Field Descriptions:Morphology SNOMED Code:
This field identifies the name of the Morphology and the SNOMED codes used in the Morphology field of a lab test to indicate the lab test is a pap smear.
Diagnosis:
This field is used to categorize the diagnosis as either No Evidence of Malignancy, Abnormal, or Unsatisfactory.
Topography SNOMED Code:
This field identifies the name of the specimen or source and the SNOMED codes used in the Topography field of a lab test to indicate the lab test is a pap smear.

### Chapter 3 Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Having completed the instructions for implementing the software as indicated in the previous chapters, you are now ready to use the options. The content contained in the following chapters provides information on all software options which can be used by clinical staff, clinical staff managers, and IRMS. This information includes the name, description or purpose for the option, menu access, and field descriptions.
Remember that on-line help is available when questions arise. The user can type ? or ??, after any prompt to get a help message that generally tells the user what to do. In some instances, a specific list of possible responses is displayed. All field names in the Women’s Health application have descriptions associated with them. Help is also available at the menu level by typing a ??, ???, or ?OPTION.

### Chapter 4 Patient Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-PATIENT MANAGEMENTPatient Management
The Patient Management Menu is divided into three groups of options: the patient related options, the procedure related options, and the notification related options.
The patient related options deal mainly with managing patients. The procedure related options deal more directly with the adding, editing, and printing of procedures. The notification related options deal mostly with the adding, editing, and printing of notifications.
Menu Display:
Select OPTION NAME: WV MENU-PATIENT MANAGEMENT Patient Management
WOMEN'S HEALTH: \* PATIENT MANAGEMENT MENU \* HINES DEVELOPMENT
=============================
[^21]PC Edit/Print Patient Case Data
PP Patient Profile
FS Print Patient Demographic Info (Face Sheet)
BD Browse Patients With Needs Past Due
LAB Save Lab Test as Procedure
AP Add a NEW Procedure
EP Edit a Procedure
HS Health Summary
BP Browse Procedures
PR Print a Procedure
HIS Add an HISTORICAL Procedure
RA Add a Refusal of Treatment
RE Edit a Refusal of Treatment
AN Add a New Notification
EN Edit a Notification
BN Browse Notifications
PL Print Individual Letters
PQ Print Queued Letters
> **NOTE:** The option MST Status Add/Edit was added to this menu by patch WV\*1\*11 in June 2000, and then this option was removed by patch WV\*1\*14 in April 2001.
WV EDIT PATIENT CASE DATA

#### Edit/Print Patient Case Data

This option allows you to add a new patient and her case data to the Women’s Health register. It also allows you to edit the case data of patients already in the register. When you add or edit a patient’s case data, you will be presented with the ‘Edit Patient Case Data’ screen.
The fields in the top third of the screen (patient name, address, SSN, and phone number) are editable only through the PIMS Registration module. Patient data is stored in the WV Patient (#790) file.
Field Descriptions:
These fields appear above the dashed line on every screen:
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Street:
This field contains the patient’s street address.
City/State/Zip:
This field contains the patient’s city, state, and zip code.
[^22]Eligibility Code:
This field contains the eligibility code of the patient.
SSN:
This field contains the social security number of the patient.
Patient Phone:
This field contains the patient’s phone number.
Primary Provider:
This field contains the name of the patient’s primary caregiver.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
[^23]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
These fields appear below the dashed line:
Case Manager:
This field contains the name of a person who is currently managing the women’s health care needs of this patient. NOTE: All case managers must be entered by the ADPAC under the File Maintenance Menu.
Date Inactive:
This field contains the date on which this patient’s record became inactive. ANY date (past, present, or future) will cause this patient’s data to be excluded from all reports that assess treatment needs (i.e., Snapshot of the Program Today report and Browse Patients with Needs Past Due).
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Tx Due Date:
This field contains the date by which the breast Tx procedure should be completed.
Breast Tx Facility:
The name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Tx Due Date:
This field contains the date when this gynecologic procedure or treatment should be completed.
Cervical Tx Facility:
The name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
PAP Regimen:
This field stores the current PAP regimen for the patient. The regimen appears in an abbreviated form so that it can be listed on several screens where there is limited space. The following abbreviations apply:
<u>symbol</u> <u>meaning</u>
P PAP
C colposcopy
wk week
m month
y year
q every
pp postpartum
x2 times 2
x3 times 3
ga gestation
The abbreviations read much like a prescription. For example, ‘Pq6mx2, Pqy’ stands for ‘PAP every 6 months times 2, then PAP every year (annually)’. Another example, ‘P6wkpp, C8-12wkpp’ stands for ‘PAP at 6 weeks postpartum, then colposcopy 8 to 12 weeks postpartum’.
PAP Regimen Start Date:
This field stores a date on which the patient began or will begin her current PAP regimen.
[^24]CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Family Hx of Breast CA:
[^25]This field identifies if the patient’s relatives have had breast cancer. The information may be selected from a set of codes to indicate no family history, a 2<sup>nd</sup> degree relative (cousin, aunt, grandmother), a 1<sup>st</sup> degree relative (mother OR sister), multiple 1<sup>st</sup> degree relatives (mother AND sister), personal history, or unknown.
Notes (WP):
This is a word processing field that stores additional information about the patient and her health care needs.
DES Daughter:
[^26]This field indicates if this patient’s mother took diethylstilbestrol (DES) when she was pregnant with this patient. Choices are yes, no, and unknown.
<span id="MCC_field_definition" class="anchor"></span>Maternity Care Coordinator:
Maternity Care Coordinator is assigned to pregnant female patients to coordinate their maternity care.
Date of 1<sup>st</sup> Encounter:
This field contains the date of the patient’s first clinic visit. Although a date is automatically stuffed when the Automatically Load Patients \[WV AUTOLOAD PATIENTS\] option is run, the information can be edited through the Edit/Print Patient Case Data option.
Referral Source:
This field stores information on who referred the patient or how the patient found out about the women’s health care services at the facility. This field points to entries in the WV Referral Source (#790.07) file. Additional choices may be added by the facility via the option Add/Edit to Referral Source File.
After exiting the ‘Edit Patient Case Data’ screen you will be given the opportunity to print the patient’s case data to a device.
WV PATIENT PROFILE

#### Patient Profile

This option allows you to list all the procedures and notifications associated with an individual patient. If you choose the brief format, only the patient’s procedures will be listed. If you choose the detailed format, both procedures and notifications, as well as PAP regimen changes and pregnancies will be listed.
The patient’s case data is shown above the double-dashed line, while the procedures, their dates, results, and status are shown below. If the device selected for the patient profile is ‘Home’ (to the screen), a column of numbers will appear to the left of the procedures (and of the notifications in the detailed report). Patient data is stored in the WV Patient (#790) file.
Report Description:
These fields appear above the dashed line, and appear on every page of the report:
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a person who is currently managing the women’s health care needs of this patient.
Facility:
This field contains the name of the facility responsible for the women’s health care needs of this patient. If the health care facility you wish to select is not available in this file, contact your site manager or ADPAC. Pointer to the Institution (or Facility) (#4) file.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Primary Provider:
This field contains the name of the primary provider who is responsible for the women’s health care needs of this patient.
[^27]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
[^28]Family Hx of Breast CA:
This field identifies if the patient’s relatives have had breast cancer. The information may be selected from a set of codes to indicate no family history, a 2<sup>nd</sup> degree relative (cousin, aunt, grandmother), a 1<sup>st</sup> degree relative (mother OR sister), multiple 1<sup>st</sup> degree relatives (mother AND sister), personal history, or unknown.
[^29]Eligibility Code:
This field contains the eligibility code of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
<span class="mark">  
</span><span id="WV_Patient_profile_MCC_definition" class="anchor"></span>Maternity Care Coordinator:
A Maternity Care Coordinator is a user that is assigned to pregnant female patients to coordinate their maternity care.
These fields appear below the dashed line:
Date:
This field contains the date the procedure was performed.
Procedure:
This field displays the abbreviation of the procedure (type) performed on the patient. Pointer to the WV Procedure (#790.1) file.
Results/Diagnosis:
This field displays the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Status:
This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
The following fields only appear on the detailed report:
PAP Regimen Change:
This is the beginning date of change and the name of the new regimen.
<span id="WV_124_pregnancy_status_remove_codes" class="anchor"></span>Pregnancy Status:
This field contains information on the pregnancy status of the patient. When the pregnancy status is unknown, the field is blank.
Notifications:
This includes the procedure accession number and name associated with the notification, notification outcome, status, purpose, and type.
Procedures:
This field includes the Women’s Health procedure accession number.
WV PATIENT DEMOGRAPHIC INFOPrint Patient Demographic Info (Face Sheet)
This option allows you to display or print patient demographic information. It provides information such as the patient’s address, phone numbers, spouse, emergency contacts and billing information. Patient demographic data is stored in the Patient (#2) file.
Field Descriptions:Name:
This field contains the name of the patient. It is a pointer to the Patient (#2) file.
SSN:
This computed field displays the patient’s social security number from the Patient (#2) file.
Address:
This field contains the address of the patient.
County:
This field contains the name of the county where the patient lives.
Phone:
This field contains the patient’s phone number.
Office:
This field contains the patient’s office phone number.
Temporary:
This field contains the patient’s temporary address, if there is one.
From/To:
This field contains the from/to dates in which the patient lived at the temporary address.
Phone:
This field contains the phone number for the temporary address.
[^30]Confidential Address:
This field contains a confidential address for the patient.
Confidential Address Categories:
This field contains the category of the confidential address.
From/To:
This field contains the date range for the confidential address.
Primary Eligibility:
This field contains the primary benefits eligibility code for this patient.
Other Eligibilities:
This field contains any other benefits eligibility codes for this patient.
Status:
This field contains the eligibility status for this patient.
Discharge Type:
This field contains the type of discharge which the patient received for her most recent episode of military service.
Admitted:
This is the date the patient was admitted to the hospital.
Discharged:
This is the date the patient was discharged from the hospital.
Ward:
This field contains the current ward location on which this patient is residing if an inpatient.
Room-Bed:
This field contains the current room and bed on which this patient is residing if an inpatient.
Provider:
This field stores the name of the provider currently assigned to this patient.
Specialty:
This field contains the treating specialty to which this inpatient is currently assigned.
Attending:
This field contains the name of the attending physician currently responsible for the care of this patient.
Admission LOS:
This field contains the number of days the patient has been in the hospital during the current stay.
Absence Days:
This field contains the number of days the patient has been absent from the hospital.
Pass Days:
This field contains the number of days the patient has been on pass.
ASIH Days:
The field contains the number of days the patient is Absent Sick In Hospital (ASIH).
Currently enrolled in:
This field contains any insurance programs the patient is currently enrolled in.
Future Appointments:
This field contains a list of any future appointments the patient may have.
Remarks:
This field contains any short comments the user may wish to enter about this patient.
WV BROWSE NEEDS PAST DUE

#### Browse Patients With Needs Past Due

This option allows you to search for and browse through patients whose treatment needs are past due. The five questions that are asked prior to the display allow you to specify the needs, dates, case managers, order of display, and device for the display.
> **NOTE:** It may be useful to select a date at some time in the future, for example, two weeks ahead, in order to anticipate which patients will become delinquent and to act on those cases ahead of time.
If the device selected is ‘Home’ (to the screen), a column of numbers will appear to the left of the chart numbers.
A patient will not be processed if there is any value (past, present, or future) in the Date Inactive field on the Edit/Print Patient Case Data option screen. Patient needs past due data is stored in the WV Patient (#790) file.
[^31]NOTE: When the option is run it checks the Patient (#2) file for a date of death. If there is a date of death, it will be entered as the inactive date in the Women's Health database.
Report Description:SSN:
This field contains the social security number of the patient.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Case Manager:
This field contains the name of a person who is currently managing the women’s health care needs of this patient.
Treatment Need and Due by Date:
This field contains the name of the current or next procedure or treatment need scheduled for this patient, including the due by date.
Primary Care Provider:
This field contains the name of the primary provider who is responsible for the women’s health care needs of this patient.
[^32]Age:
This field contains the age of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
Eligibility Code:
This field contains the eligibility code of the patient.
[^33]WV SAVE LAB TESTSave Lab Test as Procedure
This option is used to save lab tests as procedure entries in the Women's Health package. Lab tests for cytology and surgical pathology are passed to the Women's Health package from the Lab package and stored in the WV Lab Tests (#790.08) file. A mail message is sent to the patient's case manager stating a lab test has been released to the Women's Health package. This option allows the user to first view the lab tests in an uneditable screen, then dispose of the lab tests either by 1) adding the lab test data into a Women's Health package procedure, 2) deleting the lab test from the WV Lab Tests file (i.e., don't convert it into a Women's Health procedure), or 3) ignore the lab test for the time being. The lab test can be looked up by requesting provider, lab accession, patient name or SSN, or date of test.
If the user chooses to add the lab test to the Women's Health package, the user is first asked to select a WH procedure type, to associate with the lab test (e.g., PAP Smear). The lab test is saved as a Women's Health procedure in the WV Procedure (#790.1) file. The user is placed in the procedure data entry screen and may edit/close out the procedure entry. The lab report can be viewed again by going into the Reports (WP) field.
The software may provide a default response at the "Select Lab Test Accession \#:" prompt. The software checks each entry, if the user is the requesting provider for a test, or the Women's Health case manager for a patient, that entry will be displayed as a default response. A default response is provided until the user has looped through all associated tests or up-arrows out of the option. The user may enter a question mark to see a list of all entries or select any entry to process.
> **NOTE:** This option can only work if the Lab package patch LR\*5.2\*231 is installed and the "Import Test from Laboratory" field is set to 'Yes' for the facility in the Edit Site Parameters \[WV EDIT SITE PARAMETERS\] option.
It is possible that the wrong patient was originally associated with a lab test. When this happens, the Lab package has an option to associate the correct patient with the lab test. The Lab package contains a check that will call the Women's Health package if a lab test is moved from one patient to another. If the lab test was converted into a Women's Health procedure entry the Women's Health package does the following:
1\. Disassociates the Women's Health entry from the Lab package entry (i.e., will not delete the Women's Health entry, but will not show the lab results).
2\. Changes the Result/Dx of the Women's Health entry to 'Error/disregard'.
3\. Sends a mail message to the case manager stating lab results no longer belong to that patient and identify the Women's Health entry. The case manager can then make any additional changes or add notes to the record.
[^34]4. If the new patient associated with the lab test is female, then the lab test will be passed to the Women's Health package and stored as a new entry in the WV Lab Test (#790.08) file.
If the results of a lab test are ever edited by the Lab user, and the lab test was saved as a WH procedure entry, the case manager will receive a mail message indicating the lab report has changed. Also, the status of the WH procedure entry will be set to 'Open', and the Complete by (Date) is updated.
[^35]Note: Prior to software patch WV\*1\*16, there was no way to automatically identify a lab test as a pap smear. WV\*1\*16 allows SNOMED codes to be used to identify a lab test as a pap smear. First, use the Link Pap Smear with SNOMED Codes option to associate a pap smear with a SNOMED code, then you don’t need to use the Save Lab Test as Procedure option to save that lab test as a Women’s Health package procedure. Instead, a CPRS alert is sent to the WH case manager and the provider, and the lab test is saved automatically as a Women’s Health procedure in the WV Procedure file (#790.1).
WV ADD A NEW PROCEDUREAdd a NEW Procedure
This option allows you to add procedures for patients. The first prompt asks you to select a patient (either by name, or SSN). The second prompt asks you to select a procedure. The possible choices of procedures are listed in the table below:
[^36]Breast Ultrasound – BU Laser Ablation – LA
<span id="BRMRI_BTB_BTS_BTU" class="anchor"></span>Breast MRI – BRMRI Laser Cone - LC
Breast Tomosynthesis Bilat – BTB LEEP - LP
Breast Tomosynthesis Screening – BTS Lumpectomy - LM
Breast Tomosynthesis Unilat – BTU Mammogram Dx Bilat - MB
Clinical Breast Exam - CB Mammogram Dx Unilat - MU
Colposcopy Impression (No BX) - CI Mammogram Screening - MS
Colposcopy w/Biopsy - CO Mastectomy - MT
Cone Biopsy - CN Needle Biopsy - NB
Cryotherapy - CY Open Biopsy - OB
Ectocervical Biopsy - EB PAP Smear - PS
Endocervical Curettage - EC Pelvic Ultrasound - PU
Endometrial Biopsy - EM Pregnancy Test - PT
Fine Needle Aspiration - FN STD Evaluation - ST
General Surgery Consult - GS Stereotactic Biopsy - SB
GYN ONC Consult - GY Tubal Ligation - TL
Hysterectomy - HY Vaginal Ultrasound - VU
The procedure is selected by typing either its name or its abbreviated code, for example, ‘PS’ will select ‘PAP Smear’. (These codes are also used in the accession numbers, for example, ‘PS1998-43’ will be an accession# for a PAP smear.)
If the procedure is a unilateral mammogram, an additional prompt will ask you to enter ‘Left or Right’. If the procedure is a colposcopy w/biopsy, an additional prompt will ask you to select the accession# of the PAP that initiated this colposcopy.
A final prompt asks you for the date of the procedure. At this point the computer checks to see if this procedure has already been entered for this patient on this date. If so, then this would be a duplicate procedure.
Once you have added a valid new procedure, the program will automatically assign the procedure a unique accession# and then proceed to the ‘Edit a Procedure’ screen. the accession# for a procedure uniquely identifies that procedure for all editing and reporting purposes. Procedure data is stored in the WV Procedure (#790.1) file.
[^37] [^38]NOTE: When a Radiology/Nuclear Medicine package exam is passed to the Women's Health package, a CPRS alert instead of a MailMan message is sent to the WH case manager and the provider.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this woman’s health needs.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^39]Eligibility Code:
This field contains the eligibility code of the patient.
[^40]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date of Procedure (Required):
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
<span id="WV_124_move_Complete_by_date" class="anchor"></span>Complete by (Date):
This field contains the date used to determine that this procedure record is delinquent when a close status has not been entered in the record.
Clinician/Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
<span id="WV_124_add_proc_status_move" class="anchor"></span>Status:
<span id="Entered_in_Error_1" class="anchor"></span>This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent, E = Entered in Error) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
(page 1 of 2):
Some procedures, such as colposcopy, cone biopsy, laser cone, and LEEP, will have a page 2 to the ‘Edit a Procedure’ screen. This is indicated by the words ‘(page 1 of 2)’ on page 1. Page 2 is concerned with the clinical findings and tissue pathology results of colposcopy and similar procedures.
If there is no page 2 of data fields to be edited, then when you have completed the edits for this page you would save and exit this procedure via the command line at the bottom of the screen.
Page 2 – Colposcopy:
The clinical findings (for page 2) are usually found on a form used by the physician performing the colposcopy or biopsy. The tissue pathology report section would be used most commonly for colposcopies in which an ECC and a biopsy were performed at the same time as the colposcopy. Therefore, you will not need to add separate procedures for a biopsy and ECC if they are done with a colposcopy.
<span id="Follow_Up_Date_1" class="anchor"></span>Follow Up Item:
This will display a pop-up with the following fields:
- Follow Up Item
- Date/Time
- Note (Read Only)
- Entered in Error
- Follow up Date
- Comments
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed. NOTE: If the entry in the Hospital Location (#44) file has the Institution (#3) field filled in, the institution will be provided as the default for the field Health Care Facility.
[^41]Reports (WP):
If the report is from a Radiology/NM procedure, this field contains data from the Radiology/NM Report (#74) file. If a radiology report is unverified and then verified again, the words “AMENDED REPORT” will appear with the data displayed in this field. If the report is from a lab test, this field contains data from the Lab Data (#63) file. Users can get to this field by using the TAB key from the Ward/Clinic/Location field.
Health Care Facility (Required):
This field identifies the name of the health care facility where this procedure was performed.
[^42]Notes (WP):
A word-processing field for storing extensive notes/comments about this case. If there is text data present, a ‘+’ will appear to the right of the field label, like so: (WP): +. Users can get to this field by using the TAB key from the Health Care Facility field.
Comments:
An optional one-line clinical history note (limited to 78 characters).
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
> **NOTE:** Procedures cannot be deleted. If a procedure has been entered in error or is invalid for some other reason, enter a results/diagnosis of ‘Error/disregard’. Procedures with a results/diagnosis of ‘Error/disregard’ will not appear on Patient Profiles, nor will they be included in the various epidemiology reports. These procedures can be viewed only under the Patient Profile Including Errors option of the Manager’s Patient Management menu.
HPV:
This field is used to document the presence or absence of the Human Papilloma Virus (HPV) in the cytology reports.
<span id="WV_124_Outside_report_add_proc" class="anchor"></span>Outside Report:
This field marks if the procedure is related to a procedure done outside the VA. This field is set from the Reminder Dialog that updates the procedure entry.
Sec Results/Diagnosis:
This field stores a secondary outcome/diagnosis associated with the procedure. Pointer to the WV Results/Diagnosis (#790.31) file.
Screening PAP:
This field stores the PAP procedure associated with the follow-up procedure (e.g., colposcopy). Pointer to the WV Procedure (#790.1) file.
T-Zone Seen Entirely:
This field documents (set of codes: 1 = Yes, 0 = No) that the T-Zone in the colposcopy/biopsy procedure was adequately visualized.
Multifocal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was multifocal (as opposed to unifocal).
Lesion Outside Canal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was outside the canal.
Number of Quadrants:
This field contains a number (0-4) that identifies the number of quadrants occupied by the lesion.
Satisfactory Exam:
This field documents that the procedure or gynecologic exam was satisfactorily performed without any impediments. Set of codes (1 = Yes, 0 = No).
Quadrant Locations:
The location of the affected quadrants. Any of the following abbreviations may be selected: UL,LL,UR,LR. If more than one quadrant is included, separate them with a comma.
Impression:
This field contains the impression of the clinician performing the exam. Pointer to the WV Results/Diagnosis (#790.31) file.
ECC Dysplasia:
This field indicates if ectocervical dysplasia was present, if an insufficient tissue sample was provided, or the sample was not examined for dysplasia.
Margins Clear:
This field indicates tissue sample showed no pathology at the margins of the tissue sample.
Ectocervical Biopsy:
This field contains the diagnosis or impression resulting from the cytology examination. Pointer to the WV Results/Diagnosis (#790.31) file.
Stage:
This field documents the clinical stage for invasive carcinoma of the cervix. If clinical stage is unknown, enter the summary ('S-') stage.
STD Evaluation:
This field documents the findings after testing for sexually transmitted diseases. Pointer to the WV Results/Diagnosis (#790.31) file.
WV EDIT PROCEDURE

#### Edit a Procedure

This option allows you to edit previously documented procedures for patients. The first prompt asks you to select an accession# or patient name. A patient’s SSN may also be entered. An accession# would be of the form ‘PS1998-24’. If you know the accession# of the procedure you wish to edit, it will be more efficient to select the procedure by its accession# rather than by its patient (some patients will have several procedures on file). Procedure data is stored in the WV Procedure (#790.1) file.
[^43] [^44]NOTE: When a Radiology/Nuclear Medicine package exam is passed to the Women's Health package, a CPRS alert instead of a MailMan message is sent to the WH case manager and the provider.
Field Descriptions:
Page 1 - All Procedures:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this woman’s health needs.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^45]Eligibility Code:
This field contains the eligibility code of the patient.
[^46]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date of Procedure (Required):
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
Clinician/Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
<span id="WV_124_move_Complete_by_date_edit_proc" class="anchor"></span>Complete by (Date):
This field contains the date used to determine that this procedure record is delinquent when a close status has not been entered in the record.
<span id="WV_124_edit_proc_status_move" class="anchor"></span>Status:
<span id="Entered_in_Error_2" class="anchor"></span>This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent, E = Entered in Error) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
(page 1 of 2):
Some procedures, such as colposcopy, cone biopsy, laser cone, and LEEP, will have a page 2 to the ‘Edit a Procedure’ screen. This is indicated by the words ‘(page 1 of 2)’ on page 1. Page 2 is concerned with the clinical findings and tissue pathology results of colposcopy and similar procedures.
If there is no page 2 of data fields to be edited, then when you have completed the edits for this page you would save and exit this procedure via the command line at the bottom of the screen.
Page 2 – Colposcopy:
The clinical findings (for page 2) are usually found on a form used by the physician performing the colposcopy or biopsy. The tissue pathology report section would be used most commonly for colposcopies in which an ECC and a biopsy were performed at the same time as the colposcopy. Therefore, you will not need to add separate procedures for a biopsy and ECC if they are done with a colposcopy.
<span id="Follow_Up_Date_2" class="anchor"></span>Follow Up Item:
This will display a pop-up with the following fields, the values contained in this field are populated by the clinical user using Reminder Dialogs in CPRS:
- Follow Up Item
- Date/Time
- Note (Read Only)
- Entered in Error
- Follow up Date
- Comments
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed. NOTE: If the entry in the Hospital Location (#44) file has the Institution (#3) field filled in, the institution will be provided as the default for the field Health Care Facility.
[^47]Reports (WP):
If the report is from a Radiology/NM procedure, this field contains data from the Radiology/NM Report (#74) file. If a radiology report is unverified and then verified again, the words “AMENDED REPORT” will appear with the data displayed in this field. If the report is from a lab test, this field contains data from the Lab Data (#63) file. Users can get to this field by using the TAB key from the Ward/Clinic/Location field.
Health Care Facility (Required):
This field identifies the name of the health care facility where this procedure was performed.
[^48]Notes (WP):
A word-processing field for storing extensive notes/comments about this case. If there is text data present, a ‘+’ will appear to the right of the field label, like so: (WP): +. Users can get to this field by using the TAB key from the Health Care Facility field.
Comments:
An optional one-line clinical history note (limited to 78 characters).
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
> **NOTE:** Procedures cannot be deleted. If a procedure has been entered in error or is invalid for some other reason, enter a results/diagnosis of ‘Error/disregard’. Procedures with a results/diagnosis of ‘Error/disregard’ will not appear on Patient Profiles, nor will they be included in the various epidemiology reports. These procedures can be viewed only under the Patient Profile Including Errors option of the Manager’s Patient Management menu.
HPV:
This field is used to document the presence or absence of the Human Papilloma Virus (HPV) in the cytology reports.
<span id="WV_124_Outside_report_edit_proc" class="anchor"></span>Outside Report:
This field marks if the procedure is related to a procedure done outside the VA. This field is set from the Reminder Dialog that updates the procedure entry.
Sec Results/Diagnosis:
This field stores a secondary outcome/diagnosis associated with the procedure. Pointer to the WV Results/Diagnosis (#790.31) file.
Screening PAP:
This field stores the PAP procedure associated with the follow-up procedure (e.g., colposcopy). Pointer to the WV Procedure (#790.1) file.
T-Zone Seen Entirely:
This field documents (set of codes: 1 = Yes, 0 = No) that the T-Zone in the colposcopy/biopsy procedure was adequately visualized.
Multifocal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was multifocal (as opposed to unifocal).
Lesion Outside Canal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was outside the canal.
Number of Quadrants:
This field contains a number (0-4) that identifies the number of quadrants occupied by the lesion.
Satisfactory Exam:
This field documents that the procedure or gynecologic exam was satisfactorily performed without any impediments. Set of codes (1 = Yes, 0 = No).
Quadrant Locations:
The location of the affected quadrants. Any of the following abbreviations may be selected: UL,LL,UR,LR. If more than one quadrant is included, separate them with a comma.
Impression:
This field contains the impression of the clinician performing the exam. Pointer to the WV Results/Diagnosis (#790.31) file.
ECC Dysplasia:
This field indicates if ectocervical dysplasia was present, if an insufficient tissue sample was provided, or the sample was not examined for dysplasia.
Margins Clear:
This field indicates tissue sample showed no pathology at the margins of the tissue sample.
Ectocervical Biopsy:
This field contains the diagnosis or impression resulting from the cytology examination. Pointer to the WV Results/Diagnosis (#790.31) file.
Stage:
This field documents the clinical stage for invasive carcinoma of the cervix. If clinical stage is unknown, enter the summary ('S-') stage.
STD Evaluation:
This field documents the findings after testing for sexually transmitted diseases. Pointer to the WV Results/Diagnosis (#790.31) file.
[^49]WV HS-USER DEFINED

#### Health Summary

This option allows the user to create a Health Summary report for a specific patient. The user may select multiple Health Summary components to create the health summary report.
The user selects a patient, then selects one or more Health Summary components such as Cytology or Surgical Pathology. The Health Summary components offer default values for the number of occurrences to return and time span to cover. For example, after selecting the Cytology component for display, the default values for time limit may be 1 year, and number of occurrences to display may be 10. This means the Health Summary package will search the lab database for Cytology tests from 1 year ago up to today. The 10 most recent tests will be displayed. The user may edit the default limits for each of the selected components at the “Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD:” prompt. After selecting one or more of the components, the user can then edit the default for number of occurrences to return at the “OCCURRENCE LIMIT:” prompt, and the default time span to cover at the “TIME LIMIT:” prompt. Also, a special “HEADER NAME:” may be assigned to the report output. The user is then asked to select a device.
WV BROWSE PROCEDURES

#### Browse Procedures

This option allows you to search for and list procedures. The eight questions that are asked prior to the display allow you to specify patients, procedures, date range, status, normal/abnormal, case manager (site parameter), order of display, and device for the printout.
If the device selected for the ‘Browse Procedures’ display is ‘Home’ (to the screen), a column of numbers will appear to the left of the procedures. Procedure data is stored in the WV Procedure (#790.1) file.
Report Description:SSN:
This field contains the social security number of the patient.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Date:
This field contains the date the procedure was performed.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Status:
This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
Results/Diagnosis:
This field displays the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
WV PRINT A PROCEDURE

#### Print a Procedure

This option allows you to print information pertaining to a patient’s procedure. You are prompted for an accession# or patient name, and for a device. The display/printout looks very similar to the ‘Edit a Procedure’ screen. Procedure data is stored in the WV Procedure (#790.1) file.
Report Description:
These fields appear on the top of every page of the report:
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
Procedure:
This field displays the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^50]Eligibility Code:
This field contains the eligibility code of the patient.
[^51]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
Maternity Care Coordinator:
A Maternity Care Coordinator is a user that is assigned to pregnant female patients to coordinate their maternity care.
Page 1:
Date of Procedure:
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
Date First Entered:
This field displays the date on which this procedure record was first entered.
First Entered By:
This field identifies the name of the person who first entered data on this procedure.
[^52]Lab Accession#:
This field displays the Laboratory package accession number for the procedure, if one exists.
Clinician/Provider:
This field displays the name of the clinician who ordered and/or performed this procedure.
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed. NOTE: If the entry in the Hospital Location (#44) file has the Institution (#3) field filled in, the institution will be provided as the default for the field Health Care Facility.
Health Care Facility:
This field identifies the name of the health care facility where this procedure was performed.
Comments:
An optional one-line clinical history note (limited to 78 characters).
Complete by (Date):
This field contains the date used to determine that this procedure record is delinquent when a close status has not been entered in the record.
Results/Diagnosis:
This field displays the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Sec Results/Diagnosis:
This field displays a secondary outcome/diagnosis associated with the procedure. Pointer to the WV Results/Diagnosis (#790.31) file.
HPV:
This field displays the presence or absence of the Human Papilloma Virus (HPV) in the cytology reports.
Status:
<span id="Entered_in_Error_3" class="anchor"></span>This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent, E = Entered in Error) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
Page 2 (for colposcopy only):
Screening PAP:
This field displays the PAP procedure associated with the follow-up procedure (e.g., colposcopy). Pointer to the WV Procedure (#790.1) file.
T-Zone Seen Entirely:
This field documents (set of codes: 1 = Yes, 0 = No) that the T-Zone in the colposcopy/biopsy procedure was adequately visualized.
Multifocal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was multifocal (as opposed to unifocal).
Lesion Outside Canal:
This field documents (set of codes: 1 = Yes, 0 = No) that the lesion seen during the procedure was outside the canal.
Number of Quadrants:
This field contains a number (0-4) that identifies the number of quadrants occupied by the lesion.
Satisfactory Exam:
This field documents that the procedure or gynecologic exam was satisfactorily performed without any impediments. Set of codes (1 = Yes, 0 = No).
Quadrant Locations:
The location of the affected quadrants. Any of the following abbreviations may be selected: UL,LL,UR,LR. If more than one quadrant is included, separate them with a comma.
Impression:
This field contains the impression of the clinician performing the exam. Pointer to the WV Results/Diagnosis (#790.31) file.
Page 3 (for colposcopy only):
ECC Dysplasia:
This field indicates if ectocervical dysplasia was present, if an insufficient tissue sample was provided, or the sample was not examined for dysplasia.
Margins Clear:
This field indicates tissue sample showed no pathology at the margins of the tissue sample.
Ectocervical Biopsy:
This field contains the diagnosis or impression resulting from the cytology examination. Pointer to the WV Results/Diagnosis (#790.31) file.
Stage:
This field documents the clinical stage for invasive carcinoma of the cervix. If clinical stage is unknown, enter the summary ('S-') stage.
STD Evaluation:
This field documents the findings after testing for sexually transmitted diseases. Pointer to the WV Results/Diagnosis (#790.31) file.
Page 4:
[^53]Notes:
This is text describing the results/diagnosis of the procedure.
WV ADD AN HISTORICAL PROCEDUREAdd an HISTORICAL Procedure
This option allows you to add procedures for a patient done in years past, in order to make her Patient Profile more complete. Only a minimum of data is required: date of procedure, procedure, results, HPV status and an optional health care facility.
If you wish to enter more of the data on a procedure from years past, you may of course add the procedure through the standard Add a NEW Procedure option. There is no requirement to add an old procedure under the Historical option. It is important, however, that current procedures be added under the Add a NEW Procedure option, where many more of the important and relevant fields are available for entering data. Procedure data is stored in the WV Procedure (#790.1) file.
Field Descriptions:Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Date:
This field contains the date that the procedure was performed.
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
HPV:
This field is used to document the presence or absence of the Human Papilloma Virus (HPV) in the cytology reports.
Health Care Facility:
This field identifies the name of the health care facility where this procedure was performed.
WV REFUSED PROC-ADDAdd a Refusal of Treatment
This option allows you to document a refusal of treatment if the patient declines to be treated at this treatment site for any reason. Refusal of treatment data is stored in the WV Refusals (#790.3) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^54]Eligibility Code:
This field contains the eligibility code of the patient.
[^55]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date Refused:
This field contains the date the patient refused the procedure, test, or examination.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Reason:
This field indicates a general reason for why the patient refused treatment, i.e., (1) treatment was provided elsewhere, (2) no reason was given by the patient, or (3) another reason was provided by the patient.
Comments:
This field contains comments related to this refusal (limited to 3-75 characters).
WV REFUSED PROC-EDITEdit a Refusal of Treatment
This option allows editing of an existing patient's refusal for treatment. The user must identify the record to be edited by entering a date that the treatment was refused or by selecting from a list of records in the WV Refusals (#790.3) file. Refusal of treatment data is stored in the WV Refusals (#790.3) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^56]Eligibility Code:
This field contains the eligibility code of the patient.
[^57]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date Refused:
This field contains the date the patient refused the procedure, test, or examination.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Reason:
This field indicates a general reason for why the patient refused treatment, i.e., (1) treatment was provided elsewhere, (2) no reason was given by the patient, or (3) another reason was provided by the patient.
Comments:
This field contains comments related to this refusal (limited to 3-75 characters).
WV ADD A NEW NOTIFICATIONAdd a New Notification
This option allows you to add notifications for patients. A notification is a communication between the clinic staff and the patient.
When you add a notification, it must be given a type of notification. Most notifications are letters; however, they may also be phone calls, conversations, etc. The table below lists all the types of notifications that are available in Women’s Health:
CONTACT CHA MESSAGE VIA PERSON
CONTACT PHN MESSAGE VIA PHONE MACHINE
CONVERSATION WITH PATIENT PHONE CALL, 1ST
LETTER, FIRST PHONE CALL, 2ND
LETTER, SECOND PHONE CALL, 3RD
LETTER, SECOND (CERTIFIED) PROVIDER CONSULT
LETTER, THIRD (CERTIFIED) PACT/PC TO NOTIFY
<span id="Secure_Messaging_Pact_PC_to_Notify" class="anchor"></span>SECURE MESSAGING
When you add a notification, it must also be given a purpose of notification. The purpose of notification is the reason the patient is being contacted. The table below lists the purposes of notification that come pre-loaded in Women’s Health. It is possible to add other purposes of notification customized to your particular site, and to edit the ones listed below as well. (See Add/Edit a Notification Purpose & Letter option.)
COLP Abnormal, need further Tx
COLP follow up, PAP next month.
COLP follow up, next PAP 6 months.
DNKA Colposcopy (Did Not Keep Appt)
DNKA Colposcopy Follow Up
DNKA PAP routine
DNKA PAP asap
DNKA PAP urgent
MAM result normal, next MAM 1 year.
PAP abnormal, need colp 8-12 weeks PP.
PAP result abnl, rep PAP 3-6 mos.
PAP result abnormal, PAP 6 weeks P.P.
PAP result abnormal, next PAP 3 months and colp.
PAP result abnormal, schedule colposcopy.
PAP result normal, next PAP 1 year.
PAP result normal, next PAP 4 months.
PAP result normal, next PAP 6 months.
PAP, annual due.
PAP, follow-up due.
PREGNANCY Test NEGATIVE
PREGNANCY Test POSITIVE
Eventually, each notification should be given an outcome. The outcome of a notification describes the final result of the contact with the patient. The table below lists the outcomes that come pre-loaded in Women’s Health. It is possible to add other outcomes customized to your particular site, and to edit the ones listed below as well. (See Add/Edit Notification Outcomes option.)
Chart Flagged
Declined Tx
MAM Normal letter sent
No known address
No response
PAP Normal letter sent
PHN referral
Patient Deceased
Patient left Service Area
Provider consult
Response not tracked
Scheduled appt for Colposcopy
Scheduled appt for PAP
Scheduled appt for Repeat PAP
Tx elsewhere
Unable to contact Patient
As stated above, this option allows you to add notifications for patients. The first prompt asks you to select a patient (either by name, or SSN). After you have selected a patient, the ‘Edit a Notification’ screen appears. Notification data is stored in the WV Notification (#790.4) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^58]Eligibility Code:
This field contains the eligibility code of the patient.
[^59]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Date Notification Opened (Required):
This field contains the date the notification was first created.
Facility (Required):
Select the health care facility with which this letter is associated. Each letter to be printed is associated with a specific facility. When a user runs the Print Queued Letters option, only letters associated with the user’s facility will be printed. (The user’s facility is the facility (also called ‘Site’ or ‘Division’) that the user selects at sign on. If a user has only one facility, that facility is assigned automatically. For more information about selecting facilities at sign on, contact your site manager or ADPAC.) This feature allows multiple clinics to manage patients and print letters on the same computer, using the same patient database, without printing another clinic’s letters.
Purpose of Notification (Required):
This field contains the reason for the notification (e.g., the results of a test, reminder to schedule a procedure). This should be brief but descriptive enough to identify it uniquely. NOTE: This field cannot be changed because previous notifications from this purpose would become inaccurate. If the Purpose field is incorrect, make this purpose ‘Inactive’ (see next field), and then create a new purpose of notification with the correct purpose name.
Priority:
Filled in automatically, based on the purpose of notification.
<span id="WV_124_outcome_add_new_notif" class="anchor"></span>Outcome:
This field stores the results or outcome, which may be a goal or an event, associated with this patient’s notification.
Type of Notification:
This field stores the method used to notify the patient from the choices available in the WV Notification Type (#790.403) file (e.g., letter, phone call, message, etc.).
Print Date:
Date letter is to be printed. Once the letter has a ‘Print Date’, it will print out on that date (or on any later date) when the option Print Queued Letters is run. For example, if the letter is queued to print on Friday but Print Queued Letters is not run until the following Monday, then the letter will print out with the Monday batch.
The default date that appears is based on whether the letter is a results letter or a reminder letter. If it is a results letter, the default date is ‘Today’. If it is a reminder letter, the default date is based on the due date of the treatment need (breast or gynecologic) to which this purpose of notification relates. (See the Add/Edit a Notification Purpose & Letter option.)
Complete by (Date):
This field contains the date used to determine that this procedure record is delinquent when a close status has not been entered in the record.
Printed:
Filled in automatically when the letter (if the notification is a letter) is printed.
Status:
<span id="Entered_in_Error_4" class="anchor"></span>Select either ‘Open’, ‘Closed’ or ‘Enter in Error’. A notification is usually left ‘Open’ until an outcome has been entered. If the notification is a results letter, it is usually closed when the letter is printed (no further outcome is expected). If the notification is a reminder letter (reminding the patient to call for a next appointment), it is usually closed either when the patient calls to schedule an appointment, or following the edit of her next procedure. (See ‘The Basic Patient Management Loop’). A notification that is left ‘Open’ past its ‘Complete by (Date)’ will be displayed as ‘Delinquent’ on notification reports.
Patient Education:
Enter ‘Yes’ or ‘No’, depending on whether patient education occurred during the notification (for phone calls, conversations, etc.).
> **NOTE:** If the notification is a letter and the letter has already been printed, most of the fields for that notification will be blocked from editing. This is to keep the data on the computer in sync with the letter that was sent to the patient. Only the bottom four fields (Complete by Date, Outcome, Status, and Patient Ed) will be editable.
After you leave the ‘Edit a Notification’ screen, if you did not save before exiting you will be asked ‘Save changes before leaving form (Y/N)?’, and if the notification was a letter, the program will ask, ‘Do you wish to preview or print this letter now? Enter Yes or No: NO//’. ‘Preview’ allows you to look at the letter that has just been queued. To preview the letter, select ‘Home’ at the ‘Device: ‘ prompt. ‘Print’ will print the letter immediately, regardless of its ‘Print Date’, and remove it from the queue of letters waiting to print. To print the letter immediately, select a printer at the ‘Device: ‘ prompt.
If you answer ‘No’ to the ‘Do you wish to preview or print this letter now?’ prompt, the letter will remain in the queue, to be printed on its ‘Print Date’. NOTE: These letters do not print automatically, the user should run the Print Queued Letters option to print the letters.
After the ‘Edit a Notification’ screen the program will ask, ‘Do you wish to edit this patient’s case data?’. Answer ‘Yes’ if you wish to update the patient’s case data at this point. (See the Edit/Print Patient Case Data option in this chapter.)
<span id="WV_124_WHO_CONTACTED_add_new_notif" class="anchor"></span>Who Contacted:
This is the person that was contacted with the patient results. This field should only be updated when the person is contacted via a phone call or in person.
<span id="WV_124_CONTACTED_DATE_add_new_notif" class="anchor"></span>Contacted Date:
This is the date the WHO CONTACTED is made via Phone Call or Person.
WV EDIT NOTIFICATION

#### Edit a Notification

[^60]This option allows you to edit a notification that already exists. You are first asked to select a patient (by name or SSN), and then a notification (by date or accession#). Once you have selected a notification to edit, the ‘Edit a Notification’ screen will appear. You may select another notification to edit before returning to the menu. Notification data is stored in the WV Notification (#790.4) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^61]Eligibility Code:
This field contains the eligibility code of the patient.
[^62]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
Date Notification Opened (Required):
The date the notification was first created.
Facility (Required):
Select the health care facility with which this letter is associated. Each letter to be printed is associated with a specific facility. When a user runs the Print Queued Letters option, only letters associated with the user’s facility will be printed. (The user’s facility is the facility (also called ‘Site’ or ‘Division’) that the user selects at sign on. If a user has only one facility, that facility is assigned automatically. For more information about selecting facilities at sign on, contact your site manager.) This feature allows multiple clinics to manage patients and print letters on the same computer, using the same patient database, without printing one another’s letters.
Purpose of Notification (Required):
This field contains the reason for the notification (e.g., the results of a test, reminder to schedule a procedure). This should be brief but descriptive enough to identify it uniquely. NOTE: This field cannot be changed because previous notifications from this purpose would become inaccurate. If the Purpose field is incorrect, make this purpose ‘Inactive’ (see next field), and then create a new purpose of notification with the correct purpose name.
Priority:
Filled in automatically, based on the purpose of notification.
Outcome:
This field stores the results or outcome, which may be a goal or an event, associated with this patient’s notification.
Type of Notification:
This field stores the method used to notify the patient from the choices available in the WV Notification Type (#790.403) file (e.g., letter, phone call, message, etc.).
Print Date:
Date letter is to be printed. Once the letter has a ‘Print Date’, it will print out on that date (or on any later date) when the option Print Queued Letters is run. For example, if the letter is queued to print on Friday but Print Queued Letters is not run until the following Monday, then the letter will print out with the Monday batch.
The default date that appears is based on whether the letter is a results letter or a reminder letter. If it is a results letter, the default date is ‘Today’. If it is a reminder letter, the default date is based on the due date of the treatment need (breast or gynecologic) to which this purpose of notification relates. (See the Add/Edit a Notification Purpose & Letter option.)
Complete by (Date):
This field contains the date used to determine that this procedure record is delinquent when a close status has not been entered in the record.
Printed:
Filled in automatically when the letter (if the notification is a letter) is printed.
Status:
<span id="Entered_in_Error_5" class="anchor"></span>Select either ‘Open’, ‘Closed’ or ‘Enter in Error’. A notification is usually left ‘Open’ until an outcome has been entered. If the notification is a results letter, it is usually closed when the letter is printed (no further outcome is expected). If the notification is a reminder letter (reminding the patient to call for a next appointment), it is usually closed either when the patient calls to schedule an appointment, or following the edit of her next procedure. (See ‘The Basic Patient Management Loop’). A notification that is left ‘Open’ past its ‘Complete by (Date)’ will be displayed as ‘Delinquent’ on notification reports.
Patient Education:
Enter ‘Yes’ or ‘No’, depending on whether patient education occurred during the notification (for phone calls, conversations, etc.).
> **NOTE:** If the notification is a letter and the letter has already been printed, most of the fields for that notification will be blocked from editing. This is to keep the data on the computer in sync with the letter that was sent to the patient. Only the bottom four fields (Complete by Date, Outcome, Status, and Patient Ed) will be editable.
After you leave the ‘Edit a Notification’ screen, if you did not save before exiting you will be asked ‘Save changes before leaving form (Y/N)?’, and if the notification was a letter, the program will ask, ‘Do you wish to preview or print this letter now? Enter Yes or No: NO//’. ‘Preview’ allows you to look at the letter that has just been queued. To preview the letter, select ‘Home’ at the ‘Device: ‘ prompt. ‘Print’ will print the letter immediately, regardless of its ‘Print Date’, and remove it from the queue of letters waiting to print. To print the letter immediately, select a printer at the ‘Device: ‘ prompt.
If you answer ‘No’ to the ‘Do you wish to preview or print this letter now?’ prompt, the letter will remain in the queue, to be printed on its ‘Print Date’. NOTE: These letters do not print automatically, the user should run the Print Queued Letters option to print the letters.
After the ‘Edit a Notification’ screen the program will ask, ‘Do you wish to edit this patient’s case data?’. Answer ‘Yes’ if you wish to update the patient’s case data at this point. (See the Edit/Print Patient Case Data option in this chapter.)
<span id="WV_124_WHO_CONTACTED_edit_notif" class="anchor"></span>Who Contacted:
This is the person that was contacted with the patient results. This field should only be updated when the person is contacted via a phone call or in person.
<span id="WV_124_CONTACTED_DATE_edit_notif" class="anchor"></span>Contacted Date:  
WV BROWSE NOTIFICATIONSBrowse Notifications
This option allows you to search for and browse through notifications. The six questions that are asked prior to the display allow you to specify patients, date range, status, case manager (site parameter), order of display, and device for the printout.
If the device selected for the ‘Browse Notifications’ display is ‘Home’ (to the screen), a column of numbers will appear to the left of the notifications. Notification data is stored in the WV Notification (#790.4) file.
Report Description:SSN:
This field contains the social security number of the patient.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Date:
This field contains the date the procedure was performed.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Status:
This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
Priority:
This field associates a priority with the notification. The priority choices are: urgent, ASAP, and routine.
WV PRINT INDIVIDUAL LETTERS

#### Print Individual Letters

This option allows you to print individual letters. You are first asked to select a patient (by name or SSN), then a notification (by date or accession#), and then a printer device. The letter will print immediately (unless you queue it again), regardless of its ‘Print Date’, and then it will be removed from the queue of letters waiting to print. Letters are printed as needed by merging notification data (File \#790.4) with a notification form letter (File \#790.404).
[^63]This option will check for and use a patient's confidential address, if appropriate. The Registration package allows for a patient to specify a confidential address to be used for written correspondence. The patient specifies the confidential address to use, the timeframe that confidential address will be used, and one or more categories of written communications
that apply. Notification letters may contain appointment or medical results information. This type of information corresponds with APPOINTMENT/SCHEDULING and MEDICAL RECORDS (category 2 and 4 respectively) in the Registration package. If an active confidential address exists for the patient, and either category 2 or 4 is active, the confidential address is used. Otherwise, the current address is used.
WV PRINT QUEUED LETTERSPrint Queued Letters
This option allows you to print all letters that have been queued to print on the current date or on any date prior to the current date. Some of these letters may be reminder letters, put in the queue weeks or months earlier to print on this date, alerting the patient to call and schedule her next procedure (for example, an annual PAP). Others of these letters may be results letters queued earlier in the day to print today, informing the patient of results of a recent procedure. Only letters associated with your facility will be printed (see ‘Facility’). Letters are printed as needed by merging notification data (File \#790.4) with a notification form letter (File \#790.404).
> **NOTE:** The option to Print Queued Letters checks to see that the patient is not deceased. For a deceased patient, instead of the queued letter printing, an explanation is printed stating that the patient is deceased, that letter will not be printed, and that the notification has been closed and given an outcome of ‘Patient Deceased’. At this time, the user should edit the deceased patient’s case data and enter a date into the Inactive Date field. Refer to the Edit Patient Case Data explanation for additional information.
[^64]This option will check for and use a patient's confidential address, if appropriate. The Registration package allows for a patient to specify a confidential address to be used for written correspondence. The patient specifies the confidential address to use, the timeframe that confidential address will be used, and one or more categories of written communications
that apply. Notification letters may contain appointment or medical results information. This type of information corresponds with APPOINTMENT/SCHEDULING and MEDICAL RECORDS (category 2 and 4 respectively) in the Registration package. If an active confidential address exists for the patient, and either category 2 or 4 is active, the confidential address is used. Otherwise, the current address is used.

### Chapter 5 Management Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-MANAGEMENT REPORTSManagement Reports
The Management Reports Menu contains options that provide program management reports and a limited set of epidemiological reports. The remainder of this section will briefly describe each of the options under the Management Reports Menu.
Menu Display:
Select OPTION NAME: WV MENU-MANAGEMENT REPORTS Management Reports
WOMEN'S HEALTH: \* MANAGEMENT REPORTS \* HINES DEVELOPMENT
========================
PS Procedure Statistics Report
SN Snapshot of the Program Today
RS Retrieve/Print Earlier Snapshots
CR Compliance Rates for PAPs and MAMs
BP Browse Patients With Needs Past Due
[^65]ST Sexual Trauma Summary Report
[^66]LST List Sexual Trauma Data
WV PRINT PROCEDURE STATS

#### Procedure Statistics Report

[^67]This option provides a report on the different women’s health procedures performed at the facility. This report is sorted by facility. Data is broken down by veteran and non-veteran, and the numbers of procedures which have results of normal, abnormal, and no result. It also provides a count of patients who have had the respective procedures, whether or not they are veterans and if the results were normal, abnormal, or no result available. All results are also expressed as percentages. A list of any procedures that are not linked to a facility appears at the end of the report.
This report first asks you for a date range, the group of procedure types to be included, if you wish to display statistics by age group, facilities to be included in the report, and a device. If you answer ‘Yes’ to display by age group you will be instructed to enter the age ranges you wish to select for in the form of: 15-29,30-39,40-105. Use a dash ‘-’ to separate the limits of a range, use a comma to separate the different ranges. NOTE: Patient ages will reflect the age they were on the dates of their procedures. (Patient ages will NOT necessarily be their ages today.)
It is important to note that in the patient’s section for each procedure type, the total may be less than the sum of the three results categories (normal, abnormal, and no result). This is because any individual patient may be included in all three categories of normal, abnormal, and no result. A patient may have received more than one procedure during the date range selected, and those procedures may have had differing results. Each results category simply gives the number of patients who fell into that category for the date range selected. The total, however, gives the total number of patients who received that procedure type for the date range selected, the report counts each patient only once, no matter how many times she may have had the procedure. For this reason, the total for the patient’s section may be less than the sum of the three results categories. Procedure data is stored in the WV Procedure (#790.1) file.
Report Description:
The report displays a table sorted by procedure types and patients, listing the count, number of veterans and non-veterans, and the results of the procedures (normal, abnormal, and no result). Radiology credit (regular credit, no credit) is displayed for mammogram procedures.
WV PRINT SNAPSHOTSnapshot of the Program Today
This option provides a calendar or fiscal year-to-date report that gives program statistics at a glance. This report also includes total counts of treatment refusals by procedure name. Before displaying the report, the program asks: ‘Should today's Snapshot be stored for later retrieval and comparisons?’ If you answer ‘Yes’, the results of the current date’s snapshot will be stored after they have been printed out. These results can then be retrieved in the future (by selecting the date of the desired report) and compared to other snapshots in order to look at the trends and progress of your program over time. If you answer ‘No’, the program will simply print the current date’s snapshot without storing it. NOTE: If a previous snapshot for the current date has been run, it will be overwritten by any later run on the same date.
The next question asks you to Select Device:. Enter ‘Home’ to have the report display on the screen. Snapshot data is stored in the WV Snapshot Reports (#790.71) file.
> **NOTE:** A patient will not be processed if there is any value (past, present, or future) in the Date Inactive field.
Report Description:Total Active Women in Register:
This field contains the total number of women with active records in the WV Patient (#790) file.
Women Who Are Pregnant:
This field contains the number of women who were pregnant at the time the program snapshot report option was run.
Women with Cervical Tx Needs not specified or not dated:
[^68]This field contains the number of women whose records indicated that their gynecologic treatment needs were not specified or the due date was not recorded. A woman will not be counted if her cervical treatment need value is "Not Indicated".
Women with Cervical Tx Needs specified and past due:
This field contains the number of women whose records indicated that their gynecologic treatment needs were specified and are past due.
Women with Breast Tx Needs not specified or not dated:
[^69]This field contains the number of women whose records indicated that their breast treatment needs were not specified or the due date was not recorded. A woman will not be counted if her breast treatment need value is "Not Indicated".
Women with Breast Tx Needs specified and past due:
This field contains the number of women whose records indicated that their breast treatment needs were specified and are past due.
Total Number of Procedures with a Status of ‘OPEN’:
This field contains the number of procedure records that have a status of ‘Open’.
Number of OPEN Procedures Past Due (or not dated):
This field contains the number of procedure records (with an ‘Open’ status) which indicate that breast or gynecologic treatment needs are past due.
Total Number of PAP Smears done since Oct 1, 1997:
This field contains a count of the PAP smears done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of CBEs done since Oct 1, 1997:
This field contains a count of the clinical breast exams (CBE) done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of Mammograms done since Oct 1, 1997:
This field contains a count of the mammograms done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of Notifications with a Status of ‘OPEN’:
This field displays the number of notification records, with a status of ‘Open’, when the program snapshot report was run.
Number of OPEN Notifications Past Due (or not dated):
This field contains the number of notification records that were past due when the program snapshot report was run.
Number of Letters Queued (for later printing):
This field contains the number of letters scheduled to be queued at a future time. This count is calculated from the Type of Notification and the Print Date fields in the WV Notification (#790.4) file.
REFUSALS for TREATMENT:Breast Ultrasounds:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a breast ultrasound within the timeframe associated with the program snapshot report.
Clinical Breast Exams:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a clinical breast exam within the timeframe associated with the program snapshot report.
Colposcopy Impression (No Bx):
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, colposcopy impression, within the timeframe associated with the program snapshot report.
Colposcopy W/Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, colposcopy with biopsy, within the timeframe associated with the program snapshot report.
Cone Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, cone biopsy, within the timeframe associated with the program snapshot report.
Cryotherapy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, cryotherapy, within the timeframe associated with the program snapshot report.
Ectocervical Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, ectocervical biopsy, within the timeframe associated with the program snapshot report.
Endocervical Curettage:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, endocervical curettage, within the timeframe associated with the program snapshot report.
Endometrial Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, endometrial biopsy, within the timeframe associated with the program snapshot report.
Fine Needle Aspiration:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, fine needle aspiration, within the timeframe associated with the program snapshot report.
General Surgery Consults:
This field contains the number of records (in File \#790.3) indicating that a patient declined a general surgery consult referral within the timeframe associated with the program snapshot report.
Gyn Onc Consults:
This field contains the number of records (in File \#790.3) indicating that a patient declined a gynecological oncology consult referral within the timeframe associated with the program snapshot report.
Hysterectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a hysterectomy within the timeframe associated with the program snapshot report.
Laser Ablation:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a laser ablation procedure within the timeframe associated with the program snapshot report.
Laser Cone:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a laser cone procedure within the timeframe associated with the program snapshot report.
Leep:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a loop electrosurgical excision procedure (LEEP) within the timeframe associated with the program snapshot report.
Lumpectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a lumpectomy (of the breast) within the timeframe associated with the program snapshot report.
Mammogram Dx Bilat:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology test, mammogram DX bilateral, within the timeframe associated with the program snapshot report.
Mammogram Dx Unilat:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology test, mammogram DX unilateral, within the timeframe associated with the program snapshot report.
Mammogram Screening:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology procedure, mammogram screening, within the timeframe associated with the program snapshot report.
Mastectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a mastectomy within the timeframe associated with the program snapshot report.
Needle Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a needle biopsy within the timeframe associated with the program snapshot report.
Open Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having an open biopsy within the timeframe associated with the program snapshot report.
Pap Smear:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a pap smear within the timeframe associated with the program snapshot report.
Pregnancy Test:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a pregnancy test within the timeframe associated with the program snapshot report.
STD Evaluation:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a STD evaluation within the timeframe associated with the program snapshot report.
Stereotactic Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a stereotactic biopsy within the timeframe associated with the program snapshot report.
WV PRINT/RETRIEVE SNAPSHOT

#### Retrieve/Print Earlier Snapshots

This option allows you to display or print previous snapshot reports described in the previous option. At the ‘Select Snapshot: ‘ prompt, enter the date of the snapshot you wish to retrieve. Enter ‘?’ and press RETURN, to see a list of previous snapshots by date. Snapshot data is stored in the WV Snapshot Reports (#790.71) file.
Report Description:Total Active Women in Register:
This field contains the total number of women with active records in the WV Patient (#790) file.
Women Who Are Pregnant:
This field contains the number of women who were pregnant at the time the program snapshot report option was run.
Women with Cervical Tx Needs not specified or not dated:
This field contains the number of women whose records indicated that their gynecologic treatment needs were not specified or the due date was not recorded.
Women with Cervical Tx Needs specified and past due:
This field contains the number of women whose records indicated that their gynecologic treatment needs were specified and are past due.
Women with Breast Tx Needs not specified or not dated:
This field contains the number of women whose records indicated that their breast treatment needs were not specified or the due date was not recorded.
Women with Breast Tx Needs specified and past due:
This field contains the number of women whose records indicated that their breast treatment needs were specified and are past due.
Total Number of Procedures with a Status of ‘OPEN’:
This field contains the number of procedure records that have a status of ‘Open’.
Number of OPEN Procedures Past Due (or not dated):
This field contains the number of procedure records (with an ‘Open’ status) which indicate that breast or gynecologic treatment needs are past due.
Total Number of PAP Smears done since Oct 1, 1997:
This field contains a count of the PAP smears done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of CBEs done since Oct 1, 1997:
This field contains a count of the clinical breast exams (CBE) done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of Mammograms done since Oct 1, 1997:
This field contains a count of the mammograms done since the beginning of the calendar or fiscal year, depending upon what the user selected. NOTE: The date will either be Oct. 1 or Jan. 1 depending on whether the user chose fiscal or calendar year.
Total Number of Notifications with a Status of ‘OPEN’:
This field displays the number of notification records, with a status of ‘Open’, when the program snapshot report was run.
Number of OPEN Notifications Past Due (or not dated):
This field contains the number of notification records that were past due when the program snapshot report was run.
Number of Letters Queued (for later printing):
This field contains the number of letters scheduled to be queued at a future time. This count is calculated from the Type of Notification and the Print Date fields in the WV Notification (#790.4) file.
REFUSALS for TREATMENT:Breast Ultrasounds:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a breast ultrasound within the timeframe associated with the program snapshot report.
Clinical Breast Exams:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a clinical breast exam within the timeframe associated with the program snapshot report.
Colposcopy Impression (No Bx):
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, colposcopy impression, within the timeframe associated with the program snapshot report.
Colposcopy W/Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, colposcopy with biopsy, within the timeframe associated with the program snapshot report.
Cone Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, cone biopsy, within the timeframe associated with the program snapshot report.
Cryotherapy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, cryotherapy, within the timeframe associated with the program snapshot report.
Ectocervical Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, ectocervical biopsy, within the timeframe associated with the program snapshot report.
Endocervical Currettage:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, endocervical curettage, within the timeframe associated with the program snapshot report.
Endometrial Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, endometrial biopsy, within the timeframe associated with the program snapshot report.
Fine Needle Aspiration:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the procedure, fine needle aspiration, within the timeframe associated with the program snapshot report.
General Surgery Consults:
This field contains the number of records (in File \#790.3) indicating that a patient declined a general surgery consult referral within the timeframe associated with the program snapshot report.
Gyn Onc Consults:
This field contains the number of records (in File \#790.3) indicating that a patient declined a gynecological oncology consult referral within the timeframe associated with the program snapshot report.
Hysterectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a hysterectomy within the timeframe associated with the program snapshot report.
Laser Ablation:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a laser ablation procedure within the timeframe associated with the program snapshot report.
Laser Cone:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a laser cone procedure within the timeframe associated with the program snapshot report.
Leep:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a loop electrosurgical excision procedure (LEEP) within the timeframe associated with the program snapshot report.
Lumpectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a lumpectomy (of the breast) within the timeframe associated with the program snapshot report.
Mammogram Dx Bilat:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology test, mammogram DX bilateral, within the timeframe associated with the program snapshot report.
Mammogram Dx Unilat:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology test, mammogram DX unilateral, within the timeframe associated with the program snapshot report.
Mammogram Screening:
This field contains the number of records (in File \#790.3) indicating that a patient declined having the radiology procedure, mammogram screening, within the timeframe associated with the program snapshot report.
Mastectomy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a mastectomy within the timeframe associated with the program snapshot report.
Needle Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a needle biopsy within the timeframe associated with the program snapshot report.
Open Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having an open biopsy within the timeframe associated with the program snapshot report.
Pap Smear:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a pap smear within the timeframe associated with the program snapshot report.
Pregnancy Test:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a pregnancy test within the timeframe associated with the program snapshot report.
STD Evaluation:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a STD evaluation within the timeframe associated with the program snapshot report.
Stereotactic Biopsy:
This field contains the number of records (in File \#790.3) indicating that a patient declined having a stereotactic biopsy within the timeframe associated with the program snapshot report.
WV PRINT COMPLIANCE RATESCompliance Rates for PAPs and MAMs
[^70]This report is designed to serve as an indicator of compliance rates for PAP smears (PAPs) and mammograms (MAMs), in other words, it indicates the percentage of women who are returning to the program on a regular basis (e.g., annually) for screenings. This report calculates the percentages based on the number of patients who are considered active in the Women's Health package for the date range selected. This report asks you for a date range, an age group, and a device.
This report can be run for a larger time frame, for example, 5 years, in order to obtain a broader sampling. If the report was run to cover a 5 year time frame, one would hope to see the highest percentages in the 5 column (assuming the goal is to have women return annually). The report can also be run several times for shorter time periods and the results compared, in order to examine trends.
This report serves only as an indicator (NOT as an exact count of compliance rates) for gauging the success rates of annual screening programs. It can be run for several different timeframes in order to examine trends. Assuming a screening cycle of one year, a minimum date range spanning 15 months is recommended. Compliance data is stored in the WV Patient (#790) file.
Report Description:
[^71]The report displays the percentages of women who received PAPs and MAMs for screening purposes only, within the selected date range, along with the number of active patients. The output will include a breakdown by current PAP regimen.
Only patients who have had normal results for procedures in the specified date range are counted; the intent is to exclude any procedures that would involve abnormal results, diagnostic and follow-up procedures, etc. Due to the complexities involved in the treatment of individual cases that involve abnormal results, those patients will not be included, even though some of them may have received screening PAPs or MAMs.
WV BROWSE NEEDS PAST DUE

#### Browse Patients With Needs Past Due

This option is exactly the same as is found under the Patient Management Menu.
WV SEXUAL TRAUMA SUMMARY
[^72]Sexual Trauma Summary Report
This option provides the user with a short report of the number of WH patients who have experienced sexual trauma in the military, as a civilian, or both. Civilian sexual trauma data is stored in the WV Patient (#790) file. Military sexual trauma data is stored in the MST History (#29.11) file.
> **NOTE:** Patients who are deceased are not counted in this report.
Report Description:
This report can include Women’s Health patients for one case manager or all case managers.
For each sexual trauma type (military or civilian), a table sorted by number of Veterans and Non-Veterans is displayed. These tables indicate the number of WH patients who have experienced sexual trauma in the military, as a civilian, or both.
[^73]WV SEXUAL TRAUMA LISTList Sexual Trauma Data
[^74]This option displays a list of patients, their Civilian Sexual Trauma value from the WH package and the Military Sexual Trauma (MST) value from the MST module of the Registration package. The patient's name, SSN, case manager, age, veteran status and eligibility code are displayed, too.
Patients are sorted by case manager first, then MST status and finally patient name. The MST status order is:
1\) Yes, Screened reports MST
2\) No, Screened does not report MST
3\) Screened Declines to answer
4\) Unknown, not screened
Non-veteran patients are displayed after the veterans.
The user may choose to see the patients for one case manager or all case managers. Patients who are deceased or have an Inactive Date (prior to today's date) will not appear on the listing.
Report Description:SSN:
This field contains the social security number of the patient.
Patient:
This field contains the name of the patient. Pointer to the WV Patient (#790) file.
Case Manager:
This field contains the name of a WH case manager who is currently managing the women’s health care needs of this patient.
[^75]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
Primary Care Provider:
This field contains the name of the primary provider who is responsible for the women’s health care needs of this patient.
Age:
This field contains the age of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
Eligibility Code:
This field contains the eligibility code of the patient.
<span id="_Toc117589099" class="anchor"></span>

### Chapter 6 Manager's Functions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-MANAGER’S FUNCTIONSManager's Functions
The Manager’s Functions Menu contains options that provide the ADPAC with a set of utilities for configuring the software to the specific needs of the site at which the Women’s Health software is being used. It also provides utilities for other program needs, such as customizing letters, and making special edits to patient data.
The Manager’s Functions menu contains many sensitive options requiring a thorough understanding of the software. The remainder of this section will briefly describe each of the options under the Manager’s Functions Menu.
Menu Display:
Select OPTION NAME: WV MENU-MANAGER'S FUNCTIONS Manager's Functions
WOMEN'S HEALTH: \* MANAGER'S FUNCTIONS \* HINES DEVELOPMENT
=========================
FM File Maintenance Menu ...
PQ Print Queued Letters
MPM Manager's Patient Management ...
LDE Lab Data Entry Menu ...
WV MENU-FILE MAINTENANCE

#### File Maintenance Menu

The File Maintenance Menu is described in detail under Chapter 2. Please refer to that section for a complete description of the options under this menu.
Menu Display:
Select Manager’s Functions Option: FM File Maintenance Menu
WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* HINES DEVELOPMENT
===========================
AEP Add/Edit a Notification Purpose & Letter
PPL Print Notification Purpose & Letter File
ESN Edit Synonyms for Notification Types
OUT Add/Edit Notification Outcomes
ESP Edit Site Parameters  
<span id="EPP_3" class="anchor"></span>EPP Edit Package Parameters
CM Add/Edit Case Managers
MCC Add/Edit Maternity Care Coordinators
TRCM Transfer a Case Manager's Patients
TRMC Transfer a Maternity Care Coordinator's Patients
AUTO Automatically Load Patients
RAD Import Radiology/NM Exams
PRD Print Results/Diagnosis File
ESR Edit Synonyms for Results/Diagnoses
PSR Print Synonyms for Results/Diagnoses
EDX Edit Diagnostic Code Translation File
PDX Print Diagnostic Code Translation File
RS Add/Edit to Referral Source File
PAP Link Pap Smear with SNOMED Codes
> **NOTE:** The option Add Sexual Trauma Data to MST Module was added to this menu by patch WV\*1\*11 in June 2000, and then this option was removed by patch WV\*1\*14 in April 2001.
WV PRINT QUEUED LETTERSPrint Queued Letters
This option is exactly the same as is found under the Patient Management Menu.
WV MENU-MGR PATIENT MGTManager ‘s Patient Management
This is a menu of options that allow the ADPAC or case manager to view and edit certain types of patient and procedure data in greater detail.
Menu Display:
Select Manager’s Functions Option: MPM Manager's Patient Management
WOMEN'S HEALTH: \* MANAGER'S PATIENT MANAGEMENT \* HINES DEVELOPMENT
==================================
PPE Patient Profile Including Errors
PC Edit/Print Patient Case Data
HIS Add an HISTORICAL Procedure
DUP Browse Procedures for Possible Duplicates
PAL Edit PAP Regimen Log
PRL Edit Pregnancy/Lactation Status Data
WV MENU-LAB DATA ENTRYLab Data Entry Menu
This is a menu of options that allow the Lab users to enter/edit and display lab data.
Menu Display:
Select Manager’s Functions Option: LDE Lab Data Entry Menu
WOMEN'S HEALTH: \* LAB DATA ENTRY \* HINES DEVELOPMENT
====================
AP Add(Accession) a NEW Procedure
EA Edit Accessioned Procedure
PR Print a Procedure
LOG Display/Print Daily Log
<span id="_Toc117589100" class="anchor"></span>

### Chapter 7 Manager’s Patient Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-MGR PATIENT MGTManager’s Patient Management
This is a menu of options that allow the ADPAC to view and edit certain types of patient and procedure data in greater detail.
Menu Display:
Select OPTION NAME: WV MENU-MGR PATIENT MGT Manager's Patient Management
WOMEN'S HEALTH: \* MANAGER'S PATIENT MANAGEMENT \* HINES DEVELOPMENT
==================================
PPE Patient Profile Including Errors
PC Edit/Print Patient Case Data
HIS Add an HISTORICAL Procedure
DUP Browse Procedures for Possible Duplicates
PAL Edit PAP Regimen Log
PRL Edit Pregnancy/Lactation Status Data
WV PATIENT PROFILE W/ERRORSPatient Profile Including Errors
Displays the Patient Profile exactly as described under Patient Profile; however, it also includes those procedures given a results/diagnosis of ‘Error/disregard’. This is the only option in the software that the displays procedures entered in error.
WV EDIT PATIENT CASE DATA

#### Edit/Print Patient Case Data

This option is exactly the same as is found under the Patient Management Menu.
WV ADD AN HISTORICAL PROCEDURE

#### Add an HISTORICAL Procedure

This option is exactly the same as is found under the Patient Management Menu.
WV BROWSE PROCEDURES DUPLICATE

#### Browse Procedures for Possible Duplicates

This utility checks for possible duplicate procedures, in other words, two or more instances of the same procedure for a given patient on the same date. If the selected device for output is ‘Home’, the program displays the duplicate procedures with a column of numbers to the left of the SSN. Procedure data is stored in the WV Procedure (#790.1) file.
Report Description:SSN:
This field contains the social security number of the patient.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Date:
This field contains the date the procedure was performed.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Status:
This field contains the record’s status (set of codes: O = Open, C = Closed, D = Delinquent) for the procedure. The value of this field is used in the Program Snapshot reports and the Browse Patients with Needs Past Due report.
Results/Diagnosis:
This field displays the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for PAP smears are based on the Bethesda Classification system; those for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
WV EDIT PAP REGIMEN LOG

#### Edit PAP Regimen Log

Any changes made to a patient’s PAP regimen on the ‘Edit Patient Case Data’ screen are logged automatically and are displayed on the Patient Profile report. If a log entry is in error, it can be edited by the ADPAC or case manager using this option. PAP regimen log data is stored in the WV PAP Regimen Log (#790.04) file.
> **WARNING:** If you edit the ‘Begin Date:’ of an entry in the PAP regimen log, be sure that another entry with the same ‘Begin Date:’ does not already exist for this patient. Ordinarily, the program checks this and will not allow two separate entries for the same patient on the same ‘Begin Date:’. But under this option you, as the manager, have greater edit capability.
Field Descriptions:Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Begin Date:
This field contains the begin date for the PAP regimen.
PAP Regimen:
Select the PAP regimen that was given to this patient at the date and time of this entry.
WV EDIT PREG/LAC STATUS DATA

#### Edit Pregnancy/Lactation Status Data

Any changes made to a patient’s pregnancy or lactation status through the Computerized Patient Record System (CPRS) are logged automatically and are displayed on the Patient Profile report. If a log entry is in error, it can be marked entered in error by the ADPAC or case manager using this option. Pregnancy log data is stored in the WV Pregnancy Log (#790.05) file.
Field Descriptions:Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
Pregnancy State:
This field contains information on the pregnancy state of the patient. The state is a set of codes: 1 = Yes if this patient is currently pregnant, 0 = No, if not, and 2 = Do not know.
EDD:
This field stores the patient’s estimated delivery date (EDD).
Lactation State:
This field contains information on the lactation state of the patient. The state is a set of codes: 1 = Yes if this patient is currently lactating, 0 = No, if not.
<span id="_Toc345153450" class="anchor"></span>

### Chapter 8 Lab Data Entry Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV MENU-LAB DATA ENTRYLab Data Entry Menu
This menu is used by laboratory personnel to add, edit and view procedures in the Women’s Health database.
Menu Display:
Select OPTION NAME: WV MENU-LAB DATA ENTRY Lab Data Entry Menu
WOMEN'S HEALTH: \* LAB DATA ENTRY \* HINES DEVELOPMENT
====================
AP Add(Accession) a NEW Procedure
EA Edit Accessioned Procedure
EP Edit a Procedure Result
PR Print a Procedure
LOG Display/Print Daily Log
WV LAB ADD A NEW PROCEDUREAdd(Accession) a NEW Procedure
This option is used by laboratory personnel to add procedures to the Women’s Health database. Procedure data is stored in the WV Procedure (#790.1) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^76]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
[^77]Eligibility Code:
This field contains the eligibility code of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date of Procedure (Required):
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
Clinician/Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed. NOTE: If the entry in the Hospital Location (#44) file has the Institution (#3) field filled in, the institution will be provided as the default for the field Health Care Facility.
Health Care Facility (Required):
This field identifies the name of the health care facility where this procedure was performed.
WV LAB EDIT ACCESSION

#### Edit Accessioned Procedure

This option is used by laboratory personnel to edit procedures in the Women’s Health database. Procedure data is stored in the WV Procedure (#790.1) file.
Field Descriptions:
These fields appear above the dashed line on every screen. These fields are not editable through this option. They may be edited through Edit/Print Patient Case Data option (except patient name and SSN).
Patient Name:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Case Manager:
This field contains the name of a WH case manager assigned to manage this women’s health needs.
Procedure:
This field stores the name of the procedure performed on the patient. Pointer to the WV Procedure (#790.1) file.
PAP Regimen:
This field contains the PAP regimen that was given to this patient at the date and time of this entry.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Cervical Treatment Need:
This field contains the name of the current or next gynecologic procedure or treatment need scheduled for this patient.
Cervical Treatment Facility:
This field contains the name of the facility responsible for providing the gynecological tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
Breast Treatment Need:
This field contains the name of the current or next breast study procedure needed for this patient.
Breast Treatment Facility:
This field contains the name of the facility responsible for providing the breast study tests/exams for this patient. Facility choices are limited to entries in the Institution (#4) file.
[^78]MST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) in the military. Set of codes: (Y = Yes, Screened reports MST; N = No, Screened does not report MST; D = Screened Declines to answer; U = Unknown, not screened).
“\<N/A Not a Veteran\>” is displayed for non-veterans.
CST:
This field indicates if the patient has experienced any sexual trauma (rape, sexual assault, etc.) as a civilian. Set of codes: (Y = Yes, N = No, D = Declined to Answer, U = Unknown).
[^79]Eligibility Code:
This field contains the eligibility code of the patient.
Veteran:
This field contains a ‘Yes’ if the patient is a veteran, ‘No’ if the patient is not a veteran, or is blank if the veteran status of this patient is not known.
These fields appear below the dashed line:
Date of Procedure (Required):
This field identifies the date on which the procedure was performed. Dates in the future may not be entered.
Clinician/Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
Ward/Clinic/Location:
This field contains the name of the ward, clinic, or location where the procedure was performed. NOTE: If the entry in the Hospital Location (#44) file has the Institution (#3) field filled in, the institution will be provided as the default for the field Health Care Facility.
Health Care Facility (Required):
This field identifies the name of the health care facility where this procedure was performed.
WV EDIT PROCEDURE

#### Edit a Procedure Result

This option is exactly the same as the Edit a Procedure option found under the Patient Management Menu.
WV PRINT A PROCEDURE

#### Print a Procedure

This option is exactly the same as is found under the Patient Management Menu.
WV LAB PRINT LOG

#### Display/Print Daily Log

This option displays a list and/or a total count of procedures recorded in the WV Procedure (#790.1) file.
The report output is based on criteria selected by the user including date range, type of procedure, facility, and procedures with no result/diagnosis or procedures with and without a result/diagnosis. The user may sort the list of procedures by accession number or patient name, or display a totals count only.
Report Description:
If a detailed report for each procedure is selected, the following information is displayed:
Date:
This field contains the date the procedure was entered into the database, or the date the procedure record was created.
Accession#:
This is the record number assigned by the Women's Health package. It is composed of the procedure's abbreviated code, a four digit year and a sequential number.
Patient:
This field contains the name of the patient associated with the procedure. Pointer to the WV Patient (#790) file.
SSN:
This field contains the social security number of the patient.
Location:
This field contains the current ward location on which this patient is residing.
Provider:
This field stores the name of the clinician who ordered and/or performed this procedure.
Date the Procedure was performed:
This field indicates the date the procedure was performed.
Entered by:
This field indicates the name of the person who entered data on this procedure.
Results/Diagnosis:
This field stores the main result or diagnosis of the patient's procedure. Pointer to the WV Results/Diagnosis (#790.31) file. The diagnosis or results for mammograms use the American College of Radiology classification. Entries should not be locally edited. A list of the possible results/diagnosis for each procedure type is found in Appendix A.
Total Procedures:
This field indicates the total number of procedures performed.
Procedures without results:
This field indicates the number of procedures performed with no results.

### Appendix A - Results/Diagnosis File by Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^80]\* WOMEN'S HEALTH: LISTING OF RESULTS/DIAGNOSIS FILE \*PAGE 1
\* BY PROCEDURE \*
Run Date: OCT 04, 1999 15:21
--------------------------------------------------------------------------------
PROCEDURE RESULT/DIAGNOSIS PRIORITY NORMAL
--------------------------------------------------------------------------------
BREAST ULTRASOUND Cystic Mass, Complicated 1 ABNORM
Solid Mass, Irregular Margins 1 ABNORM
Solid Mass, Smooth Margins 1 ABNORM
Cystic Mass 5 ABNORM
No Discrete Mass 90 NORMAL
Error/disregard 95 NO RES
CLINICAL BREAST EXAM Abnormal/other 1 ABNORM
Bloody Nipple Discharge 1 ABNORM
Discrete Mass 1 ABNORM
Nipple/Areolar Scaliness 1 ABNORM
Retraction/Dimpling 1 ABNORM
Benign Findings 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
COLPOSCOPY IMPRESSION (NO BX) Impression: Invasive CA 1 ABNORM
Pregnant(no bx),Imp:Invasive 1 ABNORM
Impression: CIN II 2 ABNORM
Impression: CIN III 2 ABNORM
Impression: VAIN II 2 ABNORM
Impression: VAIN III 2 ABNORM
Impression: VIN II 2 ABNORM
Impression: VIN III 2 ABNORM
Pregnant(no bx),Imp:CIN II 2 ABNORM
Pregnant(no bx),Imp:CIN III 2 ABNORM
Impression: CIN I 3 ABNORM
Impression: HPV 3 ABNORM
Impression: VAIN I 3 ABNORM
Impression: VIN I 3 ABNORM
Pregnant(no bx),Imp:CIN I 3 ABNORM
Pregnant(no bx),Imp:HPV 3 ABNORM
Impression: Inflammation 5 ABNORM
Pregnant(no bx),Imp:Inflam 6 NORMAL
Impression: WNL/Normal 90 NORMAL
Not Available 90 NO RES
Pregnant(no bx),Imp:WNL 90 NORMAL
Error/disregard 95 NO RES
COLPOSCOPY W/BIOPSY Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
VAIN II 2 ABNORM
VAIN III 2 ABNORM
VIN II 2 ABNORM
VIN III 2 ABNORM
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
VAIN I 3 ABNORM
VIN I 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
CONE BIOPSY Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
Other Malignant Neoplasms 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
CRYOTHERAPY Done 92 NO RES
Error/disregard 95 NO RES
ECTOCERVICAL BIOPSY Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
Not Done 99 NO RES
ENDOCERVICAL CURRETTAGE Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
ENDOMETRIAL BIOPSY Carcinoma, Non-invasive 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
Adenomatous Hyperplas w/Atypia 2 ABNORM
Adenomatous Hyperplas w/o Atyp 3 ABNORM
Endometritis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
FINE NEEDLE ASPIRATION Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
GENERAL SURGERY CONSULT Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Not Available 90 NO RES
Error/disregard 95 NO RES
GYN ONC CONSULT See Patient Chart/Record 10 NO RES
Error/disregard 95 NO RES
HYSTERECTOMY Adenoacanthoma 1 ABNORM
Adenomyosis 1 ABNORM
CA endometrium Stage I 1 ABNORM
CA endometrium Stage II 1 ABNORM
CA endometrium Stage III 1 ABNORM
CA endometrium Stage IV 1 ABNORM
Carcinoma-in-situ 1 ABNORM
Cellular Leiomyoma 1 ABNORM
Choriocarcinoma 1 ABNORM
Chronic Pelvic Pain 1 ABNORM
Congential abn of uterus NOS 1 ABNORM
Cysto-urethrocele 1 ABNORM
Cystocele 1 ABNORM
Dysfunctional Uterine Bleeding 1 ABNORM
Dysmenorrhea, intractable NOS 1 ABNORM
Endometrial hyperplasia (rec) 1 ABNORM
Endometriosis 1 ABNORM
Enterocele 1 ABNORM
Fibro Sarcoma 1 ABNORM
Fibroids 1 ABNORM
Generalized pelvic relaxation 1 ABNORM
Hematometrium 1 ABNORM
Hydatidiform mole 1 ABNORM
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
Other 1 ABNORM
Other Malignant Neoplasms 1 ABNORM
Ovarian CA NOS 1 ABNORM
Placenta accreta 1 ABNORM
Pregnancy - cornual 1 ABNORM
Procidentia 1 ABNORM
Prolapse grade II 1 ABNORM
Prolapse grade III 1 ABNORM
Pyosalpinx 1 ABNORM
Rectocele 1 ABNORM
Salpingitis isthmica nodosa 1 ABNORM
Tubal CA NOS 1 ABNORM
Tubo-ovarian abscess 1 ABNORM
Uterine anomaly 1 ABNORM
Uterine foreign body 1 ABNORM
Uterine injury-external 1 ABNORM
Uterine injury-surgical 1 ABNORM
Uterine tuberculosis 1 ABNORM
Adenomatous Hyperplas w/Atypia 2 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
CIN I/mild dysplasia 3 ABNORM
Endometritis 5 ABNORM
Inflammation/Cervicitis 5 ABNORM
Error/disregard 95 NO RES
LASER ABLATION Done 92 NO RES
Error/disregard 95 NO RES
LASER CONE Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
Other Malignant Neoplasms 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
LEEP Insufficient Tissue 1 NO RES
Invasive CA: Cervical 1 ABNORM
Invasive CA: Other (non-cerv) 1 ABNORM
Other Malignant Neoplasms 1 ABNORM
CIN II/moderate dysplasia 2 ABNORM
CIN III/severe dysplasia 2 ABNORM
Unsatisfactory for Dx 2 NO RES
CIN I/mild dysplasia 3 ABNORM
HPV/condyloma 3 ABNORM
Inflammation/Cervicitis 5 ABNORM
Benign Changes 6 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
LUMPECTOMY Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
MAMMOGRAM DX BILAT Highly Sug of Malig, Tk Action 1 ABNORM
Suspicious Abnorm, Consider Bx 1 ABNORM
Assessment Is Incomplete 2 NO RES
Unsatisfactory for Dx 2 NO RES
Prbly Benign, Short Int F/U 4 ABNORM
Benign Finding, Negative 5 NORMAL
Indicated, But Not Performed 5 NO RES
Not Indicated 50 NO RES
Negative 90 NORMAL
Error/disregard 95 NO RES
MAMMOGRAM DX UNILAT Highly Sug of Malig, Tk Action 1 ABNORM
Suspicious Abnorm, Consider Bx 1 ABNORM
Assessment Is Incomplete 2 NO RES
Unsatisfactory for Dx 2 NO RES
Prbly Benign, Short Int F/U 4 ABNORM
Benign Finding, Negative 5 NORMAL
Indicated, But Not Performed 5 NO RES
Not Indicated 50 NO RES
Negative 90 NORMAL
Error/disregard 95 NO RES
MAMMOGRAM SCREENING Highly Sug of Malig, Tk Action 1 ABNORM
Suspicious Abnorm, Consider Bx 1 ABNORM
Assessment Is Incomplete 2 NO RES
Unsatisfactory for Dx 2 NO RES
Prbly Benign, Short Int F/U 4 ABNORM
Benign Finding, Negative 5 NORMAL
Indicated, But Not Performed 5 NO RES
Not Indicated 50 NO RES
Negative 90 NORMAL
Error/disregard 95 NO RES
MASTECTOMY Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
NEEDLE BIOPSY Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
OPEN BIOPSY Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
PAP SMEAR AGCUS 1 ABNORM
AGCUS, malignant 1 ABNORM
AGCUS, premalignant 1 ABNORM
ASCUS 1 ABNORM
ASCUS, malignant 1 ABNORM
ASCUS, premalignant 1 ABNORM
Invasive CA: Cervical 1 ABNORM
Other Malignant Neoplasms 1 ABNORM
Squamous Cell Carcinoma 1 ABNORM
Abnormal Appearing Cervix 2 ABNORM
HGSIL: CIS/CINIII/CINII 2 ABNORM
Unsatisfactory for Dx 2 NO RES
LGSIL: CINI/HPV 3 ABNORM
Benign Endometrial Cells 4 ABNORM
Benign Cell Chgs: Infection 5 ABNORM
Benign Cell Chgs: Other 5 NORMAL
Benign Cell Chgs: react/IUD 5 NORMAL
Benign Cell Chgs: react/atrphy 5 NORMAL
Benign Cell Chgs: react/inflam 5 NORMAL
Benign Cell Chgs: react/other 5 NORMAL
Benign Cell Chgs: react/radiat 5 ABNORM
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
PELVIC ULTRASOUND Done 92 NO RES
Error/disregard 95 NO RES
PREGNANCY TEST Positive 6 ABNORM
Negative 90 NORMAL
Error/disregard 95 NO RES
STD EVALUATION 2 or more STD's 5 ABNORM
3 or more STD's 5 ABNORM
Chlamydia 5 ABNORM
Gonorrhea 5 ABNORM
HIV 5 ABNORM
Herpes 5 ABNORM
Syphilis 5 ABNORM
Trichomoniasis 5 ABNORM
Positive 6 ABNORM
Negative 90 NORMAL
Not Available 90 NO RES
WNL/Normal 90 NORMAL
Error/disregard 95 NO RES
Not Done 99 NO RES
STEREOTACTIC BIOPSY Carcinoma-in-situ 1 ABNORM
Carcinoma-in-situ, NED 1 ABNORM
Carcinoma-in-situ, recurrent 1 ABNORM
Insufficient Tissue 1 NO RES
Invasive Ca 1 ABNORM
Invasive Ca, NED 1 ABNORM
Invasive Ca, progressive 1 ABNORM
Invasive Ca, responding Rx 1 ABNORM
Invasive Ca, stable 1 ABNORM
Atypia 5 ABNORM
Inflammation 5 ABNORM
Benign Findings 6 NORMAL
Error/disregard 95 NO RES
TUBAL LIGATION Done 92 NO RES
Error/disregard 95 NO RES
VAGINAL ULTRASOUND Done 92 NO RES
Error/disregard 95 NO RES
<span id="_Toc117589103" class="anchor"></span>

### Appendix B - Examples of Major Screen Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WV EDIT PATIENT CASE DATA

#### Edit/Print Patient Case Data

> \* \* \* EDIT PATIENT CASE DATA \* \* \*
> Patient Name: WVPATIENT,NINETEEN(24y/o) SSN: 666-01-0029
> Street: 123 Any St. Patient Phone: 000-400-3900
> Cty/St/Zip: ANYTOWN, STATE 30004-5049 Pr Provider: UNKNOWN
> Elig Code: NSC Veteran: Yes
> MST: Unknown, not screened
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> Case Manager: WHMANAGER,EIGHTUFF Inactive Date:
> Breast Tx Need: Undetermined Cervical Tx Need: Undetermined
> Breast Tx Due Date: Cervical Tx Due Date:
> Breast Tx Facility: Cervical Tx Facility:
> PAP Regimen: Undetermined CST:
> PAP Regimen Start Date: Notes (WP):
> Family Hx of Breast CA: DES Daughter:
> Maternity Care Coordinator:
> Date of 1st Encounter: JUN 00,2014 Referral Source:
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> COMMAND: E Press \<PF1\>H for help Insert
> Do you wish to PRINT this patient's Case Data?
> Enter Yes or No: NO//WV ADD A NEW PROCEDUREAdd a NEW Procedure
\* \* \* WOMEN'S HEALTH: ADD A NEW PROCEDURE \* \* \*
Select PATIENT NAME: WHPATIENT, ONE 00-00-49 000888888 YES SC VETERAN
Select PROCEDURE: PAP PROCEDURE// BIOPSY CO
Select DATE: TODAY// \<RET\> (00, 00, 1998) 00, 00, 1998
\* Move to PAGE 2 to edit clinical and pathology findings.
\* \* \* EDIT A PROCEDURE \* \* \*
Patient Name: WHPATIENT, ONE(xxy/o) SSN: 000-88-8888
Case Manager: WHMANAGER, ONE Procedure: BIOPSY
PAP Regimen : Pap regimen (began 00, 00,1998) Acc#: CO1998-0000
Cx Tx Need : Routine PAP (by 00, 00,1998) Cx Facility: Hines
Br Tx Need : Screening (by 00, 00,1998) Br Facility: Hines
[^81]Elig Code : SC LESS THAN 50% Veteran: YES
[^82]MST : No CST: Unknown
-----------------------------------------------------------------------------
Date of Procedure: 00, 00,1998
Clinician/Provider: WHPROVIDER, ONE
[^83]Ward/Clinic/Location: EMPLOYEE HEALTH Reports (WP):
Health Care Facility: HINES Notes (WP):
Comments:
Complete by (Date): 00, 00,1999
Results/Diagnosis: WNL/Normal HPV: YES
Sec Results/Diagnosis: Status: OPEN
(PAGE 1 OF 2)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Exit Save Next Page Refresh
Enter a command or '^' followed by a caption to jump to a specific field.
COMMAND: N Press \<PF1\>H for help Insert
\* \* \* EDIT A PROCEDURE \* \* \*
Patient Name: WHPATIENT, ONE(xxy/o) SSN: 000-88-8888
Case Manager: WHMANAGER, ONE Procedure: BIOPSY
PAP Regimen : Pap regimen (began 00, 00, 1998) Acc#: CO1998-00000
Cx Tx Need : Routine PAP (by 00 00,1998) Cx Facility: Hines
Br Tx Need : Screening (by 00, 00, 1998) Br Facility: Hines
[^84]Elig Code : SC LESS THAN 50% Veteran: YES
[^85]MST : No CST: Unknown
-----------------------------------------------------------------------------
Screening PAP: PS1998-00000
T-Zone Seen Entirely: YES Multifocal: YES
Lesion Outside Canal: YES Number of Quadrants: x
Satisfactory Exam: YES Quadrant Locations: AA,BB
IMPRESSION:
ECC Dysplasia: Not Done Margins Clear:
Ectocervical Biopsy: Not Available Stage: I
STD Evaluation: Negative (PAGE 2 OF 2)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Exit Save Next Page Refresh
Enter a command or '^' followed by a caption to jump to a specific field.
COMMAND: E Press \<PF1\>H for help Insert
WV ADD A NEW NOTIFICATIONAdd a New Notification
\* \* \* WOMEN'S HEALTH: ADD NEW NOTIFICATION \* \* \*
Select PATIENT NAME: WHPATIENT, ONE 00-00-49 000888888 YES SC VETERAN
\* \* \* EDIT A NOTIFICATION \* \* \*
Patient Name: WHPATIENT, ONE(xxy/o) SSN: 000-88-8888
Case Manager: WHMANAGER, ONE Patient Phone: 555-555-1234
Cx Tx Need : Routine PAP (by 00, 00,1998) Cx Tx Facility: Hines
Br Tx Need : Screening (by 00, 00, 1998)Xx Xx Facility: Hines
PAP Regimen : Pap regimen (began 00, 00, 1998)
[^86]Elig Code : SC LESS THAN 50% Veteran: YES
[^87]MST : No CST: Unknown
-----------------------------------------------------------------------------
Accession#: CN1998-00000 Procedure: BIOPSY
Date Notification Opened: 00, 00, 1998 Facility: HINES DEVELOPMENT
Purpose of Notification: Abnormal
Priority: URGENT, RESULT
Type of Notification: CONVERSATION WITH PATIENT Print Date:
Complete by (Date): 00, 00, 1999 Printed:
Outcome: Letter Canceled
Status: CLOSED Patient Ed: YES
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Exit Save Refresh
Enter a command or '^' followed by a caption to jump to a specific field.
Do you wish to PRINT this patient's Case Data?
Enter Yes or No: NO// \<RET\>
<span id="_Toc117589104" class="anchor"></span>

### [^88]Appendix C - Other Useful Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop a background task before it has completed, you must:
> 1\. Invoke the User’s Toolbox \[XUSERTOOLS\] menu. It may be on the primary or secondary menu.
> 2\. Select the TaskMan User \[XUTM USER\] option.
> 3\. Enter the task number at the “Select Task:” prompt. If the task number is unknown, you can enter two question marks to see a list of your tasks. Find the task number from the list and exit the list display.
> 4\. At the “Select Action (Task \# nnnnnn):” prompt (where nnnnnn is the task number you selected) enter “Stop task”.
The TaskMan utility will issue a message stating the outcome of your request.

### Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as Women’s Health, PIMS, etc.
Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of V*IST*A applications are the PIMS and Women’s Health application.
Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
ASAP Abbreviation for the phrase ‘as soon as possible’.
Audit Trail/Logging Features The use of automated software procedures to determine if the security controls implemented for protection of computer systems are being circumvented and to identify the potential source of the security breach.
Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
Baud Rate The rate at which data is being transmitted or received from a computer. The baud rate is equivalent to the number of characters per second times 10.
Block The unit of storage transferred to and from disk drives, typically 512, 1024, or 2048 bytes (characters).
Boot The process of starting up the computer.
Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
Byte A unit of computer space usually equivalent to one character.
Case Manager The person who is currently managing the women’s health care needs of a specific patient.
CIOFO Chief Information Office Field Office, formerly known as Information Resource Management Field Office, and Information Systems Center.
Contingency Plan A plan which assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
CORE A collection of VA developed programs (specific to PIMS, Pharmacy Service, and Laboratory Service) which is run at VA Medical Centers.
CPU Central Processing Unit, the heart of a computer system.
CRT Cathode Ray Tube, similar to a TV monitor but used in computer systems for viewing data. Also called a Video Display Terminal (VDT).
CST Civilian Sexual Trauma.
Cursor A visual position indicator (e.g., blinking rectangle or an underline) on a CRT that moves along with each character as it is entered from the keyboard.
Data Dictionary A description of file structure and data elements within a file.
Device A hardware input/output component of a computer system (e.g., CRT, printer).
Disk A magnetic storage device used to hold information.
Edit Used to change/modify data typically stored in a file.
Field A data element in a file.
File The M construct in which data is stored for retrieval at a later time. A computer record of related information (e.g., Patient file).
File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/ search related data in a file; a data base.
Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.
Gynecologic Pertaining to the female reproductive tract.
Hardware The physical or mechanical components of a computer system such as CPU, CRT, disk drives, etc.
IRMS Information Resource Management Service.
Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
Kilobyte More commonly known as Kbyte or ‘K’. A measure of storage capacity equivalent to 1024 characters.
LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
Legacy System An outdated system used for data storage and retrieval.
M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all V*IST*A applications.
MailMan An electronic mail, teleconferencing, and networking system.
MAM Abbreviation for Mammogram.
Maternity Care Coordinator A Maternity Care Coordinator (MCC) is a user that is assigned to pregnant female patients to coordinate their maternity care.
Megabyte A measure of storage capacity; approximately 1 million characters. Abbreviated as Mbyte or Meg.
Memory A storage area used by the computer to hold information.
Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
Menu Manager A part of the Kernel that allows each site to manage the various options or functions available to individual users.
Modem An electronic device which converts computer signals to enable transmission through a telephone.
Module A component of the Women’s Health software application that covers a single topic or a small section of a broad topic.
MST Military Sexual Trauma.
Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application. The Women’s Health Package uses WV as its namespace.
Operating System The innermost layer of software that communicates with the hardware. It controls the overall operation of the computer such as assigning places in memory, processing input and output. One of its primary functions is interpreting M computer programs into language the system can understand.
Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions. For example, the WVMENU is the main menu for the Women’s Health application.
Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within V*IST*A (e.g., the ADT and Women’s Health applications).
PAP Abbreviation for PAP smear.
Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
Port An outlet in the back of the computer into which terminals can be connected.
Printer A device for printing (on paper) data which is processed by a computer system.
Procedure Accession# A number assigned to represent a specific procedure performed on a specific patient on a certain date (e.g., PS1998-43).
Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
Response Time The average amount of time the user must wait between the time the user responded to a question at the terminal and the time the system responds by displaying data and/or the next question.
Restart/Recovery Procedures The actions necessary to restore a system's data files and computational capability after a system failure or penetration.
\<RET\> Carriage return or Enter.
Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Security Key A function which unlocks specific options and makes them accessible to an authorized user.
Security System A part of Kernel that controls user access to the various computer applications. When a user signs-on, the security system determines the privileges of the user, assigns security keys, tracks usage, and controls the menus or options the user may access. It operates in conjunction with MenuMan.
Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
Subroutine A part of a program which performs a single function.
Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
Telecommunications Any transmission, emission, or reception of signs, signals, writing, images, sounds or other information by wire, radio, visual, or any electromagnetic system.
Terminal A device used to send and receive data from a computer system (i.e., keyboard and CRT, or printer with a keyboard).
UCI User Class Identifier. The major delimiter of information structure within the operating system.
User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
Utility An M program that assists in the development and/or maintenance of a computer system.
VDT Video Display Terminal. Also called a Cathode Ray Tube (CRT).
Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
V*IST*A Veterans Health Information Systems and Technology Architecture.
<span id="_Toc117589106" class="anchor"></span>

### Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accessing menus, 1.8
Add a New Notification, 4.39
Add a NEW Procedure, 4.16
Add a Refusal of Treatment, 4.35
Add an HISTORICAL Procedure, 4.34, 7.4
Add(Accession) a NEW Procedure, 8.2
Add/Edit a Notification Purpose & Letter, 2.3
Add/Edit Case Managers, 2.11
Add/Edit Notification Outcomes, 2.7
Add/Edit to Referral Source File, 2.22
Assigning menus, 1.8
Automatically Load Patients, 2.13
Automatically loading files, 1.8
Browse Notifications, 4.49
Browse Patients with Needs Past Due, 4.12, 5.15
Browse Procedures for Possible Duplicates, 7.5
Browse Procedures, 4.28
Case Managers and the Program Manager, 1.3
Compliance Rates for PAPs and MAMs, 5.14
Display/Print Daily Log, 8.8
Edit a Notification, 4.45
Edit a Procedure, 4.22
Edit a Procedure Result, 8.6
Edit a Refusal of Treatment, 4.37
Edit Accessioned Procedure, 8.4
Edit Diagnostic Code Translation File, 2.20
Edit PAP Regimen Log, 7.6
Edit Pregnancy Log, 7.7
Edit Site Parameters, 2.8
Edit Synonyms for Notification Types, 2.6
Edit Synonyms for Results/Diagnoses, 2.18
Edit/Print Patient Case Data, 4.2, 7.3
Editing site configurable files, 1.7
Examples of Major Screen Edits, AB.1
File Maintenance Menu, 2.1, 6.2
Health Summary, 4.27
Implementation and Maintenance, 1.1
Import Radiology/NM Exams, 2.15
Installation of Software, 1.6
Lab Data Entry Menu, 6.5, 8.1
List Sexual Trauma Data, 5.17
Main Features, 1.1
Management Reports Menu, 5.1
Manager ‘s Functions Menu, 6.1
Manager ‘s Patient Management Menu, 6.4, 7.1
Package Operation, 3.1
Patient Management Menu, 4.1
Patient Profile Including Errors, 7.2
Patient Profile, 4.6
Patients, Procedures, and Notifications, 1.2
Print a Procedure, 4.29, 8.7
Print Diagnostic Code Translation File, 2.21
Print Individual Letters, 4.50
Print Notification Purpose & Letter File, 2.5
Print Patient Demographic Info (Face Sheet), 4.9
Print Queued Letters, 4.51, 6.3
Print Results/Diagnosis File, 2.17
Print Synonyms for Results/Diagnoses, 2.19
Printer issues, 1.8
Procedure Statistics Report, 5.2
Queueing TaskMan jobs, 1.8
Resource Requirements, 1.8
Results/Diagnosis File by Procedure, AA.1
Retrieve/Print Earlier Snapshots, 5.8
Save Lab Test as Procedure, 4.14
Setting up the software environment, 1.7
Sexual Trauma Summary Report, 5.16
Snapshot of the Program Today, 5.3
The Basic Patient Management Loop, 1.3
Transfer a Case Manager’s Patients, 2.12
V*IST*A, 1
[^1]: Patch WV\*1\*7 October 1999 Print future appointments
[^2]: Patch WV\*1\*16 February 2005 New fields added
[^3]: Patch WV\*1\*16 February 2005 New fields added
[^4]: Patch WV\*1\*9 February 2000 Mailing address change
[^5]: Patch WV\*1\*10 April 2000 Definition of default \# days change
[^6]: Patch WV\*1\*16 February 2005 New fields added.
[^7]: Patch WV\*1\*10 April 2000 Include some non-veterans
[^8]: Patch WV\*1\*6 May 1999 Link to Lab Package
[^9]: Patch WV\*1\*10 April 2000 Include some non-veterans
[^10]: Patch WV\*1\*7 October 1999 Future inactivation date selectable
[^11]: Patch WV\*1\*3 December 1998 Includes all patients
[^12]: Patch WV\*1\*7 October 1999 No deceased women added
[^13]: Patch WV\*1\*10 April 2000 Include age, veteran, and eligibility code in display
[^14]: Patch WV\*1\*10 April 2000 Include age, veteran, and eligibility code in report
[^15]: Patch WV\*1\*7 October 1999 Added procedures
[^16]: Patch WV\*1\*10 April 2000 Include patients by eligibility code
[^17]: Patch WV\*1\*14 April 2001 Description changed
[^18]: Patch WV\*1\*14 April 2001 Field description changed
[^19]: Patch WV\*1\*14 April 2001 New field
[^20]: Patch WV\*1\*16 February 2005 New option
[^21]: Patch WV\*1\*6 May 1999 Health Summary option added
[^22]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^23]: Patch WV\*1\*14 April 2001 MST appears in heading of the report
[^24]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to CST prompt
[^25]: Patch WV\*1\*7 October 1999 Added codes
[^26]: Patch WV\*1\*7 October 1999 Added codes
[^27]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^28]: Patch WV\*1\*7 October 1999 Added codes
[^29]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^30]: Patch WV\*1\*17 April 2003 Confidential address
[^31]: Patch WV\*1\*7 October 1999 Date of death as inactive date
[^32]: Patch WV\*1\*10 April 2000 Include age, veteran, and eligibility code in report
[^33]: Patch WV\*1\*6 May 1999 New option
[^34]: Patch WV\*1\*6 May 1999 New option
[^35]: Patch WV\*1\*16 February 2005 Explanation of new WV\*1\*16 functionality
[^36]: Patch WV\*1\*7 October 1999 New procedures added
[^37]: Patch WV\*1\*7 October 1999 Info. message to case manager
[^38]: Patch WV\*1\*16 February 2005 New CPRS alert
[^39]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^40]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^41]: Patch WV\*1\*6 May 1999 Amended report
[^42]: Patch WV\*1\*6 May 1999 ‘+’ sign if text present
[^43]: Patch WV\*1\*7 October 1999 Info. message to case manager
[^44]: Patch WV\*1\*16 February 2005 New CPRS alert
[^45]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^46]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^47]: Patch WV\*1\*6 May 1999 Amended report
[^48]: Patch WV\*1\*6 May 1999 ‘+’ sign if text present
[^49]: Patch WV\*1\*5 March 1999 New option
[^50]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^51]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^52]: Patch WV\*1\*7 October 1999 New field
[^53]: Patch WV\*1\*6 May 1999 New field
[^54]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^55]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^56]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^57]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^58]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^59]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^60]: Patch WV\*1\*7 October 1999 Select another notification
[^61]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^62]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^63]: Patch WV\*1\*17 April 2003 Confidential address
[^64]: Patch WV\*1\*17 April 2003 Confidential address
[^65]: Patch WV\*1\*14 April 2001 Change in option name
[^66]: Patch WV\*1\*11 June 2000 Added option for MST
[^67]: Patch WV\*1\*12 August 2001 Sort by facility added to report, and list of any procedures without a facility added
[^68]: Patch WV\*1\*7 October 1999 Treatment need not indicated
[^69]: Patch WV\*1\*7 October 1999 Treatment need not indicated
[^70]: Patch WV\*1\*7 October 1999 Percentage of women returning to program
[^71]: Patch WV\*1\*7 October 1999 Percentage of women returning to program
[^72]: Patch WV\*1\*14 April 2001 Change in option name and description
[^73]: Patch WV\*1\*11 June 2000 Added option for MST
[^74]: Patch WV\*1\*14 April 2001 Option description changed
[^75]: Patch WV\*1\*14 April 2001 WH prompt changed to MST prompt and CST prompt
[^76]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^77]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^78]: Patch WV\*1\*14 April 2001 Sexual Trauma prompt changed to MST prompt and CST prompt
[^79]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^80]: Patch WV\*1\*7 October 1999 New data capture
[^81]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^82]: Patch WV\*1\*14 April 2001 Sexual Trauma changed to MST and CST
[^83]: Patch WV\*1\*6 May 1999 Changed prompts
[^84]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^85]: Patch WV\*1\*14 April 2001 Sexual Trauma changed to MST and CST
[^86]: Patch WV\*1\*10 April 2000 Include eligibility code in heading
[^87]: Patch WV\*1\*14 April 2001 Sexual Trauma changed to MST and CST
[^88]: Patch WV\*1\*14 April 2001 New appendix
