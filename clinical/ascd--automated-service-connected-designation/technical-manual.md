---
title: ASCD Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: ASCD
app_name: Automated Service Connected Designation
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 60
description: 
audience: 
keywords: 
  - table
  - contents
  - sdsc
  - encounter
  - report
  - routine
  - ascd
  - date
  - patient
  - service
page_count: 0
word_count: 7509
section_count: 35
table_count: 11
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: September 2007
revision_count: 1
revision_newest: 9/20/2007
revision_oldest: 9/20/2007
docx_url: "https://www.va.gov/vdl/documents/Clinical/Automated_Service_Connected_Designation/ascd_sd_53_495_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Automated_Service_Connected_Designation/ascd_sd_53_495_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=174"
---

![](ascd-technical-manual/001.png)

Scheduling 5.3

Automated Service Connected Designation

(ASCD)

Technical Manual

September 2007

Health Program Support Office (HPSO)

Revision History

|           |          |                      |                                    |
|-----------|----------|----------------------|------------------------------------|
| Date      | Revision | Description          | Author                             |
| 9/20/2007 | 1.0      | Creation of document | <span class="mark">REDACTED</span> |
|           |          |                      |                                    |
|           |          |                      |                                    |
|           |          |                      |                                    |
|           |          |                      |                                    |
|           |          |                      |                                    |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [## Operating Specifics](#operating-specifics)
  - [Sizing Information](#sizing-information)
  - [Global Journaling](#global-journaling)
  - [Translation Tables](#translation-tables)
  - [Bulletins](#bulletins)
  - [Mail Groups](#mail-groups)
    - [SDSC NIGHTLY TALLY](#sdsc-nightly-tally)
    - [SDSC NIGHTLY TALLY Example](#sdsc-nightly-tally-example)
- [Files](#files)
  - [Overview](#overview)
  - [File List](#file-list)
    - [SDSC SERVICE CONNECTED CHANGES](#sdsc-service-connected-changes)
    - [DISABILITY CONDITION](#disability-condition)
  - [File Protection](#file-protection)
  - [Files with Security Access](#files-with-security-access)
- [Routines](#routines)
  - [Overview](#overview-1)
  - [List of Routines](#list-of-routines)
    - [DVB458P\](#dvb458p)
    - [PXBAPI21](#pxbapi21)
    - [PXBAPI22](#pxbapi22)
    - [PXCEVFI1](#pxcevfi1)
    - [PXCEVFI2](#pxcevfi2)
    - [SD53P495](#sd53p495)
    - [SDSCOM](#sdscom)
    - [SDSCAPI](#sdscapi)
    - [SDSCCHK](#sdscchk)
    - [SDSCCLM](#sdscclm)
    - [SDSCEDT](#sdscedt)
    - [SDSCINS](#sdscins)
    - [SDSCLM](#sdsclm)
    - [SDSCLM1](#sdsclm1)
    - [SDSCLST](#sdsclst)
    - [SDSCMSR](#sdscmsr)
    - [SDSCNSCP](#sdscnscp)
    - [SDSCOMP](#sdscomp)
    - [SDSCPRG](#sdscprg)
    - [SDSCPRM](#sdscprm)
    - [SDSCPRV](#sdscprv)
    - [SDSCRP1](#sdscrp1)
    - [SDSCRP2](#sdscrp2)
    - [SDSCRPT1](#sdscrpt1)
    - [SDSCRPT2](#sdscrpt2)
    - [SDSCSSD](#sdscssd)
    - [SDSCUSR](#sdscusr)
    - [SDSCUTL](#sdscutl)
- [Exported Options](#exported-options)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Options](#exported-options-1)
    - [SDSC CHECK COMPILE](#sdsc-check-compile)
    - [SDSC COMPILE](#sdsc-compile)
    - [SDSC EDIT BY DATE](#sdsc-edit-by-date)
    - [SDSC EDIT LISTMAN](#sdsc-edit-listman)
    - [SDSC ENC REPORT](#sdsc-enc-report)
    - [SDSC FIRST PARTY REPORT](#sdsc-first-party-report)
    - [SDSC MANAGER SUMMARY REPORT](#sdsc-manager-summary-report)
    - [SDSC MENU](#sdsc-menu)
    - [SDSC NIGHTLY COMPILE](#sdsc-nightly-compile)
    - [SDSC PROVIDER REPORT](#sdsc-provider-report)
    - [SDSC PROVIDER TOTAL REPORT](#sdsc-provider-total-report)
    - [SDSC PURGE NSC ENC](#sdsc-purge-nsc-enc)
    - [SDSC RECOVERED REPORT](#sdsc-recovered-report)
    - [SDSC REPORTS](#sdsc-reports)
    - [SDSC SERVICE TOTAL REPORT](#sdsc-service-total-report)
    - [SDSC SINGLE EDIT](#sdsc-single-edit)
    - [SDSC SITE PARAMETER](#sdsc-site-parameter)
    - [SDSC THIRD PARTY REPORT](#sdsc-third-party-report)
    - [SDSC UNBILL AMT REPORT](#sdsc-unbill-amt-report)
    - [SDSC USER REPORT](#sdsc-user-report)
    - [SDSC USER TOTAL REPORT](#sdsc-user-total-report)
    - [PXCE ENCOUNTER ENTRY SUPER](#pxce-encounter-entry-super)
  - [Exported Protocols](#exported-protocols)
    - [SDSC ACCEPT](#sdsc-accept)
    - [SDSC CHANGE](#sdsc-change)
    - [SDSC DETAIL](#sdsc-detail)
    - [SDSC MENU](#sdsc-menu-1)
    - [SDSC RECORD MENU](#sdsc-record-menu)
    - [SDSC SEND](#sdsc-send)
  - [Exported List Templates](#exported-list-templates)
    - [SDSC DETAIL](#sdsc-detail-1)
    - [SDSC REVIEW](#sdsc-review)
  - [Exported Parameter Definition](#exported-parameter-definition)
    - [SDSC SITE PARAMETER](#sdsc-site-parameter-1)
  - [Exported Mail Group](#exported-mail-group)
    - [SDSC NIGHTLY TALLY](#sdsc-nightly-tally-1)
  - [## Exported Security Keys](#exported-security-keys)
    - [SDSC CLINICAL](#sdsc-clinical)
    - [SDSC SUPER](#sdsc-super)
- [Archiving and Purging](#archiving-and-purging)
  - [## Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines/Entry Points/Application Programmer Interfaces](#callable-routinesentry-pointsapplication-programmer-interfaces)
  - [Overview](#overview-2)
  - [Callable Routines](#callable-routines)
- [External Relationships](#external-relationships)
  - [Overview](#overview-3)
  - [Minimum Package Requirement](#minimum-package-requirement)
  - [DBIAs](#dbias)
- [Internal Relationships](#internal-relationships)
- [Global Variables](#global-variables)
- [Glossary](#glossary)
  - [Acronyms](#acronyms)
  - [Definitions](#definitions)
- [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
  - [Overview](#overview-4)
- [Cross-References](#cross-references)
  - [Overview](#overview-5)
  - [Traditional Style Cross-References](#traditional-style-cross-references)
  - [New Style Cross-reference](#new-style-cross-reference)
- [Appendix A – Data Dictionary List of file \#409.48](#appendix-a-data-dictionary-list-of-file-40948)
- [Appendix B – Data Dictionary List of file \#31](#appendix-b-data-dictionary-list-of-file-31)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to describe the software enhancements to the VistA Legacy Mumps application that were done in support of a request submitted by Gail Graham, Director, Health Data and Informatics (HD&I) to automate the clinician’s decision-making process when marking a patient encounter either Service Connected (SC) or Non-Service Connected (NSC) within the Patient Care Encounter (PCE) and Scheduling packages.

Outpatient visits for NSC disorders are potentially billable in the Veterans Administration (VA) VistA, but are frequently and incorrectly attributed to service connected conditions. Each incorrect attribution represents lost potential revenue from insurance companies that could be invested in additional medical care to veterans. Providers are required to designate at the point of care if a specific patient care encounter is SC based on available disability rating information. The codes and nomenclature associated with the SC rating are particular to the Veteran Benefits Administration (VBA) and not consistent with industry based medical coding systems such as International Classification of Diseases (ICD) or Current Procedural Terminology (CPT). VA providers find trying to associate these two disparate coding and terminology systems confusing and ambiguous.

Currently, VA providers make SC/NSC determinations by manually selecting SC or NSC based on the conditions treated during the encounter and comparing those conditions to the list of SC conditions shown on the Computerized Patient Record System (CPRS) screen or on the printed encounter form. Both International Classification of Diseases Clinical Modification V.9 (ICD-9-CM) codes and CPT codes are used to populate the encounter form used to describe the services provided to the patient during the encounter. ICD-9-CM is the code set required for use by Health Insurance Portability and Accountability Act (HIPAA) and has been adopted by Veterans Health Administration (VHA) for the coding of all diagnoses, symptoms and conditions for inpatient/outpatient encounters. The VBA list of service connected disabilities is ambiguous and often covers a wide range of conditions making it difficult for providers to easily discern whether or not the treated condition fits the list of SC disabilities specific to the patient. Since the time to examine and treat patients is limited, providers often skip making this determination or select what seems easiest or most helpful to the patient by making an encounter service connected whether or not it is supported by documentation.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this document is to define the technical design of the Automated Service Connected Designation (ASCD) project. This project will automate the SC decision for outpatient encounters using the mapped ICD/Rated Disability codes at the time the clinician actually picks the ICD code for the encounter within the Patient Care Encounter (PCE) and Scheduling packages. Thus, when a provider or clinician chooses the diagnosis code for the encounter the system will automatically determine if the diagnosis is related to the veteran's established service connected conditions, and will likewise automatically make the proper SC/NSC determination for that encounter. This software recognizes potentially billable encounters for SC veterans that cannot be automatically matched to Rated Disability codes. These encounters are displayed in reports for coders and/or utilization review staffs who then review the patient visit information, edit incorrect SC designated encounters, and release them to Claims Tracking for billing where appropriate.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Operating Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses specific information that is needed to run the ASCD software.

## Sizing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*SDSC SERVICE CONNECTED CHANGES \[^SDSC(409.48*

Growth of the ASCD global is dependent upon the number of service connected encounters generated by your facility per day. Each encounter saved in this file is estimated at 300 bytes per entry.

*DISABILITY CONDITION \[^DIC(31, -*

The Disability Condition File is estimated to increase by 86,400 bytes with the installation of patch DVB\*4.0\*58.

## Global Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no recommendations on journaling the ^SDSC( globals.

## Translation Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^SDSC(409.48 global is created when installing the SD\*5.3\*495 build at a site with the Class III software upon conversion of file \#626140. For sites that do not have the Class III software, the ^SDSC(409.48 global will be created when the first record is added through PCE/SD or the SDSC NIGHTLY COMPILE option. The ^SDSC(409.48 global will be created with the access privileges defined for files at the site.

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently there are no bulletins set up for the ASCD (Automated Service Connected Designation) software.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SDSC NIGHTLY TALLY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This mail group should be modified to include the personnel who should be receiving a summary e-mail of those encounters found during the nightly compile.

### SDSC NIGHTLY TALLY Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is an example of adding user SDSCUSER, FIRST to the mail group SDSC NIGHTLY TALLY.

> Option: \[XMEDITMG \] Mail Group Edit

> Select MAIL GROUP NAME: SDSC NIGHTLY TALLY

> MAIL GROUP NAME: SDSC NIGHTLY TALLY//

> Select MEMBER: SDSCUSER, FIRST

> Are you adding 'SDSCUSER, FIRST’ as a new MEMBER (the 3RD for this MAIL GROUP)? N

> o// Y (Yes)

> TYPE: CC

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a listing of ASCD files with their associated VA FileMan security access, and brief descriptions of the type of data stored.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*WARNING: It is not recommended that you use VA FileMan to edit any of the files directly! Furthermore, editing these files without direction from the programmers may cause the package to become non-functional!*

### SDSC SERVICE CONNECTED CHANGES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file contains a list of encounters which were selected for review based on a comparison of the encounter’s ICD9 diagnosis codes and the mapped ICD/Rated Disability codes. See Appendix A for a complete data dictionary list of file \#409.48.

### DISABILITY CONDITION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file contains a cross-reference between the national standard VBA disability codes and their equivalent ICD9 codes. See Appendix B for a data dictionary list of file \#31.

## File Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASCD package files contain files that are standardized for this module. They carry a higher level of file protection with regard to Delete, Read, Write, and Laygo access and should not be edited locally unless otherwise directed. The data dictionaries for all files should NOT be altered.

The package has one (1) level of VA FileManager file protection enabled on its files.

> @ - Programmer access to files

## Files with Security Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                            |               |              |              |              |              |              |
|--------------------------------------------|---------------|--------------|--------------|--------------|--------------|--------------|
|                                            | FILE          | DD           | RD           | WR           | DEL          | LAYGO        |
| FILE NAME                                  | NUMBER        | ACCESS       | ACCESS       | ACCESS       | ACCESS       | ACCESS       |
| ------------------------------------------ | ------------- | ------------ | ------------ | ------------ | ------------ | ------------ |
| SDSC SERVICE CONNECTED CHANGES             | 409.48        | @            | @            | @            | @            | @            |
| DISABILITY CONDITION                       | 31            | N/A          | N/A          | N/A          | N/A          | N/A          |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASCD uses SDSC as its namespace. The routines are exported via a host file.

## List of Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines below are exported as part of the ASCD project. They are listed with brief functional summaries.

### DVB458P\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Six routines namely DVB458P, DVB458P1, DVB458P2, DVB458P3, DVB458P4, DVB458P5, DVB458P6 were exported as part of the ASCD project in the DVB\*4.0\*58 patch. These routines introduce modifications to the DISABILITY CONDITION file (#31). They provide the mapping of the Veteran Benefits Administration (VBA) 4 digit RATED DISABILITIES (VA) code terminology to the ICD-9-CM codes.

### PXBAPI21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine was modified to add a new subroutine OPCHK and additional code to perform checks on a standalone encounter entered with the PCE package.

### PXBAPI22

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine was modified to call the \$\$SC^SDSCAPI API to automate the response "Was treatment for SC Condition?" for each diagnosis code entered in the PCE and Scheduling package.

### PXCEVFI1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine was modified to capture the IEN of the diagnosis code that the user entered in PCE to facilitate the automation of the "Was treatment for SC Condition?" response.

### PXCEVFI2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine was modified to add the VBA DX CODE number to the display of the Rated Disabilities (VA) names.

### SD53P495

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This post install routine is released with SD\*5.3\*495 patch. It performs the conversion of the Class III ANU SERVICE CONNECTED CHANGES File (#626140) to the new Class I SDSC SERVICE CONNECTED CHANGES file (#409.48). It also sets the default value of 30 days in the Site PARAMETERS file (#8989.5) used by the SDSC NIGHTLY COMPILE option.

### SDSCOM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine was modified to call \$\$ST^SDSCAPI API to review the encounter diagnosis codes against the patient rated disabilities codes and then make a determination as to whether the encounter should be sent to the ASCD file (#409.48) for review.

### SDSCAPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine determines the service connected value for a specific diagnosis code or the overall encounter diagnosis code. This determination is based on the mapping of a patient’s rated disability codes and ICD-9-CM codes. The entry point “SC” is called to automate the SC value. The entry point “ST” is generally called at “check out” when deciding whether the encounter should be sent for review.

### SDSCCHK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine goes through the Outpatient Encounter File, (#409.68) to determine those encounters that have not been reviewed based on a user specified date range. The results are compiled in the “Compile Results Report” and displays a number of reasons why encounters were not compiled.

### SDSCCLM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine calls IB API routine IBRSUTL to update the claims tracking file.

### SDSCEDT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine handles the logic to review and edit encounters entered in the ASCD file. It contains the entry point for editing encounters by date and also for editing a single encounter.

### SDSCINS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine checks the Audit File (#1.1) for any newly identified insurance policies. It is used during the nightly compile to re-check previous encounters to see if any may have become reviewable by the addition of an insurance policy.

### SDSCLM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains ListMan logic for the SDSC EDIT LISTMAN option to review and edit encounters entered in the ASCD file.

### SDSCLM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains additional ListMan logic for the SDSC EDIT LISTMAN option to review encounters selected by the SCOUT compile.

### SDSCLST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains the main entry point for the SDSC EDIT LISTMAN option. It also builds the list of encounter entries to be reviewed for the date range specified.

### SDSCMSR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the Manager Summary Report and is available only to users with the SDSC SUPER key.

### SDSCNSCP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to purge encounters with a status of NEW where the Visit SC value equals the ASCD value of "NO" for a specified division(s) and a user defined date range. Users must have the SDSC SUPER key to run this option.

### SDSCOMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains the entry points for manually and automatically (TaskMan) compiling a list of encounters to be used by the ASCD review options.

### SDSCPRG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine will purge any encounters in the SDSC SERVICE CONNECTED CHANGES FILE (#409.48) that have been deleted from the OUTPATIENT ENCOUNTER File (#409.68).

### SDSCPRM 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine will allow a user with the SDSC SUPER key to change the number of days in the Site PARAMETERS File (#8989.5).

### SDSCPRV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the Provider Total Summary Report.

### SDSCRP1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the Unbilled/Billable Amount Report.

### SDSCRP2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains the logic for the Estimated Recovered Costs Report for ASCD.

### SDSCRPT1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains the entry points for several of the ASCD reports. These reports are

1)  Service Connected Encounters Report \[SDSC ENC REPORT\]
2)  First Party Billable Service Connected Report \[SDSC FIRST PARTY REPORT\]
3)  Third Party Billable Service Connected Report \[SDSC THIRD PARTY REPORT\]
4)  Provider Service Connected Encounters Report \[SDSC PROVIDER REPORT\]
5)  User Service Connected Encounters Report \[SDSC USER REPORT\]

### SDSCRPT2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains additional logic for the ASCD reports listed in 4.2.24.

### SDSCSSD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the Clinic Service Total Summary Report.

### SDSCUSR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the User Total Summary Report.

### SDSCUTL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains several utility functions used by the ASCD software.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a diagram of menus exported with the ASCD project.

> Automated Service Connected Designation Menu (SDSC MENU)

> \|

> \|

> --------------------------------------------- ASCD Compile Parameter \[SDSC

> SITE PARAMETER\]

> \*\*LOCKED: SDSC SUPER\*\*

> ----- ASCD Reports \[SDSC REPORTS\] ----------- Clinic Service Total Summary

> \| Report \[SDSC SERVICE TOTAL

> \| REPORT\]

> \|

> \|---------------------------------- Compile Results Report \[SDSC

> \| CHECK COMPILE\]

> \|

> \|---------------------------------- Estimated Recovered Costs

> \| Report \[SDSC RECOVERED REPORT\]

> \|

> \|---------------------------------- First Party Billable Service

> \| Connected Report \[SDSC FIRST

> \| PARTY REPORT\]

> \|

> \|---------------------------------- Manager Summary Report \[SDSC

> \| MANAGER SUMMARY REPORT\]

> \| \*\*LOCKED: SDSC SUPER\*\*

> \|

> \|---------------------------------- Provider Service Connected

> \| Encounters Report \[SDSC PROVIDER

> REPORT\]

> \|

> \|---------------------------------- Provider Total Summary Report

> \| \[SDSC PROVIDER TOTAL REPORT\]

> \|

> \|---------------------------------- Service Connected Encounters

> \| Report \[SDSC ENC REPORT\]

> \|

> \|---------------------------------- Third Party Billable Service

> \| Connected Report \[SDSC THIRD

> \| PARTY REPORT\]

> \|

> \|---------------------------------- Unbilled/Billable Amount

> \| Report \[SDSC UNBILL AMT REPORT\]

> \|

> \|

> \|---------------------------------- User Service Connected

> \| Encounters Report \[SDSC USER REPORT\]

\|

> \|---------------------------------- User Total Summary Report

> \[SDSC USER TOTAL REPORT\]

> --------------------------------------------- Compile ASCD Encounters by

> Date Range \[SDSC COMPILE\]

> --------------------------------------------- Edit ASCD Encounters by Date

> Range \[SDSC EDIT BY DATE\]

> --------------------------------------------- Edit ASCD Encounters by

> ListMan \[SDSC EDIT LISTMAN\]

> --------------------------------------------- Edit Single ASCD Encounter

> \[SDSC SINGLE EDIT\]

> --------------------------------------------- Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]

> \*\*LOCKED: SDSC SUPER\*\*

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are exported with ASCD and are listed below with brief functional summaries.

### SDSC CHECK COMPILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MENU TEXT: *Compile Results Report*

> TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report prints out why encounters were not compiled into ASCD.

> ROUTINE: EN^SDSCCHK

### SDSC COMPILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Compile ASCD Encounters by Date Range*

> TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option compares POVs of visits/encounters with the rated disabilities of a patient to verify if the visit is service connected. If the visit cannot be verified as service connected, the encounter will be stored for review and reporting.

> This option is interactive. It will ask the users for a date range. It is suggested that this be run at least once a month to update any records not completed at the time of the nightly compile.

ROUTINE: COMPILE^SDSCOMP

### SDSC EDIT BY DATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Edit ASCD Encounters by Date Range*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option allows the user to edit the service connected information for a set of previously compiled encounters for a specific date range.

ROUTINE: START^SDSCEDT

### SDSC EDIT LISTMAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Edit ASCD Encounters by ListMan*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option allows the user to review and edit Automated Service Connected Designation encounters via a ListMan screen.

ROUTINE: EN^SDSCLST

### SDSC ENC REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Service Connected Encounters Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report displays details of the current status of each encounter found by the Automated Service Connected Designation compile.

ROUTINE: RDPOV^SDSCRPT1

### SDSC FIRST PARTY REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *First Party Billable Service Connected Report*

> TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report displays information on any encounters found by the ASCD compile that are potentially billable to first party (means test).

ROUTINE: NSCCOP^SDSCRPT1

### SDSC MANAGER SUMMARY REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Manager Summary Report*

TYPE: run routine

LOCK: SDSC SUPER PACKAGE: SCHEDULING

> DESCRIPTION: This option compiles and prints the ASCD Managers Summary Report.

ROUTINE: EN^SDSCMSR

### SDSC MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Automated Service Connected Designation Menu*

TYPE: menu PACKAGE: SCHEDULING

> DESCRIPTION: This menu contains all the options related to the Automated Service

> Connected Designation module.

ITEM: SDSC COMPILE

> SDSC EDIT BY DATE

> SDSC SINGLE EDIT

> SDSC EDIT LISTMAN

> SDSC REPORTS

> SDSC PURGE NSC ENC

> SDSC SITE PARAMETER

### SDSC NIGHTLY COMPILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Compile ASCD Encounters on a Nightly Basis*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option compares POVs of visits/encounters with the rated disabilities of a patient to verify if the visit is service connected. If the visit cannot be verified as service connected, the encounter will be stored for review and reporting.

> This option is not interactive. It compiles data for the previous day. It is suggested that this option be scheduled in TaskMan to run daily.

ROUTINE: AUTODT^SDSCOMP

### SDSC PROVIDER REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Provider Service Connected Encounters Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report can either display details or a summary of the encounters found by the ASCD compile sorted by the primary provider from the encounter/visit.

ROUTINE: SCPRV^SDSCRPT1

### SDSC PROVIDER TOTAL REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Provider Total Summary Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option displays provider totals by division for the VBA okay codes, changed service connected encounters and encounters where the service connection was not changed.

ROUTINE: EN^SDSCPRV

### SDSC PURGE NSC ENC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MENU TEXT: *Purge ASCD NSC Encounters*

> TYPE: run routine LOCK: SDSC SUPER

> DESCRIPTION: This option will purge encounters with a status of NEW where the Encounter SC value equals the ASCD value of "NO" for a specified division(s) within a user defined date range. Users must have the SDSC SUPER key to run this option.

> ROUTINE: EN^SDSCNSCP

> PACKAGE: Scheduling

### SDSC RECOVERED REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Estimated Recovered Costs Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This is a report which will look for bills and payments for encounters that have had their Service Connected status changed by ASCD options.

ROUTINE: EN^SDSCRP2

### SDSC REPORTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *ASCD Reports*

TYPE: menu PACKAGE: SCHEDULING

> DESCRIPTION: This menu contains all the reports related to the Automated Service Connected Designation module.

ITEM: SDSC MANAGER SUMMARY REPORT

> SDSC PROVIDER TOTAL REPORT

> SDSC SERVICE TOTAL REPORT

> SDSC USER TOTAL REPORT

> SDSC CHECK COMPILE

> SDSC ENC REPORT

> SDSC FIRST PARTY REPORT

> SDSC PROVIDER REPORT

> SDSC RECOVERED REPORT

> SDSC UNBILL AMT REPORT

> SDSC THIRD PARTY REPORT

> SDSC USER REPORT

### SDSC SERVICE TOTAL REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Clinic Service Total Summary Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report displays the Service Connected changes by clinical service M:MEDICINE;S:SURGERY;P:PSYCHIATRY;R:REHAB MEDICINE;N:NEUROLOGY;0:NONE and by the clinic with that service.

ROUTINE: EN^SDSCSSD

### SDSC SINGLE EDIT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Edit Single ASCD Encounter*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option allows the user to edit the service connected information for any specific encounter previously selected by a compile.

ROUTINE: START1^SDSCEDT

### SDSC SITE PARAMETER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *ASCD Compile Parameter*

TYPE: run routine LOCK: SDSC SUPER

PACKAGE: SCHEDULING

> DESCRIPTION: This option allows the supervisor to adjust the number of days the compile uses to check for completed outpatient encounters.

ROUTINE: EN^SDSCPRM

### SDSC THIRD PARTY REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Third Party Billable Service Connected Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report displays information on any encounters found by the ASCD compile that are potentially billable to third party (insurance).

ROUTINE: NSCINS^SDSCRPT1

### SDSC UNBILL AMT REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *Unbilled/Billable Amount Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This option prints a report of those encounters whose service connection was changed and not yet billed. If a user has the supervisor key they will also be able to run the supervisor option which contains the names of the last two editors.

ROUTINE: START^SDSCRP1

### SDSC USER REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *User Service Connected Encounters Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report can either display details or a summary of the encounters found by the ASCD compile sorted by the user who last edited the service connection information for the encounter.

ROUTINE: SCUSR^SDSCRPT1

### SDSC USER TOTAL REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *User Total Summary Report*

TYPE: run routine PACKAGE: SCHEDULING

> DESCRIPTION: This report will print user information.

ROUTINE: EN^SDSCUSR

### PXCE ENCOUNTER ENTRY SUPER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU TEXT: *PCE Encounter Data Entry - Supervisor*

TYPE: action PACKAGE: PCE PATIENT CARE ENCOUNTER

DESCRIPTION: This option allows for the add/edit/deleting of information on certain

> encounters that most users should not be changing and the other PCE

> options will not allow to be changed. This option also does not conditionally not ask some fields, i.e. it always asks all of the fields. In addition this option allows users to document a clinical encounter in the V-files (visit related files), and can also delete any V-File encounter entries, even though they are not the creator of the entries. The data entered via this option includes visit information (where and when), and the following clinical data related to the visit: providers of care, problems treated, procedures and treatments done, and immunizations, skin tests, and patient education given.

> This option is intended for the Coordinator for PCE and/or supervisor of the encounter data entry staff.

Short Menu Text: SUP EXIT ACTION: K SDSCEDIT

ENTRY ACTION: S SDSCEDIT=1 D EN^PXCE("S")

> Setting variable SDSCEDIT=1 allows for the edit of the automated question “Was treatment for SC Condition?”.

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols were exported with the ASCD project.

### SDSC ACCEPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ITEM TEXT: Retain SvcConnected Status

TYPE: action PACKAGE: SCHEDULING

ENTRY ACTION: D ACC^SDSCLST

### SDSC CHANGE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ITEM TEXT: Modify SvcConnected Status

TYPE: action PACKAGE: SCHEDULING

ENTRY ACTION: D EDT^SDSCLST

### SDSC DETAIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ITEM TEXT: Review Encounter

TYPE: action PACKAGE: SCHEDULING

ENTRY ACTION: D SEL^SDSCLST

### SDSC MENU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE: menu PACKAGE: SCHEDULING

ITEM: SDSC DETAIL

SCREEN: I \$G(VALMCNT)

### SDSC RECORD MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ITEM TEXT: Edit Detail Record Menu

TYPE: menu PACKAGE: SCHEDULING

ITEM: SDSC ACCEPT

> SDSC CHANGE

> SDSC SEND

### SDSC SEND 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ITEM TEXT: Flag for Clinical Review

TYPE: action PACKAGE: SCHEDULING

ENTRY ACTION: D REV^SDSCLST

## Exported List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list templates were exported with the ASCD project.

### SDSC DETAIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80 TOP MARGIN: 2

BOTTOM MARGIN: 18 OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES PROTOCOL MENU: SDSC RECORD MENU

SCREEN TITLE: Encounter Detail ALLOWABLE NUMBER OF ACTIONS: 1

AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN

ACTIONS

ARRAY NAME: ^TMP("SDSCLST",\$J) EXIT CODE: D EXIT^SDSCLM1

HEADER CODE: D HDR^SDSCLM1 HELP CODE: D HELP^SDSCLM1

ENTRY CODE: D INIT^SDSCLM1

### SDSC REVIEW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80 TOP MARGIN: 6

BOTTOM MARGIN: 18 OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES PROTOCOL MENU: SDSC MENU

SCREEN TITLE: ASCD ALLOWABLE NUMBER OF ACTIONS: 1

> AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN

> ACTIONS

ITEM NAME: ENCDT COLUMN: 19

WIDTH: 16 DISPLAY TEXT: Enc Date/Time

ITEM NAME: ENCNO COLUMN: 8

WIDTH: 10 DISPLAY TEXT: Encounter \#

ITEM NAME: PAT COLUMN: 37

WIDTH: 32 DISPLAY TEXT: Patient

ITEM NAME: STAT COLUMN: 71

WIDTH: 9 DISPLAY TEXT: Status

ITEM NAME: LINENUM COLUMN: 1

WIDTH: 6

EXIT CODE: D EXIT^SDSCLM HEADER CODE: D HDR^SDSCLM

HELP CODE: D HELP^SDSCLM ENTRY CODE: D INIT^SDSCLM

## Exported Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following parameter definition was exported with the ASCD project.

### SDSC SITE PARAMETER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: SDSC SITE PARAMETER

MULTIPLE VALUED: No INSTANCE TERM: CHECK DAYS

VALUE TERM: DAYS VALUE DATA TYPE: numeric

VALUE HELP: Enter a number between 1-99999.

VALUE VALIDATION CODE: K:(X\<1)!(X\>99999) X

INSTANCE DATA TYPE: numeric

INSTANCE HELP: Enter a number between 1-99999.

INSTANCE VALIDATION CODE: K:(X\<1)!(X\>99999) X

PRECEDENCE: 1 ENTITY FILE: DIVISION

## Exported Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following mail group was exported with the ASCD project.

### SDSC NIGHTLY TALLY 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TYPE: public

ALLOW SELF ENROLLMENT?: NO

> DESCRIPTION: This mail group is for ASCD (Automated Service Connected Designation) software. A breakdown of records reviewed during the nightly process will be sent to this mail group.

## ## Exported Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys were exported with the ASCD project.

### SDSC CLINICAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DESCRIPTIVE NAME: SC Clinical User

> DESCRIPTION: This key should be assigned to any clinical reviewer of encounters that are part of the Automated Service Connected Designation (ASCD) system.

### SDSC SUPER 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DESCRIPTIVE NAME: SC Supervisor

> DESCRIPTION: This key should be assigned to a supervisor reviewer of encounters that are part of the Automated Service Connected Designation (ASCD) system.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving currently defined for this package.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, encounters are deleted from the OUTPATIENT ENCOUNTER File (#409.68). However, when the encounter is deleted from file \#409.68 it is not removed from the SDSC SERVICE CONNECTED CHANGES File (#409.48) automatically. The SDSC NIGHTLY COMPILE option runs a purge utility that removes encounters from the ASCD file (#409.48) if the encounter has been deleted from the Outpatient Encounter File (#409.68). A MailMan message is also sent to the mail group SDSC NIGHTLY TALLY showing how many encounters were purged.

The ‘Encounters with No Action Taken’ section lists the visit date/time, patient name, and ASCD status.

The ‘Encounters with Actions Taken’ section lists the visit date/time, patient name, and ASCD status as well as detail lines concerning each user who took some action on the encounter, the date the action was taken and the action.

Subj: ASCD PURGE REPORT \[#8675\] 10/03/06@17:59 13 lines

From: ASCD PURGE CHECK In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Encounters with No Action Taken: 1

JAN 14, 2006@13:15-PATIENT,ONE M-NEW

Encounters with Actions Taken: 3

JAN 06, 2006@14:30-PATIENT,TWO L-COMPLETED

USER,ONE-JAN 09, 2006-USER-REVIEW

USER,SUPERVISOR-JAN 09, 2005-SUPERVISOR-SC CHNG

SEP 14, 2006@10:30-PATIENT,THREE N-COMPLETED

USER,KONE-OCT 03, 2006-USER-REVIEW

USER,SUPERVISOR-OCT 03, 2006-SUPERVISOR-SC KEPT

USER,SUPERVISOR L-OCT 03, 2006-SUPERVISOR-SC CHNG

AUG 28, 2005@04:47-PATIENT,FOUR F-COMPLETED

USER,TWO-OCT 03, 2005-USER-REVIEW

USER,SUPERVISOR-OCT 03, 2005-SUPERVISOR-SC CHNG

Enter message action (in IN basket): Ignore//

# Callable Routines/Entry Points/Application Programmer Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains a list of callable routines, entry points and application program interfaces used by the ASCD project.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines listed below are called by ASCD software. A brief functional summary is provided for each.

\$\$BIL^DGMTUB Determine if patient is pending adjudication or category C and has agreed to pay the deductible.

RDIS^DGRPDB Returns patient rated disabilities.

^DGSEC Patient security look-up.

\$\$INSUR^IBBAPI Checks if patient is insured.

\$\$CT^IBRSUTL Return claims tracking record for outpatient encounter.

\$\$FIRST^IBRSUTL Checks if an outpatient encounter is billable for first party,

\$\$FPBILL^IBRSUTL Return first party bill number for an outpatient encounter.

\$\$RNBU^IBRSUTL Update claims tracking record reason not billable for an outpatient encounter.

\$\$THIRD^IBRSUTL Checks if an outpatient encounter is billable for third party.

\$\$TPBILL^IBRSUTL Returns a list of third party bill numbers for an outpatient encounter.

\$\$TPCHG^IBRSUTL Return outpatient encounters third party charges, based on encounters procedures.

\$\$ICDDX^ICDCODE Returns ICD9 code information.

\$\$CPT^ICPTCOD Returns basic info on CPT/HCPCS code.

\$\$GETDATA^PRCAAPI Returns AR bill information.

\$\$INTV^PXAPI Prompts a user for visit and related data.

\$\$PRIMVPRV^PXUTL1 Returns a visit primary provider.

\$\$CLINIC^SDAMU Check Hospital Location file (#44) for non-count clinic and occasion of service.

CLOE^SDCO21 Set-up Classification Array for Outpatient Encounter.

GETCPT^SDOE Gets encounter/visit procedure codes.

\$\$GETDX^SDOE Gets encounter/visit diagnosis codes.

\$\$GETOE^SDOE Gets the zero node from the Outpatient Encounter file (#409.68).

GETPDX^SDOERPC Get primary diagnosis code for an encounter.

^SDVER Display the version of the Scheduling package.

\$\$FMADD^XLFDT Adds a number to a FileMan date

\$\$FMTE^XLFDT Converts Filename date to an external date.

\$\$HTE^XLFDT Converts a \$H value to an external date.

\$\$UP^XLFSTR Converts a string to uppercase.

^XMD Used to generate bulletins.

\$\$GET^XPAR Returns a parameter value.

EDIT^XPAREDIT Allows for editing a value in the Parameter file.

\$\$KCHK^XUSRB Checks if a user has a particular key.

\$\$NAME^XUSER Returns the full name from the NEW PERSON file (#200).

ELIG^VADPT Gets patient eligibility information.

DEM^VADPT Gets patient demographic information.

KVA^VADPT Kills patient variables.

ADM^VADPT2 Gets patient admission information.

\$\$PRIM^VASITE Returns medical center division of primary medical center division.

\$\$SITE^VASITE Returns the institution and station number.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The section provides a list of external relationships required between the ASCD software and other packages.

## Minimum Package Requirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At a minimum ASCD will require the packages listed below. Sites should verify that all patches for these packages have been installed.

> DVB V. 4.0

> IB V. 2.0

> ICD V. 18.0

> ICPT V.6.0

> Kernel V. 8.0

> Kernel Toolkit V. 7.3

> PCE V. 1.0

> PRCA V. 4.5

> SD V. 5.3

> VA FileMan V. 22.0

> VA MailMan V. 7.1

## DBIAs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following DBIAs exist between the ASCD software and the other packages.

DBIA427 Grants permission to read ^DIC(8,D0,0.

> DBIA643 Determine if a patient was Category C on a specified date. Calls API \$\$BIL^DGMTUB.

DBIA733 Grants access to disability codes and associated ICD9 codes.

> DBIA767 This DBIA allows access to the DG SECURITY LOG file to determine whether a patient is considered sensitive. Needed so as to read the 2nd piece of the 0 node in global ^DGSL(38.1.

> DBIA2028 Grants access to read PCE global ^AUPNVSIT(.

> DBIA2295 Grants direct global read to file \#40.8. Reads field .01.

> DBIA2315 Grants access to read the Visit VPOV file ^AUPNVPOV.

> DBIA2336 Part of the Parameter Tools component of Toolkit. Call made to allow access to EDIT^XPAREDIT.

> DBIA2343 Returns the full name of the specified user in a mixed case displayable format. Calls \$\$NAME^XUSER.

> DBIA2602 Reads the Audit file \#1.1. Access to the “C” x-reference and fields 1, .03, 2 and 3. Need to order through ^DIA for a date range to determine new insurance.

> DBIA2992 Provides access to read file 8989.51.

> DBIA3857 Performs patient sensitivity/security check. Call made to routine ^DGSEC.

> DBIA3990 Retrieves ICD code related data. Call made to \$\$ICDDX^ICDCODE.

> DBIA4370 Returns accounts receivable billing data in support of the Recovery Cost Report. Call made to \$\$GETDATA^PRCAAPI.

> DBIA4419 Return insurance data. Call made to \$\$INSUR^IBBAPI.

> DBIA4807 Returns patient rated disabilities from file \#2.

DBIA4987 Billing APIs to support encounter billing. Grants access to IB data. Call made to \$\$CT^IBRSUTL, \$\$RNBU^IBRSUTL, \$\$TPCHG^IBRSUTL and \$\$TPBILL^IBRSUTL.

DBIA4990 ASCD APIs to support service connected automation.

DBIA4991 Returns a visit primary provider. Call made to \$\$PRIMVPRV^PXUTL1.

> DBIA10061 Grants access to patient demographic data in file \#2. Calls DEM^VADPT.

> DBIA10070 Create, address, and send a message. Calls routine ^XMD.

> DBIA10076 Provides supported read access to global ^XUSEC. Used to determine whether a user has a specific key.

DBIA10104 Kernel support functions. Calls \$\$UP^XLFSTR to convert to uppercase.

DBIA10112 Provides institution and station number data. Calls \$\$SITE^VASITE.

DBIA10142 Used to write a line. Calls routine EN^DDIOL.

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any ASCD option in File 19 which is a menu option should be able to run independently provided the user has the appropriate keys and FileMan access.

# Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASCD software does not make use of any global variables.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of acronyms/definitions related to the ASCD software.

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term     | Definition                                                         |
|----------|--------------------------------------------------------------------|
| AO       | Agent Orange                                                       |
| ASCD     | Automated Service Connected Designation                            |
| CPRS     | Computerized Patient Record System                                 |
| CPT      | Current Procedural Terminology                                     |
| EPS      | Enterprise Product Support                                         |
| HINQ     | Hospital Inquiry                                                   |
| HIPAA    | Health Insurance Portability and Accountability Act                |
| HSD&D    | Health Systems Design & Development                                |
| ICD      | International Classification of Diseases                           |
| ICD-9-CM | International Classification of Diseases Clinical Modification V.9 |
| NPCD     | National Patient Care Database                                     |
| NSC      | Non-Service Connected                                              |
| PCE      | Patient Care Encounter                                             |
| SC       | Service Connected                                                  |
| VA       | Department of Veterans Affairs                                     |
| VBA      | Veterans Benefits Administration                                   |
| VHA      | Veterans Health Administration                                     |
| VISN     | Veterans Integrated Service Network                                |
| VistA    | Veterans Health Information Systems and Technology Architecture    |

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRS</td>
<td><p>CPRS is the patient’s electronic medical record. It is a compilation of</p>
<p>information entered directly into CPRS and information gathered from</p>
<p>ancillary services, including but not limited to, orders, progress notes,</p>
<p>discharge summaries, medications, problems, imaging impressions, and</p>
<p>laboratory results.</p></td>
</tr>
<tr class="even">
<td>Encounter</td>
<td><p>A contact between a patient and a provider who has primary responsibility for</p>
<p>assessing and treating the patient at a given contact, exercising independent</p>
<p>judgment. A patient may have multiple encounters per visit. Outpatient</p>
<p>encounters include scheduled appointments and walk-in unscheduled visits.</p>
<p>A clinician’s telephone communications with a patient may be represented by</p>
<p>a separate visit entry. If the patient is seen in an outpatient clinic while an</p>
<p>inpatient, this is treated as a separate encounter.</p></td>
</tr>
<tr class="odd">
<td>Enterprise Product Support</td>
<td>Enterprise Product Support is the central agency responsible for distributing <strong>V</strong>ist<strong>A</strong> software patches nationally.</td>
</tr>
<tr class="even">
<td><p>National Patient</p>
<p>Care Database</p>
<p>(NPCD)</p></td>
<td><p>The National Patient Care Database is maintained in Austin and receives</p>
<p>selected demographic and encounter-based clinical and diagnostic data from</p>
<p>VAMCs. This data enables a detailed analysis of VHA inpatient and</p>
<p>outpatient health care activity.</p></td>
</tr>
<tr class="odd">
<td>Non-Count Clinic</td>
<td>A clinic whose visits do not affect AMIS statistics.</td>
</tr>
<tr class="even">
<td>PCE</td>
<td><p>PCE is a <strong>V</strong>ist<strong>A</strong> program that is part of the Ambulatory Data Capture Project</p>
<p>(ADCP) and provides clinical reminders, which appear on Health Summaries.</p>
<p>PCE helps sites collect, manage and display outpatient encounter data</p>
<p>(including providers, procedure codes, and diagnostic codes) in compliance</p>
<p>with the 10/1/96 Ambulatory Care Data Capture mandate from the</p>
<p>Undersecretary of Health. It helps sites document patient education,</p>
<p>examinations, treatments, skin tests, and immunizations, and collect and</p>
<p>manage other clinically significant data, such as defining Health Factors and</p>
<p>Health Maintenance reminders.</p></td>
</tr>
<tr class="odd">
<td>Provider</td>
<td>The entity which furnishes health care to a consumer. This definition includes an individual or defined group of individuals who provide a defined unit of health care services (defined=codable) to one or more individuals at a single session.</td>
</tr>
<tr class="even">
<td>Requirements</td>
<td>User needs that trigger the development of a program, system, or project. Requirements may be business, functional, and/or system needs. They are documented in detail in the Software Requirements Specifications (SRS) document.</td>
</tr>
<tr class="odd">
<td>Stakeholders</td>
<td>Individuals and organizations that are actively involved in the project, or whose interests may be positively or negatively affected as a result of project execution or project completion. They may also exert influence over the project and its results.</td>
</tr>
<tr class="even">
<td>Software Requirement Specifications</td>
<td>Document that outlines the functionality requirements for a project.</td>
</tr>
<tr class="odd">
<td>Stop Code</td>
<td>A three digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit. Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.</td>
</tr>
<tr class="even">
<td>Veterans Health Information System and Technology Architecture (VistA)</td>
<td><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture, formerly known as Decentralized Hospital Computer Program (DHCP), encompasses the complete information environment at VA medical facilities.</td>
</tr>
</tbody>
</table>

# How to Obtain Technical Information Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure ASCD documentation. On-line technical documentation pertaining to the ASCD software, in addition to that which is located in the help prompts and on the help screens which are found throughout the package, may be generated through utilization of KERNEL options. These include but are not limited to: XINDEX, Menu Management, Inquire Option File, Print Option File, and FileMan List File Attributes.

Automated SC Designation Draft IAB:

> <http://tspr.vista.med.va.gov/warboard/ProjectDocs/Automated_Service_Connection/Automated_SC_Designation_Draft_IAB_2005070510145.doc>

> ASCD Release Notes:

> <https://www.va.gov/vdl/>

> ASCD Technical Manual:

> <https://www.va.gov/vdl/>

> ASCD User Manual:

> <https://www.va.gov/vdl/>

> <u>ASCD Patches</u>

> SD\*5.3\*495, PX\*1.0\*184 and DVB\*4.0\*58.

> <u>ASCD Associated Patches</u>

> IB\*2.0\*369 and PRCA\*4.5\*250.

# Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASCD uses SDSC as its namespace. The routines are exported via a host file

## Traditional Style Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AC REGULAR

Field: DATE LAST EDITED (409.48,.02)

> Description: This cross reference is by DATE LAST EDITED and is used for several reports that track changes the user made to the encounter.

1)= S ^SDSC(409.48,"AC",\$E(X,1,30),DA)=""

2)= K ^SDSC(409.48,"AC",\$E(X,1,30),DA)

AD REGULAR

Field: DATE CREATED (409.48,.04)

> Description: This cross reference is by DATE CREATED and is used for several reports that track what happened when an encounter was added to this file.

> 1)= S ^SDSC(409.48,"AD",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"AD",\$E(X,1,30),DA)

AE REGULAR

Field: DATE OF ENCOUNTER (409.48,.07)

> Description: This cross reference is by DATE OF ENCOUNTER and is used by several reports.

1)= S ^SDSC(409.48,"AE",\$E(X,1,30),DA)=""

2)= K ^SDSC(409.48,"AE",\$E(X,1,30),DA)

B REGULAR

Field: OUTPATIENT ENCOUNTER (409.48,.01)

1)= S ^SDSC(409.48,"B",\$E(X,1,30),DA)=""

2)= K ^SDSC(409.48,"B",\$E(X,1,30),DA)

D REGULAR

Field: PATIENT (409.48,.11)

Description: Patient IEN cross-reference

1)= S ^SDSC(409.48,"D",\$E(X,1,30),DA)=""

2)= K ^SDSC(409.48,"D",\$E(X,1,30),DA)

TRIGGER

Field: SERV. CONNECT (OK BY USER?) (409.48,.06)

Triggered Field: STATUS (409.48,.05)

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,5),X=X S DIU=X K Y S X=DIV S X="C" S DIH=\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,5)=DIV,DIH=409.48,DIG=.05 D ^DICR

2)= Q

CREATE VALUE)= "C"

DELETE VALUE)= NO EFFECT

FIELD)= \#.05

Sub-File \#409.481 - Traditional Cross-References:

B REGULAR

Field: EDIT NUMBER (409.481,.01)

1)= S ^SDSC(409.48,DA(1),1,"B",\$E(X,1,30),DA)=""

2)= K ^SDSC(409.48,DA(1),1,"B",\$E(X,1,30),DA)

TRIGGER

Field: DATE EDITED (409.481,.02)

Triggered Field: DATE LAST EDITED (409.48,.02)

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,2),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P (^(0),U,2)=DIV,DIH=409.48,DIG=.02 D ^DICR

2)= Q

CREATE VALUE)= S X=X

DELETE VALUE)= NO EFFECT

FIELD)= \#.02

TRIGGER

Field: EDITED BY (409.481,.03)

> Triggered Field: LAST EDITED BY (409.48,.03)

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,3),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P (^(0),U,3)=DIV,DIH=409.48,DIG=.03 D ^DICR

2)= Q

CREATE VALUE)= S X=X

DELETE VALUE)= NO EFFECT

FIELD)= \#.03

TRIGGER

Field: SERV. CONNECT (OK BY USER?) (409.481,.05)

Triggered Field: SERV. CONNECT (OK BY USER?) (409.48,.06)

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,6),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P (^(0),U,6)=DIV,DIH=409.48,DIG=.06 D ^DICR

> 2)= Q

CREATE VALUE)= S X=X

DELETE VALUE)= NO EFFECT

FIELD)= \#.06

TRIGGER

Field: REVIEW REQUIRED? (409.481,.06)

Triggered Field: STATUS (409.48,.05)

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,5),X=X S DIU=X K Y S X=DIV S X="R" S DIH=\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,5)=DIV,DIH=409.48,DIG=.05 D ^DICR

> 2)= Q

> CREATE VALUE)= "R"

DELETE VALUE)= NO EFFECT

FIELD)= \#.05

## New Style Cross-reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AF (#699) RECORD REGULAR IR SORTING ONLY

Short Descr: Cross reference by PROVIDER and DATE OF ENCOUNTER

> Description: This cross reference (by PROVIDER and DATE OF ENCOUNTER) is used by a report of the providers who have had encounters reviewed through the ASCD options.

> Set Logic: S ^SDSC(409.48,"AF",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"AF",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"AF")

> X(1): PRIMARY PROVIDER (409.48,.08) (Subscr 1) (forwards)

> X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

AG (#700) RECORD REGULAR IR SORTING ONLY

Short Descr: Cross reference by LAST EDITED BY and DATE OF ENCOUNTER

> Description: This cross reference (by LAST EDITED BY and DATE OF ENCOUNTER) is used by a report of the users who reviewed encounters and what they did to each through the ASCD options.

Set Logic: S ^SDSC(409.48,"AG",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"AG",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"AG")

> X(1): LAST EDITED BY (409.48,.03) (Subscr 1) (forwards)

> X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

C (#701) RECORD REGULAR IR LOOKUP & SORTING

Short Descr: Cross Reference by STATUS and DATE OF ENCOUNTER

> Description: This cross reference (by STATUS and DATE OF ENCOUNTER) is used by a summary report of the status of encounters found on a particular day and also by a loop that runs through the NEW or REVIEW statuses for a date range.

Set Logic: S ^SDSC(409.48,"C",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"C",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"C")

X(1): STATUS (409.48,.05) (Subscr 1) (forwards)

X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

# Appendix A – Data Dictionary List of file \#409.48

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STANDARD DATA DICTIONARY \#409.48 -- SDSC SERVICE CONNECTED CHANGES FILE

MAR 19,2007@12:58:45 PAGE 1

STORED IN ^SDSC(409.48, (51 ENTRIES) SITE: <span class="mark">YOUR SITE</span> UCI: DEVVJJ,DEVVJJ

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This file contains a list of encounters which were selected for review based on

a comparison of the ICD9 diagnosis codes from the encounter and the VBA rated

disabilities (VA) codes from the patient. Entries will be edited as necessary

per the review criteria established for determining if an encounter is

service-connected (SC) or non-service connected (NSC).

DD ACCESS: @

RD ACCESS: @

WR ACCESS: @

DEL ACCESS: @

LAYGO ACCESS: @

AUDIT ACCESS: @

(NOTE: Kernel's File Access Security has been installed in this UCI.)

CROSS

REFERENCED BY: DATE LAST EDITED(AC), DATE CREATED(AD), DATE OF ENCOUNTER(AE), OUTPATIENT ENCOUNTER(B), PATIENT(D)

INDEXED BY: PRIMARY PROVIDER & DATE OF ENCOUNTER (AF), LAST EDITED BY & DATE OF ENCOUNTER (AG), STATUS & DATE OF ENCOUNTER (C)

409.48,.01 OUTPATIENT ENCOUNTER 0;1 POINTER TO OUTPATIENT ENCOUNTER FILE (#409.68) (Required)

INPUT TRANSFORM: S DINUM=X

LAST EDITED: MAR 05, 2007

DESCRIPTION: This is the Encounter Number from file \#409.68

(Outpatient Encounter) which was determined needs to be reviewed.

TECHNICAL DESCR: A pointer to the OUTPATIENT ENCOUNTER File \#409.68.

> NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 409.48^B

1)= S ^SDSC(409.48,"B",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"B",\$E(X,1,30),DA)

409.48,.02 DATE LAST EDITED 0;2 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

> LAST EDITED: SEP 16, 2004

> DESCRIPTION: This field contains the date that this encounter was last edited through the ASCD options.

> NOTES: TRIGGERED by the DATE EDITED field of the TRACK EDITS sub-field of the SDSC SERVICE CONNECTED CHANGES File

CROSS-REFERENCE: 409.48^AC

> 1)= S ^SDSC(409.48,"AC",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"AC",\$E(X,1,30),DA)

> This cross reference is by DATE LAST EDITED and is used for several reports that track changes the user made to the encounter.

409.48,.03 LAST EDITED BY 0;3 POINTER TO NEW PERSON FILE (#200)

> LAST EDITED: SEP 22, 2004

> DESCRIPTION: This field contains the user who last edited this encounter through the ASCD options.

> TECHNICAL DESCR: A pointer to the NEW PERSON File \#200.

NOTES: TRIGGERED by the EDITED BY field of the TRACK EDITS sub-field of the SDSC SERVICE CONNECTED CHANGES File

RECORD INDEXES: AG (#700)

409.48,.04 DATE CREATED 0;4 DATE (Required)

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: SEP 23, 2004

> DESCRIPTION: This field contains the date that this encounter was added to this file.

CROSS-REFERENCE: 409.48^AD

> 1)= S ^SDSC(409.48,"AD",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"AD",\$E(X,1,30),DA)

> This cross reference is by DATE CREATED and is used for several reports that track what happened when an encounter was added to this file.

409.48,.05 STATUS 0;5 SET (Required)

> 'N' FOR NEW;

> 'R' FOR REVIEW;

> 'C' FOR COMPLETED;

> LAST EDITED: SEP 23, 2004

> DESCRIPTION: This field contains the status of this encounter.

> "NEW" - this encounter was recently added to this file.

> "REVIEW" - this encounter was forwarded for clinical review.

> "COMPLETED" - edits to this encounter are complete and only a supervisor may make further modifications.

NOTES: TRIGGERED by the SERV. CONNECT (OK BY USER?) field of the SDSC SERVICE CONNECTED CHANGES File

> TRIGGERED by the REVIEW REQUIRED? field of the TRACK EDITS sub-field of the SDSC SERVICE CONNECTED CHANGES File

RECORD INDEXES: C (#701)

409.48,.06 SERV. CONNECT (OK BY USER?) 0;6 SET

'0' FOR NO;

> '1' FOR YES;

> LAST EDITED: SEP 22, 2004

> DESCRIPTION: This field will contain 1 ('YES') or 0 ('NO') based on the user determination of the encounter's service connected value.

> NOTES: TRIGGERED by the SERV. CONNECT (OK BY USER?) field of the TRACK EDITS sub-field of the SDSC SERVICE CONNECTED CHANGES File

CROSS-REFERENCE: ^^TRIGGER^409.48^.05

> 1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$S(\$D( ^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,5) ,X=X S DIU=X K Y S X=DIV S X="C" S DIH=\$G(^SDSC (409.48,DIV(0),0)),DIV=X S \$P(^(0),U,5)=DIV,DIH

=409.48,DIG=.05 D ^DICR

> 2)= Q

> CREATE VALUE)= "C"

> DELETE VALUE)= NO EFFECT

> FIELD)= \#.05

409.48,.07 DATE OF ENCOUNTER 0;7 DATE

INPUT TRANSFORM: S %DT="ESTX" D ^%DT S X=Y K:Y\<1 X

> LAST EDITED: SEP 23, 2004

> DESCRIPTION: This is the actual date of the encounter copied from the OUTPATIENT ENCOUNTER file \#409.68 at the time of the compile.

CROSS-REFERENCE: 409.48^AE

> 1)= S ^SDSC(409.48,"AE",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"AE",\$E(X,1,30),DA)

This cross reference is by DATE OF ENCOUNTER and is used by several reports.

RECORD INDEXES: AF (#699), AG (#700), C (#701)

409.48,.08 PRIMARY PROVIDER 0;8 POINTER TO NEW PERSON FILE (#200)

LAST EDITED: SEP 22, 2004

> DESCRIPTION: This field contains the primary provider for the encounter determined at the time of the compile.

TECHNICAL DESCR: A pointer to the NEW PERSON FILE \#200.

> RECORD INDEXES: AF (#699)

409.48,.09 SERV. CONNECT (OK BY VBA/ICD?) 0;9 SET

> '0' FOR NO

> '1' FOR YES;

LAST EDITED: MAR 05, 2007

> DESCRIPTION: This field will contain 1 ('YES') or 0 ('NO') depending on whether the automation or compile determined that the VBA/ICD codes found for this patient and encounter provided a match.

409.48,.1 CLAIMS TRACKING ENTRY 0;10 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>99999999999)!(X\<1)!(X?.E1"."1N.N) X

LAST EDITED: MAR 05, 2007

> HELP-PROMPT: Type a Number between 1 and 99999999999, 0 Decimal Digits

> DESCRIPTION: This field will contain the Claims Tracking Entry for a record which may have been modified.

TECHNICAL DESCR: Contains the pointer value to the CLAIMS TRACKING file \#356.

409.48,.11 PATIENT 0;11 POINTER TO 2447 FILE (#2) (Required)

LAST EDITED: MAR 02, 2007

> DESCRIPTION: This field contains the patient's DFN for the encounter.

TECHNICAL DESCR: A pointer to the PATIENT file \#2.

CROSS-REFERENCE: 409.48^D

> 1)= S ^SDSC(409.48,"D",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,"D",\$E(X,1,30),DA)

> Patient IEN cross-reference

409.48,.12 DIVISION 0;12 POINTER TO MEDICAL CENTER DIVISION FILE (#40.8)

LAST EDITED: AUG 11, 2005

> DESCRIPTION: This field is the medical center division assigned to the encounter.

TECHNICAL DESCR: A pointer to the MEDICAL CENTER DIVISION File \#40.8.

409.48,.13 SERV. CONNECT (ORIGINAL VALUE) 0;13 SET

> '0' FOR NO;

> '1' FOR YES;

> LAST EDITED: MAR 08, 2007

> DESCRIPTION: This field will contain 1 ('YES') or 0 ('NO') based on the original encounter's service connected value.

409.48,1 TRACK EDITS 1;0 Multiple \#409.481

> (Add New Entry without Asking)

> DESCRIPTION: This multiple field tracks each edit made to this encounter through the ASCD options.

409.481,.01 EDIT NUMBER 0;1 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>99)!(X\<1)!(X?.E1"."1N.N) X

LAST EDITED: NOV 07, 2006

> HELP-PROMPT: Type a Number between 1 and 99, 0 Decimal Digits

> DESCRIPTION: This field contains a unique entry for each edit. The edits are stored in order beginning at 1. Under ordinary circumstances there will usually only be between 1 and 3 edits for any record although there is no specific maximum.

CROSS-REFERENCE: 409.481^B

> 1)= S ^SDSC(409.48,DA(1),1,"B",\$E(X,1,30),DA)=""

> 2)= K ^SDSC(409.48,DA(1),1,"B",\$E(X,1,30),DA)

409.481,.02 DATE EDITED 0;2 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

> LAST EDITED: NOV 07, 2006

> DESCRIPTION: This is the date that the user edited this encounter. A trigger on this field will also update the DATE LAST EDITED field in the main file.

CROSS-REFERENCE: ^^TRIGGER^409.48^.02

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y( 1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P( Y(1),U,2),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$ G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,2)= DIV,DIH=409.48,DIG=.02 D ^DICR

2)= Q

> CREATE VALUE)= S X=X

> DELETE VALUE)= NO EFFECT

> FIELD)= \#.02

409.481,.03 EDITED BY 0;3 POINTER TO NEW PERSON FILE (#200)

LAST EDITED: NOV 07, 2006

> DESCRIPTION: This is the user who edited this encounter. A trigger on this field will also update the LAST EDITED BY field in the main file.

TECHNICAL DESCR: A pointer to the NEW PERSON file \#200.

CROSS-REFERENCE: ^^TRIGGER^409.48^.03

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,3),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$ G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,3)=DIV,DIH=409.48,DIG=.03 D ^DICR

2)= Q

> CREATE VALUE)= S X=X

> DELETE VALUE)= NO EFFECT

409.481,.04 TYPE OF ENTRY 0;4 SET

> 'U' FOR USER;

> 'C' FOR CLINICAL;

> 'S' FOR SUPERVISOR;

LAST EDITED: NOV 07, 2006

> DESCRIPTION: This is the type of user who edited this encounter. "USER" any standard user of this package.

> "CLINICAL" a clinical reviewer with the appropriate security key.

> "SUPERVISOR" a supervisor with the appropriate security key.

409.481,.05 SERV. CONNECT (OK BY USER?) 0;5 SET

> '0' FOR NO;

> '1' FOR YES;

LAST EDITED: DEC 08, 2006

> DESCRIPTION: This field will contain 1 ('YES') or 0 ('NO') based on the user determination of the encounter's service connected value. A trigger on this field will also update the SERV. CONNECT (OK BY USER?) field in the main file.

CROSS-REFERENCE: ^^TRIGGER^409.48^.06

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y( 1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P(Y(1),U,6),X=X S DIU=X K Y S X=DIV S X=X S DIH=\$ G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,6)=DIV,DIH=409.48,DIG=.06 D ^DICR

2)= Q

> CREATE VALUE)= S X=X

> DELETE VALUE)= NO EFFECT

> FIELD)= \#.06

409.481,.06 REVIEW REQUIRED? 0;6 SET

> '0' FOR NO;

> '1' FOR YES;

LAST EDITED: DEC 08, 2006

> DESCRIPTION: This field will be set to 1 ('YES') if a regular user determines that this record requires further review by a clinical reviewer. A trigger will also set the STATUS field in the main file to 'REVIEW'.

CROSS-REFERENCE: ^^TRIGGER^409.48^.05

> 1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA S Y(1)=\$S(\$D(^SDSC(409.48,D0,0)):^(0),1:"") S X=\$P( Y(1),U,5),X=X S DIU=X K Y S X=DIV S X="R" S DIH =\$G(^SDSC(409.48,DIV(0),0)),DIV=X S \$P(^(0),U,5 )=DIV,DIH=409.48,DIG=.05 D ^DICR

> 2)= Q

> CREATE VALUE)= "R"

> DELETE VALUE)= NO EFFECT

> FIELD)= \#.05

FILES POINTED TO FIELDS

2447 (#2) PATIENT (#.11)

MEDICAL CENTER DIVISION (#40.8) DIVISION (#.12)

NEW PERSON (#200) LAST EDITED BY (#.03)

> PRIMARY PROVIDER (#.08)

> TRACK EDITS:EDITED BY (#.03)

OUTPATIENT ENCOUNTER (#409.68) OUTPATIENT ENCOUNTER (#.01)

SDSC SERVICE CONNECTED CHANGES

> (#409.48) TRACK EDITS:DATE EDITED (#.02)

> EDITED BY (#.03)

> SERV. CONNECT (OK BY USER?) (#.05)

> REVIEW REQUIRED? (#.06)

INDEX AND CROSS-REFERENCE LIST -- FILE \#409.48

File \#409.48

Record Indexes:

AF (#699) RECORD REGULAR IR SORTING ONLY

Short Descr: Cross reference by PROVIDER and DATE OF ENCOUNTER

> Description: This cross reference (by PROVIDER and DATE OF ENCOUNTER) is used by a report of the providers who have had encounters reviewed through the ASCD options.

Set Logic: S ^SDSC(409.48,"AF",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"AF",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"AF")

X(1): PRIMARY PROVIDER (409.48,.08) (Subscr 1) (forwards)

X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

AG (#700) RECORD REGULAR IR SORTING ONLY

Short Descr: Cross reference by LAST EDITED BY and DATE OF ENCOUNTER

> Description: This cross reference (by LAST EDITED BY and DATE OF ENCOUNTER) is used by a report of the users who reviewed encounters and what they did to each through the ASCD options.

Set Logic: S ^SDSC(409.48,"AG",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"AG",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"AG")

X(1): LAST EDITED BY (409.48,.03) (Subscr 1) (forwards)

X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

C (#701) RECORD REGULAR IR LOOKUP & SORTING

Short Descr: Cross Reference by STATUS and DATE OF ENCOUNTER

> Description: This cross reference (by STATUS and DATE OF ENCOUNTER) is used by a summary report of the status of encounters found on a particular day and also by a loop that runs through the NEW or REVIEW statuses for a date range.

Set Logic: S ^SDSC(409.48,"C",X(1),X(2),DA)=""

Kill Logic: K ^SDSC(409.48,"C",X(1),X(2),DA)

Whole Kill: K ^SDSC(409.48,"C")

X(1): STATUS (409.48,.05) (Subscr 1) (forwards)

X(2): DATE OF ENCOUNTER (409.48,.07) (Subscr 2) (forwards)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

# Appendix B – Data Dictionary List of file \#31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STANDARD DATA DICTIONARY \#31 -- DISABILITY CONDITION FILE

OCT 9,2007@12:14:01 PAGE 1

STORED IN ^DIC(31, (1037 ENTRIES) SITE: <span class="mark">YOUR SITE</span> UCI: DEVVJJ,DEVVJJ (VERSION 4.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This file contains the VA recognized Disability conditions as used when rating

for compensation/pension.

(NOTE: Kernel's File Access Security has been installed in this UCI.)

IDENTIFIED BY: DX CODE (#2)

POINTED TO BY: RATED DISABILITIES (VA) field (#.01) of the RATED DISABILITIES

(VA) sub-field (#2.04) of the 2447 File (#2)

\*RELATED DISABILITIES field (#.01) of the \*RELATED DISABILITIES

sub-field (#396.61) of the AMIE EXAM File (#396.6)

\*RELATED DISABILITIES field (#.01) of the \*RELATED DISABILITIES

sub-field (#396.701) of the 2507 BODY SYSTEM File (#396.7)

CORRESPONDING MAS DISABILITY field (#.01) of the CORRESPONDING

MAS DISABILITY sub-field (#662.06) of the PROS DISABILITY

CODE File (#662)

ENTRY field (#.02) of the LOCAL KEYWORD File (#8984.1)

ENTRY field (#.02) of the LOCAL SHORTCUT File (#8984.2)

CROSS

REFERENCED BY: LONG DESCRIPTION(AC), LONG DESCRIPTION(ADVB), NAME(B),

DX CODE(C)

31,.001 NUMBER NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>9999)!(X\<0)!(X?.E1"."1N.N) X

LAST EDITED: MAR 20, 1986

HELP-PROMPT: TYPE A WHOLE NUMBER BETWEEN 0 AND 9999

DESCRIPTION: This field contains the internal entry number

for this disability condition. This number may

be used by various software packages. This

must not be edited and entries must not be

added or deleted unless done through a software

upgrade of the MAS package.

31,.01 NAME 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:X\[""""!(\$A(X)=45) X I \$D(X) K:\$L(X)\>45!(\$L(X) \<4)!'(X'?1P.E) X

LAST EDITED: OCT 31, 2006

HELP-PROMPT: ANSWER MUST BE 4-45 CHARACTERS IN LENGTH

DESCRIPTION: VBA DISABILITY CODES MP-6,PART IV Supp 4.1 401.02f

> UNEDITABLE

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 31^B

> 1)= S ^DIC(31,"B",\$E(X,1,30),DA)=""

> 2)= K ^DIC(31,"B",\$E(X,1,30),DA)

31,1 ABBREVIATION 0;2 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<4) X

HELP-PROMPT: ANSWER MUST BE 4-30 CHARACTERS IN LENGTH

DESCRIPTION: Enter an abbreviation, 4-30 characters.

31,2 DX CODE 0;3 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>9999)!(X\<0)!(X?.E1"."1N.N) X

LAST EDITED: OCT 29, 2004

HELP-PROMPT: TYPE A WHOLE NUMBER BETWEEN 0 AND 9999

DESCRIPTION: This field contains a numeric 0-9999. It is the diagnosis code number.

UNEDITABLE

CROSS-REFERENCE: 31^C

> 1)= S ^DIC(31,"C",X,DA)=""

> 2)= K ^DIC(31,"C",X,DA)

31,3 SENSITIVE CONDITION PRINT NAME 0;4 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>32!(\$L(X)\<4)!'(X'?1P.E) X

LAST EDITED: JUL 03, 1991

HELP-PROMPT: Answer must be 4-32 characters in length.

DESCRIPTION: In order to maintain sensitivity for certain

diagnosis this field has been added. If it is

filled in, the .01 field for the diagnosis is

not printed, but the SENSITIVE CONDITION PRINT

NAME is, instead.

31,10 LONG DESCRIPTION 1;1 FREE TEXT

INPUT TRANSFORM: K:X\[""""!(\$A(X)=45) X I \$D(X) K:\$L(X)\>200!(\$L(X )\<1) X

LAST EDITED: MAR 07, 1994

HELP-PROMPT: Answer must be 1-200 characters in length.

DESCRIPTION: This is the long description per the VBA Rating Schedule.

CROSS-REFERENCE: 31^ADVB^MUMPS

> 1)= S %="^DIC(31,""ADVB"",I,DA)" D S^XTLKWIC

> 2)= S %="^DIC(31,""ADVB"",I,DA)" D K^XTLKWIC

> This is the MTLU cross reference lookup for the AMIE application.

CROSS-REFERENCE: 31^AC^MUMPS

> 1)= S ^DIC(31,"AC",\$E(X,1,80),DA)=""

> 2)= K ^DIC(31,"AC",\$E(X,1,80),DA)

> This cross reference was created so that a

> lookup could be performed on it using IX or

> MIX\. It was created so that interactive FM

> could not use it. As a result users will not

> get confused at a selection prompt.

31,20 RELATED ICD9 CODES ICD;0 POINTER Multiple \#31.01

(Add New Entry without Asking)

DESCRIPTION: The Veterans Health Administration (VHA) has

> mapped the Veteran Benefits Administration

> (VBA) 4 digit RATED DISABILITIES (VA) code

> terminology to the ICD-9-CM codes used for

> billing and reporting purposes within VistA.

> This mapping will help automate the Service

> Connected (SC) decision for outpatient encounters.

31.01,.01 RELATED ICD9 CODES 0;1 POINTER TO ICD DIAGNOSIS FILE (#80)

LAST EDITED: JAN 18, 2007

DESCRIPTION: ICD9 code associated with the VBA code.

TECHNICAL DESCR: A pointer to the ICD DIAGNOSIS file \#80.

> UNEDITABLE

CROSS-REFERENCE: 31.01^B

> 1)= S ^DIC(31,DA(1),"ICD","B",\$E(X,1,30),DA)=""

> 2)= K ^DIC(31,DA(1),"ICD","B",\$E(X,1,30),DA)

31.01,.02 ICD9 MATCH 0;2 SET

'0' FOR PARTIAL MATCH;

'1' FOR MATCH;

LAST EDITED: JAN 18, 2007

HELP-PROMPT: Enter 1 for a match or 0 for a partial match.

DESCRIPTION: If this ICD9 code is a true match for the VBA

> code then the value will be a 1. Otherwise it

> is a 0 indicating a partial match.

> UNEDITABLE

FILES POINTED TO FIELDS

ICD DIAGNOSIS (#80) RELATED ICD9 CODES:RELATED ICD9 CODES (#.01)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):