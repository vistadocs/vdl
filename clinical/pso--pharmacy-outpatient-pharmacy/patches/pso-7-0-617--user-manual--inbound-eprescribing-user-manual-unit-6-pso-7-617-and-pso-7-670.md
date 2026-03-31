---
title: Inbound ePrescribing User Manual (Unit 6) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 6) PSO*7*617 and PSO*7*670
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
description: "--- title: | <span id=\\"_Hlk52202211\\" class=\\"anchor\\"></span>Pharmacy Reengineering (PRE)"
audience: 
keywords: 
  - cancelrx
  - request
  - span
  - holding
  - queue
  - status
  - response
  - class
  - table
  - manual
page_count: 0
word_count: 6377
section_count: 9
table_count: 15
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um__6.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um__6.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/001.png)

November 2021

Version 5.0 (Unit 6)

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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in Appendix B: Holding Queue Status Codes &amp; Descriptions.</p>
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

# CancelRx Requests and Responses


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CancelRx Requests and Responses](#cancelrx-requests-and-responses)
  - [CancelRx Request in the eR<sub>X</sub> Holding Queue](#cancelrx-request-in-the-ersubxsub-holding-queue)
  - [CancelRx Response in the eR<sub>X</sub> Holding Queue](#cancelrx-response-in-the-ersubxsub-holding-queue)
    - [Approved](#approved)
    - [Denied](#denied)
  - [CancelRx Request Message Details View](#cancelrx-request-message-details-view)
  - [CancelRx Response Message Details View](#cancelrx-response-message-details-view)
  - [CancelRx Process](#cancelrx-process)
    - [CancelRx Process - eR<sub>X</sub> Records in the Holding Queue](#cancelrx-process-ersubxsub-records-in-the-holding-queue)
    - [CancelRx Process - eR<sub>X</sub> Records in Outpatient Profile](#cancelrx-process-ersubxsub-records-in-outpatient-profile)
    - [CancelRx Request Failed (CAF)](#cancelrx-request-failed-caf)
    - [CancelRx Request Received (CAR)](#cancelrx-request-received-car)
  - [Inbound Error – CNE](#inbound-error-cne)
  - [Acknowledge: Hidden Action for CancelRx Request](#acknowledge-hidden-action-for-cancelrx-request)
    - [Acknowledge: Automated CancelRx Response Sent](#acknowledge-automated-cancelrx-response-sent)
    - [Acknowledge: No Automated CancelRx Response Sent](#acknowledge-no-automated-cancelrx-response-sent)
  - [Add Comments: Hidden Action for CancelRx Request/Response](#add-comments-hidden-action-for-cancelrx-requestresponse)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Holding Queue Status Codes & Descriptions](#holding-queue-status-codes-descriptions)
- [NCPDP Error Codes](#ncpdp-error-codes)
- [RxRenewal Request Preconditions and Warnings](#rxrenewal-request-preconditions-and-warnings)
The CancelRx Request is sent by the external/non-VA provider for a fillable eR<sub>X,</sub> so it is not processed and dispensed by VA Pharmacy. Upon successfully canceling a fillable eR<sub>X</sub> (or auto-Discontinue in Outpatient), VA Pharmacy sends back either an automated or manual CancelRx Response. When an automated CancelRx Response is sent to the provider’s EHR system, user intervention is not required. When a user must take action on the prescription for which a CancelRx Request has been received, the user may send a manual CancelRx Response.

## CancelRx Request in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CancelRx Request is received in the Holding Queue, it is displayed in the list view in one of the actionable statuses until it is acknowledged. Depending on the status of the fillable eR<sub>X</sub> on which the CancelRx Request has been received, the status of the request is changed according to the status of the fillable eR<sub>X</sub> prior to canceling or auto-Discontinuing. For a full list of CancelRx Request statuses, please refer to <u>Table 13: Holding Queue Status Codes & Descriptions for CancelRx Request Message Type</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

Once the request is acknowledged, it is no longer displayed in the list view. CancelRx Request messages may be retrieved at any point using \<MV\> Message View and/or \<SR\> Search.

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type CancelRx Request.

The CancelRx Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc83992590" class="anchor"></span>Figure ‑: CAO Status in Holding Queue

## CancelRx Response in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two types of CancelRx Responses:

- Approved
- Denied

### Approved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Approved CancelRx Response is sent back to the requesting non-VA provider when either the system or the user has been able to successfully cancel or auto-Discontinue the fillable eR<sub>X</sub>.

- In most cases, the system sends an automated Approved CancelRx Response to the requesting non-VA Provider.
- In certain cases, the system only cancels the fillable eR<sub>X</sub> in the Holding Queue and does not send an automated response. In these scenarios, the user can acknowledge the request and send a manual response.

### Denied

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Denied CancelRx Response is sent back to the requesting non-VA provider when either the system or the user has not been able to successfully cancel or auto-Discontinue the fillable eR<sub>X</sub>es.

- At this time, there is no automated Denied CancelRx Response sent from VA Pharmacies to the requesting non-VA Provider.
- When the user has not been able to locate and cancel/auto-Discontinue the fillable eR<sub>X</sub> or when the user has chosen not to cancel/auto-Discontinue the fillable eR<sub>X</sub>, the user may acknowledge the request and send a manual Denied response.

## CancelRx Request Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may select the CancelRx Request message from the Holding Queue to view the message details in the Message Details View.

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type CancelRx Request.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc83992591" class="anchor"></span>Figure ‑: Holding Queue List View

3.  Select the desired record from the list.

The CancelRx Request message details display.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc83992592" class="anchor"></span>Figure ‑: CancelRx Request Details

The user may continue to scroll through the CancelRx Request Details page to view CancelRx Request Information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc83992593" class="anchor"></span>Figure ‑: CancelRx Request Details – CancelRx Request Information

## CancelRx Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may select the CancelRx Response message from the Holding Queue to view the message details in the Message Details View.

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type CancelRx Response.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc83992594" class="anchor"></span>Figure ‑: Holding Queue List View - CancelRx Response

3.  Select the desired record from the list.

The CancelRx Response message details display.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/007.png)

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc83992595" class="anchor"></span>Figure ‑: CancelRx Response Details

## CancelRx Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CancelRx Process involves auto-Canceling a fillable eR<sub>X</sub> in the Holding Queue and auto-Discontinuing the record in the Outpatient Profile if it is already processed from the Holding Queue. In most cases, the system also sends an Approved CancelRx Response.

In some scenarios, the user must manually discontinue the prescription in the Outpatient Profile and then send a manual Approved CancelRx Response at the time of acknowledging the request.

If the user is unable to locate the fillable eR<sub>X</sub> and/or if the user is not going to cancel/discontinue the prescription, the user may send a manual Denied CancelRx Response.

If a manual Approved CancelRx Response, an automated Approved CancelRx Response, or a manual Denied CancelRx Response is sent successfully from VistA, the status of the CancelRx Response is marked CNP (CancelRx Response Processed). If the CancelRx Response is not successfully sent from VistA to the eR<sub>X</sub> Transaction Hub, then the corresponding CancelRx Request is marked CAX (CancelRx Response from VistA Unsuccessful). CNP is a non-actionable status and CAX is an actionable status. They can be retrieved in the Holding Queue using \<MV\> Message View or \<SR\> Search actions.

> **NOTE:** When CancelRx Request is received for a RxRenewal Response or a RxChange Response, the user should find all the related records in the Holding Queue and in OP, ensure that the intended records are canceled prior to acknowledging the request.

### CancelRx Process - eR<sub>X</sub> Records in the Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CancelRx Request is received, the eR<sub>X</sub> Transaction Hub sends the record to the Holding Queue. There are scenarios that apply both when there is no matching fillable eR<sub>X</sub> record for the CancelRx Request received and when there is a matching fillable eR<sub>X</sub> record for the CancelRx Request received.

#### No Matching Fillable eR<sub>X</sub> or No Auto-Cancel

The following scenarios apply when there is no matching fillable eR<sub>X</sub> record for the CancelRx Request received:

- If there is no matching fillable eR<sub>X</sub> in the eR<sub>X</sub> Transaction Hub, the request is received and displayed in the Holding Queue’s list view in status CAP (Cancel Paper R<sub>X</sub> or Faxed R<sub>X</sub>).
- When the CancelRx Request is received in the Holding Queue but does not auto-Cancel a record, it is marked with the status CAR (CancelRx Request Received).

In cases where the CancelRx Request status is marked as CAR or CAP, the user must acknowledge the requests and send out manual Approved or Denied CancelRx Responses.

The following table provides the CancelRx Request statuses before and after Acknowledging, CancelRx Response status, and the information sent back to the requesting non-VA provider on Approved and Denied CancelRx Responses.

<span id="_Toc83992572" class="anchor"></span>Table 1: CancelRx Request and Response

| CancelRx Request Status (Before ACK) | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note                | Manual Denied CancelRx Response \> Denial Reason                         |
|--------------------------------------|-------------------------------------|--------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------|
| CAR (CANCELRX REQUEST RECEIVED)      | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| CAP (CANCEL PAPERRX OR FAXED RX)     | CAA                                 | CNP                                  | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Cancel Rx Request and Response table displays the Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

For more information on the \<ACK\> Acknowledge action, refer to section <u>6.7 Acknowledge: Hidden Action for CancelRx Request</u>.

To view a CancelRx Request details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc83992596" class="anchor"></span>Figure ‑: Holding Queue List View – CAP

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc83992597" class="anchor"></span>Figure ‑: CAP Details Screen 1

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc83992598" class="anchor"></span>Figure ‑: CAP Details Screen 2

#### Matching Fillable eR<sub>X</sub> Prescription Found

When the CancelRx Request is received in the Holding Queue and finds a matching fillable eR<sub>X</sub> record to be canceled, the status of the fillable eR<sub>X</sub> record changes to “CAN” (Original eR<sub>X</sub> Canceled in Holding Queue) from its previously known status. In the case of a NewRx record, those statuses are: “N”, “I”, “W”, “H*xx* (where *x* = letter)”, “RJ” or “RM”. Once the fillable prescription is marked “CAN”, it is not an actionable entry and is not displayed in the Holding Queue’s list view.

#### Automated Approved CancelRx Responses

<span id="_Toc83992573" class="anchor"></span>Table 2: Scenarios for Automated Approved CancelRx Responses

| NewRx Status  | CancelRx Request Status (Before ACK) | CancelRx Response Status          | Automated Approved CancelRx Response \> Note             |
|---------------|--------------------------------------|-----------------------------------|----------------------------------------------------------|
| N (NEW)       | CAO (CANCEL PROCESS COMPLETE)        | CNP (CANCELRX RESPONSE PROCESSED) | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. |
| RJ (REJECTED) | CAO                                  | CNP                               | R<sub>X</sub> was never dispensed. Rejected at Pharmacy. |

The Scenarios for Automated Approved Cancel Rx Responses table displays the New Rx Status, Cancel Rx Request Status (Before ACK), Cancel Rx Response Status and Automated Approved Cancel Rx Response \>\> Note details.

To view an Automated CancelRx Response details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc83992599" class="anchor"></span>Figure ‑: CAO Status in Holding Queue List View

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc83992600" class="anchor"></span>Figure ‑: CAO Details Screen 1

As the user continues to scroll, the CancelRx Response Information displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc83992601" class="anchor"></span>Figure ‑: CAO Details Screen 2

#### Manual Approved or Denied CancelRx Responses

<span id="_Toc83992574" class="anchor"></span>Table 3: Scenarios for Manual Approved or Denied CancelRx Responses

| Inbound eRx Message Type | eRx Status                                                | CancelRx Request Status (Before ACK)    | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note | Manual Denied CancelRx Response \> Denial Reason                         |
|--------------------------|-----------------------------------------------------------|-----------------------------------------|-------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| NewRx                    | I / H*xx* / W / RM                                        | CAH (CANCEL COMPLETED IN HOLDING QUEUE) | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled – R<sub>X</sub> not found in pharmacy system. |
| RxRenewal Response       | RXR / RXE / RXI / RXW / RXP / RXC                         | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - Rx not found in pharmacy system.            |
| RxChange Response        | CXN / CXE / CXA / CXV / CXY / CXD / CXI / CXW / CXP / CXC | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Scenarios for Manual Approved or Denied Cancel Rx Responses table displays the New Rx Status, Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

To view a manually approved CancelRx Response details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc83992602" class="anchor"></span>Figure ‑: CAH Status in Holding Queue List View

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information. In the example below, the Last NewRx Status displays as “I” (In Process).

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc83992603" class="anchor"></span>Figure ‑: CAH Details Screen

### CancelRx Process - eR<sub>X</sub> Records in Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the CancelRx Request is received in the Holding Queue for a NewRx record to be canceled, and the status of the NewRx record is “PR” (Processed), an entry exists on the Outpatient side, the status changes to “CAN” (Original eR<sub>X</sub> Canceled in Holding Queue). Once the original prescription is marked “CAN”, it is not an actionable entry and is not displayed in the Holding Queue’s list view.

When the NewRx is in one of the statuses as specified in the table below, an automated Approved CancelRx Response is sent outbound after auto-Discontinuing the Prescription in OP. The Activity log for the prescription captures the auto-Discontinue activity from this process.

#### Automated Approved CancelRx Responses

<span id="_Toc83992575" class="anchor"></span>Table 4: Scenarios for Automated Approved CancelRx Responses when the original is a NewRx

| NewRx Prescription Status in OP | CancelRx Request Status (Before ACK) | CancelRx Response Status          | Automated Approved CancelRx Response \> Note                               |
|---------------------------------|--------------------------------------|-----------------------------------|----------------------------------------------------------------------------|
| Active                          | CAO (CANCEL PROCESS COMPLETE)        | CNP (CANCELRX RESPONSE PROCESSED) | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Pending                         | CAO                                  | CNP                               | R<sub>X</sub> was never dispensed. Canceled at Pharmacy.                   |
| Discontinued                    | CAO                                  | CNP                               | Prescription is already discontinued at the Pharmacy.                      |
| Refill                          | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Hold                            | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Suspended                       | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Expired                         | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Discontinued by Provider        | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Discontinued (Edit)             | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |
| Provider Hold                   | CAO                                  | CNP                               | First Fill:6/12/18, Last Fill:6/12/18, Renewals Remaining:0 (Example only) |

The Scenarios for Automated Approved Cancel Rx Responses table displays the New Rx Prescription Status in OP, Cancel Rx Request Status (Before ACK), Cancel Rx Response Status and Automated Approved Cancel Rx Response \>\> Note details

Navigate to the patient Medication Profile and select the desired eR<sub>X</sub> record.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc83992604" class="anchor"></span>Figure ‑: Medication Profile

The R<sub>X</sub> Activity Log displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc83992605" class="anchor"></span>Figure ‑: R<sub>X</sub> Activity Log 1

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/019.png)

<span id="_Toc83992606" class="anchor"></span>Figure ‑: R<sub>X</sub> Activity Log 2

The details of the CancelRx can be viewed in the Holding Queue on the CancelRx Details screen.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc83992607" class="anchor"></span>Figure ‑: CancelRx Details Screen in Holding Queue 1

As the user continues to scroll, the section for CancelRx Request Information displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc83992608" class="anchor"></span>Figure ‑: CancelRx Details Screen in Holding Queue 2

The NewRx Details screen includes an eR<sub>X</sub> status stating, “Original eR<sub>X</sub> Canceled in the Holding Queue”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc83992609" class="anchor"></span>Figure ‑: NewRx Details Screen

In addition to the above scenarios, the following also go through the same workflow in the case of an “Active” Prescription being auto-Discontinued by a CancelRx Request:

- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status when there is an outstanding Denied RxRenewal Response in the Holding Queue.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status, when corresponding eR<sub>X</sub> record is also in Outpatient with a subsequent electronic renewal fill.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient when there is an outstanding Approved or Approved with Changes RxRenewal Response not in the Holding Queue's List View.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient, when there is an outstanding Approved with Changes RxRenewal Response in the Holding Queue's List View (Approved with Changes RxRenewal Response has been \<AC\> Accepted in the Holding Queue).
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient, when there is an outstanding Approved with Changes RxRenewal Response in the Holding Queue's List View (Approved with Change RxRenewal Response has not been \<AC\> Accepted in the Holding Queue).

#### Manual Approved or Denied CancelRx Responses

When eR<sub>X</sub>es are renewed within VA using either RN function or using CPRS Renewal, the eR<sub>X</sub> is deemed as a VA Prescription. The “&” symbol used to denote eR<sub>X</sub> Prescriptions separately in OP does not display against such Prescriptions anymore. When CancelRx Requests are sent for fillable eR<sub>X</sub> prescriptions that are taken over by VA, the system will not auto-Discontinue the Prescriptions in OP. However, the corresponding Holding Queue NewRx record is changed to “CAN” status and the CancelRx Request may be marked “CAH”, indicating that there is user intervention required.

<span id="_Toc83992576" class="anchor"></span>Table 5: Scenarios for Manual Approved or Denied CancelRx Responses for NewRx

| NewRx Prescription Status in OP              | CancelRx Request Status (Before ACK)    | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note | Manual Denied CancelRx Response \> Denial Reason                         |
|----------------------------------------------|-----------------------------------------|-------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| Prescription renewed in VA using RN function | CAH (CANCEL COMPLETED IN HOLDING QUEUE) | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Prescription renewed using CPRS Renewal      | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Deleted                                      | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Drug Interactions                            | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Non-Verified                                 | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Scenarios for Manual Approved or Denied Cancel Rx Responses table displays the New Rx Prescription Status in OP, Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc83992610" class="anchor"></span>Figure ‑: Cancel Completed in Holding Queue

### CancelRx Request Failed (CAF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“CAF” (CancelRx Failed) is an actionable status used for CancelRx process when a failure occurs. One scenario is when the Outpatient Profile of a patient is locked in OERR and the system is attempting to auto-discontinue an eR<sub>X</sub>.

<span id="_Toc83992577" class="anchor"></span>Table 6: Scenarios for CancelRx Failed

| \#  | Scenario                                                                                                                                  | Lock in OERR                                                                                                       | Lock in Backdoor Orders \> Edit Mode                                                                               | Lock in Backdoor Orders                                                                                    |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1   | When a user selects an Active eR<sub>X</sub> from OP and locks it, and at the same time a CancelRx Request is sent for that prescription. | The CancelRx Request status is marked as CAF in the Holding Queue and the OP prescription continues to be Active.  | The CancelRx Request status is marked as CAF in the Holding Queue and the OP prescription continues to be Active.  | The CancelRx Request status is marked as CAO in the Holding Queue and the OP prescription is discontinued. |
| 2   | When a user selects a Pending eR<sub>X</sub> from OP and locks it, and at the same time a CancelRx Request is sent for that prescription. | The CancelRx Request status is marked as CAF in the Holding Queue.                                                 | The CancelRx Request status is marked as CAF in the Holding Queue.                                                 | The CancelRx Request status is marked as CAO in the Holding Queue and the OP prescription is discontinued. |
| 3   | When a user selects an eR<sub>X</sub> from OP that is on Hold, and at the same time a CancelRx Request is sent for that prescription.     | The CancelRx Request status is marked as CAF in the Holding Queue and the OP prescription continues to be on Hold. | The CancelRx Request status is marked as CAF in the Holding Queue and the OP prescription continues to be on Hold. | The CancelRx Request status is marked as CAO in the Holding Queue and the OP prescription is discontinued. |

The Scenarios for Cancel Rx Failed table displays the \#,Scenario,Lock in OERR, Lock in Backdoor Orders \>\> Edit Mode and Lock in Backdoor Orders details.

### CancelRx Request Received (CAR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“CAR” (CancelRx Request Received) is an actionable status used for CancelRx process when a NewR<sub>X</sub> record in “PR” status in the Holding Queue is successfully canceled. However, the corresponding eR<sub>X</sub> in OP could not be auto-Discontinued because the patient on the NewR<sub>X</sub> record did not match the VistA patient in the Outpatient record. In this case, no automated CancelRx Response is sent. The user must acknowledge and send a manual response.

## Inbound Error – CNE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inbound Error message is in the NCPDP 2017071 format for Inbound Error message received in VistA under situations including the Prescriber’s EHR system being unable to receive and process a certain transaction sent from the pharmacy or a connection between the Transaction Hub and Change Healthcare is not working.

When a CancelRx Response sent from VistA Outpatient Pharmacy results in an Inbound Error, it is retrieved but not displayed in the Holding list view, with the status “CNE” (CancelRx Response/Inbound Error). This is not an actionable entry and does not require the user to acknowledge it.

## Acknowledge: Hidden Action for CancelRx Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CancelRx Request is displayed in the Holding Queue’s list view, it is in an actionable status. The user can use the hidden action \<ACK\> Acknowledge to review and remove it from the list view. For a full list of CancelRx Request statuses, refer to <u>Table 13: Holding Queue Status Codes & Descriptions for CancelRx Request Message Type</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

### Acknowledge: Automated CancelRx Response Sent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In cases in which the automated CancelRx Response has already been sent to the requesting non-VA provider, the user does not have the ability to select the response type and send it out. This applies to the CancelRx Request records in the Holding Queue’s list view, in “CAO” (Cancel Completed in Holding Queue) actionable status only.

To Acknowledge a CancelRx Request:

1.  Select the CancelRx Request from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc83992611" class="anchor"></span>Figure ‑: Holding Queue – eR<sub>X</sub> in CAO Status

1.  Enter \<??\> to display additional actions.
2.  Enter \<ACK\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc83992612" class="anchor"></span>Figure ‑: Additional Action - ACK

3.  Enter Yes to acknowledge the record.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc83992613" class="anchor"></span>Figure ‑: Acknowledge Record

The CancelRx Request is acknowledged and Status is changed to “CAA” in the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc83992614" class="anchor"></span>Figure ‑: Holding Queue – CAA Status

When viewing the details of the record, the status of the CancelRx Request displays as “CancelRx Request Acknowledged”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc83992615" class="anchor"></span>Figure ‑: CancelRx Request Acknowledged

### Acknowledge: No Automated CancelRx Response Sent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In cases where no automated CancelRx Response has been sent to the requesting non-VA Provider, the user has the ability to select the response type and send it out. This applies to the CancelRx Request records in the Holding Queue’s list view, in the following actionable statuses only:

- “CAR” (CancelRx Request Received)
- “CAP” (Cancel Paper R<sub>X</sub> or Faxed R<sub>X</sub>)
- “CAH” (Cancel Completed in Holding Queue)
- “CAX” (CancelRx Response from VistA Unsuccessful)
- “CAF” (Cancel Process Failed)

To Acknowledge a CancelRx Request:

1.  Select the CancelRx Request from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc83992616" class="anchor"></span>Figure ‑: Holding Queue – eR<sub>X</sub> in CAH Status

4.  Enter \<??\> to display additional actions.
5.  Enter \<ACK\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc83992617" class="anchor"></span>Figure ‑: Additional Action - ACK

6.  Select the response type, \<A\> Approved or \<D\> Denied.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc83992618" class="anchor"></span>Figure ‑: Select Response Type

7.  Enter Yes to acknowledge the record.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc83992619" class="anchor"></span>Figure ‑: Acknowledge Record

The CancelRx Request is acknowledged and the Status is changed to “CAA” in the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc83992620" class="anchor"></span>Figure ‑: Holding Queue – CAA Status

When viewing the details of the record, the status of the CancelRx Request displays as “CancelRx Request Acknowledged”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc83992621" class="anchor"></span>Figure ‑: CancelRx Request Acknowledged

## Add Comments: Hidden Action for CancelRx Request/Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a free-text “Comment” field in the Message Details view for CancelRx Request and Response messages. This field allows users to enter additional comments on the CancelRx Request and Response messages. To add a comment:

1.  Type action \<AD\>.
8.  Type Request/Response comments.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc83992622" class="anchor"></span>Figure ‑: Add Comments

9.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc83992623" class="anchor"></span>Figure ‑: CancelRx Request Comments

The name of the user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the existing comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

10. Type action \<AD\>.
11. Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/037.png)

<span id="_Toc83992624" class="anchor"></span>Figure ‑: CancelRx Request Comments

12. Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc83992625" class="anchor"></span>Figure ‑: CancelRx Request Comments Updated

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix defines the acronyms referenced in this document.

<span id="_Ref51578014" class="anchor"></span>Table 7: Acronyms and Abbreviations

| Term           | Description                                                     |
|----------------|-----------------------------------------------------------------|
| AITC           | Austin Information Technology Center                            |
| CH             | Change Healthcare                                               |
| CHAMPVA        | Civilian Health and Medical Program of the VA                   |
| CPRS           | Computerized Patient Record System                              |
| CS             | Controlled Substance                                            |
| CSV            | Comma-separated value                                           |
| DAS            | Data Access Service                                             |
| DEA            | Drug Enforcement Administration                                 |
| DME            | Durable Medical Equipment                                       |
| DOB            | Date of Birth                                                   |
| DoD            | Department of Defense                                           |
| E&E            | Enrollment & Eligibility                                        |
| EHR            | Electronic Health Record                                        |
| ES             | Enrollment System                                               |
| ESD            | Enterprise Service Desk                                         |
| HIN            | Holder Identification Number                                    |
| ePA            | Electronic Prior Authorization                                  |
| eR<sub>X</sub> | Electronic Prescription                                         |
| ESD            | Enterprise Service Desk                                         |
| FAX            | Facsimile                                                       |
| FQDN           | Fully Qualified Domain Name                                     |
| ID             | Identification                                                  |
| IEP            | Inbound ePrescribing                                            |
| MbM            | Meds by Mail                                                    |
| MPI            | Master Person Index                                             |
| NAIC           | North American Industry Classification                          |
| NAICS          | North American Industry Classification System                   |
| NCPDP          | National Council for Prescription Drug Programs                 |
| NDC            | National Drug Code                                              |
| Non-CS         | Non-Controlled Substance                                        |
| NPI            | National Provider Identifier                                    |
| OERR           | Order Entry/Results Reporting                                   |
| OIT            | Office of Information & Technology                              |
| OP             | Outpatient Pharmacy                                             |
| PBM            | Pharmacy Benefits Management                                    |
| PCS            | Patient Care Services                                           |
| PHI            | Protected Health Information                                    |
| PHR            | Personal Health Record                                          |
| PII            | Personal Identifiable Information                               |
| PIN            | Personal Identification Number                                  |
| PIV            | Personal Identification Verification                            |
| POC            | Point of Contact                                                |
| PPO            | Program Planning Oversight                                      |
| PRE            | Pharmacy Reengineering                                          |
| R<sub>X</sub>  | Prescription                                                    |
| SSN            | Social Security Number                                          |
| Tech           | Technician                                                      |
| UI             | User Interface                                                  |
| UPN            | Universal Product Number                                        |
| UPC            | Universal Product Code                                          |
| VA             | Department of Veterans Affairs                                  |
| VAMC           | VA Medical Center                                               |
| VDL            | VA Documentation Library                                        |
| VHA            | Veterans Health Administration                                  |
| VISN           | Veterans Integrated Service Network                             |
| VistA          | Veterans Health Information Systems and Technology Architecture |

Acronyms and AbbreviationsThis table displays the Acronyms and Abbreviations throughout this document.

# Holding Queue Status Codes & Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix describes Holding Queue status codes.

<span id="_Ref41920640" class="anchor"></span>Table 8: Holding Queue Status Codes & Descriptions for NewRx Message Type

| Status Code | Description                                                                                                                                                                                                                                        | Actionable Status in the Holding Queue |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| N           | N/New: Status of the eR<sub>X</sub> when it first arrives in the Holding Queue and has not been acted upon in any way.                                                                                                                             | Yes                                    |
| I           | I/In Process: Status of the eR<sub>X</sub> when a user has taken an action on the eR<sub>X</sub> in the Holding Queue, including via the automatic patient or provider validation process.                                                         | Yes                                    |
| W           | W/Wait: Status of the eR<sub>X</sub> when a user has completed all 3 validations (Accept Validation/AV), on Patient, Provider and Drug/SIG, and has not yet completed the Accept (AC) action to process the eR<sub>X</sub> into the Pending Queue. | Yes                                    |
| HPT         | PATIENT NOT FOUND                                                                                                                                                                                                                                  | Yes                                    |
| HPD         | PROVIDER NOT FOUND                                                                                                                                                                                                                                 | Yes                                    |
| HNF         | NON-FORMULARY DRUG THAT NEEDS APPROVAL                                                                                                                                                                                                             | Yes                                    |
| HSO         | INSUFFICIENT STOCK                                                                                                                                                                                                                                 | Yes                                    |
| HDI         | DRUG-DRUG INTERACTION                                                                                                                                                                                                                              | Yes                                    |
| HAD         | ADVERSE DRUG INTERACTION                                                                                                                                                                                                                           | Yes                                    |
| HBA         | BAD ADDRESS                                                                                                                                                                                                                                        | Yes                                    |
| HPC         | PROVIDER CONTACTED                                                                                                                                                                                                                                 | Yes                                    |
| HPA         | PRIOR APPROVAL NEEDED                                                                                                                                                                                                                              | Yes                                    |
| HOR         | OTHER REASON                                                                                                                                                                                                                                       | Yes                                    |
| HPP         | PATIENT CONTACTED                                                                                                                                                                                                                                  | Yes                                    |
| HPR         | HOLD DUE TO PATIENT REQUEST                                                                                                                                                                                                                        | Yes                                    |
| HQY         | QUANTITY OR REFILL ISSUE                                                                                                                                                                                                                           | Yes                                    |
| HCR         | PRESCRIBER’S CS CREDENTIAL IS NOT APPROPRIATE                                                                                                                                                                                                      | Yes                                    |
| HWR         | CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS                                                                                                                                                                                                    | Yes                                    |
| HIS         | PROVIDER DEA# ISSUE                                                                                                                                                                                                                                | Yes                                    |
| HRX         | HOLD FOR RX EDIT                                                                                                                                                                                                                                   | Yes                                    |
| HDE         | DRUG USE EVALUATION                                                                                                                                                                                                                                | Yes                                    |
| HTI         | THERAPUTIC INTERCHANGE                                                                                                                                                                                                                             | Yes                                    |
| RJ          | RJ/Rejected: Status of the eR<sub>X</sub> when it has been rejected by a user. A message is sent back to the external provider indicating the eR<sub>X</sub> was rejected and the reason for rejection. Refer to the various reject reasons below. | No                                     |
| RM          | RM/Removed: Status of the eR<sub>X</sub> when it has been removed by a user. Note that a message is NOT sent back to the external provider when an eR<sub>X</sub> is removed. Refer to the various remove reasons below.                           | No                                     |
| CAN         | Original eR<sub>X</sub> Canceled in Holding Queue                                                                                                                                                                                                  | No                                     |
| HC          | HOLD DUE TO CHANGE                                                                                                                                                                                                                                 | Yes                                    |
| CXQ         | CANCELED DUE TO CHANGE                                                                                                                                                                                                                             | No                                     |

Holding Queue Status Codes & Descriptions

<span id="_Ref41921814" class="anchor"></span>Table 9: Holding Queue Status Codes & Descriptions for RxRenewal Request Message Type

<table>
<caption>Holding Queue Status Codes &amp; Descriptions</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
<th>Actionable Status in the Holding Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RRN</td>
<td>RXRENEWAL REQUEST - NEW</td>
<td>No</td>
</tr>
<tr class="even">
<td>RRC</td>
<td>RXRENEWAL REQUEST COMPLETE</td>
<td>No</td>
</tr>
<tr class="odd">
<td>RRP</td>
<td>RXRENEWAL REQUEST PROCESSED</td>
<td>No</td>
</tr>
<tr class="even">
<td>RRX</td>
<td><p>RXRENEWAL REQUEST EXPIRED</p>
<p>(RxRenewal Request message changes to “Expired” status if a response is not received after two weeks)</p></td>
<td>No</td>
</tr>
<tr class="odd">
<td>RRR</td>
<td>RXRENEWAL REQUEST RESPONSE RECEIVED</td>
<td>No</td>
</tr>
<tr class="even">
<td>RRE</td>
<td>RXRENEWAL REQUEST ERROR</td>
<td>No</td>
</tr>
</tbody>
</table>

Holding Queue Status Codes & Descriptions

<span id="_Ref41921843" class="anchor"></span>Table 10: Holding Queue Status Codes & Descriptions for RxRenewal Response Message Type

| Status Code | Description                           | Actionable Status in the Holding Queue |
|-------------|---------------------------------------|----------------------------------------|
| RXN         | RXRENEWAL RESPONSE - NEW              | Yes                                    |
| RXR         | RXRENEWAL RESPONSE REPLACE - NEW      | Yes                                    |
| RXI         | RXRENEWAL RESPONSE - IN PROGRESS      | Yes                                    |
| RXP         | RXRENEWAL RESPONSE PROCESSED          | No                                     |
| RXC         | RXRENEWAL RESPONSE COMPLETE           | No                                     |
| RXD         | RXRENEWAL RESPONSE DENIED/DNTF        | Yes                                    |
| RXW         | RXRENEWAL RESPONSE WAITING            | Yes                                    |
| RXA         | RXRENEWAL RESPONSE ACKNOWLEDGED       | No                                     |
| RXF         | RXRENEWAL RESPONSE FAILED             | Yes                                    |
| RXE         | RXRENEWAL RESPONSE - PROCESSING ERROR | Yes                                    |

Holding Queue Status Codes & Descriptions

<span id="_Ref52562818" class="anchor"></span>Table 11: Holding Queue Status Codes & Descriptions for RxChange Request Message Type

<table>
<caption>Holding Queue Status Codes &amp; Descriptions</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 48%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
<th>Actionable Status in the Holding Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CRN</td>
<td>RXCHANGE REQUEST - NEW</td>
<td>No</td>
</tr>
<tr class="even">
<td>CRC</td>
<td>RXCHANGE REQUEST COMPLETE</td>
<td>No</td>
</tr>
<tr class="odd">
<td>CRP</td>
<td>RXCHANGE REQUEST PROCESSED</td>
<td>No</td>
</tr>
<tr class="even">
<td>CRX</td>
<td><p>RXCHANGE REQUEST EXPIRED</p>
<p>(RxChange Request message changes to “Expired” status if a response is not received after two weeks)</p></td>
<td>No</td>
</tr>
<tr class="odd">
<td>CRR</td>
<td>RXCHANGE REQUEST RESPONSE RECEIVED</td>
<td>No</td>
</tr>
<tr class="even">
<td>CRE</td>
<td>RXCHANGE REQUEST ERROR</td>
<td>No</td>
</tr>
</tbody>
</table>

Holding Queue Status Codes & Descriptions

<span id="_Ref46236456" class="anchor"></span>Table 12: Holding Queue Status Codes & Descriptions for RxChange Response Message Type

| Status Code | Description                               | Actionable Status in the Holding Queue |
|-------------|-------------------------------------------|----------------------------------------|
| CXN         | RXCHANGE RESPONSE - NEW                   | Yes                                    |
| CXV         | RXCHANGE RESPONSE – PRESCRIBER AUTH - NEW | Yes                                    |
| CXY         | RXCHANGE RESPONSE – PRIOR AUTH - NEW      | Yes                                    |
| CXI         | RXCHANGE RESPONSE - IN PROCESS            | Yes                                    |
| CXP         | RXCHANGE RESPONSE PROCESSED               | No                                     |
| CXC         | RXCHANGE RESPONSE COMPLETE                | No                                     |
| CXD         | RXCHANGE RESPONSE DENIED                  | Yes                                    |
| CXW         | RXCHANGE RESPONSE WAITING                 | Yes                                    |
| CXA         | RXCHANGE RESPONSE ACKNOWLEDGED            | No                                     |
| CXE         | RXCHANGE RESPONSE - PROCESSING ERROR      | Yes                                    |

Holding Queue Status Codes & Descriptions

<span id="_Ref52740079" class="anchor"></span>Table 13: Holding Queue Status Codes & Descriptions for CancelRx Request Message Type

| Status Code | Description                               | Actionable Status in the Holding Queue |
|-------------|-------------------------------------------|----------------------------------------|
| CAA         | CANCELRX REQUEST ACKNOWLEDGED             | No                                     |
| CAH         | CANCEL COMPLETED IN HOLDING QUEUE         | Yes                                    |
| CAO         | CANCEL PROCESS COMPLETE                   | Yes                                    |
| CAP         | CANCEL PAPERRX OR FAXED RX                | Yes                                    |
| CAR         | CANCELRX REQUEST RECEIVED                 | Yes                                    |
| CAX         | CANCELRX RESPONSE FROM VISTA UNSUCCESSFUL | Yes                                    |
| CAF         | CANCEL PROCESS FAILED                     | Yes                                    |

Holding Queue Status Codes & Descriptions

<span id="_Ref46236450" class="anchor"></span>Table 14: Holding Queue Status Codes & Descriptions for CancelRx Response Message Type

| Status Code | Description                               | Actionable Status in the Holding Queue |
|-------------|-------------------------------------------|----------------------------------------|
| CNE         | CANCELRX RESPONSE/INBOUND ERROR           | No                                     |
| CNP         | CANCELRX RESPONSE PROCESSED               | No                                     |
| CNX         | MANUAL OR AUTO-CANCELRX RESPONSE NOT SENT | No                                     |

Holding Queue Status Codes & Descriptions

<span id="_Ref46236459" class="anchor"></span>Table 15: Holding Queue Status Codes & Descriptions for Inbound Error Message Type

| Status Code | Description                          | Actionable Status in the Holding Queue |
|-------------|--------------------------------------|----------------------------------------|
| RRE         | RXRENEWAL REQUEST ERROR              | Yes                                    |
| IRA         | INBOUND RXRENEWAL ERROR ACKNOWLEDGED | No                                     |
| E           | ERROR                                | No                                     |
| CNE         | CANCELRX RESPONSE/INBOUND ERROR      | No                                     |
| CRE         | RXCHANGE REQUEST ERROR               | Yes                                    |
| ICA         | INBOUND RXCHANGE ERROR ACKNOWLEDGED  | No                                     |

Holding Queue Status Codes & Descriptions

<span id="_Ref46236461" class="anchor"></span>Table 16: Reject Reason Codes (NewRx Message Only)

| Status Code | Description                                           |
|-------------|-------------------------------------------------------|
| PTT01       | Patient not eligible                                  |
| PTT02       | Cannot resolve patient                                |
| PVD01       | Provider not eligible                                 |
| PVD02       | Cannot resolve provider                               |
| DRU01       | Not eligible for renewals                             |
| DRU02       | Non-formulary drug                                    |
| DRU03       | Duplicate prescription found for this patient         |
| DRU04       | Invalid quantity                                      |
| DRU05       | Duplicate therapeutic class                           |
| DRU06       | Controlled substances are disallowed                  |
| ERR01       | Multiple errors, please contact the pharmacy          |
| ERR02       | Incorrect pharmacy                                    |
| ERR03       | Issues with prescription, please contact the pharmacy |
| PVD03       | Missing/bad digital signature on inbound CS ERX       |
| PVD04       | Prescriber’s CS credential is not appropriate         |
| PTT03       | Patient’s mailing address is missing/mismatched       |
| ERR09       | Other                                                 |

Holding Queue Status Codes & Descriptions

<span id="_Ref528333332" class="anchor"></span>Table 17: Remove Reason Codes (NewRx Message Only)

| Status Code | Description                                                      |
|-------------|------------------------------------------------------------------|
| REM01       | Drug out of stock or on backorder and unavailable for processing |
| REM02       | Patient was not able to pick up                                  |
| REM03       | Prescription canceled by provider                                |
| REM04       | Prescription processed manually                                  |
| REM05       | Provider will cancel this eR<sub>X</sub> and submit another      |
| REM06       | Unable to mail prescription and patient unable to pick up        |
| REM07       | Unable to contact patient                                        |
| REM08       | Unable to contact provider                                       |
| REM91       | Undefined system error                                           |
| REM92       | Other                                                            |
| REM09       | ERX Issue not resolved-Provider contacted                        |

Holding Queue Status Codes & Descriptions

# NCPDP Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix outlines common NCPD error codes and their descriptions, which will be visible in the Detail View of a message in the IEP web-based application.

<span id="_Ref520887324" class="anchor"></span>Table 18: NCPDP Error Codes

<table>
<caption>NCPDP Error Codes displays the Element Name, M/O, Datatype, Possible, Values, Description details.</caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>M/O</th>
<th>Datatype</th>
<th>Possible Values</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Code</td>
<td>M</td>
<td>String</td>
<td>600|601|602|900</td>
<td><ul>
<li><p>6ØØ Communication problem - try again later</p></li>
<li><p>6Ø1 Receiver unable to process</p></li>
<li><p>6Ø2 Receiver System Error</p></li>
<li><p>9ØØ Transaction rejected</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Description Code</td>
<td>O</td>
<td>String</td>
<td>001|002|003</td>
<td><ul>
<li><p>ØØ1 Sender ID not on file.</p></li>
<li><p>ØØ2 Receiver ID not on file.</p></li>
<li><p>ØØ3 Invalid password for sender.</p></li>
<li><p>ØØ4 Invalid password for receiver</p></li>
<li><p>ØØ5 No password on file for sender.</p></li>
<li><p>ØØ6 No password on file for receiver.</p></li>
<li><p>ØØ7 Internal processing error has occurred.</p></li>
<li><p>ØØ8 Request timed out before response could be received.</p></li>
<li><p>ØØ9 Required segment UIB is missing.</p></li>
<li><p>Ø1Ø Required segment UIH is missing.</p></li>
<li><p>Ø11 Required segment UIT is missing.</p></li>
<li><p>Ø12 Required segment UIZ is missing.</p></li>
<li><p>Ø13 Unknown segment has been encountered.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Description</td>
<td>O</td>
<td>an (70)</td>
<td>Free text</td>
<td></td>
</tr>
</tbody>
</table>

NCPDP Error Codes displays the Element Name, M/O, Datatype, Possible, Values, Description details.

# RxRenewal Request Preconditions and Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix outlines when warnings are triggered for an outbound RxRenewal Request. A warning is received when:

1.  Renewals are remaining for the prescription; therefore, a renewal request cannot be created.
1.  \<RR\> is being used on a non-eR<sub>X</sub> prescription.
2.  \<RR\> is used on an eR<sub>X</sub> that already has a RxRenewal Request generated. Warning text includes the user who initiated the request, when each request was sent, any response received for the request or if it ended up in an ERROR scenario, and the number of requests sent in the last 30 days.
3.  \<RN\> (Renew) function is initiated for an eR<sub>X</sub>.
4.  Place Order \# contains “S” or it is not a positive integer.
5.  Prescription does not exist in File \#52.
6.  Orderable item is in Inactive status.
7.  Prescription is in CMOP Transmission state.
8.  Prescription has been expired for greater than 120 days.
9.  Prescription has been discontinued for greater than 120 days.
10. Drug mismatch.
11. Invalid dosage.
12. Missing SIG.
13. Drug is no longer used by Outpatient Pharmacy.
14. DEA Special Handling filed has 1, 2, or W.
15. Schedule I Narcotic Drug.
16. Maximum number of renewals (26) has been reached.
17. Status in File \#52 is 2, 5, 6, 11, 14.
18. R<sub>X</sub> has Forward Order \# field, 39.5 in File \#52.
19. Same as previous, but checks cross-referenced AQ.
20. Titration – Tapering Dose/Complex.