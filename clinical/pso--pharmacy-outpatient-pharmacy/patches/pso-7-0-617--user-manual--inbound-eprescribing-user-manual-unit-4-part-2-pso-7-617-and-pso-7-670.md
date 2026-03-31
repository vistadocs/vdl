---
title: Inbound ePrescribing User Manual (Unit 4 Part 2) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 4 Part 2) PSO*7*617 and PSO*7*670
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
description: "- [Denied, New Prescription to Follow](#denied-new-prescription-to-follow) - [Denied](#denied) - [Replace](#replace) - [Inbound Error – RRE](#inbound-error-rre) - [Add Comments: Hidden Action for RxRenewal Request/Response](#add-comments-hidden-action-for-rxrenewal-requestresponse) - [Acknowledge: H"
audience: 
keywords: 
  - rxrenewal
  - response
  - span
  - inbound
  - figure
  - class
  - unit
  - eprescribing
  - status
  - part
page_count: 0
word_count: 5303
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_42.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_42.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

## Table of Contents

    - [Denied, New Prescription to Follow](#denied-new-prescription-to-follow)
    - [Denied](#denied)
    - [Replace](#replace)
  - [Inbound Error – RRE](#inbound-error-rre)
  - [Add Comments: Hidden Action for RxRenewal Request/Response](#add-comments-hidden-action-for-rxrenewal-requestresponse)
  - [Acknowledge: Hidden Action for RxRenewal Response/Inbound Error](#acknowledge-hidden-action-for-rxrenewal-responseinbound-error)
---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)
  Inbound ePrescribing (IEP) 5.0
  User Guide
---
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/001.png)
November 2021
Version 5.0 (Unit 4 Part 2)
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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in Unit 6.</p>
<ul>
<li><p>eR<sub>X</sub> Default Loopback Days</p></li>
<li><p>Replaced column label “LAST USER” with “LOCKED BY” and updated the description under Table 9</p></li>
<li><p>Added the information for LOCKED BY column in section 3.5.2 Patient Centric View</p></li>
<li><p>Replaced Figure 3-14, Figure 3-16, Figure 3-17, Figure 3-18, Figure 3-19, Figure 3-42, Figure 3-52,<br />
Figure 3-55, Figure 3-56, Figure 3-57, Figure 3-59, Figure 3-60, Figure 3-61, and Figure 3-68 for updated layout</p></li>
<li><p>Added Note and included <strong>Error! Reference source not found.</strong> to indicate to the user that a Provider’s DEA# has expired in section 3.6.2.3 Edit Provider</p></li>
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
1.  
2.  
3.  
4.  1.  
    2.  
    3.  
    4.  
    5.  
    6.  1.  
        2.  1.  

#### Changes to Provider Segment

In some scenarios, the RxRenewal Response message displays in the Holding Queue List View screen. If the changes are related to the provider or the provider and number of renewals, the RxRenewal Response displays in the Holding Queue List View because the pharmacist needs to validate the updates to the Provider.
When a RxRenewal Response message type is Approved with Changes, Provider segment only, or Provider and number of renewals in the Drug segment, it displays in the Holding Queue List View screen. It can also be found using \<MV\> Message View or \<SR\> Search. The status of the Approved with Changes RxRenewal Response is “RXN” (RxRenewal Response - New).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/002.png)
<span id="_Toc89097654" class="anchor"></span>Figure 4.6.3‑1: RXN Status in Holding Queue List View
The RxRenewal Response details displays the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/003.png)
<span id="_Toc89097655" class="anchor"></span>Figure 4.6.3‑3: RxRenewal Response Details Screen
As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Approved with Changes.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/004.png)
<span id="_Toc89097656" class="anchor"></span>Figure 4.6.3‑4: RxRenewal Response Information Section
If the user edits the provider’s information when they exercise \<VM\> Validate Provider on this response, the status of the record changes to “RXW” (RxRenewal Response – Waiting). When the user accepts the validation \<AV\> under \<VM\> Validate Provider, the status of the record changes to “RXW” (RxRenewal Response – Waiting).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/005.png)
<span id="_Toc89097657" class="anchor"></span>Figure 4.6.3‑5: RXW Status in the Holding Queue
The user may select the record to view the RxRenewal Response Details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/006.png)
<span id="_Toc89097658" class="anchor"></span>Figure 4.6.3‑6: RxRenewal Response Details Screen
When the user accepts the RxRenewal Response record using \<AC\>, the status of the record changes to “RXP” (RxRenewal Response Processed), and it is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/007.png)
<span id="_Toc89097659" class="anchor"></span>Figure 4.6.3‑7: RXP Status in Holding Queue
On the OP side, a pending line entry is added for the user to renew the Approved with Changes RxRenewal Response.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/008.png)
<span id="_Toc89097660" class="anchor"></span>Figure 4.6.3‑8: Medication Profile – Pending Line Entry
For information about how to process the Approved with Changes RxRenewal Response further in OP, refer to section Error! Reference source not found.Error! Reference source not found..
Once the Approved with Changes RxRenewal Response is successfully renewed in Outpatient Pharmacy, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/009.png)
<span id="_Toc89097661" class="anchor"></span>Figure 4.6.3‑9: RXC Status in the Holding Queue
Select the record to view the RxRenewal Response details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/010.png)
<span id="_Toc89097662" class="anchor"></span>Figure 4.6.3‑10: RxRenewal Response Details Screen
The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/011.png)
<span id="_Toc38526977" class="anchor"></span>Figure 4.6.3‑11: RRC Status in the Holding Queue
Select the record to view the RxRenewal Request details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/012.png)
<span id="_Toc38526978" class="anchor"></span>Figure 4.6.3‑12: RxRenewal Request Details Screen
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

