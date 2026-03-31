---
title: OOPS*2*15 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: OOPS
app_name: Automated Safety Incident Surveillance Tracking System
section: FIN
app_status: active
pkg_ns: OOPS
patch_ver: 2
patch_id: OOPS*2*15
group_key: "OOPS:OOPS:2"
file_numbers: []
security_keys: []
menu_options: 4
description: The main purpose of this release is to implement changes regarding privacy act requirements, modify the Accident report, update the Request for Compensation Form (CA-7), and minor bug fixes.
audience: 
keywords: 
  - report
  - table
  - contents
  - incident
  - form
  - accident
  - print
  - create
  - status
  - added
page_count: 0
word_count: 2210
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_15_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_15_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=56"
---

![](oops-2-15-release-notes/001.png)

Automated Safety Incident Surveillance Tracking System (ASISTS) V. 2.0Patch OOPS\*2\*15 Release NotesSeptember 2008

Office of Enterprise Development

Management & Financial Systems

Preface

Purpose of the Release Notes

The Release Notes document describes the new features and functionality of Patch OOPS\*2\*15.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

Table of Contents

[1.1 Overview [1](#overview)](#overview)

# # Chapter 1 - Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Reference Numbering System](#reference-numbering-system)
- [# Chapter 1 - Introduction](#chapter-1-introduction)
  - [Overview](#overview)
- [Chapter 2 - Functional Changes](#chapter-2-functional-changes)
  - [## Main Menu Options](#main-menu-options)
  - [Modification to the option Create Accident/Illness Report](#modification-to-the-option-create-accidentillness-report)
  - [Modify the Complete/Validate/Sign Accident Report (2162)](#modify-the-completevalidatesign-accident-report-2162)
  - [Modify Print Report of Accident (2162)](#modify-print-report-of-accident-2162)
  - [Modified the Print Accident Report Status](#modified-the-print-accident-report-status)
  - [Error messages (in Help) updated](#error-messages-in-help-updated)
  - [Added new bulletin: OOPS INCIDENT OUTCOME REQUIRED](#added-new-bulletin-oops-incident-outcome-required)
  - [Modification to the CA-7 (Request for Compensation) (Enter/Edit form)](#modification-to-the-ca-7-request-for-compensation-enteredit-form)
  - [Modifications to the Print CA-7 Report Option](#modifications-to-the-print-ca-7-report-option)
  - [Change to Log of Needlestick Report](#change-to-log-of-needlestick-report)
- [Chapter 3 - Bug Fixes](#chapter-3-bug-fixes)
  - [## Bug fixes without Remedy Tickets](#bug-fixes-without-remedy-tickets)
    - [Error when the Occupational Series and Title field is longer than 30](#error-when-the-occupational-series-and-title-field-is-longer-than-30)
    - [Problem with the Print Accident Report Status (now Print Incident Report Status report)](#problem-with-the-print-accident-report-status-now-print-incident-report-status-report)
    - [Create Accident/Illness Report (now Create Incident Report)](#create-accidentillness-report-now-create-incident-report)
    - [Create Accident/Illness Report (now Create Incident Report)](#create-accidentillness-report-now-create-incident-report-1)
    - [CA-1 (Enter/Edit Form)](#ca-1-enteredit-form)
    - [Print CA1/CA2](#print-ca1ca2)
    - [Log of Needlestick Report](#log-of-needlestick-report)
  - [Bug fixes with Remedy Tickets](#bug-fixes-with-remedy-tickets)
    - [HD0000000130515](#hd0000000130515)
    - [HD0000000152026](#hd0000000152026)
    - [HD0000000183787](#hd0000000183787)
    - [HD0000000206374](#hd0000000206374)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main purpose of this release is to implement changes regarding privacy act requirements, modify the Accident report, update the Request for Compensation Form (CA-7), and minor bug fixes.

The information contained in this document is not intended to replace the User Manual or On-line help documentation. New functionality is briefly discussed so that readers are aware of high level functional changes. The User Manual or On-line help should be used to obtain detailed information regarding specific functionality.

# Chapter 2 - Functional Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Main Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu options available to the Occupational Health, Safety Officer and Workers’ Compensation (WC) specialist have been modified to ensure that the privacy of individuals in ASISTS is protected. This involved removing or modifying options on menus.

The following options have been removed from the Occupational Health menu.

Print CA1/CA2

Approve Workers' Comp Signing for Employee

The following options have been removed from the Safety menu.

Print CA1/CA2

Approve Workers' Comp Signing for Employee

Complete/Validate/Sign CA1

Complete/Validate/Sign CA2

The following options have been removed from the Workers’ Compensation menu.

Create Accident/Illness Report

Create Amendment

Complete/Validate/Sign Accident Report (2162)

Classify Incident Outcome

Display Incident Outcome Report

Display Incidence Rates Worksheet

The following option has been modified.

> Electronically Sign for Employee - removed requirements that the Safety officer and Occupational Health must approve the Workers’ Compensation specialist signing for the employee.

Additionally, modifications have been made to the terminology of the Accident/Illness form by removing references to Form 2162. All references to “Accident/Illness (2162)” have been changed to “Incident”.

Specifically, the following options have been renamed.

> From: Create Accident/Illness Report

> To: Create Incident Report

> From: Complete/Validate/Sign Accident Report (2162)

> To: Complete/Validate/Sign Incident Report

> From: Print Report of Accident (2162)

> To: Print Report of Incident

> From: Print Accident Report Status

> To: Print Incident Report Status

> From: Manual Transmit of National Database (2162) Data

> To: Manual Transmit of National Database Data

> From: Incident Reports

> To: Summary Incident Reports

## Modification to the option Create Accident/Illness Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option name and screen title was changed to Create Incident Report.

Added *SEVERITY OF INJURY* prompt in the Incident information panel and modified the logic so that if the incident is an injury, this information is collected. If the incident is an illness, the illness type is collected. The appropriate prompt is displayed based on the incident type.

The Severity of Injury valid codes are:

> 1 No Treatment Required

> 2 First Aid Only

> 3 Medical Treatment

> 4 Disabling Injury

> 5 Fatality

The following six prompts in the Quick OSHA Log Assessment panel have had the default values changed from ‘No’ to ‘None Selected’.

> Was there Loss of Consciousness

> Hospitalized overnight as in-patient

> Treated in non-VA Emergency Room

> Was prescription strength medication ordered/given

> Was non-Rx medication ordered/given at Rx strength

> Initial return to work status

The *None Selected* radio button was added and is now the default when the user opens the form. The default value must be changed before a new case can be created. The ‘None Selected’ choice was necessary so that a screen-reader user could tab into the radio group to maintain 508 compliance.

A “behind the scenes” change was made to the M code. The employee address fields: street, city, state, zip code, and home phone number will no longer be “pulled” from the PAID Employee file (#450) and inserted as default values when creating a new case. These prompts are required and the user will now have to enter those fields before saving the data.

## Modify the Complete/Validate/Sign Accident Report (2162)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of the option was changed to Complete/Validate/Sign Incident Report.

A new tab, Other Factors, has been added to collect additional information relating to the cause of the incident.

![](oops-2-15-release-notes/002.png)

The six new prompts (with valid responses) are as follows.

Weather Factor

> Snow/Ice

> Dust Storm

> Lightning

> High Temperature

> Low Temperature

> Humidity

> Fog

> Rain

> Windstorm

> Weather - N.E.C.

> Weather Not a Factor

Source of Incident

> Unpowered Equipment, Furnishings, Supplies

> Powered Equipment, Appliances, Machines

> Building Material, Feature or Condition

> Toxic Substance, Radiation Source

> Vehicle

> Person

> Patient Handling

Cause of Incident

> Equipment or Environment

> Person

> Nature

> Cause Unknown

Prevention Method

> Training

> More Staff

> Motivation

> Better Equipment or Material

> Better Planning/Coordination

> Improved written Procedures

> More Funds for Hazard Elimination

> Personnel Action

> Preventive - N.E.C.

> None

Additional Cause of Incident

> Equipment or Environment

> Person

> Nature

> No additional Cause

Status of Corrective Action

> Taken

> Requested and Anticipated

> Requested

> None

These fields must be answered before the supervisor can electronically sign the form.

Additionally, the General Settings tab was modified by moving the Description of Incident prompt to the Other Factors tab. The verbiage “Note: No personal identifiers should be used!” was added to the descriptive prompt narrative.

The General Setting tab has been modified as shown below.

![](oops-2-15-release-notes/003.png)

The text “(No personal identifiers should be used)” was added to the Corrective Action and Safety Comments prompt on the Signatures tab as shown below.

![](oops-2-15-release-notes/004.png)

## Modify Print Report of Accident (2162)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of the option was changed to Print Report of Incident.

The report title was changed to Veterans Health Administration Incident report.

A new Report Type was added to the immediate right of Case number on page 1 of the report. The value of this block is derived from the database. If the case has been amended, Report Type = Corrected, otherwise the value is Initial.

The SSN display was changed from the actual value to xxx-xx-NNNN where only the last 4 numbers of the SSN are displayed.

The Date of Birth (DOB) block was changed to the Age at Time of Incident. The age is derived from the DOB and Date/Time of Occurrence.

FORM 2162 was removed from the bottom left hand corner of page 1 of the report.

The report run date and time was added at the bottom right hand corner of each page of the report.

Page 3 of the report was modified by inserting the following new fields at the top of the page and adjusting the OSHA fields towards the bottom.

> Weather Factor

> Source of Incident

> Cause of Incident

> Prevention Method

> Additional Cause of Incident

> Status of Corrective Action

## Modified the Print Accident Report Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The name of the option was changed to Print Incident Report Status.
- The report title was changed to Incident Report Status.
- The SSN display was changed from nnn-nn-nnnn to xxx-xx-nnnn.

## Error messages (in Help) updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The error messages have been updated in the Complete/Validate/Sign Incident Report CA-1, Complete/Validate/Sign Incident Report CA-2, Witness Form (for the CA-1), and in the Print Incident Report Status options to remove references to the 2162 Form (Accident Report) and replace them with Incident or Incident Report.

## Added new bulletin: OOPS INCIDENT OUTCOME REQUIRED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A bulletin will now be sent to the Safety mail group if the response to the Initial Return to Work Status prompt entered in the Create Incident Report or modified in the Complete/Validate/Sign Incident Report is “Days away work” or “Job Transfer/Restriction”.

*Example*

Subj: ASISTS - Incident Outcome Required \[#214\] 05/06/08@13:53 8 lines

From: ASISTS, USER In 'IN' basket. Page 1

-----------------------------------------------------------------------

A new incident has been entered or an existing incident has been

modified where the Initial Return to Work Status for the incident

is "Days Away Work" or "Job Transfer/Restriction".

The Case Number is: 2008-000XX

An entry in the Classify Incident Outcome option is required to

record the dates and the incident outcome for this case.

## Modification to the CA-7 (Request for Compensation) (Enter/Edit form)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new prompt was added in the CA7-Request for Compensation enter/edit form in Section 15. It must be completed before the WC specialist can electronically sign the form. The only data validation completed is that it must be a valid date and cannot precede the date the form was created. An example screen is shown below.

![](oops-2-15-release-notes/005.png)

Correction of an unreported bug fix is included involving Section 6 - The radio buttons were getting reset to “unchecked” after data from the claim had been loaded. This resulted in data being potentially "erased" without the user being aware.

Correction of an unreported bug fix where the signature was not displayed if the user or WC specialist had signed the form - It appeared that the form had not been signed when it had. Additionally, the sign/validate button was not properly enabled when a user entered the form. Corrected the problem so the user could click the sign/validate button and be prompted to sign the form.

## Modifications to the Print CA-7 Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 1 - Changed the “expires” date from 08/31/2005 to 10/31/2008.

Section 3 - Text in this section has been changed as follows.

> From: Have you worked outside your federal job during the period(s) claimed in Section

> 2? (Include salaried, self-employed, commission, volunteer, etc.)

> To: You must report all earnings from employment (outside your federal job); include

> any employment for which you received a salary, wage income, sales

> commissions, piecework, or payment of any kind during the period(s) claimed in

> Section 2. Include self-employment, involvement in business enterprises, as well

> as service with the military forces. Fraudulent concealment of employment or

> failure to report income may result in forfeiture of compensation benefits and/or

> criminal prosecution. Have you worked outside your federal job for the period(s)

> claimed in Section 2?

Section 6c - Added check boxes for the retirement field. If the data value = CSRS then the CSRS box is checked, if FERS then the FERS checkbox should be checked, if SSA then the SSA checkbox should be checked, and if not one of those 3, then the Other check box should be checked.

Changed form reference at bottom right corner of page 1 to: Form CA-7 Rev. June 2005.

Section 10c - Added "D-Z only" underneath the line next to the Class field.

Section 13 - Removed the lines in this section which resulted in underlined text when data was entered in that field.

Section 15 - Increased the size of this section to facilitate adding the new field, Date Claim Form Received from Employee.

A new Privacy Act paragraph (completely new page 4) has been added with the following text.

> In accordance with the Privacy Act of 1974, as amended (5 U.S.C. 552a), you are here by

> notified that: (1) The Federal Employees' Compensation Act, as amended and extended

> (5 U.S.C. 8101, et seq.) (FECA) is administered by the Office of Workers' Compensation

> Programs of the U. S .Department of Labor, which receives and maintains personal

> information on claimants and their immediate families. (2) Information which the Office

> has will be used to determine eligibility for and the amount of benefits payable under the

> FECA, and may be verified through computer matches or other appropriate means. (3)

> Information may be given to the Federal agency which employed the claimant at the time

> of injury in order to verify statements made, answer questions concerning the status of

> the claim, verify billing, and to consider issues relating to retention, rehire, or other

> relevant matters. (4) Information may also be given to other Federal agencies, other

> government entities, and to private-sector agencies and/or employers as part of

> rehabilitative and other return-to-work programs and services. (5) Information may be

> disclosed to physicians and other healthcare providers for use in providing treatment or

> medical/vocational rehabilitation, making evaluations for the Office, and for other

> purposes related to the medical management of the claim. (6) Information may be given

> to Federal, state and local agencies for law enforcement purposes, to obtain information

> relevant to a decision under the FECA, to determine whether benefits are being paid

> properly, including whether prohibited dual payments are being made, and, where

> appropriate, to pursue salary/administrative offset and debt collection actions required or

> permitted by the FECA and/or the Debt Collection Act. (7) Disclosure of the claimant's

> social security number (SSN) or tax identifying number (TIN) on this form is mandatory.

> The SSN and/or TIN, and other information maintained by the Office, may be used for

> identification, to support debt collection efforts carried on by the Federal government,

> and for other purposes required or authorized by law. (8) Failure to disclose all requested

> information may delay the processing of the claim or the payment of benefits, or may

> result in an unfavorable decision or reduced level of benefits.

> Note: This notice applies to all forms requesting information that you might receive

> from the Office in connection with the processing and adjudication of the claim you

> filed under the FECA.

> Note: The current hardcopy form can be downloaded from:

> http://www.dol.gov/libraryforms/go-us-dol-form.asp?FormNumber=362

## Change to Log of Needlestick Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Include Names of Persons Involved prompt has been removed from the Enter/Edit screen. Prior to this change, the name field would either be blank or contain the words “Privacy Case”.

The report entry form now appears as shown below.

![](oops-2-15-release-notes/006.png)

A lost time indicator has been added back into the report. It was removed with Patch OOPS\*2\*7. A new column has been added, Lost Time, which will contain either Yes or No. If the response for the prompt INITIAL RETURN TO WORK STATUS is DAYS AWAY WORK, then the Lost Time column will be Yes; otherwise the Lost Time column will be No.

# Chapter 3 - Bug Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Bug fixes without Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Error when the Occupational Series and Title field is longer than 30

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An error will occur when sending a claim to the Department of Labor when the Occupational Series and Title field (pulled from the PAID EMPLOYEE File \#450) is longer than 30 characters. Modified the M server side code to only accept the first 30 characters when auto populating an ASISTS claim with this data. This modification will only be apparent to the user if the occupation for the employee is truncated in the CA-1 or CA-2.

### Problem with the Print Accident Report Status (now Print Incident Report Status report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There was a condition where an Incident Report Status report would not print data when there were cases that met the criteria and should have been included on the report. This was the result of a variable not being removed properly in all cases. The input transform for eight date fields has been modified to remove the offending variable.

> In the ASISTS ACCIDENT REPORTING File (#2260), the fields are:

> DATE/TIME STUB CREATED

> DATE OUTCOME CREATED

> LAST EDIT DATE

> DATE/TIME WORK STOPPED (CA-1)

> DATE PAY STOPPED (CA-1)

> DATE 45 DAY PERIOD BEGAN

> DATE/TIME RETURNED TO WORK

> DATE/TIME WORK STOPPED (CA-2)

> DATE/TIME PAY STOPPED (CA-2)

DATE/TIME RETURNED TO WORK

> In the ASISTS SITE PARAMETER FILE, STATION SUBFILE (#2262.315), the field is: OSHA MONTH/YEAR

### Create Accident/Illness Report (now Create Incident Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Proper time error checking did not occur in this option when the Incident was an Illness, the Date First Aware of Illness had been previously entered, and the Incident was changed to an Injury. Data validation has been added to check for time in the Date of Incident field if a date has been entered and the Incident is changed from an Illness to an Injury.

### Create Accident/Illness Report (now Create Incident Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The error message on the “Treated in non-VA Emergency Room” field in the Quick OSHA Log Assessment panel (QOLA) has been changed to better reflect the missing field. It now states: “Please enter if Individual treated in a non-VA Emergency Room”. Previously the indication for a non-VA condition was omitted.

### CA-1 (Enter/Edit Form)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the Physician tab of this option, the labels for the physician fields were shifted to the right and cut off when the fields were required. When the fields were not required, the labels displayed properly. Fixed the labels so that they properly display the entire label whether required or not.

### Print CA1/CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The date in block 22, Date of Injury, on page 2 of the CA-1 printed over the line to the right into block 23, Date of Notice. Moved the display of the Date of Injury slightly to the left so that it prints entirely in the block.

### Log of Needlestick Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the report criteria resulted in no data being found, the printed message on the report read: THERE IS NO DATA TO REPORT FOR. The message has been changed to: THERE IS NO DATA TO REPORT FOR THIS TIME FRAME.

## Bug fixes with Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HD0000000130515

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Modifications have been completed so that page numbers print correctly on the OSHA 300 Log with more than 9 pages. Previously, the page numbers over 9 did not print at the bottom of the report.

### HD0000000152026

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to the modification made to ASISTS, a separated employee or terminated non-paid employee could have a new Incident report created for them. These individuals would show up in the listing of valid employees. Modifications were completed so that separated employees and terminated non-paid employees could not be selected.

### HD0000000183787

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the Regular From or To hours was midnight, the PM box on the CA-1 was checked rather than the AM checkbox. The problem was corrected so the appropriate checkbox was checked for all times.

### HD0000000206374

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to the correction, in the Create Incident Report or the Complete/Validate/Sign Incident Report, a user was able to select a terminated Supervisor or Secondary Supervisor. Modifications were made so that individuals terminated from the NEW PERSON File (#200) would not be included for selection.