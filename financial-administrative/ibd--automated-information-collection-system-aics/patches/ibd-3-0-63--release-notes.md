---
title: IBD*3.0*63 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: IBD
app_name: Automated Information Collection System (AICS)
section: FIN
app_status: active
pkg_ns: IBD
patch_ver: 3.0
patch_id: IBD*3.0*63
group_key: "IBD:IBD:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - codes
  - encounter
  - diagnosis
  - search
  - table
  - contents
  - report
  - form
  - selection
page_count: 0
word_count: 5521
section_count: 17
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/icd-10_rn_ibd_3_63.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/icd-10_rn_ibd_3_63.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

ICD-10 Follow On Class 1 Software Remediation Project

Automated Information Collection System (AICS)

Application Version 3.0

Release Notes

IBD\*3.0\*63

![](ibd-3-0-63-release-notes/001.png)

April 2014

Office of Information and Technology

Product Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [Encounter Forms Menu Option](#encounter-forms-menu-option)
  - [Edit Encounter Forms Option](#edit-encounter-forms-option)
  - [Edit Tool Kit Option](#edit-tool-kit-option)
  - [Reports and Utilities Option](#reports-and-utilities-option)
    - [Maintenance Utility for Active/Inactive Codes Report](#maintenance-utility-for-activeinactive-codes-report)
    - [ICD-10 Status Update Report](#icd-10-status-update-report)
- [Adding ICD-10 Blocks](#adding-icd-10-blocks)
  - [DEFAULTS Form](#defaults-form)
  - [Inactive Codes](#inactive-codes)
- [ICD-10 Search Functionality](#icd-10-search-functionality)
  - [ICD-10-CM Diagnosis Code Search](#icd-10-cm-diagnosis-code-search)
  - [ICD-10 Wildcard Search](#icd-10-wildcard-search)
- [Technical Information](#technical-information)
  - [Routines](#routines)
  - [Hardcoded Value](#hardcoded-value)
  - [Integration Control Registration](#integration-control-registration)
  - [Data Dictionary Changes](#data-dictionary-changes)
  - [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements that are contained in patch IBD\*3.0\*63 to the Automated Information Collection System (AICS) package.

This patch introduces the International Classification of Diseases, Tenth Revision (ICD-10) code set to replace the 30-year-old set of International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) that medical personnel have been using. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the ICD-9-CM code set with ICD-10-CM and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 Activation Date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch IBD\*3\*63 makes the following user-related changes to the AICS package:

- Added a new “Encounter Forms ICD-10 Update” report.
- A new menu item—Encounter Forms \> Reports and Utilities \> Encounter Forms ICD-10 Update—was introduced to run this report. This new report allows you to display a list of Encounter Forms and Clinics after making selections from several input options. When the report has been displayed, you may then update the ICD-10 Status field.
- Two date fields show the latest dates that the form was changed. The history fields contain the user ID (DUZ) of the person who last changed the files.
- Added ICD-10 Code selections in Encounter Forms and Maintenance Utility Active/Inactive Report.
- Added ICD-10 Code wildcard search help text, including a partial code wildcard search.
- The Replace Code option in the Maintenance Utility Report uses the approved standard Lexicon partial code search.
- The Problem List Package Interfaces are obsolete; therefore, the Problem List Package Interfaces are now Unavailable.
- User can now add or edit inactive codes on encounter forms, unless the code is currently INACTIVE because its last INACTIVE status date has been reached.

For technical information on changes for this patch, see [section 5](#technical-information).

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AICS user documentation is posted on the VistA Documentation Library (VDL) [Automated Information Collection System (AICS)](http://www.va.gov/vdl/application.asp?appid=30) page.

The following AICS manuals are updated with changes for IBD\*3\*63:

- Technical Manual
- User Manual

The following manual does not require changes for this patch:

- Installation Guide

The following manual does not exist for the AICS package:

- Security Guide

# Encounter Forms Menu Option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AICS package provides the ability to add, edit, enter and search ICD Diagnoses within more than one functional area. Changes for ICD-10 functionality pertain to editing Encounter Forms, editing the Tool Kit and updating the Maintenance Utility Report. Also, a new ICD-10 Status Update Report is now available from the *Reports and Utilities* option.

> **NOTE:** If you are editing Encounter Forms with Lexicon User Filters in place, those filters will be honored <u>with the exception of</u> editing an ICD-9 block or editing an ICD-10 block within the encounter form.  When editing ICD-9 blocks, you will be allowed to choose from any ICD-9 code; and when editing an ICD-10 block, you will be allowed to select any ICD-10 code, regardless of what Lexicon User Filters are in place.

Users will be prompted for whether they wish to enter Active or Inactive Diagnosis Codes for both code sets.

The AICS *Encounter Forms* menu below shows the options updated for ICD-10:

Current Encounter Forms Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>IBDF ENCOUNTER FORM Encounter Forms menu options:</p>
<p>EE Edit Encounter Forms ...</p>
<p>PR Print Options ...</p>
<p>PM Print Manager ...</p>
<p>TK Edit Tool Kit ...</p>
<p>DE AICS Data Entry Menu ...</p>
<p>RU Reports and Utilities ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** Existing ICD-9 functionality has not changed.

## Edit Encounter Forms Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When defining a form block, you now have the option to choose ICD-10 Diagnosis Codes in the TYPE OF DATA selection.

Editing a Form Block, Updated with ICD-10 Selection

EDITING A FORM BLOCK Feb 24, 2012@14:01:28 Page: 1 of 2

1 2 3 4 5 6 7

123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456

1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2 \| P S CODE ADD DIAGNOSIS

3 \| \| \| \| \|

4 \| \| \| \| \|

5 \| \| \| \| \|

6 \| \| \| \| \|

7 \| \| \| \| \|

8 \| \| \| \| \|

9 \| \| \| \| \|

10 \|

11 \| Diagnosis

12 \| \[ \] \[ \] \[ \]

13 \| P S ADD

14 \|

15 \|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\+ Enter ?? for more actions \>\>\>

You can create a \[N\]ew list, edit its \[A\]ppearance, \[D\]elete it,

edit its \[Co\]ntents, \[P\]osition or size its columns. Choose from:

\[N\]ew \[A\]ppearance \[D\]elete \[C\]ontents \[P\]osition: C// NEW

Select the TYPE OF DATA that the list will contain: DG

1 DG APPOINTMENT DISPOSITION TYPE=SELECTION

2 DG SELECT CPT PROCEDURE CODES TYPE=SELECTION

3 DG SELECT ICD-10 DIAGNOSIS CODES TYPE=SELECTION

4 DG SELECT ICD-9 DIAGNOSIS CODES TYPE=SELECTION

5 DG SELECT VISIT TYPE CPT PROCEDURES TYPE=SELECTION

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

## Edit Tool Kit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When defining a tool kit block, you now have the option to select ICD-10 Diagnoses.

Defining a Tool Kit Block, with ICD-10 Selection Displayed

EDIT TOOL KIT BLOCKS Feb 24, 2012@14:08:06 Page: 3 of 4

\+ BLOCK NAME TK# BRIEF DESCRIPTION

35 CLINICAL REMINDERS FULL (V3.0) 35 Clinical Reminders w/ full display of

36 CPT MODIFIER DISPLAY 36 Display CPT Modifiers (with sample mod

37 CPT MODIFIER DISPLY W/O SAMPLE 37 Display CPT Modifiers (without sample

38 BASIC DEMOGRAPHICS (MST) 38 Data fields - contains patient name,do

39 HIDDEN CLASSIFICATN (V2.1 MST) 39 Classifications for visit - not scanna

40 HIDDEN CLASSIFICATN (V3.0 MST) 40 Classifications for visit - scannable

41 HIDDEN SC TREATMNT QUEST (MST) 41 Data fields-questions on SC of treatme

42 HIDDEN SC/MST CLASSIFICATIONS 42 SC/MST classifications for visit - not

43 MST STATUS DISPLAY 43 Display MST status code and descriptio

44 SC CONDITIONS (V2.1 MST) 44 SC conditions,indicators,classificatio

45 SC/MST CLASSIFICATION 45 SC/MST classifications for visit - sca

46 BASIC DEMOGRAPHICS (V3.0) 46 Data fields - contains patient name,do

47 PATIENT INFORMATION (V3.0) 47 Name,sex,DOB,PID,eligibilty,address,te

48 GAF HAND PRINT V3.0 48 Previous GAF Score and Hand Print

49 GAF DISPLAY V3.0 49 Previous GAF Score Display Only

50 GAF SCORE MULT CHOICE V3.0 50 Previous and New GAF Score

51 ICD-10 DIAGNOSES (V1.0) 51 Common ICD-10 diagnoses

\+ Enter ?? for more actions \>\>\>

EB Edit Block DB Delete Block CB Copy Block

NB New Block CH Change TK Order

Select Action: Next Screen//

In the Appearance definition for this new ICD-10 Diagnosis tool kit block, the subcolumn for displaying the ICD-10 code allows a maximum of 8 characters and the short description allows a maximum of 30 characters.

Appearance Definition for ICD-10 Diagnoses

You can create a \[N\]ew list, edit its \[A\]ppearance, \[D\]elete it,

edit its \[Co\]ntents, \[P\]osition or size its columns. Choose from:

\[N\]ew \[A\]ppearance \[D\]elete \[C\]ontents \[P\]osition: C// APPEARANCE ICD-1

0 DIAGNOSES Block: CINDY'S ICD-10 CODES Form: WORKCOPY

NAME: ICD-10 DIAGNOSES//

WHAT TEXT SHOULD APPEAR AT THE TOP OF EACH COLUMN? (OPTIONAL):

SUBCOLUMN HEADER APPEARANCE:

HOW SHOULD THE SUBCOLUMNS BE SEPARATED?: SPACE/LINE/SPACE

//

HOW SHOULD THE HEADER FOR EACH GROUP OF ENTRIES APPEAR? CHOOSE FROM {U,B,S,C}: S

C//

NUMBER OF ADDITIONAL LINES FOR EACH ENTRY ON LIST?: 0

//

SHOULD EACH ENTRY ON THE LIST BE UNDERLINED? (YES/NO): NO

//

You can now specify the subcolumns the list should contain.

There can be at most 6 subcolumns, numbered 1-6.

Available Data:

1= CODE :8 char 2= DIAGNOSIS :30 char

3= DESCRIPTION :200 char 4= (N/A)

Select SUBCOLUMN NUMBER: 2//

## Reports and Utilities Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IBD\*3\*63 creates a new report, ICD-10 Status Update Report. Also, the Maintenance Utility for Active/Inactive Codes Report now contains selections for ICD-10 codes.

### Maintenance Utility for Active/Inactive Codes Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can now choose ICD-10 Diagnosis Codes to display or print on the Maintenance Utility Report in the Type of Code to Display selection. Depending on whether you select ACTIVE or INACTIVE, the report displays up to 8 characters for the ICD-10 code and as many characters of the ICD-10 short description as can display, with truncation as needed.

Maintenance Utility Report Selections, Updated for ICD-10

CHOOSE 1-5: 4 IBDF ENCOUNTER FORM Encounter Forms

Select Encounter Forms Option: RU Reports and Utilities

Select Reports and Utilities Option: MU Maintenance Utility for Active/Inactive

Codes

Sort by \[C\]linics, \[G\]roups, \[F\]orms: CLINICS// (Individual)

Select Clinic: ALL//

Select Type of Code to Display: DG

1 DG SELECT CPT PROCEDURE CODES TYPE=SELECTION

2 DG SELECT ICD-10 DIAGNOSIS CODES TYPE=SELECTION

3 DG SELECT ICD-9 DIAGNOSIS CODES TYPE=SELECTION

4 DG SELECT VISIT TYPE CPT PROCEDURES TYPE=SELECTION

CHOOSE 1-4: 2 DG SELECT ICD-10 DIAGNOSIS CODES

Display codes \[A\]ctive, \[I\]nactive: ACTIVE//

Select ICD-10 code:

Example of Inactive ICD-10 Codes on Maintenance Utility Report

Maintenance Utility Apr 07, 2012@18:15:46 Page: 1 of 4

This screen lists Inactive codes on Encounter Forms.

CODE DESCRIPTION BLOCK FORM CLINIC

TEST CLINIC ONE

1\) S62.001A Unsp fracture o ICD-10 DIAGNOS TEST ONE TEST CLINIC ONE

2\) S62.009D Unsp fx navic b ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

3\) S62.011B Disp fx of dist ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

4\) S62.013A Disp fx of dist ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

5\) S62.014P Nondisp fx of d ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

6\) S62.015D Nondisp fx of d ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

7\) S62.016G Nondisp fx of d ICD-10 DIAGNOS TEST TWO TEST CLINIC ONE

\+ Enter ?? for more actions

CL Change List DL Delete From List JP Jump

RC Replace Code IC Invalid Code List PL Print List

Select Action: Next Screen//

> **NOTE:** The Replace Code (RC) action in the Maintenance Utility Report uses the approved standard Lexicon partial code search.

The Replace Code action in the Maintenance Utility Report prompt has changed depending upon which Type of Code you selected (ICD-9 or ICD-10).

Replace Code for ICD-9 Codes

Select Action: Next Screen// RC=3 Replace Code

Select ICD 9 DIAGNOSIS CODE NUMBER: 278.01 278.01 MORBID OBESITY

...OK? Yes// \<RET\> (Yes)

Subcolumn Header:

Edit Subcolumn 3: MORBID OBESITY// \<RET\>

NARRATIVE TO SEND TO PCE: ??

Enter the narrative that should be sent to PCE when this selection is

scanned. This will be the provider narrative that is shown in PCE. If there is

no entry in this field the text as it appears

on the form will be sent as the narrative.

This field can only be entered for the type of interfaces that allow

adding this narrative, and then send the narrative to PCE.

NARRATIVE TO SEND TO PCE:

Replace Code for ICD-10 Codes

Select Action: Next Screen// RC=3 Replace Code

Enter Diagnosis, a Code or a Code Fragment:

This prompt allows you to use the partial code search.

### ICD-10 Status Update Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report provides a list of Encounter Forms that require updates for ICD-10. You can display or print a Summary or a Detail report. A new action “IS” allows you to update ICD-10 status.

> **NOTE:** This report will be useful during the time period when existing national and locally defined Encounter Forms are being updated to add or update ICD-10 diagnoses, as well as for future quarterly updates to ICD-10-CM.

Summary Report contains data listed in the following columns, in the order indicated:

- Entry: sequential number assigned to entries currently displayed
- Encounter Form: name up to 22 characters
- ICD9/ICD10: heading is in two rows without the dash. Depending on your prompt selections, the column contains “ICD9”, ICD10”, “BOTH”, or blank if neither.
- Last Edited: one column each for ICD9 and ICD10. The date format is MM/DD/YY.
- ICD10 Status: blank if Incomplete, REV (Review) or COMP (Complete)
- Clinic: Clinic name up to 22 characters

Detail Report contains the data as described for the Summary Report as well as the following additional details listed underneath each Encounter Form that is included on the report:

- Name for each block on the Encounter Form that contains ICD-9 diagnosis code(s).
- ICD-9 code (up to 6 characters) and short description for each ICD-9 diagnosis on that block.
- Name for each block on the Encounter Form that contains ICD-10 diagnosis code(s).
- ICD-10 code (up to 8 characters, including decimal point after the 3rd character) and short description for each ICD-10 diagnosis on that block.

Example of Prompts for ICD-10 Status Update Summary Report

Select Reports and Utilities Option: UP Encounter Forms ICD-10 Update

Sort by \[C\]linics, \[G\]roups, \[F\]orms: CLINICS//

Select one of the following:

AC ALL CLINICS

SC SELECTED CLINICS

RC RANGE OF CLINICS

Selection type: ALL CLINICS//

Select one of the following:

9 ICD-9

10 ICD-10

B Both

N Neither

A All

Contains ICD-9 and/or ICD-10 diagnosis codes:

ICD-\[9\], ICD-\[10\], \[B\]oth, \[N\]either, \[A\]ll: ALL// All

Select one of the following:

I Incomplete

C Complete

R Review

A All

ICD-10 Update Status:

\[I\]ncomplete, \[C\]omplete, \[R\]eview, \[A\]ll: ALL// All

Select one of the following:

S Summary Report

D Detail Report

Report Type:

\[S\]ummary Report, \[D\]etail Report: SUMMARY// Summary Report  
Sort Selections

If you sort the report by Clinics, the report output is sorted first by Clinic name, in alphabetic order, then by Encounter Form name, in alphabetic order.

If you sort the report by Groups, the report output is sorted first by Clinic Group, in alphabetic order, then by Clinic name, in alphabetic order, then by Encounter Form name, in alphabetic order.

If you sort the report by Forms, the report output is sorted by Encounter Form name, in alphabetic order.

Example of ICD-10 Status Update Summary Report

ICD-10 Status Update Report   Feb 10, 2012@16:40:19          Page:    1 of    3

     ENCOUNTER FORM         ICD9/   LAST EDITED    ICD10  CLINIC

                            ICD10  ICD9     ICD10  STATUS      
1)   NEW FORM               ICD9  01/24/12 01/24/12 REV   AUDIOLOGY            
2)   WHT RIVER TEST 83                     02/10/12 REV   AUDIOLOGY            
3)   WHT RIVER TEST 83                     02/10/12 REV   TEST CLINIC       
4)   PHILLY VASCULAR (DSD)  ICD9           02/10/12 COMP  CARDIOLOGY           
5)   EF CLASS DEMO \#303     ICD9           02/10/12 COMP  EF CLASS DEMO \#303   
6)   EF CLASS DEMO TWO \#303                               EF CLASS DEMO \#303   
7)   ONE TEST                                             ONE TEST CLINIC                
8)   VITALS-SLC                            02/10/12 COMP  HOUR CLINIC          
9)   TWO TEST FORM          ICD9                          TWO TEST CLINIC  
10)  TEST NEW FORM          BOTH  02/06/12 02/07/12 REV   TEST NEW CLINIC              
+         Enter ?? for more actions                                            

CL  Change List           PL  Print List

JP  Jump List             IS  Status Update

Select Action: Next Screen// ISStatus Update Action

Initially, the IS action is blank (i.e., incomplete) for all Encounter Forms. You can select a single entry or a range of entries, and you are then prompted to change the update status to “Review” or “Complete”.

> **NOTE:** During the period of time when Encounter Forms are being updated for the initial activation of ICD-10, the ICD-10 Update Status “Incomplete” could be used to manage Encounter Forms that may have had none or only some ICD-10 diagnosis codes added; the Status “Review” could be used if ICD-10 diagnosis codes that have been added are impacted by an update to the ICD-10-CM code set; the Status “Complete” could be used if the Encounter Form’s ICD-10 update has been completed. For future updates to the ICD-10-CM code set (i.e., subsequent to the initial ICD-10 activation), the “Review” status could be used to indicate which Encounter Forms may require updates based on ICD-10-CM codes that have been added, deleted, or updated in the ICD-10-CM code set; the Status “Complete” could be used when those Encounter Form updates have been completed.

# Adding ICD-10 Blocks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DEFAULTS Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the entries that is updated by the installation process is the DEFAULTS form in File \#357, which contains all standard blocks. During installation the new ICD-10 block is added to the DEFAULTS form. This standard form is supposed to reside in all AICS databases and should not be deleted.

In case it was deleted for some reason, the IBD\*3.0\*63 installation process checks if the DEFAULTS form exists in the AICS environment. If it is not found, then a warning message is printed on the screen and to the installation log, and the following e-mail is sent to the person who is installing the patch or to the POSTMASTER user:

The DEFAULTS form was not found in the environment and therefore the installation process didn't add the new ICD-10 block to the DEFAULTS form.

Please log a Remedy ticket to add the DEFAULTS form to your AICS environment if you need it.

When you have it in the environment you can use TK menu options to add the ICD-10 block to the DEFAULTS form manually.

## Inactive Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications implemented in the IBD\*3.0\*63 patch allow the user to add any ICD-10 code regardless of its current status (ACTIVE or INACTIVE), unless the last status of the code is INACTIVE and the effective date has been exceeded.

# ICD-10 Search Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IBD\*3\*63 patch provides the ability to search on ICD-10-CM diagnosis codes when creating or editing Encounter Forms/blocks. Also, a wildcard search allows you to enter an “\*” (asterisk) to select multiple, valid ICD-10 diagnosis codes for Encounter Forms. Whether the current date is prior to *or* on or after the ICD-10 Activation Date, you can access the ICD-10-CM code set.

> **NOTE:** Existing ICD-9 search functionality has not changed.

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AICS ICD-10 diagnosis code search functionality allows you to select a single, valid ICD-10 diagnosis code and display its description. The user interface prompts you for input, invokes the Lexicon utility to get data, and then presents that data. 

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes. A dash after a number indicates that it contains a sub-category.

ICD-10-CM diagnosis code search highlights include:

- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.
- You are presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, you are prompted to refine the search.
- You can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

The AICS package provides the ability to search on ICD-10-CM diagnosis codes at the following prompts when editing Encounter Forms/blocks:

- Select ICD-10 DIAGNOSIS CODE NUMBER:
- Select a SECOND ICD-10 code to associate with the original:
- Select a THIRD ICD-10 code to associate with the original:

If a user enters fewer than two characters during a DIAGNOSIS code search, the system will respond with a prompt to explain the issue and provide a resolution:

SELECT ICD-10 DIAGNOSIS CODE NUMBER: e0

Enter 3 to 8 characters or '??' for more help.

Example of ICD-10 Diagnosis Code Search

Select Action: Next Screen// RC Replace Code

Select Entry: (1-7): 1

Enter Diagnosis, a Code or a Code Fragment: S62

7 matches found

1\. S62.0- Fracture of navicular \[scaphoid\] bone of wrist

\(147\)

2\. S62.1- Fracture of other and unspecified carpal bone(s)

\(357\)

3\. S62.2- Fracture of first metacarpal bone (231)

4\. S62.3- Fracture of other and unspecified metacarpal

bone (560)

5\. S62.5- Fracture of thumb (105)

6\. S62.6- Fracture of other and unspecified finger(s)

\(490\)

7\. S62.9- Unspecified fracture of wrist and hand (21)

Select 1-7: 1

4 matches found

1\. S62.00- Unspecified fracture of navicular \[scaphoid\]

bone of wrist (21)

2\. S62.01- Fracture of distal pole of navicular \[scaphoid\]

bone of wrist (42)

3\. S62.02- Fracture of middle third of navicular \[scaphoid\]

bone of wrist (42)

4\. S62.03- Fracture of proximal third of navicular

\[scaphoid\] bone of wrist (42)

Select 1-4: 4

42 matches found

1\. S62.031A Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

for closed Fracture

2\. S62.031B Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

for open Fracture

3\. S62.031D Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Routine Healing

4\. S62.031G Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Delayed Healing

5\. S62.031K Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Nonunion

6\. S62.031P Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

Encounter for Fracture with Malunion

7\. S62.031S Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of right Wrist, Sequela

8\. S62.032A Displaced Fracture of Proximal third of

Navicular \[Scaphoid\] Bone of left Wrist, Initial Encounter

for closed Fracture

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 1

## ICD-10 Wildcard Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the ICD-10 wildcard search functionality for diagnosis code retrieval is to serve a specific user end goal, which is the selection of *multiple*, valid ICD-10 diagnosis codes (often related) to associate with specific functional elements, such as Encounter Forms.

Use the wildcard search when you are defining Encounter Forms and have previously identified the ICD-10 codes that you want to quickly and efficiently select.

ICD-10 wildcard search highlights include:

- This is a completely code-based search (i.e., not text-based). Two wildcard characters (\* and ?) are used to assist with searches.
- If the search terms provided by the application consist of a string of characters (i.e., the search string) containing an \* (asterisk) as the wildcard character (e.g., E08\*, 005\*), the system finds all ICD-10 codes that match the search terms, where zero or more alphanumeric characters (including the “X” placeholder character for ICD-10-CM diagnosis codes) exist at the position where the \* exists in the search string.
- The \* (asterisk) wildcard character can only appear in the last position of the search string.
- If the search terms provided by the application consist of a string of characters containing one or more ? (question mark) as the wildcard character (e.g. E1?.?0, 005??ZZ), the system finds all ICD-10 codes that match the search terms, where a single alphanumeric character (including the “X” placeholder character for ICD-10-CM diagnosis codes) exists at the position where a ? exists in the search string.
- The ? (question mark) wildcard character can appear anywhere in the search string, and can appear more than once. The system does not match a null (blank) value where a ? exists at the end of the search string.
- If the search terms provided by the application consist of a string of characters containing both an \* <u>and</u> one or more ? as wildcard characters (e.g., E2?.1\*, 0SU?3\*), the system finds all ICD-10 codes that match the search terms, where zero or more alphanumeric characters exist at the position where the \* exists in the search terms and a single alphanumeric character exists at the position where a ? exists in the search string.
- The first 2 characters in the search string cannot consist of a wildcard character (\* or ?).
- The system provides the code and long description for each ICD-10 diagnosis or procedure matching the search terms.
- You can select one or more ICD-10 codes from the list of matching codes, using a list, range, or combination.
- When editing an Encounter Form, you can enter a partial code without using any wildcard characters (e.g., E08, 005), in order to select a group of ICD-10 codes all at once, with the individual ICD-10 codes and descriptions not displayed.
- Entering ^ saves your selection and exits the search.

A wildcard search entry works differently from a selection list. If you answer “Yes” to automatically select ICD-10 codes, then a selection list does NOT display. The selection automatically prompts you for the NEXT available ICD-10 code based on the wildcard entry that you entered.

Automatic Selection of ICD-10 Codes in Wildcard Search

Select Action: Quit// AS Add Selection

SELECT ICD-10 DIAGNOSIS CODE NUMBER: E16\*

There are 7 ICD-10-CM diagnosis codes that begin with E16\*. Do you wish to

automatically add all of these diagnosis codes to this block? No// Y (Yes)

E16.0 Drug-induced hypoglycemia without coma

Select SELECTION GROUP HEADER: GROUPONE 1 ICD-10 DIAGNOSES

PRINT ORDER WITHIN GROUP: 3// 3

Select a SECOND ICD-10 code to associate with the original:

Select a THIRD ICD-10 code to associate with the original:

Subcolumn Header: DIAGNOSIS

Edit Subcolumn 3: Drug-induced hypoglycemia without coma

Replace

NARRATIVE TO SEND TO PCE:

CLINICAL LEXICON ENTRY: E16.0//

Drug-Induced Hypoglycemia without Coma (ICD-10-CM E16.0)

Ok? YES// YES Drug-Induced Hypoglycemia without Coma (ICD-10-CM E16.0)

\>\>\> ICD-10-CM Code: E16.0

Now for another!

Automatic selection continued:

E16.1 Other hypoglycemia

Select SELECTION GROUP HEADER: GROUP ONE 1 ICD-10 DIAGNOSES

Ok? (Yes/No) Yes// YES

Select SELECTION GROUP HEADER: GROUPONE 1 ICD-10 DIAGNOSES

PRINT ORDER WITHIN GROUP: 4// 4

Select a SECOND ICD-10 code to associate with the original:

Select a THIRD ICD-10 code to associate with the original:

Subcolumn Header: DIAGNOSIS

Edit Subcolumn 3: Other hypoglycemia

NARRATIVE TO SEND TO PCE:

CLINICAL LEXICON ENTRY: E16.1//

Other Hypoglycemia (ICD-10-CM E16.1)

Ok? YES// YES Other Hypoglycemia(ICD-10-CM E16.1)

\>\>\> ICD-10-CM Code: E16.1

Now for another!

Automatic selection continued:

E16.2 Hypoglycemia, unspecified

Select SELECTION GROUP HEADER: GROUP ONE 1 ICD-10 DIAGNOSES

Ok? (Yes/No) Yes// YES  

Select SELECTION GROUP HEADER: GROUPONE 1 ICD-10 DIAGNOSES

PRINT ORDER WITHIN GROUP: 5// 5

Select a SECOND ICD-10 code to associate with the original:

Select a THIRD ICD-10 code to associate with the original:

Subcolumn Header: DIAGNOSIS

Edit Subcolumn 3: Hypoglycemia, unspecified

NARRATIVE TO SEND TO PCE:

CLINICAL LEXICON ENTRY: E16.2//

Hypoglycemia, unspecified (ICD-10-CM E16.2)

Ok? YES// YES Hypoglycemia, unspecified (ICD-10-CM E16.2)

\>\>\> ICD-10-CM Code: E16.2

Now for another!

Automatic selection continued:

7 Diagnosis Added.

Drug-induced hypoglycemia without coma (ICD-10-CM E16.0)

Other hypoglycemia (ICD-10-CM E16.1)

Hypoglycemia, unspecified (ICD-10-CM E16.2)

Increased secretion of glucagon (ICD-10-CM E16.3)

Increased secretion of gastrin (ICD-10-CM E16.4)

Other specified disorders of pancreatic internal secretion (ICD-10-CM E16.8)

Disorder of pancreatic internal secretion, unspecified (ICD-10-CM E16.9)

Enter RETURN to continue or '^' to exit: \<RET\>

Please wait while I build the list............

<u>Selection List Display Feb 14, 2012@15:53:30 Page: 1 of 1</u>

This screen displays the selection list for 'ICD-10 DIAGNOSES (V1.0)'

on Encounter Form 'TEST ONE CLINIC FORM'

<u>CODE ORDER NARRATIVE</u>

1 GROUP ONE

1\) S62.001A 1 Unsp fracture of navicular bone of right wrist, init

2\) S62.001D 2 Unsp fx navicular bone of r wrist, subs for fx w routn

3\) E16.0 3 Drug-induced hypoglycemia without coma

4\) E16.1 4 Other hypoglycemia

