---
title: EAS*1*40 Long Term Care Copayment Phase 4 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Long Term Care Copayment Phase 4
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1*40
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [What’s New in Phase 4](#whats-new-in-phase-4) - [New Option(s)](#new-options) - [# Phase 4 Software Enhancements](#phase-4-software-enhancements) - [NOIS Calls](#nois-calls) - [Add, Edit, and View a LTC Copayment Test](#add-edit-and-view-a-ltc-copayment-test) - [Determine LTC Copayment Obligation
audience: 
keywords: 
  - table
  - contents
  - copayment
  - strong
  - phase
  - template
  - copayments
  - test
  - edit
  - modified
page_count: 0
word_count: 1044
section_count: 8
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p40_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p40_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-1-40-long-term-care-copayment-phase-4-release-notes/001.png)

veterans millennium health care and benefits act

Long Term Care Copayment (LTC) phase 4

Release notes

Patch EAS\*1\*40

November 2003

V*IST*A Healthcare System Design & Development

Table of Contents

# What’s New in Phase 4


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [What’s New in Phase 4](#whats-new-in-phase-4)
  - [New Option(s)](#new-options)
- [# Phase 4 Software Enhancements](#phase-4-software-enhancements)
  - [NOIS Calls](#nois-calls)
  - [Add, Edit, and View a LTC Copayment Test](#add-edit-and-view-a-ltc-copayment-test)
  - [Determine LTC Copayment Obligations for Legally Separated Veterans](#determine-ltc-copayment-obligations-for-legally-separated-veterans)
  - [LTC Copayment Calculations and Displays](#ltc-copayment-calculations-and-displays)
- [Phase 4 Technical Release Notes](#phase-4-technical-release-notes)
  - [Input Template Changes](#input-template-changes)
    - [New Template(s)](#new-templates)
    - [Modified Template(s)](#modified-templates)
  - [Option Changes](#option-changes)
    - [New Option(s)](#new-options-1)
    - [Modified Option(s)](#modified-options)
Phase 4 of the Long Term Care (LTC) Copayments project provides the following new functionality:

## New Option(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following option has been added to the LTC Copayments Menu:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Option Name</strong></td>
<td><strong>Menu Text</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>EASEC LTC COPAY TEST EXPIRE</td>
<td>Expiring or Expired LTC Copayment Tests:</td>
<td><p>This option is used to print a choice of two reports:</p>
<ul>
<li><p>Pending Expiration - Prints a list of veterans whose tests are about to expire within a user-specified number of days. Can be sorted by name or date.</p></li>
<li><p>Expired - Prints a list of veterans whose tests have already expired since a user-specified start date. Can be sorted by name or date.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# # Phase 4 Software Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NOIS Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 4 of the LTC Copayments project addresses the following NOIS issues:

|                    |                                            |                                                                                                                                                                               |
|--------------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NOIS Call Name | Subject                                | Functionality Modification / Enhancement                                                                                                                                  |
| TUA-0803-31858     | LTC CO-PAY - CHANGING REASON FOR EXEMPTION | A change in Phase 3 prevented users from changing the REASON FOR EXEMPTION field (#2.07) in the ANNUAL MEANS TEST file (#408.31). Phase 4 allows users to change this field.  |
| ASH-0303-30561     | LTC AND A&A AND VA PEN ELIG                | The exemption status prompt flow has been modified to have it at the beginning screen of the LTC Copayment test. Users will be able to modify the Reason for Exemption field. |

Phase 4 of the LTC Copayments project provides the following enhancements to previously existing functionality in the LTC Copayments Menu. For information about how to use the options on the LTC Copayments Menu, refer to the LTC Copayments User Manual.

## Add, Edit, and View a LTC Copayment Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Option(s) Affected

#### *Add a New LTC Copayment Test*

#### *Edit an Existing LTC Copayment Test*

#### *View a LTC Copayment Test*

#### Enhanced Functionality

- The financial data screens have been modified to reflect the format changes made to the Application for Extended Care (10-10EC) paper form.
- The ELIGIBILITY STATUS DATA SCREEN \<2\> has been replaced by the INSURANCE DATA SCREEN \<5\> from the Registration options.
- The *Add a New LTC Copayment Test and Edit an Existing LTC Copayment Test* options have been modified to enable the user to indicate that the veteran is exempt from LTC copayments (for a reason other than low income) and complete the LTC Copayment Test without having to go through all of the financial screens.

#### ## Printing Application for Extended Care (10-10EC)

#### Option(s) Affected

#### *Print Application for Extended Care*

#### Enhanced Functionality

The system now supports the display and printing of the LTC Copayment Tests in either the old or new 10-10EC format, depending on which one is used to complete the test.

## Determine LTC Copayment Obligations for Legally Separated Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Option(s) Affected

*Add a New LTC Copayment TestEdit an Existing LTC Copayment TestView a LTC Copayment*

#### Enhanced Functionality

The user can now indicate if a veteran is legally separated, and if so, the copayments will be calculated using the rules for an unmarried veteran.

## LTC Copayment Calculations and Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Option(s) Affected

####### Calculated LTC Copayments Print

#### Enhanced Functionality

The format of the Calculated LTC Copayments report has been modified. The user will be prompted to choose to print the copayments for either inpatient or outpatient services, then enter the patient’s LTC admission date (for the inpatient report) and report start date.

# Phase 4 Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Input Template Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Template(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Input Template Name</strong></td>
<td><strong>File Number</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>EASEC ENTER/EDIT ASSETS NEW</td>
<td>408.21</td>
<td>This template was added to edit the assets fields for the new 10-10EC format. The new format skips the STOCKS AND BONDS field #2.02.</td>
</tr>
<tr class="odd">
<td>EASEC ENTER/EDIT INCOME NEW</td>
<td>408.21</td>
<td><p>This template was added to edit the income fields for the new 10-10EC format. The new format has only 3 income fields:</p>
<ul>
<li><p>TOTAL INCOME FROM EMPLOYMENT (#.14)</p></li>
<li><p>INTEREST, DIVIDEND, OR ANNUITY (#.15)</p></li>
<li><p>OTHER INCOME (#.17)</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Modified Template(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Input Template Name</strong></td>
<td><strong>File Number</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>EASEC EDIT MARITAL STATUS</td>
<td>408.22</td>
<td><p>The template logic was modified to add a new prompt for “Legally Separated” and remove the prompt “Are you living with your spouse?”:</p>
<p>IS YOUR MARITAL STATUS EITHER MARRIED OR SEPARATED: YES//</p>
<p>ARE YOU LEGALLY SEPARATED: YES//</p>
<p>Display the next prompt only if “Legally Separated” is answered “No”:</p>
<p>IS YOUR SPOUSE RESIDING IN THE COMMUNITY: YES//</p></td>
</tr>
</tbody>
</table>

## Option Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Option(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name             | Menu Text                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EASEC LTC COPAY TEST EXPIRE | Expiring or Expired LTC Copayment Tests | This option will print a choice of two reports: one is a list of veterans whose LTC copayment test (10-10EC) is about to be a year old within a user-specified time frame (up to 60 days), the other is a list of veterans whose LTC copayment test (10-10EC) is more than a year old since a user-specified date. The user will be prompted to select which report to produce. These reports will not include deceased veterans, veterans who were exempt from LTC copayments due to a compensable service-connected disability, or veterans whose LTC episode began before 11/30/99. |

### Modified Option(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                      |                     |                                                                                  |
|----------------------|---------------------|----------------------------------------------------------------------------------|
| Option Name      | Menu Text       | Description of Changes                                                       |
| EASEC LTC COPAY MENU | LTC Copayments Menu | The new option, Expiring or Expired LTC Copayment Tests, was added to this menu. |