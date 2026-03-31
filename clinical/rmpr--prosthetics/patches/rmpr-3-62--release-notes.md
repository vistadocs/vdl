---
title: RMPR*3*62 Automated Patient Care Enhancement (PCE) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Automated Patient Care Enhancement (PCE)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*62
group_key: "RMPR:RMPR:3"
file_numbers: 
  - 660
  - 669
security_keys: []
menu_options: 14
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"patch-description\\">Patch description</h5></td> <td><blockquote> <p>Patch RMPR3.062 enhances the purchase order process from the <strong>Purchasing (PU) Menu</strong> to link the "
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - suspense
  - colgroup
  - style
  - width
  - tbody
  - patient
  - prosthetics
page_count: 0
word_count: 10647
section_count: 5
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_62.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_62.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [All About Error Messages](#all-about-error-messages)
  - [Suspense Processing (SP) Menu](#suspense-processing-sp-menu)
  - [Suspense Reports](#suspense-reports)
  - [Appendix A](#appendix-a)
![](rmpr-3-62-automated-patient-care-enhancement-pce-release-notes/001.png)
PROSTHETICSAutomatedPatient Care Enhancement (PCE)RELEASE NOTESPatch RMPR\*3.0\*62
February 2002
V*IST*A System Design and Development
Table of Contents
Patch RMPR\*3.0\*62 Automated PCE Release Notes [1](#patch-rmpr3.062-automated-pce-release-notes)
Overview of Patch [1](#overview-of-patch)
Patient Care Encounters (PCE) [4](#patient-care-encounters-pce)
Set up a Hospital Location Clinic in Prosthetics Site Parameter File (for IRM and Prosthetics) [5](#set-up-a-hospital-location-clinic-in-prosthetics-site-parameter-file-for-irm-and-prosthetics)
Set up a Clinic in the Hospital Location File [7](#set-up-a-clinic-in-the-hospital-location-file)
All About Error Messages [8](#all-about-error-messages)
PCE Mail Messages With No Errors [8](#pce-mail-messages-with-no-errors)
PCE Mail Messages With Errors [9](#pce-mail-messages-with-errors)
Possible Error Produced during PCE Interface [12](#possible-error-produced-during-pce-interface)
Suspense Processing (SP) Menu [13](#suspense-processing-sp-menu)
Overview [13](#overview)
Suspense Items Linked [14](#suspense-items-linked)
Link a Range of 2319 Records [15](#link-a-range-of-2319-records)
Adding New Line Items/Shipping Charges During Reconcile/Close Out [16](#adding-new-line-itemsshipping-charges-during-reconcileclose-out)
<u>No</u> Suspense Item is Selected/No Linking [17](#no-suspense-item-is-selectedno-linking)
Link Patient Records to Suspense (LS) Option [18](#link-patient-records-to-suspense-ls-option)
Suspense Reports [19](#suspense-reports)
Overview [19](#overview-1)
New Report: Print Patient Records Linked to Suspense (RL) [20](#new-report-print-patient-records-linked-to-suspense-rl)
New Report: Patient Records Not Linked to Suspense (RN) [21](#new-report-patient-records-not-linked-to-suspense-rn)
New Report: Print Patient PCE Data (PD) [22](#new-report-print-patient-pce-data-pd)
Updated Report: PSAS HCPCS History (PH) [23](#updated-report-psas-hcpcs-history-ph)
Appendix A [24](#appendix-a)
Using Prosthetics Help [24](#using-prosthetics-help)

#### ## Patch RMPR\*3.0\*62 Automated PCE Release Notes

#### Overview of Patch

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-linking-feature">New Linking Feature</h5></td>
<td><blockquote>
<p>Patch RMPR*3.0*62 was created to standardize the method used by Prosthetics nationally to create and capture Patient Care Encounters (PCE). Changes with this patch have been made to the process when creating a transaction (issuing or purchasing items) for a patient.</p>
<p><u>You will now link the transaction</u> (item issued or purchased) <u>to the patient's consult</u> in the <strong>Suspense Processing</strong> <strong>List Manager</strong> screen for electronic consult orders (through CPRS) as well as manually-entered consult orders (into Prosthetics). This screen will automatically display after creating a transaction for either the single item or multiple items.</p>
<p><strong>NOTE:</strong> Do <strong>NOT</strong> install this patch (or any patch) during the first week of the month as this will affect the Prosthetics Inventory Package (PIP) statistics.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menu-and-menu-options-affected">Menu and menu options affected…</h5></td>
<td><blockquote>
<p>Patch RMPR*3.0*62 affects these menu options:</p>
<p>Enter New Request (EN) Menu [RMPR ENT REQUESTS]:</p>
</blockquote>
<ul>
<li><p>2421 Form (24) [RMPR 2421]</p></li>
<li><p>2914 Eyeglass Record (29) [RMPR 2914 - EYEGLASS]</p></li>
<li><p>Create a No-Form Daily Record (NF) [RMPR ADD OTHER DAILY REC]</p></li>
<li><p>Pickup and Delivery Charges (PD) [RMPR DELIVERY]</p></li>
<li><p>Purchase Card Form (PC) [RMPR4 PC]</p></li>
</ul>
<blockquote>
<p>Stock Issues (SI) Menu [RMPR STOCK ISS]:</p>
</blockquote>
<ul>
<li><p>Issue From Stock (IS) [RMPR ADD 2319]</p></li>
<li><p>Edit/Delete Issue From Stock (ED) [RMPR EDT 2319]</p></li>
</ul>
<blockquote>
<p>Other Purchasing Menu Options affected include:</p>
</blockquote>
<ul>
<li><p>Record 2237 Purchase to 2319 (RE) [RMPR ENT 2237]</p></li>
<li><p>Edit/Delete 2237 from 10-2319 (ED) [RMPR 2319 EDT]</p></li>
<li><p>Cancel Purchase Card Transaction (CPC) [RMPR4 PCC]</p></li>
</ul>
<blockquote>
<p>Process Form 2529-3 (PS) [RMPR 2529-3 MAIN]:</p>
</blockquote>
<ul>
<li><p>2529-3 Request Menu (RQ) [RMPR 2529-3 REQUEST MENU]</p></li>
</ul>
<blockquote>
<p>NPPD Tools (ND) [RMPR NPPD TOOLS]:</p>
</blockquote>
<ul>
<li><p>PSAS HCPCS History (PH) [RMPR PSAS HCPCS HISTORY]</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> If the system does not allow you to access an option, contact your Fiscal Service and inform them that you need access to fund control points.</p>
</blockquote></td>
</tr>
</tbody>
</table>
Continued on next page
, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="change-patient-cg-action">Change Patient (CG) action</h5></td>
<td><blockquote>
<p>The <strong>Suspense Processing List Manager</strong> screen has been changed when it automatically displays after a transaction has been created (i.e., posting, issuing or purchasing an item) vs. when it is accessed through the <strong>Suspense Processing (SP) Menu</strong>. This screen will <strong><u>not</u></strong> display the <strong>Change Patient (CG)</strong> action, because this functionality cannot be used when creating a transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-screen-from-suspense-processing-su-menu">Suspense screen from Suspense Processing (SU) Menu</h5></td>
<td><p>Suspense Processing Aug 21, 2001@10:15:45 Page: 1 of 8</p>
<p>Open/Pending/Closed Suspense for PROSPATIENT,ONE (000-45-6789)</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 07/26/01 MANUAL PROSPROVIDER,ONE @18 OPEN</p>
<p>2 05/22/01 ROUTINE PROSPROVIDER,TWO OXYGEN 08/14/01 *60 PENDING</p>
<p>3 05/22/01 ROUTINE PROSPROVIDER,TWO TOOLS @65 OPEN</p>
<p>4 03/20/01 MANUAL @110 OPEN</p>
<p>5 03/20/01 MANUAL PROSPROVIDER,ONE @110 OPEN</p>
<p>6 03/15/01 MANUAL PROSPROVIDER,ONE GLOVES @113 OPEN</p>
<p>7 12/04/00 MANUAL PROSPROVIDER,THREE EYEGLASS 12/04/00 0 CLOSED</p>
<p>8 11/17/00 ROUTINE PROSPROVIDER,THREE SHOE LIFT 12/26/00 *27 PENDING</p>
<p>9 10/17/00 MANUAL PROSPROVIDER,TWO 10/24/00 5 CLOSED</p>
<p>10 10/17/00 MANUAL PROSPROVIDER,TWO 02/14/01 *86 CLOSED</p>
<p><u>11 10/17/00 MANUAL PROSPROVIDER,TWO WHEELCHAIR 03/21/01 *111 CLOSED</u></p>
<p><u>+ Enter ?? for more actions</u>___________________________________________</p>
<p>23 Display 2319 PI Post Initial Action CD CPRS Display</p>
<p>VR View Request OT Post Other <strong>CG Change Patient</strong></p>
<p>IA View Initial Action PC Post Complete CR Cancel Request</p>
<p>VO View Other Action AD Add Manual FW Forward Consult</p>
<p>CO View Complete ED Edit Manual PR Print Consult</p>
<p>Select Item(s): Next Screen//</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-processing-list-manager-screen-after-postingissuing-an-item">Suspense Processing List Manager Screen after Posting/Issuing an Item</h5></td>
<td><p>Suspense Processing Aug 21, 2001@10:13:41 Page: 1 of 8</p>
<p>Open/Pending/Closed Suspense for PROSPATIENT,ONE (000-12-2750P)</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 07/26/01 MANUAL PROSPROVIDER,ONE @18 OPEN</p>
<p>2 05/22/01 ROUTINE PROSPROVIDER,TWO OXYGEN 08/14/01 *60 PENDING</p>
<p>3 05/22/01 ROUTINE PROSPROVIDER,TWO TOOLS @65 OPEN</p>
<p>4 03/20/01 MANUAL @110 OPEN</p>
<p>5 03/20/01 MANUAL PROSPROVIDER,ONE @110 OPEN</p>
<p>6 03/15/01 MANUAL PROSPROVIDER,ONE GLOVES @113 OPEN</p>
<p>7 12/04/00 MANUAL PROSPROVIDER,THREE EYEGLASS 12/04/00 0 CLOSED</p>
<p>8 11/17/00 ROUTINE PROSPROVIDER,THREE SHOE LIFT 12/26/00 *27 PENDING</p>
<p>9 10/17/00 MANUAL PROSPROVIDER,TWO 10/24/00 5 CLOSED</p>
<p>10 10/17/00 MANUAL PROSPROVIDER,TWO 02/14/01 *86 CLOSED</p>
<p>11 10/17/00 MANUAL PROSPROVIDER,TWO WHEELCHAIR 03/21/01 *111 CLOSED</p>
<p>+ Enter ?? for more actions</p>
<p>23 Display 2319 PI Post Initial Action CD CPRS Display</p>
<p>VR View Request OT Post Other CR Cancel Request</p>
<p>IA View Initial Action PC Post Complete FW Forward Consult</p>
<p>VO View Other Action AD Add Manual PR Print Consult Select</p>
<p>CO View Complete ED Edit Manual (<strong>Note: Action CG Is Missing)</strong></p>
<p>Item(s): Next Screen//</p></td>
</tr>
</tbody>
</table>
Continued on next page
, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patch-workflow-diagram">Patch Workflow Diagram</h5></td>
<td><blockquote>
<p>Below is a diagram chart of the workflow process that took place to create a PCE before Patch RMPR*3.0*62 existed and how it now takes place after the installation of this patch.</p>
</blockquote></td>
</tr>
</tbody>
</table>
![](rmpr-3-62-automated-patient-care-enhancement-pce-release-notes/002.png)

#### Patient Care Encounters (PCE)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="what-is-a-pce">What is a PCE?</h5></td>
<td><blockquote>
<p>A “<em>Patient Care Encounter</em>” (PCE) is a professional contact between a patient and a Provider. The Provider determines the primary reason the patient sought treatment at that encounter.</p>
<p>PCE entries are communicated to Integrated Billing for all non-service connected services (NSC) for veterans with insurance.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="what-is-a-provider">What is a Provider?</h5></td>
<td><blockquote>
<p>A provider is the entity, which furnishes health care to a consumer. This definition includes an individual or defined group of individuals who provide a defined unit of health care services to one or more individuals at a single session.</p>
<p><strong>Note:</strong> The Provider in Prosthetics is actually the Purchasing Agent who creates or initiates the purchase order for a requested item in Prosthetics for a patient. The <em><strong>Provider</strong></em> is a field in the PCE module and the <em><strong>Initiator</strong></em> is the field in Prosthetics that corresponds to the <em><strong>Provider</strong></em> in the PCE file.</p>
<p>The <em><strong>Initiator</strong></em> field in Prosthetics intuitively acknowledges the person logged in to the system (by their Logon ID) and who is creating the transaction for the Prosthetic item.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="link-to-suspense-overview">Link to Suspense Overview</h5></td>
<td><blockquote>
<p>With Patch RMPR*3.0*62, you will now <strong>link</strong> a transaction to the Suspense record (from CPRS) in the patient’s <strong>Suspense</strong> <strong>Processing List Manager</strong> screen. A result of the linking is a match of the HCPCS Code to the ICD-9 Code which will automatically create the PCE (Patient Care Encounter) for electronic consults.</p>
<p>Linking is required for manual consult suspense entries; however, no PCE is generated. Therefore, the <strong>Appointment Management Menu</strong> no longer appears.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="more-about-encounters">More about encounters</h5></td>
<td><blockquote>
<p>A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Set up a Hospital Location Clinic in Prosthetics Site Parameter File (for IRM and Prosthetics)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="attention-to-irm-and-prosthetics">ATTENTION to IRM and Prosthetics </h5></td>
<td><blockquote>
<p><strong><u>First Step for Prosthetics</u>:</strong> After the installation of Patch RMPR*3.0*62, coordinate with your IRM to enter a Prosthetics PCE Hospital Location clinic in the Prosthetics Site Parameters file (#669.9).</p>
<p><strong><u>Note to IRM</u>:</strong> If there is no clinic for Prosthetics in the Hospital Location file (#44), which belongs to Scheduling, then enter a clinic with the required fields listed as an additional instruction. (See next topic for more details.)</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="visn-prompt">VISN Prompt</h5></td>
<td><blockquote>
<p>Enter <strong>^PCE Hospital Location</strong> at the <strong>VISN</strong> prompt (<strong>required entry</strong>). Then you can enter your “active” clinic name. If your site is a multi-division site, see next page for more details.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample">Screen sample</h5>
<p>Required Entry</p></td>
<td><blockquote>
<p>PU Purchasing ...</p>
<p>DD Display/Print ...</p>
<p>UT Utilities ...</p>
<p>AM AMIS ...</p>
<p>SU Suspense ...</p>
<p>CO Correspondence ...</p>
<p>SC Scheduled Meetings and Home/Liaison Visits ...</p>
<p>PS Process Form 2529-3 ...</p>
<p>EL Eligibility Inquiry</p>
<p>ET PSC/Entitlement Records ...</p>
<p>HO Home Oxygen Main Menu ...</p>
<p>INV Pros Inventory Main ...</p>
<p>ND NPPD Tools ...</p>
<p>Select Prosthetic Official's Menu Option: <strong>Utilities &lt;Enter&gt;</strong></p>
<p>AP Add/Edit Patient to Prosthetics</p>
<p>DIS Enter Prosthetic Disability Code to 2319</p>
<p>REM Delete Prosthetic Disability Code from 2319</p>
<p>EN Enter/Edit Prosthetic Item Master</p>
<p>IF IFCAP Utilities ...</p>
<p>PGE Purge Obsolete Data ...</p>
<p>RC Flag Item as Returned/Condemned</p>
<p>RE Edit Returned/Condemned Item</p>
<p>SP Enter/Edit Site Parameters ...</p>
<p>Select Utilities Option: Enter/Edit Site Parameters &lt;Enter&gt;</p>
<p>SS Enter/Edit Station Site Parameters</p>
<p>RF Set CPT Modifier Rental Flag</p>
<p>Select Enter/Edit Site Parameters Option: <strong>Enter/Edit Station Site</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Parameters</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME: 578 HINES, IL <strong>&lt;Enter&gt;</strong> ST. NUM.</p>
<p>578 Hines Development System2</p>
<p>SITE NAME: Hines Development System2 Replace <strong>&lt;Enter&gt;</strong></p>
<p>VISN: 7// <strong>^PCE HOSPITAL LOCATION &lt;Enter&gt;</strong> <em><strong>(This is a required entry!!)</strong></em></p>
<p>PCE HOSPITAL LOCATION: PROSTHETICS &lt;---------Enter a prosthetics clinic</p>
<p>or any clinic belongs to prosthetics.</p>
<p>Every entry in the Site Parameter file</p>
<p>should have a corresponding clinic.</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME:</p>
</blockquote></td>
</tr>
</tbody>
</table>
Continued on next page
, Continued
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="entering-multi--division-sites">Entering Multi- Division Sites</h5></td>
<td><blockquote>
<p>Below are the prompts needed to set up a PCE Hospital Location clinic if sites are multi-divisions. Take into consideration that a Clinic for every Division has already been created by Scheduling.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-multi-division-site-entry">Sample Multi-Division Site entry</h5>
<p>Site #1</p>
<p>Site #2</p>
<p>Site #3 (if needed)</p></td>
<td><blockquote>
<p>Select Enter/Edit Site Parameters Option: <strong>Enter/Edit Station Site</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Parameters</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME: <strong>578 HINES, IL &lt;Enter&gt;</strong> ST. NUM.</p>
<p>578 Hines Development System2</p>
<p>SITE NAME: Hines Development System2 Replace <strong>&lt;Enter&gt;</strong></p>
<p>VISN: 7// ^PCE HOSPITAL LOCATION &lt;Enter&gt; <em>(This is a required entry!!)</em></p>
<p>PCE HOSPITAL LOCATION: PROSTHETICS &lt;---------Enter a prosthetics clinic</p>
<p>or any clinic that belongs to prosthetics.</p>
<p>Every entry in the Site Parameter file</p>
<p>should have a corresponding clinic.</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME: <strong>671</strong> <strong>&lt;Enter&gt;</strong> SAN ANTONIO, TX 671</p>
<p>&lt;ENTER ANOTHER SITE HERE&gt;</p>
<p>SITE NAME: SAN ANTONIO VAMC//</p>
<p>VISN: 7// ^PCE HOSPITAL LOCATION</p>
<p>PCE HOSPITAL LOCATION: LAB DIV CLINIC</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME: <strong>991</strong> ZZOJ VAMC IL VAMC 991</p>
<p>&lt;ENTER ANOTHER SITE HERE&gt;</p>
<p>SITE NAME: ZZOJ VAMC VAMC//</p>
<p>VISN: 7// ^PCE HOSPITAL LOCATION</p>
<p>PCE HOSPITAL LOCATION: PROBLEM TEST//</p>
<p>Select PROSTHETICS SITE PARAMETER SITE NAME:</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Set up a Clinic in the Hospital Location File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="attention">ATTENTION</h5></td>
<td><blockquote>
<p>After the installation of Patch RMPR*3.0*62, enter or edit the Hospital Location file (#44) for Prosthetics entry. If there is no entry for the Prosthetics clinic, select a clinic that belongs to Prosthetics or create a new one.</p>
<p>The following are the required fields and must be entered:</p>
</blockquote>
<ul>
<li><p>Name = Clinic</p></li>
<li><p>Non-Count Clinic? (Y or N) = No</p></li>
<li><p>Division = XXX (Note: Enter your Division)</p></li>
<li><p>Stop Code Number = Prosthetics/Orthotics</p></li>
<li><p>Credit Stop Code = Prosthetics/Orthotics</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> If you use an existing entry in the Hospital Location file (#44), make sure it has not been deactivated.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-1">Screen sample</h5></td>
<td><blockquote>
<p>Select OPTION NAME<strong>: SET UP A CLINIC SDBUILD</strong> Set up a Clinic</p>
<p>Set up a Clinic</p>
<p>Select CLINIC NAME: PROSTHETICS PROSPROVIDER,FOUR</p>
<p><strong>NAME:</strong> PROSTHETICS//</p>
<p>PROSVENDOR,ONEREVIATION: PROS//</p>
<p>CLINIC MEETS AT THIS FACILITY?: YES//</p>
<p>SERVICE: NONE//</p>
<p><strong>NON-COUNT CLINIC? (Y OR N):</strong> NO//</p>
<p><strong>DIVISION:</strong> CIOFO HINES DEV//</p>
<p><strong>STOP CODE NUMBER:</strong> PROSTHETICS/ORTHOTICS//</p>
<p>DEFAULT APPOINTMENT TYPE: REGULAR//</p>
<p>TELEPHONE:</p>
<p>REQUIRE X-RAY FILMS?:</p>
<p>REQUIRE ACTION PROFILES?: YES//</p>
<p>NO SHOW LETTER:</p>
<p>PRE-APPOINTMENT LETTER:</p>
<p>CLINIC CANCELLATION LETTER:</p>
<p>APPT. CANCELLATION LETTER:</p>
<p>ASK FOR CHECK IN/OUT TIME:</p>
<p>Select PROVIDER: PROSPROVIDER,FOUR//</p>
<p>PROVIDER: PROSPROVIDER,FOUR//</p>
<p>DEFAULT PROVIDER: YES//</p>
<p>Select PROVIDER:</p>
<p>DEFAULT TO PC PRACTITIONER?:</p>
<p>Select DIAGNOSIS:</p>
<p>WORKLOAD VALIDATION AT CHK OUT:</p>
<p>ALLOWABLE CONSECUTIVE NO-SHOWS: 3//</p>
<p>MAX # DAYS FOR FUTURE BOOKING: 33//</p>
<p>START TIME FOR AUTO REBOOK:</p>
<p>MAX # DAYS FOR AUTO-REBOOK: 3//</p>
<p>SCHEDULE ON HOLIDAYS?:</p>
<p><strong>CREDIT STOP CODE:</strong> PROSTHETICS/ORTHOTICS//</p>
<p>PROHIBIT ACCESS TO CLINIC?:</p>
<p>PHYSICAL LOCATION:</p>
<p>PRINCIPAL CLINIC:</p>
<p>OVERBOOKS/DAY MAXIMUM: 4//</p>
<p>Select SPECIAL INSTRUCTIONS:</p>
<p>LENGTH OF APP'T: 15//</p>
<p>VARIABLE APP'NTMENT LENGTH:</p>
<p>AVAILABILITY DATE:</p>
</blockquote></td>
</tr>
</tbody>
</table>

## All About Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PCE Mail Messages With No Errors

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-pce-background-function">New PCE Background Function</h5></td>
<td><blockquote>
<p>A daily PCE Mail Message will be sent to a specified mail group, the Prosthetics users in the RMPR PCE Mail Group. This message will be automatically created when Patch RMPR*3.0*62 is installed. The Prosthetics Service Supervisor needs to determine who should be in this group. Contact your IRM with the name of the user(s) that has been designated to be in that group.</p>
<p><strong><u>FOR IRM</u>:</strong> PROSTHETICS PCE BACKGROUND TASK [RMPR PCE BACKGROUND TASK] - This is a nightly job that processes the patient encounter to the PCE module. This option should be tasked to run at night when Prosthetics' users are off or Prosthetics' activities are minimal.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="no-errors">No Errors…</h5></td>
<td><blockquote>
<p>If there are no errors, the message will display as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="pce-mail-message-with-no-errors">PCE Mail Message with No Errors</h5></td>
<td><blockquote>
<p>Subj: PROSTHETICS PCE BACKGROUND MESSAGE [#65424] 27 Aug 01 08:31</p>
<p>10 lines</p>
<p>From: POSTMASTER In 'IN' basket. Page 1 *New*</p>
<p>---------------------------------------------------------------------</p>
<p>Run Date: AUG 27, 2001</p>
<p>This is a notification from the Prosthetics Department........</p>
<p>* NO ERROR TO REPORT !!!!!</p>
<p>Thank You!!!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="error-messages">Error Messages</h5></td>
<td><blockquote>
<p>If you do have errors, you will receive a mail message with the errors listed. PCE Mail messages with errors are described in the next few pages.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PCE Mail Messages With Errors

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="who-receives-an-error-message">Who receives an Error Message?</h5></td>
<td><blockquote>
<p>A monitoring tool for Prosthetics is the PCE Mail Message With Errors. You will receive this mail message if there are Prosthetics errors in the PCE package and if you are in the RMPR PCE Mail Group. <strong>Contact your PCE Coordinator at your site to resolve these errors.</strong></p>
<p><strong>Note:</strong> If you don’t have a PCE Coordinator, <strong>contact your IRM.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="when-does-an-error-happen">When does an error happen?</h5></td>
<td><blockquote>
<p>Since this Patch RMPR*3.0*62 is interfacing with two system modules – Prosthetics with the Patient Care Encounter (PCE) module, errors can occur in the PCE module and not create the PCE entry. These errors occur when the Prosthetics nightly job runs to create the final PCE entry. This alerts Prosthetics that a certain transaction did not process completely in the PCE module. There are several reasons why a PCE returns an error when Prosthetics initiates an encounter.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="error-review-process">Error Review Process</h5></td>
<td><blockquote>
<p>There are two instances where errors can occur. <u>First</u> an error can occur in Prosthetics. If one or more required fields in Prosthetics are not entered when a transaction is linked to a PCE, it will cause an error. You will then receive the PCE Error Message in the RMPR PCE Mail Group. If this happens, it is rejected as a local Prosthetics error (because the PCE has not been created and the PCE data has not been transmitted to Austin yet).</p>
<p><u>Secondly</u>, a PCE error can occur after it has been sent from Prosthetics to be transmitted as a PCE in Austin.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="how-is-an-error-fixed">How is an error fixed?</h5></td>
<td><blockquote>
<p>The PCE Coordinator has a menu option to check if the PCE data is being processed correctly or if there is a specific problem. PCE data is processed in Austin, and the PCE Coordinator can investigate the problem. This menu option is not accessible to Prosthetics users as it is in the Ambulatory Care package.</p>
<p>Also, the PCE Coordinator has the ability to correct an individual, patient-specific error and mark it for retransmission to Austin. They will also mark errors for retransmission after Prosthetics fixes them.</p>
<p>The transmission of PCE data to Austin is controlled by the Ambulatory Care package and not by Prosthetics. If encounters are not being processed in Austin, the PCE Coordinator can investigate this instance as well.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="for-pas">For PAs</h5></td>
<td><blockquote>
<p>A Purchasing Agent (PA) must have a “<em><strong>Provider Class</strong></em>” in the <strong>New Person File</strong>. If a PA is not designated in this file, then they cannot create an encounter, and they may need to manually enter a PCE. A manually entered PCE can be generated and corrected, if there are errors, up to 90 days prior to the current date.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="pce-coordinator">PCE Coordinator</h5></td>
<td><blockquote>
<p>Your PCE Coordinator will get the PCE Error Mail Message shown below and will notify Prosthetics if they need help in correcting errors. Otherwise, the PCE Coordinator will process the errors.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="pce-mail-message-with-errors">PCE Mail Message with Errors</h5>
<p>Error Message description</p></td>
<td><p>Subj: PROSTHETICS PCE BACKGROUND MESSAGE [#67719] 07 Jan 02 12:51</p>
<p>13 lines</p>
<p>From: POSTMASTER In 'IN' basket. Page 1</p>
<p>------------------------------------------------------------------------------</p>
<p>Run Date: JAN 07, 2002</p>
<p>This is a notification from the Prosthetics Department........</p>
<p>File #660 IEN=1158 - Error in PCE interface!!!</p>
<p>File #660 IEN=1160 - Error in PCE interface!!!</p>
<p><strong>???? The Provider does not have an ACTIVE person class!</strong></p>
<p>* Please contact your PCE Coordinator or IRM *</p>
<p>Thank You!!!</p>
<p>PROSTHETICS DEPARTMENT</p>
<blockquote>
<p>Enter message action (in IN basket): Ignore//</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="error-message-description-explanation">Error message description explanation</h5></td>
<td><blockquote>
<p>Note the message above that is preceded with four (4) question marks and states “<strong>????The Provider does not have an ACTIVE person class!</strong>” This message is a description of the PCE error (shown above the description) that states “<strong>File #660 IEN =1160 – Error in PCE interface!!!</strong>”</p>
<p><strong>Contact your PCE Coordinator or IRM for assistance to resolve this.</strong></p>
<p><strong><u>Note to the PCE Coordinator or IRM</u>:</strong> This sample instance of an error means that the Initiator of the Prosthetics transaction (or Provider) does not have the required information in the “<em><strong>Person class</strong></em>” field within the <strong>Person</strong> <strong>File</strong> (which is a common shared file among different packages).</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="set-up-a-clinic-error">Set Up a Clinic Error</h5></td>
<td><blockquote>
<p>There are some errors that may only occur once and can be resolved in a one-time procedure. The Set Up a Clinic in the <strong>Hospital Location File</strong> can produce an error. It will display daily in the RMPR PCE Mail Group for each PCE transaction that is created until it is resolved. Once it is fixed, it will not occur again. <strong><u>Contact your IRM</u></strong> to correct any Clinic Set-up errors with encounters that did not get processed.</p>
<p><strong><u>For IRM</u>:</strong> The <em><strong>Division</strong></em> field (in File 44, the <strong>Hospital Location</strong> <strong>File</strong>) did not correspond with the <em><strong>PCE Hospital Location Clinic</strong></em> field in the <strong>Prosthetics Site Parameter File</strong> (File #669.9). This problem resulted in PCE errors. The problem can be resolved by listing the appropriate DIVISION for the clinic in File #669.9.</p>
<p><strong>Note:</strong> See the section: “Set up a Clinic in the Hospital Location File” for details.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetics-error-messages">Prosthetics Error Messages</h5></td>
<td><blockquote>
<p>Below are possible fields where errors can occur within Prosthetics and the error message that will be delivered through the RMPR PCE Mail Group. This table also lists whom to contact to correct the error.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                                        |                                                                                                |                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If…                                                                                                                                | …Then an Error Message displays the following:                                             | Who Can Fix This Error?                                                                                                                                  |
| If a HCPCS is missing from the 2319 record…                                                                                            | “You are missing a pointer to the Procedure CPT File \#81 that represents the procedure name.” | Prosthetics users can fix this error through the Edit 2319 (ED2) Menu option (from the Purchasing Menu).                                             |
| If the Initiator (Prosthetic User) information is missing from the “New Person File”…                                                  | “You are missing a pointer to the New Person file \#200 that represents the provider’s name.”  | Contact IRM or PCE Coordinator to fix this file.                                                                                                             |
| If there is an Initiator entered, but the Effective Date is a future date in the “New Person File” (which is not a Prosthetics file)…. | “The [^1]Provider does not have an active Person Class."”                                      | Contact your IRM or PCE Coordinator to fix through File 200 (New Person File) from the User Management Menu under the Person Class Edit Menu option. |
| And if there is an Initiator but no Person Class Code File…                                                                            | “The [^2]Provider does not have an active Person Class."”                                      | Contact your IRM to fix through File 200 (New Person File) from the User Management Menu under the Person Class Edit Menu option.                    |

#### Possible Error Produced during PCE Interface

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="ed2-stock-issue-and-edit-1358-error-message">ED2, Stock Issue and Edit 1358 Error Message</h5></td>
<td><blockquote>
<p>Errors can occur during the interface with the Patient Care Encounter (PCE) module.</p>
<p>When using the <strong>Edit 2319 (ED2)</strong> <strong>Menu</strong> option (from the <strong>Purchasing Menu</strong>) as well as editing a Stock Issue or 1358, you may receive an error message like the one shown below:</p>
<p>???? You are missing a pointer to the PROCEDURE CPT FILE#81!</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="edit-2319-screen-sample">Edit 2319 Screen sample</h5></td>
<td><p>Select PATIENT: `1160 11-21-2001 TEST ITEM $1000.00</p>
<p>...OK? Yes// (Yes)</p>
<p>TYPE OF TRANSACTION: INITIAL//<strong>&lt;Enter&gt;</strong> INITIAL ISSUE</p>
<p>PATIENT CATEGORY: NSC/OP// <strong>&lt;Enter&gt;</strong> NSC/OP</p>
<p>SPECIAL CATEGORY: // <strong>&lt;Enter&gt;</strong></p>
<p>SOURCE: COMMERCIAL// <strong>&lt;Enter&gt;</strong></p>
<p>ITEM: TEST ITEM// <strong>&lt;Enter&gt;</strong></p>
<p>PSAS HCPCS: B9000// <strong>A9010</strong> <strong>&lt;Enter&gt; <em>(Notice that a change has been made.)</em></strong></p>
<p>OLD CPT MODIFER: NU <strong>&lt;Enter&gt;</strong></p>
<p>Would you like to edit the CPT Modifier ? N// <strong>&lt;Enter&gt; N</strong>O</p>
<p>VENDOR: PROSVENDOR,ONE // <strong>&lt;Enter&gt;</strong></p>
<p>QTY: 1// <strong>&lt;Enter&gt;</strong></p>
<p>TOTAL COST: 1000// <strong>&lt;Enter&gt;</strong></p>
<p>SERIAL NBR: <strong>&lt;Enter&gt;</strong></p>
<p>LOT NUMBER: <strong>&lt;Enter&gt;</strong></p>
<p>REMARKS: <strong>&lt;Enter&gt;</strong></p>
<p>EXTENDED DESCRIPTION: <strong>&lt;Enter&gt;</strong></p>
<p>ENTERAL NUTRTION INFUSION PUMP - WITHOUT ALARM</p>
<p>Edit? NO// <strong>&lt;Enter&gt;</strong></p>
<p><strong>File #660=IEN1175 – Error in PCE interface!!!</strong></p>
<p><strong>???? You are missing a pointer to the PROCEDURE CPT FILE#81!</strong></p>
<p>Would You like to Edit another Entry (Y/N) ?</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="how-to-fix-this-error">How to fix this error?</h5></td>
<td><blockquote>
<p>See previous page of possible Prosthetics Error Messages to determine how to fix the error.</p>
<p>If there is something wrong with the HCPCS Code you have selected, it needs to be reviewed and corrected. Prosthetics users can fix this error through the <strong>Edit 2319 (ED2) Menu</strong> option.</p>
<p>If it is another error message, then contact your PCE Coordinator or your IRM.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Suspense Processing (SP) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patch-description">Patch description</h5></td>
<td><blockquote>
<p>Patch RMPR*3.0*62 enhances the purchase order process from the <strong>Purchasing (PU) Menu</strong> to link the transaction to the Suspense record(s). You can access the Prosthetic purchase orders through the <strong>Enter New Request (EN) Menu</strong> (under the <strong>Purchasing (PU) Menu)</strong>. The <strong>Suspense Processing List Manager</strong> screen now <u>automatically</u> displays after posting a transaction.</p>
<p><strong>Note:</strong> There are other Prosthetic menus and options that automatically display the <strong>Suspense Processing List Manager</strong> screen (listed on the first page of this document).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-menu-option">New Menu option</h5></td>
<td><blockquote>
<p>In addition to the new reports with Patch RMPR*3.0*62, there is a new <strong>Suspense Menu</strong> option entitled<strong>: Link Patient Record to Suspense (LS)</strong>, but the main changes with this patch have been done to the <strong>Suspense Processing List Manager</strong> screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="linking-feature">Linking Feature</h5></td>
<td><blockquote>
<p>With Patch RMPR*3.0*62, you will now <strong>LINK</strong> a transaction to the Suspense record (from CPRS) in the patient’s <strong>Suspense</strong> <strong>Processing List Manager</strong> screen.</p>
</blockquote>
<ul>
<li><p>A result of the linking is a match of the HCPCS Code to the ICD-9 Code which will automatically create the PCE (Patient Care Encounter) for <u>electronic</u> consults.</p></li>
<li><p>Linking is required for <u>manual</u> suspense entries; however, no PCE is generated. Therefore, the <strong>Appointment Management Menu</strong> no longer appears.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-suspense-menu-option">New Suspense Menu option</h5></td>
<td><blockquote>
<p>SP Suspense Processing</p>
<p>ES Edit Suspense Station</p>
<p>IS Inquire to Individual Suspense Record</p>
<p>PC Print Closed Suspense Records</p>
<p>PO Print Detailed Open/Pending Suspense Records</p>
<p>PR Print 5 Day Old Suspense Report</p>
<p>PS Print Summary Open/Pending Suspense Records</p>
<p>ST Print Suspense Statistics</p>
<p>RL Print Patient Records Linked To Suspense</p>
<p>RN Print Patient Records Not Linked To Suspense</p>
<p>PD Print Patient PCE Data</p>
<p><strong>LS Link Patient Record to Suspense</strong></p>
<p>Select Suspense Option:</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Suspense Items Linked

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="accessing-the-suspense-processing-screen">Accessing the Suspense Processing Screen</h5></td>
<td><blockquote>
<p>After you post a transaction, the <strong>Suspense Processing List Manager</strong> screen automatically displays. You can then <strong>Post Initial Action (PI)</strong>, <strong>Post Other Note (OT)</strong>, or <strong>Post Complete (PC)</strong> to link to a transaction.</p>
<p>You can also perform any action on a patient that you need to as if you had accessed this screen from the <strong>Suspense Processing (SP)</strong> <strong>Menu</strong> EXCEPT the following action: <strong>Change Patient (CG).</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps">Steps</h5></td>
<td><blockquote>
<p>To link suspense items, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                                                               |
| 1    | From the Suspense Processing List Screen, select the action: Post Initial (PI), Post Other (OT), or Post Complete (PC) on the Suspense record for the patient you want to link with the transaction. |
| 2    | Select the number of the Suspense record that you want to post the note.                                                                                                                                             |
| 3    | The List of 2319 Record(s) display which includes the date, the item description, and the vendor in the 2319.                                                                                                        |
| 4    | At the Enter 2319 Record to be LINKED prompt, select the number of the transaction you issued or posted.                                                                                                         |
| 5    | You then have the option to edit the note that you just created or quit.                                                                                                                                             |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-screen-and-prompts">NEW Screen and Prompts!!!</h5></td>
<td><p>Suspense Processing Oct 02, 2001@08:51:17 Page: 1 of 1</p>
<p>Open/Pending/Closed Suspense for TEXAS,Dan (000-65-4321)</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 08/29/01 MANUAL PROVIDER,ONE MANUAL SUSPENSE ENTERE @24 OPEN</p>
<p>2 02/21/01 MANUAL PROVIDER,ONE 08/29/01 *135 CLOSED</p>
<p>3 08/16/00 MANUAL PROVIDER,SEVEN DESCRIPTION OF APPLIAN @294 OPEN</p>
<p>4 08/15/00 MANUAL PROVIDER,SEVEN EDIT DESCRIPTION @295 OPEN</p>
<p>5 07/05/00 ROUTINE PROVIDER,ONE DESCRIPTION OF APPLIAN 04/26/01 *211 CLOSED</p>
<p>6 05/24/00 MANUAL PROVIDER,SEVEN EDITING THE DESCRIPTIO 08/02/00 *50 CLOSED</p>
<p>7 05/11/00 MANUAL PROVIDER,SEVEN Editing free-text field 05/11/00 0 CLOSED</p>
<p>8 05/05/00 MANUAL ROVIDER,SEVEN Adding a manual suspen @367 OPEN</p>
<p>9 03/27/00 ROUTINE 08/03/00 *93 CLOSED</p>
<p>10 03/22/00 MANUAL PROVIDER,SEVEN ADDING A PATIENT SUSPE @399 OPEN</p>
<p>11 03/22/00 MANUAL PROVIDER,SEVEN ADDING AND POSTING cLO 03/22/00 0 CLOSED</p>
<p><u>12 03/20/00 MANUAL PROVIDER,SIX THE PHYSICIAN 03/20/00 0 CLOSED</u></p>
<p><u>+ Enter ?? for more actions___________________________________________</u></p>
<p>23 Display 2319 PI Post Initial Action CD CPRS Display</p>
<p>VR View Request OT Post Other CR Cancel Request</p>
<p>IA View Initial Action PC Post Complete FW Forward Consult</p>
<p>VO View Other Action AD Add Manual PR Print Consult Select</p>
<p>CO View Complete ED Edit Manual</p>
<p>Select Item(s): Quit// <strong>PI</strong> <strong>&lt;Enter&gt;</strong> Post Initial Action</p>
<p>Enter a list or range of numbers (1-14): <strong>1 &lt;Enter&gt;</strong></p>
<p><strong>List of 2319 Records:</strong></p>
<p><strong>1. 10/02/01 OXYGEN CONCENTR PROSVENDOR,ONE</strong></p>
<p><strong>Enter 2319 Record to be LINKED : (1-1): 1 &lt;Enter&gt;</strong></p>
<p>INITIAL ACTION NOTE:</p>
<p>No existing text</p>
<p>Edit? NO//</p></td>
</tr>
</tbody>
</table>

#### Link a Range of 2319 Records

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="link-a-range-of-items">Link a Range of Items</h5></td>
<td><blockquote>
<p>You can link a range of 2319 transactions by entering a dash between two numbers if there are multiple 2319 records listed. You can only select <u>one Suspense record</u> at a time, but you can link <u>multiple transactions</u> to that specific Suspense record.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-processing-screen">Suspense Processing screen</h5>
<p>Multiple 2319 records linked</p></td>
<td><blockquote>
<p>Suspense Processing Oct 05, 2001@12:39:18 Page: 1 of 8</p>
<p>Open/Pending/Closed Suspense for PROSPATIENT,ONE (000-45-6789)</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 08/29/01 MANUAL PROVIDER,ONE PCE 08/29/01 0 CLOSED</p>
<p>2 08/29/01 MANUAL PROVIDER,ONE TESTING PCE 09/19/01 *15 PENDING</p>
<p>3 08/29/01 MANUAL PROVIDER,FIVE TEST LINK 08/29/01 0 PENDING</p>
<p>4 08/28/01 MANUAL ADDING A MANUAL SUSPEN 09/10/01 *9 CLOSED</p>
<p>5 07/26/01 MANUAL PROVIDER,ONE 08/23/01 *20 CLOSED</p>
<p>6 06/08/01 DESCRIPTION OF APPLIAN 08/22/01 *53 CLOSED</p>
<p>7 05/22/01 ROUTINE SECOND TEST ROES 08/14/01 *60 CLOSED</p>
<p>8 05/22/01 ROUTINE PROVIDER,TWO ROES ON 08/23/01 *67 CLOSED<br />
TOOLS OK, NO C</p>
<p>9 03/20/01 MANUAL @143 OPEN</p>
<p>10 03/20/01 MANUAL PROVIDER,EIGHT @143 OPEN</p>
<p>11 03/15/01 MANUAL PROVIDER,EIGHT TEST C @146 OPEN</p>
<p>12 12/04/00 MANUAL PROVIDER,NINE DFSDFS 12/04/00 0 CLOSED</p>
<p>13 11/17/00 ROUTINE PROVIDER,NINE TEST ASTERIKS 12/26/00 *27 PENDING</p>
</blockquote>
<p><u>+ Enter ?? for more actions___________________________________________</u></p>
<p><u>23 Display 2319 PI Post Initial Action CD CPRS Display___________</u></p>
<p>VR View Request OT Post Other CR Cancel Request</p>
<p>IA View Initial Action PC Post Complete FW Forward Consult</p>
<p>VO View Other Action AD Add Manual PR Print Consult Select</p>
<p>CO View Complete ED Edit Manual</p>
<blockquote>
<p>Select Item(s): Next Screen// OT Post Other</p>
<p>Enter a list or range of numbers (1-14): <strong>1</strong> <strong>&lt;Enter&gt;</strong></p>
<p>List of 2319 Records:</p>
<p>1. 10/05/01 WHEELCHAIR - EL PROSVENDOR,ONE</p>
<p>2. 10/05/01 EYEGLASSES PROSVENDOR,ONE</p>
<p>3. 10/05/01 OXYGEN CONCENTR PROSVENDOR,ONE</p>
<p>Enter 2319 Record to be LINKED : (1-3): <strong>1-2 &lt;Enter&gt;</strong></p>
<p>ACTION NOTE:</p>
<p>No existing text</p>
<p>Edit? NO//</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-scenario-example">Sample Scenario Example</h5></td>
<td><p>If two or more transactions are shown for one consult, but they were created from different menus (i.e., <strong>Stock Issue Menu</strong> and <strong>Purchase Card Menu</strong>), when linking the first transaction (<strong>Stock Issue Menu</strong>), you would perform one of these actions:</p>
<p><strong>1)</strong> <strong>Post Initial (PI)</strong> or <strong>Post Other (OT)</strong> for a note on that consult. In the second transaction linking, you would then <strong>Post a Complete (PC)</strong> note to the same consult.</p>
<p>- Or -</p>
<p><strong>2)</strong> Remember that you can always <strong>Post Other (OT)</strong> after a consult has been closed. An example is the case of two transactions from one consult resulting from different menus. You can <strong>Post Complete Note (PC)</strong> for the first transaction (<strong>Stock Issue</strong>) and then <strong>Post Other (OT)</strong> for the second transaction (Purchase Card) in order to complete the “Linking” process.</p></td>
</tr>
</tbody>
</table>

#### Adding New Line Items/Shipping Charges During Reconcile/Close Out

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-to-automatic-linking">Introduction to Automatic Linking</h5></td>
<td><blockquote>
<p>You can add a new line item or a shipping charge to an already created Purchase Order (PO) during the reconciling/close out process. There are two possible linking scenarios including:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p><u>Multiple Consults</u> - where you will select the proper link for the new line item or a shipping charge.</p>
</blockquote></li>
<li><blockquote>
<p><u>Single Consult</u> - <strong>Automatic Linking</strong> – where you are adding a line item or a shipping charge to a PO that has only one consult associated with it. Therefore the linking association is done <strong><u>automatically</u></strong> for you.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scenario-1-multiple-consults">Scenario 1 –Multiple Consults</h5></td>
<td><blockquote>
<p>When creating a PO – a 1358 or Visa, it may be associated with two or more Suspense (consults) records. One consult could be a CPRS consult and the other one is a Manual consult. But when you reconcile/close out the transaction, you need to add a new line item or a shipping charge as you did not include this in the original transaction.</p>
<p>Because you are adding to the PO, and it has two Suspense records associated with it, you will be prompted to identify which record – the CPRS or the Manual consult to link the new line item or the shipping charge to the correct transaction.</p>
<p><strong>Note:</strong> Since the PO has some items associated with one consult, and some items associated with another, you will have to determine the proper link.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scenario-2-automatic-linking">Scenario 2 – Automatic Linking</h5></td>
<td><blockquote>
<p>A PO is created and linked to one Suspense record. It is not split into multiple records, and NO estimated shipping charge was included. At the reconcile/close out of this transaction, you need to add the shipping charge.</p>
<p>Because all the items were on the same consult (same Suspense record), all additional items and/or shipping charges will be <strong><u>automatically linked</u></strong> at the close out without the user having to select the link. Because the linking is done automatically, there will be no additional prompt for you.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### <u>No</u> Suspense Item is Selected/No Linking

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="no-action-on-suspense">No action on Suspense</h5></td>
<td><blockquote>
<p>When no action is performed on a Suspense record, there is no linking done. When you exit the <strong>Suspense Processing List Manager</strong> screen, a new message displays as shown below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-processing-list-manager-screen">Suspense Processing List Manager screen</h5>
<p>New Message</p>
<p>New Prompt</p></td>
<td><p>Suspense Processing Aug 21, 2001@12:15:44 Page: 1 of 8</p>
<p>Open/Pending/Closed Suspense for PROSPATIENT,ONE (000-45-6789)</p>
<p><u>Date Type Requestor Description Init Act Days Status</u></p>
<p>1 07/26/01 MANUAL PROSPROVIDER,ONE @18 PENDING</p>
<p>2 05/22/01 ROUTINE PROSPROVIDER,TWO OXYGEN 08/14/01 *60 PENDING</p>
<p>3 05/22/01 ROUTINE PROSPROVIDER,TWO TOOLS @65 OPEN</p>
<p>4 03/20/01 MANUAL @110 OPEN</p>
<p>5 03/20/01 MANUAL PROSPROVIDER,ONE @110 OPEN</p>
<p>6 03/15/01 MANUAL PROSPROVIDER,ONE GLOVES @113 OPEN</p>
<p>7 12/04/00 MANUAL PROSPROVIDER,THREE EYEGLASS 12/04/00 0 CLOSED</p>
<p>8 11/17/00 ROUTINE PROSPROVIDER,THREE SHOE LIFT 12/26/00 *27 PENDING</p>
<p>9 10/17/00 MANUAL PROSPROVIDER,TWO 10/24/00 5 CLOSED</p>
<p>10 10/17/00 MANUAL PROSPROVIDER,TWO 02/14/01 *86 CLOSED</p>
<p><u>11 10/17/00 MANUAL PROSPROVIDER,TWO WHEELCHAIR 03/21/01 *111 CLOSED_</u></p>
<p><u>+ Enter ?? for more actions___________________________________________</u></p>
<p>23 Display 2319 PI Post Initial Action CD CPRS Display</p>
<p>VR View Request OT Post Other CR Cancel Request</p>
<p>IA View Initial Action PC Post Complete FW Forward Consult</p>
<p>VO View Other Action AD Add Manual PR Print Consult Select</p>
<p>CO View Complete ED Edit Manual</p>
<p>Select Item(s): Quit// <strong>&lt;Enter&gt;</strong> QUIT</p>
<p><strong>*</strong></p>
<p><strong> Patient record(s) is/are still exist............... </strong></p>
<p><strong> You must select an entry from the list to complete </strong></p>
<p><strong> all transactions, otherwise some transactions will </strong></p>
<p><strong> not be linked to SUSPENSE!!! </strong></p>
<p><strong>*</strong></p>
<p><strong>Would you like to LINK Suspense or EXIT without linking?:</strong> (L/E): L// <strong>??</strong> <strong>&lt;Enter&gt;</strong></p>
<p>Answer `L` to Link to suspense, 'E' to Exit transaction without link to suspense.</p>
<p>Select one of the following:</p>
<p><strong>L LINK Suspense to Patient Record</strong></p>
<p>E EXIT and NO Link to Suspense</p>
<p>Would you like to LINK Suspense or EXIT without linking?: (L/E): L// &lt;<strong>Enter&gt;</strong> LINK Suspense</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-link-prompt">New Link prompt</h5></td>
<td><blockquote>
<p>You can then return to the <strong>Suspense Processing List Manager</strong> screen by selecting “L” for <strong>Link Suspense to Patient Record</strong> or select “E” to <strong>Exit</strong> with no link to Suspense.</p>
<p><strong>Note:</strong> To eliminate the new message (as shown above), you need to link the transactions!</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Link Patient Records to Suspense (LS) Option

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="function-description">Function description</h5></td>
<td><blockquote>
<p>The <strong>Link Patient Records to Suspense (LS)</strong> option is used for linking patient records to Suspense records. This option can be used as a <strong>BACKUP</strong> to perform linking if it is not done directly after posting a transaction.</p>
<p>In order to link a patient record to a Suspense record, you must access the Suspense record and add a note using either of these actions: <strong>Post Initial (PI), Post Other (OT),</strong> or <strong>Post Complete (PC)</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-2">Screen sample</h5></td>
<td><blockquote>
<p>SP Suspense Processing</p>
<p>ES Edit Suspense Station</p>
<p>IS Inquire to Individual Suspense Record</p>
<p>PC Print Closed Suspense Records</p>
<p>PO Print Detailed Open/Pending Suspense Records</p>
<p>PR Print 5 Day Old Suspense Report</p>
<p>PS Print Summary Open/Pending Suspense Records</p>
<p>ST Print Suspense Statistics</p>
<p>RL Print Patient Records Linked To Suspense</p>
<p>RN Print Patient Records Not Linked To Suspense</p>
<p>PD Print Patient PCE Data</p>
<p><strong>LS Link Patient Record to Suspense</strong></p>
<p>Select Suspense Option: <strong>LS &lt;Enter&gt;</strong> Link Patient Record to Suspense</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select PATIENT: <strong>PROSPATIENT,ONE&lt;Enter&gt;</strong> PROSPATIENT,ONE 12-27-50 000000001 YES SC VETERAN</p>
<p>Enrollment Priority: GROUP 2 Category: IN PROCESS End Date:</p>
<p>SUPPORT ISC</p>
<p>1 PROSPATIENT,ONE 12-13-1999 EYEGLASSES $ 10.00</p>
<p>2 PROSPATIENT,ONE 12-13-1999 PORK-GROUND/FRZN $ 1.00</p>
<p>3 PROSPATIENT,ONE 12-13-1999 WHEELCHAIR-ADULT/HEMI/B $ 0.00</p>
<p>4 PROSPATIENT,ONE 12-13-1999 WHEELCHAIR-ADULT/HEMI/B $ 0.00</p>
<p>5 PROSPATIENT,ONE 12-13-1999 WHEELCHAIR-ADULT/HEMI/B $ 0.00</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 3 &lt;Enter&gt; 12-13-1999 WHEELCHAIR-ADULT/HEMI/B $ 0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-processing-list">Suspense Processing List</h5></td>
<td><blockquote>
<p>After you select an item from the 2319 list, then you will be routed to the <strong>Suspense Processing List Manager</strong> screen where you can link the record to the transaction from this list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Suspense Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="new-reports">New Reports</h5></td>
<td><blockquote>
<p>With Patch RMPR*3.0*62, there are three new reports available from the <strong>Suspense Processing (SP) Menu</strong> as follows:</p>
</blockquote>
<ul>
<li><p>Print Patient Records Linked to Suspense (RL)</p></li>
<li><p>Print Patient Records Not Linked to Suspense (RN)</p></li>
<li><p>Print Patient PCE Data (PD)</p></li>
</ul>
<blockquote>
<p>The <strong>PSAS HCPCS History (PH)</strong> report from the <strong>NPPD Tools Menu (ND)</strong> has also been updated.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-menu-options">Suspense Menu options</h5></td>
<td><blockquote>
<p>SP Suspense Processing</p>
<p>ES Edit Suspense Station</p>
<p>IS Inquire to Individual Suspense Record</p>
<p>PC Print Closed Suspense Records</p>
<p>PO Print Detailed Open/Pending Suspense Records</p>
<p>PR Print 5 Day Old Suspense Report</p>
<p>PS Print Summary Open/Pending Suspense Records</p>
<p>ST Print Suspense Statistics</p>
<p>RL Print Patient Records Linked To Suspense</p>
<p>RN Print Patient Records Not Linked To Suspense</p>
<p>PD Print Patient PCE Data</p>
<p>LS Link Patient Record to Suspense</p>
<p>Select Suspense Option:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-patient-records-linked-to-suspense-rl">Print Patient Records Linked to Suspense (RL)</h5></td>
<td><blockquote>
<p>The <strong>Print Patient Records Linked to Suspense (RL)</strong> report displays or prints patient record(s) from a given date range that have been linked to any Suspense records.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="patient-records-not-linked-to-suspense-rn">Patient Records Not Linked to Suspense (RN)</h5></td>
<td><blockquote>
<p>The <strong>Patient Records Not Linked to Suspense (RN)</strong> report displays or prints patient record(s) in a given date range that have not been linked to any Suspense records.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-patient-pce-data-pd">Print Patient PCE Data (PD)</h5></td>
<td><blockquote>
<p>The report <strong>Print Patient PCE Data (PD)</strong> option prints all patients in a given date range with a PCE linked to it. You can only review data for the <u>previous</u> day that has been through batch processing.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="psas-hcpcs-history-ph">PSAS HCPCS History (PH)</h5></td>
<td><blockquote>
<p>The <strong>PSAS HCPCS History (PH)</strong> option, from the <strong>NPPD Tools Menu (ND)</strong> has a modification that includes an ICD9 Code and a description in the printout now.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### New Report: Print Patient Records Linked to Suspense (RL)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description">Report description</h5></td>
<td><blockquote>
<p>With Patch RMPR*3.0*62, the <strong>Print Patient Records Linked to Suspense (RL)</strong> is a new report that displays or prints patient record(s) from a given date range that have been linked to any Suspense records.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="output-sample">Output sample</h5></td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-300</strong> <strong>&lt;Enter&gt;</strong> (FEB 20, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (DEC 17, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// &lt;Enter&gt;</p>
<p>Processing report.......</p>
</blockquote>
<p>* PROSTHETICS PATIENT RECORDS LINKED TO SUSPENSE * PAGE: 11</p>
<p>Start Date: FEB 20, 2001 End Date: DEC 17, 2001 station: MILWAUKEE, WI</p>
<p>------------------------------------------------------------------------------</p>
<p>TYPE OF CPRS</p>
<p>DATE PATIENT ITEM REQUEST REQUESTOR INITIATOR</p>
<p>---- ------- ---- ---- --------- ---------</p>
<p>12/11/01 PATIENT,TWO SPONGE-BATH ROUTINE PROVIDER,TEN PROSPROVIDER1,THREE</p>
<p>12/11/01 PATIENT,TWO SHOEHORN-24IN-STAI ROUTINE PROVIDER,TEN PROSPROVIDER1,THREE</p>
<p>12/11/01 PATIENT,TWO STICK-DRESSING ROUTINE PROVIDER,TEN PROSPROVIDER1,THREE</p>
<p>12/11/01 PATIENT,TWO SOCK AID-EASY PULL ROUTINE PROVIDER,TEN PROSPROVIDER1,THREE</p>
<p>12/11/01 PATIENT,THREE WHEELCHAIR PARTS MANUAL ROVIDER1,ONE PROSPROVIDER1,THREE</p>
<p>12/11/01 PATIENT,FOUR WHEELCHAIR PARTS MANUAL PROVIDER1,ONE PROSPROVIDER1,FOUR</p>
<p>12/11/01 PATIENT,FIVE CANE-WALKIN-EAG-WO ROUTINE PROVIDER1,TWO PROSPROVIDER1,FIVE</p>
<p>12/11/01 PATIENT,SIX AID-SOCK ROUTINE PROVIDER,TEN PROSPROVIDER1,FIVE</p>
<p>12/11/01 PATIENT,SIX SHOEHORN-24IN-STAI ROUTIN PROVIDER,TEN PROSPROVIDER1,FIVE</p>
<p>12/11/01 PATIENT,SIX SPONGE-BATH ROUTIE PROVIDER,TEN PROSPROVIDER1,FIVE</p>
<p>12/11/01 PATIENT,SIX REACHER-32-PLASTIC ROUTINE PROVIDER,TEN PROSPROVIDER1,FIVE</p>
<p>12/11/01 PATIENT,SIX STICK-DRESSING ROUTINE PROVIDER,TEN PROSPROVIDER1,FIVE</p>
<blockquote>
<p>------------------------------------------------------------------------------</p>
<p>Totals: Routine Prosthetics = 57 Eyeglass = 4 Contact Lens = 0</p>
<p>Oxygen = 1 Manual = 3</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### New Report: Patient Records Not Linked to Suspense (RN)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description-1">Report description</h5></td>
<td><blockquote>
<p>The <strong>Patient Records Not Linked to Suspense (RN)</strong> report displays or prints patient record(s) in a given date range that have not been linked to any Suspense records.</p>
<p>The following information will NOT be included on this report:</p>
<p>1. All Home Oxygen patients and patient data (from Screen 8 of the 2319).</p>
<p>2. Shipping data (from the 2319).</p>
<p>3. Historical Data (from the integration of sites)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="cost-column">Cost Column</h5></td>
<td><blockquote>
<p>The <strong>Cost</strong> column displays the dollar cost of the item that is shown.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="output-sample-1">Output sample</h5></td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: <strong>T-300</strong> <strong>&lt;Enter&gt;</strong> (FEB 20, 2001)</p>
<p>Ending Date: <strong>T</strong> <strong>&lt;Enter&gt;</strong> (DEC 17, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// &lt;Enter&gt;</p>
<p>Processing report.......</p>
<p>PROSTHETICS PATIENT RECORDS NOT LINKED TO SUSPENSE Run Date:12/17/01 PAGE: 4</p>
<p>Start Date: FEB 20, 2001 End Date: DEC 17, 2001 station: SUPPORT ISC</p>
<p>------------------------------------------------------------------------------</p>
<p>DATE PATIENT ITEM COST VISTA # INITIATOR</p>
<p>---- ------- ---- ---- ------- ---------</p>
<p>09/19/01 PROSPATIENT,ONE WHEELCHAIR - ELECT 10.00 1108 PROSPROVIDER,ONE</p>
<p>09/20/01 PROSPATIENT1,FIVE SHOE COMPONENTS 0.00 1115 PROSPROVIDER,ONE</p>
<p>09/25/01 PROSPATIENT,ONE EYEGLASSES 1.00 1120 PROSPROVIDER,TWO</p>
<p>09/27/01 PROSPATIENT1,FIVE EYEGLASSES 1.00 1129 PROSPROVIDER,ONE</p>
<p>10/11/01 PROSPATIENT,ONE WHEELCHAIR - ELECT 10.00 1143 PROSPROVIDER,ONE</p>
<p>10/16/01 PROSPATIENT,ONE WHEELCHAIR - MANUA 14.00 1148 PROSPROVIDER,ONE</p>
<p>10/18/01 PROSPATIENT,ONE SHOE COMPONENTS 22.00 1149 PROSPROVIDER,SEVEN</p>
<p>11/15/01 PROSPATIENT,ONE SHOE COMPONENTS 24.75 1156 PROSPROVIDER,SEVEN</p>
<p>11/20/01 PROSPATIENT1,FIVE SHOE COMPONENTS 2.00 1159 PROSPROVIDER,SEVEN</p>
<p>11/27/01 PROSPATIENT1,FIVE SHOE COMPONENTS 20.00 1161 PROSPROVIDER,SEVEN</p>
<p>12/04/01 PROSPATIENT1,FIVE WHEELCHAIR - MANUA 14.00 1162 PROSPROVIDER,ONE</p>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="to-eliminate-items-from-this-report">To eliminate items from this report…</h5></td>
<td><blockquote>
<p>You can eliminate item(s) from displaying on this report! You must create a manual Suspense entry if there is no Suspense entry already created. Then you can link this entry to the transaction to eliminate the item(s) on this report.</p>
<p>Also you may have the Suspense entry already created, but you have not linked it to the transaction yet. This will also continue to display item(s) on this report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### New Report: Print Patient PCE Data (PD)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="report-description-2">Report description</h5></td>
<td><blockquote>
<p>With the Patch RMPR*3.0*62, the new report <strong>Print Patient PCE Data (PD)</strong> is available. This option prints all patients in a given date range with a PCE linked to it.</p>
<p><strong>Note:</strong> You can only review data for the <u>previous</u> day that has been through batch processing.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="output-sample-2">Output sample</h5></td>
<td><blockquote>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Starting Date: T-300 <strong>&lt;Enter&gt;</strong> (FEB 20, 2001)</p>
<p>Ending Date: T <strong>&lt;Enter&gt;</strong> (DEC 17, 2001)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80// &lt;Enter&gt;</p>
<p>Processing report.......</p>
<p>* PROSTHETICS PCE DATA * Run Date: 12/17/01 PAGE: 1</p>
<p>Start Date: FEB 20, 2001 End Date: DEC 17, 2001 station: SUPPORT ISC</p>
</blockquote>
<p>--------------------------- ---------------------------------------------------</p>
<p>TYPE OF CPRS PCE</p>
<p>DATE PATIENT ITEM REQUEST REQUESTOR ICD9 DATE DIAGNOSIS</p>
<p>---- ------- ---- ------- --------- ---- -------- ---------12/11/01 PATIENT,SEVEN WALKER-W ROUTINE PROVIDER1,SIX 829.0 12/12/01 Fractures</p>
<p>12/11/01 PATIENT,THREE STOCKING ROUTINE PROVIDER1,SEVEN 799.3 12/12/01 Debility</p>
<p>12/11/01 PATIENT,SIX MIRROR-I ROUTINE PROVIDER1,EIGHT 344.1 12/12/01 Paraplegi</p>
<p>12/11/01 PATIENT,EIGHT WHEELCHA ROUTINE PROVIDER1,NINE 344.00 12/12/01 Quadriple</p>
<p>12/11/01 PATIENT,NINE BLOOD PR ROUTINE PROVIDER1,TEN 401.9 12/12/01 Hypertens</p>
<p>12/11/01 PATIENT,TEN BA-RECRE ROUTINE PROVIDER2,ONE 369.4 12/12/01 Legal bli</p>
<p>12/11/01 PATIENT1,ONE CANE-WAL ROUTINE PROVIDER2,TWO 716.46 12/12/01 Transient</p>
<p>12/11/01 PATIENT1,TWO RAIL-BAT ROUTINE PROVIDER2,THREE 799.3 12/12/01 Debility</p>
<p>12/11/01 PATIENT1,THREE CRUTCH-A ROUTINE PROVIDER2,FOUR 892.0 12/12/01 Open wound</p>
<p>12/11/01 PATIENT1,FOUR CANE-WAL ROUTINE PROVIDER1,SEVEN 719.46 12/12/01 Pain in jo</p>
<blockquote>
<p>------------------------------------------------------------------------------</p>
<p>&lt;End of Report&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Updated Report: PSAS HCPCS History (PH)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>The <strong>PSAS HCPCS History (PH)</strong> option, from the <strong>NPPD Tools Menu (ND),</strong> has a modification that includes an ICD9 Code and a Description in the printout now.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="screen-sample-3">Screen sample</h5></td>
<td><blockquote>
<p><strong>PH PSAS HCPCS History</strong></p>
<p>AE Add/Edit HCPCS Synonyms</p>
<p>HH DSS HCPCS History</p>
<p>INQ HCPCS Inquiry</p>
<p>LPRT Print 2529-3 Worksheets</p>
<p>LSL Print 2529-3 Single Line</p>
<p>MAP Print PSAS HCPCS List</p>
<p>PRT Print NPPD Worksheets</p>
<p>QED2 Quick Edit 2319 Record</p>
<p>SL Print NPPD Single Line Detail</p>
<p>Select NPPD Tools Option: <strong>PH</strong> <strong>&lt;Enter&gt;</strong> PSAS HCPCS History</p>
<p>SITE: Hines Development System// <strong>&lt;Enter&gt;</strong> 499</p>
<p>Select PSAS HCPCS (1): <strong>E1372</strong> <strong>&lt;Enter&gt;</strong> OXY SUPPL HEATER FOR NEBULIZ</p>
<p>Select PSAS HCPCS (2): <strong>&lt;Enter&gt;</strong></p>
<p>Beginning Date: T-30// <strong>&lt;Enter&gt;</strong> (JAN 07, 2002)</p>
<p>Ending Date: TODAY// <strong>&lt;Enter&gt;</strong> (FEB 06, 2002)</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> TELNET Right Margin: 80//<strong>&lt;Enter&gt;</strong></p>
<p>PSAS HCPCS HISTORY:E1372 STA 499 PAGE 1</p>
<p>REQUEST DATE PATIENT NAME SSN VENDOR JAN 05, 2002-FEB 04, 2002</p>
<p>=============================================================================</p>
<p>JAN 22, 2002 PROSPATIENT1,FIVE0005 PROSVENDOR,ONE</p>
<p>ITEM: PORK-GROUND/FRZN QTY: 1 TOTAL COST: 15.00 INITIAL ISSUE</p>
<p>INITIATOR: PROSPROVIDER,ONENO</p>
<p>ICD9 Code:</p>
<p>JAN 22, 2002 PROSPATIENT1,FIVE0005 PROSVENDOR,ONE</p>
<p>ITEM: EYEGLASSES QTY: 1 TOTAL COST: 20.00 INITIAL ISSUE</p>
<p>INITIATOR: PROSPROVIDER,ONENO</p>
<p>ICD9 Code:</p>
<p>JAN 22, 2002 PROSPATIENT1,FIVE0005 PROSVENDOR,ONE</p>
<p>ITEM: PORK-GROUND/FRZN QTY: 1 TOTAL COST: 5.00 INITIAL ISSUE</p>
<p>INITIATOR: PROSPROVIDER,ONENO</p>
<p>ICD9 Code: 401.0 MALIGNANT HYPERTENSION</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Using Prosthetics Help

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="question-mark-help">Question Mark Help</h5></td>
<td><blockquote>
<p>You can view online descriptive help for menus, options, and prompts. You can enter one, two, or three question marks to get extended online help in Prosthetics.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="single-question-mark">? (Single question mark)</h5></td>
<td><blockquote>
<p>Entering a single question mark at a prompt provides you with a single line of standard help.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="double-question-mark">?? (Double question mark)</h5></td>
<td><blockquote>
<p><strong>Two question marks entered at a prompt provide you with a list of choices appropriate to the prompt where you entered the question marks.</strong></p>
<p>SITE: Hines Development System// <strong>?? &lt;Enter&gt;</strong></p>
<p>Choose from:</p>
<p>ATLANTA VAMC 508</p>
<p>CORKWELL VAMC 500</p>
<p>HINESTEST 998</p>
<p>Hines Development System 499</p>
<p>SAN ANTONIO VAMC 671</p>
<p>ZZOJ VAMC VAMC 991</p>
<p>SITE: Hines Development System//</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menu-options">Menu Options</h5></td>
<td><blockquote>
<p>You can enter three question marks to view Menu option descriptions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="triple-question-mark">??? (Triple question mark)</h5></td>
<td><blockquote>
<p><strong>Entering three question marks provides you with a brief description and a synonym:</strong></p>
<p>24 2421 Form</p>
<p>25 2520 Transaction without printing 10-55</p>
<p>10 10-55 PSC Form</p>
<p>29 2914 Eyeglass Record</p>
<p>NF Create a No-Form Daily Record</p>
<p>PD Pickup and Delivery Charges</p>
<p>PC Purchase Card Form</p>
<p>SS Purchase Card Site Parameter</p>
<p>Select Enter New Request Option: <strong>??? &lt;Enter&gt;</strong></p>
<p>'10-55 PSC Form' Option name: RMPR 10-55 Synonym: 10</p>
<p>This will create a new FL 10-55 form and post purchasing data to patient's VAF 10-2319 record and update the Service's VAF 1358 obligation.</p>
<p>'2421 Form' Option name: RMPR 2421 Synonym: 24</p>
<p>This option will create a new VAF 10-2421 form, post to the patient's</p>
<p>VAF 10-2319, and update the VAF 1358 obligation.</p>
<p>'2520 Transaction without printing 10-55' Option name: RMPR 2520 Synonym: 25</p>
<p>For VAF 10-2520 PSC transactions that are under $300.00 and do not have an FL 10-55. It will then post to the VAF 1358 and patient's VAF 10-2319 record.</p>
</blockquote></td>
</tr>
</tbody>
</table>

[^1]: The Provider in this case is NOT the clinician. This person is the Prosthetics employee who initiates the transaction and is known by their Logon ID.

[^2]: Same as above.