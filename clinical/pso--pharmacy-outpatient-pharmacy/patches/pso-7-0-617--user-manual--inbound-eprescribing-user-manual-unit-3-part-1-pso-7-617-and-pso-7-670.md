---
title: Inbound ePrescribing User Manual (Unit 3 Part 1) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 3 Part 1) PSO*7*617 and PSO*7*670
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
description: - Inbound eR<sub>X</sub> VistA Holding Queue - Inbound eR<sub>X</sub> VistA Outpatient Profile - Complete Orders from Order Entry/Results Reporting (OERR) and Patient Prescription Processing
audience: 
keywords: 
  - span
  - patient
  - inbound
  - view
  - figure
  - class
  - queue
  - holding
  - unit
  - message
page_count: 0
word_count: 6575
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_31.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_31.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/001.png)

November 2021

Version 5.0 (Unit 3 Part 1)

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
<td><p>PSO*7*617:</p>
<ul>
<li><p>Updated all screen captures with the latest versions</p></li>
<li><p>Included changes related to Controlled Substance and Controlled Substance eRx processing</p></li>
<li><p>Added <a href="#jump-to-erx">Jump to eRx</a> and <a href="#view-audit-log">View Audit Log</a> sections</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>10/20/2020</td>
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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in Appendix B: Holding Queue Status Codes &amp; Descriptions.</p>
<ul>
<li><p>eR<sub>X</sub> Default Loopback Days</p></li>
<li><p>Replaced column label “LAST USER” with “LOCKED BY” and updated the description under Table 9</p></li>
<li><p>Added the information for LOCKED BY column in section 3.5.2 Patient Centric View</p></li>
<li><p>Replaced Figure 3-14, Figure 3-16, Figure 3-17, Figure 3-18, Figure 3-19, Figure 3-42, Figure 3-52,<br />
Figure 3-55, Figure 3-56, Figure 3-57, Figure 3-59, Figure 3-60, Figure 3-61, and Figure 3-68 for updated layout</p></li>
<li><p>Added Note and included Figure 3‑50 to indicate to the user that a Provider’s DEA# has expired in section 3.6.2.3 Edit Provider</p></li>
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

