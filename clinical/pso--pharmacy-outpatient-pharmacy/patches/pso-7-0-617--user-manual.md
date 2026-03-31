---
title: Inbound ePrescribing User Manual (Unit 1 & Unit 2) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 1 & Unit 2) PSO*7*617 and PSO*7*670
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7.0
patch_id: PSO*7.0*617
group_key: "PSO:PSO:7.0"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of PRE IEP is to enable the VA to receive and subsequently process eR<sub>X</sub>es from outside of VA. This user guide serves as a guide and useful reference for VA Pharmacy Users, Systems Administrators, Managers, and other VA staff to assist in accessing, navigating, and performing ta
audience: 
keywords: 
  - unit
  - span
  - inbound
  - pharmacy
  - eprescribing
  - class
  - table
  - figure
  - message
  - anchor
page_count: 0
word_count: 10346
section_count: 9
table_count: 13
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_1_2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_1_2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/001.png)

November 2021

Version 5.0 (Unit 1 & Unit 2)

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Revision History

<table style="width:100%;">
<caption>This table displays the revision history providing the date, version number and description details.</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 58%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/01/2021</td>
<td>5.0</td>
<td><p>PSO*7.0*617:</p>
<ul>
<li><p>Updated all screen captures with the latest versions</p></li>
<li><p>Included changes related to Controlled Substance and Controlled Substance eRx processing</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>10/20/20</td>
<td>4.0</td>
<td><p>PSO_7_0_p581_UM updated:</p>
<ul>
<li><p>Updated all screen shots with the latest versions</p></li>
<li><p>Added paragraph numbers to all paragraphs</p></li>
<li><p>Updated terminology throughout to comply with NCPDP 2017071 standards</p></li>
<li><p>Added “Prohibit Renewal Request” functionality details under Unit 3</p></li>
<li><p>Added New unit for RxChange Requests and Responses - Unit 5</p></li>
<li><p>Moved CancelRx Requests and Responses under Unit 6</p></li>
<li><p>Added RxRenewal Response – Replace Type under Unit 5</p></li>
<li><p>Added Note for RxVerify functionality under Unit 3</p></li>
<li><p>Added Note for Reject functional under Unit 3</p></li>
</ul></td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>05/05/2020</td>
<td>3.0</td>
<td><p>PSO*7.0*610:</p>
<ul>
<li><p>Added note to indicate a minor change in the display of the Station ID drop-down list in the Reports tab</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>03/23/2020</td>
<td>2.9</td>
<td><p>PSO*7.0*590:</p>
<ul>
<li><p>Added production application <strong>URL</strong></p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>03/05/2020</td>
<td>2.8</td>
<td><p>PSO*7.0*591:</p>
<ul>
<li><p>Updated Figure 3-44 and 3-45</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>08/27/2019</td>
<td>2.7</td>
<td><p>PSO*7.0*567 updated:</p>
<ul>
<li><p>Help Desk contact information/name</p></li>
<li><p>Screen capture dates for ERX Lookback Days beginning with page 108 through 203</p></li>
<li><p>Corrected Figure 3-12 and reworded the bullets above</p></li>
<li><p>Added Figure 3-13</p></li>
<li><p>Title page, TOC, LOF, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>05/07/2019</td>
<td>2.6</td>
<td><p>Updated document for the following:</p>
<ul>
<li><p>Standardized images throughout document</p></li>
<li><p>Clarified patient DOB format under Table 3</p></li>
<li><p>Added Note to replace text “Dispense Notes” with “Substitutions” under Track/Audit Details screen in Section 5 Inbound/Outbound Message Detail</p></li>
<li><p>Added Note to indicate the change of screen/page title from “Users” to “User Management” in section 2.2.5 User Management</p></li>
<li><p>Included description for ERX LOOK-BACK DAYS display on the Holding Queue’s Traditional View and Patient Centric Views in section in section 3.5.1.2.1. Non-Actionable records are those that are in the Holding Queue but are not displayed in the List View. All records acknowledged, removed, rejected, processed/completed and auto-canceled are non-actionable. Non-Actionable records further include:</p></li>
<li><p>R<sub>X</sub>Renewal Request</p></li>
<li><p>R<sub>X</sub>Renewal Response – Approved</p></li>
<li><p>R<sub>X</sub>Renewal Response – Approved with Changes (change to drug data only)</p></li>
<li><p>R<sub>X</sub>Change Request</p></li>
<li><p>CancelR<sub>X</sub> Response</p></li>
<li><p>Inbound Errors related to CancelRx Responses</p></li>
</ul>
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in <u>Appendix B: Holding Queue Status Codes &amp; Descriptions</u> in <a href="#UM_6">Unit 6</a>.</p>
<ul>
<li><p>eR<sub>X</sub> Default Loopback Days</p></li>
<li><p>Replaced column label “LAST USER” with “LOCKED BY” and updated the description under Table 9</p></li>
<li><p>Added the information for LOCKED BY column in section 3.5.2 Patient Centric View</p></li>
<li><p>Replaced Figure 3-14, Figure 3-16, Figure 3-17, Figure 3-18, Figure 3-19, Figure 3-42, Figure 3-52,<br />
Figure 3-55, Figure 3-56, Figure 3-57, Figure 3-59, Figure 3-60, Figure 3-61, and Figure 3-68 for updated layout</p></li>
<li><p>Added Note and included to indicate to the user that a Provider’s DEA# has expired in section 3.6.2.3 Edit Provider</p></li>
<li><p>Removed reference to “Limited Duration” field from Validate Drug/SIG for the modified workflow in section 3.6.3.3 Edit Drug/SIG</p></li>
<li><p>Added description under Note for modified workflow in section 3.6.3.3 Edit Drug/SIG</p></li>
<li><p>Updated description for VistA Days Supply calculation in section 3.6.3.3.1 Additional Field-level Information</p></li>
<li><p>Added scenarios for Quantity/Days Supply workflow under VD Edit screen based on Available Dosage(s) in section 3.6.3.3.2 Quantity/Days Supply work flow under Validate Drug/SIG &gt; Edit:</p></li>
<li><p>Added Note to replace text “Qty Qualifier” with “Code List Qualifier” and replace, “DAW Code” with “Substitutions” in section 3.13 Complete Orders from OERR and Patient Prescription Processing</p></li>
<li><p>Added Note describing eR<sub>X</sub> Date, Date Written, Issue Date, and Written Date fields in section 3.13 Complete Orders from OERR and Patient Prescription Processing</p></li>
</ul></td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>11/09/2018</td>
<td>2.5</td>
<td><ul>
<li><p>Updated per HPS Review pgs. 55, 57, 87, 88, 90, 92, 194, and 195.</p></li>
<li><p>Updated Cover page to month of November (pg. i)<br />
(TWR, 508 accessibility checks, document is compliant)</p></li>
</ul></td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>10/24/2018</td>
<td>2.4</td>
<td>Update TOC – Remove Graphic and reran TOC</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>08/27/2018</td>
<td>2.3</td>
<td>Technical Writer Review and 508 accessibility checks</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>08/01/2018</td>
<td>2.2</td>
<td>Updated screenshots and added R<sub>X</sub>Renewal Requests and Responses and CancelR<sub>X</sub> Requests and Responses sections</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>07/28/2018</td>
<td>2.1</td>
<td>Updated screenshots and added 30-day Lookback</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>4/12/2018</td>
<td>2.0</td>
<td>Updated screenshots to include 2.1 changes</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>11/15/2017</td>
<td>1.0</td>
<td><p>Baseline release:</p>
<ul>
<li><p>Updated Table of Figures</p></li>
<li><p>Updates based on feedback from HPS</p></li>
<li><p>Updated screenshots and verbiage throughout the document, formatting, and sections Inbound ePrescribing Workflow and Summary/Details screen, Pharmacy Management section</p></li>
<li><p>Updates made based on changes made during SureScripts Certification and IOC Production Testing</p></li>
</ul></td>
<td>Technatomy</td>
</tr>
</tbody>
</table>

This table displays the revision history providing the date, version number and description details.

Table of Contents

List of Figures

List of Tables