### Denied, New Prescription to Follow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Denied New Prescription to Follow (DNTF). This indicates the renewal is denied, but a NewRx will follow.
When a RxRenewal Response message type is Denied NewRx to Follow (DNTF), it will display in the List View screen. It can also be found using \<MV\> Message View or \<SR\> Search. The status of the DNTF RxRenewal Response will be “RXD” (RxRenewal Response Denied/DNTF).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/013.png)
<span id="_Toc89097665" class="anchor"></span>Figure 4.6.3‑1: RXD Status in the Holding Queue List View
The RxRenewal Response details display the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/014.png)
<span id="_Toc89097666" class="anchor"></span>Figure 4.6.3‑2: RxRenewal Response Denied/DNTF Details Screen
In the below figure, the RxRenewal Response Information segment indicates the RxRenewal Response Message type is Denied, New Prescription to Follow.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/015.png)
<span id="_Toc89097667" class="anchor"></span>Figure 4.6.3‑3: RxRenewal Response Information Section
On the Outpatient side, the eR<sub>X</sub> Prescription on which the renewal was requested is auto-Discontinued (auto-DC).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/016.png)
<span id="_Toc89097668" class="anchor"></span>Figure 4.6.3‑4: Medication Profile – eR<sub>X</sub> After DNTF RxRenewal Response
The Activity Log on the OP side is updated to display that the eR<sub>X</sub> Prescription has been auto-Discontinued.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/017.png)
<span id="_Toc89097669" class="anchor"></span>Figure 4.6.3‑5: Activity Log 1
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/018.png)
<span id="_Toc89097670" class="anchor"></span>Figure 4.6.3‑6: Activity Log 2
Once the DNTF RxRenewal Response has successfully auto-Discontinued the eR<sub>X</sub> Prescription in OP, the status of the RxRenewal Response in the Holding Queue continues to display as “RXD” (RxRenewal Response Denied/DNTF).
The status of the corresponding RxRenewal Request will change to “RRP” (RxRenewal Request Processed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/019.png)
<span id="_Toc89097671" class="anchor"></span>Figure 4.6.3‑7: RRP Status in the Holding Queue
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type.

