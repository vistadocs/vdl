---
title: AICS Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: IBD
app_name: Automated Information Collection System (AICS)
section: FIN
app_status: active
pkg_ns: IBD
patch_ver: 3
patch_id: IBD*3
group_key: "IBD:IBD:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - form
  - forms
  - encounter
  - print
  - table
  - contents
  - edit
  - clinic
  - code
  - class
page_count: 0
word_count: 25747
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics_3_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics_3_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSUSERManual

![](aics-version-3-user-manual/001.png)

April 1997

Office of Information and Technology

Product Development

<span id="revhist" class="anchor"></span>Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 21%" />
<col style="width: 39%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>April 2014</td>
<td><p>IBD*3.0*63</p>
<p>Title page</p>
<p><a href="#ICDpiv">Table of Contents</a></p>
<p>p. <a href="#ICDp1">1</a></p>
<p>pp. <a href="#ICDp2">2</a>, <a href="#ICDp75">75</a></p>
<p>pp. <a href="#ICDp7">7</a>, <a href="#ICDp84">84</a></p>
<p>p. <a href="#p7a">7</a></p>
<p>pp. <a href="#p35">35</a>, <a href="#ICDp38">38</a></p>
<p>p. <a href="#ICDp75b">75</a></p>
<p>p.<a href="#ICDp76">76</a></p>
<p>pp.<a href="#ICDp83">83-84</a></p>
<p>pp.<a href="#icd-10-search-functionality">85-89</a></p>
<p>p. <a href="#ICDp93">93</a></p>
<p>pp. <a href="#ICDp97">97-98</a></p></td>
<td><p>Updates for ICD-10 remediation.</p>
<p>Revised per ProPath template</p>
<p>Updated TOC</p>
<p>Updated information in Introduction</p>
<p>Problem List made Unavailable.</p>
<p>Note about Lexicon filters when editing encounter forms.</p>
<p>Note about Inactive ICD-10 codes</p>
<p>Added ICD-10.</p>
<p>Added ICD-10 information and example screen</p>
<p>Added example of new prompt for Replace Code</p>
<p>Added information on new report: Encounter Forms ICD-10 Update</p>
<p>Added information on ICD-10 search functionality and examples</p>
<p>Added ICD-10 information to Glossary</p>
<p>Updated Index</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/4/04</td>
<td>Updated manual to comply with SOP 192-352 Displaying Sensitive Data</td>
<td>REDACTED</td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

