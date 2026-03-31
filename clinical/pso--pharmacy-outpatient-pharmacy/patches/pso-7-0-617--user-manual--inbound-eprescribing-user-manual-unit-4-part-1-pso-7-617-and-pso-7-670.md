---
title: Inbound ePrescribing User Manual (Unit 4 Part 1) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 4 Part 1) PSO*7*617 and PSO*7*670
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
  - rxrenewal
  - span
  - response
  - request
  - figure
  - class
  - unit
  - message
  - inbound
  - eprescribing
page_count: 0
word_count: 3969
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_41.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_41.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/001.png)

November 2021

Version 5.0 (Unit 4 Part 1)

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
</ul>
<p>Updated Title page, Revision History, and Footers</p></td>
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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in <strong>Error! Reference source not found.</strong> <strong><u>Error! Reference source not found.</u></strong>.</p>
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

# R<sub>X</sub>Renewal Requests and Responses


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [R<sub>X</sub>Renewal Requests and Responses](#rsubxsubrenewal-requests-and-responses)
  - [Generate R<sub>X</sub>Renewal Requests from Outpatient Profile](#generate-rsubxsubrenewal-requests-from-outpatient-profile)
    - [RxRenewal Request Precondition Checks and Warnings](#rxrenewal-request-precondition-checks-and-warnings)
  - [RxRenewal Requests in the eR<sub>X</sub> Holding Queue](#rxrenewal-requests-in-the-ersubxsub-holding-queue)
  - [RxRenewal Responses in the eR<sub>X</sub> Holding Queue](#rxrenewal-responses-in-the-ersubxsub-holding-queue)
  - [RxRenewal Request Message Details View](#rxrenewal-request-message-details-view)
  - [RxRenewal Response Message Details View](#rxrenewal-response-message-details-view)
  - [RxRenewal Response Process](#rxrenewal-response-process)
    - [Approved](#approved)
    - [Approved with Changes](#approved-with-changes)
The RxRenewal Request function is used by pharmacists to generate and send outbound RxRenewal Requests, also referred to as Renewals within VA/VistA. The RxRenewal Request message is sent to the external provider that originally sent the eR<sub>X</sub> into VistA. After a RxRenewal Request has been sent to the external provider, the provider is able to send a RxRenewal Response back to the requesting pharmacy.
The Pharmacy user is allowed to generate and send an outbound RxRenewal Request when there are no more renewals on the original prescription to fill or if the prescription is expired.
> **NOTE:** If the original NewRx Prohibit Renewals is set to true, the user is not allowed to generate renewal requests on the corresponding eR<sub>X</sub> prescription in Outpatient Pharmacy. A warning message is displayed to the user attempting renewal when the Prohibit Renewals is set to true.
Warning Text: Renewals are prohibited for this eR<sub>X</sub>.

## Generate R<sub>X</sub>Renewal Requests from Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To generate a RxRenewal Request, navigate to the patient’s Medication Profile in Complete Orders from OERR or Patient Prescription Processing. The Medication Profile displays all of the R<sub>X</sub>es associated with the patient. To generate a RxRenewal Request:

1.  Select the eR<sub>X</sub>.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc86395681" class="anchor"></span>Figure 4‑1: Select R<sub>X</sub> from Medication Profile

1.  Type \<Other\> to display additional actions.
2.  Select \<RR\> RxRenewal Request.
3.  Indicate \<R\> Refill with Pre-Populated Value or \<C\> Refill and Change Quantity.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc86395682" class="anchor"></span>Figure 4‑2: Generating RxRenewal Request Actions

4.  Enter \<Yes\> to send the renewal request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc86395683" class="anchor"></span>Figure 4‑3: RxRenewal Request Sent

> **NOTE:** When an Outbound RxRenewal Request is sent, if the user requested “n” as the number of renewals using either option “R” or option “C”, the NCPDP 2017071 RxRenewal Request message with a value of “n+1” is sent to the Provider.

The user is allowed to generate and send more than one RxRenewal Request for the same eR<sub>X</sub>. The history of all the requests sent, along with any responses or errors received within the last 30 days, is displayed at the time of generating a duplicate request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc86395684" class="anchor"></span>Figure 4‑4: RxRenewal Request History

The RxRenewal Request generated in Outpatient Profile and sent by the Pharmacy user can be found in the Holding Queue in the Message View, displaying a status of “RRN” (RxRenewal Request - New).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc86395685" class="anchor"></span>Figure 4‑5: RRN in Holding Queue

### RxRenewal Request Precondition Checks and Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of RxRenewal Request warnings that may display at the time of the outbound RxRenewal Request. For example, a warning displays when \<RR\> is being used on a non-eR<sub>X</sub> prescription.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc86395686" class="anchor"></span>Figure 4‑6: RxRenewal Request Warning

A complete list of RxRenewal Request Warnings can be found in <u>Appendix D: RxRenewal Request Preconditions and Warnings</u> in User Manual Unit (PSO_7_0_P617_UM_6) available on the Veteran's Documentation Library (VDL).

## RxRenewal Requests in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outbound RxRenewal Request messages sent from VistA Outpatient Profile are stored in the Holding Queue. They can be viewed using search criteria or in the \<MV\> Message View action. To view a RxRenewal Request:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<RR\> RxRenewal Request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc86395687" class="anchor"></span>Figure 4‑7: Message View Action and RxRenewal Request

The Holding Queue displays all RxRenewal Request messages, sorted by received date in descending order (newest requests first).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc86395688" class="anchor"></span>Figure 4‑8: Message View Displaying RxRenewal Request Messages

The RxRenewal Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue. For RxRenewal Request statuses, refer to <u>Appendix D: RxRenewal Request Preconditions and Warnings</u> in [Unit 6](#Unit_6).

> **NOTE:** RxRenewal Request messages are not in actionable statuses and so, they are not displayed in the Holding Queue’s list view. Users may view them only by using \<MV\> Message View action or using the \<SR\> Search criteria.

RxRenewal Requests in the Holding Queue without a response or an error received for 2 weeks or more change status from “RRN” (RxRenewal Request - New) to “RRX” (RxRenewal Request Expired) in the Holding Queue.

## RxRenewal Responses in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxRenewal Request receives a RxRenewal Response from an external provider sent from the VistA OP, the RxRenewal Response message is first received by the Hub and is then sent to the VistA Holding Queue. The RxRenewal Response message types include:

- Approved
- Approved with Changes
- Denied
- Denied, New Prescription to Follow
- Replace

RxRenewal Responses that are in actionable statuses are displayed in the Holding Queue’s list view. For the full list of RxRenewal Response statuses, refer to <u>Appendix D: RxRenewal Request Preconditions and Warnings</u> in [Unit 6](#Unit_6).

To view a RxRenewal Response in the Holding Queue:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<RE\> RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc86395689" class="anchor"></span>Figure 4‑9: Message View Action

The eR<sub>X</sub> Holding Queue screen displays all RxRenewal Response messages, sorted by received date in descending order (newest responses first).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/011.png)

<span id="_Toc86395690" class="anchor"></span>Figure 4‑10: Holding Queue Displaying RxRenewal Response Messages

## RxRenewal Request Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may view the message details in the Message Details view by selecting the RxRenewal Request message to be displayed from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc86395691" class="anchor"></span>Figure 4‑11: RxRenewal Request – New

See more message details below.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/013.png)

<span id="_Toc86395692" class="anchor"></span>Figure 4‑12: RxRenewal Request Medication Dispensed and RxRenewal Request Information

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc86395693" class="anchor"></span>Figure 4‑13: RxRenewal Request Message History

The Message History segment displays the message history with a reference to the original R<sub>X</sub>. The RxRenewal Request Reference \# field displays a “V”, indicating that this was generated from VistA.

## RxRenewal Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user selects the RxRenewal Response from the eR<sub>X</sub> Holding Queue, the RxRenewal Response details display in the Message Details View. The Message Details View displays the content of the RxRenewal Response, along with the relation to the RxRenewal Request message, and the original NewRx message.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc86395694" class="anchor"></span>Figure 4‑14: RxRenewal Response Message Details

> **NOTE:** When an Inbound RxRenewal Response is received, if the provider approved “n” as the number of renewals, the Message Details view displays “n-1” as the number of renewals approved. This is applicable to Approved, Approved with Changes, and Replace RxRenewal Response Types.

The RxRenewal Response Information section contains the RxRenewal Response message type along with the response date and time and any additional notes and comments.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc86395695" class="anchor"></span>Figure 4‑15: RxRenewal Response Information 2

The Message History section links the RxRenewal Request reference number to the RxRenewal Response and the original NewRx message.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc86395696" class="anchor"></span>Figure 4‑16: RxRenewal Request Information and Message History

## RxRenewal Response Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Approved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxRenewal Response message type is Approved, it is not displayed in the List View screen. It can be found using \<MV\> Message View or \<SR\> Search. The status of the Approved RxRenewal Response is “RXP” (RxRenewal Response Processed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc86395697" class="anchor"></span>Figure 4‑17: Message View and RxRenewal Response Actions

The details of the RxRenewal Response display the RxRenewal Response Message type. In Figure 4‑18, the RxRenewal Response Information segment shows the RxRenewal Response Message type is Approved.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/019.png)

<span id="_Ref52553559" class="anchor"></span>Figure 4‑18: RxRenewal Response – Approved

When the user continues to scroll, the RxRenewal Response Information section displays.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc86395699" class="anchor"></span>Figure 4‑19: RxRenewal Response Information Section

On the OP side, a pending line entry is available for the user to renew the Approved RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc86395700" class="anchor"></span>Figure 4‑20: Medication Profile – Pending Line Entry

The Activity Log on the OP side shows that a pending response entry was added.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc86395701" class="anchor"></span>Figure 4‑21: Activity Log 1

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc86395702" class="anchor"></span>Figure 4‑22: Activity Log 2 (Sample from Another Patient Record)

The user may select the pending line entry to renew the Approved RxRenewal.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc86395703" class="anchor"></span>Figure 4‑23: Pending Line Entry Selected

Then, the user may accept the Approved RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc86395704" class="anchor"></span>Figure 4‑24: AC/Accept eR<sub>X</sub> Renewal

The Response includes information on the eR<sub>X</sub> prescription renewal that the Response was processed for. The renewed R<sub>X</sub> displays in the Active section of the Medication Profile. The R<sub>X</sub> number has an “A” appended to the end, indicating this is the first refill. Subsequent renewals include the next letter of the alphabet appended. (i.e., & 123456 changes to & 123456A after the first refill; for next refill: & 123456A changes to & 123456B)

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc86395705" class="anchor"></span>Figure 4‑25: Renewed R<sub>X</sub> Active

Once the Approved RxRenewal Response is successfully renewed, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc86395706" class="anchor"></span>Figure 4‑26: RxRenewal Response RXC Status in Holding Queue

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc86395707" class="anchor"></span>Figure 4‑27: RxRenewal Response Details Screen

The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc86395708" class="anchor"></span>Figure 4‑28: Corresponding RxRenewal Request – RRC in Holding Queue

Select the record to view the RxRenewal Request details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc86395709" class="anchor"></span>Figure 4‑29: Corresponding RxRenewal Request Details Screen

The \<VP\>, \<VM\>, \<VD\>. and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type. If one of the actions is selected from here, the user receives an error message:

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc86395710" class="anchor"></span>Figure 4‑30: Error - Validate Provider Action Not Available

### Approved with Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Approved with Changes. This indicates the renewal is approved. However, changes must be made prior to renewal.

Depending on the scenario, the RxRenewal Response message may display in the Holding Queue List View screen:

- If changes are only related to only the number of renewals in the Drug segment, the pharmacist does not need to take any action in the Holding Queue, therefore the RxRenewal Response message does not display in the Holding Queue List View.
- If the changes are related to the provider or the provider and number of renewals, the RxRenewal Response displays in the Holding Queue List View because the pharmacist is required to validate the updates.

#### Changes to Number of Renewals Only

When a RxRenewal Response message type is Approved with Changes (for number of renewals only), it does not display in the Holding Queue List View screen. It can be found using \<MV\> Message View or \<SR\> Search. The status of the Approved with Changes RxRenewal Response is “RXP” (RxRenewal Response Processed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc86395711" class="anchor"></span>Figure 4‑31: RXP Status in Holding Queue

The RxRenewal Response details display the RxRenewal Response Message type.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc86395712" class="anchor"></span>Figure 4‑32: RxRenewal Response Details Screen

As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Approved with Changes.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc86395713" class="anchor"></span>Figure 4‑33: RxRenewal Response Information Section

On the OP side, a pending line entry allows for the user to renew the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc86395714" class="anchor"></span>Figure 4‑34: Medication Profile

The Activity Log on the OP side is updated to display the information that a pending response entry was added.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc86395715" class="anchor"></span>Figure 4‑35: R<sub>X</sub> Activity Log 1

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/037.png)

<span id="_Toc86395716" class="anchor"></span>Figure 4‑36: R<sub>X</sub> Activity Log 2

The user may select the pending line entry to renew the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc86395717" class="anchor"></span>Figure 4‑37: Medication Profile – Pending Line Entry

Then, the user may accept the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/039.png)

<span id="_Toc86395718" class="anchor"></span>Figure 4‑38: AC/Accept eR<sub>X</sub> Renewal

The eR<sub>X</sub> on which Renewals were requested and the Response has been processed, is now reinstated with the Response. The renewed R<sub>X</sub> displays in the Active section of the Medication Profile. The R<sub>X</sub> number has an “A” appended to the end, indicating this is the first refill. Subsequent renewals include the next letter of the alphabet appended. (Ex: & 123456 changes to & 123456A after the first refill; for next refill: & 123456A changes to & 123456B).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/040.png)

<span id="_Toc86395719" class="anchor"></span>Figure 4‑39: Renewed R<sub>X</sub> Active in Medication Profile

Once the Approved with Changes RxRenewal Response is successfully renewed, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/041.png)

<span id="_Toc86395720" class="anchor"></span>Figure 4‑40: RxRenewal Response RXC Status in the Holding Queue

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/042.png)

<span id="_Toc86395721" class="anchor"></span>Figure 4‑41: RxRenewal Response Details Screen

The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc86395722" class="anchor"></span>Figure 4‑42: RxRenewal Request RRC in the Holding Queue

Select the record to view the RxRenewal Request details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc86395723" class="anchor"></span>Figure 4‑43: RxRenewal Request Details Screen

The \<VP\>, \<VM\>, \<VD\>. and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type.