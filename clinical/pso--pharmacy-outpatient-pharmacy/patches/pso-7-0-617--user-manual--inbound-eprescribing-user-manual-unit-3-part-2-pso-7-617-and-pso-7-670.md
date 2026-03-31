---
title: Inbound ePrescribing User Manual (Unit 3 Part 2) PSO*7*617 and PSO*7*670
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Inbound ePrescribing  (Unit 3 Part 2) PSO*7*617 and PSO*7*670
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
description: - [Manual Validation](#manual-validation) - [Validate Patient](#validate-patient) - [Validate Provider](#validate-provider) - [Validate Drug/SIG](#validate-drugsig) - [Accepting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue](#accepting-ersubxsubes-in-the-ersubxsub-holding-queue) - [Manual Val
audience: 
keywords: 
  - span
  - provider
  - patient
  - figure
  - class
  - validation
  - drug
  - inbound
  - unit
  - manual
page_count: 0
word_count: 12410
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_32.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p617_um_32.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
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
![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/001.png)
November 2021
Version 5.0 (Unit 3 Part 2)
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
<li><p>Updated Sections <a href="#edit-provider">3.6.2.3</a>, <a href="#accept-provider-validation">3.6.2.4</a>, <a href="#edit-drugsig">3.6.3.3</a>, and <a href="#accept-drugsig-validation">3.6.3.4</a></p></li>
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
3.  1.  
    2.  
    3.  
    4.  
    5.  

## Manual Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to accepting a fillable eR<sub>X</sub> \<AC\> and moving the eR<sub>X</sub> to Pending Outpatient Orders file, the VistA patient, provider, and drug/SIG must be validated. The eR<sub>X</sub> is then further processed using Complete Orders from OERR \[PSO LMOE FINISH\] or Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\].

The validation process begins by selecting one of the validate actions from the Summary/Details screen. For training, the sections further will show examples of NewRx processing. The remaining inbound fillable prescriptions follow the same workflow.

> **NOTE:** Before the Drug/SIG on an eR<sub>X</sub> can be manually validated, the eR<sub>X</sub> Patient must have a linked VistA patient. The \<VD\> (Validate Drug/SIG) action has parenthesis around the action to signify this action is not available until a VistA patient is linked, as illustrated in the figure below.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/002.png)

<span id="_Toc88060410" class="anchor"></span>Figure ‑: Summary/Details Screen Actions

### Validate Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient must be validated before a fillable eR<sub>X</sub> can be accepted. Information about the Patient Validation screen and editing the patient information is described in the following sections.

To validate patient information, type \<VP\> VALDIATE PATIENT from the Summary/Details screen. The Patient Validation screen displays and is described in the following sections.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/003.png)

<span id="_Toc88060411" class="anchor"></span>Figure ‑: Validate Patient

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/004.png)

<span id="_Toc88060412" class="anchor"></span>Figure ‑: Patient Validation Screen Display - Patient Not Validated/Not Auto Matched

If a match is found, however, the patient has NOT been validated, the Summary/Details screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with VistA information displaying, where applicable.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/005.png)

<span id="_Toc88060413" class="anchor"></span>Figure ‑: Patient Validation Screen Display - Patient Not Validated/Patient Auto Matched

If the VistA patient has known allergies, verified allergies display in the Allergies section.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/006.png)

<span id="_Toc88060414" class="anchor"></span>Figure ‑: VistA Patient with Known Allergies

If the patient has been validated, the Status field above the VistA Patient contains “VALIDATED”, with the user who performed the validation and date/timestamp.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/007.png)

<span id="_Toc88060415" class="anchor"></span>Figure ‑: Patient Validated

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/008.png)

<span id="_Toc88060416" class="anchor"></span>Figure ‑: Edit Patient on a VistA Match

3.  If a VistA patient match does not exist, the system prompts to select a patient at the “Select Patient Name” prompt. The partial or full name of the patient, DOB or SSN can be entered.
1.  Select the correct patient and press \<Enter\>.
2.  A message displays confirming the patient selection. Enter \<Y\> Yes.
3.  The select patient information populates the VistA Patient fields on the Patient Validation screen.

> **NOTE:** A Warning Message displays if there is a DOB, Gender, and/or on the patient selected during the edit process.

CS NOTE: For Controlled Substance eRx records, an additional check is performed for the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL for patients residing abroad. If not found, the message below will be displayed.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/009.png)

<span id="_Toc88060417" class="anchor"></span>Figure ‑: Mismatch Message

#### Accept Patient Validation

Once the patient information has been edited and reviewed for accuracy, the validation needs to be accepted on the Patient Validation screen.

1.  Select \<AV\> Accept Validation on the Patient Validation screen to accept the provider validation.
2.  A message displays confirming whether to mark the patient as validated. Enter \<Y\> Yes.

If the validation is successful, a message displays indicating that the validation was updated.

The Status changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/timestamp.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/010.png)

<span id="_Toc88060418" class="anchor"></span>Figure ‑: Confirm Acceptance of Patient Validation

A “\[v\]” displays to the right of the VistA Patient field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/011.png)

<span id="_Ref5967556" class="anchor"></span>Figure ‑: Patient Validation Complete: Summary/Details Screen Indicator

CS NOTE: For Controlled Substance eRx records, the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE for patients residing abroad will be required. If not found, the message below will be displayed and the user will not be able to proceed with the Validation as shown below.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/012.png)

