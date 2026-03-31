---
consolidated_title: "claims tracking user guide"
app_code: IB
doc_type: UG
master_source: "IB*2*568 Claims Tracking User Guide"
master_pub_date: September 2016
consolidated_from: 2 versions
prior_versions:
  - "IB*2*796 Claims Tracking User Guide"
---

Medical Care Collection Fund (MCCF) eBilling Compliance Phase 3

Claims Tracking and Health Care Services Review – Request for Review and Response (278)

Document Version 2.0

User Guide

![](ib-2-568-claims-tracking-user-guide/001.png)

September 2016

Revised May 2018Department of Veterans Affairs

Office of Information and Technology (OI&T)

Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 58%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td>May 2018</td>
<td>3.0</td>
<td><p>Updated for patch IB*2*568 which added new security key IB PARAMETER EDIT.</p>
<p>Also added new menu option “Manually Add Prosthetics to Claims Tracking” to the Supervisor’s Menu (Claims Tracking)</p></td>
<td><p>PM: REDACTED</p>
<p>Tech Writer: REDACTED</p></td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td>2.0</td>
<td>Updated to reference patient policy comments within the Patient Insurance Screens due to patch IB*2.0*549.</td>
<td><p>PM: REDACTED</p>
<p>Tech Writer: REDACTED</p></td>
</tr>
<tr class="even">
<td>August 2016</td>
<td>1.0</td>
<td>Initial Document</td>
<td><p>PM: REDACTED</p>
<p>Tech Writer:</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

Table of Contents

Table of Figures

