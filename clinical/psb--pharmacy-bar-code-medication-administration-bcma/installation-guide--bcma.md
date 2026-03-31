---
consolidated_title: "bcma installation guide"
app_code: PSB
doc_type: IG
master_source: "BCMA Version 3 Installation Guide (updated PSB*3*157 February 2026)"
master_pub_date: February 2026
consolidated_from: 6 versions
prior_versions:
  - "BCMA Version 3 Installation Guide (updated PSB*3*101 Dec 2019)"
  - "BCMA Version 3 Installation Guide (Updated PSB*3*118 May 2019)"
  - "BCMA Version 3 Installation Guide (updated PSB*3*123 May 2021)"
  - "BCMA Version 3 Installation Guide (updated PSB*3*140 October 2023)"
  - "BCMA Version 3 Installation Guide (updated PSB*3*152 October 2025)"
---

---
---

BAR CODE MEDICATION ADMINISTRATION (BCMA)

![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/001.png)INSTALLATION GUIDE

February 2026

VISTA Health Systems Design & Development

Revision History

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/2026</td>
<td>PSB*3*157</td>
<td><p>Incident resolution.</p>
<p>Updated BCMA V. 3.0 Documentation and Related File Names table (<a href="#_Toc6806324">p. 13</a>)</p>
<p>Updated Client Files Distributed During BCMA V. 3.0 Installation table (<a href="#Client_files_distributed_table">p. 30</a>)</p></td>
</tr>
<tr class="even">
<td>09/2025</td>
<td>PSB*3*152</td>
<td><p>Delphi 12 Upgrade, incident resolution.</p>
<p>Updated BCMA V. 3.0 Documentation and Related File Names table (<a href="#_Toc6806324">p. 13</a>)</p>
<p>Updated Client Files Distributed During BCMA V. 3.0 Installation table (<a href="#Client_files_distributed_table">p. 30</a>)</p>
<p>Updated the software retrieval location information (p. <a href="#PSB_152_Software_Link_2">12</a>, <a href="#task-1-download-bcma-v.-3.0-software">25</a>)</p></td>
</tr>
<tr class="odd">
<td>12/2023</td>
<td>PSB*3*140</td>
<td><p>Delphi 11 Upgrade, include ORDERCOM.dll in installation wizard, p 23.</p>
<p>Added additional Optional Command Line Parameters SHOWCERTS, /K, and /IHS, p 27</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/2021</td>
<td>PSB*3*106</td>
<td>Added GUI Enhancements for Hazardous to Handle/Disposal of Drug, p 23.</td>
</tr>
<tr class="odd">
<td>5/2021</td>
<td>PSB*3*123</td>
<td><p>BCMA and BCMA Parameters are being converted to Delphi XE10.4 to make them TRM Compliant, and several reported defects were resolved, p 23.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2019</td>
<td>PSB*3*101</td>
<td><p>PSB*3*101 addresses reported defects in BCMA and BCMA parameters applications, p 23</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>5/2019</td>
<td>PSB*3*118</td>
<td><p>BCMA is being converted to Delphi XE10 and made Windows 10 compatible, p 23</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2018</td>
<td>PSB*3*96</td>
<td><p>Two-factor authentication (2FA) patch for BCMA is releasing a dll, OrderCom.dll, that is replacing the BCMAOrderCom.dll, p 23</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

Table of Contents

