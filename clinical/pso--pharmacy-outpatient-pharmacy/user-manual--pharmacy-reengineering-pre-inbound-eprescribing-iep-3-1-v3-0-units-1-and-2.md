---
title: Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) 3.1 Version 3.0 User Manual (Units 1 and 2)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Version 3.0  (Units 1 and 2)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 3.1
patch_id: PSO*3.1
group_key: "PSO:PSO:3.1"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of PRE IEP is to enable the VA to receive and subsequently process electronic prescriptions (eRxs) from outside of VA. This user guide serves as a guide and useful reference for VA Pharmacy Users, Systems Administrators, Managers, and other VA staff to assist in accessing, navigating, an
audience: 
keywords: 
  - blockquote
  - class
  - pharmacy
  - span
  - inbound
  - table
  - eprescribing
  - figure
  - strong
  - message
page_count: 0
word_count: 11057
section_count: 9
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_iep_um_1_2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_iep_um_1_2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

# Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) 3.1 User Manual


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) 3.1 User Manual](#pharmacy-reengineering-pre-inbound-eprescribing-iep-31-user-manual)
    - [June 2020](#june-2020)
    - [Department of Veterans Affairs (VA) Office of Information and Technology (OIT)](#department-of-veterans-affairs-va-office-of-information-and-technology-oit)
    - [List of Tables](#list-of-tables)
- [![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/004.png)Introduction to Inbound ePrescribing](#pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-004pngintroduction-to-inbound-eprescribing)
  - [Organization of the Inbound ePrescribing User Guide](#organization-of-the-inbound-eprescribing-user-guide)
  - [Inbound ePrescribing Overview](#inbound-eprescribing-overview)
    - [Purpose](#purpose)
    - [Overview](#overview)
    - [User Interfaces](#user-interfaces)
    - [Inbound ePrescribing Workflow](#inbound-eprescribing-workflow)
  - [Inbound ePrescribing Architecture](#inbound-eprescribing-architecture)
  - [Roles and Capabilities](#roles-and-capabilities)
  - [Help Desk](#help-desk)
    - [Help Desk Ticket Instructions](#help-desk-ticket-instructions)
  - [Fax Failover](#fax-failover)
- [![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/013.png)Inbound ePrescribing Web-Based Application](#pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-013pnginbound-eprescribing-web-based-application)
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
![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/001.png)

### June 2020

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 3.0 (Units 1 and 2)

### Department of Veterans Affairs (VA) Office of Information and Technology (OIT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Revision History
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/15/2020</td>
<td>3.0</td>
<td><blockquote>
<p>PSO*7.0*610:</p>
</blockquote>
<ul>
<li><p>Added <a href="#_bookmark105"><u>NOTE</u></a> to indicate a minor change in the display of the <strong>Station ID</strong> drop-down list in the <strong>Reports</strong> tab</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/23/2020</td>
<td>2.9</td>
<td><blockquote>
<p>PSO*7.0*590:</p>
</blockquote>
<ul>
<li><p>Added production application <a href="#_bookmark29"><strong>URL</strong></a></p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/05/2020</td>
<td>2.8</td>
<td><blockquote>
<p>PSO*7.0*591:</p>
</blockquote>
<ul>
<li><p>Updated <a href="#_bookmark214"><strong>Figure 3-44</strong></a> and <a href="#_bookmark229"><strong>Figure 3-53</strong>.</a></p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/27/2019</td>
<td>2.7</td>
<td><blockquote>
<p>PSO*7.0*567:</p>
</blockquote>
<ul>
<li><p>Help Desk contact information/name</p></li>
<li><p>Screen capture dates for ERX Lookback Days beginning with page <a href="#_bookmark271">98</a> through <a href="#_bookmark488">189.</a></p></li>
<li><p>Corrected <a href="#_bookmark169"><strong>Figure 3-12</strong></a> and reworded the bullets above</p></li>
<li><p>Added <a href="#_bookmark170"><strong>Figure 3-13</strong></a></p></li>
<li><p>Title page, TOC, LOF, and Footers</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/07/2019</td>
<td>2.6</td>
<td><blockquote>
<p>PSO*7.0*551:</p>
<p>Updated document for the following:</p>
</blockquote>
<ul>
<li><p>Standardized images throughout document.</p></li>
<li><p>Clarified patient DOB format under Table 3.</p></li>
<li><p>Added Note to replace text “Dispense Notes” with “Substitutions” under Track/Audit Details screen in the Inbound/Outbound Message Detail section.</p></li>
<li><p>Added Note to indicate the change of screen/page title from “Users” to “User Management” in the User Management section.</p></li>
<li><p>Included description for ERX LOOK-BACK DAYS display on the Holding Queue’s Traditional View and Patient Centric Views in the eRx Default Lookback Days section.</p></li>
<li><p>Replaced column label “LAST USER” with “LOCKED BY” and updated the description under Table 9.</p></li>
</ul></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><ul>
<li><p>Added the information for LOCKED BY column in the Patient Centric View section.</p></li>
<li><p>Replaced Figure 3-14, Figure 3-16, Figure 3-17, Figure 3-18, Figure 3-19, Figure 3-42,</p></li>
</ul>
<blockquote>
<p>Figure 3-52, Figure 3-55<strong>,</strong> Figure 3-56, Figure</p>
<p>3-57, Figure 3-59, Figure 3-60, Figure 3-61, and Figure 3-68 for updated layout</p>
</blockquote>
<ul>
<li><p>Added Note and included Figure 3-48 to indicate to the user that a Provider’s DEA# has expired in the Edit Provider section.</p></li>
<li><p>Removed reference to “Limited Duration” field from Validate Drug/SIG for the modified workflow in the Edit Drug/SIG section.</p></li>
<li><p>Added description under Note for modified workflow in the <a href="#_bookmark236">Edit Drug/SIG</a> section.</p></li>
<li><p>Updated description for VistA Days Supply calculation in the Additional Field-level Information: section.</p></li>
<li><p>Added scenarios for Quantity/Days Supply workflow under VD Edit screen based on Available Dosage(s) in the Quantity/Days Supply work flow under Validate Drug/SIG &gt;&gt; Edit: section.</p></li>
<li><p>Added Note to replace text “Qty Qualifier” with “Code List Qualifier” and replace, “DAW Code’ with “Substitutions” in the Complete Orders from OERR and Patient Prescription Processing section.</p></li>
<li><p>Added Note describing eRx Date, Date Written, Issue Date and Written Date fields in the Complete Orders from OERR and Patient Prescription Processing section.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td>11/09/2018</td>
<td>2.5</td>
<td><blockquote>
<p>Updated per HPS Review pgs.: 55, 57, 87, 88, 90,</p>
<p>92, 194, and 195.</p>
<p>Updated Cover page to month of November (pg. i) (TWR, 508 accessibility checks, document is compliant).</p>
</blockquote></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/24/2018</td>
<td>2.4</td>
<td><blockquote>
<p>Update TOC – Remove Graphic and reran TOC.</p>
</blockquote></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/27/2018</td>
<td>2.3</td>
<td><blockquote>
<p>Technical Writer Review and 508 accessibility checks.</p>
</blockquote></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/01/2018</td>
<td>2.2</td>
<td><blockquote>
<p>Updated screenshots and added Refill Requests and Responses and Cancel Rx Requests and Responses sections.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/28/2018</td>
<td>2.1</td>
<td><blockquote>
<p>Updated screenshots and added 30-day Lookback</p>
</blockquote></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/12/2018</td>
<td>2.0</td>
<td><blockquote>
<p>Updated screenshots to include 2.1 changes</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/15/2017</td>
<td>1.0</td>
<td><blockquote>
<p>Baseline release: Updated Table of Figures.</p>
</blockquote></td>
<td><blockquote>
<p>Technatomy</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Updates based on feedback from HPS.</p>
<p>Updated screenshots and verbiage throughout the document, formatting and sections Inbound ePrescribing Workflow and Summary Screen, Pharmacy Management section.</p>
<p>Updates made based on changes made during SureScripts Certification and IOC Production Testing</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1: Inbound ePrescribing Web-Based Application User Roles & Capabilities 8](#_bookmark14)
> [Table 2: Inbound eR<sub>x</sub> VistA Holding Queue User Roles & Capabilities 9](#_bookmark15)
> [Table 3: Track/Audit Search Criteria Descriptions 25](#_bookmark69)
> [Table 4: Search Results Fields & Descriptions 27](#_bookmark72)
> [Table 5: New R<sub>x</sub> Only Summary Report Columns 40](#_bookmark109)
> [Table 6: Auto Check Details Report Columns 41](#_bookmark113)
> [Table 7: Reject Reason Report Columns 43](#_bookmark117)
> [Table 8: eR<sub>x</sub> Summary Report Columns 45](#_bookmark121)

# ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/004.png)Introduction to Inbound ePrescribing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This unit provides the purpose and organization of the Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) solution and a list of acronyms and abbreviations.

## Organization of the Inbound ePrescribing User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE IEP user guide is comprised of the following sections:

- [<u>Unit 1 – Introduction to Inbound ePrescribing</u>](#introduction-to-inbound-eprescribing): Discusses general PRE Inbound ePrescribing information.
- <u>Unit 2 - [Inbound ePrescribing Web-Based Application](#inbound-eprescribing-web-based-application-1)</u>: Outlines the IEP web-based application and capabilities, including Pharmacy Management, Track/Audit, Reports, and User Management functions.
- [<u>Unit 3 – Inbound eRx VistA Outpatient Pharmacy</u>](#_bookmark139): Discusses the VistA OP eRx Holding Queue and capabilities, including eRx validation, search, sort, hold, acceptance, remove, and rejection.
- <u>Unit 4 - [Refill Requests and Responses](#_bookmark322)</u>: Discusses the Refill Requests and Responses. The Refill Requests function is used by pharmacists to generate and send an outbound Refill Request. After a Refill Request has been sent to the external provider, the provider will be able to send a Refill Response back to the requesting Pharmacy.
- <u>Unit 5 - [Cancel Rx Requests and Responses](#_bookmark430)</u>: Discusses the Cancel Rx Request and Response. The Cancel Rx Request is sent by the external/non-VA Provider for an original New Rx, so it is not processed and dispensed by VA Pharmacy. Upon successfully canceling a New Rx, the VA Pharmacy sends back a Cancel Rx Response.

## Inbound ePrescribing Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE IEP functionality addresses a longstanding need for the Department of Veterans Affairs (VA) to be able to receive and process prescriptions from external providers. This enhancement moves the VA towards increased efficiency and improved customer satisfaction.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of PRE IEP is to enable the VA to receive and subsequently process electronic prescriptions (eRxs) from outside of VA. This user guide serves as a guide and useful reference for VA Pharmacy Users, Systems Administrators, Managers, and other VA staff to assist in accessing, navigating, and performing tasks associated with the PRE IEP web-based application and the Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy (OP) eRx Holding Queue.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To improve on its ability to deliver Veterans their medications as quickly and efficiently as possible, the Veterans Health Administration (VHA), Patient Care Services (PCS), and Pharmacy Benefits Management (PBM) requested a new capability as part of the PRE program to receive inbound eRxs from an external provider (e.g., a doctor not associated with the VA, medical staff at a Department of Defense (DoD) military treatment facility, etc.).

Overall, PRE IEP provides:

- Improved efficiency. More efficient use of VA pharmacy resources and non-VA provider resources based on:
  - Fewer transcribing/translation errors
  - Clear/error-free communications
  - Time saved not having to communicate back and forth regarding the content of a prescription
- Improved Veteran/beneficiary satisfaction. Makes the existing manual processing easier, more efficient, and more effective through the automation of the prescription process by:
  - Reducing the risk of loss of paper Rxs
  - Enabling more secure communication of Rx data
  - Providing timelier dispensing of Rxs prescribed by non-VA providers
- Improved patient safety: Reduces transcription errors
- Improved data accuracy: Provides enhanced functionality within VistA OP that improves the accuracy and use of the data it collects

By automating data transmission from providers to the VA, and between other pharmacies, the need for VA pharmacy personnel to manually input Rx data from non-VA providers is largely eliminated, reducing the chance for data to be entered incorrectly or missed.

Specific elements of what is included in PRE IEP include:

- Receiving and processing inbound eRxs, where “inbound” refers to the ordering of medication or medical related supplies for a VA patient by a non-VA provider; to be filled at a VA pharmacy.
- Pharmacy Service is not responsible for filling prescriptions for non-expendable medical equipment.
- Pharmacy Service may dispense refills for expendable supplies upon receipt of requests from patients with continuing eligibility for a period not to exceed one year from the date of the last signed order.
- Expendable stock items may include: catheters, colostomy sets, ileostomy sets and/or supplies, plastic and rubber gloves, skin preparations and powders, urinal bags and drainage supplies, incontinence supplies, etc.
- Electronically receiving and processing outpatient prescriptions only, including prescriptions created for a VA patient upon discharge from a non-VA hospital to be filled on an outpatient basis by a VA pharmacy.
- Receiving and processing inbound eRxs from non-VA providers that currently prescribe medications and medical-related supplies for Civilian Health and Medical Program of the VA (CHAMPVA) beneficiaries, and which are currently handled by the Meds by Mail (MbM) program.
- Sending outbound electronic notifications from a VA pharmacy that received an inbound eRx, to the non-VA provider that originally sent the eRx.

The following areas are not included in PRE IEP:

- VA providers generating eRxs at one VA Medical Center (VAMC) location to be electronically transmitted to and processed by (filled, dispensed, etc.) a different VAMC location’s pharmacy.
- Initiating outbound eRxs (generation of an eRx by a VA provider to be filled at a non-VA pharmacy).
- Electronic receipt and processing of any VA or non-VA inpatient medication orders.
- Electronic receipt and processing of any VA or non-VA orders for Durable Medical Equipment (DME), such as wheelchairs.
- Electronic receipt and processing of Rx refill requests from a VA patient’s non-VA Electronic Health Record (EHR) system.
- Electronic transfers of prescriptions from any non-VA pharmacy to a VA pharmacy.
- Electronic transfers of prescriptions from a VA pharmacy to a non-VA pharmacy.
- The ability for the VA to request an Electronic Prior Authorization (ePA) form and authorization from a provider.

The following are out of an eRx user’s control, which requires validation by Pharmacists.

- Patient: eRxs can be sent for any patient, including Veterans or non-Veterans.
- Provider: eRxs can be sent by any provider, whether VA authorized or not.
- Drugs: VA has no control over the drug, nor the name of drug sent to VA.
- SIG: VA has no control over directions that are sent to VA.
- All information coming to the VA is controlled by the EHR system which is what the provider is using to send information to the VA. VA has no control over the process.

### User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two user interfaces associated with IEP, including the following:

- IEP Web-Based Application
- Inbound eRx VistA Outpatient Pharmacy

#### Inbound ePrescribing Web-Based Application

The IEP web-based application is used by Pharmacy Users, Administrators, Pharmacy Managers, and PBM Admin personnel. It has tab displays for the following:

- Home
- Pharmacy Management
- Track/Audit
- Reports
- User Management
- Help

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/005.png)

<span id="_bookmark7" class="anchor"></span>Figure 1-1: Inbound ePrescribing Web-based Application

The IEP web-based application is discussed in more detail in [<u>Unit 2 - Inbound ePrescribing</u>](#inbound-eprescribing-web-based-application-overview) [<u>Web-Based Application</u>](#inbound-eprescribing-web-based-application-overview).

#### Inbound eRx VistA Outpatient Pharmacy

The Inbound eRx VistA Outpatient Pharmacy display screens include VistA screens that are used by VA Pharmacists and Technicians to validate and process eRxs.

The eRx Holding Queue is discussed in more detail in [<u>Unit 3 - Inbound eRx VistA Outpatient</u>](#_bookmark139) [<u>Pharmacy</u>](#_bookmark139).

### Inbound ePrescribing Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IEP workflow is illustrated in the figure and described below.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/006.png)

<span id="_bookmark10" class="anchor"></span>Figure 1-2: Inbound ePrescribing Process Flow

1.  eRxs are sent from an external provider to SureScripts and/or Change Healthcare (CH). CH provides commercial ePrescribing solutions and, for the purposes of the IEP implementation, serves as a gateway to all participating ePrescribing providers nationwide.
2.  CH verifies and transmits eRx transactions to/from SureScripts and/or an external provider’s EHR system and the IEP system.
3.  The eRxs are routed from CH to the IEP Processing Hub via the Data Access Service (DAS) external gateway. DAS and CH communicate using https requests over a secured network.
4.  In the IEP Processing Hub, auto-checks occur on the eRxs for Patient, Provider, and Drug/SIG. The Master Veteran Index (MVI) is used for patient checking, depending on the data set that is sent by the Prescriber for that patient. For patient Enrollment and Eligibility (E&E) checks, the Enrollment System (ES) is utilized. The ES assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with E&E data. The E&E check is optional and can be turned on or off for each site. Patient Registration is also confirmed against the instance of the receiving pharmacy.
5.  The Drug Name is matched against the local Drug File first, the VA Product Name next and then the National Drug Code (NDC), depending on which it matches first on. As a note, auto-checks can be incorrect therefore the data must also be validated against the original eRx data sent (Please refer to the [Validate Drug/SIG](#_bookmark230) section).
6.  The IEP web-based GUI allows users to view and generate reports on the auto-check results in the Processing Hub, as well as manage VA pharmacy information, and search for and print an eRx.
7.  Once the eRx has completed all auto-checks in the IEP Processing Hub, the original prescription, as well as the outcomes of all the auto-checks (patient, provider, and drug), are transmitted to VistA OP. VistA Link is used for the provider and drug checks against the VistA OP system.
8.  The VistA OP’s IEP Holding Queue allows for the initial validation and acceptance of an eRx before being transmitted to Pending Outpatient Orders file for additional order checks and then final dispensing.
9.  A Refill Renewal Request transaction is originated by the pharmacy. This transaction is for requesting approval for additional refills of a prescription once the original number of refills has been dispensed. A Refill Renewal Response is sent by the prescriber to the pharmacy in response to a request to refill a prescription. The response indicates whether the Refill Renewal Request has been accepted or denied.
10. A Cancel Rx Request message is used to notify the pharmacy that a previously sent prescription should be cancelled and not filled. The message is originated by the prescriber system as a Cancel Rx Request message. The Cancel Rx Response message is sent from the pharmacy to the prescriber system in response to a Cancel Rx Request message.
11. Patient Centric View is a dashboard view, in addition to the Traditional View of the eRx Holding Queue, to provide the user the ability to view the eRx records that are in actionable statuses and that are grouped by Patients. The user can further select and view only the patients who have new prescriptions in one of the actionable statuses. The user

> can also jump to the Outpatient side and navigate back to the Holding Queue when there is a Pending Order for the selected patient. Each site can configure the number of lookback days to view the patient/prescription records that are still actionable statuses in the Holding Queue.

## Inbound ePrescribing Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/007.png)The IEP architecture is illustrated in the below figure, which depicts the different programs/applications that IEP interfaces with.

<span id="_bookmark12" class="anchor"></span>Figure 1-3: Inbound ePrescribing Architecture

## Roles and Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IEP roles and tasks are described in this section as primary and secondary users. Primary users include VA Pharmacy Users. Secondary users include System Administrators, VA Pharmacy Managers, VA PBM personnel, Non-VA Providers, and External Pharmacy personnel. The

following sections provide an overview of primary and secondary user roles and their capabilities within IEP.

VA users have the capability of performing eRx-related tasks in the IEP web-based application and in the VistA OP eRx Holding Queue module. Specific tasks for each component are described in more detail in <u>Unit 2.</u> [<u>Inbound ePrescribing Web-Based Application</u>](#inbound-eprescribing-web-based-application-1) and [<u>Unit 3</u>](#_bookmark139) [<u>Inbound eRx VistA Outpatient Pharmacy</u>](#_bookmark139).

The primary users of IEP are VA Pharmacy Users. Secondary user roles of this functionality include:

- Administrator – VA Local and National System Administrators.
- Pharmacy Manager – VA Pharmacy Management to include VA management, hospital director, under sec, etc., or anyone outside pharmacy that will need to know how many and what is the cost of the project.
- PBM Admin – All VA PBM personnel, including management.
- Non-VA Providers – Submit inbound requests to VA and review statuses sent from VA.

> Details of the roles and capabilities for each user in the IEP web-based application and the VistA eRx Holding Queue are outlined in the tables below. Users with the ability to add/update a pharmacy may only add/update pharmacies for the site(s) in which the user is assigned to. Any user that is not assigned to MbM sites cannot view the Track/Audit records of MbM sites.

<span id="_bookmark14" class="anchor"></span>Table 1: Inbound ePrescribing Web-Based Application User Roles & Capabilities

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User Role</strong></th>
<th><strong>Functionality</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Administrator</td>
<td>Full Control, access to all tabs</td>
</tr>
<tr class="even">
<td>Pharmacy Management</td>
<td><p>Home</p>
<p>Pharmacy Management Track/Audit</p>
<p>Reports Help</p></td>
</tr>
<tr class="odd">
<td>PBM Administrator</td>
<td><p>Home</p>
<p>Pharmacy Management Track/Audit</p>
<p>Reports Help</p></td>
</tr>
<tr class="even">
<td>Pharmacy Users</td>
<td>Home Track/Audit Reports Help</td>
</tr>
<tr class="odd">
<td>Default VA User (Read Only)</td>
<td>Home Reports Help</td>
</tr>
</tbody>
</table>

<span id="_bookmark15" class="anchor"></span>Table 2: Inbound eRx VistA Holding Queue User Roles & Capabilities

<table style="width:100%;">
<colgroup>
<col style="width: 40%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Security Key</strong></th>
<th><strong>PSD RPH</strong></th>
<th><blockquote>
<p><strong>PSO ERX ADV TECH</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PSO ERX TECH</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PSO ERX VIEW</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Validate Patient</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Validate Provider</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Validate Drug/SIG</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Accept Validation</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Accept eRx</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reject</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Remove</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Hold</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Un Hold</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Search/Sort</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Print</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Message View</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Ack – Refill Response</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>eRx Change Request</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Refill Request (OP)</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Ack – Rx Cancel</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ack – Inbound Refill Error</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Help Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues with the IEP web-based application that cannot be resolved by this manual or the site administrator, please contact the Enterprise Service Desk (ESD) at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

### Help Desk Ticket Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To submit a Help Desk ticket:

1.  Select the “Your IT” icon on your desktop.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/008.png)

<span id="_Toc104287495" class="anchor"></span>Figure 1-4: YourIT Desktop Icon

The homepage displays.

2.  Select Incident.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/009.png)

3.  Select Create New.

<span id="_Toc104287496" class="anchor"></span>Figure 1-5: Incident Section

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/010.png)

4.  Populate the required fields.

<span id="_Toc104287497" class="anchor"></span>Figure 1-6: Create New

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/011.png)

<span id="_bookmark21" class="anchor"></span>Figure 1-7: Category and Enterprise Application Required Fields

5.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/012.png)Select Submit.

Figure 1-8: New Incident

## Fax Failover

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Change Healthcare attempts to send an eRx to a pharmacy, but VA Inbound eRx Processing Hub does not send an NCPDP STATUS message back before the request times out, a “FAX failover” occurs. Change Healthcare delivers the eRx message via FAX using the FAX number on record of the destination pharmacy. A failover to FAX is a rare occurrence. VA Pharmacies need to process eRx records received via FAX as non-electronic Rxs. There will be no record of these FAX messages in either the Inbound eRx Processing Hub or the VistA OP Holding Queue.

# ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/013.png)Inbound ePrescribing Web-Based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Inbound ePrescribing Web-Based Application Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the Inbound ePrescribing web-based application.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inbound ePrescribing (IEP) web-based application provides eRx management, administration, and monitoring capabilities.

### Access Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user should contact the supervisor or the administrator assigned at their local site for managing the application for questions on access to the IEP web-based application and/or modifications to user roles/permissions.

### Accessing the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the production Inbound eRx application go to this <span id="_bookmark29" class="anchor"></span>URL in your browser: <u>https://vaausappiep221.aac.va.gov/inbound/</u>

A Personal Identification Verification (PIV) card is required to access the application, using the following steps:

1.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/014.png)On the VA Single Sign-on screen, select the Sign In with VA PIV Card icon.

<span id="_bookmark30" class="anchor"></span>Figure 2-1: VA Single Sign-on

2.  In the “Select a Certificate” dialog, select the desired certificate and then select OK.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/015.png)

<span id="_bookmark31" class="anchor"></span>Figure 2-2: Select a Certificate

3.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/016.png)In the “ActivClient Login” dialog, enter the Personal Identification Number (PIN) in the “PIN” text box and select OK.

<span id="_bookmark32" class="anchor"></span>Figure 2-3: Active Client Login

4.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/017.png)A warning message displays. Select Accept.

<span id="_bookmark33" class="anchor"></span>Figure 2-4: Warning Message

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/018.png)When authentication and authorization is successful, the application home screen displays.

> <span id="_bookmark34" class="anchor"></span>Figure 2-5: Home Screen

### Screen Navigation and Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure outlines the key areas of the screen layout. Brief descriptions of the screen layout are provided below:

1.  On the top-right of the screen is a Go to Main Content link for Section 508 purposes to allow a user to be directed to the main content on the screen.
2.  The logged-in user’s VA User ID and logout link displays on the right side of the banner.
3.  Below the banner, the main tabs display for accessing the screens within the application.
4.  The name of the screen displays below the main tabs.
5.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/019.png)The bottom of the screen also contains links to the main tabs.

<span id="_bookmark36" class="anchor"></span>Figure 2-6: Web-Based Application Screen Layout

Only the menu bar tabs that the user has access to display. Access to the tab displays or screens is granted or restricted by roles assigned to the user by the administrator. For additional information, please refer [to the Roles and Capabilities](#roles-and-capabilities) section in this guide.

The tabs include:

- Home/Inbound eRx Homepage – All Users
- Pharmacy Management – Administrators, Pharmacy Managers, and PBM Admin
- Track/Audit – Administrators, Pharmacy Managers, PBM Admin, and VA Pharmacy Users
- Reports – All Users
- User Management – Administrators
- Help – All Users

#### Inbound eRx Homepage

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/020.png)The Inbound eRx Homepage is displayed when successful login authentication and verification is completed. The Inbound eRx Homepage is always accessible by selecting the Home tab in the menu bar. The Home screen is accessible to all user roles. However, only the tabs authorized for the user’s role are displayed.

#### Pharmacy Management

<span id="_Toc104287505" class="anchor"></span>Figure 2-7: Home Screen

To access the Pharmacy Management screen, select the Pharmacy Management tab in the menu bar. The Pharmacy Management screen displays the Pharmacy Management table that provides information about pharmacies and allows Administrators and Pharmacy Managers to search for, add, and edit pharmacies. Users can also enable/disable the receiving of prescriptions targeted for a particular pharmacy.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/021.png)

#### Track/Audit

<span id="_Toc104287506" class="anchor"></span>Figure 2-8: Pharmacy Management Screen

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/022.png)To access the Track/Audit eRx screen, select the Track/Audit tab in the menu bar. The Track/Audit eRx screen that displays allows users view eRxs and their related messages.

#### Reports

<span id="_Toc104287507" class="anchor"></span>Figure 2-9: Track/Audit Screen

To access the Reports screen, select the Reports tab in the menu bar. The Reports screen provides all users with the ability to run and view a Summary Report.

The system uses the comma-separated value (.CSV) format. Users can view reports using a third- party tool, such as Microsoft Excel.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/023.png)

<span id="_Toc104287508" class="anchor"></span>Figure 2-10: Reports Screen

#### User Management

To access the User Management screen, select the User Management tab in the menu bar. The User Management screen provides Administrators with the ability to add users, enable/disable users, and modify user roles. This screen only displays for users with Administrator access.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/024.png)

<span id="_Toc104287509" class="anchor"></span>Figure 2-11: User Management Screen

<span id="_bookmark46" class="anchor"></span>

#### Help Page

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/025.png)To access the Help page, select the Help tab in the menu bar. The Help page provides help topics and production support information.

<span id="_bookmark48" class="anchor"></span>Figure 2-12: Help Tab

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/026.png)When the Help tab is selected, the Help Page displays in a new window.

<span id="_bookmark49" class="anchor"></span>Figure 2-13: Help Page

## Inbound ePrescribing Web-based Application Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide descriptions of the IEP web-based application’s capabilities within each tab.

### Pharmacy Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Management screen displays the Pharmacy Management table. The default view displays all VA pharmacies. Actions available to users include:

- [<u>Searching for a Pharmacy</u>](#searching-for-a-pharmacy)
- [<u>Adding a Pharmacy</u>](#adding-a-pharmacy)
- [<u>Updating a Pharmacy</u>](#updating-a-pharmacy)

#### Searching for a Pharmacy

Users can search for a pharmacy from the Pharmacy Management screen. The default view lists all VA pharmacies.

To search for a pharmacy:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/027.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/028.png)Enter the NCPDP ID (if known). Enter the Pharmacy Name.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/029.png)Select the desired VISN number from the “VISN” drop down.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/030.png)Select the desired Station ID from the “Station ID” drop down. If viewing All VISNs, the user is unable to select a Station ID. To select a specific Station ID, the VISN must be selected.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/031.png)Select Search.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/032.png)The Pharmacy Management table displays results for the selected search criteria.

#### Adding a Pharmacy

<span id="_Toc104287512" class="anchor"></span>Figure 2-14: Search for a Pharmacy

To add a new pharmacy, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

#### Updating a Pharmacy

To update information for a VA pharmacy, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

#### Disable eRx

To completely halt a specific Pharmacy from receiving ePrescriptions, please contact the ESD at 1-855-673-4357 and reference “VistA - Pharmacy: Outpatient Pharmacy.”

> <span id="_bookmark57" class="anchor"></span>Temporarily Disable eR<sub>x</sub>

In case where a site needs to halt receiving ePrescriptions temporarily, use Disable eRx/Enable eRx fields.

Disabling a pharmacy allows users the ability to temporarily disable the pharmacy from receiving eRxs in the event of a natural or facility disaster, maintenance, or move. This disables the pharmacy from receiving New eRxs, but outbound messages still go back to the external provider via CH. The pharmacy is disabled on the Processing Hub, but no changes are made in CH.

To temporarily disable a pharmacy: Search for the desired pharmacy.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/033.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/034.png)From the Pharmacy Management table, select the hyperlink for the desired pharmacy to

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/035.png)edit in the “NCPDP ID” column.

<span id="_bookmark58" class="anchor"></span>Figure 2-15: NCPDP ID Column Hyperlinks

The Edit Pharmacy screen displays. At the top of the screen is a Warning Message with text notifying the user that any change made here will not updated the pharmacy in Change Healthcare’s published pharmacy directory. Selecting the Return to Pharmacy Management button returns the user to the Pharmacy Management screen.

3.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/036.png)Select No from the “Inbound eRx Enabled” drop down.

<span id="_bookmark59" class="anchor"></span>Figure 2-16: eRx Enabled Drop Down

4.  ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/037.png)At the bottom of the Edit Pharmacy screen, select Update to save all changes. The date that the fields were modified displays in the “Updated Date” field.

#### Enable eRx

<span id="_Toc104287515" class="anchor"></span>Figure 2-17: Update Pharmacy Information

The pharmacy can be enabled once it is ready to receive eRxs again. To enable a pharmacy select Yes from the “Inbound eRx Enabled” drop down on the Edit Pharmacy screen and select the Update button.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/038.png)

Figure 2-18: Enable/Disable Pharmacy

#### Enrollment and Eligibility Check

The Enrollment and Eligibility (E&E) check may be enabled or disabled for individual pharmacies. This option is provided so each pharmacy may decide whether to turn the E&E check on or off depending on whether the patients whose eRxs are filled at the pharmacy are enrolled in the E&E system. For example, MbM does not currently have any patient enrolled with the E&E system.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/039.png)To ensure the Enrollment and Eligibility Check is enabled for a pharmacy, select the desired pharmacy from the Pharmacy Management table and ensure Yes displays in the “Enrollment and Eligibility Check Enabled” field.

<span id="_bookmark64" class="anchor"></span>Figure 2-19: Enrollment and Eligibility Check Enabled

If the Enrollment and Eligibility Check is not enabled for a pharmacy, the Patient Auto Check Status displays as “EandE_CHECK_NOT_PERFORMED” on the Track/Audit screen.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/040.png)

<span id="_bookmark65" class="anchor"></span>Figure 2-20: Track/Audit – Enrollment and Eligibility Check Not Performed

### Track/Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Track/Audit screen allows users to search for eRx messages and track prescriptions and provides the ability to view and print the details of a prescription.

When the user initially enters the Track/Audit page, the default date range is two days (the current date and the previous date).

#### Searching for a Message

To search for a message:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/041.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/042.png)Select the desired search criteria from the drop downs and enter search keywords in the text fields. The search criteria are listed in the table below.

<span id="_bookmark68" class="anchor"></span>Figure 2-21: Track/Audit Search Criteria

> <span id="_bookmark69" class="anchor"></span>Table 3: Track/Audit Search Criteria Descriptions

<table style="width:100%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Search Field</strong></th>
<th><blockquote>
<p><strong>Field Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Drop Down Options</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VISN</td>
<td><blockquote>
<p>Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>VISN number that a VA pharmacy is associated with</p>
</blockquote></td>
<td><blockquote>
<p>All VISNs, each VISN number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA Station ID</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Station ID of the VA pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>From</td>
<td><blockquote>
<p>Text or Calendar Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>Beginning date. Choose From date for the date range search, select date from calendar or type date</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>To</td>
<td><blockquote>
<p>Text or Calendar Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>End date. Choose To date for a date range search; select the date from the calendar or enter a date in MM/DD/YYYY format</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Message Type</td>
<td><blockquote>
<p>Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>Type of the NCPDP message type</p>
</blockquote></td>
<td><blockquote>
<p>All, CancelRx, CancelRxResponse, Error, NewRx, RefillResponse, RefillRequest, Status, Verify</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Message ID</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Prescription message ID (generated by Change Healthcare for incoming eRxs)</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Relates to Message ID</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>To search for messages related to a Message ID</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Patient Social Security Number</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient Last Name</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Patient last name</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Patient First Name</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Patient first name</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient DOB</td>
<td><blockquote>
<p>Text or Calendar Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>Patient date of birth</p>
</blockquote></td>
<td><blockquote>
<p>Calendar/Enter DOB in MM/DD/YYYY format</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prescriber NPI</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Prescriber National Provider Identifier (NPI)</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Prescribed Drug</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Drug prescribed from the eRx</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prescriber First Name</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>First name of prescriber</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Prescriber Last Name</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Last name of prescriber</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prescriber DEA #</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Drug Enforcement Administration (DEA) number of prescriber</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Search Field</strong></th>
<th><blockquote>
<p><strong>Field Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Drop Down Options</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Message Status</td>
<td><blockquote>
<p>Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>Processing Hub message status</p>
</blockquote></td>
<td><blockquote>
<p>Auto-check Processing Completed, VistA OP Delivery Successful, VistA OP Delivery Retries Exceeded, Auto check in Progress, Pharmacy Inbound eRx Not Enabled, Pharmacy Unknown</p>
</blockquote></td>
</tr>
<tr class="even">
<td>eRx Reference #</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Unique, internal VA reference # assigned to all messages</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Sent or Received</td>
<td><blockquote>
<p>Drop Down</p>
</blockquote></td>
<td><blockquote>
<p>Select Sent (Outbound) or Received (Inbound) messages</p>
</blockquote></td>
<td><blockquote>
<p>Received, Sent</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/043.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/044.png)Select Search to execute the search.

<span id="_bookmark70" class="anchor"></span>Figure 2-22: Track/Audit eRx Search

The search results display in the table. The total number of records in the search results display at the bottom of the table.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/045.png)

<span id="_bookmark71" class="anchor"></span>Figure 2-23: Search Results

The Search Results fields and descriptions are listed in the table below.

> <span id="_bookmark72" class="anchor"></span>Table 4: Search Results Fields & Descriptions

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>eRx Reference #</td>
<td><blockquote>
<p>Unique, internal VA reference # assigned to all messages as a hyperlink</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Message Type</td>
<td><blockquote>
<p>Type of message</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient Name</td>
<td><blockquote>
<p>First and last name of the patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Patient DOB</td>
<td><blockquote>
<p>Date of birth for the patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient SSN</td>
<td><blockquote>
<p>Social security number of the patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Drug Prescribed</td>
<td><blockquote>
<p>Drug prescribed to the patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Message Id</td>
<td><blockquote>
<p>Identification of the message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prescriber Name</td>
<td><blockquote>
<p>First and last name of the prescriber</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Prescriber NPI</td>
<td><blockquote>
<p>National Provider Identifier for the prescriber</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prescriber DEA</td>
<td><blockquote>
<p>Identifier assigned to prescriber by United States Drug Enforcement Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VISN</td>
<td><blockquote>
<p>VISN that the VA pharmacy is associated with</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Station ID</td>
<td><blockquote>
<p>Station ID of the VA pharmacy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Pharmacy Name</td>
<td><blockquote>
<p>Internal VA pharmacy name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Address</td>
<td><blockquote>
<p>Address of VA pharmacy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Relates to Message ID</td>
<td><blockquote>
<p>Lists message related to a particular Message ID as a hyperlink</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Received Date</td>
<td><blockquote>
<p>Date that the eRx was received by VA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient AutoCheck Status</td>
<td><blockquote>
<p>Results of system patient auto-validation check</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Provider AutoCheck Status</td>
<td><blockquote>
<p>Results of system provider auto-validation check</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Drug AutoCheck Status</td>
<td><blockquote>
<p>Results of system drug auto-validation check</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Message Status</td>
<td><blockquote>
<p>Current status of the message</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Export Search Results

From the Track/Audit tab, users have the capability of exporting the search results. Exports are in .CSV format and can be viewed in Microsoft Excel.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/046.png)To export the search results: Select the Export button.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/047.png)

<span id="_bookmark74" class="anchor"></span>Figure 2-24: Export Search Results

A prompt displays asking to Open or Save the results.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/048.png)Select Open to view the results.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/049.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/050.png)To save the results, select Save. The system displays a Save As dialog. Users should navigate to a location on their system to save the file.

