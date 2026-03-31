---
title: RMPR*3*168 ICD - 10 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ICD - 10
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*168
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - table
  - contents
  - prosthetics
  - diagnosis
  - description
  - date
  - codes
  - vendor
  - cocaine
page_count: 0
word_count: 3269
section_count: 14
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/icd-10_rn_rmpr_3_168.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/icd-10_rn_rmpr_3_168.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

ICD-10 Follow On Class 1 Software Remediation Project

Prosthetics

ICD-10 Release Notes

RMPR\*3.0\*168

![](rmpr-3-168-icd-10-release-notes/001.png)

Application Version 3.0

August 2014

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
  - [Dependencies](#dependencies)
- [Prosthetics Roll and Scroll](#prosthetics-roll-and-scroll)
  - [Appliance Transaction Warning Display](#appliance-transaction-warning-display)
  - [PSAS HCPCS History Option Warning Display](#psas-hcpcs-history-option-warning-display)
  - [Add/Edit Home Oxygen Patient Option Warning Display](#addedit-home-oxygen-patient-option-warning-display)
- [Prosthetics GUI](#prosthetics-gui)
  - [Prosthetics GUI Installation](#prosthetics-gui-installation)
  - [Appliance Detail Form](#appliance-detail-form)
  - [NPPD Detail Screen](#nppd-detail-screen)
  - [View Prosthetics Billing Information](#view-prosthetics-billing-information)
- [ICD-10 Searches](#icd-10-searches)
  - [ICD-10-CM Diagnosis Code Search](#icd-10-cm-diagnosis-code-search)
    - [Performing ICD-10 Look-Ups and Searches](#performing-icd-10-look-ups-and-searches)
    - [Partial Code Look-Up](#partial-code-look-up)
    - [Partial Description Look-Up](#partial-description-look-up)
- [Known Issue](#known-issue)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Prosthetics package contained in patch RMPR\*3\*168.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alphanumeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision-making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                             |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character |
| Decimal after first 2 characters | Does not contain decimals                                                                                                             |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch RMPR\*3\*168 makes the following changes to the Prosthetics package:

- Ability to display full (expanded) text descriptions associated with ICD-10-CM codes in the provisional diagnosis field of the *Suspense Processing* menu option within VistA’s roll-and-scroll Prosthetics package on the screen and printed on applicable reports.
- Ability to display full (expanded) text descriptions associated with ICD-10-CM codes in the provisional diagnosis field of the *Processing* menu option within the Prosthetics VistA Suite Graphical User Interface (GUI) on the screen and printed on applicable reports.
- Ability to display full (expanded) text descriptions associated with ICD-10-CM codes in the ICD code field within the *Administrative Home Oxygen* module on the A*dd/Edit Home Oxygen Patient* data entry screen.
- Ability to identify the ICD code/description displayed is an ICD-9 or an ICD-10 code within VistA’s roll-and-scroll Prosthetics package on the screen and printed on applicable reports.
- Ability to display separately ICD-9 and ICD-10 codes/descriptions within the Prosthetics VistA Suite GUI on the screen and printed on applicable reports.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Prosthetics manuals are posted on the VistA Documentation Library (VDL) [Prosthetics](http://www.va.gov/vdl/application.asp?appid=96) page.

The following manuals are updated with changes for RMPR\*3\*168:

- Prosthetics VistA Suite (GUI) User Manual
- Prosthetics Basics User Manual
- National Prosthetics Patient Database (NPPD) User Manual
- View Billing Information (GUI) User Manual
- Home Oxygen Module User Manual
- Electronic Order/Suspense Processing User Manual  

The following manuals do not contain changes relating to patch number RMPR\*3\*168:

- Prosthetics VistA Suite (GUI) Installation Guide
- Prosthetics Inventory Package (PIP) Lessons Learned
- Prosthetics Inventory Package (PIP) User Guide 
- Installation Guide
- Prosthetics Security Guide
- NPPD Detail Display (GUI) Installation Guide
- Purchasing - Stock Issues User Manual
- Purchase Cards User Manual
- Delayed Order Report (DOR) (GUI) User Manual
- Delayed Order Report (DOR) (GUI) Installation Guide
- Prosthetics Technical Manual

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete pre-installation and post-installation instructions can be found in the RMPR\*3.0\*168 Patch Description in FORUM.

Patches  
Prior to installing RMPR\*3\*168, the following associated patches must already be installed:

- GMRC\*3\*73
- ICD\*18\*57
- LEX\*2\*80
- OR\*3\*361
- PX\*1\*199
- RMPR\*3\*125
- RMPR\*3\*128
- RMPR\*3\*148
- RMPR\*3\*150
- RMPR\*3\*162
- RMPR\*3\*163

# Prosthetics Roll and Scroll

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appliance Transaction Warning Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** *Date of Interest* is the Home Oxygen Prescription Date.

If the ICD code being displayed was inactive on the Date of Interest, the software displays an alert message after the Diagnosis description. This alert may wrap onto the next line if the Diagnosis description is too long.

To avoid this, and to make the display more readable, the software has been updated to check the length of the information being displayed. If it is determined that not all of the alert information is able to fit onto a single line, then the entire warning displays on the following line and is indented two spaces to denote the relationship to the previous line.

The example below shows how this warning message displays for Appliance Transactions.

Example: Warning and Indentation for Appliance Transactions

PROSPATIENT, ONE SSN: 000-12-3456 DOB: 01-01-1000

APPLIANCE/REPAIR LINE ITEM DETAIL \<4-1\>

TYPE OF FORM: INITIATOR: DATE: OCT 01, 2013

DELIVER TO:

TYPE TRANS: INITIAL ISSUE QTY: SOURCE: COMMERCIAL

VENDOR:

DELIVERY DATE:

TOTAL COST: OBL:

REMARKS:

DISABILITY SERVED: NSC/OP

ITEM DESCRIPTION: ULTRALIGHTWEIGHT WHEELCHAIR

APPLIANCE: ULTRALIGHTWEIGHT WHEELCHAIR

CONTRACT \#:

EXCLUDED/WAIVER:

PSAS HCPCS: A4364 ADHESIVE

ICD-10 Code: A00.0 CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR CHOLERAE

\*\* Inactive \*\* Date: OCT 01, 2013

CPT MODIFIER:

DESCRIPTION:

EXTENDED DESCRIPTION:

## *PSAS HCPCS History Option* Warning Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** *Date of Interest* is the Entry Date.

If the ICD code being displayed was inactive on the Date of Interest, the software displays an alert message after the Diagnosis description. This alert may wrap onto the next line if the Diagnosis description is too long.

To avoid this, and to make the display more readable, the software has been updated to check the length of the information being displayed. If it is determined that not all of the alert information is able to fit onto a single line, then the entire warning displays on the following line and is indented two spaces to denote the relationship to the previous line.

The example below shows how this warning message displays for PSAS HCPCS History Option.

Example: Warning and Indentation for *PSAS HCPCS History* Option

REQUEST DATE PATIENT NAME SSN VENDOR OCT 01, 2013-DEC 31, 2020

=========================================================================

MAR 30, 2020 PROSPATIENT, ONE O 0478

ITEM: ACETAMINOPHEN W/CODE QTY: TOTAL COST: 0.00 INITIAL ISSUE

INITIATOR:

ICD-10 Code: A01.09 Typhoid fever with other complications

\*\* Inactive \*\* Date: DEC 31, 2020

TOTAL DOLLARS SPENT ON THIS HCPCS: \$ 0.00 TOTAL QUANTITY ISSUED: 0

## *Add/Edit Home Oxygen Patient* Option Warning Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the *Add/Edit Home Oxygen Patient* option, if you select an existing Item and that Item contains an ICD code that is inactive based on the Start Date of the currently selected prescription, the software then issues a warning and provides choices on how to proceed.

You have three options:

1.  Select a different item with no ICD code or with an active ICD code.
2.  Enter a new item.
3.  Proceed with this item. If you proceed with this item, the existing ICD Diagnosis code will be DELETED. You may then enter an active ICD Diagnosis code or you may leave the ICD Diagnosis field blank.

Example: Warning for *Add/Edit Home Oxygen Patient* Option

The following items are already in the patient's template:

Item Description Vendor ICD CS+

\* 1 HEAD GEAR-CPAP-SOFT VENDOR ONE 784.0 9

2 NECK COOLER, STEELE VENDOR ONE 847.0 9

3 NECKLOOP POWERED AMPLIFIED VENDOR ONE

\* = Primary Item

CS = Code Set for ICD Diagnosis code

\+ = Item with active ICD code on start date of prescription

Select ACTION: (A/D/E): Edit

Select an ITEM: (1-3): 1 \* 1 HEAD GEAR-CPAP-SOFT

This item contains the ICD Diagnosis Code: 784.0 which was inactive based

on the start date of the currently selected prescription.

You may 1)select a different item with no ICD code or with an active ICD code,

2)enter a new item or

3)proceed with this item. If you proceed with this item, the existing

ICD Diagnosis code 784.0 will be DELETED.

You may then enter an active ICD-10 Diagnosis code or you may leave

the ICD Diagnosis field blank.

Do you wish to continue?

# Prosthetics GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prosthetics GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please confirm the information that will be included into Version info for Prosthetics package:

- CompanyName: Veterans Administration
- FileDescription: Prosthetics VistA Suite
- FileVersion: 3.0.168.82
- ProductName: Prosthetics VistA Suite
- Product Version: 3.8.168 (Patch 168)

Install the Prosthetics GUI client software following the instructions of the *Prosthetics VistA Suite (GUI) Installation Guide* found on the VistA Documentation Library (VDL) at the following link:

<http://www.va.gov/vdl/application.asp?appid=96>.

## Appliance Detail Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appliance Detail form reveals, in the ICD Code box on the Appliance Item section, whether the ICD description is for ICD-10 on the Appliance Transaction Detail form.

Example: Appliance Detail Form

![](rmpr-3-168-icd-10-release-notes/002.png)

The Appliance Detail form also presents a warning if the ICD date attached to the ICD code is incorrect.

Example: ICD-10 Description and Warning Display for Appliance Detail

PROSPATIENT, ONE SSN: 000-12-3456 DOB: 01-01-1000

APPLIANCE/REPAIR LINE ITEM DETAIL \<4-1\>

TYPE OF FORM: INITIATOR: DATE: OCT 01, 2013

DELIVER TO:

TYPE TRANS: INITIAL ISSUE QTY: SOURCE: COMMERCIAL

VENDOR:

DELIVERY DATE:

TOTAL COST: OBL:

REMARKS:

DISABILITY SERVED: NSC/OP

ITEM DESCRIPTION: DESCRIPTION

APPLIANCE: DESCRIPTION

CONTRACT \#:

EXCLUDED/WAIVER:

PSAS HCPCS: A4364 ADHESIVE

ICD-10 Code: A00.0 CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR CHOLERAE

\*\* Inactive \*\* Date: OCT 01, 2013

CPT MODIFIER:

DESCRIPTION:

EXTENDED DESCRIPTION:

## NPPD Detail Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NPPD Detail Display Screen contains the following changes:

- Customizable data field is now called Suspense ICD.
- Column Headers are now called Suspense ICD.
- If the Provisional Diagnosis is entered using a manual suspense entry via the VistA Prosthetics package, then the Prosthetics VistA Suite GUI package does not designate the diagnosis as ICD- 9 or ICD-10.

Example: NPPD Detail Display Screen

![](rmpr-3-168-icd-10-release-notes/003.png)

> **NOTE:** When you select “Suspense ICD” as one of the custom fields, you may not select “Suspense ICD” from either of the two remaining custom fields until “Suspense ICD” is deselected. This prevents you from accidentally creating more than one “Suspense ICD” column and more than one associated ICD Code Set column.

## View Prosthetics Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Prosthetic Billing Information Screen contains the following changes:

- Displays the code and full description/definition of the ICD-10- CM Diagnosis.
- Column Headers are now called ICD Code and ICD Desc.
- Displays only the “ICD” label.

Example: Prosthetics Billing Information Screen

![](rmpr-3-168-icd-10-release-notes/004.png)

> **NOTE:** If the Provisional Diagnosis is entered using a manual suspense entry, then the Prosthetics VistA Suite GUI package does not designate the diagnosis as ICD- 9 or ICD-10.

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Prosthetics package provides the ability to search on ICD-10-CM diagnosis codes and ICD-10-PCS procedure codes.

> **NOTE:** Existing ICD-9 functionality has not changed.

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only one routine in Prosthetics performs a look-up on ICD codes. The original code used a ^DIE FileMan call. Utilizing the original FileMan call, new Application Programmer Interfaces (APIs) have been created to perform the ICD-10 look-ups.

The ICD-10 code set is much more complex and detailed than the ICD-9 code set. When you enter a partial code or a partial description, a list displays matching your input, from which you can pick your next selection. This may result in an additional list displaying at an even lower level of detail. This process continues until you select the desired ICD-10 code from the list.

ICD-10 diagnosis code search highlights include:

- Both partial code searches and full ICD-10 code entry are possible, where all or part of the code is known.
  - The software displays the total number of entries that match the three-character input (20), a numbered list of matching codes, their descriptions, and designates if the entry is a branch (-) or a leaf node match.
- You can “drill down” through the branches (-) and or a leaf nodes to identify the single, valid ICD-10 code that best matches the patient diagnosis.
- Sixty-character short descriptions for the valid ICD-10 codes display.

### Performing ICD-10 Look-Ups and Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the active ICD-10 code set, searches performed may return more matches than can be displayed on a single screen, which is due to the added detail available with the ICD-10 code set.

In these instances, you can follow the steps listed below:

1.  To begin your search, you can enter any of the following:
    1.  A valid ICD-10 code.
    2.  A partial ICD-10 code.
    3.  A partial description of a valid ICD-10 code.
2.  These matches could contain either a valid ICD-10 code (leaf node) or a branch node which is followed by a "-".
    1.  If you select a valid ICD-10 code, the software continues to the next function.
    2.  If you select one partial ICD-10 code (i.e. a branch node denoted by a trailing "-), all immediate descendants of that branch node display for you to see.
3.  This step repeats until you select a valid ICD-10 code.

### Partial Code Look-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shown below is a detailed, multi-screen sample of a look-up / search using a partial code.

Example: ICD-10 - Help and Partial Code Look-Up Screen

Select Home Oxygen Main Menu Option: ED Add/Edit Home Oxygen Patient

Select PROSTHETICS PATIENT NAME: PROSPATIENT, ONE 5001AC 1-12-42 0001

23456 YES SC VETERAN

HOME OXYGEN ELIGIBILITY: SC/OP//

HOME OXYGEN CONTRACT LOCATION: ALBANY//

HOME OXYGEN ACTIVATION DATE: MAR 1,2000//

Select HOME OXYGEN PRESCRIPTION DATE: Jan 01, 2014// JAN 01, 2014

DATE: JAN 1,2014//

EXPIRATION DATE: JAN 1,2014//

DESCRIPTION:

No existing text

Edit? NO//

The following items are already in this patient's template:

\* 1 ACETAMINOPHEN W/CODEINE 30MG TAB VENDOR ONE

2 WHEELCHAIR LIGHTWEIGHT VENDOR TWO

3 COLOSTOMY BAGS VENDOR ONE

4 ACETAMINOPHEN W/CODEINE 30MG TAB VENDOR ONE

5 NECK BRACE VENDOR TWO

6 COLOSTOMY BAGS VENDOR ONE

7 COLOSTOMY BAGS VENDOR ONE

\* = Primary Item

Select ACTION: (A/D/E): Edit

Select an ITEM: (1-7): 1\* 1 ACETAMINOPHEN W/CODEINE 3

PRIMARY ITEM: YES//

ITEM: ACETAMINOPHEN W/CODEINE 30MG TAB//

HCPCS CODE: A4365//

VENDOR: VENDOR ONE//

QUANTITY: 1//

UNIT COST: 1.00//

UNIT OF ISSUE: EA EACH

ICD10 Diagnosis code: F14.21 Cocaine dependence, in remission

> **NOTE:** ?, ?? and ??? are used to display Help texts and prompts.

When entering ?:

Enter code or “text” for more information.

When entering ??:

Enter a "free text" term or part of a term such as ”femur fracture”.

Or

Enter a ”classification code” (ICD/CPT, etc.) to find the single term associated with the code.

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

### Partial Description Look-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shown below is a detailed, multi-screen sample of a performing a look-up or search using a partial description. For this example, first select *Home Oxygen* Main Menu Option: *ED Add/Edit Home Oxygen Patient*.

Example: ICD-10 - Help and Partial Description Look-Up Screen

Select PROSTHETICS PATIENT NAME: PROSPATIENT, ONE 5001AC 1-12-42 0001

23456 YES SC VETERAN

HOME OXYGEN ELIGIBILITY: SC/OP//

HOME OXYGEN CONTRACT LOCATION: ALBANY//

HOME OXYGEN ACTIVATION DATE: MAR 1,2000//

Select HOME OXYGEN PRESCRIPTION DATE: Jan 01, 2014// JAN 01, 2014

DATE: JAN 1,2014//

EXPIRATION DATE: JAN 1,2014//

DESCRIPTION:

No existing text

Edit? NO//

The following items are already in this patient's template:

\* 1 ACETAMINOPHEN W/CODEINE 30MG TAB VENDOR ONE

2 WHEELCHAIR LIGHTWEIGHT VENDOR TWO

3 COLOSTOMY BAGS VENDOR ONE

4 ACETAMINOPHEN W/CODEINE 30MG TAB VENDOR ONE

5 NECK BRACE VENDOR TWO

6 COLOSTOMY BAGS VENDOR ONE

7 COLOSTOMY BAGS VENDOR ONE

\* = Primary Item

Select ACTION: (A/D/E): Edit

Select an ITEM: (1-7): 1 \* 1 ACETAMINOPHEN W/CODEINE 3

PRIMARY ITEM: YES//

ITEM: ACETAMINOPHEN W/CODEINE 30MG TAB//

HCPCS CODE: A4365//

VENDOR: VENDOR TWO//

QUANTITY: 1//

UNIT COST: 1.00//

UNIT OF ISSUE: EA//

ICD10 Diagnosis code: F14.151 Cocaine abuse w cocaine-induc psychotic disorder

w hallucin

ICD10 Diagnosis code: F14.151// COCAINE

> **NOTE:** A "–" following the number means more entries are under that “branch”. Selecting these entries displays the lower level branches, and ultimately the “leafs”, or individual ICD-10 codes.

23 matches found \<-

1\. F14.10 Cocaine Abuse, Uncomplicated

2\. F14.12- Cocaine abuse with intoxication

3\. F14.14 Cocaine Abuse with Cocaine-Induced Mood Disorder

4\. F14.15- Cocaine abuse with cocaine-induced psychotic

disorder

5\. F14.18- Cocaine abuse with other cocaine-induced disorder

6\. F14.19 Cocaine Abuse with unspecified Cocaine-Induced

Disorder

7\. F14.20 Cocaine Dependence, Uncomplicated

8\. F14.21 Cocaine Dependence, in Remission

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 4

3 matches found

1\. F14.150 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder with Delusions (ICD-10-CM F14.150)

2\. F14.151 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder with Hallucinations (ICD-10-CM F14.151)

3\. F14.159 Cocaine Abuse with Cocaine-Induced Psychotic

Disorder, unspecified (ICD-10-CM F14.159)

Select 1-3: 2

ICD10 Diagnosis code: F14.151

ICD10 Diagnosis description: Cocaine Abuse with Cocaine-Induced Psychotic

Disorder with Hallucinations (ICD-10-CM F14.151)

REMARKS: Test with new ICD10 lookup API Replace

ITEM TYPE: Initial Issue//

Select FUND CONTROL POINT: ^

# Known Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICD-10 Class I Remediation project will update VistA to include the ICD-10 Diagnosis and Procedure codes. The first patches to be delivered by this project will be the STS patches ICD\*18.0\*57 and LEX\*2.0\*80 which will include both the ICD-10 Diagnosis and Procedure codes along with new or updated APIs that will be used by the other VistA applications to select, retrieve and display these new codes.

Several VistA applications do not currently utilize code set versioning. Those applications are Prosthetics, Home Based Primary Care, and Laboratory: Anatomic Pathology. As a result, these applications currently allow inactive ICD-9 codes to be displayed and selected for ICD-9 dates of service.

During the interim, after the installation of the STS ICD-10 Class I Remediation patches and prior to the ICD-10 Implementation date, these applications will also allow the display and selection of inactive ICD-10 codes including statuses of (Inactive) or (Pending). The users of these applications should use CAUTION to select ICD-9 or ICD-10 codes that are appropriate and active.

The following examples show how the software appears in these applications:

EXAMPLE 1: Inactive ICD-9 codes

The warning (Inactive) appears at the end of the short description.

ICD-9 DIAGNOSIS CODE: 100.81// 488.

12 matches found

1\. 488. FLU D/T AVIAN FLU VIRUS (Inactive)

2\. 488.0 FLU DT IDEN AVIAN VIRUS (Inactive)

3\. 488.01 FLU DT IDEN AVIAN W PNEU (Major CC)

4\. 488.02 FLU DT AVIAN W OTH RESP (CC)

5\. 488.09 FLU DT AVIAN MANFEST NEC (CC)

Press \<RETURN\> for more, '^' to exit, or Select 1-5:

EXAMPLE 2: Inactive ICD-10 codes

The warning (Pending) appears at the end of the short description.

ICD-9 DIAGNOSIS CODE: 100.81// S06.816

3 matches found

1\. S06.816A Inj r int crtd,intcr w LOC \>24 hr w/o ret consc w

surv, init (10/01/2014) (Pending)

2\. S06.816D Inj r int crtd,intcr w LOC \>24 hr w/o ret consc w

surv, subs (10/01/2014) (Pending)

3\. S06.816S Inj r int crtd,intcr w LOC \>24 hr w/o ret consc w

surv, sqla (10/01/2014) (Pending)

Select 1-3:

When creating or editing records dated after the ICD-10 Activation Date, the software will correctly screen out both the inactive ICD-9 and inactive ICD-10 codes.