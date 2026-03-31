---
title: PATS Data Migration Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: QAC
app_name: Patient Advocate Tracking System (PATS)
section: GUI
app_status: active
pkg_ns: QAC
patch_ver: 1.1
patch_id: QAC*1.1
group_key: "QAC:QAC:1.1"
file_numbers: 
  - 2
  - 4
  - 21
  - 44
  - 49
  - 200
  - 745
security_keys: []
menu_options: 7
description: > The Patient Advocate Tracking System (PATS) is a centralized, web-based application. PATS replaces Patient Representative (Patient Rep) as the VHA’s system for documenting, tracking, and communicating patient-related issues. Patient Rep data at each medical site must be migrated to PATS. Once data
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - class
  - pats
  - style
  - width
  - patient
  - contents
  - migration
page_count: 0
word_count: 17213
section_count: 46
table_count: 7
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: October 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_1_datamigrationguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_1_datamigrationguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=172"
---

> ![](pats-data-migration-guide/001.png)

PATIENT ADVOCATE TRACKING SYSTEM (PATS)

DATA MIGRATION GUIDE

> PATSDM Version 1.1

> Revised October 2011

> Department of Veterans Affairs Office of Enterprise Development (OED)

> Veterans Health Information Technology (VHIT)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Data Migration Steps](#data-migration-steps)
  - [Data Migration Diagram](#data-migration-diagram)
  - [Job Roles Responsible for Data Migration Steps](#job-roles-responsible-for-data-migration-steps)
  - [Before You Begin](#before-you-begin)
- [Chapter 1 - Downloading the List of Valid National Divisions](#chapter-1-downloading-the-list-of-valid-national-divisions)
  - [(Role Performing Task: PATS Migration Manager)](#role-performing-task-pats-migration-manager)
- [Chapter 2 - Cleaning the Data](#chapter-2-cleaning-the-data)
  - [(Role Performing Task: Patient Advocate)](#role-performing-task-patient-advocate)
  - [Running the Data Cleanup Options](#running-the-data-cleanup-options)
  - [Printing Reports](#printing-reports)
  - [Resolving Outstanding Alerts](#resolving-outstanding-alerts)
- [Chapter 3 - Moving the Data to a Temporary Staging Area](#chapter-3-moving-the-data-to-a-temporary-staging-area)
  - [(Role Performing Task: PATS Migration Manager)](#role-performing-task-pats-migration-manager-1)
  - [Running VistA Patient Representative Migration Steps](#running-vista-patient-representative-migration-steps)
  - [Data in the Staging Area](#data-in-the-staging-area)
  - [Re-Running the Migration Steps](#re-running-the-migration-steps)
  - [Using the UTIL Options](#using-the-util-options)
  - [Printing Reports](#printing-reports-1)
- [Chapter 4 - Migrating Data into PATS](#chapter-4-migrating-data-into-pats)
  - [(Role Performing Task: PATS Migration Manager)](#role-performing-task-pats-migration-manager-2)
  - [Migrating Institution Data into PATS](#migrating-institution-data-into-pats)
  - [Viewing Institution Migration History](#viewing-institution-migration-history)
- [Chapter 5 - Post Migration](#chapter-5-post-migration)
  - [(Role Performing Task: Patient Advocate)](#role-performing-task-patient-advocate-1)
  - [Planning Reference Tables](#planning-reference-tables)
  - [Populating Reference Tables](#populating-reference-tables)
- [Appendix A - Correcting Data Errors](#appendix-a-correcting-data-errors)
  - [(Role Performing Task: Patient Advocate)](#role-performing-task-patient-advocate-2)
  - [General Rules](#general-rules)
  - [Specific Fields](#specific-fields)
    - [Consumer Contact (745.1)](#consumer-contact-7451)
    - [Congressional Office (745.4)](#congressional-office-7454)
    - [Contact Discipline (745.5)](#contact-discipline-7455)
    - [Qac Service/Discipline (745.55)](#qac-servicediscipline-74555)
    - [Customer Service Standard (745.6)](#customer-service-standard-7456)
    - [Patient (2)](#patient-2)
    - [Hospital Location (44)](#hospital-location-44)
    - [New Person (200)](#new-person-200)
- [Appendix B - Data Migration Reports](#appendix-b-data-migration-reports)
  - [(Role Performing Task: Patient Advocate)](#role-performing-task-patient-advocate-3)
  - [RPTS – Report Descriptions](#rpts-report-descriptions)
  - [DERR](#derr)
  - [ALST](#alst)
  - [CNG](#cng)
  - [CNT](#cnt)
  - [STAT](#stat)
  - [NOT](#not)
- [Appendix C - Deleting Migrated Data](#appendix-c-deleting-migrated-data)
  - [(Role Performing Task: PATS Migration Manager)](#role-performing-task-pats-migration-manager-3)
  - [Starting Over](#starting-over)
  - [Deleting Data from the PATS Database](#deleting-data-from-the-pats-database)
- [Appendix D - Technical Information for Maintenance and Support](#appendix-d-technical-information-for-maintenance-and-support)
  - [Verifying that Data Migration was Successful](#verifying-that-data-migration-was-successful)
  - [Use of the ^XTMP global](#use-of-the-xtmp-global)
  - [Downloaded List of National Divisions](#downloaded-list-of-national-divisions)
  - [Option QACI PREMIGRATION ERROR REPORT](#option-qaci-premigration-error-report)
  - [Option QACI AUTO CLOSE ROCS](#option-qaci-auto-close-rocs)
  - [Option QACI MIGRATION DATA BUILD](#option-qaci-migration-data-build)
  - [Migrating the Data to PATS](#migrating-the-data-to-pats)
  - [Description of Migration Process](#description-of-migration-process)
  - [Troubleshooting Tips](#troubleshooting-tips)
  - [Patient Representative to PATS Data Migration Mapping](#patient-representative-to-pats-data-migration-mapping)
> The following table displays the revision history for this document.
| Date   | Revision | Description                                                            | Author |
|------------|--------------|----------------------------------------------------------------------------|------------|
| 3-19-07    | Initial      |                                                                            | REDACTED   |
| 10-10-2011 | 1.1          | Revised in relation to EIE name change, Updated Oracle version information | REDACTED   |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Advocate Tracking System (PATS) is a centralized, web-based application. PATS replaces Patient Representative (Patient Rep) as the VHA’s system for documenting, tracking, and communicating patient-related issues. Patient Rep data at each medical site must be migrated to PATS. Once data is moved to PATS, Patient Rep menus are inactivated. These menus can be re-activated, if necessary.

## Data Migration Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Chapter and Process Breakdown

> This guide provides background information and step-by-step instructions for migrating data from Patient Rep to PATS. The guide is divided into the following sections:

| Chapter  | Tasks                                          | Performed By              |
|--------------|----------------------------------------------------|-------------------------------|
| 1            | Downloading the list of valid National divisions   | IRM or PATS Migration Manager |
| 2            | Cleaning the data                                  | Patient Advocate              |
| 3            | Moving the data from Patient Rep to a staging area | PATS Migration Manager        |
| 4            | Migrating the data from the staging area to PATS   | PATS Migration Manager        |
| 5            | Populating reference tables                        | Patient Advocate              |
| Appendix | Description                                    | Performed By              |
| A            | Correcting Data Errors                             | Patient Advocate              |
| B            | Data Migration Reports                             | Patient Advocate              |
| C            | Deleting Migrated Data                             | PATS Migration Manager        |
| D            | Technical Information                              | Maintenance and Support staff |

> Note: Tasks are written in the sequence they should be performed. You can deviate from this sequence with no harm to the data; however, you may receive error messages.

## Data Migration Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pats-data-migration-guide/002.png)Patient Rep (VistA) PATS (Java/Oracle)

> Advocate runs CHK and reviews reports to find errors in Patient Rep data.

> Has DV app been run?

> Advocate fixes errors using Patient Rep or FileMan.

> ~~Yes~~

Yes

> Fix data errors?

No

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p>EMC fixes</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>problem on</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Java/Oracle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Manager uses</td>
<td><blockquote>
<p>side.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Yes

> Fix data errors?

> No Data

> migrated successfully

> ?

> EMC examines LOG files to determine cause of error.

Post - Migration

> Yes

## Job Roles Responsible for Data Migration Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below assigns data migration responsibilities to job roles. These roles may not match real job titles and may overlap at some sites. Roles are controlled by assigning menu options and security keys on the VistA side (see the *PATS Installation Guide for IRM Staff*).

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Role</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Location</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Responsibilities</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Should know how to:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Patient Advocate</strong></td>
<td>Field Site</td>
<td><ul>
<li><p>Generate data analysis reports</p></li>
<li><p>Fix data errors</p></li>
<li><p>Use menu options to auto-close Reports of Contact (ROCs)</p></li>
</ul></td>
<td><ul>
<li><p>Use VistA menus</p></li>
<li><p>Use Patient Rep</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>PATS Migration Manager (</strong>Probably the Patient Advocate)</td>
<td>Field Site</td>
<td><ul>
<li><p>Download the list of valid National divisions from the EIE</p></li>
<li><p>Move data from Patient Rep into a temporary staging area</p></li>
<li><p>Migrate data from the temporary staging area into PATS</p></li>
</ul></td>
<td><ul>
<li><p>Use VistA menus</p></li>
<li><p>Navigate, enter data, and use interface controls on a web page</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Information Resource Management (IRM) Repres- entative</strong></td>
<td>Field Site</td>
<td><ul>
<li><p>Correct data errors that cannot be corrected using Patient Rep</p></li>
</ul></td>
<td><ul>
<li><p>Use FileMan</p></li>
<li><p>Directly edit a MUMPS global to correct invalid characters</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Enterprise Infrastructure Engineering (EIE) Data Manager</strong></td>
<td>EIE</td>
<td><ul>
<li><p>Maintain the PATS Oracle database</p></li>
<li><p>Determine source of migration errors (EIE or data)</p></li>
</ul></td>
<td><ul>
<li><p>Read and use error logs</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tasks must be completed prior to beginning the steps in *Chapter 2, Cleaning the Data*. For more information, see the *PATS Installation Guide for IRM Staff* or contact your IRM representative.

<table>
<colgroup>
<col style="width: 72%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Task</strong></th>
<th><blockquote>
<p><strong>Performed by</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATS KIDS build QAC*2.0*19 has been installed at the local M VistA site.</td>
<td>IRM</td>
</tr>
<tr class="even">
<td>Patient Advocates responsible for data cleanup have been assigned the Main Menu for Pre-Migration Data Cleanup.</td>
<td>IRM</td>
</tr>
<tr class="odd">
<td>PATS Migration Manager responsible for moving data into the staging area has been assigned the Main Menu for Patient Rep Migration Steps.</td>
<td>IRM</td>
</tr>
<tr class="even">
<td>PATS Migration Manager responsible for migrating the data from the VistA Patient Rep files into the PATS system has access to a web browser and has been <em>assigned the QACV_DMGR key</em>.</td>
<td>IRM</td>
</tr>
</tbody>
</table>

| Task                                                                         | Performed by       |
|----------------------------------------------------------------------------------|------------------------|
| EIE has been notified that your site wishes to begin the data migration process. | PATS Migration Manager |

# Chapter 1 - Downloading the List of Valid National Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: PATS Migration Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to starting the data cleanup at your site, you must download a list of valid National divisions (station numbers) for your default institution. During data cleanup (see Chapter 2), this list is used to report any data that references a division that is not in the National file.

> Note: If a division is not in the National file, you must either change the division on the Patient Rep data shown in the error report or contact Central Office to have the division added to the National table.

> Note: The person performing this task must hold the VistA QACV_DMGR security key.

> The Project Implementation Office (PIO) will send you a URL to download the list of valid National divisions when you’re scheduled to begin your data cleanup.

> To download this list, the PATS Migration Manager or an IRM staff member at your field site performs the following steps:

1.  Open a browser window and enter the URL for PATS Download to Vista application that you received from the PIO.
2.  Enter your VistA Access and Verify codes.
3.  From the drop-down list, select your Institution.

> Note: For a multi-division site, select the default Institution (i.e., the 3-digit station number that represents the institution that stores the VistA data for all the divisions). Station numbers for all divisions within your default institution will be downloaded.

4.  Click Logon.
5.  Click the Download button.

> *Result: The browser displays ‘Division downloaded successfully’ when the list has been successfully downloaded.*

> Note: This process only needs to be performed one time and must be performed *prior to beginning the data cleanup*. However, it does not hurt anything to perform the process more than once.

# Chapter 2 - Cleaning the Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: Patient Advocate)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to migration, Patient Representative (Patient Rep) data must be complete and accurate in the Reports of Contact (ROCs) and reference tables. Any records with reported errors will not be moved to PATS. *Only ROCs without errors will be moved into PATS.* Also, outstanding alerts will not be moved into PATS.

> This chapter describes how Patient Advocates can identify errors in the Patient Rep data and automatically close ROCs with a date of contact prior to the previous quarter. The chapter also explains how to resolve outstanding alerts.

> For detailed information on how to fix errors (clean up data), see *Appendix A, Correcting Data Errors* and *Appendix B, Data Migration Reports*.

> Several reference tables must be populated in the new PATS system before the sites can begin using the new system. To minimize downtime, you should begin planning what data you will want to have in these new tables during the data cleanup process. (See *Chapter 5, Post Migration* for details on planning table entries.)

## Running the Data Cleanup Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Advocate at each field site must perform the following steps to run the data cleanup options:

1.  From any VistA menu, enter PRDC (Main Menu for Pre-Migration Data Cleanup) and press \<Enter\>.

> *Result: The Main Menu for Pre-Migration Data Cleanup screen displays with the following menu options:*

> CHK Check for Data Errors Prior to Migration CLS Auto-Close Old Open Contacts (ROCs)

> RPTS Data Migration Reports …

2.  To analyze data errors, enter chk (CHK – Check for Data Errors Prior to Migration).

> *Result: This process may take a few minutes to run, as it checks all of the Patient Representative data for errors. After finding all errors, it creates the following error reports:*

- *Data Cleanup – Ref Table Data Errors*
- *Data Cleanup – ROC Errors*

> Note: If you have not downloaded the list of valid National divisions from the central PATS system, you will get an error message. See Chapter 1.

> Note: If a division is not in the National file, you must either change the division on the Patient Rep data shown in the error report or contact Central Office to have the division added to the National table.

3.  Use Patient Rep to correct the errors detailed in the Data Cleanup reports.

> Note: Records that contain data errors will not be migrated into PATS.

> See *Appendix A, Correcting Data Errors*, for specific information about making corrections.

4.  After correcting the errors, repeat steps 1 and 2 to run new error reports and verify that errors have been corrected.

> Note: Continue running CHK until all records you wish to migrate are corrected.

5.  *OPTIONAL STEP: Automatically close old ROCs*

> Once all errors have been corrected in Steps 1 – 4 above, you may want to automatically close any open ROCs that have a Date of Contact prior to the beginning of the previous quarter.

> Note: Any ROCs with errors will not be closed. To automatically close old ROCs, enter CLS.

> *Result: The system performs the following functions:*

- Sets the status of these ROCs to “Closed” and in some cases automatically replaces null fields required to close a ROC.
- Creates a report that lists the closed ROCs and any changes made to them during the auto-close process.

> See *Appendix B, Data Migration Reports* for details about the Auto-Closed ROCs report.

## Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Data Migration reports are available and can be printed at any time.

6.  From any VistA menu, enter PRDC (Main Menu for Pre-Migration Data Cleanup) and press \<Enter\>.
7.  Enter RPTS (RPTS – Data Migration Reports).
    - DERR option: reprints the error reports (last CHK report) generated in Step 2 above (see *Running the Data Cleanup Options* section).
    - ALST option: reprints the list of auto-closed ROCs generated in Step 5 above.
    - CNG option: displays system-generated changes (null data) that will be made to ROCs when they are migrated into PATS.
    - CNT option: displays total number of ROCs, total count of errors, total count of entries in the staging area, and total count of entries migrated for each of the reference files and the ROC files.

> Note: Counts for entries in the staging area and for entries migrated will be 0 prior to starting the migration steps.

- STAT option: displays the current migration status of an individual ROC.
- NOT option: prints report of outstanding Patient Rep Alerts.

> Recommendation: After you’ve cleaned up the data, print the CNT and NOT

> reports.

> See *Appendix B, Data Migration Reports* for detailed descriptions of all of the reports found on the RPTS menu*.*

## Resolving Outstanding Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data migration process does not migrate alerts from Patient Rep to PATS.

> To view outstanding alerts, run the NOT option (see *Printing Reports* section). Then complete one of the following tasks:

- Resolve any outstanding alerts prior to migrating the data into PATS.

#### OR

- After data has been migrated into PATS, use the Edit a ROC option to send a notification to the user.

# Chapter 3 - Moving the Data to a Temporary Staging Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: PATS Migration Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes how to move the data from the Patient Rep files into a temporary staging area. When you move data into the staging area, Patient Rep menus are inactivated (data can not be entered into Patient Rep) and the data is ready to migrate into PATS.

> Note: Do not move data into the staging area until right before you’re ready to migrate data.

## Running VistA Patient Representative Migration Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PATS Migration Manager at each field site should perform the following steps to run Patient Rep migration options:

1.  From any VistA menu, enter PRDM (Main Menu for Patient Rep Migration Steps), and press \<Enter\>.

> *Result: The Main Menu for Patient Rep Migration Steps screen displays with the following menu options:*

> MSTG Move Data to Staging Area for Migration RPTS Data Migration Reports ...

> UTIL Activate/Inactivate Options ...

2.  To copy data from Patient Rep into the temporary staging area, enter mstg (MSTG - Move Data to Staging Area for Migration) and press \<Enter\>.

> *Result: The system performs the following steps, which may take several minutes depending on the amount of data:*

- Inactivates all Patient Rep menus that allow Patient Rep data to be edited \[QAC NEW, QAC EDIT, QAC STATUS, QAC SETUP MENU, QAC ALERT and QAC ROLLUP (MANUAL)\].
- Kills the tasked job that performs the nightly rollup of data to Austin. Data that is ready to send will be picked up by the next rollup from the PATS system after the data is migrated.
- Runs the same error checks and generates the same error reports as in Chapter 2, section 2.2.

> Note: Data with errors are not moved to the staging area. Only error-free ROCs will be moved to the staging area.

> If you want to correct errors in Patient Rep after running MSTG, you must re-run MSTG to move the corrected data into the staging area.

3.  Select the RPTS menu. Select the CNT report (Count of Errors, Ready to Migrate, Migrated) in order to verify that the data is ready to migrate.
4.  To migrate data from the staging area to PATS, go to *Chapter 4, Moving Data into PATS*.

## Data in the Staging Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options to generate an error report, auto-close ROCs, or move data to the staging area generate temporary data in VistA. The temporary data will be purged 30 days from the time that the user last executes one of those options. You can take as long as necessary for data cleanup. *However, you should not move the data into the staging area until shortly before you perform the actual migration.* Also, if you want to keep any of the reports generated during the migration phases, you should print them, since they are generated from the temporary data and will no longer be available 30 days after migration completes.

> Another reason to avoid moving data to the staging area far in advance of the actual migration is that it inactivates the Patient Rep menus, which prohibits users from entering any new data into Patient Rep.

> If you decide you want to re-activate Patient Rep after moving data to the staging area, you should repeat the step of moving data to the staging area (section 3.1) shortly before the actual migration. If you don’t move the data to the staging area again, the new data that was entered into Patient Rep won’t be migrated, because only data from the staging area will migrate.

## Re-Running the Migration Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Patient Advocate wants to correct data errors in Patient Rep after the data has been copied to the staging area or data migration has been completed, Patient Rep menus need to be re- activated. Then data is moved to the staging area to pick up the corrected records.

5.  To re-activate Patient Rep menus, enter util (UTIL - Activate/Inactivate Options….).

#### Enter popt (POPT – Activate/Inactivate Patient Rep Options).

6.  A prompt asks if you want to reactivate the menu. Enter yes and press \<Enter\>.
7.  Go to Patient Rep and correct the data errors by following the steps in *Chapter 2, Cleaning the Data.*
8.  Repeat the steps in section 3.1, *Running VistA Patient Representative Migration Steps*.

## Using the UTIL Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The UTIL menu has the following options.

- POPT – Activate/Inactivate Patient Rep Options
- RTSK – Reschedule Rollup to Austin
- KTSK – Stop (Kill) Rollup to Austin

> The table explains situations when you would use these UTIL options.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Use the option when</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>POPT</strong> – Activate/Inactivate Patient Rep Options</td>
<td><ul>
<li><p>Data was moved to the staging area or migrated to PATS and you want to clean up and migrate other data.</p></li>
<li><blockquote>
<p>Data was moved to the staging area and you decide to keep running Patient Rep and restart the data migration later.</p>
</blockquote></li>
<li><blockquote>
<p>You accidentally inactivated or reactivated the Patient Rep options.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>RTSK</strong> – Reschedule Rollup to Austin</td>
<td>Data was moved to the staging area and you decide to keep running Patient Rep and restart the data migration later. Rollups need to continue to be transmitted to Austin.</td>
</tr>
<tr class="odd">
<td><strong>KTSK</strong> – Stop (Kill) Rollup to Austin</td>
<td>You want to stop the rollup to Austin.</td>
</tr>
</tbody>
</table>

## Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Data Migration reports are available and can be printed at any time.

1.  From any VistA menu, enter PRDM (Main Menu for Patient Rep Migration Steps) and press \<Enter\>.

#### Enter rpts (RPTS – Data Migration Reports).

- DERR option: reprints the last CHK report (error reports) generated.
- ALST option: reprints the list of auto-closed ROCs generated.
- CNG option: displays system-generated changes (null data) that will be made to ROCs when they are migrated into PATS.
- CNT option: displays total number of ROCs, total count of errors, total count of entries in the staging area, and total count of entries migrated for each of the reference files and the ROC files.
- STAT option: displays the current migration status of an individual ROC.
- NOT option: prints report of outstanding Patient Rep Alerts.

> Important: After you’ve moved the data to the staging area and before you migrate data, print the CNT report to verify that the data is ready to migrate

> See *Appendix B, Data Migration Reports* for detailed descriptions of all of the reports found on the RPTS menu*.*

# Chapter 4 - Migrating Data into PATS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: PATS Migration Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Now that the data you want to migrate is free of errors, ROCs are closed, and the data is in the staging area, the PATS Migration Manager performs the steps below to migrate the data into the PATS database. This final stage is completed via a web-based application hosted on the EIE centralized servers using the following options:

- Migrate Institution – Moves the data for an institution or multi-divisional site from the staging area in VistA into the PATS Oracle tables.
- View Institution Report – View the data migration status/history report for a selected institution or multi-divisional site.

> The Project Implementation Office (PIO) will send you a URL to access the Data Migration application when you’re scheduled to begin using PATS. Please coordinate with the PIO to determine exactly when you should run the migration and let them know if you are unable to perform the migration during your allotted time.

> After a site migrates all of its data into PATS, users can no longer enter new data into Patient Rep. Patient Rep reports which display the legacy data may still be run after data migration.

> Note: The person performing the data migration must hold the VistA QACV_DMGR security key.

## Migrating Institution Data into PATS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Important: Before you migrate data, print the VistA CNT report to verify that data is ready to migrate.

> To migrate data into PATS, the PATS Migration Manager at each field site should perform the following steps:

1.  Open a browser window and enter the URL for the PATS Data Migration application that you received from the PIO.
2.  Enter your Access and Verify codes for the Institution into which you are migrating data.
3.  From the drop-down list, select the Institution into which you are migrating data.

> Note: For a multi-division site, select the default Institution (i.e., the 3-digit station number that represents the institution that stores the VistA data for all the divisions). All data for the child divisions will be migrated along with the data for the default Institution.

4.  Click Logon.
5.  From the menu bar on the left, select Migrate Institution.

> *Result: The system displays your Institution name and number and a Start button.*

6.  Click Start.

> *Result: The browser displays a confirmation that the request to migrate has been successfully submitted.*

7.  Click the “<u>View the migration report</u>” message.

> *Result: The browser displays a report showing the status of the current migration, followed by a history of all of the other PATS data migration and deletion operations for this institution.*

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](pats-data-migration-guide/003.png)</p>
</blockquote></th>
<th>After you confirm that you want to run a data migration and you click on the link to view the report, it may appear that nothing has happened. If two institutions migrate their data about the same time, the second institution request is put in a queue. If your institution is the second request, the confirmation will not appear in your report until the first institution’s migration has completed. You can come back to the data migration application at a later time to check the status. You do not need to run the data migration again.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Note: Once your migration begins, the process may take several minutes to finish, depending on the amount of data being migrated. The migration report page will refresh every 10 seconds to display the current status of the migration. You can safely close your browser, or you can leave it open to track the status.

#### Tip: To monitor the counts of data items still in the staging area (ready to migrate) and the number of items that have successfully migrated into PATS, go to the RPTS menu in VistA and run the CNT report as described *Chapter 3*.

8.  When the data migration is complete, the first entry on the migration report page shows that the data migration was successful and displays the starting and ending times.

> Note: If you receive an error message on the migration report page, contact EVS for assistance. They will determine the cause of the error. In most cases, they will advise you to correct an error in the data. Once you have been informed the problem has been corrected, you will need to repeat the migration steps as described in section *3.3, Re-Running the Migration Steps*.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](pats-data-migration-guide/004.png)</p>
</blockquote></th>
<th><em><strong>When the data migration has completed, notify the PIO. The PIO will contact the EIE Manager to verify that the data migrated successfully into the central database.</strong></em></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Viewing Institution Migration History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rather than wait for the data migration to run, you can close the browser and complete other tasks. When you’re ready, you can view the history report to verify that the migration ran successfully.

9.  Open a browser window and enter the URL for the PATS Data Migration application that you received from the PIO.
10. Enter your Access and Verify codes for the Institution into which you are migrating data.
11. From the drop-down list, select the Institution into which you are migrating data. If this is a multi-divisional site, all data for the child divisions will be migrated along with the data for the parent institution.
12. Click Logon.
13. From the menu bar on the left, select View Institution Report.

> *Result: The system displays your Institution name and number and a View button.*

14. Click View.

> *Result: The system displays a history in chronological order of all migration and/or deletion actions performed for the selected institution. The report displays starting and ending dates of successful operations and error reports, if any errors occurred during the operation.*

# Chapter 5 - Post Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: Patient Advocate)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Several reference tables must be populated in the new PATS system before the sites can begin using the new system. During data cleanup time, you should begin planning what data you want to have in these new tables. As soon as you receive the URL that allows you to access PATS, you may begin populating the tables. You do not have to wait until the data migration has completed to populate these tables. This will minimize the downtime between the time the Patient Advocates stop using the old Patient Rep system and the time they begin using the new PATS system.

> Note: During migration of reference table entries, the name of each entry coming in from Patient Rep is compared to entries already in the PATS table. If an entry with the same name already exists in the table, the migration process will not create a new entry and will not over-write the existing entry.

## Planning Reference Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section gives you background information to assist you in planning what data you want to include in the reference tables. Planning ahead will help you to be up and running the PATS application in the minimal amount of time.

#### Facility Service or Section

> The VISN-level user for each VISN is responsible for populating the new Facility Service or Section (FSoS) table for their VISN in the new PATS system. The FSoS table is a replacement for the old Service/Discipline entries in file 745.55 at the local sites. Old service/discipline entries will migrate from Patient Rep; however, they will be marked inactive in the PATS system. In order to make them available for use on new Reports of Contact (ROCs), the VISN-level user must either re-activate the migrated entries, or add new entries. This table must be populated before the first site within that VISN will be able to resolve ROCs in the PATS system. A facility service or section entry must be associated with each Issue Code on a ROC.

#### Hospital Location

> SRCU (Site Record Control Users) users at each local division are responsible for populating the new Hospital Location table for their site. Old hospital location entries will migrate from Patient Rep, however they will be marked inactive in the PATS system. In order to make them available for use on new ROCs, the SRCU user must either re-activate the migrated entries, or add new entries. This table must be populated before the local division will be able to select hospital locations associated with issue codes on a ROC.

#### Comps

> If a site distributes comps as part of the resolution process, SRCU users at each local division will be responsible for populating the new Comps table. This data did not exist in Patient Rep. If you populate the Comps table, your users will be able to select a Comp for inclusion on a ROC as part of the process to resolve the ROC. This table must be populated before the local division will be able to add a Comp to a ROC.

#### Boilerplate Resolution Text

> The new PATS system allows a local division to associate canned resolution text related to a specific issue code. If you choose to populate the Boilerplate Resolution Text table, your users will be allowed to copy the canned text related to an issue code on a ROC into the resolution text for that ROC, thus saving time. The SRCU users at each local division are responsible for populating the new Boilerplate Resolution Text table. This data did not exist in Patient Rep. This table must be populated before the local site will be able to use the canned resolution text.

## Populating Reference Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Project Implementation Office (PIO) will send you a URL to access the PATS application when you’re scheduled to begin using PATS. Once you have the URL, you can enter the items using the PATS Maintenance option. The table below summarizes the data you need to update. This is followed by detailed steps for the maintenance process.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Patient Rep Tables</strong></th>
<th><strong>PATS Table</strong></th>
<th><strong>Comment/Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Service/discipline</td>
<td>Facility Service or Section</td>
<td><ul>
<li><p>Patient Rep items are inactivated when migrated.</p></li>
<li><p>Reactivate items and/or enter new items.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Hospital Location</td>
<td>Hospital Location</td>
<td><ul>
<li><p>Patient Rep items are inactivated when migrated.</p></li>
<li><p>Reactivate items and/or enter new items.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td>Comp (Service Recovery)</td>
<td><em>Optional: Populate table</em></td>
</tr>
<tr class="even">
<td></td>
<td>Boilerplate Resolution Text</td>
<td><em>Optional: Populate table</em></td>
</tr>
</tbody>
</table>

> Complete the following table maintenance tasks:

1.  Prior to making PATS available to the first site in a VISN, the VISN Patient Advocate Coordinator (VPAC) must enter or reactivate entries in the Facility Service or Section table for that VISN.
2.  Prior to making PATS available to each site, the Patient Advocate for that site must enter or reactivate entries in the Hospital Location table. Stations that award Comps (Service Recovery) or use canned Resolution Text will want to populate the Comps and Boilerplate Resolution Text tables.

> For detailed information about populating reference tables, refer to the *PATS User Guide, Chapter 6, Maintenance*.

3.  View several ROCs and verify that the data is accurate.
4.  Make sure that the IRM staff has given users access to PATS (see the *PATS Installation Guide for IRM Staff*).

# Appendix A - Correcting Data Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: Patient Advocate)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you run the CHK option described in *Chapter 2, Cleaning the Data*, you must correct the errors or the data will not migrate into PATS. This section describes the possible errors you might see on the error reports for each data field and offers guidelines for correcting the data.

## General Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The same error checks are done when running the pre-migration error reports as when moving the data to the staging area.

> Errors in the ROCs are listed in a ROC error report by ROC number. Errors on Referenced Files appear in a Reference File error report under separate headings for each Referenced File. Most errors can be corrected using Patient Rep. Some errors may need special handling and are noted in the ‘In case of error’ column (i.e., using VA FileMan to make the correction).

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 50%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Notes</strong></th>
<th><blockquote>
<p><strong>In case of error</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Free Text</strong></td>
<td><ul>
<li><p>Fields can contain all printable keyboard characters except “<strong>^</strong>”.</p></li>
<li><p>Data must be no longer than the maximum length allowed by the FileMan data dictionary.</p></li>
</ul></td>
<td><ul>
<li><p>Edit the field and re-enter or delete the text (if not required).</p></li>
<li><p>If the field contains control characters, the global may need to be manually edited by</p></li>
</ul>
<blockquote>
<p>IRM staff.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Date</strong></td>
<td><ul>
<li><p>Date must be valid in standard FileMan format. YYYMMDD where YYY is the number of years since 1700 (e.g. Dec 31,</p></li>
</ul>
<blockquote>
<p>2002 = 3021231).</p>
</blockquote></td>
<td>Edit or delete the date (if not required).</td>
</tr>
<tr class="odd">
<td><strong>Pointer Fields</strong></td>
<td><ul>
<li><p>Must point to a valid entry in the pointed- to file.</p></li>
</ul></td>
<td><ul>
<li><p>Edit the field.</p></li>
<li><p>Even if it appears correct, re- enter the value so that FileMan repeats the lookup on</p></li>
</ul>
<blockquote>
<p>the pointed-to file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Word Processing Fields</strong></td>
<td><ul>
<li><p>Each individual global node must not exceed a maximum of 256 characters.</p></li>
<li><p>Data must contain only alphanumeric or punctuation characters.</p></li>
</ul></td>
<td>Edit the field. If it contains control characters, the global may need to be manually edited by IRM staff.</td>
</tr>
<tr class="odd">
<td><strong>Set of Codes</strong></td>
<td><ul>
<li><p>Unless otherwise noted, the code must be a member of the valid set from the FileMan data dictionary.</p></li>
</ul></td>
<td>Edit the data to choose a valid code.</td>
</tr>
<tr class="even">
<td><strong>Number</strong></td>
<td><ul>
<li><p>Fields must contain only numeric values.</p></li>
<li><p>Fields must meet the criteria in the FileMan data dictionary.</p></li>
</ul></td>
<td>Edit the field and re-enter or delete the value.</td>
</tr>
</tbody>
</table>

## Specific Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tables describe the fields in greater detail.

### Consumer Contact (745.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,.01</td>
<td><blockquote>
<p>Contact Number</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=14)</p></li>
<li><p>Checks to make sure record has a non-null ROC number and at least one other field in the 0 node. If not, the record is deleted from the Consumer Contact file and no error is displayed.</p></li>
<li><p>If ROC number is not in the format: ###(0-3)ALPHA<strong>.</strong>#########, or if the station number (the 3 digits before the ‘.’) is not valid, ‘<em>ROC number is not correctly formatted</em>’ is displayed.</p></li>
<li><p>ROC Number will be converted from SSS.YYNNNN to SSS.YYYYNNNN<strong>N</strong>, where SSS=station number, YY=fiscal year, and NNNN=sequential counter in PATS.</p></li>
</ul>
<blockquote>
<p><em>Note: The fiscal year is now 4 digits rather than 2 (YYYY instead of YY); the sequential counter is 5 digits rather than 4 digits (NNNNN instead of NNNN).</em></p>
</blockquote>
<ul>
<li><p>If there are duplicate ROC numbers, the first ROC will be moved to the staging area (as long as it has no errors). Subsequent duplicates are reported as</p></li>
</ul>
<blockquote>
<p>errors: ‘<em>[ROC number] [IEN] is a duplicate ROC number.’</em></p>
</blockquote></td>
<td>Delete the ROC or edit the ROC number directly using FileMan.</td>
</tr>
<tr class="even">
<td>745.1,1</td>
<td><blockquote>
<p>Date of Contact</p>
</blockquote></td>
<td><ul>
<li><p>Field type: date.</p></li>
<li><p>This field must be non-null or else the error ‘<em>DATE OF CONTACT is missing</em>’ is displayed.</p></li>
<li><p>Standard date checks and conversions are done. If not valid, the error ‘<em>DATE OF CONTACT’ is invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Delete the ROC or edit the Date of Contact using FileMan.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,2</td>
<td><blockquote>
<p>Patient name</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Can be null. If not null, it must point to a valid entry in the Patient file, or else the error ‘<em>PATIENT pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If data associated with the patient is invalid, an error will be displayed (see individual patient data fields below), and the ROC will also be in error: ‘<em>PATIENT has invalid data—see ref data report.</em>’</p></li>
</ul></td>
<td><ul>
<li><p>If the PATIENT pointer is invalid, edit the ROC using FileMan and select a different patient.</p></li>
<li><p>You may also need to edit the Eligibility Status and Category fields for the ROC.</p></li>
<li><p>If the Patient has invalid data, consult Medical Administration Service (MAS) or</p></li>
</ul>
<blockquote>
<p>Registration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>745.1,6</td>
<td><blockquote>
<p>Eligibility Status</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>Text is taken from the ROC, not from current Patient data during migration.</p></li>
<li><p>Standard checks are done for a text field. If an error is found, the message ‘<em>Eligibility Status is Invalid</em>’ is displayed.</p></li>
</ul></td>
<td><ul>
<li><p>Select a different Primary Eligibility Code for the ROC using FileMan. If necessary, consult MAS or Registration to find out what the Primary Eligibility</p></li>
</ul>
<blockquote>
<p>Code should be.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>745.1,7</td>
<td><blockquote>
<p>Category</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>Text is taken directly from the ROC, not from current Patient data during migration.</p></li>
<li><p>Standard checks are done for a text field. If an error is found, ‘<em>CATEGORY (current means test) Invalid</em>’ is displayed.</p></li>
</ul></td>
<td><ul>
<li><p>Consult MAS or Registration to get the Current Means Test value corrected, or</p></li>
<li><p>Select a different Means Test value for the patient using FileMan to edit the</p></li>
</ul>
<blockquote>
<p>Category field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>745.1,8</td>
<td><blockquote>
<p>Information Taken By</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>If both this field and Entered By are null, the error ‘<em>INFO TAKEN BY and ENTERED BY are both NULL</em>’ is displayed.</p></li>
<li><p>If Information Taken By is null, it is set equal to Entered By. If not null, must be a valid pointer to the NEW PERSON file (200), else the error ‘<em>INFO TAKEN BY pointer is invalid</em>’ is displayed.</p></li>
<li><p>If data associated with the info taker is invalid, an error will be displayed, and the ROC will also be in error: ‘<em>INFO TAKER has invalid data—see USER on ref data</em></p></li>
</ul>
<blockquote>
<p><em>report.</em>’</p>
</blockquote></td>
<td><ul>
<li><p><em>INFO TAKEN BY and ENTERED BY are both NULL</em>: Edit the ROC, enter a value in the Info Taken By field.</p></li>
<li><p><em>INFO TAKEN BY pointer is invalid</em>: Edit the ROC to choose a different person.</p></li>
<li><p><em>INFO TAKER has invalid data—see USER on ref data report</em>: see individual</p></li>
</ul>
<blockquote>
<p>user data fields.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,9</td>
<td><blockquote>
<p>Entered By</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>If this field and Information Taken By are both null, the error ‘<em>INFO TAKEN BY and ENTERED BY are both NULL</em>’ is displayed.</p></li>
<li><p>If Entered By is null, it is set equal to Information Taken By. If not null, it must be a valid pointer to the NEW PERSON file (200) or else the error ‘<em>ENTERED BY pointer is invalid</em>’ is displayed.</p></li>
<li><p>If data associated with the Entered By person is invalid, an error will be displayed and the ROC will also be in error: ‘<em>ENTERED BY has invalid data—</em></p></li>
</ul>
<blockquote>
<p><em>see USER on ref data report.</em>’</p>
</blockquote></td>
<td><ul>
<li><p><em>‘INFO TAKEN BY and ENTERED BY are both NULL</em>:<em>’</em> Enter a value in the Info Taken By field.</p></li>
<li><p><em>‘ENTERED BY pointer is invalid</em>:<em>’</em> Edit the ROC using FileMan to choose a different person.</p></li>
<li><p><em>‘ENTERED BY has invalid data—see USER on ref data report</em>:<em>’</em> See individual</p></li>
</ul>
<blockquote>
<p>user data fields.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>745.1,10</td>
<td><blockquote>
<p>Name of Contact</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>Normal checks for a text field are done. Errors generate the message: ‘<em>NAME OF</em></p></li>
</ul>
<blockquote>
<p><em>CONTACT. too long or contains control character</em>s.’</p>
</blockquote></td>
<td>Edit the field.</td>
</tr>
<tr class="odd">
<td>745.1,11</td>
<td><blockquote>
<p>Telephone No. of Contact</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>Normal checks for a text field are done. Errors generate a message saying ‘<em>TELEPHONE NO. too long or contains</em></p></li>
</ul>
<blockquote>
<p><em>control characters.</em>’</p>
</blockquote></td>
<td>Edit the field.</td>
</tr>
<tr class="even">
<td>745.1,12</td>
<td><blockquote>
<p>Contact Made By</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If the contacting entity is null or does not match a code in the set, it is changed to</p></li>
</ul>
<blockquote>
<p>“10” (Other) in PATS.</p>
</blockquote></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>745.1,13</td>
<td><blockquote>
<p>Source of Contact (Method of Contact)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>Can be null.</p></li>
<li><p>If the source of contact does not match one of the codes in the set, the message</p></li>
</ul>
<blockquote>
<p>‘<em>SOURCE OF CONTACT is invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the ROC and choose a valid code or delete the existing entry.</td>
</tr>
<tr class="even">
<td>745.1,14</td>
<td><blockquote>
<p>Location of Event</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Can be null. If not null, this must be a valid pointer to the HOSPITAL LOCATION file (44). Otherwise, the error <em>‘LOCATION OF EVENT pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If the Issue Codes in the ROC are inactive, the Hospital Location name is put into the Resolution Text when the</p></li>
</ul>
<blockquote>
<p>ROC is migrated into PATS.</p>
</blockquote></td>
<td>Delete the field from the ROC or choose a different Hospital Location.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,16.5</td>
<td><blockquote>
<p>Treatment Status</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If the Treatment Status is null or does not match one of the codes in the set and there is a pointer to patient data, the Treatment Status value is set to ‘Not Registered at Site’ in PATS.</p></li>
<li><p>If there is no patient involved, the Treatment Status value is set to ‘No Patient Associated’ in PATS.</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>745.1,17</td>
<td><blockquote>
<p>Employee (multiple)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Can be null. If not null, must be a valid pointer to the NEW PERSON file. Otherwise, the error ‘<em>EMPLOYEE pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If the Issue Codes in the ROC are inactive, the employee name is put into the Resolution Text when the ROC is</p></li>
</ul>
<blockquote>
<p>migrated into PATS.</p>
</blockquote></td>
<td>Delete the field from the ROC or choose a different employee.</td>
</tr>
<tr class="odd">
<td>745.1,21</td>
<td><blockquote>
<p>Issue Codes (multiple)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Cannot be null. Must be a valid pointer to the CONTACT ISSUE CODE (745.2) file. Otherwise, the error ‘<em>Issue Code pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If the Date of Contact is after Fiscal Year 2003, there must be at least one valid entry in the Issue Codes multiple or the ROC will not migrate and the error ‘<em>ROC has no valid Issue Codes</em>’ is displayed.</p></li>
<li><p>If the CODE or NAME fields in the pointed-to entry are null, the error ‘<em>Issue Code or Issue Code Name NULL</em>’ is displayed.</p></li>
<li><p>If an Issue Code is inactive, the Issue Code and Name are put into the Resolution Text when the ROC is</p></li>
</ul>
<blockquote>
<p>migrated into PATS.</p>
</blockquote></td>
<td><ul>
<li><p><em>‘Issue Code pointer nnn is invalid:’</em> Choose a different issue code.</p></li>
<li><p><em>‘ROC has no valid Issue Code:’</em> Create at least one Issue Code for the ROC.</p></li>
<li><p><em>‘Issue Code or Issue Code Name NULL:’</em> Edit the CONTACT ISSUE CODE file entry.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.121,3</td>
<td><blockquote>
<p>Service/ Discipline (Facility Service or Section)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Can be null. If not null, must be a valid pointer to the QAC SERVICE/ DISCIPLINE (745.55) file. Otherwise, the error ‘<em>SERVICE/ DISCIPLINE pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If NAME field in file 745.55 is too long, the error <em>SERVICE/DISCIPLINE on issue SC01 invalid -- see ref data report</em>.</p></li>
<li><p>If the Issue Codes in the ROC are inactive, the service/discipline name is put into the Resolution Text when the ROC is</p></li>
</ul>
<blockquote>
<p>migrated into PATS.</p>
</blockquote></td>
<td><ul>
<li><p>For invalid pointer error, delete the field from the ROC or choose a different service/discipline.</p></li>
<li><p>For NAME field errors, edit the entry in the SERVICE/ DISCIPLINE file.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>745.1,22</td>
<td><blockquote>
<p>Issue Text</p>
</blockquote></td>
<td><ul>
<li><p>Field type: word processing.</p></li>
<li><p>Standard checks are done for a word- processing field. If errors are found, the message ‘<em>Issue Text node ‘n’ too long or contains invalid characters</em>’ is displayed. If the total length of the issue text is greater than 4000 characters, the overflow is moved to the end of the resolution comments.</p></li>
<li><p>If the Issue Text is null, the text ‘No data present in this field during migration from Patient Rep. Text required for closed ROCs in PATS’ will be inserted into the</p></li>
</ul>
<blockquote>
<p>issue text field in PATS. No error is displayed.</p>
</blockquote></td>
<td><em>‘Issue Text node ‘n’ too long or contains invalid characters’</em>: Edit the text as needed.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,25</td>
<td><blockquote>
<p>Resolution Comments</p>
</blockquote></td>
<td><ul>
<li><p>Field type: word processing.</p></li>
<li><p>Standard checks are done for a word- processing field. If errors are found in a single node, ‘<em>Resolution Text node ‘n’ too long or contains invalid characters</em>’ is displayed.</p></li>
<li><p>If the Resolution Text is longer than 8000 characters, you will get the error <em>‘Resolution Text=n char (8000 maximum).’</em></p></li>
<li><p>If the total length of the issue text is greater than 4,000 characters, the overflow is moved to the end of the resolution comments. If this makes the text too long, the error message will contain the additional words ‘<em>overflow issue text.’</em></p></li>
<li><p>If there is data in the REFER CONTACT TO multiple field (28), the NAME field from the pointed-to entries in the NEW PERSON file (200) is moved to the end of the resolution text. If the text is too long, the error message will contain the additional words ‘<em>Refer to.’</em></p></li>
<li><p>If the issue codes are inactive, the issue code multiple information (issue code, hospital location, employee and service/discipline) is moved to the end of the resolution text. If this makes the text too long, the error message will contain</p></li>
</ul>
<blockquote>
<p>the additional words <em>‘issue code data.’</em></p>
</blockquote></td>
<td><ul>
<li><p>Edit the text as needed.</p></li>
<li><p>If the text is too long, you will need to condense it.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>745.1,26</td>
<td><blockquote>
<p>Date Resolved</p>
</blockquote></td>
<td><ul>
<li><p>Field type: date.</p></li>
<li><p>Can be null. If not null and not a valid</p></li>
</ul>
<blockquote>
<p>date, error ‘<em>DATE RESOLVED is invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Re-enter the date.</td>
</tr>
<tr class="odd">
<td>745.1,27</td>
<td><blockquote>
<p>Status</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If not set to ‘O’ (open) or ‘C’ (closed) the</p></li>
</ul>
<blockquote>
<p>error ‘<em>STATUS not set to either Open or Closed</em>’ is displayed.</p>
</blockquote></td>
<td>Use the Open/Close/Delete Contact Record option to set the status.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,29</td>
<td><blockquote>
<p>Congressional Contact</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>Can be null. If not null, this must be a valid pointer to the Congressional Office file (745.4). Otherwise, the error ‘<em>CONGRESSIONAL CONTACT pointer nnn is invalid</em>’ is displayed.</p></li>
<li><p>If there is an error in the referenced Congressional Office entry, the error ‘<em>CONGRESSIONAL CONTACT contact_name invalid see ref data report’</em></p></li>
</ul>
<blockquote>
<p>is displayed.</p>
</blockquote></td>
<td><ul>
<li><p>For the invalid pointer error, delete or re- enter the data.</p></li>
<li><p>For errors in the Congressional Contact, see the ref data report, and edit the Congressional Contact as needed.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>745.1,30</td>
<td><blockquote>
<p>Source(s) of Contact (Method of Contact)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>Can be null.</p></li>
<li><p>If the source of contact does not match one of the codes in the set, the message ‘<em>SOURCE(S) OF CONTACT are invalid</em>’</p></li>
</ul>
<blockquote>
<p>is displayed.</p>
</blockquote></td>
<td>Edit the ROC and choose a valid code or delete the existing entry.</td>
</tr>
<tr class="odd">
<td>745.1,37</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>If the Division points to an entry that is not in the list of valid entries from the MEDICAL CENTER DIVISION file, the error ‘<em>DIVISION pointer nnn not in MEDICAL CENTER DIVISION file’ is displayed.</em></p></li>
<li><p>If entry is not a valid pointer, or the pointed-to INSTITUTION file entry has nothing in the STATION NUMBER field, the error ‘<em>DIVISION</em> pointer <em>nnn is invalid or has no Station number</em>’ is displayed.</p></li>
<li><p>If null, Station number is extracted from the ROC number. If this does not match an entry in the STATION NUMBER field of an entry on the Institution File (4), the error ‘<em>DIVISION is missing</em>’ is displayed.</p></li>
<li><p>If the division is not on the central list of national institutions used by the PATS application, you will see the error: <em>DIVISION nnn is not a valid national station</em></p></li>
</ul></td>
<td><ul>
<li><p>‘<em>DIVISION pointer nnn not in MEDICAL CENTER DIVISION file.’ Edit the ROC to choose a new division.</em></p></li>
<li><p><em>DIVISION pointer nnn is invalid or has no Station number.’</em> Edit the ROC to choose a new division, or edit the Institution file entry to add a Station number.</p></li>
<li><p><em>‘DIVISION is missing.’</em> Edit the ROC number to start with a valid Station number.</p></li>
<li><p>‘<em>DIVISION nnn is not a valid national station.’</em> You must either change the division on the ROC, or contact Central Office to get the division added to the</p></li>
</ul>
<blockquote>
<p>national table.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>745.1, 41</td>
<td><blockquote>
<p>Roll-up Status</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If this field is set to 3, a value of 1 (ready to roll up) is migrated to PATS.</p></li>
</ul>
<blockquote>
<p>Otherwise, a value of 0 is migrated.</p>
</blockquote></td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1,43</td>
<td><blockquote>
<p>Internal Appeal</p>
<p>(Clinical Appeal)</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If set to ‘Y’, 1 is migrated (‘true’) to PATS, otherwise 0 (‘false’) is migrated.</p></li>
</ul></td>
<td>N/A</td>
</tr>
</tbody>
</table>

> *Contact Issue Code (745.2)*

> No entries are migrated.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.2</td>
<td><blockquote>
<p>none</p>
</blockquote></td>
<td><blockquote>
<p>A nationally-maintained ISSUE_CODE table replaces this file and is pre-populated</p>
<p>on the PATS server from the existing national Contact Issue Code entries.</p>
</blockquote></td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Congressional Office (745.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All entries are migrated, even if not pointed-to by a ROC.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.4,.01</td>
<td><blockquote>
<p>Office Name</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=60)</p></li>
<li><p>Cannot be null.</p></li>
<li><p>Regular checks for text data type are done.</p></li>
<li><blockquote>
<p>If any errors occur, the error ‘<em>Office or Person Name Invalid</em>’ is displayed.</p>
</blockquote></li>
</ul></td>
<td>Edit the Office Name using FileMan.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.4,1</p>
</blockquote></td>
<td><blockquote>
<p>Inactive</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If set to 1 (inactive), the inactivation data is set when the entry is migrated into PATS.</p></li>
<li><p>If flag is anything other than null, 0 or 1,</p></li>
</ul>
<blockquote>
<p>the error ‘<em>Inactive Flag is invalid’</em> is displayed</p>
</blockquote></td>
<td>Edit the Inactive field using FileMan.</td>
</tr>
</tbody>
</table>

### Contact Discipline (745.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No entries are migrated.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name [type]</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.5</td>
<td><blockquote>
<p>none</p>
</blockquote></td>
<td><blockquote>
<p>A new ISSUE CODE CATEGORY table replaces this file and is pre-populated on the server using information provided by the</p>
<p>user group.</p>
</blockquote></td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Qac Service/Discipline (745.55)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All entries referenced by at least one ROC within an active Issue Code are migrated to the Facility Service or Section (FSoS) table in PATS. All entries are inactivated after being migrated into PATS. Patient Advocates must either activate or enter new FSoSs to be used for new ROCs.

> Note: If a ROC has inactive issue codes, the associated service/discipline entries are not migrated into the FSoS table. Instead, the inactive issue code and the name of the service/discipline are moved into the Resolution Text of the migrated ROC.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.55,01</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=50)</p></li>
<li><p>Regular checks for text data type are done. If errors occur, the message ‘<em>FSOS_NAME – Name Invalid</em>’ is displayed, where FSOS_NAME is the name of the service/discipline. Note that the maximum length is 30 characters in</p></li>
</ul>
<blockquote>
<p>Patient Rep, but can be up to 50 in PATS.</p>
</blockquote></td>
<td>Edit the entry in this file or choose a different service/discipline in the ROCs that reference it.</td>
</tr>
</tbody>
</table>

### Customer Service Standard (745.6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No entries are migrated.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.6</td>
<td><blockquote>
<p>none</p>
</blockquote></td>
<td><blockquote>
<p>A new ISSUE CODE CATEGORY table replaces this file and is pre-populated on the</p>
<p>server using information provided by the user group.</p>
</blockquote></td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Patient (2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All entries referenced by at least one ROC are migrated. If errors are displayed, either ask MAS Personnel to correct the Patient data or edit the ROC using FileMan to reference a different patient.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2,.001</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td><blockquote>
<p>Field type: number.</p>
</blockquote></td>
<td>No checks are done; no errors are displayed.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Integration Control Number</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=29)</p></li>
<li><p>Must be null, or both the ICN and the ICN checksum must be numeric. ‘<em>ICN invalid</em>’ is displayed.</p></li>
</ul></td>
<td>A valid ICN must be assigned to the patient.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><ul>
<li><p>Retrieves name components from file 20, last name (max=35), first name (max=25), middle name (max=25), prefix (max=10), suffix (max=10) and degree (max=10).</p></li>
<li><p>Field type.</p></li>
<li><p>Each name component is checked like any normal text field.</p></li>
<li><p>Last name and first name cannot be null.</p></li>
<li><p>If any errors are found, ‘<em>Name Invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the patient’s Name.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Sex</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If not equal to M or F, ‘<em>Gender Invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the patient’s Sex.</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Date of Birth</p>
</blockquote></td>
<td><ul>
<li><p>Field type: date.</p></li>
<li><p>If not a valid date, ‘<em>Date of Birth Invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the patient’s Date of Birth.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text.</p></li>
<li><p>Must be a 9-digit number, followed optionally by ‘P’.</p></li>
<li><p>If not valid, ‘<em>SSN invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the patient’s Social Security Number.</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Primary Eligibility Code</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>If pointer value on patient’s PRIMARY ELIGIBILITY CODE field is invalid, error ‘<em>Primary Eligibility Code Pointer Invalid’</em> is displayed</p></li>
<li><p>Standard checks are done for a text field.</p></li>
</ul>
<blockquote>
<p>If an error is found, ‘<em>Primary Eligibility Code Invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the patient’s Primary Eligibility Code.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Enrollment Priority</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes</p></li>
<li><p>Can be null.</p></li>
<li><p>Retrieves the ENROLLMENT PRIORITY based on the current enrollment for this patient. If an error is found, ‘<em>Current Enrollment Priority</em></p></li>
</ul>
<blockquote>
<p><em>Invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the patient’s current enrollment.</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Period of Service</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>If pointer value on patient’s PRIMARY ELIGIBILITY CODE field is invalid, error ‘<em>Period of Service Pointer Invalid’</em> is displayed</p></li>
<li><p>Standard checks are done for a text field.</p></li>
</ul>
<blockquote>
<p>If an error is found, ‘<em>Period of Service Invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the patient’s Period of Service or the referenced entry in the Period of Service file.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Is Service Connected</p>
</blockquote></td>
<td><ul>
<li><p>Field type: set of codes.</p></li>
<li><p>If not equal to 0 or 1, ‘<em>Is Service Connected Flag Invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the patient’s ‘Is Service Connected’ flag.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Service Connected Percent</p>
</blockquote></td>
<td><ul>
<li><p>Field type: number.</p></li>
<li><p>Can be null.</p></li>
<li><p>If not an integer between 0 and 100, ‘<em>Service Connected % Invalid</em>’ is</p></li>
</ul>
<blockquote>
<p>displayed.</p>
</blockquote></td>
<td>Edit the patient’s service- connected percent.</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Current Means Test Status</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>Can be null.</p></li>
<li><p>If pointer value on patient’s CURRENT MEANS TEST STATUS field is invalid, error ‘<em>Current Means Test Status Pointer Invalid’</em> is displayed</p></li>
<li><p>Standard checks are done for a text field. If an error is found, ‘<em>Current Means Test</em></p></li>
</ul>
<blockquote>
<p><em>Status Invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the patient’s current means test status.</td>
</tr>
</tbody>
</table>

### Hospital Location (44)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All entries referenced by the LOCATION OF EVENT field in at least one ROC with at least one active Issue Code are migrated. If errors are displayed, either edit the HOSPITAL LOCATION file or edit the ROC to reference a different location.

> All entries are inactivated after being migrated into PATS. Patient Advocates must activate and/or enter new hospital locations to be used for new ROCs.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><ul>
<li><p>Field type: free text. (max=30)</p></li>
<li><p>If null, ‘<em>LOCATION OF EVENT Name field is NULL.</em>’</p></li>
<li><p>Standard checks are done for a text field. If an error is found, ‘<em>NAME is missing or</em></p></li>
</ul>
<blockquote>
<p><em>invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the Name field.</td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>Institution</p>
</blockquote></td>
<td><ul>
<li><p>Field type: pointer.</p></li>
<li><p>If null, the Station number for the institution in the QUALITY ASSURANCE SITE PARAMETERS FILE is passed and no error is displayed.</p></li>
<li><p>If this pointer to the INSTITUTION file is invalid, or if the pointed-to institution has no STATION NUMBER field, ‘<em>Hospital Location Name – has no STATION NUMBER</em>’ is displayed.</p></li>
<li><p>If the division is not on the central list of national institutions used by the PATS application, you will see the error: <em>NNN is not a valid national station number.</em></p></li>
</ul></td>
<td><ul>
<li><p>‘<em>Hospital Location Name – has no STATION NUMBER.’</em> Edit the Hospital Location to point to another division, or edit the INSTITUTION file entry to add the station number.</p></li>
<li><p>‘<em>DIVISION nnn is not a valid national station.’</em> You must either change the division on the HOSPITAL LOCATION entry, or contact Central Office to get the division added to the national</p></li>
</ul>
<blockquote>
<p>table.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### New Person (200)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All entries referenced by either the INFORMATION TAKEN BY, ENTERED BY or EMPLOYEE (multiple) fields on at least one ROC with at least one active Issue Code are migrated. If errors are displayed, either ask IRM staff to edit the NEW PERSON file or edit the ROC to reference a different person.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Notes</strong></th>
<th><strong>In case of error</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10.1</td>
<td><blockquote>
<p>Name Components</p>
</blockquote></td>
<td><ul>
<li><p>Retrieves name components from file 20, last name (max=35), first name (max=25), middle name (max=25), prefix (max=10), suffix (max=10) and degree (max=10).</p></li>
<li><p>Field type: free text.</p></li>
<li><p>Each name component is checked like any normal text field.</p></li>
<li><p>Last name and first name cannot be null.</p></li>
<li><p>If any errors are found, ‘<em>Name Invalid</em>’ is displayed.</p></li>
</ul></td>
<td>Edit the Name field.</td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>Title</p>
</blockquote></td>
<td><ul>
<li><p>Can be null.</p></li>
<li><p>Field type: free text. (Extracts first 30 characters)</p></li>
<li><p>Migrated only for Employees Involved in an ROC.</p></li>
<li><p>If pointer value to TITLE file is invalid, error ‘<em>Title Pointer Invalid’</em> is displayed</p></li>
<li><p>Standard checks are done for a text field.</p></li>
</ul>
<blockquote>
<p>If an error is found, ‘<em>Title invalid</em>’ is displayed.</p>
</blockquote></td>
<td>Edit the individual’s title.</td>
</tr>
<tr class="odd">
<td>28</td>
<td><blockquote>
<p>Mail Code</p>
</blockquote></td>
<td><ul>
<li><p>Can be null.</p></li>
<li><p>Field type: free text. (Extracts first 10 characters.)</p></li>
<li><p>Migrated only for Employees Involved in an ROC.</p></li>
<li><p>Standard checks are done for a text field. If an error is found, ‘<em>Mail Code invalid</em>’ is</p></li>
</ul>
<blockquote>
<p>displayed.</p>
</blockquote></td>
<td>Edit the individual’s mail code.</td>
</tr>
</tbody>
</table>

# Appendix B - Data Migration Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: Patient Advocate)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix describes the Data Migration reports. You can access the report menu from either the Pre-Migration Data Cleanup menu (PRDC) *or* the Patient Rep Migration Steps menu (PRDM) by selecting RPTS.

> Note: One month after all of the data migration steps on the VistA-side have been completed, the data used to generate the Data Migration reports will be deleted and these reports will not be available.

## RPTS – Report Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are five types of reports you can run from the data cleanup menus and from the Migration Steps Menu. You can re-run these reports as often as necessary.

> Select Main Menu for Pre-Migration Data Cleanup Option: RPTS \[Enter\] Data Migration Reports

> DERR Reprint Migration/Pre-Migration Data Errors Report

> ALST Reprint All ROCs that were Auto-Closed

> CNG System Generated Changes to ROCs for Migration CNT Count of Errors, Ready to Migrate, Migrated STAT Display Migration Status for a ROC

> <span id="B.2__DERR" class="anchor"></span>NOT Pending Notifications Report

## DERR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option reprints the error reports that were last generated by either the CHK or MSTG option.

- CHK: checks for data errors and generates two error reports: *Data Cleanup – Ref Table Data Errors* and *Data Cleanup – ROC Errors*.
- MSTG: moves the data to the staging area in preparation for final migration. It generates the same error checks and builds the same error reports as CHK, but with different headers (*Move to Staging Area – Ref Table Data Errors* and *Move to Staging Area – ROC Errors*).

> See *Appendix A, Correcting Data Errors* for a detailed list of all fields, possible error messages you might see on reports and tips on correcting errors.

## ALST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option reprints the list of ROCs that were auto-closed when the CLS option was run—*Auto-Closed ROCs*. The list displays the ROC number and the date the ROC was auto-closed. It also prints a short descriptive message if any null field within a ROC record was replaced with some other value. The following table explains the messages that might appear.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><blockquote>
<p><strong>Change Made</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Entered By</td>
<td><blockquote>
<p>The ENTERED BY field was set equal to the value in the INFORMATION TAKEN BY field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Info Taken By</td>
<td><blockquote>
<p>The INFORMATION TAKEN BY field was set equal to the value in the ENTERED BY field.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Division</td>
<td><blockquote>
<p>The DIVISION field was set to the institution based on the first part of the ROC number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Issue Text</td>
<td><blockquote>
<p>The field was set to "This ROC was auto-closed prior to migration to PATS."</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Resolution Text</td>
<td><blockquote>
<p>The field was set to "This ROC was auto-closed prior to migration to PATS."</p>
</blockquote></td>
</tr>
</tbody>
</table>

## CNG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report details any ROCs that were changed by the system when the data was moved to the staging area during the MSTG process, *ROCs With Data Changed for Migration*. The changes were made in the staging area itself and not in the Patient Rep files. The report shows the ROC number and a message describing the change that was made. The following table describes the types of changes that could be displayed.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Change Reported</strong></th>
<th><blockquote>
<p><strong>Change Made</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Issue Text</td>
<td><blockquote>
<p>ISSUE TEXT was null and will be replaced with the text “No data present in this field during migration from Patient Rep. Text required for closed ROCs in</p>
<p>PATS.”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Info Taken By</td>
<td><blockquote>
<p>INFORMATION TAKEN BY was null and will be replaced with the ENTERED BY name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Entered By</td>
<td><blockquote>
<p>ENTERED BY was null and will be replaced with the INFORMATION TAKEN BY name.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Division</td>
<td><blockquote>
<p>The DIVISION field was null and will be replaced with the institution based on the first part of the ROC number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Issue Text Overflow</td>
<td><blockquote>
<p>The ISSUE TEXT was longer than 4,000 characters. The overflow text will be moved to the Resolution Text.</p>
<p><em>Note: If this causes Resolution Text to be more than 8,000 characters, it will appear on the error report.</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## CNT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a status of data in the staging area and counts of data in each step of the migration process. There are two status messages for data in the staging area:

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Status of data to be migrated to PATS</strong></th>
<th><strong>Message that appears in the report</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>No data ready to be migrated</p>
</blockquote></td>
<td><blockquote>
<p> No data in staging area </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Data has been moved to the staging area and is ready to be migrated.</p>
</blockquote></td>
<td><blockquote>
<p> Data has been moved to the staging area and is ready to migrate to PATS </p>
</blockquote></td>
</tr>
</tbody>
</table>

> This report displays the total number of ROCs in the ROC file. For each of the Patient Rep files to be migrated, the report also displays counts of the following:

- Items ready to be migrated (i.e., in the staging area)
- Items that have been successfully migrated
- Items that have errors

## STAT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows a user to select a ROC and displays the current status of that ROC online. The table explains ROC status messages:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Status Reported</strong></th>
<th><blockquote>
<p><strong>Meaning</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This ROC has errors</td>
<td><blockquote>
<p>This ROC has errors that prevent it from migrating</p>
<p>into PATS. Check the ROC error report that you previously generated to see the errors.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>This ROC is in the staging area ready to migrate</td>
<td><blockquote>
<p>You ran the step that moves data into the staging area ready to be migrated into PATS (see Chapter 3), but have not yet migrated the data (see Chapter 4).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>This ROC has been successfully migrated into</p>
<p>PATS</p></td>
<td><blockquote>
<p>You ran the final step to migrate data into the PATS system (see Chapter 4). This ROC was successfully</p>
<p>migrated into the new PATS system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>No action has been taken for this ROC</td>
<td><blockquote>
<p>Either:</p>
</blockquote>
<ul>
<li><blockquote>
<p>You have not started the migration process.</p>
</blockquote></li>
<li><p>ROC has no errors and you have not yet moved data to the staging area.</p></li>
<li><blockquote>
<p>ROC was entered into the Patient Rep system after the migration process was started.</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Note:</strong> If you already moved the data to the staging area, or you already completed the migration into PATS, then this ROC may have been entered into Patient Rep after the migration was completed. You can repeat the migration steps in Chapters 1 – 4 to</p>
<p>migrate the ROC into PATS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## NOT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a report of all pending notifications, including the ROC number, sender, recipient, date sent and the notification message *(Pending Notifications)*. Pending Notification information does not get migrated into the PATS system. Patient Advocates can try to resolve pending notifications prior to migration or send a new notification from PATS after migration.

# Appendix C - Deleting Migrated Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## (Role Performing Task: PATS Migration Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix describes how to delete data that was previously migrated to PATS. Deleting data and starting the data migration process over rarely happens. The decision to perform this operation should be made only after agreement between the PIO, the PATS Migration Manager<span id="C.1__Starting_Over" class="anchor"></span> and the EIE Data Manager.

## Starting Over

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There may be situations when you want to perform the data migration over from the beginning. For example:

> After migrating some or all of the data into PATS, you find you have a large number of ROCs that have invalid data—such as a reference to the wrong Institution. The PATS Migration Manager and the EIE Data Manager both feel that the data should have been corrected in Patient Rep before it was migrated. The managers decide to redo the migration process.

> To re-start the data migration process to PATS, complete the following tasks:

1.  Delete all of the site’s data from the PATS database following the procedures in this Appendix.
2.  Correct data errors in Patient Rep following the procedures in Chapter 2 of this guide.
3.  Migrate data from Patient Rep to PATS following the procedures in Chapters 3 and 4.

## Deleting Data from the PATS Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PATS Migration Manager uses the Data Migration application to delete data from the PATS database for the selected institution or multi-divisional site. When you use the delete data option, it also automatically deletes VistA’s temporary lists of data migrated from Patient Rep into PATS.

#### CAUTION! If the site has already started entering new data using PATS, the new data will be deleted along with the legacy data from Patient Rep.

> To delete the migrated data from the PATS application:

4.  Open a browser window and enter the URL for the PATS Data Migration application that you received from the PIO.
5.  Enter your Access and Verify codes for the institution from which you want to delete data.
6.  From the drop down list, select the institution from which you want to delete data.
7.  Click Logon.
8.  From the menu on the left, select Delete Institution Data.

> *Result: You should see the Institution number representing the data that will be deleted from the PATS Oracle database.*

9.  Click Delete.

> *Result: You will receive a warning that you are about to delete the data for the selected Institution.*

10. Click OK to confirm that you wish to delete the data. If you selected this option in error, click CANCEL and the data will not be deleted.

> *Result: The browser will display a confirmation that the request to delete the data has been submitted successfully.*

11. Click the “<u>View the migration report</u>” message.

> *Result: The browser displays a report showing the status of the current data deletion, followed by a history of all of the other PATS data migration/deletion operations for this institution.*

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](pats-data-migration-guide/005.png)</p>
</blockquote></th>
<th>After you click on the link to view the report, it may appear that nothing has happened. If two institutions delete or migrate their data about the same time, the second institution request is put in a queue. If your institution is the second request, the confirmation will not appear in your report until the first institution’s migration has completed. You can come back to the data migration application at a later time to check the status. You do not need to run the data deletion again.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Note: This process may take several minutes to finish, depending on the amount of data being deleted. The migration report page will refresh every 10 seconds to display the current status of the deletion. You can safely close your browser, or you can leave it open to track the status.

12. When the data is completely deleted, the first entry on the report page will show that the data was deleted successfully.

> Once you have deleted the migrated data from PATS, correct the errors in Patient Rep (see

> *Chapter 2*) and then migrate the data to PATS (*Chapters 3 − 4*).

# Appendix D - Technical Information for Maintenance and Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix includes technical details about data migration. It is not written for the end-user; the intended audience is maintenance developers and other support staff.

## Verifying that Data Migration was Successful

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EIE Manager or the Database Administrator at the EIE can verify that a data migration of an institution’s data was successful. When the Project Implementation Office notifies the EIE that an institution has completed a data migration, the following steps can be taken to verify the migration.

1.  Log on as the PATS user or the SYS DBA.
2.  Execute the following SQL statement to see the data migration history for the institution. This will show either that the migration completed successfully or that an error occurred.

> SELECT \* FROM PATS.DMLOG WHERE STATIONNUMBER = ‘NNN’;

> (NNN is the station number of the institution whose migration you are checking.)

3.  You can also execute the following SQL statement to make sure that ROCs have migrated from the site.

> SELECT COUNT(\*) ROC_COUNT FROM PATS.REPORT_OF_CONTACT WHERE ROC_NUMBER LIKE ‘NNN%’;

> (NNN is the station number of the institution whose migration you are checking. ROC_COUNT should be a large number. If you want to check with the site, ROC_COUNT should be close to the number of ROCs that the sites VistA CNT report shows. The EIE count may be less than the institutions count in an integrated site, because the older ROC numbers may begin with a different station number.)

## Use of the ^XTMP global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ^XTMP global is used to store information during the data migration process. Each time the user runs either the pre-migration data cleaning report, the option to auto-close ROCs, or the option to move the legacy data to the staging area in preparation for migration, the automatic purge date for this global is set to 30 days from the current date. Thus, each step in data migration resets this date, so the data is not purged until 30 days from the last time any data migration step is performed

> Note: The file_code subscript in the nodes described below can be set to HL (hospital location), USER (employee involved or entered by), PT (patient), CC (congressional contact), EMPINV (employee involved), FSOS (facility service or section, i.e., service/discipline) or ROC (Report of Contact).

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Temporary Global Name</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^XTMP(“QACMIGR”,0)</td>
<td><blockquote>
<p>Holds the purge date and the date a data migration step was last performed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>^XTMP(“QACMIGR”,”STDINSTITUTION”)</td>
<td><blockquote>
<p>Holds the list of all national station numbers that start with the 3-digit default institution number. This is the list downloaded from Oracle when you run the PATS Download to VistA application prior to data cleanup (see Chapter 1).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>^XTMP(“QACMIGR”,”AUTO”,”C”)</td>
<td><blockquote>
<p>Holds a list of ROC numbers for ROCs that were automatically closed by the auto-close option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>^XTMP(“QACMIGR”,file_code,”E”)</td>
<td><blockquote>
<p>Holds error information generated either when the pre-migration data cleaning report is run, or when data is moved to the staging area ready for migration. Used to create the error reports and to prevent data with errors from migrating.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>^XTMP(“QACMIGR”,file_code,”U”)</td>
<td><blockquote>
<p>Holds data ready to be migrated. This is where the ‘staging area’ data is held.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>^XTMP(“QACMIGR”,”ROC”,”C”)</td>
<td><blockquote>
<p>Holds information about any changes that will be made to fill in null data when a ROC is migrated.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>^XTMP(“QACMIGR”,file_code,”D”)</td>
<td><blockquote>
<p>Holds a list of data items that have been successfully migrated into PATS. This contains the key value for the field on the VistA side (usually the IEN), and the key value in the associated PATS Oracle Table (usually the ID).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Downloaded List of National Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Download to VistA (DV) application downloads the list of national division station numbers whose first three digits match the 3-digit station number of the DEFAULT INSTITUTION in the VistA KERNEL SITE PARAMETERS file (see Chapter 1). The list is retrieved from the Oracle SDSADM.STD_INSTITUTION table at the EIE and is stored in

> ^XTMP(“QACMIGR”,”STDINSTITUTION”,station_number). It is used to verify that pointers from the VistA data to the local INSTITUTION file are valid (i.e., they are in the list of nationally recognized station numbers). If not, they are reported by the CHK error report and you must either change the division on the Patient Rep data shown in the error report or contact Central Office to have the division added to the National table.

## Option QACI PREMIGRATION ERROR REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Checking Code

> The error checking option CHK uses exactly the same error checking code as the option that moves data to the staging area MSTG. The code reads through every ROC record on the VistA system. It also checks all records that are referenced (pointed-to) by the ROC, if the referenced record is part of the data that will be migrated to PATS. Each time the error checking option is run, the old list of errors is deleted then rebuilt so that it always reflects current errors.

#### Errors stored in ^XTMP global

> ROC errors are recorded in ^XTMP(“QACMIGR”,”ROC”,”E”,rocno,n) where n is a sequential number, and rocno is the ROC number in the old Patient Rep format SSS.YYNNNN, followed by a single space in order to sort the ROC numbers correctly. (SSS is the station number, YY is the last 2 digits of the fiscal year, NNNN is a 4-digit sequential number.)

> Errors in reference tables are recorded in ^XTMP(“QACMIGR”,file_code,”E”,ien,n) where file_code is HL, USER, PT, CC, EMPINV, FSOS or ROC, ien is the internal entry number of the record with the error and n is a sequential number. For example, if the file_code is “CC”, then ien is the internal entry number of a record in the CONGRESSIONAL OFFICE file 745.4.

> The error nodes in the ^XTMP global are used both to keep data from migrating, and to generate the error reports.

## Option QACI AUTO CLOSE ROCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option reads through all records on the CONSUMER CONTACT file 745.1. Any CONSUMER CONTACT record (ROC) that has the STATUS field set to O (open), and that has a DATE OF CONTACT that is prior to the beginning of the previous quarter, based on the date that the option is run, will be auto-closed (i.e., STATUS will be set to C (closed)).

#### An ROC will not be auto-closed when:

- ROC Number is NULL or Date of Contact is NULL.
- ROC has errors found when the Error Check routine was run – i.e.,

> \$D(^XTMP("QACMIGR","ROC","E",ROCNO\_" ")) is true, where ROCNO

> contains the ROC number in Patient Rep format (SSS.YYNNNN).

- ROC has already been migrated to the PATS system – i.e.,

> \$D(^XTMP("QACMIGR","ROC","D",CONVROC)) is true, where CONVROC

> contains the ROC number in PATS format (SSS.YYYYNNNNN).

- Station Number is invalid. The code first tries to extract the pointer from file 745.1, field 37, or if that is null, takes the first “.” Piece of the ROC number and converts it to a pointer by calling \$\$LKUP^XUAF4. It then retrieves the STATION NUMBER field from file 4 by calling \$\$STA^XUAF4.
- Both the INFORMATION TAKEN BY field and the ENTERED BY field are null.
- The DATE OF CONTACT is in FY 2004 or later, and there are no ISSUE CODES for the ROC (i.e., no entries in multiple field 21).

#### Changes made to the ROC in file 745.1 when it is auto-closed:

- Status is set to C (closed)
- If the ISSUE TEXT field 22 is null, it is replaced by the canned text No data present in this field during migration from Patient Rep. Text required for closed ROCs in PATS.
- If the INFORMATION TAKEN BY field 8 is null, it is replaced by the value from the ENTERED BY field 9.
- If the ENTERED BY field 9 is null, it is replaced by the value from the INFORMATION TAKEN BY field 8
- If the DIVISION field is null, the code takes the first “.” Piece of the ROC number and uses it in a call to LKUP^XUAF4 to return the pointer value, then updates the DIVISION field with the pointer value.

#### Auto-closed data stored in ^XTMP global

> ^XTMP(“QACMIGR”,”AUTO”,”C”,ROCNO\_” “) is set to the date closed, followed by flags indicating whether any of the data fields mentioned in the previous section were changed by the auto-close. In this global, ROCNO is the ROC number in Patient Rep format. This information is used to generate the report of all ROCs that were auto-closed.

## Option QACI MIGRATION DATA BUILD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option moves the data to the staging area in preparation for migrating it to PATS. This option uses exactly the same error checking code as the error checking option described in section

> *9.2 Option QACI PREMIGRATION ERROR REPORT*.

> The code reads through every record in the CONSUMER CONTACT file (745.1). It also checks all records that are referenced (pointed-to) by the ROC, if the referenced record is part of the data that will be migrated to PATS. If errors are found on a ROC, that ROC will not be moved to the staging area, and will not be migrated into the PATS system. If errors are found on a referenced record, none of the ROCs that reference that record will be migrated into the PATS system.

> The migration process takes all data from the staging area and none from the production data files.

#### Data to be migrated stored in ^XTMP global

> Data that is error free and ready to migrate is stored in the *staging area* in the ^XTMP global.

#### ROC data

> ^XTMP(“QACMIGR”,”ROC”,”U”,rocno,n) where n is a sequential number, and rocno is the ROC number in the new PATS format SSS.YYYYNNNNN, followed by a single space in order to sort the ROC numbers correctly. (SSS is the station number, YYYY is the 4 digit fiscal year, NNNNN is a 5 digit sequential number.)

> The MAIN (first) node for a ROC contains the following up-arrow delimited pieces:

1.  ROC Number in new PATS format SSS.YYYYNNNNN (ex. 442.200500483)
2.  “MAIN”
3.  Date of Contact in format MM/DD/YYYY
4.  Patient IEN (DFN)
5.  Information Taken By IEN
6.  Entered By IEN
7.  Treatment Status (ID in Oracle treatment_status table – This is static because the referenced table is loaded during the installation of PATS)
8.  Congressional Contact (external NAME field from 745.4)
9.  ROC Status (O (open) or C (closed))
10. Station number
11. Resolution Date in format MM/DD/YYYY
12. Name of Contact (phone/fax)
13. Telephone No. of Contact
14. Contacting Made By (ID in Oracle contacting_entity table – This is static because the referenced table is loaded during the installation of PATS)
15. Internal Appeal (1 (true), 0 (false))
16. Eligibility Status (free-text taken directly from record in file 745.1)
17. Category (current means test, free-text taken directly from record in file 745.1)
18. Roll-up Status (1 (select during next rollup) or 0 (do not select for next rollup))

> Followed by one or more Issue Text records with the following format:

1.  ROC Number in new PATS format SSS.YYYYNNNNN (ex. 442.200500483)
2.  “ITXT”
3.  Issue Text (from a single node of the FileMan word-processing field)

> Followed by 0 or more Resolution Text records with the following format:

1.  ROC Number in new PATS format SSS.YYYYNNNNN (ex. 442.200500483)
2.  “RTXT”
3.  Resolution Text (from a single node of the FileMan word-processing field)

> Note that the resolution text may include overflow issue text, Refer To names and inactive Issue Codes with their associated Service/Discipline, Employee and Hospital Location.

> Followed by 0 or more Issue Code records with the following format:

1.  ROC Number in new PATS format SSS.YYYYNNNNN (ex. 442.200500483)
2.  “ISS”
3.  Issue code
4.  Service/Discipline (Facility service or section) name
5.  Employee IEN (from file 200)
6.  Location of Event (Hospital location name)
7.  Station number for hospital location

> Followed by 0 or more Source(s) of Contact records with the following format:

1.  ROC Number in new PATS format SSS.YYYYNNNNN (ex. 442.200500483)
2.  “MOC”
3.  Source(s) of Contact ID(s) delimited by “^” (ID(s) in Oracle method_of_contact table – These are static because the referenced table is loaded during the installation of PATS.)

#### Additional technical notes on data error checking and conversions

> Note: Details on most error checking and data conversions can be found in the *Patient Advocate Tracking System (PATS) Data Migration Guide,* in Appendix A – Correcting Data Errors

#### Text Fields

> All text fields are checked to make sure that the ASCII value of each character is greater than 31 and less than 127.

#### Date Fields

> Date fields are converted from FileMan internal format to MM/DD/YYYY.

> Note: Because Contacting Entity, Method of Contact and Treatment Status table entries are populated during the installation of PATS, the ID values are static. In the staging area, the set of code values in VistA are changed to the internal Oracle id values as described below.

#### Contacting Entity mapping (In Patient Rep this was Contact Made By)

| Patient Rep                                   | PATS ID/value                              |
|---------------------------------------------------|------------------------------------------------|
| PA – Patient                                      | 1 Patient                                      |
| RE – Relative                                     | 2 Relative                                     |
| FR – Friend                                       | 3 Friend                                       |
| CO – Congressional                                | 4 Congressional                                |
| VH – VISN/HQ                                      | 5 VISN/HQ                                      |
| VO – Veterans Service Organization                | 6 Veterans Service Organization                |
| AT – Attorney/Legal Guardian/Conservator/ Trustee | 7 Attorney/Legal Guardian/Conservator/ Trustee |
| DI – Director’s Office                            | 8 Director’s Office                            |

| ST – Staff – VAMC     | 9 Staff – VAMC |
|-----------------------|----------------|
| OT – Other            | 10 Other       |
| Null or invalid entry | 10 Other       |

> Method of Contact mapping (In Patient Rep this was Source Of Contact and Source(s) Of Contact)

| Patient Rep | PATS ID/value |
|-----------------|-------------------|
| L – Letter      | 4 Letter          |
| W – Ward Visit  | 2 Visit           |
| V – Visit       | 2 Visit           |
| P – Phone       | 1 Phone           |
| S – Survey      | 5 Survey          |
| I – Internet    | 3 Internet        |

> If the SOURCE OF CONTACT field is invalid, an error is generated. If it’s null, no action is taken, because this is an obsolete field.

> If .01 field in SOURCE(S) OF CONTACT is invalid or null, an error is generated.

#### Treatment Status Mapping

> Note that in the new PATS system, there are just 5 active entries 1 Outpatient, 2 Inpatient, 3 Long Term Care, 4 Not Registered at Site and 5 No Patient Associated. No treatment status values from migrated ROCs reference these new active treatment statuses:

| Patient Rep                  | PATS ID/value                                |
|----------------------------------|--------------------------------------------------|
| I – Inpatient                    | 6 Pat Rep – Inpatient (inactivated)              |
| O – Outpatient                   | 7 Pat Rep – Outpatient (inactivated)             |
| D – Domiciliary                  | 8 Pat Rep – Domiciliary (inactivated)            |
| N – NHCU                         | 9 Pat Rep – NHCU (inactivated)                   |
| L – Long Term Psych              | 10 Pat Rep – Long Term Psych (inactivated)       |
| E - Extended/Intermed. Care      | 11 Pat Rep – Extend/Intermed. Care (inactivated) |
| H – HBHC                         | 12 Pat Rep – HBHC (inactivated)                  |
| Null or invalid, ROC has patient | 4 Not Registered at site                         |
| Null or invalid, no patient      | 5 No Patient Associated                          |

#### Issue Code

> The list of valid, national issue codes is built into the Oracle issue_code table for PATS during the deployment of the PATS application. This same list is hard-coded into the data migration routines. Issue codes on a ROC that appear on this list will be migrated to the

> roc_issue table, along with the associated SERVICE/DISCIPLINEs (facility_service_or_section), LOCATION OF EVENT and EMPLOYEEs. Any other issue codes on a ROC will be considered to be local or inactive. Local or inactive issue code information, along with the associated SERVICE/DISCIPLINEs (facility_service_or_section), LOCATION OF EVENT and EMPLOYEEs data, is copied into the Resolution Text on the migrated ROC and is not moved into the roc_issue table.

## Migrating the Data to PATS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Order of Installation

> During migration, the data is inserted into the tables in the following order:

1.  hospital_location
2.  pats_user (Information Takers and Entered By)
3.  pats_patient
4.  congressional_contact
5.  pats_user (Employee Involved)
6.  facility_service_or_section (Service/Discipline)
7.  ROC data for each ROC is installed in the order:
    1.  report_of_contact
    2.  roc_phone_fax
    3.  roc_contacting_entity
    4.  roc_issue
    5.  roc_method_of_contact

#### Reference Table Data – Additional technical details

> During migration into the PATS Oracle tables, all of the reference table data is inserted prior to inserting the ROCs.

> All foreign keys referencing institutions or divisions will reference the Standard Data Services table std_institution in the SDSADM schema. The VISN and default institution Server station numbers for the institution being migrated are passed from VistA. A lookup is done on the sdsadm.std_institution table to get the internal ID values for each of the institutions. These are used for foreign key fields in tables referencing an institution.

#### Hospital Location

> At the users request, entries in the HOSPITAL LOCATION file (#44) that are referenced by at least one ROC will be migrated into PATS, but will be inactivated (i.e., the inactivation date will be set to the date that the migration occurs). The users have asked to maintain their own Hospital Location data, separate from the VistA data. So before using the PATS system, they will need to either re-activate or add new entries to the

> PATS Hospital_location table. After the migration, there is no link between the VistA HOSPITAL LOCATION file and the PATS hospital_location table.

#### PATS User

- Data from the INFORMATION TAKEN BY, ENTERED BY and EMPLOYEE field are all loaded into the pats_user table.
- The User Identifier is built in the Oracle procedure, using the server station number and the IEN from the VistA NEW PERSON file entry. This is used as a unique identifier for an entry in the table. This is identical to the KAAJEE user identifier.
- If the entry came from the EMPLOYEE field, the TITLE and MAIL CODE are passed from VistA.
- A placeholder has been left for the future National Patient Identifier field.

#### PATS Patient

- The IEN for the patient on the VistA PATIENT file 2 is brought over in the data to be migrated and stored in the Oracle table. The combination of IEN and Institution_fk is used as a unique identifier for an entry in the pats_patient table.
- The institution_fk field references the default institution.
- The foreign key referencing ethnicity references the Standard Data Services table std_ethnicity in the SDSADM schema.
- The foreign key referencing race, in the pats_patient_race table, references the Standard Data Services table std_race in the SDSADM schema. A patient can have multiple races.
- The Integration Control Number is stored on the pats_patient table.

#### Facility Service or Section

> For each VISN, one new entry is added to this table with the name Not Reported in Patient Rep. Because PATS requires that each issue code have at least one FSOS associated with it, any migrated ROC that had issues with no Service/Discipline associated will have the facility_servsect_fk set to reference this Not Reported in Patient Rep entry.

#### ROC – Additional technical details

1.  Report_of_contact table

> Foreign Key fields: During migration into the PATS Oracle tables, all of the reference tables are populated prior to populating the ROCs. External key values for most reference table data associated with an individual ROC are passed with that ROC’s data in the ^XTMP global as described above. While inserting a ROC, the code does lookups on the reference tables to find matches to the external key value for any reference data associated with that ROC. This identifier field for the

> entry in the reference table is then used to populate the foreign key value in the ROC.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Fields in Report of Contact Table</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Institution_fk</strong></td>
<td>The station number associated with an individual ROC is used to lookup an entry on the sdsadm.std_institution table. The ID from the std_institution table is stored as the foreign key field.</td>
</tr>
<tr class="even">
<td><strong>Patient_fk</strong></td>
<td>The default institution ID and the IEN for the patient associated with a ROC are used to look up an entry on the pats_patient table. The ID from the pats_patient table is the foreign key value stored in the patient_fk field.</td>
</tr>
<tr class="odd">
<td><strong>Info_taken_by_user_fk, Entered_by_fk</strong></td>
<td><p>The KAAJEE User Identifier is built, using the server station number and the IEN from the NEW PERSON file. This is used to lookup an entry in the pats_user table. The ID from the</p>
<p>pats_user table is stored as the foreign key field.</p></td>
</tr>
<tr class="even">
<td><strong>Congressional_contact_fk</strong></td>
<td><p>The default institution ID and the congressional contact name are used to lookup an entry on the congressional_contact table. The ID from the congressional_contact table is stored as the</p>
<p>foreign key field.</p></td>
</tr>
<tr class="odd">
<td><strong>Resolution_text1, Resolution_text2</strong></td>
<td><p>The individual resolution text nodes from the migrated data are appended together into VARCHAR fields. The first 4000 characters will go into resolution_text1. If there are more than 4000 characters, the overflow goes into</p>
<p>Resolution_text2.</p></td>
</tr>
</tbody>
</table>

2.  ROC_Contacting_Entity table

> In PATS, there can be multiple Contacting Entities for a single ROC. For this reason, the single CONTACT MADE BY entry migrated with a ROC is added to the separate roc_contacting_entity table.

> Since contacting entities are pre-loaded into PATS, the ID fields are static, so the contacting entity id is passed with the migrated ROC data, and becomes the foreign key field contacting_entity_fk.

3.  ROC_Issue table

> In the PATS system, one entry is created in the roc_issue table for each unique combination of an ISSUE CODE, SERVICE/DISCIPLINE, EMPLOYEE and LOCATION OF EVENT from Patient Rep.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Fields in Report of Contact Table</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Issue_code_fk</strong></td>
<td>The issue code is the key field on the PATS issue_code table, and is stored as the foreign key field in the roc_issue table.</td>
</tr>
<tr class="even">
<td><strong>Hospital_Location_fk</strong></td>
<td>The local institution (division) station number associated with a hospital location used to do a lookup on the sdsadm.std_institution table. The resulting division ID field and the hospital location name are used to look up the entry on the PATS hospital_location table. The ID from the hospital_location table in stored as the foreign key field.</td>
</tr>
<tr class="odd">
<td><strong>Facility_ServSect_fk</strong></td>
<td><p>The VISN institution station number and the service/section name are used to look up the entry on the PATS facility_service_or_section table. The resulting ID is stored as the foreign</p>
<p>key field .</p></td>
</tr>
<tr class="even">
<td><strong>Employee_involved_fk</strong></td>
<td>The KAAJEE User Identifier is built, using the server station number and the IEN from the NEW PERSON file. This is used to lookup an entry in the pats_user table. The ID from the pats_user table is stored as the foreign key field.</td>
</tr>
</tbody>
</table>

4.  ROC_Method_of_Contact

> The SOURCE OF CONTACT and SOURCE(S) OF CONTACT entries are added to the roc_method_of_contact table.

> Since methods of contact are pre-loaded into PATS, the ID fields are static, so the method of contact id is passed with the migrated ROC data, and becomes the foreign key field method_of_contact_fk.

5.  ROC_Phone_Fax

> In PATS, there can be multiple phone/fax values for contacting the person who made the complaint. The NAME OF CONTACT and TELEPHONE NO. OF CONTACT entries are added to the roc_phone_fax table.

## Description of Migration Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The PATS data migration application makes multiple calls to VistA Remote Procedures using VistALink, to retrieve data from the staging area in the ^XTMP global, into a Java array.
- The retrieved array data is passed to various methods in the Oracle package pkg_load_legacy_data, depending on the table being updated.
- Each Oracle procedure returns an array to the data migration application, containing an indicator of the table being updated and a list of value pairs consisting of a key value from the VistA data and the resulting key value in the Oracle table for each record successfully migrated.
- This array is passed back to VistA on the subsequent VistALink call, and is stored in the ^XTMP global as described above. This list is used to track the entries for each table that have been successfully migrated.

## Troubleshooting Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PATS data migration process has been designed so that any data on from VistA that might cause errors when being loaded in the Oracle tables is not migrated. However it is possible that an error might occur.

#### Troubleshooting an error

1.  Consult the logs. In most cases you will see an Oracle error that includes the name of the table and the IEN of the record that was being updated when the error occurred. In the case of ROC data errors, the error message will usually also say what field caused the error. Example *ORA-20011: User Last Name: OSBORNE8999999 IEN:1370 was not updated. Error ORA-06502: PL/SQL: numeric or value error: character string buffer too small...* The logs will also contain the Java stack trace information.
2.  Check the record at the VistA site to determine what is wrong with the data. You can also check the data in the staging area in the ^XTMP global described above.
3.  The data migration code either in Oracle, or in VistA may need to be corrected to catch some type of data error that it is not currently catching.
4.  The data migration code in Oracle is in the package pkg_load_legacy_data, as described in detail above.
5.  The data migration code that moves data to the staging area in VistA is in the QAC2\* namespace.
6.  In the meantime, in order to allow the site to continue with their migration, have them correct the error in the VistA data, then repeat the migration steps, starting from the step of moving the data to the staging area. This will not cause any problems--records that have successfully migrated will not migrate again.

#### Migrating the same VistA data into two Oracle Databases

> The EIE may want to migrate a sites VistA data into a test Oracle database prior to loading it into the production database. To do that, perform the following steps.

7.  Follow all of the steps to migrate the data to the test database as described in the

> *Patient Advocate Tracking System (PATS) Data Migration Guide*

8.  Change the properties in the file gov.va.med.pats.migration.db.oracle.properties that is currently pointing to the test database, to the values of the production database in order to re-point to the production database. Redeploy the PATS Data Migration application.
9.  The person doing data migration at the site logs on to the PATS Data Migration Application, and runs the option to Delete All Data for the site, as described in *Appendix C – Deleting Migrated Data* of the *Patient Advocate Tracking System (PATS) Data Migration Guide*
10. There will be no data deleted from the Oracle database, since the site has not yet migrated their data to this database, however the information in the VistA database will be re-set to look as if migration has not yet been performed (i.e., the data in the ^XTMP global as described above).
11. The person doing data migration at the site repeats the migration steps, starting from the step of moving the data to the staging area, to migrate the VistA data into the production database.

## Patient Representative to PATS Data Migration Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This table shows the mapping of fields from Patient Rep to PATS. If data isn’t migrated, PATS data is not applicable. Blank cells are intentional.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>QA Site Parameters 740</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>740,.01</td>
<td>Name</td>
<td>Pointer to Institution file #4 (default Institution at Site)</td>
<td>Y</td>
<td>Institution_FK</td>
<td>Foreign Key Referencing SDSADM.STD_INSTI TUTION</td>
<td>PATS_Patient, PATS_User, Congressional_contact,</td>
</tr>
<tr class="odd">
<td><p>PARENT^XUAF4</p>
<p>(Passing value in 740,.01)</p></td>
<td>Name</td>
<td>Pointer to Institution file #4 (VISN Institution)</td>
<td>Y</td>
<td>VISN_FK</td>
<td>Foreign Key Referencing SDSADM.STD_INSTI TUTION</td>
<td>Facility_Service_or_Secti on</td>
</tr>
<tr class="even">
<td><strong>Consumer Contact 745.1</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 01</td>
<td>Contact Number</td>
<td>String (10 - 14)</td>
<td>Y</td>
<td>ROC_Number</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 1</td>
<td>Date of Contact</td>
<td>Fileman Date format</td>
<td>Y</td>
<td>Date_of_Contact</td>
<td>Oracle Date format</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 2</td>
<td>Patient Name</td>
<td>Pointer to Patient file #2</td>
<td>Y</td>
<td>Patient_FK</td>
<td>Foreign Key (References PATS_Patient)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 3</td>
<td>SSN</td>
<td>Computed, uses pointer to Patient file</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 4</td>
<td>DOB</td>
<td>Computed, uses pointer to Patient file</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1,5</td>
<td>Sex</td>
<td>Computed, uses pointer to Patient file</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 6</td>
<td>Eligibility Status</td>
<td>String, Originally Extracted from file 8</td>
<td>Y</td>
<td>Eligibility_Status</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 7</td>
<td>Category</td>
<td>String, Originally Comes from Patient Current Means Test Status</td>
<td>Y</td>
<td>Category</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1, 8</td>
<td>Information Taken By</td>
<td>Pointer to New Person file #200</td>
<td>Y</td>
<td>Info_Taken_By_User_FK</td>
<td>Foreign Key (References PATS_User)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 9</td>
<td>Entered By</td>
<td>Pointer to New Person file #200</td>
<td>Y</td>
<td>Entered_By_User_FK</td>
<td>Foreign Key (References PATS_User)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 10</td>
<td>Name of Contact</td>
<td>String</td>
<td>Y</td>
<td>Name_or_Description</td>
<td>String</td>
<td>ROC_Phone_Fax</td>
</tr>
<tr class="even">
<td>745.1, 11</td>
<td>Telephone No. of Contact</td>
<td>String</td>
<td>Y</td>
<td>Phone_Fax_Number</td>
<td>String</td>
<td>ROC_Phone_Fax</td>
</tr>
<tr class="odd">
<td>745.1, 12</td>
<td>Contact Made By</td>
<td>Set - array of values</td>
<td>Y</td>
<td>Contacting_Entity_FK (VISN-HQ is inactivated in PATS)</td>
<td>Foreign Key (References Contacting_Entity)</td>
<td>ROC_Contacting_Entity</td>
</tr>
<tr class="even">
<td>745.1, 13</td>
<td>Source of Contact</td>
<td>Set - array of values</td>
<td>Y</td>
<td><p>Method_of_Contact_FK ("Ward Visit" changed to</p>
<p>"Visit". If null or invalid, set to "Other")</p></td>
<td>Foreign Key (References Method_Of_Contact)</td>
<td>ROC_Method_of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 14</td>
<td>Location of Event</td>
<td>Pointer to Hospital Location file #44</td>
<td>Y</td>
<td>Hospital_Location_FK</td>
<td>Foreign Key (References Hospital_Location)</td>
<td>ROC_Issue</td>
</tr>
<tr class="even">
<td>745.1, 15</td>
<td>Service Involved</td>
<td></td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 16</td>
<td>Category of Care</td>
<td></td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 16.5</td>
<td>Treatment Status</td>
<td>Set - array of values</td>
<td>Y</td>
<td><p>Treatment_Status_FK (If null and no patient, set to "No Patient Associated" If there is a patient, set to "Not Registered at Site".</p>
<p>All Patient Rep entries are inactivated in PATS)</p></td>
<td>Foreign Key (References Treatment_Status)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 17</td>
<td>Employee</td>
<td>* multiple</td>
<td>Y</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.117,.01</p>
</blockquote></td>
<td><blockquote>
<p>Employee</p>
</blockquote></td>
<td>Pointer to New Person file #200</td>
<td>Y</td>
<td>Employee_Involved_FK</td>
<td>Foreign Key (References PATS_User)</td>
<td>ROC_Issue</td>
</tr>
<tr class="odd">
<td>745.1, 18</td>
<td>Refer to</td>
<td></td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 19</td>
<td>Date Sent</td>
<td>Date</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1, 20</td>
<td>Days Response Expected By</td>
<td>Number</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1,20.1</td>
<td>Date Due</td>
<td>Computed date</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 21</td>
<td>Issue Codes</td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.121.01</p>
</blockquote></td>
<td><blockquote>
<p>Issue Codes</p>
</blockquote></td>
<td>Pointer to Contact Issue Code file #745.2</td>
<td>Y</td>
<td>Issue_Code_FK</td>
<td>Foreign Key (References Issue_Code)</td>
<td>ROC_Issue</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.121,1</p>
</blockquote></td>
<td><blockquote>
<p>Serv/Sect Involved</p>
</blockquote></td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.1211,.01</p>
</blockquote></td>
<td>Serv/Sect Involved</td>
<td>Pointer to Service/Section file #49</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.121,2</p>
</blockquote></td>
<td>Disciplines Involved</td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.1212,.01</p>
</blockquote></td>
<td>Disciplines Involved</td>
<td>Pointer to Contact Disciplines file #745.5</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.121,3</p>
</blockquote></td>
<td><blockquote>
<p>Service/Discipline</p>
</blockquote></td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.1213,.01</p>
</blockquote></td>
<td><blockquote>
<p>Service/Discipline</p>
</blockquote></td>
<td>Pointer to QAC Service/Discipline file #745.55</td>
<td>Y</td>
<td>Facility_ServSect_FK</td>
<td>Foreign Key (References Facility_Service_or_S ection</td>
<td>ROC_Issue</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.1213,1</p>
</blockquote></td>
<td>Discipline</td>
<td>Pointer to Contact Disciplines file #745.5</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 22</td>
<td>Issue Text</td>
<td>Word-Processing</td>
<td>Y</td>
<td>Issue_Text</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 23</td>
<td>Report of Contact Generated</td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 24</td>
<td>QM Involvement</td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.124,.01</p>
</blockquote></td>
<td><blockquote>
<p>QM Involvement</p>
</blockquote></td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 25</td>
<td>Resolution Comments</td>
<td>Word-Processing</td>
<td>Y</td>
<td>Resolution_Text1, Resolution_Text2</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 26</td>
<td>Date Resolved</td>
<td>Date</td>
<td>Y</td>
<td>Date_Closed</td>
<td>Date</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 27</td>
<td>Status</td>
<td>Set - array of values</td>
<td>Y</td>
<td>Status</td>
<td>Char</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 28</td>
<td>Refer Contact To</td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>745.128, .01</p>
</blockquote></td>
<td><blockquote>
<p>Refer Contact To</p>
</blockquote></td>
<td>Pointer to New Person file #200</td>
<td>Y</td>
<td>Resolution_Text1, Resolution_Text2</td>
<td>String</td>
<td>Report_Of_Contact</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>745.1, 29</td>
<td>Congressional Contact</td>
<td>Pointer to Congressional Office file #745.4</td>
<td>Y</td>
<td><blockquote>
<p>Congressional_Contact_ FK</p>
</blockquote></td>
<td>Foreign Key (References Congressional_Conta ct)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 30</td>
<td>Source(s) of Contact</td>
<td>* multiple</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>745.11. .01</p>
</blockquote></td>
<td>Source(s) of Contact</td>
<td>Set - array of values</td>
<td>Y</td>
<td>Method_of_Contact_FK ("Ward Visit" changed to "Visit". If null or invalid, set to "Other")</td>
<td>Foreign Key (References Method_Of_Contact)</td>
<td>ROC_Method_of_Contact</td>
</tr>
<tr class="even">
<td>745.1, 31</td>
<td>Period of Service</td>
<td>Pointer to Period of Service file #21</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 32</td>
<td>Persian Gulf Service</td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 33</td>
<td>Refer to SEAT</td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 34</td>
<td>Date Resolved</td>
<td>Date</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 35</td>
<td>Days to Resolution</td>
<td>Number</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 36</td>
<td>Level of Satisfaction</td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 37</td>
<td>Division</td>
<td>Pointer to Institution file</td>
<td>Y</td>
<td>Institution_FK</td>
<td>Foreign Key (References SDSADM.STD_INSTI TUTION)</td>
<td>Report_Of_Contact</td>
</tr>
<tr class="odd">
<td>745.1, 38</td>
<td>Discipline</td>
<td>String</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 39</td>
<td>Resolved by SEAT</td>
<td>Set - array of values</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.1, 40</td>
<td>SEAT Resolution Comments</td>
<td>String</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.1, 41</td>
<td>Rollup Status</td>
<td>Set - array of values</td>
<td>Y</td>
<td>rollup_to_natl_reports_st atus (Set to 0 unless equal to 3 in Patient Rep, then set to 1)</td>
<td>Number - 0 or 1 (acts like boolean)</td>
<td>report_of_contact</td>
</tr>
<tr class="odd">
<td>745.1, 43</td>
<td>Internal Appeal</td>
<td>Set - array of values</td>
<td>Y</td>
<td>Is_Internal_Appeal (Set to 1 if YES, set to 0 otherwise)</td>
<td>Number - 0 or 1 (acts like boolean)</td>
<td>Report_Of_Contact</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Patient data - referenced by field 2 in file 745.1</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2,.001</td>
<td>NUMBER</td>
<td>VistA internal entry no.</td>
<td>Y</td>
<td>VistA_IEN</td>
<td>Number</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>GETICN^MPIF00 1</td>
<td>Integration Control Number</td>
<td>String</td>
<td>Y</td>
<td>Integration_control_numb er</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>HLNAME^XLFNA ME</td>
<td>Patient Name</td>
<td>Name Components - See file 20 below.</td>
<td>Y</td>
<td><p>Last_Name, First_Name, Middle_Name, Name_Prefix,</p>
<p>Name_Suffix, Academic_Degree</p></td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>DEM^VADPT</td>
<td>Sex</td>
<td></td>
<td>Y</td>
<td>Gender</td>
<td>Char</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>DEM^VADPT</td>
<td>Date of Birth</td>
<td>Date</td>
<td>Y</td>
<td>Date_of_Birth</td>
<td>Date</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>DEM^VADPT</td>
<td>SSN</td>
<td>String</td>
<td>Y</td>
<td>Social_Security_Number</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>DEM^VADPT</td>
<td>SSN (Pseudo SSn flag)</td>
<td>Single Character='P' if this is a pseudo SSN</td>
<td>Y</td>
<td>Is_Pseudo_SSN</td>
<td>Number - 0 or 1 (acts like boolean)</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>ELIG^VADPT</td>
<td>Eligibility Code</td>
<td>String</td>
<td>Y</td>
<td>Eligibility_Code</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>PRIORITY^DGE NA, EXTERNAL^DILF D</td>
<td>Enrollment Priority</td>
<td>String</td>
<td>Y</td>
<td>Enrollment_Priority</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>ELIG^VADPT</td>
<td>Period of Service</td>
<td>String</td>
<td>Y</td>
<td>Period_of_Service</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>ELIG^VADPT</td>
<td>Is Service Connected</td>
<td>Set of Codes (0=no,1=yes)</td>
<td>Y</td>
<td>Is_Service_Connected</td>
<td>Number - 0 or 1 (acts like boolean)</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td>ELIG^VADPT</td>
<td>Service Connected PerCent</td>
<td>Number</td>
<td>Y</td>
<td>Service_Connected_Perc ent</td>
<td>Number</td>
<td>PATS_Patient</td>
</tr>
<tr class="even">
<td>ELIG^VADPT</td>
<td>Current Means Test Status</td>
<td>String</td>
<td>Y</td>
<td>Category</td>
<td>String</td>
<td>PATS_Patient</td>
</tr>
<tr class="odd">
<td><strong>Contact Issue Code 745.2</strong></td>
<td></td>
<td></td>
<td>N</td>
<td><p>Replaced by table issue_code, populated</p>
<p>manually during installation of PATS</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>*Quality Matrix 745.3</strong></td>
<td></td>
<td></td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Congressional Office 745.4</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.4,.01</td>
<td>Office/Name</td>
<td>String</td>
<td>Y</td>
<td>Office_or_Person_Name</td>
<td>String</td>
<td>Congressional_Contact</td>
</tr>
<tr class="even">
<td>745.4,1</td>
<td>Inactive</td>
<td>Set - array of values</td>
<td>Y</td>
<td>Inactivation_Date (Set to date migrated if entry is inactive)</td>
<td>Date</td>
<td>Congressional_Contact</td>
</tr>
<tr class="odd">
<td><strong>Contact Discipline - 745.5</strong></td>
<td></td>
<td></td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>QAC Service Discipline 745.55</strong></td>
<td></td>
<td></td>
<td></td>
<td>All entries brought from Patient Rep are inactivated in PATS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.55,.01</td>
<td>Name</td>
<td>String</td>
<td>Y</td>
<td>Service_or_Section_Nam e</td>
<td>String</td>
<td>Facility_Service_or_Secti on</td>
</tr>
<tr class="even">
<td>745.55,1</td>
<td>Abbreviation</td>
<td>String</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>745.55,2</td>
<td>Discipline</td>
<td>String</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>745.55,3</td>
<td>Comment</td>
<td>String</td>
<td>N</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Customer Service Standards 745.6</strong></td>
<td></td>
<td></td>
<td>N</td>
<td><p>Replaced by table Issue_category, populated manually</p>
<p>during installation of PATS</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Hospital Location 44 - referenced by field 14 in file 745.1</strong></td>
<td></td>
<td></td>
<td></td>
<td>All entries brought from Patient Rep are inactivated in PATS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>44,.01</td>
<td>Name</td>
<td>String</td>
<td>Y</td>
<td>Location_Name</td>
<td>String</td>
<td>Hospital_Location</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA File, Field</strong></th>
<th><strong>VistA Field Name</strong></th>
<th><strong>VistA Field Description</strong></th>
<th><strong>Migrate?</strong></th>
<th><strong>PATS Data Item</strong></th>
<th><strong>Data Item Description</strong></th>
<th><strong>PATS Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name Components 20</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>20,1</td>
<td>Family (Last) Name</td>
<td>String</td>
<td>Y</td>
<td>Last_Name</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="odd">
<td>20,2</td>
<td>Given (First) Name</td>
<td>String</td>
<td>Y</td>
<td>First_Name</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="even">
<td>20,3</td>
<td>Middle Name</td>
<td>String</td>
<td>Y</td>
<td>Middle_Name</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="odd">
<td>20,4</td>
<td>Prefix</td>
<td>String</td>
<td>Y</td>
<td>Name_Prefix</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="even">
<td>20,5</td>
<td>Suffix</td>
<td>String</td>
<td>Y</td>
<td>Name_Suffix</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="odd">
<td>20,6</td>
<td>Degree</td>
<td>String</td>
<td>Y</td>
<td>Academic_Degree</td>
<td>String</td>
<td>PATS_User, PATS_Patient</td>
</tr>
<tr class="even">
<td><p><strong>New Person 200 (referenced by fields 8, 9 and</strong></p>
<p><strong>17 in 745.1)</strong></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>200,28</td>
<td>Mail Code</td>
<td>String</td>
<td>Y</td>
<td>Mail_Code</td>
<td>String</td>
<td>PATS_User</td>
</tr>
<tr class="even">
<td>200,8</td>
<td>Title</td>
<td>String</td>
<td>Y</td>
<td>Title</td>
<td>String</td>
<td>PATS_User</td>
</tr>
</tbody>
</table>