<span id="_Toc88060420" class="anchor"></span>Figure ‑: Patient Validation Unable To Validate Address Warning

#### Automatic Patient Validation

When a patient validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub>es in the Holding Queue for the same patient, received on the same day, a message displays asking if the patient validation should be applied to the other eR<sub>X</sub>es. Refer to Figure 3.6‑12. If the user selects \<Y\> Yes, the system links and applies the patient validation for the eR<sub>X</sub>es currently in the Holding Queue for that patient.

> **NOTE:** Automatic Patient Validation is only available for NewRx.

The determination of the same patient is based on unique records from the ERX EXTERNAL PATIENT file (#52.46). The system only validates the same patients on eR<sub>X</sub>es that are currently in the ERX HOLDING QUEUE file (#52.49) received at the time of the automatic patient validation. Patient validation is not applied for eR<sub>X</sub>es received for that patient after the auto validation is applied. For example, if VA receives six eR<sub>X</sub>es for the same patient on the same day, the user only has to validate the patient once. If eR<sub>X</sub>es are received later that same day, those eR<sub>X</sub>es need to be revalidated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/013.png)

<span id="_Ref53477014" class="anchor"></span>Figure ‑: Automatic Patient Validation

To apply patient validation to other eR<sub>X</sub>es in the Holding Queue for the same patient, received on the same day:

1.  The system asks the user if the previous validation should be applied to the other eR<sub>X</sub>es received for the patient.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/014.png)

<span id="_Toc88060422" class="anchor"></span>Figure ‑: Apply Patient Validation to Other eR<sub>X</sub>es

4.  Enter Y for Yes to apply the validation to the other eR<sub>X</sub>es for the patient. After selecting Yes, the patient validation is applied to the other eR<sub>X</sub>es. As previously noted, any eR<sub>X</sub>es received after this action will not be validated.
3.  A message displays indicating that the validation was updated.
5.  A “\[v\]” displays to the right of the VistA Patient field on the Summary/Details screen and the Status field changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/timestamp. This occurs for all the eR<sub>X</sub>es validated via the automatic patient validation process.
6.  The statuses on all eR<sub>X</sub>es validated by the automatic patient validation process changes to “I” for In Process.

> **NOTE:** When doing a batch validation for a patient, it is possible that one or more of the records for the patient is for Controlled Substance which requires the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE if they reside abroad. So, a check will be performed for such records and if the requirement is not fulfilled, the record will not be validated. The message below will be displayed for each record with this issue:

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/015.png)

<span id="_Toc88060423" class="anchor"></span>Figure ‑: Patient Validation Unable To Validate Address Warning

### Validate Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provider must be validated before a fillable eR<sub>X</sub> can be accepted.

To validate provider information, from the Summary/Details screen, type \<VM\> VALIDATE PROVIDER. The eR<sub>X</sub> Provider Validation screen displays.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/016.png)

<span id="_Toc88060424" class="anchor"></span>Figure ‑: Summary/Details Screen Action - Validate Provider

Information about the Validate Provider display and editing the provider information is described in the following sections.

#### Provider Auto-Match in the Processing Hub

The auto-match on an external provider is based upon the NPI of the prescriber coming in on the new eR<sub>X</sub>. The NPI is matched against the VistA instance’s NEW PERSON file (#200) entry. If the NPI matches and if the Provider is marked “Authorized to Write Meds” that is considered as a match. Upon successful match, the VistA provider is linked with the incoming provider’s record in VistA.

#### Provider Manual Validation Screen Overview

The header of the Provider Validation screen contains the eR<sub>X</sub> Patient Name and the eR<sub>X</sub> Reference \#. Below the header is the eR<sub>X</sub> and VistA information for the provider, where applicable.

If a match was NOT found for the eR<sub>X</sub> provider, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with “PROVIDER NOT MATCHED” below the Status. No provider information displays.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/017.png)

<span id="_Toc88060425" class="anchor"></span>Figure ‑: Provider Not Auto Matched / Not Validated

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/018.png)

<span id="_Toc88060426" class="anchor"></span>Figure ‑: Modify Current VistA Provider

4.  Once the VistA provider is selected, the VistA provider fields populate on the Provider Validation screen, along with information whether the DEA of the Provider has expired or not.
5.  The next step in the provider validation process is to accept the validation, which is described in the next section.

> **NOTE:** The text, “Expired”, displays when the DEA \# of the selected VistA Provider has expired in File \#200.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/019.png)

<span id="_Ref5968279" class="anchor"></span>Figure ‑: Select Provider Warning for Expired DEA#

CS NOTE: The following message displays upon selecting the Provider if the Provider’s DEA date is expired.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/020.png)

<span id="_Toc88060428" class="anchor"></span>Figure ‑: Select Provider DEA Expiration Date Message

CS NOTE: The following block message displays upon selecting the Provider if the Provider’s eRx DEA number is missing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/021.png)

<span id="_Toc88060429" class="anchor"></span>Figure ‑: Select Provider Missing DEA Number Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Provider does not have a valid DEA number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/022.png)

<span id="_Toc88060430" class="anchor"></span>Figure ‑: Select VistA Provider Missing DEA Number Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the eRx Provider does not have a valid DEA number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/023.png)