[Table 1: Patient Centric View [20](#_Ref5967146)](#_Ref5967146)

# Inbound eR<sub>X</sub> VistA Outpatient Pharmacy


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#inbound-ersubxsub-vista-outpatient-pharmacy)
  - [Introduction](#introduction)
  - [Purpose of Inbound eR<sub>X</sub> VistA Holding Queue](#purpose-of-inbound-ersubxsub-vista-holding-queue)
  - [NCPDP 2017071 Messages in the Holding Queue](#ncpdp-2017071-messages-in-the-holding-queue)
    - [NewRx Message](#newrx-message)
    - [RxRenewal Request Message](#rxrenewal-request-message)
    - [RxRenewal Response Message](#rxrenewal-response-message)
    - [RxChange Request Message](#rxchange-request-message)
    - [RxChange Response Message](#rxchange-response-message)
    - [CancelRx Request Message](#cancelrx-request-message)
    - [CancelRx Response Message](#cancelrx-response-message)
    - [Inbound Error Message](#inbound-error-message)
    - [Inbound vs. Outbound Messages](#inbound-vs-outbound-messages)
  - [Accessing the eR<sub>X</sub> Holding Queue](#accessing-the-ersubxsub-holding-queue)
  - [Traditional View vs. Patient Centric View](#traditional-view-vs-patient-centric-view)
    - [Traditional View](#traditional-view)
    - [Patient Centric View](#patient-centric-view)
    - [eR<sub>X</sub> Holding Queue Summary/Details Screen NewRx Message](#ersubxsub-holding-queue-summarydetails-screen-newrx-message)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound eR<sub>X</sub> VistA Outpatient Pharmacy is comprised of two sections:

- Inbound eR<sub>X</sub> VistA Holding Queue
- Inbound eR<sub>X</sub> VistA Outpatient Profile - Complete Orders from Order Entry/Results Reporting (OERR) and Patient Prescription Processing

## Purpose of Inbound eR<sub>X</sub> VistA Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eR<sub>X</sub> Holding Queue allows for validation and review of eR<sub>X</sub>es by VA Pharmacy users prior to the eR<sub>X</sub> being added to the VA record and merging with the existing outpatient functionality. For the fillable prescriptions, VA Pharmacy users can validate patient, provider, and drug/SIG information. Additionally, users can accept, hold, un hold, print, reject, or remove an eR<sub>X</sub> from the Holding Queue after it has been received by VistA from the eR<sub>X</sub> Processing Hub. The users can also work with RxRenewal Responses, RxChange Responses and CancelRx Requests, which are described.

> **NOTE:** Controlled Substance records that meet the requirements of the Drug Enforcement Administration’s electronic prescribing for Controlled Substance rules will have a visual indicator stating “EPCS DEA Valid” at the top right corner in the VistA Holding Queue.

## NCPDP 2017071 Messages in the Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message types in the Holding Queue include:

- <u>NewRx Message</u>
- <u>RxRenewal Request Message</u>
- <u>RxRenewal Response Message</u>
- <u>RxChange Request Message</u>
- <u>RxChange Response Message</u>
- <u>CancelRx Request Message</u>
- <u>CancelRx Response Message</u>
- <u>Inbound Error Message</u>

### NewRx Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NewRx message is the NCPDP 2017071 format for New Electronic Prescription sent by an external (non-VA) provider.

### RxRenewal Request Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RxRenewal Request message is the NCPDP 2017071 format for RxRenewal Request sent by a VA Pharmacy for electronic Prescriptions.

### RxRenewal Response Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RxRenewal Response message is the NCPDP 2017071 format for RxRenewal Response sent by an External Provider for RxRenewal Request sent by a VA Pharmacy.

### RxChange Request Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RxChange Request message is the NCPDP 2017071 format for RxChange Request sent by a VA Pharmacy for electronic Prescriptions.

### RxChange Response Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RxChange Response message is the NCPDP 2017071 format for RxChange Response sent by an External Provider for RxChange Request sent by a VA Pharmacy.

### CancelRx Request Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CancelRx Request message is the NCPDP 2017071 format for CancelRx Request sent by External Provider on Electronic Prescriptions.

### CancelRx Response Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CancelRx Response message is the NCPDP 2017071 format for CancelRx Response sent by VA Pharmacy for a CancelRx Request sent by External Provider.

### Inbound Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ERROR messages are in the NCPDP 2017071 format for Inbound Error message received in VistA under situations such as, the Prescriber’s EHR system being unable to receive and process a certain transaction sent from the Pharmacy or a connection between the Transaction Hub and CH is not working.

### Inbound vs. Outbound Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound messages are those that are sent by the external (non-VA) Providers and are received in the Holding Queue. NewRx, RxRenewal Response, RxChange Response, CancelRx Request, and Inbound Error are Inbound messages.

Outbound messages are those that are sent by VA pharmacies to the external Provider’s EHR system. RxRenewal Request, RxChange Request, and CancelRx Response are Outbound messages.

## Accessing the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The inbound eR<sub>X</sub> message is transmitted from the Processing Hub to VistA and stored in the eR<sub>X</sub> Holding Queue.

## Traditional View vs. Patient Centric View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Traditional View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Traditional View of the eR<sub>X</sub> Holding Queue:

1.  Follow this navigation path: Core Applications \> Outpatient Pharmacy Manager \> (select Division) \> RX (Prescriptions) ... \> Complete Orders from eR<sub>X</sub> \[PSO ERX FINISH\]

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc83909373" class="anchor"></span>Figure 3‑1: Complete Orders from eR<sub>X</sub> Menu Option

2.  To enter eRx Holding Queue, you must select the type of records you want to see on the Holding Queue. The options are Non-CS for Non-Contrlled Substance, CS for Controlled Substance and B for Both. For our example we will select B.

    <span id="_Toc83909374" class="anchor"></span>![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/003.png)Figure 3‑2: Controlled Substance Selection
3.  This next filter is displayed if you selected CS or B above. It allows you to select specific CS drug schedule of the records you want to see in the Holding Queue. For this example we are electing Schedules II-V which basically includes all CS drug schedules.

    ![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc83909375" class="anchor"></span>Figure 3‑3: Drug Schedule Selection

4.  Select RX Prescription Received Date.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc83909376" class="anchor"></span>Figure 3‑4: Select RX

The first screen that displays upon accessing the eR<sub>X</sub> Holding Queue is the Holding Queue list view screen. Controlled Substance records will be indicated with a square bracket “\]” symbol. Records without a “\]” are for Non-Controlled Substance medications.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc83909377" class="anchor"></span>Figure 3‑5: eR<sub>X</sub> Holding Queue List View

#### eR<sub>X</sub> Holding Queue List View

The eR<sub>X</sub> Holding Queue List columns include the patient’s name (Patient), date of birth of the patient (DOB), the prescribed drug from the external provider (Drug), the prescribing physician’s name (Provider), the status of the eR<sub>X</sub> (STA), and the date that the eR<sub>X</sub> was received by VistA (Rec Date). At any given time, 999 eR<sub>X</sub> records are displayed in the Holding Queue List View with actionable statuses of “N”, “I”, “W”, or with one of the Hold codes (H*xx* (where *x* = letter), HC), CAH, CAO, CAP, CAR, CXD, CXE, CXI, CXN, CXV, CXW, CXY, RXD, RXE, RXF, RXI, RXN, RXR, RXW, or the Inbound Error in RRE and CRE status. The records are sorted by Received Date with oldest records first. Refer to <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in User Manual Unit 6 (PSO_7_0_P617_UM_6) available on the Veteran's Documentation Library (VDL) for additional information on the various statuses in the list.

The following actions are available from the eR<sub>X</sub> Holding Queue List:

- \<SI\> Select Item can be entered to select an item in the Enter a Number prompt. Additionally, the record \# can be entered without selecting SI at the “Select Action: Next Screen//” prompt.
- \<SR\> Search Queue can be entered to search for an eR<sub>X</sub> based on a variety of search criteria.
- \<SO\> Sort Entries can be entered to sort the list.
- \<MV\> Message View can be entered to display various message types.

#### Message Viewb

Message View, \<MV\>, is an action in the Holding Queue. When the user enters \<MV\>, the system prompts the user to select the message type. By selecting the message type, the user can view all the messages in the various statuses for the selected message type in the order of date received, with the newest records displayed first. Records containing a Controlled Substance will be indicated with a bracket “\]” symbol. Records without a “\]” are Non-Controlled Subsatnce.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc83909378" class="anchor"></span>Figure 3‑6: Message View

#### Actionable and Non-Actionable eR<sub>X</sub> Records

There are two types of Inbound eR<sub>X</sub> records: Actionable records and Non-Actionable records.

Actionable Records are those that are displayed in the eRX Holding Queue List View. Actionable records include:

- NewRx (status in New, In Process, Hold, and Wait)
- CancelRx Request
- RxRenewal Response (Denied, Denied NewRx to Follow, RxRenewal Response Failed)
- RxRenewal Response – Approved with Changes (when there is a change to the provider data)
- RxRenewal Response – Replace (in statuses of new, in process, hold, wait or error)
- Inbound Errors related to RxRenewal Requests
- RxChange Response (Denied for all request types)
- RxChange Response (Approved for Prior Authorization Required request type)
- RxChange Response (Validated for Prescriber Authorization request type)
- RxChange Response (Approved and Approved with Changes for request types Generic Substitution, Therapeutic Interchange/Substitution, Drug Use Evaluation, Script Clarification and Out of Stock, and in statuses of new, in process, hold, wait, or error)
- Inbound Errors related to RxChange Requests

Non-Actionable records are those that are in the Holding Queue but are not displayed in the List View. All records acknowledged, removed, rejected, processed/completed, and auto-canceled are non-actionable. Non-Actionable records further include:

- RxRenewal Request
- RxRenewal Response – Approved
- RxRenewal Response – Approved with Changes (change to drug data only)
- RxChange Request
- CancelRx Response
- Inbound Errors related to CancelRx Responses

For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in [Unit 6](#User_Manual_6).

#### eR<sub>X</sub> Default Lookback Days

A new field, ERX DEFAULT LOOKBACK DAYS file (#10.2), has been added to the OUTPATIENT SITE file (#59), which contains the number of days the user would like to look back before loading the Holding Queue’s list view or completing a Search (SR) or Sort (SO). This is a configurable field that can be updated with the desired value by the local site’s VistA Admin. The addition of this new configurable field facilitates increased processing speed in the eR<sub>X</sub> Holding Queue.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc519780526" class="anchor"></span>Figure 3‑7: eR<sub>X</sub> Default Lookback Days

- The number of eR<sub>X</sub> records displayed in the Holding Queue’s list view is based on the ERX DEFAULT LOOKBACK DAYS file (#10.2) configured in OUTPATIENT SITE file (#59).
- By default, the ERX DEFAULT LOOKBACK DAYS field is blank, so the software goes back to 365 days.
- ERX LOOK-BACK DAYS label along with the value and date stamp are displayed both in the Traditional View and the Patient Centric View of the eR<sub>X</sub> Holding Queue, in the Header section.
- If the Pharmacy user would like to see eR<sub>X</sub> records received from older dates, the user can use the Search (SR) option and select the ‘Received Date Range’ (#3), to retrieve those records.

> **NOTE:** Refer to the Implementation Guide – Inbound ePrescribing (PSO\*7.0\*p581) on the VA Documentation Library (VDL) for details on configuring the ERX DEFAULT LOOKBACK DAYS for a site.

### Patient Centric View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Centric View allows users to view eR<sub>X</sub>es grouped by patient. This view makes it easier to view the eR<sub>X</sub> records in the Holding Queue when there is a high volume of records. Patient Centric View displays the actionable eR<sub>X</sub> records only per patient. It allows the user to easily identify the message types that are in outstanding or actionable statuses, such as, N, I, W, H*xx* (where *x* = letter), HC, CAH, CAO, CAP, CAR, CXD, CXE, CXI, CXN, CXV, CXW, CXY, RXD, RXE, RXF, RXI, RXN, RXR, RXW, or the Inbound Error in RRE and CRE status. It also displays the last user information, which identifies which actionable eR<sub>X</sub> records have been worked on and/or whom to contact when there is a problem with one or more records.

Once the user selects a patient from the Patient Centric View, the prescription view displays, with only the actionable eR<sub>X</sub> records for the selected patient.

To access Patient Centric View:

1.  Enter \<PT\>.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc520302017" class="anchor"></span>Figure 3‑8: PT – Patient (Grouped)

5.  Select an option to filter the Patient Centric View by specific actionable status.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc520302018" class="anchor"></span>Figure 3‑9: Patient Centric View Filters – Select by Status

While accessing the Patient Centric View, one of the following selections may be made to filter the display results by specific actionable statuses:

- \<A\> All – Patients with eR<sub>X</sub> records in all actionable statuses in the Holding Queue.
- \<1\> New – Patients with eR<sub>X</sub> records in New status in the Holding Queue. (NewRx only)
- \<2\> In Process – Patients with eR<sub>X</sub> records in In Process status in the Holding Queue.
- \<3\> Wait – Patients with eR<sub>X</sub> records in Wait status in the Holding Queue.
- \<4\> Hold – Patients with eR<sub>X</sub> records in one of the Hold statuses in the Holding Queue.
  - If \<4\> Hold is entered, \<S\> must then be selected for a single Hold status or \<A\> for all hold codes.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc520302019" class="anchor"></span>Figure 3‑10: Patient Centric View Filters – Hold

If \<S\> is entered to filter the display results by a single Hold status, the desired Hold status to filter by must be selected.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc520302020" class="anchor"></span>Figure 3‑11: Patient Centric View – Hold Statuses

For additional details on Hold statuses, refer to <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in [Unit 6](#User_Manual_6).

> **NOTE:** The Hold status codes of the format H*xx* apply to all fillable prescriptions. However, HC applies to NewRx type only.

- \<5\> CCR – Patients with CancelRx Request and/or actionable RxRenewal Response and/or RxChange Response in the Holding Queue.
  - If \<5\> CCR is entered, \<S\> must be selected to filter for a single CCR status, or \<A\> for all actionable CCR statuses.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc83909384" class="anchor"></span>Figure 3‑12: Patient Centric View Filter – CCR

If \<S\> is entered to filter the display results by a single CCR status, they must then select the desired CCR status to filter by.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc83909385" class="anchor"></span>Figure 3‑13: Patient Centric View – CCR Statuses

Once a selection is made:

- If the site has not configured ERX DEFAULT LOOKBACK DAYS, a list of patients who have Actionable eR<sub>X</sub> records in the Holding Queue for the last 365 days displays. See Figure 3‑12.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/015.png)

<span id="PSO_7_567_Fig_3_12" class="anchor"></span>Figure 3‑14: Non-Configured ERX LOOK-BACK DAYS Field

- If options \<1\>, \<2\>, \<3\>, or \<4\> are selected to filter by status, a list of patients displays if the patient has Actionable eR<sub>X</sub> records under the selected status within the number of days set as the ERX DEFAULT LOOKBACK DAYS. For example, if the ERX DEFAULT LOOKBACK DAYS is set to a value of 30 and a user selected \<1\> New when filtering the Patient Centric View, the patient(s) displayed should have had a new record received within the last 30 days. See Figure 3‑13.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/016.png)

<span id="PSO_7_567_Fig_3_13" class="anchor"></span>Figure 3‑15: Configured ERX LOOK-BACK DAYS Field

The table below describes the columns visible in the Patient Centric View.

<span id="_Ref5967146" class="anchor"></span>Table 1: Patient Centric View

| Column Label | Description                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERX PATIENT  | Name of the patient sent on the New prescription                                                                                                                                                 |
| DOB          | eR<sub>X</sub> patient’s date of birth                                                                                                                                                           |
| ED           | The number of days elapsed since the oldest eR<sub>X</sub> that is still in an actionable status was received for that patient                                                                   |
| LOCKED BY    | Name of the current user that applied lock on the patient record successfully                                                                                                                    |
| NW           | Number of NewRxes                                                                                                                                                                                |
| WT           | Number of eR<sub>X</sub>es in WAIT status. WAIT status displays if all validations have been performed, but the eR<sub>X</sub> has not been Accepted (AC) (Includes all fillable prescriptions). |
| IP           | Number of eR<sub>X</sub>es In Process (includes all fillable prescriptions)                                                                                                                      |
| HD           | Number of eR<sub>X</sub>es on Hold (includes all fillable prescriptions)                                                                                                                         |
| CCR          | CancelRx Request, RxChange Response, and RxRenewal Response records in actionable statuses; (also, includes RXF,RXE and CXE records)                                                             |
| OTH          | Inbound Error related to RxRenewal/RxChange Request (Status – RRE/CRE)                                                                                                                           |
| TOT          | Total number of eR<sub>X</sub>es in actionable statuses                                                                                                                                          |

This table displays the Patient Centric View Column label descriptions.

- If an eR<sub>X</sub> patient does not have user name displayed in the LOCKED BY column, this means that the patient’s eR<sub>X</sub> record is available to the user.
- Under columns NW, IP, HD, WT, CCR, and OTH the maximum count displayed is 99, even if the patient has more actionable eR<sub>X</sub> records, which the TOT (Total) column would indicate.
- Under the TOT column, the maximum count displayed is 999, even if the patient has more than 999 items in actionable status.
- Patient Centric View displays up to 999 records.
- Patient Centric View records are sorted by Elapsed Days, in descending order.

To select a patient to view the eR<sub>X</sub>es associated with them, select the patient record number. A list of actionable eR<sub>X</sub> records displays.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/017.png)

<span id="_Ref5967400" class="anchor"></span>Figure 3‑16: Patient eR<sub>X</sub> List

To view the details of an eR<sub>X</sub>, select the record number.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc520302023" class="anchor"></span>Figure 3‑17: eR<sub>X</sub> Summary/Details Screen

Validation actions may be completed from here. If validation actions are started on NewRx message types, but not Accepted, the Status of the eR<sub>X</sub> displays as “I” for In Process. In the example below, just the patient was validated, therefore the eR<sub>X</sub> is still In Process.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/019.png)

<span id="_Ref5967413" class="anchor"></span>Figure 3‑18: eR<sub>X</sub> List with Updated Status – I

In the Patient Centric View, if an eR<sub>X</sub> status changes one actionable status to another, the eR<sub>X</sub> total remains the same, but the totals for various statuses are updated. In the example below, the second record displays 17 NewRxes and 3 eR<sub>X</sub>es that are In Process, and a total of 35 eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/020.png)

<span id="_Ref5967421" class="anchor"></span>Figure 3‑19: Patient Centric View

If an eR<sub>X</sub> status changes from New to In Process, the numbers for the various statuses are updated while the eR<sub>X</sub> total remains the same, as seen in the second record in the example below. There are now 16 NewRxes, 4 eR<sub>X</sub>es In Process, and still a total of 35 eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/021.png)

<span id="_Ref5967490" class="anchor"></span>Figure 3‑20: Patient Centric View – Updated Actionable Status to another Actionable Status

In the Patient Centric View, if an eR<sub>X</sub> status changes an actionable Status to a non-actionable status, the eR<sub>X</sub> total decreases by one and the totals for various statuses are also updated. In the example below, the record in the second row, the WT column has updated from 1 eR<sub>X</sub>es to 0 eR<sub>X</sub>es, therefore updating the total column from 35 to 34.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/022.png)

<span id="_Ref5967502" class="anchor"></span>Figure 3‑21: Patient Centric View Total Updated

### eR<sub>X</sub> Holding Queue Summary/Details Screen NewRx Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A record from the eR<sub>X</sub> Holding Queue List View can be selected by both typing \<SI\> and the record number or by typing the record number itself. The first screen displayed is the Summary/Details screen, which displays information about the original eR<sub>X</sub> from the external provider and matched VistA information (if any).

On this screen, the header contains the eR<sub>X</sub> Patient Name and eR<sub>X</sub> Reference \#, which is an internal VA reference number assigned for tracking the eR<sub>X</sub>. Below the header is information received from the external provider for the patient, provider, and the drug/SIG. Where applicable, VistA information displays below the eR<sub>X</sub> information.

> **NOTE:** - “eRx Written Date” – Date the eR<sub>X</sub> was received in the VistA Holding Queue.

- “eRx Issue Date” – Effective Date, if sent by the provider.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc520302028" class="anchor"></span>Figure 3‑22: Summary/Details Screen Page 1

Press \<Enter\> to display Page 2 of the Summary/Details screen, which contains eR<sub>X</sub> Notes, applicable Allergy information, and Diagnosis information.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc520302029" class="anchor"></span>Figure 3‑23: Summary/Details Screen Page 2

If the VistA information for the patient, provider, or drug is not linked, the display is as shown below:

- VistA Patient: NOT LINKED
- VistA Provider: NOT LINKED
- VistA Drug: NOT LINKED

VistA information displayed includes allergies. If the patient has no known allergies, “NKA” displays in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc520302030" class="anchor"></span>Figure 3‑24: Patient with No Known Allergies

If the VistA patient has known allergies, verified allergies display in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc520302031" class="anchor"></span>Figure 3‑25: VistA Patient with Known Allergies

#### eR<sub>X</sub> Actions

- Manual Validation:
  - \<VP\> [Validate Patient](#_Validate_Patient)
  - \<VM\> [Validate Provider](#_Validate_Provider)
  - \<VD\> ([Validate Drug/SIG](#_Validate_Drug/SIG)) - Note that this action is not available unless a VistA patient has been linked, as indicated with parenthesis around the action.
- \<P\> Printing in the eR<sub>X</sub> Holding Queue displays all details of an eR<sub>X</sub> and allows the user to select a local printer and print the eR<sub>X.</sub>
- \<RJ\> Rejecting an eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes the eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>
- \<AC\> Accepting eR<sub>X</sub>es in the eRX Holding Queue action is not available until the validation of the eR<sub>X</sub> Patient, provider, and drug/SIG have been completed. Also note that the \<AC\> action is not available if the eR<sub>X</sub> is on Hold.
- \<H\> Places eR<sub>X</sub> on Hold in the eR<sub>X</sub> Holding Queue.
- \<UH\> UnHold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue.
- \<RM\> Removing the eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>
- \<??\> For hidden actions.

For more details on the above actions, refer to the sections identified in this guide.

> **NOTE:** From the Summary/Details screen, users <u>cannot</u> edit any of the VistA information. The validate screens contain the option for editing the VistA information. For further information on editing and validating VistA information for an eR<sub>X</sub>, refer to section <u>3.6 Manual Validation</u>.

#### Jump to OP

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR, from the eR<sub>X</sub> Holding Queue Summary/Details screen. Once the user has completed reviewing on the Outpatient side, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR only if the following conditions are true:

1.  The R<sub>X</sub> record is a fillable prescription only.
6.  The VistA Patient is already matched to an eR<sub>X</sub> Patient under the Validate Patient \<VP\> action.
7.  The matched VistA Patient has a current pending line entry on the Outpatient side.

To use the Jump to OP action, enter \<??\> to view a list of hidden actions.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc520302032" class="anchor"></span>Figure 3‑26: Jump to OP – Hidden Action

Enter the hidden Jump to OP \<JO\> action.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc520302033" class="anchor"></span>Figure 3‑27: JO Action Selected

If a user attempts to Jump to OP \<JO\> when a VistA Patient is not matched to an eR<sub>X</sub> Patient, an error message is received stating, “VistA patient has not been matched. Cannot jump to outpatient”.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc520302034" class="anchor"></span>Figure 3‑28: JO Error – VistA Patient Not Matched

If a user attempts to Jump to OP \<JO\> from an eR<sub>X</sub> record that is not a fillable prescription, an error message is received stating, “Jumping can only be done on ‘NewRx’ messages, Renewal Response-Replace and fillable RxChange Response messages”.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc520302035" class="anchor"></span>Figure 3‑29: JO Error – Fillable eR<sub>X</sub> Messages Only

Once the user has completed reviewing on the Outpatient side, upon selecting \<Enter\> at the “Select Patient:” prompt, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc83909402" class="anchor"></span>Figure 3‑30: JO “Select Patient” – Jump Back to Holding Queue eR<sub>X</sub> Summary/Details Screen

#### Jump to eRx 

The Jump to eRx \<JE\> hidden action allows the user to navigate to the VistA eRx Holding Queue display from the Pending Outpatient (OP) Orders display for a pending order or an eRx active prescription. Once the user has completed reviewing or editing in the VistA eRx Holding Queue, the user is navigated back to the pending order or active eRx prescription in the Pending OP Orders display which \<JE\> was initiated from.

To use the Jump to eRx action, enter \<??\> to view a list of hidden actions.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc83909403" class="anchor"></span>Figure 3‑31: Jump to eRx – Hidden Action

Enter the hidden Jump to eRx \<JE\> action.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc83909404" class="anchor"></span>Figure 3‑32: JE Action Selected

To return back to the pending order or active prescription in the Pending OP Orders display, type ‘^’. The Jump to OP \<JO\> hidden action is not available while utilizing the \<JE\> function and users will receive the following error message.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc83909405" class="anchor"></span>Figure 3‑33: JE Action JO Error Message

#### Status History

The Status History \<SH\> hidden action displays the history of status changes on an eR<sub>X</sub> record within the Holding Queue. It does not include the initial status of the record.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc83909406" class="anchor"></span>Figure 3‑34: Status History – Hidden Action

Enter the hidden Status History \<SH\> action to display the history of status changes.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc83909407" class="anchor"></span>Figure 3‑35: SH Action - Status Changes on eR<sub>X</sub> Record in Holding Queue

Comments are displayed where applicable (i.e. Hold, RJ, and RM statuses).

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/037.png)

<span id="_Toc83909408" class="anchor"></span>Figure 3‑36: Status History with Comment for Rejected eR<sub>X</sub>

#### eR<sub>X</sub> Change Request

eR<sub>X</sub> Change Request \<EC\> hidden action is used to request change on a NewRx prescription from the external Provider who sent the original NewRx. For detailed information about RxChange Request, refer to <u>Unit 5 – RxChange Requests and Responses</u> (PSO_7_0_P617_UM_51 and PSO_7_0_P617_UM52) available on the Veteran's Documentation Library (VDL).

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc83909409" class="anchor"></span>Figure 3‑37: eR<sub>X</sub> Change Request

#### View Audit Log

View Audit Log \<AU\> hidden action is used to view all edits made to a VistA Patient, Provider, and Drug/Sig. This feature will also capture any edits made by auto-matching and display them on the Audit Log.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/039.png)

<span id="_Toc83909410" class="anchor"></span>Figure 3‑38: eR<sub>X</sub> View Audit Log

Once the user selects View Audit Log \<AU\>, the Audit Log report will display.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/040.png)

<span id="_Toc83909411" class="anchor"></span>Figure 3‑39: eR<sub>X</sub> Audit Log

Users are able to sort the Audit Log by Date/Time \<DT\>, Field \<FN\>, Edited By \<EB\>, or Show/Hide eRx Value \<SH\>. All sort options contain a sort indicator to inform the user if the results are in ascending \[^\] or descending \[v\] order. To change the chronological order of the Audit Log display, enter the sort option a second time

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/041.png)

<span id="_Toc83909412" class="anchor"></span>Figure 3‑40: eR<sub>X</sub> Audit Log Sorted by Date/Time Ascending

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/042.png)

<span id="_Toc83909413" class="anchor"></span>Figure 3‑41: eR<sub>X</sub> Audit Log Sorted by Date/Time Descending

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc83909414" class="anchor"></span>Figure 3‑42: eR<sub>X</sub> Audit Log Sorted by Edited By Ascending

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc83909415" class="anchor"></span>Figure 3‑43: eR<sub>X</sub> Audit Log Sorted by Edited By Descending

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/045.png)

<span id="_Toc83909416" class="anchor"></span>Figure 3‑44: eR<sub>X</sub> Audit Log Sorted by Field Ascending

<span id="_Toc83909417" class="anchor"></span>![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/046.png)Figure 3‑45: eR<sub>X</sub> Audit Log Sorted by Field Descending

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/047.png)

<span id="_Toc83909418" class="anchor"></span>Figure 3‑46: eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Shown

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/048.png)

<span id="_Toc83909419" class="anchor"></span>Figure 3‑47: eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Hidden

To exit the Audit Log \<AU\> and return to the eRx Holding Queue Display, press ‘Enter’.

#### Patient-Level Record Lock

Note that when either the Summary/Details screen or any of the validate screens of an eR<sub>X</sub> are open, all the eR<sub>X</sub>es for that same patient in the Holding Queue are locked and inaccessible for other users to access until the lock is released (the screens are closed). This is referred to as a patient-level record lock.

The following message displays if a user attempts to access an eR<sub>X</sub> for the same patient that another user has opened.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/049.png)

<span id="_Toc83909420" class="anchor"></span>Figure 3‑48: Patient-Level Record Lock

#### Prohibit Renewals

The Prohibit Renewal Request flag is used to denote that a RxRenewal Request should not be sent to the sending prescriber for an original NewRx or a subsequent fillable RxChange Response when the flag is set on the original NewRx. This is usually used when the visit is for a one time prescription (i.e., Urgent Care Center or Emergency Department).

> **NOTE:** \(i\) The Prohibit Renewal Request information is not displayed for RxRenewal Request and Response records.

\(ii\) The Prohibit Renewal Request information is displayed both in VistA and on web GUI under Track/Audit details screen, whenever it is sent on the inbound NewRx record.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-617-and-pso-7-670/050.png)

<span id="_Toc83909421" class="anchor"></span>Figure 3‑49: Prohibit Renewal Request