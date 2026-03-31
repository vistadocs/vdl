---
title: Inbound ePrescribing User Manual (Unit 5 Part 2) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 5 Part 2) PSO*7*617 and PSO*7*670
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
description: - [RxChange Response Message Details View](#rxchange-response-message-details-view) - [Fillable RxChange Responses](#fillable-rxchange-responses) - [Non-fillable RxChange Responses](#non-fillable-rxchange-responses) - [RxChange Response Process](#rxchange-response-process) - [Fillable RxChange Respo
audience: 
keywords: 
  - rxchange
  - response
  - span
  - inbound
  - class
  - figure
  - request
  - unit
  - message
  - eprescribing
page_count: 0
word_count: 4577
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um__52.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um__52.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

## Table of Contents

  - [RxChange Response Message Details View](#rxchange-response-message-details-view)
    - [Fillable RxChange Responses](#fillable-rxchange-responses)
    - [Non-fillable RxChange Responses](#non-fillable-rxchange-responses)
  - [RxChange Response Process](#rxchange-response-process)
    - [Fillable RxChange Response Process](#fillable-rxchange-response-process)
    - [Non-Fillable RxChange Response Process](#non-fillable-rxchange-response-process)
  - [Inbound Error – CRE](#inbound-error-cre)
  - [Add Comments: Hidden Action for RxChange Request/Response](#add-comments-hidden-action-for-rxchange-requestresponse)
  - [Acknowledge: Hidden Action for RxChange Response/Inbound Error](#acknowledge-hidden-action-for-rxchange-responseinbound-error)
---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)
  Inbound ePrescribing (IEP) 5.0
  User Guide
---
![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/001.png)
November 2021
Version 5.0 (Unit 5 Part 2)
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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in</p>
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
5.  
    1.  
    2.  
    3.  
    4.  

## RxChange Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user selects the RxChange Response from the eR<sub>X</sub> Holding Queue, the RxChange Response details display in the Message Details View. It displays the content of the RxChange Response, along with the relation to the RxChange Request message, and the original NewRx message.

### Fillable RxChange Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc83992236" class="anchor"></span>Figure ‑: Response Message Details – Approved (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc83992237" class="anchor"></span>Figure ‑: RxChange Response Information – Approved (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc83992238" class="anchor"></span>Figure ‑: RxChange Response Message Details – AwC (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc83992239" class="anchor"></span>Figure ‑: RxChange Response Information – AwC (D, G, T, S and OS Request Types )

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc83992240" class="anchor"></span>Figure ‑: RxChange Response Message Details – Validated (U Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc83992241" class="anchor"></span>Figure ‑: RxChange Response Information – Validated (U Request Type)

> **NOTE:** When Prohibit Renewal Request flag is sent on an original NewRx, it is carried forward into the subsequent fillable RxChange Response and is displayed in the Message Details View. It is not displayed for a non-fillable RxChange Response.

### Non-fillable RxChange Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc83992242" class="anchor"></span>Figure ‑: RxChange Response Message Details – Approved (P Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc83992243" class="anchor"></span>Figure ‑: RxChange Response Information – Approved (P Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc83992244" class="anchor"></span>Figure ‑: RxChange Response Message Details – Denied (All Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc83992245" class="anchor"></span>Figure ‑: RxChange Response Information – Denied (All Request Types)

For all types of change responses, the Message History section links the RxChange Request Reference Number to the RxRenewal Response and to the Original NewRx message.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc83992246" class="anchor"></span>Figure ‑: RxChange Request Information and Message History

## RxChange Response Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Fillable RxChange Response Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following RxChange Response types have the same workflow in VistA Holding Queue.

- RxChange Response Message – Approved response type for request types, D, T, G, S and OS
- RxChange Response Message - Approved with Changes (AwC) response type for request types, D, T, G, S and OS
- RxChange Response Message - Validated response type for request type U

The fillable change responses display in the Holding Queue List View screen as an actionable entries. They can also be found using \<MV\> Message View or \<SR\> Search.

The statuses of the RxChange Response Message – Approved and AwC response types for request types, D, T, G, S and OS, are CXN (RxChange Response - New). The status of the RxChange Response Message – Validated is CXV (RxChange Response – Prescriber Auth - New).

When a fillable change response is received, the original is canceled in the Holding Queue and discontinued in Outpatient Pharmacy (if exists), and the change response is to be treated exactly the same way as a NewRx wherein the pharmacy user would exercise actions such as \<VP\>, \<VM\>, \<VD\> and so on.

> **NOTE:** The workflow of a fillable change response is very similar to that of a NewRx record. For complete details about how to process a NewRx record, refer to section 3.3.1 NewRx Message in User Manual Unit 3 Part 1 (PSO_7_0_P617_UM_31) available on the Veteran’s Documentation Library (VDL).

For the sake of training, a full life cycle of fillable Approved RxChange Response will be discussed further.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc83992247" class="anchor"></span>Figure ‑: CXN Status in Holding Queue List View

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc83992248" class="anchor"></span>Figure ‑: Original eR<sub>X</sub> record auto-canceled in Holding Queue

The RxChange Response details displays the RxChange Response Message type.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc83992249" class="anchor"></span>Figure ‑: RxChange Response - Approved (fillable) Details Screen

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Replace.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc83992250" class="anchor"></span>Figure ‑: RxChange Response - Approved (fillable) Information Section

When a user takes any action on the CXN/CXV record in the Holding Queue, the status of the record changes to CXI, which indicates that the record is in process.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc83992251" class="anchor"></span>Figure ‑: CXI Status in the Holding Queue

The user may select the record to view the fillable RxChange Response Details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc83992252" class="anchor"></span>Figure ‑: CXI – Summary/Details screen

When the user completes accepting the validation of Patient, Provider and Drug on the fillable change response, the status changes to CXW, indicating that the record is now in waiting status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/019.png)

<span id="_Toc83992253" class="anchor"></span>Figure ‑: CXW Status in the Holding Queue

The user may select the record to view the RxChange Response Details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc83992254" class="anchor"></span>Figure ‑: CXW – Summary/Details screen

When the user accepts the RxChange Response record using \<AC\>, the status of the record changes to “CXP” (RxChange Response Processed), and it is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc83992255" class="anchor"></span>Figure ‑: CXP Status in Holding Queue

On the Outpatient side, a pending line entry is added for the user to finish the RxChange Response.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc83992256" class="anchor"></span>Figure ‑: Medication Profile – Pending Line Entry

The user may select the pending line entry to finish the RxChange Response and accept it.

RxChange Response is now an active prescription, which displays in the Active section of the Medication Profile.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc83992257" class="anchor"></span>Figure ‑: RxChange Response to an active R<sub>X</sub> in Active Section of the Medication Profile

Once the RxChange Response becomes an active prescription, the status of the RxChange Response in the Holding Queue changes to CXC (RxChange Response Completed).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc83992258" class="anchor"></span>Figure ‑: CXC Status in the Holding Queue

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc83992259" class="anchor"></span>Figure ‑: RxChange Response Details Screen

The status of the corresponding RxChange Request changes to CRC (RxChange Request Completed).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc83992260" class="anchor"></span>Figure ‑: CRC Status in the Holding Queue

Select the record to view the RxChange Request details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc83992261" class="anchor"></span>Figure ‑: RxChange Request Details Screen

The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

The status of a RxChange Request record transitions from CRN, CRR, CRP to CRC. For more information about RxChange Request status codes, refer to <u>Table 11: Holding Queue Status Codes & Descriptions for RxChange Request Message Types</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in Unit 6 (PSO_7_0_P617_UM_6) available on the Veteran’s Documentation Library (VDL).

#### RxChange Response – Processing Error (CXE)

RxChange Response – Processing Error (CXE) is an actionable status used for fillable RxChange Responses if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a fillable RxChange Response is attempting to auto-discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxChange Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a fillable RxRenewal Response is sent for the prescription.

When a fillable RxRenewal Response record is in CXE status, the user can still process that record similar to a NewRx record after manually canceling the original in the Holding Queue and in Outpatient Pharmacy (if a record exists).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc83992262" class="anchor"></span>Figure ‑: CXE Status in Holding Queue List View

The RxChange Response details displays the RxRenewal Response Message type.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc83992263" class="anchor"></span>Figure ‑: RxChange Response - Message Details Screen for CXE

When the user exercises one of the available actions, a warning is displayed that the corresponding HQ/OP record may not have been auto-canceled/auto-discontinued. The user is prompted to select Yes or No. Upon selecting Yes, the status of the record changes to CXI. Upon selecting No, the record remains in CXE status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc83992264" class="anchor"></span>Figure ‑: RxChange Response Processing Error Warning Text/Prompt

Once the status of the CXE record is changed to CXI, the user can exercise the record same way as a fillable change response record that was originally in CXN/CXY status. For information on how to process a fillable change response, refer to section <u>5.6.1 <span class="mark"></span>Fillable RxChange Response Process</u>.

> **NOTE:** Additional CXE information are as follows:

CXE applies to fillable change response types only.

1.  When a user selects an Active eR<sub>X</sub> from OP that has an outstanding RxChange Request and locks it, and at the same time a fillable RxChange Response is received.
2.  When a RxChange Request is sent out for a prescription, the original prescription is manually discontinued before receiving a response, following which a fillable RxChange Response is received.
3.  When a RxChange Request is sent for a prescription expired within 120 days, the patient record is locked in OP during which, a fillable RxChange Response message is received.
4.  When a RxChange Request is sent for a prescription expired within 120 days, the original is manually discontinued following which, a fillable RxChange Response message is received.
5.  When a RxChange Request is sent for a prescription discontinued within 120 days and a fillable RxChange Response message is received.
6.  When a user selects an Active eR<sub>X</sub> in OP that has an outstanding RxChange Request and locks it, and at the same time a fillable RxChange Response is sent, the Prescription gets auto-discontinued and the corresponding Response is marked as CXN/CXY in the Holding Queue. However, if the record is locked in Edit mode in OP, the response fails to auto-discontinue and is marked as CXE in the Holding Queue.
7.  When a RxChange Request is sent out for a prescription, and it is renewed within VA, the prescription becomes a non-electronic prescription. If a fillable RxChange Response is then sent, the VA Order (non-eR<sub>X</sub>) is not modified by the response. The response is marked as “CXE” in the Holding Queue.

### Non-Fillable RxChange Response Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Approved RxChange Response for P Request Type

For a P change request type, one of the response types is Approved, which is not a fillable prescription but an ‘information only’ kind of message.

When a RxChange Response – Approved for a P request type is received in the Holding Queue, it is displayed in the List View in “CXY” status (RxChange Response – Prior Auth - New).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc83992265" class="anchor"></span>Figure ‑: CXY Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc83992266" class="anchor"></span>Figure ‑: RxChange Response Details Screen – Approved for P Request Type

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Approved.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc83992267" class="anchor"></span>Figure ‑: RxChange Response Information Section

There is no user intervention required on the Approved RxChange Response (for P Request Type), other than acknowledging. For more information on how to acknowledge a record in actionable status, refer to section <u>5.9 Acknowledge: Hidden Action for RxChange Response/Inbound Error</u>.

The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

#### Denied RxChange Response for all Request Types

Another RxChange Response message type is Denied. This indicates the change request is denied. This response applies to all request types.

When a RxChange Response – Denied type is received in the Holding Queue, it is displayed in the List View in “CXD” status (RxChange Response Denied).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc83992268" class="anchor"></span>Figure ‑: CXD Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc83992269" class="anchor"></span>Figure ‑: RxChange Response Details Screen – Denied

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Denied.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc83992270" class="anchor"></span>Figure ‑: RxChange Response Information Section

There is no user intervention required on the Denied RxChange Response other than acknowledging. For more information on how to acknowledge a record in actionable status, refer to section <u>5.9 Acknowledge: Hidden Action for RxChange Response/Inbound Error</u>.

The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

## Inbound Error – CRE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound ERROR message is the NCPDP 2017071 format for Inbound Error message received in VistA under certain situations, including the Prescriber’s EHR system being unable to receive and process a certain transaction sent from the Pharmacy or a connection between the Transaction Hub and Change Healthcare is not working.

When a RxChange Request sent from VistA Outpatient Pharmacy results in an Inbound Error, it is retrieved and displayed in the Holding Queue’s list view with the status CRE (RxChange Request Error). This is an actionable entry and requires the user to acknowledge it.

For more information about \<ACK\> Acknowledge, refer to section <span class="mark"></span><u>5.9 <span class="mark"></span>Acknowledge: Hidden Action for RxChange Response/Inbound Error</u>.

## Add Comments: Hidden Action for RxChange Request/Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a free-text Comment field in the Message Details view for RxChange Request and Response messages. This field allows users to enter additional comments on the RxChange Request and Response messages. To add a comment:

1.  Type action \<AD\>.
1.  Type Request/Response comments.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/037.png)

<span id="_Toc83992271" class="anchor"></span>Figure ‑: Add Comments

2.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc83992272" class="anchor"></span>Figure ‑: RxChange Request Comments

The user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

3.  Type action \<AD\>.
4.  Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/039.png)

<span id="_Toc83992273" class="anchor"></span>Figure ‑: Replacing RxChange Request Comments

5.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/040.png)

<span id="_Toc83992274" class="anchor"></span>Figure ‑: RxChange Request Comments Updated

## Acknowledge: Hidden Action for RxChange Response/Inbound Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user completes reviewing an Approved for Prior Authorization Request or a Denied RxChange Response message in the Holding Queue’s list view, the user can exercise \<ACK\> Acknowledge Hidden action to remove the message from the list view. The resulting acknowledged message can be retrieved using \<MV\> Message View or \<SR\> Search. Acknowledge is also enabled for the Inbound Errors with status CRE. When a RxChange Response – Denied type is received in the Holding Queue, it is displayed in the list view, and is in the actionable “CXD” status. When a RxChange Response – Approved type for Prior Authorization request is received in the Holding Queue, it is displayed in the list view, and is in the actionable “CXY” status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/041.png)

<span id="_Toc83992275" class="anchor"></span>Figure ‑: CXD Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/042.png)

<span id="_Toc83992276" class="anchor"></span>Figure ‑: RxChange Response Denied Details Screen

The user may type \<ACK\> at the prompt to acknowledge the RxChange Response message.

Once the user selects Yes at the prompt, the status of the message is changed from “CXD” to “CXA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc83992277" class="anchor"></span>Figure ‑: CXA Status in the Holding Queue

Select the record to view the RxChange Response details screen, displaying the eR<sub>X</sub> status of RxChange Response Acknowledged.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc83992278" class="anchor"></span>Figure ‑: RxChange Response Acknowledged Details Screen

> **NOTE:** When the user acknowledges a RxChange Response with a status of “CXY”, it changes to “CXA”. The workflow is the same as “CXD” to “CXA”.

When a RxChange Request results in an Inbound Error with the status “CRE”, it is displayed in the list view as an actionable entry.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/045.png)

<span id="_Toc83992279" class="anchor"></span>Figure ‑: CRE Status in the Holding Queue List View

Select the record to view the Inbound Error details screen, displaying an eR<sub>X</sub> status of RxChange Request Error.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/046.png)

<span id="_Toc83992280" class="anchor"></span>Figure ‑: RxChange Request Error Details Screen

The user may type \<ACK\> Acknowledge at the prompt to acknowledge the RxChange Response message.

Once the user selects Yes at the prompt, the status of the message is changed from “CRE” to “ICA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/047.png)

<span id="_Toc83992281" class="anchor"></span>Figure ‑: ICA Status in the Holding Queue

Select the record to view the Inbound Error details screen, with an eR<sub>X</sub> status of Inbound RxChange Request Error Acknowledged.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-617-and-pso-7-670/048.png)

<span id="_Toc83992282" class="anchor"></span>Figure ‑: Inbound Error Details Screen – Inbound RxChange Request Error Acknowledged