<span id="_Toc88060431" class="anchor"></span>Figure ‑: Select eRx Provider Missing DEA Number Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the eRx Provider’s DEA number does not match the VistA DEA number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/024.png)

<span id="_Toc88060432" class="anchor"></span>Figure ‑: Select Provider DEA Number Mismatch Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Drug selected is a Controlled Substance, but the VistA Provider is not authorized to write for the Schedule of the Drug.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/025.png)

<span id="_Toc88060433" class="anchor"></span>Figure ‑: Select VistA Provider Not Authorized Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Drug selected is a detox Drug and the VistA Provider does not have a valid detox number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/026.png)

<span id="_Toc88060434" class="anchor"></span>Figure ‑: Select VistA Provider Missing DEA Number Warning Message

#### Accept Provider Validation

Once the correct provider has been selected and reviewed for accuracy, the next step is to accept the validation using the following steps.

1.  Select \<AV\> ACCEPT VALIDATION on the Provider Validation screen to accept the provider validation.

> **NOTE:** The following warning message displays upon selecting the validation if there is a DEA \# and/or NPI mismatch.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/027.png)

<span id="_Toc88060435" class="anchor"></span>Figure ‑: Select Provider Warning Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s Vista DEA number is missing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/028.png)

<span id="_Toc88060436" class="anchor"></span>Figure ‑: Select Provider Missing VistA DEA Number Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s not authorized to write a scheduled Controlled Substance prescription.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/029.png)

<span id="_Toc88060437" class="anchor"></span>Figure ‑: Select Provider Not Authorized Message

CS NOTE: The following warning message displays upon selecting the validation if the eRx Provider does not have a valid DEA number and the Drug is not selected or the Drug selected is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/030.png)

<span id="_Toc88060438" class="anchor"></span>Figure ‑: Select eRx Provider Missing DEA Number Warning Message

> **NOTE:** The following warning message displays upon selecting the validation if the VistA Provider does not have a valid DEA number on file and Drug is not selected or Drug selected is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/031.png)

<span id="_Toc88060439" class="anchor"></span>Figure ‑: Select VistA Provider Missing DEA Number Warning Message

> **NOTE:** The following block message displays upon selecting the validation if the eRx Provider’s DEA number does not match the VistA DEA number and Drug is not selected or Drug selected is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/032.png)

<span id="_Toc88060440" class="anchor"></span>Figure ‑: Select Provider DEA Mismatch Message

CS NOTE: The following block message displays upon selecting the validation if the VistA Drug selected is a Controlled Substance, but the VistA Provider is not authorized to write for the Schedule of the Drug.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/033.png)

<span id="_Toc88060441" class="anchor"></span>Figure ‑: Select Provider Not Authorized Message

CS NOTE: The following block message displays upon selecting the validation if the VistA Drug selected is a detox Drug, but the VistA Provider does not have a valid Detox number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/034.png)

<span id="_Toc88060442" class="anchor"></span>Figure ‑: Select VistA Provider Invalid Detox Number Message

A message displays confirming whether to mark the provider as validated.

2.  Enter \<Y\> Yes.
3.  If the validation is successful, a message displays indicating that the validation was updated. Type \<Enter\> to continue or \<Shift\><sub>+</sub>\<^\> to Quit.

> **NOTE:** If there are other eR<sub>X</sub>es for the patient, written by the same provider, received on the same day for that patient, a message displays asking if the provider validation should be applied to those eR<sub>X</sub>es. Refer to section <u>3.6.2.5 Automatic Provider Validation</u> for more information.

- The Status field changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/timestamp displays to the right of “VALIDATED”.
- A “\[v\]” displays to the right of the VistA Provider field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/035.png)

<span id="_Toc88060443" class="anchor"></span>Figure ‑: Before Provider Validation (Validate Provider Screen)

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/036.png)

<span id="_Toc88060444" class="anchor"></span>Figure ‑: After Provider Validation (Validate Provider Screen)

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/037.png)

<span id="_Ref5967567" class="anchor"></span>Figure ‑: After Provider Validation (Summary/Details Screen)

#### Automatic Provider Validation

When a provider validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub>es in the Holding Queue for the same patient by the same provider, received on the same day, a message displays asking if the other eR<sub>X</sub>es for the patient written by the provider should be validated. If the user selects \<Y\> Yes, the system links and applies the provider validation for the eR<sub>X</sub>es currently in the Holding Queue for the patient by the same provider.

> **NOTE:** Automatic Provider Validation is available only for NewRx.

The determination of the same provider is based on unique records from the ERX EXTERNAL PERSON file (#52.48). The system only validates the same provider on eR<sub>X</sub>es that are currently in the ERX HOLDING QUEUE file (#52.49) for the same patient received on the same date. Provider validation is not applied for the same provider received after the auto validation is applied once. For example, if VA receives six eR<sub>X</sub>es for the same patient on the same day from the same provider, the user only has to validate the provider once; however, if eR<sub>X</sub>es are received after the automatic provider validation is applied (e.g., later that same day by that provider), the provider for those eR<sub>X</sub>es needs to be validated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/038.png)

<span id="_Toc88060446" class="anchor"></span>Figure ‑: Automatic Provider Validation

To apply the provider validation to the other eR<sub>X</sub>es enter \<Y\> Yes. A message displays indicating that the validation was updated.

- The Status field on all the eR<sub>X</sub>es, where the provider validation has been applied, changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/timestamp displays to the right of “VALIDATED”.
- A “\[v\]” displays to the right of the VistA Provider field on the Summary/Details screen.
- The statuses on all eR<sub>X</sub>es validated by the automatic provider validation process changes to “I” for In Process.

### Validate Drug/SIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The drug/SIG information on the eR<sub>X</sub> must be validated before a fillable eR<sub>X</sub> can be accepted.

> **NOTE:** A VistA patient must be linked (matched) before the Validate Drug/SIG action is available.

To validate drug/SIG information for the eR<sub>X</sub>, type \<VD\> Validate Drug/SIG from the Summary/Details screen. The Drug Validation screen displays and is described in the following sections.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/039.png)

