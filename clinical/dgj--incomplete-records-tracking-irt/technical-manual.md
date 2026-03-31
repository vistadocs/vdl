---
title: Incomplete Records Tracking (IRT) Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: DGJ
app_name: Incomplete Records Tracking (IRT)
section: CLI
app_status: active
pkg_ns: DGJ
patch_ver: 1
patch_id: DGJ*1
group_key: "DGJ:DGJ:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Introduction 1](#introduction-1) - [Orientation 3](#orientation-3) - [General Information 5](#general-information-5) - [Implementation and Maintenance 7](#implementation-and-maintenance-7) - [Routines 11](#routines-11) - [Files 13](#files-13) - [Exported Options 15](#exported-options-15) - [Archi
audience: 
keywords: 
  - table
  - contents
  - package
  - vaip
  - physician
  - vadpt
  - incomplete
  - entry
  - patient
  - options
page_count: 0
word_count: 4823
section_count: 14
table_count: 22
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=124"
---

![](incomplete-records-tracking-irt-version-1-technical-manual/001.png)

Incomplete Records Tracking (IRT)Technical Manual

April 2002

V*IST*A Software Design & Development

table of Contents

## Introduction 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Information 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Namespace and Conventions 5

> Background Job Options 5

> E-Mail Notifications 5

> E-Mail Reports 5

> Integrity Checker 5

> SACC Exemptions/Non-Standard Code 5

## Implementation and Maintenance 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Set up IRT Parameters 7

> ADT System Definition Menu Option: Bulletin Selection 9

## Routines 11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routine to Map 11

> Callable Routines 11

> Compiled Template Routines 11

> Routine List 11

## Files 13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Globals and Files 13

> File List 13

> Templates 14

## Exported Options 15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Menu Diagrams 15

> Exported Protocols 15

> Exported Options 15

> Exported List Templates 15

## Archiving and Purging 17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External/Internal Relations 19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DBIA Agreements 19

Package Wide-Variables 21

> VADPT Variables (See Appendix) 21

> VAUTOMA 21

## How to Generate On-Line Documentation 23

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security 25

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security Keys 25

> FileMan Access Codes 25

## Glossary 27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix - VADPT Variables 29

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Overview 29

> Supported References 30

> Callable Entry Points in VADPT 31