[Figure 1: Health Care Services Review – Part 1 [5](#_Toc514255757)](#_Toc514255757)

[Figure 2: Health Care Services Review – Part 2 [6](#_Toc514255758)](#_Toc514255758)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
  - [Project References](#project-references)
  - [Organization of the Manual](#organization-of-the-manual)
  - [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Contingencies and Alternate Modes of Operation](#contingencies-and-alternate-modes-of-operation)
- [Getting Started](#getting-started)
  - [Troubleshooting](#troubleshooting)
- [Claims Tracking Master Menu](#claims-tracking-master-menu)
- [Claims Tracking Menu (Combined Functions) ...](#claims-tracking-menu-combined-functions)
  - [Pending Reviews](#pending-reviews)
    - [About the Screens](#about-the-screens)
    - [Common Actions](#common-actions)
    - [Pending Reviews Screen](#pending-reviews-screen)
    - [Expanded Claims Tracking Entry Screen](#expanded-claims-tracking-entry-screen)
    - [Insurance Reviews/Contacts Screen](#insurance-reviewscontacts-screen)
    - [Expanded Insurance Reviews](#expanded-insurance-reviews)
    - [Hospital Reviews Screen](#hospital-reviews-screen)
    - [Expanded Hospital Reviews Screen](#expanded-hospital-reviews-screen)
  - [Claims Tracking Edit](#claims-tracking-edit)
  - [Single Patient Admission Sheet](#single-patient-admission-sheet)
  - [Insurance Review Edit](#insurance-review-edit)
    - [About the Screens](#about-the-screens-1)
    - [Common Actions](#common-actions-1)
    - [Insurance Reviews/Contacts](#insurance-reviewscontacts)
    - [Expanded Insurance Reviews](#expanded-insurance-reviews-1)
    - [Appeal and Denial Tracking Screen](#appeal-and-denial-tracking-screen)
  - [Appeal/Denial Edit](#appealdenial-edit)
    - [About the Screens](#about-the-screens-2)
    - [Appeal and Denial Tracking Screen](#appeal-and-denial-tracking-screen-1)
    - [Expanded Appeals/Denials Screen](#expanded-appealsdenials-screen)
  - [Inquire to Claims Tracking](#inquire-to-claims-tracking)
  - [Supervisors Menu (Claims Tracking)…](#supervisors-menu-claims-tracking)
    - [Manually Add Opt. Encounters to Claims Tracking](#manually-add-opt-encounters-to-claims-tracking)
    - [Claims Tracking Parameter Edit](#claims-tracking-parameter-edit)
    - [Manually Add Prosthetics to Claims Tracking](#manually-add-prosthetics-to-claims-tracking)
    - [Manually Add Rx Refills to Claims Tracking](#manually-add-rx-refills-to-claims-tracking)
    - [Reports Menu (Claims Tracking)…](#reports-menu-claims-tracking)
  - [Hospital Reviews](#hospital-reviews)
    - [About the Screens](#about-the-screens-3)
    - [Common Actions](#common-actions-2)
    - [Hospital Reviews Screen](#hospital-reviews-screen-1)
    - [Expanded Hospital Reviews Screen](#expanded-hospital-reviews-screen-1)
- [Claims Tracking Menu for Billing ...](#claims-tracking-menu-for-billing)
  - [Claims Tracking Edit](#claims-tracking-edit-1)
    - [Claims Tracking Editor Screen](#claims-tracking-editor-screen)
  - [Print CT Summary for Billing](#print-ct-summary-for-billing)
  - [Assign Reason Not Billable](#assign-reason-not-billable)
  - [Third Party Joint Inquiry](#third-party-joint-inquiry)
- [Claims Tracking Menu (Hospital Reviews) ...](#claims-tracking-menu-hospital-reviews)
- [Claims Tracking Menu (Insurance Reviews)…](#claims-tracking-menu-insurance-reviews)
  - [Health Care Services Review (HCSR) 278 Response](#health-care-services-review-hcsr-278-response)
  - [Health Care Services Review (HCSR) Worklist](#health-care-services-review-hcsr-worklist)
    - [The HCSR Worklist](#the-hcsr-worklist)
    - [HCSR Expanded Entry](#hcsr-expanded-entry)
- [MCCR Site Parameters](#mccr-site-parameters)
  - [The MCCR Site Parameter Display/Edit](#the-mccr-site-parameter-displayedit)
    - [Clinics Included In the Search](#clinics-included-in-the-search)
    - [Wards Included in the Search](#wards-included-in-the-search)
    - [Insurance Companies Included In Appointment Search](#insurance-companies-included-in-appointment-search)
    - [Insurance Companies Included In Admissions Search](#insurance-companies-included-in-admissions-search)
- [Appendix A – Follow-up Actions Codes](#appendix-a-follow-up-actions-codes)
The Claims Tracking module within VistA, is designed to be used by both billing personnel and utilization review (UR) staff. Claims Tracking tracks patient care events such as inpatient admissions, outpatient appointments, prescription releases and issuances of prosthetic devices. These events are most often added to Claims Tracking automatically but they may also be added manually when necessary.
Parameters that control Claims Tracking are defined in the Medical Care Cost Recovery (MCCR) Site Parameter Display/Edit option.
Claims Tracking is used by the automated billing processes in VistA to determine when and if an event should be billed to a third-party payer.
In 1996, Congress passed into law, the Health Insurance Portability and Accountability Act (HIPAA). This Act directs providers and payers to adopt national electronic standards for automated transfer of certain healthcare data between healthcare providers and payers.
One of the standardize transactions for exchange of data is the ASC X12N Health Care Services Review – Request for Review and Response (278). The 278 transaction is designed to allow a provider to request authorization or certification of healthcare services from a Utilization Management Organization (UMO). Initiation of requests and receipt of responses are managed from within Claims Tracking.
The 278 transaction is designed to support the following business events:
- Admission certification review requests and associated responses
- Referral review requests and associated responses
- Health care services certification review requests and associated responses
- Extend certification review requests and associated responses
- Certification appeal review requests and associated responses
- Reservation of medical services review requests and associated responses
- Cancellation of service reservations review requests and associated responses

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user guide is to provide end-users with instructions for using the Claims Tracking software.

## Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA users (UR/RUR nurses) have the ability to manage insurance reviews and hospital reviews through the Claims Tracking module.

VistA users (UR/RUR nurses) have the ability to request authorization for healthcare events such as admissions and clinic appointments for claims tracking events identified by the software. Authorization for care numbers are then added to the claims creation process so that authorization numbers are submitted to the third-party payers as part of the claims.

The implementation of the electronic 278 transaction is intended to replace the manual processes that the sites’ Revenue Utilization Review (RUR) nurses use to obtain authorization numbers as well as the manual processes the billing personnel use to look up the authorization numbers and to add them to the healthcare claims.

Claims Tracking works in conjunction with other VistA modules such as clinical, admission/discharge and transfer (ADT), pharmacy, accounts receivable (AR) and integrated billing (IB).

Outpatient encounters are added to Claims Tracking by the IB MT NIGHT COMP task that runs each night.

VistA is an existing system with a 2 color, roll and scroll interface. There are no changes to the existing architecture, security or backup processes associated with the Claims Tracking software.

The outbound 278 request transactions will be HL7 messages from a VistA site to the Financial Services Center (FSC) in Austin, TX. FSC will then convert the HL7 messages to HIPAA compliant messages which will then be sent to a health care clearing house (HCCH). The HCCH will be responsible for transmitting the messages to the third-party payers or their utilization management organization (UMO).

The inbound 278 response transactions will be HL7 messages received by a VistA site from the FSC. The HCCH will receive HIPAA compliant responses from the payers and will send the responses to FSC. FSC will convert these responses to HL7 before sending them to the originating VistA sites.

## Project References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Reference                                                           | Location                                                                                | Date           |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------|
| Health Care Services Review – Request for Review and Response (278) | <http://www.wpc-edi.com/>                                                               | May 2006       |
| eBilling 278 ICD                                                    | REDACTED                                                                                | June 2016      |
| Integrated Billing (IB) V. 2.0 User Manual                          | <http://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_um.doc> | September 2015 |

## Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document contains the following sections:

- Claims Tracking Master Menu
- Claims Tracking Menu (Combined Functions) ...
- Claims Tracking Menu for Billing ...
- CT ENHANCED for CODERS/MCCR MENU ...
- Claims Tracking Menu (Hospital Reviews) ...
- Claims Tracking Menu (Insurance Reviews) ...

## Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                                                                                    |
|-------|---------------------------------------------------------------------------------------------------------------|
| ADT   | Admission/Discharge/Transfer                                                                                  |
| AR    | Accounts Receivable                                                                                           |
| ASC   | Accredited Standards Committee                                                                                |
| CT    | Claims Tracking                                                                                               |
| ECME  | Electronic Claims Management Engine is the real-time claims processing engine for prescription (RX) claims    |
| FSC   | Financial Service Center                                                                                      |
| HCCH  | Health Care Clearing House                                                                                    |
| HCSR  | Health Care Services Review                                                                                   |
| HIPAA | Health Insurance Portability and Accountability Act                                                           |
| HL7   | Health Level Seven International (HL7) is a not-for-profit, ANSI-accredited standards developing organization |
| IB    | Integrated Billing                                                                                            |
| ICD   | International Classification of Diseases                                                                      |
| Ins.  | Insurance                                                                                                     |
| MCCR  | Medical Care Cost Recovery                                                                                    |
| MT    | Means Test                                                                                                    |
| NUMI  | National Utilization Management Integration (NUMI)                                                            |
| Opt.  | Outpatient                                                                                                    |
| Psych | Psychiatry                                                                                                    |
| QA    | Quality Assurance                                                                                             |
| ROI   | Release of Information                                                                                        |
| RUR   | Revenue Utilization Review                                                                                    |
| RX    | Outpatient Prescription for Medication                                                                        |
| TPJI  | Third Party Joint Inquiry                                                                                     |
| UR    | Utilization Review                                                                                            |
| UMO   | Utilization Management Organization                                                                           |

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific system configurations associated with this project except those mentioned previously:

- Schedule IB MT NIGHT COMP
- Schedule IBT HCSR NIGHTLY PROCESS
- Define MCCR Site Parameter Display/Edit

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ib-2-568-claims-tracking-user-guide/002.png)

<span id="_Toc514255757" class="anchor"></span>Figure : Health Care Services Review – Part 1

![](ib-2-568-claims-tracking-user-guide/003.png)

<span id="_Toc514255758" class="anchor"></span>Figure 2: Health Care Services Review – Part 2

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This functionality is designed to be used by the RUR nurses and the billing personnel at the sites. The following security keys exist to support this functionality:

- IB PARAMETER EDIT – controls access to the MCCR Site Parameter Display/Edit option
- IB Claims Supervisor – controls access to the Supervisors Menu (Claims Tracking) ... option
- IB PARAMETER EDIT – controls access to the option Claims Tracking Parameter Edit which is located on the Supervisors Menu (Claims Tracking) parent menu option.
- IB HCSR Param Edit – controls access to the Health Care Services Review (HCSR) parameters within the MCCR Site Parameters

## Contingencies and Alternate Modes of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The request of authorization of health care services or events can be accomplished via the telephone and/or via some payers’ websites.

Claims can be created manually if a biller has access to data from a patient care event.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements for logging on to or off of VistA associated with the Claims Tracking module.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific problems or issues associated with the use of the Claims Tracking software.

If there are no events being added automatically to the Claims Tracking software, contact your site’s Information Resource Management (IRM) to make sure the IB MT NIGHT COMP task is scheduled to run each night and make sure the site’s Claims Tracking parameters are set as desired by the RUR and billing personnel.

If there are no events being added automatically to the HCSR Worklist, contact your site’s IRM to make sure the IBT HCSR NIGHTLY PROCESS task is scheduled to run each night and make sure the site’s Claims Tracking parameters are set as desired by the RUR and billing personnel.

# Claims Tracking Master Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Claims Tracking module has a master menu that provides access to claims tracking for different groups of users. Each of the following menus is tailored to the expected users’ workflow:

- Claims Tracking Master Menu

Select Integrated Billing Master Menu \<TEST ACCOUNT\> Option: CT Claims Tracking

Master Menu

BI Claims Tracking Menu for Billing ...

CT Claims Tracking Menu (Combined Functions) ...

EN CT ENHANCED for CODERS/MCCR MENU ...

HR Claims Tracking Menu (Hospital Reviews) ...

IR Claims Tracking Menu (Insurance Reviews) ...

Select Claims Tracking Master Menu \<TEST ACCOUNT\> Option:

-   
  Integrated Billing Menu

Select Claims Tracking Master Menu \<TEST ACCOUNT\> Option: bi Claims Tracking Me

nu for Billing

CT Claims Tracking Edit

PS Print CT Summary for Billing

RN Assign Reason Not Billable

TP Third Party Joint Inquiry

Select Claims Tracking Menu for Billing \<TEST ACCOUNT\> Option:

- Combined Menu

Select Claims Tracking Master Menu \<TEST ACCOUNT\> Option: ct Claims Tracking Me

nu (Combined Functions)

PR Pending Reviews

CT Claims Tracking Edit

SP Single Patient Admission Sheet

IR Insurance Review Edit

AD Appeal/Denial Edit

IC Inquire to Claims Tracking

SM Supervisors Menu (Claims Tracking) ...

RM Reports Menu (Claims Tracking) ...

HR Hospital Reviews

HW Health Care Services Review (HCSR) Worklist

HC Health Care Services Review (HCSR) 278 Response

Select Claims Tracking Menu (Combined Functions) \<TEST ACCOUNT\> Option:

- Coder Menu - *Note:* No longer used
- Hospital Reviewer Menu

Select Claims Tracking Master Menu \<TEST ACCOUNT\> Option: HR Claims Tracking Me

nu (Hospital Reviews)

PR Pending Reviews

CT Claims Tracking Edit

HR Hospital Reviews

IC Inquire to Claims Tracking

RM Reports Menu (Claims Tracking) ...

SM Supervisors Menu (Claims Tracking) ...

SP Single Patient Admission Sheet

Select Claims Tracking Menu (Hospital Reviews) \<TEST ACCOUNT\> Option:

*Note:* Hospital reviews are no longer done using VistA Claims Tracking. National Utilization Management Integration (NUMI) is a web-based application that supports hospital reviews.

-   
  Insurance Reviewer Menu

Select Claims Tracking Master Menu \<TEST ACCOUNT\> Option: HR Claims Tracking Me

nu (Hospital Reviews)

PR Pending Reviews

AD Appeal/Denial Edit

CT Claims Tracking Edit

HC Health Care Services Review (HCSR) 278 Response

HW Health Care Services Review (HCSR) Worklist

IC Inquire to Claims Tracking

IR Insurance Review Edit

RM Reports Menu (Claims Tracking) ...

SM Supervisors Menu (Claims Tracking) ...

SP Single Patient Admission Sheet

TP Third Party Joint Inquiry

Select Claims Tracking Menu (Hospital Reviews) \<TEST ACCOUNT\> Option:

# Claims Tracking Menu (Combined Functions) ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu combines many of the Claims Tracking options including the Supervisors Menu and the Claims Tracking parameters. This menu would be appropriate for a supervisory RUR Nurse or a RUR Nurse with multiple duties or a Billing Supervisor.

## Pending Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option uses a series of screens to display all pending reviews that have a pending review date within the last seven days. Each day, a Pending Review List, sorted by ward, patient, assignment or date, should be printed and used to perform reviews. The Pending Reviews option may then be used to perform all necessary actions on the reviews. This option is available to individuals who do Insurance Reviews, Hospital Reviews or both. If the user performs both types of reviews, a plus sign (+) will appear by the names of patients needing both types of review. On admission, appropriate reviews are automatically made pending on the day they are added. Please refer to the Insurance Reviews and Hospital Reviews option documentation for information on when reviews are automatically created.

The following screens show the actions accessed through this option and the actions available on each subsequent screen:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Pending Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>QE Quick Edit</td>
<td>IR Ins. Reviews</td>
<td>RL Remove from List</td>
</tr>
<tr class="even">
<td>VE View/Edit Entry</td>
<td>SC SC Conditions</td>
<td>DU Diagnosis Update</td>
</tr>
<tr class="odd">
<td><em><strong>CT Claims Tracking Edit</strong></em></td>
<td>CS Change Status</td>
<td>PU Procedure Update</td>
</tr>
<tr class="even">
<td>PW Print Worksheet</td>
<td>CD Change Date Range</td>
<td>PV Provider Update</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Claims Tracking Entry</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BI Billing Info Edit</td>
<td><em><strong>IR Insurance Reviews</strong></em></td>
<td>PV Provider Update</td>
</tr>
<tr class="even">
<td>RI Review Info</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td>TA Treatment Auth.</td>
<td>PU Procedure Update</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Insurance Reviews/Contacts</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Ins. Review</td>
<td>SC SC Conditions</td>
<td>PV Provider Update</td>
</tr>
<tr class="even">
<td>DR Delete Ins. Review</td>
<td>AE Appeals Edit</td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>AC Add Comment</td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td><em><strong>VE View/Edit Ins. Review</strong></em></td>
<td>PU Procedure Update</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Insurance Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA Appeal Address</td>
<td>AI Action Info</td>
<td>PU Procedure Update</td>
</tr>
<tr class="even">
<td>CI Contact Info</td>
<td>AC Add Comments</td>
<td>PV Provider Update</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>VP View Pat. Ins</td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="even">
<td>IU Ins. Co. Update</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Pending Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>QE Quick Edit</td>
<td><em><strong>HR Hospital Reviews</strong></em></td>
<td>RL Remove from List</td>
</tr>
<tr class="even">
<td>VE View/Edit Entry</td>
<td>SC SC Conditions</td>
<td>DU Diagnosis Update</td>
</tr>
<tr class="odd">
<td><strong>CT Claims Tracking Edit</strong></td>
<td>CS Change Status</td>
<td>PU Procedure Update</td>
</tr>
<tr class="even">
<td>PW Print Worksheet</td>
<td>CD Change Date Range</td>
<td>PV Provider Update</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Hospital Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Next Hosp.Review</td>
<td><em><strong>VE View/Edit Review</strong></em></td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>DR Delete Review</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td>QE Quick Edit</td>
<td>PU Procedure Update</td>
<td></td>
</tr>
<tr class="even">
<td>CS Change Status</td>
<td>PV Provider Update</td>
<td></td>
</tr>
</tbody>
</table>

<span class="mark"></span>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Hospital Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Ins. Review</td>
<td>SC SC Conditions</td>
<td>PV Provider Update</td>
</tr>
<tr class="even">
<td>DR Delete Review</td>
<td>AE Appeals Edit</td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>AC Add Comment</td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td><strong>VE View/Edit Review</strong></td>
<td>PU Procedure Update</td>
<td></td>
</tr>
</tbody>
</table>

*Notes:*

- The View Edit Entry action will take you directly to the Expanded Insurance or Expanded Hospital Reviews Screens depending on the type of review.
- The View Pat. Ins action brings you to the Patient Insurance Screens.
- The Appeals Edit action brings you to the Appeal and Denial Tracking screen.

### About the Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the top left corner of each screen is the screen title. A plus sign (+) at the bottom left of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right on the screen. Available actions are displayed below the screen. Two question marks entered at any "Select Action" prompt displays all available actions for that screen. For more information on the use of the screens, please refer to the appendix at the end of this manual.

You may quit from any screen, which will bring you back one level or screen, or you may exit (this exits the option entirely and returns you to the menu).

### Common Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are common to more than one screen accessed through this option. They are listed here to avoid duplication of documentation:

- Quick Edit - This action allows you to quickly edit all information about the review without leaving the Pending Review option.
- SC Conditions - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.
- Change Status - This action allows you to quickly change the status of a review. Only completed reviews are used in the report preparation and by the MCCR NDB roll-up or the QM roll-up (which is tentatively scheduled for release in June 1994).
- Reviews have a status of ENTERED when automatically added. A status of PENDING may be used for those you are still working on or when one person does the data entry and another needs to review it.
- Add Comment - This action allows you to edit the word processing (comments) field in Hospital or Insurance Reviews without having to edit other fields.
- Diagnosis Update - This action allows input of ICD diagnoses for the patient. Whether diagnoses are input on this screen or another screen, they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary diagnosis, secondary diagnosis and the onset date of the diagnosis for this admission. For outpatient visits this information is stored with the outpatient encounter information.
- Procedure Update - This action allows the input of ICD procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.
- Provider Update - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document individual physicians if the administrative record indicates teams, or vice versa.
- Change Patient - This action allows you to change the selected patient without having to leave and reenter the option.
- Review Worksheet Print - This action prints a worksheet for use on the wards for writing notes prior to calling the insurance company and entering the review. Basic information about the patient and the visit is included. Please note that the format is slightly different for 80 and 132 column outputs.

### Pending Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Pending Reviews screen:

- View/Edit Entry - This action allows you to jump to either the Expanded Insurance Review screen or the expanded Hospital Review screen, depending on the type of review.
- Claims Tracking Edit - This action allows you to jump to the expanded Claims Tracking screen and perform all necessary edits to the entry in that file. This may include the input of billing information.
- Print Worksheet - This action allows you to print a generic worksheet for selected entries. The latest administrative data is printed on the worksheet including patient name, ward, physicians, room-bed, etc.
- Insurance Reviews - This action allows you to jump to the Insurance Reviews Screen. For details see the Insurance Reviews option documentation. Please note that if you try to perform an Insurance Review on a pending Hospital Review, the software will automatically take you to the Hospital Review screen. This action is not available on the Claims Tracking Menu (Hospital Reviews).
- Hospital Reviews - This action allows you to jump to the Hospital Reviews screen. For details see the Hospital Reviews option documentation. Please note that if you try to perform a Hospital Review on a pending Insurance Review, the software will automatically take you to the Insurance Review screen. This action is not available on the Claims Tracking Menu (Insurance Reviews).
- Change Date Range - This action allows you to change the beginning and ending date of the search for pending reviews. You can search into the past or future for pending reviews. Reviews for the past 7 days is the default.
- Remove From List - This action allows you to quickly remove the review from the Pending Review List by automatically deleting the Next Review Date. For Insurance Reviews, the TRACK AS INSURANCE CLAIM field is also asked. If this is set to NO, no further reviews are automatically created for this visit.

### Expanded Claims Tracking Entry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Claims Tracking screen:

- Billing Info Edit - This action allows you to edit the billing information about expected revenues and next auto bill date. This is useful for comparing expected revenues versus what was received.
- Review Info - This action allows you to review/edit whether or not a special consent release of information form (ROI) for this patient for this episode of care is required, obtained, or not necessary; and whether this review should be tracked as a random sample, insurance claim, special condition, or local addition.
- Treatment Auth. - This action allows you to enter whether a second opinion for this patient insurance policy was required and obtained. (If a second opinion was obtained but did not meet the insurance company's criteria, enter NO in the SECOND OPINION OBTAINED field.) This field will be used to help determine the estimated reimbursement from the insurance carrier. If a second opinion was not obtained, certain denials and penalties may be assessed.
- Hospital Reviews - This action accesses the Hospital Reviews Screen.
- Insurance Reviews - This action accesses the Insurance Reviews/Contacts Screen.

### Insurance Reviews/Contacts Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Insurance Reviews/Contacts screen:

- Add Ins. Review - This action will add a new review for the visit. The default Review Types are:
- Pre-admission Certification Review (a scheduled admission with no previous review)
- Urgent/Emergent Admission Review (a scheduled admission with no previous review)
- Continued Stay Review (for follow-up reviews)
- Other available Review Types are:
  - DISCHARGE REVIEW
  - INPT RETROSPECTIVE REVIEW
  - OPT RETROSPECTIVE REVIEW
  - OTHER
  - OUTPATIENT TREATMENT
  - PATIENT
  - SNF/NHCU REVIEW
  - SUBSEQUENT APPEAL
- Delete Ins. Review - This action allows an insurance review to be deleted. If a review is automatically created, but the visit does not require reviews and follow-up with the insurance company, it can be deleted. Use care in exercising this action. It can be as important to document that no review is required as it is to document the required reviews.
- View/Edit Ins. Review - This action allows access to the Expanded Insurance Reviews Screen.
- Appeals Edit - This action allows you to jump to the Appeals and Denials Screen. For details see the Appeals and Denials option. Only denials and penalties may be appealed. This action is not available on the Claims Tracking for Hospital Reviews option.

### Expanded Insurance Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Insurance Reviews screen:

- Appeal Address - This action allows you to edit the appeals address information for the insurance company.
- Contact Info - This action allows you to enter/edit the review date, person contacted, method of contact, phone and reference numbers.
- Ins. Co. Update - This action allows you to view/edit the billing, pre-certification, verification, claims, appeals, and inquiry phone numbers for the insurance company.
- Action Info - This action allows you to view/edit information pertaining to action taken on a review such as type of contact, care authorization from and to dates, authorization number, and review date and status.
- View Pat. Ins. - This action takes you to the Patient Insurance Screens. Note: From this instance of the Patient Insurance Screen users may not add, edit, or delete Patient Policy Comments. It is in view only mode. For more detailed information on Patient Insurance Menu, refer to the IB V. 2.0 User Manual.

### Hospital Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Hospital Reviews screen:

- Add Next Hosp. Review - This action will add the next review and automatically set it to either an admission review or continued stay review. The day for review and review date are automatically computed but can be edited. The category of severity of illness and intensity of service that was met can be entered; or if not met, the reason it was not met.
- Delete Review - This action allows a hospital review to be deleted. If a review is automatically created, but the visit does not require reviews and follow-up with the insurance company, it can be deleted. Use care in exercising this action. It can be as important to document that no review is required as it is to document the required reviews.
- View/Edit Review - This action allows access to the Expanded Hospital Reviews Screen.

### Expanded Hospital Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Hospital Reviews screen:

- Review Information - This action allows you to enter/edit the type of review (admission or continued stay), review date, and the specialty and methodology for the review. There should be only one admission review for an admission. Normally, reviews are done for RUR purposes on days 3, 6, 9, 14, 21, 28, and every 7 days thereafter. Usually, the INTERQUAL method is used as the methodology for RUR required reviews. Insurance carriers may require other review methodologies.
- Criteria Update - This action allows you to enter or edit data regarding criteria met/not met for an acute admission within 24 hours, such as the review date and methodology; severity of illness and intensity of service; and whether additional reviews are required

## Claims Tracking Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to access the Claims Tracking Editor for a selected patient. From this option, you can do the following additional tasks:

- Delete the tracking entry
- Edit the entry
- Assign the hospital review to a particular user
- Edit billing information
- View or add ROI

Sample Screen

Claims Tracking Editor Oct 22, 2014@10:53:42 Page: 1 of 1

Claims Tracking Entries for: IB,PATIENT 1 IXXXX

for Visits beginning on: 10/22/13 to 11/05/14

Type Urgent Date Ins. UR ROI Bill Ward

1 \*INPT. NO 10/21/14 1:22 pm YES YES C MEDICI

Service Connected: NO \*=Current Admission \>\>\>

*DT Delete Tracking Entry* SC SC Conditions VP View Pat. Ins.

QE Quick Edit AE Appeals Edit *RO ROI ConsentAC Assign Case* CP Change Patient EX Exit*BI Billing Info Edit* CD Change Date Range

VE View/Edit Episode DU Diagnosis Update

HR Hospital Reviews PU Procedure Update

Select Action: Quit//

## Single Patient Admission Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print an admission sheet for a single visit (either the current admission or a selected admission). The admission sheet serves as a temporary cover sheet in the inpatient chart where reviewers and coders can make notes about the visit in summary form. If the facility chooses to have physicians sign the admission sheet, it can then be used as documentation to prepare inpatient bills prior to the signing of the discharge summary.

## Insurance Review Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option uses a series of screens to allow you to enter and edit MCCR/UR related contacts associated with a claims tracking entry.

An initial review is automatically created upon admission for all insured patients. If UR is not required for the patient, the review can be deleted, inactivated, or left in an Entered status. If reviews are performed, and contact with the insurance company is made, the following information can be documented through this option:

- Contact with the insurance company
- Action taken by the insurance company
- Relevant clinical information
- The need for further reviews

Once a review or entry is complete, its status should be updated to COMPLETE in order to be used in reporting. If further reviews are required, the NEXT REVIEW DATE should contain the date on which the next review is required. It will then appear in the Pending Reviews option.

The following screens show the actions accessed through this option and the actions available on each subsequent screen:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Insurance Reviews/Contacts</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Ins. Review</td>
<td>SC SC Conditions</td>
<td>PV Provider Update</td>
</tr>
<tr class="even">
<td>DR Delete Ins. Review</td>
<td><em><strong>AE Appeals Edit</strong></em></td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>AC Add Comment</td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td><em><strong>VE View/Edit Ins. Review</strong></em></td>
<td>PU Procedure Update</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Insurance Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA Appeal Address</td>
<td>AI Action Info</td>
<td>PU Procedure Update</td>
</tr>
<tr class="even">
<td>CI Contact Info</td>
<td>AC Add Comments</td>
<td>PV Provider Update</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>VP View Pat. Ins.</td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="even">
<td>IU Ins. Co. Update</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Appeal and Denial Tracking</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VE View Edit Entry</td>
<td>DA Delete Appeal/Denial</td>
<td>IC Ins. Co. Edit</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>SC SC Conditions</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td>AA Add Appeal</td>
<td>PI Patient Ins. Edit.</td>
<td></td>
</tr>
</tbody>
</table>

### About the Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the top left corner of each screen is the screen title. A plus sign (+) at the bottom left of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right on the screen. Available actions are displayed below the screen. Two question marks entered at any "Select Action" prompt displays all available actions for that screen. For more information on the use of the screens, please refer to the appendix at the end of this manual.

You may quit from any screen, which will bring you back one level or screen, or you may exit (this exits the option entirely and returns you to the menu).

### Common Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are common to more than one screen accessed through this option. They are listed here to avoid duplication of documentation:

- Quick Edit - This action allows you to edit most of the fields in Claims Tracking, specify if there should be insurance or hospital reviews, add billing information, and assign the visit to a reviewer.
- SC Conditions - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.
- Diagnosis Update - This action allows input of International Classification of Diseases (ICD) diagnoses for the patient. Whether diagnoses are input on this screen or another screen, they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis, and the onset of the diagnosis for this admission. For outpatient visits, this information is stored with the outpatient encounter information.
- Procedure Update - This action allows the input of ICD procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.
- Provider Update - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document actual physicians if the administrative record indicates teams or vice versa.
- Change Status - This action allows you to quickly change the status of a review. Only completed reviews are used in the report preparation and by the MCCR NDB roll-up or the QM roll-up.

Reviews have a status of ENTERED when automatically added. A status of PENDING may be used for those you are still working on or when one person does the data entry and another needs to review it.

- Add Comment - This action allows you to edit the word processing (comments) field in Hospital or Insurance Reviews without having to edit other fields.
- Review Worksheet Print - This action prints a worksheet for use on the wards for writing notes prior to calling the insurance company and entering the review. Basic information about the patient and the visit is included. Please note that the format is slightly different for 80 and 132 column outputs.

### Insurance Reviews/Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Insurance Reviews/Contacts screen:

- Add Ins. Review - This action will add a new review for the visit. The default Review Types are:
- Pre-admission Certification Review (a scheduled admission with no previous review)
- Urgent/Emergent Admission Review (a scheduled admission with no previous review)
- Continued Stay Review (for follow-up reviews)
- Other available Review Types are:
  - DISCHARGE REVIEW
  - INPT RETROSPECTIVE REVIEW
  - OPT RETROSPECTIVE REVIEW
  - OTHER
  - OUTPATIENT TREATMENT
  - PATIENT
  - SNF/NHCU REVIEW
  - SUBSEQUENT APPEAL
- Delete Ins. Review - This action allows an insurance review to be deleted. If a review is automatically created, but the visit does not require reviews and follow-up with the insurance company, it can be deleted. Use care in exercising this action. It can be as important to document that no review is required as it is to document the required reviews.
- View/Edit Ins. Review - This action allows access to the Expanded Insurance Reviews Screen.
- Appeals Edit - This action allows you to jump to the Appeals and Denials Screen. For details see the Appeals and Denials option. Only denials and penalties can be appealed. This action is not available on the Claims Tracking for Hospital Reviews option.
- Change Patient - This action allows you to change to another patient without going back to the beginning of the option.

### Expanded Insurance Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Insurance Reviews screen:

- Appeal Address - This action allows you to edit the appeals address information for the insurance company.
- Contact Info - This action allows you to enter/edit the review date, person contacted, method of contact, phone and reference numbers.
- Ins. Co. Update - This action allows you to view/edit the billing, pre-certification, verification, claims, appeals, and inquiry phone numbers for the insurance company.
- Action Info - This action allows you to view/edit information pertaining to action taken on a review such as type of contact, care authorization from and to dates, authorization number, and review date and status.
- View Pat. Ins. - This action takes you to the Patient Insurance Screens. Note: From this instance of the Patient Insurance Screen users may not add, edit, or delete Patient Policy Comments. It is in view only mode. For more detailed information on Patient Insurance Menu, refer to the IB V. 2.0 User Manual.

### Appeal and Denial Tracking Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Appeal and Denial Tracking screen:

- View/Edit Entry - This action allows you to jump to the Expanded Appeal/Denial Screen where you can view much of the data for one visit and perform related actions.
- Add Appeal - This action allows adding an appeal to a denial or penalty. The first appeal will be an initial appeal. All other appeals will be subsequent appeals. You may enter an administrative or clinical appeal. There is no limit to the number of appeals that may be entered.
- Delete Appeal/Denial - This action allows deletion of appeals and denials. This was designed for use in cases of erroneous entry.
- Patient Ins. Edit - This action allows editing of fields in the Insurance Company file (#36) that pertain to appeals address and phone numbers.
- Ins. Co. Edit - This action allows you to edit patient policy information.

*Note:* With the exception of the Edit Pt. Ins. action, all other actions available on this screen are also available on the Expanded Insurance Reviews Screen documented on previous pages.

- Edit Pt. Ins. - This action brings you to the Patient Insurance Screen. Note: From this instance of the Patient Insurance Screen users may add, edit, or delete Patient Policy Comments. For more detailed information on Patient Insurance Menu, refer to the IB V. 2.0 User Manual.

## Appeal/Denial Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to enter, edit, and track the appeals for either a patient or an insurance company. You can speed processing by using the following syntax: 2.\<entry name\> (i.e., 2.John) to enter a patient name or 36.\<entry name\> (e.g., 36.GHI) to select an insurance company. If you simply enter a name, the system searches both files for the name you have entered.

This option uses a series of screens to display denials and penalties and associated appeals. It is very similar to the Insurance Review option; however, if an appeal is approved or partially approved, the amount won on appeal is tracked.

The following shows the Claims Tracking Screens accessed through this option and the actions available on each screen:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Appeals and Denial Tracking</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>VE View Edit Entry</strong></em></td>
<td>DA Delete Appeal/Denial</td>
<td>IC Ins. Co. Edit</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>SC SC Conditions</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td>AA Add Appeal</td>
<td>PI Patient Ins. Edit.</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Appeals/Denials</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA Appeal Address</td>
<td>AI Action Info</td>
<td>EX Exit</td>
</tr>
<tr class="even">
<td>CI Contact Info</td>
<td>AC Add Comment</td>
<td></td>
</tr>
<tr class="odd">
<td>IU Ins. Co. Update</td>
<td>EP Edit Pt. Ins.</td>
<td></td>
</tr>
</tbody>
</table>

### About the Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the top left corner of each screen is the screen title. A plus sign (+) at the bottom left of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right on the screen. Available actions are displayed below the screen. Two question marks entered at any "Select Action" prompt displays all available actions for that screen. For more information on the use of the screens, please refer to the appendix at the end of this manual.

You may quit from any screen, which will bring you back one level or screen, or you may exit (this exits the option entirely and returns you to the menu).

Following is a list of the screens accessed through this option, the actions they provide, and a brief description of each action.

### Appeal and Denial Tracking Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Appeal and Denial Tracking screen:

- View/Edit Entry - This action allows you to jump to the Expanded Appeal/Denial Screen where you can view much of the data for one visit and perform related actions.
- Quick Edit - This action allows you to edit nearly all of the fields in the appeal or denial, add comments, maintain its status, and assign follow-up dates.
- Add Appeal - This action allows adding an appeal to a denial or penalty. The first appeal will be an initial appeal. All other appeals will be subsequent appeals. You may enter an administrative or clinical appeal. There is no limit to the number of appeals that may be entered.
- Delete Appeal/Denial - This action allows deletion of appeals and denials. This was designed to be used in cases of erroneous entry.
- SC Conditions - This action allows a quick look at the patient's eligibility, SC status, service-connected conditions, and percent of service connection for service-connected veterans.
- Ins. Co. Edit - This action allows editing of fields in the Insurance Company file (#36) that pertain to appeals address and phone numbers.
- Patient Ins. Edit - This action allows you to edit patient policy information.

### Expanded Appeals/Denials Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Appeals/Denials screen:

- Appeal Address - This action allows you to edit the name and address for a selected appeal.
- Contact Info - This action allows you to enter/edit the review date, person contacted, method of contact, phone and reference numbers.
- Ins. Co. Update - This action allows you to view/edit the billing, pre-certification, verification, claims, appeals, and inquiry phone numbers for the insurance company.
- Action Info - This action allows you to view/edit information pertaining to action taken on a review such as type of contact, care authorization from and to dates, authorization number, and review date and status.
- Add Comment - This action allows you to edit the word processing (comments) field in Hospital or Insurance Reviews without having to edit other fields.
- Edit Pt. Ins. - This action brings you to the Patient Insurance Screen. Note: from this instance of the Patient Insurance Screen users may add, edit, or delete Patient Policy Comments. For more detailed information on Patient Insurance Menu, refer to the IB V. 2.0 User Manual.

## Inquire to Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to display or print stored information about a single visit. You are prompted to select a patient and the Claims Tracking entry you wish to view/print. Visit, billing, and insurance information is provided, as well as all reviews performed. This output is less detailed than the Claims Tracking Summary for Billing option and does not contain the word processing fields from the reviews.

The following screen is an example of what is displayed for a patient using the Inquire to Claims Tracking option:

  
Sample Screen

Claim Tracking Inquiry Page 1 XXX XX, XXXX@15:55:54

IB,PATIENT 1 XX-XX-XXXX DOB: XXX XX, XXXX

INPATIENT ADMISSION on XXX XX, XXXX@09:30:35

------------------------------------------------------------------------------

Visit Information

Visit Type: INPATIENT ADMISSION Visit Billable: YES

Admission Date: XXX XX,XXXX@09:30:35 Second Opinion: NOT REQUIRED

Ward: C-MEDICINE Auto Bill Date:

Specialty: MEDICINE Special Consent: ROI OBTAINED

Discharge Date: Special Billing: FEDERAL OWCP

------------------------------------------------------------------------------

Billing Information

Initial Bill: Estimated Recv (Pri): \$

Bill Status: Estimated Recv (Sec): \$

Total Charges: \$ 0 Estimated Recv (ter): \$

Amount Paid: \$ 0 Means Test Charges: \$

------------------------------------------------------------------------------

Diagnosis Information

Nothing on File

Associated Interim DRG Information

Nothing on File

------------------------------------------------------------------------

Procedure Information

Nothing on File

------------------------------------------------------------------------

Provider Information

Nothing on File

------------------------------------------------------------------------

Insurance Review Information

Type Review: CONTINUED STAY REVIEW Review Date: XX/XX/XX 1:41 pm

Action: DENIAL Insurance Co.: AETNA US HEALTHCARE

Denied From: XX/XX/XX Person Contacted:

Denied To: XX/XX/XX Contact Method: PHONE

Denial Reasons: FAILURE TO MEET PAYER Call Ref. Number:

Status: PENDING

Last Edited By: UR,NURSE 2

Type Review: URGENT/EMERGENT ADMIT Review Date: XX/XX/XX

Action: Insurance Co.: AETNA US HEALTHCARE

Person Contacted:

Contact Method:

Call Ref. Number:

Status: ENTERED

Last Edited By:

Last Edited By:

------------------------------------------------------------------------------

Hospital Review Information

None on file.

## Supervisors Menu (Claims Tracking)…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manually Add Opt. Encounters to Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient encounters that have been checked out through the Scheduling module are normally added when the IB nightly background job is run. Only primary outpatient encounters that have been processed using the Check Out option of the Scheduling module are added in the first twenty days after the date of the encounter. This option allows you to search for outpatient encounters that were not checked out within twenty days and to automatically add them to Claims Tracking. If you choose to run the automated bill preparation portion of IB V. 2.0, you should periodically run this report to insure that all outpatient care is billed. This option is automatically queued to run in the background and a mail message is sent upon completion.

You may queue this option into the future; however, only outpatient encounters checked out at least one day prior to the actual execution will be added automatically. A message indicating any change will be added to the completion mail message.

Sample Mail Message

Subj: Outpatient Encounters added to Claims Tracking Complete \[#204668\]

10/22/14@15:52 13 lines

From: INTEGRATED BILLING PACKAGE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The process to automatically add Opt Encounters has successfully completed.

Start Date: 05/01/09

End Date: 05/02/09

Total Encounters Checked: 1214

Total Encounters Added: 0

Total Non-billable Encounters Added: 0

\*The SC, Agent Orange, Southwest Asia, Ionizing Radiation,

Military Sexual Trauma, Head Neck Cancer, Combat Veteran and Project 112/SHAD

status visits have been added for insured patients but automatically

indicated as not billable.

Enter message action (in IN basket): Ignore//

### Claims Tracking Parameter Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to edit the MCCR Site Parameters that affect the Claims Tracking module. The parameters can also be edited in the option, MCCR Site Parameters. This option is locked with the IB PARAMETER EDIT security key.

  
Sample Screen

Claims Tracking Parameter Enter Edit

--------------------------------------------------------------------------------

Initialization Date: 01/01/94

Use Admission Sheet: NO

Header line 1: ANYSITE VAMC

Header line 2: 2360 E. ANYSTREET

Header line 3: ANYSITE, WY

Track Inpatient: INSURED AND UR ONLY Track Outpatient: INSURED ONLY

Track Rx: INSURED ONLY Track Prosthetics: INSURED ONLY

Reports can Add CT: YES

Medicine Sample: 5 Surgery Sample: 5

Medicine Admissions: 5 Surgery Admissions: 5

Psych Sample: 1

Psych Admissions: 5

INSURANCE EXTENDED HELP: ON//

CLAIMS TRACKING START DATE: JAN 1,1994//

INPATIENT CLAIMS TRACKING: INSURED AND UR ONLY//

OUTPATIENT CLAIMS TRACKING: INSURED ONLY//

PRESCRIPTION CLAIMS TRACKING: INSURED ONLY//

PROSTHETICS CLAIMS TRACKING: INSURED ONLY//

REPORTS ADD TO CLAIMS TRACKING: YES//

USE ADMISSION SHEETS: NO//

MEDICINE SAMPLE SIZE: 5//

MEDICINE WEEKLY ADMISSIONS: 5//

SURGERY SAMPLE SIZE: 5//

SURGERY WEEKLY ADMISSIONS: 5//

PSYCH SAMPLE SIZE: 1//

PSYCH WEEKLY ADMISSIONS: 5//

Inquiry can be Triggered for Appointment: 14

Inquiry can be Triggered for Admission: 0

Days to wait to purge entry on HCSR Response: 20

The following is a list of each parameter with a brief description:

- Insurance Extended Help

Should the extended help display always be on in the Insurance Management options?

ON - if you always want it to display automatically

OFF - if you do not want to see it

- Claims Tracking Start Date

If you choose to run the Claims Tracking module and populate the files with past episodes of care, this is the earliest visit date for which the Claims Tracking software will automatically add visits.

- Inpatient Claims Tracking

This field determines which inpatients will automatically be added to the Claims Tracking module. It is recommended that this field be set to INSURED AND UR ONLY.

- OFF - no new patients will be added
- INSURED AND UR ONLY - only the insured patients and random sample patients will be added
- ALL PATIENTS -a record of all admissions will be created

If a patient is not insured, each record will be so annotated automatically on creation and no follow-up will be required. The advantage of tracking all patients is that you can determine the percentage of billable cases and make necessary adjustments if the patients are later found to have insurance. The disadvantage is that additional capacity is used.

- Outpatient Claims Tracking

This field determines whether outpatient visit dates will automatically be entered into the Claims Tracking module.

- OFF - no entries will be entered
- INSURED ONLY - only outpatient encounters for insured patients will be added
- ALL PATIENTS - an entry for all outpatient encounters will be added
- Prescription Claims Tracking

This field determines whether prescriptions will automatically be entered into the Claims Tracking module.

If a prescription or refill does not appear to be billable, Service Connected (SC) care for example, or there is a visit date associated with that prescription or refill, this will be noted in the reason not billable.

It is recommended that this field be set to INSURED ONLY.

- OFF - no prescriptions or refills will be entered
- INSURED ONLY - only prescriptions and refills will be added if the patient is insured
- ALL PATIENTS - an entry for all prescriptions will be entered
- Prosthetic Claims Tracking

This field will be used to determine if issuance of prosthetics should be tracked in the Claims Tracking module.

- OFF - no prosthetic items should be tracked
- INSURED ONLY - only prosthetic items for patients with insurance will be tracked
- ALL PATIENTS - prosthetic items for all patients will be tracked
- Reports Add to Claims Tracking

This field determines whether or not to allow the Veterans with Insurance reports to add entries to Claims Tracking. Enter YES for admissions and outpatient visits found as billable but not found in claims tracking to be added to claims tracking for billing information purposes only. No review will be set up. This is to allow the flagging of these visits as unbillable so that they can be removed from these reports.

- Use Admission Sheets

Indicate whether your facility is using Admission Sheets as part of the MCCR/UR functionality. If the answer to this parameter is YES, users will be asked for the device to which admissions sheets are printed. A default device can be defined in the BILL FORM TYPE file.

- Admission Sheet Header Line 1

Enter the text that your facility would like to print as the first line of the header on the admission sheet. This is usually the name of your medical center.

- Admission Sheet Header 2

Enter the text that your facility would like to print as the second line of the header on the admission sheet. This is usually the street address of your medical center.

- Admission Sheet Header Line 3

Enter the text that your facility would like to print as the third line of the header on the admission sheet. This is usually the city, state, and ZIP code of your medical center.

- Medicine Sample Size

This is the number of required Utilization Reviews that you wish to have done each week for Medicine admissions. The minimum recommended by the Quality Assurance (QA) office is one per week.

- Medicine Weekly Admissions

This is the minimum number of admissions that your facility usually averages for Medicine. This is used along with the Medicine Sample Size to compute a random number. Changing this number to a lower value will cause the random sample case to be selected earlier in the week. A higher number provides a more even distribution of cases during the week. If the number exceeds the admissions for the week, the possibility exists that a random sample case may not be generated for this service.

- Surgery Sample Size

This is the number of required Utilization Reviews that you wish to have done each week for Surgery admissions. The minimum recommended by the QA office is one per week.

- Surgery Weekly Admissions

This is the minimum number of admissions that your medical center usually averages for Surgery. This is used along with the Surgery Sample Size to compute a random number. Changing this number to a lower value will cause the random sample case to be selected earlier in the week. A higher number provides a more even distribution of cases during the week. If the number exceeds the admissions for the week, the possibility exists that a random sample case may not be generated for this service.

- Psych Sample Size

This is the number of required Utilization Reviews that you wish to have done each week for Psychiatry admissions. The minimum recommended by the QA office is one per week.

- Psych Weekly Admissions

This is the minimum number of admissions that your medical center usually averages for Psychiatry. This is used along with the Psychiatry Sample Size to compute a random number. Changing this number to a lower value will cause the random sample case to be selected earlier in the week. A higher number provides a more even distribution of cases during the week. If the number exceeds the admissions for the week, the possibility exists that a random sample case may not be generated for this service.

- Inquiry can be Triggered for Appointments

This is the number of days after the creation of an HCSR Worklist entry from an appointment to wait before automatically triggering an X12N Health Care Services Review – Request for Review and Response (278).

- Inquiry can be Triggered for Admissions

This is the number of days after the creation of an HCSR Worklist entry from an admission to wait before automatically triggering an X12N Health Care Services Review – Request for Review and Response (278).

- Days to wait to purge entry on HCSR Response

This is the number of days an HCSR Transmission entry with a completed response status will remain on the HCSR Response Worklist.

### Manually Add Prosthetics to Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prosthetic items which have been issued through the Prosthetics module are normally added to Claims Tracking when the IB nightly background job is run based on the date of service of the item and the day of the month. On the tenth (10<sup>th</sup>) of each month the date range for the IB nightly background job is T-730 days through T-3 days to pull Prosthetics items based on the date of service. On all other days of the month, the date range for the IB nightly background job is T-20 days through T-3 days. This option allows you to search for prosthetic items that have a date of service within a user-specified date range and automatically add them to Claims Tracking. If you choose to run the automated bill preparation portion of IB V. 2.0, you should run this report periodically to insure that all prosthetic items are billed. This option is automatically queued to run in the background and a mail message is sent upon completion.

You may queue this option into the future; however, only prosthetic items issued during the user-specified date range will be added automatically. A message indicating any change will be added to the completion mail message.

Sample Mail Message

Subj: Prosthetic Items added to Claims Tracking Complete \[#114894\] 02 Feb 17 08:52

10 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The process to automatically add Prosthetic Items has successfully completed.

Start Date: 05/01/16

End Date: 07/17/17

(Selected end date of 07/20/17 automatically changed to 07/17/17.)

Total Prosthetics Items checked: 200210

Total NSC Prosthetic Items Added: 14430

Total SC Prosthetic Items Added: 0

\*The items added as SC require determination and editing to be billed

### Manually Add Rx Refills to Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prescription refills that have been released within ten days of the fill date are automatically added to Claims Tracking when the IB MT NIGHT COMP task is run. This option allows you to search for refills that were not released within ten days of the fill date and automatically add them to Claims Tracking. If you choose to run the automated bill preparation portion of IB V. 2.0, you should run this report periodically to insure that all outpatient care is billed. This option is automatically queued to run in the background and a mail message is sent upon completion.

You may queue this option into the future; however, only outpatient encounters checked out at least one day prior to the actual running will be added automatically. A message indicating any change will be added to the completion mail message.

Sample Mail Message

Subj: Rx Refills added to Claims Tracking Complete \[#114894\] 02 Feb 94 08:52

10 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The process to automatically add Rx Refills has successfully completed.

Start Date: 01/22/94

End Date: 01/29/94

(Selected end date of 02/01/94 automatically changed to 01/29/94.)

Total Rx fills checked: 0

Total NSC Rx fills Added: 0

Total SC Rx fills Added: 0

\*The fills added as SC require determination and editing to be billed

Select MESSAGE Action: IGNORE (in IN basket)//

### Reports Menu (Claims Tracking)…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the reports available through the Reports Menu (Claims Tracking):

SR 278 Statistical Volume Report

CR 278 Certification Report

DR 278 Deletion Disposition Report

BI Print CT Summary for Billing

DD Days Denied Report

IC Inquire to Claims Tracking

MS MCCR/UR Summary Report

RC List Visits Requiring Reviews

RW Review Worksheet Print

SA Scheduled Admissions w/Insurance

SP Single Patient Admission Sheet

TODO Pending Work Report

UA Unscheduled Admissions w/Insurance

UR UR Activity Report

Select Reports Menu (Claims Tracking) \<TEST ACCOUNT\> Option:

- 278 Statistical Volume Report

This report is used to monitor the X12 278 transaction process including statistics based on outgoing request, inquiry and incoming responses of authorization received, pending received and rejection received. You can print a statistical report based on the following:

- Report by Staff (All Staff Members or Selected Staff Members)
- Report by Patient (All Patients or Selected Patient)
- Report by Date Range

Sample Report

278 Statistical Volume Report Nov 10, 2015@00:57:39 Page: 1

Sort by: Staff

Report Timeframe:

03/01/2015 - 11/10/2015

All Staff

Staff Date \#278s \#217 \#215 \#215 \#Auth \#Rej \#Pend AAA Await

Submitted Man Auto Recd Recd

================================================================================

IB,STAFF 1 03/05/15 2 2 1 1

IB,STAFF 1 03/26/15 1 1 1

IB,STAFF 1 03/31/15 3 3 1 2

IB,STAFF 1 04/02/15 1 1 1

IB,STAFF 1 04/27/15 2 2 2

IB,STAFF 1 08/04/15 1 1 1

IB,STAFF 1 09/09/15 1 1 1

IB,STAFF 1 11/04/15 1 1 1

------------------------------------------------------

Total 12 12 0 0 1 1 1 0 9

278 Statistical Volume Report Nov 10, 2015@00:57:39 Page: 2

Sort by: Staff

Report Timeframe:

03/01/2015 - 11/10/2015

All Staff

Staff Date \#278s \#217 \#215 \#215 \#Auth \#Rej \#Pend AAA Await

Submitted Man Auto Recd Recd

================================================================================

IB,STAFF 2 03/26/15 1 1 1

IB,STAFF 2 04/02/15 1 1 1

------------------------------------------------------

Total 2 2 0 0 0 0 0 0 2

==============================================================

Grand Total 14 14 0 0 1 1 1 0 11

\*\*\* END OF REPORT \*\*\*

- 278 Certification Report

This report provides information based on the X12 278 transaction based on the outgoing request, inquiry and incoming responses with all types of certification. You can print a certification report based on the following:

- Report by Payer (All Payers or Selected Payers)
- Report by Staff (All Staff Members or Selected Staff Members)
- Report by Patient (All Patients or Selected Patient)
- Report by Date Range

This report is formatted to print 132 columns.

Sample Report

278 Certification Report Nov 10, 2015@01:16:01 Page: 1

Sort by: Payer Detail: Excluded

Report Timeframe:

01/01/2015 - 11/10/2015

All Payer(s)

Payer \#278s \#A1 \#A2 \#A6 \#A4 \#A3 \#C CT NA

====================================================================================================================================

AETNA US HEALTHCARE 1 1

BLUE CROSS/BS WY 4 1 2 1

CIGNA 1 1

-------------------------------------------------------------------------------------------------------

Grand Total 6 2 0 0 2 1 0 0 1

=======================================================================================================

\*\*\* END OF REPORT \*\*\*

- 278 Deletion Disposition Report

This report provides information on the deleted entries. You can print a deletion disposition report based on the following:

- Report by Staff (All Staff Members or Selected Staff Members)
- Report by Patient (All Patients or Selected Patient)
- Report by Date Range

Sample Report

278 Deletion Disposition Report Nov 10, 2015@09:14:36 Page: 1

Sort by: Staff

Report Timeframe:

03/01/2015 - 11/10/2015

Selected Staff

Staff Date \#278s Submitted \#Delete Reasons

================================================================================

IB,STAFF 1 11/02/15 0 2

IB,STAFF 1 10/14/15 1 1

Total 1 3

\*\*\* END OF REPORT \*\*\*

- Print CT Summary for Billing

You can print a Claims Tracking Summary which can be used for preparation of a bill/claim. The content of the summary is based upon the type of Claims Tracking event.

Sample Report 1 – Inpatient Admission

Bill Preparation Report Page 1 Oct 23, 2014@14:53:41

IB,PATIENT 78 XX-XX-XXXX DOB: XXX XX, XXXX

INPATIENT ADMISSION on XXX XX, XXXX@13:22:16

--------------------------------------------------------------------------------

Visit Information

Visit Type: INPATIENT ADMISSION Visit Billable: YES

Admission Date: XXX XX,XXXX@13:22:16 Second Opinion: NOT REQUIRED

Ward: C MEDICINE Auto Bill Date: XXX XX,XXXX

Specialty: MEDICINE Special Consent: ROI NOT DETERMINED

Discharge Date: Special Billing:

------------------------------------------------------------------------

Insurance Information

Ins. Co 1: AETNA US HEALTHCARE Pre-Cert Phone: 800/523-7978

Subsc.: IB,PATIENT 78 Type: COMPREHENSIVE MAJO

Subsc. ID: WXXXXXXXX Group: GRP NUM 8802

Coord Ben: SECONDARY Billing Phone: 800/523-7978

Filing Time Fr: Claims Phone: 800/523-7978

Group Plan Comments:

------------------------------------------------------------------------

Billing Information

Initial Bill: Estimated Recv (Pri): \$

Bill Status: Estimated Recv (Sec): \$

Total Charges: \$ 0 Estimated Recv (ter): \$

Amount Paid: \$ 0 Means Test Charges: \$

------------------------------------------------------------------------

Eligibility Information

Primary Eligibility: NSC, VA PENSION

Means Test Status:

Service Connected Percent: Patient Not Service Connected

------------------------------------------------------------------------

Diagnosis Information

Nothing on File

Associated Interim DRG Information

Nothing on File

------------------------------------------------------------------------

Procedure Information

Nothing on File

------------------------------------------------------------------------

Provider Information

Nothing on File

------------------------------------------------------------------------

Insurance Review Information

Type Review: CONTINUED STAY REVIEW Review Date: XX/XX/XX@1:41 pm

Action: DENIAL Insurance Co.: AETNA US HEALTHCARE

Denied From: XX/XX/XX Person Contacted:

Denied To: XX/XX/XX Contact Method: PHONE

Denial Reasons: FAILURE TO MEET PAYER Call Ref. Number:

Status: PENDING

Last Edited By: UR,NURSE

Comment:

-------------------------------------------------------------------------

Type Review: URGENT/EMERGENT ADMIT Review Date: XX/XX/XX

Action: Insurance Co.: AETNA US HEALTHCARE

Person Contacted:

Contact Method:

Call Ref. Number:

Status: ENTERED

Last Edited By:

Comment:

-------------------------------------------------------------------------

Sample Report 2 – Prescription Refill

Bill Preparation Report Page 1 Oct 23, 2014@15:10:38

IB,PATIENT 37 XX-XX-XXXX DOB: XXX XX, XXXX

PRESCRIPTION REFILL on Jan 13, 2011

--------------------------------------------------------------------------------

Visit Information

Visit Type: PRESCRIPTION REFILL Visit Billable: NO-NO PHARMACY COVE

Prescription \#: XXXXXXX Second Opinion: NOT REQUIRED

Refill Date: XXX XX, XXXX Auto Bill Date:

Drug: LISINOPRIL 20MG TAB Special Consent: ROI NOT DETERMINED

Quantity: 90 Special Billing:

Days Supply: 90

NDC#: 00904-5809-89

Physician: IB,DOCTOR C

------------------------------------------------------------------------

Insurance Information

Ins. Co 1: NORTHWEST ADMINISTRATOR Pre-Cert Phone: 800/872-5439

Subsc.: IB,PATIENT 37 Type: RETIREE

Subsc. ID: XXXXXXXXX Group: GRP NUM 13377

Coord Ben: SECONDARY Billing Phone: 800/872-5439

Filing Time Fr: Claims Phone: 800/872-5439

Policy Comment: POLICY EFF 3-1-03

Group Plan Comments:

PER NOTE, EFF 090103 ALL RX ARE PD @ 20% UNDER MEDICAL

PLAN. SAYS SHOULD'VE NEVER PROCESSED UNDER PRESCRIPTION

PLAN.

POLICY PAYS 70% MEDICARE INPT DEDUCTIBLE.

HAS RX COVERAGE. EFF 010196, NO RX DEDUCTIBLE. INSURANCE

WILL REIMBURSE A MAXIMUM 34-DAY SUPPLY. LARGER AMTS

REIMBURSE 0--DON'T BILL UNLESS THE RX MEETS THIS CRITERIA.

051598: RX PAY @ 20% ALLOWABLE AFTER DEDUCTIBLE. NO

COVERAGE FOR ASCORBIC ACID 001 MG, NUTRITION SUPL ENSURE,

SMOKING DETERRENTS, MULTIVITAMIN/MINERALS CAP/TAB 011200:

PER APRIL, THIS POLICY WILL COVER RX 20% ALLOWABLE AFTER

DEDUCTIBLE; HOWEVER, CLMS APPEAR TO BE PAYING IN EXCESS OF

THAT. DIABETIC & OTHER SUPPLIES ARE COVERED.

122700: PER TAUSHA, EFFECT. 100100 VA IS CONSIDERED

IN-NETWORK AND WE WILL BE REIMBURSED 60% ON BRAND NAME RX.

INS WILL TAKE \$8 COPAY OUT OF OUR REIMBURSEMENT ON GENERIC

RX FOR IN-NETWORK. PRIOR TO THAT DATE VA WAS CONSIDERED

OUT-OF-NETWORK AND OUR REIMBURSEMENT SHOULD'VE BEEN 50%

FOR BRAND NAME RX. THERE IS NO RX DEDUCTIBLE.

NO ROUTINE CARE INCL VISION. NO PRECERT REQ'D VERIFIED

W/BLAINE 013098.

WHEN BILLING ANESTHESIA, INCL TIME PER DEE-DEE 032400.

-----------------------------------

--------------------------------------------------------------------------------

Billing Information

Initial Bill: Estimated Recv (Pri): \$

Bill Status: Estimated Recv (Sec): \$

Total Charges: \$ 0 Estimated Recv (ter): \$

Amount Paid: \$ 0 Means Test Charges: \$

Reason Not Billable: NO PHARMACY COVERAGE

Additional Comment:

------------------------------------------------------------------------

Eligibility Information

Primary Eligibility: SERVICE CONNECTED 50% to 100%

Means Test Status: NO LONGER REQUIRED

Service Connected Percent: 100%

Service Connected Conditions:

LIMITED MOTION OF ANKLE 10%

FLAT FOOT CONDITION 0%

COLD INJURY RESIDUALS 20%

COLD INJURY RESIDUALS 20%

TINNITUS 10%

DEGENERATIVE ARTHRITIS OF THE SPINE 10%

TRAUMATIC ARTHRITIS 10%

TRAUMATIC ARTHRITIS 10%

IMPAIRED HEARING 0%

COLD INJURY RESIDUALS 20%

LIMITED MOTION OF ANKLE 10%

LIMITED MOTION OF ARM 20%

COLD INJURY RESIDUALS 10%

TRAUMATIC ARTHRITIS 10%

POST-TRAUMATIC STRESS DISORDER 30%

TRAUMATIC ARTHRITIS 10%

TRAUMATIC ARTHRITIS 10%

------------------------------------------------------------------------

- Inquire to Claims Tracking

You can display or print stored information about a single visit. You are prompted to select a patient and the Claims Tracking entry you wish to view/print.

The following information is displayed:

- Visit,
- Billing
- Insurance information
- Reviews performed

*Note:* This report does not contain the word processing fields from the reviews.

Sample Report

Claim Tracking Inquiry Page 1 Jan 14, 1994@15:55:54

IB,PATIENT 1 XX-XX-XXXX DOB: XXX XX,XXXX

INPATIENT ADMISSION on XXX XX,XXXX@09:30:35

------------------------------------------------------------------------------

Visit Information

Visit Type: INPATIENT ADMISSION Visit Billable: YES

Admission Date: XXX XX,XXXX@09:30:35 Second Opinion: NOT REQUIRED

Ward: 11-B MEDICINE XREF Auto Bill Date:

Specialty: MEDICINE Special Consent: ROI OBTAINED

Discharge Date: Special Billing: FEDERAL OWCP

Billing Information

Initial Bill: Estimated Recv (Pri): \$

Bill Status: Estimated Recv (Sec): \$

Total Charges: \$ 0 Estimated Recv (ter): \$

Amount Paid: \$ 0 Means Test Charges: \$

Insurance Review Information

Type Review: INITIAL APPEAL Review Date: XX/XX/XX

Appeal Type: ADMINISTRATIVE Insurance Co.: IB INS. CO. 30

Case Status: OPEN Person Contacted: UMO,CONTACT

No Days Pending: 3 Contact Method: Letter

Final Outcome: Call Ref. Number:

Status: COMPLETE

Last Edited By:

Type Review: CONTINUED STAY REVIEW Review Date: XX/XX/XX

Action: DENIAL Insurance Co.: IB INS. CO. 1

Denied From: XX/XX/XX Person Contacted: SPOUSE

Denied To: XX/XX/XX Contact Method: PHONE

Denial Reasons: NOT MEDICALLY NECESSAR Call Ref. Number: XXXXXXSS

Denial Reasons: TREATMENT PROVIDED NOT Status: COMPLETE

Last Edited By: UR,NURSE

Type Review: URGENT/EMERGENT ADMIT Review Date: XX/XX/XX

Action: APPROVED Insurance Co.: IB INS. CO. 14

Authorized From: XX/XX/XX Person Contacted: UMO,CONTACT

Authorized To: XX/XX/XX Contact Method: VOICE MAIL

Authorized Diag: 259.0 - DELAY SEXUAL D Call Ref. Number: XXXXXXXXXA

Auth. Number: 88889354A Status: COMPLETE

Last Edited By: UR,NURSE

Hospital Review Information

Review Date: XX/XX/XX Day of Review: 3

Review Type: CONTINUED STAY REVIEW Severity of Ill: Generic

Specialty: MEDICINE Intensity of Svc: Generic

Methodology: INTERQUAL Non-Acute Reason:

Status: ENTERED

Last Edited By: UR,NURSE

- Days Denied Report

You can print a summary or a detailed listing of denials. The report can be sorted by the following:

- Patient
- Attending physician, or
- Bed service (i.e., surgery, psychiatry, medicine).

The summary report shows the number of denials, the total days denied, the dollar amount of the denials, and the days won on appeal by service.

The detail section includes the following:

- Inpatient Admission's Service, which is the Service the patient was under at either the admission, if that date is included in the report, or the Service the patient was under on the begin date of the report. This Service is used to provide the summary.
- The Amount Denied is also displayed for each denied stay in the detail section. The Amount Denied is either the full charge of the admission, if the entire admission was denied and the entire stay is within the date range of the report, or an average charge based on the full charge and the number of denied days on the report, if only a partial denial. The charges displayed as the Amount Denied are the current active charges per Reasonable Charges.

This report is formatted to print 132 columns.

Sample Report

MCCR/UR DENIED DAYS INPATIENT Denials Dated Jan 01, 2005 to Jan 01, 2006 Page 1 Mar 21, 2013@20:41:30

Dates of Dates Days Approved

Patient PtID Care Attending Denied Denial Reason Appealed on Appeal SRVS Amount

---------------------------------------------------------------------------------------------------------------------------------

IB,PATIENT 1 XXXX 01/24/05 to 520634204 ALL (3) OBSERVATION IS MORE APPRO NO 0 SURG \$19,224

01/27/05

IB,PATIENT 23 XXXX 02/24/05 to 1404 ALL (4) NOT MEDICALLY NECESSARY YES 2 NHCU \$2,777

02/28/05

IB,PATIENT 54 XXXX 12/27/04 to 520629761 ALL (1) NOT MEDICALLY NECESSARY NO 0 NHCU \$629

01/02/05

IB,PATIENT 6 XXXX 09/13/05 to 520644029 ALL (2) NOT MEDICALLY NECESSARY NO 0 MEDI \$13,109

09/15/05

------

10

MCCR/UR DENIED DAYS OUTPATIENT Denials Dated Jan 01, 2005 to Jan 01, 2006 Page 2 Mar 21, 2013@20:41:30

Patient PtID Episode Date Outpatient Treatment Appealed Approved Amount

---------------------------------------------------------------------------------------------------------------------------------

IB,PATIENT 7 XXXX 12/25/05@13:20 OPT OPHTHALMOLOGY ST NO NO \$0

IB,PATIENT 288 XXXX 10/9/05@08:30 YES YES \$126

IB,PATIENT 67 XXXX 10/17/05@15:54 Physical Therapy NO NO \$0

------

3

MCCR/UR DENIED DAYS PROSTHETIC Denials Dated Jan 01, 2005 to Jan 01, 2006 Page 3 Mar 21, 2013@20:41:30

Patient PtID Episode Date Outpatient Treatment Appealed Approved Amount

---------------------------------------------------------------------------------------------------------------------------------

IB,PATIENT 23 XXXX 1/27/05 Av Prosth Auto Blood NO NO \$25

IB,PATIENT 1 XXXX 10/1/05 Delivery/Labor NO NO \$150

------

2

MCCR/UR DENIED DAYS PRESCRIPTION Denials Dated Jan 01, 2005 to Jan 01, 2006 Page 4 Mar 21, 2013@20:41:30

Patient PtID Episode Date Outpatient Treatment Appealed Approved Amount

---------------------------------------------------------------------------------------------------------------------------------

IB,PATIENT 6 XXXX 1/27/05 Av RxFill \#: 7399X89 NO NO \$0

IB,PATIENT 45 XXXX 10/7/05 Rx \#:76699X9 NO NO \$45

------

2

MCCR/UR DENIED DAYS Summary Report for Reviews Dated Jan 01, 2005 to Jan 01, 2006 Page 5 Mar 21, 2013@20:41:30

Number Days Amount Days won

Service Denials Denied Denied on Appeal

---------------------------------------------------------------------------------------------------------------------------------

MEDICINE 1 2 \$13,109 0

NHCU 2 5 \$2,839 2

SURGERY 1 3 \$19,224 0

--------

10

Amount Appeals

Service Number Denied Appealed Approved

---------------------------------------------------------------------------------------------------------------------------------

OUTPATIENT 3 \$126 1 1

PRESCRIPTION 2 \$45 0 0

PROSTHETICS 2 \$175 0 0

- MCCR/UR Summary Report

You can print a summary of hospital activity by either admission or discharge for a specified date range. A Penalty Report is included and, if appropriate, a Days Approved Report, and a Days Denied Report. These are sorted by specialty.

Sample Report

MCCR/UR SUMMARY REPORT

for

SITENAME (001)

for Discharges

From: AUG 18, 1993

To: FEB 14, 1994

Date Printed: FEB 14, 1994

Page: 1

--------------------------

Total Discharges: 29

Total Discharges with Insurance: 5

Total Billable Discharges: 4

Total Discharges Requiring Reviews: 4

Total Discharges Reviewed: 4

Total Discharges Reviewed, Multi Carrier: 0

Total Reviews Done: 5

Number of Days Approved: 10

Amount Collectible Approved for Billing: \$3,370

Number of Days Denied: 4

Amount Denied for Billing: \$1,348

Total Cases Appealed: 0

Number of Initial Appeals: 0

Number of Subsequent Appeals: 0

Penalty Report: Number of cases Dollars

--------------- ------------------------------------

No Pre Admission Certification: 0 \$0

Untimely Pre Admission Certification: 0 \$0

VA a Non-Provider: 0 \$0

Reason Not Billable Report: Reason Count

--------------------------- ------------------------------------

OTHER 1

Days Approved by Specialty: Specialty No. Days Dollars

--------------------------- ------------------------------------

ALCOHOL 10 \$3,370

Days Denied by Specialty: Specialty No. Days Dollars

------------------------- ------------------------------------

ALCOHOL 4 \$1,348

- 
- List Visits Requiring Reviews

You can print a list of visits based on the following:

- Insurance Review,
- Hospital Review
- Both

Only inpatient admission visits are included in the report. This report can be used to list the random sample cases being tracked for hospital reviews by selecting only hospital reviews for admissions.

Sample Output

LIST OF VISITS FROM: 01/01/94 TO: 02/18/94 REQUIRING REVIEWS FEB 18,1994 14:40 PAGE 1

VISIT INS. RANDOM SPECIAL LOCAL HOSP

PATIENT PT. ID WARD TYPE DATE CASE CASE COND. CASE REVIEWER INS REVIEWER

---------------------------------------------------------------------------------------------------------------------------

IB,PATIENT 2 XX-XX-XXXX 8C ORTHO S ADMIT FEB 7,1994 YES YES UR,NURSE

IB,PATIENT 52 XX-XX-XXXX SCH ADM. FEB 4,1994 YES NO COPD NO UR,NURSE

IB,PATIENT 111 XX-XX-XXXX OUTPT FEB 11,1994 YES UR,NURSE

IB,PATIENT 77 XX-XX-XXXX 7A(NHCU) ADMIT FEB 7,1994 NO YES UR,NURSE

IB,PATIENT 9 XX-XX-XXXX 11-B MEDIC ADMIT JAN 13,1994 YES YES NONE NO UR,NURSE ---- --- ---- ---

COUNT 4 3 1 0

- Review Worksheet Print

This option is similar to the Review Worksheet action on the Insurance Review screen. A worksheet for a current inpatient can be printed containing demographic data and information about current room/bed, ward, and provider.

Sample Worksheet

INSURANCE REVIEW WORKSHEET

XXX XX, XXXX@15:33:37

Specialty: MEDICINE Ward: 11-B MEDICINE

Name: IB,PATIENT 34 Insurance Co: IB INS. CO. 12

Pt ID: XX-XX-XXXX

DOB: XXX XX, XXXX

Admission Date: XXX XX,XXXX@09:30:35 DC Date: \_\_\_\_\_\_\_\_ LOS: \_\_\_\_\_

Attending MD: IB,DOCTOR A Primary MD: IB,DOCTOR P

Complaint/Hist: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Treatment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

============================================================================

\|Date \|Diagnosis \|Procedure \|DRG \|LOS \|

\| \| \| \| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\| \| \| \| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\| \| \| \| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\| \| \| \| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\| \| \| \| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

============================================================================

\|Insurance Contact: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\|Date \|Comments (#day approved, next review date, etc.) \|

\| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

\| \| \|

\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|

============================================================================

Reviewer: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- 
- Scheduled Admissions w/Insurance

You can print a list of scheduled admissions in Claims Tracking for insured patients. Included are patients with past scheduled admissions and scheduled admissions up to three days into the future. This differs from the Scheduled Admission List from MAS, as it does not contain all scheduled admissions from MAS. Scheduled admissions are normally moved to Claims Tracking four days prior to the scheduled admission date so that reviews can be completed prior to admission. Included are the number and type of reviews performed and the insurance company actions.

This report is formatted to print 132 columns.

Sample Report

Scheduled Admissions with Insurance Page 1 Feb 11, 1994@09:05:48

For Period beginning on XX/XX/XX to XX/XX/XX

Patient Pt. ID Adm. Date Billable Ward Type

------------------------------------------------------------------------------------------------------------------

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 1:00 pm YES 5D SURG SCHEDULED

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 2:40 pm YES 9D MED SCHEDULED

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 11:40 pm YES 2D CARD SCHEDULED

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 10:11 am NO 4a nurs SCHEDULED

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 9:00 am YES 9D MED SCHEDULED

IB,PATIENT 33 XX-XX-XXXX XX/XX/XX 2:52 pm YES 2B ICU SCHEDULED

------------------

TOTAL = 6

- 
- Single Patient Admission Sheet

You can print an admission sheet for a single visit (either the current admission or a selected admission). The admission sheet serves as a temporary cover sheet in the inpatient chart where reviewers and coders can make notes about the visit in summary form. If the facility chooses to have physicians sign the admission sheet, it can then be used as documentation to prepare inpatient bills prior to the signing of the discharge summary.

Sample Worksheet

ADMISSION SHEET

SITENAME VAMC

113 HOLLAND AVE

SITENAME,NY

Patient: IB,PATIENT 456 Address: 123 TEST ST.

Pt ID: XX-XX-XXXX

Dob: XX XX, XXXX

SC: YES - 20% TROY, NY 12180

Sex: MALE Phone:

--------------------------------------------------------------------------------

Adm. Date: XXX XX, XXXX@09:30:35 Adm. Type: URGENT

Provider: IB,PATIENT 456 Specialty: MEDICINE

Ward: 11-B MEDICINE Room/Bed:

Adm. Diag: 466.0 – ACUTE BRONCHITIS

--------------------------------------------------------------------------------

Employer: E-Cont.:

Phone: Phone:

--------------------------------------------------------------------------------

Ins. Co 1: IB INS. CO, 44 Phone: 555-555-4312

Subsc.: IB,PATIENT 456 Type: MAJOR MEDICAL EXPENS

Subsc. ID: WXXXXXXXX Group: 4446333

--------------------------------------------------------------------------------

Date Diagnosis Procedure Final DRG LOS

\| \| \| \| \|

\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_

\| \| \| \| \|

\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_

\| \| \| \| \|

\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_

Service Connected Conditions: Treated

NONE STATED

I attest that these are the diagnoses and procedures for which the

Patient was treated during this episode of care.

MD: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Patient: IB,PATIENT 456 XX-XX-XXXX Printed: XXX XX, XXXX@13:18

- 
- Pending Work Report

You can print a Pending Work List similar to the Pending Reviews option.

The report can be sorted by the following:

- Assigned to
- Due Date,
- Patient,
- Type of Review
- Current Ward

You can print the report for either Insurance Reviews, Hospital Reviews, or both. A plus sign (+) before the patient's name indicates there is both a hospital and insurance review on the list for that patient.

This report is formatted to print 132 columns.

Sample Report

Pending Reviews Report for Division SITENAME Page 1 Feb 11, 1994@09:44:52

For Period Feb 01, 1994 to Feb 11, 1994

Patient Pt. ID Ward Review Type Due Date Status Assigned to Visit Date

---------------------------------------------------------------------------------------------------------------------------

+IB,PATIENT 22 XXXX 8C ORTHO SU Hosp Review-Admission XX/XX/XX ENTERED UR,NURSE ADMIT 02/07/94 2:42 pm

IB,PATIENT 22 XXXX 2B ICU Hosp Review-Admission XX/XX/XX ENTERED Unassigned ADMIT 02/01/94 2:01 am

IB,PATIENT 22 XXXX 11-B MEDICI Hosp Review-CONT. STAY XX/XX/XX ENTERED UR,NURSE ADMIT 01/13/94 9:30 am

IB,PATIENT 22 XXXX 2D ICU Ins. Review-URG ADM XX/XX/XX ENTERED Unassigned ADMIT 02/01/94 2:01 am

IB,PATIENT 22 XXXX 11-B MEDICI Ins. Review-URG ADM XX/XX/XX COMPLETE UR,NURSE ADMIT 01/13/94 9:30 am

+IB,PATIENT 22 XXXX 8C ORTHO SU Hosp Review-Admission XX/XX/XX ENTERED UR,NURSE ADMIT 02/07/94 2:42 pm

  
Unscheduled Admissions w/Insurance

You can print a list of patients who had active insurance on the date of their unscheduled admission. The report prints information about the number of reviews completed and the insurance companies’ actions.

This report is formatted to print 132 columns.

Sample Report

Unscheduled Admissions with Insurance Page 1 Feb 11, 1994@10:05:06

For Period beginning on 02/01/94 to 02/11/94

Patient Pt. ID Adm. Date Billable Ward Type

--------------------------------------------------------------------------------------------------------------

IB,PATIENT 22 XX-XX-XXXX XX/XX/XX 5:07 pm YES 9D MED

IB,PATIENT 221 XX-XX-XXXX XX/XX/XX 11:00 am YES 13B PSYCH

IB,PATIENT 3 XX-XX-XXXX XX/XX/XX 2:42 pm YES 8C ORTHO SUR URGENT

IB,PATIENT 66 XX-XX-XXXX XX/XX/XX 11:38 a YES 2D ICU URGENT

IB,PATIENT 987 XX-XX-XXXX XX/XX/XX 2:01 am YES 5D SURGICAL URGENT

------------------

TOTAL = 5

- UR Activity Report

The UR Activity Report includes the total activity during a date range. It provides a detailed listing of the following:

- Insurance Reviews
- Hospital Reviews
- Both
- Summary Report by Admission
- Summary Report by Specialty

All completed Insurance Reviews are included. For Hospital Reviews, it lists each case reviewed indicating whether it met admission criteria and the number of days that met/did not meet the criteria for acute care.

The detailed report can be sorted by the following:

- Reviewer
- Specialty
- Patient

When the report is sorted by reviewer, it sorts within reviewer by type of review.

This report is formatted to print 132 columns.

Sample Report

UR Insurance Review Activity Report Page 1 Feb 15, 1994@10:17:10

For Insurance Reviews Dated 01/01/94 to 02/15/94

Dates of Review

Patient Pt. ID Care Review Type Date Ins. Co. Action Last Reviewer

-----------------------------------------------------------------------------------------------------------------

IB,PATIENT 22 XX-XX-XXXX XX/XX/XX URG ADM 02/07/94 ABC INS APPROVED UR,NURSE

IB,PATIENT 67 XX-XX-XXXX XX/XX/XX to PRE-ADM 01/07/94 CDPHP APPROVED UR,NURSE

XX/XX/XX

IB,PATIENT 456 XX-XX-XXXX XX/XX/XX to URG ADM 02/11/94 BLUE SHIELD APPROVED UR,NURSE

XX/XX/XX

UR ACTIVITY SUMMARY REPORT

for Insurance Reviews

SITENAME (001)

From: JAN 1, 1994

To: FEB 15, 1994

Date Printed: Feb 15, 1994@10:17:10

Page: 2

--------------------------

Total Admissions: 15

Total Admissions to NHCU: 4

Total Admissions to Domiciliary: 1

Total Admissions Requiring Reviews: 0

Number of Scheduled Adm. Reviewed: 0

Total Admissions with Insurance: 4

Total Billable Admissions: 3

Cases with Pre-Cert and Follow-up: 0

Cases with Pre-Cert no Follow-up: 0

Number of Closed Cases: 0

Number of Billable Closed Cases: 0

Number of Unbillable Closed Cases: 0

Number of New Case Still Open: 0

Number of Previous Cases: 0

Number of Previous Cases Closed and Billable: 9

Number of Previous Cases Closed, not Billable: 0

Number of Previous Cases still Open: 0

Number of Outpatient Cases Reviewed: 0

Reason Not Billable Report: Reason Count

--------------------------- ------------------------

NOT INSURED 1

INSURANCE REVIEW SPECIALTY SUMMARY REPORT Feb 15, 1994@10:17:10 Page 3

For Insurance Reviews Dated 01/01/94 to 02/15/94

Days Days Amount Amount

Specialty Approved Denied Approved Denied

------------------------------------------------------------------------------------

GENERAL MEDICINE 0 0 \$0 \$0

MEDICINE 5 10 \$4,135 \$8,270

ORTHOPEDIC SURGERY 0 0 \$0 \$0

UROLOGY 0 1 \$0 \$1,164

Unknown 0 0 \$0 \$0

-------------------------------------------------------------------------------

5 11 \$4,135 \$9,434

UR Hospital Review Activity Report Page 4 Feb 15, 1994@10:17:10

For Hospital Reviews Dated 01/01/94 to 02/15/94

Dates of Admission Days Met Days Not Met

Patient Pt. ID Care Review Type Met Criteria Criteria Criteria Assigned Reviewer

-----------------------------------------------------------------------------------------------------------------------

IBpatient,one 000-11-1111 02/07/94 RANDOM YES 1 0 JOHN

IBpatient, two 000-22-2222 12/23/93 RANDOM YES 1 0 ED

IBpatient, three 000-33-3333 02/01/94 to COPD YES 1 0 STEVE

02/09/94

IBpatient, four 000-44-4444 12/29/93 LOCAL 1 0 SEAN

UR ACTIVITY SUMMARY REPORT

for Hospital Reviews

SITENAME (001)

From: JAN 1, 1994

To: FEB 15, 1994

Date Printed: Feb 15, 1994@10:17:10

Page: 5

--------------------------

Total Admissions: 15

Total Cases Reviewed: 14

Number of New Case Still Open: 0

Number of Previous Cases: 3

Number of Previous Cases still Open: 0

Total Random Sample Cases: 12

Total Special Condition Cases: 1

COPD: 1

CVD: 0

TURP: 0

Total Locally Added Cases: 1

Total Cases Meeting Criteria on Adm.: 13

Total Cases Not Meeting Crit. on Adm.: 1

Total Days Reviewed: 20

Total Days Meeting Criteria: 14

Total Days Not Meeting Criteria: 6

HOSPITAL REVIEW SPECIALTY SUMMARY REPORT Feb 15, 1994@10:17:10 Page 6

For Hospital Reviews Dated 01/01/94 to 02/15/94

Admissions Admissions Days Days

Specialty Met Criteria Not Met Crit. Met Criteria Not Met Crit.

------------------------------------------------------------------------------------

GENERAL MEDICINE 5 0 0 5

MEDICINE 1 0 2 1

NEUROLOGY 0 0 1 0

ORTHOPEDIC SURGERY 3 0 0 3

PSYCHIATRY 1 0 0 1

SURGERY 2 0 1 2

UROLOGY 1 1 2 1

-----------------------------------------------------------------------------

13 1 6 14

## Hospital Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note:* Hospital reviews are no longer done using VistA Claims Tracking. National Utilization Management Integration (NUMI) is a web-based application that supports hospital reviews.

This option is designed to allow the entry of the utilization management information required by the Quality Management office. The Claims Tracking module will automatically identify a random sample of admissions (see the Claim Tracking Parameter Edit option) that require review. Hospital reviews are the application of Interqual criteria to determine if the admission or continued stay meets specific criteria. This module will allow entry of the category of criteria that was met for Severity of Illness and Intensity of Service or the reasons that criteria was not met. An entry for every day being reviewed is required. This can easily be accomplished by using the Add Next Review action which is designed to reduce the data entry time by duplicating the entries for days where the information is identical.

The following screens show the Claims Tracking screens accessed through this option and the actions available on each screen:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Hospital Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Next Hosp.Review</td>
<td><em><strong>VE View/Edit Review</strong></em></td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>DR Delete Review</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td>QE Quick Edit</td>
<td>PU Procedure Update</td>
<td></td>
</tr>
<tr class="even">
<td>CS Change Status</td>
<td>PV Provider Update</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Hospital Reviews</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AI Add Ins. Review</td>
<td>SC SC Conditions</td>
<td>PV Provider Update</td>
</tr>
<tr class="even">
<td>DR Delete Review</td>
<td>AE Appeals Edit</td>
<td>RW Review Wksheet Print</td>
</tr>
<tr class="odd">
<td>CS Change Status</td>
<td>AC Add Comment</td>
<td>CP Change Patient</td>
</tr>
<tr class="even">
<td>QE Quick Edit</td>
<td>DU Diagnosis Update</td>
<td>EX Exit</td>
</tr>
<tr class="odd">
<td><strong>VE View/Edit Review</strong></td>
<td>PU Procedure Update</td>
<td></td>
</tr>
</tbody>
</table>

### About the Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the top left corner of each screen is the screen title. A plus sign (+) at the bottom left of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right on the screen. Available actions are displayed below the screen. Two question marks entered at any "Select Action" prompt displays all available actions for that screen. For more information on the use of the screens, please refer to the appendix at the end of this manual.

You may quit from any screen, which will bring you back one level or screen, or you may enter the Exit action.

### Common Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are actions common to both screens accessed through this option:

- Change Status - This action allows you to quickly change the status of a review. Only completed reviews are used in the report preparation and by the MCCR NDB roll-up or the QM roll-up (which is tentatively scheduled for release in June, 1994).

Reviews have a status of ENTERED when automatically added. A status of PENDING may be used for those you are still working on or when one person does the data entry and another needs to review it.

- Diagnosis Update - This action allows input of ICD diagnoses for the patient. Whether diagnoses are input on this screen or another screen, they are available across the Claims Tracking module. You may enter an admitting diagnosis, primary (DXLS) diagnosis, secondary diagnosis and the onset date of the diagnosis for this admission. For outpatient visits this information is stored with the outpatient encounter information.
- Procedure Update - This action allows the input of ICD procedures for the patient. You may input the procedure and the date. This is a separate procedure entry from the PTF module and is optional for use.
- Provider Update - This action allows you to input the admitting physician, attending physician, and care provider separate from the MAS information. The purpose is to provide a location to document the attending physician and to provide an alternate place to document individual physicians if the administrative record indicates teams, or vice versa.

### Hospital Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This following actions are available from the Hospital Reviews screen:

- Add Next Hosp. Review - This action allows you to add the next review and automatically set it to either an admission review or continued stay review. The day for review and review date are automatically computed but can be edited. The category of severity of illness and intensity of service that was met can be entered; or if not met, the reason it was not met.
- Delete Review - This action allows a hospital review to be deleted. If a review is automatically created, but the visit does not require reviews and follow-up with the insurance company, it can be deleted. Use care in exercising this action. It can be as important to document that no review is required as it is to document the required reviews.
- Quick Edit - This action allows you to quickly edit all information about the review without leaving the Pending Review option.
- View/Edit Review - This action allows you to access to the Expanded Hospital Reviews Screen.
- Change Patient - This action allows you to change the selected patient without leaving the option.

Sample Screen

Hospital Reviews Feb 03, 1994 13:49:45 Page: 1 of 1

Hospital Review Entries for: IB,PATIENT 77 XXX ROI: OBTAINED

for: INPATIENT ADMISSION on 01/13/94 9:30 am

Review Date Type Ward Status Specialty Day Next Review

1 01/15/94 CONT. STA 11-B ME COMPLETE MEDICINE 3 01/17/94

2 01/14/94 CONT. STA 11-B ME COMPLETE MEDICINE 2

3 01/13/94 Admission 11-B ME COMPLETE MEDICINE 1

Random Sample \>\>\>

*AN Add Next Hosp. ReviewVE View/Edit ReviewCP Change PatientDR Delete Review* DU Diagnosis Update EX Exit

*QE Quick Edit* PU Procedure Update

CS Change Status PV Provider Update

Select Action: Quit//

### Expanded Hospital Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Expanded Hospital Reviews screen:

- Review Information - This action allows you to enter/edit the type of review (admission or continued stay), review date, and the specialty and methodology for the review. There should be only one admission review (pre-certification or urgent/ emergent admission review) for an admission. Normally, reviews are done for UR purposes on days 3, 6, 9, 14, 21, 28, and every 7 days thereafter. (Usually, the INTERQUAL method is used as the methodology for UR required review. Insurance carriers may require other review methodologies.)
- Add Comment - This action allows you to edit the word processing (comments) field in Hospital or Insurance Reviews without having to edit other fields.
- Criteria Update - This action allows you to enter or edit data regarding criteria met/not met for an acute admission within 24 hours, such as the review date and methodology; severity of illness and intensity of service; and whether additional reviews are required.

Sample Screens

Expanded Hospital Reviews Feb 03, 1994 13:55:38 Page: 1 of 3

Expanded Review for: IB,PATIENT 77 XXXX ROI:OBTAINED

for: CONTINUED STAY REVIEW on 01/15/94

Visit Information Review Information

Visit Type: INPATIENT ADMISSION Review Type: CONTINUED STAY REVI

Admission Date: XXX XX,XXXX@09:30:35 Review Date: XX/XX/XX

Ward: 11-B MEDICINE XREF Specialty: MEDICINE

Specialty: MEDICINE Methodology: INTERQUAL

Ins. Action:

Criteria Information

Day of Review: 3

Severity of Ill: CARDIOVASCULAR

Intensity of Svc: CARDIOVASCULAR

Apply all Days:

Non-Acute Reason:

No. Acute Days:

Non-Acute Days:

\+ Enter ?? for more actions

RI Review Information CU Criteria Update PV Provider Update

CS Change Status DU Diagnosis Update EX Exit

AC Add Comments PU Procedure Update

Select Action: Quit// Next Page

Expanded Hospital Reviews Feb 03, 1994 13:58:13 Page: 2 of 3

Expanded Review for: IB,PATIENT 77 XXXX ROI:OBTAINED

for: CONTINUED STAY REVIEW on 01/15/94

\+

Status Information Clinical Information

Review Status: ENTERED Provider: IBprovider,one

Entered by: UR,NURSE 3 Admitting Diag: 101.0 - VINCENTS ANG

Entered on: XX/XX/XX 2:51 pm Primary Diag:

Completed by: UR,NURSE 3 1st Procedure: 89.44 - CARDIAC STRE

Completed on: XX/XX/XX 2:53 pm 2nd Procedure:

Next Review Date: XX/XX/XX Interim DRG: 0 - on

Estimate ALOS: 0.0

Days Remaining: 0.0

Review Comments

Patient not doing well, consult to psych is recommended.

\+ Enter ?? for more actions

RI Review Information CU Criteria Update PV Provider Update

CS Change Status DU Diagnosis Update EX Exit

AC Add Comments PU Procedure Update

Select Action: Quit// Next Page

Expanded Hospital Reviews Feb 03, 1994 14:09:46 Page: 3 of 3

Expanded Review for: IBpatient,one 1111 ROI:OBTAINED

for: CONTINUED STAY REVIEW on 01/15/94

\+

Visit Information Review Information

Visit Type: INPATIENT ADMISSION Review Type: CONTINUED STAY REVI

Admission Date: XXX XX,XXXX@09:30:35 Review Date: XX/XX/XX

Ward: 11-B MEDICINE XREF Specialty: MEDICINE

Specialty: MEDICINE Methodology: INTERQUAL

Ins. Action:

Criteria Information

Day of Review: 3

Severity of Ill: CARDIOVASCULAR

Intensity of Svc: CARDIOVASCULAR

Apply all Days:

Non-Acute Reason:

No. Acute Days:

\+ Enter ?? for more actions

RI Review Information CU Criteria Update PV Provider Update

CS Change Status DU Diagnosis Update EX Exit

AC Add Comments PU Procedure Update

Select Action: Quit//

# Claims Tracking Menu for Billing ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Claims Tracking menu is intended for Billing personnel. Billing personnel sometimes need to obtain Claims Tracking data for the preparation of third-party bills. You may also need to update Claims Tracking if you determine, for example, that an event is not billable though this capability has also been added to IB.

Sample Menu

CT Claims Tracking Edit

PS Print CT Summary for Billing

RN Assign Reason Not Billable

TP Third Party Joint Inquiry

Select Claims Tracking Menu for Billing \<TEST ACCOUNT\> Option:

## Claims Tracking Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to enter a patient’s name and then view all of the patient’s current Claims Tracking events.

The following screens show the actions accessed through this option and the actions available on each subsequent screen:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Claims Tracking Editor</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BI Billing Info Edit</td>
<td>CP Change Patient</td>
<td>EX Exit</td>
</tr>
<tr class="even">
<td><em><strong>VE View/Edit Episode</strong></em></td>
<td>CD Change Date Range</td>
<td></td>
</tr>
<tr class="odd">
<td>SC SC Conditions</td>
<td>VP View Pat. Ins.</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>Expanded Claims Tracking Entry</p>
<p>--------------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BI Billing Info Edit</td>
<td>TA Treatment Auth.</td>
<td>EX Exit</td>
</tr>
<tr class="even">
<td>RI Review Info</td>
<td>SE Submit Claim to ECME</td>
<td></td>
</tr>
</tbody>
</table>

1.  <span id="_Toc514255738" class="anchor"></span>About the Screens

In the top left corner of each screen is the screen title. A plus sign (+) at the bottom left of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right on the screen. Available actions are displayed below the screen. Two question marks entered at any "Select Action" prompt displays all available actions for that screen. For more information on the use of the screens, please refer to the appendix at the end of this manual.

You may quit from any screen, which will bring you back one level or screen, or you may enter the Exit action.

2.  <span id="_Toc514255739" class="anchor"></span>Common Actions

The following are actions common to both screens accessed through this option:

- Billing Info Edit – This action allows you to enter the reason for which an event is determined to be unbillable. You will also need to enter a comment if you enter a reason equal to Other.

### Claims Tracking Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the Claims Tracking Editor screen:

- View/Edit Episode – This action allows you to jump to the Expanded Claims Tracking Entry screen.
- SC Conditions – This action allows you to see what, if any, service connected conditions are recorded for the patient.
- Change Patient – This action allows you to change the selected patient without having to leave and reenter the option.
- Change Date Range – This action allows you to change the date range of events without having to leave and reenter the option.
- View Pat. Ins. – This action takes you to the Patient Insurance Screens. Note: From this instance of the Patient Insurance Screen users may not add, edit, or delete Patient Policy Comments. It is in view only mode. For more detailed information on Patient Insurance Menu, refer to the IB V. 2.0 User Manual.

Sample Screen

Claims Tracking Editor Oct 27, 2014@17:16:01 Page: 1 of 1

Claims Tracking Entries for: IB,PATIENT 300 IXXXX

for Visits beginning on: 10/27/13 to 11/10/14

Type Urgent Date Ins. UR ROI Bill Ward

1 \*INPT. NO 07/16/14 1:48 pm YES YES C MEDICI

2 INPT. NO 05/06/14 9:25 am YES NO

3 Sch Adm NO 01/07/14 10:00 a YES YES

4 OPT. NO 01/06/14 4:00 pm YES YES

Service Connected: NO \*=Current Admission \>\>\>

BI Billing Info Edit CP Change Patient EX Exit

VE View/Edit Episode CD Change Date Range

SC SC Conditions VP View Pat. Ins.

Select Action: Quit//

## Print CT Summary for Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can print a Claims Tracking Summary which can be used for preparation of a bill/claim. The content of the summary is based upon the type of Claims Tracking event.

Sample Report

Bill Preparation Report Page 1 Oct 23, 2014@14:53:41

IB,PATIENT 78 XX-XX-XXXX DOB: XXX XX, XXXX

INPATIENT ADMISSION on XXX XX, XXXX@13:22:16

--------------------------------------------------------------------------------

Visit Information

Visit Type: INPATIENT ADMISSION Visit Billable: YES

Admission Date: XXX XX,XXXX@13:22:16 Second Opinion: NOT REQUIRED

Ward: C MEDICINE Auto Bill Date: XXX XX,XXXX

Specialty: MEDICINE Special Consent: ROI NOT DETERMINED

Discharge Date: Special Billing:

------------------------------------------------------------------------

Insurance Information

Ins. Co 1: AETNA US HEALTHCARE Pre-Cert Phone: 800/523-7978

Subsc.: IB,PATIENT 78 Type: COMPREHENSIVE MAJO

Subsc. ID: WXXXXXXXX Group: GRP NUM 8802

Coord Ben: SECONDARY Billing Phone: 800/523-7978

Filing Time Fr: Claims Phone: 800/523-7978

Group Plan Comments:

------------------------------------------------------------------------

Billing Information

Initial Bill: Estimated Recv (Pri): \$

Bill Status: Estimated Recv (Sec): \$

Total Charges: \$ 0 Estimated Recv (ter): \$

Amount Paid: \$ 0 Means Test Charges: \$

------------------------------------------------------------------------

Eligibility Information

Primary Eligibility: NSC, VA PENSION

Means Test Status:

Service Connected Percent: Patient Not Service Connected

------------------------------------------------------------------------

Diagnosis Information

Nothing on File

Associated Interim DRG Information

Nothing on File

------------------------------------------------------------------------

Procedure Information

Nothing on File

------------------------------------------------------------------------

Provider Information

Nothing on File

------------------------------------------------------------------------

Insurance Review Information

Type Review: CONTINUED STAY REVIEW Review Date: XX/XX/XX@1:41 pm

Action: DENIAL Insurance Co.: AETNA US HEALTHCARE

Denied From: XX/XX/XX Person Contacted:

Denied To: XX/XX/XX Contact Method: PHONE

Denial Reasons: FAILURE TO MEET PAYER Call Ref. Number:

Status: PENDING

Last Edited By: UR,NURSE

Comment:

-------------------------------------------------------------------------

Type Review: URGENT/EMERGENT ADMIT Review Date: XX/XX/XX

Action: Insurance Co.: AETNA US HEALTHCARE

Person Contacted:

Contact Method:

Call Ref. Number:

Status: ENTERED

Last Edited By:

Comment:

-------------------------------------------------------------------------

## Assign Reason Not Billable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the ability to enter a patient’s name and the Claims Tracking event which has been determined to be non-billable. This option also provides the ability for you to enter the following data:

- REASON NOT BILLABLE:
- EARLIEST AUTO BILL DATE: OCT 22,2014//
- OTHER TYPE OF BILL: OTHER//
- ESTIMATED INS. PAYMENT (PRI):
- ESTIMATED INS. PAYMENT (SEC):
- ESTIMATED INS. PAYMENT (TER):
- ESTIMATED MT CHARGES:
- ESTIMATED TOTAL CHARGES:
- ADDITIONAL COMMENT:
- Current BILLABLE FINDINGS: \<none existing\>
- Do you wish to Add or Change Findings?

For some Reasons Not Billable such as Other, you must add an additional comment of at least 15 characters. If you remove the default date in the Earliest Auto Bill Date field, the autobiller will not create a claim for this event.

## Third Party Joint Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is shared by all the financial modules within VistA and appears on numerous menus and options of the Claims Tracking, IB, and AR modules. You can use the Third Party Joint Inquiry (TPJI) option to look up a specific claim or all the claims, active and inactive, for a selected patient. You can add comments from within TPJI but the option is designed primarily as a source of information.

*Note:* For more detailed information on TPJI, refer to the IB V. 2.0 User Manual.

This option provides the following types of patient and claim information:

- Bill Charges
- Explanation of Benefits
- Bill Diagnoses
- Bill Procedures
- AR Account Profile
- Comment History
- Insurance Reviews
- Health Summary
- Insurance Company
- Insurance Policy
- Annual Benefits
- Patient Eligibility
- Expanded Benefit Information
- Electronic Claims Management Engine (ECME) - Prescription Claims
- EDI Status – electronic claim data

# Claims Tracking Menu (Hospital Reviews) ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu was intended for those RUR Nurses who did Hospital reviews. Refer to the Claims Tracking Menu (Combined Functions)… menu for details of the following options:

- Pending Reviews
- Claims Tracking Edit
- Hospital Reviews
- Inquire to Claims Tracking
- Reports Menu (Claims Tracking) ...
- Supervisors Menu (Claims Tracking) ...
- Single Patient Admission Sheet

*Note:* Hospital reviews are now done using the web-based National Utilization Management Integration (NUMI) system.

# Claims Tracking Menu (Insurance Reviews)…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu was intended for those RUR Nurses who do Insurance reviews. Refer to the Claims Tracking Menu (Combined Functions)… menu for details of the following options:

- Pending Reviews
- Appeal/Denial Edit
- Claims Tracking Edit
- Inquire to Claims Tracking
- Insurance Review Edit
- Reports Menu (Claims Tracking) ...
- Supervisors Menu (Claims Tracking) ...
- Single Patient Admission Sheet
- Third Party Joint Inquiry

## Health Care Services Review (HCSR) 278 Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the above options, the Claims Tracking Menu (Insurance Reviews)… menu contains the Health Care Services Review (HCSR) 278 Response option. You can use this option to view an X12N Health Care Services – Request for Review and Response (278) response from the UMO.

You can enter a patient’s name and the system will display a list of events. You can then select the event response you wish to view.

When an X12N Health Care Services – Request for Review and Response (278) response with a final status is received by VistA, the patient’s entry on the HCSR Worklist is removed. To view the response or to take further action such as submitting an Appeal, you may use the Health Care Services Review (HCSR) 278 Response option or the HCSR Response WL action from within the HCSR Worklist.

The following are final statuses:

- A1 – Certified in total
- A3 – Not Certified
- A6 – Modified
- C – Cancelled
- CT – Contact payer
- NA – No Action Required

Sample 278 Response Screens

HCSR Response View Nov 13, 2014@10:09:54 Page: 1 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

<span class="mark">Insurance Company Information</span>

Name: CIGNA Reimburse?: WILL REIMBURSE

Phone: 800/525-9999 Billing Phone: 800/525-9999

Precert Phone: 800/111-1209

Address: POD 9358, ANYCITY, TX 99999

<span class="mark">Group/Plan Information</span>

Type Of Plan: COMPREHENSIVE MAJOR MEDICAL Require UR: YES

Group?: YES Require Amb Cert:

Group Name: CIGNA Require Pre-Cert: YES

Group Number: WXXXXX Exclude Pre-Cond:

BIN: Benefits Assignable: YES

PCN:

Plan Comments:

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

HCSR Response View Nov 13, 2014@10:10:43 Page: 2 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

\+

<span class="mark">Policy/Subscriber Information</span>

Insured's Name: IB,PATIENT 343 Effective: 1/1/2014

Subscriber Id: 123456789 Expiration:

Relationship: SELF Coord of Benefits: PRIMARY

Insured's DOB: 1/1/1979

Employer Sponsored Group Health Plan?:

<span class="mark">User Added Comments for This Entry</span>

UMO Contact Information

UMO Name:

UMO Contact \#:

UMO Name:

UMO Contact \#:

<span class="mark">PATIENT EVENT DETAIL</span>

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

HCSR Response View Nov 13, 2014@10:11:05 Page: 3 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

\+

Health Care Services Review

*Certification Action: Certified in totalCertification/Authorization Number: XXXXXXXXXXXX*

Review Decision Reason:

Second Surgical Opinion Ind:

Admin Ref \#:

Previous Review Autho \#:

Proposed/Actual Event Date:

Proposed/Actual Admission Date: XXX XX,XXXX@09:00

Proposed or Discharge Date:

*Cert. Effective Date:Cert. Issue Date: Cert. Expiration Date:XXX XX, XXXX*

<span class="mark">Health Care Services Delivery</span>

Quantity Qualifier: Visits Service Unit Count: 1

Unit/Basis for Measure Code: Sample Selection Modulus:

Time Period Qualifier: Period Count:

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

*Note:* Much of the data in the 278 Response is the same data that you include in your 278 Request.

The following important data is in the Health Care Services Review section of the response:

- Certification Action
- Certification/Authorization Number
- Review Decision Reason
- Certification Effective Date
- Certification Issue Date
- Certification Expiration Date

  Note: The certification/authorization number that is received in the response will be automatically added to a third-party bill (billing screen 10) for the patient event when the billing clerk adds each payer to the claim (billing screen 3). The certification/authorization number(s) will then be transmitted in the X12N Health Care Claim (837) transaction to the payer(s).

HCSR Response View Nov 13, 2014@10:11:31 Page: 4 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

\+

Delivery Frequency:

Delivery Pattern:

<span class="mark">Patient Diagnosis Information</span>

No Diagnosis Information

<span class="mark">Institutional Claim Code</span>

Admission Type Code: Admission Source Code:

Patient Status Code: INPATIENT

Ambulance Transport Information

Ambulance Transport Code: Unit/Basis for Measure Code:

Transport Distance:

<span class="mark">Spinal Manipulation Service Information</span>

No Spinal Manipulation Service Information

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

HCSR Response View Nov 13, 2014@10:12:22 Page: 5 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

\+

<span class="mark">Home Oxygen Therapy Information</span>

No Home Oxygen Therapy Information

<span class="mark">Home Health Care Information</span>

Prognosis Code: Home Health Start Date:

Home Health Certification Period: Start: End:

Medicare Coverage Indicator:

Certification Type Code: Initial

<span class="mark">Additional Patient Information</span>

No Additional Patient Information

Message Text:

XXXXXXX XX XXX XXXXXXX XXX XXXXXXXX XXX XXXXXX X XXXXXXXXXX XXXXXXXX XXXX.

<span class="mark">Additional Patient Information Contact Data</span>

No Additional Patient Information Contact Data

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

HCSR Response View Nov 13, 2014@10:13:18 Page: 6 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

\+

<span class="mark">Additional Patient Information Contact</span>

Response Contact Name:

Response Contact \#:

<span class="mark">Patient Event Provider Information</span>

Entity Provider Code: 24

Provider ID: XXXXXXXXXX Provider Taxonomy: Person

Provider Name: IB,DOCTOR 32

Provider Address: 123 TEST LN

ANYSITE, WY 11111

<span class="mark">Patient Event Transport Information</span>

No Patient Event Transport Information

<span class="mark">SERVICE DETAIL</span>

No Service Detail Lines available

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

## Health Care Services Review (HCSR) Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The X12N Health Care Services Review – Request for Review and Response transaction is an Electronic Data Interchange (EDI) standard for the transmission of standardized data for the request of care authorizations or certifications and for the responses to those requests. The messages from VistA to the Financial Services Center (FSC) in Austin, TX are Health Level Seven (HL7) messages. The HL7 messages received by FSC are converted to a HIPAA compliant format and sent to a Health Care Clearing House (HCCH). The HCCH then sends the transaction to the payer or the payer’s Utilization Management Organization. The UMO returns either a Pending notification to the VAMC or a response containing the authorization/certification number or denial of services or error condition. The 278 transactions from VistA are real-time transactions and are transmitted as soon as you trigger a request.

Refer to the eBilling_Build 2 ICD for details of the message structures.

### The HCSR Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can select either only CHAMPVA/TRICARE if you are at a site and responsible for UR for these payers, only CPAC if you are not responsible for CHAMPVA and TRICARE and Both if you are responsible for all types of authorizations and certifications.

Sample HCSR Worklist Screens

Select Claims Tracking Menu (Insurance Reviews) \<TEST ACCOUNT\> Option: hw

Health Care Services Review (HCSR) Worklist

Select one of the following:

T CHAMPVA/TRICARE

C CPAC

B Both

Show CHAMPVA/TRICARE entries, CPAC entries or Both: B//oth

You can select either Outpatient, Inpatient or Both types of events to be included on your worklist.

If you select Inpatient or Both, you are prompted for one or more wards.

*Note:* If you leave the ward prompt blank, you will get all wards.

If you select Outpatient or Both, you are prompted for one or more clinics.

*Note:* If you leave the Clinic prompt blank, you will get all clinics.

The screen then displays all of your choices.

You are then able to select how you want you worklist displayed (sorted).

Select one of the following:

O Outpatient

I Inpatient

B Both

Show Inpatient entries, Outpatient entries or Both: B//oth

Select Ward: C SURGERY

Select Another Ward:

Select Clinic: TEST

Select Another Clinic: TEST 1

Select Another Clinic: TEST 2

Select Another Clinic:

Show CHAMPVA/TRICARE entries, CPAC entries or Both: B

Show Inpatient entries, Outpatient entries or Both: B

Clinics to Display: TEST, TEST 1, TEST 2

Wards to Display: C SURGERY

Enter RETURN to continue or '^' to exit:

Select one of the following:

1 Oldest Entries First

2 Newest Entries First

3 Outpatient Appointments First

4 Inpatient Admissions First

5 Insurance Company Name

Sort the list by: Oldest Entries First//

The worklist is displayed.

Sample HCSR Worklist

HCSR Worklist Oct 29, 2014@15:03:41 Page: 1 of 3

Filtered By: Both CPAC and Champ/TRICARE, Selected Outpt, Selected Inpt

Sorted By: Oldest Entries First

Patient Name S Apt Date Ward/Clnc COB Insurance Comp U/P SC Re

1 \*IB,PATIENT 2 XXXX O 08/29/14 TEST P AETNA US HEALT Y Y

2 ?IB,PATIENT 2 XXXX O 08/29/14 TEST S NEW YORK LIFE

3 \*IB,PATIENT 37 XXXX O 09/02/14 TEST P CIGNA Y Y

4 \*IB,PATIENT 6 XXXX O 09/15/14 TEST P BCBS SERVICE B

5 ?IB,PATIENT 37 XXXX O 09/15/14 TEST P CIGNA HEALTHCA Y

6 ?IB,PATIENT 37 XXXX O 09/15/14 TEST S CHAMPVA

7 ?IB,PATIENT 44 XXXX O 09/18/14 TEST 2 S AETNA US HEALT Y Y

8 ?IB,PATIENT 44 XXXX O 10/07/14 TEST P AETNA N A

9 IB,PATIENT 2 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE

10 ?IB,PATIENT 777 XXXX O 10/09/14 TEST 2 P BLUE CROSS/BS N N

11 ?IB,PATIENT 2 XXXX O 10/14/14 TEST 1 P AETNA US HEALT Y Y

12 IB,PATIENT 2 XXXX O 10/14/14 TEST 1 S NEW YORK LIFE

13 IB,PATIENT 98 XXXX I 10/16/14 C SURGERY P CIGNA

14 \#IB,PATIENT 37 XXXX I 10/17/14 C SURGERY P BLUE CROSS/BS N N

\+ ?Await \#In-Prog -RespErr !Unable +Pend \*NextRev

DE Remove Entry AC Add Comment SP Set 'In Progress' Mark

EE Expand Entry ST Sort List RP Remove 'In Progress' Mark

AE Add Entry NR Next Review Date PR HCSR Response WL

RL Refresh EX Exit

Select Action: Next Screen//

The following actions are available from the HCSR Worklist:

- Remove Entry - This action allows you to remove an entry from the list.
- Expand Entry – This action allows you to select and expand an entry from the list.
- Add Entry – This actions allows you to add an entry to the list
- Next Review Date – This action allows you to delay a review until a specified future date or until an inpatient is discharged. Next Review Date is for inpatient entries only.
- Add Comment – This action allows you to enter a free text comment. The comments can be viewed in Expanded Entry. The user’s name and the date and time are added to the comment automatically.
- Sort List – This action allows you to resort the worklist based on the following:
- Oldest Entries First
- Newest Entries First
- Outpatient Appointments First
- Inpatient Admissions First
- Insurance Company Name
- HCSR Response WL – This action allows you to view a list of entries with final 278 Responses.

*Note:* When an X12N Health Care Services – Request for Review and Response (278) response with a final status is received by VistA, the patient’s entry on the HCSR Worklist is removed. To view the response or to take further action such as submitting an Appeal, you may use the either the stand-alone Health Care Services Review (HCSR) 278 Response option or this HCSR Response WL action.

The following are final statuses:

- A1 – Certified in total
- A3 – Not Certified
- A6 – Modified
- C – Cancelled
- CT – Contact payer
- NA – No Action Required
- Set ‘In Progress’ Mark – This action allows you to mark an entry as being worked by you. The software places a pound sign (#) before the patient’s name.

  *Note:* If you start a 278 request and need to stop for some reason before you are done, the data you have entered will be saved and the entry will be automatically marked ‘In Progress’.
- Remove “In Progress’ Mark – This action allows you to remove the ‘In Progress’ indicator.
- Refresh – this action allows you to rebuild the worklist without leaving the option.

The HCSR Worklist provides an on screen legend which provides the following information:

?Await \#In-Prog -RespErr !Unable +Pend \*NextRev

- ?Await – This indicator means that a 278 Request has been transmitted and a response has not yet been received.
- \#In-Prog – This indicator means someone is working on this entry.
- -RespErr – This indicator means a 278 Request was sent and a 278 Response has been received which contains an error condition.
- !Unable – This indicator means VistA was unable to send a 278 Request for some reason (example: missing required data).
- +Pend - This indicator means a 278 Request was sent and a PENDING 278 Response has been received.
- \*NextRev - This indicator means the entry on the worklist has been delayed either until a specific date or until the patient’s discharge date.

  
Sample Next Review Date Screen

HCSR Worklist Oct 30, 2014@14:00:08 Page: 1 of 3

Filtered By: Both CPAC and CHAMPVA/TRICARE, Selected Outpt, Selected Inpt

Sorted By: Oldest Entries First

Patient Name S Apt Date Ward/Clnc COB Insurance Comp U/P SC Re

1 \*IB,PATIENT 2 XXXX O 08/29/14 TEST P AETNA US HEALT Y Y

2 ?IB,PATIENT 2 XXXX O 08/29/14 TEST S NEW YORK LIFE

3 \*IB,PATIENT 37 XXXX O 09/02/14 TEST P CIGNA Y Y

4 \*IB,PATIENT 6 XXXX O 09/15/14 TEST P BCBS SERVICE B

5 ?IB,PATIENT 37 XXXX O 09/15/14 TEST P CIGNA HEALTHCA Y

6 ?IB,PATIENT 37 XXXX O 09/15/14 TEST S CHAMPVA

7 ?IB,PATIENT 44 XXXX O 09/18/14 TEST 2 S AETNA US HEALT Y Y

8 ?IB,PATIENT 44 XXXX O 10/07/14 TEST P AETNA N A

9 IB,PATIENT 2 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE

10 ?IB,PATIENT 777 XXXX O 10/09/14 TEST 2 P BLUE CROSS/BS N N

11 ?IB,PATIENT 2 XXXX O 10/14/14 TEST 1 P AETNA US HEALT Y Y

12 IB,PATIENT 2 XXXX O 10/14/14 TEST 1 S NEW YORK LIFE

13 IB,PATIENT 98 XXXX I 10/16/14 C SURGERY P CIGNA

14 \#IB,PATIENT 37 XXXX I 10/17/14 C SURGERY P BLUE CROSS/BS N N

\+ ?Await \#In-Prog -RespErr !Unable +Pend \*NextRev

DE Remove Entry AC Add Comment SP Set 'In Progress' Mark

EE Expand Entry ST Sort List RP Remove 'In Progress' Mark

AE Add Entry *NR Next Review Date* PR HCSR Response WL

RL Refresh EX Exit

Select Action: Next Screen// NR Next Review Date

Select Event Entry(s): (1-14): 2

Enter 'D' or Future Date for Entry 2: ??

Entry a future date or 'D' to delay until discharge. A 'D' will remove the

selected entries from the worklist until the patients have been discharged.

Entering a Date will remove the selected entries from the worklist until the

selected date.

Enter 'D' or Future Date for Entry 2: D

Sample Add Comment Screen

HCSR Worklist Oct 30, 2014@14:04:13 Page: 1 of 3

Filtered By: Both CPAC and CHAMPVA/TRICARE, Selected Outpt, Selected Inpt

Sorted By: Oldest Entries First

Patient Name S Apt Date Ward/Clnc COB Insurance Comp U/P SC Re

1 \*IB,PATIENT 2 XXXX O 08/29/14 TEST P AETNA US HEALT Y Y

2 ?IB,PATIENT 2 XXXX O 08/29/14 TEST S NEW YORK LIFE

3 \*IB,PATIENT 37 XXXX O 09/02/14 TEST P CIGNA Y Y

4 \*IB,PATIENT 6 XXXX O 09/15/14 TEST P BCBS SERVICE B

5 ?IB,PATIENT 37 XXXX O 09/15/14 TEST P CIGNA HEALTHCA Y

6 ?IB,PATIENT 37 XXXX O 09/15/14 TEST S CHAMPVA

7 ?IB,PATIENT 44 XXXX O 09/18/14 TEST 2 S AETNA US HEALT Y Y

8 ?IB,PATIENT 44 XXXX O 10/07/14 TEST P AETNA N A

9 IB,PATIENT 2 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE

10 ?IB,PATIENT 777 XXXX O 10/09/14 TEST 2 P BLUE CROSS/BS N N

11 ?IB,PATIENT 2 XXXX O 10/14/14 TEST 1 P AETNA US HEALT Y Y

12 IB,PATIENT 2 XXXX O 10/14/14 TEST 1 S NEW YORK LIFE

13 IB,PATIENT 98 XXXX I 10/16/14 C SURGERY P CIGNA

14 \#IB,PATIENT 37 XXXX I 10/17/14 C SURGERY P BLUE CROSS/BS N N + ?Await \#In-Prog -RespErr !Unable +Pend \*NextRev

DE Remove Entry *AC Add Comment* SP Set 'In Progress' Mark

EE Expand Entry ST Sort List RP Remove 'In Progress' Mark

AE Add Entry NR Next Review Date PR HCSR Response WL

RL Refresh EX Exit

Select Action: Next Screen// AC Add Comment

Select Event Entry(s): (1-14): 1

COMMENT:

No existing text

Edit? NO// y YES

==\[ WRAP \]==\[ INSERT \]===============\< COMMENT \>=============\[ \<PF1\>H=Help \]====

This is a test comment for an entry on the HCSR WL.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Sample HCSR Response WL

HCSR Response Worklist Nov 17, 2014@16:08:46 Page: 1 of 2

Filtered By: Both CPAC and CHAMPVA/TRICARE, All Outpt, All Inpt

Sorted By: Oldest Entries First

Patient Name S Apt Date Ward/Clnc COB Insurance Comp CertAct

1 IB,PATIENT 2 XXXX I 08/27/14 C MEDICINE S NEW YORK LIFE A2

2 IB,PATIENT 56 XXXX I 09/15/14 O&E SURGIC P CIGNA A1

3 IB,PATIENT 203 XXXX O 09/15/14 TEST P CIGNA HEALTHCA A1

4 IB,PATIENT 66 XXXX O 09/22/14 C MEDICINE S BLUE CROSS/BS A1

5 IB,PATIENT 543 XXXX O 10/02/14 TESTIB S BLUE CROSS CA A3

6 IB,PATIENT 11 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE A3

7 IB,PATIENT 92 XXXX O 10/22/14 TEST S BLUE CROSS/BS A1

8 IB,PATIENT 123 XXXX O 10/30/14 TEST P AETNA C

9 IB,PATIENT 6 XXXX O 10/30/14 TEST 1 S AETNA HEALTH P A3

10 IB,PATIENT 44 XXXX O 10/30/14 TEST 1 S AETNA HEALTH P NA

11 IB,PATIENT 129 XXXX O 10/31/14 TEST P AETNA GROUP IN C

12 IB,PATIENT 377 XXXX I 11/01/14 O&E MEDICA P CIGNA A1

13 IB,PATIENT 10 XXXX O 11/03/14 TEST P AETNA A1

14 IB,PATIENT 76 XXXX O 11/04/14 TEST 2 P AETNA GROUP IN C

15 IB,PATIENT 3 XXXX O 11/10/14 TEST 1 P AETNA US HEALT A1

\+ Enter ?? for more actions

DE Remove Entry ST Sort RP Remove 'In Progress'

EE Expand Entry RL Refresh EX Exit

NR Next Review Date SP Set 'In Progress'

Select Action: Next Screen//

When you expand an entry from this list, a screen is displayed that looks the same as the stand-alone Health Care Services Review (HCSR) 278 Response option.

HCSR Response View Nov 13, 2014@10:09:54 Page: 1 of 7

IB,PATIENT 343 XX-XX-XXXX DOB: XXX X,XXXX AGE: XX

<span class="mark">Insurance Company Information</span>

Name: CIGNA Reimburse?: WILL REIMBURSE

Phone: 800/525-9999 Billing Phone: 800/525-9999

Precert Phone: 800/111-1209

Address: POD 9358, ANYCITY, TX 99999

<span class="mark">Group/Plan Information</span>

Type Of Plan: COMPREHENSIVE MAJOR MEDICAL Require UR: YES

Group?: YES Require Amb Cert:

Group Name: CIGNA Require Pre-Cert: YES

Group Number: WXXXXX Exclude Pre-Cond:

BIN: Benefits Assignable: YES

PCN:

Plan Comments:

\+ Enter ?? for more actions

SR (Send 278 Request) RP Remove 'In Progress'

SP Set 'In Progress' VR View Sent Request EX Exit

Select Action: Next Screen//

Sample Set ‘In Progress’ Mark Screen

HCSR Worklist Oct 30, 2014@14:21:51 Page: 2 of 3

Filtered By: Both CPAC and CHAMPVA/TRICARE, Selected Outpt, Selected Inpt

Sorted By: Oldest Entries First

\+ Patient Name S Apt Date Ward/Clnc COB Insurance Comp U/P SC Re

1 \*IB,PATIENT 2 XXXX O 08/29/14 TEST P AETNA US HEALT Y Y

2 ?IB,PATIENT 2 XXXX O 08/29/14 TEST S NEW YORK LIFE

3 \*IB,PATIENT 37 XXXX O 09/02/14 TEST P CIGNA Y Y

4 \*IB,PATIENT 6 XXXX O 09/15/14 TEST P BCBS SERVICE B

5 ?IB,PATIENT 37 XXXX O 09/15/14 TEST P CIGNA HEALTHCA Y

6 ?IB,PATIENT 37 XXXX O 09/15/14 TEST S CHAMPVA

7 ?IB,PATIENT 44 XXXX O 09/18/14 TEST 2 S AETNA US HEALT Y Y

8 ?IB,PATIENT 44 XXXX O 10/07/14 TEST P AETNA N A

9 IB,PATIENT 2 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE

10 ?IB,PATIENT 777 XXXX O 10/09/14 TEST 2 P BLUE CROSS/BS N N

11 ?IB,PATIENT 2 XXXX O 10/14/14 TEST 1 P AETNA US HEALT Y Y

12 \#IB,PATIENT 2 XXXX O 10/14/14 TEST 1 S NEW YORK LIFE

13 IB,PATIENT 98 XXXX I 10/16/14 C SURGERY P CIGNA

14 \#IB,PATIENT 37 XXXX I 10/17/14 C SURGERY P BLUE CROSS/BS N N

\+ ?Await \#In-Prog -RespErr !Unable +Pend \*NextRev DE Remove Entry AC Add Comment *SP Set 'In Progress' Mark*

EE Expand Entry ST Sort List RP Remove 'In Progress' Mark

AE Add Entry NR Next Review Date PR HCSR Response

RL Refresh EX Exit

Select Action: Next Screen// sp Set 'In Progress' Mark

Select Event Entry(s): (15-28): 13

Sample Remove ‘In Progress” Mark Screen

HCSR Worklist Oct 30, 2014@14:47:22 Page: 2 of 3

Filtered By: Both CPAC and CHAMPVA/TRICARE, Selected Outpt, Selected Inpt

Sorted By: Newest Entries First

\+ Patient Name S Apt Date Ward/Clnc COB Insurance Comp U/P SC Re

1 \*IB,PATIENT 2 XXXX O 08/29/14 TEST P AETNA US HEALT Y Y

2 ?IB,PATIENT 2 XXXX O 08/29/14 TEST S NEW YORK LIFE

3 \*IB,PATIENT 37 XXXX O 09/02/14 TEST P CIGNA Y Y

4 \*IB,PATIENT 6 XXXX O 09/15/14 TEST P BCBS SERVICE B

5 ?IB,PATIENT 37 XXXX O 09/15/14 TEST P CIGNA HEALTHCA Y

6 ?IB,PATIENT 37 XXXX O 09/15/14 TEST S CHAMPVA

7 ?IB,PATIENT 44 XXXX O 09/18/14 TEST 2 S AETNA US HEALT Y Y

8 ?IB,PATIENT 44 XXXX O 10/07/14 TEST P AETNA N A

9 IB,PATIENT 2 XXXX O 10/09/14 TEST 1 S NEW YORK LIFE

10 ?IB,PATIENT 777 XXXX O 10/09/14 TEST 2 P BLUE CROSS/BS N N

11 ?IB,PATIENT 2 XXXX O 10/14/14 TEST 1 P AETNA US HEALT Y Y

12 \#IB,PATIENT 2 XXXX O 10/14/14 TEST 1 S NEW YORK LIFE

13 IB,PATIENT 98 XXXX I 10/16/14 C SURGERY P CIGNA

14 \#IB,PATIENT 37 XXXX I 10/17/14 C SURGERY P BLUE CROSS/BS N N

\+ ?Await \#In-Prog -RespErr !Unable +Pend \*NextRev

DE Remove Entry AC Add Comment SP Set 'In Progress' Mark

EE Expand Entry ST Sort List *RP Remove 'In Progress' Mark*

AE Add Entry NR Next Review Date PR HCSR Response WL

RL Refresh EX Exit

Select Action: Next Screen// rp Remove 'In Progress' Mark

Select Event Entry(s): (15-28): 12

### HCSR Expanded Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides you with the ability to view more information related to an entry and to create an initial X12N Health Care Services Review – Request for Review and Response (278 - 217) request to the UMO. It also provides you with the ability to force a follow-up X12N Health Care Services Review – Request for Review and Response (278 - 215) inquiry to the UMO. If a 278 request results in an error condition, you can fix the error and resubmit the request.

*Note:* An initial 278 transaction is referred to as a 278 - 217 transaction. A follow-on 278 inquiry sent in response to a Pending reply to an initial 217 is referred to as a 278 - 215 transaction.

*Note:* If a UMO responds to a X12N Health Care Services Review – Request for Review and Response (278 - 217) request with a Pending response, then the requester must respond with a follow-up X12N Health Care Services Review – Request for Review and Response (278 - 215) inquiry. VistA will automatically create and submit the 215 inquiry based on the number of days set in the following site parameters:

- Inquiry can be Triggered for Appointment: 2//
- Inquiry can be Triggered for Admission: 1//

Sample HCSR Expanded Entry Screens

HCSR Expanded Entry Oct 30, 2014@14:59:32 Page: 1 of 3

IB,PATIENT M XX-XX-XXXX DOB: XX-XX-XXXX AGE: XX

Insurance Company Information

Name: BLUE CROSS CA (65-WY) Reimburse?: WILL REIMBURSE

Phone: Billing Phone: 111/737-7776

Precert Phone:

Address: POD 60007, LOS ANGELES, CA 90060

Group/Plan Information

Type Of Plan: PREFERRED PROVIDER ORGANIZATION (PPO)Require UR:

Group?: YES Require Amb Cert:

Group Name: GRP NAME 10 Require Pre-Cert:

Group Number: GRP NUM 10794 Exclude Pre-Cond:

BIN: Benefits Assignable: YES

PCN:

\+ Enter ?? for more actions

SR (Send 278 Req Full) DP View Pending Resp SP Set 'In Progress'

SS Send 278 Req Brief AC Add Comment RP Remove 'In Progress'

CR (Copy 278 Request) SI Send 278 Inquiry VR View Sent Request

EX Exit

Select Action: Next Screen//

HCSR Expanded Entry Oct 30, 2014@15:05:19 Page: 2 of 3

IB,PATIENT M XX-XX-XXXX DOB: XX-XX-XXXX AGE: XX

\+

Plan Comments:

THIS GROUP NAME "CALPERS" STANDS FOR CALIFORNIA PUBLIC EMPLOYEES'

RETIREMENT SYSTEM.

Policy/Subscriber Information

Insured's Name: IB,PATIENT M Effective: 3/2/2014

Subscriber Id: RXXXXXXX Expiration:

Relationship: SELF Coord of Benefits: SECONDARY

Insured's DOB: X/X/XXXX

Employer Sponsored Group Health Plan?:

User Added Comments for This Entry

User's Name: UR,NURSE 2 Date Comment Entered: 10/30/2014@15:03:38

Comment:

This is a Test comment.

\+ Enter ?? for more actions

SR (Send 278 Req Full) DP View Pending Resp SP Set 'In Progress'

SS Send 278 Req Brief AC Add Comment RP Remove 'In Progress'

CR (Copy 278 Request) SI Send 278 Inquiry VR View Sent Request

EX Exit

Select Action: Next Screen//

HCSR Expanded Entry Oct 30, 2014@15:07:25 Page: 3 of 3

IB,PATIENT M XX-XX-XXXX DOB: XX-XX-XXXX AGE: XX

\+

User's Name: UR,NURSE 2 Date Comment Entered: 10/30/2014@15:04:17

Comment:

This is a follow-up Test comment.

Enter ?? for more actions

SR (Send 278 Req Full) DP View Pending Resp SP Set 'In Progress'

SS Send 278 Req Brief AC Add Comment RP Remove 'In Progress'

CR (Copy 278 Request) SI Send 278 Inquiry VR View Sent Request

EX Exit

Select Action: Quit//

The following actions are available from the HCSR Expanded Entry screen:

- Send 278 Request Full – This action allows you to send an initial X12N Health Care Services Review – Request for Review and Response (278) request to the UMO.

> This action also allows you to edit a 278 request for resubmission when the original results in an error condition.

> Note: This action is currently disabled

- Send 278 Request Brief – This action allows you to send an initial X12N Health Care Services Review – Request for Review and Response (278) request to the UMO by selecting one of the following brief request formats:
- Admission (Initial)
- Appointment (Initial)
- Copy 278 Request – This action allows you to enter the data for a X12N Health Care Services Review – Request for Review and Response (278) request to a primary payer and then to copy that data to a new request for a secondary and/or tertiary payer.

  Note: This action is currently disabled
- View Pending Response – This actions allows you to view a Pending response from the UMO.
- Add Comment - This action allows you to enter a free text comment. The comments can be viewed in Expanded Entry. The user’s name and the date and time are added to the comment automatically.
- Send 278 Inquiry – This action allows you to send a X12N Health Care Services Review – Inquiry and Response for a 278 request or inquiry with a Pending status. It also allows you to send a X12N Health Care Services Review – Inquiry and Response to cancel a 278 request or inquiry with a Pending status.
- Set ‘In Progress’ Mark – This action allows you to mark an entry as being worked by you. The software places a pound sign (#) before the patient’s name.
- Remove “In Progress’ Mark – This action allows you to remove the ‘In Progress’ indicator.
- View Sent Request – This action allows you to view the request or inquiry that was sent to payer in X12 format

Sample Send 278 Request Screens – Outpatient Brief

HCSR 278 Appointment - Brief Nov 04, 2014@15:29:07 Page: 1 of 5

IB,PATIENT 543 XX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

<span class="mark">UM Organization</span> <span class="mark">Requester</span>

Name\*: Aetna Name\*: ANYSITE VAMC

National Payer ID\*: XXXXXXXXXX NPI\*: XXXXXXXXXX

HPID: XXXXXX Tax ID\*: XXXXXXXXXX

Taxonomy Code: XXXXXXXXXX

<span class="mark">Subscriber</span> Address\*: 1234 Test Blvd

Name\*: IB,SPOUSE City: ANYSITE

Primary ID\*: WXXXXXXXXXX State/ZIP\*: WY 82005

Address:123 TEST BLVD Contact Name\*: UR,NURSE 34

City/State/ZIP: FORT COLLINS WY 82007 Contact Phone/Ext.:

Contact Fax:

\+ Enter ?? for more actions

SR Send 278 Request AD Add Data EX Exit

Select Action: Next Screen//

HCSR 278 Appointment - Brief Nov 04, 2014@15:29:07 Page: 2 of 5

IB,PATIENT 543 XX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

<span class="mark">Dependent</span> <span class="mark">Diagnosis</span>

Name: IB,PATIENT 543 Diagnosis Qualifier:

Diagnosis:

<span class="mark">Health Care Service Review</span> <span class="mark">Provider Information</span>

Category\*: Health Services Review Provider Type:

Certification Type\*: Initial Provider Name:

Service Type\*: Medical Provider NPI:

Facility Type\*: ON CAMPUS-OUTPATIENT HOSPITAL

\+ Enter ?? for more actions

SR Send 278 Request AD Add Data EX Exit

Select Action: Next Screen//

HCSR 278 Appointment - Brief Nov 04, 2014@15:29:07 Page: 3 of 5

IB,PATIENT 543 XX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

<span class="mark">Service Line</span> <span class="mark">Paperwork Attachments</span>

Service Line \#: Report Type:

Date of Service: Appointment Date Transmission Method:

Procedure Code\*: Attachment Control Number:

<span class="mark">Request Comments</span>

Message:

\+ Enter ?? for more actions

SR Send 278 Request AD Add Data EX Exit

Select Action: Next Screen//AD Add data

PATIENT EVENT DETAIL

Patient Event Service Type: Medical Care// 1 Medical Care

Diagnosis Qualifier: ABF ICD-10 Diagnosis

Patient Event Diagnosis: M25.539

Searching for a ICD-10 Diagnosis

One match found

M25.539 Pain in unspecified wrist

OK? Yes// YES M25.539 Pain in unspecified wrist

The following Diagnoses are currently on file.

\# Type Diagnosis

-- ----- ---------

1 ABF M25.539

Enter the \# of a Diagnosis to edit, 'NEW' to add one or press Return to skip.

Selection \#:

Product or Service ID Qualifier: HC// CPT/HCPCS Code

Procedure: 73100

Searching for a HCPCS (CPT) Procedure Codes

73100 X-RAY EXAM OF WRIST

...OK? Yes// (Yes)

The following Service Lines are currently on file.

\# Proc Code

-- --------------------

1 73100

Enter the \# of a line to edit, 'NEW' to add one or press Return to skip.

Selection \#:

Patient Event Provider Data

Provider Type: DK Ordering Physician

Provider: IB,DOCTOR R

Searching for a VA providers

IB,DOCTOR R VMS 111 PHYSICIAN

...OK? Yes// (Yes)

The following Provider Data Information is currently on file.

\# Provider Type Provider

-- ------------------------------ ------------------------------

1 Ordering Physician IB,DOCTOR R

Enter the \# of an entry to edit, 'NEW' to add one or press Return to skip.

Selection \#:

No Additional Patient Information is currently on file.

Add Additional Patient Information? NO// YES

Report Type: RADIOLOGY REPORTS RR Radiology reports

Report Transmission: AVAI Available on request at provider site

Attachment Control \#:

The following Additional Patient Information is currently on file.

\# Report Type Delivery Method Attachment Control \#

-- ---------------------------- --------------------- ----------------------

1 Radiology reports Available on request

Enter the \# of an entry to edit, 'NEW' to add one or press Return to skip.

Selection \#:

Message Text:

1\>

Requester Contact Name: UR,STAFF 1//

Type of Requester Contact Number \#1: TE// Telephone

Requester Contact Number \#1: 1112223333

Type of Requester Contact Number \#2: FX Facsimile

Requester Contact Number \#2: 444555666

Type of Requester Contact Number \#3:

HCSR 278 Appointment - Brief Nov 04, 2014@15:29:07 Page: 4 of 5

IB,PATIENT 543 XX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

<span class="mark">Dependent</span> <span class="mark">Diagnoses</span>

Name: IB,PATIENT 543 Diagnosis Qualifier: ICD-10 Diag

Diagnosis: M25.539

<span class="mark">Health Care Service Review</span> <span class="mark">Provider Information</span>

Category\*: Health Services Review Provider Type:Ordering Physician

Certification Type\*: Initial Provider Name: IB,DOCTOR R

Service Type\*: Diagnostic X-Ray NPI: XXXXXXXXXX

Facility Type\*: ON CAMPUS-OUTPATIENT HOSPITAL

\+ Enter ?? for more actions

SR Send 278 Request AD Add Data EX Exit

Select Action: Next Screen//

HCSR 278 Appointment - Brief Nov 04, 2014@15:29:07 Page: 5 of 5

IB,PATIENT 543 XX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

<span class="mark">Service Line</span> <span class="mark">Paperwork Attachments</span>

Service Line \#: 1 Report Type: Radiology Report

Date of Service: Appointment Date Transmission Method: Available on Request

Procedure Code\*: 73100 Attachment Control Number:

<span class="mark">Request Comments</span>

Message:

\+ Enter ?? for more actions

SR Send 278 Request AD Add Data EX Exit

Select Action: Next Screen// Send 278 Request

# MCCR Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MCCR Site Parameter Display/Edit option is an IB option that can be used to update IB, Claims Tracking, Automated Billing and Insurance Verification parameters. Refer to the IB V. 2.0 User Manual for a full description of all of the parameters.

Sample Screen

MCCR Site Parameters Oct 28, 2014@12:39 Page: 1 of 1

Display/Edit MCCR Site Parameters.

Only authorized persons may edit this data.

*IB Site ParametersClaims Tracking Parameters*

Facility Definition General Parameters

Mail Groups Tracking Parameters

Patient Billing Random Sampling

Third Party Billing HCSR Parameters

Provider Id

EDI Transmission

*Third Party Auto Billing ParametersInsurance Verification*

General Parameters General Parameters

Inpatient Admission Batch Extracts Parameters

Outpatient Visit Service Type Codes

Prescription Refill

Enter ?? for more actions

IB Site Parameter AB Automated Billing EX Exit

CT Claims Tracking IV Ins. Verification

Select Action: Quit//

The difference between the MCCR Site Parameter Display/Edit option and the Claims Tracking - Claims Tracking Parameter Edit option is that you can view all of the Claims Tracking parameters from MCCR Site Parameters Display/Edit option. The Claims Tracking Parameter Edit option only allows you to view/edit those parameters that are editable. Refer to the Claims Tracking Menu (Combined Functions)… Supervisor Menu (Claims Tracking)… Claims Tracking Parameter Edit.

## The MCCR Site Parameter Display/Edit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MCCR Site Parameter Display/Edit allows you to see all the following Claims Tracking parameter values:

- Tracking Parameters
- Track Inpatient:
  - OFF
  - INSURED AND UR ONLY
  - ALL PATIENTS
- Track Outpatient
  - OFF
  - INSURED ONLY
  - ALL PATIENTS
- Track Rx
  - OFF
  - INSURED ONLY
  - ALL PATIENTS
- Track Prosthetics
  - OFF
  - INSURED ONLY
  - ALL PATIENTS
- General Parameters
- Extended Help
  - OFF
  - ON
- Initialization Date
  - Date
- Use Admission Sheet
  - NO
  - YES
- Header Line 1
  - Free text
- Header Line 2
  - Free text
- Header Line 3
  - Free text
- Random Sample Parameters
- Medicine Sample
  - Number
- Medicine Admissions
  - Number
- Surgery Sample
  - Number
- Surgery Admissions
  - Number
- Psych Sample
  - Number
- Psych Admissions
  - Number

The sample number and the admissions number are used by the system to compute a random number.

- Health Care Services Review (HCSR) Parameters
- CPAC Future Appointments Search: 30 days - Not editable
- CPAC Future Admissions Search: 30 days – Not editable
- CPAC Past Appointments Search: 14 days – Not editable
- CPAC Past Admissions Search: 14 days – Not editable
- TRICARE/CHAMPVA Future Appointments Search: 30 days – Not editable
- TRICARE/CHAMPVA Future Admissions Search: 30 days – Not editable
- TRICARE/CHAMPVA Past Appointments Search: 14 days – Not editable
- TRICARE/CHAMPVA Past Admissions Search: 14 days – Not editable
- Inquiry can be Triggered for Appointment
  - Number of days before an automatic 278 is triggered
- Inquiry can be Triggered for Admission
  - Number of days before an automatic 278 is triggered
- Days to wait to purge entry on HCSR Response
  - Number of days before a 278 response is removed from the worklist
- Clinics Included In the Search – Defined in MCCR Site Parameters
- Wards Included In the Search - Defined in MCCR Site Parameters
- Insurance Companies Included In Appointments Search - Defined in MCCR Site Parameters
- Insurance Companies Included In Admissions Search - Defined in MCCR Site Parameters

Sample Screens

Claims Tracking Parameters Oct 28, 2014@13:09:50 Page: 1 of 2

Only authorized persons may edit this data.

*Tracking Parameters Random Sample Parameters*

Track Inpatient: INSURED AND UR ONLY Medicine Sample: 5

Track Outpatient: INSURED ONLY Medicine Admissions: 5

Track Rx: INSURED ONLY Surgery Sample: 5

Track Prosthetics: INSURED ONLY Surgery Admissions: 5

Reports Can Add CT: YES Psych Sample: 1

Psych Admissions: 5

*General Parameters*

Initialization Date: 01/01/94

Use Admission Sheet: NO

Header Line 1: ANYSITE VAMC

Header Line 2: 2360 E. ANYSTREET

Header Line 3: ANYSITE, WY

\+ Enter ?? for more actions

TP Tracking RS Random Sample GP General

EA Edit All HS HCSR EX Exit

Select Action: Next Screen//

HCSR Parameters Oct 28, 2014@14:20:48 Page: 1 of 1

Only authorized persons may edit this data.

*Health Care Services Review (HCSR) Parameters*

CPAC Future Appointments Search: 30 days

CPAC Future Admissions Search: 30 days

CPAC Past Appointments Search: 14 days

CPAC Past Admissions Search: 14 days

TRICARE/CHAMPVA Future Appointments Search: 30 days

TRICARE/CHAMPVA Future Admissions Search: 30 days

TRICARE/CHAMPVA Past Appointments Search: 14 days

TRICARE/CHAMPVA Past Admissions Search: 14 days

Inquiry can be Triggered for Appointment: 2 days

Inquiry can be Triggered for Admission: 1 days

Days to wait to purge entry on HCSR Response: 20 days

Clinics Included In the Search: 3

Wards Included In the Search: 0

Insurance Companies Included In Appointments Search: 6

Insurance Companies Included In Admissions Search: 8

Enter ?? for more actions

HC Clinics HW Wards OP Other

HA Adm Ins HI Appt Ins EX Exit

Select Action: Quit//

### Clinics Included In the Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter is defined in an option within the HCSR parameters. You can add an existing clinic for all payers or selected payers from the Hospital Location file to a list of clinics that will be included in the nightly search for appointment events. If a patient has an appointment in one of these clinics, his/her appointment event will be added to the HCSR Worklist.

If circumstances change, a clinic can be deleted from this inclusion list or a payer can be deleted from the clinic.

> **NOTE:** If you remove a clinic from the list, it will affect future searches. Entries already on the list from earlier searches, will remain on the worklist.

HCSR Parameters Oct 28, 2014@15:10:55 Page: 1 of 1

Only authorized persons may edit this data.

Health Care Services Review (HCSR) Parameters

CPAC Future Appointments Search: 14 days

CPAC Future Admissions Search: 14 days

CPAC Past Appointments Search: 7 days

CPAC Past Admissions Search: 7 days

TRICARE/CHAMPVA Future Appointments Search: 14 days

TRICARE/CHAMPVA Future Admissions Search: 14 days

TRICARE/CHAMPVA Past Appointments Search: 7 days

TRICARE/CHAMPVA Past Admissions Search: 7 days

Inquiry can be Triggered for Appointment: 0 days

Inquiry can be Triggered for Admission: 0 days

Days to wait to purge entry on HCSR Response: 20 days

*Clinics Included In the Search: 3*

Wards Included In the Search: 0

Insurance Companies Included In Appointments Search: 6

Insurance Companies Included In Admissions Search: 9

Enter ?? for more actions

*HC Clinics* HW Wards OP Other

HA Adm Ins HI Appt Ins EX Exit

Select Action: Quit// HC

HCSR Clinic Inclusions Nov 19, 2014@10:51:39 Page: 1 of 1

Only authorized persons may edit this data.

Clinics Included in the Search:

1 CHY CARDIOLOGY -for all payers

2 TEST -for 2 payers

3 TEST 1 -for all payers

4 TEST 2 -for all payers

5 TESTIB -for all payers

Enter ?? for more actions

AC Add Clinic AP Add Payer to Clinic EX Exit

DL Delete Clinic DP Delete Payer from Clinic

Select Action: Quit// ac Add Clinic

\*\*Warning\*\*

Changing the value in CPAC/TRICARE/CHAMPVA parameters will affect the Health

Care Services Review Worklist.

Select a Clinic to be added: FTC DIABETIC IB,DOCTOR L

Clinic is currently included in the list for no payers

INCLUDE FOR ALL PAYERS?: NO// y YES

Select a Clinic to be added:

Select Action: Quit// ap Add Payer to Clinic

Select HCSR Clinic(s): (1-5): 2

Clinic is currently included in the list for the following 2 payers:

AETNA

CIGNA

INCLUDE FOR ALL PAYERS?: NO//

Select Payer: BCBS KANSAS CITY

Payer added to the list.

Select Payer:

### Wards Included in the Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter is defined in an option within the HCSR parameters. You can add an existing ward for all payers or selected payers from the Hospital Location file to a list of wards that will be included in the nightly search for admission events. If a patient has an admission to one of these wards, his/her admission event will not be added to the HCSR Worklist if the wards are not specified in the inclusion list.

*Note:* If circumstances change, a ward can be deleted from this inclusion list or a payer can be deleted from the ward.

*Note:* If you remove a ward from the list, it will affect future searches. Entries already on the list from earlier searches, will remain on the worklist.

Sample Screens

HCSR Parameters Oct 28, 2014@15:10:55 Page: 1 of 1

Only authorized persons may edit this data.

Health Care Services Review (HCSR) Parameters

CPAC Future Appointments Search: 14 days

CPAC Future Admissions Search: 14 days

CPAC Past Appointments Search: 7 days

CPAC Past Admissions Search: 7 days

TRICARE/CHAMPVA Future Appointments Search: 14 days

TRICARE/CHAMPVA Future Admissions Search: 14 days

TRICARE/CHAMPVA Past Appointments Search: 7 days

TRICARE/CHAMPVA Past Admissions Search: 7 days

Inquiry can be Triggered for Appointment: 0 days

Inquiry can be Triggered for Admission: 0 days

Days to wait to purge entry on HCSR Response: 20 days

Clinics Included In the Search: 3

*Wards Included In the Search: 0*

Insurance Companies Included In Appointments Search: 6

Insurance Companies Included In Admissions Search: 9

Enter ?? for more actions

HC Clinics *HW Wards* OP Other

HA Adm Ins HI Appt Ins EX Exit

HCSR Ward Inclusions Nov 19, 2014@10:56:13 Page: 1 of 0

Only authorized persons may edit this data.

Wards Included In the Search:

1 O&E MEDICAL - for 2 payers

2 TRANSITIONAL - for all payers

Enter ?? for more actions

AW Add Ward AP Add Payer to Ward EX Exit

DW Delete Ward DP Delete Payer from Ward

Select Action: Quit// AW Add Ward

\*\*Warning\*\*

Changing the value in CPAC/TRICARE/CHAMPVA parameters will affect the Health

Care Services Review Worklist.

Select a Ward to be added: C MEDICINE

INCLUDE FOR ALL PAYERS?: NO// Y

Select a Ward to be added:

Select Action: Quit// AP Add Payer to Ward

Select HCSR Ward(s): (1-2): 1

Ward is currently included in the list for the following 2 payers:

CIGNA NATIONAL

CIGNA

INCLUDE FOR ALL PAYERS?: NO//

Select Payer: bcbs of Kansas

Payer added to the list.

Select Payer:

### Insurance Companies Included In Appointment Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter is defined in an option within the HCSR parameters. You can add an existing insurance company from the Insurance Company file to a list of companies that will be included in the nightly search for appointment events. If a patient has insurance with one of these insurance companies, his/her appointment event will be added to the HCSR Worklist.

*Note:* If circumstances change, an insurance company can be deleted from this inclusion list.

*Note:* If you remove an insurance company from the list, it will affect future searches. Entries already on the list from earlier searches, will remain on the worklist.

Sample Screens

HCSR Parameters Oct 28, 2014@14:20:48 Page: 1 of 1

Only authorized persons may edit this data.

Health Care Services Review (HCSR) Parameters

CPAC Future Appointments Search: 14 days

CPAC Future Admissions Search: 14 days

CPAC Past Appointments Search: 7 days

CPAC Past Admissions Search: 7 days

TRICARE/CHAMPVA Future Appointments Search: 14 days

TRICARE/CHAMPVA Future Admissions Search: 14 days

TRICARE/CHAMPVA Past Appointments Search: 7 days

TRICARE/CHAMPVA Past Admissions Search: 7 days

Inquiry can be Triggered for Appointment: 0 days

Inquiry can be Triggered for Admission: 0 days

Days to wait to purge entry on HCSR Response: 20 days

Clinics Included In the Search: 3

Wards Included From the Search: 0

*Insurance Companies Included From Appointments Search: 6*

Insurance Companies Included From Admissions Search: 8

Enter ?? for more actions

HC Clinics HW Wards OP Other

HA Adm Ins *HI Appt Ins* EX Exit

Select Action: Quit// HI Appt Ins

HCSR Insurance Inclusions Nov 19, 2014@11:03:09 Page: 1 of 1

Only authorized persons may edit this data.

Insurance Companies Included In the Appointment Search:

Insurance Company Name Address Line 1 ST

1 AETNA POD 2600 CA

2 CIGNA POD 9999 KY

AI Add Ins DI Delete Ins EX Exit

Select Action: Quit// AI Add Ins

\*\*Warning\*\*

Changing the value in CPAC/TRICARE/CHAMPVA parameters will affect the Health

Care Services Review Worklist.

Select an Insurance Company to be added: AETNA US HEALTHCARE POD 2559 ANYTOWN INDIANA Y

Include all payers with the same electronic Payer ID?? NO// y YES

Select an Insurance Company to be added:

### Insurance Companies Included In Admissions Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter is defined in an option within the HCSR parameters. You can add an existing insurance company from the Insurance Company file to a list of companies that will be included in the nightly search for admission events. If a patient has insurance with one of these insurance companies, his/her admission event will be added to the HCSR Worklist.

*Note:* If circumstances change, an insurance company can be deleted from this inclusion list.

*Note:* If you remove an insurance company from the list, it will affect future searches. Entries already on the list from earlier searches, will remain on the worklist.

Sample Screens

HCSR Parameters Oct 28, 2014@14:20:48 Page: 1 of 1

Only authorized persons may edit this data.

Health Care Services Review (HCSR) Parameters

CPAC Future Appointments Search: 14 days

CPAC Future Admissions Search: 14 days

CPAC Past Appointments Search: 7 days

CPAC Past Admissions Search: 7 days

TRICARE/CHAMPVA Future Appointments Search: 14 days

TRICARE/CHAMPVA Future Admissions Search: 14 days

TRICARE/CHAMPVA Past Appointments Search: 7 days

TRICARE/CHAMPVA Past Admissions Search: 7 days

Inquiry can be Triggered for Appointment: 0 days

Inquiry can be Triggered for Admission: 0 days

Days to wait to purge entry on HCSR Response: 20 days

Clinics Included In the Search: 3

Wards Included In the Search: 0

Insurance Companies Included In Appointments Search: 6

*Insurance Companies Included In Admissions Search: 8*

Enter ?? for more actions

HC Clinics HW Wards OP Other

*HA Adm Ins* HI Appt Ins EX Exit

Select Action: Quit//

HCSR Insurance Inclusions Nov 19, 2014@11:07:56 Page: 1 of 1

Only authorized persons may edit this data.

Insurance Companies Included In the Admissions Search:

Insurance Company Name Address Line 1 ST

1 AETNA POD 2344 CA

2 CIGNA POD 99999 KY

AI Add Ins DI Delete Ins EX Exit

Select Action: Quit// AI Add Ins

\*\*Warning\*\*

Changing the value in CPAC/TRICARE/CHAMPVA parameters will affect the Health

Care Services Review Worklist.

Select an Insurance Company to be added: UNITED HEALTHCARE POD 30555 MYTOWN UTAH Y

Include all payers with the same electronic Payer ID?? NO// y YES

Select an Insurance Company to be added:

# Appendix A – Follow-up Actions Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the AAA error segments and follow-up codes that may be returned to the requester when there is a problem with an X12N Health Care Services Review – Request for Review and Response (278):

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 27%" />
<col style="width: 31%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Loop</th>
<th>Valid Request</th>
<th>Segment Name</th>
<th>Reject Reason Codes</th>
<th>Follow-up Action Codes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2000A</td>
<td>Yes or No</td>
<td>AAA – Request Validation</td>
<td><p>Authorization Quantity Exceeded</p>
<p>Authorization/Access Restrictions</p>
<p>Unable to Respond at Current Time</p>
<p>Invalid Participant Identification</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p>
<p>Please Resubmit Original Transaction</p>
<p>Do Not Resubmit; We Will Hold Your Request and Respond Shortly</p></td>
</tr>
<tr class="even">
<td>2010A</td>
<td>Always No</td>
<td>AAA – UMO Request Validation</td>
<td><p>Unable to Respond at Current Time</p>
<p>Invalid Participant Identification</p>
<p>No Response received – Transaction Terminated</p>
<p>Payer Name or Identifier Missing</p></td>
<td><p>Resubmission Not Allowed</p>
<p>Please Resubmit Original Transaction</p>
<p>Do Not Resubmit; We Will Hold Your Request and Respond Shortly</p></td>
</tr>
<tr class="odd">
<td>2010B</td>
<td>Always No</td>
<td>AAA – Requester Request Validation</td>
<td><p>Required application data missing</p>
<p>Out of Network</p>
<p>Authorization/Access Restrictions</p>
<p>Invalid/Missing Provider Identification</p>
<p>Invalid/Missing Provider Name</p>
<p>Invalid/Missing Provider Specialty</p>
<p>Invalid/Missing Provider Phone Number</p>
<p>Invalid/Missing Provider State</p>
<p>Provider is Not Primary Care Physician</p>
<p>Provider Not on File</p>
<p>Invalid Participant Identification</p>
<p>Invalid or Missing Provider Address</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p>
<p>Resubmission Allowed</p></td>
</tr>
<tr class="even">
<td>2010C</td>
<td>Always No</td>
<td>AAA – Subscriber Request Validation</td>
<td><p>Invalid/Missing Date-of-Birth</p>
<p>Invalid/Missing Patient ID</p>
<p>Invalid/Missing Patient Name</p>
<p>Invalid/Missing Patient Gender Code</p>
<p>Patient Not Found</p>
<p>Duplicate Patient ID Number</p>
<p>Patient Birth Date Does Not Match That for the Patient on the Database</p>
<p>Invalid/Missing Subscriber/Insured ID</p>
<p>Invalid/Missing Subscriber/Insured Name</p>
<p>Invalid/Missing Subscriber/Insured Gender Code</p>
<p>Subscriber/Insured Not Found</p>
<p>Duplicate Subscriber/Insured ID Number</p>
<p>Subscriber Found/Patient Not Found</p>
<p>Invalid Participant Identification</p>
<p>Patient Not Eligible</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="odd">
<td>2010D</td>
<td>Always No</td>
<td>AAA – Dependent Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Invalid/Missing Date-of-Birth</p>
<p>Invalid/Missing Patient ID</p>
<p>Invalid/Missing Patient Name</p>
<p>Invalid/Missing Patient Gender Code</p>
<p>Patient Not Found</p>
<p>Duplicate Patient ID Number</p>
<p>Patient Birth Date Does Not Match That for the Patient on the Database</p>
<p>Subscriber Found/Patient Not Found</p>
<p>Patient Not Eligible</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="even">
<td>2000E</td>
<td>Always No</td>
<td>AAA – Patient Event Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Service Date Not Within Provider Plan Enrollment</p>
<p>Inappropriate Date</p>
<p>Invalid/Missing Date(s) of Service</p>
<p>Date of Birth Follows Date(s) of Service</p>
<p>Date of Death Precedes Date(s) of Service</p>
<p>Date of Service Not Within Allowable Inquiry Period</p>
<p>Authorization Number Not Found</p>
<p>Invalid/Missing Diagnosis Code(s)</p>
<p>Invalid/Missing Onset of Current Condition or Illness Date</p>
<p>Invalid/Missing Accident Date</p>
<p>Invalid/Missing Last menstrual Period Date</p>
<p>Invalid/Missing Expected dat4e of Birth</p>
<p>Invalid/Missing Admission Date</p>
<p>Invalid/Missing Discharge Date</p>
<p>Certification Information Missing</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="odd">
<td>2010EA</td>
<td>Always No</td>
<td>AAA – Patient Event Provider Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Out of Network</p>
<p>Authorization/Access Restrictions</p>
<p>Invalid/Missing Provider Identification</p>
<p>Invalid/Missing Provider Name</p>
<p>Invalid/Missing Provider Specialty</p>
<p>Invalid/Missing Provider Phone Number</p>
<p>Invalid/Missing Provider State</p>
<p>Provider is Not Primary Care Physician</p>
<p>Provider Not on File</p>
<p>Service Dates Not Within Provider Plan Enrollment</p>
<p>Invalid Participant Identification</p>
<p>Invalid or Missing Provider Address</p>
<p>Inappropriate Provider Role</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="even">
<td>2010EC</td>
<td>Always No</td>
<td>AAA – Patient Event Transport Location Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Invalid/Missing Provider State</p>
<p>Invalid or Missing Provider Address</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="odd">
<td>2000F</td>
<td>Always No</td>
<td>AAA – Service Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Service Dates Not Within Provider Plan Enrollment</p>
<p>Invalid/Missing Date(s) of Service</p>
<p>Date of Birth Follows Date(s) of Service</p>
<p>Date of Death Procedes Date(s) of Service</p>
<p>Date of Service Not Within Allowable Inquiry Period</p>
<p>Authorization Number Not Found</p>
<p>Invalid/Missing Procedure Code(s)</p>
<p>Certification Information Missing</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
<tr class="even">
<td>2010FA</td>
<td>Always No</td>
<td>AAA – Service Provider Request Validation</td>
<td><p>Required application data missing</p>
<p>Input Errors</p>
<p>Out of Network</p>
<p>Authorization/Access Restrictions</p>
<p>Invalid/Missing Provider Identification</p>
<p>Invalid/Missing Provider Name</p>
<p>Invalid/Missing Provider Specialty</p>
<p>Invalid/Missing Provider Phone Number</p>
<p>Invalid/Missing Provider State</p>
<p>Provider is Not Primary Care Physician</p>
<p>Provider Not on File</p>
<p>Service Dates Not Within Provider Plan Enrollment</p>
<p>Invalid Participant Identification</p>
<p>Invalid or Missing Provider Address</p>
<p>Inappropriate Provider Role</p></td>
<td><p>Please Correct and Resubmit</p>
<p>Resubmission Not Allowed</p></td>
</tr>
</tbody>
</table>