<span id="_Toc88060447" class="anchor"></span>Figure ‑: Validate Drug / SIG

#### Drug Auto-Match in the Processing Hub

The pre-conditions for a drug auto-match in the Processing Hub are that the drug should be a one-to-one match, should not be a Compound, not a Controlled Substance, should be Active, not Investigational and should be marked for Outpatient use in the local DRUG file (#50).

First, the drug description on the new eR<sub>X</sub> is matched against the Drug Generic Name entry in the VistA instance’s DRUG file (#50). If successful, the match stops right here, and the drug is linked in VistA.

If the match is not successful, the drug description is then matched against the VA Product Name entry in the VistA instance’s VA PRODUCT file (#50.68). Then a drug in local file for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

If the match is not successful, the NDC is used to match against the VistA instance’s NDC/UPN file (#50.67). Using the VA Product Name identified at this step, a drug in the local file for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

> **NOTE:** The NDC is an optional field and may or may not be included with the new eR<sub>X</sub>. For a supply, if UPC is sent, it is not matched against the NDC/UPN file (#50.67). Only the Drug Description match is attempted.

#### Drug/SIG Manual Validation Screen Overview

The header of the Drug/SIG Validation screen contains the eR<sub>X</sub> Patient Name and the eR<sub>X</sub> Reference \#. Below the header is the eR<sub>X</sub> and VistA information for the drug/SIG, where applicable.

If a match was NOT found for the VistA drug, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with “NOT MATCHED” to the right of the VistA Drug field. The other VistA drug/SIG fields may or may not be populated.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/040.png)

<span id="_Ref5967579" class="anchor"></span>Figure ‑: Drug Validation Screen Display - VistA Drug Not Validated / Not Auto Matched

If a VistA match was found for the drug, the screen looks similar to the below figure. The Status field has “NOT VALIDATED”, with VistA drug/SIG information displaying in the VistA Drug field (#1).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/041.png)

<span id="_Ref5967587" class="anchor"></span>Figure ‑: Drug Validation Screen Display - VistA Drug Matched / Not Validated

#### Edit Drug/SIG

1.  To edit the drug/SIG information, use the \<E\> Edit action on the Drug Validation screen.
2.  If the VistA drug/SIG information has been linked for the eR<sub>X</sub>, the edit drug/SIG sequence prompts the user to select a field or select All fields.
    - Select Item (s): Quit// \<E\> Edit
    - Which fields (s) would you like to edit? (1-10) or “A” 11: A//
3.  Under eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit, if a drug is already matched in the hub, that drug is displayed at the “select” prompt. The user is still allowed to change the drug by entering the drug name.
7.  Under eR<sub>X</sub> Holding Queue \> Validate Drug/SIG screen \> Edit, if a drug is not matched in the hub, at the “select” prompt, it is blank wherein the user can enter the drug name.
8.  When a Yes/No confirmation is asked for the selected drug, if the user hits enter or selects “No”, the control comes out of Edit mode back to VD screen.

> **NOTE:** The eR<sub>X</sub> Drug/SIG information from the external provider displays throughout the edit drug/SIG process as reference.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/042.png)

<span id="_Ref5967596" class="anchor"></span>Figure ‑: eR<sub>X</sub> Display during Edit Drug / SIG

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/043.png)

<span id="_Toc88060451" class="anchor"></span>Figure ‑: Select Provider Not Authorized Message

CS NOTE: The following warning message displays upon selecting the validation if the Provider does not have a valid Detox number.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/044.png)

<span id="_Toc88060452" class="anchor"></span>Figure ‑: Select Provider Missing Valid Detox Number Warning Message

CS NOTE: The following block message displays upon selecting the Drug validation if the eRx is Non-Controlled Substance and the VistA drug is a Controlled Substance. The Accept Validation will be blocked.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/045.png)

<span id="_Toc88060453" class="anchor"></span>Figure ‑: Blocked Accept Validation Message

CS NOTE: The following warning message displays upon selecting an eRx that is a Controlled Substance, but the VistA drug selected is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/046.png)

<span id="_Toc88060454" class="anchor"></span>Figure ‑: Drug Validation Warning Message

CS NOTE: The following block message displays upon selecting an eRx that is not digitally signed and the VistA drug is a Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/047.png)

<span id="_Toc88060455" class="anchor"></span>Figure ‑: Drug Validation eRx without DS Message

> **NOTE:** The following block message displays upon selecting an eRx that is digitally signed and the VistA drug is a Non-Controlled Substance.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/048.png)

<span id="_Toc88060456" class="anchor"></span>Figure ‑: Drug Validation eRx without DS Message