#### RxRenewal Response Failed (RXF)

RxRenewal Response Failed (RXF) is an actionable status used for the RxRenewal Response types Approved, Approved with Changes, and Denied NewRx to Follow (DNTF) if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a DNTF RxRenewal Response is attempting to auto-Discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxRenewal Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a DNTF RxRenewal Response is sent for the prescription.
> **NOTE:** Additional RXF scenarios are as follows:
RXF applies to Approved, Approved with Changes and Denied NewRx to Follow response types only.
1.  When a user selects an active eR<sub>X</sub> from OP that has an outstanding RxRenewal Request and locks it, and at the same time an Approved or Approved with Changes RxRenewal Response is received, a new pending line entry for that response is added in OP.
2.  When a RxRenewal Request is sent out for a prescription and it is manually discontinued before receiving a response, if an Approved or Approved with Changes RxRenewal Response is received, a new pending line entry for that response is added in OP.
3.  When a user selects an active eR<sub>X</sub> from OP in Backdoor Orders that has an outstanding RxRenewal Request and locks it, and at the same time a DNTF RxRenewal Response is received, the Prescription gets auto-Discontinued, and the corresponding Response is marked as “RXD” in the Holding Queue. However, if the record is locked in Edit mode in Backdoor Orders, the response fails to auto-Discontinue and is marked as “RXF” in the Holding Queue.
4.  When a RxRenewal Request is sent out for a prescription, and it is renewed within VA, the prescription becomes a non-electronic prescription. If an Approved RxRenewal Response is then received, no pending line entry is added in OP. The VA Order (non-eR<sub>X</sub>) is not modified by the response. The response is marked as “RXN” in the Holding Queue.
5.  When a RxRenewal Request is sent out for a prescription and it is renewed within VA, the prescription becomes a non-electronic prescription. If a DNTF RxRenewal Response is then received, the VA Order (non-eR<sub>X</sub>) is not auto-Discontinued by the response. The response is marked as “RXD” in the Holding Queue.

### Denied

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Denied. This indicates the renewal request is denied.
When a RxRenewal Response – Denied type is received in the Holding Queue, it is displayed in the List View in “RXD” status (RxRenewal Response Denied/DNTF).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/020.png)
<span id="_Toc38526989" class="anchor"></span>Figure 4.6.4‑1: RXD Status in the Holding Queue List View
Select the record to view the RxRenewal Response details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/021.png)
<span id="_Toc38526990" class="anchor"></span>Figure 4.6.4‑2: RxRenewal Response Details Screen – Denied
As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Denied.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/022.png)
<span id="_Toc38526991" class="anchor"></span>Figure 4.6.4‑3: RxRenewal Response Information Section
There is no user intervention required on the Denied RxRenewal Response other than acknowledging the response. For more information on how to acknowledge a record in actionable status, refer to section <u>4.9 Acknowledge: Hidden Action for RxRenewal Response/Inbound Error</u>.
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