# Introduction to Inbound ePrescribing


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction to Inbound ePrescribing](#introduction-to-inbound-eprescribing)
  - [Organization of the Inbound ePrescribing User Guide](#organization-of-the-inbound-eprescribing-user-guide)
  - [Inbound ePrescribing Overview](#inbound-eprescribing-overview)
    - [Purpose](#purpose)
    - [Overview](#overview)
    - [User Interfaces](#user-interfaces)
    - [Fillable Prescriptions](#fillable-prescriptions)
    - [Inbound ePrescribing Workflow](#inbound-eprescribing-workflow)
  - [Inbound ePrescribing Architecture](#inbound-eprescribing-architecture)
  - [Roles and Capabilities](#roles-and-capabilities)
  - [Help Desk](#help-desk)
  - [FAX Failover](#fax-failover)
- [Inbound ePrescribing Web-Based Application](#inbound-eprescribing-web-based-application)
  - [Inbound ePrescribing Web-Based Application Overview](#inbound-eprescribing-web-based-application-overview)
    - [Purpose](#purpose-1)
    - [Access Requests](#access-requests)
    - [Accessing the Application](#accessing-the-application)
    - [Screen Navigation and Description](#screen-navigation-and-description)
  - [Inbound ePrescribing Web-based Application Capabilities](#inbound-eprescribing-web-based-application-capabilities)
    - [Pharmacy Management](#pharmacy-management)
    - [Track/Audit](#trackaudit)
    - [Reports](#reports)
    - [Export Reports](#export-reports)
    - [User Management](#user-management)
This unit provides the purpose and organization of the Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) solution.

## Organization of the Inbound ePrescribing User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE IEP user guide is comprised of the following sections:

- [Unit 1 – Introduction to Inbound ePrescribing](#introduction-to-inbound-eprescribing): Discusses general PRE Inbound ePrescribing information.
- <u>Unit 2 - Inbound ePrescribing Web-Based Application</u>: Outlines the IEP web-based application and capabilities, including Pharmacy Management, Track/Audit, Reports, and User Management functions.
- <span id="Unit_3" class="anchor"></span><u>Unit 3 – Inbound eR<sub>X</sub> VistA Outpatient Pharmacy</u>: Discusses the Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy (OP) electronic prescriptions (eR<sub>X</sub>) Holding Queue and capabilities, including eR<sub>X</sub> validation, search, sort, hold, acceptance, remove, and rejection.

  <u>Note:</u> User Manual Unit 3 Part 1 (PSO_7_0_P617_UM_31) and Unit 3 Part 2 (PSO_7_0_P617_UM_32) are available on the Veteran’s Documentation Library (VDL).
- <u>Unit 4 – RxRenewal Requests and Responses:</u> Discusses the RxRenewal Requests and Responses. The RxRenewal Requests function is used by pharmacists to generate and send an outbound RxRenewal Request. After a RxRenewal Request is sent to the external provider, the provider can send a RxRenewal Response back to the requesting Pharmacy.’

  <u>Note:</u> User Manual Unit 4 Part 1 (PSO_7_0_P617_UM_41) and Unit 4 Part 2 (PSO_7_0_P617_UM_42) are available on the Veteran’s Documentation Library (VDL).
- <u>Unit 5 – RxChange Requests and Responses:</u> Discusses the RxChange Requests and Responses. The RxChange Requests function is used by pharmacists to generate and send an outbound RxChange Request. After a RxChange Request has been sent to the external provider, the provider is able to send a RxRenewal Response back to the requesting Pharmacy.

  <u>Note:</u> User Manual Unit 5 Part 1 (PSO_7_0_P617_UM_51) and Unit 5 Part 2 (PSO_7_0_P617_UM_52) are available on the Veteran’s Documentation Library (VDL).
- <u>Unit 6 – CancelRx Requests and Responses:</u> Discusses the CancelRx Request and Response. The CancelRx Request is sent by the external/non-VA Provider for an original NewRx, so it is not processed and dispensed by VA Pharmacy. Upon successfully canceling a NewRx, the VA Pharmacy sends back a CancelRx Response.

  <u>Note:</u> User Manual Unit 6 (PSO_7_0_P617_UM_6) is available on the Veteran’s Documentation Library (VDL).

## Inbound ePrescribing Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE IEP functionality addresses a longstanding need for the Department of Veterans Affairs (VA) to be able to receive and process prescriptions from external providers. This enhancement moves the VA towards increased efficiency and improved customer satisfaction.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of PRE IEP is to enable the VA to receive and subsequently process eR<sub>X</sub>es from outside of VA. This user guide serves as a guide and useful reference for VA Pharmacy Users, Systems Administrators, Managers, and other VA staff to assist in accessing, navigating, and performing tasks associated with the PRE IEP web-based application and the VistA OP eR<sub>X</sub> Holding Queue.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To improve on its ability to deliver Veterans their medications as quickly and efficiently as possible, the Veterans Health Administration (VHA), Patient Care Services (PCS), and Pharmacy Benefits Management (PBM) requested a new capability as part of the PRE program to receive inbound eR<sub>X</sub>es from an external provider (e.g., a doctor not associated with the VA, medical staff at a Department of Defense (DoD) Military Treatment Facility (MTF), etc.).

Overall, PRE IEP provides:

- Improved efficiency. More efficient use of VA pharmacy resources and non-VA provider resources based on:
  - Fewer transcribing/translation errors
  - Clear/error-free communications
  - Time saved not having to communicate back and forth about the content of a prescription
- Improved Veteran/beneficiary satisfaction. Makes the existing manual processing easier, more efficient, and more effective through the automation of the prescription process by:
  - Reducing the risk of loss of paper prescriptions (R<sub>X</sub>es)
  - Enabling more secure communication of R<sub>X</sub> data
  - Providing timelier dispensing of R<sub>X</sub>es prescribed by non-VA providers
- Improved patient safety: Reduces transcription errors
- Improved data accuracy: Provides enhanced functionality within VistA OP that improves the accuracy and use of the data it collects

By automating data transmission from providers to the VA, and between other pharmacies, the need for VA pharmacy personnel to manually input R<sub>X</sub> data from non-VA providers is largely eliminated, reducing the chance for data to be entered incorrectly or missed.

Specific elements of PRE IEP include:

- Receiving and processing inbound eR<sub>X</sub>es, where “inbound” refers to the ordering of medication or medical related supplies for a VA patient by a non-VA provider to be filled at a VA pharmacy.
- Pharmacy Service is not responsible for filling prescriptions for non-expendable medical equipment.
- Pharmacy Service may dispense renewals for expendable supplies upon receipt of requests from patients with continuing eligibility for a period not to exceed one year from the date of the last signed order.
- Expendable stock items may include catheters, colostomy sets, ileostomy sets and/or supplies, plastic and rubber gloves, skin preparations and powders, urinal bags and drainage supplies, incontinence supplies, etc.
- Electronically receiving and processing outpatient prescriptions only, including prescriptions created for a VA patient upon discharge from a non-VA hospital to be filled on an outpatient basis by a VA pharmacy.
- Receiving and processing inbound eR<sub>X</sub>es from non-VA providers that currently prescribe medications and medical-related supplies for Civilian Health and Medical Program of the VA (CHAMPVA) beneficiaries and which are currently handled by the Meds by Mail (MbM) program.
- Sending outbound electronic notifications from a VA pharmacy that received an inbound eR<sub>X</sub>, to the non-VA provider that originally sent the eR<sub>X.</sub>

Areas not included in PRE IEP include:

- VA providers generating eR<sub>X</sub>es at one VA Medical Center (VAMC) location to be electronically transmitted to and processed by (filled, dispensed, etc.) a different VAMC location’s pharmacy.
- Initiating outbound eR<sub>X</sub>es (generation of an eR<sub>X</sub> by a VA provider to be filled at a non-VA pharmacy).
- Electronic receipt and processing of any VA or non-VA inpatient medication orders.
- Electronic receipt and processing of any VA or non-VA orders for Durable Medical Equipment (DME), such as wheelchairs.
- Electronic receipt and processing of RxRenewal Requests from a VA patient’s non-VA Electronic Health Record (EHR) system.
- Electronic transfers of prescriptions from any non-VA pharmacy to a VA pharmacy.
- Electronic transfers of prescriptions from a VA pharmacy to a non-VA pharmacy.

Items out of an eR<sub>X</sub> user’s control and requires validation by Pharmacists include:

- Patient: eR<sub>X</sub>es can be sent for any patient, including Veterans or non-Veterans.
- Provider: eR<sub>X</sub>es can be sent by any provider, whether VA authorized or not.
- Drugs: VA has no control over the drug, nor the name of drug sent to VA.
- SIG: VA has no control over directions that are sent to VA.
- All information coming to the VA is controlled by the EHR system which is what the provider is using to send information to the VA. VA has no control over the process.

### User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two user interfaces associated with IEP, including:

- <u>Inbound ePrescribing Web-Based Application</u>
- <u>Inbound eRX VistA Outpatient Pharmacy</u>

#### Inbound ePrescribing Web-Based Application

The IEP web-based application is used by Pharmacy Users, Administrators, Pharmacy Managers, and PBM Admin personnel. Tabs include:

- Home
- Pharmacy Management
- Track/Audit
- Reports
- User Management
- Help

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc83910092" class="anchor"></span>Figure 1‑1: Inbound ePrescribing Web-based Application

The IEP web-based application is discussed in more detail in [Unit 2 - Inbound ePrescribing Web-Based Application](\l).

#### Inbound eR<sub>X</sub> VistA Outpatient Pharmacy

The Inbound eR<sub>X</sub> VistA Outpatient Pharmacy display screens include VistA screens that are used by VA Pharmacists and Technicians to validate and process eR<sub>X</sub>es.

The eR<sub>X</sub> Holding Queue is discussed in more detail in [Unit 3 Part 1- Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#Unit_3) available on the Veteran’s Document Library (VDL).

<span id="_Fillable_Prescriptions" class="anchor"></span>

### Fillable Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A “fillable prescription” is any inbound prescription with medication information, sent by an external or non-VA provider, which includes one of the following National Council for Prescription Drug Programs (NCPDP) 2017071 XML messages:

- NewRx Message
- RxRenewal Response Message - Replace response type
- RxChange Response Message - Approved response type for request types Generic Substitution, Therapeutic Interchange/Substitution, Drug Use Evaluation, Script Clarification and Out of Stock
- RxChange Response Message - Approved with Changes (AwC) response type for request types Generic Substitution, Therapeutic Interchange/Substitution, Drug Use Evaluation, Script Clarification and Out of Stock.
- RxChange Response Message - Validated response type for request type Prescriber Authorization

> **NOTE:** According to NCPDP 2017071, RxRenewal Response Approved and Approved with Changes types are also treated as fillable prescriptions. But the workflows for these are different than the above mentioned inbound message types. Throughout the guide, the term “fillable” is used for the above mentioned inbound message types only. For Controlled Substance prescriptions the only responses possible for RxRenewal request are ‘Denied’ and ‘Replace’.

### Inbound ePrescribing Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IEP workflow is illustrated in the figure and described below.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc83910093" class="anchor"></span>Figure 1‑2: Process Inbound ePrescribing Flow

1.  eR<sub>X</sub>es are sent from an external provider to SureScripts and/or Change Healthcare (CH). CH provides commercial ePrescribing solutions and, for the purposes of the IEP implementation, serves as a gateway to all participating ePrescribing providers nationwide.
2.  CH verifies and transmits eR<sub>X</sub> transactions to/from SureScripts and/or an external provider’s EHR system and the IEP system.
3.  The eR<sub>X</sub>es are routed from CH to the IEP Processing Hub via the Data Access Service (DAS) external gateway. DAS and CH communicate using https requests over a secured network.
4.  In the IEP Processing Hub, autochecks occur on the fillable prescriptions for Patient, Provider, and Drug/SIG. Refer to section <u>1.2.4</u> [Fillable Prescriptions](#_Fillable_Prescriptions) for the definition of fillable prescriptions. The Master Person Index (MPI) is used for patient checking, depending on the data set that is sent by the Prescriber for that patient. For patient Enrollment and Eligibility (E&E) checks, the Enrollment System (ES) is used. The ES assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with E&E data. The E&E check is optional and can be turned on or off for each site. Patient Registration is also confirmed against the instance of the receiving pharmacy.
5.  The Drug Name is matched against the local Drug File first, the VA Product Name next and then the National Drug Code (NDC), depending on which it matches first on. As a note, autochecks can be incorrect therefore the data must also be validated against the medication data sent for fillable prescriptions. Refer to section <u>Unit 3: Section 3.6.3 Validate Drug/SIG</u> in [Unit 3 Part 2](#Unit_3) (PSO_7_0_P617_UM_32) available on the Veteran’s Documentation Library (VDL) for more information.
6.  The IEP web-based application allows users to view and generate reports on the autocheck results in the Processing Hub, as well as manage VA pharmacy information, and search for and print an eR<sub>X</sub>.
7.  Once the eR<sub>X</sub> has completed all autochecks in the IEP Processing Hub, the fillable prescription, as well as the outcomes of all the autochecks (patient, provider, and drug), are transmitted to VistA OP. VistA Link is used for the provider and drug checks against the VistA OP system.
8.  The VistA OP’s IEP Holding Queue allows for the initial validation and acceptance of an eR<sub>X</sub> before being transmitted to Pending Outpatient Orders file for additional order checks and then final dispensing.
9.  A RxRenewal Request transaction is originated by the pharmacy. This transaction is for requesting approval for additional renewals of a prescription once the original number of renewals has been dispensed. A RxRenewal Response is sent by the prescriber to the pharmacy in response to a request to renew a prescription. The response indicates whether the RxRenewal Request has been accepted, denied, or replaced.
10. A CancelRx Request message is used to notify the pharmacy that a previously sent fillable prescription should be canceled and not filled. The message is originated by the prescriber system as a CancelRx Request message. The CancelRx Response message is sent from the pharmacy to the prescriber system in response to a CancelRx Request message.
11. A RxChange Request transaction is originated by the pharmacy. This transaction is for requesting changes to a prescription, Prior Authorization or Prescriber Authorization. A RxChange Response is sent by the prescriber to the pharmacy in response to the change requested. The response indicates whether the RxChange Request has been accepted, denied, or validated.
12. Patient Centric View is a dashboard view, in addition to the Traditional View of the eR<sub>X</sub> Holding Queue, to provide the user the ability to view the eR<sub>X</sub> records that are in actionable statuses and that are grouped by Patients. The user can further select and view only the patients who have new prescriptions in one of the actionable statuses. The user can also jump to the Outpatient side and navigate back to the Holding Queue when there is a Pending Order for the selected patient. Each site can configure the number of lookback days to view the patient/prescription records that are still actionable statuses in the Holding Queue.

## Inbound ePrescribing Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IEP architecture, illustrated in the below figure, depicts the different programs/applications that IEP interfaces with.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc83910094" class="anchor"></span>Figure 1‑3: Inbound ePrescribing Architecture

## Roles and Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IEP roles and tasks are described in this section as primary and secondary users. Primary users are VA Pharmacy Users. Secondary users include: System Administrators, VA Pharmacy Managers, VA PBM personnel, Non-VA Providers, and External Pharmacy personnel. The following sections provide an overview of primary and secondary user roles and their capabilities within IEP.

VA users have the capability of performing eR<sub>X</sub>-related tasks in the IEP web-based application and in the VistA OP eR<sub>X</sub> Holding Queue module. Specific tasks for each component are described in more detail in [Unit 2 - Inbound ePrescribing Web-Based Application](#inbound-eprescribing-web-based-application-overview) and  
[Unit 3 Part 1 - Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#Unit_3) (PSO_7_0_P617_UM_31) available on the Veteran’s Documentation Library (VDL).

The primary users of IEP are VA Pharmacy Users. Secondary user roles of this functionality include:

- Administrator – VA Local and National System Administrators.
- Pharmacy Manager – VA Pharmacy Management to include VA management, hospital director, under sec, etc., or anyone outside pharmacy that will need to know how many and what is the cost of the project.
- PBM Admin – All VA PBM personnel, including management.
- Non-VA Providers – Submit inbound requests to VA and review statuses sent from VA.

Details of the roles and capabilities for each user in the IEP web-based application and the VistA eR<sub>X</sub> Holding Queue based on their security keys are outlined in the tables below. Users with the ability to add/update a pharmacy may only add/update pharmacies for the site(s) in which the user is assigned to. Any user that is not assigned to MbM sites cannot view the Track/Audit records of MbM sites.

<span id="_Toc498002236" class="anchor"></span>Table 1: Inbound ePrescribing Web-Based Application User Roles & Capabilities

<table>
<caption>This table provides an overview of the user roles and their capabilities within the Inbound ePrescribing web-based application. </caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>User Role</th>
<th>Functionality</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Administrator</td>
<td><ul>
<li><p>Full Control, access to all tabs</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Pharmacy Management</td>
<td><ul>
<li><p>Home</p></li>
<li><p>Pharmacy Management</p></li>
<li><p>Track/Audit</p></li>
<li><p>Reports</p></li>
<li><p>Help</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>PBM Administrator</td>
<td><ul>
<li><p>Home</p></li>
<li><p>Pharmacy Management</p></li>
<li><p>Track/Audit</p></li>
<li><p>Reports</p></li>
<li><p>Help</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Pharmacy Users</td>
<td><ul>
<li><p>Home</p></li>
<li><p>Track/Audit</p></li>
<li><p>Reports</p></li>
<li><p>Help</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Default VA User (Read Only)</td>
<td><ul>
<li><p>Home</p></li>
<li><p>Reports</p></li>
<li><p>Help</p></li>
</ul></td>
</tr>
</tbody>
</table>

This table provides an overview of the user roles and their capabilities within the Inbound ePrescribing web-based application.

<span id="_Toc498002237" class="anchor"></span>

Table 2: NewRx, Refill/RxRenewal Request and Response, CancelRx Request and Response  
(v2.0 and v3.0)

| VistA Security Key            | PSD RPH | PSO ERX ADV TECH | PSO ERX TECH | PSO ERX VIEW |
|-------------------------------|---------|------------------|--------------|--------------|
| Validate Patient              | X       | X                | X            |              |
| Validate Provider             | X       | X                | X            |              |
| Validate Drug/SIG             | X       | X                | X            |              |
| Accept Validation             | X       | X                | X            |              |
| Accept eRX                    | X       | X                |              |              |
| Reject                        | X       | X                | X            |              |
| Remove                        | X       | X                | X            |              |
| Hold                          | X       | X                | X            |              |
| Un Hold                       | X       | X                | X            |              |
| Search/Sort                   | X       | X                | X            | X            |
| Print                         | X       | X                | X            | X            |
| Message View                  | X       | X                | X            | X            |
| Ack – RxRenewal Response      | X       | X                | X            |              |
| RxChange Request              | X       | X                | X            |              |
| RxRenewal Request (OP)        | X       | X                | X            |              |
| Ack – CancelRx                | X       | X                |              |              |
| Ack – Inbound RxRenewal Error | X       | X                | X            |              |

This table displays the VistA OP Inbound eRx Holding Queue User Roles & Capabilities listing the Security Key, PSDRPH, PSO ERX ADV TECH, and PSO ERX VIEW description details.

<span id="_Toc83902207" class="anchor"></span>Table 3: RxRenewal Response – Replace Type (v4.0)

| VistA Security Key    | PSD RPH | PSO ERX ADV TECH | PSO ERX TECH | PSO ERX VIEW |
|-----------------------|---------|------------------|--------------|--------------|
| Validate Patient      | X       | X                | X            |              |
| Validate Provider     | X       | X                | X            |              |
| Validate Drug/SIG     | X       | X                | X            |              |
| Accept Validation     | X       | X                |              |              |
| Accept eR<sub>X</sub> | X       | X                |              |              |
| Reject                | X       | X                | X            |              |
| Remove                | X       | X                | X            |              |
| Hold                  | X       | X                | X            |              |
| Un Hold               | X       | X                | X            |              |
| Search/Sort           | X       | X                | X            | X            |
| Print                 | X       | X                | X            | X            |
| Message View          | X       | X                | X            | X            |

This table displays the VistA OP Inbound eRx Holding Queue User Roles & Capabilities listing the Security Key, PSDRPH, PSO ERX ADV TECH, and PSO ERX VIEW description details.

<span id="_Toc83902208" class="anchor"></span>Table 4: RxChange Response – Replace Type (v4.0)

| VistA Security Key      | PSD RPH | PSO ERX ADV TECH | PSO ERX TECH | PSO ERX VIEW |
|-------------------------|---------|------------------|--------------|--------------|
| Validate Patient        | X       | X                | X            |              |
| Validate Provider       | X       | X                | X            |              |
| Validate Drug/SIG       | X       | X                | X            |              |
| Accept Validation       | X       | X                |              |              |
| Accept eR<sub>X</sub>   | X       | X                |              |              |
| Reject                  | X       | X                | X            |              |
| Remove                  | X       | X                | X            |              |
| Hold                    | X       | X                | X            |              |
| Un Hold                 | X       | X                | X            |              |
| Search/Sort             | X       | X                | X            | X            |
| Print                   | X       | X                | X            | X            |
| Message View            | X       | X                | X            | X            |
| Ack – RxChange Response | X       | X                | X            |              |

This table displays the VistA OP Inbound eRx Holding Queue User Roles & Capabilities listing the Security Key, PSDRPH, PSO ERX ADV TECH, and PSO ERX VIEW description details.

> **NOTE:** When a user is assigned more than one VistA security key, the key with least access overrides the other keys assigned. For example, when a user is granted both PSDRPH and PSO ERX VIEW keys, access will drop to the level of the least access offered by PSO ERX VIEW key and the broader access of PSDRPH will be ignored.

## Help Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues with the IEP web-based application that cannot be resolved by this guide or the site administrator, please contact the Enterprise Service Desk (ESD) at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

## FAX Failover

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When CH attempts to send an eR<sub>X</sub> to a pharmacy, but the VA Inbound eR<sub>X</sub> Processing Hub does not return an NCPDP STATUS message back before the request times out or if a synchronous NCPDP ERROR message is returned by the Hub, a “FAX failover” occurs. CH delivers the eR<sub>X</sub> message via FAX using the FAX number on record of the destination pharmacy. VA Pharmacies need to process eR<sub>X</sub> records received via FAX as non-electronic R<sub>X</sub>es. There is no record of these FAX messages in either the Inbound eR<sub>X</sub> Processing Hub or the VistA OP Holding Queue.

# Inbound ePrescribing Web-Based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Inbound ePrescribing Web-Based Application Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the Inbound ePrescribing web-based application.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inbound ePrescribing (IEP) web-based application provides eR<sub>X</sub> management, administration, and monitoring capabilities.

### Access Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user should contact their supervisor, or the administrator assigned at their local site for managing the application for questions on access to the IEP web-based application and/or modifications to user roles/permissions.

### Accessing the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Personal Identification Verification (PIV) card is required to access the application, using the following steps:

1.  Using Internet Explorer, go to URL [<u>https://vaausappiep201.aac.va.gov/inbound/</u>](https://gcc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fvaausappiep201.aac.va.gov%2Finbound%2F&data=04%7C01%7C%7C35074d49539d487aa04508d88cc0ab0d%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C637414106410727228%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=ijlR8GI4zY514StDd4DP6bRc2xVDw1qfOIaFFox6E7k%3D&reserved=0) to access the web-based application.
2.  On the VA Single Sign-on screen, select the Sign In with VA PIV Card icon.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc83910095" class="anchor"></span>Figure 2‑1: VA Single Sign-on

3.  In the “Select a Certificate” dialog, select the desired certificate and then select OK.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc83910096" class="anchor"></span>Figure 2‑2: Select a Certificate

4.  In the “ActivClient Login” dialog, enter the Personal Identification Number (PIN) in the “PIN” text box and select OK.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc83910097" class="anchor"></span>Figure 2‑3: Active Client Login

13. A warning message displays. Select Accept.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc83910098" class="anchor"></span>Figure 2‑4: Warning Message

When authentication and authorization is successful, the application home screen displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc83910099" class="anchor"></span>Figure 2‑5: Home Screen

### Screen Navigation and Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure outlines the key areas of the screen layout. Brief descriptions of the screen layout are provided below:

1.  On the top-right of the screen is a Go to Main Content link for Section 508 purposes to allow a user to be directed to the main content on the screen.
2.  The logged-in user’s VA User ID and a Logout link displays on the right side of the banner.
3.  Below the banner, the main tabs display for accessing the screens within the application.
4.  The name of the screen displays below the main tabs.
5.  The bottom of the screen also contains hyperlinks to the main tab screens.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc83910100" class="anchor"></span>Figure 2‑6: Web-Based Application Screen Layout

Only the menu bar tabs that the user has access to display. The administrator grants or restricts tab display or screen access based on the user role assigned. For additional information, refer to section <u>1.4 Roles and Capabilities</u>.

The tabs and their associated user access include:

- <u>Inbound</u> eRX Homepage – Inbound eR<sub>X</sub> Homepage. All Users
- <u>Pharmacy Management</u> – Administrators, Pharmacy Managers, and PBM Admin
- <u>Track/Audit</u> – Administrators, Pharmacy Managers, PBM Admin, and VA Pharmacy Users
- <u>Reports</u> – All Users
- <u>User Management</u> – Administrators
- <u>Help</u> – All Users

#### Inbound eR<sub>X</sub> Homepage

The Inbound eR<sub>X</sub> Homepage is displayed when successful login authentication and verification is completed. The Inbound eR<sub>X</sub> Homepage is always accessible by selecting the Home tab in the menu bar. The Home screen is accessible to all user roles. However, only the tabs authorized for the user’s role display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc83910101" class="anchor"></span>Figure 2‑7: Home Screen

#### Pharmacy Management

To access the Pharmacy Management screen, select the Pharmacy Management tab in the menu bar. The Pharmacy Management screen displays the Pharmacy Management table that provides information about pharmacies and allows Administrators and Pharmacy Managers to search for, add, and edit pharmacies. Users can also enable/disable the receiving of prescriptions targeted for a particular pharmacy.

> **NOTE:** The search filters default to “All” in the VISN field. The user must select the Search button for information to populate.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc83910102" class="anchor"></span>Figure 2‑8: Pharmacy Management Screen

#### Track/Audit

To access the Track/Audit eR<sub>X</sub> screen, select the Track/Audit tab in the menu bar. The Track/Audit eR<sub>X</sub> screen allows users view eR<sub>X</sub>es and their related messages.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc83910103" class="anchor"></span>Figure 2‑9: Track/Audit Screen

#### Reports

To access the Reports screen, select the Reports tab in the menu bar. The Reports screen allows all users to run and view a Summary Report.

The system uses the comma-separated values (.CSV) format. Users can view reports using a third-party tool, such as Microsoft Excel.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc83910104" class="anchor"></span>Figure 2‑10: Reports Screen

#### User Management

To access the User Management screen, select the User Management tab in the menu bar. The User Management screen allows Administrators to add users, enable/disable users, and modify user roles. This screen only displays for users with Administrator access.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc83910105" class="anchor"></span>Figure 2‑11: User Management Screen

#### Help 

To access the Help page, select the Help tab in the menu bar. The Help page provides help topics and production support information.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc498613630" class="anchor"></span>Figure 2‑12: Help Tab

When the Help tab is selected, the Help Page displays in a new window.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc83910107" class="anchor"></span>Figure 2‑13: Help Page

## Inbound ePrescribing Web-based Application Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide descriptions of the IEP web-based application’s capabilities within each tab.

### Pharmacy Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Management screen displays the Pharmacy Management table. The default view displays all VA pharmacies. Actions available to users include:

- <u>Searching for a Pharmacy</u>
- <u>Adding a Pharmacy</u>
- <u>Updating a Pharmacy</u>

#### Searching for a Pharmacy

Users can search for a pharmacy from the Pharmacy Management screen. The default view lists all VA pharmacies.

To search for a pharmacy:

1.  Enter the NCPDP ID (if known).
2.  Enter the Pharmacy Name.
3.  Select the desired VISN number from the “VISN” drop down.
4.  Select the desired Station ID from the “Station ID” drop down. If viewing All VISNs, the user is unable to select a Station ID. To select a specific Station ID, the VISN must be selected.
5.  Select Search.

The Pharmacy Management table displays results for the selected search criteria.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc83910108" class="anchor"></span>Figure 2‑14: Search for a Pharmacy

#### Adding a Pharmacy

To add a new pharmacy, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

> **NOTE:** The pharmacy must be pre-registered as a pharmacy in ePharmacy. ePharmacy is supported by CH therefore ePharmacy registration adds the pharmacy to the same CH Pharmacy Directory (\*NCPDP ID required) used by Inbound eR<sub>X</sub>. For IEP, CH must also enable eR<sub>X</sub> support for the pharmacy through the IEP web-based application.

#### Updating a Pharmacy

To update information for a VA pharmacy, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

#### Disable eR<sub>X</sub>

To completely halt a specific Pharmacy from receiving ePrescriptions, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

> **NOTE:** If a pharmacy is to be disabled for a long duration, a request must be made to CH. Note that the ESD routes the ticket to an IEP administrator to assist with this step. CH can switch the pharmacy to fax only or turn off eR<sub>X</sub> delivery (electronic or fax) completely.

#### Temporarily Disable eR<sub>X</sub>

In cases where a site needs to halt receiving ePrescriptions temporarily, use the Disable eR<sub>X</sub>/Enable eR<sub>X</sub> fields.

Disabling a pharmacy allows users to temporarily disable the pharmacy from receiving eR<sub>X</sub>es in the event of a natural or facility disaster, maintenance, or move. This disables the pharmacy from receiving new inbound messages, but outbound messages still go back to the external provider via CH. The pharmacy is disabled on the Processing Hub, but no changes are made in CH.

> **NOTE:** The enable/disable field in the Processing Hub is for a temporary disable, which also allows outgoing messages to continue flowing from VistA. Additionally, incoming messages still flow from CH to the Processing Hub for the pharmacy, however an error message is returned to the provider saying that Inbound eR<sub>X</sub> messaging is currently not available. In these cases, CH then sends a fax of the eR<sub>X</sub> to the pharmacy.

To temporarily disable a pharmacy:

1.  Search for the desired pharmacy.
2.  From the Pharmacy Management table, select the hyperlink for the desired pharmacy to edit in the “NCPDP ID” column.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/019.png)

<span id="_Toc83910109" class="anchor"></span>Figure 2‑15: NCPDP ID Column Hyperlinks

The Edit Pharmacy screen displays. At the top of the screen is a Warning Message with text notifying the user that any change made here will not update the pharmacy in CH’s published pharmacy directory. Selecting Return to Pharmacy Management returns the user to the Pharmacy Management screen.

3.  Select No from the “Inbound eR<sub>X</sub> Enabled” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc83910110" class="anchor"></span>Figure 2‑16: eR<sub>X</sub> Enabled Drop Down

4.  At the bottom of the Edit Pharmacy screen, select Update to save all changes. The date that the fields were modified displays in the “Updated Date” field.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc83910111" class="anchor"></span>Figure 2‑17: Update Pharmacy Information

#### Enable eR<sub>X</sub>

The pharmacy can be enabled once it is ready to receive eR<sub>X</sub>es again.

To enable a pharmacy:

1.  Select Yes from the “Inbound eR<sub>X</sub> Enabled” drop down on the Edit Pharmacy screen.
2.  Select Update (not shown).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc83910112" class="anchor"></span>Figure 2‑18: Enable/Disable Pharmacy

> **NOTE:** If a pharmacy is not enabled and a prescription comes in for that pharmacy, an error message is sent back to the provider’s EHR system to notify the provider that the pharmacy is not currently receiving eR<sub>X</sub>es.

#### Enrollment and Eligibility Check

The Enrollment and Eligibility (E&E) check may be enabled or disabled for individual pharmacies. This option is provided so each pharmacy may decide whether to turn the E&E check on or off depending on whether the patients whose eR<sub>X</sub>es are filled at the pharmacy are enrolled in the E&E system. For example, MbM does not currently have any patient enrolled with the E&E system.

To ensure the Enrollment and Eligibility Check is enabled for a pharmacy:

1.  Select the desired pharmacy from the Pharmacy Management table.
2.  Ensure Yes displays in the “Enrollment and Eligibility Check Enabled” field.
3.  If required, select Yes in the “Enrollment and Eligibility Check Enabled” drop-down and then select Update.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc83910113" class="anchor"></span>Figure 2‑19: Enrollment and Eligibility Check Enabled

If the Enrollment and Eligibility Check is not enabled for a pharmacy, the Patient Auto Check Status displays as “MVI_MATCH_NOT_FOUND” on the Track/Audit screen.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc83910114" class="anchor"></span>Figure 2‑20: Track/Audit – Enrollment and Eligibility Check Not Performed

### Track/Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Track/Audit screen allows users to search for eR<sub>X</sub> messages and track prescriptions and provides the ability to view and print the details of a prescription.

When the user initially enters the Track/Audit screen, the default date range is two days (the current date and the previous date) and the default records limit is set to 100.

Users can now see whether individual messages are Controlled Substance (CS) or Non-Controlled Substance (NON-CS) prescriptions and whether they have been digitally signed under the “PRESCRIBER DS” column. The value given in this row can be in 5 different states based off of how the signature was processed. Please see below table for details of all the different states:

| Written Date (WD)  older or equals Effective Date (ED) | Digital Signature (DS) | DS Indicator | Prescriber DS Column | Captured under Message Status ‘NCPDP_MSG \_INVALID’ | eRx message reaches VistA? |
|--------------------------------------------------------|------------------------|--------------|----------------------|-----------------------------------------------------|----------------------------|
| Yes (WD ≤ ED)                                          | Valid                  | Missing      | ‘VERIFIED’           | No                                                  | Yes                        |
| Yes                                                    | Invalid                | Missing      | ‘FAILED’             | Yes                                                 | No                         |
| Yes                                                    | Missing                | Missing      | ‘NULL’               | No                                                  | Yes                        |
| Yes                                                    | Missing                | ‘TRUE’       | ‘TRUE’               | No                                                  | Yes                        |
| Yes                                                    | Missing                | ‘FALSE’      | ‘FALSE’              | No                                                  | Yes                        |
| No  (WD \> ED)                                         | Missing                | Missing      | ‘NULL’               | Yes                                                 | No                         |
| No                                                     | Missing                | ‘TRUE’       | ‘TRUE’               | Yes                                                 | No                         |
| No                                                     | Missing                | ‘FALSE’      | ‘FALSE’              | Yes                                                 | No                         |

> **NOTE:** If a user is not assigned to one of the MbM station IDs, that user cannot see any records related to MbM station IDs.

#### Searching for a Message

To search for a message:

1.  Select the desired search criteria from the drop downs and enter desired search keywords in the text fields.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc83910115" class="anchor"></span>Figure 2‑21: Track/Audit Search Criteria

If filtering by eRx Type for Controlled Substance (CS) records, an additional filter will populate to filter the results by drug class (Schedule II-V, Schedule II, Schedule III-V).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc83910116" class="anchor"></span>Figure 2‑22: Track/Audit CS Search Criteria

The search criteria are described in the table below.

<span id="_Ref5966673" class="anchor"></span>Table 5: Track/Audit Search Criteria Descriptions

| Search Field          | Field Type                 | Description                                                                                                                       | Drop Down Options                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VISN                  | Drop Down                  | VISN number that a VA pharmacy is associated with                                                                                 | All VISNs, each VISN number                                                                                                                                                                                                                                                                                                                                                        |
| VA Station ID         | Text                       | Station ID of the VA pharmacy                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| From Date             | Text or Calendar Drop Down | Beginning date. Choose From date for a date range search; select the date from the calendar or enter a date in MM/DD/YYYY format. | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                                                            |
| To Date               | Text or Calendar Drop Down | End date. Choose To date for a date range search; select the date from the calendar or enter a date in MM/DD/YYYY format.         | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                                                            |
| Message Type          | Drop Down                  | Type of the NCPDP message type                                                                                                    | All, CancelRx, CancelRxResponse, Error, NewRx, RxRenewalResponse, RxRenewalRequest, RxChangeResponse, RxChangeRequest, Status, Verify                                                                                                                                                                                                                                              |
| Message ID            | Text                       | Prescription message ID (generated by CH for incoming eR<sub>X</sub>es)                                                           | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Relates to Message ID | Text                       | To search for messages related to a Message ID                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Patient SSN           | Text                       | Patient Social Security Number                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Patient Last Name     | Text                       | Patient last name                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Patient First Name    | Text                       | Patient first name                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Patient DOB           | Text or Calendar Drop Down | Patient date of birth                                                                                                             | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                                                            |
| Prescriber NPI        | Text                       | Prescriber National Provider Identifier (NPI)                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Prescribed Drug       | Text                       | Drug prescribed from the eR<sub>X</sub>                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Prescriber LastName   | Text                       | Last name of prescriber                                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Prescriber FirstName  | Text                       | First name of prescriber                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Prescriber DEA \#     | Text                       | Drug Enforcement Administration (DEA) number of prescriber                                                                        | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| eRx Reference \#      | Test                       | Unique, internal VA reference \# assigned to all messages                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                |
| Sent or Received      | Drop Down                  | Select Sent (Outbound) or Received (Inbound) messages                                                                             | Both, Received, Sent                                                                                                                                                                                                                                                                                                                                                               |
| Message Status        | Drop Down                  | Processing Hub message status                                                                                                     | Auto check Processing Completed, VistA OP Delivery Successful, VistA OP Delivery In Process, VistA OP Delivery Retries Exceeded, Auto check in Progress, Pharmacy Inbound eR<sub>X</sub> Not Enabled, Pharmacy Unknown, Outbound Message Send Completed, Outbound Message Delivery Retries Exceeded, Outbound Message Send In Progress, Ready for Autocheck, NCPDP Message Invalid |
| Max Records           | Drop Down                  | Select number of maximum records to display in search query                                                                       | 100, 7500, 10000, 50000, 100000                                                                                                                                                                                                                                                                                                                                                    |
| eRx Type              | Drop Down                  | Select type of eRx (Controlled Substance or Non-Controlled Substance) to filter search query by                                   | All, CS, Non-CS                                                                                                                                                                                                                                                                                                                                                                    |
|                       |                            |                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |
|                       |                            |                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |

Track/Audit eRx Search Criteria

2.  Use the “Max Records” drop down to set the limit of search results. This value can be set to 100, 7500, 10000, 50000, or 100,000. The default value is 100. Limiting search results decreases the time required to conduct a search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc83910117" class="anchor"></span>Figure 2‑23: Max Records Drop Down

3.  Select Search to execute the search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc83910118" class="anchor"></span>Figure 2‑24: Track/Audit eR<sub>X</sub> Search

A “Search in progress” message displays during search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc83910119" class="anchor"></span>Figure 2‑25: Search in Progress Message

The search results display in a table below the search criteria. The total number of records in the search results display at the bottom of the table.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc83910120" class="anchor"></span>Figure 2‑26: Search Results

The Search Results fields and descriptions are listed in the table below.

<span id="_Toc498002240" class="anchor"></span>Table 6: Search Results Fields & Descriptions

| Field                       | Description                                                                        |
|-----------------------------|------------------------------------------------------------------------------------|
| Received Date               | Date that the eR<sub>X</sub> was received by VA                                    |
| eR<sub>X</sub> Reference \# | Unique, internal VA reference \# assigned to all messages as a hyperlink           |
| eRx Type                    | Controlled Substance (CS) or Non-Controlled Substance (Non-CS)                     |
| Message Type                | Type of message                                                                    |
| Patient Name                | First and last name of the patient                                                 |
| Patient DOB                 | Date of birth for the patient                                                      |
| Patient SSN                 | Social security number of the patient                                              |
| Drug Prescribed             | Drug prescribed to the patient                                                     |
| Schedule                    | Schedule of Controlled Substance                                                   |
| Message ID                  | Identification of the message                                                      |
| Prescriber DS               | Verification of Prescriber’s Digital Signature (DS)                                |
| Prescriber Name             | First and last name of the prescriber                                              |
| Prescriber NPI              | National Provider Identifier for the prescriber                                    |
| Prescriber DEA              | Identifier assigned to prescriber by United States Drug Enforcement Administration |
| VISN                        | VISN that the VA pharmacy is associated with                                       |
| Station ID                  | Station ID of the VA pharmacy                                                      |
| Pharmacy Name               | Internal VA pharmacy name                                                          |
| Address                     | Address of VA pharmacy                                                             |
| Relates to Message ID       | Lists message related to a particular Message ID as a hyperlink                    |
|                             |                                                                                    |
| Patient AutoCheck Status    | Results of system patient auto-validation check                                    |
| Provider AutoCheck Status   | Results of system provider auto-validation check                                   |
| Drug AutoCheck Status       | Results of system drug auto-validation check                                       |
| Message Status              | Current status of the message                                                      |

Table of the Search Results Fields and Descriptions

#### Export Search Results

From the Track/Audit tab, users have the capability of exporting the search results. Exports are in .CSV format and can be viewed in Microsoft Excel. The number of records exported is dependent on the number of records selected in the “Max Records” dropdown.

To export the search results:

1.  Select Export.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc83910121" class="anchor"></span>Figure 2‑27: Export Search Results

A prompt displays asking to Open or Save the results.

2.  Select Open to view the results.
3.  Select the down arrow to the right of Save to save the results to a desired location.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc83910122" class="anchor"></span>Figure 2‑28: Track/Audit Export Prompt (after clicking Export buttons)

4.  When the arrow is selected, the system displays a “Save As” dialog (not shown). Navigate to a location on your system to save the file.
14. 

#### Inbound/Outbound Message Detail

Inbound/outbound message detail information is reviewed and managed under the Track/Audit tab.

To access the detail screen of a message, select the hyperlink in the “eRx Reference \#” column to display the desired message detail.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc83910123" class="anchor"></span>Figure 2‑29: Track/Audit Grid View

The message details display. Each message detail screen includes the following buttons:

- Return to Search: Return to the search results screen.
- Show Related Messages: Displays all sent and received eR<sub>X</sub> messages that are related to the displayed message.7
- Print: Print the eR<sub>X</sub> message details.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc83910124" class="anchor"></span>Figure 2‑30: Message Details

If the Show Related Messages button is selected, any sent and received messages that are related to the current message display based on the Message ID linkage. For example, Related Messages for a RxRenewal Response should, at minimum, display the related RxRenewal Request and the NewRx for which the refill was requested. Related messages also include related Status, Verify, and/or Error Messages, if applicable. Related messages display in descending order of received date. The most recent message is at the top of the list, and the NewRx message is at the bottom. Select the number in the “eR<sub>X</sub> Reference \#” column to view message details.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc83910125" class="anchor"></span>Figure 2‑31: Related Messages

#### NewRx Message

The NewRx detail screen displays the new eR<sub>X</sub> from an external provider.

To access the NewRx detail screen, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc83910126" class="anchor"></span>Figure 2‑32: NewRx Message Search and Results Screen

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/037.png)

<span id="_Toc83910127" class="anchor"></span>Figure 2‑33: NewRx Message Details Screen

#### RxRenewal Request

RxRenewal Request message details can be viewed under the Track/Audit tab.

To access the RxRenewal Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc83910128" class="anchor"></span>Figure 2‑34: RxRenewal Request Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/039.png)

<span id="_Toc83910129" class="anchor"></span>Figure 2‑35: RxRenewal Request Details Screen

#### RxRenewal Response

RxRenewal Response message details can be viewed under the Track/Audit tab.

To access the RxRenewal Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/040.png)

<span id="_Toc83910130" class="anchor"></span>Figure 2‑36: RxRenewal Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/041.png)

<span id="_Toc83910131" class="anchor"></span>Figure 2‑37: RxRenewal Response Detail Screen

#### RxChange Request

RxChange Request message details can be viewed under the Track/Audit tab.

To access the RxChange Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/042.png)

<span id="_Toc83910132" class="anchor"></span>Figure 2‑38: RxChange Request Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc83910133" class="anchor"></span>Figure 2‑39: RxChange Request Detail Screen

#### RxChange Response

RxChange Response message details can be viewed under the Track/Audit tab.

To access the RxChange Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc83910134" class="anchor"></span>Figure 2‑40: RxChange Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/045.png)

<span id="_Toc83910135" class="anchor"></span>Figure 2‑41: RxChange Response Detail Screen

#### CancelRx Request

The CancelRx Request message details can be viewed under the Track/Audit tab.

To access the CancelRx Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/046.png)

<span id="_Toc83910136" class="anchor"></span>Figure 2‑42: CancelRx Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/047.png)

<span id="_Toc83910137" class="anchor"></span>Figure 2‑43: CancelRx Detail Screen

#### CancelRx Response

The CancelRx Response message details can be displayed under the Track/Audit tab.

To access the CancelRx Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/048.png)

<span id="_Toc83910138" class="anchor"></span>Figure 2‑44: CancelRx Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/049.png)

<span id="_Toc83910139" class="anchor"></span>Figure 2‑45: CancelRx Response Detail Screen

#### Error Messages

At multiple points in the process, an Error transaction can be generated. Outbound error messages are sent when an eR<sub>X</sub> record that is NCPDP corrupted is received, when the receiving Pharmacy is not one of the VA pharmacies configured in the Inbound eR<sub>X</sub> system, or when an eR<sub>X</sub> record with a Written or Effective Date older than or equal to 365 days is received.

Inbound Errors for VistA may be received under multiple situations such as if the Prescriber’s EHR system is unable to receive and process a certain transaction sent from the Pharmacy, or a connection between the Transaction Hub and CH is not working or an inbound message with a digital signature fails authentication.

To access the Error message details, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/050.png)

<span id="_Toc83910140" class="anchor"></span>Figure 2‑46: Error Message Search and Search Results

The selected message details sent and received by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/051.png)

<span id="_Toc83910141" class="anchor"></span>Figure 2‑47: Error Message Detail Screen

#### Verify Messages

The Verify message confirms delivery of a message to its final destination. The Verify message is an NCPDP transaction that indicates the acceptance of the request by the receiving system. This message is used to communicate the data content status of a transaction. Verify Messages sent from the Transaction Hub are Outbound Verify Messages. Verify Messages received from CH and/or an External Provider’s EHR system are Inbound Verify Messages.

To access the Verify message detail screen, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/052.png)

<span id="_Toc83910142" class="anchor"></span>Figure 2‑48: Verify Message Search and Search Results

The selected message details sent by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/053.png)

<span id="_Toc83910143" class="anchor"></span>Figure 2‑49: Verify Message Detail Screen

#### Status Messages

The Status message is used to relay acceptance of a transaction back to the sender. The Status message is an NCPDP transaction that indicates the acceptance of the request. For the Inbound eR<sub>X</sub> web-based application, Inbound Status messages are received from CH and Outbound Status messages are sent from the Transaction Hub. Outbound Status messages are not stored in the Transaction Hub and cannot be viewed.

To access the Status message detail screen, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/054.png)

<span id="_Toc83910144" class="anchor"></span>Figure 2‑50: Status Message Search and Search Results

The selected message details received by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/055.png)

<span id="_Toc83910145" class="anchor"></span>Figure 2‑51: Status Message Detail Screen

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports tab is used to generate high-level reports. From the Reports tab, users can generate, view, and export the following reports:

- <u>Summary Report NewRx Only</u>
- <u>Auto Check Details Report</u>
- <u>Reject Reasons Report</u>
- <u>eRX Summary Report</u>

When the user initially views any of the Reports pages, the default date range is two days (the current date and the previous date). Each report displays counts under the respective columns for the selected date range based on the status of the records in the system during the selected date range. When the user selects any report, the “Search in progress, please wait…” message displays while the report is loading.

Reports can be viewed in the web application or they can be exported. For additional information on exporting reports, refer to section <u>2.2.4 Export Reports</u>.

#### Summary Report NewRx Only

The Summary Report NewRx Only provides a summary of eR<sub>X</sub> auto-validation checks for all fillable prescriptions.

To run a NewRx Summary Report:

1.  From the Reports screen, select Summary Report NewRx Only from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/056.png)

<span id="_Toc83910146" class="anchor"></span>Figure 2‑52: Summary Report NewRx Only Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/057.png)

<span id="_Toc83910147" class="anchor"></span>Figure 2‑53: NewRx Summary Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The NewRx Only Summary Report fields are described in the table below.

<span id="_Toc83902211" class="anchor"></span>Table 7: NewRx Only Summary Report Columns

| Field                     | Description                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| VISN                      | Pharmacy VISN number                                                                                                  |
| VA Station ID             | VistA pharmacy identification number                                                                                  |
| NCPDP ID                  | National Council for Prescription Drug Programs (NCPDP) identification number                                         |
| Pharmacy Name             | VistA pharmacy name                                                                                                   |
| Address                   | Pharmacy Address                                                                                                      |
| \#New Rx                  | Number of fillable prescriptions                                                                                      |
| CS \#New Rx               | Number of fillable Controlled Substance prescriptions                                                                 |
| \#Pharmacy Disabled       | Number of Pharmacy Disabled errors                                                                                    |
| \#Rejected at Hub         | Number of eR<sub>X</sub>es rejected at the Processing Hub                                                             |
| CS \#Rejected at Hub      | Number of Controlled Substance eR<sub>X</sub>es rejected at the Processing Hub                                        |
| \#Passed Auto check       | Number of eR<sub>X</sub>es that passed auto check criteria                                                            |
| CS \#Passed Auto check    | Number of Controlled Substance eR<sub>X</sub>es that passed auto check criteria                                       |
| \#Failed Auto check       | Sum of eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks                                           |
| CS \#Failed Auto check    | Sum of Controlled Substance eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks                      |
| \#Rejected by Pharmacy    | Number of eR<sub>X</sub>es rejected by the pharmacy                                                                   |
| CS \#Rejected by Pharmacy | Number of Controlled Substance eR<sub>X</sub>es rejected by the pharmacy                                              |
| \#Rx Filled               | Number of RxFill messages received by the Processing Hub from VistA                                                   |
| CS \#Rx Filled            | Number of Controlled Substance RxFill messages received by the Processing Hub from VistA                              |
| \#Accepted by Pharmacy    | Number of eR<sub>X</sub>es that have been accepted by the Pharmacy into VistA Pending/Outpatient                      |
| CS \#Accepted by Pharmacy | Number of Controlled Substance eR<sub>X</sub>es that have been accepted by the Pharmacy into VistA Pending/Outpatient |

Summary Report Columns

#### Auto Check Details Report

The Auto Check Details Report provides details of the auto checks performed by the hub side.

To run an Auto Check Details Report:

1.  From the Reports screen, select Auto Check Details Report from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/058.png)

<span id="_Toc83910148" class="anchor"></span>Figure 2‑54: Auto Check Details Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/059.png)

<span id="_Toc83910149" class="anchor"></span>Figure 2‑55: Auto Check Details Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The Auto Check Details Report fields are described in the table below.

<span id="_Toc83902212" class="anchor"></span>Table 8: Auto Check Details Report Columns

| Field                          | Description                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------|
| VISN                           | Pharmacy VISN number                                                                                       |
| VA Station ID                  | VistA pharmacy identification number                                                                       |
| NCPDP ID                       | National Council for Prescription Drug Programs (NCPDP) identification number                              |
| Pharmacy Name                  | VistA pharmacy name                                                                                        |
| Address                        | Pharmacy Address                                                                                           |
| \#New Rx                       | Number of fillable prescriptions                                                                           |
| \#Passed Autocheck             | Number of eR<sub>X</sub>es that passed auto check criteria                                                 |
| \#Passed Autocheck CS          | Number of Controlled Substance eR<sub>X</sub>es that passed auto check criteria                            |
| \#Failed Autocheck             | Sum of eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks                                |
| \#Failed Autocheck CS          | Sum of Controlled Substance eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks           |
| \#MPI Patient Found            | Number of eR<sub>X</sub>es in which the MPI Patient Found auto check passed                                |
| \#MPI Patient Not Found        | Number of eR<sub>X</sub>es in which the MPI Patient was Not Found, therefore auto check failed             |
| \#E&E Enrolled/Eligible        | Number of eR<sub>X</sub>es in which E&E Enrolled/Eligible auto check passed                                |
| \#E&E Not Enrolled/Eligible    | Number of eR<sub>X</sub>es in which the Patient was Not E&E Enrolled/Eligible, therefore auto check failed |
| \#Patient Not Enrolled at Site | Number of eR<sub>X</sub>es in which the Patient was Not Enrolled at the Site, therefore auto check failed  |
| \#Drug Match Found             | Number of eR<sub>X</sub>es in which a Drug Match was Found, therefore auto check passed                    |
| \#Drug Match Failed            | Number of eR<sub>X</sub>es in which the Drug Match Failed, therefore auto check failed                     |
| \#Provider Match Found         | Number of eR<sub>X</sub>es in which a Provider Match was Found, therefore auto check passed                |
| \#Provider Match Failed        | Number of eR<sub>X</sub>es in which the Provider Match Failed, therefore auto check failed                 |

This table displays the Summary Report Columns field descriptions.

#### Reject Reasons Report

The Reject Reasons Report provides details of eR<sub>X</sub> Rejections.

To run a Reject Reasons Report:

1.  From the Reports screen, select Reject Reasons Report from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/060.png)

<span id="_Toc83910150" class="anchor"></span>Figure 2‑56: Reject Reasons Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/061.png)

<span id="_Toc83910151" class="anchor"></span>Figure 2‑57: Reject Reasons Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The Reject Reason Report fields are described in the table below.

<span id="_Toc83902213" class="anchor"></span>Table 9: Reject Reason Report Columns

| Field                                | Description                                                                                    |
|--------------------------------------|------------------------------------------------------------------------------------------------|
| VISN                                 | Pharmacy VISN number                                                                           |
| VA Station ID                        | VistA pharmacy identification number                                                           |
| NCPDP ID                             | National Council for Prescription Drug Programs (NCPDP) identification number                  |
| Pharmacy Name                        | VistA pharmacy name                                                                            |
| \#New Rx                             | Number of fillable prescriptions                                                               |
| \#Accepted by Pharmacy               | Number of Inbound messages – (minus) number of failures and rejections – (minus) number filled |
| \#Rejected by Pharmacy               | Number eR<sub>X</sub>es rejected by the pharmacy                                               |
| \#Patient Not Eligible               | Number of Patient Not Eligible rejections                                                      |
| \#Cannot Resolve Patient             | Number of Cannot Resolve Patient rejections                                                    |
| \#Provider Not Eligible              | Number of Provider Not Eligible rejections                                                     |
| \#Cannot Resolve Provider            | Number of Cannot Resolve Provider rejections                                                   |
| \#Not Eligible for Refills           | Number of Drug Not Eligible for Renewals rejections                                            |
| \#Non Formulary                      | Number of Non Formulary rejections                                                             |
| \#Duplicate Rx                       | Number of rejections due to duplicate R<sub>X</sub>                                            |
| \#Invalid Qty                        | Number of rejections due to an Invalid Quantity entered                                        |
| \#Duplicate Therapy Class            | Number of rejections due to Duplicate Therapy Class                                            |
| \#Contact Pharmacy (ERR01)           | Multiple errors, please contact the pharmacy                                                   |
| \#Incorrect Pharmacy                 | Number of rejections due to Incorrect Pharmacy                                                 |
| \#Contact Pharmacy (ERR03)           | Incorrect Pharmacy                                                                             |
| \#Missing/Bad CS DS                  | Missing or Invalid Controlled Substance Provider Digital Signature                             |
| \#Prescriber’s CS Credential Invalid | Prescriber’s Controlled substance credentials are invalid                                      |

This table displays the Summary Report Columns field descriptions.

#### eR<sub>X</sub> Summary Report

The eR<sub>X</sub> Summary Report provides a summary of eR<sub>X</sub> auto-validation checks.

To run an eR<sub>X</sub> Summary Report:

1.  From the Reports screen, select eRx Summary Report from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/062.png)

<span id="_Toc83910152" class="anchor"></span>Figure 2‑58: eR<sub>X</sub> Summary Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select eRx Type to filter the report by All, Controlled Substance (CS), or Non-Controlled Substance (Non-CS).
5.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
6.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/063.png)

<span id="_Toc83910153" class="anchor"></span>Figure 2‑59: eR<sub>X</sub> Summary Report

The eR<sub>X</sub> Summary Report has the ability to be filtered by Controlled Substance (CS), Non-Controlled Substance (Non-CS), or All (both CS and Non-CS).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/064.png)

<span id="_Toc83910154" class="anchor"></span>Figure 2‑60: eR<sub>X</sub> Summary Report eRx Type Details Expanded

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp. The eR<sub>X</sub> Summary Report fields are described in the table below.

<span id="_Toc498002241" class="anchor"></span>Table 10: eR<sub>X</sub> Summary Report Columns

| Field                   | Description                                                                              |
|-------------------------|------------------------------------------------------------------------------------------|
| VISN                    | Pharmacy VISN number                                                                     |
| VA Station ID           | VistA pharmacy identification number                                                     |
| NCPDP ID                | National Council for Prescription Drug Programs (NCPDP) identification number            |
| Pharmacy Name           | VistA pharmacy name                                                                      |
| Address                 | Pharmacy Address                                                                         |
| \#New Rx                | Number of New eR<sub>X</sub>es                                                           |
| CS \#New Rx             | Number of New Controlled Substance eR<sub>X</sub>es                                      |
| \#RxRenewal Request     | Number of renewal requests                                                               |
| CS \#RxRenewal Request  | Number of Controlled Substance renewal requests                                          |
| \#RxRenewal Response    | Number of renewal responses                                                              |
| CS \#RxRenewal Response | Number of Controlled Substance renewal responses                                         |
| \#RxChange Request      | Number of changes requested                                                              |
| CS \#RxChange Request   | Number of Controlled Substance changes requested                                         |
| \#RxChange Response     | Number of changed R<sub>X</sub> responses                                                |
| CS \#RxChange Response  | Number of Controlled Substance changed R<sub>X</sub> responses                           |
| \#CancelRx Request      | Number of canceled R<sub>X</sub> requests                                                |
| CS \#CancelRx Request   | Number of Controlled Substance canceled R<sub>X</sub> requests                           |
| \#CancelRx Response     | Number of canceled R<sub>X</sub> responses                                               |
| CS \#CancelRx Response  | Number of Controlled Substance canceled R<sub>X</sub> responses                          |
| \#RxFill                | Number of RxFill messages received by the Processing Hub from VistA                      |
| CS \#RxFill             | Number of Controlled Substance RxFill messages received by the Processing Hub from VistA |

Summary Report Columns

### Export Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Reports tab, users may export a report to a .CSV format.

To Export a report:

1.  Select the Export button.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/065.png)

<span id="_Toc83910155" class="anchor"></span>Figure 2‑61: Export Report buttons

A prompt displays asking to Open or Save the report.

2.  Select Open to view the report.
3.  Select the down arrow to the right of Save to save the report to a desired location.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/066.png)

<span id="_Toc83910156" class="anchor"></span>Figure 2‑62: Summary Report Export Prompt (after clicking Export button)

4.  When the arrow is selected, the system displays a “Save As” dialog (not shown). Navigate to a location on your system to save the file.

### User Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Management screen allows Administrators to add new users to one or more sites (Station ID), enable users, disable users, modify user roles and existing user records by assigning them to one or more sites. This screen only displays for users with Administrator access.

The User Management screen displays the list of all users that are added to this system along with their roles and privileges and is sorted by First Name.

#### Add New User

System Administrators can add new users from the User Management screen.

To add a new user:

1.  Enter the new user’s User ID, First Name, and Last Name.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/067.png)

<span id="_Toc83910157" class="anchor"></span>Figure 2‑63: Add User - User ID, First Name, Last Name

2.  Select the new user’s role(s). Multiple roles may be selected by holding \<Ctrl\> while selecting more than one role.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/068.png)

<span id="_Toc83910158" class="anchor"></span>Figure 2‑64: Add User - Select User Roles

3.  Select the Station ID(s) for the user to have access to. Use the drop down menu to display the Station ID selection. Multiple Station IDs may be selected by holding \<Ctrl\> while selecting more than one Station ID.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/069.png)

<span id="_Toc83910159" class="anchor"></span>Figure 2‑65: Add User – Select Station ID

15. Select Add to add the selected Station ID(s) to the “Selected Station IDs” field. To remove Station IDs from the “Selected Station IDs” field, select Remove (not shown).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/070.png)