CS NOTE: The following block message displays upon selecting an eRx that doesn’t have a valid DEA number on file for the eRx Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/049.png)

<span id="_Toc88060457" class="anchor"></span>Figure ‑: Drug Validation eRx with Invalid eRx Provider DEA Number Message

CS NOTE: The following block message displays upon selecting an eRx that doesn’t have a valid DEA number on file for the VistA Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/050.png)

<span id="_Toc88060458" class="anchor"></span>Figure ‑: Drug Validation eRx with Invalid VistA Provider DEA Number Message

> **NOTE:** The following block message displays upon selecting an eRx that has a mismatched DEA number on file for the Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/051.png)

<span id="_Toc88060459" class="anchor"></span>Figure ‑: Drug Validation eRx with Provider DEA Number Mismatch Message

CS NOTE: The following warning message displays upon selecting an eRx that was written or issues after the VistA Provider’s DEA number has expired.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/052.png)

<span id="_Toc88060460" class="anchor"></span>Figure ‑: Drug Validation eRx Written After VistA Provider DEA Expiration Warning Message

CS NOTE: The following block message displays upon selecting an eRx that does not have a valid VistA Provider detox number on file.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/053.png)

<span id="_Toc88060461" class="anchor"></span>Figure ‑: Drug Validation eRx VistA Provider Invalid DEA Number Message

CS NOTE: The following warning message displays upon selecting an eRx that does not have a valid VistA Provider authorization to write the drug schedule.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/054.png)

<span id="_Toc88060462" class="anchor"></span>Figure ‑: Drug Validation eRx VistA Provider Not Authorized Warning Message

CS NOTE: The following warning message displays upon selecting an eRx that is written/issued after the VistA Provider’s DEA expiration date.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/055.png)

<span id="_Toc88060463" class="anchor"></span>Figure ‑: Drug Validation eRx VistA Provider Not Authorized Warning Message

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/056.png)

<span id="_Toc88060464" class="anchor"></span>Figure ‑: Confirm Acceptance of Drug / SIG Validation

CS NOTE: The following block message displays upon selecting an eRx that does not have a valid VistA Provider authorization to write the drug schedule.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/057.png)

<span id="_Toc88060465" class="anchor"></span>Figure ‑: Drug Accept Validation eRx VistA Provider Not Authorized Block Message

CS NOTE: The following block message displays upon selecting an eRx that is written/issued after the VistA Provider’s DEA expiration date.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/058.png)

<span id="_Toc88060466" class="anchor"></span>Figure ‑: Drug Accept Validation eRx VistA Provider Not Authorized Block Message

The Status changes to “VALIDATED” on the Drug Validation screen, along with the user who performed the validation and date/timestamp. “\[v\]” also displays to the right of the VistA Drug field on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/059.png)

<span id="_Ref5967604" class="anchor"></span>Figure ‑: Drug / SIG Validation Complete (Validate Drug / SIG Screen)

The modified VistA Drug/SIG information populates on the Drug/SIG Validation screen.

Press \<Enter\> to display Pages 2 and 3 of the Drug/SIG Validation screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/060.png)

<span id="_Ref5967613" class="anchor"></span>Figure ‑: Drug / SIG Validation Complete (Summary/Details Screen)

#### Wait Status Flag “W”

When the user completes validating Patient, Provider and Drug/SIG for an eR<sub>X</sub>, the status of the prescription changes from “I” In Process to “W” Wait in the Holding Queue’s list view.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/061.png)

<span id="_Ref5967623" class="anchor"></span>Figure ‑: eR<sub>X</sub> Holding Queue Summary/Details Screen with Validations Complete

“W” can now be seen in the status column.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/062.png)

<span id="_Toc519780560" class="anchor"></span>Figure ‑: eR<sub>X</sub> Holding Queue List View with eR<sub>X</sub> Record in “W” Status

## Accepting eR<sub>X</sub>es in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conditions must be met, before a fillable eR<sub>X</sub> can be accepted and transmitted to the Pending Queue for further processing:

1.  The eR<sub>X</sub> cannot be on Hold. If the eR<sub>X</sub> is on Hold, the eR<sub>X</sub> status on the Holding Queue List has one of the Hold Status codes, and the Hold Status, Hold Reason, and the user who placed the eR<sub>X</sub> on hold is displayed on the Summary/Details screen.
10. The eR<sub>X</sub> cannot have a status of “Rejected” RJ, “Removed” RM, “Processed” PR or “Canceled” CAN/CXQ.

All validation steps, for patient, provider, and drug/SIG must be completed, including the \<AV\> Accept Validation action on the validate screens. For additional information on the validation steps, refer to section User Manual Unit 1 (PSO_7_0_P617_UM_1_2) available on the Veteran's Documentation Library (VDL).

1.  
2.  
3.  
4.  

## Manual Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user attempts to accept an eR<sub>X</sub> where one or more of the conditions have not been met, an error message displays indicating that the eR<sub>X</sub> cannot be processed and the reason.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/063.png)

<span id="_Toc88060471" class="anchor"></span>Figure ‑: Accept eR<sub>X</sub> - Sample Validation Errors

After all the above pre-conditions have been met, to Accept an eR<sub>X</sub> \<AC\> from the Summary/Details screen, complete the following steps.

From the Summary/Details screen, type \<AC\> Accept eR<sub>X</sub>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/064.png)