### Replace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Replace is one of the RxRenewal Response types introduced with NCPDP 2017071 which displays in the Holding Queue List View screen as an actionable entry. It can also be found using \<MV\> Message View or \<SR\> Search. The status of the Replace Response is “RXR” (RxRenewal Response Replace - New).
Replace is used as a fillable prescription which is sent to replace an original NewRx on which the renewal was requested. When a Replace type Response is received, the original is discontinued in Outpatient Pharmacy and the Replace response is to be treated exactly the same way as a NewRx wherein the pharmacy user would exercise actions such as \<VP\>, \<VM\>, \<VD\> and so on.
> **NOTE:** The workflow of a Replace type Response is very similar to that of a NewRx record. For complete details about how to process a NewRx record, refer to section 3.3.1 NewRx Message in Unit 3 Part 1 (PSO_7_0_P617_UM_31) available on the Veteran’s Documentation Library (VDL).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/023.png)
<span id="_Toc89097675" class="anchor"></span>Figure 4.6.5‑1: RXR Status in Holding Queue List View
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/024.png)
<span id="_Toc89097676" class="anchor"></span>Figure 4.6.5‑2: eR<sub>X</sub> record discontinued in Outpatient
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/025.png)
<span id="_Toc89097677" class="anchor"></span>Figure 4.6.5‑3: Activity Log of eR<sub>X</sub> record discontinued in Outpatient 1
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/026.png)
<span id="_Toc89097678" class="anchor"></span>Figure 4.6.5‑4: Activity Log of eR<sub>X</sub> record discontinued in Outpatient 2
The RxRenewal Response details screen displays the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/027.png)
<span id="_Toc89097679" class="anchor"></span>Figure 4.6.5‑5: RxRenewal Response - Replace Details Screen
As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Replace.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/028.png)
<span id="_Toc89097680" class="anchor"></span>Figure 4.6.5‑6: RxRenewal Response - Replace Information Section
When a user takes any action on the “RXR” record in the Holding Queue, the status of the record changes to “RXI”, which indicates that the record is in process.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/029.png)
<span id="_Toc89097681" class="anchor"></span>Figure 4.6.5‑7: RXI Status in the Holding Queue
The user may select the record to view the RxRenewal Response Details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/030.png)
<span id="_Toc89097682" class="anchor"></span>Figure 4.6.5‑8: RXI – Summary/Details screen
When the user completes accepting the validation of Patient, Provider and Drug sections on the Replace type response, the status changes to “RXW”, indicating that the record is now in waiting status.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/031.png)
<span id="_Toc89097683" class="anchor"></span>Figure 4.6.5‑9: RXW Status in the Holding Queue
The user may select the record to view the RxRenewal Response Details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/032.png)
<span id="_Toc89097684" class="anchor"></span>Figure 4.6.5‑10: RXW – Summary/Details screen
When the user accepts the RxRenewal Response record using \<AC\>, the status of the record changes to “RXP” (RxRenewal Response Processed), and it is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/033.png)
<span id="_Toc89097685" class="anchor"></span>Figure 4.6.5‑11: RXP Status in Holding Queue
On the OP side, a pending line entry is added for the user to finish the Replace RxRenewal Response.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/034.png)
<span id="_Toc89097686" class="anchor"></span>Figure 4.6.5‑12: Medication Profile – Pending Line Entry
The user may select the pending line entry to finish the Replace RxRenewal Response and accept it. The Replace RxRenewal Response is now an active prescription which displays in the Active section of the Medication profile.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/035.png)
<span id="_Toc89097687" class="anchor"></span>Figure 4.6.5‑13: Replace Response to an active R<sub>X</sub> in Active Section of the Medication Profile
Once the Replace RxRenewal Response becomes an active prescription, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/036.png)
<span id="_Toc89097688" class="anchor"></span>Figure 4.6.5‑14: RXC Status in the Holding Queue
Select the record to view the RxRenewal Response details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/037.png)
<span id="_Toc89097689" class="anchor"></span>Figure 4.6.5‑15: RxRenewal Response Details Screen
The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/038.png)
<span id="_Toc89097690" class="anchor"></span>Figure 4.6.5‑16: RRC Status in the Holding Queue
Select the record to view the RxRenewal Request details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/039.png)
<span id="_Toc89097691" class="anchor"></span>Figure 4.6.5‑17: RxRenewal Request Details Screen
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type. Similar to the status change with other RxRenewal Response types, in case of Replace the corresponding RxRenewal Request record transitions from RRN, RRR, RRP to RRC. For more information about RxRenewal Request status codes, refer to <u>Appendix D: RxRenewal Request Preconditions and Warnings</u> in Unit 6 (PSO_7_0_P617_UM_6) available on the Veteran’s Documentation Library (VDL).

