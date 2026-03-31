---
title: ASISTS GUI Version 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: OOPS
app_name: Automated Safety Incident Surveillance Tracking System
section: FIN
app_status: active
pkg_ns: OOPS
patch_ver: 2
patch_id: OOPS*2
group_key: "OOPS:OOPS:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The main purpose of this release is to enhance the ASISTS roll and scroll VistA package by implementing a Graphical User Interface (GUI) order to increase usability of ASISTS thereby promoting the collection and reporting of accidents and injuries. The scope of the enhancements affects the screens a
audience: 
keywords: 
  - table
  - contents
  - asists
  - report
  - version
  - employee
  - both
  - available
  - single
  - safety
page_count: 0
word_count: 5429
section_count: 18
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 3/6/02
revision_oldest: 3/6/02
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=56"
---

### ![](asists-gui-version-2-release-notes/001.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automated Safety Incident SurveillanceTracking System (ASISTS)RELEASE NOTES

(ASISTS GUI Version)

June 3, 2002

V*IST*A Technical Services

Revision History

|          |              |                 |            |
|----------|--------------|-----------------|------------|
| Date | Revision | Description | Author |
| 3/6/02   | 1.0          | Initial Version | REDACTED   |
|          |              |                 |            |
|          |              |                 |            |

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [![](asists-gui-version-2-release-notes/001.png)](#asists-gui-version-2-release-notes001png)
- [Preface](#preface)
  - [## Purpose of the Release Notes](#purpose-of-the-release-notes)
  - [Note: The User Manual, Installation Guide, Technical Manual and Security Guide for ASISTS 2.0 are presented separately.](#note-the-user-manual-installation-guide-technical-manual-and-security-guide-for-asists-20-are-presented-separately)
  - [## Reference Numbering System](#reference-numbering-system)
- [# Chapter 1 Introduction](#chapter-1-introduction)
  - [Overview](#overview)
  - [Types of Changes](#types-of-changes)
- [Chapter 2 Bug Fixes](#chapter-2-bug-fixes)
  - [## Overview](#overview-1)
  - [Bug fixes as the result of NOIS](#bug-fixes-as-the-result-of-nois)
    - [PUG-1101-51611 XMDUZ WRONG](#pug-1101-51611-xmduz-wrong)
    - [ASH-0901-31438 Questions CA-1’s and CA-2’s](#ash-0901-31438-questions-ca-1s-and-ca-2s)
    - [HOU-1001-72833 Undefined error WP+19^OOPSDOLX](#hou-1001-72833-undefined-error-wp19oopsdolx)
    - [### ### WRJ-1201-11937 Pulling wrong employee information](#wrj-1201-11937-pulling-wrong-employee-information)
    - [### ALT-0102-23246 Employee Occupation Code](#alt-0102-23246-employee-occupation-code)
    - [## Bug fixes / Modifications initiated by developers or requested by TAG](#bug-fixes-modifications-initiated-by-developers-or-requested-by-tag)
    - [Third Party Fields in the CA2](#third-party-fields-in-the-ca2)
    - [Injury Address Fields](#injury-address-fields)
    - [ASISTS DOL Anatomical Location Codes file (2261.1)](#asists-dol-anatomical-location-codes-file-22611)
    - [Changes made in data extraction routines for transmission of claims to DOL](#changes-made-in-data-extraction-routines-for-transmission-of-claims-to-dol)
    - [Physician Data on CA1](#physician-data-on-ca1)
    - [Bug in transmission of 2162 data to the ASISTS National Database (NDB)](#bug-in-transmission-of-2162-data-to-the-asists-national-database-ndb)
- [Chapter 3 New Functionality](#chapter-3-new-functionality)
  - [## Overview](#overview-2)
  - [New Options](#new-options)
    - [Complete/Validate/Sign Accident Report (2162)](#completevalidatesign-accident-report-2162)
    - [Complete/Validate/Sign CA1](#completevalidatesign-ca1)
    - [Complete/Validate/Sign CA2](#completevalidatesign-ca2)
    - [Display/Print CA1/CA2](#displayprint-ca1ca2)
    - [Reports SubMenu](#reports-submenu)
  - [Obsolete Options](#obsolete-options)
  - [Modifications to Menus](#modifications-to-menus)
  - [Data Dictionary Changes in the ASISTS Accident Reporting File (#2260)](#data-dictionary-changes-in-the-asists-accident-reporting-file-2260)
    - [Reason For Deletion Field (#58)](#reason-for-deletion-field-58)
    - [Date/Time Stub Created Field (#90)](#datetime-stub-created-field-90)
    - [Include on OSHA Log Field (#88)](#include-on-osha-log-field-88)
    - [Fatality Field (#89)](#fatality-field-89)
    - [Supervisor Phone Ext Field (#173.1) for the CA1](#supervisor-phone-ext-field-1731-for-the-ca1)
    - [Supervisor Phone Ext Field (#269.1) for the CA2](#supervisor-phone-ext-field-2691-for-the-ca2)
  - [# Chapter 4 Miscellaneous Technical Information](#chapter-4-miscellaneous-technical-information)
  - [Overview](#overview-3)
  - [New Routines](#new-routines)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [Mail Groups, Mail Bulletins, and Security Keys](#mail-groups-mail-bulletins-and-security-keys)

## ## Purpose of the Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Notes section of this document describes the new features and functionality of ASISTS 2.0.

## Note: The User Manual, Installation Guide, Technical Manual and Security Guide for ASISTS 2.0 are presented separately.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

(This page is intentionally left blank)

Table Of Contents

[Purpose of the Release Notes [iii](#purpose-of-the-release-notes)](#purpose-of-the-release-notes)

[Reference Numbering System [iii](#_Toc12761831)](#_Toc12761831)

[1.1 Overview [1](#overview)](#overview)

[1.2 Types of Changes [1](#types-of-changes)](#types-of-changes)

# # Chapter 1 Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main purpose of this release is to enhance the ASISTS roll and scroll VistA package by implementing a Graphical User Interface (GUI) order to increase usability of ASISTS thereby promoting the collection and reporting of accidents and injuries. The scope of the enhancements affects the screens and functionality of ASISTS. The development of this GUI requires the design of application screens that will capture all the data that is presently available in ASISTS. The goal of this GUI design is to be consistent in the look and feel with current VistA GUI applications and provide a consistent, event driven, windows-style, user interface.

Since there are differences between how the ASISTS roll and scroll and the ASISTS GUI work, a claim that is initiated using the roll and scroll must be completed using the roll and scroll. The same is true for the ASISTS GUI, if the claim is begun with GUI, it must be completed with GUI. This is to assure that all fields that are required for the transmission of claims to the Department of Labor are properly populated. Failure to follow this process may result in the rejection of claims at the Austin Automation Center.

The information contained in this document is not intended to replace the User Manual or On-line help documentation. New functionality is briefly discussed so that readers are aware of high level functional changes. The User Manual or On-line help should be used to obtain detailed information regarding specific functionality.

## Types of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the main focus of ASISTS v2.0 was to implement a GUI, both bug fixes and minor enhancements are introduced with this release and will be described in detail below. The main new functionality consists of an option for Employee Health, Safety Officers, and Workers’ Compensation specialist to create and run reports from data collected on the Accident Report (2162).

# Chapter 2 Bug Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bug fixes described below have been fixed in both the ASISTS roll and scroll and GUI versions.

## Bug fixes as the result of NOIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PUG-1101-51611 XMDUZ WRONG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sender for the Mailman bulletin’s, OOPS WC SIGNED and OOPS WC EDITED has been changed to the Postmaster. This will prevent programming staff from receiving a copy of the bulletin.

### ASH-0901-31438 Questions CA-1’s and CA-2’s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Made the ILLNESS OCCURRED ZIP CODE field (#213) required prior to the Supervisor or Workers’ Compensation Specialist being able to electronically sign a claim. This modification will prevent users from having to create an amendment so that the claim can be electronically submitted to the Department of Labor.

### HOU-1001-72833 Undefined error WP+19^OOPSDOLX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A problem with Word Processing fields caused an \<UNDEFINED\> error at WP+19^OOPSDOLX. This error occurred if data had been entered in a word processing field and then deleted.

### ### ### WRJ-1201-11937 Pulling wrong employee information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a claim is created for an Employee, fields are ‘pulled’ from the PAID Employee file (#450). If there were two entries in the PAID file with the exact name, then the Pay Plan, Salary, and Retirement were not correctly being populated in ASISTS. The result of this error is that the required fields did not properly populate the ASISTS Accident Reporting File (#2260). This has been corrected.

### ### ALT-0102-23246 Employee Occupation Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, valid occupation codes were between 0 and 2200 and 2500 through 9000. At the beginning of the fiscal year the occupation codes were updated to allow for codes between 0 and 2300 and 2500 through 9000. Updated the routines used in the transmission of claims to DOL to transmit claims with Occupation Codes in the range 2200 – 2300.

### ## Bug fixes / Modifications initiated by developers or requested by TAG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Third Party Fields in the CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous to this release an ‘Y’es Response to Injury Caused By 3<sup>RD</sup> Party did not result in the remaining Third Party fields being required. Made fields Third Party Name (#259), Third Party Address (#260), Third Party City (#261), Third Party State (#262), and Third Party Zip Code (#263) required if field Injury Caused By 3rd Party (#258) is responded to with a ‘Y’es.

### Injury Address Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Made fields Injury Occurred Address (#183), Injury Occurred City (#184), Injury Occurred State (#185), and Zip Code Where Injury Occurred (#181) required before the claim can be electronically signed by the Supervisor or Workers’ Compensation Specialist.

### ASISTS DOL Anatomical Location Codes file (2261.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of this file was changed for Patch 8 (OOPS\*1.0\*8), but was inadvertently left out of the KIDS build for that patch. With a full version release, the name will now be changed.

### Changes made in data extraction routines for transmission of claims to DOL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Transmission of Last Name

For claims electronically transmitted to DOL, spaces in the field in segment OP01, field 10 (Last Name) have been removed. This does not change or affect how ASISTS files the Person Involved field (#1) in the ASISTS Accident Reporting file (#2260). The full name, as it is entered, is filed.

#### Duplicate claim transmissions

In certain circumstances, claims that have been transmitted to DOL via the AAC are retransmitted causing a duplicate error message being generated by the AAC back to the facility. A temporary solution is being provided in this release so that any duplicate entries in the “AW” cross reference of file \#2260 are removed when the claim is first transmitted. This will eliminate the possibility of ASISTS attempting to re-send a claim previously transmitted. A different long term solution may be provided in the future.

#### Pay Grade and Step for Volunteers and Fee Basis employees

Claims for either Volunteers or Fee Basis employees are sent to the DOL without including a Pay Grade or Step. Prior to this modification, the Pay Grade and Step for Fee Basis employees was transmitted to the AAC. This change is being implemented as claims for either of these Personnel Status would not have a valid Pay Grade and Step.

In conjunction with this change, additional error checking has been incorporated on individuals whose Pay Plan (ASISTS Accident Reporting file (#2260), field \#63) equals ‘OT’. A pay plan of ‘OT’ should only exist if the Personnel Status (file \#2260, field \#2) equals Employee and the Pay Plan (PAID Employee file (#450), field \#20) equals F (Fee Basis). The error checking that occurs is to ensure that the claim being submitted meets the requirements for transmitting the Claim to the DOL via the Austin Automation Center. Additional requirements that must be met are that the Emp Retirement Coverage (file \#2260, field \#60) must equal ‘Other’ and the Emp Retirement Coverage Desc (file \#2260, field \#61) must be entered, the Grade (file \#2260, field \#16) must equal ‘00’ with a Step (file \#2260, field \#17) of ‘N’. Additionally, if the claim is for a CA1, the Pay Rate Dollar (file \#2260, field \#166) cannot exceed \$999.99. If the above criteria is not met, then the following is displayed from the Workers’ Compensation Menu, the Workers' Compensation Edit CA1/CA2 Option from the roll and scroll version (Note a similar but not exact message is displayed for the GUI):

> Validating data on form CA1.

> This person does not appear to be eligible for submitting a claim

> to DOL, please review the RETIREMENT, GRADE, STEP, PAY

> PLAN, PAY RATE and PAY RATE PER Fields. You may need to

> contact your Human Resources Department or IRM for assistance.

#### Removal of Supervisors Signature on 2162

In certain circumstances, when the Safety officer was in the Edit Report of Incident, the Supervisors signature, if present, was being overwritten by the Safety Officer’s signature. This has been corrected. Additionally, added code to assure that in all cases the Supervisor must sign the 2162 before the Safety Officer can.

#### Valid Personnel Status for creating a CA1 or CA2

In the past, claims with a PERSONNEL STATUS of Employee, Volunteer, Non-PAID Employee, Medical Student, Nursing Student, Other Student, or Resident Physician on the 2162 could initiate either a CA1 or CA2. ASISTS has been modified to only allow CA1 or CA2 claims to be initiated for an Employee, Volunteer, or Non-Paid Employee.

### Physician Data on CA1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Physician information is no longer required on the CA1. However, if the Physician Name is entered then the address information will be required as the Physician name cannot be sent to DOL without their address information. Similar error checking has been added to the CA2. These changes have been applied to both the ASISTS roll and scroll and the GUI versions.

### Bug in transmission of 2162 data to the ASISTS National Database (NDB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A problem that resulted in a claim not being processed into the ASISTS NDB if data was present in the Safety Device Not Used field (#85) in the ASISTS Accident Reporting File (#2260) was corrected.

# Chapter 3 New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter details the modifications and changes that have been made to ASISTS that provides new functionality. The enhancements that have not been implemented in ASISTS roll and scroll will be noted when described below.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Complete/Validate/Sign Accident Report (2162)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be accessed from the Supervisor, Employee Health, Safety Officer, and Workers’ Compensation menus. Note, that from the Employee Health menu the option is called the Edit/Validate Stub Record. This functionality combines the Edit Report of Incident and Validate and Sign CA1, CA2, or 2162 menu options from the roll and scroll version. Users will now have separate options to complete the 2162, CA1, and CA2 forms. Fields/Prompts that are available from the Supervisor (or any) menu from the roll and scroll, will be available from the GUI menu. If a field/prompt is not available from the Supervisor (or any) menu for roll and scroll, it will not be available from the GUI. Required fields are marked with a double asterisk (\*\*). A screen print displaying all available tabs is shown below. Note that all tabs may not be available from all menus. Additionally, the Exposure and Equipment tabs are not visible unless the Type of Incident is either an Exposure to Body Fluids/Splash, Hollow Bore Needlestick, Sharps Exposure, or Suture Needlestick. The dependencies for required fields for these types of incidents are the same for GUI and roll and scroll.

To determine if a case was initiated using the roll and scroll version vs. GUI, the Date/Time Stub Created field (#90) in the ASISTS Accident Reporting file (#2260) can be checked. This field is only present if the claim was initiated using the GUI version and can be viewed by running the Print Report of Accident Report on the Supervisor, Employee Health, Safety, Workers’ Compensation, or Union menus.

![](asists-gui-version-2-release-notes/002.png)

Two new fields have been added for the Safety Officer to complete. They are the Include on OSHA Log (file \#2260, field \#88) and Fatality (file \#2260, field \#89). The fields are described in the Data Dictionary section (#3.4) of this document. They are located on the Signatures Tab which is shown below:

![](asists-gui-version-2-release-notes/003.png)

The prompts Lost Time (file \#2260, field \#33), Duty Returned To (file \#2260, field \#32), Fatality (file \#2260, field \#89), and Include on OSHA Log (file \#2260, field \#88) can only be answered from the Safety Officer menu. If the response to Lost Time is ‘N’o then Duty Returned To is required if the Person Involved is an Employee, Non-Paid Employee or Volunteers. If the Person Involved does not have one of these Personnel Status’ then Lost Time is not required.

The Complete Report of Accident (2162) (Safety Officer and Workers’ Comp Menu) option has been made obsolete with ASISTS GUI. Now, when the Safety Officer signs the 2162 they will be prompted to close the case.

These changes are only available in the ASISTS GUI version.

### Complete/Validate/Sign CA1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be accessed from Employee, Supervisor, Safety Officer, and Workers’ Compensation menus. This functionality combines the Edit Report of Incident and Validate and Sign CA1, CA2, or 2162 menu options from the roll and scroll version.. Users will now have separate options to complete the 2162, CA1, and CA2 forms. A field that is available from the Supervisor (or any) menu from the roll and scroll, will be available from the GUI menu. If a field/prompt is not available from the Supervisor (or any) menu for roll and scroll, it will not be available from the GUI. Required fields are marked with a double asterisk (\*\*). A screen print displaying all available tabs is shown below. Note that all tabs may not be available from all menus.

![](asists-gui-version-2-release-notes/004.png)

A few changes have been made and are noted below. When entering Witness information, if the Name button is clicked, the user will be able to select a witness from a lookup into the PAID Employee File (#450), otherwise a witness name and address information can be directly entered in the edit boxes. If a lookup is done, the address information is ‘pulled’ from the Institution File (#4) based on the Station number of the Person Involved in the claim. A screen print of the form with the witness name is shown:

![](asists-gui-version-2-release-notes/005.png)

The second change involves default information for the Employee Duty Station. The Duty Station can be selected from a drop down list of stations. Once a station is selected, the address information is retrieved from the Institution File (#4) and the Employee Duty Station Address fields are populated. If a different Duty Station is selected, the ‘old’ address information is replaced by the address information for the newly selected station.

The Injury Address fields, Injury Occurred Address (#183), Injury Occurred City (#184), Injury Occurred State (#185), and Zip Code Where Injury Occurred (#181) are also now ‘pulled’ from the Institution file (#4) using the Station Number (#13) entered when the case was created. Since the Street Addr. 1 (# 1.01) and the City (1.03) fields in the Institution file (#4) can be up to 40 characters long, the default value is truncated to the corresponding ASISTS fields if necessary. The only time the default value is ‘pulled’ into an Injury Address field is if the field is blank.

Another change is that the home address information; street, city, state, and zip code are ‘pulled’ from the PAID Employee File (#450) if the Personnel Status of the Person Involved is an Employee. The home phone number is also ‘pulled’ from the New Person File (#200).

A new code has been added for Dependents: None. This item was added to the list in GUI at the request of TAG. However, it is not a valid code that can be transmitted to the DOL so it is not stored in file \#2260.

These changes are only available in the ASISTS GUI version.

### Complete/Validate/Sign CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be accessed from Employee, Supervisor, Safety Officer, and Workers’ Compensation menus. This functionality combines the Edit Report of Incident and Validate and Sign CA1, CA2, or 2162 menu options from the roll and scroll version.. Users will now have separate options to complete the 2162, CA1, and CA2 forms. A field that is available from the Workers’ Comp (or any) menu from the roll and scroll, will be available from the GUI menu. If a field/prompt is not available from the Workers’ Comp (or any) menu for roll and scroll, it will not be available from the GUI. Required fields are marked with a double asterisk (\*\*). A screen print displaying all available tabs is shown below. Note that all tabs may not be available from all menus.

The functionality coded in the CA1 for the Dependents field and Employee Duty Station fields is also available in the CA2. Additionally, if the Personnel Status of the Person Involved is an Employee the address and phone information is also ‘pulled’ as described for the CA1.

![](asists-gui-version-2-release-notes/006.png)

The Illness Address fields, Illness Occurred Address (#210), Illness Occurred City (#211), Illness Occurred State (#212), and Illness Occurred Zip Code (#213) are also now ‘pulled’ from the Institution file (#4) using the Station Number (#13) entered when the case was created. Since the Street Addr. 1 (# 1.01) and the City (1.03) fields in the Institution file (#4) can be up to 40 characters long, the default value is truncated to the corresponding ASISTS fields if necessary. The only time the default value is ‘pulled’ into an Injury Address field is if the field is blank.

These changes are only available in the ASISTS GUI version.

### Display/Print CA1/CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display and Print CA1/CA2 options have been combined in the ASISTS GUI version. The ability to display the CA form to the screen is now available. Additionally, the claim can be printed to any printer connected to your PC. The following screen is used to select a claim and then choose whether to print or preview your selection:

![](asists-gui-version-2-release-notes/007.png)

This option is only available in the ASISTS GUI version.

### Reports SubMenu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new menu option has been added to the Employee Health, Safety Officer, Workers’ Comp and Union menus. This menu option contains the following options for running reports: Log of Federal Occupational Injuries and Illnesses, Log of Needlestick Incidents, Print Accident Report Status, Print Report of Accident, and Incident Reports except on the Union menu which only has the Log of Federal Occupational Injuries and Illnesses, Print Accident Report Status, and Print Report of Accident. The reports will be described below.

Currently, reports can only be run for a single station or for all stations. If the report is run for all stations, sorting is not performed so that each station is grouped together. This feature was not completed due to time constraints with the project but is on the list for future consideration. A report can be run for each station separately to obtain any station grouping necessary.

All reports can be printed without previewing them to the screen or previewed prior to printing.

Three of these reports require that special software (Borland Database Engine) be installed before they can be run. This software is available with the ASISTS GUI package (see the installation guide for instructions).

The reports requiring the Reports Data Base installation are:

Log of Federal Occupational Injuries and Illnesses

Log of Needlestick Incidents

Incident Reports

Therefore, the Reports Data Base installation can be limited to the few desktops used by Employee Health, Safety, Union, and Workers’ Compensation personnel.

The following reports, which are used by all areas including supervisors, do not require the Reports Data Base installation:

Print Report of Accident

Print Accident Report Status

This option is only available in the ASISTS GUI version.

#### Log of Federal Occupational Injuries and Illnesses

The Log of Federal Occupational Injuries and Illnesses has been changed to meet the OSHA requirements under and by the direction of the Program Office. The report output format was dictated by these requirements. The criteria for inclusion on this report is that the field, Include on OSHA Log, entered by the Safety Officer from the Complete/Validate/Sign 2162 option, must be ‘Y’es. The report can be run for any date range, by station and include names (unless run from the Union menu) or exclude names. The Start Date is defaulted to a date 6 months prior to ‘today’s’ date.

The screen used to run the report is shown below:

![](asists-gui-version-2-release-notes/008.png)

This option in this format is only available in the ASISTS GUI version.

#### Log of Needlestick Incidents

The criteria for inclusion on this report is that the field, Type of Incident (file \#2260, field \#3), entered from the Complete/Validate/Sign 2162 option (Edit/Validate Stub Record from the Employee Health Menu), must be either an Exposure to Body Fluids/Splash, Hollow Bore Needlestick, Sharps Exposure, or Suture Needlestick. The report can be run for any date range, by station and include names or exclude names. The Start Date is defaulted to a date 6 months prior to ‘today’s’ date.

The screen used to run the report is shown below:

![](asists-gui-version-2-release-notes/009.png)

This option in this format is only available in the ASISTS GUI version.

#### Print Accident Report Status

The criteria for inclusion on this report is that the Case Status (file \#2260, field \#51) must be open. The report can be run for any date range, and by station. The Start Date is defaulted to a date 6 months prior to ‘today’s’ date. A new column for this report has been added to indicate whether the Workers’ Compensation specialist has signed off giving their Ok to transmit the claim to DOL.

The screen used to run the report is shown below:

![](asists-gui-version-2-release-notes/010.png)

This option in this format is only available in the ASISTS GUI version.

#### Print Report of Accident

The Print Report of Accident formats the data to more closely match a 2162 form. The screen used to select a case is shown below:

> ![](asists-gui-version-2-release-notes/011.png)

After a case is selected the user can print or preview the claim (prior to printing). The same criteria is used in the roll and scroll and the GUI version for accessing a claim or printing one from the Union menu.

This option in this format is only available in the ASISTS GUI version.

#### Incident Reports

This report contains new functionality to provide additional information to the ASISTS user. The data used for this report comes only from the data collected on the 2162. The screen used to define the report is shown below:

![](asists-gui-version-2-release-notes/012.png)

There are seven (7) different Types of Reports that can be selected: Type of Incidents, Occupation Code, Characterization of Injury, Service, Body Parts, Day of Week, and Time of Day. The date range, case status, lost time, station, and personnel status can be used to further select what type of report (which claims should be included) should be produced. Additionally, the format of the report can be specified as a standard report, pie chart, bar graph, or Excel spreadsheet.

The body part report groups the body parts into the following groups (note that the body parts are separated by a ~ to avoid confusion with using a comma):

Abdomen: Abdomen~ Bladder~ Urethra~ Intestines~ Both Kidneys~ Single Kidney~ Liver~ Spleen~ Stomach

Arm(S) Lower: Single Arm And/Or Wrist~ Both Arms And/Or Wrist~ Both Forearms~ Both Wrists~ Single Forearm~ Single Wrist

Arm(S) Upper: Arm(S), Multiple Sites~ Arm(S), Other~ Both Upper Arms~ Single Upper Arm

Back (Lumbar Region): Lower Back/Buttocks

Back (Upper): Upper Back

Chest: Chest~ Sternum

Ear(S): Both Ears (External)~ Both Ears~ Single Ear (External)~ Single Ear

Elbow: Both Elbows~ Single Elbow

Eye(S): Both Eyes (External)~ Both Eyes~ Single Eye (External)~ Single Eye

Face: Bones Of Face, Other(S)~ Chin~ Face~ Jaw~ Mandible~ Lips~ Mouth~ Nose~ Nose, Internal~ Teeth~ Tongue

Foot, Includes Toes: Both Feet~ Both Great Toes~ Oth/Mult Toe(S), Single Foot~ Oth/Mutl Toe(S), Both Feet~ Single Foot~ Single Great Toe

Hand(S),Includes Fingers: Both First Fingers~ Both Fourth Fingers~ Both Hands~ Both Second Fingers~ Both Third Fingers~ Both Thumbs~ Multiple Fingers, Both Hands~ Multiple Fingers, Single Hand~ Single First Finger~ Single Fourth Finger~ Single Hand~ Single Second Finger~ Single Third Finger~ Single Thumb

Knees: Both Knees~ Single Knee

Leg(S), Lower: Both Lower Leg/Ankles~ Single Lower Leg/Ankle

Leg(S), Upper: Leg(S), Multiple Sites~ Leg(S), Other

Neck: Neck~ Larynx~ Throat~ Other

Not Elsewhere Classified: Anatomic Site Not Mentioned~ Both Hips/Thighs~ Both Legs/Hips/Ankles/Buttocks~ External, External, Other~ Multiple Anatomical Sites~ Nerve~ Pelvis~ Single Leg/Hip/Ankle/Buttock~ Single Hip/Thigh

Reproductive Organs: Both Breasts~ Both Testicles~ Penis~ Reproductive Organs~ Single Breast~ Single Testicle~ Vulva/Vagina

Ribs: Rib~ Ribs, Multiple

Shoulder: Both Clavicles~ Both Scapulae~ Both Shoulders~ Single Clavicle~ Single Scapula~ Single Shoulder

Skull/Head: Brain~ Head, External, Multiple Sites~ Head, External, Other~ Head, Internal, Multiple Sites~ Head, Internal, Other~ Scalp~ Skull (Cranial Bones)~ Sinus (Es)

Spinal Cord: Spinal Cord~ Vertebra (Spine, Spinal Col)

Thorax: Heart~ Both Lungs~ Single Lung

Trunk: Side/Flank~ Trunk Bone, Other~ Trunk, External, Mult Sites~ Trunk, Internal, Mult Organs~ Trunk, Internal, Other~ Trunk, Multiple Bones~ Waist

This option is only available in the ASISTS GUI version.

## Obsolete Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality contained in the following options were incorporated into new options described above and will not be explicitly found in the GUI version:

Display CA1 or CA2

Validate and Sign CA-1 or CA-2 (Employee and Workers’ Comp Menu)

Edit Report of Incident (Supervisor, Safety Officer, Workers’ Comp Menu)

Validate and Sign CA1,CA2 or 2162 (Supervisor, Safety Officer, Workers’ Comp Menu)

Complete Report of Accident (2162) (Safety Officer and Workers’ Comp Menu)

Edit Stub Record (Employee Health, Safety Officer and Workers’ Comp Menu)

Validate and Sign 2162 (Safety Officer Menu)

Complete Employee CA-1 & CA-2 (Workers’ Comp Menu)

## Modifications to Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create Amendment Option has been removed from the Supervisors menu at the request of the TAG. This functionality is to be provided by the Safety Officer or Workers’ Compensation personnel.

## Data Dictionary Changes in the ASISTS Accident Reporting File (#2260)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reason For Deletion Field (#58)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The length of this field has been increased from 30 to 60 characters. (ASISTS roll and scroll and GUI).

### Date/Time Stub Created Field (#90)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field will capture the date and time the initial stub record (Create Accident/Illness Report) was filed in the system. It will be displayed at the bottom of the Print Report of Accident. (ASISTS GUI only).

### Include on OSHA Log Field (#88)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field is a Set of Codes field with valid responses of Yes or No. It should be completed by the Safety Officer and will indicate whether to include the claim on the Log of Federal Occupational Injuries and Illnesses. This field is required prior to the Safety Officer electronically signing the 2162. Include on OSHA Log is collected on the Signatures Tab in the Complete/Validate/Sign Accident Report (2162) menu option from the Safety menu. If an ‘Y’es is entered in this field the claim will be included on the new Log, otherwise it will not. (ASISTS GUI only).

### Fatality Field (#89)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field is a Set of Codes field with valid responses of either Yes or No. This field will indicate whether the incident that is being reported on this claim resulted in a fatality and will be used to complete the new OSHA Log. Fatality is collected on the Signatures Tab in the Complete/Validate/Sign Accident Report (2162) menu option from the Safety menu. It should be completed by the Safety Officer and is required prior to the Safety Officer electronically signing the 2162. (ASISTS GUI only).

### Supervisor Phone Ext Field (#173.1) for the CA1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field is a free text field that must be 3 to 20 characters if completed. (ASISTS GUI only).

### Supervisor Phone Ext Field (#269.1) for the CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field is a free text field that must be 3 to 20 characters if completed. (ASISTS GUI only).

## # Chapter 4 Miscellaneous Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed technical information will be presented in the ASISTS V 2.0 Technical Guide. A brief introduction of technical information will be described below.

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> OOPSGUI0 OOPSGUI6

> OOPSGUI1 OOPSGUI7

> OOPSGUI2 OOPSGUI8

> OOPSGUI3 OOPSGUI9

> OOPSGUI4 OOPSGUIF

> OOPSGUI5 OOPSGUIT

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> OOPS APPROVE SIGN FOR EMPLOYEE OOPS CHANGE CASE STATUS

> OOPS CHECK PAID EMP DATA OOPS CLEAR SIGNATURE

> OOPS CREATE AMENDMENT OOPS DELETE SITEP STATION

> OOPS DELETE SITEPAR STATION OOPS DELETE UNION

> OOPS DELETE WITNESS OOPS EDIT 2260

> OOPS EDIT SITE PARAMETER OOPS EDIT SITEPAR STATION

> OOPS EMPLOYEE DATA OOPS GET 2260 DATA

> OOPS GET ASISTS CASE OOPS GET BODY PART

> OOPS GET CASE NUMBERS OOPS GET CKRANGE

> OOPS GET DATA OOPS GET DEFAULT MD

> OOPS GET DUPLICATES OOPS GET NOI CODE

> OOPS GET OSHA DATA OOPS GET POINTED TO

> OOPS GET PRT ACC STATUS RPT OOPS GET SINGLE FIELD

> OOPS GET SITE PARAMETER OOPS GET SUPERVISOR

> OOPS GET STATION INFORMATION OOPS GET UNION

> OOPS GET WITNESSES OOPS INCIDENT REPORT

> OOPS LOAD OOPS OOPS MANUAL XMIT DATA

> OOPS NEEDLESTICK LOG OOPS NEW PERSON DATA

> OOPS PUT UNION OOPS RELEASE RECORD LOCK

> OOPS REMOTE GET USER OPTIONS OOPS REPLACE DATE/TIME

> OOPS REPLACE MULTIPLE OOPS REPLACE WP

> OOPS SET FIELD OOPS SET RECORD LOCK

> OOPS UNION CONSENT OOPS VALIDATE AND SIGN

> OOPS VALIDATE TIME OOPS WCEDIT

> OOPS WITNESS CREATE OOPS WITNESS DELETE

> OOPS WITNESS EDIT

## Mail Groups, Mail Bulletins, and Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new Mail Groups, Bulletins, or Security Keys introduced with this new version.