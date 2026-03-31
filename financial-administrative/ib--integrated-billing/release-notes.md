---
title: Integrated Billing Version 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 1
description: This release of Integrated Billing (IB) will substantially impact the way your medical center conducts business. Functionallity is included which will help you implement encounter forms in all clinics. You will be able to collect and store much more detailed information about insurance carriers and
audience: 
keywords: 
  - insurance
  - edit
  - billing
  - patient
  - claims
  - form
  - tracking
  - action
  - print
  - company
page_count: 0
word_count: 21581
section_count: 24
table_count: 9
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

Decentralized Hospital Computer Program

integrated billingrelease notes

February 1994

Information Systems Center

Albany, New York

o:\devpackg\ib_20\relnotes\ivv2_0rn.doc (printed 02/04/94)

Table of Contents

Introduction

Executive Summary

Section 1. Claims Tracking

I. Functional Description

II\. Changed Options

Veterans with Insurance and Outpatient Visits

Veterans with Insurance and Admissions

Veterans with Insurance and Discharges

III\. New Options

Pending Review

Claims Tracking Edit

Single Patient Admission Sheet

Insurance Review Edit

Appeal/Denial Edit

Inquire to Claims Tracking

Supervisors Menu

Manually Add OPT Encounters to Claims Tracking

Manually Add Rx Refills to Claims Tracking

Claims Tracking Parameter Edit

Reports Menu (Claims Tracking)

UR Activity Report

Days Denied Report

MCCR/UR Summary Report

Review Worksheet Print

Scheduled Admissions w/Insurance

Pending Work Report

Unscheduled Admission w/Insurance

Print CT Summary for Billing

Assign Reason Not Billable

IV\. New or Changed Bulletins

V. Implementation Guide

VI\. General Comments

Section 2. Encounter Form Utilities

I. Functional Description

II\. Changed Options

III\. New Options

Clinic Setup/Edit Forms

Edit Clinic Setup Screen

Section 2. Encounter Form Utilities, cont.

Edit Form Screen

Select Tool Kit Block Screen

Edit Block Screen

Edit Selection Group Screen

Edit Selections Screen

Copy CPT Check-off Sheet to Encounter Form

Define Available Report (not Health Summaries)

Define Available Health Summary

Delete Unused Stuff

Edit Clinic Reports

Edit Division Reports

Edit Encounter Forms

Edit Marking Area (for selection lists)

Edit Package Interface

Edit Tool Kit

Edit Tool Kit Blocks

Edit Tool Kit Blocks Screen

Edit Tool Kit Forms

Tool Kit Forms Screen

Encounter Form IRM Options

Encounter Forms

For Each Form List Clinic Use

Import/Export Utility

Import/Export Workspace Screen

Print Blank Encounter Form

Print Encounter Forms for Appointments

Print Form w/Patient Data, No Appt

Print Manager

Print Options

Report Clinic Setups

IV\. New or Changed Bulletins

V. Implementation Guide

VI\. General Comments

Getting Started

Printer Considerations

Lines Per Inch, Characters Per Line

Boxes

Underlining

Emboldening

Example Terminal Setup for a HP LaserJet IVSi Printer

Section 3. Insurance Data Capture

Overview

I. Functional Description

Insurance Company Changes

Patient Insurance Policy Changes

Group Plans

Annual Benefits

Benefits Used

II\. Changed Options

Insurance Company Edit

III\. New Options

Patient Insurance Menu

Patient Insurance Info View/Edit

List New not Verified Policies

View Patient Insurance

View Insurance Company

Programmer APIs

IV\. New or Changed Bulletins

V. Implementation Guide

VI\. General Comments

Section 4. Patient Billing

I. Functional Description

II\. Changed Options

Cancel/Edit/Add Patient Charges

Outpatient Registration Events Report

Billing Rates List

Insurance Payment Trend Report

Enter/Edit Billing Rates

Fast Enter of New Billing Rates

Find Billing Data to Archive

III\. New Options

List Deferred Billing Cases

List Charges Awaiting New Copay Rate

Release Charges Awaiting New Copay Rate

List Special Inpatient Billing Cases

Disposition Special Inpatient Billing Cases

Flag Stop Codes/Dispositions/Clinics

List Flagged Stop Codes/Dispositions/Clinics

Rank Insurance Carriers By Amount Billed

IV\. New or Changed Bulletins

V. Implementation Guide

VI\. General Comments

Section 5. Third Party Billing

I. Functional Description

General Third Party Billing Changes

HCFA 1500 Claim From

Automated Biller

II\. Changed Options

UB-82 Menu

Enter/Edit Billing Information

III\. New Options

Enter/Edit Automated Billing Parameters

Print Auto Biller Results

Delete Auto Biller Results

UB-92 Test Pattern Print

Employer Report

IV\. New or Changed Bulletins

V. Implementation Guide

VI\. General Comments

Introduction

This release of Integrated Billing (IB) version 2.0 will introduce fundamental changes to the way MCCR-related tasks are done. This software introduces three new modules:

Claims Tracking

Encounter Form Utilities

Insurance Data Capture

There are also significant enhancements to the two previous modules: Patient Billing and Third Party Billing. IB has moved from a package with the sole purpose of identifying billable episodes of care and creating bills to a package which is responsible for the whole billing process through the passing of charges to Accounts Receivable (AR). IB v2.0 has added functionality to assist in

Capturing patient data

Tracking potentially billable episodes of care

Completing utilization review (UR) tasks

Capturing more complete insurance information

IB v2.0 has been targeted for a much wider audience than previous versions.

The Encounter Form Utilities module will be used by MAS ADPACs or clinic supervisors to create and print clinic-specific forms. Physicians will be using the forms and consequently be providing input into their creation.

The Claims Tracking module will be used by UR nurses within MCCR and Quality Management (QM) to track episodes of care, do pre-certifications, do continued stay reviews, and complete other UR tasks.

Insurance verifiers will use the Insurance Data Capture module to collect and store patient and insurance carrier-specific data.

The billing clerks will see substantial changes to their jobs with the enhancements provided in the Patient Billing and Third Party Billing modules.

IB version 2.0 is highly integrated with other DHCP packages.

PIMS is a feeder of patient demographic and eligibility data to IB. PIMS also provides information to Claims Tracking, Third Party Billing and Patient Billing on each billable episode of care, both inpatient and outpatient.

IB passes bills and/or charges to Accounts Receivable for the purpose of follow-up and collection.

Prescription information is passed from Outpatient Pharmacy to Patient Billing for the purpose of billing Pharmacy Copayments.

Prescription Refills are passed through Claims Tracking to Third Party Billing to be billed using the Automated Biller.

The Encounter Form Utilities print data on the forms from the Allergy, PIMS and Problem List packages. The Print Manager, included with the Encounter Form Utilities, will also print out Health Summaries as well as documents from the Outpatient Pharmacy and PIMS packages.

Means Test billing data may be transmitted between facilities using the PDX package.

The new functionality seen in this software is the direct result of input and feedback received from field users. Task groups made up of representatives from the field were created under the auspices of the MCCR Systems Committee and MCCR EP. These groups had meetings and/or conference calls with the developers and VACO Program Office (MCCR, MAS, and MIRMO) officials on a regular basis to develop the initial specifications and answer questions that arose during the development cycle. The field representatives on these groups included physicians, UR nurses, MAS ADPACs, MCCR coordinators, and billing clerks. An additional group of users was assembled prior to alpha testing to conduct full usability and functional testing of the software. The input from each of the individuals on these groups was invaluable to the software developers. A full list of each task group and its members is provided in Appendix A to this document.

The software developers would like to express sincere thanks to the seven alpha and beta test sites for installing and implementing this package. Special mention goes to VAMCs San Diego, CA and Buffalo, NY for their hospitality to the developers during site visits for software installation. Thanks also go to the remaining test sites: Augusta, GA; Hampton, VA; Leavenworth, KS; Pittsburgh (HD), PA; and Sioux Falls, SD. The willingness of these sites to test the software helps ensure that the released package meets the field users' needs.

These release notes are presented in a different format from previous versions of Integrated Billing. The release notes have been divided into sections for each module. This will allow each section to be targeted specifically toward the users who will be using the module described. Each module will be presented in the following format:

I. Functional description

II\. Changed options

III\. New options

IV\. New or changed bulletins

V. Implementation guidelines (when applicable)

VI\. General Comments

An Executive Summary, providing a short overview of the software, will also be provided for management to peruse. These release notes will concentrate on user functionality and not provide technical documentation. Descriptions of the files, fields, templates, routines and security keys will be provided in the Technical Manual.

Please ensure that copies of these release notes are distributed to the appropriate users.

