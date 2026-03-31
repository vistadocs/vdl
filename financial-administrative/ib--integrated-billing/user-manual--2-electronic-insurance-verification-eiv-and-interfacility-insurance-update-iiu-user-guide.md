---
title: IB*2 Electronic Insurance Verification (EIV) and Interfacility Insurance Update (IIU) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: IB*2 Electronic Insurance Verification (EIV) and Interfacility Insurance Update (IIU)
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: archive
pkg_ns: IB
patch_ver: 2.0
patch_id: IB*2.0
group_key: "IB:IB:2.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - insurance
  - entry
  - company
  - buffer
  - report
  - payer
  - patient
  - table
  - contents
  - date
page_count: 0
word_count: 27630
section_count: 42
table_count: 6
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: September 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_eiv_iiu_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_eiv_iiu_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=266"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Electronic Insurance Verification &  
  Interfacility Insurance Update

  Integrated Billing  
  Version 2.0

  User Guide
---

![](ib-2-electronic-insurance-verification-eiv-and-interfacility-insurance-update-ii/001.png)

September 2003  
Revised: February 2023

Office of Information and Technology (OIT)

Revision History

1.  The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption><p><span id="_Toc121848912" class="anchor"></span>Table 1: IV Site Parameters – General (Editable)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 49%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/2023</td>
<td>3.8</td>
<td><p>Patch IB*2*737</p>
<ul>
<li><blockquote>
<p>Updated User Edit Report</p>
</blockquote></li>
<li><blockquote>
<p>Removed references to asterisk in the buffer</p>
</blockquote></li>
<li><blockquote>
<p>Added section for Fixed Corrupt Buffers action</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>10/2022</td>
<td>3.7</td>
<td><p>Updated IB*2*732 and DG*5.3*1080</p>
<ul>
<li><blockquote>
<p>Update Site Parameters (section 2 and 2.1)</p>
</blockquote></li>
<li><blockquote>
<p>Update Payer Edit (section 3.3)</p>
</blockquote></li>
<li><blockquote>
<p>Update Request a 270 Health Care + Benefits Inquiry (section 6.1)</p>
</blockquote></li>
<li><blockquote>
<p>Update screen shots to include PROSTHETICS and VISION (section 7.1)</p>
</blockquote></li>
<li><blockquote>
<p>Update Appendix B - eIV Error Message Descriptions</p>
</blockquote></li>
<li><blockquote>
<p>Updated references of “eIV Nightly Process” to be “eInsurance Night Process”. The software was changed with IB*2.0*687, but we missed this in the documentation.</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>08/2022</td>
<td>3.6</td>
<td><p>Updated IB*2*713</p>
<ul>
<li><blockquote>
<p>Update to IV Site Parameters screen</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>05/2022</td>
<td>3.5</td>
<td><p>Updated IB*2*702</p>
<ul>
<li><blockquote>
<p>Update to Request Electronic Insurance Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Update to IV Site Parameters screen</p>
</blockquote></li>
<li><blockquote>
<p>Update to eIV Reports screen,</p>
</blockquote></li>
<li><blockquote>
<p>Update to eIV Response Report screen</p>
</blockquote></li>
<li><blockquote>
<p>Update to eIV Ambiguous Policy Report</p>
</blockquote></li>
<li><blockquote>
<p>Update to eIV Inactive Policy Report</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>12/2021</td>
<td>3.4</td>
<td><p>Updated IB*2*687</p>
<ul>
<li><blockquote>
<p>Update to Site Parameters</p>
</blockquote></li>
<li><blockquote>
<p>Update to eIV Statistical Report</p>
</blockquote></li>
<li><blockquote>
<p>Update to Payer Edit</p>
</blockquote></li>
<li><blockquote>
<p>Update to Link Insurance Company to Payers using Insurance Company Editor</p>
</blockquote></li>
<li><blockquote>
<p>Removed eIV Payer Link Report which is now in the IB User Manual</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>04/2021</td>
<td>3.3</td>
<td><p>Updated IB*2*668</p>
<ul>
<li><blockquote>
<p>IIU: Remove all old SSVI files routines and components</p>
</blockquote></li>
<li><blockquote>
<p>New Source of Information</p>
</blockquote></li>
<li><blockquote>
<p>Updated section 11</p>
</blockquote></li>
<li><blockquote>
<p>Update to PAL template v1.8, July 2016</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>11/2020</td>
<td>3.2</td>
<td><p>Updated IB*2*664</p>
<ul>
<li><blockquote>
<p>Updated User Edit Report</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>04/2020</td>
<td>3.1</td>
<td><p>Updated IB*2*659</p>
<ul>
<li><blockquote>
<p>Updated section 2 Site Parameters to bring it up to date and add the new functionality from IB*2*659</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/2019</td>
<td>3.0</td>
<td>Updated IB*2*652</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/2019</td>
<td>2.9</td>
<td>Updated IB*2*631</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/2019</td>
<td>2.8</td>
<td>Updated IB*2*621</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/2018</td>
<td>2.7</td>
<td>Updated IB*2*595</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/2018</td>
<td>2.6</td>
<td>Updated IB*2*601</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/2017</td>
<td>2.5</td>
<td>Updated IB*2*582</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/2016</td>
<td>2.4</td>
<td>Updated IB*2*549</td>
<td>FY15 eInsurance Development Team</td>
</tr>
<tr class="even">
<td>02/2016</td>
<td>2.3</td>
<td>Updated IB*2*525, IB*528</td>
<td>Harris Team</td>
</tr>
<tr class="odd">
<td>1/2/2015</td>
<td>2.2</td>
<td>Updated IB*2*521 (Payer Link Report)</td>
<td>FirstView Team</td>
</tr>
<tr class="even">
<td>5/22/2014</td>
<td>2.1</td>
<td>Updated IB*2*111</td>
<td>FirstView Team</td>
</tr>
<tr class="odd">
<td>1/29/2014</td>
<td>2.0</td>
<td>Updated IB*2*497</td>
<td>FirstView Team</td>
</tr>
<tr class="even">
<td>12/20/2011</td>
<td>1.7</td>
<td>Tech Writer Review</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/17/2011</td>
<td>1.6</td>
<td>Updated IB*2*467</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/02/2011</td>
<td>1.5</td>
<td>Updated IB*2*438</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/24/2010</td>
<td>1.4</td>
<td>Updated IB*2*416</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/28/2005</td>
<td>1.2</td>
<td>Updated IB*2*300</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/06/2005</td>
<td>1.3</td>
<td>Updated IB*2*316</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/08/2005</td>
<td>1.1</td>
<td>Updated IB*2*271</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/18/2003</td>
<td>1.0</td>
<td>IB*2*184</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc121848912" class="anchor"></span>Table 1: IV Site Parameters – General (Editable)

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Electronic Insurance Verification (eIV) Process Flow](#electronic-insurance-verification-eiv-process-flow)
  - [Intended Audience](#intended-audience)
  - [Role of the Insurance Verification Interface](#role-of-the-insurance-verification-interface)
  - [National Insurance Payers](#national-insurance-payers)
- [Site Parameters](#site-parameters)
  - [Define General Parameters](#define-general-parameters)
  - [Define Batch Extract Parameters](#define-batch-extract-parameters)
  - [Fix Corrupt Buffers](#fix-corrupt-buffers)
- [Payers](#payers)
  - [Link Insurance Company to Payers using Link Insurance Company to Payers](#link-insurance-company-to-payers-using-link-insurance-company-to-payers)
  - [Link Insurance Company to Payers using Insurance Company Editor](#link-insurance-company-to-payers-using-insurance-company-editor)
  - [Payer Edit](#payer-edit)
- [Process Insurance Buffer](#process-insurance-buffer)
  - [Status Flags](#status-flags)
    - [Buffer Symbols](#buffer-symbols)
    - [Buffer Entry Status Flags](#buffer-entry-status-flags)
    - [Patient Status Flags](#patient-status-flags)
    - [Buffer Entry Source of Information Indicators](#buffer-entry-source-of-information-indicators)
    - [Insurance Entry Update Methods](#insurance-entry-update-methods)
  - [Buffer Actions](#buffer-actions)
    - [Process Entry](#process-entry)
    - [Reject Entry](#reject-entry)
    - [Expand Entry](#expand-entry)
    - [Add Entry](#add-entry)
    - [Sort Buffer Views](#sort-buffer-views)
    - [Check Insurance Company](#check-insurance-company)
    - [Buffer Views: Complete, Positive, Negative, Medicare, Failure, ePharmacy](#buffer-views-complete-positive-negative-medicare-failure-epharmacy)
    - [AAA Errors – Complete Buffer View, Expand Entry](#aaa-errors-complete-buffer-view-expand-entry)
- [Medicare Potential Insurance Worklist – Potential COB Report](#medicare-potential-insurance-worklist-potential-cob-report)
  - [User Prompts](#user-prompts)
    - [Search Criteria – Potential COB Worklist](#search-criteria-potential-cob-worklist)
    - [Sort Criteria – Potential COB Worklist](#sort-criteria-potential-cob-worklist)
    - [Format – Potential COB Worklist](#format-potential-cob-worklist)
    - [Screen ListManager for Completed Entries – Potential COB Worklist](#screen-listmanager-for-completed-entries-potential-cob-worklist)
    - [ListManager – Potential COB Worklist](#listmanager-potential-cob-worklist)
    - [Comments – Potential COB Worklist](#comments-potential-cob-worklist)
    - [Visual Indicators – Potential COB Worklist](#visual-indicators-potential-cob-worklist)
- [Request Electronic Insurance Inquiry](#request-electronic-insurance-inquiry)
  - [Request a 270 Health Care + Benefits Inquiry](#request-a-270-health-care-benefits-inquiry)
  - [Request an Electronic Insurance Coverage Discovery Inquiry](#request-an-electronic-insurance-coverage-discovery-inquiry)
- [Patient Insurance Info View / Edit](#patient-insurance-info-view-edit)
  - [View Patient Policy Information](#view-patient-policy-information)
    - [Patient Policy Comments](#patient-policy-comments)
  - [View Eligibility Benefit Information](#view-eligibility-benefit-information)
- [IIV Auto Match Payers](#iiv-auto-match-payers)
  - [Auto Match in VistA Applications](#auto-match-in-vista-applications)
  - [Types of Auto Match Matches](#types-of-auto-match-matches)
    - [Simple Auto Matches](#simple-auto-matches)
    - [Wildcard Auto Match Matches](#wildcard-auto-match-matches)
  - [Enter / Edit Auto Match Entries (AE)](#enter-edit-auto-match-entries-ae)
    - [Add an Auto Match Entry](#add-an-auto-match-entry)
    - [Edit an Auto Match Entry](#edit-an-auto-match-entry)
    - [Delete an Auto Match Entry](#delete-an-auto-match-entry)
  - [Add Auto Match Entries Using Insurance Buffer Data](#add-auto-match-entries-using-insurance-buffer-data)
  - [Check Insurance Buffer Company Names](#check-insurance-buffer-company-names)
  - [Change Company Name via the Insurance Buffer](#change-company-name-via-the-insurance-buffer)
- [eIV Reports](#eiv-reports)
  - [HL7 Response Report](#hl7-response-report)
  - [eIV Auto Update Report](#eiv-auto-update-report)
  - [eIV Response Report](#eiv-response-report)
  - [eIV Payer Report](#eiv-payer-report)
  - [Medicare Potential Insurance Worklist - Potential COB Worklist / Report](#medicare-potential-insurance-worklist-potential-cob-worklist-report)
    - [Medicare Potential COB – as a Worklist](#medicare-potential-cob-as-a-worklist)
    - [Medicare Potential COB – as a Report](#medicare-potential-cob-as-a-report)
  - [eIV Statistical Report](#eiv-statistical-report)
  - [MailMan Summaries](#mailman-summaries)
  - [MailMan Notification to Link Payers](#mailman-notification-to-link-payers)
  - [MailMan Notification to Activate Payers](#mailman-notification-to-activate-payers)
  - [eIV Ambiguous Policy Report](#eiv-ambiguous-policy-report)
  - [eIV Inactive Policy Report](#eiv-inactive-policy-report)
- [Insurance Reports](#insurance-reports)
  - [List Group Plans without Annual Benefits Report](#list-group-plans-without-annual-benefits-report)
  - [User Edit Report](#user-edit-report)
- [Exporting Reports to Excel](#exporting-reports-to-excel)
- [Schedule / Unschedule MailMan Messages](#schedule-unschedule-mailman-messages)
- [Real Time Insurance Verification Inquiry](#real-time-insurance-verification-inquiry)
- [Purging eIV Files (IRM Users)](#purging-eiv-files-irm-users)
  - [Purge Transmission Queue and or Response File](#purge-transmission-queue-and-or-response-file)
  - [Purge Mailman Reminder](#purge-mailman-reminder)
- [Appendix A – eIV Troubleshooting](#appendix-a-eiv-troubleshooting)
  - [No eIV Inquiries Transmitted](#no-eiv-inquiries-transmitted)
    - [Site Parameters](#site-parameters-1)
    - [Restoring Connectivity to FSC (IRM)](#restoring-connectivity-to-fsc-irm)
    - [Requeue Batch Process (IRM)](#requeue-batch-process-irm)
    - [Restart HL7 Logical Link (IRM)](#restart-hl7-logical-link-irm)
  - [No link between an Insurance Company and a Payer](#no-link-between-an-insurance-company-and-a-payer)
  - [A Buffer or Appointment Extract Entry Failed to Create an Inquiry](#a-buffer-or-appointment-extract-entry-failed-to-create-an-inquiry)
- [Appendix B – eIV Error Message Descriptions](#appendix-b-eiv-error-message-descriptions)
- [Appendix C – Acronyms / Abbreviations / Terms](#appendix-c-acronyms-abbreviations-terms)
In 1996, Congress passed into law the Health Insurance Portability and Accountability Act (HIPAA). This Act directs the federal government to adopt national electronic standards for automated transfer of certain health care data between health care payers, plans, and providers. Now that these standards are in place, the Veterans Health Administration (VHA) will submit electronic 270 Health Care Benefits Eligibility Inquiries to payers and receive 271 Health Care Benefits Eligibility Responses from the payers.

## Electronic Insurance Verification (eIV) Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA (Veterans Health Information Systems and Technology Architecture) users enter patient insurance information through a variety of processes:

- Insurance information may be entered manually during the Registration process
- It may be entered when the patient’s insurance card is read by the insurance card reader
- A user may enter patient’s insurance information directly into the Patient file using the Patient Insurance Info View/Edit option

Regardless of how the patient’s insurance information gets entered into VistA, it must be verified with the insurance company and the verification must be periodically updated. The goal of the eIV process is to automate as much of the verification process as possible to ensure that the insurance information, used to submit claims for services rendered to the patient, is accurate and up to date. This in turn, increases the likelihood of timely reimbursement and increased revenue.

The eIV interface is bi-directional. The HIPAA Health Care Eligibility Benefit Inquiry transaction is referred to as the 270 and the Response is referred to as the 271. The 270 Health Care Eligibility Benefit Inquiry originates at a VAMC VistA system and is transmitted as a Health Level Seven (HL7) message to the Eligibility Communicator at the Financial Services Center (FSC) in Austin, TX. At FSC, the HL7 message is translated into a HIPAA compliant 270 Health Care Eligibility Benefit Inquiry message and sent to one of the VA’s clearinghouses. From the clearinghouse, the 270 message is transmitted to the designated payer.

The 271 Health Care Eligibility Benefit Response originates at the payer and is sent to FSC through the clearinghouse. FSC translates the response back into an HL7 message and transmits it to the originating VAMC VistA system.

<span id="_Toc121848904" class="anchor"></span>Figure 1: eIV Process Flow

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this guide is primarily intended for those users who create, update, accept and reject insurance buffer entries or otherwise maintain patients’ insurance data using VistA Integrated Billing (IB) software.

## Role of the Insurance Verification Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the electronic insurance verification software is to replace much of the telephone work performed by insurance personnel to verify patients’ health care insurance.

Electronic insurance inquiries can be made to any electronically active payer.

Automating the insurance verification process should result in an increase in the accuracy and timeliness of patient insurance information in VistA. These improvements will, in turn, reduce the number of rejected third-party claims for services rendered to the Veteran by the Veteran’s Administration (VA).

VistA performs both a Buffer Extract and an Appointment Extract. For the Appointment Extract, VistA prepares HL7 inquiries during the night in response to appointment events. For the Buffer Extract, VistA immediately prepares HL7 inquiries in response to registration and check in events. The HL7 inquiries are transmitted to the Eligibility Communicator at the FSC. The messages are translated into 270 Health Care Eligibility Benefits Inquiry messages. They are then sent to the VA’s clearinghouses who then distribute them to the correct insurance companies. The 271 Health Care Eligibility Benefits Responses are returned from the payer through the clearinghouses to FSC for translation into an HL7 format and then transmitted to the originating VistA system. There the information is either placed into the insurance buffer for the insurance clerk to review and process to the patient’s insurance file or used to automatically update the patient’s insurance file.

<span id="_Toc121848905" class="anchor"></span>Figure 2: Flowchart of eIV Processes

Automatic updates are made only when a response meets pre-determined criteria. The criteria vary slightly depending upon the situation (e.g. Non-Medicare insurance when the Patient is the Insurance Subscriber will be different from Non-Medicare insurance when the Patient is a dependent of the Insurance Subscriber). Below is an example of some of the criteria:

1.  Automatic Update Setting = Yes
2.  Subscriber ID (VistA) = Subscriber ID (271 Response)
3.  Subscriber DOB (VistA) = Subscriber DOB (271 Response)
4.  Subscriber’s Name (VistA) = Subscriber Name (271 Response)
5.  Group Number (VistA) = Group Number (271 Response)
2.  The Automatic Update Setting is also referred to as the Trusted Payer Flag.

## National Insurance Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the various VistA sites to be able to request eligibility information from the various payers, a national VA insurance payer list has been established. The national payer list provides a standard identification system for all payers that are participating in this process. Each VistA site has the ability to link the insurance companies in their own database to the appropriate payer in the national payer list. This standardizes the identification of the payer to which each inquiry will be directed.

<span id="_Toc121848906" class="anchor"></span>Figure 3: Flowchart of Inquiries from VistA to Payers and Responses from Payers to VistA

# Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VistA site can use the IVsite parameters to configure some aspects of the eIV and Interfacility Insurance Update (IIU) software in order to meet a site's unique requirements.

| General Parameter (Editable) | Definition                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Medicare Payer               | Medicare entry from the Payer file (#365.12). It is used to identify the Medicare payer for the insurance buffer lists and any other applications that need to know which payer is the Medicare WNR payer.                                                                                                                                                 |
| HMS Directory                | The name of the directory where Extract/Result files are stored as needed by HMS Data Extractor.                                                                                                                                                                                                                                                           |
| EII Active                   | Enable/activate eII Software? YES / NO                                                                                                                                                                                                                                                                                                                     |
| IIU Enabled                  | When enabled, the receiving VAMC will evaluate the possibility of storing the active verified policy in the buffer. When not enabled, the receiving VAMC will NOT store the policy in the buffer.                                                                                                                                                          |
| eIV No Group \# Auto-Update  | Select a value which represents how long ago a policy expiration date must be older than to evaluate eIV responses without a group number for auto-update consideration. This only applies when a patient file contains a single active policy and one or more expired policies for the same insurance company. Value must be a number between 7-180 days. |

<span id="_Toc121848913" class="anchor"></span>Table 2: IV Site Parameters – eIV Parameters (Non-editable)

<table>
<caption><p><span id="_Toc121848914" class="anchor"></span>Table 3: IV Site Parameters – Batch Extracts: Buffer Extract</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eIV Parameters</p>
<p>(Non-editable)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Freshness Days</td>
<td><p>How frequently should insurance information be re-verified in days? 7–180 Days</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Medicare Freshness Days</td>
<td><p>How frequently should Medicare insurance information be re-verified in days? 181-545 Days</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td>Timeout Days</td>
<td><p>Number of days that will define a communication timeout. 1–7 Days</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Retry Flag</td>
<td><p>Should an eIV Inquiry retransmit if no response is received?<br />
YES / NO</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td>Timeout Mailman Msg</td>
<td>Send a mail message for each communication timeout?<br />
YES / NO</td>
</tr>
<tr class="even">
<td>Number of Retries</td>
<td>Number of times to retry an eIV transmission. 0–5 Days</td>
</tr>
<tr class="odd">
<td>Default STC</td>
<td>Default Service Type Code to be used on the eIV 270 transmissions.</td>
</tr>
<tr class="even">
<td>Mail Group</td>
<td>To which mail group should the eIV Statistical Report and other eIV messages be sent?</td>
</tr>
<tr class="odd">
<td>Master Switch Realtime</td>
<td><p>”YES” allows real time 270 transactions to be created and transmitted to the Eligibility Communicator (EC). YES / NO</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Master Switch Nightly</td>
<td><p>YES / NO.</p>
<p>”YES” allows the following to occur when the eInsurance Night Process is run: eIV extracts run and create 270 transactions, an eIV registration message is sent to the EC, eIV sends 270 transactions upon successful exchange of eIV registration message, the morning statistical report is scheduled to run at a given time (Daily Mailman Msg), the morning eIV registration message with statistics is scheduled to be created and sent to EC at a given time (Daily Mailman Msg).</p>
<p>“NO” prevents all of the tasks listed above from occurring.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td>CMS MBI Payer</td>
<td><p>The National Payer used for MBI transactions. This field stores a pointer to the Payer File (#365.12).</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>HL7 Max #</td>
<td><p>Allows the restriction of the daily number of HL7 messages created and sent during the HL7 process for eIV during the eInsurance Night Process. 1–99999 Messages</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td><p>EICD Payer</p>
<p>(Electronic Insurance Coverage Discovery)</p></td>
<td><p>The National Payer used for EICD transactions. This field stores a pointer to the Payer File.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Send MailMan Message if Communication Problem</td>
<td>Defines whether a MailMan message will be sent if a communication problem/failure occurs. YES / NO</td>
</tr>
<tr class="odd">
<td>Receive MailMan Message, Daily Statistical</td>
<td><p>Defines whether the eIV Statistical Report will be sent in a MailMan message each day and the statistical data to FSC at the time specified. YES / NO</p>
<p>It also defines the time this message would be sent (set to be sent at 7:00 a.m., local time, each day) “at 0700”.</p>
<p>If the system is set to send an eIV Statistical Report it will be sent to the Messages Mail Group (listed above as ‘Mail Group’).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc121848914" class="anchor"></span>Table 3: IV Site Parameters – Batch Extracts: Buffer Extract

<table>
<caption><p><span id="_Toc121848915" class="anchor"></span>Table 4: IV Site Parameters – Batch Extracts: Appointment Extract</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Batch Extracts section: Buffer Extract</p>
<p>(Non-editable)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>On/Off</td>
<td>Buffer Extract will be turned on.</td>
</tr>
<tr class="even">
<td>Start Days From Today</td>
<td>Displayed as Today, due to the fact that the Buffer Extract attempts to verify <u>all</u> user editable buffer entries that have not been processed by eIV.</td>
</tr>
<tr class="odd">
<td>Days After Start</td>
<td>Displayed as Today, due to the fact that the Buffer Extract attempts to verify <u>all</u> user editable buffer entries that have not been processed by eIV.</td>
</tr>
<tr class="even">
<td>Freq.</td>
<td>How frequently should insurance information be re-verified in days? Typically this is set to 180 days.</td>
</tr>
<tr class="odd">
<td>Maximum # to Extract/Day</td>
<td><p>Maximum number of records extracted and available to be transmitted to FSC each day. Max is typically set to 99999. Valid values are 10-99999.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc121848915" class="anchor"></span>Table 4: IV Site Parameters – Batch Extracts: Appointment Extract

<table>
<caption><p><span id="_Toc121848916" class="anchor"></span>Table 5: IV Site Parameters – Batch Extracts: Non-verified Extract</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Batch Extracts section:</p>
<p>Appointment Extract</p>
<p>(Non-editable)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>On/Off</td>
<td>Appointment Extract will be turned on.</td>
</tr>
<tr class="even">
<td>Start Days From Today</td>
<td>Appointment extracts will search for Appointments scheduled starting “Today”.</td>
</tr>
<tr class="odd">
<td>Days After Start</td>
<td>Appointment extracts will search for appointments scheduled for the next X number of days from the Start Date. X is typically set to 10 days. Valid values are 0-20 days.</td>
</tr>
<tr class="even">
<td>Freq.</td>
<td>How frequently should insurance information be re-verified in days? Typically this is set to 180 days.</td>
</tr>
<tr class="odd">
<td>Maximum # to Extract/Day</td>
<td><p>Maximum number of records extracted and available to be transmitted to FSC each day. Max is typically set to 99999. Valid values are 10-99999.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc121848916" class="anchor"></span>Table 5: IV Site Parameters – Batch Extracts: Non-verified Extract

<table>
<caption><p><span id="_Toc121848917" class="anchor"></span>Table 6: IV Site Parameters – Batch Extracts: EICD Extract</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Batch – Non-verified Extract</p>
<p>(This extract is not visible to the user at this time.)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active?</td>
<td>Non-Verified Extract will be turned off.</td>
</tr>
<tr class="even">
<td>Selection Criteria #1</td>
<td>Non-Verified Extract will be turned off.</td>
</tr>
<tr class="odd">
<td>Selection Criteria #2</td>
<td>Non-Verified Extract will be turned off.</td>
</tr>
<tr class="even">
<td>MAXIMUM EXTRACT NUMBER</td>
<td>Non-Verified Extract will be turned off.</td>
</tr>
</tbody>
</table>

<span id="_Toc121848917" class="anchor"></span>Table 6: IV Site Parameters – Batch Extracts: EICD Extract

<table>
<caption><p><span id="_Toc121848918" class="anchor"></span>Table 7: Buffer Symbols</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Batch Extracts section:</p>
<p>EICD Extract</p>
<p>(Non-editable)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>On/Off</td>
<td>EICD Extract will be turned on.</td>
</tr>
<tr class="even">
<td>Start Days From Today</td>
<td><p>EICD Extract will search for Appointments scheduled X days from Today. X is typically set to 31 days. Valid values are 0-31 days.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td>Days After Start</td>
<td><p>EICD Extract will search for X number of days from the Start Date. X is typically set to 9 days. Valid values are 0-20 days.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Freq.</td>
<td><p>How often a veteran’s insurance can be picked up by this extract. Typically, no more than once a year (365 Days). Valid values are 90-365 days.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="odd">
<td>Maximum # to Extract/Day</td>
<td><p>Maximum number of records extracted and available to be transmitted to FSC each day. Max is typically set to 99999. Valid values are 10-99999.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc121848918" class="anchor"></span>Table 7: Buffer Symbols

Table 7: IV Site Parameters – IIU (non-editable)

<table>
<caption><p><span id="_Toc121848919" class="anchor"></span>Table 8: Patient Status Flags</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><p>IIU Parameters</p>
<p>(Non-editable)</p></th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Max Days of Recent Visit</td>
<td><p>A patient must have recently visited the receiving VAMC within this number of days, for the possibility of storing the active verified policy in the buffer. Valid values are 0-500 days.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Purging Sent Records</td>
<td><p>Number of days to retain previously sent policies that are stored in the Interfacility Insurance Update file (#365.19) before purging. Valid values are 3-365 days.</p>
<p>This was set to 180 days to retain IIU data as its initial value.</p></td>
</tr>
<tr class="odd">
<td>Min Days Before Sharing Again</td>
<td><p>Minimum number of days allowed since the last time the policy information was sent/shared to another VAMC via IIU. Valid values are 1-500 days.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Purging Received Records</td>
<td><p>Number of days to retain previously received Interfacility Insurance Update file (#365.19) before purging. Valid values are 15-60 days.</p>
<p>This was set to 30 days to retain IIU data as its initial value.</p></td>
</tr>
<tr class="odd">
<td>IIU Master Switch</td>
<td><p>YES / NO.</p>
<p>This field is used in VistA to allow/prevent the sharing of verified active policies to other VAMCs via the IIU process. “YES” allows the following to occur when the <strong>eInsurance Night Process</strong> is run: verified active policies are shared with other VAMCs. A 'NO' means the IIU processing is Disabled.</p>
<p>This value is controlled by FSC via an HL7 message.</p></td>
</tr>
<tr class="even">
<td>Purging Candidate Records</td>
<td><p>Number of days to retain candidate records in the Interfacility Insurance Update file (#365.19) that are still waiting to be sent to other VAMCs before purging. Valid values are 3-14 days.</p>
<p>This was set to 7 days to retain IIU data as its initial value.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc121848919" class="anchor"></span>Table 8: Patient Status Flags

## Define General Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the SYST MCCR System DefinitionMenu.
2.  Access the SITE MCCR Site Parameter Display/Edit option.
3.  At the Select Action: prompt, enter IV for Ins. Verification.

MCCR Site Parameters Dec 10, 2010@11:15:16 Page: 1 of 1

Display/Edit MCCR Site Parameters.

Only authorized persons may edit this data.

IB Site Parameters Claims Tracking ParametersFacility Definition General ParametersMail Groups Tracking ParametersPatient Billing Random SamplingThird Party Billing HCSR ParametersProvider IdEDI TransmissionThird Party Auto Billing Parameters Insurance VerificationGeneral Parameters General ParametersInpatient Admission eIV ParametersOutpatient Visit eIV Batch ExtractsPrescription Refill IIU Parameters

Enter ?? for more actions

IB Site Parameter AB Automated Billing EX Exit

CT Claims Tracking IV Ins. Verification

Select Action: Quit// IV Ins. Verification

The following screen will be displayed.

IV Site Parameters May 28, 2015@18:58:17 Page: 1 of 2

Only authorized persons may edit this data.

-----------------------------------------------------------------------------

General Parameters (editable)

Medicare Payer: CMS

HMS Directory: /home/kidsfiles/

EII Active: NO

IIU Enabled: YES eIV No Group \# Auto-Update: 180

eIV Parameters (non-editable)

Freshness Days: 180 Medicare Freshness Days: 365

Timeout Days: 5 Retry Flag: NO

Timeout Mailman Msg: NO Number of Retries: 1

Default STC: 30 Mail Group: IBCNE EIV MESSAGE

Master Switch Realtime: YES Master Switch Nightly: YES

CMS MBI Payer: CMS MBI ONLY HL7 Max \#: 99999

EICD Payer: ELECTRONIC COVERAGE DISCOVERY

Send MailMan Message if Communication Problem: YES

Receive MailMan Message, Daily Statistical: YES at 0700

\+ Enter ?? for more actions

GP General Parameters FB Fix Corrupt Buffers EX Exit

Select Action: Next Screen//

IV Site Parameters May 28, 2015@19:00:08 Page: 2 of 2

Only authorized persons may edit this data.

--------------------------------------------------------------------------------

Batch Extracts

Extract Start Days Days After Maximum \# to

\_<u>Name On/Off From Today Start Freq. Extract/Day</u>

Buffer ON Today Today 180 99999

Appt \* ON Today 10 180 99999

EICD ON 31 9 365 99999

\* Appt extract - Medicare frequency is 365 days

IIU Parameters (non-editable)

Max Days of Recent Visit: 335 Purging Sent Records: 180

Min Days Before Sharing Again: 170 Purging Received Records: 30

IIU Master Switch: YES Purging Candidate Records: 7

\+ Enter ?? for more actions

GP General Parameters FB Fix Corrupt Buffers EX Exit

Select Action: Quit// GP General Parameters

General Parameters

Medicare Payer: CMS//

HMS Directory: /home/kidsfiles//

EII Active: NO//

IIU Enabled: YES//

eIV No Group \# Auto-Update: 180//

6.  At the Select Action: prompt, enter GP for General Parameters.
7.  At the Medicare Payer: prompt, enter the appropriate value.
8.  At the HMS Directory: prompt, enter the directory appropriate for your site.
9.  At the EII Active: prompt, enter the appropriate value.
10. At the IIU Enabled: prompt, enter the appropriate value.
11. At the eIV No Group \# Auto-Update: prompt, enter the appropriate value.
3.  The FRESHNESS DAYS prompt has been removed with patch IB\*2\*506. This is no longer editable and system is set to 180.

    The MEDICARE FRESHNESS DAYS prompt was added with patch IB\*2\*659. This prompt is non-editable, and the system is set to 365.

    The DAILY MAILMAN MSG prompt has been removed as it is no longer optional.

    The DAILY MSG TIME prompt has been removed with patch IB\*2\*506. The system is set to automatically send the daily message at 0700 local time.

    The MESSAGES MAILGROUP: prompt has been removed by patch IB\*2\*549. This field is no longer editable and is set to IBCNE EIV MESSAGE.

    The HL7 RESPONSE PROCESSING prompt has been removed with patch IB\*2\*506. This field is no longer editable and the system is set to Immediate.

    Patch IB\*2\*416 removed the prompt HL7 MAXIMUM NUMBER. A site can no longer limit the number of daily inquiries.

    The Store Service Type code entry functionality has been removed by patch IB\*2\*549. This field is no longer editable and is set to 30.

    The FAILURE MAILMAN MSG: prompt has been removed by patch IB\*2\*549. This field is no longer editable and is set to Yes.

    The IIU ENABLED prompt was added with patch IB\*2\*687. This prompt is editable.

## Define Batch Extract Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*438 removed the ability for the sites to define Batch Extract Parameters.

4.  Patch IB\*2\*416 removed the ability for sites to define Buffer and Appointment parameters. No insurance parameters were removed as no inquiries will be sent for patients w/o insurance.

    Patch IB\*2\*438 set Non-verified parameters to Not Active and Non-editable.

    Patch IB\*2\*438 updated the eIV system to no longer check for freshness days (‘Days between electronic re-verification checks’ defined in the MCCR site parameter) for eligibility benefit inquiries that are available in the buffer and are awaiting transmission in the transmission queue.

    Appointment extracts will skip policies whose last verified date is less than the freshness days from creating buffer entries. (Medicare policies have a different freshness days parameter than non-Medicare policies.)

    Patch IB\*2\*631 added the Electronic Insurance Coverage Discovery (EICD) extract that will look for insurance coverage for patients with appointments within a date range but no more than once a year.

## Fix Corrupt Buffers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FIX CORRUPT BUFFERS action is a restricted action that frees up patient records when no buffer entry is found. This action was added with Patch IB\*2\*713.

# Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Payer file (#365.12) is a VA national file of insurance companies within each VistA system. It is automatically updated when a payer is enrolled and registered at the FSC by the eBusiness Solutions Office. It is non-editable at the facility level and the same data exists in this file at all VistA locations. However, the VistA locations do have the option to locally enable/not enable payers.

When a 270 Health Care Eligibility Benefits Inquiry is constructed, it is this payer name in the Payer file (#365.12), not the Insurance Company name, which is transmitted with the inquiry. In order for an individual insurance company to participate in the eIV process, it must be linked to a payer in the Payer file. It is important to note that:

- An insurance company can be linked to only one payer.
- Many insurance companies can be linked to a single payer.
- The payer must also be eIV Locally Enabled in order for it to be eligible for inclusion in the eIV process.

## Link Insurance Company to Payers using Link Insurance Company to Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Link Insurance Companies to Payers option provides a tool for identifying potential matches of active Insurance Companies with Professional and Institutional IDs that are not linked to a particular Payer. Professional and Institutional Payer Primary ID fields correspond respectively to the EDI ID NUMBER – PROF and EDI ID NUMBER – INST fields in the Insurance Company Editor.

1.  Access the PI Patient InsuranceMenu.
12. Access the PM Payer Maintenance option.
5.  Users must hold the IBCNE EIV IIU MAINTENANCE security key to access this option.
13. Access the LI Link Insurance Companies to Payers option.
6.  The system finds potential matches for users based on matching Payer Primary ID fields in the Insurance Company Editor. Please note that all matches are not definitive and should be linked at the user’s discretion.

The following screen of Payers who have potentially matching insurance company entries will be displayed:

Payer Maintenance Sep 22, 2009@14:26:21 Page: 1 of 1

Payers with potential matches to active insurance companies.

Payer Name \# Potential Matches

1 IBpayer One 2

2 IBpayer Two 1

3 IBpayer Three 3

4 IBpayer Four 1

Enter ?? for more actions

EE Expand Entry EX Exit

Select Action: Quit//

14. At the Select Action: prompt, enter EE for Expand Entry.
15. At the Select entry to Expand, by line \#: (1-5): prompt, enter 2 for this example.

The following screen will be displayed:

Payer Expand Screen Sep 22, 2009@14:45:22 Page: 1 of 1

PAYER: IBpayer Two Prof. EDI#:11111 Inst. EDI#:11111

Insurance Company Name - Active Only

Insurance Company Name Address Prof# Inst#

1 IBinsurance Two A PO BOX 5555 ANYTOWN, PA 11111 11111

2 IBinsurance Two B PO BOX 55555 ANYCITY OHIO 11111 11111

Enter ?? for more actions

PL Print List EX Exit

LP Link Payer

Select Action: Quit//

16. At the Select Action: prompt, enter LP for Link Payer.
17. At the Select 1 or more Insurance Company Entries: prompt, enter 1-2 for this example.
18. At the OK to proceed? YES// prompt, press RETURN to accept the default of YES.
7.  Patch IB\*2\*416 provided the ability to link more than one insurance company to a payer at one time.

    Users also have the option to print a list of insurance companies that may match a Payer. The list can be printed to a printer or to the screen.

Select 1 or more Insurance Company Entries: (1-2): 1-2

You have selected 2 insurance companies  
to be linked to payer IBpayer Two.  
OK to proceed? YES//

Link process is complete.

You may view/edit this relationship by using the  
Insurance Company Entry/Edit option.

Enter RETURN to continue or '^' to exit:

To print the details, go back to Expand Entry and select Print List as detailed below.

1.  Access the PI Patient Insurance Menu.
19. Access the PM Payer Maintenance option.
20. Access the LI Link Insurance Companies to Payers option.
21. At the Select Action: prompt, enter EE for Expand Entry.
22. At the Select entry to Expand, by line \#: (1-5): prompt, enter 2 for this example.
23. At the Select Action: prompt, enter PL for Print List.
24. At the Device://Home: prompt enter RETURN to display to the screen or enter a device name.

The following screen will be displayed.

Payer Expand Screen Sep 22, 2009@14:45:22 Page: 1 of 1

PAYER: IBpayer Two Prof. EDI#:11111 Inst. EDI#:11111

Insurance Company Name - Active Only

Insurance Company Name Address Prof# Inst#

1 IBinsurance Two A PO BOX 5555 ANYTOWN, PA 11111 11111

2 IBinsurance Two B PO BOX 555555 ANYCITY OHIO 11111 11111

Enter RETURN to continue or '^' to exit:

## Link Insurance Company to Payers using Insurance Company Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA is unable for any reason to identify an insurance company as a potential match to a payer, users can link the insurance company to a payer from within the Insurance Company Editor.

1.  Access the PI Patient InsuranceMenu.
25. Access the EI Insurance Company Entry/Edit option.
26. At the Select INSURANCE COMPANY NAME: prompt, enter IBinsurance Two A for this example.

The following screen will be displayed:

Insurance Company Editor Sep 22, 2009@15:11:57 Page: 1 of 9

Insurance Company Information for: IBinsurance Two A

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Type Of Coverage: HEALTH INSURAN

Reimburse?: WILL REIMBURSE Billing Phone: 555-555-5555

Mult. Bedsections: YES Verification Phone: 555-555-5555

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone: 1-800-555-5555

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (12 MONTH(S))

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC

PAYER: IBpayer Two

27. At the Select Action: prompt, enter PA for Payer.
28. At the Payer: prompt, enter ?? to see a list of Payers.
29. At the Payer: prompt, enter IBpayer Two for this example.
8.  Users must hold the IBCNE EIV IIU MAINTENANCE security key to access the (PA) Payer action.

    To view the linked Payer for a particular insurance company, users may access VI for View Insurance Company.

The following screen will be displayed:

Insurance Company Editor Jul 07, 2010@13:55:50 Page: 8 of 9

Insurance Company Information for: IBinsurance Two A

Type of Company: HEALTH INSURANCE Currently Active

\+

Insurance Company Editor Jul 07, 2010@13:55:50 Page: 8 of 9

Insurance Company Information for: IBinsurance Two A

Type of Company: HEALTH INSURANCE Currently Active

\+

Payer: PAYER1

VA National ID: VA10 CMS National ID:

Deactivated: NO

Payer Application: eIV

Nationally Enabled: YES FSC Auto-Update: YES

Locally Enabled: YES

Payer Application: IIU

Nationally Enabled: YES Receive IIU Data: NO

Locally Enabled: YES

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

<span id="_Insurance_Company_Entry/Edit" class="anchor"></span>To view the linked payer for an insurance company, go back to the Patient Insurance Menu and select View Insurance Company.

1.  Access the PI Patient Insurance Menu.
30. Access the VI View Insurance Company option.
31. At the Select INSURANCE COMPANY NAME: prompt, enter IBinsurance Two A for this example.

The following screen will be displayed:

Insurance Company Editor Sep 22, 2009@15:11:57 Page: 1 of 8

Insurance Company Information for: IBinsurance Two A

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Type Of Coverage: HEALTH INSURAN

Reimburse?: WILL REIMBURSE Billing Phone: 555-555-5555

Mult. Bedsections: YES Verification Phone: 555-555-5555

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone: 1-800-555-5555

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (12 MONTH(S))

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

Inst Payer Primary ID: XXXXX Prof Payer Primary ID: XXXXX

\+ Enter ?? for more actions \>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen//

## Payer Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit the payer information users must use the Payer Maintenance Menu. The Payer Edit option is restricted to users with the IBCNE EIV IIU MAINTENANCE security key.

1.  Access the PI Patient Insurance Menu.
32. Access the PM Payer Maintenance Menu.
33. Access the PE Payer Edit option.
34. The user will be prompted with the chance to filter the Payer Name by begins with or contains. At this same prompt, the user may select list to view all available payers.
35. When selecting begins with or contains, at the Payer Name: prompt, enter IBPAYER TWO for this example.
9.  Users must hold the IBCNE EIV IIU MAINTENANCE security key to access Payer Edit.

The following screen will be displayed:

Payer Edit

This option displays the data in the Payer file for a given payer. You

may only edit site controlled fields and most fields are not site controlled.

Site controlled fields cannot be edited for a deactivated payer.

Payer Name: IBPAYER TWO

VA National ID: VA685

CMS National ID:

Blue Payer: YES

Inst Electronic Bill ID: 12B23

Prof Electronic Bill ID: SB810

Date/Time Created: 09/25/2003@06:31:19

Payer Application: eIV Payer Application: IIU

-------------------------------------- -----------------------------------

Nationally Enabled: Enabled Nationally Enabled: Enabled

Future Service Days: 30 IIU Locally Enabled: Enabled

Past Service Days: 9999 Receive IIU Data: YES

Auto-update Pt. Insurance: YES

eIV Locally Enabled: Enabled

eIV App \> eIV Locally Enabled: Enabled//

IIU App \> Receive IIU Data: YES//

36. At the eIV App \> eIV Locally Enabled: prompt, users can type Enabled or disable (Not Enabled) . Press RETURN to accept the default for this example.
37. At the IIU App \> Receive IIU Data: prompt, users can select NO or YES for a Payer. Press RETURN to accept the default for this example.
10. Users can only type Enabled or Not Enabled (disable) a Payer for eIV under the eIV Locally Enabled field and select NO or YES for Receive IIU Data when applicable. The remainder of the Payer information is set by FSC.

    WARNING: A payer must be nationally enabled and locally enabled for 270 / 271 Health Care Eligibility Inquiry and Response messages to be transmitted.
11. Patch IB\*2\*416 removed the ability for patient SSNs be transmitted as IDs in a 270 Health Care Eligibility Inquiry so those prompts were removed from Payer Edit.
12. Users can select YES for Receive IIU Data in order to show policies received from IIU for this payer in the buffer.

# Process Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Insurance Buffer option provides six buffer views from which users may process entries and thus update patients’ insurance information in the patient file:

- Complete Buffer – Contains all records that can be found on the other Insurance Buffer views (Positive, Negative, Medicare, Failure and ePharm) in addition to the following types of records: eIV inquiries waiting for responses “?”, manual entries \<blank\> , ambiguous responses “#”, responses that include the value “%”.
- Positive Buffer – Positive 271 Health Care Eligibility Benefits Responses (that failed to meet the auto-update criteria and are non-Medicare). These responses may have one of the symbols “+” or “\$”.
- Negative Buffer - Negative 271 Health Care Eligibility Benefits Responses (non-Medicare). These responses have the eIV symbol “-”.
- Medicare Buffer – Positive, Negative or Ambiguous 271 Health Care Eligibility Benefits Responses. These responses may have any of the eIV symbols. (Refer to section 4.1.1 below.)
- Failure Buffer – Contains only non-Medicare records that have an eIV symbol of “!”
- ePharm Buffer – Contains insurance billable pharmacy data.
- TRICARE / CHAMPVA – Entries that contain the word TRICARE and / or CHAMPVA in the insurance company name.

## Status Flags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Buffer Symbols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc121848920" class="anchor"></span>Table 9: Buffer Entry Source of Information Indicators</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Flag</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>(blank)</td>
<td>Inquiry not yet sent</td>
</tr>
<tr class="even">
<td>+</td>
<td>Matching patient data was found at payer, payer indicates active policy</td>
</tr>
<tr class="odd">
<td>-</td>
<td>Matching patient data was found at payer, payer indicates expired policy</td>
</tr>
<tr class="even">
<td>#</td>
<td><p>eIV is unable to determine if payer indicates active or expired policy</p>
<p>OR</p>
<p>matching patient data was NOT found at payer</p>
<p>OR</p>
<p>response did not return requested value (may include an additional message with explanation)</p></td>
</tr>
<tr class="odd">
<td>%</td>
<td>Response returned the requested value</td>
</tr>
<tr class="even">
<td>?</td>
<td>Inquiry was sent, waiting for response</td>
</tr>
<tr class="odd">
<td>!</td>
<td>eIV was unable to send an inquiry for this entry. A manual correction is required before eIV can send inquiry. A descriptive error message will be displayed on the last screen of the expanded buffer entry.</td>
</tr>
<tr class="even">
<td>$</td>
<td>Buffer entry was escalated to user with appropriate security key.</td>
</tr>
</tbody>
</table>

<span id="_Toc121848920" class="anchor"></span>Table 9: Buffer Entry Source of Information Indicators

### Buffer Entry Status Flags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Flag | Meaning                                                   |
|----------|---------------------------------------------------------------|
| ~~d~~    | ~~Patient appears on more than one buffer view (Duplicate).~~ |

<span id="_Toc121848921" class="anchor"></span>Table 10: Insurance Entry Update Methods

### Patient Status Flags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Flag | Meaning                                                                          |
|----------|--------------------------------------------------------------------------------------|
| i        | Patient currently has active insurance on file                                       |
| I        | Patient is currently admitted as an inpatient                                        |
| E        | Patient is deceased (expired)                                                        |
| Y        | Patient is required to pay VA copayment for incurred charges according to Means Test |
| H        | Patient has charges on hold                                                          |

<span id="_Toc121848922" class="anchor"></span>Table 11: Acronyms / Abbreviations / Terms

### Buffer Entry Source of Information Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Letter | Meaning                    |
|------------|--------------------------------|
| I          | Interview                      |
| P          | Pre-Registration               |
| M          | Medicare                       |
| D          | Data Match                     |
| E          | eIV                            |
| R          | ICB Card Reader                |
| V          | IVM                            |
| H          | HMS                            |
| C          | Contract Services              |
| X          | e-Pharmacy                     |
| F          | Interfacility Insurance Update |
| T          | Insurance Import               |
| U          | Community Care Network         |
| B          | Purchased Care Fee-Basis       |
| O          | Purchased Care Other           |
| N          | Insurance Intake               |
| S          | Insurance Verification         |
| A          | Veteran Appt Request           |
| K          | Kiosk                          |
| J          | MYVA Health Journal            |
| W          | Electronic Health Record       |
| G          | Adv Med Cost Mgmt Solution     |

### Insurance Entry Update Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Letter | Meaning                                                                                                                                                                                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M          | Merge - Data from the buffer entry will be saved to the insurance entry ONLY if the corresponding data field in the insurance entry is blank.                                                                                                                         |
| O          | Overwrite - ALL non-blank data in the buffer entry will be saved to the insurance entry. If a buffer entry field has a value it will be saved to the corresponding insurance entry field. Blank insurance fields will be filled and existing insurance data replaced. |
| R          | Replace - ALL fields in the buffer entry will be saved to the insurance entry, including blank fields. Therefore all data in the insurance entry will be deleted then completely replaced by the buffer entry.                                                        |
| N          | No Change - This option may be used to identify the Insurance entry that corresponds to a buffer entry without actually changing any of the Insurance Information. The Buffer data is ignored.                                                                        |
| I          | Individually Accept - This option may be used to accept only non-blank specific fields from the buffer entry into the Insurance entry. Only those values accepted by the user will replace the corresponding fields in the Insurance entry.                           |

See Appendix B – eIV Error Message Descriptions for a detailed list of error messages associated with entries that were created because a 270 Health Care Eligibility Benefits Inquiry could not be transmitted.

## Buffer Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All views provide users the same actions for each buffer view.

13. Patients with no insurance on file will not be included in the nightly Buffer Extract.

These following actions are available in Process Insurance Buffer:

- PE – Process Entry
- RE – Reject Entry
- EE – Expand Entry
- AE – Add Entry
- ST – Sort List
- CC – Check Ins Co’s
- PB – Positive Buffer
- NB – Negative Buffer
- MB – Medicare Buffer
- FB – Failure Buffer
- RX – ePharm Buffer
- EX – Exit
- CB – Complete Buffer
- TC – TRICARE/CHAMPVA

These following actions are hidden, but available in Process Insurance Buffer:

- + – Next Screen
- – – Previous Screen
- UP – Up a Line
- DN – Down a Line
- \> – Shift view to Right
- \< – Shift view to Left
- FS – First Screen
- LS – Last Screen
- GO – Go to Page
- RD – Re Display Screen
- PS – Print Screen
- PL – Print List
- SL – Search List
- ADPL – Auto Display (On/Off)
- Q – Quit

### Process Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Processing an entry in a Buffer View results in updating the patient’s insurance and removing the entry from the buffer. Once users access Process Entry, they will have access to the following additional actions:

- Accept Entry – Allows users to update the patient’s insurance and remove the entry from the buffer
- Reject Entry – Allows users to remove the entry from the buffer without updating the patient’s insurance
- Compare Entry – Allows users to compare the data in the buffer with the data in the patient’s insurance
- Expand Entry – Allows users to Expand an Entry – Refer to Section 4.2.3
- Insurance Co / Patient – Allows users to view specific information about an insurance company’s available policies

To process an entry, complete the following steps:

1.  Access the PI Patient Insurance Menu.
38. Access the BI Process Insurance Buffer option.
14. The default Insurance Buffer view is the Positive Insurance Buffer and users can move between views using the action for each view.

    Some actions such as Reject Entry are only available to users who hold the IB INSURANCE SUPERVISOR key.

The following screen will be displayed:

Complete Buffer Oct 19, 2015@16:16:01 Page: 1 of 2

Sorted by: Patient Name

Patient Name Insurance Company Subscr Id S Entered iIEYH

1 !IBPATIENT,ONE XXXX IBINSURANCE,ONE SUB ID XXXX E 10/01/15 iI

2 !IBPATIENT,TWO XXXX IBINSURANCE,ONE SUB ID XXXX E 09/10/15

3 !IBPATIENT,THREE XXXX IBINSURANCE,ONE SUB ID XXXX E 09/10/15

4 !IBPATIENT,FOUR XXXX IBINSURANCE,TWO SUB ID XXXX P 09/10/15

5 !IBPATIENT,FIVE XXXX IBINSURANCE,FOUR SUB ID XXXX P 09/10/15

6 !IBPATIENT,SIX XXXX IBINSURANCE,FOUR SUB ID XXXX P 09/03/15

7 !IBPATIENT,SEVEN XXXX IBINSURANCE,FOUR SUB ID XXXX P 09/10/15

8 !IBPATIENT,EIGHT XXXX IBINSURANCE,FIVE SUB ID XXXX P 09/10/15

9 !IBPATIENT,NINE XXXX IBINSURANCE,ONE SUB ID XXXX I 09/09/15

10 !IBPATIENT,TEN XXXX IBINSURANCE,SIX SUB ID XXXX I 09/30/15

11 !IBPATIENT,ELEVEN XXXX IBINSURANCE,TWO SUB ID XXXX I 10/01/15 I

12 !IBPATIENT,TWELVE XXXX IBINSURANCE,TWO SUB ID XXXX P 10/01/15 i H

13 ?IBPATIENT,THIRTEEN XXXX IBINSURANCE,ONE SUB ID XXXX E 09/30/15 Y

14 !IBPATIENT,FOURTEEN XXXX IBINSURANCE,TWO SUB ID XXXX P 09/30/15 i H

15 !IBPATIENT,FIFTEEN XXXX IBINSURANCE,FOUR SUB ID XXXX I 09/30/15 i Y

\+ Enter ?? for more actions

PE Process Entry ST Sort List MB Medicare Buffer CB Complete Buffer

RE Reject Entry CC Check Ins Co's FB Failure Buffer TC TRICARE/CHAMPVA

EE Expand Entry PB Pos. Buffer RX ePharm Buffer

AE Add Entry NB Neg. Buffer EX Exit

Select Action: Next Screen//

39. At the Select Action: prompt, enter PE for Process Entry.
40. At the Select Buffer Entry(s): (1-15): prompt, enter 1 for this example.

The following screen will be displayed:

Insurance Buffer Process May 21, 2010@10:21:24 Page: 1 of 1

IBpatient,One XXX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

IBinsurance One (P.O. BOX 555555, ANYCITY, OH)

\- IBinsurance One GRP NUM 11269 PATIEN 10/01/00

Patient's Existing Insurance

Insurance Company Group \# Subscriber Id Holder Effective Expires

1 IBinsurance Two GRP NUM 11269 SUB ID XXXX PATIEN 04/01/95 10/01/00

Any Group/Plan that may match Group Name or Group Number

Insurance Company Group Name Group Number

2 IBinsurance Two PO BOX 740800 XXXXX GRP NUM XXXX

3 IBinsurance Two PO BOX 740800 XXXXX GRP NUM XXXXX

Enter ?? for more actions

AE Accept Entry CE Compare Entry VP Insurance Co/Patient

RE Reject Entry EE Expand Entry EX Exit

Select Action: Quit//

41. At the Select Action: prompt, enter AE for Accept Entry.
42. At the Select Company/Policy: (1-3): prompt, enter 1 for this example.

The following screen will be displayed:

Insurance Data: Buffer Data Selected Insurance Company

Company Name: TEST-1 \| BLUE CROSS

Reimburse?: \| WILL REIMBURSE

Phone Number: \|

Billing Phone: \| 877.277.3368

Pre-Cert Phone: \| 877.277.3368

Street \[Line 1\]: \| 123 HERE

Street \[Line 2\]: \|

Street \[Line 3\]: \|

City: \| ANYTOWN

State: \| CALIFORNIA

Zip Code: \| 99999

(bold=accepted on Merge) \| (bold=replaced on Overwrite)

Is this the correct INSURANCE COMPANY to match with this Buffer entry? YES

Select the method to update the INSURANCE COMPANY: (M/O/R/N/I): NO CHANGE

43. At the Is this the correct INSURANCE COMPANY to match with this Buffer entry? Prompt, enter YES.
44. At the Select the method to update the INSURANCE COMPANY: (M/O/R/N/I): prompt, always enter N.
15. VistA has no control over the information that the payers return, so by selecting N, the details about the payer in the VistA insurance file will not be changed.

The following screen will be displayed:

Patient is a member of this Insurance Group/Plan

Group/Plan Data: Buffer Data Selected Group/Plan

Company Name: TEST-1 \| BLUE CROSS

Is Group Plan?: \| YES

Group Name: \| BLUE CROSS OF CA

Group Number: \| 3485

BIN: \|

PCN: \|

Require UR: \| NO

Require Pre-Cert: \|

Require Amb Cert: \|

Exclude Pre-Cond: \|

Benefits Assign: \| YES

Type of Plan: \| ACCIDENT AND HEALTH INSURANCE

(bold=accepted on merge) \| (bold=replaced on overwrite)

Is this the correct GROUP/PLAN to match with this Buffer entry? YES

Select the method to update the GROUP/PLAN: (M/O/R/N/I): NO CHANGE

45. At the Is this the correct Group Plan to match with this Buffer entry? Prompt, enter YES.
46. At the Select the method to update the Group Plan: (M/O/R/N/I): prompt, enter N.
16. VistA has no control over the information that the payers return, so by selecting N the details about the payer in the VistA insurance file will not be changed.

The following screen will be displayed

Do you want to Review the AB Y/N? No// YES

Benefit year:

JAN 01, 2001

JAN 20, 2001

JAN 01, 2002

JAN 01, 2016

FEB 05, 2012

FEB 09, 2015

Enter Existing Date or Add New Benefit Year: JAN 1, 2001 (JAN 01, 2001)

47. At the Do you want to Review the AB Y/N? prompt, enter YES.
48. At the Enter the Existing Data or Add New Benefit Year prompt, enter the JAN 01, 2001 for this example.

The follow screen will be displayed:

Annual Benefits Data

Benefit Year : JAN 01, 2001

Policy Information : BLUE CROSS

Max Out of Pocket : 33.33

Ambulance Coverage(%) : 9

Inpatient:

Annual Deductible : 23

Per Admis Deduct : 2

Inpt. Lifetime Max : 100

Inpt. Annual Max : 68

Room & Board (%) : 34

Drug/Alcohol Lifet. Max : 67.00

Drug/Alcohol Annual Max : 02

Nursing Home (%) : 44

Other Inpt. Charges (%) : 77

Outpatient:

Annual Deductible : 38.89

Per Visit Deductible : 56.12

Enter RETURN to continue or '^' to exit:

Lifetime Max : 69.99

Annual Max : 99.00

Visit (%) : 50

Max Visits Per Year : 4

Surgery (%) : 67

Emergency (%) : 23

Prescription (%) : 98

Adult Day Health Care? : YES

Dental Cov. Type : PERCENTAGE AMOUNT

Dental Cov. (%) : 69

Mental Health Inpatient:

MH Inpt. Max Days/Year : 89

MH Lifetime Inpt. Max : 56.32

MH Annual Inpt Max : 48

Mental Health Inpt. (%) : 5

Mental Health Outpatient:

MH Opt. Max Days/Year : 92

MH Lifetime Opt. Max : 42

Enter RETURN to continue or '^' to exit:

MH Annual Opt. Max : 78

Mental Health Opt. (%) : 4

Home Health Care:

Care Level : THERAPIST/OTHER

Visits Per Year : 56

Max. Days Per Year : 89

Med. Equipment (%) : 50

Visit Definition : CHECK-UP

Hospice:

Annual Deductible : 10.00

Inpatient Annual Max. : 25.00

Inpatient Lifetime Max. : 100.00

Room and Board (%) : 30

Other Inpt. Charges (%) : 1

Rehabilitation:

OT Visits/Yr : 93

PT Visits/Yr : 99

Enter RETURN to continue or '^' to exit:

ST Visits/Yr : 92

Med Cnslg Visits/Yr : 94

IV Management:

IV Infusion Opt? : YES

IV Infusion Inpt? : YES

IV Antibiotics Opt? : YES

IV Antibiotics Inpt? : YES

Are you sure you want to edit existing benefit year information for: JAN 1,2001 Y/N?: YES

49. At the Are you sure you want to edit the existing benefit year information for \<date\> Y/N prompt, enter the YES.

The following screen will display:

----------------------- EDIT ANNUAL BENEFITS INFORMATION -----------------------

Benefit Year : JAN 1,2001//

Policy Information : BLUE CROSS//

Max Out of Pocket : 33.33// 80.00

Ambulance Coverage(%) : 9//

Inpatient:

Annual Deductible : 23//

Per Admis Deduct : 2// ^

Save Changes to Annual Benefits File Y/N? No// NO

Do you want to Review the AB Y/N? No// NO

50. At the Save Changes to Annual Benefits File Y/N? prompt, enter NO.
51. At the Do you want to review the AB Y/N prompt, enter N.
52. At the Do you want to Review the CV Y/N? prompt, enter YES.

The following screen will be displayed:

Do you want to Review the CV Y/N? No// YES

Coverage Date:

JAN 01, 1995

JAN 01, 2002

APR 08, 2015

APR 10, 2015

APR 20, 2015

APR 25, 2015

SEP 01, 2005

SEP 25, 2005

SEP 22, 2014

SEP 25, 2015

OCT 01, 2003

NOV 01, 2003

DEC 25, 2011

DEC 31, 2015

Enter Existing Date or Add New Coverage Date: JAN 01,1995 (JAN 01, 1995)

53. At the Enter Existing Date or Add New Coverage Date prompt, enter the JAN 01, 2001 for this example.

The following screen will be displayed:

Coverage Limitations Data

INPATIENT:

Inpatient Coverage : COVERED

Inpatient Date of Coverage : JAN 01, 1995

Inpatient Limit Comments : test

OUTPATIENT:

Outpatient Coverage :

Outpatient Date of Coverage :

Outpatient Limit Comments :

PHARMACY:

Pharmacy Coverage :

Pharmacy Date of Coverage :

Pharmacy Limit Comments :

DENTAL:

Dental Coverage :

Dental Date of Coverage :

Dental Limit Comments :

Enter RETURN to continue or '^' to exit:

Coverage Limitations Data

MENTAL HEALTH:

MH Health Coverage :

MH Health Date of Coverage :

MH Health Limit Comments :

LONG TERM CARE:

Long Term Coverage :

Long Term Date of Coverage :

Long Term Limit Comments :

Are you sure you want to Edit existing Coverage Date information: JAN 1,1995 Y/N

?: NO

Do you want to Review the CV Y/N? No// NO

54. At the Are you sure you want to edit existing Coverage Date information Y/N? prompt, enter NO.
55. At the Do you want to Review the CV Y/N prompt, enter N.

The following screen will be displayed:

Policy Data: Buffer Data Selected Policy

Company Name: TEST-1 \| BLUE CROSS

Group \#: 3458 \| 3485

Patient Name: IBPATIENT, ONE \| IBPATIENT,ONE

Last Verified: \| APR 23, 2015

Effective Date: MMM DD, YYYY \| JAN 01, 2015

Expiration Date: \| JAN 01, 2040

Subscriber Id: \| 123456789

Whose Insurance: \| VETERAN

Relationship: \| PATIENT

Rx Relationship: \| 0

Rx Person Code: \| 001

Subscriber Name: \| IBTEST,EB

Subscriber's DOB: MMM DD, YYYY \| MMM DD, YYYY

Subscriber's SSN: \| XX-XX-XXXX

Subscriber's SEX: \| FEMALE

Primary Provider: \| IBDOCTOR,ONE

Provider Phone: \| (555)515-5555

Coor of Benefits: \| SECONDARY

Emp Sponsored?: \| YES

Patient Id: \| 7654321

Subscr Str Ln 1: \| 936 Little Street

Subscr Str Ln 2: \| Suite 17

Subscr City: \| ANYWHERE

Subscr State: \| NEW YORK

Subscr Zip: \| 11111

Subscr Country: \| USA

Subscr Subdiv: \| 321

Subscr Phone: \| (111)111-111

Subscriber Id: XXXXXXXXXX \| XXXXXXXXXX

Enter RETURN to continue:

Employer Name: \| Cognitive Solutions

Emp Status: \|

Retirement Date: \|

Send to Employer: \|

Emp Street Ln 1: \| 1 Alpha Lane

Emp Street Ln 2: \| Galaxy Suite

Emp Street Ln 3: \|

Emp City: \| ANYTOWN

Emp State: \| CALIFORNIA

Emp Zip Code: \| 99999

Emp Phone: \|

(bold=accepted on merge) \| (bold=replaced on overwrite)

Is this the correct PATIENT POLICY to match with this Buffer entry? YES

Select the method to update the PATIENT POLICY: (M/O/R/N/I): INDIVIDUALLY ACCEP

T (SKIP BLANKS)

Select the Patient Relationship to Subscriber: 01 SPOUSE

56. At the Is this the correct Patient Policy to match with this Buffer entry? Prompt, enter YES.
57. At the Select the method to update the Patient Policy: (M / O / R / N / I): prompt, enter I.
17. VistA has no control over the information that the payers return, so by selecting I, the user has full control over the details that are changed in the VistA insurance file.

The following screen shows the prompts to Accept, Change, or Replace entries:

Policy Data: Buffer Data Selected Policy

Company Name: TEST-1 \| BLUE CROSS

Group \#: 3485 \| 3485

Patient Name: IBPATIENT, ONE \| IBPATIENT,ONE

Last Verified: \| APR 23, 2015

Effective Date: MMM DD, YYYY \| JAN 01, 2015

Accept Change, Replace? No// NO

Expiration Date: \| JAN 01, 2040

Subscriber Id: \| 123456789

Whose Insurance: VETERAN \| VETERAN

Relationship: PATIENT \| PATIENT

Rx Relationship: \| 0

Rx Person Code: \| 001

Subscriber Name: \| IBTEST,EB

Subscriber's DOB: MMM DD, YYYY \| MMM DD, YYYY

Accept Change, Replace? No// NO

Subscriber's SSN: \| XX-XX-XXXX

Subscriber's SEX: \| FEMALE

Primary Provider: \| IBDOCTOR,ONE

Provider Phone: \| (555)555-5555

Coor of Benefits: \| SECONDARY

Emp Sponsored?: \| YES

Patient Id: \| XXXXXX

Subscr Str Ln 1: \| 123 Main Street

Subscr Str Ln 2: \| Suite XX

Subscr City: \| ANYWHERE

Subscr State: \| NEW YORK

Subscr Zip: \| 11111

Subscr Country: \| USA

Subscr Subdiv: \| 321

Subscr Phone: \| (111)111-1111

Subscriber Id: XXXXXXXXXX \| XXXXXXXXXX

Accept Change, Replace? No// NO

Employer Name: \| Employer’s Name

Emp Status: \|

Retirement Date: \|

Send to Employer: \|

Emp Street Ln 1: \| 123 Main Street

Emp Street Ln 2: \| Galaxy Suite

Emp Street Ln 3: \|

Emp City: \| ANYTOWN

Emp State: \| CALIFORNIA

Emp Zip Code: \| 99999

Emp Phone: \|

(bold=accepted on merge) \| (bold=replaced on overwrite)

End of changes for POLICY related data.

Enter RETURN to continue or '^' to exit:

Select the Patient Relationship to Subscriber: 01 SPOUSE

58. At the Select the Patient Relationship to Subscriber prompt, enter the 01 SPOUSE for this example.

Subscriber Data: Patient Registration Patient Insurance Policy

Subscriber Id: XXXXXX \| XXXXXXXX

Whose Insurance: VETERAN \| VETERAN

Relationship: SELF \| SELF

Rx Relationship: 1 - NOT SPECIFIED \| 0

Rx Person Code: 001 \| 001

Subscriber Name: IBTEST,EB \| IBTEST,EB

Subscriber's DOB: NOV 04, 1939 \| NOV 04, 1939

Subscriber's SSN: XX-XX-XXXX \| XX-XX-XXXX

Subscriber's SEX: MALE \| MALE

Primary Provider: IBPROVIDER, ONE \| IBPROVIDER, TWO

Provider Phone: (222)222-2222 \| (555)555-5555

Coor of Benefits: PRIMARY \| SECONDARY

Patient Id: \| 2345678

Subscr Str Ln 1: 123 Main Street \| 123 Main Street

Subscr Str Ln 2: \| Suite XX

Subscr City: ANYWHERE \| ANYWHERE

Subscr State: NEW YORK \| NEW YORK

Subscr Zip: 99999 \| 11111

Subscr Country: USA \| USA

Subscr Phone: 777-777-7777 \| (444)444-4444

(bold=accepted on merge) \| (bold=replaced on overwrite)

Is this the correct SUBSCRIBER INSURANCE to match with this Patient Registration

entry? YES

Select the method to update the SUBSCRIBER INSURANCE: (M/O/R/N/I): NO CHANGE

18. Eligibility / benefit data groups may be available on multiple pages. To scroll through each page, enter RETURN. To skip to the last page, enter ^.
59. At the Is this the correct SUBSCRIBER INSURANCE to match with this Patient Registration entry? prompt, enter YES.
60. At the Select the method to update the SUBSCRIBER INSURANCE: (M/O/R/N/I): prompt, enter N.
19. VistA has no control over the information that the payers return, so by selecting N, the user has full control over the details that are changed in the VistA insurance file.

\*\*\* Non-editable Patient Eligibility/Benefit data from payer \*\*\*

Payer Response VISTA Pt.Insurance

<u>Eligibility Information</u>

Subscriber: IBpatient,One \|

Subscriber Id: XXXXXXXXX \|

Subscriber DOB: XXXXXXXX \|

Subscriber SSN: XXXXXXXX \|

Group Name: XXXXXXX \|

Group ID: XXXXXXXXXXXXX \|

Whose Insurance: VETERAN \|

Pt.Rel. to Subscriber: PATIENT \|

Member ID: \|

COB: \|

Service Date: \|

Effective Date: XXX XX, XXXX \|

Certification Date: \|

Expiration Date: \|

Payer Updated Policy: \|

Response Date: XXX XX, XXXX \|

Trace \#: \|

Policy Number: \|

\|

Contact Information \| Contact Information

Eligibility/Group Plan Information

Reference ID Qualifier: \| Reference ID Qualifier:

Reference ID: \| Reference ID:

Reference ID description: \| Reference ID description:

\|

Provider Code: \| Provider Code:

Reference ID: \| Reference ID:

\|

Primary Diagnosis Code: \| Primary Diagnosis Code:

Secondary Diagnosis Code: \| Secondary Diagnosis Code:

\|

Military Info Status: \| Military Info Status:

Employment Status: \| Employment Status:

Government Affiliation: \| Government Affiliation:

Date Time Period: \| Date Time Period:

Service Rank: \| Service Rank:

Desc: \| Desc:

\|

Summary of eIV Eligibility/ \|

\| No eIV Eligibility/Benefi

Coverage Status: ACTIVE \| No eIV Eligibility/Benefi

Insurance Type: BLUE CROSS \| No eIV Eligibility/Benefi

eIV Eligibility/Benefit Data Group# 1 of 7

\|

Eligibility/Benefit Information

Elig/Ben Info: Active Coverage \|

Coverage Level: Individual \|

Date/Time Qual: \|

D/T Period: \|

Service Type: \|

Time Period: \|

Insurance Type: Medicare Part A \|

Plan Coverage Desc: \|

Benefit Amount: \|

Benefit %: \|

Quantity Qual: \|

Quantity Amount: \|

Auth/Certification Required: \|

In-Plan-Network: \|

\|

Enter RETURN to continue or '^' to exit: ^

Replace the Pt's Eligibility/Benefits data? YES//

61. At the Replace the Pt’s Eligibility/Benefits data? prompt, enter YES.

The following screen will be displayed:

STEP 1: Insurance Company

There will be NO CHANGE to the existing Insurance Company data.

STEP 2: Group/Plan

There will be NO CHANGE to the existing Group/Plan data.

STEP 3: Annual Benefits

No Edits made/saved. No data saved into the Annual Benefits File.

STEP 4: Coverage Limitation

No Edits made/saved. No data saved into the Coverage Limitations File.

STEP 5: Patient Policy

The Buffer data will INDIVIDUALLY ACCEPT (SKIP BLANKS) the existing Policy data.

STEP 6: Subscriber Update

There will be NO CHANGE to the existing Patient Insurance data.

STEP 7: Eligibility/Benefits

The Buffer data will replace the existing EB data.

Is this Correct, update the existing Insurance files now? YES ...

Patient Policy Updated...

> **WARNING:** Insurance Company selected already on file for this patient.

The previous entry is active.

The WHOSE INSURANCE are the same.

The Group Plans are the same.

Press 'V' to view the changes or Return to continue:

62. If you want to review the changes that were made when you chose Individually Accept, at the Press 'V' to view the changes or Return to continue: prompt, press RETURN for this example.
20. Users may select more than one entry from the buffer at a time to process. The system will then cycle users through each selected entry.

### Reject Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can remove an entry from the Buffer by rejecting the entry.

1.  At the Select Action: prompt, enter RE for Reject Entry.
63. At the Select Buffer Entry(s): (1-17): prompt, enter 12 for this example.

The following screen will be displayed:

--------------------------------------------------------------------------------

Entered: 9/9/09@13:46 Source: INTERVIEW

Entered By: IBclerk,One Verified:

Patient: IBpatient,Twelve Sub Id: XXXXXX

Insurance: IBinsurance Five Group \#: XXXXX-XX

--------------------------------------------------------------------------------

This action will delete all insurance and patient specific data from a buffer

entry without first saving that data to the insurance files, leaving a stub

entry for reporting purposes.

Reject this buffer entry (delete without saving to Insurance files)? N// Y

64. At the Reject this buffer entry (delete without saving to Insurance files)? N// prompt, enter YES to remove entry from the buffer.
21. Users may select more than one entry from the buffer at a time to reject. The system will then cycle users through each entry prompting them to reject each selected entry.

### Expand Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can Expand an Entry. Expanding an entry will cause the following categories of information to be displayed:

- Insurance Company Information
- Group / Plan Information
- Policy / Subscriber Information
- Buffer Entry Information

To Expand an Entry, follow these steps:

1.  Access the BI Process Insurance Buffer.
65. At the Select Action: prompt, enter EE for Expand Entry.
66. At the Select Buffer Entry(s): (1-17): prompt, enter 1 for this example and page through the screens.

The following screens will be displayed:

Insurance Buffer Entry Jul 23, 2013@17:16:47 Page: 1 of 4

IBpatient,One XXX-XX-XXXX DOB: XXX XX, XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Insurance Company Information

Name: XYZ INS Reimburse?: WILL REIMBURSE

Phone: Billing Phone:

Precert Phone:

Remote Query From:

Address:

Group/Plan Information

Group Plan?: Yes

Group Name: TEST1

Group Number: INS1234

BIN: Require UR: No

PCN: Require Amb Cert: No

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen//

Insurance Buffer Entry Jul 23, 2013@17:19:39 Page: 2 of 4

IBpatient,One XXX-XX-XXXX DOB: XXX XX, XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Require Pre-Cert: No

Type of Plan: COMPREHENSIVE MAJOR MEDIC Exclude Pre-Cond: No

Benefits Assignable: Yes

Policy/Subscriber Information

Whose Insurance: SPOUSE Effective: 07/01/01

Expiration:

Subscriber's Name: IBINS,ACTIVE

Subscriber Id: XXXX

Relationship: SPOUSE Primary Provider:

Provider Phone:

Subscriber's DOB: XX/XX/XX Coord of Benefits:

Patient Id: XXXXXX

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

Insurance Buffer Entry Jul 23, 2013@17:20:17 Page: 3 of 4

IBpatient,One XXX-XX-XXXX DOB: XXX XX, XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK, IB (INTERVIEW)

+----------------------------------------------------------------------------

Employer Sponsored Group Health Plan?:

Buffer Entry Information

Date Entered: 7/5/13@09:05 Date Verified:

Entered By: CLERK,IB Verified By:

\*\* This response is based on service date XX/XX/XXXX and service type: Health

Benefit Plan Cov \*\*

eIV Trace \#: xxxxxxxxx eIV Processed Date: 7/5/13@09:38

Source: INTERVIEW

Current eIV Status: Response Received, Active Policy

Information received via electronic inquiry indicates patient has active

insurance.

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

Insurance Buffer Entry Jul 23, 2013@17:20:26 Page: 4 of 4

IBpatient,One XXX-XX-XXXX DOB: XXX XX. XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB(INTERVIEW)

+----------------------------------------------------------------------------

Action to take: Review the details listed in the eIV Response Report

before processing this buffer entry.

----------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Quit//

Once users access Expand Entry, they will have access to the following additional Actions:

- Ins. Co. Edit – Allows users to edit or change the Insurance Company.
- All edit– Allows users to edit each of the Expand Entry categories.
- Group/Plan Edit - Allows users to edit the Group/Plan category.
- Escalate Entry – Allows users to escalate an entry, to indicate to other buffer users that the record needs to be processed by someone else with more rights. Only active policies may be ‘Escalated’. Also, not all users may ‘Escalate’ a buffer record. Those users who do not have the IB INSURANCE COMPANY EDIT security key and the IB GROUP PLAN EDIT security key will be the only ones authorized to use this ‘Escalate’ action. These users are restricted to accessing only certain positive “+” buffer entries.
- Pt. Policy Edit – Allows users to edit the Policy/Subscriber category.
- Expand Benefits – Allows users to see the Eligibility/Benefits data that was returned in the associated 271 Health Care Eligibility Benefits Response if there is one for this entry.

### Add Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add Entry action, allows users to manually add a patient to the insurance buffer.

1.  At the Select Action: prompt, enter AE for Add Entry.
67. At the Select PATIENT NAME: prompt, enter IBpatient,Thirteen for this example.

The following screen will be displayed:

Select PATIENT NAME: IBpatient,Thirteen X-X-XX XXXXXXXXX YES SC VETERAN

Enrollment Priority: Category: NOT ENROLLED End Date:

Financial query queued to be sent to HEC...

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from APR 15,1999

Enter \<RETURN\> to continue.

MEANS TEST REQUIRED

68. Follow the prompts shown below to enter the insurance company, group/plan and policy, and subscriber information.
69. When you have added an entry to the insurance buffer, you will be returned to the Complete Buffer.

Insurance Company: ??

Please enter the name of the insurance company that provides coverage for this

patient. This response is a free text response, however, a partial insurance

company name look-up is available here.

Insurance Company: IBinsurance

1 IBinsurance One

2 IBinsurance Two

3 IBinsurance Three

4 IBinsurance Four

5 IBinsurance Five

CHOOSE 1-5: 2

Add a new Insurance Buffer entry for this patient and company? YES//

------------------------ INSURANCE COMPANY INFORMATION -------------------------

INSURANCE COMPANY NAME: IBinsurance Two//

1 IBinsurance Two

CHOOSE 1-1: 1

REIMBURSE?:

PHONE NUMBER:

BILLING PHONE NUMBER:

PRECERTIFICATION PHONE NUMBER:

STREET ADDRESS \[LINE 1\]:

CITY:

STATE:

ZIP CODE:

---------------------------- GROUP/PLAN INFORMATION ----------------------------

The following data defines a specific Group or Plan provided by an Insurance

Company. This may be either a group plan with many potential members or an

individual plan with a single member.

IS THIS A GROUP POLICY?: N NO

GROUP NAME:

GROUP NUMBER:

BANKING IDENTIFICATION NUMBER:

PROCESSOR CONTROL NUMBER (PCN):

TYPE OF PLAN:

UTILITZATION REVIEW REQUIRED:

PRECERTIFICATION REQUIRED:

AMBULATORY CARE CERTIFICATION:

EXCLUDE PREEXISTING CONDITION:

BENEFITS ASSIGNABLE:

---------------------- POLICY AND SUBSCRIBER INFORMATION -----------------------

The following data defines the subscriber specific policy information for a

particular Insurance Plan. The subscriber, the insured, and the policy holder

all refer to the person who is a member of the plan and therefore holds the

policy. The patient must be covered under the plan but may not be the policy

holder.

EFFECTIVE DATE:

EXPIRATION DATE:

PT. RELATIONSHIP TO SUBSCRIBER:

NAME OF SUBSCRIBER:

SUBSCRIBER'S DOB:

SUBSCRIBER'S SEX:

PATIENT PRIMARY ID:

PRIMARY CARE PROVIDER:

PRIMARY PROVIDER PHONE:

COORDINATION OF BENEFITS:

SOURCE OF INFORMATION: INTERVIEW//

ESGHP?:

SUBSCRIBER ADDRESS LINE 1:

SUBSCRIBER ADDRESS LINE 2:

SUBSCRIBER ADDRESS CITY:

SUBSCRIBER ADDRESS STATE:

SUBSCRIBER ADDRESS ZIP: .......................................................\|

### Sort Buffer Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default sort for all Buffer views (except the Positive Insurance Buffer) is alphabetically by patient name. The Positive Insurance Buffer is sorted by “+” eIV Status first and then alphabetically by patient name.

Users may re-sort the buffer based upon the following criteria:

- Patient Name
- Insurance Company
- Source of Information
- Date Entered
- Inpatients
- Means Test
- On Hold
- eIV Status
- Positive Response

### Check Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may view a list of insurance companies that exist in the insurance buffer that do not match any of the insurance company names or synonyms in the insurance company file. These insurance companies do not match any entries in the IIV AUTO MATCH file.

Once users select the Check Ins Co's action, they will have access to the following actions (Refer to Section 7 Auto Match):

- Select Entry
- Auto Match Enter/Edit

To view a list of insurance companies, follow these steps:

1.  Access the BI Process Insurance Buffer.
70. At the Select Action: prompt, enter CC for Check Ins Co's.

The following screen will be displayed.

Unmatched Buffer Names Jul 07, 2010@12:02:54 Page: 1 of 1

These are Insurance Company names from the Insurance Buffer file that do not

exist in the Insurance Company file (either as Names or as Synonyms). They

also do not exist or pattern match with any entry in the Auto Match file.

1 IBinsurance Onee

2 IBinsurance Twu

3 IBinsurance Threee

Enter ?? for more actions

Select Entry Auto Match Enter/Edit Exit

Select Action: Next Screen//

22. Each buffer entry that fails to make any match to an entry in the Insurance Company file (#36) or the IIV AUTO MATCH file (#365.11) is presented to the user.

    This example sets up an auto match entry to associate IBinsurance Twu with IBinsurance Two.
71. At the Select Action: prompt, enter SE for Select Entry.
72. At the Select Entry: (1-192): prompt select 2 for IBinsurance Twu.
73. At the Select INSURANCE COMPANY NAME: prompt enter IBinsurance Two.

The following screen will be displayed.

Select INSURANCE COMPANY NAME: IBinsurance Two

1 IBinsurance Two SAMPLE RD MYTOWN OHIO Y

2 IBinsurance Two TEST RD MYTOWN MICHIGAN Y

3 IBinsurance Two PO BOX 5555 ANYTOWN NEW YORK Y

CHOOSE 1-3: 1 IBinsurance Two SAMPLE RD MYTOWN OHIO Y

74. At the CHOOSE 1-3: prompt in this example, enter 1 for IBinsurance Two SAMPLE RD.
75. At the Do you want to add an Auto Match entry that associates IBinsurance Twu with IBinsurance Two? No//: prompt, enter YES.

The following prompts are displayed along with a confirmation message.

Do you want to add an Auto Match entry that associates

IBinsurance Twu with IBinsurance Two? No// Y YES

AUTO MATCH VALUE: IBinsurance Twu //

IBinsurance Twu is now associated with IBinsurance Two.

### Buffer Views: Complete, Positive, Negative, Medicare, Failure, ePharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may switch back and forth between the different available Buffer Views by selecting one of the following actions:

- PB – Pos. Buffer
- NB – Neg. Buffer
- MB – Medicare Buffer
- FB – Failure Buffer
- CB – Complete Buffer
- RX – ePharm Buffer
- TC – TRICARE / CHAMPVA

### AAA Errors – Complete Buffer View, Expand Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may view the Error Reporting Codes and corresponding textual descriptions in the Expand Entry when an Error Reporting Code is received in response to an associated 270 Health Care Eligibility Benefits entry.

1.  Access the BI Process Insurance Buffer.
76. At the Select Action: prompt, enter EE to expand an entry that has a “#”.
23. Any AAA error messages listed in the Buffer entry.

The AAA errors are displayed as shown in the following sample Expand Entry when accessed from within the Process Insurance Buffer option:

Insurance Buffer Entry May 07, 2013@13:26:09 Page: 4 of 4

IBPATIENT,ONE XXX-XX-XXXX DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 05/07/13 by IBCLERK,ONE (eIV)

\+

Action to take: Review the details listed in the eIV Response Report and

contact the insurance company to manually verify this insurance

information.

Eligibility Communicator Error Information

Invalid/Missing Subscriber/Insured ID (Error Condition '72')

Please Correct and Resubmit (Error Action 'C')

Enter ?? for more actions

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Quit//

The AAA errors listed will be identical whether displayed on the Expand Entry screen within the Insurance Buffer or the Response Report called from the eIV Menu.

eIV Response Report

Insurance verification responses are received daily.

Please select a date range in which responses were received to view the

associated response detail. Otherwise, select a Trace \# to view specific

response detail.

Select one of the following:

1 Report by Date Range

2 Report by Trace \#

Select the type of report to generate: 1// 2 Report by Trace \#

Enter Trace \# for report:

Enter Trace \# for report: XXXXXXXXXXXXXXXXXX xxxxx,xxxxxx IBINSURANCE2

...OK? Yes// y (Yes)

DEVICE: HOME// Linux Telnet/SSH

Compiling report data ...

The AAA errors are displayed as shown in the following sample Response Report when accessed from the eIV Menu:

eIV Response Report by Trace \# May 07, 2013@11:48:22 Page:1

Trace \#: XXXXXXXXX

Payer: IBINSURANCE2

Patient: IBpatient,One (SSN: XXX-XX-XXXX DOB: XX/XX/XXXX

Subscriber: IBPATIENT, ONE

Subscriber ID:

Subscriber DOB: XX/XX/XXXX

Subscriber SSN: Subscriber Sex: M

Group Name:

Group ID:

Whose Insurance: VETERAN PATIENT

Member ID: COB:

Service Date: Date of Death:

Effective Date: Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: XX/XX/XXXX Trace \#: XXXXXXXXX

ERROR INFORMATION:

Reject Reason Code: 72

Reject Reason Text: Invalid/Missing Subscriber/Insured ID

Action Code: C

Action Code Text: Please Correct and Resubmit

HIPAA Loop: Subscriber Name

HL7 Location: N/A

Error Source: P

# Medicare Potential Insurance Worklist – Potential COB Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may create a worklist of those patients Medicare has identified in a 271 HL7 response message as having insurance subsequent to their Medicare insurance.

1.  Access the Integrated Billing MasterMenu.
77. Select the PI Patient InsuranceMenu.
78. Select the EIV eIV MENU.
79. Select the MW Medicare Potential COB Worklist option.
80. Accept all default answers to the prompts for Earliest Report Date, Latest Report Date, and Sort Report By.
81. Select either S “Screen List” or R “Report” for the format type.
24. This is new for patch IB\*2\*497.

### Search Criteria – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may search for patients whom Medicare has identified in a 271 HL7 response message as having insurance subsequent to their Medicare insurance based on the following:

- Earliest Date 271 HL7 message received
- Latest Date 271 HL7 message received

### Sort Criteria – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may sort entries for patients whom Medicare has identified as having insurance subsequent to their Medicare insurance:

- Chronological Order
- Reverse Chronological Order

### Format – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may select one of the following formats for the list of patients whom Medicare has identified as having insurance subsequent to their Medicare insurance:

- Report (refer to report section for more details)
- ListManager

### Screen ListManager for Completed Entries – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ListManager view of patients whom Medicare has identified as having insurance subsequent to their Medicare insurance does not display completed entries.

### ListManager – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may perform the following actions from within the list of patients whom Medicare has identified as having insurance subsequent to their Medicare insurance:

- Mark entry as Not Reviewed
- Mark entry as Review in Process
- Mark entry as Review Complete
- Enter Comments
- View Comments

### Comments – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system captures the following information when users enter comments to an entry on the list of patients whom Medicare has identified as having insurance subsequent to their Medicare Insurance:

- User Name
- Date
- Time

### Visual Indicators – Potential COB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides visual indicators for entries on the list of patients whom Medicare has identified as having insurance subsequent to their Medicare insurance for the following conditions:

- Entries as Not Reviewed
- Entries marked as Review in Process
- Entries marked as Review Complete (can only be seen on the report format)
- Entries the system thinks, based on exact match of insurance company name and address, already exist in the Patient’s Insurance.

# Request Electronic Insurance Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows users to create a Health Care Eligibility Benefits Inquiry whenever needed. In addition this option also allows a user to create an Electronic Insurance Coverage Discovery (EICD) inquiry when needed.

25. Users must hold the IBCNE IIV SUPERVISOR security key to access this option.

## Request a 270 Health Care + Benefits Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Request Electronic Insurance Inquiry option allows users to create a Health Care Eligibility Benefits Inquiry whenever needed. This option allows users to override the re-verification of Service Date of today and individually select a specific Service Type Code. If no code is selected, the default of Service Type Code as set in the IV Site Parameters is used, typically it is set to 30. Using the default Service Type Code to create a buffer entry allows the entry to auto-update. Selecting any other Service Type code during this process will bypass the auto-update feature, leaving the buffer entry for manual processing.

26. This example will send an insurance inquiry for Service Code Type 87 (cancer). If Service Type Code is defaulted then an inquiry will be sent for the Service Type Code defined in section 2.3 Define Service Code Parameters
1.  Access the PI Patient Insurance Menu.
82. Access the eIV Menu.
83. Access the EIRequest Electronic Insurance Inquiry option.
84. At the Select Patient Name prompt, enter Patient Name (in this example IBPATIENT, ONE).

    NOTE: Patch IB\*2\*438 provided the ability to request insurance inquiries with specific Service Type Codes. Patch IB\*2\*497 removed the ability to request multiple Service Type Codes but does allow for the selection of a single Service Type Code.

The following screen will be displayed:

eIV Insurance Request Dec 22, 2010@16:53:22 Page: 1 of 1

Request Electronic Insurance Inquiry for Patient: IB PATIENT, ONE XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 Insurance Comp1 TST1223 OTHER 07/01/2001

2 Insurance Comp2 GRP NUM 20 SELF 04/09/2010

Enter ?? for more actions \>\>\>

SE Select Entry CD EICD Request

EX Exit

Select Action: Quit// SE Select Entry

Select entry to request electronic inquiry: (1-2): 1

Enter Service Type Code: 30// ?

Answer with X12 271 SERVICE TYPE CODE

Do you want the entire 187-Entry X12 271 SERVICE TYPE List? N

Enter Service Type Code: 30// ??

Enter the single SERVICE TYPE CODE to be sent with inquiry or press

'ENTER' to send default service type code. The default service type

code may auto-update. All other service types will not auto-update.

Enter Service Type Code: 30// ?

Answer with X12 271 SERVICE TYPE CODE

Do you want the entire 187-Entry X12 271 SERVICE TYPE List? Y (Yes)

Choose from:

1 Medical Care

2 Surgical

3 Consultation

4 Diagnostic X-Ray

5 Diagnostic Lab

6 Radiation Therapy

7 Anesthesia

8 Surgical Assistance

9 Other Medical

10 Blood Charges

11 Used DME

12 DME Purchase

13 Ambulatory SC Facility

14 Renal Supplies/Home

15 Alt. Method Dialysis

16 CRD Equipment

17 Pre-Admission Testing

18 DME Rental

19 Pneumonia Vaccine

20 2nd Surgical Opinion

'^' TO STOP:

Enter Service Type Code: 30// 11 Used DME

Enter Eligibility Date: TODAY//

Are you sure you want to request an insurance inquiry? NO// Y YES

Insurance Buffer entry created!

Enter RETURN to continue or '^' to exit:

85. At the Select Action prompt, enter SE Select Entry.
86. At the Select entry to request electronic inquiry: (1-2): prompt, enter 1 for this example.
87. At the SERVICE TYPE CODE prompt, enter ? for a list of the Service Type Codes or enter the one required. In this example enter 11. Now select Yes.
88. At the Enter Eligibility Date prompt, enter a valid date in MM/DD/YY.
89. You will then be prompted Are you sure you want to request an insurance inquiry? Enter Yes for this example. You will see the message Insurance Buffer entry created!
27. An asterisk (\*) will indicate that the request already has a matching buffer entry.

## Request an Electronic Insurance Coverage Discovery Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

28. Users must hold the IBCNE EICD REQUEST security key to perform this action.

The Request Electronic Insurance Inquiry option also allows a user to create an Electronic Insurance Coverage Discovery (EICD) inquiry when needed. There are restrictions and this action cannot be used for all patients. This functionality is intended to discover insurance coverage for those veterans whom have no active billable insurance on file.

1.  Access the PI Patient Insurance Menu.
2.  Access the eIV Menu.
3.  Access the EI Request Electronic Insurance Inquiry option.
4.  At the Select Patient Name prompt, enter Patient Name (in this example IBPATIENT, ONE).
5.  At the Select Action prompt, enter CD EICD Request.
6.  You will then be prompted Are you sure you want to request a search for this patient's insurance? Enter YES.
7.  The following screen will display with a message stating: An EICD request has been sent. If active insurance is found for this patient results will be displayed in the buffer within 30 days.

eIV Insurance Request Dec 22, 2010@16:53:22 Page: 1 of 1

Request Electronic Insurance Inquiry for Patient: IBPATIENT,ONE XXXX

<u>Insurance Co. Type of Policy Group Holder Effect. Expires</u>

No eligible insurance policies found.

Enter ?? for more actions \>\>\>

SE Select Entry CD EICD Request

EX Exit

Select Action: Quit// CD EICD Request

Are you sure you want to request a search for this patient's insurance? YES//

An EICD request has been sent. If active insurance is found for this patient

results will be displayed in the buffer within 30 days.

Type \<Enter\> to continue or '^' to exit:

29. If the patient does not meet the EICD rules, you will see the message: Sorry the patient does not qualify for this action.

# Patient Insurance Info View / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Insurance Info View / Edit option is used to look at a patient's insurance information and edit that data, if necessary. The system groups information that is specific to the insurance company, specific to the patient, specific to the group plan, specific to the annual benefits available, and the annual benefits already used.

Once a patient is selected, this screen is displayed listing all the patient's insurance policies. Information provided for each policy may include type of policy, group name, holder, effective date, and expiration date.

## View Patient Policy Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays expanded policy information for the selected company. Categories include utilization review data, subscriber data, subscriber's employer information, effective dates, plan coverage limitations, last contact, date of death, and comments on the patient policy or insurance group plan.

1.  Access the PI Patient Insurance Menu.
90. Access the PI Patient Insurance Info View/Edit Option
91. At the Select Patient Name prompt, enter Patient Name.

The following screen will be displayed:

Patient Insurance Management Jul 21, 2010@13:23:59 Page: 1 of 1

Insurance Management for Patient: IB,PATIENT XXXXX XX/XX/XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 IBinsurance COMPREHENSIVE M GRP NUM 13 SELF 08/24/14

Enter ?? for more actions \>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EB Expand Benefits

EX Exit

Select Item(s): Quit//

92. At the Select Action prompt, enter VP for Policy Edit/View.

The following series of screens will be displayed:

Patient Insurance Management Jul 21, 2010@13:23:59 Page: 1 of 1

Insurance Management for Patient: IBPATIENT,ONE XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 IBinsurance COMPREHENSIVE M GRP NUM 13 SELF 06/20/09

Enter ?? for more actions \>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EB Expand Benefits

RX RX COB Determination EX Exit

Select Item(s): Quit// VP Policy Edit/View .......................

Patient Policy Information Mar 12, 2015@11:15:02 Page: 1 of 8

For: IBPATIENT,ONE XXX-XX-XXXX XX/XX/XXXX

IBinsurance Insurance Company \*\* Plan Currently Active \*\*

Insurance Company

Company: IBinsurance

Street: XXXXXXXXXXXXX

City/State: XXXXXX, IN 99999

Billing Ph: 800/XXX-XXXX

Precert Ph: 800/XXX-XXXX

Plan Information

Is Group Plan: YES

Group Name: XXXXXXX

Group Number: GRP NUM 13

BIN:

PCN:

Type of Plan: COMPREHENSIVE MAJOR MED

Electronic Type: COMMERCIAL

Plan Filing TF: (2 YEAR(S))

ePharmacy Plan ID:

ePharmacy Plan Name:

ePharmacy Natl Status:

ePharmacy Local Status:

Utilization Review Info Effective Dates & Source

Require UR: Effective Date: 08/24/14

Require Amb Cert: YES Expiration Date:

Require Pre-Cert: YES Source of Info: INTERVIEW

Exclude Pre-Cond: Stop Policy From Billing: NO

Benefits Assignable: YES

Subscriber Information

Whose Insurance: VETERAN

Subscriber Name: IB,PATIENT One

Relationship: SELF

Primary ID: XXXXXXXXXX

Coord. Benefits: PRIMARY

Subscriber's Employer Information

Employment Status: Emp Sponsored Plan: No

Employer: Claims to Employer: No, Send to Insurance

Street: Retirement Date:

City/State:

Phone:

Primary Provider:

Prim Prov Phone:

Subscriber’s Information (use Subscriber Update Action)

Subscriber’s DOB: XX/XX/XXXX

Str 1: xxxx Test Street

Str 2:

City: ANYWHERE

St/Zip: WY 99999

SubDiv:

Country:

Phone: XXXXXXX

Subscriber’s Sex: FEMALE

Subscr’s Branch:

Subscr’s Rank:

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber ID: xxxxxxxx

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 08/24/2014 YES

OUTPATIENT BY DEFAULT

PHARMACY 09/24/2014 NO

DENTAL BY DEFAULT

MENTAL HEALTH BY DEFAULT

LONG TERM CARE BY DEFAULT

PROSTHETICS BY DEFAULT

VISION BY DEFAULT

User Information

Entered By: IBCLERK,ONE

Entered On: 10/08/14

Last Verified By:

Last Verified On:

Last Updated By: IBCLERK,ONE

Last Updated On: 10/08/14

Comment -- Group Plan

This is a long group comment. This area can hold much more than 80

Characters in the field.

Comment -- Patient Policy

Dt Entered Entered By Method Person Contacted

09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

+09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 74 CHARACTERS TO SHOW THE WRAP INDICATO

Personal Riders

Rider \#1: DENTAL COVERAGE

\+ Enter ?? for more actions

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action:

### Patient Policy Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*528 enhances Patient Policy Comments. The Patient Policy Comments can be accessed from the Patient Policy Information screens. The Patient Policy Comments can now hold 245 characters. This field will also hold a history of previously entered comments. With patch IB\*2.0\*549, the first 74 characters of the two most recent comments will be displayed when a user selects the action Policy Edit/View(VP) from with the Patient Policy Information screens.

1.  Access the PI Patient Insurance Menu.
93. Access the PI Patient Insurance Info View/Edit option
94. At the Select Patient Name prompt, enter Patient Name.
95. At the Select Action prompt, enter VP for Policy Edit/View.
30. A “+” symbol next to a comment indicates that there is more to the comment and only a portion is currently displayed to the user.

The following is a sample of what will be displayed along with other policy related information:

Comment -- Patient Policy

Dt Entered Entered By Method Person Contacted

09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

+09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 77 CHARACTERS TO SHOW THE WRAP INDICATO

To modify, delete, or add a comment, the user must select the Pt Policy Comments (PT) action.

96. At the Select Action prompt, enter PT for Pt Policy Comments.
31. A “+” symbol next to a comment indicates that there is more to the comment and only a portion is currently displayed to the user.

The following screen will be displayed:

Patient Policy Comments Nov 17, 2015@16:51:41 Page: 1 of 1

Policy Comment History for: IBPATIENT, ONE XXX-XX-XXXX XX/XX/XXXX

IBinsurance \*\* Plan Currently Active \*\*

Dt Entered Entered By Method Person Contacted

1 09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

2 +09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 77 CHARACTERS TO TEST THE WRAP INDI

3 04/26/15 IBCLERK,ONE MAIL USER-B

Contacted the insurance company to confirm the subscriber ID.

4 +04/26/15 IBCLERK,FOUR PHONE USER-D

CONTACTED THE PATIENT'S GRANDSON WHO WAS ABLE TO CONFIRM THE INSURANCE A

5 +04/25/15 IBCLERK,FOUR PERSONAL USER-B

THIS IS THE VERY FIRST PATIENT POLICY COMMENT FOR IB,PATIENT AND I'M JUST

\+ Enter ?? for more actions

EE Expand Entry AC Add Comment SL Search List

EC Edit Comment DC Delete Comment EX Exit

Select Action: Quit//

These following actions are available in Patient Policy Comments screen:

- EE – Expand Entry
- AC – Add Comment
- SL – Search List
- EC – Edit Comment
- DC – Delete Comment
- EX - Exit

<u>Expand Entry</u> – Use this action to view a specific comment in its entirety including the following additional information that may be associated with that comment:

- Last Edited Date
- Last Edited By
- Contact Person
- Contact Phone \#
- Method
- Call Reference \#
- Authorization \#
- Comment (Entire comment – no truncation)

<u>Add Comment</u> – Use this action to create a new comment. If you were the last person to add a comment and it is the same day as when you added the last comment, this action will function like the “Edit Comment” action.

<u>Search List</u> – Use this action to search all comments for that patient policy. It will display all comments where the search criteria was found in at least one of the following fields:

- Contact Person
- Contact Phone \#
- Call Reference \#
- Authorization \#
- Comment (Entire comment – no truncation)

<u>Edit Comment</u> – Use this action to edit a comment. Comments can be edited later on the same date they were entered. If another comment is entered on that day, the comment will be locked. Users can only edit a comment during the same business day that it was created, until another user creates a new comment. A user cannot edit another user’s comment.

<u>Delete Comment</u> – Use this action to delete a comment. Users who *do not* hold the IBCN PT POLICY COMNT DELETE security key can only delete a comment on the same date it was entered or until another comment is entered on that same day by a different user. After another comment by a different user is entered on the same day or as of the following day, the comment will be locked and cannot be deleted by those users. A user without the IBCN PT POLICY COMNT DELETE key cannot delete another user’s comment. If a user without the security key attempts to delete a comment that is outside those rules, the message “Contact your supervisor for assistance” displays.

Supervisors and managers who hold the IBCN PT POLICY COMNT DELETE security key can delete unwanted comments that are not the latest comment, comments that were not entered on the current date, and comments entered by another user.

<u>Exit</u> – Use this action to leave the Patient Policy Comment screen.

## View Eligibility Benefit Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen allows eligibility / benefit information to be displayed.

1.  Access the PI Patient Insurance Menu.
97. Access the PI Patient Insurance Info View/Edit option.
98. At the Select Patient Name prompt, enter Patient Name (in this example IBpatient,One).
99. At the Select Action prompt, enter EB for Expand Benefits.

The following screen will be displayed:

eIV Elig/Benefit Information Jul 23, 2015@17:41:07 Page: 1 of 11

PATIENT,ONE xxx-xx-xxxx IBinsurance

\*\* This response is based on service date 07/05/2015 and service type: Health

Benefit Plan Cov \*\*

-----------------------------------------------------------------------------

Eligibility/Group Plan Information

Reference ID Qualifer: OTHER Reference ID: 12345

Reference ID description:

Reference ID Qualifer: Group Number Reference ID: AET1234

Reference ID description: TEST1

Provider Code:

Reference ID:

Primary Diagnosis Code:

Military Info Status: Employment Status:

Government Affiliation: Personnel Desc:

Service Rank: Date Time Period:

eIV Eligibility/Benefit Data Group# 1 of 6

+---------Enter ?? for more actions------------------------------------------

PS Payer Summary EX Exit

Select Action: Next Screen// NEXT SCREEN

eIV Elig/Benefit Information Jul 23, 2015@17:41:10 Page: 2 of 11

IBPATIENT,ONE xxx-xx-xxxx IBinsurance

\*\* This response is based on service date 07/05/2015 and service type: Health

Benefit Plan Cov \*\*

+----------------------------------------------------------------------------

Eligibility/Benefit Information

Elig/Ben Info: Active Coverage Coverage Level:

Date/Time Qual: D/T Period:

Service Type:

Time Period:

Insurance Type:

Plan Coverage Desc: eIV Eligibility Determination

Benefit Amount: Benefit %:

Quantity Qual: Quantity Amount:

Auth/Certification Required: In-Plan-Network:

eIV Eligibility/Benefit Data Group# 2 of 6

Eligibility/Benefit Information

Elig/Ben Info: Active Coverage Coverage Level:

+---------Enter ?? for more actions------------------------------------------

PS Payer Summary EX Exit

Select Action: Next Screen//

100. At the Select Action prompt, enter PS for Payer Summary. (This will show all the other data that the payer responded with, which is not specifically benefit related.)
32. This is the same data that is displayed on the eIV Response Report if one used the trace# to look up the payer’s response. The eIV Response Report data is periodically purged from the system; therefore, the data has been added to this screen.

    The Eligibility Benefits action (and this subscreen of related information ... Payer Summary) only contains one payer response at any given time.

The following screen will be displayed:

eIV Elig/Benefit Information Jul 23, 2015@17:41:07 Page: 1 of 1

IBPATIENT,ONE xxx-xx-xxxx IBinsurance

\*\* This response is based on service date 07/05/2015 and service type: Health

Benefit Plan Cov \*\*

-----------------------------------------------------------------------------

Subscriber: IB,Patient

Subscriber ID: XXXXXXXXX

Subscriber DOB: XXXXXXXX

Subscriber SSN: XXXXXXXXXXX Subscriber Sex:

Group Name: XXXXXXXXXXXXXX

Group ID: XXXXXXXXXXXX

Whose Insurance: XXXXXXX

Patient Relationship to Subscriber: PATIENT

Member ID: XXXXXXXXXX

COB: XXXXXXXXX

Service Date: 07/05/2015 Date of Death:

Effective Date: XXXXXXXXX Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: XXXXXXXXX Trace \#: XXXXXXXXXXX

Policy Number: XXXXXXXXXXXX

Contact Information

+---------Enter ?? for more actions------------------------------------------

EX Exit

Select Action: Next Screen// NEXT SCREEN

# IIV Auto Match Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Auto Match is a VistA feature designed to help match user-entered insurance company names to the correct payers in the database. In VistA, there are several places a user can enter an insurance company name (free text) without a list of valid insurance names from which to pick. Patient Registration and the Insurance Buffer are two examples. This can result in misspelled, improperly formatted, or incomplete insurance company names. Auto Match is necessary because the eIV software must be able to identify which insurance company the user is referring to in order to appropriately generate inquiries and process responses. This functionality promotes the use of consistent insurance company names.

There is an IIV AUTO MATCH file (#365.11) in each VistA system. Each record in the file has two fields. The first field, Entered Name, stores the insurance company name that the user entered into the VistA system without validation. The second field, Proper Name, stores the name of the insurance company that can be found in the INSURANCE COMPANY file (#36) of the VistA database.

The Auto Match feature is used to teach the VistA system how to interpret common misspellings or incomplete entries that users enter when typing in free-text insurance company names.

It is recommended that users run the Check Ins Co’s action on names from the Insurance Buffer Views to initially populate the Auto Match files based on existing entries in the Insurance Buffer. Selecting this action will generate a list of insurance company names found in the INSURANCE VERIFICATION PROCESSOR file (#355.33) that do not exist in the INSURANCE COMPANY file (#36). The more one “teaches” the Auto Match functionality, the fewer problems eIV will encounter when it creates insurance inquiries for electronic transmission to the payers.

Users can enter (add), edit, or delete Auto Match entries using the Menu option  
PI \> EIV \> AE (Enter/Edit Auto Match Entries), as described in section 8.3.

Users must have the IBCNE EIV IIU MAINTENANCE security key to enter (add), edit, or delete an Auto Match entry.

## Auto Match in VistA Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Auto Match is currently used in the Insurance Buffer.

When a user types a free-text insurance company name, VistA attempts to match the name with one of the proper insurance company names stored in the INSURANCE COMPANY file (#36). If no match is found, the name as typed by the user is then compared to the list of Entered Name(s) in the IIV AUTO MATCH file (#365.11). If there are Entered Name(s) in the IIV AUTO MATCH file that match the user-typed name, they are displayed along with their associated Proper Name(s). Users may then select one of the Proper Names to replace the free-text entry.

Users are not required to accept one of the supplied choices; they can choose to keep the free-text name. The Auto Match process may fail to find matching insurance company name(s), in which case no choices are presented to users.

## Types of Auto Match Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Simple Auto Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a simple Auto Match, the Entered Name field literally contains the name found in the Insurance Buffer (or entered by a user into the IIV AUTO MATCH file (#365.11). Leading and trailing spaces are ignored. An entry in the buffer might have BC/BS as the Entered Name and show Blue Cross Blue Shield in the Proper Name field. As the insurance staff encounter misnamed insurance companies (i.e. the name on the insurance card does not match the name in the VistA database), users can correct the name and VistA will prompt users to add it as a new record in the IIV AUTO MATCH file (#365.11).

### Wildcard Auto Match Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a wildcard Auto Match, simple matches are supported but the wildcard character, the asterisk (\*), can also be used. Wildcards may be used to anticipate common spelling mistakes. The asterisk can be substituted for any number of characters. For example, if users enter BC\*BS, the system will return all Insurance Company names that begin with BC and end with BS. BC/BS, BC BS, BC-BS, BCBS, and BC / BS would all match BC\*BS.

An Entered Name may contain more than one asterisk (i.e. BC\*BS\*). When a wildcard is used, a minimum of four non-wildcard characters must also be specified.

## Enter / Edit Auto Match Entries (AE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA offers a Menu option to enter (add), edit, or delete entries in the IIV AUTO MATCH file (#365.11). Each AE option is explained separately below.

### Add an Auto Match Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the eIV Menu.
101. Select the AE Enter/Edit Auto Match Entries option.

The following prompts display:

Select an Auto Match Entry: ??

Choose from:

1199 SEIU is associated with 1199 NAT'L BEN INPAT

BC/BS OF ILLINOIS is associated with BCBS WY\*

BC/BS OF TEXAS is associated with BCBS WY\*

BCBS is associated with BCBS WY\*

You may enter a new IIV AUTO MATCH, if you wish.

This field is the entered name for the insurance company. This

value holds the 'incorrect' insurance company name which needs

to get corrected and replaced with the valid insurance company

name. Typical values in this field will include common

spelling mistakes and incorrect insurance company names. Also

allowed here is the "\*" wildcard character. Any entry with a

wildcard character must also contain at least 4 non-wildcard

characters. Multiple asterisks are allowed here.

Select an Auto Match Entry: TEST ADDED ENTRY

Are you adding ‘TEST ADDED ENTRY’ as a new IIV AUTO MATCH (the 5TH)? No// Y

IIV AUTO MATCH INSURANCE COMPANY NAME: Z

1 SAMPLENAME ADMINISTRATORS  
CHOOSE 1 – 1: 1

102. At the Select an Auto Match Entry prompt, type the Entered Name for the entry you want to add (for this example, TEST ADDED ENTRY).
103. (For this example) At the Are you adding ‘TEST ADDED ENTRY’ as a new IIV AUTO MATCH (the 5TH)? No / / prompt, answer YES.
104. At the IIV AUTO MATCH INSURANCE COMPANY NAME prompt, enter a valid Proper Name from the Insurance Company file (or enter ??).
33. Remember – the Entered Name must be a minimum of 3 characters. If an ‘\*’ is used, it must be accompanied by four additional characters.

    Entered Names must be unique. One Entered Name cannot be associated with more than one Insurance Company Name.

### Edit an Auto Match Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the eIV Menu.
105. Select the AE Enter/Edit Auto Match Entries option.

The following prompts display:

Select an Auto Match Entry: ??

Choose from:

1199 SEIU is associated with 1199 NAT'L BEN INPAT

BC/BS OF ILLINOIS is associated with BCBS WY\*

BC/BS OF TEXAS is associated with BCBS WY\*

BCBS is associated with BCBS WY\*

TEST ADDED ENTRY is associated with SAMPLENAME ADMINISTRATORS

You may enter a new IIV AUTO MATCH, if you wish.

This field is the entered name for the insurance company. This

value holds the 'incorrect' insurance company name which needs

to get corrected and replaced with the valid insurance company

name. Typical values in this field will include common

spelling mistakes and incorrect insurance company names. Also

allowed here is the "\*" wildcard character. Any entry with a

wildcard character must also contain at least 4 non-wildcard

characters. Multiple asterisks are allowed here.

Select an Auto Match Entry: TEST ADDED ENTRY is associated with SAMPLENAME  
ADMINISTRATORS

...OK? Yes// (Yes)

Do you want to Edit or Delete this entry? E// Edit

AUTO MATCH VALUE: TEST ADDED ENTRY//

INSURANCE COMPANY NAME: SAMPLENAME ADMINISTRATORS Replace

TEST ADDED ENTRY is now associated with SAMPLENAME ADMINISTRATORS.

106. At the Select an Auto Match Entry prompt, type the Entered Name for the entry you want to edit.
107. At the Do You Want to Edit or Delete this entry? E// prompt, type Edit.
108. At the AUTO MATCH VALUE prompt, accept or change the existing Entered Name value.
109. At the INSURANCE COMPANY NAME prompt, accept or change Insurance Company to be matched to this entry.
34. Remember – the Entered Name must be a minimum of 3 characters. If an ‘\*’ is used, it must be accompanied by four additional characters.

    Entered Names must be unique. One Entered Name cannot be associated with more than one Insurance Company Name.

### Delete an Auto Match Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the eIV Menu.
110. Select the AE Enter/Edit Auto Match Entries option.

The following prompts display:

Select an Auto Match Entry: ??

Choose from:

1199 SEIU is associated with 1199 NAT'L BEN INPAT

BC/BS OF ILLINOIS is associated with BCBS WY\*

BC/BS OF TEXAS is associated with BCBS WY\*

BCBS is associated with BCBS WY\*

TEST ADDED ENTRY is associated with SAMPLENAME ADMINISTRATORS

You may enter a new IIV AUTO MATCH, if you wish.

This field is the entered name for the insurance company. This

value holds the 'incorrect' insurance company name which needs

to get corrected and replaced with the valid insurance company

name. Typical values in this field will include common

spelling mistakes and incorrect insurance company names. Also

allowed here is the "\*" wildcard character. Any entry with a

wildcard character must also contain at least 4 non-wildcard

characters. Multiple asterisks are allowed here.

Select an Auto Match Entry: TEST ADDED ENTRY is associated with SAMPLENAME  
ADMINISTRATORS

...OK? Yes// (Yes)

Do you want to Edit or Delete this entry? E// Delete

Are you sure you want to delete \<TEST ENTRY\>: ? N//

111. At the Select an Auto Match Entry prompt, type the Entered Name for the entry you want to delete.
112. At the Do You Want to Edit or Delete this entry? E//, type Delete (Edit is the default).
113. (For this example) At the Are you sure you want to delete \<TEST ADDED ENTRY\>: ? N// prompt, answer YES.
35. Remember – the Entered Name must be a minimum of 3 characters. If an ‘\*’ is used, it must be accompanied by four additional characters.

    Entered Names must be unique. One Entered Name cannot be associated with more than one Insurance Company Name.

## Add Auto Match Entries Using Insurance Buffer Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the eIV Menu.
114. Select the AB Add Auto Match Entries Using Insurance Buffer Data option.

The following prompts display:

Unmatched Buffer Names Jul 07, 2010@12:02:54 Page: 1 of 1

These are Insurance Company names from the Insurance Buffer file that do not

exist in the Insurance Company file (either as Names or as Synonyms). They

also do not exist or pattern match with any entry in the Auto Match file.

1 IBinsurance Onee

2 IBinsurance Number Two

3 IBinsurance Threee

Enter ?? for more actions

Select Entry Auto Match Enter/Edit Exit

Select an Auto Match Entry: IBinsurance Number Two

Are you adding ‘IBinsurance Number Two’ as a new IIV AUTO MATCH (the 5TH)? No// Y

IIV AUTO MATCH INSURANCE COMPANY NAME: IBinsurance Two

115. At the Select Action prompt, enter Auto Match Enter/Edit for this example.
116. Select the AE Enter/Edit Auto Match Entries option.
117. At the Select an Auto Match Entry prompt, enter IBinsurance Number Two for this example.
118. (For this example) At the Are you adding ‘IBinsurance Number Two’as a new IIV AUTO MATCH (the 144<sup>th</sup>)? No// prompt, answer YES.
119. At the IIV AUTO MATCH INSURANCE COMPANY NAME prompt, enter IBinsurance Two for this example.
36. Remember – the Entered Name must be a minimum of 3 characters. If an ‘\*’ is used, it must be accompanied by four additional characters.

    Entered Names must be unique. One Entered Name cannot be associated with more than one Insurance Company Name.

## Check Insurance Buffer Company Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As described in section 4.2.6, the action Check Ins Co’s. in the Insurance Buffer screen is another method of accessing the Auto Match Enter/Edit option.

1.  Access the PI Patient Insurance Menu.
120. Select the BI Process Insurance Buffer option.

The following screen will be displayed:

Positive Insurance Buffer May 21, 2010@10:18:01 Page: 1 of 1

Sorted by: Positive Response

Patient Name Insurance Company Subscr Id S Entered iIEYH

1 +IBpatient,One XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

2 +IBpatient,Two XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

3 +IBpatient,Three XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

4 +IBpatient,Four XXXX IBinsurance Two SUB ID XXXX P 09/21/04 Y

5 +IBpatient,Five XXXX IBinsurance Four SUB ID XXXX P 03/31/05

6 +IBpatient,Six XXXX IBinsurance Four SUB ID XXXX P 12/08/04

7 +IBpatient,Seven XXXX IBinsurance Two SUB ID XXXX P 11/30/04 Y

8 +IBpatient,Eight XXXX IBinsurance Four SUB ID XXXX P 02/28/05 YH

9 +IBpatient,Nine XXXX IBinsurance Two SUB ID XXXX I 03/29/05 Y

10 +IBpatient,Ten XXXX IBinsurance Three SUB ID XXXX I 11/16/04

11 +IBpatient,Eleven XXXX IBinsurance Two SUB ID XXXX P 03/31/05 YH

12 +IBpatient,Twelve XXXX IBinsurance Five SUB ID XXXX I 03/24/05 H

+Active ?Await/Reply

PE Process Entry AE Add Entry PB Pos. Buffer FA Future Appts.

RE Reject Entry ST Sort List NB Neg. Buffer EX Exit

EE Expand Entry CC Check Ins Co's MB Medicare Buffer

Select Action: Next Screen//

121. At the Select Action: prompt, enter CC for Check Ins Co’s.

The following screen will be displayed:

Unmatched Buffer Names Jul 07, 2010@12:02:54 Page: 1 of 1

These are Insurance Company names from the Insurance Buffer file that do not

exist in the Insurance Company file (either as Names or as Synonyms). They

also do not exist or pattern match with any entry in the Auto Match file.

1 IBinsurance Onee

2 IBinsurance Number Two

3 IBinsurance Threee

Enter ?? for more actions

Select Entry Auto Match Enter/Edit Exit

Select Action: Next Screen//

## Change Company Name via the Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Auto Match entries can also be created when users change an Insurance Buffer entry’s insurance company name in the insurance buffer edit screen. When users change the existing insurance company name, listed on an Insurance Buffer entry, VistA prompts users to keep track of the original typed name and new name as an Auto Match entry. If users concur, the original typed insurance company name is treated as the Entered Name and the new insurance company name is considered the Proper Name. The user is then offered the opportunity to modify the Entered Name, possibly to make it more general.

37. This example sets up an auto match entry to associate IBinsurance Flur with IBinsurance Four.
1.  Access the PI Patient Insurance Menu.
122. Select the BI Process Insurance Buffer option.
38. VistA warns users when the Proper Name matches an insurance company’s name synonym and not the company’s name, or the Proper Name matches more than one synonym and company name.

The following screen will be displayed:

Positive Insurance Buffer May 21, 2010@10:18:01 Page: 1 of 1

Sorted by: Positive Response

Patient Name Insurance Company Subscr Id S Entered iIEYH

1 IBpatient,One XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

2 -IBpatient,Two XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

3 -IBpatient,Three XXXX IBinsurance One SUB ID XXXX E 05/18/10 i

4 IBpatient,Four XXXX IBinsurance Two SUB ID XXXX P 09/21/04 Y

5 IBpatient,Five XXXX IBinsurance Four SUB ID XXXX P 03/31/05

6 !IBpatient,Six XXXX IBinsurance Flur SUB ID XXXX P 12/08/04

7 -IBpatient,Seven XXXX IBinsurance Two SUB ID XXXX P 11/30/04 Y

8 IBpatient,Eight XXXX IBinsurance Four SUB ID XXXX P 02/28/05 YH

9 +IBpatient,Nine XXXX IBinsurance Two SUB ID XXXX I 03/29/05 Y

10 IBpatient,Ten XXXX IBinsurance Three SUB ID XXXX I 11/16/04

11 +IBpatient,Eleven XXXX IBinsurance Two SUB ID XXXX P 03/31/05 YH

12 +IBpatient,Twelve XXXX IBinsurance Five SUB ID XXXX I 03/24/05 H

+Active

PE Process Entry AE Add Entry PB Pos. Buffer FA Future Appts.

RE Reject Entry ST Sort List NB Neg. Buffer EX Exit

EE Expand Entry CC Check Ins Co's MB Medicare Buffer

Select Action: Exit//

123. At the Select Action: prompt, enter EE for Expand Entry.
124. At the Select Buffer Entries: prompt, enter 6 for this example and page through the screens.

The following screens will be displayed:

Insurance Buffer Entry Jul 23, 2013@17:16:47 Page: 1 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Insurance Company Information

Name: IBinsurance Flur Reimburse?: WILL REIMBURSE

Phone: Billing Phone:

Precert Phone:

Remote Query From:

Address:

Group/Plan Information

Group Plan?: Yes

Group Name: TEST1

Group Number: IB 1234

BIN: Require UR: No

PCN: Require Amb Cert: No

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen//

Insurance Buffer Entry Jul 23, 2013@17:19:39 Page: 2 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Require Pre-Cert: No

Type of Plan: COMPREHENSIVE MAJOR MEDIC Exclude Pre-Cond: No

Benefits Assignable: Yes

Policy/Subscriber Information

Whose Insurance: SPOUSE Effective: 07/01/01

Expiration:

Subscriber's Name: IBINS,ACTIVE

Subscriber Id: XXXXXXXXXXX

Relationship: SPOUSE Primary Provider:

Provider Phone:

Subscriber's DOB: XX/XX/XXXX Coord of Benefits:

Patient Id: XXXXXXXXXXXX

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

Insurance Buffer Entry Jul 23, 2013@17:20:17 Page: 3 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

+----------------------------------------------------------------------------

Employer Sponsored Group Health Plan?:

Buffer Entry Information

Date Entered: 7/5/13@09:05 Date Verified:

Entered By: CLERK,IB Verified By:

\*\* This response is based on service date 07/05/2013 and service type: Health

Benefit Plan Cov \*\*

eIV Trace \#: xxxxxxxxx eIV Processed Date: 7/5/13@09:38

Source: INTERVIEW

Current eIV Status: Problem Identified

Insurance company IBinsurance Flur could not be matched to a valid entry inthe Insurance Company file.

eIV could not create an inquiry for this entry. eIV could not match the

insurance company name in the Insurance Buffer file (#355.33) to a valid

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

125. At the Select Action: prompt, enter EI for Ins. Co. Edit.
126. At the Insurance Company Name: IBinsurance Flur // prompt, enter IBinsurance Four.
127. At the CHOOSE 1-5: prompt, enter 1 for this example.
128. At the Do you want to add an Auto Match entry that associates IBinsurance Flur with IBinsurance Four? No// prompt, enter YES.

The following prompts are displayed along with a confirmation message:

------------------------ INSURANCE COMPANY INFORMATION -------------------------

INSURANCE COMPANY NAME: IBinsurance Flur // IBinsurance Four

1 IBinsurance Four

2 IBinsurance Four A

3 IBinsurance Four B

4 IBinsurance Four C

CHOOSE 1-5: 1

Do you want to add an Auto Match entry that associates

IBinsurance Flur with IBinsurance Four? No// Y YES

AUTO MATCH VALUE: IBinsurance Flur //

IBinsurance Flur is now associated with IBinsurance Four.

129. The user will then be a series of prompts to update the insurance company details. At each prompt, enter RETURN to keep the current setting.

REIMBURSE?:

PHONE NUMBER: 8005555555//

BILLING PHONE NUMBER:

PRECERTIFICATION PHONE NUMBER:

STREET ADDRESS \[LINE 1\]: PO BOX 55555//

STREET ADDRESS \[LINE 2\]:

CITY: ANYCITY//

STATE: OHIO//

ZIP CODE: 99999//

130. After accepting all the current insurance company settings, the original insurance buffer entry will be displayed showing the revised insurance company.

Insurance Entry Jul 23, 2013@17:16:47 Page: 1 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Insurance Company Information

Name: IBinsurance Four Reimburse?: WILL REIMBURSE

Phone: Billing Phone:

Precert Phone:

Remote Query From:

Address:

Group/Plan Information

Group Plan?: Yes

Group Name: TEST1

Group Number: IB1234

BIN: Require UR: No

PCN: Require Amb Cert: No

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen//

Insurance Buffer Entry Jul 23, 2013@17:19:39 Page: 2 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

-----------------------------------------------------------------------------

Require Pre-Cert: No

Type of Plan: COMPREHENSIVE MAJOR MEDIC Exclude Pre-Cond: No

Benefits Assignable: Yes

Policy/Subscriber Information

Whose Insurance: SPOUSE Effective: 07/01/01

Expiration:

Subscriber's Name: IBINS,ACTIVE

Subscriber Id: XXXXXXXXXXX

Relationship: SPOUSE Primary Provider:

Provider Phone:

Subscriber's DOB: XX/XX/XXXX Coord of Benefits:

Patient Id: XXXXXXXXXXXX

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

Insurance Buffer Entry Jul 23, 2013@17:20:17 Page: 3 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

+----------------------------------------------------------------------------

Employer Sponsored Group Health Plan?:

Buffer Entry Information

Date Entered: 7/5/13@09:05 Date Verified:

Entered By: CLERK,IB Verified By:

\*\* This response is based on service date 07/05/2013 and service type: Health

Benefit Plan Cov \*\*

eIV Trace \#: xxxxxxxxx eIV Processed Date: 7/5/13@09:38

Source: INTERVIEW

Current eIV Status: Response Received, Active Policy

Information received via electronic inquiry indicates patient has active

insurance.

+---------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Next Screen// NEXT SCREEN

Insurance Buffer Entry Jul 23, 2013@17:20:26 Page: 4 of 4

IBpatient,One xxx-xx-xxxx DOB: XXX XX,XXXX AGE: XX

Buffer entry created on 07/05/13 by CLERK,IB (INTERVIEW)

+----------------------------------------------------------------------------

Action to take: Review the details listed in the eIV Response Report

before processing this buffer entry.

----------Enter ?? for more actions------------------------------------------

EI Ins. Co. Edit ES Escalate Entry EX Exit

EA All Edit PI Pt. Policy Edit

PE Group/Plan Edit EB Expand Benefits

Select Action: Quit//

# eIV Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are multiple eIV-related reports. An explanation of and instructions for each report are described in this section.

eIV Reports can be found on the eIV Menu on the Patient Insurance Menu.

AB Add Auto Match Entries Using Insurance Buffer Data

AE Enter/Edit Auto Match Entries

AR eIV Ambiguous Policy Report

EI Request Electronic Insurance Inquiry

HL HL7 Response Report

IR eIV Inactive Policy Report

IU eIV Auto Update Report

MW Medicare Potential COB Worklist

PR eIV Payer Report

RR eIV Response Report

SR eIV Statistical Report

Select eIV Menu Option:

## HL7 Response Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to capture incoming and outgoing HL7 messages transmitted from a VistA database to the FSC.

> **WARNING:** Only those entries that were once associated with a buffer entry are candidates for this report. Therefore, if the eIV appointment extract verified a policy and the payer response was automatically processed by the software (eIV auto update) then it would never be found on this report, as a buffer entry was not created in that scenario.

Report Parameters

Search Criteria:

- All or Selected Payers
- Response Received Date Range
- All or Selected Patients

Sort Criteria:

- Payer Name
- Patient Name

This is a 132 column report.

Sample Report

HL7 Response Report Aug 03, 2015@09:12:53 Page: 1

01/01/2014 - 08/03/2015

All Payers

Payer Name Patient Name SSN Dt Sent Dt Rec'd Trace \# Buffer \#

-----------------------------------------------------------------------------------------------------------------------------------

CIGNA Count = 1

CIGNA IBTEST,EB 1234 9/24/14@10:10 2424 45

## eIV Auto Update Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to view the list of patients whose Patient Insurance Information has been updated automatically based on a 271 Response message.

Report Parameters

Search Criteria:

- Summary or Detail
- All or Selected Payers
- Insurance Company Detail or not (only applies to ‘Selected Payers’)
- Response Received Date Range (Earliest Date Received defaults to 6 months ago; Latest Date Received defaults to current system date.)
- All or Selected Patients (only applies to ‘Detailed’ version of the report)

Sort Criteria:

- Payer Name
- Patient Name
- Clerk Name

This is a 132 column report, for the ‘Detailed’ version of the report.

Sample Report

Auto Update Report Jun 03, 2010@10:35:41 Page:1

Response Received: 05/12/2010 - 05/23/2010

Detailed Report: All Payers; All Insurance Companies; All Patients

Payer Insurance Co Patient Name SSN Dt Sent Auto Dt eIV Trace

--------------------------------------------------------------------------------------------------------------------------------

AETNA AETNA IBpatient,One XXXX 05/12/10 05/12/10@07:48:27 XXXXXXXX

AETNA AETNA IBpatient,Two XXXX 05/12/10 05/12/10@09:16:37 XXXXXXXX

AARP AARP IBpatient,One XXXX 05/13/10 05/13/10@07:51:21 XXXXXXXX

AARP AARP IBpatient,Two XXXX 05/16/10 05/16/10@08:30:35 XXXXXXXX

CIGNA CIGNA IBpatient,One XXXX 05/21/10 05/21/10@09:30:56 XXXXXXXX

CIGNA CIGNA IBpatient,Two XXXX 05/21/10 05/21/10@07:25:30 XXXXXXXX

CIGNA CIGNA IBpatient,Three XXXX 05/22/10 05/22/10@10:25:30 XXXXXXXX

CIGNA CIGNA IBpatient,Four XXXX 05/23/10 05/23/10@10”15:45 XXXXXXXX

Enter RETURN to continue or '^' to exit:

## eIV Response Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to view the data that was received through the eIV process – receipt of 271 Health Care Eligibility Benefits Response messages.

Report Parameters

Search Criteria:

- Response Received Date Range
- Trace \#
- All or Selected Payers
- All or Selected Patients
- All Responses or Most Recent (for a payer/patient combination)

Sort Criteria:

- Payer or Patient

Sample Report

eIV Response Report

Insurance verification responses are received daily.

Please select a date range in which responses were received to view the

associated response detail. Otherwise, select a Trace \# to view specific

response detail.

Select one of the following:

1 Report by Date Range

2 Report by Trace \#

Select the type of report to generate: 1// Report by Date Range

Start DATE: T-1 (JUL 09, 2013)

End DATE: T (JUL 10, 2013)

Payer or \<Return\> for All Payers:

Patient or \<Return\> for All Patients:

Select one of the following:

A All Responses

M Most Recent Responses

Select the type of responses to display: A// ll Responses

Select one of the following:

1 Payer Name

2 Patient Name

Select the primary sort field: 1// Payer Name

DEVICE: HOME//

Compiling report data ...

eIV Response Report Jul 10, 2013@12:08:38 Page: 1

Sorted by: Payer Name Responses Displayed: All

07/09/2013 - 07/10/2013

All Payers

All Patients

Payer: IBINSURANCE2

Patient: IBINS,ACTIVE (SSN: xxx-xx-xxxx DOB: XX/XX/XXXX)

Subscriber: IBINS,ACTIVE

Subscriber ID: XXXXXXXXXXX

Subscriber DOB: XX/XX/XXXX

Subscriber SSN: Subscriber Sex:

Group Name: TEST1

Group ID: AET1234

Whose Insurance: PATIENT

Member ID: COB:

Service Date: Date of Death:

Effective Date: 07/01/2001 Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: 07/09/2013 Trace \#: XXXXXXXXX

Policy Number:

Subscriber Dates:

Discharge: 20010801

Issue: 20010715

COBRA Begin: 20010501

COBRA End: 20010531

Patient Dates:

Plan Begin: 20010701

\*\*\* END OF REPORT \*\*\*Below is an example of the error information generated by the Payer or FSC displayed in the Response Report.

eIV Response Report by Trace \# May 07, 2013@11:48:22 Page:1

Trace \#: XXXXXXXXX

Payer: IBINSURANCE2

Patient: IBPATIENT,ONE (SSN: xxx-xx-xxxx DOB: XX/XX/XXXX)

Subscriber: IBSUB,AAAERROR

Subscriber ID:

Subscriber DOB: XX/XX/XXXX

Subscriber SSN: Subscriber Sex: M

Group Name:

Group ID:

Whose Insurance: VETERAN PATIENT

Member ID: COB:

Service Date: Date of Death:

Effective Date: Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: 05/02/2013 Trace \#: XXXXXXXXX

ERROR INFORMATION:

Reject Reason Code: 72

Reject Reason Text: Invalid/Missing Subscriber/Insured ID

Action Code: Invalid/Missing Subscriber/Insured ID

HIPAA Loop: Please Correct and Resubmit

HL7 Location: N/A

Error Source: Subscriber Name

The Error Source shows the originator of the returned error: “P” = Payer, “F” = FSC.

## eIV Payer Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to monitor the communication between VistA and the payers, including the types of error and warning messages that are received by VistA from the different payers.

Report Parameters

Search Criteria:

- Inquiry Made Date Range
- All or Selected Payers
- Include Rejection Detail (Yes/No)
- All Responses or Most Recent (for a payer/patient combination)

Sort Criteria:

- Payer Name
- Total Inquiries

This is a 132 column report.

Sample Report

eIV Payer Report Jun 03, 2010@10:39:21 Page: 1

Sorted by: Payer Rejection Detail: Not Included

05/04/2010 - 06/03/2010

All Payers

\*\*\*\*\* SENT \*\*\*\*\* \*\*\* RECEIVED \*\*\* AvgResp

Payer \[Inactive Date\] Created Cancel Queued 1st Att Retry Good Error (Days) Timeout Pending

==================================================================================================================================

IBpayer One 12 0 0 12 0 12 0 0.00 0 0

----------------------------------------------------------------------------------------

IBpayer Two 6 0 0 6 1 7 0 0.00 0 0

----------------------------------------------------------------------------------------

IBpayer Three 12 0 0 12 0 11 1 0.00 0 0

----------------------------------------------------------------------------------------

IBpayer Four 37 0 0 37 3 28 5 0.00 3 5

========================================================================================

Grand Totals 67 0 0 67 4 58 6 0.00 3 5

==================================================================================================================================

\*\*\* END OF REPORT \*\*\*

Enter RETURN to continue or '^' to exit:

## Medicare Potential Insurance Worklist - Potential COB Worklist / Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to create a list of those patients whom Medicare has identified in a 271 HL7 response message as having insurance subsequent to their Medicare insurance with the following data extracted from the 271 HL7 message when available:

- Patient Name
- Payer Code (primary, secondary, tertiary)
- Name of Insurance Company
- Insurance Company ID
- Review Status (not reviewed, review in process, completed)
- Insurance Company Address
- Insurance Company Phone Number
- Insurance Company Web Address

Report Parameters

Search Criteria:

- Earliest Date 271 HL7 message received
- Latest Date 271 HL7 message received

Sort Criteria

- Chronological Order
- Reverse Chronological Order

Report Format:

- Report
- Screen List (for additional details including screenshot, see in Section 4.3)

Report Type:

- COMPLETED entries ONLY
- COMPLETED entries ONLY with comments
- Exclude COMPLETED entries
- Exclude COMPLETED entries with comments

Sample Medicare COB Report

Pt. Secondary Insurance Report Jul 23, 2013@18:02:01 Page: 1

Sort: Chronological Order 06/23/2013 - 07/23/2013

Includes Completed Entries

IB,PATIENT XX/XX/XXXX 2

----------------------------------------------------------------------------

IBINSURANCE3 \T\\ HEALTH INSURANCE COMPANY, INC.,

2900 NORTH LOOP W

SOMEWHERE, TX XXXXX Phone: 9999999999 Website: www. IBinsurance3

IB,PATIENT XX/XX/XXXX 2

---------------------------------------------------------------------------

HEALTHSPRING LIFE \T\\ HEALTH INSURANCE COMPANY, INC.,

2900 NORTH LOOP W

SOMEWHERE, TX XXXXX Phone: 999999999 Website: www. IBinsurance3.com

IB,PATIENT XX/XX/XXXX 2

----------------------------------------------------------------------------

IBINSURANCE3 \T\\ HEALTH INSURANCE COMPANY, INC.,

2900 NORTH LOOP W

SOMEWHERE, TX XXXXX Phone: 999999999

Website: www. IBinsurance3.com

\*\*\* END OF REPORT \*\*\*

### Medicare Potential COB – as a Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User comments are not shown in the Worklist version of the Medicare Potential COB display.

The EE – Expand Entry action is available in Medicare Potential COB Worklist.

These following actions are hidden, but available in Medicare Potential COB Worklist:

- + – Next Screen
- - – Previous Screen
- UP – Up a Line
- DN – Down a Line
- \> - Shift view to Right
- \< - Shift view to Left
- FS – First Screen
- LS – Last Screen
- GO – Go to Page
- RD – Re Display Screen
- PS – Print Screen
- PL – Print List
- SL – Search List
- ADPL – Auto Display (On/Off)
- QU - Quit

Several indicators may be found on the main screen of the worklist:

- Stat – Status of the eIV Response Record. A “Y” means that the review of the response has been started by someone.
- Following the insurance company name:
- P – the eIV response indicates that the insurance company is the primary insurance
- S – eIV response indicates that the insurance company is the secondary insurance
- T – eIV response indicates that the insurance company is the tertiary insurance

Sample Medicare Potential COB Worklist

Medicare Potential COB List Dec 10, 2013@13:47:22 Page: 1 of 1

Sorted in Chronological Order.

---Resp Rcv--Subscriber----------DOB------Stat-INS COMPANY-------------------

03/14/13

1 IB,PATIENT A SR 0150P 01/01/50 Y INSURANCE COMPANY ONE (P)

INSURANCE COMPANY TWO

----------\*Exact Match-------------------------------------------------------

EE Expand Entry

Select Action: Quit// EE

Once an entry is selected and expanded by using the EE – Expand Entry action, additional actions are available to the user.

Sample Medicare Potential COB Worklist – Expanded Entry

Medicare Potential COB List Jan 06, 2014@07:16:26 Page: 1 of 1

Patient: IB,PATIENT A SR In Process

Code Payer

----------------------------------------------------------------------------

P INSURANCE COMPANY ONE

111 MAIN STREET

ANYCITY, TX 999991111

Phone: 1112223333

Website: www.INSURANCECOMPANYONE.com

INSURANCE COMPANY TWO

222 MAIN STREET

ANYCITY, TX 888882222

Phone: 4445556666

Website: www.INSURANCECOMPANYTWO.com

Comments:

No Comments Entered.

\*Exact Match

CS Change Status AC Add Comments

Select Action: Quit//

The CS – Change Status action is used to change the status of the record.

The AC – Add Comments action is used to enter comments.

### Medicare Potential COB – as a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information displayed on the Medicare Potential COB directly depends on which “Report Type” was selected. The header of the report reflects the selected date range and Report Type.

Sample Medicare Potential COB Report

Pt. Secondary Insurance Report Jul 23, 2013@18:02:01 Page: 1

Sort: Chronological Order 06/23/2013 - 07/23/2013

Includes Completed Entries

IB,PATIENT 03/09/1935 Review Status: Complete

----------------------------------------------------------------------------

INSURANCE COMPANY ONE.,

111 MAIN STREET

ANYCITY, TX 999991111

Phone: 1112223333

Website: www.INSURANCECOMPANYONE.com

IB,PATIENT 03/09/1935 2

---------------------------------------------------------------------------

INSURANCE COMPANY TWO, 222 MAIN STREET

ANYCITY, TX 999991111

Phone: 1112223333

Website: www.INSURANCECOMPANYTWO.com

IB,PATIENT 03/09/1935 2

----------------------------------------------------------------------------

INSURANCE COMPANY THREE,

333 MAIN STREET

ANYCITY, TX 999991111

Phone: 1112223333

Website: www.INSURANCECOMPANYTHREE.com

\*\*\* END OF REPORT \*\*\*

## eIV Statistical Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is used to monitor the eIV and IIU process including statistics based on outgoing inquiries, incoming responses, pending responses and queued inquiries, etc.

This report should be monitored on a daily basis as it provides users the ability to detect eIV and IIU communication problems with the FSC in addition to potential problems in the configuration of the eIV and IIU Site Parameters. It also provides users with a quick view of new eIV and IIU associated payers and a summary of the insurance buffer entries.

This report is distributed daily as a MailMan message to the members of the mail group that is defined in the IB Site Parameters. The MailMan version covers the most recent 24 hours and is based on the default report parameters. The MailMan message is only sent when enabled through the IB Site Parameters.

Report Parameters

- Date Range with Time
- Sections to Display: All, Outgoing Data, Incoming Data, Current Status / Payer Activity

Sample Report

eIV Statistical Report Jul 19, 2018@14:04:10 Page: 1

Report Timeframe: 07/19/2018 06:00 - 07/19/2018 14:04

Outgoing Data (Inquiries Sent) 15

=============

Insurance Buffer 2

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 5

EICD-Triggered eInsurance Verification 8

MBI Inquiry 0

Incoming Data (Responses Received) 15

=============

Insurance Buffer 2

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 5

EICD-Triggered eInsurance Verification 8

MBI Response 0

Current Status

==============

Responses Pending: 0

Insurance Buffer 0

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 0

EICD-Triggered eInsurance Verification 0

MBI Inquiry 0

Queued Inquiries: 0

Deferred Inquiries: 0

Insurance Companies w/o National ID: 723

eIV Payers 'Locally Enabled' is NO: 43

IIU Payers 'Receive IIU Data' is NO: 9

Insurance Buffer Entries: 450

User Action Required: 177

\# of + entries (Payer indicated Active policy) 102

\# of \$ entries (Escalated, Active policy) 1

\# of % entries (MBI value received) 0

\# of - entries (Payer indicated Inactive policy) 15

\# of \# entries (Policy status undetermined) 33

\# of ! entries (eIV needs user assistance for entry) 14

Entries Awaiting Processing: 225

\# of ? entries (eIV is waiting for a response) 0

\# of blank entries (yet to be processed or accepted) 225

Payer Activity (During Report Date Range)

==============

New eIV Payers received:

------------------------

Please link the associated active insurance companies to these payers at your

earliest convenience. Locally enable the payers after you link insurance

companies to them. For further details regarding this process, please refer

to the Electronic Insurance Verification User Guide.

1199 NATIONAL BENEFIT FUND

AARP HEALTH PLAN

ACORDIA NATIONAL-MOHWK/HCKRY SPRGS

ACS BENEFIT SERVICES

WRITERS GUILD

eIV Payers - FSC changed the 'Nationally Enabled' field:

--------------------------------------------------------

1199 NATIONAL BENEFIT FUND 02/13/2015@11:39:40 Set: ON

1199 NATIONAL BENEFIT FUND 02/12/2015@15:25:26 Set: OFF

1199 NATIONAL BENEFIT FUND 02/12/2015@14:56:12 Set: ON

1199 NATIONAL BENEFIT FUND 02/12/2015@14:34:20 Set: OFF

eIV Payers - FSC changed the 'Auto Update' field:

-------------------------------------------------

No information available

New IIU Payers received:

------------------------

Please review the payer linking for the associated active insurance companies

to these payers at your earliest convenience. To receive incoming IIU records

from other VAMCs into your buffer, turn ON the 'Receive IIU Data' field for

the payers. For further details regarding this process, please refer to the

Electronic Insurance Verification User Guide.

AETNA

CIGNA

CMS

IIU Payers - FSC changed the 'Nationally Enabled' field:

--------------------------------------------------------

AETNA 06/10/2021@13:20:51 Set: ON

AETNA 06/10/2021@13:19:52 Set: OFF

CIGNA 06/10/2021@13:29:57 Set: OFF

\*\*\* END OF REPORT \*\*\*

## MailMan Summaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA automatically produces a daily MailMan message with a copy of the eIV Statistical Report summarizing the eIV activity for the preceding 24 hours. This mail message will be sent to those in the pre-determined mail group that is designated in the general parameters section of the IB Site Parameter.

Sample - eIV Statistical Report in MailMan Message

Subj: \*\* eIV Statistical Rpt \*\* \[#316226\] 06/12/21@07:00 76 lines

From: EIV INTERFACE (IB) In 'IN' basket. Page 1

-------------------------------------------------------------------------------

eIV Statistical Report Jun 12, 2021@07:00:07 Page: 1

Report Timeframe: 06/11/2021 07:00 - 06/12/2021 07:00

Outgoing Data (Inquiries Sent) 2

=============

Insurance Buffer 2

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 0

EICD-Triggered eInsurance Verification 0

MBI Inquiry 0

Incoming Data (Responses Received) 2

=============

Insurance Buffer 2

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 0

EICD-Triggered eInsurance Verification 0

MBI Response 0

Current Status

==============

Responses Pending: 0

Insurance Buffer 0

Appointment 0

Electronic Insurance Coverage Discovery (EICD) 0

EICD-Triggered eInsurance Verification 0

MBI Inquiry 0

Queued Inquiries: 1

Deferred Inquiries: 0

Insurance Companies w/o National ID: 706

eIV Payers 'Locally Enabled' is NO: 41

IIU Payers 'Receive IIU Data' is NO: 7

Insurance Buffer Entries: 2

User Action Required: 2

\# of + entries (Payer indicated Active policy) 2

\# of \$ entries (Escalated, Active policy) 0

\# of % entries (MBI value received) 0

\# of - entries (Payer indicated Inactive policy) 0

\# of \# entries (Policy status undetermined) 0

\# of ! entries (eIV needs user assistance for entry) 0

Entries Awaiting Processing: 0

\# of ? entries (eIV is waiting for a response) 0

\# of blank entries (yet to be processed or accepted) 0

Payer Activity (During Report Date Range)

==============

New eIV Payers received:

------------------------

No new eIV Payers added

eIV Payers - FSC changed the 'Nationally Enabled' field:

--------------------------------------------------------

No information available

eIV Payers - FSC changed the 'Auto Update' field:

-------------------------------------------------

No information available

New IIU Payers received:

------------------------

No new IIU Payers added

IIU Payers - FSC changed the 'Nationally Enabled' field:

--------------------------------------------------------

No information available

\*\*\* END OF REPORT \*\*\*

## MailMan Notification to Link Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA automatically triggers a mailman message on a weekly basis to the IBCNE EIV Message Mail group if the following information is available:

- Total Number of Nationally Active Unlinked Payers with Potential Matches to active insurance companies.

Sample MailMan Notification

Subj: ACTION REQ: POTENTIAL PAYERS TO BE LINKED  \[#159564\] 01/14/11@10:46

7 lines

From: EIV INTERFACE (IB)  In 'IN' basket. Page 1  \*New\*

-------------------------------------------------------------------------------

TOTAL NUMBER OF PAYERS WITH POTENTIAL INSURANCE COMPANY MATCHES: 4

Immediate Attention Required:

-----------------------------

Please link the associated active insurance companies to these payers at your

earliest convenience. Please visit the e-Business Projects Webpage on VistA

University Website to download the Link Payer Instructions.

Enter message action (in IN basket): Ignore//

## MailMan Notification to Activate Payers 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA automatically triggers a mailman message on a weekly basis to IBCNE EIV MESSAGE mail group if the following information is available:

- A List of Payers that meet the following criteria:
- eIV Locally Not Enabled
- eIV Nationally Enabled

Sample MailMan Notification

subj: ACTION REQ: PAYERS TO BE LOCALLY ACTIVATED  \[#159565\] 01/14/11@10:46

12 lines

From: EIV INTERFACE (IB) In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Nationally Active Payers that are Locally Inactive:

---------------------------------------------------

INSURANCE ONE

INSURANCE TWO

INSURANCE THREE

INSURANCE FOUR

INSURANCEFIVE Immediate Attention Required:

-----------------------------

Please locally activate the payers after you link insurance companies to them.

Please visit the e-Business Projects Webpage on VistA University Website to

download the Payer Activation Instructions.

Enter message action (in IN basket): Ignore//

## eIV Ambiguous Policy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of Report

This report allows users to view ambiguous payer 270 Health Care Eligibility Benefits Responses. Ambiguous payer responses are those responses that do not have enough information for eIV to safely determine if the policy is active or not active.

Report Parameters

Search Criteria:

- Response Received Date Range
- All or Selected Payers
- All or Selected Patients
- All Responses or Most Recent (for a payer/patient combination)

Sort Criteria:

- Payer Name
- Patient Name

Sample Report

eIV Ambiguous Policy Report

Please select a date range in which ambiguous responses were received to view the associated response detail. Date range selection is based on the date that eIV receives the response from the payer.

Start DATE: T-10000 (FEB 22, 1986)

End DATE: T (JUL 10, 2013)

Payer or \<Return\> for All Payers:

Patient or \<Return\> for All Patients:

Select one of the following:

A All Responses

M Most Recent Responses

Select the type of responses to display: A// ll Responses

Select one of the following:

1 Payer Name

2 Patient Name

Select the primary sort field: 1// Payer Name

DEVICE: HOME//

Compiling report data ...

eIV Ambiguous Policy Report Jul 10, 2013@12:19:19 Page: 1

Sorted by: Payer Name Responses Displayed: All

02/22/1986 - 07/10/2013

All Payers

All Patients

Payer: IBINSURANCE2

Patient: IB,PATIENT (SSN: xxx-xx-xxxx DOB: XX/XX/XXXX)

Subscriber: IB,PATIENT

Subscriber ID: XXXXXXXXX

Subscriber DOB:

Subscriber SSN: XX-XXX-XXXX Subscriber Sex:

Group Name:

Group ID:

Whose Insurance:

Member ID: COB:

Service Date: 11/19/2003 Date of Death:

Effective Date: Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: 02/17/2004 Trace \#: XXXXXXXXX

eIV Ambiguous Policy Report Jul 10, 2013@12:19:34 Page: 2

Sorted by: Payer Name Responses Displayed: All

Payer: IBINSURANCE2

Patient: IB,PATIENT (SSN: xxx-xx-xxxx DOB: XX/XX/XXXX)

\*\*\* END OF REPORT \*\*\*

## eIV Inactive Policy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of Report

This report displays any inactive insurance policies that the eIV software identified while making 270 Health Care Eligibility Benefits Inquiries.

Users have the ability to define which inactive policies are included in the report based on the reported policy expiration date. This allows users the ability to search for inactive policies that expired within the payer’s filing timeframe.

Report Parameters

Search Criteria:

- Response Received Date Range
- All or Selected Payers
- All or Selected Patients
- All Responses or Most Recent (for a payer/patient combination)

Sort Criteria:

- Payer or Patient

Sample Report

eIV Inactive Policy Report

Please select a date range in which inactive responses were received to view the

associated response detail. Date range selection is based on the date that

eIV receives the response from the payer.

Start DATE: T-10000 (FEB 22, 1986)

End DATE: T (JUL 10, 2013)

Payer or \<Return\> for All Payers:

Patient or \<Return\> for All Patients:

Select one of the following:

A All Responses

M Most Recent Responses

Select the type of responses to display: A// ll Responses

Select one of the following:

1 Payer Name

2 Patient Name

Select the primary sort field: 1// Payer Name

DEVICE: HOME//

Compiling report data ...

eIV Inactive Policy Report Jul 10, 2013@12:23:57 Page: 1

Sorted by: Payer Name Responses Displayed: All

02/22/1986 - 07/10/2013

All Payers

All Patients

Payer: IBINSURANCE2

Patient: Patient,One (SSN: xxx-xx-xxxx DOB: XX/XX/XXXX)

)

Subscriber: Patient,One

Subscriber ID:

Subscriber DOB:

Subscriber SSN: XXXXXXXXX Subscriber Sex:

Group Name:

Group ID:

Whose Insurance:

Member ID: COB:

Service Date: 11/19/2003 Date of Death:

Effective Date: Certification Date:

Expiration Date: Payer Updated Policy:

Response Date: 02/17/2004 Trace \#: XXXXXXXXX

Payer: IBINSURANCE2

\*\*\* END OF REPORT \*\*\*

# Insurance Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under the Patient Insurance Menu, the Insurance Reports option holds most insurance related reports. Some of the eIV related reports are listed below.

## List Group Plans without Annual Benefits Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report will generate a list of group insurance plans by company without annual benefits for the year requested. The definition of "without" is: either missing year and/or a year (date) is entered but no values within the Annual Benefits have been completed.

Report Parameters

Search Criteria:

- Annual Benefit Year
- All or Selected Insurance Companies
- All or Selected Group Plans

Sort Criteria:

- Insurance Company IEN
- Group Plan IEN

This is a 132 column report.

Sample Report

GP List Group Plans without Annual Benefits

This report will generate a list of group insurance plans by company

without annual benefits for the year requested. The definition of

"without" is: either missing year and/or a year (date) is entered

but no values within the AB have been completed.

Select the Annual Benefit Year: 2017// (2017)

There are 5 insurance companies associated with plans.

1\. List All 5 Ins. Companies

2\. List Only Ins. Companies That You Select

SELECT 1 or 2: 2. List Only Ins. Companies That You Select

Select a Filter for Insurance Company:

1\. Active

2\. Inactive

SELECT 1 or 2: 1. Active

There are 5 plans. List all plans for each company? No// NO

Select a Filter for Group:

1\. Active

2\. Inactive

SELECT 1 or 2: 1. Active

Select insurance company: TEST-1 DKFJSDF QWFDKHJWEIFO SDAGSDF

NEW YORK Y

Select another insurance company: ANYONE’S INSURANCE CO. 123 ANYPLACE

ANYCITY TEXAS Y

Select another insurance company:

Insurance Company \# 1: ANYONE’S INSURANCE CO.

...OK? YES// ...building a list of plans...

Insurance Plan Lookup May 21, 2015@14:44:48 Page: 1 of 1

All Active Plans for: ANYONE’S INSURANCE CO. Phone: \<not filed\>

123 ANYPLACE Precerts: \<not filed\>

ANYCITY, TX 00001

\# + =\> Indiv. Plan Pre- Pre- Ben

Group Name Group Number Type of Plan UR? Ct? ExC? As?

ANYONE’S GROUP K-3900 DENTAL INSURA UNK UNK UNK UNK

Enter ?? for more actions

SP Select PlanSelect Action: Quit// SP Select Plan

Select Plan(s): (1-1): 1

Would you like to select any other plans? NO//

Insurance Company \# 2: TEST-1

...OK? YES// ...building a list of plans...

Insurance Plan Lookup May 21, 2015@14:44:54 Page: 1 of 1

All Active Plans for: TEST-1 Phone: \<not filed\>

DKFJSDF QWFDKHJWEIFO Precerts: \<not filed\>

SDAGSDF, NY 12233

\# + =\> Indiv. Plan Pre- Pre- Ben

Group Name Group Number Type of Plan UR? Ct? ExC? As?

GROUP 1 TEST TEST-1212 MEDICARE SECO NO NO YES YES

Enter ?? for more actions

SP Select PlanSelect Action: Quit// SP Select Plan

Select Plan(s): (1-1): 1

Would you like to select any other plans? NO//

(E)xcel Format or (R)eport Format: Report//

There is 1 insurance company associated with group plans without annual

benefits.

Enter RETURN to continue or '^' to exit:

\*\*\* You will need a 132 column printer for this report. \*\*\*

DEVICE: HOME// ;132 UCX/TELNET

LIST OF GROUP PLANS BY INSURANCE COMPANY WITHOUT ANNUAL BENEFITS MAY 21, 2015@14:45 Page: 1

Benefit Year Selected: 2017

------------------------------------------------------------------------------------------------------------------------------------

INSURANCE COMPANY NAME: TEST-1 PHONE:

DKFJSDF QWFDKHJWEIFO PRECERT PHONE:

SDAGSDF, NY 12233

REIMBURSE TYPE OF COVERAGE GROUP NAME GROUP NUMBER ACTIVE/INACTIVE LAST PERSON TO EDIT TYPE OF PLAN

WILL REIMBURSE GROUP 1 TEST TEST-1212 ACTIVE IBUSER,ONE MEDICARE SECO

Enter RETURN to continue or '^' to exit:

## User Edit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose of this Report

This report is capturing all of the Creates, Edits, and Deletes done by specific users in the following files to certain specific fields:

- Insurance Company File (#36)
- Group Plan File (#355.3)
- Coverage File (#355.32)
- Annual Benefits File (#355.4)
- Payer (#365.12)
- Receive IIU Data (#365.121,5.01)
- Type of Plan (355.3,.09)
- Standard FTF (36,.18)
- Standard FTF Value (36,.19)

Report Parameters

Search Criteria:

- Insurance Company (multiple select)
- Group Plan (multiple select)
- Payer (multiple select)
- Date Range
- User ID (one, multiple, all)

This is a 132 column report.

Sample Report – Selecting Insurance Company

Select one of the following:

1\. User Edits for Insurance Company/Group Plan

2\. User Edits for Payers

3\. BOTH

Select 1 or 2 or 3: 1// 1 INSURANCE COMPANY/GROUP PLAN

Insurance Company Selection:

1\. Report User Edits for all 1564 Insurance Companies

2\. Report User Edits for selected Insurance Companies

ENTER 1 or 2: 2 Report Insurance Companies that are selected

Group Plan Selection:

Do you want to report any edits made to Group Plans (Y/N)? YES

1\. Report User Edits for all Group Insurance Plans

2\. Report User Edits for selected Group Insurance Plans

ENTER 1 or 2: 2 Report Group Insurance Plans that are selected

Select Insurance Company: BLUE CROSS 911 STREET ANYTOWN

CALIFORNIA Y

Select another Insurance Company:

Insurance Company \# 1: BLUE CROSS

...OK? YES//

...building a list of plans...

Insurance Plan Lookup Sep 14, 2015@12:26:10 Page: 1 of 1

All Active Plans for: BLUE CROSS Phone: \<not filed\>

911 STREET Precerts: 877.277.3368

ANYTOWN, CA 99999

\# + =\> Indiv. Plan Pre- Pre- Ben

<u>Group Name Group Number Type of Plan UR? Ct? ExC? As?</u>

1 BLUE CROSS OF CA 1234 HIGH DEDUCTIB NO UNK UNK YES

Enter ?? for more actions

SP Select Plan

Select Action: Quit// SP Select Plan

Select Plan(s): (1-1): 1

Would you like to select any other plans? NO//

User Selection:

1\. All User IDs

2\. Select One or Multiple User IDs

ENTER 1 or 2: 2 Specified Users

Select NEW PERSON NAME: IBUSER,ONE AC

Is IBUSER, ONE the one you want? YES//

Select NEW PERSON NAME:

Start date: 5/13 (MAY 13, 2015)

End date: 6/12 (JUN 12, 2015)

Export to Microsoft Excel (Y/N): ? NO//

\*\*\* You will need a 132 column printer for this report. \*\*\*

DEVICE: HOME// ;132

USER EDIT REPORT Mar 23, 2020@09:17:52 Page: 2

Insurance Company Group Name

User Date/Time of Change Modified Field Previous Value of Data Modified Value of Data

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COVENTRY ADVANTRA(WNR)

IBUSER, ONE 3/19/20 15:20 EDI ID NUMBER - PROF \<no previous value\> 00000

EASTERN SHOSHONE TRIBE BE

IBUSER, TWO 3/20/20 08:38 EDI ID NUMBER - INST \<no previous value\> 13193

EMI HEALTH

IBUSER, THREE 3/20/20 08:39 TRANSMIT ELECTRONICALLY \<no previous value\> YES-LIVE

LOYAL AMERICAN

IBUSER, FOUR 3/20/20 08:13 PAYER LOYAL AMERICAN MEDICARE SUPP

UMR GROUPA

IBUSER, FIVE 6/23/22 13:12 STANDARD FTF DAYS PLUS ONE YEAR MONTH(S)

UNITED GROUPB

IBUSER, SIX 6/23/22 13:12 STANDARD FTF VALUE \<no previous value\> 2

AETNA LAZARO

IBUSER, SEVEN 6/23/22 13:10 TYPE OF PLAN \<no previous value\> COMPREHENSIVE MAJOR MEDICAL

Type \<Enter\> to continue or '^' to exit:

Sample Report – Selecting Payer

Select one of the following:

1\. User Edits for Insurance Company/Group Plan

2\. User Edits for Payers

3\. BOTH

Select 1 or 2 or 3: 1// 2 PAYERS

eIV Payer Selection:

1\. Report User Edits for all Payers

2\. Report User Edits for selected Payers

ENTER 1 or 2: 1 Report all Payers

User Selection:

1\. All User IDs

2\. Select One or Multiple User IDs

ENTER 1 or 2: 1 All Users

Start date: t-30 (FEB 22, 2020)

End date: t (MAR 23, 2020)

Export to Microsoft Excel (Y/N): ? NO//

\*\*\* You will need a 132 column printer for this report. \*\*\*

DEVICE: HOME// HOME (CRT) Right Margin: 132

USER EDIT REPORT Mar 23, 2020@09:45:45 Page: 1

Payer

User Date/Time of Change Modified Field Previous Value of Data Modified Value of Data

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AARP HEALTH PLAN

IBUSER,ONE 3/16/20 14:02:51 LOCAL ACTIVE Not Active Active

AETNA

IBUSER,ONE 3/16/20 14:11:02 LOCAL ACTIVE Active Not Active

END OF REPORT

Sample Report – Selecting Both

Select Insurance Reports \<TEST ACCOUNT\> Option: AU User Edit Report

Select one of the following:

1\. User Edits for Insurance Company/Group Plan

2\. User Edits for Payers

3\. BOTH

Select 1 or 2 or 3: 1// 3 BOTH

Insurance Company Selection:

1\. Report User Edits for all 1564 Insurance Companies

2\. Report User Edits for selected Insurance Companies

ENTER 1 or 2: 1 Report all Insurance Companies

Group Plan Selection:

Do you want to report any edits made to Group Plans (Y/N)? NO

eIV Payer Selection:

1\. Report User Edits for all Payers

2\. Report User Edits for selected Payers

ENTER 1 or 2: 1 Report all Payers

User Selection:

1\. All User IDs

2\. Select One or Multiple User IDs

ENTER 1 or 2: 1 All Users

Start date: t-60 (JAN 23, 2020)

End date: t (MAR 23, 2020)

Export to Microsoft Excel (Y/N): ? NO//

\*\*\* You will need a 132 column printer for this report. \*\*\*

DEVICE: HOME// HOME (CRT) Right Margin: 132

USER EDIT REPORT Aug 18, 2022@09:28:19 Page: 6

Insurance Company Group Name

User Date/Time of Change Modified Field Previous Value of Data Modified Value of Data

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MED ONE INS CO EDITS

LASTNAME,FIRST 8/4/22 09:13 TRANSMIT ELECTRONICALLY \<no previous value\> YES-LIVE

MED ONE INS CO EDITS

LASTNAME,FIRST 8/4/22 09:17 STANDARD FTF VALUE 12

MED ONE INS CO EDITS

LASTNAME,FIRST 8/4/22 09:17 STANDARD FTF MONTH(S) YEAR(S)

MED ONE HALGREN

LASTNAME,FIRST 8/4/22 09:14 TYPE OF PLAN PRESCRIPTION MANAGED CARE SYSTEM (MCS)

Type \<Enter\> to continue or '^' to exit:

USER EDIT REPORT Mar 23, 2020@09:17:52 Page: 2

Payer

User Date/Time of Change Modified Field Previous Value of Data Modified Value of Data

AARP HEALTH PLAN

IBUSER, ONE 3/16/20 14:02:51 LOCAL ACTIVE Not Active Active

AETNA

IBUSER, ONE 3/16/20 14:11:02 RECEIVE IIU DATA \<no previous value\> YES

END OF REPORT

# Exporting Reports to Excel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users have the ability under most reports to output data in a format that can be opened by Excel.

1.  Run the report of your choice.
131. At the format prompt, choose Excel.

A screen similar the following will be displayed:

Generate Insurance Company Listings^Nov 19, 2020@08:03:45

List of All Insurance Companies^where NAME Between Aet and Cigna

Active/Inactive^Insurance Name^Reimburse?^Street Address 1^Street Address 2^Stre

et Address 3^City^State^ZIP^Phone Number

Active^BALL AEROSPACE^WILL REIMBURSE^PO BOX 1235^^^BROOMFIELD^CO^80038^303/460-2

453

Active^BANKER FIDELITY^WILL REIMBURSE^PO BOX 105652^^^ATLANTA^GA^30348^

Active^BANKERS FIDELITY^WILL REIMBURSE^PO BOX 105652^^^ATLANTA^GA^30348^

Active^BANKERS LIFE & CASUALTY^WILL REIMBURSE^PO BOX 1935^^^CARMEL^IN^46082-1935

^800 621-3724

Active^BANKERS LIFE & CASUALTY^WILL REIMBURSE^PO BOX 37504^^^OAK PARK^MI^48237-0

504^810/826-4300

Active^BANKERS LIFE & CASUALTY^WILL REIMBURSE^PO BOX 66994^^^CHICAGO^IL^60666-09

94^

Active^BANNER CHOICE PLUS^WILL REIMBURSE^PO BOX 16423^^^MESA^AZ^85211^800 827-24

64 OPT 5

Active^BANNER HEALTH SYSTEMS^WILL REIMBURSE^PO BOX 9239^^^FARGO^ND^58106^

Active^BC/BS RX CARE WYOMING^WILL REIMBURSE^PO BOX 2266^^^CHEYENNE^WY^82003^800

424-7094

Enter RETURN to continue or '^' to exit:

132. Capture the output as a text file.
39. The above step will depend on the terminal emulation application being used.
133. Open a blank worksheet in Excel, select the Data tab, select the From Text / CSV button from the Get & Transform Data section. (These instructions vary on Excel version. This is Office 365.)

<span id="_Toc121848907" class="anchor"></span>Figure 4: Open Dialog Box

![](ib-2-electronic-insurance-verification-eiv-and-interfacility-insurance-update-ii/002.png)

134. Open the text file saved in step 3.

The following screen will be displayed.

<span id="_Toc121848908" class="anchor"></span>Figure 5: Opened File

![](ib-2-electronic-insurance-verification-eiv-and-interfacility-insurance-update-ii/003.png)

135. Choose Delimiter, select Custom and enter “^”, and press Load.
136. Apply any special formatting.
137. Press the Finish button.
138. Depending on your version of Excel, an Import Data dialog may display. If it does, select the New worksheet and OK.
139. Save the Excel file.

# Schedule / Unschedule MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This existing feature allows users to schedule and unscheduled MailMan messages to their preference. Both Activate Payer and Link Payer messages can be scheduled using this option Unlinked payers notification \[IBCNE EIV PAYER LINK NOTIFY\] option.

40. This option is controlled by IRM access only.

The following screens will be displayed:

Select OPTION to schedule or reschedule: IBCNE EIV

1 IBCNE EIV PAYER LINK NOTIFY Unlinked payers notification

Schedule/Unschedule Options

Select OPTION to schedule or reschedule: unlinked PAYERS NOTIFICATION IBCNE EIV

PAYER LINK NOTIFY Unlinked payers notification

Are you adding 'IBCNE EIV PAYER LINK NOTIFY' as

a new OPTION SCHEDULING (the 503RD)? No//Y

Edit Option Schedule

Option Name: IBCNE EIV PAYER LINK NOTIFY

Menu Text: Unlinked payers notification TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MMM DD, YYYY@HH:MM

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 7D

TASK PARAMETERS:

SPECIAL QUEUEING: \< This field is only for special jobs:

1\. That need to start every time the system is rebooted.

2\. Need to be persistent.

3\. BOTH \>

MAIL CODE:

# Real Time Insurance Verification Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A real time eligibility verification inquiry is created when a new buffer entry has been entered in the INSURANCE VERIFICATION PROCESSOR file \#355.33 (buffer). The inquiry is triggered immediately if the following information is available in the buffer entry:

- INSURANCE COMPANY NAME,
- PATIENT NAME,
- SUBSCRIBER ID (if patient is the subscriber),
- INSURED'S DOB (if patient is not the subscriber), and
- PATIENT ID (if patient is not the subscriber)

No inquiry will be created if:

- An inquiry already exists in the queue waiting to be transmitted.
- The same patient and policy is waiting for a response from the payer.
- The patient insurance information is locked by another user.
- The 270 Master Switch Realtime field (#350.9, 51.27) is set to NO.
- Displayed as “Master Switch Realtime” under the eIV site parameters.

Real time inquiry is triggered by modifications to the following fields in the buffer:

- INSURANCE COMPANY NAME; or
- GROUP NAME; or
- GROUP NUMBER; or
- PATIENT NAME; or
- SUBSCRIBER ID; or
- INSURED'S DOB; or
- PATIENT ID
41. Remember – To utilize the benefit of real-time verification and get immediate responses, the facility should set the “HL7 Response Processing Method” to “Immediate”.

    Remember – The Request Electronic Inquiry option can be used to create a buffer entry for real-time verification. The response received for buffer entries created by EI; stay in the buffer and never automatically updates the patient insurance file.

    Remember – Real time verification inquiries are not triggered for buffer entries created by HMS data upload. Source = HMS

    Remember – The system does not send a registration request message to FSC each time a real time insurance verification is triggered.

    Remember – If the 270 Master Switch Realtime is set to NO, then the inquiry will be added to the buffer but will not transmit to the payer until the eInsurance Night Process runs. The eInsurance Night Process will not run if the 270 Master Switch Nightly field (#350.9, 51.28) is set to NO. (Displayed as “Master Switch Nightly” under the eIV site parameters.)

# Purging eIV Files (IRM Users)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purge Transmission Queue and or Response File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM users have the ability to purge files from the IIV TRANSMISSION QUEUE file (#365.1) and IIV RESPONSE file (#365) beyond a date range. The Purge eIV Transactions option is on the Purge Menu which is on the System Manager's Integrated Billing Menu.

1.  Access the IRM System Manager’s Integrated Billing Menu.
140. Access the Purge Menu.
141. Access the Purge eIV Transactions option.
42. Purged data can fill journal files if the files are not purged routinely. It may be a good idea to temporarily disable journaling of the global that includes the IIV TRANSMISSION QUEUE (#365.1) and IIV RESPONSE (#365) files prior to running the purge if the files have not been purged in a long time.

    The Purge eIV Transactions option is locked with the XUMGR security key.

The following screen will be displayed:

Purge Electronic Insurance Identification and Verification (IIV) Data Files

This option will allow you to purge data from the IIV Response File (#365)

and the IIV Transmission Queue File (#365.1). The data must be at least six

months old before it can be purged. Only insurance transactions that have a

transmission status of "Response Received", "Communication Failure", or

"Cancelled" may be purged. You will be allowed to select a date range for

this purging. The default beginning date will be the date of the oldest

eligible record in the system. The default ending date will be six months

ago from today's date. You may modify this default date range. However, you

may not select an ending date that is more recent than six months ago.

Enter the purge begin date: 10/04/2004// 3/8/09 (MAR 8, 2009)

Enter the purge end date: 04/08/2009// (APR 08, 2009)

You want to purge all IIV data created between 03/08/2004 and 04/08/2009.

OK to continue? NO//

142. At the Enter the Purge Begin Date: prompt, enter 6 Months plus 30 days for this example.
143. At the Enter the Purge End Date: prompt, press RETURN to accept the default.
144. At the OK to continue: prompt, enter YES.
43. Files that are not older than six months cannot be purged.

## Purge Mailman Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the first day of each month, during the nightly batch extract process, the eIV application determines if historical data exists that is eligible to be purged. The process utilizes the same search criteria used by the Purge eIV Transactions utility described above. If at least one eligible eIV transaction exists, the mail group defined in the General Parameters section of the IB Site Parameters will receive the following MailMan reminder.

Subj: eIV Data Eligible for Purge \[#13511224\] 11/06/03@17:37 13 lines

From: IB IIV INTERFACE In 'IN' basket. Page 1

Subject: eIV Data Eligible for Purge

ATTENTION IRM: There are eIV TRANSMISSION QUEUE and

eIV RESPONSE records eligible to be purged.

File Eligible Total

Count Count

------------------------------------ -------- --------

IIV RESPONSE FILE (#365) 267 1993

IIV TRANSMISSION QUEUE FILE (#365.1) 331 2400

==================================== ======== ========

Total 598 4393

Please run option IBCNE PURGE IIV DATA - Purge eIV Transactions,

if you would like to purge the eligible records.

# Appendix A – eIV Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## No eIV Inquiries Transmitted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Inquiries Sent and Responses Received entries on the eIV Statistical Report both remain at zero while the Queued Inquiries entry on the report continues to increase over a period of time, then no 270 Health Care Eligibility Benefits Inquiry transmissions are being sent to FSC. If this situation continues and both the Inquiries Sent and Responses Received entries remain at zero, there is a communications problem with FSC. This section provides information to restore connectivity to FSC.

The eIV Statistical report should be reviewed the following day to ensure that 270 Health Care Eligibility Benefits Inquiry transmissions are once again being sent to FSC.

### Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Verify MCCR Site Parameters
- Check Insurance Verification site parameters (IV) \>\> General Parameters (non-editable)
  - Mail Group must be: IBCNE EIV MESSAGE
    - IBCNE EIV MESSAGE mail group must be populated with valid personnel

### Restoring Connectivity to FSC (IRM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Verify that the names of the HL7 Logical Links were not changed. It must be IIV EC.
- Verify the following settings for the HL7 Logical Link IIV EC.
- The institution field is blank.
- The AUTOSTART field is set to enabled.
- For help with the settings for the following fields, please contact the eInsurance Rapid Response team.
  - The domain field
  - The TCP / IP address
  - The TCP / IP port
- Verify that the HL7 Logical Link IIV EC is running.
- Ask the IB Supervisor or insurance personnel to review the eIV Statistical Report the following day and confirm that connectivity has been restored with FSC.
- If this does not resolve the connectivity issue with FSC for eIV, ask the IB Supervisor or insurance personnel to log a Remedy Ticket with VA Product Support.

### Requeue Batch Process (IRM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Verify the eInsurance Night Process \[IBCN EINSURANCE NIGHT PROCESS\] is still a scheduled option in Taskman.
- Reschedule the \[IBCN EINSURANCE NIGHT PROCESS\] task matching the settings (frequency, date / time to run) of another VAMC production site.

### Restart HL7 Logical Link (IRM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Verify the “IIV EC” HL7 logical link is running.
- Stop & Restart “IIV EC” HL7 logical link.

## No link between an Insurance Company and a Payer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For eIV to work, insurance companies must be linked to a payer. This is an important on-going process. To link insurance companies to a payer, follow the basic guidelines listed below:

- Run the Insurance Company Link Report for all unlinked insurance companies. Use the keyword feature when running the report to narrow down the search. This will provide a report showing which insurance companies, whose name contains the keyword, that are not linked to a payer.
- Next, use the [Insurance Company Entry/Edit](#_Insurance_Company_Entry/Edit) option to link those insurance companies to the correct payer.

## A Buffer or Appointment Extract Entry Failed to Create an Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the eIV process is unable to create and transmit a 270 Health Care Eligibility Benefits Inquiry to a payer, the entry in Process Insurance Buffer will be flagged with an exclamation point. To view the error or problem that eIV encountered, expand the buffer entry using the Expand Entry action. Underneath the section Buffer Entry Information, the error message will be displayed as the Current eIV Status. Read the explanation of the problem. Sometimes there is more than one way to correct the problem. For a possible solution, follow the instructions listed below for the specific error. These instructions usually start with, Action to take.

For a list of all Error Messages that may display as the Current eIV Status of an insurance buffer entry, see Appendix B – eIV Error Message Descriptions.

# Appendix B – eIV Error Message Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  eIV could not create an inquiry for this entry. eIV could not match the insurance company name in the Insurance Buffer file (#355.33) to a valid insurance company name in the Insurance Company file (#36).

*Action to take:* Correct the spelling of the insurance company name found in the buffer so that it matches one found in the Insurance Company file (#36). Otherwise, contact the insurance company to manually verify this insurance information.

145. eIV could not create an inquiry for this entry. eIV matched the insurance company name in the Insurance Buffer file (#355.33) to more than one uniquely named insurance company in the Insurance Company file (#36). This indicates that the Auto Match check or the Synonym check yielded multiple insurance companies from the Insurance Company file.

*Action to take*: Correct the spelling of the insurance company name found in the buffer so that it matches one found in the Insurance Company file (#36). Otherwise, contact the insurance company to manually verify this insurance information. (\* Advanced users: Use the option “Enter/Edit Auto Match Entries” to check the entries in the Auto Match file (#365.11). Make sure there is no more than one entry in the Auto Match file, if any, which corresponds to the insurance company name found in this buffer entry.)

146. eIV could not create an inquiry for this entry. eIV matched the insurance company name in the Insurance Buffer file (#355.33) to more than one insurance company entry with the same name in the Insurance Company file (#36). At least one of these matching entries are linked to a different payer.

*Action to take:* Run the “eIV Payer Link Report” option by Insurance Company List, for all linked insurance companies, using the keyword feature to narrow down the search. This will provide a report showing which payer the different insurance company records are linked to. Next, use the “Insurance Company Entry/Edit” option to correct those insurance companies who are linked to the wrong payer.

147. eIV could not create an inquiry for this entry. There is no link for this insurance company between the Insurance Company file (#36) and the Payer file (#365.12). This may occur because the insurance staff did not attempt to manually link the named insurance company to the payer list or the insurance staff did not find a payer in the payer list that they wanted to link this insurance company to.

*Action to take:* Either contact the insurance company to manually verify this insurance information or link the insurance company to a payer. Steps to link an insurance company to a payer are as follows: run the “eIV Payer Link Report” option by Insurance Company List, for all unlinked insurance companies. Use the keyword feature when running the report to narrow down the search. This will provide a report showing which insurance companies are not linked to a payer. Next, use the “Insurance Company Entry/Edit” option to link those insurance companies to the correct payer.

148. eIV could not create an inquiry for this entry. The payer is not nationally enabled for eIV.

*Action to take:* Contact the insurance company to manually verify this insurance information.

149. eIV could not create an inquiry for this entry. The payer is not locally enabled for eIV.

*Action to take:* Either use the option “Payer Edit” to locally enable this payer or contact the insurance company to manually verify this insurance information.

150. eIV could not create an inquiry for this entry. The payer does not accept electronic insurance eligibility requests. The eIV application data does not exist in the Payer file (#365.12) for this payer.

*Action to take:* Contact the insurance company to manually verify this insurance information.

151. Information received via electronic inquiry indicates patient has active insurance.

*Action to take:* Review the details listed in the eIV Response Report before processing this buffer entry.

152. Information received via electronic inquiry indicates patient does NOT have active insurance.

*Action to take:* Review the details listed in the eIV Response Report before processing this buffer entry.

153. This buffer entry is currently still being processed by the eIV application. Unless instructed otherwise, there is no reason you should do anything with this buffer entry.

*Action to take*: None.

154. The electronic response indicated an error of some kind that needs to be corrected before the insurance inquiry can be re-transmitted.

*Action to take:* Contact the insurance company to manually verify this insurance information.

155. An unknown and unforeseen error has occurred with this entry.

*Action to take:* Please call the Help Desk for this issue; include a trace number if available.

156. eIV could not create an inquiry for this entry. The insurance company found is listed as inactive in the Insurance Company file (#36).

*Action to take:* Contact the insurance company to manually verify this insurance information.

157. eIV could not create an inquiry for this entry. eIV cannot send inquiries to Medicaid.

*Action to take:* Contact the insurance company to manually verify this insurance information.

158. eIV was unable to electronically verify this insurance information due to a communication failure.

*Action to take:* Contact the insurance company to manually verify this insurance information.

159. The insurance company name for this buffer entry is blank.*Action to take:* Please call the Help Desk and provide them with buffer information and trace number, if available.
160. eIV could not create an inquiry for this entry. The payer associated with this insurance company has been deactivated.

*Action to take:* Either edit this insurance company and link it to another payer, using the “Insurance Company Entry/Edit” option; otherwise, contact the insurance company to manually verify this insurance information.

161. eIV could not create an inquiry for this entry. This inquiry requires the Subscriber ID field to be populated before an inquiry can be transmitted electronically.

*Action to take:* Update the inquiry with the missing Subscriber ID or contact the insurance company to manually verify this insurance information.

162. An ambiguous response has been received. It could NOT be determined whether the insurance company identified the patient as an active member of the insurance plan. Please contact the insurance company to manually verify this insurance information.

*Action to take:* Review the details listed in the eIV Response Report and contact the insurance company to manually verify this insurance information.

163. While processing a payer response, an unknown and unforeseen error has occurred with this entry.*Action to take:* Please call the Help Desk for this issue; include a trace number if available. A user may process this buffer entry if a Help Desk call has been logged with the associated trace number. To process this buffer entry, review the details listed in the eIV Response Report and contact the insurance company to manually verify this insurance information.
164. eIV could not create an inquiry for this entry. This dependent inquiry requires the Patient ID field to be populated before an inquiry can be transmitted electronically.

*Action to take*: Update the inquiry with the missing Patient ID or contact the insurance company to manually verify this insurance information.

165. eIV was unable to electronically verify this insurance information due to a communication failure.*Action to take:* Contact the insurance company to manually verify this insurance information.
166. Information received via electronic inquiry indicates patient has active insurance; however, another verifier did not have the authority to process this entry.*Action to take:* Review the details listed in the eIV Response Report before processing this buffer entry.
167. eIV was unable to electronically verify this insurance information as invalid characters were identified in a required field(s).*Action to take:* Contact the insurance company to manually verify this insurance information.
44. Error messages 26 and 27 intentionally omitted.

# Appendix C – Acronyms / Abbreviations / Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term             | Definition                                                                                                                                                                                                                                                                                                 |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AITC             | Austin Information Technology Center.                                                                                                                                                                                                                                                                      |
| EC               | Eligibility Communicator – this refers to the National Health Insurance database that is housed at the FSC. The eIV software communicates with the Eligibility Communicator directly through HL7.                                                                                                          |
| EDI              | Electronic Data Interchange.                                                                                                                                                                                                                                                                               |
| EICD             | Electronic Insurance Coverage Discovery                                                                                                                                                                                                                                                                    |
| eIV              | Electronic Insurance Verification. It is also the Insurance buffer entry source name in the Insurance Buffer List to signal entry processing by Electronic Insurance Verification.                                                                                                                         |
| Freshness Days   | FRESHNESS DAYS (#350.9,51.01) is a general site parameter that determines how recent the insurance verification must be before eIV seeks to electronically re-verify it.                                                                                                                                   |
| FSC              | VA Financial Services Center – Austin, TX.                                                                                                                                                                                                                                                                 |
| HL7              | Health Level Seven, a standardized application level communications protocol that enables systems to exchange information.                                                                                                                                                                                 |
| HMO              | Health Maintenance Organization.                                                                                                                                                                                                                                                                           |
| HPID             | Health Plan Identifier                                                                                                                                                                                                                                                                                     |
| IIU              | Interfacility Insurance Update. This term refers to the automated push of active, verified insurance information in real time from the VistA instance used to verify to the account, to other VistA instances where the Veteran has received care.                                                         |
| IIV              | Insurance Identification and Verification. This nomenclature was used during initial software development. The official title of the software is now eIV, although some programming options are still labeled with the old IIV nomenclature.                                                               |
| Insurance Buffer | The data store within the VistA database that holds proposed permanent insurance file changes for review and acceptance and upon acceptance, merges the changes into the permanent insurance files. The IBCN Insurance Buffer Process option available in VistA is also known as Process Insurance Buffer. |
| IRM              | Information Resource Management.                                                                                                                                                                                                                                                                           |
| MailMan          | MailMan is an integrated data channel in VistA for the distribution of: Patches (KIDS builds), software releases (KIDS builds), computer-to-computer communications (HL7 transfers, Servers, etc.), Person-to-person messaging (Email).                                                                    |
| MCCF             | Medical Care Cost Fund.                                                                                                                                                                                                                                                                                    |
| MCCR             | Medical Care Cost Recovery. This term has been officially replaced by MCCF though both are used interchangeably.                                                                                                                                                                                           |
| OEID             | Other Entity Identifier                                                                                                                                                                                                                                                                                    |
| Payer            | An entity that makes third party payments (the patient is the first party, VHA is the second party) for health care services. Health care insurance companies are payers.                                                                                                                                  |
| Provider         | A term used to describe both human and organizational entities that provide health care.                                                                                                                                                                                                                   |
| SRS              | Software Requirements Specification.                                                                                                                                                                                                                                                                       |
| Trusted Payer    | A payer whose responses, the FSC determines can be used for Automatic Updates. It is also referred to as the Automatic Update Setting.                                                                                                                                                                     |
| VA               | Veterans Administration.                                                                                                                                                                                                                                                                                   |
| VAMC             | Veterans Administration Medical Center.                                                                                                                                                                                                                                                                    |
| VHA              | Veterans Health Administration.                                                                                                                                                                                                                                                                            |
| VISN             | Veterans Integrated Service Network.                                                                                                                                                                                                                                                                       |
| VistA            | Veterans Health Information Systems & Technology Architecture, which includes the systems formerly known as the Decentralized Hospital Computer Program (DHCP) System.                                                                                                                                     |
| WNR              | Will not reimburse.                                                                                                                                                                                                                                                                                        |
| X12              | A standardized application level communications protocol that enables systems to exchange information.                                                                                                                                                                                                     |