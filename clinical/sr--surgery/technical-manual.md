---
consolidated_title: "surgery technical manual/security guide change pages"
app_code: SR
doc_type: TM
master_source: "SR*3*184 Surgery Technical Manual/Security Guide Change Pages"
master_pub_date: November 2015
consolidated_from: 2 versions
prior_versions:
  - "SR*3*177 Surgery Technical Manual/Security Guide Change Pages"
---

# Surgery


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Surgery](#surgery)
  - [Version 3.0](#version-30)
  - [Revised November 2015](#revised-november-2015)
  - [Product Development](#product-development)
- [Introduction](#introduction)
- [Overview](#overview)
  - [Organization](#organization)
  - [Requesting and Scheduling](#requesting-and-scheduling)
  - [Tracking Clinical Procedures](#tracking-clinical-procedures)
  - [Generating Surgical Reports](#generating-surgical-reports)
  - [Chief of Surgery Reporting](#chief-of-surgery-reporting)
  - [Managing the Software Package](#managing-the-software-package)
  - [Assessing Surgical Risk](#assessing-surgical-risk)
  - [Assessing Surgical Transplants](#assessing-surgical-transplants)
  - [Documentation Conventions](#documentation-conventions)
  - [![](sr-3-184-surgery-technical-manual-security-guide-change-pages/002.png)![](sr-3-184-surgery-technical-manual-security-guide-change-pages/003.png)![](sr-3-184-surgery-technical-manual-security-guide-change-pages/004.png)Getting Help and Exiting](#sr-3-184-surgery-technical-manual-security-guide-change-pages002pngsr-3-184-surgery-technical-manual-security-guide-change-pages003pngsr-3-184-surgery-technical-manual-security-guide-change-pages004pnggetting-help-and-exiting)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [Installation](#installation)
- [Site Specific Parameters](#site-specific-parameters)
- [Files](#files)
- [File Descriptions](#file-descriptions)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Options Listed by Name](#options-listed-by-name)
- [Option Descriptions](#option-descriptions)
    - [Admissions w/in 14 days of Out Surgery if Postop Occ \[SROQADM\]](#admissions-win-14-days-of-out-surgery-if-postop-occ-sroqadm)
    - [Annual Report of Surgical Procedures \[SROARSP\]](#annual-report-of-surgical-procedures-sroarsp)
    - [Circulating Nurse Staffing Report \[SROCNR\]](#circulating-nurse-staffing-report-srocnr)
    - [Comparison of Preop and Postop Diagnosis \[SROPPC\]](#comparison-of-preop-and-postop-diagnosis-sroppc)
    - [Deaths Within 30 Days of Surgery \[SROQD\]](#deaths-within-30-days-of-surgery-sroqd)
    - [Delete or Update Operation Requests \[SRSUPRQ\]](#delete-or-update-operation-requests-srsuprq)
    - [Flag Drugs for Use as Anesthesia Agents \[SROCODE\]](#flag-drugs-for-use-as-anesthesia-agents-srocode)
    - [List Completed Cases Missing CPT Codes \[SRSCPT\]](#list-completed-cases-missing-cpt-codes-srscpt)
    - [List of Invasive Diagnostic Procedures \[SROQIDP\]](#list-of-invasive-diagnostic-procedures-sroqidp)
    - [List of Unverified Surgery Case \[SROUNV\]](#list-of-unverified-surgery-case-srounv)
    - [Make a Request from the Waiting List \[SRSWREQ\]](#make-a-request-from-the-waiting-list-srswreq)
    - [Morbidity & Mortality Reports \[SROMM\]](#morbidity-mortality-reports-sromm)
    - [Non-Operative Occurrences (Enter/Edit) \[SROCOMP\]](#non-operative-occurrences-enteredit-srocomp)
    - [Operating Room Information (Enter/Edit) \[SRO-ROOM\]](#operating-room-information-enteredit-sro-room)
    - [Report of Daily Operating Room Activity \[SROPACT\]](#report-of-daily-operating-room-activity-sropact)
    - [Report of Unscheduled Admissions to ICU \[SROICU\]](#report-of-unscheduled-admissions-to-icu-sroicu)
    - [Reschedule or Update a Scheduled Operation \[SRSCHUP\]](#reschedule-or-update-a-scheduled-operation-srschup)
    - [Schedule Unrequested Concurrent Cases \[SRSCHDC\]](#schedule-unrequested-concurrent-cases-srschdc)
    - [Surgeon's Verification of Diagnosis & Procedures \[SROVER\]](#surgeons-verification-of-diagnosis-procedures-srover)
    - [Surgery Risk Assessment - Site Update Server \[SROASITE\]](#surgery-risk-assessment-site-update-server-sroasite)
    - [Wound Classification Report \[SROWC\]](#wound-classification-report-srowc)
- [Templates](#templates)
- [Input Templates](#input-templates)
- [Sort Template](#sort-template)
- [Editing Input Templates](#editing-input-templates)
- [Globals in the Surgery Package](#globals-in-the-surgery-package)
- [Journaling Globals](#journaling-globals)
- [Archiving and Purging](#archiving-and-purging)
- [Archiving](#archiving)
- [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Packages Needed to Run Surgery](#packages-needed-to-run-surgery)
- [Calls Made by Surgery](#calls-made-by-surgery)
- [Database Integration Control Registrations](#database-integration-control-registrations)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Contingency Planning](#contingency-planning)
- [Interfacing](#interfacing)
- [Interface for Automated Anesthesia Systems](#interface-for-automated-anesthesia-systems)
- [Electronic Signatures](#electronic-signatures)
- [Menus](#menus)
- [Security Keys](#security-keys)
- [File Security](#file-security)
- [Glossary](#glossary)
- [Index](#index)
> Technical Manual/Security Guide
![](sr-3-184-surgery-technical-manual-security-guide-change-pages/001.png)

## Version 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> July 1993

## Revised November 2015

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Office of Information and Technology (OIT)

## Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Product Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the

> changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/15</td>
<td>All</td>
<td><blockquote>
<p>SR*3*184</p>
</blockquote></td>
<td><blockquote>
<p>Added the new routines, new files added by this patch, and updated Glossary page for the Abort definition.</p>
<p>Additions/removals necessitated a document reissue.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>09/14</td>
<td>i, 13, 72, 78</td>
<td><blockquote>
<p>SR*3*182</p>
</blockquote></td>
<td><blockquote>
<p>Removed the SURGERY DISPOSITION file (#131.6) from the list of files that can be maintained by sites.</p>
<p>Change SURGERON field (#.14) to “PRIMARY SURGEON”.</p>
<p>Updated the Glossary to reflect new changes related to cancellation process.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/14</td>
<td>i, <a href="#_bookmark17"><u>14</u>,</a> <a href="#routines"><u>18-19</u>,</a> <a href="#_bookmark23"><u>39</u>,</a> <a href="#_bookmark26"><u>40</u></a></td>
<td><blockquote>
<p>SR*3*177</p>
</blockquote></td>
<td><blockquote>
<p>Removed “9” from references to ICD. Added File #130.4 ICD SEARCH API.</p>
<p>Added 3 new routines: SR3P177, SROICDGT, and SROICDL.</p>
<p>Added input templates: SREQUEST-ICD10, SRSCHED-UNREQUESTED-ICD10, SRSRES2.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/12</td>
<td><blockquote>
<p>i, iii, 10, 18-19, 23-</p>
<p>25, 71, 73, 80-82</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*176</p>
</blockquote></td>
<td><blockquote>
<p>References to “Quarterly Report” removed. Routine “SROQ30D” added to the list of routines. Removal of “9” from references to ICD. Appendix A removed.</p>
<p>Index renumbered.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/11</td>
<td><blockquote>
<p>i, 13, 18-19, 20-22,</p>
<p>24-29, 34-36, 38,</p>
<p>40, 67, 69, 78-79</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*175</p>
</blockquote></td>
<td><blockquote>
<p>Change in definitions. Routine SRTOVRF added to the list of routines. Options description list updated.</p>
<p>Quarterly Report Menu removed. References to CICSP and NSQIP removed from the Glossary.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/10</td>
<td>i, 27</td>
<td><blockquote>
<p>SR*3*174</p>
</blockquote></td>
<td><blockquote>
<p>Change in definition of List of Surgery Risk Assessments report.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/08</td>
<td>All</td>
<td><blockquote>
<p>SR*3*167</p>
</blockquote></td>
<td><blockquote>
<p>Updated to provide the Surgery Transplant Assessment module information. Additions necessitated a document reissue.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an overview of the Surgery package, and also provides documentation conventions used in this *Surgery V. 3.0 Technical Manual/Security Guide*.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package is designed to be used by Surgeons, Surgical Residents, Anesthetists, Operating Room Nurses, and other surgical staff. The Surgery package is part of the patient information system that stores data on patients who have, or are about to undergo, surgical procedures. This package integrates booking, clinical, and patient data to provide a variety of administrative and clinical reports.

> The *Surgery V. 3.0 Technical Manual/Security Guide* acquaints the user with the various Surgery options and offers specific guidance on the maintenance and use of the Surgery package. Documentation concerning the Surgery package, including any subsequent change pages affecting this documentation, is located on the VistA Documentation Library (VDL) on the Internet at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/).

## Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package contains the following major components, also called modules:

- Requesting and Scheduling
- Tracking Clinical Procedures
- Generating Surgical Reports
- Chief of Surgery Module
- Managing the Software Package
- Assessing Surgical Risk
- Assessing Surgical Transplants

## Requesting and Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The surgeon uses this component to enter requests for surgical procedures. These requests are then assigned an operating room and time slot by the operating room scheduling manager. The Operating Room Schedule is generated automatically on any designated printer in the medical center. The Request and Scheduling module also allows for the rescheduling or cancellation of operative procedures.

## Tracking Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This component is comprised of options used to enter information specific to an individual surgical case. This information includes staff, times, diagnosis, perioperative occurrences, and anesthesia information. The package is designed so that information regarding a case can be entered on a terminal inside the operating room during the actual operative procedure. This information can then be used to generate the Patient Record and the Nurse Intraoperative Report.

## Generating Surgical Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module contains management reports for the Surgical Service. Reports generated include:

- Annual Report of Surgical Procedures
- Attending Surgeons Report
- Nurse Staffing Report
- Laboratory Interim Report

## Chief of Surgery Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module contains options and reports for the exclusive use of the Service Chief. The Chief has access to lists of cancellations and operations to be dictated, the Morbidity and Mortality Report, and Patient Perioperative Occurrences.

## Managing the Software Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module contains options designed for the Surgery package coordinator. The package coordinator can configure some of the Surgery fields to conform to the site's needs.

## Assessing Surgical Risk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module provides medical centers a mechanism to track information related to surgical risk and operative mortality. It gives surgeons an online method for evaluating and tracking patient probability of operative mortality. The Risk Assessment Data Manager is the primary user of this component.

## Assessing Surgical Transplants

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This module provides medical centers a mechanism to track information related to surgical transplant risk and operative mortality. The Transplant Coordinator is the primary user of this component. Additionally, this module is placed out of order with VistA patch SR\*3\*184.

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This *Surgery V. 3.0 Technical Manual/Security Guide* includes documentation conventions, also known as notations, which are used consistently throughout this manual. Each convention is outlined below.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Convention</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Menu option text is italicized.</td>
<td>The <em>Print Surgery Waiting List</em> option generates the long form surgery waiting list for the surgical service(s) selected.</td>
</tr>
<tr class="even">
<td>Screen prompts are denoted with quotation marks around them.</td>
<td>The "Puncture Site:" prompt will display next.</td>
</tr>
<tr class="odd">
<td>Responses in <strong>bold face</strong> indicate user input.</td>
<td>Needle Size: <strong>25G</strong></td>
</tr>
<tr class="even">
<td><p>Text centered between arrows represents a keyboard key that needs to be pressed for the system to capture a user response or move the cursor to another field.</p>
<p><strong>&lt;Enter&gt;</strong> indicates that the Enter key (or Return key on some keyboards) must be pressed.</p>
<p><strong>&lt;Tab&gt;</strong> indicates that the Tab key must be pressed.</p></td>
<td><p>Type <strong>Y</strong> for Yes or <strong>N</strong> for No and press</p>
<p><strong>&lt;Enter&gt;</strong>.</p>
<p>Press <strong>&lt;Tab&gt;</strong> to move the cursor to the next field.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Indicates especially important or helpful information.</p>
</blockquote></td>
<td><blockquote>
<p>If the user attempts to reschedule a case after the schedule close time for the date of operation,</p>
</blockquote>
<p>only the time, and not the date, can be changed.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Indicates that options are locked with a particular security key. The user must hold the</p>
</blockquote>
<p>particular security key to be able to perform the menu option.</p></td>
<td><blockquote>
<p>Without the SROAMIS key the</p>
</blockquote>
<p><em>Anesthesia AMIS</em> option cannot be accessed.</p></td>
</tr>
</tbody>
</table>

## ![](sr-3-184-surgery-technical-manual-security-guide-change-pages/002.png)![](sr-3-184-surgery-technical-manual-security-guide-change-pages/003.png)![](sr-3-184-surgery-technical-manual-security-guide-change-pages/004.png)Getting Help and Exiting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ?, ??, ??? One, two or three question marks can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

> Up arrow (caret or a circumflex) and pressing \<Enter\> can be used to exit the present option.

> *(This page included for two-sided copying.)*

> *(This page included for two-sided copying.)*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Implementation and Maintenance section contains information regarding the installation and setup of the Surgery package.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For installation of the Surgery V. 3.0 software package, please call the VA Service Desk (VASD) at 1- 888-596-4357 (HELP).

# Site Specific Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before using the Surgery package, the following initial information must be set up.

#### NEW PERSON File (#200)

> All personnel (surgeons, anesthesiologists, nurses, etc.) must be properly defined in the NEW PERSON file (#200).

#### Security Keys

> Security keys have various uses in the Surgery package and must be assigned as needed before using the package. The security keys used by the Surgery package are described in the Security Keys section of this manual.

#### Surgery Site Parameters

> There are a number of fields contained in the SURGERY SITE PARAMETERS file (#133) that can be updated locally. These fields are described below in the order they display in the Screen Server. The *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] option contains the *Surgery Site Parameters (Enter/Edit)* \[SROPARAM\] option to facilitate editing.

> MAIL CODE FOR ANESTHESIA Field (#3): This is the mail code for the Anesthesia service. It will be used to flag anesthesiologists on the Anesthesia AMIS.

> CANCEL IVS Field (#6): If this field is set equal to YES, all active IV orders are cancelled when a surgical case begins.

> DEFAULT BLOOD COMPONENT Field (#41): If a facility uses a certain type of blood component for most surgical cases, the user can enter that blood component in this field. The component displays as a default when requesting blood.

> CHIEF’S NAME Field (#9): This is the name of the Chief of Surgery. The name displays on the schedule of operations in the format entered in this field.

> LOCK AFTER HOW MANY DAYS Field (#10): This field determines how many days a surgical case remains unlocked after completion. Editing information related to a surgical case is prohibited after a case has been locked.

> REQUEST DEADLINE Field (#11): This is the time of day that requests are no longer accepted for the next available day. This field is used along with the REQUEST CUTOFF fields explained in this section.

> SCHEDULE CLOSE TIME Field (#13): This is the time of day that the schedule will be closed for the following day. It is used to determine whether canceled cases will appear on the cancellation report. Cases canceled before this time are not counted as cancellations and are deleted from the system. The SCHEDULE CLOSE TIME cannot be later than 3:00 pm.

> NURSE INTRAOP REPORT Field (#29): This field determines which format is used when printing the Nurse Intraoperative Report. One format prints all field titles, even when there is no data associated with the field. The other only prints those field titles that have information entered.

> CARDIAC ASSESSMENT IN USE (Y/N) Field (#15): This field determines whether the Cardiac Risk Assessment Module is being used at this facility. If so, enter 'YES'; if not enter 'NO'.

> ASK FOR RISK PREOP INFO Field (#17): This field is used to determine if the user should be prompted for risk assessment preoperative information when entering a new case and when updating a requested or scheduled case.

> SURGICAL RESIDENTS (Y/N) Field (#33): This field indicates whether residents may perform surgery at this facility. Enter NO if all surgeons at this facility are staff surgeons. If this field is NO, an attending surgeon is not required by the PCE interface and cases with no attend code are counted as Level 0 (Staff Alone) on the Quarterly Report.

> REQUIRED FIELDS FOR SCHEDULING Field (#28): With Surgery V. 3.0, scheduling of a surgical case can be prohibited until certain fields have been entered. This "multiple" field will contain any fields that are required prior to scheduling a procedure. For example, if the user wants to make the principal operative code (CPT), mandatory for scheduling, the field name would be entered here. Since this is a multiple field, the user can restrict scheduling dependent on more than one field. Fields that are multiple fields or that are word-processing fields cannot be selected.

> REQUEST CUTOFF FOR SUNDAY Field (#20): This field determines which day of the week is the cutoff day for requesting cases for Sunday. For example, if the cutoff day is Friday, the user is unable to request cases for Sunday after the request deadline on Friday. Sunday can also be made inactive, prohibiting requests entirely.

> The following fields function similar to the REQUEST CUTOFF FOR SUNDAY field:

> REQUEST CUTOFF FOR MONDAY field (#21) REQUEST CUTOFF FOR TUESDAY field (#22) REQUEST CUTOFF FOR WEDNESDAY field (#23) REQUEST CUTOFF FOR THURSDAY field (#24) REQUEST CUTOFF FOR FRIDAY field (#25) REQUEST CUTOFF FOR SATURDAY field (#26)

> HOLIDAY SCHEDULING ALLOWED Field (#27): This field determines which holidays have surgical cases scheduled. This information must be updated each year for all holidays.

> INACTIVE? Field (#35): This field is used to make a division inactive and to prevent its selection and use by Surgery users.

> AUTOMATED CASE CART ORDERING Field (#37): This field indicates whether or not the CoreFLS interface is in use at the facility. Enter YES, NO, or leave the field blank.

> ANESTHESIA REPORT IN USE Field (#40): Many Veterans Affairs (VA) Medical Centers do not use the Anesthesia Report provided with the Surgery package. A parameter has been created so that the automatic creation of stub Anesthesia Reports in the Text Integration Utilities (TIU) files can be eliminated when an operation is completed. If a site does not use the report, there is no need to create the stub for eventual signature. To indicate that the site uses the Anesthesia Report, select YES. If the site does not use the Anesthesia Report, select NO.

> DEFAULT CLINIC FOR DOCUMENTS Field (# 42): Enter a non-count clinic so that TIU documents will be associated with the appropriate default clinics. This non-count clinic is the default clinic for this division. It will be the location passed to TIU when Surgery documents are created if no other location can be identified. Enter the hospital location name, abbreviation, or team name.

> CODE ISSUE MAIL GROUP Field (# 43): This is the name of the mail group that will receive all coding issue messages sent by the Risk Assessment Nurse Reviewer. When the Non-Cardiac and Cardiac Risk Assessment option Alert Coder Regarding Coding Issues is used, a mail message is sent to the person that coded the Surgery case and the mail group identified in this field.

#### Options Tasked Daily

> The following option must be performed on a daily basis.

> SRTASK-NIGHT: This option initiates a number of background tasks to clean up the surgery database and update all appropriate information. Among the tasks performed are calculation of average procedure times, cleanup of outstanding requests, update expected start and end times for operating rooms, locking cases, transmit risk assessment and workload information, and send updates to PCE.

#### Adding Operating Rooms

> The operating rooms must be added to the VA FileMan HOSPITAL LOCATION file (#44) and the OPERATING ROOM file (#131.7) before they can be used in any of the Surgery package applications. All locations for non-O.R. procedures must be defined in the HOSPITAL LOCATION file (#44).

#### HOSPITAL LOCATION file (#44)

> The following is an example of how to set up an operating room in the HOSPITAL LOCATION file (#44). Please coordinate entries with the Medical Administration Service (MAS) package coordinator.

> Example: Setting Up an Operating Room in the HOSPITAL LOCATION file (#44)

#### OPERATING ROOM file (#131.7)

> Following is an example of how to set up an operating room in the OPERATING ROOM file (#131.7).

> The *Surgery Utilization Menu* \[SR OR UTIL\] option in the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] *option* has a sub-option called the *Normal Daily Hours (Enter/Edit)* \[SR NORMAL HOURS\] option for editing operating room normal daily hours. The *Operating Room Information (Enter/Edit)* \[SRO-ROOM\] option in the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] option can be used to edit other information in this file.

> ![](sr-3-184-surgery-technical-manual-security-guide-change-pages/005.png)The Schedule of Operations displays the operating rooms in the same sequence in which they are entered in the OPERATING ROOM file (#131.7).

> Example: Setting Up an Operating Room in the OPERATING ROOM File (#131.7)

> Select VA FileMan Option: Enter or Edit File Entries

> INPUT TO WHAT FILE: OPERATING ROOM

> EDIT WHICH FIELD: ALL// \<Enter\>

> Select OPERATING ROOM NAME: OR1

> ARE YOU ADDING 'OR1' AS A NEW OPERATING ROOM (THE 1ST)? Y (YES) LOCATION: THIRD FLOOR NORTH WING

> PERSON RESP.: SURNURSE,ONE TELEPHONE: EXT 5244 REMARKS: \<Enter\>

> TYPE: ?

> ANSWER WITH OPERATING ROOM TYPE NAME

> DO YOU WANT THE ENTIRE 13-ENTRY OPERATING ROOM TYPE LIST? Y (YES) CHOOSE FROM:

> AMBULATORY OPERATING ROOM CARDIAC OPERATING ROOM CARDIAC/NEURO OPERATING ROOM CLINIC

> CYSTOSCOPY ROOM DEDICATED ROOM ENDOSCOPY ROOM

> GENERAL PURPOSE OPERATING ROOM INTENSIVE CARE UNIT NEUROSURGERY OPERATING ROOM ORTHOPEDIC OPERATING ROOM OTHER LOCATION

> WARD

> TYPE: GENERAL PURPOSE OPERATING ROOM

> CLEANING TIME: 30

> Select DAY OF THE WEEK: SUNDAY

> ARE YOU ADDING 'SUNDAY' AS A NEW DAY OF THE WEEK (THE 1ST FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: \<Enter\>

> NORMAL END TIME: \<Enter\>

> INACTIVE (Y/N): YES

> Select DAY OF THE WEEK: MONDAY

> ARE YOU ADDING 'MONDAY' AS A NEW DAY OF THE WEEK (THE 2ND FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: 07:00

> NORMAL END TIME: 15:30

> INACTIVE (Y/N): \<Enter\>

> Select DAY OF THE WEEK: TUESDAY

> ARE YOU ADDING 'TUESDAY' AS A NEW DAY OF THE WEEK (THE 3RD FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: 07:00

> NORMAL END TIME: 15:30

> INACTIVE (Y/N): \<Enter\>

> Select DAY OF THE WEEK: WEDNESDAY

> ARE YOU ADDING 'WEDNESDAY' AS A NEW DAY OF THE WEEK (THE 4TH FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: 07:00

> NORMAL END TIME: 15:30

> INACTIVE (Y/N): \<Enter\>

> Select DAY OF THE WEEK: THURSDAY

> ARE YOU ADDING 'THURSDAY' AS A NEW DAY OF THE WEEK (THE 5TH FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: 07:00

> NORMAL END TIME: 15:30

> INACTIVE (Y/N): \<Enter\>

> Select DAY OF THE WEEK: FRIDAY

> ARE YOU ADDING 'FRIDAY' AS A NEW DAY OF THE WEEK (THE 6TH FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: 07:00

> NORMAL END TIME: 15:30

> INACTIVE (Y/N): \<Enter\>

> Select DAY OF THE WEEK: SATURDAY

> ARE YOU ADDING 'SATURDAY' AS A NEW DAY OF THE WEEK (THE 7TH FOR THIS OPERATING ROOM)? Y (YES) NORMAL START TIME: \<Enter\>

> NORMAL END TIME: \<Enter\>

> INACTIVE (Y/N): YES

> INACTIVE?: \<Enter\>

#### Adding Entries to Surgery-Related Files

> There are several site-configurable Surgery files that may need updating to add new entries or to inactivate or change existing entries. These configurable files are listed below. Use the *Update Site Configurable Files* \[SR UPDATE FILES\] option on the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] option to update these files.

- SURGERY TRANSPORTATION DEVICES file (#131.01)
- SURGERY POSITION file (#132)
- SURGICAL DELAY file (#132.4)
- IRRIGATION file (#133.6)
- SKIN INTEGRITY file (#135.2)
- PATIENT CONSCIOUSNESS file (#135.4)
- ELECTROGROUND POSITIONS file (#138)
- PROSTHESIS file (#131.9)
- RESTRAINTS AND POSITIONAL AIDS file (#132.05)
- MONITORS file (#133.4)
- SURGERY REPLACEMENT FLUIDS file (#133.7)
- SKIN PREP AGENTS file (#135.1)
- PATIENT MOOD file (#135.3)
- LOCAL SURGICAL SPECIALTY file (#137.45)
- SPECIAL EQUIPMENT file (#131.3)
- PLANNED IMPLANT file (#131.5)
- PHARMACY ITEMS file (#131.06)
- SPECIAL INSTRUMENTS file (#131.02)
- SPECIAL SUPPLIES file (#131.04)

#### Flag Drugs for Anesthesia Agents

> Drugs to be used as anesthesia agents must be flagged or they cannot be selected as entries in the ANESTHESIA AGENT data fields.

#### Mail Groups

> The following mail groups should be created with the appropriate persons added as members.

> RISK ASSESSMENT SRHL DISCREPANCY SR TRANSPLANT

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each entry in the SURGERY file (#130) contains information regarding a surgery case, consisting of an operative procedure, or multiple operative procedures, for a patient. The file includes the information necessary for creating the Nurse Intraoperative Report, the Operation Report, and the Anesthesia Report.

> The following files are exported with the Surgery package.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Comes With File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>User Override</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>130</td>
<td>SURGERY</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td><span id="_bookmark17" class="anchor"></span>130.4</td>
<td>ICD SEARCH API</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>131</td>
<td>PERSON FIELD RESTRICTION</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>NO</td>
</tr>
<tr class="even">
<td>131.01</td>
<td>SURGERY TRANSPORTATION DEVICES</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.02</td>
<td>SPECIAL INSTRUMENTS</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.04</td>
<td>SPECIAL SUPPLIES</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.06</td>
<td>PHARMACY ITEMS</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.25</td>
<td>OPERATION TIMES</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.3</td>
<td>SPECIAL EQUIPMENT</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.4</td>
<td>CPT-SPINAL LEVEL</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.5</td>
<td>PLANNED IMPLANT</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.6</td>
<td>SURGERY DISPOSITION</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>131.7</td>
<td>OPERATING ROOM</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.8</td>
<td>SURGERY UTILIZATION</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.9</td>
<td>PROSTHESIS</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>132</td>
<td>SURGERY POSITION</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>132.05</td>
<td>RESTRAINTS AND POSITIONAL AIDS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>132.4</td>
<td>SURGICAL DELAY</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>132.8</td>
<td>ASA CLASS</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="even">
<td>132.9</td>
<td>ATTENDING CODES</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>132.95</td>
<td>ANESTHESIA SUPERVISOR CODES</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="even">
<td>133</td>
<td>SURGERY SITE PARAMETERS</td>
<td>YES</td>
<td>NO (OVERWRITE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>133.2</td>
<td>SURGERY INTERFACE PARAMETER</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
</tr>
<tr class="even">
<td>133.4</td>
<td>MONITORS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>133.6</td>
<td>IRRIGATION</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>133.7</td>
<td>SURGERY REPLACEMENT FLUIDS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>133.8</td>
<td>SURGERY WAITING LIST</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>134</td>
<td>OPERATING ROOM TYPE</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>135</td>
<td>SURGERY CANCELLATION REASON</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>135.1</td>
<td>SKIN PREP AGENTS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>135.2</td>
<td>SKIN INTEGRITY</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>135.3</td>
<td>PATIENT MOOD</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>135.4</td>
<td>PATIENT CONSCIOUSNESS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update</strong></p>
<p><strong>DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Comes With</strong></p>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>User</strong></p>
<p><strong>Override</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>136</td>
<td>SURGERY PROCEDURE/DIAGNOSIS CODES</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>136.5</td>
<td>PERIOPERATIVE OCCURRENCE CATEGORY</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>137</td>
<td>CPT EXCLUSIONS</td>
<td>YES</td>
<td>NO</td>
<td>NO</td>
</tr>
<tr class="even">
<td><blockquote>
<p>137.45</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL SURGICAL SPECIALTY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (OVERWRITE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>138</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROGROUND POSITIONS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (MERGE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>139.2</p>
</blockquote></td>
<td><blockquote>
<p>RISK MODEL LAB TEST</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (OVERWRITE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>139.5</p>
</blockquote></td>
<td><blockquote>
<p>SURGERY TRANSPLANT ASSESSMENTS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following non-Surgery file is exported with the Surgery package.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Comes With File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>User Override</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>723</td>
<td>MEDICAL SPECIALTY</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>YES</td>
</tr>
</tbody>
</table>

# File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> View file descriptions by using the VA FileMan *Print File Entries* \[DIPRINT\] option. Surgery file numbers range from 130 to 139.5.

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Select VA FileMan Option: <strong>PRINT FILE ENTRIES</strong></th>
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><p>OUTPUT FROM WHAT FILE: <strong>FILE</strong> SORT BY: NAME// .001 NUMBER START WITH NUMBER: FIRST// <strong>130</strong> GO TO NUMBER: LAST// <strong>130</strong></p>
<blockquote>
<p>WITHIN NUMBER, SORT BY:</p>
</blockquote>
<p>FIRST PRINT ATTRIBUTE: <strong>1</strong> GLOBAL NAME THEN PRINT ATTRIBUTE: <strong>.01</strong> NAME</p>
<p>THEN PRINT ATTRIBUTE: <strong>DESCRIPTION</strong> (word-processing) THEN PRINT ATTRIBUTE:</p>
<p>Heading (S/C): FILE LIST// <strong>&lt;Enter&gt;</strong></p>
<p>START AT PAGE: 1// <strong>&lt;Enter&gt;</strong></p></th>
<th></th>
</tr>
<tr class="header">
<th>DEVICE: VIRTUAL Right Margin: 80// <strong>&lt;Enter&gt;</strong></th>
<th></th>
</tr>
<tr class="odd">
<th><p>FILE LIST AUG 15,2001 10:17</p>
<p>GLOBAL NAME NAME DESCRIPTION</p></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>NUMBER: 130</p>
</blockquote>
<p>^SRF( SURGERY</p>
<blockquote>
<p>Each entry in the SURGERY file contains information regarding a surgery case made up of an operative procedure, or multiple operative procedures for a patient. The file includes the information necessary for creating the Nurses' Intraoperative Report, Operation Report, and Anesthesia Report</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2">Select VA FileMan Option:</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is the list of routines used in the Surgery package. This list excludes all initialization routines, protocol installation routines, and routines exported with patches that performed a one-time function. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine in the SR- namespace.

| SR3P177  | SRBL     | SRBLOOD  | SRCHL7A  | SRCHL7U  | SRCUSS   | SRCUSS0  | SRCUSS1  |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SRCUSS2  | SRCUSS3  | SRCUSS4  | SRCUSS5  | SRENSCS  | SRHLDW   | SRHLDW1  | SRHLENV  |
| SRHLMFN  | SRHLOORU | SRHLORU  | SRHLQRY  | SRHLSCRN | SRHLU    | SRHLUI   | SRHLUO   |
| SRHLUO1  | SRHLUO2  | SRHLUO3  | SRHLUO4  | SRHLUO4C | SRHLVOOR | SRHLVORU | SRHLVQRY |
| SRHLVU   | SRHLVUI  | SRHLVUI2 | SRHLVUO  | SRHLVUO1 | SRHLVUO2 | SRHLVUO4 | SRHLVZIU |
| SRHLVZQR | SRHLVZSQ | SRHLXTMP | SRHLZIU  | SRHLZQR  | SRO1L    | SRO1L1   | SROA30   |
| SROABCH  | SROACAR  | SROACAR1 | SROACAT  | SROACC   | SROACC0  | SROACC1  | SROACC2  |
| SROACC3  | SROACC4  | SROACC5  | SROACC6  | SROACCM  | SROACCT  | SROACL1  | SROACL2  |
| SROACLN  | SROACMP  | SROACMP1 | SROACOD  | SROACOM  | SROACOM1 | SROACOP  | SROACPM  |
| SROACPM0 | SROACPM1 | SROACPM2 | SROACR1  | SROACR2  | SROACS   | SROACTH  | SROACTH1 |
| SROADEL  | SROADOC  | SROADOC1 | SROADX   | SROADX1  | SROADX2  | SROAERR  | SROAEX   |
| SROAL1   | SROAL11  | SROAL2   | SROAL21  | SROALAB  | SROALC   | SROALCP  | SROALCS  |
| SROALCSP | SROALDP  | SROALEC  | SROALEN  | SROALESS | SROALET  | SROALL   | SROALLP  |
| SROALLS  | SROALLSP | SROALM   | SROALMN  | SROALN1  | SROALN2  | SROALN3  | SROALNC  |
| SROALNO  | SROALOG  | SROALSL  | SROALSS  | SROALSSP | SROALST  | SROALSTP | SROALT   |
| SROALTP  | SROALTS  | SROALTSP | SROAMAN  | SROAMEAS | SROAMIS  | SROAMIS1 | SROANEST |
| SROANEW  | SROANIN  | SROANP   | SROANP1  | SROANR   | SROANR0  | SROANR1  | SROANT   |
| SROANTP  | SROANTS  | SROANTSP | SROAO    | SROAOP   | SROAOP1  | SROAOP2  | SROAOPS  |
| SROAOSET | SROAOTH  | SROAOUT  | SROAPAS  | SROAPC   | SROAPCA  | SROAPCA0 | SROAPCA1 |
| SROAPCA2 | SROAPCA3 | SROAPCA4 | SROAPIMS | SROAPM   | SROAPR1A | SROAPR2  | SROAPRE  |
| SROAPRE1 | SROAPRE2 | SROAPRT1 | SROAPRT2 | SROAPRT3 | SROAPRT4 | SROAPRT5 | SROAPRT6 |
| SROAPRT7 | SROAPS1  | SROAPS2  | SROAR    | SROAR1   | SROAR2   | SROARET  | SROARPT  |
| SROASITE | SROASS   | SROASS1  | SROASSE  | SROASSN  | SROASSP  | SROAT0P  | SROAT0T  |
| SROAT1P  | SROAT1T  | SROAT2P  | SROAT2T  | SROATCM  | SROATCM1 | SROATCM2 | SROATCM3 |
| SROATM1  | SROATM2  | SROATM3  | SROATM4  | SROATMIT | SROATMN1 | SROATMNO | SROATT   |
| SROATT0  | SROATT1  | SROATT2  | SROAUTL  | SROAUTL0 | SROAUTL1 | SROAUTL2 | SROAUTL3 |
| SROAUTL4 | SROAUTLC | SROAWL   | SROAWL1  | SROAX    | SROBLOD  | SROCAN   | SROCAN0  |
| SROCANUP | SROCASE  | SROCCAT  | SROCD    | SROCD0   | SROCD1   | SROCD2   | SROCD3   |
| SROCD4   | SROCDX   | SROCDX1  | SROCDX2  | SROCL1   | SROCLAB  | SROCMP   | SROCMP1  |
| SROCMP2  | SROCMPD  | SROCMPED | SROCMPL  | SROCMPS  | SROCNR   | SROCNR1  | SROCNR2  |
| SROCODE  | SROCOM   | SROCOMP  | SROCON   | SROCON1  | SROCOND  | SROCPT   | SROCPT0  |
| SROCRAT  | SROCVER  | SRODATE  | SRODEL76 | SRODELA  | SRODEV   | SRODIS   | SRODIS0  |
| SRODLA1  | SRODLA2  | SRODLAY  | SRODLT   | SRODLT0  | SRODLT1  | SRODLT2  | SRODPT   |
| SRODTH   | SROERR   | SROERR0  | SROERR1  | SROERR2  | SROERRPO | SROES    | SROESAD  |

| SROESAD1 | SROESAR  | SROESAR0 | SROESAR1 | SROESAR2 | SROESARA | SROESHL  | SROESL   |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SROESNR  | SROESNR0 | SROESNR1 | SROESNR2 | SROESNR3 | SROESNRA | SROESPR  | SROESPR1 |
| SROESPR2 | SROESTV  | SROESUTL | SROESX   | SROESX0  | SROESXA  | SROESXP  | SROFILE  |
| SROFLD   | SROGMTS  | SROGMTS0 | SROGMTS1 | SROGMTS2 | SROGTSR  | SROHIS   | SROICD   |
| SROICDGT | SROICDL  | SROICU   | SROICU1  | SROICU2  | SROINQ   | SROIRR   | SROKEY   |
| SROKEY1  | SROKRET  | SROLABS  | SROLOCK  | SROMED   | SROMENU  | SROMOD   | SROMOD0  |
| SROMOR   | SROMORT  | SRONAN   | SRONAN1  | SRONASS  | SRONBCH  | SRONEW   | SRONIN   |
| SRONITE  | SRONON   | SRONOP   | SRONOP1  | SRONOR   | SRONOR1  | SRONOR2  | SRONOR3  |
| SRONOR4  | SRONOR5  | SRONOR6  | SRONOR7  | SRONOR8  | SRONP    | SRONP0   | SRONP1   |
| SRONP2   | SRONPEN  | SRONRPT  | SRONRPT0 | SRONRPT1 | SRONRPT2 | SRONRPT3 | SRONRPT4 |
| SRONUR   | SRONUR1  | SRONUR2  | SRONXR   | SROOPRM  | SROOPRM1 | SROP     | SROP1    |
| SROPAC0  | SROPAC1  | SROPACT  | SROPAT   | SROPCE   | SROPCE0  | SROPCE0A | SROPCE0B |
| SROPCE1  | SROPCEP  | SROPCEU  | SROPCEU0 | SROPCEX  | SROPDEL  | SROPECS  | SROPECS1 |
| SROPER   | SROPFSS  | SROPLIS  | SROPLIST | SROPLST1 | SROPLSTS | SROPPC   | SROPREQ  |
| SROPRI   | SROPRI1  | SROPRI2  | SROPRIN  | SROPRIO  | SROPRIT  | SROPROC  | SROPRPT  |
| SROPS    | SROPS1   | SROPSEL  | SROPSN   | SROQ     | SROQ0    | SROQ0A   | SROQ30D  |
| SROQADM  | SROQD    | SROQD0   | SROQD1   | SROQIDP  | SROQIDP0 | SROQL    | SROQN    |
| SROR     | SRORACE  | SRORAT1  | SRORAT2  | SRORATA  | SRORATP  | SRORATS  | SROREA   |
| SROREA1  | SROREA2  | SROREAS  | SROREQ   | SROREQ1  | SROREQ2  | SROREQ3  | SROREQ4  |
| SROREST  | SRORESV  | SRORET   | SRORHRS  | SRORHRS0 | SRORIN   | SRORTRN  | SRORUT   |
| SRORUT0  | SRORUT1  | SRORUT2  | SROSCH   | SROSCH1  | SROSCH2  | SROSNR   | SROSNR1  |
| SROSNR2  | SROSPC1  | SROSPEC  | SROSPLG  | SROSPLG1 | SROSPLG2 | SROSPSS  | SROSRPT  |
| SROSTAFF | SROSTOP  | SROSUR   | SROSUR1  | SROSUR2  | SROTHER  | SROTIUD  | SROTRIG  |
| SROTRPT  | SROTRPT0 | SROUNV   | SROUNV1  | SROUNV2  | SROUTC   | SROUTED  | SROUTIN  |
| SROUTL   | SROUTL0  | SROUTL1  | SROUTLN  | SROUTUP  | SROVAR   | SROVER   | SROVER1  |
| SROVER2  | SROVER3  | SROWC    | SROWC1   | SROWC2   | SROWC3   | SROWL    | SROWL0   |
| SROWRQ   | SROWRQ1  | SROXPR   | SROXR1   | SROXR2   | SROXR4   | SROXREF  | SROXRET  |
| SRSAVG   | SRSAVL   | SRSAVL1  | SRSBD1   | SRSBDEL  | SRSBLOK  | SRSBOUT  | SRSBUTL  |
| SRSCAN   | SRSCAN0  | SRSCAN1  | SRSCAN2  | SRSCD    | SRSCDS   | SRSCDS1  | SRSCDW   |
| SRSCDW1  | SRSCG    | SRSCHAP  | SRSCHC   | SRSCHC1  | SRSCHC2  | SRSCHCA  | SRSCHCC  |
| SRSCHD   | SRSCHD1  | SRSCHD2  | SRSCHDA  | SRSCHDC  | SRSCHK   | SRSCHOR  | SRSCHUN  |
| SRSCHUN1 | SRSCHUP  | SRSCONR  | SRSCOR   | SRSCPT   | SRSCPT1  | SRSCPT2  | SRSCRAP  |
| SRSDIS1  | SRSDISP  | SRSDT    | SRSGRPH  | SRSIND   | SRSKILL  | SRSKILL1 | SRSKILL2 |
| SRSMREQ  | SRSPUT0  | SRSPUT1  | SRSPUT2  | SRSRBS   | SRSRBS1  | SRSRBW   | SRSRBW1  |
| SRSREQ   | SRSREQUT | SRSRQST  | SRSRQST1 | SRSTCH   | SRSTIME  | SRSUP1   | SRSUPC   |
| SRSUPRG  | SRSUPRQ  | SRSUTIN  | SRSUTL   | SRSUTL2  | SRSWL    | SRSWL1   | SRSWL10  |
| SRSWL11  | SRSWL12  | SRSWL13  | SRSWL14  | SRSWL15  | SRSWL2   | SRSWL3   | SRSWL4   |
| SRSWL5   | SRSWL6   | SRSWL7   | SRSWL8   | SRSWL9   | SRSWLST  | SRSWREQ  | SRTOVRF  |
| SRTPASS  | SRTPCOM  | SRTPDONR | SRTPHRT1 | SRTPHRT2 | SRTPHRT3 | SRTPHRT4 | SRTPHRT5 |
| SRTPHRT6 | SRTPKID1 | SRTPKID2 | SRTPKID3 | SRTPKID4 | SRTPKID6 | SRTPLIV1 | SRTPLIV2 |
| SRTPLIV3 | SRTPLIV4 | SRTPLIV5 | SRTPLIV6 | SRTPLIV7 | SRTPLS   | SRTPLST  | SRTPLSTP |
| SRTPLUN1 | SRTPLUN2 | SRTPLUN3 | SRTPLUN5 | SRTPNEW  | SRTPPAS  | SRTPRACE | SRTPRH   |

| SRTPRH1  | SRTPRH2  | SRTPRK   | SRTPRK1  | SRTPRK2  | SRTPRK3 | SRTPRLI | SRTPRLI1 |
|----------|----------|----------|----------|----------|---------|---------|----------|
| SRTPRLI2 | SRTPRLU  | SRTPRLU1 | SRTPRLU2 | SRTPSITE | SRTPSS  | SRTPTM1 | SRTPTM2  |
| SRTPTMIT | SRTPTRAN | SRTPUTL  | SRTPUTL4 | SRTPUTLC | SRTPVAN |         |          |

> 630 routines

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains information about the Surgery package options; first, the exported options are listed by name, and then they are provided alphabetically, with a description of the option.

# Options Listed by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table contains a list of all of the options in the Surgery package, listed alphabetically by name.

| SR ANESTH REPORTS           | SR BLOOD PRODUCT VERIFICATION | SR BLOOD PRODUCT VERIFY AUDIT |
|-----------------------------|-------------------------------|-------------------------------|
| SR CPT ACCURACY             | SR CPT REPORTS                | SR MANAGE REPORTS             |
| SR NO ASSESSMENT REASON     | SR NON-OR INFO                | SR NON-OR REPORT              |
| SR NORMAL HOURS             | SR OR HOURS                   | SR OR UTIL                    |
| SR OR UTL1                  | SR PURGE UTILIZATION          | SR STAFFING REPORTS           |
| SR SURGERY REQUEST          | SR TRANSPLANT ASSESSMENT      | SR TRANSPLANT ENTER/EDIT      |
| SR TRANSPLANT PARAMETERS    | SR UPDATE FILES               | SR UPDATE SCHEDULE DEVIC      |
| SR UTIL EDIT ROOM           | SR VIEW HISTORICAL REPORTS    | SRCODING EDIT                 |
| SRCODING MENU               | SRCODING NURSE REPORT         | SRCODING OP REPORT            |
| SRCODING UPDATE/VERIFY MENU | SRHL DOWNLOAD INTERFACE FILES | SRHL DOWNLOAD SET OF CODES    |
| SRHL INTERFACE              | SRHL INTERFACE FLDS           | SRHL PARAMETER                |
| SRO CASES BY DISPOSITION    | SRO CASES BY PRIORITY         | SRO COMPLICATIONS MENU        |
| SRO DEATH RELATED           | SRO DEL MENU                  | SRO DELAY TIME                |
| SRO ECS COMPLIANCE          | SRO INTRAOP COMP              | SRO M&M VERIFICATION REPORT   |
| SRO PACKAGE MANAGEMENT      | SRO PCE NOTRANS               | SRO PCE STATUS                |
| SRO POSTOP COMP             | SRO QUARTERLY REPORT          | SRO SURGICAL PRIORITY         |
| SRO UPDATE CANCELLED CASE   | SRO UPDATE RETURNS            |                               |
| SRO-CHIEF REPORTS           | SRO-LRRP                      | SRO-ROOM                      |
| SRO-UNLOCK                  | SROA ASSESSMENT LIST          | SROA CARDIAC COMPLICATIONS    |
| SROA CARDIAC ENTER/EDIT     | SROA CARDIAC OPERATIVE RISK   | SROA CARDIAC PROCEDURES       |
| SROA CARDIAC RESOURCE       | SROA CARDIAC-OUTCOMES         | SROA CATHETERIZATION          |
| SROA CLINICAL INFORMATION   | SROA CODE ISSUE               | SROA COMPLETE ASSESSMENT      |
| SROA DEMOGRAPHICS           | SROA ENTER/EDIT               | SROA LAB                      |
| SROA LAB TEST EDIT          | SROA LAB-CARDIAC              | SROA MONTHLY WORKLOAD REPORT  |

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>SROA ONE-LINER UPDATE</th>
<th>SROA OPERATION DATA</th>
<th>SROA OUTCOMES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SROA PREOP DATA</td>
<td>SROA PRINT ASSESSMENT</td>
<td>SROA REPRINT LETTERS</td>
</tr>
<tr class="even">
<td>SROA RISK ASSESSMENT</td>
<td>SROA TRANSMIT ASSESSMENTS</td>
<td>SROA TRANSMITTED IN ERROR</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SROABRT</p>
</blockquote></td>
<td>SROADOC</td>
<td>SROAMIS</td>
</tr>
<tr class="even">
<td>SROACCT</td>
<td>SROANES MED</td>
<td>SROANES-D</td>
</tr>
<tr class="odd">
<td>SROANES</td>
<td>SROANP</td>
<td>SROARPT</td>
</tr>
<tr class="even">
<td>SROANES1</td>
<td>SROASITE</td>
<td>SROATT</td>
</tr>
<tr class="odd">
<td>SROARSP</td>
<td>SROCHIEF</td>
<td>SROCNR</td>
</tr>
<tr class="even">
<td>SROCAN</td>
<td>SROCOMP</td>
<td>SROCRAT</td>
</tr>
<tr class="odd">
<td>SROCODE</td>
<td>SRODISP</td>
<td>SROERR BACKFILL</td>
</tr>
<tr class="even">
<td>SRODELA</td>
<td>SROKEY ENTER</td>
<td>SROKEY MENU</td>
</tr>
<tr class="odd">
<td>SROICU</td>
<td>SROMEN-ANES</td>
<td>SROMEN-ANES TECH</td>
</tr>
<tr class="even">
<td>SROKEY REMOVE</td>
<td>SROMEN-M&amp;M</td>
<td>SROMEN-OP</td>
</tr>
<tr class="odd">
<td>SROMEN-COM</td>
<td>SROMEN-OUT</td>
<td>SROMEN-PACU</td>
</tr>
<tr class="even">
<td>SROMEN-OPINFO</td>
<td>SROMEN-REFER</td>
<td>SROMEN-REST</td>
</tr>
<tr class="odd">
<td>SROMEN-POST</td>
<td>SROMEN-VERF</td>
<td>SROMEN-START</td>
</tr>
<tr class="even">
<td>SROMEN-STAFF</td>
<td>SROMM</td>
<td>SRONOP</td>
</tr>
<tr class="odd">
<td>SROMENU</td>
<td>SRONOP-EDIT</td>
<td>SRONOP-ENTER</td>
</tr>
<tr class="even">
<td>SRONOP-ANNUAL</td>
<td>SRONOR-CODERS</td>
<td>SRONRPT</td>
</tr>
<tr class="odd">
<td>SRONOR</td>
<td>SROOPREQ</td>
<td>SROP REQ</td>
</tr>
<tr class="even">
<td>SRONSR</td>
<td>SROPARAM</td>
<td>SROPER</td>
</tr>
<tr class="odd">
<td>SROPACT</td>
<td>SROPLIST1</td>
<td>SROPPC</td>
</tr>
<tr class="even">
<td>SROPLIST</td>
<td>SROQ MENU</td>
<td>SROQ MISSING DATA</td>
</tr>
<tr class="odd">
<td>SROQ LIST OPS</td>
<td>SROQD</td>
<td>SROQIDP</td>
</tr>
<tr class="even">
<td>SROQADM</td>
<td>SROREQ</td>
<td>SROREQV</td>
</tr>
<tr class="odd">
<td>SROREAS</td>
<td>SRORPTS</td>
<td>SROSCH</td>
</tr>
<tr class="even">
<td>SRORET</td>
<td>SROSNR</td>
<td>SROSPEC</td>
</tr>
<tr class="odd">
<td>SROSCHOP</td>
<td>SROSRPT</td>
<td>SROSTAFF</td>
</tr>
<tr class="even">
<td>SROSRES</td>
<td>SROTRPT</td>
<td>SROUNV</td>
</tr>
<tr class="odd">
<td>SROSUR</td>
<td>SROW-DELETE</td>
<td>SROW-EDIT</td>
</tr>
<tr class="even">
<td>SROVER</td>
<td>SROWAIT</td>
<td>SROWC</td>
</tr>
<tr class="odd">
<td>SROW-ENTER</td>
<td>SRSBDEL</td>
<td>SRSBOUT</td>
</tr>
<tr class="even">
<td>SROWRQ</td>
<td>SRSCD</td>
<td>SRSCHD1</td>
</tr>
<tr class="odd">
<td>SRSCAN</td>
<td>SRSCHDC</td>
<td>SRSCHUP</td>
</tr>
<tr class="even">
<td>SRSCHDA</td>
<td>SRSRBS</td>
<td>SRSREQCC</td>
</tr>
<tr class="odd">
<td>SRSCPT</td>
<td>SRSUPRQ</td>
<td>SRSWL2</td>
</tr>
<tr class="even">
<td>SRSUPC</td>
<td>SRTASK-NIGHT</td>
<td>SRTP ASSESSMENT LIST</td>
</tr>
<tr class="odd">
<td>SRSWREQ</td>
<td>SRTP PRINT ASSESSMENT</td>
<td></td>
</tr>
</tbody>
</table>

# Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an alphabetical listing of Surgery options, and includes a brief description of each option.

> *Abort/Cancel Operation* \[SROABRT\]

> This option has been added as a new option under the Operation Menu \[SROPER\]. This new option will prompt the user for CASE ABORTED field (#18.5) (“NO” default) and the cancellation information fields (CANCEL DATE, CANCELLATION TIMEFRAME and PRIMARY CANCEL REASON).

> This menu option should only be used if the patient has been taken to the operating room and no incision has been made. If an incision is made, the case should be completed and the discontinued procedure indicated in the record. Cancellation of future surgical cases should not use this option

### Admissions w/in 14 days of Out Surgery if Postop Occ \[SROQADM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides a list of patients with completed outpatient surgical cases which resulted in at least one postoperative occurrence AND a hospital admission within 14 days of the surgery.

> *Alert Coder Regarding Coding Issues* \[SROA CODE ISSUE\]

> This option is used to provide the Risk Assessment Nurse Reviewers an electronic method to notify coders of potential coding issues or concerns. The message sent will include the basic Surgery case information and comments specifically added by the Nurse Reviewer.

> *Anesthesia AMIS* \[SROAMIS\]

> This report generates the Anesthesia AMIS Report required by Central Office (C.O.).

> *Anesthesia Data Entry Menu* \[SROANES-D\]

> This menu contains options used to enter or edit anesthesia related information.

> *Anesthesia Information (Enter/Edit)* \[SROMEN-ANES\]

> This option is used to enter Anesthesia related information for a given case.

> *Anesthesia Menu* \[SROANES1\]

> This menu contains the various options used to enter and display information related to the anesthesia technique and personnel.

> *Anesthesia Provider Report* \[SROADOC\]

> This report provides information concerning the Anesthesia staff and technique for completed cases. It will sort the cases by the principal anesthetist.

> *Anesthesia Report* \[SROARPT\]

> This option, locked by the SROANES security key, generates the Anesthesia Report containing anesthesia information for a surgical case. Before the report is electronically signed, the option displays information directly from the SURGERY file (#130) with the choice to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically, if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the report to be viewed or printed.

> *Anesthesia Reports* \[SR ANESTH REPORTS\] This menu contains various Anesthesia Reports, including the Anesthesia AMIS Report and List of Anesthetic Procedures.

> *Anesthesia Technique (Enter/Edit)* \[SROMEN-ANES TECH\]

> This option is used to enter information for the anesthesia technique used. Depending on what technique was used, a different set of fields may be entered.

> *Anesthesia for an Operation Menu* \[SROANES\]

> This menu contains the various Anesthesia related options used to input and display anesthesia staff and technique information.

> *Annual Report of Non-O.R. Procedures* \[SRONOP-ANNUAL\]

> This option is used to generate the Annual Report of Non-OR Procedures. It will display the total number of procedures based on CPT code.

### Annual Report of Surgical Procedures \[SROARSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to generate the Annual Report of Surgical Procedures. It will count procedures within Surgical Specialties.

> *Attending Surgeon Reports* \[SROATT\]

> This option generates the Attending Surgeon Reports that displays staffing information for completed cases along with cumulative totals for each attending code. It can be sorted by surgical specialty and can be generated for an individual surgeon.

> *Blood Product Verification* \[SR BLOOD PRODUCT VERIFICATION\]

> The user can access this option through the *Operation Menu* \[SROPER\] option. After scanning the blood unit ID, the software will check for an association with the patient identified. If there are multiple entries with the Unit ID scanned, these entries will be listed along with the Blood Component, Patient Associated, and Expiration Date. The user will then be prompted to select the one that matches the blood product about to be administered. If the selected product is not associated with the patient identified, the warning message will be displayed.

> *CPT Code Reports* \[SR CPT REPORTS\]

> This menu contains reports based on CPT Codes. It includes the Cumulative Report of CPT Codes, Report of CPT Coding Accuracy, and the Report of Cases Missing CPT Codes.

> *CPT/ICD Coding Menu* \[SRCODING MENU\]

> This menu provides functionality for reviewing operations and non-OR procedures and for editing operation and non-OR procedure CPT and ICD codes.

> *CPT/ICD Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] This menu contains options to be used by those responsible for entering CPT and ICD codes for operations and non-OR procedures.

> *Cancel Scheduled Operation* \[SRSCAN\]

> This option is used to cancel a scheduled operation on a given date. When a scheduled case is cancelled, a new request is automatically generated for that case on the same date.

> *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] This option is used to enter or edit information related to cardiac procedures requiring cardiopulmonary bypass for the cardiac surgery risk assessments.

> *Cardiac Risk Assessment Information (Enter/Edit)* \[SROA CARDIAC ENTER/EDIT\]

> This menu contains options to enter or edit assessment information for the cardiac risk assessments.

> *Chief of Surgery Menu* \[SROCHIEF\]

> This menu contains the various options designed for use by the Chief of Surgery and his package coordinator.

### Circulating Nurse Staffing Report \[SROCNR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides nurse-staffing information, sorted by the circulating nurses’ name.

> *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]

> This option is used to enter the clinical information required for the cardiac surgery risk assessments.

> *Comments* \[SROMEN-COM\]

> This option is used to enter general comments about a case.

### Comparison of Preop and Postop Diagnosis \[SROPPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report contains completed cases in which the principal preoperative and principal postoperative diagnoses are different.

> *Create Service Blockout* \[SRSBOUT\]

#### This option is used to block out times on the Operating Room Schedule by surgical specialty.

> *Cumulative Report of CPT Codes* \[SROACCT\]

> This report displays the total number of each CPT code entered for the date range selected. It also breaks down the totals into two categories, principal procedures and other operative procedures.

### Deaths Within 30 Days of Surgery \[SROQD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lists patients who had surgery within the selected date range and who died within 30 days of surgery. Two separate reports are available through this option.

#### Total Cases Summary

> This report can be printed in one of three ways.

- All Cases: The report lists all patients who had surgery within the selected date range and who died within 30 days of surgery, along with all of the patients’ operations that were performed during the selected date range. These patients are included in the postoperative deaths totals on the Quarterly Report.
- Outpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as outpatient (ambulatory) deaths on the Quarterly Report.
- Inpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as inpatient deaths. Although the count of deaths associated with inpatient cases is not a part of the Quarterly Report, this report is provided to help with data validation.

#### Specialty Procedures

> This report will list the surgical cases that are associated with deaths that are counted for the national surgical specialty linked to the local surgical specialty. Cases are listed by national surgical specialty.

> *Delay and Cancellation Reports* \[SRO DEL MENU\]

> This menu contains various reports used to track delays and cancellations.

> *Delete Service Blockout* \[SRSBDEL\]

> This option is used to delete service blockouts already existing on a schedule.

> *Delete a Patient from the Waiting List* \[SROW-DELETE\]

> This option is used to delete a patient currently on the surgery waiting list for a selected service.

### Delete or Update Operation Requests \[SRSUPRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to delete, change the date, or update the information entered on a requested operation.

> *Display Availability* \[SRODISP\]

> This option provides a graph of the availability of operating rooms. Times that are unavailable will be marked by “X”s.

> *Edit Non-O.R. Procedure* \[SRONOP-EDIT\]

> This option allows the editing of information on the pre-selected non-OR procedure.

> *Edit a Patient on the Waiting List* \[SROW-EDIT\]

> This option is used to edit a patient already on the waiting list for a selected surgical specialty.

> *Enter/Edit Transplant Assessments* \[SR TRANSPLANT ENTER/EDIT\]

> This option is used to enter the information required for the transplant assessments.

#### \*\*\*\*\*\*This option is no longer used after Patch SR\*3\*184\*\*

> *Enter Cardiac Catheterization & Angiographic Data* \[SROA CATHETERIZATION\] This option is used to enter or edit cardiac catheterization and angiographic information for cardiac surgery risk assessments.

> *Enter Irrigations and Restraints* \[SROMEN-REST\]

> This option is used to stuff in multiple restraints and positioning aids.

> *Enter PAC(U) Information* \[SROMEN-PACU\]

> This option is used to enter or edit recovery room scores and times.

> *Enter Referring Physician Information* \[SROMEN-REFER\]

> This option is used to enter the name, phone number, and address of the referring physician or institution.

> *Enter Restrictions for 'Person' Fields* \[SROKEY ENTER\]

> This option is used to enter restrictions on person fields. It will allow the user to add keys to existing entries in the PERSON FIELD RESTRICTION file (#131). If the field to be restricted has not already been entered in the PERSON FIELD RESTRICTION file (#131), the user may enter it along with the restricting keys through this option.

> *Enter a Patient on the Waiting List* \[SROW-ENTER\]

> This option is used to enter a patient on the waiting list for a selected surgical specialty.

> *Ensuring Correct Surgery Compliance Report* \[SRO ECS COMPLIANCE\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option produces the Ensuring Correct Surgery Compliance Report. This report is a two-part report:

1)  the compliance summary and (2) the list of non-compliant cases. The report is printed for a selected date range and may be sorted by surgical specialty. This report is a tool for reviewing compliance with the documentation process for ensuring correct surgery.

> *Exclusion Criteria (Enter/Edit)* \[SR NO ASSESSMENT REASON\] This option is used to flag major cases that will not have a surgery risk assessment due to certain exclusion criteria.

> *File Download* \[SRHL DOWNLOAD INTERFACE FILES\]

> This option is used to download Surgery interface files to the Automated Anesthesia Information System (AAIS). The process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send Health Level 7 (HL7) master file updates.

### Flag Drugs for Use as Anesthesia Agents \[SROCODE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to flag drugs for use as anesthesia agents. Only those drugs that are flagged will be available when selecting anesthesia agents.

> *Flag Interface Fields* \[SRHL INTERFACE FLDS\]

> This option allows the package coordinator to set the INTERFACE field in the SURGERY INTERFACE file (#133.2). The categories listed on the first screen correspond to entries in the SURGERY INTERFACE file (#133.2). These categories are listed in the Surgery Health Level 7 Interface Specifications document as being the OBR (Observation Request) text identifiers. Each identifier corresponds to several fields in the VistA Surgery package. This allows the user to control the flow of data between the VistA Surgery package and the ancillary system on a field-by-field basis.

> The option lists each identifier and its current setting. To receive the data coming from the ancillary system for a category, set the flag to R for receive. To ignore the data, set the flag to N for not receive. To see a second underlying layer of OBX (Observation Information) text identifiers (fields in SURGERY file (#130) and their settings), set the OBR text identifier to RR for receive. The option will allow the user to toggle the settings for a range or for individual items.

> *Intraoperative Occurrences (Enter/Edit)* \[SRO INTRAOP COMP\]

> This option is used to enter or edit intraoperative occurrences. Every occurrence entered must have a corresponding perioperative occurrence category.

> *Key Missing Surgical Package Data* \[SROQ MISSING DATA\]

> This option generates a list of surgical cases performed within the selected date range that are missing key information. This report includes surgical cases with an entry in the TIME PAT IN OR field and does not include aborted cases.

> *Laboratory Interim Report* \[SRO-LRRP\]

> This option will print or display interim reports for a selected patient, within a given time period. The printout will go in inverse date order. This report will output all tests for the time period specified. If no results are available, the option will ask for another patient. This option will only print verified results and at present does not output the microbiology reports.

> *Laboratory Test Results (Enter/Edit)* \[SROA LAB\]

> This option is used to enter or edit laboratory information for an individual risk assessment.

> *Laboratory Test Results (Enter/Edit)* \[SROA LAB-CARDIAC\]

> This option is used to enter or edit laboratory information for an individual Cardiac risk assessment.

### List Completed Cases Missing CPT Codes \[SRSCPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Completed Cases Missing CPT Codes option generates a report of completed cases that are missing the Principal CPT code for a specified date range. It is important to note that only procedures that have CPT codes will be counted on the Annual Report of Surgical Procedures.

> *List Operation Requests* \[SRSRBS\]

> This option is designed to list requested cases, including those patients on the waiting list. It will print all future requests, sorted by ward location or surgical specialty.

> *List Scheduled Operations* \[SRSCD\]

> This option is designed to provide a short form listing of scheduled cases for a given date. It will sort by surgical specialty, operating room, or ward location and is designed to be displayed on the user’s CRT.

> *List of Anesthetic Procedures* \[SROANP\]

> This option generates the List of Anesthetic Procedures for a specified date range.

### List of Invasive Diagnostic Procedures \[SROQIDP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\* Not used after patch SR\*3\*175 \*\*

> This option provides a report listing the completed surgical cases that were performed during the selected date range and that have a principal CPT code on the list defined by Surgical Service at VHA Headquarters as invasive diagnostic procedures.

> *List of Operations* \[SROPLIST\]

> This report contains general information for completed cases within a selected date range. It includes the procedure(s), surgical service, surgeons and case type.

> *List of Operations (by Postoperative Disposition)* \[SRO CASES BY DISPOSITION\] This report will list completed cases for a selected date range sorted by postoperative disposition and by surgical specialty.

> *List of Operations (by Surgical Priority)* \[SRO CASES BY PRIORITY\] This report will list completed cases for a specified date range sorted by the surgical priority (elective, emergent, etc.). The patient name, patient social security number (SSN), date of operation, operative procedure, and surgical specialty will be displayed for each case.

> *List of Operations (by Surgical Specialty)* \[SROPLIST1\]

> This report contains general information for completed cases within a selected date range, sorted by surgical specialty. It includes procedure(s), surgical specialty, surgeons and case type.

> *List of Operations Included on Quarterly Report* \[SROQ LIST OPS\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option generates a list of completed operations that are included in the totals displayed on the Quarterly Report. The report displays the data fields that are checked by the Quarterly Report.

> *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\]

> This option is used to print the List of Surgery Risk Assessments reports.

> *List of Transplant Assessments* \[SRTP ASSESSMENT LIST\]

> This option is used to print the List of Transplant Assessments. It will provide summary information for assessments within the sort parameters selected.

> \*\*\*\*\*\*This option is no longer used after Patch SR\*3\*184\*\*

### List of Unverified Surgery Case \[SROUNV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will generate a list of all completed surgery cases that have not had the procedure, diagnosis and complications verified.

> *M&M Verification Report* \[SRO M&M VERIFICATION REPORT\]

> The *M&M Verification Report* option produces the M&M Verification Report, which may be useful for:

- reviewing occurrences and their assignment to operations
- reviewing death unrelated/related assignments to operations

> The full report includes all patients who had operations within the selected date range who experienced intraoperative occurrences, postoperative occurrences or death within 90 days of surgery. The pre- transmission report is similar but includes operations with completed risk assessments that have not yet transmitted to the national database.

#### Full Report:

> Information is printed by patient, listing all operations for the patient that occurred during the selected date range, plus any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that were performed prior to the selected date range and, if printed by specialty, may include operations performed by other specialties. For every operation listed, the intraoperative and postoperative occurrences are listed. The report indicates if the operation was flagged as unrelated or related to death and the risk assessment type and status. The report may be printed for a selected list of surgical specialties.

#### Pre-Transmission Report:

> Information is printed in a format similar to the full report. This report lists all completed risk assessed operations that have not yet transmitted to the national database and that have intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The report includes any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that may or may not be risk assessed, and, if risk assessed, may have a status other than 'complete'. However, every patient listed on this report will have at least one operation with a risk assessment status of 'complete'.

> *Maintain Surgery Waiting List* \[SROWAIT\]

> This menu contains options to enter, edit, and delete patients on the surgery waiting list. It also includes an option to print the list.

> *Make Operation Requests* \[SROOPREQ\]

> This option is used to “book” operations for a selected date. This request will in turn be scheduled for a specific operating room at a specific time on that date.

> *Make a Request for Concurrent Cases* \[SRSREQCC\]

> This option is used to request concurrent operative procedures.

### Make a Request from the Waiting List \[SRSWREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to “book” a patient for surgery that has been entered on the waiting list. The operative procedure and specialty will be stuffed automatically.

> *Make Reports Viewable in CPRS* \[SR VIEW HISTORICAL REPORTS\] This option allows Operation Reports, Nurse Intraoperative Reports, Anesthesia Reports and Procedure Reports (Non-O.R.) for historical cases to be moved into TIU as "electronically unsigned" to make them viewable through the Computerized Patient Record System (CPRS).

> *Management Reports* \[SR MANAGE REPORTS\]

> This menu contains various management type reports used by the surgical service.

> *Management Reports* \[SRO-CHIEF REPORTS\]

> This menu contains various management reports to be generated by the Chief of Surgery.

> *Medications (Enter/Edit)* \[SROANES MED\]

> This option is used to enter or edit medications given during the operative procedure.

> *Monthly Surgical Case Workload Report* \[SROA MONTHLY WORKLOAD REPORT\] This option generates the Monthly Surgical Case Workload Report that may be printed and/or transmitted to the VASQIP national database.

### Morbidity & Mortality Reports \[SROMM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates the Morbidity and Mortality Reports to be used by the Chief of Surgery. This option includes the Mortality Report and Perioperative Occurrences Report.

> *Non-Cardiac Assessment Information (Enter/Edit)* \[SROA ENTER/EDIT\]

> This menu contains options used to enter and edit information related to individual risk assessments.

> *Non-O.R. Procedure Info* \[SR NON-OR INFO\]

> This option displays information on the selected non-OR procedure except the provider’s dictated summary. This information may be printed or reviewed on the screen.

> *Non-O.R. Procedures* \[SRONOP\]

> This menu contains options related to non-O.R. procedures.

> *Non-O.R. Procedures (Enter/Edit)* \[SRONOP-ENTER\]

> This option is used to enter, update, or delete information related to non-OR procedures.

### Non-Operative Occurrences (Enter/Edit) \[SROCOMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter or edit occurrences that are not related to surgical procedures.

> *Normal Daily Hours (Enter/Edit)* \[SR NORMAL HOURS\]

> This option is used to enter or edit the daily start and end times for each operating room. The information is used to set up the start and end times, for operating room utilization, on a weekly basis.

> *Nurse Intraoperative Report* \[SRONRPT\]

> This option generates the Nurse Intraoperative Report, which contains surgical case information documented by nursing staff. Before the report is electronically signed, the option displays information directly from the SURGERY file (#130), giving the user choices to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the signed report to be viewed or printed.

> *Nurse Intraoperative Report* \[SRCODING NURSE REPORT\] Coders use this option to print the Nurse Intraoperative Report for an operation. If the report is not electronically signed, the option displays information directly from the SURGERY file (#130), giving the choice to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the signed report to be viewed or printed. This report is not available for non-OR procedures.

### Operating Room Information (Enter/Edit) \[SRO-ROOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter or edit information pertinent to each operating room, including start and end times, and the cleaning time.

> *Operating Room Utilization (Enter/Edit)* \[SR UTIL EDIT ROOM\]

> This option is used to enter or edit start and end times for operating rooms on a selected date.

> *Operating Room Utilization Report* \[SR OR UTL1\]

> This report prints utilization information for a selected date range for all operating rooms or for a single operating room. The report displays the percent utilization, the number of cases, the total operation time and the time worked outside normal hours for each operating room individually and all operating rooms collectively.

> The percent utilization is derived by dividing the total operation time for all operations (including total time patients were in OR, plus the cleanup time allowed for each case, plus one hour allowance for startup and shutdown daily for each OR that had at least one case) by the total OR functioning time as defined in the SURGERY UTILIZATION file (#131.8). The quotient is then multiplied by 100.

> *Operation* \[SROMEN-OP\]

> This option is used to enter or edit information determined during the operative procedure.

> *Operation (Short Screen)* \[SROMEN-OUT\]

> This screen is designed for surgical procedures performed on outpatient or ambulatory patients with local anesthesia.

> *Operation Information* \[SROMEN-OPINFO\]

> This one page display allows the user to quickly reference primary information for a given case. There are no editing capabilities in this option.

> *Operation Information (Enter/Edit)* \[SROA OPERATION DATA\]

> This option is used to enter or edit information related to the operation.

> *Operation Menu* \[SROPER\]

> This menu contains the various options used to enter and display information for a selected surgical case.

> *Operation Report* \[SROSRPT\]

> This option generates the Operation Report. This report consists of the electronically signed operative summary (surgeon’s dictation) stored in the Text Integration Utilities (TIU) software.

> *Operation Requests for a Day* \[SROP REQ\]

> This option will generate a list of requested operations for a specific date. There are two formats (long and short form) in which the requests may be printed.

> *Operation Startup* \[SROMEN-START\]

> This option is used to enter information prior to the actual start of the operation.

> *Operation/Procedure Report* \[SRCODING OP REPORT\]

> Coders use this option to print the Operation Report on an operation or the Non-O.R. Procedure Report on a non-OR procedure.

> *Operative Risk Summary Data (Enter/Edit)* \[SROA CARDIAC OPERATIVE RISK\]

> This option is used to enter or edit operative risk summary data for the cardiac surgery risk assessments.

> *Outcome Information (Enter/Edit)* \[SROA OUTCOMES\]

> This option is used to enter or edit postoperative information including complication outcomes, discharge diagnosis, and postoperative length of stay.

> *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\]

> \*\* Not used after patch SR\*3\*184 \*\*

> This option is used to enter or edit outcome information for cardiac procedures.

> *Outpatient Encounters Not Transmitted to NPCD* \[SRO PCE NOTRANS\] Outpatient surgical and non-OR procedures that are filed as encounters in the Patient Care Encounters (PCE) package without an active, count clinic identified for each encounter are not transmitted to the National Patient Care Database (NPCD) as workload. This option may be used as a tool for identifying

> these encounters that represent uncounted workload so that corrective actions may be taken in the Surgery package to insure these procedures are associated with an active, count clinic. After corrections are made, these encounters may be re-filed with PCE to be transmitted to NPCD.

> This option provides functionality to:

- Count and/or list surgical cases and non-OR procedures that have entries in PCE but have no matching entries in the OUTPATIENT ENCOUNTER file (#409.68) or have matching entries that are non-count encounters or encounters requiring action.
- Re-file with PCE the cases identified as having no matching entries in the OUTPATIENT ENCOUNTER file (#409.68) or having matching entries that are non-count encounters or encounters requiring action.

> Both the report and the re-filing process may be run for OR surgical cases, non-OR procedures, or both. The report and the re-filing process may be run for a specific specialty or for all specialties, and may be run for a selected date range.

> *PCE Filing Status Report* \[SRO PCE STATUS\]

> This option provides a report of the PCE filing status of completed cases performed during the selected date range in accordance with the site parameter controlling PCE updates. If this site parameter is turned off, the report will show no cases. The report may be printed for OR surgical cases, non-OR procedures or both. Also, the report may be printed for all specialties or for a single specialty only.

> This report is intended to be used as a tool in the review of Surgery case information that is passed automatically to PCE. The report uses 2 status categories:

1.  FILED - This status indicates that case information has already been filed with PCE.
2.  NOT FILED - This status indicates that the case information has not been filed with PCE. The case may or may not be missing information needed to file with PCE.

> Two forms of the report are available: the long and the short. The long form uses a 132 column format and prints case information including the surgeon/provider, the attending, the specialty, the principal post- op diagnosis, and the principal procedure. If the PCE filing status is FILED, the CPT codes and ICD diagnosis codes will be printed. If the filing status is NOT FILED, information fields needed for PCE filing that do not contain data will be printed. At the end of the report, the number of cases in each PCE filing status will be printed, plus the number of CPT and ICD codes for cases with a status of FILED.

> The short form uses an 80-column format and does not include surgeon/provider, attending, principal post-op diagnosis, CPT, or ICD code information. The totals printed at the end will show only the total cases for each status.

> *Patient Demographics (Enter/Edit)* \[SROA DEMOGRAPHICS\] This option is used to enter, edit or review risk assessment patient demographic information such as patient movement dates, length of postoperative hospital stay, race, in/out-patient status and other information related to this surgical episode.

> *Perioperative Complications (Enter/Edit)* \[SROA CARDIAC COMPLICATIONS\] This option is used to enter or edit perioperative complication information for cardiac surgery risk assessments.

> *Perioperative Occurrences Menu* \[SRO COMPLICATIONS MENU\] This menu contains options used to enter, edit, and display perioperative occurrence information. It is only accessible to those users that hold the SROCOMP security key.

> *Person Field Restrictions Menu* \[SROKEY MENU\]

> This menu contains options used to maintain restrictions applied to "person" type fields in files. One or more keys may be entered so that only those who have at least one of them may be entered in a particular field.

> *Post Operation* \[SROMEN-POST\]

> This option is used to enter or edit information obtained after the operation.

> *Postoperative Occurrences (Enter/Edit)* \[SRO POSTOP COMP\]

> This option is used to enter or edit information related to postoperative occurrences.

> *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\]

> The nurse reviewer uses this option to enter or edit preoperative assessment information.

> *Print 30 Day Follow-up Letters* \[SROA REPRINT LETTERS\] This option is used to print 30-day follow up letters. When using this option, letters can be printed for a specific assessment or all assessments within a selected date range.

> *Print Blood Product Verification Audit Log* \[SR BLOOD PRODUCT VERIFY AUDIT\] This option is used to print the KERNEL audit log for the Surgery *Blood Product Verification* \[SRBLOOD PRODUCT VERIFICATION\] option.

> *Print Surgery Waiting List* \[SRSWL2\]

> This option generates the long-form surgery waiting list for the surgical service(s) selected.

> *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]

> This option is used to print an entire Surgery Risk Assessment for an individual patient.

> *Print Transplant Assessment* \[SRTP PRINT ASSESSMENT\]

> This option is used to print a Surgery Transplant Assessment for an individual patient.

#### \*\*\*\*\*\*This option is no longer used after Patch SR\*3\*184\*\*

> *Procedure Report (Non-O.R.)* \[SR NON-OR REPORT\]

> This option generates the Procedure Report (Non-O.R.). This report consists of the electronically signed procedure summary (provider’s dictation) stored in the Text Integration Utilities (TIU) software.

> *Purge Utilization Information* \[SR PURGE UTILIZATION\] This option is used to purge utilization information for a selected date range. After selecting a starting date, the user may purge all utilization information for dates prior to, and including, that starting date.

> *Quarterly Report - Surgical Service* \[SRO QUARTERLY REPORT\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option will generate the Quarterly Report to be submitted to the Surgical Service, Central Office. The option also provides the flexibility to print the summary report for selected date ranges.

> Quarterly Report Menu \[SROQ MENU\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This menu contains the option to generate the Quarterly Report and the associated options that may be helpful in validating information on the Quarterly Report.

> *Queue Assessment Transmissions* \[SROA TRANSMIT ASSESSMENTS\]

> This option may be used to manually queue the VASQIP transmission process to run at a selected time. The VASQIP transmission process is a part of the nightly maintenance and cleanup process.

> *Remove Restrictions on 'Person' Fields* \[SROKEY REMOVE\]

> This option is used to delete keys that have been assigned to a field to restrict entries. Using this option the user may delete one specific key, or all keys.

> *Report of CPT Coding Accuracy* \[SR CPT ACCURACY\]

> This report prints cases sorted by the CPT code used for principal and other operative procedures. It is designed as a tool to check the accuracy of coding procedures.

> *Report of Cancellation Rates* \[SROCRAT\]

> This option generates the Report of Cancellation Rates. The report can be printed for an individual Surgical Specialty, or the entire medical center. The report shows the following three rates:

1)  The cancellation percentage of all scheduled cases, calculated as follows: (TOTAL CANCELS / TOTAL SCHEDULED) x 100
2)  The avoidable cancellation percentage of all scheduled cases, calculated as follows: (TOTAL AVOIDABLE CANCELS / TOTAL SCHEDULED) x 100
3)  The avoidable cancellation percentage of all cancelled cases, calculated as follows: (TOTAL AVOIDABLE CANCELS / TOTAL CANCELS) x 100

> *Report of Cancellations* \[SROCAN\]

> This report provides information for cases that have been scheduled and cancelled.

> *Report of Cases Without Specimens* \[SROSPEC\]

> This report lists all completed cases in which there were no specimens taken from the operative site. It can be printed for an individual surgical specialty if desired.

### Report of Daily Operating Room Activity \[SROPACT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a list of cases started between 6:00 AM on the date selected and 5:59 AM of the following day for all operating rooms.

> *Report of Delay Reasons* \[SROREAS\]

> This option prints the Report of Delay Reasons. This report will display the total number of times each reason was used for the date range selected. It can be sorted by surgical specialty or displayed for an individual surgical specialty.

> *Report of Delay Time* \[SRO DELAY TIME\]

> This report provides the total amount of delay time for each delay reason over a specified range of dates.

> *Report of Delayed Operations* \[SRODELA\]

> This report displays all cases that have been delayed. It will display both the delay cause and delay time.

> *Report of Non-O.R. Procedures* \[SRONOR\]

> This report lists chronologically Non-OR Procedures sorted by Medical Specialty, by provider, or by location.

> *Report of Non-O.R. Procedures* \[SRONOR-CODERS\]

> This report lists chronologically Non-OR Procedures sorted by Medical Specialty, by provider or by location.

> *Report of Normal Operating Room Hours* \[SR OR HOURS\]

> This report outputs the start time and the end time of the normal working hours for all operating rooms or for the selected operating room for each date within the specified date range. The total time of the normal working day is displayed for each operating room for each date.

> *Report of Returns to Surgery* \[SRORET\]

> This option generates a report listing information related to cases that have related surgical procedures within 30 days of the date of the operation.

> *Report of Surgical Priorities* \[SRO SURGICAL PRIORITY\] This report provides the total number of surgical cases for each Surgical Priority (i.e. Elective, Emergent, Urgent). It can be sorted by Surgical Specialty and printed for a specific specialty.

### Report of Unscheduled Admissions to ICU \[SROICU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all unscheduled admissions to the ICU based on the requested (expected) postoperative care and actual postoperative disposition.

> *Request Operations* \[SROREQ\]

> This menu contains the various options used to make, delete, update and display requested operations.

> *Requests by Ward* \[SROWRQ\]

> This option prints request information for all wards, or a specific ward.

### Reschedule or Update a Scheduled Operation \[SRSCHUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to change the date, time or operating room for which a case is scheduled. It may also be used to update information entered when the case was requested or scheduled.

> *Resource Data* \[SROA CARDIAC RESOURCE\] This option is used to enter, edit or review risk assessment cardiac patient demographic information such as hospital admission and discharge dates and other information related to this surgical episode.

> *Review Request Information* \[SROREQV\]

> This option is used to review or edit request information for an individual case.

> *Risk Model Lab Test (Enter/Edit)* \[SROA LAB TEST EDIT\]

> This option is used to allow the nurse to map VASQIP data in the Risk Model Lab Test (#139.2) file.

> *Schedule Anesthesia Personnel* \[SRSCHDA\]

> This option is used to schedule anesthesia personnel for surgery cases.

> *Schedule Operations* \[SROSCHOP\]

> This menu contains the various options used to schedule, update, cancel and display scheduled operations.

> *Schedule Requested Operations* \[SRSCHD1\]

> This option is used to schedule cases that have been previously “booked” for the selected date.

### Schedule Unrequested Concurrent Cases \[SRSCHDC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to schedule concurrent cases that have not been requested.

> *Schedule Unrequested Operations* \[SROSRES\]

> This option is used to schedule cases that have not been previously “booked.” The user will be asked to enter some initial information regarding this case as well as the operating room and date/time for it to be scheduled.

> *Schedule of Operations* \[SROSCH\]

> This option generates the Operating Room Schedule to be used by the OR nurses, surgeons and anesthetists.

> *Scrub Nurse Staffing Report* \[SROSNR\]

> This report contains general information for completed cases, sorted by the Operating Room Scrub Nurse.

> *Surgeon Staffing Report* \[SROSUR\]

> This report prints completed cases, sorted by the surgeon and his role (i.e. attending, first assistant) for each case. It includes the procedure, diagnosis and operation date/time.

### Surgeon's Verification of Diagnosis & Procedures \[SROVER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to verify that the procedure(s), diagnosis and complications are correct for the case. It is intended for use by the Surgeon, not the OR nurses.

> *Surgery Interface Management Menu* \[SRHL INTERFACE\]

> This menu contains options that allow the user to set up certain interface parameters that control the processing of HL7 messages. The interface adheres to the Health Level 7 (HL7) protocol and forms the basis for the exchange of health care information between the VistA Surgery package and any ancillary system.

> *Surgery Menu* \[SROMENU\]

> This is the main menu for the Surgery package.

> *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\]

> This option is queued to run daily. It initiates a number of background tasks to clean up the surgery database and update all appropriate information. Among the tasks done are calculation of average procedure times, cleanup of outstanding requests, update expected start and end times for operating rooms and surgical specialties, and locking cases.

> *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] This menu contains options used to manage the Surgery package. It includes options to maintain site- configurable information within the package.

> *Surgery Reports* \[SRORPTS\]

> This menu contains the various reports used in the Surgery package. Those reports that are restricted to the Chief of Surgery do not appear within this menu.

> *Surgery Request* \[SR SURGERY REQUEST\]

> This protocol allows the entry and editing of operation requests through OE/RR.

### Surgery Risk Assessment - Site Update Server \[SROASITE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This server is used to update Surgery Risk Assessments that have been successfully transmitted to the Surgery Risk Assessment National Database. This server updates two fields, ASSESSMENT STATUS (#235) and DATE TRANSMITTED (#260). These fields are updated at the site from the message sent by the database servers only if the messages were processed successfully into the national database.

> *Surgery Risk Assessment Menu* \[SROA RISK ASSESSMENT\]

> This menu contains options used to create, maintain, and transmit surgery risk assessments.

> *Surgery Site Parameters (Enter/Edit)* \[SROPARAM\]

> This option is used to create or update local site parameters for the Surgery package.

> *Surgery Staffing Reports* \[SR STAFFING REPORTS\] This menu contains surgical staffing reports for surgeons and nurses.

> *Surgery Transplant Assessment - Site Update Server* \[SRTPSITE\]

> This server is used to update Surgery Transplant Assessments that have been successfully transmitted to the Surgery Risk Assessment National Database at the Chicago ISC. This server updates two fields, ASSESSMENT STATUS (#181) and DATE TRANSMITTED (#184). These fields are updated at the site from the message sent by the database servers at Chicago only if the messages were processed successfully into the national database.

> *Surgery Utilization Menu* \[SR OR UTIL\]

> This menu contains various Operating Room Utilization reports.

> *Surgical Nurse Staffing Report* \[SRONSR\]

> This option generates the Surgical Nurse Staffing Report for a specified date range.

> *Surgical Staff* \[SROMEN-STAFF\]

> This option is used to enter the staff (surgeons, nurses, anesthetists) for a given case. It includes everyone in the operating room for this case.

> *Table Download* \[SRHL DOWNLOAD SET OF CODES\]

> This option downloads the SURGERY file (#130) set of codes to the Automated Anesthesia Information System (AAIS). This process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send HL7 master file updates.

> *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\]

> This option is used to enter information related to Time Out Verified Utilizing Checklist.

> *Tissue Examination Report* \[SROTRPT\]

> This option is used to generate the Tissue Examination Report that contains culture and specimens sent to the laboratory.

> *Transplant Assessment Menu* \[SR TRANSPLANT ASSESSMENT\]

> \*\* Not used after patch SR\*3\*184 \*\*

> This menu contains options to enter or edit transplant assessment information, print transplant assessments, list transplant assessments, and manage transplant assessments.

> *Transplant Assessment Parameters (Enter/Edit)* \[SR TRANSPLANT PARAMETERS\] This option is used to update local site parameters for the Surgery Transplants Assessment module. Each site can identify which type of organ transplant is performed or assessed by their Transplant Coordinator. Identification of the type of organ transplants done at your facility will streamline selections when doing data entry.

#### \*\*\*\*\*\*This option is no longer used after Patch SR\*3\*184\*\*

> *Unlock a Case for Editing* \[SRO-UNLOCK\]

> The Chief of Surgery (or a person designated by the Chief) uses this option to unlock a case that has been completed and locked.

> *Update 1-Liner Case* \[SROA ONE-LINER UPDATE\]

> This option may be used to enter missing data for the 1-liner cases (major cases marked for exclusion from assessment, minor cases and cardiac assessed cases that transmit to the VASQIP database as a single line or two of data). Cases edited with this option will be queued for transmission to the VASQIP database at Chicago.

> *Update Assessment Completed/Transmitted in Error* \[SROA TRANSMITTED IN ERROR\] This option is used to update the status of a completed or transmitted assessment that has been entered in error. The status will change from “COMPLETED” or “TRANSMITTED” to “INCOMPLETE” so that editing may occur.

> *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\]

> This option is used to update the status of a risk assessment entry from “INCOMPLETE” to “COMPLETE.” Only completed assessments can be transmitted.

> *Update Cancellation Reason* \[SRSUPC\]

#### This option is used to update the cancellation date and reason previously entered for a selected surgical case.

> *Update Cancelled Case* \[SRO UPDATE CANCELLED CASE\]

> This option allows the Chief of Surgery to update information on a cancelled case.

> *Update Interface Parameter Field* \[SRHL PARAMETER\]

> This option may be used to edit the site parameter that determines which Surgery HL7 interface is used, the interface compatible with VistA HL7 V. 1.6 or the older one compatible with VistA HL7 V. 1.5.

> If applications communicating with the Surgery HL7 interface must use the interface designed for use with HL7 V. 1.5, enter YES. Otherwise, enter NO or leave this field blank.

> *Update O.R. Schedule Devices* \[SR UPDATE SCHEDULE DEVICE\] This option is used to update the list of O.R. Schedule Devices in the SURGERY SITE PARAMETERS file (#133).

> *Update Operations as Unrelated/Related to Death* \[SRO DEATH RELATED\]

> This option is used to update the status of operations performed within 90 days prior to death as unrelated or related to death, allowing comments to be entered to further document the review of death.

> *Update Site Configurable Files* \[SR UPDATE FILES\]

> This option is used to add, edit, or delete information in the site configurable files contained within the Surgery package.

> File entries that are not to be used should be made inactive and should not be deleted from the file.

> *Update Staff Surgeon Information* \[SROSTAFF\]

> This option allows the designation of a user as a staff surgeon by assigning the security key “SR STAFF SURGEON.” The Annual Report of Surgical Procedures counts cases performed by holders of this

> security key as performed by “STAFF.” All other cases are counted as performed by 'RESIDENT'.

> *Update Status of Returns Within 30 Days* \[SRO UPDATE RETURNS\]

> This option is used to update the status of Returns to Surgery within 30 days of a surgical case.

> <span id="_bookmark23" class="anchor"></span>*Update/Verify Procedure/Diagnosis Codes* \[SRCODING EDIT\]

> This option is used to edit and/or verify the final CPT and final ICD codes for an operation or non-OR procedure.

> *View Patient Perioperative Occurrences* \[SROMEN-M&M\]

> This option displays perioperative occurrence information for a given case.

### Wound Classification Report \[SROWC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a report for the selected date range showing the total number of surgical cases with each of the various wound classifications broken down by surgical service.

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the templates provided with the Surgery package.

# Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are input templates included with the Surgery package.

> SREQUEST file \#130

> <span id="_bookmark26" class="anchor"></span>SREQUEST-ICD10 file \#130

> SRISK-MISC file \#130

> SRISK-NOCARD file \#130

> SRISK-NOCOMP file \#130

> SRNON-OR file \#130

> SRNORRPT file \#130

> SRO-NOCOMP file \#130

> SROANES-AMIS file \#130

> SROARPT file \#130

> SROCOMP file \#130

> SROMEN-ANES file \#130 SROMEN-ANES TECH file \#130 SROMEN-COMP file \#130

> SROMEN-OPER file \#130

> SROMEN-OUT file \#130

> SROMEN-PACU file \#130

> SROMEN-POST file \#130

> SROMEN-REFER file \#130

> SROMEN-STAFF file \#130

> SROMEN-START file \#130

> SROMEN-VERF file \#130

> SROMEN-VERF1 file \#130

> SROMEN-VERF2 file \#130

> SRONRPT file \#130

> SRONRPT1 file \#130

> SRONRPT2 file \#130

> SROSRPT file \#130

> SROTHER file \#130

> SROVER file \#130

> SRPARAM file \#133

> SRSCHED-UNREQUESTED file \#130

> SRSCHED-UNREQUESTED-ICD10 file \#130

> SRSREQV file \#130

> SRSRES-ENTRY file \#130

> SRSRES-ENTRY1 file \#130

> SRSRES-SCHED file \#130

> SRSRES-SCHED1 file \#130

> SRSRES1 file \#130

> SRSRES2 file \#130

> SROALAB file \#139.2

> SR TRANSPLANT file \#133

# Sort Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One sort template is included:

> SR BLOOD PRODUCT VERIFICATION file \#19.081

# Editing Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input templates are used by package options that use the Surgery Screen Server to define the fields that are displayed for editing. These input templates may themselves be edited to add fields, to remove fields or to rearrange field display order. Below is a list of options used for entering operation or non-OR procedure information and the associated input templates used by the screen server.

| Option                               | Template |
|------------------------------------------|--------------|
| Surgical Staff \[SROMEN-STAFF\]          | SROMEN-STAFF |
| Operation Startup \[SROMEN-START\]       | SROMEN-START |
| Operation \[SROMEN-OP\]                  | SROMEN-OPER  |
| Operation (Short Screen) \[SROMEN-OUT\]  | SROMEN-OUT   |
| Post Operation \[SROMEN-POST\]           | SROMEN-POST  |
| Enter PAC(U) Information \[SROMEN-PACU\] | SROMEN-PACU  |
| Edit Non-O.R. Procedure \[SRONOP-EDIT\]  | SRNON-OR     |

# Globals in the Surgery Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package stores data in the following globals.

> ^SRF

> ^SRO

> ^SRP

> ^SRS

> ^SRT

> ^SRU

# Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The globals SR\* are recommended for journaling.

> *(This page included for two-sided copying.)*

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the archiving and purging processes related to the Surgery package.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgery V. 3.0 does not provide for the archiving of data.

# Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package contains the *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\] option, which should be tasked to run nightly for purging outstanding requests that have not been acted upon and are older than 14 days, based upon the requested date of operation. The Surgery package also includes an option within the Utilization module for purging information from the SURGERY UTILIZATION file (#131.8) prior to the selected date.

> *(This page included for two-sided copying.)*

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following routines have callable entry points and are available to other packages through Database Integration Control Agreements (ICRs).

#### SROANEST

> Entry point: ANESTIME

> This call returns an array containing multiple anesthesia time records, total anesthesia time in minutes, Surgical case number, Principal Diagnosis Code (internal value), Service Connected and Environmental Indicators.

> Input variable: DFN - The patient’s IEN in the PATIENT file (#2).

> SRFDATE - the start date of operation to begin looking for matching surgical cases. SRTDATE - the end date of operation to begin looking for matching surgical cases.

#### SROESL

> Entry point: CASLIST(SDFN,SIDN)

> This call generates a list of all signed Surgery reports of a given Report Identifier type for that patient. Input variable: SRDFN - The patient’s IEN in the PATIENT file (#2).

> SIDN – The identifier for the report.

#### SROGMTS

> Entry point: HS(IEN)

> This call extracts Surgery Reports from Surgery/TIU globals.

> Input variable: IEN - The Internal Entry Number of the SURGERY file (#130).

#### SROGTSR

> Entry point: GET(SRGY,SRDFN)

> This call returns an array containing a list of the patient’s operations.

> Parameter list: SRGY - the name of the array

> SRDFN - the patient’s IEN in the PATIENT file (#2)

#### SROPRPT

> Entry point: SROPRPT

> This call displays the Operation Report.

> Input variable: The variable SRTN (which identifies the surgical case) may be defined before making the call. If the variable SRTN is not defined when the call is made, the user will be prompted to select a patient and operation.

#### SROPS

> Entry point: SROPS

> This call provides patient lookup and operation selection.

#### SROSPLG

> Entry point: SROSPLG

> This call was designed specifically for the surgical pathology module of the LABORATORY package.

> Input variables: LRDFN - the patient’s IEN in the LAB DATA file (#63) LRSS - the laboratory subscript for surgical pathology (“SP”) LRI - the inverse date subscript the LAB DATA file (#63)

#### SROESTV

> Entry point: LIST(SRG,SRDFN,SRSDT,SREDT,SRMAX,SRLDOC)

> This call returns a list of completed cases between the start and end dates along with the associated documents.

> Parameter list: SRG- return array

> SRDFN - pointer to patient file (DFN) SRSDT - (optional) start date (earlier date) SREDT - (optional) end date (later date)

> SRMAX - (optional) maximum number of cases to return SRLDOC - (optional) if 0, do not list documents

#### SROSRPT

> Entry point: OPTOP(SRTN,SRLAST,SRG)

> This call returns Optop information on a surgical case.

> Input variable: SRTN - The IEN of the case in the SURGERY file (#130).

> Parameter list: SRLAST – determines if the Optop will be returned with a summary status at the end.

> SRG (optional) -- return array

#### SRSCLM

> Entry point: MSG

> The Communication Service Library (CSL) is given permission to call SRSCLM to pass information about surgery cases that the Supply Processing and Distribution (SPD) was unable to process due to problems with the HL7 transaction transmitted to SPD.

> Input variable: CSLCASE -- The IEN of the case in the Surgery file \#130.

> CSLTEXT – This is the reason behind CSL/SPD rejecting the Surgery case information.

#### SROTIUD

> Entry point: OS(SRTN)

> This entry point deletes the existing pointer in the TIU OPERATIVE SUMMARY field (#1000) of the Surgery file (#130) when a document is deleted, and it will then call the TIU API to generate a new Stub entry in TIU for that case.

> Parameter list: SRTN - IEN in SURGERY file (#130)

> Entry point: NON(SRTN)

> This entry point deletes the existing pointer in the TIU PROCEDURE REPORT (NON-OR) field (#1002) of the Surgery file (#130) when a document is deleted, and it will then call the TIU API to generate a new Stub entry in TIU for that case.

> Parameter list: SRTN - IEN in SURGERY file (#130)

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the packages needed to run the Surgery package, and also the calls that are made by the Surgery package to external routines.

# Packages Needed to Run Surgery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgery V. 3.0 relies minimally on the following external packages. This software is not included in this package and must be installed before Surgery V. 3.0 is completely functional.

| Package                        | Minimum Version Needed |
|------------------------------------|----------------------------|
| Kernel                             | 8.0                        |
| VA FileMan                         | 22.0                       |
| MailMan                            | 8.0                        |
| PIMS                               | 5.3                        |
| Laboratory                         | 5.2                        |
| Inpatient Medications              | 4.5                        |
| Pharmacy Data Management           | 1.0                        |
| Patient Care Encounter             | 1.0                        |
| Health Level Seven                 | 1.5                        |
| Order Entry/Results Reporting      | 3.0                        |
| Text Integration Utilities         | 1.0                        |
| Authorization/Subscription Utility | 1.0                        |
| Vitals                             | 5.0                        |

# Calls Made by Surgery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgery V. 3.0 makes calls to the following external routines:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><blockquote>
<p><strong>Entry Points Used</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>%DT</td>
<td>^%DT, DD</td>
</tr>
<tr class="even">
<td>%DTC</td>
<td>^%DTC, C, DW, H, NOW</td>
</tr>
<tr class="odd">
<td>%RCR</td>
<td>%XY</td>
</tr>
<tr class="even">
<td>%ZIS</td>
<td><blockquote>
<p>%ZIS, HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>%ZISC</td>
<td><blockquote>
<p>^%ZISC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>%ZISS</td>
<td><blockquote>
<p>ENDR, KILL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>%ZOSV</td>
<td><blockquote>
<p>$$EC, T0, T1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>%ZTLOAD</td>
<td><blockquote>
<p>^%ZTLOAD, $$S</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AUPNVSIT</td>
<td><blockquote>
<p>ADD, SUB</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CSLSUR1</td>
<td><blockquote>
<p>$$BLDSEG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DDIOL</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DGPMDDCF</td>
<td><blockquote>
<p>WIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DGPTFAPI</td>
<td><blockquote>
<p>RPC</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><blockquote>
<p><strong>Entry Points Used</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DGRPDB</td>
<td><blockquote>
<p>DIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DGUTL3</td>
<td><blockquote>
<p>$$BADADR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DGUTL4</td>
<td><blockquote>
<p>$$PTR2CODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIC</td>
<td><blockquote>
<p>^DIC,LIST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DICN</td>
<td><blockquote>
<p>WAIT, FILE, YN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DICRW</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DID</td>
<td><blockquote>
<p>$$GET1,FIELD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIE</td>
<td><blockquote>
<p>^DIE,CHK,FILE,HELP,UPDATE,WP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIFROM0</td>
<td><blockquote>
<p>Q</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DII</td>
<td><blockquote>
<p>OS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIK</td>
<td><blockquote>
<p>^DIK, DIE, EN, EN1, ENALL, IX1, IXALL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIKZ</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DILFD</td>
<td><blockquote>
<p>$$EXTERNAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DINIT</td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIP</td>
<td><blockquote>
<p>EN1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIQ</td>
<td><blockquote>
<p>$$GET1 ,D, EN, GETS, Y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIQ1</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIR</td>
<td><blockquote>
<p>^DIR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DITR</td>
<td><blockquote>
<p>I</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIU</td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIU2</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIWE</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIWP</td>
<td><blockquote>
<p>^DIWP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIWW</td>
<td><blockquote>
<p>^DIWW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>GMRADPT</td>
<td><blockquote>
<p>^GMRADPT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>GMRVUTL</td>
<td><blockquote>
<p>EN6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>GMRVUT0</td>
<td><blockquote>
<p>EN1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HLFNC</td>
<td><blockquote>
<p>$$FMDATE, $$FMNAME, $$HLDATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HLFNC2</td>
<td><blockquote>
<p>INIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HLMA</td>
<td><blockquote>
<p>GENERATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HLMA1</td>
<td><blockquote>
<p>GENACK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HLTRANS</td>
<td><blockquote>
<p>EN, EN1, INIT, KILL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ICDCODE</td>
<td><blockquote>
<p>$$ICDDX</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ICPTAPIU</td>
<td><blockquote>
<p>COPY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ICPTCOD</td>
<td><blockquote>
<p>$$CPT, $$CPTD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ICPTMOD</td>
<td><blockquote>
<p>$$MOD, $$MODP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LRBLB</td>
<td><blockquote>
<p>BAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LRBLBU</td>
<td><blockquote>
<p>^LRBLBU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MPIF001</td>
<td><blockquote>
<p>$$GETICN</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><blockquote>
<p><strong>Entry Points Used</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORVOM</td>
<td><blockquote>
<p>DOT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ORX</td>
<td><blockquote>
<p>FILE, RETURN, ST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSIVACT</td>
<td><blockquote>
<p>DCOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSSGIU</td>
<td><blockquote>
<p>END, ENS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSS50</td>
<td><blockquote>
<p>DATA</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSSDI</td>
<td><blockquote>
<p>DIC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSSHUIDG</td>
<td><blockquote>
<p>DRG</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PXAPI</td>
<td><blockquote>
<p>$$DATA2PCE, $$DELVFILE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SDCO21</td>
<td><blockquote>
<p>CL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIULC1</td>
<td><blockquote>
<p>$$DOCCLASS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TIULG</td>
<td><blockquote>
<p>$$PRNTGRP, $$PRNTMTHD, $$PRNTNBR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIULQ</td>
<td><blockquote>
<p>EXTRACT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TIUPUTU</td>
<td><blockquote>
<p>$$WHATITLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIUSROI</td>
<td><blockquote>
<p>ES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TIUSRVLR</td>
<td><blockquote>
<p>GETDOCS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIUSRVP</td>
<td><blockquote>
<p>DELETE, FILE, MAKE, MAKEADD, UPDATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TIUSRVP1</td>
<td><blockquote>
<p>$$CANDEL, DOCPARM, TGET</p>
</blockquote></td>
</tr>
<tr class="even">
<td>USRLM</td>
<td><blockquote>
<p>$$ISA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VADPT</td>
<td><blockquote>
<p>ADD ,DEM, ELIG, IN5, INP, KVA ,OERR, OPD, SVC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VAFHLPID</td>
<td><blockquote>
<p>$$EN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VASITE</td>
<td><blockquote>
<p>$$NAME, $$SITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VBECA1B</td>
<td><blockquote>
<p>AVUNIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VPRSR</td>
<td><blockquote>
<p>DEL, NEW, UPD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XLFDT</td>
<td><blockquote>
<p>$$FMADD, $$FMDIFF, $$FMTE ,$$HTFM, $$NOW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XLFSTR</td>
<td><blockquote>
<p>$$LJ, $$UP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XMA1C</td>
<td><blockquote>
<p>REMSBMSG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XMBGRP</td>
<td><blockquote>
<p>$$MG</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XMD</td>
<td><blockquote>
<p>^XMD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XPAR</td>
<td><blockquote>
<p>PUT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XPDUTL</td>
<td><blockquote>
<p>$$NEWCP, $$PARCP, $$PATCH, $$UPCP, $$VERSION, BMES, MES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XQALERT</td>
<td><blockquote>
<p>DELETEA, SETUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XUPARAM</td>
<td><blockquote>
<p>$$KSP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XUSESIG</td>
<td><blockquote>
<p>SIG</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Database Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package has Database Integration Control Registrations (ICRs) with other packages. For complete information regarding ICRs, please refer to the *DBA* \[DBA\] option on FORUM and then the *INTEGRATION CONTROL REGISTRATIONS* \[DBA INTEGRATION AGREEMENTS\] option.

> *(This page included for two-sided copying.)*

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the Surgery package options are designed to be standalone. Each option requires the use of the package-wide variable array SRSITE that is set as users enter the package. Locally created menus containing Surgery package options run quicker if the following exit action and entry action are included in the OPTION file (#19).

> EXIT ACTION: D EXIT^SROVAR ENTRY ACTION: D ^SROVAR

> *(This page included for two-sided copying.)*

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following Surgery namespaced local variables are package-wide variables.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Variable</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SRSITE</td>
<td><blockquote>
<p>This variable is the internal file number of the site in the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSITE("AML")</td>
<td><blockquote>
<p>This variable represents the mail code for the institution's anesthesia department as defined in the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSITE("DIV")</td>
<td><blockquote>
<p>This variable represents the division selected. It is the institution number in the INSTITUTION file (#4).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSITE("IV")</td>
<td><blockquote>
<p>This variable will equal 1 if IV orders are deleted upon admission to surgery. The value of this variable is derived from the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSITE("NRPT")</td>
<td><blockquote>
<p>This variable will equal 1 if the Nurse Intraoperative Report is to print all field titles. The value of this variable is derived from the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSITE("OPTION")</td>
<td><blockquote>
<p>This variable holds the internal file number of the entry option into the Surgery package. When this option is exited, the package-wide variables will be killed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSITE("REQ")</td>
<td><blockquote>
<p>This variable represents the cut-off time for making operation requests as defined in the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSITE("RISK")</td>
<td><blockquote>
<p>This variable represents whether the Surgery Risk Assessment Module is being used. The value of this variable is derived from the SURGERY SITE PARAMETERS file (#133).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSITE("SITE")</td>
<td><blockquote>
<p>This variable represents the name of the institution in the INSTITUTION file (#4).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRTN</td>
<td><blockquote>
<p>This variable is the internal entry number in the SURGERY file (#130). It also serves as the case number.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The SRSITE array is set when the user enters the Surgery package and is killed upon exit from the package. This array stores values from the SURGERY SITE PARAMETERS file (#133) that may be referenced by the package.

> SRTN is set when a surgery case is selected for editing or reviewing, and is killed or reset when another case is selected or when the user exits the menu or exits the package.

> *(This page included for two-sided copying.)*

> *(This page included for two-sided copying.)*

# Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites using the Surgery package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field Station Information Security Officers (ISOs) can obtain further assistance from their Network Information Security Officers.

> *(This page included for two-sided copying.)*

# Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the interface of the Surgery package to the Automated Anesthesia Information Systems.

# Interface for Automated Anesthesia Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package includes a generic interface to the Automated Anesthesia Information Systems. This interface is used by the VistA Surgery package in communicating with any Automated Anesthesia Information Systems or ancillary system for the purpose of exchanging health care information. The interface strictly adheres to the HL7 protocol and avoids using Z type segments to the protocol whenever possible. A detailed description of this interface can be found in the *Surgery Anesthesia Interface Specifications* on the VDL at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/) under the Surgery section.

> *(This page included for two-sided copying.)*

# Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With the implementation of the changes resulting from the Surgery Electronic Signature for Operative Reports project, which includes patch SR\*3\*100, the user is provided with the ability to electronically sign operative reports contained within the VistA Surgery package. Additionally, the Surgery Electronic Signature for Operative Reports project provides the user the ability to view these signed reports using CPRS by storing them within TIU. This new functionality is applied to the Surgeon’s Operation Report, the Nurse Intraoperative Report, the Procedure Report (Non-O.R.), and the Anesthesia Report.

> Electronic signatures may be established by using the *Electronic Signature Code Edit* \[XUSESIG\] option. In Kernel V. 8.0, the *Electronic Signature Code Edit* \[XUSESIG\] option has been tied to the Common Options, under the *User’s Toolbox* \[XUSERTOOLS\] submenu option for easy access by all users.

> *(This page included for two-sided copying.)*

# Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Screen displays can vary among different sites and the user may not see the data on the terminal exactly as the data is shown in this manual. Although screens are subject to modification, the major menu options, as they appear in this manual, are fixed and not subject to modifications except by the package developer. The following is a list of the major menu options and their sub-options, in the order in which they appear. A restricted option (the Chief of Surgery’s menu, for example) will not display if the user does not have the proper security clearance.

> Maintain Surgery Waiting List Locked with SROWAIT

> Print Surgery Waiting List

> Enter a Patient on the Waiting List Edit a Patient on the Waiting List Delete a Patient from the Waiting List

#### Request Operations

> Display Availability Make Operation Requests

> Delete or Update Operation Requests Make a Request from the Waiting List Make a Request for Concurrent Cases Review Request Information Operation Requests for a Day Requests by Ward

> List Op Requests by Surgeon or Attending

#### List Operation Requests Schedule Operations

> Display Availability

> Schedule Requested Operations Locked with SROSCH

> Schedule Unrequested Operations Locked with SROSCH

> Schedule Unrequested Concurrent Cases Locked with SROSCH

> Reschedule or Update a Scheduled Operation Locked with SROSCH

> Cancel Scheduled Operation Locked with SROSCH

> Update Cancellation Reason Locked with SROSCH

> Schedule Anesthesia Personnel

> Create Service Blockout Locked with SROSCH

> Delete Service Blockout Locked with SROSCH

> Schedule of Operations

#### List Scheduled Operations

> Operation Menu Locked with SROPER

> Operation Information Surgical Staff Operation Startup Operation

> Post Operation

> Enter PAC(U) Information Operation (Short Screen)

> Time Out Verified Utilizing Checklist

> Surgeon's Verification of Diagnosis & Procedures Locked with SROEDIT Anesthesia for an Operation Menu Locked with SROANES Anesthesia Information (Enter/Edit) Locked with SROANES

Anesthesia Technique (Enter/Edit) Locked with SROANES

> Medications (Enter/Edit)

Anesthesia Report Locked with SROANES

> Schedule Anesthesia Personnel Operation Report

Anesthesia Report Locked with SROANES

> Nurse Intraoperative Report Tissue Examination Report

> Enter Referring Physician Information Locked with SROEDIT

> Enter Irrigations and Restraints Locked with SROEDIT

> Medications (Enter/Edit) Abort/Cancel Operation Blood Product Verification

Anesthesia Menu Locked with SROANES

Anesthesia Data Entry Menu Locked with SROANES

Anesthesia Information (Enter/Edit) Locked with SROANES

Anesthesia Technique (Enter/Edit) Locked with SROANES

> Medications (Enter/Edit)

Anesthesia Report Locked with SROANES

> Schedule Anesthesia Personnel

Perioperative Occurrences Menu Locked with SROCOMP

> Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit)

> Non-Operative Occurrences (Enter/Edit) Locked with SROSURG

> Update Status of Returns Within 30 Days Morbidity & Mortality Reports

> Non-O.R. Procedures Locked with SROPER

> Non-O.R. Procedures Menu (Enter/Edit) Locked with SROPER

> Edit Non-O.R. Procedure Anesthesia Information (Enter/Edit) Medications (Enter/Edit) Anesthesia Technique (Enter/Edit) Procedure Report (Non-O.R.) Tissue Examination Report

> Non-OR Procedure Information

> Annual Report of Non-O.R. Procedures Locked with SROREP

> Report of Non-O.R. Procedures Locked with SROREP Comments Locked with SROPER

> Surgery Reports Locked with SROREP

> Management Reports

> Schedule of Operations (132 CRT) Annual Report of Surgical Procedures List of Operations

> List of Operations (by Postoperative Disposition) List of Operations (by Surgical Specialty)

> List of Operations (by Surgical Priority) Report of Surgical Priorities

> Report of Daily Operating Room Activity PCE Filing Status Report

> Outpatient Encounters Not Transmitted to NPCD Surgery Staffing Reports

> Attending Surgeon Reports Surgeon Staffing Report Surgical Nurse Staffing Report Scrub Nurse Staffing Report

> Circulating Nurse Staffing Report CPT Code Reports

> Cumulative Report of CPT Codes Report of CPT Coding Accuracy

> List Completed Cases Missing CPT Codes Missing Codes Report

#### Laboratory Interim Report

> Chief of Surgery Menu Locked with SROCHIEF

> View Patient Perioperative Occurrences Management Reports

> Morbidity & Mortality Reports M&M Verification Report

> Comparison of Preop and Postop Diagnosis Delay and Cancellation Reports

> Report of Delayed Operations Report of Delay Reasons Report of Delay Time

> Report of Cancellations Report of Cancellation Rates

> List of Unverified Surgery Cases Report of Returns to Surgery

> Report of Daily Operating Room Activity Report of Cases Without Specimens Report of Unscheduled Admissions to ICU Operating Room Utilization Report Wound Classification Report

> Print Blood Product Verification Audit Log Key Missing Surgical Package Data

> Admissions w/in 14 days of Out Surgery If Postop Occ Deaths Within 30 Days of Surgery

> Unlock a Case for Editing

> Update Status of Returns Within 30 Days

> Update Cancelled Case Locked with SROCHIEF

> Update Operations as Unrelated/Related to Death

> Surgery Package Management Menu Locked with SRCOORD

> Surgery Site Parameters (Enter/Edit) Operating Room Information (Enter/Edit)

> Surgery Utilization Menu Locked with SRCOORD

> Operating Room Utilization (Enter/Edit) Normal Daily Hours (Enter/Edit) Operating Room Utilization Report Report of Normal Operating Room Hours Purge Utilization Information

> Person Field Restrictions Menu

> Enter Restrictions for 'Person' Fields Remove Restrictions for 'Person' Fields

> Update O.R. Schedule Devices Update Staff Surgeon Information

> Flag Drugs for Use as Anesthesia Agents Update Site Configurable Files

> Backfill Order File with Surgical Cases Locked with SRCOORD

> Surgery Interface Management Menu Flag Interface Fields

> File Download Table Download

> Update Interface Parameter Field Make Reports Viewable in CPRS

> Surgery Risk Assessment Menu Locked with SR RISK ASSESSMENT

> Non-Cardiac Risk Assessment Information (Enter/Edit) Preoperative Information (Enter/Edit) Laboratory Test Results (Enter/Edit)

> Operation Information (Enter/Edit) Patient Demographics (Enter/Edit) Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit) Update Status of Returns Within 30 Days

> Update Assessment Status to ‘COMPLETE’ Alert Coder Regarding Coding Issues

> Cardiac Risk Assessment Information (Enter/Edit) Clinical Information (Enter/Edit) Laboratory Test Results (Enter/Edit)

> Enter Cardiac Catheterization & Angiographic Data Operative Risk Summary Data (Enter/Edit)

> Cardiac Procedures Operative Data (Enter/Edit) Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit) Outcome Information (Enter/Edit)

> Resource Data

> Update Assessment Status to ‘COMPLETE’ Alert Coder Regarding Coding Issues

> Print a Surgery Risk Assessment

> Update Assessment Completed/Transmitted in Error List of Surgery Risk Assessments

> Print 30 Day Follow-up Letters Exclusion Criteria (Enter/Edit)

> Monthly Surgical Case Workload Report

> Update Operations as Unrelated/Related to Death M&M Verification Report

> Update 1-Liner Case

> Queue Assessment Transmissions Risk Model Lab Test (Enter/Edit)

> CPT/ICD Coding Menu Locked with SR CODER

CPT/ICD Update/Verify Menu Locked with SR CODER

> Update/Verify Procedure/Diagnosis Codes Operation/Procedure Report

> Nurse Intraoperative Report Non-OR Procedure Information

> Cumulative Report of CPT Codes Report of CPT Coding Accuracy

> List Completed Cases Missing CPT Codes List of Operations

> List of Operations (by Surgical Specialty) List of Undictated Operations

> Report of Daily Operating Room Activity PCE Filing Status Report

> Report of Non-O.R. Procedures

Transplant Assessment Menu Locked with SR TRANSPLANT

> \*\*\*\*\*\*This option is no longer used after Patch SR\*3\*184\*\*

> Enter/Edit Transplant Assessments Print Transplant Assessment

> List of Transplant Assessments

> Transplant Assessment Parameters (Enter/Edit)

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 23 security keys in the Surgery package. Most are used to restrict access to certain options within the package. Other keys can be used to restrict which people can be entered in specific fields. This section of the manual describes each key. These descriptions can aid the package coordinator in assigning security levels to the user personnel. A list of users' names and security key levels must be supplied to the site manager.

> The following keys are used to determine whether a person can be entered in a specific field. Surgery V.

> 3.0 allows the user to restrict entries for any “person” type field based on keys. For example, the user could restrict entries into the PRIMARY SURGEON (.14) field in the SURGERY (#130) file to only those people who are holders of the SR SURGEON key. When entering data for a surgical case, only those people can be selected as a surgeon. Restriction of fields is not limited to the keys listed below. The user can use any existing key, or create keys of their own, to restrict access. The keys listed below are supplied for convenience. If the user does not choose to restrict "person" type fields, these keys will not be used elsewhere in the Surgery package.

| Security Key       | Description                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| SR ANESTHESIOLOGIST    | This key is used to restrict entry into selected fields in which an anesthesiologist can be entered. |
| SR MED STUDENT         | This key is used to restrict entry into selected fields in which a medical student can be entered.   |
| SR NURSE               | This key is used to restrict entry into selected fields in which a nurse can be entered.             |
| SR NURSE ANESTHETIST   | This key is used to restrict entry into fields in which a nurse anesthetist can be entered.          |
| SR PHYSICIAN ASSISTANT | This key is used to restrict entry into fields in which a physician assistant can be entered.        |
| SR SURGEON             | This key is used to restrict entry into fields in which a surgeon can be entered.                    |

> ![](sr-3-184-surgery-technical-manual-security-guide-change-pages/006.png)The following keys are used to restrict access to menus and options. Only holders of these keys will be permitted to access the locked options or functions.

| Security Key   | Description                                                                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SR CODER           | This key should be given to those responsible for entering CPT and ICD codes for operations and non-OR procedures. This key is used to lock the Surgery *CPT/ICD Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] option.                  |
| SR REQ OVERRIDE    | This key allows users to make operation requests beyond the site selected cutoff times. The SR REQ OVERRIDE key should only be given to those users that are permitted to make this type of last minute request.                              |
| SR RISK ASSESSMENT | This key is used to lock the *Surgery Risk Assessment Menu* \[SROA RISK ASSESSMENT\] option and all the options it contains. The SR RISK ASSESSMENT key should be given to the Surgery Risk Data Manager and Surgery Application Coordinator. |
| SR STAFF SURGEON   | This key is used to determine whether a person is a staff surgeon.                                                                                                                                                                            |
| SRCOORD            | This key is used to lock the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] *option* and the options it contains. The SRCOORD key should be given to the Surgery Application Coordinator.                                       |
| SROAAMIS           | This key is required when accessing the *Anesthesia AMIS* \[SROAMIS\] option and should be given to only those users that will need to print the Anesthesia AMIS Report.                                                                      |
| SROANES            | This key is required when accessing any anesthesia related option, with the exception of the *Anesthesia AMIS* \[SROAMIS\] option, which has its own unique key.                                                                              |
| SROCHIEF           | This key is required when accessing the *Chief of Surgery Menu* \[SROCHIEF\] option and the options it contains. The SROCHIEF key should be given to the Surgery Application Coordinator, Chief of Surgery, and his or her designee.          |
| SROCOMP            | This key is used to lock the *Perioperative Occurrences Menu* \[SRO COMPLICATIONS MENU\] option. It should be given to those users permitted to enter, edit, and delete surgical complications.                                               |
| SROEDIT            | This key is required when entering or editing Surgery related data. Users that do <u>not</u> have this key are limited to viewing access, rather than editing access, on all Surgery screens.                                                 |
| SROPER             | This key is required to access the *Operation Menu* \[SROPER\] option and all of the options it contains.                                                                                                                                     |
| SROREP             | This key is required when accessing the *Surgery Reports* \[SRORPTS\] option. Options in this menu cannot be accessed without this key.                                                                                                       |
| SROREQ             | This key is required when accessing the *Request Operations* \[SROREQ\] option, and is given only to those users responsible for making requests.                                                                                             |
| SROSCH             | This key is required when accessing the *Schedule Operations* \[SROSCHOP\] option and is given only to users responsible for scheduling operations.                                                                                           |

| Security Key | Description                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SROSURG          | This key is required when accessing the *Undictated Operations* \[SRODICT\] option and the *Enter/Edit Non-Operative Complications* \[SROCOMP\] option.                                                     |
| SROWAIT          | This key is required when accessing the *Maintain Surgery Waiting List* \[SROWAIT\] option. Only users responsible for adding, changing, deleting, or printing data on the waiting list are given this key. |
| SR TRANSPLANT    | This key is used to restrict entry into the Transplant Assessment module.                                                                                                                                   |

> *(This page included for two-sided copying.)*

# File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following files were distributed with limited access for first time installations of the VistA Surgery software. Files not listed below were sent without restrictions on VA FileMan access. Sites can add their own file access codes as needed, but it is highly recommended that they do not change the codes that are sent with this software package.

| File Number | File Name               | Read | Write | Delete | LAYGO |
|-----------------|-----------------------------|----------|-----------|------------|-----------|
| 131             | PERSON FIELD RESTRICTION    | @        | ^         | ^          | @         |
| 132.9           | ATTENDING CODES\*           | @        | @         | @          | @         |
| 132.95          | ANESTHESIA SUPERVISOR CODES |          | ^         | ^          | ^         |
| 134             | OPERATING ROOM TYPE         |          | ^         | ^          | ^         |
| 136.5           | OCCURRENCE CATEGORY         | ^        | ^         | ^          | ^         |

> \* This file was not included in the original release of Surgery V. 3.0, but was added by patch SR\*3\*129.

> *(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table provides definitions for common terms used in this manual.
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term/Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Aborted</td>
<td><p>Case status indicating the case was cancelled after the patient entered the operating room. Cases with ABORTED status must contain entries in the TIME PAT OUT OR field (#.232) and/or the TIME PAT IN OR field (#.205), plus the CANCEL DATE field (#17) and/or the CANCELLATION TIMEFRAME field (#17.5) and the CANCEL REASON field (#18) and the CASE ABORTED field</p>
<p>entered with “YES”.</p></td>
</tr>
<tr class="even">
<td>ASA Class</td>
<td><p>This is the American Society of Anesthesiologists’ classification</p>
<p>relating to the patient’s physiologic status. Numbers followed by an “E” indicate an emergency.</p></td>
</tr>
<tr class="odd">
<td>Attending Code</td>
<td>Code that corresponds to the highest level of supervision provided by the attending staff surgeon during the procedure.</td>
</tr>
<tr class="even">
<td>Blockout Graph</td>
<td>Graph showing the availability of operating rooms.</td>
</tr>
<tr class="odd">
<td>Cancelled Case</td>
<td>Case status indicating that an entry has been made in the CANCEL DATE field (#17) and/or the CANCELLATION TIMEFRAME field (#17.5) and the CANCEL REASON field (#18) without the patient entering the operating room.</td>
</tr>
<tr class="even">
<td>CCSHS</td>
<td>VA Center for Cooperative Studies in Health Services located at Hines, Illinois.</td>
</tr>
<tr class="odd">
<td>Completed Case</td>
<td>Case status indicating that an entry has been made in the TIME PAT OUT OR (#.232) field.</td>
</tr>
<tr class="even">
<td>Concurrent Case</td>
<td>A patient undergoing two operations by different surgical specialties at the same time, or back-to-back, in the same operating room.</td>
</tr>
<tr class="odd">
<td>CPT Code</td>
<td>Current Procedural Terminology; also known as Operation Code.</td>
</tr>
<tr class="even">
<td>CRT</td>
<td>Cathode ray tube display. A display device that uses a cathode ray tube.</td>
</tr>
<tr class="odd">
<td>Enter</td>
<td>To type in information on a keyboard and press the Enter key (or the Return key for some keyboards) to send the information to the computer.</td>
</tr>
<tr class="even">
<td>Intraoperative Occurrence</td>
<td>Perioperative occurrence during the procedure.</td>
</tr>
<tr class="odd">
<td>Major</td>
<td>Any operation performed under general, spinal, or epidural anesthesia plus all inguinal herniorrhaphies and carotid endarterectomies, regardless of anesthesia administered.</td>
</tr>
<tr class="even">
<td>Minor</td>
<td>All operations not designated as Major.</td>
</tr>
<tr class="odd">
<td>New Surgical Case</td>
<td>A surgical case that has not been previously requested or scheduled such as an emergency case. A surgical case entered in the records without being booked through scheduling will not appear on the Schedule of Operations or as an operative request.</td>
</tr>
<tr class="even">
<td>Non-Operative Occurrence</td>
<td>Occurrence that develops before a surgical procedure is performed.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term/Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Not Complete</td>
<td><p>Case status indicating one of the following two situations with no entry in the TIME PAT OUT OR field (#.232):</p>
<ol type="1">
<li><p>Case has entry in TIME PAT IN OR field (#.205).</p></li>
<li><p>Case has not been requested or scheduled.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Operation Code</td>
<td>Identifying code for reporting medical services and procedures performed by physicians. See CPT Code.</td>
</tr>
<tr class="odd">
<td>PACU</td>
<td>Post Anesthesia Care Unit.</td>
</tr>
<tr class="even">
<td>Postoperative Occurrence</td>
<td>Perioperative occurrence following the procedure.</td>
</tr>
<tr class="odd">
<td>Procedure Occurrence</td>
<td>Occurrence related to a non-OR procedure.</td>
</tr>
<tr class="even">
<td>Requested</td>
<td>Operation has been slotted for a particular day but the time and operating room are not yet firm.</td>
</tr>
<tr class="odd">
<td>Risk Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>Scheduled</td>
<td>Operation has both an operating room and a scheduled starting time, but the operation has not yet begun.</td>
</tr>
<tr class="odd">
<td>Screen</td>
<td>An illuminated display surface on which display images are presented.</td>
</tr>
<tr class="even">
<td>Screen Server</td>
<td>A format for displaying data on a cathode ray tube display. Screen Server is designed specifically for the Surgery Package.</td>
</tr>
<tr class="odd">
<td>Screen Server Function</td>
<td>The Screen Server prompt for data entry.</td>
</tr>
<tr class="even">
<td>Service Blockouts</td>
<td>The reservation of an operating room for a particular service on a recurring basis. The reservation is charted on a blockout graph.</td>
</tr>
<tr class="odd">
<td>Transplant Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical transplant risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>VASQIP</td>
<td>VA Surgical Quality Improvement Program.</td>
</tr>
</tbody>
</table>
> *(This page included for two-sided copying.)*

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### A

> anesthesia agents, 13, 28
> Anesthesia Menu, 23, 72
> Anesthesia Report, 9, 14, 16, 23, 69, 72
> Archiving, 49

#### B

> background tasks, 10, 40

#### C

> callable entry points, 51 Calls, 53
> Change Site Parameters, 75 configurable files, 13, 43
> contingency plan, 65
> CPT/ICD Coding Menu, 25, 76

#### D

> Data Base Integration Agreements, 51, 57

#### E

> exported files, 14, 15, 18
> external packages, 53

#### F

> Field Station Information Security Officers, 65 File descriptions, 16
> Files, 13, 14,28,43,75, 81
> FORUM, 57

#### G

> generic interface, 62
> globals, 47

#### H

> HL7, 28,39, 41, 43
> holidays, 9
> HOSPITAL LOCATION file, 10
> I
> IAs, 51, 57
> initialization routines, 18
> Input Templates, 44, 46
> installation, 7, 18
> interface, 8, 28, 39, 43, 67
> ISOs, 65

#### J

> journaling, 47

#### K

> key, 3
> keys, 7, 27, 36, 37, 76, 77, 78

#### L

> List Operation Requests, 29, 71
> List Scheduled Operations, 29, 72

#### M

> mail groups, 13
> Maintain Surgery Waiting List, 30, 71, 79

#### N

> namespaced, 61
> NEW PERSON file, 7
> Non-O.R. Procedures, 25, 31, 33, 36, 38, 73, 76
> Nurse Intraoperative Report, 8, 14, 31, 69, 72

#### O

> Operation Menu, 25, 34, 72
> Operation Report, 14, 16, 34, 72
> operative procedure, 1, 14, 16, 29, 31, 33
> Option Descriptions, 23
> OPTION file, 59

#### P

> package-wide variables, 61
> Perioperative Occurrences Menu, 36, 72
> protocol, 18, 39, 40, 67
> Purging, 49

#### R

> REQUEST CUTOFF FOR SUNDAY field, 9
> Request Operations, 38, 71, 78
> routines, 18, 51, 53

#### S

> Schedule Operations, 39, 71, 83
> Security Keys, 7, 77
> Site Specific Parameters, 7 Sort Template, 45
> SR REQ OVERRIDE key, 78
> SURGERY file, 14, 16, 23, 28, 33, 41, 51,52, 61
> Surgery Nightly Cleanup and Updates, 40, 49 Surgery Package Management Menu option, 7,
> 11, 13, 75, 78
> Surgery Site Parameters, 40, 43, 75
> SURGERY UTILIZATION file, 33, 49

#### T

> templates, 44
> Transplant Assessment Menu, 76

#### X

> XU FIRST LINE PRINT, 18


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: SR*3*177 Surgery Technical Manual/Security Guide Change Pages

## Adding Entries to Surgery-Related Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are several site-configurable Surgery files that may need updating to add new entries or to inactivate or change existing entries. These configurable files are listed below. Use the *Update Site Configurable Files* \[SR UPDATE FILES\] option on the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] option to update these files.

- SURGERY TRANSPORTATION DEVICES file (#131.01)
- SURGERY POSITION file (#132)
- SURGICAL DELAY file (#132.4)
- IRRIGATION file (#133.6)
- SKIN INTEGRITY file (#135.2)
- PATIENT CONSCIOUSNESS file (#135.4)
- ELECTROGROUND POSITIONS file (#138)
- PROSTHESIS file (#131.9)
- RESTRAINTS AND POSITIONAL AIDS file (#132.05)
- MONITORS file (#133.4)
- SURGERY REPLACEMENT FLUIDS file (#133.7)
- SKIN PREP AGENTS file (#135.1)
- PATIENT MOOD file (#135.3)
- LOCAL SURGICAL SPECIALTY file (#137.45)
- SURGERY DISPOSITION file (#131.6)

## Flag Drugs for Anesthesia Agents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Drugs to be used as anesthesia agents must be flagged or they cannot be selected as entries in the ANESTHESIA AGENT data fields.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following mail groups should be created with the appropriate persons added as members.

> RISK ASSESSMENT SRHL DISCREPANCY SR TRANSPLANT