# EXECUTIVE SUMMARY


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [EXECUTIVE SUMMARY](#executive-summary)
  - [Overview](#overview)
    - [Claims Tracking](#claims-tracking)
    - [Encounter Form Utilities](#encounter-form-utilities)
  - [### Insurance Data Capture](#insurance-data-capture)
  - [### Patient Billing](#patient-billing)
  - [### Third Party Billing](#third-party-billing)
- [Section 1. CLAIMS TRACKING](#section-1-claims-tracking)
  - [I. Functional Description](#i-functional-description)
  - [I. Functional Description](#i-functional-description-1)
  - [I. Functional Description](#i-functional-description-2)
  - [II. Changed Options](#ii-changed-options)
  - [II. Changed Options](#ii-changed-options-1)
  - [III. New Options](#iii-new-options)
  - [III. New Options](#iii-new-options-1)
    - [Actions](#actions)
  - [<u> </u>III. New Options](#u-uiii-new-options)
    - [Actions](#actions-1)
  - [III. New Options](#iii-new-options-2)
  - [<u> </u>III. New Options](#u-uiii-new-options-1)
  - [<u> </u>III. New Options](#u-uiii-new-options-2)
  - [<u> </u>III. New Options](#u-uiii-new-options-3)
  - [<u> </u>III. New Options](#u-uiii-new-options-4)
  - [<u> </u>III. New Options](#u-uiii-new-options-5)
  - [III. New Options](#iii-new-options-3)
  - [III. New Options](#iii-new-options-4)
  - [III. New Options](#iii-new-options-5)
  - [IV. New or Changed Bulletins](#iv-new-or-changed-bulletins)
  - [V. Implementation Guide](#v-implementation-guide)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release of Integrated Billing (IB) will substantially impact the way your medical center conducts business. Functionallity is included which will help you implement encounter forms in all clinics. You will be able to collect and store much more detailed information about insurance carriers and policies related to your patients. The Claims Tracking Module will allow you to track an episode of care from a scheduled admission to final disposition of a charge. An Automated Biller is introduced with this release which will automatically create inpatient and outpatient bills as well as bills for prescription refills. In addition to your MCCR unit, this package will impact your utilization review staff, clinicians and clinic clerks. IB v2.0 is highly integrated with other DHCP packages including PIMS, Accounts Receivable, Allergy, Problem List, Health Summary, Prosthetics and Outpatient Pharmacy.

### Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Claims Tracking module provides functionality for the Utilization Review Nurse to do both Hospital Reviews, using Interqual Standards, and Insurance Reviews. It allows for the tracking of an episode of care from the scheduling of the event to the final disposition of the bill. This module is new in IB v2.0, and was added in response to multiple requests from users for functionality to track pre-certification reviews, continuing stay reviews, appeals and denials. Highlights of this module include the following:

Events requiring insurance company reviews are tracked from the time of the actual event until payment is resolved.

Random inpatient stays are selected for hospital reviews using the Interqual standards. Severity of Illness and Intensity of Service are recorded for each day of care.

This module tracks inpatient stays, outpatient visits, prescription refills and prosthetics and acts as a feeder to the Automated Biller in the Third Party Billing module.

An admission sheet, similar to those used in the private sector, is introduced in this release. This document may be placed in the front of the inpatient chart and used to document concurrent reviews.

The ability to enter comments related to insurance company or other contacts is included throughout this module.

### Encounter Form Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB v2.0 provides medical centers with the ability to create encounter forms for the purpose of collecting clinical data in the outpatient clinics. Forms can be formatted so as to best fit the needs of each clinic and Medical Center. Medical Centers have the ability to decide what types of data may be printed on the form and what data needs to be collected on the form. There is enough flexibility in the software to allow medical centers to meet their clinical and billing needs with the same form. The encounter form may be used as part of the clinical record. The software is designed to print forms for each scheduled appointment prior to the appointment. Highlights of this module include the following:

A Form Generator is provided which will allow sites to design their own forms. This will allow sites to design forms similar to what they are already using.

Forms may be designed to print with data already displayed for the patient, such as patient demographics, insurance information, allergies, and active problems.

Through the use of blocks and selection lists, data such as procedures, diagnoses, problems, progress notes, and orders may be collected on the forms.

A Tool Kit of previously designed forms and blocks is included to assist in the creation of forms so each user will not need to create forms from scratch.

A Print Manager is included which allows all clinic-specific forms (routing sheets, health summaries, information profiles, and action profiles) to print with the encounter form for an appointment.

An Import/Export Utility is included which will make it easier for sites to exchange forms that they have already created.

## ### Insurance Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The whole concept behind gathering insurance data for billing purposes has changed with IB v2.0. The responsibility for insurance collection has moved from MAS to MCCR with this release. Users will have the ability to store more detailed insurance information about insurance companies, group plans, and benefits. This data will ultimately help billing and collections more accurately estimate reimbursements from insurance carriers. Highlights of this module include the following:

Multiple addresses, including main mailing, outpatient claims, inpatient claims, and appeals addresses may be stored for each insurance carrier.

Tools are available to maintain and/or clean up the Insurance Company file (#36).

Insurance company-specific billing parameters are available so bills will be able to reflect local insurance company requirements.

Group plans may be established which will be pointed to by each patient with a policy attached to that plan. This will save the re-input of the same policy data for each patient.

Annual benefits covered by a plan may be stored. This will be captured by year.

Benefits used by a patient, such as deductibles and lifetime maximums, may be stored.

## ### Patient Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Billing module in IB v2.0 went through the fewest substantial changes of the five modules included in this release. This module is responsible for generating all charges that are directly billed to the patient. It was the original module in Integrated Billing, initially designed to create Pharmacy Copayment charges. Since then, Means Test Copayments and Per Diems have been added as well as CHAMPVA subsistence charges. Highlights of new functionality in this module include the following:

This module is fully integrated with the Check Out functionality released in the PIMS v5.3 software package. Patients who claim exposure to Agent Orange and Environmental Contaminants and are treated for conditions not related to these conditions are now billed automatically.

Specific stop codes or dispositions may be flagged so that they cannot be billed.

Means Test billing data may now be transmitted between medical centers using the PDX v1.5 software package.

This software will now handle the problems caused when billing rates are not received prior to the beginning of the new fiscal year.

Subsistence charges for CHAMPVA patients will now be created automatically and passed to Accounts Receivable.

## ### Third Party Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Third Party Billing module includes changes in three main areas.

Functionality to generate a UB-92 (which is replacing the UB-82) is included.

Enhancements to the HCFA-1500 functionality were added.

An Automated Biller has been created which will be able to automatically generate bills for inpatient stays, outpatient visits and prescription refills.

Highlights of new functionality in this module include the following:

The HCFA-1500 has been enhanced to include inpatient as well as outpatient claims so that professional fees can now be billed on this document.

Through the use of a series of parameters, sites will be able to determine what type of events are automatically billed using the new Automated Biller.

A list of bills created by the Automated Biller will be provided. Billing clerks will then be able to edit and authorize these bills.

The ability to add Prescription Refills and Prosthetics Items to a bill.

# Section 1. CLAIMS TRACKING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## I. Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Claims Tracking is a new module within the Integrated Billing Package that will provide the following six major areas of enhancement:

> 1\. Provide the ability to track billing information about patient visits and services from the time of the event until payment

> 2\. Track those cases where the insurance company requires reviews

> 3\. Provide tracking of those cases requiring Utilization Review by the VACO QM office based on Interqual criteria

> 4\. Track not only inpatient and outpatient visits, but also prescription refills, Prosthetics, and Fee Basis visits

> 5\. Provide the feeding mechanism for automated bill preparation for third party bills

> 6\. Introduce an Admission Sheet which may be placed in the front of an

> inpatient chart and used to document concurrent reviews

Entries to the Claims Tracking module are made automatically. An admission automatically triggers entry of a Claims Tracking record. A pending insurance review (MCCR) and/or hospital review (QM) are also automatically added, if appropriate. Entries for outpatient visits and prescription refills are added as part of the nightly background job, as these entries are not needed in the same time frame as the admission information. It is important that pre-certifications be done in the time frame required by the insurance carrier.

One of the long-term goals of MCCR has been to provide the ability to track all visits and document why a claim for that visit or service was or was not processed. The Claims Tracking module can run in the following three modes:

Off

Tracking of only insurance cases

Tracking of all cases, based on site parameters

## I. Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a place to record reasons why visits were not billed. There is also a place to record the estimated collections. In a future release, we hope to be able to automate the estimated collection based on data in the new Insurance Data Capture module. Incorporating this information into existing reports will hopefully expedite manual billing, and will be used by the automated billing module.

The MCCR/UR portion of the Claims Tracking module provides for tracking of cases that require reviews for insurance companies. The center of this functionality is the Pending Review option that provides the necessary tickler file to make sure reviewers are reminded of pending work in a timely fashion. Review information about approvals, denials, penalties, and appeals can be entered and tracked. Appeals and denials can be tracked either by patient or by insurance company. A number of reports are available that can provide valuable information to the clinical staff regarding appropriateness of care. Sites may find that by reducing the number of days of unnecessary care, which are reflected in MCCR by days denied by an insurance company, they may be able to reduce costs.

The Quality Management portion of the Claims Tracking module has little to do with MCCR. It provides for data entry of Utilization Review criteria required by the Quality Management office. The REDACTED ISC is working with the REDACTED ISC to develop a national UR data base of this information. The initial roll-up of this data is tentatively scheduled for June, 1994.

This version of Integrated Billing introduces automated third party bill preparation. The various types of visits and when the bills are prepared are controlled by site parameters. Only entries in the Claims Tracking module will be billed automatic-ally. Currently, this includes tracking of scheduled admissions, inpatient stays, outpatient encounters, and prescription refills. Bills that are given a reason of Not Billable will no longer appear on the lists of visits or admissions to bill, nor will bills automatically be prepared for these visits. While the Automated Biller will be discussed in greater detail in another section, it is important to note that the episodes of care being billed are from the Claims Tracking module.

In non-VA hospitals, a form called an admission sheet or attestation sheet is commonly used at the front of inpatient charts. This version of IB introduces the admission sheet to the VA. It is intended to be a one-page document that provides basic demographic information, a workspace for concurrent review, and a place for early sign-off on the admission sheet as documentation to support billing prior to sign-off of the discharge summary. Many carriers request a copy of the admission sheet as additional documentation to be submitted with a claim. It is not intended to be a permanent part of the medical record but rather a temporary worksheet.

## I. Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four user menus for Claims Tracking, which are based on the type of user. There is a menu for individuals who need the full range of UR and billing portions of Claims Tracking. This is designed for use by MCCR supervisors and those personnel who do both Hospital (QM) and Insurance (MCCR) Reviews. There are two separate menus, one each for those sites that have separate personnel doing Hospital and MCCR Reviews. And finally, there is a Claims Tracking menu designed just for personnel in the Billing Unit to allow viewing of UR data as well as updating of billing information.

The primary data display and data entry for Claims Tracking is done through a series of nine List Manager screens. Each screen is associated with a number of actions that can be taken on the data displayed on the screen. The following are the main screens:

> 1\. Claims Tracking data by patient

> 2\. Hospital (QM) Review data by visit

> 3\. Insurance Review data by visit

> 4\. Appeals and associated denials by patient or by insurance company

> 5\. Pending Reviews (hospital and/or insurance depending on the menu)

The first four screens have an associated expanded display of items on the list. This series of screens form the primary display and data input for the Claims Tracking module.

## II. Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients with Insurance and Outpatient Visits

This option has been changed to reflect the new Claims Tracking module. This report now "knows" about the Claims Tracking Module. When running the report you may choose to include or exclude those potentially billable episodes of care that have a Reason Not Billable entered in Claims Tracking. A new column has been added to print the Reason Not Billable if you choose to print by this option. A new parameter has been added that allows sites to let this report add data to the Claims Tracking module. This is the only automated way to add outpatient care prior to Check Out to Claims Tracking. If you choose to add data with this report, no events prior to the Claims Tracking Start Date specified in the parameters will be added. If this report is queued, it will stop if there is a user-initiated request to stop the task.

## II. Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients with Insurance and Admission<u>s</u>

This option has been changed to reflect the new Claims Tracking module. This report now "knows" about the Claims Tracking Module. When running the report you may choose to include or exclude those potentially billable episodes of care that have a Reason Not Billable entered in Claims Tracking. A new column has been added to print the Reason Not Billable if you choose to print by this option. A new parameter has been added that allows sites to let this report add data to the Claims Tracking module. This is the only automated way to add prior inpatient care to Claims Tracking. If you choose to add data with this report, no events prior to the Claims Tracking Start Date specified in the parameters will be added. If this report is queued it will stop if there is a user-initiated request to stop the task.

Patients with Insurance and Discharges

This option has been changed to reflect the new Claims Tracking module. This report now "knows" about the Claims Tracking Module. When running this report you may choose to include or exclude those potentially billable episodes of care that have a Reason Not Billable entered in Claims Tracking. A new column has been added to print the Reason Not Billable if you choose to print by this option. A new parameter has been added that allows sites to let this report add data to the Claims Tracking module. This is the only automated way to add prior inpatient care to Claims Tracking. If you choose to add data with this report, no events prior to the Claims Tracking Start Date specified in the parameters will be added. If this report is queued, it will stop if there is a user-initiated request to stop the task.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four user menus exported with Claims Tracking. There are menus for

Users who perform only insurance reviews

Users who perform only hospital reviews

Users who perform all types of reviews

Billing personnel (on the Billing Clerks menu and the Billing Supervisors Menu)

The Claims Tracking Menu for billing clerks contains only four options, allows input of only billing information into Claims Tracking, and provides billing-specific reports. This section will describe the comprehensive user menu with all the options and actions. The options and actions that act differently or do not appear on all menus will be so noted.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pending Review \[IBT EDIT REVIEWS TO DO\]

This option will list all pending reviews that have a pending review date during the last seven days. The option is designed to be run the first thing every morning. You should print a Pending Review List sorted by either ward, patient, assignment or date, and go to the ward and perform your reviews. You can then come back to this option to perform all the necessary actions on the reviews or you may use the separate options. This option is available to individuals who do Insurance Reviews, Hospital Reviews or both. If the user performs both types of reviews, then a plus sign (+) will appear by the names of patients needing both type of reviews. Reviews are automatically made pending for the day they are added. See the discussions under the Insurance Reviews option and the Hospital Reviews option for a discussion on when reviews are automatically created.

### Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Change Date</u> - This action allows you to change the beginning and ending date of the search for pending reviews. You can search farther into the past or into the future to find reviews that are pending.

> <u>Claims Tracking Edit</u> - This action allows you to jump to the expanded Claims Tracking screen and perform all necessary edits to the entry in that file that is necessary. This may include the input of billing information, if it is known.

> <u>Diagnosis Update</u> - This action allows input of ICD-9 diagnoses for the patient. Whether diagnoses are input on this screen or another screen they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis and the onset of the diagnosis for this admission. For outpatient visits this information is stored with the outpatient encounter information.

> <u>Insurance Reviews</u> - This action allows you to jump to the insurance reviews screen. For details see the Insurance Reviews option. Note that if you try to perform an insurance review on a pending Hospital Review, the software will automatically take you to the Hospital Review screen. This is not available on the Claims Tracking for Hospital Reviewers option.

> <u>Print Worksheet</u> - This action allows you to print a generic worksheet for selected entries. The latest administrative data is printed on the worksheet, including patient name, ward, physicians, room-bed, etc.

> <u>Procedure Update</u> - This action allows the input of ICD-9 procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pending Review \[IBT EDIT REVIEWS TO DO\]

### Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Provider Update</u> - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document actual physicians if the administrative record indicates teams or vice versa.

> <u>Quick Edit</u> - This action allows you to quickly edit all information about the review without leaving the Pending Review option.

> <u>Remove From List</u> - This action allows you to quickly remove the review from the Pending Review List by automatically deleting the Next Review Date. For Insurance Reviews, the field TRACK AS INSURANCE CLAIM is also asked. If this is set to NO, no further reviews will automatically be created for this visit.

> <u>Show SC Conditions</u> - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.

> <u>Change Status</u> - This action allows you to quickly change the status of a review. Only completed reviews are used in the report preparation. Only completed reviews are used by the MCCR NDB roll-up or the QM roll-up (which is tentatively scheduled for release in June, 1994).

> <u>Hospital Reviews</u> - This action allows you to jump to the Hospital Reviews screen. For details see the Hospital Reviews option. Note that if you try to perform a Hospital Review on a pending Insurance Review, the software will automatically take you to the Insurance Review screen. This is not available on the Claims Tracking for Insurance Reviewers option.

> <u>View/Edit Entry</u> - This action allows you to jump to either the expanded Insurance Review screen or the expanded Hospital Review screen, depending on the type of review.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Claims Tracking Edit \[IBT EDIT TRACKING ENTRY\]

This option is the main gateway to all Claims Tracking functions (except pending reviews). Each visit, whether inpatient, outpatient, or prescription refill, has a unique entry where it is tracked to see if it is billable or not. Normally, only visits of insured patients are tracked; however, all visits may be tracked. You can edit information about anticipated revenues and required reviews with this option, and perform a number of maintenance and clinical update edits. Depending upon how you set your site parameters, admissions, outpatient visits, and prescription refills may automatically be added. If you are using the schedule options, then scheduled admissions will also be added. Upon installation, all current inpatients will automatically be loaded into Claims Tracking.

> Actions

> <u>Add Tracking Entry</u> - This action can be used to add an entry to be tracked if it was not automatically added. This will most commonly be used to add old visits or to add scheduled admissions if you are not using the scheduled admission package.

> <u>Assign Case</u> - This action allows you to assign a visit to a reviewer. This is useful in sorting pending reviews by the reviewer to whom they are assigned. Insurance and hospital reviews can be assigned separately.

> <u>Billing Info Edit</u> - This action allows you to edit the billing information about expected revenues and next auto bill date. This is useful for comparing expected revenues versus what was received.

> <u>Change Date</u> - This action allows you to change the default date range for the list of visits. Normally only the past year's visits are displayed, including any current admission. If you wish to view or take action on a visit outside of the current year, use this action to select the correct date range. Note that for inpatient care, the admission date is used.

> <u>Change Patient</u> - This action allows you to change the selected patient without having to leave the option and choose it again.

> <u>Delete Tracking Entry</u> - This action allows you to delete a tracking entry. If for some reason an entry was mistakenly added, use this action to delete the entry. Normally, if there is associated data with a review, it is preferable to inactivate the entry rather than delete it.

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Claims Tracking Edit \[IBT EDIT TRACKING ENTRY\]

> Actions

> <u>Appeals Edit</u> - This action allows you to jump to the Appeals and Denials screen. For details see the Appeals and Denials option. This is not available on the Claims Tracking for Hospital Reviews option. Only denials and penalties may be appealed.

> <u>Insurance Reviews</u> - This action allows you to jump to the insurance reviews screen. For details see the Insurance Reviews option. This is not available on the Claims Tracking for Hospital Reviewers option.

> <u>Hospital Reviews</u> - This action allows you to jump to the hospital reviews screen. For details see the Hospital Reviews option. This is not available on the Claims Tracking for Insurance Reviewers option.

> <u>Diagnosis Update</u> - This action allows input of ICD-9 diagnoses for the patient. Whether diagnoses are input on this screen or another screen, they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis, and the onset of the diagnosis for this admission. For outpatient visits, this information is stored with the outpatient encounter information.

> <u>Procedure Update</u> - This action allows the input of ICD-9 procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.

> <u>Provider Update</u> - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document actual physicians if the administrative record indicates teams or vice versa.

> <u>Quick Edit</u> - This action allows you to edit nearly all of the fields in Claims Tracking, specify if there should be insurance or hospital reviews, add billing information, and assign the visit to a reviewer.

> <u>Show SC Conditions</u> - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>View/Edit Episode</u> - This action allows you to jump to the expanded Claims Tracking screen where they can view much of the data on one visit and perform related actions.

Single Patient Admission Sheet \[IBT OUTPUT ONE ADMISSION SHEET\]

This option allows you to print an admission sheet for one visit. The function of the admission sheet is to serve as a temporary cover sheet in the inpatient chart where reviewers and coders can make notes about the visit in summary form. If the facility chooses to have physicians sign the admission sheet it can then be used as documentation to prepare inpatient bills prior to the signing of the discharge summary.

Insurance Review Edit \[IBT EDIT COMMUNICATIONS\]

This option is designed to allow the person doing reviews for insurance purposes to document the following events:

Contact with the insurance company

Action taken by the insurance company

Relevant clinical information

The need for further reviews

An initial review is automatically created upon admission for all insured patients. If UR is not required for the patient, the review can be deleted, inactivated, or left in an Entered status. If reviews are performed, and contact with the insurance company is made, the information can be input into this module. Once a review or entry is complete, its status should be updated to COMPLETE so it will be used in reporting. If further reviews are required, the NEXT REVIEW DATE should contain the date the next review is required and it will then appear in the Pending Reviews option or the Pending Reviews List.

> Actions

> <u>Add Comment</u> - This action allows you to edit the word processing field in the Insurance Review to add or edit this information without having to edit other fields.

> <u>Add Ins. Review</u> - This action will add a new review for the visit. The following are the default review types:

> Pre-certification Review (if it is a scheduled admission and no previous review)

> Urgent Admission review (if it is not a scheduled admission and no previous review)

> Continued Stay Review (for follow-up reviews)

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Insurance Review Edit \[IBT EDIT COMMUNICATIONS\]

> Actions

> <u>Appeals Edit</u> - This action allows you to jump to the Appeals and Denials screen to add/edit appeals. Only reviews where the action is either a denial or a penalty can be appealed. The denials and penalties can be edited on either the appeals screen or the insurance reviews screen. Appeals can only be edited on the appeals screen.

> <u>Delete Insurance Review</u> - This action allows an insurance review to be deleted. If a review is automatically created, but the visit does not require reviews and follow-up with the insurance company, it can be deleted. Use care in exercising this action. It may be just as important to document that no review is required as it is to document the required reviews.

> <u>Diagnosis Update</u> - This action allows input of ICD-9 diagnoses for the patient. Whether diagnoses are input on this screen or another screen they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis and the onset of the diagnosis for this admission. For outpatient visits this information is stored with the outpatient encounter information.

> <u>Procedure Update</u> - This action allows the input of ICD-9 procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional.

> <u>Provider Update</u> - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document actual physicians if the administrative record indicates teams or vice versa.

> <u>Quick Edit</u> - This action allows you to edit nearly all the fields in the insurance review. The type of review can be specified, along with the action of the insurance company, comments, the status of the review, and a follow-up date for the next review.

> <u>Review Worksheet Print</u> - This action will print a worksheet for use in taking to the ward for writing notes prior to calling the insurance company and entering the review. Basic information is printed about the patient and the visit on the form. Note that the format is slightly different for 80 column and 132 column output.

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Insurance Review Edit \[IBT EDIT COMMUNICATIONS\]

> Actions

> <u>Show SC Conditions</u> - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.

> <u>Status Change</u> - This action allows you to edit the status of a review. The choices are Inactive, Entered, Pending, and Complete. An inactive review disappears as though deleted. A review is given a status of Entered when it is created and updated to pending once data entry is started on the review. It should be changed to Complete once the review is complete. Note that this would support data entry by non-clinical users, and the status could be updated to Complete once the reviewer is satisfied with the entry.

> <u>View/Edit Episode</u> - This action allows you to jump to the expanded Insurance Review screen where they can view much of the data on one review and perform related actions. The actions are similar to the actions on the Insurance Review List screen, however, there are some abbreviated input actions that allow editing of only a few fields.

Appeal/Denial Edit \[IBT EDIT APPEALS/DENIALS\]

This option is slightly different from most Claims Tracking options. You can select either a patient or an insurance company for whom you wish to list the appeals and denials. This option lists the denials, initial appeal, and subsequent appeals; then, penalties, initial appeal, and subsequent appeals. This can be used to track the appeals for either a patient or an insurance company. It is very similar to the Insurance Review option; however, if an appeal is approved or partially approved, the amount won on appeal is tracked.

> Actions

> <u>Add Appeal</u> - This action allows adding an appeal to a denial or penalty. The first appeal will be an initial appeal. All other appeals will be subsequent appeals. You may enter an administrative or clinical appeal. There is no limit to the number of appeals that may be entered.

> <u>Delete Appeal/Denial</u> - This action allows deletion of appeals and denials. This was designed to be used in cases of erroneous entry.

## <u> </u>III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appeal/Denial Edit \[IBT EDIT APPEALS/DENIALS\]

> Actions

> <u>Diagnosis Update</u> - This action allows input of ICD-9 diagnoses for the patient. Whether diagnoses are input on this screen or another screen, they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis, and the onset of the diagnosis for this admission. For outpatient visits, this information is stored with the outpatient encounter information.

> <u>Procedure Update</u> - This action allows the input of ICD-9 procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.

> <u>Provider Update</u> - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document actual physicians if the administrative record indicates teams or vice versa.

> <u>Insurance Company Edit</u> - This action allows editing of fields in the Insurance Company file (#36) that pertain to appeals address and phone numbers.

> <u>Patient Insurance Edit</u> - This action allows editing of patient policy information. See the section on Insurance Data Capture for details.

> <u>Quick Edit</u> - This action allows you to edit nearly all of the fields in the appeal or denial, add comments, maintain its status, and assign follow-up dates.

> <u>Show SC Conditions</u> - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.

> <u>View/Edit Episode</u> - This action allows you to jump to the expanded Appeal/Denial screen where you can view much of the data for one visit and perform related actions.

Inquire to Claims Tracking \[IBT OUTPUT CLAIM INQUIRY\]

This option will display or print stored information about a single visit. You can select a patient, list the Claims Tracking entries, and view the information. A brief display of the reviews performed is also provided. This display is less detailed than the Claims Tracking Summary for Billing option.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supervisors Menu \[IBT SUPERVISORS MENU\]

This option contains the options to edit the Claims Tracking site parameters and to manually add outpatient encounters and Rx Refills to Claims Tracking.

Manually Add OPT. Encounters to Claims Tracking \[IBT SUP MANUALLY QUE ENCOUNTERS\]

Outpatient Encounters that have been checked out are normally added during the IB nightly background job. Only primary outpatient encounters that have been checked out will be added in the first twenty days after the date of the encounter. The purpose of this option is to allow sites to search for outpatient encounters that were not checked out within twenty days and have them automatically added to Claims Tracking. If sites choose to run the automated bill preparation portion of IB v2.0, they will want to periodically run this report to insure that all outpatient care

is billed. This option is automatically queued and a bulletin is sent upon completion.

Manually Add Rx Refills to Claims Tracking \[IBT SUP MANUALLY QUE RX FILLS\]

Rx refills are normally added during the IB nightly background job. Refills that have been released within ten days of the fill date are automatically added at night. The purpose of this option is to allow sites to search for refills that were not released within ten days and have them automatically added to Claims Tracking. If sites choose to run the automated bill preparation portion of IB v2.0, they will want to periodically run this report to insure that all outpatient care is billed. This option is automatically queued and a bulletin is sent upon completion.

Claims Tracking Parameter Edit \[IBT EDIT TRACKING PARAMETERS\]

This option allows editing of the Claims Tracking Parameters. There are a number of parameters designed to limit the automatic addition of information to Claims Tracking for sites that do not have sufficient computer resources to run this module. A site can set the earliest date for adding entries, or turn on or off Inpatient, Outpatient, and Rx Refill tracking separately. There are a number of parameters that also control the random sampling of admissions for Hospital Reviews.

Reports Menu (Claims Tracking) \[IBT OUTPUT MENU\]

This menu contains all the report options available in Claims Tracking.

UR Activity Report \[IBT OUTPUT UR ACTIVITY REPORT\]

This report is similar to the MCCR/UR summary report, however, it counts total activity during the period. It also provides a detailed listing of the Insurance Reviews done during the period, along with a summary report. The detailed listing can be sorted by patient, review date, or specialty.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Days Denied Report \[IBT OUTPUT DENIED DAYS REPORT\]

This report can print a summary or detailed listing of denials by insurance companies. The report can be sorted by patient, attending, or service. The summary report shows the number of denials, the total days denied, the dollar amount of the denials, and the days won on appeal by service.

MCCR/UR Summary Report \[IBT OUTPUT SUMMARY REPORT\]

This report prints a summary of hospital activity by either admission or discharge and the number of reviews for the period. If sorting by discharge, only reviews for discharges for the period are counted. Included is a Penalty Report, a Days Approved Report, and a Days Denied Report, all by specialty.

Review Worksheet Print \[IBT OUTPUT REVIEW WORKSHEET\]

This option is similar to the Review Worksheet action on the Insurance Review screen. A worksheet for a current inpatient can be printed containing demographic data and information about current room/bed, ward, and provider.

Scheduled Admissions w/Insurance \[IBT OUTPUT SCHED ADM W/INS\]

This option prints a list of scheduled admissions in Claims Tracking for insured patients. This will produce a list of patients with past scheduled admissions and scheduled admissions up to three days into the future. This is not the same as the Scheduled Admission List from MAS, as it does not contain all scheduled admissions from MAS. Scheduled admissions are normally moved to Claims Tracking four days prior to the scheduled admission date so that reviews can be completed prior to admission. Included are the number and type of reviews performed and the insurance company actions.

Pending Work Report \[IBT OUTPUT PENDING ITEMS\]

This option will print a Pending Work List, similar to the Pending Reviews option. It can be sorted by due date, patient, ward, or assigned to, for either Insurance Review, Hospital Reviews, or both. This option will limit the number of reviews on the list to those reviews which meet the sort criteria rather than just sort the reviews. The output is formatted differently from the format if printing the reviews from the Pending Reviews option.

Unscheduled Admission w/Insurance \[IBT OUTPUT UNSCHE ADM W/INS\]

This option prints a list of unscheduled admissions in Claims Tracking for insured patients. In addition it prints information about the number of reviews completed and the insurance company actions.

## III. New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Print CT Summary for Billing \[IBT OUTPUT BILLING SHEET\]

This option prints nearly all information about a visit that can be determined. Summary information from MAS or Pharmacy is printed about the visit, such as

Summary information from Claims Tracking

Information from all Hospital and Insurance Reviews (including comments)

Diagnoses, procedures, and provider information from Claims Tracking

This report is designed to provide as much detailed information about a visit as possible for use by billers when entering a claim, or when answering questions about a claim.

Assign Reason Not Billable \[IBT EDIT REASON NOT BILLABLE\]

This option provides functionality to flag a visit, inpatient, outpatient, or Rx refill as billable or non-billable. This is done by assigning a Reason Not Billable. If there is no Reason Not Billable assigned, the billing information can be entered into Claims Tracking for the visit. This option appears on the Claims Tracking for Billers menu and is a simplified edit of Claims Tracking information that is of interest to billing personnel.

## IV. New or Changed Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no bulletins in claims tracking.

## V. Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because Claims Tracking is a new module you will want to consider how you plan to implement this package. You will probably want to have a meeting with the IRM staff, MCCR Coordinator, the MAS ADPAC and Quality Management/UR supervisor. Discuss how each section plans to use this module. In particular, is MCCR planning on running automated billing, and if yes, for what types of bills. Does IRM have the disk space and capacity to support this. In this meeting you will want to review the Claims Tracking site parameters and discuss how they affect the package. (The recommended settings are shown in the user manual.) The claims tracking module has the ability to use a great deal of disk space and capacity if turned on to track all episodes. Generally you will not want to do this except for short periods of time.

Claims Tracking contains the data entry portion of the QM national roll-up of data and will determine the random sample cases for review. Most sites will be compelled to run this part of the inpatient tracking. If you plan to use the automated biller to do bill preparation for outpatient and prescription refill billing you will also want to turn on tracking of these portions of the claims tracking module for insurance cases. There are ways to automatically back load insurance cases into claims tracking. If you don't currently have the capacity or want to delay implementation you can still take advantage of this module at a later date. We suggest you initially turn on the inpatient claims tracking for insurance and UR cases to see how the system works and then to implement outpatient and prescription claims tracking for insurance cases after a few weeks and only if you plan to use those parts of the package.

The major of the data entry in Claims Tracking is oriented to the UR personnel. Expect that training may be an issue at your site. Many of our initial users were not experienced DHCP users and required assistance in basic data entry techniques prior to using the package. Using the module in a training account helped but be prepared to provide a few minutes to a several hours of support from an experienced user or trainer when using the package for the first time. If an entry doesn't come out right the first few times, remember that they can be deleted and re-entered if need be. (use the Print CT Summary for Billing prior to deleting so you can review what was done)

1\. Back loading the required QM reviews.

The Quality Management office is apparently mandating that the UR cases from the beginning of the fiscal year (fy-94) be input into claims tracking so that this information is available for the national roll-up expected to be released in June, 1994.

To input these prior cases use the option Claims Tracking Edit. Use the option Add Tracking Entry and enter the following information as indicated. If other prompts appear, enter nothing or accept the default answer.

> Select Tracking Type: INPATIENT ADMISSION (don't select scheduled admission as that is for future scheduled admissions)

> Admission Date: JAN 20, 1994 (enter any date that the patient was an inpatient and the system will find the correct admission date) Note you can enter dates that the patient was not an inpatient and this will cause you to lose the link to MAS type information.

> Okay to Add Claims Tracking entry for Admission Date AUG 30,1993@07:44:18? NO// YES (notice that the computer found the correct admission date and time)

> ADMISSION TYPE: URGENT// (you can change this if you want, the default is urgent, type a Question mark for the choices.)

> TRACKED AS INSURANCE CLAIM?: NO// (accept the default answer here)

> REASON NOT BILLABLE: (if this appears and you don't know the answer, leave blank)

> SPECIAL CONSENT ROI: (if this appears and you don't know the answer, leave blank)

> TRACKED AS RANDOM SAMPLE?: YES (Enter Yes if this is a random case or No if not)

> TRACKED AS SPECIAL CONDITION: COPD (If this case involved TURP, COPD, or CVD, enter which one it was or leave it blank if nothing. Note that a case can be both random and a special condition)

> TRACKED AS A LOCAL ADDITION?: NO (Enter Yes if you are doing UR on this case as a locally determined case to follow or No if not. If not answered No is assumed. Note that how you answered the previous two questions has no affect on this field)

> HOSPITAL REVIEWS ASSIGNED TO: (Enter the name of the user assigned this case for quality management reviews if you track cases by who did the review or leave blank.)

> INS. REVIEWS ASSIGNED TO: (Enter the name of the user assigned this case for Insurance reviews if you track cases by who did the review or leave blank.)

Now use the action Hospital Reviews to go to the hospital Review Input screen. If you have your worksheets in front of you use the Add Next Review action to enter your reviews. An entry for every day of the review period is required. If the entry for succeeding days is exactly like the prior day say yes to the question is this exactly like the previous review until you are done. You can later edit any of these reviews. Remember to enter a next review date if you want this to later show up on your pending work report (or to do list). The status of each review must be Complete in order for the National roll-up to extract the data.

When done with entering reviews for this patient, return to the Claims Tracking Edit screen and use the action to Change Patient to select the next patient and repeat the sequence.

IV. ENCOUNTER FORM UTILITIES1. FUNCTIONAL DESCRIPTION

An encounter form is a paper form designed specifically for an outpatient appointment. It is used both to display relevant patient data for use during the appointment, such as demographics, allergies, and problems, and to collect data about the appointment, such as procedures and tests performed. Its focus is primarily clinical but it has other purposes, such as collecting data necessary for billing.

The Encounter Form Utilities are a set of options that allow encounter forms to be: designed, edited and assigned to clinics; printed for appointments with patient data; and printed with or without patient data for patients without an appointment.

The Encounter Form Utilities will enable collection of outpatient clinical and administrative data. They will provide a more organized method of data collection which will be less obtrusive to the clinician and supporting clerical staff.

Included with the utilities is a Print Manager that allows sites to define reports that should print along with the encounter forms. This should result in a considerable savings in time required to collate the various reports and forms printed for each appointment. Reports can be defined to print for entire divisions or for individual clinics. Also, at the division level conditions can be specified under which the reports should print, such as "for all appointments" or "only for the earliest appointment". Currently, the Routing Slip, Information Profile, Action Profile, and any Health Summary can be printed via the Print Manager. Others will be added, depending on demand by local sites. There is an option that local sites can use to add their own reports for use by the Print Manager.

Many sites already use encounter forms of their own design. For this reason, a "form generator" was created, rather than a set of pre-formatted encounter forms, so that sites can design forms similar to the ones they may already use. The form generator displays the form to a portion of the screen with a coordinate system drawn across the top and left side so that the position of its contents can be determined. Objects can then be created and placed on the form. Many actions are included that are meant to ease the burden of creating forms. For example, users can copy a form that someone else designed and then edit it, or they can copy a block from another form and place it on their own form. Users can move a single block on the form or shift entire groups of blocks. There are a variety of object types that can be created and placed on the form. Learning the terminology that was invented to describe these objects is the biggest hurdle to overcome before a site can successfully use the utilities to design their own forms.

The encounter form interfaces with DHCP to display patient data. Currently data displayed on the encounter forms comes from just the PIMS, Allergies, and Problem List packages. Data that can be printed to the form includes patient demographic data and insurance data, patient allergies and problems. In the future, more interfaces will be added as they are requested by users. The utilities are designed to interface in a well-defined manner with other packages so that new interfaces can be easily added. There are options for use by local IRMs that enable them to easily add their own Package Interfaces.

So that sites don't have to spend a lot of time creating custom forms the utilities include a "tool kit" of forms and form components. In most cases the tool kit will meet the needs of the local sites, allowing them to avoid the time-consuming process of creating forms from scratch. There are options to allow IRM sites to edit the tool kit. There is also an Import/Export Utility that will enable sites to exchange forms and form components. It is important to note that after the tool kit is initially installed, additional forms, contained in Files 357-357.5 and 357.77-357.8, can only be installed through the import/export utility. Data for these files should not be transferred via DIFROM after the initial install.

2. NEW OPTIONSClinic Setup/Edit Forms \[IBDF CLINIC SETUP/EDIT FORMS\]

This option allows the user to assign encounter forms to clinics and to edit encounter forms. A description of the screens and actions accessible from this option follows.

![](integrated-billing-version-2-release-notes/001.png)

Edit Clinic Setup Screen

This screen displays a list of forms defined for the clinic. It provides the ability to assign forms to clinics and provides entry to the form generator for creating and editing form descriptions.

Actions

<u>Change Clinic</u> - This action allows the clinic to be changed and changes the list of forms displayed to the screen accordingly.

<u>Add Form to Setup</u> - This action allows a form to be assigned to a clinic. The forms included in the tool kit cannot be assigned to a clinic, since they are templates that must remain unchanged. However, tool kit forms can be copied and the copy assigned to a clinic. Forms can be shared between clinics.

<u>Delete from Setup</u> - This action allows a form to be dropped from use for the clinic.

<u>Delete Unused Form</u> - This action allows a form that is not in use by any clinic to be deleted completely.

<u>Copy Form</u> - This action allows any form, whether it is in the tool kit or in use by another clinic, to be copied. The form must be re-named.

<u>Create Blank Form</u> - This action allows a blank form to be created. The user must name the form, enter a description and the size of the form. It is used to create forms from scratch.

<u>Print Sample Form</u> - This action is used to print a form without patient data.

<u>Form Name/Descr/Size</u> - This action allows the form's name, description and size to be edited.

<u>Edit Form</u> - This action allows the user to view a form and edit its appearance and content. It takes the user to the "Edit Form" screen.

<u>Recompile Form</u> - The need to use this action will rarely, if ever, occur. The action allows forms to be recompiled. Forms are automatically compiled each time they are edited. The compiled form prints using a small fraction of the computer resources as compared to printing the uncompiled version. When an uncompiled form is printed it is automatically compiled. You can use this action if you have reason to believe that the compiled version of the form does not match the actual form as entered through the Edit Form action. It is here as a safety feature only; its actual need is not anticipated.

Edit Form Screen

This screen displays the form as identically as possible to how it will appear on paper. It allows the contents of the form to be edited.

Actions

<u>Move Block</u> - This action allows a block to be selected and moved anywhere on the form. The top left-hand corner is used as the reference point for moving the block.

<u>Shift Blocks</u> - This action allows the user to specify a range of blocks to shift either up or down or to either side.

<u>Block Size</u> - This action allows the size of the block to be changed, within the limits set by the size of the form. When sizing the block the user is asked for what line to move the bottom margin to, and to what column the right-hand margin should be moved.

<u>Form Header</u> - This action allows a sequence of header lines to be entered. A block is created and the header lines are automatically centered within the block in the sequence in which they are typed.

<u>Add Tool Kit Block</u> - This action allows a tool kit block to be selected and places it at the desired position on the form. This action takes the user to the "Select Tool Kit Block" screen. The block header, description, and size can be edited.

<u>New Block</u> - This action is used to create a new, empty block.

<u>Edit Block</u> - This action allows a block to be selected and its appearance and contents to be edited. This action takes the user to the "Edit Block" screen.

<u>Delete Block</u> - This action allows a block to be selected for deletion. Everything in the block is also deleted.

<u>Re Display Screen</u> - The user can use this action if he suspects the screen display of the form is not correct. It redraws the entire form.

<u>Copy Other Form's Block</u> - This can be used to copy a block from any form into the user's form.

Select Tool Kit Block Screen

This screen displays a list of the available tool kit blocks. It allows the user to select a tool kit block and view any of the tool kit blocks.

Actions

<u>Select Tool Kit Block</u> - This action allows the user to select one of the tool kit blocks from the displayed list.

<u>View Tool Kit Block</u> - This action allows the user to select one of the tool kit blocks and then displays the block.

Edit Block Screen

This screen displays the block as it will appear on paper as nearly as possible. It allows the user to edit the block's contents, appearance and description.

Actions

<u>Header/Descr/Outline</u> - This action allows the block header and description to be edited. Also, the outline around the block can be made to appear as a solid line or can be made invisible.

<u>Block Size</u> - This action is used to change the size of the block.

<u>Selection List</u> - Selection lists are lists of diagnoses, procedures, problems, etc. that can be included on an encounter form. The appearance of the selection list can be changed, a new selection list can be created, an existing selection list can be deleted, or the list's contents can be altered. Choosing to edit the list's contents takes the user to the screen labeled "Edit Selection Group" in the diagram.

<u>Data Field</u> - Certain patient or clinic specific information may automatically be printed on the encounter forms. This action allows adding, editing, and deleting of these fields and their associated labels from blocks. Some data fields may have more than one data element (called subfields), such as SC Conditions, which have a name and a percentage. If the data field is a multiple, the ITEM NUMBER will specify the order and number limit that can appear on the form.

<u>Straight Line</u> - This action allows lines, either horizontal or vertical, to be added to the block, deleted, or edited. Horizontal lines use underlining, which can be handy.

<u>Text Area</u> - This action allows text areas to be added, deleted, or edited. A text area is a rectangular area within the block which contains text. The text is automatically formatted to fit within the defined area.

<u>Shift Contents</u> - This action allows the user to shift the position of the contents of the block. The direction and degree of movement can be specified, as well as the type of object to be shifted, and a range within which to act.

Edit Selection Group Screen

This screen displays the selection groups defined for the selection list, with the header text and the print orders. A selection group is a named collection of items on the list with a header and a defined print order. A selection list is made up of one or more selection groups. The user is allowed to edit the contents of the list. To edit individual selections, a group must be selected.

Actions

<u>Add Group</u> - This action allows a new group to be added. The header text and print order must be entered. A group named BLANK is special in that its header alone will not display to the form, i.e., its selections will be grouped together but won't appear under a header.

<u>Delete Group</u> - A group can be selected for deletion from the form. All of the group's selections are also deleted.

<u>Group Header/Order</u> - This action allows the header text and print order to be edited.

<u>Group's Contents</u> - This action allows the contents of the group to be edited. Choosing this action takes the user to the screen labeled "Edit Selections" in the diagram.

Edit Selections Screen

This screen displays the selections appearing under the group. A selection is just one item on the list, usually selected from a table, such as the table of ICD-9 Diagnosis Codes. The user can edit selections on the list.

Actions

<u>Add Selection</u> - This action allows a new selection to be added to the group.

<u>Delete Selection</u> - This action allows a selection to be deleted.

<u>Edit Selection</u> - This action allows the text appearing on the form to be edited and the print order changed.

Copy CPT Check-off Sheet to Encounter Form \[IBDF COPY CPTS TO FORM\]

This option requests the user to select a CPT Check-off Sheet and Encounter Form. The Check-off Sheet's CPT codes are then copied to the Encounter Form.

Define Available Report (not Health Summaries) \[IBDF DEFINE AVAILABLE REPORT\]

This option is used to make reports, other than Health Summaries, available for use by the Print Manager. The user is asked to enter the entry point in the program that prints the report, and is allowed to specify entry and exit actions, required variables, etc. This option is meant for use by a programmer.

Define Available Health Summary \[IBDF DEFINE AVLABLE HLTH SMRY\]

This option allows a Health Summary to be made available for use by the Print Manager. The Health Summary must have already been created through the Health Summary package. This option can be used by the non-programmer.

Delete Unused Stuff \[IBDF DELETE UNUSED BLOCKS\]

This option can be used to delete form blocks and compiled forms that are no longer in use. The utilities do this automatically, so this option need be used only very rarely, if ever.

Edit Clinic Reports \[IBDF EDIT CLINIC REPORTS\]

This option is used to select encounter forms and reports that should print for the clinic. It can also be used to specify reports that should not print; this will override what is defined to print for the division.

Edit Division Reports \[IBDF EDIT DIVISION REPORTS\]

This option is used to select reports that should print for the entire division. Print conditions can be specified.

Edit Encounter Forms \[IBDF EDIT ENCOUNTER FORMS\]

This menu contains the options that can be used to edit encounter forms other than those in the tool kit.

Edit Marking Area (for selection lists) \[IBDF EDIT MARKING AREA\]

This option can be used by the local sites to create their own Marking Areas to supplement those that come with the tool kit. Marking Areas are the areas on a selection list that are used for writing in to indicate choices.

Edit Package Interface \[IBDF EDIT PACKAGE INTERFACE\]

This option allows package interfaces for selection routines and output routines to be created and edited. By creating their own Package Interfaces the local sites can display data to their forms that is not provided for in the tool kit. Care must be taken not to delete Package Interfaces that are in use.

Edit Tool Kit \[IBDF EDIT TOOL KIT\]

This menu contains the options that allow the user to edit forms and blocks contained in the tool kit.

Edit Tool Kit Blocks \[IBDF EDIT TOOL KIT BLOCKS\]

This option is used to edit, create, and delete tool kit blocks. Following is a description of the screens and actions accessible through this option.

> Edit Tool Kit Blocks Screen

> This screen displays a list of all the tool kit blocks. The user is allowed to edit, create and delete tool kit blocks.

> Actions

> <u>Edit Block</u> - This action can be used to select a block from the list and then edit it. It takes the user to the Edit Block screen, which is described under the Clinic Setup/Edit Forms option.

> <u>New Block</u> - This action is used to create a new, empty block.

> <u>Delete Block</u> -This action is used to delete a tool kit block.

> <u>Copy Block</u> - This action is used to copy a block from any form and make it a tool kit block.

> <u>Change TK Order</u> - This action allows user to change the order of the tool kit blocks on the list.

Edit Tool Kit Forms \[IBDF EDIT TOOL KIT FORMS\]

This option allows tool kit forms to be edited, created, deleted. The screens and actions that are accessible from this option follow.

> Tool Kit Forms Screen

> This screen displays a list of all the tool kit forms. Tool kit forms can be created, edited, and deleted.

> Actions

> <u>Form Name/Descr/Size</u> - This action allows the user to edit the name of the form, its description, and size.

> <u>Delete Form</u> - This is used to delete a form from the tool kit.

> <u>Copy Form</u> - This action is used to copy any form and make it part of the tool kit.

> <u>Create Blank Form</u> - This action is used to create a new form for the tool kit from scratch.

> <u>Edit Form</u> - This action is used to get to the Edit Form screen, which is described under the Clinic Setup/Edit Form option.

> <u>Print Sample Form</u> - This is used to print any encounter form without patient data.

Encounter Form IRM Options \[IBDF IRM OPTIONS\]

The basic intent of this menu is to contain the options that should only be available to MUMPS programmers.

Encounter Forms \[IBDF ENCOUNTER FORM\]

This menu contains all of the Encounter Form Utilities options.

For Each Form List Clinic Use \[IBDF LIST CLINICS USING FORMS\]

For each encounter form this report lists the clinics using it.

Import/Export Utility \[IBDF IMPORT/EXPORT UTILITY\]

This option allows forms and blocks to be transferred between sites. It utilizes a set of files in the 358 number range that serve as a workspace. To export, it invokes ^DIFROM and to import, it executes the Inits received from the other site. ^DIFROM is used only to affect the workspace. The user can move forms into and out of the workspace. Following are the screens and actions that are accessible from this option.

> Import/Export Workspace Screen

> This screen displays a list of the forms and tool kit blocks that are in the workspace. The workspace serves as a staging area where material can be either imported or exported.

> Actions

> <u>Help</u> - This action provides a description and step-by-step instructions of the import/export process.

> <u>List Forms/List Tool Kit Blocks</u> - These two actions are used to toggle back and forth between the display of the forms in the workspace and the tool kit blocks in the workspace.

> <u>Import Entry</u> - This is used to select a form or tool kit block from the workspace and make it into a real form or tool kit block that can be used.

> <u>Delete Entry</u> - This is used to delete a form or tool kit block from the workspace.

> <u>Add Entry</u> - This is used to select a form or block and bring it into the workspace. Blocks selected are always made into tool kit blocks.

> <u>View Imp/Exp Notes</u> - When exporting a form or block a description of the exported object should always be included. This action allows the description to be viewed.

> <u>Edit Imp/Exp Notes</u> - This action allows notes to be added and edited for each entry in the workspace. The notes are meant for the receiving site when exporting forms.

> <u>DIFROM</u> - This action executes ^DIFROM, using a package entry that was created for use by the Import/Export Utility. It creates Inits for all the entries in the workspace.

> <u>Run Inits</u> - This action executes the Inits, usually named ^IBDEINIT, received from another site and produced using the Import/Export Utility. Executing the Inits fills the workspace, but does not actually result in forms or blocks that can be used. The workspace only serves as a staging area where forms can be imported or exported from.

> <u>Clear Work Space</u> -This action clears the workspace.

Print Blank Encounter Form \[IBDF PRINT BLNK ENCOUNTER FORM\]

This option allows the user to select a clinic, and if an encounter form is defined to print without patient data for that clinic the form will be printed.

Print Encounter Forms for Appointments \[IBDF PRINT ENCOUNTER FORMS\]

This option is the principal means of printing encounter forms. The user is asked to specify appointments for a particular date, either by division, clinic, or patient. For each appointment, the encounter forms specified in the clinic setup are printed, complete with patient data. The reports specified for the clinic and division are also printed. Sorting is either by division/terminal digits or by division/clinic/patient. The option allows the user to specify that only add-ons should be printed. It also allows the user to specify that printing should begin somewhere in the middle of the job. That will come in useful, for example, if a job terminates part way through due to equipment failure.

Print Form w/Patient Data, No Appt \[IBDF PRNT FORM W/DATA NO APPT\]

Allows an encounter form to be printed with patient data, but does not ask that an appointment be selected. It uses the current time as the appointment time. The user is allowed either to choose the form to print or to invoke the Print Manager.

Print Manager \[IBDF PRINT MANAGER\]

This menu contains all of the options pertaining to the Print Manager. The Print Manager is used to specify what encounter forms and reports should print for which clinics and divisions.

Print Options \[IBDF PRINT OPTIONS\]

This menu contains all of the options for printing encounter forms.

Report Clinic Setups \[IBDF REPORT CLINIC SETUPS\]

This option reports on each clinic setup, listing the encounter forms and other reports defined for use by the clinic.

3. IMPLEMENTATION GUIDELINES

The purpose of these Implementation Guidelines is to provide a general format for the process of implementing the Encounter Form at your facility. Forethought and a study of the needs in your outpatient clinical areas are key ingredients to successful setup and use of this module's functionality. Included in this portion are descriptions of computer and non-computer-related steps one should consider. This guide is intended as a general overview of the implementation process and is not meant as a literal mandate in regard to steps taken.

GENERAL STEPS FOR IMPLEMENTATION

1\. *Begin by forming a committee.* It may be a good idea to include a member or two from each of the clinical services whose members attend clinics as well as the Chief of Ambulatory Care, MAS clinic supervisor or designee. Physician participation and input is important, as it will affect acceptability by clinicians. Educate members of the committee regarding the module's capabilities and the end results (examples of encounter forms). Ask each clinical member to educate fellow clinicians about the Encounter Form, including the input needed from clinicians re: the set-up, and the consequent benefits (improved communications between clinician and administration, tailored forms which will provide administrative and clinical data needed by clinician, increased efficiency for progress notes and DHCP entry of CPT codes and Diagnoses, functionality in conjunction with the Problem List clinical DHCP package, et cetera). Administrative members can educate peers or subordinates about their role in the use of Encounter Forms as well.

2\. *Create an Implementation Plan.* The plan need not be a formal paper or study. Outline each of the individual tasks which need to be completed in the necessary order. It may be a good idea to have a number of committee members involved in the completion of these steps. Gain consensus and approval of Clinical, Administrative and Executive Management. If steps are documented, however, they can be followed step by step and checked off.

3\. *Execute the Implementation Plan.* A sample of general tasks is provided below:

> A. Create one or two general encounter forms for examples and for clinician review. You may also copy and/or print the forms in the Tool Kit as a beginning. Another alternative is to get copies from other facilities who have already created forms. Forms can be imported and exported via the utility option in the Encounter Form IRM Options Menu.

> B. Organize appointments with clinicians for their input. Collect all needed data for the forms as explained below. It may be wise to interview all members according to their particular subspecialty, such as Dermatology or General Surgery. Standardize the questions you will ask. Questions can be: (1) What kind of administrative information do you need, such as a list of SC Disabilities, etc.? Here, an example of administrative data displayed by a Tool Kit form may be all they require. (2) What particular diagnoses do you treat in your clinic? It is suggested that a list of diagnoses or a small ICD-9 code book be available during this portion of the interview to aid in pinpointing specific diagnoses. (3) What particular treatment do you provide (in the form of CPT Codes). Again, a CPT code list or book may help. We strongly suggest running the option *Most Commonly used Outpatient CPT Codes* for the clinics in question. The output will provide a list of CPT codes entered for each clinic for a user-specified date range. This will be very useful in identifying those CPT codes which should be listed on the form for the clinic. If your site has utilized the CPT Check-Off Sheets included in Integrated Billing version 1.5, you may use the option *Copy CPT Check-off Sheet to Encounter Form,* which will allow the user to copy all CPT information on a Check-Off sheet and upload it to a CPT code graphics box previously placed into the form. CPT codes should be updated in all of the Check-Off Sheets first by using the *Delete/List Inactive Codes on Check-off Sheets* option (in the Ambulatory Surgery Maintenance Menu) before uploading to the Encounter Form. This step will save considerable time and effort.

> C. Create forms for Clinicians and give them copies to review. Make any necessary changes. You may also wish to create versions of the form with an area for imprinting the patient's data card with the embosser. *Tip*: Copy the Clinic's Basic form and modify the copy to include the space for the card imprint. The area for the ID Card imprint is included as a Tool Kit block. You may also get copies from other facilities who have already created forms. As mentioned before, forms can be imported and exported via the utility option in the Encounter Form IRM Options Menu.

> D. Identify Health Summary reports used by your clinicians. You will be able to identify them for the Print Manager functionality by using the *Define Available Health Summary* option and then include them in the printout setup by using either of the *Edit Division Reports* (re: a default Health Summary for the division) or the *Edit Clinic Reports* option (to set Health Summaries for specific clinics.)

4\. *Implementing Form Usage.* It may be a good idea to introduce the Encounter Forms for a portion of your clinics at one time. For example, a site could first implement forms for all surgical clinics at one location. There are a number of issues to decide upon before actually printing the forms. Some of these may be:

> A. Where will the forms be printed and how will they be distributed? Your committee members must decide if they will be printed at night in one location and how they will be distributed. It may be feasible to have them print near the site's file room. Due to the availability of the Print Manager functionality, your site can designate other forms, such as the Routing Slip, Pharmacy Action or Information Profile, and any identified Health Summary reports to print in terminal digit or alphabetical (clinic then patient) order. This way, the printouts can easily be integrated with patient record pull lists and attached to the patient's record during the chart pull process.

> B. After Encounter Forms are filled out by the clinician and used by the clerk to input information, where do they go? Your committee should decide whether to include them in the patient's chart, send to billing, etc. Input from MAS and MCCR is necessary at this step.

> C. Data Validation considerations. Will your facility implement a "checks & balances" function to insure information from the sheet is entered correctly in the system? You may wish to include the Appointment Status tool kit block on your forms as part of this requirement. Clerks can then check off whether the appointment was rescheduled, cancelled, "No-showed" or checked out.

> D. Training. How will you train involved personnel in the use of the Encounter Form? Also, training for different users may be a good idea. An example is an involved clinician providing a training session to other clinicians on the use of and need for the Encounter Form.

> E. "Local" Customs. Local conventions on the use of the form should be decided upon. For example, how will the clerks identify a no-show or a canceled appointment on the form?

> F. Non-compliance. Who will address lack of use of the form (if this is an issue). How will it be handled? Will a Clinical Manager, such as the Chief of Staff or Clinical Service Chief, become involved? Approval and endorsement from Hospital Management will lower the likelihood of problems.

5\. *Monitor the process* and make improvements where you find problems. Keep the committee intact and informed until the process has been completed and is running smoothly at the facility.

4. GENERAL COMMENTSGetting Started

There are steps that the local site must take before encounter forms can be used.

First, forms must be designed and assigned to the clinics. Forms can be shared between clinics, but it is then important to control who has responsibility for editing the shared forms. One important aspect of designing encounter forms is determining what codes should go on the form. Many encounter forms will have lists of CPT codes, diagnosis codes, or problems. Because space on an encounter form is at a premium, careful analysis is required to determine the codes most commonly used by the clinic before entering codes to the form. For CPT codes, there is an option, "Most Commonly Used Outpatient CPT Codes", that can be used to determine a clinic's most commonly used codes.

Procedures for printing the encounter forms must be determined. Some of the questions that must be answered are what printers to use, can the printers be loaded with enough paper, how many days in advance should the forms be printed, what time of day to run the print job, should the printers be watched, and what to do if there are printer problems. It is expected that most printing of forms will be done in batch at night for entire divisions, and that forms will be printed several days in advance with only the add-ons printed the night before.

Then there are questions concerning what to do with the encounter forms - how will the completed encounter forms be routed, who will input the data, etc. It is expected that much of the collected data will be input through Check-out that is part of PIMS 5.3.

The Print Manager that comes with the Encounter Form Utilities is expected to be very useful to the local sites. Sites must decide what reports should be printed. The Print Manager allows these reports to be specified along with the encounter forms. The fastest way to define the reports is at the division level, rather than at the clinic level. Individual clinics can override reports defined to print at the division level.

Printer ConsiderationsLines Per Inch, Characters Per Line

It is highly recommended that each site standardize on the number of lines per page and the number of characters per line that all encounter forms will use. This is because different kinds of forms may be printed for a single print job because it could cover multiple clinics. Since only one device may be selected each time the option is used, unless all forms printed are defined to have the same number of lines per page and characters per line, some of the forms will be printed improperly. During development of the utilities, 80 lines per page, with 132 characters per line was found to be a good choice. Another reason that 132 characters per line is a good choice is that some of the reports that can be printed through the Print Manager require it.

Boxes

The utilities allow boxes to be drawn around blocks. Defining these terminal attributes will improve the appearance of the boxes drawn:

XY CRT

> TOP LEFT CORNER

> BOTTOM LEFT CORNER

> TOP RIGHT CORNER

> BOTTOM RIGHT CORNER

> VERTICAL LINE

> HORIZONTAL LINE

> GRAPHICS OFF

> GRAPHICS ON

> **NOTE:** Boxes printed with a gap between each vertical line are an indication that either the lines per inch or the font point size should be increased.

Underlining

The utilities have the ability to underline text. These terminal attributes might be used if defined:

> UNDERLINE ON

> UNDERLINE OFF

Emboldening

The utilities have the ability to embolden text if these terminal attributes are defined:

> HIGH INTENSITY (BOLD)

> NORMAL INTENSITY (RESET)

> **NOTE:** On the HP LaserJet IIISi that the utilities were developed on, using the terminal setup shown at the end of this section, emboldening did not work! That is because there was no bold font available that had all of the other requested characteristics.

Example Terminal Setup for a HP LaserJet IVSi printer

|                          |                                                  |
|--------------------------|--------------------------------------------------|
| XY CRT                   | W \$C(27)\_"@a"\_DX\_"C"\_\$C(27)\_"@a"\_DY\_"R" |
| FORM FEED                | \#                                               |
| PAGE LENGTH              | 80                                               |
| BACK SPACE               | \$C(8)                                           |
| OPEN EXECUTE             | W \$C(27),"E",\$C(27),"(s16.7H",\*27,"&l8D"      |
| CLOSE EXECUTE            | W \$C(27),"E"                                    |
| UNDERLINE ON             | \$C(27)\_"&dD"                                   |
| UNDERLINE OFF            | \$C(27)\_"&d@"                                   |
| HIGH INTENSITY (BOLD)    | \$C(27)\_"(s3B"                                  |
| RIGHT MARGIN             | 132                                              |
| NORMAL INTENSITY (RESET) | \$C(27)\_"(s0B"                                  |
| GRAPHICS ON              | \$C(27)\_"(10U"                                  |
| GRAPHICS OFF             | \$C(27)\_"(8U"                                   |
| TOP LEFT CORNER          | \$C(218)                                         |
| BOTTOM LEFT CORNER       | \$C(192)                                         |
| TOP RIGHT CORNER         | \$C(191)                                         |
| BOTTOM RIGHT CORNER      | \$C(217)                                         |
| VERTICAL LINE            | \$C(179)                                         |
| HORIZONTAL LINE          | \$C(196)                                         |

REDACTED ISC *Form Header - occupies a block. In*

Troy, NY t*his example, it has an invisible outline.*

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><em><strong>Block - with a solid outline and no block header.</strong></em></p>
<p><em><strong>Contains Data Fields.</strong></em></p>
<p><em><strong>Label &gt;&gt;</strong></em></p>
<p><em><strong>Data &gt;&gt;</strong></em></p></td>
<td><p>Patient Name: IBpatient, One</p>
<p>DOB: JAN 1,1945 PID: 00045-6789</p>
<p><u>SC Conditions:</u></p>
<p>OSTEOMYELITIS 10%</p></td>
<td><em><strong>&lt;&lt; Data field with two subfields</strong></em></td>
</tr>
</tbody>
</table>

*Subcolumn containinga Marking Area*\\

|                              |     |                       |              |     |       |     |     |     |     |     |                                 |
|------------------------------|-----|-----------------------|--------------|-----|-------|-----|-----|-----|-----|-----|---------------------------------|
| *Subcolumn Headers \>\>* |     | VISIT (mark one only) |              |     | CODE  |     |     | X   |     |     |                                 |
| *Group Header \>\>*      |     | NEW PATIENT           |              |     |       |     |     |     |     |     |                                 |
|                              |     | Brief Exam            | (1-10 min)   |     | 90000 |     |     |     |     |     | *Selection List -*          |
| *Group's*                |     | Limited Exam          | (11-20 min)  |     | 90010 |     |     |     |     |     | *contains one column*       |
| *Selections* \>\>        |     | Intermediate Exam     | (21-30 min)  |     | 90015 |     |     |     |     |     | *of selections. The column* |
|                              |     | Extended Exam         | (31-45 min)  |     | 90017 |     |     |     |     |     | *has three subcolumns.*     |
|                              |     | Comprehensive Exam    | (46-60+ min) |     | 90020 |     |     |     |     |     |                                 |
|                              |     | ESTABLISHED PATIENT   |              |     |       |     |     |     |     |     |                                 |
|                              |     | Brief Exam            | (11-20 min)  |     | 90040 |     |     |     |     |     |                                 |
|                              |     | Limited Exam          | (11-20 min)  |     | 90050 |     |     |     |     |     |                                 |
|                              |     | Intermediate Exam     | (21-30 min)  |     | 90060 |     |     |     |     |     |                                 |
| *Subcolumn*              |     | Extended Exam         | (31-45 min)  |     | 90070 |     |     |     |     |     |                                 |
| *containing TEXT* \>\>   |     | Comprehensive Exam    | (46-60+ min) |     | 90080 |     |     |     |     |     |                                 |
|                              |     |                       |              |     |       |     |     |     |     |     |                                 |

|                                   |     |                                       |           |     |     |     |     |      |           |     |     |
|-----------------------------------|-----|---------------------------------------|-----------|-----|-----|-----|-----|------|-----------|-----|-----|
| *Block Header -*              |     |                                       |           |     |     |     |     |      |           |     |     |
| *centered and underlined\>\>* |     | PLEASE CHECK OFF CPT CODES THAT APPLY |           |     |     |     |     |      |           |     |     |
|                                   |     |                                       |           |     |     |     |     |      |           |     |     |
|                                   |     | CODE                                  | PROCEDURE | X   |     |     |     | CODE | PROCEDURE | X   |     |
| *This Selection List has two* |     |                                       |           |     |     |     |     |      |           |     |     |
| *columns. Each column*        |     |                                       |           |     |     |     |     |      |           |     |     |
| *has three subcolumns.*       |     |                                       |           |     |     |     |     |      |           |     |     |
|                                   |     |                                       |           |     |     |     |     |      |           |     |     |

*Block Header -*

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 0%" />
<col style="width: 2%" />
<col style="width: 23%" />
<col style="width: 49%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><em><strong>underlined, not centered &gt;&gt;</strong></em></td>
<td></td>
<td colspan="3">TEST SAMPLE BLOCK</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><em><strong>Form Lines -</strong></em></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><em><strong>(Horizontal &amp; Vertical)&gt;&gt;</strong></em></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>RELEASE OF INFORMATION: I authorize any</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>holder of medical information about me</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>to release to the Health Care Financing</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Administration (Medicare), and its</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>agents any information needed to</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><em><strong>Text Area &gt;&gt;</strong></em></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>determine these benefits or the</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>benefits payable for related services.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>I authorize any holder of medical</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>information about me to release to any</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>insurance company ..........</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

V. INSURANCE DATA CAPTURE1. FUNCTIONAL DESCRIPTION

There have been a number of requests for enhancements to insurance data capture for several years. To accomplish this, conceptual changes in the way insurance data is captured and stored were needed. Changes will be made to the insurance data stored in the patient file. Specifically, data elements which are related to an insurance group plan have been moved. This data may be shared by many patients. (An example of a group plan is General Motors' Retirees' plan. All retirees of GM get the same coverage.)

Users have asked for the ability to store more detailed information about insurance companies, group plans and benefits. IB v2.0 provides at least five new files to store this data, and many new fields in the patient file and the insurance company file. There is no requirement that this information be added.

The data input from screen 5 of Registration and Load Edit are being streamlined with this release. There are stand-alone options to update the insurance company and patient insurance information and there are view-only options that mirror the data input options. Additionally, there are tools provided to help clean up files containing duplicate and/or inactive insurance companies.

This module is radically different from what you now have. Currently you have two main components to insurance information, insurance company information and patient policy information. IB v2.0 will have five main components to insurance information. You will still have insurance company information which is greatly enhanced and will be discussed later. We are dividing the current patient policy information into two components. We are leaving the information specific to that patient's policy in the Patient file but we are moving information specific to the group plan to a new file. This then allows us to add the two new components, Annual Benefits and Benefits Used.

Many patients have identical policies providing identical benefits from the same group plan. The goal was to input this data once and then have it be known to all patients who belong to the same group plan.

Future releases of IB will include enhancements to the Insurance Data Capture module. It is our goal that once we know this information, we can accurately estimate the dollar amount we can expect to receive for any episode of care. If we know the type of care and compute the billing charges, the benefits available, and the benefits used to date we can attempt to compute what we should receive. This will tie in closely to an MCCR/UR module we call Claims Tracking that will also be released with IB v2.0.

Insurance Company Changes

There is a great deal of new functionality in the Insurance Company module. First there is a new Insurance Company Edit option. You will use this option to enter and store all of the addresses and phone numbers used by an insurance company--addresses for inpatient claims, outpatient claims, appeals, pre-certifications and inquiries. In addition, it is possible to specify that one company performs functions (such as pre-certifications or outpatient claims) for another company. The addresses supplied here are then automatically used in the billing module. If you don't enter data in these special address fields, bills will continue to use the original "main" address of the company performing the function. Additionally, both a comments field and a field for synonyms (alternative names for the same insurance carrier) have been added to the Insurance Company file.

IB v2.0 provides you with tools to manage duplicate entries in your Insurance Company file. There is a new report that shows patients with policies associated with INACTIVE insurance companies. You may use the new Insurance Company Edit option to inactivate insurance companies (provided you hold a new key, IB INSURANCE SUPERVISOR). One reason to inactivate an insurance company is that it is already in the Insurance Company file, but under a synonym. When inactivating a company you may print a list of its patients and (optionally) merge these patients to a new company. Because the new data structures are a little complex, we do the whole thing auto-magically for you. You may also specify synonyms for insurance companies. With these two tools you should be able to inactivate duplicate-named companies and reduce potential new duplicates, as well as clean up old problems.

Unwanted insurance company entries should be inactivated rather than deleted. It will not be possible to delete an insurance company unless you are a holder of the new key, IB INSURANCE SUPERVISOR and all patients with policies with this company have been merged to another company. Because of the new MCCR NDB reports it is important to keep old entries that have claims associated with them as this may be reported nationally.

Patient Insurance Policy Changes

The agent information currently stored in the Patient file is being flagged as obsolete as well as the Group Name and Group Number fields in the Patient file, which are moving to the new Group Plan file. A separate message is being sent as formal notification to the IRM services. If you currently use any data in these fields and anticipate continued need you will need to work with your local IRM to make sure they save this data.

There is a lot of new functionality being added to the patient policy information. We are now automatically capturing the user and date the information is entered and last edited. There is a separate action to verify the insurance and record the date and the user performing the verification. We have added a field to specify if the policy is the primary, secondary, or tertiary policy for this patient. We have added the ability to specify that the policy should be sent to the patient's employer and to put in the specific address it should be sent to for those patients whose employers pre-process claims for the insurance carrier. Deleting policies will not be allowed if that patient has any un-canceled bills associated with the same insurance company.

One of the major new components is the addition of a bulletin that is sent every time a new policy is added for a patient and the patient has current or previous episodes of care (in the past two years) which may be billable. The bulletin will list the policy added, any previous policies, what is potentially billable inpatient and outpatient care, and who added the policy and when, and the option used. This is intended to help us bill for care when the policy is identified after the care was provided.

Group Plans

This new functionality is being called Group Plans to differentiate it from the term "policy". Each patient policy will point to a group plan. If the plan is an individual plan then only that patient may have that plan. This is where the new group number and group name will be stored. It is important to realize that editing this information may affect many more patients than just one. It is also possible to store whether pre-certification, and Utilization Review are required for this plan. For each plan, you may indicate its type, e.g., is it a major medical plan, Medicare supplemental, etc., whether the plan requires UR, and whether it requires pre-certification. This information is used by the Claims Tracking module also scheduled for release with IB v2.0.

The ability to add comments is being greatly expanded. Brief comments may be added about a policy in the patient file. Long comments may be added about the group plan that can then be seen when editing the policy information for all patients with that plan. Comments may also be added when calling for insurance verification of inpatient care along with updating fields about who was contacted, any pre-certification or authorization number, etc. This information is then available to the person doing MCCR/UR reviews.

Annual Benefits

The ability to store the benefits that a plan covers by year has been added. The year will usually be a calendar year but may start on any date. There are many fields to enter the amount or percent of coverage for specific types of care (inpatient, outpatient, mental health, substance abuse, etc.). Once this data is entered for a year it will be available for all patients covered by the same group plan. This functionality will help those of you who have to call for insurance verification. There will be an up-front cost to gathering and storing this data but once captured it will be of great benefit. Entry of any or all information in this file is strictly a local decision.

Benefits Used

As part of insurance verification, such questions as whether the patient has any remaining coverage for the type of care the patient is receiving in your medical center may be asked. This is especially true for mental health and rehabilitative services. A place is now provided to record this information. You may enter the benefits used, e.g., has the patient met any applicable deductible, how much has been paid on an annual or lifetime maximum, etc. This information should be of great help when determining if the amount received from a carrier matches the expected receivable.

2. CHANGED OPTIONSInsurance Company Edit \[IBCN INSURANCE CO EDIT\]

The Insurance Company Edit option has changed both in functionality and appearance. The option now uses the List Manager screens as does much of Integrated Billing. The functionality has been expanded to handle a number of different addresses, to provide for synonyms and comments, and to add tools to merge companies. When editing an insurance company the following actions are available:

Actions

<u>Billing Parameters</u> - This action allows editing of fields that are used by the billing module.

<u>(In)Activate Company</u> - This action allows users to inactivate an active company or activate an inactive company. When inactivating a company a warning will be given if there are patients covered by this company. If so, then the user will be allowed to print a list of the patients and to repoint, or merge the patients into another (active) insurance company entry. Use the new option List Inactive Ins. Co. Covering Patients to get a list of these companies. Then choose the action (In)Activate Company and accept the inactive status and you can then list the patients and merge companies if you choose to. When patients are repointed, no plan or policy data from the inactive company entry is lost. Rather, this information is inherited by the insurance company entry to which the patients have been repointed.

<u>Main Mailing Address</u> - It is now possible to specify a number of new specific addresses for each insurance company. The old address fields are now referred to as the Main Mailing Address. This action allows editing of this address. Billing will automatically use the main mailing address unless a separate address has been specified for claims, appeals, or inquiries.

<u>Inpt Claims Office</u> - This action allows the user to specify a separate address and phone for inpatient claims. There are two ways to specify Inpt Claims addresses. First you can specify that another company processes inpatient claims for the original company. If you specify the company then the inpatient claims address or main mailing address of the entry that is specified will be used. Alternatively a user can complete the address and phone number fields for a separate address for the original company.

<u>Opt Claims Office</u> - This action allows the user to specify a separate address and phone for outpatient claims. There are two ways to specify Opt. Claims addresses. First you can specify that another company processes outpatient claims for the original company. If you specify the company then the outpatient claims address or main mailing address of the entry that is specified will be used. Alternatively a user can complete the address and phone number fields for a separate address for the original company.

<u>Prescr Claims Office -</u> This action allows the user to specify a separate address and phone for prescription claims. There are two ways to specify Prescr Claims addresses. First you can specify that another company processes prescription claims for the original company. If you specify the company then the prescription claims address or main mailing address of the entry that is specified will be used. Alternatively a user can complete the address and phone number fields for a separate address for the original company.

<u>Appeals Office</u> - This action allows the user to specify a separate address and phone for sending appeals. There are two ways to do this, and they are analogous to the two ways to specify Claims Office addresses (see above).

<u>Inquiry Office</u> - This action allows the user to specify a separate address and phone for insurance verification. There are two ways to do this, and they are analogous to the two ways to specify Claims Office addresses.

<u>Remarks</u> - This action allows the user to add comments about the insurance company screen.

<u>Synonyms</u> - This action allows the user to specify synonyms for this company. Part of the problem with duplicate insurance companies is that previously there was no way to assign multiple names to the same company. For example, there are several common abbreviations for Blue Cross Blue Shield, such as BCBS, BC/BS, BC-BS, all which may appear as unique entries in your data base, thus creating duplicates. When merging companies, make sure you add the common synonyms so that it is easy to retrieve the correct company for the personnel adding policies.

<u>Edit All</u> - This action allows editing of all the fields in the Insurance Company file.

<u>Change Insurance Company</u> - This action allows selecting a new insurance company to edit without having to leave the option or action.

<u>Exit</u> - This action allows leaving the option as does the hidden action Quit.

3. NEW OPTIONSPatient Insurance Menu \[IBCN INSURANCE MGMT MENU\]

This menu contains the Insurance Company Edit option, the Patient Insurance Info View/Edit option, the two new reports and the two view-only options. It is designed as a supervisor's menu where all insurance-related options are logically located. Normally one or two of the edit or view options will be placed on menus for the necessary users.

Patient Insurance Info View/Edit \[IBCN PATIENT INSURANCE\]

This new option allows editing or viewing of all patient policy and plan information. It consists of one list screen and three display screens. Upon selecting a patient the user is given a list of the patient's policies and may take a number of actions on these. Three of the actions involve moving to the three display screens that in turn have their own set of actions that may be taken. There is the Expanded Policy View screen where the user can add/edit the policy and plan information and view comments, user information, etc. There is the Annual Benefits screen where the benefits that are provided by the plan for a year can be entered. An annual benefit year may begin on any date and for any plan there may be more than one annual benefit year, but they must all be at least one year apart. And finally there is the Benefits Used screen where the user can enter the benefits that a patient has used against a policy. There must be an annual benefit year for the corresponding plan entered on the Annual Benefits screen before you can enter the benefits used.

Main List Screen (Patient Insurance Info View/Edit)

This screen lists all of the insurance policies for the patient selected.

Actions

<u>Add Policy</u> - This action is used to add a new policy for the patient. A new plan can be created during this action or a previously created plan can be selected.

<u>Delete Policy</u> - This action is used to delete a patient's policy. A policy cannot be deleted if there is a bill for that insurance company for that patient on file. The user must also hold the new key IB INSURANCE SUPERVISOR.

<u>Annual Benefits</u> - This action takes the user to the Annual Benefits screen. See actions below. This is a display, edit screen where a number of possible benefits may be entered.

<u>Policy Edit View</u> - This action takes the user to the expanded view screen for the plan and policy. Information can be edited and viewed, including the addition of comments, user information, contacts, etc. that is not available on the main list screen.

<u>Fast Edit All</u> - This action allows the user to quickly edit the most common information about a policy.

<u>Benefits Used</u> - This action takes the user to the Benefits Used screen. See actions below. This is a display, edit screen where a number of commonly used benefits can be entered for the patient for a specific policy/year.

<u>Verify Coverage</u> - This action allows the user to flag the insurance policy as verified. This can be used in conjunction with the new option of New Not Verified Policies to ensure that a contact has been made with the insurance company to verify the insurance. The date and user are automatically stored.

<u>Personal Riders</u> - This action allows the user to edit personal riders.

<u>Change Patient</u> - This action allows the user to select a new patient without exiting the option or action.

<u>Worksheet Print</u> - This action allows the user to print a worksheet to collect insurance information on by hand when contacting an insurance company.

<u>Print Insurance Coverage</u> - This action produces a report whose format is similar to that of Worksheet Print, but it will print the past two years' coverage for the patient's policy.

<u>Exit</u> - This action allows the user to quickly return to the menu.

Policy Edit/View Screen

This screen displays policy and plan information for whichever of the patient's policies that was selected.

Actions

<u>Change Plan Information</u> - This action allows the user to edit a few fields about the group plan.

<u>UR Information</u> - This action allows the user to edit four group plan fields related to Utilization Review.

<u>Effective Dates</u> - This action allows the user to edit the effective and expiration dates of the policy.

<u>Subscriber Update</u> - This action allows the user to edit the subscriber information about the policy.

<u>Insurance Contact Information</u> - This action allows the user to enter the name of a contact with the insurance company. If the patient is a current inpatient this will automatically create an Insurance Review in the Claims Tracking module that is linked to the admission and the information and comments will be available to the person performing the insurance review.

<u>Employer Info</u>. - This action allows the user to specify that the employer pre-processes the claim for the carrier and to enter an address for the claim to be sent to. This address will automatically be used by the billing module.

<u>Add Comment</u> - This action allows the user to enter a brief comment about the patient's policy and an unlimited comment about the group plan.

<u>Fast Edit All</u> - This action allows the user to edit all the common information about the plan and policy.

<u>Annual Benefits</u> - This action takes the user to the Annual Benefits screen. See actions below. This is a display, edit screen where a number of possible benefits may be entered.

<u>Benefits Used</u> - This action takes the user to the Benefits Used screen. See actions below. This is a display, edit screen where a number of commonly used benefits can be entered for the patient for a specific policy/year.

<u>Verify Coverage</u> - This action allows the user to flag the insurance policy as verified. This can be used in conjunction with the new option of New Unverified policies to ensure that a contact has been made with the insurance company to verify the insurance. The date and user are automatically stored.

<u>Exit</u> - This action allows the user to quickly return to the menu.

Annual Benefits Screen

This screen displays the benefits provided by a particular plan for the benefit year that is selected.

Actions

<u>Policy Info</u> - This action allows the user to quickly edit general plan benefits.

<u>Inpatient</u> - This action allows the user to edit inpatient benefits.

<u>Outpatient</u> - This action allows the user to edit outpatient benefits.

<u>Mental Health</u> - This action allows the user to edit mental health benefits.

<u>Home Health</u> - This action allows the user to edit home health benefits.

<u>Hospice</u> - This action allows the user to edit hospice benefits.

<u>Rehab</u> - This action allows the user to edit rehab service benefits.

<u>IV Mgmt</u>. - This action allows the user to edit IV management benefits.

<u>Edit All</u> - This action allows the user to edit all benefit fields.

<u>Change Year</u> - This action allows the user to edit the plan benefits for a different benefit year.

<u>Exit</u> - This action allows the user to quickly return to the menu.

Benefits Used Screen

This screen displays the benefits that a patient has used against one of the benefit years of one of their policies.

Actions

<u>Policy Info</u> - This action allows the user to edit general benefits that have been used, such as has the deductible been met for the year.

<u>Opt Deductible</u> - This action allows the user to enter the outpatient benefits that have been used.

<u>Inpt Deductible</u> - This action allows the user to enter the inpatient benefits that have been used.

<u>Add Comment</u> - This action allows the user to enter comments about the benefits used.

<u>Change Year</u> - This action allows the user to edit the benefits used for a different benefit year.

<u>Edit All</u> - This action allows the user to edit all benefits used fields.

<u>Exit</u> - This action allows the user to quickly return to the menu.

List Inactive Ins. Co. Covering Patients \[IBCN LIST INACTIVE INS W/PAT\]

This option will print a list of insurance companies that are currently inactive yet there are patients that still have policies with these companies. This situation is created when duplicate-named insurance companies are inactivated. Use the (In)activate Company action available through the Insurance Company Edit option to list the patients by company and to merge them to another company if appropriate.

List New not Verified Policies \[IBCN LIST NEW NOT VER\]

This option will print a list of policies added in the selected date range but that have not been verified in the past 365 days. Generally this report is run to find policies added to a patient's record that have not been verified by the person assigned that responsibility. Because policies are generally identified by MAS during registration, this was designed to help sites identify cases added that may still need to have additional data collected.

View Patient Insurance \[IBCN VIEW PATIENT INSURANCE\]

This option is very similar to the Patient Insurance Info View/Edit option, however, no editing of insurance data is allowed. This option can be assigned to users who need read access to this information but have no need to update the information.

View Insurance Company \[IBCN VIEW INSURANCE CO\]

This option is very similar to the Insurance Company Edit option, however, no editing of insurance company data is allowed. This option can be assigned to users who need read access to this information but have no need to update the information.

4. IMPLEMENTATION GUIDELINES

There are a number of tools in the insurance module to identify duplicate insurance company file entries and to resolve these problems. It may also be helpful to review the process of how insurance information is collected at your facility. This module was designed so that as little information as possible would be collected during registration and that the complete information was collected by a separate employee who was knowledgeable about insurance information who contacted the insurance company.

1\. Prior to installation

You may want to review how the Group Number and Group Name fields in the Insurance Type multiple of the patient file are entered. These will be used to create the new group plan file. A new group plan will be created for every unique group plan entry for each insurance company. If possible you may want to consolidate similar but unique names.

You may want to print a list of all active and inactive insurance companies along with their addresses. There are a number of new insurance company address fields. Determine which insurance company entries can be inactivated and merged into another (active) insurance company entry. (Note: do not delete the old entries, they must be inactivated at this time.)

Determine which users should have access to the new Insurance options. There are options that allow for view-only access to both the insurance company information and patient insurance information as well as data entry. Limiting the ability of certain individuals to add/edit/delete information may improve the quality of your insurance information. Having accurate and detailed insurance information can improve your collections by focusing your efforts on cases that are reimbursable.

Many sites enter medicare and medicaide policy information as an insurance policy. If the entry in the insurance company file for medicare and medicaide exist, we recommend that the field Will Reimburse? be answered NO. This will prevent the software from treating this as a billable insurance company entry. If this is answered other than no, this could have a significant impact on the Claims Tracking module.

2\. After Installation:

First run the option List Inactive Ins. Co. Covering Patients. This option will list companies that are currently covering patients but this information is considered non-billable by the insurance and billing software. In the Insurance Co. Enter/Edit option is an action to activate and inactivate an insurance company. Use this action for the inactive insurance companies and it will allow you to print a list of the patients covered under this company. If you wish to merge the patients to another company you may do so at this or a later time.

If you found in your list of insurance companies that you have many similar entries to handle different inpatient, outpatient or prescription address information you may want to combine these entries into one. Choose the entry you wish to update and enter the complete information. Then go back and inactivate the companies you no longer wish to use and use the feature that lets you merge (repoint) the patients to the updated company entry. If you found many similar entries with the same name but entered slightly differently then you may want to consider entering those names as synonyms for the updated company.

The option List New not Verified Policies can be run periodically to list new policies that have been added since a specific date and have not be verified by your insurance staff. Updating this information can help you maintain the patient insurance information in top shape and allow your MCCR staff to concentrate on billing for covered care. This may foster good communication with your insurance carriers and ultimately improve your rates of collection

5. NEW OR CHANGED BULLETINS

There is one new bulletin in the insurance module. A bulletin is generated whenever a new billable insurance policy is added for a patient and the patient has billable inpatient episodes or scheduled outpatient visits within the effective dates of the policy (going back to the beginning of the prior calendar year). The bulletin lists the new policy, any other policies, potentially billable inpatient stays and scheduled outpatient visits.

6. GENERAL COMMENTSProgrammer API's

A number of Programmer API's are now available to retrieve insurance information and to display patients policies. It is requested that developers not directly access insurance information but rather use the provided interface calls so that we do not limit our future development plans. Specific information on using the programmer API's can be found in the IB v2.0 Technical Manual.

(please move the following details on the API's to the technical manual.)

\$\$INSURED^IBCNS1(dfn, date) - This extrinsic function will return a 1 if the patient is insured for the specified date and 0 if the patient is not insured. Input of date is optional, the default is today. No other data is returned. For billing purposes, we only consider a patient insured if he has an entry in the Insurance Type sub-file that meets four conditions: the insurance company is active, the insurance company will reimburse the government (many sites track Medicare coverage of patients, the entry in the Insurance Company file should be set to not reimburse), the effective date is before the date of care, and the expiration date is after the date of care (we treat no entry in the effective date and expiration date fields as from the beginning of time to the end of time). You might find a reference something like this

> I \$\$INSURED^IBCNS1(DFN,+\$G(^DGPM(+DGPMCA,0))) D BILL...

DISP^IBCNS - This tag can be called to do the standard insurance display. This display is used extensively in registration and billing. The variable DFN must be defined to the current patient. Using this display will keep your displays current when we update them or make other data dictionary changes.

ALL^IBCNS1(dfn, variable, active, date)

This function will return all insurance data in the array of your choice. Input the patient internal entry number and the variable you want the data returned in. Optionally you can ask for only active insurance information by putting any true value (non-zero) in the third parameter and a date for the insurance to be active on in the fourth parameter (the default is today). If the value of the third parameter is 2 then insurance companies that do not reimburse the VA will be included. This is primarily to retrieve Medicare policies when it is desirable to include them in active policies such as when printing insurance information on encounter forms.

It will return the 0, 1, and 2 nodes for each entry in the Insurance Type sub-file and the 0 node from the Group Plan file (355.3) in a 2 dimensional array, Array(x, node). The array element Array(0) will be defined to the count of entries. In Array (x, node) x will be the internal entry in the Insurance Type sub-file and node will be 0,1,2 or 355.3. The group name and number fields have been moved to the Group Plan file (355.3), but since many programmers are used to looking for this data on the 0th node from the Insurance Type sub-file we put the current value from 355.3 back into the respective pieces of the 0th node. The code for this call looks something like this:

> K IBINS

> D ALL^IBCNS1(DFN,"IBINS",1,IBDT) I \$G(IBINS(0)) D LIST

See below for additional information that may be useful.

A new field SOURCE OF DATA has been added to the Insurance Type sub-file of the Patient file. If you are involved in a project to identify insurance from any other means than by conventional contact of the patient or the patient's employer, e.g., electronic requests for information, this field should be updated appropriately. The changes to the MCCR national data base will be using this information in determining the cost effectiveness of these and other initiatives.

IBCN NEW INSURANCE EVENTS Event Driver. We have added an event driver that is executed every time that a new insurance policy for a patient is added. The IVM team will be using this event driver in the future. We created it so that there was a single point where adding of all new insurance policies is known. We use this to trigger a bulletin whenever a new policy is added that has current or past (two years) potentially billable care. We do not execute this for edits or deletions as we have no current need. This could be done if requested.

We have at least one integration agreement to use calls in routine DGCRNS. This routine will continue to be exported and supported with IB v2 but will be discontinued with the first release 18 months after IB v2 is released. Developers can easily convert to the same functionality as it appears in routine IBCNS (almost exactly the same functionality, just moved to the IB namespace) or convert to the more reliable calls listed above. There is a logic problem with the calls to DGCRNS and IBCNS that return the insurance arrays that may cause a second policy with the same company to fail to be contained in the array or list.

  
VI. PATIENT BILLING1. FUNCTIONAL DESCRIPTION

The Integrated Billing Patient Billing module encompasses all software systems which generate charges which are directly billed to the patient. These systems currently include the Pharmacy Copay and the Automated Means Test billing modules.

This release provides many enhancements to the Patient Billing module, focusing primarily on Means Test billing. Full integration is achieved with the Check Out functionality in PIMS v5.3, incorporating legislative changes released over the past year which restrict billing for veterans who have claimed exposure to Agent Orange and Environmental Contaminants. Additionally, outpatient encounters recorded in Scheduling as registrations or "stand-alone" stop codes are now billed automatically. The implementation of this functionality allows sites to flag specific stop codes or dispositions which should not be billed.

The Cancel/Edit/Add Patient Charges option has been re-worked extensively. The user interface has been re-designed, the ordering of prompts has been improved, and new functionality has been introduced.

Many requests for improvements in the Means Test billing module which have been received from the field have been incorporated into this release:

The bulletins generated when patient movement or Means Test data is changed have been improved. These bulletins will now be generated only when Means Test charges might actually be affected. Additional information has been added to the bulletins to aid in the decision-making process. Sites now have the ability to suppress the bulletins generated for patients who have active health insurance.

Means Test billing data may now be transmitted between facilities to assist in the preparation of bills for inpatients who transfer between facilities. This functionality works in conjunction with the PDX v1.5 software package.

Sites routinely experience problems at the beginning of each fiscal year when the new outpatient copayment rate is not available. When the new rate is released to the field, outpatient copayment charges billed since the beginning of the fiscal year require manual editing. In this version, these charges will not be automatically billed to the patient if the effective date of the copayment rate is over one year old. The charges will be held in billing, and once the new rate is entered, all of the charges held up in billing will be passed to the Accounts Receivable package.

This release will also support the enhanced patient statement which is being introduced in Accounts Receivable v4.0. The new statement will provide detailed information for billed prescriptions, outpatient visits, and admissions.

Direct billing to CHAMPVA patients is also supported in this release. CHAMPVA inpatients are required to pay a \$9.30 daily subsistence charge, which is not to exceed \$25.00 for an admission. This functionality is being released with software support from the Accounts Receivable package.

2. CHANGED OPTIONSCancel/Edit/Add Patient Charges \[IB CANCEL/EDIT/ADD CHARGES\]

This option is used primarily to add, cancel, and edit Means Test charges. Many cosmetic, technical, procedural, and functional changes have been made to this option. The charges list has been modified. The user interface has been changed consistently for all actions. The display of billing clock information has been enhanced.

Actions

<u>Add a Charge</u> - The ordering of prompts has been modified. The entry of per diem and inpatient copayment charges has been simplified. CHAMPVA charges may be added. Charges added for deferred or special inpatient billing cases are recognized, and deferred and special inpatient billing cases are automatically dispositioned.

<u>Cancel a Charge</u> - Many new cancellation reasons have been added. The cancellation logic has been improved. Deferred billing cases are recognized and dispositioned.

<u>Edit a Charge</u> - The edit procedure has been simplified. The dialogue has been separated from processing. The edit logic is improved.

<u>Pass a Charge</u> - Deferred billing cases are recognized and dispositioned.

<u>Update Claim Date</u> - This action is used to enter, for a deferred billing case, the date on which the veteran submitted his claim for a service-connected disability. Entry of the date extends the deferment of the charge to 180 days.

<u>Extend Adjudication</u> - Often the claim for service connection cannot be adjudicated within 180 days. This action is used to extend the deferment of the charge to 360 days.

<u>Update Event</u> - This new List Manager application allows the user to manage the event records created in conjunction with inpatient charges.

<u>Change Status</u> - This action is used if the status of the event record must be changed from open to closed, or vice versa.

<u>Last Calc Date</u> - This action is used to change the date that charges were last calculated for an admission.

Outpatient Registration Events Report \[IB OUTPUT EVENTS REPORT\]

This report has been enhanced to display whether the outpatient encounters listed on the report were related to claimed exposures, if those classification questions were answered at Check Out. Also, patients with active insurance, or who have claimed exposures, are flagged on the report. If the report has been queued, it may be stopped by the user.

3. NEW OPTIONSList Deferred Billing Cases \[IB MT LIST DEFERRED CASES\]

Charges billed to veterans whose care was related to exposure to Environmental Contaminants need to be deferred, pending adjudication of the veteran's claim for a service-connected disability. The charges which are created, and thus deferred, are filed as deferred billing cases. This report lists all deferred billing cases, and the final case disposition, for a site.

List Charges Awaiting New Copay Rate \[IB MT LIST HELD (RATE) CHARGES\]

This report may be used to generate a list of all charges which are being held in billing, awaiting the entry of the new Means Test outpatient copay rate.

Release Charges Awaiting New Copay Rate \[IB MT REL HELD (RATE) CHARGES\]

If charges are being held in billing, awaiting entry of the new Means Test outpatient copay rate, and the new rate is entered, all of the charges being held need to be passed to Accounts Receivable. This option recognizes if there are held charges which need to be billed, and allows the user to queue a job to bill all charges on hold awaiting the new rate.

List Special Inpatient Billing Cases \[IB MT LIST SPECIAL CASES\]

If a Category C inpatient has claimed exposure to Agent Orange or Environmental Contaminants, there is no reliable and timely way to determine, electronically, whether the admission was related to the claimed exposure. These admissions are stored as special inpatient billing cases. This option lists all special inpatient billing cases, with the final billing disposition, for a site.

Disposition Special Inpatient Billing Cases \[IB MT DISP SPECIAL CASES\]

Special inpatient billing cases are not billed automatically. Once the case has been determined to be billable or non-billable, action must be taken to disposition the special inpatient billing case. If the case is not to be billed, this option is used to enter the

reason for not billing.

Flag Stop Codes/Dispositions/Clinics \[IB MT FLAG OPT PARAMS\]

Outpatient Encounters which are recorded in the Scheduling package as either registrations or 'stand-alone' stop codes will be billed automatically as those events are checked out. This option is used to flag (or unflag) stop codes and dispositions which should not be billed. The option may also be used to flag clinics where Means Test billing is not appropriate.

List Flagged Stop Codes/Dispositions/Clinics \[IB MT LIST FLAGGED PARAMS\]

This option is used to generate a list of all stop codes, dispositions, and clinics which have been flagged as not being billable for Means Test billing.

4. IMPLEMENTATION GUIDELINES

There is no preparation required by the facility to use the Patient Billing module of Integrated Billing version 2.0. However, the following guidelines are suggested:

Make a list of all stop codes, dispositions, and clinics where the billing of the Means Test outpatient copayment is not desired. These values may easily be entered into the system (utilizing the option Flag Stop Codes/Dispositions/Clinics) from the list.

Decide whether you would like to suppress the generation of bulletins for insured patients who have been billed Means Test copayments. If you wish to suppress these bulletins, update the parameter 'Suppress MT Ins Bulletin' using the option MCCR Site Parameter Enter/Edit.

5. NEW OR CHANGED BULLETINS

There are several new and changed bulletins in the Patient Billing module. Please note that the members of the current Category C Billing mailgroup (IB CAT C) are the recipients of all of these bulletins, with the exception of the bulletin generated after the tasked job to bill copayment charges awaiting the new copay rate is completed.

New Bulletins:

> <u>Special Inpatient Admission</u> - When a Category C veteran who has claimed exposure to Agent Orange, Ionizing Radiation, or Environmental Contaminants is admitted, a bulletin is generated to explain that a special inpatient billing case has automatically been generated for the patient.

> <u>Special Inpatient Discharge</u> - When a Category C veteran who has claimed exposure to Agent Orange, Ionizing Radiation, or Environmental Contaminants is discharged, a bulletin is generated to explain that the user must decide whether or not to bill the patient within 45 days.

> <u>Disposition Special Inpatient Billing Case</u> - If a special inpatient billing case has not been dispositioned within 45 days from the discharge date, a reminder to disposition the case is generated.

> <u>Deferred Billing Case</u> - When a Category C veteran, who has claimed exposure to Environmental Contaminants, receives care which is related to the claimed exposure, the Means Test copayment charge is deferred and a deferred billing case is automatically generated. A bulletin is generated which explains that the veteran must file a claim for service connection within 60 days.

> <u>Disposition Deferred Billing Case</u> - If veteran has filed a claim for service connection, but the case has not been dispositioned after 180 days, a reminder is sent to either extend the adjuducation period an additional 180 days or to disposition the case.

> <u>Bill Deferred Billing Case</u> - If a claim date has not been filed within 60 days, or if the claim has not been adjudicated within 360 days, the deferred charge will automatically be billed to the patient. A bulletin is generated which explains this action and lists the case disposition code which was selected by the system.

> <u>Billing of Stop Codes Exempt from Classification</u> - There are a series of stop codes which are exempt from the classification questions in the Check Out process. If one of these stop codes is filed for a Category C veteran who has claimed exposure, there is not enough information available to determine if the patient should be billed. The system will bill the patient, and then issue a bulletin advising the user to check the patient's medical record to determine if the patient's care was actually related to the claimed exposure. If the care was related to the claimed exposure, the charge should be cancelled using the option Cancel/Edit/Add patient Charges.

> <u>Billing of Charges Awaiting New Copay Rate</u> - If the new Means Test outpatient copay rate is being added, and there are copay charges on hold awaiting the new rate, the user may queue a job which will automatically bill all of the charges awaiting the new rate (the user may also queue this job using the option Release Charges Awaiting New Copay Rate). When the queued job is completed, a bulletin is sent to the user (and not to the Category C Billing mailgroup) which contains the job start and end date/times, and the number of charges passed to the Accounts Receivable module.

> <u>CHAMPVA Admission</u> - A bulletin is generated when a CHAMPVA patient is admitted. The bulletin explains that the inpatient subsistence charge, which is billed directly to the patient, will be automatically generated when the patient is discharged.

> <u>Edited/Deleted CHAMPVA Discharge</u> - If a discharge for a CHAMPVA patient is either edited or deleted, the subsistence charge may need to be edited. This bulletin alerts the user to check the subsistence charge which was billed and determine if it needs to be edited or deleted.

> <u>Error in Billing/Cancelling CHAMPVA Subsistence Charge</u> - The system will generate an error bulletin if a logical error (system cannot determine the billable rate, etc.) occurs while creating or cancelling a CHAMPVA subsistence charge.

Changed Bulletins:

> <u>Changes in Patient Movements</u> - This existing bulletin has been changed so that it will only be generated if either a patient movement date or billable bedsection (derived from the Facility Treating Specialty) has been changed, and the patient has previously been billed for the admission. The actual changes to the movement date and bedsection are included in the bulletin.

> <u>Changes in Means Tests</u> - If a change in a patient's Means Test places the patient in Category C, and the patient has received care since the effective date of the Means Test, a bulletin will be generated which lists the episodes of care which may potentially be billed. If a change in a patient's Means Test removes a patient from Category C, and the patient has been billed Means Test charges since the effective date of the Means Test, a bulletin is generated which lists the charges which may need to be cancelled. If a Category C patient is billed the outpatient copayment charge on the current date, and later on in the day takes a new Means Test which places the patient outside of Category C, the copay charge is automatically cancelled. The bulletin which is generated will state that the listed charge has been cancelled.

> <u>Means Test Charge Billed to Insured Patient</u> - This bulletin has not been changed, but the site may elect to suppress the generation of this bulletin. This may be done by changing the parameter Suppress MT Ins Bulletin in the option MCCR Site Parameter Enter/Edit.

6. GENERAL COMMENTSVII. THIRD PARTY BILLING1. FUNCTIONAL DESCRIPTION

The Third Party Billing Module of Integrated Billing contains the functionality to create bills for insurance companies and other third party payer's. The IB v2.0 release includes enhancements to the previously existing functionality. The HCFA 1500 has undergone major modifications. And there is new functionality that, in conjunction with the Claims Tracking module, will automatically create bills.

GENERAL THIRD PARTY BILLING CHANGES

The length of stay and charge calculations have been modified to count the admission date rather than the discharge date, to be consistent with patient billing. This calculation has also been changed to calculate inpatient interim bills differently. Previously, interim bills had to be overlapped for the correct number of days to be counted. However because bills could not cross the fiscal or calendar year interim bills covering those date ranges could not be overlapped, resulting in the automatic calculation of Length of Stay and the number of days charged being inaccurate. To correct these problems caused by being unable to overlap certain bills the new length of stay calculation counts each day on inpatient interim first and interim continuous bills. Therefore, inpatient interim bills should no longer be overlapped, the beginning of each bill should be one day after the end date of the last bill.

The UB-82 claim form had 5 form locators for Diagnosis. This has been expanded to 9 form locators on the UB-92. This expanded functionality was not provided by IB v1.5 patch 19 when the UB-92 was first released, however this capability is provided in v2.0. Also added is the ability to enter a print order for each diagnosis, similar to the print order for procedures. Therefore the user will no longer need to rearrange the position of the diagnoses, only the print order. The principle diagnosis should always be the diagnosis with the lowest print order.

CHAMPVA has been added as new Rate Type. This will allow CHAMPVA bills to be created and passed to Accounts Receivable.

Both Prescription Refill's and Prosthetic items have been added to the enter/edit and print bill functions. On the UB-92 these items will be printed as free text in the revenue code block, as additional procedures have been. Since the space available on the HCFA 1500 form is limited an addendum sheet has been added to print the relevant information for all prescription refills and prosthetic items on a bill. Several parameters have been defined to help in the creation of the Prescription Refill bills, these are listed under 4. Implementation Guidelines.

A new option has been added to print bills in a user specified order. Bills that have been authorized but not yet printed may be printed in order of their mailing address zip code, insurance company name and/or the patients name.

Functionality has been added to allow the enter and edit of Occurrence Spans and a limited number of Value Codes for the UB-92.

Additional entries have been made to the following lists:

o Discharge Status

o Rate Type

o Revenue Codes

HCFA 1500 CLAIM FORM

The HCFA 1500 functionality has changed significantly in IB v2.0. The form has been expanded to include inpatient as well as outpatient claims so that inpatient professional fees can now the billed on the HCFA 1500. The form has been expanded to allow for multiple pages. Therefore, there is no longer a maximum number of procedures allowed. The version of the printed form in use at most sites contains a series of black bars where the mailing address was being printed, therefore a new site parameter, HCFA 1500 ADDRESS COLUMN, will allow specification of the column that the mailing address should begin printing on.

The Place of Service and Type of Service have been changed so that they can be entered for each procedure rather than having one of each for each bill. Also, the number of ASSOCIATED DIAGNOSIS for each procedure has been expanded from one to four.

The Visit CPT has been removed. This was being used to specify which CPT procedure the outpatient charge would be associated with. The new version has been expanded to allow any revenue code to be entered and the charge functionality is now the same as that for the UB forms. However, the HCFA 1500 form does not allow for revenue codes, each charge must be associated with a CPT procedure. To facilitate coordination between CPT procedures and revenue codes PROCEDURE and DIVISION have been added to all revenue codes being added to a HCFA 1500. If this is entered then the revenue code charge will be associated with that procedure on the printed form. The following rules are used to coordinate the expanded functionality of revenue codes and charges associated with procedures as required in block 24:

> The procedures entered on screens 4 and 5 are printed first in order of their Print Order.

> If a revenue code procedure and division matches one of the CPT procedures from screens 4/5 then the charge associated with that revenue code is printed in the same line item on the bill as the procedure.

> If the revenue code does not have an associated procedure then its charge is printed on the first available CPT line item, i.e. on the line of the first procedure that does not already have a charge.

> If the revenue code does have a procedure but that procedure does not match any CPT procedure entered on screens 4/5 then the line item is printed after all procedures entered on screens 4/5 have been printed, regardless of their print order, with the revenue code procedure (in block 24d) and charge.

> If the revenue code does not have an associated procedure and the charge cannot be matched with any procedure from screens 4/5 then the line item will be printed after all CPT procedures have been printed with block 24d containing the revenue code name and bedsection.

> Please note that to match procedures and revenue codes the number of units must also match. If only one procedure is entered on screen 4/5 but the revenue code has 5 units then one unit of the charge will be printed with the procedure and the other 4 units of charge will be printed with the revenue code and bedsection in block 24d.

Offsets are now allowed and will be printed after all charges and procedures.

A Bill Addendum sheet has been provided to list all rx refills and prosthetic items and their associated information since not all required information can fit on the HCFA 1500 form. This sheet may be printed for each HCFA 1500 that has prescription refills or prosthetic items.

AUTOMATED BILLER

The new functionality of the Automated Bill for Integrated Billing v2.0 builds on the previously existing third party functionality and the new Claims Tracking Module. If the new Claims Tracking module in IB v2.0 is being used for the tracking of inpatient admissions, outpatient visits or prescription refills for veteran patients with insurance then these records can be used to automatically create reimbursable insurance bills. The status of these bills will be ENTERED/NOT REVIEWED and should be processed as any other bills with that status.

There are a variety of parameters that allow each site to control what type of event is automatically billed and when:

> The AUTO BILLER FREQUENCY parameter is used to determine how often and if the auto biller will run. This is the number of days between each successive executions of the auto biller. Using this parameter a site may specify that the auto biller runs every night or once a week, etc. This should be set to zero (or left blank as it is released) if the auto biller should never run.

> The AUTOMATE BILLING parameter controls the amount of user interaction required for automatic bill creation. Bills will be automatically created only for those Claims Tracking events that have an EARLIEST AUTO BILL DATE. The setting of the EARLIEST AUTO BILL DATE for an entry may be accomplished automatically when the entry is created in Claims Tracking if the AUTOMATE BILLING parameter is set. This can be set for each type of event in Claims Tracking that can be automatically billed, currently this is limited to inpatient admissions, outpatient visits and prescription refills. If this site parameter is not set to yes then the auto biller can still be used, however the user must specifically set EARLIEST AUTO BILL DATE for any events that the auto biller should create a bill for.

> The BILLING CYCLE parameter controls the maximum number of days allowed to be billed on a single bill. This can also be specified for each type of event in Claims Tracking that can be automatically billed, currently this is limited to inpatient admissions, outpatient visits and prescription refills. For inpatient bills this is the maximum length of stay for each bill, interim or admit through discharge. If the patient is discharged then the bills date range may be less than the billing cycle. For outpatient visits this is the maximum number of visits dates allowed on a bill. For example if the outpatient billing cycle is set to 3 then the bill may have a date range of 3 days with three outpatient visits dates. However, if the patient had only one visit within the three consecutive day period then the bill will have a date range of one day and only the single outpatient visit date.

> An additional parameter, DAYS DELAY, controls the minimum number of days after certain events occur that a bill may be created. This parameter is used at two different points to determine if a bill should be created. The first time is when the Claims Tracking entry is first created. If the AUTOMATE BILLING parameter is set to Yes, then when the Claims Tracking entry is first created the EARLIEST AUTO BILL DATE will be set to the current date plus the number of days delay. Therefore, the earliest possible date a bill can be created for an event is days delay after entry into Claims Tracking. After that date the auto biller will continuously test the event to see if it is ready to be billed. The second time this parameter is used is when the auto biller is trying to set up a date range for the events bill. In this case DAYS DELAY is added to the BILLING CYCLE to determine if the correct amount of time has elapsed for the bill to be created. Therefore, a bill will not be created until DAYS DELAY after the BILLING CYCLE. For example if DAYS DELAY is 3 and BILLING CYCLE is 10, then a bill will not be created for at least 13 days after the initial entry was created in Claims Tracking.

> Inpatient admissions are handled slightly differently. The auto biller can not create a bill for an inpatient stay until after the PTF record for that stay is closed. Also, if the patient is discharged the auto biller will not wait until the end of the BILLING CYCLE to try to create a bill. Therefore, the number of DAYS DELAY for an inpatient admission is the minimum number of days after discharge or the end of the BILLING CYCLE that the auto biller will begin checking the PTF status and try to create a bill.

> This delay is setup to allow time between the date the event actually occurred until a bill is created for any pre-processing of events that need to be done, such as insurance verification. This will also accommodate any delays such as late entry of events or information. For example, if outpatient visits are generally not coded for 5 days then the days delay should be at least 5.

The automatic biller searches through the Claims Tracking file for entries that have a EARLIEST AUTO BILL DATE not greater than the current date. Any entry with this field not set will not be automatically billed, whether the event is billable or not. If the EARLIEST AUTO BILL DATE is set for the event by the system it will be set to the date the event was entered into Claims Tracking plus the number of DAYS DELAY. This date will be the first date on which the auto biller will attempt to create a bill for the event. Which events are automatically billed can be manually specified by using the Claims Tracking module and entering or deleting the EARLIEST AUTO BILL DATE for the event.

When the auto biller runs it will first attempt to create a bill for any event with an EARLIEST AUTO BILL DATE not greater than the current date. The results of the execution of the auto biller are listed in the AUTOMATED BILLER ERRORS/COMMENTS report. For Claims Tracking events this report will list either the reason no bill was created or the bill number and possibly comments on the bill.

The auto biller checks a variety of data elements concerning an event before a bill is created. The auto biller will only attempt to create reimbursable insurance bills, so the patient must be a veteran with active insurance. Also, the disposition prior to the event date is checked and if NEED WAS RELATED TO AN ACCIDENT or the NEED WAS RELATED TO OCCUPATION then the event may be either Tort Feasor or Workers Comp and the auto biller will not create a bill. Also, since dental is usually billed separately any event with a dental clinic stop will be excluded.

The auto biller also checks to ensure that the event has not already been billed. For outpatient bills it will not set up a bill for an outpatient visit already defined for another uncancelled bill. For inpatients it checks to see if the event is already on another bill, if that bill is a final bill (either interim-last or admit through discharge) then another bill will not be created. If the inpatient event does not have a final bill then the auto biller will create the new bill with a beginning date immediately after the ending date of the already existing bill.

A comment of explanation will be added to the AUTOMATED BILLER ERRORS/COMMENTS report for the event in any of the previous cases and no bill will be created.

If a bill was successfully created then the bill number will be entered into INITIAL BILL NUMBER (if that does not already have a bill) and the EARLIEST AUTO BILL DATE will be deleted (if the bill was a final bill) for the Claims Tracking Entry for the event. Once a bill has been set-up the auto biller continues and attempts to gather as much information as is available. For inpatients, diagnosis and procedures are gathered from the PTF record. Procedures are added for outpatient visits. Additional comments are added to the AUTOMATED BILLER ERRORS/COMMENTS report for the event if the visit is for an SC condition or if any of the movements are for SC conditions or non-billable bedsections.

Entries are removed from the AUTOMATED BILLER ERRORS/COMMENTS report in two ways. If a bill was created for the event then when that bill is either authorized or canceled then the bills entry is removed from the report. If no bill was created then the option Delete Auto Biller Results must be used to delete the entry.

2. CHANGED OPTIONSCopy and Cancel \[IB COPY AND CANCEL\]

Updated to copy the new data fields that can be entered using the Enter/Edit billing Information option from the old bill to the new bill. Also, when a bill that was created by the automatic biller is cancelled the automatic biller comments entry will be deleted from the Automated Biller Errors/Comments report.

Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

This has been changed to reflect changes to Diagnosis, HCFA 1500, and Insurance Data Capture.

Screen 3 - has been modified so that the form type will only be displayed and be editable if the site has multiple form types available to the user. Note that in this instance the UB-82 and the UB-92 are considered a single form so that for a site to have multiple forms they would be using one of the UB forms and the HCFA 1500. This is the same functionality initially released with IB v1.5 however it was modified by IB v1.5 patch 19 so that the transition between the UB-82 and the UB-92 would be visible to the user. However, that transition should be almost complete and the type of UB form is not controlled on screen 3 in any case so it was removed unless there was the possibility of using the HCFA 1500.

Screen 3 - The enter and edit of insurance information on screen 3 has also changed to conform with the new insurance module information.

Screen 4 of the HCFA 1500 - Included add/edit of Occurrence Code State.

Screens 4 and 5 - The enter and edit of diagnosis on Screens 4 and 5 has been modified so that more than 5 diagnosis can be entered, however only 5 will be displayed on the screen. Also added was the ability to enter a print order for each diagnosis, similar to the print order for procedures.

The addition of Prosthetic items to both inpatient and outpatient bills being edited has been added.

Occurrence Spans have been added as a subset of Occurrence Codes. If an Occurrence Span is picked for entry the Date will be consider the beginning date and then End Date will be asked. A limited number of Value Codes have been defined and can be added to a bill on these screens.

Screens 4 and 5 of HCFA 1500 - Place of Service and Type of Service have been added so that they are now entered for each procedure and there is no longer a maximum number of procedures that can be entered. Associated Diagnosis has been expanded to four diagnosis.

Screen 5 - Prescription Refills can now be add to outpatient bills. The Number of Days Supply, Quantity and NDC Number may be added to each prescription refill for printing on the bill if required by the primary insurer.

Screen 6 - Modified the length of stay and charge calculation to count the admission date rather than the discharge date. Also, modified inpatient interim-continuous and interim-last bills to add every day of the bills date range to the charge calculation. Interim inpatient bills should no longer be overlapped.

Screen 6 and 7 of the UB-92 - Replaced BC/BS Provider \# with the more generic Provider \#. This should be the provider number associated with the primary insurance carrier and will be printed in block 51A of the UB-92. The UB-92 does not have a specific field for the BC/BS provider number as the UB-82 did.

Screen 6 and 7 of HCFA 1500 - The Visit CPT has been removed. Revenue codes and their corresponding data can now be added. The charge functionality is now the same as that for the UB forms. Offsets are now allowed. Also, CPT procedure and division may now be entered for each revenue code.

Screen 8 of the UB-92 - Admitting Diagnosis has been changed from a free text entry to an actual ICD-9 diagnosis code. The enter and edit of UB-92 Unlabled Form Locators 2, 11, 31, 37, 56, 57, and 78 have been added to this screen.

Screen 8 of the HCFA 1500 - Enter and edit of Block 31 has been added. Place of Service, Type of Service and Bill Remarks have been removed from this screen.

Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]

An additional column has been added to this report to reflect the actual amount of the bill that is pending collection. If the report is queued, it may be stopped by the user.

Print Bill \[IB PRINT BILL\]

Modified to display during the review and print all new data elements that can be added to a bill. When printing a HCFA 1500 with prescription refills or prosthetic items the Bill Addendum sheet will automatically be printed if a device has been selected for it. Also, when a bill that was created by the automatic biller is printed the automatic biller comments entry will be deleted from the Automated Biller Errors/Comments report.

Third Party Billing Menu \[IB UB-82 MENU\]

The name of this menu has been changed to Third Party Billing Menu \[IB THIRD PARTY BILLING MENU\].

Several new options have been added to this menu:

o Delete Auto Biller Results \[IB CLEAN AUTO BILLER LIST\]

o Print Authorized Bills \[IB BATCH PRINT BILLS\]

o Print Auto Biller Results \[IB OUTPUT AUTO BILLER\]

o Print Bill Addendum Sheet \[IB PRINT BILL ADDENDUM\]

3. NEW OPTIONSDelete Auto Biller Results \[IB CLEAN AUTO BILLER LIST\]

Deletes entries from the AUTOMATED BILLER ERRORS/COMMENTS report for any entry not associated with a bill, before a given date. This option has been added to the Third Party Billing Menu \[IB THIRD PARTY BILLING MENU\]

Employer Report \[IB OUTPUT EMPLOYER REPORT\]

This report searches for all events (either inpatient admissions or outpatient visits) for non-deceased, non-insured patients within a time frame specified by the user. Only if the patient or patient's spouse is employed or has an employer listed then the patient is added. The report is sorted by employer name and lists the employer address as well as various information on the patient and employed person. This report has been added to the Patient Billing Reports Menu \[IB OUTPUT PATIENT REPORT MENU\].

Enter/Edit Automated Billing Parameters \[IB AUTO BILLER PARAMS\]

This option has been added to the MCCR System Definition Menu \[IB SYSTEM DEFINITION MENU\] and is used to enter or edit the parameters controlling the execution of the Automated Biller.

Print Authorized Bills \[IB BATCH PRINT BILLS\]

Prints all authorized bills in a user specified order. This option has been added to the Third Party Billing Menu \[IB THIRD PARTY BILLING MENU\] If a HCFA 1500 with prescription refills or prosthetic items is printed in the batch then the Bill Addendum sheet will automatically be printed if a device has been selected for it. Also, if a bill that was created by the automatic biller is printed the automatic biller comments entry will be deleted from the Automated Biller Errors/Comments report.

Print Auto Biller Results \[IB OUTPUT AUTO BILLER\]

Prints the AUTOMATED BILLER ERRORS/COMMENTS report with the results of the execution of the automated biller, sorted by date. This option has been added to the Third Party Billing Menu \[IB THIRD PARTY BILLING MENU\]

Print Bill Addendum Sheet \[IB PRINT BILL ADDENDUM\]

Prints a Bill Addendum sheets that may accompany HCFA 1500 bills with rx refills or prosthetic items. This sheet will itemize the refills and prosthetic items on a bill with information that is not possible to fit on the HCFA 1500 form itself. This option has been added to the Third Party Billing Menu \[IB THIRD PARTY BILLING MENU\]

Rank Insurance Carriers By Amount Billed \[IB OUTPUT RANK CARRIERS\]

This report ranks, for all claims within a specified date range, insurance carriers by the total amount billed to each carrier. The user may transmit the report to the MCCR Program Office.

4. IMPLEMENTATION GUIDELINES

If your site wishes to use the Automated Biller, enter the values appropriate to your site for the following site parameters that control the execution of the automated biller, using the Enter/Edit Automated Billing Parameters \[IB AUTO BILLER PARAMS\] option:

> AUTO BILLER FREQUENCY: Enter the number of days between each execution of the automated biller. For example, enter 7 if you want bills created only once a week.

> The following parameters may be entered for both inpatient admissions, outpatient visits, and prescription refills:

> AUTOMATE BILLING: Enter 'Y'es bills if should be automatically created for possibly billable events with no user interaction. Otherwise, leave this blank if your site prefers each event to be manually checked before a bill is created by the auto biller.

> BILLING CYCLE: For each type of event, enter the maximum date range of a bill. If this is left blank then the date range will default to the entire month in which the event took place or for inpatient interim bills this will be the next month after the last interim bill.

> DAYS DELAY: Enter the number of days after the end of the BILLING CYCLE that the bill should be created.

The following parameters may be used by sites to control prescription refill billing data and charge calculation. If your site plans to implement Prescription Refill billing then enter the appropriate values using the MCCR Site Parameter Enter/Edit option \[IB MCCR PARAMETER EDIT\]:

> DEFAULT RX REFILL REV CODE used for the revenue code that should be used for most prescription refill bills. If this revenue code is defined then charges will automatically be added to the bill with this revenue code for every prescription refill added to the bill. This site parameter may be overridden by the Insurance Company file parameter PRESCRIPTION REFILL REV. CODE. If left blank .

> DEFAULT RX REFILL DX if applicable, enter a diagnosis code that should be added to every prescription refill bill.

> DEFAULT RX REFILL CPT if applicable, enter a CPT code that should be added to every prescription refill bill.

Other new site parameters that may need to be set using the MCCR Site Parameter Enter/Edit option \[IB MCCR PARAMETER EDIT\]:

> HCFA 1500 ADDRESS COLUMN for the HCFA 1500, enter the column number that the mailing address should begin printing on for it to show in the envelope window, if it does not already print in the appropriate place.

> UB-92 ADDRESS COLUMN for the UB-92, enter the column number that the mailing address should begin printing on for it to show in the envelope window, if it does not already print in the appropriate place.

If the Bill Addendum sheet should be automatically printed for every HCFA 1500 with prescription refills or prosthetic items then the DEFAULT PRINTER (BILLING) must be set for the BILL ADDENDUM form type to the appropriate device using the Select Default Device for Forms option \[IB SITE DEVICE SETUP\].

If certain Insurance Companies require a specific revenue code to be used for Rx Refills that is different than the DEFAULT RX REFILL REV CODE then use the option Insurance Company Entry/Edit \[DG INSURANCE COMPANY EDIT\] to enter the required revenue code in PRESCRIPTION REFILL REV. CODE.

5. NEW OR CHANGED BULLETINS6. GENERAL COMMENTS  
VIII. MISCELLANEOUS CHANGESCHANGED OPTIONSBilling Rates List \[IB LIST OF BILLING RATES\]

This output has been modified to include the new CHAMPVA inpatient subsistence rates and limits.

Enter/Edit Billing Rates \[IB BILLING RATES FILE\]

This option has been modified to allow the entry of the CHAMPVA inpatient subsistence rate and limit. If a new Means Test outpatient copayment rate is entered, and there are charges on hold, awaiting the new rate, the user may queue a job to bill all the charges on hold.

Fast Enter of New Billing Rates \[IB FAST ENTER BILLING RATES\]

If a new Means Test outpatient copayment rate is entered, and there are charges on hold, awaiting the new rate, the user may queue a job to bill all the charges on hold.

Find Billing Data to Archive \[IB PURGE/FIND BILLING DATA\]

Instead of archiving exclusively by fiscal year, the user may archive and purge up through a specified date. Interim claims may only be archived and purged if the final claim may be archived and purged.

MCCR Site Parameter Enter/Edit \[IB MCCR PARAMETER EDIT\]

This option has been updated so that the following parameters may be entered:

o Default Rx Refill Rev Code

o Default Rx Refill Dx

o Default Rx Refill CPT

o HCFA 1500 Address Column

o Suppress Means Test Insurance Bulletins (Yes/No)

o UB-92 Address Column

MCCR System Definition Menu \[IB SYSTEM DEFINITION MENU\]

The new option Enter/Edit Automated Billing Parameters \[IB AUTO BILLER PARAMS\] has been added.

Patient Billing Reports Menu \[IB OUTPUT PATIENT REPORT MENU\]

The option UB-82 Test Pattern Print \[IB UB-82 TEST PATTERN PRINT\] has been removed from this menu.

The new option Employer Report \[IB OUTPUT EMPLOYER REPORT\] has been added to this menu.