<span id="_bookmark75" class="anchor"></span>Figure 2-25: Track/Audit Export Prompt (after clicking Export buttons)

#### Inbound/Outbound Message Detail

Inbound/outbound message detail information is reviewed and managed under the Track/Audit

tab.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/051.png)To access the detail screen of a message, select the hyperlink in the “eRx Reference \#” column.

<span id="_bookmark77" class="anchor"></span>Figure 2-26: Track/Audit Grid View

The message details display. Each message detail screen includes the following buttons:

- Return to Search: Return to the search results screen.
- Show Related Messages: Displays all sent and received eRx messages that are related to the displayed message.
- ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/052.png)Print: Print the eRx message details.

<span id="_bookmark78" class="anchor"></span>Figure 2-27: Message Details

If the Show Related Messages button is selected, any sent and received messages that are related to the current message display based on the Message ID linkage. For example, Related Messages for a Refill Response should, at minimum, display the related Refill Request and the New Rx for which the refill was requested. Related messages also include related Status, Verify, and/or Error Messages, if applicable. Related messages display in descending order of received date. The most recent message is at the top of the list, and the New Rx message is at the bottom. Select the eRx message number to view message details.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/053.png)

#### New Rx Message

<span id="_Toc104287526" class="anchor"></span>Figure 2-28: Related Messages