<span id="_Toc88060472" class="anchor"></span>Figure ‑: Accept eR<sub>X</sub>es

A message displays notifying the user that the eR<sub>X</sub> was sent to Pending Outpatient Orders for further processing.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/065.png)

<span id="_Toc88060473" class="anchor"></span>Figure ‑: eR<sub>X</sub>es Sent to Pending Outpatient Orders

The user can then go to Complete Orders from OERR or Patient Prescription Processing to view the eR<sub>X</sub> information. Refer to section <u>3.23 Complete Orders from OERR and Patient Prescription Processing</u>.

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/066.png)

<span id="_Toc88060474" class="anchor"></span>Figure ‑: Rejecting an eR<sub>X</sub>

Once the eR<sub>X</sub> is rejected, the details of the reject message are available in the IEP Processing Hub as reference. Refer to Figure 3.16‑2.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/067.png)

<span id="_Ref53479128" class="anchor"></span>Figure ‑: Reject Message in Processing Hub

## Do Not Fill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a Controlled Substance record contains a value of ‘E’, the following message will display to inform the user that this is a DO NOT FILL record per the Provider.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/068.png)

<span id="_Toc88060476" class="anchor"></span>Figure ‑: eRx has Do Not Fill Indicator Per Provider

The user will be prompted to select REMOVE or REJECT actions.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/069.png)

<span id="_Toc88060477" class="anchor"></span>Figure ‑: Do Not Fill Error Message

## Printing in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Summary/Details screen and from any of the validate screens, the \<P\> Print action is available to print the eR<sub>X</sub>. \<P\> Print action is available for all records in the Holding Queue.

1.  Enter \<P\> Print.
2.  Enter the Device (local or network printer) and press \<Enter\>.

The print display of the eR<sub>X</sub> prints to the selected printer.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/070.png)

<span id="_Ref5967635" class="anchor"></span>Figure ‑: Print Display of Non-Controlled Substance eR<sub>X</sub>

| ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/071.png)![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/072.png)![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/073.png) |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc88060479" class="anchor"></span>Figure ‑: Print Display of Controlled Substance eR<sub>X</sub>

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
3.  To view the available hold reasons, enter a double question mark \<??\> at the “Select HOLD reason code” prompt, refer to Figure 3.19‑1. The available hold reasons display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/074.png)

<span id="_Ref53479810" class="anchor"></span>Figure ‑: Hold eR<sub>X</sub>

11. Enter the reason code at the “Select HOLD Reason code:” prompt and press \<Enter\>.
12. A prompt displays asking for additional comments on the reason for the hold. These comments are optional. Either press \<Enter\> to complete the hold process or add comments and then press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/075.png)

<span id="_Toc88060481" class="anchor"></span>Figure ‑: Select Hold Reason Code

The Hold Status, Hold Reason, and the user placing the eR<sub>X</sub> on hold display below the VistA Drug section on the Summary/Details screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/076.png)

<span id="_Toc88060482" class="anchor"></span>Figure ‑: Hold Status and Reason

The hold status also displays in the “Status” column (STA) on the Holding Queue List screen.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/077.png)

<span id="_Toc88060483" class="anchor"></span>Figure ‑: Hold Status in Status Column

> **NOTE:** When a fillable eR<sub>X</sub> is put on ‘Hold’ the only actions available for the user are UH/Un Hold, P/Print and SH/Status History.

## Un Hold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eR<sub>X</sub>es may be removed from a hold by typing \<UH\> Un Hold. Users who see the Un Hold function in parentheses “()” are not able to remove an eR<sub>X</sub> from a hold.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/078.png)

<span id="_Toc88060484" class="anchor"></span>Figure ‑: Un Hold eR<sub>X</sub>

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
<u>3.22.1 Searching eRXes</u>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/079.png)

<span id="_Toc88060485" class="anchor"></span>Figure ‑: Removing an eR<sub>X</sub>

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/080.png)

<span id="_Toc88060486" class="anchor"></span>Figure ‑: Search Queue Actions

- The display contains all eR<sub>X</sub>es satisfying the search criteria. The list is refreshed depending on the action performed. After an action is performed, the user can return to the original filtered list.
- The number of eR<sub>X</sub> records displayed in the Holding Queue’s list view is based on the ERX DEFAULT LOOKBACK DAYS file (#10.2) configured in OUTPATIENT SITE file (#59).
- By default, the ERX DEFAULT LOOKBACK DAYS field is blank, so the software goes back 365 days.
- If the Pharmacy user would like to see eR<sub>X</sub> records received from older dates, the user can use the Search (SR) option and select the “Received Date Range” (#3), to retrieve those records.

#### Search eR<sub>X</sub> – Patient Name

Users can search by patient name. A search initiated with a partial patient name may return multiple patient names, from which one patient can be selected. Selecting a patient displays the eR<sub>X</sub>es for that patient.

To search by patient name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  From the Search Queue, type \<1\> or PATIENT NAME.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/081.png)

<span id="_Toc88060487" class="anchor"></span>Figure ‑: Search Criteria - Patient Name

3.  Type the full or partial name of the patient press \<Enter\>. If multiple patients exist for the search criteria entered, select the correct patient from the list provided.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/082.png)

<span id="_Toc88060488" class="anchor"></span>Figure ‑: Patient Name Search

4.  A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

