---
title: DG*5.3*P624/EAS*1.0*P57 10-10EZ Phase 3.0 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: *P624/EAS*1.0*P57 10-10EZ Phase 3.0
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 5.3
patch_id: EAS*5.3*624
group_key: "EAS:EAS:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - application
  - vista
  - spouse
  - manual
  - enrollment
  - benefits
  - revised
  - form
page_count: 0
word_count: 2099
section_count: 12
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/dg_5_3_p624_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/dg_5_3_p624_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](dg-5-3-p624-eas-1-0-p57-10-10ez-phase-3-0-release-notes/001.png)

10-10EZ Phase 3.0

Release Notes

DG\*5.3\*P624

EAS\*1.0\*P57

March 2001

V*IST*A System Design & Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [Related Documents](#related-documents)
  - [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
    - [10-10EZ Phase 3.0 Project Stakeholder Requests](#10-10ez-phase-30-project-stakeholder-requests)
- [Technical Release Notes](#technical-release-notes)
  - [Patient Information Management Systems (PIMS) (DG\5.3\624)](#patient-information-management-systems-pims-dg53624)
    - [Host File Information](#host-file-information)
  - [Added and Modified Fields](#added-and-modified-fields)
  - [Data Dictionary Changes](#data-dictionary-changes)
  - [Templates](#templates)
  - [Options](#options)
  - [Protocols](#protocols)
  - [Enrollment Application System (EAS\1.0\57)](#enrollment-application-system-eas1057)
    - [Data Element Changes](#data-element-changes)
    - [Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)](#callable-routines-entry-points-and-application-programmer-interfaces-apis)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current V*IST*A Enrollment Application System (EAS) enables a local V*IST*A treatment facility to electronically process a 10-10EZ Application for Health Benefits, which has been submitted by a veteran via a web-based application located on the VA web server. The 10-10EZ Application that is presented on the VA web server has been revised in both form and content.

The primary focus of the *10-10EZ Phase 3.0 Project* is to enhance the ability to enter and edit data via the V*IST*A User Interface at the field sites during the processing of Health Benefits applications. Intakes that are done at the sites by Mail-in and Walk-in applications currently account for 94% of total Health Benefits Applications within VHA.

Version 2.5 of the 10-10EZ software updated the EAS screens and data filing functionality to support the revised format of the June 2004 10-10EZ Application for Health Benefits form. These software updates included adding approximately 27 data elements to the EAS Data Comparison screen, enhancing the EAS data filing capabilities to store the new data in the VistA Patient Database, and changing the EAS-printed 10-10EZ form to match the format of the June 2005 10-10EZ Application for Health Benefits form.

Version 3.0 of the 10-10EZ software again aligns the EAS screens with the Feb 2005 10-10EZ Application for Health Benefits form and also continues that alignment into other VistA applications: Registration, Enrollment and Means Testing. Version 3.0 of the 10-10EZ software also delivers new end user functionality such as modifying Registration, Enrollment and Means Testing printing options to only offer the valid or active health benefits forms:

- 10-10EZ Application for Health Benefits form
- 10-10EZR Health Benefit Renewal form

The ability to print invalid or inactive health benefits forms (e.g.: 10-10, 10-10I, 10-10F, etc) was removed. Another component of new end user functionality is the automatic calculation of the Medical Expense Deductible. When an end user enters the gross medical expenses provided by the veteran, the VistA software will now automatically calculate the Adjusted Medical Expenses amount based upon the yearly Maximum Annual Pension Rate (MAPR) tables.

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the EAS and HEC Legacy system.

This document will outline the detailed new features, new functions, and enhancements for the 10-10EZ Phase 3.0 project, which incorporates several enhancements.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><p>EAS_1_P57 _LTC_UM.PDF</p></li>
</ul></td>
<td>Revised Long Term Care (LTC) Copayment User Manual</td>
</tr>
<tr class="even">
<td><ul>
<li><p>EAS_1_P57_UM.PDF</p></li>
</ul></td>
<td>Revised Enrollment Application System User Manual</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>EAS_1_P57_TM.PDF</p></li>
</ul></td>
<td>Revised Enrollment Application System Online 10-10EZ Technical Manual</td>
</tr>
<tr class="even">
<td><ul>
<li><p>DG_5_3_P624_REG_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Registration Menu Module</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>DG_5_3_P624_ADTO_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Outputs Menu Module</td>
</tr>
<tr class="even">
<td><ul>
<li><p>DG_5_3_P624_MTS_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Means Test Supervisor Menu Module</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>DG_5_3_P624_CETS_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual Copay, Exemption Test Supervisor Menu Module</td>
</tr>
<tr class="even">
<td><ul>
<li><p>DG_5_3_P624_ADTBE_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual; Menus, Intro, Orientation, etc. Module</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>DG_5_3_P624_SADT_UM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT User Manual, Supervisor ADT Menu</td>
</tr>
<tr class="even">
<td><ul>
<li><p>DG_5_3_P624_PIMS_TM.PDF</p></li>
</ul></td>
<td>Revised PIMS ADT Technical Manual</td>
</tr>
</tbody>
</table>

#### ## Acronyms and Definitions

#### Acronyms

| Acronym     | Description                                                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10-10EZ         | A VA form used by veterans to apply for VHA healthcare benefits                                                                                                                                                                                                                       |
| 10-10EZR        | A VA form used by veterans who are already enrolled within the VHA to update personal, insurance, or financial information.                                                                                                                                                           |
| AO              | Agent Orange                                                                                                                                                                                                                                                                          |
| CBO             | Chief Business Office                                                                                                                                                                                                                                                                 |
| EAS             | Enrollment Application System: An application that allows local V*IST*A systems to electronically process applications for enrollment and healthcare benefits filled out by veterans via a web-based application.                                                             |
| EAP             | Enrollment Application Processor: This module enables the local V*IST*A system to electronically process a 10-10EZ application for enrollment and healthcare benefits, which has been submitted by a veteran via a web-based application located on the VHA ReachForm server. |
| EC              | Environmental Contaminants                                                                                                                                                                                                                                                            |
| EGT             | Enrollment Group Threshold                                                                                                                                                                                                                                                            |
| HEC             | Health Eligibility Center                                                                                                                                                                                                                                                             |
| IVM             | Income Verification Matching                                                                                                                                                                                                                                                          |
| MT              | Means Test                                                                                                                                                                                                                                                                            |
| NSC             | Non-service-connected                                                                                                                                                                                                                                                                 |
| PIMS            | Patient Information Management System                                                                                                                                                                                                                                                 |
| SC              | Service-connected                                                                                                                                                                                                                                                                     |
| VA              | Veterans Administration                                                                                                                                                                                                                                                               |
| VHA             | Veterans Health Administration                                                                                                                                                                                                                                                        |
| V*IST*A | VHA Information Systems and Technology Architecture                                                                                                                                                                                                                                   |
Definitions
| Term          | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Disenrollment     | Voluntary request from veteran to discontinue enrollment in the VA Health Care system                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| GMT Thresholds    | a.k.a. HUD Indices. Geographical income level thresholds set yearly by the U.S. Department of Housing and Urban Development                                                                                                                                                                                                                                                                                                                                                                                                               |
| HL7               | Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*IST*A HL7 package to assist in transporting data using this specification.                                                                                                                                                                                                                                                                                       |
| IVM               | Income Verification Match. A program designed to verify income and insurance data reported by the veteran with that received from IRS (Internal Revenue Service), SSA (Social Security Administration), and other sources                                                                                                                                                                                                                                                                                                                 |
| Means Test        | Eligibility for VA hospital care and nursing home care is divided into two categories - mandatory and discretionary. An income assessment is made to determine whether a non service-connected veteran, who is not in receipt of VA monetary benefits or otherwise exempt from income assessment, is eligible for cost-free VA medical care. This income assessment is known as "Means Testing". Patients whose income is above the defined income levels must agree to make copayments to VA for outpatient and inpatient care rendered. |
| MT Thresholds     | Income threshold levels set yearly within the VA for the purpose of establishing benefit levels for veterans                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HEC Legacy System | M-based database currently in use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### # User Release Notes

## New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### 10-10EZ Phase 3.0 Project Stakeholder Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Print the new 10-10EZ and 10-10EZR (dated Feb 2005) at any time in the business process within V*IST*A, through the Registration, Enrollment, and Financial Assessment applications. Also remove and/or modify any reference to the obsolete 1010 forms. These obsolete forms are:
  - 10/10 - Application for Medical Benefits
  - Supplemental 10/10 - Supplemental Data Sheet
  - 10/10T- Application for Medical Benefits (with Consent to Release Information, Co-payment Notice, Privacy Act Notice)
  - 10-10F - Financial Worksheet
  - 10-10I - Insurance Information Form
- Automatically calculate the medical expense deductible on V*IST*A per IAW 38 CFR3.272(g)
- Create a V*IST*A storage location for ‘Amount Contributed to Child Support’, as well as display and make the data element editable within the V*IST*A User Interface
- Auto-populate V*IST*A storage location A/O LOCATION with ‘Vietnam’, when applicant answers ‘Yes’ to 10-10EZ web application question “Were You Exposed to Agent Orange While Serving In Vietnam?”
- 10-10EZ web application will align its input or data validation rules on the Military Service Number (Section IV, Block 1D) with those rules in V*IST*A. The 10-10EZ web application will add a checkbox labeled "Same as SSN” in Section IV, Block (complies with other 'Same As' checkboxes used in other places on the web form).
- Modify ‘CHILD PERMANENTLY DISABLED”, CHILD BETWEEN 18-23, and CHILD’S RELATIONSHIP TO YOU on the 10-10EZ web application and eliminate the defaulting to ‘No’ when no dependents have been entered (only web form change needed ).
- Change V*IST*A EAS 10-10EZ from printing ‘UNK’ to ‘Unknown’.
- Make the following data elements available in the V*IST*A user interface for the mail-in processing and the walk-in processing of the 10-10EZ and 10-10EZR. They will not be shared with the HEC or other V*IST*A sites:
  - DO YOU WANT AN APPOINTMENT WITH A VA DOCTOR OR PROVIDER AS SOON AS ONE BECOMES AVAILABLE?
  - E-MAIL ADDRESS
  - DATE OF RETIREMENT (APPLICANT)
  - DATE OF RETIREMENT (SPOUSE)
  - SPOUSE'S MAIDEN NAME
  - SPOUSE'S STREET ADDRESS 1
  - SPOUSE'S STREET ADDRESS 2
  - SPOUSE'S STREET ADDRESS 3
  - SPOUSE'S CITY
  - SPOUSE'S STATE
  - SPOUSE'S ZIP
  - SPOUSE'S TELEPHONE NUMBER
  - DEPENDENT ADDRESS FIELDS;

> DEPENDENT’S STREET ADDRESS 1

> DEPENDENT’S STREET ADDRESS 2

> DEPENDENT’S STREET ADDRESS 3

> DEPENDENT’S CITY

> DEPENDENT’S STATE

> DEPENDENT’S ZIP

- IS CHILD 18-23 IN SCHOOL
- VETERAN CELL PHONE NUMBER
- VETERAN PAGER NUMBER
- Receive, display, and accept the Veteran Cell Phone Number and Veteran Pager Number through the V*IST*A EAS application to support the current Nov 2004 and Feb 2005 10-10EZ Application for Health Benefits forms.
- Within the VistA Applicant/Spouse Employment Data screen, the Employment Retirement Date (Year), for either Veteran or Spouse, will not be required when the Employment Status = RETIRED. This will allow sites who have experienced mailed-in 10-10EZ forms where the Date of Retirement has been left blank to complete the form without entering a date. However, for the on-line 10-10EZ form, the Date of Retirement (Year) <u>will remain</u> a required entry when the Retired checkbox is checked.
- Within the VistA DG Means Test, DG Copay Test and EASEC LTC Copay Exemption Test applications, users will receive the 'PRINT 10-10EZR?' prompt first. Only when the 'PRINT 10-10EZR?' response is NO will the user receive the 'PRINT 10-10EZ?" prompt.
- Since the Gross Annual Income (GAI) and Net Worth (NW) money categories in the current VistA user interface do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA software will:
  - Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar mount in block ‘3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.’ of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
    - \[1\] Social Security (Not SSI) +
    - \[2\] U.S. Civil Service +
    - \[3\] U.S. Railroad Retirement +
    - \[4\] Military Retirement +
    - \[5\] Unemployment Compensation +
    - \[6\] Other Retirement +
    - \[8\] Interest, Dividend, Annuity +
    - \[9\] Worker’s Comp or Black Lung
  - Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar mount in block ‘1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)’ of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
    - \[1\] Cash, Amts in Bank Accts +
    - \[2\] Stocks and Bonds
  - Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar mount in block ‘3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)’ of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
    - \[4\] Other Property or Assets –
    - \[5\] Debts

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Information Management Systems (PIMS) (DG\*5.3\*624)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following must be installed BEFORE DG\*5.3\*624:

- (v)DG\*5.3\*395
- (v)DG\*5.3\*563
- (v)DG\*5.3\*570
- (v)DG\*5.3\*642
- (v)DG\*5.3\*610
- (v)DG\*5.3\*638

### Host File Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software for this patch is being distributed in a host file. The host file will contain two KIDS files.

Host File Name: EAS_1_P57.KID

Builds:

- DG\*5.3\*624
- EAS\*1.0\*57

## Added and Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Added Files \# | File Name            | Field \# | Field Name              |
|--------------------|--------------------------|--------------|-----------------------------|
| 2                  | Patient                  | .134         | Phone Number \[Cellular\]   |
|                    |                          | .135         | Pager Number                |
|                    |                          | 1010.1511    | Appointment Request Date    |
| 408.21             | Individual Annual Income | 1.12         | Gross Medical Expense       |
| 408.22             | Income Relation          | .19          | Amount Contributed To Child |

| Modified Files \# | File Name            | Field \# | Field Name                |
|-----------------------|--------------------------|--------------|-------------------------------|
| 2                     | Patient                  | .133         | Email Address                 |
|                       |                          | .2515        | Spouse's Employment Status    |
|                       |                          | .2516        | Spouse's Date of Retirement   |
|                       |                          | .31115       | Employment Status             |
|                       |                          | .31116       | Date of Retirement            |
|                       |                          | .362         | Disability Ret. from Military |
|                       |                          | 1010.159     | Appointment Request on 1010EZ |
| 408.13                | Income Person            | 1.1          | Maiden Name                   |
|                       |                          | 1.2          | Street Address 1              |
|                       |                          | 1.3          | Street Address 2              |
|                       |                          | 1.4          | Street Address 3              |
|                       |                          | 1.5          | City                          |
|                       |                          | 1.6          | State                         |
|                       |                          | 1.7          | Zip                           |
|                       |                          | 1.8          | Telephone Number              |
| 408.21                | Individual Annual Income | 1.01         | Adjusted Medical Expense      |
| 408.22                | Income Relation          | .18          | Child 18-23 in School         |

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Registration Patch DG\*5.3\*624 is distributed with Enrollment Application System Patch EAS\*1.0\*57 in a single host file in order to:

- Update data dictionaries for the PATIENT file (#2), the INCOME PERSON file (\#408.13), the INDIVIDUAL ANNUAL INCOME file (#408.21), and the INCOME RELATION file (#408.22)
- Allow fields added through 1010EZ Phase 2.5 (EAS\*1.0\*51 & DG\*5.3\*597) to be displayed and editable through Registration, Load/Edit, and Means Test options
- Remove routines, options, and protocols related to printing obsolete 1010 forms

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following input templates are exported with this patch:

- \[DGMT ENTER/EDIT EXPENSES\] FILE \#408.21
- \[DGMT ENTER/EDIT DEPENDENTS\] FILE \#408.22

The following list template is exported with this patch:

- \[DGMT DEPENDENTS\] Dependents Module

The following print templates are exported with this patch:

- \[DGDISPOSTIONS\] FILE \#2
- \[DGOPENDISPOSITIONS\] FILE \#2

The following list template is removed with this patch:

- \[DGRPT 1010T REGISTRATION\] 10-10T Registration

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are exported with this patch:

- \[DG REGISTRATION 10/10 REPRINT\] 10-10 Print
- \[DG CO-PAY TEST\] ADD
- \[DG CO-PAY EDIT\] EDIT
- \[DG MEANS TEST\] ADD
- \[DG MEANS TEST\] COMPLETE
- \[DG MEANS TEST\] EDIT

The following option is removed with this patch:

- \[DGRPT 10-10T REGISTRATION\] 10-10T Registration

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are exported with this patch:

- \[DGEN PATIENT ENROLLMENT MENU\] Patient Enrollment
- \[DGENCD CATASTROPHIC DISABILITY\] Catastrophic Disability
- \[DGENUP PRINT 1010EZ-EZR\] Print 1010EZ/EZR

The following protocols are removed with this patch:

- \[DGRPT INTERVIEW\] Interview
- \[DGRPT MENU\] 10-10T Registration

## Enrollment Application System (EAS\*1.0\*57)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS\*1\*60 must be installed BEFORE EAS\*1\*57.

This patch will install along with DG\*5.3\*624 - each a part of a single host file. KIDS will install DG\*5.3\*624 before it installs EAS\*1\*57.

### Data Element Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A few data elements will be added to or changed in file 711 (1010EZ Mapping) for collection, display, updating, filing, and printing. They include:

| Display Name     | Map-to File | Map-to Field     |
|----------------------|-----------------|----------------------|
| Amt To Child Support | 408.22          | .19 (Change from .1) |
| Cell Phone           | 2               | .134 (New)           |
| Pager \#             | 2               | .135 (New)           |

### Callable Routines, Entry Points, and Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EAS contains 1 new callable entry point API Routine EASEZPDG under Integration Agreement 4600 for Phase 3.0.