The New Rx detail screen displays the new eRx from an external provider.

To access the New Rx detail screen, select the hyperlink in the “eRx Reference \#” column.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/054.png)

<span id="_bookmark81" class="anchor"></span>Figure 2-29: eRx Reference \# Hyperlink

The details of the New Rx message display.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/055.png)

<span id="_bookmark82" class="anchor"></span>Figure 2-30: Track/Audit Detail Screen for New Rx Message Type

#### Refill Request

Refill Request Message details can be viewed under the Track/Audit tab.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/056.png)

<span id="_bookmark84" class="anchor"></span>Figure 2-31: Refill Request Search and Search Results

Select an eRx Reference number to display the Refill Request message detail screen.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/057.png)

<span id="_Toc104287530" class="anchor"></span>Figure 2-32: Refill Request Details Screen

<span id="_bookmark86" class="anchor"></span>

#### Refill Response

Refill Response Message details can be viewed under the Track/Audit tab.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/058.png)

<span id="_bookmark87" class="anchor"></span>Figure 2-33: Refill Response Search and Search Results

> Select an eRx Reference number to display the Refill Request message detail screen.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/059.png)

<span id="_bookmark88" class="anchor"></span>Figure 2-34: Refill Response Detail Screen

#### Cancel Rx

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/060.png)The Inbound Cancel Rx Request message details can be viewed under the Track/Audit tab.