The search results display. To execute another search, enter \<Shift\>+\<^\> or \<Q\> Quit to exit the current search and return to the original Holding Queue List. The SR Search Queue action is in parentheses, indicating that the user must exit the current search to execute a new search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/083.png)

<span id="_Toc88060489" class="anchor"></span>Figure ‑: Search eR<sub>X</sub> by Patient Name Results

#### Search eR<sub>X</sub> – Date of Birth

To search by patient’s date of birth:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  From the Search Queue Type \<2\> or DATE OF BIRTH.
3.  Enter the date of birth and press \<Enter\>.

    A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/084.png)

<span id="_Toc88060490" class="anchor"></span>Figure ‑: Search Criteria - Date of Birth

The search results in the following display:

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/085.png)

<span id="_Toc88060491" class="anchor"></span>Figure ‑: Search eR<sub>X</sub> by Date of Birth Results

#### Search eR<sub>X</sub> – Received Date Range

To search for an eR<sub>X</sub> by a received date range:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
13. Type \<3\> or RECEIVED DATE RANGE.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/086.png)

<span id="_Toc88060492" class="anchor"></span>Figure ‑: Search Criteria - Received Date Range

14. Enter the beginning date and press \<Enter\>.
15. Enter the ending date and press \<Enter\>.
16. A message displays indicating that the user can enter additional search criteria or press \<Enter\> to continue with the current search.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/087.png)

<span id="_Toc88060493" class="anchor"></span>Figure ‑: Enter Beginning and Ending Date

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/088.png)

<span id="_Toc88060494" class="anchor"></span>Figure ‑: Search eR<sub>X</sub> by Received Date Range

#### Search eR<sub>X</sub> – Provider Name

To search for an eR<sub>X</sub> by a provider:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<4\> or PROVIDER NAME.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/089.png)

<span id="_Toc88060495" class="anchor"></span>Figure ‑: Search Criteria - Provider Name

3.  Type the provider’s name and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/090.png)

<span id="_Toc88060496" class="anchor"></span>Figure ‑: Enter Provider Name

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/091.png)

<span id="_Toc88060497" class="anchor"></span>Figure ‑: Search eR<sub>X</sub> by Provider

#### Search eR<sub>X</sub> – ERX Status

To search for an eR<sub>X</sub> by Status:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<5\> or ERX STATUS.
3.  Enter the eR<sub>X</sub> status and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/092.png)

<span id="_Toc88060498" class="anchor"></span>Figure ‑: Search Criteria - ERX Status

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/093.png)

<span id="_Toc88060499" class="anchor"></span>Figure ‑: Search by eR<sub>X</sub> Status

For more information on the available statuses in the Holding Queue, refer to the tables in Appendix B: Holding Queue Status Codes & Descriptions.

#### Search eR<sub>X</sub> – Drug Name

To search for an eR<sub>X</sub> by Drug Name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<6\> or DRUG NAME.
3.  Type the name or partial name of the incoming eR<sub>X</sub> drug and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/094.png)

<span id="_Toc88060500" class="anchor"></span>Figure ‑: Search Criteria - Drug Name

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/095.png)

<span id="_Toc88060501" class="anchor"></span>Figure ‑: Search eR<sub>X</sub> by Drug Name

#### Search eR<sub>X</sub> – Message Type 

To search for an eR<sub>X</sub> by Message Type:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<7\> or MESSAGE TYPE.
3.  Select the Message Type and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/096.png)

<span id="_Toc88060502" class="anchor"></span>Figure ‑: Search Criteria - Message Type

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/097.png)

<span id="_Toc88060503" class="anchor"></span>Figure ‑: Search by Message Type

#### Search eR<sub>X</sub> – eR<sub>X</sub> Reference Number

Users may also search for eR<sub>X</sub>es by eR<sub>X</sub> Reference Number. When searching by eR<sub>X</sub> Reference Number, the user may search by either inbound or outbound message types.

To search for an inbound eR<sub>X</sub> message type by eR<sub>X</sub> Reference Number:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SR\> Search Queue.
2.  Type \<8\> or ERX REFERENCE NUMBER.
3.  Enter the eR<sub>X</sub> Reference Number and press \<Enter\>.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/098.png)

<span id="_Toc88060504" class="anchor"></span>Figure ‑: Search Criteria – eR<sub>X</sub> Reference Number: Inbound

The search results display.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/099.png)

<span id="_Toc88060505" class="anchor"></span>Figure ‑: Search by eR<sub>X</sub> Reference Number Results – Inbound eR<sub>X</sub> Message Type

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/100.png)

<span id="_Toc88060506" class="anchor"></span>Figure ‑: Sort Entries Action

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

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/101.png)

<span id="_Toc88060507" class="anchor"></span>Figure ‑: Sort by Patient Name

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/102.png)

<span id="_Toc88060508" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The sorted entries display Sorted by Patient in ascending order (A-Z), and within Patient by Received Date Range with most recent first, and then by Provider in ascending order (A-Z).

#### Sort eR<sub>X</sub> – Date of Birth

To sort by Date of Birth:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<2\> or Date of Birth.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/103.png)

<span id="_Toc88060509" class="anchor"></span>Figure ‑: Sort by Date of Birth

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/104.png)

<span id="_Toc88060510" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The entries display by DOB, newest Received Date first, Patient Name ascending.

#### Sort eR<sub>X</sub> – Received Date Range