> [Edit Encounter Forms 7](#edit-encounter-forms)

> [Clinic Setup/Edit Forms 7](#ClinicSetup)

> [Copy CPT Check-off Sheet to Encounter Form 15](#section)

> [Most Commonly used Outpatient CPT Codes 16](#section-1)

> [Print Options 18](#print-options)

> [Print Encounter Forms for Appointments 18](#section-2)

> [Print Form w/Patient Data, No Appt 21](#section-4)

> [Print Blank Encounter Form 23](#section-5)

> [Print Manager 25](#print-manager)

> [Edit Division Reports 25](#edit-division-reports)

> [Edit Clinic Reports 27](#section-6)

> [Define Available Health Summary 29](#section-7)

> [Report Clinic Setups 30](#section-8)

> [Setup Automatic Print Queues 31](#section-12)

> [Edit Tool Kit 34](#edit-tool-kit)

> [Edit Tool Kit Blocks 34](#section-20)

> [Edit Tool Kit Forms 36](#section-21)

> [Encounter Form IRM Options 39](#encounter-form-irm-options)

> [Edit Package Interface 39](#section-23)

> [Edit Marking Area (for selection lists) 45](#section-25)

> [Define Available Report (not Health Summaries) 47](#section-27)

> [Import/Export Utility 51](#section-28)

> [Recompile All Forms 62](#section-29)

> [Miscellaneous Cleanup 63](#section-31)

> [Device Edit 64](#device-edit)

> [Purge Form Tracking files 65](#section-34)

> [Reports and Utilities 66](#reports-and-utilities)

> [Form Components 66](#form-components)

> [Edit Site Parameters 67](#edit-site-parameters)

> [Scanning Error Listing 70](#scanning-error-listing)

> [Forms Tracking 71](#forms-tracking)

> [List Clinics Using Forms 74](#list-clinics-using-forms)

> [Maintenance Utility for Active/Inactive Codes 75](#maintenance-utility-for-activeinactive-codes)

> [Clinics With No Encounter Forms 78](#clinics-with-no-encounter-forms)

> [Print Sample of all Forms 79](#print-sample-of-all-forms)

> [Report Clinic Setups 82](#report-clinic-setups-1)

> [Encounter Forms ICD-10 Update 83](\l)

> [ICD-10 Search Functionality 85](#icd-10-search-functionality)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [OrientationPackage Operation](#orientationpackage-operation)
- [Package Management](#package-management)
- [Package Operation](#package-operation)
  - [Edit Encounter Forms](#edit-encounter-forms)
    - [Clinic Setup/Edit Forms](#clinic-setupedit-forms)
    - [### Copy CPT Check-off Sheet to Encounter Form](#copy-cpt-check-off-sheet-to-encounter-form)
    - [### Most Commonly used Outpatient CPT Codes](#most-commonly-used-outpatient-cpt-codes)
  - [Print Options](#print-options)
    - [### Print Encounter Forms for Appointments](#print-encounter-forms-for-appointments)
    - [Introduction](#introduction-1)
    - [### Print Form w/Patient Data, No Appt](#print-form-wpatient-data-no-appt)
    - [### Print Blank Encounter Form](#print-blank-encounter-form)
  - [Print Manager](#print-manager)
    - [Edit Division Reports](#edit-division-reports)
    - [### Edit Clinic Reports](#edit-clinic-reports)
    - [### Define Available Health Summary](#define-available-health-summary)
    - [### Report Clinic Setups](#report-clinic-setups)
- [Introduction](#introduction-2)
- [This option provides a report, by division that lists each clinic setup and the encounter forms and other reports defined for use by that clinic. For clinics with reports defined, the condition on which the report is printed is also provided.](#this-option-provides-a-report-by-division-that-lists-each-clinic-setup-and-the-encounter-forms-and-other-reports-defined-for-use-by-that-clinic-for-clinics-with-reports-defined-the-condition-on-which-the-report-is-printed-is-also-provided)
- [Example](#example)
    - [### Setup Automatic Print Queues](#setup-automatic-print-queues)
- [Introduction](#introduction-3)
- [This option allows you to enter Print Manager queuing parameters and to specify automatic queuing parameters.](#this-option-allows-you-to-enter-print-manager-queuing-parameters-and-to-specify-automatic-queuing-parameters)
- [Example](#example-1)
- [<u>Print Mgrs. Queuing Params. Mar 06, 1997 16:15:40 Page: 1 of 1</u>](#uprint-mgrs-queuing-params-mar-06-1997-161540-page-1-of-1u)
- [# Select Print Mgrs. Queuing Params. Name: NEW GROUP](#select-print-mgrs-queuing-params-name-new-group)
- [PRINT PRIORITY: 1// ??](#print-priority-1)
  - [Edit Tool Kit](#edit-tool-kit)
    - [### Edit Tool Kit Blocks](#edit-tool-kit-blocks)
    - [### Edit Tool Kit Forms](#edit-tool-kit-forms)
    - [Introduction](#introduction-4)
  - [Encounter Form IRM Options](#encounter-form-irm-options)
    - [### Edit Package Interface](#edit-package-interface)
    - [Introduction](#introduction-5)
    - [### Edit Marking Area (for selection lists)](#edit-marking-area-for-selection-lists)
    - [Introduction](#introduction-6)
    - [### Define Available Report (not Health Summaries)](#define-available-report-not-health-summaries)
    - [### Import/Export Utility](#importexport-utility)
    - [### Recompile All Forms](#recompile-all-forms)
    - [Introduction](#introduction-7)
    - [### Miscellaneous Cleanup](#miscellaneous-cleanup)
    - [Introduction](#introduction-8)
    - [Device Edit](#device-edit)
    - [Introduction](#introduction-9)
  - [Example](#example-2)
    - [### Purge Form Tracking files](#purge-form-tracking-files)
  - [Reports and Utilities](#reports-and-utilities)
    - [Form Components](#form-components)
    - [Introduction](#introduction-10)
    - [Edit Site Parameters](#edit-site-parameters)
    - [Scanning Error Listing](#scanning-error-listing)
    - [Introduction](#introduction-11)
    - [Forms Tracking](#forms-tracking)
    - [Introduction](#introduction-12)
    - [List Clinics Using Forms](#list-clinics-using-forms)
    - [Maintenance Utility for Active/Inactive Codes](#maintenance-utility-for-activeinactive-codes)
    - [Clinics With No Encounter Forms](#clinics-with-no-encounter-forms)
    - [Print Sample of all Forms](#print-sample-of-all-forms)
    - [Introduction](#introduction-13)
    - [Report Clinic Setups](#report-clinic-setups-1)
    - [Introduction](#introduction-14)
- [This option provides a report that lists each clinic setup, and the encounter forms and other reports defined for use by that clinic. For clinics with reports defined, the condition on which the report is printed is also provided.](#this-option-provides-a-report-that-lists-each-clinic-setup-and-the-encounter-forms-and-other-reports-defined-for-use-by-that-clinic-for-clinics-with-reports-defined-the-condition-on-which-the-report-is-printed-is-also-provided)
    - [Encounter Forms ICD-10 Update](#encounter-forms-icd-10-update)
    - [Introduction](#introduction-15)
    - [ICD-10 Search Functionality](#icd-10-search-functionality)
- [Glossary](#glossary)
- [Index](#index)
- [Appendix A - Background EF Print with Special Instructions](#appendix-a-background-ef-print-with-special-instructions)
- [Appendix B - List Manager](#appendix-b-list-manager)
- [Appendix C - Scanning](#appendix-c-scanning)
- [Appendix D - HP LaserJet 5Si Printer](#appendix-d-hp-laserjet-5si-printer)
The encounter form is designed specifically for outpatient visits. It is used both to display relevant patient data for use during the visit, such as demographics, allergies, and problems; and to collect data about the visit, such as procedures and tests performed. Its primary focus is clinical and to collect data for the Ambulatory Care Reporting Project. It also has other purposes such as collecting data necessary for billing.
The AICS package contains all the software necessary to design, edit, and assign encounter forms to clinics. The software enables collection of outpatient clinical and administrative data; and provides a more organized, less obtrusive method of data collection to the clinician and supporting clerical staff.
<span id="ICDp1" class="anchor"></span>Many of the lists that a user sees in Computerized Patient Record System (CPRS) for input of outpatient encounter data are based on lists created when designing encounter forms for clinics.
A form generator is included, which allows sites to design forms which meet local medical facility needs. There is enough flexibility in the software so sites can build forms that meet their individual clinical, billing, and resource requirements. The encounter form may be filed in the clinical record.
A print manager is included that allows sites to print blank encounter forms, but only on a contingency basis or for non-patient uses such as employee health, since VA policy prohibits the use of printed encounter forms as a rule. Reports and Utilities options are available to assist with maintenance of the encounter forms.
Features supporting the scanning of encounter forms are no longer available, with the onset of electronic means of entering data using the lists provided in the encounter forms, such as CPRS.
Code Set Versioning
With functionality put in place by the Code Set Versioning project, the options listed below have been deleted from AICS. The user will see the following message.
Sorry, your Primary Menu is out of order with the message: \*\* This option is OUT OF ORDER \*\*
Clinic Based Data Entry
Conversion Utility for Scanning
Data Entry by Form
Form Component Inquiry
Group Clinic Data Entry
Pre-printed From Data Entry
Scanned Forms w/Bill Gen
Validate Forms
Functionality
The AICS software provides:
a "tool kit" of forms and components that allows sites to avoid the time consuming process of creating forms from scratch;
a "form generator" to allow sites to design custom forms;
a print manager that allows sites to define reports to print along with the encounter form;
an import/export utility that enables sites to exchange forms and components;
V*IST*A interfaces that allow patient demographic data, insurance data, allergies, and problems to be displayed. More interfaces can be added in the future, as requested.
Integration
AICS integrates with the following software for the purpose indicated.
Scheduling - clinic setup, patient information, and list creation.
International Classification of Diseases (ICD) - list creation.
Current Procedural Terminology (CPT) - list creation.
Patient Care Encounter (PCE) - list creation.
Clinical Lexicon - list creation.
<span id="ICDp2" class="anchor"></span>Problem List - list creation. Obsolete. Made Unavailable by IBD\*3\*63.
Allergy - patient information.
Integrated Billing (IB) - billing information for reports.
Health Summary - print health summaries for patient appointments.
Outpatient Pharmacy - print action profiles for patient appointments.
Accounts Receivable (AR) - billing information for reports.
Related Manuals
- AICS V. 3.0 Technical Manual - assists the site manager in maintenance of the software.
- AICS V. 3.0 Installation Guide - provides assistance in installation of the software.
- AICS V. 3.0 Release Notes - describe any modifications and enhancements to the software new to this version.

# OrientationPackage Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Package Operation section provides documentation of each option, including a brief introduction to the option, sample screens, and sample outputs, when applicable.

List Manager

AICS uses the List Manager utility; a tool designed to list items for selection and action. Available actions are displayed below the screen. A double question mark (??) entered at any "Select Action" prompt displays all available actions for that screen.

Screens that display forms are numbered at the left from 1 to 80 (rows or lines) and across the top from 1 to 160 (columns). It is strongly recommended that forms are limited to 80 lines and 132 columns because of printer constraints.

For more information on the use of the screens, please refer to the List Manager Appendix at the end of this manual.

# Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements, responsibilities, or necessary security measures specific to the Automated Information Collection System (AICS) software.

# Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Edit Encounter Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="ClinicSetup" class="anchor"></span>

### Clinic Setup/Edit Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Clinic Setup/Edit Forms option is a form generator used to create and edit encounter forms, and to associate those forms with specific clinics.

When using Group Copy (under Fast Selection Edit) to add a group from one selection list to another, both selection lists must have the same format. If they do not, data will not be displayed properly. Blanks will display for those subcolumns that do not match. The Form Components option can be used to check the selection list format of the groups being copied.

A new action on the Selection List Display Screen, Resequence Group, now allows you to resequence one or more groups within the block, or to resequence the entire block.

You are now asked for Alternative Narrative and Clinical Lexicon. Both Data Entry and Scanning will now pass this data to PCE.

CPT type blocks give the Form Creator the ability to enter a quantity for a CPT code.

More than one Diagnosis code can be passed.

<span id="ICDp7" class="anchor"></span>NOTES for IBD\*3.0\*63 Patch:

- If you are editing Encounter Forms with Lexicon User Filters in place, those filters will be honored <u>with the exception of</u> editing an ICD-9 block or editing an ICD-10 block within the encounter form.  When editing ICD-9 blocks, you will be allowed to choose from any ICD-9 code; and when editing an ICD-10 block, you will be allowed to select any ICD-10 code, regardless of what Lexicon User Filters are in place. User will be prompted for whether they wish to enter Active or Inactive Diagnosis Codes for both Code Sets.
- <span id="p7a" class="anchor"></span>Modifications allow you to add any ICD-10 code regardless of its current status (ACTIVE or INACTIVE), unless the last status of the code is INACTIVE and the effective date has been exceeded.

  
Edit Encounter Forms

> Clinic Setup/Edit FormsNormal Work Flow

![](aics-version-3-user-manual/002.png)

Edit Encounter Forms

> Clinic Setup/Edit Forms

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Screen</strong></th>
<th><strong>Subscreen</strong></th>
<th><strong>Primary Purpose</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1. List of Forms for Clinic</td>
<td></td>
<td><ol>
<li><p>Starting point to associate forms with a clinic</p></li>
<li><p>Choose one form to edit</p></li>
<li><p>Create a form</p></li>
</ol></td>
<td>1</td>
</tr>
<tr class="even">
<td>2. Edit Encounter Form</td>
<td><p>Add Tool Kit Block</p>
<p>Create Block</p>
<p>Edit Block</p></td>
<td><ol start="4">
<li><p>Starting point to edit a form</p></li>
<li><p>Add block</p></li>
<li><p>Move block</p></li>
<li><p>Create blank block</p></li>
<li><p>Edit a list or field on the form (actual contents)</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>3. Editing a Form Block</td>
<td></td>
<td><ol start="9">
<li><p>Add/edit a list</p></li>
<li><p>Add/edit fields for display</p></li>
<li><p>Add/edit lines</p></li>
<li><p>Change block size</p></li>
</ol></td>
<td><p>2</p>
<p>3</p></td>
</tr>
<tr class="even">
<td>4. Edit Selection List</td>
<td><p>Edit Group</p>
<p>Edit Selections</p></td>
<td><ol start="13">
<li><p>Add or edit groups on a list</p></li>
<li><p>Add entries to a group</p></li>
</ol></td>
<td></td>
</tr>
</tbody>
</table>

Tasks/Processes

| Add or change forms associated with a clinic | On List of Forms for Clinic screen, use *Add Form to Setup* or *Delete from Setup.*                                                                                                             |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Easiest way to edit an existing list         | On the List of Forms for Clinic screen, Use *Fast Selection Edit*.                                                                                                                              |
| Make a form scannable                        | On List of Forms for Clinic screen use *Form Name/Descr/Size*. Then, edit the appearance of each list on the Edit a Form Block screen. Marking areas must be bubbles.                           |
| Edit a form                                  | From the Edit Encounter Form screen, you can add, delete, edit, move, or resize blocks.                                                                                                         |
| Create a new form                            | From the List of Forms for Clinic screen you can copy an existing form, create a blank form and add existing tool kit blocks (or design your own blocks).                                       |
| Add predefined blocks                        | On the Edit Encounter Form screen, use *Add Tool Kit Block* or *Copy From Other Form*.                                                                                                          |
| Edit the scanning parameters for a list      | From the Edit Encounter Form screen, use *Edit Block*. Use *List* to edit the list, and then choose appearance.                                                                                 |
| Create a new list                            | On the Editing a Form Block screen, use *List*; or *Fast Selection Edit* on the List of Forms for Clinic screen. First, add your group headers; then for each group, list the items under each. |
| Delete a form                                | On the List of Forms for Clinic screen, *Delete from Setup*, then *Delete Unused Form*.                                                                                                         |

Edit Encounter Forms

> Clinic Setup/Edit FormsExample 1 - List of Forms for Clinic Screen

<u>LIST OF FORMS FOR CLINIC Mar 05, 1997 11:03:11 Page: 1 of 1</u>

FORMS CURRENTLY USED BY 'ORTHOPEDIC' CLINIC

<u>FORM NAME USE & BRIEF DESCRIPTION</u>

1 BASIC FORM Basic Encounter Form

scannable form for ambulatory surgery

2 SUPPLEMENTAL FORM Supplemental Form - All Patients

supplemental form for scanning

<u>Enter ?? for more actions \>\>\></u>

CC Change Clinic CF Copy Form FE Fast Selection Edit

NM Form Name/Descr/Size CR Create Blank Form RC Recompile Form

AS Add Form to Setup DF Delete Unused Form

DS Delete from Setup EF Edit Form

Select Action: Quit//

Edit Encounter Forms

> Clinic Setup/Edit FormsExample 2 - Add/Edit Selection List

\[N\]ew \[A\]ppearance \[D\]elete \[C\]ontents \[P\]osition: C// APP APPEARANCE

NAME: DIAGNOSES// \<RET\>

WHAT TEXT SHOULD APPEAR AT THE TOP OF EACH COLUMN? (OPTIONAL): \<RET\>

SUBCOLUMN HEADER APPEARANCE: ?

R=Reverse Printing

SUBCOLUMN HEADER APPEARANCE: R

HOW SHOULD THE SUBCOLUMNS BE SEPARATED?: \<RET\>

HOW SHOULD THE HEADER FOR EACH GROUP OF ENTRIES APPEAR? CHOOSE FROM {U,B,S,C}:C// \<RET\>

NUMBER OF ADDITIONAL LINES FOR EACH ENTRY ON LIST?: 0// \<RET\>

SHOULD EACH ENTRY ON THE LIST BE UNDERLINED? (YES/NO): NO// \<RET\>

You can now specify the subcolumns the list should contain.

There can be at most 6 subcolumns, numbered 1-6.

Available Data:

1= CODE :7 char 2= DIAGNOSIS :30 char

3= DESCRIPTION :200 char 4= (N/A)

Select SUBCOLUMN NUMBER: 2// 1 HEADER=P CONTENT

=BUBBLE (use for scanning)

SUBCOLUMN NUMBER: 1// \<RET\>

SUBCOLUMN CONTAINS TEXT, OR FOR MARKING? (TEXT/MARKING): MARKING// \<RET\>

TYPE OF MARKING AREA: BUBBLE (use for scanning)// \<RET\>

SELECTION RULE: EXACTLY ONE// \<RET\>

DATA QUALIFIER: PRIMARY// ?

Does one of the qualifiers apply to the choices made in this subcolumn?

Allows only certain data qualifiers, defined in the Package Interface

file.

Answer with AICS DATA QUALIFIERS NAME, or RECOMMENDED HEADER

Do you want the entire AICS DATA QUALIFIERS List? N (No)

DATA QUALIFIER: PRIMARY// \<RET\>

WHAT TEXT SHOULD APPEAR AT THE TOP OF THE SUBCOLUMN?:// \<RET\>

Available Data:

1= CODE :7 char 2= DIAGNOSIS :30 char

3= DESCRIPTION :200 char 4= (N/A)

Select SUBCOLUMN NUMBER:

HOW MANY 'OTHER' DO YOU WANT TO ALLOCATE SPACE FOR?: 2// \<RET\>

WHAT SHOULD SPACE BE ALLOCATED FOR IN 'OTHER'?: NARRATIVE AND CODE// \<RET\>

WHAT DO YOU WANT ENTERED TO THE DATABASE?: CODE ONLY// \<RET\>

... BUILDING THE FORM BLOCK ...

Edit Encounter Forms

> Clinic Setup/Edit FormsExample 3 - Add/Edit Fields for Display

Select Action: Next Screen// DF Data Field

A DISPLAY FIELD outputs data from VISTA, MULTIPLE CHOICE FIELDS

and HAND PRINT FIELDS allow input of data, LABELS are for fixed text fields

Edit fields for: \[D\]isplay, \[M\]ultiple Choice, \[H\]and Print, \[L\]abel only: (D/M/H/L): D// \<RET\>isplay Field

You can Create, Edit, or Delete a data field, Shift all of the data fields

within a range up or down, or List their locations .

\[C\]reate, \[D\]elete, \[E\]dit, \[S\]hift, \[L\]ocations, \[Q\]uit: (C/E/D/S/L/Q): C// ED Edit

1 393 PATIENT NAME

2 393 PATIENT DOB

3 393 PID

4 393 SEX

5 393 ELIGIBILITY

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1 PATIENT NAME

NAME: PATIENT NAME// \<RET\>

Available Data:

1= Patient's Name :30 char 2= (N/A)

Select SUBFIELD LABEL: Patient Name:// \<RET\>

SUBFIELD LABEL: Patient Name:// \<RET\>Edit Encounter Forms

> Clinic Setup/Edit Forms

<u>EDITING A FORM BLOCK Mar 06, 1997 13:09:07 Page: 1 of 2</u>

1 2 3 4 5 6 7

<u>123456789 123456789 123456789 123456789 123456789 123456789 123456789</u>

1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_:

2 \| PATIENT INFORMATION \|:

3 \| \|:

4 \|Patient Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

5 \|DOB: \_\_\_\_\_\_\_\_\_\_\_\_ PID: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Sex: \_ \|:

6 \|Eligibility: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

7 \|Means Test Cat: \_ \|:

8 \|Address: Telephone:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

9 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

10 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

11 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

12 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

13 \| ACTIVE INSURANCE POLICIES \|:

14 \| \|:

<u>15 \| \|:</u>

<u>+ Enter ?? for more actions \>\>\></u>

HOW SHOULD THE LABEL APPEAR? CHOOSE FROM {U,B,R,I}: B //\<RET\>

STARTING ROW FOR LABEL: 4// \<RET\>

STARTING COLUMN FOR LABEL: 2// \<RET\>

LENGTH OF DATA: 30// \<RET\>

STARTING ROW FOR DATA: 4// \<RET\>

STARTING COLUMN FOR DATA: 16// \<RET\>

Available Data:

1= Patient's Name :30 char 2= (N/A)

Select SUBFIELD LABEL: \<RET\>

... BUILDING THE FORM BLOCK ...

Edit Encounter Forms

> Clinic Setup/Edit Forms

123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456

1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_:

2 \| PATIENT INFORMATION \|:

3 \| \|:

4 \|Patient Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

5 \|DOB: \_\_\_\_\_\_\_\_\_\_\_\_ PID: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Sex: \_ \|:

6 \|Eligibility: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

7 \|Means Test Cat: \_ \|:

8 \|Address: Telephone:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

9 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

10 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

11 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

12 \| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|:

13 \| ACTIVE INSURANCE POLICIES \|:

14 \| \|:

<u>15 \| \|:</u>

<u>+ Enter ?? for more actions \>\>\></u>

You can Create, Edit, or Delete a data field, Shift all of the data fields

within a range up or down, or List their locations .

\[C\]reate, \[D\]elete, \[E\]dit, \[S\]hift, \[L\]ocations, \[Q\]uit: (C/E/D/S/L/Q): C//

Edit Encounter Forms

### ### Copy CPT Check-off Sheet to Encounter Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to copy a selected CPT Check-off Sheet's CPT codes to an encounter form.

You are prompted to select the form you are copying the Check-off Sheet to. (The form you select must contain a selection list with CPT codes.) You are then asked to enter the Ambulatory Check-off Sheet name. Once entered, the CPT codes from the selected sheet are added to the form. Any codes already included on the form remain and are not replaced by the new codes.

Example

Select the encounter form you want to copy CPT codes to!

Select a FORM: GENERAL MED scannable form for primary care

Select AMBULATORY CHECK-OFF SHEET NAME: GEN MED

...OK? Yes// \<RET\> (Yes)...

Edit Encounter Forms

### ### Most Commonly used Outpatient CPT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option produces an output that lists the most common Ambulatory Procedures and Ambulatory Surgeries performed in a date range for a given set of clinics (limit 20). It is provided to assist in building CPT Check-off Sheets.

You are prompted to enter one of the following sorts for the selected date range and clinic(s).

CLINIC - provides a count of procedures used, by clinic.

PROCEDURE - provides a total count of all procedures used including the total count used in billing.

PROCEDURE WITH EXTENDED DESCRIPTION - provides the same report as PROCEDURE, and includes a full procedure description.

At multi-divisional sites, this report can also be printed for selected divisions.

Example

Select one of the following:

C CLINIC

P PROCEDURE

D PROCEDURE WITH EXTENDED DESCRIPTION

Sort report by: D PROCEDURE WITH EXTENDED DESCRIPTION

Start with DATE: 1/1 (JAN 01, 1997)

Go to DATE: t (MAR 06, 1997)

Select division: ALL// TROY 500T

Select another division: \<RET\>

Select clinic: ALL// cardIOLOGY BABCOCK,LISA

Select another clinic: \<RET\>

This report requires 132 columns.

OUTPUT DEVICE: HOME// \<RET\> LAT RIGHT MARGIN: 80// 132Edit Encounter FormsMost Commonly used Outpatient CPT Codes

CLINIC CPT USAGE FOR JAN 1,1997 - MAR 6,1997 MAR 06, 1997 13:57 PAGE 1

ALL DIVISIONS AND CLINICS

AMBULATORY PROCEDURE COUNT \#BILLED OPC STATUS CHARGE

-------------------------------------------------------------------------------------------------------------------

00102 ANESTH, REPAIR OF CLEFT LIP 2 2 NATIONALLY ACTIVE

ANESTHESIA FOR PROCEDURES ON INTEGUMENTARY SYSTEM OF HEAD AND/OR

SALIVARY GLANDS, INCLUDING BIOPSY; PLASTIC REPAIR OF CLEFT LIP

00126 ANESTH, TYMPANOTOMY 1 NATIONALLY ACTIVE

ANESTHESIA FOR PROCEDURES ON EXTERNAL, MIDDLE, AND INNER EAR

INCLUDING BIOPSY; TYMPANOTOMY

10040 ACNE SURGERY OF SKIN ABSCESS 12 NATIONALLY ACTIVE

ACNE SURGERY (EG, MARSUPIALIZATION, OPENING OR REMOVAL OF MULTIPLE

MILIA, COMEDONES, CYSTS, PUSTULES)

10060 DRAINAGE OF SKIN ABSCESS 9 NATIONALLY ACTIVE

INCISION AND DRAINAGE OF ABSCESS (EG, CARBUNCLE, SUPPURATIVE

HIDRADENITIS, CUTANEOUS OR SUBCUTANEOUS ABSCESS, CYST, FURUNCLE, OR

PARONYCHIA); SIMPLE OR SINGLE

Enter RETURN to continue or '^' to exit:

## Print Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Print Encounter Forms for Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print an encounter form for appointments either by patient or clinic.

When you choose appointments by clinic, there are three sort options: Division/Clinic/Patient, Division/Terminal Digits, or Division/Clinic/Terminal Digits. You also can print forms for one, many, or all clinics, (for one/many/all divisions - if your site is multi-divisional); and for all patients or add-ons only.

When appointments are selected by patient, you can enter any number of patients individually. Once a patient name is entered, you are prompted to select an

appointment for that patient.

The report can also be printed for individual clinic groups or divisions. If you select a clinic group, you are prompted for additional clinic groups, but not for additional clinics or divisions.

When printing encounter forms, it is important to remember they require a page size of 80 lines and 132 columns.

Print OptionsPrint Encounter Forms for AppointmentsExample

Do you want to print forms for a particular patient or for entire clinics?

Select one of the following:

P Patient

C Clinic

Select Appointment by: Clinic// \<RET\>

Select one of the following:

1 Division/Clinic/Patient Name

2 Division/Terminal Digits

3 Division/Clinic/Terminal Digits

How should the output be SORTED?: 1// \<RET\> Division/Clinic/Patient Name

Appointment Date to Print Forms For: TODAY// \<RET\> (MAR 06, 1997)

Select Print Manager Clinic Group: PRIMARY CARE

Select another Print Manager Clinic Group: \<RET\>

WANT TO PRINT ADD-ONS ONLY? NO// \<RET\>

IS THIS A REPRINT OF A PREVIOUS RUN? NO// \<RET\>

\*\* Encounter Forms require a page size of 80 lines and 132 columns. \*\*

OUTPUT DEVICE: HOME// A138 RIGHT MARGIN: 80// 132Print OptionsPrint Encounter Forms for Appointments

------------------------------------------------- ----------- Clinic: CARDIOLOGY

\|Patient Name: AICSPATIENT,ONE \| \|ALBANY NY\|

\|DOB: JUL 10,1964 PID: 000-45-6789 Sex: M \| ----------- Appt. DT/Time: MAR 06, 1997@09:00

\|Eligibility: NSC \|

\|SC Conditions: SC%: % Means Test Cat: R \|

\| \| Vital Signs:

\| \| WT: \_\_\_\_\_\_\_\_\_\_ BP: \_\_\_\_\_\_\_\_\_\_ T: \_\_\_\_\_\_\_\_\_\_

\| \|

\| \| P: \_\_\_\_\_\_\_\_\_\_ INITIALS/TIME: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\|AO: NO IR: NO POW: NO EC: NO \|

\|Address: Telephone: 518 555-2222 \| <u>\_</u>

\|123 Lake rd \| \| PLEASE CHECK OFF DIAGNOSIS TREATED THIS VISIT \|

\|Anywhere, NEW YORK 12345 \| \| \| \|\| \| \|

\| \| \| <u>CODE \| DIAGNOSIS \|x</u> \|\| <u>CODE DIAGNOSIS \|x</u> \|

\| \| \| <u>\| OTHER \| \|</u>\| <u>\| \|</u> \|

\|Insurance: NO Policy Number: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Marital Status: S \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Employer: Status: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Spouse's Employer: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

------------------------------------------------- \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

<u>\| \|</u>

Progress Notes: ( ) Attached ( ) See Chart

Subjective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Objective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Assessment/Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Plan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Provider Signature

Print Options

### ### Print Form w/Patient Data, No Appt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to print encounter form(s) with patient data. It does not require that an appointment is selected. On forms that show appointment times, the current time (time form is printed) is shown.

You can print a specific encounter form, or the form specified through the Clinic Setup/Edit Forms option for the selected clinic.

Please remember that encounter forms require a page size of 80 lines and 132 columns.

Print OptionsPrint Form w/Patient Data, No ApptExample

\- ----------- Clinic: CARDIOLOGY

\|Patient Name: AICSPATIENT,ONE \| \|ALBANY NY\|

\|DOB: JUL 10,1964 PID: 000-45-6789 Sex: M \| ----------- Appt. DT/Time: NOV 22,\| 1993@09:00

\|Eligibility: NSC \|

\|SC Conditions: SC%: % Means Test Cat: R \|

\| \| Vital Signs:

\| \| WT: \_\_\_\_\_\_\_\_\_\_ BP: \_\_\_\_\_\_\_\_\_\_ T: \_\_\_\_\_\_\_\_\_\_

\| \|

\| \| P: \_\_\_\_\_\_\_\_\_\_ INITIALS/TIME: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\|AO: NO IR: NO POW: NO EC: NO \|

\|Address: Telephone: 518 555-2222 \|

\|123 Lake rd \| \| PLEASE CHECK OFF DIAGNOSIS TREATED THIS VISIT \|

\|Anywhere, NEW YORK 12345 \| \| \|\| \|

\| \| \| <u>CODE \| DIAGNOSIS \|x</u> \|\| <u>CODE \| DIAGNOSIS \|x</u> \|

\| \| \| <u>\| OTHER \| \|</u>\| <u>\| \|</u> \|

\|Insurance: NO Policy Number: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Marital Status: S \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Employer: Status: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\|Spouse's Employer: \| \| <u>\| \| \|</u>\| <u>\| \|</u> \|

<u>\| \|</u> \| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

\| <u>\| \| \|</u>\| <u>\| \|</u> \|

Progress Notes: ( ) Attached ( ) See Chart

Subjective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Objective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Assessment/Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Plan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Provider Signature

Print Options

### ### Print Blank Encounter Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to print a blank form for a selected clinic. Only forms defined as "FORM TO PRINT WITHOUT PATIENT DATA" in the Clinic Setup/Edit Forms option can be printed. These are forms intended for use with patient cards or forms with blank space for handwritten patient data.

Example\| <u>PLACE PATIENT CARD HERE</u> \| Clinic: DERMATOLOGY\| \|\| \| Appt. DT/Time: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\| \|\| \| \|WT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ BP: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ T: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\| \| \| \|\| \| \|P: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ INITIALS/TIME: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\| \|\| \|\| \|\| <u>VISIT (mark one only) x</u> \|\| <u>VISIT (mark one only) x</u> \|\| \|\| <u>NEW PATIENT</u> \|\|<u>Intermediate (21-30 min) \|</u> \|\| \|\|<u>Brief Exam (1-10 min) \|</u> \|\|<u>Extended (31-45 min) \|</u> \|\| \|\|<u>Limited Exam (11-20 min) \|</u> \|\|<u>Comprehensive (46-60+ min) \|</u> \|\| \|\|<u>Intermediate Exam (21-30 min) \|</u> \|\|<u>F/U Brief (1-10 min) \|</u> \|\| \|\|<u>Extended Exam (31-45 min) \|</u> \|\|<u>F/U Limited (11-20 min) \|</u> \|\| \|\|<u>Comprehensive Exam (46-60+ min)\|</u> \|\|<u>F/U Intermediate (21-30 min) \|</u> \|\| \|\| <u>CONSULTATIONS</u> \|\| <u>\|</u> \|\| \|\|<u>Limited (1-20 min) \|</u> \|\| <u>\|</u> \|<u>\|\|</u><u>PLEASE CHECK OFF DIAGNOSIS TREATED THIS VISIT</u>\| \|\| \|\| \|\| <u>CODE DIAGNOSIS x</u> \|\| <u>CODE DIAGNOSIS x</u> \|\| <u>CODE DIAGNOSIS x</u> \|<u>\| OTHER</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|\| <u>\| \|</u> \|<u>PLEASE CHECK PROCEDURES PERFORMED THIS VISIT</u>\| \|\| \|\| \|\|<u>CODE PROCEDURE x</u> \|\|<u>CODE PROCEDURE x</u> \|\|<u>CODE PROCEDURE x</u> \|\|<u>REMOVAL OF SKIN LESION, TRUNK, ARMS OR LEG</u>\|\|<u>11643\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11622\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11400\|BENIGN 0.5 CM OR LESS \|</u> \|\|<u>11644\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11426\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11600\|MALIG. 0.5 CM OR LESS \|</u> \|\|<u>REMOVAL OF SKIN LESION, SCALP, NECK OR HAN</u>\|\|<u>FACE, EARS, EYELIDS, NOSE, LIPS, MUCOUS ME</u>\|\|<u>11401\|BENIGN .06 TO 1.0 CM \|</u> \|\|<u>11420\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11440\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11601\|MALIG. .06 TO 1.0 CM \|</u> \|\|<u>11620\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11640\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11402\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11421\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11441\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11602\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11621\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11641\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11606\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11422\|REMOVAL OF SKIN LESION \|</u> \|\|<u>11442\|REMOVAL OF SKIN LESION \|</u> \|Progress Notes: ( ) Attached ( ) See ChartSubjective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Print OptionsPrint Blank Encounter FormObjective: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Assessment/Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Plan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Was treatment for a SC condition? \_\_ YES \_\_ NO \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Was treatment related to: AO \_\_ IR \_\_ EC \_\_ Provider Signature

## Print Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Division Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is used to print selected reports for a specific division under specified conditions.

Only reports contained in the Package Interface file can be printed. The following reports are included in the file: ACTION PROFILE - 45 DAYS and INFORMATION PROFILE - 45 DAYS (both from the Outpatient Pharmacy package); and ROUTING SLIP (from the Scheduling Package). Other reports can be added to the file; however, only health summary reports can be added by most users. Reports other than health summary can only be added by IRM personnel.

You can choose one of the following conditions for each selected report.

FOR EVERY APPOINTMENT - form will print for every appointment.

ONLY FOR EARLIEST APPOINTMENT - form will print once per patient, even if the patient has multiple appointments. It will print even if it is defined to be excluded through the Edit Clinic Reports option. One form will print for each division.

ONLY IF MULTIPLE APPOINTMENTS - form will print for the earliest appointment for patients with multiple appointments. It will print even if it is defined to be excluded through the Edit Clinic Reports option. One form will print for each division.

Print ManagerEdit Division ReportsExample

You can now select reports that should be printed for the entire division

EDIT REPORTS TO PRINT FOR WHICH DIVISION?: TROY 500T

DIVISION: TROY// \<RET\>

Select REPORT: ACTION PROFILE - 45 DAYS// ROUTING SLIP

ROUTING SLIP TYPE=REPORT

Are you adding 'ROUTING SLIP' as a new REPORT (the 3RD for this PRINT MANAGER DIVISION SETUP)? Y (Yes)

REPORT PRINT CONDITION: ??

Choose FOR EVERY APPOINTMENT if the form should print for every appointment.

Choose ONLY FOR EARLIEST APPOINTMENT if the form should print once per

patient, even if he has multiple appointments

Choose ONLY IF MULTIPLE APPOINTMENTS if the form should print only if the

patient has multiple appointments. If so, it will print only for the

earliest appointment.

The condition under which the report should print.

Choose from:

FOR EVERY APPOINTMENT

ONLY FOR EARLIEST APPOINTMENT

ONLY IF MULTIPLE APPOINTMENTS

REPORT PRINT CONDITION: FOR EVERY APPOINTMENT

PRINT CONDITION: FOR EVERY APPOINTMENT// \<RET\>

SIMPLEX/DUPLEX: DUPLEX,SHORT-EDGE BINDING// \<RET\> DUPLEX,SHORT-EDGE BINDING

Select REPORT:

Print Manager

### ### Edit Clinic Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is used to enter/edit the reports/forms printed for a specific clinic.

BASIC DEFAULT ENCOUNTER FORM - the encounter form that will be printed for every appointment.

SUPPLMNTL FORM - ALL PATIENTS - A supplemental form to be used by all patients of the clinic. A form in this category should not also be in one of the other categories for supplemental forms or it would print twice. You may have up to three supplemental forms for all patients.

SUPPLMNTL FORM - ESTBLSHED PT. - A supplemental form that will print only for patients who have previously been seen in the clinic.

SUPPLMNTL FORM - FIRST VISIT - A supplemental form that will print only for patients who have not previously been seen at the clinic.

FORM W/O PATIENT DATA - The encounter form that should be printed for unscheduled visits. It can have a space in the top left hand corner for imprinting the embossed patient card or writing in patient data.

RESERVED FOR FUTURE USE - This category was created to store new forms that have not yet been completed. Forms entered here are not printed.

DON'T USE PCMM PROVIDERS - AICS defaults to printing providers specified in PCMM, if defined; otherwise, providers from the clinic setup are used. If YES is entered, AICS prints the providers from clinic setup regardless of PCMM.

Select REPORT - Reports that should be printed for the clinic in addition to the encounter forms that have been selected. Only reports contained in the Package Interface file can be selected at this prompt.

Select EXCLUDED REPORT - Reports that you do not want to print for this clinic. Entering a report as an excluded report will prevent it from printing even if it is defined to print for every appointment for the division through the Edit Division Reports option. Reports defined through the Edit Division Reports option as printing only earliest appointment or only if multiple appointments will not be excluded from printing for the first clinic.

Print ManagerEdit Clinic ReportsExample

EDIT REPORTS TO PRINT FOR WHICH CLINIC?: ORTHOPEDIC

CLINIC: ORTHOPEDIC// \<RET\>

BASIC DEFAULT ENCOUNTER FORM: ORTHO CLINIC// \<RET\>

SUPPLMNTL FORM \#1 ALL PATIENTS: PRIMARY CARE scannable form for primary care

SUPPLMNTL FORM \#2 ALL PATIENTS: \<RET\>

SUPPLMNTL FORM \#3 ALL PATIENTS: \<RET\>

SUPPLMNTL FORM - ESTBLSHED PT.: \<RET\>

SUPPLMNTL FORM - FIRST VISIT: \<RET\>

FORM W/O PATIENT DATA: \<RET\>

RESERVED FOR FUTURE USE: \<RET\>

DON'T USE PCMM PROVIDERS: \<RET\>

You can now select reports that should be printed for the clinic

IN ADDITION to the encounter forms that have been selected.

Select REPORT: ROUTING SLIP

ROUTING SLIP TYPE=REPORT

Are you adding 'ROUTING SLIP' as a new REPORT (the 1ST for this PRINT MANAGER CLINIC SETUP)? Y (Yes)

SIMPLEX/DUPLEX: DUPLEX,SHORT-EDGE BINDING// \<RET\> DUPLEX,SHORT-EDGE BINDING

Select REPORT:

Print Manager

### ### Define Available Health Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows a Health Summary to be made available for use by the print manager. The Health Summary selected must have been created through the Health Summary package prior to defining it to the print manager.

You are prompted to enter the name of the health summary you wish to define. You may enter a list of words with which to index this interface. You will then be able to look up this interface by entering any word you have entered. Each word should be at least three characters in length and words must be separated by a space. The purpose of this field is to assist you in locating the package interface you need to display a particular item of data to a form.

You can also set the interface to YES if available, NO if it is not. Interfaces that are not available are not called.

Example

You can now edit the Health Summaries available through the print manager.

Select a Health Summary defined to the print manager: LAB RESULTS

Are you adding 'LAB RESULTS' as a new PACKAGE INTERFACE? Y (Yes)

PACKAGE INTERFACE ACTION TYPE: PRINT REP PRINT REPORT

NAME: LAB RESULTS// \<RET\>

DESCRIPTION:

1\>This health summary prints lab results for patients for the last

2\>three months.

3\>

EDIT Option: \<RET\>

USER LOOKUP: LAB 90 DAYS

TYPE OF HEALTH SUMMARY: SAMPLE 1

AVAILABLE? (Y/N): Y YES

Print Manager

### ### Report Clinic Setups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# This option provides a report, by division that lists each clinic setup and the encounter forms and other reports defined for use by that clinic. For clinics with reports defined, the condition on which the report is printed is also provided.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AICS Print Manager Clinic Setup Report Mar 06, 1997@16:14:43 PAGE 1

For Division: ALBANY

------------------------------------------------------------------------------

Division: ALBANY

Clinic: DENTAL

BASIC DEFAULT FORM: ..........................32X-DENTAL

Clinic: DERMATOLOGY

BASIC DEFAULT FORM: ..........................BILOXI.AICS

FORM WITH NO PRE-PRINTED PATIENT DATA: .......BILOXI.AICS

SUPPLEMENTAL FORM - PATIENT WITH PRIOR VISITS: BILOXI.AICS II

RESERVED FOR FUTURE USE: .....................BILOXI.AICS III

REPORTS PRINT CONDITION

======= ===============

ACTION PROFILE - 45 DAYS FOR EVERY APPOINTMENT

ACTION PROFILE - 45 DAYS FOR EVERY APPOINTMENT

Clinic: EF TEST

BASIC DEFAULT FORM: ..........................PRIMARY CARE

Enter RETURN to continue or '^' to exit:

Print Manager

### ### Setup Automatic Print Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# This option allows you to enter Print Manager queuing parameters and to specify automatic queuing parameters.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The wild card, \*, can now be used when entering clinics to clinic groups.

Normal Work Flow

![](aics-version-3-user-manual/003.png)

Print ManagerSetup Automatic Print Queues

# Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Print Mgrs. Queuing Params. Mar 06, 1997 16:15:40 Page: 1 of 1</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the list of Print Manager's Queuing Parameters (PMQP) for your facility

You may enter new ones or edit those already set up.

There are no PARAMETER GROUPS listed.

<u>Enter ?? for more actions</u>

EP Edit Parameter Grp. PF Print Forms One Group DG Delete Param Grp

AP Add Parameter Grp. HL Special Instruc Help EX Exit

JP Jump to Param. Grp. QS Queue Status

CG Clinic Group Menu TI Task Interupt

Select Action: Quit// AP

# # Select Print Mgrs. Queuing Params. Name: NEW GROUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CLINIC SORT BY: DIVISION/CLINIC/PATIENT// \<RET\>

ADD ONS: NO// \<RET\>

CLINIC GROUPS: ??

This field is a pointer to the PRINT MANAGERS CLINIC GROUPS file

(#357.99). This stores the name of the clinic group that the

encounter forms should be printed for. Each Clinic Group has one

or more clinics assigned to it.

Choose from:

PRIMARY CARE A

PRIMARY CARE B

PRIMARY CARE C

CLINIC GROUPS: PRIMARY CARE A

DAYS TO PRINT AHEAD: 3

SPECIAL INSTRUCTIONS: R// ?

Choose from:

R RUN REGARDLESS

I IGNORE BOTH WEEKENDS AND HOLIDAYS

W IGNORE WEEKENDS

H IGNORE HOLIDAYS

T TODAY

N NOT ACTIVE

SPECIAL INSTRUCTIONS: R// \<RET\> RUN REGARDLESS

DEVICE: HP LASER// ??

This field contains a free text pointer to the device. This stores the

name of the printer where the encounter forms should be printed for

the print job.

DEVICE: HP LASER// \<RET\>Print ManagerSetup Automatic Print Queues

# PRINT PRIORITY: 1// ??

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains a number which will be used to sequence the print

job tasks. The lower the number, the higher the priority of the job

and those will be queued to print first.

PRINT PRIORITY: 1// \<RET\>

TIME QUEUED: 1330//\<RET\>

Print Mgrs. Queuing Params. Mar 06, 1997 16:19:32 Page: 1 of 1

This is the list of Print Manager's Queuing Parameters (PMQP) for your facility

You may enter new ones or edit those already set up.

1\) NEW GROUP

Starting Date/Time: Days To Print Ahead: 3

Ending Date/Time: Add Ons Only: NO

Clinic Groups: PRIMARY CARE A Last Date Printed:

Sort By: Div/Clin/Patient Print Priority: 1

Special Instructions: Run Regardless Device/Time Queued: Hp Laser @1330

Enter ?? for more actions

EP Edit Parameter Grp. PF Print Forms One Group DG Delete Param Grp

AP Add Parameter Grp. HL Special Instruc Help EX Exit

JP Jump to Param. Grp. QS Queue Status

CG Clinic Group Menu TI Task Interupt

Select Action: Quit//

## Edit Tool Kit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Edit Tool Kit Blocks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

To help you to create customized forms, a tool kit is provided which contains template forms and blocks that can be copied and edited to create new forms/blocks. The Edit Tool Kit Blocks option is used to create, edit, or delete tool kit blocks. (Please refer to the Edit Tool Kit Forms option to edit, create, or delete forms.)

Five new tool kit blocks have been added: Practitioner, Hidden Classifications, Patient Immunizations, Eye Art I, and Eye Art II.

Normal Work Flow

![](aics-version-3-user-manual/004.png)

Edit Tool KitEdit Tool Kit BlocksScreen Descriptions

<u>Edit Tool Kit Blocks Screen</u>

This screen lists the blocks available in the tool kit with a brief description. You can create, edit, copy, change the order of, and delete the blocks.

<u>Editing a Form Block Screen</u>

This screen is accessed through the *Edit Block* action on the Edit Tool Kit Block screen. The block is displayed as nearly as possible to how it will appear on paper. You can edit the block's contents, appearance, and description.

<u>Edit Selection List Screen</u>

This screen is accessed by choosing to edit a list's contents through the *Selection List* action on the Editing a Form Block screen. It displays the selection groups defined for the selection list, with the header text and the print orders, and allows you to edit the contents of the list. A selection group is a group of selections with a header and a defined print order. A selection list is made up of one or more selection groups. To edit individual selections, a group must be selected. A group is a named collection of items on the list.

<u>Edit Group's Selections Screen</u>

This screen is accessed through the *Group's Contents* action on the Edit Selection List screen. It displays the selections appearing under the group, showing the text appearing on the form and the print order of the selections within the group. It allows you to edit selections on the list. A selection is just one item on the list, usually selected from a table, such as the table of ICD-9 Diagnosis Codes or ICD-10 <span id="p35" class="anchor"></span>Diagnosis Codes.

Please refer to the Clinic Setup/Edit Forms option for additional documentation.

Edit Tool Kit

### ### Edit Tool Kit Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To help you to create customized forms, a tool kit is provided with the AICS software which contains template forms and blocks that can be copied and edited to create new forms/blocks. The Edit Tool Kit Forms option is used to create, copy, edit, print, and delete these template forms. (Please refer to the Edit Tool Kit Blocks option documentation.)

Normal Work Flow

![](aics-version-3-user-manual/005.png)

Edit Tool KitEdit Tool Kit FormsScreen Descriptions

<u>List of Tool Kit Forms</u>

This screen lists all forms currently contained in the tool kit with a brief description of each form. You can create, copy, edit, and delete the forms.

<u>Edit Encounter Form Screen</u>

This screen is accessed through the *Edit Form* action on the List of Tool Kit Forms screen. You are first asked to select which form you wish to edit. The Edit Encounter Form screen then displays the selected form for editing.

<u>List of Tool Kit Blocks Screen</u>

This screen is accessed through the *Add Tool Kit Block* action on the Edit Encounter Form screen. It displays a list of the available tool kit blocks for selection.

<u>View Tool Kit Block Screen</u>

This screen is accessed through the Select Tool Kit Block action on the List of Tool Kit Blocks screen. It is for viewing only.

<u>Editing a Form Block Screen</u>

This screen is accessed through the *Edit Block* action on the Edit Encounter Form screen. The block is displayed as nearly as possible to how it will appear on paper. You can edit the block's contents, appearance and description.

<u>Edit Selection List Screen</u>

This screen is accessed by choosing to edit a list's contents through the *Selection List* action on the Editing a Form Block screen. It displays the selection groups defined for the selection list, with the header text and the print orders, and allows you to edit the contents of the list. A selection group is a group of selections with a header and a defined print order. A selection list is made up of one or more selection groups. To edit individual selections, a group must be selected. A group is a named collection of items on the list.

<u>  
</u>Edit Tool KitEdit Tool Kit Forms

<u>Edit Group's Selections Screen</u>

This screen is accessed through the *Group's Contents* action on the Edit Selection List screen. It displays the selections appearing under the group, showing the text appearing on the form and the print order of the selections within the group. It allows you to edit selections on the list. A selection is just one item on the list, usually selected from a table, such as the table of ICD-9 Diagnosis Codes or ICD-10 <span id="ICDp38" class="anchor"></span>Diagnosis Codes.

Please refer to the Clinic Setup/Edit Forms option for additional documentation.

## Encounter Form IRM Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Edit Package Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the IBDF IRM security key.

This option allows package interfaces to be created, edited, and deleted; however, package interfaces that are in use in any form should not be deleted. The option only allows selection routines and output routines, which are defined as follows:

OUTPUT Routines that are used to obtain data from other packages that will be displayed to DATA FIELDS. Output routines fill in the data on an encounter form (e.g., name, DOB, etc.). The data is not stored with the form, but instead is obtained at the time the form is printed.

SELECTION Routines that are used to obtain data from other packages that will be displayed to SELECTION LISTS. Selection routines select data from a table (e.g., CPT, DX, etc.) and fill in the form with codes. The data is stored with the form.

There is a new package interface, DG 1010F PRINT, which will print a 1010F with the encounter form if a new Means Test or Copay Test is due within the number of days specified in the AICS parameters (the default is 30).

The following documentation provides instructions to help you write your own package interfaces to obtain data not available through the Tool Kit.

Step 1 - Write a routine to obtain the data. Output routines must write the data to the ^TMP global in the following format:

<u>Single Value</u> (a string without pieces):

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>)=data

<u>Record</u> (a set of strings concatenated together with "^" separating the pieces):

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>)=piece1^piece2^...

> **NOTE:** You can enter a maximum of seven pieces of data. The string must be less than 256 characters long.

<u>  
</u>Encounter Form IRM Options

> Edit Package Interface

<u>List of Single Values</u> (an indefinite number of values, each numbered, each containing the same type of information):

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,1)=value 1

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,2)=value 2

etc.

<u>List of Records</u> (an indefinite number of values, each numbered, each containing the same type of information):

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,1)=piece1^piece2^...

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,2)=piece1^piece2^...

etc.

> **NOTE:** You can enter a maximum of seven pieces of data.

<u>Word Processing</u> (data in VA FileMan format):

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,1,0)=line 1

^TMP("IB",\$J,"INTERFACES",+\$G(DFN),\<interface name\>,2,0)=line 2

etc.

Where piece 1 must be an identifier for the selection and the other pieces are other fields returned for the selection. A SELECTION routine must write the data returned to the ^TMP global in the following format.

^TMP ("IB",\$J,"INTERFACES",\<interface name\>)^piece1^piece2^piece3...

For the DG SELECT CPT PROCEDURE CODES interface, the returned data is in the following format.

^TMP("IB",\$J"INTERFACES","DG SELECT PROCEDURE CODES")=\<CPT CODE\>^\<short name\>^\<Description\>.

Step 2 - Add an entry to the package interface file (#357.6). At the "Select a PACKAGE INTERFACE:" and "NAME:" prompts, enter the name of the package interface you are creating. For output type interfaces, i.e., interfaces returning data for data fields, the name must be preceded with the namespace of the package providing the data.

Encounter Form IRM Options

> Edit Package Interface

The subsequent prompts you encounter while using this option will vary depending on whether your response to the "SELECT THE TYPE OF PACKAGE INTERFACE TO EDIT:" prompt is "OUTPUT" or "SELECTION". (Please refer to the definitions on the previous page.) Table 1, which follows this introduction, provides a brief overview of the prompts used with this option and possible responses. Also provided is a column which indicates whether the prompt will appear for output routines, selection routines, or both.

When responding to the "Select PROTECTED LOCAL VARIABLES:" and "Select REQUIRED LOCAL VARIABLE:" prompts, it is very important that you consider the following:

The interface routine will not be called unless all of the required variables are defined.

It is safe to assume that the following variables are defined. Calling a package interface must leave them defined. They should be left unchanged after leaving the exit action from the package interface.

DFN = ien of the patient in the PATIENT file (#2)

IBCLINIC = ien of the clinic in the HOSPITAL LOCATION file (#44)

IBAPPT = Appointment date/time in VA FileMan format

Use of the Edit Package Interface option performs the following actions:

Checks for required variables

"News" protected variables

Does entry action

Calls the specified entry point

Does exit action

Encounter Form IRM Options

> Edit Package InterfaceTable 1 - Prompts used with the Edit Package Interface option

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 54%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Prompt</strong></th>
<th><strong>Possible Response(s)</strong></th>
<th><strong>Output, Selection, or Both</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*SELECT THE TYPE OF PACKAGE INTERFACE TO EDIT:</td>
<td>1, 2, Output, Selection, or up-arrow &lt;^&gt;</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*Select a PACKAGE INTERFACE:</td>
<td>&lt;RET&gt;, up-arrow &lt;^&gt;, package interface name</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>Are you sure this is the right type of data?:</td>
<td>Yes, No, &lt;RET&gt;, up-arrow &lt;^&gt;</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*NAME:</td>
<td>&lt;RET&gt;, up-arrow &lt;^&gt;, name of the interface you are writing, prefixed by the namespace of the package that is providing the data</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>DESCRIPTION:</td>
<td>Free text entry of pertinent information. Should advise the user of the data contained/returned. You will be given the opportunity to edit this information before proceeding to the next prompt.</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*WHAT FORMAT WILL THE DATA BE IN?:</td>
<td><p>SINGLE VALUE - A string without pieces.</p>
<p>RECORD - A set of strings concatenated together with "^" separating</p>
<p>the pieces.</p>
<p>LIST OF SINGLE VALUES - An indefinite number of values, each</p>
<p>numbered, each containing the same type of information.</p>
<p>LIST OF RECORDS - An indefinite number of values, each numbered,</p>
<p>each containing the same type of information.</p>
<p>WORD PROCESSING - Data in VA FileMan format.</p></td>
<td>Output only</td>
</tr>
<tr class="odd">
<td>*LIST OF WORDS TO MAKE LOOK-UPS EASIER:</td>
<td>List of words with which you wish to index the interface.</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*CUSTODIAL PACKAGE:</td>
<td>Free text pointer to the package file (#9.4).</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>*ROUTINE:</td>
<td>The routine that should be called.</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*ENTRY POINT:</td>
<td>The entry point in the routine that should be called.</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>*Select PROTECTED LOCAL VARIABLES:</td>
<td>A list of variables that should be "newed" before the entry action or calling the interface.</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*Select REQUIRED LOCAL VARIABLE:</td>
<td>A variable that is required input to the interface routine. The interface routine will not be called unless all of the required variables are defined.</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>*AVAILABLE? (Y/N): YES//</td>
<td><p>0 NO</p>
<p>1 YES</p>
<p>&lt;RET&gt; or up-arrow &lt;^&gt;</p>
<p>This field should be set to YES if the interface is available; NO if it is not available. Interfaces that are not available are not called.</p></td>
<td>Both</td>
</tr>
<tr class="even">
<td>*WHAT IS THE FIRST PIECE OF DATA RETURNED BY THE INTERFACE?:</td>
<td>Free text entry that should be a descriptive name of the first field in the record returned by the interface. This prompt will repeat as second piece, third piece, etc., for up to a maximum of seven pieces.</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>*WHAT IS ITS MAXIMUM LENGTH?:</td>
<td>The maximum length (number of characters) of the applicable field of the record returned by the interface routine.</td>
<td>Both</td>
</tr>
<tr class="even">
<td>*CAN THIS FIELD BE DISPLAYED TO THE USER?: YES//</td>
<td><p>0 NO</p>
<p>1 YES</p>
<p>&lt;RET&gt; or up-arrow &lt;^&gt;</p>
<p>If NO, the value cannot be displayed to the encounter form. The first piece is reserved for the unique id of the selection.</p></td>
<td>Selection only</td>
</tr>
<tr class="odd">
<td>*ARE SELECTIONS EXPORTABLE?: YES//</td>
<td><p>0 NO</p>
<p>1 YES</p>
<p>&lt;RET&gt; or up-arrow &lt;^&gt;</p>
<p>Determines whether selections appearing on selection lists that are populated via the package interface will be exported along with the form on which they appear. The Import/Export Utility will not resolve pointers, so if the id returned by the package interface (piece 1) is a pointer that differs between sites, this field should contain NO.</p></td>
<td>Selection only</td>
</tr>
</tbody>
</table>

\*Entering an up-arrow \<^\> will return you to the menu.

> **NOTE:** Entering \<?\> or \<??\> at any prompt will activate on-line help.

Encounter Form IRM Options

> Edit Package InterfaceExample

You can write your own Package Interfaces to obtain data not available

through the Toolkit. Before you do so, however, please consult the technical

documentation for the guidelines that must be followed. In particular, you

must know where the data should be placed and what format must be used.

Press RETURN to continue...\<RET\>

OUTPUT interfaces are used to obtain data from other packages that will be

displayed to DATA FIELDS.

SELECTION interfaces are used to obtain data from other packages that will be

displayed to SELECTION LISTS.

Select one of the following:

1 OUTPUT

2 SELECTION

SELECT THE TYPE OF PACKAGE INTERFACE TO EDIT: 1// \<RET\> OUTPUT

Select a PACKAGE INTERFACE: DPT NUMBER OF CHILDREN

Are you adding 'DPT NUMBER OF CHILDREN' as

a new PACKAGE INTERFACE? Y (Yes)

You must prefix the name with the name space of the package that is providing

the data.

NAME: DPT NUMBER OF CHILDREN Replace \<RET\>

DESCRIPTION:

1\>For displaying the number of children dependent on the patient.

2\>

EDIT Option: \<RET\>

WHAT FORMAT WILL THE DATA BE IN?: ?

What format will the data be in?

Choose from:

1 SINGLE VALUE

2 RECORD

3 LIST OF SINGLE VALUES

4 LIST OF RECORDS

5 WORD PROCESSING

WHAT FORMAT WILL THE DATA BE IN?: 1 SINGLE VALUE

You can enter a list of words with which to index this interface. You will

then be able to look up this interface by entering any word on the list.

Each word should be at least 3 characters long, and words must be separated

by a space.

Encounter Form IRM Options

> Edit Package Interface

LIST OF WORDS TO MAKE LOOK-UPS EASIER: CHILDREN DEPENDENTS NUMBER

CUSTODIAL PACKAGE: PATIENT FILE

ROUTINE: IBDFN11

ENTRY POINT: CHILDREN

Select PROTECTED LOCAL VARIABLES: DFN

Are you adding 'DFN' as a new PROTECTED LOCAL VARIABLES (the 1ST for this PACKAGE INTERFACE)? Y (Yes)

Select PROTECTED LOCAL VARIABLES: \<RET\>

Select REQUIRED LOCAL VARIABLE: IBCLINIC

Are you adding 'IBCLINIC' as a new REQUIRED LOCAL VARIABLE (the 1ST for this PACKAGE INTERFACE)? Y (Yes)

Select REQUIRED LOCAL VARIABLE: \<RET\>

AVAILABLE? (Y/N): Y YES

WHAT IS THE FIRST PIECE OF DATA RETURNED BY THE INTERFACE?: NUMBER OF DEPENDENT CHILDREN

WHAT IS ITS MAXIMUM LENGTH?: 2Encounter Form IRM Options

### ### Edit Marking Area (for selection lists)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the IBDF IRM security key.

This option allows the local sites to add, edit, or delete their own Marking Areas (the areas on a selection list that the user marks to indicate selections from the list, e.g., ( ), \[ \], { }) to change the look of the form. The option is screened by the tool kit field so users can only add or edit their own Marking Areas.

The following three prompts are used with this option:

"Select MARKING AREA TYPE NAME:"

Your response should describe the Marking Area as it will appear on the form (e.g., "brackets" if { } will appear on the form).

"NAME:"

This prompt allows you to accept, edit, or delete a Marking Area. Your response to the "Select MARKING AREA TYPE NAME:" prompt will appear as a default value. Press \<RET\> to accept the default. To edit the name of a Marking Area, enter the correct name at this prompt. Enter an at-sign \<@\> to delete the default value. You will be asked if you are sure you want to delete the Marking Area. A "YES" response will delete the Marking Area and return you to the menu. A "NO" response will cause the prompt to repeat. An up-arrow \<^\> entered at this prompt will return you to the menu.

"DISPLAY STRING:"

Enter the characters that should be printed on the form, including spaces, up to a maximum of twenty characters. The message, "New marking area created!" will appear on the screen, and you will be returned to the menu. This prompt will not appear if you deleted the Marking Area at the "NAME:" prompt. This prompt requires a response. Pressing \<RET\> will repeat the prompt until you enter a response. Entering an up-arrow \<^\> at this prompt will return you to the menu, and will cancel your attempt to create a new Marking Area.

Encounter Form IRM Options

> Edit Marking Area (for selection lists)Example

You can create your own MARKING AREAS to supplement those that come with the

toolkit. Marking areas are the areas on a selection list that the user

marks to indicate selections from the list.

Press RETURN to continue...\<RET\>

Select MARKING AREA TYPE NAME: SLASHES

Are you adding 'SLASHES' as a new MARKING AREA TYPE? Y (Yes)

NAME: SLASHES// \<RET\>

Enter the characters that should be printed on the form, including spaces.

DISPLAY STRING: / /

New marking area created!

Encounter Form IRM Options

### ### Define Available Report (not Health Summaries)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is locked with the IBDF IRM security key.

This option allows you to define the reports available through the Print Manager. Reports do not have to be namespaced. Care must be taken when defining reports to the Print Manager. Please follow these rules:

1\. Entry points must involve no user interaction.

2\. The device must not be changed or closed.

3\. Local variables should be the same on exit as on entry.

4\. Assume that the device is already at the top of the form, so there are no form feeds at the beginning.

5\. There should be a form feed after the report prints.

The following variables are available, and should not be changed after exit action from the package interface:

DFN = ien of the patient in the PATIENT file (#2)

IBCLINIC = ien of the clinic in the HOSPITAL LOCATION file (#44)

IBAPPT = Appointment date/time in VA FileMan format

The following prompts are used with this option:

"Select a report defined to the print manager:""NAME:"

Your response to both of these prompts should be the name of the package interface. Your response to "Select a report defined to the print manager:" will appear as the default value at the "NAME:" prompt, where you will be able to edit or delete the entry.

"DESCRIPTION:"

This prompt allows you to enter a free text description of the report.

Encounter Form IRM Options

> Define Available Report (not Health Summaries)"USER LOOKUP:"

This is the same as the "LIST OF WORDS TO MAKE LOOK-UPS EASIER:" prompt in the Edit Package Interface option. Enter a word or list of words with which you wish to index the package interface to facilitate lookup. Each word should be at least three characters long, and multiple words must be separated by a space. This field is used to create a KWIC index for this file in order to assist the user in locating the package interface that will display a particular item of data to a form.

"CUSTODIAL PACKAGE:"

This is a free text pointer to the package file (#9.4).

"ENTRY POINT:"

Your response should be the entry point in the routine that should be called.

"ROUTINE:"

Your response should be the routine that should be called.

"Select PROTECTED LOCAL VARIABLES:"

You can define a list of variables (without subscripts) that should be "newed" before the entry action or calling the interface.

"Select REQUIRED LOCAL VARIABLE:"

You can define a list of variables which are required input to the interface routine. The Print Manager will not call the entry point in the interface routine unless all of the required variables are defined.

"AVAILABLE? (Y/N):"

This field should be set to YES if the interface is available, NO if it is not available. Interfaces that are not available are not called. The Print Manager will not print the report unless this is set to YES.

Encounter Form IRM Options

> Define Available Report (not Health Summaries)Example

You can now edit the reports available through the print manager.

Care must be taken when defining reports to the Print Manager. Please

Enter RETURN to continue or '^' to exit: \<RET\>

follow these rules:

1\) Entry points must involve no user interaction.

2\) The device must not be changed or closed.

3\) Local variables should be the same on exit as on entry.

THESE VARIABLES ARE AVAILABLE:

DFN = ien of patient in the PATIENT file

IBCLINIC = ien of clinic in the HOSPTIAL LOCATION file

IBAPPT = appointment date/time in FM format

FEATURES OF INTEREST, IN THE ORDER PERFORMED BY THE PRINT MANAGER:

AVAILABLE?: The Print Manager will not print the report unless

this is set to YES.

REQUIRED VARIABLES: You can define a list of variables that should

be defined. The Print Manager won't call the entry point unless

they are defined.

Enter RETURN to continue or '^' to exit: \<RET\>

PROTECTED VARIABLES: You can define a list of variables (without

subscripts) that should be NEWed.

ENTRY ACTION: Mumps code that should be Xecuted before calling

the entry point.

EXIT ACTION: Mumps code that should be Xecuted after calling

the entry point.

EXAMPLE: Supposing the entry point kills DFN. You could do this:

REQUIRED VARIABLE: DFN

PROTECTED VARIABLE: IBDFN

ENTRY ACTION: S IBDFN=DFN

EXIT ACTION: S DFN=IBDFN

Encounter Form IRM Options

> Define Available Report (not Health Summaries)

Select a report defined to the print manager: ACTION PROFILE - 45 DAYS

ACTION PROFILE - 45 DAYS TYPE=REPORT

NAME: ACTION PROFILE - 45 DAYS Replace \<RET\>

DESCRIPTION:

1\>The Action Profile from Outpatient Pharmacy. The medicine profile is

2\>printed for the last 45 days.

EDIT Option: \<RET\>

USER LOOKUP: OUTPATIENT PHARMACY ACTION PROFILE Replace \<RET\>

CUSTODIAL PACKAGE: OUTPATIENT PHARMACY// \<RET\>

ENTRY POINT: RXPROF// \<RET\>

ROUTINE: IBDFN3// \<RET\>

ENTRY ACTION: S PSTYPE=1,PSDAYS=45 Replace \<RET\>

EXIT ACTION: \<RET\>

Select PROTECTED LOCAL VARIABLES: PSDAYS// \<RET\>

Select REQUIRED LOCAL VARIABLE: DFN// \<RET\>

AVAILABLE? (Y/N): YES//\<RET\>Encounter Form IRM Options

### ### Import/Export Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is locked with the IBDF IRM security key.

This option allows forms and Tool Kit blocks to be transferred between sites. The initial install of the Encounter Form Utilities at your site included a Tool Kit of forms and blocks that must be imported using this utility. The only safe method for transferring additional forms and blocks between sites is through this option.

The Import/Export Utility includes a set of files (#358 through \#358.98) that are nearly identical to the files used by AICS (#357 through \#357.94) to store form descriptions. These import/export files are a workspace in which forms and blocks can be safely exported to other sites, and imported from other sites to your own.

You should have a package entry for the Import/Export Utility already set up. The files listed should be in the \#358 to \#358.98 range. The package entry is named IB ENCOUNTER FORM IMP/EXP, and the prefix is IBDE. The package entry is necessary to export.

You should follow these steps when IMPORTING:

1\. Make sure the other site has prepared a set of inits, using this utility, that contain the forms and Tool Kit blocks they want to transfer.

2\. Make sure your workspace does not contain any forms or blocks that you want to keep, then clear the workspace using the Clear Work Space action. NOTE: Anything remaining in the workspace will be lost when you use the Clear Work Space action.

3\. Execute the inits using the Run Inits action. The init should normally be named IBDEINIT.

4\. The workspace should now contain forms and tool kit blocks from which you can choose which ones you want. Use the IMPORT ENTRY action to actually make the form or block available for use. The forms cannot be viewed while in the workspace, but you can view the IMPORT/EXP NOTES.

Encounter Form IRM OptionsImport/Export Utility

(Using the IMPORT ENTRY action copies the form from the 358 series of files at the remote site to the 357 series of files at your site.) You must import each item separately.

5\. Change the name of the form or tool kit block if that block already exists at your site.

You should follow these steps when EXPORTING:

> **NOTE:** Only users with PROGRAMMER ACCESS can export.

1\. Clear the workspace of anything you do not want to export.

2\. Add any forms or blocks to the workspace that you do want to export.

3\. Add Import/Export Notes for each entry you add to the workspace, accurately describing the form or block for the site to which you are exporting. (The receiving site will be able to view the notes, but they will not be able to view the form itself until they import it.)

4\. Create the inits that will be sent to the other site using the DIFROM action.

5\. Send the inits to the other site.

Table 2 - List Manager Actions Used with the Import/Export Utility option

| Synonym | Name           | Description                                                                          |
|-------------|--------------------|------------------------------------------------------------------------------------------|
| HE          | Help               | Provides on-line instructions for importing and exporting.                               |
| DE          | Delete Entry       | Deletes an entry from your workspace.                                                    |
| DI          | DIFROM             | Calls the VA FileMan utility.                                                            |
| LF          | List Forms         | Lists forms in the workspace.                                                            |
| AE          | Add Entry          | Adds an entry to your workspace.                                                         |
| RI          | Run Inits          | Runs inits obtained from the site that is exporting the data.                            |
| IE          | Import Entry       | Imports a form or block to your site from the workspace.                                 |
| VI          | View Imp/Exp Notes | Allows you to view descriptions of forms and blocks that are in your workspace.          |
| CW          | Clear Work Space   | Clears your workspace. Any items in the workspace when this action is used will be lost. |
| EI          | Edit Imp/Exp Notes | Allows you to edit import/export notes written by you.                                   |

Encounter Form IRM Options

> Import/Export UtilityExample 1 - Exporting a Form

<u>Import/Export Work Space Mar 07, 1997 10:57:06 Page: 1 of 1</u>

LIST OF FORMS READY FOR IMPORT OR EXPORT

(\*\* there are also toolkit blocks in the work space \*\*)

<u>FORM NAME USE & BRIEF DESCRIPTION</u>

1 DEFAULTS selection list defaults - DO NOT DELETE

<u>Enter ?? for more actions \>\>\></u>

HE Help DE Delete Entry DI DIFROM

LB List TK Blocks AE Add Entry RI Run Inits

IE Import Entry VI View Imp/Exp Notes

CW Clear Work Space EI Edit Imp/Exp Notes

Select Action: Quit// AE

Do you want to select a form from the toolkit? YES

Select a FORM: ??

Choose from:

AMBULATORY SURGERY SAMPLE V2.1 scannable form for ambulatory surgery

EMERGENCY SERVICES SAMPLE V2.1 scannable form for primary care

PRIMARY CARE SAMPLE V2.1 scannable form for primary care

Select a FORM: PRIMARY CARE SAMPLE V2.1 scannable form for primary care

............

EXPORT NOTES:

1\>Contains CPT codes, Dx codes, demographics, and SOAP.

2\>\<RET\>

EDIT Option: \<RET\>Encounter Form IRM Options

> Import/Export Utility

Select Action: Quit// DI DIFROM

===================================================================

You must enter these parameters to the prompts generated by DIFROM:

===================================================================

Enter the Name of the Package (2-4 characters): IBDE

I am going to create a routine called 'IBDEINIT'.

but 'IBDEINIT' is ALREADY ON FILE!

Is that OK? YES

Would you like to include Data Dictionaries? YES// \<RET\> YES

Would you like to see the package definition? NO// \<RET\> NO

Do you want to accept the current definition? NO// \<RET\> YES

===================================================================

{now DIFROM lists the files.....}

===================================================================

Now you must enter the information that goes on the second line

of the INIT routines.

Enter RETURN to continue or '^' to exit: \<RET\>

Select VERSION: 3.0// \<RET\>

DATE DISTRIBUTED: AUG 3,1993// TODAY

Would you like to include OPTIONS? YES// NO

Would you like to include BULLETINS? YES// NO

Would you like to include SECURITY KEYS? YES// NO

Would you like to include FUNCTIONS? YES// NO

Would you like to include HELP FRAMES? YES// NO

Would you like security codes sent along: NO// \<RET\> NO

Would you like this sent via the network: NO// \<RET\> NO

Maximum Routine Size (2000 - 9999) : 4000// \<RET\> 4000

===================================================================

OKAY, READY TO RUN DIFROM!

===================================================================

Enter RETURN to continue or '^' to exit: \<RET\>Encounter Form IRM Options

> Import/Export Utility

\* \* Please Note \* \*

DIFROM generates routines in the following format:

nmspInxx

^^^^^^^^

\|\|\|\|\|\|\|\|

\|\|\|\|\|\| \\- xx is any combination of numbers and

\|\|\|\|\|\| upper case alpha characters.

\|\|\|\|\|\|

\|\|\|\|\| \\-- n is a number 0 - 9 and uppercase letter N.

\|\|\|\|\|

\|\|\|\| \\--- I is always uppercase letter I.

\|\|\|\|

\\\\----- 2 to 4 characters of package namespace.

Any routines that support the init process should not

be in this format.

Enter the Name of the Package (2-4 characters): IBDE IB ENCOUNTER FORM IMP/EXP IBDE

I am going to create a routine called 'IBDEINIT'.

Is that OK? YES

Would you like to include Data Dictionaries? YES// \<RET\>

Would you like to see the package definition? NO// \<RET\>

Do you want to accept the current definition? NO// YESEncounter Form IRM Options

> Import/Export Utility

IMP/EXP ENCOUNTER FORM

IMP/EXP ENCOUNTER FORM BLOCK

IMP/EXP SELECTION LIST

IMP/EXP SELECTION

IMP/EXP SELECTION GROUP

IMP/EXP DATA FIELD

IMP/EXP PACKAGE INTERFACE

IMP/EXP FORM LINE

IMP/EXP TEXT AREA

IMP/EXP MARKING AREA

IMP/EXP HAND PRINT FIELD

IMP/EXP MULTIPLE CHOICE FIELD

IMP/EXP AICS DATA ELEMENTS

IMP/EXP AICS DATA QUALIFIERS

Now you must enter the information that goes on the second line

of the INIT routines.

Select VERSION: 3.0// \<RET\>

Are you adding '3.0' as a new VERSION (the 3RD for this PACKAGE)? Y (Yes)

VERSION DATE DISTRIBUTED: 3/24/97 (MAR 24, 1997)

DATE DISTRIBUTED: MAR 24,1997// \<RET\>

Would you like to include OPTIONS? YES// NO

Would you like to include BULLETINS? YES// NO

Would you like to include SECURITY KEYS? YES// NO

Would you like to include FUNCTIONS? YES// NO

Would you like to include HELP FRAMES? YES// NO

Would you like security codes sent along: NO// \<RET\>

Maximum Routine Size (2000 - 9999) : 5000//\<RET\>

...SORRY, HOLD ON...

Moving IB ENCOUNTER FORM IMP/EXP Entry into Init's.....

IBDEI001 HAS BEEN FILED...

IBDEI002 HAS BEEN FILED.......

Encounter Form IRM Options

> Import/Export Utility

IBDEI003 HAS BEEN FILED...

IBDEI004 HAS BEEN FILED.......

IBDEI005 HAS BEEN FILED...

IBDEI006 HAS BEEN FILED.......

IBDEI007 HAS BEEN FILED...

IBDEI008 HAS BEEN FILED...

IBDEI009 HAS BEEN FILED...

IBDEI00A HAS BEEN FILED...

IBDEI00B HAS BEEN FILED...

IBDEI00C HAS BEEN FILED...

IBDEI00D HAS BEEN FILED...

IBDEI00E HAS BEEN FILED...

IBDEI00F HAS BEEN FILED...

IBDEI00G HAS BEEN FILED.......

IBDEI00H HAS BEEN FILED...

IBDEI00I HAS BEEN FILED.......

IBDEI00J HAS BEEN FILED...

IBDEI00K HAS BEEN FILED.......

IBDEI00L HAS BEEN FILED...

IBDEI00M HAS BEEN FILED...

IBDEI00N HAS BEEN FILED...

IBDEI00O HAS BEEN FILED...

IBDEI00P HAS BEEN FILED...

IBDEI00Q HAS BEEN FILED...

IBDEI00R HAS BEEN FILED...

IBDEI00S HAS BEEN FILED.......

IBDEI00T HAS BEEN FILED...

IBDEI00U HAS BEEN FILED.......

IBDEI00V HAS BEEN FILED...

IBDEI00W HAS BEEN FILED.......

IBDEI00X HAS BEEN FILED...

IBDEI00Y HAS BEEN FILED.......

IBDEI00Z HAS BEEN FILED...

IBDEI010 HAS BEEN FILED.......

IBDEI011 HAS BEEN FILED...

IBDEI012 HAS BEEN FILED.......

IBDEI013 HAS BEEN FILED...

IBDEI014 HAS BEEN FILED.......

IBDEI015 HAS BEEN FILED...

IBDEI016 HAS BEEN FILED......

IBDEINI1 HAS BEEN FILED...

IBDEINI2 HAS BEEN FILED...

IBDEINI3 HAS BEEN FILED...

IBDEINI4 HAS BEEN FILED...

IBDEINI5 HAS BEEN FILED...

IBDEINIT HAS BEEN FILED...

IBDEINIS HAS BEEN FILED...

DONE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Encounter Form IRM Options

> Import/Export UtilityExample2 - Importing a Form

Select Action: Quit// RI Run Inits

The work space must be cleared before the INITS are run. Is that okay?

Enter Yes or No: YES

What is the name of the init routine that contains the forms that you want to

import? IBDEINIT// \<RET\>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

First the files contained in the inits will be listed.

THEN ....

You must enter these parameters to the prompts generated by INITS:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> NO

ARE YOU SURE EVERYTHING'S OK? NO// YES

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Now to execute the inits!

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Enter RETURN to continue or '^' to exit: \<RET\>Encounter Form IRM Options

> Import/Export Utility

This version (#2.1V1) of 'IBDEINIT' was created on 07-MAR-1997

(at ISC-ALBANY DEMO TEXT RET V.1, by VA FileMan V.21.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Initialization Started: MAR 07, 1997@11:07:33

I AM GOING TO SET UP THE FOLLOWING FILES:

358 IMP/EXP ENCOUNTER FORM (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP ENCOUNTER FORM' File.

I will OVERWRITE your data with mine.

358.1 IMP/EXP ENCOUNTER FORM BLOCK (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP ENCOUNTER FORM BLOCK' File.

I will OVERWRITE your data with mine.

358.2 IMP/EXP SELECTION LIST (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION LIST' File.

I will OVERWRITE your data with mine.

358.3 IMP/EXP SELECTION (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION' File.

I will OVERWRITE your data with mine.

358.4 IMP/EXP SELECTION GROUP (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION GROUP' File.

I will OVERWRITE your data with mine.

358.5 IMP/EXP DATA FIELD (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP DATA FIELD' File.

I will OVERWRITE your data with mine.

358.6 IMP/EXP PACKAGE INTERFACE (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP PACKAGE INTERFACE' File.

I will OVERWRITE your data with mine.

Encounter Form IRM Options

> Import/Export Utility

358.7 IMP/EXP FORM LINE (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP FORM LINE' File.

I will OVERWRITE your data with mine.

358.8 IMP/EXP TEXT AREA (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP TEXT AREA' File.

I will OVERWRITE your data with mine.

358.91 IMP/EXP MARKING AREA (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP MARKING AREA' File.

I will OVERWRITE your data with mine.

358.93 IMP/EXP MULTIPLE CHOICE FIELD (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP MULTIPLE CHOICE FIELD' File.

I will OVERWRITE your data with mine.

358.94 IMP/EXP HAND PRINT FIELD (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP HAND PRINT FIELD' File.

I will OVERWRITE your data with mine.

358.98 IMP/EXP AICS DATA QUALIFIERS (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP AICS DATA QUALIFIERS' File.

I will OVERWRITE your data with mine.

358.99 IMP/EXP AICS DATA ELEMENTS (Partial Definition) (including data)

> **NOTE:** You already have the 'IMP/EXP AICS DATA ELEMENTS' File.

I will OVERWRITE your data with mine.

SHALL I WRITE OVER FILE SECURITY CODES? No// \<RET\> (No)

ARE YOU SURE EVERYTHING'S OK? No// Y (Yes)

...HMMM, JUST A MOMENT PLEASE..................................................

..........................................

OK,I’M DONE.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Encounter Form IRM Options

> Import/Export Utility

<u>Import/Export Work Space Mar 07, 1997 11:08:24 Page: 1 of 1</u>

LIST OF FORMS READY FOR IMPORT OR EXPORT

(\*\* there are also toolkit blocks in the work space \*\*)

<u>FORM NAME USE & BRIEF DESCRIPTION</u>

1 DEFAULTS selection list defaults - DO NOT DELETE

2 PRIMARY CARE SAMPLE V2.1 scannable form for primary care

<u>Enter ?? for more actions \>\>\></u>

HE Help DE Delete Entry DI DIFROM

LB List TK Blocks AE Add Entry RI Run Inits

IE Import Entry VI View Imp/Exp Notes

CW Clear Work Space EI Edit Imp/Exp Notes

Select Action: Quit//

<u>Import/Export Work Space Mar 07, 1997 11:08:24 Page: 1 of 1</u>

LIST OF FORMS READY FOR IMPORT OR EXPORT

(\*\* there are no toolkit blocks in the work space \*\*)

<u>FORM NAME USE & BRIEF DESCRIPTION</u>

1 PRIMARY CARE SAMPLE V2.1 scannable form for primary care

<u>Enter ?? for more actions \>\>\></u>

HE Help DE Delete Entry DI DIFROM

LB List TK Blocks AE Add Entry RI Run Inits

IE Import Entry VI View Imp/Exp Notes

CW Clear Work Space EI Edit Imp/Exp Notes

Select Action: Quit// IE=1 Import Entry

New Form Name: PRIMARY CARE SAMPLE V2.1 Replace \<RET\> …………

SHOULD THIS FORM BE PART OF THE TOOKIT?: YES// \<RET\> …………

Encounter Form IRM Options

### ### Recompile All Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the IBDF IRM security key.

This option is used to recompile all forms. The compiled version of every form and block is deleted. Each form is recompiled the first time it is printed.

Example

Do you really want to Recompile all Forms? YES

Uncompiling all forms..........................

Okay, forms will be recompiled as they are printed.

Encounter Form IRM Options

### ### Miscellaneous Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the IBDF IRM security key.

This option deletes various data structures that are no longer in use. Because AICS was designed to automatically delete all data structures when no longer needed, this option is a backup that should rarely be needed. Currently, the option deletes the compiled version of forms where the form itself no longer exists. It also deletes blocks that do not belong to any form.

When you use this option, the cleanup is performed, a message similar to the following appears on the screen, and you automatically return to the menu.

Blocks not belonging to any form have been deleted Extraneous cross-references on non-existent forms have been deleted

Encounter Form IRM Options

### Device Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is locked with the IBDF IRM security key.

This option allows editing of the Encounter Form Printers file. You can specify whether or not a terminal type is PCL5 compatible and the proper escape sequences for simplex and duplex. Only PCL5 compatible printers can print scannable encounter forms, and must be so indicated. Most HP laser printers are PCL5 compatible.

## Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add/Edit Encounter Form Printers Terminal Type

Select ENCOUNTER FORM PRINTERS TERMINAL TYPE: P-HPLASER/16/8/UP/DUPLEX

Laser Jet with 16.66 pitch and 8 lines per inch (Upright)

...OK? Yes// \<RET\> (Yes)

TERMINAL TYPE: P-HPLASER/16/8/UP/DUPLEX// \<RET\>

PRINTER LANGUAGE TYPE: PCL5// \<RET\>

SIMPLEX: \$C(27)\_"&l0S"// \<RET\>

DUPLEX, LONG-EDGE BINDING: \$C(27)\_"&l1S"// \<RET\>

DUPLEX, SHORT-EDGE BINDING: \$C(27)\_"&l2S"// \<RET\>

Select ENCOUNTER FORM PRINTERS TERMINAL TYPE:

  
Encounter Form IRM Options

### ### Purge Form Tracking files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is locked with the IBDF IRM security key.

This option purges old data from the ENCOUNTER FORM TRACKING file (357.96), the ENCOUNTER FORM DEFINITION file (357.95), and the FORM SPECIFICATION file (359.2). It should be queued to run at the site’s convenience. The IBDF AUTO PURGE FORM TRACKING option should be used to automatically queue this option to run on a recurring basis.

The option needs no device and has no output.

Example

Do you want to purge Form Tracking?

Enter Yes or No: YES

This is a required response. Enter '^' to exit

Enter Yes or No: NO

Number of Days to Retain: (60-999): 60// 100

Select one of the following:

0 None

1 Purge Completed Entries

2 Purge All Entries

Purge what Entries: 1// 2 Purge All Entries

Requested Start Time: NOW// \<RET\> (MAR 06, 1997@08:50:19)

Requested Queued Task+236109

## Reports and Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Form Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view form and block components such as starting row, block height and width, block name and contents, and subcolumn information for selection lists.

Example

<u>Form Components Mar 07, 1997 13:07:47 Page: 1 of 4</u>

Form Name: PRIMARY CARE2 SAMPLE V2.1 FORM ID \#:

Status: Uncompiled Toolkit: Yes

Scannable: Yes Use ICR: Yes

Simplex/Duplex: Duplex Short-Edge \# Pages: 2

1\) PATIENT INFORMATION (V2.1)

Starting Row: 2 Starting Column: 1

Block Width: 63 Block Height: 21

2\) HEADER

Starting Row: 2 Starting Column: 90

Block Width: 12 Block Height: 1

3\) APPOINTMENT

Starting Row: 6 Starting Column: 68

Block Width: 66 Block Height: 5

<u>4) FUTURE APPTS (V2.1)</u>

<u>+ Enter ?? for more actions</u>

EX Expand Item BC Block Components

Select Action: Next Screen//

  
Reports and Utilities

### Edit Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option is locked with the IBDF IRM security key.

The FILL % FOR BUBBLES and BACKGROUND % FOR BUBBLES fields are asked only if you hold the IBD MANAGER key.

This option allows editing of AICS site parameters that affect the printing of forms, manual data entry, the purge utility and scanning.

Following are the parameters with a brief description. A double question mark (??) entered at any prompt provides a complete description of that parameter.

Form Tracking Purge Parameters

RECORDS TO PURGE - whether you want the background purge option to purge *all records* , *completed records*, or *no records* older than the number of days specified in the FORM TRACKING RETENTION DAYS field.

FORM TRACKING RETENTION DAYS - the number of days to retain form tracking information after it is no longer used.

PURGE NOTIFICATION MAIL GROUP - the mail group automatically notified of purge results. Results are also stored in the AICS PURGE LOG file and may be reviewed. Mail notification is not required.

Data Entry Parameters

DEFAULT DATA ENTRY FORM - the form to be used as the default form for doing data entry when no form exists for a clinic. If no form is defined, the Primary Care Sample form exported with AICS 2.1 will be used as the default form.

  
Reports and UtilitiesEdit Site Parameters

MAKE APPOINTMENT IN DATA ENTRY - whether you want users at your site to be prompted to make a follow up appointment during data entry of an encounter form.

PASS DATA TO PCE - how data captured in the AICS EF Data Entry Options should be passed to PCE. (Enter a double question mark at the prompt for a list of choices with complete descriptions.)

Print Parameters

PRINT FORMS FOR INPATIENTS - whether you would like to suppress printing of encounter forms for inpatients. If left blank, Encounter Forms for inpatients will print.

DAYS TO PRINT 1010F - the number of days between the expiration of a Means Test and the appointment date before that you want to print 1010Fs for. For example, if this field is set to 30, then 1010Fs will print for Means Tests that are due to expire within 30 days of the appointment.

Scanning Parameters

FILL % FOR BUBBLES - a number between 0 and 99 that represents the percentage of fill required for a bubble to be considered as checked. Entering a zero will leave the determination up to Paper Keyboard. If this field is left blank, AICS will use 20% as the amount of fill required.

This field corresponds to the Threshold % field in the Metric dialog box in Paper Keyboard. The value of this field should always be more than the value for the BACKGROUND % FOR BUBBLES field.

Modifying this field will affect only new files, and will not affect any existing form specification files. To modify an existing form specification file, it must be deleted from the workstation and the corresponding entry in file 359.2 must be deleted. This field is asked only if you hold the IBD MANAGER key.

BACKGROUND % FOR BUBBLES - a number between 0 and 99 that represents the percentage of background fill in a bubble that can exist before Paper Keyboard will consider any markings in the bubble. If this field is left blank then AICS will use 5%. Entering a zero leaves the determination up to Paper Keyboard.

  
Reports and UtilitiesEdit Site Parameters

This field corresponds to the Background % field in the Metric dialog box. Entering a small value prevents small dots on the page from appearing as check marks. The value of this field should always be less than the value for the FILL % FOR BUBBLES field.

Modifying this field will affect only new files, and will not affect any existing form specification files. To modify an existing form specification file, it must be deleted from the workstation and the corresponding entry in file 359.2 must be deleted. This field is asked only if you hold the IBD MANAGER key.

STOP DEFAULTING C/O DATE/TIME - if there is no checkout date/time on the encounter form, the scan date/time is automatically entered by default as the checkout date/time. YES must be entered in this field to stop the automatic default.

Example

Edit AICS Site Parameters

Form Tracking Purge Parameters

RECORDS TO PURGE: COMPLETED// \<RET\>

FORM TRACKING RETENTION DAYS: 60// \<RET\>

PURGE NOTIFICATION MAIL GROUP: \<RET\>

Data Entry Parameters

DEFAULT DATA ENTRY FORM: PRIMARY CARE// \<RET\>

MAKE APPOINTMENT IN DATA ENTRY: YES// \<RET\>

PASS DATA TO PCE: FOREGROUND/WITH DISPLAY// \<RET\>

Print Parameters

PRINT FORMS FOR INPATIENTS: YES// \<RET\>

DAYS TO PRINT 1010F: 30// \<RET\>

Scanning Parameters

FILL % FOR BUBBLES: 20

BACKGROUND % FOR BUBBLES: 5

STOP DEFAULTING C/O DATE/TIME: YES// \<RET\>  
Reports and Utilities

### Scanning Error Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During scanning, errors reported by AICS or PCE are stored in the AICS Error & WARNING Log file. This report allows you to print a list of the errors so that the encounter forms can be retrieved and the data validated.

This report prints at 132 columns.

Example

AICS UNCORRECTED SCANNING ERROR LIST MAR 7,1997 13:23 PAGE 1

FORM

TRACKING ERROR

PATIENT ID APPOINTMENT DATE ID SOURCE USER ERROR MESSAGE

----------------------------------------------------------------------------------------------------------------------------------

841, AICS AICSUSER,ONE SCANNING ERROR: AICS was passed a

Form ID of "841," and this entry

does not exist in the Form

Tracking file.

No other information about the

form was available. No data was

passed to PCE. Error Code

3579605\.

AICSPATIENT,ONE 000-45-6789 APR 17,1997 08:00 300005 PCE AICSUSER,TWO SCANNING ERROR: PCE Returned the

following Errors and Warnings for

Form ID: 33029. PCE ERROR: ICD9

Code not in file 80 - 438. PCE

ERROR: User is not in File 200 - 0

PCE WARNING: There is already a

Primary Diagnosis this one is

changed to Secondary - P PCE

> **WARNING:** There are "PXKERROR"s in

in the "PCE DEVICE INTERFACE

MODULE ERRORS" file in entry

number - 94

  
Reports and Utilities

### Forms Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new actions have been added. Delete Entry allows a forms tracking entry to be deleted. Rel Forms w/Lost Pages allows you to pass a Forms Tracking entry to PCE when the remainder of the pages have been lost.

The IBD MANAGER key is required to use the new action, RF Rel Forms w/Lost Pages.

This option now also sorts by clinic group.

The Status Report now lists by date order within clinics.

The Statistics Report now includes the number and percentage of forms entered through manual data entry (DE); and number and percentage sent to PCE.

New statuses have been added (see below).

This report is now queuable to a printer.

This option allows you to display encounter forms sorted by clinic, patient, or clinic group for a specified division(s), clinic group(s) and date range. The Change List action, found on the Form Tracking Status Report screen, allows you to re-enter this information without exiting the option.

The Form Tracking Status Report, shows the date the form was printed and scanned (if applicable), and the status.

The Statistics Report shows statistical information such as the number and percentage of forms printed, entered through manual data entry, and scanned for each clinic.

The Status Select Report allows you to display forms with a specific status(es).

  
Reports and UtilitiesForms TrackingExample

Following are the possible statuses.

ALL

PRINTED

SCANNED

SCANNED TO PCE

SCANNED W/PCE ERROR

DATA ENTRY

DATA ENTRY TO PCE

DATA ENTRY W/PCE ERROR

PENDING PAGES

ERRORS DETECTED, NOT TRANSMITTED

*Form Tracking Main Screen*

<u>Form Tracking Status Report Mar 07, 1997 13:30:26 Page: 1 of 2</u>

Encounter forms - printed; scanned (to PCE, w/ERrors); pending pages;

data entry (to PCE,w/ERrors); error detected, not transmitted; not printed.

<u>FORM ID APPT. D/T PATIENT/CLINIC PRINTED SCANNED STATUS</u>

ALBANY

CARDIOLOGY

1\) 78 01/08/97 09:00 AICSpatient,One 01/08/97 01/24/97 Pend Pgs

2\) 79 01/08/97 11:30 AICSpatient,Two 01/08/97 02/27/97 Pend Pgs

3\) 33002 02/10/97 14:46 AICSpatient,Two 02/10/97 02/10/97 De W/Er

4\) 33005 02/19/97 13:00 AICSpatient,Two 02/26/97 02/26/97 Scanned

ORTHOPEDIC

5\) 80 01/08/97 13:00 AICSpatient,Two 01/08/97 Printed

TROY

<u>+ Enter ?? for more actions \>\>\></u>

SA Statistics PL Print List DL Delete Entry

SS Status Select CL Change List

Select Action: Next Screen//

  
Reports and UtilitiesForms Tracking

*Statistics Report*

<u>Statistics Report Mar 07, 1997 13:34:47 Page: 1 of 1</u>

Statistical data for the date range of NOV 27,1996 to MAR 7,1997

<u>CLINIC/PATIENT TOTAL \#PRNT %PRNTD \#DE %DE \#SCND %SCND</u> \#PCE

ALBANY

Dermatology 4 4 100 0 0 1 25 0

Orthopedic 1 1 100 0 0 0 0 0

TROY

Ophthalmology 7 6 85.71 0 0 0 0 0

Cardiology 4 3 75 0 0 0 0 0

<u>Enter ?? for more actions \>\>\></u>

PL Print List

Select Action: Quit//

*Status Report*

<u>Status Select Report Mar 07, 1997 13:36:58 Page: 1 of 2</u>

Encounter forms with selected status for the date range of

NOV 27,1996 to MAR 7,1997

<u>FORM ID APPT. D/T PATIENT/CLINIC PRINTED SCANNED STATUS</u>

ALBANY

CARDIOLOGY

1\) 78 01/08/97 09:00 AICSpatient,One 01/08/97 01/24/97 Pendng

2\) 79 01/08/97 11:30 AICSpatient,Two 01/08/97 02/27/97 Pendng

3\) 33002 02/10/97 14:46 AICSpatient,Two 02/10/97 02/10/97 De/Er

4\) 33005 02/19/97 13:00 AICSpatient,Two 02/26/97 02/26/97 Scannd

ORTHOPEDIC

5\) 80 01/08/97 13:00 AICSpatient,Two 01/08/97 Printed

TROY

<u>+ Enter ?? for more actions</u>

PL Print List

Select Action: Next Screen//

  
Reports and Utilities

### List Clinics Using Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option provides a list, by division, of encounter forms and the clinics using each form. It can be used to identify what clinics might be sharing a form, as well as to determine when a form is not being used.

Example

List of Encounter Forms and their Use by Clinics Mar 07, 1997@13:38:54 PAGE 1

For Division: ALBANY

FORM NAME CLINIC DIVISION

FORM USAGE

------------------------------------------------------------------------------

Division: ALBANY

32X-DENTAL DENTAL ALBANY

Basic Form

CARDIOLOGY TROY

Basic Form

BILOXI.AICS DERMATOLOGY ALBANY

Form w/o Patient Data

CARDIOLOGY ALBANY

Form w/o Patient Data

BILOXI.AICS II DERMATOLOGY ALBANY

Supplmntl form - Establshed Pt.

BILOXI.AICS III DERMATOLOGY ALBANY

Reserved

GITEST GI ALBANY

Basic Form

PRIMARY CARE GEN MED ALBANY

Basic Form

ORTHOPEDIC ALBANY

Basic Form

Enter RETURN to continue or '^' to exit: \<RET\>

List of Encounter Forms and their Use by Clinics Mar 07, 1997@13:38:54 PAGE 2

For Division: FORMS NOT IN USE

FORM NAME CLINIC DIVISION

FORM USAGE

-------------------------------------------------------------------------------

CNV.32X-DENTAL \*\* NOT IN USE \*\*

GENERAL MED \*\* NOT IN USE \*\*

GENERAL MEDICINE \*\* NOT IN USE \*\*

INFECTIOUS DIS CLIN \*\* NOT IN USE \*\*

NEW NAME \*\* NOT IN USE \*\*  
Reports and Utilities

### Maintenance Utility for Active/Inactive Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction*Note: With functionality put in place by the Code Set Versioning project, the date and time that this report is run will determine whether codes are considered active or inactive.*

<span id="ICDp75b" class="anchor"></span>*Note 2: Patch IBD\*3\*63 adds ICD-10 code information. You can now select either ICD-9 or ICD-10 Diagnosis Codes, depending on whether the date is before the ICD-10 Activation Date (ICD-9) or on or after the ICD-10 Activation Date (ICD-10).*

Now allows you to list active CPT, ICD-9 or ICD-10, and Visit codes that appear on encounter forms.

This option allows you to display a list of invalid ICD-9 or ICD-10, CPT and VISIT codes that appear on encounter forms. You can display a selected type of code by individual clinic(s), clinic group(s), or encounter form(s). The Change List action allows you to re-enter this information without exiting the option.

Other actions allow you to display a complete list of all invalid ICD-9 or ICD-10, CPT, and VISIT codes; and replace or delete invalid codes from the forms.

The Jump action allows you to jump to any clinic/group/form on the Maintenance Utility screen.

Example

Sort by \[C\]linics, \[G\]roups, \[F\]orms: CLINICS// \<RET\> (Individual)

Select Clinic: ALL// \<RET\>

Select Type of Code to Display: DG

1 DG SELECT CPT PROCEDURE CODES TYPE=SELECTION

2 DG SELECT ICD-10 DIAGNOSIS CODES TYPE=SELECTION

3 DG SELECT ICD-9 DIAGNOSIS CODES TYPE=SELECTION

4 DG SELECT VISIT TYPE CPT PROCEDURES TYPE=SELECTION

CHOOSE 1-4: 3 DG SELECT ICD-9 DIAGNOSIS CODES TYPE=SELECTION

Display codes \[A\]ctive, \[I\]nactive: ACTIVE// \<RET\>

Select ICD-9 code:

  
Reports and UtilitiesMaintenance Utility for Active/Inactive Codes

The Replace Code action in the Maintenance Utility Report prompt has changed depending upon which Type of Code you selected (ICD-9 or ICD-10).

*Replace Code for ICD-9 Codes*

Select Action: Next Screen// RC=3 Replace Code

Select ICD 9 DIAGNOSIS CODE NUMBER: 278.01 278.01 MORBID OBESITY

...OK? Yes// \<RET\> (Yes)

Subcolumn Header:

Edit Subcolumn 3: MORBID OBESITY// \<RET\>

<span id="ICDp75" class="anchor"></span>NARRATIVE TO SEND TO PCE: ??

Enter the narrative that should be sent to PCE when this selection is

scanned. This will be the provider narrative that is shown in PCE. If there is no entry in this field the text as it appears on the form will be sent as the narrative.

This field can only be entered for the type of interfaces that allow

adding this narrative, and then send the narrative to PCE.

NARRATIVE TO SEND TO PCE:

<span id="ICDp76" class="anchor"></span>*Replace Code for ICD-10 Codes*

Select Action: Next Screen// RC=3 Replace Code

Enter Diagnosis, a Code or a Code Fragment:

This prompt allows you to use the partial code search.

*Invalid Code List*

<u>Complete Invalid List Mar 07, 1997 13:46:31 Page: 1 of 267</u>

This screen displays the most current invalid codes for the CPT file.

<u>CODE DESCRIPTION CATEGORY</u>

Allergy And Clinical Immu

1\) 95000 Allergy Skin Tests, Allergy And Clinical

2\) 95001 Allergy Skin Tests, Allergy And Clinical

3\) 95002 Allergy Skin Tests, Allergy And Clinical

4\) 95003 Allergy Skin Tests, Allergy And Clinical

5\) 95005 Sensitivity Skin Tes Allergy And Clinical

6\) 95006 Sensitivity Skin Tes Allergy And Clinical

7\) 95007 Sensitivity Skin Tes Allergy And Clinical

8\) 95011 Sensitivity Skin Tes Allergy And Clinical

9\) 95014 Sensitivity Skin Tes Allergy And Clinical

10\) 95016 Sensitivity Skin Tes Allergy And Clinical

<u>11) 95017 Sensitivity Skin Tes Allergy And Clinical</u>

<u>+ Enter ?? for more actions</u>

JP Jump

Select Action: Next Screen//

  
Reports and UtilitiesMaintenance Utility for Active/Inactive Codes

*Jump*

<u>Complete Invalid List Mar 07, 1997 13:50:03 Page: 5 of 267</u>

This screen displays the most current invalid codes for the CPT file.

<u>+ CODE DESCRIPTION CATEGORY</u>

Cardiovascular

50\) 93045 Special Electrocardi Cardiovascular

51\) 93240 Ballistocardiogram Cardiovascular

52\) 93255 Apexcardiography Cardiovascular

53\) 93258 Ecg Monitor/Report, Cardiovascular

54\) 93259 Ecg Monitor/Report, Cardiovascular

55\) 93262 Ecg Monitor/Report, Cardiovascular

56\) 93263 Ecg Monitor/Report, Cardiovascular

57\) 93266 Ecg Monitor/Record, Cardiovascular

58\) 93269 Ecg Monitor/Record Cardiovascular

59\) 93273 Ecg Monitor/Report, Cardiovascular

<u>60) 93274 Ecg Monitor/Report, Cardiovascular</u>

<u>+ Enter ?? for more actions</u>

JP Jump

Select Action: Next Screen//

Reports and Utilities

### Clinics With No Encounter Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This report lists, by division, all clinics that do not have encounter forms assigned to them. Division counts are provided.

Example

List of Clinics Without Encounter Forms Mar 07, 1997@14:16:48 PAGE 1

For Division: TROY

CLINICS SERVICE COMMENT

------------------------------------------------------------------------------

Division: TROY

PULMONARY MEDICINE

PULMONARY FUNCTION MEDICINE

RENAL-I MEDICINE

RENAL-II MEDICINE

RES/MED MEDICINE

RHEUMATOLOGY MEDICINE

----------------

Division Count = 6

  
Reports and Utilities

### Print Sample of all Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints one copy of each form currently in use. It could be used to prepare a package of materials for review, or to share with other facilities.

This could be lengthy depending on the number of forms. It is also important to remember encounter forms require a page size of 80 lines and 132 columns.

Instead of printing the patient name and SSN at the bottom of the form, this option will print the form name and clinic. Care needs to be exercised in distributing forms with patient identifiers that appear on other areas of the form.

  
Reports and UtilitiesPrint Sample of all FormsExample

+-------------------------------------------------------------+ Primary Care

\| PATIENT INFORMATION \|

\| \|

\|Patient Name: AICSPATIENT,ONE \|

\|DOB: JUL 7,1950 PID: 000-45-6789 Sex: M \| +-------------------------------------------------------------+

\|Eligibility: NSC \| \| APPOINTMENT INFORMATION \|

\|Means Test Cat: N \| \|Clinic: BONNIE \|

\|Address: Telephone:399-0000 \| \|Appt. DT/Time: FEB 09, 1996@07:49:32 \|

\| SCREEN 1 ADDRESS \| +-------------------------------------------------------------+

\| LSKDJFLKJSD, CALIFORNIA 90062 \| +-------------------------------------------------------------+

\| \| \| FUTURE APPOINTMENTS \|

\| \| \| \|

\| ACTIVE INSURANCE POLICIES \| \| \|

\|AETNA 9029 INS \# \| \| \|

\|GHI DSFKLJFSDJKL \| \| \|

\|GHI POIREWP \| \| \|

\|Marital Status: DIVORCED \| \| \|

\|Employer: EMPLOYER NAME \| \| \|

\|Spouse's Emp: \| \| \|

\| \| +-------------------------------------------------------------+

+-------------------------------------------------------------+ +-------------------------------------------------------------+

\| VITALS \| \| \*\*\*\*\*\* PATIENT ALLERGIES \*\*\*\*\*\* \|

\| \| \| TYPE VERIFIED \|

\|Blood Press.: / \| \| \|

\| \_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\| systolic/diastolic\| \| \|

\| \| \| \|

\| Weight: . \| \| \|

\| \_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\| lbs \| \| \|

\| \| \| \|

+-------------------------------------------------------------+ +-------------------------------------------------------------+

+----------------------------------------------------------------------------------------+ +---------------------------------+

\| SERVICE CONNECTED CONDITIONS \| \| CHECKOUT \|

\|Service Connected Percentage: AO: NO IR: NO POW: NO EC: NO \| \| \|

\| \| \|No-show \[ \] \|

\| \| \|Cancel \[ \] \|

\| \| \|Rescheduled \[ \] \|

\| \| \| \|

\| \| \|Checkout: \|

\| \| \| \_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\| hhmm \|

\|Was the visit related to: SC \[ \] AO \[ \] EC \[ \] IR \[ \] \| \| \|

+----------------------------------------------------------------------------------------+ +---------------------------------+

+----------------------------------------------------------------------------------------+ +---------------------------------+

\| TYPE OF VISIT \| \| PROVIDER \|

\| \| \| \|

\| NEW PATIENT \|\| ESTABLISHED PATIENT \|\| CONSULTATIONS \| \| P \|

\| Brief Visit \| \[ \] \|\| Brief Exam \| \[ \] \|\| Brief Visit \| \[ \] \| \|#1 \[ \] HYPHEN-NAME,PROVIDER \|

\| Limited Exam \| \[ \] \|\| Limited Exam \| \[ \] \|\| Limited Visit \| \[ \] \| \| \[ \] \|

\| Intermediate Exam \| \[ \] \|\| Intermediate Exam \| \[ \] \|\| Intermediate Visit \| \[ \] \| \| \[ \] \|

\| Extended Exam \| \[ \] \|\| Extended Exam \| \[ \] \|\| Extended Visit \| \[ \] \| \| \[ \] \|

\| Comprehensive Exam \| \[ \] \|\| Comprehensive Exam \| \[ \] \|\| Comprehensive Visit \| \[ \] \| \| \[ \] \|

+----------------------------------------------------------------------------------------+ +---------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+

\| PROCEDURES \|

\| \[ \] Acne Surgery 10040 \| \[ \] Removal/revision of cast 29799 \| \[ \] Pneumococcal (V03.82) 9073\|

\| \[ \] Application of Paste Boot 29580 \| \[ \] Remove impacted ear wax 69210 \| \[ \] PPD skin test 8658\|

\| \[ \] Assay quantitative glucose 82947 \| \[ \] Spirometry 94010 \| \[ \] Testosterone 100/200 mg 8440\|

\| \[ \] Biopsy of skin lesion 11100 \| \[ \] TB intradermal test 86580 \| \[ \] Tetanus/Diptheria (V03.7) 9072\|

\| \| \[ \] Toe nail trimming 11750 \| \[ \] Toadol J188\|

\| Blood gases: \| \| \[ \] Vitamin B-12 9078\|

\| \[ \] Ph 82800 \| Injection/Immunizations: \| \|

\| \[ \] PO2/PCO2 82803 \| \[ \] Antibiotic 90788 \| \|

\| \| \[ \] Decadron J1100 \| \|

\| \[ \] Destruction of facial lesion 17000 \| \[ \] Hepatitis B 90731 \| \|

\| \[ \] Drainage of skin abscess 10060 \| \[ \] Influenza (V04.8) 90724 \| \|

\| \[ \] EKG, routine (12 leads) 93000 \| \[ \] Small joint/bursa 20600 \| \|

\| \[ \] Oximetry, noninvasive 94760 \| \[ \] Medium joint/bursa 20605 \| \|

\| \[ \] Pulmonary function test 94010 \| \[ \] Major joint/bursa 20610 \| \|

\| \|

\| Procedure Narrative CPT CODE \|

\| (OTHER#1) \|

\| \[ \] \|

\| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\|

\| (OTHER#2) \|

\| \[ \] \|

\| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\|

\| (OTHER#3) \|

\| \[ \] \|

\| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\|

+--------------------------------------------------------------------------------------------------------------------------------+

  
Reports and UtilitiesPrint Sample of all Forms

+--------------------------------------------------------------------------------------------------------------------------------+

\| DIAGNOSIS \|

\| Cardiovascular \| \[ \] Gastroenteritis 558.9 \| \[ \] Chronic renal insufficiency 593.9 \|

\| \[ \] Aortic stenosis/insuff 424.2 \| \[ \] GI bleeding 578.9 \| \[ \] Dialysis status V45.1 \|

\| Arrhytmia: \| \[ \] Hemorrhoids 455.6 \| \[ \] Hematuria 599.7 \|

\| \[ \] Atrial flutter 427.32 \| \[ \] Hepatitis viral, NOS 070.9 \| \[ \] Impotence 607.84 \|

\| \[ \] Atrial tachycardia 427.89 \| \[ \] Hepatitis, alcoholic 571.1 \| \[ \] Renal calculus 592.0 \|

\| \[ \] Sick sinus syndrome 427.81 \| \[ \] Intestinal malabsorption 579.9 \| \[ \] Urinary tract infection 599.0 \|

\| \[ \] Other arrhythmia 427.9 \| \[ \] Irritable bowel syndrome 564.1 \| Rheumatology/Ortho \|

\| \| \[ \] Pancreatitis, acute 577.0 \| \[ \] Ankylosing spondylitis 720.0 \|

\| \[ \] Cardiomyopathy 425.4 \| \[ \] Pancreatitis, chronic 577.1 \| \[ \] Arthralgia 719.40 \|

\| \[ \] Coronary pulmonale 416.9 \| \[ \] Polyp(s), colon 211.3 \| \[ \] Bursitis 727.3 \|

\| \[ \] Coronary bypass surg (Hx) V15.2 \| \[ \] Ulcer, peptic 533.90 \| \[ \] Carpal tunnel syndrome 354.0 \|

\| \[ \] Endocarditis 424.90 \| Hematology/Oncology \| DJD/oteoarthritis: \|

\| \[ \] Hypertension, essential 401.9 \| \[ \] Anemia 285.9 \| \[ \] Hip 715.95 \|

\| \[ \] Mitral valve prolapse 424.0 \| Anemia, defiency: \| \[ \] Knee 715.96 \|

\| Dermatology \| \[ \] B12 & folate 266.2 \| \[ \] Multiple sites 715.89 \|

\| \[ \] Acne 706.1 \| \[ \] Folate 281.2 \| \[ \] Shoulder 715.91 \|

\| \[ \] Alopecia 704.00 \| \[ \] Iron 280.9 \| \[ \] Fracture 829.0 \|

\| \[ \] Cellulitis 682.9 \| Musculoskeletal \| \[ \] Gout 274.9 \|

\| \[ \] Cyst, epiderm/sebaceous 706.2 \| \[ \] Hernia, femoral 553.00 \| \[ \] Hx of joint replacement V43.60 \|

\| \[ \] Dermatitis 692.9 \| \[ \] Hernia, inquinal 550.90 \| \[ \] Myalgia 729.0 \|

\| \[ \] Herpes zoster 053.9 \| \[ \] Low back pain, acute 724.2 \| \[ \] Osteoarthritis 715.90 \|

\| \[ \] Psoriasis 696.1 \| \[ \] Low back pain, chronic 724.9 \| \[ \] Osteomyelitis 730.20 \|

\| \[ \] Rosacea 695.3 \| \[ \] Muscle spasm 728.85 \| \[ \] Polyarthralgia, NOS 719.49 \|

\| \[ \] Seborrhea 706.3 \| Neurology \| \[ \] Rheumatoid arthritis 714.0 \|

\| \[ \] Seborrhea 701.9 \| \[ \] Alzheimer's disease 331.0 \| \[ \] Tendonitis 726.90 \|

\| \[ \] Skin hypertroph/atroph 701.9 \| \[ \] Bell's palsy 351.0 \| \[ \] Vertebral fx, closed 805.8 \|

\| \[ \] Skin lesion 709.9 \| \[ \] Caroid artery occlusion 433.10 \| Vascular \|

\| \[ \] Skin ulcer, chronic 707.9 \| \[ \] Convulsive/seizure disorder 780.3 \| \[ \] Abdominal aortic aneurysm 441.4 \|

\| Skin neoplasm: \| \[ \] CVA, Hx of w/o sequelae 436. \| \[ \] Thrombophlebitis 451.2 \|

\| \[ \] Benign 216.9 \| \[ \] Dementia, non-Alzheimers 290.0 \| \[ \] Varicose veins 454.9 \|

\| \[ \] Malignant 173.9 \| \[ \] Epilepsy 345.90 \| \[ \] Venous thrombosis 453.9 \|

\| \[ \] Melanoma 172.9 \| \[ \] Headache, migraine 346.90 \| \|

\| \[ \] Uncrtn behavior 238.2 \| \[ \] Headache, vascular 784.0 \| \|

\| EENT \| \[ \] Parkinson disease 332.0 \| \|

\| \[ \] Allergic rhinitis 477.8 \| \[ \] Sciatica, acute 724.3 \| \|

\| \[ \] Cerumen impaction 380.4 \| \[ \] Sciatica, chronic 724.4 \| \|

\| \[ \] Ear pain 388.70 \| \[ \] TIA 435.9 \| \|

\| Eye: \| Peripheral neuropathy due to: \| \|

\| \[ \] Cataract, senile 366.10 \| \[ \] Alcohol 357.5 \| \|

\| \[ \] Conjunctivitis 372.30 \| \[ \] Diabetes 250.60 \| \|

\| \[ \] Foreign body 930.9 \| \[ \] Drugs 356.9 \| \|

\| \[ \] Glaucoma 365.9 \| Psychiatric \| \|

\| \| \[ \] Alcoholism 303.90 \| \|

\| \[ \] Eustachian tube dysfunction 381.81 \| \[ \] Adjst Rxn emtn/&condct dsrd 312.10 \| \|

\| \[ \] Hearing loss 389.9 \| \[ \] Affective disorder 296.90 \| \|

\| \[ \] Otitis externa 380.10 \| \[ \] Anxiety state 300.00 \| \|

\| \[ \] Otitis media 382.9 \| \[ \] Depressive disorder 311. \| \|

\| \[ \] Pharyngitis, acute 462. \| \[ \] Drug abuse, NOS 305.90 \| \|

\| \[ \] Sinusitis, chronic 472.0 \| \[ \] Grief reaction 309.0 \| \|

\| \[ \] Sinusitis, acute 461.9 \| \[ \] Insomnia 780.50 \| \|

\| \[ \] Upper respiratory infection 465.9 \| \[ \] Psychosis, NOS 298.9 \| \|

\| Endocrine \| \[ \] Psychosocial problems V62.9 \| \|

\| \[ \] Diabetes I-IDDM comp 250.01 \| \[ \] PTSD, acute 308.3 \| \|

\| \[ \] Diabetes II-NIDDM comp 250.00 \| \[ \] PTSD, chronic 309.81 \| \|

\| \[ \] Hypercholesterolemia 272.0 \| \[ \] Schizophrenia 295.90 \| \|

\| \[ \] Hyperthyroidism 242.90 \| \[ \] Somatization disorder 300.81 \| \|

\| \[ \] Hypothyroidism 244.9 \| Pulmonology \| \|

\| \[ \] Obesity 278.0 \| \[ \] Asthma 493.90 \| \|

\| \[ \] Osteoporosis 733.00 \| \[ \] Bronchitis, acute 466.0 \| \|

\| Gastroenterology \| \[ \] Bronchitis, chronic 491.9 \| \|

\| \[ \] Cholelithiasis 574.20 \| \[ \] Emphysema 492.8 \| \|

\| \[ \] Cirrhosis, alcoholic 571.2 \| \[ \] Pharyngitis 462. \| \|

\| \[ \] Cirrhosis, non alcoholic 571.9 \| \[ \] Pneumonia, NOS 486. \| \|

\| \[ \] Diarrhea 558.9 \| \[ \] Pulmonary embolism (Hx of) V12.5 \| \|

\| \[ \] Diarrhea infectious 009.2 \| \[ \] Sinusitis, chronic 473.9 \| \|

\| \[ \] Diverticulosis 562.10 \| \[ \] Sleep apnea syndrome 780.57 \| \|

\| \[ \] Esophageal varices 456.1 \| Nephrology/Urology \| \|

\| \[ \] Esophageal reflux disease 530.81 \| \[ \] Bladder dysfunction 596.59 \| \|

\| \[ \] Gall Bladder disease 575.9 \| \[ \] Benign prostatic hypertrphy 600. \| \|

\| \| \| \|

\| Diagnosis ICD-9 Code \|

\| (OTHER#1) \|

\| \[ \] . \|

\| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\|

\| (OTHER#2) \|

\| \[ \] \|

\| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\_\_\_\|\|

+--------------------------------------------------------------------------------------------------------------------------------+

Reports and Utilities

### Report Clinic Setups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# This option provides a report that lists each clinic setup, and the encounter forms and other reports defined for use by that clinic. For clinics with reports defined, the condition on which the report is printed is also provided.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example

AICS Print Manager Clinic Setup Report Mar 12, 1997@09:19:59 PAGE 1

For Division: ALBANY

------------------------------------------------------------------------------

Division: ALBANY

Clinic: DENTAL

BASIC DEFAULT FORM: ..........................32X-DENTAL

Clinic: DERMATOLOGY

BASIC DEFAULT FORM: ..........................BILOXI.AICS

FORM WITH NO PRE-PRINTED PATIENT DATA: .......BILOXI.AICS

SUPPLEMENTAL FORM - PATIENT WITH PRIOR VISITS: BILOXI.AICS II

RESERVED FOR FUTURE USE: .....................BILOXI.AICS III

REPORTS PRINT CONDITION

======= ===============

ACTION PROFILE - 45 DAYS FOR EVERY APPOINTMENT

ACTION PROFILE - 45 DAYS FOR EVERY APPOINTMENT

Clinic: EF TEST

BASIC DEFAULT FORM: ..........................PRIMARY CARE

Enter RETURN to continue or '^' to exit:

<span id="ICDp83" class="anchor"></span>Reports and Utilities

### Encounter Forms ICD-10 Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to display a list of Encounter Forms and Clinics after making selections from several input options. When the report has been displayed, you may then update the ICD-10 Status field. Two date fields show the latest dates that the form was changed. The history fields contain the user ID (DUZ) of the person who last changed the files.

Example 1 Prompts for ICD-10 Status Update Summary Report

Select Reports and Utilities Option: UP Encounter Forms ICD-10 Update

Sort by \[C\]linics, \[G\]roups, \[F\]orms: CLINICS// \<RET\>

Select one of the following:

AC ALL CLINICS

SC SELECTED CLINICS

RC RANGE OF CLINICS

Selection type: ALL CLINICS// \<RET\>

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

\[S\]ummary Report, \[D\]etail Report: SUMMARY// Summary ReportSort Selections

If you sort the report by Clinics, the report output is sorted first by Clinic name, in alphabetic order, then by Encounter Form name, in alphabetic order.

If you sort the report by Groups, the report output is sorted first by Clinic Group, in alphabetic order, then by Clinic name, in alphabetic order, then by Encounter Form name, in alphabetic order.

If you sort the report by Forms, the report output is sorted by Encounter Form name, in alphabetic order.

Example 2 ICD-10 Status Update Summary Report

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

Initially, the IS action is blank (i.e., incomplete) for all Encounter Forms. You can select a single entry or a range of entries, and you are then prompted to change the update status to “REV” (Review) or “COMP” (Complete).

*Note: During the period of time when Encounter Forms are being updated for the initial activation of ICD-10, the ICD-10 Update Status “Incomplete” could be used to manage Encounter Forms that may have had none or only some ICD-10 diagnosis codes added; the Status “Review” could be used if ICD-10 diagnosis codes that have been added are impacted by an update to the ICD-10-CM code set; the Status “Complete” could be used if the Encounter Form’s ICD-10 update has been completed. For future updates to the ICD-10-CM code set (i.e., subsequent to the initial ICD-10 activation), the “Review” status could be used to indicate which Encounter Forms may require updates based on ICD-10-CM codes that have been added, deleted, or updated in the ICD-10-CM code set; the Status “Complete” could be used when those Encounter Form updates have been completed.*

<span id="ICDp84" class="anchor"></span>*Note: If you are editing Encounter Forms with Lexicon User Filters in place, those filters will be honored with the exception of editing an ICD-9 block or editing an ICD-10 block within the encounter form. When editing ICD-9 blocks, you will be allowed to choose from any ICD-9 code; and when editing an ICD-10 block, you will be allowed to select any ICD-10 code, regardless of what Lexicon User Filters are in place. Users will be prompted for whether they wish to enter Active or Inactive Diagnosis Codes for both code sets.*

### ICD-10 Search Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IBD\*3\*63 patch provides the ability to search on ICD-10-CM diagnosis codes when creating or editing Encounter Forms/blocks. Also, a wildcard search allows you to enter an “\*” (asterisk) to select multiple, valid ICD-10 diagnosis codes for Encounter Forms. Whether the current date is prior to or on or after the ICD-10 Activation Date, you can access the ICD-10-CM code set.

*Note: Existing ICD-9 search functionality has not changed.*ICD-10 Diagnosis Code Search

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

Example

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
ICD-10 Wildcard Search

The purpose of the ICD-10 wildcard search functionality for diagnosis code retrieval is to serve a specific user end goal, which is the selection of multiple, valid ICD-10 diagnosis codes (often related) to associate with specific functional elements, such as Encounter Forms. Use the wildcard search when you are defining Encounter Forms and have previously identified the ICD-10 codes that you want to quickly and efficiently select.

ICD-10 wildcard search highlights include:

- This is a completely code-based search (i.e., not text-based). Two wildcard characters (\* and ?) are used to assist with searches.
- If the search terms provided by the application consist of a string of characters (i.e., the search string) containing an \* (asterisk) as the wildcard character (e.g., E08\*, 005\*), the system finds all ICD-10 codes that match the search terms, where zero or more alphanumeric characters (including the “X” placeholder character for ICD-10-CM diagnosis codes) exist at the position where the \* exists in the search string.
- The \* (asterisk) wildcard character can only appear in the last position of the search string.
- If the search terms provided by the application consist of a string of characters containing one or more ? (question mark) as the wildcard character (e.g. E1?.?0, 005??ZZ), the system finds all ICD-10 codes that match the search terms, where a single alphanumeric character (including the “X” placeholder character for ICD-10-CM diagnosis codes) exists at the position where a ? exists in the search string.
- The ? (question mark) wildcard character can appear anywhere in the search string, and can appear more than once. The system does not match a null (blank) value where a ? exists at the end of the search string.
- If the search terms provided by the application consist of a string of characters containing both an \* and one or more ? as wildcard characters (e.g., E2?.1\*, 0SU?3\*), the system finds all ICD-10 codes that match the search terms, where zero or more alphanumeric characters exist at the position where the \* exists in the search terms and a single alphanumeric character exists at the position where a ? exists in the search string.
- The first 2 characters in the search string cannot consist of a wildcard character (\* or ?).
- The system provides the code and long description for each ICD-10 diagnosis or procedure matching the search terms.
- You can select one or more ICD-10 codes from the list of matching codes, using a list, range, or combination.
- When editing an Encounter Form, you can enter a partial code without using any wildcard characters (e.g., E08, 005), in order to select a group of ICD-10 codes all at once, with the individual ICD-10 codes and descriptions not displayed.
- Entering ^ saves your selection and exits the search.

A wildcard search entry works differently from a selection list. If you answer “Yes” to automatically select ICD-10 codes, then a selection list does NOT display. The selection automatically prompts you for the NEXT available ICD-10 code based on the wildcard entry that you entered.

Example

Select Action: Quit// AS Add Selection

SELECT ICD-10 DIAGNOSIS CODE NUMBER: E16\*

There are 7 ICD-10-CM diagnosis codes that begin with E16\*. Do you wish to

automatically add all of these diagnosis codes to this block? No// Y (Yes)

E16.0 Drug-induced hypoglycemia without coma

Select SELECTION GROUP HEADER: GROUP ONE 1 ICD-10 DIAGNOSES

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

Select SELECTION GROUP HEADER: GROUP ONE 1 ICD-10 DIAGNOSES

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

Ok? (Yes/No) Yes// YESSelect SELECTION GROUP HEADER: GROUP ONE 1 ICD-10 DIAGNOSESPRINT ORDER WITHIN GROUP: 5// 5Select a SECOND ICD-10 code to associate with the original:Select a THIRD ICD-10 code to associate with the original:Subcolumn Header: DIAGNOSISEdit Subcolumn 3: Hypoglycemia, unspecifiedNARRATIVE TO SEND TO PCE:CLINICAL LEXICON ENTRY: E16.2//Hypoglycemia, unspecified (ICD-10-CM E16.2)Ok? YES// YES Hypoglycemia, unspecified (ICD-10-CM E16.2)\>\>\> ICD-10-CM Code: E16.2Now for another!Automatic selection continued:7 Diagnosis Added.Drug-induced hypoglycemia without coma (ICD-10-CM E16.0)Other hypoglycemia (ICD-10-CM E16.1)Hypoglycemia, unspecified (ICD-10-CM E16.2)Increased secretion of glucagon (ICD-10-CM E16.3)Increased secretion of gastrin (ICD-10-CM E16.4)Other specified disorders of pancreatic internal secretion (ICD-10-CM E16.8)Disorder of pancreatic internal secretion, unspecified (ICD-10-CM E16.9)Enter RETURN to continue or '^' to exit:Please wait while I build the list............<u>Selection List Display Feb 14, 2012@15:53:30 Page: 1 of 1</u>This screen displays the selection list for 'ICD-10 DIAGNOSES (V1.0)'on Encounter Form 'TEST ONE CLINIC FORM'<u>CODE ORDER NARRATIVE</u>1 GROUP ONE1) S62.001A 1 Unsp fracture of navicular bone of right wrist, init2) S62.001D 2 Unsp fx navicular bone of r wrist, subs for fx w routn3) E16.0 3 Drug-induced hypoglycemia without coma4) E16.1 4 Other hypoglycemia5) E16.2 5 Hypoglycemia, unspecified6) E16.3 6 Increased secretion of glucagon7) E16.4 7 Increased secretion of gastrin8) E16.8 8 Other specified disorders of pancreatic internal secret9) E16.9 9 Disorder of pancreatic internal secretion, unspecifiedEnter ?? for more actions \>\>\>AS Add Selection FA Format All GE Group EditES Edit Selection GA Group Add RS Resequence GroupDS Delete Selection GC Group CopyPH New Place Holder GD Group DeleteSelect Action: Quit//

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>anchor marks</th>
<th>Cross-hair or angle marks appearing on a scannable form. They are used by the commercial scanning engine to align the form.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>block</td>
<td>A form is composed of blocks. Blocks are a rectangular region on the form. Attributes include position, size, outline type, and header. All other form components are contained within a particular block, and their position is relative to the block's position.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>bubbles</td>
<td>Marking areas on a form. They are filled in to indicate a selection, and will be read by the scanner.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>column</td>
<td>A selection list contains one or more columns, a column being a rectangular area that contains a portion of the entries on a selection list. Attributes include position and height.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>comb</td>
<td>Marking areas on a form to guide a user into entering one character per box.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>conversion</td>
<td><p>Refers to the conversion of forms designed using IB</p>
<p>V. 2.0 to forms that can be scanned.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CSV</td>
<td>Code Set Versioning. This package is mandated under the Health Information Portability and Accountability Act (HIPAA). It contains routines, globals and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD‑9‑CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, certain applications will allow users of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO)-established specific code that existed on that event date.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>data field</td>
<td>A block component that is the means by which data from V<em>IST</em>A is printed to the form, such as the patient's name. The data is obtained at the time the form is printed (i.e., it is not stored with the form) and can be particular to the patient. A data field can have subfields, which are conceptually a collection of related data fields. Attributes include label, label type (underline, bold, invisible), position, data area, data length and position (area on the form allocated to the data), item number, and package interface (the routine used to get the data).</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>data qualifiers</td>
<td>A selection list component. Example: with data qualifiers, a diagnosis can be designated as either primary or secondary.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>dynamic selection lists</td>
<td>Lists used to print the patient's active problems, insurance policies, providers assigned to the clinic, etc. Dynamic lists provide the capability of scanning data such as patient's active problems. They also provide an easier method of printing lists of data such as SC disabilities, as compared to using data fields.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>encounter form</td>
<td>A paper form used to display data pertaining to an outpatient visit and to collect additional data pertaining to that visit.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>entry action</td>
<td>An attribute of a package interface. It is MUMPS code that is executed before the interface's entry point is executed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>exit action</td>
<td>An attribute of a package interface. It is MUMPS code that is executed after the interface's entry point is executed.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>form line</td>
<td>A block component. A straight line that will be printed to the form. Attributes include orientation (horizontal, vertical), position, and length.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>form tracking</td>
<td>Tracks the processing status of forms. Each printed form will be assigned an ID, allowing it to be tracked while it's being processed. The lists of forms printed, their status, and statistics can be obtained from the Form Tracking option.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>hand print field</td>
<td>Allow input of hand printing.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span id="ICDp93" class="anchor"></span>ICD-10 codes</td>
<td>Replace the ICD-9-CM code set with ICD-10-CM with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 Activation Date.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>intelligent character recognition</td>
<td>(ICR) The ability to read hand written characters (usually printed) in combs or boxes.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>item number</td>
<td>An attribute that must be specified when defining a data field if the data field's package interface returns a list. The item number is used to specify which item on the list should be printed to the data field. For example, there is a package interface for returning service connected conditions. The first data field created for a form for displaying a service connected condition would specify item number one.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>operator fill field</td>
<td>A field that is completed by an operator once it’s scanned.</td>
</tr>
<tr class="odd">
<td>optical character recognition</td>
<td>(OCR) The ability for scanning software to read characters printed by a printer on a form.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>package interface</td>
<td>A table that is the method by which AICS interfaces with other packages. Presently there are three types of package interfaces: for printing reports via the print manager, printing data to data fields, and for entering data to selection lists. Attributes include entry point, routine, entry action, exit action, protected variables, required variables, data type, data description, and custodial package.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Paper Keyboard</td>
<td>A commercial scanning application, by Datacap, Inc., used to perform the scanning, recognition, and validation portions of the scanning process.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>place holders</td>
<td>A component of a selection list. They can contain text and serve as subheaders for the selections that follow within a group.</td>
</tr>
<tr class="even">
<td>print manager</td>
<td>The print manager is a utility used to define the reports and encounter forms that should be printed for clinics. It will then print the reports and forms in packets for each appointment specified.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>scannable</td>
<td>A form or marking area that is designed to be scanned and formatted; and defined to the scanning software.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>selection</td>
<td>A component of a selection list. It is a single entry on the list. It is stored with the form and usually consists of data taken from a file in V<em>IST</em>A such as a CPT code with its description.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>selection group</td>
<td>A component of a selection list. It is a named group of selections on the list. Attributes include a header and the print order.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>selection list</td>
<td>A block component whose purpose is to contain a list; for example, a list of CPT codes. The list contains subcolumns for marking areas, which are areas meant to be marked to indicate selections being made from the list. Attributes include headers, subcolumns, subcolumn width, subcolumn type, package interface (the routine used to fill the list), and many attributes for the appearance of the list.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>selection rule</td>
<td>There are a set of rules on the number of items that can be accepted for each list. For example, exactly one primary diagnosis and any number of secondary diagnoses can be specified.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>subcolumn</td>
<td>A component of a selection list. It can contain either text, such as a CPT code, or a marking area.</td>
</tr>
<tr class="odd">
<td>subfield</td>
<td>A component of a data field. It can display a single value, whereas a data field can be used to display a collection of related values. Attributes include those for the label and the area on the form to print the data. Also, for package interfaces that return records that have multiple values, the particular data must be specified.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>text area</td>
<td>A rectangular area in a block that is used to display a word-processing field. The text is automatically formatted to fit within the block. Attributes include the word-processing field, the position and size of the text area. The text is stored with the form.</td>
</tr>
</tbody>
</table>
Military Time Conversion Table
> STANDARD MILITARY
> 12:00 MIDNIGHT 2400 HOURS
> 11:00 PM 2300 HOURS
> 10:00 PM 2200 HOURS
> 9:00 PM 2100 HOURS
> 8:00 PM 2000 HOURS
> 7:00 PM 1900 HOURS
> 6:00 PM 1800 HOURS
> 5:00 PM 1700 HOURS
> 4:00 PM 1600 HOURS
> 3:00 PM 1500 HOURS
> 2:00 PM 1400 HOURS
> 1:00 PM 1300 HOURS
> 12:00 NOON 1200 HOURS
> 11:00 AM 1100 HOURS
> 10:00 AM 1000 HOURS
> 9:00 AM 0900 HOURS
> 8:00 AM 0800 HOURS
> 7:00 AM 0700 HOURS
> 6:00 AM 0600 HOURS
> 5:00 AM 0500 HOURS
> 4:00 AM 0400 HOURS
> 3:00 AM 0300 HOURS
> 2:00 AM 0200 HOURS
> 1:00 AM 0100 HOURS

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AICS Data Entry Menu
> *With functionality put in place by the Code Set Versioning project, the options in this Menu have been deleted from AICS.*
<span id="ICDp97" class="anchor"></span>Background EF Print Special Instructions (Appendix A) 99
Clinic Setup/Edit Forms 7
Clinics With No Encounter Forms 78
Copy CPT Check-off Sheet to Encounter Form 15
Define Available Health Summary 29
Define Available Report (not Health Summaries) 47
Device Edit 64
Edit Clinic Reports 27
Edit Division Reports 25
Edit Encounter Forms 7
Edit Marking Area (for selection lists) 45
Edit Package Interface 39
Edit Site Parameters 67
Edit Tool Kit 34
Edit Tool Kit Blocks 34
Edit Tool Kit Forms 36
Encounter Form IRM Options 39
Form Components 66
Forms Tracking 71
Glossary 91
HP LaserJet 5Si Printer (Appendix D) 109
ICD-10 Search Functionality 85
Import/Export Utility 51
Introduction 1
List Clinics Using Forms 74
List Manager (Appendix B) 105
Maintenance Utility for Active/Inactive Codes 75
Miscellaneous Cleanup 63
Most Commonly used Outpatient CPT Codes 16
Orientation 3
Package Management 5
Package Operation 7
Print Blank Encounter Form 23
Print Encounter Forms for Appointments 18
Print Form w/Patient Data, No Appt 21
Print Manager 25
Print Options 18
Print Sample of all Forms 79
Purge Form Tracking files 65
Recompile All Forms 62
Report Clinic Setups 30, 82
Reports and Utilities 66
Revision History i
Scanning (Appendix C) 107
Scanning Error Listing 70
Setup Automatic Print Queues 31

# Appendix A - Background EF Print with Special Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release of AICS V. 2.1 enabled you to print encounter forms through the use of several options, one of which is the Background EF Print option. In order for this option to work, you must set parameters to run the job. Some of the main parameters that run this job are listed below. You can set up multiple jobs, each with its own set of parameters.

Last Date Printed

This parameter contains the date of the last day for which encounter forms were printed.

Days To Print Ahead

This parameter stores the number of days ahead (from the date the job is queued) for which the encounter forms should be printed.

Special Instructions

This parameter is required when setting up individual encounter form print jobs for a facility using the Background EF Print option. Use the Setup Automatic Queues option on the Print Managers menu to set this parameter from the following choices. Brief scenarios are provided for those involving weekends and holidays.

*Note: This parameter is a very important one and should be well understood in order for the printing to be done correctly and encounter forms to be printed when they are supposed to.*

R - Run Regardless When the parameter is set to this value, the print job will run daily at the scheduled time, regardless of what day of the week it is or whether it is a holiday when no clinics meet.

N - Not Active When the parameter is set to this value, the job is considered inactive and no encounter forms will print.

T - Today When the parameter is set to this value, encounter forms will print for today only. The Days to Print Ahead parameter should be set to zero.

I - Ignore Both When the parameter is set to this, if the day the

Weekends and job is queued to run is a weekend day or a holiday,

Holidays the job will abort. It also checks the day for which the encounter forms are to be printed. If it is a weekend day or a holiday, the job will keep going until it finds a regular work day. It will then print the encounter forms for the regular work day and quits.

*\*\*Include weekends and holidays in counting the number of days ahead!\*\

*<u>Scenario 1</u>The facility will be printing encounter forms three days in advance with the Special Instructions parameter set to Ignore Both Weekends and Holidays.*Day queued Day to be printed (+3)=========== ===============

Monday Thursday

Tuesday Friday

Wednesday Saturday, Sunday, Monday (holiday), Tuesday

Since the forms print three days in advance, on Wednesday the forms for Saturday should be printed. This is a weekend day, and according to the special instructions, should be ignored. The job checks the Last Date Printed parameter and will try to print this day if the day to be printed is after the last date that encounter forms were printed. No encounter forms will be printed since no appointments are scheduled for this day. The queue will then check the next day and see if it is a weekend day or a holiday. Sunday is a weekend day and a day after the Last Date Printed; therefore, the job queues off but no encounter forms are printed because nothing is scheduled for this day. The job will then check the next day to see if it is a regular work day and not a weekend day or holiday and print forms if there are any for that day. The Monday, for our example, will be a holiday and a day after the Last Date Printed so the job is queued but nothing prints for this day either. The queue will then check the next day for a regular workday...Tuesday, and print encounter forms for that day.

The system will then update the Last Date Printed and quit the job. The job will run until it finds the first regular work day and prints the encounter forms for that day.

Thursday Wednesday

On Thursday, the forms for Sunday should normally print. It is a weekend day and a date before the Last Date Printed; therefore, the job prints nothing for this day. It looks for the next day...Monday...it's a holiday and before the Last Date Printed... nothing prints. It then looks to the next day...Tuesday...the day of the Last Date Printed...nothing prints for this day since the encounter forms have already been printed for this day. It then looks to the next day...Wednesday, and prints that day’s encounter forms and updates the Last Date Printed parameter. It then quits the job.

Friday Thursday

It is supposed to print Monday the holiday, but Monday has already been taken care of and it's before the Last Date Printed so it ignores that and also ignores Tuesday and Wednesday because encounter forms have already been printed for those days because the Last Date Printed is Wednesday; therefore, Thursday is the next day to print encounter forms for.

Saturday Nothing prints. The job stops immediately because it is a weekend day.

Sunday Nothing prints. The job stops immediately because it is a weekend day.

Monday (holiday) Nothing prints. The job stops immediately because it is a holiday.

Tuesday Friday

Wednesday Sat, Sun, Mon.

Thursday Tuesday

Friday Wednesday

Saturday Nothing prints.

Sunday Nothing prints.

Monday Thursday

At this point, you are back on a schedule.

W - Ignore Weekends When the parameter is set to this, if the day the job is queued for a weekend day, the job will abort. It also checks the day that the encounter forms are to be printed for. If it is a weekend day the job will keep going until it finds a regular work day and prints forms for it. The job then quits.

*\*\*Include weekends in counting the number of days ahead!\*\

*<u>Scenario 2</u>The facility will be printing encounter forms three days in advance with the Special Instructions parameter set to Ignore Weekends.*Day queued Day to be printed (+3)=========== ===============

\*Monday Thursday

\*Tuesday Friday

\*Wednesday Saturday, Sunday, Monday

Thursday Tuesday

Friday Wednesday

Saturday Nothing prints. The job stops immediately because it is a weekend day.

Sunday Nothing prints. The job stops immediately because it is a weekend day.

Monday Thursday

*\*Same explanation as Scenario 1.*

H - Ignore Holidays When the parameter is set to this, if the day the job is queued for is a holiday, the job will abort. It also checks the day that the encounter forms are to be printed for. If it is a holiday, the job will keep going until it finds a regular work day and prints forms for it. The job then quits.

*<u>Scenario 3</u>The facility will be printing encounter forms three days in advance with the Special Instructions parameter set to Ignore Holidays.*Day queued Day to be printed (+3)=========== ===============

Monday Thursday

Tuesday Friday

Wednesday Saturday

Thursday Sunday

Friday Monday (holiday), Tuesday

Saturday Wednesday

Sunday Thursday

Monday Nothing prints, and the job is stopped immediately because it is a holiday.

Tuesday Friday

Wednesday Saturday

Thursday Sunday

Friday Monday

Saturday Tuesday

Sunday Wednesday

Monday Thursday

# Appendix B - List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager is a tool that displays a list of items in a screen format and provides you the following functionality.

> browse through the list

> select items that need action

> take action against those items

> select other List Manager actions without leaving the option

A plus sign (+) at the bottom of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) might be displayed to indicate there is additional information to the left or right on the screen. Actions(s) are entered by typing the name(s), or abbreviation(s) at the "Select Action" prompt. Actions can be preselected by separating them with a semicolon (;). For example, "AL;CI" (Appointment Lists;Checked In) will advance through the two actions automatically.

Entries can be preselected in the following manner.

CI=1 will process entry 1 for check in

CI=3 4 5 will process entries 3, 4, 5 for check in

CI=1-3 will process entries 1, 2, 3 for check in

In addition to the various actions that can be available specific to the option you are working in, List Manager provides generic actions applicable to any List Manager screen. You can enter a double question mark \<??\> at the "Select Action" prompt for a list of all actions available. On the following page is a list of generic List Manager actions with a brief description. The abbreviation for each action is shown in brackets \[\] following the action name. Entering the abbreviation is the quickest way to select an action.

Action Description

Next Screen \[+\] move to the next screen

Previous Screen \[-\] move to the previous screen

Up a Line \[UP\] move up one line

Down a Line \[DN\] move down one line

Shift View to Right \[\>\] move the screen to the right if the screen width is more then 80 characters

Shift View to Left \[\<\] move the screen to the left if the screen width is more then 80 characters

First Screen \[FS\] move to the first screen

Last Screen \[LS\] move to the last screen

Go to Page \[G0\] move to any selected page in the list

Re Display Screen (RD) redisplay the current screen

Print Screen \[PS\] prints the header and the portion of the list currently displayed

Print List \[PL\] prints the list of entries currently displayed

Search List \[SL\] finds selected text in list of entries

Auto Display(On/Off) \[ADPL\] toggles the menu of actions to be displayed/not displayed automatically

Quit \[QU\] exits the screen

# Appendix C - Scanning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With functionality put in place by the Code Set Versioning project, Scanning and Manual Data Entry (MDE) functionality in AICS is terminated. This shutdown is for the following reasons.

1\. Because this functionality is no longer being enhanced, it is not compatible with the new diagnostic and procedure codes as defined by HIPAA. If Scanning & MDE are allowed to continue, encounter data may be rejected which would result in the generation of application errors.

2\. VHA DIRCTIVE 2003-012.

> a\. All facilities should only be using "electronic encounter forms" by October 1, 2003.

> b\. All providers should enter their own encounter data using CPRS by October 1, 2003.

3\. CPRS is now the method of choice for entering outpatient encounter data.

# Appendix D - HP LaserJet 5Si Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the addition of scanning to the AICS package, a need for duplex printing, and the need for a printer that could handle high volume printing as well as print pages that would be scannable and compatible with the AICS workstation software, the HP LaserJet 5Si printer was purchased. This printer prints 24 ppm ( pages per minute), handling a wide variety of paper weights and sizes. Three input paper trays and two output bins handle a variety of print media. The HP LaserJet 5Si comes with 4 Mbytes of memory with the potential to expand memory to 132 Mbytes, and the potential to add additional printer features with four single inline memory module (SIMM) slots. Thirty five scaleable fonts as well as 10 True Type fonts are included in this printer. Some additional options have been purchased with the HP LaserJet 5Si that add to the capability and efficiency of this printer. They are an envelope feeder, duplex unit for printing 2 sided documents, 2000 sheet input tray (tray 4) and a multi-bin mailbox ( works in mailbox, job separation and stacking mode).

Software is included with the HP LaserJet 5Si and must be installed on each individual PC that will be using the printer. If running windows, a new printer will need to be set up in order to use the device. There are additional parameters and definitions that must be setup in order for the printer to be workable and usable to print AICS encounter forms and duplex printing. Due to many differing factors and variables at each site (wiring/connector schemes, terminal server configurations, sysgen definitions, physical device set ups, VMS print queues, etc.) it is hard to standardize one combination of successful printer setups, device and terminal type definitions for printing Encounter Forms and subsequent output reports (action profile, health summary, etc.). It is very important to remember that each unique Terminal Type, (Device Subtype) must be defined in the Encounter Form Printers file (357.94) with Printer Language Type equal to PCL5.

The following definitions and parameters need to be set up before using the printer :

1.  Physical Device Information/Set-up,
2.  Terminal Type File,
3.  Device File,
4.  Encounter Form Printers File.
1) PHYSICAL DEVICE INFORMATION/SET-UP - Control Panel Menu

The following information is included in the printer and can be obtained by printing from the printer itself. These are the default settings for the printer. They may be changed to accommodate your site. This information is contained on the Configuration page which can be printed out by doing the following.

Press Menu - Select Test Menu

Press Item - PCL Configuration Page

Press Select - this will print the configuration Page

The following information is included on this printout.

Printer Information

Serial Number: USDF015318

Formatter Number: EA48XB

Firmware Datacode: 19960208 v8_5

Processor Revision: 29040 D40d

Page Count: 32

Pages Since Last Power Cycle: 0

Pages Since Last Maintenance: 32

Installed Personalities and Options

PCL (19960208)

Postscript (19951204) \*

SIMM Slot 1: Empty

SIMM Slot 2: Empty

SIMM Slot 3: 8 MByte RAM SIMM

SIMM Slot 4: 1 MByte ROM SIMM

Memory

Total Memory: 12 Mbytes

Available Memory: 7.9 Mbytes

I/O Buffering

Not Enabled - Need: 11 Mbytes More Memory

Resource Saving:

Not Enabled - Need: 12 Mbytes More Memory

Security

Control Panel Lock: DISABLED

Control Panel Password: DISABLED

Paper Handling Options

Duplex Unit

PH Controller \[01.51\]

Device 1:

HEWLETT-PACKARD 2000 SHEET INPUT TRAY C3763A

1: Tray 4, 2000 sheets

Device 2:

HEWLET -PACKARD MULTIBIN MAILBOX C3764A \[BNP43.90\]

1: OPTIONAL OUTBIN 1. 125 Sheets, Face Up

2: OPTIONAL OUTBIN 2. 250 Sheets, Face Down

3: OPTIONAL OUTBIN 3. 250 Sheets, Face Down

4: OPTIONAL OUTBIN 4. 250 Sheets, Face Down

5: OPTIONAL OUTBIN 5. 250 Sheets, Face Down - Only if you have Multi-bin

6: OPTIONAL OUTBIN 6. 250 Sheets, Face Down option.

7: OPTIONAL OUTBIN 7. 250 Sheets, Face Down

8: OPTIONAL OUTBIN 8. 250 Sheets, Face Down

9: OPTIONAL OUTBIN 9. 250 Sheets, Face Down

This information is contained on the TRAY MENU page of the printer which can also be printed.

TRAY MENU

TRAY 1 TYPE = PLAIN

TRAY 1 SIZE = LETTER

TRAY 2 TYPE = PLAIN

TRAY 3 TYPE = PLAIN

TRAY 4 TYPE = PLAIN

JOB CONTROL MENU

CANCEL JOB

PRESS SELECT TO FORM FEED

TEST MENU

PCL CONFIGURATION PAGE

POSTSCRIPT CONFIGURATION PAGE - may not contain this if printer doesn’t

> have postscript option

PCL FONT LIST

POSTSCRIPT FONT LIST - may not contain this if printer doesn’t have postscript

option

DEMO PAGE

PRINT ERROR LOG

PAPER PATH TEST

SHOW ERROR LOG

CONFIGURATION MENU

2-SIDED = OFF

PAPERDESTINATION = TOP OUTPUT BIN

ORIENTATION = PORTRAIT

POWER SAVE DELAY = 1 HOUR

PERSONALITY = AUTO

AUTO CONTINUE = ON

TONER LOW = STOP - this setting is highly recommended for paper saving.

PRINT QUALITY MENU

ECONOMODE = OFF

RESOLUTION = 600 DOTS PER INCH

RESOLUTION ENHANCEMENT = ON

PRINT DENSITY = 5

POSTSCRIPT MENU - may not contain this if printer doesn’t have postscript option

PRINT POSTSCRIPT ERRORS = OFF

JAME RECOVERY = OFF

IO MENU

PARALLEL ID SPEED = HIGH

IO TIMEOUT = 15 SECONDS

  
HP MIO1 MENUHP MIO2 MENU

Serial=RS232

Baud Rate=9600

Handshk=XON

DTR Polarity=Hi

Data Bits=8

Parity=None

Stop Bits=1

  
2) TERMINAL TYPE FILE (# 3.2)

With each new printer (device), there should be an associated entry in the Terminal Type file. This file is pointed to by the Subtype field of the Device file. The fields that need to be populated in this file will vary depending on what the printer is being used for. This file may hold vendor-specific code to characterize a terminal type. For example, escape sequences may be entered in the Open and Close Execute fields to set pitch or font. The following are some of the more standard fields that will be set up.

NUMBER: XXX NAME: P-HPLASERJ5-16/8/UP/DUPLEX

SELECTABLE AT SIGN-ON: YES RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 80

BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"E",\*27,"(s16.66H",\*27,"&l8D"

CLOSE EXECUTE: W \*27,"E"

DESCRIPTION: LASER JET W/16.66 PITCH & 8 LPI (UPRIGHT)

SIMPLEX: \$C(27)\_”&l0S”// - l is lower case “L”, 0 is zero.

DUPLEX, LONG EDGE BINDING: \$C(27)\_”&l1S”// - first 1 is lower case “L”,

second 1 is \#1.

DUPLEX, SHORT EDGE BINDING: \$C(27)\_”&l2S”// - l is lower case “L”.

\<\<\<If the printer is being used for graphics, the graphics fields need to be set up.\>\>

\<\<\<The EXAMPLES section will show some successful working configurations of Terminal Types and Devices being used at some sites.\>\>\>

  
3) DEVICE FILE (# 3.5)

With each new printer, an entry must be made in the Device file (# 3.5). This file defines all input/output devices that can be accessed from a CPU (definitions are not account-specific). Each device is identified with a unique name. Each is associated with a \$I value which may correspond with a hardware port or, on layered systems, a host file or directory. If there are several devices for the same volume set and \$I, one may be given sign-on system status. Devices may also be assigned to hunt groups to share work. The following are some of the more standard fields that will be set up.

NUMBER: site specific\* NAME: site specific\*

\$I: XXX ASK DEVICE: YES

ASK PARAMETERS: YES VOLUME SET(CPU): PSA

LOCATION OF TERMINAL: SCHEDULING CLERK

SUPPRESS FORM FEED AT CLOSE: YES \*MARGIN WIDTH: 132

\*FORM FEED: \# \*PAGE LENGTH: 80

\*BACK SPACE: \$C(8) SUBTYPE: P-HPLASERJ5-

16/8/UP/DUPLEX

TYPE: TERMINAL

EQUINOX BOX (c): site specific\* EQUINOX PORT (c): site

> specific\*

EQUINOX BOX-PORT (c): site specific\*

\<\<\<The EXAMPLES section shows some successful working configurations of Terminal Types being used at some sites.\>\>\>

  
4) ENCOUNTER FORM PRINTERS FILE (# 357.94)

With each unique printer (Terminal Type), an entry must be made in the Encounter Form Printers file to allow the site to print encounter forms and duplex print. The printer’s Terminal Type name will be the entry name for this file. This file contains a list of terminal types that can support either duplex printing or the printer control language PCL5. Entering the correct information in this file will allow encounter forms printed to these terminal types to utilize these features. There is a standard setup that the site must enter into this file. The following parameters should be set up exactly as follows.

TERMINAL TYPE: Should be the Terminal Type name.

PRINTER LANGUAGE TYPE: PCL5// - This must be set to PCL5 in order to print

Encounter Forms

SIMPLEX: \$C(27)\_”&l0S”// - l is lower case “L”, 0 is zero.

DUPLEX, LONG EDGE BINDING: \$C(27)\_”&l1S”// - first 1 is lower case “L”,

second 1 is \#1.

DUPLEX, SHORT EDGE BINDING: \$C(27)\_”&l2S”// - l is lower case “L”.

General information:

W \*27,"E" resets the printer to the user defaults, not the factory defaults; so if a user makes any changes on the menu front control panel, the printer resets to these selected parameters.

In composing an escape code sequence, a W \*27,"&l" needs to be issued once followed by the parameter string.

The 4Si and 5Si escape codes work the same, with the 5Si having more features.

  
EXAMPLES

This section lists some of the configurations that have shown to be successful for printer setups in the Terminal Type file and Device file for the HP5Si. Each site may need to modify the configurations to get the most successful printer/device/ terminal type definitions to print Encounter Forms and duplex print. The Encounter Form Printers file for each of these, is set up with the standard configuration listed under the ENCOUNTER FORM PRINTERS FILE (#357.94) section.

Device File (#3.5)

NAME: ENCOUNTER FORM PRINTER \$I: 0

ASK DEVICE: YES ASK PARAMETERS: YES

LOCATION OF TERMINAL: MAUNETTE'S OFFICE

\*MARGIN WIDTH: 132 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

MNEMONIC: EF

SUBTYPE: P-HPLASER/16/8/UP/DUPLEX TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type file (#3.2)

NAME: P-HPLASER/16/8/UP/DUPLEX SELECTABLE AT SIGN-ON:YES

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

\*OLD XY CRT: W \$C(27)\_"&a"\_DX\_"c"\_DY\_"R"

OPEN EXECUTE: W \*27,"E",\*27,"(s16.66H",\*27,"&l8D"

CLOSE EXECUTE: W \*27,"E"

DESCRIPTION: Laser Jet w/16.66 pitch and 8 lines per inch (Upright)

TOP LEFT CORNER: \$C(218) BOTTOM LEFT CORNER: \$C(192)

TOP RIGHT CORNER: \$C(191) BOTTOM RIGHT CORNER: \$C(217)

VERTICAL LINE: \$C(179) HORIZONTAL LINE: \$C(196)

GRAPHICS OFF: \$C(27)\_"(8U" GRAPHICS ON: \$C(27)\_"10U"

XY CRT: W \$C(27)\_"&a"\_DX\_"c"\_DY\_"R"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
For a typical MSM site the General site configuration statistics are as follows.MSM v4.0.14Equinox Terminal ServersHP 4/5Si Printers\<\<\<\<Note that sites are similar in configurations but may vary.\>\>\>\>

The following device types followed by their corresponding Terminal Type definitions are used by MSM sites (used with HP 4/5Sis).

Device

NAME: P21-22 STACKING SET \$I: 303

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: MIS RM A9

DEFAULT SUBTYPE: P-HP5SI STACKING MODE

\*MARGIN WIDTH: 80 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

SUBTYPE: P-HP5SI STACKING MODE TYPE: TERMINAL

-----------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HP5SI STACKING MODE SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,\*38,\*108,"2",\*73

DESCRIPTION: SETS HPSI PRINTERS TO STACKING MODE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: P21-22A \$I: 303

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: MIS RM A9

DEFAULT SUBTYPE: P-HPLASERIV 10X80/8X80

\*MARGIN WIDTH: 80 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

MNEMONIC: P4-42A

SUBTYPE: P-HPLASERIV 10X80/8X80 TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASERIV 10X80/8X80 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"(s10H",\*27,"&l8D"

10 PITCH: \$C(27)\_"(s10H" 12 PITCH: \$C(27)\_"(s12H"

DESCRIPTION: -HPLASER IV 10 cpi 80 colms 8 lpi 80 lines/page

16 PITCH: \$C(27)\_"(s16.66H" 6 LINES PER INCH: \$C(27)\_"&l6D"

8 LINES PER INCH: \$C(27)\_"&l8D"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: P21-22B \$I: 303

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: MIS RM A9

DEFAULT SUBTYPE: P-HPLASER-P10 \*MARGIN WIDTH: 80

\*FORM FEED: \# \*PAGE LENGTH: 60

\*BACK SPACE: \$C(8)

MNEMONIC: P4-42B

SUBTYPE: P-HPLASER-P10 TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASER-P10 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 60 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"E" CLOSE EXECUTE: W \*27,"E"

10 PITCH: \$C(27)\_"k12H" 12 PITCH: \$C(27)\_"k10H"

UNDERLINE ON: \$C(27,38,100,48,68) UNDERLINE OFF: \$C(27,38,100,64)

DESCRIPTION: LASER PRINTER PORTRAIT MODE 10 CPI

16 PITCH: \$C(27)\_"k16.66H"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: P21-22E BAR \$I: 303

LOCATION OF TERMINAL: MIS

DEFAULT SUBTYPE: P-HPLASERIV 12X96/8X80 BAR

\*MARGIN WIDTH: 96 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

BARCODE AVAIL: YES SUBTYPE: P-HPLASERIV 12X96/8X80

BAR

TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASERIV 12X96/8X80 BAR SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 96 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l8D",\*27,"(s12H"

CLOSE EXECUTE: W \#

BAR CODE OFF: \*27,"E",\*27,"&l8D",\*27,"(s12H"

BAR CODE ON: \*27,"E",\*27,"&l0O",\*27,"(0Y",\*27,"(s0p12.00v4.69h0s0b0T"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: P21-22ENC/BAR \$I: 303

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: MIS

DEFAULT SUBTYPE: P-HPLASER 17X132/8X80 BAR

\*MARGIN WIDTH: 132 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

SUBTYPE: P-HPLASER 17X132/8X80 BAR TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASER 17X132/8X80 BAR SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,"&l5.8C"

CLOSE EXECUTE: W \# 6 LINES PER INCH: \$C(27)\_"&l6D"

8 LINES PER INCH: \$C(27)\_"&l8D"

BAR CODE OFF: \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,"&l5.8C"

BAR CODE ON: \*27,"&l0O",\*27,"(0Y",\*27,"(s0p12.00v8.11h0s0b0T"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: P21-22I \$I: 303

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: MIS RM A9

DEFAULT SUBTYPE: P-HPLASERIV 17X132/8X80

\*MARGIN WIDTH: 132 \*FORM FEED: \#

\*PAGE LENGTH: 80 \*BACK SPACE: \$C(8)

MNEMONIC: P4-42

SUBTYPE: P-HPLASERIV 17X132/8X80 TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASERIV 17X132/8X80 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l8D",\*27,"(s16.66H"

CLOSE EXECUTE: W \*27,"E" 10 PITCH: \$C(27)\_"(s10H"

12 PITCH: \$C(27)\_"(s12H"

DESCRIPTION: P-HPLASER IV 17 cpi 132 colms 8 lpi 80 lines/page

16 PITCH: \$C(27)\_"(s16.6H"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: E104 \$I: 198

ASK DEVICE: YES ASK PARAMETERS: YES

VOLUME SET(CPU): PSA

LOCATION OF TERMINAL: SP MAS HP4Si Bot/Duplex EQSPA20

DEFAULT SUBTYPE: P-HP4SI-16/8-BOT-DUPLEX

KEY OPERATOR: DSV4020 \*MARGIN WIDTH: 132

\*FORM FEED: \# \*PAGE LENGTH: 80

\*BACK SPACE: \$C(8)

SUBTYPE: P-HP4SI-16/8-BOT-DUPLEX TYPE: TERMINAL

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HP4SI-16/8-BOT-DUPLEX SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W

\*27,"E",\*27,"(8U",\*27,"(s0p16.67h8.5v0s0b0T",\*27,"&l8D",\*27,"&

l2G" CLOSE EXECUTE: W \*27,"E"

DESCRIPTION: HP4Si,16cpi,8Lpi,Stacker/Duplex

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*For a typical AXP site the General site configuration statistics are as follows:VMS v 6.2DSM v 6.4DecServer 550 and 90L terminal serversHP 4/5Si Printers\<\<\<Note that sites are similar in configurations but may vary.\>\>\>

The following setups are taken from AXP (Alpha) sites:

Device File

NUMBER: 670 NAME: SURGERY CLIN ENCOUNTER

\$I: \_LTA9302: LOCATION OF TERMINAL: 101-66

SUPPRESS FORM FEED AT CLOSE: YES NEAREST PHONE: 2671

\*MARGIN WIDTH: 132 \*FORM FEED: \#

\*PAGE LENGTH: 60 \*BACK SPACE: \$C(8)

MNEMONIC: OUTPATIENT-NURSING

SUBTYPE: P-HPLASER-6/16 TYPE: TERMINAL

LAT SERVER NODE: NJA023943 LAT SERVER PORT: PORT_1

BAUD RATE (c): UNKNOWN

------------------------------------------------------------------------------------------------------------------

Terminal Type

NUMBER: 221 NAME: P-HPLASER-6/16

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 60 BACK SPACE: \$C(8)

OPEN EXECUTE: W

\*27,\*38,\*108,\*54,\*68,\*27,\*38,\*107,\*50,\*83,\*27,\*38,\*108,\*48,\*79

CLOSE EXECUTE: W \*27,"E" HIGH INTENSITY

> (BOLD):\$C(27)\_"(s3B"

NORMAL INTENSITY (RESET): \$C(27)\_"(s0B"

DESCRIPTION: HPLASER 6 LPI 16 CPI

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Device

NAME: MAS15-5 ENC \$I: \_LTA9155:

ASK DEVICE: NO SIGN-ON/SYSTEM DEVICE: NO

LOCATION OF TERMINAL: B-59 SUPPRESS FORM FEED AT CLOSE: YES

NEAREST PHONE: 1803 KEY OPERATOR: DENISE

\*MARGIN WIDTH: 132 \*FORM FEED: \#

\*PAGE LENGTH: 83 \*BACK SPACE: \$C(8)

SUBTYPE: P-HPLASER4SI-16.6-ENC-FORM TYPE: TERMINAL

LAT SERVER NODE: M60715 LAT SERVER PORT: PORT_5

VMS DEVICE TYPE: NOT SPOOLED LAT PORT SPEED: 192

------------------------------------------------------------------------------------------------------------------

Terminal Type

NAME: P-HPLASER4SI-16.6-ENC-FORM RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 60

BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l8D",\*27,"(s16.66H"

CLOSE EXECUTE: W \*27,"E" 10 PITCH: \$C(27)\_"(s10H"

12 PITCH: \$C(27)\_"(s12H"

HIGH INTENSITY (BOLD): \$C(27,40,115,53,66)

NORMAL INTENSITY (RESET): \$C(27,40,115,48,66)

DESCRIPTION: HP4SI at 16.6 pitch 16 PITCH: \$C(27)\_"(s16.6H"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This setup works for printing bar-codes on Action Profiles that print with encounter forms.

In order to print bar-codes on Pharmacy Action Profiles that print with AICS Encounter Forms, the following example describes the BAR CODE OFF (#61) and BAR CODE ON (#60) fields in the TERMINAL TYPE file (#3.2) as well as the associated DEVICE file (#3.5) entry for either a HP 4Si or HP 5Si printer:

Device File Entry - Please note that this example is for a TCP/IP (network printer).

NAME: EF\$PRT \$I: VA7\$:\[TCP\$SPOOL\]EF\$PRT.TXT

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: MCCR AREA ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO \*MARGIN WIDTH: 132

\*FORM FEED: \# \*PAGE LENGTH: 80

\*BACK SPACE: \$C(8)

OPEN PARAMETERS: (NEWVERSION,PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED))

SUBTYPE: P-AICS BARCODE TYPE: HOST FILE SERVER

Terminal Type File Entry

NAME: P-AICS BARCODE SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,"&l

5.8C"

CLOSE EXECUTE: W \*27,"E" C IO K IO(1,IO) S

QUE="/QUEUE="\_\$E(ION,1,\$F(ION

,"PRT")-1)\_"/DELETE",QUE=\$ZC(%PRINT,IO,QUE)

DESCRIPTION: Laser Jet with 16.66 pitch and 8 lines per inch (Upright)

6 LINES PER INCH: \$C(27)\_"&l6D" 8 LINES PER INCH: \$C(27)\_"&l8D"

SIMPLEX: \$C(27)\_"&l0S"

DUPLEX, LONG EDGE BINDING: \$C(27)\_"&l1S"

DUPLEX, SHORT EDGE BINDING: \$C(27)\_"&l2S"

BAR CODE OFF: \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,"&l5.

8C"

BAR CODE ON: \*27,"&l0O",\*27,"(0Y",\*27,"(s0p12.00v8.11h0s0b0T"

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Selecting different bins for a multi-bin mailbox:

The OPEN EXECUTE for the Terminal Type file should be set to the following.

Top output bin:

OPEN EXECUTE: W \*27,”&l1G” - First l - lower case L, second 1 - number 1

Left output bin:

OPEN EXECUTE: W \*27,”&l2G” - First l - lower case L

Printer has a mail box:

OPEN EXECUTE: W \*27,”&l3G” - First l - lower case L

\<\<\<The user must manually set the stacker to stacker mode on the printer control panel and turn the printer off, then on again. This sets the stacker to on. The OPEN EXECUTE codes can redirect the output.\>\>\>

The only other way the stacker can be set without turning the printer off then on again is if the printer is set up as a network printer, and from Windows the JetAdministrator software is used to switch the modes.

\<\<\<Once the stacker mode is enabled, you can check this by printing the configuration page for the printer. Under Paper Handling, you should see the configuration for the bins.\>\>\>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Following is a general sample for setting up a network printer to print Encounter Forms.

This is a sample configuration listing for a network printer to be used to print Encounter Forms on an AXP system. The printer in this example is a HP 5Si with JetDirect card installed. For VMS and UCX setups, please refer to the published documentation on configuring client services, VMS queues, etc.

1. UCX setup

Digital TCP/IP Services for Open VMS CLIENT Components Configuration Menu

Configuration options:

1 - FTP Enabled

2 - LPR/LPD Enabled \<=== this option must be enabled

3 - NFS Client Disabled

4 - REXEC and RSH Disabled

5 - RLOGIN Disabled

6 - SMTP Disabled

7 - TELNET Enabled

A - Configure options 1 - 7

\[E\] - Exit menu

UCX Printer Setup Program

Command \< add delete view help exit \>: v

\#

\# LOCAL PRINTERS

\#

UCX\$LPD_QUEUE:\\

:lp=UCX\$LPD_QUEUE:\\

:sd=UCX\$LPD_SPOOL:

\#

\# setup using queue names with \$prt suffix

EF\$PRT\|ef\$prt:\\

:lf=/SYS\$SPECIFIC/UCX_LPD/EF\$PRT.LOG:\\

:lp=EF\$PRT:\\

:ps=lps:\\

:rm=ef\$prt:\\

:sd=/SYS\$SPECIFIC/UCX_LPD/EF\$PRT:

\#

  
2. VMS setup

Server queue EF\$PRT, idle, on ISC1A2::, mounted form DEFAULT

/AUTOSTART_ON=(ISC1A2::,ISC1A1::) /BASE_PRIORITY=4

/DEFAULT=(FEED, FORM=DEFAULT) /PROCESSOR=UCX\$LPD_SMB

3. VISTA setup

DEVICE file (#3.5) entry -

NAME: EF\$PRT \$I: VA7\$:\[TCP\$SPOOL\]EF\$PRT.TXT

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: MCCR AREA ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO \*MARGIN WIDTH: 132

\*FORM FEED: \# \*PAGE LENGTH: 80

\*BACK SPACE: \$C(8)

OPEN PARAMETERS: (NEWVERSION,PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED))

SUBTYPE: P-AICS BARCODE TYPE: HOST FILE SERVER

TERMINAL TYPE file (#3.2) entry -

NAME: P-AICS BARCODE SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 80 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,

"&l5.8C"

CLOSE EXECUTE: W \*27,"E" C IO K IO(1,IO) S QUE="/QUEUE="\_\$E(ION,1,\$F

(ION,"PRT")-1)\_"/DELETE",QUE=\$ZC(%PRINT,IO,QUE)

DESCRIPTION: Laser Jet with 16.66 pitch and 8 lines per inch (Upright)

6 LINES PER INCH: \$C(27)\_"&l6D" 8 LINES PER INCH: \$C(27)\_"&l8D"

SIMPLEX: \$C(27)\_"&l0S" DUPLEX, LONG EDGE BINDING:

\$C(27)\_"&l1S"

DUPLEX, SHORT EDGE BINDING: \$C(27)\_"&l2S"

BAR CODE OFF: \*27,"&l0O",\*27,"(8U",\*27,"(s0p9.42v16.67h0s0b6T",\*27,"&l5.8C"

BAR CODE ON: \*27,"&l0O",\*27,"(0Y",\*27,"(s0p12.00v8.11h0s0b0T"

ENCOUNTER FORM PRINTER file (#357.94) entry -

TERMINAL TYPE: P-AICS BARCODE

PRINTER LANGUAGE TYPE: PCL5

SIMPLEX: \$C(27)\_"&l0S"

DUPLEX, LONG-EDGE BINDING: \$C(27)\_"&l1S"

DUPLEX, SHORT-EDGE BINDING: \$C(27)\_"&l2S"

TCP PRINTER: YES

\<\<\< W \*27 is used in some setups. While “W \*” is ANSI standard, implementation is vendor and device specific; therefore, it is not entirely portable.\>\>\>

> Reference: SAC2.1. ANSI standard p. 68