<span id="_bookmark90" class="anchor"></span>Figure 2-35: Cancel Rx Search and Search Results

Select an eRx Reference number to display the Cancel Rx detail screen.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/061.png)

<span id="_bookmark91" class="anchor"></span>Figure 2-36: Cancel Rx Detail Screen

#### Cancel Rx Response

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/062.png)The Cancel Rx Response message details can be displayed under the Track/Audit tab.

> Figure 2-37: Cancel Rx Response Search and Search Results

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/063.png)The Cancel Rx Response detail screen displays.

<span id="_bookmark94" class="anchor"></span>Figure 2-38: Cancel Rx Response Detail Screen

#### Error Messages

At multiple points in the process, an Error transaction can be generated. Outbound Error Messages are sent when an eRx record that is NCPDP corrupted is received, when the receiving Pharmacy is not one of the VA pharmacies configured in the Inbound eRx system, or when an eRx record with a Written or Effective Date older than or equal to 365 days is received. A Reject transaction exercised by a Pharmacy user in the VistA Holding Queue is also sent outbound in the same format as an NCPDP Error Message.

Inbound Errors for VistA may be received under situations such as, the Prescriber’s EHR system is unable to receive and process a certain transaction sent from the Pharmacy or a connection between the Transaction Hub and Change Healthcare is not working.