To sort eR<sub>X</sub>es by received date (most recent date displays at top of sort results):

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<3\> or Received Date Range.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/105.png)

<span id="_Toc88060511" class="anchor"></span>Figure ‑: Sort by Received Date Range

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/106.png)

<span id="_Toc88060512" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The entries sort by Received Date with most recent first and within Received Date by Patient in ascending order (A-Z), and then by Provider in ascending order (A-Z).

#### Sort eR<sub>X</sub> – Provider Name

To sort eR<sub>X</sub>es by provider name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<4\> or Provider Name.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/107.png)

<span id="_Toc88060513" class="anchor"></span>Figure ‑: Sort Criteria - Sort by Provider

1.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/108.png)

<span id="_Toc88060514" class="anchor"></span>Figure ‑: Group by Controlled Substance

2.  The entries sort by Provider in ascending order (A-Z), and within Provider by Received Date with oldest first, and then by Patient in ascending order (A-Z).

#### Sort eR<sub>X</sub> – ERX Status

To sort eR<sub>X</sub>es by eR<sub>X</sub> Status:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<5\> or ERX Status.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/109.png)

<span id="_Toc88060515" class="anchor"></span>Figure ‑: Sort Criteria – Sort by eR<sub>X</sub> Status

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/110.png)

<span id="_Toc88060516" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The entries sort by Patient Name ascending, newest Received Date first.

#### Sort eR<sub>X</sub> – Drug Name

To sort eR<sub>X</sub>es by Drug Name:

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<6\> or Drug Name.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/111.png)

<span id="_Toc88060517" class="anchor"></span>Figure ‑: Sort Criteria – Sort by Drug Name

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/112.png)

<span id="_Toc88060518" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The entries sort by Drug Name in ascending order.

#### Sort eR<sub>X</sub> – Message Type

1.  From the eR<sub>X</sub> Holding Queue List screen, type \<SO\> Sort Entries.
2.  Type \<7\> or MESSAGE TYPE.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/113.png)

<span id="_Toc88060519" class="anchor"></span>Figure ‑: Sort Criteria – Sort by Message Type

3.  Enter Yes or No to group by Controlled Substance. If the user selects ‘Yes’, prescriptions are grouped by Controlled Substance for each sort. If the user selects ‘No’, the prescriptions are not grouped by a Controlled Substance for each sort.

    ![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/114.png)

<span id="_Toc88060520" class="anchor"></span>Figure ‑: Group by Controlled Substance

4.  The entries sort by Message Type in ascending order.

## Complete Orders from OERR and Patient Prescription Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following all the validation steps for patient, provider, and drug/SIG, and after the eR<sub>X</sub> has been accepted, the eR<sub>X</sub> advances to Pending Outpatient Orders file for further processing. The eR<sub>X</sub> is further finished using either Complete Orders from OERR or Patient Prescription Processing.

The “&” symbol indicates that an eR<sub>X</sub> was received from an external provider. eR<sub>X</sub> records without the “&” symbol are VA eR<sub>X</sub>es.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/115.png)

<span id="_Toc88060521" class="anchor"></span>Figure ‑: eR<sub>X</sub> Received from External Provider

The eR<sub>X</sub> information displays at the top of the screen under the Secondary header, as shown in the figure below in both Complete Orders from OERR and Patient Prescription Processing. The hidden Option EP is provided in Outpatient to print the eR<sub>X</sub> (see figure below).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/116.png)

<span id="_Toc88060522" class="anchor"></span>Figure ‑: Hidden Option EP / Print Display of eR<sub>X</sub>

The eR<sub>X</sub> information can be edited and either finished to process further for dispensing or discontinued as needed (such as a duplicate order, since it is not filtered in the eR<sub>X</sub> Holding Queue).

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/117.png)

<span id="_Toc88060523" class="anchor"></span>Figure ‑: eR<sub>X</sub> Display in Pending Queue - Page 1

Refer to the user manuals available on the VA Documentation Library (VDL) for information on Complete Orders from OERR and Patient Prescription Processing.

Press \<Enter\> to view Pages 2 through 5 of the order in the Pending Queue.

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/118.png)

<span id="_Toc88060524" class="anchor"></span>Figure ‑: eR<sub>X</sub> Order in Pending Queue – Page 2

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/119.png)

<span id="_Toc88060525" class="anchor"></span>Figure ‑: eR<sub>X</sub> Order in Pending Queue - Page 3

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/120.png)

<span id="_Toc88060526" class="anchor"></span>Figure ‑: eR<sub>X</sub> Order in Pending Queue - Page 4

![](inbound-eprescribing-user-manual-unit-3-part-2-pso-7-617-and-pso-7-670/121.png)

<span id="_Toc88060527" class="anchor"></span>Figure ‑: eR<sub>X</sub> Order in Pending Queue - Page 5

> **NOTE:** - “eRx Date” on Holding Queue Summary screen – Date when the eR<sub>X</sub> was received in the VistA Holding Queue.

- “Date Written” on Validate Drug/SIG screen – Date when the eR<sub>X</sub> was received in the VistA Holding Queue.
- “Issue Date” on OERR/Backdoor Orders Summary screen – Effective Date if sent by the provider; if not, it is Written Date, both as sent on the eR<sub>X</sub>.
- “Written Date” displayed on Track/Audit screen on web GUI – Written Date as sent on the eR<sub>X</sub>.