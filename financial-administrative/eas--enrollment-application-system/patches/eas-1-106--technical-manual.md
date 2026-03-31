---
title: EAS*1*106 LOCAL Signed Means Test Application (ROSSIO 22) Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: LOCAL Signed Means Test Application (ROSSIO 22)
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1*106
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: This project was initially undertaken in response to Item \#22 in the "Report of Task Force to Review Enrollment, Means Testing and Income Verification" (a.k.a. Rossio Report) dated December 15, 2000. In the area of Means Test (MT) Deficiencies, Item \#22 required that the Veterans Health Administra
audience: 
keywords: 
  - table
  - contents
  - letters
  - print
  - background
  - software
  - test
  - letter
  - means
  - patch
page_count: 0
word_count: 3922
section_count: 20
table_count: 10
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p106_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p106_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-1-106-local-signed-means-test-application-rossio-22-technical-manual/001.png)

local signed mEANS TEST application (Rossio 22)

Enrollment application systems (EAS)

TECHNICAL Manual

Patch EAS\*1\*106

March 2014

V*IST*A System Design & Development

### # Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# | Revision Date | Brief Description                                                                                                       | Author   |

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [# Revision History](#revision-history)
- [| Revision Date | Brief Description                                                                                                       | Author   |](#revision-date-brief-description-author)
- [# Introduction](#introduction)
  - [Overview](#overview)
  - [Related Manuals](#related-manuals)
- [Implementation](#implementation)
  - [Pre-Installation](#pre-installation)
  - [Installation](#installation)
  - [Post-Installation](#post-installation)
- [Files](#files)
  - [File List](#file-list)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
    - [List Templates](#list-templates)
- [# Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Routine List](#routine-list)
- [Exported Options](#exported-options)
  - [Tasked Background Jobs](#tasked-background-jobs)
  - [Interactive Menu Diagram](#interactive-menu-diagram)
- [# Archiving & Purging](#archiving-purging)
- [Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)](#callable-routines-entry-points-and-application-programmer-interfaces-apis)
- [External Interfaces](#external-interfaces)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
  - [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [# Software Product Security](#software-product-security)
  - [Security Features](#security-features)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
    - [Remote Systems](#remote-systems)
    - [Archiving/Purging](#archivingpurging)
    - [Interfaces](#interfaces)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [Official Policy](#official-policy)
- [Glossary](#glossary)
- [Appendix A - Background Job Setup](#appendix-a-background-job-setup)
  - [Background Letter Search](#background-letter-search)
  - [Background Letter Print](#background-letter-print)
- [Index](#index)
|---------------|-------------------------------------------------------------------------------------------------------------------------|----------|
| 01/28/14      | Added note :Deployment of the VFA software (DG_53_P858.KID) deactivated the Means Test Letters and associated software. | REDACTED |
| 7/29/02       | Revisions due to release of Patch EAS\*1\*15                                                                            | REDACTED |
| 4/17/02       | Initial version based on release of Patch EAS\*1\*3                                                                     | REDACTED |
Table of Contents

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Veterans Financial Assessment project removed the requirement for Veterans to renew their means test each year. EAS\*1\*106 deployed with DG_53_P858.KID disabled the means test letter options. Sites were requested to remove the associated scheduled jobs.

The MTCHK^EASMTCHK API shall return a MT Not Required result if a current

Means Test is less than 1 year old as of the Veterans Financial

Assessment (VFA), January 1, 2013.

The following menu options were disabled.

Automated Means Test Letter Menu \[EAS MT AUTO LETTERS MENU\]

Search For MT Anniversary Dates \[EAS MT LETTERS SEARCH\]

Veteran MT Return Edit \[EAS MT RETURNED\]

Letters Print Menu \[EAS MT PRINT MENU\]

Sixty Day Letters Print \[EAS MT 60 DAY LETTER PRINT\]

Thirty Day Letters Print \[EAS MT 30 DAY LETTER PRINT\]

Zero Day Letters Print \[EAS MT 0 DAY LETTER PRINT\]

Reprint Letters by Processing Date \[EAS MT REPRINT LETTERS\]

Reprint Single Letter \[EAS MT REPRINT SINGLE LETTER\]

Print Report of Contact \[EAS MT REPORT OF CONTACT\]

User Enrollee Site Print Override \[EAS MT UES OVERRIDE\]

Report Menu \[EAS MT REPORT MENU\]

Count of pending letters to be printed \[EAS MT PENDING LETTERS\]

Automated MT Letters Summary Report \[EAS MT SUMMARY REPORT\]

Means Test Letters Statistic Report \[EAS MT STATISTICS SUMMARY\]

Unreturned Letter Statistic Report \[EAS MT UNRETURNED LETTERS\]

Means Test Expiration by Appt Date \[EAS MT APPT EXPIRATION RPT\]

Means Test Expiration Report \[EAS MT EXPIRATIONS\]

User Enrollee Status for MT Letters \[EAS MT UE STATUS\]

EAS MT Parameter Menu \[EAS MT SETUP MENU\]

EAS MT Parameter Entry/Edit \[EAS MT PARAMETERS\]

Prohibit MT Letters Add/Edit \[EAS MT PROHIBIT EDIT\]

Edit Final Section of Letters \[EAS MT LETTERS EDIT\]

Print a Test Letter (EAS MT) \[EAS MT TEST LETTER\]

Clear Letter Search In-Use flag \[EAS MT CLEAR IN USE FLAG\]

The following background jobs should no longer be scheduled:

Background print job for EAS MT Letters \[EAS MT LETTER BG PRINT\]

Background search for MT Anniversary dates \[EAS MT LETTERS BG SEARCH\]

Daily Means Test Expiration Report \[EAS MT EXPIRATION BG PRINT\]

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This project was initially undertaken in response to Item \#22 in the "Report of Task Force to Review Enrollment, Means Testing and Income Verification" (a.k.a. Rossio Report) dated December 15, 2000. In the area of Means Test (MT) Deficiencies, Item \#22 required that the Veterans Health Administration (VHA) identify best practices for means testing and acquiring veterans’ signatures at the local level and explore the promulgation of these best practices throughout the system. Until Patch EAS\*1\*3 was released in April 2002, there were no provisions within Veterans Information System & Technology Architecture (V*IST*A) functionality that prevented the scheduling of future appointments for patients who required a means test. Additionally, there was no mechanism present to provide the patient adequate notification of the need to provide a current means test prior to the annual anniversary date. In response to the Rossio Report, the Enrollment Task Force recommended the national implementation of functionality similar to that developed locally at several sites in order to manage scheduling activities for veterans who require the completion of a means test. Sites that had developed and implemented local software (Class III) provided copies of their routines and supporting documentation to the Enrollment Systems Group (ESG) to assist in this endeavor.

Patch EAS\*1\*3 (April 2002) provided a national patch release to the Enrollment Application Systems (EAS) software of locally implemented software that had been converted from Class III to Class I.

Patch EAS\*1\*15 is in response to requests for enhancements and changes to the way means test reminder letters are printed and to correct issues with letter printing as reported by several sites.

##################### Functionality

This project addresses two major issues of functionality for the V*IST*A sites defined as means test deficiencies by the Enrollment Task Force:

- Generation of letters to veterans at designated times prior to the expiration of a veteran's means test and the tracking of letter status.
- Prevention of scheduling future appointments or the check-in/check-out of appointments for patients requiring a means test.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this Technical Manual, both a User Manual and PIMS User Manual change pages will be released with the Local Signed MT Application software.

You can download the Local Signed MT Application User and Technical Manuals as follows:

From the Anonymous Directory:

1.  Go to the anonymous.software directory.
2.  Ftp the files listed in the following table. Remember to use binary format.

|                  |                             |
|------------------|-----------------------------|
| File Name    | Documentation Component |
| EAS_1_P15_UM.pdf | User Manual                 |
| EAS_1_P15_TM.pdf | Technical Manual            |

From the Project Notebook Web Page:

REDACTED

From VistA University, Enrollment Training Initiatives, Local Means Test ~ Appointment Blocking:

REDACTED

You may obtain a .pdf version of the PIMS v5.3 User Manual – Scheduling Module through the V*IST*A Documentation Library REDACTED. References to the functionality included in the Local Signed MT Application software may be found in the Appointment Menu under the Make Appointment and Check-in/Unsched. Visit options.

# Implementation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This applies to the original installation of this software in Patch EAS\*1\*3. Subsequent patches to this software do not require pre-installation steps other than as specified in appropriate patch documents.

Any sites that have loaded the Local Signed Means Test Class III software must back out any routines which were modified by that software and restore them to Gold status before installing Patch EAS\*1\*3. A list of the affected routines follows:

Checksums:

DG10 value = 6376645

DGMTEO value = 4567628

DGRPD value = 19143142

SDAMWI1 value = 7639750

The following patches must be installed PRIOR TO installation of Patch EAS\*1\*15:

- Kernel patch – XU\*8\*134
- Scheduling patches - SD\*5.3\*193, SD\*5.3\*223, SD\*5.3\*241
- Registration patch - DG\*5.3\*426
- PCE patch – PX\*1\*111

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed installation instructions may be found in the current patch documentation.

## Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following installation of Patch EAS\*1\*3, users must be assigned the new menu option, Automated Means Test Letter Menu, in order to have access to the functionality provided by this patch. Users would include site personnel involved in patient workload credit, appointment management, and other staff involved in the enrollment and/or scheduling of patients.

The EAS MTOVERRIDE security key should be assigned to those users responsible for making appointments who <u>MAY</u> need to override the blocking action. (See details elsewhere in this manual.) Assignment of this key should be severely restricted.

The letters functionality uses the OFFICIAL VA NAME, Field \#100, in the INSTITUTION File, \#4, for the primary facility as the first line in the return address. If this field is not populated, the default “VA Medical Center” is used. You should also ensure that the following fields in the INSTITUTION file for the primary facility are correctly populated:

> Street Addr. 1, Field \#1.01

> Street Addr. 2, Field \#1.02

> City, Field \#1.03

> Zip, Field \#1.04

> State, Field \#.02

The EAS MTSUPV security key must be assigned as appropriate. (See details elsewhere in this manual.) The individual assigned this key must then:

> Use the Edit Final Section of Letter \[EAS MT LETTERS EDIT\] option to edit the Final Letter Section for each of the three letters in the EAS MT LETTERS File, \#713.3 for the primary facility. Local information may also be entered into the Report of Contact form. See the User Manual for specifics on entering this section. The wording of the initial section of each letter has been specified by the Health Administration Services Office and is not to be modified. In the case of an integrated site with multiple divisions, additional Final Letter Sections may be added for each division if desired, or the common primary facility entry may be used for all divisions.

> Edit the parameters from the EAS MT Parameter Menu \[EAS MT SETUP MENU\]. See the User Manual for specifics on entering this section. At a minimum, you need to enter the PRIMARY PRINT DEVICE Field, \#5.

Due to the potential quantity of letters that may be generated, it is necessary for any printers being used to print the means test letters to be configured as spooled devices on your network. Since the letters will be streamed to the selected device, a network printer that is not spooled may “lose” letters if its print buffer becomes filled. If you are having problems printing, please check the latest FAQ for current changes and tips.

For subsequent patch releases to this software, review the appropriate patch documentation for any specific patch post-installation steps.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are exported with Patch EAS\*1\*3.

|             |                            |                                                                                                                                                                                                                                                                                  |            |
|-------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| File \# | File Name              | Description                                                                                                                                                                                                                                                                  | Global |
| 713         | EAS MT Parameters File     | Contains the site-specific parameters that are used by the Enrollment Application System. The “EAS MT Parameters” menu option sets the parameters used in the auto-generation of the 60, 30, and 0-day means test letters.                                                       | ^EAS       |
| 713.1       | EAS MT Patient Status File | Contains the patient list for which the automated means test letters have been generated. Will also allow specific patients to be flagged from having means test reminder letters generated. Based on local Class III file \#6185243.                                            | ^EAS       |
| 713.2       | EAS MT Letters Status File | Contains the patient’s means test anniversary date and letter threshold dates. Entries are generated when the auto-generated means test letter functionality runs for reminder letters. 60/30/0-day thresholds are set with respective Flag or Print? and Printed status fields. | ^EAS       |
| 713.3       | EAS MT Letters File        | Contains the EAS means test letters that may be sent out by a site. The initial section of the letter should not be modified locally. Facilities should enter facility specific information in the Final Section field.                                                          | ^EAS       |

## File Flow (Relationships between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# (or range of File \#s)

5\. Select Standard listing format

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “Pointer To”.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Templates have been removed and recoded into the software.

# # Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines in the Local Signed MT Application software do not require mapping.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MT^EASMTCHK is a supported API on the DBA menu.

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of EAS routines with checksums included in the initial release of the Local Signed MT Application software. The second line of each of these routines will look like:

\<tab\>;;1.0;ENROLLMENT APPLICATION SYSTEM;\*\*\[patch list\]\*\*;MAR 15, 2001

CHECK^XTSUMBLD results

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Before Patch</strong></td>
<td><p id="after-patch" class="heading">After Patch*</p></td>
<td><strong>Patch List</strong></td>
<td><p id="bytes" class="heading">Bytes*</p></td>
</tr>
<tr class="even">
<td>EASMTCHK</td>
<td>N/A</td>
<td>4750265</td>
<td>3</td>
<td>5239</td>
</tr>
<tr class="odd">
<td>EASMTL1</td>
<td>N/A</td>
<td>7113958</td>
<td>3</td>
<td>5022</td>
</tr>
<tr class="even">
<td>EASMTL10</td>
<td>N/A</td>
<td>7319092</td>
<td>3</td>
<td>5119</td>
</tr>
<tr class="odd">
<td>EASMTL2</td>
<td>N/A</td>
<td>4752261</td>
<td>3</td>
<td>4613</td>
</tr>
<tr class="even">
<td>EASMTL6</td>
<td>N/A</td>
<td>9156246</td>
<td>3</td>
<td>6904</td>
</tr>
<tr class="odd">
<td>EASMTL6A</td>
<td>N/A</td>
<td>5560639</td>
<td>3</td>
<td>3819</td>
</tr>
<tr class="even">
<td>EASMTL6B</td>
<td>N/A</td>
<td>2494451</td>
<td>3</td>
<td>2295</td>
</tr>
<tr class="odd">
<td>EASMTL8</td>
<td>N/A</td>
<td>5784758</td>
<td>3</td>
<td>4023</td>
</tr>
<tr class="even">
<td>EASMTPAR</td>
<td>N/A</td>
<td>1812108</td>
<td>3</td>
<td>1465</td>
</tr>
<tr class="odd">
<td>EASMTRP1</td>
<td>N/A</td>
<td>6480721</td>
<td>3</td>
<td>4447</td>
</tr>
<tr class="even">
<td>EASMTRP2</td>
<td>N/A</td>
<td>2007560</td>
<td>3</td>
<td>1723</td>
</tr>
<tr class="odd">
<td>EASMTRPT</td>
<td>N/A</td>
<td>12856390</td>
<td>3</td>
<td>7207</td>
</tr>
<tr class="even">
<td>EASMTUTL</td>
<td>N/A</td>
<td>6116353</td>
<td>3</td>
<td>5810</td>
</tr>
</tbody>
</table>

See appropriate patch documentation for current checksums.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EAS MT Auto Letters Menu may be provided to selected users as a separate secondary menu option or attached to an existing local menu as deemed appropriate by your site.

Certain designated users may be assigned the EAS MT OVERRIDE security key, allowing them to override any MT blocking action that might occur when entering a future appointment.

Users must be given the EAS MTSUPV security key in order to use the EAS MT Parameters Menu option. Access to this option will be at the site’s discretion, but is normally limited to the Enrollment Coordinator or other appropriate designated individual.

## Tasked Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the site’s discretion, the following options may be used to run auto MT letters as a tasked background job:

- Background Search for MT Anniversary Dates \[EAS MT LETTERS BG SEARCH\] – searches for 60-day MT threshold dates
- Background print job for EAS MT Letters \[EAS MT LETTERS BG PRINT\] – prints all pending auto-generated MT letters/forms
- Daily Means Test Expiration Report \[EAS MT EXPIRATION BG PRINT\] – background prints daily MT expiration of anniversary dates

*Please note that these options are not part of the interactive EAS MT Auto Letters Menu shown below.*

See Appendix A for detailed instructions on background job setup.

The EAS MT LETTERS BG SEARCH option should be scheduled to run first, followed by the EAS MT LETTERS BG PRINT option. The print option should be scheduled to run no earlier than four hours after the scheduled start time of the EAS MT LETTERS BG SEARCH task to allow ample time for the completion of the background search and file update. The frequency of these tasked jobs can be determined locally.

The EAS MT EXPIRATION BG PRINT option should be scheduled to run after midnight for the previous day's report as this report uses the current date variable (DT) to define the anniversary date for the report.

When scheduling any of these options in the Schedule/Unschedule option, SPECIAL QUEUEING is suggested to ensure a restart of the tasks when the system is rebooted.

## Interactive Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automated Means Test Letter Menu \[EAS MT AUTO LETTERS MENU\]

Search For MT Anniversary Dates \[EAS MT LETTERS SEARCH\]

Veteran MT Return Edit \[EAS MT RETURNED\]

Letters Print Menu ... \[EAS MT PRINT MENU\]

> Sixty Day Letters Print \[EAS MT 60 DAY LETTER PRINT\]

> Thirty Day Letters Print \[EAS MT 30 DAY LETTER PRINT\]

> Zero Day Letters Print \[EAS MT 0 DAY LETTER PRINT\]

Reprint Letters by Processing Date \[EAS MT

> REPRINT LETTERS\]

> Reprint Single Letter \[EAAS MT REPRINT SINGLE LETTER\]

> Print Report of Contact \[EAS MT REPORT OF CONTACT\]

Report Menu ... \[EAS MT REPORT MENU\]

> Count of Pending Letters to be Printed \[EAS MT PENDING LETTERS\]

> Automated MT Letters Summary Report \[EAS MT SUMMARY REPORT\]

> Means Test Letters Statistic Report \[EAS MT STATISTICS SUMMARY\]

> Unreturned Letter Statistic Report \[EAS MT UNRETURNED LETTERS\]

> Means Test Expiration by Appt Date \[EAS MT APPT EXPIRATION RPT\]

> (*Note: This option was added with Patch EAS\*1\*15.)*

> Means Test Expiration Report \[EAS MT EXPIRATIONS\]

EAS MT Parameter Menu ... \[EAS MT SETUP MENU\]

EAS MT Parameter Enter/Edit \[EAS MT PARAMETERS\]

Prohibit MT Letters Add/Edit \[EAS MT PROHIBIT EDIT\]

Edit Final Section of Letters \[EAS MT LETTERS EDIT\]

Print a Test Letter (EAS MT) \[EAS MT TEST LETTER\]

(*Note: This option was added with Patch EAS\*1\*15.)*

Clear Letter Search In-Use flag \[EAS MT CLEAR IN USE FLAG\]

# # Archiving & Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging capabilities exported with the Local Signed MT Application software.

# Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MT^EASMTCHK is a supported API.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no external interfaces associated with the Local Signed MT Application software.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*IST*A package versions (or higher) must be installed prior to installing the local Signed MT Application software.

|                  |                              |
|------------------|------------------------------|
| Package Name | Minimum Version Required |
| Kernel           | 8.0                          |
| VA FileMan       | 22.0                         |
| EAS              | 1.0                          |

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Database Integration Agreements (DBIAs) are required for this software:

DBIA 1850

DBIA3326

DBIA3327

DBIA243-G

DBIA3499

DBIA 3523

DBIAs can be retrieved from the Database Administrator’s menu on Forum. From Forum’s main menu, select the DBA option; then select the Integration Agreements menu. Select Inquiry, and enter the desired DBIA number.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Signed MT Application options have been designed to stand alone.

Scheduling Options are modified to check for the API. If found, Scheduling will check for MT blocking. If the MT software is not installed, Scheduling will ignore.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the Local Signed MT Application software.

# # Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new mail group, EAS MTLETTERS, has been created. Users must be members of this mail group in order to receive the EAS automated Means Test letters statistics, reports, and bulletins. This mail group is exported allowing self-enrollment.

When the tasked jobs are run, members of the EAS MTLETTERS mail group will receive the following bulletins:

- Auto MT letters – All dates already processed
- Auto MT Letters – Processing is currently running
- Auto MT Letters – Processing complete
- Auto MT Letters – Printing completed

A new bulletin for MT completion has been created. EAS MTCOMPLETION will show the veteran’s name, SSN, user completing, and date completed and will be sent to the EAS MTLETTERS mail group. This bulletin can be turned on through the EAS MT PARAMETER MENU, EAS MT PARAMETER ENTRY/EDIT option by enabling the Send Means Test Completion Notice parameter.

When the letters are printed, if a veteran does not have a complete mailing address on file (i.e., street address, city, state, and zip), a message will be sent to the EAS MTLETTERS mail group as notification and the letter will not be printed. If the address is corrected, the letter will print the next time the print job is run.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Signed MT Application software does not transmit data to any remote system/facility database.

### Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging capabilities exported with the Local Signed MT Application software.

### Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized (not VA-produced) products (hardware and/or software) embedded within or required by the Local Signed MT Application software.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures utilized in the Local Signed MT Application software.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no menu options in the Local Signed MT Application software that would be of particular interest to Information Security Officers.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS MTOVERRIDE – Key that allows user to override MT blocking action when entering a future appointment for a patient who requires a new means test. Does not apply to check-in/out.

EAS MTSUPV - Supervisor key required in order to access the EAS MT Parameters Menu for setup of the auto letter parameters.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of recommended VA FileMan access codes for the files in the Local Signed MT Application software.

|             |                       |               |               |               |                |                  |
|-------------|-----------------------|---------------|---------------|---------------|----------------|------------------|
| FILE \# | NAME              | DD ACCESS | RD ACCESS | WR ACCESS | DEL ACCESS | LAYGO ACCESS |
| 713         | EAS MT Parameters     | @             | @             | @             | @              | @                |
| 713.1       | EAS MT Patient Status | @             | @             | @             | @              | @                |
| 713.2       | EAS MT Letter Status  | @             | @             | @             | @              | @                |
| 713.3       | EAS MT Letters        | @             | @             | @             | @              | @                |

### Official Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In accordance with VHA Directive 10-93-142 (“Local Modifications to DHCP Software”), the files and fields exported with the Local Signed MT Application software should not be modified locally.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Acronyms 

##################### 

| Acronym     | Description                                       |
|-----------------|-------------------------------------------------------|
| EAS             | Enrollment Application System                         |
| ESG             | Enrollment Systems Group                              |
| IRM             | Information Resource Management                       |
| MT              | Means Test                                            |
| VAMC            | Veterans Affairs Medical Center                       |
| VHA             | Veterans Health Administration                        |
| VISN            | Veterans Integrated Service Network                   |
| V*IST*A | Veterans Information System & Technology Architecture |

# Appendix A - Background Job Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Background Letter Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION to schedule or reschedule: EAS MT LETTERS BG SEARCH Background search for MT Anniversary dates

...OK? Yes// (Yes)

\(A\)

Edit Option Schedule

Option Name: EAS MT LETTERS BG SEARCH

Menu Text: Background search for MT Anniver TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: \_\_<u>1\_\_</u>

DEVICE FOR QUEUED JOB OUTPUT: \_\_<u>2</u>\_\_

QUEUED TO RUN ON VOLUME SET: \_\_<u>3</u>\_\_

RESCHEDULING FREQUENCY: \_\_<u>4</u>\_\_

TASK PARAMETERS: \_\_<u>5</u>\_\_

SPECIAL QUEUEING: \_\_<u>6</u>\_\_

1.  Enter the time at which you want the background job to run, i.e. <T+1@0100> (tomorrow at 1 AM)
2.  Enter a NULL device
3.  Leave blank
4.  Enter the frequency at which you want the background job to run, i.e. 1D for every day, 1W for once a week. Each site will need to determine the frequency for their facility.
5.  Leave blank
6.  Enter SP (Startup Persistent) to ensure the background job is restarted after a system boot-up and a restart if the task should stop unexpectedly.

*Example of a completed set up:*

Edit Option Schedule

Option Name: EAS MT LETTERS BG SEARCH

Menu Text: Background search for MT Anniver TASK ID: 476769

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: AUG 1,2002@01:00

DEVICE FOR QUEUED JOB OUTPUT: NULL;;80;999

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

## Background Letter Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION to schedule or reschedule: eas mt letters bg print Background print job for EAS MT Letters

...OK? Yes// (Yes)

\(A\)

Edit Option Schedule

Option Name: EAS MT LETTERS BG PRINT

Menu Text: Background print job for EAS MT TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: \_\_<u>1\_\_</u>

DEVICE FOR QUEUED JOB OUTPUT: \_\_<u>2</u>\_\_

QUEUED TO RUN ON VOLUME SET: \_\_<u>3</u>\_\_

RESCHEDULING FREQUENCY: \_\_<u>4</u>\_\_

TASK PARAMETERS: \_\_<u>5</u>\_\_

SPECIAL QUEUEING: \_\_<u>6</u>\_\_

1.  Enter the time to run the background job at, i.e. <T+1@0700> (Tomorrow at 7 AM). This time should be at least several hours after the search was scheduled to run to ensure adequate time for the search to complete and update EAS MT LETTER STATUS File, \#713.2.
2.  Enter the print device the letters are to print to, i.e. DEV\$PRT 10/6/UP;P-REMOTE TCP 1
3.  Leave blank
4.  Enter the frequency the job is to run at, i.e. 1D for every day, 1W for once a week. Each site will need to determine the frequency for their facility. This should be the same frequency that the background search is run at.
5.  Leave blank
6.  Enter SP (Startup Persistent) to ensure the background job is restarted after a system boot-up and a restart if the task should stop unexpectedly.

*Example of a completed setup:*

Edit Option Schedule

Option Name: EAS MT LETTERS BG PRINT

Menu Text: Background print job for EAS MT TASK ID: 476770

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: AUG 1,2002@07:00

DEVICE FOR QUEUED JOB OUTPUT: DEV\$PRT 10/6/UP;P-REMOTE TCP 1

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING: STARTUP

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Acronyms 14
Appendix A - Background Job Setup 15
Archiving & Purging 10
Archiving/Purging 12
C
Callable Entry Points & APIs 10
Callable Routines 7
D
Database Integration Agreements (DBIAs) 11
E
Electronic Signatures 13
Exported Options 8
External Interfaces 10
External Relations 11
External/ Internal Relations 11
F
File Flow (Relationships between files) 5
File List 5
File Security 13
Files 5
G
Glossary 14
I
Implementation 3
Index 17
Installation 3
Interactive Menu Diagram 9
Interfaces 13
Internal Relations 11
Introduction 1
L
List Templates 6
M
Mail Groups, Alerts, and Bulletins 12
Menus 13
O
Official Policy 13
Overview 1
P
Package-wide Variables 11
Post-Installation 4
Pre-Installation 3
Purpose 1
R
Related Manuals 2
Remote Systems 12
Revision History i
Routine List 7
Routines 7
Routines to Map 7
S
Security 12
Security Features 12
Security Keys 13
T
Table of Contents ii
Tasked Background Jobs 8
Templates 6