To access the Error message detail screen, select the hyperlink in the “eRx Reference \#” column.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/064.png)

<span id="_bookmark96" class="anchor"></span>Figure 2-39: Error Message Search and Search Results

The Error message detail screen displays the error message details sent and received by the Processing Hub.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/065.png)

<span id="_Toc104287537" class="anchor"></span>Figure 2-40: Error Message Detail Screen

#### Verify Messages

The Verify message confirms delivery of a message to its final destination. The Verify message is an NCPDP transaction that indicates the acceptance of the request. This message is used to communicate the data content status of a transaction. Verify Messages sent from VistA or the Transaction Hub are Outbound Verify Messages. Verify Messages received from Change Healthcare and/or an External Provider’s EHR system are Inbound Verify Messages.

To access the Verify message detail screen, select the hyperlink in the “eRx Reference \#” column.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/066.png)

<span id="_bookmark99" class="anchor"></span>Figure 2-41: Verify Message Search and Search Results

The Verify message detail screen displays the verify message details sent by the Processing Hub.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/067.png)

<span id="_bookmark100" class="anchor"></span>Figure 2-42: Verify Message Detail Screen

#### Status Messages

The Status message is used to relay acceptance of a transaction back to the sender. The Status message is an NCPDP transaction that indicates the acceptance of the request. For Inbound eRx web-based application, Inbound Status messages are received from Change Healthcare and Outbound Status messages are sent from the Transaction Hub.