#### RxRenewal Response – Processing Error (RXE)

RxRenewal Response – Processing Error (RXE) is an actionable status used for Replace RxRenewal Responses if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a Replace RxRenewal Response is attempting to auto-Discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxRenewal Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a Replace RxRenewal Response is sent for the prescription.
When a Replace RxRenewal Response record is in “RXE” status, the user can still process the record similar to a NewRx record after manually canceling the original in Outpatient Pharmacy. The status codes for Replace RxRenewal Response workflow is covered in Error! Reference source not found..
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/040.png)
<span id="_Toc89097692" class="anchor"></span>Figure 4.6.5‑18: RXE Status in Holding Queue List View
The RxRenewal Response details section displays the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/041.png)
<span id="_Toc89097693" class="anchor"></span>Figure 4.6.5‑19: RxRenewal Response - Replace Details Screen for RXE
When the user exercises one of the available actions, a warning displays that the corresponding OP record may not have been auto-Discontinued. The user is prompted to select Yes or No. Upon selecting Yes, the status of the record changes to “RXI”. Upon selecting No, the record remains in “RXE” status.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/042.png)
<span id="_Toc89097694" class="anchor"></span>Figure 4.6.5‑20: Replace Response Processing Error Warning Text/Prompt
Once the status of the Replace record is changed to “RXI”, the user can exercise the record same way as a Replace record that was originally in “RXR” status. For information on how to process a Replace type response, refer to section <u>4.6.5 Replace</u>.
> **NOTE:** Additional “RXE” information are as follows:
“RXE” applies to Replace response type only.
1.  When a user selects an Active eR<sub>X</sub> from OP that has an outstanding RxRenewal Request and locks it, and at the same time a Replace RxRenewal Response is received.
2.  When a RxRenewal Request is sent out for a prescription and the original prescription is manually discontinued before receiving a response, following which a Replace RxRenewal Response is received.
3.  When a RxRenewal Request is sent for a prescription that has expired within 120 days, and the patient record is locked in OP, during which a Replace RxRenewal Response message is received.
4.  When a RxRenewal Request is sent for a prescription that has expired within 120 days, and the original is manually discontinued, following which a Replace RxRenewal Response message is received.
5.  When a RxRenewal Request is sent for a prescription that has been discontinued within 120 days and a Replace RxRenewal Response message is received.
6.  When a user selects an Active eR<sub>X</sub> in OP that has an outstanding RxRenewal Request and locks it, and at the same time a Replace RxRenewal Response is sent, the Prescription gets auto-Discontinued and the corresponding Response is marked as “RXR” in the Holding Queue. However, if the record is locked in Edit mode in OP, the response fails to auto-Discontinue and is marked as “RXE” in the Holding Queue.
7.  When a RxRenewal Request is sent out for a prescription, and it is renewed within VA, the prescription becomes a non-electronic prescription. If a Replace RxRenewal Response is then sent, the VA Order (non-eR<sub>X</sub>) is not modified by the response. The response is marked as “RXE” in the Holding Queue.

## Inbound Error – RRE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Inbound ERROR” message is the NCPDP 2017071 format for an Inbound Error message received in VistA under certain situations, such as the Prescriber’s EHR system being unable to receive and process a certain transaction sent from the Pharmacy or a connection between the Transaction Hub and Change Healthcare not working.

When a RxRenewal Request sent from VistA Outpatient Pharmacy results in an Inbound Error, it is retrieved and displayed in the Holding Queue’s list view with the status RRE (RxRenewal Request Error). This is an actionable entry and requires the user to acknowledge it.

For more information about \<ACK\> Acknowledge, refer to section <u>4.9 Acknowledge: Hidden Action for RxRenewal Response/Inbound Error</u>.

## Add Comments: Hidden Action for RxRenewal Request/Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a free-text “Comment” field in the Message Details view for RxRenewal Request and Response messages. This field allows users to enter additional comments on the RxRenewal Request and Response messages. To add a comment:

1.  Type action \<AD\>.
1.  Type Request/Response comments.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc89097695" class="anchor"></span>Figure 4.6.5‑1: Add Comments

2.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc89097696" class="anchor"></span>Figure 4.6.5‑2: RxRenewal Request Comments

The user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

3.  Type action \<AD\>.
4.  Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/045.png)

<span id="_Toc89097697" class="anchor"></span>Figure 4.6.5‑3: Replacing RxRenewal Request Comments

5.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/046.png)

<span id="_Toc89097698" class="anchor"></span>Figure 4.6.5‑4: RxRenewal Request Comments Updated

## Acknowledge: Hidden Action for RxRenewal Response/Inbound Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user completes reviewing a Denied or a Denied, NewRx to Follow RxRenewal Response message in the Holding Queue List View, the user can exercise the \<ACK\> Acknowledge Hidden action to remove the message from the list view. The resulting acknowledged message can be retrieved using \<MV\> Message View or \<SR\> Search. Acknowledge is also enabled for RxRenewal Responses that fail to auto-process and are in status of “RXF” and the Inbound Errors with status “RRE”. When a RxRenewal Response – Denied or Denied NewRx to Follow type is received in the Holding Queue, it is displayed in the list view, and is in the actionable “RXD” status.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/047.png)

<span id="_Toc89097699" class="anchor"></span>Figure 4.6.5‑1: RXD Status in the Holding Queue List View

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/048.png)

<span id="_Toc89097700" class="anchor"></span>Figure 4.6.5‑2: RxRenewal Response Denied/DNTF Details Screen

The user may type \<ACK\> at the prompt to acknowledge the RxRenewal Response message.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/049.png)

<span id="_Toc89097701" class="anchor"></span>Figure 4.6.5‑3: Acknowledge RxRenewal Response Message

Once the user selects Yes at the prompt, the status of the message is changed from “RXD” to “RXA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/050.png)

<span id="_Toc89097702" class="anchor"></span>Figure 4.6.5‑4: RXA Status in the Holding Queue

Select the record to view the RxRenewal Response details screen, displaying the eR<sub>X</sub> status of RxRenewal Response Acknowledged.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/051.png)

<span id="_Toc89097703" class="anchor"></span>Figure 4.6.5‑5: RxRenewal Response Acknowledged Details Screen

> **NOTE:** When the user acknowledges a RxRenewal Response with a status of “RXF”, it changes to “RXA”. The workflow is the same as “RXD” to “RXA”.

When a RxRenewal Request results in an Inbound Error with the status “RRE”, it is displayed in the list view as an actionable entry.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/052.png)

<span id="_Toc89097704" class="anchor"></span>Figure 4.6.5‑6: RRE Status in the Holding Queue List View

Select the record to view the Inbound Error details screen, displaying an eR<sub>X</sub> status of RxRenewal Request Error.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/053.png)

<span id="_Toc89097705" class="anchor"></span>Figure 4.6.5‑7: RxRenewal Request Error Details Screen

The user may type \<ACK\> Acknowledge at the prompt to acknowledge the RxRenewal Response message.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/054.png)

<span id="_Toc89097706" class="anchor"></span>Figure 4.6.5‑8: Acknowledge Action

Once the user selects Yes at the prompt, the status of the message is changed from “RRE” to “IRA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/055.png)

<span id="_Toc89097707" class="anchor"></span>Figure 4.6.5‑9: IRA Status in the Holding Queue

Select the record to view the Inbound Error details screen, with an eR<sub>X</sub> status of Inbound RxRenewal Request Error Acknowledged.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-617-and-pso-7-670/056.png)

<span id="_Toc89097708" class="anchor"></span>Figure 4.6.5‑10: Inbound Error Details Screen – Inbound RxRenewal Request Error Acknowledged