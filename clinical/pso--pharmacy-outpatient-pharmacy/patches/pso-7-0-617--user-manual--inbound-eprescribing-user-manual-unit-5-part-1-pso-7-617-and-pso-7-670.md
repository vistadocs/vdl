---
title: Inbound ePrescribing User Manual (Unit 5 Part 1) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 5 Part 1) PSO*7*617 and PSO*7*670
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
  - request
  - span
  - rxchange
  - figure
  - class
  - unit
  - change
  - inbound
  - eprescribing
  - manual
page_count: 0
word_count: 3413
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_51.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_51.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/001.png)

November 2021

Version 5.0 (Unit 5 Part 1)

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

# RxChange Requests and Responses


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [RxChange Requests and Responses](#rxchange-requests-and-responses)
  - [Generate RxChange Requests from Outpatient Profile](#generate-rxchange-requests-from-outpatient-profile)
    - [Hidden Action - eR<sub>X</sub> Change Request/EC](#hidden-action-ersubxsub-change-requestec)
    - [Change Request Forms](#change-request-forms)
  - [RxChange Requests in the eR<sub>X</sub> Holding Queue](#rxchange-requests-in-the-ersubxsub-holding-queue)
  - [RxChange Request Message Details View](#rxchange-request-message-details-view)
    - [RxChange Request for D, G, T, OS, and S Request types](#rxchange-request-for-d-g-t-os-and-s-request-types)
    - [RxChange Request for P and U Request Types](#rxchange-request-for-p-and-u-request-types)
  - [RxChange Responses in the eR<sub>X</sub> Holding Queue](#rxchange-responses-in-the-ersubxsub-holding-queue)
The RxChange Request function is used by pharmacists to generate and send outbound RxChange Requests. The RxChange Request message is sent to the external provider that originally sent the eR<sub>X</sub> into VistA. After a RxChange Request has been sent to the external provider, the provider is able to send a RxChange Response back to the requesting Pharmacy.
The Pharmacy user is allowed to generate and send the following outbound RxChange Request types:
- D - DUE (Drug Use Evaluation): May be used to request a prescriber authorize a change to the patient's current medication therapy, such as a dosing regimen change or an alternative medication that will have fewer, or no, adverse effects than the original prescription. This option is not available for CS eRx records.
- G - Generic Substitution: A modification of the product prescribed to a generic equivalent. This option is not available for CS eRx records.
- OS - Out of Stock: Pharmacy is out of stock of the medication prescribed and it cannot be obtained in a clinically appropriate timeframe. This option is not available for CS eRx records.
- P - Prior Authorization Required: A request to obtain prior authorization before dispensing.
- S - Script Clarification: The pharmacist needs to clarify what the prescriber is sending. This option is not available for CS eRx records.
- T - Therapeutic Interchange/Substitution: A modification of the product prescribed to a preferred product choice. This option is not available for CS eRx records.
- U - Prescriber Authorization: Resolution of the prescriber authorization conflict related to state/federal regulatory requirements is required before dispensing.

## Generate RxChange Requests from Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Hidden Action - eR<sub>X</sub> Change Request/EC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eR<sub>X</sub> Change Request/EC is a hidden action used for requesting change on a NewRx message, in the Holding Queue. The user can exercise EC action on NewRx record in one of the following statuses: N, I, W, or PR.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc86846808" class="anchor"></span>Figure 5‑1: Hidden Action – EC/eR<sub>X</sub> Change Request

#### HC Status/Hold Due to Change

Once a user requests change on a NewRx, the NewRx record is changed from its current Holding Queue status to HC/Hold Due to Change. When a record is in HC status only UH/Un Hold, P/Print and SH/Status History actions are available.

> **NOTE:** HC status is unavailable for the user while manually putting a fillable eR<sub>X</sub> record on ‘Hold’.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc86846809" class="anchor"></span>Figure 5‑2: NewRx in HC Status

#### Un Hold an HC Record

When a NewRx record is in HC status the user may use UH/Un Hold action to revert the record back to its previous status.

### Change Request Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Long Form

The long form is used for the change request types, D, G, T, OS, and S. On this version, there are two required fields, Drug and Substitutions. The user can request up to 3 new medications. The user can also enter an optional ‘Note’ and echo the eR<sub>X</sub> Drug information back to the provider.

1.  When the user exercises EC action, the eRX information is displayed for reference.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc86846810" class="anchor"></span>Figure 5‑3: eR<sub>X</sub> information on EC Form

- The user selects the change request code, D, G, T, OS, or S. An optional Note displays where the user enters a note for why the change is being requested. This option is not available for CS eRx records.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc86846811" class="anchor"></span>Figure 5‑4: Optional Note on EC Form

1.  The user is prompted to either select the eR<sub>X</sub> Drug E or select another drug from local drug file, for requesting the medication. The user is also prompted select Y or N for Substitutions.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc86846812" class="anchor"></span>Figure 5‑5: Selecting eR<sub>X</sub> Drug on EC Form

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc86846813" class="anchor"></span>Figure 5‑6: Selecting Drug from local file on EC Form

2.  The user is prompted to enter an optional ‘Quantity’.
    1.  If the user skips entering a value for ‘Quantity’, the next prompt for optional ‘Days Supply’ entry is displayed.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc86846814" class="anchor"></span>Figure 5‑7: Skip Quantity entry on EC Form

2.  If the user enters a value for ‘Quantity’, the 2 required fields associated with ‘Quantity’ field are displayed for the user.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc86846815" class="anchor"></span>Figure 5‑8: Quantity related fields on EC Form

> **NOTE:** ‘Quantity Code List Qualifier’ and ‘Quantity Unit Of Measure’ are text entry fields. The user could enter “??” for each field to view the list of values they can select from.

3.  The user is prompted to enter the optional ‘Days Supply’ and ‘Refills’ values.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc86846816" class="anchor"></span>Figure 5‑9: Days Supply and Refills on EC Form

4.  The user is prompted to enter the optional SIG (using the Word Processing feature). The SIG maybe up to 1000 alphanumeric characters.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc86846817" class="anchor"></span>Figure 5‑10: SIG on EC Form

5.  The requested medication information is displayed for the user to review and decide if they want to use that or not. The user can send between one and 3 medications by answering the questions.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc86846818" class="anchor"></span>Figure 5‑11: Additional Questions on EC Form

The option for selecting the G type change request is unavailable to the user when the substitutions on the original NewRx is allowed.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc86846819" class="anchor"></span>Figure 5‑12: G Unavailable When Substitutions Are Allowed

#### Short Form

The short form is used for the change request types P and U. On this version, the user can enter an optional ‘Note’. No new medication can be requested on these change request types.

#### EC Form for Prior Authorization Request

1.  When the user exercises EC action, the eRx information is displayed for reference.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc86846820" class="anchor"></span>Figure 5‑13: eR<sub>X</sub> information and optional Note on EC Form

2.  The user selects the change request code, P/Prior Authorization Required. An optional Note will be displayed where the user enters a note for why the change is being request.
3.  The user then answers the question whether to send the request out or not.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc86846821" class="anchor"></span>Figure 5‑14: Question on EC Form for P Type Request

#### EC Form for Prescriber Authorization Request

1.  When the user exercises EC action, the eR<sub>X</sub> information is displayed for reference.
2.  The user selects the change request code, U/Prescriber Authorization.
3.  The user selects the change request sub code for, U type request code.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc86846822" class="anchor"></span>Figure 5‑15: Change Request code and Sub Codes for U Type Request

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc86846823" class="anchor"></span>Figure 5‑16: Change Request Sub Codes List for U Type Request

4.  An optional Note will be displayed where the user enters a note for why the change is being requested.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc86846824" class="anchor"></span>Figure 5‑17: Optional Note on EC From for U Type Request

5.  The user then answers the question whether to send the request out or not.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/019.png)

<span id="_Toc86846825" class="anchor"></span>Figure 5‑18: Question on EC Form for U Type Request

## RxChange Requests in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outbound RxChange Request messages sent from VistA Outpatient Profile are stored in the Holding Queue. They can be viewed using search criteria or in the \<MV\> Message View action. To view a RxChange Request:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<CR\> RxChange Request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc86846826" class="anchor"></span>Figure 5‑19: Message View Action and RxChange Request

The Holding Queue displays all RxChange Request messages, sorted by received date in descending order (newest requests first).

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc86846827" class="anchor"></span>Figure 5‑20: Message View Displaying RxChange Request Messages

The RxChange Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue. For RxChange Request statuses, refer to <u>Table 11</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in User Manual Unit 6 (PSO_7_0_P617_UM_6) available on the Veteran's Documentation Library (VDL).

> **NOTE:** RxChange Request messages are not in actionable statuses and so, they are not displayed in the Holding Queue’s list view. Users may view them only by using \<MV\> Message View action or using the \<SR\> Search criteria.

RxChange Requests in the Holding Queue without a response or an error received for 2 weeks or more, change status from CRN (RxChange Request - New) to CRX (RxChange Request Expired) in the Holding Queue.

## RxChange Request Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may select the RxChange Request message to display from the Holding Queue to view the message details in the Message Details View.

### RxChange Request for D, G, T, OS, and S Request types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Details View looks the same for all the request types D, G, T, OS, and S. The ‘Change Request Type’ field displays what the request type is based on the user’s selection while generating the request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc86846828" class="anchor"></span>Figure 5‑21: RxChange Request – New

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc86846829" class="anchor"></span>Figure 5‑22: RxChange Medication Request 1

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc86846830" class="anchor"></span>Figure 5‑23: RxChange Medication Request 2

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc86846831" class="anchor"></span>Figure 5‑24: RxChange Request and Message History

The Message History segment displays message history with a reference to the original R<sub>X</sub>. The RxChange Request Reference \# field displays a “V”, indicating that this was generated from VistA.

### RxChange Request for P and U Request Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Details View looks almost the same for all the request types P and U. In case of U only, the sub request code is included. The ‘Change Request Type’ field displays what the request type is based on the user’s selection while generating the request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc86846832" class="anchor"></span>Figure 5‑25: RxChange Request – New (P type request)

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc86846833" class="anchor"></span>Figure 5‑26: RxChange Request – New (U type request)

## RxChange Responses in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxChange Response is received from an external provider for the RxChange Request sent from VistA OP, the RxChange Response message is first received by the Hub and is then sent to the VistA Holding Queue. The RxChange Response message types include:

- Approved
- Approved with Changes
- Validated
- Denied

RxChange Responses that are in actionable statuses are displayed in the Holding Queue’s list view. For the full list of RxChange Response statuses, refer to <u>Table 12</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u> in [Unit 6](#User_Manual_Unit_6).

To view a RxChange Response in the Holding Queue:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<CX\> RxChange Response.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc86846834" class="anchor"></span>Figure 5‑27: Message View Action

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc86846835" class="anchor"></span>Figure 5‑28: Holding Queue Displaying RxChange Response Messages