To access the Status message detail screen, select the hyperlink in the “eRx Reference \#” column.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/068.png)

<span id="_bookmark102" class="anchor"></span>Figure 2-43: Status Message Search and Search Results

The Status message detail screen displays the status message details received by the Processing Hub.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/069.png)

<span id="_bookmark103" class="anchor"></span>Figure 2-44: Status Message Detail Screen

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports tab is used to generate high-level reports. From the Reports tab, users can generate, view, and export the following reports:

- [<u>Summary Report New Rx Only</u>](#summary-report-new-rx-only)
- [<u>Auto Check Details Report</u>](#auto-check-details-report)
- [<u>Reject Reasons Report</u>](#reject-reasons-report)
- [<u>eRx Summary Report</u>](#erx-summary-report)

When the user initially views any of the Reports pages, the default date range is two days (the current date and the previous date).

#### Summary Report New Rx Only

The Summary Report – New Rx Only provides a summary of eRx auto-validation checks for only new Rxs. To run a New Rx Summary Report:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/070.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/071.png)From the Reports screen, select Summary Report New R<sub>x</sub> Only from the “Select Report” drop down.

<span id="_bookmark107" class="anchor"></span>Figure 2-45: Summary Report New Rx Only Drop Down Selection

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/072.png)Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/073.png)To narrow the search by VA Station ID, select the Station ID for the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/074.png)Select the date range from the Calendar drop down for the report or enter a date using the MM/DD/YYYY format.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/075.png)Select the Run Report button to generate the report.