> Alpha Subscripts 67

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Introduction 1](#introduction-1)
  - [Orientation 3](#orientation-3)
  - [General Information 5](#general-information-5)
  - [Implementation and Maintenance 7](#implementation-and-maintenance-7)
  - [Routines 11](#routines-11)
  - [Files 13](#files-13)
  - [Exported Options 15](#exported-options-15)
  - [Archiving and Purging 17](#archiving-and-purging-17)
  - [External/Internal Relations 19](#externalinternal-relations-19)
  - [How to Generate On-Line Documentation 23](#how-to-generate-on-line-documentation-23)
  - [Security 25](#security-25)
  - [Glossary 27](#glossary-27)
  - [Appendix - VADPT Variables 29](#appendix-vadpt-variables-29)
- [# Introduction](#introduction)
- [The Physician for Deficiency will be tracked throughout the IRT process. The users will know who is responsible for the deficiency at various stages of tracking, from entry through completion.](#the-physician-for-deficiency-will-be-tracked-throughout-the-irt-process-the-users-will-know-who-is-responsible-for-the-deficiency-at-various-stages-of-tracking-from-entry-through-completion)
- [Orientation](#orientation)
- [General Information](#general-information)
- [Namespace and Conventions](#namespace-and-conventions)
- [The namespace assigned to Incomplete Records Tracking is DGJ.](#the-namespace-assigned-to-incomplete-records-tracking-is-dgj)
- [Background Job Options](#background-job-options)
- [<u>OPTION</u> <u>SUBJECT</u> <u>ROUTINE</u>](#uoptionu-usubjectu-uroutineu)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [The IRT package may be tailored specifically to meet the needs of the various sites. The IRT package will function around the parameters defined through the Set up IRT Parameters option. The IRT short form list group entry may be found in the Bulletin Selection of the ADT System Definition Menu option.](#the-irt-package-may-be-tailored-specifically-to-meet-the-needs-of-the-various-sites-the-irt-package-will-function-around-the-parameters-defined-through-the-set-up-irt-parameters-option-the-irt-short-form-list-group-entry-may-be-found-in-the-bulletin-selection-of-the-adt-system-definition-menu-option)
- [Routines](#routines)
- [Routines to Map](#routines-to-map)
- [Files](#files)
- [Globals and Files](#globals-and-files)
- [Exported Options](#exported-options)
- [The following are the steps you may take to obtain information about menus, exported protocols, exported options and exported list templates concerning the IRT package.](#the-following-are-the-steps-you-may-take-to-obtain-information-about-menus-exported-protocols-exported-options-and-exported-list-templates-concerning-the-irt-package)
- [Archiving and Purging](#archiving-and-purging)
- [There are no archiving and purging capabilities connected to the IRT package.](#there-are-no-archiving-and-purging-capabilities-connected-to-the-irt-package)
- [External/Internal Relations](#externalinternal-relations)
- [Minimums of VA FileMan V. 21.0, Kernel V. 8.0, and PIMS V. 5.3 are required to run this package.](#minimums-of-va-fileman-v-210-kernel-v-80-and-pims-v-53-are-required-to-run-this-package)
- [Package-Wide Variables](#package-wide-variables)
- [There are no package-wide variables associated with the IRT package.](#there-are-no-package-wide-variables-associated-with-the-irt-package)
- [How to Generate On-Line Documentation](#how-to-generate-on-line-documentation)
- [This section describes some of the various methods by which users may secure IRT technical documentation. On-line technical documentation pertaining to the IRT software, in addition to that which is located in the help prompts and on the help screens which are found throughout the IRT package, may be generated through utilization of several KERNEL options. These include but are not limited to: XINDEX, Menu Management Inquire Option File, Print Option File, and FileMan List File Attributes.](#this-section-describes-some-of-the-various-methods-by-which-users-may-secure-irt-technical-documentation-on-line-technical-documentation-pertaining-to-the-irt-software-in-addition-to-that-which-is-located-in-the-help-prompts-and-on-the-help-screens-which-are-found-throughout-the-irt-package-may-be-generated-through-utilization-of-several-kernel-options-these-include-but-are-not-limited-to-xindex-menu-management-inquire-option-file-print-option-file-and-fileman-list-file-attributes)
- [Security](#security)
- [Security Keys](#security-keys)
- [Glossary](#glossary)
- [ADT Admission, Discharge, and Transfer](#adt-admission-discharge-and-transfer)
- [Appendix – VADPT Variables](#appendix-vadpt-variables)
The Incomplete Records Tracking (IRT) software is formerly a component of PIMS V. 5.3. With PIMS V. 5.3, it includes many enhancements that should allow the users greater flexibility and efficiency when tracking incomplete records.
The package now tracks all types of deficiencies, in addition to those already being tracked (Discharge and Interim Summaries and OP Reports). The sites will have the ability to add the deficiencies they wish to track to make this package more site specific.

# The Physician for Deficiency will be tracked throughout the IRT process. The users will know who is responsible for the deficiency at various stages of tracking, from entry through completion.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the technical manual for the Incomplete Records Tracking (IRT) software package. It is designed to provide necessary information for use in the technical operation of the Incomplete Records Tracking software product. The technical manual is intended for use by technical computer personnel and not the typical end user.

# General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Namespace and Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The namespace assigned to Incomplete Records Tracking is DGJ.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Background Job Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SUGGESTED DEVICE

<u>OPTION NAME</u> <u>RUN FREQUENCY</u> <u>REQUIRED</u> <u>REMARKS</u>

DGJ IRT UPDATE (BACKGROUND) Nightly NO Schedule in TaskMan

E-Mail Notifications

# <u>OPTION</u> <u>SUBJECT</u> <u>ROUTINE</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRT Update Std. Def. Background Job Patients Discharged Less than 48 hours DGJBGJ

IRT Update Std. Deficiencies Patients Discharged Less than 48 hours DGJBGJ

E-Mail Reports

There is a report that is created by the IRT background job that is sent to a mail group at each facility. This report lists the patients that have had short form discharges (less than 48 hours from admission) within the time frame of when the IRT background job was run. The facility should use the Bulletin Selection option under the ADT System Definition menu to set up the mail group to receive this report.

Integrity Checker

IRT uses KIDS integrity checker. Under the installation option of the Kernel Installation Distribution System menu, select Verify Checksums in Transport Global to ensure that the routines are correct.

SACC Exemptions/Non-Standard Code

There are no SACC exemptions/non-standard code in the IRT package.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The IRT package may be tailored specifically to meet the needs of the various sites. The IRT package will function around the parameters defined through the Set up IRT Parameters option. The IRT short form list group entry may be found in the Bulletin Selection of the ADT System Definition Menu option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set up IRT Parameters

The Set up IRT Parameters option is used to establish site specific parameters and activate/inactivate the IRT package. You must hold the DGJ SUPER key to access this option.

These site parameters determine the default physician responsible for dictating and signing the summary/report, whether reviewed by another physician is required, the default physician (if any) responsible for reviewing the summary/report, whether outpatient operation reports are tracked, the number of days a physician has to dictate, sign, and review a summary/report before it is considered incomplete, any message you wish to have appear on the bottom of each page of the Incomplete Records List or Undictated Reports List, and if short forms (admission and discharge within 48 hours) should have standard deficiencies created for them.

Listed below is a brief explanation of each site parameter.

MEDICAL CENTER DIVISION NAME

The name or number of the division for which you wish to set the IRT parameters. The division entered at this prompt must be in the MEDICAL CENTER DIVISION file.

TRACK INCOMPLETE SUMMARIES?

Enter YES to track incomplete summaries/reports. If NO is entered, the IRT package will be inactivated and no incomplete reports or summaries will be tracked. The system will maintain the default values of all other site parameters while the package is inactivated. When the IRT package is reactivated, those defaults will become effective.

DEFAULT PRIMARY PHYSICIAN

Select PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report entry is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default Primary physician for the Incomplete Records entry.

ARE REPORTS REVIEWED?

Enter YES if this division requires a second physician to review the summary/report. Enter NO if review by a second physician is not necessary.

DEFAULT REVIEWING PHYSICIAN

This prompt will only appear if YES was entered at the previous prompt. Enter PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default Attending physician for the Incomplete Records entry.

DEFAULT PHYS. FOR SIGNATURE

Select PRIMARY or ATTENDING physician. Depending on the entry made, when the summary or operation report entry is created, the physician of record (PRIMARY or ATTENDING) in Bed Control will be the default physician.

TRACK OUTPATIENT OP REPORTS?

Enter YES if you want to track outpatient operation reports at this division. Enter NO to not track outpatient reports.

DAYS FOR DICTATION

The number of days (0-99) the physician has to dictate a summary/report before it is considered incomplete.

DAYS FOR SIGNATURE

The number of days (0-99) from the date of transcription the physician has to sign a summary/report before it is considered incomplete.

DAYS FOR REVIEW

The number of days (0-99) the reviewing physician has to review the report, once it has been signed, before it is considered incomplete. This prompt will only appear if “ARE REPORTS REVIEWED” prompt is answered YES.

INCOMPLETE SUMMERIES MESSAGE

A free text message, 1-99 characters in length, which will appear on the reports generated by the Incomplete Reports Print and Undictated Reports Print options.

STD. DEFIC. FOR SHORT FORMS

Renter YES if you wish the IRT background job to create standard deficiencies for short form discharges (discharged less than 48 hours after admission).

DEFAULT MEDICAL RECORD TYPE

Enter the Record Type name used for Medical Records. If the entry is left blank, the default value will be MEDICAL RECORDS. This parameter is useful at sites which may have a different name for their Medical Records department.

ADT System Definition Menu Option: Bulletin Selection

This option is used to specify the mail group you desire specific types of notification to be made to. The mail group can be one created locally or a distributed 'DG' mail group. If a mail group is selected, notification concerning that specific action will be made in the form of a mailman bulletin. If no notification is desired for a specific action, no mail group should be specified. If you have any questions concerning the purpose of a specific type of notification enter a question, mark at the applicable prompt.

DEATH GROUP: DEATH GROUP// ^IRT SHORT FORM LIST GROUP

IRT SHORT FORM LIST GROUP: ???

Select the name of the mail group which should be notified whenever

the IRT Background Job is run, options: (IRT Update Std. Deficiencies and

IRT Update Std. Def. Background Job), to receive a list of patients that

have been discharged less than 48 hours from their admission (Short Form).

If no mail group is selected no bulletin will be generated.

Answer with MAIL GROUP NAME

Do you want the entire 860-Entry MAIL GROUP List?

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For those sites where routine mapping is applicable, the compiled templates DGJX\* may be recommended for mapping.

Callable Routines

VADATE Generic Date Routine

VADPT Obtain Patient Information

VALM List Manager

VAUTOMA Generic One, Many, All Routine

See Package-Wide Variables section of this manual for entry points.

Compiled Template Routines

It is recommended you recompile the following input templates at 4000 bytes.

<u>FILE \#</u> <u>TEMPLATE NAME</u> <u>ROUTINES</u>

393 DGJ EDIT IRT RECORD DGJXE\*

DGJ ENTER IRT RECORD DGJXA\*

Routine List

The following are the steps you may take to obtain a listing of the routines contained in the IRT package.

1)  Programmer Options Menu
2)  Routine Tools Menu
3)  First Line Routine Print Option
4)  Routine Selector: DGJ\*

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main globals used in the IRT package are ^DG, and ^VAS. The main files are INCOMPLETE RECORDS, MAS SERVICE, IRT STATUS, IRT TYPE OF DEFICIENCY, and TYPE OF CATEGORY.

The MEDICAL CENTER DIVISION, MAS PARAMETERS, and PATIENT MOVEMENT files belong to the Registration package . These files contain fields belonging to the IRT package.

File List

<u>FILE \#</u> <u>FILE NAME</u> <u>GLOBAL</u>

<u>FIELD NAME</u> <u>FIELD \#</u>

40.8 MEDICAL CENTER DIVISION ^DG(40.8,

TRACK INCOMPLETE SUMMARIES? 100.01

DEFAULT PRIMARY PHYSICIAN 100.02

ARE REPORTS REVIEWED? 100.03

DEFAULT REVIEWING PHYSICIAN 100.04

TRACK OUTPATIENT OP REPORTS? 100.05

DAYS FOR DICTATION 100.06

DAYS FOR SIGNATURE 100.07

DAYS FOR REVIEW 100.08

INCOMPLETE SUMMARIES MESSAGE 100.09

DEFAULT PHYS. FOR SIGNATURE 100.1

STD. DEFIC. FOR SHORT FORMS? 100.2

DEFAULT MEDICAL RECORD TYPE 100.3

43 MAS PARAMETERS ^DG(43,

IRT BACKGROUND JOB LAST RUN 401

IRT SHORT FROM LIST GROUP 513

393 INCOMPLETE RECORDS ^VAS(393,

393.1 MAS SERVICE ^DG(393.1,

393.2 IRT STATUS ^DG(393.2,

393.3 IRT TYPE OF DEFICIENCY ^VAS(393.3,

393.41 TYPE OF CATEGORY ^VAS(393.41,

405 PATIENT MOVEMENT ^DGPM(405,

Templates

1)  VA FileMan Menu
2)  Print File Entries Option
3)  Output from what File: Print Template, Sort Template, Input Template, List Template
4)  Sort by: Name
5)  Start with name: DGJ to DGJZ
6)  Within name, sort by: \<RET\>
7)  First print field: Name

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The following are the steps you may take to obtain information about menus, exported protocols, exported options and exported list templates concerning the IRT package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menu Diagrams

1.  Programmers Options
2.  Menu Management
3.  Display Menus and Options Menu
4.  Diagram Menus
5.  Select User or Option Name: O.DGJ IRT MENU

Exported Protocols

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: PROTOCOL
4.  Sort by: Name
5.  Start with name: DGJ to DGJZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

Exported Options

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: OPTION
4.  Sort by: Name
5.  Start with name: DGJ to DGJZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

Exported List Templates

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: LIST TEMPLATES
4.  Sort by: Name
5.  Start with name: DGJ to DGJZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# There are no archiving and purging capabilities connected to the IRT package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Minimums of VA FileMan V. 21.0, Kernel V. 8.0, and PIMS V. 5.3 are required to run this package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DBIA AGREEMENTS

The following are the steps you may take to obtain the database integration agreements for the IRT package.

DBIA Agreements - Custodial Package

1.  FORUM
2.  DBA Menu
3.  Integration Agreements Menu
4.  Custodial Package Menu
5.  Active by Custodial Package Option
6.  Select Package Name: Incomplete Records Tracking

DBIA Agreements - Subscriber Package

1.  FORUM
2.  DBA Menu
3.  Integration Agreements Menu
4.  Subscriber Package Menu
5.  Print Active by Subscriber Package Option
6.  Start with subscriber package: Incomplete Records Tracking

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# There are no package-wide variables associated with the IRT package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VADPT Variables

See Appendix.

VAUTOMA

VAUTOMA is a routine which will do a one/many/all prompt - returning the chosen values in a subscripted variable specified by the calling programmer.

Input variables:

> VAUTSTR string which describes what is to be entered.

> VAUTNI defines if array is sorted alphabetically or numerically.

> VAUTVB name of the subscripted variable to be returned.

> VAUTNALL define this variable if you do not want the user to be given the

> ALL option.

> Other variables as required by a call to ^DIC (see VA FileMan Programmers Manual).

Output variables:

> As defined in VAUTVB

# How to Generate On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# This section describes some of the various methods by which users may secure IRT technical documentation. On-line technical documentation pertaining to the IRT software, in addition to that which is located in the help prompts and on the help screens which are found throughout the IRT package, may be generated through utilization of several KERNEL options. These include but are not limited to: XINDEX, Menu Management Inquire Option File, Print Option File, and FileMan List File Attributes.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the V*ist*A Kernel Reference Manual.

XIndex

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to V*ist*A Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from V*ist*A Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the IRT package, specify the following namespaces at the "routine(s) ?\>" prompt: DGJ\*.

IRT initialization routines which reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the IRT namespace should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

List File Attributes

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information about the security keys contained in the IRT package.

1.  VA FileMan Menu
2.  Print File Entries Option
3.  Output from what File: SECURITY KEY
4.  Sort by: Name
5.  Start with name: DGJ to DGJZ
6.  Within name, sort by: \<RET\>
7.  First print field: Name
8.  Then print field: Description

FileMan Access Codes

Below is a list of recommended FileMan Access Codes associated with each file contained in the IRT package. This list may be used to assist in assigning users appropriate FileMan Access Codes.

FILE FILE DD RD WR DEL LAYGO

<u>NUMBER</u> <u>NAME</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

40.8\*\* MEDICAL CENTER DIVISION @ d @ @ D

43\*\* MAS PARAMETERS @ d D @ @

393 INCOMPLETE RECORDS @ d D D D

393.1 MAS SERVICE @ d @ @ @

393.2 IRT STATUS @ d @ @ @

393.3 IRT TYPE OF DEFICIENCY @ d @ @ @

393.41 TYPE OF CATEGORY @ d @ @ @

405\*\* PATIENT MOVEMENT @ d @ @ @

\*\* Files owned by the Registration package contain fields belonging to the IRT package.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ADT Admission, Discharge, and Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRT Incomplete Records Tracking

KIDS Kernel Installation and Distribution System

PIMS Patient Information Management System

PTF Patient Treatment File

SACC Standards and Conventions Committee

PTF Patient Treatment File

VISTA Veterans Health Information Systems and Technology Architecture

# Appendix – VADPT Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

I. OVERVIEWVADPT is a utility routine designed to provide a central point where a programmer can obtain information concerning a patient's record. Supported entry points are

provided which will return demographics, inpatient status, eligibility information, etc.

Access to patient information is not limited to using the supported entry points in VADPT. Integration agreements can be established through the DBA between PIMS and other packages to reference information. Additionally, several data elements are supported without an integration agreement.

II. SUPPORTED REFERENCES

The following references to patient information (PATIENT file \#2) are supported without an integration agreement. All nationally distributed cross-references on these fields are also supported.

|                           |              |                     |                    |
|---------------------------|--------------|---------------------|--------------------|
| Field Name            | Field \# | Global Location | Type of Access |
| NAME                      | (#.01)       | 0;1                 | Read               |
| SEX                       | (#.02)       | 0;2                 | Read               |
| DATE OF BIRTH             | (#.03)       | 0;3                 | Read               |
| AGE                       | (#.033)      | N/A                 | Read               |
| MARITAL STATUS            | (#.05)       | 0;5                 | Read               |
| RACE                      | (#.06)       | 0;6                 | Read               |
| OCCUPATION                | (#.07)       | 0;7                 | Read               |
| RELIGIOUS PREFERENCE      | (#.08)       | 0;8                 | Read               |
| DUPLICATE STATUS          | (#.081)      | 0;18                |                    |
| PATIENT MERGED TO         | (#.082)      | 0;19                |                    |
| CHECK FOR DUPLICATE       | (#.083)      | 0;20                |                    |
| SOCIAL SECURITY NUMBER    | (#.09)       | 0;9                 | Read               |
| REMARKS                   | (#.091)      | 0;10                | Read               |
| PLACE OF BIRTH \[CITY\]   | (#.092)      | 0;11                | Read               |
| PLACE OF BIRTH \[STATE\]  | (#.093)      | 0;12                | Read               |
| WHO ENTERED PATIENT       | (#.096)      | 0;15                | Read               |
| DATE ENTERED INTO FILE    | (#.097)      | 0;16                | Read               |
| WARD LOCATION             | (#.1)        | .1;1                | Read               |
| ROOM-BED                  | (#.101)      | .101;1              | Read               |
| CURRENT MOVEMENT          | (#.102)      | .102;1              | Read               |
| TREATING SPECIALTY        | (#.103)      | .103;1              | Read               |
| PROVIDER                  | (#.104)      | .104;1              | Read               |
| ATTENDING PHYSICIAN       | (#.1041)     | .1041;1             | Read               |
| CURRENT ADMISSION         | (#.105)      | .105;1              | Read               |
| LAST DMMS EPISODE NUMBER  | (#.106)      | .106;1              | Read               |
| LODGER WARD LOCATION      | (#.107)      | .107;1              | Read               |
| CURRENT ROOM              | (#.108)      | .108;1              | Read               |
| CURRENT MEANS TEST STATUS | (#.14)       | 0;14                | Read               |
| DATE OF DEATH             | (#.351)      | .35;1               | Read               |
| DEATH ENTERED BY          | (#.352)      | .35;2               | Read               |
| PRIMARY LONG ID           | (#.363)      | .36;3               |                    |
| PRIMARY SHORT ID          | (#.364)      | .36;4               |                    |
| CURRENT PC PRACTITIONER   | (#404.01)    | PC;1                | Read               |
| CURRENT PC TEAM           | (#404.02)    | PC;2                | Read               |
| LAST MEANS TEST           | (#999.2)     | N/A                 | Read               |

III. CALLABLE ENTRY POINTS IN VADPT

1\. DEM^VADPT

This entry point returns demographic information for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VAPTYP This optional variable can be set to the

> internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, DOD, or IHS through the eligibility. If this variable is not defined or the eligibility does not exist, the VA patient IDs will be returned.

> VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VADM(1) would be VADM("NM"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VADM",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VADM",\$J,"NM"))

> VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGDEM")

> Output: VADM(1) The NAME of the patient.

> (e.g., IRTPATIENT,ONE)

> VADM(2) The SOCIAL SECURITY NUMBER of

> the patient in internal^external format.

> (e.g., 000456789^000-45-6789)

> VADM(3) The DATE OF BIRTH of the patient

> in internal^external format.

> (e.g., 2551025^OCT 25,1955)

> VADM(4) The AGE of the patient as of today,

> unless a date of death exists, in which case the age returned will be as of that date. (e.g., 36)

> VADM(5) The SEX of the patient in internal

> ^external format. (e.g., M^MALE)

> VADM(6) The DATE OF DEATH of the patient,

> should one exist, in internal^external format.

> (e.g., 2881101.08^NOV 1,1988@08:00)

> VADM(7) Any REMARKS concerning this

> patient which may be on file.

> (e.g., Need to obtain dependent info.)

> VADM(8) The RACE of the patient in internal

> ^external format.

> (e.g., 1^WHITE,NON-HISPANIC)

> VADM(9) The RELIGION of the patient in

> internal^external format.

> (e.g., 99^CATHOLIC)

> VADM(10) The MARITAL STATUS of the patient

> in internal^external format.

> (e.g., 1^MARRIED)

> VA("PID") The PRIMARY LONG ID for a patient.

> The format of this variable will depend on the type of patient if VAPTYP is set. (e.g., 000-45-6789)

> VA("BID") The PRIMARY SHORT ID for a

> patient. The format of this variable will depend on the type of patient if VAPTYP is set. (e.g., 6789)

> VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

2\. ELIG^VADPT

This entry point returns eligibility information for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAEL(1) would be VAEL("EL"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VAEL",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAEL",\$J,"EL"))

> VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGELG")

> Output: VAEL(1) The PRIMARY ELIGIBILITY CODE

> of the patient in internal^external format.

> (e.g., 1^SERVICE CONNECTED 50-100%)

> VAEL(1,#) An array of other PATIENT ELIGI-

> BILITIES to which the patient is entitled to care, in internal^external format. The \# sign represents the internal entry number of the eligibility in the ELIGIBILITY CODE file. (e.g., 13^PRISONER OF WAR)

VAEL(2) The PERIOD OF SERVICE of the

> patient in internal^external format.

> (e.g., 19^WORLD WAR I)

> VAEL(3) If the SERVICE CONNECTED? field

> is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If service connected, the SERVICE CONNECTED PERCENTAGE field will be returned in the second piece. (e.g., 1^70)

> VAEL(4) If the VETERAN (Y/N)? field is YES, a

> "1" will be returned; otherwise, a "0" will be returned. (e.g., 1)

> VAEL(5) If an INELIGIBLE DATE exists, a "0"

> will be returned indicating the patient is ineligible; otherwise, a "1" will be returned. (e.g., 0)

> VAEL(5,1) If ineligible, the INELIGIBLE DATE

> of the patient in internal^external format. (e.g., 2880101^JAN 1,1988)

> VAEL(5,2) If ineligible, the INELIGIBLE TWX

> SOURCE in internal^external format.

> (e.g., 2^REGIONAL OFFICE)

> VAEL(5,3) If ineligible, the INELIGIBLE TWX

> CITY. (e.g., ALBANY)

> VAEL(5,4) If ineligible, the INELIGIBLE TWX

> STATE from which the ineligible notification was received in internal^external format.

> (e.g., 36^NEW YORK)

> VAEL(5,5) If ineligible, the INELIGIBLE VARO

> DECISION.

> (e.g., UNABLE TO VERIFY)

> VAEL(5,6) If ineligible, the INELIGIBLE

> REASON. (e.g., NO DD214)

> VAEL(6) The TYPE of patient in internal

> ^external format.

> (e.g., 1^SC VETERAN)

> VAEL(7) The CLAIM NUMBER of the patient.

> (e.g., 000456789)

> VAEL(8) The current ELIGIBILITY STATUS of

> the patient in internal^external format. (e.g., V^VERIFIED)

> VAEL(9) The CURRENT MEANS TEST

> STATUS of the patient CODE^

> NAME. (e.g., A^CATEGORY A)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

3\. MB^VADPT

This entry point returns monetary benefit information for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAMB(1) would be VAMB("AA"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VAMB",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAMB",\$J,"AA"))

> VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGMB")

Output: VAMB(1) If the RECEIVING A&A BENEFITS?

> field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving A&A benefits, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 1^1000)

> VAMB(2) If the RECEIVING HOUSEBOUND

> BENEFITS? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving housebound benefits, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece.

> (e.g., 1^0)

VAMB(3) If the RECEIVING SOCIAL

> SECURITY field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving social security, the AMOUNT OF SOCIAL SECURITY will be returned in the second piece. (e.g., 0)

> VAMB(4) If the RECEIVING A VA PENSION?

> field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving a VA pension, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 1^563.23)

> VAMB(5) If the RECEIVING MILITARY

> RETIREMENT? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving military retirement, the AMOUNT OF MILITARY RETIRE-MENT will be returned in the second piece. (e.g., 0)

> VAMB(6) The RECEIVING SUP. SECURITY

> (SSI) field is being eliminated. Since v5.2, a "0" is returned for this variable.

> VAMB(7) If the RECEIVING VA DISABILITY?

> field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving VA disability, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 0)

> VAMB(8) If the TYPE OF OTHER RETIRE-

> MENT field is filled in, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving other retirement, the AMOUNT OF OTHER RETIREMENT will be returned in the second piece.

> (e.g., 1^2500.12)

> VAMB(9) If the GI INSURANCE POLICY? field

> is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving GI insurance, the AMOUNT OF GI INSURANCE will be returned in the second piece.

> (e.g., 1^100000)

> VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

4\. SVC^VADPT

This entry point returns service information for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VASV(1) would be VASV("VN"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VASV",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VASV",\$J,"VN"))

> VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGSVC")

Output: VASV(1) If the VIETNAM SERVICE

> INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

> VASV(1,1) If Vietnam Service, the VIETNAM

> FROM DATE in internal^external format.

> (e.g., 2680110^JAN 10,1968)

> VASV(1,2) If Vietnam Service, the VIETNAM TO

> DATE in internal^external format.

> (e.g., 2690315^MAR 15,1969)

> VASV(2) If the AGENT ORANGE EXPOS.

> INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

> VASV(2,1) If Agent Orange exposure, the AGENT

> ORANGE REGISTRATION DATE in internal^external format.

> (e.g., 2870513^MAY 13,1987)

> VASV(2,2) If Agent Orange exposure, the AGENT

ORANGE EXAMINATION DATE in internal^external format.

> (e.g., 2871101^NOV 1,1987)

> VASV(2,3) If Agent Orange exposure, AGENT

> ORANGE REPORTED TO C.O. date in internal^external format.

> (e.g., 2871225^DEC 25,1987)

> VASV(2,4) If Agent Orange exposure, AGENT

> ORANGE REGISTRATION \#.

> (e.g., 123456)

> VASV(2,5) If Agent Orange exposure, the AGENT

> ORANGE EXPOSURE LOCATION in

> internal^external format

> (e.g., V^VIETNAM)

> VASV(3) If the RADIATION EXPOSURE

> INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned (e.g., 0)

> VASV(3,1) If Radiation Exposure, RADIATION

> REGISTRATION DATE in internal^external format.

> (e.g., 2800202^FEB 02,1980)

> VASV(3,2) If Radiation Exposure, RADIATION

> EXPOSURE METHOD in internal^external format.

> (e.g., T^NUCLEAR TESTING)

> VASV(4) If the POW STATUS INDICATED

> field is YES, a "1" will be returned; otherwise a "0" will be returned.

> (e.g., 0)

> VASV(4,1) If POW status, POW FROM DATE in

> internal^external format.

> (e.g., 2450319^MAR 19,1945)

> VASV(4,2) If POW status, POW TO DATE in

> internal^external format.

> (e.g., 2470101^JAN 1,1947)

> VASV(4,3) If POW status, POW CONFINEMENT

> LOCATION in internal^external format.

> (e.g., 2^WORLD WAR II - EUROPE)

> VASV(5) If the COMBAT SERVICE

> INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

> VASV(5,1) If combat service, COMBAT FROM

> DATE in internal^external format.

> (e.g., 2430101^JAN 1,1943)

> VASV(5,2) If combat service, COMBAT TO DATE

> in internal^external format.

> (e.g., 2470101^JAN 1,1947)

> VASV(5,3) If combat service, COMBAT SERVICE

> LOCATION in internal^external format.

> (e.g., 2^WORLD WAR II - EUROPE)

> VASV(6) If a SERVICE BRANCH \[LAST\] field

> is indicated, a "1" will be returned in the first piece; otherwise a "0" will be returned. (e.g., 0)

> VASV(6,1) If service branch, BRANCH OF

> SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

> VASV(6,2) If service branch, SERVICE NUMBER

> field in internal^external format.

> (e.g., 000456789)

> VASV(6,3) If service branch, SERVICE

> DISCHARGE TYPE in internal^external format.

> (e.g., 1^HONORABLE)

> VASV(6,4) If service branch, SERVICE ENTRY

> DATE in internal^external format.

> (e.g., 2440609^JUN 9,1944)

> VASV(6,5) If service branch, SERVICE

> SEPARATION DATE in internal^external format.

> (e.g., 2480101^JAN 1,1948)

VASV(7) If a SERVICE SECOND EPISODE

> field is indicated, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

> VASV(7,1) If second episode, BRANCH OF

> SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

> VASV(7,2) If second episode, SERVICE

> NUMBER field in internal^external format. (e.g., 000456789)

> VASV(7,3) If second episode, SERVICE

> DISCHARGE TYPE in internal^external format.

> (e.g., 1^HONORABLE)

> VASV(7,4) If second episode, SERVICE ENTRY

> DATE in internal^external format.

> (e.g., 2440609^JUN 9,1944)

> VASV(7,5) If second episode, SERVICE

> SEPARATION DATE in internal^external format.

> (e.g., 2480101^JAN 1,1948)

> VASV(8) If a SERVICE THIRD EPISODE field

> is indicated, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

> VASV(8,1) If third episode, BRANCH OF

> SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

> VASV(8,2) If third episode, SERVICE NUMBER

> field in internal^external format.

> (e.g., 000456789)

> VASV(8,3) If third episode, SERVICE DIS-

> CHARGE TYPE in internal^external

format. (e.g., 1^HONORABLE)

> VASV(8,4) If third episode, SERVICE ENTRY

> DATE in internal^external format.

> (e.g., 2440609^JUN 9,1944)

> VASV(8,5) If third episode, SERVICE

SEPARATION DATE in

internal^external format.

> (e.g., 2480101^JAN 1,1948)

> VASV(9) If the CURRENT PH INDICATOR

field is YES, a “1” will be returned;

otherwise a “0” will be returned (e.g., 0)

> VASV(9,1) If the CURRENT PH INDICATOR

field is YES, CURRENT PURPLE

HEART STATUS in internal^external

format.(e.g., 2^IN PROCESS)

> VASV(9,2) If the CURRENT PH INDICATOR

field is NO, CURRENT PURPLE

HEART REMARKS in internal^

external format. (e.g., 5^VAMC)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

5\. ADD^VADPT

This entry point returns address data for a patient. If a temporary address is in effect, the data returned will be that pertaining to that temporary address; otherwise, the permanent patient address information will be returned.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAPA(1) would be VAPA("L1"))

> 2 -- return the output in the ^UTIL-

> ITY global with numeric subscripts

> (e.g., ^UTILITY(“VAPA”, \$J,1))

> 12 -- return the output in the

> ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAPA",\$J,"L1"))

> VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGADD")

> VAPA("P") This optional variable can be set to

> force the return of the patient's permanent address. The permanent address array will be returned regardless of whether or not a temporary address is in effect.

> (e.g., VAPA("P")="")

> VATEST("ADD",9) This optional variable can be defined

> to a beginning date in VA File-Manager format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned. (e.g., VATEST("ADD",9)=2920101)

> VATEST("ADD",10) This optional variable can be defined

> to a ending date in VA FileManager format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned.

> (e.g., VATEST("ADD",10)=2920301)

> Output: VAPA(1) The first line of the STREET ADDRESS.

> (e.g., 123 South Main Street)

> VAPA(2) The second line of the STREET

> ADDRESS. (e.g., Apartment \#1245.)

> VAPA(3) The third line of the STREET

> ADDRESS. (e.g., P.O. Box 1234)

VAPA(4) The CITY corresponding to the street

> address previously indicated.

> (e.g., ALBANY)

VAPA(5) The STATE corresponding to the city

> previously indicated in internal^

> external format.

> (e.g., 6^CALIFORNIA)

> VAPA(6) The ZIP CODE of the city previously

> indicated. (e.g., 12345)

> VAPA(7) The COUNTY in which the patient is

> residing in internal^external format.

> (e.g., 1^ALAMEDA)

> VAPA(8) The PHONE NUMBER of the location

> in which the patient is currently residing. (e.g., (123) 555-7890)

> VAPA(9) If the address information provided

> pertains to a temporary address, the TEMPORARY ADDRESS START DATE in internal^external format.

> (e.g., 2880515^MAY 15,1988)

> VAPA(10) If the address information provided

> pertains to a temporary address, the TEMPORARY ADDRESS END DATE in internal^external format.

> (e.g., 2880515^MAY 15,1988)

> VAPA(11) The ZIP+4 (5 or 9 digit zip code) of the

> city previously indicated in internal^external format.

> (e.g., 123454444^12345-4444)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

6\. OAD^VADPT

This entry point returns other specific address information.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAOA(1) would be VAOA("L1"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VAOA",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAOA,\$J,"L1")

VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGOA")

VAOA("A") This optional variable may be passed

> to indicate which specific address the programmer wants returned. If it is not defined, the PRIMARY NEXT-OF-KIN will be returned. Otherwise, the following will be returned based on information desired.

> VAOA("A")=1 primary emergency

> contact

> VAOA("A")=2 designee for personal

> effects

> VAOA("A")=3 secondary next-of-kin

> VAOA("A")=4 secondary emergency

> contact

> VAOA("A")=5 patient employer

> VAOA("A")=6 spouse's employer

Output: VAOA(1) The first line of the STREET

> ADDRESS.

> (e.g., 123 South First Street)

> VAOA(2) The second line of the STREET

> ADDRESS. (e.g., Apartment 9D)

> VAOA(3) The third line of the STREET

> ADDRESS. (e.g., P.O. Box 1234)

VAOA(4) The CITY in which the contact/

> employer resides.

> (e.g., NEWINGTON)

VAOA(5) The STATE in which the contact/

> employer resides in internal^external format. (e.g., 6^CALIFORNIA)

VAOA(6) The ZIP CODE of the location in

> which the contact/employer resides.

> (e.g., 12345)

VAOA(7) The COUNTY in which the contact/

> employer resides in internal^external format. (e.g., 1^ALAMEDA)

VAOA(8) The PHONE NUMBER of the

> contact/employer.

> (e.g., (415) 555-1234)

VAOA(9) The NAME of the contact or, in case

> of employment, the employer to whom this address information applies.

> (e.g., IRTEMPLOYER,ONE)

VAOA(10) The RELATIONSHIP of the contact (if

> applicable) to the patient; otherwise, null. (e.g., FATHER)

VAOA(11) The ZIP+4 (5 or 9 digit zip code) of the

> location in which the contact/employer resides in internal^external format.

> (e.g., 123454444^12345-4444)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

7\. INP^VADPT

This entry point will return data related to an inpatient episode.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAIN(1) would be VAIN("AN"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VAIN",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAIN,\$J,"AN")

VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGIN")

VAINDT This optional variable may be set to a

> past date/time for which the programmer wishes to know the patient's inpatient status. This must be passed as an internal VA FileManager date/time format. If time is not passed, it will assume anytime during that day. If this variable is not defined, it will assume now as the date/time. (e.g., 2880101.08)

Output: VAIN(1) The INTERNAL NUMBER \[IFN\] of

> the admission if one was found for the date/time requested. If no inpatient episode was found for the date/time passed, then all variables in the VAIN array will be returned as null.

> (e.g., 123044)

VAIN(2) The PRIMARY CARE PHYSICIAN

> \[PROVIDER\] assigned to the patient at the date/time requested in internal^external format.

> (e.g., 3^IRTPHYSICIAN,ONE)

VAIN(3) The TREATING SPECIALTY

> assigned to the patient at the date/time requested in internal^external format.

> (e.g., 19^GERIATRICS)

VAIN(4) The WARD LOCATION to which the

> patient was assigned at the date/time requested in internal^external format.

> (e.g., 27^IBSICU)

VAIN(5) The ROOM-BED to which the patient

> was assigned at the date/time requested in external format.

> (e.g., 123-B)

VAIN(6) This will return a "1" in the first piece

> if the patient is in a bed status; otherwise, a "0" will be returned. A non-bed status is made based on the last transfer type to a non-bed status, (i.e., authorized absence, unauthorized absence, etc.) The second piece will contain the name of the last transfer type should one exist.

> (e.g., 1^FROM AUTHORIZED ABSENCE)

VAIN(7) The ADMISSION DATE/TIME for the

> patient in internal^external format.

> (e.g., 2870213.0915^FEB 13,1987@

> 09:15)

VAIN(8) The ADMISSION TYPE for the

> patient in internal^external format.

> (e.g., 3^DIRECT)

VAIN(9) The ADMITTING DIAGNOSIS for the

> patient. (e.g., PSYCHOSIS)

> VAIN(10) The internal entry number of the PTF

> record corresponding to this admission. (e.g., 2032)

VAIN(11) The ATTENDING PHYSICIAN in

> internal^external format.

> (e.g., 25^IRTPHYSICIAN,TEN)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

8\. IN5^VADPT

This entry point will return data related to an inpatient episode.

Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAIP(1) would be VAIP("MN"))

> 2 -- return the output in the ^UTILITY

> global with numeric subscripts

> (e.g., ^UTILITY("VAIP",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAIP",\$J,"MN")

VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGI5")

VAIP("D") This optional variable can be defined

> as follows.

> VAIP("D")=VA FileManager date in internal format.

> If the patient was an inpatient at the date/time passed, movement data pertaining to that date/time will be returned.

> VAIP("D")="LAST"

> Movement data pertaining to the last movement on file, regardless if patient is a current inpatient.

> VAIP("D")=valid date without time

> Will return movement data if patient was an inpatient at any time during the day on the date that was passed in.

> VAIP("D") - not passed

> Will return movement data if the patient was in inpatient based on "now".

VAIP("L") This optional variable, when passed,

> will include lodgers movements in the data. (e.g., VAIP("L")="")

VAIP("V") Can be defined as the variable used

> instead of VAIP(.

> (e.g., VAIP("V")="SD")

VAIP("E") This optional variable is defined as

> the internal file number of a specific movement. If this is defined, VAIP("D") is ignored.

> (e.g., VAIP("E")=123445)

VAIP("M") This optional variable can be passed

> as a "1" or a "0" (or null).

> VAIP("M")=0 - The array returned will be based on the admission movement associated with the movement date/time passed.

> VAIP("M")=1 - The array returned will be based on the last movement associated with the date/time passed.

Output: VAIP(1) The INTERNAL FILE NUMBER

> \[IFN\] of the movement found for the specified date/time. (e.g., 231009)

VAIP(2) The TRANSACTION TYPE of the

> movement in internal^external format where:

> 1=admission

> 2=transfer

> 3=discharge

> 4=check-in lodger

> 5=check-out lodger

> 6=specialty transfer

> (e.g., 3^DISCHARGE)

VAIP(3) The MOVEMENT DATE/TIME in

> internal^external date format.

> (e.g., 2880305.09^MAR 5,1988@09:00)

VAIP(4) The TYPE OF MOVEMENT in

> internal^external format.

> (e.g., 4^INTERWARD TRANSFER)

VAIP(5) The WARD LOCATION to which

> patient was assigned with that movement in internal^external format. (e.g., 32^1B-SURG)

VAIP(6) The ROOM-BED to which the patient

> was assigned with that movement in internal^external format.

> (e.g., 88^201-01)

VAIP(7) The PRIMARY CARE PHYSICIAN

> assigned to the patient in internal^

> external format. (e.g., 3^IRTPHYSICIAN,ONE)

VAIP(8) The TREATING SPECIALTY

> assigned with that movement in internal^external format.

> (e.g., 98^OPTOMETRY)

> VAIP(9) The DIAGNOSIS assigned with that

> movement.

> (e.g., UPPER GI BLEEDING)

VAIP(10) This will return a "1" in the first piece

> if the patient is in a bed status; otherwise, a "0" will be returned. A non-bed status is made based on the last transfer type, if one exists, and a transfer to a non-bed status, (i.e., authorized absence, unauthorized absence, etc.) The second piece will contain the name of the last transfer type should one exist.

> (e.g., 1^FROM AUTHORIZED ABSENCE)

VAIP(11) If patient is in an absence status on

> the movement date/time, this will return the EXPECTED RETURN DATE from absence in internal^external format.

> (e.g., 2880911^SEP 11,1988)

> VAIP(12) The internal entry number of the PTF

> record corresponding to this

> admission. (e.g., 2032)

VAIP(13) The INTERNAL FILE NUMBER of

> the admission associated with this movement. (e.g., 200312)

VAIP(13,1) The MOVEMENT DATE/TIME in

> internal^external format.

> (e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(13,2) The TRANSACTION TYPE in

> internal^external format.

> (e.g., 1^ADMISSION)

VAIP(13,3) The MOVEMENT TYPE in

> internal^external format.

> (e.g., 15^DIRECT)

VAIP(13,4) The WARD LOCATION associated

> with this patient with this movement in internal^external format.

> (e.g., 5^7BSCI)

VAIP(13,5) The PRIMARY CARE PHYSICIAN

> assigned to the patient for this movement in internal^external format. (e.g., 16^IRTPHYSICIAN,FOUR)

VAIP(13,6) The TREATING SPECIALTY for the

> patient for this movement in internal^external format.

> (e.g., 3^NEUROLOGY)

VAIP(14) The INTERNAL FILE NUMBER of

> the last movement associated with this movement.

> (e.g., 187612)

VAIP(14,1) The MOVEMENT DATE/TIME in

> internal^external format.

> (e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(14,2) The TRANSACTION TYPE in

> internal^external format.

> (e.g., 2^TRANSFER)

VAIP(14,3) The MOVEMENT TYPE in internal^

> external format.

> (e.g., 4^INTERWARD TRANSFER)

VAIP(14,4) The WARD LOCATION associated

> with this patient with this movement in internal^external format.

> (e.g., 5^7BSCI)

VAIP(14,5) The PRIMARY CARE PHYSICIAN

> assigned to the patient for this movement in internal^external format.

> (e.g., 16^IRTPHYSICIAN,ONE)

VAIP(14,6) The TREATING SPECIALTY for the

> patient for this movement in internal^external format.

> (e.g., 3^NEUROLOGY)

VAIP(15) The INTERNAL FILE NUMBER of

> the movement which occurred immediately prior to this one, if one exists. (e.g., 153201)

VAIP(15,1) The MOVEMENT DATE/TIME in

> internal^external format.

> (e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(15,2) The TRANSACTION TYPE in

> internal^external format.

> (e.g., 2^TRANSFER)

VAIP(15,3) The MOVEMENT TYPE in internal^

> external format.

> (e.g., 4^INTERWARD TRANSFER)

VAIP(15,4) The WARD LOCATION associated

> with this patient with this movement in internal^external format.

> (e.g., 5^7BSCI)

VAIP(15,5) The PRIMARY CARE PHYSICIAN

> assigned to the patient for this movement in internal^external format.

> (e.g., 16^IRTPHYSICIAN,TEN)

VAIP(15,6) The TREATING SPECIALTY for the

> patient for this movement in internal^external format.

> (e.g., 3^NEUROLOGY)

VAIP(16) The INTERNAL FILE NUMBER of

> the movement which occurred immediately following this one, if one exists. (e.g., 146609)

VAIP(16,1) The MOVEMENT DATE/TIME in

> internal^external format.

> (e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(16,2) The TRANSACTION TYPE in

> internal^external format.

> (e.g., 2^TRANSFER)

VAIP(16,3) The MOVEMENT TYPE in internal^

> external format.

> (e.g., 4^INTERWARD TRANSFER)

VAIP(16,4) The WARD LOCATION associated

> with this patient with this movement in internal^external format.

> (e.g., 5^7BSCI)

VAIP(16,5) The PRIMARY CARE PHYSICIAN

> assigned to the patient for this movement in internal^external format.

> (e.g., 16^IRTPHYSICIAN,TEN)

VAIP(16,6) The TREATING SPECIALTY for the

> patient for this movement in internal^external format.

> (e.g., 3^NEUROLOGY)

VAIP(17) The INTERNAL FILE NUMBER of

> the discharge associated with this movement. (e.g., 1902212)

VAIP(17,1) The MOVEMENT DATE/TIME in

> internal^external format.

> (e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(17,2) The TRANSACTION TYPE in

> internal^external format.

> (e.g., 3^DISCHARGE)

VAIP(17,3) The MOVEMENT TYPE in internal^

> external format.

> (e.g., 16^REGULAR)

VAIP(17,4) The WARD LOCATION associated

> with this patient for this movement in internal^external format.

> (e.g., 5^7BSCI)

VAIP(17,5) The PRIMARY CARE PHYSICIAN

> assigned to the patient for this movement in internal^external format.

> (e.g., 16^IRTPHYSICIAN,ONE)

VAIP(17,6) The TREATING SPECIALTY for the

> patient for this movement in internal^external format.

> (e.g., 3^NEUROLOGY)

VAIP(18) The ATTENDING PHYSICIAN

> assigned to the patient for this movement in internal^external format.

> (e.g., 25^IRTPHYSICIAN,FOUR)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

9\. OPD^VADPT

Returns other pertinent patient data which is commonly used but not contained in any other calls to VADPT.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAHOW This optional variable can be set to a

> requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

> 1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAPD(1) would be VAPD("BC"))

> 2 -- return the output in the ^UTILITY global with numeric subscripts

> (e.g., ^UTILITY("VAPD",\$J,1))

> 12 -- return the output in the ^UTILITY global with alpha subscripts

> (e.g., ^UTILITY("VAPD",\$J,"BC")

VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGPD")

Output: VAPD(1) The PLACE OF BIRTH \[CITY\].

> (e.g., SAN FRANCISCO)

VAPD(2) The PLACE OF BIRTH \[STATE\] in

> internal^external format.

> (e.g., 6^CALIFORNIA)

> VAPD(3) The FATHER'S NAME.

> (e.g., IRTFATHER,ONE)

> VAPD(4) The MOTHER'S NAME.

> (e.g., MARY)

> VAPD(5) The MOTHER'S MAIDEN NAME.

> (e.g., IRTMOTHER,ONE)

> VAPD(6) The patient's OCCUPATION.

> (e.g., CARPENTER)

VAPD(7) The patient's EMPLOYMENT

> STATUS in internal^external format.

> (e.g., 4^SELF EMPLOYED)

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

10\. REG^VADPT

Returns REGISTRATION/DISPOSITION data.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAROOT This optional variable can be set to a

> local variable or global name in which to return the output.

> (e.g., VAROOT="DGADD")

VARP("F") Can be defined as the "from" date for

> which registrations are desired. This must be passed as a valid VA File-Manager date.

> (e.g., VARP("F")=2930101)

VARP("T") Can be defined as the "to" date for

> which registrations are desired. This must be passed as a valid VA File-Manager date. If neither VARP("F") nor VARP("T") are defined, all registrations will be returned.

> (e.g., VARP("T")=2930530)

VARP("C") Can be defined as the number of

> registrations you want returned in the array.

> (e.g., VARP("C")=5 - will return 5 most recent)

> Output: ^UTILITY("VARP",\$J,#,"I") Internal format

> ^UTILITY("VARP",\$J,#,"E") External format

> Piece 1 Registration Date/Time

> Piece 2 Status

> Piece 3 Type of Benefit applied

> for

> Piece 4 Facility Applying to

> Piece 5 Who Registered

> Piece 6 Log out (disposition)

> date/time

> Piece 7 Disposition Type

> Piece 8 Who Dispositioned

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

11\. SDE^VADPT

Returns ACTIVE clinic enrollments for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> Output: ^UTILITY("VAEN",\$J,#,"I") Internal format

> ^UTILITY("VAEN",\$J,#,"E") External format

> Piece 1 Clinic Enrolled in

> Piece 2 Enrollment Date

> Piece 3 OPT or AC

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

12\. SDA^VADPT

Returns APPOINTMENT DATE/TIME data for a patient.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

> VASD("T") Can be defined as the "to" date for

> which registrations are desired. This must be passed as a valid VA File-Manager date. If neither VASD("F") nor VASD("T") are defined, all future appointments will be returned.

> VASD("F") Can be defined as the "from" date for

> which appointments are desired. This must be passed as a valid VA File-Manager date. If not defined, it is assumed only future appointments should be returned.

> VASD("W") Can be passed as the specific STATUS

> desired in the following format. If not passed, only those appointments which are still scheduled (or kept in the event of a past date) for both inpatients and outpatients will be returned.

If VASD("W")

> <u>Contains a</u> <u>These appts. are returned</u>

> 1 Active/Kept

> 2 Inpatient appts. only

> 3 No-shows

> 4 No-shows, auto-rebook

> 5 Cancelled by Clinic

> 6 Cancelled by Clinic, auto

> rebook

> 7 Cancelled by Patient

> 8 Cancelled by Patient,

> auto rebook

> 9 No action taken

> VASD("C",Clinic IFN)

> Can be set up to contain only those internal file entries from the HOSPITAL LOCATION file for clinics which you would like to see appointments for this particular patient. You may define this array with just one clinic or with many. If you do not define this variable, it will be assumed that you want appointments for this patient in all clinics returned.

> Output: ^UTILITY("VASD",\$J,#,"I") Internal format

> ^UTILITY("VASD",\$J,#,"E") External format

> Piece 1 Date/Time of Appointment

> Piece 2 Clinic

> Piece 3 Status

> Piece 4 Appointment Type

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

13\. PID^VADPT

This call is used to obtain the patient identifier in long and brief format.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAPTYP This optional variable can be set to the

> internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, DOD, or IHS through the eligibility. If this variable is not defined or the eligibility does not exist, the VA patient IDs will be returned.

> Output: VA("PID") The long patient identifier.

> (e.g., 111-22-3333P)

> VA("BID") The short patient identifier.

> (e.g., 3333P)

> VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

14\. PID^VADPT6

This call returns the same variables as the call mentioned above, but will eliminate the unnecessary processing time required calling PID^VADPT.

15\. ADM^VADPT2

This returns the internal file number of the admission movement. If VAINDT is not defined, this will use "NOW" for the date/time.

> Input: DFN This required variable is the internal

> entry number in the PATIENT file.

VAINDT This optional variable may be set to a

> past date/time for which the programmer wishes to know the patient's inpatient status. This must be passed as an internal VA FileManager date/time format.

> (e.g., 2880101.08)

> Output: VADMVT Returns the internal file number of

> the admission movement.

VAERR The error flag will have one of the

> following values.

> 0 -- no errors encountered

> 1 -- error encountered - DFN or

> ^DPT(DFN,0) is not defined

16\. KVAR^VADPT

This call is used to remove all variables defined by the VADPT routine. The programmer should elect to utilize this call to remove the arrays which were returned by VADPT.

17\. KVA^VADPT

This call is used as above and will also kill the VA("BID") and VA("PID") variables.

18\. COMBINATIONS

The following calls may be made to return a combination of arrays with a single call.

Input: DFN This required variable is the internal

> entry number in the PATIENT file.

See specific call for other variable input

Output:

|      |             |             |           |           |         |         |          |                |                |                |
|------|-------------|-------------|-----------|-----------|---------|---------|----------|----------------|----------------|----------------|
|      | DEMOGRAPHIC | ELIGIBILITY | INPATIENT | INPATIENT | ADDRESS | SERVICE | MONETARY | REGISTRATION   | ENROLLMENT     | APPOINTMENT    |
| CALL | VADM        | VAEL        | VAIN      | VAIP      | VAPA    | VASV    | VAMB     | UTILITY("VARP" | UTILITY("VAEN" | UTILITY("VASD" |
| OERR | X       |             | X     |           |         |         |          |                |                |                |
| 1    | X       |             | X     |           |         |         |          |                |                |                |
| 2    | X       | X       |           |           |         |         |          |                |                |                |
| 3    |             | X       | X     |           |         |         |          |                |                |                |
| 4    | X       |             |           |           | X   |         |          |                |                |                |
| 5    |             |             | X     |           | X   |         |          |                |                |                |
| 6    | X       | X       |           |           | X   |         |          |                |                |                |
| 7    |             | X       |           |           |         | X   |          |                |                |                |
| 8    |             | X       |           |           |         | X   | X    |                |                |                |
| 9    | X       |             |           |           |         |         |          | X          | X          | X          |
| 10   |             |             |           |           |         |         |          |                | X          | X          |
| 51   | X       |             |           | X     |         |         |          |                |                |                |
| 52   |             | X       |           | X     |         |         |          |                |                |                |
| 53   |             |             |           | X     | X   |         |          |                |                |                |
| ALL  | X       | X       | X     |           | X   | X   | X    | X          | X          | X          |
| A5   | X       | X       |           | X     | X   | X   | X    | X          | X          | X          |

Alpha Subscripts

|               |              |                       |
|---------------|--------------|-----------------------|
| Call      | Variable | Alpha Translation |
| DEM^VADPT | VADM(1)      | VADM("NM")            |
|               | VADM(2)      | VADM("SS")            |
|               | VADM(3)      | VADM("DB")            |
|               | VADM(4)      | VADM("AG")            |
|               | VADM(5)      | VADM("SX")            |
|               | VADM(6)      | VADM("EX")            |
|               | VADM(7)      | VADM("RE")            |
|               | VADM(8)      | VADM("RA")            |
|               | VADM(9)      | VADM("RP")            |
|               | VADM(10)     | VADM("MS")            |

|                |           |              |
|----------------|-----------|--------------|
| ELIG^VADPT | VAEL(1)   | VAEL("EL")   |
|                | VAEL(1,#) | VAEL("EL",#) |
|                | VAEL(2)   | VAEL("PS")   |
|                | VAEL(3)   | VAEL("SC")   |
|                | VAEL(4)   | VAEL("VT")   |
|                | VAEL(5)   | VAEL("IN")   |
|                | VAEL(5,#) | VAEL("IN",#) |
|                | VAEL(6)   | VAEL("TY")   |
|                | VAEL(7)   | VAEL("CN")   |
|                | VAEL(8)   | VAEL("ES")   |
|                | VAEL(9)   | VAEL("MT")   |

|              |         |            |
|--------------|---------|------------|
| MB^VADPT | VAMB(1) | VAMB("AA") |
|              | VAMB(2) | VAMB("HB") |
|              | VAMB(3) | VAMB("SS") |
|              | VAMB(4) | VAMB("PE") |
|              | VAMB(5) | VAMB("MR") |
|              | VAMB(6) | VAMB("SI") |
|              | VAMB(7) | VAMB("DI") |
|              | VAMB(8) | VAMB("OR") |
|              | VAMB(9) | VAMB("GI") |

|               |              |                       |
|---------------|--------------|-----------------------|
| Call      | Variable | Alpha Translation |
| SVC^VADPT | VASV(1)      | VASV("VN")            |
|               | VASV(1,#)    | VASV("VN",#)          |
|               | VASV(2)      | VASV("AO")            |
|               | VASV(2,#)    | VASV("AO",#)          |
|               | VASV(3)      | VASV("IR")            |
|               | VASV(3,#)    | VASV("IR",#)          |
|               | VASV(4)      | VASV("PW")            |
|               | VASV(4,#)    | VASV("PW",#)          |
|               | VASV(5)      | VASV("CS")            |
|               | VASV(5,#)    | VASV("CS",#)          |
|               | VASV(6)      | VASV("S1")            |
|               | VASV(6,#)    | VASV("S1",#)          |
|               | VASV(7)      | VASV("S2")            |
|               | VASV(7,#)    | VASV("S2",#)          |
|               | VASV(8)      | VASV("S3")            |
|               | VASV(8,#)    | VASV("S3",#)          |
|               | VASV(9)      | VASV(“PH”)            |
|               | VASV(9,#)    | VASV(“PH”,#)          |

|               |          |            |
|---------------|----------|------------|
| ADD^VADPT | VAPA(1)  | VAPA("L1") |
|               | VAPA(2)  | VAPA("L2") |
|               | VAPA(3)  | VAPA("L3") |
|               | VAPA(4)  | VAPA("CI") |
|               | VAPA(5)  | VAPA("ST") |
|               | VAPA(6)  | VAPA("ZP") |
|               | VAPA(7)  | VAPA("CO") |
|               | VAPA(8)  | VAPA("PN") |
|               | VAPA(9)  | VAPA("TS") |
|               | VAPA(10) | VAPA("TE") |
|               | VAPA(11) | VAPA("Z4") |

|               |              |                       |
|---------------|--------------|-----------------------|
| Call      | Variable | Alpha Translation |
| OAD^VADPT | VAOA(1)      | VAOA("L1")            |
|               | VAOA(2)      | VAOA("L2")            |
|               | VAOA(3)      | VAOA("L3")            |
|               | VAOA(4)      | VAOA("CI")            |
|               | VAOA(5)      | VAOA("ST")            |
|               | VAOA(6)      | VAOA("ZP")            |
|               | VAOA(7)      | VAOA("CO")            |
|               | VAOA(8)      | VAOA("PN")            |
|               | VAOA(9)      | VAOA("NM")            |
|               | VAOA(10)     | VAOA("RE")            |
|               | VAOA(11)     | VAOA("Z4")            |

|               |          |            |
|---------------|----------|------------|
| INP^VADPT | VAIN(1)  | VAIN("AN") |
|               | VAIN(2)  | VAIN("DR") |
|               | VAIN(3)  | VAIN("TS") |
|               | VAIN(4)  | VAIN("WL") |
|               | VAIN(5)  | VAIN("RB") |
|               | VAIN(6)  | VAIN("BS") |
|               | VAIN(7)  | VAIN("AD") |
|               | VAIN(8)  | VAIN("AT") |
|               | VAIN(9)  | VAIN("AF") |
|               | VAIN(10) | VAIN("PT") |
|               | VAIN(11) | VAIN("AP") |

|               |              |                       |
|---------------|--------------|-----------------------|
| Call      | Variable | Alpha Translation |
| IN5^VADPT | VAIP(1)      | VAIP("MN")            |
|               | VAIP(2)      | VAIP("TT")            |
|               | VAIP(3)      | VAIP("MD")            |
|               | VAIP(4)      | VAIP("MT")            |
|               | VAIP(5)      | VAIP("WL")            |
|               | VAIP(6)      | VAIP("RB")            |
|               | VAIP(7)      | VAIP("DR")            |
|               | VAIP(8)      | VAIP("TS")            |
|               | VAIP(9)      | VAIP("MF")            |
|               | VAIP(10)     | VAIP("BS")            |
|               | VAIP(11)     | VAIP("RD")            |
|               | VAIP(12)     | VAIP("PT")            |
|               | VAIP(13)     | VAIP("AN")            |
|               | VAIP(13,#)   | VAIP("AN",#)          |
|               | VAIP(14)     | VAIP("LN")            |
|               | VAIP(14,#)   | VAIP("LN",#)          |
|               | VAIP(15)     | VAIP("PN")            |
|               | VAIP(15,#)   | VAIP("PT",#)          |
|               | VAIP(16)     | VAIP("NN")            |
|               | VAIP(16,#)   | VAIP("NN",#)          |
|               | VAIP(17)     | VAIP("DN")            |
|               | VAIP(17,#)   | VAIP("DN",#")         |
|               | VAIP(18)     | VAIP("AP")            |

|               |         |            |
|---------------|---------|------------|
| OPD^VADPT | VAPD(1) | VAPD("BC") |
|               | VAPD(2) | VAPD("BS") |
|               | VAPD(3) | VAPD("FN") |
|               | VAPD(4) | VAPD("MN") |
|               | VAPD(5) | VAPD("MM") |
|               | VAPD(6) | VAPD("OC") |
|               | VAPD(7) | VAPD("ES") |

#