5\) E16.2 5 Hypoglycemia, unspecified

6\) E16.3 6 Increased secretion of glucagon

7\) E16.4 7 Increased secretion of gastrin

8\) E16.8 8 Other specified disorders of pancreatic internal secret

9\) E16.9 9 Disorder of pancreatic internal secretion, unspecified

Enter ?? for more actions \>\>\>

AS Add Selection FA Format All GE Group Edit

ES Edit Selection GA Group Add RS Resequence Group

DS Delete Selection GC Group Copy

PH New Place Holder GD Group Delete

Select Action: Quit//

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some AICS routines were modified to replace direct global reads and old Application Program Interfaces (APIs) with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible. Several AICS routines were modified to replace direct global reads to the ICD Diagnosis file (#80). For example, a direct read to ^ICD9(IEN#,0) to find the ICD code or description was replaced by a call to this API: ICDDATA^ICDXCODE. The following routines were changed to accommodate this: IBDFBK2, IBDFN4, IBDFN7, IBDFN8, IBDFN9, IBDFN11, IBDFN14, IBDFLST, IBDFUTL and IBDFUTL1.

A new report, Encounter Forms ICD-10 Update, allows you to display a list of Encounter Forms and Clinics after making selections from several input options. When the report has been displayed, you may then update the ICD-10 Status field. Two new routines were written for this new report: IBDFUTL4 and IBDFUTL5.

## Hardcoded Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, AICS uses a hardcoded value of 799.9 (Illness, unspecified). After the ICD-10 Activation Date, the ICD-10 code R69 (Illness, unspecified) replaces 799.9.

## Integration Control Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes have been made to Integration Control Registration (ICR) \#1296 to introduce new parameters values for the API GETLST^IBDF18A.

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The date and time are recorded in the Encounter Form file when changes are made to a form. Fields were added to the Encounter Form file (#357) and to the Selection file (#357.3) to accommodate the history date and time.

The Data Dictionary (DD) for the new fields in File \#357 is as follows:

STANDARD DATA DICTIONARY \#357.03 -- CODING SYSTEM UPDATES SUB-FILE

FEB 19,2012@08:26:40 PAGE 1

STORED IN ^IBE(357,D0,3, SITE: VEHU MASTER UCI: VISTA,ROU

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This subfile stores tracking information on encounter form blocks' updates

related to a specific coding system.

COMPILED CROSS-REFERENCE ROUTINE: IBDX0

CROSS-REFERENCED BY: CODING SYSTEM(B)

357.03,.01 CODING SYSTEM 0;1 POINTER TO ICD CODING SYSTEMS FILE (#80.4)[Top](#TOP)

LAST EDITED: FEB 07, 2012

HELP-PROMPT: Select the coding system for which the

encounter form was updated.

DESCRIPTION: This field stores the coding system identifier

for which the block of the form has been

updated.

CROSS-REFERENCE: 357.03^B

1)= S ^IBE(357,DA(1),3,"B",\$E(X,1,30),DA)=""

2)= K ^IBE(357,DA(1),3,"B",\$E(X,1,30),DA)

CROSS-REFERENCE: 357^CS

1)= S ^IBE(357,"CS",\$E(X,1,30),DA(1),DA)=""

2)= K ^IBE(357,"CS",\$E(X,1,30),DA(1),DA)