The Summary Report New Rx Only displays.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/076.png)

<span id="_Toc104287543" class="anchor"></span>Figure 2-46: New Rx Summary Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

Reports can be viewed in the web application or they can be exported. For additional information on exporting reports, please go to [the Export Reports](#export-reports) section in this unit of the User Guide.

The New Rx Only Summary Report fields are described in the table below.

> <span id="_bookmark109" class="anchor"></span>Table 5: New Rx Only Summary Report Columns

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VISN</td>
<td><blockquote>
<p>Pharmacy VISN number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA Station ID</td>
<td><blockquote>
<p>VistA pharmacy identification number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NCPDP ID</td>
<td><blockquote>
<p>National Council for Prescription Drug Programs (NCPDP) identification number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Pharmacy Name</td>
<td><blockquote>
<p>VistA pharmacy name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Address</td>
<td><blockquote>
<p>Pharmacy Address</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#New Rx</td>
<td><blockquote>
<p>Number of New eRxs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Pharmacy Disabled</td>
<td><blockquote>
<p>Number of Pharmacy Disabled errors</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Rejected at Hub</td>
<td><blockquote>
<p>Number of eRxs rejected at the Processing Hub</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Passed Auto check</td>
<td><blockquote>
<p>Number of eRxs that passed auto check criteria</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Failed Auto check</td>
<td><blockquote>
<p>Sum of eRxs that failed Patient, Provider, and Drug Auto checks</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Rejected by Pharmacy</td>
<td><blockquote>
<p>Number of eRxs rejected by the pharmacy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Rx Filled</td>
<td><blockquote>
<p>Number of RxFill messages received by the Processing Hub from VistA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Accepted by Pharmacy</td>
<td><blockquote>
<p>Number of eRxs that have been accepted by the Pharmacy into VistA Pending/Outpatient</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Auto Check Details Report

The Auto Check Details Report provides details of the auto-checks performed by the hub side. To run an Auto Check Details Report:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/077.png)From the Reports screen, select Auto Check Details Report from the “Select Report” drop down.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/078.png)

<span id="_Toc104287544" class="anchor"></span>Figure 2-47: Auto Check Details Report Drop Down Selection

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/079.png)Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/080.png)To narrow the search by VA Station ID, select the Station ID for the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/081.png)Select the date range from the Calendar drop down for the report or enter a date using the MM/DD/YYYY format.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/082.png)Select the Run Report button to generate the report.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/083.png)The Auto Check Details Report displays.

<span id="_bookmark112" class="anchor"></span>Figure 2-48: Auto Check Details Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

Reports can be viewed in the Web Application or they can be exported. For additional information on exporting reports, please go to the [Export Reports](#export-reports) section in this unit of the User Guide.

The Auto Check Details Report fields are described in the table below.

> <span id="_bookmark113" class="anchor"></span>Table 6: Auto Check Details Report Columns

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VISN</td>
<td><blockquote>
<p>Pharmacy VISN number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA Station ID</td>
<td><blockquote>
<p>VistA pharmacy identification number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NCPDP ID</td>
<td><blockquote>
<p>National Council for Prescription Drug Programs (NCPDP) identification number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Pharmacy Name</td>
<td><blockquote>
<p>VistA pharmacy name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#New Rx</td>
<td><blockquote>
<p>Number of New eRxs</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Passed Auto check</td>
<td><blockquote>
<p>Number of eRxs that passed auto check criteria</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#Failed Auto check</td>
<td><blockquote>
<p>Sum of eRxs that failed Patient, Provider, and Drug Auto checks</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#MVI Patient Found</td>
<td><blockquote>
<p>Number of eRxs in which the MVI Patient Found auto check passed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#MVI Patient Not Found</td>
<td><blockquote>
<p>Number of eRxs in which the MVI Patient was Not Found, therefore auto check failed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#E&amp;E Enrolled/Eligible</td>
<td><blockquote>
<p>Number of eRxs in which E&amp;E Enrolled/Eligible auto check passed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#E&amp;E Not Enrolled/Eligible</td>
<td><blockquote>
<p>Number of eRxs in which the Patient was Not E&amp;E Enrolled/Eligible, therefore auto check failed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Patient Not Enrolled at Site</td>
<td><blockquote>
<p>Number of eRxs in which the Patient was Not Enrolled at the Site, therefore auto check failed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Drug Match Found</td>
<td><blockquote>
<p>Number of eRxs in which a Drug Match was Found, therefore auto check passed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Drug Match Failed</td>
<td><blockquote>
<p>Number of eRxs in which the Drug Match Failed, therefore auto check failed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Provider Match Found</td>
<td><blockquote>
<p>Number of eRxs in which a Provider Match was Found, therefore auto check passed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Provider Match Failed</td>
<td><blockquote>
<p>Number of eRxs in which the Provider Match Failed, therefore auto check failed</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Reject Reasons Report

The Reject Reasons Report provides details of eRx Rejections. To run a Reject Reasons Report:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/084.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/085.png)From the Reports screen, select Reject Reasons Report from the “Select Report” drop down.

<span id="_bookmark115" class="anchor"></span>Figure 2-49: Reject Reasons Report Drop Down Selection

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/086.png)Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/087.png)To narrow the search by VA Station ID, select the Station ID for the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/088.png)Select the date range from the Calendar drop down for the report or enter a date using the MM/DD/YYYY format.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/089.png)Select the Run Report button to generate the report.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/090.png)The Reject Reasons Report displays.

<span id="_bookmark116" class="anchor"></span>Figure 2-50: Reject Reasons Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

