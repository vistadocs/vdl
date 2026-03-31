---
consolidated_title: "inbound eprescribing user manual"
app_code: PSO
doc_type: UM
master_source: "Inbound ePrescribing User Manual (Unit 3 Part 2) PSO*7*743"
master_pub_date: May 2024
consolidated_from: 12 versions
prior_versions:
  - "Inbound ePrescribing User Manual (Unit 1) PSO*7*700"
  - "Inbound ePrescribing User Manual (Unit 1 & Unit 2) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 3 Part 1) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 3 Part 2) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 4 Part 1) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 4 Part 2) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 5 Part 1) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 5 Part 2) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 6) PSO*7*581"
  - "Inbound ePrescribing User Manual (Unit 7 Part 1) PSO*7*746"
  - "Inbound ePrescribing User Manual (Unit 7 Part 2) PSO*7*746"
---

## Table of Contents

  - [Manual Validation](#manual-validation)
    - [Validate Patient](#validate-patient)
    - [Validate Provider](#validate-provider)
    - [Validate Drug/SIG](#validate-drugsig)
  - [Accepting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue](#accepting-ersubxsubes-in-the-ersubxsub-holding-queue)
  - [Manual Validation](#manual-validation-1)
  - [Rejecting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue](#rejecting-ersubxsubes-in-the-ersubxsub-holding-queue)
  - [Do Not Fill](#do-not-fill)
  - [Printing in the eR<sub>X</sub> Holding Queue](#printing-in-the-ersubxsub-holding-queue)
  - [Placing eR<sub>X</sub>es on Hold in the eR<sub>X</sub> Holding Queue](#placing-ersubxsubes-on-hold-in-the-ersubxsub-holding-queue)
  - [Un Hold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#un-hold-ersubxsub-in-the-ersubxsub-holding-queue)
  - [Removing eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue](#removing-ersubxsubes-in-the-ersubxsub-holding-queue)
  - [Searching and Sorting in the eR<sub>X</sub> Holding Queue](#searching-and-sorting-in-the-ersubxsub-holding-queue)
    - [Searching eR<sub>X</sub>es](#searching-ersubxsubes)
    - [Sorting eR<sub>X</sub>es](#sorting-ersubxsubes)
  - [Complete Orders from OERR and Patient Prescription Processing](#complete-orders-from-oerr-and-patient-prescription-processing)
---
title: |
  <span id="_Hlk52202211" class="anchor"></span>Pharmacy Reengineering (PRE)
  Inbound ePrescribing (IEP) 5.0
  User Guide
---
![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/001.png)
May 2024
Version 5.0 (Unit 3 Part 2)
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
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
<td>05/20/2024</td>
<td>6.0</td>
<td><p>PSO*7*743:</p>
<ul>
<li><p>Updated notes: <a href="#PSO_7_743_p12"><u>11</u></a>, <a href="#PSO_7_743_p18"><u>11</u></a>, <a href="#PSO_7_743_p22"><u>13</u></a>, <a href="#PSO_7_743_p25"><u>16</u></a>, <a href="#PSO_7_743_p26_2"><u>17</u></a>, <u><a href="#PSO_7_743_p38">28</a>,</u> <a href="#PSO_7_743_p40"><u>29</u></a>, <a href="#PSO_7_743_p32"><u>31</u></a></p></li>
<li><p>Updated figures: <a href="#PSO_7_743_p15"><u>14</u></a>, <a href="#PSO_7_743_Figure_p16"><u>15</u></a>, <a href="#PSO_7_743_Figure_p17"><u>15</u></a>, <a href="#PSO_7_743_Figure_p18"><u>16</u></a>, <a href="#PSO_7_743_Figure_p19_1"><u>17</u></a>, <a href="#_Ref165290406"><u>29</u></a>, <a href="#_Ref165290419"><u>31</u></a>, <a href="#_Toc519780560"><u>33</u></a>, <a href="#_Ref165290453"><u>34</u></a></p></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>11/01/2021</td>
<td>5.0</td>
<td><p>PSO*7.0*617:</p>
<ul>
<li><p>Updated all screen captures with the latest versions</p></li>
<li><p>Included changes related to Controlled Substance and Controlled Substance eRx processing</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
<li><p>Updated Sections <a href="#edit-provider">3.6.2.3</a>, <a href="#accept-provider-validation">3.6.2.4</a>, <a href="#edit-drugsig">3.6.3.3</a>, and <a href="#accept-drugsig-validation">3.6.3.4</a></p></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="odd">
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
<td>Redacted</td>
</tr>
<tr class="even">
<td>05/05/2020</td>
<td>3.0</td>
<td><p>PSO*7.0*610:</p>
<ul>
<li><p>Added note to indicate a minor change in the display of the Station ID drop-down list in the Reports tab</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Redacted <mark></mark></td>
</tr>
<tr class="odd">
<td>03/23/2020</td>
<td>2.9</td>
<td><p>PSO*7.0*590:</p>
<ul>
<li><p>Added production application <strong>URL</strong></p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Redacted <mark></mark></td>
</tr>
<tr class="even">
<td>03/05/2020</td>
<td>2.8</td>
<td><p>PSO*7.0*591:</p>
<ul>
<li><p>Updated Figure 3-44 and 3-45</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td>Redacted <mark></mark></td>
</tr>
<tr class="odd">
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
<td>Redacted</td>
</tr>
<tr class="even">
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
<p>For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in <u>Appendix B: Holding Queue Status Codes &amp; Descriptions</u> in Unit 6 (PSO_7_0_P617_UM_6) available on the Veteran's Documentation Library (VDL).</p>
<ul>
<li><p>eR<sub>X</sub> Default Loopback Days</p></li>
<li><p>Replaced column label “LAST USER” with “LOCKED BY” and updated the description under Table 9</p></li>
<li><p>Added the information for LOCKED BY column in section 3.5.2 Patient Centric View</p></li>
<li><p>Replaced Figure 3-14, Figure 3-16, Figure 3-17, Figure 3-18, Figure 3-19, Figure 3-42, Figure 3-52,<br />
Figure 3-55, Figure 3-56, Figure 3-57, Figure 3-59, Figure 3-60, Figure 3-61, and Figure 3-68 for updated layout</p></li>
<li><p>Added Note and included Figure 3.6‑18 to indicate to the user that a Provider’s DEA# has expired in section 3.6.2.3 Edit Provider</p></li>
<li><p>Removed reference to “Limited Duration” field from Validate Drug/SIG for the modified workflow in section 3.6.3.3 Edit Drug/SIG</p></li>
<li><p>Added description under Note for modified workflow in section 3.6.3.3 Edit Drug/SIG</p></li>
<li><p>Updated description for VistA Days Supply calculation in section 3.6.3.3.1 Additional Field-level Information</p></li>
<li><p>Added scenarios for Quantity/Days Supply workflow under VD Edit screen based on Available Dosage(s) in section 3.6.3.3.2 Quantity/Days Supply work flow under Validate Drug/SIG &gt; Edit:</p></li>
<li><p>Added Note to replace text “Qty Qualifier” with “Code List Qualifier” and replace, “DAW Code” with “Substitutions” in section 3.13 Complete Orders from OERR and Patient Prescription Processing</p></li>
<li><p>Added Note describing eR<sub>X</sub> Date, Date Written, Issue Date, and Written Date fields in section 3.13 Complete Orders from OERR and Patient Prescription Processing</p></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>11/09/2018</td>
<td>2.5</td>
<td><ul>
<li><p>Updated per HPS Review pgs. 55, 57, 87, 88, 90, 92, 194, and 195.</p></li>
<li><p>Updated Cover page to month of November (pg. i)<br />
(TWR, 508 accessibility checks, document is compliant)</p></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>10/24/2018</td>
<td>2.4</td>
<td>Update TOC – Remove Graphic and reran TOC</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>08/27/2018</td>
<td>2.3</td>
<td>Technical Writer Review and 508 accessibility checks</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>08/01/2018</td>
<td>2.2</td>
<td>Updated screenshots and added R<sub>X</sub>Renewal Requests and Responses and CancelR<sub>X</sub> Requests and Responses sections</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>07/28/2018</td>
<td>2.1</td>
<td>Updated screenshots and added 30-day Lookback</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>4/12/2018</td>
<td>2.0</td>
<td>Updated screenshots to include 2.1 changes</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>11/15/2017</td>
<td>1.0</td>
<td><p>Baseline release:</p>
<ul>
<li><p>Updated Table of Figures</p></li>
<li><p>Updates based on feedback from HPS</p></li>
<li><p>Updated screenshots and verbiage throughout the document, formatting, and sections Inbound ePrescribing Workflow and Summary/Details screen, Pharmacy Management section</p></li>
<li><p>Updates made based on changes made during SureScripts Certification and IOC Production Testing</p></li>
</ul></td>
<td>Redacted</td>
</tr>
</tbody>
</table>
This table displays the revision history providing the date, version number and description details.
Table of Contents
List of Figures
1.  
2.  
3.  1.  
    2.  
    3.  
    4.  
    5.  

## Manual Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to accepting a fillable eR<sub>X</sub> \<AC\> and moving the eR<sub>X</sub> to Pending Outpatient Orders file, the VistA patient, provider, and drug/SIG must be validated. The eR<sub>X</sub> is then further processed using Complete Orders from OERR \[PSO LMOE FINISH\] or Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\].

The validation process begins by selecting one of the validate actions from the Summary/Details screen. For training, the sections further will show examples of NewRx processing. The remaining inbound fillable prescriptions follow the same workflow.

> **NOTE:** Before the Drug/SIG on an eR<sub>X</sub> can be manually validated, the eR<sub>X</sub> Patient must have a linked VistA patient. The \<VD\> (Validate Drug/SIG) action has parenthesis around the action to signify this action is not available until a VistA patient is linked, as illustrated in the following figure.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/002.png)

<span id="_Toc167367304" class="anchor"></span>Figure 3.6‑1: Summary/Details Screen Actions

### Validate Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient must be validated before a fillable eR<sub>X</sub> can be accepted. Information about the Patient Validation screen and editing the patient information is described in the following sections.

To validate patient information, type \<VP\> VALDIATE PATIENT from the Summary/Details screen. The Patient Validation screen displays and is described in the following sections.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/003.png)

<span id="_Toc167367305" class="anchor"></span>Figure 3.6‑2: Validate Patient

#### Patient Auto-Match in the Processing Hub

The following outlines the scenarios for a patient auto-match in the IEP Processing Hub before being sent down to VistA:

Patient Match - Primary Hub

1.  MPI Check - receive ICN and SSN from MPI if successful:
1.  If SSN is sent on a NewRx, then the SSN is used in the auto-match with the MPI along with Last Name, First Name, DOB, Gender, Address Line 1, and Home Telephone Number. If Home Telephone Number is not sent, Primary Telephone is used.
2.  If SSN is not sent on the NewRx, then the match is be done with MPI against Last Name, First Name, DOB, Gender, Address Line 1, and Home Telephone Number. If Home Telephone Number is not sent, Primary Telephone is used.
3.  Since only the Last Name, First Name, DOB, and Gender are mandatory on a fillable prescription, the match is done against all the data pieces that are received.
4.  When a patient is successfully matched, the patient registration at the sites is checked.
2.  E&E Check - Then E&E Services is checked to see if the patient is both enrolled and eligible to their system to receive pharmacy benefits (This is done using ICN retrieved from MPI).

Patient Secondary Match in VistA

- Case 1: Patient Auto match successful (MPI record found, E&E check passed, and Patient Site Registration passed).
1.  Use the ICN received from MPI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
2.  If ICN check fails, use the SSN received from MPI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
- Case 2: MPI Match successful but E&E check failed at the Hub:
1.  Use the ICN received from MPI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
2.  If ICN check fails, use the SSN received from MPI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
- Case 3: MPI match unsuccessful at the Hub:
1.  No secondary match.

#### Patient Manual Validation Screen Overview

The header of the Patient Validation screen contains the eR<sub>X</sub> Patient Name and the eR<sub>X</sub> Reference \#. Below the header is the eR<sub>X</sub> and VistA information for the patient, including any known allergies where applicable.

If a match was NOT found for the eR<sub>X</sub> Patient, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with “PATIENT NOT MATCHED” below the Status. No VistA patient information displays.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/004.png)

<span id="_Toc167367306" class="anchor"></span>Figure 3.6‑3: Patient Validation Screen Display - Patient Not Validated/Not Auto Matched

If a match is found, however, the patient has NOT been validated, the Summary/Details screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with VistA information displaying, where applicable.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/005.png)

<span id="_Toc167367307" class="anchor"></span>Figure 3.6‑4: Patient Validation Screen Display - Patient Not Validated/Patient Auto Matched

If the VistA patient has known allergies, verified allergies display in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/006.png)

<span id="_Toc167367308" class="anchor"></span>Figure 3.6‑5: VistA Patient with Known Allergies

If the patient has been validated, the Status field above the VistA Patient contains “VALIDATED”, with the user who performed the validation and date/timestamp.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/007.png)

<span id="_Toc167367309" class="anchor"></span>Figure 3.6‑6: Patient Validated

The actions at the bottom of the Patient Validation screen include:

- \<P\> Print – Prints display of the eR<sub>X</sub> for printing to network or local printer.
- \<H\> Hold – Places an eR<sub>X</sub> on hold.
- \<UH\> Un Hold – Removes an eR<sub>X</sub> from a Hold.
- \<E\> Edit – User edits if the information is empty or incorrect.
- \<AV\> Accept Validation – User accepts the validation if information is correct.
- \<RJ\> Reject – Rejects the eR<sub>X.</sub>

#### Edit Patient

1.  Enter \<E\> Edit to edit the patient information.
2.  If a VistA patient already exists for the eR<sub>X</sub>, the system displays a message confirming the edit.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/008.png)

<span id="_Toc167367310" class="anchor"></span>Figure 3.6‑7: Edit Patient on a VistA Match

3.  If a VistA patient match does not exist, the system prompts to select a patient at the “Select Patient Name” prompt. The partial or full name of the patient, DOB or SSN can be entered.
1.  Select the correct patient and press \<Enter\>.
2.  A message displays confirming the patient selection. Enter \<Y\> Yes.
3.  The select patient information populates the VistA Patient fields on the Patient Validation screen.

> **NOTE:** A Warning Message displays if there is a DOB, Gender, and/or on the patient selected during the edit process.

CS NOTE: For Controlled Substance eRx records, an additional check is performed for the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL for patients residing abroad. If not found, the message below will be displayed.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/009.png)

<span id="_Toc167367311" class="anchor"></span>Figure 3.6‑8: Mismatch Message

#### Accept Patient Validation

Once the patient information has been edited and reviewed for accuracy, the validation needs to be accepted on the Patient Validation screen.

1.  Select \<AV\> Accept Validation on the Patient Validation screen to accept the provider validation.
2.  A message displays confirming whether to mark the patient as validated. Enter \<Y\> Yes.

If the validation is successful, a message displays indicating that the validation was updated.

The Status changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/timestamp.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/010.png)

<span id="_Toc167367312" class="anchor"></span>Figure 3.6‑9: Confirm Acceptance of Patient Validation

A “\[v\]” displays to the right of the VistA Patient field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/011.png)

<span id="_Ref5967556" class="anchor"></span>Figure 3.6‑10: Patient Validation Complete: Summary/Details Screen Indicator

CS NOTE: For Controlled Substance eRx records, the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE for patients residing abroad will be required. If not found, the message below will be displayed and the user will not be able to proceed with the Validation as shown below.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/012.png)

<span id="_Toc167367314" class="anchor"></span>Figure 3.6‑11: Patient Validation Unable To Validate Address Warning

#### Automatic Patient Validation

When a patient validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub>es in the Holding Queue for the same patient, received on the same day, a message displays asking if the patient validation should be applied to the other eR<sub>X</sub>es. Refer to Figure 3.6‑12. If the user selects \<Y\> Yes, the system links and applies the patient validation for the eR<sub>X</sub>es currently in the Holding Queue for that patient.

> **NOTE:** Automatic Patient Validation is only available for NewRx.

The determination of the same patient is based on unique records from the ERX EXTERNAL PATIENT file (#52.46). The system only validates the same patients on eR<sub>X</sub>es that are currently in the ERX HOLDING QUEUE file (#52.49) received at the time of the automatic patient validation. Patient validation is not applied for eR<sub>X</sub>es received for that patient after the auto validation is applied. For example, if VA receives six eR<sub>X</sub>es for the same patient on the same day, the user only has to validate the patient once. If eR<sub>X</sub>es are received later that same day, those eR<sub>X</sub>es need to be revalidated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/013.png)

<span id="_Ref53477014" class="anchor"></span>Figure 3.6‑12: Automatic Patient Validation

To apply patient validation to other eR<sub>X</sub>es in the Holding Queue for the same patient, received on the same day:

1.  The system asks the user if the previous validation should be applied to the other eR<sub>X</sub>es received for the patient.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/014.png)

<span id="_Toc167367316" class="anchor"></span>Figure 3.6‑13: Apply Patient Validation to Other eR<sub>X</sub>es

4.  Enter Y for Yes to apply the validation to the other eR<sub>X</sub>es for the patient. After selecting Yes, the patient validation is applied to the other eR<sub>X</sub>es. As previously noted, any eR<sub>X</sub>es received after this action will not be validated.
3.  A message displays indicating that the validation was updated.
5.  A “\[v\]” displays to the right of the VistA Patient field on the Summary/Details screen and the Status field changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/timestamp. This occurs for all the eR<sub>X</sub>es validated via the automatic patient validation process.
6.  The statuses on all eR<sub>X</sub>es validated by the automatic patient validation process changes to “I” for In Process.

> **NOTE:** When doing a batch validation for a patient, it is possible that one or more of the records for the patient is for Controlled Substance which requires the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE if they reside abroad. So, a check will be performed for such records and if the requirement is not fulfilled, the record will not be validated. The message below will be displayed for each record with this issue:

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/015.png)

<span id="_Toc167367317" class="anchor"></span>Figure 3.6‑14: Patient Validation Unable To Validate Address Warning

### Validate Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provider must be validated before a fillable eR<sub>X</sub> can be accepted.

To validate provider information, from the Summary/Details screen, type \<VM\> VALIDATE PROVIDER. The eR<sub>X</sub> Provider Validation screen displays.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/016.png)

<span id="_Toc167367318" class="anchor"></span>Figure 3.6‑15: Summary/Details Screen Action - Validate Provider

Information about the Validate Provider display and editing the provider information is described in the following sections.

#### Provider Auto-Match in the Processing Hub

The auto-match on an external provider is based upon the NPI of the prescriber coming in on the new eR<sub>X</sub>. The NPI is matched against the VistA instance’s NEW PERSON file (#200) entry. If the NPI matches and if the Provider is marked “Authorized to Write Meds” that is considered as a match. Upon successful match, the VistA provider is linked with the incoming provider’s record in VistA.

#### Provider Manual Validation Screen Overview

The header of the Provider Validation screen contains the eR<sub>X</sub> Patient Name and the eR<sub>X</sub> Reference \#. Below the header is the eR<sub>X</sub> and VistA information for the provider, where applicable.

If a match was NOT found for the eR<sub>X</sub> provider, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with “PROVIDER NOT MATCHED” below the Status. No provider information displays.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/017.png)

<span id="_Toc167367319" class="anchor"></span>Figure 3.6‑16: Provider Not Auto Matched / Not Validated

#### Edit Provider

To edit the provider information:

1.  Press the \<E\> Edit action on the Provider Validation screen.
2.  If no VistA provider information is in the system for the eR<sub>X</sub>, the “Select Provider Name” prompt displays for searching for and selecting a provider.
1.  Enter either the partial name or full name of the provider or the NPI of the Provider, or DEA of the Provider at the “Select Provider Name” prompt. If multiple providers exist with the same name exist, a list of providers is provided with additional identifying information (e.g., middle initial, mail code, and title, where applicable, etc.).
2.  Select the provider.
3.  If a VistA provider is currently linked for the eR<sub>X</sub>, the system asks if the current provider should be modified.
1.  Enter \<Y\> Yes.
2.  Enter either the partial name or full name of the provider at the “Select Provider Name” prompt.
3.  Select the provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/018.png)

<span id="_Toc167367320" class="anchor"></span>Figure 3.6‑17: Modify Current VistA Provider

4.  Once the VistA provider is selected, the VistA provider fields populate on the Provider Validation screen, along with information whether the DEA of the Provider has expired or not.
5.  The next step in the provider validation process is to accept the validation, which is described in the next section.

<span id="PSO_7_743_p12" class="anchor"></span>NOTE: The text, “Expired”, displays when the DEA \# of the selected VistA Provider has expired in File \#8991.9.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/019.png)

<span id="_Ref5968279" class="anchor"></span>Figure 3.6‑18: Select Provider Warning for Expired DEA#

<span id="PSO_7_743_p18" class="anchor"></span>CS NOTE: The following message displays upon selecting the Provider if the date of the Provider’s matching DEA \# is expired.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/020.png)

<span id="_Toc167367322" class="anchor"></span>Figure 3.6‑19: Select Provider DEA Expiration Date Message

CS NOTE: The following block message displays upon selecting the Provider if the Provider’s eRx DEA number is missing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/021.png)

<span id="_Toc167367323" class="anchor"></span>Figure 3.6‑20: Select Provider Missing DEA Number Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Provider does not have a valid DEA number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/022.png)

<span id="_Toc167367324" class="anchor"></span>Figure 3.6‑21: Select VistA Provider Missing DEA Number Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the eRx Provider does not have a valid DEA number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/023.png)

<span id="_Toc167367325" class="anchor"></span>Figure 3.6‑22: Select eRx Provider Missing DEA Number Warning Message

<span id="PSO_7_743_p22" class="anchor"></span>CS NOTE: The following warning message displays upon selecting the Provider if the VistA Provider does not have a DEA number on file matching the eRx Provider’s DEA number.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/024.png)

<span id="_Toc167367326" class="anchor"></span>Figure 3.6‑23: Select Provider DEA Number Mismatch Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Drug selected is a Controlled Substance, but the VistA Provider’s DEA number matching the eRx Provider’s DEA number is not authorized to write medication orders for the DEA Schedule of the Drug.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/025.png)

<span id="_Toc167367327" class="anchor"></span>Figure 3.6‑24: Select VistA Provider Not Authorized Warning Message

#### Accept Provider Validation

Once the correct provider has been selected and reviewed for accuracy, the next step is to accept the validation using the following steps.

1.  Select \<AV\> ACCEPT VALIDATION on the Provider Validation screen to accept the provider validation.

> **NOTE:** The following warning message displays upon selecting the validation if there is a DEA \# and/or NPI mismatch.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/026.png)

<span id="PSO_7_743_p15" class="anchor"></span>Figure 3.6‑25: Accept Provider Validation Warning Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s Vista DEA number is missing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/027.png)

<span id="PSO_7_743_Figure_p16" class="anchor"></span>Figure 3.6‑26: Accept Provider Validation Missing VistA DEA Number Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s not authorized to write a scheduled Controlled Substance prescription.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/028.png)

<span id="PSO_7_743_Figure_p17" class="anchor"></span>Figure 3.6‑27: Accept Provider Validation Not Authorized Message

<span id="PSO_7_743_p25" class="anchor"></span>CS NOTE: The following warning message displays upon selecting the validation if the eRx Provider does not have a valid DEA number and the Drug is not selected or the Drug selected is a Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/029.png)

<span id="_Toc167367331" class="anchor"></span>Figure 3.6‑28: Select eRx Provider Missing DEA Number Warning Message

> **NOTE:** The following warning message displays upon selecting the validation if the VistA Provider does not have a valid DEA number on file and Drug is not selected or Drug selected is a Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/030.png)

<span id="PSO_7_743_Figure_p18" class="anchor"></span>Figure 3.6‑29: Select VistA Provider Missing DEA Number Warning Message

<span id="PSO_7_743_p26_2" class="anchor"></span>NOTE: The following block message displays upon selecting the validation if the eRx Provider’s DEA number does not match the VistA DEA number and Drug is not selected or Drug selected is a Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/031.png)

<span id="PSO_7_743_Figure_p19_1" class="anchor"></span>Figure 3.6‑30: Select Provider DEA Mismatch Message

CS NOTE: The following block message displays upon selecting the validation if the VistA Drug selected is a Controlled Substance, but the VistA Provider is not authorized to write for the Schedule of the Drug.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/032.png)

<span id="PSO_7_743_Figure_p19_2" class="anchor"></span>Figure 3.6‑31: Select Provider Not Authorized Message

A message displays confirming whether to mark the provider as validated.

2.  Enter \<Y\> Yes.
3.  If the validation is successful, a message displays indicating that the validation was updated. Type \<Enter\> to continue or \<Shift\><sub>+</sub>\<^\> to Quit.

> **NOTE:** If there are other eR<sub>X</sub>es for the patient written by the same provider and received on the same day for that patient, a message displays asking if the provider validation should be applied to those eR<sub>X</sub>es. Refer to section <u>3.6.2.5 Automatic Provider Validation</u> for more information.

- The Status field changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/timestamp displays to the right of “VALIDATED”.
- A “\[v\]” displays to the right of the VistA Provider field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/033.png)

<span id="_Toc167367335" class="anchor"></span>Figure 3.6‑32: Before Provider Validation (Validate Provider Screen)

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/034.png)

<span id="_Toc167367336" class="anchor"></span>Figure 3.6‑33: After Provider Validation (Validate Provider Screen)

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/035.png)

<span id="_Ref5967567" class="anchor"></span>Figure 3.6‑34: After Provider Validation (Summary/Details Screen)

#### Automatic Provider Validation

When a provider validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub>es in the Holding Queue for the same patient by the same provider, received on the same day, a message displays asking if the other eR<sub>X</sub>es for the patient written by the provider should be validated. If the user selects \<Y\> Yes, the system links and applies the provider validation for the eR<sub>X</sub>es currently in the Holding Queue for the patient by the same provider.

> **NOTE:** Automatic Provider Validation is available only for NewRx.

The determination of the same provider is based on unique records from the ERX EXTERNAL PERSON file (#52.48). The system only validates the same provider on eR<sub>X</sub>es that are currently in the ERX HOLDING QUEUE file (#52.49) for the same patient received on the same date. Provider validation is not applied for the same provider received after the auto validation is applied once. For example, if VA receives six eR<sub>X</sub>es for the same patient on the same day from the same provider, the user only has to validate the provider once; however, if eR<sub>X</sub>es are received after the automatic provider validation is applied (e.g., later that same day by that provider), the provider for those eR<sub>X</sub>es needs to be validated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/036.png)

<span id="_Toc167367338" class="anchor"></span>Figure 3.6‑355: Automatic Provider Validation

To apply the provider validation to the other eR<sub>X</sub>es enter \<Y\> Yes. A message displays indicating that the validation was updated.

- The Status field on all the eR<sub>X</sub>es, where the provider validation has been applied, changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/timestamp displays to the right of “VALIDATED”.
- A “\[v\]” displays to the right of the VistA Provider field on the Summary/Details screen.
- The statuses on all eR<sub>X</sub>es validated by the automatic provider validation process changes to “I” for In Process.

### Validate Drug/SIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The drug/SIG information on the eR<sub>X</sub> must be validated before a fillable eR<sub>X</sub> can be accepted.

> **NOTE:** A VistA patient must be linked (matched) before the Validate Drug/SIG action is available.

To validate drug/SIG information for the eR<sub>X</sub>, type \<VD\> Validate Drug/SIG from the Summary/Details screen. The Drug Validation screen displays and is described in the following sections.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/037.png)

<span id="_Toc167367339" class="anchor"></span>Figure 3.6‑36: Validate Drug / SIG

#### Drug Auto-Match in the Processing Hub

The pre-conditions for a drug auto-match in the Processing Hub are that the drug should be a one-to-one match, should not be a Compound, not a Controlled Substance, should be Active, not Investigational and should be marked for Outpatient use in the local DRUG file (#50).

First, the drug description on the new eR<sub>X</sub> is matched against the Drug Generic Name entry in the VistA instance’s DRUG file (#50). If successful, the match stops right here, and the drug is linked in VistA.

If the match is not successful, the drug description is then matched against the VA Product Name entry in the VistA instance’s VA PRODUCT file (#50.68). Then a drug in local file for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

If the match is not successful, the NDC is used to match against the VistA instance’s NDC/UPN file (#50.67). Using the VA Product Name identified at this step, a drug in the local file for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

> **NOTE:** The NDC is an optional field and may or may not be included with the new eR<sub>X</sub>. For a supply, if UPC is sent, it is not matched against the NDC/UPN file (#50.67). Only the Drug Description match is attempted.

#### Drug/SIG Manual Validation Screen Overview

The header of the Drug/SIG Validation screen contains the eR<sub>X</sub> Patient Name and the eR<sub>X</sub> Reference \#. Below the header is the eR<sub>X</sub> and VistA information for the drug/SIG, where applicable.

If a match was NOT found for the VistA drug, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with “NOT MATCHED” to the right of the VistA Drug field. The other VistA drug/SIG fields may or may not be populated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/038.png)

<span id="_Ref5967579" class="anchor"></span>Figure 3.6‑37: Drug Validation Screen Display - VistA Drug Not Validated / Not Auto Matched

If a VistA match was found for the drug, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with VistA drug/SIG information displaying in the VistA Drug field (#1).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/039.png)

<span id="_Ref5967587" class="anchor"></span>Figure 3.6‑38: Drug Validation Screen Display - VistA Drug Matched / Not Validated

#### Edit Drug/SIG

1.  To edit the drug/SIG information, use the \<E\> Edit action on the Drug Validation screen.
2.  If the VistA drug/SIG information has been linked for the eR<sub>X</sub>, the edit drug/SIG sequence prompts the user to select a field or select All fields.
    - Select Item (s): Quit// \<E\> Edit
    - Which fields (s) would you like to edit? (1-10) or “A” 11: A//
3.  Under eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit, if a drug is already matched in the hub, that drug is displayed at the “select” prompt. The user is still allowed to change the drug by entering the drug name.
7.  Under eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit, if a drug is not matched in the hub, at the “select” prompt, it is blank wherein the user can enter the drug name.
8.  When a Yes/No confirmation is asked for the selected drug, if the user hits enter or selects “No”, the control comes out of Edit mode back to VD screen.

> **NOTE:** The eR<sub>X</sub> Drug/SIG information from the external provider displays throughout the edit drug/SIG process as reference.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/040.png)

<span id="_Ref5967596" class="anchor"></span>Figure 3.6‑39: eR<sub>X</sub> Display during Edit Drug / SIG

9.  Next, enter the Dosage. Either enter a free text dose or enter a question mark \<?\> to view a list of available dosages. The system prompts the user to confirm the selected dosage.
1.  Enter the Verb, Route, and Schedule.
2.  Patient Instructions are default/consistent instructions that come from the Orderable Item. VA Patient Instructions are auto populated when either a drug is auto matched or manually matched, or the drug’s Pharmacy Order Item has an entry for those instructions. If it is blank, enter VA Patient Instructions. Or if it needs to be edited, use the Replace function. Even abbreviated Patient Instructions from Medication Instruction files are allowed, which expand upon saving. This field holds the patient instructions for an eR<sub>X</sub>. This field is transferred to the Pending Queue upon acceptance of an eR<sub>X</sub>.
3.  Provider Comments are additional free text comments that the provider may enter. The VA Provider Comments field contains the eR<sub>X</sub> Notes from the external provider and can be edited by entering \<Replace\>. Even abbreviated Provider Comments from Medication Instruction files are allowed, which expand upon saving. This field is transferred to the Pending Queue upon acceptance of an eR<sub>X</sub>.
4.  Enter Patient Status and edit the Patient Status as required.
5.  Enter/edit VistA Quantity, VistA Days Supply, and VistA Renewals as needed.

> **NOTE:** The Vista Days Supply prompt is pre-populated with an auto-calculated value given to the user as a suggested value for the Days Supply prompt. This value is displayed as \[DAYS SUPPLY:(1-90): 90//\], with suggested value behind two forward slashes. This value is derived from the values entered by the user in the Quantity prompt, the Units Per Dose prompt, and the Schedule prompt. The auto-calculated value is the result of dividing the Quantity by the Units Per Dose, then dividing the resulting value by the Schedule (Units Per Dose/Quantity/Schedule). This auto-calculated value is only a suggested entry for the user. The user can enter any amount that fits within the Days Supply range supplied by the eRX software.

When editing the Quantity field after the VistA drug has been linked, the Vista Quantity prompt is pre-populated with an auto-calculated value as a suggested value to the user. This value is displayed as \[QTY:(1-90): 90//\], with the suggested value behind two forward slashes. This value is derived from the values entered by the user in the Days Supply prompt, the Units Per Dose prompt, and the Schedule prompt. The auto-calculated value is the result of dividing the Days Supply by the Units Per Dose, then dividing the resulting value by the Schedule (Units Per Dose/Days Supply/Schedule). This auto-calculated value is only a suggested entry for the user. The user can enter any amount that fits within the Quantity range supplied by the eRX software.

6.  Enter Routing. Either \<M\> for Mail or \<W\> for Window.
7.  The system displays the Default eR<sub>X</sub> Clinic setup by the site. If it is not configured, this field is blank. The user can select a clinic as required in either case.

> **NOTE:** Setting up the Default eR<sub>X</sub> Clinic is optional. Sites are encouraged to edit their OUTPATIENT SITE file (#59) to define the default eR<sub>X</sub> clinic. The following field is added to the OUTPATIENT SITE file (#59): DEFAULT ERX CLINIC field (#10).

Please reference the Implementation Guide – Inbound ePrescribing (PSO\*7.0\*p581) on the VA Documentation Library (VDL) at the following link for details on setting up the default eR<sub>X</sub> clinic for a site.

Outpatient Pharmacy VDL URL: <https://www.va.gov/vdl/application.asp?appid=90>

8.  Once all the drug/SIG fields have been edited and the drug/SIG sequence is complete, the edited information displays on the Drug Validation screen.
9.  The next step is to accept the validation \<AV\>, which is described in the next section.
10. If you have to edit after this, you can pick the fields:
    - Select Item (s): Quit// E Edit
    - Which fields (s) would you like to edit? (1-10) or “A” 11: A//

> **NOTE:** If the Default eR<sub>X</sub> Clinic is changed from the one that is configured with the NPI Institution, of the receiving Pharmacy, the eR<sub>X</sub> may not show up in OERR when processed. Refer to the Implementation Guide – Inbound ePrescribing (PSO\*7.0\*p581) on the VA Documentation Library (VDL) for details on setting up the Default eR<sub>X</sub> Clinic for a site.

CS NOTE: The following block message displays upon selecting the Drug validation if the Provider’s not authorized to write a scheduled Controlled Substance prescription.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/041.png)

<span id="_Toc167367343" class="anchor"></span>Figure 3.6‑40: Select Provider Not Authorized Message

CS NOTE: The following block message displays upon selecting the Drug validation if the eRx is Non-Controlled Substance and the VistA drug is a Controlled Substance. The Accept Validation will be blocked.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/042.png)

<span id="_Toc167367344" class="anchor"></span>Figure 3.6‑41: Blocked Accept Validation Message

CS NOTE: The following warning message displays upon selecting an eRx that is a Controlled Substance, but the VistA drug selected is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/043.png)

<span id="_Toc167367345" class="anchor"></span>Figure 3.6‑42: Drug Validation Warning Message

CS NOTE: The following block message displays upon selecting an eRx that is not digitally signed and the VistA drug is a Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/044.png)

<span id="_Toc167367346" class="anchor"></span>Figure 3.6‑43: Drug Validation eRx without DS Message

> **NOTE:** The following block message displays upon selecting an eRx that is digitally signed and the VistA drug is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/045.png)

<span id="_Toc167367347" class="anchor"></span>Figure 3.6‑44: Drug Validation eRx without DS Message

CS NOTE: The following block message displays upon selecting an eRx that doesn’t have a valid DEA number on file for the eRx Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/046.png)

<span id="_Toc167367348" class="anchor"></span>Figure 3.6‑45: Drug Validation eRx with Invalid eRx Provider DEA Number Message

CS NOTE: The following block message displays upon selecting an eRx that doesn’t have a valid DEA number on file for the VistA Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/047.png)

<span id="_Toc167367349" class="anchor"></span>Figure 3.6‑46: Drug Validation eRx with Invalid VistA Provider DEA Number Message

> **NOTE:** The following block message displays upon selecting an eRx that has a mismatched DEA number on file for the Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/048.png)

<span id="_Toc167367350" class="anchor"></span>Figure 3.6‑47: Drug Validation eRx with Provider DEA Number Mismatch Message

<span id="PSO_7_743_p38" class="anchor"></span>CS NOTE: The following warning message displays upon selecting an eRx that was written or issued after the VistA Provider’s matching DEA number has expired.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/049.png)

<span id="_Toc167367351" class="anchor"></span>Figure 3.6‑48: Drug Validation eRx Written After VistA Provider DEA Expiration Warning Message

CS NOTE: The following warning message displays upon selecting an eRx that does not have a valid VistA Provider authorization to write the drug schedule.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/050.png)

<span id="_Toc167367352" class="anchor"></span>Figure 3.6‑49: Drug Validation eRx VistA Provider Not Authorized Warning Message

<span id="PSO_7_743_p40" class="anchor"></span>CS NOTE: The following warning message displays upon selecting an eRx that is written/issued after the expiration date of the VistA Provider’s matching DEA number.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/051.png)

<span id="_Ref165290406" class="anchor"></span>Figure 3.6‑50: Drug Validation eRx VistA Provider Not Authorized Warning Message

#### Additional Field-level Information:

- Quantity Unit of Measure is displayed in the eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit, along with the reference eR<sub>X</sub> information.
- eR<sub>X</sub> Quantity displays up to 5 digits after the decimal in the eR<sub>X</sub> Holding Queue Summary/Details screen and VD \> Edit screen.
- VistA Quantity is displayed same as eR<sub>X</sub> Quantity if there are 2 digits after decimal places. If there are more than 2 digits after decimal places, VistA Quantity field is left blank so that the user can key in.
- eR<sub>X</sub> Days Supply displays up to 999 in the eR<sub>X</sub> Holding Queue Summary/Details screen and VD \> Edit screen.
- VistA Days Supply is auto-calculated based on Units Per Dose, Quantity, and Schedule values. User can also key in a desired value in this field.
- eR<sub>X</sub> Renewals displays up to 99 in the eR<sub>X</sub> Holding Queue Summary/Details screen and VD \> Edit screen.
- VistA Renewals allows a value between 0 and 11 only.
- VistA Renewals is auto-populated based on Dispensing Units, Quantity, and Days Supply values.
- Help text for VistA Quantity is under eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit.

#### Quantity/Days Supply Work Flow under Validate Drug/SIG \> Edit:

Scenario 1: The updated Quantity/Days Supply work flow works in the holding queue for only available dosages such as 40MG, 80MG and so on. The Quantity divided by schedule is then divided by units per dose to provide the Days Supply value.

> Available Dosage(s):

> 1\. 40MG

> 2\. 80MG

Scenario 2: Quantity/Days Supply auto-calculation does not function for available dosages such as SMALL AMOUNT/LIBERAL AMOUNT, DROP/DROPS, TEASPOONFUL, PATCH etc. For these available dosages, Holding queue VD screen works similar to CPRS, not auto-calculating Days Supply based on Quantity, Schedule, and Units per dose.

> There are 2 Available Dosage(s):

> 1\. 1 DROP

> 2\. 2 DROPS

> There are 4 Available Dosage(s):

> 1\. 1 TEASPOONFUL

> 2\. 2 TEASPOONFULS

> 3\. 1 TABLESPOONFUL

> There are 3 Available Dosage(s):

> 1\. LIBERAL AMOUNT

> 2\. SMALL AMOUNT

> 3\. MODERATE AMOUNT

Scenario 3: Quantity/Days Supply auto-calculation does not function for drugs when there are no available dosages. Holding queue VD screen works similar to CPRS, not auto-calculating Days Supply based on Quantity, Schedule, and Units per dose.

> There are NO Available Dosage(s).

> Please Enter a Free Text Dose:

#### Accept Drug/SIG Validation

Once the VistA Drug/SIG information has been edited and reviewed for accuracy, the next step is to accept the validation \<AV\> on the Drug Validation screen. The system prompts the user to confirm the validation. After entering \<Y\> Yes, a message displays that the drug validation has been updated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/052.png)

<span id="_Toc167367354" class="anchor"></span>Figure 3.6‑51: Confirm Acceptance of Drug / SIG Validation

CS NOTE: The following block message displays upon selecting an eRx that does not have a valid VistA Provider authorization to write the drug schedule.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/053.png)

<span id="_Toc167367355" class="anchor"></span>Figure 3.6‑52: Drug Accept Validation eRx VistA Provider Not Authorized Block Message

<span id="PSO_7_743_p32" class="anchor"></span>CS NOTE: The following block message displays upon selecting an eRx that is written/issued after the expiration date of the VistA Provider’s matching DEA number.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/054.png)

<span id="_Ref165290419" class="anchor"></span>Figure 3.6‑53: Drug Accept Validation eRx VistA Provider Not Authorized Block Message

The Status changes to “VALIDATED” on the Drug Validation screen, along with the user who performed the validation and date/timestamp. “\[v\]” also displays to the right of the VistA Drug field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/055.png)

<span id="_Ref5967604" class="anchor"></span>Figure 3.6‑54: Drug / SIG Validation Complete (Validate Drug / SIG Screen)

The modified VistA Drug/SIG information populates on the Drug/SIG Validation screen.

Press \<Enter\> to display Pages 2 and 3 of the Drug/SIG Validation screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/056.png)

<span id="_Ref5967613" class="anchor"></span>Figure 3.6‑55: Drug / SIG Validation Complete (Summary/Details Screen)

#### Wait Status Flag “W”

When the user completes validating Patient, Provider and Drug/SIG for an eR<sub>X</sub>, the status of the prescription changes from “I” In Process to “W” Wait in the Holding Queue’s list view.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/057.png)

<span id="_Ref5967623" class="anchor"></span>Figure 3.6‑56: eR<sub>X</sub> Holding Queue Summary/Details Screen with Validations Complete

“W” can now be seen in the status column.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/058.png)

<span id="_Toc519780560" class="anchor"></span>Figure 3.6‑57: eR<sub>X</sub> Holding Queue List View with eR<sub>X</sub> Record in “W” Status

## Accepting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conditions must be met, before a fillable eR<sub>X</sub> can be accepted and transmitted to the Pending Queue for further processing:

1.  The eR<sub>X</sub> cannot be on Hold. If the eR<sub>X</sub> is on Hold, the eR<sub>X</sub> status on the Holding Queue List has one of the Hold Status codes, and the Hold Status, Hold Reason, and the user who placed the eR<sub>X</sub> on hold is displayed on the Summary/Details screen.
10. The eR<sub>X</sub> cannot have a status of “Rejected” RJ, “Removed” RM, “Processed” PR or “Canceled” CAN/CXQ.

All validation steps, for patient, provider, and drug/SIG must be completed, including the \<AV\> Accept Validation action on the validate screens. For additional information on the validation steps, refer to section User Manual Unit 1 (PSO_7_0_P617_UM_1_2) available on the Veteran's Documentation Library (VDL).

## Manual Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user attempts to accept an eR<sub>X</sub> where one or more of the conditions have not been met, an error message displays indicating that the eR<sub>X</sub> cannot be processed and the reason.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/059.png)

<span id="_Toc167367361" class="anchor"></span>Figure 3.8‑1: Accept eR<sub>X</sub> - Sample Validation Errors

After all the above pre-conditions have been met, to Accept an eR<sub>X</sub> \<AC\> from the Summary/Details screen, complete the following steps.

From the Summary/Details screen, type \<AC\> Accept eR<sub>X</sub>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/060.png)

<span id="_Ref165290453" class="anchor"></span>Figure 3.8‑2: Accept eR<sub>X</sub>es

A message displays notifying the user that the eR<sub>X</sub> was sent to Pending Outpatient Orders for further processing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/061.png)

<span id="_Ref165290444" class="anchor"></span>Figure 3.8‑3: eR<sub>X</sub>es Sent to Pending Outpatient Orders

The user can then go to Complete Orders from OERR or Patient Prescription Processing to view the eR<sub>X</sub> information. Refer to section <u>3.16 Complete Orders from OERR and Patient</u> Prescription Processing.

Complete Orders from OERR and Patient Prescription Processing.

> **NOTE:** RxVerify messages are stored in the Hub for reporting purposes only. Unlike in the past, no NCPDP message will be sent back to the originating EHR system indicating that eR<sub>X</sub> has been accepted.

CS NOTE: All Controlled Substance prescriptions checks for Patient, Provider, and Drug are re-performed at Accept eRx and any issues will prevent the eRx from being accepted.

## Rejecting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reject is used to remove a fillable eR<sub>X</sub> from the eR<sub>X</sub> Holding Queue. Reject must be accompanied by a reject code/reason.

> **NOTE:** Reject messages are stored in the Hub for reporting purposes only. Unlike in the past, no NCPDP message will be sent back to the originating EHR system indicating that eR<sub>X</sub> has been rejected.

To reject an eR<sub>X</sub>, complete the following steps:

1.  From the Summary/Details screen, type \<RJ\> Reject.
2.  Enter \<Y\> Yes to confirm the reject.
3.  Enter a reason for the rejection. The following reasons are available:
    - PTT01 – Patient not eligible
    - PTT02 – Cannot resolve patient
    - PVD01 – Provider not eligible
    - PVD02 – Cannot resolve provider
    - DRU01 – Not eligible for renewals
    - DRU02 – Non-formulary drug
    - DRU03 – Duplicate prescription found for this patient
    - DRU04 – Invalid quantity
    - DRU05 – Duplicate therapeutic class
    - DRU06 – Controlled substances are disallowed
    - ERR01 – Multiple errors, please contact the pharmacy
    - ERR02 – Incorrect pharmacy
    - ERR03 – Issues with prescription, please contact the pharmacy
    - PVD03 – Missing/bad digital signature on inbound CS ERX
    - PVD04 – Prescriber’s CS credential is not appropriate
    - PTT03 – Patient’s mailing address is missing/mismatched
    - ERR99 - Other
4.  Type additional comments as to why the eR<sub>X</sub> is being rejected and press \<Enter\>. These comments are optional.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/062.png)

<span id="_Toc167367364" class="anchor"></span>Figure 3.9‑1: Rejecting an eR<sub>X</sub>

Once the eR<sub>X</sub> is rejected, the details of the reject message are available in the IEP Processing Hub as reference. Refer to Figure 3.9‑2.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/063.png)

<span id="_Ref53479128" class="anchor"></span>Figure 3.9‑2: Reject Message in Processing Hub

## Do Not Fill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a Controlled Substance record contains a value of ‘E’, the following message will display to inform the user that this is a DO NOT FILL record per the Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/064.png)

<span id="_Toc167367366" class="anchor"></span>Figure 3.10‑1: eRx has Do Not Fill Indicator Per Provider

The user will be prompted to select REMOVE or REJECT actions.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/065.png)

<span id="_Toc167367367" class="anchor"></span>Figure 3.10‑2: Do Not Fill Error Message

## Printing in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Summary/Details screen and from any of the validate screens, the \<P\> Print action is available to print the eR<sub>X</sub>. \<P\> Print action is available for all records in the Holding Queue.

1.  Enter \<P\> Print.
2.  Enter the Device (local or network printer) and press \<Enter\>.

The print display of the eR<sub>X</sub> prints to the selected printer.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/066.png)

<span id="_Ref5967635" class="anchor"></span>Figure 3.11‑1: Print Display of Non-Controlled Substance eR<sub>X</sub>

| ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/067.png)![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/068.png)![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/069.png) |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc167367369" class="anchor"></span>Figure 3.11‑2: Print Display of Controlled Substance eR<sub>X</sub>

## Placing eR<sub>X</sub>es on Hold in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fillable eR<sub>X</sub> can be placed on hold for several reasons indicating that there is an issue with the eR<sub>X</sub>.

1.  To place an eR<sub>X</sub> on hold, type \<H\> Hold from the Summary/Details screen or any of the validate screens.
2.  Enter a hold reason from the available reasons. The following reasons are available:
- HPT – PATIENT NOT FOUND
- HPD – PROVIDER NOT FOUND
- HNF – NON-FORMULARY DRUG THAT NEEDS APPROVAL
- HSO – INSUFFICIENT STOCK
- HDI – DRUG-DRUG INTERACTION
- HAD – ADVERSE DRUG INTERACTION
- HBA – BAD ADDRESS
- HPC – PROVIDER CONTACTED
- HPA – PRIOR APPROVAL NEEDED
- HOR – OTHER REASON
- HPP – PATIENT CONTACTED
- HPR – HOLD DUE TO PATIENT REQUEST
- HQY – QUANTITY OR REFILL ISSUE
- HCR – PRESCRIBER’S CS CREDENTIAL IS NOT APPROPRIATE
- HWR – CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS
- HIS – PROVIDER DEA# ISSUE
- HRX – HOLD FOR RX EDIT
- HDE – DRUG USE EVALUATION
- HTI – THERAPUTIC INTERCHANGE
3.  To view the available hold reasons, enter a double question mark \<??\> at the “Select HOLD reason code” prompt, refer to Figure 3.12‑1. The available hold reasons display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/070.png)

<span id="_Ref53479810" class="anchor"></span>Figure 3.12‑1: Hold eR<sub>X</sub>

11. Enter the reason code at the “Select HOLD Reason code:” prompt and press \<Enter\>.
12. A prompt displays asking for additional comments on the reason for the hold. These comments are optional. Either press \<Enter\> to complete the hold process or add comments and then press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/071.png)

<span id="_Toc167367371" class="anchor"></span>Figure 3.12‑2: Select Hold Reason Code

The Hold Status, Hold Reason, and the user placing the eR<sub>X</sub> on hold display below the VistA Drug section on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/072.png)

<span id="_Toc167367372" class="anchor"></span>Figure 3.12‑3: Hold Status and Reason

The hold status also displays in the “Status” column (STA) on the Holding Queue List screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/073.png)

<span id="_Toc167367373" class="anchor"></span>Figure 3.12‑4: Hold Status in Status Column

> **NOTE:** When a fillable eR<sub>X</sub> is put on ‘Hold’ the only actions available for the user are UH/Un Hold, P/Print and SH/Status History.

## Un Hold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eR<sub>X</sub>es may be removed from a hold by typing \<UH\> Un Hold. Users who see the Un Hold function in parentheses “()” are not able to remove an eR<sub>X</sub> from a hold.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/074.png)

<span id="_Toc167367374" class="anchor"></span>Figure 3.13‑1: Un Hold eR<sub>X</sub>

> **NOTE:** When a user exercises Un Hold option on a NewR<sub>X</sub> record that is in one of the Hold statuses, if all the 3 validations (Patient, Provider, and Drug/SIG) are complete, the eR<sub>X</sub> record’s status changes to “W” (Wait). When a user exercises Un Hold option on a NewR<sub>X</sub> record that is in one of the Hold statuses, if all the 3 validations (Patient, Provider, and Drug/SIG) are not complete, the eR<sub>X</sub> record’s status changes to “I” (In Process).

## Removing eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fillable eR<sub>X</sub> can be removed from the Holding Queue without sending a message back to the originating external provider. Sample scenarios include, but are not limited to, the patient requested that the eR<sub>X</sub> not be filled, or the user has been unable to contact the provider or patient for a significant amount of time.

To remove an eR<sub>X</sub> from the Holding Queue:

1.  From the Summary/Details screen, type \<RM\> Remove.
2.  Enter a reason for the eR<sub>X</sub> removal. The following removal reasons are available:
- REM01 - Drug out of stock or on backorder and unavailable for processing
- REM02 - Patient was not able to pick up
- REM03 - Prescription canceled by Provider
- REM04 - Prescription processed manually
- REM05 - Provider will cancel this eR<sub>X</sub> and submit another
- REM06 - Unable to mail prescription and patient unable to pick up
- REM07 - Unable to contact patient
- REM08 - Unable to contact provider
- REM91 - Undefined system error
- REM92 – Other
- REM09 – ERX Issue not resolved - Provider contacted
1.  Type additional comments as to why the eR<sub>X</sub> is being removed and press \<Enter\>. These comments are optional.

Once the eR<sub>X</sub> is removed, the status changes to “RM” and it no longer displays in the default Holding Queue List; however, the eR<sub>X</sub> can be accessed via the search action from the main Holding Queue List screen using one or more of the search criteria. Refer to section  
<u>3.15.1 Searching eRXes</u>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/075.png)

<span id="_Toc167367375" class="anchor"></span>Figure 3.14‑1: Removing an eR<sub>X</sub>

> **NOTE:** If the Remove function is in parentheses “()”, the user is not able to remove an eR<sub>X</sub>. If the action is still attempted, the user receives a message that the action is not available.

## Searching and Sorting in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can search and sort eR<sub>X</sub>es in the Holding Queue. Searching and sorting eR<sub>X</sub>es is described in the following sections.

### Searching eR<sub>X</sub>es

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Searching and filtering of eR<sub>X</sub>es is available by typing \<SR\> Search Queue at the “Select Action” prompt. The Search Queue screen displays. Users can search using one or more of the following search criteria in the Traditional View:

1.  PATIENT NAME
2.  DATE OF BIRTH
3.  RECEIVED DATE RANGE
4.  PROVIDER NAME
5.  ERX STATUS
6.  DRUG NAME
7.  MESSAGE TYPE
8.  ERX REFERENCE NUMBER

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/076.png)

<span id="_Toc167367376" class="anchor"></span>Figure 3.15‑1: Search Queue Actions

- The display contains all eR<sub>X</sub>es satisfying the search criteria. The list is refreshed depending on the action performed. After an action is performed, the user can return to the original filtered list.
- The number of eR<sub>X</sub> records displayed in the Holding Queue’s list view is based on the ERX DEFAULT LOOKBACK DAYS file (#10.2) configured in OUTPATIENT SITE file (#59).
- By default, the ERX DEFAULT LOOKBACK DAYS field is blank, so the software goes back 365 days.
- If the Pharmacy user would like to see eR<sub>X</sub> records received from older dates, the user can use the Search (SR) option and select the “Received Date Range” (#3), to retrieve those records.

#### Search eR<sub>X</sub> – Patient Name

Users can search by patient name. A search initiated with a partial patient name may return multiple patient names, from which one patient can be selected. Selecting a patient displays the eR<sub>X</sub>es for that patient.

To search by patient name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  From the Search Queue, type \<1\> or PATIENT NAME.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/077.png)

<span id="_Toc167367377" class="anchor"></span>Figure 3.15‑2: Search Criteria - Patient Name

3.  Type the full or partial name of the patient press \<Enter\>. If multiple patients exist for the search criteria entered, select the correct patient from the list provided.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/078.png)

<span id="_Toc167367378" class="anchor"></span>Figure 3.15‑3: Patient Name Search

4.  A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

The search results display. To execute another search, enter \<Shift\>+\<^\> or \<Q\> Quit to exit the current search and return to the original Holding Queue List. The SR Search Queue action is in parentheses, indicating that the user must exit the current search to execute a new search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/079.png)

<span id="_Toc167367379" class="anchor"></span>Figure 3.15‑4: Search eR<sub>X</sub> by Patient Name Results

#### Search eR<sub>X</sub> – Date of Birth

To search by patient’s date of birth:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  From the Search Queue Type \<2\> or DATE OF BIRTH.
3.  Enter the date of birth and press \<Enter\>.

    A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/080.png)

<span id="_Toc167367380" class="anchor"></span>Figure 3.15‑5: Search Criteria - Date of Birth

The search results in the following display:

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/081.png)

<span id="_Toc167367381" class="anchor"></span>Figure 3.15‑6: Search eR<sub>X</sub> by Date of Birth Results

#### Search eR<sub>X</sub> – Received Date Range

To search for an eR<sub>X</sub> by a received date range:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
13. Type \<3\> or RECEIVED DATE RANGE.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/082.png)

<span id="_Toc167367382" class="anchor"></span>Figure 3.15‑7: Search Criteria - Received Date Range

14. Enter the beginning date and press \<Enter\>.
15. Enter the ending date and press \<Enter\>.
16. A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/083.png)

<span id="_Toc167367383" class="anchor"></span>Figure 3.15‑8: Enter Beginning and Ending Date

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/084.png)

<span id="_Toc167367384" class="anchor"></span>Figure 3.15‑9: Search eR<sub>X</sub> by Received Date Range

#### Search eR<sub>X</sub> – Provider Name

To search for an eR<sub>X</sub> by a provider:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<4\> or PROVIDER NAME.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/085.png)

<span id="_Toc167367385" class="anchor"></span>Figure 3.15‑10: Search Criteria - Provider Name

3.  Type the provider’s name and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/086.png)

<span id="_Toc167367386" class="anchor"></span>Figure 3.15‑11: Enter Provider Name

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/087.png)

<span id="_Toc167367387" class="anchor"></span>Figure 3.15‑12: Search eR<sub>X</sub> by Provider

#### Search eR<sub>X</sub> – ERX Status

To search for an eR<sub>X</sub> by Status:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<5\> or ERX STATUS.
3.  Enter the eR<sub>X</sub> status and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/088.png)

<span id="_Toc167367388" class="anchor"></span>Figure 3.15‑13: Search Criteria - ERX Status

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/089.png)

<span id="_Toc167367389" class="anchor"></span>Figure 3.15‑14: Search by eR<sub>X</sub> Status

For more information on the available statuses in the Holding Queue, refer to the tables in Appendix B: Holding Queue Status Codes & Descriptions.

#### Search eR<sub>X</sub> – Drug Name

To search for an eR<sub>X</sub> by Drug Name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<6\> or DRUG NAME.
3.  Type the name or partial name of the incoming eR<sub>X</sub> drug and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/090.png)

<span id="_Toc167367390" class="anchor"></span>Figure 3.15‑15: Search Criteria - Drug Name

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/091.png)

<span id="_Toc167367391" class="anchor"></span>Figure 3.15‑16: Search eR<sub>X</sub> by Drug Name

#### Search eR<sub>X</sub> – Message Type 

To search for an eR<sub>X</sub> by Message Type:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<7\> or MESSAGE TYPE.
3.  Select the Message Type and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/092.png)

<span id="_Toc167367392" class="anchor"></span>Figure 3.15‑17: Search Criteria - Message Type

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/093.png)

<span id="_Toc167367393" class="anchor"></span>Figure 3.15‑18: Search by Message Type

#### Search eR<sub>X</sub> – eR<sub>X</sub> Reference Number

Users may also search for eR<sub>X</sub>es by eR<sub>X</sub> Reference Number. When searching by eR<sub>X</sub> Reference Number, the user may search by either inbound or outbound message types.

To search for an inbound eR<sub>X</sub> message type by eR<sub>X</sub> Reference Number:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<8\> or ERX REFERENCE NUMBER.
3.  Enter the eR<sub>X</sub> Reference Number and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/094.png)

<span id="_Toc167367394" class="anchor"></span>Figure 3.15‑19: Search Criteria – eR<sub>X</sub> Reference Number: Inbound

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/095.png)

<span id="_Toc167367395" class="anchor"></span>Figure 3.15‑20: Search by eR<sub>X</sub> Reference Number Results – Inbound eR<sub>X</sub> Message Type

Under Patient Centric View, the user can use the following Search options:

1.  Patient Name
2.  Date of Birth
3.  eR<sub>X</sub> Reference Number

### Sorting eR<sub>X</sub>es

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA users can sort eR<sub>X</sub>es in the Holding Queue List. Sort parameters are retained at the user level when reentering the original list during the same session (i.e., when performing an action on an eR<sub>X</sub> and then reentering the eR<sub>X</sub> list). The default sort order of the Holding Queue List is the following:

1.  Date Received - Oldest date to Newest date.
2.  Secondary sort by Patient Name.
3.  Grouped by Controlled Substance

Additional sorting of eR<sub>X</sub>es is available by typing \<SO\> Sort Entries.

- The number of eR<sub>X</sub> records displayed in the Holding Queue’s list view is based on the ERX DEFAULT LOOKBACK DAYS file (#10.2) configured in OUTPATIENT SITE file (#59).
- By default, the ERX DEFAULT LOOKBACK DAYS field is blank, so the software goes back 365 days.
- If the Pharmacy user would like to see eR<sub>X</sub> records received from older dates, the user can use the Search \<SR\> option and select the “Received Date Range” (#3), to retrieve those records.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/096.png)

<span id="_Toc167367396" class="anchor"></span>Figure 3.15‑21: Sort Entries Action

eR<sub>X</sub>es can be sorted by only one criterion at a time. The sort criteria include:

- Patient Name: Sorted by Patient in ascending order (A-Z), and within Patient by Received Date with most recent first, and then by Provider in ascending order (A-Z)
- Date of Birth: By DOB, newest Received Date first, Patient Name ascending
- Received Date Range: Sorted by Received Date with most recent first and within Received Date by Patient in ascending order (A-Z), and then by Provider in ascending order (A-Z)
- Provider Name: Sorted by Provider in ascending order (A-Z), and within Provider by Received Date with oldest first, and then by Patient in ascending order (A-Z)
- eR<sub>X</sub> Status: Drug Name ascending
- Drug Name: Patient Name ascending, newest Received Date first
- Message Type: RxRenewal Request, RxRenewal Response, NewRx, RxChange Request, RxFill, Inbound Error, Outbound Error, CancelRx Response, RxChange Response

#### Sort eR<sub>X</sub> – Patient Name

To sort by patient:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<1\> or Patient Name.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/097.png)

<span id="_Toc167367397" class="anchor"></span>Figure 3.15‑22: Sort by Patient Name

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/098.png)

<span id="_Toc167367398" class="anchor"></span>Figure 3.15‑23: Group by Controlled Substance

4.  The sorted entries display Sorted by Patient in ascending order (A-Z), and within Patient by Received Date Range with most recent first, and then by Provider in ascending order (A-Z).

#### Sort eR<sub>X</sub> – Date of Birth

To sort by Date of Birth:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<2\> or Date of Birth.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/099.png)

<span id="_Toc167367399" class="anchor"></span>Figure 3.15‑24: Sort by Date of Birth

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/100.png)

<span id="_Toc167367400" class="anchor"></span>Figure 3.15‑25: Group by Controlled Substance

4.  The entries display by DOB, newest Received Date first, Patient Name ascending.

#### Sort eR<sub>X</sub> – Received Date Range

To sort eR<sub>X</sub>es by received date (most recent date displays at top of sort results):

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<3\> or Received Date Range.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/101.png)

<span id="_Toc167367401" class="anchor"></span>Figure 3.15‑26: Sort by Received Date Range

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/102.png)

<span id="_Toc167367402" class="anchor"></span>Figure 3.15‑27: Group by Controlled Substance

4.  The entries sort by Received Date with most recent first and within Received Date by Patient in ascending order (A-Z), and then by Provider in ascending order (A-Z).

#### Sort eR<sub>X</sub> – Provider Name

To sort eR<sub>X</sub>es by provider name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<4\> or Provider Name.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/103.png)

<span id="_Toc167367403" class="anchor"></span>Figure 3.15‑28: Sort Criteria - Sort by Provider

1.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/104.png)

<span id="_Toc167367404" class="anchor"></span>Figure 3.15‑29: Group by Controlled Substance

2.  The entries sort by Provider in ascending order (A-Z), and within Provider by Received Date with oldest first, and then by Patient in ascending order (A-Z).

#### Sort eR<sub>X</sub> – ERX Status

To sort eR<sub>X</sub>es by eR<sub>X</sub> Status:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<5\> or ERX Status.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/105.png)

<span id="_Toc167367405" class="anchor"></span>Figure 3.15‑30: Sort Criteria – Sort by eR<sub>X</sub> Status

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/106.png)

<span id="_Toc167367406" class="anchor"></span>Figure 3.15‑31: Group by Controlled Substance

4.  The entries sort by Patient Name ascending, newest Received Date first.

#### Sort eR<sub>X</sub> – Drug Name

To sort eR<sub>X</sub>es by Drug Name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<6\> or Drug Name.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/107.png)

<span id="_Toc167367407" class="anchor"></span>Figure 3.15‑32: Sort Criteria – Sort by Drug Name

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/108.png)

<span id="_Toc167367408" class="anchor"></span>Figure 3.15‑33: Group by Controlled Substance

4.  The entries sort by Drug Name in ascending order.

#### Sort eR<sub>X</sub> – Message Type

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<7\> or MESSAGE TYPE.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/109.png)

<span id="_Toc167367409" class="anchor"></span>Figure 3.15‑34: Sort Criteria – Sort by Message Type

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/110.png)

<span id="_Toc167367410" class="anchor"></span>Figure 3.15‑35: Group by Controlled Substance

4.  The entries sort by Message Type in ascending order.

## Complete Orders from OERR and Patient Prescription Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following all the validation steps for patient, provider, and drug/SIG, and after the eR<sub>X</sub> has been accepted, the eR<sub>X</sub> advances to Pending Outpatient Orders file for further processing. The eR<sub>X</sub> is further finished using either Complete Orders from OERR or Patient Prescription Processing.

The “&” symbol indicates that an eR<sub>X</sub> was received from an external provider. eR<sub>X</sub> records without the “&” symbol are VA eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/111.png)

<span id="_Toc167367411" class="anchor"></span>Figure 3.16‑1: eR<sub>X</sub> Received from External Provider

The eR<sub>X</sub> information displays at the top of the screen under the Secondary header, as shown in the figure below in both Complete Orders from OERR and Patient Prescription Processing. The hidden Option EP is provided in Outpatient to print the eR<sub>X</sub> (see figure below).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/112.png)

<span id="_Toc167367412" class="anchor"></span>Figure 3.16‑2: Hidden Option EP / Print Display of eR<sub>X</sub>

The eR<sub>X</sub> information can be edited and either finished to process further for dispensing or discontinued as needed (such as a duplicate order, since it is not filtered in the eR<sub>X</sub> Holding Queue).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/113.png)

<span id="_Toc167367413" class="anchor"></span>Figure 3.16‑3: eR<sub>X</sub> Display in Pending Queue - Page 1

Refer to the user manuals available on the VA Documentation Library (VDL) for information on Complete Orders from OERR and Patient Prescription Processing.

Press \<Enter\> to view Pages 2 through 5 of the order in the Pending Queue.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/114.png)

<span id="_Toc167367414" class="anchor"></span>Figure 3.16‑4: eR<sub>X</sub> Order in Pending Queue – Page 2

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/115.png)

<span id="_Toc167367415" class="anchor"></span>Figure 3.16‑5: eR<sub>X</sub> Order in Pending Queue - Page 3

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/116.png)

<span id="_Toc167367416" class="anchor"></span>Figure 3.16‑6: eR<sub>X</sub> Order in Pending Queue - Page 4

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-743/117.png)

<span id="_Toc167367417" class="anchor"></span>Figure 3.16‑7: eR<sub>X</sub> Order in Pending Queue - Page 5

> **NOTE:** - “eRx Date” on Holding Queue Summary screen – Date when the eR<sub>X</sub> was received in the VistA Holding Queue.

- “Date Written” on Validate Drug/SIG screen – Date when the eR<sub>X</sub> was received in the VistA Holding Queue.
- “Issue Date” on OERR/Backdoor Orders Summary screen – Effective Date if sent by the provider; if not, it is Written Date, both as sent on the eR<sub>X</sub>.
- “Written Date” displayed on Track/Audit screen on web GUI – Written Date as sent on the eR<sub>X</sub>.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Inbound ePrescribing User Manual (Unit 7 Part 1) PSO*7*746

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new option replaces the existing *Complete Orders from eR<sub>X</sub>* option \[PSO ERX FINISH\]. VistA Outpatient Pharmacy is comprised of two sections:

- Inbound eR<sub>X</sub> VistA Holding Queue
- Inbound eR<sub>X</sub> VistA Outpatient Profile - Complete Orders from Order Entry/Results Reporting (OERR) and Patient Prescription Processing

## Purpose of Inbound eR<sub>X</sub> VistA Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eR<sub>X</sub> Holding Queue allows for validation and review of the eR<sub>X</sub> by VA Pharmacy users prior to the eR<sub>X</sub> being added to the VA record and merging with the existing outpatient functionality. For the fillable prescriptions, VA Pharmacy users can validate patient, provider, and drug/SIG information. Additionally, users can accept, hold, un hold, print, reject, or remove an eR<sub>X</sub> from the Holding Queue after it has been received by VistA from the eR<sub>X</sub> Processing Hub. The users can also work with RxRenewal Responses, RxChange Responses and CancelRx Requests, which are described.

> **NOTE:** Controlled Substance records that meet the requirements of the Drug Enforcement Administration’s (DEA) electronic prescribing for Controlled Substance rules will have a visual indicator stating “EPCS DEA Valid” at the top right corner in the VistA Holding Queue.

## eRx Holding Queue Processing \[PSO ERX QUEUE PROCESSING\] option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The inbound eR<sub>X</sub> message is transmitted from the Processing Hub to VistA and stored in the eR<sub>X</sub> Holding Queue.

To access the eR<sub>X</sub> Holding Queue:

Follow this navigation path: Core Applications \> Outpatient Pharmacy Manager \> (select Division) \> RX (Prescriptions) ... \> eRx Holding Queue Processing \[PSO ERX QUEUE PROCESSING\]

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patient Prescription Processing</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX eRx Holding Queue Processing</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>FERX Complete Orders from eRx</p>
<p><strong>&gt;Out of order: Please use PSO ERX QUEUE PROCESSING option instead</strong></p>
<p>PRNT Print a PMI Sheet</p>
<p>PROF Medication Profile</p>
<p>Barcode Rx Menu ...</p>
<p>Check Drug Interaction</p>
<p>Complete Orders from OERR</p>
<p>Discontinue Prescription(s)</p>
<p>Edit Prescriptions</p>
<p>ePharmacy Menu ...</p>
<p>List One Patient's Archived Rx's</p>
<p>Manual Print of Multi-Rx Forms</p>
<p>OneVA Pharmacy Prescription Report</p>
<p>Release Medication</p>
<p>Reprint an Outpatient Rx Label</p>
<p>Signature Log Reprint</p>
<p>View Prescriptions</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Holding Queue Processing Menu Option

To enter eRx Holding Queue Processing option, you must select the type of records you want to see on the Holding Queue. You will enter directly into the Patient Centric View, but you can easily switch to the Rx List view back and forth to the Patient Centric View.

### Actionable and Non-Actionable eR<sub>X</sub> Records 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before learning how this option works it is important to understand that there are two types of Inbound eR<sub>X</sub> records: Actionable records and Non-Actionable records.

<u>Actionable records include:</u>

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

<u>Non-Actionable records</u>

Are all records acknowledged, removed, rejected, processed/completed, and auto-canceled are non-actionable. Non-Actionable records further include:

- RxRenewal Request
- RxRenewal Response – Approved
- RxRenewal Response – Approved with Changes (change to drug data only)
- RxChange Request
- CancelRx Response
- Inbound Errors related to CancelRx Responses

### Initial Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon entering the option, the user is prompted to choose which eRx record status they would like to view or work on. Once the prompts are answered, the user will enter the eRx Patient Centric View Queue, which is explained further down on this document.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will be prompted to select a Clinic. This helps MbM distribute the workload into multiple clinics so when the pharmacists are finishing the prescriptions they can work on the queue for a specific clinic.</p>
<p>eRx Clinic (Optional):</p>
<p>Although VAMC’s users are not presented this prompt, their eRx is still assigned a default clinic that is entered in the Site Parameter Enter/Edit [PSO SITE PARAMETERS] option under the field DEFAULT ERX CLINIC.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>A All</p>
<p>N New</p>
<p>I In Progress</p>
<p>W Wait</p>
<p>H Hold</p>
<p>C CCR</p>
<p>WP Workload Processing</p>
<p>Enter response: A// ?</p>
<p>All - View all patients with actionable prescriptions</p>
<p>New - View patients with prescriptions in the 'NEW' status</p>
<p>In Process - View patients with prescriptions in the 'IN PROCESS' status</p>
<p>Wait - View patients with prescriptions in the 'WAIT' status</p>
<p>Hold - View patients with prescriptions in the 'HOLD' status</p>
<p>CCR - View patients with prescriptions in the 'CCR' status</p>
<p>Workload Processing - Process New prescriptions for one patient at a</p>
<p>time using FIFO (First In First Out) method</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Status Selection

The screen above shows all the options users can chose for building the initial list upon entering the Patient Centric View. With the exception of the WP (Workload Processing), which will be explained further down on this document.

Users holding the PSO ERX WORKLOAD TECH security key will be limited to selecting the following options from the menu above to 3 options shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>H Hold</p>
<p>C CCR</p>
<p>WP Workload Processing</p>
<p>Enter response: WP//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

PSO ERX WORKLOAD TECH security key holders options

A – All

This choice will include all eRx that are actionable. Meaning that they still have some work to be done before they can be considered completed.

N – New

This choice will include only eRx with a NEW status. These are records for a new eRx that have not yet been changed by any other user.

I - In-Process

This choice will include only eRx with a IN PROCESS status. These are records that one or multiple users have already done some work on but, they are not yet completed.

W - Wait

This choice will include only eRx with a WAIT status. Similar to IN PROCESS these are records that one or multiple users have already done some work on, but they are not yet completed. They have usually been put on Hold and now have been removed from Hold.

H – Hold

This choice will include only eRx in a HOLD status. However, there are many different HOLD statuses and that’s why the next prompts shown below allows the user to further define this choice.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// Hold</p>
<p>Select one of the following:</p>
<p>S SINGLE CODE</p>
<p>A ALL HOLD CODES</p>
<p>Enter response: A// SINGLE CODE</p>
<p>Select eRx Status: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT - PATIENT NOT FOUND</p>
<p>119 HPD - PROVIDER NOT FOUND</p>
<p>120 HNF - NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO - INSUFFICIENT STOCK</p>
<p>122 HDI - DRUG-DRUG INTERACTION</p>
<p>123 HAD - ADVERSE DRUG INTERACTION</p>
<p>124 HBA - BAD ADDRESS</p>
<p>125 HPC - PROVIDER CONTACTED</p>
<p>126 HPA - PRIOR APPROVAL NEEDED</p>
<p>127 HOR - OTHER REASON</p>
<p>128 HPP - PATIENT CONTACTED</p>
<p>129 HPR - HOLD DUE TO PATIENT REQUEST</p>
<p>130 HQY - QUANTITY OR REFILL ISSUE</p>
<p>1442 HC - HOLD DUE TO CHANGE</p>
<p>1618 HCR - PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>1619 HWR - CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>1620 HIS - PROVIDER DEA# ISSUE</p>
<p>1621 HRX - HOLD FOR RX EDIT</p>
<p>1622 HDE - DRUG USE EVALUATION</p>
<p>1623 HTI - THERAPUTIC INTERCHANGE</p>
<p>1624 HSC - SCRIPT CLARIFICATION</p>
<p>1625 HGS - GENERIC SUBSTITUTION</p>
<p>1631 HAL - NO ALLERGY ASSESSMENT</p>
<p>1632 HEL - ELIGIBILITY ISSUE</p>
<p>1633 HUR - UN-REMOVED</p>
<p>1668 HFF – HOLD FOR FUTURE FILL</p>
<p>Select eRx Status:</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

Hold Status Selection

In this case the user can select ALL HOLD CODES to include every eRx in a HOLD status or SINGLE CODE which allows the user to load eRx for one single HOLD code to be on the queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Note</u></strong></p>
<p>The code numbers shown on the left column above may not match the numbers on your VistA account.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

C – CCR

This choice will include only eRx in a CCR status. However, there are many different CCR statuses and that’s why the next prompts shown below allows the user to further define this choice. If they choose “A” (ALL CCR CODES) the list will include all eRx records with any of the eRx statuses shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// CCR</p>
<p>Select one of the following:</p>
<p>S SINGLE CODE</p>
<p>A ALL CCR CODES</p>
<p>Enter response: A// SINGLE CODE</p>
<p>Select eRx Status: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>246 RXR - RXRENEWAL RESPONSE REPLACE - NEW</p>
<p>247 RXE - RXRENEWAL RESPONSE - PROCESSING ERROR</p>
<p>248 RXN - RXRENEWAL RESPONSE - NEW</p>
<p>289 RXF - RXRENEWAL RESPONSE FAILED</p>
<p>606 CAO - CANCEL PROCESS COMPLETE</p>
<p>607 CAH - CANCEL COMPLETED IN HOLDING QUEUE</p>
<p>609 CAR - CANCEL REQUEST RECEIVED</p>
<p>612 CAF - CANCEL PROCESS FAILED</p>
<p>613 CAP - CANCEL PAPER RX OR FAXED RX</p>
<p>618 RXD - RXRENEWAL RESPONSE DENIED/DNTF</p>
<p>620 CAX - CANCEL RESPONSE FROM VISTA UNSUCCESSFUL</p>
<p>1412 CXN - RXCHANGE RESPONSE - NEW</p>
<p>1413 CXV - RXCHANGE RESPONSE - PRESCRIBER AUTH - NEW</p>
<p>1414 CXY - RXCHANGE RESPONSE - PRIOR AUTH - NEW</p>
<p>1418 CXD - RXCHANGE RESPONSE DENIED</p>
<p>1421 CXE - RXCHANGE RESPONSE - PROCESSING ERROR</p>
<p>Select eRx Status:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CCR Status Selection

In this case the user can select ALL CCR CODES to include every eRx in a CCR status or SINGLE CODE which allows the user to load eRx for one single CCR code to be on the queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Note</u></strong></p>
<p>The code numbers shown on the left column above may not match the numbers on your VistA account.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

WP – Workload Processing

This option will bypass the Patient Centric Queue and will load one patient at a time directly into the Single Patient Queue. Once inside the Single Patient queue the user can use the action NP (Next Patient) to load the next patient. The order in which the patients are presented are based on the eRx received date. Patient with the oldest records will be presented first. The date range for looking for these records are based on the ERX DEFAULT LOOKBACK DAYS parameter in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\].

Users holding the PSO ERX WORKLOAD TECH security key they cannot jump to the next patient (by selecting NP – Next Patient) until they have processed all the prescriptions for the current patient on their screen. Once a user with the PSO ERX WORKLOAD TECH key enters the first patient, that patient is assigned to that user for that day and no matter how many times the user gets out of the option and comes back in, such patient will be presented to them for processing. This feature was designed to prevent users from “cherry-picking” patients to work on while working in a Workload Processing mode.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// WP Workload Processing</p>
<p>Select one of the following:</p>
<p>1 PATIENT NOT MATCHED</p>
<p>2 PROVIDER NOT MATCHED</p>
<p>3 DRUG NOT MATCHED</p>
<p>4 PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>MATCH STATUS: 5//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Workload Processing option filters

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will see a slightly different labeling for the options above:</p>
<p>1 <mark>PATIENT FAIL -</mark> PATIENT NOT MATCHED</p>
<p>2 <mark>PROVIDER FAIL -</mark> PROVIDER NOT MATCHED</p>
<p>3 <mark>DRUG FAIL -</mark> DRUG NOT MATCHED</p>
<p>4 <mark>BASIC -</mark> PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>This is only a labeling difference and won’t affect the functionality of this filter, which works the same for VAMC and MbM sites.</p></td>
</tr>
</tbody>
</table>

1 – PATIENT NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Patient has not been matched to a VistA Patient.

2 – PROVIDER NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Provider has not been matched to a VistA Provider. Furthermore, the patient cannot quality for the PATIENT NOT MATCHED filter.

3 – DRUG NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Drug has not been matched to a VistA Drug. Furthermore, the patient cannot quality for the PATIENT NOT MATCHED and PROVIDER NOT MATCHED filters.

4 – PATIENT, PROVIDER AND DRUG MATCHED

This option will only load and go through eRx Patients with at least one eRx record where all three (PATIENT, PROVIDER and DRUG) are matched to a VistA corresponding record.

5 – ALL (NO FILTERS)

This option will not apply any filters regarding matching. It will start from the oldest records and move its way through the patients with the newest records.

### eRx Patient Centric Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the status selection is made, the user will enter the eRx Holding Queue in the Patient Centric view by default with the exception for the WP (Workload Processing) choice which will take the user directly to the Single Patient Queue View, explained further down in this document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Holding Queue – Patient Centric Queue

The figure above shows the eRx Holding Queue initial screen, in Patient Centric Queue view which contains a list of patients with Actionable (non-processed) eRx records. Below is an explanation of each segment of the screen.

#### Top Line

It contains the title of the list, in this case “eRx Patient Centric Queue”, then the current date/time to the right the page the user is on and how many pages there are total.

#### Header Area

In this non-scrollable area, there are 4 fields that control the list being displayed.

LOOK BACK DAYS

Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

CS/NON-CS

Indicates whether the list contains Controlled Substances (CS), Non-Controlled Substances (Non-CS) or Both. In case of CS being included it will also indicate the schedule of the CS drugs being displayed. It can also be changed by the user as described further down.

MAX. QUEUE SIZE

Indicates the maximum number of records that can be loaded in the list. It means that any selection that produces a number of records greater than this number will be cutoff at this number of records on the list. This limit can also be changed by the user as described further down.

ERX STATUS  
Indicates the status selection by the user before entering the list (Figure 6-2 above). With the exception of the WP selection, which bypass this list completely.

#### Column Header Line

\#

This column indicates the sequence number for the patient being displayed, which can be selected by the user to open the patient in a Single Patient Queue view screen.

PATIENT

Patient name column (maximum of 24 characters).

DOB

Date of birth column (MM/DD/YYY format).

SSN

Social Security column.

ED

Elapsed Days column. Indicates how many days ago the oldest actionable record for the patient was received.

NW

New eRx record status count. The number in this column indicates how many eRx are in a NEW status.

WT

Wait eRx record status count. The number in this column indicates how many eRx are in a WAIT status.

IP

In-Process eRx record status count. The number in this column indicates how many eRx are in a IN-PROCESS status.

HD

Hold eRx record status count. The number in this column indicates how many eRx are in a HOLD status.

CCR

CCR eRx record status count. The number in this column indicates how many eRx are in a CCR status: CancelRx Request, RxChange Response, and RxRenewal Response records in actionable statuses; including RXF, RXE and CXE records.

OTH

A count of all other status not captured by the columns to the left. It also includes Inbound Error related to RxRenewal/RxChange Request (Status – RRE/CRE).

TOT

A sum of all the numbers from the columns to the left.

<span class="mark">^</span> or <span class="mark">v</span>

One of these two symbols above can be spotted besides one of the following columns: PATIENT, DOB or ED. It indicates the column that the list is sorted by. <span class="mark">^</span> indicates an ascending order (smaller first A-\>Z or 0\>9) and <span class="mark">v</span> indicates a descending order (greater first Z-\>A or 9-\>0). Look further down to see how to sort by different columns and order (ascending or descending).

#### Listing Area

This area is where all the records are listed. They are always sequential number that goes from 1 to the last item on the list. This number can be selected by the user to view all the patient’s eRx records in a Single Patient Queue view.

\#. Vs. \#\] (Digitally Signed Vs. Not Digitally Signed)

Following each number there will be one of two characters “.” (dot) or “\]” (closing square bracket), as seen on lines 2. 10 and 14 on figure 6-7 above. The “.” indicates that the patient does not have any Digitally Signed eRx records, while the “\]” indicates that the patient has at least one eRx records that was Digitally Signed by the external provider. Digitally signed records is an indication by the external provider that the drug in the eRx records is a Controlled Substance drug. CS drugs are mandated by DEA (Drug Enforcement Agency) to always be transmitted to the pharmacy with a Digital Signature.

Bolded Lines

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A bolded line as seen on lines 4 and 14 above indicates another user has the patient or one of their eRx records open. When the user tries to select such numbers, a message will display on the message bar (below the list and above the Action Menu) indicating the user and date/time the records was locked, as shown below:

| \+ Patient Locked:XXXXXXXXX,XXXXXXXXX\|09/16/23@12:12:16 |
|----------------------------------------------------------|

Patient Centric Queue - Patient Locked

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SPAT – Sort By Patient

By default, the list is always sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Name by selecting the SPAT action. It will sort the list by Patient Name in ascending order when the user picks it once. If currently sorted by Patient Name and the users selects SPAT again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT<span class="mark">^</span> DOB SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient Name in Ascending Order

| \# PATIENT<span class="mark">v</span> DOB SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient Name in Descending Order

#### SQ – Search Queue

This action allows the user to place filters on the list by a few different selection criteria shown below. Multiple filters can be applied in one search criteria with the exception of ERX REFERENCE NUMBER and RX# which will result in the selection of one single record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// SQ Search Queue</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Queue options

1 - ERX PATIENT

Users can filter the list by single or multiple eRx patients by selecting them as seen below. The LAST REC. DATE column indicates the last eRx received for this patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 1 ERX PATIENT</p>
<p>ERX PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># ERX PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXXX 99/99/9999 PICKLETON-NY 09/10/23</p>
<p>2. XXXXXX,XXXXXXX 99/99/9999 BUTTERVILLE-NY 09/02/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX| XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

2 - ERX DATE OF BIRTH

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 2 ERX DATE OF BIRTH</p>
<p>Date of Birth (DOB): 99/99/999 (XXX 99, 9999)</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient Date of Birth

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>DOB(99/99/99)|PATIENT(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Results

In the case of the Search criteria not providing any matching entries, the screen below will display:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: DOB(99/99/99)|PATIENT(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No patients with actionable prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Results

3 - ERX REFERENCE NUMBER

This search will take the user to the eRx Display screen and show the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 3 ERX REFERENCE NUMBER</p>
<p>ERX REFERENCE NUMBER: 9999999999</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Search by eRx REFERENCE NUMBER

4 – RX#

This search will first find the associated eRx with the VistA Rx \# selected and will take the user to the eRx Display screen then show the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 4 VISTA RX #</p>
<p>VISTA Rx #: 9999999999</p>
<p>This prescription is not an eRx prescription.</p>
<p>VISTA Rx #:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Search by VISTA Rx \#

5 – VISTA PATIENT

Users can filter the list by single or multiple VistA patients by selecting them as seen below. The REC. DATE column indicates the last eRx received for this patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 1 ERX PATIENT</p>
<p>VISTA PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXXX 99/99/9999 PLANO-TX 09/19/23</p>
<p>2. XXXXXX,XXXXXXX 99/99/9999 NEW YORK-NY 09/18/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT <strong>(XXXXXX,XXXXXX| XXXXXX,XXXXXX)</strong></p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

6 – MATCH STATUS

This search will qualify patients based on the matching status of the patient, provider, and drug to a corresponding VistA Record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 6 MATCH STATUS</p>
<p>Select one of the following:</p>
<p>1 PATIENT NOT MATCHED</p>
<p>2 PROVIDER NOT MATCHED</p>
<p>3 DRUG NOT MATCHED</p>
<p>4 PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>MATCH STATUS: 4</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

6.1 – MATCH STATUS: PATIENT NOT MATCHED

If the patient has at least one actionable record which the eRx patient has not yet been matched to, a corresponding VistA patient will be included in the list.

6.2 – MATCH STATUS: PROVIDER NOT MATCHED

If the patient has at least one actionable record which the eRx provider has not yet been matched to, a corresponding VistA provider AND the patient does not qualify for PATIENT NOT MATCHED filter above, it will be included in the list.

6.3 – MATCH STATUS: DRUG NOT MATCHED

If the patient has at least one actionable record which the eRx Drug has not yet been matched to, a corresponding VistA drug AND the patient does not qualify for PATIENT NOT MATCHED filter above AND the patient does not qualify for the PROVIDER NOT MATCHED filter above, it will be included in the list.

6.4 – MATCH STATUS: PATIENT, PROVIDER AND DRUG MATCHED

If the patient has at least one actionable record which the eRx patient has been matched to the VistA patient, the eRx Provider has been matched to the VistA provider and the Drug has been matched to a VistA drug AND the patient does not quality to either of the 3 filters described above, it will be included in the list.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will see a slightly different labeling for the options above:</p>
<p>1 <mark>PATIENT FAIL -</mark> PATIENT NOT MATCHED</p>
<p>2 <mark>PROVIDER FAIL -</mark> PROVIDER NOT MATCHED</p>
<p>3 <mark>DRUG FAIL -</mark> DRUG NOT MATCHED</p>
<p>4 <mark>BASIC -</mark> PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>This is only a labeling difference and won’t affect the functionality of this filter, which works the same for VAMC and MbM sites.</p></td>
</tr>
</tbody>
</table>

Removing Individual Filters

Individual filters can be removed by using the “^” (up-caret) along with the Number of the filter applied, as show below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p>
<p>SEARCH BY: <strong>^2</strong></p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Individual Filter Removal

#### LBD – Change Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s date. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Quit// LBD Change Look Back Days</p>
<p>LOOK BACK DAYS: 45// ??</p>
<p>This field holds the number of days to look back in order to include records</p>
<p>in the Patient Centric Queue.</p>
<p>LOOK BACK DAYS: 45// 365 Please Wait...</p>
<p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@12:12:23 Page: 1 of 5</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Changing Look Back Days

#### RX – Rx List View

This action takes the user to Rx Medication Queue list which will be described further down in this document.

#### RAF – Remove All Filters

This action allows the user to remove all filters currently applied to the list. This list is then refreshed to without any filters.

#### REF – Refresh List

This action allows the user to refresh the list. This is used to make sure you are looking at the latest version of the list because other users might have already worked through some of the records currently on the list which may have altered it, which will not show until it is refreshed.

#### Hidden Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following actions are also available:</p>
<p>CS Group By CS - Previous Screen PS Print Screen</p>
<p>SDOB Sort By DOB UP Up a Line PT Print List</p>
<p>SED Sort By Elapsed Days DN Down a Line SL Search List</p>
<p>NP Next Patient FS First Screen QU Quit</p>
<p>CV Change View LS Last Screen</p>
<p>+ Next Screen GO Go to Page</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### CS – Group by CS (hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. The action can be used to turn ON and OFF this hidden action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p> <u><strong><mark>CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>1] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p>4] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</p>
<p>5] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p> <u><strong><mark>NON-CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 41 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 40 0 0 1 0 0 0 1</p>
<p>10 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 38 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 35 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 33 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>14 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Grouped by CS and Non-CS

#### SDOB – Sort By Date of Birth (hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Date of Birth (DOB) by selecting the SDOB hidden action. It will sort the list by Patient DOB in ascending order when the user picks it once. If currently sorted by Patient DOB and the users selects SDOB again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB<span class="mark">^</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient DOB in Ascending Order

| \# PATIENT DOB<span class="mark">v</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient DOB in Descending Order

#### SED – Sort By Elapsed Days (hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first). The user can sort the list by the Elapsed Days by selecting the SED hidden action. It will sort the list by Elapsed Days in ascending order when the user picks it once. If currently sorted by Elapsed Days and the users selects SED again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB SSN ED<span class="mark">^</span> NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Elapsed Days in Ascending Order

| \# PATIENT DOB SSN ED<span class="mark">v</span> NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Elapsed Days in Descending Order

#### NP – Next Patient (hidden)

This hidden action allows the user to open the patient with the oldest eRx record in an actionable status. It will take the user to the eRx Single Patient Queue. Once in the eRx Single Patient Queue the user can type NP again to jump to the next patient with the oldest order after the previous patient.

#### CV – Change View (hidden)

This hidden action allows the user to change the following parameters that affect the content and appearance of the eRx Patient Centric Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days) . Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>LOOK BACK DAYS: 45// 45 DAYS</p>
<p>SORT BY: ED// ED ELAPSED DAYS</p>
<p>SORT ORDER: D// DESCENDING</p>
<p>INCLUDE CS/NON-CS: B// BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE: SCHEDULES II - V// SCHEDULES II - V</p>
<p>GROUP BY CS: NO// NO NO</p>
<p>MAXIMUM QUEUE SIZE: 999//</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action (No Default View Saved)

Once the user chooses all the parameters above the option will prompt them if they want to save the current parameters as their default view. Whether they chose YES or NO the option will refresh the list according to the parameters selected. If they select YES to save the view the next time they select CV they will be given a chance to delete their saved default view, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>Your saved default view:</p>
<p>-----------------------</p>
<p>LOOK BACK DAYS : 45 DAYS</p>
<p>SORT BY : ELAPSED DAYS</p>
<p>SORT ORDER : DESCENDING</p>
<p>INCLUDE CS/NON-CS : BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE : SCHEDULES II - V</p>
<p>GROUP BY CS/NON-CS : NO</p>
<p>MAXIMUM QUEUE SIZE : 999</p>
<p>Delete this saved default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action (With Default View Saved)

The parameters LOOK BACK DAYS, SORT BY, SORT ORDER and GROUP BY CS/NON-CS have been explained above on how they impact the queue. The other parameters are explained below:

INCLUDE CS/NON-CS

This parameter allows the user to select which type of eRx records should be displayed on the list: Controlled Substances only (CS), Non-Controlled Substances only (Non-CS) or Both (B). The default value is B. This parameter is displayed on the header of the Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INCLUDE CS/NON-CS: B// ?</p>
<p>Indicate whether CS and/or Non-CS records should be included in the</p>
<p>Patient Centric Queue.</p>
<p>Choose from:</p>
<p>CS CS ERXS ONLY</p>
<p>Non-CS NON-CS ERXS ONLY</p>
<p>B BOTH (CS AND NON-CS)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action – INCLUDE CS/NON-CS Field

CS SCHEDULE

This parameter is only prompted in the case the user selects either CS or B above. The default value is 3 (SCHEDULES II – V). This parameter is displayed on the header of the Queue. It allows the user to further filter the CS eRx records based on the drug schedule, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CS SCHEDULE: SCHEDULES II - V// ?</p>
<p>Indicate which CS Schedules should be included in the Patient Centric</p>
<p>Queue.</p>
<p>Choose from:</p>
<p>1 SCHEDULE II ONLY</p>
<p>2 SCHEDULES III - V</p>
<p>3 SCHEDULES II - V</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action – CS SCHEDULE Field

MAXIMUM QUEUE SIZE

This parameter determines the maximum number of records to be loaded for the queue. Once the process that builds the list reaches this limit it stops. The default is 999 and the maximum is 4,999. This parameter is displayed on the header of the Queue.

#### 48-Lines Terminal Emulator Display Feature

There is a Class 3 software (KIDS Build) that allows sites, including Meds-By-Mail (MbM), to expand their ListMan Listing Area to more than double of the displayed lines for one page when using the regular 24-Lines on the Terminal Emulator. It is important to emphasize that simply setting the Terminal Emulator to 48-Lines won’t work, the VistA account where the user is connecting must have this Class 3 software installed for it to work.

Once the KIDS Build is installed and the Terminal Emulator is set to display 48-Line, the eRx Patient Centric Queue will look like the following:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 2</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p><strong>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</strong></p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>17. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 0 0 1 0 0 1 2</p>
<p>18. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>19. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 3 0 0 1 0 0 4</p>
<p>20 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 1 0 1 0 0 0 2</p>
<p>21. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 0 0 1 0 0 1 2</p>
<p>22. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 1 0 0 0 1 0 2</p>
<p>23. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 2 1 0 0 3</p>
<p>23. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 1 0 0 0 1</p>
<p>25. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 1 0 0 0 1</p>
<p>26] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 24 0 0 1 0 0 0 1</p>
<p>27. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 24 1 0 0 0 1 0 2</p>
<p>28. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 23 1 0 0 0 0 0 1</p>
<p>29. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 22 2 0 1 0 0 0 3</p>
<p>30] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 21 1 0 0 0 0 0 1</p>
<p>31. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 21 1 0 0 0 0 0 1</p>
<p>32. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 20 1 0 0 0 0 0 1</p>
<p>33. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 19 0 0 1 0 0 1 2</p>
<p>34. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 9 2 0 1 0 0 0 3</p>
<p>35. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 7 3 0 0 1 0 0 4</p>
<p>36. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 1 1 0 1 0 0 0 2</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### eRx Single Patient Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user selects a patient in the eRx Patient Centric Queue above, they will be taken to the eRx Single Patient Queue. This list will by default display all the eRx Patient’s Actionable records and they will be sorted by the REC.DATE column in a descending order (oldest records first).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A AV A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Single Patient Queue

#### Top Line

It contains the title of the list, in this case “eRx Single Patient Queue”, then the current date/time to the right the page the user is on and how many pages there are total.

#### Header Area

In this non-scrollable area, there are 6 fields that control the list being displayed.

eRx PATIENT

This is the eRx Patient name as received by the outside prescriber.

SEX

eRx Patient gender.

DOB

eRx Patient date of birth followed by their age between parentheses.

LOOK BACK DAYS

Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

STATUS

By default, only ‘Actionable’ eRx records are included on the eRx Single Patient Queue, however the user can easily change this parameter as described further down on this document.

SSN

This is the eRx Patient Social Security Number (SSN) exactly as it was received from the outside prescriber.

#### Column Header Line

\#

This column indicates the sequence number for the eRx record being displayed, which can be selected by the user to open the eRx Individual record and view the details.

ERX ID

This is the eRx number or ID, which is the same as the eRx Hub.

DRUG NAME

This is the eRx Drug Name exactly as received from the prescriber software. It is truncated at 22 characters.

PROVIDER NAME

This is the eRx Prescriber Name exactly as received from the prescriber software

REC.DATE

This is the date when the eRx was received.

STA

This is eRx Status column. It shows the current eRx record status. It’s truncated at 3 characters.

MATCHING PT

This column indicates the current matching status for the eRx Patient. The following variations are possible for this column:

“” (blank) – eRx Patient has not been matched to a VistA Patient

“A” – eRx Patient has been auto-matched to a VistA Patient

“M” – eRx Patient has been manually matched to a VistA Patient by the user

“M” (bold) – eRx Patient was initially auto-matched and then manually matched to a different VistA Patient by the user

“AV” – eRx Patient has been auto-matched to a VistA Patient and manually validated

“MV” – eRx Patient has been manually matched to a VistA Patient and manually validated

“MV” (bold M) – eRx Patient was initially auto-matched and then manually matched to a different VistA Patient and subsequently manually validated by the user

MATCHING PR

This column indicates the current matching status for the eRx Provider. The following variations are possible for this column:

“” (blank) – eRx Provider has not been matched to a VistA Provider

“A” – eRx Provider has been auto-matched to a VistA Provider

“M” – eRx Provider has been manually matched to a VistA Provider by the user

“M” (bold) – eRx Provider was initially auto-matched and then manually matched to a different VistA Provider by the user

“AV” – eRx Provider has been auto-matched to a VistA Provider and manually validated

“AV” (bold V)– eRx Provider has been auto-matched to a VistA Provider and auto-validated (MbM Only – see below)

“MV” – eRx Provider has been manually matched to a VistA Provider and validated

“MV” (bold M) – eRx Provider was initially auto-matched and then manually matched to a different VistA Provider and subsequently manually validated by the user

MATCHING DR

This column indicates the current matching status for the eRx Drug. The following variations are possible for this column:

“” (blank) – eRx Drug has not been matched to a VistA Drug

“A” – eRx Drug has been auto-matched to a VistA Drug

“M” – eRx Drug has been manually matched to a VistA Drug by the user

“M” (bold) – eRx Drug was initially auto-matched and then manually matched to a different VistA Drug by the user

“AV” – eRx Drug has been auto-matched to a VistA Drug and manually validated

“MV” – eRx Drug has been manually matched to a VistA Drug and manually validated

“MV” (bold M) – eRx Drug was initially auto-matched and then manually matched to a different VistA Drug and subsequently manually validated by the user

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong><u>Provider Auto-Validation</u></strong></p>
<p>An eRx provider will be automatically validated if the following conditions are met when the eRx arrives:</p>
<ul>
<li><p>eRx is not digitally signed (indicating a prescription for a controlled substance)</p></li>
<li><p>eRx Provider was auto-matched</p></li>
<li><p>eRx Provider last name and VistA Provider last names match exactly</p></li>
<li><p>eRx Provider first letter of first name matches the VistA Provider first letter of first name</p></li>
<li><p>First 5 digits of eRx Provider zip code matches exactly with the VistA Provider zip code first 5 digits</p></li>
</ul>
<p>The user recorded as responsible for the validation will be PSOAPPLICATIONPROXY,PSO</p></td>
</tr>
</tbody>
</table>

In the displayed lists, the user can select or enter the line number of the eRx number to view and examine the details of the eRx or select the actions displayed right below the listing area.

Validation actions for a single patient may be complete from there. For more details, refer to the sections identified in this guide.

> **NOTE:** From the Summary/Details screen, users <u>cannot</u> edit any of the VistA information. The validate screens contain the option for editing the VistA information. For further information on editing and validating VistA information for an eR<sub>X</sub>, refer to section 6.2.

#### Listing Area

This area is where all the records are listed. They are always sequential number that goes from 1 to the last item on the list. This number can be selected by the user to view the patient’s corresponding eRx record in the Summary eRx View Display.

\#. Vs. \#\] (Digitally Signed Vs. Not Digitally Signed)

Following each number there will be one of two characters “.” (dot) or “\]” (closing square bracket), as seen on lines 2. 10 and 14 on figure 6-7 above. The “.” indicates that the patient does not have any Digitally Signed eRx records, while the “\]” indicates that the patient has at least one eRx records that was Digitally Signed by the external provider. Digitally signed records is an indication by the external provider that the drug in the eRx records is a Controlled Substance drug. CS drugs are mandated by DEA (Drug Enforcement Agency) to always be transmitted to the pharmacy with a Digital Signature.

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

DET – Show/Hide Details

This action shows or hides the eRx prescription details.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// DET Show/Hide Details Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DET - Show/Hide Details – Shown

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// DET Show/Hide Details Please wait...Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DET - Show/Hide Details - Hidden

IAS – Include All Statuses

This action displays all Actionable and Non-Actionable eRx status codes for a patient. Once the \<IAS\> action is selected, the list is refreshed to display all eRx statuses for the patient. The new status will be displayed in the header section.

For additional information on Actionable and Non-Actionable eRX Status Codes, refer to Appendix B: Holding Queue Status Codes & Descriptions in User Manual Unit 6 available on the Veteran's Documentation Library (VDL) for additional information on the various statuses in the list.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// IAS Include All Statuses Please wait...Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ALL</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y 09/25/23 PR MV MV AV</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S 09/25/23 R01 MV A</p>
<p>3. 99999994 NAPROXEN 250MG TABLET YYYYYY,YYYYY Y 09/25/23 R92 MV MV A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A AV A</p>
<p>6. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>7] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>8. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

IAS - Include All Statuses – eRx Details are Hidden

> **NOTE:** Selecting/entering the \<DET\> action again while displaying all actionable and non-actionable eRx statuses will display the details of each eRx.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong><u>REMOVED Status</u></strong></p>
<p>For MbM sites the status column won’t show “RM” like it does for a VA Medical Center site. Instead, it will show an abbreviation of the Removal Reason which is composed by “R” concatenated with the last 2 numbers of the Removal Reason. Like show above for entries #2 and #3 under the STA (Status) column.</p>
<p>REM01 Drug out of stock or on backorder and unavailable for processing</p>
<p>REM02 Patient was not able to pick up</p>
<p>REM03 Prescription canceled by Provider</p>
<p>REM04 Prescription processed manually</p>
<p>REM05 Provider will cancel this eRx and submit another</p>
<p>REM06 Unable to mail prescription and patient unable to pick up</p>
<p>REM07 Unable to contact patient</p>
<p>REM08 Unable to contact provider</p>
<p>REM09 ERX Issue not resolved-Provider contacted</p>
<p>REM91 Undefined system error</p>
<p>REM92 Other</p></td>
</tr>
</tbody>
</table>

LBD – Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// LBD Change Look Back Days</p>
<p>LOOK BACK DAYS: 45// ?</p>
<p>Type a number between 0 and 1000, 0 decimal digits.</p>
<p>LOOK BACK DAYS: 45// ??</p>
<p>This field holds the number of days to look back in order to include records in</p>
<p>the Single Patient Queue.</p>
<p>LOOK BACK DAYS: 45// 365 Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU – Sort By Drug (hidden)

This action sorts the display list by eRx Drug Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SDRU\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>^</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU - Sort By Drug in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>v</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU - Sort By Drug in Descending Order

SPRO – Sort by Provider (hidden)

This action sorts the display list by eRx Provider Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SPRO\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>^</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRO - Sort By Provider in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>v</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRO - Sort By Provider in Descending Order

SREC – Sort by Rec. Date (hidden)

This action sorts the display list by eRx Received Date. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SREC\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SREC - Sort By Received Date in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>v</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SREC - Sort By Received Date in Descending Order

SSTA – Sort by Status (hidden)

This action sorts the display list by eRx Status. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SSTA\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>^</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SSTA - Sort By Status in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>v</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SSTA - Sort By Status in Descending Order

SPTM – Sort by Pat. Match (hidden)

This action sorts the current matching status for the eRx Patient. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the patient matched first, records with patient matched but not validated next and finally the entries with the patient matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SPTM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPTM SPTM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>^</mark></strong> PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPTM - Sort By Patient Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPTM SPTM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>v</mark></strong> PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPTM - Sort By Patient Match in Descending Order

SPRM – Sort by Prov. Match (hidden)

This action sorts the current matching status for the eRx Provider. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the provider matched first, records with provider matched but not validated next and finally the entries with the provider matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SPRM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRM SPRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR<strong><mark>^</mark></strong> DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRM - Sort By Provider Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRM SPRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR<strong><mark>v</mark></strong> DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRM - Sort By Provider Match in Descending Order

SDRM – Sort by Drug Match (hidden)

This action sorts the current matching status for the eRx Drug. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the drug matched first, records with drug matched but not validated next and finally the entries with the drug matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SDRM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRM SDRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRM - Sort By Drug Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRM SDRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR<strong><mark>v</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRM - Sort By Drug Match in Descending Order

SALL – Sort by All Matches (hidden)

This action sorts the current matching status for the eRx Patient, Provider and Drug. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the patient, provider and drug matched first, records with patient, provider and drug matched but not validated next and finally the entries with the patient, provider and drug matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SALL\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SALL SALL Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>^</mark></strong> PR<strong><mark>^</mark></strong> DR<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SALL - Sort By All Matches in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SALL SALL Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>v</mark></strong> PR<strong><mark>v</mark></strong> DR<strong><mark>v</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SALL - Sort By All Matches in Descending Order

SERX – Sort By eRx ID (hidden)

This action sorts the entries by eRx ID for the patient. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SERX\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SERX SERX Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID<strong><mark>^</mark></strong> DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SERX - Sort By eRx ID in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SERX SERX Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID<strong><mark>v</mark></strong> DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SERX - Sort By eRx ID in Descending Order

BU – Batch Un-Hold (hidden)

This action allows the user to batch un-hold eRx entries for a patient. To perform batch un-hold, the eRx record status should have a HOLD status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BU BU</p>
<p>Select Range: ?</p>
<p>Select the range of eRx entries from the list above. Ex: '1-5'; '1,3,5';</p>
<p>'1-4,6-8'.</p>
<p>Select Range: 2</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X HOR</p>
<p>Additional Comments (Optional): TESTING BU UN-HOLD ACTION FROM eRx Single Patient Queue functionality.</p>
<p>Confirm Batch Un-Hold? N// YES</p>
<p>Updating...done Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Un-Hold

In the example above, after the user successfully performs the batch un-hold action, the status of eRx AMANTADINE 100MG CAP is updated from HOR to I.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Un-Hold Result

If user enters invalid range, the verbiage below will be displayed

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BU BU</p>
<p>Select Range: 100ABC</p>
<p>Invalid Range. Please select a range of entries between 1 and 5.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If user select an eRx entry range whose status is not on hold, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BU BU</p>
<p>Select Range: 3</p>
<p>UNABLE TO BATCH UN-HOLD: At least one eRx entry cannot be removed from HOLD.</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITAMIN C CA XXXXXX,XXXXX X N</p>
<p>REASON: eRx is not on Hold</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BH – Batch Hold (hidden)

This action allows the user to batch hold eRx entries for a patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BH BH</p>
<p>Select Range: ?</p>
<p>Select the range of eRx entries from the list above. Ex: '1-5'; '1,3,5';</p>
<p>'1-4,6-8'.</p>
<p>Select Range: 1-5</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 32MG TAB YYYYYY,YYYYY Y W</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X I</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITAMIN C CA XXXXXX,XXXXX X N</p>
<p>4. 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X N</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X I</p>
<p>Select HOLD reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG INTERACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>598 HCR PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>599 HWR CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>600 HIS PROVIDER DEA# ISSUE</p>
<p>601 HRX HOLD FOR RX EDIT</p>
<p>602 HDE DRUG USE EVALUATION</p>
<p>603 HTI THERAPUTIC INTERCHANGE</p>
<p>604 HSC SCRIPT CLARIFICATION</p>
<p>605 HGS GENERIC SUBSTITUTION</p>
<p>1561 HAL NO ALLERGY ASSESSMENT</p>
<p>1562 HEL ELIGIBILITY ISSUE</p>
<p>1563 HUR HOLD - UN-REMOVE</p>
<p>1599 HFF HOLD FOR FUTURE FILL</p>
<p>Select HOLD reason code: 127 HOR OTHER REASON</p>
<p>Additional Comments (Optional): TESTING BATCH HOLD FROM ERX SINGLE PATIENT QUEUE FUNCTIONALITY.</p>
<p>Confirm Batch Hold? N// YES</p>
<p>Updating...done Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold

In the example above, the user performs the batch hold action on all ACTIONABLE eRx status for a patient. The user then selected 'HOR OTHER REASON' as the reason for holding the eRx. Once the update is done, you can see that the list has been refreshed to reflect the new status, 'HOR'. See the refreshed display list below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold Result

If the user enters an invalid range, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 100ABC</p>
<p>Invalid Range. Please select a range of entries between 1 and 5.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user does not enter a hold reason code, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 3</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X N</p>
<p>Select HOLD reason code: ^Hold Reason required. eRx not placed in a 'Hold' status.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the event the eRx status in the header section is set to ALL (actionable and non-actionable), then the user either selects:

1\. An eRx with non-actionable status

2\. All eRx displayed lists, which both contain actionable and non-actionable status.

The following verbiage will be displayed below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ALL</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y 09/25/23 PR MV MV AV</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S 09/25/23 R01 MV A</p>
<p>3. 99999994 NAPROXEN 250MG TABLET YYYYYY,YYYYY Y 09/25/23 R92 MV MV A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A AV A</p>
<p>6. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>7] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>8. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A AV A</p>
<p>9. 876543 N/A ZZZZZZZ,ZZZZZZ 09/29/23 CAN</p>
<p>10. 41852 N/A ZZZZZZZ,ZZZZZZ 09/29/23 CAH</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BH BH</p>
<p>Select Range: 9-10</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold

In the example below, the user selects eRx’s (#9 and \#10) with a non-actionable status. See the displayed list above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>9. 876543 N/A ZZZZZZZ,ZZZZZZ CAN</p>
<p>10. 741852 N/A ZZZZZZZ,ZZZZZZ CAH</p>
<p>UNABLE TO BATCH HOLD: Either you do not have the appropriate security keys</p>
<p>or one or more records cannot be put on HOLD</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the example below, the user selects All eRx displayed lists, which both contain actionable and non-actionable status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 1-10</p>
<p>UNABLE TO BATCH HOLD: At least one eRx entry cannot be put on HOLD.</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y PR</p>
<p>REASON: eRx with a status of 'Rejected', 'Removed' or 'Processed'.</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S REM01</p>
<p>REASON: eRx with a status of 'Removed'.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient (hidden)

Once in the eRx Single Patient Queue, this action allows the user to automatically open to the next patient with the oldest order after the current patient in an actionable status. The user can type \<NP\> again to jump to the next patient.

For example:

In the eRx Patient Centric Queue, the user selects \#3 from the lists displayed, see below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 27, 2023@11:06:43 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. AAAAA,AAAAAAAAAA 99/99/9990 999-99-9990 44 0 0 1 0 0 1 2</p>
<p>2] BBBBB,BBBBBBBBBB 99/99/9991 999-99-9991 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9994 999-99-9994 37 0 0 1 0 0 1 2</p>
<p>4. CCCCC,CCCCCCCCCC 99/99/9992 999-99-9992 37 3 0 0 1 0 0 4</p>
<p>5. ZZZZZ,ZZZZZZZZZZ 99/99/9993 999-99-9993 37 1 0 1 0 0 0 2</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// <strong>3</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Inside eRx Single Patient Queue, the use enter \<NP\> action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:52 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// NP NP Loading Next Patient...Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient

In the display below, the patient listed in \#4 above in the eRx Single Patient Queue is displayed after entering the \<NP\> action since that is the next patient after XXXXX,XXXXXXXXXX.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:55 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>CCCCCCCCC,CCCCCCCCCCC C</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient

CS – Group by CS/Non CS (hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. To turn ON or OFF the action, enter \<CS\> action the second time, and vice versa.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:52 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><u><strong><mark>CONTROLLED SUBSTANCE Rx's</mark> _ a</strong></u></p>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p><u><strong><mark>NON-CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>3. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CS – Group by CS/Non-CS

CV – Change View (hidden)

This action allows the user to change the following parameters that affect the content and appearance of the eRx Single Patient Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days). Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// CV CV</p>
<p>LOOK BACK DAYS: 365// ?</p>
<p>Type a number between 0 and 1000, 0 decimal digits.</p>
<p>LOOK BACK DAYS: 365// ??</p>
<p>This field holds the number of days to look back in order to include records in</p>
<p>the Single Patient Queue.</p>
<p>LOOK BACK DAYS: 365// 45 DAYS</p>
<p>SORT BY: RE// ?</p>
<p>Indicate the order (Ascending or Descending) to sort the Single Patient</p>
<p>Queue.</p>
<p>Choose from:</p>
<p>ID ERX ID</p>
<p>DR DRUG NAME</p>
<p>PR PROVIDER NAME</p>
<p>RE RECEIVED DATE</p>
<p>STA ERX STATUS</p>
<p>PAM PATIENT MATCH</p>
<p>PRM PROVIDER MATCH</p>
<p>DRM DRUG MATCH</p>
<p>ALL ALL MATCHES</p>
<p>SORT BY: RE// RECEIVED DATE</p>
<p>SORT ORDER: A// ?</p>
<p>Choose from:</p>
<p>A ASCENDING</p>
<p>D DESCENDING</p>
<p>SORT ORDER: A// ASCENDING</p>
<p>DISPLAY DETAILS: NO// ?</p>
<p>Indicate whether the Details (Medication Instructions, Quantity, # of</p>
<p>Refills and Days Supply) should be displayed on the Single Patient Queue</p>
<p>or not.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>DISPLAY DETAILS: NO// ??</p>
<p>This field indicates whether the user wants to display the Details (Medication Instructions, Quantity, # of Refills and Days Supply) for each record on the Single Patient Queue.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>DISPLAY DETAILS: NO// NO NO</p>
<p>GROUP BY CS: NO// ??</p>
<p>This field indicates whether the user wants the entries in the Single Patient Queue grouped by CS and Non-CS (ON) or all together (OFF).</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>GROUP BY CS: NO// Y YES</p>
<p>INCLUDE ALL STATUSES: NO// ??</p>
<p>This field indicates whether the user wants all statuses to be included on the Single Patient Queue or only actionable statuses.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>INCLUDE ALL STATUSES: NO// NO NO</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CV – Change View

If the user already has personal Change View default view saved, this option will display the saved preferences and will give the user the option to delete them.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// cv CV</p>
<p>Your saved default view:</p>
<p>-----------------------</p>
<p>LOOK BACK DAYS : 45 DAYS</p>
<p>SORT BY : ERX ID</p>
<p>SORT ORDER : ASCENDING</p>
<p>DISPLAY DETAILS : YES</p>
<p>GROUP BY CS/NON-CS : NO</p>
<p>INCLUDE ALL STATUSES: NO</p>
<p>Delete this saved default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CV – Change View (User has saved default view)

### eRx Medication Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rx Action on the Patient Centric Queue takes the user to the Rx Medication Queue. Within the Rx Medication Screen (or Rx List View Screen), the user will have the ability to easily filter the list by Message Type by selecting one of the following hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen//</p>
<p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Medication Queue

#### Top Line

| <u>Rx Medication Queue Sep 16, 2023@11:06:54 Page: 1 of 1</u> |
|-------------------------------------------------------------------|

Action Menu the user selected from the eRx Patient Centric Queue. Title of menu “Rx Medication Queue”, followed by the current date/time, and ending with view of current page the user is on and how many pages there are total.

#### Header Area

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In this non-scrollable area, there are 4 fields that the list being displayed.

LOOK BACK DAYS - Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

CS/NON-CS - Indicates Controlled Substances (CS) and Non-Controlled Substances (Non-CS) are displayed, including the CS Schedule (e.g., II-V).

MAXIMUM QUEUE SIZE - This parameter determines the maximum number of records to be loaded for the queue. The process will build and stop once it reaches this limit. The default is 999. User can request up to a maximum of 4,999. This parameter is displayed on the header of the Queue.

ERX STATUS - Indicates the status selection by the user before entering the list (e.g., I-In process, N, New).

#### Column Header Line 

| \# PATIENT DOB DRUG PROVIDER STA REC.DATE<span class="mark">^</span> |
|--------------------------------------------------------------------------|

\# - This column indicates the sequence number for the patient being displayed, which can be selected by the user to open the eRx in the eRx Holding Queue Display view screen (see below for eRx Holding Queue Display description).

PATIENT - Patient name column (maximum of 24 characters).

DOB - Date of birth column (MM/DD/YYY format).

DRUG - This is the eRx Drug Name exactly as received from the prescriber software. It is truncated at 22 characters.

STA - This is eRx Status column. It shows the current eRx record status. It’s truncated at 3 characters.

REC.DATE -This is the date when the eRx was received. By default, the list is always sorted by the REC. DATE column in a descending order (oldest records first) as noted by “<span class="mark">^</span>”.

#### Listing Area

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX I 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This area is where all the eRx records are listed. They are always in sequential order that goes from 1 to the last item on the list. The user will select a record by number to view a detailed description of the eRx in the eRx Holding Queue Display view screen (see below for eRx Holding Queue Display description).

#### Action & Hidden Action Menus

Below the Listing Area includes a few select actions that are available to users to filter or change views. Users can access the Hidden Action Menu by typing “??” (double question mark). Hidden Action Menu will be described further below.

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPAT – Sort By Patient

By default, the list is always sorted by the REC. DATE column in a descending order (oldest records first), but the user can sort the list by the Patient Name by selecting the SPAT action. Once the user selects it once, it will sort the list by Patient Name in an ascending order. If currently sorted by Patient Name and the users selects SPAT again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT<span class="mark">^</span> DOB DRUG PROVIDER STA REC.DATE |
|----------------------------------------------------------------------|

Rx Medication Queue – Sorted By Patient Name in Ascending Order

| \# PATIENT<span class="mark">v</span> DOB DRUG PROVIDER STA REC.DATE |
|----------------------------------------------------------------------|

Rx Medication Queue – Sorted By Patient Name in Descending OrderSQ – Search Queue

This action allows the user to place filters on the list by a few different selection criteria shown below. Multiple filters can be applied in one search criteria.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// SQ Search Queue</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - Search Queue options

SQ 1 - ERX PATIENT

User can filter search criteria by entering patient LAST NAME. Response must contain from 3 to 30 characters. Response must not contain embedded up-arrows (^).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: <strong>1 ERX PATIENT</strong></p>
<p>ERX PATIENT NAME: <strong>XXXXX, XXXXXXX</strong></p>
<p>LAST</p>
<p># ERX PATIENT NAME DOB CITY REC.DATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXXX, XXXXXXX X 99/99/9999 PLANO-TX 01/21/22</p>
<p>2. XXXXX, XXXXXXXX X 99/99/9999 NEW YORK-NY 09/27/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – eRx Patient SelectionNote: The LAST REC.DATE column above displays the last date that the patient received an eRx.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT <strong>(XXXXX, XXXXXX| XXXXX, XXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Patient

SQ 2 – ERX DATE OF BIRTH

User can filter search criteria by entering DATE OF BIRTH.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 2 ERX DATE OF BIRTH</p>
<p>Date of Birth (DOB): 99999999 (XXX 99, 9999)</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT <strong>(XXXXX, XXXXXX| XXXXX, XXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – eRx Patient and DOB filters selected

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1_</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: DOB(99/99/99)|PATIENT(XXXXX,XXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Patient and DOB resultSQ 3 – RECEIVED DATE RANGE

User can filter search criteria by entering a date range for the eRx Received Date. Begin date defaults to T-45 days. End date defaults to today. The Begin Date must not be a future date and the End Date must be earlier or equal to the Begin Date.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 3 RECEIVED DATE RANGE</p>
<p>BEGIN DATE: 09/29/2023//090123 (SEP 01, 2023)</p>
<p>END DATE: 10/19/2023//093023 (SEP 30, 2023)</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE <strong>(09/01/23 TO 09/30/23)</strong></p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Received Date Range

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: 09/08/23-09/28/23</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX PR 09/08/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/11/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/20/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Received Date Range resultSQ 4 – ERX PROVIDER

User can filter search criteria by entering an eRx Provider. This response can be free text. Response must contain from 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 4 ERX PROVIDER</p>
<p>ERX PROVIDER NAME: XXXX, XXXXX</p>
<p># ERX PROVIDER NAME NPI CITY STATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXX, XXXXX 9999999999 BIRMINGHAM AL</p>
<p>SELECT (1-1): 1</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER <strong>(XXXX, XXXXX)</strong></p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Provider

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 2</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PROVIDER(XXXX,XXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX RXA 09/05/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX RXA 09/05/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX R01 09/11/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX PR 09/25/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/27/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<p>9. XXXXX,XXXXXXXX 99/99/9999 ALMOPIDINE 100MG TAB XXXXX,XXXXX N 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Provider resultSQ 5 – ERX STATUS

User can filter search criteria by entering an eRx Order Status. User response must select one specific eRx Order Status. User can type “??” (double question mark) to review list of eRx status reason codes and numbers.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 5 ERX STATUS</p>
<p>ERX STATUS: ??</p>
<p>Choose from:</p>
<p>112 P PENDING</p>
<p>113 A APPROVED</p>
<p>114 PR PROCESSED</p>
<p>115 E ERROR</p>
<p>116 N NEW RX</p>
<p>117 I IN PROCESS</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG REACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit: ^</p>
<p>ERX STATUS: N NEW RX</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS <strong>(N)</strong></p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Status

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>STATUS(N)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX N 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX N 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Status resultSQ 6 – DRUG NAME

User can filter search criteria by entering a drug name or parts of the name. This response is free text and must be between 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 6 DRUG NAME</p>
<p>DRUG NAME: ASP</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME <strong>(‘ASP’)</strong></p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Drug Name

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>DRUG(‘ASP’)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXXXX I 09/20/23</p>
<p>3. XXXX, XXXXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXX W 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Drug Name resultSQ 7 – MESSAGE TYPE

User can filter search criteria by message type. User can type “??” (double question mark) to view list of message types associated with incoming eRx or enter message code.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 7 MESSAGE TYPE</p>
<p>MESSAGE TYPE: ??</p>
<p>This is the message type associated with an incoming eRx request</p>
<p>(Change, Cancel, RxRenewal, Partial Fill, etc.).</p>
<p>Choose from:</p>
<p>RR RXRENEWALREQUEST</p>
<p>RE RXRENEWALRESPONSE</p>
<p>N NEWRX</p>
<p>CR RXCHANGEREQUEST</p>
<p>RXF RXFILL</p>
<p>IE INBOUND ERROR</p>
<p>OE OUTBOUND ERROR</p>
<p>CA CANCELRX</p>
<p>CN CANCELRXRESPONSE</p>
<p>CX RXCHANGERESPONSE</p>
<p>MESSAGE TYPE: N</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE (<strong>NEWRX)</strong></p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Message Type

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1__</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>TYPE(NEWRX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 250MG S.T. XXXXX,XXXXX PR 09/16/23</p>
<p>2. XXXXX,XXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/27/23</p>
<p>3. XXXX, XXXXXXXX 99/99/9999 MELOXICAM 7.5MG TB XXXXX,XXXXX N 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Message Type resultSQ 8 – ERX REFERENCE NUMBER

User can filter search criteria by eRx ID. This search will take the user to the eRx Display screen and show the single eRx selected, which is described further down on this document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 8 ERX ID</p>
<p>ERX ID: 9999999999</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx REFERENCE NUMBERSQ 9 – VISTA RX \#

User can filter search criteria VISTA RX#. This search will first find the eRx record associated with the VISTA Rx \# selected then the user will be taken to the eRx Holding Queue Display to view the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 9 VISTA RX #</p>
<p>Rx #: 9999999999</p>
<p>This prescription is not an eRx prescription.</p>
<p>Rx #:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VISTA RX \#SQ 10 – VISTA PATIENT

Users can filter the list by a single or multiple VistA patients by entering name. Response must contain from 3 to 30 characters. For each VistA Patient selected the software will find all eRx patients that were ever matched to selected VistA patient and will convert this search into an eRx Patient search with all the eRx Patients associated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: 10 VISTA PATIENT</p>
<p>VISTA PATIENT NAME: XXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXX,XXXXXX X 01/13/1970 SERIA LEONE-MT 08/10/23</p>
<p>2. XXXX,XXXXXXXX 09/24/1947 STEELTOWN-NV 08/10/23</p>
<p>3. XXXX,XXXXXXXXX X 02/16/1925 VENICIA-LA 09/30/23</p>
<p>4. XXXX,XXXXXXXXX 11/09/1950 MINOPOLIS-MI 06/20/23</p>
<p>5. XXXX,XXXXXXXX 07/01/1933 ELDORADO-AK</p>
<p>6. XXXX,XXXXXXXX X 07/29/1948 HOVINGTON-MO</p>
<p>7. XXXX,XXXXXXXXXX 07/10/1933 PICKLETON-SD 10/05/23</p>
<p>SELECT (1-9): 1-7</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXX,XXXXX X|XXXX,XXXXXX|XXXX,XXXXXXX,...)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT <strong>(XXXX,XXXXX X|XXXX,XXXXXX|XXXX)</strong></p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VISTA PATIENT

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 10 VISTA PATIENT</p>
<p>VISTA PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXX X 01/13/1970 SERIA LEONE-MT 08/10/23</p>
<p>2. XXXXXXX,XXXXXX X 09/24/1947 STEELTOWN-NV 08/10/23</p>
<p>3. XXXXXXXX,XXXXXX 02/16/1925 VENICIA-LA 09/30/23</p>
<p>4. XXXXXX,XXXXXXX X 11/09/1950 MINOPOLIS-MI 06/20/23</p>
<p>SELECT (1-4): 1-4</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT <strong>(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – VistA Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PATIENT(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VistA Patient resultSQ 11 – VISTA PROVIDER

Users can filter the list by a single or multiple VistA provider by entering name. Response must contain from 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: 11</p>
<p>VISTA PROVIDER NAME: XXX</p>
<p># VISTA PROVIDER NAME DEA CITY REC.DATE</p>
<p>-------------------------------------------------------------------------------</p>
<p>1. XXX,XXXXXXX AM3256181 NEW YORK,NY 10/12/23</p>
<p>2. XXX,XXXXXXX X BD9270911 ROCHESTER,NY 09/21/23</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – VistA Provider Search

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PROVIDER(XXXXX,XXXXXX X|XXXXXXX,XXXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX X I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Provider resultSQ 12 – MATCH STATUS

This search will qualify patients based on the matching status of the patient, provider, and drug to a corresponding VistA Record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 12 MATCH STATUS</p>
<p>Select one of the following:</p>
<p>1 PATIENT FAIL - PATIENT NOT MATCHED</p>
<p>2 PROVIDER FAIL - PROVIDER NOT MATCHED</p>
<p>3 DRUG FAIL - DRUG NOT MATCHED</p>
<p>4 BASIC - PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>MATCH STATUS: 4</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>RX PATIENT</p></li>
<li><p>ERX DATE OF BIRTH</p></li>
<li><p>RECEIVED DATE RANGE</p></li>
<li><p>ERX PROVIDER</p></li>
<li><p>ERX STATUS</p></li>
<li><p>DRUG NAME</p></li>
<li><p>MESSAGE TYPE</p></li>
<li><p>ERX REFERENCE NUMBER</p></li>
<li><p>VISTA RX #</p></li>
<li><p>VISTA PATIENT</p></li>
<li><p>VISTA PROVIDER</p></li>
<li><p>MATCH STATUS (BASIC)</p></li>
</ol>
<p>SEARCH BY: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Match Status

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>MATCH(BASIC)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Match Status result12.1 –MATCH STATUS: PATIENT FAIL - PATIENT NOT MATCHED

If the patient has at least one actionable record which the eRx patient has not yet been matched to a corresponding VistA patient it will be included in the list.

12.2 –MATCH STATUS: PROVIDER FAIL - PROVIDER NOT MATCHED

If the patient has at least one actionable record which the eRx provider has not yet been matched to a corresponding VistA provider AND the patient does not qualify for PATIENT NOT MATCHED filter above, it will be included in the list.

12.3 – MATCH STATUS: DRUG FAIL - DRUG NOT MATCHED

If the patient has at least one actionable record which the eRx Drug has not yet been matched to a corresponding VistA drug AND the patient does not qualify for PATIENT NOT MATCHED filter above AND the patient does not qualify for the PROVIDER NOT MATCHED filter above, it will be included in the list.

12.4 – MATCH STATUS: BASIC - PATIENT, PROVIDER AND DRUG MATCHED

If the patient has at least one actionable record which the eRx patient has been matched to the VistA patient, the eRx Provider has been matched to the VistA provider and the Drug has been matched to a VistA drug AND the patient does not qualify to either of the 3 filters described above, it will be included in the list.

LBD – Change Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s date. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// LBD</p>
<p>LOOK BACK DAYS: 365//45 Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Change Look Back DaysPC – Patient Centric View

This action allows the user to return to the eRx Patient Centric Queue

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Patient Centric Queue

RAF – Remove All Filters

This action allows the user to remove all filters currently applied to the list. This list is then refreshed to without any filters.

REF – Refresh List

This action allows the user to refresh the list. This is used to make sure you’re looking at the latest version of the list because other users might have already worked through some of the records currently on the list which may have altered it the changes won’t show until the list is refreshed. This new action called Refresh (REF) was added to allow the user to re-display the queue. This feature also allows the user to view the latest “locks” from other users that have been placed since the queue was last built.

#### Hidden Action Menus

The user can access the Hidden Action Menu can be viewed by typing “??” (double question mark). The user can use easily filter the list by Message Type by selecting one of the following hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>CS Group By CS CR Change Request only UP Up a line</p>
<p>SDOB Sort by DOB RXF Rx Refill Only DN Down a Line</p>
<p>SDRU Sort By Drug IE Inbound Errors Only FS First Screen</p>
<p>SPRO Sort by Provider OE Outbound Errors Only LS Last Screen</p>
<p>SSTA Sort by Status CA Cancel Rx’s Only GO Go to Page</p>
<p>SREC Sort by Received Date CN Cancel Response Only PS Print Screen</p>
<p>CV Change View CX Change Response Only PT Print List</p>
<p>RRQ Renewal Request Only DET Show/Hide Details SL Search List</p>
<p>RRP Renewal Response Only + Next Screen QU Quit</p>
<p>New New Rx’s Only - Previous Screen</p>
<p>Type &lt;Enter&gt; to continue or ‘^” to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CS – Group By CS (Hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. The action can be used to turn ON and OFF this hidden action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3_______</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><u><strong>CONTROLLED SUBSTANCE Rx's a</strong></u></p>
<p>1] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p>4] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</p>
<p>5] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p><u><strong>NON-CONTROLLED SUBSTANCE Rx's a</strong></u></p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 41 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 40 0 0 1 0 0 0 1</p>
<p>10 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 38 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 35 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 33 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>14 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 1 0 0 0 0 0 1</p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Grouped by CS and Non-CS

SDOB – Sort By Date of Birth (Hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Date of Birth (DOB) by selecting the SDOB hidden action. Once the user selects it once, it will sort the list by Patient DOB in an ascending order. If currently sorted by Patient DOB and the users selects SDOB again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB<span class="mark">^</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Rx Medication Queue – SDOB - Sorted By Patient DOB in Ascending Order

| \# PATIENT DOB<span class="mark">v</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Rx Medication Queue – SDOB - Sorted By Patient DOB in Descending Order

SDRU – Sort By Drug (Hidden)

This hidden action sorts the display list by eRx Drug Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SDRU\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>^</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SDRU - Sort By Drug in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1__</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>v</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – SDRU - Sort By Drug in Descending Order

SPRO – Sort by Provider (Hidden)

This hidden action sorts the display list by eRx Provider Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SPRO\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>^</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SPRO - Sort By Provider in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>v</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SPRO - Sort By Provider in Descending Order

SSTA – Sort by Status (Hidden)

This hidden action sorts the display list by eRx Status. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SSTA\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>^</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SSTA - Sort By Status in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>v</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SSTA - Sort By Status in Descending Order

SREC – Sort by Rec. Date (Hidden)

This hidden action sorts the display list by eRx Received Date. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SREC\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SREC - Sort By received Date in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>v</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SREC - Sort By Received Date in Descending Order

CV – Change View (Hidden)

This hidden action allows the user to change the following parameters that affect the content and appearance of the eRx Patient Centric Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days). Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>LOOK BACK DAYS: 45// 45 DAYS</p>
<p>SORT BY: ED// ED ELAPSED DAYS</p>
<p>SORT ORDER: D// DESCENDING</p>
<p>INCLUDE CS/NON-CS: B// BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE: SCHEDULES II - V// SCHEDULES II - V</p>
<p>GROUP BY CS: NO// NO NO</p>
<p>MAXIMUM QUEUE SIZE: 999//</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Change View hidden action (No Default View Saved)

RRQ – Renewal Request Only (Hidden)

This hidden action allows the user to filter the list by Renewal Request Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RRQ</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRENEWALREQUEST)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX RXR 09/28/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX RXR 09/28/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX RXR 09/28/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXR 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Renewal Request OnlyRRP – Renewal Response Only(Hidden)

This hidden action allows the user to filter the list by Renewal Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RRP</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRESPONSEONLY)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXP 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Renewal Response OnlyNEW – New eRx’s Only (Hidden)

This hidden action allows the user to filter by new Rx’s Only (status in New, In Process, Hold, and Wait)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>NEW</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(NEWRX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX PR 09/08/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/11/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/20/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by New eRx OnlyCR – Change Request Only (Hidden)

This hidden action allows the user to filter by Change Request Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CR</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXCHANGEREQUEST)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX CXN 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Cancel Rx ResponseRXF – Rx Refill Only (Hidden)

This hidden action allows users to filter by Rx Refill Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RXF</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRFILL)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXF 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Medication Queue (Hidden Action) – Filtered by Rx Refill OnlyIE – Inbound Errors Only (Hidden)

This hidden action allows users to filter by Inbound Errors Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>IE</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(INBOUND ERROR)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Inbound Errors OnlyOE – Outbound Errors Only (Hidden)

This hidden action allows users to filter by Outbound Errors Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>OE</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(OUTBOUND ERROR)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Outbound Errors OnlyCA – Cancel Rx’s Only (Hidden)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CA</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRFILL)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 METOPROLOL XXXXX,XXXXX CAO 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Cancel Rx’s OnlyCN – Cancel Response Only (Hidden)

This hidden action allows users to filter by Cancel Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CN</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(CANCELRXRESPONSE)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Inbound Errors OnlyCX – Change Response Only (Hidden)

This hidden action allows users to filter by Change Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CX</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXCHANGERESPONSE)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Change Response OnlyDET – Show/Hide Details (Hidden)

This hidden action will show/hide additional information about each one of the eRx on the list. It will display Qty, \# of Refills, Days Supply, and the SIG (medication instructions).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/99 WARFARIN 2MG TAB XXXXX,XXXXX I 12/13/22</p>
<p>2. XXXXX,XXXXXXXX 99/99/99 METOPROLOL 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) –Hide Details

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>DET</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/99 WARFARIN 2MG TAB XXXXX,XXXXX I 12/13/22</p>
<p><strong>eRx Qty: 30 eRx # of Refills: 0 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE ONE TABLET BY MOUTH EVERY 24 HOURS</strong></p>
<p>2. XXXXX,XXXXXXXX 99/99/99 METOPROLOL 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p><strong>eRx Qty: 90 eRx # of Refills: 15 eRx Days Supply: 90</strong></p>
<p><strong>SIG: TAKE ½ TABLET BY MOUTH EVERY DAY</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Show Details

### Single eRx Details Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A record from the eR<sub>X</sub> Single Patient Queue or Rx Medication Queue can be selected by typing the record number itself. The first screen displayed is the Summary/Details screen, which displays information about the original eR<sub>X</sub> from the external provider and matched VistA information (if any).

On this screen, the header contains the following:

- eR<sub>X</sub> Patient Name and eR<sub>X</sub> Reference \#, which is an internal VA reference number assigned for tracking the eR<sub>X</sub>.
- eRx Message type, which is the message type associated with the incoming eRx (New, Cancel, RxRenewal, etc.) , and Written Date.
- eRx Status appropriate for the incoming eRx.

Below the header is information received from the external provider for the patient, the provider, and the drug/SIG. If the message type is NEWRX, the display will be in a side-by-side format. However, if the message type is one of the following (see NOTE below), the display will not be in side-by-side format, but the data entered will have a reverse video display and highlighted and bolded fonts. These features depend on the terminal display settings being set differently for reverse video and highlighted fonts for them to work.

At the end of the Single eRx View/Display screen, users will find the eRx received time stamp. Additionally, the name of the user who accepted the eRx will also be displayed.

#### eRx Details

To view the details of an eR<sub>X</sub>, select the record number from either the Single Patient eRx Queue or Rx.

> **NOTE:** From the Single eRx Details Display screen, users <u>cannot</u> edit any of the VistA information. The validate screens contain the option for editing the VistA information. For further information on editing and validating VistA information for an eR<sub>X</sub>, refer to section 6.2.

#### Non-Controlled Substance (CS) eRx Details Display

This initial screen shown right after the user selects an individual eRx records shows a summary of the entire eRx record as well as the corresponding VistA matched records. VistA records can be automatically matched by the software or manually entered by the user by selecting the Validation actions VP (Validate Patient), VM (Validate Provider) and VD (Validate Drug). Received Allergy and Diagnosis information are also displayed. Digitally Signed eRx’s will display the additional information shown in the CS Single eRx View/Details Display section.

#### Side-by-Side Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 05, 2024@10:37:33 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>6791230457</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>PR - PROCESSED</strong></p>
<p><u>ERX | VISTA</u></p>
<p><u>PATIENT AUTO-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21</u></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>5555555555</strong></p>
<p><u>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21:52</u></p>
<p>Name: <strong>YYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYY,YYYYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX99999999</strong> |DEA :</p>
<p>Clinic: <strong>EXTERNAL PHARMACY</strong> |</p>
<p><u>DRUG AUTO-MATCHED | VALIDATED by USER,USER on 3/13/24@17:29:10</u></p>
<p>Drug: <strong>BAG,URINARY DRAINAGE MERIT #MD</strong> |Drug: <strong>BAG,DRAINAGE 600ML REMINGTON #6</strong></p>
<p>| <strong>00</strong> <strong>D</strong></p>
<p>Substitution? Renewals? <strong>YES</strong> | <strong>* NON-FORMULARY *</strong></p>
<p>|Drug Message:</p>
<p>| <strong>NATL N/F</strong></p>
<p>SIG: |SIG:</p>
<p><strong>USE ONE BAG AS DIRECTED BY PROVIDER</strong> | <strong>USE ONE BAG AS DIRECTED BY PROVIDER</strong></p>
<p>| <strong>FOR 4 HOURS, THEN USE ONE BAG BY</strong></p>
<p>| <strong>PROVIDER FOR 6 HOURS THIS IS ONLY A</strong></p>
<p>| <strong>TEST</strong></p>
<p>Prescriber Drug Use Evaluation: | Verb: <strong>USE</strong></p>
<p><strong>None</strong> | Dosage: <strong>ONE BAG</strong></p>
<p>| Route: <strong>DIRECTED</strong></p>
<p>| Schedule: <strong>BY PROVIDER</strong></p>
<p>| Duration: <strong>4H (HOURS)</strong></p>
<p>|Conjunction: <strong>THEN</strong></p>
<p>| Verb: <strong>USE</strong></p>
<p>| Dosage: <strong>ONE BAG</strong></p>
<p>| Route: <strong>DIRECTED</strong></p>
<p>| Schedule: <strong>BY PROVIDER</strong></p>
<p>| Duration: <strong>6H (HOURS)</strong></p>
<p>|Patient Instructions:</p>
<p>| <strong>THIS IS ONLY A TEST</strong></p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>| THIS IS ONLY A TEST</p>
<p>Quantity: 120 |Quantity: 1</p>
<p>Dispense Unit: | Dispense Unit: <strong>EA</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |</p>
<p>Days Supply: 90 Refills: 3 |Days Supply: 1 Refills: 10</p>
<p>|Routing: <strong>MAIL</strong></p>
<p>|Clinic: <strong>CHY TEST CLINIC 2</strong></p>
<p>Written: <strong>3/6/24</strong> Effective: |</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
<p>| LIMA BEANS</p>
<p>|Adverse Reactions:</p>
<p>| <u>Verified:</u></p>
<p>| ABROCITINIB</p>
<p>_______________________________________|_____________________________________</p>
<p>Primary Dx: |</p>
<p><strong><u>ICD-10 A01.01 TYPHOID MENINGITIS</u></strong> |</p>
<p><strong>Typhoid meningitis Test primary diagno</strong>|</p>
<p><strong>sis</strong> |</p>
<p>Secondary Dx: |</p>
<p><strong><u>ICD-10 E11.21 TYPE 2 DIABETES MELLITUS</u></strong> |</p>
<p><strong><u>WITH DIABETIC NEPHROPATHY</u></strong> |</p>
<p><strong>Test secondary Diagnosis</strong> |</p>
<p>_______________________________________|_____________________________________</p>
<p><strong>eRx Received on 12/12/23@15:47 - Accepted by USER,USER on 6/05/24@11:12</strong></p>
<p>+ Enter ?? for more actions</p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient, Provider, DrugAuto Matched, Validated and Accepted by the User

If the user manually matched the Patient or the Provider, or the Drug, the only difference is that “AUTO-MATCHED” is changed to “MANUALLY-MATCHED”, as shown below.

| PATIENT MANUALLY-MATCHED \| VALIDATED by USER,USER on 3/13/24@17:21 |
|---------------------------------------------------------------------|

| PROVIDER MANUALLY-MATCHED \| VALIDATED by USER,USER on 3/13/24@17:52 |
|----------------------------------------------------------------------|

| DRUG MANUALLY-MATCHED \| VALIDATED by USER,USER on 3/13/24@17:29 |
|------------------------------------------------------------------|

In the event that the record is edited after it has been auto or manually matched, the Patient, or the Provider, or the Drug header section will display similar information below.

| PATIENT AUTO-MATCHED/EDITED \| VALIDATED by USER,USER on 6/7/24@11:30:22 |
|--------------------------------------------------------------------------|

In the eRx Single View/Display screen, if the eRx status is On-Hold, the eRx Hold Reason will be displayed on the first line or row in the list area if it contains data. If the On-Hold reason is longer than 60 characters, the eRx Hold Reason will be truncated. The last three characters will be replaced with three (3) dots (…), as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:29:09 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXX</strong> eRx Reference #: <strong>789123456</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/08/24</strong></p>
<p>eRx Status: <strong>HWR - CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Hold Reason: <strong>Testing On-Hold Reason longer than 60 characters. Hold Reason t...</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>Primary Phone: <strong>3219998888</strong> |</p>
<p>. . . |</p>
<p>_______________________________________|_____________________________________</p>
<p><strong>eRx Received on 3/13/24@14:03</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To view the entire eRx Hold Reason, users can use the View History Log (HL) action, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// HL HL</p>
<p>Please wait...</p>
<p><u><strong>eRx History Log</strong> Jun 07, 2024@12:59:42 Page: 4 of 9</u></p>
<p>eRx Patient: XXXXXXXXX,XXXXXX</p>
<p>eRx Reference #: 789123456</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>06/07/24@12:35:44 HWR-CS PRESCRIPTION WRITTEN/ISSUE DATE USER,USER</p>
<p><strong>Status Comments: Testing On-Hold Reason longer than 60 characters. Hold</strong></p>
<p><strong>Reason test. This is a test.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the incoming eRx for the patient, provider, or drug is not auto matched, the display is as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:29:09 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXX</strong> eRx Reference #: <strong>789123456</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/08/24</strong></p>
<p>eRx Status: <strong>N – NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT NOT MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>Primary Phone: <strong>3219998888</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER NOT MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYYY,YYYYYY</strong> |Name:</p>
<p>NPI : 0000000000 |NPI :</p>
<p>DEA : |DEA :</p>
<p>Clinic: <strong>TEST NAME</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG NOT MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>IBUPROFEN</strong> |Drug:</p>
<p>Substitution? Renewals? <strong>YES</strong> |Drug Message:</p>
<p>|</p>
<p>SIG: |SIG:</p>
<p>. . . |</p>
<p>_______________________________________|_____________________________________</p>
<p><strong>eRx Received on 3/08/24@14:03</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient, Provider, Drugnot Auto/Manually Matched

#### Non Side-by-Side Display

Below is an example of how the screen will be displayed if the message type (RR, RE, etc.) is one of the following listed above (without the reverse or highlighted video features).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@14:25:39 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>12345678901234</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-APPROVED WITH CHANGES</strong> Written: <strong>01/30/24</strong></p>
<p>eRx Status: <strong>HUR - UN-REMOVED</strong></p>
<p><u>_______________________________________________________________________________</u></p>
<p>eRx Patient Primary Telephone: <strong>5552341234</strong></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>XX/99/99</strong></p>
<p>Vista Patient[v]: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>XX/99/99</strong></p>
<p>_______________________________________________________________________________</p>
<p>eRx Provider Primary Telephone: <strong>5550984567X03</strong></p>
<p>eRx Provider: <strong>YYYYYYYYYY,YYYYYYYY</strong> DEA#: <strong>XX1234567</strong> NPI: <strong>0987654321</strong></p>
<p>Vista Provider[v]: <strong>YYYYYYYYYY,YYYYYYYY</strong> DEA#: NPI: <strong>0987654321</strong></p>
<p>_______________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation:</p>
<p>Co-Agent: <strong>CLONIDINE 0.2MG/24HR PATCH</strong></p>
<p>Reason: <strong>Therapeutic</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: <strong>Does not apply to patient</strong></p>
<p>_______________________________________________________________________________</p>
<p>eRx Drug: <strong>CLONIDINE 0.2MG/24HR PATCH</strong></p>
<p>eRx Qty: <strong>13</strong> eRx Refills: <strong>0</strong> eRx Days Supply:</p>
<p>eRx Written Date: <strong>JAN 30, 2024</strong> eRx Issue Date:</p>
<p>eRx Notes: <strong>TEST COMING FROM XML SIMULATOR</strong></p>
<p>Allergies</p>
<p>Verified: <strong>LISINOPRIL, TESTOSTERONE,</strong></p>
<p>Remote: <strong>No remote data available</strong></p>
<p>Adverse Reactions</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RXRENEWAL RESPONSE INFORMATION</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>APPROVED WITH CHANGES</p>
<p>Response Date/Time: <strong>JAN 30, 2024@11:25:58</strong></p>
<p>RxRenewal Response Comments:</p>
<p>Comments By:</p>
<p>Comments Date/Time:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MEDICATION DISPENSED</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VA Rx#: <strong>Unable to resolve.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RXRENEWAL REQUEST INFORMATION</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Requested By:</p>
<p>Request Date/Time:</p>
<p># of Refills Requested:</p>
<p>RxRenewal Request Comments:</p>
<p>RxRenewal Request Comments:</p>
<p>Comments By:</p>
<p>Comments Date/Time</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MESSAGE HISTORY</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Request Reference #:</p>
<p>New eRx Reference #:</p>
<p>Response eRx Reference #: <strong>12345678901234</strong></p>
<p>_______________________________________________________________________________</p>
<p><strong>eRx Received on 1/30/24@11:25</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Single View/Display Screen – Not Side-by-Side Format and Not Digitally Signed (Non-CS)

In the not side-by-side format, if the Vista information for the patient, provider, or drug is not linked, the display is as shown below:

- VistA Patient: NOT LINKED
- VistA Provider: NOT LINKED
- VistA Drug: NOT LINKED

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@14:25:39 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>123456789012333</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-APPROVED WITH CHANGES</strong> Written: <strong>01/30/24</strong></p>
<p>eRx Status: <strong>HUR - UN-REMOVED</strong></p>
<p><u>_______________________________________________________________________________</u></p>
<p>eRx Patient Primary Telephone: <strong>5552341234</strong></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>XX/99/99</strong></p>
<p>Vista Patient<strong>: NOT LINKED</strong> DOB: <strong>N/A</strong></p>
<p>_______________________________________________________________________________</p>
<p>eRx Provider Primary Telephone: <strong>5550984567X03</strong></p>
<p>eRx Provider: <strong>YYYYYYYYYY,YYYYYYYY</strong> DEA#: <strong>XX1234567</strong> NPI: <strong>0987654321</strong></p>
<p>Vista Provider: <strong>NOT LINKED</strong> DEA#: <strong>N/A</strong> NPI: <strong>N/A</strong></p>
<p>_______________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation:</p>
<p>Co-Agent: <strong>CLONIDINE 0.2MG/24HR PATCH</strong></p>
<p>Reason: <strong>Therapeutic</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: <strong>Does not apply to patient</strong></p>
<p>_______________________________________________________________________________</p>
<p>eRx Drug:</p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<p>Vista Drug: <strong>NOT LINKED</strong></p>
<p>Vista Qty: Vista Refills: Vista Days Supply:</p>
<p>. . .</p>
<p>_______________________________________________________________________________</p>
<p><strong>eRx Received on 1/30/24@11:25</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Single View/Display Screen – Patient, Provider, DrugNot Linked and Not Side-by-Side Format

#### Controlled Substance (CS) eRx Details Display

The only differences from a Non-CS are the two highlighted information below that are include for all Digitally Signed eRx.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:49:40 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>111144455566</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> EPCS DEA VALIDATED</p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>. . . |</p>
<p>Secondary Dx: |</p>
<p><strong><u>ICD-10 E11.21 TYPE 2 DIABETES MELLITUS</u></strong>|</p>
<p><strong><u>WITH DIABETIC NEPHROPATHY</u></strong> |</p>
<p><strong>TESTING SECONDARY DIAGNOSIS</strong> |</p>
<p>Primary Dx: |</p>
<p><strong><u>ICD-10 I10 TYPHOID MENINGITIS</u></strong> |</p>
<p><strong>TESTING ANOTHER PRIMARY DIAGNOSIS</strong> |</p>
<p>_______________________________________|_______________________________________</p>
<p><strong>eRx Received on 6/5/24@12:00</strong></p>
<p><strong>This prescription meets the requirements of the Drug Enforcement Administration</strong></p>
<p><strong>(DEA) electronic prescribing for controlled substances rules (21 CFR Parts 1300</strong></p>
<p><strong>1304, 1306, &amp; 1311).</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen Side-by-Side - Digitally Signed (CS)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:49:40 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>111144455566</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-APPROVED WITH CHANGES</strong> EPCS DEA VALIDATED</p>
<p>eRx Status<strong>: I - IN PROCESS</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>. . .</p>
<p>eRx Drug: <strong>LORAZEPAM 2MG/ML ORAL CONCENTRATE</strong></p>
<p>eRx Qty: <strong>10</strong> eRx Refills: <strong>0</strong> eRx Days Supply: <strong>10</strong></p>
<p>eRx Written Date: <strong>MAR 08, 2024</strong> eRx Issue Date:</p>
<p>eRx Notes: <strong>TAKE 1 TABLET BY MOUTH TWICE DAILY AS NEEDED</strong></p>
<p><strong>This prescription meets the requirements of the Drug Enforcement Administration</strong></p>
<p><strong>(DEA) electronic prescribing for controlled substances rules (21 CFR Parts 1300</strong></p>
<p><strong>1304, 1306, &amp; 1311).</strong></p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ Reject AC (Accept eRx)</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen Non Side-by-Side - Digitally Signed (CS)

> **NOTE:** The fact that an eRx is Digitally Signed does not mean it will become a Controlled Substance VistA prescription. The criteria for an eRx to become a CS VistA Rx is dependent on the VistA Dispense Drug matched to the eRx. If the VistA Dispense Drug is marked as CS then the VistA prescription will be treated as a CS VistA prescription, otherwise it will not.

#### Prescriber Drug Use Evaluation (DUE) Information

The prescriber DUE information is displayed in the Single eRx View/Display Screen only for New Rx, Change Response, and Renewal Response, as shown below.

#### DUE on New eRX

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:49:40 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>200071007</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>04/18/24</strong></p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>. . . |</p>
<p>|</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>VALSARTAN 160MG TAB</strong> |Drug: <strong>VALSARTAN 160MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>PA-F - RESTRICTED TO PTS W/HEART</strong></p>
<p>| <strong>FAILURE (GENERIC NF MENU)</strong></p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET A DAY ON AN EMPTY</strong> | <strong>FOR BLOOD PRESSURE/KIDNEY</strong></p>
<p><strong>STOMACH</strong> | <strong>PROTECTION(2720|680)</strong></p>
<p>Prescriber Drug Use Evaluation: |Patient Instructions:</p>
<p>Co-Agent: <strong>VALSARTAN 160MG TAB</strong> | <strong>FOR ANXIETY - DO NOT DRIVE, OPERATE</strong></p>
<p><strong>RATE</strong> | <strong>MACHINERY, DRINK ALCOHOL, OR USE</strong></p>
<p>Reason: <strong>Therapeutic</strong> | <strong>ILLICIT DRUGS WHILE ON THIS</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong> | <strong>MEDICATION.</strong></p>
<p>Override: <strong>Does not apply to patient</strong> |</p>
<p>...................................... |</p>
<p>Co-Agent: <strong>TESTING</strong> |</p>
<p>Reason: <strong>Drug-Allergy</strong> |</p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong> |</p>
<p>Override: <strong>Has previously tolerated</strong> |</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>This is a TEST NOTE. E-prescribed to |</p>
<p>. . . |</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 5/1/24@12:17</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen – New RX With Prescriber Drug Use Evaluation (DUE)

Below is an example of a record that does not contain a Prescriber Drug Use Evaluation (DUE).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@16:49:40 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>200071007</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>04/18/24</strong></p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>. . . |</p>
<p>|</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>VALSARTAN 160MG TAB</strong> |Drug: <strong>VALSARTAN 160MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>PA-F - RESTRICTED TO PTS W/HEART</strong></p>
<p>| <strong>FAILURE (GENERIC NF MENU)</strong></p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET A DAY ON AN EMPTY</strong> | <strong>FOR BLOOD PRESSURE/KIDNEY</strong></p>
<p><strong>STOMACH</strong> | <strong>PROTECTION(2720|680)</strong></p>
<p>Prescriber Drug Use Evaluation: | Dosage:</p>
<p><strong>None</strong> |Patient Instructions:</p>
<p>| <strong>FOR BLOOD PRESSURE/KIDNEY</strong></p>
<p>| <strong>PROTECTION(2720|680)</strong></p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>This is a TEST NOTE. E-prescribed to |</p>
<p>. . . |</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 5/1/24@12:17</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen – New RX without Prescriber Drug Use Evaluation (DUE)

#### DUE on eRx Change Response

Below is an example of a record with a Change Response message type with a Prescriber Drug Use Evaluation (DUE).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 10, 2024@13:14:59 Page: 1 of 2</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>44194747</strong></p>
<p>eRx Msg Type: <strong>RXCHANGERESPONSE</strong> Written:</p>
<p>eRx Status: <strong>CXN - RXCHANGE RESPONSE - NEW</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient Primary Telephone: <strong>555-555-55555</strong></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> DOB: <strong>3/1/70</strong></p>
<p>Vista Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> DOB: <strong>3/1/70</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: <strong>XX1111111</strong> NPI: <strong>1932288248</strong></p>
<p>Vista Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: NPI: <strong>1932288248</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation:</p>
<p>Co-Agent: <strong>LISINOPRIL 40MG TAB</strong></p>
<p>Reason: <strong>Drug-Allergy</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: Has pr<strong>eviously tolerated</strong></p>
<p>................................................................................</p>
<p>Co-Agent: <strong>RED DYE</strong></p>
<p>Reason: <strong>Drug-Allergy</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: Red Dy<strong>e patient Has previously tolerated.</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug:</p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<p>Vista Drug: <strong>LISINOPRIL 40MG TAB</strong></p>
<p>. . .</p>
<p>________________________________________________________________________________</p>
<p><strong>eRx Received on 4/3/24@21:17</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen – Change Response with Prescriber Drug Use Evaluation (DUE)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 10, 2024@13:14:59 Page: 1 of 2</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>44194747</strong></p>
<p>eRx Msg Type: <strong>RXCHANGERESPONSE</strong> Written:</p>
<p>eRx Status: <strong>CXN - RXCHANGE RESPONSE - NEW</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient Primary Telephone: <strong>555-555-55555</strong></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> DOB: <strong>3/1/70</strong></p>
<p>Vista Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> DOB: <strong>3/1/70</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: <strong>XX1111111</strong> NPI: <strong>1932288248</strong></p>
<p>Vista Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: NPI: <strong>1932288248</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation: <strong>NONE</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug:</p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<p>Vista Drug: <strong>LISINOPRIL 40MG TAB</strong></p>
<p>. . .</p>
<p>________________________________________________________________________________</p>
<p><strong>eRx Received on 4/3/24@21:17</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen – Change Response without Prescriber Drug Use Evaluation (DUE)

#### DUE on eRx Renewal Response

Below is an example of a record with a Renewal Response message type that contain a Prescriber Drug Use Evaluation (DUE).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 10, 2024@13:27:54 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>99999999994321</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-APPROVED WITH CHANGES</strong> Written: <strong>02/29/24</strong></p>
<p>eRx Status: <strong>RXW - RXRENEWAL RESPONSE WAITING</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>6/12/46</strong></p>
<p>Vista Patient[v]: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>6/12/46</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: <strong>XX1111111</strong> NPI: <strong>1366412157</strong></p>
<p>Vista Provider[v]: <strong>YYYYYYYYY,YYY</strong> DEA#: NPI: <strong>1104244151</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation:</p>
<p>Co-Agent: <strong>ROSUVASTATIN</strong></p>
<p>Reason: <strong>Therapeutic</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: Clinic<strong>ian reviewed</strong></p>
<p>................................................................................</p>
<p>Co-Agent: <strong>TESTING 2</strong></p>
<p>Reason: <strong>Drug-Drug Interaction</strong></p>
<p>Result: <strong>Prescribed w/ acknowledgements</strong></p>
<p>Override: Clinic<strong>ian reviewed 2</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>ROSUVASTATIN</strong></p>
<p>eRx Qty: <strong>120</strong> eRx Refills: <strong>2</strong> eRx Days Supply: <strong>90</strong></p>
<p>eRx Written Date: <strong>FEB 29, 2024</strong> eRx Issue Date:</p>
<p>eRx Notes:</p>
<p>Allergies</p>
<p>Verified: <strong>PENICILLIN,</strong></p>
<p><strong>. . .</strong></p>
<p>________________________________________________________________________________</p>
<p><strong>eRx Received on 2/29/24@13:00</strong></p>
<p>+ Enter ?? for more actions</p>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRX Single View/Display Screen – Renewal Response with Prescriber Drug Use Evaluation (DUE)

Below is an example of a record with a Renewal Response message type that does not contain a Prescriber Drug Use Evaluation (DUE).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 10, 2024@13:27:54 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>99999999994321</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-APPROVED WITH CHANGES</strong> Written: <strong>02/29/24</strong></p>
<p>eRx Status: <strong>RXW - RXRENEWAL RESPONSE WAITING</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>6/12/46</strong></p>
<p>Vista Patient[v]: <strong>XXXXXXXXX,XXXXXXXX</strong> DOB: <strong>6/12/46</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYY,YYY</strong> DEA#: <strong>XX1111111</strong> NPI: <strong>1366412157</strong></p>
<p>Vista Provider[v]: <strong>YYYYYYYYY,YYY</strong> DEA#: NPI: <strong>1104244151</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation: <strong>NONE</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>ROSUVASTATIN</strong></p>
<p>eRx Qty: <strong>120</strong> eRx Refills: <strong>2</strong> eRx Days Supply: <strong>90</strong></p>
<p>eRx Written Date: <strong>FEB 29, 2024</strong> eRx Issue Date:</p>
<p>eRx Notes:</p>
<p>Allergies</p>
<p>Verified: <strong>PENICILLIN,</strong></p>
<p><strong>. . .</strong></p>
<p>________________________________________________________________________________</p>
<p><strong>eRx Received on 2/29/24@13:00</strong></p>
<p>+ Enter ?? for more actions</p>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Single View/Display Screen – Renewal Response without Prescriber Drug Use Evaluation (DUE)

#### Rx Details Display – Allergy Information

eRx and VistA information displayed includes allergies and diagnosis. If the patient has no known allergies, eRx displays “NO ALLERGY INFORMATION RECEIVED” in the Allergies section. Vista section displays “NO KNOWN ALLERGIES”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@17:04:30 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>999998</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>12/12/23</strong></p>
<p>eRx Status: <strong>I - IN PROCESS</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>. . . |</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | NO KNOWN ALLERGIES</p>
<p>|</p>
<p>. . . |</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>_______________________________________|_______________________________________</p>
<p><strong>eRx Received on 12/12/23@15:47</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient with No Allergy Assessment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 06, 2024@17:04:30 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>999998</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>12/12/23</strong></p>
<p>eRx Status: <strong>I - IN PROCESS</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>. . . |</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>Allergy: |Allergy:</p>
<p>CIPROFLOXACIN,CODEINE | <u>Verified:</u></p>
<p>| LIMA BEANS</p>
<p>|Adverse Reactions:</p>
<p>| <u>Verified:</u></p>
<p>| ABROCITINIB</p>
<p>. . . |</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>_______________________________________|_______________________________________</p>
<p><strong>eRx Received on 12/12/23@15:47</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient with Known Allergies

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Due to the complexity of the functionality behind the VP (VALIDATE PATIENT), VM (VALIDATE PROVIDER) and VD (VALIDATE DRUG) the action menu actions will be explained separately in the next manual (Section 6, Part 2).

- Manual Validation:
  - \<VP\> [VALIDATE](#_Validate_Patient) PATIENT
  - \<VM\> [VALIDATE](#_Validate_Provider) PROVIDER
  - \<VD\> ([VALIDATE](#_Validate_Drug/SIG) DRUG/SIG)

> NOTE: The VALIDATE DRUG/SIG is not available unless a VistA patient has been matched, as indicated with parenthesis around the action.

#### P – Print

The eRx Print action in the Single eRx View/Display screen was updated to include two new sections: Diagnosis and Prescriber Drug Use Evaluation (DUE) information. However, these sections will only be displayed when the information exists in the eRx.

Printing in the Single eRx View/Display, displays all details of an eR<sub>X</sub> and allows the user to select a local printer and print the eR<sub>X.</sub>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// p Print</p>
<p>DEVICE: ;;999 HOME (CRT)</p>
<p>PHARMACY INFORMATION*</p>
<p>UNDER PHARMACY AMP CHEYENNE VAMC PHARMACY</p>
<p>Address: TEST ADDRESS BOULEVARD</p>
<p>CHEYENNE, WYOMING 00001</p>
<p>Primary Phone: 5552341234 NCPDP: 1111127</p>
<p>*PRESCRIBER INFORMATION</p>
<p>Name: YYYYYYYYY, YYYYYY</p>
<p>Address: UNKNOWN STREET</p>
<p>JULESBURG, COLORADO 807371121</p>
<p>NPI: 1366412157 DEA: XX1234567 State Lic:</p>
<p>Primary Telephone: Fax:</p>
<p>PATIENT INFORMATION</p>
<p>Name: XXXXXXXX,XXXXXXX TEST</p>
<p>DOB: XXX 99, 9999 Sex: MALE Primary Phone: 555-555-55555 SSN: XXXXXXXXX</p>
<p>Address: STREET ADDRESS LINE 1</p>
<p>STREET ADDRESS LINE 2</p>
<p>ARLINGTON, TEXAS 76017</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>PRESCRIPTION INFORMATION*</p>
<p>eRx Drug: LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>NDC: 1472583693 Written Date: JUN 05, 2024 Issue Date:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3</p>
<p>Code List Qualifier: Original Quantity</p>
<p>Drug Form:</p>
<p>Strength:</p>
<p>Substitutions?: YES Prohibit Renewals: No</p>
<p>eRx Sig:</p>
<p>TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>Provider Comments: This is a TEST NOTE FROM PROVIDER.</p>
<p>*PRESCRIBER DRUG USE EVALUATION</p>
<p>Co-Agent: LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>Reason: Therapeutic</p>
<p>Result: Prescribed w/ acknowledgements</p>
<p>Override: Does not apply to patient</p>
<p>...............................................................................</p>
<p>Co-Agent: TESTING</p>
<p>Reason: Drug-Allergy</p>
<p>Result: Prescribed w/ acknowledgements</p>
<p>Override: Has previously tolerated</p>
<p>*DIAGNOSIS INFORMATION*</p>
<p>Primary Dx:</p>
<p>ICD-10 A01.01 TYPHOID MENINGITIS</p>
<p>TESTING PRIMARY DIAGNOSIS</p>
<p>...............................................................................</p>
<p>Secondary Dx:</p>
<p>ICD-10 E11.21 TYPE 2 DIABETES MELLITUS WITH DIABETIC NEPHROPATHY</p>
<p>TESTING SECONDARY DIAGNOSIS</p>
<p>...............................................................................</p>
<p>Primary Dx:</p>
<p>ICD-10 I10 TYPHOID MENINGITIS</p>
<p>TESTING ANOTHER PRIMARY DIAGNOSIS</p>
<p>eRx Reference #: 111144455566 Message ID: NEWRX.442.3825611.3240403.125235</p>
<p>*END OF eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Print eRx Output

#### RJ – Reject

Rejecting an eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes the eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// RJ Reject</p>
<p>Would you like to 'Reject' eRx #33939? Y// ES</p>
<p>Select REJECT reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>203 PTT01 Patient not eligible</p>
<p>204 PTT02 Cannot resolve Patient</p>
<p>205 PVD01 Provider not eligible</p>
<p>206 PVD02 Cannot resolve Provider</p>
<p>207 DRU01 Not eligible for refills</p>
<p>208 DRU02 Non-formulary drug</p>
<p>209 DRU03 Duplicate Prescription found for this Patient</p>
<p>210 DRU04 Invalid Quantity</p>
<p>211 DRU05 Duplicate therapeutic class</p>
<p>212 DRU06 CS prescription written/issue date has problems</p>
<p>213 ERR01 Multiple errors, please contact the Pharmacy</p>
<p>214 ERR02 Incorrect Pharmacy</p>
<p>215 ERR03 Issues with prescription, please contact the pharmacy</p>
<p>1627 PVD03 Missing/bad digital signature on inbound CS ERX</p>
<p>1628 PVD04 Prescriber's CS credential is not appropriate</p>
<p>1629 PTT03 Patient's mailing address is missing/mismatched</p>
<p>1630 ERR99 Other</p>
<p>Select REJECT reason code: PTT01 Patient not eligible</p>
<p>Additional Comments (Optional):</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Reject eRx

#### AC – Accept eRx

Accepting an eRx in the eRX Holding Queue action is not available until the validation of the eR<sub>X</sub> Patient, provider, and drug/SIG have been completed. Also note that the \<AC\> action is not available if the eR<sub>X</sub> is on Hold.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// ac Accept eRx</p>
<p>Errors encountered during processing:</p>
<p>1.) Drug has not been manually validated.</p>
<p>Cannot process eRx.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRx – Drug no validated

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// ac Accept eRx</p>
<p>eRx #99999999 sent to PENDING ORDERS Queue. (Clinic: XXXXXXXXXXXXXX)</p>
<p>Sending rxVerify Message to prescriber.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRx – Drug no validated

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will be prompted to select a Clinic if the current Clinic on the eRx being accepted is different that the Clinic they logged on upon entering the eRx Holding Queue Processing option.</p>
<p>eRx Clinic (Optional): XXXXXXXXXXXXXXXX//</p>
<p>The default clinic will be the Clinic they are logged on.</p></td>
</tr>
</tbody>
</table>

#### H – Hold

This action places eR<sub>X</sub> on Hold in the eR<sub>X</sub> Holding Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// H Hold</p>
<p>Select HOLD reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG INTERACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>129 HPR HOLD DUE TO PATIENT REQUEST</p>
<p>130 HQY QUANTITY OR REFILL ISSUE</p>
<p>1353 HC HOLD DUE TO CHANGE</p>
<p>1618 HCR PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>1619 HWR CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>1620 HIS PROVIDER DEA# ISSUE</p>
<p>1621 HRX HOLD FOR RX EDIT</p>
<p>1622 HDE DRUG USE EVALUATION</p>
<p>1623 HTI THERAPUTIC INTERCHANGE</p>
<p>1624 HSC SCRIPT CLARIFICATION</p>
<p>1625 HGS GENERIC SUBSTITUTION</p>
<p>1631 HAL NO ALLERGY ASSESSMENT</p>
<p>1632 HEL ELIGIBILITY ISSUE</p>
<p>1633 HUR UN-REMOVED</p>
<p>1640 HFF HOLD FOR FUTURE FILL</p>
<p>Select HOLD reason code: HSO INSUFFICIENT STOCK</p>
<p>Additional Comments (Optional):</p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold – Single eRx

Batch Holding

Once the user completes holding one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider. If it does, the software will offer the also put these eRx on hold with the same reason and comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the same day:</p>
<p>PROVIDER: XXXXXXX,XXXXXX eRx RECEIVED DATE: OCT 04, 2023@18:14:50</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------</p>
<p>999999999 NAPROXEN 250MG TAB XXXXXXX,XXXXXX N</p>
<p>999999999 UREA 20% CREAM XXXXXXX,XXXXXX N</p>
<p>Do you want to put them on HOLD-HSO? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Hold

The hold code HOLD FOR CHANGE (HC), besides being used for when the user submits a Change Request to the Provider, can also be used manually to place eRx’s on-hold and also un-hold.

Additionally, a new hold code named HOLD FOR FUTURE FILL (HFF) is being added. This new hold code will work differently than all other hold codes. Once the user selects this code, the software will prompt the user to enter a future fill date. If there is an effective fill date on file for the eRx, this date will be used as the default date, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// h Hold</p>
<p>Select HOLD reason code: HFF HOLD FOR FUTURE FILL</p>
<p><strong>The eRx will be un-held automatically on the date you enter below and placed</strong></p>
<p><strong>in 'IN PROCESS' status.</strong></p>
<p>Future Fill Hold Date: T+10 (JUN 22, 2024)</p>
<p>Additional Comments (Optional): TEST</p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold For Future Fill Date

The Status History (SH) and History Log (HL) actions will display the hold date.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// SH SH</p>
<p>-------------------------------------------------------------------------------</p>
<p>03/18/24@14:39:19 I IN PROCESS</p>
<p>Entered By: USER,USER</p>
<p>Comments:</p>
<p>03/18/24@14:39:19 I IN PROCESS</p>
<p>Entered By: USER,USER</p>
<p>Comments:</p>
<p>03/18/24@14:39:23 I IN PROCESS</p>
<p>Entered By: USER,USER</p>
<p>Comments:</p>
<p>06/12/24@17:50:09 HFF HOLD FOR FUTURE FILL (JUN 22, 2024)</p>
<p>Entered By: USER,USER</p>
<p>Comments: TEST</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold For Future Fill Date – Status History (SH)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// HL HL</p>
<p>Please wait...</p>
<p><u><strong>eRx History Log</strong> Jun 12, 2024@17:55:36 Page: 1 of 2</u></p>
<p>eRx Patient: XXXXXXXXXX,XXXXXX</p>
<p>eRx Reference #: 563333345679</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Pat Auto-Match: Pat Manual Edit:</p>
<p>Prov Auto-Match: Prov Manual Edit: VALIDATED</p>
<p>Drug Auto-Match: Drug Manual Edit:</p>
<p>Status History:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Date/Time Status Entered By</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>03/18/24@14:39:19 I-IN PROCESS USER,USER</p>
<p>03/18/24@14:39:19 I-IN PROCESS USER,USER</p>
<p>03/18/24@14:39:23 I-IN PROCESS USER,USER</p>
<p>06/12/24@17:50:09 HFF-HOLD FOR FUTURE FILL (Jun 22, 2024) USER,USER</p>
<p><strong>Status Comments: TEST</strong></p>
<p>Order:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Date/Time Order# Status</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No Order History Available</p>
<p>Activity Log:</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold For Future Fill Date – History Log (HL)

On the date the eRx was held for it will be automatically un-held and placed on the eRx Holding Queue as In-Process or Wait status.

#### UH – UnHold

This action removes the eR<sub>X</sub> from Hold in the eR<sub>X</sub> Holding Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// UH Un Hold</p>
<p>Additional Comments (Optional):</p>
<p>eRx removed from hold status, and placed to 'In process'.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Holding – Single eRx

Similar to Batch Holding, the Batch Un-Holding performs the opposite functionality. Once the user completes un-holding one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider that have also been put on Hold with the same Hold Code. If it does, the software will offer the also remove these eRx from hold with the same comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the same day:</p>
<p>PROVIDER: XXXXXXX,XXXXXX eRx RECEIVED DATE: OCT 04, 2023@18:14:50</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------</p>
<p>999999999 NAPROXEN 250MG TAB XXXXXXX,XXXXXX N</p>
<p>999999999 UREA 20% CREAM XXXXXXX,XXXXXX N</p>
<p>Do you want to remove them from HOLD? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Un-Holding

#### RM – Remove eRx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Removing the eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>Select Action:Next Screen// RM Remove eRx</p>
<p>Select REMOVAL reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>216 REM01 Drug out of stock or on backorder and unavailable for processing</p>
<p>217 REM02 Patient was not able to pick up</p>
<p>218 REM03 Prescription canceled by Provider</p>
<p>219 REM04 Prescription processed manually</p>
<p>220 REM05 Provider will cancel this eRx and submit another</p>
<p>221 REM06 Unable to mail prescription and patient unable to pick up</p>
<p>222 REM07 Unable to contact patient</p>
<p>223 REM08 Unable to contact provider</p>
<p>224 REM91 Undefined system error</p>
<p>225 REM92 Other</p>
<p>1626 REM09 ERX Issue not resolved-Provider contacted</p>
<p>Select REMOVAL reason code: REM02 Patient was not able to pick up</p>
<p>Additional Comments (Optional):</p>
<p>Would you like to 'Remove' eRx #11137? Y//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch eRx Remove

Once the user completes removing one eRx for the patient, the software checks whether the patient has other eRx records received on the same date from the same provider. If it does, the software will prompt or ask the user to remove these eRx’s with the same reason and comments (if there are any, comments are optional) entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the</p>
<p>same day:</p>
<p>PROVIDER: PROVIDER,PROVIDERNAME eRx RECEIVED DATE: FEB 07, 2024@11:11:54</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>--------------------------------------------------------------------------12345678901235 ASPIRIN 325MG EC TAB PROVIDER,PROVIDERNAME HUR</p>
<p>12345678901237 LISINOPRIL 20MG TAB PROVIDER,PROVIDERNAME HUR</p>
<p>12345678901238 NAPROXEN 500MG TAB PROVIDER,PROVIDERNAME HUR</p>
<p>Do you want to 'Remove' them - REM02? No// <strong>YES</strong></p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Remove

#### Hidden Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Hidden Actions

#### AD – Add a Comment

This option is used to add a record comment to request and responses eRx types regarding refills/renewals.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// AD AD</p>
<p>REQUEST/RESPONSE COMMENTS: // ?</p>
<p>Enter the refill request/response comments. Answer must be 1-255</p>
<p>characters in length.</p>
<p>REQUEST/RESPONSE COMMENTS: // TEST TEST TEST</p>
<p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@18:34:06 Page: 2 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXXX,XXXXXX</strong> eRx Reference #: <strong>V43046209</strong></p>
<p>eRx Msg Type: <strong>RXCHANGEREQUEST</strong> Written: <strong>02/06/24</strong></p>
<p>eRx Status: <strong>CRX - RXCHANGE REQUEST EXPIRED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p><strong>. . .</strong></p>
<p>Qty: <strong>30</strong> Refills: <strong>6</strong> Days Supply: <strong>30</strong></p>
<p>Quantity Unit Of Measure: <strong>TABLET DOSING UNIT</strong></p>
<p>Sig: <strong>TEST TESTING TESTING</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RXCHANGE REQUEST INFORMATION</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Requested By: <strong>USER,USER</strong></p>
<p>Request Date/Time: <strong>MAR 04, 2024@14:46:13</strong></p>
<p>RxChange Request Comments: <strong>TEST TEST TEST</strong></p>
<p>Comments By: <strong>USER,USER</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MESSAGE HISTORY</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Request Reference #: <strong>V43046209</strong></p>
<p>New eRx Reference #: <strong>12345678901239</strong></p>
<p>Response eRx Reference #:</p>
<p>________________________________________________________________________________</p>
<p><strong>eRx Received on 3/4/24@14:46</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Add Comment

#### ACK – Acknowledge

The \<ACK\> hidden action is used by the user to indicate they are aware of the event that caused the eRx to be in the current status, which is the majority of cases is considered Actionable until it is acknowledged by the user and is then updated to a Non-Actionable Status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@18:42:41 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>33332222</strong></p>
<p>eRx Msg Type: <strong>CANCELRX</strong> Written:</p>
<p>eRx Status: <strong>CAO - CANCEL PROCESS COMPLETE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Last New Rx status: <strong>N - NEW</strong></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXX</strong> DOB: <strong>7/12/48</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYY,YYYYY</strong> DEA#: NPI: <strong>1073662086</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>rosuvastatin 40 mg tablet (CRESTOR)</strong></p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CANCEL REQUEST INFORMATION</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Request Status: <strong>CANCEL PROCESS COMPLETE</strong></p>
<p>Requested By: <strong>YYYYYY,YYYYY</strong></p>
<p>Request Date/Time: <strong>MAY 06, 2024@09:11:04</strong></p>
<p>Request Comments:</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p>Select Action:Next Screen// ACK ACK</p>
<p>Would you like to acknowledge this record?</p>
<p>Enter Yes or No: N// YES</p>
<p>Cancel request acknowledged.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@22:01:13 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXX</strong> eRx Reference #: <strong>33332222</strong></p>
<p>eRx Msg Type: <strong>CANCELRX</strong> Written:</p>
<p>eRx Status: <strong>CAA - CANCEL REQUEST ACKNOWLEDGED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYY,YYYYY</strong> DEA#: NPI: <strong>1073662086</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>rosuvastatin 40 mg tablet (CRESTOR)</strong></p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CANCEL REQUEST INFORMATION</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Request Status: <strong>CANCEL REQUEST ACKNOWLEDGED</strong></p>
<p>Requested By: <strong>YYYYYY,YYYYY</strong></p>
<p>Request Date/Time: <strong>MAY 06, 2024@09:11:04</strong></p>
<p>Request Comments:</p>
<p>Comments By:</p>
<p>Comments Date/Time:</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SH – Status History

The Status History \<SH\> hidden action displays the history of status changes on an eR<sub>X</sub> record within the Holding Queue. It does not include the initial status of the record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jul 08, 2024@18:51:26 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>2024070000005</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/02/24</strong></p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>YYYYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYYYY,YYYYYYY</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>5551112222</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 7/2/24@10:09:18</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,PROVIDER</strong> |Name: <strong>PROVIDER,PROVIDER</strong></p>
<p>NPI : <strong>1215926985</strong> |NPI : <strong>1215926985</strong></p>
<p>DEA : AV4538419 |DEA :</p>
<p>Clinic: <strong>TEST BUSINESS NAME</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>LORAZEPAM 1MG TAB</strong> |Drug: <strong>LORAZEPAM 1MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Status History – Hidden Action

Enter the hidden Status History \<SH\> action to display the history of status changes.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// SH SH</p>
<p>---------------------------------------------------------------------------</p>
<p>07/01/24@17:30:36 HAL NO PATIENT ALLERGY ASSESSMENT</p>
<p>Entered By: USER,USER</p>
<p>Comments: Hold for Allergy Assessment</p>
<p>07/01/24@17:35:32 I IN PROCESS</p>
<p>Entered By: USER,USER</p>
<p>Comments:</p>
<p>07/01/24@17:35:38 I IN PROCESS</p>
<p>Entered By: USER,USER</p>
<p>Comments:</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SH Action - Status Changes on eR<sub>X</sub> Record in Holding Queue

Comments are displayed where applicable (i.e. Hold, RJ, and RM statuses).

#### HL – View History Log

The View History Log (HL) hidden action has been added to the eRx Holding Queue Display screen. This action allows the user to display a comprehensive history of the eRx as it moves through the Outpatient Pharmacy software, including activities in Backdoor Pharmacy. The View History Log action will display the following information (if available):

- The Patient, Provider, and Drug Match/Validation Status
- The Status History
- The Order Status
- The Prescription Status
- The Rx Activity Log
- The CMOP Event Log
- The Change, Cancel, Renewal Log - which shows the related messages

> **NOTE:** If no data is available for a section it will display ‘No (section name) Available’.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jul 08, 2024@18:51:26 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>2024070000005</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/02/24</strong></p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>YYYYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYYYY,YYYYYYY</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>5551112222</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 7/2/24@10:09:18</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,PROVIDER</strong> |Name: <strong>PROVIDER,PROVIDER</strong></p>
<p>NPI : <strong>1215926985</strong> |NPI : <strong>1215926985</strong></p>
<p>DEA : AV4538419 |DEA :</p>
<p>Clinic: <strong>TEST BUSINESS NAME</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>LORAZEPAM 1MG TAB</strong> |Drug: <strong>LORAZEPAM 1MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

View History Log Hidden ActionNOTE: If no data is available for a section it will display ‘No (section name) Available’.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx History Log</strong> Jul 08, 2024@18:58:30 Page: 1 of 2</u></p>
<p>eRx Patient: XXXXXXXXX,XXXXXXXX</p>
<p>eRx Reference #: 2024070000005</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Pat Auto-Match: MATCHED Pat Manual Edit: MATCHED</p>
<p>Prov Auto-Match: MATCHED Prov Manual Edit: VALIDATED</p>
<p>Drug Auto-Match: MATCHED Drug Manual Edit:</p>
<p><mark>Status History:</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Date/Time Status Entered By</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No Status History Available</p>
<p><mark>Order:</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Date/Time Order# Status</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No Order History Available</p>
<p><mark>Activity Log:</mark></p>
<p>Date/Time Reason Rx Ref Initiator Of Activity</p>
<p>===========================================================================</p>
<p>No Activity Log Available</p>
<p><mark>CMOP Event Log:</mark></p>
<p>Date/Time Rx Ref TRN-Order Stat NDC</p>
<p>===========================================================================</p>
<p>No CMOP Log Available</p>
<p><mark>Change, Cancel, Renewal Log:</mark></p>
<p><u>Date/Time MessageType eRx ID eRx Order Status</u></p>
<p>07/02/24@10:09:18 NEWRX 2024070000005 N</p>
<p><strong>Status Description: NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

View History Log display

#### EC – eRx Change Request

eR<sub>X</sub> Change Request \<EC\> hidden action is used to request change on a NewRx prescription from the external Provider who sent the original NewRx. The user can exercise EC action on NewRx record in one of the following eRx statuses: N, I, W, or PR and the Vista Patient must be matched and validated.

The eRx Change Request has been significantly improved to facilitate the submission of RX CHANGE REQUEST messages to the prescriber.

> **NOTE:** Every time an eRx Change Request (EC) or Resend eRx Change Request (REC) in invoked:

1.  A RxChangeRequest is sent to the provider to request a change on a new prescription, for example, the change request is due to drug allergy or for generic substitution, etc..
2.  A RxChangeRequest CPRS Progress Note is created regarding the RxChangeRequest sent to the provider.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 10, 2024@17:09:16 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>6791230457</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>W - WAIT</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Cell Phone: |Cell Phone: <strong>5552341234</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER MANUALLY-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21:52</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYYYYY,YYYYYY</strong> |Name: <strong>YYYYYYYY,YYYYYY</strong></p>
<p>NPI : <strong>0000000000</strong> |NPI : <strong>0000000000</strong></p>
<p>DEA : <strong>XX1111111</strong> |DEA :</p>
<p>Clinic: <strong>UNDER PRESCRIBER EXTERNAL am</strong>|</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG MANUALLY-MATCHED | VALIDATED by USER,USER on 3/13/24@17:29:10</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: BAG,URINARY DRAINAGE MERIT #MD |Drug: BAG,DRAINAGE 600ML REMINGTON #600-</p>
<p>| D</p>
<p>Substitution? Renewals? <strong>YES</strong> | <strong>* NON-FORMULARY *</strong></p>
<p>|Drug Message:</p>
<p>. . . |</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 3/13/24@14:03</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Change Request (EC)

> **NOTE:** One new hidden action has been added to the action option display. (See RESEND eRx Change Request)

To enter the eRx RX Change Request Menu, the user will select a patient from the eRx Patient Centric Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>eRx Patient Centric Queue</strong> Apr 05, 2024@14:12:15 Page: 1 of 2</p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<p><mark># PATIENT DOB SSN EDv NW WT IP HD CCR OTH TOT</mark></p>
<p>1. XXXXXX,XXXXX X 99/99/9999 999-99-9999 115 0 1 0 0 1 0 2</p>
<p>2. XXX, XXXXXXXXX X 99/99/9999 999-99-9999 115 0 0 1 0 1 0 2</p>
<p>3. XXXXXXXX, XXXXX 99/99/9999 999-99-9999 66 0 0 0 1 0 0 1</p>
<p>4. XXXXXX,XXXXXXX X 99/99/9999 999-99-9999 66 0 0 1 0 0 0 1</p>
<p>5. XXXXXX, XXXX X 99/99/9999 999-99-9999 59 0 0 0 5 0 0 5</p>
<p>6. XXXXXXXXXXX,XXXXXXXX 99/99/9999 999-99-9999 45 0 1 0 0 0 0 1</p>
<p>7. XXXXX, XXXXX 99/99/9999 999-99-9999 30 0 1 15 1 1 0 18</p>
<p>8. XXXX, XXXXXXXX 99/99/9999 999-99-9999 29 0 1 0 0 0 0 1</p>
<p>+ Select the entry # to view or ?? for more actions</p>
<p>SPAT Sort By Patient SQ Search Queue LBD Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p><strong>Select Item(s): Next Screen// 7</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Patient Centric Queue

The user will then be directed to the eRx Single Patient Queue. The eRx Single Patient Queue will list medications associated with the selected patient. From this screen, the user will select the line number of the medication to be viewed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>eRx Single Patient Queue</strong> Apr 04, 2024@08:24:20 Page: 1 of 1</p>
<p>eRx PATIENT: XXXXXXX, XXXXXXX SEX: <strong>F</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: 999-99-9999 MATCHING</p>
<p><mark># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong>^</strong>STA PT PR DR</mark></p>
<p>1. 999999999 rosuvastatin 40 mg tab XXXXX, XXXX 02/29/24 W <strong>M</strong>V AV AV</p>
<p>2. 999999999 Tetracycline HCL 250MG XXXXX, XXXX 02/29/24 W MV AV AV</p>
<p>Select the entry # to view or ?? for more actions</p>
<p>DET Show/Hide Details IAS Include All Statuses LBD Change Look Back Days</p>
<p>Select: Quit// 1</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Single Patient Queue

From the Single eRx View/Display, the user will Select Action: EC (eRx Change Request) to enter the change request menu.

The Change Request Display populates, and the user will then select which change request option to enter. Below is the description of each change request code and sub-code with or without a predefined template in the NOTE TO PROVIDER (see below for description of Note to Provider).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>S VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// <strong>EC EC</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>rosuvastatin 40 mg tablet (CRESTOR)</strong></p>
<p>eRx SIG : <strong>Take 1 tablet by mouth daily for atherosclerotic cardiovascular disease.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>90</strong> Days Supply: Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Change Request Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// <strong>EC EC</strong></p>
<p><strong>The VistA Patient must be matched and validated first.</strong></p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Vista Patient not matched and validated

The users will now be allowed to send more than one change request for the same eRx. The software will inform the user that one (or more) Change Request(s) has already been sent for the eRx right after they select EC(eRx Change Request) and will allow them to proceed, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>S VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// <strong>EC EC</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>rosuvastatin 40 mg tablet (CRESTOR)</strong></p>
<p>eRx SIG : <strong>Take 1 tablet by mouth daily for atherosclerotic cardiovascular disease.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>90</strong> Days Supply: Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p><strong>2 Rx Change Requests have already been sent for this eRx.</strong></p>
<p># ERX ID ERX TYPE STATUS DATE/TIME</p>
<p>--------------------------------------------------------------------------------</p>
<p>1 V42861749 RXCHANGEREQUEST CRX Feb 16, 2024@17:41:41</p>
<p>2 V42864653 RXCHANGEREQUEST CRX Feb 16, 2024@21:10:07</p>
<p>Select Suggestion Option: (N)EW (R)ESEND:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

EC (eRx Change Request) with more than one eRx’sChange Request already sent

In the “Select Suggestion Option: (N)EW (R)ESEND:” prompt, the user can either generate a New eRx Rx Change Request or Resend the previously sent eRx record. If the user selects the "RESEND" option, the software will then prompt which of the previously sent eRx records to resend. Refer to the Resend Change Request section on how to performed the Resend action.

CHANGE REQUEST CODE

The user is allowed to generate and send the following outbound RX Change Request Code:

- D - DUE (Drug Use Evaluation): May be used to request a prescriber authorize a change to the patient's current medication therapy, such as a dosing regimen change or an alternative medication that will have fewer, or no, adverse effects than the original prescription. This option is not available for CS eRx records.
- G - Generic Substitution: A modification of the product prescribed to a generic equivalent. This option will always be available for selection, and in case the user selects this code for an eRx that already allows substitution, the following message will display.

> CHANGE REQUEST CODE: Generic Substitution

Substitutions are already allowed by prescriber for this eRx.

- OS - Out of Stock: Pharmacy is out of stock of the medication prescribed and it cannot be obtained in a clinically appropriate timeframe. This option is not available for CS eRx records.
- P - Prior Authorization Required: A request to obtain prior authorization before dispensing.
- S - Script Clarification: The pharmacist needs to clarify what the prescriber is sending. This option is not available for CS eRx records.
- T - Therapeutic Interchange/Substitution: A modification of the product prescribed to a preferred product choice. This option is not available for CS eRx records.
- U - Prescriber Authorization: Resolution of the prescriber authorization conflict related to state/federal regulatory requirements is required before dispensing.

  D - DUE (Drug Use Evaluation) CHANGE REQUEST SUB-CODE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CHANGE REQUEST CODE: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Select one of the following:</p>
<p>AR - Adverse Drug Reaction</p>
<p>DA - Drug-Allergy</p>
<p>DD - Drug-Drug Interaction</p>
<p>DI - Drug Incompatibility</p>
<p>DR - Dose Range Conflict</p>
<p>HD - High Dose</p>
<p>ID - Ingredient Duplication</p>
<p>LD - Low Dose</p>
<p>MS - Missing Information/Clarification</p>
<p>PS - Product Selection Opportunity</p>
<p>SX - Drug-Gender</p>
<p>TD - Therapeutic</p>
<p>TP - Payer/Processor</p>
<p>UD - Duplicate Drug</p>
<p>Type '?' for the full list.</p>
<p>CHANGE REQUEST SUB-CODE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Short Sub-Code List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CHANGE REQUEST CODE: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Select one of the following:</p>
<p>AD - Additional Drug Needed</p>
<p>AN - Prescription Authentication</p>
<p>AR - Adverse Drug Reaction</p>
<p>AT - Additive Toxicity</p>
<p>CD - Chronic Disease Management</p>
<p>CH - Call Help Desk</p>
<p>CS - Patient Complaint/Symptom</p>
<p>DA - Drug-Allergy</p>
<p>DC - Drug-Disease (Inferred)</p>
<p>DD - Drug-Drug Interaction</p>
<p>DF - Drug-Food interaction</p>
<p>DI - Drug Incompatibility</p>
<p>DL - Drug-Lab Conflict</p>
<p>DM - Apparent Drug Misuse</p>
<p>DR - Dose Range Conflict</p>
<p>DS - Tobacco Use</p>
<p>ED - Patient Education/Instruction</p>
<p>ER - Overuse</p>
<p>EX - Excessive Quantity</p>
<p>HD - High Dose</p>
<p>IC - Iatrogenic Condition</p>
<p>ID - Ingredient Duplication</p>
<p>LD - Low Dose</p>
<p>LK - Lock In Recipient</p>
<p>LR - Underuse</p>
<p>MC - Drug-Disease (Reported)</p>
<p>MN - Insufficient Duration</p>
<p>MS - Missing Information/Clarification</p>
<p>MX - Excessive Duration</p>
<p>NA - Drug Not Available</p>
<p>NC - Non-covered Drug Purchase</p>
<p>ND - New Disease/Diagnosis</p>
<p>NF - Non-Formulary Drug</p>
<p>NN - Unnecessary Drug</p>
<p>NP - New Patient Processing</p>
<p>NR - Lactation/Nursing Interaction</p>
<p>NS - Insufficient Quantity</p>
<p>OH - Alcohol Conflict</p>
<p>PA - Drug-Age</p>
<p>PC - Patient Question/Concern</p>
<p>OH - Alcohol Conflict</p>
<p>PA - Drug-Age</p>
<p>PC - Patient Question/Concern</p>
<p>PG - Drug-Pregnancy</p>
<p>PH - Preventive Health Care</p>
<p>PN - Prescriber Consultation</p>
<p>PP - Plan Protocol</p>
<p>PR - Prior Adverse Reaction</p>
<p>PS - Product Selection Opportunity</p>
<p>RE - Suspected Environmental Risk</p>
<p>RF - Health Provider Referral</p>
<p>SC - Suboptimal Compliance</p>
<p>SD - Suboptimal Drug/Indication</p>
<p>SE - Side Effect</p>
<p>SF - Suboptimal Dosage Form</p>
<p>SR - Suboptimal Regimen</p>
<p>SX - Drug-Gender</p>
<p>TD - Therapeutic</p>
<p>TN - Laboratory Test Needed</p>
<p>TP - Payer/Processor</p>
<p>UD - Duplicate Drug</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Full List of Sub-Codes in Change RequestDrug Use Evaluation (DUE) Change Request Sub-Codes with NOTE TO PROVIDER pre-populated text content:NOTE:

\- The place holder \[DRUG_NAME\] and \[ADD_TEXT_HERE\] must be replaced before proceeding.

\- The NOTE TO PROVIDER word-processing field only allow a maximum of 250 characters. CTRL + E to save and exit out of provider note.

The user can also used “Num Lock + E” to exit. Num Lock + E automatically save the note without prompting the user if they want to save changes.

AR - Adverse Drug Reaction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Patient has an adverse drug reaction to medication/component of medication prescribed. To fill as is, send denial to this request with note stating reason fill is acceptable. If med should not be filled- Cancel RX and send a replacement</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T======T&gt;============</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DA - Drug-Allergy

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Pt has a listed allergy to medication/component of medication prescribed <strong>[DRUG-NAME]</strong>. Please advise: To fill as is, send denial to this request with note stating reason fill is acceptable. If med should not be filled, Cancel Rx and send replacement</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DD - Drug-Drug Interaction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>eRx drug interacts with <strong>[DRUG_NAME]</strong>. Please advise: To fill this medication, send denial with note stating pt requires both medications or note that <strong>[DRUG_NAME]</strong> should be canceled. If med should not be filled, Cancel RX and send replacement</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DI - Drug Incompatibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>eRx drug is incompatible with <strong>[DRUG_NAME]</strong>. To fill this Rx, send denial with note stating pt requires both medications or a note that <strong>[DRUG_NAME]</strong> should be canceled. If med should not be filled, Cancel Rx and send a replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DR - Dose Range Conflict

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>The prescribe dosage does not align with manufacturer recommendations. Please advise: To fill as is, send denial to this request with note stating reason fill is acceptable. To fill within manufacturer guidelines, approve recommendation below.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

HD – High Dose

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>The prescribed dosage exceeds typical maximum. Please advise: To fill as is, send denial to this request with note stating reason fill is acceptable. To fill within manufacturer guidelines, approve recommendation below</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

ID – Ingredient Duplication

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Pt has medication containing the same ingredient on file. To fill this Rx, send denial with note stating pt requires both medications or note that <strong>[DRUG-NAME]</strong> should be canceled. If med should not be filled-Cancel RX and send a replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

MS - Missing Information/Clarification

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>The eRx is missing or unclear on <strong>[ADD_TEXT_HERE].</strong> Please edit and respond or cancel Rx and send a new prescription with the requested information.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

PS - Product Selection Opportunity

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Pharmacy is unable to supply medication as prescribed; however, alternative options by exist. Please approve an option below or Cancel Rx and send a replacement</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SX - Drug-Gender

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>The prescribed medication does not align with manufacturer recommendations based on patient sex assigned at birth. The pharmacy is unable to fill the medication as prescribed. Pt may obtain locally at usual cash price.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

TD – Therapeutic

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Pt has medication of the same class/indication/drug on file. To fill this Rx, send denial with note stating pt requires both medications or note that <strong>[DRUG_NAME]</strong> should be canceled. If this med should not be filled, Cancel Rx and send a replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

TP - Payer/Processor

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Prior to processing this medication/class the pharmacy is required to obtain a diagnosis code. Please edit an respond or Cancel Rx and send a new prescription with the requested information.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

UD - Duplicate Drug

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>==[ WRAP ] == [INSERT] ========&lt;NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]===</p>
<p>Pt has multiple prescriptions for the same drug and strength on file. To fulfill both Rx, send one Rx containing total qty/directions etc. To fill only this Rx, send denial with note stating other should be canceled. If med should not be filled, Cancel Rx.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=========T&gt;=========</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NOTE TO PROVIDER

A new field called NOTE TO PROVIDER will be presented to the user after the change code (and sub-code) is answered. It is a word-processing field, and it will be pre-populated for most codes/sub-codes selected with a predefined template text. Some predefined texts contain place holders such as \[ADD_TEXT_HERE\] and \[DRUG_NAME\] that must be replaced with the actual information before proceeding.

DRUG SUGGESTION OPTION

The interface for entering drug suggestion was improved to easily allow the user to view, edit, and delete entries before submitted the RX CHANGE REQUEST to the prescriber, as shown below:

After the NOTE TO PROVIDER section has been saved, the user will then have the option to select a New drug suggestion or Finish the change request. This option will be available in each change request code.

> **NOTE:** User will be able to enter up to 9 different drug suggestions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// EC EC</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>ROSUVASTATIN CA 10MG TAB</strong></p>
<p>eRx SIG : <strong>1 tablet Orally Once a day 90 day(s)</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>120</strong> Days Supply: <strong>90</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: DUE (Drug Use Evaluation)</p>
<p>Select one of the following:</p>
<p>AR - Adverse Drug Reaction</p>
<p>DA - Drug-Allergy</p>
<p>DD - Drug-Drug Interaction</p>
<p>DI - Drug Incompatibility</p>
<p>DR - Dose Range Conflict</p>
<p>HD - High Dose</p>
<p>ID - Ingredient Duplication</p>
<p>LD - Low Dose</p>
<p>MS - Missing Information/Clarification</p>
<p>PS - Product Selection Opportunity</p>
<p>SX - Drug-Gender</p>
<p>TD - Therapeutic</p>
<p>TP - Payer/Processor</p>
<p>UD - Duplicate Drug</p>
<p>Type '?' for the full list.</p>
<p>CHANGE REQUEST SUB-CODE: DA Drug-Allergy</p>
<p>NOTE TO PROVIDER:........</p>
<p>==[ WRAP ]==[INSERT ]===========&lt; NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]====</p>
<p>Pt has a listed allergy to medication/component of medication prescribed</p>
<p>ROSUVASTATIN CA 10MG TAB.</p>
<p>Please advise: To fill as is, send denial to this request with</p>
<p>note stating reason fill is acceptable. If med should not be filled, Cancel Rx</p>
<p>and send replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p>
<p>Select Drug Suggestion Option: (N)EW (F)INISH:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Request (EC) – Drug Suggestion

If the user selects (N)EW, the original eRx summary is displayed, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Drug Suggestion Option: (N)EW (F)INISH: n NEW</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>ROSUVASTATIN CA 10MG TAB</strong></p>
<p>eRx SIG : <strong>1 tablet Orally Once a day 90 day(s)</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>120</strong> Days Supply: <strong>90</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Select one of the following:</p>
<p>E USE ERX DRUG</p>
<p>V CHOOSE A VISTA DRUG</p>
<p>DRUG SELECTION: E USE ERX DRUG</p>
<p>eRx Drug: ROSUVASTATIN CA 10MG TAB UPN:</p>
<p>SUBSTITUTIONS? YES//</p>
<p>QUANTITY: 120//</p>
<p>Select one of the following:</p>
<p>38 Original Quantity</p>
<p>40 Remaining Quantity</p>
<p>87 Quantity Received</p>
<p>QS Quantity sufficient as determined by the dispensing pharmacy</p>
<p>QT Quantity Transferred</p>
<p>CF Compound Final Quantity</p>
<p>UQ Central Fill Unit of Use Quantity</p>
<p>QTY QUALIFIER: 38// Original Quantity</p>
<p>QTY UNIT OF MEASURE: TABLET DOSING UNIT C48542 TABLET DOSING UNIT</p>
<p>DAYS SUPPLY: (1-365): 90//</p>
<p># OF REFILLS: (0-11): 3//</p>
<p>SIG Text: ..</p>
<p>==[ WRAP ]==[INSERT ]===============&lt; SIG Text &gt;=====[Press &lt;PF1&gt;H for help]====</p>
<p>1 tablet Orally Once a day 90 day(s)</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p>
<p>ADDITIONAL NOTE TO PROVIDER: TEST NOTE TO PROVIDER</p>
<p>Updating...OK</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 10MG TAB 120 3 90 YES</p>
<p><u>Sig :</u> 1 tablet Orally Once a day 90 day(s)</p>
<p><u>Note:</u> TEST</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After entering the suggested medications the user will be prompted to enter a comment for the field VA PROGRESS NOTE COMMENTS (Optional). The input from the user will be appended to the patient progress note automatically created after the Change Request is submitted to the prescriber.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>. . .</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH: FINISH</p>
<p>VA PROGRESS NOTE COMMENTS (Optional): TESTING VA PROGRESS NOTE COMMENTS.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Request (EC) – VA Progress Note Comments

A Summary will be displayed to the user and a prompt asking if they want to edit the Change Request before submitting to the prescriber, as show below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>RX CHANGE REQUEST SUMMARY</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Change Request Reason Code: <strong>D - DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Reason Sub-Code: <strong>DA - Drug-Allergy</strong></p>
<p>Note to Provider:</p>
<p><strong>Pt has a listed allergy to medication/component of medication prescribed</strong></p>
<p><strong>ROSUVASTATIN CA 10MG TAB.</strong></p>
<p><strong>Please advise: To fill as is, send denial to this request with</strong></p>
<p><strong>note stating reason fill is acceptable. If med should not be filled, Cancel Rx</strong></p>
<p><strong>and send replacement.</strong></p>
<p><u># DRUG QTY # REFS DAYS SUPPLY SUBS</u></p>
<p>1 (E)ROSUVASTATIN CA 10MG TAB 120 3 90 YES</p>
<p><u>Sig :</u> 1 tablet Orally Once a day 90 day(s)</p>
<p><u>Note:</u> TEST</p>
<p>VA Progress Note Comment:</p>
<p><strong>TESTING VA PROGRESS NOTE COMMENTS.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Would you like to edit this Rx Change Request before sending it? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Request (EC) – RX Change Request Summary

Once the user submits the Change Request to the prescriber a Progress Note (refer to the Patient Progress Note section) will be automatically created for the patient. The content of the Progress Note created will be same text from the eRx Change Request Display record addition of the VA PROGRESS NOTE COMMENT field mentioned above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Would you like to edit this Rx Change Request before sending it? NO//</p>
<p>Would you like to send this Rx Change Request? YES//</p>
<p>Sending Request to Provider...Done.</p>
<p>Creating a new Progress Note...Done.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When the response is received from the prescriber for the submitted Change Request an addendum to Progress Note (refer to the Patient Progress Note section) created for the Request will be automatically created with the Change Response content.

In the event the user decides not to send the Rx Change Request, the Rx Change will not be sent, and all the information entered will be lost, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Would you like to edit this Rx Change Request before sending it? NO//</p>
<p>Would you like to send this Rx Change Request? YES// n NO</p>
<p>Are you sure you want to exit (ALL INFORMATION ENTERED WILL BE LOST)? YES// y YES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Cancelled Rx Change Request

#### PA – Patient Allergies

If the VistA patient has known allergies, verified allergies display in the Allergies section. This section will be the same for the Patient Validation as well as for the Drug Validation Screens. Furthermore, the same segment will display in the Pending Order in Backdoor Pharmacy as well. The reverse video for each allergy on either side (eRx or VistA) indicates that the exact allergy was not found on the other side.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 18, 2023@13:37:41 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>999999</strong> Eligibility: <strong>NSC</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : APR 21, 1990 |DOB : JAN 1,1980</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>Sex : MALE |Sex : MALE</p>
<p>Address: |Address:</p>
<p>12345 TEST WAY | 12345 TEST WAY</p>
<p>CHEYENNE,WY 82001 | CHEYENNE,WY 82001</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with Known Allergies

A new hidden action is available on the Patient Validation screen that allows the user to display the Patient Allergies in greater detail. This hidden action can be invoked from the following screens listed below:

- Patient Validation screen
- Drug Validation screen
- eRx Holding Queue Display screen
- Pending Orders screen (Backdoor Outpatient Pharmacy)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>PA Patient Allergies DN Down a Line PS Print Screen</p>
<p>+ Next Screen FS First Screen PT Print List</p>
<p>- Previous Screen LS Last Screen SL Search List</p>
<p>UP Up a Line GO Go to Page QU Quit</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hidden Action (PA) Patient Allergies

When the user selects the Patient Allergies (PA) hidden action from the Patient Validation screen, a new screen displays titled Patient Allergies. The Patient Allergies screen was created to show the eRx patient allergies side-by-side with the VistA patient allergies in detail.

The Patient Allergies screen also contains a new action called VistA Patient Allergies (VPA). The VPA action invokes a new screen titled Detailed Allergy List and this screen allows the user to edit allergy data.

> **NOTE:** A VistA Patient must be matched to use the VistA Patient Allergies (VPA) action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 18, 2023@14:18:39 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : JUN 21, 1954 |DOB : JUN 21,1954</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>Sex : MALE |Sex : MALE</p>
<p>Address: |Address:</p>
<p>PO BOX 9999 | PO BOX 9999</p>
<p>NIRVANA,NY 12345 | NIRVANA,OR 12345</p>
<p>Primary Phone: 9999999999 |</p>
<p>Home Phone: |Home Phone: (999) 999-9999</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// PA PA</p>
<p><u><strong>Patient Allergies</strong> Oct 18, 2023@14:18:43 Page: 1 of 4</u></p>
<p>eRx Reference #: <strong>99999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : JUN 21, 1954 |DOB : JUN 21,1954</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| <u>Drug:</u></p>
<p>| IBUPROFEN</p>
<p>| Effective Date: <strong>Dec 10, 2008@15:29</strong></p>
<p>| Reaction: <strong>OBSERVED</strong></p>
<p>| Severity: <strong>MODERATE</strong></p>
<p>| Symptoms:</p>
<p>| <strong>RASH</strong></p>
<p>| PERCODAN</p>
<p>| Effective Date: <strong>Nov 07, 2008@13:28</strong></p>
<p>| Reaction: <strong>HISTORICAL</strong></p>
<p>| Symptoms:</p>
<p>+ Enter ?? for more actions</p>
<p>VPA Vista Patient Allergies</p>
<p>Select Item(s): Next Screen// VPA Vista Patient Allergies</p>
<p><u><strong>DETAILED ALLERGY LIST</strong> Oct 18, 2023@14:50:25 Page: 1 of 1</u></p>
<p>XXXXX,XXXXXXXXXX &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 182.88 (02/24/2011)</p>
<p>DOB: JUN 21,1954 (69) Wt(kg): 93.44 (02/24/2011)</p>
<p>Verified</p>
<p>Drug:</p>
<p>1 ALBUTEROL</p>
<p>2 IBUPROFEN</p>
<p>3 PERCODAN</p>
<p>4 VALIUM</p>
<p>Drug/Food:</p>
<p>5 EGG PRODUCTS</p>
<p>6 PEANUTS</p>
<p>Food:</p>
<p>7 HONEY</p>
<p>8 TOMATO PRODUCTS</p>
<p>+ Enter ?? for more actions</p>
<p>EA Enter/Edit Allergy/ADR Data SA Select Allergy</p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient Allergies

#### UR – Un-Remove eRx

It is possible after a fillable eRx is Removed, it needs to be moved back to the Holding Queue to be processed. Users can utilize the Include All Statuses (IAS) action on the Single Patient Queue screen or use the Rx List View action on the eRx Patient Centric Queue screen, then use the Search Queue (SQ) action to search for the eRx with a Removed status (ERX STATUS). Once the Removed eRx is selected, the user can utilize the Un-Remove (UR) hidden action on the eRx Holding Queue Display screen. This action will allow users to Un-Remove an eRx that was previously Removed, so the eRx will display again on the eRx Single Patient Queue screen to be worked.

To Un-Remove an eRx from the Holding Queue:

1.  From the eRx Holding Queue Display screen, type \<UM\> Un-Remove eRx.
2.  Enter a HOLD reason code for the eRx Un-Removal.

> NOTE: A default value of HUR (HOLD UNREMOVE) will display and can be selected.

3.  Type Additional Comments as to why the eRx is being Un-Removed and press \<Enter\>.

These comments are optional.

> **NOTE:** Only eRxs with a REMOVED status can be UN-REMOVED.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@10:49:07 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXX</strong> eRx Reference #: <strong>369258</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>REM02 - Patient was not able to pick up</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:34:58</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Home Phone: |Home Phone: 555-2222</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:42:35</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYY,YYYYYY</strong> |Name: <strong>YYYYY,YYYYYY</strong></p>
<p>NPI : 1234567890 |NPI :</p>
<p>DEA : |DEA :</p>
<p>Clinic: <strong>TEST NAME</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:46:07</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: IBUPROFEN |Drug: IBERET-FOLIC-500 TAB</p>
<p>Substitution? Renewals? <strong>YES</strong> |</p>
<p>SIG: |SIG:</p>
<p><strong>ONE TABLET EVERY 4-6 HOURS AS NEEDED</strong> | <strong>TAKE TESTING BY MOUTH 4H FOR 4 HOURS</strong></p>
<p>|</p>
<p><strong>. . .</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 10/18/23@11:18</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// UR UR</p>
<p>Select HOLD reason code: HUR// UN-REMOVED</p>
<p>Additional Comments (Optional): TESTING BATCH UN-REMOVED</p>
<p>Would you like to 'Un-Remove' eRx #369258? Y//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Remove an eRx

Similar to Batch eRx Remove, the Batch Un-Remove performs the opposite functionality. Once the user completes un-removing one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider that have also been put on Remove with the same Remove Code. If it does, the software will prompt or ask the user to un-remove these eRx’s with the same comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the</p>
<p>same day:</p>
<p>PROVIDER: PROVIDER,PROVIDERNAME eRx RECEIVED DATE: MAR 06, 2024@16:43:21</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>8456710 ACETAMINOPHEN 250MG/IBUPROFEN 125M PROVIDER,PROVIDERNAME REM02</p>
<p>6429103 VENETOCLAX 10MGX14/50MG X7/100 PROVIDER,PROVIDERNAME REM02</p>
<p>54123789 POUCH,DRAINABLE,SUR-FIT C#4164 PROVIDER,PROVIDERNAME REM02</p>
<p>6510348 BAG,URINARY DRAINAGE MERIT #MD PROVIDER,PROVIDERNAME REM02</p>
<p>Do you want to 'Un-Remove' them? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Un-Remove eRx

#### Jump to OP

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR, from the eR<sub>X</sub> Holding Queue Summary/Details screen. Once the user has completed reviewing on the Outpatient side, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR only if the following conditions are true:

1.  The R<sub>X</sub> record is a fillable prescription only.
1.  The VistA Patient is already matched to an eR<sub>X</sub> Patient under the Validate Patient \<VP\> action.
2.  The matched VistA Patient has been validated.

To use the Jump to OP action, enter \<??\> to view a list of hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@12:22:24 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>6791230457</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>W - WAIT</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/13/24@17:21</td>
</tr>
</tbody>
</table>
<p>Name: <strong>TESTMBMONE,ONE A</strong> |Name: <strong>TESTMBMONE,ONE A</strong></p>
<p>DOB : <strong>JAN 02, 1960</strong> |DOB : <strong>JAN 2,1960</strong></p>
<p>Cell Phone: |Cell Phone: <strong>5552341234</strong></p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Jump to OP – Hidden Action

Enter the hidden Jump to OP \<JO\> action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@12:37:40 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXX,XXXXXXXXX</strong> eRx Reference #: <strong>741000</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written:</p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT NOT-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXX,XXXXXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>Cell Phone: |Cell Phone:</p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// JO JO</p>
<p>Vista patient has not been validated. Cannot jump to outpatient.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

JO Action Selected (Patient not matched)

If a user attempts to Jump to OP \<JO\> when a VistA Patient is not matched to an eR<sub>X</sub> Patient, an error message is received stating, “VistA patient has not been matched. Cannot jump to outpatient”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@12:37:40 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXX,XXXXXXXXX</strong> eRx Reference #: <strong>741000</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written:</p>
<p>eRx Status: <strong>N - NEW RX</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXX,XXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>Cell Phone: |Cell Phone:</p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// JO JO</p>
<p>Vista patient has not been validated. Cannot jump to outpatient.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

JO Action Selected (Patient not validated)

If a user attempts to Jump to OP \<JO\> from an eR<sub>X</sub> record that is not a fillable prescription, an error message is received stating, “Jumping can only be done on ‘NewRx’ messages, Renewal Response-Replace and fillable RxChange Response messages”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@17:13:38 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>XXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>V44164697</strong></p>
<p>eRx Msg Type: <strong>RXCHANGEREQUEST</strong> Written: <strong>04/03/24</strong></p>
<p>eRx Status: <strong>CRR - RXCHANGE REQUEST RESPONSE RECEIVED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Change Request Type: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Sub Type: <strong>Drug-Drug Interaction</strong></p>
<p>Change Request Reason Text:</p>
<p><strong>eRx drug interacts with TESTING. Please advise: To fill this medication, send denial with note stating pt requires both medications or note that TESTING should be canceled. If med should not be filled, Cancel RX and send replacement.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MEDICATION PRESCRIBED</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Patient Primary Telephone: <strong>555-555-55555</strong></p>
<p>eRx Patient: <strong>PATIENTONE,MBMECREC TEST</strong> DOB: <strong>3/1/70</strong></p>
<p>Vista Patient: <strong>NOT LINKED</strong> DOB: <strong>N/A</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>BROWN,WILLIAM</strong> DEA#: <strong>FB5656802</strong> NPI: <strong>1366412157</strong></p>
<p>Vista Provider: <strong>NOT LINKED</strong> DEA#: <strong>N/A</strong> NPI: <strong>N/A</strong></p>
<p><strong>. . .</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// JO JO</p>
<p>Jumping can only be done on 'NewRx', 'Renewal Response - Replace' and fillable '</p>
<p>RxChange Response' messages.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

JO Action Selected (Invalid Record Type)

Once the user has completed reviewing on the Outpatient side, upon selecting \<Enter\> at the “Select Patient:” prompt, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/002.png)

JO “Select Patient” – Jump Back to Holding Queue eR<sub>X</sub> Summary/Details Screen

#### UX – Un-Process eRx

The Un-Process (UX) hidden action has been added to the eRx Holding Queue Display screen. This action allows the user to Un-Process an eRx order that has been accepted in the eRx Holding Queue \[PSO ERX QUEUE PROCESSING\] and finished in Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]. The following checks are in place to Un-Process an eRx:

- The eRx status for the order must be Processed (PR), RXRENEWAL Response Processed (RXP), or RXCHANGE Response Processed (CXP).
- The user must hold the “PSDRPH” key.
- Only message types NEWRX (N), RXRENEWALRESPONSE (RE) and RXCHANGERESPONSE (CX) can be unprocessed. 
- If message type is RXRENEWALRESPONSE, it must have a Response Value of ‘REPLACE’.
- Must be original fill and not transmitted to CMOP.
- The prescription status must be SUSPENDED or HOLD.

To Un-Process an eRx from the Holding Queue:

1.  From the eRx Holding Queue Display screen, type \<UX\> Un-Process eRx.
2.  Type Additional Comments or accept the default comments and press \<Enter\>.
3.  

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@15:25:12 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>12345678901233</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-REPLACE</strong> Written: <strong>01/30/24</strong></p>
<p>eRx Status: <strong>RXP - RXRENEWAL RESPONSE PROCESSED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXXX</strong> DOB: <strong>99/99/99</strong></p>
<p>Vista Patient[v]: <strong>XXXXXXXX,XXXXXXXX</strong> DOB: <strong>99/99/99</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYYYY,YYYYYY</strong> DEA#: <strong>MT5372963</strong> NPI: <strong>1447816921</strong></p>
<p>Vista Provider: <strong>YYYYYYYYYYY,YYYYYY</strong> DEA#: NPI: <strong>1447816921</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation: <strong>NONE</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>CLONIDINE 0.3MG/24HR PATCH</strong></p>
<p>eRx Qty: <strong>13</strong> eRx Refills: <strong>0</strong> eRx Days Supply: <strong>30</strong></p>
<p>eRx Written Date: <strong>JAN 30, 2024</strong> eRx Issue Date:</p>
<p>Vista Drug[v]<strong>: CLONIDINE 0.3MG/24HR PATC</strong>H</p>
<p>Vista Qty: <strong>13</strong> Vista Refills: <strong>0</strong> Vista Days Supply: <strong>30</strong></p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

|     |
|-----|

Un-Process an eRx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@15:25:12 Page: 1 of 1</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>12345678901233</strong></p>
<p>eRx Msg Type: <strong>RXRENEWALRESPONSE-REPLACE</strong> Written: <strong>01/30/24</strong></p>
<p>eRx Status: <strong>RXP - RXRENEWAL RESPONSE PROCESSED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXXX</strong> DOB: <strong>99/99/99</strong></p>
<p>Vista Patient[v]: <strong>XXXXXXXX,XXXXXXXX</strong> DOB: <strong>99/99/99</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider: <strong>YYYYYYYYYYY,YYYYYY</strong> DEA#: <strong>MT5372963</strong> NPI: <strong>1447816921</strong></p>
<p>Vista Provider: <strong>YYYYYYYYYYY,YYYYYY</strong> DEA#: NPI: <strong>1447816921</strong></p>
<p>________________________________________________________________________________</p>
<p>Prescriber Drug Use Evaluation: <strong>NONE</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>CLONIDINE 0.3MG/24HR PATCH</strong></p>
<p>eRx Qty: <strong>13</strong> eRx Refills: <strong>0</strong> eRx Days Supply: <strong>30</strong></p>
<p>eRx Written Date: <strong>JAN 30, 2024</strong> eRx Issue Date:</p>
<p>Vista Drug[v]<strong>: CLONIDINE 0.3MG/24HR PATC</strong>H</p>
<p>Vista Qty: <strong>13</strong> Vista Refills: <strong>0</strong> Vista Days Supply: <strong>30</strong></p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Quit// UX UX</p>
<p>Comments: Un-Process for correction Replace</p>
<p>Would you like to 'Un-Process' eRx #12345678901233 and Rx #3059528? Y//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Process an eRx

#### PN – Patient Progress Note

A shortcut to the existing hidden action PN – Progress Note (OP) in the Backdoor Pharmacy was added to the eRx Holding queue so that the user could enter a Progress Note for the VistA patient before accepting the eRx. In order to use this action the VistA patient must have been matched and validated. For more information on Progress Notes, please refer to the Outpatient Pharmacy User Manual in the Veteran's Documentation Library (VDL).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@17:25:03 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXX,XXXXXXXXXXXX</strong> eRx Reference #: <strong>563333345679</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>I - IN PROCESS</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/22/24@14:32:12</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXX,XXXXXXXXXXXX</strong> |Name: <strong>XXXXXXX,XXXXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>Cell Phone: |Cell Phone: 5556781234</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER MANUALLY-MATCHED | VALIDATED by USER,USER on 3/22/24@14:33:35</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYYYYY,YYYYY</strong> |Name: <strong>YYYYYYYY,YYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : XXB5656802 |DEA :</p>
<p>Clinic: <strong>EXTERNAL PROVIDER CLINIC</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG NOT MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong>ROSUVASTATIN CA 10MG TAB</strong> |Drug:</p>
<p>Substitution? Renewals? <strong>YES</strong> |</p>
<p>SIG: |SIG:</p>
<p><strong>1 tablet Orally Once a day 90 day(s)</strong> |</p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Request Patient Progress Note

Once the user submits the Change Request to the prescriber, a Patient Progress Note will be automatically created for the patient with a title of ERX RX CHANGE REQUEST NOTE. The content of the Progress Note created will be same text from the eRx Change Request Display record, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>LOCAL TITLE: ERX RX CHANGE REQUEST NOTE</p>
<p>STANDARD TITLE: PHARMACY PROGRESS NOTE</p>
<p>DATE OF NOTE: MAY 02, 2024@10:50:49 ENTRY DATE: MAY 02, 2024@10:50:49</p>
<p>AUTHOR: USER,USER EXP COSIGNER:</p>
<p>URGENCY: STATUS: COMPLETED</p>
<p>SUBJECT: IBUPROFEN:IBUPROFEN</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX</p>
<p>eRx Reference #: V45261983</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>RXCHANGEREQUEST</p>
<p>Change Request Type: DUE (Drug Use Evaluation)</p>
<p>Change Request Sub Type: Missing Information/Clarification</p>
<p>Change Request Reason Text:</p>
<p>The eRx is missing or unclear on TESTING MORE THAN 1 DUE SAMPLE DISPLAY, Please</p>
<p>edit and respond or cancel Rx and send a new prescription with the requested</p>
<p>information.</p>
<p>MEDICATION PRESCRIBED</p>
<p>eRx Patient Primary Telephone: 555-555-5555</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX DOB: 99/99/99</p>
<p>eRx Provider: YYYYYYYY,YYYYYYYY</p>
<p>DEA#: XX5656802 NPI: 1366412157</p>
<p>eRx Drug: IBUPROFEN 200MG TAB</p>
<p>eRx Qty: 20 eRx Refills: 3 eRx Days Supply: 30</p>
<p>eRx Written Date: APR 18, 2024 eRx Issue Date:</p>
<p>eRx Sig: TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Provider Notes/Comments:</p>
<p>This is a TEST NOTE.</p>
<p>MEDICATION REQUESTED 1</p>
<p>Drug: IBUPROFEN 200MG TAB</p>
<p>Substitutions: YES</p>
<p>Note: TESTING MORE THAN 1 DUE SAMPLE DISPLAY.</p>
<p>Qty: 20 Refills: 3 Days Supply: 30</p>
<p>Quantity Unit Of Measure: TABLET DOSING UNIT</p>
<p>Sig: TESTING MORE THAN ONE DUE. TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>RXCHANGE REQUEST INFORMATION</p>
<p>Requested By: USER,USER</p>
<p>Request Date/Time: MAY 02, 2024@10:50:49</p>
<p>RxChange Request Comments:</p>
<p>Comments By:</p>
<p>Comments Date/Time:</p>
<p>*MESSAGE HISTORY</p>
<p>Request Reference #: V45261983</p>
<p>New eRx Reference #: 2000510005</p>
<p>Response eRx Reference #:</p>
<p>TESTING VA PROGRESS NOTE COMMENTS.</p>
<p>Provider's feedback pending.</p>
<p>/es/ USER R USER</p>
<p>OIT</p>
<p>Signed: 05/02/2024 10:50</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Request Patient Progress NoteeRx Change Response Patient Progress Note Addendum

When the response is received from the prescriber for the submitted change request, an addendum to the patient progress note created when the change request was submitted will be automatically created with the same change response content that you see when viewing the change response record in the Single eRx Detail Display screen.

In CPRS, the eRx Change Request and Response would like similar below:

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/003.png)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>LOCAL TITLE: Addendum</p>
<p>STANDARD TITLE: ADDENDUM</p>
<p>DATE OF NOTE: MAY 02, 2024@10:59:01 ENTRY DATE: MAY 02, 2024@10:59:01</p>
<p>AUTHOR: USER,USER EXP COSIGNER:</p>
<p>URGENCY: STATUS: COMPLETED</p>
<p>SUBJECT: IBUPROFEN</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX</p>
<p>eRx Reference #: 202445261983</p>
<p>eRx HT: (cm)() eRx WT: 99.79(kg)()</p>
<p>RXCHANGERESPONSE</p>
<p>eRx Status: CXN - RXCHANGE RESPONSE - NEW</p>
<p>MEDICATION PRESCRIBED</p>
<p>eRx Patient Primary Telephone: 555-555-5555</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX DOB: 99/99/99</p>
<p>eRx Provider: YYYYYY,YYYYYYY</p>
<p>DEA#: FB5656802 NPI: 1366412157</p>
<p>Prescriber Drug Use Evaluation:</p>
<p>Co-Agent: Ibuprofen</p>
<p>Reason: Drug-Allergy</p>
<p>Result: Prescribed w/ acknowledgements</p>
<p>Acknowledgement: Has previously tolerated</p>
<p>................................................................................</p>
<p>Co-Agent: RED DYE</p>
<p>Reason: Drug-Allergy</p>
<p>Result: Prescribed w/ acknowledgements</p>
<p>Acknowledgement: Red Dye patient Has previously tolerated.</p>
<p>eRx Drug:</p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<p>Vista Drug: IBUPROFEN 200MG TAB</p>
<p>Vista Qty: Vista Refills: Vista Days Supply:</p>
<p>Substitutions? :</p>
<p>Vista Sig:</p>
<p>Pat Inst: WITH FOOD FOR PAIN/INFLAMMATION(638|5051)</p>
<p>Hold Status:</p>
<p>Hold Reason:</p>
<p>Placed on hold by:</p>
<p>eRx Notes:</p>
<p>/es/ USER U USER</p>
<p>OIT</p>
<p>Signed: 05/02/2024 10:59</p>
<p>==============================================================================</p>
<p>--- Original Document ---</p>
<p>05/02/24 ERX RX CHANGE REQUEST NOTE:</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX</p>
<p>eRx Reference #: V45261983</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>RXCHANGEREQUEST</p>
<p>Change Request Type: DUE (Drug Use Evaluation)</p>
<p>Change Request Sub Type: Missing Information/Clarification</p>
<p>Change Request Reason Text:</p>
<p>The eRx is missing or unclear on TESTING MORE THAN 1 DUE SAMPLE DISPLAY, Please</p>
<p>edit and respond or cancel Rx and send a new prescription with the requested</p>
<p>information.</p>
<p>MEDICATION PRESCRIBED</p>
<p>eRx Patient Primary Telephone: 555-555-5555</p>
<p>eRx Patient: XXXXXXXXXXX,XXXXXXXXXXXX DOB: 99/99/99</p>
<p>eRx Provider: YYYYYYYY,YYYYYYYYYYY</p>
<p>DEA#: FB5656802 NPI: 1366412157</p>
<p>eRx Drug: IBUPROFEN 200MG TAB</p>
<p>eRx Qty: 20 eRx Refills: 3 eRx Days Supply: 30</p>
<p>eRx Written Date: APR 18, 2024 eRx Issue Date:</p>
<p>eRx Sig: TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Provider Notes/Comments:</p>
<p>This is a TEST NOTE.</p>
<p>MEDICATION REQUESTED 1</p>
<p>Drug: IBUPROFEN 200MG TAB</p>
<p>Substitutions: YES</p>
<p>Note: TESTING MORE THAN 1 DUE SAMPLE DISPLAY.</p>
<p>Qty: 20 Refills: 3 Days Supply: 30</p>
<p>Quantity Unit Of Measure: TABLET DOSING UNIT</p>
<p>Sig: TESTING MORE THAN ONE DUE. TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>RXCHANGE REQUEST INFORMATION</p>
<p>Requested By: USER, USER</p>
<p>Request Date/Time: MAY 02, 2024@10:50:49</p>
<p>RxChange Request Comments:</p>
<p>Comments By:</p>
<p>Comments Date/Time:</p>
<p>*MESSAGE HISTORY</p>
<p>Request Reference #: V45261983</p>
<p>New eRx Reference #: 2000510005</p>
<p>Response eRx Reference #:</p>
<p>TESTING VA PROGRESS NOTE COMMENTS.</p>
<p>Provider's feedback pending.</p>
<p>/es/ USER U USER</p>
<p>OIT</p>
<p>Signed: 05/02/2024 10:50</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Change Response Patient Progress Note Addendum

|     |
|-----|

#### AU – View Audit Log

View Audit Log \<AU\> hidden action is used to view all edits made to a VistA Patient, Provider, and Drug/Sig. This feature will also capture any edits made by auto-matching and display them on the Audit Log.

Once the user selects View Audit Log \<AU\>, the Audit Log report will display.

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/004.png) eRx Audit Log

Users are able to sort the Audit Log by Date/Time \<DT\>, Field \<FN\>, Edited By \<EB\>, or Show/Hide eRx Value \<SH\>. All sort options contain a sort indicator to inform the user if the results are in ascending \[^\] or descending \[v\] order. To change the chronological order of the Audit Log display, enter the sort option a second time.

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/005.png)

eRx Audit Log Sorted by Date/Time Ascending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/006.png)

eR<sub>X</sub> Audit Log Sorted by Date/Time Descending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/007.png)

eR<sub>X</sub> Audit Log Sorted by Edited By Ascending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/008.png)

eR<sub>X</sub> Audit Log Sorted by Edited By Descending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/009.png)

eR<sub>X</sub> Audit Log Sorted by Field Ascending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/010.png) eR<sub>X</sub> Audit Log Sorted by Field Descending

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/011.png)

eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Shown

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/012.png)

eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Hidden

To exit the Audit Log \<AU\> and return to the eRx Holding Queue Display, press ‘Enter’.

#### <span class="mark">VS – View Suggestion(s)</span>

A new hidden action called View Suggestion(s) (VS) is being added to the Validate Patient, Validate Provider and Validate Drug screens. This feature will allow users to view and manage suggestions at any time, before or after the eRx has been accepted/processed. For detailed information about VS -View Suggestions(s) action, refer to <u>Unit 7 Part</u> 2 available on the Veteran's Documentation Library (VDL).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Jun 11, 2024@17:49:47 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>200071007</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED | VALIDATED by USER,USER on 5/1/24@17:33:10</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX PATIENT | VISTA PATIENT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>XXXXXXXX,XXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>0000000000</strong> |SSN : <strong>000-000-0000</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>STREET ADDRESS LINE 1 STREET ADDRESS</strong> | <strong>STREET ADDRESS LINE 1 STREET ADDRESS</strong></p>
<p><strong>LINE 2</strong> | <strong>LINE 2</strong></p>
<p><strong>ARLINGTON</strong>,<strong>TX</strong> <strong>76017</strong> | <strong>ARLINGTON</strong>,<strong>TX</strong> <strong>76017</strong></p>
<p>Primary Phone: 555-555-55555 |</p>
<p>Home Phone: |Home Phone: <strong>555-555-5555</strong></p>
<p>Cell Phone: |Cell Phone: <strong>555-555-5555</strong></p>
<p>_______________________________________|_______________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|_______________________________________</p>
<p>Allergy: |Allergy:</p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>PA Patient Allergies DN Down a Line PS Print Screen</p>
<p>VS View Suggestion(s) FS First Screen PT Print List</p>
<p>+ Next Screen LS Last Screen PT Print List</p>
<p>- Previous Screen GO Go to Page SL Search List</p>
<p>UP Up a Line QU Quit</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation – View Suggestions(s) (VS)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Jun 11, 2024@17:55:52 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>200071007</strong> eRx Patient: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>Status: <strong>AUTO-MATCHED | VALIDATED by USER,USER on 5/1/24@17:33:39</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX PROVIDER | VISTA PROVIDER</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYYY,YYYYY</strong> |Name: <strong>YYYYYY,YYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : XX5656802 |DEA :</p>
<p>Clinic: <strong>UNDER PRESCRIBER EXTERNAL am</strong>|</p>
<p><strong>p TEST CLINIC 1</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Address: |Address:</p>
<p>900 CEDAR STREET | 4700 Lady Moon Dr</p>
<p>JULESBURG,<strong>CO</strong> 80737 | Fort Collins,<strong>CO</strong> 80528</p>
<p>Tel: |Tel: (888) 888-8888</p>
<p>_______________________________________|________________________________________</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// ??</p>
<p>The following actions are also available:</p>
<p>VS View Suggestion(s) DN Down a Line PS Print Screen</p>
<p>+ Next Screen FS First Screen PT Print List</p>
<p>- Previous Screen LS Last Screen SL Search List</p>
<p>UP Up a Line GO Go to Page QU Quit</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Provider Validation – View Suggestions(s) (VS)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Drug Validation</strong> Jun 11, 2024@18:06:32 Page: 1 of 3</u></p>
<p>eRx Reference #: <strong>200071007</strong> eRx Patient: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>Date Written : <strong>4/18/24</strong> Effective Date:</p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX MED | VISTA MED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
<p>| ROSEMARY</p>
<p>|Adverse Reactions:</p>
<p>| <u>Verified:</u></p>
<p>| SIMPLYTHICK</p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>VALSARTAN 160MG TAB</strong> |<u>1)</u>Drug: <strong>VALSARTAN 160MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>PA-F - RESTRICTED TO PTS W/HEART</strong></p>
<p>| <strong>FAILURE (GENERIC NF MENU)</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET A DAY ON AN EMPTY</strong> | <strong>FOR BLOOD PRESSURE/KIDNEY</strong></p>
<p><strong>STOMACH</strong> | <strong>PROTECTION(2720|680)</strong></p>
<p>. . . |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation RJ Reject</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>PA Patient Allergies UP Up a Line PS Print Screen</p>
<p>VS View Suggestion(s) DN Down a Line PT Print List</p>
<p>+ Next Screen FS First Screen SL Search List</p>
<p>- Previous Screen GO Go to Page QU Quit</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug/SIG Validation – View Suggestions(s) (VS)

#### <span class="mark">JE – Jump to eRx Patient</span>

A new hidden action called Jump to eRx Patient (JE) is being added to the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option. It will be available in the Patient Information screen as well as in the Medication Profile screen. This option will allow the user to jump to the eRx Single Patient Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Information</strong> Jun 11, 2024@18:23 Page: 1 of 2</u></p>
<p>XXXXXXX,XXXXXXXX &lt;A&gt;</p>
<p>PID: 000-00-0000 Ht(cm): _______ (______)</p>
<p>DOB: XXX 99,9999 (62) Wt(kg): 94.80 (06/28/2021)</p>
<p>SEX: MALE <u>eRx &amp; Non-VA Meds on File - Last Non-VA Entry on 08/18/21</u></p>
<p>CrCL: &lt;Not Found&gt; (CREAT: 1.06mg/dL 6/22/21) BSA (m2): _______</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Eligibility: NSC</p>
<p>RX PATIENT STATUS: OUTPT NON-SC</p>
<p>Disabilities:</p>
<p>6619 ECHO CIR</p>
<p>HOME PHONE:</p>
<p>FIRESTONE CELL PHONE: (999) 999-9999</p>
<p>COLORADO 80504-5704 WORK PHONE: (999) 999-9999</p>
<p>Prescription Mail Delivery: Regular Mail</p>
<p>Allergies</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>EA Enter/Edit Allergy/ADR Data PU Patient Record Update</p>
<p>DD Detailed Allergy/ADR List EX Exit Patient List</p>
<p>Select Action: Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>IN Intervention Menu FS First Screen ADPL Auto Display(On/Off)</p>
<p>+ Next Screen LS Last Screen QU Quit</p>
<p>- Previous Screen GO Go to Page ARI View Addtnl Rej Info</p>
<p>UP Up a Line RD Re Display Screen VER View ePharmacy Rx</p>
<p>DN Down a Line PS Print Screen EPR Print eRx</p>
<p>&gt; Shift View to Right PT Print List JE Jump to eRx Patient</p>
<p>&lt; Shift View to Left SL Search List</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Information Prescription Processing Screen – Jump to eRx Patient (JE)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Medication Profile</strong> Jun 11, 2024@18:32:54 Page: 1 of 1</u></p>
<p>XXXXXXX,XXXXXXXX &lt;A&gt;</p>
<p>PID: 000-00-000 Ht(cm): _______ (______)</p>
<p>DOB: XXX 99,9999 (62) Wt(kg): 94.80 (06/28/2021)</p>
<p>SEX: MALE <u>eRx &amp; Non-VA Meds on File - Last Non-VA Entry on 08/18/23</u></p>
<p>CrCL: &lt;Not Found&gt; (CREAT: 1.06mg/dL 6/22/21) BSA (m2): _______</p>
<p>ISSUE LAST REF DAY</p>
<p># RX # DRUG QTY ST DATE FILL REM SUP</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>-------------------------------------ACTIVE-------------------------------------</p>
<p>1 3059519$ ACEBUTOLOL HCL 200MG CAP 30 A&gt; 01-22 01-22 11 30</p>
<p>-----------------------Non-VA MEDS (Not dispensed by VA)------------------------</p>
<p>LORATADINE TAB,ORAL ONCE DAILY AS NEEDED Date Doc: 08/18/21</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>PU Patient Record Update NO New Order</p>
<p>PI Patient Information SO Select Order</p>
<p>Select Action: Quit// ??</p>
<p>The following actions are also available:</p>
<p>RP Reprint (OP) DN Down a Line QU Quit</p>
<p>RN Renew (OP) RD Re Display Screen LS Last Screen</p>
<p>DC Discontinue (OP) PT Print List FS First Screen</p>
<p>RL Release (OP) PS Print Screen GO Go to Page</p>
<p>RF Refill (OP) &gt; Shift View to Right + Next Screen</p>
<p>PP Pull Rx (OP) &lt; Shift View to Left - Previous Screen</p>
<p>IP Inpat. Profile (OP) SL Search List ADPL Auto Display(On/Off)</p>
<p>RS Reprint Sig Log RDD Fill/Rel Date Disply CK Check Interactions</p>
<p>CM Manual Queue to CMOP DR Display Remote IN Intervention Menu</p>
<p>OTH PSO ERX JE Jump to eRx Patient UP Up a Line</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Medical Profile Prescription Processing Screen – Jump to eRx Patient (JE)

Once the user jumps to the eRx Patient side and wants to go back to the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option, upon selecting \<Enter\> at the “Select: Quit//” prompt, the user is navigated back to the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option screen from which \<JE\> was initiated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Jun 29, 2024@09:00:17 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXX,XXXX</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99</strong> <strong>(99)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong>^</strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 369258 IBUPROFEN 800MG TAB TEST,PROVIDER 06/18/24 I MV MV MV</p>
<p>2. 369261 ALBUTEROL INHALER TEST,PROVIDER 06/18/24 HAL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>DET Show/Hide Details IAS Include All Statuses LBD Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### REC – Resend Change Request

The new hidden action called Resend Change Request (REC) allows the user to send the previously sent eRx Change Request to the prescriber if the message type of the eRx is “CR”. Right after the user enters REC in the Select Action:Next Screen// prompt, the software will display the RX CHANGE REQUEST SUMMARY. This allows the user to review the previously sent eRx Change Request. The user can edit the existing eRx Change Request or just leave it as is, as shown below:

> **NOTE:** CR for RXCHANGEREQUEST

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@10:04:16 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>V45305034</strong></p>
<p>eRx Msg Type: <strong>RXCHANGEREQUEST</strong> Written: <strong>01/26/22</strong></p>
<p>eRx Status: <strong>CRN - RXCHANGE REQUEST - NEW</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Change Request Type: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Sub Type: <strong>Missing Information/Clarification</strong></p>
<p>Change Request Reason Text:</p>
<p><strong>The eRx is missing or unclear on RESENDING EXISTING ERX CHANGE REQUEST WITH A V record. Please edit and respond or cancel Rx and send a new prescription with the requested information.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MEDICATION PRESCRIBED</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Patient Primary Telephone: <strong>5871695248</strong></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXX</strong> DOB: <strong>99/99/99</strong></p>
<p>Vista Patient: <strong>NOT LINKED</strong> DOB: <strong>N/A</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Provider Primary Telephone: <strong>1234567890</strong></p>
<p>eRx Provider: <strong>YYYYY,YYYYY</strong> DEA#: NPI: <strong>1346563335</strong></p>
<p>Vista Provider: <strong>NOT LINKED</strong> DEA#: <strong>N/A</strong> NPI: <strong>N/A</strong></p>
<p>________________________________________________________________________________</p>
<p>eRx Drug: <strong>Spiriva with HandiHaler 18 mcg and inhalation capsules (tiotropium)</strong> <strong>. . .</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen SL Search List JO Jump to OP</p>
<p>- Previous Screen ADPL Auto Display(On/Off) UX Un Process eRx</p>
<p>UP Up a Line Q Quit PN Patient Progress Note</p>
<p>DN Down a Line AD Add Comment AU View Audit Log</p>
<p>FS First Screen ACK Acknowledge VO View Original eRx</p>
<p>LS Last Screen SH Status History VRQ View Request eRx</p>
<p>GO Go to Page HL View History Log VRE View Response eRx</p>
<p>RD Re Display Screen EC eRx Change Request REC Resend Change Request</p>
<p>PS Print Screen PA Patient Allergies</p>
<p>PL Print List UR Un Remove eRx</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// REC</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>RX CHANGE REQUEST SUMMARY</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Change Request Reason Code: <strong>D - DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Reason Sub-Code: <strong>MS - Missing Information/Clarification</strong></p>
<p>Note to Provider:</p>
<p><strong>The eRx is missing or unclear on RESENDING EXISTING ERX CHANGE REQUEST WITH A V record. Please edit and respond or cancel Rx and send a new prescription with the requested information.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)LISINOPRIL 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> This is the 1st EC action made for this medication.</p>
<p>2 (V)RIBOFLAVIN 100MG TAB 90 1 90 NO</p>
<p><u>Sig :</u> TAKE 1 TABLET ORALLY EACH DAY FOR 90 DAYS.</p>
<p><u>Note:</u> Added additional medication for this EC action aside from the existing</p>
<p>drug LISINOPRIL.</p>
<p>VA Progress Note Comment:</p>
<p><strong>TESTING VA PROGRESS NOTE COMMENT</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Would you like to edit this Rx Change Request before sending it? NO//</p>
<p>Would you like to send this Rx Change Request? YES//</p>
<p>Sending Request to Provider...Done.</p>
<p>Creating a new Progress Note...Done.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Resending eRx Change Request AS IS (no changes made)

Similar to an eRx Change Request (EC) action, every time an REC action is invoked, a new Rx Change Request is sent to the provider and CPRS Progress Notes (refer to the Patient Progress Note section).

Users are also allowed to edit the existing eRx Change Request before resending the eRx record again, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// REC</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>RX CHANGE REQUEST SUMMARY</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Change Request Reason Code: <strong>D - DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Reason Sub-Code: <strong>MS - Missing Information/Clarification</strong></p>
<p>Note to Provider:</p>
<p><strong>Please edit and respond or cancel Rx and send a new prescription with the requested information.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> TESTING</p>
<p>VA Progress Note Comment:</p>
<p><strong>TESTING VA PROGRESS NOTE COMMENT</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Would you like to edit this Rx Change Request before sending it? NO// YES</p>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: D// OS Out of Stock</p>
<p>NOTE TO PROVIDER:......</p>
<p>==[ WRAP ]==[INSERT ]===========&lt; NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]====</p>
<p>The medication prescribed is currently out of stock, if a substitutable product</p>
<p>exists and is presented as an option below, it may be approved. Otherwise, pt</p>
<p>may need to obtain locally or have replacement product prescribed.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> TESTING.</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH: NEW</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>ROSUVASTATIN CA 40MG TAB</strong></p>
<p>eRx SIG : <strong>TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</strong></p>
<p>eRx Notes: <strong>TESTING.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>20</strong> Days Supply: <strong>30</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<p>Select one of the following:</p>
<p>E USE ERX DRUG</p>
<p>V CHOOSE A VISTA DRUG</p>
<p>DRUG SELECTION: V CHOOSE A VISTA DRUG</p>
<p>Select DRUG GENERIC NAME: VITAMIN B COMPLEX CAP VT109 NATL FOR</p>
<p>M; Increments of 100</p>
<p>SUBSTITUTIONS? YES//</p>
<p>QUANTITY: 100</p>
<p>Select one of the following:</p>
<p>38 Original Quantity</p>
<p>40 Remaining Quantity</p>
<p>87 Quantity Received</p>
<p>QS Quantity sufficient as determined by the dispensing pharmacy</p>
<p>QT Quantity Transferred</p>
<p>CF Compound Final Quantity</p>
<p>UQ Central Fill Unit of Use Quantity</p>
<p>QTY QUALIFIER: 38// Original Quantity</p>
<p>QTY UNIT OF MEASURE: C64696 CAPLET DOSING UNIT</p>
<p>DAYS SUPPLY: (1-365): 100</p>
<p># OF REFILLS: (0-11): 0</p>
<p>SIG Text:</p>
<p>==[ WRAP ]==[INSERT ]===============&lt; SIG Text &gt;=====[Press &lt;PF1&gt;H for help]====</p>
<p>TAKE 1 CAPSULE DAILY.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p>
<p>ADDITIONAL NOTE TO PROVIDER: TESTING.</p>
<p>Updating...OK</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> TESTING.</p>
<p>2 (V)VITAMIN B COMPLEX CAP 100 0 100 YES</p>
<p><u>Sig :</u> TAKE 1 CAPSULE DAILY.</p>
<p><u>Note:</u> TESTING.</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH: FINISH</p>
<p>VA PROGRESS NOTE COMMENTS (Optional): TESTING ADDING A NEW DRUG.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>RX CHANGE REQUEST SUMMARY</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Change Request Reason Code: <strong>OS - Out of Stock</strong></p>
<p>Note to Provider:</p>
<p><strong>The medication prescribed is currently out of stock, if a substitutable product</strong></p>
<p><strong>exists and is presented as an option below, it may be approved. Otherwise, pt</strong></p>
<p><strong>may need to obtain locally or have replacement product prescribed.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> TESTING.</p>
<p>2 (V)VITAMIN B COMPLEX CAP 100 0 100 YES</p>
<p><u>Sig :</u> TAKE 1 CAPSULE DAILY.</p>
<p><u>Note:</u> TESTING.</p>
<p>VA Progress Note Comment:</p>
<p><strong>TESTING ADDING A NEW DRUG.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Would you like to edit this Rx Change Request before sending it? NO//</p>
<p>Would you like to send this Rx Change Request? YES//</p>
<p>Sending Request to Provider...Done.</p>
<p>Creating a new Progress Note...Done.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Resend Change Request – Added New Drug and Change the Change Request Code

After the user completed (entered FINISH in the “Select Drug Suggestion Option:” prompt) the addition of the new drug, the software displayed the RX Change Request Summary again. The display includes all the changes made to the existing eRx, as shown above.

> **NOTE:** Once the user answered “YES” to the prompt “Would you like to edit this Rx Change Request before sending it? NO//”, the user can edit/modify all the fields such as the patient’s current medication (e.g. dosage change) or change request code in the existing eRx record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@10:04:16 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>V45305034</strong></p>
<p>eRx Msg Type: <strong>RXCHANGEREQUEST</strong> Written: <strong>01/26/22</strong></p>
<p>eRx Status: <strong>CRN - RXCHANGE REQUEST - NEW</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Change Request Type: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Sub Type: <strong>Missing Information/Clarification</strong></p>
<p>Change Request Reason Text:</p>
<p><strong>Please edit and respond or cancel Rx and send a new prescription with the requested information.</strong></p>
<p><strong>. . .</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// REC</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY.</p>
<p><u>Note:</u> TESTING.</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH: EDIT</p>
<p>Select Entry # to Edit: (1-1):</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Resend Change Request – Edit the Existing eRx Drug

In the “Select Entry \# to Edit:” prompt, the user selects which drug to edit. In the example above, the existing record contains only one (1) eRx drug. In the event that there are more than 1, the prompt would be similar below.

Select Entry \# to Edit: (1-2):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 12, 2024@10:04:16 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXX,XXXXXXX</strong> eRx Reference #: <strong>V45305034</strong></p>
<p>eRx Msg Type: <strong>RXCHANGEREQUEST</strong> Written: <strong>01/26/22</strong></p>
<p>eRx Status: <strong>CRN - RXCHANGE REQUEST - NEW</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Change Request Type: <strong>DUE (Drug Use Evaluation)</strong></p>
<p>Change Request Sub Type: <strong>Missing Information/Clarification</strong></p>
<p>Change Request Reason Text:</p>
<p><strong>Please edit and respond or cancel Rx and send a new prescription with the requested information.</strong></p>
<p><strong>. . .</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// REC</p>
<p>. . .</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH.</p>
<p><u>Note:</u> TESTING.</p>
<p>2 (V)RIBOFLAVIN 25MG TAB 90 2 90 YES</p>
<p><u>Sig :</u> TESTING.</p>
<p><u>Note:</u> TESTING.</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH: DELETE</p>
<p>Select Entry # to Delete: (1-2): 2</p>
<p>Confirm? NO// YES</p>
<p>Deleting...Ok.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># DRUG QTY # REFS DAYS SUPPLY SUBS</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1 (E)ROSUVASTATIN CA 40MG TAB 20 3 30 YES</p>
<p><u>Sig :</u> TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p><u>Note:</u> TESTING.</p>
<p>Select Drug Suggestion Option: (N)EW (E)DIT (D)ELETE (F)INISH:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Resend Change Request – Deleted Existing eRx Drug

#### Patient-Level Record Lock

Note that when either the Summary/Details screen or any of the validate screens of an eR<sub>X</sub> are open, all the eR<sub>X</sub> for that same patient in the Holding Queue are locked and inaccessible for other users to access until the lock is released (the screens are closed). This is referred to as a patient-level record lock.

The following message displays if a user attempts to access an eR<sub>X</sub> for the same patient that another user has opened.

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/013.png)

Patient-Level Record Lock

#### Prohibit Renewals

The Prohibit Renewal Request flag is used to denote that a RxRenewal Request should not be sent to the sending prescriber for an original NewRx or a subsequent fillable RxChange Response when the flag is set on the original NewRx. This is usually used when the visit is for a one time prescription (i.e., Urgent Care Center or Emergency Department).

> **NOTE:** \(i\) The Prohibit Renewal Request information is not displayed for RxRenewal Request and Response records.

\(ii\) The Prohibit Renewal Request information is displayed both in VistA and on web GUI under Track/Audit details screen, whenever it is sent on the inbound NewRx record.

![](inbound-eprescribing-user-manual-unit-7-part-1-pso-7-746/014.png)

Prohibit Renewal Request

### From: Inbound ePrescribing User Manual (Unit 1) PSO*7*700

### Actionable and Non-Actionable eR<sub>X</sub> Records 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before learning how this option works it is important to understand that there are two types of Inbound eR<sub>X</sub> records: Actionable records and Non-Actionable records.

<u>Actionable records include:</u>

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

<u>Non-Actionable records</u>

Are all records acknowledged, removed, rejected, processed/completed, and auto-canceled are non-actionable. Non-Actionable records further include:

- RxRenewal Request
- RxRenewal Response – Approved
- RxRenewal Response – Approved with Changes (change to drug data only)
- RxChange Request
- CancelRx Response
- Inbound Errors related to CancelRx Responses

### Initial Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon entering the option, the user is prompted to choose which eRx record status they would like to view or work on. Once the prompts are answered, the user will enter the eRx Patient Centric View Queue, which is explained further down on this document.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will be prompted to select a Clinic. This helps MbM distribute the workload into multiple clinics so when the pharmacists are finishing the prescriptions they can work on the queue for a specific clinic.</p>
<p>eRx Clinic (Optional):</p>
<p>Although VAMC’s users are not presented this prompt, their eRx is still assigned a default clinic that is entered in the Site Parameter Enter/Edit [PSO SITE PARAMETERS] option under the field DEFAULT ERX CLINIC.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>A All</p>
<p>N New</p>
<p>I In Progress</p>
<p>W Wait</p>
<p>H Hold</p>
<p>C CCR</p>
<p>WP Workload Processing</p>
<p>Enter response: A// ?</p>
<p>All - View all patients with actionable prescriptions</p>
<p>New - View patients with prescriptions in the 'NEW' status</p>
<p>In Process - View patients with prescriptions in the 'IN PROCESS' status</p>
<p>Wait - View patients with prescriptions in the 'WAIT' status</p>
<p>Hold - View patients with prescriptions in the 'HOLD' status</p>
<p>CCR - View patients with prescriptions in the 'CCR' status</p>
<p>Workload Processing - Process New prescriptions for one patient at a</p>
<p>time using FIFO (First In First Out) method</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Status Selection

The screen above shows all the options users can chose for building the initial list upon entering the Patient Centric View. With the exception of the WP (Workload Processing), which will be explained further down on this document.

Users holding the PSO ERX WORKLOAD TECH security key will be limited to selecting the following options from the menu above to 3 options shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>H Hold</p>
<p>C CCR</p>
<p>WP Workload Processing</p>
<p>Enter response: WP//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

PSO ERX WORKLOAD TECH security key holders options

A – All

This choice will include all eRx that are actionable. Meaning that they still have some work to be done before they can be considered completed.

N – New

This choice will include only eRx with a NEW status. These are records for a new eRx that have not yet been changed by any other user.

I - In-Process

This choice will include only eRx with a IN PROCESS status. These are records that one or multiple users have already done some work on but, they are not yet completed.

W - Wait

This choice will include only eRx with a WAIT status. Similar to IN PROCESS these are records that one or multiple users have already done some work on, but they are not yet completed. They have usually been put on Hold and now have been removed from Hold.

H – Hold

This choice will include only eRx in a HOLD status. However, there are many different HOLD statuses and that’s why the next prompts shown below allows the user to further define this choice.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// Hold</p>
<p>Select one of the following:</p>
<p>S SINGLE CODE</p>
<p>A ALL HOLD CODES</p>
<p>Enter response: A// SINGLE CODE</p>
<p>Select eRx Status: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT - PATIENT NOT FOUND</p>
<p>119 HPD - PROVIDER NOT FOUND</p>
<p>120 HNF - NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO - INSUFFICIENT STOCK</p>
<p>122 HDI - DRUG-DRUG INTERACTION</p>
<p>123 HAD - ADVERSE DRUG INTERACTION</p>
<p>124 HBA - BAD ADDRESS</p>
<p>125 HPC - PROVIDER CONTACTED</p>
<p>126 HPA - PRIOR APPROVAL NEEDED</p>
<p>127 HOR - OTHER REASON</p>
<p>128 HPP - PATIENT CONTACTED</p>
<p>129 HPR - HOLD DUE TO PATIENT REQUEST</p>
<p>130 HQY - QUANTITY OR REFILL ISSUE</p>
<p>1442 HC - HOLD DUE TO CHANGE</p>
<p>1618 HCR - PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>1619 HWR - CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>1620 HIS - PROVIDER DEA# ISSUE</p>
<p>1621 HRX - HOLD FOR RX EDIT</p>
<p>1622 HDE - DRUG USE EVALUATION</p>
<p>1623 HTI - THERAPUTIC INTERCHANGE</p>
<p>1624 HSC - SCRIPT CLARIFICATION</p>
<p>1625 HGS - GENERIC SUBSTITUTION</p>
<p>1631 HAL - NO ALLERGY ASSESSMENT</p>
<p>1632 HEL - ELIGIBILITY ISSUE</p>
<p>1633 HUR - UN-REMOVED</p>
<p>Select eRx Status:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold Status Selection

In this case the user can select ALL HOLD CODES to include every eRx in a HOLD status or SINGLE CODE which allows the user to load eRx for one single HOLD code to be on the queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Note</u></strong></p>
<p>The code numbers shown on the left column above may not match the numbers on your VistA account.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

C – CCR

This choice will include only eRx in a CCR status. However, there are many different CCR statuses and that’s why the next prompts shown below allows the user to further define this choice. If they choose “A” (ALL CCR CODES) the list will include all eRx records with any of the eRx statuses shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// CCR</p>
<p>Select one of the following:</p>
<p>S SINGLE CODE</p>
<p>A ALL CCR CODES</p>
<p>Enter response: A// SINGLE CODE</p>
<p>Select eRx Status: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>246 RXR - RXRENEWAL RESPONSE REPLACE - NEW</p>
<p>247 RXE - RXRENEWAL RESPONSE - PROCESSING ERROR</p>
<p>248 RXN - RXRENEWAL RESPONSE - NEW</p>
<p>289 RXF - RXRENEWAL RESPONSE FAILED</p>
<p>606 CAO - CANCEL PROCESS COMPLETE</p>
<p>607 CAH - CANCEL COMPLETED IN HOLDING QUEUE</p>
<p>609 CAR - CANCEL REQUEST RECEIVED</p>
<p>612 CAF - CANCEL PROCESS FAILED</p>
<p>613 CAP - CANCEL PAPER RX OR FAXED RX</p>
<p>618 RXD - RXRENEWAL RESPONSE DENIED/DNTF</p>
<p>620 CAX - CANCEL RESPONSE FROM VISTA UNSUCCESSFUL</p>
<p>1412 CXN - RXCHANGE RESPONSE - NEW</p>
<p>1413 CXV - RXCHANGE RESPONSE - PRESCRIBER AUTH - NEW</p>
<p>1414 CXY - RXCHANGE RESPONSE - PRIOR AUTH - NEW</p>
<p>1418 CXD - RXCHANGE RESPONSE DENIED</p>
<p>1421 CXE - RXCHANGE RESPONSE - PROCESSING ERROR</p>
<p>Select eRx Status:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CCR Status Selection

In this case the user can select ALL CCR CODES to include every eRx in a CCR status or SINGLE CODE which allows the user to load eRx for one single CCR code to be on the queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Note</u></strong></p>
<p>The code numbers shown on the left column above may not match the numbers on your VistA account.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

WP – Workload Processing

This option will bypass the Patient Centric Queue and will load one patient at a time directly into the Single Patient Queue. Once inside the Single Patient queue the user can use the action NP (Next Patient) to load the next patient. The order in which the patients are presented are based on the eRx received date. Patient with the oldest records will be presented first. The date range for looking for these records are based on the ERX DEFAULT LOOKBACK DAYS parameter in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\].

Users holding the PSO ERX WORKLOAD TECH security key they cannot jump to the next patient (by selecting NP – Next Patient) until they have processed all the prescriptions for the current patient on their screen. Once a user with the PSO ERX WORKLOAD TECH key enters the first patient, that patient is assigned to that user for that day and no matter how many times the user gets out of the option and comes back in, such patient will be presented to them for processing. This feature was designed to prevent users from “cherry-picking” patients to work on while working in a Workload Processing mode.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter response: A// WP Workload Processing</p>
<p>Select one of the following:</p>
<p>1 PATIENT NOT MATCHED</p>
<p>2 PROVIDER NOT MATCHED</p>
<p>3 DRUG NOT MATCHED</p>
<p>4 PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>MATCH STATUS: 5//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Workload Processing option filters

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will see a slightly different labeling for the options above:</p>
<p>1 <mark>PATIENT FAIL -</mark> PATIENT NOT MATCHED</p>
<p>2 <mark>PROVIDER FAIL -</mark> PROVIDER NOT MATCHED</p>
<p>3 <mark>DRUG FAIL -</mark> DRUG NOT MATCHED</p>
<p>4 <mark>BASIC -</mark> PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>This is only a labeling difference and won’t affect the functionality of this filter, which works the same for VAMC and MbM sites.</p></td>
</tr>
</tbody>
</table>

1 – PATIENT NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Patient has not been matched to a VistA Patient.

2 – PROVIDER NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Provider has not been matched to a VistA Provider. Furthermore, the patient cannot quality for the PATIENT NOT MATCHED filter.

3 – DRUG NOT MATCHED

This option will only load and go through eRx Patients with at least one eRx record where the eRx Drug has not been matched to a VistA Drug. Furthermore, the patient cannot quality for the PATIENT NOT MATCHED and PROVIDER NOT MATCHED filters.

4 – PATIENT, PROVIDER AND DRUG MATCHED

This option will only load and go through eRx Patients with at least one eRx record where all three (PATIENT, PROVIDER and DRUG) are matched to a VistA corresponding record.

5 – ALL (NO FILTERS)

This option will not apply any filters regarding matching. It will start from the oldest records and move its way through the patients with the newest records.

### eRx Patient Centric Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the status selection is made, the user will enter the eRx Holding Queue in the Patient Centric view by default with the exception for the WP (Workload Processing) choice which will take the user directly to the Single Patient Queue View, explained further down in this document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Holding Queue – Patient Centric Queue

The figure above shows the eRx Holding Queue initial screen, in Patient Centric Queue view which contains a list of patients with Actionable (non-processed) eRx records. Below is an explanation of each segment of the screen.

#### Top Line

It contains the title of the list, in this case “eRx Patient Centric Queue”, then the current date/time to the right the page the user is on and how many pages there are total.

#### Header Area

In this non-scrollable area, there are 4 fields that control the list being displayed.

LOOK BACK DAYS

Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

CS/NON-CS

Indicates whether the list contains Controlled Substances (CS), Non-Controlled Substances (Non-CS) or Both. In case of CS being included it will also indicate the schedule of the CS drugs being displayed. It can also be changed by the user as described further down.

MAX. QUEUE SIZE

Indicates the maximum number of records that can be loaded in the list. It means that any selection that produces a number of records greater than this number will be cutoff at this number of records on the list. This limit can also be changed by the user as described further down.

ERX STATUS  
Indicates the status selection by the user before entering the list (Figure 6-2 above). With the exception of the WP selection, which bypass this list completely.

#### Column Header Line

\#

This column indicates the sequence number for the patient being displayed, which can be selected by the user to open the patient in a Single Patient Queue view screen.

PATIENT

Patient name column (maximum of 24 characters).

DOB

Date of birth column (MM/DD/YYY format).

SSN

Social Security column.

ED

Elapsed Days column. Indicates how many days ago the oldest actionable record for the patient was received.

NW

New eRx record status count. The number in this column indicates how many eRx are in a NEW status.

WT

Wait eRx record status count. The number in this column indicates how many eRx are in a WAIT status.

IP

In-Process eRx record status count. The number in this column indicates how many eRx are in a IN-PROCESS status.

HD

Hold eRx record status count. The number in this column indicates how many eRx are in a HOLD status.

CCR

CCR eRx record status count. The number in this column indicates how many eRx are in a CCR status: CancelRx Request, RxChange Response, and RxRenewal Response records in actionable statuses; including RXF, RXE and CXE records.

OTH

A count of all other status not captured by the columns to the left. It also includes Inbound Error related to RxRenewal/RxChange Request (Status – RRE/CRE).

TOT

A sum of all the numbers from the columns to the left.

<span class="mark">^</span> or <span class="mark">v</span>

One of these two symbols above can be spotted besides one of the following columns: PATIENT, DOB or ED. It indicates the column that the list is sorted by. <span class="mark">^</span> indicates an ascending order (smaller first A-\>Z or 0\>9) and <span class="mark">v</span> indicates a descending order (greater first Z-\>A or 9-\>0). Look further down to see how to sort by different columns and order (ascending or descending).

#### Listing Area

This area is where all the records are listed. They are always sequential number that goes from 1 to the last item on the list. This number can be selected by the user to view all the patient’s eRx records in a Single Patient Queue view.

\#. Vs. \#\] (Digitally Signed Vs. Not Digitally Signed)

Following each number there will be one of two characters “.” (dot) or “\]” (closing square bracket), as seen on lines 2. 10 and 14 on figure 6-7 above. The “.” indicates that the patient does not have any Digitally Signed eRx records, while the “\]” indicates that the patient has at least one eRx records that was Digitally Signed by the external provider. Digitally signed records is an indication by the external provider that the drug in the eRx records is a Controlled Substance drug. CS drugs are mandated by DEA (Drug Enforcement Agency) to always be transmitted to the pharmacy with a Digital Signature.

Bolded Lines

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A bolded line as seen on lines 4 and 14 above indicates another user has the patient or one of their eRx records open. When the user tries to select such numbers, a message will display on the message bar (below the list and above the Action Menu) indicating the user and date/time the records was locked, as shown below:

| \+ Patient Locked:XXXXXXXXX,XXXXXXXXX\|09/16/23@12:12:16 |
|----------------------------------------------------------|

Patient Centric Queue - Patient Locked

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SPAT – Sort By Patient

By default, the list is always sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Name by selecting the SPAT action. It will sort the list by Patient Name in ascending order when the user picks it once. If currently sorted by Patient Name and the users selects SPAT again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT<span class="mark">^</span> DOB SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient Name in Ascending Order

| \# PATIENT<span class="mark">v</span> DOB SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient Name in Descending Order

#### SQ – Search Queue

This action allows the user to place filters on the list by a few different selection criteria shown below. Multiple filters can be applied in one search criteria with the exception of ERX REFERENCE NUMBER and RX# which will result in the selection of one single record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// SQ Search Queue</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Queue options

1 - ERX PATIENT

Users can filter the list by single or multiple eRx patients by selecting them as seen below. The LAST REC. DATE column indicates the last eRx received for this patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 1 ERX PATIENT</p>
<p>ERX PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># ERX PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXXX 99/99/9999 PICKLETON-NY 09/10/23</p>
<p>2. XXXXXX,XXXXXXX 99/99/9999 BUTTERVILLE-NY 09/02/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX| XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

2 - ERX DATE OF BIRTH

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 2 ERX DATE OF BIRTH</p>
<p>Date of Birth (DOB): 99/99/999 (XXX 99, 9999)</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient Date of Birth

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>DOB(99/99/99)|PATIENT(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Results

In the case of the Search criteria not providing any matching entries, the screen below will display:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: DOB(99/99/99)|PATIENT(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No patients with actionable prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search Results

3 - ERX REFERENCE NUMBER

This search will take the user to the eRx Display screen and show the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 3 ERX REFERENCE NUMBER</p>
<p>ERX REFERENCE NUMBER: 9999999999</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Search by eRx REFERENCE NUMBER

4 – RX#

This search will first find the associated eRx with the VistA Rx \# selected and will take the user to the eRx Display screen then show the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 4 VISTA RX #</p>
<p>VISTA Rx #: 9999999999</p>
<p>This prescription is not an eRx prescription.</p>
<p>VISTA Rx #:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Search by VISTA Rx \#

5 – VISTA PATIENT

Users can filter the list by single or multiple VistA patients by selecting them as seen below. The REC. DATE column indicates the last eRx received for this patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 1 ERX PATIENT</p>
<p>VISTA PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXXX 99/99/9999 PLANO-TX 09/19/23</p>
<p>2. XXXXXX,XXXXXXX 99/99/9999 NEW YORK-NY 09/18/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue - Search By Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT <strong>(XXXXXX,XXXXXX| XXXXXX,XXXXXX)</strong></p>
<p>6 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

6 – MATCH STATUS

This search will qualify patients based on the matching status of the patient, provider, and drug to a corresponding VistA Record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 6 MATCH STATUS</p>
<p>Select one of the following:</p>
<p>1 PATIENT NOT MATCHED</p>
<p>2 PROVIDER NOT MATCHED</p>
<p>3 DRUG NOT MATCHED</p>
<p>4 PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>MATCH STATUS: 4</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – eRx Patients Selected

6.1 – MATCH STATUS: PATIENT NOT MATCHED

If the patient has at least one actionable record which the eRx patient has not yet been matched to, a corresponding VistA patient will be included in the list.

6.2 – MATCH STATUS: PROVIDER NOT MATCHED

If the patient has at least one actionable record which the eRx provider has not yet been matched to, a corresponding VistA provider AND the patient does not qualify for PATIENT NOT MATCHED filter above, it will be included in the list.

6.3 – MATCH STATUS: DRUG NOT MATCHED

If the patient has at least one actionable record which the eRx Drug has not yet been matched to, a corresponding VistA drug AND the patient does not qualify for PATIENT NOT MATCHED filter above AND the patient does not qualify for the PROVIDER NOT MATCHED filter above, it will be included in the list.

6.4 – MATCH STATUS: PATIENT, PROVIDER AND DRUG MATCHED

If the patient has at least one actionable record which the eRx patient has been matched to the VistA patient, the eRx Provider has been matched to the VistA provider and the Drug has been matched to a VistA drug AND the patient does not quality to either of the 3 filters described above, it will be included in the list.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will see a slightly different labeling for the options above:</p>
<p>1 <mark>PATIENT FAIL -</mark> PATIENT NOT MATCHED</p>
<p>2 <mark>PROVIDER FAIL -</mark> PROVIDER NOT MATCHED</p>
<p>3 <mark>DRUG FAIL -</mark> DRUG NOT MATCHED</p>
<p>4 <mark>BASIC -</mark> PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>5 ALL (NO FILTERS)</p>
<p>This is only a labeling difference and won’t affect the functionality of this filter, which works the same for VAMC and MbM sites.</p></td>
</tr>
</tbody>
</table>

Removing Individual Filters

Individual filters can be removed by using the “^” (up-caret) along with the Number of the filter applied, as show below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p>
<p>SEARCH BY: <strong>^2</strong></p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXXX,XXXXXX|XXXXXX,XXXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 ERX REFERENCE NUMBER</p>
<p>4 VISTA RX #</p>
<p>5 VISTA PATIENT</p>
<p>6 MATCH STATUS <strong>(ALL MATCHED)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Individual Filter Removal

#### LBD – Change Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s date. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Quit// LBD Change Look Back Days</p>
<p>LOOK BACK DAYS: 45// ??</p>
<p>This field holds the number of days to look back in order to include records</p>
<p>in the Patient Centric Queue.</p>
<p>LOOK BACK DAYS: 45// 365 Please Wait...</p>
<p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@12:12:23 Page: 1 of 5</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Changing Look Back Days

#### RX – Rx List View

This action takes the user to Rx Medication Queue list which will be described further down in this document.

#### RAF – Remove All Filters

This action allows the user to remove all filters currently applied to the list. This list is then refreshed to without any filters.

#### REF – Refresh List

This action allows the user to refresh the list. This is used to make sure you are looking at the latest version of the list because other users might have already worked through some of the records currently on the list which may have altered it, which will not show until it is refreshed.

#### Hidden Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following actions are also available:</p>
<p>CS Group By CS - Previous Screen PS Print Screen</p>
<p>SDOB Sort By DOB UP Up a Line PT Print List</p>
<p>SED Sort By Elapsed Days DN Down a Line SL Search List</p>
<p>NP Next Patient FS First Screen QU Quit</p>
<p>CV Change View LS Last Screen</p>
<p>+ Next Screen GO Go to Page</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### CS – Group by CS (hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. The action can be used to turn ON and OFF this hidden action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p> <u><strong><mark>CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>1] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p>4] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</p>
<p>5] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p> <u><strong><mark>NON-CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 41 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 40 0 0 1 0 0 0 1</p>
<p>10 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 38 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 35 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 33 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>14 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Grouped by CS and Non-CS

#### SDOB – Sort By Date of Birth (hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Date of Birth (DOB) by selecting the SDOB hidden action. It will sort the list by Patient DOB in ascending order when the user picks it once. If currently sorted by Patient DOB and the users selects SDOB again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB<span class="mark">^</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient DOB in Ascending Order

| \# PATIENT DOB<span class="mark">v</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Patient DOB in Descending Order

#### SED – Sort By Elapsed Days (hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first). The user can sort the list by the Elapsed Days by selecting the SED hidden action. It will sort the list by Elapsed Days in ascending order when the user picks it once. If currently sorted by Elapsed Days and the users selects SED again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB SSN ED<span class="mark">^</span> NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Elapsed Days in Ascending Order

| \# PATIENT DOB SSN ED<span class="mark">v</span> NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Patient Centric Queue – Sorted By Elapsed Days in Descending Order

#### NP – Next Patient (hidden)

This hidden action allows the user to open the patient with the oldest eRx record in an actionable status. It will take the user to the eRx Single Patient Queue. Once in the eRx Single Patient Queue the user can type NP again to jump to the next patient with the oldest order after the previous patient.

#### CV – Change View (hidden)

This hidden action allows the user to change the following parameters that affect the content and appearance of the eRx Patient Centric Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days) . Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>LOOK BACK DAYS: 45// 45 DAYS</p>
<p>SORT BY: ED// ED ELAPSED DAYS</p>
<p>SORT ORDER: D// DESCENDING</p>
<p>INCLUDE CS/NON-CS: B// BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE: SCHEDULES II - V// SCHEDULES II - V</p>
<p>GROUP BY CS: NO// NO NO</p>
<p>MAXIMUM QUEUE SIZE: 999//</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action (No Default View Saved)

Once the user chooses all the parameters above the option will prompt them if they want to save the current parameters as their default view. Whether they chose YES or NO the option will refresh the list according to the parameters selected. If they select YES to save the view the next time they select CV they will be given a chance to delete their saved default view, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>Your saved default view:</p>
<p>-----------------------</p>
<p>LOOK BACK DAYS : 45 DAYS</p>
<p>SORT BY : ELAPSED DAYS</p>
<p>SORT ORDER : DESCENDING</p>
<p>INCLUDE CS/NON-CS : BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE : SCHEDULES II - V</p>
<p>GROUP BY CS/NON-CS : NO</p>
<p>MAXIMUM QUEUE SIZE : 999</p>
<p>Delete this saved default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action (With Default View Saved)

The parameters LOOK BACK DAYS, SORT BY, SORT ORDER and GROUP BY CS/NON-CS have been explained above on how they impact the queue. The other parameters are explained below:

INCLUDE CS/NON-CS

This parameter allows the user to select which type of eRx records should be displayed on the list: Controlled Substances only (CS), Non-Controlled Substances only (Non-CS) or Both (B). The default value is B. This parameter is displayed on the header of the Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INCLUDE CS/NON-CS: B// ?</p>
<p>Indicate whether CS and/or Non-CS records should be included in the</p>
<p>Patient Centric Queue.</p>
<p>Choose from:</p>
<p>CS CS ERXS ONLY</p>
<p>Non-CS NON-CS ERXS ONLY</p>
<p>B BOTH (CS AND NON-CS)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action – INCLUDE CS/NON-CS Field

CS SCHEDULE

This parameter is only prompted in the case the user selects either CS or B above. The default value is 3 (SCHEDULES II – V). This parameter is displayed on the header of the Queue. It allows the user to further filter the CS eRx records based on the drug schedule, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CS SCHEDULE: SCHEDULES II - V// ?</p>
<p>Indicate which CS Schedules should be included in the Patient Centric</p>
<p>Queue.</p>
<p>Choose from:</p>
<p>1 SCHEDULE II ONLY</p>
<p>2 SCHEDULES III - V</p>
<p>3 SCHEDULES II - V</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Centric Queue – Change View hidden action – CS SCHEDULE Field

MAXIMUM QUEUE SIZE

This parameter determines the maximum number of records to be loaded for the queue. Once the process that builds the list reaches this limit it stops. The default is 999 and the maximum is 4,999. This parameter is displayed on the header of the Queue.

#### 48-Lines Terminal Emulator Display Feature

There is a Class 3 software (KIDS Build) that allows sites, including Meds-By-Mail (MbM), to expand their ListMan Listing Area to more than double of the displayed lines for one page when using the regular 24-Lines on the Terminal Emulator. It is important to emphasize that simply setting the Terminal Emulator to 48-Lines won’t work, the VistA account where the user is connecting must have this Class 3 software installed for it to work.

Once the KIDS Build is installed and the Terminal Emulator is set to display 48-Line, the eRx Patient Centric Queue will look like the following:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 2</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p><strong>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</strong></p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>17. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 0 0 1 0 0 1 2</p>
<p>18. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>19. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 3 0 0 1 0 0 4</p>
<p>20 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 1 0 1 0 0 0 2</p>
<p>21. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 31 0 0 1 0 0 1 2</p>
<p>22. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 1 0 0 0 1 0 2</p>
<p>23. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 2 1 0 0 3</p>
<p>23. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 1 0 0 0 1</p>
<p>25. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 27 0 0 1 0 0 0 1</p>
<p>26] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 24 0 0 1 0 0 0 1</p>
<p>27. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 24 1 0 0 0 1 0 2</p>
<p>28. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 23 1 0 0 0 0 0 1</p>
<p>29. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 22 2 0 1 0 0 0 3</p>
<p>30] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 21 1 0 0 0 0 0 1</p>
<p>31. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 21 1 0 0 0 0 0 1</p>
<p>32. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 20 1 0 0 0 0 0 1</p>
<p>33. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 19 0 0 1 0 0 1 2</p>
<p>34. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 9 2 0 1 0 0 0 3</p>
<p>35. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 7 3 0 0 1 0 0 4</p>
<p>36. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 1 1 0 1 0 0 0 2</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### eRx Single Patient Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user selects a patient in the eRx Patient Centric Queue above, they will be taken to the eRx Single Patient Queue. This list will by default display all the eRx Patient’s Actionable records and they will be sorted by the REC.DATE column in a descending order (oldest records first).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A AV A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Single Patient Queue

#### Top Line

It contains the title of the list, in this case “eRx Single Patient Queue”, then the current date/time to the right the page the user is on and how many pages there are total.

#### Header Area

In this non-scrollable area, there are 6 fields that control the list being displayed.

eRx PATIENT

This is the eRx Patient name as received by the outside prescriber.

SEX

eRx Patient gender.

DOB

eRx Patient date of birth followed by their age between parentheses.

LOOK BACK DAYS

Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

STATUS

By default, only ‘Actionable’ eRx records are included on the eRx Single Patient Queue, however the user can easily change this parameter as described further down on this document.

SSN

This is the eRx Patient Social Security Number (SSN) exactly as it was received from the outside prescriber.

#### Column Header Line

\#

This column indicates the sequence number for the eRx record being displayed, which can be selected by the user to open the eRx Individual record and view the details.

ERX ID

This is the eRx number or ID, which is the same as the eRx Hub.

DRUG NAME

This is the eRx Drug Name exactly as received from the prescriber software. It is truncated at 22 characters.

PROVIDER NAME

This is the eRx Prescriber Name exactly as received from the prescriber software

REC.DATE

This is the date when the eRx was received.

STA

This is eRx Status column. It shows the current eRx record status. It’s truncated at 3 characters.

MATCHING PT

This column indicates the current matching status for the eRx Patient. The following variations are possible for this column:

“” (blank) – eRx Patient has not been matched to a VistA Patient

“A” – eRx Patient has been auto-matched to a VistA Patient

“M” – eRx Patient has been manually matched to a VistA Patient by the user

“M” (bold) – eRx Patient was initially auto-matched and then manually matched to a different VistA Patient by the user

“AV” – eRx Patient has been auto-matched to a VistA Patient and manually validated

“MV” – eRx Patient has been manually matched to a VistA Patient and manually validated

“MV” (bold M) – eRx Patient was initially auto-matched and then manually matched to a different VistA Patient and subsequently manually validated by the user

MATCHING PR

This column indicates the current matching status for the eRx Provider. The following variations are possible for this column:

“” (blank) – eRx Provider has not been matched to a VistA Provider

“A” – eRx Provider has been auto-matched to a VistA Provider

“M” – eRx Provider has been manually matched to a VistA Provider by the user

“M” (bold) – eRx Provider was initially auto-matched and then manually matched to a different VistA Provider by the user

“AV” – eRx Provider has been auto-matched to a VistA Provider and manually validated

“AV” (bold V)– eRx Provider has been auto-matched to a VistA Provider and auto-validated (MbM Only – see below)

“MV” – eRx Provider has been manually matched to a VistA Provider and validated

“MV” (bold M) – eRx Provider was initially auto-matched and then manually matched to a different VistA Provider and subsequently manually validated by the user

MATCHING DR

This column indicates the current matching status for the eRx Drug. The following variations are possible for this column:

“” (blank) – eRx Drug has not been matched to a VistA Drug

“A” – eRx Drug has been auto-matched to a VistA Drug

“M” – eRx Drug has been manually matched to a VistA Drug by the user

“M” (bold) – eRx Drug was initially auto-matched and then manually matched to a different VistA Drug by the user

“AV” – eRx Drug has been auto-matched to a VistA Drug and manually validated

“MV” – eRx Drug has been manually matched to a VistA Drug and manually validated

“MV” (bold M) – eRx Drug was initially auto-matched and then manually matched to a different VistA Drug and subsequently manually validated by the user

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong><u>Provider Auto-Validation</u></strong></p>
<p>An eRx provider will be automatically validated if the following conditions are met when the eRx arrives:</p>
<ul>
<li><p>eRx is not digitally signed (indicating a prescription for a controlled substance)</p></li>
<li><p>eRx Provider was auto-matched</p></li>
<li><p>eRx Provider last name and VistA Provider last names match exactly</p></li>
<li><p>eRx Provider first letter of first name matches the VistA Provider first letter of first name</p></li>
<li><p>First 5 digits of eRx Provider zip code matches exactly with the VistA Provider zip code first 5 digits</p></li>
</ul>
<p>The user recorded as responsible for the validation will be PSOAPPLICATIONPROXY,PSO</p></td>
</tr>
</tbody>
</table>

In the displayed lists, the user can select or enter the line number of the eRx number to view and examine the details of the eRx or select the actions displayed right below the listing area.

Validation actions for a single patient may be complete from there. For more details, refer to the sections identified in this guide.

> **NOTE:** From the Summary/Details screen, users <u>cannot</u> edit any of the VistA information. The validate screens contain the option for editing the VistA information. For further information on editing and validating VistA information for an eR<sub>X</sub>, refer to section 6.2.

#### Listing Area

This area is where all the records are listed. They are always sequential number that goes from 1 to the last item on the list. This number can be selected by the user to view the patient’s corresponding eRx record in the Summary eRx View Display.

\#. Vs. \#\] (Digitally Signed Vs. Not Digitally Signed)

Following each number there will be one of two characters “.” (dot) or “\]” (closing square bracket), as seen on lines 2. 10 and 14 on figure 6-7 above. The “.” indicates that the patient does not have any Digitally Signed eRx records, while the “\]” indicates that the patient has at least one eRx records that was Digitally Signed by the external provider. Digitally signed records is an indication by the external provider that the drug in the eRx records is a Controlled Substance drug. CS drugs are mandated by DEA (Drug Enforcement Agency) to always be transmitted to the pharmacy with a Digital Signature.

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

DET – Show/Hide Details

This action shows or hides the eRx prescription details.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// DET Show/Hide Details Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>eRx Qty: 60 eRx # of Refills: 5 eRx Days Supply: 30</p>
<p>SIG: TAKE ONE CAPSULE BY BY MOUTH EVERY 12 HOURS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DET - Show/Hide Details – Shown

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// DET Show/Hide Details Please wait...Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

DET - Show/Hide Details - Hidden

IAS – Include All Statuses

This action displays all Actionable and Non-Actionable eRx status codes for a patient. Once the \<IAS\> action is selected, the list is refreshed to display all eRx statuses for the patient. The new status will be displayed in the header section.

For additional information on Actionable and Non-Actionable eRX Status Codes, refer to Appendix B: Holding Queue Status Codes & Descriptions in User Manual Unit 6 available on the Veteran's Documentation Library (VDL) for additional information on the various statuses in the list.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// IAS Include All Statuses Please wait...Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ALL</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y 09/25/23 PR MV MV AV</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S 09/25/23 R01 MV A</p>
<p>3. 99999994 NAPROXEN 250MG TABLET YYYYYY,YYYYY Y 09/25/23 R92 MV MV A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A AV A</p>
<p>6. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>7] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>8. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A AV A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

IAS - Include All Statuses – eRx Details are Hidden

> **NOTE:** Selecting/entering the \<DET\> action again while displaying all actionable and non-actionable eRx statuses will display the details of each eRx.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong><u>REMOVED Status</u></strong></p>
<p>For MbM sites the status column won’t show “RM” like it does for a VA Medical Center site. Instead, it will show an abbreviation of the Removal Reason which is composed by “R” concatenated with the last 2 numbers of the Removal Reason. Like show above for entries #2 and #3 under the STA (Status) column.</p>
<p>REM01 Drug out of stock or on backorder and unavailable for processing</p>
<p>REM02 Patient was not able to pick up</p>
<p>REM03 Prescription canceled by Provider</p>
<p>REM04 Prescription processed manually</p>
<p>REM05 Provider will cancel this eRx and submit another</p>
<p>REM06 Unable to mail prescription and patient unable to pick up</p>
<p>REM07 Unable to contact patient</p>
<p>REM08 Unable to contact provider</p>
<p>REM09 ERX Issue not resolved-Provider contacted</p>
<p>REM91 Undefined system error</p>
<p>REM92 Other</p></td>
</tr>
</tbody>
</table>

LBD – Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// LBD Change Look Back Days</p>
<p>LOOK BACK DAYS: 45// ?</p>
<p>Type a number between 0 and 1000, 0 decimal digits.</p>
<p>LOOK BACK DAYS: 45// ??</p>
<p>This field holds the number of days to look back in order to include records in</p>
<p>the Single Patient Queue.</p>
<p>LOOK BACK DAYS: 45// 365 Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU – Sort By Drug (hidden)

This action sorts the display list by eRx Drug Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SDRU\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>^</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU - Sort By Drug in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>v</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRU - Sort By Drug in Descending Order

SPRO – Sort by Provider (hidden)

This action sorts the display list by eRx Provider Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SPRO\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>^</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRO - Sort By Provider in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>v</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRO - Sort By Provider in Descending Order

SREC – Sort by Rec. Date (hidden)

This action sorts the display list by eRx Received Date. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SREC\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SREC - Sort By Received Date in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>v</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SREC - Sort By Received Date in Descending Order

SSTA – Sort by Status (hidden)

This action sorts the display list by eRx Status. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SSTA\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>^</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SSTA - Sort By Status in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>v</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SSTA - Sort By Status in Descending Order

SPTM – Sort by Pat. Match (hidden)

This action sorts the current matching status for the eRx Patient. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the patient matched first, records with patient matched but not validated next and finally the entries with the patient matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SPTM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPTM SPTM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>^</mark></strong> PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPTM - Sort By Patient Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPTM SPTM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>v</mark></strong> PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPTM - Sort By Patient Match in Descending Order

SPRM – Sort by Prov. Match (hidden)

This action sorts the current matching status for the eRx Provider. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the provider matched first, records with provider matched but not validated next and finally the entries with the provider matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SPRM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRM SPRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR<strong><mark>^</mark></strong> DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRM - Sort By Provider Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRM SPRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR<strong><mark>v</mark></strong> DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPRM - Sort By Provider Match in Descending Order

SDRM – Sort by Drug Match (hidden)

This action sorts the current matching status for the eRx Drug. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the drug matched first, records with drug matched but not validated next and finally the entries with the drug matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SDRM\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRM SDRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRM - Sort By Drug Match in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRM SDRM Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR<strong><mark>v</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SDRM - Sort By Drug Match in Descending Order

SALL – Sort by All Matches (hidden)

This action sorts the current matching status for the eRx Patient, Provider and Drug. The entries are sorted in ascending \[^\] or descending \[v\]. In the case of this column, ascending order will list the entries without the patient, provider and drug matched first, records with patient, provider and drug matched but not validated next and finally the entries with the patient, provider and drug matched and validated. To change the sorting order from ascending to descending and vice-versa, enter the \<SALL\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SALL SALL Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>^</mark></strong> PR<strong><mark>^</mark></strong> DR<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SALL - Sort By All Matches in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SALL SALL Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA PT<strong><mark>v</mark></strong> PR<strong><mark>v</mark></strong> DR<strong><mark>v</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SALL - Sort By All Matches in Descending Order

SERX – Sort By eRx ID (hidden)

This action sorts the entries by eRx ID for the patient. The entries are sorted in ascending \[^\] or descending \[v\]. To change the sorting order from ascending to descending and vice-versa, enter the \<SERX\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SERX SERX Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID<strong><mark>^</mark></strong> DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SERX - Sort By eRx ID in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SERX SERX Please wait...</p>
<p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID<strong><mark>v</mark></strong> DRUG NAME PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SERX - Sort By eRx ID in Descending Order

BU – Batch Un-Hold (hidden)

This action allows the user to batch un-hold eRx entries for a patient. To perform batch un-hold, the eRx record status should have a HOLD status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BU BU</p>
<p>Select Range: ?</p>
<p>Select the range of eRx entries from the list above. Ex: '1-5'; '1,3,5';</p>
<p>'1-4,6-8'.</p>
<p>Select Range: 2</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X HOR</p>
<p>Additional Comments (Optional): TESTING BU UN-HOLD ACTION FROM eRx Single Patient Queue functionality.</p>
<p>Confirm Batch Un-Hold? N// YES</p>
<p>Updating...done Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Un-Hold

In the example above, after the user successfully performs the batch un-hold action, the status of eRx AMANTADINE 100MG CAP is updated from HOR to I.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Un-Hold Result

If user enters invalid range, the verbiage below will be displayed

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BU BU</p>
<p>Select Range: 100ABC</p>
<p>Invalid Range. Please select a range of entries between 1 and 5.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If user select an eRx entry range whose status is not on hold, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BU BU</p>
<p>Select Range: 3</p>
<p>UNABLE TO BATCH UN-HOLD: At least one eRx entry cannot be removed from HOLD.</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITAMIN C CA XXXXXX,XXXXX X N</p>
<p>REASON: eRx is not on Hold</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BH – Batch Hold (hidden)

This action allows the user to batch hold eRx entries for a patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BH BH</p>
<p>Select Range: ?</p>
<p>Select the range of eRx entries from the list above. Ex: '1-5'; '1,3,5';</p>
<p>'1-4,6-8'.</p>
<p>Select Range: 1-5</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 32MG TAB YYYYYY,YYYYY Y W</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X I</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITAMIN C CA XXXXXX,XXXXX X N</p>
<p>4. 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X N</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X I</p>
<p>Select HOLD reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG INTERACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>598 HCR PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>599 HWR CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>600 HIS PROVIDER DEA# ISSUE</p>
<p>601 HRX HOLD FOR RX EDIT</p>
<p>602 HDE DRUG USE EVALUATION</p>
<p>603 HTI THERAPUTIC INTERCHANGE</p>
<p>604 HSC SCRIPT CLARIFICATION</p>
<p>605 HGS GENERIC SUBSTITUTION</p>
<p>1561 HAL NO ALLERGY ASSESSMENT</p>
<p>1562 HEL ELIGIBILITY ISSUE</p>
<p>1563 HUR HOLD - UN-REMOVE</p>
<p>Select HOLD reason code: 127 HOR OTHER REASON</p>
<p>Additional Comments (Optional): TESTING BATCH HOLD FROM ERX SINGLE PATIENT QUEUE FUNCTIONALITY.</p>
<p>Confirm Batch Hold? N// YES</p>
<p>Updating...done Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold

In the example above, the user performs the batch hold action on all ACTIONABLE eRx status for a patient. The user then selected 'HOR OTHER REASON' as the reason for holding the eRx. Once the update is done, you can see that the list has been refreshed to reflect the new status, 'HOR'. See the refreshed display list below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold Result

If the user enters an invalid range, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 100ABC</p>
<p>Invalid Range. Please select a range of entries between 1 and 5.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user does not enter a hold reason code, the verbiage below will be displayed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 3</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X N</p>
<p>Select HOLD reason code: ^Hold Reason required. eRx not placed in a 'Hold' status.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the event the eRx status in the header section is set to ALL (actionable and non-actionable), then the user either selects:

1\. An eRx with non-actionable status

2\. All eRx displayed lists, which both contain actionable and non-actionable status.

The following verbiage will be displayed below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ALL</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y 09/25/23 PR MV MV AV</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S 09/25/23 R01 MV A</p>
<p>3. 99999994 NAPROXEN 250MG TABLET YYYYYY,YYYYY Y 09/25/23 R92 MV MV A</p>
<p>4. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A AV A</p>
<p>6. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A AV A</p>
<p>7] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>8. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 I A AV A</p>
<p>9. 876543 N/A ZZZZZZZ,ZZZZZZ 09/29/23 CAN</p>
<p>10. 41852 N/A ZZZZZZZ,ZZZZZZ 09/29/23 CAH</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// BH BH</p>
<p>Select Range: 9-10</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

BU – Batch Hold

In the example below, the user selects eRx’s (#9 and \#10) with a non-actionable status. See the displayed list above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>9. 876543 N/A ZZZZZZZ,ZZZZZZ CAN</p>
<p>10. 741852 N/A ZZZZZZZ,ZZZZZZ CAH</p>
<p>UNABLE TO BATCH HOLD: Either you do not have the appropriate security keys</p>
<p>or one or more records cannot be put on HOLD</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the example below, the user selects All eRx displayed lists, which both contain actionable and non-actionable status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// BH BH</p>
<p>Select Range: 1-10</p>
<p>UNABLE TO BATCH HOLD: At least one eRx entry cannot be put on HOLD.</p>
<p># ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------------</p>
<p>1. 12314 LOXAPINE 50MG CAP YYYYYY,YYYYY Y PR</p>
<p>REASON: eRx with a status of 'Rejected', 'Removed' or 'Processed'.</p>
<p>2. 12345671 BENADRYL DIPHENHYDRAM SSSSSS,SSSSS S REM01</p>
<p>REASON: eRx with a status of 'Removed'.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient (hidden)

Once in the eRx Single Patient Queue, this action allows the user to automatically open to the next patient with the oldest order after the current patient in an actionable status. The user can type \<NP\> again to jump to the next patient.

For example:

In the eRx Patient Centric Queue, the user selects \#3 from the lists displayed, see below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 27, 2023@11:06:43 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. AAAAA,AAAAAAAAAA 99/99/9990 999-99-9990 44 0 0 1 0 0 1 2</p>
<p>2] BBBBB,BBBBBBBBBB 99/99/9991 999-99-9991 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9994 999-99-9994 37 0 0 1 0 0 1 2</p>
<p>4. CCCCC,CCCCCCCCCC 99/99/9992 999-99-9992 37 3 0 0 1 0 0 4</p>
<p>5. ZZZZZ,ZZZZZZZZZZ 99/99/9993 999-99-9993 37 1 0 1 0 0 0 2</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// <strong>3</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Inside eRx Single Patient Queue, the use enter \<NP\> action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:52 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>2. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>3. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit// NP NP Loading Next Patient...Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient

In the display below, the patient listed in \#4 above in the eRx Single Patient Queue is displayed after entering the \<NP\> action since that is the next patient after XXXXX,XXXXXXXXXX.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:55 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>CCCCCCCCC,CCCCCCCCCCC C</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

NP – Next Patient

CS – Group by CS/Non CS (hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. To turn ON or OFF the action, enter \<CS\> action the second time, and vice versa.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Sep 27, 2023@14:38:52 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>XXXXXXXXX,XXXXXXXXXXX X</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99(99)</strong></p>
<p>LOOK BACK DAYS: <strong>45</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><u><strong><mark>CONTROLLED SUBSTANCE Rx's</mark> _ a</strong></u></p>
<p>1] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 HOR A</p>
<p><u><strong><mark>NON-CONTROLLED SUBSTANCE Rx's</mark> a</strong></u></p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 HOR MV MV AV</p>
<p>3. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<p>5. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 HOR A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong>DET</strong> Show/Hide Details <strong>IAS</strong> Include All Statuses <strong>LBD</strong> Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CS – Group by CS/Non-CS

CV – Change View (hidden)

This action allows the user to change the following parameters that affect the content and appearance of the eRx Single Patient Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days). Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// CV CV</p>
<p>LOOK BACK DAYS: 365// ?</p>
<p>Type a number between 0 and 1000, 0 decimal digits.</p>
<p>LOOK BACK DAYS: 365// ??</p>
<p>This field holds the number of days to look back in order to include records in</p>
<p>the Single Patient Queue.</p>
<p>LOOK BACK DAYS: 365// 45 DAYS</p>
<p>SORT BY: RE// ?</p>
<p>Indicate the order (Ascending or Descending) to sort the Single Patient</p>
<p>Queue.</p>
<p>Choose from:</p>
<p>ID ERX ID</p>
<p>DR DRUG NAME</p>
<p>PR PROVIDER NAME</p>
<p>RE RECEIVED DATE</p>
<p>STA ERX STATUS</p>
<p>PAM PATIENT MATCH</p>
<p>PRM PROVIDER MATCH</p>
<p>DRM DRUG MATCH</p>
<p>ALL ALL MATCHES</p>
<p>SORT BY: RE// RECEIVED DATE</p>
<p>SORT ORDER: A// ?</p>
<p>Choose from:</p>
<p>A ASCENDING</p>
<p>D DESCENDING</p>
<p>SORT ORDER: A// ASCENDING</p>
<p>DISPLAY DETAILS: NO// ?</p>
<p>Indicate whether the Details (Medication Instructions, Quantity, # of</p>
<p>Refills and Days Supply) should be displayed on the Single Patient Queue</p>
<p>or not.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>DISPLAY DETAILS: NO// ??</p>
<p>This field indicates whether the user wants to display the Details (Medication Instructions, Quantity, # of Refills and Days Supply) for each record on the Single Patient Queue.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>DISPLAY DETAILS: NO// NO NO</p>
<p>GROUP BY CS: NO// ??</p>
<p>This field indicates whether the user wants the entries in the Single Patient Queue grouped by CS and Non-CS (ON) or all together (OFF).</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>GROUP BY CS: NO// Y YES</p>
<p>INCLUDE ALL STATUSES: NO// ??</p>
<p>This field indicates whether the user wants all statuses to be included on the Single Patient Queue or only actionable statuses.</p>
<p>Choose from:</p>
<p>1 YES</p>
<p>0 NO</p>
<p>INCLUDE ALL STATUSES: NO// NO NO</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CV – Change View

If the user already has personal Change View default view saved, this option will display the saved preferences and will give the user the option to delete them.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// cv CV</p>
<p>Your saved default view:</p>
<p>-----------------------</p>
<p>LOOK BACK DAYS : 45 DAYS</p>
<p>SORT BY : ERX ID</p>
<p>SORT ORDER : ASCENDING</p>
<p>DISPLAY DETAILS : YES</p>
<p>GROUP BY CS/NON-CS : NO</p>
<p>INCLUDE ALL STATUSES: NO</p>
<p>Delete this saved default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CV – Change View (User has saved default view)

### eRx Medication Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rx Action on the Patient Centric Queue takes the user to the Rx Medication Queue. Within the Rx Medication Screen (or Rx List View Screen), the user will have the ability to easily filter the list by Message Type by selecting one of the following hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen//</p>
<p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Medication Queue

#### Top Line

| <u>Rx Medication Queue Sep 16, 2023@11:06:54 Page: 1 of 1</u> |
|-------------------------------------------------------------------|

Action Menu the user selected from the eRx Patient Centric Queue. Title of menu “Rx Medication Queue”, followed by the current date/time, and ending with view of current page the user is on and how many pages there are total.

#### Header Area

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In this non-scrollable area, there are 4 fields that the list being displayed.

LOOK BACK DAYS - Indicates up to how many days back the search looked for unprocessed records. The default value comes from the ERX DEFAULT LOOKBACK DAYS field in the Site Parameter Enter/Edit option \[PSO SITE PARAMETERS\]. This value can be changed by the user which will be described further below.

CS/NON-CS - Indicates Controlled Substances (CS) and Non-Controlled Substances (Non-CS) are displayed, including the CS Schedule (e.g., II-V).

MAXIMUM QUEUE SIZE - This parameter determines the maximum number of records to be loaded for the queue. The process will build and stop once it reaches this limit. The default is 999. User can request up to a maximum of 4,999. This parameter is displayed on the header of the Queue.

ERX STATUS - Indicates the status selection by the user before entering the list (e.g., I-In process, N, New).

#### Column Header Line 

| \# PATIENT DOB DRUG PROVIDER STA REC.DATE<span class="mark">^</span> |
|--------------------------------------------------------------------------|

\# - This column indicates the sequence number for the patient being displayed, which can be selected by the user to open the eRx in the eRx Holding Queue Display view screen (see below for eRx Holding Queue Display description).

PATIENT - Patient name column (maximum of 24 characters).

DOB - Date of birth column (MM/DD/YYY format).

DRUG - This is the eRx Drug Name exactly as received from the prescriber software. It is truncated at 22 characters.

STA - This is eRx Status column. It shows the current eRx record status. It’s truncated at 3 characters.

REC.DATE -This is the date when the eRx was received. By default, the list is always sorted by the REC. DATE column in a descending order (oldest records first) as noted by “<span class="mark">^</span>”.

#### Listing Area

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX I 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This area is where all the eRx records are listed. They are always in sequential order that goes from 1 to the last item on the list. The user will select a record by number to view a detailed description of the eRx in the eRx Holding Queue Display view screen (see below for eRx Holding Queue Display description).

#### Action & Hidden Action Menus

Below the Listing Area includes a few select actions that are available to users to filter or change views. Users can access the Hidden Action Menu by typing “??” (double question mark). Hidden Action Menu will be described further below.

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

SPAT – Sort By Patient

By default, the list is always sorted by the REC. DATE column in a descending order (oldest records first), but the user can sort the list by the Patient Name by selecting the SPAT action. Once the user selects it once, it will sort the list by Patient Name in an ascending order. If currently sorted by Patient Name and the users selects SPAT again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT<span class="mark">^</span> DOB DRUG PROVIDER STA REC.DATE |
|----------------------------------------------------------------------|

Rx Medication Queue – Sorted By Patient Name in Ascending Order

| \# PATIENT<span class="mark">v</span> DOB DRUG PROVIDER STA REC.DATE |
|----------------------------------------------------------------------|

Rx Medication Queue – Sorted By Patient Name in Descending OrderSQ – Search Queue

This action allows the user to place filters on the list by a few different selection criteria shown below. Multiple filters can be applied in one search criteria.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// SQ Search Queue</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - Search Queue options

SQ 1 - ERX PATIENT

User can filter search criteria by entering patient LAST NAME. Response must contain from 3 to 30 characters. Response must not contain embedded up-arrows (^).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: <strong>1 ERX PATIENT</strong></p>
<p>ERX PATIENT NAME: <strong>XXXXX, XXXXXXX</strong></p>
<p>LAST</p>
<p># ERX PATIENT NAME DOB CITY REC.DATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXXX, XXXXXXX X 99/99/9999 PLANO-TX 01/21/22</p>
<p>2. XXXXX, XXXXXXXX X 99/99/9999 NEW YORK-NY 09/27/23</p>
<p>SELECT (1-2): ?</p>
<p>This response must be a list or range, e.g., 1,3,5 or 2-4,8.</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – eRx Patient SelectionNote: The LAST REC.DATE column above displays the last date that the patient received an eRx.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT <strong>(XXXXX, XXXXXX| XXXXX, XXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Patient

SQ 2 – ERX DATE OF BIRTH

User can filter search criteria by entering DATE OF BIRTH.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 2 ERX DATE OF BIRTH</p>
<p>Date of Birth (DOB): 99999999 (XXX 99, 9999)</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT <strong>(XXXXX, XXXXXX| XXXXX, XXXXX)</strong></p>
<p>2 ERX DATE OF BIRTH <strong>(99/99/99)</strong></p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – eRx Patient and DOB filters selected

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1_</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: DOB(99/99/99)|PATIENT(XXXXX,XXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Patient and DOB resultSQ 3 – RECEIVED DATE RANGE

User can filter search criteria by entering a date range for the eRx Received Date. Begin date defaults to T-45 days. End date defaults to today. The Begin Date must not be a future date and the End Date must be earlier or equal to the Begin Date.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 3 RECEIVED DATE RANGE</p>
<p>BEGIN DATE: 09/29/2023//090123 (SEP 01, 2023)</p>
<p>END DATE: 10/19/2023//093023 (SEP 30, 2023)</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE <strong>(09/01/23 TO 09/30/23)</strong></p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Received Date Range

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: 09/08/23-09/28/23</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX PR 09/08/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/11/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/20/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Received Date Range resultSQ 4 – ERX PROVIDER

User can filter search criteria by entering an eRx Provider. This response can be free text. Response must contain from 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 4 ERX PROVIDER</p>
<p>ERX PROVIDER NAME: XXXX, XXXXX</p>
<p># ERX PROVIDER NAME NPI CITY STATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXX, XXXXX 9999999999 BIRMINGHAM AL</p>
<p>SELECT (1-1): 1</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER <strong>(XXXX, XXXXX)</strong></p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Provider

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 2</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PROVIDER(XXXX,XXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX RXA 09/05/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX RXA 09/05/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX R01 09/11/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX PR 09/25/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/27/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<p>9. XXXXX,XXXXXXXX 99/99/9999 ALMOPIDINE 100MG TAB XXXXX,XXXXX N 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Provider resultSQ 5 – ERX STATUS

User can filter search criteria by entering an eRx Order Status. User response must select one specific eRx Order Status. User can type “??” (double question mark) to review list of eRx status reason codes and numbers.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 5 ERX STATUS</p>
<p>ERX STATUS: ??</p>
<p>Choose from:</p>
<p>112 P PENDING</p>
<p>113 A APPROVED</p>
<p>114 PR PROCESSED</p>
<p>115 E ERROR</p>
<p>116 N NEW RX</p>
<p>117 I IN PROCESS</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG REACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit: ^</p>
<p>ERX STATUS: N NEW RX</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS <strong>(N)</strong></p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Status

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>STATUS(N)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX N 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX N 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx Status resultSQ 6 – DRUG NAME

User can filter search criteria by entering a drug name or parts of the name. This response is free text and must be between 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 6 DRUG NAME</p>
<p>DRUG NAME: ASP</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME <strong>(‘ASP’)</strong></p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Drug Name

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>DRUG(‘ASP’)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXXXX I 09/20/23</p>
<p>3. XXXX, XXXXXXXX 99/99/9999 ASPIRIN 325MG BUFFERE XXXXX,XXX W 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Drug Name resultSQ 7 – MESSAGE TYPE

User can filter search criteria by message type. User can type “??” (double question mark) to view list of message types associated with incoming eRx or enter message code.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 7 MESSAGE TYPE</p>
<p>MESSAGE TYPE: ??</p>
<p>This is the message type associated with an incoming eRx request</p>
<p>(Change, Cancel, RxRenewal, Partial Fill, etc.).</p>
<p>Choose from:</p>
<p>RR RXRENEWALREQUEST</p>
<p>RE RXRENEWALRESPONSE</p>
<p>N NEWRX</p>
<p>CR RXCHANGEREQUEST</p>
<p>RXF RXFILL</p>
<p>IE INBOUND ERROR</p>
<p>OE OUTBOUND ERROR</p>
<p>CA CANCELRX</p>
<p>CN CANCELRXRESPONSE</p>
<p>CX RXCHANGERESPONSE</p>
<p>MESSAGE TYPE: N</p>
<p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE (<strong>NEWRX)</strong></p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: &lt;RET&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Message Type

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1__</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>TYPE(NEWRX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 250MG S.T. XXXXX,XXXXX PR 09/16/23</p>
<p>2. XXXXX,XXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/27/23</p>
<p>3. XXXX, XXXXXXXX 99/99/9999 MELOXICAM 7.5MG TB XXXXX,XXXXX N 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Message Type resultSQ 8 – ERX REFERENCE NUMBER

User can filter search criteria by eRx ID. This search will take the user to the eRx Display screen and show the single eRx selected, which is described further down on this document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 8 ERX ID</p>
<p>ERX ID: 9999999999</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by eRx REFERENCE NUMBERSQ 9 – VISTA RX \#

User can filter search criteria VISTA RX#. This search will first find the eRx record associated with the VISTA Rx \# selected then the user will be taken to the eRx Holding Queue Display to view the single eRx selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 9 VISTA RX #</p>
<p>Rx #: 9999999999</p>
<p>This prescription is not an eRx prescription.</p>
<p>Rx #:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VISTA RX \#SQ 10 – VISTA PATIENT

Users can filter the list by a single or multiple VistA patients by entering name. Response must contain from 3 to 30 characters. For each VistA Patient selected the software will find all eRx patients that were ever matched to selected VistA patient and will convert this search into an eRx Patient search with all the eRx Patients associated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: 10 VISTA PATIENT</p>
<p>VISTA PATIENT NAME: XXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>---------------------------------------------------------------------------</p>
<p>1. XXXX,XXXXXX X 01/13/1970 SERIA LEONE-MT 08/10/23</p>
<p>2. XXXX,XXXXXXXX 09/24/1947 STEELTOWN-NV 08/10/23</p>
<p>3. XXXX,XXXXXXXXX X 02/16/1925 VENICIA-LA 09/30/23</p>
<p>4. XXXX,XXXXXXXXX 11/09/1950 MINOPOLIS-MI 06/20/23</p>
<p>5. XXXX,XXXXXXXX 07/01/1933 ELDORADO-AK</p>
<p>6. XXXX,XXXXXXXX X 07/29/1948 HOVINGTON-MO</p>
<p>7. XXXX,XXXXXXXXXX 07/10/1933 PICKLETON-SD 10/05/23</p>
<p>SELECT (1-9): 1-7</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXX,XXXXX X|XXXX,XXXXXX|XXXX,XXXXXXX,...)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT <strong>(XXXX,XXXXX X|XXXX,XXXXXX|XXXX)</strong></p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VISTA PATIENT

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 10 VISTA PATIENT</p>
<p>VISTA PATIENT NAME: XXXXXX</p>
<p>LAST</p>
<p># VISTA PATIENT NAME DOB CITY REC.DATE</p>
<p>----------------------------------------------------------------------------</p>
<p>1. XXXXXX,XXXXXX X 01/13/1970 SERIA LEONE-MT 08/10/23</p>
<p>2. XXXXXXX,XXXXXX X 09/24/1947 STEELTOWN-NV 08/10/23</p>
<p>3. XXXXXXXX,XXXXXX 02/16/1925 VENICIA-LA 09/30/23</p>
<p>4. XXXXXX,XXXXXXX X 11/09/1950 MINOPOLIS-MI 06/20/23</p>
<p>SELECT (1-4): 1-4</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT <strong>(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT <strong>(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – VistA Patient

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PATIENT(XXXXX,XXXXXX X|XXXXXXX,XXXXXX|...)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by VistA Patient resultSQ 11 – VISTA PROVIDER

Users can filter the list by a single or multiple VistA provider by entering name. Response must contain from 3 to 30 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select one of the following:</p>
<p>1 RX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>SEARCH BY: 11</p>
<p>VISTA PROVIDER NAME: XXX</p>
<p># VISTA PROVIDER NAME DEA CITY REC.DATE</p>
<p>-------------------------------------------------------------------------------</p>
<p>1. XXX,XXXXXXX AM3256181 NEW YORK,NY 10/12/23</p>
<p>2. XXX,XXXXXXX X BD9270911 ROCHESTER,NY 09/21/23</p>
<p>SELECT (1-2): 1-2</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – VistA Provider Search

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: PROVIDER(XXXXX,XXXXXX X|XXXXXXX,XXXXXX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX X I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Provider resultSQ 12 – MATCH STATUS

This search will qualify patients based on the matching status of the patient, provider, and drug to a corresponding VistA Record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SEARCH BY: 12 MATCH STATUS</p>
<p>Select one of the following:</p>
<p>1 PATIENT FAIL - PATIENT NOT MATCHED</p>
<p>2 PROVIDER FAIL - PROVIDER NOT MATCHED</p>
<p>3 DRUG FAIL - DRUG NOT MATCHED</p>
<p>4 BASIC - PATIENT, PROVIDER AND DRUG MATCHED</p>
<p>MATCH STATUS: 4</p>
<p><strong>NOTE: Only patients with actionable records are captured with this search.</strong></p>
<p><strong>Non-Actionable records can be searched through the SQ action under Rx</strong></p>
<p><strong>List View.</strong></p>
<p>Select one of the following:</p>
<ol type="1">
<li><p>RX PATIENT</p></li>
<li><p>ERX DATE OF BIRTH</p></li>
<li><p>RECEIVED DATE RANGE</p></li>
<li><p>ERX PROVIDER</p></li>
<li><p>ERX STATUS</p></li>
<li><p>DRUG NAME</p></li>
<li><p>MESSAGE TYPE</p></li>
<li><p>ERX REFERENCE NUMBER</p></li>
<li><p>VISTA RX #</p></li>
<li><p>VISTA PATIENT</p></li>
<li><p>VISTA PROVIDER</p></li>
<li><p>MATCH STATUS (BASIC)</p></li>
</ol>
<p>SEARCH BY: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Match Status

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>MATCH(BASIC)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Search by Match Status result12.1 –MATCH STATUS: PATIENT FAIL - PATIENT NOT MATCHED

If the patient has at least one actionable record which the eRx patient has not yet been matched to a corresponding VistA patient it will be included in the list.

12.2 –MATCH STATUS: PROVIDER FAIL - PROVIDER NOT MATCHED

If the patient has at least one actionable record which the eRx provider has not yet been matched to a corresponding VistA provider AND the patient does not qualify for PATIENT NOT MATCHED filter above, it will be included in the list.

12.3 – MATCH STATUS: DRUG FAIL - DRUG NOT MATCHED

If the patient has at least one actionable record which the eRx Drug has not yet been matched to a corresponding VistA drug AND the patient does not qualify for PATIENT NOT MATCHED filter above AND the patient does not qualify for the PROVIDER NOT MATCHED filter above, it will be included in the list.

12.4 – MATCH STATUS: BASIC - PATIENT, PROVIDER AND DRUG MATCHED

If the patient has at least one actionable record which the eRx patient has been matched to the VistA patient, the eRx Provider has been matched to the VistA provider and the Drug has been matched to a VistA drug AND the patient does not qualify to either of the 3 filters described above, it will be included in the list.

LBD – Change Look Back Days

This action allows the user to change the number of days to look back for eRx actionable records. A number between 0 (zero) and 1,000 can be selected. 0 (zero) would include only records for today’s date. Once the new value is selected the list is refreshed to account for the new number of days to look back and the new number will be displayed on the header section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX I 09/16/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// LBD</p>
<p>LOOK BACK DAYS: 365//45 Please wait...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Change Look Back DaysPC – Patient Centric View

This action allows the user to return to the eRx Patient Centric Queue

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p><strong>4. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</strong></p>
<p>5. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>10] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 2 0 1 0 0 0 3</p>
<p><strong>14] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 0 0 0 0 1</strong></p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Patient Centric Queue

RAF – Remove All Filters

This action allows the user to remove all filters currently applied to the list. This list is then refreshed to without any filters.

REF – Refresh List

This action allows the user to refresh the list. This is used to make sure you’re looking at the latest version of the list because other users might have already worked through some of the records currently on the list which may have altered it the changes won’t show until the list is refreshed. This new action called Refresh (REF) was added to allow the user to re-display the queue. This feature also allows the user to view the latest “locks” from other users that have been placed since the queue was last built.

#### Hidden Action Menus

The user can access the Hidden Action Menu can be viewed by typing “??” (double question mark). The user can use easily filter the list by Message Type by selecting one of the following hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>CS Group By CS CR Change Request only UP Up a line</p>
<p>SDOB Sort by DOB RXF Rx Refill Only DN Down a Line</p>
<p>SDRU Sort By Drug IE Inbound Errors Only FS First Screen</p>
<p>SPRO Sort by Provider OE Outbound Errors Only LS Last Screen</p>
<p>SSTA Sort by Status CA Cancel Rx’s Only GO Go to Page</p>
<p>SREC Sort by Received Date CN Cancel Response Only PS Print Screen</p>
<p>CV Change View CX Change Response Only PT Print List</p>
<p>RRQ Renewal Request Only DET Show/Hide Details SL Search List</p>
<p>RRP Renewal Response Only + Next Screen QU Quit</p>
<p>New New Rx’s Only - Previous Screen</p>
<p>Type &lt;Enter&gt; to continue or ‘^” to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CS – Group By CS (Hidden)

This action allows the user to group the list in two listing areas: Controlled Substances (CS) and Non-Controlled Substances (Non-CS) as seen below. The action can be used to turn ON and OFF this hidden action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Rx medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 3_______</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong><mark>v</mark></strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><u><strong>CONTROLLED SUBSTANCE Rx's a</strong></u></p>
<p>1] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 1 0 0 1 2</p>
<p>2] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 2 0 1 0 0 0 3</p>
<p>3] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 3 0 0 1 0 0 4</p>
<p>4] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 1 0 1 0 0 0 2</p>
<p>5] XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 37 0 0 1 0 0 1 2</p>
<p><u><strong>NON-CONTROLLED SUBSTANCE Rx's a</strong></u></p>
<p>6. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 1 0 0 0 1 0 2</p>
<p>7. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 44 0 0 2 1 0 0 3</p>
<p>8. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 41 0 0 1 0 0 0 1</p>
<p>9. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 40 0 0 1 0 0 0 1</p>
<p>10 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 38 0 0 1 0 0 0 1</p>
<p>11. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 35 1 0 0 0 1 0 2</p>
<p>12. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 33 1 0 0 0 0 0 1</p>
<p>13. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 2 0 1 0 0 0 3</p>
<p>14 XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 32 1 0 0 0 0 0 1</p>
<p>15. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<p>16. XXXXX,XXXXXXXXXX 99/99/9999 999-99-9999 34 1 0 0 0 0 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Grouped by CS and Non-CS

SDOB – Sort By Date of Birth (Hidden)

By default, the list is sorted by the ED (Elapsed Days) column in a descending order (oldest records first), but the user can sort the list by the Patient Date of Birth (DOB) by selecting the SDOB hidden action. Once the user selects it once, it will sort the list by Patient DOB in an ascending order. If currently sorted by Patient DOB and the users selects SDOB again it will reverse the sorting order (from ascending to descending and vice-versa), as shown below:

| \# PATIENT DOB<span class="mark">^</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Rx Medication Queue – SDOB - Sorted By Patient DOB in Ascending Order

| \# PATIENT DOB<span class="mark">v</span> SSN ED NW WT IP HD CCR OTH TOT |
|------------------------------------------------------------------------------|

Rx Medication Queue – SDOB - Sorted By Patient DOB in Descending Order

SDRU – Sort By Drug (Hidden)

This hidden action sorts the display list by eRx Drug Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SDRU\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>^</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SDRU - Sort By Drug in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SDRU SDRU Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1__</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME<strong><mark>v</mark></strong> PROVIDER NAME REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – SDRU - Sort By Drug in Descending Order

SPRO – Sort by Provider (Hidden)

This hidden action sorts the display list by eRx Provider Name. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SPRO\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>^</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SPRO - Sort By Provider in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SPRO SPRO Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 28, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME<strong><mark>v</mark></strong> REC.DATE STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SPRO - Sort By Provider in Descending Order

SSTA – Sort by Status (Hidden)

This hidden action sorts the display list by eRx Status. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SSTA\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>^</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SSTA - Sort By Status in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SSTA SSTA Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1___</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE STA<strong><mark>v</mark></strong> PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SSTA - Sort By Status in Descending Order

SREC – Sort by Rec. Date (Hidden)

This hidden action sorts the display list by eRx Received Date. The entries are sorted in ascending \[^\] or descending \[v\]. To change the chronological order of the entries, enter the \<SREC\> action a second time.

\[^\] and \[v\] are sort indicators to inform the user of the current enabled sort.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>^</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>2. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SREC - Sort By received Date in Ascending Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select: Quit// SREC SREC Please wait...</p>
<p><u><strong>Rx Medication Queue</strong> Sep 27, 2023@14:38:27 Page: 1 of 1____</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: BOTH (II-V) MAX. QUEUE SIZE: 999</p>
<p>ERX STATUS: ALL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong><mark>v</mark></strong> STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 99999996 ASPIRIN 500/CAFFEINE 3 YYYYYY,YYYYY Y 09/27/23 W MV MV AV</p>
<p>2. 99999999 LOVASTATIN 40MG TAB XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>3] 99999998 DIAZEPAM 5MG TAB XXXXXX,XXXXX X 09/28/23 N A</p>
<p>4. 99999997 VITAMIN B COMPLEX/VITA XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<p>5. 99999995 AMANTADINE 100MG CAP XXXXXX,XXXXX X 09/28/23 N A A<strong>V</strong> A</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Items (s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue - SREC - Sort By Received Date in Descending Order

CV – Change View (Hidden)

This hidden action allows the user to change the following parameters that affect the content and appearance of the eRx Patient Centric Queue. Some of these parameters also have their own action (e.g., LBD – Look Back Days). Furthermore, the users can also save the parameters to be applied to the queue every time they enter the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// CV Change View</p>
<p>LOOK BACK DAYS: 45// 45 DAYS</p>
<p>SORT BY: ED// ED ELAPSED DAYS</p>
<p>SORT ORDER: D// DESCENDING</p>
<p>INCLUDE CS/NON-CS: B// BOTH (CS AND NON-CS)</p>
<p>CS SCHEDULE: SCHEDULES II - V// SCHEDULES II - V</p>
<p>GROUP BY CS: NO// NO NO</p>
<p>MAXIMUM QUEUE SIZE: 999//</p>
<p>Save as your default view? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue – Change View hidden action (No Default View Saved)

RRQ – Renewal Request Only (Hidden)

This hidden action allows the user to filter the list by Renewal Request Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RRQ</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRENEWALREQUEST)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX RXR 09/28/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX RXR 09/28/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX RXR 09/28/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXR 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Renewal Request OnlyRRP – Renewal Response Only(Hidden)

This hidden action allows the user to filter the list by Renewal Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RRP</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: N/A CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRESPONSEONLY)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXP 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Renewal Response OnlyNEW – New eRx’s Only (Hidden)

This hidden action allows the user to filter by new Rx’s Only (status in New, In Process, Hold, and Wait)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>NEW</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(NEWRX)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX PR 09/08/23</p>
<p>2. XXXXX,XXXXXXXX 99/99/9999 NAPROXEN 25MG TABLET XXXXX,XXXXX I 09/11/23</p>
<p>3. XXXXX,XXXXXXXX 99/99/9999 MELOXICAN7.5MG TB XXXXX,XXXXX N 09/16/23</p>
<p>4. XXXXX,XXXXXXXX 99/99/9999 LOSARTAN 20MG TAB XXXXX,XXXXX I 09/20/23</p>
<p>5. XXXXX,XXXXXXXX 99/99/9999 IBUPROFEN 400MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>6. XXXXX,XXXXXXXX 99/99/9999 LOXAPINE 50MG CAP XXXXX,XXXXX N 09/25/23</p>
<p>7. XXXXX,XXXXXXXX 99/99/9999 ASPIRIN 200MG TAB XXXXX,XXXXX I 09/25/23</p>
<p>8. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX I 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by New eRx OnlyCR – Change Request Only (Hidden)

This hidden action allows the user to filter by Change Request Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CR</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXCHANGEREQUEST)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 TYLENOL 250MG TAB XXXXX,XXXXX CXN 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Cancel Rx ResponseRXF – Rx Refill Only (Hidden)

This hidden action allows users to filter by Rx Refill Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>RXF</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRFILL)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 BENADRYL DIPHENHYDRA XXXXX,XXXXX RXF 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Medication Queue (Hidden Action) – Filtered by Rx Refill OnlyIE – Inbound Errors Only (Hidden)

This hidden action allows users to filter by Inbound Errors Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>IE</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(INBOUND ERROR)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Inbound Errors OnlyOE – Outbound Errors Only (Hidden)

This hidden action allows users to filter by Outbound Errors Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>OE</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(OUTBOUND ERROR)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Outbound Errors OnlyCA – Cancel Rx’s Only (Hidden)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CA</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXRFILL)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/9999 METOPROLOL XXXXX,XXXXX CAO 09/28/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Cancel Rx’s OnlyCN – Cancel Response Only (Hidden)

This hidden action allows users to filter by Cancel Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CN</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(CANCELRXRESPONSE)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Inbound Errors OnlyCX – Change Response Only (Hidden)

This hidden action allows users to filter by Change Response Only

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>CX</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 28, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: 365 CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p><strong>FILTERED BY: TYPE(RXCHANGERESPONSE)</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>No prescriptions found.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Filtered by Change Response OnlyDET – Show/Hide Details (Hidden)

This hidden action will show/hide additional information about each one of the eRx on the list. It will display Qty, \# of Refills, Days Supply, and the SIG (medication instructions).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/99 WARFARIN 2MG TAB XXXXX,XXXXX I 12/13/22</p>
<p>2. XXXXX,XXXXXXXX 99/99/99 METOPROLOL 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) –Hide Details

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// <strong>DET</strong></p>
<p><u><strong>eRx Medication Queue</strong> Sep 16, 2023@11:06:54 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DATE<strong><mark>^</mark></strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXX,XXXXXXXX 99/99/99 WARFARIN 2MG TAB XXXXX,XXXXX I 12/13/22</p>
<p><strong>eRx Qty: 30 eRx # of Refills: 0 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE ONE TABLET BY MOUTH EVERY 24 HOURS</strong></p>
<p>2. XXXXX,XXXXXXXX 99/99/99 METOPROLOL 25MG TABLET XXXXX,XXXXX I 09/16/23</p>
<p><strong>eRx Qty: 90 eRx # of Refills: 15 eRx Days Supply: 90</strong></p>
<p><strong>SIG: TAKE ½ TABLET BY MOUTH EVERY DAY</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Rx Medication Queue (Hidden Action) – Show Details

### Single eRx Details Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A record from the eR<sub>X</sub> Single Patient Queue or Rx Medication Queue can be selected by typing the record number itself. The first screen displayed is the Summary/Details screen, which displays information about the original eR<sub>X</sub> from the external provider and matched VistA information (if any).

On this screen, the header contains the eR<sub>X</sub> Patient Name and eR<sub>X</sub> Reference \#, which is an internal VA reference number assigned for tracking the eR<sub>X</sub>. Below the header is information received from the external provider for the patient, provider, and the drug/SIG. Where applicable, VistA information displays below the eR<sub>X</sub> information.

> **NOTE:** - “eRx Written Date” – Date the eR<sub>X</sub> was received in the VistA Holding Queue.

- “eRx Issue Date” – Effective Date, if sent by the provider.

#### eRx Details

To view the details of an eR<sub>X</sub>, select the record number from either the Single Patient eRx Queue or Rx.

> **NOTE:** From the Summary/Details screen, users <u>cannot</u> edit any of the VistA information. The validate screens contain the option for editing the VistA information. For further information on editing and validating VistA information for an eR<sub>X</sub>, refer to section 6.2.

#### Non-CS eRx Details Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 15, 2023@12:31:51 Page: 1 of 1</u></p>
<p>eRx Patient: XXXXXXXX,XXXXXXX X</p>
<p>eRx Reference #: 9999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p><mark>NEWRX</mark></p>
<p>eRx Status: NEW RX</p>
<p>eRx Patient: XXXXXXX,XXXXXXXX X DOB: 99/99/99</p>
<p>Vista Patient: NOT LINKED DOB:</p>
<p>eRx Provider Primary Telephone: 999-999-9999</p>
<p>eRx Provider: YYYYYYYYYYY,YYYYYYY Y</p>
<p>DEA#: XX9999999 NPI: 9999999999</p>
<p>Vista Provider: NOT LINKED</p>
<p>DEA#: NPI:</p>
<p>eRx Drug: MAGNESIUM 200MG TAB</p>
<p>eRx Qty: 60 eRx Refills: 11 eRx Days Supply: 3</p>
<p>eRx Written Date: SEP 30, 2023 eRx Issue Date:</p>
<p>Prohibit Renewals: No</p>
<p>eRx Sig:</p>
<p>TAKE ONE CAPSULE BY MOUTH ONCE DAILY BEFORE MEAL</p>
<p>Vista Drug: NOT LINKED</p>
<p>Vista Qty: 90 Vista Refills: 0 Vista Days Supply: 90</p>
<p>Substitutions? :YES</p>
<p>Vista Sig:</p>
<p>Pat Inst:</p>
<p>Hold Status:</p>
<p>Hold Reason:</p>
<p>Placed on hold by:</p>
<p>eRx Notes:</p>
<p>Allergies</p>
<p>Verified: WASP STINGS,</p>
<p>Adverse Reactions</p>
<p>Primary Dx: (ICD-10 A01.01) Typhoid meningitis</p>
<p>Description: Typhoid meningitis Test primary diagnosis</p>
<p>Secondary Dx: (ICD-10 E11.21) Type 2 diabetes mellitus with diabetic</p>
<p>nephropathy</p>
<p>Description: Test secondary Diagnosis</p>
<p>Primary Dx: (ICD-10 L40.0) Psoriasis vulgaris</p>
<p>Description: Test Primary diagnosis</p>
<p>Secondary Dx: (ICD-10 B18.9) Chronic viral hepatitis, unspecified</p>
<p>Description: Test Secondary Diagnosis</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Holding Queue Display Screen – Not Digitally Signed (Non-CS)

This initial screen shown right after the user selects an individual eRx records shows a summary of the entire eRx record as well as the corresponding VistA matched records. VistA records can be automatically matched by the software or manually entered by the user by selecting the Validation actions VP (Validate Patient), VM (Validate Provider) and VD (Validate Drug). Received Allergy and Diagnosis information are also displayed. Digitally Signed eRx’s will display the additional information shown above.

If the VistA information for the patient, provider, or drug is not linked, the display is as shown below:

- VistA Patient: NOT LINKED
- VistA Provider: NOT LINKED
- VistA Drug: NOT LINKED

#### CS eRx Details Display

The only differences from a Non-CS are the two highlighted information below that are include for all Digitally Signed eRx.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 15, 2023@12:31:51 Page: 1 of 1</u></p>
<p>eRx Patient: XXXXXXXX,XXXXXXX X</p>
<p>eRx Reference #: 9999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p><mark>NEWRX</mark></p>
<p>eRx Status: NEW RX</p>
<p>eRx Patient: XXXXXXX,XXXXXXXX X DOB: 99/99/99</p>
<p>Vista Patient: NOT LINKED DOB:</p>
<p>...</p>
<p>Secondary Dx: (ICD-10 B18.9) Chronic viral hepatitis, unspecified</p>
<p>Description: Test Secondary Diagnosis</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Holding Queue Display Screen – Digitally Signed (CS)

> **NOTE:** The fact that an eRx is Digitally Signed does not mean it will become a Controlled Substance VistA prescription. The criteria for an eRx to become a CS VistA Rx is dependent on the VistA Dispense Drug matched to the eRx. If the VistA Dispense Drug is marked as CS then the VistA prescription will be treated as a CS VistA prescription, otherwise it will not.

#### Rx Details Display – Allergy Information

VistA information displayed includes allergies and diagnosis. If the patient has no known allergies, “NKA” displays in the Allergies section.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 15, 2023@12:31:51 Page: 1 of 1</u></p>
<p>eRx Patient: XXXXXXXX,XXXXXXX X</p>
<p>eRx Reference #: 9999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p><mark>NEWRX</mark></p>
<p>eRx Status: NEW RX</p>
<p>...</p>
<p>Adverse Reactions:</p>
<p>...</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with No Allergy Assessment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 15, 2023@12:31:51 Page: 1 of 1</u></p>
<p>eRx Patient: XXXXXXXX,XXXXXXX X</p>
<p>eRx Reference #: 9999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p><mark>NEWRX</mark></p>
<p>eRx Status: NEW RX</p>
<p>...</p>
<p>Adverse Reactions:</p>
<p>...</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with No Known Allergies

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 15, 2023@12:31:51 Page: 1 of 1</u></p>
<p>eRx Patient: XXXXXXXX,XXXXXXX X</p>
<p>eRx Reference #: 9999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p><mark>NEWRX</mark></p>
<p>eRx Status: NEW RX</p>
<p>...</p>
<p>...</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with Known Allergies

#### Action & Hidden Action Menus

A few actions can be taken by the user on list displayed. The Action Menu is displayed right below the listing area while the Hidden Action Menu can be viewed by typing “??” (double question mark).

#### Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Due to the complexity of the functionality behind the VP (VALIDATE PATIENT), VM (VALIDATE PROVIDER) and VD (VALIDATE DRUG) the action menu actions will be explained separately in the next manual (Section 6, Part 2).

- Manual Validation:
  - \<VP\> [VALIDATE](\l) PATIENT
  - \<VM\> [VALIDATE](\l) PROVIDER
  - \<VD\> ([VALIDATE](#_Validate_Drug/SIG) DRUG/SIG)

> NOTE: The VALIDATE DRUG/SIG is not available unless a VistA patient has been matched, as indicated with parenthesis around the action.

#### P – Print

Printing in the eR<sub>X</sub> Holding Queue displays all details of an eR<sub>X</sub> and allows the user to select a local printer and print the eR<sub>X.</sub>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// p Print</p>
<p>DEVICE: ;;999 HOME (CRT)</p>
<p>*PHARMACY INFORMATION</p>
<p>VAMC PHARMACY NAME</p>
<p>Address: P.O. BOX 999999</p>
<p>XXXXXXXXXXX, XXXXXXX 99999-9999</p>
<p>Primary Telephone: 99999999999 NCPDP: 9999999</p>
<p>PRESCRIBER INFORMATION*</p>
<p>Last: XXXXXXXXXXXX</p>
<p>First: XXXXXXXX</p>
<p>Mid: X</p>
<p>Address: 999 XXXX XXXXXXXX XX</p>
<p>APT 9999</p>
<p>XXXXXXXXXX, XXXXXXXXXX 99999-9999</p>
<p>NPI: 99999999999</p>
<p>DEA: XX99999999</p>
<p>State Lic:</p>
<p>Primary Telephone: 999-999-9999</p>
<p>Fax:</p>
<p>Supervisor:</p>
<p>Agent Last Name:</p>
<p>Agent First Name:</p>
<p>Agent Middle Name:</p>
<p>PATIENT INFORMATION</p>
<p>Last: XXXXXXXXXXXXX</p>
<p>First: XXXX</p>
<p>Mid: X</p>
<p>SSN: 99999999 Sex: MALE</p>
<p>Address: 999 XXXXXXXXXXX XXXXX XXX</p>
<p>XXXXXXXXXXXXXX, XXXXXXXXXXX 99999-9999</p>
<p>DOB: XXX 99, 9999 Primary Telephone: 999-999-9999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>PRESCRIPTION INFORMATION*</p>
<p>eRx Drug: MAGNESIUM 200MG TAB</p>
<p>NDC: 999999999999</p>
<p>eRx Written Date: SEP 30, 2023 eRx Issue Date:</p>
<p>Qty: 60 Days Supply: 30</p>
<p>Code List Qualifier: Original Quantity</p>
<p>Drug Form:</p>
<p>Strength:</p>
<p>Refills: 11</p>
<p>Prohibit Renewals: No</p>
<p>Substitutions?: YES</p>
<p>eRx Sig:</p>
<p>TAKE 1 TABLET ONCE A DAY WITH FOOD</p>
<p>eRx Reference #: 99999999</p>
<p>Message ID: 999.999999.9999999.999999</p>
<p>Substitutions?: YES</p>
<p>Comments:</p>
<p>*END OF eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Print eRx Output

#### RJ – Reject

Rejecting an eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes the eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// RJ Reject</p>
<p>Would you like to 'Reject' eRx #33939? Y// ES</p>
<p>Select REJECT reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>203 PTT01 Patient not eligible</p>
<p>204 PTT02 Cannot resolve Patient</p>
<p>205 PVD01 Provider not eligible</p>
<p>206 PVD02 Cannot resolve Provider</p>
<p>207 DRU01 Not eligible for refills</p>
<p>208 DRU02 Non-formulary drug</p>
<p>209 DRU03 Duplicate Prescription found for this Patient</p>
<p>210 DRU04 Invalid Quantity</p>
<p>211 DRU05 Duplicate therapeutic class</p>
<p>212 DRU06 CS prescription written/issue date has problems</p>
<p>213 ERR01 Multiple errors, please contact the Pharmacy</p>
<p>214 ERR02 Incorrect Pharmacy</p>
<p>215 ERR03 Issues with prescription, please contact the pharmacy</p>
<p>1627 PVD03 Missing/bad digital signature on inbound CS ERX</p>
<p>1628 PVD04 Prescriber's CS credential is not appropriate</p>
<p>1629 PTT03 Patient's mailing address is missing/mismatched</p>
<p>1630 ERR99 Other</p>
<p>Select REJECT reason code: PTT01 Patient not eligible</p>
<p>Additional Comments (Optional):</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Reject eRx

#### AC – Accept eRx

Accepting an eRx in the eRX Holding Queue action is not available until the validation of the eR<sub>X</sub> Patient, provider, and drug/SIG have been completed. Also note that the \<AC\> action is not available if the eR<sub>X</sub> is on Hold.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// ac Accept eRx</p>
<p>Errors encountered during processing:</p>
<p>1.) Drug has not been manually validated.</p>
<p>Cannot process eRx.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRx – Drug no validated

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// ac Accept eRx</p>
<p>eRx #99999999 sent to PENDING ORDERS Queue. (Clinic: XXXXXXXXXXXXXX)</p>
<p>Sending rxVerify Message to prescriber.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRx – Drug no validated

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Meds-By-Mail site users will be prompted to select a Clinic if the current Clinic on the eRx being accepted is different that the Clinic they logged on upon entering the eRx Holding Queue Processing option.</p>
<p>eRx Clinic (Optional): XXXXXXXXXXXXXXXX//</p>
<p>The default clinic will be the Clinic they are logged on.</p></td>
</tr>
</tbody>
</table>

#### H – Hold

This action places eR<sub>X</sub> on Hold in the eR<sub>X</sub> Holding Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// H Hold</p>
<p>Select HOLD reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? y (Yes)</p>
<p>Choose from:</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG INTERACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>129 HPR HOLD DUE TO PATIENT REQUEST</p>
<p>130 HQY QUANTITY OR REFILL ISSUE</p>
<p>1618 HCR PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>1619 HWR CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>1620 HIS PROVIDER DEA# ISSUE</p>
<p>1621 HRX HOLD FOR RX EDIT</p>
<p>1622 HDE DRUG USE EVALUATION</p>
<p>1623 HTI THERAPUTIC INTERCHANGE</p>
<p>1624 HSC SCRIPT CLARIFICATION</p>
<p>1625 HGS GENERIC SUBSTITUTION</p>
<p>1631 HAL NO ALLERGY ASSESSMENT</p>
<p>1632 HEL ELIGIBILITY ISSUE</p>
<p>1633 HUR UN-REMOVED</p>
<p>Select HOLD reason code: HSO INSUFFICIENT STOCK</p>
<p>Additional Comments (Optional):</p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold – Single eRx

Batch Holding

Once the user completes holding one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider. If it does, the software will offer the also put these eRx on hold with the same reason and comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the same day:</p>
<p>PROVIDER: XXXXXXX,XXXXXX eRx RECEIVED DATE: OCT 04, 2023@18:14:50</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------</p>
<p>999999999 NAPROXEN 250MG TAB XXXXXXX,XXXXXX N</p>
<p>999999999 UREA 20% CREAM XXXXXXX,XXXXXX N</p>
<p>Do you want to put them on HOLD-HSO? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Hold

#### UH – UnHold

This action removes the eR<sub>X</sub> from Hold in the eR<sub>X</sub> Holding Queue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// UH Un Hold</p>
<p>Additional Comments (Optional):</p>
<p>eRx removed from hold status, and placed to 'In process'.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Holding – Single eRx

Similar to Batch Holding, the Batch Un-Holding performs the opposite functionality. Once the user completes un-holding one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider that have also been put on Hold with the same Hold Code. If it does, the software will offer the also remove these eRx from hold with the same comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the same day:</p>
<p>PROVIDER: XXXXXXX,XXXXXX eRx RECEIVED DATE: OCT 04, 2023@18:14:50</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>------------------------------------------------------------------------</p>
<p>999999999 NAPROXEN 250MG TAB XXXXXXX,XXXXXX N</p>
<p>999999999 UREA 20% CREAM XXXXXXX,XXXXXX N</p>
<p>Do you want to remove them from HOLD? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Un-Holding

#### RM – Remove eRx

Removing the eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// RM Remove eRx</p>
<p>Select REMOVAL reason code: ?</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER, or BRIEF DESCRIPTION, or</p>
<p>CODE TYPE ABBREVIATION, or NCIT SUBTYPE</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>216 REM01 Drug out of stock or on backorder and unavailable for processing</p>
<p>217 REM02 Patient was not able to pick up</p>
<p>218 REM03 Prescription canceled by Provider</p>
<p>219 REM04 Prescription processed manually</p>
<p>220 REM05 Provider will cancel this eRx and submit another</p>
<p>221 REM06 Unable to mail prescription and patient unable to pick up</p>
<p>222 REM07 Unable to contact patient</p>
<p>223 REM08 Unable to contact provider</p>
<p>224 REM91 Undefined system error</p>
<p>225 REM92 Other</p>
<p>1626 REM09 ERX Issue not resolved-Provider contacted</p>
<p>Select REMOVAL reason code: REM02 Patient was not able to pick up</p>
<p>Additional Comments (Optional):</p>
<p>Would you like to 'Remove' eRx #11137? Y//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Hidden Action Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx Hidden Actions

#### AD – Add a Comment

This option is used to add a record comment to request and responses eRx types regarding refills/renewals.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// AD AD</p>
<p>REQUEST/RESPONSE COMMENTS: // ?</p>
<p>Enter the refill request/response comments. Answer must be 1-255</p>
<p>characters in length.</p>
<p>REQUEST/RESPONSE COMMENTS: // ASDLF JLKSDFJ LKASJDF KLSJDF LSJDF LASJDFKLSD</p>
<p><u><strong>eRx Holding Queue Display</strong> Nov 11, 2023@10:56:59 Page: 2 of 2</u></p>
<p>eRx Patient: XXXXXXX,XXXXXXXXX X</p>
<p>eRx Reference #: 999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>+________________________________________________________________________</p>
<p>Request Status: CANCEL RESPONSE FROM VISTA UNSUCCESSFUL</p>
<p>Requested By: XXXXXXX,XXXXXXXXXXXXXXX X</p>
<p>Request Date/Time: OCT 16, 2023@15:39:06</p>
<p>Request Comments: ASDLF JLKSDFJ LKASJDF KLSJDF LSJDF LASJDFKLSD F</p>
<p>Comments By: XXXXXXXX,XXXXX</p>
<p>Comments Date/Time: NOV 11, 2023@10:56:43</p>
<p>MESSAGE HISTORY</p>
<p>Request Reference #: 11134999</p>
<p>New eRx Reference #: 11134</p>
<p>Response eRx Reference #:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Add Comment

#### ACK – Acknowledge

The \<ACK\> hidden action is used by the user to indicate they are aware of the event that caused the eRx to be in the current status, which is the majority of cases is considered Actionable until it is acknowledged by the user and is then updated to a Non-Actionable Status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Nov 11, 2023@11:07:04 Page: 1 of 2</u></p>
<p>eRx Patient: XXXXXXXXXX,XXXXXXXX</p>
<p>eRx Reference #: 99999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p>CANCELRX</p>
<p>eRx Status: CANCEL PROCESS COMPLETE</p>
<p>Last New Rx status: I - IN PROCESS</p>
<p>eRx Patient: XXXXXXXXXXXXXX,XXXXXXXXX DOB: 10/1/48</p>
<p>eRx Provider: XXXXXXXXXXXX,XXXXXX</p>
<p>DEA#: XX9999999 NPI: 99999999999</p>
<p>eRx Drug: HYDROCHLOROTHIAZIDE 25MG TAB</p>
<p>eRx Qty: eRx Refills: eRx Days Supply:</p>
<p>eRx Written Date: eRx Issue Date:</p>
<p>CANCEL REQUEST INFORMATION*</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP (VALIDATE PATIENT) VM (VALIDATE PROVIDER) VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH (Un Hold) RM (Remove eRx)</p>
<p>Select Action:Next Screen// ACK ACK</p>
<p>Would you like to acknowledge this record?</p>
<p>Enter Yes or No: N// YES</p>
<p>Cancel request acknowledged.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p><u><strong>eRx Holding Queue Display</strong> Nov 11, 2023@11:07:04 Page: 1 of 2</u></p>
<p>eRx Patient: XXXXXXXXXX,XXXXXXXX</p>
<p>eRx Reference #: 99999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>___________________________________________________________________________</p>
<p>CANCELRX</p>
<p>eRx Status: CANCEL REQUEST ACKNOWLEDGED</p>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SH – Status History

The Status History \<SH\> hidden action displays the history of status changes on an eR<sub>X</sub> record within the Holding Queue. It does not include the initial status of the record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Status History – Hidden Action

Enter the hidden Status History \<SH\> action to display the history of status changes.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/002.png)

SH Action - Status Changes on eR<sub>X</sub> Record in Holding Queue

Comments are displayed where applicable (i.e. Hold, RJ, and RM statuses).

#### HL – View History Log

The View History Log (HL) hidden action has been added to the eRx Holding Queue Display screen. This action allows the user to display a comprehensive history of the eRx as it moves through the Outpatient Pharmacy software, including activities in Backdoor Pharmacy. The View History Log action will display the following information (if available):

- The Patient, Provider, and Drug Match/Validation Status
- The Status History
- The Order Status
- The Prescription Status
- The Rx Activity Log
- The CMOP Event Log
- The Change, Cancel, Renewal Log - which shows the related messages

> **NOTE:** If no data is available for a section it will display ‘No (section name) Available’.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Oct 30, 2023@14:22:34 Page: 1 of 3</u></p>
<p>eRx Patient: XXXXX,XXXXXXXXXX</p>
<p>eRx Reference #: 999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>NEWRX</p>
<p>eRx Status: IN PROCESS</p>
<p>eRx Patient: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>Vista Patient[v]: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>eRx Provider: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>Vista Provider: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>eRx Drug: TYLENOL ACETAMINOPHEN 325MG TAB</p>
<p>eRx Qty: 180 eRx Refills: 2 eRx Days Supply: 30</p>
<p>eRx Written Date: OCT 24, 2023 eRx Issue Date:</p>
<p>Prohibit Renewals: No</p>
<p>+ Enter ?? for more actions</p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

View History Log Hidden ActionNOTE: If no data is available for a section it will display ‘No (section name) Available’.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx History Log</strong> Nov 01, 2023@19:13:32 Page: 1 of 4</u></p>
<p>eRx Patient: XXXXX,XXXXXXXXXX</p>
<p>eRx Reference #: 999999999</p>
<p>Pat Auto-Match: Pat Manual Edit: MATCHED</p>
<p>Prov Auto-Match: MATCHED Prov Manual Edit: VALIDATED</p>
<p>Drug Auto-Match: MATCHED Drug Manual Edit:</p>
<p>Status History:</p>
<p>Date/Time Status Entered By</p>
<p>05/15/23@14:36:44 I-IN PROCESS USERNAME,USER</p>
<p><strong>Status Comments: COMMENTS ADDED</strong></p>
<p>05/15/23@14:39:20 I-IN PROCESS USERNAME,USER</p>
<p><strong>Status Comments: COMMENTS ADDED AGAIN</strong></p>
<p>05/15/23@14:47:44 I-IN PROCESS USERNAME,USER</p>
<p><strong>Status Comments: COMMENTS ADDED ONCE AGAIN</strong></p>
<p>05/15/23@14:51:41 W-WAIT USERNAME,USER</p>
<p><strong>Status Comments: COMMENTS FOR WAIT STATUS</strong></p>
<p>05/15/23@14:55:47 PR-PROCESSED USERNAME,USER</p>
<p><strong>Status Comments: COMMENTS FOR PROCESSED</strong></p>
<p>Order:</p>
<p>Date/Time Order# Status</p>
<p>11/02/21@08:14:19 99999999 DISCONTINUED</p>
<p>Prescription:</p>
<p>Prescription#: 9999999 Status: DISCONTINUED</p>
<p>Activity Log:</p>
<p>Date/Time Reason Rx Ref Initiator Of Activity</p>
<p>===========================================================================</p>
<p>05/17/23 PATIENT INST ORIGINAL</p>
<p><strong>Comments: Patient Instructions Sent By Provider.</strong></p>
<p>05/17/23@14:50:41 SUSPENDED ORIGINAL USERNAME,USER</p>
<p><strong>Comments: RX Placed on Suspense for CMOP until 05-17-23</strong></p>
<p>05/17/23@08:03:22 PROCESSED ORIGINAL USERNAME,USER</p>
<p><strong>Comments: Transmitted to CMOP NATIONAL CMOP</strong></p>
<p>09/18/23@08:14:19 IERX ORIGINAL USERNAME,USER</p>
<p><strong>Comments: Electronic RxRenewal Request sent to External Provider</strong></p>
<p>09/22/23@08:19:37 IERX ORIGINAL USERNAME,USER</p>
<p><strong>Comments: RxRenewal response from external provider – Replace.</strong></p>
<p>09/22/23@14:50:41 DISCONTINUED ORIGINAL USERNAME,USER</p>
<p><strong>Comments: eRx discontinued by external prescriber</strong></p>
<p>CMOP Event Log:</p>
<p>Date/Time Rx Ref TRN-Order Stat NDC</p>
<p>===========================================================================</p>
<p>05/19/23@11:07:20 ORIGINAL 99999-1 DISP 99999-9999-99</p>
<p>Carrier: USPS Package ID: PKGID99999</p>
<p><strong>Comments: CMOP Comments</strong></p>
<p>Change, Cancel, Renewal Log:</p>
<p><u>Date/Time MessageType eRx ID eRx Order Status</u></p>
<p>09/22/23@19:23:51 NEWRX 999999999 CAN</p>
<p><strong>Status Description: ORIGINAL ERX CANCELED IN THE HOLDING QUEUE</strong></p>
<p>09/22/23@19:37:57 RXRENEWALREQUEST V9999999 RRC</p>
<p><strong>Status Description: RXRENEWAL REQUEST COMPLETE</strong></p>
<p>09/23/23@20:29:36 RXRENEWALRESPONSE 99999 RXC</p>
<p><strong>Status Description: RXRENEWAL RESPONSE COMPLETE</strong></p>
<p>+ Enter ?? for more actions</p>
<p>Select Action:Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

View History Log display

#### EC – eRx Change Request

eR<sub>X</sub> Change Request \<EC\> hidden action is used to request change on a NewRx prescription from the external Provider who sent the original NewRx. For detailed information about RxChange Request, refer to <u>Unit 5 – RxChange Requests and Responses</u> available on the Veteran's Documentation Library (VDL).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Change Request

#### PA – Patient Allergies

If the VistA patient has known allergies, verified allergies display in the Allergies section. This section will be the same for the Patient Validation as well as for the Drug Validation Screens. Furthermore, the same segment will display in the Pending Order in Backdoor Pharmacy as well. The reverse video for each allergy on either side (eRx or VistA) indicates that the exact allergy was not found on the other side.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 18, 2023@13:37:41 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>999999</strong> Eligibility: <strong>NSC</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : APR 21, 1990 |DOB : JAN 1,1980</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>Sex : MALE |Sex : MALE</p>
<p>Address: |Address:</p>
<p>12345 TEST WAY | 12345 TEST WAY</p>
<p>CHEYENNE,WY 82001 | CHEYENNE,WY 82001</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with Known Allergies

A new hidden action is available on the Patient Validation screen that allows the user to display the Patient Allergies in greater detail. This hidden action can be invoked from the following screens listed below:

- Patient Validation screen
- Drug Validation screen
- eRx Holding Queue Display screen
- Pending Orders screen (Backdoor Outpatient Pharmacy)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>PA Patient Allergies DN Down a Line PS Print Screen</p>
<p>+ Next Screen FS First Screen PT Print List</p>
<p>- Previous Screen LS Last Screen SL Search List</p>
<p>UP Up a Line GO Go to Page QU Quit</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hidden Action (PA) Patient Allergies

When the user selects the Patient Allergies (PA) hidden action from the Patient Validation screen, a new screen displays titled Patient Allergies. The Patient Allergies screen was created to show the eRx patient allergies side-by-side with the VistA patient allergies in detail.

The Patient Allergies screen also contains a new action called VistA Patient Allergies (VPA). The VPA action invokes a new screen titled Detailed Allergy List and this screen allows the user to edit allergy data.

> **NOTE:** A VistA Patient must be matched to use the VistA Patient Allergies (VPA) action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 18, 2023@14:18:39 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : JUN 21, 1954 |DOB : JUN 21,1954</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>Sex : MALE |Sex : MALE</p>
<p>Address: |Address:</p>
<p>PO BOX 9999 | PO BOX 9999</p>
<p>NIRVANA,NY 12345 | NIRVANA,OR 12345</p>
<p>Primary Phone: 9999999999 |</p>
<p>Home Phone: |Home Phone: (999) 999-9999</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// PA PA</p>
<p><u><strong>Patient Allergies</strong> Oct 18, 2023@14:18:43 Page: 1 of 4</u></p>
<p>eRx Reference #: <strong>99999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: XXXXX,XXXXXXXXXX |Name: XXXXX,XXXXXXXXXX</p>
<p>DOB : JUN 21, 1954 |DOB : JUN 21,1954</p>
<p>SSN : 999999999 |SSN : 999-99-9999</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| <u>Drug:</u></p>
<p>| IBUPROFEN</p>
<p>| Effective Date: <strong>Dec 10, 2008@15:29</strong></p>
<p>| Reaction: <strong>OBSERVED</strong></p>
<p>| Severity: <strong>MODERATE</strong></p>
<p>| Symptoms:</p>
<p>| <strong>RASH</strong></p>
<p>| PERCODAN</p>
<p>| Effective Date: <strong>Nov 07, 2008@13:28</strong></p>
<p>| Reaction: <strong>HISTORICAL</strong></p>
<p>| Symptoms:</p>
<p>+ Enter ?? for more actions</p>
<p>VPA Vista Patient Allergies</p>
<p>Select Item(s): Next Screen// VPA Vista Patient Allergies</p>
<p><u><strong>DETAILED ALLERGY LIST</strong> Oct 18, 2023@14:50:25 Page: 1 of 1</u></p>
<p>XXXXX,XXXXXXXXXX &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 182.88 (02/24/2011)</p>
<p>DOB: JUN 21,1954 (69) Wt(kg): 93.44 (02/24/2011)</p>
<p>Verified</p>
<p>Drug:</p>
<p>1 ALBUTEROL</p>
<p>2 IBUPROFEN</p>
<p>3 PERCODAN</p>
<p>4 VALIUM</p>
<p>Drug/Food:</p>
<p>5 EGG PRODUCTS</p>
<p>6 PEANUTS</p>
<p>Food:</p>
<p>7 HONEY</p>
<p>8 TOMATO PRODUCTS</p>
<p>+ Enter ?? for more actions</p>
<p>EA Enter/Edit Allergy/ADR Data SA Select Allergy</p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient Allergies

#### UR – Un-Remove eRx

It is possible after a fillable eRx is Removed, it needs to be moved back to the Holding Queue to be processed. Users can utilize the Include All Statuses (IAS) action on the Single Patient Queue screen or use the Rx List View action on the eRx Patient Centric Queue screen, then use the Search Queue (SQ) action to search for the eRx with a Removed status (ERX STATUS). Once the Removed eRx is selected, the user can utilize the Un-Remove (UR) hidden action on the eRx Holding Queue Display screen. This action will allow users to Un-Remove an eRx that was previously Removed, so the eRx will display again on the eRx Single Patient Queue screen to be worked.

To Un-Remove an eRx from the Holding Queue:

1.  From the eRx Holding Queue Display screen, type \<UM\> Un-Remove eRx.
2.  Enter a HOLD reason code for the eRx Un-Removal.

> NOTE: A default value of HUR (HOLD UNREMOVE) will display and can be selected.

3.  Type Additional Comments as to why the eRx is being Un-Removed and press \<Enter\>.

These comments are optional.

> **NOTE:** Only eRxs with a REMOVED status can be UN-REMOVED.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Nov 01, 2023@11:36:08 Page: 1 of 3</u></p>
<p>eRx Patient: XXXXX,XXXXXXXXXX</p>
<p>eRx Reference #: 999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>NEWRX</p>
<p>eRx Status: Prescription canceled by Provider</p>
<p>eRx Patient: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>Vista Patient[v]: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>eRx Provider: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>Vista Provider: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>eRx Drug: TYLENOL ACETAMINOPHEN 325MG TAB</p>
<p>eRx Qty: 180 eRx Refills: 2 eRx Days Supply: 30</p>
<p>eRx Written Date: OCT 24, 2023 eRx Issue Date:</p>
<p>Prohibit Renewals: No</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// UR UR</p>
<p>Select HOLD reason code: HUR// HOLD UNREMOVE</p>
<p>Additional Comments (Optional): UNREMOVE COMMENTS</p>
<p>Would you like to 'Un-Remove' eRx #33005500? Y// ES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Remove an eRx

#### Jump to OP

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR, from the eR<sub>X</sub> Holding Queue Summary/Details screen. Once the user has completed reviewing on the Outpatient side, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

The Jump to OP \<JO\> hidden action allows the user to navigate to Complete Orders from OERR only if the following conditions are true:

1.  The R<sub>X</sub> record is a fillable prescription only.
1.  The VistA Patient is already matched to an eR<sub>X</sub> Patient under the [Validate Patient](\l) \<VP\> action.
2.  The matched VistA Patient has been validated.

To use the Jump to OP action, enter \<??\> to view a list of hidden actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Jump to OP – Hidden Action

Enter the hidden Jump to OP \<JO\> action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// JO JO</p>
<p>Vista patient has not been matched. Cannot jump to outpatient.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

JO Action Selected (Patient not matched)

If a user attempts to Jump to OP \<JO\> when a VistA Patient is not matched to an eR<sub>X</sub> Patient, an error message is received stating, “VistA patient has not been matched. Cannot jump to outpatient”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// JO JO</p>
<p>Vista patient has not been validated. Cannot jump to outpatient.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

JO Action Selected (Patient not validated)

If a user attempts to Jump to OP \<JO\> from an eR<sub>X</sub> record that is not a fillable prescription, an error message is received stating, “Jumping can only be done on ‘NewRx’ messages, Renewal Response-Replace and fillable RxChange Response messages”.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/003.png)

JO Action Selected (Invalid Record Type)

Once the user has completed reviewing on the Outpatient side, upon selecting \<Enter\> at the “Select Patient:” prompt, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/004.png)

JO “Select Patient” – Jump Back to Holding Queue eR<sub>X</sub> Summary/Details Screen

#### UX – Un-Process eRx

The Un-Process (UX) hidden action has been added to the eRx Holding Queue Display screen. This action allows the user to Un-Process an eRx order that has been accepted in the eRx Holding Queue \[PSO ERX QUEUE PROCESSING\] and finished in Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]. The following checks are in place to Un-Process an eRx:

- The eRx status for the order must be Processed (PR), RXRENEWAL Response Processed (RXP), or RXCHANGE Response Processed (CXP).
- The user must hold the “PSDRPH” key.
- Only message types NEWRX (N), RXRENEWALRESPONSE (RE) and RXCHANGERESPONSE (CX) can be unprocessed. 
- If message type is RXRENEWALRESPONSE, it must have a Response Value of ‘REPLACE’.
- Must be original fill and not transmitted to CMOP.
- The prescription status must be SUSPENDED or HOLD.

To Un-Process an eRx from the Holding Queue:

1.  From the eRx Holding Queue Display screen, type \<UX\> Un-Process eRx.
2.  Type Additional Comments or accept the default comments and press \<Enter\>.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Holding Queue Display</strong> Nov 01, 2023@15:14:01 Page: 1 of 3</u></p>
<p>eRx Patient: XXXXX,XXXXXXXXXX</p>
<p>eRx Reference #: 999999999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>NEWRX</p>
<p>eRx Status:</p>
<p>eRx Patient: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>Vista Patient[v]: XXXXX,XXXXXXXXXX DOB: 4/21/90</p>
<p>eRx Provider: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>Vista Provider[v]: PROVIDER,ONE</p>
<p>DEA#: XX1234567 NPI: 1234567890</p>
<p>eRx Drug: DIPHENHYDRAMINE HCL 2% CREAM</p>
<p>eRx Qty: 180 eRx Refills: 2 eRx Days Supply: 30</p>
<p>eRx Written Date: OCT 22, 2023 eRx Issue Date:</p>
<p>Prohibit Renewals: No</p>
<p>+ Enter ?? for more actions</p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>P Print RJ (Reject) AC (Accept eRx)</p>
<p>H (Hold) UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// UX UX</p>
<p>Comments: Un-Process for correction Replace</p>
<p>Would you like to 'Un-Process' eRx #33004422 and Rx #2299503? Y// ES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Process an eRx

#### PN – Patient Progress Note

A shortcut to the existing hidden action PN – Progress Note (OP) in the Backdoor Pharmacy was added to the eRx Holding queue so that the user could enter a Progress Note for the VistA patient before accepting the eRx. In order to use this action the VistA patient must have been matched and validated. For more information on Progress Notes, please refer to the Outpatient Pharmacy User Manual in the Veteran's Documentation Library (VDL).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>eRx Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>Vista Provider: XXXXXXXXXXXX,XXXXX MD</p>
<p>DEA#: XX9999999 NPI:</p>
<p>eRx Drug: LORAZEPAM 1MG TAB</p>
<p>eRx Qty: 45 eRx Refills: 5 eRx Days Supply: 30</p>
<p>eRx Written Date: AUG 03, 2023 eRx Issue Date:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen PS Print Screen HL View History Log</p>
<p>- Previous Screen PL Print List EC eRx Change Request</p>
<p>UP Up a Line SL Search List PA Patient Allergies</p>
<p>DN Down a Line ADPL Auto Display(On/Off) UR Un Remove eRx</p>
<p>FS First Screen Q Quit JO Jump to OP</p>
<p>LS Last Screen AD Add Comment UX Un Process eRx</p>
<p>GO Go to Page ACK Acknowledge PN Patient Progress Note</p>
<p>RD Re Display Screen SH Status History AU View Audit Log</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### AU – View Audit Log

View Audit Log \<AU\> hidden action is used to view all edits made to a VistA Patient, Provider, and Drug/Sig. This feature will also capture any edits made by auto-matching and display them on the Audit Log.

Once the user selects View Audit Log \<AU\>, the Audit Log report will display.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/005.png) eRx Audit Log

Users are able to sort the Audit Log by Date/Time \<DT\>, Field \<FN\>, Edited By \<EB\>, or Show/Hide eRx Value \<SH\>. All sort options contain a sort indicator to inform the user if the results are in ascending \[^\] or descending \[v\] order. To change the chronological order of the Audit Log display, enter the sort option a second time.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/006.png)

eRx Audit Log Sorted by Date/Time Ascending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/007.png)

eR<sub>X</sub> Audit Log Sorted by Date/Time Descending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/008.png)

eR<sub>X</sub> Audit Log Sorted by Edited By Ascending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/009.png)

eR<sub>X</sub> Audit Log Sorted by Edited By Descending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/010.png)

eR<sub>X</sub> Audit Log Sorted by Field Ascending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/011.png) eR<sub>X</sub> Audit Log Sorted by Field Descending

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/012.png)

eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Shown

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/013.png)

eR<sub>X</sub> Audit Log Sorted by Show/Hide eRx Value - Hidden

To exit the Audit Log \<AU\> and return to the eRx Holding Queue Display, press ‘Enter’.

#### Patient-Level Record Lock

Note that when either the Summary/Details screen or any of the validate screens of an eR<sub>X</sub> are open, all the eR<sub>X</sub> for that same patient in the Holding Queue are locked and inaccessible for other users to access until the lock is released (the screens are closed). This is referred to as a patient-level record lock.

The following message displays if a user attempts to access an eR<sub>X</sub> for the same patient that another user has opened.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/014.png)

Patient-Level Record Lock

#### Prohibit Renewals

The Prohibit Renewal Request flag is used to denote that a RxRenewal Request should not be sent to the sending prescriber for an original NewRx or a subsequent fillable RxChange Response when the flag is set on the original NewRx. This is usually used when the visit is for a one time prescription (i.e., Urgent Care Center or Emergency Department).

> **NOTE:** \(i\) The Prohibit Renewal Request information is not displayed for RxRenewal Request and Response records.

\(ii\) The Prohibit Renewal Request information is displayed both in VistA and on web GUI under Track/Audit details screen, whenever it is sent on the inbound NewRx record.

![](inbound-eprescribing-user-manual-unit-1-pso-7-700/015.png)

Prohibit Renewal Request

### From: Inbound ePrescribing User Manual (Unit 7 Part 2) PSO*7*746

## Purpose of eR<sub>X</sub> Matching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the most important features of the eR<sub>X</sub> Holding Queue is the matching of the outside information sent by the prescriber to corresponding VistA records so that an Outpatient VistA prescription can be created. For the fillable prescriptions, VA Pharmacy users can validate patient, provider, and drug/SIG information.

## Reverse Vs. Highlight Video

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The reverse video feature is being utilized in this new option as a mechanism to alert users of a discrepancy between two equivalent fields, one value being received from the outside prescriber in comparison to the equivalent VistA field value.

For more information on terminal display settings, please refer to the VistA Patch \# PSO\*7.0\*700 Release Notes in the Veteran's Documentation Library (VDL).

There are some important rules and exceptions when comparing the two fields:

1.  If the VistA record has not been matched yet, the reverse video will not apply, as seen on the example below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>SSN : <strong>999999999</strong> |SSN :</p>
<p>Sex : <strong>MALE</strong> |Sex :</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> |</p>
<p><strong>XXXXXXXX,XX 99999</strong> |</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Lowercase and Uppercase discrepancies are ignored:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|</p>
<p>Name: <strong>Xxxx,Xxxxxxxxxxx</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Special characters, including blank spaces are ignored:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><em><u>Example 1:</u></em></p>
<p>|</p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>|</p>
<p><em><u>Example 2:</u></em></p>
<p>|</p>
<p>Phone: (<strong>999) 999-9999</strong> |SSN : <strong>9999999999</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Dates formatted differently are ignored:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|</p>
<p>DOB : <strong>Xxx 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Only the first 5 digits of a Zip Code is compared:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999-9999</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

6.  If either a non-numeric text on the left or on the right contains the other side text, it is ignored as well (exception: MALE & FEMALE):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><em><u>Example 1:</u></em></p>
<p>|</p>
<p>Name: <strong>XXXXX,XXXXXXXXXX XXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Sex : <strong><mark>MALE</mark></strong> |Sex : <strong><mark>FEMALE</mark></strong></p>
<p>|</p>
<p><em><u>Example 2:</u></em></p>
<p>|</p>
<p><strong>1234 ERX TEST ST</strong> | <strong>1234 ERX TEST STREET</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999-9999</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  In the case of phone numbers, if the same number is found on different fields (e.g., Cell Phone for one record and Home Number for another) it is ignored as well:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|</p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: <strong>(999) 999-9999</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Allergy information comparison is performed the following way:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><em><u>Example 1:</u></em></p>
<p>_____________________________________________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> | <strong>NO ALLERGY ASSESSMENT</strong></p>
<p>_____________________________________________________________________________</p>
<p><em><u>Example 2:</u></em></p>
<p>_____________________________________________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong><mark>NO ALLERGY INFORMATION RECEIVED</mark></strong> | <strong><mark>NO KNOWN ALLERGIES</mark></strong></p>
<p>_____________________________________________________________________________</p>
<p><em><u>Example 3:</u></em></p>
<p>_____________________________________________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>HONEY BEE STINGS</strong>,<strong>LATEX GLOVES,PEANUTS</strong> | <u>Verified:</u></p>
<p><strong><mark>TOMATO</mark>,ZOLPIDEM</strong> | <strong><mark>ABOLENE</mark></strong>,<strong><mark>ACEBUTOLOL</mark></strong>,<strong>HONEY BEE STINGS</strong></p>
<p>| <strong>LATEX GLOVES</strong>,<strong><mark>MOLD</mark></strong>,<strong><mark>POLLEN</mark>,PEANUTS</strong></p>
<p>| <strong><mark>TOMATO PRODUCTS</mark></strong>,<strong><mark>TYLENOL</mark>,ZOLPIDEM</strong></p>
<p>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

9.  Fields without a corresponding value on the other side will not reverse video:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><em><u>Example 1 (Patient Instructions):</u></em></p>
<p>_____________________________________________________________________________</p>
<p>|<u>3)</u>Patient Instructions:</p>
<p>| <strong>- IF SPLITTING TABLET, SPLIT JUST</strong></p>
<p>| <strong>PRIOR TO USE</strong></p>
<p>_____________________________________|______________________________________</p>
<p><em><u>Example 2 (Routing):</u></em></p>
<p>_____________________________________________________________________________</p>
<p>Days Supply: <strong><mark>30</mark></strong> Refills: <strong><mark>11</mark></strong> |<u>7)</u>Days Supply: <strong><mark>90</mark></strong> <u>8)</u>Refills: <strong><mark>3</mark></strong></p>
<p>_____________________________________|_______________________________________</p>
<p>|<u>9)</u>Routing: <strong>WINDOW</strong></p>
<p>_____________________________________|_______________________________________</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

10. Substitution field exception. Although there is no equivalent VistA value for this field, it will always reverse video if the value is NO to alert users that no substitution is allowed:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>_____________________________________________________________________________</p>
<p>Drug: <strong>MELOXICAM 15MG TAB</strong> |<u>1)</u>Drug: <strong>MELOXICAM 15MG TAB</strong></p>
<p>Substitution? <strong><mark>NO</mark></strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>_______________________________________|_____________________________</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

11. SIG field exception. Since the VistA SIG is automatically composed by the dosage fields along with the VistA patient instructions, it becomes extremely hard to match it letter-by-letter with the SIG sent in by the outside prescriber; therefore, the SIG field value will never reverse video:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>_____________________________________________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>Take 1 Tablet (40 mg total) by mouth</strong> | <strong>TAKE ONE TABLET BY MOUTH EVERY DAY</strong></p>
<p><strong>Once a day</strong> |</p>
<p>________________________________________|____________________________________</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

12. DEA EXP field exception. This DEA Expiration Date for the VistA Provider will display in reverse video when it is expired:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name: <strong>XXXXXXXX,XXXXXXX MD</strong> |Name: <strong>XXXXXXXX,XXXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong> DEA EXP: <strong><mark>99/99/99</mark></strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Accepting eR<sub>X</sub>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conditions must be met, before a fillable eR<sub>X</sub> can be accepted and transmitted to the Pending Queue for further processing:

1.  The eR<sub>X</sub> cannot be on Hold. If the eR<sub>X</sub> is on Hold, the eR<sub>X</sub> status on the Holding Queue List has one of the Hold Status codes, and the Hold Status, Hold Reason, and the user who placed the eR<sub>X</sub> on hold is displayed on the Summary/Details screen.
10. The eR<sub>X</sub> cannot have a status of “Rejected” RJ, “Removed” RM, “Processed” PR or “Canceled” CAN/CXQ.

All validation steps, for patient, provider, and drug/SIG must be completed, including the \<AV\> Accept Validation action on the validate screens. For additional information on the validation steps, refer to section User Manual Unit 1 available on the Veteran's Documentation Library (VDL).

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>When MbM users accept an eR<sub>X,</sub> the software will check if the Clinic they are currently logged on (the one they chose when entering the option) matches the clinic in the eR<sub>X</sub> (edited during Validate Drug/SIG). If they are different, MbM users will see the following message/prompt:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// AC Accept eRx</p>
<p>Current Clinic assigned to the eRx: ADMISSION MED</p>
<p>Send to eRx Clinic: EMERGENCY ROOM*//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>The default value will always be the clinic they are logged on. This will give them a chance to select/change the clinic they want to send the eR<sub>X</sub> to.</p></td>
</tr>
</tbody>
</table>

If a user attempts to accept an eR<sub>X</sub> where one or more of the conditions have not been met, an error message displays indicating that the eR<sub>X</sub> cannot be processed and the reason.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/039.png)

Accept eR<sub>X</sub> - Sample Validation Errors

After all the above preconditions have been met, to Accept an eR<sub>X</sub> \<AC\> from the Summary/Details screen, complete the following steps.

From the Summary/Details screen, type \<AC\> Accept eR<sub>X</sub>.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/040.png)

Accept eR<sub>X</sub>es

A message displays notifying the user that the eR<sub>X</sub> was sent to Pending Outpatient Orders for further processing.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/041.png)

eR<sub>X</sub>es Sent to Pending Outpatient Orders

The user can then go to Complete Orders from OERR or Patient Prescription Processing to view the eR<sub>X</sub> information.

Complete Orders from OERR and Patient Prescription Processing.

> **NOTE:** RxVerify messages are stored in the Hub for reporting purposes only. Unlike in the past, no NCPDP message will be sent back to the originating EHR system indicating that eR<sub>X</sub> has been accepted.

CS NOTE: All Controlled Substance prescriptions checks for Patient, Provider, and Drug are re-performed at Accept eRx and any issues will prevent the eRx from being accepted.

## Rejecting eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reject is used to remove a fillable eR<sub>X</sub> from the eR<sub>X</sub> Holding Queue. Reject must be accompanied by a reject code/reason.

> **NOTE:** Reject messages are stored in the Hub for reporting purposes only. Unlike in the past, no NCPDP message will be sent back to the originating EHR system indicating that eR<sub>X</sub> has been rejected.

To reject an eR<sub>X</sub>, complete the following steps:

1.  From the Summary/Details screen, type \<RJ\> Reject.
2.  Enter \<Y\> Yes to confirm the reject.
3.  Enter a reason for the rejection. The following reasons are available:
- PTT01 – Patient not eligible
- PTT02 – Cannot resolve patient
- PVD01 – Provider not eligible
- PVD02 – Cannot resolve provider
- DRU01 – Not eligible for renewals
- DRU02 – Non-formulary drug
- DRU03 – Duplicate prescription found for this patient
- DRU04 – Invalid quantity
- DRU05 – Duplicate therapeutic class
- DRU06 – Controlled substances are disallowed
- ERR01 – Multiple errors, please contact the pharmacy
- ERR02 – Incorrect pharmacy
- ERR03 – Issues with prescription, please contact the pharmacy
- PVD03 – Missing/bad digital signature on inbound CS ERX
- PVD04 – Prescriber’s CS credential is not appropriate
- PTT03 – Patient’s mailing address is missing/mismatched
- ERR99 - Other
4.  Type additional comments as to why the eR<sub>X</sub> is being rejected and press \<Enter\>. These comments are optional.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/042.png)

Rejecting an eR<sub>X</sub>

Once the eR<sub>X</sub> is rejected, the details of the reject message are available in the IEP Processing Hub as reference. Error! Reference source not found.![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/043.png)

Reject Message in Processing Hub

## Placing eR<sub>X</sub> on Hold in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fillable eR<sub>X</sub> can be placed on hold for several reasons indicating that there is an issue with the eR<sub>X</sub>.

1.  To place an eR<sub>X</sub> on hold, type \<H\> Hold from the Summary/Details screen or any of the validate screens.
2.  Enter a hold reason from the available reasons. The following reasons are available:
- HPT – PATIENT NOT FOUND
- HPD – PROVIDER NOT FOUND
- HNF – NON-FORMULARY DRUG THAT NEEDS APPROVAL
- HSO – INSUFFICIENT STOCK
- HDI – DRUG-DRUG INTERACTION
- HAD – ADVERSE DRUG INTERACTION
- HBA – BAD ADDRESS
- HPC – PROVIDER CONTACTED
- HPA – PRIOR APPROVAL NEEDED
- HOR – OTHER REASON
- HPP – PATIENT CONTACTED
- HPR – HOLD DUE TO PATIENT REQUEST
- HQY – QUANTITY OR REFILL ISSUE
- HCR – PRESCRIBER’S CS CREDENTIAL IS NOT APPROPRIATE
- HWR – CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS
- HIS – PROVIDER DEA# ISSUE
- HRX – HOLD FOR RX EDIT
- HDE – DRUG USE EVALUATION
- HTI – THERAPUTIC INTERCHANGE
- HAL – NO PATIENT ALLERGY ASSESSMENT
- HEL – PATIENT ELIGIBILITY ISSUE
- HUR – HOLD UN-REMOVED
- HFF – HOLD FOR FUTURE FILL

  To view the available hold reasons, enter a double question mark \<??\> at the “Select HOLD reason code” prompt. The available hold reasons display.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// H Hold</p>
<p>Select HOLD reason code: ??</p>
<p>Choose from:</p>
<p>118 HPT PATIENT NOT FOUND</p>
<p>119 HPD PROVIDER NOT FOUND</p>
<p>120 HNF NON-FORMULARY DRUG THAT NEEDS APPROVAL</p>
<p>121 HSO INSUFFICIENT STOCK</p>
<p>122 HDI DRUG-DRUG INTERACTION</p>
<p>123 HAD ADVERSE DRUG INTERACTION</p>
<p>124 HBA BAD ADDRESS</p>
<p>125 HPC PROVIDER CONTACTED</p>
<p>126 HPA PRIOR APPROVAL NEEDED</p>
<p>127 HOR OTHER REASON</p>
<p>128 HPP PATIENT CONTACTED</p>
<p>129 HPR HOLD DUE TO PATIENT REQUEST</p>
<p>130 HQY QUANTITY OR REFILL ISSUE</p>
<p>1618 HCR PRESCRIBER'S CS CREDENTIAL IS NOT APPROPRIATE</p>
<p>1619 HWR CS PRESCRIPTION WRITTEN/ISSUE DATE HAS PROBLEMS</p>
<p>1620 HIS PROVIDER DEA# ISSUE</p>
<p>1621 HRX HOLD FOR RX EDIT</p>
<p>1622 HDE DRUG USE EVALUATION</p>
<p>1623 HTI THERAPUTIC INTERCHANGE</p>
<p>1624 HSC SCRIPT CLARIFICATION</p>
<p>1625 HGS GENERIC SUBSTITUTION</p>
<p>1631 HAL NO PATIENT ALLERGY ASSESSMENT</p>
<p>1632 HEL ELIGIBILITY ISSUE</p>
<p>1633 HUR HOLD UNREMOVE</p>
<p>1644 HFF HOLD FOR FUTURE FILL</p>
<p>Select HOLD reason code:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold eR<sub>X</sub>

11. Enter the reason code at the “Select HOLD Reason code:” prompt and press \<Enter\>.
12. A prompt displays asking for additional comments on the reason for the hold. These comments are optional. Either press \<Enter\> to complete the hold process or add comments and then press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/046.png)

Select Hold Reason Code

The Hold Status, Hold Reason, and the user placing the eR<sub>X</sub> on hold display below the VistA Drug section on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/047.png)

Hold Status and Reason

The hold status also displays in the “Status” column (STA) on the Holding Queue List screen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Nov 11, 2023@11:57:59 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>45</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DAT<strong>^</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. XXXXXXXXXX,XXXXXXXXX 07/10/33 MELOXICAM 15MG TAB XXXXX,XXXXX I 10/04/23</p>
<p>2. XXXXXXXXXX,XXXXXXXXX 04/26/80 ACETAMINOPHEN 325MG T XXXXX,XXXXX N 10/04/23</p>
<p>3] XXXXXXXXXX,XXXXXXXXX 09/22/63 PHENOBARBITAL 32MG TA XXXXX,XXXXX N 10/04/23</p>
<p>4] XXXXXXXXXX,XXXXXXXXX 07/30/48 AZITHROMYCIN 250MG TA XXXXX,XXXXX I 10/04/23</p>
<p>5] XXXXXXXXXX,XXXXXXXXX 07/10/33 DIAZEPAM 2MG TAB XXXXX,XXXXX I 10/04/23</p>
<p>6. XXXXXXXXXX,XXXXXXXXX 08/01/62 NAPROXEN 250MG TAB XXXXX,XXXXX N 10/04/23</p>
<p>7] XXXXXXXXXX,XXXXXXXXX 04/20/80 ALPRAZOLAM 0.5MG TAB XXXXX,XXXXX HAL 10/04/23</p>
<p>8] XXXXXXXXXX,XXXXXXXXX 05/13/53 AZITHROMYCIN 250MG TA XXXXX,XXXXX N 10/04/23</p>
<p>9. XXXXXXXXXX,XXXXXXXXX 12/31/70 FORMOTEROL 5/MOMETASO XXXXX,XXXXX N 10/04/23</p>
<p>10. XXXXXXXXXX,XXXXXXXXX 10/01/23 SALMETEROL 50MCG/BLST XXXXX,XXXXX HEL 10/04/23</p>
<p>11] XXXXXXXXXX,XXXXXXXXX 10/08/67 DIAZEPAM 5MG/ML 2ML I XXXXX,XXXXX HSO 10/04/23</p>
<p>12. XXXXXXXXXX,XXXXXXXXX 03/16/42 OMEPRAZOLE 20MG EC CA XXXXX,XXXXX N 10/04/23</p>
<p>13. XXXXXXXXXX,XXXXXXXXX 01/25/43 CIPROFLOXACIN HCL 500 XXXXX,XXXXX I 10/04/23</p>
<p>14. XXXXXXXXXX,XXXXXXXXX 10/05/44 COLON ELECTROLYTE LAV XXXXX,XXXXX N 10/04/23</p>
<p>15] XXXXXXXXXX,XXXXXXXXX 03/16/42 CEPHALEXIN 250MG CAP XXXXX,XXXXX N 10/04/23</p>
<p>16] XXXXXXXXXX,XXXXXXXXX 12/21/48 SORBITOL 70% SOLN XXXXX,XXXXX N 10/04/23</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Hold Status in Status Column

> **NOTE:** When a fillable eR<sub>X</sub> is put on ‘Hold’ the only actions available for the user are UH/Un Hold, P/Print and SH/Status History.

### Future Fill Hold (HFF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Future Fill Hold (HFF) works slightly different from other Hold codes. When the user selects the HFF for the Hold Code the software will prompt the user to enter a Future Fill Hold Date, if the eRx has a future Effective Date, the software will use the date as a default value. Once the user enters this date and completes the holding of the eRx, the software will start checking on a daily basis if the date entered is the current day, if it is the software will automatically un-hold the eRx and place it in an IN-PROCESS status.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// H Hold</p>
<p>Select HOLD reason code: HFF HOLD FOR FUTURE FILL</p>
<p><strong>The eRx will be un-held automatically on the date you enter below and placed</strong></p>
<p><strong>in 'IN PROCESS' status.</strong></p>
<p>Future Fill Hold Date: 07/10/24//</p>
<p>Additional Comments (Optional): Not to be filled until July 10</p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Once the eRx is automatically un-held, the Status History Log will track the action indicating it was automatically un-held by the PSOAPPLICATIONPROXY,PSO user.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Action:Next Screen// SH SH</p>
<p>---------------------------------------------------------------------------</p>
<p>06/14/24@16:23:31 I IN PROCESS</p>
<p>Entered By: TEST,USER</p>
<p>Comments:</p>
<p>06/15/24@10:55:24 HFF HOLD FOR FUTURE FILL (JUL 10, 2024)</p>
<p>Entered By: TEST,USER</p>
<p>Comments: Not to be filled until July 10th</p>
<p>07/10/24@06:56:25 I IN PROCESS</p>
<p>Entered By: PSOAPPLICATIONPROXY,PSO</p>
<p>Comments: Future Fill Automatically Un-Held</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** HFF holds can be un-held manually at any time by the user.

## Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fillable eR<sub>X</sub> can be removed from the Holding Queue without sending a message back to the originating external provider. Sample scenarios include, but are not limited to, the patient requested that the eR<sub>X</sub> not be filled, or the user has been unable to contact the provider or patient for a significant amount of time.

To remove an eR<sub>X</sub> from the Holding Queue:

1.  From the Summary/Details screen, type \<RM\> Remove.
2.  Enter a reason for the eR<sub>X</sub> removal. The following removal reasons are available:
- REM01 - Drug out of stock or on backorder and unavailable for processing
- REM02 - Patient was not able to pick up
- REM03 - Prescription canceled by Provider
- REM04 - Prescription processed manually
- REM05 - Provider will cancel this eR<sub>X</sub> and submit another
- REM06 - Unable to mail prescription and patient unable to pick up
- REM07 - Unable to contact patient
- REM08 - Unable to contact provider
- REM91 - Undefined system error
- REM92 – Other
- REM09 – ERX Issue not resolved - Provider contacted
1.  Type additional comments as to why the eR<sub>X</sub> is being removed and press \<Enter\>. These comments are optional.

Once the eR<sub>X</sub> is removed, the status changes to “RM” and it no longer displays in the default Holding Queue List; however, the eR<sub>X</sub> can be accessed via the search action from the main Holding Queue List screen using one or more of the search criteria.

![](inbound-eprescribing-user-manual-unit-7-part-2-pso-7-746/049.png)

Removing an eR<sub>X</sub>

> **NOTE:** If the Remove function is in parentheses “()”, the user is not able to remove an eR<sub>X</sub>. If the action is still attempted, the user receives a message that the action is not available.

### Batch Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user completes removing one eRx for the patient, the software checks whether the patient has other eRx records received on the same date from the same provider. If it does, the software will prompt or ask the user to remove these eRx’s with the same reason and comments (if there are any, comments are optional) entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the</p>
<p>same day:</p>
<p>PROVIDER: PROVIDER,PROVIDERNAME eRx RECEIVED DATE: FEB 07, 2024@11:11:54</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>--------------------------------------------------------------------------12345678901235 ASPIRIN 325MG EC TAB PROVIDER,PROVIDERNAME HUR</p>
<p>12345678901237 LISINOPRIL 20MG TAB PROVIDER,PROVIDERNAME HUR</p>
<p>12345678901238 NAPROXEN 500MG TAB PROVIDER,PROVIDERNAME HUR</p>
<p>Do you want to 'Remove' them - REM02? No// <strong>YES</strong></p>
<p>Updating...done.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Remove

## Un Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible after a fillable eRx is Removed, it needs to be moved back to the Holding Queue to be processed. Users can utilize the Include All Statuses (IAS) action on the Single Patient Queue screen or use the Rx List View action on the eRx Patient Centric Queue screen, then use the Search Queue (SQ) action to search for the eRx with a Removed status (ERX STATUS). Once the Removed eRx is selected, the user can utilize the Un-Remove (UR) hidden action on the Single eRx View/Display screen. This action will allow users to Un-Remove an eRx that was previously Removed, so the eRx will display again on the eRx Single Patient Queue screen to be worked.

To Un-Remove an eRx from the Holding Queue:

1.  From the Single eRx View/Display screen, type \<UR\> Un-Remove eRx.
2.  Enter a HOLD reason code for the eRx Un-Removal.

> NOTE: A default value of HUR (HOLD UNREMOVE) will display and can be selected.

3.  Type Additional Comments as to why the eRx is being Un-Removed and press \<Enter\>.

These comments are optional.

> **NOTE:** Only eRxs with a REMOVED status can be UN-REMOVED.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 11, 2024@10:49:07 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXX</strong> eRx Reference #: <strong>369258</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/06/24</strong></p>
<p>eRx Status: <strong>REM02 - Patient was not able to pick up</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:34:58</td>
</tr>
</tbody>
</table>
<p>Name: <strong>XXXXXXXXX,XXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXX</strong></p>
<p>DOB : <strong>XXX 99,9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>Home Phone: |Home Phone: 555-2222</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:42:35</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>YYYYY,YYYYYY</strong> |Name: <strong>YYYYY,YYYYYY</strong></p>
<p>NPI : 1234567890 |NPI :</p>
<p>DEA : |DEA :</p>
<p>Clinic: <strong>TEST NAME</strong> |</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG MANUALLY-MATCHED | VALIDATED by USER,USER on 3/6/24@10:46:07</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: IBUPROFEN |Drug: IBERET-FOLIC-500 TAB</p>
<p>Substitution? Renewals? <strong>YES</strong> |</p>
<p>SIG: |SIG:</p>
<p><strong>ONE TABLET EVERY 4-6 HOURS AS NEEDED</strong> | <strong>TAKE TESTING BY MOUTH 4H FOR 4 HOURS</strong></p>
<p>|</p>
<p><strong>. . .</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 10/18/23@11:18</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>P Print RJ Reject AC Accept eRx</p>
<p>H Hold UH Un Hold RM Remove eRx</p>
<p>Select Action:Next Screen// UR UR</p>
<p>Select HOLD reason code: HUR// UN-REMOVED</p>
<p>Additional Comments (Optional): TESTING BATCH UN-REMOVED</p>
<p>Would you like to 'Un-Remove' eRx #369258? Y//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un-Remove an eRx

### Batch Un Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Similar to Batch eRx Remove, the Batch Un-Remove performs the opposite functionality. Once the user completes un-removing one eRx for the patient the software checks whether the patient has other eRx records received on the same date from the same Provider that have also been put on Remove with the same Remove Code. If it does, the software will prompt or ask the user to un-remove these eRx’s with the same comments entered above.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The following prescriptions are from the same provider and received on the</p>
<p>same day:</p>
<p>PROVIDER: PROVIDER,PROVIDERNAME eRx RECEIVED DATE: MAR 06, 2024@16:43:21</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>-------------------------------------------------------------------------------</p>
<p>8456710 ACETAMINOPHEN 250MG/IBUPROFEN 125M PROVIDER,PROVIDERNAME REM02</p>
<p>6429103 VENETOCLAX 10MGX14/50MG X7/100 PROVIDER,PROVIDERNAME REM02</p>
<p>54123789 POUCH,DRAINABLE,SUR-FIT C#4164 PROVIDER,PROVIDERNAME REM02</p>
<p>6510348 BAG,URINARY DRAINAGE MERIT #MD PROVIDER,PROVIDERNAME REM02</p>
<p>Do you want to 'Un-Remove' them? No//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Un-Remove eRx

## eR<sub>X</sub> in the Backdoor Pharmacy Pending Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the eR<sub>X</sub> is accepted in the Holding Queue it moves to the Patient Medication Profile under the Pending Orders section, which is the same queue where CPRS outpatient pharmacy orders are sent to by the VA Providers after they sign them.

### Patient Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Medication Profile can be accessed through these two different options: *Complete Orders from OERR* \[PSO LMOE FINISH\] or *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\]. An eR<sub>X</sub> Pending Order or a finished prescription are marked by an ampersand (&) before the prescription number or drug name in the case of pending orders.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Medication Profile</strong> Nov 12, 2023@09:20:13 Page: 1 of 2</u></p>
<p>XXXXXXXXXXX,XXXXXXX &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 999.99 (99/99/9999)</p>
<p>DOB: XXX 99,9999 (99) Wt(kg): 99.99 (99/99/9999)</p>
<p>SEX: MALE</p>
<p>CrCL: 99.9(est.) (CREAT: 9.99mg/Dl 99/99/99) BSA (m2): 9.99</p>
<p><strong>ISSUE LAST REF DAY</strong></p>
<p><strong># RX # DRUG QTY ST DATE FILL REM SUP</strong></p>
<p><strong>________________________________________________________________________________</strong></p>
<p>-------------------------------------ACTIVE-------------------------------------</p>
<p>1 &amp; 2297959$ MELOXICAM 7.5MG TAB 30 A&gt; 08-09 08-16 11 30</p>
<p>2 2297948$ METFORMIN HCL 1000MG TAB 30 A&gt; 08-10 08-10 5 30</p>
<p>3 2297920$ NAPROXEN 250MG TAB 60 A&gt; 06-20 06-20 11 30</p>
<p>------------------------------------PENDING-------------------------------------</p>
<p>4 &amp; ATENOLOL 25MG TAB QTY: 60 ISDT: 09-18&gt; REF: 11</p>
<p>5 GABAPENTIN 100MG CAP QTY: 30 ISDT: 08-09&gt; REF: 11</p>
<p>6 LEVOTHYROXINE (LEVOTHROID) 0.125MG TAB</p>
<p>QTY: 30 ISDT: 08-10 REF: 5</p>
<p>7 &amp; LOSARTAN 25MG TAB QTY: 60 ISDT: 09-20&gt; REF: 11</p>
<p>8 &amp; MELOXICAM 15MG TAB QTY: 30 ISDT: 08-09&gt; REF: 11</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>PU Patient Record Update NO New Order</p>
<p>PI Patient Information SO Select Order</p>
<p>Select Action: Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Medication Profile

### eRx Pending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An eR<sub>X</sub> pending order will display similar to the split screen in the eR<sub>X</sub> Holding Queue for validating patient, provider, and drug/SIG, including the reverse video for discrepancies. The main difference is that it will contain all sections (patient, provider, and drug/SIG) in one screen, as seen below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Pending OP Orders (ROUTINE)</strong> Nov 12, 2023@09:18:09 Page: 1 of 1</u></p>
<p>XXXXXXXXX,XXXXXXX &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 999.99 (99/99/9999)</p>
<p>DOB: XXX 99,9999 (99) Wt(kg): 99.99 (99/99/9999)</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX (999999) | VISTA PENDING ORDER</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong><u>PATIENT AUTO-MATCHED/EDITED | VALIDATED by XXXXX,XXXXXXX on 9/20/23@11:47:15__</u></strong></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>SSN : <strong>999-99-9999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><mark>NO ALLERGY INFORMATION RECEIVED</mark> | Verified:</p>
<p>| <mark>ALBUTEROL</mark>,<mark>EGG PRODUCTS</mark>,<mark>HONEY</mark></p>
<p>| <mark>IBUPROFEN</mark>,<mark>PEANUTS</mark>,<mark>PERCODAN</mark></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>PROVIDER AUTO-MATCHED | VALIDATED by PSOAPPLICATIONPROXY on 9/20/23@11:44:29</u></strong></p>
<p>Name: <strong>XXXXXXXX,XXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>DRUG AUTO-MATCHED | VALIDATED by XXXXX,XXXXXXX on 9/20/23@11:48:05</u></strong></p>
<p>Substitution? <strong>NO</strong> |<u>1)</u> Orderable Item: &lt;DIN&gt;</p>
<p>Renewals? <strong>YES</strong> | <strong>ATENOLOL TAB</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Drug: |<u>2)</u> CMOP Drug: &lt;DIN&gt;</p>
<p><strong>Tylenol 250mg tablet</strong> | <strong>TYLENOL 250MG TAB</strong></p>
<p>Drug Form: <strong>Tablet</strong> |Drug Message:</p>
<p>| <strong>NATL FORM * TCGRx &amp; SCRIPTPRO *</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE 1 TABLET QD</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Prescriber Drug Use Evaluation: |3) Dosage: 250 (MG)</p>
<p>Co-Agent: Ibuprofen | Verb: TAKE</p>
<p>Reason: Drug-Allergy |Disp. Units: 1</p>
<p>Result: Prescribed w/ acknowledgements | Noun: TABLET</p>
<p>Acknowledgement: Previously Tolerated | Route: ORAL</p>
<p>...................................... | Schedule: BID-WITH FOOD</p>
<p>Co-Agent: Nsaids (Non-Steroidal Anti-In|__________________________________</p>
<p>flammatory Drug) |4)Patient Instructions:</p>
<p>Reason: Drug-Allergy |</p>
<p>Result: Prescribed w/ acknowledgements |</p>
<p>Acknowledgement: Previously Tolerated |</p>
<p>_______________________________________|________________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>|<u>5)</u> Pat.Status: <strong>SERVICE CONNECTED</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Date Written: <strong>SEP 18, 2023</strong> |<u>6)</u> Issue Date: <strong>SEP 18,2023</strong></p>
<p>Effective Date: |<u>7)</u> Fill Date: <strong>Nov 12, 2023</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Days Supply: <mark>30</mark> |<u>8)</u> Days Supply: <mark>90</mark></p>
<p>_______________________________________|________________________________________</p>
<p>Quantity: <mark>30</mark> |<u>9)</u> QTY (TAB): <mark>90</mark></p>
<p>Dispense Unit: |</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Refills: <mark>11</mark> |<u>10)</u> Refills: <mark>3</mark></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>11)</u> Routing: <strong>MAIL</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>12)</u> Clinic: <strong>CC</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Provider: <strong>XXXXXXXX,XXXXXX</strong> |<u>13)</u> Provider: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>14)</u> Copies: <strong>1</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>15)</u> Remarks:</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 9/20/23@11:44 | Accepted by XXXXXX,XXXXXXX on 9/26/23@10:30</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>AC Accept DC Discontinue FL Flag/Unflag</p>
<p>BY Bypass ED Edit</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>MbM Only</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>If the VistA patient is not eligible for ChampVA benefits the message “PATIENT NOT ELIGIBLE” will blink on the header section of the pending order:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Pending OP Orders (ROUTINE)</strong> Nov 12, 2023@09:18:09 Page: 1 of 1</u></p>
<p>XXXXXXXXX,XXXXXXX <strong>PATIENT NOT ELIGIBLE</strong> &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 999.99 (99/99/9999)</p>
<p>DOB: XXX 99,9999 (99) Wt(kg): 99.99 (99/99/9999)</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX (999999) | VISTA PENDING ORDER</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Renewal eRx Pending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An eR<sub>X</sub> renewal pending order will display slightly different than a regular eR<sub>X</sub>, which is in line with how these two types of orders display for CPRS orders. See the differences highlighted below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Prescription Renew</strong> Nov 12, 2023@09:18:09 Page: 1 of 1</u></p>
<p>XXXXXXXXX,XXXXXXX &lt;A&gt;</p>
<p>PID: 999-99-9999 Ht(cm): 999.99 (99/99/9999)</p>
<p>DOB: XXX 99,9999 (99) Wt(kg): 99.99 (99/99/9999)</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX (999999) | VISTA PENDING ORDER</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><strong><u>PATIENT PREVIOUSLY MATCHED/VALIDATED (RENEWAL)</u>_______________</strong></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99,9999</strong></p>
<p>SSN : <strong>999-99-9999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><mark>NO ALLERGY INFORMATION RECEIVED</mark> | Verified:</p>
<p>| <mark>ALBUTEROL</mark>,<mark>EGG PRODUCTS</mark>,<mark>HONEY</mark></p>
<p>| <mark>IBUPROFEN</mark>,<mark>PEANUTS</mark>,<mark>PERCODAN</mark></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>PROVIDER PREVIOUSLY MATCHED/VALIDATED (RENEWAL)</u>___________</strong></p>
<p>Name: <strong>XXXXXXXX,XXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>DRUG PREVIOUSLY MATCHED/VALIDATED (RENEWAL)</u>_______________</strong></p>
<p>Substitution? <strong>NO</strong> |Orderable Item: &lt;DIN&gt;</p>
<p>Renewals? <strong>YES</strong> | <strong>ATENOLOL TAB</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Drug: |CMOP Drug: &lt;DIN&gt;</p>
<p><strong>Atenolol 25mg tablet</strong> | <strong>ATENOLOL 25MG TAB</strong></p>
<p>Drug Form: <strong>Tablet</strong> |Drug Message:</p>
<p>| <strong>NATL FORM * TCGRx &amp; SCRIPTPRO *</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE 1 TABLET QD</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Prescriber Drug Use Evaluation: | *Dosage: <strong>25 (MG)</strong></p>
<p><strong>None</strong> | Verb: <strong>TAKE</strong></p>
<p>| Disp. Units: <strong>1</strong></p>
<p>| Noun: <strong>TABLET</strong></p>
<p>| *Route: <strong>ORAL</strong></p>
<p>| *Schedule: <strong>ONCE DAILY</strong></p>
<p>|________________________________________</p>
<p>|Patient Instruction:</p>
<p>_______________________________________|________________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>|Pat.Status: <strong>SERVICE CONNECTED</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Date Written: <strong>SEP 18, 2023</strong> |<u>1)</u> Issue Date: <strong>SEP 18,2023</strong></p>
<p>Effective Date: |<u>2)</u> Fill Date: <strong>Nov 12, 2023</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Days Supply: <mark>30</mark> |Days Supply: <mark>90</mark></p>
<p>_______________________________________|________________________________________</p>
<p>Quantity: <mark>30</mark> |QTY (TAB): <mark>90</mark></p>
<p>Dispense Unit: |</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Refills: <mark>10</mark> <strong>(Renewal)</strong>0 |<u>3)</u> Refills: <mark>3</mark></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>4)</u> Routing: <strong>MAIL</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>5)</u> Clinic: <strong>CC</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Provider: <strong>XXXXXXXX,XXXXXX</strong> |<u>6)</u> Provider: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>7)</u> Copies: <strong>1</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>8)</u> Remarks:</p>
<p>| <strong>RENEWED FROM RX # 999999999</strong></p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 9/20/23@11:44 | Accepted by XXXXXX,XXXXXXX on 9/26/23@10:30</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>AC Accept DC Discontinue FL Flag/Unflag</p>
<p>BY Bypass ED Edit</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The main differences indicated above are:

- Header will display Prescription Renew instead of Pending OP Orders (ROUTINE)
- Some eR<sub>X</sub> renewals pass through the eR<sub>X</sub> Holding Queue and go straight to the Pending Order and that is why there will be no information about the patient, provider, and drug matching/validation.
- The number of Refills will be reduced by one and the note (Renewal) will display beside it on the eR<sub>X</sub> side (left).
- The field numbers will change completely for an eR<sub>X</sub> Pending Renewal. This is because a reduced number of fields are editable for a renewal compared to regular pending order. This is also in line with a CPRS Pending Renewal.

### eRx Pending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A note "eRx Meds on File" will display in the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option header when the patient has at least one 'actionable' eRx in the eRx Holding Queue, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patient Information May 02, 2024@17:19:54 Page: 1 of 2 TEST,PATIENT</p>
<p>PID: 999-99-9999 Ht(cm): _______ (______)</p>
<p>DOB: XXX 99,9999 (99) Wt(kg): _______ (______)</p>
<p>SEX: MALE <strong><u>eRx Meds on File</u></strong></p>
<p>CrCL: &lt;Not Found&gt; (CREAT: Not Found) BSA (m2): _______</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Jump to eRx Patient from Backdoor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can jump to eRx Single Patient Queue from the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option. It will be available in the Patient Information screen as well as in the Medication Profile screen. The option will work independently if the patient has actionable eRx or not. However, the patient must have had at least one eRx received in the past.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Medication Profile</strong> Jun 29, 2024@08:55:32 Page: 1 of 1</u></p>
<p>TEST,PATIENT</p>
<p>PID: 999-99-9999 Ht(cm): _______ (______)</p>
<p>DOB: XXX 9,9999 (99) Wt(kg): _______ (______)</p>
<p>SEX: MALE <strong><u>eRx Meds on File</u></strong></p>
<p>CrCL: &lt;Not Found&gt; (CREAT: Not Found) BSA (m2): _______</p>
<p><strong>ISSUE LAST REF DAY</strong></p>
<p><strong># RX # DRUG QTY ST DATE FILL REM SUP</strong></p>
<p>----------------------------------PENDING----------------------------------</p>
<p>1 &amp; ASCORBIC ACID 250MG TAB QTY: 1 ISDT: 09-11 REF: 0</p>
<p>2 &amp; FAMOTIDINE 20MG TAB QTY: 60 ISDT: 10-07 REF: 0</p>
<p>3 GRISEOFULVIN 500MG S.T. QTY: 3 ISDT: 05-17 REF: 3</p>
<p>4 INSULIN NPH U-100 INJ (PORK) QTY: 100000 ISDT: 04-19 REF: 11</p>
<p>5 L-ASPARGINASE INJ,10,000U/VIAL QTY: 2 ISDT: 05-20 REF: 2</p>
<p>6 &amp; NAPROXEN 250MG S.T. QTY: 10 ISDT: REF: 5</p>
<p>7 PREDNISONE 1MG TAB QTY: 30 ISDT: 04-27 REF: 0</p>
<p>8 &amp; VITAMIN E 200 IU CAP QTY: 33 ISDT: 05-02 REF: 0</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>PU Patient Record Update NO New Order</p>
<p>PI Patient Information SO Select Order</p>
<p>Select Action: Quit// ??</p>
<p>The following actions are also available:</p>
<p>RP Reprint (OP) DN Down a Line QU Quit</p>
<p>RN Renew (OP) RD Re Display Screen LS Last Screen</p>
<p>DC Discontinue (OP) PT Print List FS First Screen</p>
<p>RL Release (OP) PS Print Screen GO Go to Page</p>
<p>RF Refill (OP) &gt; Shift View to Right + Next Screen</p>
<p>PP Pull Rx (OP) &lt; Shift View to Left - Previous Screen</p>
<p>IP Inpat. Profile (OP) SL Search List ADPL Auto Display</p>
<p>RS Reprint Sig Log RDD Fill/Rel Date Disply CK Check Interactions</p>
<p>CM Manual Queue to CMOP DR Display Remote IN Intervention Menu</p>
<p>OTH PSO ERX <strong>JE Jump to eRx Patient</strong> UP Up a Line</p>
<p>Select Action: Quit// <strong>JE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> Jun 29, 2024@09:00:17 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>TEST,PATIENT</strong> SEX: <strong>M</strong> DOB: <strong>99/99/99</strong> <strong>(99)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> <mark>MATCHING</mark></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong>^</strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 369258 IBUPROFEN 800MG TAB TEST,PROVIDER 06/18/24 I MV MV MV</p>
<p>2. 369261 ALBUTEROL INHALER TEST,PROVIDER 06/18/24 HAL</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the entry # to view or ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>DET Show/Hide Details IAS Include All Statuses LBD Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### From: Inbound ePrescribing User Manual (Unit 1 & Unit 2) PSO*7*581

## Organization of the Inbound ePrescribing User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE IEP user guide is comprised of the following sections:

- [Unit 1 – Introduction to Inbound ePrescribing](#introduction-to-inbound-eprescribing): Discusses general PRE Inbound ePrescribing information.
- <u>Unit 2 - Inbound ePrescribing Web-Based Application</u>: Outlines the IEP web-based application and capabilities, including Pharmacy Management, Track/Audit, Reports, and User Management functions.
- [Unit 3 – Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#_VistA_OP_eRx): Discusses the Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy (OP) electronic prescriptions (eR<sub>X</sub>) Holding Queue and capabilities, including eR<sub>X</sub> validation, search, sort, hold, acceptance, remove, and rejection.
- <u>Unit 4 – Error! Reference source not found.</u>: Discusses the RxRenewal Requests and Responses. The RxRenewal Requests function is used by pharmacists to generate and send an outbound RxRenewal Request. After a RxRenewal Request is sent to the external provider, the provider can send a RxRenewal Response back to the requesting Pharmacy.
- <u>Error! Reference source not found. – Error! Reference source not found.</u>: Discusses the RxChange Requests and Responses. The RxChange Requests function is used by pharmacists to generate and send an outbound RxChange Request. After a RxChange Request has been sent to the external provider, the provider is able to send a RxRenewal Response back to the requesting Pharmacy.
- <u>Error! Reference source not found. – Error! Reference source not found.</u>: Discusses the CancelRx Request and Response. The CancelRx Request is sent by the external/non-VA Provider for an original NewRx, so it is not processed and dispensed by VA Pharmacy. Upon successfully canceling a NewRx, the VA Pharmacy sends back a CancelRx Response.

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/002.png)

<span id="_Toc56760875" class="anchor"></span>Figure 1‑1: Inbound ePrescribing Web-based Application

The IEP web-based application is discussed in more detail in [Unit 2 - Inbound ePrescribing Web-Based Application](\l).

#### Inbound eR<sub>X</sub> VistA Outpatient Pharmacy

The Inbound eR<sub>X</sub> VistA Outpatient Pharmacy display screens include VistA screens that are used by VA Pharmacists and Technicians to validate and process eR<sub>X</sub>es.

The eR<sub>X</sub> Holding Queue is discussed in more detail in [Unit 3 - Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#_VistA_OP_eRx).

<span id="_Fillable_Prescriptions" class="anchor"></span>

### Fillable Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A “fillable prescription” is any inbound prescription with medication information, sent by an external or non-VA provider, which includes one of the following National Council for Prescription Drug Programs (NCPDP) 2017071 XML messages:

- NewRx Message
- RxRenewal Response Message - Replace response type
- RxChange Response Message - Approved response type for request types Generic Substitution, Therapeutic Interchange/Substitution, Drug Use Evaluation, Script Clarification and Out of Stock
- RxChange Response Message - Approved with Changes (AwC) response type for request types Generic Substitution, Therapeutic Interchange/Substitution, Drug Use Evaluation, Script Clarification and Out of Stock.
- RxChange Response Message - Validated response type for request type Prescriber Authorization

> **NOTE:** According to NCPDP 2017071, RxRenewal Response Approved and Approved with Changes types are also treated as fillable prescriptions. But the workflows for these are different than the above mentioned inbound message types. Throughout the guide, the term “fillable” is used for the above mentioned inbound message types only.

### Inbound ePrescribing Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IEP workflow is illustrated in the figure and described below.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/003.png)

<span id="_Toc56760876" class="anchor"></span>Figure 1‑2: Process Inbound ePrescribing Flow

1.  eR<sub>X</sub>es are sent from an external provider to SureScripts and/or Change Healthcare (CH). CH provides commercial ePrescribing solutions and, for the purposes of the IEP implementation, serves as a gateway to all participating ePrescribing providers nationwide.
2.  CH verifies and transmits eR<sub>X</sub> transactions to/from SureScripts and/or an external provider’s EHR system and the IEP system.
3.  The eR<sub>X</sub>es are routed from CH to the IEP Processing Hub via the Data Access Service (DAS) external gateway. DAS and CH communicate using https requests over a secured network.
4.  In the IEP Processing Hub, autochecks occur on the fillable prescriptions for Patient, Provider, and Drug/SIG. Refer to section <u>1.2.4</u> [Fillable Prescriptions](#_Fillable_Prescriptions) for the definition of fillable prescriptions. The Master Person Index (MPI) is used for patient checking, depending on the data set that is sent by the Prescriber for that patient. For patient Enrollment and Eligibility (E&E) checks, the Enrollment System (ES) is used. The ES assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with E&E data. The E&E check is optional and can be turned on or off for each site. Patient Registration is also confirmed against the instance of the receiving pharmacy.
5.  The Drug Name is matched against the local Drug File first, the VA Product Name next and then the National Drug Code (NDC), depending on which it matches first on. As a note, autochecks can be incorrect therefore the data must also be validated against the medication data sent for fillable prescriptions. Refer to section <u>Error! Reference source not found.Error! Reference source not found.</u> for more information.
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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/004.png)

<span id="_Toc56760877" class="anchor"></span>Figure 1‑3: Inbound ePrescribing Architecture

## Roles and Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IEP roles and tasks are described in this section as primary and secondary users. Primary users are VA Pharmacy Users. Secondary users include: System Administrators, VA Pharmacy Managers, VA PBM personnel, Non-VA Providers, and External Pharmacy personnel. The following sections provide an overview of primary and secondary user roles and their capabilities within IEP.

VA users have the capability of performing eR<sub>X</sub>-related tasks in the IEP web-based application and in the VistA OP eR<sub>X</sub> Holding Queue module. Specific tasks for each component are described in more detail in [Unit 2 - Inbound ePrescribing Web-Based Application](#inbound-eprescribing-web-based-application-overview) and  
[Unit 3 - Inbound eR<sub>X</sub> VistA Outpatient Pharmacy](#_VistA_OP_eRx).

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
| Accept Validation             | X       | X                |              |              |
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

<span id="_Toc65696640" class="anchor"></span>Table 3: RxRenewal Response – Replace Type (v4.0)

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

<span id="_Toc65696641" class="anchor"></span>Table 4: RxChange Response – Replace Type (v4.0)

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/005.png)

<span id="_Toc56760878" class="anchor"></span>Figure 2‑1: VA Single Sign-on

3.  In the “Select a Certificate” dialog, select the desired certificate and then select OK.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/006.png)

<span id="_Toc56760879" class="anchor"></span>Figure 2‑2: Select a Certificate

4.  In the “ActivClient Login” dialog, enter the Personal Identification Number (PIN) in the “PIN” text box and select OK.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/007.png)

<span id="_Toc56760880" class="anchor"></span>Figure 2‑3: Active Client Login

13. A warning message displays. Select Accept.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/008.png)

<span id="_Toc56760881" class="anchor"></span>Figure 2‑4: Warning Message

When authentication and authorization is successful, the application home screen displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/009.png)

<span id="_Toc56760882" class="anchor"></span>Figure 2‑5: Home Screen

### Screen Navigation and Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure outlines the key areas of the screen layout. Brief descriptions of the screen layout are provided below:

1.  On the top-right of the screen is a Go to Main Content link for Section 508 purposes to allow a user to be directed to the main content on the screen.
2.  The logged-in user’s VA User ID and a Logout link displays on the right side of the banner.
3.  Below the banner, the main tabs display for accessing the screens within the application.
4.  The name of the screen displays below the main tabs.
5.  The bottom of the screen also contains hyperlinks to the main tab screens.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/010.png)

<span id="_Toc56760883" class="anchor"></span>Figure 2‑6: Web-Based Application Screen Layout

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/011.png)

<span id="_Toc56760884" class="anchor"></span>Figure 2‑7: Home Screen

#### Pharmacy Management

To access the Pharmacy Management screen, select the Pharmacy Management tab in the menu bar. The Pharmacy Management screen displays the Pharmacy Management table that provides information about pharmacies and allows Administrators and Pharmacy Managers to search for, add, and edit pharmacies. Users can also enable/disable the receiving of prescriptions targeted for a particular pharmacy.

> **NOTE:** The search filters default to “All” in the VISN field. The user must select the Search button for information to populate.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/012.png)

<span id="_Toc56760885" class="anchor"></span>Figure 2‑8: Pharmacy Management Screen

#### Track/Audit

To access the Track/Audit eR<sub>X</sub> screen, select the Track/Audit tab in the menu bar. The Track/Audit eR<sub>X</sub> screen allows users view eR<sub>X</sub>es and their related messages.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/013.png)

<span id="_Toc56760886" class="anchor"></span>Figure 2‑9: Track/Audit Screen

#### Reports

To access the Reports screen, select the Reports tab in the menu bar. The Reports screen allows all users to run and view a Summary Report.

The system uses the comma-separated values (.CSV) format. Users can view reports using a third-party tool, such as Microsoft Excel.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/014.png)

<span id="_Toc56760887" class="anchor"></span>Figure 2‑10: Reports Screen

#### User Management

To access the User Management screen, select the User Management tab in the menu bar. The User Management screen allows Administrators to add users, enable/disable users, and modify user roles. This screen only displays for users with Administrator access.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/015.png)

<span id="_Toc56760888" class="anchor"></span>Figure 2‑11: User Management Screen

#### Help 

To access the Help page, select the Help tab in the menu bar. The Help page provides help topics and production support information.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/016.png)

<span id="_Toc498613630" class="anchor"></span>Figure 2‑12: Help Tab

When the Help tab is selected, the Help Page displays in a new window.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/017.png)

<span id="_Toc56760890" class="anchor"></span>Figure 2‑13: Help Page

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/018.png)

<span id="_Toc56760891" class="anchor"></span>Figure 2‑14: Search for a Pharmacy

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/019.png)

<span id="_Toc56760892" class="anchor"></span>Figure 2‑15: NCPDP ID Column Hyperlinks

The Edit Pharmacy screen displays. At the top of the screen is a Warning Message with text notifying the user that any change made here will not update the pharmacy in CH’s published pharmacy directory. Selecting Return to Pharmacy Management returns the user to the Pharmacy Management screen.

3.  Select No from the “Inbound eR<sub>X</sub> Enabled” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/020.png)

<span id="_Toc56760893" class="anchor"></span>Figure 2‑16: eR<sub>X</sub> Enabled Drop Down

4.  At the bottom of the Edit Pharmacy screen, select Update to save all changes. The date that the fields were modified displays in the “Updated Date” field.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/021.png)

<span id="_Toc56760894" class="anchor"></span>Figure 2‑17: Update Pharmacy Information

#### Enable eR<sub>X</sub>

The pharmacy can be enabled once it is ready to receive eR<sub>X</sub>es again.

To enable a pharmacy:

1.  Select Yes from the “Inbound eR<sub>X</sub> Enabled” drop down on the Edit Pharmacy screen.
2.  Select Update (not shown).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/022.png)

<span id="_Toc56760895" class="anchor"></span>Figure 2‑18: Enable/Disable Pharmacy

> **NOTE:** If a pharmacy is not enabled and a prescription comes in for that pharmacy, an error message is sent back to the provider’s EHR system to notify the provider that the pharmacy is not currently receiving eR<sub>X</sub>es.

#### Enrollment and Eligibility Check

The Enrollment and Eligibility (E&E) check may be enabled or disabled for individual pharmacies. This option is provided so each pharmacy may decide whether to turn the E&E check on or off depending on whether the patients whose eR<sub>X</sub>es are filled at the pharmacy are enrolled in the E&E system. For example, MbM does not currently have any patient enrolled with the E&E system.

To ensure the Enrollment and Eligibility Check is enabled for a pharmacy:

1.  Select the desired pharmacy from the Pharmacy Management table.
2.  Ensure Yes displays in the “Enrollment and Eligibility Check Enabled” field.
3.  If required, select Yes in the “Enrollment and Eligibility Check Enabled” drop-down and then select Update.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/023.png)

<span id="_Toc56760896" class="anchor"></span>Figure 2‑19: Enrollment and Eligibility Check Enabled

If the Enrollment and Eligibility Check is not enabled for a pharmacy, the Patient Auto Check Status displays as “MVI_MATCH_NOT_FOUND” on the Track/Audit screen.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/024.png)

<span id="_Toc56760897" class="anchor"></span>Figure 2‑20: Track/Audit – Enrollment and Eligibility Check Not Performed

### Track/Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Track/Audit screen allows users to search for eR<sub>X</sub> messages and track prescriptions and provides the ability to view and print the details of a prescription.

When the user initially enters the Track/Audit screen, the default date range is two days (the current date and the previous date) and the default records limit is set to 100.

> **NOTE:** If a user is not assigned to one of the MbM station IDs, that user cannot see any records related to MbM station IDs.

#### Searching for a Message

To search for a message:

1.  Select the desired search criteria from the drop downs and enter desired search keywords in the text fields.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/025.png)

<span id="_Toc56760898" class="anchor"></span>Figure 2‑21: Track/Audit Search Criteria

The search criteria are described in the table below.

<span id="_Ref5966673" class="anchor"></span>Table 5: Track/Audit Search Criteria Descriptions

| Search Field                | Field Type                 | Description                                                                                                                       | Drop Down Options                                                                                                                                                                                                                                                                                                                      |
|-----------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VISN                        | Drop Down                  | VISN number that a VA pharmacy is associated with                                                                                 | All VISNs, each VISN number                                                                                                                                                                                                                                                                                                            |
| VA Station ID               | Text                       | Station ID of the VA pharmacy                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                    |
| From                        | Text or Calendar Drop Down | Beginning date. Choose From date for a date range search; select the date from the calendar or enter a date in MM/DD/YYYY format. | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                |
| To                          | Text or Calendar Drop Down | End date. Choose To date for a date range search; select the date from the calendar or enter a date in MM/DD/YYYY format.         | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                |
| Message Type                | Drop Down                  | Type of the NCPDP message type                                                                                                    | All, CancelRx, CancelRxResponse, Error, NewRx, RxRenewalResponse, RxRenewalRequest, RxChangeResponse, RxChangeRequest, Status, Verify                                                                                                                                                                                                  |
| Message ID                  | Text                       | Prescription message ID (generated by CH for incoming eR<sub>X</sub>es)                                                           | N/A                                                                                                                                                                                                                                                                                                                                    |
| Relates to Message ID       | Text                       | To search for messages related to a Message ID                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                    |
| Patient SSN                 | Text                       | Patient Social Security Number                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                    |
| Patient Last Name           | Text                       | Patient last name                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                    |
| Patient First Name          | Text                       | Patient first name                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                    |
| Patient DOB                 | Text or Calendar Drop Down | Patient date of birth                                                                                                             | Calendar/Enter DOB in MM/DD/YYYY format                                                                                                                                                                                                                                                                                                |
| Prescriber NPI              | Text                       | Prescriber National Provider Identifier (NPI)                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                    |
| Prescribed Drug             | Text                       | Drug prescribed from the eR<sub>X</sub>                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                    |
| Prescriber First Name       | Text                       | First name of prescriber                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                    |
| Prescriber Last Name        | Text                       | Last name of prescriber                                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                    |
| Prescriber DEA \#           | Text                       | Drug Enforcement Administration (DEA) number of prescriber                                                                        | N/A                                                                                                                                                                                                                                                                                                                                    |
| Message Status              | Drop Down                  | Processing Hub message status                                                                                                     | Auto check Processing Completed, VistA OP Delivery Successful, VistA OP Delivery In Process, VistA OP Delivery Retries Exceeded, Auto check in Progress, Pharmacy Inbound eR<sub>X</sub> Not Enabled, Pharmacy Unknown, Outbound Message Send Completed, Outbound Message Delivery Retries Exceeded, Outbound Message Send In Progress |
| eR<sub>X</sub> Reference \# | Text                       | Unique, internal VA reference \# assigned to all messages                                                                         | N/A                                                                                                                                                                                                                                                                                                                                    |
| Sent or Received            | Drop Down                  | Select Sent (Outbound) or Received (Inbound) messages                                                                             | Received, Sent                                                                                                                                                                                                                                                                                                                         |

Track/Audit eRx Search Criteria

2.  Use the “Max Records” drop down to set the limit of search results. This value can be set to 100, 7500, or 10000. The default value is 100. Limiting search results decreases the time required to conduct a search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/026.png)

<span id="_Toc56760899" class="anchor"></span>Figure 2‑22: Max Records Drop Down

3.  Select Search to execute the search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/027.png)

<span id="_Toc56760900" class="anchor"></span>Figure 2‑23: Track/Audit eR<sub>X</sub> Search

A “Search in progress” message displays during search.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/028.png)

<span id="_Toc56760901" class="anchor"></span>Figure 2‑24: Search in Progress Message

The search results display in a table below the search criteria. The total number of records in the search results display at the bottom of the table.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/029.png)

<span id="_Toc56760902" class="anchor"></span>Figure 2‑25: Search Results

The Search Results fields and descriptions are listed in the table below.

<span id="_Toc498002240" class="anchor"></span>Table 6: Search Results Fields & Descriptions

| Field                       | Description                                                                        |
|-----------------------------|------------------------------------------------------------------------------------|
| eR<sub>X</sub> Reference \# | Unique, internal VA reference \# assigned to all messages as a hyperlink           |
| Message Type                | Type of message                                                                    |
| Patient Name                | First and last name of the patient                                                 |
| Patient DOB                 | Date of birth for the patient                                                      |
| Patient SSN                 | Social security number of the patient                                              |
| Drug Prescribed             | Drug prescribed to the patient                                                     |
| Message ID                  | Identification of the message                                                      |
| Prescriber Name             | First and last name of the prescriber                                              |
| Prescriber NPI              | National Provider Identifier for the prescriber                                    |
| Prescriber DEA              | Identifier assigned to prescriber by United States Drug Enforcement Administration |
| VISN                        | VISN that the VA pharmacy is associated with                                       |
| Station ID                  | Station ID of the VA pharmacy                                                      |
| Pharmacy Name               | Internal VA pharmacy name                                                          |
| Address                     | Address of VA pharmacy                                                             |
| Relates to Message ID       | Lists message related to a particular Message ID as a hyperlink                    |
| Received Date               | Date that the eR<sub>X</sub> was received by VA                                    |
| Patient AutoCheck Status    | Results of system patient auto-validation check                                    |
| Provider AutoCheck Status   | Results of system provider auto-validation check                                   |
| Drug AutoCheck Status       | Results of system drug auto-validation check                                       |
| Message Status              | Current status of the message                                                      |

Table of the Search Results Fields and Descriptions

#### Export Search Results

From the Track/Audit tab, users have the capability of exporting the search results. Exports are in .CSV format and can be viewed in Microsoft Excel. The number of records exported is dependent on the number of records selected in the “Max Records” dropdown.

To export the search results:

1.  Select Export.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/030.png)

<span id="_Toc56760903" class="anchor"></span>Figure 2‑26: Export Search Results

A prompt displays asking to Open or Save the results.

2.  Select Open to view the results.
3.  Select the down arrow to the right of Save to save the results to a desired location.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/031.png)

<span id="_Toc56760904" class="anchor"></span>Figure 2‑27: Track/Audit Export Prompt (after clicking Export buttons)

4.  When the arrow is selected, the system displays a “Save As” dialog (not shown). Navigate to a location on your system to save the file.
14. 

#### Inbound/Outbound Message Detail

Inbound/outbound message detail information is reviewed and managed under the Track/Audit tab.

To access the detail screen of a message, select the hyperlink in the “eRx Reference \#” column to display the desired message detail.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/032.png)

<span id="_Toc56760905" class="anchor"></span>Figure 2‑28: Track/Audit Grid View

The message details display. Each message detail screen includes the following buttons:

- Return to Search: Return to the search results screen.
- Show Related Messages: Displays all sent and received eR<sub>X</sub> messages that are related to the displayed message.
- Print: Print the eR<sub>X</sub> message details.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/033.png)

<span id="_Toc56760906" class="anchor"></span>Figure 2‑29: Message Details

If the Show Related Messages button is selected, any sent and received messages that are related to the current message display based on the Message ID linkage. For example, Related Messages for a RxRenewal Response should, at minimum, display the related RxRenewal Request and the NewRx for which the refill was requested. Related messages also include related Status, Verify, and/or Error Messages, if applicable. Related messages display in descending order of received date. The most recent message is at the top of the list, and the NewRx message is at the bottom. Select the number in the “eR<sub>X</sub> Reference \#” column to view message details.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/034.png)

<span id="_Toc56760907" class="anchor"></span>Figure 2‑30: Related Messages

#### NewRx Message

The NewRx detail screen displays the new eR<sub>X</sub> from an external provider.

To access the NewRx detail screen, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/035.png)

<span id="_Toc56760908" class="anchor"></span>Figure 2‑31: NewRx Message Search and Results Screen

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/036.png)

<span id="_Toc56760909" class="anchor"></span>Figure 2‑32: NewRx Message Details Screen

#### RxRenewal Request

RxRenewal Request message details can be viewed under the Track/Audit tab.

To access the RxRenewal Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/037.png)

<span id="_Toc56760910" class="anchor"></span>Figure 2‑33: RxRenewal Request Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/038.png)

<span id="_Toc56760911" class="anchor"></span>Figure 2‑34: RxRenewal Request Details Screen

#### RxRenewal Response

RxRenewal Response message details can be viewed under the Track/Audit tab.

To access the RxRenewal Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/039.png)

<span id="_Toc56760912" class="anchor"></span>Figure 2‑35: RxRenewal Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/040.png)

<span id="_Toc56760913" class="anchor"></span>Figure 2‑36: RxRenewal Response Detail Screen

#### RxChange Request

RxChange Request message details can be viewed under the Track/Audit tab.

To access the RxChange Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/041.png)

<span id="_Toc56760914" class="anchor"></span>Figure 2‑37: RxChange Request Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/042.png)

<span id="_Toc56760915" class="anchor"></span>Figure 2‑38: RxChange Request Detail Screen

#### RxChange Response

RxChange Response message details can be viewed under the Track/Audit tab.

To access the RxChange Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/043.png)

<span id="_Toc56760916" class="anchor"></span>Figure 2‑39: RxChange Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/044.png)

<span id="_Toc56760917" class="anchor"></span>Figure 2‑40: RxChange Response Detail Screen

#### CancelRx Request

The CancelRx Request message details can be viewed under the Track/Audit tab.

To access the CancelRx Request message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/045.png)

<span id="_Toc56760918" class="anchor"></span>Figure 2‑41: CancelRx Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/046.png)

<span id="_Toc56760919" class="anchor"></span>Figure 2‑42: CancelRx Detail Screen

#### CancelRx Response

The CancelRx Response message details can be displayed under the Track/Audit tab.

To access the CancelRx Response message details, select the hyperlink in the “eRx Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/047.png)

<span id="_Toc56760920" class="anchor"></span>Figure 2‑43: CancelRx Response Search and Search Results

The selected message details display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/048.png)

<span id="_Toc56760921" class="anchor"></span>Figure 2‑44: CancelRx Response Detail Screen

#### Error Messages

At multiple points in the process, an Error transaction can be generated. Outbound error messages are sent when an eR<sub>X</sub> record that is NCPDP corrupted is received, when the receiving Pharmacy is not one of the VA pharmacies configured in the Inbound eR<sub>X</sub> system, or when an eR<sub>X</sub> record with a Written or Effective Date older than or equal to 365 days is received.

Inbound Errors for VistA may be received under multiple situations such as if the Prescriber’s EHR system is unable to receive and process a certain transaction sent from the Pharmacy, or a connection between the Transaction Hub and CH is not working.

To access the Error message details, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/049.png)

<span id="_Toc56760922" class="anchor"></span>Figure 2‑45: Error Message Search and Search Results

The selected message details sent and received by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/050.png)

<span id="_Toc56760923" class="anchor"></span>Figure 2‑46: Error Message Detail Screen

#### Verify Messages

The Verify message confirms delivery of a message to its final destination. The Verify message is an NCPDP transaction that indicates the acceptance of the request by the receiving system. This message is used to communicate the data content status of a transaction. Verify Messages sent from the Transaction Hub are Outbound Verify Messages. Verify Messages received from CH and/or an External Provider’s EHR system are Inbound Verify Messages.

To access the Verify message detail screen, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/051.png)

<span id="_Toc56760924" class="anchor"></span>Figure 2‑47: Verify Message Search and Search Results

The selected message details sent by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/052.png)

<span id="_Toc56760925" class="anchor"></span>Figure 2‑48: Verify Message Detail Screen

#### Status Messages

The Status message is used to relay acceptance of a transaction back to the sender. The Status message is an NCPDP transaction that indicates the acceptance of the request. For the Inbound eR<sub>X</sub> web-based application, Inbound Status messages are received from CH and Outbound Status messages are sent from the Transaction Hub. Outbound Status messages are not stored in the Transaction Hub and cannot be viewed.

To access the Status message detail screen, select the hyperlink in the “eR<sub>X</sub> Reference \#” column for the desired message.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/053.png)

<span id="_Toc56760926" class="anchor"></span>Figure 2‑49: Status Message Search and Search Results

The selected message details received by the Processing Hub display.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/054.png)

<span id="_Toc56760927" class="anchor"></span>Figure 2‑50: Status Message Detail Screen

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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/055.png)

<span id="_Toc56760928" class="anchor"></span>Figure 2‑51: Summary Report NewRx Only Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/056.png)

<span id="_Toc56760929" class="anchor"></span>Figure 2‑52: NewRx Summary Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The NewRx Only Summary Report fields are described in the table below.

<span id="_Toc65696644" class="anchor"></span>Table 7: NewRx Only Summary Report Columns

| Field                  | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| VISN                   | Pharmacy VISN number                                                                             |
| VA Station ID          | VistA pharmacy identification number                                                             |
| NCPDP ID               | National Council for Prescription Drug Programs (NCPDP) identification number                    |
| Pharmacy Name          | VistA pharmacy name                                                                              |
| Address                | Pharmacy Address                                                                                 |
| \#New Rx               | Number of fillable prescriptions                                                                 |
| \#Pharmacy Disabled    | Number of Pharmacy Disabled errors                                                               |
| \#Rejected at Hub      | Number of eR<sub>X</sub>es rejected at the Processing Hub                                        |
| \#Passed Auto check    | Number of eR<sub>X</sub>es that passed auto check criteria                                       |
| \#Failed Auto check    | Sum of eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks                      |
| \#Rejected by Pharmacy | Number of eR<sub>X</sub>es rejected by the pharmacy                                              |
| \#Rx Filled            | Number of RxFill messages received by the Processing Hub from VistA                              |
| \#Accepted by Pharmacy | Number of eR<sub>X</sub>es that have been accepted by the Pharmacy into VistA Pending/Outpatient |

Summary Report Columns

#### Auto Check Details Report

The Auto Check Details Report provides details of the auto checks performed by the hub side.

To run an Auto Check Details Report:

1.  From the Reports screen, select Auto Check Details Report from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/057.png)

<span id="_Toc56760930" class="anchor"></span>Figure 2‑53: Auto Check Details Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/058.png)

<span id="_Toc56760931" class="anchor"></span>Figure 2‑54: Auto Check Details Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The Auto Check Details Report fields are described in the table below.

<span id="_Toc65696645" class="anchor"></span>Table 8: Auto Check Details Report Columns

| Field                          | Description                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------|
| VISN                           | Pharmacy VISN number                                                                                       |
| VA Station ID                  | VistA pharmacy identification number                                                                       |
| NCPDP ID                       | National Council for Prescription Drug Programs (NCPDP) identification number                              |
| Pharmacy Name                  | VistA pharmacy name                                                                                        |
| \#New Rx                       | Number of fillable prescriptions                                                                           |
| \#Passed Autocheck             | Number of eR<sub>X</sub>es that passed auto check criteria                                                 |
| \#Failed Autocheck             | Sum of eR<sub>X</sub>es that failed Patient, Provider, and Drug Auto checks                                |
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

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/059.png)

<span id="_Toc56760932" class="anchor"></span>Figure 2‑55: Reject Reasons Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/060.png)

<span id="_Toc56760933" class="anchor"></span>Figure 2‑56: Reject Reasons Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp.

The Reject Reason Report fields are described in the table below.

<span id="_Toc65696646" class="anchor"></span>Table 9: Reject Reason Report Columns

| Field                       | Description                                                                                    |
|-----------------------------|------------------------------------------------------------------------------------------------|
| VISN                        | Pharmacy VISN number                                                                           |
| VA Station ID               | VistA pharmacy identification number                                                           |
| NCPDP ID                    | National Council for Prescription Drug Programs (NCPDP) identification number                  |
| Pharmacy Name               | VistA pharmacy name                                                                            |
| \#New Rx                    | Number of fillable prescriptions                                                               |
| \#Accepted by Pharmacy      | Number of Inbound messages – (minus) number of failures and rejections – (minus) number filled |
| \#Rejected by Pharmacy      | Number eR<sub>X</sub>es rejected by the pharmacy                                               |
| \#Patient Not Eligible      | Number of Patient Not Eligible rejections                                                      |
| \#Cannot Resolve Patient    | Number of Cannot Resolve Patient rejections                                                    |
| \#Provider Not Eligible     | Number of Provider Not Eligible rejections                                                     |
| \#Cannot Resolve Provider   | Number of Cannot Resolve Provider rejections                                                   |
| \#Not Eligible for Renewals | Number of Drug Not Eligible for Renewals rejections                                            |
| \#Non Formulary             | Number of Non Formulary rejections                                                             |
| \#Duplicate Rx              | Number of rejections due to duplicate R<sub>X</sub>                                            |
| \#Invalid Qty               | Number of rejections due to an Invalid Quantity entered                                        |
| \#Duplicate Therapy Class   | Number of rejections due to Duplicate Therapy Class                                            |
| \#CS Not Allowed            | Number of rejections due to CS Not Allowed                                                     |
| \#Contact Pharmacy (ERR01)  | Multiple errors, please contact the pharmacy                                                   |
| \#Incorrect Pharmacy        | Number of rejections due to Incorrect Pharmacy                                                 |
| \#Contact Pharmacy (ERR03)  | Incorrect Pharmacy                                                                             |

This table displays the Summary Report Columns field descriptions.

#### eR<sub>X</sub> Summary Report

The eR<sub>X</sub> Summary Report provides a summary of eR<sub>X</sub> auto-validation checks.

To run an eR<sub>X</sub> Summary Report:

1.  From the Reports screen, select eRx Summary Report from the “Select Report” drop down.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/061.png)

<span id="_Toc56760934" class="anchor"></span>Figure 2‑57: eR<sub>X</sub> Summary Report Drop Down Selection

2.  Select the desired VISN from the “VISN” drop down. The drop down contains each VISN number as well as an ALL selection to select all VISNs.
3.  To narrow the search by VA Station ID, select the Station ID for the report.
4.  Select the date range from the Calendar drop downs for the report or enter date(s) using the MM/DD/YYYY format.
5.  Select Run Report to generate the report.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/062.png)

<span id="_Toc56760935" class="anchor"></span>Figure 2‑58: eR<sub>X</sub> Summary Report

Beneath the generated report, a total number of records displays. The totals for each column display at the bottom of the page, along with a “Report As of:” date and time stamp. The eR<sub>X</sub> Summary Report fields are described in the table below.

<span id="_Toc498002241" class="anchor"></span>Table 10: eR<sub>X</sub> Summary Report Columns

| Field                | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| VISN                 | Pharmacy VISN number                                                          |
| VA Station ID        | VistA pharmacy identification number                                          |
| NCPDP ID             | National Council for Prescription Drug Programs (NCPDP) identification number |
| Pharmacy Name        | VistA pharmacy name                                                           |
| \#New Rx             | Number of New eR<sub>X</sub>es                                                |
| \#RxRenewal Request  | Number of renewal requests                                                    |
| \#RxRenewal Response | Number of renewal responses                                                   |
| \#RxChange Request   | Number of changes requested                                                   |
| \#RxChange Response  | Number of changed R<sub>X</sub> responses                                     |
| \#CancelRx Request   | Number of canceled R<sub>X</sub> requests                                     |
| \#CancelRx Response  | Number of canceled R<sub>X</sub> responses                                    |
| \#RxFill             | Number of RxFill messages received by the Processing Hub from VistA           |

Summary Report Columns

### Export Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Reports tab, users may export a report to a .CSV format.

To Export a report:

1.  Select the Export button.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/063.png)

<span id="_Toc56760936" class="anchor"></span>Figure 2‑59: Export Report buttons

A prompt displays asking to Open or Save the report.

2.  Select Open to view the report.
3.  Select the down arrow to the right of Save to save the report to a desired location.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/064.png)

<span id="_Toc56760937" class="anchor"></span>Figure 2‑60: Summary Report Export Prompt (after clicking Export button)

4.  When the arrow is selected, the system displays a “Save As” dialog (not shown). Navigate to a location on your system to save the file.

### User Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Management screen allows Administrators to add new users to one or more sites (Station ID), enable users, disable users, modify user roles and existing user records by assigning them to one or more sites. This screen only displays for users with Administrator access.

The User Management screen displays the list of all users that are added to this system along with their roles and privileges and is sorted by First Name.

#### Add New User

System Administrators can add new users from the User Management screen.

To add a new user:

1.  Enter the new user’s User ID, First Name, and Last Name.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/065.png)

<span id="_Toc56760938" class="anchor"></span>Figure 2‑61: Add User - User ID, First Name, Last Name

2.  Select the new user’s role(s). Multiple roles may be selected by holding \<Ctrl\> while selecting more than one role.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/066.png)

<span id="_Toc56760939" class="anchor"></span>Figure 2‑62: Add User - Select User Roles

3.  Select the Station ID(s) for the user to have access to. Use the drop down menu to display the Station ID selection. Multiple Station IDs may be selected by holding \<Ctrl\> while selecting more than one Station ID.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/067.png)

<span id="_Toc56760940" class="anchor"></span>Figure 2‑63: Add User – Select Station ID

15. Select Add to add the selected Station ID(s) to the “Selected Station IDs” field. To remove Station IDs from the “Selected Station IDs” field, select Remove (not shown).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/068.png)

<span id="_Toc56760941" class="anchor"></span>Figure 2‑64: Add User – Add and Remove Station ID

When a user is assigned to a Station ID, they are only able to see other users and information within that Station ID. For example, in the User Management table they only see users also assigned to that Station ID and under Pharmacy Management, they only see information for pharmacies within that Station ID.

If All is selected from the “Station ID” field and added to the “Selected Station IDs” field, the user has access to all Station IDs. Additional Station ID values cannot be added if All has been selected and added to the “Selected Station IDs” field. If a user attempts to add additional values an error message displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/069.png)

<span id="_Toc56760942" class="anchor"></span>Figure 2‑65: All Selection Error Message

16. Select Save to add the new user to the users list. Select Cancel to cancel adding a new user.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/070.png)

<span id="_Toc56760943" class="anchor"></span>Figure 2‑66: Add User - Save and Cancel

#### Modify User Roles

System Administrators can modify user roles from the User Management screen. User roles include:

- Pharmacy Manager
- PBM Admin
- Pharmacy User
- Administrator

For further information on user roles and capabilities, refer to section <u>1.4 Roles and Capabilities</u>.

To modify user roles:

1.  From the users list, locate the user and select the checkbox(es) for the desired user role(s).

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/071.png)

<span id="_Toc56760944" class="anchor"></span>Figure 2‑67: Select User Roles

2.  Select Save at the bottom of the screen.

A message displays indicating that the user was updated successfully.

3.  Select Cancel to cancel modifying user roles.

#### Enable/Disable Users

Users can be disabled and/or re-enabled to use the web application. Enabling and disabling a user’s access is selected using the “Enable/Disable User” checkbox in the desired user’s row. A deselected checkbox (shown below) reflects that the user’s access is enabled, and a selected checkbox reflects that the user’s access has been disabled.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/072.png)

<span id="_Toc56760945" class="anchor"></span>Figure 2‑68: User Management Table – Enable/Disable User

To update a user’s access:

1.  Locate the user in the User Management table.
2.  Select the checkbox in the “Enable/Disable User” column to disable access or deselect the checkbox to re-enable access.
3.  Select Save from the bottom of the screen (not shown) to update the user’s access.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/073.png)

<span id="_Toc56760946" class="anchor"></span>Figure 2‑69: User Disabled

When a user is disabled, their information is greyed in the User Management table.

If a user that has been disabled tries to log in to the application, an error message displays.

![](inbound-eprescribing-user-manual-unit-1-unit-2-pso-7-581/074.png)

<span id="_Toc56760947" class="anchor"></span>Figure 2‑70: User Disabled Error Message

### From: Inbound ePrescribing User Manual (Unit 6) PSO*7*581

## CancelRx Request in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CancelRx Request is received in the Holding Queue, it is displayed in the list view in one of the actionable statuses until it is acknowledged. Depending on the status of the fillable eR<sub>X</sub> on which the CancelRx Request has been received, the status of the request is changed according to the status of the fillable eR<sub>X</sub> prior to canceling or auto-Discontinuing. For a full list of CancelRx Request statuses, please refer to <u>Table 13: Holding Queue Status Codes & Descriptions for CancelRx Request Message Type</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

Once the request is acknowledged, it is no longer displayed in the list view. CancelRx Request messages may be retrieved at any point using \<MV\> Message View and/or \<SR\> Search.

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type CancelRx Request.

The CancelRx Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/002.png)

<span id="_Toc56761232" class="anchor"></span>Figure ‑: CAO Status in Holding Queue

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

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/003.png)

<span id="_Toc56761233" class="anchor"></span>Figure ‑: Holding Queue List View

3.  Select the desired record from the list.

The CancelRx Request message details display.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/004.png)

<span id="_Toc56761234" class="anchor"></span>Figure ‑: CancelRx Request Details

The user may continue to scroll through the CancelRx Request Details page to view CancelRx Request Information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/005.png)

<span id="_Toc56761235" class="anchor"></span>Figure ‑: CancelRx Request Details – CancelRx Request Information

## CancelRx Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may select the CancelRx Response message from the Holding Queue to view the message details in the Message Details View.

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type CancelRx Response.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/006.png)

<span id="_Toc56761236" class="anchor"></span>Figure ‑: Holding Queue List View - CancelRx Response

3.  Select the desired record from the list.

The CancelRx Response message details display.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/007.png)

<span id="_Toc56761237" class="anchor"></span>Figure ‑: CancelRx Response Details

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

<span id="_Toc56761279" class="anchor"></span>Table 1: CancelRx Request and Response

| CancelRx Request Status (Before ACK) | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note                | Manual Denied CancelRx Response \> Denial Reason                         |
|--------------------------------------|-------------------------------------|--------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------|
| CAR (CANCELRX REQUEST RECEIVED)      | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| CAP (CANCEL PAPERRX OR FAXED RX)     | CAA                                 | CNP                                  | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Cancel Rx Request and Response table displays the Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

For more information on the \<ACK\> Acknowledge action, refer to section <u>6.7 Acknowledge: Hidden Action for CancelRx Request</u>.

To view a CancelRx Request details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/008.png)

<span id="_Toc56761238" class="anchor"></span>Figure ‑: Holding Queue List View – CAP

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/009.png)

<span id="_Toc56761239" class="anchor"></span>Figure ‑: CAP Details Screen 1

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/010.png)

<span id="_Toc56761240" class="anchor"></span>Figure ‑: CAP Details Screen 2

#### Matching Fillable eR<sub>X</sub> Prescription Found

When the CancelRx Request is received in the Holding Queue and finds a matching fillable eR<sub>X</sub> record to be canceled, the status of the fillable eR<sub>X</sub> record changes to “CAN” (Original eR<sub>X</sub> Canceled in Holding Queue) from its previously known status. In the case of a NewRx record, those statuses are: “N”, “I”, “W”, “H*xx* (where *x* = letter)”, “RJ” or “RM”. Once the fillable prescription is marked “CAN”, it is not an actionable entry and is not displayed in the Holding Queue’s list view.

#### Automated Approved CancelRx Responses

<span id="_Toc56761280" class="anchor"></span>Table 2: Scenarios for Automated Approved CancelRx Responses

| NewRx Status  | CancelRx Request Status (Before ACK) | CancelRx Response Status          | Automated Approved CancelRx Response \> Note             |
|---------------|--------------------------------------|-----------------------------------|----------------------------------------------------------|
| N (NEW)       | CAO (CANCEL PROCESS COMPLETE)        | CNP (CANCELRX RESPONSE PROCESSED) | R<sub>X</sub> was never dispensed. Canceled at Pharmacy. |
| RJ (REJECTED) | CAO                                  | CNP                               | R<sub>X</sub> was never dispensed. Rejected at Pharmacy. |

The Scenarios for Automated Approved Cancel Rx Responses table displays the New Rx Status, Cancel Rx Request Status (Before ACK), Cancel Rx Response Status and Automated Approved Cancel Rx Response \>\> Note details.

To view an Automated CancelRx Response details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/011.png)

<span id="_Toc56761241" class="anchor"></span>Figure ‑: CAO Status in Holding Queue List View

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/012.png)

<span id="_Toc56761242" class="anchor"></span>Figure ‑: CAO Details Screen 1

As the user continues to scroll, the CancelRx Response Information displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/013.png)

<span id="_Toc56761243" class="anchor"></span>Figure ‑: CAO Details Screen 2

#### Manual Approved or Denied CancelRx Responses

<span id="_Toc56761281" class="anchor"></span>Table 3: Scenarios for Manual Approved or Denied CancelRx Responses

| Inbound eRx Message Type | eRx Status                                                | CancelRx Request Status (Before ACK)    | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note | Manual Denied CancelRx Response \> Denial Reason                         |
|--------------------------|-----------------------------------------------------------|-----------------------------------------|-------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| NewRx                    | I / H*xx* / W / RM                                        | CAH (CANCEL COMPLETED IN HOLDING QUEUE) | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled – R<sub>X</sub> not found in pharmacy system. |
| RxRenewal Response       | RXR / RXE / RXI / RXW / RXP / RXC                         | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - Rx not found in pharmacy system.            |
| RxChange Response        | CXN / CXE / CXA / CXV / CXY / CXD / CXI / CXW / CXP / CXC | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Scenarios for Manual Approved or Denied Cancel Rx Responses table displays the New Rx Status, Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

To view a manually approved CancelRx Response details screen, select the desired record from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/014.png)

<span id="_Toc56761244" class="anchor"></span>Figure ‑: CAH Status in Holding Queue List View

The details screen displays the eR<sub>X</sub> information along with the CancelRx Request information. In the example below, the Last NewRx Status displays as “I” (In Process).

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/015.png)

<span id="_Toc56761245" class="anchor"></span>Figure ‑: CAH Details Screen

### CancelRx Process - eR<sub>X</sub> Records in Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the CancelRx Request is received in the Holding Queue for a NewRx record to be canceled, and the status of the NewRx record is “PR” (Processed), an entry exists on the Outpatient side, the status changes to “CAN” (Original eR<sub>X</sub> Canceled in Holding Queue). Once the original prescription is marked “CAN”, it is not an actionable entry and is not displayed in the Holding Queue’s list view.

When the NewRx is in one of the statuses as specified in the table below, an automated Approved CancelRx Response is sent outbound after auto-Discontinuing the Prescription in OP. The Activity log for the prescription captures the auto-Discontinue activity from this process.

#### Automated Approved CancelRx Responses

<span id="_Toc56761282" class="anchor"></span>Table 4: Scenarios for Automated Approved CancelRx Responses when the original is a NewRx

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

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/016.png)

<span id="_Toc56761246" class="anchor"></span>Figure ‑: Medication Profile

The R<sub>X</sub> Activity Log displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/017.png)

<span id="_Toc56761247" class="anchor"></span>Figure ‑: R<sub>X</sub> Activity Log 1

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/018.png)

<span id="_Toc56761248" class="anchor"></span>Figure ‑: R<sub>X</sub> Activity Log 2

The details of the CancelRx can be viewed in the Holding Queue on the CancelRx Details screen.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/019.png)

<span id="_Toc56761249" class="anchor"></span>Figure ‑: CancelRx Details Screen in Holding Queue 1

As the user continues to scroll, the section for CancelRx Request Information displays.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/020.png)

<span id="_Toc56761250" class="anchor"></span>Figure ‑: CancelRx Details Screen in Holding Queue 2

The NewRx Details screen includes an eR<sub>X</sub> status stating, “Original eR<sub>X</sub> Canceled in the Holding Queue”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/021.png)

<span id="_Toc56761251" class="anchor"></span>Figure ‑: NewRx Details Screen

In addition to the above scenarios, the following also go through the same workflow in the case of an “Active” Prescription being auto-Discontinued by a CancelRx Request:

- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status when there is an outstanding Denied RxRenewal Response in the Holding Queue.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status, when corresponding eR<sub>X</sub> record is also in Outpatient with a subsequent electronic renewal fill.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient when there is an outstanding Approved or Approved with Changes RxRenewal Response not in the Holding Queue's List View.
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient, when there is an outstanding Approved with Changes RxRenewal Response in the Holding Queue's List View (Approved with Changes RxRenewal Response has been \<AC\> Accepted in the Holding Queue).
- Auto-Cancel on NewR<sub>X</sub> records in the Holding Queue in “PR” status and in Outpatient, when there is an outstanding Approved with Changes RxRenewal Response in the Holding Queue's List View (Approved with Change RxRenewal Response has not been \<AC\> Accepted in the Holding Queue).

#### Manual Approved or Denied CancelRx Responses

When eR<sub>X</sub>es are renewed within VA using either RN function or using CPRS Renewal, the eR<sub>X</sub> is deemed as a VA Prescription. The “&” symbol used to denote eR<sub>X</sub> Prescriptions separately in OP does not display against such Prescriptions anymore. When CancelRx Requests are sent for fillable eR<sub>X</sub> prescriptions that are taken over by VA, the system will not auto-Discontinue the Prescriptions in OP. However, the corresponding Holding Queue NewRx record is changed to “CAN” status and the CancelRx Request may be marked “CAH”, indicating that there is user intervention required.

<span id="_Toc56761283" class="anchor"></span>Table 5: Scenarios for Manual Approved or Denied CancelRx Responses for NewRx

| NewRx Prescription Status in OP              | CancelRx Request Status (Before ACK)    | CancelRx Request Status (After ACK) | CancelRx Response Status (After ACK) | Manual Approved CancelRx Response \> Note | Manual Denied CancelRx Response \> Denial Reason                         |
|----------------------------------------------|-----------------------------------------|-------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| Prescription renewed in VA using RN function | CAH (CANCEL COMPLETED IN HOLDING QUEUE) | CAA (CANCELRX REQUEST ACKNOWLEDGED) | CNP (CANCELRX RESPONSE PROCESSED)    | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Prescription renewed using CPRS Renewal      | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Deleted                                      | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Drug Interactions                            | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |
| Non-Verified                                 | CAH                                     | CAA                                 | CNP                                  | R<sub>X</sub> canceled at Pharmacy.       | R<sub>X</sub> Not Canceled - R<sub>X</sub> not found in pharmacy system. |

The Scenarios for Manual Approved or Denied Cancel Rx Responses table displays the New Rx Prescription Status in OP, Cancel Rx Request Status (Before ACK), Cancel Rx Request Status (After ACK), Cancel Rx Response Status (After ACK), Manual Approved Cancel Rx Response \>\> Note and Manual Denied Cancel Rx Response \>\> Denial Reason details.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/022.png)

<span id="_Toc56761252" class="anchor"></span>Figure ‑: Cancel Completed in Holding Queue

### CancelRx Request Failed (CAF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“CAF” (CancelRx Failed) is an actionable status used for CancelRx process when a failure occurs. One scenario is when the Outpatient Profile of a patient is locked in OERR and the system is attempting to auto-discontinue an eR<sub>X</sub>.

<span id="_Toc56761284" class="anchor"></span>Table 6: Scenarios for CancelRx Failed

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

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/023.png)

<span id="_Toc56761253" class="anchor"></span>Figure ‑: Holding Queue – eR<sub>X</sub> in CAO Status

1.  Enter \<??\> to display additional actions.
2.  Enter \<ACK\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/024.png)

<span id="_Toc56761254" class="anchor"></span>Figure ‑: Additional Action - ACK

3.  Enter Yes to acknowledge the record.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/025.png)

<span id="_Toc56761255" class="anchor"></span>Figure ‑: Acknowledge Record

The CancelRx Request is acknowledged and Status is changed to “CAA” in the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/026.png)

<span id="_Toc56761256" class="anchor"></span>Figure ‑: Holding Queue – CAA Status

When viewing the details of the record, the status of the CancelRx Request displays as “CancelRx Request Acknowledged”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/027.png)

<span id="_Toc56761257" class="anchor"></span>Figure ‑: CancelRx Request Acknowledged

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

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/028.png)

<span id="_Toc56761258" class="anchor"></span>Figure ‑: Holding Queue – eR<sub>X</sub> in CAH Status

4.  Enter \<??\> to display additional actions.
5.  Enter \<ACK\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/029.png)

<span id="_Toc56761259" class="anchor"></span>Figure ‑: Additional Action - ACK

6.  Select the response type, \<A\> Approved or \<D\> Denied.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/030.png)

<span id="_Toc56761260" class="anchor"></span>Figure ‑: Select Response Type

7.  Enter Yes to acknowledge the record.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/031.png)

<span id="_Toc56761261" class="anchor"></span>Figure ‑: Acknowledge Record

The CancelRx Request is acknowledged and the Status is changed to “CAA” in the Holding Queue.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/032.png)

<span id="_Toc56761262" class="anchor"></span>Figure ‑: Holding Queue – CAA Status

When viewing the details of the record, the status of the CancelRx Request displays as “CancelRx Request Acknowledged”.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/033.png)

<span id="_Toc56761263" class="anchor"></span>Figure ‑: CancelRx Request Acknowledged

## Add Comments: Hidden Action for CancelRx Request/Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a free-text “Comment” field in the Message Details view for CancelRx Request and Response messages. This field allows users to enter additional comments on the CancelRx Request and Response messages. To add a comment:

1.  Type action \<AD\>.
8.  Type Request/Response comments.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/034.png)

<span id="_Toc56761264" class="anchor"></span>Figure ‑: Add Comments

9.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/035.png)

<span id="_Toc56761265" class="anchor"></span>Figure ‑: CancelRx Request Comments

The name of the user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the existing comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

10. Type action \<AD\>.
11. Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/036.png)

<span id="_Toc56761266" class="anchor"></span>Figure ‑: CancelRx Request Comments

12. Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-6-pso-7-581/037.png)

<span id="_Toc56761267" class="anchor"></span>Figure ‑: CancelRx Request Comments Updated

### From: Inbound ePrescribing User Manual (Unit 3 Part 1) PSO*7*581

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

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/002.png)

<span id="_Toc65697515" class="anchor"></span>Figure 3‑1: Complete Orders from eR<sub>X</sub> Menu Option

1.  Select RX Prescription Received Date.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/003.png)

<span id="_Toc65697516" class="anchor"></span>Figure 3‑2: Select RX

The first screen that displays upon accessing the eR<sub>X</sub> Holding Queue is the Holding Queue list view screen.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/004.png)

<span id="_Toc65697517" class="anchor"></span>Figure 3‑3: eR<sub>X</sub> Holding Queue List View

#### eR<sub>X</sub> Holding Queue List View

The eR<sub>X</sub> Holding Queue List columns include the patient’s name (Patient), date of birth of the patient (DOB), the prescribed drug from the external provider (Drug), the prescribing physician’s name (Provider), the status of the eR<sub>X</sub> (STA), and the date that the eR<sub>X</sub> was received by VistA (Rec Date). At any given time, 999 eR<sub>X</sub> records are displayed in the Holding Queue List View with actionable statuses of “N”, “I”, “W”, or with one of the Hold codes (H*xx* (where *x* = letter), HC), CAH, CAO, CAP, CAR, CXD, CXE, CXI, CXN, CXV, CXW, CXY, RXD, RXE, RXF, RXI, RXN, RXR, RXW, or the Inbound Error in RRE and CRE status. The records are sorted by Received Date with oldest records first. Refer to <u>Appendix B: Holding Queue Status Codes & Descriptions</u> for additional information on the various statuses in the list.

The following actions are available from the eR<sub>X</sub> Holding Queue List:

- \<SI\> Select Item can be entered to select an item in the Enter a Number prompt. Additionally, the record \# can be entered without selecting SI at the “Select Action: Next Screen//” prompt.
- \<SR\> Search Queue can be entered to search for an eR<sub>X</sub> based on a variety of search criteria.
- \<SO\> Sort Entries can be entered to sort the list.
- \<MV\> Message View can be entered to display various message types.

#### Message View

Message View, \<MV\>, is an action in the Holding Queue. When the user enters \<MV\>, the system prompts the user to select the message type. By selecting the message type, the user can view all the messages in the various statuses for the selected message type in the order of date received, with the newest records displayed first.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/005.png)

<span id="_Toc65697518" class="anchor"></span>Figure 3‑4: Message View

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

For additional information on Actionable and Non-Actionable eR<sub>X</sub> Status Codes, refer to the tables in <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

#### eR<sub>X</sub> Default Lookback Days

A new field, ERX DEFAULT LOOKBACK DAYS file (#10.2), has been added to the OUTPATIENT SITE file (#59), which contains the number of days the user would like to look back before loading the Holding Queue’s list view or completing a Search (SR) or Sort (SO). This is a configurable field that can be updated with the desired value by the local site’s VistA Admin. The addition of this new configurable field facilitates increased processing speed in the eR<sub>X</sub> Holding Queue.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/006.png)

<span id="_Toc519780526" class="anchor"></span>Figure 3‑5: eR<sub>X</sub> Default Lookback Days

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

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/007.png)

<span id="_Toc520302017" class="anchor"></span>Figure 3‑6: PT – Patient (Grouped)

2.  Select an option to filter the Patient Centric View by specific actionable status.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/008.png)

<span id="_Toc520302018" class="anchor"></span>Figure 3‑7: Patient Centric View Filters – Select by Status

While accessing the Patient Centric View, one of the following selections may be made to filter the display results by specific actionable statuses:

- \<A\> All – Patients with eR<sub>X</sub> records in all actionable statuses in the Holding Queue.
- \<1\> New – Patients with eR<sub>X</sub> records in New status in the Holding Queue. (NewRx only)
- \<2\> In Process – Patients with eR<sub>X</sub> records in In Process status in the Holding Queue.
- \<3\> Wait – Patients with eR<sub>X</sub> records in Wait status in the Holding Queue.
- \<4\> Hold – Patients with eR<sub>X</sub> records in one of the Hold statuses in the Holding Queue.
  - If \<4\> Hold is entered, \<S\> must then be selected for a single Hold status or \<A\> for all hold codes.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/009.png)

<span id="_Toc520302019" class="anchor"></span>Figure 3‑8: Patient Centric View Filters – Hold

If \<S\> is entered to filter the display results by a single Hold status, the desired Hold status to filter by must be selected.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/010.png)

<span id="_Toc520302020" class="anchor"></span>Figure 3‑9: Patient Centric View – Hold Statuses

For additional details on Hold statuses, refer to <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

> **NOTE:** The Hold status codes of the format H*xx* apply to all fillable prescriptions. However, HC applies to NewRx type only.

- \<5\> CCR – Patients with CancelRx Request and/or actionable RxRenewal Response and/or RxChange Response in the Holding Queue.
  - If \<5\> CCR is entered, \<S\> must be selected to filter for a single CCR status, or \<A\> for all actionable CCR statuses.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/011.png)

<span id="_Toc65697524" class="anchor"></span>Figure 3‑10: Patient Centric View Filter – CCR

If \<S\> is entered to filter the display results by a single CCR status, they must then select the desired CCR status to filter by.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/012.png)

<span id="_Toc65697525" class="anchor"></span>Figure 3‑11: Patient Centric View – CCR Statuses

Once a selection is made:

- If the site has not configured ERX DEFAULT LOOKBACK DAYS, a list of patients who have Actionable eR<sub>X</sub> records in the Holding Queue for the last 365 days displays. See Figure 3‑12.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/013.png)

<span id="PSO_7_567_Fig_3_12" class="anchor"></span>Figure 3‑12: Non-Configured ERX LOOK-BACK DAYS Field

- If options \<1\>, \<2\>, \<3\>, or \<4\> are selected to filter by status, a list of patients displays if the patient has Actionable eR<sub>X</sub> records under the selected status within the number of days set as the ERX DEFAULT LOOKBACK DAYS. For example, if the ERX DEFAULT LOOKBACK DAYS is set to a value of 30 and a user selected \<1\> New when filtering the Patient Centric View, the patient(s) displayed should have had a new record received within the last 30 days. See Figure 3‑13.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/014.png)

<span id="PSO_7_567_Fig_3_13" class="anchor"></span>Figure 3‑13: Configured ERX LOOK-BACK DAYS Field

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

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/015.png)

<span id="_Ref5967400" class="anchor"></span>Figure 3‑14: Patient eR<sub>X</sub> List

To view the details of an eR<sub>X</sub>, select the record number.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/016.png)

<span id="_Toc520302023" class="anchor"></span>Figure 3‑15: eR<sub>X</sub> Summary/Details Screen

Validation actions may be completed from here. If validation actions are started on NewRx message types, but not Accepted, the Status of the eR<sub>X</sub> displays as “I” for In Process. In the example below, just the patient was validated, therefore the eR<sub>X</sub> is still In Process.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/017.png)

<span id="_Ref5967413" class="anchor"></span>Figure 3‑16: eR<sub>X</sub> List with Updated Status – I

In the Patient Centric View, if an eR<sub>X</sub> status changes one actionable status to another, the eR<sub>X</sub> total remains the same, but the totals for various statuses are updated. In the example below, the second record displays 17 NewRxes and 3 eR<sub>X</sub>es that are In Process, and a total of 35 eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/018.png)

<span id="_Ref5967421" class="anchor"></span>Figure 3‑17: Patient Centric View

If an eR<sub>X</sub> status changes from New to In Process, the numbers for the various statuses are updated while the eR<sub>X</sub> total remains the same, as seen in the second record in the example below. There are now 16 NewRxes, 4 eR<sub>X</sub>es In Process, and still a total of 35 eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/019.png)

<span id="_Ref5967490" class="anchor"></span>Figure 3‑18: Patient Centric View – Updated Actionable Status to another Actionable Status

In the Patient Centric View, if an eR<sub>X</sub> status changes an actionable Status to a non-actionable status, the eR<sub>X</sub> total decreases by one and the totals for various statuses are also updated. In the example below, the record in the second row, the WT column has updated from 1 eR<sub>X</sub>es to 0 eR<sub>X</sub>es, therefore updating the total column from 35 to 34.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/020.png)

<span id="_Ref5967502" class="anchor"></span>Figure 3‑19: Patient Centric View Total Updated

### eR<sub>X</sub> Holding Queue Summary/Details Screen NewRx Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A record from the eR<sub>X</sub> Holding Queue List View can be selected by both typing \<SI\> and the record number or by typing the record number itself. The first screen displayed is the Summary/Details screen, which displays information about the original eR<sub>X</sub> from the external provider and matched VistA information (if any).

On this screen, the header contains the eR<sub>X</sub> Patient Name and eR<sub>X</sub> Reference \#, which is an internal VA reference number assigned for tracking the eR<sub>X</sub>. Below the header is information received from the external provider for the patient, provider, and the drug/SIG. Where applicable, VistA information displays below the eR<sub>X</sub> information.

> **NOTE:** - “eRx Written Date” – Date the eR<sub>X</sub> was received in the VistA Holding Queue.

- “eRx Issue Date” – Effective Date, if sent by the provider.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/021.png)

<span id="_Toc520302028" class="anchor"></span>Figure 3‑20: Summary/Details Screen Page 1

Press \<Enter\> to display Page 2 of the Summary/Details screen, which contains eR<sub>X</sub> Notes, applicable Allergy information, and Diagnosis information.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/022.png)

<span id="_Toc520302029" class="anchor"></span>Figure 3‑21: Summary/Details Screen Page 2

If the VistA information for the patient, provider, or drug is not linked, the display is as shown below:

- VistA Patient: NOT LINKED
- VistA Provider: NOT LINKED
- VistA Drug: NOT LINKED

VistA information displayed includes allergies. If the patient has no known allergies, “NKA” displays in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/023.png)

<span id="_Toc520302030" class="anchor"></span>Figure 3‑22: Patient with No Known Allergies

If the VistA patient has known allergies, verified allergies display in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/024.png)

<span id="_Toc520302031" class="anchor"></span>Figure 3‑23: VistA Patient with Known Allergies

#### eR<sub>X</sub> Actions

- Manual Validation:
  - \<VP\> [Validate Patient](#_Validate_Patient)
  - \<VM\> [Validate Provider](#_Validate_Provider)
  - \<VD\> ([Validate Drug/SIG](#_Validate_Drug/SIG)) - Note that this action is not available unless a VistA patient has been linked, as indicated with parenthesis around the action.
- \<AC\> Accepting eR<sub>X</sub>es in the eRX Holding Queue action is not available until the validation of the eR<sub>X</sub> Patient, provider, and drug/SIG have been completed. Also note that the \<AC\> action is not available if the eR<sub>X</sub> is on Hold.
- \<RJ\> Rejecting an eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue removes the eR<sub>X</sub> from the main list display and prevents further processing of the eR<sub>X.</sub>
- \<P\> Printing in the eR<sub>X</sub> Holding Queue displays all details of an eR<sub>X</sub> and allows the user to select a local printer and print the eR<sub>X.</sub>
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
3.  The VistA Patient is already matched to an eR<sub>X</sub> Patient under the Validate Patient \<VP\> action.
4.  The matched VistA Patient has a current pending line entry on the Outpatient side.

To use the Jump to OP action, enter \<??\> to view a list of hidden actions.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/025.png)

<span id="_Toc520302032" class="anchor"></span>Figure 3‑24: Jump to OP – Hidden Action

Enter the hidden Jump to OP \<JO\> action.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/026.png)

<span id="_Toc520302033" class="anchor"></span>Figure 3‑25: JO Action Selected

If a user attempts to Jump to OP \<JO\> when a VistA Patient is not matched to an eR<sub>X</sub> Patient, an error message is received stating, “VistA patient has not been matched. Cannot jump to outpatient”.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/027.png)

<span id="_Toc520302034" class="anchor"></span>Figure 3‑26: JO Error – VistA Patient Not Matched

If a user attempts to Jump to OP \<JO\> from an eR<sub>X</sub> record that is not a fillable prescription, an error message is received stating, “Jumping can only be done on ‘NewRx’ messages, Renewal Response-Replace and fillable RxChange Response messages”.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/028.png)

<span id="_Toc520302035" class="anchor"></span>Figure 3‑27: JO Error – Fillable eR<sub>X</sub> Messages Only

Once the user has completed reviewing on the Outpatient side, upon selecting \<Enter\> at the “Select Patient:” prompt, the user is navigated back to the same Summary/Details screen in which \<JO\> was initiated from.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/029.png)

<span id="_Toc65697542" class="anchor"></span>Figure 3‑28: JO “Select Patient” – Jump Back to Holding Queue eR<sub>X</sub> Summary/Details Screen

#### Status History

The Status History \<SH\> hidden action displays the history of status changes on an eR<sub>X</sub> record within the Holding Queue. It does not include the initial status of the record.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/030.png)

<span id="_Toc65697543" class="anchor"></span>Figure 3‑29: Status History – Hidden Action

Enter the hidden Status History \<SH\> action to display the history of status changes.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/031.png)

<span id="_Toc65697544" class="anchor"></span>Figure 3‑30: SH Action - Status Changes on eR<sub>X</sub> Record in Holding Queue

Comments are displayed where applicable (i.e. Hold, RJ, and RM statuses).

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/032.png)

<span id="_Toc65697545" class="anchor"></span>Figure 3‑31: Status History with Comment for Rejected eR<sub>X</sub>

#### eR<sub>X</sub> Change Request

eR<sub>X</sub> Change Request \<EC\> hidden action is used to request change on a NewRx prescription from the external Provider who sent the original NewRx. For detailed information about RxChange Request, refer to <u>Unit 5 - RxChange Requests and Responses</u>.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/033.png)

<span id="_Toc65697546" class="anchor"></span>Figure 3‑32: eR<sub>X</sub> Change Request

#### Patient-Level Record Lock

Note that when either the Summary/Details screen or any of the validate screens of an eR<sub>X</sub> are open, all the eR<sub>X</sub>es for that same patient in the Holding Queue are locked and inaccessible for other users to access until the lock is released (the screens are closed). This is referred to as a patient-level record lock.

The following message displays if a user attempts to access an eR<sub>X</sub> for the same patient that another user has opened.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/034.png)

<span id="_Toc65697547" class="anchor"></span>Figure 3‑33: Patient-Level Record Lock

#### Prohibit Renewals

The Prohibit Renewal Request flag is used to denote that a RxRenewal Request should not be sent to the sending prescriber for an original NewRx or a subsequent fillable RxChange Response when the flag is set on the original NewRx. This is usually used when the visit is for a one time prescription (i.e., Urgent Care Center or Emergency Department).

> **NOTE:** \(i\) The Prohibit Renewal Request information is not displayed for RxRenewal Request and Response records.

\(ii\) The Prohibit Renewal Request information is displayed both in VistA and on web GUI under Track/Audit details screen, whenever it is sent on the inbound NewRx record.

![](inbound-eprescribing-user-manual-unit-3-part-1-pso-7-581/035.png)

<span id="_Toc65697548" class="anchor"></span>Figure 3‑34: Prohibit Renewal Request

### From: Inbound ePrescribing User Manual (Unit 4 Part 2) PSO*7*581

### Denied, New Prescription to Follow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Denied New Prescription to Follow (DNTF). This indicates the renewal is denied, but a NewRx will follow.
When a RxRenewal Response message type is Denied NewRx to Follow (DNTF), it will display in the List View screen. It can also be found using \<MV\> Message View or \<SR\> Search. The status of the DNTF RxRenewal Response will be “RXD” (RxRenewal Response Denied/DNTF).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/013.png)
<span id="_Toc56761113" class="anchor"></span>Figure ‑: RXD Status in the Holding Queue List View
The RxRenewal Response details display the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/014.png)
<span id="_Toc56761114" class="anchor"></span>Figure ‑: RxRenewal Response Denied/DNTF Details Screen
In the below figure, the RxRenewal Response Information segment indicates the RxRenewal Response Message type is Denied, New Prescription to Follow.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/015.png)
<span id="_Toc56761115" class="anchor"></span>Figure ‑: RxRenewal Response Information Section
On the Outpatient side, the eR<sub>X</sub> Prescription on which the renewal was requested is auto-Discontinued (auto-DC).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/016.png)
<span id="_Toc56761116" class="anchor"></span>Figure ‑: Medication Profile – eR<sub>X</sub> After DNTF RxRenewal Response
The Activity Log on the OP side is updated to display that the eR<sub>X</sub> Prescription has been auto-Discontinued.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/017.png)
<span id="_Toc56761117" class="anchor"></span>Figure ‑: Activity Log 1
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/018.png)
<span id="_Toc56761118" class="anchor"></span>Figure ‑: Activity Log 2
Once the DNTF RxRenewal Response has successfully auto-Discontinued the eR<sub>X</sub> Prescription in OP, the status of the RxRenewal Response in the Holding Queue continues to display as “RXD” (RxRenewal Response Denied/DNTF).
The status of the corresponding RxRenewal Request will change to “RRP” (RxRenewal Request Processed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/019.png)
<span id="_Toc56761119" class="anchor"></span>Figure ‑: RRP Status in the Holding Queue
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type.

#### RxRenewal Response Failed (RXF)

RxRenewal Response Failed (RXF) is an actionable status used for the RxRenewal Response types Approved, Approved with Changes, and Denied NewRx to Follow (DNTF) if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a DNTF RxRenewal Response is attempting to auto-Discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxRenewal Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a DNTF RxRenewal Response is sent for the prescription.
> **NOTE:** Additional RXF scenarios are as follows:
RXF applies to Approved, Approved with Changes and Denied NewRx to Follow response types only.
1.  When a user selects an active eR<sub>X</sub> from OP that has an outstanding RxRenewal Request and locks it, and at the same time an Approved or Approved with Changes RxRenewal Response is received, a new pending line entry for that response is added in OP.
2.  When a RxRenewal Request is sent out for a prescription and it is manually discontinued before receiving a response, if an Approved or Approved with Changes RxRenewal Response is received, a new pending line entry for that response is added in OP.
3.  When a user selects an active eR<sub>X</sub> from OP in Backdoor Orders that has an outstanding RxRenewal Request and locks it, and at the same time a DNTF RxRenewal Response is received, the Prescription gets auto-Discontinued and the corresponding Response is marked as “RXD” in the Holding Queue. However, if the record is locked in Edit mode in Backdoor Orders, the response fails to auto-Discontinue and is marked as “RXF” in the Holding Queue.
4.  When a RxRenewal Request is sent out for a prescription, and it is renewed within VA, the prescription becomes a non-electronic prescription. If an Approved RxRenewal Response is then received, no pending line entry is added in OP. The VA Order (non-eR<sub>X</sub>) is not modified by the response. The response is marked as “RXN” in the Holding Queue.
5.  When a RxRenewal Request is sent out for a prescription and it is renewed within VA, the prescription becomes a non-electronic prescription. If a DNTF RxRenewal Response is then received, the VA Order (non-eR<sub>X</sub>) is not auto-Discontinued by the response. The response is marked as “RXD” in the Holding Queue.

### Denied

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Denied. This indicates the renewal request is denied.
When a RxRenewal Response – Denied type is received in the Holding Queue, it is displayed in the List View in “RXD” status (RxRenewal Response Denied/DNTF).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/020.png)
<span id="_Toc38526989" class="anchor"></span>Figure ‑: RXD Status in the Holding Queue List View
Select the record to view the RxRenewal Response details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/021.png)
<span id="_Toc38526990" class="anchor"></span>Figure ‑: RxRenewal Response Details Screen – Denied
As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Denied.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/022.png)
<span id="_Toc38526991" class="anchor"></span>Figure ‑: RxRenewal Response Information Section
There is no user intervention required on the Denied RxRenewal Response other than acknowledging the response. For more information on how to acknowledge a record in actionable status, refer to section <u>4.9 Acknowledge: Hidden Action for RxRenewal Response/Inbound Error</u>.
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

### Replace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Replace is one of the RxRenewal Response types introduced with NCPDP 2017071 which displays in the Holding Queue List View screen as an actionable entry. It can also be found using \<MV\> Message View or \<SR\> Search. The status of the Replace Response is “RXR” (RxRenewal Response Replace - New).
Replace is used as a fillable prescription which is sent to replace an original NewRx on which the renewal was requested. When a Replace type Response is received, the original is discontinued in Outpatient Pharmacy and the Replace response is to be treated exactly the same way as a NewRx wherein the pharmacy user would exercise actions such as \<VP\>, \<VM\>, \<VD\> and so on.
> **NOTE:** The workflow of a Replace type Response is very similar to that of a NewRx record. For complete details about how to process a NewRx record, refer to section <u>3.6 Manual Validation</u>.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/023.png)
<span id="_Toc56761123" class="anchor"></span>Figure ‑: RXR Status in Holding Queue List View
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/024.png)
<span id="_Toc56761124" class="anchor"></span>Figure ‑: eR<sub>X</sub> record discontinued in Outpatient
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/025.png)
<span id="_Toc56761125" class="anchor"></span>Figure ‑: Activity Log of eR<sub>X</sub> record discontinued in Outpatient 1
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/026.png)
<span id="_Toc56761126" class="anchor"></span>Figure ‑: Activity Log of eR<sub>X</sub> record discontinued in Outpatient 2
The RxRenewal Response details screen displays the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/027.png)
<span id="_Toc56761127" class="anchor"></span>Figure ‑: RxRenewal Response - Replace Details Screen
As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Replace.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/028.png)
<span id="_Toc56761128" class="anchor"></span>Figure ‑: RxRenewal Response - Replace Information Section
When a user takes any action on the “RXR” record in the Holding Queue, the status of the record changes to “RXI”, which indicates that the record is in process.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/029.png)
<span id="_Toc56761129" class="anchor"></span>Figure ‑: RXI Status in the Holding Queue
The user may select the record to view the RxRenewal Response Details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/030.png)
<span id="_Toc56761130" class="anchor"></span>Figure ‑: RXI – Summary/Details screen
When the user completes accepting the validation of Patient, Provider and Drug sections on the Replace type response, the status changes to “RXW”, indicating that the record is now in waiting status.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/031.png)
<span id="_Toc56761131" class="anchor"></span>Figure ‑: RXW Status in the Holding Queue
The user may select the record to view the RxRenewal Response Details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/032.png)
<span id="_Toc56761132" class="anchor"></span>Figure ‑: RXW – Summary/Details screen
When the user accepts the RxRenewal Response record using \<AC\>, the status of the record changes to “RXP” (RxRenewal Response Processed), and it is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/033.png)
<span id="_Toc56761133" class="anchor"></span>Figure ‑: RXP Status in Holding Queue
On the OP side, a pending line entry is added for the user to finish the Replace RxRenewal Response.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/034.png)
<span id="_Toc56761134" class="anchor"></span>Figure ‑: Medication Profile – Pending Line Entry
The user may select the pending line entry to finish the Replace RxRenewal Response and accept it. The Replace RxRenewal Response is now an active prescription which displays in the Active section of the Medication profile.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/035.png)
<span id="_Toc56761135" class="anchor"></span>Figure ‑: Replace Response to an active R<sub>X</sub> in Active Section of the Medication Profile
Once the Replace RxRenewal Response becomes an active prescription, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/036.png)
<span id="_Toc56761136" class="anchor"></span>Figure ‑: RXC Status in the Holding Queue
Select the record to view the RxRenewal Response details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/037.png)
<span id="_Toc56761137" class="anchor"></span>Figure ‑: RxRenewal Response Details Screen
The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/038.png)
<span id="_Toc56761138" class="anchor"></span>Figure ‑: RRC Status in the Holding Queue
Select the record to view the RxRenewal Request details screen.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/039.png)
<span id="_Toc56761139" class="anchor"></span>Figure ‑: RxRenewal Request Details Screen
The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type. Similar to the status change with other RxRenewal Response types, in case of Replace the corresponding RxRenewal Request record transitions from RRN, RRR, RRP to RRC. For more information about RxRenewal Request status codes, refer to <u>Table 20: Holding Queue Status Codes & Descriptions for RxRenewal Request Message Type</u> in <u>Appendix B: Holding Queue Status Codes & Descriptions</u>.

#### RxRenewal Response – Processing Error (RXE)

RxRenewal Response – Processing Error (RXE) is an actionable status used for Replace RxRenewal Responses if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a Replace RxRenewal Response is attempting to auto-Discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxRenewal Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a Replace RxRenewal Response is sent for the prescription.
When a Replace RxRenewal Response record is in “RXE” status, the user can still process the record similar to a NewRx record after manually canceling the original in Outpatient Pharmacy. The status codes for Replace RxRenewal Response workflow is covered in Table 21.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/040.png)
<span id="_Toc56761140" class="anchor"></span>Figure ‑: RXE Status in Holding Queue List View
The RxRenewal Response details section displays the RxRenewal Response Message type.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/041.png)
<span id="_Toc56761141" class="anchor"></span>Figure ‑: RxRenewal Response - Replace Details Screen for RXE
When the user exercises one of the available actions, a warning displays that the corresponding OP record may not have been auto-Discontinued. The user is prompted to select Yes or No. Upon selecting Yes, the status of the record changes to “RXI”. Upon selecting No, the record remains in “RXE” status.
![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/042.png)
<span id="_Toc56761142" class="anchor"></span>Figure ‑: Replace Response Processing Error Warning Text/Prompt
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

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/043.png)

<span id="_Toc56761143" class="anchor"></span>Figure ‑: Add Comments

2.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/044.png)

<span id="_Toc56761144" class="anchor"></span>Figure ‑: RxRenewal Request Comments

The user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

3.  Type action \<AD\>.
4.  Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/045.png)

<span id="_Toc56761145" class="anchor"></span>Figure ‑: Replacing RxRenewal Request Comments

5.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/046.png)

<span id="_Toc56761146" class="anchor"></span>Figure ‑: RxRenewal Request Comments Updated

## Acknowledge: Hidden Action for RxRenewal Response/Inbound Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user completes reviewing a Denied or a Denied, NewRx to Follow RxRenewal Response message in the Holding Queue List View, the user can exercise the \<ACK\> Acknowledge Hidden action to remove the message from the list view. The resulting acknowledged message can be retrieved using \<MV\> Message View or \<SR\> Search. Acknowledge is also enabled for RxRenewal Responses that fail to auto-process and are in status of “RXF” and the Inbound Errors with status “RRE”. When a RxRenewal Response – Denied or Denied NewRx to Follow type is received in the Holding Queue, it is displayed in the list view, and is in the actionable “RXD” status.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/047.png)

<span id="_Toc56761147" class="anchor"></span>Figure ‑: RXD Status in the Holding Queue List View

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/048.png)

<span id="_Toc56761148" class="anchor"></span>Figure ‑: RxRenewal Response Denied/DNTF Details Screen

The user may type \<ACK\> at the prompt to acknowledge the RxRenewal Response message.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/049.png)

<span id="_Toc56761149" class="anchor"></span>Figure ‑: Acknowledge RxRenewal Response Message

Once the user selects Yes at the prompt, the status of the message is changed from “RXD” to “RXA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/050.png)

<span id="_Toc56761150" class="anchor"></span>Figure ‑: RXA Status in the Holding Queue

Select the record to view the RxRenewal Response details screen, displaying the eR<sub>X</sub> status of RxRenewal Response Acknowledged.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/051.png)

<span id="_Toc56761151" class="anchor"></span>Figure ‑: RxRenewal Response Acknowledged Details Screen

> **NOTE:** When the user acknowledges a RxRenewal Response with a status of “RXF”, it changes to “RXA”. The workflow is the same as “RXD” to “RXA”.

When a RxRenewal Request results in an Inbound Error with the status “RRE”, it is displayed in the list view as an actionable entry.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/052.png)

<span id="_Toc56761152" class="anchor"></span>Figure ‑: RRE Status in the Holding Queue List View

Select the record to view the Inbound Error details screen, displaying an eR<sub>X</sub> status of RxRenewal Request Error.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/053.png)

<span id="_Toc56761153" class="anchor"></span>Figure ‑: RxRenewal Request Error Details Screen

The user may type \<ACK\> Acknowledge at the prompt to acknowledge the RxRenewal Response message.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/054.png)

<span id="_Toc56761154" class="anchor"></span>Figure ‑: Acknowledge Action

Once the user selects Yes at the prompt, the status of the message is changed from “RRE” to “IRA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/055.png)

<span id="_Toc56761155" class="anchor"></span>Figure ‑: IRA Status in the Holding Queue

Select the record to view the Inbound Error details screen, with an eR<sub>X</sub> status of Inbound RxRenewal Request Error Acknowledged.

![](inbound-eprescribing-user-manual-unit-4-part-2-pso-7-581/056.png)

<span id="_Toc56761156" class="anchor"></span>Figure ‑: Inbound Error Details Screen – Inbound RxRenewal Request Error Acknowledged

### From: Inbound ePrescribing User Manual (Unit 5 Part 2) PSO*7*581

## RxChange Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user selects the RxChange Response from the eR<sub>X</sub> Holding Queue, the RxChange Response details display in the Message Details View. It displays the content of the RxChange Response, along with the relation to the RxChange Request message, and the original NewRx message.

### Fillable RxChange Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/002.png)

<span id="_Toc56761185" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Message Details – Approved (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/003.png)

<span id="_Toc56761186" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information – Approved (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/004.png)

<span id="_Toc56761187" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Message Details – AwC (D, G, T, S and OS Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/005.png)

<span id="_Toc56761188" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information – AwC (D, G, T, S and OS Request Types )

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/006.png)

<span id="_Toc56761189" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Message Details – Validated (U Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/007.png)

<span id="_Toc56761190" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information – Validated (U Request Type)

> **NOTE:** When Prohibit Renewal Request flag is sent on an original NewRx, it is carried forward into the subsequent fillable RxChange Response and is displayed in the Message Details View. It is not displayed for a non-fillable RxChange Response.

### Non-fillable RxChange Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/008.png)

<span id="_Toc56761191" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Message Details – Approved (P Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/009.png)

<span id="_Toc56761192" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information – Approved (P Request Type)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/010.png)

<span id="_Toc56761193" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Message Details – Denied (All Request Types)

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/011.png)

<span id="_Toc56761194" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information – Denied (All Request Types)

For all types of change responses, the Message History section links the RxChange Request Reference Number to the RxRenewal Response and to the Original NewRx message.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/012.png)

<span id="_Toc56761195" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Request Information and Message History

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

> **NOTE:** The workflow of a fillable change response is very similar to that of a NewRx record. For complete details about how to process a NewRx record, refer to section <u>Error! Reference source not found.Error! Reference source not found.</u>.

For the sake of training, a full life cycle of fillable Approved RxChange Response will be discussed further.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/013.png)

<span id="_Toc56761196" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXN Status in Holding Queue List View

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/014.png)

<span id="_Toc56761197" class="anchor"></span>Figure Error! No text of specified style in document.‑: Original eR<sub>X</sub> record auto-canceled in Holding Queue

The RxChange Response details displays the RxChange Response Message type.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/015.png)

<span id="_Toc56761198" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response - Approved (fillable) Details Screen

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Replace.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/016.png)

<span id="_Toc56761199" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response - Approved (fillable) Information Section

When a user takes any action on the CXN/CXV record in the Holding Queue, the status of the record changes to CXI, which indicates that the record is in process.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/017.png)

<span id="_Toc56761200" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXI Status in the Holding Queue

The user may select the record to view the fillable RxChange Response Details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/018.png)

<span id="_Toc56761201" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXI – Summary/Details screen

When the user completes accepting the validation of Patient, Provider and Drug on the fillable change response, the status changes to CXW, indicating that the record is now in waiting status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/019.png)

<span id="_Toc56761202" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXW Status in the Holding Queue

The user may select the record to view the RxChange Response Details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/020.png)

<span id="_Toc56761203" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXW – Summary/Details screen

When the user accepts the RxChange Response record using \<AC\>, the status of the record changes to “CXP” (RxChange Response Processed), and it is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/021.png)

<span id="_Toc56761204" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXP Status in Holding Queue

On the Outpatient side, a pending line entry is added for the user to finish the RxChange Response.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/022.png)

<span id="_Toc56761205" class="anchor"></span>Figure Error! No text of specified style in document.‑: Medication Profile – Pending Line Entry

The user may select the pending line entry to finish the RxChange Response and accept it.

RxChange Response is now an active prescription, which displays in the Active section of the Medication Profile.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/023.png)

<span id="_Toc56761206" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response to an active R<sub>X</sub> in Active Section of the Medication Profile

Once the RxChange Response becomes an active prescription, the status of the RxChange Response in the Holding Queue changes to CXC (RxChange Response Completed).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/024.png)

<span id="_Toc56761207" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXC Status in the Holding Queue

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/025.png)

<span id="_Toc56761208" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Details Screen

The status of the corresponding RxChange Request changes to CRC (RxChange Request Completed).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/026.png)

<span id="_Toc56761209" class="anchor"></span>Figure Error! No text of specified style in document.‑: CRC Status in the Holding Queue

Select the record to view the RxChange Request details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/027.png)

<span id="_Toc56761210" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Request Details Screen

The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

The status of a RxChange Request record transitions from CRN, CRR, CRP to CRC. For more information about RxChange Request status codes, refer to <u>Error! Reference source not found.</u> in <u>Error! Reference source not found.Error! Reference source not found.</u>.

#### RxChange Response – Processing Error (CXE)

RxChange Response – Processing Error (CXE) is an actionable status used for fillable RxChange Responses if a failure occurs. One scenario is when a patient’s Outpatient Profile record is locked in OERR and a fillable RxChange Response is attempting to auto-discontinue an eR<sub>X</sub> record at the same time. Another scenario is when a RxChange Request is sent out for a prescription, and it is manually discontinued before a response is received. Then, a fillable RxRenewal Response is sent for the prescription.

When a fillable RxRenewal Response record is in CXE status, the user can still process that record similar to a NewRx record after manually canceling the original in the Holding Queue and in Outpatient Pharmacy (if a record exists).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/028.png)

<span id="_Toc56761211" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXE Status in Holding Queue List View

The RxChange Response details displays the RxRenewal Response Message type.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/029.png)

<span id="_Toc56761212" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response - Message Details Screen for CXE

When the user exercises one of the available actions, a warning is displayed that the corresponding HQ/OP record may not have been auto-canceled/auto-discontinued. The user is prompted to select Yes or No. Upon selecting Yes, the status of the record changes to CXI. Upon selecting No, the record remains in CXE status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/030.png)

<span id="_Toc56761213" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Processing Error Warning Text/Prompt

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

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/031.png)

<span id="_Toc56761214" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXY Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/032.png)

<span id="_Toc56761215" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Details Screen – Approved for P Request Type

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Approved.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/033.png)

<span id="_Toc56761216" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information Section

There is no user intervention required on the Approved RxChange Response (for P Request Type), other than acknowledging. For more information on how to acknowledge a record in actionable status, refer to section <u>5.9 Acknowledge: Hidden Action for RxChange Response/Inbound Error</u>.

The \<VP\>, \<VM\>, \<VD\>, \<Hold\>, \<UnHold\>, \<RJ\>, \<RM\>, and \<AC\> actions are in parentheses ( ), therefore the user cannot select these actions for this message type.

#### Denied RxChange Response for all Request Types

Another RxChange Response message type is Denied. This indicates the change request is denied. This response applies to all request types.

When a RxChange Response – Denied type is received in the Holding Queue, it is displayed in the List View in “CXD” status (RxChange Response Denied).

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/034.png)

<span id="_Toc56761217" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXD Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/035.png)

<span id="_Toc56761218" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Details Screen – Denied

As the user continues to scroll, the RxChange Response Information section indicates the RxChange Response Message type is Denied.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/036.png)

<span id="_Toc56761219" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Information Section

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

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/037.png)

<span id="_Toc56761220" class="anchor"></span>Figure Error! No text of specified style in document.‑: Add Comments

2.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/038.png)

<span id="_Toc56761221" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Request Comments

The user who made the comment displays in the “Comments By” field and the date/time the comments were made display in the “Comments Date/Time” field. Users can replace the comments with updated comments. When comments are replaced, the last user who made comments displays in the “Comments By” field and the date/time the comments were updated display in the “Comments Date/Time” field. To update or replace comments:

3.  Type action \<AD\>.
4.  Replace with updated comments.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/039.png)

<span id="_Toc56761222" class="anchor"></span>Figure Error! No text of specified style in document.‑: Replacing RxChange Request Comments

5.  Select \<Enter\>.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/040.png)

<span id="_Toc56761223" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Request Comments Updated

## Acknowledge: Hidden Action for RxChange Response/Inbound Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user completes reviewing an Approved for Prior Authorization Request or a Denied RxChange Response message in the Holding Queue’s list view, the user can exercise \<ACK\> Acknowledge Hidden action to remove the message from the list view. The resulting acknowledged message can be retrieved using \<MV\> Message View or \<SR\> Search. Acknowledge is also enabled for the Inbound Errors with status CRE. When a RxChange Response – Denied type is received in the Holding Queue, it is displayed in the list view, and is in the actionable “CXD” status. When a RxChange Response – Approved type for Prior Authorization request is received in the Holding Queue, it is displayed in the list view, and is in the actionable “CXY” status.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/041.png)

<span id="_Toc56761224" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXD Status in the Holding Queue List View

Select the record to view the RxChange Response details screen.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/042.png)

<span id="_Toc56761225" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Denied Details Screen

The user may type \<ACK\> at the prompt to acknowledge the RxChange Response message.

Once the user selects Yes at the prompt, the status of the message is changed from “CXD” to “CXA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/043.png)

<span id="_Toc56761226" class="anchor"></span>Figure Error! No text of specified style in document.‑: CXA Status in the Holding Queue

Select the record to view the RxChange Response details screen, displaying the eR<sub>X</sub> status of RxChange Response Acknowledged.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/044.png)

<span id="_Toc56761227" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Response Acknowledged Details Screen

> **NOTE:** When the user acknowledges a RxChange Response with a status of “CXY”, it changes to “CXA”. The workflow is the same as “CXD” to “CXA”.

When a RxChange Request results in an Inbound Error with the status “CRE”, it is displayed in the list view as an actionable entry.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/045.png)

<span id="_Toc56761228" class="anchor"></span>Figure Error! No text of specified style in document.‑: CRE Status in the Holding Queue List View

Select the record to view the Inbound Error details screen, displaying an eR<sub>X</sub> status of RxChange Request Error.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/046.png)

<span id="_Toc56761229" class="anchor"></span>Figure Error! No text of specified style in document.‑: RxChange Request Error Details Screen

The user may type \<ACK\> Acknowledge at the prompt to acknowledge the RxChange Response message.

Once the user selects Yes at the prompt, the status of the message is changed from “CRE” to “ICA” and the message is not displayed in the list view. It can be found using \<MV\> Message View or \<SR\> Search.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/047.png)

<span id="_Toc56761230" class="anchor"></span>Figure Error! No text of specified style in document.‑: ICA Status in the Holding Queue

Select the record to view the Inbound Error details screen, with an eR<sub>X</sub> status of Inbound RxChange Request Error Acknowledged.

![](inbound-eprescribing-user-manual-unit-5-part-2-pso-7-581/048.png)

<span id="_Toc56761231" class="anchor"></span>Figure Error! No text of specified style in document.‑: Inbound Error Details Screen – Inbound RxChange Request Error Acknowledged

### From: Inbound ePrescribing User Manual (Unit 4 Part 1) PSO*7*581

## Generate R<sub>X</sub>Renewal Requests from Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To generate a RxRenewal Request, navigate to the patient’s Medication Profile in Complete Orders from OERR or Patient Prescription Processing. The Medication Profile displays all of the R<sub>X</sub>es associated with the patient. To generate a RxRenewal Request:

1.  Select the eR<sub>X</sub>.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/002.png)

<span id="_Toc65771150" class="anchor"></span>Figure 4‑1: Select R<sub>X</sub> from Medication Profile

1.  Type \<Other\> to display additional actions.
2.  Select \<RR\> RxRenewal Request.
3.  Indicate \<R\> Refill with Pre-Populated Value or \<C\> Refill and Change Quantity.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/003.png)

<span id="_Toc65771151" class="anchor"></span>Figure 4‑2: Generating RxRenewal Request Actions

4.  Enter \<Yes\> to send the renewal request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/004.png)

<span id="_Toc65771152" class="anchor"></span>Figure 4‑3: RxRenewal Request Sent

> **NOTE:** When an Outbound RxRenewal Request is sent, if the user requested “n” as the number of renewals using either option “R” or option “C”, the NCPDP 2017071 RxRenewal Request message with a value of “n+1” is sent to the Provider.

The user is allowed to generate and send more than one RxRenewal Request for the same eR<sub>X</sub>. The history of all the requests sent, along with any responses or errors received within the last 30 days, is displayed at the time of generating a duplicate request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/005.png)

<span id="_Toc65771153" class="anchor"></span>Figure 4‑4: RxRenewal Request History

The RxRenewal Request generated in Outpatient Profile and sent by the Pharmacy user can be found in the Holding Queue in the Message View, displaying a status of “RRN” (RxRenewal Request - New).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/006.png)

<span id="_Toc65771154" class="anchor"></span>Figure 4‑5: RRN in Holding Queue

### RxRenewal Request Precondition Checks and Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of RxRenewal Request warnings that may display at the time of the outbound RxRenewal Request. For example, a warning displays when \<RR\> is being used on a non-eR<sub>X</sub> prescription.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/007.png)

<span id="_Toc65771155" class="anchor"></span>Figure 4‑6: RxRenewal Request Warning

A complete list of RxRenewal Request Warnings can be found in <u>Error! Reference source not found.Error! Reference source not found..</u>

## RxRenewal Requests in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outbound RxRenewal Request messages sent from VistA Outpatient Profile are stored in the Holding Queue. They can be viewed using search criteria or in the \<MV\> Message View action. To view a RxRenewal Request:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<RR\> RxRenewal Request.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/008.png)

<span id="_Toc65771156" class="anchor"></span>Figure 4‑7: Message View Action and RxRenewal Request

The Holding Queue displays all RxRenewal Request messages, sorted by received date in descending order (newest requests first).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/009.png)

<span id="_Toc65771157" class="anchor"></span>Figure 4‑8: Message View Displaying RxRenewal Request Messages

The RxRenewal Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue. For RxRenewal Request statuses, refer to <u>Error! Reference source not found.</u> in <u>Error! Reference source not found.Error! Reference source not found.</u>.

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

RxRenewal Responses that are in actionable statuses are displayed in the Holding Queue’s list view. For the full list of RxRenewal Response statuses, refer to <u>Error! Reference source not found.</u> in <u>Error! Reference source not found.Error! Reference source not found.</u>.

To view a RxRenewal Response in the Holding Queue:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<RE\> RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/010.png)

<span id="_Toc65771158" class="anchor"></span>Figure 4‑9: Message View Action

The eR<sub>X</sub> Holding Queue screen displays all RxRenewal Response messages, sorted by received date in descending order (newest responses first).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/011.png)

<span id="_Toc65771159" class="anchor"></span>Figure 4‑10: Holding Queue Displaying RxRenewal Response Messages

## RxRenewal Request Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may view the message details in the Message Details view by selecting the RxRenewal Request message to be displayed from the Holding Queue.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/012.png)

<span id="_Toc65771160" class="anchor"></span>Figure 4‑11: RxRenewal Request – New

See more message details below.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/013.png)

<span id="_Toc65771161" class="anchor"></span>Figure 4‑12: RxRenewal Request Medication Dispensed and RxRenewal Request Information

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/014.png)

<span id="_Toc65771162" class="anchor"></span>Figure 4‑13: RxRenewal Request Message History

The Message History segment displays the message history with a reference to the original R<sub>X</sub>. The RxRenewal Request Reference \# field displays a “V”, indicating that this was generated from VistA.

## RxRenewal Response Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user selects the RxRenewal Response from the eR<sub>X</sub> Holding Queue, the RxRenewal Response details display in the Message Details View. The Message Details View displays the content of the RxRenewal Response, along with the relation to the RxRenewal Request message, and the original NewRx message.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/015.png)

<span id="_Toc65771163" class="anchor"></span>Figure 4‑14: RxRenewal Response Message Details

> **NOTE:** When an Inbound RxRenewal Response is received, if the provider approved “n” as the number of renewals, the Message Details view displays “n-1” as the number of renewals approved. This is applicable to Approved, Approved with Changes, and Replace RxRenewal Response Types.

The RxRenewal Response Information section contains the RxRenewal Response message type along with the response date and time and any additional notes and comments.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/016.png)

<span id="_Toc65771164" class="anchor"></span>Figure 4‑15: RxRenewal Response Information 2

The Message History section links the RxRenewal Request reference number to the RxRenewal Response and the original NewRx message.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/017.png)

<span id="_Toc65771165" class="anchor"></span>Figure 4‑16: RxRenewal Request Information and Message History

## RxRenewal Response Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Approved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxRenewal Response message type is Approved, it is not displayed in the List View screen. It can be found using \<MV\> Message View or \<SR\> Search. The status of the Approved RxRenewal Response is “RXP” (RxRenewal Response Processed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/018.png)

<span id="_Toc65771166" class="anchor"></span>Figure 4‑17: Message View and RxRenewal Response Actions

The details of the RxRenewal Response display the RxRenewal Response Message type. In Figure 4‑18, the RxRenewal Response Information segment shows the RxRenewal Response Message type is Approved.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/019.png)

<span id="_Ref52553559" class="anchor"></span>Figure 4‑18: RxRenewal Response – Approved

When the user continues to scroll, the RxRenewal Response Information section displays.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/020.png)

<span id="_Toc65771168" class="anchor"></span>Figure 4‑19: RxRenewal Response Information Section

On the OP side, a pending line entry is available for the user to renew the Approved RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/021.png)

<span id="_Toc65771169" class="anchor"></span>Figure 4‑20: Medication Profile – Pending Line Entry

The Activity Log on the OP side shows that a pending response entry was added.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/022.png)

<span id="_Toc65771170" class="anchor"></span>Figure 4‑21: Activity Log 1

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/023.png)

<span id="_Toc65771171" class="anchor"></span>Figure 4‑22: Activity Log 2 (Sample from Another Patient Record)

The user may select the pending line entry to renew the Approved RxRenewal.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/024.png)

<span id="_Toc65771172" class="anchor"></span>Figure 4‑23: Pending Line Entry Selected

Then, the user may accept the Approved RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/025.png)

<span id="_Toc65771173" class="anchor"></span>Figure 4‑24: AC/Accept eR<sub>X</sub> Renewal

The Response includes information on the eR<sub>X</sub> prescription renewal that the Response was processed for. The renewed R<sub>X</sub> displays in the Active section of the Medication Profile. The R<sub>X</sub> number has an “A” appended to the end, indicating this is the first refill. Subsequent renewals include the next letter of the alphabet appended. (i.e., & 123456 changes to & 123456A after the first refill; for next refill: & 123456A changes to & 123456B)

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/026.png)

<span id="_Toc65771174" class="anchor"></span>Figure 4‑25: Renewed R<sub>X</sub> Active

Once the Approved RxRenewal Response is successfully renewed, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/027.png)

<span id="_Toc65771175" class="anchor"></span>Figure 4‑26: RxRenewal Response RXC Status in Holding Queue

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/028.png)

<span id="_Toc65771176" class="anchor"></span>Figure 4‑27: RxRenewal Response Details Screen

The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/029.png)

<span id="_Toc65771177" class="anchor"></span>Figure 4‑28: Corresponding RxRenewal Request – RRC in Holding Queue

Select the record to view the RxRenewal Request details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/030.png)

<span id="_Toc65771178" class="anchor"></span>Figure 4‑29: Corresponding RxRenewal Request Details Screen

The \<VP\>, \<VM\>, \<VD\>. and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type. If one of the actions is selected from here, the user receives an error message:

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/031.png)

<span id="_Toc65771179" class="anchor"></span>Figure 4‑30: Error - Validate Provider Action Not Available

### Approved with Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another RxRenewal Response message type is Approved with Changes. This indicates the renewal is approved. However, changes must be made prior to renewal.

Depending on the scenario, the RxRenewal Response message may display in the Holding Queue List View screen:

- If changes are only related to only the number of renewals in the Drug segment, the pharmacist does not need to take any action in the Holding Queue, therefore the RxRenewal Response message does not display in the Holding Queue List View.
- If the changes are related to the provider or the provider and number of renewals, the RxRenewal Response displays in the Holding Queue List View because the pharmacist is required to validate the updates.

#### Changes to Number of Renewals Only

When a RxRenewal Response message type is Approved with Changes (for number of renewals only), it does not display in the Holding Queue List View screen. It can be found using \<MV\> Message View or \<SR\> Search. The status of the Approved with Changes RxRenewal Response is “RXP” (RxRenewal Response Processed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/032.png)

<span id="_Toc65771180" class="anchor"></span>Figure 4‑31: RXP Status in Holding Queue

The RxRenewal Response details display the RxRenewal Response Message type.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/033.png)

<span id="_Toc65771181" class="anchor"></span>Figure 4‑32: RxRenewal Response Details Screen

As the user continues to scroll, the RxRenewal Response Information section indicates the RxRenewal Response Message type is Approved with Changes.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/034.png)

<span id="_Toc65771182" class="anchor"></span>Figure 4‑33: RxRenewal Response Information Section

On the OP side, a pending line entry allows for the user to renew the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/035.png)

<span id="_Toc65771183" class="anchor"></span>Figure 4‑34: Medication Profile

The Activity Log on the OP side is updated to display the information that a pending response entry was added.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/036.png)

<span id="_Toc65771184" class="anchor"></span>Figure 4‑35: R<sub>X</sub> Activity Log 1

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/037.png)

<span id="_Toc65771185" class="anchor"></span>Figure 4‑36: R<sub>X</sub> Activity Log 2

The user may select the pending line entry to renew the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/038.png)

<span id="_Toc65771186" class="anchor"></span>Figure 4‑37: Medication Profile – Pending Line Entry

Then, the user may accept the Approved with Changes RxRenewal Response.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/039.png)

<span id="_Toc65771187" class="anchor"></span>Figure 4‑38: AC/Accept eR<sub>X</sub> Renewal

The eR<sub>X</sub> on which Renewals were requested and the Response has been processed, is now reinstated with the Response. The renewed R<sub>X</sub> displays in the Active section of the Medication Profile. The R<sub>X</sub> number has an “A” appended to the end, indicating this is the first refill. Subsequent renewals include the next letter of the alphabet appended. (Ex: & 123456 changes to & 123456A after the first refill; for next refill: & 123456A changes to & 123456B).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/040.png)

<span id="_Toc65771188" class="anchor"></span>Figure 4‑39: Renewed R<sub>X</sub> Active in Medication Profile

Once the Approved with Changes RxRenewal Response is successfully renewed, the status of the RxRenewal Response in the Holding Queue changes to “RXC” (RxRenewal Response Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/041.png)

<span id="_Toc65771189" class="anchor"></span>Figure 4‑40: RxRenewal Response RXC Status in the Holding Queue

Select the record to view the RxRenewal Response details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/042.png)

<span id="_Toc65771190" class="anchor"></span>Figure 4‑41: RxRenewal Response Details Screen

The status of the corresponding RxRenewal Request changes to “RRC” (RxRenewal Request Completed).

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/043.png)

<span id="_Toc65771191" class="anchor"></span>Figure 4‑42: RxRenewal Request RRC in the Holding Queue

Select the record to view the RxRenewal Request details screen.

![](inbound-eprescribing-user-manual-unit-4-part-1-pso-7-581/044.png)

<span id="_Toc65771192" class="anchor"></span>Figure 4‑43: RxRenewal Request Details Screen

The \<VP\>, \<VM\>, \<VD\>. and \<AC\> actions are in parentheses “( )”, therefore the user cannot select these actions for this message type.

### From: Inbound ePrescribing User Manual (Unit 5 Part 1) PSO*7*581

## Generate RxChange Requests from Outpatient Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Hidden Action - eR<sub>X</sub> Change Request/EC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eR<sub>X</sub> Change Request/EC is a hidden action used for requesting change on a NewRx message, in the Holding Queue. The user can exercise EC action on NewRx record in one of the following statuses: N, I, W, or PR.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/002.png)

<span id="_Toc56761157" class="anchor"></span>Figure ‑: Hidden Action – EC/eR<sub>X</sub> Change Request

#### HC Status/Hold Due to Change

Once a user requests change on a NewRx, the NewRx record is changed from its current Holding Queue status to HC/Hold Due to Change. When a record is in HC status only UH/Un Hold, P/Print and SH/Status History actions are available.

> **NOTE:** HC status is unavailable for the user while manually putting a fillable eR<sub>X</sub> record on ‘Hold’.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/003.png)

<span id="_Toc56761158" class="anchor"></span>Figure ‑: NewRx in HC Status

#### Un Hold an HC Record

When a NewRx record is in HC status the user may use UH/Un Hold action to revert the record back to its previous status.

### Change Request Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Long Form

The long form is used for the change request types, D, G, T, OS, and S. On this version, there are two required fields, Drug and Substitutions. The user can request up to 3 new medications. The user can also enter an optional ‘Note’ and echo the eR<sub>X</sub> Drug information back to the provider.

1.  When the user exercises EC action, the eRX information is displayed for reference.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/004.png)

<span id="_Toc56761159" class="anchor"></span>Figure ‑: eR<sub>X</sub> information on EC Form

1.  The user selects the change request code, D, G, T, OS, or S. An optional Note displays where the user enters a note for why the change is being requested.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/005.png)

<span id="_Toc56761160" class="anchor"></span>Figure ‑: Optional Note on EC Form

2.  The user is prompted to either select the eR<sub>X</sub> Drug E or select another drug from local drug file, for requesting the medication. The user is also prompted select Y or N for Substitutions.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/006.png)

<span id="_Toc56761161" class="anchor"></span>Figure ‑: Selecting eR<sub>X</sub> Drug on EC Form

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/007.png)

<span id="_Toc56761162" class="anchor"></span>Figure ‑: Selecting Drug from local file on EC Form

3.  The user is prompted to enter an optional ‘Quantity’.
    1.  If the user skips entering a value for ‘Quantity’, the next prompt for optional ‘Days Supply’ entry is displayed.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/008.png)

<span id="_Toc56761163" class="anchor"></span>Figure ‑: Skip Quantity entry on EC Form

2.  If the user enters a value for ‘Quantity’, the 2 required fields associated with ‘Quantity’ field are displayed for the user.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/009.png)

<span id="_Toc56761164" class="anchor"></span>Figure ‑: Quantity related fields on EC Form

> **NOTE:** ‘Quantity Code List Qualifier’ and ‘Quantity Unit Of Measure’ are text entry fields. The user could enter “??” for each field to view the list of values they can select from.

4.  The user is prompted to enter the optional ‘Days Supply’ and ‘Refills’ values.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/010.png)

<span id="_Toc56761165" class="anchor"></span>Figure ‑: Days Supply and Refills on EC Form

5.  The user is prompted to enter the optional SIG (using the Word Processing feature). The SIG maybe up to 1000 alphanumeric characters.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/011.png)

<span id="_Toc56761166" class="anchor"></span>Figure ‑: SIG on EC Form

6.  The requested medication information is displayed for the user to review and decide if they want to use that or not. The user can send between one and 3 medications by answering the questions.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/012.png)

<span id="_Toc56761167" class="anchor"></span>Figure ‑: Additional Questions on EC Form

The option for selecting the G type change request is unavailable to the user when the substitutions on the original NewRx is allowed.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/013.png)

<span id="_Toc56761168" class="anchor"></span>Figure ‑: G Unavailable When Substitutions Are Allowed

#### Short Form

The short form is used for the change request types P and U. On this version, the user can enter an optional ‘Note’. No new medication can be requested on these change request types.

#### EC Form for Prior Authorization Request

1.  When the user exercises EC action, the eRx information is displayed for reference.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/014.png)

<span id="_Toc56761169" class="anchor"></span>Figure ‑: eR<sub>X</sub> information and optional Note on EC Form

2.  The user selects the change request code, P/Prior Authorization Required. An optional Note will be displayed where the user enters a note for why the change is being request.
3.  The user then answers the question whether to send the request out or not.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/015.png)

<span id="_Toc56761170" class="anchor"></span>Figure ‑: Question on EC Form for P Type Request

#### EC Form for Prescriber Authorization Request

1.  When the user exercises EC action, the eR<sub>X</sub> information is displayed for reference.
2.  The user selects the change request code, U/Prescriber Authorization.
3.  The user selects the change request sub code for, U type request code.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/016.png)

<span id="_Toc56761171" class="anchor"></span>Figure ‑: Change Request code and Sub Codes for U Type Request

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/017.png)

<span id="_Toc56761172" class="anchor"></span>Figure ‑: Change Request Sub Codes List for U Type Request

4.  An optional Note will be displayed where the user enters a note for why the change is being requested.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/018.png)

<span id="_Toc56761173" class="anchor"></span>Figure ‑: Optional Note on EC From for U Type Request

5.  The user then answers the question whether to send the request out or not.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/019.png)

<span id="_Toc56761174" class="anchor"></span>Figure ‑: Question on EC Form for U Type Request

## RxChange Requests in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outbound RxChange Request messages sent from VistA Outpatient Profile are stored in the Holding Queue. They can be viewed using search criteria or in the \<MV\> Message View action. To view a RxChange Request:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<CR\> RxChange Request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/020.png)

<span id="_Toc56761175" class="anchor"></span>Figure ‑: Message View Action and RxChange Request

The Holding Queue displays all RxChange Request messages, sorted by received date in descending order (newest requests first).

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/021.png)

<span id="_Toc56761176" class="anchor"></span>Figure ‑: Message View Displaying RxChange Request Messages

The RxChange Request message statuses are displayed in the “Status” column on the eR<sub>X</sub> Holding Queue. For RxChange Request statuses, refer to <u>Error! Reference source not found.</u> in <u>Error! Reference source not found.Error! Reference source not found.</u>.

> **NOTE:** RxChange Request messages are not in actionable statuses and so, they are not displayed in the Holding Queue’s list view. Users may view them only by using \<MV\> Message View action or using the \<SR\> Search criteria.

RxChange Requests in the Holding Queue without a response or an error received for 2 weeks or more, change status from CRN (RxChange Request - New) to CRX (RxChange Request Expired) in the Holding Queue.

## RxChange Request Message Details View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy user may select the RxChange Request message to display from the Holding Queue to view the message details in the Message Details View.

### RxChange Request for D, G, T, OS, and S Request types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Details View looks the same for all the request types D, G, T, OS, and S. The ‘Change Request Type’ field displays what the request type is based on the user’s selection while generating the request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/022.png)

<span id="_Toc56761177" class="anchor"></span>Figure ‑: RxChange Request – New

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/023.png)

<span id="_Toc56761178" class="anchor"></span>Figure ‑: RxChange Medication Request 1

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/024.png)

<span id="_Toc56761179" class="anchor"></span>Figure ‑: RxChange Medication Request 2

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/025.png)

<span id="_Toc56761180" class="anchor"></span>Figure ‑: RxChange Request and Message History

The Message History segment displays message history with a reference to the original R<sub>X</sub>. The RxChange Request Reference \# field displays a “V”, indicating that this was generated from VistA.

### RxChange Request for P and U Request Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Details View looks almost the same for all the request types P and U. In case of U only, the sub request code is included. The ‘Change Request Type’ field displays what the request type is based on the user’s selection while generating the request.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/026.png)

<span id="_Toc56761181" class="anchor"></span>Figure ‑: RxChange Request – New (P type request)

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/027.png)

<span id="_Toc56761182" class="anchor"></span>Figure ‑: RxChange Request – New (U type request)

## RxChange Responses in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxChange Response is received from an external provider for the RxChange Request sent from VistA OP, the RxChange Response message is first received by the Hub and is then sent to the VistA Holding Queue. The RxChange Response message types include:

- Approved
- Approved with Changes
- Validated
- Denied

RxChange Responses that are in actionable statuses are displayed in the Holding Queue’s list view. For the full list of RxChange Response statuses, refer to <u>Error! Reference source not found.</u> in <u>Error! Reference source not found.Error! Reference source not found.</u>.

To view a RxChange Response in the Holding Queue:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<MV\> Message View.
2.  Type \<CX\> RxChange Response.

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/028.png)

<span id="_Toc56761183" class="anchor"></span>Figure ‑: Message View Action

![](inbound-eprescribing-user-manual-unit-5-part-1-pso-7-581/029.png)

<span id="_Toc56761184" class="anchor"></span>Figure ‑: Holding Queue Displaying RxChange Response Messages
