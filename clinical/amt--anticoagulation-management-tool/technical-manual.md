---
title: Anticoagulation Management Tool Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: Anticoagulation Management Tool
app_code: AMT
app_name: Anticoagulation Management Tool
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - oram
  - anticoagulation
  - class
  - patient
  - routine
  - routines
  - management
  - indication
page_count: 0
word_count: 3002
section_count: 6
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/am_oramtm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/am_oramtm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=188"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Anticoagulation Management Tool

  Technical Manual

  (Patch OR\*3.0\*447)
---

![](anticoagulation-management-tool-technical-manual/001.png)

Initial Release: March 2010

Revised: February 2018

Office of Enterprise Development

Product Development

Revision History

| Date       | Description of Change                       | Authors                            |
|------------|---------------------------------------------|------------------------------------|
| Feb 2018   | Patch OR\*3.0\*447 – 2FA implementation     | <span class="mark">redacted</span> |
| April 2015 | Patch OR\*3.0\*391 – Updated new parameters | <span class="mark">redacted</span> |
| Mar 2010   | Initial Release                             | <span class="mark">redacted</span> |

Table of Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Screen Capture Conventions](#screen-capture-conventions)
- [Online Help](#online-help)
- [Related Manuals](#related-manuals)
- [Implementation](#implementation)
- [Files](#files)
- [Routines](#routines)
- [Parameters](#parameters)
- [Exported Options](#exported-options)
- [Archiving](#archiving)
- [# Application Programmer Interfaces](#application-programmer-interfaces)
- [External Relationships](#external-relationships)
- [Database Integration Agreements](#database-integration-agreements)
- [Internal Relationships](#internal-relationships)
- [Global Variables](#global-variables)
- [Additional Useful Information](#additional-useful-information)
- [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
  - [Routines](#routines-1)
  - [Globals](#globals)
  - [XINDEX](#xindex)
  - [Data Dictionaries](#data-dictionaries)
- [External Interfaces \](#external-interfaces)
  - [Remote Procedures:](#remote-procedures)
- [Cross-References](#cross-references)
- [Software Security](#software-security)
- [Glossary](#glossary)
This tool was developed at the Portland VA Medical Center to help simplify the complex, time consuming processes required to manage patients on anticoagulation medication.
The tool enables the user to enter, review, and continuously update all information connected with patient anticoagulation management. With the Anticoagulation Tracking, one can order lab tests, enter outside lab results and graphically review lab data, enter notes, complete encounter data, complete the consults if consults are used to initiate entry into the Anticoagulation clinic, and print a variety of patient letters. Upon exiting the program all activities within the program are recorded on an Anticoagulation flow sheet maintained on the Computerized Patient Record System (CPRS) Reports tab. The Anticoagulation Tracking provides clinic staff a mechanism of ensuring continuous patient monitoring *with a built-in mechanism that alerts staff when patients haven’t been monitored in a timely period.* A Lost to Follow-up list is maintained to ensure that staff knows of patients who need attention.

# Screen Capture Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this manual, user responses are shown in bold type. In most cases, you need only enter the first few letters to increase speed and accuracy. Pressing the Return or Enter key, which is indicated by the symbol \<RET\>, must follow every response you enter. This symbol is not shown, but is implied, following bold type entries.

Enter a caret, indicated by the symbol (^), at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to exit the system.

# Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online help is available at almost any prompt in the software by entering a single question mark (?). This will provide information to help you answer the prompt. In some instances, entering double (??) or triple (???) question marks will provide more detailed information.

# Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two other manuals that give information on the Anticoagulation Management Tool (AMT). They are both much more technical than this manual and intended for use to set up and modify the tool. These are:

> *Anticoagulation Management Tool Installation/Implementation Guide*

> *Anticoagulation Management Tool User Manual*

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All implementation issues are addressed in the *Anticoagulation Management Tool Installation/Implementation Guide.*

.

# Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is only one VistA file installed with the Anticoagulation Management Tool (AMT). It is:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 28%" />
<col style="width: 53%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File #</td>
<td>File Name</td>
<td>Description</td>
</tr>
<tr class="even">
<td>103</td>
<td>ORAM FLOWSHEET</td>
<td><p>This file captures flowsheet data in support of AMT, which is a Joint Commission National Patient Safety Goal initiative to use a standardized process for the management of their patients on extended anticoagulation therapy.</p>
<p>AMT runs as a Windows Application from the CPRS Tools menu, and assists Clinicians with the expeditious documentation of visits to Anticoagulation Clinics.</p></td>
</tr>
</tbody>
</table>

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are exported with (AMT version 1):

| Name    | Description                              |
|---------|------------------------------------------|
| ORAM    | ANTICOAGULATION MANAGEMENT RPCS (1 of 4) |
| ORAM1   | ANTICOAGULATION MANAGEMENT RPCS (2 of 4) |
| ORAM2   | ANTICOAGULATION MANAGEMENT RPCS (3 of 4) |
| ORAM3   | ANTICOAGULATION MANAGEMENT RPCS (4 of 4) |
| ORAMSET | Anticoagulation Setup                    |
| ORAMX   | ADDITIONAL ANTICOAGULATION CALLS         |
| ORAMY   | Anticoagulation Management Installation  |

The following routines are modified or new with (AMT version 2 or patch OR\*3.0\*391):

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORAM</td>
<td>Modified the PATIENT subroutine to correct a problem where if a new patient was not yet enrolled in the Anticoagulation flowsheet database but had a visit scheduled in the look-up interval, the visit was not being identified.</td>
</tr>
<tr class="even">
<td>ORAM1</td>
<td>Modified the ACDATA subroutine to handle selection of SNOMED CT concepts with multiple mapped ICD-9-CM diagnoses (e.g., Transient cerebral ischemia due to atrial fibrillation (SNOMED CT 426814001) = 427.31/435.9).</td>
</tr>
<tr class="odd">
<td>ORAM2</td>
<td>Modified the RPT subroutine to assure that the Anticoagulation Report on the CPRS Reports tab displays indications in a manner consistent with the rest of AMT.</td>
</tr>
<tr class="even">
<td>ORAMSET</td>
<td><p>Modified the GET &amp; INDICS subroutines to accept Visit Date as an argument, and return the appropriate Parameter values, given the ICD-10-CM Implementation date.</p>
<p>Introduced a new function $$GETCMPDT(CODESYS) that returns a compare date for the Coding System of interest, to be used in screening active codes during parameter set-up.</p></td>
</tr>
<tr class="odd">
<td>ORAMX</td>
<td><p>Modified the PCESET subroutine to handle the case where a SNOMED CT concept is selected for the indication which has multiple mapped ICD-9-CM targets.</p>
<p>Split routine, moving the WRAP function to ORAMX1, to comply with the SACC routine size limit.</p></td>
</tr>
<tr class="even">
<td>ORAMX1</td>
<td><p>Moved the WRAP function from ORAMX, and the RPT subroutine from ORAM2 in order to keep those routines within the SACC size limit.</p>
<p>Introduced a new function GETVSIT, which will assure that the CPRS Report for AMT uses includes all information stored in PCE for the Encounter generated for most recent flowsheet entry, including any diagnoses that were added via the CPRS Encounter form or any other data source.</p></td>
</tr>
<tr class="odd">
<td>ORY391</td>
<td>Post-install routine, which creates the package-level default values for the ORAM I10 INDICATIONS FOR CARE parameter.</td>
</tr>
</tbody>
</table>

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Anti-Coagulation Management Tool (AMT) v.2 includes the following parameters:

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORAM AUTO PRIMARY INDICATION</td>
<td><p>Using this parameter, the facility can specify an Automatic Primary Indication for Care (ICD-9- CM code) for each clinic using the Anticoagulation Management Tool (AMT).</p>
<p>The OR*3.0*391 patch modifies the VALUE SCREEN CODE to assure the selection of an active ICD-9-CM code prior to ICD-10-CM implementation.</p></td>
</tr>
<tr class="even">
<td>ORAM AUTO SECONDARY INDICATION</td>
<td><p>This is an Indication for care which will automatically be filed as the first Secondary Indication for each visit to the applicable Clinic.</p>
<p>For example, if all visits to a non-licensed provider should be filed with the ICD-9-CM code V58.83 ENCTR THERAP DRUG MONITOR as the first secondary indication, you can specify that with this parameter, and the user will still be able to select additional secondary indication(s) from the list.</p></td>
</tr>
<tr class="odd">
<td>ORAM I10 AUTO PRIM INDICATION</td>
<td><p>In anticipation of the ICD-10 implementation, the facility will use this parameter to specify an Automatic Primary Indication for Care (an ICD-10-CM code) for each clinic using the AMT software.</p>
<p>The OR*3.0*391 patch includes VALUE SCREEN CODE to assure the selection of an active ICD-10-CM code following ICD-10-CM implementation.</p></td>
</tr>
<tr class="even">
<td>ORAM I10 AUTO SEC INDICATION</td>
<td><p>This is an Indication for care which will automatically be filed as the first Secondary Indication for each visit to the applicable Clinic after ICD-10-CM implementation.</p>
<p>For example, if all visits to a non-licensed provider should be filed with the ICD-10-CM code Z51.81 Encounter for therapeutic drug level monitoring as the first secondary indication, you can specify that with this parameter, and the user will still be able to select additional secondary indication(s) from the list).</p></td>
</tr>
<tr class="odd">
<td>ORAM I10 INDICATIONS FOR CARE</td>
<td><p>In anticipation of the ICD-10-CM implementation, this parameter provides a server-side mechanism to specify a list of Additional Indications for Care (ICD-10-CM codes).</p>
<p>The current patch includes VALUE SCREEN CODE to assure the selection of active ICD-10-CM codes following ICD-10-CM implementation.</p></td>
</tr>
<tr class="even">
<td>ORAM INDICATIONS FOR CARE</td>
<td><p>Prior to ICD-10-CM implementation, this parameter provides a server-side mechanism to specify a list of Additional Indications for Care (as ICD-9-CM codes).</p>
<p>The current patch modifies the VALUE SCREEN CODE to assure the selection of active ICD-9-CM codes prior to ICD-10-CM implementation.</p></td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS install places menu options for reports on the server but does not place them into your menu structure. These are:

- Anticoagulation Complication Report \[ORAM COMPLICATIONS REPORT\]
- All Anticoagulation Patients \[ORAM PATIENT LIST ALL\]
- Complex Anticoagulation Patients \[ORAM PATIENT LIST COMPLEX\]
- Next Lab Patient List \[ORAM PATIENT LIST NEXT LAB\]
- Single Patient TTR \[ORAM ROSENDAAL SINGLE PT TTR\]
- Calculate TTR (Rosendaal Method) \[ORAM ROSENDAAL TTR REPORT\]

TTR stands for Time in Therapeutic Range.

It also provides two umbrella menu actions that give access to the Anticoagulation Complication Report, Calculate TTR (Rosendaal Method), and Single Patient TTR. It is:

- Anticoagulation Management Reports \[ORAM REPORTS MENU\]
- Anticoagulation Patient Lists \[ORAM PATIENT LIST MENU\]

These reports must be assigned to the clinic personnel who need them in the performance of their duties.

To have access to the reports on the menu, users must have them assigned to their menu tree.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving for any VistA program including the Anticoagulation Management Tool (AMT).

# # Application Programmer Interfaces 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no routines in ORAM that are intended for access from another application.

# External Relationships 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the Anticoagulation Management Tool (AMT) can be installed, the following packages and patches must be installed and *fully* patched in your accounts.

|                                          |         |
|------------------------------------------|---------|
| Application Name                         | Version |
| Authorization/Subscription Utility (ASU) | V 1.0   |
| \*Consult/Request Tracking               | V 2.5   |
| Kernel                                   | V. 8.0  |
| Laboratory                               | V. 5.2  |
| \*Order Entry/Results Reporting (OE/RR)  | V. 3.0  |
| Patient Care Encounter (PCE)             | V. 1.0  |
| RPC Broker                               | V 1.1   |
| Text Integration Utilities (TIU)         | V 1.0   |
| ToolKit                                  | V. 7.3  |
| VA FileMan                               | V. 21.0 |
| Visit Tracking                           | V 2.0   |

# Database Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database Integration Agreements (DBIA) are available on the DBA menu on MailMan.

Callable routines, entry points, Application Program Interfaces (APIs), and Remote Procedure Calls (RPCs) can be subscribed to. Lists of these will be available on the DBA menu on the Forum.

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMT is a GUI Delphi application, designed to be invoked from the Tools Menu in CPRS. Having no patient look-up of its own, it receives Server, Port, Patient, and User context from CPRS. A future version is expected to use CCOW to mediate this sharing of User and Patient context.

> **NOTE:** | ![](anticoagulation-management-tool-technical-manual/002.png) | *The Anticoagulation Management Tool (AMT) may not work properly if executed from a shortcut or the Windows Start Menu.* |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|

# Global Variables 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Anticoagulation Management Tool (AMT) is exported with one global variable:

- The Anticoagulation Flowsheet File (#103)

# Additional Useful Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following elements may be helpful for users where applicable; however, they are not required in all VistA Technical Manuals:

# How to Obtain Technical Information Online 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace for AMT is ORAM.

## Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XUPRROU (List Routines) prints a list of any or all of the ORAM routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: list Routines

Routine Print

Want to start each routine on a new page: No// \[ENTER\]

routine(s) ? \> ORAM\*

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each ORAM subset routine.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: First Line Routine Print

PRINTS FIRST LINES

routine(s) ? \>ORAM\*

## Globals 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The global unique to VA in the TIU package is ^ORAM(. Use the Kernel option XUPRGL (List Global) to print a list of any of these globals. This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: LIST Global

Global ^^PX\*

## XINDEX 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls.

XINDEX is invoked from programmer mode: D ^XINDEX.

When selecting routines, select ORAM\*.

## Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number-spaces for ORAM files unique to VA are 103. Use the VA FileMan DATA DICTIONARY UTILITIES, option \#8 ( DILIST, List File Attributes), to print a list of these files. Depending on the FileMan template used to print the list, this option will print out all or part of the data dictionary for the ORAM files.

> Example:

> \>D P^DI

> VA FileMan 21.0

> Select OPTION: DATA DICTIONARY UTILITIES

> Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

> START WITH WHAT FILE: 103

> (1 entry)

> GO TO WHAT FILE: 8925// 103\*

> Select LISTING FORMAT: STANDARD// \[Enter\]

> DEVICE: PRINTER

# External Interfaces \*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Remote Procedures:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ORAM APPTMTCH    | This RPC supports revision of the appointment match when the user selects a new Clinic in AMT.                                                                                                                                                                                                                                                                                                             |
| ORAM CONCOMP     | Receives the Consult Number, the note number and the DUZ; completes the consult with the note.                                                                                                                                                                                                                                                                                                             |
| ORAM HCT         | Returns the patient's most recent Hematocrit (HCT).                                                                                                                                                                                                                                                                                                                                                        |
| ORAM INR         | Returns last 6 months of INR values and dates.                                                                                                                                                                                                                                                                                                                                                             |
| ORAM ORDER       | This RPC supports placing INR and CBC orders from the AMT.                                                                                                                                                                                                                                                                                                                                                 |
| ORAM PROVIDER    | Returns provider DUZ and name.                                                                                                                                                                                                                                                                                                                                                                             |
| ORAM SIGCHECK    | Validates the Electronic Signature Code entered by the user.                                                                                                                                                                                                                                                                                                                                               |
| ORAM1 ACDATA     | Retrieves record header information (e.g., indication for treatment, permissions, risks, goals, etc.) for the current patient. In patch OR\*3.0\*391, it is modified to accept Date of Service as a parameter.                                                                                                                                                                                             |
| ORAM1 ADDTOP     | Files record header information for the current patient and care episode.                                                                                                                                                                                                                                                                                                                                  |
| ORAM1 COMPTEST   | Files complications for the current flowsheet entry.                                                                                                                                                                                                                                                                                                                                                       |
| ORAM1 FLOWTT     | Retrieves flowsheet data for the current patient.                                                                                                                                                                                                                                                                                                                                                          |
| ORAM1 GETPT      | Returns list of patients from Anticoagulation Flowsheet file (#103).                                                                                                                                                                                                                                                                                                                                       |
| ORAM1 LOCK       | Sets lock in Anticoagulation Flowsheet file (#103) so that only one person can edit a given patient's record at a time.                                                                                                                                                                                                                                                                                    |
| ORAM1 LOG        | Updates Anticoagulation Flowsheet file (#103) and adds log entry.                                                                                                                                                                                                                                                                                                                                          |
| ORAM1 OUTINR     | Receives outside INR values and returns value^date (in \$H format) for graphing.                                                                                                                                                                                                                                                                                                                           |
| ORAM1 PCGOAL     | Calculates percent in goal from filed INR entries for Anticoagulation Management patients can do either Stable or all patients (pass 1 as second parameter for stable).                                                                                                                                                                                                                                    |
| ORAM1 PTCHECK    | Boolean RPC. Checks to see if patient is in Anticoagulation Flowsheet file (#103).                                                                                                                                                                                                                                                                                                                         |
| ORAM1 PTENTER    | Adds a new patient to the Anticoagulation Flowsheet file (#103).                                                                                                                                                                                                                                                                                                                                           |
| ORAM1 TERASE     | Removes a patient from the Anticoagulation Team List.                                                                                                                                                                                                                                                                                                                                                      |
| ORAM1 UNLOCK     | Unlocks a patient's record in the Anticoagulation Flowsheet file (#103).                                                                                                                                                                                                                                                                                                                                   |
| ORAM2 ALLGOAL    | Returns the percentage of patients in the Anticoagulation Flowsheet file (#103) whose last INRs (within the specified number of days) were in.                                                                                                                                                                                                                                                             |
| ORAM2 NOACT      | Checks Anticoagulation Flowsheet file (#103) for patients not seen within the user-specified number of days                                                                                                                                                                                                                                                                                                |
| ORAM2 PTAPPT     | Returns the number of patients scheduled in the Anticoagulation clinic per day for the next 30 days. Only days with appointments are displayed.                                                                                                                                                                                                                                                            |
| ORAM2 REMIND     | Sets date and text for ACM Reminder (can also be set as part of a complete visit entry).                                                                                                                                                                                                                                                                                                                   |
| ORAM2 SHOWRATE   | Returns percentage of visits in which the patient was on time or within one day (before or after) scheduled draw date.                                                                                                                                                                                                                                                                                     |
| ORAM2 TEAMCHK    | Checks list of teams to be sure they are in the OE/RR LIST file (#100.21), and returns the IEN and Clinic Name.                                                                                                                                                                                                                                                                                            |
| ORAM3 COMPENT    | Enters complication note into the Anticoagulation Flowsheet file (#103). Can also be entered as part of a complete visit entry.                                                                                                                                                                                                                                                                            |
| ORAM3 PTADR      | Retrieves contact information. Will also check for active temporary information.                                                                                                                                                                                                                                                                                                                           |
| ORAM3 PTFONE     | Gets home phone^work phone for the patient in question.                                                                                                                                                                                                                                                                                                                                                    |
| ORAMSET GET      | Returns the Anticoagulation Manager parameters for the division which the user is logged into, and the clinic which is responsible for the patient. In patch OR\*3.0\*391, this introduced a new parameter to allow the client to pass Visit Date/time in internal VA FileMan format and return a boolean flag indicating whether ICD-10-CM is active as the 11th piece of the 2-node of the result array. |
| ORAMSET GETCLINS | This RPC fetches the list of Clinic Names from the configuration of the Anticoagulation Management Tool (AMT).                                                                                                                                                                                                                                                                                             |
| ORAMX CONSULT    | Send DFN and the name of the Consult Service (from the ORAM CONSULT REQUEST SERVICE parameter). Returns pending and active consults which meet those criteria.                                                                                                                                                                                                                                             |
| ORAMX PCESET     | Checks for service connection, etc, for PCE data call or files PCE data.                                                                                                                                                                                                                                                                                                                                   |

# Cross-References 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All cross-references on the ORAM FLOWSHEET file (#103) are Regular, FileMan cross-references available for either sorting or searching (see Data Dictionary Listing for details).

# Software Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Permission to use the Anticoagulation Management Tool (AMT) is controlled by menu assignment and deployment of the MS Windows executable file (AntiCoagulate.exe).

To grant a user access to ACM, simply assure that the ORAM ANTICOAGULATION CONTEXT option is in their menu tree (usually by adding it to their Secondary Menus), and add Anticoagulation Management to their CPRS Tools menu. Finally, be sure that the Windows executable file (AntiCoagulate.exe) is either placed on a workstation to which the user has access, or in a network share directory to which the user has read permission. Details of this process are described in the Installation/Implementation Guide.

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CPRS</strong></th>
<th>Computerized Patient Record System. A user interface for the popular Windows operating system to the Department of Veterans Affairs hospital software system (VistA). The original design criterion was to allow most hospital employees to access patient medical data without the use of command line processing. Eventually CPRS will allow medical record access from any Graphical User Interface (GUI) such as used on Unix, Linux, and OS X.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ICD-9</strong></td>
<td>International Statistical Classification of Diseases and Related Health Problems Ninth Revision. This coding system has become a standard used by insurance companies for claims and billing purposes. Thus the VA uses it to retrieve to help produce revenue by sending insurance claims for non-service connected work done at its medical centers. This numbering classification is updated often and care must be taken to use currently valid codes.</td>
</tr>
<tr class="even">
<td><strong>ICD-10</strong></td>
<td>International Statistical Classification of Diseases and Related Health Problems Tenth Revision. This coding system has been selected as the new standard to be used by insurance companies for claims and billing purposes. Thus the VA uses it to retrieve to help produce revenue by sending insurance claims for non-service connected work done at its medical centers. The VA is planning on moving from ICD-9 to ICD-10. The move is currently scheduled for October 1, 2015.</td>
</tr>
<tr class="odd">
<td><strong>INR</strong></td>
<td><p>International Normalized Ratio: The INR is used to the exclusion of other measurements because the result (in seconds) for a prothrombin time performed on a normal individual varies depending on what type of analytical system is used. This is due to the differences between batches of the manufacturer's tissue factor used in the reagent to perform the test. The INR standardizes the results.</p>
<p>INR is the ratio of a patient's prothrombin time to a normal (control) sample, raised to the power of the International Sensitivity Index (ISI) value for the analytical system used. Each manufacturer assigns an ISI value for any tissue factor they manufacture. (This value indicates how a particular batch of tissue factor compares to an internationally standardized sample. The ISI is usually between 1.0 and 2.0.) ![](anticoagulation-management-tool-technical-manual/003.png)</p></td>
</tr>
<tr class="even">
<td><strong>ISI</strong></td>
<td>International Sensitivity Index. This value indicates how a particular batch of tissue factor compares to an internationally standardized sample. The ISI is usually between 1.0 and 2.0.</td>
</tr>
</tbody>
</table>
| Prothrombin Time | A measurement of the time it takes, in seconds, for blood to coagulate. Because of the wide variability of laboratory tests to determine prothrombin time it has become standard practice to use a derived measurement, the INR, for clinical data. |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VistA | Veterans Health Information Systems and Technology Architecture. This is a replacement nomenclature the Decentralized Hospital Computer Program originally developed starting in 1977 for VA hospitals. The adoption of the new name in 1996 acknowledges the maturity of the system to a point where it is moving toward a more centralized architecture with communication of patient data between medical centers and the Department of Defense. |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
