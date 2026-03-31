---
title: Problem List User Manual Version 2 (GMPL*2*60)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (GMPL*2*60)
app_code: GMPL
app_name: "CPRS: Problem List"
section: CLI
app_status: active
pkg_ns: GMPL
patch_ver: 2
patch_id: GMPL*2
group_key: "GMPL:GMPL:2"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - problem
  - problems
  - selection
  - table
  - gmpl
  - contents
  - patient
  - snomed
  - code
  - active
page_count: 0
word_count: 26328
section_count: 37
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmplum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmplum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=64"
---

Problem List

User Manual

![](problem-list-user-manual-version-2-gmpl-2-60/001.png)

April 2025

Office of Information & Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Page</td>
<td>Patch #/ Change</td>
<td><p>Writer/</p>
<p>Project Manager</p></td>
</tr>
<tr class="even">
<td>Apr 2025</td>
<td><p><a href="#removed_1">21</a></p>
<p><a href="#removed_2">117</a></p>
<p><a href="#removed_3">118</a></p></td>
<td><p>GMPL*2*60:</p>
<ul>
<li><p>Updated document globally for 508 compliance</p></li>
<li><p>Removed broken links discontinued/unavailable information</p>
<ul>
<li><p><a href="#removed_1">SACC</a> reference doc</p></li>
<li><p><a href="#removed_2">Permission</a> request</p></li>
<li><p><a href="#removed_3">CPRS Wiki</a></p></li>
</ul></li>
</ul></td>
<td>CPRS development team</td>
</tr>
<tr class="odd">
<td>Dec. 2017</td>
<td><p><u><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements">2</a>, <a href="#assign_ICD_diagnosis_out_of_order_menu">20</a>, <a href="#GMPL_IMPRT_UTIL_key">20</a>, <a href="#Check_Prob_select_List_Prob_codes_option">23</a>, <a href="#Prob_Select_List_code_set_version_review">23</a>, <a href="#managment_menu_options">28</a>,</u></p>
<p><u><a href="#Create_Prblm_Select_Lists_new_menu_items">30</a>, <a href="#assignremove-problem-selection-list-gmpl-assign-list">39</a>, <a href="#check-problem-selection-list-problem-codes-gmpl-selection-list-csv-check">43</a>, <a href="#import-problem-selection-list-gmpl-selection-list-import">44</a></u></p>
<p><a href="#VA_National_Prob_select_categ_problems"><u>66</u></a></p></td>
<td><p>GMPL*2*49:</p>
<ul>
<li><p><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements">Added a summary of Problem Selection List enhancements</a></p></li>
<li><p><a href="#assign_ICD_diagnosis_out_of_order_menu">Made a note that the Assign ICD Diagnosis is now marked out of order.</a></p></li>
<li><p><a href="#GMPL_IMPRT_UTIL_key">Added information about the GMPL IMPRT UTIL key that gives a user the ability to import Problem Selection List content.</a></p></li>
<li><p><a href="#Check_Prob_select_List_Prob_codes_option">Added a minor note about the Check Problem Selection List Problem Codes menu option.</a></p></li>
<li><p><a href="#Prob_Select_List_code_set_version_review">Updated the example for Problem Selection List Code Set Version review</a></p></li>
<li><p><a href="#_Toc31613587">Example of Problem Selection List inactive codes report</a></p></li>
<li><p><a href="#managment_menu_options">Updated the captures that shows the options under the Problem List Management menu</a></p></li>
<li><p><a href="#Create_Prblm_Select_Lists_new_menu_items">Updated the items on the Create Problem Selection Lists menu</a></p></li>
<li><p><a href="#VA_National_Prob_select_categ_problems">Added a screen capture showing the VA National Problem Selection List content with a category and problems showing</a></p></li>
<li><p><a href="#assignremove-problem-selection-list-gmpl-assign-list">Made edits in the Assign/Remove Problem Selection List and to remove a problem selection list</a></p></li>
<li><p>Updated information for <a href="#check-problem-selection-list-problem-codes-gmpl-selection-list-csv-check">Check Problem Selection List Problem Codes</a> and <a href="#import-problem-selection-list-gmpl-selection-list-import">Import Problem Selection List</a></p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 2016</td>
<td><a href="#snomed-in-diagnosis-field-error-report"><u>53</u></a></td>
<td>GMPL*2*40 – <a href="#snomed-in-diagnosis-field-error-report">Minor edits from review and the addition of a section for the Generate SNOMED in Diagnosis Field Err/Cleanup Rpt.</a></td>
<td></td>
</tr>
<tr class="odd">
<td>July 2016</td>
<td><u><a href="#changes-made-by-gmpl2.040---erroneous-problem-file-cleanup">3</a>, <a href="#snomed-in-diagnosis-field-error-report">53</a></u></td>
<td>GMPL*2*40 – <a href="#changes-made-by-gmpl2.040---erroneous-problem-file-cleanup">Erroneous Problem File Cleanup description.</a> <a href="#snomed-in-diagnosis-field-error-report">Added material about two new reports to help users find and correct an issue where SNOMED codes were being stored where an ICD code should be.</a></td>
<td></td>
</tr>
<tr class="even">
<td>February 2016</td>
<td><u><a href="#changes-made-by-gmpl2.045-changes-to-comment-length-and-a-provider-can-now-view-edit-or-delete-comments-entered-by-another-provider">3</a>,</u> <u><a href="#patch_list_patch45">12</a>,</u> <a href="#all_comments_and_200_characters"><u>86</u></a></td>
<td>GMPL*2*45 - Changes to Comment Length and a Provider Can Now View, Edit, or Delete Comments Entered by Another Provider – Added description.</td>
<td></td>
</tr>
<tr class="odd">
<td>March 2014</td>
<td><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements"><u>2</u></a></td>
<td>GMPL*2*42 - PROBLEM LIST SUPPORT FOR ICD-10-CM – Added description.</td>
<td></td>
</tr>
<tr class="even">
<td>March 2014</td>
<td><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements"><u>2</u></a></td>
<td>GMPL*2*44 - PROBLEM LIST ICD-10-CHANGES FOR CLINICAL REMINDERS – Added description.</td>
<td></td>
</tr>
<tr class="odd">
<td>June 2012</td>
<td><a href="#newreports"><u>49</u></a></td>
<td>GMPL*2*36: Added examples of new follow-up reports</td>
<td></td>
</tr>
<tr class="even">
<td>June 2012</td>
<td><a href="#lexiconsearch"><u>67</u></a></td>
<td>GMPL*2*36: Added examples of using new Extended Lexicon Search</td>
<td></td>
</tr>
<tr class="odd">
<td>June 2012</td>
<td><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements"><u>2</u></a></td>
<td>GMPL*2*36: Added description of patch 36, Extensions to Accommodate SNOMED-CT.</td>
<td></td>
</tr>
<tr class="even">
<td>June 2012</td>
<td><a href="#index"><u>116</u></a></td>
<td>Added Appendix B –and Frequently Asked Questions re Problem List standardization</td>
<td></td>
</tr>
<tr class="odd">
<td>June 2012</td>
<td><a href="#appendix-a-lexiconntrt-tips-for-the-problems-tab"><u>109</u></a></td>
<td>Added Tips for CACs (for PL standardization)</td>
<td></td>
</tr>
<tr class="even">
<td>June 2012</td>
<td><a href="#changes-made-by-gmpl2.049-problem-selection-list-enhancements"><u>2</u></a></td>
<td>Added recent patch descriptions</td>
<td></td>
</tr>
<tr class="odd">
<td><p>November/</p>
<p>December 2004</p></td>
<td>various</td>
<td>Patient name and SSN edits, to comply with VHA Directive</td>
<td></td>
</tr>
<tr class="even">
<td>August 2003</td>
<td><a href="#code-set-versioning-csv-requirements"><u>20</u></a>-16</td>
<td>GMPL*2*28: Updated for Code Set Versioning (CSV) changes.</td>
<td></td>
</tr>
<tr class="odd">
<td>July 2002</td>
<td>various</td>
<td>Various manual reorganization changes.</td>
<td></td>
</tr>
<tr class="even">
<td>May 2002</td>
<td>2 and various manual</td>
<td>Added section on GMPL*2.0*26, Co-Pay Enhancements; also updated examples throughout manual to reflect these changes.</td>
<td></td>
</tr>
<tr class="odd">
<td>April 2002</td>
<td>43, 86</td>
<td>Added section on use of Problem List in CPRS.</td>
<td></td>
</tr>
<tr class="even">
<td>March 2002</td>
<td>various</td>
<td>Format changes; updates per patch GMPL*2.0*25 and others.</td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Features in Problem List](#features-in-problem-list)
  - [Related Manuals](#related-manuals)
  - [Release Notes - Recent patches](#release-notes-recent-patches)
    - [Changes Made by GMPL\2.0\49 – Problem Selection List Enhancements](#changes-made-by-gmpl2049-problem-selection-list-enhancements)
    - [Changes Made by GMPL\2.0\40 - Erroneous Problem File Cleanup](#changes-made-by-gmpl2040-erroneous-problem-file-cleanup)
    - [Changes Made by GMPL\2.0\45 – Changes to Comment Length and a Provider Can Now View, Edit, or Delete Comments Entered by Another Provider](#changes-made-by-gmpl2045-changes-to-comment-length-and-a-provider-can-now-view-edit-or-delete-comments-entered-by-another-provider)
    - [Changes Made by GMPL\2.0\42 - PROBLEM LIST SUPPORT FOR ICD-10-CM](#changes-made-by-gmpl2042-problem-list-support-for-icd-10-cm)
    - [Diagnosis Code Search](#diagnosis-code-search)
    - [Add/Edit/Store Diagnosis Code](#addeditstore-diagnosis-code)
    - [Display Diagnosis](#display-diagnosis)
    - [GMPL\2.0\44 - PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS](#gmpl2044-problem-list-icd-10-changes-for-clinical-reminders)
    - [GMPL\2\36 - EXTENSIONS TO ACCOMMODATE SNOMED-CT](#gmpl236-extensions-to-accommodate-snomed-ct)
    - [Problem List NTRT Follow-up Report](#problem-list-ntrt-follow-up-report)
    - [Problem List Freetext Follow-up Report](#problem-list-freetext-follow-up-report)
    - [GMPL\2.0\27 - Clinical Reminders Index](#gmpl2027-clinical-reminders-index)
    - [GMPL\2.0\26 - Head-Neck Cancer/Military Sexual Trauma](#gmpl2026-head-neck-cancermilitary-sexual-trauma)
    - [Problem List Patches](#problem-list-patches)
- [Orientation](#orientation)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [### VistA, Problem List, List Manager, and CPRS/Windows Conventions](#vista-problem-list-list-manager-and-cprswindows-conventions)
    - [Conventions used in this manual](#conventions-used-in-this-manual)
    - [List Manager Conventions](#list-manager-conventions)
    - [Windows Conventions](#windows-conventions)
- [Package Management](#package-management)
  - [Implementation of Problem List](#implementation-of-problem-list)
  - [# Package Management](#package-management-1)
  - [Links to other packages](#links-to-other-packages)
  - [Lexicon](#lexicon)
  - [Encounter Forms](#encounter-forms)
  - [CPRS](#cprs)
  - [## Menu Access](#menu-access)
  - [Security Keys](#security-keys)
  - [Electronic Signature](#electronic-signature)
  - [Legal Requirements i](#legal-requirements-i)
  - [Code Set Versioning (CSV) Requirements](#code-set-versioning-csv-requirements)
    - [CPRS GUI Problem List Tab](#cprs-gui-problem-list-tab)
    - [Add Problem](#add-problem)
    - [Verify Problem](#verify-problem)
    - [Restore Problem](#restore-problem)
    - [Change Problem](#change-problem)
  - [CPRS Problem List Management](#cprs-problem-list-management)
  - [Management Menu Options](#management-menu-options)
    - [Edit PL Site Parameters](#edit-pl-site-parameters)
    - [\[GMPL PARAMETER EDIT\]](#gmpl-parameter-edit)
    - [Create Problem Selection Lists \[GMPL BUILD LIST MENU\]](#create-problem-selection-lists-gmpl-build-list-menu)
    - [Create Problem Selection Lists \[GMPL BUILD LIST MENU\]](#create-problem-selection-lists-gmpl-build-list-menu-1)
    - [Build Problem Selection List(s)](#build-problem-selection-lists)
    - [Copy Selection List from IB Encounter Form](#copy-selection-list-from-ib-encounter-form)
    - [Assign/Remove Problem Selection List \[GMPL ASSIGN LIST\]](#assignremove-problem-selection-list-gmpl-assign-list)
    - [Delete Problem Selection List \[GMPL DELETE LIST\]](#delete-problem-selection-list-gmpl-delete-list)
  - [Check Problem Selection List Problem Codes \[GMPL SELECTION LIST CSV CHECK\]](#check-problem-selection-list-problem-codes-gmpl-selection-list-csv-check)
  - [Import Problem Selection List \[GMPL SELECTION LIST IMPORT\]](#import-problem-selection-list-gmpl-selection-list-import)
    - [List Patients with Problem List data \[GMPL PATIENT LISTING\]](#list-patients-with-problem-list-data-gmpl-patient-listing)
    - [Search for Patients having selected Problem \[GMPL PROBLEM LISTING\]](#search-for-patients-having-selected-problem-gmpl-problem-listing)
  - [### Replace Removed Problems on Patient’s List \[GMPL REPLACE PROBLEMS\]](#replace-removed-problems-on-patients-list-gmpl-replace-problems)
    - [Problem List NTRT Follow-up Report](#problem-list-ntrt-follow-up-report-1)
    - [Problem List Freetext Follow-up Report](#problem-list-freetext-follow-up-report-1)
    - [SNOMED in Diagnosis Field Error Report](#snomed-in-diagnosis-field-error-report)
    - [SNOMED in Diagnosis Field Cleanup Report](#snomed-in-diagnosis-field-cleanup-report)
    - [Generate SNOMED in Diagnosis Field Err/Cleanup Rpt](#generate-snomed-in-diagnosis-field-errcleanup-rpt)
    - [Changing Views on the Problem List](#changing-views-on-the-problem-list)
- [Package Operation](#package-operation)
  - [Potential Scenarios for Problem List Entry](#potential-scenarios-for-problem-list-entry)
  - [Problem List in CPRS GUI](#problem-list-in-cprs-gui)
  - [Customizing the Problem List](#customizing-the-problem-list)
  - [Problem List in CPRS List Manager](#problem-list-in-cprs-list-manager)
    - [Potential Scenarios for Problem List Entry](#potential-scenarios-for-problem-list-entry-1)
  - [Using Problem List through the Problem List Program in List Manager](#using-problem-list-through-the-problem-list-program-in-list-manager)
    - [Patient Problem List Option \[GMPL CLINICAL USER\]](#patient-problem-list-option-gmpl-clinical-user)
    - [Problem List Data Entry \[GMPL DATA ENTRY\]](#problem-list-data-entry-gmpl-data-entry)
    - [How to Use Problem List User List Manager Actions](#how-to-use-problem-list-user-list-manager-actions)
  - [ACTIONS](#actions)
  - [Select Action: Next Screen// <u>cm</u> Comment on a Problem](#select-action-next-screen-ucmu-comment-on-a-problem)
  - [Select Problem (1-12): <u>4</u>](#select-problem-1-12-u4u)
  - [Acute myocardial infarction](#acute-myocardial-infarction)
  - [COMMENT (\<200 char): <u>Low RBC mass</u>](#comment-200-char-ulow-rbc-massu)
  - [Another Comment: \<Enter\>](#another-comment-enter)
  - [The detailed display shows further information about the problem, such as date of onset, ICD code, service connection, author, provider narrative, and date entered.](#the-detailed-display-shows-further-information-about-the-problem-such-as-date-of-onset-icd-code-service-connection-author-provider-narrative-and-date-entered)
  - [Select View of List](#select-view-of-list)
  - [More Actions](#more-actions)
    - [How to Use Problem List User GUI Actions](#how-to-use-problem-list-user-gui-actions)
- [Helpful Hints & Tips](#helpful-hints-tips)
- [Glossary](#glossary)
- [Appendix A: Lexicon/NTRT Tips for the Problems Tab](#appendix-a-lexiconntrt-tips-for-the-problems-tab)
- [Index](#index)
- [-, 18](#18)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem List application is used to document and track a patient’s problems. It provides clinicians with a current and historical view of a patient’s health care problems across clinical specialties. It will allow each identified problem to be traced through the VistA health care system in terms of treatment, test results, and outcome.

The Problem List application is designed to be used by primary caregivers such as physicians, nurses, social workers, and others, in both inpatient and outpatient settings, as well as by ward clerks and coding clerks.

Various data entry methods are possible with this application.

## Features in Problem List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Allows one problem list for a given patient.
- Tied to coding systems: SNOMED CT and ICD-10-CM.
- Requires minimal data entry.
- Linked to other sections of the medical record, such as CPRS and Health Summary.
- Supports import of problem information from other clinical settings outside the immediate VAMC.
- Uses a common language of terminology, the Lexicon Utility. Each term is well-defined and understandable. A user, site, or application may substitute a preferred synonym. Allows reformulation of a problem.
- Problem List now accommodates the use of the Systematic Nomenclature of Medicine – Clinical Terms (SNOMED CT) for selection of Patient Problems. Problem List is working with Standard Terminology Service (STS) to implement SNOMED CT on both the Enterprise Terminology Server and the Clinical Lexicon, using the New Term Rapid Turnaround (NTRT) strategy for vetting and deployment of novel clinical expressions.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Problem List Technical ManualLexicon Utility ManualsCPRS Manuals*

## Release Notes - Recent patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Changes Made by GMPL\*2.0\*49 – Problem Selection List Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces enhancements to the Problem Selection List feature that may be used as an alternative method to quickly document common and/or frequently used problems by selecting problems from the curated specialty categories containing the top SNOMED CT diagnoses pre-mapped to ICD-10-CM called the VA-National Problem Selection List. This patch includes updates to the Problem Selection List menu items and menu actions to assist in the creation and maintenance of selection lists related to editing and assigning of problem selection lists to users and locations.

![](problem-list-user-manual-version-2-gmpl-2-60/002.png)

When a problem list is assigned, it will display on the left of the Problems tab. The VA-National Problem Selection List is shown above.

To support these enhancements, the file structure for \#125 and \#125.11 were redesigned and the data is migrated with new reports to identify duplicate selection lists and categories and selection list names in mixed/lower case. A new class field was added to both \#125 and \#125.11 files to identify, control, and manage the editing capabilities of national, VISN, or local level lists and categories. In CPRS, the VA-National Problem Selection List will display by default unless users have previously defined their own selection lists. The national selection list will be nationally distributed and maintained but require Clinical Application Coordinators (CAC) to import the updates using new GMPL Selection List Import feature.

This patch works with the OR\*3.0\*429 patch that migrates existing problem selection lists that currently exist into a new file structure. The patch migrates the lists that will be available after the patch is installed. Because mixed case list names are no longer allowed, this patch converts any lists with mixed case to all upper case.

### Changes Made by GMPL\*2.0\*40 - Erroneous Problem File Cleanup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To correct an issue where SNOMED codes get stored in the DIAGNOSIS field \#.01 instead of ICD codes, three new options have been added to the Problem List Mgt Menu \[GMPL MGT MENU\]:

1.  SNOMED in Diagnosis Field Error Report \[GMPL DIAG ERROR REPORT\]
2.  SNOMED in Diagnosis Field Cleanup Report \[GMPL DIAG CLEANUP REPORT\]
3.  Generate SNOMED in Diagnosis Field Err/Cleanup Rpt \[GMPL GENERATE DIAG RPTS\]

The first two reports identify fields that have the error and where they are cleaned up. The third option enables users with access to this menu to rerun the filescan and cleanup tasks for any potential new errors.

### Changes Made by GMPL\*2.0\*45 – Changes to Comment Length and a Provider Can Now View, Edit, or Delete Comments Entered by Another Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The length of the comment field has been changed from less than 60 characters (which includes spaces and punctuation) to less than 200.

Also, providers can now view, edit, and delete another provider’s comments on a problem.

### Changes Made by GMPL\*2.0\*42 - PROBLEM LIST SUPPORT FOR ICD-10-CM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Problem List patch to support the requirements of ICD-10-CM implementation. The Problem Search function will continue to originate with the Problem List Subset of SNOMED CT and follow the algorithm introduced by the Problem List Data Standardization effort and CPRS v29. Prior to the ICD-10-CM implementation date (1 October 2015), the selected SNOMED CT code will continue to be resolved to the corresponding ICD-9-CM code(s), and all of the Problem List display and print options will continue to render the diagnostic codes as ICD-9-CM.

Beginning on the ICD-10-CM implementation date, the selected SNOMED CT code will be resolved to the corresponding ICD-10-CM code(s), and all of the Problem List display and print options will render the diagnostic codes as either ICD-9-CM or ICD-10-CM, depending upon the date when the code for the problem was last edited.

### Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Problem List application will provide the ability to search for SNOMED CT diagnoses which will be linked to a generic ICD-10 diagnosis code of R69.

![](problem-list-user-manual-version-2-gmpl-2-60/003.png)

Users may use the following search methods:

- SNOMED CT concept codes
- Text strings (i.e. SNOMED CT description)

### Add/Edit/Store Diagnosis Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If the ‘Current System Date’ is on or after the ICD-10 activation date, the CPRS Problem List package will provide the ability to perform the following actions for ICD-10-CM diagnosis codes (problems) through the Action List items on the patient’s problem list.
  - New Problem: Add an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Change: Change an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Inactivate: Inactivate a SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Verify: Verify an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Annotate: Annotate and update an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Remove: Remove an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - Restore: Restore an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
  - View Details: View details of an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.

### Display Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Problem List allows for the display of problems for the Active View, Inactive View, and Removed View options within the initial Problem List.
  - The Problem List application will display the patient’s list of problems. Problems entered prior to July of 2013 will display in ICD-9-CM and those entered after will be represented in SNOMED CT. Problems added through Reminder Dialogs or Group notes will display problems in an ICD-10 diagnosis short description within the initial Problem List screen and will label whether an ICD diagnosis code is either ICD-9 or ICD-10.
- When user selects the ‘View Details’ action, the CPRS Problem List application will:
  - Display the details of an SNOMED CT diagnosis mapped to an ICD-10-CM diagnosis code of R69 and its full descriptions/definitions, or
  - If the problem was updated via the encounter form, it would display the newly mapped ICD10 code and not the R69.
  - Print the SNOMED CT to ICD-10-CM diagnosis code audit history
- When using the ‘View Details’ action, the CPRS Problem List application will display the ICD-10 label, ICD-10-CM diagnosis code, and short description within the audit history.

![](problem-list-user-manual-version-2-gmpl-2-60/004.png)

![](problem-list-user-manual-version-2-gmpl-2-60/005.png)

Print Diagnosis

- When the user selects the “View Details” action:
  - If the date the diagnosis code was entered is on or after the ICD-10 activation date, the CPRS Problem List application will provide the ability to print the problem represented in SNOMED CT linked to ICD-10-CM diagnosis codes and descriptions/definitions.
  - The CPRS Problem List application will designate whether diagnosis codes are SNOMED CT linked to ICD 10-CM and ICD-9-CM.

![](problem-list-user-manual-version-2-gmpl-2-60/006.png)

### GMPL\*2.0\*44 - PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

> ^PXRMINDX (9000011, CODING SYSTEM,”ISPP”, CODE, STATUS, PRIORITY, DFN, DLM, DAS)

> ^PXRMINDX (9000011, CODING SYSTEM,”PSPI”, DFN, STATUS, PRIORITY, CODE, DLM, DAS)

> Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Manual (PXRM_INDEX_TM).

> The post-install routine will start a background job to rebuild the file \#9000011 index in the new format.

### GMPL\*2\*36 - EXTENSIONS TO ACCOMMODATE SNOMED-CT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this patch is to accommodate the use of the Systematic Nomenclature of Medicine -- Clinical Terms (SNOMED CT) for selection of Patient Problems, and to dovetail with the efforts of Standard Data Service (SDS) to implement SNOMED CT on both the Enterprise Terminology Server and the Clinical Lexicon, using the New Term Rapid Turnaround (NTRT) strategy for vetting and deployment of novel clinical expressions.

This patch introduces changes required by CPRS v29 for selection of Patient Problems using SNOMED CT.

A new bulletin, GMPL PROBLEM NTRT BULLETIN, is added by the patch. This bulletin is sent to members of the FORUM mail group g.PROBLEM LIST NTRT when a SNOMED CT Concept is selected by the user for which no ICD-9-CM codes are mapped. The mail group is populated with members of OI&T’s Standards and Terminology Service. When approved by the Domain Steward for Problem List, new standardized mappings will be deployed using the New Term Rapid Turnaround capability.

Two new options are included:

### Problem List NTRT Follow-up Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report allows sites to evaluate problems with valid SNOMED CT Concept codes, which were unmapped to ICD at the time of entry.

> The report may be filtered by Medical Center Division, Provider(s), and Time Interval.

### Problem List Freetext Follow-up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report allows sites to evaluate uncoded free text problems that have been entered by one or more providers over a specified time interval.

GMPL\*2\*41 - CORRECT WINDOWS REPORT FOOTER

This patch corrects the printing of inaccurate CBOC division information in the footer section of the Patient Problem List report which is printed from the Problems Tab in the CPRS GUI.

GMPL\*2\*39 - FIX FOR GENERAL ERRORS IN PROBLEM LIST

This patch addresses the following issues:

1\. A diagnosis entered on the Diagnosis Tab of the Encounter Form on the Notes Tab of CPRS GUI is not added to the problem list for inpatients whose hospital location type is "Clinic".

2\. A CPRS GUI user at a non-VA site entering a new problem list item while entering an encounter for a patient will generate an undefined variable error when saving the form. This will cause all of the just entered data for the encounter to not be saved.

GMPL\*2\*38 - Fix for Problem List Priority Value

This patch fixes a problem with the problem list priority field always being set to a value of "Unknown". This can happen when the user is adding a new problem list entry to the patient chart, or when editing an existing problem list entry. If the user picks a priority of "Acute" or "Chronic" when adding or editing a problem list entry, the entry is saved to the PROBLEM file with a priority of "Unknown". This will only happen to Problem tab entries that were added or edited after GMPL\*2.0\*37 was installed on the system.

A site can use FileMan to find a list of entries that were added or modified after GMPL\*2.0\*37 was installed on the system.

GMPL\*2\*37 - PROBLEM LIST REPAIR DUE TO SHAD

When entering a new problem in CPRS 27 with an Immediacy of "\<unknown\>" a zero was entered in the PRIORITY field of the PROBLEM File, file \#9000011. The Priority field should be null for an unknown problem. Having a zero value in the PRIORITY field created a bad entry in the Clinical Reminder Index that caused Clinical Reminders to incorrectly evaluate ICD9 data that is stored in the PROBLEM File.

This patch contains two fixes to address this problem: a change to GMPLSAVE to evaluate the data that is being passed to this routine. If CPRS passes a zero value for the Priority field GMPLSAVE will set the Priority field to null.

A post-install routine will evaluate the PROBLEM file, for entries that contain a zero in the Priority field. If any entries in the PROBLEM file, contains a zero the Priority field will be set to Null and the entry will be corrected in the Clinical Reminder Index. A mailman message will be sent to the person installing this patch. The message will list out the number of entries that contain a zero value in the priority field. The number of entries that were corrected and a final check to make sure that all the bad entries were corrected.

GMPL\*2\*35 - ADD SHAD AND CV TREATMENT FACTORS TO LEGACY VISTA

This patch is being released in conjunction with CPRS GUI v27. CPRS GUI version 27 consists of two host files: OR_PSJ_PSO_27.KID and CPRS_BUNDLE_GUI_27_REQ_REL.KID. These two host files contain software patches that support CPRS GUI v27 functionality. The host files were created to simplify installation at Veterans Health Administration (VHA) facilities.

GMPL\*2\*33 - USERS UNABLE TO VIEW INACTIVE ICD9 CODES

This patch addresses the problem where users were unable to modify current Problem Category Lists to make it assignable. The users cannot tell if the code is Inactive.

GMPL\*2\*32 - GMPL\*2\*31 INFORMATIONAL FOLLOW_UP

Included in patch GMPL\*2\*31 was a clean-up routine GMPL31P. This routine searched out bad ICD9 (file 81) pointers in the PROBLEM LIST file and PROBLEM LIST AUDIT entries. For pointers that included the "~", the "~" was removed and the remaining value was left. If a "-1" was found the pointer to the default ICD9 code 799.99 was put in the place of the "-1".

GMPL\*2\*31 - CORRECT DIAGNOSIS PTR UPDATE IN PROBLEM LIST

This patch corrects the problem of invalid characters (~) appearing in the DIAGNOSIS (pointer to the ICD DIAGNOSIS file \#80) in the PROBLEM FILE (9000011). This modification will also add a check for the ICD code not being found. (-1 being returned instead of pointer from ICD \#80 file search) The problem occurs when adding a problem or changing a problem via the CPRS GUI.

This patch also adds code that will record an audit trail when a Problem comment is modified.

GMPL\*2.0\*28 - CSV – Problem List Compliance

The following functionality has been added to Problem List in support of the Code Set Versioning project:

- Evaluation of problems on the active problem list to identify those entries with codes that are inactive for the current date.
- Display of problems with inactive codes.
- Prompts to edit problem list entries with codes that are inactive for the current date.
- Modifications of Lexicon Search Utility to display diagnoses that have active ICD9 codes for the current date. Only items that have active ICD9 codes for the current date will be selectable.

*See page 14 for more detailed information of this CSV Compliance functionality.*GMPL\*2.0\*26 and GMTS\*2.7\*52 - CPRS/Problem List Enhancements

These patches added the following enhancements to Problem List and Health Summary:

1.  The CPRS List Manager displays Head and Neck Cancer in the Problem List for veterans diagnosed with cancer of the head and/or neck related to nose and throat radium treatment.
2.  The CPRS Health Summary displays Head and Neck Cancer for veterans diagnosed with cancer of the head and/or neck related to nose and throat radium treatment.
3.  The CPRS GUI displays Head and Neck Cancer in the Problem List for veterans diagnosed with cancer of the head and/or neck related to nose and throat radium treatment.
4.  (Available in CPRS v20) The CPRS GUI enables a user to indicate on the problem list that a veteran has cancer of the head and/or neck that is related to nose and throat radium treatments.
5.  (Available in CPRS v20) Upon indicating Head and Neck Cancer on the Problem List, the CPRS GUI associates related services categories to this diagnosis.
6.  (Available in CPRS v20) The CPRS GUI Problem List Clinic Report (remote data view) displays associated related service categories for a diagnosis of head and neck cancer that is indicated on the problem list.

See examples later in this manual for entering MST and Head and/or Neck Cancer conditions.

### GMPL\*2.0\*27 - Clinical Reminders Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch supports the Clinical Reminders Index (PXRM\*1.5\*12), whose goal is to create a new global in the Clinical Reminders namespace, ^PXRMINDX, that is an index of clinical data. Each of the packages whose data Clinical Reminders uses as a finding type is participating in this project.

### GMPL\*2.0\*26 - Head-Neck Cancer/Military Sexual Trauma

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is in response to the Veterans Millennium Health Care and Benefits Act, Copayment Exemptions Software Requirements Specification, dated February 4, 2002. Special Conditions have been added to the Problem List for:

> Head and/or Neck Cancer

> Military Sexual Trauma

### Problem List Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                 |                                                             |                        |
|-----------------------------------------------------------------|-------------------------------------------------------------|------------------------|
| Patch \#                                                    | Description                                             | Release Date       |
| GMPL\*2\*1                                                      | Form Number in Footer                                       | 02/09/95               |
| GMPL\*2\*2                                                      | PGMOV error in Report                                       | 02/02/95               |
| GMPL\*2\*3                                                      | ALLOC Error/Duplicates/AICS API                             | 12/06/95               |
| GMPL\*2\*4                                                      | Fixes Encounter Form/PL Interface                           | 12/15/95               |
| GMPL\*2\*5                                                      | Fix UNDEFs in GMPLPREF & GMPLEDT4                           | 03/07/96               |
| GMPL\*2\*6                                                      | Fix PCE Interface                                           | 03/18/96               |
| GMPL\*2\*7                                                      | Problem List/ Lexicon                                       | 10/04/96               |
| GMPL\*2\*8                                                      | Stop Duplicate Probl                                        | 10/03/96               |
| GMPL\*2\*9                                                      | Duplicate Problems w                                        | 11/01/96               |
| GMPL\*2\*10                                                     | CPRS INTERFACE                                              | 07/07/98               |
| GMPL\*2\*11                                                     | Viewing Selections                                          | 09/09/97               |
| GMPL\*2\*12                                                     | REMOVE DUPLICATE PRO                                        | 07/07/99               |
| GMPL\*2\*13                                                     | ACUTE PROBLEM \*'S NO                                       | 11/12/98               |
| GMPL\*2\*14                                                     | NEW API FOR PROBLEM                                         | 02/11/99               |
| GMPL\*2\*15                                                     | API FOR PROBLEM LIST                                        | 05/05/99               |
| GMPL\*2\*16                                                     | INCONSISTENT PROVIDE                                        | 09/29/99               |
| GMPL\*2\*17                                                     | EDITING PROBLEM LIST                                        | 09/29/99               |
| GMPL\*2\*18                                                     | ADD AUDIT TRAIL TO O                                        | 09/29/99               |
| GMPL\*2\*19                                                     | NEW API VARIABLE (PR                                        | 02/07/00               |
| GMPL\*2\*20                                                     | PROBLEM LIST WARNING                                        | 08/16/00               |
| GMPL\*2\*21                                                     | PROBLEM LIST COMMENT                                        | 05/15/00               |
| GMPL\*2\*22                                                     | Add Lexicon Problem                                         | 05/15/00               |
| GMPL\*2\*23                                                     | MODIFIED CROSS REFERENCE                                    | 05/15/00               |
| GMPL\*2\*24                                                     | Run an ICD9 code 799                                        | 01/18/01               |
| GMPL\*2\*25                                                     | Undefined GMPLCOND Variable                                 | 03/01/02               |
| GMPL\*2\*26                                                     | Head-Neck Cancer/Military Sexual Trauma                     | 05/24/02               |
| GMPL\*2\*27                                                     | Clinical Reminders Index                                    | 11/04                  |
| GMPL\*2\*28                                                     | CSV – Problem List Compliance                               | 08/15/03               |
| GMPL\*2\*31                                                     | CORRECT DIAGNOSIS PTR UPDATE IN PROBLEM LIST FILE           | 5/05                   |
| GMPL\*2\*32                                                     | GMPL\*2\*31 INFORMATIONAL FOLLOW_UP                         | 10/05                  |
| GMPL\*2\*35                                                     | ADD SHAD AND CV TREATMENT FACTORS TO LEGACY VistA           | 8/08                   |
| GMPL\*2\*36                                                     | EXTENSIONS TO ACCOMMODATE SNOMED-CT                         | 5/13                   |
| GMPL\*2\*37                                                     | PROBLEM LIST REPAIR DUE TO SHAD                             | 11/08                  |
| GMPL\*2\*38                                                     | Fix for Problem List Priority Value                         | 2/09                   |
| GMPL\*2\*39                                                     | FIX FOR GENERAL ERRORS IN PROBLEM LIST                      | 11/11                  |
| GMPL\*2\*40                                                     | Erroneous Problem File Cleanup                              |                        |
| GMPL\*2\*41                                                     | CORRECT WINDOWS REPORT FOOTER                               | 11/10                  |
| GMPL\*2\*42                                                     | ICD-10 Remediation                                          | 8/5/2014               |
| GMPL\*2\*44                                                     | ICD-10 Remediation related to Clinical Reminders            | 7/24/2014              |
| <span id="patch_list_patch45" class="anchor"></span>GMPL\*2\*45 | CHANGES TO PROBLEM LIST COMMENTS IN SUPPORT OF NSR 20130312 | (3/8/16)               |
| GMPL\*2\*47                                                     | Clinical Reminders Mapping Target index update              | (3/8/16)               |
| GMPL\*2\*49                                                     | Problem Selection List Enhancements                         | TBD (fall/winter 2017) |

# Orientation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. Make sure you know how to log on, navigate among menus and options, and respond to prompts for data entry. If necessary, ask your Application Coordinator or an IRM staff member to help you. The *DHCP User’s Guide to Computing* provides basic information about general computing and your computer system.
2. Review the Preface, the Table of Contents, and the Introduction in this manual, to understand the organization of Problem List and this manual.
3. If you are the application coordinator, review the Operation section, and, if desired, copy and distribute the appropriate sections to individual users, according to the menus assigned by IRM/ADPAC personnel.
4. Review the following pages in which we describe special keys and commands used in VistA and the Problem List, as well as style conventions used in this manual.

## ### VistA, Problem List, List Manager, and CPRS/Windows Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem List uses the same conventions (in its List Manager and terminal-based version) as Lab, Pharmacy, and other VistA packages. Only a few of the special keys and commands are described here. See the User’s Guide to Computing, for more complete lists of conventions. Problem List in CPRS follows standard Windows and VistA GUI standards and conventions.

Keep in mind that these keys and commands vary somewhat according to the kind of terminal you are using. Also note that your hospital IRM staff or the clinical coordinator can change menus (and even some of the prompts) to fit your hospital needs.

> \<Enter\> The symbol used in computer dialogue examples for the return key. On some keyboards this is the ENTER key or the key with the symbol ↵. Enter \<Enter\> (press the return key) after every response you enter or when you wish to bypass a prompt, accept a default (//), or return to a previous action.

> ? If you enter a question mark after a prompt, the computer will display instructions or a list of choices for responding to that prompt.

> ?? Two question marks will usually cause more detailed instructions to appear, or a list of choices.

> // Double slashes mean a default response has been provided. This will either be the most likely choice, a previously entered response, or the least harmful choice. (Ex.: Are you sure you want to remove this problem? NO//) If you wish to select the default response (NO), just press the return key (indicated in this manual by \<Enter\>). Otherwise enter a different choice.

> + The plus sign moves the screen to the next screen.

> - The minus sign moves you back to the previous screen.

> ^ A single up-arrow, if allowed, terminates a series of questions and returns you to a previous level. You may need to enter ^ several times to exit the program or return to the level you wish. If you want to return to a previous prompt or option, enter ^ and the name of the desired prompt or option.

> ^(#) will take you back to an earlier problem when the problem you are adding has more than five matches (see the Helpful Hints section in this manual for an example).

> \$ A dollar sign next to a problem on the problem list indicates that a clinician needs to verify a transcribed problem.

> \* An asterisk next to a problem indicates that it has been designated an acute problem.

> ( ) Parentheses around an action mean that you can’t select that action in that context. For example, if a patient has no active problems, you cannot choose the action Edit a problem.

### Conventions used in this manual 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Option examples: Menus and examples of computer dialogue that you see on the CRT screen are depicted here in boxes:

> Select Problem List Menu Option: pl Patient Problem List

> Select PATIENT NAME: PLPATIENT,ONE 03-04-14 666123432 NSC VETERAN

> Searching for the patient's problem list...

- CPRS GUI Examples:

> Examples of Problem List in CPRS are graphic captures such as the following:

> ![](problem-list-user-manual-version-2-gmpl-2-60/007.png)

- Reports or Printouts: Reports are depicted here in double-lined boxes:

> --------------------------------------------------------------------------------

> PLPATIENT,TWO (P3333) \| PROBLEM LIST

> --------------------------------------------------------------------------------

> Prob Date Date of Date

> No. Recorded Active Problems Onset Resolved

> --------------------------------------------------------------------------------

> 1\. 2/9/04 Peripheral Vascular Disease Leg/Foot 1991 PROVIDER,TWO

> Due to diabetic neuropathy and old football injury

> 2\. 2/9/04 Cholecystitis 1991 1972 PROVIDER,TWO

> 3\. 2/9/04 Intermittent Claudication 7/92 PROVIDER,TWO

> R profunda femoris occlusion - 90%

• User responses: In computer dialogues, the user response is in boldface.

> Select NEW PERSON NAME: PLPROVIDER,ONE

> NOTE: You can respond to many prompts by typing the first few letters of a name, option, or action.

• Option Selection: Some option names have “mnemonics,” an abbreviation that you can enter rather than the entire option name. Since sites frequently assign their own numbers or letter abbreviations to options, we use the first letter or letters for selecting options in the examples in this manual.

• Explanations: Special notes are in a box, preceded by a pointing finger:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/008.png)</p></th>
<th>A list must be defined before you can use this option.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

+ NOTE:

• Problem Selection: When you are prompted to select a problem from a range of problems (e.g., Select Problem(s) (1-5)), you may select one item or more by using commas or a range of items separated by a dash.

### List Manager Conventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• List Manager Screen Display: The List Manager utility allows Problem List (and other applications) to maintain the header and action portion of a list, while the center display (for example, the problems or the detailed display) scrolls. So if a patient has too many problems to fit within the scrolling portion of the screen, pressing the return key causes that portion of the screen to scroll up while the top and bottom stay unchanged.

Select PATIENT NAME: PLPATIENT,THREE 03-04-14 6666432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 09, 2002@15:22:08 Page: 1 of 1</u>

PLPATIENT,THREE (P2432) 1 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Asthma Bronchial, Onset 1997 4/9/02 LAB-MENTAL HEALTH

+ Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

Q Quit

Select Action: Quit// ED Edit a Problem

The highlighted bar in the middle contains instructions about actions you can take.

For example:

You can type + to move forward or - to move back. To see a list of navigation actions, type two question marks (??) at the Select Action prompt.

### Windows Conventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the CPRS online help.<span id="removed_1" class="anchor"></span>

# Package Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation of Problem List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing Problem List, other implementation steps are mostly optional. These include:

> 1\. Assigning menus and options (required)

> 2\. Assigning the security key (optional)

> 3\. Editing site parameters (optional)

> 4\. Setting User Preferences (optional)

> 5\. Creating selection lists (optional)

> 6\. Creating Encounter Forms (optional)

All functions except \#6 are described in the following pages of the Package Management section. See the Encounter Form Utilities Module User Manual (part of the Integrated Billing V. 2.0 documentation set) for instructions about creating Encounter Forms to use with Problem List. Also see CPRS documentation for further information about using Problem List through CPRS (either the List Manager or the GUI version).

## # Package Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Links to other packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem List is closely linked to other applications: Lexicon Utility, Computerized Patient Record System (CPRS), Data Standardization/Near Term Rapid Turnaround Time (NTRT, Encounter Form (part of Integrated Billing), Health Summary, and Patient Care Encounter (PCE). This linkage should remain transparent to users, but the IRM office and Clinical Coordinators will need to work closely to coordinate all the components. See the User and Technical Manuals of these packages for further instructions, such as how to build an encounter form for your hospital.

## Lexicon 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lexicon Utility can be modified to meet local site needs (for example, to allow nurses to see only nursing terms). See the Appendix in this manual and the Lexicon Utility documentation for information on customizing this package for use with the Problem List application.

## Encounter Forms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Encounter Forms (scannable or otherwise) can be used by clinicians and clerks for data entry of problems into the Problem List. See the Appendix in this manual and the Encounter Form Utilities User Manual (part of the Integrated Billing 2.0 documentation set) for further information.

## CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the release of CPRS in 1999, many sites now use Problem List through the List Manager or GUI version of CPRS, which allows a more integrated view of the patient record. The cover sheet of CPRS displays a patient’s current problems (site or user-configurable) and allows the clinician to click on any of these for immediate information. The Problem tab allows entry, edit, and display of problems.

## ## Menu Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign menus and options as follows:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Common Name</strong></td>
<td><strong>Technical Name</strong></td>
<td><strong>Who</strong></td>
</tr>
<tr class="even">
<td><p><span id="assign_ICD_diagnosis_out_of_order_menu" class="anchor"></span><strong>Assign ICD Diagnoses to Problem List</strong></p>
<p><strong>Note:</strong> This has been marked OUT OF ORDER with GMPL*2.0*49</p></td>
<td>GMPL CODE LIST</td>
<td>PIMS Clerks, Clinical Coordinators (CACs)</td>
</tr>
<tr class="odd">
<td><strong>Patient Problem List</strong></td>
<td>GMPL CLINICAL USER</td>
<td>Clinicians, Nurses, Clinical Coordinators (CACs)</td>
</tr>
<tr class="even">
<td><strong>Problem List Data Entry</strong></td>
<td>GMPL DATA ENTRY</td>
<td>PIMS Clerks, Clinical Coordinators (CACs)</td>
</tr>
<tr class="odd">
<td><strong>Problem List Mgt Menu</strong></td>
<td>GMPL MGT MENU</td>
<td>IRMS, Clinical Coordinators (CACs)</td>
</tr>
<tr class="even">
<td><strong>Problem List User Preferences Menu</strong></td>
<td>GMPL USER PREFS MENU</td>
<td>Clinicians, Nurses, IRMS, Clinical Coordinators (CACs)</td>
</tr>
</tbody>
</table>

## Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <span id="GMPL_IMPRT_UTIL_key" class="anchor"></span>GMPL IMPRT UTIL: The GMPL IMPRT UTIL key is used to access the new option Import Problem Selection List \[GMPL SELECTION LIST IMPORT\]. Users with this access will be responsible for performing the National Problem Selection List updates and for creating/maintaining VISN or Local Problem Selection lists/categories if requested.
- GMPL ICD CODE: The GMPL ICD CODE security key is used by the Problem List package to determine if the current user is trained and authorized to code provider text relating to the ICD Diagnosis codes. Recommended allocation: PIMS Coding Clerks.

## Electronic Signature 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem List doesn’t use electronic signature.

## Legal Requirements i

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific legal requirements for Problem List.

## Code Set Versioning (CSV) Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality has been added to Problem List in support of the Code Set Versioning project.

Problem List is available in two places:

- CPRS GUI Problem List tab
- List Manager Problem List

Both of these provide functionality to enter and manage problems associated with the patient, and all will evaluate problems on the active problem list to identify those entries with codes that are inactive for the current date.

ICD-10 Project

> **NOTE:** With the ICD-10 project, many changes have been made to Problem List and the Lexicon utility, some of which may override Code Set Versioning requirements described here.

The following functionality was added to Problem List in support of the Code Set Versioning project:

Problem List in List Manager

- Evaluates problems on the active problem list to identify those entries with codes that are inactive for the current date.
- Provides a method to display to the user the identified problems with inactive codes.
- Prompts the user to edit problem list entries with codes that are inactive for the current date.
- Uses the Lexicon Search Utility and displays diagnoses that have active SNOMED CT codes for the current date. Only items that have active SNOMED CT codes for the current date will be selectable.

*Adding a Problem*

- When adding a new problem, Problem List uses the Lexicon Search Utility and displays diagnoses that have an active SNOMED CT code for the current date. Only items that have active SNOMED CT codes for the current date will be selectable.
- If the user or clinic has a Problem Selection List assigned, Problem List displays only items that have active SNOMED CT codes for the current date.

*Changing a Problem*

- When changing a problem, Problem List uses the Lexicon Search Utility and display diagnoses that have active SNOMED CT codes for the current date. Only items that have active SNOMED CT codes for the current date will be selectable.

*Saving a Problem*

- When the problem is saved, Problem List evaluates the problem code to ensure that it has an active SNOMED CT code for the current date. If the code is not active, an error message will be displayed to the user.

*Verifying a Problem*

- When verifying a problem on the Problem List, Problem List evaluates the code associated with the problem. If the code is inactive for the current date, OE/RR will display a message to the user stating that the code is not active for the current date and ask the user to edit the problem.

Problem List Selection Lists and Categories

- Problem Selection List functionality was modified to ensure that all selectable problems have an active SNOMED CT code for the current date.
- Problem Selection Lists can be assigned to a user or to a clinic. If a Problem Selection List is defined for a user or a clinic, CPRS GUI uses the list on the CPRS GUI Problems Tab. In addition, OERR List Manager displays the list on the OERR List Manager Problems Tab, and Problem List also uses it. In each interface, the list is displayed as a default common Problem List when a new problem is added.
- Problem List evaluates entries on the Problem Selection List and identify problems with inactive SNOMED CT, ICD-10-CM, and ICD-9-CM codes.
- When adding a problem to a Problem Category, Problem List allows selection of problems that have an active SNOMED CT code for the current date.
- When editing a problem included in a Problem Category, Problem List allows selection of problems that have active SNOMED CT codes for the current date.
- When adding a Problem Category to the Problem Selection List, Problem List evaluates the problems in the Problem Category. If a problem has an inactive code, the Problem Category will not be added to the Problem Selection List, an error message advising the user to edit the entries with inactive codes will be presented to the user, and the user will be returned to the BUILD PROBLEM SELECTION LIST screen.
- When saving the Problem Selection List, Problem List evaluates the problems for active SNOMED CT code for the current date. If an entry has an inactive code, the list will not be saved, an error message advising the user to edit the entries with inactive codes will be presented to the user, and the user will be returned to the BUILD PROBLEM SELECTION LIST screen.
- When assigning new SNOMED CT codes to a problem, Problem List allows selection of codes that are active for the current date.
- Problem List identifies any selection list problem with an SNOMED CT code that has been inactivated.
- Problem List generates a report that identifies the Problem Categories and Problem Selection Lists that include problems with inactivated codes.
- Problem List menu option <span id="Check_Prob_select_List_Prob_codes_option" class="anchor"></span>Check Problem Selection List Problem Codes \[GMPL SELECTION LIST CSV CHECK\] creates a report that identifies the Problem Categories and Problem Selection Lists that include problems with inactivated codes. CACs should update the problems with inactivated codes.

An example of information that is included in the message sent to CACs is included below:

Subj: <span id="Prob_Select_List_code_set_version_review" class="anchor"></span>Problem Selection List Code Set Version review \[#156209\] 09/28/17@08:46

5 lines

From: CODE SET VERSION INSTALL In 'IN' basket. Page 1

------------------------------------------------------------------------------

The following Problem Selection Lists contain one or more problems that have

inactive SNOMED and/or ICD codes attached to them. Any current users or clinics using these Selection Lists, will not be able to add the problems with inactive codes, until the list and the inactive codes are updated. The list may not be assigned to any additional users or clinics until updated.

TEST LIST1:

CARDIO:

Acute Myocardial Infarction (ICD-9-CM 410.9) \<INACTIVE ICD CODE\>

Coronary Artery Disease (ICD-9-CM 414.9) \<INACTIVE ICD CODE\>

Angina Pectoris, Unstable (ICD-9-CM 411.1) \<INACTIVE ICD CODE\>

Chest Pain (ICD-9-CM 786.50) \<INACTIVE ICD CODE\>

Angina Pectoris (ICD-9-CM 413.9) \<INACTIVE ICD CODE\>

Dyspnea (ICD-9-CM 786.09) \<INACTIVE ICD CODE\>

GENERAL:

Headache (ICD-9-CM 784.0) \<INACTIVE ICD CODE\>

Fever (ICD-9-CM 780.6) \<INACTIVE ICD CODE\>

TEST LIST2:

UROLOGY:

Bladder Carcinoma (ICD-9-CM 188.9) \<INACTIVE ICD CODE\>

Impotence (ICD-9-CM 302.72) \<INACTIVE ICD CODE\>

Prostatic Carcinoma (ICD-9-CM 185.) \<INACTIVE ICD CODE\>

Prostatic Hypertrophy, Benign (ICD-9-CM 600.) \<INACTIVE ICD CODE\>

Renal Calculi (ICD-9-CM 592.0) \<INACTIVE ICD CODE\>

Urinary Incontinence (ICD-9-CM 788.30) \<INACTIVE ICD CODE\>

- Problem List developed a new option for CACs and IRM staff to manually initiate evaluation of the PROBLEM SELECTION CATEGORY file (#125.11) for inactivated SNOMED and/or ICD codes. This option performs similar actions as the Problem Selection List CSV Event Protocol. It is manually initiated rather than electronically triggered.
- Problem List evaluates the entries in PROBLEM SELECTION CATEGORY file (#125.11) and identifies any selection list problem with a code that has been inactivated.
- Problem List will generate a report that identifies the Problem Categories and Problem Selection Lists that include problems with inactivated codes.

Example of information that is included in the report:

<span id="_Toc31613587" class="anchor"></span>

The following Problem Selection Lists contain one or more problems that have

inactive SNOMED and/or ICD codes attached to them. Any current users or clinics using these Selection Lists, will not be able to add the problems with inactive codes, until the list and the inactive codes are updated. The list may not be assigned to any additional users or clinics until updated.

TEST LIST1:

CARDIO:

Acute Myocardial Infarction (ICD-9-CM 410.9) \<INACTIVE ICD CODE\>

Coronary Artery Disease (ICD-9-CM 414.9) \<INACTIVE ICD CODE\>

Angina Pectoris, Unstable (ICD-9-CM 411.1) \<INACTIVE ICD CODE\>

Chest Pain (ICD-9-CM 786.50) \<INACTIVE ICD CODE\>

Angina Pectoris (ICD-9-CM 413.9) \<INACTIVE ICD CODE\>

Dyspnea (ICD-9-CM 786.09) \<INACTIVE ICD CODE\>

GENERAL:

Headache (ICD-9-CM 784.0) \<INACTIVE ICD CODE\>

Fever (ICD-9-CM 780.6) \<INACTIVE ICD CODE\>

TEST LIST2:

UROLOGY:

Bladder Carcinoma (ICD-9-CM 188.9) \<INACTIVE ICD CODE\>

Impotence (ICD-9-CM 302.72) \<INACTIVE ICD CODE\>

Prostatic Carcinoma (ICD-9-CM 185.) \<INACTIVE ICD CODE\>

Prostatic Hypertrophy, Benign (ICD-9-CM 600.) \<INACTIVE ICD CODE\>

Renal Calculi (ICD-9-CM 592.0) \<INACTIVE ICD CODE\>

Urinary Incontinence (ICD-9-CM 788.30) \<INACTIVE ICD CODE\>

### CPRS GUI Problem List Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Entry of a new problem only allows selection of SNOMED codes that are active as of the current date. This applies both to the lexicon lookup and to the predefined list of selectable problems and categories.
- Any action taken on an active problem having an inactive ICD code first requires correction/update of that code via the "Change" action.

### *Add Problem* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When adding a new problem, CPRS GUI uses the Problem List Lexicon Search Utility and display diagnoses that have active SNOMED codes for the current date. Only items that have active SNOMED codes for the current date are selectable.
- If the user or clinic has a Problem Selection List assigned, CPRS GUI displays only items that have an active SNOMED and ICD code for the current date.

### *Verify Problem* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When verifying a problem, CPRS GUI evaluates the code associated with the Problem. If the code is inactive for the current date, CPRS GUI displays an error message to the user stating that the SNOMED CT or ICD-10-CM code is not active for the current date and advise the user that the problem can be edited using the change action.

### *Restore Problem* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When replacing a removed problem*,* CPRS GUI evaluates the code associated with the problem. If the code is inactive for the current date, CPRS GUI displays an error message to the user stating that the SNOMED CT or ICD-10-CM code is not active for the current date and then present the user with the change problem screen.

### *Change Problem* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When changing a problem, CPRS GUI uses the Problem List Lexicon Search Utility and displays diagnoses that have active SNOMED codes for the current date. Only items that have active SNOMED codes for the current date are selectable.

![](problem-list-user-manual-version-2-gmpl-2-60/009.png)

## CPRS Problem List Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Problem List is used through CPRS, several CPRS parameters can be set that affect the use of Problem List.

Initial Tab and Cover Sheet Parameters

The tab that displays first when a user starts CPRS may be set by the parameter ORCH INITIAL TAB. This parameter may be set for the site and then overridden at the division and user levels, as needed. If no value is set, the chart will open, by default, to the Cover Sheet. ORCH INITIAL TAB may be set to the following values:

> 1 Cover

> 2 Problems

> 3 Meds

> 4 Orders

> 6 Notes

> 7 Consults

> 8 DC Summ

> 9 Labs

> 10 Reports

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/010.png)</p></th>
<th><p>The number 5 is not one of the possible values. It is reserved.</p>
<p>Additionally, CPRS may be configured to remain on the same tab when the user changes to another patient record. Setting ORCH USE LAST TAB to “yes” will accomplish this. If ORCH USE LAST TAB is set to “no” or not set, the chart will always open to the tab identified by ORCH INITIAL TAB when changing patients.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The criteria for determining what gets loaded into each section of the cover sheet are determined by parameter settings. To set Cover Sheet parameters, use the “CPRS Configuration (Clin Coordinator)” menu option then “GUI Parameters” and then “GUI Cover Sheet Display Parameters” on the CPRS Configuration menu to set Cover Sheet parameters. These parameters may be set for the system, a division, a service, a location, or an individual user. For Problem List, Currently active problems are shown in the list.

Problem List Default Views

The user’s default view on the Problems tab is determined by two different settings. Both the GUI and the List Manager versions of CPRS use the ORCH CONTEXT PROBLEMS parameter. Its value can be set at the SYSTEM and USER levels. The parameter takes the form of a semicolon-delimited string, with the different pieces’ meaning as follows:

> a;b;c;d;e (example: T-180;T;A;1;1329)

> a Begin date

> b End date

> c Status (A = active, I = inactive, B = both, R = removed)

> d If “1”, show all comments as default

> e Provider internal entry number

The user-level value for this parameter can be set using the View \| Filter menu and saving the selected settings as the default. There should be no need to edit the parameter directly at the user level.

Both the GUI and List Manager versions of CPRS use the PROBLEM LIST PRIMARY VIEW field (#125) of the NEW PERSON (#200) file. The contents of the field determine whether the outpatient (clinics) or inpatient (services) view of the problem list will be used, and can also be used to specify clinics or services to include in the list. The field will contain a “C” or “S,” followed by a list of internal entry numbers of clinics and services, separated by a forward slash (/ ) and ending with a trailing forward slash. Here is an example, excerpted from a VA FileMan INQUIRE into the NEW PERSON file for a user:

PROBLEM LIST PRIMARY VIEW: C/4/5/

“C” indicates outpatient (Clinics) view should be used. “S” indicates that the inpatient (Services) view should be used. “4” and “5” are pointers to default clinics or services (depending on “C” or “S”) to include in the view. Others will be hidden. If none are specified, all will be shown.

For users of the GUI, it is best to use the View \| Filter menu to set this field. Save as Default will update it with the selected view and clinics or services to include. Since it is stored in the NEW PERSON file, it is applicable only to the individual user.

User Access and Privileges

If the user holds any of the ORES/ORELSE/PROVIDER keys, that user is viewed as a clinical user, and has full access privileges to all problem list options. If a user holds the OREMAS key, that user is viewed as a clerical user. In that case, the Verify, Remove, Restore, and View Removed options will not be available. If the site parameter requiring verification is set to TRUE, then problems entered will be left in an UNVERIFIED state until a clinical user verifies them. Problems in the UNVERIFIED state are denoted by a dollar sign (\$) inserted at the beginning of the line.

These access levels are also enforced when problems are entered via the encounter form. Problems entered on the encounter form by clerical personnel will be left as UNVERIFIED.

CPRS List Manager and the Problem List package do not operate exactly the same as described above. The Problem List package evaluates the presence/absence of menu options in the user’s menu tree, and determines access accordingly. Since CPRS LM sometimes drops into PL package code, it uses a hybrid method of keys and menu options to determine access.

## Management Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem List Mgt Menu \[GMPL MGT MENU\]

1 Patient Problem List

2 Edit PL Site Parameters

3 <span id="managment_menu_options" class="anchor"></span>Create Problem Selection Lists ...

1 Build Problem Selection List(s) \[GMPL BUILD SELECTION LIST\]

2 Copy Selection List from IB Encounter Form \[GMPL BUILD ENC

FORM LIST\]

\*\*\> Out of order: This option has been disabled due to

the Problem List SNOMED CT implementation.

3 Assign/Remove Problem Selection List \[GMPL ASSIGN LIST\]

4 Delete Problem Selection List \[GMPL DELETE LIST\]

5 Check Problem Selection List Problem Codes \[GMPL SELECTION LIST

CSV CHECK\]

6 Import Problem Selection List \[GMPL SELECTION LIST IMPORT\]

\*\*\> Locked with GMPL IMPRT UTIL

4 List Patients with Problem List data

5 Search for Patients having selected Problem

6 Replace Removed Problem(s) on Patient's List

7 Problem List NTRT Follow-up Report

8 Problem List Freetext Follow-up Report

9 SNOMED in Diagnosis Field Error Report

10 SNOMED in Diagnosis Field Cleanup Report

11 Generate SNOMED in Diagnosis Field Err/Cleanup Rpt

Patient Problem List is described in the Package Operation section of this manual.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/011.png)</p></th>
<th>Problem List NTRT Follow-up Report and Problem List Freetext Follow-up Report are new with GMPL*2*36.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Edit PL Site Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[GMPL PARAMETER EDIT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These site parameters are stored in the Problem List Site Parameters file \#125.99.

This option lets you set five site parameters:

1.  Place a flag on problems entered by clerks so that a clinician must review the problems and verify them. The flag will appear as a dollar sign (\$).
2.  Prompt users to have a chart copy printed.
3.  Search the Lexicon Utility when adding to or editing a problem list. The Lexicon Utility provides standardized text and codes – ICD-10-CM, CPT, SNOMED, and other codes, if they’re available. If you choose not to use the Lexicon Utility, the Problem List will capture *only* the free text that is entered (the Provider Narrative) \[NOTE: Not Recommended\].
4.  Choose whether to display the patient problem list in chronological or reverse chronological order (most recent at top).
5.  Screen duplicate orders. If YES is entered in this field, duplicate problems (those having the same SNOMED and/or ICD code) will NOT be added to the problem list. The primary purpose of this field is to screen entries added via the scannable encounter form.

> Select Problem List Mgt Menu Option: Edit PL Site Parameters

> VERIFY TRANSCRIBED PROBLEMS: NO// YES

> PROMPT FOR CHART COPY: YES, ASK// \<Enter\>

> USE LEXICON UTILITY: YES// \<Enter\>

> DISPLAY ORDER: CHRONOLOGICAL// REVERSE

> SCREEN DUPLICATE ENTRIES: YES// \<Enter\>

> You have PENDING ALERTS

> Enter "VA VIEW ALERTS to review alerts

> Select Problem List Mgt Menu Option: \<Enter\>

> Follow these steps to set the Problem List parameters:

> 1. Go into the Problem List Mgt Menu.

> 2. Select Edit PL Site Parameters.

> 3. Type NO if you don’t wish to have transcribed entries flagged for clinician verification.

> 4. Type NO if you don’t wish to have the users prompted about whether they want to have chart copies printed.

> 5. Type NO if you don’t wish to use the Lexicon Utility to match the problem against a standardized term with corresponding codes (SNOMED, ICD10, etc.).

> 6. Type Reverse if you want your problems displayed in reverse chronological order (most recent at top).

> 7. Enter the @ sign if you don’t want to screen duplicate entries. Otherwise, press the enter key.

### Create Problem Selection Lists \[GMPL BUILD LIST MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for creating and maintaining lists of commonly selected problems (sometimes called a “Pick List”). These lists can help speed up the process of using the Problem List.

After you have a selection list assigned to you, this list will appear on your screen whenever you want to add new problems for a selected patient. Lists may also be assigned to a clinic. If you don’t have an individual problem selection list assigned to you, but a list has been built for a clinic, this list will appear when adding problems for a patient associated with that particular clinic.

Problem Selection Lists Options:

<span id="Create_Prblm_Select_Lists_new_menu_items" class="anchor"></span> Create Problem Selection Lists

> 1 Build Problem Selection List(s) \[GMPL BUILD SELECTION LIST\]

> 2 Copy Selection List from IB Encounter Form \[GMPL BUILD ENC FORM LIST\]

> \*\*\> Out of order: This option has been disabled due to the Problem

> List SNOMED CT implementation.

> 3 Assign/Remove Problem Selection List \[GMPL ASSIGN LIST\]

> 4 Delete Problem Selection List \[GMPL DELETE LIST\]

> 5 Check Problem Selection List Problem Codes \[GMPL SELECTION LIST CSV CHECK\]

> 6 Import Problem Selection List \[GMPL SELECTION LIST IMPORT\]

> \*\*\> Locked with GMPL IMPRT UTIL

*Option 1 allows you to:*

> • Create a pick list

> • Add categories to it

> • Add problems to the categories

> • Assign the list to a user or clinic

The Clinical Coordinator can also use option 3 to assign selection lists to users.

> Option 2 : This option has been disabled due to the Problem List SNOMED CT implementation.

### Create Problem Selection Lists \[GMPL BUILD LIST MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Category: A grouping with or without a header of related problems, such as Cardiology, Musculoskeletal, Vascular, Neurology, etc.

- A list is made up of one or more Categories, each of which contains several related problems.
- Categories can be re-used in other lists.

Problem Selection List Class: The type of class that is associated with this list. Answer with a VISN or Local class type. National class types are reserved for the National Development team and cannot be added by the local sites.

These are the steps to create a problem selection list from scratch. See the next pages for examples and step-by-step instructions on creating problem selection lists.

1. Create a new list by typing in a name at the Select LIST NAME prompt.
2. Create a new problem category using the action EC (Enter/Edit Category).
3. Add problems to the category using the action AD (Add Problems).
4. Continue to create more categories if you wish to have more on your list. Add problems to each category.

REMEMBER: You can respond to many prompts by typing the first few letters of a name, option, or action. Some option names have “mnemonics” — an abbreviation that you can enter rather than the entire option name.

### Build Problem Selection List(s) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you create selection lists by creating one or more problem categories and adding the problems you want in each category.

New categories may be added to this list, or an existing category can be removed. Enter/Edit Category allows you to change the contents (problems) of a category, or create a new one that may be added to this list.

You may also change how each category appears in this list, view each category's sequence number to facilitate resequencing, assign this list to a clinic or user(s), or edit a different list.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select the Create Problem Selection Lists option.

If numbers are used for menu options, you can type in that number or the first letter(s) of the option.

3. Select Build Problem Selection List(s).
4. At the “Select LIST NAME” prompt, type the name of a new selection list by entering a new name.
5. Enter the Problem Selection Class.

Select Create Problem Selection Lists Option: 1 Build Problem Selection List(s)

Select LIST NAME: Dr. Provider's List

Are you adding 'Dr. Provider's List' as

a new PROBLEM SELECTION LIST (the 9TH)? No// y (Yes)

PROBLEM SELECTION LIST CLASS: ?

Enter the Class for this selection list.

National lists are reserved for National Development and cannot be edited

by sites.

Choose from:

V VISN

L Local

PROBLEM SELECTION LIST CLASS: L Local

Searching for the list ...

<u>BUILD PROBLEM SELECTION LIST Apr 29, 2002@10:46:52 Page: 1 of 1</u>

Last Modified: \<new list\> 0 categories

<u>Dr. Provider's List</u>

No items available.

\+ Next Screen - Prev Screen ?? More actions

AD Add Category to List SQ Resequence Categories VW View w/wo Seq Numbers

RM Remove Category CD Edit Category Display CL Change Selection Lists

EC Enter/Edit Category SS Assign List SV Save List and Quit

6. At the “Select Action” prompt, type EC to create a new Category.
7. Type a name for a category you wish to have on your list.

Select Action: Quit// EC

Select CATEGORY NAME: Cardiovascular

ARE YOU ADDING ‘Cardiovascular’ AS A NEW PROBLEM SELECTION CATEGORY (THE 1ST)? YES

*The screen is then redisplayed, with a new list of actions for adding, removing, and editing problems.*

After you have built one category containing problems, repeat the process to add more categories to your list.

*Example: Adding problems to category*

Searching for the list

<u>BUILD PROBLEM SELECTION LIST Apr 29, 2002@10:46:52 Page: 1 of 1</u>

Last Modified: \<new list\> 0 categories

<u>Dr. Provider's List</u>

No items available.

\+ Next Screen - Prev Screen ?? More actions

AD Add Category to List SQ Resequence Categories VW View w/wo Seq Numbers

RM Remove Category CD Edit Category Display CL Change Selection Lists

EC Enter/Edit Category SS Assign List SV Save List and Quit

Q Quit

Select Action: Quit// ec Enter/Edit Category

Select CATEGORY NAME: Cardiovascular

Are you adding 'Cardiovascular' as

a new PROBLEM SELECTION CATEGORY (the 4TH)? No// y (Yes)

Searching for the problems ...

AD Add Problems SQ Resequence Problems SV Save Category and Quit

RM Remove a Problem DL Delete Category CC Change Categories

ED Edit Problems VW View w/wo Seq Numbers Q Quit

Select Item(s): Quit//

8. At the “Select Action” prompt, type AD for Add Problems.
9. Type the name of a problem for this category.

*If there is more than one match for this problem, choose the one you will see most frequently in your practice.*  
10. Accept the defaults for Display Text, SNOMED CT, ICD CODE, and SEQUENCE, or enter new values.

Select Item(s): Quit// AD Add Problems

PROBLEM: HYPERTENSION

338 matches found

1 FH: Hypertension (SNOMED CT 160357008)

2 H/O: hypertension (SNOMED CT 161501007)

3 Renal hypertension (SNOMED CT 28119000)

4 Ocular hypertension (SNOMED CT 4210003)

5 Benign hypertension (SNOMED CT 10725009)

Type "^" to STOP or Select 1-5: 1

DISPLAY TEXT: FH: Hypertension (SCT 160357008)

The following SNOMED CT & ICD-10-CM Code(s) are associated with the problem

you selected:

SNOMED CT: 160357008 ICD-10-CM: R69.

... Yes? YES

SEQUENCE: 1//

11. Continue to enter all the problem names you want included in this category; then press return at the Problem prompt.

PROBLEM: OBESITY

72 matches found

1 Obesity (SNOMED CT 414916001)

2 FH: Obesity (SNOMED CT 160311006)

3 H/O: obesity (SNOMED CT 161453001)

4 Morbid obesity (SNOMED CT 238136002)

5 Simple obesity (SNOMED CT 415530009)

Type "^" to STOP or Select 1-5: 1

DISPLAY TEXT: Obesity (SCT 414916001)

The following SNOMED CT & ICD-10-CM Code(s) are associated with the problem

you selected:

SNOMED CT: 414916001 ICD-10-CM: R69.

... Yes? YES

SEQUENCE: 2//

PROBLEM:

<u>EDIT PROBLEM CATEGORY Apr 29, 2002@10:55:51 Page: 1 of 1</u>

Last Modified: \<new category\> 2 problems

Cardiovascular

1 FH: Hypertension (SCT 160357008) (ICD-10-CM R69.)

2 Obesity (SCT 414916001) (ICD-10-CM R69.)

b <span class="mark">+ Nextt Screen – Prev Screen ?? More Actions</span> AD Add Problems SQ Resequence Problems SV Save Category and Quit

RM Remove a Problem DL Delete Category CC Change Categories

ED Edit Problems VW View w/wo Seq Numbers Q Quit

Select Item(s): Quit//

12. If you want to create more categories, type CC for Change Categories, then enter a new category name at the “Select CATEGORY NAME” prompt, and repeat the previously described process.

*Adding more categories*

Select Item(s): Quit// AD Add Problems

PROBLEM: STROKE

126 matches found

1 Heat stroke (SNOMED CT 52072009)

2 Embolic stroke (SNOMED CT 371041009)

3 Neonatal stroke (SNOMED CT 371121002)

4 Ischemic stroke (SNOMED CT 422504002)

5 Completed stroke (SNOMED CT 25133001)

Type "^" to STOP or Select 1-5: 5

DISPLAY TEXT: Completed stroke (SCT 25133001)

The following SNOMED CT & ICD-10-CM Code(s) are associated with the problem

you selected:

SNOMED CT: 25133001 ICD-10-CM: R69.

... Yes? YES

SEQUENCE: 1//

PROBLEM: TOURETTE SYNDROME

2 matches found

1 Gilles de la Tourette's syndrome (SNOMED CT 5158005)

2 Dysphonia of Gilles de la Tourette's syndrome (SNOMED CT 23772009)

Type "^" to STOP or Select 1-2: 1

DISPLAY TEXT: Gilles de la Tourette's syndrome (SCT 5158005)

The following SNOMED CT & ICD-10-CM Code(s) are associated with the problem

you selected:

SNOMED CT: 5158005 ICD-10-CM: R69.

... Yes? YES

SEQUENCE: 2//

PROBLEM: EPILEPSY

206 matches found

1 Epilepsy (SNOMED CT 84757009)

2 FH: Epilepsy (SNOMED CT 160341008)

3 H/O: epilepsy (SNOMED CT 161480008)

4 Motor epilepsy (SNOMED CT 307356008)

5 Visual epilepsy (SNOMED CT 39194005)

Type "^" to STOP or Select 1-5: 1

DISPLAY TEXT: Epilepsy (SCT 84757009)

The following SNOMED CT & ICD-10-CM Code(s) are associated with the problem

you selected:

SNOMED CT: 84757009 ICD-10-CM: R69.

... Yes? YES

SEQUENCE: 3//

<u>EDIT PROBLEM CATEGORY April 29, 2002 17:08:53 Page: 1 of 1</u>

Last Modified: \<new category\> 3 problems

<u>Neurology</u>

1 Completed stroke (SCT 25133001) (ICD-10-CM R69.)

2 Gilles de la Tourette's syndrome (SCT 5158005) (ICD-10-CM R69.)

3 Epilepsy (SCT 84757009) (ICD-10-CM R69.)

<span class="mark">+ Nextt Screen – Prev Screen ?? More Actions</span>

AD Add Problems SQ Resequence Problems SV Save Category and Quit

RM Remove a Problem DL Delete Category CC Change Categories

ED Edit Problems VW View w/wo Seq Numbers Q Quit

Select Item(s): Quit// \<Enter\>

<u>BUILD PROBLEM SELECTION LIST April 29, 2002 17:11:36 Page:1 of 1</u>

Last Modified: \<new list\> 2 categories

<u>Mirph's List</u>

1 <u>Cardiovascular</u>

FH: Hypertension (SCT 160357008) (ICD-10-CM R69.)

Obesity (SCT 414916001) (ICD-10-CM R69.)

2 <u>Neurology</u>

Completed stroke (SCT 25133001) (ICD-10-CM R69.)

Gilles de la Tourette's syndrome (SCT 5158005) (ICD-10-CM R69.)

Epilepsy (SCT 84757009) (ICD-10-CM R69.)

+ Next Screen - Prev Screen ?? More actions

AD Add Category to List SQ Resequence Categories VW View w/wo Seq Numbers

RM Remove Category CD Edit Category Display CL Change Selection Lists

EC Enter/Edit Category SS Assign List SV Save List and Quit

Q Quit

Select Action: Quit// \<Enter\>Build Problem Selection List(s)cont’d)

This option also lets you add problem categories to an existing list.

New categories may be added to this list, or an existing one removed; Enter/Edit Category allows you to change the contents (problems) of a category, or create a new one that may be added to this list.

Other actions allow you to change how each category appears in this list, view each category's sequence number to facilitate resequencing, assign this list to a clinic or user(s), or edit a different list.

  
Example: Editing a Problem Selection List1. Go into the Problem List Mgt Menu.

2. Select Create Problem Selection Lists.
3. Select Build Problem Selection List(s).
4. At the “Select LIST NAME” prompt, type the name of a selection list that you wish to add categories to.

Select Create Problem Selection Lists Option: B Build Problem Selection List(s)

Select LIST NAME: LIST 2

Searching for the list ...

<u>BUILD PROBLEM SELECTION LIST April 29, 2002 16:42:17 Page 1 of 2</u>

<u>Last Modified: April 20, 2002 3 categories</u>

LIST 2

1 <u>Diabetes</u>

Diabetes Mellitus (SCT 73211009) (ICD-10-CM R69.)

FH: Hypertension (SCT 160357008) (ICD-10-CM R69.)

Myocardial Infarction (SCT 22298006) (ICD-10-CM R69.)

2 <u>Miscellaneous</u>

Malignant essential hypertension (SCT 78975002) (ICD-10-CM R69.)

Chronic Lung Disease (SCT 413839001) (ICD-10-CM R69.)

Myocardial Infarction (SCT 22298006) (ICD-10-CM R69.)

+ Next Screen - Prev Screen ?? More actions

AD Add Category to List SQ Resequence Categories VW View w/wo Seq Numbers

RM Remove Category CD Edit Category Display CL Change Selection Lists

EC Enter/Edit Category SS Assign List SV Save List and Quit

Q Quit

Select Action: Quit// AD5. At the “Select Action” prompt, type AD to add existing problem categories to your selection list.

Example: Adding an existing category to your list, and then adding a new problem to that category

Select CATEGORY NAME: PSYCHOLOGY

HEADER: PSYCHOLOGY// \<Enter\>

SEQUENCE: 1// \<Enter\>

<u>BUILD PROBLEM SELECTION LIST April 29, 2002 16:42:17 Page 1 of 1</u>

Last Modified: May 01, 2004 6 problems

1 PSYCHOLOGY

Alcohol Abuse (SCT 15167005) (ICD-10-CM R69.)

Drug Abuse (SCT 26416006) (ICD-10-CM R69.)

Severe Major Depression (SCT 450714000) (ICD-10-CM R69.)

+ Next Screen - Prev Screen ?? More actions

AD Add Category to List SQ Resequence Categories VW View w/wo Seq Numbers

RM Remove Category CD Edit Category Display CL Change Selection Lists

EC Enter/Edit Category SS Assign List SV Save List and Quit

Q Quit

Select Action: EC

<u>EDIT PROBLEM CATEGORY April 29, 2002 15:32:17 Page: 1 of 1</u>

Last Modified: April 20, 2002 4 problems

<u>PSYCHOLOGY</u>

1 Alcohol Abuse (SCT 15167005) (ICD-10-CM R69.)

2 Drug Abuse (SCT 26416006) (ICD-10-CM R69.)

3 Sever Major Depression (SCT 450714000) (ICD-10-CM R69.)

+ Next Screen - Prev Screen ?? More actions

AD Add Problems SQ Resequence Problems SV Save Category and Quit

RM Remove a Problem DL Delete Category CG Change Categories

ED Edit Problems VW View w/wo Seq Numbers Q Quit

Select Item(s): Quit// AD Add Problem(s)

PROBLEM: Hypertension*Etc. (as described on the previous pages)*6. Type the name of an existing category.

7. Accept the HEADER and SEQUENCE defaults or enter new values.

*Build Problem Selection List Screen is displayed.*8. Type EC at the Select Action prompt.

*Edit Problem Category Screen is displayed*9. Select AD to add problems.

10. Repeat the process described on the previous pages.

The screen will be re-displayed with your problem categories after you enter \<Enter\> to the “Select CATEGORY NAME: prompt. You can add more categories or quit.

### Copy Selection List from IB Encounter Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This option was removed as a result of the project to begin using ICD-10 codes.

### Assign/Remove Problem Selection List \[GMPL ASSIGN LIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you assign or remove selection lists to users, clinics, divisions, or the system.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select the Create Problem Selection Lists option.
3. Select Assign/Remove Problem Selection List.
4. At the “Default Problem Selection List Display may be set for the following” prompt, type the entity (User, Location, Division, or System) that you wish to assign a selection list to.
5. At the “Select \<ENTITY\>” prompt, type the value of the entity you are assigning a list to.

Select Create Problem Selection Lists Option: A Assign/Remove Problem Selection List

Default Problem Selection List Display may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[XXXX.MED.VA.GOV\]

Enter selection: User NEW PERSON

Select NEW PERSON NAME: PROVIDER, ONE

--- Setting Default Problem Selection List Display for User: PROVIDER, ONE---

Selection List: // LIST 1 Local

To remove a selection list from one of the entities, follow the steps below.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select Create Problem Selection Lists.
3. Select Assign/Remove Problem Selection List.
4. At the “Default Problem Selection List Display may be set for the following” prompt, type the entity (User, Location, Division, or System) that you wish to remove a selection list from.
5. At the “Select \<ENTITY\>” prompt, type the value of the entity you are removing a list from.
6. At the “Selection List: \<LIST NAME\>//” prompt, type an “@” symbol and hit enter to remove the selection list from the corresponding entity.

Select Create Problem Selection Lists Option: A Assign/Remove Problem Selection List

Default Problem Selection List Display may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[XXXX.MED.VA.GOV\]

Enter selection: User NEW PERSON

Select NEW PERSON NAME: PROVIDER, ONE

--- Setting Default Problem Selection List Display for User: PROVIDER, ONE---

Selection List: LIST 1// @ ...deleted

Default Problem Selection List Display may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[CPRS31.xxx.VA.GOV\]

Enter selection: 1 User NEW PERSON

Select NEW PERSON NAME: PROVIDER, ONE

--- Setting Default Problem Selection List Display for User: PROVIDER, ONE ---

Selection List:

### Delete Problem Selection List \[GMPL DELETE LIST\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will let you delete a problem selection list that is no longer in use. After you select a list name, the system checks to see if this list is assigned to any User, Clinic, Division, or System, and if so, doesn’t allow you to delete the list.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select Create Problem Selection Lists.
3. Select Delete Problem Selection List.
4. At the “Select LIST NAME” prompt, type the name of a selection list that you wish to delete.

Select Create Problem Selection Lists Option: 4 Delete Problem Selection List

Select LIST NAME: LIST 1 Local

Checking the Default Problem Selection List parameter for use of this list ...

No other parameter settings found.

Are you sure you want to delete this list? NO// YES

Deleting LIST 1 selection list ...

DONE.

If the list being deleted is also assigned to any users in the NEW PERSON file, those assignments will be deleted as well.

Checking the NEW PERSON file for any pointers to this list and removing them...

No pointers found.

If the list is currently assigned to any users, clinics, division, or system, you will be notified and the list will not be deleted:

Select Create Problem Selection Lists Option: D Delete Problem Selection List

Select LIST NAME: LIST 2

Checking the Default Problem Selection List parameter for use of this list .....

CANNOT DELETE

This list is currently assigned to the following entities:

User: PROVIDER, ONE

Clinic: PRIMARY CARE

## Check Problem Selection List Problem Codes \[GMPL SELECTION LIST CSV CHECK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will scan all the current selection lists in the system for any problems that have inactive SNOMED CT and/or ICD codes. A report is displayed containing the selection list name(s), categorie(s), and problems with the inactive codes.

Problems with inactive SNOMED concept codes will be identified with \<INACTIVE SCT

CODE\>, inactive ICD codes will be identified with \<INACTIVE ICD CODE\>,

and if both SNOMED & ICD codes are inactive: \<INACTIVE SCT/ICD CODE\>.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select Create Problem Selection Lists.
3. Select Check Problem Selection List Problem Codes.
4. At the “DEVICE: HOME//” prompt, choose a device to print the report to.

Code Set Version Review of Problem Selection Lists Page: 1

--------------------------------------------------------------------------

The following Problem Selection List(s) contain one or more problems that

have inactive SNOMED and/or ICD codes attached to them. Any current users

or clinics using these Selection Lists, will not be able to add the

problems with inactive codes, until the list and the inactive codes are

updated. The list may not be assigned to any additional users or clinics

until updated.

TEST LIST:

CARDIO:

Acute Myocardial Infarction (ICD-9-CM 410.9) \<INACTIVE ICD CODE\>

Coronary Artery Disease (ICD-9-CM 414.9) \<INACTIVE ICD CODE\>

Angina Pectoris, Unstable (ICD-9-CM 411.1) \<INACTIVE ICD CODE\>

Chest Pain (ICD-9-CM 786.50) \<INACTIVE ICD CODE\>

Angina Pectoris (ICD-9-CM 413.9) \<INACTIVE ICD CODE\>

Dyspnea (ICD-9-CM 786.09) \<INACTIVE ICD CODE\>

GENERAL:

Headache (ICD-9-CM 784.0) \<INACTIVE ICD CODE\>

Fever (ICD-9-CM 780.6) \<INACTIVE ICD CODE\>

UROLOGY:

Bladder Carcinoma (ICD-9-CM 188.9) \<INACTIVE ICD CODE\>

Impotence (ICD-9-CM 302.72) \<INACTIVE ICD CODE\>

Type \<Enter\> to continue or '^' to exit:

## Import Problem Selection List \[GMPL SELECTION LIST IMPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is an import utility that will assist in the addition and distribution of National problem selection list content. This utility or menu option is locked with the new GMPL IMPRT UTIL security key and should only be assigned to CAC users.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select Create Problem Selection Lists.
3. Select Import Problem Selection List.
4. At the “Select the import method:” prompt, type the import method that you would like to use. Both methods require the selection list content to be in a specific spreadsheet format and saved as a comma separated value (.CSV) file.
5. If utilizing the "HF" method, the CSV host file must reside on an accessible host system.

Select Create Problem Selection Lists Option: 6 Import Problem Selection List

Select one of the following:

HF CSV host file

WEB CSV file from a web site

Select the import method: HF CSV host file

Enter a path: USER\$:\[TEMP\]// USER\$:\[USER1\]

The following CSV files were found in USER\$:\[USER1\]

SELECTION_LIST_CONTENT1.CSV;1

SELECTION_LIST_CONTENT2.CSV;1

Enter a file name: SELECTION_LIST_CONTENT1.CSV;1

Starting the import process ...

6. If utilizing the "WEB" method, the CSV host file must reside on an accessible website.

Select Create Problem Selection Lists Option: 6 Import Problem Selection List

Select one of the following:

HF CSV host file

WEB CSV file from a web site

Select the import method: WEB CSV file from a web site

Input the URL for the CSV file: http://vista.med.va.gov/cprs/docs/pl_content_upv

Starting the import process ...

Do you want to review the problem selection list contents? Y//

Selection List Contents To Be Imported

Selection List Name: VA-National Problem Selection List

List Class: National Category Class: National

Category Name: VA-Primary Care

Subheader: Primary Care (VA) Category Sequence: 1

Prob SNOMED CT SNOMED CT

Seq Concept Designation ICD Code SNOM

--------------------------------------------------------------------------------

1 49436004 1230726010 I48.91 AF-

2 15167005 25750014 F10.10 Alco

3 371434005 1210092019 F10.21 Hist

4 61582004 102311013 J30.9 Alle

5 271737000 406636013 D64.9 Anem

6 48694002 81133019 F41.9 Anxi

7 195967001 301485011 J45.909 Asth

8 236646007 2470105014 N40.1/N13.8 Beni

9 254902007 2773349010 N40.0 Beni

10 193699007 298251016 H54.0 Blin

11 22950006 38553019 H54.40 Blin

12 53741008 2536394018 I25.10 CAD

13 413838009 2534671011 I25.9 Chro

Col\> 1 \|Press \<PF1\>H for help\| Line\> 22 of 775 Screen\> 1 of 36

Do you want to save the imported list contents? N// YES

Import process completed successfully.

If there are any formatting or content errors, they will be listed and the import will be aborted.

Starting the import process ...

Add/delete cell cannot be empty. Must contain \# (to add) or @ (to delete).

Please verify cell in import file and correct any errors.

Name cannot contain the "~" character.

Error: List class cannot be empty.

Error: Invalid Category class value, DIVISION.

Category Sequence: Cat Seq 1 is invalid.

Error: Category name cannot be empty.

For category sequence \#Cat Seq 1.

SNOMED CT Concept: D8475700 is invalid.

ICD Code: R5T. is invalid.

Error: Problem sequence cannot be empty.

'%' is an invalid character. Must contain \# (to add) or @ (to delete).

Please verify cell in import file and correct any errors.

Problem Sequence: Prob Seq 3 is invalid.

SNOMED CT Designation: 2920839016 is invalid.

Error: Check failed, problem description does not match that of system.

SNOMED CT Designation: 301480018 is invalid.

Error: Check failed, designation code does not match that of system.

Import process aborted due to validation errors.

### List Patients with Problem List data \[GMPL PATIENT LISTING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will generate a listing of all patients identified as having problem lists.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select List Patients with Problem List data.
3. Type a device (printer) name for the list to print to (or accept the default of HOME if you want the list displayed on your screen).

Select Problem List Mgt Menu Option:: L List Patients with Problem List data

....SORRY, LET ME THINK ABOUT THAT A MOMENT....................

DEVICE: HOME// \<Enter\>

PROBLEM LIST PATIENT LISTING 04/29/02 PAGE 1

<u>Patient Name \# Active/Inactive</u>

PLPATIENT,ONE 2 0

PLPATIENT,TWO 1 0

PLPATIENT,THREE 3 1

PLPATIENT,FOUR 2 1

PLPATIENT,FIVE 2 0

PLPATIENT,SIX 4 0

PLPATIENT,SEVEN 3 0

PLPATIENT,EIGHT 30 8

PLPATIENT,NINE 13 2

PLPATIENT,TEN 6 2

PLPATIENT,ELEVEN 6 0

Total of 11 patients found

Press RETURN to continue or '^' to exit

Select Problem List Mgt Menu Option: \<Enter\>

### Search for Patients having selected Problem \[GMPL PROBLEM LISTING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you print or display lists of all patients who have the same problem.

Steps to use option:1. Go into the Problem List Mgt Menu.

2. Select Search for Patients having selected Problem.
3. Type the problem name or the ICD9 code.
4. Type a device (printer) name for the list to print to (or accept the default of HOME if you want the list displayed on your screen).

Select Problem List Mgt Menu Option:: S Search for Patients having selected Problem

Select PROBLEM: heart failure

SEARCHING...................

The following 4 matches were found:

1: Heart failure

2: Heart Failure, Congestive

3: Left Heart Failure

4: Cor Pulmonale, Chronic (RIGHT HEART FAILURE)

SELECT 1-4, '^\<NUMBER\>' TO JUMP, '^' OR \<ENTER\>: 2

Select STATUS: ACTIVE// BOTH

DEVICE: HOME// \<Enter\>

PATIENTS WITH 'HEART FAILURE, CONGESTIVE' 04/29/02 PAGE 1

<u>Patient Name Status</u>

PLPATIENT,TWO active

PLPATIENT,THREE active

PLPATIENT,FIVE inactive

PLPATIENT,XEVEN active

Total of 4 patients found

Press RETURN to continue or ‘^’ to exit \<Enter\>

Select Problem : \<Enter\>

## ### Replace Removed Problems on Patient’s List \[GMPL REPLACE PROBLEMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to list all the problems that have been removed from a selected patient’s problem list and place any of them back on the problem list.

Some sites might want to limit the Remove Problem action, as well as this option, to those with access to the Management Menu.

Steps to use option:1. Type the name of the patient.

2. A list of problems that have been removed for this patient is displayed.
3. If you wish to replace any of these problems on the patient’s list, type the number of the problem(s).
4. The name of the problem you selected is displayed, followed by a prompt asking you if you’re sure. If you’re sure you wish to replace this problem, type Yes.

> Select Problem List Mgt Menu Option: R Replace Removed Problems on Patient's List

> Select PATIENT NAME: PLPATIENT,FIVE 10-15-35 666034567 SC VETERAN

> A: Known allergies

> D: 01/31/02 08:44

> ...HMMM, JUST A MOMENT PLEASE.........

> REMOVED PROBLEMS FOR PLPATIENT,FIVE (P4567):

> Problem Removed By Whom

> ---------------------------------------------------------------------

> 1 Empyema, Tuberculous 8/3/01 PLPROVIDER,TWO

> 2 Bronchitis

> 3 Arm Pain

> 4 Chest Wall Pain 1/19/02 PLPROVIDER,ONE

> 5 Chest Wall Pain 1/19/02 PLPROVIDER,ONE

> 6 Diabetic autonomic neuropathy 1/21/02 PLPROVIDER,THREE

> Select the problem(s) you wish to replace on this patient's list: 6

> Replacing problem(s) on patient's list ...

> Diabetic autonomic neuropathy

> Are you sure you want to do this? NO// YES

> \< DONE \>

<span id="newreports" class="anchor"></span>New Problem List Reports in VistA

### Problem List NTRT Follow-up Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report allows sites to evaluate problems with valid SNOMED CT Concept codes, which were unmapped to ICD at the time of entry.

The report may be filtered by Medical Center Division, Provider(s), and Time Interval.

Steps to use option:

1.  Select Problem List Management Menu Option:
2.  Select (7) Problem List NTRT Follow-up Report.
3.  Select Division: ALL or a specific Division.
4.  Indicate the NTRT Status for the report.

Select one of the following:

1.  0 ALL
2.  1 Pending
3.  2 Completed
5.  Select Specific Provider(s)? enter one or more providers.
6.  Select Start Modification Date \[Time\]: T-10 (month, day and year display).
7.  Select Ending Modification Date \[Time\]: Now (month, day & year and time display).
8.  Select DEVICE: HOME// Home (CRT) or Home;80;999 or TELNET PORT (or Device Name;/settings
9.  View PROBLEM LIST NTRT MAPPING REPORT

Select Problem List Mgt Menu Option: 7 Problem List NTRT Follow-up Report

--- Problem List NTRT Mapping Follow-up Report ---

Select division: ALL//

NTRT Status? ALL// ?

Indicate the NTRT Status for the report.

Select one of the following:

0 All

1 Pending

2 Completed

NTRT Status? ALL// All

Specific Provider(s)? NO//

Start Modification Date \[Time\]: T-30// (SEP 05, 2017)

Ending Modification Date \[Time\]: NOW// (OCT 05, 2017@07:45)

DEVICE: HOME// TELNET PORT

Page 1

================================================================================

P R O B L E M L I S T N T R T M A P P I N G R E P O R T

CAMP MASTER

for Problems Modified: 09/05/2017 to 10/05/2017 Printed: 10/05/2017 07:45

Provider Patient Modified Service Clinic NTRT Map

Narrative Status

================================================================================

PROVIDER,O TWO,I (1002) 09/27/17 n/a PCM PENDING

Allergic diarrhea

SCT: 49237006 ==\> R69.

PROVIDER,O TWO,I (1002) 09/27/17 n/a PCM PENDING

Application site rash

SCT: 95371007 ==\> R69.

PROVIDER,O TWO,I (1002) 09/25/17 n/a PCM PENDING

Allergic Disorder of Digestive System

SCT: 420373003 ==\> R69.

PROVIDER,T SEVEN,O (0607) 09/25/17 n/a PCM PENDING

Neck pain

SCT: 81680005 ==\> R69.

PROVIDER,T THIRTY,I (0830) 09/25/17 n/a PCM PENDING

Acute dermatitis (SCT 26435006)

SCT: 26435006 ==\> R69.

PROVIDER,T THIRTY,I (0830) 09/23/17 n/a PCM PENDING

Insomnia (SCT 193462001)

SCT: 193462001 ==\> R69.

PROVIDER,T THIRTY,I (0830) 09/22/17 n/a PCM PENDING

Chronic obstructive lung disease (SCT 13645005)

SCT: 13645005 ==\> R69.

PROVIDER,T THIRTY,I (0830) 09/21/17 n/a PCM PENDING

Diabetes mellitus AND insipidus with optic atrophy AND deafness

SCT: 70694009 ==\> R69.

PROVIDER,T THIRTYFIVE,I (0835) 09/21/17 n/a PCM PENDING

Tumor of ear, nose and throat

SCT: 254467007 ==\> R69.

### Problem List Freetext Follow-up Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report allows sites to evaluate uncoded free text problems that have been entered by one or more providers over a specified time interval.

Steps to use option:

1.  Select Problem List Management Menu Option:
2.  Select (8) Problem List Freetext Follow-up Report.
3.  Select Division: ALL or a specific Division.
4.  Indicate the NTRT Status for the report.

> Select one of the following:  
> 0 ALL

> 1 Pending

> 2 Completed

> Select Specific Provider(s)? enter one or more providers.

5.  Select Start Modification Date \[Time\]: T-10 (month, day and year display).
6.  Select Ending Modification Date \[Time\]: Now (month, day & year and time display).
7.  Select DEVICE: HOME// Home (CRT) or Home;80;999 or TELNET PORT (or Device Name;/settings
8.  View PROBLEM LIST Freetext Follow-UP REPORT

Select Problem List Mgt Menu Option: 8 Problem List Freetext Follow-up Report

--- Problem List Freetext Follow-up Report ---

Select division: ALL//

Specific Provider(s)? NO//

Print Comments? YES//

Start Modification Date \[Time\]: T-30// (APR 24, 2017)

Ending Modification Date \[Time\]: NOW// (MAY 24, 2017@07:53)

DEVICE: HOME// TELNET PORT

Page 1

=============================================================================

P R O B L E M L I S T F R E E T E X T F O L L O W - U P R E P O RT

CAMP MASTER

for Problems Modified: 04/24/2017 to 05/24/2017 Printed: 05/24/2017 07:53

Provider Patient Modified Service Clinic NTRT Narrative Requested

=============================================================================

PROVIDER,O ONE,O (0601) 04/30/17 n/a PCM True

Financial Anxiety

Comments:

pt is extremely concerned about his exorbitant medical bills.

PROVIDER,O ONE,O (0601) 04/30/17 n/a PCM True

Anxiety anxiety

Comments:

pt is anxious about his anxiety.

PROVIDER,O TWO,I (1002) 04/30/17 n/a PCM False

HTN anxiety

PROVIDER,T SEVEN,O (0607) 04/25/17 AMBULA n/a True

Financial Anxiety

Comments:

pt is concerned about his enormous medical bill

PROVIDER,T THIRTY,I (0830) 05/01/17 n/a CARDIO True

Financial anxiety

Comments:

pt is very concerned about his enormous medical bills

PROVIDER,T THIRTY,I (0830) 05/08/17 n/a CARDIO True

Peter Pan anxiety

Comments:

pt is terrified to growing up

PROVIDER,T THIRTY,I (0830) 05/08/17 n/a CARDIO True

SVT

Comments:

Superficial Venous Thrombosis

PROVIDER,T THIRTYTHRE,I (0833) 05/08/17 n/a CARDIO True

Mapping Anxiety

Comments:

pt worried that his problem won't be found in SNOMED CT

PROVIDER,T THIRTYTHRE,I (0833) 05/09/17 n/a CARDIO True

Dulcinea fixation

Comments:

pt thinks he's Don Quixote

PROVIDER,T THIRTYTHRE,I (0833) 05/09/17 n/a CARDIO True

hysteria anxiety

Comments:

used freetext problem button

### SNOMED in Diagnosis Field Error Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report goes back to the last Problem file cleanup runtime and identifies any occurrences where SNOMED codes have been saved in the Diagnosis field where an ICD code should be.

Steps to use option:

1.  Select Problem List Management Menu Option:
2.  Select (9) SNOMED in Diagnosis Field Error Report.

Sample Error Report:

Erroneous Problem File Record Entries Report

\*\*NOTE\*\*: This report is retroactive as of the last Problem file scan

runtime: Jul 09, 2015@13:00:32. This report will expire and be purged from

the system in 30 days. If the Generate SNOMED in Diagnosis Field

Err/Cleanup Rpt \[GMPL GENERATE DIAG RPTS\] menu option is run prior to the

30 days, then this report will expire on the date/time the option is run.

Whichever comes first.

A scan of your system's Problem file \#9000011 has been performed for

possible errors. The following 9 record entries contain a SNOMED CT

concept code in the Diagnosis field \#.01. This report contains 4 columns.

Please scroll to the right to see a full display of the Problem text.

These record entries will be corrected and upon completion, a separate

MailMan message will be sent to the installer containing instructions on

how to access the cleanup report.

DATE LAST

IEN MODIFIED DIAGNOSIS PROBLEM

--------------- ------------ ------------------ --------------------

285 MAY 28, 2015 443694000 Unresolved

400 MAY 28, 2015 88805009 Chronic Systolic...

730 MAY 28, 2015 1201005 Hypertension

851 MAY 28, 2015 267434003 Hyperlipidemia

1075 MAY 28, 2015 63480004 Bronchitis

1077 MAY 28, 2015 68449006 Arthritis, Rhemat...

1079 MAY 28, 2015 25702006 Alcohol Dependence

1080 MAY 28, 2015 193031009

1177 JUN 10, 2015 230572002 Unresolved

### SNOMED in Diagnosis Field Cleanup Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report goes back to the last Problem file cleanup runtime and identifies any corrections where SNOMED codes in the Diagnosis field were corrected to ICD codes.

Steps to use option:

1.  Select Problem List Management Menu Option:
2.  Select (10) SNOMED in Diagnosis Field Cleanup Report.

Sample Cleanup Report:

Problem File Cleanup Report

\*\*NOTE\*\*: This report is retroactive as of the last Problem file cleanup

runtime:Jul 09, 2015@13:00:32. This report will expire and be purged from

the system in 30 days. If the Generate SNOMED in Diagnosis Field

Err/Cleanup Rpt \[GMPL GENERATE DIAG RPTS\] menu option is run prior to the

30 days, then this report will expire on the date/time the option is run.

Whichever comes first.

A cleanup of the Problem file has been performed and the following 9

record entries have been corrected. This report contains 7 columns.

Please scroll to the right for more information.

These entries no longer contain a SNOMED CT concept code in the Diagnosis

field \#.01. The correct primary ICD diagnosis and secondary diagnosis

code(s) is now stored in the appropriate fields. The corresponding SNOMED

CT concept and designation codes have also been correctly filed in their

respective fields. The provider narrative and problem fields were also

updated accordingly as well.

DATE LAST PRIMARY SNOMED C

IEN MODIFIED DIAGNOSIS SECONDARY DIAGNOSIS CONCEPT

--------------- ------------ --------- ------------------- -------

285 MAY 28, 2015 250.02 44369...

400 MAY 28, 2015 428.0 88805...

730 MAY 28, 2015 401.1 12010...

851 MAY 28, 2015 272.2 26743...

1075 MAY 28, 2015 491.9 63480...

1077 MAY 28, 2015 716.60 68449...

1079 MAY 28, 2015 305.00 25702...

1080 MAY 28, 2015 339.00 19303...

1177 JUN 10, 2015 250.60 355.9 23057...

### Generate SNOMED in Diagnosis Field Err/Cleanup Rpt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows a user to rerun the file scan and cleanup tasks for any potential new errors.

Steps to use option:

1.  Select Problem List Management Menu Option:
2.  Select (11) Generate SNOMED in Diagnosis Field Err/Cleanup Rpt.

Problem File SNOMED Error Scan and Cleanup queued.

The task number is 158595.

Personal PreferencesProblem List User Preferences Menu \[GMPL USER PREFS MENU\]

1 Problem List Preferred View \[GMPL USER VIEW\]

2 Problem Look‑up Defaults ... \[GMPL USER LOOK‑UP DEFAULTS\]

3 Preferred Problem Selection List \[GMPL USER LIST\]

Problem List Preferred View;\[GMPL USER VIEW\]

This option on the User Preferences Menu lets you limit your Problem List display to one or more specific hospital services or clinics. It also displays the clinics or services you have already selected. If you type +, you will see more clinics or services to choose from.

Steps to use option:1. Go into the Problem List User Preferences Menu.

2. Select Problem List Preferred View.
3. Type Yes if you wish to change your preferred view.
4. At the “Select VIEW” prompt, type Inpatient or Outpatient.
5. Type A or S for All problems or Selected clinics.

Select Problem List User Preferences Menu Option: 1 Problem List Preferred View

CURRENT VIEW: Inpatient, all services included

Do you want to change your preferred view? NO// y YES

Select VIEW: INPATIENT// OUTPATIENT

Include (A)ll problems or only those from (S)elected clinics? ALL// SELECTED

Retrieving list of clinics........

<u>PROBLEM LIST PREFERRED VIEW Apr 29, 2002 07:46:26 Page:1 of 2</u>

PLPROVIDER,ONE 0 Clinics

CLINICS

<u>Clinic Included in View</u>

1 CARDIOLOGY

2 AUDIOLOGY

3 ENT

+ + More Clinics ?? More actions

AD Add Items to View DV Delete Preferred View \* Exit

RM Remove Items from View SV Save Preferred View & Exit

VE Select New View of Problems Q Quit w/o Saving Changes

Select Action: Next Screen// ad

Select Item(s): 2 Audiology

6. After the screen containing clinics for your preferred view is displayed, type AD or Add Item(s) to View if you wish to add more clinics or services.
7. Type the number(s) of the clinics or services you wish to add to your preferred view.

Problem Look-up Defaults\[GMPL USER LOOK-UP DEFAULTS\]

This option lets you define your own default screens for use when looking up a problem in the Lexicon Utility. The purpose of this option is to speed up the look-up and selection process by only looking for and displaying terms relevant to your practice.

Specific kinds of terms may be included or excluded from the search, if defined here.

Steps to use option:1. Go into the Problem List User Preferences Menu.

2. Type 2 for Problem Look-up Defaults.
3. Type the number of the kind of look-up default you wish.

Select Problem List User Preferences Menu Option: 2 Problem Look-up Defaults

1 Filter

\*\*\> Out of order: This option has been disabled due to the Problem List SNOMED CT implementation.

2 Display

\*\*\> Out of order: This option has been disabled due to the Problem List SNOMED CT implementation.

3 Vocabulary

\*\*\> Out of order: This option has been disabled due to the Problem List SNOMED CT implementation.

4 Shortcuts

5 List Current Defaults

4. Type the name(s) or number(s) of the filter option you wish to limit your Problem List to.

> Preferred Problem Selection ;\[GMPL USER LIST\]Note: This option is no longer used with patch GMPL\*2.0\*49. List are designated using a CPRS parameter (ORQQPL SELECTION LIST) and set using another Problem List option.

Viewing the Problems Tab

When you click on the Problems Tab, a screen similar to the following opens up:

![](problem-list-user-manual-version-2-gmpl-2-60/012.png)

![](problem-list-user-manual-version-2-gmpl-2-60/013.png)

View Options

You have a choice of how to display a patient’s problems: active problems only, inactive problems only, both active and inactive problems, and problems for a selected service or provider by customizing your view of the problem list.

You can change the view, add, deactivate, remove, verify, or annotate problems.

### Changing Views on the Problem List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changing the view of the Problem List allows you to focus the list of problems on one of several criteria. Focusing the list will speed up the selection process.

Problems List views:

- Active
- Inactive
- Active and Inactive
- Removed

To change the view, click on any of the options listed in the View options field or click on View on the menu.

![](problem-list-user-manual-version-2-gmpl-2-60/014.png)

Filters

Select the Filters option on the menu to further focus the list of problems you wish to have displayed. From the Filters dialog, you may choose to display problems by any combination of Status, Source Clinic (which is listed when you select Outpatient), Source Service (which is listed when you select Inpatient), and Provider.

![](problem-list-user-manual-version-2-gmpl-2-60/015.png)

# Package Operation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use Problem List

Operation of Problem List will vary from site to site, depending on the data entry method your hospital has chosen. Typical scenarios that might be used are described on the next two pages.

The actions for both clinician entry and clerk entry are essentially identical. In the descriptions on the following pages, differences between the two are noted.

The basic operation of the Problem List program is very simple:

1. Pick a patient.
2. Enter the Provider Name, if you’re a clerk.
3. The patient’s problem list is displayed.
4. Perform one of several possible actions, such as add a new problem, edit a problem, print a problem list, as described on the following pages.

## Potential Scenarios for Problem List Entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient ScenariosA. *Direct data entry into the Problem List:* A *clinician* (nurse, Physician Assistant, physician) compiles a list of patient problems relevant to the visit by direct data entry into either the CPRS GUI, the CPRS List Manager, or the Problem List package.

B. *Manual entry into encounter form:* A patient checks in, is seen by a clinician, and an encounter form (usually an electronically generated form from the Integrated Billing software) is filled out by the provider. Problems addressed in the visit are captured. A purpose of visit may be recorded. The encounter form may be generic or it may be patient-specific, with ID, demographics, and Service Connection (SC) information. It may be customized to the clinic as well, with clinic, provider, and clinic-specific procedures and diagnoses. Data entry is done by a provider, who may check items or fill in free text. The provider must note which services delivered were for a service-connected condition. The provider may, in some cases, use the same form to create a progress note.

A clerk transcribes the problem and procedure data from the form into VistA. Free-text problem entries will be transferred to the computer to the best of the clerk’s ability. Unclear entries will be returned to the provider for clarification. A new encounter form is electronically generated from this data, to be used by the provider the next time he/she enters data for the patient.

C. Same as above, except that after the encounter form is completed by the provider, it is scanned (through a scanning device), and entered electronically into DHCP.

Inpatient ScenariosA. A *clinician* (nurse, Physician Assistant, physician) compiles the list of patient problems relevant to the hospitalization. Presently, this is mainly done by direct data entry. The potential applications of Problem List data during inpatient stays include Treatment Plans, creation of headers for Progress Notes, preparation of a prompt sheet for a discharge document, and worksheets for rounds. Problem data may benefit the Utilization Review specialist who must submit data for certification of ongoing inpatient treatment.

Another scenario would be using the application to create a problem list (VAF 10-1415) when one is required, as for a new patient with a new chart.

B. A *clerk* transcribes patient information entered by a provider on an encounter form designed to capture problem data for an inpatient. The clerk enters data from checkbox entries and free-text entries. The clerk then prints a turnaround form to allow the provider to correct errors. Clerks will record corrections and set a verification flag. (Providers may verify data online, as well.)

## Problem List in CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem List is available as a tab on the CPRS GUI Cover Sheet. The Cover Sheet is the first screen you see after opening a patient record unless your site defines another tab as the initial tab. It presents a quick overview of a patient’s condition and history. It shows active problems, allergies and postings, active medications, clinical reminders, lab results, vitals, and a list of appointments or visits.

See [Appendix A](#appendix-a-lexiconntrt-tips-for-the-problems-tab) for information about using the new Lexicon Search capability.

![](problem-list-user-manual-version-2-gmpl-2-60/016.png)

You can quickly review the active problems (asterisks identify acute problems, and dollar signs identify unverified problems).

Scroll bars beside a box mean that more information is available if you scroll up or down.

Single-click on one of the five menus: File, Edit, View, Tools, or Help, to see choices of things you can do or other options available to you.

File Menu

The File menu contains three commands that you will use often:

- Select New Patient brings up the Patient Selection dialog.
- Update/Provider/Location brings up a dialog that enables you to change the clinician or location of an encounter.
- Review/Sign Changes enables you to view the orders you have placed that require an electronic signature, select the orders you want to sign at this time, and enter your electronic signature (if you are authorized to sign them).

Click on any Problem List item on the cover sheet to get more detailed information.

Example

![](problem-list-user-manual-version-2-gmpl-2-60/017.png)  
Adding a Problem Using a Problem Selection List

If a Problem Selection List is assigned to a user, selected clinic, division, or system under which the user is signed into, those corresponding problem selection list categories and problems will be displayed for user selection.

*Steps to add a new problem to a patient’s problem list:*

1.  Select the Problems tab.
2.  Select the New Problem button. The Problem Selection List categories and problems appear.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/018.png)</p></th>
<th>If you have not defined the provider or location, you will be prompted for this encounter information.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="VA_National_Prob_select_categ_problems" class="anchor"></span>![](problem-list-user-manual-version-2-gmpl-2-60/019.png)

3.  Select a problem associated with a particular Problem category/specialty.
4.  Enter information about the problem, such as whether it is acute or chronic, treatment factors (Service Connected, Radiation, Agent Orange, or Environmental Contaminants), the Date of Onset, the provider, and the clinic.
5.  Add a comment if you wish by clicking Add Comment and entering the comment in the dialog that appears. Then click OK.
6.  Click OK again.

Adding a Problem Using the Lexicon Search

You add a new problem from the Problems tab. From this tab, you can add, remove, change, verify, and annotate a problem.

See [Appendix A](#appendix-a-lexiconntrt-tips-for-the-problems-tab) for information about using the new Lexicon Search capability.

*Steps to add a new problem to a patient’s problem list:*

1.  Select the Problems tab.
2.  Select New Problem. The Problem List Lexicon Search box appears (only if there are no Problem Selection Lists currently assigned).

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/020.png)</p></th>
<th>If you have not defined the provider or location, you will be prompted for this encounter information.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="lexiconsearch" class="anchor"></span> ![](problem-list-user-manual-version-2-gmpl-2-60/021.png)

3.  Select a problem from the list or search the lexicon for the problem by clicking Extend Search on the lower left side of the Problems tab. When the list appears, locate and click on the problem.
4.  Enter information about the problem, such as whether it is acute or chronic, treatment factors (Service Connected, Radiation, Agent Orange, or Environmental Contaminants), the Date of Onset, the provider, and the clinic.
5.  Add a comment if you wish by clicking Add Comment and entering the comment in the dialog that appears. Then click OK.
6.  Click OK again.
7.  If you select Extend Search, a screen such as the following appears. You can select one of the listed terms or click on the Freetext Problem button.

> ![](problem-list-user-manual-version-2-gmpl-2-60/022.png)

If you click on the Freetext Problem button, you have a choice of Requesting a New Term.

> ![](problem-list-user-manual-version-2-gmpl-2-60/023.png)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/024.png)</p></th>
<th>See <a href="#appendix-a-lexiconntrt-tips-for-the-problems-tab">Appendix A</a> for more details about requesting new terms.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Annotating a Problem

To annotate a problem, use these steps:

1\. Click on the problem in the problem list.

2\. Select Action \| Annotate... or right-click the problem and select Annotate... from the pop-up menu.

3\. Enter your annotation in the dialog that appears (up to 200 characters).

4\. Click OK.

Changing a Problem

To change a problem on a patient’s problem list, use these steps:

1\. Click the Problems tab.

2\. Click on the problem in the list box that you want to change.

3\. Select Action \| Change… or right-click the problem and select Change… from the pop-up menu.

4\. Enter the desired changes.

5\. Add or remove a comment if desired.

> **NOTE:** A comment can be as many as 200 characters (including spaces) in length.

6\. Click OK.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/025.png)</p></th>
<th>When you view the details of a problem, you will see who changed the problem and when.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](problem-list-user-manual-version-2-gmpl-2-60/026.png)

Deactivating a Problem

To deactivate a problem on a patient’s problem list, use the following steps:

1\. Click on a problem in the list box.

2\. Select Action \| Inactivate or right-click the problem and select Inactivate from the pop-up menu.

Removing a Problem

A problem is not removed from the database because things “pointing” to it might be broken if it is removed. A field in the problem record can be “flagged” with an “H” and the problem will be HIDDEN. Any software that runs on the database must look at the field to see if it is hidden or not. The hidden record will not appear on any reports or lists and will appear to the user that it has been removed. Actually it is only removed from sight.

To remove a problem from a patient’s problem list, use these steps:

1\. Click on the problem.

2\. Select Action \| Remove or right-click the problem and click Remove on the pop up menu.

Verifying a Problem

To verify a problem on a patient’s problem list, use these steps:

1\. Click on the problem in the problem list.

2\. Select Action \| Verify or right-click the problem and click Verify on the pop up menu.

## Customizing the Problem List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Problems tab, you can sort the problem list by problem status or use the view filtering to get a more specific list of problems. You can sort the list to see the following:

- Active Problems
- Inactive Problems
- Both Active/Inactive Problems
- Removed Problems

## Problem List in CPRS List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using Problem List through the List Manager version of CPRS is very similar to using it directly in the Problem List application. The advantage of using it in CPRS is that you also have access to the complete patient chart, which includes Orders, Notes, Reports, Summaries, and Meds.

When you sign in to the List Manager version of CPRS, the first screen you see is the Patient Selection screen. If you have a default list defined, the names on the list will appear here for you to select from.

Steps to use Options:1. Select patient name.

<u>Patient Selection Apr 12, 2002@11:37:30 Page: 1 of 1</u>

Current patient: \*\* No patient selected \*\*

<u>Patient Name ID DOB Room-Bed</u>

No patients found

Enter the number of the patient chart to be opened \>\>\>

\+ Next Screen CV Change View ... FD Find Patient

\- Previous Screen SV (Save as Default List)Q Close

Select Patient: Change View//CPRSPATIENT,EIGHT \*SENSITIVE

\* \*SENSITIVE\* YES SC VETERAN C

\*\*\*WARNING\*\*\*

\*\*\*RESTRICTED RECORD\*\*\*

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

\* This record is protected by the Privacy Act of 1974. If you elect \*

\* to proceed, you will be required to prove you have a need to know. \*

\* Accessing this patient is tracked, and your station Security Officer \*

\* will contact you for your justification. \*

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Do you want to continue processing this patient record? No// Y (Yes)

Searching the patient's chart ...

NW Enter New Allergy/ADR CV (Change View ...) SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Next Screen// CC Chart Contents ...

2. Select CC, Chart Contents, to see the “tabs” or components of the patient chart.

<u>Cover Sheet Jun 29, 2012@10:10:28 Page: 1 of 2</u>

CPRSPATIENT,EIGHT 666-06-1008 ICU/CCU 4/15/53(59)

Attend: CPRSPROVIDER,O PrimCare: CPRSPROV,F PCTeam: GREEN

<u>Item Entered</u>

<u>Allergies/Adverse Reactions</u> \|

No assessment available \|

\|

<u>Patient Postings</u> \|

\<None\> \|

\|

<u>Recent Vitals</u> \|

No data available \|

\|

<u>Recent Immunizations</u> \|

\|

<u>Eligibility</u> \|

Not Service Connected \|

+ Enter the numbers of the items you wish to act on.

Cover Sheet Orders Imaging Reports

Problems Meds Consults

Notes Labs D/C Summaries

Select chart component: P Problems

Searching the patient's chart ...

3. Select Problems for the Problem List.<u>Active Problems Jun 29, 2012@10:10:42 Page: 1 of 2</u>

CPRSPATIENT,EIGHT 666-06-1008 ICU/CCU 4/15/53(59)

Attend: CPRSPROVIDER,O PrimCare: CPRSPROV,F PCTeam: GREEN

<u>Problem Onset Updated Status</u>

1 Abdominal pain (SCT 21522001) \| 04/23/08 active

2 Abdominal pain (SCT 21522001) \| 04/23/08 active

testing problem update from encounter \|

form - same session as \|

3 Acute conjunctivitis (SCT 53726008) \| 04/23/08 active

4 Anger reaction (SCT 192085004) \| 04/23/08 active

5 Winter itch (SCT 201025002) \| 04/23/08 active

6 Smith-Lemli-Opitz syndrome (SCT \| 04/23/08 active

43929004\) \|

7 Edema (SCT 267038008) \| 04/23/08 active

8 Hypertensive disorder (SCT 38341003) \| 00/00/94 04/18/08 active

entered on problems tab. \|

9 Gastresophageal reflux disease (SCT \| 04/18/08 active

+ Enter the numbers of the items you wish to act on.

Select: Next Screen// 1

Inactivate Add Comment Detailed Display

Remove Edit Verify

Select Action: E Edit

Patient Location: Mental Health

Retrieving current data for problem

<u>PROBLEM LIST Jun 29, 2012@10:28:15 Page: 1 of 1</u>

<u>CPRSPATIENT,EIGHT (C1008) Last Updated: Apr 23, 2008</u>

1 Problem: Abdominal pain

2 Onset: unknown 6 SC Condition: unknown

3 Status: ACTIVE 7 Exposure: \<None\>

4 Provider: CPRSPROVIDER,ONE

5 Service:

<u>Comments</u>:

Enter the number of the item(s) you wish to change

CM Additional Comments RM Remove Problem from List

Q Quit w/o Saving Changes SC Save Changes and Exit

Select Item(s): Quit// 5 5

SERVICE: MEDICINE

<u>PROBLEM LIST Jun 29, 2012@10:38:16 Page: 1 of</u> 1

CPRSPATIENT,EIGHT (C1008) Last Updated: Apr 23, 2008

1 Problem: Abdominal pain

2 Onset: unknown 6 SC Condition: unknown

3 Status: ACTIVE 7 Exposure: \<None\>

4 Provider: CPRSPROVIDER,ONE

5 Service: MEDICINE

Comments:

Enter the number of the item(s) you wish to change

CM Additional Comments RM Remove Problem from List

Q Quit w/o Saving Changes SC Save Changes and Exit

Select Item(s): Save Changes and Exit// \<Enter\>

Save Changes and Exit

Saving ... done.

### Potential Scenarios for Problem List Entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient ScenariosA. *Direct data entry into the Problem List:* A *clinician* (nurse, Physician Assistant, physician) compiles a list of patient problems relevant to the visit by direct data entry into either the CPRS GUI, the CPRS List Manager, or the Problem List package.

B. *Manual entry into encounter form:* A patient checks in, is seen by a clinician, and an encounter form (usually an electronically generated form from the Integrated Billing software) is filled out by the provider. Problems addressed in the visit are captured. A purpose of visit may be recorded. The encounter form may be generic or it may be patient-specific, with ID, demographics, and Service Connection (SC) information. It may be customized to the clinic as well, with clinic, provider, and clinic-specific procedures and diagnoses. Data entry is done by a provider, who may check items or fill in free text. The provider must note which services delivered were for a service-connected condition. The provider may, in some cases, use the same form to create a progress note.

A clerk transcribes the problem and procedure data from the form into VistA. Free-text problem entries will be transferred to the computer to the best of the clerk’s ability. Unclear entries will be returned to the provider for clarification. A new encounter form is electronically generated from this data, to be used by the provider the next time he/she enters data for the patient.

C. Same as above, except that after the encounter form is completed by the provider, it is scanned (through a scanning device), and entered electronically into DHCP.

Inpatient ScenariosA. A *clinician* (nurse, Physician Assistant, physician) compiles the list of patient problems relevant to the hospitalization. Presently, this is mainly done by direct data entry. The potential applications of Problem List data during inpatient stays include Treatment Plans, creation of headers for Progress Notes, preparation of a prompt sheet for a discharge document, and worksheets for rounds. Problem data may benefit the Utilization Review specialist who must submit data for certification of ongoing inpatient treatment.

Another scenario would be using the application to create a problem list (VAF 10-1415) when one is required, as for a new patient with a new chart.

B. A *clerk* transcribes patient information entered by a provider on an encounter form designed to capture problem data for an inpatient. The clerk enters data from checkbox entries and free-text entries. The clerk then prints a turnaround form to allow the provider to correct errors. Clerks will record corrections and set a verification flag. (Providers may verify data online, as well.)

## Using Problem List through the Problem List Program in List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patient Problem List Option \[GMPL CLINICAL USER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets clinicians use the Problem List program to review a patient’s problems, add a new problem, edit an existing problem, inactivate a problem, and a number of other actions, as described in the following pages.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/027.png)</p></th>
<th>Problems on the list will appear in chronological order unless you choose reverse chronological order in the Edit PL Site Parameters option (on the Problem List Mgt Menu).</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Option: Patient Problem List

Select PATIENT NAME: PLPATIENT,ONE 03-04-14 666001111 SC VETERAN

Searching for the patient's problem list...

1. Select the Patient Problem List option from your clinical menu. (Each site will decide what menu to place this option on.)
2. Type the name of the patient whose problem you wish to enter.

*The patient’s problem list is then displayed, as shown in the example below:*

<u>PROBLEM LIST Jun 29, 2017@09:11:27 Page: 1 of 2</u>

CPRSPATIENT,FIFTEEN (C0010) 6 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 6/1/17 6/1/17 45 PATTERN

2 Hypertension (SCT 38341003), Onset 4/10/17

4/7/17

3 Hyperlipidemia (SCT 55822004), Onset 4/10/17

4/7/17

4 Acute myocardial infarction (SCT 3/17/17 GENERAL MEDICINE

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 3/9/17 GENERAL MEDICINE

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

Q Quit

Select Action: Next Screen//

REMEMBER: You can respond to many prompts by typing the first few letters of a name, option, or action. Some option names have “mnemonics” — an abbreviation that you can enter rather than the entire option name.

### Problem List Data Entry \[GMPL DATA ENTRY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets clerks enter and maintain Problem Lists. Clerks can enter new problems, edit problems, remove, or print a problem. The clerks in outpatient clinics will probably be working with Encounter Forms (or similar data entry forms) to enter and edit problems that clinicians have entered onto the forms.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/028.png)</p></th>
<th>When problems are entered into the problem list with no ICD code attached, the system automatically assigns the number <strong>R69</strong>.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Select Option: Problem List Data Entry

> Select PATIENT NAME: CPRSPATIENT,EIGHT 06-18-62 666221008

> Searching for the patient's active problem list...

1. Select the Problem List Data Entry option from your clinical menu. (Each site will decide what menu to place this option on.)
2. Type the name of the patient whose problem you wish to enter.
3. Type the name of the Provider for this problem list.

<u>PROBLEM LIST Jun 29, 2012@09:37:10 Page: 1 of 3</u>

CPRSPATIENT,EIGHT (C1008) 14 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Abdominal pain (SCT 21522001) 4/23/08 20 MINUTE

2 Abdominal pain (SCT 21522001) 4/23/08 20 MINUTE

3 Acute conjunctivitis (SCT 53726008) 4/23/08 20 MINUTE

4 Anger reaction (SCT 192085004) 4/23/08 20 MINUTE

5 Winter itch (SCT 201025002) 4/23/08 20 MINUTE

6 Smith-Lemli-Opitz syndrome (SCT 4/23/08 20 MINUTE

43929004\)

7 Edema (SCT 267038008) 4/23/08 20 MINUTE

8 Hypertensive disorder (SCT 38341003), 4/18/08 20 MINUTE

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen//

4. Select the Action you wish to take (add, remove, edit, etc.).

### How to Use Problem List User List Manager Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Problem List and Problem List Data Entry options in List Manager present screens that contain patient information and one or more problems for that patient (if they have been previously entered). At the bottom of this screen are a number of actions you can perform at this time. This section describes the following user actions:

Add New Problems

Comment on a Problem

Detailed Display

Edit a Problem

Inactivate Problems

Print Problem List

Remove Problems

Select New Patient

Select View of List

Show All Problems

Verify Problems

More Actions

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/029.png)</p></th>
<th>Other actions are available on management screens, but they aren’t described individually in this manual. See the Package Management section earlier in this manual for further information about management actions.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ACTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add New Problems

> Follow the steps listed below the sample screen to create a problem list for a patient or add a new problem to an already existing problem list.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/030.png)</p></th>
<th><blockquote>
<p>New problems that you add will appear at the bottom of the list unless you change the display to reverse chronological order through the option Edit PL Site Parameters. They will then appear at the top of the list.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/031.png)</p></td>
<td><blockquote>
<p>If there is more than one match to the problem you enter, a list is displayed for you to select from.</p>
</blockquote></td>
</tr>
</tbody>
</table>

These lists are displayed in groups of five. If there are more than five matches and you want to scroll back to a previous batch of five, type ^(#) – e.g., ^1 – and the screen will re-display the first group.

*Example 1*

Select PATIENT NAME: PLPATIENT,ONE 03-04-14 666001111 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 12 active problems

ACTIVE CLINIC PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>AD</u> Add New Problem

Clinic: <u>Podiatry</u>

PROBLEM: <u>Diabetes Mellitus</u>

363 matches found

1 Diabetes mellitus (SNOMED CT 73211009)

2 FH: Diabetes mellitus (SNOMED CT 160303001)

3 H/O: diabetes mellitus (SNOMED CT 161445009)

4 Type 2 diabetes mellitus (SNOMED CT 44054006)

5 Type 1 diabetes mellitus (SNOMED CT 46635009)

Type "^" to STOP or Select 1-5: <u>1</u>

1. Type the name of the patient to add a problem for.
2. Type AD at the “Select Action” prompt.
3. If the patient is an outpatient, you will be prompted for a clinic.
4. Enter the name of the problem you wish to add to the patient’s problem list. You will be re-prompted for “PROBLEM” until you press return.

The patient’s problem should be entered in clinical terms. You can use one full word or two to three partial words; for example, DIABETES, DIAB MELL, or DIAB MELL INSUL.

- You can enter as many comments to a problem (up to 200 characters each) as you wish.
- The date of onset should be the date the problem was first observed, as precisely as known.
- If you have no idea of the date, press return to bypass the prompt.

> *Example 1 (cont’d)*

COMMENT (\<200 char): <u>Check foot sore</u>

DATE OF ONSET: <u>T-3</u> (MAY 19, 2004)

STATUS: ACTIVE// \<Enter\>

(A)cute or (C)hronic: <u>Chronic</u>

\>\>\> Currently known service-connection data for CUMQUAT,EARNEST.:

SC %: 50%

Disabilities: NONE STATED

Is this problem related to a service-connected condition? <u>Y</u> YES

Is this problem related to AGENT ORANGE EXPOSURE? <u>N</u> NO

Is this problem related to RADIATION EXPOSURE? <u>Y</u>

Problem: Diabetes Mellitus

\<1 comment appended\>

Onset: 5/17/04 SC Condition: YES

Status: ACTIVE/CHRONIC Exposure: RADIATION

Provider: PLPROVIDER,ONE

Clinic : Podiatry

Recorded : 5/22/04 by PLPROVIDER,ONE

(S)ave this data, (E)dit it, or (Q)uit w/o saving? SAVE// \<Enter\>

Saving......done

Please enter another problem, or press \<return\> to exit. \<Enter\>*(Problem List screen is re-displayed)*5. Enter a comment (less than 200 characters), the date of onset, status of problem (active or inactive, acute or chronic), and service-connection. All responses are optional. If you don’t respond to Status, it will default to Active.

6. Add more problems or edit problems, if you wish.
7. When you exit this patient’s list, you are prompted to print a new problem list. Press return if you want a new list printed. Otherwise, type No. *See the Print Problem List action description in this manual for examples of printed problem lists.*

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/032.png)</p></th>
<th><blockquote>
<p>You must already have a selection list created for this example.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This example illustrates use of a General Medicine List to choose problems from.

> (See the Package Management section for descriptions of creating customized selection lists or customizing your view of problems.)

*Example 2: Adding a problem from a selection list.*

Select PATIENT NAME: PLPATIENT,ONE 03-04-14 666001111 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 12 active problems

ACTIVE CLINIC PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>AD</u> Add New Problems

Clinic: <u>General Medicine</u>1. Type the name of the patient whose problem you wish to add.

2. Type AD at the “Select Action” prompt.
3. Type the name of the clinic you have a selection list defined for.

> *Example 2 (cont’d) Using a pre-defined selection list*

<u>PROBLEM LIST FEB 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 12 active problems

GENERAL MEDICINE

1 Hypothyroidism (SCT 40930008) (R69)

2 Iron deficiency anemia (SCT 87522002) (R69)

3 Macrocytic Anemia (SCT 83414005) (R69)

4 Chronic Anemia (SCT 191268006) (R69)

5 Diabetes Mellitus (SCT 73211009) (R69)

Enter the number of the item(s) you wish to view

AD Add a Problem not on a menu Q Quit to Problem List

Select Item: Next Screen// <u>2</u>

\>\>\> Adding Problem \#2 ‘Iron deficiency anemia’...

COMMENT (\<200 char): <u>Seems pretty rundown</u>

ANOTHER COMMENT: \<Enter\>

DATE OF ONSET: <u>T-30</u> (January 30,2017)

STATUS: ACTIVE// \<Enter\>

(A)cute or (C)hronic: <u>??</u>

You may further refine the status of this problem by designating it as ACUTE or CHRONIC; problems marked as ACUTE will be flagged on the list display with a '\*'.

(A)cute or (C)hronic: <u>A</u>

\>\>\> Currently known service-connection data for PLPATIENT,ONE:

SC %: 50%

Disabilities: NONE STATED

Is this problem related to a service-connected condition? <u>Y</u> YES

Is this problem related to AGENT ORANGE EXPOSURE? <u>N</u> NO

Is this problem related to RADIATION EXPOSURE? <u>Y</u>

Problem: Iron deficiency anemia

\<1 Comment appended\>

Onset: 1/30/17 SC Condition: YES

Status: ACTIVE/ACUTE Exposure: RADIATION

Provider: PLPROVIDER,ONE

Clinic: GENERAL MEDICINE

Recorded: 2/10 by PLPROVIDER,ONE

(S)ave this data, (E)dit it, or (Q)uit w/o saving? SAVE// \<Enter\>4. Select a problem from the list that is displayed or add a problem not on the list.

5. Enter a comment (less than 200 characters), the date of onset, status of problem (active or inactive), and service-connection.

> Add New Problems, cont’d

- If you have a pre-defined selection list, but the problem you wish to add isn’t on that list, you may choose a problem from the Lexicon Utility.
- If an asterisk is by the term, you can type in ?(#) and get a brief description of the term.
- The date of onset should be the date the problem was first observed, but you can bypass the prompt if unknown.
- All responses are optional. If you don’t respond to Status, it will default to Active.

Example 3: *Adding a problem not on a menu, when you have a selection list defined*

<u>PROBLEM LIST Feb 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 12 active problems

<u>GENERAL MEDICINE</u>

1 Hypothyroidism (SCT 40930008) (R69)

2 Iron deficiency anemia (SCT 87522002) (R69)

3 Macrocytic Anemia (SCT 83414005) (R69)

4 Chronic Anemia (SCT 191268006) (R69)

5 Diabetes Mellitus (SCT 73211009) (R69)

Enter the number of the item(s) you wish to view

AD Add a Problem not on a menu Q Quit to Problem List

Select Category: Quit to Problem List// <u>AD</u>

Add Problem not on a menu

\>\>\> Adding a problem not on the menu ...

PROBLEM: <u>Anemia</u>

391 matches found

1 Anemia (SNOMED CT 271737000)

2 FH: Anemia (SNOMED CT 266888008)

3 H/O: anemia (SNOMED CT 275538002)

4 O/E - anemia (SNOMED CT 164139008)

5 Fetal anemia (SNOMED CT 462166006)

Type "^" to STOP or Select 1-5: 1

COMMENT (\<200 char): <u>Aggravated by flu</u>

ANOTHER COMMENT: \<Enter\>

DATE OF ONSET: <u>T-3</u> (FEB 07, 2017)

STATUS: ACTIVE// \<Enter\>

(A)cute or (C)hronic: <u>ACUTE</u>

\>\>\> Currently known service-connection data for CUMQUAT,EARNEST.:

SC Percent: 50%

Disabilities: NONE STATED

Is this problem related to a service-connected condition? <u>Y</u> YES

Is this problem related to AGENT ORANGE EXPOSURE? <u>N</u> NO

Is this problem related to RADIATION EXPOSURE? <u>Y</u>

Problem: Anemia

\<1 Comment appended\>

Onset: 2/07/17 SC Condition: YES

Status: ACTIVE/ACUTE Exposure: RADIATION

Provider: PLPROVIDER,ONE

Clinic: GENERAL MEDICINE

Recorded: 2/10 by PLCLERK,ONE

(S)ave this data, (E)dit it, or (Q)uit w/o saving? SAVE// \<Enter\>1. Select AD for Add a Problem not on the menu.

2. Type the name of the problem.
3. Enter a comment(s) (less than 200 characters), the date of onset, status of problem (active or inactive), and service-connection.

> Add New Problems – Clerk Entry

> Clerks can enter new problems to a patient’s problem list, from an encounter form or other types of documentation.

*Example 4: Clerk Entry*

Select PATIENT NAME:<u>PLPATIENT,ONE</u> 03-04-14 666001111 NSC VETERAN

Provider: <u>PLPROVIDER,ONE</u>

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 16, 2017 14:19:45 Page: 1 of 2</u>

<u>PLPATIENT,ONE</u> (P1111) 8 of 26 active problems

<u>ACTIVE PROBLEMS</u>

<u>Problem ICD SC Exposure Resolved</u>

1 Multiple Sclerosis (SCT R69 YES Agent Orange

24700007), Onset 3/5/17

2 Cholecystitis (SCT 76581006), R69 YES Radiation

Onset 3/7/17

3 Diabetes Mellitus (SCT R69 NO

73211009), Onset 4/1/17

4 Hemotysis (SCT 66857006) R69 NO

5 Fracture of multiple ribs (SCT R69 NO

1261007\)

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems SP Select New Patient

RM Remove Problems CM Comment on a Problem PP Print Problem List

ED Edit a Problem VW Show All Problems Q Quit

Select Action: Next Screen// <u>AD</u>

Clinic: <u>Cardiology</u>

PROBLEM: <u>Anemia</u>1. Type the name of the patient whose problem you wish to add.

2. Enter the name of the provider.
3. Type AD at the “Select Action” prompt.
4. Enter the name of the clinic the patient is in, if known.
5. Enter the name of the patient’s problem.

> Add New Problems*Clerk Entry (cont’d)*

You may further refine the status of this problem by designating it as acute or chronic; problems marked as acute will be flagged on the list display with an asterisk.

COMMENT (\<200 char): <u>Aggravated by flu</u>

DATE OF ONSET: <u>T-30</u> (JAN 19, 2017)

STATUS: ACTIVE// \<Enter\>

(A)cute or (C)hronic: <u>ACUTE</u>

\>\>\>Currently known service-connection data for PLPATIENT,ONE:

SC Percent:

Disabilities: NONE STATED

Is this problem related to a service-connected condition? <u>No</u>

Is this problem related to Agent Orange exposure? <u>No</u>

Is this problem related to RADIATION exposure? <u>No</u>

Is this problem related to ENVIRONMENTAL CONTAMINANTS exposure? <u>No</u>

------------------------------------------------------------------

Problem: ANEMIA

Onset: 1/19/17 SC Condition: NO

Status: ACTIVE/ACUTE Exposure: NONE

Provider: PLPROVIDER,ONE

Clinic: CARDIOLOGY

Recorded: 2/10 by PLCLERK,ONE

-------------------------------------------------------------------

(S)ave this data, (E)dit it, or (Q)uit w/o saving? SAVE// \<Enter\>

Saving ...DONE

\>\>\> Please enter another problem, or press \<return\> to exit.

PROBLEM: \<Enter\>7. Enter comments, date of onset, the status of the problem (active or inactive, acute or chronic), and service-connection information (if any).

*All of these responses are optional. If you don’t respond to Status, it will default to Active.*

> Comment on a Problem

> You can add a note or comments to your own or another clinician’s patient problem. Clerks can also enter comments provided to them by clinicians.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/033.png)</p></th>
<th><blockquote>
<p>1-12 problems are indicated, while only 5 problems are displayed above. The + means there are more problems. Type in + at the “Select Action” prompt o see the remainder.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You can enter up to <span id="all_comments_and_200_characters" class="anchor"></span>200 characters. All the associated comments will appear on the problem list display.

Select PATIENT NAME: <u>PLPATIENT,ONE</u> 03-04-14 666001111 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

## Select Action: Next Screen// <u>cm</u> Comment on a Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Select Problem (1-12): <u>4</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acute myocardial infarction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## COMMENT (\<200 char): <u>Low RBC mass</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Another Comment: \<Enter\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. Type the patient’s name.
2. Type CM for Comment on a Problem.
3. Type the number of the problem (shown in the left-hand column) you wish to annotate.
4. Type the comment (in free-text form —less than 200 characters).

You may enter several comments on separate lines. You will be prompted with:

Another Comment:

Type another comment or press return.

5. The following message will appear when you quit the problem list or change patients:

\>\>\> THIS PATIENT'S PROBLEM LIST HAS CHANGED!

Print a new problem list? YES//

Detailed Display

## The detailed display shows further information about the problem, such as date of onset, ICD code, service connection, author, provider narrative, and date entered. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/034.png)</p></th>
<th><blockquote>
<p>You can see a detailed display for more than one problem by entering two or more problem numbers separated by a comma, or entering a range of numbers separated by a hyphen.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The status can be active or inactive and acute or chronic.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/035.png)</p></th>
<th>You may need to scroll to the Next Screen to see all of the display.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<u>  
PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P1111) 13 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Diabetes Mellitus (SCT 73211009) 4/27/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>dt</u> Detailed Display

Select Problem(s) (1-13): <u>3</u>

Retrieving current data for problem \#3...

1. Type DT for Detailed Display at the “Select Action” prompt.
2. Type the number of the problem from the problem list screen that you wish to see a detailed display of.

<u>PROBLEM LIST Apr 07, 2017 08:13:38 Page: 1 of 2</u>

PLPATIENT,ONE (P1111) Last Updated: Mar 23, 2017@08:56

Problem: Diabetes Mellitus (SCT 73211009)

ICD-10-CM: R69. \[Illness, unspecified\]

Onset: 2/18/17 SC Condition: YES

Status: ACTIVE Exposure: RADIATION

Provider: PLPROVIDER,ONE

Clinic: GENERAL MEDICINE

Author: PLPROVIDER,ONE

Recorded: 02/18/17, by PLPROVIDER,ONE

Entered: 02/18/17, by PLPROVIDER,ONE

Comments:

+ + Next Screen - Prev Screen ?? More actions

NP Continue to Next Selected Problem Q Quit to Problem List

Select Action: NEXT SCREEN// \<Enter\>

<u>PROBLEM LIST Apr 07, 2017 08:13:38 Page: 2 of 2</u>

PLPATIENT,ONE (P1111) Last Updated: Mar 23, 2017@08:56

3/3/17: Mistakenly removed from list.

<u>History</u>

3/3/17: PROBLEM placed back on list by PLPROVIDER,ONE

+ + Next Screen - Prev Screen ?? More actions

P Continue to Next Selected Problem Q Quit to Problem List

Select Action: Quit to Problem List// \<Enter\>

> Edit a Problem

> You can edit/change the problem name, the date of onset, the Clinic, the SC status, etc., or add more comments to an existing problem.

> You can also change the status of the problem to acute so that critical problems will be displayed with an \*.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/036.png)</p></th>
<th><blockquote>
<p>When you are prompted to select a problem from all the problems on the list (e.g., Select Problem(s) (1-5)), you may select one item or more by using commas or a range of items separated by a hyphen.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select PATIENT NAME: <u>PLPATIENT,ONE</u> 03-04-14 123432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,ONE (P2432) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>ed</u>

Select Problem (1-12): <u>4</u>

Retrieving current data for problem \#4.....

1. Type the name of the patient.
2. Type ED for Edit a Problem.
3. Type the problem number that is listed in the left-hand column.

> Edit a Problem (cont’d)

You may further refine the status of this problem by designating it as acute or chronic; acute problems will be flagged with asterisks (\*).

<u>PROBLEM LIST Apr 07, 2017 08:22:53 Page: 1 of 1</u>

<u>PLPATIENT,ONE (P2432) Last Updated: Mar 31, 2017@11:07</u>

1 Problem: Acute myocardial infarction (SCT 57054005)

2 Onset 3/17/17 6 SC Condition: YES

3 Status: ACTIVE 7 Exposure: RADIATION

4 Provider: PLPROVIDER,THREE

5 Clinic: AMBULATORY CARE

<u>Comments</u>:

8 3/17/17 Comment \#1

Enter the number of the item(s) you wish to change

CM Additional Comments RM Remove Problem from List

Q Quit w/o Saving Changes SC Save Changes and Exit

Select Item(s): Quit// <u>1</u>

PROBLEM: Acute myocardial infarction// Myocardial Infarction

117 matches found

1 Myocardial infarction (SNOMED CT 22298006)

2 Old myocardial infarction (SNOMED CT 1755008)

3 FH: Myocardial infarction (SNOMED CT 266897007)

4 EKG: myocardial infarction (SNOMED CT 164865005)

5 Acute myocardial infarction (SNOMED CT 57054005)

Type "^" to STOP or Select 1-5:

Select Item(s): Save Changes and Exit// \<Enter\>4. Type the number of the item you wish to change.

For example, select \#1 if you want to change the problem name.

5. Enter the new value.

For example, type the new name of the problem. If several matches are available, choose one. If you simply want to delete an entry, type @. This does not delete the problem; it only removes it from the list.

6. If you choose Status to edit, you can enter active or inactive, acute or chronic. If you choose Acute, this problem will be displayed with an asterisk (\*) on the left. If the problem is Inactive, you will be prompted for the Date Resolved.
7. If you wish to completely remove this problem from the patient’s list, type RM.
8. Press the return key to save the changes and quit.

Inactivate Problems

When a problem is no longer active, you can inactivate it. It will then appear on an inactive problem list (or a combined active/inactive list) with the date the problem was resolved.

Select PATIENT NAME: <u>PLPATIENT,FOUR</u> 03-04-14 666432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,FOUR (P2432) 11 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>IN</u> Inactivate a problem

Select Problem (1-11): <u>1</u>

Anxiety (SCT 48694002)

DATE RESOLVED: TODAY// <u>5/1/17</u>

COMMENT (\<200 char): <u>Problem cleared up after treatment and rest</u>

.....inactivated!

1. Type your patient’s name.
2. Type IN for Inactivate a problem.
3. Type the number of the problem (shown in the left-hand column).
4. Type the date the problem was resolved, if known.
5. Add a new comment, if desired.
6. An “I” will now appear between the number and text of the problem, to indicate that the problem is inactive.

Print Problem List

You can print the currently displayed list or a complete list with active and inactive problems. You will be prompted to select the print device.

Select Problem List Menu Option: <u>pl</u> Patient Problem List

Select PATIENT NAME: <u>PLPATIENT,FOUR</u> 03-04-14 666432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,FOUR (P2432) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

D Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>PP</u> Print Problem List

Print (C)urrently displayed problems only, or include (A)ll problems? <u>C</u>

DEVICE: HOME// \<Enter\>1. Type PP for Print List.

2. Select C for currently displayed list or A for all problems (active, inactive, etc.).
3. Type the name of the printer at the “DEVICE” prompt.

> Displayed Problem ListCurrently Displayed List

------------------------------------------------------------------------------

\*\* NOT for Medical Record \*\* \| PARTIAL PROBLEM LIST

------------------------------------------------------------------------------

Date Date of Date

Recorded Problems Onset Resolved

------------------------------------------------------------------------------

1\. 4/25/17 Anxiety (SCT 48694002)(ICD-10-CM R69) 4/25/17

2\. 11/27/16 Hypertension (SCT 38341003)(ICD-10-CM R69) 11/27/16

3\. 3/30/17 Hyperlipidemia (SCT 55822004)(ICD-10-CM R69) 3/30/17

4\. 3/17/17 Acute myocardial infarction (SCT 57054005) 3/17/17

(ICD-10-CM R69)

5\. 3/9/17 Chronic Systolic Heart failure (SCT 3/9/17

441481004\)\(ICD-10-CM R69)

----------------------------------------------------------------------------

PLPATIENT,FOUR (P2432) SALT LAKE CITY VAMC Printed 12/4/17

666-95-2432 Page 1

----------------------------------------------------------------------------

> Printed Problem ListComplete List

------------------------------------------------------------------------------

Medical Record \| PROBLEM LIST

------------------------------------------------------------------------------

Date Date of Date

Recorded Problems Onset Resolved

------------------------------------------------------------------------------

1\. 4/25/17 Anxiety (SCT 48694002)(ICD-10-CM R69) 4/25/17

2\. 11/27/16 Hypertension (SCT 38341003)(ICD-10-CM R69) 11/27/16

3\. 3/30/17 Hyperlipidemia (SCT 55822004)(ICD-10-CM R69) 3/30/17

4\. 3/17/17 Acute myocardial infarction (SCT 57054005) 3/17/17

(ICD-10-CM R69)

5\. 3/9/17 Chronic Systolic Heart failure (SCT 3/9/17

441481004\)\(ICD-10-CM R69)

6\. 2/19/17 Multiple Sclerosis (SCT 24700007)(ICD-10-CM 2/12/17

R69)

7\. 2/19/17 Cholecystitis (SCT 76581006)(ICD-10-CM R69) 2/3/17

8\. 5/26/17 Diabetes Mellitus (SCT 73211009)(ICD-10-CM 5/26/17

R69)

9\. 7/15/17 Hemotysis (SCT 66857006)(ICD-10-CM R69) 7/15/17

10\. 7/21/17 Fracture of multiple ribs (SCT 1261007) 7/21/17

(ICD-10-CM R69)

------------------------------------------------------------------------------

PLPATIENT,FOUR (P2432) SALT LAKE CITY VAMC Printed 12/24/17

666-95-2432 Page 1

------------------------------------------------------------------------------

> Remove Problems

> You can remove a problem from the list if it was incorrectly entered.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/037.png)</p></th>
<th><blockquote>
<p>If it is necessary to see problems that have been removed or you want to replace them on the list, someone with the Problem List Mgt Menu can access the option, Replace Removed Problems on Patient’s List, to do this.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select PATIENT NAME: <u>PLPATIENT,FOUR</u> 03-04-14 666432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page: 1 of 3</u>

PLPATIENT,FOUR (P2432) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Newt Screen// <u>RM</u> Remove Problems

Select Problem (1-12): <u>1</u>

> **CAUTION:** This problem will be completely removed from this patient’s list!!

Are you sure? NO// <u>Yes</u>

Anxiety (SCT 48694002)

REASON FOR REMOVAL: <u>?</u>

Enter any text you wish appended to this problem, up to 200 characters in length. You may append as many comments to a problem as you wish.

REASON FOR REMOVAL: <u>Wrong patient</u>

... removed!

1. Type RM for Remove Problems, at the “Select Action” prompt.
2. Type the number of the problem you wish to remove.
3. Type Yes, if you’re sure this is the problem you wish to remove.
4. Enter a reason for removing the problem (optional).

> Select New Patient

Use this action to access other patients’ problem lists without exiting back to the menu.

Select Problem List Menu Option: <u>pl</u> Patient Problem List

Select PATIENT NAME: PLPATIENT,FOUR 10-15-35 666032432 SC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page: 1 of 3</u>

PLPATIENT,FOUR (P2432) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>SP</u> Select New Patient

Select PATIENT NAME: <u>PLPATIENT,TWO</u> PLPATIENT,TWO 06-18-62 666223333 NON-VETERAN (OTHER)

Searching for the patient’s problem list ...

<u>PROBLEM LIST APR 30, 2017 16:00 Page 1 of 3</u>

PLPATIENT,TWO (P3333) 15 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Bacterial pneumonia (SCT 53084003 4/30/17 IMD

), Onset 4/28/17

Treated last month also

2 Anemia (SCT 271737000), Onset 4/30/17 PTSD

4/20/17

3 Malaise and fatigue (SCT 3/20/17 PTSD

271795006\), Onset 3/1/17

4 CHOLECYSTITIS (SCT 76581006), 3/20/17 MED

ONSET 2/23/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action:

1. Type SP for Select New Patient.
2. Type the new patient’s name.

*The new patient’s list is displayed.*

## Select View of List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action lets you view your problem list several different ways, such as by a selected clinic, a selected provider, active or inactive problems only, etc.

Select Problem List Menu Option: <u>pl</u> Patient Problem List

Select PATIENT NAME: <u>PLPATIENT,FOUR</u> 10-15-35 666032432 SC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page: 1 of 3</u>

PLPATIENT,FOUR (P2432) 5 of 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>vw</u> Select view of list

CURRENT VIEW: Outpatient, active problems from preferred clinics.

You may change your view of this patient's problem list by selecting one or more of the following attributes to alter:

AT Active only SC Selected Clinic(s) PR Selected Provider

IA Inactive only CL All Clinics AP All Providers

BO Active & Inactive IP Inpatient View PV Preferred View

Select Item(s):

1. Type VW for Select View of List at the Select Action prompt.
2. Type the abbreviation(s) for the attribute(s) that describe the way you wish to view problem lists.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/038.png)</p></th>
<th><blockquote>
<p>The Preferred View action will display the selection (if any) you have made through the option Problem List Preferred View on the Create Problem Selection List menu.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Show All Problems

> This action on the Data Entry option lets a clerk view all active and inactive problems.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/039.png)</p></th>
<th>When problems are entered into the problem list with no ICD code attached, the system automatically assigns the number R69.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<u>PROBLEM LIST Apr 16, 2004 14:19:45 Page: 1 of 2</u>

PLPATIENT,TWO (P3333) 26 active problems

ACTIVE PROBLEMS

<u>Problem ICD SC Exposure Resolved</u>

1 Multiple Sclerosis (SCT R69 YES Agent Orange

24700007), Onset 3/5/17

2 Cholecystitis (SCT 76581006), R69 YES Radiation

Onset 3/7/17

3 Diabetes Mellitus (SCT R69 NO

73211009), Onset 4/1/17

4 Hemotysis (SCT 66857006) R69 NO

5 Fracture of multiple ribs (SCT R69 NO

1261007\)

6 Pneumonia, Pneumocystis carinii R69

7 Respiratory Distress Syndrome R69

8 Peripheral Vascular Disease R69

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate a Problem SP Select New Patient

RM Remove Problems CM Comment on a Problem PP Print Problem List

ED Edit a Problem VW Show All Problems Q Quit

Select Action: Next Screen// <u>VW</u>

Searching for the patient's problem list ...

1. Type your patient’s name at the “Select Patient Name” prompt.
2. Type VW for Show All problems.

*All the problems for this patient will be displayed, with a column indicating whether the problem is Inactive (I).*

<u>PROBLEM LIST Apr 16, 2017 14:19:45 Page: 1 of 2</u>

PLPATIENT,TWO (P3333) 26 active problems

ALL PROBLEMS

<u>Problem ICD SC Exposure Resolved</u>

1 Multiple Sclerosis (SCT R69 YES Agent Orange

24700007), Onset 3/5/17

2 Cholecystitis (SCT 76581006), R69 YES Radiation

Onset 3/7/17

3 Diabetes Mellitus (SCT R69 NO

73211009), Onset 4/1/17

4 I Hemotysis (SCT 66857006) R69 NO

5 I Fracture of multiple ribs (SCT R69 NO

1261007\)

6 Pneumonia, Pneumocystis carinii R69

7 Respiratory Distress Syndrome R69

8 Peripheral Vascular Disease R69

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate a Problem SP Select New Patient

RM Remove Problems CM Comment on a Problem PP Print Problem List

ED Edit a Problem VW Show All Problems Q Quit

Select Action: Next Screen//

> c2.Verify Problems

If problems are entered from an Encounter Form (or other printed material) by clerks, the hospital can set a parameter to require that these transcribed problems must be verified by the clinician.

When the problem appears on the problem list, it will have a \$ beside it to indicate that the clinician must take action to verify that the problem is correct as entered.

Select Problem List Menu Option: <u>pl</u> Patient Problem List

Select PATIENT NAME: PLPATIENT,FOUR 03-04-14 666432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,FOUR (P2432) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 \$ Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate a Problem VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>\$</u>

Select the problem(s) you wish to verify as correct.

Select Problem(s) (1-5): <u>2</u>

Hypertension (SCT 38341003)

...verified!

1. Type \$ at the “Select Action” prompt.
2. Type the number of the problem to be verified.
3. The problem list will be displayed again without the \$ beside the verified problem.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/040.png)</p></th>
<th>See the Edit PL Site Parameters description in the Package Management section of this manual for instructions on how to set the parameter requiring (or not requiring) clinician verification.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## More Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A secondary list of actions is available if you enter two question marks (??) at the Select Action prompt. These are mostly navigational actions that are not directly related to performing actions on the problem list itself.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/041.png)</p></th>
<th>If a $ (dollar sign) appears beside a problem (see problem 1 in example), it means that the problem was entered by a clerk and requires clinician review. This is a site parameter that must be set through the option Edit PL Site Parameters.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Problem List Menu Option: <u>pl</u> Patient Problem List

Select PATIENT NAME: <u>PLPATIENT,FOUR</u> 03-04-14 123432432 NSC VETERAN

Searching for the patient's problem list...

<u>PROBLEM LIST Apr 30, 2017 15:40:06 Page:1 of 3</u>

PLPATIENT,FOUR (P4567) 12 active problems

ACTIVE PROBLEMS

<u>Problem Updated Clinic</u>

1 \$Anxiety (SCT 48694002), Onset 4/29/17 ISC

4/25/17

2 Hypertension (SCT 38341003), Onset 4/26/17 PSYC

11/27/16

3 Hyperlipidemia (SCT 55822004), 4/7/17 AC

Onset 3/30/17

4 Acute myocardial infarction (SCT 4/1/17 AC

57054005), Onset 3/17/17

5 Chronic Systolic Heart failure (SCT 4/1/17 AC

441481004\), Onset 3/9/17

+ + Next Screen - Prev Screen ?? More actions

AD Add New Problems IN Inactivate Problems VW Select View of List

RM Remove Problems CM Comment on a Problem SP Select New Patient

ED Edit a Problem DT Detailed Display PP Print Problem List

\$ Verify Problems Q Quit

Select Action: Next Screen// <u>??</u>

To update the problem list first select from Add, Remove, Edit,

Verify, Inactivate, or Comment, then enter the problem

number(s). If you need more information on a problem, select

Detailed Display; to change whether all or only selected

problems for this patient are listed, choose Select View. Enter

?? to see more actions for facilitating navigation of the list.

Problem statuses: \* - Acute I - Inactive \$ - Unverified

Press \<return\> to continue...

The following actions are also available:

\+ Next Screen FS First Screen SL Search List

\- Previous Screen LS Last Screen ADPL Auto Display(On/Off)

UP Up a Line RD Re-Display Screen QU Quit

DN Down a Line PS Print Screen

GO Go to Page PL Print List

Press RETURN to continue or '^' to exit:

1. Type two question marks.
2. Additional available actions are displayed.
3. Select the abbreviation of the action you wish.

### How to Use Problem List User GUI Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you select the Problems tab, the Action menu on the toolbar contains actions relevant to Problem List: New Problem, Change, Inactivate, Verify, Annotate, Remove, and Restore.

![](problem-list-user-manual-version-2-gmpl-2-60/042.png)

Annotating a Problem

To annotate a problem, use these steps:

1\. Click on the problem in the problem list.

2\. Select Action \| Annotate... or right-click the problem and select Annotate... from the pop-up menu.

3\. Enter your annotation in the dialog that appears (up to 200 characters).

4\. Click OK.

Changing a Problem

To change a problem on a patient’s problem list, use these steps:

1\. Click the Problems tab.

2\. Click on the problem in the list box that you want to change.

3\. Select Action \| Change… or right-click the problem and select Change... from the pop-up menu.

4\. Enter the desired changes.

5\. Add or remove a comment if desired.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/043.png)</p></th>
<th><blockquote>
<p>A comment can be as many as 200 characters (including spaces) in length.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

6\. Click OK.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Note:</p>
<p>![](problem-list-user-manual-version-2-gmpl-2-60/044.png)</p></th>
<th>When you view the details of a problem, you will see who changed the problem and when.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](problem-list-user-manual-version-2-gmpl-2-60/045.png)

Inactivating a Problem

To deactivate a problem on a patient’s problem list, use the following steps:

1\. Click on a problem in the list box.

2\. Select Action \| Inactivate or right-click the problem and select Inactivate from the pop-up menu.

Removing a Problem

A problem is not removed from the database because things “pointing” to it might be broken if it is removed. A field in the problem record can be “flagged” with an “H” and the problem will be HIDDEN. Any software that runs on the database must look at the field to see if it is hidden or not. The hidden record will not appear on any reports or lists and will appear to the user that it has been removed. Actually it is only removed from sight.

To remove a problem from a patient’s problem list, use these steps:

1\. Click on the problem.

2\. Select Action \| Remove or right-click the problem and click Remove.

Verifying a Problem

To verify a problem on a patient’s problem list, use these steps:

1\. Click on the problem in the problem list.

2\. Select Action \| Verify or right-click the problem and click Verify on the pop up menu.

# Helpful Hints & Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Helpful HintsQ: When I want to add a problem that has many different names (more than five) to choose from, is there any way I can scroll back to the top of the list?

A: If you type an up-arrow and the number of the problem (^#), you will go back to the group of five numbers that includes the number you entered.

*Example*:

Select Action: Next Screen// <u>ad</u> Add New Problem(s)

PROBLEM: diabetes

457 matches found

1 Renal diabetes (SNOMED CT 236367002)

2 Bronze diabetes (SNOMED CT 399144008)

3 Diabetes mellitus (SNOMED CT 73211009)

4 Diabetes resolved (SNOMED CT 315051004)

5 Diabetes insipidus (SNOMED CT 15771004)

Type "^" to STOP or Select 1-5: \<ENTER\>

6 Anemia of diabetes (SNOMED CT 82980005)

7 Adult diabetes diet (SNOMED CT 34170007)

8 Child diabetes diet (SNOMED CT 79367009)

9 Diarrhea in diabetes (SNOMED CT 38205001)

10 Lipoatrophic diabetes (SNOMED CT 127012008)

Type "^" to STOP or Select 1-10: <u>^3</u>

1 Renal diabetes (SNOMED CT 236367002)

2 Bronze diabetes (SNOMED CT 399144008)

3 Diabetes mellitus (SNOMED CT 73211009)

4 Diabetes resolved (SNOMED CT 315051004)

5 Diabetes insipidus (SNOMED CT 15771004)

Type "^" to STOP or Select 1-10:

Q: Can I add Problem List items to the Health Summary?

A: You can add Problem List components (Active, Inactive, and All) to your Health Summary when you build a Health Summary type. You can also jump between Health Summary and Problem List if you attach the two protocols listed above.

Q: How can I change the length of time before the system times out? Frequently, I have to leave my terminal to take care of a patient or other business; then when I come back, I have to log in and go through all the prompts and such to get back to where I was.

A: Each site sets its time-outs; talk to your ADPAC or IRMS to see what can be done. Security is the main issue in determining time-out times.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \$ A symbol that can appear beside a problem, indicating that the problem was entered by a clerk and needs to be verified by a physician. For this functionality to exist, a site parameter must be set through the option Edit PL Site Parameters (on the Problem List Mgt Menu).
> \* A symbol that can appear beside a problem, indicating that the problem has been designated as acute or critical.
> Action A functional process a user takes within the Problem List option that affects the end result or, what is actually accomplished by the option.
> *Examples*: Edit a problem, print a problem list, add a comment to a problem.
> CPT Current Procedural Terminology, a coding system of medical terms, used for billing purposes.
> Clinical Term Names used for problems, diagnoses, procedures, etc.
> Clinician A doctor or other health care provider in the medical center who is authorized to enter problems onto a patient’s chart.
> DSM-IV Diagnostic and Statistical Manual of Mental Disorders, 4th Ed,.
> Encounter Form A paper form (which can be created by a form generator utility) for use with Problem List to print a patient’s problems on, for the clinician to edit and/or add new problems, then used by clerks to enter new problems and/or edit existing problems.
> Health Summary A VistA clinical module that allows users to compile summaries of a patient’s health care by combining various components of data drawn from other VistA modules such as Laboratory, Pharmacy, and Radiology.
> ICD-9-CM; International Classification of Diseases, 9th Rev, Clinical Modification, 1991.
> ICD-10-CM; International Classification of Diseases, 10th Rev, Clinical Modification, 2015.
> Indian Health Service The Indian Health Service has a computerized
> (IHS) system comparable to VistA, called Resource and Patient Management System (RPMS).
> Lexicon A terminology utility that uses UMLS terms, the Multiterm Lookup and other utilities to provide clinical terms and concepts, semantic types, special coding, etc.
> NTRT New Term Rapid Turnaround (NTRT) is the process to distribute standard reference files to VistA and to HealtheVet environments.
> PCE Patient Care Encounter, a VistA application.
> PL Occasionally this abbreviation for Problem List is used in option or menu names.
> Problem The term that the clinician gives to a patient’s complaint or diagnosis.
> Progress Note A VistA module, as well as a non-computerized form, for maintaining text about a patient’s condition.
> SNOMED Systematic Nomenclature of Medicine, another coding system, used mostly by the Anatomic Pathology module of Laboratory.
> Specialty Subset Because many discipline-specific terms are synonyms to other terms, they are not accessible unless you specify the appropriate subset of the Lexicon to choose from. When building problem selection lists, users must choose one of the following specialty subsets: Nursing, Dental, Social Work, Immunology, or General Problem.
> VistA Veterans Information System Technology Architecture, the VHA computer program used in VA facilities.

# Appendix A: Lexicon/NTRT Tips for the Problems Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In 2013 the Problem List application adopted SNOMED CT to comply with the interoperability terminology standard in support of data exchange among the DoD, VA, and private sector healthcare providers worldwide. Therefore enhancements were implemented to support the standardization effort.

Lexicon searches are based on the SNOMED CT vocabulary, a clinical terminology rather than the administrative code set of ICD.

1.  There are two searches—Initial and Extended: The initial search displays matches from a commonly used list of SNOMED CT terms used within the VA. If the desired term is not found on the initial list, use the Extend Search button to display a list of matches from a larger set of SNOMED CT and matches from the initial search.

*<u>Example from the initial search</u>*

> ![](problem-list-user-manual-version-2-gmpl-2-60/046.png)

> ![](problem-list-user-manual-version-2-gmpl-2-60/047.png)

![](problem-list-user-manual-version-2-gmpl-2-60/048.png)

2.  The extended search displays a list of matches from a larger set of SNOMED CT as well as matches from the initial search. By default, matches from the extended search are mapped to ICD-10-CM code R69 the equivalent of ICD-9-CM code799.9.

*<u>  
Example from the extended search</u>*

> ![](problem-list-user-manual-version-2-gmpl-2-60/049.png)

*<u>  
Example of the 799.9 Updated in the Patient Record</u>*

![](problem-list-user-manual-version-2-gmpl-2-60/050.png)![](problem-list-user-manual-version-2-gmpl-2-60/051.png)

3.  If there are no matches from the initial search or extended search, the user may have the option to enter a free text problem entry by clicking on the free text problem button. A dialog box displays giving the user a choice to submit his/her term to the STS team for consideration to be added to the Core Problem List subset or to return to the search dialog to again search for a closely related term. By clicking on “Apply for New Term” a bulletin is automatically generated as shown below.

*<u>Example of Bulletin for a New Problem/Diagnosis Request</u>*

> Subj: NEW PROBLEM/DIAGNOSIS TERM REQUEST \[#196413\] 02/14/12@15:54 33 lines

> From: OR PROBLEM NTRT BULLETIN In 'IN' basket. Page 1 \*New\*

> ------------------------------------------------------------------------

> \*\*\* New Problem/Diagnosis Term Request \*\*\*

> Requested term: acroangiodermatitis of mali

> Date/Time of request: 2/14/12@15:54

> Name of requester: Ten Cprsprodvider MD

> Service: INFORMATION OFFICE

> Location: SITE VAMC(442)

> A New Term Rapid Turnaround (NTRT) mail message has been sent to you because a user from your facility has failed to find a suitable term after initiating the search options within the Problem List application

> and has chosen to request a new term to be added to the Problem List subset.

> Please review the requested term and verify it is understandable, clinically useful, and does not already exist within the Problem List subset. If the term is found appropriate, then submit a NTRT request at the NTRT website, http://vista.med.va.gov/ntrt/. Follow the link to Access the NTRT Request Web Site.

> The Problem List domain steward will review each request and respond to you with the outcome of this request. If the term is approved by the Problem List NTRT committee it will be added to the Problem List subset and made available within future searches.

> The progress of this request may be monitored by accessing the NTRT website at the NTRT website.

> If you have questions, need more information, or are having accessibility problems with this website, please contact STS by Exchange E-Mail: \[VHA OI HDI STS NTRT\].

> Thank-you.

4.  Submitting New Term Rapid Turnaround Requests (NTRT)

All users must have logon access to submit new term requests. This is in addition to your VA authentication. If you do not have access, contact your CPRS <span id="removed_2" class="anchor"></span>administrator.

Below is the Welcome page where you enter your “Username” and “Password” to logon. Logon names and passwords are case-sensitive.

5.  Setting the new ORQQPL Parameter

This parameter determines whether the user will be shown SNOMED CT and ICD codes when searching for patient problems.

1.  Logon to Programmer Mode.
2.  Select OPTION NAME: XPAR MENU TOOLS General Parameter Tools
3.  Select General Parameter Tools Option: EP  Edit Parameter Values       
4.  Select PARAMETER DEFINITION NAME: ORQQPL SUPPRESS CODES Suppress Codes in Lexicon Problem Search
5.  ORQQPL SUPPRESS CODES may be set for the following:

>      5   User          USR    \[choose from NEW PERSON\]

>      10  Service       SRV    \[choose from SERVICE/SECTION\]

>      15  Division      DIV    \[choose from INSTITUTION\]

>      20  System        SYS    \[xxx.VA.GOV\]

6.  Enter selection: 5  User   NEW PERSON
7.  Select NEW PERSON NAME: \<USER\>
8.  Setting ORQQPL SUPPRESS CODES for User: \<USER\> Suppress Codes?: NO// ?

> This indicates whether code values should be hidden during Problem searches. Suppress Codes?: NO// YES

> Setting the parameter value to YES will suppress the code display during lexicon look-ups. If you wish to set it for a given service, division, or system-wide, you can set the value at the corresponding level.

> ORQQPL SUPPRESS CODES may be set for the following:

>      5   User          USR    \[choose from NEW PERSON\]

>      10  Service       SRV    \[choose from SERVICE/SECTION\]

>      15  Division      DIV    \[choose from INSTITUTION\]

>      20  System        SYS    \[xxxmVA.GOV\]

6.  Setting up CPRS Tools Menu (instructions for this are in the CPRS Technical Manual as well)
1.  In VistA, go to CPRS Configuration Clinical Coordinator.
2.  Select GUI Parameters
3.  GUI Tool Menu Items
4.  Setup for a User, Location, Service, System, or Division.
5.  Add New Sequence
6.  Name=Command: Terminology
7.  Browser=http://vahdrppwls14.aac.xxx:7204/sts.browser/index.action
8.  Open CPRS, Click on Tools in the Menu Bar and View the Terminology <span id="removed_3" class="anchor"></span>Browser. ![](problem-list-user-manual-version-2-gmpl-2-60/052.png)
7.  Setting up Selection List

Below is a quick set up instructions for building a problem Selection List. Refer to Problem List User Manual for other options

Management Menu Options

1.  Problem List Mgt Menu \[GMPL Mgt Menu\]
2.  Create Problem Selection List(s)
3.  Build Problem Selection List(s)
4.  Allows you to create a pick list
5.  Add categories to it
6.  Add problems to categories
7.  Assign the list to a user of clinic
8.  Select LIST NAME: type the name of new selection list that you want to have this list associated
9.  Type a name for a category you wish to have on your list
10. At the “Selection Action”, type AD for Add Problems
11. Type the name of a problem for this category
12. Accept defaults for display text, code and sequence or enter new values
13. Assign List to users to make list available on the Problems Tab

> ![](problem-list-user-manual-version-2-gmpl-2-60/053.png)

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# -, 18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$, 18

\$, 104

( ), 19

\*, 19

//, 18

?, 18

??, 18

^, 18

+, 18

Encounter Form, 110

Health Summary, 110

ICD-9-CM, 111

Indian Health Service, 111

PCE, 111

Problem, 111

Problem List, 75

Progress Note, 111

SNOMED, 111

Specialty Subset, 112