<span id="_Toc83910160" class="anchor"></span>Figure 2‑66: Add User – Add and Remove Station ID

When a user is assigned to a Station ID, they are only able to see other users and information within that Station ID. For example, in the User Management table they only see users also assigned to that Station ID and under Pharmacy Management, they only see information for pharmacies within that Station ID.

If All is selected from the “Station ID” field and added to the “Selected Station IDs” field, the user has access to all Station IDs. Additional Station ID values cannot be added if All has been selected and added to the “Selected Station IDs” field. If a user attempts to add additional values an error message displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/071.png)

<span id="_Toc83910161" class="anchor"></span>Figure 2‑67: All Selection Error Message

16. Select Save to add the new user to the users list. Select Cancel to cancel adding a new user.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/072.png)

<span id="_Toc83910162" class="anchor"></span>Figure 2‑68: Add User - Save and Cancel

#### Modify User Roles

System Administrators can modify user roles from the User Management screen. User roles include:

- Pharmacy Manager
- PBM Admin
- Pharmacy User
- Administrator

For further information on user roles and capabilities, refer to section <u>1.4 Roles and Capabilities</u>.

To modify user roles:

1.  From the users list, locate the user and select the checkbox(es) for the desired user role(s).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/073.png)

<span id="_Toc83910163" class="anchor"></span>Figure 2‑69: Select User Roles

2.  Select Save at the bottom of the screen.

A message displays indicating that the user was updated successfully.

3.  Select Cancel to cancel modifying user roles.

#### Enable/Disable Users

Users can be disabled and/or re-enabled to use the web application. Enabling and disabling a user’s access is selected using the “Enable/Disable User” checkbox in the desired user’s row. A deselected checkbox (shown below) reflects that the user’s access is enabled, and a selected checkbox reflects that the user’s access has been disabled.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/074.png)

<span id="_Toc83910164" class="anchor"></span>Figure 2‑70: User Management Table – Enable/Disable User

To update a user’s access:

1.  Locate the user in the User Management table.
2.  Select the checkbox in the “Enable/Disable User” column to disable access or deselect the checkbox to re-enable access.
3.  Select Save from the bottom of the screen (not shown) to update the user’s access.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/075.png)

<span id="_Toc83910165" class="anchor"></span>Figure 2‑71: User Disabled

When a user is disabled, their information is greyed in the User Management table.

If a user that has been disabled tries to log in to the application, an error message displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-617-and-pso-7-670/076.png)

<span id="_Toc83910166" class="anchor"></span>Figure 2‑72: User Disabled Error Message