This cross-reference is used to provide a quick

access to entries with coding system updates.

357.03,.02 UPDATE STATUS 0;2 SET

'C' FOR COMPLETE;

'R' FOR REVIEW;

LAST EDITED: FEB 07, 2012

HELP-PROMPT: Enter the coding system update status.

DESCRIPTION: This field will be set to 'C' if the migration

to the coding system specified in the field

\#.01 of this multiple entry has been marked as

completed and 'R' if changes were reviewed. To

change back to incomplete, delete its value.

CROSS-REFERENCE: 357^CSST

1)= S ^IBE(357,"CSST",\$E(X,1,30),DA(1),DA)=""

2)= K ^IBE(357,"CSST",\$E(X,1,30),DA(1),DA)

This cross-reference is used to provide a quick

access to the status of the coding system

updates.

357.03,.03 DATE LAST EDITED 0;3 DATE

INPUT TRANSFORM: S %DT="ETXR" D ^%DT S X=Y K:X\<1 X

LAST EDITED: FEB 15, 2012

HELP-PROMPT: (No range limit on date)

357.03,.04 CHANGES MADE BY 0;4 POINTER TO NEW PERSON FILE (#200)

LAST EDITED: FEB 15, 2012

HELP-PROMPT: Select the person who last made changes to

blocks for the coding system in the form.

DESCRIPTION: The person who last updated ICD blocks of the

form.

FILES POINTED TO FIELDS [Top](#TOP)

ICD CODING SYSTEMS (#80.4) CODING SYSTEM (#.01)

NEW PERSON (#200) CHANGES MADE BY (#.04)

The DD for the new fields in File \#357.3 is as follows:

STANDARD DATA DICTIONARY \#357.3 -- SELECTION FILE

FEB 19,2012@15:35:44 PAGE 26

STORED IN ^IBE(357.3, (22185 ENTRIES) SITE: VEHU MASTER UCI: CPM,ROU (VERSI

ON 3.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

357.3,4.01 ICD CODE EDIT DATE/TIME 4;1 DATE

INPUT TRANSFORM: S %DT="ETX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: JAN 19, 2012

HELP-PROMPT: Enter date and time when ICD diagnosis code was

edited.

DESCRIPTION: Indicates date and time of ICD-9 diagnosis code

edit to block/encounter form.

357.3,4.02 ICD CHANGES MADE BY 4;2 POINTER TO NEW PERSON FILE (#200)

LAST EDITED: JAN 19, 2012

HELP-PROMPT: Enter the person who made ICD changes to this

record last timedate and time.

DESCRIPTION: Indicates date and time of ICD-10 diagnosis

code edit to block/encounter form.

> **NOTE:** In order to check the history fields in File \#357.3, it is necessary to locate the Block that is being worked on.

## Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text (?) and extended help text (??, ???) are included for prompts related to ICD-10 codes.

When entering ?:

Enter code or “text” for more information.

When entering ??:

Enter a "free text" term or part of a term such as ”femur fracture”.

Or

Enter a ”classification code” (ICD/CPT etc) to find the single term associated with the code.

Or

Enter a ”partial code”. Include the decimal when a search criterion includes 3 characters or more for code searches.

When entering ???:

Number of Code Matches

----------------------

The ICD-10 Diagnosis Code search will show the user the number of matches found, indicate if additional characters in ICD code exist, and the number of codes within the category or subcategory that are available for selection.

19 matches found

M91. - Juvenile osteochondrosis of hip and pelvis (19)

This indicates that 19 unique matches or matching groups have been found and will be displayed.

M91. - the “-“ indicates that there are additional characters that specify unique ICD-10 codes available.

\(19\) Indicates that there are 19 additional ICD-10 codes in the M91 ”family” that are possible selections.