Reports can be viewed in the Web Application or they can be exported. For additional information on exporting reports, please go to the [Export Reports](#export-reports) section in this unit of the User Guide.

The Reject Reason Report fields are described in the table below.

> <span id="_bookmark117" class="anchor"></span>Table 7: Reject Reason Report Columns

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VISN</td>
<td><blockquote>
<p>Pharmacy VISN number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA Station ID</td>
<td><blockquote>
<p>VistA pharmacy identification number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NCPDP ID</td>
<td><blockquote>
<p>National Council for Prescription Drug Programs (NCPDP) identification number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Pharmacy Name</td>
<td><blockquote>
<p>VistA pharmacy name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#New Rx</td>
<td><blockquote>
<p>Number of New eRxs</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Accepted by Pharmacy</td>
<td><blockquote>
<p>Number of Inbound messages – (minus) number of failures and rejections – (minus) number filled</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Rejected by Pharmacy</td>
<td><blockquote>
<p>Number eRxs rejected by the pharmacy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Patient Not Eligible</td>
<td><blockquote>
<p>Number of Patient Not Eligible rejections</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Cannot Resolve Patient</td>
<td><blockquote>
<p>Number of Cannot Resolve Patient rejections</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Provider Not Eligible</td>
<td><blockquote>
<p>Number of Provider Not Eligible rejections</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Cannot Resolve Provider</td>
<td><blockquote>
<p>Number of Cannot Resolve Provider rejections</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Not Eligible for Refills</td>
<td><blockquote>
<p>Number of Drug Not Eligible for Refills rejections</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#Non Formulary</td>
<td><blockquote>
<p>Number of Non Formulary rejections</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Duplicate Rx</td>
<td><blockquote>
<p>Number of rejections due to duplicate Rx</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Invalid Qty</td>
<td><blockquote>
<p>Number of rejections due to an Invalid Quantity entered</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Duplicate Therapy Class</td>
<td><blockquote>
<p>Number of rejections due to Duplicate Therapy Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#CS Not Allowed</td>
<td><blockquote>
<p>Number of rejections due to CS Not Allowed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Contact Pharmacy (ERR01)</td>
<td><blockquote>
<p>Multiple errors, please contact the pharmacy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#Incorrect Pharmacy</td>
<td><blockquote>
<p>Number of rejections due to Incorrect Pharmacy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>#Contact Pharmacy (ERR03)</td>
<td><blockquote>
<p>Incorrect Pharmacy</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### eRx Summary Report

The eRx Summary Report provides a summary of eRx auto-validation checks. To run an eRx Summary Report:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/091.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/092.png)From the Reports screen, select eRx Summary Report from the “Select Report” drop down.

<span id="_bookmark119" class="anchor"></span>Figure 2-51: eRx Summary Report Drop Down Selection

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/093.png)Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/094.png)To narrow the search by VA Station ID, select the Station ID for the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/095.png)Select the date range from the Calendar drop down for the report or enter a date using the MM/DD/YYYY format.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/096.png)Select the Run Report button to generate the report.

The eRx Summary Report displays.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/097.png)

<span id="_Toc104287549" class="anchor"></span>Figure 2-52: eRx Summary Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

Reports can be viewed in the Web Application or they can be exported. For additional information on exporting reports, please go to the [Export Reports](#export-reports) section in this unit of the User Guide.

The eRx Summary Report fields are described in the table below.

> <span id="_bookmark121" class="anchor"></span>Table 8: eRx Summary Report Columns

| Field            | Description                                                               |
|----------------------|-------------------------------------------------------------------------------|
| VISN                 | Pharmacy VISN number                                                          |
| VA Station ID        | VistA pharmacy identification number                                          |
| NCPDP ID             | National Council for Prescription Drug Programs (NCPDP) identification number |
| Pharmacy Name        | VistA pharmacy name                                                           |
| \#New Rx             | Number of New eRxs                                                            |
| \#Refill Request     | Number of refill requests                                                     |
| \#Refill Response    | Number of refill responses                                                    |
| \#Rx Change Request  | Number of changed Rx requests                                                 |
| \#Rx Change Response | Number of changed Rx responses                                                |
| \#Rx Cancel Request  | Number of cancelled Rx requests                                               |
| \#Cancel Rx Response | Number of cancelled Rx responses                                              |
| \#RxFill             | Number of RxFill messages received by the Processing Hub from VistA           |

### Export Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Reports tab, users may export a report to a .CSV format. To Export a report:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/098.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/099.png)Select the Export button.

<span id="_bookmark123" class="anchor"></span>Figure 2-53: Export Report buttons

A prompt displays asking to Open or Save the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/100.png)Select Open to view the report.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/101.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/102.png)To save the report, select Save. The system displays a Save As dialog. Navigate to a location on your system to save the file.

<span id="_bookmark124" class="anchor"></span>Figure 2-54: Summary Report Export Prompt (after clicking Export button)

### User Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The User Management screen allows Administrators to add new users to one or more sites (Station ID), enable users, disable users, modify user roles and existing user records by assigning them to one or more sites. This screen will only display for users with Administrator access.

The User Management screen currently displays the list of all users that are added to this system along with their roles and privileges. Please note the user list is currently sorted by First Name.

#### Add New User

> System Administrators have the ability to add new users from the User Management screen. To add a new user:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/103.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/104.png)Enter the new user’s User ID, First Name, and Last Name.

<span id="_bookmark127" class="anchor"></span>Figure 2-55: Add User - User ID, First Name, Last Name

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/105.png)Select the new user’s role(s). Multiple roles may be selected by holding \<Ctrl\> while selecting more than one role.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/106.png)

<span id="_bookmark128" class="anchor"></span>Figure 2-56: Add User - Select User Roles

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/107.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/108.png)Select the Station ID(s) for the user to have access to. Use the drop down menu to display the Station ID selection.

<span id="_bookmark129" class="anchor"></span>Figure 2-57: Add User – Select Station ID

4.  Select the Add button to add the selected Station ID to the “Selected Station IDs” box. To remove Station IDs from the “Selected Station IDs” box, select the Remove button.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/109.png)

<span id="_bookmark130" class="anchor"></span>Figure 2-58: Add User – Add and Remove Station ID

When a user is assigned to a Station ID, they are only able to see other users and information within that Station ID. For example, in the User Management table they will only see users also assigned to that Station ID and under Pharmacy Management, they will only see information for pharmacies within that Station ID.

If “All” is selected from the “Station ID” field and added to the “Selected Station IDs” box, the user will have access to all Station IDs. Additional Station ID values cannot be added if “All” has been selected. If a user attempts to add additional values an error message will display.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/110.png)

<span id="_bookmark131" class="anchor"></span>Figure 2-59: All Selection Error Message

5.  Select Save to add the new user to the users list. To cancel adding a new user, select Cancel.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/111.png)

<span id="_Toc104287557" class="anchor"></span>Figure 2-60: Add User - Save and Cancel

<span id="_bookmark132" class="anchor"></span>

#### Modify User Roles

System Administrators have the ability to modify user roles from the User Management screen. User roles include:

- Pharmacy Manager
- PBM Admin
- Pharmacy User
- Administrator

For further information on user roles and capabilities, please refer to the [Roles and Capabilities](#roles-and-capabilities) section of this guide.

To modify user roles:

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/112.png)![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/113.png)From the users list, locate the user and select the checkbox(es) for the desired user role(s).

<span id="_bookmark134" class="anchor"></span>Figure 2-61: Select User Roles

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/114.png)Select Save at the bottom of the screen.

A message displays indicating that the user was updated successfully. The Administrator may also select Cancel to cancel modifying user roles.

#### Enable/Disable Users

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/115.png)Users can be disabled and/or re-enabled to use the web application. To update a user’s access to the application, locate the user in the User Management table and select the checkmark in the Enable/Disable column. Select Save from the bottom of the screen to update the user’s access.

<span id="_bookmark136" class="anchor"></span>Figure 2-62: User Management Table – Enable/Disable User

When a user is disabled, their information is greyed in the User Management table. To modify the user’s access again, select the checkbox in the Enable/Disable column again.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/116.png)

Figure 2-63: User Disabled

If a user that has been disabled attempts to log in to the application, they will receive an error message.

> ![](pharmacy-reengineering-pre-inbound-eprescribing-iep-3-1-version-3-0-user-manual-/117.png)

<span id="_bookmark138" class="anchor"></span>Figure 2-64: User Disabled Error Message