# BCMA V. 3.0 and This Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [BCMA V. 3.0 and This Guide](#bcma-v-30-and-this-guide)
- [Pre-Installation Information](#pre-installation-information)
- [# Installation Information](#installation-information)
- [Working with GUI BCMA V. 3.0](#working-with-gui-bcma-v-30)
- [Working with the Monthly SAGG Report](#working-with-the-monthly-sagg-report)
- [Glossary](#glossary)
  - [<table>](#table)
- [APPENDIX A: Sample KIDS Load & Installation](#appendix-a-sample-kids-load-installation)
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="tip-lightbulb-iconbenefits-of-bcma-v.-3.0">![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/002.png)Benefits of BCMA V. 3.0</h2></th>
<th><p>This section lists the National Online Information System (NOIS)tickets that are corrected in Bar Code Medication Administration (BCMA) V. 3.0, and provided in the Build description.</p>
<ol type="1">
<li><p><strong>Problem:</strong> NOIS ISB-0603-31561</p></li>
</ol>
<p>A medication order that has administration times set for today, but before the Start Time of the order, displays on the Bar Code Medication Administration (BCMA) Due List Report</p>
<p>Corrective Action:</p>
<p>The Due List Report will not display medication orders until the Start Date/Time of the medication order takes effect.</p>
<ol start="2" type="1">
<li><p><strong>Problem:</strong> NOIS ISB-0903-31964</p></li>
</ol>
<p>When the user selects a time frame for the Medication Administration History (MAH) Report and no administrations are due, the report lists the medication order number from Inpatient Medications V. 5.0 under the “Initial – Name Legend” section.</p>
<p>Corrective Action:</p>
<p>The MAH Report will not display the order number from Inpatient Medications V. 5.0 under the “Initial – Name Legend” section when no administrations are due for a specific time frame.</p>
<ol start="3" type="1">
<li><p><strong>Problem:</strong> NOIS LAH-1203-61493</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 66%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th>Benefits of BCMA V. 3.0 (cont.)</th>
<th><p>The user receives the following error message, “BCMA failed to communicate with VISTA,” if the Graphical User Interface (GUI) BCMA times out and is unable to connect to the server.</p>
<p><strong>Corrective Action:</strong></p>
<p>The processing time for the GUI BCMA software to display the patient’s record on the BCMA Virtual Due List (VDL) has been reduced.</p>
<ol start="4" type="1">
<li><p><strong>Problem:</strong> NOIS LIT-0603-71923</p></li>
</ol>
<p>Users sometimes receive an “allocation failure” error message when accessing a patient’s record using the GUI BCMA.</p>
<p><strong>Corrective Action:</strong></p>
<p>The “allocation failure” error message has been corrected.</p>
<ol start="5" type="1">
<li><p><strong>Problem:</strong> NOIS MAD-1203-42204</p></li>
</ol>
<p>The MAH Report takes an extended amount of time to run if the Start Date and the Stop Date of the report, requested by the user, are for different years. For example, if the Start Date is 12/28/03 and the Stop Date is 01/03/04.</p>
<p><strong>Corrective Action:</strong></p>
<p>The user can now request different years for the MAH Report without experiencing extended delays as BCMA accesses the data.</p>
<ol start="6" type="1">
<li><p><strong>Problem:</strong> NOIS MIN-1203-41637</p></li>
</ol>
<p>Users sometimes experience an “Invalid Medication Lookup” error message after scanning a medication in the “Scan Medication Bar Code:”</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Benefits of BCMA V. 3.0 (cont.)</p>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/003.png)</p></td>
<td colspan="2"><p>field of the “Order Manager” dialog box when using the BCMA Med Order Button in GUI BCMA.</p>
<p><strong>Corrective Action:</strong></p>
<p>The BCMA medication lookup process has been corrected to properly validate the medications scanned in the “Scan Medication Bar Code:” field of the “Order Manager” dialog box in GUI BCMA.</p>
<ol start="7" type="1">
<li><p><strong>Problem:</strong> NOIS UNY-0104-10174</p></li>
</ol>
<p>Multiple IV medication orders display as merged on the IV Medication Tab after an order is discontinued, but the IV bag is still infusing.</p>
<p><strong>Corrective Action:</strong></p>
<p>Multiple IV medication orders will display properly on the IV Medication Tab.</p>
<ol start="8" type="1">
<li><p><strong>Problem:</strong> NOIS TNV-0104-30647</p></li>
</ol>
<p>Users sometimes experience the following error message, “ERROR: 16^Server Protocol Disabled,” when using the Edit Medication Log [PSB MED LOG EDIT] option. This occurs when the PSB BCMA RASO17 SRV Health Level Seven (HL7) server protocol is being disabled.</p>
<p><strong>Corrective Action:</strong></p>
<p>The error message is only intended to notify the BCMA software that the protocol is being disabled. BCMA will now validate the message and not display it to users.</p>
<ol start="9" type="1">
<li><p><strong>Problem:</strong> NOIS ISB-0104-31384</p></li>
</ol></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Benefits of BCMA V. 3.0 (cont.)</th>
<th><p>When an IV medication order with an infusing bag is “Renewed,” the renewed order continues to display on the IV Medication Tab of the BCMA VDL until the infusing bag is “Completed,” even if the “Renewed” order’s Start Date/Time has expired.</p>
<p><strong>Corrective Action:</strong></p>
<p>When an IV medication order with an infusing bag is “Renewed,” the renewed order will continue to display on the IV Medication Tab of the BCMA VDL until the infusing bag is “Completed,” or until the Start Date/Time of the new order that was created during the renewal process. Once the new order is active, the infusing bag from the previous order will display on the BCMA VDL with the new order, along with any additional bags created from the new order. Any available bags from the previous order will display on the new order based on the IV Site Parameter settings in the GUI BCMA Site Parameters application.</p>
<p>This section provides an overview of the major changes in the Bar Code Medication Administration (BCMA) V. 3.0 software such as the new routines and files, Phase Release changes, and maintenance fixes. This version also includes enhancements, which are a direct result of feedback from the BCMA Workgroup and our many end users, and included in Phase Releases I-IV.</p>
<h3 id="patient-transfer-notification-message">Patient Transfer Notification Message</h3>
<p>The Patient Transfer Notification Information message displays when you open a patient’s record, or view the Unit Dose or the IVP/IVPB Medication Tab for the first time. It indicates that the patient has had a movement type (usually a transfer) within the Patient Transfer Notification Timeframe site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Benefits of BCMA V. 3.0 (cont.)</td>
<td><p>You can define this site parameter, by division, with a minimum value of 2 and a maximum value of 99. The default is 72 hours.</p>
<p><strong>Note:</strong> The display of the message is dependent on the last action displayed in the “Last Action” column of the BCMA VDL. BCMA then evaluates the last action performed on a medication each time the Unit Dose or the IVP/IVPB Medication Tabs are refreshed.</p>
<h3 id="documenting-fractional-dose-orders">Documenting Fractional Dose Orders</h3>
<p>You can document Fractional Dose medication orders on the Unit Dose and the IVP/IVPB Medication Tabs. This functionality alerts you when dispensed drug dosages need to be administered to a patient in “fractional” doses so you can provide comments about this order type once administered. The Fractional Dose dialog box displays when the units per dose is fractional and <em>less than</em> 1.0. The Multiple/ Fractional Dose dialog box displays when the units per dose is <em>greater than</em> 1.0.</p>
<p><strong>Note:</strong> If you do not scan once for each unit listed in the Multiple/Fractional Dose dialog box, the Confirmation dialog box displays requesting that you confirm the actual total units administered.</p>
<h3 id="bcma-clinical-reminders-marquee">BCMA Clinical Reminders Marquee</h3>
<p>Located in the lower, right-hand corner of the BCMA VDL, this “marquee” identifies Pro Re Nata (PRN) medication orders needing effectiveness documentation. The setting is based on the PRN Documentation site-definable parameter, and applies to current admissions or to the site parameter timeframe (whichever is greater). Values can be set from 1-999, with 72 hours the default setting. A “mouse-over” list, in the PRN Effectiveness Activity area, provides the four most recent PRN orders that need comments.</p></td>
</tr>
<tr class="even">
<td><p>Benefits of BCMA V. 3.0 (cont.)</p>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/004.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/005.png)</p></td>
<td><h3 id="prn-documentation-site-parameter">PRN Documentation Site Parameter</h3>
<p>The PRN Documentation site parameter lets you define the minimum number of hours from NOW that BCMA will search for PRN medication orders needing effectiveness comments. The four most recent PRN orders that need documentation display within the PRN Effectiveness mouse-over list in the “BCMA Clinical Reminders” marquee, located in the lower, right-hand corner of the BCMA VDL.</p>
<p>The allowable entry for this parameter, definable by division, is a minimum value of 1 and a maximum value of 999. The default is 72 hours.</p>
<h3 id="include-schedule-types-site-parameter">Include Schedule Types Site Parameter</h3>
<p>You can automatically display PRN medication orders when the BCMA VDL is first opened by selecting the PRN check box in the “Include Schedule Types” area of the GUI BCMA Site Parameters application. This parameter controls the default display of PRN medications on the BCMA Character-based User Interface (CHUI) Due List and the BCMA VDL — even if you change the Schedule Types or Medication Tab during a medication pass.</p>
<p>Your medical center can choose to have the PRN Schedule Types display on the BCMA VDL by default, or to display PRN medications once a clinician selects the PRN Schedule Type check box on the BCMA VDL. All other Schedule Types will display by default and cannot be changed.</p>
<h3 id="accessing-prn-effectiveness-log">Accessing PRN Effectiveness Log</h3>
<p>You can quickly access the PRN Effectiveness Log dialog box by selecting a medication on the BCMA VDL, and then selecting the PRN Effectiveness command from the Right Click drop-down menu.</p></td>
</tr>
<tr class="odd">
<td>Benefits of BCMA V. 3.0 (cont.)</td>
<td><p>The PRN Effectiveness Log displays the patient’s medication information at the top of the box, under the Selected Administration area, and all PRN medication administrations in the PRN List table. Once a medication is selected, the “Selected Administration” area of the dialog box populates with administration information. The Med History button on the dialog box displays the Medication History Report for the orderable item listed in the ”Selected Administration” area of the dialog box.</p>
<h3 id="schedule-type-indicator-alert-lights">Schedule Type Indicator Alert Lights</h3>
<p>In the Schedule Type area of the BCMA VDL, a <strong>GREEN</strong> “alert light” indicates that a medication order exists for the Schedule Type selected within the respective start/stop date and time selected on the BCMA VDL. If grayed out, then none exist.</p>
<h3 id="medication-log-dialog-box">Medication Log Dialog Box</h3>
<p>The Medication Log dialog box includes the Vitals area, which displays the four previous vitals entries for each of the Vital signs listed in the area. The “+” (plus) sign, to the left of a Vital sign, expands the row to reveal additional entries. The “–” (minus) sign collapses the row to hide all, but the most recent entry.</p>
<h3 id="prn-effectiveness-dialog-box">PRN Effectiveness Dialog Box</h3>
<p>The PRN Effectiveness dialog box includes the Vitals area, which displays the four previous vitals entries for each of the Vital signs listed in the area. The “+” (plus) sign, to the left of a Vital sign, expands the row to reveal additional entries. The “–” (minus) sign collapses the row to hide all, but the most recent entry.</p>
<h3 id="bag-information-column-on-vdl">Bag Information Column on VDL</h3>
<p>This new column on the BCMA VDL identifies an IV order that currently has an IV bag with a status of Infusing or Stopped. It also identifies orders that have changed since the Infusing or Stopped IV bag was first infused.</p></td>
</tr>
<tr class="even">
<td>Benefits of BCMA V. 3.0 (cont.)</td>
<td><h3 id="scan-iv-dialog-box">Scan IV Dialog Box</h3>
<p>The “Bag Information” title/area at the top of the Scan IV dialog box has been replaced with “IV Bag #.” BCMA populates this area with pertinent information about the IV bag selected on the BCMA VDL. The “Other Print Info” title has been replaced with “Order Changes,” which now displays changes to an IV order, which have an Infusing or Stopped IV bag.</p>
<h3 id="report-printing">Report Printing</h3>
<p>Here’s the changes to the report printing functionality in BCMA V. 3.0:</p>
<ul>
<li><p><strong>Medication Administration History (MAH) Report:</strong> The Date column lists three asterisks (*) to indicate that a medication is not due. This information is also noted in the Legend at the bottom of the MAH Report.</p></li>
</ul>
<p>The report also includes information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</p>
<ul>
<li><p><strong>Medication Variance Report:</strong> Provides “exceptions” (variances) to the medication administration process. It also lists “event” information within a selected date range, such as the type and number of events, and the total percentage of events that occurred. A variance preceded by a minus sign (such as –24) indicates the number of minutes that a medication was given before the administration time.</p></li>
<li><p><strong>Cumulative Vitals/Measurement Report:</strong> Lists a patient’s vitals from the Vitals package, along with their demographics and hospital location information. You cannot print this report by ward.</p></li>
</ul></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Benefits of BCMA V. 3.0 (cont.)</th>
<th><ul>
<li><p><strong>Ward-Specific Reports:</strong> Simply click CANCEL at the Patient Lookup dialog box to access the Menu Bar — without opening a patient record — and print ward-specific reports only, except for the Cumulative Vitals/Measurement Report. A patient’s file must be opened to access patient-specific reports.</p></li>
<li><p><strong>Missed Medications Report:</strong> Indicates when a medication order is placed “On Hold” and taken “Off Hold” in CPRS or Inpatient Medications V. 5.0. The Hold information is provided below the medication information on the report, and only applies to administrations due within the Hold timeframe.</p></li>
</ul>
<p>The “Order Num” column on the report lists the actual order number and order type (i.e., Unit Dose or IV). This information is quite helpful when troubleshooting problems with BCMA.</p>
<ul>
<li><p><strong>CHUI Missing Dose Report:</strong> Changed the line item “Dosage Schedule” on the BCMA CHUI Missing Dose Report to “Schedule” to coincide with the Missing Dose E-mail Notification change described on the next page.</p></li>
</ul>
<h3 id="hl7-messaging">HL7 Messaging</h3>
<p>BCMA V. 3.0 supports “Health Level Seven (HL7),” a standard package (<strong>V</strong><em>IST</em><strong>A</strong> Messaging) used with M-based applications for conducting HL7 transactions. This package provides the facilities to create, transmit, and receive HL7 messages over a variety of transport layers. BCMA only exports HL7 messages.</p>
<h3 id="missing-dose-e-mail-notification">Missing Dose E-Mail Notification</h3>
<p>The e-mail notification that is sent from BCMA to the Pharmacy, when you submit a Missing Dose Request, now includes “Schedule” information.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">Benefits of BCMA V. 3.0 (cont.)</td>
<td><h3 id="documenting-prn-pain-scores">Documenting PRN Pain Scores</h3>
<p>With BCMA V. 3.0, you can perform the following tasks with regards to documenting PRN pain scores:</p>
<ul>
<li><p><strong>Define Items:</strong> In the “Reason Medication Given PRN” default Answer Lists of the GUI BCMA Site Parameters application you can identify those items that will require the documentation of a pain score within BCMA. The pain score will be documented and stored in the Vitals package.</p></li>
<li><p><strong>Select a Pain Score:</strong> When documenting an administration for a PRN medication, you can select a pain score from a pre-defined list.</p></li>
</ul>
<p>Access a Pain Score: When documenting the effectiveness for a PRN medication, you can access pain score information for the patient.</p>
<h3 id="administering-a-multiple-dose-order">Administering a Multiple Dose Order</h3>
<p>If you do not scan once for each Unit Dose or IVP medication listed in the Multiple Dose dialog box, BCMA displays the Confirmation dialog box informing you to scan additional units. The Multiple Dose dialog box retains the data that you entered before receiving the message.</p>
<h3 id="administering-a-prn-order">Administering a PRN Order</h3>
<p>In the Medication Log dialog box, you can select the patient’s pain score, between 0 and 10 or 99, with “0” being No Pain, “10” the Worst Imaginable, and “99” for “Unable to Respond.”</p>
<h3 id="recording-the-effectiveness-of-a-prn-medication">Recording the Effectiveness of a PRN Medication</h3>
<p>In the PRN Effectiveness Log dialog box, you can select the patient’s pain score, between 0 and 10 or 99, with “0” being No Pain, “10” the Worst Imaginable, and “99” for “Unable to Respond.”</p></td>
</tr>
<tr class="even">
<td>Benefits of BCMA V. 3.0 (cont.)</td>
<td><h3 id="creating-default-answers-lists">Creating Default Answers Lists </h3>
<p>In the GUI BCMA Site Parameters application, the Attribute column is available only when you choose the Default Answer Lists Tab and select the “Reason Medication Given PRN” list. This column identifies that a Pain Score is required from the patient when a clinician administers a specific medication.</p>
<p>When you select the “Requires Pain Score” check box when adding or renaming a “Reason Medication Given PRN” item, you must choose a pain score in the BCMA Medication Log and PRN Effectiveness dialog boxes when administering a medication.</p></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="benefits-of-this-guide">Benefits of This Guide</h2></th>
<th><p>Preparing your site for the installation and implementation of BCMA V. 3.0 helps to ensure a smooth integration. This Installation Guide is designed to help you do just that. It includes detailed information such as system requirements; installation time estimates and instructions; and procedures that will get you up and running quickly with BCMA V. 3.0.</p>
<h3 id="our-target-audience">Our Target Audience</h3>
<p>We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package.</p>
<ul>
<li><p>Development Engineering</p></li>
<li><p>Information Resources Management (IRM)</p></li>
<li><p>Clinical Application Coordinator (CAC) – called Applications Package Coordinator (ADPAC) at some sites</p></li>
<li><p>Enterprise <strong>V</strong><em>IST</em><strong>A</strong> Support (EVS)</p></li>
<li><p>Software Quality Assurance (SQA)</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="other-sources-of-information">Other Sources of Information</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/006.png)</p></th>
<th><p>Refer to the Web sites listed below when you want to receive more background and technical information about BCMA V. 3.0, and to download this manual and related documentation.</p>
<h3 id="backgroundtechnical-information">Background/Technical Information</h3>
<p>From your Intranet, enter <mark>REDACTED</mark> in the Address field to access the BCMA Main Web page.</p>
<h3 id="this-manual-and-related-documentation">This Manual and Related Documentation</h3>
<p>From your Intranet, enter <a href="http://www.va.gov/vdl">http://www.va.gov/vdl</a> in the Address field to access this manual, and those listed below, from the <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL).</p>
<ul>
<li><p>Technical Manual/Security Guide</p></li>
<li><p>GUI User Manual</p></li>
<li><p>Nursing CHUI User Manual</p></li>
<li><p>Pharmacy CHUI User Manual</p></li>
<li><p>Manager’s User Manual</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="tip-bookmark-these-sites-for-future-reference.documentation-retrieval-process">![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/007.png)Documentation Retrieval Process</h2></th>
<th><p>Your site can retrieve the BCMA V. 3.0 documentation listed below from the following location, /srv/vista/patches/SOFTWARE</p>
<p><span id="PSB_152_Software_Link_2" class="anchor"></span>Software files can also be obtained by accessing</p>
<p>the URL: <a href="https://download.vista.med.va.gov/index.html/SOFTWARE">https://download.vista.med.va.gov/index.html/SOFTWARE</a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<span id="_Toc6806324" class="anchor"></span>
Example: BCMA V. 3.0 Documentation and Related File names
|                                 |                                   |
|---------------------------------|-----------------------------------|
| BCMA V. 3.0 Documentation       | Documentation File name           |
| Installation Guide              | PSB_3_P157_IG.PDF                 |
| Technical Manual/Security Guide | PSB_3_TM.PDF                      |
| GUI User Manual                 | PSB_3_UM.PDF                      |
| Nursing CHUI User Manual        | PSB_3_UM_NURSE_CHUI_R1216.PDF     |
| Pharmacy CHUI User Manual       | PSB_3_0_UM_P106_PHARM_CHUI_UM.PDF |
| Manager’s User Manual           | PSB_3_UM_MAN_UM.PDF               |
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="tip-in-a-chui-environment-when-you-press-enter-instead-of-typing-a-response-the-system-accepts-the-default-value-shown-to-the-left-of-the-double-slash-at-a-prompt-or-a-field.conventions-used-in-this-guide">![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/008.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/009.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/010.png)Conventions Used in This Guide</h2></th>
<th><p>Before installing BCMA V. 3.0, review this section to learn the many conventions used throughout this guide.</p>
<ul>
<li><p><strong>Keyboard Responses:</strong> Keys provided in <strong>boldface</strong>, within the steps, help you quickly identify what to press on your keyboard to perform an action. See the examples provided below.</p></li>
</ul>
<ul>
<li><p>Within the Steps: At the “Select Kernel Installation &amp; Distribution System Option:” prompt, type INSTALL, and then press <span class="smallcaps">enter.</span></p></li>
<li><p>Within Screen Captures: Text in boldface, centered between arrows on screen captures, identifies the key you must press for the system to capture your response or to move the cursor to the next field. See the following example.</p></li>
</ul>
<ul>
<li><p><strong>Mouse Responses:</strong> Buttons provided in <strong>boldface</strong>, within the steps, indicate what you should click on your computer screen using the mouse. For example, when you see <strong><span class="smallcaps">next, yes/no,</span></strong> or <strong><span class="smallcaps">ok</span></strong> in the steps, click the appropriate button on your computer screen.</p></li>
<li><p><strong>User Responses:</strong> Information presented in <strong>boldface</strong>, within steps or shaded screen captures, indicate what you should “type” (enter) onto your computer screen. See the examples provided below.</p></li>
</ul>
<ul>
<li><p>Within the Steps: At the “Select OPTION NAME:” prompt, type XPD MAIN and then press <span class="smallcaps">enter</span>.</p></li>
<li><p>Within Screen Captures: See the following example.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Conventions Used in This Guide (cont.)</p>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/011.png)</p></td>
<td><ul>
<li><p><strong>Screen Captures:</strong> Provide “shaded” examples of what you will see on your computer screen, and possible user responses.</p></li>
<li><p><strong>Notes:</strong> Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our staff, developers, and testers.</p></li>
<li><p><strong>Tips:</strong> Located in the left margin, these helpful hints are designed to help you work more efficiently with<br />
BCMA V. 3.0.</p></li>
<li><p><strong>Menu Options:</strong> When provided in <em>italics</em>, identifies a menu option. When provided in <strong>boldface</strong>, ALL CAPS, identifies the letters that you should type onto your computer screen, before pressing <span class="smallcaps"><strong>enter</strong>.</span> The system then goes directly to the menu option. (<strong>Note:</strong> The letters do not have to be entered as capital letters, even though they are provided within the steps in this format.) See the examples provided below.</p></li>
</ul>
<ul>
<li><p>Italicized: Use the Kernel <em>First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of every PSB routine.</p></li>
<li><p>Capitalized: At the “Taskman Management Option:” prompt, type SCHEDule/Unschedule Options, and then press <span class="smallcaps">enter</span>.</p></li>
</ul></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="obtaining-on-line-help">Obtaining On-line Help</h2></th>
<th><p>On-line help is designed right into the Graphical User Interface (GUI) and Character-based User Interface (CHUI) versions of BCMA V. 3.0, making it quick and easy for you to get answers to your questions. Here’s how to access help in both versions of BCMA V. 3.0:</p>
<ul>
<li><p><strong>GUI BCMA:</strong> Provides context-sensitive, on-line help and the Help menu.</p></li>
</ul>
<ul>
<li><p><strong>Context-Sensitive Help:</strong> Place your “focus” on a feature, button, or Tab on the BCMA VDL, using the <strong><span class="smallcaps">tab</span></strong> key, and then press <strong><span class="smallcaps">f1</span></strong> to receive help specific to that area of the BCMA VDL. In the case of a command, first highlight it in the Menu Bar or Right Click drop-down menu, and then press <span class="smallcaps"><strong>f1</strong>.</span></p></li>
<li><p><strong>Help Menu:</strong> Open the Help menu, and then choose the Contents and Index command to receive help for every feature in GUI BCMA V. 3.0.</p></li>
</ul>
<ul>
<li><p><strong>CHUI BCMA:</strong> Lets you enter up to two question marks at any prompt to receive on-line help.</p></li>
</ul>
<ul>
<li><p><strong>One Question Mark:</strong> Provides a brief statement related to the prompt.</p></li>
</ul>
<p><strong>Two Question Marks:</strong> Displays more detailed information about the prompt, plus any hidden<br />
actions</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="locating-detailed-listings">Locating Detailed Listings</h2></th>
<th><p>You can obtain and print listings about BCMA V. 3.0 routines, and Data Dictionaries using the information provided below.</p>
<h3 id="routines">Routines</h3>
<p>Use the Kernel routine XINDEX to produce detailed listings of routines. Use the Kernel <em>First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of every PSB routine.</p>
<h3 id="data-dictionaries">Data Dictionaries</h3>
<p>You can use the VA FileMan <em>List File Attributes</em> [DILIST] option, under the <em>Data Dictionary Utilities</em> [DI DDU] option, to print the Dictionaries.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="minimum-required-packages">Minimum Required Packages</h2></th>
<th>Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Minimum Required Packages and Versions

|                               |                        |
|-------------------------------|------------------------|
| Package                       | Minimum Version Needed |
| Inpatient Medications         | 5.0                    |
| Kernel                        | 8.0                    |
| MailMan                       | 8.0                    |
| Nursing                       | 4.0                    |
| Order Entry/Results Reporting | 3.0                    |
| Pharmacy Data Management      | 1.0                    |
| RPC Broker (32-bit)           | 1.1                    |
| Toolkit                       | 7.3                    |
| VA FileMan                    | 22.0                   |
| Vitals/Measurements           | 5.0                    |

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="important-you-should-install-and-test-bcma-in-your-test-accounts-before-installing-in-your-production-accounts.installation-time-estimates">![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/012.png)Installation Time Estimates</h2></th>
<th><p>On average, it takes approximately two minutes to install BCMA V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its’ system resources.</p>
<p>Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="tip-the-approximate-size-for-psb-was-calculated-using-a-normal-medication-pass-for-a-unit-dose-and-an-iv-medication-order.-this-is-only-an-estimated-number-it-serves-as-the-mean.resource-requirements">![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/013.png)Resource Requirements</h2></th>
<th><p>This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.</p>
<ul>
<li><p>Routines 60</p></li>
<li><p>Globals 1 (^PSB)</p></li>
<li><p>Files 5 (53.66-53.79)</p></li>
<li><p>^PSB Size Unit Dose = 300 x # of Medications<br />
(in bytes) Administered<br />
IV = 2100 x # of IV Bags<br />
Administered</p></li>
<li><p>FTEE Support .2</p></li>
<li><p>FTEE Maintenance .2</p></li>
</ul>
<h3 id="response-time-monitor">Response Time Monitor</h3>
<p>BCMA V. 3.0 does not include Response Time Monitor hooks.</p>
<h3 id="laptops-and-bar-code-scanners">Laptops and Bar Code Scanners</h3>
<p>The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas, at your site, that use BCMA V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.</p>
<h3 id="printers">Printers</h3>
<p>Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Resource Requirements (cont.)</th>
<th><p><strong>Unit Dose Label Printer Devices</strong></p>
<p>BCMA V. 3.0 includes the <em>Label print</em> [PSBO BL] option for printing individual or batch Unit Dose bar code labels. It is specifically coded to the Zebra-brand printers using the Zebra Programming Language (ZPL). Model 105SE was used in the development of the labels. Routine PSBO BL uses site-specific printers or terminals to produce labels.</p>
<h3 id="iv-label-printer-devices">IV Label Printer Devices</h3>
<p>Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section “Interfacing with the Bar Code Label Printer” in the Inpatient Medications V. 5.0 Technical Manual/Security <em>Guide</em> for detailed setup information.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="client-pc-setup-requirements">Client PC Setup Requirements</h2></th>
<th><p>Once all BCMA V. 3.0 files are installed, make sure that every Client PC includes the minimum system <em>before</em> users run BCMA V. 3.0 from it. BCMA must be installed via an account that has Administrative privileges.</p>
<p>For specific Client PC Setup Requirements, see the “VA Standard Desktop Configurations” link below, which provides the current corporate software and hardware configurations per VA Directive 6401.</p>
<p><mark>REDACTED</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="files-required-to-run-bcma-v.-3.0">Files Required to Run BCMA V. 3.0</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/014.png)</p></th>
<th><p>BCMA V. 3.0 uses the following files installed on the <strong>V</strong><em>IST</em><strong>A</strong> Server. “Journaling” is recommended.</p>
<ul>
<li><p>^PSB (53.66, BCMA IV Parameters</p></li>
<li><p>^PSB (53.68, BCMA Missing Dose Request</p></li>
<li><p>^PSB (53.69, BCMA Report Request</p></li>
<li><p>^PSB (53.78, BCMA Medication Variance Log</p></li>
<li><p>^PSB (53.79, BCMA Medication Log</p></li>
</ul>
<p><strong>Note:</strong> You can learn more about these files by generating a list with file attributes using VA FileMan</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="routines-installed">Routines Installed</h2></th>
<th><p>Review the listing below to learn the routines installed on to your site’s <strong>V</strong><em>IST</em><strong>A</strong> Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.</p>
<p><strong>Note:</strong> You can use the <em>Kernel First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of each PSB routine.</p>
<h3 id="routine-mapping">Routine Mapping</h3>
<p>At this time, we do <em>not</em> offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: BCMA V. 3.0 Routines Installed on to VISTA Server

PSBALL PSBAPIPM PSBCHIVH PSBCHKIV PSBMD PSBML PSBML1 PSBMLEN

PSBMLEN1 PSBMLHS PSBMLTS PSBMLU PSBMLVAL PSBO PSBO1 PSBOAL

PSBOBL PSBODL PSBODL1 PSBODO PSBOHDR PSBOMD PSBOMH PSBOMH1

PSBOMH2 PSBOML PSBOMM PSBOMV PSBOPE PSBOPI PSBOPM PSBOVT

PSBOWA PSBPAR PSBPARIV PSBPOIV PSBPRN PSBRPC PSBRPC1 PSBRPC2

PSBRPC3 PSBRPCMO PSBRPCXM PSBSAGG PSBSVHL7 PSBUTL PSBVAR PSBVDLIV

PSBVDLPA PSBVDLPB PSBVDLTB PSBVDLU1 PSBVDLU2 PSBVDLU3 PSBVDLUD PSBVDLVL

PSBVITFL PSBVT PSBVT1 PSBXMRG

60 routines

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="routines-with-related-checksums">Routines with Related Checksums</h3></th>
<th>This section lists the routines and related checksums for BCMA V. 3.0 provided during the installation process.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: BCMA V. 3.0 Routines with Related Checksums

Select BUILD NAME: PSB 3.0 BAR CODE MED ADMIN

PSBALL value = 1475151

PSBAPIPM value = 9031085

PSBCHIVH value = 1166996

PSBCHKIV value = 35513271

PSBMD value = 17319681

PSBML value = 23421797

PSBML1 value = 7074072

PSBMLEN value = 18077803

PSBMLEN1 value = 9220985

PSBMLHS value = 2525483

PSBMLTS value = 8100734

PSBMLU value = 1498988

PSBMLVAL value = 9734944

PSBO value = 17926200

PSBO1 value = 2876667

PSBOAL value = 1806300

PSBOBL value = 4045534

PSBODL value = 16589922

PSBODL1 value = 8836828

PSBODO value = 2948451

PSBOHDR value = 5286664

PSBOMD value = 6143174

PSBOMH value = 20105393

PSBOMH1 value = 20721307

PSBOMH2 value = 9443664

PSBOML value = 10399745

PSBOMM value = 21442785

PSBOMV value = 13276146

PSBOPE value = 7022505

PSBOPI value = 288600

PSBOPM value = 4855752

PSBOVT value = 790819

PSBOWA value = 13904863

PSBPAR value = 6032995

PSBPARIV value = 16437954

PSBPOIV value = 24363099

PSBPRN value = 7079605

PSBRPC value = 10743383

PSBRPC1 value = 5473533

PSBRPC2 value = 20110546

PSBRPC3 value = 194738

PSBRPCMO value = 18080428

PSBRPCXM value = 2728593

PSBSAGG value = 1431404

PSBSVHL7 value = 16217830

PSBUTL value = 14185290

PSBVAR value = 4760179

PSBVDLIV value = 17858201

PSBVDLPA value = 4059667

PSBVDLPB value = 19523684

PSBVDLTB value = 3557813

PSBVDLU1 value = 18022165

PSBVDLU2 value = 4610568

PSBVDLU3 value = 3001261

PSBVDLUD value = 18568646

PSBVDLVL value = 23162182

PSBVITFL value = 2483832

PSBVT value = 22976876

PSBVT1 value = 767427

PSBXMRG value = 1576759

# # Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="vista-server-installation-instructions">V<em>IST</em>A Server Installation Instructions</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/015.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/016.png)</p></th>
<th><p>Perform the steps provided below to download BCMA V. 3.0 from an FTP Server. Then you will be ready to use this section for loading the Kernel Installation &amp; Distribution System (KIDS) Distribution file and the Broker Server file, and for installing BCMA V. 3.0 on to the <strong>V</strong><em>IST</em><strong>A</strong> Server.</p>
<p><strong>Attention:</strong> BCMA V. 3.0 includes a new GUI executable file. Installation of this GUI is NOT required immediately after the KIDS install for the software to function. The installation process will make significant changes to routines, files, and files within the BCMA<br />
V. 3.0 application. Review the bulleted list below, taken from the Build description, for more information.</p>
<ul>
<li><p>Prior clients compatible with BCMA V. 3.0: 2.0.36.14</p></li>
<li><p>Client can be copied instead of installed: Yes</p></li>
</ul>
<h3 id="task-1-download-bcma-v.-3.0-software">Task 1: Download BCMA V. 3.0 Software</h3>
<p>Use the following information to download BCMA V. 3.0 from an FTP Server.</p>
<ol type="1">
<li><p>Download the GUI BCMA file PSB3_0.exe, the Host File PSB_3_0.KID from the following location,</p></li>
</ol>
<p>/srv/vista/patches/SOFTWARE</p>
<p>Software files can also be obtained by accessing</p>
<p>the URL: <a href="https://download.vista.med.va.gov/index.html/SOFTWARE">https://download.vista.med.va.gov/index.html/SOFTWARE</a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>V<em>IST</em>A Server Installation Instructions (cont.)</th>
<th><ul>
<li><p>.EXE or .PDF files need to be FTP in BINARY.</p></li>
<li><p>KIDS Build needs to be FTP in ASCII.</p></li>
</ul>
<ol start="2" type="1">
<li><p>Move the files to the appropriate directory on your system.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>V<em>IST</em>A Server Installation Instructions (cont.)</th>
<th><h3 id="task-2-load-the-kids-distribution-file">Task 2: Load the KIDS Distribution File</h3>
<p>Perform the steps listed below to load the KIDS Distribution file.</p>
<ol type="1">
<li><blockquote>
<p>Sign in to the UCI where the KIDS Distribution file will be loaded and BCMA V. 3.0 will be installed.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Select OPTION NAME:” prompt, type <strong>XPD MAIN</strong>, and then press <strong><span class="smallcaps">enter</span>.</strong></p>
</blockquote></li>
<li><blockquote>
<p>At the “Select Kernel Installation &amp; Distribution System Option:” prompt, type <strong>INSTALL</strong>ation, and then press <strong><span class="smallcaps">enter</span></strong>.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Select Installation Option:” prompt, type <strong>Load a Distribution</strong>, and then press <strong><span class="smallcaps">enter</span></strong> to prepare for loading the KIDS Distribution file.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Enter a Host File:” prompt, type <strong>the directory where you have stored the Host File</strong>, followed by PSB_3_0.KID. Then press <strong><span class="smallcaps">enter</span></strong>.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Want to Continue with Load YES//?” prompt, press <strong><span class="smallcaps">enter</span></strong>. The system then loads the file to this location.</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>VISTA Server Installation Instructions (cont.)</th>
<th><h3 id="task-3-install-bcma-v.-3.0">Task 3: Install BCMA V. 3.0</h3>
<p>Now you are ready to install BCMA V. 3.0 on to the <strong>V</strong><em>IST</em><strong>A</strong> Server. Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.</p>
<blockquote>
<p>Note: You should perform step #1 listed below <em>now</em> if you are planning to install BCMA V. 3.0 immediately. However, if you are installing the application at another time, ask users to log off your system at that time.</p>
</blockquote>
<ol type="1">
<li><p>From the Facility Tab of the GUI BCMA Site Parameters application, take BCMA users offline.</p></li>
<li><p>Request that all BCMA users log off BCMA.</p></li>
<li><p>Review mapped sets for PSB* namespaces.</p></li>
</ol>
<ul>
<li><blockquote>
<p>If the routines are mapped, remove them from the mapped set at this time.</p>
</blockquote></li>
</ul>
<ol start="4" type="1">
<li><p>Backup your system. This step is optional but recommended.</p></li>
<li><p>At the “Select INSTALL NAME:” prompt, type PSB 3.0 and then press <strong><span class="smallcaps">enter</span></strong> to install BCMA V. 3.0. This Build provides all of the routines and files necessary for BCMA V. 3.0.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>VISTA Server Installation Instructions (cont.)</th>
<th><p>Task 3: Install BCMA V. 3.0 (cont.)</p>
<ol start="6" type="1">
<li><p>At the “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” prompt, type <strong>NO</strong>, and then press <span class="smallcaps"><strong>enter</strong>.</span></p></li>
<li><p>At the “Want KIDS to INHIBIT LOGONs during the install? YES//” prompt, type <strong>NO</strong>, and then press <span class="smallcaps"><strong>enter</strong>.</span></p></li>
<li><p>At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” prompt, type <strong>NO</strong>, and then press <span class="smallcaps"><strong>enter</strong>.</span></p></li>
<li><p>At the “DEVICE:” prompt, press <strong><span class="smallcaps">enter</span></strong> to use the default device HOME (the screen) for printing the Installation message. If you want to print a hard copy, enter your site printer, and then press <strong><span class="smallcaps">enter.</span></strong></p></li>
<li><p>If routines were unmapped as part of the installation process, return them to the mapped set once the installation of<br />
BCMA V. 3.0 is completed.</p></li>
<li><p>From the Facility Tab of the GUI BCMA Site Parameters application, place BCMA V. 3.0 back on-line.</p></li>
</ol>
<h3 id="additional-preparation-for-bcma-v.-3.0">Additional Preparation for BCMA V. 3.0</h3>
<p>Now you are ready to perform the steps listed below to further prepare your site and staff for using BCMA V. 3.0.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>VISTA Server Installation Instructions (cont.)</th>
<th><ol type="1">
<li><p>If you are a Micronectics Standard MUMPS (MSM) site, move the PSB routines only, to all nodes.</p></li>
<li><p>Assign the following security keys to appropriate site personnel.</p></li>
</ol>
<ul>
<li><p><strong>PSB MANAGER</strong> – designates the holder as a manager</p></li>
<li><p><strong>PSB INSTRUCTOR</strong> – designates the holder as a nursing instructor supervising student nurses</p></li>
<li><p><strong>PSB STUDENT</strong> – designates the holder as a student nurse, requiring that an instructor also sign on to BCMA V. 3.0 at the same time</p></li>
<li><p><strong>PSB CPRS MED BUTTON</strong> – designates the holder as a nurse who can document administered verbal- and phone-type STAT and NOW orders using the CPRS Med Order Button on the BCMA V. 3.0 VDL</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Working with GUI BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="client-pc-setup-requirements-1">Client PC Setup Requirements</h2></th>
<th><p>Once all BCMA V. 3.0 files are installed, make sure that every Client PC includes the minimum system configuration <em>before</em> users run BCMA V. 3.0 from it. BCMA must be installed via an account that has Administrative privileges.</p>
<p>For specific Client PC Setup Requirements, see the “VA Standard Desktop Configurations” link below, which provides the current corporate software and hardware configurations per VA Directive 6401.</p>
<p><mark>REDACTED</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="client-distribution-files">Client Distribution Files</h2></th>
<th>This section lists the Client files distributed during the installation of BCMA V. 3.0. Note: the file list has been updated to reflect current file versions releasing with PSB*3.0*157</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="Client_files_distributed_table" class="anchor"></span>Example: Client Files Distributed During BCMA V. 3.0 Installation

| File names   | Description                                       | File Version | Kilobytes |
|--------------|---------------------------------------------------|--------------|-----------|
| BCMA.exe     | Main BCMA application                             | 3.0.157.1    | 9,370     |
| BCMA.chm     | BCMA help file                                    |              | 1,180     |
| OrderCom.dll | CPRS Med Order Button, Dynamic Link Library (DLL) | 2.0.18.3     | 4,614     |
| BCMApar.exe  | GUI BCMA Site Parameters Application              | 3.0.157.1    | 5,340     |
| BCMApar.chm  | Site Parameter help file                          |              | 161       |
| ReadMe.txt   | Supplementary Information                         |              | 8         |

> **NOTE:** The BCMAOrderCom.dll was replaced with the OrderCom.dll file released in PSB\*3.0\*96. With the release of PSB\*3.0\*96 you can remove all instances of the BCMAOrderCom.dll file. Also, ROBOEX32.DLL is no longer needed or distributed.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="standard-installation-procedure-for-gui-bcma-v.-3.0">Standard Installation Procedure for GUI BCMA V. 3.0</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/017.png)</p></th>
<th colspan="2"><p>Use the instructions listed below to install the GUI version of BCMA V. 3.0, on a Client PC.</p>
<h3 id="to-install-gui-bcma-v.-3.0-on-a-client-pc">To install GUI BCMA V. 3.0 on a Client PC</h3>
<ol type="1">
<li><p>Locate the directory where you downloaded the GUI BCMA V. 3.0 file PSB_3_0P157 via FTP, and then double click on the file to launch the InstallShield Wizard.</p></li>
<li><p>Click <strong><span class="smallcaps">yes</span></strong> at the message, "Would you like to install BCMA?”</p></li>
<li><p>At the InstallShield Wizard Welcome screen, click <strong><span class="smallcaps">next</span></strong>.</p></li>
<li><p>Read the contents of the BCMA Installation screen, and then click <strong><span class="smallcaps">next</span></strong>.</p></li>
<li><p>Click <strong><span class="smallcaps">next</span></strong> at the Choose Destination Location screen.</p></li>
</ol>
<ol type="a">
<li><p>Click <strong><span class="smallcaps">browse</span></strong> if you want to locate another folder to replace the default destination folder. Once located and selected, click <strong><span class="smallcaps">next</span></strong> to proceed with the installation process.</p></li>
</ol>
<ol start="6" type="1">
<li><p>At the Setup Type screen, select one of the following choices, and then click <strong><span class="smallcaps">next</span></strong> to continue with the installation process. “Typical” is the default installation.</p></li>
</ol>
<ul>
<li><blockquote>
<p><strong>Typical</strong> – Installs only the BCMA Client program, which is necessary for using BCMA V. 3.0 to perform the medication administration process.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Full</strong> – Installs the BCMA Client program, and the GUI BCMA Site Parameters application.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Custom</strong> – Lets you select which programs (i.e., BCMA Client program or GUI BCMA Site Parameters application) that you want to install.</p>
</blockquote></li>
</ul>
<ol start="7" type="1">
<li><p>At the InstallShield Wizard Complete screen, click <span class="smallcaps">finish</span> to complete the BCMA installation process. BCMA V. 3.0 is now installed on to the PC.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><h2 id="working-with-the-hosts-file-on-the-client-pc">Working with the Hosts File on the Client PC</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/018.png)</p></td>
<td><p>Make sure that every Client PC has a link established between the Client PC and the <strong>V</strong><em>IST</em><strong>A</strong> Server via the Hosts file on the PC — <em>before</em> running GUI BCMA V. 3.0 from a Client PC. Then you can set up the Optional Command Line Parameters using the table provided in the next section.</p>
<p>Where your Hosts file (no extension) is located, depends on your system. For example:</p>
<ul>
<li><p><strong>Microsoft Windows 11</strong> – C:\Windows\System32\drivers\etc.</p></li>
</ul>
<ul>
<li><p>If No Hosts File Exists</p></li>
</ul>
<p>If the Hosts file does not exist, create one. (Your system may already contain a sample file called “hosts.sam.”) If you create the file using Notepad, it will automatically save the file with a .txt extension. You can use Microsoft Windows File Explorer to rename the file without an extension.</p>
<ul>
<li><p>If the Hosts File Exists</p></li>
</ul>
<p>If the Hosts file already exists, do not delete anything. Just add the new information (i.e., the address and the name) at the end of the file. See the examples provided below.</p>
<ul>
<li><p><strong>If a user only needs access to one BCMA Server and the ServerPort is 9200,</strong> add one line to the Hosts file. Use the IP address provided by your Server Administrator. See the example provided below.</p></li>
</ul>
<blockquote>
<p>152.111.222.333 BrokerServer</p>
</blockquote>
<ul>
<li><p><strong>If the user only needs to access one BCMA Server <em>and</em> the ServerPort is <em>not</em> 9200,</strong> add one line to the Hosts file as shown in the example provided above. Then use the table in the next section to set up the Optional Command Line Parameters.</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Working with the Hosts File on the Client PC (cont.)</th>
<th><ul>
<li><p><strong>If the user needs to access multiple BCMA Servers and/or the ServerPort is <em>not</em> 9200,</strong> add the BCMA Server names to the Hosts file. (The names can be anything you like.) See the examples listed below. Then use the table in the next section to set up the Optional Command Line Parameters.</p></li>
</ul>
<blockquote>
<p>152.111.222.333 BrokerServer1</p>
<p>152.222.333.444 BrokerServer2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="setting-up-optional-command-line-parameters">Setting up Optional Command Line Parameters</h2></th>
<th><p>Use the table provided below to set up the Optional Command Line Parameters. The order that you set up each Parameter is up to your site. However, each Parameter must be continuous, without any spaces.</p>
<p><strong>Note:</strong> If Parameters “S” and “P” are set, they must both be present, or the Client PC will ignore them</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Set up for Optional Command Line Parameters

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Parameter</td>
<td>Example<br />
(default)</td>
<td>Description</td>
</tr>
<tr class="even">
<td>S=</td>
<td>S=BrokerServer</td>
<td>The name of the BCMA Broker Server, as defined in the Hosts file. The default is “BrokerServer.”</td>
</tr>
<tr class="odd">
<td>P=</td>
<td>P=9200</td>
<td>The server port used by the BCMA Broker Server. The default is “9200.”</td>
</tr>
<tr class="even">
<td>L=</td>
<td>L=C:\Temp</td>
<td>The DOS path location for the BCMA Error Log file. Any DOS path will work. The default is “C:\Temp.”</td>
</tr>
<tr class="odd">
<td>T=</td>
<td>T=300</td>
<td><p>RPC Broker TimeOut in seconds. This is the amount of time that BCMA V. 3.0 will wait for a response from an RPC on V<em>IST</em>A. If it is not defined, the default value is five minutes. The minimum value is 30 seconds; anything less is ignored. If the V<em>IST</em>A System's CPU utilization is near 100 percent, and frequent timeouts occur in the<br />
GUI version of BCMA V. 3.0, you can increase this value.</p>
<p>NOTE: The higher the value, the longer BCMA V. 3.0 will appear to hang until the RPC Broker call is complete.</p></td>
</tr>
<tr class="even">
<td>/NOLOGFILE</td>
<td></td>
<td>This parameter disables the Error Log.</td>
</tr>
<tr class="odd">
<td>/DEBUG</td>
<td></td>
<td>This parameter turns on (displays) the BCMA Debug screens.</td>
</tr>
<tr class="even">
<td>-S –A –S</td>
<td></td>
<td><p>Silent install. These command line parameters only work on the distribution file. For example: PSB2_0P24.exe -s -a –s</p>
<p>The silent install will only install the GUI BCMA application, and will not install the GUI BCMA Site Parameters application. At this time, a silent un-install does not exist.</p></td>
</tr>
<tr class="odd">
<td>SHOWCERTS</td>
<td></td>
<td>This will prompt the application to display a certificate selection screen.</td>
</tr>
<tr class="even">
<td>/K</td>
<td>/K=500</td>
<td>This overrides the default timer value in the BCMA desktop shortcut as follows: you can add /K= and a time value in milliseconds, for example: /K=500.</td>
</tr>
<tr class="odd">
<td>/IHS</td>
<td></td>
<td>Turns on SetIHS which forces BCMA to use IHS mode as though running in an RPMS system.</td>
</tr>
</tbody>
</table>

# Working with the Monthly SAGG Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="setting-up-the-monthly-batch-job">Setting up the Monthly Batch Job</h2>
<p>![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/019.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/020.png)![](bcma-version-3-installation-guide-updated-psb-3-157-february-2026/021.png)</p></th>
<th><p>Use the steps listed below to set up your system to run the Monthly Statistical Analysis of Global Growth (SAGG) Report.</p>
<p><strong>Note:</strong> You do not need to perform the steps listed below if you have already set up the Monthly SAGG Report.</p>
<p>To set up the monthly batch job</p>
<p>At the Programmer’s prompt, type <strong>D ^XUP</strong>, and then press <strong><span class="smallcaps">enter</span></strong> to access the menu option for setting up your Monthly SAGG Report.</p>
<p>At the “Select OPTION NAME:” prompt, type <strong>EVE</strong>, and then press <strong><span class="smallcaps">enter</span></strong>.</p>
<p>From the list of choices, select Systems Manager Menu, and then press <strong><span class="smallcaps">enter</span></strong>.</p>
<p>At the “Select Systems Manager Menu Option:” prompt, type <strong>TASK</strong>man Management, and then press <strong><span class="smallcaps">enter</span>.</strong></p>
<p>At the “Select Taskman Management Option:” prompt, type <strong>SCHED</strong>ule/Unschedule Options, and then press <strong><span class="smallcaps">enter</span></strong>.</p>
<p>At the “Select OPTION schedule or reschedule:” prompt, type <strong>PSB SAGG MONTHLY REPORT</strong>, and then press <strong><span class="smallcaps">enter</span></strong>.</p>
<p>At the “Are you adding ‘PSB SAGG MONTHLY REPORT’ as a new OPTION SCHEDULING (the ###)? No//” prompt, type <strong>Yes</strong>, and then press <strong><span class="smallcaps">enter</span></strong>. The Edit Option Schedule screen displays.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Setting up the Monthly Batch Job (cont.)</th>
<th><p>At the “QUEUED TO RUN AT WHAT TIME:” prompt, type a <strong>date and time</strong> <strong>when you want the report to run</strong>, in a VA FileMan format. Then press <strong><span class="smallcaps">enter</span></strong> to move to the next prompt.</p>
<p>At the “DEVICE FOR QUEUED JOB OUTPUT:” prompt, press <strong><span class="smallcaps">enter</span></strong> (leave this prompt blank).</p>
<p>At the “QUEUED TO RUN ON VOLUME SET:” prompt, type <strong>the volume set (CPU)</strong> to use for running the monthly batch job. Then press <strong><span class="smallcaps">enter</span></strong> to move to the next prompt.</p>
<p>At the “RESCHEDULING FREQUENCY:” prompt, type <strong>1M</strong> to run the report on a monthly basis. Then press <strong><span class="smallcaps">enter</span></strong> to move to the next prompt.</p>
<p>At the “TASK PARAMETERS:” prompt, press <strong><span class="smallcaps">enter</span></strong> (leave this prompt blank).</p>
<p>At the “SPECIAL QUEUEING:” prompt, press <strong><span class="smallcaps">enter</span></strong> (leave this prompt blank).</p>
<p>At the “COMMAND:” prompt, type <strong>S</strong> to save the settings, and then press <strong><span class="smallcaps">enter</span></strong>. Your report will print on the same day and time each month (until you specify otherwise).</p>
<p>At the “COMMAND:” prompt, type <strong>E</strong> to exit the Edit Option Schedule screen.</p>
<p>The following example illustrates the set up process for running the SAGG Monthly Report at your site.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Set up for SAGG Monthly Report

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: EVE

1 EVE Systems Manager Menu

2 EVENT CAPTURE DATA ENTRY ECENTER Event Capture Data Entry

3 EVENT CAPTURE MANAGEMENT MENU ECMGR Event Capture Management Menu

4 EVENT CAPTURE MENU ECMENU Event Capture Menu

5 EVENT CAPTURE ONLINE DOCUMENTA ECDSONL Event Capture Online Documentation

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 EVE Systems Manager Menu

Select Systems Manager Menu Option: TASKman Management

Select Taskman Management Option: SCHEDule/Unschedule Options

Select OPTION to schedule or reschedule: PSB SAGG MONTHLY REPORT Monthly SAGG Report

...OK? Yes// \<Enter\>

| Setting up the Monthly Batch Job (cont.) | The example provided below illustrates the prompts (fields) to complete on the Edit Option Schedule screen for running the PSB SAGG Monthly Report at your site. |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Set up for SAGG Monthly Report (cont.)

Edit Option Schedule

Option Name: PSB SAGG MONTHLY REPORT

Menu Text: Monthly SAGG Report TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: \<Date, time to run the report\>

DEVICE FOR QUEUED JOB OUTPUT: \<Enter\>

QUEUED TO RUN ON VOLUME SET: \<Volume set (CPU)\>

RESCHEDULING FREQUENCY: 1M

TASK PARAMETERS: \<Enter\>

SPECIAL QUEUEING: \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: S Press \<PF1\>H for help Insert

COMMAND: E Press \<PF1\>H for help Insert

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="learning-bcma-v.-3.0-lingo">Learning BCMA V. 3.0 Lingo</h2></th>
<th>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td>Definition</td>
</tr>
<tr class="even">
<td>Broker Server</td>
<td>The M portion of the RPC Broker within the VA’s Veterans Health Information Systems and Technology Architecture (<strong>V</strong><em>IST</em><strong>A</strong>) environment.</td>
</tr>
<tr class="odd">
<td>CHUI</td>
<td><strong>Ch</strong>aracter-based <strong>U</strong>ser <strong>I</strong>nterface.</td>
</tr>
<tr class="even">
<td>Client</td>
<td>An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td><strong>C</strong>omputerized <strong>P</strong>atient <strong>R</strong>ecord <strong>S</strong>ystem. A <strong>V</strong><em>IST</em><strong>A</strong> software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.</td>
</tr>
<tr class="even">
<td>Data Dictionary</td>
<td>Also called “DD,” the dictionary that contains file attributes.</td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td>The <strong>V</strong><em>IST</em><strong>A</strong> database management system.</td>
</tr>
<tr class="even">
<td>FTEE</td>
<td><strong>F</strong>ull <strong>T</strong>ime <strong>E</strong>quivalent <strong>E</strong>mployee.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser <strong>I</strong>nterface. The type of interface chosen for BCMA V. 3.0.</td>
</tr>
<tr class="even">
<td>IV</td>
<td>A medication given intraveneously (within a vein) to a patient from an<br />
IV bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</td>
</tr>
<tr class="odd">
<td>Journaling</td>
<td>A record of changes made in files and messages transmitted. It is quite useful when recovering previous versions of a file before updates were made, or to reconstruct updates if an updated file gets damaged.</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td><strong>K</strong>ernel <strong>I</strong>nstallation &amp; <strong>D</strong>istribution <strong>S</strong>ystem.</td>
</tr>
<tr class="odd">
<td>MSM</td>
<td><strong>M</strong>icronectics <strong>S</strong>tandard <strong>M</strong>UMPS.</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><strong>M</strong>assachusetts General Hospital <strong>U</strong>tility <strong>M</strong>ulti-<strong>P</strong>rogramming <strong>S</strong>ystem.</td>
</tr>
<tr class="odd">
<td>PRN Order</td>
<td>The Latin abbreviation for <strong>P</strong>ro <strong>R</strong>e <strong>N</strong>ata. A medication dosage given to a patient on an “as needed” basis.</td>
</tr>
<tr class="even">
<td>PSB CPRS MED BUTTON</td>
<td>The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and NOW (One-Time) medication orders using the CPRS Med Order Button on the BCMA VDL.</td>
</tr>
<tr class="odd">
<td>PSB INSTRUCTOR</td>
<td>The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.</td>
</tr>
</tbody>
</table>
| Learning BCMA V. 3.0 Lingo | The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide. |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td colspan="2">Definition</td>
</tr>
<tr class="even">
<td>PSB MANAGER</td>
<td>The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.</td>
<td></td>
</tr>
<tr class="odd">
<td>PSB STUDENT</td>
<td>The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options within BCMA V. 3.0. This key also requires that a nursing instructor sign on to BCMA.</td>
<td></td>
</tr>
<tr class="even">
<td>RPC</td>
<td colspan="2"><strong>R</strong>emote <strong>P</strong>rocedure <strong>C</strong>all. A procedure stored on the <strong>V</strong><em>IST</em><strong>A</strong> Server, which is executed to return data to the Client.</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td colspan="2">A Client/Server System within the VA’s Veterans Health Information Systems and Technology Architecture (<strong>V</strong><em>IST</em><strong>A</strong>) environment. It enables client applications to communicate and exchange data with M Servers.</td>
</tr>
<tr class="even">
<td>Security Keys</td>
<td colspan="2">Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="odd">
<td>Server</td>
<td colspan="2">An architecture in which one computer can get information from another. The Server, which can be anything from a personal computer to a mainframe, supplies the requested data or services to the Client.</td>
</tr>
<tr class="even">
<td>VDL</td>
<td colspan="2"><p><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</p>
<p><strong>Note:</strong> This is called BCMA VDL in this guide to eliminate confusion with the <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL) also mentioned in this guide.</p></td>
</tr>
<tr class="odd">
<td>V<em>IST</em>A</td>
<td colspan="2"><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</td>
</tr>
<tr class="even">
<td>ZPL</td>
<td colspan="2"><strong>Z</strong>ebra <strong>P</strong>rogramming <strong>L</strong>anguage.</td>
</tr>
</tbody>
</table>

# APPENDIX A: Sample KIDS Load & Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option: INSTALLation

Select Installation Option: ?

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: PSB_3_0.KID

KIDS Distribution saved on Jan 22, 2004@06:00:58

Comment: BAR CODE MED ADMIN V3

This Distribution contains Transport Globals for the following Package(s):

PSB 3.0

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

PSB 3.0

Use INSTALL NAME: PSB 3.0 to install this Distribution.

Select Installation Option: ?

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSB 3.0 Loaded from Distribution 1/22/04@06:44:48

=\> BAR CODE MED ADMIN V3 ;Created on Jan 22, 2004@06:00:58

This Distribution was loaded on Jan 22, 2004@06:44:48 with header of

BAR CODE MED ADMIN V3 ;Created on Jan 22, 2004@06:00:58

It consisted of the following Install(s):

PSB 3.0

Checking Install for Package PSB 3.0

Install Questions for PSB 3.0

Incoming Files:

53.66 BCMA IV PARAMETERS

> **NOTE:** You already have the 'BCMA IV PARAMETERS' File.

53.68 BCMA MISSING DOSE REQUEST

> **NOTE:** You already have the 'BCMA MISSING DOSE REQUEST' File.

53.69 BCMA REPORT REQUEST

> **NOTE:** You already have the 'BCMA REPORT REQUEST' File.

53.78 BCMA MEDICATION VARIANCE LOG

> **NOTE:** You already have the 'BCMA MEDICATION VARIANCE LOG' File.

53.79 BCMA MEDICATION LOG

> **NOTE:** You already have the 'BCMA MEDICATION LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// GENERIC INCOMING TELNET

Install Started for PSB 3.0 :

Jan 22, 2004@06:45:58

Build Distribution Date: Jan 22, 2004

Installing Routines:

Jan 22, 2004@06:45:59

Installing Data Dictionaries:

Jan 22, 2004@06:46

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing FORM

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing LIST TEMPLATE

Installing OPTION

Installing PARAMETER DEFINITION

Installing PARAMETER TEMPLATE

Jan 22, 2004@06:46:05

Updating Routine file...

Updating KIDS files...

PSB 3.0 Installed.

Jan 22, 2004@06:46:06

Install Message sent \#160672

----------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: BCMA Version 3 Installation Guide (updated PSB*3*140 October 2023)

## ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/001.png)Benefits of BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the National Online Information System (NOIS)tickets that are corrected in Bar Code Medication Administration (BCMA) V. 3.0, and provided in the Build description.

1.  Problem: NOIS ISB-0603-31561  
    A medication order that has administration times set for today, but before the Start Time of the order, displays on the Bar Code Medication Administration (BCMA) Due List Report  
      
    Corrective Action:  
    The Due List Report will not display medication orders until the Start Date/Time of the medication order takes affect.
2.  Problem: NOIS ISB-0903-31964  
    When the user selects a time frame for the Medication Administration History (MAH) Report and no administrations are due, the report lists the medication order number from Inpatient Medications V. 5.0 under the “Initial – Name Legend” section.  
      
    Corrective Action:  
    The MAH Report will not display the order number from Inpatient Medications V. 5.0 under the “Initial – Name Legend” section when no administrations are due for a specific time frame.
3.  Problem: NOIS LAH-1203-61493  
    The user receives the following error message, “BCMA failed to communicate with VISTA,” if the Graphical User Interface (GUI) BCMA times out and is unable to connect to the server.  
      
    Corrective Action:  
    The processing time for the GUI BCMA software to display the patient’s record on the BCMA Virtual Due List (VDL) has been reduced.
4.  Problem: NOIS LIT-0603-71923  
    Users sometimes receive an “allocation failure” error message when accessing a patient’s record using the GUI BCMA.  
      
    Corrective Action:  
    The “allocation failure” error message has been corrected.

## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Problem: NOIS MAD-1203-42204  
    The MAH Report takes an extended amount of time to run if the Start Date and the Stop Date of the report, requested by the user, are for different years. For example, if the Start Date is 12/28/03 and the Stop Date is 01/03/04.  
      
    Corrective Action:  
    The user can now request different years for the MAH Report without experiencing extended delays as BCMA accesses the data.
6.  Problem: NOIS MIN-1203-41637  
    Users sometimes experience an “Invalid Medication Lookup” error message after scanning a medication in the “Scan Medication Bar Code:” field of the “Order Manager” dialog box when using the BCMA Med Order Button in GUI BCMA.  
      
    Corrective Action:  
    The BCMA medication lookup process has been corrected to properly validate the medications scanned in the “Scan Medication Bar Code:” field of the “Order Manager” dialog box in GUI BCMA.
7.  Problem: NOIS UNY-0104-10174  
    Multiple IV medication orders display as merged on the IV Medication Tab after an order is discontinued, but the IV bag is still infusing.  
      
    Corrective Action:  
    Multiple IV medication orders will display properly on the IV Medication Tab.
8.  Problem: NOIS TNV-0104-30647  
    Users sometimes experience the following error message, “ERROR: 16^Server Protocol Disabled,” when using the Edit Medication Log \[PSB MED LOG EDIT\] option. This occurs when the PSB BCMA RASO17 SRV Health Level Seven (HL7) server protocol is being disabled.  
      
    Corrective Action:  
    The error message is only intended to notify the BCMA software that the protocol is being disabled. BCMA will now validate the message and not display it to users.

## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

9.  Problem: NOIS ISB-0104-31384  
    When an IV medication order with an infusing bag is “Renewed,” the renewed order continues to display on the IV Medication Tab of the BCMA VDL until the infusing bag is “Completed,” even if the “Renewed” order’s Start Date/Time has expired.

> Corrective Action:  
> When an IV medication order with an infusing bag is “Renewed,” the renewed order will continue to display on the IV Medication Tab of the BCMA VDL until the infusing bag is “Completed,” or until the Start Date/Time of the new order that was created during the renewal process. Once the new order is active, the infusing bag from the previous order will display on the BCMA VDL with the new order, along with any additional bags created from the new order. Any available bags from the previous order will display on the new order based on the IV Site Parameter settings in the GUI BCMA Site Parameters application.

## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/002.png)

This section provides an overview of the major changes in the Bar Code Medication Administration (BCMA) V. 3.0 software such as the new routines and files, Phase Release changes, and maintenance fixes. This version also includes enhancements, which are a direct result of feedback from the BCMA Workgroup and our many end users, and included in Phase Releases I-IV.

### Patient Transfer Notification Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Transfer Notification Information message displays when you open a patient’s record, or view the Unit Dose or the IVP/IVPB Medication Tab for the first time. It indicates that the patient has had a movement type (usually a transfer) within the Patient Transfer Notification Timeframe site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe.

You can define this site parameter, by division, with a minimum value of 2 and a maximum value of 99. The default is 72 hours.

> **NOTE:** The display of the message is dependent on the last action displayed in the “Last Action” column of the BCMA VDL. BCMA then evaluates the last action performed on a medication each time the Unit Dose or the IVP/IVPB Medication Tabs are refreshed.

### Documenting Fractional Dose Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/003.png)You can document Fractional Dose medication orders on the Unit Dose and the IVP/IVPB Medication Tabs. This functionality alerts you when dispensed drug dosages need to be administered to a patient in “fractional” doses so you can provide comments about this order type once administered. The Fractional Dose dialog box displays when the units per dose is fractional and *less than* 1.0. The Multiple/ Fractional Dose dialog box displays when the units per dose is *greater than* 1.0.

> **NOTE:** If you do not scan once for each unit listed in the Multiple/Fractional Dose dialog box, the Confirmation dialog box displays requesting that you confirm the actual total units administered.

### BCMA Clinical Reminders Marquee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Located in the lower, right-hand corner of the BCMA VDL, this “marquee” identifies Pro Re Nata (PRN) medication orders needing effectiveness documentation. The setting is based on the PRN Documentation site-definable parameter, and applies to current admissions or to the site parameter timeframe (whichever is greater). Values can be set from 1-999, with 72 hours the default setting. A “mouse-over” list, in the PRN Effectiveness Activity area, provides the four most recent PRN orders that need comments.

## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PRN Documentation Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRN Documentation site parameter lets you define the minimum number of hours from NOW that BCMA will search for PRN medication orders needing effectiveness comments. The four most recent PRN orders that need documentation display within the PRN Effectiveness mouse-over list in the “BCMA Clinical Reminders” marquee, located in the lower, right-hand corner of the BCMA VDL.

The allowable entry for this parameter, definable by division, is a minimum value of 1 and a maximum value of 999. The default is 72 hours.

### Include Schedule Types Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can automatically display PRN medication orders when the BCMA VDL is first opened by selecting the PRN check box in the “Include Schedule Types” area of the GUI BCMA Site Parameters application. This parameter controls the default display of PRN medications on the BCMA Character-based User Interface (CHUI) Due List and the BCMA VDL — even if you change the Schedule Types or Medication Tab during a medication pass.

Your medical center can choose to have the PRN Schedule Types display on the BCMA VDL by default, or to display PRN medications once a clinician selects the PRN Schedule Type check box on the BCMA VDL. All other Schedule Types will display by default and cannot be changed.

### Accessing PRN Effectiveness Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can quickly access the PRN Effectiveness Log dialog box by selecting a medication on the BCMA VDL, and then selecting the PRN Effectiveness command from the Right Click drop-down menu.

The PRN Effectiveness Log displays the patient’s medication information at the top of the box, under the Selected Administration area, and all PRN medication administrations in the PRN List table. Once a medication is selected, the “Selected Administration” area of the dialog box populates with administration information. The Med History button on the dialog box displays the Medication History Report for the orderable item listed in the ”Selected Administration” area of the dialog box.

## # ## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/004.png) Schedule Type Indicator Alert Lights

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Schedule Type area of the BCMA VDL, a GREEN “alert light” indicates that a medication order exists for the Schedule Type selected within the respective start/stop date and time selected on the BCMA VDL. If grayed out, then none exist.

### Medication Log Dialog Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Log dialog box includes the Vitals area, which displays the four previous vitals entries for each of the Vital signs listed in the area. The “+” (plus) sign, to the left of a Vital sign, expands the row to reveal additional entries. The “–” (minus) sign collapses the row to hide all, but the most recent entry.

### PRN Effectiveness Dialog Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRN Effectiveness dialog box includes the Vitals area, which displays the four previous vitals entries for each of the Vital signs listed in the area. The “+” (plus) sign, to the left of a Vital sign, expands the row to reveal additional entries. The “–” (minus) sign collapses the row to hide all, but the most recent entry.

### Scan IV Dialog Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Bag Information” title/area at the top of the Scan IV dialog box has been replaced with “IV Bag \#.” BCMA populates this area with pertinent information about the IV bag selected on the BCMA VDL. The “Other Print Info” title has been replaced with “Order Changes,” which now displays changes to an IV order, which have an Infusing or Stopped IV bag.

### Bag Information Column on VDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new column on the BCMA VDL identifies an IV order that currently has an IV bag with a status of Infusing or Stopped. It also identifies orders that have changed since the Infusing or Stopped IV bag was first infused.

## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Report Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here’s the changes to the report printing functionality in BCMA V. 3.0:

- Medication Administration History (MAH) Report: The Date column lists three asterisks (\*\*\*) to indicate that a medication is not due. This information is also noted in the Legend at the bottom of the MAH Report.

The report also includes information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.

- Medication Variance Report: Provides “exceptions” (variances) to the medication administration process. It also lists “event” information within a selected date range, such as the type and number of events, and the total percentage of events that occurred. A variance preceded by a minus sign (such as –24) indicates the number of minutes that a medication was given before the administration time.
- Cumulative Vitals/Measurement Report: Lists a patient’s vitals from the Vitals package, along with their demographics and hospital location information. You cannot print this report by ward.
- Ward-Specific Reports: Simply click CANCEL at the Patient Lookup dialog box to access the Menu Bar — without opening a patient record — and print ward-specific reports only, except for the Cumulative Vitals/Measurement Report. A patient’s file must be opened to access patient-specific reports.
- Missed Medications Report: Indicates when a medication order is placed “On Hold” and taken “Off Hold” in CPRS or Inpatient Medications V. 5.0. The Hold information is provided below the medication information on the report, and only applies to administrations due within the Hold timeframe.

The “Order Num” column on the report lists the actual order number and order type (i.e., Unit Dose or IV). This information is quite helpful when troubleshooting problems with BCMA.

- CHUI Missing Dose Report: Changed the line item “Dosage Schedule” on the BCMA CHUI Missing Dose Report to “Schedule” to coincide with the Missing Dose E-mail Notification change described on the next page.

### HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 supports “Health Level Seven (HL7),” a standard package (V*IST*A Messaging) used with M-based applications for conducting HL7 transactions. This package provides the facilities to create, transmit, and receive HL7 messages over a variety of transport layers. BCMA only exports HL7 messages.

### Missing Dose E-Mail Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The e-mail notification that is sent from BCMA to the Pharmacy, when you submit a Missing Dose Request, now includes “Schedule” information.

### Documenting PRN Pain Scores

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With BCMA V. 3.0, you can perform the following tasks with regards to documenting PRN pain scores:

- Define Items: In the “Reason Medication Given PRN” default Answer Lists of the GUI BCMA Site Parameters application you can identify those items that will require the documentation of a pain score within BCMA. The pain score will be documented and stored in the Vitals package.
- Select a Pain Score: When documenting an administration for a PRN medication, you can select a pain score from a pre-defined list.
- Access a Pain Score: When documenting the effectiveness for a PRN medication, you can access pain score information for the patient.

## # ## Benefits of BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Administering a Multiple Dose Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you do not scan once for each Unit Dose or IVP medication listed in the Multiple Dose dialog box, BCMA displays the Confirmation dialog box informing you to scan additional units. The Multiple Dose dialog box retains the data that you entered before receiving the message.

### Administering a PRN Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Medication Log dialog box, you can select the patient’s pain score, between 0 and 10 or 99, with “0” being No Pain, “10” the Worst Imaginable, and “99” for “Unable to Respond.”

### Recording the Effectiveness of a PRN Medication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the PRN Effectiveness Log dialog box, you can select the patient’s pain score, between 0 and 10 or 99, with “0” being No Pain, “10” the Worst Imaginable, and “99” for “Unable to Respond.”

### Creating Default Answers Lists 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the GUI BCMA Site Parameters application, the Attribute column is available only when you choose the Default Answer Lists Tab and select the “Reason Medication Given PRN” list. This column identifies that a Pain Score is required from the patient when a clinician administers a specific medication.

When you select the “Requires Pain Score” check box when adding or renaming a “Reason Medication Given PRN” item, you must choose a pain score in the BCMA Medication Log and PRN Effectiveness dialog boxes when administering a medication.

## Benefits of This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Other Sources of Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/005.png)

Preparing your site for the installation and implementation of  
BCMA V. 3.0 helps to ensure a smooth integration. This Installation Guide is designed to help you do just that. It includes detailed information such as system requirements; installation time estimates and instructions; and procedures that will get you up and running quickly with BCMA V. 3.0.

### Our Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package.

- Development Engineering
- Information Resources Management (IRM)
- Clinical Application Coordinator (CAC) – called Applications Package Coordinator (ADPAC) at some sites
- Enterprise V*IST*A Support (EVS)
- Software Quality Assurance (SQA)

Refer to the Web sites listed below when you want to receive more background and technical information about BCMA V. 3.0, and to download this manual and related documentation.

### Background/Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From your Intranet, enter <span class="mark">REDACTED</span> in the Address field to access the BCMA Main Web page.

### This Manual and Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From your Intranet, enter <http://www.va.gov/vdl> in the Address field to access this manual, and those listed below, from the V*IST*A Documentation Library (VDL).

- Technical Manual/Security Guide
- GUI User Manual
- Nursing CHUI User Manual
- Pharmacy CHUI User Manual
- Manager’s User Manual

## ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/011.png)Conventions Used in This Guide (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Tips: Located in the left margin, these helpful hints are designed to help you work more efficiently with  
  BCMA V. 3.0.
- Menu Options: When provided in *italics*, identifies a menu option. When provided in boldface, ALL CAPS, identifies the letters that you should type onto your computer screen, before pressing <span class="smallcaps">enter.</span> The system then goes directly to the menu option. (Note: The letters do not have to be entered as capital letters, even though they are provided within the steps in this format.) See the examples provided below.
- Italicized: Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list containing the first line of every PSB routine.
- Capitalized: At the “Taskman Management Option:” prompt, type SCHEDule/Unschedule Options, and then press <span class="smallcaps">enter</span>.

## ## Obtaining On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Locating Detailed Listings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On-line help is designed right into the Graphical User Interface (GUI) and Character-based User Interface (CHUI) versions of BCMA V. 3.0, making it quick and easy for you to get answers to your questions. Here’s how to access help in both versions of BCMA V. 3.0:

- GUI BCMA: Provides context-sensitive, on-line help and the Help menu.
- Context-Sensitive Help: Place your “focus” on a feature, button, or Tab on the BCMA VDL, using the <span class="smallcaps">tab</span> key, and then press <span class="smallcaps">f1</span> to receive help specific to that area of the BCMA VDL. In the case of a command, first highlight it in the Menu Bar or Right Click drop-down menu, and then press <span class="smallcaps">f1.</span>
- Help Menu: Open the Help menu, and then choose the Contents and Index command to receive help for every feature in GUI BCMA V. 3.0.
- CHUI BCMA: Lets you enter up to two question marks at any prompt to receive on-line help.
- One Question Mark: Provides a brief statement related to the prompt.
- Two Question Marks: Displays more detailed information about the prompt, plus any hidden  
  actions.

You can obtain and print listings about BCMA V. 3.0 routines, and Data Dictionaries using the information provided below.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Kernel routine XINDEX to produce detailed listings of routines. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list containing the first line of every PSB routine.

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the VA FileMan *List File Attributes* \[DILIST\] option, under the *Data Dictionary Utilities* \[DI DDU\] option, to print the Dictionaries.

## Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).

Example: Minimum Required Packages and Versions

|                               |                        |
|-------------------------------|------------------------|
| Package                       | Minimum Version Needed |
| Inpatient Medications         | 5.0                    |
| Kernel                        | 8.0                    |
| MailMan                       | 8.0                    |
| Nursing                       | 4.0                    |
| Order Entry/Results Reporting | 3.0                    |
| Pharmacy Data Management      | 1.0                    |
| RPC Broker (32-bit)           | 1.1                    |
| Toolkit                       | 7.3                    |
| VA FileMan                    | 22.0                   |
| Vitals/Measurements           | 5.0                    |

## ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/012.png)Installation Time Estimates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On average, it takes approximately two minutes to install BCMA  
V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its’ system resources.

Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.

### Response Time Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 does not include Response Time Monitor hooks.

### Laptops and Bar Code Scanners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas, at your site, that use BCMA V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.

### Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.

### Unit Dose Label Printer Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *Label print* \[PSBO BL\] option for printing individual or batch Unit Dose bar code labels. It is specifically coded to the Zebra-brand printers using the Zebra Programming Language (ZPL). Model 105SE was used in the development of the labels. Routine PSBO BL uses site-specific printers or terminals to produce labels.

### IV Label Printer Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section “Interfacing with the Bar Code Label Printer” in the *Inpatient Medications V. 5.0 Technical Manual/Security Guide* for detailed setup information.

## ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/014.png)Files Required to Run BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once all BCMA V. 3.0 files are installed, make sure that every Client PC includes the minimum system *before* users run BCMA V. 3.0 from it. BCMA must be installed via an account that has Administrative privileges.

For specific Client PC Setup Requirements, see the “VA Standard Desktop Configurations” link below, which provides the current corporate software and hardware configurations per VA Directive 6401.

> <span class="mark">REDACTED</span>

BCMA V. 3.0 uses the following files installed on the V*IST*A Server. “Journaling” is recommended.

- ^PSB (53.66, BCMA IV Parameters
- ^PSB (53.68, BCMA Missing Dose Request
- ^PSB (53.69, BCMA Report Request
- ^PSB (53.78, BCMA Medication Variance Log
- ^PSB (53.79, BCMA Medication Log

> Note: You can learn more about these files by generating a list with file attributes using VA FileMan

### Routines Installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the listing below to learn the routines installed on to your site’s V*IST*A Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.

> **NOTE:** You can use the *Kernel First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list containing the first line of each PSB routine.

### Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At this time, we do *not* offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memor

Example: BCMA V. 3.0 Routines Installed on to VISTA Server

PSBALL PSBAPIPM PSBCHIVH PSBCHKIV PSBMD PSBML PSBML1 PSBMLEN

PSBMLEN1 PSBMLHS PSBMLTS PSBMLU PSBMLVAL PSBO PSBO1 PSBOAL

PSBOBL PSBODL PSBODL1 PSBODO PSBOHDR PSBOMD PSBOMH PSBOMH1

PSBOMH2 PSBOML PSBOMM PSBOMV PSBOPE PSBOPI PSBOPM PSBOVT

PSBOWA PSBPAR PSBPARIV PSBPOIV PSBPRN PSBRPC PSBRPC1 PSBRPC2

PSBRPC3 PSBRPCMO PSBRPCXM PSBSAGG PSBSVHL7 PSBUTL PSBVAR PSBVDLIV

PSBVDLPA PSBVDLPB PSBVDLTB PSBVDLU1 PSBVDLU2 PSBVDLU3 PSBVDLUD PSBVDLVL

PSBVITFL PSBVT PSBVT1 PSBXMRG

60 routines

### Routines with Related Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the routines and related checksums for BCMA  
V. 3.0 provided during the installation process.

Example: BCMA V. 3.0 Routines with Related Checksums

Select BUILD NAME: PSB 3.0 BAR CODE MED ADMIN

PSBALL value = 1475151

PSBAPIPM value = 9031085

PSBCHIVH value = 1166996

PSBCHKIV value = 35513271

PSBMD value = 17319681

PSBML value = 23421797

PSBML1 value = 7074072

PSBMLEN value = 18077803

PSBMLEN1 value = 9220985

PSBMLHS value = 2525483

PSBMLTS value = 8100734

PSBMLU value = 1498988

PSBMLVAL value = 9734944

PSBO value = 17926200

PSBO1 value = 2876667

PSBOAL value = 1806300

PSBOBL value = 4045534

PSBODL value = 16589922

PSBODL1 value = 8836828

PSBODO value = 2948451

PSBOHDR value = 5286664

PSBOMD value = 6143174

PSBOMH value = 20105393

PSBOMH1 value = 20721307

PSBOMH2 value = 9443664

PSBOML value = 10399745

PSBOMM value = 21442785

PSBOMV value = 13276146

PSBOPE value = 7022505

PSBOPI value = 288600

PSBOPM value = 4855752

PSBOVT value = 790819

PSBOWA value = 13904863

PSBPAR value = 6032995

PSBPARIV value = 16437954

PSBPOIV value = 24363099

PSBPRN value = 7079605

PSBRPC value = 10743383

PSBRPC1 value = 5473533

PSBRPC2 value = 20110546

PSBRPC3 value = 194738

Example: BCMA V. 3.0 Routines with Related Checksums (cont.)

PSBRPCMO value = 18080428

PSBRPCXM value = 2728593

PSBSAGG value = 1431404

PSBSVHL7 value = 16217830

PSBUTL value = 14185290

PSBVAR value = 4760179

PSBVDLIV value = 17858201

PSBVDLPA value = 4059667

PSBVDLPB value = 19523684

PSBVDLTB value = 3557813

PSBVDLU1 value = 18022165

PSBVDLU2 value = 4610568

PSBVDLU3 value = 3001261

PSBVDLUD value = 18568646

PSBVDLVL value = 23162182

PSBVITFL value = 2483832

PSBVT value = 22976876

PSBVT1 value = 767427

PSBXMRG value = 1576759

### ### V*IST*A Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/015.png)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/016.png)

Perform the steps provided below to download BCMA V. 3.0 from an FTP Server. Then you will be ready to use this section for loading the Kernel Installation & Distribution System (KIDS) Distribution file and the Broker Server file, and for installing BCMA V. 3.0 on to the V*IST*A Server.

Attention: BCMA V. 3.0 includes a new GUI executable file. Installation of this GUI is NOT required immediately after the KIDS install for the software to function. The installation process will make significant changes to routines, files, and files within the BCMA  
V. 3.0 application. Review the bulleted list below, taken from the Build description, for more information.
- Prior clients compatible with BCMA V. 3.0: 2.0.36.14
- Client can be copied instead of installed: Yes

### Task 1: Download BCMA V. 3.0 Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following information to download BCMA V. 3.0 from an FTP Server.

1.  Download the GUI BCMA file PSB3_0.exe, the Host File PSB_3_0.KID from an FTP Server using an address listed in the table below.
- The preferred method is to “FTP” the files from <span class="mark">REDACTED</span>. This location automatically transmits files from the *first* available FTP Server. (See the order listed below under the FTP Address column).
- .EXE or .PDF files need to be FTP in BINARY.
- KIDS Build needs to be FTP in ASCII.

> **NOTE:** If you prefer, you can retrieve the software *directly* from one of the FTP Servers, listed below, under the FTP Address column.

10. Move the files to the appropriate directory on your system.

Example: FTP Addresses Available for Downloading BCMA V. 3.0 Software

| OI Field Office                | FTP Address                    | Directory                      |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

### Task 2: Load the KIDS Distribution File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the steps listed below to load the KIDS Distribution file.

1.  Sign in to the UCI where the KIDS Distribution file will be loaded and BCMA V. 3.0 will be installed.
11. At the “Select OPTION NAME:” prompt, type XPD MAIN, and then press <span class="smallcaps">enter</span>.
12. At the “Select Kernel Installation & Distribution System Option:” prompt, type INSTALLation, and then press <span class="smallcaps">enter.</span>
13. At the “Select Installation Option:” prompt, type Load a Distribution, and then press <span class="smallcaps">enter</span> to prepare for loading the KIDS Distribution file.
14. At the “Enter a Host File:” prompt, type the directory where you have stored the Host File, followed by PSB_3_0.KID. Then press <span class="smallcaps">enter.</span>
15. At the “Want to Continue with Load YES//?” prompt, press <span class="smallcaps">enter</span>. The system then loads the file to this location.

### Task 3: Install BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you are ready to install BCMA V. 3.0 on to the V*IST*A Server. Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.

> Note: You should perform step \#1 listed below *now* if you are planning to install BCMA V. 3.0 immediately. However, if you are installing the application at another time, ask users to log off your system at that time.

1.  From the Facility Tab of the GUI BCMA Site Parameters application, take BCMA users offline.
16. Request that all BCMA users log off BCMA.
17. Review mapped sets for PSB\* namespaces.
- If the routines are mapped, remove them from the mapped set at this time.
18. Backup your system. This step is optional, but recommended.
19. At the “Select INSTALL NAME:” prompt, type PSB 3.0 and then press <span class="smallcaps">enter</span> to install BCMA V. 3.0. This Build provides all of the routines and files necessary for BCMA V. 3.0.

### Task 3: Install BCMA V. 3.0 (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

20. At the “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” prompt, type NO, and then press <span class="smallcaps">enter.</span>
21. At the “Want KIDS to INHIBIT LOGONs during the install? YES//” prompt, type NO, and then press <span class="smallcaps">enter.</span>
22. At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” prompt, type NO, and then press <span class="smallcaps">enter.</span>
23. At the “DEVICE:” prompt, press <span class="smallcaps">enter</span> to use the default device HOME (the screen) for printing the Installation message. If you want to print a hard copy, enter your site printer, and then press <span class="smallcaps">enter.</span>
24. If routines were unmapped as part of the installation process, return them to the mapped set once the installation of  
    BCMA V. 3.0 is completed.
25. From the Facility Tab of the GUI BCMA Site Parameters application, place BCMA V. 3.0 back on-line.

### Additional Preparation for BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you are ready to perform the steps listed below to further prepare your site and staff for using BCMA V. 3.0.

1.  If you are a Micronectics Standard MUMPS (MSM) site, move the PSB routines only, to all nodes.
26. Assign the following security keys to appropriate site personnel.
- PSB MANAGER – designates the holder as a manager
- PSB INSTRUCTOR – designates the holder as a nursing instructor supervising student nurses
- PSB STUDENT – designates the holder as a student nurse, requiring that an instructor also sign on to BCMA V. 3.0  
  at the same time
- PSB CPRS MED BUTTON – designates the holder as a nurse who can document administered verbal- and phone-type STAT and NOW orders using the CPRS Med Order Button on the BCMA V. 3.0 VDL

### ### Client PC Setup Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Client Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once all BCMA V. 3.0 files are installed, make sure that every Client PC includes the minimum system configuration *before* users run BCMA V. 3.0 from it. BCMA must be installed via an account that has Administrative privileges.

For specific Client PC Setup Requirements, see the “VA Standard Desktop Configurations” link below, which provides the current corporate software and hardware configurations per VA Directive 6401.

<span class="mark">REDACTED</span>

This section lists the Client files distributed during the installation of BCMA V. 3.0. Note: the file list has been updated to reflect current file versions releasing with PSB\*3.0\*140.

Example:Client Files Distributed During BCMA V. 3.0 Installation

| File names   | Description                                       | File Version | Kilobytes |
|--------------|---------------------------------------------------|--------------|-----------|
| BCMA.exe     | Main BCMA application                             | 3.0.140.2    | 8,856     |
| BCMA.chm     | BCMA help file                                    |              | 1,180     |
| OrderCom.dll | CPRS Med Order Button, Dynamic Link Library (DLL) | 2.0.18.3     | 4,614     |
| BCMApar.exe  | GUI BCMA Site Parameters Application              | 3.0.140.2    | 5,266     |
| BCMApar.chm  | Site Parameter help file                          |              | 161       |
| ReadMe.txt   | Supplementary Information                         |              | 8         |

> **NOTE:** The BCMAOrderCom.dll was replaced with the OrderCom.dll file released in PSB\*3.0\*96. With the release of PSB\*3.0\*96 you can remove all instances of the BCMAOrderCom.dll file. Also, ROBOEX32.DLL is no longer needed or distributed.

## ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/017.png)Standard Installation Procedure for GUI BCMA V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the instructions listed below to install the GUI version of  
BCMA V. 3.0, on a Client PC.

### To install GUI BCMA V. 3.0 on a Client PC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the directory where you downloaded the GUI BCMA  
    V. 3.0 file PSB_3_0P140 via FTP, and then double click on the file to launch the InstallShield Wizard.
2.  Click <span class="smallcaps">yes</span> at the message, "Would you like to install BCMA?”
3.  At the InstallShield Wizard Welcome screen, click <span class="smallcaps">next</span>.
4.  Read the contents of the BCMA Installation screen, and then click <span class="smallcaps">next</span>.
5.  Click <span class="smallcaps">next</span> at the Choose Destination Location screen.
    1.  Click <span class="smallcaps">browse</span> if you want to locate another folder to replace the default destination folder. Once located and selected, click <span class="smallcaps">next</span> to proceed with the installation process.
6.  At the Setup Type screen, select one of the following choices, and then click <span class="smallcaps">next</span> to continue with the installation process. “Typical” is the default installation.
- Typical – Installs only the BCMA Client program, which is necessary for using BCMA V. 3.0 to perform the medication administration process.
- Full – Installs the BCMA Client program, and the GUI BCMA Site Parameters application.
- Custom – Lets you select which programs (i.e., BCMA Client program or GUI BCMA Site Parameters application) that you want to install.
7.  At the InstallShield Wizard Complete screen, click <span class="smallcaps">finish</span> to complete the BCMA installation process. BCMA V. 3.0 is now installed on to the PC.

## Working with the Hosts File on the Client PC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/018.png)

Make sure that every Client PC has a link established between the Client PC and the V*IST*A Server via the Hosts file on the PC — *before* running GUI BCMA V. 3.0 from a Client PC. Then you can set up the Optional Command Line Parameters using the table provided in the next section.

Where your Hosts file (no extension) is located, depends on your system. For example:

- Microsoft Windows 10 – C:\Windows\System32\drivers\etc.
- If No Hosts File Exists

If the Hosts file does not exist, create one. (Your system may already contain a sample file called “hosts.sam.”) If you create the file using Notepad, it will automatically save the file with a .txt extension. You can use Microsoft Windows File Explorer to rename the file without an extension.

- If the Hosts File Exists

If the Hosts file already exists, do not delete anything. Just add the new information (i.e., the address and the name) at the end of the file. See the examples provided below.

- ![](bcma-version-3-installation-guide-updated-psb-3-140-october-2023/019.png)If a user only needs access to one BCMA Server and the ServerPort is 9200, add one line to the Hosts file. Use the IP address provided by your Server Administrator. See the example provided below.

> 152.111.222.333 BrokerServer

- If the user only needs to access one BCMA Server *and* the ServerPort is *not* 9200, add one line to the Hosts file as shown in the example provided above. Then use the table in the next section to set up the Optional Command Line Parameters.
- If the user needs to access multiple BCMA Servers and/or the ServerPort is *not* 9200, add the BCMA Server names to the Hosts file. (The names can be anything you like.) See the examples listed below. Then use the table in the next section to set up the Optional Command Line Parameters.

> 152.111.222.333 BrokerServer1

> 152.222.333.444 BrokerServer2

## Setting up the Monthly Batch Job (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example illustrates the set up process for running the SAGG Monthly Report at your site.

Example: Set up for SAGG Monthly Report

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: EVE

1 EVE Systems Manager Menu

2 EVENT CAPTURE DATA ENTRY ECENTER Event Capture Data Entry

3 EVENT CAPTURE MANAGEMENT MENU ECMGR Event Capture Management Menu

4 EVENT CAPTURE MENU ECMENU Event Capture Menu

5 EVENT CAPTURE ONLINE DOCUMENTA ECDSONL Event Capture Online Documentation

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 EVE Systems Manager Menu

Select Systems Manager Menu Option: TASKman Management

Select Taskman Management Option: SCHEDule/Unschedule Options

Select OPTION to schedule or reschedule: PSB SAGG MONTHLY REPORT Monthly SAGG Report

...OK? Yes// \<Enter\>

## Setting up the Monthly Batch Job (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example provided below illustrates the prompts (fields) to complete on the Edit Option Schedule screen for running the PSB SAGG Monthly Report at your site.

Example: Set up for SAGG Monthly Report (cont.)

Edit Option Schedule

Option Name: PSB SAGG MONTHLY REPORT

Menu Text: Monthly SAGG Report TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: \<Date, time to run the report\>

DEVICE FOR QUEUED JOB OUTPUT: \<Enter\>

QUEUED TO RUN ON VOLUME SET: \<Volume set (CPU)\>

RESCHEDULING FREQUENCY: 1M

TASK PARAMETERS: \<Enter\>

SPECIAL QUEUEING: \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: S Press \<PF1\>H for help Insert

COMMAND: E Press \<PF1\>H for help Insert

## ## Learning BCMA V. 3.0 Lingo

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td>Definition</td>
</tr>
<tr class="even">
<td>Broker Server</td>
<td>The M portion of the RPC Broker within the VA’s Veterans Health Information Systems and Technology Architecture (<strong>V</strong><em>IST</em><strong>A</strong>) environment.</td>
</tr>
<tr class="odd">
<td>CHUI</td>
<td><strong>Ch</strong>aracter-based <strong>U</strong>ser <strong>I</strong>nterface.</td>
</tr>
<tr class="even">
<td>Client</td>
<td>An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td><strong>C</strong>omputerized <strong>P</strong>atient <strong>R</strong>ecord <strong>S</strong>ystem. A <strong>V</strong><em>IST</em><strong>A</strong> software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.</td>
</tr>
<tr class="even">
<td>Data Dictionary</td>
<td>Also called “DD,” the dictionary that contains file attributes.</td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td>The <strong>V</strong><em>IST</em><strong>A</strong> database management system.</td>
</tr>
<tr class="even">
<td>FTEE</td>
<td><strong>F</strong>ull <strong>T</strong>ime <strong>E</strong>quivalent <strong>E</strong>mployee.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser <strong>I</strong>nterface. The type of interface chosen for BCMA V. 3.0.</td>
</tr>
<tr class="even">
<td>IV</td>
<td>A medication given intraveneously (within a vein) to a patient from an<br />
IV bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</td>
</tr>
<tr class="odd">
<td>Journaling</td>
<td>A record of changes made in files and messages transmitted. It is quite useful when recovering previous versions of a file before updates were made, or to reconstruct updates if an updated file gets damaged.</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td><strong>K</strong>ernel <strong>I</strong>nstallation &amp; <strong>D</strong>istribution <strong>S</strong>ystem.</td>
</tr>
<tr class="odd">
<td>MSM</td>
<td><strong>M</strong>icronectics <strong>S</strong>tandard <strong>M</strong>UMPS.</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><strong>M</strong>assachusetts General Hospital <strong>U</strong>tility <strong>M</strong>ulti-<strong>P</strong>rogramming <strong>S</strong>ystem.</td>
</tr>
<tr class="odd">
<td>PRN Order</td>
<td>The Latin abbreviation for <strong>P</strong>ro <strong>R</strong>e <strong>N</strong>ata. A medication dosage given to a patient on an “as needed” basis.</td>
</tr>
<tr class="even">
<td>PSB CPRS MED BUTTON</td>
<td>The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and NOW (One-Time) medication orders using the CPRS Med Order Button on the BCMA VDL.</td>
</tr>
<tr class="odd">
<td>PSB INSTRUCTOR</td>
<td>The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.</td>
</tr>
</tbody>
</table>

## Learning BCMA V. 3.0 Lingo

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td colspan="2">Definition</td>
</tr>
<tr class="even">
<td>PSB MANAGER</td>
<td>The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.</td>
<td></td>
</tr>
<tr class="odd">
<td>PSB STUDENT</td>
<td>The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options within BCMA V. 3.0. This key also requires that a nursing instructor sign on to BCMA.</td>
<td></td>
</tr>
<tr class="even">
<td>RPC</td>
<td colspan="2"><strong>R</strong>emote <strong>P</strong>rocedure <strong>C</strong>all. A procedure stored on the <strong>V</strong><em>IST</em><strong>A</strong> Server, which is executed to return data to the Client.</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td colspan="2">A Client/Server System within the VA’s Veterans Health Information Systems and Technology Architecture (<strong>V</strong><em>IST</em><strong>A</strong>) environment. It enables client applications to communicate and exchange data with M Servers.</td>
</tr>
<tr class="even">
<td>Security Keys</td>
<td colspan="2">Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="odd">
<td>Server</td>
<td colspan="2">An architecture in which one computer can get information from another. The Server, which can be anything from a personal computer to a mainframe, supplies the requested data or services to the Client.</td>
</tr>
<tr class="even">
<td>VDL</td>
<td colspan="2"><p><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</p>
<p><strong>Note:</strong> This is called BCMA VDL in this guide to eliminate confusion with the <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL) also mentioned in this guide.</p></td>
</tr>
<tr class="odd">
<td>V<em>IST</em>A</td>
<td colspan="2"><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</td>
</tr>
<tr class="even">
<td>ZPL</td>
<td colspan="2"><strong>Z</strong>ebra <strong>P</strong>rogramming <strong>L</strong>anguage.</td>
</tr>
</tbody>
</table>
