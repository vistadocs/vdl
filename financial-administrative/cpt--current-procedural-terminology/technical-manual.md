---
title: CPT Version 6 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: CPT
app_name: Current Procedural Terminology
section: FIN
app_status: active
pkg_ns: CPT
patch_ver: 6
patch_id: CPT*6
group_key: "CPT:CPT:6"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Extrinsic Function Calls](#extrinsic-function-calls) Current Procedural Terminology (CPT)V. 6.0 Technical ManualMay 1997IntroductionImplementation and Maintenance > Integrity Checker Routines > Callable Routines > Routines to Map > Routine List Files > Globals to Journal > File List > Templates >
audience: 
keywords: 
  - code
  - package
  - routines
  - files
  - routine
  - codes
  - print
  - fileman
  - options
  - icpt
page_count: 0
word_count: 1457
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=33"
---

## Table of Contents

  - [Extrinsic Function Calls](#extrinsic-function-calls)
Current Procedural Terminology (CPT)V. 6.0 Technical ManualMay 1997IntroductionImplementation and Maintenance
> Integrity Checker
Routines
> Callable Routines
> Routines to Map
> Routine List
Files
> Globals to Journal
> File List
> Templates
> File Flow (Relationships between files)
Exported Options
> Menu Diagrams
> Exported Options
Archiving and PurgingExternal/Internal Relations
> DBIA Agreements
Package-wide Variables
> SACC Exemptions/Non-Standard Code
How to Generate On-Line DocumentationSecurity
> General Security
> Security Keys
> Legal Requirements
> VA FileMan Access Codes
Glossary
Introduction
Current Procedural Terminology (CPT) codes are used for reporting medical services and procedures performed by physicians. Their purpose is to provide a uniform language that will accurately describe medical, surgical, and diagnostic services, thereby providing an effective means for reliable nationwide communication among physicians, patients, and third parties. This system of terminology is the most widely accepted nomenclature for the reporting of physician procedures and services under government and private health insurance programs.
CPT V. 6.0 provides the software to update the CPT files. The software includes all CPT codes to code outpatient services for reimbursement and workload purposes (as determined by the American Medical Association) and the Common Procedure Coding System from the Health Care Financing Administration (HCPCS). These codes may also be utilized to report inpatient services in certain instances.
The CPT Technical Manual has been divided into major sections for easy use and is intended to be a reference document. While you are free to review the entire document, it is best used by selecting specific sections which contain the information sought for a particular need.
Implementation and Maintenance
There are no site-configurable features connected with the CPT package.
Total disk space requirements for the ICPT global is 23.3 megabytes.
Integrity Checker
CPT V. 6.0 uses the KIDS integrity checker. Under the installation option of the Kernel Installation Distribution System Menu, select “Verify Checksums in Transport Global” to ensure that the routines are correct.
Routines
Callable Routines
Listed below are the available APIs.

## Extrinsic Function Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPT Code Basic Information

\$\$CPT^ICPTCOD(CODE,CDT,SRC,DFN)

> Input: CODE - CPT/HCPCS code, internal or external format (Required)

> CDT - date to check status for, FileMan format (default =

> TODAY)

> If CDT is prior to 1/1/1989, 1/1/1989 will be used

> If CDT is year only, the first of that year will be used

> If CDT is month and year only, the first of the month

> will be used

> If CDT is later than today, validation will be performed

> using the newest activation and inactivation dates

> SRC - screen source

> If '\$G(SRC), check Level I and II codes only

> If \$G(SRC), check Level I, II, and III codes

> DFN - not in use but included in anticipation of future need

> Output: string: ien^CPT code^short name^category ien^source^effective

> date^status^inactivation date^activation date^msg

> where the pieces are:

> 1 internal entry number of code in ^ICPT

> 2 CPT CODE (.01 field)

> 3 SHORT NAME (#2 field)

> 4 CATEGORY ien (#3 field)

> 5 SOURCE code (#6 field) C:CPT; H:HCPCS; L:VA LOCAL

> 6 EFFECTIVE DATE (from field \#60 multiple)

> 7 STATUS (from .02 of \#60 multiple) where 0:inactive; 1:active

> 8 INACTIVATION DATE (from .01 of \#60 multiple)

> 9 ACTIVATION DATE (from .01 of \#60 multiple)

> 10 MSG (a message stating: CODE TEXT MAY BE INACCURATE)

> or

> -1^error description

CPT Code Long Description

\$\$CPTD^ICPTCOD(CODE,OUTARR,DFN,CDT)

> Input: CODE - CPT/HCPCS code, internal or external format (Required)

> OUTARR - array name to store description (default =

> ^TMP("ICPTD",\$J))

> DFN - not in use but included in anticipation of future need

> CDT - date to screen against - not used currently, included in

> anticipation of future need, FileMan format (default =

> TODAY)

> If CDT is prior to 1/1/1989, 1/1/1989 will be used

> If CDT is year only, the first of that year will be used

> If CDT is month and year only, the first of the month

> will be used

> If CDT is later than today, TODAY will be used

> Output: \# - number of lines in description

> @OUTARR(1:n) - description (lines 1 through n)

> @OUTARR(n+1) - blank

> @OUTARR(n+1) - a message stating: CODE TEXT MAY BE INACCURATE

> or

> -1^error description

Modifiers for a Code

\$\$CODM^ICPTCOD(CODE,OUTARR,SRC,CDT,DFN)

> Input: CODE = CPT/HCPCS code, internal or external format (Required)

> OUTARR = array name for list returned (default =

> ^TMP(“ICPTM”,\$J))

> SRC = source screen

> If 0 or Null, check Level I and II code/modifiers only

> If \>0, check Level I, II, and III code/modifiers

> CDT = date to check modifier status, Fileman format

> If 0 or Null, return all the modifiers for a code

> Else return only modifiers active on the date of CDT

> If CDT is prior to 1/1/1989, 1/1/1989 will be used

> If CDT is year only, the first of that year will be used

> If CDT is month and year only, the first of the month

> will be used

> If CDT is later than today, validation will be performed

> using the newest activation and inactivation dates

> DFN = not in use but included in anticipation of future need

> Output: \# of modifiers that apply

> OUTARR array in the format: OUTARR(mod) = name^mod ien

> (mod is the .01 field)

> or

> -1^error description

Modifier Basic Information

\$\$MOD^ICPTMOD(MOD,MFT,MDT,SRC,DFN)

> Input: MOD - modifier, internal or external format (Required)

> MFT - modifier format

> "I" = ien

> "E" = .01 field (Defualt)

> MDT - date to check status for, FileMan format (default =

> TODAY)

> If MDT is prior to 1/1/1989, 1/1/1989 will be used

> If MDT is year only, the first of that year will be used

> If MDT is month and year only, the first of the month

> will be used

> If MDT is later than today, validation will be performed

> using the newest activation and inactivation dates

> SRC - source screen

> If 0 or Null, check Level I and II modifiers only

> If \>0, check Level I, II, and III modifiers

> DFN - not in use but included in anticipation of future need

> Output: String: ien^modifier^name^code^source^effective date^status

> ^inactivation date^activation date^msg

> where the pieces are:

> 1 internal entry number

> 2 MODIFIER (.01 field)

> 3 NAME (.02 field)

> 4 CODE (.03 field) alternate 5-digit code for CPT modifiers

> 5 SOURCE (.04 field) C:CPT; H:HCPCS; V:VA NATIONAL

> 6 EFFECTIVE DATE (from multiple field 60)

> 7 STATUS (.02 field of multiple field 60) where 0:inactive;

> 1:active

> 8 INACTIVATION DATE (from .01 of \#60 multiple)

> 9 ACTIVATION DATE (from .01 of \#60 multiple)

> 10 MSG (a message stating: CODE TEXT MAY BE INACCURATE)

> or

> -1^error description

Code/Modifier Pairs

\$\$MODP^ICPTMOD(CODE,MOD,MFT,MDT,SRC,DFN)

> Input: CODE - CPT/HCPCS code, internal or external format (Required)

> MOD - modifier, internal or external format (Required)

> MFT - modifier format

> "I" = ien

> "E" = .01 field (Default)

> MDT - date to check against, FileMan format (default = TODAY)

> If MDT is prior to 1/1/1989, 1/1/1989 will be used

> If MDT is year only, the first of that year will be used

> If MDT is month and year only, the first of the month

> will be used

> If MDT is later than today, validation will be performed

> using the newest activation and inactivation dates

> SRC - source screen.

> If 0 or Null, check Level I and II code/modifiers only

> If \>0, check Level I, II, and III code/modifiers

> DFN - not in use but included in anticipation of future need

> Output: 0, if pair is unacceptable

> or

> IEN in 81.3^MODIFIER name (.02 field), if pair is acceptable

> or

> -1^error message

Code’s IEN

\$\$CODEN^ICPTCOD(CODE)

> Input: CODE - CPT/HCPCS code (Required)

> Output: ien of code

IEN’s Code

\$\$CODEC^ICPTCOD(CODE)

> Input: CODE - ien of CPT/HCPCS code (Required)

> Output: CPT/HCPCS code

Code Status Check

\$\$STATCHK^ICPTAPIU(CODE,CDT)

> Input: CODE - CPT/HCPCS code, or Modifier (Required)

> CDT - date to check status for, FileMan format (default =

> TODAY)

> If CDT is prior to 1/1/1989, 1/1/1989 will be used

> If CDT is year only, the first of that year will be used

> If CDT is month and year only, the first of the month

will be used

> If CDT is later than today, validation will be performed

> using the newest activation and inactivation dates

> Output: string: status^ien

> where the pieces are:

> 1 0:inactive; 1:active

> 2 internal entry number of code in ^ICPT or ^DIC(81.3,

> or

> 0^–1 if not found

Code Activation History

\$\$HIST^ICPTAPIU(CODE,ARY)

> Input: CODE - CPT/HCPCS code, or Modifier (Required)

> ARY - Array, (passed by Reference)

> Output: Returns ARY(0) or –1 if error

> ARY(0) = Number of Activation History Entries

> ARY(\<date\>) = STATUS, where 0:inactive; 1:active

> ARY("IEN") = internal entry number of code in ^ICPT or

> ^DIC(81.3,

Previous Code/Modifier

\$\$PREV^ICPTAPIU(CODE)

> Input: CODE - CPT/HCPCS code, or Modifier (Required)

> Output: Returns previous code/modifier (whether active or inactive)

> or

> "" if a previous code/modifier is not found

Next Code/Modifier

\$\$NEXT^ICPTAPIU(CODE)

> Input: CODE - CPT/HCPCS code, or Modifier (Required)

> Output: Returns next code/modifier (whether active or inactive)

> or

> "" if a next code/modifier is not found

Activation/Inactivation Period

PERIOD^ICPTAPIU(CODE,ARY)

> Input: CODE - CPT/HCPCS code, or Modifier (Required)

> ARY - Array, (passed by Reference)

> Output: ARY(0) = string: ien^selectable

> where the pieces are:

> 1 internal entry number of code in ^ICPT or ^DIC(81.3,

> 2 0:unselectable; 1:selectable

> ARY(activation date) = inactivation date^short text

> where short text is:

> SHORT NAME (#2 field) for CPT/HCPCS codes

> NAME (#.02 field) for Code Modifiers

Category Name

\$\$CAT^ICPTAPIU(CAT,DFN)

> Input: CAT - category ien (Required)

> DFN - not in use but included in anticipation of future need

> Output: String: CATEGORY NAME^SOURCE (C or H)^MAJOR CATEGORY IEN^MAJOR CATEGORY NAME

> or

> -1^error message

Codes Distribution Date

\$\$CPTDIST^ICPTAPIU

> Input: none

> Output: DISTRIBUTION DATE of current CPT

Copyright Information

\$\$COPY^ICPTAPIU

> Input: none

> Output: CPT copyright information

Routines to Map

The ICPT routines are not recommended for mapping.

Routine List

Steps to obtain routines contained in the CPT package.

1\. Programmer Options Menu

2\. Routine Tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: ICPT\*  
Files

The CPT data dictionaries may not be modified. The file descriptions of these files will be so noted.

Globals to Journal

There are no globals to journal in the CPT package.

File List

<u>File \#</u> <u>File Name</u> <u>Global</u>

81 CPT ^ICPT(

81.1 CPT CATEGORY ^DIC(81.1,

81.2 CPT COPYRIGHT ^DIC(81.2,

81.3 CPT MODIFIER ^DIC(81.3,

The following are the steps you may take to obtain information concerning the files and templates contained in the CPT package.

Templates

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: Print TemplateSort Template

4\. Sort by: Name

5\. Start with name: ICPT

6\. Within name, sort by: \<RET\>

7\. First print field: NameFile Flow (Relationships between files)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

Exported Options

The following are the steps you may take to obtain information concerning the menus and exported options contained in the CPT package.

Menu Diagrams

1\. Programmers Options

2\. Menu Management Menu

3\. Display Menus and Options Menu

4\. Diagram Menus

5\. Select User or Option Name: ICPT OUTPUT MENUExported Options

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: OPTION

4\. Sort by: Name

5\. Start with name: ICPT

6\. Within name, sort by: \<RET\>

7\. First print field: Name

Archiving and Purging

Archiving and purging capabilities are not applicable as the data is a national table.

External/Internal Relations

Minimums of VA FileMan V. 21.0, Kernel V. 8.0, PCE V. 1.0, and PIMS (MAS) V. 5.3 are required to run this package.

DBIA Agreements

The following are the steps you may take to obtain the database integration agreements for the CPT package.

DBIA Agreements - Custodial Package

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Custodial Package Menu

5\. Active by Custodial Package Option

6\. Select Package Name: CPTDBIA Agreements - Subscriber Package

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Subscriber Package Menu

5\. Print Active by Subscriber Package Option

6\. Start with subscriber package: CPT

Package-wide Variables

There are no package-wide variables in the CPT package.

SACC Exemptions/Non-Standard Code

There are no SACC exemptions/non-standard code in the CPT package.

How to Generate On-Line Documentation

This section describes some of the various methods by which users may secure CPT technical documentation. On-line technical documentation pertaining to the CPT software, in addition to that which is located in the help prompts, may be generated through utilization of several Kernel options. These include XINDEX and VA FileMan List File Attributes. Further information about other utilities which supply on-line technical documentation may be found in the Kernel Reference Manual.

XIndex

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to V*is*tA Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from V*is*tA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the CPT package, specify the following namespace at the "routine(s) ?\>" prompt: ICPT\*. CPT initialization routines which reside in the UCI in which XINDEX is being run, as well as local routines found within the CPT namespace, should be omitted at the "routine(s)?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

List File Attributes

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates. For a comprehensive listing of CPT files, please refer to the Files section of this manual.

Security

General Security

The CPT data dictionaries may not be modified. The file descriptions of these files will be so noted.

Security Keys

There are no security keys in the CPT package.

Legal Requirements

The CPT codes are an American Medical Association (AMA) copyrighted product. Their use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA.

Printing of any CPT information that will be released external to the VA (excluding areas of billing/fee basis processing, administrative management, clinical management including research, and patient coding/summarizing) must include the following notice: "CPT five-digit codes and/or descriptions only are copyright 1988 AMA (or such other date or publication of the work as defined in the Berne Implementation Act of 1988, formerly the Copyright Revision Act of 1976)."

VA FileMan Access Codes

Below is a list of recommended VA FileMan access codes associated with each file contained in the CPT package. This list may be used to assist in assigning users appropriate VA FileMan access codes.

File File DD RD WR DEL LAYGO

<u>Number</u> <u>Name</u> <u>Access</u> <u>Access</u> <u>Access</u> <u>Access</u> <u>Access</u>

81 CPT @ D @ @ @

81.1 CPT CATEGORY @ D @ @ @

81.2 CPT COPYRIGHT @ D @ @ @

81.3 CPT MODIFIER @ D @ @ @

Glossary

AMA American Medical Association

CPT Current Procedural Terminology

CPT Category Category name associated with a specified CPT code.

HCFA Health Care Financing Administration

HCPCS Health Care Financing Administration’s Common Procedure

Coding System

VISTA Veterans Health Information Systems and Technology

Architecture