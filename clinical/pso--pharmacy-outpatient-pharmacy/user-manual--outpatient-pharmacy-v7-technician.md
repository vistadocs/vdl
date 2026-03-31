---
title: Outpatient Pharmacy Version 7 Technician User Manual (updated PSO*7*630)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Technician  (updated PSO*7*630)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 2
description: In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during t
audience: 
keywords: 
  - order
  - drug
  - patient
  - prescription
  - pharmacy
  - date
  - class
  - take
  - checks
  - table
page_count: 0
word_count: 46723
section_count: 26
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_tech_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_tech_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

Outpatient Pharmacy (PSO)Technician’s User Manual

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/001.png)

December 1997

(Revised July 2021)

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office

Revision History

When updates occur, the Title Page lists the new revised date and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Patch</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2021</td>
<td>PSO*7*630</td>
<td>Added <a href="#chapter-14-meds-by-mail-virtual-pharmacy-services">Chapter 14: Meds by Mail</a> – Virtual Pharmacy Services</td>
</tr>
<tr class="even">
<td>07/2021</td>
<td>PSO*7*524</td>
<td>Added <a href="#hazardous-medication-warnings---order-checks">Hazardous Medication Warning Messages</a> during Patient Prescription Processing: 40-42</td>
</tr>
<tr class="odd">
<td>6/2020</td>
<td>PSO*7*477</td>
<td><p>Added a note about the EXCEPT conjunction: <a href="#p477_36_Except_note"><u>35</u></a>, <a href="#p477_133_Except_no_copy_ref"><u>132</u></a>, <a href="#p477_143_Except_no_copy_ref"><u>142</u></a></p>
<p>Removed references to EXCEPT conjunction: <a href="#p477_116_Remove_Except_ref"><u>115</u></a></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>2/2019</td>
<td>PSO*7*532</td>
<td><p>Updated the popup message for if the query connection to the HDR/CDS Repository fails, in the <a href="#PSO_532_OneVAPharmPatRxProcess">OneVA Pharmacy Processing within Patient Prescription Processing</a> section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/2018</td>
<td>PSO*7*452</td>
<td><p>Added information about <a href="#patient-demographics-and-clinical-alerts">patient demographic information and Clinical Alerts</a> available in the List Manager <a href="#HEADER_LM">header area</a> when using Pharmacy options <a href="#PSO_P">[PSO P]</a> and <a href="#PSO_LM_BACKDOOR">[PSO LM BACKDOOR ORDERS]</a>.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2018</td>
<td>PSO*7*502</td>
<td><p>Updates for ScripTalk enhancement:</p>
<p><a href="#scriptalk-mapping-error-messages">Included ScripTalk Mapping Error Messages</a></p>
<p>508 &amp; OIT Compliance update throughout</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td>PSO*7*402</td>
<td><p>Updated title page to reflect month/year of revision</p>
<p>Updated patient header displays</p>
<p>3, 6, 27, 30, 48, 50, 60-61, 64, 66-67, 69, 73, 76-77, 79, 90, 92, 101, 106-107, 116, 122, 126-127, 131-132,136, 140, 156</p>
<p>Updated Available Dosage List displays</p>
<p>37, 62, 64, 68, 77-78, 81-82, 89, 100-101, 104-105, 110, 114-115, 140</p>
<p>Updated Schedule prompt displays: 37, 62-64, 68, 78, 82, 89, 100, 101-102, 106, 112, 114, 140</p>
<p><a href="#Page_108">Updated information on Available Dosage List display changes</a></p>
<p><a href="#Page_111">Updated text for schedule changes</a></p>
<p>Updated Error Table Information: 33,163</p>
<p><a href="#Page_103">Updated Dosing Order Check section</a></p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>9/2017</td>
<td>PSO*7*422</td>
<td><p>Removed “Do You want to Edit the SIG?”</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2017</td>
<td>PSO*7*479</td>
<td><p>Modifies the prompt to the user when printing a OneVA Pharmacy label.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2016</td>
<td>PSO*7*460</td>
<td><p>Updated copay activity log for Fixed Medication Copayment Tiers <mark>REDACTED</mark></p>
<p>Updated Title Page to current OI&amp;T Standards</p>
<p>Updated Revision History</p>
<p>Updated Table of Contents</p>
<p>Updated footer date to March 2014 per business request.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td>PSO*7*454</td>
<td><p>Updated Title Page Revised Date; Updated Revision History; Updated Table of Contents; Updated Footer Date; Updated Introduction; Updated Medication Profile; Added OneVA Pharmacy to Patient Prescription Processing; Updated Glossary; Updated Index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/2016</td>
<td>PSO*7*448</td>
<td><p>Using the Copy Action section</p>
<p>Updated Holding and Unholding a Prescription section</p>
<p>Updated examples to read “Veteran Prescription”</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/2016</td>
<td>PSO*7*411</td>
<td><p>Updated Revision History</p>
<p>Updated Table of Contents</p>
<p>Added Allergy Order Checks</p>
<p>Added Clinical Reminder Order Checks changes</p>
<p>Updated Screens<br />
Updated description, captures</p>
<p>Updated Glossary</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>01/2016</td>
<td>PSO*7*427</td>
<td><p>Updated cover date to January 2016. Updated screenshots to display the National Drug Code (NDC) in accordance with new functionality associated with PSO*7*427 as</p>
<p>well as additional text added to Chapter 10 “Pull Early From Suspense” (3rd paragraph about the Label Log) and additional new screenshot.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2015</td>
<td>PSO*7*438</td>
<td>Updated help text for patient lookup.</td>
</tr>
<tr class="even">
<td>08/2014</td>
<td>PSO*7*313</td>
<td><p>Updated Outpatient Pharmacy Hidden Actions</p>
<p>Added section on titration</p>
<p>Updated [PSO LM BACKDOOR ORDERS]</p>
<p>Updated Glossary</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td>PSO*7*421</td>
<td><p>Updated all pages throughout the document</p>
<p>Updated contents to reflect added/removed functionality of current patch.</p>
<p>Added Reject Resolution Required information</p>
<p>Added Example for handling Reject Required Rejected</p>
<p>Added if claim submission returns a Reject Resolution Required information</p>
<p>Added Reject Resolution Required reject to index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/2013</td>
<td>PSO*7*372</td>
<td><p>Updated Revision History &amp; Table of Contents</p>
<p>Added to the Related Manuals</p>
<p>Update text</p>
<p>Delete text</p>
<p>Update screens</p>
<p>Add Dosing Order Checks information</p>
<p>Updated Error Message section</p>
<p>Update Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2013</td>
<td>PSO*7*391</td>
<td><p>Updated Table of Contents</p>
<p>New sort selection for CS.</p>
<p>New security key named "PSDRPH" introduced.</p>
<p>Added Hash Counts and DEA Certification section.</p>
<p>Added two System Error messages.</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>01/2013</td>
<td>PSO*7*390</td>
<td><p>Updated Revision History &amp; Table of Contents</p>
<p>Added new option Check Interaction</p>
<p>Added Creatinine Clearance (CrCl) and Body Surface Area (BSA), when available, to the header area of Patient and Medication Profile displays</p>
<p>Added new option Check Drug Interaction</p>
<p>Added information regarding clinic orders</p>
<p>Update Hidden Actions</p>
<p>Added drug allergy changes</p>
<p>Update Glossary</p>
<p>Update Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/2012</td>
<td>PSO*7*386</td>
<td><p>Added section on HOLD and UNHOLD functionality.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/2012</td>
<td><p>PSO*7*385</p>
<p>PSO*7*359</p></td>
<td><p>Added signature alert</p>
<p>Expanded ECME Numbers to twelve digits</p>
<p>Corrected typos</p>
<p>Updated wording on p. 34 from “a message” to “messages”</p>
<p>Updated Service Code values</p>
<p>Added CHAMPVA functionality</p>
<p>Added TRICARE to Glossary</p>
<p>Added CHAMPVA to Glossary</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/2011</td>
<td>PSO*7*251</td>
<td><p>The following changes are included in this patch:</p>
<p>-Updated Revision History</p>
<p>-Updated Table of Contents</p>
<p>-Outpatient List Manager Screen Views</p>
<p>-Added HP and H to Hold Status, and Added DF,DE,DP,DD and DA</p>
<p>-Added Intervention menu hidden action information</p>
<p>-Added DF,DE,DP,DD and DA, and Added HP and H to Hold Status</p>
<p>-Replaced Medication Short Profile</p>
<p>-Added Intervention menu hidden action information</p>
<p>-Inserted enhanced Order checks, Outpatient Pharmacy generated order checks</p>
<p>-Added IN to Screen Scrape</p>
<p>-Modified New Order Screen Scrape</p>
<p>-Updated Entering a New Order, Added Allergy/ADR, Therapeutic Duplication, and CPRS Order Checks</p>
<p>-Duplicate Drug examples</p>
<p>-Duplicate Drug examples</p>
<p>-CPRS Order Checks – How They Work</p>
<p>-Error Messages</p>
<p>-Added API, DATUP, DIF, DoD, ETC, FDB, HDR-Hx, and HDR-IMS to the Glossary, and updated page numbering</p>
<p>-Updated Index to include Enhanced Drug-Drug Interactions, Duplicate Drug Order Check, Allergy/ADR Order Check Display, Therapeutic Duplication, and CPRS Order Checks, and updated page numbering</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/2009</td>
<td>PSO*7*326</td>
<td><p>The Social Security Number was removed from print outs given to patients. The patient lookup has been expanded to include the ability to look up by prescription number or wand a barcode with the prescription from many options.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/2009</td>
<td>PSO*7*320</td>
<td><p>The following changes are included in this patch.</p>
<ul>
<li><p>Remote Data prompt, notification, and screen have been added.</p></li>
<li><p>A hidden action, DR [Display Remote], has been added.</p></li>
<li><p>"THIS PATIENT HAS PRESCRIPTIONS AT OTHER FACILITIES" prints at the end of the Pull Early from Suspense report.</p></li>
</ul>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

  
(This page included for two-sided copying.)

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Documentation Conventions](#documentation-conventions)
  - [Getting Help](#getting-help)
- [Related Manuals](#related-manuals)
- [Chapter 2: List Manager](#chapter-2-list-manager)
- [Outpatient List Manager](#outpatient-list-manager)
  - [Patient Demographics and Clinical Alerts](#patient-demographics-and-clinical-alerts)
- [Using List Manager with Outpatient Pharmacy](#using-list-manager-with-outpatient-pharmacy)
  - [Entering Actions](#entering-actions)
  - [Outpatient Pharmacy Hidden Actions](#outpatient-pharmacy-hidden-actions)
    - [Speed Actions](#speed-actions)
    - [Other Outpatient Pharmacy ListMan Actions](#other-outpatient-pharmacy-listman-actions)
    - [Other Screen Actions](#other-screen-actions)
- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Chapter 3: Using the Pharmacy Technician’s Menu](#chapter-3-using-the-pharmacy-technicians-menu)
- [Patient Lookup](#patient-lookup)
- [Chapter 4: Using the Bingo Board User Menu](#chapter-4-using-the-bingo-board-user-menu)
- [Bingo Board User](#bingo-board-user)
  - [Enter New Patient](#enter-new-patient)
  - [Display Patient's Name on Monitor](#display-patients-name-on-monitor)
  - [Remove Patient's Name from Monitor](#remove-patients-name-from-monitor)
  - [Status of Patient's Order](#status-of-patients-order)
  - [ScripTalk Mapping Error Messages](#scriptalk-mapping-error-messages)
- [Chapter 5: Changing the Label Printer](#chapter-5-changing-the-label-printer)
- [Change Label Printer](#change-label-printer)
- [Chapter 6: Check Drug Interaction](#chapter-6-check-drug-interaction)
- [Check Drug Interaction](#check-drug-interaction)
- [Chapter 7: Creating, Editing, and Printing a DUE Answer Sheet](#chapter-7-creating-editing-and-printing-a-due-answer-sheet)
- [DUE User](#due-user)
  - [Enter a New Answer Sheet](#enter-a-new-answer-sheet)
  - [Edit an Existing Answer Sheet](#edit-an-existing-answer-sheet)
  - [Batch Print Questionnaires](#batch-print-questionnaires)
- [Chapter 8: Using the Medication Profile](#chapter-8-using-the-medication-profile)
- [Medication Profile](#medication-profile)
  - [Medication Profile: Short Format](#medication-profile-short-format)
    - [OneVA Pharmacy and the Medication Profile](#oneva-pharmacy-and-the-medication-profile)
  - [Medication Profile: Long Format](#medication-profile-long-format)
- [Chapter 9: Processing a Prescription](#chapter-9-processing-a-prescription)
- [Patient Prescription Processing](#patient-prescription-processing)
    - [Hazardous Medication Warnings - Order Checks](#hazardous-medication-warnings-order-checks)
    - [Allergy Order Checks](#allergy-order-checks)
    - [OneVA Pharmacy Processing within Patient Prescription Processing](#oneva-pharmacy-processing-within-patient-prescription-processing)
- [# Outpatient Allergy Order Entry Process](#outpatient-allergy-order-entry-process)
    - [Clinical Reminder Order Checks](#clinical-reminder-order-checks)
    - [Enhanced Drug-Drug Interactions](#enhanced-drug-drug-interactions)
    - [Clinic Orders](#clinic-orders)
    - [Titration](#titration)
  - [Entering a New Order](#entering-a-new-order)
    - [Allergy/ADR Order Check Display](#allergyadr-order-check-display)
    - [Provider Override Reason: N/A - Order Entered Through VistA](#provider-override-reason-na-order-entered-through-vista)
    - [Therapeutic Duplication](#therapeutic-duplication)
    - [Dosing Order Checks](#dosing-order-checks)
    - [CPRS Order Checks](#cprs-order-checks)
    - [Entering a New Order – ePharmacy (Third Party Billable)](#entering-a-new-order-epharmacy-third-party-billable)
    - [NDC Validation](#ndc-validation)
  - [Using the Copy Action](#using-the-copy-action)
    - [Copying an ePharmacy Order](#copying-an-epharmacy-order)
    - [Holding and Unholding a Prescription](#holding-and-unholding-a-prescription)
  - [Renewing a Prescription](#renewing-a-prescription)
    - [Renewing an ePharmacy Order](#renewing-an-epharmacy-order)
- [Chapter 10: Pull Early from Suspense](#chapter-10-pull-early-from-suspense)
- [Pull Early from Suspense](#pull-early-from-suspense)
- [Chapter 11: Queue CMOP Prescription](#chapter-11-queue-cmop-prescription)
- [Queue CMOP Prescription](#queue-cmop-prescription)
- [Chapter 12: Releasing Medication](#chapter-12-releasing-medication)
- [Release Medication](#release-medication)
  - [Fixed Medication Copayment Tiers (FMCT)](#fixed-medication-copayment-tiers-fmct)
  - [Changes to Releasing Orders Function - Digitally Signed Orders Only](#changes-to-releasing-orders-function-digitally-signed-orders-only)
  - [Changes to Releasing Orders Function - ScripTalk](#changes-to-releasing-orders-function-scriptalk)
  - [Changes to Releasing Orders Function – Signature Alert](#changes-to-releasing-orders-function-signature-alert)
  - [Changes to Releasing Orders function – HIPAA NCPDP Global](#changes-to-releasing-orders-function-hipaa-ncpdp-global)
- [Chapter 13: Updating a Patient’s Record](#chapter-13-updating-a-patients-record)
- [Update Patient Record](#update-patient-record)
- [# Chapter 14: Meds by Mail – Virtual Pharmacy Services](#chapter-14-meds-by-mail-virtual-pharmacy-services)
- [Chapter 15: CPRS Order Checks: How They Work](#chapter-15-cprs-order-checks-how-they-work)
  - [Introduction](#introduction)
  - [Order Check Data Caching](#order-check-data-caching)
  - [Hash Counts and DEA Certification](#hash-counts-and-dea-certification)
- [Chapter 16: Error Messages](#chapter-16-error-messages)
- [Glossary](#glossary)
- [Index](#index)
This user manual describes the functional characteristics of Outpatient Pharmacy V. 7.0. It is intended for pharmacists and technicians who are familiar with the functioning of Outpatient Pharmacy in a VA Medical Center.
(*This page included for two-sided copying.)*

# Chapter 1: Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy (OP) software provides a way to manage the medication regimen of Veterans seen in the outpatient clinics and to monitor and manage the workload and costs in the Outpatient Pharmacy. The Pharmacy Ordering Enhancements (POE) project (patch PSO\*7\*46 for Outpatient Pharmacy) improves the flow of orders between Inpatient and Outpatient Pharmacy as well as between Computerized Patient Record System (CPRS) and backdoor pharmacy.

The primary benefits to the Veteran are the assurance that he or she is receiving the proper medication and the convenience of obtaining refills easily. The clinicians and pharmacists responsible for patient care benefit from a complete, accurate, and current medication profile available at any time to permit professional evaluation of treatment plans. Utilization, cost, and workload reports provide management cost controlling tools while maintaining the highest level of patient care.

The OneVA Pharmacy project (patch PSO\*7\*454 - December 2016) provided Pharmacists the capability to dispense prescriptions that originated in other VistA host sites. The OneVA Pharmacy User Manual and Installation Guide describe the site parameter required to use this functionality.

# Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *Outpatient Pharmacy V. 7.0 Technician’s User Manual* includes documentation conventions, also known as notations, which are used consistently throughout this manual. Each convention is outlined below.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Convention</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Menu option text is italicized.</td>
<td>There are eight options on the <em>Archiving</em> menu.</td>
</tr>
<tr class="even">
<td>Screen prompts are denoted with quotation marks around them.</td>
<td>The “Dosage:” prompt displays next.</td>
</tr>
<tr class="odd">
<td>Responses in bold face indicate user input.</td>
<td>Select Orders by number: (1-6): <strong>5</strong></td>
</tr>
<tr class="even">
<td><p><strong>&lt;Enter&gt;</strong> indicates that the Enter key (or Return key on some keyboards) must be pressed.</p>
<p><strong>&lt;Tab&gt;</strong> indicates that the Tab key must be pressed.</p></td>
<td><p>Type <strong>Y</strong> for Yes or <strong>N</strong> for No and press <strong>&lt;Enter&gt;</strong>.</p>
<p>Press <strong>&lt;Tab&gt;</strong> to move the cursor to the next field.</p></td>
</tr>
<tr class="odd">
<td>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/002.png)Indicates especially important or helpful information.</td>
<td><blockquote>
<p>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/003.png)Up to four of the last LAB results can be displayed in the message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/004.png)Indicates that options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.</p>
</blockquote></td>
<td>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/005.png)This option requires the security key PSOLOCKCLOZ.</td>
</tr>
</tbody>
</table>

## Getting Help 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

?, ??, ??? One, two or three question marks can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

# Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals are located on the VistA Documentation Library (VDL) at: <http://www.va.gov/vdl>.

Main Package Documentation:

- Outpatient Pharmacy V. 7.0 Release Notes
- Outpatient Pharmacy V. 7.0 Manager’s User Manual
- Outpatient Pharmacy V. 7.0 Pharmacist’s User Manual
- Outpatient Pharmacy V. 7.0 Technician’s User Manual
- Outpatient Pharmacy V. 7.0 User Manual – Supplemental
- Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide
- Dosing Order Check User Manual
- VistA to MOCHA Interface Document
- *Installation Guide – OneVA Pharmacy*
- *Release Notes – OneVA Pharmacy*
- *User Manual – OneVA Pharmacy*Additional Documentation:

Additional documentation related to specific projects is also located on the VDL. For example, there may be several different Release Notes documents, which apply to specific projects. Also, there may be several sets of “Change Page” documents, which apply to changes made only for a specific package patch.

# Chapter 2: List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The screen displayed when processing an order has changed dramatically from the previous version of Outpatient Pharmacy (e.g., v. 6.0). The new screen was designed using List Manager.

This new screen gives more information and easier accessibility to vital reports and areas of a patient’s chart.

Please take the time to read over the explanation of the screen and the actions that can now be executed at the touch of a key. This type of preparation before attempting to use List Manager will reduce the time and effort needed to become skilled in order processing with this new version of List Manager.

# Outpatient List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Screen title:      | The screen title changes according to what type of information List Manager is displaying (e.g., Patient Information, Medication Profile, New OP Order (ROUTINE), etc.).                                                                                                                                                                                                                                     |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allergy indicator: | This indicator displays when there has been information entered into the ALLERGY field for the patient. The indicator displays “NO ALLERGY ASSESSMENT” if there is no allergy assessment for the patient.                                                                                                                                                                                                    |
| Header area:       | <span id="HEADER_LM" class="anchor"></span>The header area is a "fixed" (non-scrollable) area that displays patient information, including demographic information and Clinical Alerts.                                                                                                                                                                                                                      |
| List area:         | (scrolling region) This area scrolls (like the previous version) and displays the information on which action can be taken.                                                                                                                                                                                                                                                                                  |
| Message window:    | This section displays a plus (+) sign, minus (-) sign, or informational text (i.e., Enter ?? for more actions). If a plus sign is entered at the action prompt, List Manager will "jump" forward a page. If a minus sign is displayed and entered at the action prompt, List Manager will "jump" back a screen. The plus and minus signs are only valid actions if they are displayed in the message window. |
| Action area:       | A list of actions display in this area of the screen. If a double question mark (??) is entered at the “Select Item(s)” prompt, a “hidden” list of additional actions that are available will be displayed. Outpatient Pharmacy hidden actions are displayed with the letters (OP) next to the action.                                                                                                       |

Example: Showing more Indicators and Definitions

> Medication Profile May 22, 2006 10:44:56 Page: 1 of 1

> OPPATIENT16,ONE \<A\>

> PID: 000-24-6802 Ht(cm): 177.80 (02/08/2004)

> DOB: APR 3,1941 (65) Wt(kg): 90.45 (02/08/2004)

> SEX: MALE

> CrCL: 102.4(est.) (CREAT:1.0mg/dL 10/30/12) BSA (m2): 2.08

> Non-VA Meds on File

> Last entry on 01/13/01

> ISSUE LAST REF DAY

> \# RX \# DRUG QTY ST DATE FILL REM SUP

> ------------------------------------ACTIVE----------------------------------

> 1 503902 ACETAMINOPHEN 500MG TAB 60 AT 05-22 05-22 3 30

> 2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

> 3 503871\$ HISTOPLASMIN 1ML 1 A 03-14 03-14R 5 30

> 4 100002042\$e NALBUPHINE HCL INJ 10MG/ML 1 A 03-14 03-14 5 30

> 5 100002040\$ SALICYLIC ACID 40% OINT (OZ) 1 S 03-14 03-17 5 30

> ---------------------------------DISCONTINUED----------------------------------

> 6 503881 BACLOFEN 10MG TABS 30 DC 04-07 05-01 2 30

> 7 100002020A\$ TIMOLOL 0.25% OPTH SOL 10ML 1 DE 02-03 02-03 5 30

> 8 10000205 HALOPERIDOL 20MG TAB 1 DF 02-03 02-03 5 30

> 9 8201954 BILAFUMIN .05 MG CAP 1 DP 01-03 03-03 5 30

> 10 6041972 RONINPENSATE 15MG SA TAB 1 DD 03-03 04-03 5 30

> 11 3012001 PRESTANUS 1% SOL 1 DA 02-03 02-03 5 30

> --------------------------------------HOLD-------------------------------------

> 12 8251996 VONITRATE CAL 325MG EC TAB 1 HP 02-03 02-03 5 30

> 13 100001942 ABDOMINAL PAD 7 1/2 X 8 STERILE 1 H 09-28 09-28 5 30

> ----------------------------------NON-VERIFIED---------------------------------

> 14 100002039\$ BACLOFEN 10MG TABS 30 N 03-14 03-14 5 30

> ------------------------------------PENDING------------------------------------

15 AMPICILLIN 250MG CAP QTY: 40 ISDT: 05-29 REF: 0

16 SIMETHICONE 40MG TAB QTY: 30 ISDT: 05-30 REF: 3

> ------------------------NON-VA MEDS (Not dispensed by VA)----------------------

> GINKO EXT 1 TAB ONCE A DAY BY MOUTH Date Documented: 01/13/01

> IBUPROFPEN 50MG TAB Date Documented: 12/10/00

> Enter ?? for more actions

> PU Patient Record Update NO New Order

> PI Patient Information SO Select Order

> Select Action: Quit//

All orders are sub-grouped by like statuses and then listed alphabetically within the sub-group.

| Order Status: | The current status of the order. These statuses include: |
|-------------------|----------------------------------------------------------|
|                   | A Active                                                 |
|                   | S Suspended                                              |
|                   | N Non-Verified or Drug Interactions                      |
|                   | HP Placed on hold by provider through CPRS               |
|                   | H Placed on hold via backdoor Pharmacy                   |
|                   | E Expired                                                |
|                   | DA Auto discontinued due to admission                    |
|                   | DP Discontinued by provider through CPRS                 |

The Status column may also reflect the type of Discontinue action performed on the order:

> DF Discontinued due to edit by a provider through CPRS

> DE Discontinued due to edit via backdoor Pharmacy

> DC Discontinued via backdoor Pharmacy

> DD Discontinued due to death

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/006.png)A “B” will be appended to the above statuses if the Bad Address Indicator was set and there was no active temporary address at the time of the last label activity.

CMOP Indicators: There are two separate indicators when the drug in an order is marked for Consolidated Mail Outpatient Pharmacy (CMOP) processing. This indicator is displayed after the Order Status if applicable.

\> Drug for the prescription is marked for CMOP

T Displayed when the last fill is either in a Transmitted or Retransmitted CMOP state. (This indicator can overwrite the “\>” indicator.

Copay Indicator: A “\$” displayed to the right of the prescription number indicates the prescription is copay eligible.

ePharmacy An ‘e’ displayed to the right of the prescription number indicates that

Indicator: the prescription is electronic third-party billable.

Return to Stock An “R” displayed to the right of the Last Fill Date indicates the last fill

Indicator: was returned to stock.

Pending Orders: Any orders entered through Computerized Patient Records System (CPRS), or another outside source, that have not been finished by Outpatient Pharmacy.

Non-VA Meds: Any over the counter (OTC) medications, herbal supplements, medications.

Orders: prescribed by providers outside the VA, and medications prescribed by the VA, but purchased by the patient at an outside pharmacy are displayed here. Non-VA Meds orders cannot be placed or updated in Outpatient Pharmacy. The user can input information about a patient’s use of Non-VA Meds only through CPRS. However, the user can use either CPRS or Outpatient Pharmacy menu options to view Non-VA Meds data in a patient’s medical records.

Third Party Rejects Any prescriptions that are rejected by third-party payers because of Refill Too Soon (code 79) or Drug Utilization Review (DUR - code 88) are displayed in this section.

Example: Showing Rejected Prescriptions

Medication Profile August 12, 2006@12:35:04 Page: 1 of 1

OPPATIENT, ONE \<A\>

PID: 000-24-6802 Ht(cm): 177.80 (02/08/2005)

DOB: APR 3,1941 (65) Wt(kg): 90.45 (02/08/2005)

SEX: MALE

CrCL: 78.1(est.) (CREAT:1.0mg/dL 6/24/03) BSA (m2): 2.08

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

----------------REFILL TOO SOON/DUR REJECTS (Third Party)----------------------

1 51368009\$e DIGOXIN (LANOXIN) 0.05MG CAP 90 A\> 02-16 02-16 3 90

2 51360563e OXYBUTYNIN CHLORIDE 15MG SA TAB 180 S\> 02-15 05-06 0 90

---------------------------------ACTIVE---------------------------------------

3 100003470e ABSORBABLE GELATIN FILM 1 A 11-04 11-04 5 31

4 100003461 ACETAMINOPHEN 650MG SUPPOS. 10 A\> 11-04 11-04 1 10

5 100003185e ALBUMIN 25% 50ML 2 A 08-01 08-01 5 5

-----------------------------------DISCONTINUED-------------------------------

6 100003530 ANALGESIC BALM 1 POUND 1 A 01-08 01-08 3 90

7 100003400 APPLICATORS, COTTON TIP STERILE 10 A 09-23 09-23 5 31

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen//

## Patient Demographics and Clinical Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient demographic information and Clinical Alerts display in the List Manager header area when using certain Pharmacy options.

The demographic details are derived from existing patient information and include details such as date of birth, weight, height, and gender, as well as information about the patient’s primary care team and/or physician, physician contact numbers (phone/pager), clinician remarks, and assigned or recent facility where care is received.

Clinical Alerts are used to convey important patient care information. Pharmacy Supervisors can enter one or more alerts using the Clinical Alert Enter/Edit \[PSO CLINICAL ALERT ENTER/EDIT\] option to make pharmacy personnel aware of things like drug interactions or the patient’s participation in clinical trials. For more information on setting up Clinical Alerts, refer to the Outpatient Pharmacy (PSO) Manager’s User Manual.

Patient demographics and any Clinical Alerts are prominently displayed when using either of the following Pharmacy options:

- Medication Profile \[PSO P\]
- Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]

> **NOTE:** Pharmacists and Pharmacy Managers see additional demographics and Clinical Alerts when using certain other Pharmacy options that are not available to Pharmacy Technicians. More information on these options can be found in the *Outpatient Pharmacy (PSO) Manager’s User Manual* or the *Outpatient Pharmacy (PSO) Pharmacist’s User Manual*.

Example: Header Displaying Patient Demographics and Clinical Alerts

Example: Clinical Alerts Displayed with Patient Demographics

OPPATIENT16,ONE \<A\>

PID: 000-12-3456 Ht(cm): 175.26 (08/06/2000)

DOB: AUG 30,1948 (62) Wt(kg): 108.18 (01/14/2006)

SEX: MALE

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 70

RX PATIENT STATUS: SC LESS THAN 50%

Extended Patient Demographics

Primary Care Team: GREEN TEAM Phone: (307)778-7533

PC Provider: SAAD,VANCE MILTON Position: PROV GREEN 7

Pager: 12345 Phone: 8001234567

Remarks:\*\*PURPLE HEART RECIPIENT\*\*

Assigned/Recent Facility: CHEYENNE VAMC

CLINICAL ALERTS:

AUG 16, 2017@08:53:38 ENROLLED IN CLINICAL TRIAL

OCT 06, 2017@11:54:32 REMOVED FROM CLINICAL TRIAL – ELEVATED BP

# Using List Manager with Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager is a tool designed so that a list of items can be presented to the user for an action.

For Outpatient Pharmacy, the List Manager does the following:

- Allows the pharmacist or technician to browse through a list of actions.
- Allows the pharmacist or technician to take action against those items.
- Allows the user to select an action that displays an action or informational profile.
- Allows the user to select a different action without leaving an option.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/007.png)Not all functionality displayed in this section (i.e., hidden and speed actions) is available to pharmacy technicians.

## Entering Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Actions are entered by typing the name(s), or synonym(s) at the “Select Item(s)” prompt. In addition to the various actions that may be available specific to a particular option, List Manager provides generic actions applicable to any List Manager screen. A double question mark (??) may be entered at the “Select Action” prompt for a list of all actions available. The following is a list of generic List Manager actions with a brief description. The synonym for each action is shown in brackets following the action name. Entering the synonym is the quickest way to select an action. Outpatient Pharmacy hidden actions are displayed with the letters (OP) next to the action.

| Action                     | Description                                                              |
|--------------------------------|------------------------------------------------------------------------------|
| Next Screen \[+\]              | Move to the next screen (may be shown as a default).                         |
| Previous Screen \[-\]          | Move to the previous screen.                                                 |
| Up a Line \[UP\]               | Move up one line.                                                            |
| Down a Line \[DN\]             | Move down one line.                                                          |
| Shift View to Right \[\>\]     | Move the screen to the right if the screen width is more than 80 characters. |
| Shift View to Left \[\<\]      | Move the screen to the left if the screen width is more than 80 characters.  |
| First Screen \[FS\]            | Move to the first screen.                                                    |
| Last Screen \[LS\]             | Move to the last screen.                                                     |
| Go to Page \[GO\]              | Move to any selected page in the list.                                       |
| Re Display Screen \[RD\]       | Redisplay the current.                                                       |
| Print Screen \[PS\]            | Prints the header and the portion of the list currently displayed.           |
| Print List \[PL\]              | Prints the list of entries currently displayed.                              |
| Search List \[SL\]             | Finds selected text in list of entries.                                      |
| Auto Display (On/Off) \[ADPL\] | Toggles the menu of actions to be displayed/not displayed automatically.     |
| Quit \[QU\]                    | Exits the screen (may be shown as a default).                                |

## Outpatient Pharmacy Hidden Actions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy hidden actions will display with the previous hidden actions once a completed or finished order is selected and a double question mark (??) is entered at the “Select Action” prompt.

The following hidden actions appear on the prescription profile screen and can only be applied to one order at a time.

Action Description

Activity Logs \[AL\] Displays the Activity Logs.

Copy \[CO\] Allows the user to copy and edit an order.

Check Interactions \[CK\] Allows a user to perform order checks against the patient’s active medication profile with or without a prospective drug.

DIN Displays available drug restriction/guideline information for the  
Dispense Drug and Orderable Item associated with the selected medication order.

Intervention Menu (IN) Allows a user to enter a new intervention or delete, edit, print and view an existing intervention.

Hold \[HD\] Places an order on a hold status.

Other OP Actions \[OTH\] Allows the user to choose from the following sub-actions:

Progress Note \[PN\],

Action Profile \[AP\],

Print Medication Instructions \[MI\],

Display Orders' Statuses \[DO\], or

Non-VA Meds Report \[NV\].

Patient Information \[PI\] Shows patient information, allergies, adverse reactions, and pending clinic appointments.

Pull Rx \[PP\] Action taken to pull prescription(s) early from suspense.

Reprint \[RP\] Reprints the label.

> ![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/008.png) Note: The Reprint function is not enabled for

> OneVA Pharmacy labels. To reprint a OneVA Pharmacy

> label execute a OneVA Pharmacy partial.

View Reject \[REJ\] Allows the user to view and resolve the Refill Too Soon or Drug Utilization Review returned by the third party payer for a specific prescription/fill claim.

Unhold \[UH\] Removes an order from a hold status.

Verify \[VF\] Allows the pharmacist to verify an order a pharmacy technician has entered.

The PSO HIDDEN ACTIONS Protocol in PROTOCOL File (#101) includes two hidden actions, PSO LM BACKDOOR MARK AS TITRATION and PSO LM BACKDOOR TITRATION RX REFILL, which are both added to the PROTOCOL File (#101).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* IMPORTANT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The enhancements related to Titration/Maintenance dose Rx are made only

for Outpatient Pharmacy package. The corresponding changes to CPRS package

are not included at this time. Therefore, the CPRS Order Copy and Order

Change functionalities will continue to function as is. Furthermore, there

will be no indication of a Titration/Maintenance order in the CPRS

application.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

There is also a hidden action, TR (Convert Titration Rx), in the Patient Prescription Processing \[PSO LM BACKDOOR TITRATION RX REFILL\] option. This action populates the MAINTENANCE DOSE RX (#45.2) field in the PRESCRIPTION File (#52). When a titration to maintenance prescription needs to be refilled so the patient can continue on the Maintenance Dose, this option allows the users to create a new prescription with the maintenance dose only. This process works similar to copying an existing prescription; however, it can only be used on prescriptions with the following characteristics:

- Rx is a complex order with a THEN conjunction
- Rx is released
- Rx status is ACTIVE
- Rx does not have refills previously ordered
- Rx \# Of Refills is greater than 0 (zero)

Before the new Maintenance Rx can be accepted, the user is prompted to validate the QTY field for the new Rx, which may or may not be automatically re-calculated. Only the last dose from the original prescription is carried over to the new Maintenance Rx, and the \# of Refills field is decreased by 1 because the new Maintenance Rx counts as a fill.

Once a user verifies the information for the Maintenance Rx is accurate, they can accept the Maintenance Rx. This action triggers a Duplicate Drug check against the original complex order, which must be discontinued before the new Maintenance Rx can be accepted. After the new Maintenance Rx is accepted, it will have the new indicator 'm' on the right side of the Rx \# in the patient's Medication Profile.

: : :

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------ACTIVE-------------------------------

1 100005436m AMOXAPINE 50MG TAB 30 S 09-26 09-26 1 30

2 100005022 AMOXICILLIN 250MG CAP 30 A 08-18 08-18 11 30

3 100005035 KALETRA 3 A 09-29 09-29 0 3

: : :

### Speed Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Outpatient Pharmacy actions are referred to as “speed actions” and appear on the medication profile screen. These actions can be applied to one or more orders at a time.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Reprint [RP]</td>
<td><p>Reprints the label.</p>
<p>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/009.png) <strong>Note:</strong> The Reprint function is not enabled for OneVA Pharmacy labels. To reprint a OneVA Pharmacy label execute a OneVA Pharmacy partial.</p></td>
</tr>
<tr class="even">
<td>Renew [RN]</td>
<td>A continuation of a medication authorized by the provider.</td>
</tr>
<tr class="odd">
<td>Refill [RF]</td>
<td>A second or subsequent filling authorized by the provider.</td>
</tr>
<tr class="even">
<td>Reprint Signature [RS]</td>
<td>Reprints the signature log.</td>
</tr>
<tr class="odd">
<td>Discontinue [DC]</td>
<td>Status used when an order was made inactive either by a new order or by the request of a physician.</td>
</tr>
<tr class="even">
<td>Release [RL]</td>
<td>Action taken at the time the order is filled and ready to be given to the patient.</td>
</tr>
<tr class="odd">
<td>Pull Rx [PP]</td>
<td>Action taken to pull prescription(s) early from suspense.</td>
</tr>
<tr class="even">
<td>Inpat. Profile [IP]</td>
<td>Action taken to view an Inpatient Profile.</td>
</tr>
<tr class="odd">
<td>CM</td>
<td>Action taken to manually queue to CMOP.</td>
</tr>
<tr class="even">
<td>Fill/Rel Date Disply [RDD]</td>
<td>Switch between displaying the FILL DATE column and the LAST RELD column.</td>
</tr>
<tr class="odd">
<td>Display Remote [DR]</td>
<td>Action taken to display a patient’s remote prescriptions.</td>
</tr>
</tbody>
</table>

### Other Outpatient Pharmacy ListMan Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Action  | Description                |
|-------------|--------------------------------|
| Exit \[EX\] | Exit processing pending orders |
| AC          | Accept                         |
| BY          | Bypass                         |
| DC          | Discontinue                    |
| ED          | Edit                           |
| FN          | Finish                         |

### Other Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Edit/Enter Allergy/ADR Data [EA]</td>
<td>Provides access to the Adverse Reaction Tracking package to allow entry and/or edit of allergy adverse reaction data for the patient. See the Adverse Reaction Tracking package documentation for more information on allergy/ADR processing.</td>
</tr>
<tr class="even">
<td>Detailed Allergy Display [DA]</td>
<td>Displays a detailed listing of the selected item from the patient's allergy/ADR list. Entry to the Edit Allergy/ADR Data action is provided with this list also.</td>
</tr>
<tr class="odd">
<td>Patient Record Update [PU]</td>
<td>Allows editing of patient data such as SSN, birth date, address, phone, and outpatient narrative. Patient data can also be updated using the <em>Update Patient Record</em> menu option. If implementing Other Language Modifications, either can be used to set a patient's other language preference.</td>
</tr>
<tr class="even">
<td>New Order [NO]</td>
<td>Allows new orders to be entered for the patient.</td>
</tr>
<tr class="odd">
<td>Exit Patient List [EX]</td>
<td>Exit patient’s Patient Information screen so that a new patient can be selected.</td>
</tr>
<tr class="even">
<td>Refill Rx from Another VA Pharmacy (RF)</td>
<td><p>OneVA Pharmacy (patch PSO*7*454) introduced the RF action item on the new ‘REMOTE OP Medications’ profile. The RF action item allows the Pharmacist to refill a prescription order that originated from another VA Pharmacy location.</p>
<p>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/010.png) <strong>Note:</strong> For additional information regarding OneVA Pharmacy RF processing go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – OneVA Pharmacy” document.</p></td>
</tr>
<tr class="odd">
<td>Partial from Another VA Pharmacy (PR)</td>
<td><p>OneVA Pharmacy (patch PSO*7*454) introduced the PR action item on the new ‘REMOTE OP Medications’ profile. The PR action item allows the Pharmacist to partial a prescription order that originated from another VA Pharmacy location.</p>
<p>![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/011.png)<strong>Note:</strong> For additional information regarding OneVA Pharmacy PR processing go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – OneVA Pharmacy” document.</p></td>
</tr>
</tbody>
</table>

# (*This page included for two-sided copying.)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Chapter 3: Using the Pharmacy Technician’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options shown in this chapter are intended for use by pharmacy technicians and other pharmacy personnel assigned the *PSO USER2* menu, who will view prescriptions and/or inquire into other Outpatient Pharmacy files.

Example: Accessing the Pharmacy Technician’s Menu

Select OPTION NAME: PSOUSER2 Pharmacy Technician's Menu

Outpatient Pharmacy software - Version 7.0

The following options are available on this menu:

- *Bingo Board User ...*
- *Change Label Printer*
- *DUE User ...*
- *Medication Profile*
- *Patient Prescription Processing*
- *Pull Early from Suspense*
- *Queue CMOP Prescription*
- *Release Medication*
- *Update Patient Record*

# Patient Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ability to look up a patient by prescription number or wand a barcode with the prescription has been added to the patient lookup prompt on the following options.

- *Bingo Board User ... \[PSO BINGO USER\]*
- *Medication Profile \[PSO P\]*
- *Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]*
- *Update Patient Record \[PSO PAT\]*

The help text for patient lookup reads as follows.

Enter the prescription number prefixed by a \# (ex. \#XXXXXXX) or

Wand the barcode of the prescription. The format of the barcode is

NNN-NNNNNNN where the first 3 digits are your station number.

\- OR -

Enter the universal Member ID number from the patient's VHIC Card

or wand the barcode of the VHIC card

\- OR -

Answer with PATIENT NAME, or SOCIAL SECURITY NUMBER, or last 4 digits

of SOCIAL SECURITY NUMBER, or first initial of last name with last 4

digits of SOCIAL SECURITY NUMBER

Do you want the entire NNNNNNNN-Entry PATIENT List?

*(This page included for two-sided copying.)*

# Chapter 4: Using the Bingo Board User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options available on the Bingo Board User menu.

# Bingo Board User 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO BINGO USER\]

This menu enables use of the bingo board display. The options on this menu allow the user to display, enter, or remove a patient’s name or a number from the bingo board display located in the pharmacy area.

When the routing for an order is set to “Window”, the entering of prescription orders stores information in the bingo board PATIENT NOTIFICATION (Rx READY) file. For new, renew, pull early from suspense, refill orders, barcode refill/renew, and finish process for orders entered via Computerized Patient Record System (CPRS), the date and time is captured when the order is stored in this file. The same occurs for partials, except the time is captured when a prescription number is entered.

Releasing the prescription places the name or ticket number of the patient on the bingo board monitor if a display group exists and stores data in the WAITING TIME file. The options on this menu are used to manually enter, display, or remove a patient’s name or number from the monitor.

The following options are available on the *Bingo Board User* menu:

- *Enter New Patient*
- *Display Patient’s Name on Monitor*
- *Remove Patient’s Name from Monitor*
- *Status of Patient’s Order*

## Enter New Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO BINGO NEW PATIENT\]

Use this option to manually enter the name of a new patient on the bingo board. Each prescription number for the patient's order must be entered.

A “Ticket \#” prompt appears if ticket number was chosen as the method of display in the *Enter/Edit Display* option on the *Bingo Board Manager* menu. Enter the ticket number and at the next prompt enter each of the prescription numbers for that patient.

## Display Patient's Name on Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO BINGO DISPLAY PATIENT\]

Use this option to begin displaying the name or number of a patient whose prescription is ready. The message, “PRESCRIPTIONS ARE READY FOR:” appears as fixed text on the display screen. This option displays the following reminder for ECME billable prescriptions: “\*\*\* This Pharmacy Rx requires a patient signature! \*\*\*”

## Remove Patient's Name from Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO BINGO DELETE PATIENT\]

After the patient picks up the prescription, remove the name or ticket number from the display either manually or through the barcode reader.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/012.png)It is recommended that a patient’s name be removed from the monitor as soon as the prescription is picked up.

## Status of Patient's Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO BINGO STATUS\]

This option enables checking of the number of prescriptions a patient has ready, the division, time in/time out, and the prescription number(s). There are four possible statuses:

| Status           | Description                                                                       |
|------------------|-----------------------------------------------------------------------------------|
| Pending          | Active order input via CPRS that is in the PENDING OUTPATIENT ORDERS file.        |
| Being Processed  | Order that is in the PATIENT NOTIFICATION (Rx READY) file, but not displayed.     |
| Ready For Pickup | Order that is in the PATIENT NOTIFICATION (Rx READY) file and is being displayed. |
| Picked Up        | Order that has been picked up.                                                    |

Example: Status of Patient’s Order

Select Bingo Board User Option: STATUS of Patient's Order

Enter Patient Name: OPPATIENT3,ONE 02-23-74 000579013 NO NSC VETERAN

OPPATIENT3,ONE has the following orders for 10/31/06

Being Processed: \*\*\*Entered on OCT 31, 2006\*\*\*

Division: GENERAL HOSPITAL Time In: 10:27 Time Out:

Rx \#: 500416,

Pending:

Orderable Item: ACETAMINOPHEN Provider: OPPROVIDER3,TWO

Entered By: OPCLERK2,FOUR Time In: 10/31/06@06:46

Drug: ACETAMINOPHEN 325MG TAB UD Routing: MAIL

Ready For Pickup:

Division: GENERAL HOSPITAL Time In: 10:36 Time Out: 10:46

Rx \#: 1022731,

Enter Patient Name:

## ScripTalk Mapping Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of the error messages that will be displayed on the screen for a site using the Bingo Board in the event of a mapping issue with the ScripTalk device when ScripTalk labels are printed.

| Error Level | Error Message                                                                                         | Why message is being displayed.                                                                                                |
|-----------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| System          | Please review ScripTalk mapped device setup.                                                              | The system has detected that there is a printer in the PRINTER TO BE MAPPED field, but no device has been selected.                |
| System          | NO SCRIPTALK PRINTER DEFINED FOR THIS DIVISION!                                                           | The system cannot find a division printer defined. However, there is a properly defined printer in the PRINTER TO BE MAPPED field. |
| System          | There is no mapped printer and the division printer is set for manual.                                    | There is no PRINTER TO BE MAPPED and the Division printer is set for manual. No ScripTalk label will print.                        |
| System          | NO SCRIPTALK PRINTER DEFINED FRO THIS DIVISION! No mapped printer defined. No ScripTalk label will print. | No printers are defined so no label will print.                                                                                    |

(*This page included for two-sided copying.)*

# Chapter 5: Changing the Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the *Change Label Printer* option.

# Change Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO CHANGE PRINTER\]

This option allows the user to change the printer to which labels are printed.

Select Outpatient Pharmacy Manager Option: Change Label Printer

Select LABEL PRINTER: LABELPRT2// \<Enter\> LABELPRT2

OK to assume label alignment is correct? YES//\<Enter\>

(*This page included for two-sided copying.)*

# Chapter 6: Check Drug Interaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the *Check Drug Interaction* option shown on the Outpatient Pharmacy Manager \[PSO MANAGER\] menu and the Pharmacist Menu \[PSO USER1\].

# Check Drug Interaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO CHECK DRUG INTERACTION\]

This option allows a user to check drug interactions between two or more drugs.

Select Outpatient Pharmacy Manager Option: CHECK Drug Interaction

Drug 1: WARFARIN 2MG TABS BL110

...OK? Yes// (Yes)

Drug 2: SIMVASTATIN 40MG TAB

Lookup: GENERIC NAME

SIMVASTATIN 40MG TAB CV350

...OK? Yes// (Yes)

Drug 3:

Now Processing Enhanced Order Checks! Please wait...

\*\*\* DRUG INTERACTION(S) \*\*\*

============================================================

\*\*\*Significant\*\*\* Drug Interaction with

SIMVASTATIN 40MG TAB and

WARFARIN 2MG TABS

CLINICAL EFFECTS: Increase hypoprothrombinemic effects of warfarin.

============================================================

Press Return to Continue...:

Display Professional Interaction monograph? N// YES

DEVICE: HOME// SSH VIRTUAL TERMINAL Right Margin: 80//

------------------------------------------------------------

Professional Monograph

Drug Interaction with SIMVASTATIN 40MG TAB and WARFARIN 2MG TABS

This information is generalized and not intended as specific medical

advice. Consult your healthcare professional before taking or

discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Selected Anticoagulants/Selected HMG-CoA Reductase

Inhibitors

SEVERITY LEVEL: 3-Moderate Interaction: Assess the risk to the

patient and take action as needed.

MECHANISM OF ACTION: The exact mechanism of this interaction is

unknown. The HMG-CoA reductase inhibitor may inhibit the hepatic

hydroxylation of warfarin. The HMG-CoA reductase inhibitors, which

are highly plasma protein bound, may displace warfarin from its

binding site.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with SIMVASTATIN 40MG TAB and WARFARIN 2MG TABS

CLINICAL EFFECTS: Increase hypoprothrombinemic effects of warfarin.

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Patients should be monitored for changes in

prothrombin time when a HMG Co-A reductase inhibitor is added to or

discontinued from warfarin therapy, or if the dosage of the HMG Co-A

reductase inhibitor is adjusted.

DISCUSSION: Case reports in the medical literature and to the

manufacturer have documented an interaction between lovastatin and

warfarin. A case report has documented an interaction between

pravastatin and fluindione (an orally administered indanedione

anticoagulant), suggesting that pravastatin could also interact

similarly with warfarin. Information concerning a potential

interaction with simvastatin is conflicting. A case report has

documented an interaction between simvastatin and acenocoumarol while

another case report showed no interaction with warfarin. One group of

authors reported three case reports of increased international

normalized ratios (INRs) following the addition of fluvastatin to

warfarin therapy. The addition of rosuvastatin to patients stabilized

on warfarin resulted in clinically significant changes in INR.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with SIMVASTATIN 40MG TAB and WARFARIN 2MG TABS

REFERENCES:

1.Ahmad S. Lovastatin. Warfarin interaction. Arch Intern Med 1990 Nov;

150(11):2407.

2.Hoffman HS. The interaction of lovastatin and warfarin. Conn Med

1992 Feb; 56(2):107.

3.Iliadis EA, Konwinski MF. Lovastatin during warfarin therapy

resulting in bleeding. Pa Med 1995 Dec;98(12):31.

4.Personal communication. Merck & Co., Inc. 1991.

5.Trenque T, Choisy H, Germain ML. Pravastatin: interaction with oral

anticoagulant?. BMJ 1996 Apr 6;312(7035):886.

6.Grau E, Perella M, Pastor E. Simvastatin-oral anticoagulant

interaction. Lancet 1996 Feb 10;347(8998):405-6.

7.Gaw A, Wosornu D. Simvastatin during warfarin therapy in

hyperlipoproteinaemia. Lancet 1992 Oct 17;340(8825):979-80.

8.Trilli LE, Kelley CL, Aspinall SL, Kroner BA. Potential interaction

between warfarin and fluvastatin. Ann Pharmacother 1996 Dec;

30(12):1399-402.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with SIMVASTATIN 40MG TAB and WARFARIN 2MG TABS

9.Crestor (rosuvastatin calcium) US prescribing information.

AstraZeneca Pharmaceuticals LP February, 2012.

Copyright 2012 First DataBank, Inc.

------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

Display Professional Interaction monograph? N// O

# Chapter 7: Creating, Editing, and Printing a DUE Answer Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options on the *DUE User* menu.

# DUE User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSOD DUE USER\]

This menu provides the means to create an answer sheet entry in the DUE ANSWER SHEET file and edit an existing Answer Sheet. A blank form of a selected DUE questionnaire can also be printed in multiple copies to be distributed to providers to complete when ordering medications being evaluated.

- *Enter a New Answer sheet*
- *Edit an Existing Answer Sheet*
- *Batch Print Questionnaires*

## Enter a New Answer Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSOD CREATE ANSWER SHEET\]

In this option, answers to a DUE Questionnaire can be entered. This creates an answer sheet entry in the DUE ANSWER SHEET file. These answer sheets can be kept online for statistical and/or compliance studies. Answer sheets are stored in the file using a sequence number. This number is automatically generated by the computer and should be written on the hard copy of the answer sheet immediately so that it can be used later in editing or deleting the entry.

## Edit an Existing Answer Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSOD EDIT ANSWER SHEET\]

Edit a DUE Answer Sheet entry using this option. Ordinarily, the sequence number is available when editing the Answer Sheet; however, the user can search the file if the provider, drug, or questionnaire is known by typing ^S at the “SEQUENCE NUMBER” prompt. The search displays all of the entries containing the combination of provider, drug, or questionnaire used in the search.

## Batch Print Questionnaires

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSOD BATCH PRINT QUESTIONNAIRE\]

To print a blank form of a selected questionnaire, enter the number of copies and a printer device. These questionnaire answer sheets can be distributed to providers to complete when ordering medications being evaluated.

(*This page included for two-sided copying.)*

# Chapter 8: Using the Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the Medication Profile, its different formats, and how it can be used in patient care.

# Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO P\]

The Medication Profile displays a profile of all prescriptions on file for a particular patient. The prescription display includes all Non-VA Med orders also. Effective with the OneVA Pharmacy (patch PSO\*7\*454 – December 2016), the Medication Profile displays all active medications from other facilities. The medications are retrieved from the Health Data Repository/Clinical Data Service (HDR/CDS) Repository and are displayed below the ‘local’ or ‘Non-VA Med’ orders and are sorted/grouped by facility. The prescriptions originating from other VA Pharmacy locations display under a divider header line showing the site name, site number, and status. The user may view this information directly on the screen or request it to be printed. The medication profile is available in two formats: short or long.

<span id="PSO_P" class="anchor"></span>Patient demographics and Clinical Alerts display in the header area when using this option. Refer to [Patient Demographics and Clinical Alerts](#patient-demographics-and-clinical-alerts) for more information.

## Medication Profile: Short Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The short format displays the following information:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>patient name</p></li>
</ul></th>
<th><ul>
<li><p>address</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>last four digits of the patient’s SSN</p></li>
</ul></td>
<td><ul>
<li><p>DOB</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Eligibility</p></li>
</ul></td>
<td><ul>
<li><p>narrative</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>reactions</p></li>
</ul></td>
<td><ul>
<li><p>prescriptions</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>prescription number</p></li>
</ul></td>
<td><ul>
<li><p>drug name</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Sig</p></li>
</ul></td>
<td><ul>
<li><p>status</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>quantity</p></li>
</ul></td>
<td><ul>
<li><p>issue date</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>last fill date</p></li>
</ul></td>
<td><ul>
<li><p>refills remaining</p></li>
</ul></td>
</tr>
</tbody>
</table>

The short report format of the fields for Non-VA Med orders include the drug name or orderable item name, dosage, schedule and date documented.

The short format displays the status and or action in an abbreviated form. The following is an explanation of the codes:

Code Status/Description

A Active

B Bad Address Indicated

> DF Discontinued due to edit by a provider through CPRS

> DE Discontinued due to edit via backdoor Pharmacy

> DP Discontinued by provider through CPRS

> DC Discontinued via backdoor Pharmacy

> DD Discontinued due to death

> DA Auto discontinued due to admission

E Expired

> HP Placed on hold by provider through CPRS

> H Placed on hold via backdoor Pharmacy

N Non Verified

P Pending due to drug interactions

S Suspended

\$ Copay eligible

E Third-party electronically billable

R Returned to stock prescription (next to last fill date)

Example: Medication Profile – Short Format

Medication Profile Jun 12, 2006@22:33:13 Page: 1 of 1

OPPATIENT16, ONE

PID: 000-55-3421 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: DEC 2, 1923 (82) Wt(kg): 100.00 (06/24/2003)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Non-VA Meds on File

Last entry on 1-20-05

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

----------------REFILL TOO SOON/DUR REJECTS (Third Party)----------------------

1 2390\$e DIGOXIN (LANOXIN) 0.05MG CAP 90 A\> 02-16 02-16 3 90

2 2391e OXYBUTYNIN CHLORIDE 15MG SA TAB 180 S\> 02-15 05-06 0 90

-------------------------------------ACTIVE-------------------------------------

3 2396 AMPICILLIN 250MG CAP 40 A\> 06-12 06-12 0 10

4 2395 AZATHIOPRINE 50MG TAB 90 E 06-10 05-03 3 90

----------------------------------DISCONTINUED----------------------------------

5 2398 FOLIC ACID 1MG TAB 90 DD\> 05-03 05-03R 3 90

6 2400 HYDROCORTISONE 1%CR 1 DE\> 05-03 05-03R 11 30

7 2394 IBUPROFEN 400MG TAB 500'S 270 DC 05-03 05-03 3 90

8 2399 MVI CAP/TAB 90 DP\> 05-03 05-03R 3 90

9 2402 TEMPAZEPAM 15MG CAP 30 DF 06-01 06-01 5 30

10 2392 THIAMINE HCL 100MG TAB 90 DA\> 05-03 05-03R 3 90

--------------------------------------HOLD--------------------------------------

11 2393 WARFARIN 5MG TAB 90 H 05-03 - 3 90

12 2401 FUROSEMIDE 40MG TAB 90 HP 05-03 - 2 90

----------------------------------NON-VERIFIED---------------------------------

13 2397 BACLOFEN 10MG TABS 30 N 03-14 03-14 5 30

------------------------------------PENDING------------------------------------

14 CAPTOPRIL 25MG TAB QTY: 180 ISDT: 06-12 REF: 3

15 MULTIVITAMIN CAP/TAB QTY: 30 ISDT: 06-12\> REF: 3

------------------------NON-VA MEDS (Not dispensed by VA) ----------------------

GINKO EXT 1 TAB ONCE A DAY BY MOUTH Date Documented: 01/13/01

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

Order \#4 is highlighted (reverse video) to indicate that it has recently expired.

Orders \#5, 7, 10 are highlighted (reverse video) to indicate that they were recently discontinued.

Hold Type display codes are shown in blue.Discontinue Type display codes are shown in blue.

### OneVA Pharmacy and the Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Effective with the OneVA Pharmacy patch PSO\*7\*454 – December 2016, the Medication Profile displays all active medications from other facilities. The medications are retrieved from the Health Data Repository/Clinical Data Service (HDR/CDS) Repository and are displayed below the ‘local’ or ‘Non-VA Med’ orders and are sorted/grouped by facility. The prescriptions originating from other VA Pharmacy locations display under a divider header line showing the site name, site number, and status.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/013.png)Note: For additional information regarding OneVA Pharmacy processing go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – OneVA Pharmacy” document.

The example shown below displays three pages of a test patient’s Medication Profile, displaying the ‘local’ prescription orders followed by prescription orders that originated at other facilities.

<u>Medication Profile Jul 28, 2016@05:20:23 Page: 1 of 3</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 10000126 FLUTICAS 100/SALMETEROL 50 INHL DISK 60 E\> 06-01 02-02 11 45

Qty: 2

2 10000128 NIACIN 250MG TAB 270 S\> 06-08 08-27 2 90

3 10000122 RAMIPRIL 5MG CAP 30 A\> 05-31 05-31 8 30

----------------------------------DISCONTINUED----------------------------------

4 10000125 HYDROCHLOROTHIAZIDE 25MG TAB 60 DC\>02-01 02-02 5 60

--------------------------------------HOLD--------------------------------------

5 10000127 LISINOPRIL 2.5MG TAB 90 H\> 03-10 - 3 90

------------------------------DAYTON (552) ACTIVE-------------------------------

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen//

<u>Medication Profile Jul 28, 2016@05:20:46 Page: 2 of 3</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

<u>+</u>

6 2718399 IBUPROFEN 800MG TAB 30 A 06-09 07-19 0 10

7 2718383 OMEPRAZOLE 10MG SA CAP 30 A 02-02 06-10 11 30

8 2718397 VERAPAMIL HCL 120MG TAB 60 A 06-15 06-15 5 60

---------------------------DAYTON (552) DISCONTINUED----------------------------

9 2718398 ASPIRIN 325MG BUFFERED TAB 300 DC 03-15 03-15 2 90

-------------------------------DAYTON (552) HOLD--------------------------------

10 2718400 ALBUTEROL 0.5% INHL SOLN 2 H 06-09 - 1 14

-----------------------------DAYTON (552) SUSPENDED-----------------------------

11 2718401 CALCIUM GLUCONATE 500MG TAB 30 S 05-25 07-14 3 30

-------------------------DAYTSHR TEST LAB (984) ACTIVE--------------------------

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen//

<u>Medication Profile Jul 28, 2016@05:16:31 Page: 3 of 3</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

<u>+</u>

12 2718902 BANDAGE, GAUZE, ROLLER 2 IN X 6 YD 3 A 04-19 04-19 9 29

13 2718744 OMEPRAZOLE 10MG SA CAP 60 A 05-03 05-03 5 60

----------------------DAYTSHR TEST LAB (984) DISCONTINUED-----------------------

14 2718745 QUINAPRIL 20MG TAB 30 DC 03-04 03-04 11 30

-------------------------DAYTSHR TEST LAB (984) EXPIRED-------------------------

15 2718746 AMOXICILLIN 250MG CAP 30 E 06-01 05-04 0 10

--------------------------DAYTSHR TEST LAB (984) HOLD---------------------------

16 2718747 CETIRIZINE HCL 10MG TAB 45 H 04-23 - 4 45

------------------------DAYTSHR TEST LAB (984) SUSPENDED------------------------

17 2718748 TRAZODONE HCL 50MG TAB 90 S 04-05 06-24 2 90

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

The OneVA Pharmacy OneVA Pharmacy patch PSO\*7\*454 – December 2016 introduces the new view, ‘REMOTE OP Medications’, which displays the details of the remote prescription order. When selecting a OneVA Pharmacy prescription order from the Medication Profile screen, the new ‘REMOTE OP Medications’ page display as shown in the example below.

<u>REMOTE OP Medications (ACTIVE)Jul 27, 2016@10:12:37 Page: 1 of 1</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEFEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

Site \#: 984(DAYTSHR TEST LAB)

Rx \#: 2718862

Drug Name: IBUPROFEN 800MG TAB

Days Supply: 30

Quantity: 60

Refills: 11

Expiration Date: 06/01/17

Issue Date: 05/31/16

Stop Date: 06/01/17

Last Fill Date: 05/31/16

Sig: TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED --TAKE WITH

FOOD IF GI UPSET OCCURS/DO NOT CRUSH OR CHEW--

Enter ?? for more actions

RF Refill Rx from Another VA Pharmacy PR Partial

Select Action:Quit//

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/014.png)Note: For additional information regarding OneVA Pharmacy processing go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – OneVA Pharmacy” document.

## Medication Profile: Long Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The long format displays all information contained on the short format as well as the following additional fields:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>physician’s name</p></li>
</ul></th>
<th><ul>
<li><p>clerk code</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>fill date</p></li>
</ul></td>
<td><ul>
<li><p>total allowable refills</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>dates of refills/partial fills</p></li>
</ul></td>
<td><ul>
<li><p>which division filled it</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>whether the prescription was filled at the pharmacy window or by mail</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

The long report format of the fields for Non-VA Med orders include the start date, CPRS order \#, status, documented by, order check(s), override reason, override provider, and statement of explanation.

Example: Medication Profile – Long Format

Select PATIENT NAME: OPPATIENT,ONE 8-5-19 666000777 NO NSC

VETERAN OPPATIENT,ONE

WARNING : \*\* This patient has been flagged with a Bad Address Indicator.

LONG or SHORT: SHORT// LONG

Sort by DATE, CLASS or MEDICATION: DATE// \<Enter\>

All Medications or Selection (A/S): All// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]* GENERIC INCOMING TELNET

OPPATIENT,ONE ID#: 0777

(TEMP ADDRESS from AUG 28,2006 till (no end date))

LINE1 DOB: AUG 5,1919

ANYTOWN PHONE: 555-1212

TEXAS 77379 ELIG: NSC

CANNOT USE SAFETY CAPS.

WEIGHT(Kg): HEIGHT(cm):

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_

DISABILITIES:

ALLERGIES:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ADVERSE REACTIONS:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter RETURN to continue or '^' to exit: \<Enter\>

Outpatient prescriptions are discontinued 72 hours after admission

Medication Profile Sorted by ISSUE DATE

Rx \#: 100001968Ae Drug: LOPERAMIDE 2MG CAP

SIG: TAKE TWO CAPSULES BY MOUTH EVERY DAY

QTY: 60 \# of Refills: 5 Issue/Expr: 12-15-05/06-16-06

Prov: OPPROVIDER16,TWO Entry By: 10000000013 Filled: 01-14-06 (M)

Last Released: Original Release:

Refilled: 02-19-04 (M) Released:

Remarks:

Division: ALBANY (500) Active 4 Refills Left

Example: Medication Profile – Long Format (continued)

-------------------------------------------------------------------------------

Non-VA MEDS (Not Dispensed by VA)

GINKO BILLOBA TAB

Dosage: 1 TABLET

Schedule: ONCE A DAY

Route: MOUTH

Status: Discontinued (10/08/03)

Start Date: 09/03/03 CPRS Order \#: 12232

Documented By: OPCLERK21,FOUR on 09/03/03

Statement of Explanation: Non-VA medication not recommended by VA provider.

Example: Medication Profile – Long Format (continued)

ACETAMINPHEN 325MG CT

Dosage: 325MG

Schedule:

Route:

Status: Active

Start Date: 09/03/03 CPRS Order \#: 12234

Documented By: OPCLERK21,FOUR on 09/03/03

Statement of Explanation: Non-VA medication recommended by VA provider

Patient wants to buy from Non-VA pharmacy

The Intervention menu hidden action has been included in the Patient Information, the Medication Profile and Detailed Order ListMan screens when utilizing the following options:

- Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]
- Complete Orders from OERR \[PSO LMOE FINISH\]
- Edit Prescriptions \[PSO RXEDIT\]

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/015.png)

> **NOTE:** Patch PSO\*7\*391 added a new sort selection, 'CS' to the Complete Orders from OERR, enabling users to select digitally signed pending CS orders separately.

See “Using the Pharmacy Intervention Menu” for more details.

# Chapter 9: Processing a Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the option and processes used in processing prescriptions.

# Patient Prescription Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO LM BACKDOOR ORDERS\]

> ![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/016.png) If the order utilizes the <span id="p477_36_Except_note" class="anchor"></span>EXCEPT conjunction, copy, renew, and reinstate will no longer be allowed.

The *Patient Prescription Processing* option is used to process outpatient medication orders from OERR V. 3.0. This option uses List Manager features that allow the pharmacy technician to perform the following actions on a prescription without leaving this option.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Enter a new Rx</p></li>
</ul></th>
<th><ul>
<li><p>Release</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Refill</p></li>
</ul></td>
<td><ul>
<li><p>Order a partial</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Copy (new)</p></li>
</ul></td>
<td><ul>
<li><p>Pull early from suspense</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Renew</p></li>
</ul></td>
<td><ul>
<li><p>Show a profile</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Reprint</p></li>
</ul></td>
<td><ul>
<li><p>View activity log (new)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="PSO_LM_BACKDOOR" class="anchor"></span>Patient demographics and Clinical Alerts display in the header area when using this option. Refer to [Patient Demographics and Clinical Alerts](#patient-demographics-and-clinical-alerts) for more information.

When a new drug order is processed (new, renewal, finish, verify, copy, or an edit that creates a new order), order checks are performed. These include checking for duplicate drug, duplicate drug therapy, drug-drug interaction, drug allergy, and maximum single dose.

Outpatient Pharmacy generated order checks are displayed in this sequence:

- System Errors
- Duplicate Drug
- Clozapine
- Allergy/ADR (local & remote) or Non-Assessment
- CPRS checks generated backdoor (3 new checks)
- Drug Level Errors
- Local & Remote Critical Drug Interactions
- Local & Remote Significant Drug Interactions
- Local & Remote Duplicate Therapy
- Maximum Single Dose

Additionally, the order check display sequence is applied to the following processes:

- Backdoor new order entry
- Finishing a pending order
- Renewing an outpatient medication order
- Creating a new order when editing an outpatient medication order
- Verifying an outpatient medication order
- Copying an outpatient medication order
- Reinstating a discontinued outpatient medication order

There are three levels of error messages associated with Enhanced Order Checking (Drug Interactions, Duplicate Therapy, and Dosing):

1.  System - When a system level error occurs, no Drug Interaction, Duplicate Therapy, or Dosing order checks that utilize the COTS database (FDB) will be performed. Other order checks, such as Allergy/ADRs, Duplicate Drug (for outpatient only), and the new CPRS order checks, etc. that are performed entirely within VISTA will continue to be executed.
2.  Drug - When a drug level error occurs, no Drug Interaction, Duplicate Therapy, or Dosing order checks will be performed for a specific drug. Drug level errors can occur for the prospective drug (drug being processed) or the profile drug. If a drug level error occurs on the prospective drug, no profile drug errors will be displayed. The only exception to this is when you are processing an IV order with multiple prospective drugs (i.e. multiple IV Additives). Profile drug level errors will only be shown once per patient session.

There are two reasons that a drug level error is generated; the drug is not matched to NDF or the drug is matched to NDF, but the VA Product to which it is matched does not have a GCNSEQNO assigned or the GCNSEQNO assigned does not match up to the GCNSEQNO in the COTS database. The latter (GCNSEQNO mismatch) is rare.

3.  Order - The third error level is for the order. Order level errors will only occur with dosing order checks. Please see the Dosing Order Check User Manual for more information.

See table below for an explanation of the errors:

| Error Level | Error Message                                                                                                                         | Reason                                               | Why message is being displayed.                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System          | No Enhanced Order Checks can be performed.                                                                                                | Vendor Database cannot be reached.                       | The connectivity to the vendor database has gone down. A MailMan message is sent to the G. PSS ORDER CHECKS mail group when the link goes down and when it comes back up.                                                                                                               |
| System          | No Enhanced Order Checks can be performed.                                                                                                | The connection to the vendor database has been disabled. | A user has executed the Enable/Disable Vendor Database Link \[PSS ENABLE/DISABLE DB LINK\] option and disabled the interface.                                                                                                                                                           |
| System          | No Enhanced Order Checks can be performed                                                                                                 | Vendor database updates are being processed              | The vendor database (custom and standard data) is being updated using the DATUP (Data Update) process.                                                                                                                                                                                  |
| System          | No Dosing Order Checks can be performed                                                                                                   | Dosing Order Checks are disabled                         | A user has executed the *Enable/Disable Dosing Order Checks* \[PSS Dosing Order Checks\] option.                                                                                                                                                                                        |
| Drug            | Enhanced Order Checks cannot be performed for Local or Remote Outpatient Drug: \<DRUG NAME\>                                              | Drug not matched to NDF                                  | The local drug being ordered/ or on profile has not been matched to NDF. Matching the drug to a VA Product will eliminate this message.                                                                                                                                                 |
| Drug            | Order Checks could not be done for RemoteDrug: \<DRUG NAME\>, please complete a manual check for Drug Interactions and Duplicate Therapy. |                                                          | If this error message is displayed, it means that the VA product that the local or remote drug being ordered/or on local or remote profile does not have a GCNSEQNO or in rare cases, the GCNSEQNO assigned to the VA Product does not match up with a GCNSEQNO in the vendor database. |
| Drug            | Enhanced Order Checks cannot be performed for Orderable Item: \<OI NAME\>                                                                 | No active Dispense Drug found                            | Highly unlikely that this error would be seen. At the time the order check was being performed the orderable item did not have an active dispense drug associated.                                                                                                                      |

See examples below to illustrate error sequences:

New Order Entry – System Level Error

Select Action: Quit// NO New Order

Eligibility: SC LESS THAN 50% SC%: 40

RX PATIENT STATUS: SC LESS THAN 50%//

DRUG: AMLOD

Lookup: GENERIC NAME

1 AMLODIPINE 10MG/BENAZAPRIL 20MG TAB CV400

2 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB CV200

CHOOSE 1-2: 1 AMLODIPINE 10MG/BENAZAPRIL 20MG TAB CV400

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

No Enhanced Order Checks can be performed.

Reason: Vendor database cannot be reached.

Press Return to Continue...

There are 2 Available Dosage(s):

1 TABLET

2 TABLETS

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 1 TABLET

You entered 1 TABLET is this correct? Yes// YES

VERB: TAKE

ROUTE: PO//

1 PO ORAL (BY MOUTH) PO

2 PO ORAL PO

CHOOSE 1-2: 1 ORAL (BY MOUTH) PO MOUTH

Schedule: Q4H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q4H Q4H EVERY 4 HOURS

...OK? Yes// (Yes)

(EVERY 4 HOURS LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Drug Error Message – Finishing Pending Outpatient Order

\+ Enter ?? for more actions

BY Bypass DC Discontinue

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

Enhanced Order Checks cannot be performed for Local Drug: WARFARIN 5MG TAB

Reason: Drug not matched to NDF

Press Return to Continue...

Was treatment for Service Connected condition? YES//

Are you sure you want to Accept this Order? NO//

Renewing an Order – Therapeutic Duplication – Drug Level Error

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// rn Renew

FILL DATE: (3/12/2008 - 3/13/2009): TODAY// (MAR 12, 2008)

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Now Renewing Rx \# 2580 Drug: SUCRALFATE 1GM TAB

Press Return to Continue...

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait…

-------------------------------------------------------------------------------

Order Checks could not be done for Drug: RANITIDINE 150MG TAB, please complete a manual check for Drug Interactions and Duplicate Therapy.

====================================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* SUCRALFATE 1GM TAB with

Local Rx#: 2574

Drug: CIMETIDINE 300MG TAB (DISCONTINUED)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Processing Status: Released locally on 03/07/08@08:55:32 (Window)

Last Filled On: 11/08/06

Local Rx#: 2573

Drug: NIZATIDINE 150MG CAP (ACTIVE)

SIG: TAKE ONE CAPSULE BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Processing Status: Released locally on 03/07/08@08:55:32 (Window)

Last Filled On: 11/08/06

Local Rx#: 2599

Drug: FAMOTIDINE 20MG TAB (PROVIDER HOLD)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Processing Status: Released locally on 03/07/08@08:55:32 (Window)

Last Filled On: 11/08/06

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists

====================================================================================

Discontinue RX \#2573 NIZATIDINE 150MG CAP? Y/N No

Press Return to Continue:

2580A SUCRALFATE 1GM TAB QTY: 360

\# OF REFILLS: 3 ISSUED: 03-12-08

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY

FILLED: 03-12-08

ROUTING: WINDOW PHYS: PSOPROVIDER,ONE

Edit renewed Rx ? Y// n NO

SC Percent: 80%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO//

### Hazardous Medication Warnings - Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following events will check if a medication is Hazardous per the National Drug files and display an alert to remind the clinician to follow appropriate procedures.

- New Order (NO)
- Finish (FN) a Pending Order
- Renew (RN) an Order

Example Hazardous Medication Warning - New Order (NO) Entry:

> \+ Enter ?? for more actions

> PU Patient Record Update NO New Order

> PI Patient Information SO Select Order

> Select Action: Next Screen// NO New Order

> Eligibility: SC%:

> RX PATIENT STATUS: SC//

> DRUG: NIZATIDINE

> Lookup: VA PRODUCT NAME

> NIZATIDINE 150MG CAP TEST DRUG IV GA301 TESTING CURRENT INVENTO

> RY

> ...OK? Yes// (Yes)

> --------------------------------------------------------------------------------

> \*\*\*\*\* WARNING \*\*\*\*\*

> NIZATIDINE is hazardous to dispose. Please notify pharmacy staff

> and counsel patient to take the appropriate disposal precautions.

> --------------------------------------------------------------------------------

> Press Return to continue:

> Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

> Now Processing Enhanced Order Checks! Please wait...

Example Hazardous Medication Warning - Finishing (FN) Pending Order:

> <u>Pending OP Orders (ROUTINE) Apr 29, 2021@12:59:35 Page: 1 of 3</u>

> OUTPATIENT,ONE

> PID: 000-22-1234 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

> DOB: MAY 5,1988 (32) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

> SEX: MALE

> CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

> CPRS Order Checks:

> Patient has no allergy assessment.

> Overriding Provider: PROVIDER,OUTPATIENT

> \*(1) Orderable Item: WARFARIN TAB \<DIN\>

> \(2\) Drug: WARFARIN 2MG TABS \<DIN\>

> \(3\) \*Dosage: 2 (MG)

> Verb: TAKE

> Dispense Units: 1

> Noun: TABLET

> \*Route: ORAL (BY MOUTH)

> \*Schedule: HS

> \+ Enter ?? for more actions

> BY Bypass DC Discontinue FL Flag/Unflag

> ED Edit FN Finish

> Select Item(s): Next Screen// FN Finish

> --------------------------------------------------------------------------------

> \*\*\*\*\* WARNING \*\*\*\*\*

> WARFARIN is hazardous to handle and dispose. Please notify

> pharmacy staff and counsel patient to take the appropriate handling and

> disposal precautions.

> --------------------------------------------------------------------------------

> Press Return to continue:

> Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

> Now Processing Enhanced Order Checks! Please wait...

Example Hazardous Medication Warning - Renewing (RN) an Order:

> <u>OP Medications (SUSPENDED) Apr 29, 2021@13:07:19 Page: 1 of 3</u>

> OUTPATIENT,TWO

> PID: 111-22-1234 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

> DOB: MAY 1,1989 (31) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

> SEX: FEMALE

> CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

> Rx \#: 300503

> \(1\) \*Orderable Item: SPIRONOLACTONE TAB

> \(2\) Drug: SPIRONOLACTONE 25MG S.T. \<DIN\>

> NDC: 00005-3782-31

> \(3\) \*Dosage: 25 (MG)

> Verb: TAKE

> Dispense Units: 1

> Noun: TABLET

> \*Route: ORAL (BY MOUTH)

> \*Schedule: BID

> \*Duration: 3D (DAYS)

> (4)Pat Instructions:

> \+ Enter ?? for more actions

> DC Discontinue PR Partial RL Release

> ED Edit RF (Refill) RN Renew

> Select Action: Next Screen// RN Renew

> FILL DATE: (APR 29, 2021-APR 30, 2022): TODAY// (APR 29, 2021)

> MAIL/WINDOW: WINDOW// WINDOW

> METHOD OF PICK-UP:

> Nature of Order: WRITTEN// W

> WAS THE PATIENT COUNSELED: NO// NO

> Do you want to enter a Progress Note? No// NO

> Now Renewing Rx \# 300503 Drug: SPIRONOLACTONE 25MG S.T.

> --------------------------------------------------------------------------------

> \*\*\*\*\* WARNING \*\*\*\*\*

> SPIRONOLACTONE is hazardous to handle. Please notify pharmacy

> staff and counsel patient to take the appropriate handling

> precautions.

> --------------------------------------------------------------------------------

> Press Return to continue:

> Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

> Now Processing Enhanced Order Checks! Please wait...

### Allergy Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the display of Allergy Order Checks functionality that appear prior to Clinical Reminder Order Checks (CROCs) and Enhanced Order Checks.

The following changes have been made to the existing allergy order checks:

1.  In Backdoor Pharmacy, the system will require the pharmacist to complete an Intervention if the severity value equals ‘Severe’ before allowing the pharmacist to continue with the order.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/017.png)Note: Severity for an allergy can ONLY be entered for (O)bserved and NOT (H)istorical Allergy/Adverse Reactions and the user MUST HOLD the GMRA-ALLERGY VERIFY key and complete an observed reaction report to enter MECHANISM and SEVERITY for Observed types of Allergy/Adverse Reactions.

> Clerk Does Not Get Intervention Prompt:

> Observed:

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

A Drug-Allergy Reaction exists for this medication and/or class!

Prospective Drug: NITROGLYCERIN 0.3MG S.L.T.

Causative Agent: NITROGLYCERIN (ALBANY - 01/21/16)

Historical/Observed: OBSERVED

Severity: SEVERE

Signs/Symptoms: NAUSEA,VOMITING

Drug Class: CV250 ANTIANGINALS

Provider Override Reason: N/A - Order Check Not Evaluated by Provider

Press Return to continue:

Now processing Clinical Reminder Order Checks. Please wait ...

> Historical:

> Now doing allergy checks.  Please wait...   

> A Drug-Allergy Reaction exists for this medication and/or class! 

>     Prospective Drug: AMPICILLIN 250MG   
>      Causative Agent: AMPICILLIN (ALBANY - 01/14/16)   
>  Historical/Observed: HISTORICAL   
>             Severity: Not Entered   
>          Ingredients: AMPICILLIN   
>       Signs/Symptoms: DRY MOUTH, HIVES   
>           Drug Class: AM111 PENICILLINS,AMINO DERIVATIVES 

Press Return to continue:

Now processing Clinical Reminder Order Checks. Please wait ...

2.  Allergies that are mild or moderate are still captured and stored by order number in the ORDER CHECK INSTANCES file (#100.05), regardless of whether or not an intervention was entered. The information can be viewed from the prescription screen using the hidden action – DA Display Drug Allergies

    CPRS Allergy Entry Process

From the Order tab, enter a new allergy using the Allergies Dialog:

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/018.png)

Example of Historical Allergy:

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/019.png)

Example of Observed Allergy:

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/020.png)

### OneVA Pharmacy Processing within Patient Prescription Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/021.png)Note: For information regarding OneVA Pharmacy processing go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – OneVA Pharmacy” document.

OneVA Pharmacy patch PSO\*7\*454 introduces new messaging to query the Health Data Repository/Clinical Data Services (HDR/CDS) Repository for prescriptions from other VA Pharmacy locations and displays them in the Medications Profile view. The new query will only execute if the patient has been treated at more than one VA Medical Center. The query retrieves all prescriptions associated with the patient from the repository, which requires additional time. To execute the HDR/CDS Repository query, the user must accept the default of ‘YES’ to the ‘Would you like to query prescriptions from other OneVA Pharmacy locations?’ prompt. When the user responds ‘YES’ or accepts the default to the OneVA Pharmacy prompt, the system displays the OneVA Pharmacy Query Message.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/022.png)The OneVA Pharmacy’s feature to query the HDR/CDS Repository will not execute if the patient has only one entry in the ‘TREATING FACILITY LIST file (#391.91)’.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/023.png)The system identifies and queries the HDR/CDS Repository for all the prescriptions that are active, suspended, on hold, expired (within 120 days), or discontinued (within 120 days).

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/024.png) <span id="PSO_532_OneVAPharmPatRxProcess" class="anchor"></span>If the query connection to the HDR/CDS Repository fails, a message will display stating ‘The system is down or not responding (Connection Failed). Could not query prescriptions at other VA Pharmacy locations. Press RETURN to continue:’ The user should press return to continue and contact local support if this problem persists.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/025.png)When the system is down message displays, the VistA session will continue to display the local/dispensing sites prescriptions on the Medication Profile view. There will be no indication if a patient is registered or has prescriptions on other sites (i.e., remote site/OneVA Pharmacy prescriptions will not display on the Medication Profile view.)

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/026.png)If the patient does not have any prescription records from other VA Pharmacy locations, matching the search criteria, a message will display stating the “Patient found with no prescription records matching search criteria.”

Example: OneVA Pharmacy Processing

Select PATIENT NAME: PSOPATIENT,SIX 2-13-61 666012136 NO

NSC VETERAN

No Patient Warnings on file for PSOPATIENT,SIX.

Press RETURN to continue...

PSOPATIENT,SIX (666-01-2136)

No Allergy Assessment!

Press Return to continue:

Would you like to query prescriptions from other OneVA Pharmacy

locations? YES//

Please wait. Checking for prescriptions at other VA Pharmacy locations. This may

take a moment...

REMOTE PRESCRIPTIONS AVAILABLE!

Display Remote Data? N// O

Eligibility:

RX PATIENT STATUS: OUTPT NON-SC//

OneVA Pharmacy Refill Example<u>Medication Profile Jul 27, 2016@10:11:28 Page: 1 of 1</u>PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)SEX: FEMALECrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_ISSUE LAST REF DAY\# RX \# DRUG QTY ST DATE FILL REM SUP\<No local prescriptions found.\>-------------------------DAYTSHR TEST LAB (984) ACTIVE--------------------------1 2718861 CETIRIZINE HCL 10MG TAB 30 A 05-21 07-07 7 302 2718863 HYDRALAZINE HCL 25MG TAB 60 A 05-11 05-11 5 603 2718862 IBUPROFEN 800MG TAB 60 A 05-31 05-31 11 30Enter ?? for more actionsPU Patient Record Update NO New OrderPI Patient Information SO Select OrderSelect Action: Quit//Select Action: Quit// SO Select OrderSelect Orders by number: (1-3): 3<u>REMOTE OP Medications (ACTIVE)Jul 27, 2016@10:12:37 Page: 1 of 1</u>PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)SEX: FEMALECrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_Site \#: 984(DAYTSHR TEST LAB)Rx \#: 2718862Drug Name: IBUPROFEN 800MG TABDays Supply: 30Quantity: 60Refills: 11Expiration Date: 06/01/17Issue Date: 05/31/16Stop Date: 06/01/17Last Fill Date: 05/31/16Sig: TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED --TAKE WITHFOOD IF GI UPSET OCCURS/DO NOT CRUSH OR CHEW--Enter ?? for more actionsRF Refill Rx from Another VA Pharmacy PR PartialSelect Action:Quit//Select Action:Quit// RFSelect Action:Quit// RF Refill Rx from Another VA PharmacyRemote site drug name: IBUPROFEN 800MG TABMatching Drug Found for Dispensing: IBUPROFEN 800MG TABWould you like to use the system matched drug for thisrefill/partial fill? NO//refill/partial fill? NO// YESProcessing refill request. Please be patient as it may take a momentfor the host site to respond and generate your label data...MESSAGE SENT TO TARGET VISTA; TIMED OUT AWAITING REPLYPress RETURN to continue:Processing refill request. Please be patient as it may take a momentfor the host site to respond and generate your label data...Select LABEL DEVICE:Select LABEL DEVICE: 0 DEC WindowsVAMC DAYTON, OH 45428-0415 VAMC DAYTON, OH 45428-0415 (REPRINT)984 937-267-5325 (35783/ ) 984 937-267-5325 (35783/ ) 984 (35783/ ) JUL 27,2016@10:14:57Rx# 2718862 JUL 27,2016 Fill 2 of 12 Rx# 2718862 JUL 27,2016Fill 2 of 12 Rx# 2718862 JUL 27,2016 Fill 2 of 12PSOPATIENT,SIX PSOPATIENT,SIXPSOPATIENT,SIXTAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED--TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOTCRUSH OR CHEW-- CRUSH OR CHEW--CRUSH OR CHEW--GUIGLIA,MARY C GUIGLIA,MARY CGUIGLIA,MARY CQty: 60 TAB Qty: 60 TABQty: 60 TABIBUPROFEN 800MG TAB IBUPROFEN 800MG TABIBUPROFEN 800MG TAB10 Refills remain prior toJUN 1,2017 Mfg \_\_\_\_\_\_\_\_ Lot# \_\_\_\_\_\_\_\_PO BOX 415 COPAY Days Supply: 30Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_DAYTON, OH 45428-0415ADDRESS SERVICE REQUESTEDRead FDA Med Guide\*\*\*DO NOT MAIL\*\*\* ,Routing: WINDOWDays supply: 30 Cap: SAFETYIsd: MAY 31,2016 Exp: JUN 1,2017PSOPATIENT,SIX \*Indicate address change on back of this form Last Fill: 05/31/2016\[ \] PermanentPat. Stat ONSC Clinic: CINCI\[ \] Temporary until \_\_/\_\_/\_\_ DRUG WARNING 8,10,19Signature\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_PSOPATIENT,SIXPSOPATIENT,SIXRx# 2718862IBUPROFEN 800MG TABVerified AllergiesDRUG WARNING:------------------DO NOT DRINK ALCOHOLIC BEVERAGESwhen taking this medication. Non-Verified AllergiesTAKE WITH FOOD OR MILK.----------------------This is the same medication youhave been getting. Color,size Verified Adverse Reactionsor shape may appear different. --------------------------Non-Verified Adverse Reactions------------------------------PSOPATIENT,SIX JUL 27,2016Pharmacy Service (119)DAYTONP.O. BOX 415DAYTON, OH 45428-0415Use the label above to mail the computercopies back to us. Apply enough postageto your envelope to ensure delivery.The VA Notice of Privacy Practices, IB 10-163, which outlines your privacyrights, is available online at http://www1.va.gov/Health/ or you may obtaina copy by writing the VHA Privacy Office (19F2), 810 Vermont Avenue NW,Washington, DC 20420.Rx \# 2718862 refilled.Press RETURN to continue:Updating prescription order list...OneVA Pharmacy Partial Example<u>Medication Profile Jul 27, 2016@10:26:23 Page: 1 of 1</u>PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)SEX: FEMALECrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_ISSUE LAST REF DAY\# RX \# DRUG QTY ST DATE FILL REM SUP\<No local prescriptions found.\>-------------------------DAYTSHR TEST LAB (984) ACTIVE--------------------------1 2718861 CETIRIZINE HCL 10MG TAB 30 A 05-21 07-07 7 302 2718863 HYDRALAZINE HCL 25MG TAB 60 A 05-11 05-11 5 603 2718862 IBUPROFEN 800MG TAB 60 A 05-31 07-27 10 30Enter ?? for more actionsPU Patient Record Update NO New OrderPI Patient Information SO Select OrderSelect Action: Quit//Select Action:Quit// PR PartialRemote site drug name: CETIRIZINE HCL 10MG TABMatching Drug Found for Dispensing: CETIRIZINE HCL 10MG TABWould you like to use the system matched drug for thisrefill/partial fill? NO// YESEnter Quantity: 10DAYS SUPPLY: 10Select PHARMACIST Name: COPE,THOMAS J// TJC 192 BAY PINES TEST LABREMARKS: last refill lostProcessing partial fill request. Please be patient as it may take a momentfor the host site to respond and generate your label data...Select LABEL DEVICE:Select LABEL DEVICE: 0 DEC WindowsVAMC DAYTON, OH 45428-0415 VAMC DAYTON, OH 45428-0415 (REPRINT)(PARTIAL)984 937-267-5325 (35783/ ) 984 937-267-5325 (35783/ ) 984 (35783/ ) JUL 27,2016@10:29:20Rx# 2718861 JUL 27,2016 Fill 2 of 9 Rx# 2718861 JUL 27,2016Fill 2 of 9 Rx# 2718861 JUL 27,2016 Fill 2 of 9PSOPATIENT,SIX PSOPATIENT,SIXPSOPATIENT,SIXTAKE ONE TABLET BY MOUTH DAILY TAKE ONE TABLET BY MOUTH DAILY TAKE ONE TABLET BY MOUTH DAILYGUIGLIA,MARY C GUIGLIA,MARY CGUIGLIA,MARY CQty: 10 TAB Qty: 10 TABQty: 10 TABCETIRIZINE HCL 10MG TAB CETIRIZINE HCL 10MG TABCETIRIZINE HCL 10MG TAB7 Refills remain prior toMAY 22,2017 Mfg \_\_\_\_\_\_\_\_ Lot# \_\_\_\_\_\_\_\_PO BOX 415 Days Supply: 10Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_DAYTON, OH 45428-0415ADDRESS SERVICE REQUESTED\*\*\*DO NOT MAIL\*\*\* ,Routing: WINDOWDays supply: 10 Cap: SAFETYIsd: MAY 21,2016 Exp: MAY 22,2017PSOPATIENT,SIX \*Indicate address change on back of this form Last Fill: 05/23/2016\[ \] PermanentPat. Stat ONSC Clinic: CINCI\[ \] Temporary until \_\_/\_\_/\_\_ DRUG WARNING 1,8Signature\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_PSOPATIENT,SIXPSOPATIENT,SIXRx# 2718861CETIRIZINE HCL 10MG TABVerified AllergiesDRUG WARNING:-------------------MAY CAUSE DROWSINESS-Alcohol may intensify thiseffect. Non-Verified AllergiesUSE CARE when driving or----------------------when operating dangerous machinery.DO NOT DRINK ALCOHOLIC BEVERAGES Verified Adverse Reactionswhen taking this medication. --------------------------Non-Verified Adverse Reactions------------------------------PSOPATIENT,SIX JUL 27,2016Pharmacy Service (119)DAYTONP.O. BOX 415DAYTON, OH 45428-0415Use the label above to mail the computercopies back to us. Apply enough postageto your envelope to ensure delivery.The VA Notice of Privacy Practices, IB 10-163, which outlines your privacyrights, is available online at http://www1.va.gov/Health/ or you may obtaina copy by writing the VHA Privacy Office (19F2), 810 Vermont Avenue NW,Washington, DC 20420.Partial complete for RX \#2718861.Press RETURN to continue:Updating prescription order list...<u>Medication Profile Jul 27, 2016@10:31:11 Page: 1 of 1</u>PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)SEX: FEMALECrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_ISSUE LAST REF DAY\# RX \# DRUG QTY ST DATE FILL REM SUP\<No local prescriptions found.\>-------------------------DAYTSHR TEST LAB (984) ACTIVE--------------------------1 2718861 CETIRIZINE HCL 10MG TAB 30 A 05-21 07-07 7 302 2718863 HYDRALAZINE HCL 25MG TAB 60 A 05-11 05-11 5 603 2718862 IBUPROFEN 800MG TAB 60 A 05-31 07-27 10 30Enter ?? for more actionsPU Patient Record Update NO New OrderPI Patient Information SO Select OrderSelect Action: Quit//<u>Medication Profile Jul 28, 2016@05:20:23 Page: 1 of 3</u>PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>PID: 666-01-2136 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)SEX: FEMALECrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_ISSUE LAST REF DAY\# RX \# DRUG QTY ST DATE FILL REM SUP-------------------------------------ACTIVE-------------------------------------1 10000126 FLUTICAS 100/SALMETEROL 50 INHL DISK 60 E\> 06-01 02-02 11 45Qty: 22 10000128 NIACIN 250MG TAB 270 S\> 06-08 08-27 2 903 10000122 RAMIPRIL 5MG CAP 30 A\> 05-31 05-31 8 30----------------------------------DISCONTINUED----------------------------------4 10000125 HYDROCHLOROTHIAZIDE 25MG TAB 60 DC\>02-01 02-02 5 60--------------------------------------HOLD--------------------------------------5 10000127 LISINOPRIL 2.5MG TAB 90 H\> 03-10 - 3 90------------------------------DAYTON (552) ACTIVE-------------------------------+ Enter ?? for more actionsPU Patient Record Update NO New OrderPI Patient Information SO Select Order

One Va Pharmacy patch PSO\*7\*479 modifies routine PSORRX2 to add the following text if no error message is returned when retrieving the label information from the host system. The following text is displayed just prior to the Label Device: ‘ prompt:

For a refill:

TRANSACTION SUCCESSFUL... The refill for RX \#763002 has been recorded on

the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE:

For a partial fill:

TRANSACTION SUCCESSFUL... The partial for RX \#763002 has been recorded on

the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE:

# # Outpatient Allergy Order Entry Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Observed Allergy Example

<u>Patient Information Jan 20, 2016@16:50:39 Page: 2 of 2</u>

ROWPATNM,BOAT \<A\>

PID: 666-00-0363 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAR 4,1950 (65) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2):

<u>+</u>

Non-Verified: PENICILLIN,

Remote:

Adverse Reactions

Verified: ASPIRIN,

Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Quit// EA Enter/Edit Allergy/ADR Data

OBS/

REACTANT VER. MECH. HIST TYPE

-------- ---- ------- ---- ----

PENICILLIN NO UNKNOWN OBS DRUG

Reactions: RASH

ASPIRIN YES PHARM OBS DRUG

Reactions: ANXIETY FOOD

CHOCOLATE AUTO UNKNOWN HIST DRUG

(FLAVOR) FOOD

Reactions: ANXIETY

Enter Causative Agent: GENTAMICIN

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

1 GENTAMICIN

2 GENTAMICIN/PREDNISOLONE

3 GENTAMICIN/SODIUM CHLORIDE

CHOOSE 1-3: 1 GENTAMICIN

GENTAMICIN OK? Yes// (Yes)

(O)bserved or (H)istorical Allergy/Adverse Reaction: O OBSERVED

Select date reaction was OBSERVED (Time Optional): T-15 (JAN 05, 2016) JAN 0

5, 2016 (JAN 05, 2016)

Are you adding 'JAN 05, 2016' as

a new ADVERSE REACTION REPORTING? No// Y (Yes)

No signs/symptoms have been specified. Please add some now.

The following are the top ten most common signs/symptoms:

1\. ANXIETY 7. HIVES

2\. ITCHING,WATERING EYES 8. DRY MOUTH

3\. ANOREXIA 9. DRY NOSE

4\. DROWSINESS 10. RASH

5\. NAUSEA,VOMITING 11. OTHER SIGN/SYMPTOM

6\. DIARRHEA

Enter from the list above : 7,10

Date(Time Optional) of appearance of Sign/Symptom(s): Jan 05, 2016// (JAN 05, 2

016\)

The following is the list of reported signs/symptoms for this reaction:

Signs/Symptoms Date Observed

---------------------------------------------------------------------------

1 HIVES Jan 05, 2016

2 RASH Jan 05, 2016

Select Action (A)DD, (D)ELETE OR \<RET\>:

COMMENTS:

No existing text

Edit? NO//

Enter another Causative Agent? YES// NO

Causative Agent Data edited this Session:

ADVERSE REACTION

----------------

GENTAMICIN

Obs/Hist: OBSERVED

Obs d/t: Jan 05, 2016

Signs/Symptoms: HIVES (1/5/16)

RASH (1/5/16)

Is this correct? NO// YES

This session you have CHOSEN:

GENTAMICIN

Historical Allergy entry

<u>Patient Information Jan 20, 2016@17:02:40 Page: 1 of 2</u>

OPHEPPAT,ONE \<A\>

PID: 666-03-1990 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAR 19,1990 (25) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE Non-VA Meds on File - Last entry on 08/04/15

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Eligibility:

RX PATIENT STATUS: OTHER FEDERAL

Disabilities:

HOME PHONE:

CELL PHONE:

WORK PHONE:

Prescription Mail Delivery: Regular Mail

Allergies

Verified: METFORMIN, PENICILLIN, ASPIRIN,

\+ Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Next Screen// ea Enter/Edit Allergy/ADR Data

OBS/

REACTANT VER. MECH. HIST TYPE

-------- ---- ------- ---- ----

METFORMIN AUTO ALLERGY OBS DRUG

(METFORMIN HYDROCHLORIDE)

Reactions: ANXIETY, HIVES, ITCHING,WATERING EYES

OXYCODONE NO ALLERGY OBS DRUG

Reactions: COMA, SHORTNESS OF BREATH

PENICILLIN AUTO ALLERGY OBS DRUG

Reactions: ANAPHYLAXIS, RASH, NAUSEA,VOMITING,

BELCHING

ASPIRIN AUTO ALLERGY OBS DRUG

Reactions: DIARRHEA, NAUSEA,VOMITING, HIVES FOOD

Enter Causative Agent: Gentamicin

Checking existing PATIENT ALLERGIES (#120.8) file for matches...

Now checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

1 GENTAMICIN

2 GENTAMICIN/PREDNISOLONE

3 GENTAMICIN/SODIUM CHLORIDE

CHOOSE 1-3: 1 GENTAMICIN

GENTAMICIN OK? Yes// (Yes)

(O)bserved or (H)istorical Allergy/Adverse Reaction: h HISTORICAL

No signs/symptoms have been specified. Please add some now.

The following are the top ten most common signs/symptoms:

1\. ANXIETY 7. HIVES

2\. ITCHING,WATERING EYES 8. DRY MOUTH

3\. ANOREXIA 9. DRY NOSE

4\. DROWSINESS 10. RASH

5\. NAUSEA,VOMITING 11. OTHER SIGN/SYMPTOM

6\. DIARRHEA

Enter from the list above : 7,10

Date(Time Optional) of appearance of Sign/Symptom(s): t (JAN 20, 2016)

The following is the list of reported signs/symptoms for this reaction:

Signs/Symptoms Date Observed

---------------------------------------------------------------------------

1 HIVES Jan 20, 2016

2 RASH Jan 20, 2016

Select Action (A)DD, (D)ELETE OR \<RET\>:

COMMENTS:

No existing text

Edit? NO//

Enter another Causative Agent? YES// n NO

Causative Agent Data edited this Session:

ADVERSE REACTION

----------------

GENTAMICIN

Obs/Hist: HISTORICAL

Signs/Symptoms: HIVES (1/20/16)

RASH (1/20/16)

Is this correct? NO// y YES

This session you have CHOSEN:

GENTAMICIN

### Clinical Reminder Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Clinical Reminder Order Checks and functionality brought in with patch PSO\*7\*411.

Order Checks now includes the ability to view Clinical Reminders (prior to the display of Enhanced Drug-Drug interactions). Reminders are used to aid physicians in performing tasks to fulfill Clinical Practice Guidelines and periodic procedures or education as needed for Veteran patients.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/027.png)

> **NOTE:** Technicians do not get prompted for interventions.

Severe Clinical Reminder Example

Now processing Clinical Reminder Order Checks. Please wait ...

==============================================================

\*\*\* Clinical Reminder Order Check \| Severity: HIGH \*\*\*

Potentially Teratogenic Medication (FDA Category D or C)

Concern has been raised about use of this medication during pregnancy.

1\) Pregnancy status should be determined. Discuss use of this medication on the

context of risks to the mother and child of untreated disease. Potential

benefits may warrant use of the drug in pregnant women despite risks.

2\) The patient must be provided contraceptive counseling on potential risk vs.

benefit of taking this medication if she were to become pregnant.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The 'Teratogenic Medications' Order Check will display for female patients

between the ages of 12 and 50, except those with a known exclusion criterion

(e.g., hysterectomy), or those with a documented IUD placement that is more

recent than a documented IUD removal.

--------------------------------------------------------------

Do you want to Continue? Y// ES

Medium Severity Clinical Reminder Example

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

This patient has received NSAID/Cox II for at least 365 days. A Creatinine level

Is recommended at this time to safely monitor NSAID/Cox II Therapy.

--------------------------------------------------------------

Do you want to Continue? Y//

### Enhanced Drug-Drug Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the enhanced Outpatient Pharmacy application Drug-Drug interaction functionality (PSO\*7\*251).

Legacy VistA drug-drug interactions have been enhanced to utilize First DataBank (FDB) MedKnowledge Framework business rules, Application Programming Interfaces (APIs) and database to provide more clinically relevant drug interaction information. VistA severity levels of ‘critical’ and ‘significant’ will continue to be used. No changes have been made to the existing user actions for critical or significant drug interactions. The pharmacist will have to log an intervention for local, pending and remote critical interactions and have the option of logging an intervention for local and remote significant interactions. No action is required for Non-VA medications orders.

See examples:

Drug interaction warning message for a local outpatient order:

Critical Drug Interaction with Local Rx

\*\*\*CRITICAL\*\*\* Drug Interaction with Prospective Drug:

INDINAVIR 400MG CAP and

Local Rx#: 2443

Drug: AMIODARONE 200MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH THREE TIMES DAILY

Processing Status: Released locally on 11/08/06@08:55:32 (Window)

Last Filled On: 11/08/06

The concurrent administration of amiodarone with indinavir,(1) nelfinavir,(2) ritonavir,(3) or tipranavir coadministered with ritonavir(4) may result in increased levels, clinical effects, and toxicity of amiodarone.

SIGNIFICANT Drug Interaction with Local Rx

\*\*\*SIGNIFICANT\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 5MG TAB and

Local RX#: 2443

Drug: ASPIRIN 325MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH THREE TIMES DAILY

Processing Status: Released locally on 11/08/06@08:55:32 (Window)

Last Filled On: 11/08/06

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

Drug interaction warning message for a remote outpatient order:

Significant Drug Interaction with Remote Rx

\*\*\* Significant\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 5MG TAB and

LOCATION: \<VA or DOD facility\> Remote RX#: 10950021

Drug: ASPIRIN 325MG EC TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

Last Filled On: 11/08/06

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

Critical Drug Interaction with Remote Rx

\*\*\*CRITICAL\*\*\* Drug Interaction with Prospective Drug:

INDINAVIR 400MG CAP and

LOCATION: \<VA or DOD Facility\> Remote Rx#: 2443

Drug: AMIODARONE 200MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH THREE TIMES DAILY

Last Filled On: 11/08/06

The concurrent administration of amiodarone with indinavir,(1) nelfinavir,(2) ritonavir,(3) or tipranavir coadministered with ritonavir(4) may result in increased levels, clinical effects, and toxicity of amiodarone.

Drug interaction warning message that is currently displayed for a Non-VA medication:

Critical Drug Interaction with Non-VA Med Order

\*\*\*Critical\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 5MG TAB and

Non-VA Med: CIMETIDINE 200MG TAB

SIG: ONE TABLET Schedule: AT BEDTIME

The pharmacologic effects of warfarin may be increased resulting in severe bleeding.

Significant Drug Interaction with Non-VA Med Order

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 5MG TAB and

Non-VA Med: ASPIRIN 325MG TAB

SIG: ONE TABLET Schedule: \<NOT ENTERED\>

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

Drug interaction warning message that shall be displayed for a pending order:

Critical Drug Interaction with Pending Order

\*\*\*CRITICAL\*\*\* Drug Interaction with Prospective Drug:

INDINAVIR 400MG CAP and

Pending Drug: AMIODARONE 200MG TAB

SIG: TAKE ONE TABLET EVERY 8 HOURS

The concurrent administration of amiodarone with indinavir,(1) nelfinavir,(2) ritonavir,(3) or tipranavir coadministered with ritonavir(4) may result in increased levels, clinical effects, and toxicity of amiodarone.

Significant Drug Interaction with Pending Order

\*\*\*SIGNIFICANT\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 5MG TAB and

Pending Drug: ASPIRIN 325MG TAB

SIG: TAKE ONE TABLET EVERY 8 HOURS

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

### Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinic orders are created via CPRS generally using the Meds Inpatient tab or the IV Fluids tab. Drug orders that have a clinic and an appointment date and time are considered clinic orders. The clinic must be defined with ‘ADMINISTER INPATIENT MEDS?’ prompt answered YES under the SETUP A CLINIC \[SDBUILD\] option in the Scheduling package. Defining the clinic in this manner ensures that an appointment date and time are defined. Orders placed via backdoor inpatient medications are not considered clinic orders.

MOCHA v1.0 Enhancements 1 adds drug interaction and therapeutic duplication order checks for clinic orders to Outpatient Pharmacy. Previously Inpatient Medications package performed order checks on active, pending, and non-verified clinic orders. With the MOCHA v1.0 Enhancements 1, Inpatient medications will perform enhanced order checks for recently discontinued and expired inpatient medications clinic orders.

For both packages, the system will display clinic orders in a standard format to differentiate them from Inpatient Medications and Outpatient Pharmacy order checks.

Discontinued/expired orders must have a stop date within the last 90 days to be evaluated during enhanced order checks. For pending clinic orders, a variety of start and stop dates are available based on the information that the provider enters during initial order entry. The following are the scenarios that drive which dates will be displayed for the clinic order:

- If there are start/stop dates defined, they are displayed.
- If there are no stop/start dates defined, the ‘requested start/stop dates’ will be displayed with the word “Requested” prior to the start/stop date header.
- If there are no requested start/stop dates defined, the order date will be displayed and the start/stop date headers will be displayed with “\*\*\*\*\*\*\*\*” for the date.
- If there is either a requested start date or a requested stop date, the available date will be displayed and “\*\*\*\*\*\*\*\*” will be displayed for the undefined date.

Unit Dose Clinic Order Check Example:

> Now Processing Enhanced Order Checks! Please wait...

> \*\*\*CRITICAL\*\*\* Drug Interaction with Prospective Drug:

> CIMETIDINE 300 MG and

> Clinic Order: PHENYTOIN 100MG CAP (DISCONTINUED)

> Schedule: Q8H

> Dosage: 100MG

> Start Date: FEB 27, 2012@13:00

> Stop Date: FEB 28, 2012@15:22:27

> Concurrent use of cimetidine or ranitidine may result in elevated levels

> of and toxicity from the hydantoin. Neutropenia and thrombocytopenia have

> been reported with concurrent cimetidine and phenytoin.

IV Clinic Order Check Example:

> \*\*\*CRITICAL\*\*\* Drug Interaction with Prospective Drug:

> WARFARIN 2MG TAB and

> Clinic Order: POTASSIUM CHLORIDE 20 MEQ (ACTIVE)

> Other Additive(s): MAGNESIUM SULFATE 1 GM (1), CALCIUM GLUCONATE 1 GM (2),

> HEPARIN 1000 UNITS, CIMETIDINE 300 MG

> Solution(s): DEXTROSE 20% 500 ML 125 ml/hr

> AMINO ACID SOLUTION 8.5% 500 ML 125 ml/hr

> Start Date: APR 05, 2012@15:00

> Stop Date: APR 27, 2012@24:00

> The pharmacologic effects of warfarin may be increased resulting in severe

> bleeding.

Therapeutic Duplication – IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions.

Unit Dose Clinic Order Check Example:

> \*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* POTASSIUM CHLORIDE 30 MEQ with

> Clinic Order: POTASSIUM CHLORIDE 10MEQ TAB (PENDING)

> Schedule: BID

> Dosage: 20MEQ

> Requested Start Date: NOV 20, 2012@17:00

> Stop Date: \*\*\*\*\*\*\*\*

> Class(es) Involved in Therapeutic Duplication(s): Potassium

IV Order Check Example:

> \*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* CEFAZOLIN 1 GM with

> Clinic Order: CEFAZOLIN 2 GM (PENDING)

> Solution(s): 5% DEXTROSE 50 ML OVER 30 MINUTES

> Schedule: Q8H

> Order Date: NOV 20, 2012@11:01

> Start Date: \*\*\*\*\*\*\*\*

> Stop Date: \*\*\*\*\*\*\*\*

> Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

> Solution(s): 5% DEXTROSE 50 ML OVER 30 MINUTES

> Schedule: Q12H

> Start Date: OCT 24, 2012@16:44

> Stop Date: OCT 25, 2012@24:00

> Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

> Cephalosporins, Cephalosporins - 1st Generation

The Duplicate Drug order check is performed against active, pending, non-verified, orders on hold (initiated through pharmacy or CPRS), expired and discontinued orders. The timeframe for inclusion of expired and discontinued orders is determined by the display rules on the medication profile. This check will be performed on active Non-VA Medication orders.

Users have the capability to discontinue duplicate orders. The existing order will only be discontinued upon acceptance of the order being processed. No discontinue actions can be performed on remote outpatient orders, Non-VA medications, discontinued, and expired orders or orders placed on provider hold through CPRS. If the DRUG CHECK FOR CLERK outpatient site parameter is set to ‘No’, no discontinue action is allowed for a clerk on a duplicate drug check. If a medication order is being entered through the pharmacy backdoor options it will be deleted. If finishing a pending order, the user will be forced to discontinue it.

Any remote Outpatient order (from another VAMC or Department of Defense (DoD) facility) using data from Health Data Repository Historical (HDR-Hx) or Health Data Repository- Interim Messaging Solution (HDR-IMS) that has been expired for 30 days or less will be included in the list of medications to be checked.

The Duplicate Drug warning displays the following information for a local or remote outpatient medication order:

Local Rx

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

Remote Rx

Duplicate Drug in Remote Rx:

LOCATION NAME: \<NAME OF FACILITY\>

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Days Supply: 30

Duplicate Drug order check for Pending Orders:

Pending Order

DUPLICATE DRUG in a Pending Order for:

Drug: ALLOPURINOL 300MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 180 \# of Refills: 3

Provider: PSOPROVIDER,TEN Issue Date: 03/24/08@14:44:15

Provider Comments: \<only if data present\>

Duplicate Drug order check for Non-Va Medications:

Non-VA Med Order

Duplicate Drug in a Non-VA Med Order for

Drug: CIMETIDINE 300MG TAB

Dosage: 300MG

Schedule: AT BEDTIME

Medication Route: MOUTH

Start Date: \<NOT ENTERED\> CPRS Order \#: 13554

Documented By: PSOPROVIDER,TEN on Mar 24, 2008@14:44:15

Duplicate Drug Order Check business rules:

1.  If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO, the system will not prompt a clerk (no PSORPH key) to discontinue the order when a Duplicate Drug order check occurs.

> b\. If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO, and a new order is being entered by a clerk (no PSORPH key) via the pharmacy backdoor, the order being processed will be deleted by the system immediately after the duplicate drug warning is displayed.

> c\. If the duplicate drug is a remote order, the system will allow the clerk to process the new order after the display of the duplicate drug warning.

> d\. If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO, and a clerk (no PSORPH key) is finishing a pending order:

> d1. When the VERIFICATION outpatient site parameter is set to YES and the duplicate drug is a local order, the system will return the user back to the detailed order ListMan display with the available actions of Accept/Edit/Discontinue.

> d2. When the VERIFICATION outpatient site parameter is set to YES and the duplicate drug is a remote order.

> d2a. A duplicate drug warning will be displayed.

> d2b. The clerk will be allowed to finish the order.

> d2c. The finished order will have a status of non-verified.

> d3. When the VERIFICATION outpatient site parameter is set to NO, the clerk will not be allowed to finish the order.

> d4. If the DRUG CHECK FOR CLERK outpatient site parameter is set to Yes, a clerk (no PSORPH key) will see the same discontinue prompts as a pharmacist.

> e\. If the VERIFICATION outpatient site parameter is set to YES when reinstating an order, no duplicate message will be displayed and the reinstated order will have a non-verified status.

> f\. No discontinuation prompt will be displayed for a duplicate Non-VA medication order in any situation.

After the Duplicate Drug warning is displayed, the system will ask the user if they wish to discontinue the order.

Active Order

Discontinue RX \#2580A SUCRALFATE 1GM TAB? Y/N

Pending Order

Discontinue Pending Order for ALLOPURINOL 300MG? Y/N

If the user chooses not to discontinue the displayed order when entering a new order via the pharmacy backdoor, the system will delete the order being entered (prospective drug).

If the user chooses not to discontinue the displayed order when finishing a pending order, the system will redisplay the pending order and prompt them to accept, edit or discontinue the order.

If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO, and if the clerk (no PSORPH key) is copying an order, the system will return them back to the detailed order ListMan display where the copy action was initiated.

If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO and the VERIFICATION outpatient site parameter is set to YES when a clerk (no PSORPH key) is reinstating a discontinued order for a medication for which an active local order exists, the system will delete the active order and reinstate the discontinued order.

If the DRUG CHECK FOR CLERK outpatient site parameter is set to NO and the VERIFICATION outpatient site parameter is set to NO when a clerk is reinstating a discontinued order for a medication for which an active local order exists, the system will display a duplicate drug warning, but the order will not be reinstated.

If the DRUG CHECK FOR CLERK outpatient site parameter is set to YES or NO and the VERIFICATION outpatient site parameter is set to NO when a clerk is reinstating a discontinued order for a medication for which a remote order exists, the system will display a duplicate drug warning and the reinstated order will be assigned an active status.

If the DRUG CHECK FOR CLERK outpatient site parameter is set to YES or NO and the VERIFICATION outpatient site parameter is set to YES when a clerk is reinstating a discontinued order, the system will not display a duplicate drug warning and the reinstated order will be assigned a non-verified status.

If a duplicate drug warning is displayed for a medication order, it will not be included in a duplicate therapy order check.

The following examples illustrate the conditions described above.

Duplicate Pending Order

Pending OP Orders (ROUTINE) Mar 24, 2008@13:52:04 Page: 1 of 2

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.58

Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 325MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING DUPLICATE THERAPY FUNCTIONALITY

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 325MG EC TAB \<DIN\>

\(3\) \*Dosage: 325 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: QAM

\+ Enter ?? for more actions

BY Bypass DC Discontinue

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

RX \#: 2603

Drug: ASPIRIN 325MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

Discontinue RX \#2603 ASPIRIN 325MG EC TAB? Y/N NO -Prescription was not discontinued...

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

Press Return to Continue:

Pending OP Orders (ROUTINE) Mar 24, 2008@13:52:45 Page: 1 of 2

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.58

Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 325MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING DUPLICATE THERAPY FUNCTIONALITY

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 325MG EC TAB \<DIN\>

NDC: 00056-0176-75

\(3\) \*Dosage: 325 (MG)

Verb: TAKE

Dispense Units: 1

NOUN: TABLET

\*Route: ORAL

\*Schedule: QAM

\+ Enter ?? for more actions

AC Accept ED Edit DC Discontinue

Select Item(s): Next Screen//

.

.

OR

Discontinue RX \#2603 ASPIRIN 325MG EC TAB? Y/N <u>YES</u>

RX \#2603 ASPIRIN 325MG EC TAB will be discontinued after the acceptance of the new order.

Rx \# 2604 03/24/08

PSOPATIENT,FOUR \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

ASPIRIN 325MG EC TAB

PSOPROVIDER,TEN PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 100%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? YES// YES

Are you sure you want to Accept this Order? NO// YES

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

-Duplicate Drug Rx \#2603 ASPIRIN 325MG EC TAB has been discontinued...

Press Return to Continue:

New Order Entry Backdoor – Duplicate Drug

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: aspirin

Lookup: DRUG GENERIC NAME

1 ASPIRIN 325MG EC TAB CN103

2 ASPIRIN 325MG SUPPOSITORY CN103

3 ASPIRIN 325MG TAB CN103

4 ASPIRIN 650MG/BUTALBITAL 50MG TAB CN103

5 ASPIRIN 81MG EC TAB CN103

Press \<RETURN\> to see more, '^' to exit this list, '^^' to exit all lists, OR

CHOOSE 1-5: 1 ASPIRIN 325MG EC TAB CN103

Restriction/Guideline(s) exist. Display? : (N/D): No// NO

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

RX \#: 2604

Drug: ASPIRIN 325MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

Discontinue RX \#2604 ASPIRIN 325MG EC TAB? Y/N <u>NO</u> -Prescription was not discontinued...

RX DELETED

OR

Discontinue RX \#2604 ASPIRIN 325MG EC TAB? Y/N <u>YES</u>

RX \#2604 ASPIRIN 325MG EC TAB will be discontinued after the acceptance of the new order.

VERB: TAKE

There are 2 Available Dosage(s):

1\. 325MG

2\. 650MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 325MG

You entered 325MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 325MG

NOUN: TABLET

ROUTE: PO// ORAL PO MOUTH

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

BID BID TWICE A DAY

...OK? Yes// (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(TAKE ONE TABLET BY MOUTH TWICE A DAY)

DAYS SUPPLY: (1-90): 30//

QTY ( TAB ) : 60// 60

COPIES: 1// 1

\# OF REFILLS: (0-11): 11//

PROVIDER: PSOPROVIDER,TEN

CLINIC:

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

ISSUE DATE: TODAY// (MAR 24, 2008)

FILL DATE: (3/24/2008 - 3/25/2009): TODAY// (MAR 24, 2008)

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2605 03/24/08

PSOPATIENT,FOUR \#60

TAKE ONE TABLET BY MOUTH TWICE A DAY

ASPIRIN 325MG EC TAB

PSOPROVIDER,TEN PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 100%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? n NO

Is this correct? YES//

-Duplicate Drug RX \#2604 ASPIRIN 325MG EC TAB has been discontinued...

Another New Order for PSOPATIENT,FOUR? YES//

Editing Dispense Drug – Create New Order

Rx \#: 2605A

\(1\) \*Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 325MG EC TAB \<DIN\>

NDC: 00056-0176-75

\(3\) \*Dosage: 325 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/24/08 (7) Fill Date: 03/24/08

Last Fill Date: 03/24/08 (Window)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// ED Edit

Select fields by number: (1-19): 2

DRUG: ASPIRIN 325MG EC TAB// ASPIRIN 8

Lookup: GENERIC NAME

ASPIRIN 81MG EC TAB CN103

...OK? Yes// (Yes)

TRADE NAME:

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2606

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 03/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

Discontinue RX \#2606 ASPIRIN 81MG EC TAB? Y/N NO -Prescription was not discontinued...

.

.

OR

Discontinue RX \#2606 ASPIRIN 81MG EC TAB? Y/N YES

RX \#2606 ASPIRIN 81MG EC TAB will be discontinued after the acceptance of the new order.

You have changed the dispense drug from

ASPIRIN 325MG EC TAB to ASPIRIN 81MG EC TAB.

Current SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

There are 2 Available Dosage(s):

1\. 81MG

2\. 162MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 81MG

You entered 81MG is this correct? Yes// YES

This edit will discontinue the duplicate Rx & change the dispensed drug!

Do You Want to Proceed? NO// YES

VERB: TAKE// TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 81MG

NOUN: TABLET// TABLET

ROUTE: ORAL// ORAL

Schedule: BID// QAM

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QAM QAM EVERY MORNING

...OK? Yes// (Yes)

(EVERY MORNING)

LIMITED DURATION (IN MONTHS, WEEKS, DAYS, HOURS OR MINUTES):

CONJUNCTION:

New OP Order (ROUTINE) Mar 24, 2008@14:10:20 Page: 1 of 2

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.58

Orderable Item: ASPIRIN TAB,EC

\(1\) Drug: ASPIRIN 81MG EC TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: MAR 24,2008 (4) Fill Date: MAR 24,2008

\(5\) Dosage Ordered: 81 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

Route: ORAL

Schedule: QAM

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(7\) Days Supply: 30 (8) QTY (TAB): 60

\(9\) \# of Refills: 11 (10) Routing: WINDOW

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// AC Accept

Nature of Order: SERVICE CORRECTION// S

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2607 03/24/08

PSOPATIENT,FOUR \#60

TAKE ONE TABLET BY MOUTH EVERY MORNING

ASPIRIN 81MG EC TAB

PSOPROVIDER,TEN PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 100%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? YES//

Is this correct? YES// ...

-Duplicate Drug RX \#2606 ASPIRIN 81MG EC TAB has been discontinued...

Clerk Entering New Order via Backdoor – Drug Check for Clerk Parameter set to No

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ASPIRIN 81

Lookup: GENERIC NAME

ASPIRIN 81MG EC TAB CN103

...OK? Yes// (Yes)

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

RX DELETED

Another New Order for PSOPATIENT,FOUR? YES//

Clerk Entering New Order via Backdoor – Drug Check for Clerk Parameter set to No – Duplicate Drug – Discontinued Status

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ASPIRIN

Lookup: GENERIC NAME

1 ASPIRIN 325MG EC TAB CN103

2 ASPIRIN 325MG SUPPOSITORY CN103

3 ASPIRIN 325MG TAB CN103

4 ASPIRIN 650MG/BUTALBITAL 50MG TAB CN103

5 ASPIRIN 81MG EC TAB CN103

Press \<RETURN\> to see more, '^' to exit this list, '^^' to exit all lists, OR

CHOOSE 1-5: 1 ASPIRIN 325MG EC TAB CN103

Restriction/Guideline(s) exist. Display? : (N/D): No// NO

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2605A

Drug: ASPIRIN 325MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 60 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Discontinued (Edit) Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

Press Return to Continue:

Clerk Finishing Pending Order – Drug Check for Clerk parameter set to No

ED (Edit) FN Finish

Pending OP Orders (ROUTINE) Mar 24, 2008@14:35:21 Page: 1 of 3

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.58

CPRS Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 81MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

Duplicate drug class order:(ASPIRIN TAB,EC 325MG

TAKE ONE TABLET BY MOUTH EVERY MORNING \[UNRELEASED\])

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 81MG EC TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 81 (MG)

\+ Enter ?? for more actions

BY Bypass DC (Discontinue)

ED (Edit) FN Finish

Select Item(s): Next Screen// FN Finish

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

--------------------------------------------------------------------------------

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

Press Return to Continue:

Pending OP Orders (ROUTINE) Mar 24, 2008@14:35:25 Page: 1 of 3

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.58

CPRS Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 81MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

Duplicate drug class order: NON-OPIOID ANALGESICS (ASPIRIN TAB,EC 325MG

TAKE ONE TABLET BY MOUTH EVERY MORNING \[UNRELEASED\])

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 81MG EC TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 81 (MG)

\+ Enter ?? for more actions

AC Accept ED Edit DC Discontinue

Select Item(s): Next Screen// DC Discontinue

Nature of Order: SERVICE CORRECTION// S

Requesting PROVIDER: PSOPROVIDER,TEN// LBB 119

Comments: Per Pharmacy Request Replace

Press Return to :

PI Patient Information SO Select Order

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// 2

Medication Profile Mar 24, 2008@14:36:28 Page: 1 of 1

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: 102.4(est.) (CREAT:1.0mg/dL 10/30/12) BSA (m2): 1.78

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 2608 ASPIRIN 81MG EC TAB 30 A 03-24 03-24 11 30

----------------------------------NON-VERIFIED----------------------------------

2 2609 ASPIRIN 325MG EC TAB 30 N 03-24 03-24 5 30

Duplicate with Non-VA Med – No Action Required

DRUG: CIMETIDINE

Lookup: GENERIC NAME

1 CIMETIDINE 100MG TAB GA301

2 CIMETIDINE 200MG TAB GA301

3 CIMETIDINE 300MG TAB GA301 90 DAY SUPPLY

4 CIMETIDINE 400MG TAB GA301

5 CIMETIDINE 800MG TAB GA301

CHOOSE 1-5: 3 CIMETIDINE 300MG TAB GA301 90 DAY SUPPLY

--------------------------------------------------------------------------------

Duplicate Drug in a Non-VA Med Order for

Drug: CIMETIDINE 300MG TAB

Dosage: 300MG

Schedule: AT BEDTIME

Medication Route: MOUTH

Start Date: CPRS Order \#: 13554

Documented By: PSOPROVIDER,TEN on Mar 24, 2008@14:44:15

--------------------------------------------------------------------------------

Press Return to Continue:

VERB: TAKE

There are 2 Available Dosage(s):

1\. 300MG

2\. 600MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 300MG

You entered 300MG is this correct? Yes//

Duplicate Drug with Pending Order

Another New Order for PSOPATIENT,FOUR? YES//

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ALLOPURINOL

Lookup: GENERIC NAME

1 ALLOPURINOL 100MG TAB MS400

2 ALLOPURINOL 300MG TAB MS400

CHOOSE 1-2: 2 ALLOPURINOL 300MG TAB MS400

-------------------------------------------------------------------------------

DUPLICATE DRUG in a Pending Order for:

Drug: ALLOPURINOL 300MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 180 \# of Refills: 3

Provider: PSOPROVIDER,TEN Issue Date: 03/24/08@14:44:15

-------------------------------------------------------------------------------

Discontinue Pending Order for ALLOPURINOL 300MG? Y/N <u>YES</u>

Pending Order for ALLOPURINOL 300MG will be discontinued after the acceptance of the new order.

VERB: TAKE

There are 2 Available Dosage(s):

1\. 300MG

2\. 600MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 300MG

You entered 300MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 300MG

NOUN: TABLET

ROUTE: PO// ORAL PO MOUTH

Schedule: QAM //

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QAM QAM EVERY MORNING

...OK? Yes// (Yes)

(EVERY MORNING)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(TAKE ONE TABLET BY MOUTH EVERY MORNING)

DAYS SUPPLY: (1-90): 30//

QTY ( TAB ) : 30// 30

COPIES: 1// 1

\# OF REFILLS: (0-11): 11//

PROVIDER: PSOPROVIDER,TEN

CLINIC:

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

ISSUE DATE: TODAY// (MAR 24, 2008)

FILL DATE: (3/24/2008 - 3/25/2009): TODAY// (MAR 24, 2008)

Nature of Order: WRITTEN// W

Rx \# 2610 03/24/08

PSOPATIENT,FOUR \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

ALLOPURINOL 300MG TAB

PSOPROVIDER,TEN PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 100%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? y YES

Is this correct? YES//

\- Duplicate Drug Pending Order for ALLOPURINOL 300MG has been discontinued...

Copying an Existing Order

RN Renew

Select Action: Next Screen// CO CO

OP Medications (ACTIVE) Mar 12, 2008@09:15:48 Page: 1 of 2

PSOPATIENT,TWO \<A\>

PID: 000-00-0000 Ht(cm): 182.88 (04/13/2005)

DOB: JAN 1,1945 (63) Wt(kg): 77.27 (04/13/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

Rx \#: 2584\$

\(1\) \*Orderable Item: AMLODIPINE/ATORVASTATIN TAB

\(2\) Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

Verb: TAKE

\(3\) \*Dosage: ONE TABLET

\*Route: ORAL

\*Schedule: QAM

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/12/08 (7) Fill Date: 03/12/08

Last Fill Date: 03/12/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 03/13/09 MFG:

\+ Enter ?? for more actions

AC Accept ED Edit

New OP Order (COPY) Mar 12, 2008@09:15:48 Page: 1 of 2

PSOPATIENT,TWO \<A\>

PID: 000-00-0000 Ht(cm): 182.88 (04/13/2005)

DOB: JAN 1,1945 (63) Wt(kg): 77.27 (04/13/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

Orderable Item: AMLODIPINE/ATORVASTATIN TAB

\(1\) Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: MAR 12,2008 (4) Fill Date: MAR 12,2008

Verb: TAKE

\(5\) Dosage Ordered: ONE TABLET

Route: ORAL

Schedule: QAM

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(7\) Days Supply: 30 (8) QTY ( ): 30

\(9\) \# of Refills: 11 (10) Routing: WINDOW

\(11\) Clinic:

\(12\) Provider: PSOPROVIDER,ONE (13) Copies: 1

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

-----------------------------------------------------------------------------

Duplicate Drug in Local RX:

Rx \#: 2584

Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: OPPROVIDER, ONE Issued: 03/12/07

Status: ACTIVE Last filled on: 03/12/07

Processing Status: Released locally on 3/12/07@08:55:32 (Window)

Days Supply: 30

-----------------------------------------------------------------------------

Discontinue Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB? Y/N YES

Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB will be discontinued after the acceptance of the new order.

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2585 03/12/08

PSOPATIENT,TWO T \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 40%

Disabilities: NONE STATED

Was treatment for Service Connected condition? NO//

Is this correct? YES// ...

Duplicate Drug Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB has been discontinued...

The CPRS Auto Refill field can be updated using the *Pharmacy Systems Parameter Edit* \[PSS MGR\] option. This parameter works in conjunction with the PSOUATRF security key.

- When the CPRS Auto Refill field is set to YES and the PSOAUTRF security key has been assigned to at least one user, all refills placed in CPRS by the provider are processed and suspended with the next fill date and all routing is set to Mail automatically.
- When the CPRS Auto Refill field is set to NO or if the PSOAUTRF security key is not assigned, the manual refill process is required.

If the auto refill process fails, the order will not be processed and will require manual refilling. A MailMan message will be sent to the holders of the PSOAUTRF key describing the reason for not filling the auto refill. All of the refill activity, manual or automatic, is recorded in the Activity Log entry notes.

Following the installation of patches PSO\*7\*207 and OR\*3\*238 (Remote Data Interoperability (RDI) trigger patch), order checks will be made using additional data from the Health Data Repository Interim Messaging Solution (HDR-IMS) and the HDR-Historical (HDR-Hx). This will contain both Outpatient orders from other VAMCs as well as from Department of Defense (DoD) facilities, if available. All remote prescription statuses will be included in order checking for a new order being processed from within backdoor outpatient pharmacy and for new orders being placed by CPRS or by Inpatient Medications. Any remote Outpatient order that has been expired or discontinued for 30 days or less will be included in the list of medications to be checked.

If the verification site parameter is turned on, prescriptions entered by the technician will be non-verified and must be verified by the pharmacist. If the verification site parameter is turned off the label is queued to print as though the pharmacist has entered it unless the prescription causes a critical drug interaction. In which case, the prescription will be non-verified and must be verified by the pharmacist.

Actions are displayed in the action area of the screen. Actions with a parenthesis ( ) around them are invalid actions for that order. A double question mark (??) displays all the actions available, including the Outpatient Pharmacy hidden actions described in “Chapter 2: List Manager”. If one of the hidden actions is selected and it is invalid, a message will display in the message window. Outpatient Pharmacy hidden actions are displayed with the letters OP next to the action.

With Patch PSO\*7\*233, when a name is selected, if the patient’s address is flagged with a Bad Address Indicator, a warning message is displayed. If the user has proper authorization (i.e., the PSO SITE parameter “EDIT PATIENT DATA” is set to Yes or the user holds the new PSO ADDRESS UPDATE security key), a prompt appears asking if the user wants to update the address.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/028.png)For the *Patient Prescription Processing,* if a temporary address has no end date, the following text is displayed in the Status column: “(Temp address from XXX 99,9999 till (no end date))”.

### Titration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduced in PSO\*7\*313, the user has the ability to mark prescriptions as 'Titration to Maintenance' when finishing prescriptions from CPRS as well as via the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option by invoking the new hidden action 'TM' - Mark Rx as Titration. This action will result in preventing the following actions to be taken on the prescription: Refill, Renewal (including via CPRS), and Copy and editing of any field that requires a new Rx to be created. This action will also set the new field TITRATION RX FLAG (#45.3) in the PRESCRIPTION File (#52) as well as the new field TITRATION DOSE RX (#45.1) in the PRESCRIPTION File (#52). Prescriptions that are marked as Titration/Maintenance will have the letter 't' postfix to the RX \# as seen below (entry \#1):

: : :

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------ACTIVE-------------------------------

1 100005024t AMOXAPINE 50MG TAB 30 S 09-26 09-26 2 30

2 100005022 AMOXICILLIN 250MG CAP 30 A 08-18 08-18 11 30

3 100005035 KALETRA 3 A 09-29 09-29 0 3

: : :

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/029.png)Note: A prescription can be unmarked as Titration/Maintenance by invoking the same TM action on an already marked prescription.

There is also a new hidden action in the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option called TR (Convert Titration Rx). This action populates the MAINTENANCE DOSE RX (#45.2) field in the PRESCRIPTION File (#52). When a titration to maintenance prescription needs to be refilled so the patient can continue on the Maintenance Dose, this option allows users to create a new prescription with the maintenance dose only. The process works similar to copying an existing prescription; however, it can only be used on prescriptions with the following characteristics:

- Rx is a complex order with a THEN conjunction
- Rx is released
- Rx status is ACTIVE
- Rx does not have refills previously ordered
- Rx \# Of Refills is greater than 0 (zero)

Before the new Maintenance Rx can be accepted, the user is prompted to validate the QTY field for the new Rx, which may or may not be automatically re-calculated. Only the last dose from the original prescription is carried over to the new Maintenance Rx, and the \# of Refills field is decreased by 1 because the new Maintenance Rx counts as a fill. Once the user verifies the information for the Maintenance Rx is accurate, they can accept the Maintenance Rx. This action will trigger a Duplicate Drug check against the original complex order, which must be discontinued before the new Maintenance Rx can be accepted. After the new Maintenance Rx is accepted, it will have the new indicator 'm' on the right side of the Rx \# in the patient's Medication Profile as seen below (entry \#1):

: : :

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------ACTIVE-------------------------------

1 100005436m AMOXAPINE 50MG TAB 30 S 09-26 09-26 1 30

2 100005022 AMOXICILLIN 250MG CAP 30 A 08-18 08-18 11 30

3 100005035 KALETRA 3 A 09-29 09-29 0 3

: : :

## Entering a New Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a double question mark (??) is entered at the “Select Action” prompt, the following hidden actions will display in the action area. Actions that apply only to outpatient orders are followed by (OP).

The following actions are also available:

RP Reprint (OP) DN Down a Line LS Last Screen

RN Renew (OP) RD Re Display Screen FS First Screen

DC Discontinue (OP) PT Print List GO Go to Page

RL Release (OP) PS Print Screen + Next Screen

RF Refill (OP) \> Shift View to Right - Previous Screen

PP Pull Rx (OP) \< Shift View to Left ADPL Auto Display(On/Off)

IP Inpat. Profile (OP) SL Search List CK Check Interactions

RS Reprint Sig Log RDD Fill/Rel Date Disply IN Intervention Menu

CM Manual Queue to CMOP DR Display Remote UP Up a Line

OTH Other OP Actions QU Quit

First, a patient is selected.

Example: Entering a New Order

Select Pharmacy Technician's Menu Option: PATient Prescription Processing

Select PATIENT NAME: OPPATIENT16,ONE 4-3-41 000246802 YES SC VETERAN

Patient is enrolled to receive ScripTalk ‘talking’ prescription labels.

Eligibility: SC

RX PATIENT STATUS: SERVICE CONNECTED// \<Enter\>

\[Patient Information Screen skipped\]

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/030.png)If RDI is active and a patient has prescriptions at another location, when the user selects the patient to enter a new order from Patient Prescription Processing, the following message appears.

REMOTE PRESCRIPTIONS AVAILABLE!

Display Remote Data? N//

If the user responds NO, then the normal procedure occurs for entering prescriptions. If the user responds YES, the “Remote Facilities Visited” screen appears. See the Displaying a Patient’s Remote Prescriptions section later in Entering a New Order for more details.

Although “Quit” is the default at the “Select Action” prompt shown on the Patient Information screen, \<Enter\> at this prompt quits the screen and displays the Medication Profile. This Medication Profile includes any Non-VA Med orders documented via the CPRS GUI package.

Medication Profile Jun 12, 2001 14:12:21 Page: 1 of 1

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: 102.4(est.) (CREAT:1.0mg/dL 10/30/12) BSA (m2): 2.08

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 503904\$ AMPICILLIN 250MG CAP 80 E 05-25 05-25 0 10

2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

----------------------------------DISCONTINUED---------------------------------

3 503902 ACETAMINOPHEN 500MG TAB 60 DC\>05-22 05-22 3 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Typing in the letters “NO” at the “Select Action” prompt creates a new order.

Example: Entering a New Order (continued)

Medication Profile Mar 29, 2011@14:34:27 Page: 1 of 1

(Patient information is displayed here.)

:

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility:

RX PATIENT STATUS: SC LESS THAN 50%//

DRUG: ACETAMINOPHEN

Lookup: GENERIC NAME

1 ACETAMINOPHEN 160MG/5ML LIQUID CN103 NATL FORM; 480 M

L/BT (NDC)

2 ACETAMINOPHEN 325MG TAB CN103 NATL FORM; DU: INCREMEN

TS OF 100 ONLY \*\*\* AUTOMED & SCRIPTPRO \*\*\*

3 ACETAMINOPHEN 325MG/BUTALBITAL 50MG TAB CN103 N/F N

ATL N/F

4 ACETAMINOPHEN 500MG TAB CN103 NATL FORM; DU: INCREMEN

TS OF 100 ONLY\*\*\* AUTOMED & SCRIPTPRO \*\*\*

5 ACETAMINOPHEN 650MG RTL SUPP CN103 NATL FORM (IEN)

CHOOSE 1-5: 5 ACETAMINOPHEN 650MG RTL SUPP CN103 NATL FORM (IEN

)

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* ACETAMINOPHEN 650MG RTL SUPP with

Local RX#: 2054930

Drug: ACETAMINOPHEN 500MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH EVERY FOUR HOURS AS NEEDED

QTY: 180 Days Supply: 30

Processing Status: Not released locally (Window)

Last Filled On: 03/29/11

Class(es) Involved in Therapeutic Duplication(s): Non-Narcotic

Analgesic/Antipyretic, Non-Salicylate

===============================================================================

Press Return to continue:

Discontinue Rx \#2054930 ACETAMINOPHEN 500MG TAB Y/N ?

The system checks the medication selected for any duplicate drugs or classes, interactions, or allergies that are noted in the patient’s local and remote record. This also includes any local Non-VA Meds. See the following order check examples.

Clerk Entering New Order via Backdoor – Drug Check for Clerk Parameter set to No

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ASPIRIN 81

Lookup: GENERIC NAME

ASPIRIN 81MG EC TAB CN103

...OK? Yes// (Yes)

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

------- RX DELETED

Another New Order for PSOPATIENT,FOUR? YES//

.

------------------------------------------------------------------------

Clerk Entering New Order via Backdoor – Drug Check for Clerk Parameter set to No – Duplicate Drug – Discontinued Status

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ASPIRIN

Lookup: GENERIC NAME

1 ASPIRIN 325MG EC TAB CN103

2 ASPIRIN 325MG SUPPOSITORY CN103

3 ASPIRIN 325MG TAB CN103

4 ASPIRIN 650MG/BUTALBITAL 50MG TAB CN103

5 ASPIRIN 81MG EC TAB CN103

Press \<RETURN\> to see more, '^' to exit this list, '^^' to exit all lists, OR

CHOOSE 1-5: 1 ASPIRIN 325MG EC TAB CN103

Restriction/Guideline(s) exist. Display? : (N/D): No// NO

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2605A

Drug: ASPIRIN 325MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 60 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Discontinued (Edit) Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

-------------------------------------------------------------------------------

Press Return to Continue:

Clerk Finishing Pending Order – Drug Check for Clerk parameter set to No

ED (Edit) FN Finish

Pending OP Orders (ROUTINE) Mar 24, 2008@14:35:21 Page: 1 of 3

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

CPRS Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 81MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

Duplicate drug class order:(ASPIRIN TAB,EC 325MG

TAKE ONE TABLET BY MOUTH EVERY MORNING \[UNRELEASED\])

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 81MG EC TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 81 (MG)

\+ Enter ?? for more actions

BY Bypass DC (Discontinue)

ED (Edit) FN Finish

Select Item(s): Next Screen// FN Finish

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2608

Drug: ASPIRIN 81MG EC TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: PSOPROVIDER,TEN Issued: 03/24/08

Status: Active Last filled on: 03/24/08

Processing Status: Released locally on 3/24/08@08:55:32 (Window)

Days Supply: 30

--------------------------------------------------------------------------------

Pending OP Orders (ROUTINE) Mar 24, 2008@14:35:25 Page: 1 of 3

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

CPRS Order Checks:

Duplicate drug order: ASPIRIN TAB,EC 81MG TAKE ONE TABLET BY MOUTH EVERY

MORNING \[ACTIVE\]

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

Duplicate drug class order: NON-OPIOID ANALGESICS (ASPIRIN TAB,EC 325MG

TAKE ONE TABLET BY MOUTH EVERY MORNING \[UNRELEASED\])

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: TESTING

\*(1) Orderable Item: ASPIRIN TAB,EC

\(2\) Drug: ASPIRIN 81MG EC TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 81 (MG)

\+ Enter ?? for more actions

AC Accept ED Edit DC Discontinue

Select Item(s): Next Screen// DC Discontinue

Nature of Order: SERVICE CORRECTION// S

Requesting PROVIDER: PSOPROVIDER,TEN// LBB 119

Comments: Per Pharmacy Request Replace

Press Return to :

PI Patient Information SO Select Order

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// 2

Medication Profile Mar 24, 2008@14:36:28 Page: 1 of 1

PSOPATIENT,FOUR \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 168.91 (04/11/2006)

DOB: MAY 20,1966 (41) Wt(kg): 68.18 (09/06/2006)

SEX: MALE

CrCL: 102.4(est.) (CREAT:1.0mg/dL 10/30/12) BSA (m2): 1.78

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 2608 ASPIRIN 81MG EC TAB 30 A 03-24 03-24 11 30

----------------------------------NON-VERIFIED----------------------------------

2 2609 ASPIRIN 325MG EC TAB 30 N 03-24 03-24 5 30

Duplicate with Non-VA Med – No Action Required

DRUG: CIMETIDINE

Lookup: GENERIC NAME

1 CIMETIDINE 100MG TAB GA301

2 CIMETIDINE 200MG TAB GA301

3 CIMETIDINE 300MG TAB GA301 90 DAY SUPPLY

4 CIMETIDINE 400MG TAB GA301

5 CIMETIDINE 800MG TAB GA301

CHOOSE 1-5: 3 CIMETIDINE 300MG TAB GA301 90 DAY SUPPLY

--------------------------------------------------------------------------------

Duplicate Drug in a Non-VA Med Order for

Drug: CIMETIDINE 300MG TAB

Dosage: 300MG

Schedule: AT BEDTIME

Medication Route: MOUTH

Start Date: CPRS Order \#: 13554

Documented By: PSOPROVIDER,TEN on Mar 24, 2008@14:44:15

--------------------------------------------------------------------------------

Press Return to Continue:

VERB: TAKE

There are 2 Available Dosage(s):

1\. 300MG

2\. 600MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 300MG

You entered 300MG is this correct? Yes//

Duplicate Drug with Pending Order

Another New Order for PSOPATIENT,FOUR? YES//

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: OPT NSC//

DRUG: ALLOPURINOL

Lookup: GENERIC NAME

1 ALLOPURINOL 100MG TAB MS400

2 ALLOPURINOL 300MG TAB MS400

CHOOSE 1-2: 2 ALLOPURINOL 300MG TAB MS400

-------------------------------------------------------------------------------

DUPLICATE DRUG in a Pending Order for:

Drug: ALLOPURINOL 300MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 180 \# of Refills: 3

Provider: PSOPROVIDER,TEN Issue Date: 03/24/08@14:44:15

-------------------------------------------------------------------------------

Discontinue Pending Order for ALLOPURINOL 300MG? Y/N <u>YES</u>

Pending Order for ALLOPURINOL 300MG will be discontinued after the acceptance of the new order.

VERB: TAKE

There are 2 Available Dosage(s):

1\. 300MG

2\. 600MG

Select from list of Available Dosages(1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 300MG

You entered 300MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 300MG

NOUN: TABLET

ROUTE: PO// ORAL PO MOUTH

Schedule: QAM //

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QAM QAM EVERY MORNING

...OK? Yes// (Yes)

(EVERY MORNING)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(TAKE ONE TABLET BY MOUTH EVERY MORNING)

DAYS SUPPLY: (1-90): 30//

QTY ( TAB ) : 30// 30

COPIES: 1// 1

\# OF REFILLS: (0-11): 11//

PROVIDER: PSOPROVIDER,TEN

CLINIC:

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

ISSUE DATE: TODAY// (MAR 24, 2008)

FILL DATE: (3/24/2008 - 3/25/2009): TODAY// (MAR 24, 2008)

Nature of Order: WRITTEN// W

Rx \# 2610 03/24/08

PSOPATIENT,FOUR \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

ALLOPURINOL 300MG TAB

PSOPROVIDER,TEN PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 100%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? y YES

Is this correct? YES//

\- Duplicate Drug Pending Order for ALLOPURINOL 300MG has been discontinued...

Copying an Existing Order

RN Renew

Select Action: Next Screen// CO CO

OP Medications (ACTIVE) Mar 12, 2008@09:15:48 Page: 1 of 2

PSOPATIENT,TWO \<A\>

PID: 000-00-0000 Ht(cm): 182.88 (04/13/2005)

DOB: JAN 1,1945 (63) Wt(kg): 77.27 (04/13/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

Rx \#: 2584\$

\(1\) \*Orderable Item: AMLODIPINE/ATORVASTATIN TAB

\(2\) Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

Verb: TAKE

\(3\) \*Dosage: ONE TABLET

\*Route: ORAL

\*Schedule: QAM

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/12/08 (7) Fill Date: 03/12/08

Last Fill Date: 03/12/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 03/13/09 MFG:

\+ Enter ?? for more actions

AC Accept ED Edit

New OP Order (COPY) Mar 12, 2008@09:15:48 Page: 1 of 2

PSOPATIENT,TWO \<A\>

PID: 000-00-0000 Ht(cm): 182.88 (04/13/2005)

DOB: JAN 1,1945 (63) Wt(kg): 77.27 (04/13/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

Orderable Item: AMLODIPINE/ATORVASTATIN TAB

\(1\) Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: MAR 12,2008 (4) Fill Date: MAR 12,2008

Verb: TAKE

\(5\) Dosage Ordered: ONE TABLET

Route: ORAL

Schedule: QAM

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(7\) Days Supply: 30 (8) QTY ( ): 30

\(9\) \# of Refills: 11 (10) Routing: WINDOW

\(11\) Clinic:

\(12\) Provider: PSOPROVIDER,ONE (13) Copies: 1

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

-----------------------------------------------------------------------------

Duplicate Drug in Local RX:

Rx \#: 2584

Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: OPPROVIDER, ONE Issued: 03/12/07

Status: ACTIVE Last filled on: 03/12/07

Processing Status: Released locally on 3/12/07@08:55:32 (Window)

Days Supply: 30

-----------------------------------------------------------------------------

Discontinue Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB? Y/N YES

Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB will be discontinued after the acceptance of the new order.

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2585 03/12/08

PSOPATIENT,TWO T \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 40%

Disabilities: NONE STATED

Was treatment for Service Connected condition? NO//

Is this correct? YES// ...

Duplicate Drug Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB has been discontinued...

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/031.png)

> **NOTE:** More than one ingredient and more than one VA Drug Class may be associated with an Allergy/ADR. See output below:

A Drug-Allergy Reaction exists for this medication and/or class!

Drug: DILTIAZEM (DILACOR XR) 240MG SA CAP

Ingredients: DILTIAZEM (REMOTE SITE(S)),

Class: CV200 CALCIUM CHANNEL BLOCKERS (REMOTE SITE(S))

### Allergy/ADR Order Check Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section details the Allergy/ADR order check display within Outpatient Pharmacy.

Outpatient Pharmacy displays the same Allergy/ADR warning only once if both a drug class(es) and drug ingredient(s) are defined for the Allergy/ADR. The drug class and drug ingredient will be listed on the single display. The user is prompted to intervene once. If no intervention is chosen, the standard order entry dialog will resume. Local and remote Allergy/ADRs are combined.

If no Allergy Assessment has been documented for the patient for whom the medication order is being processed, the user will be forced to log an intervention for every medication order entered until the allergy assessment is resolved.

See examples below:

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/032.png)

> **NOTE:** Technicians do not get prompted for interventions.

Remote Allergy/ADR – New Order Entry Backdoor – Both Ingredient and Drug Class defined for Allergy/ADR

Select Action: Quit// NO New Order

PATIENT STATUS: SC//

DRUG: DILTIAZEM

Lookup: GENERIC NAME

1 DILTIAZEM (DILACOR XR) 240MG SA CAP CV200 N/F This

drug will not be processed without Drug Request Form 10-7144

2 DILTIAZEM (INWOOD) 120MG SA CAP CV200

3 DILTIAZEM (INWOOD) 180MG SA CAP CV200

4 DILTIAZEM (INWOOD) 240MG SA CAP CV200

5 DILTIAZEM (INWOOD) 300MG SA CAP CV200

Press \<RETURN\> to see more, '^' to exit this list, '^^' to exit all lists, OR

CHOOSE 1-5: 1 DILTIAZEM (DILACOR XR) 240MG SA CAP CV200 N/F This drug will not be processed without Drug Request Form 10-7144

Now doing allergy checks. Please wait...

A Drug-Allergy Reaction exists for this medication and/or class!

Prospective Drug: DILTIAZEM (DILACOR XR) 240MG SA CAP

Causative Agent: DILTIAZEM (SITE REPORTING ALLERGY – DATE REPORTED)

Historical/Observed: OBSERVED

Severity: MODERATE

Ingredients: DILTIAZEM ,

Signs/Symptoms: ITCHING,WATERING EYES, ANOREXIA, NAUSEA,VOMITING,

ANXIETY, DROWSINESS, DRY MOUTH, DRY NOSE, RASH,

Drug Class: CV200 CALCIUM CHANNEL BLOCKERS

,

Provider Override Reason: N/A - Order Entered Through VistA

VERB: TAKE

There are 2 Available Dosage(s):

1\. 240MG

2\. 480MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list:

Local Allergy/ADR – New Order Entry Backdoor - Only Drug Class defined.

Another New Order for PSOPATIENT, TEN? YES//

Eligibility: NSC

RX PATIENT STATUS: OPT NSC//

DRUG: PENICILLIN

  Lookup: GENERIC NAME

     1   PENICILLIN GK 5 MILLION UNIT VIAL INJ             AM110          

     2   PENICILLIN VK 250MG TAB           BWATC     AM110          

     3   PENICILLIN VK 500MG TAB             AM110       02-25-20      

     4   PENICILLIN VK SUSP 250MG/5ML             AM110         MAY BE TAKEN WIT

HOUT REGARD TO FOOD    

CHOOSE 1-4: 2  PENICILLIN VK 250MG TAB         BWATC     AM110          

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

A Drug-Allergy Reaction exists for this medication and/or class!

    Prospective Drug: PENICILLIN VK 250MG TAB

     Causative Agent: PENICILLIN (CLE13 TEST LAB - 06/18/02)

 Historical/Observed: HISTORICAL

            Severity: Not Entered

         Ingredients: PENICILLIN

      Signs/Symptoms: HIVES

          Drug Class: AM110 PENICILLIN-G RELATED PENICILLINS

   Provider Override Reason: N/A - Order Check Not Evaluated by Provider

Press Return to continue:

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please wait...

VERB: TAKE

There is 1 Available Dosage(s):

       1. 250MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 1 TABLET

You entered 1 TABLET is this correct? Yes//   YES

VERB: TAKE

ROUTE: PO//   ORAL      PO  MOUTH

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

BID BID TWICE A DAY

...OK? Yes// (Yes)

(TWICE A DAY LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

  
Local & Remote Allergy/ADR – Multi-ingredients, Pending Order

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/033.png)

> **NOTE:** Technicians do not get prompted for interventions.

ED Edit FN Finish

Select Item(s): Next Screen// NEXT SCREEN

Pending OP Orders (ROUTINE) Mar 24, 2008@21:56:03 Page: 2 of 3

PSOPATIENT,THREE \<A\>

PID: 000-00-0000 Ht(cm): 167.64 (06/10/1993)

DOB: FEB 2,1939 (69) Wt(kg): 68.18 (06/10/1993)

\+

\*(1) Orderable Item: SULFAMETHOXAZOLE/TRIMETHOPRIM TAB

\(2\) Drug: SULFAMETHOXAZOLE/TRIMETHOPRIM DS TAB

Verb: TAKE

\(3\) \*Dosage: 1 TABLET

\*Route: ORAL

\*Schedule: Q12H

\(4\) Pat Instruct:

Provider Comments:

Instructions: TAKE 1 TABLET PO Q12H

SIG: TAKE 1 TABLET BY MOUTH EVERY 12 HOURS

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: MAR 24,2008 (7) Fill Date: MAR 24,2008

\+ Enter ?? for more actions

BY Bypass DC Discontinue

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

Now doing allergy checks. Please wait...

A Drug-Allergy Reaction exists for this medication and/or class!

Prospective Drug: SULFAMETHOXAZOLE/TRIMETHOPRIM DS TAB

Causative Agent: SULFADIAZINE/SULFAMERAZINE/SULFAMETHAZINE (SITE REPORTING ALLERGY – DATA REPORTED)

Historical/Observed: HISTORICAL

Severity: Not Entered

Ingredients: SULFAMETHOXAZOLE TRIMETHOPRIM

Signs/Symptoms: ITCHING,WATERING EYES, ANOREXIA,

NAUSEA,VOMITING, ANXIETY, DROWSINESS,

### Provider Override Reason: N/A - Order Entered Through VistA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Therapeutic Duplication 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes enhancements to the existing VistA Duplicate Class order checks. The current VistA Duplicate Class checks have been enhanced using the FDB business rules and database, as well as the FDB Enhanced Therapeutic Classification (ETC) system. The Duplicate Class check will now be referred to as the Duplicate Therapy order check. This order check will continue to be performed against active, pending, non-verified orders on hold (initiated through pharmacy or CPRS), expired and discontinued orders. The timeframe for inclusion of locally discontinued orders is determined by the following formula: Discontinued Date (Cancel Date) + Days Supply + 7. This check will be performed on active Non-VA Medication orders.

No changes have been made to the existing user actions for Duplicate Therapy order checks. Users will continue to have the ability to discontinue the order. The existing order will only be discontinued upon acceptance of the order being processed. No discontinue actions can be performed on remote outpatient orders, Non-VA medications, discontinued, and expired orders or orders placed on provider hold through CPRS. If the CANCEL DRUG IN SAME CLASS outpatient site parameter is set to ‘No’, no discontinue action is allowed on any duplicate class order.

Any remote Outpatient order (from another VAMC or Department of Defense (DoD) facility) using data from Health Data Repository Historical (HDR-Hx) or Health Data Repository- Interim Messaging Solution (HDR-IMS) that has been expired for 30 days or less will be included in the list of medications to be checked.

FDB custom tables will be used to store custom changes to the duplication allowance for a FDB therapeutic classification. Each duplicate therapy class is assigned a duplication allowance. The duplication allowance for a therapeutic allowance determines whether or not the therapeutic duplication warning will be displayed to the user.

The Vendor's (currently FDB) Enhanced Therapeutic Classification (ETC) System is now used in place of the VA Drug Class for the Duplicate Therapy (formerly duplicate class) order checks.

Duplicate Therapy order checks will no longer be processed in pairs. Each duplicate therapy warning includes as many outpatient medication orders as it applies to.

A duplicate therapy warning is only displayed if the number of duplicate therapy matches exceeds the duplication allowance specified for the FDB duplicate therapy class.

The following processes use the enhanced functionality:

- Entering a new outpatient medication order through pharmacy options
- Finishing a pending outpatient medication order
- Renewing an outpatient medication order
- When a new outpatient medication order is created via an edit
- Verification of an outpatient medication order entered or finished by a non-pharmacist
- Copy of an outpatient medication order
- Reinstatement of an outpatient medication order

See illustrations below:

Example: Local RX

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* FAMOTIDINE 20MG TAB with

Local Rx#: 2561

Drug: CIMETIDINE 300MG TAB (DISCONTINUED)

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

QTY: 30 Days Supply: 30

Processing Status: Released locally on 3/4/08@08:55:32 (Window)

Last Filled On: 11/08/06

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

===============================================================================

Example: Remote Rx

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* SUCRALFATE 1GM TAB with

LOCATION: \<VA OR DOD FACILITY\> Remote Rx#: 65343

Drug: RANITIDINE HCL 150MG TAB (EXPIRED)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Last Filled On: 11/08/06

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents

===============================================================================

Example: Pending Order

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* NIZATIDINE 150MG CAP with

Pending Drug: FAMOTIDINE 20MG TAB

SIG: TAKE ONE TABLET BY TWICE DAILY

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents

===============================================================================

Example: Non-VA Med Order

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* FAMOTIDINE 20MG TAB with

Non-VA Med: CIMETIDINE 300MG TAB

Dosage: 300MG Schedule: TWICE A DAY

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

===============================================================================

If the CANCEL DRUG IN SAME CLASS outpatient site parameter is set to ‘No’, the following information is shown for the duplicate therapy warning:

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* NIZATIDINE 150MG CAP with

Local Rx \#2561 (ACTIVE) for CIMETIDINE 300MG TAB

Local Rx \#2572 (PROVIDER HOLD) for SUCRALFATE 1MG TAB

Remote Rx \#2571 (DISCONTINUED) for RANITIDINE HCL 150MG TAB

Pending Order for FAMOTIDINE 20MG TAB

Non-VA Med Order for CIMETIDINE 300MG TAB

Class(es)Involved in Therapeutic Duplication(s): PEPTIC ULCER AGENTS, HISTAMINE-2 RECEPTOR ANTAGOINSTS (H2 ANTAGONISTS)

===============================================================================

If there is more than one remote, local, pending or Non-VA med order involved in the therapeutic duplication, the order details will be displayed one after the other.

If the same drugs are involved in multiple therapeutic duplications, a single therapeutic duplication warning will be displayed and multiple therapeutic classes will be listed.

If the CANCEL DRUG IN SAME CLASS outpatient site parameter is set to ‘No’, no discontinue action prompt will be presented.

After all the therapeutic duplication warnings are displayed and if the CANCEL DRUG IN SAME CLASS outpatient site parameter is set to ‘Yes’, the user will be asked if they want to discontinue any of the orders.

See Examples:

Discontinue RX \#2580A SUCRALFATE 1GM TAB? Y/N

Discontinue Pending Order SUCRALFATE 1GM TAB? Y/N

The system will only allow a discontinuation action on active, pending, non-verified and orders placed on hold by pharmacy.

The system will display the following information for the numbered list of orders:

- Prescription number (if applicable)
- Dispense Drug (Orderable item if dispense drug not assigned to order)
- Indicate if the order is pending (with text ‘Pending Order’)

See example below:

1\. Pending order AMLODIPINE 5MG/ATORVASTATIN 10MG

2\. RX \#2426 LOVASTATIN 40MG TAB

The discontinuation of selected orders by the system will occur at the time the user accepts the order that is being processed.

Discontinue order(s)? Y/N Y es

1\. RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

2\. RX \#2581 CHOLESTYRAMINE 9GM PACKETS

Select (1-2): 1 Duplicate Therapy RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB will be discontinued after the acceptance of the new order.

Discontinue order(s)? Y/N Y es

1\. RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

2\. Pending Order CHOLESTYRAMINE 9GM PACKETS

Select (1-2): 2 Duplicate Therapy Pending Order CHOLESTYRAMINE 9GM PACKETS will be discontinued after the acceptance of the new order.

If the user fails to accept the order that is being processed or exits before accepting the order, the system will not discontinue the order(s) selected.

The message displayed to the user will contain:

- Indicate that discontinuance was for Duplicate Therapy
- The prescription number or text ‘Pending order’ if order status is pending.
- Dispense Drug (Orderable item if dispense drug not assigned to order)
- Ending with text ‘NOT Discontinued’

See examples below:

Duplicate Therapy RX \#2710 CIMETIDINE 300MG TAB NOT Discontinued.

Duplicate Therapy Pending Order RANITIDINE 150MG TAB NOT Discontinued.

Once the order being processed is accepted and there were orders selected for discontinuation, the system will inform the user when the discontinuation occurs.

The message displayed to the user will contain:

- An indication that discontinuance was for Duplicate Therapy
- The prescription number or text ‘Pending order’ if order status is pending.
- Dispense Drug (Orderable item if dispense drug not assigned to order)
- Ending with text ‘has been discontinued.’

See examples below:

Duplicate Therapy RX \#2549 CIMETIDINE 300MG TAB has been discontinued...

Duplicate Therapy Pending Order RANITIDINE 150MG TAB has been discontinued.

See Therapeutic Duplication examples below:

Example: Finishing pending order – Therapeutic Duplication with Non-VA med and discontinued order -No discontinue action allowed.

\*(1) Orderable Item: FAMOTIDINE TAB \*\*\*(N/F)\*\*\* \<DIN\>

\(2\) CMOP Drug: FAMOTIDINE 20MG TAB \*\*\*(N/F)\*\*\* \<DIN\>

NDC: 00056-0176-75

\(3\) \*Dosage: 20 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\+ Enter ?? for more actions

BY Bypass DC Discontinue

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

=============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* FAMOTIDINE 20MG TAB with

Local Rx#: 2561

Drug: CIMETIDINE 300MG TAB (DISCONTINUED)

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

QTY: 30 Days Supply: 30

Processing Status: Released locally on 3/4/08@08:55:32 (Window)

Last Filled On: 11/08/06

-----------------------------------------------------------------------------

Non-VA Med: CIMETIDINE 300MG TAB

Dosage: 300MG Schedule: TWICE A DAY

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

===============================================================================

Press Return to Continue:

Rx \# 2570 03/07/08

PSOPATIENT,ONE \#180

TAKE ONE TABLET BY MOUTH TWICE A DAY

FAMOTIDINE 20MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 3

SC Percent: 80%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? YES//

Are you sure you want to Accept this Order? NO//

Example: New Order Entry Backdoor – Therapeutic Duplication with pending and active order. Discontinue action shown.

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// no New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 80

RX PATIENT STATUS: SC//

DRUG: Nizatidine

Lookup: DRUG GENERIC NAME

NIZATIDINE 150MG CAP GA302

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* NIZATIDINE 150MG CAP with

Local Rx#: 2549

Drug: CIMETIDINE 300MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

QTY: 30 Days Supply: 30

Processing Status: Released locally on 3/4/09@08:55:32 (Window)

Last Filled On: 11/08/06

-------------------------------------------------------------------------------

Pending Drug: FAMOTIDINE 20MG TAB

SIG: TAKE ONE TABLET BY TWICE DAILY

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

==============================================================================

Discontinue order(s)? Y/N No

Press Return to Continue...

There are 2 Available Dosage(s):

1\. 150MG

2\. 300MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list:

.

.

OR

Discontinue order(s)? Y/N Y es

1\. Pending Order FAMOTIDINE 20MG TAB

2\. RX \#2549 CIMETIDINE 300MG TAB

Select (1-2): 2 Duplicate Therapy RX \#2549 CIMDTIDINE 300MG TAB will be discontinued after the acceptance of the new order.

There are 2 Available Dosage(s):

1\. 150MG

2\. 300MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 150MG

You entered 150MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 150MG

NOUN: TABLET

ROUTE: PO// ORAL PO MOUTH

Schedule:

This is a required response. Enter '^' to exit

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

BID BID TWICE A DAY

...OK? Yes// (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(TAKE ONE TABLET BY MOUTH TWO TIMES A DAY)

DAYS SUPPLY: (1-90): 60//

QTY ( ) : 360// 180

COPIES: 1// 1

\# OF REFILLS: (0-3): 3//

PROVIDER: PSOPROVIDER,ONE

CLINIC: BARB'S CLINIC 2

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

ISSUE DATE: TODAY// (MAR 12, 2008)

FILL DATE: (3/12/2008 - 3/13/2009): TODAY// (MAR 12, 2008)

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2580 03/12/08

PSOPATIENT,ONE \#180

TAKE ONE TABLET BY MOUTH TWO TIMES A DAY

NIZATIDINE 150MG CAP

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 3

SC Percent: 80%

Disabilities: NONE STATED

Was treatment for a Service Connected condition?

This is a required response. Enter '^' to exit

Was treatment for a Service Connected condition? NO

Is this correct? YES//

-Duplicate Therapy RX \#2549 CIMETIDINE 300MG TAB has been discontinued...

Another New Order for PSOPATIENT,ONE? YES//

Example: Finishing Pending Order – Therapeutic Duplication with Non-Verified and Active orders. One drug is involved in both therapeutic duplications. One duplication allowance value is greater than ‘0’.

-------------------------------------ACTIVE----------------------------------

1 2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB 90 A 03-07 03-07 3 90

2 2578 ITRACONAZOLE 100MG CAP 60 A 03-07 03-07 0 30

3 2576 SUCRALFATE 1MG TAB 120 A 03-07 03-07 0 30

----------------------------------NON-VERIFIED-------------------------------

4 2581 CHOLESTYRAMINE 9GM PACKETS 60 N 03-12 03-12 11 30

------------------------------------PENDING----------------------------------

5 SIMVASTATIN 20MG TAB QTY: 30 ISDT: 03-12 REF: 6

Enter ?? for more actions

ED Edit FN Finish

Pending OP Orders (ROUTINE) Mar 12, 2008@07:54:21 Page: 1 of 3

OPPATIENT, THREE \<A\>

PID: 666-44-4444 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JUL 3,1949 (58) Wt(kg): 51.36 (10/01/1996)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

CPRS Order Checks:

CRITICAL drug-drug interaction: ITRACONAZOLE & SIMVASTATIN

(ITRACONAZOLE CAP,ORAL 100MG TAKE ONE CAPSULE BY MOUTH EVERY 12 HOURS

\[ACTIVE\])

Overriding Provider: PSOPROVIDER,ONE

Overriding Reason: TESTING

CRITICAL drug-drug interaction: ITRACONAZOLE & SIMVASTATIN

ITRACONAZOLE CAP,ORAL 100MG PO BID \[ACTIVE\])

Overriding Provider: PSOPROVIDER,ONE

Overriding Reason: TESTING

Duplicate drug class order: ANTILIPEMIC AGENTS (CHOLESTYRAMINE 9GM

PACKETS TAKE ONE PACKET BY MOUTH TWICE A DAY DISSOLVE IN WATER OR

JUICE. \[PENDING\])

\+ Enter ?? for more actions

BY Bypass DC Discontinue

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

=============================================================================

THERAPEUTIC DUPLICATION(S) \*\*\* SIMVASTATIN 20MG TAB with

Local Rx#: 2577

Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 90 Days Supply: 90

Processing Status: Released locally on 3/7/08@08:55:32 (Window)

Last Filled On: 03/07/08

Local Rx#: 2581

Drug: CHOLESTYRAMINE 9GM PACKETS (NON-VERIFIED)

SIG: TAKE ONE PACKET BY MOUTH TWICE A DAY DISSOLVE IN WATER

OR JUICE.

QTY: 60 Days Supply: 30

Processing Status: Not released locally (Window)

Last Filled On: 11/08/06

Class(es)Involved in Therapeutic Duplication(s): HMGCo-A Reductase Inhibitors, Antihyperlipidemics

==============================================================================

Discontinue order(s)? Y/N Y es

1\. RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

2\. RX \#2581 CHOLESTYRAMINE 9GM PACKETS

Select (1-2): 1 Duplicate Therapy RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB will be discontinued after the acceptance of the new order.

Rx \# 2582 03/12/08

TEST,D \#30

TAKE ONE TABLET BY MOUTH EVERY EVENING

SIMVASTATIN 20MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 6

This Rx has been flagged by the provider as: NO COPAY

Was treatment related to Agent Orange exposure? YES//

Are you sure you want to Accept this Order? NO// YES

METHOD OF PICK-UP:

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

-Duplicate Therapy RX \#2577 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB has been discontinued...

Press Return to Continue:

Example: Renewing an order –Therapeutic Duplication involving 5 drugs, one therapy class and only one order can be discontinued.

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// rn Renew

FILL DATE: (3/12/2008 - 3/13/2009): TODAY// (MAR 12, 2008)

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Now Renewing Rx \# 2580 Drug: SUCRALFATE 1GM TAB

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* SUCRALFATE 1GM TAB with

Local Rx#: 2574

Drug: CIMETIDINE 300MG TAB (DISCONTINUED)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Processing Status: Released locally on 3/7/08@08:55:32 (Window)

Last Filled On: 03/07/08

Local Rx#: 2573

Drug: NIZATIDINE 150MG CAP (HOLD)

SIG: TAKE ONE CAPSULE BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Processing Status: Released locally on 3/7/08@08:55:32 (Window)

Last Filled On: 03/07/08

LOCATION: \<VA OR DOD FACILITY\> Remote Rx#: 65343

Drug: RANITIDINE HCL 150MG TAB (EXPIRED)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 180 Days Supply: 90

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

==============================================================================

Discontinue RX \#2573 NIZATIDINE 150MG CAP? Y/N No

Press Return to Continue:

2580A SUCRALFATE 1MG TAB QTY: 360

\# OF REFILLS: 3 ISSUED: 03-12-08

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY

FILLED: 03-12-08

ROUTING: WINDOW PHYS: PSOPROVIDER,ONE

Edit renewed Rx ? Y// n NO

SC Percent: 80%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO//

Example: Verification of Non-Verified Order

OP Medications (NON-VERIFIED) Dec 20, 2011@14:45:54 Page: 1 of 2

PSOPATIENT,ONE \<A\>

PID: 666-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 1,1945 (66) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 2382\$

\(1\) \*Orderable Item: NIZATIDINE CAP,ORAL

\(2\) Drug: NIZATIDINE 150MG CAP

NDC: 00056-0176-75

\(3\) \*Dosage: 150 (MG)

Verb: TAKE

Dispense Units: 1

Noun: CAPSULE

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE ONE CAPSULE BY BY MOUTH TWICE A DAY

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 12/20/11 (7) Fill Date: 12/20/11

Last Fill Date: 12/20/11 (Window)

\+ Enter ?? for more actions

DC Discontinue PR (Partial) RL (Release)

ED Edit RF (Refill) RN (Renew)

Select Action: Next Screen// VF VF

RX: 2382 PATIENT: PSOPATIENT,ONE (666-00-0000)

STATUS: Non-Verified CO-PAY STATUS

DRUG: NIZATIDINE 150MG CAP

QTY: 180 90 DAY SUPPLY

SIG: TAKE ONE CAPSULE BY MOUTH TWICE A DAY

LATEST: 12/20/2011 \# OF REFILLS: 3 REMAINING: 3

ISSUED: 12/20/11 PROVIDER:

LOGGED: 12/20/11 CLINIC: NOT ON FILE

EXPIRES: 12/20/12 DIVISION: HINES (499)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PSTECH,ONE VERIFIED BY:

EDIT: (Y/N/P): N// O

PSOPATIENT,ONE ID#:666-00-0000 RX#: 2382

ISSUE LAST REF DAY

RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------------------------------------------------

-------------------------------------ACTIVE------------------------------------

2380\$ ACETAMINOPHEN 325MG TAB U.D. 540 A 12-20 12-20 3 90

2379\$ WARFARIN 2.5MG TABS 90 A 12-20 12-20 3 90

----------------------------------DISCONTINUED---------------------------------

2378\$ INDOMETHACIN 25MG CAP 270 DC 12-20 12-20 3 90

2377\$ WARFARIN 10MG TABS 2160 DC 12-20 12-20 3 90

----------------------------------NON-VERIFIED---------------------------------

2382\$ NIZATIDINE 150MG CAP 180 N 12-20 12-20 3 90

2381\$ SUCRALFATE 1 GM TAB 360 N 12-20 12-20 3 90

Press Return to continue:

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

> Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* NIZATIDINE 150MG CAP with

Local RX#: 2381

Drug: SUCRALFATE 1 GM TAB (Non-Verified)

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY

QTY: 360 Days Supply: 90

Processing Status: Not released locally (Window)

Last Filled On: 12/20/11

Class(es) Involved in Therapeutic Duplication(s): Peptic Ulcer Agents

===============================================================================

Press Return to continue:

Discontinue Rx \#2381 SUCRALFATE 1 GM TAB Y/N ? NO

PSOPATIENT,ONE ID#:666-00-0000 RX#: 2382

NIZATIDINE 150MG CAP

VERIFY FOR PSOPATIENT,ONE ? (Y/N/Delete/Quit): Y// ES

Example: Copying an Existing Order

New OP Order (COPY) Mar 12, 2008@09:15:48 Page: 1 of 2

PSOPATIENT,TWO \<A\>

PID: 000-00-0000 Ht(cm): 182.88 (04/13/2005)

DOB: JAN 1,1945 (63) Wt(kg): 77.27 (04/13/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

Orderable Item: AMLODIPINE/ATORVASTATIN TAB

\(1\) Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: MAR 12,2008 (4) Fill Date: MAR 12,2008

Verb: TAKE

\(5\) Dosage Ordered: ONE TABLET

Route: ORAL

Schedule: QAM

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(7\) Days Supply: 30 (8) QTY ( ): 30

\(9\) \# of Refills: 11 (10) Routing: WINDOW

\(11\) Clinic:

\(12\) Provider: PSOPROVIDER,ONE (13) Copies: 1

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

-----------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 2584

Drug: AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

QTY: 30 Refills remaining: 11

Provider: OPPROVIDER, ONE Issued: 03/12/07

Status: ACTIVE Last filled on: 03/12/07

Processing Status: Released locally on 03/12/07@08:55:32 (Window)

Days Supply: 30

-----------------------------------------------------------------------------

Discontinue Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB? Y/N YES

Rx \#2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB will be discontinued after the acceptance of the new order.

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* AMLODIPINE 5MG/ATORVASTATIN 10MG TAB with

Pending Drug: LOVASTATIN 20MG TAB

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME FOR HIGH CHOLESTEROL

Pending Drug: NIFEDIPINE 10MG CAP

SIG: TAKE ONE CAPSULE BY MOUTH THREE TIMES A DAY

Class(es)Involved in Therapeutic Duplication(s): Calcium Channel Blockers, HMGCo-A Reductase Inhibitors

==============================================================================

Discontinue order(s)? Y/N Y es

1\. Pending Order NIFEDIPINE 10MG CAP

2\. Pending Order LOVASTATIN 20MG TAB

Select (1-2): 1-2 Pending Order NIFEDIPINE 10MG CAP will be discontinued after the acceptance of the new order.

Pending Order LOVASTATIN 20MG TAB will be discontinued after the acceptance of the new order.

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2585 03/12/08

PSOPATIENT,TWO T \#30

TAKE ONE TABLET BY MOUTH EVERY MORNING

AMLODIPINE 5MG/ATORVASTATIN 10MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 11

SC Percent: 40%

Disabilities: NONE STATED

Was treatment for Service Connected condition? NO//

Is this correct? YES// ...

Duplicate Drug Rx 2584 AMLODIPINE 5MG/ATORVASTATIN 10MG TAB has been discontinued…

Duplicate Therapy Pending Order NIFEDIPINE 10MG CAP has been discontinued…

Duplicate Therapy Pending Order LOVASTATIN 20MG TAB has been discontinued…

Example: Reinstating a Discontinued Order

Rx \#: 2586

(1) \*Orderable Item: CIMETIDINE TAB

\(2\) Drug: CIMETIDINE 300MG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 300 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: QHS

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/12/08 (7) Fill Date: 03/12/08

Last Fill Date: 03/12/08 (Window)

\+ Enter ?? for more actions

DC Discontinue PR (Partial) RL Release

ED (Edit) RF (Refill) RN Renew

Select Action: Next Screen// dc Discontinue

Are you sure you want to Reinstate? NO// YES

Comments: REINSTATING

Nature of Order: SERVICE CORRECTION//        S

================================================================================

2586            CIMETIDINE 300MG TAB

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please wait...

==============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* CIMETIDINE 300MG TAB with

Local Rx#: 2576

Drug: SUCRALFATE 1GM TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY

QTY: 1200 Days Supply: 30

Processing Status: Released locally on 3/7/08@08:55:32 (Window)

Last Filled On: 03/07/08

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents

=============================================================================

Discontinue RX \# 2576 SUCRALFATE 1GM TAB? Y/N NO - Prescription was not discontinued...

Prescription \#2586 REINSTATED!

Prescription \#2586 Filled: MAR 12, 2008Printed: Released:

Either print the label using the reprint option

or check later to see if the label has been printed.

Example: Creating a New Order – Editing the Orderable Item

Rx \#: 2594

\(1\) \*Orderable Item: ENALAPRIL TAB \*\*\*(N/F)\*\*\*

\(2\) Drug: ENALAPRIL 5MG TAB \*\*\*(N/F)\*\*\*

NDC: 00056-0176-75

\(3\) \*Dosage: 5 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: QAM

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH EVERY MORNING

\(5\) Patient Status: SC

\(6\) Issue Date: 03/12/08 (7) Fill Date: 03/12/08

Last Fill Date: 03/12/08 (Window)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// 1

Current Orderable Item: ENALAPRIL TAB

Select PHARMACY ORDERABLE ITEM NAME: ENALAPRIL// dip

1 DIPHENHYDRAMINE CREAM,TOP

2 DIPHENHYDRAMINE CAP,ORAL

3 DIPYRIDAMOLE TAB

CHOOSE 1-3: 3 DIPYRIDAMOLE TAB

New Orderable Item selected. This edit will create a new prescription!

Press Return to Continue...

DRUG NAME REQUIRED!

Instructions:

The following Drug(s) are available for selection:

1\. DIPYRIDAMOLE 25MG TAB

2\. DIPYRIDAMOLE 50MG TAB

Select Drug by number: (1-2): 1

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

==============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* DIPYRIDAMOLE 25MG TAB with

Local Rx#: 2560

Drug: WAFFARIN 5MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

QTY: 90 Days Supply: 90

Processing Status: Released locally on 3/4/08@08:55:32 (Window)

Last Filled On: 03/04/08

Class(es)Involved in Therapeutic Duplication(s): Antiplatelet Drugs, Antithrombotic Drugs

===============================================================================

Discontinue RX \# 2560 WAFFARIN 5MG TAB? Y/N NO -Prescription was not discontinued...

You have changed the Orderable Item from ENALAPRIL to

DIPYRIDAMOLE.

There are 2 Available Dosage(s):

1\. 25MG

2\. 50MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 25MG

You entered 25MG is this correct? Yes// YES

VERB: TAKE// TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 25MG

NOUN: TABLET// TABLET

ROUTE: ORAL// ORAL

Schedule: QAM// TID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

TID TID THREE TIMES A DAY

...OK? Yes// (Yes)

(THREE TIMES A DAY)

LIMITED DURATION (IN MONTHS, WEEKS, DAYS, HOURS OR MINUTES):

CONJUNCTION:

New OP Order (ROUTINE) Mar 12, 2008@10:58:24 Page: 1 of 2

PSOPATIENT,ONE \<A\>

PID: 666-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 1,1910 (98) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE Non-VA Meds on File Last entry on 03/03/08

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Orderable Item: DIPYRIDAMOLE TAB

\(1\) Drug: DIPYRIDAMOLE 25MG TAB

\(2\) Patient Status: SC

\(3\) Issue Date: MAR 12,2008 (4) Fill Date: MAR 12,2008

\(5\) Dosage Ordered: 25 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

Route: ORAL

Schedule: TID

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH THREE TIMES A DAY

\(7\) Days Supply: 90 (8) QTY (TAB): 180

\(9\) \# of Refills: 3 (10) Routing: WINDOW

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// ac Accept

Nature of Order: SERVICE CORRECTION// S

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2595 03/12/08

PSOPATIENT,ONE \#180

TAKE ONE TABLET BY MOUTH THREE TIMES A DAY

DIPYRIDAMOLE 25MG TAB

PSOPROVIDER,ONE PSOPHARMACIST,ONE

\# of Refills: 3

The Pharmacy Orderable Item has changed for this order. Please review any

existing SC or Environmental Indicator defaults carefully for appropriateness.

SC Percent: 80%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? YES//

Is this correct? YES// ...

  
Example: Cancel drug in same class parameter set to No

PSOPATIENT,ONE \<A\>

PID: 666-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 1,1910 (98) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE Non-VA Meds on File Last entry on 03/03/08

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE----------------------------------

1 2562 AMINOPHYLLINE 200MG TAB 360 A 03-04 03-04 3 90

2 2567 CAPTOPRIL 12.5MG TAB 180 A 03-06 03-06 3 90

3 2563 CISAPRIDE 10MG 90 A 03-06 03-06 3 90

4 2568 DIGOXIN 0.125MG 30 A 03-06 03-06 3 90

5 2550 IBUPROFEN 600MG TAB 270 A 03-03 03-04 3 90

6 2560 WARFARIN 5MG TAB 90 A 03-04 03-04 3 90

----------------------------------DISCONTINUED-------------------------------

7 2561 CIMETIDINE 300MG TAB 90 DC 03-04 03-04 3 90

--------------------------------------HOLD-----------------------------------

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 80

RX PATIENT STATUS: SC//

DRUG: NIZATIDINE

Lookup: GENERIC NAME

NIZATIDINE 150MG CAP GA301

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

=======================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* NIZATIDINE 150MG CAP with

Local Rx \#2561 (ACTIVE) for CIMETIDINE 300MG TAB

Local Rx \#2572 (PROVIDER HOLD) for SUCRALFATE 1MG TAB

Remote Rx \#2571 (DISCONTINUED) for RANITIDINE HCL 150MG TAB

Pending Order FAMOTIDINE 20MG TAB

Non-VA Med Order for CIMETIDINE 300MG TAB

Class(es) Involved in Therapeutic Duplication(s): PEPTIC ULCER AGENTS, HISTAMINE-2 RECEPTOR ANTAGOINSTS (H2 ANTAGONISTS)

=============================================================================

VERB: TAKE

There are 2 Available Dosage(s):

1\. 150MG

2\. 300MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list:

  
Example: Entering a New Order – Not accepting order, duplicate therapy not discontinued

Select Action: Quit// NO New Order

Eligibility: NSC SC%: 5

RX PATIENT STATUS: OPT NSC//

DRUG: FAMOTIDINE

Lookup: GENERIC NAME

FAMOTIDINE 20MG TAB GA301

...OK? Yes// (Yes)

Restriction/Guideline(s) exist. Display? : (N/D/O/B): No// NO

Now doing remote order checks. Please wait...

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* FAMOTIDINE 20MG TAB with

Local RX#: 2586A

Drug: CIMETIDINE 300MG TAB (DISCONTINUED)

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

QTY: 90 Days Supply: 30

Processing Status: Released locally on 3/12/08@08:55:32 (Window)

Last Filled On: 03/12/08

Press Return to Continue:

Local RX#: 2710

Drug: RANITIDINE HCL 150MG TAB (ACTIVE)

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 60 Days Supply: 30

Processing Status: Released locally on 6/1/09@08:55:32 (Window)

Last Filled On: 06/01/09

Press Return to Continue:

Class(es)Involved in Therapeutic Duplication(s): Peptic Ulcer Agents, Histamine-2 Receptor Antagonists (H2 Antagonists)

===============================================================================

Press Return to Continue:

Discontinue Rx \#2710 for RANITIDINE HCL 150MG TAB Y/N ? YES

Duplicate Therapy RX \#2710 RANITIDINE HCL 150MG TAB will be discontinued after the acceptance of the new order.

===============================================================================

VERB: TAKE

There are 2 Available Dosage(s):

1\. 20MG

2\. 40MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 20MG

You entered 20MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 20MG

NOUN: TABLET

ROUTE: PO// ORAL PO MOUTH

Schedule: BID// QAM

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QAM QAM EVERY MORNING

...OK? Yes// (Yes)

(EVERY MORNING)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(TAKE ONE TABLET BY MOUTH EVERY MORNING )

DAYS SUPPLY: (1-90): 30// ^

RX DELETED

Duplicate Therapy RX \#2710 RANITIDINE HCL 150MG TAB NOT Discontinued.

### Dosing Order Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.0 implements the first increment of dosage checks and introduces the Maximum Single Dose Check for simple and complex orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.1b implements the second increment of dosage checks and introduces the Max Daily Dose Check for simple orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.0 and MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/034.png)Please refer to the *Dosing Order Checks User Manual* for a detailed description of dosing order checks.

### CPRS Order Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three CPRS order checks have been added to the list of order checks performed within the Outpatient Pharmacy application.

- Aminoglycoside Ordered
- Dangerous Meds for Patient \>64
- Glucophage –Lab Results

The CPRS order checks shall be incorporated in the following Outpatient Pharmacy order entry processes:

- Entering a new order via backdoor pharmacy options
- Finishing a pending order
- Renewing an order
- Editing an order which results in a new order being created.
- Verifying an order
- Copying an order
- Reinstating a discontinued order

No user action/intervention shall be required after a CPRS order check warning is displayed.

The following information is displayed for the Aminoglycoside Ordered order check:

- Order Check Name
- Text message displaying an estimated CrCL if available or a message that it is not

\*\*\*Aminoglycoside Ordered\*\*\*

Aminoglycoside - est. CrCl: \<VALUE\> (CREAT: \<result\>  BUN: \<result\>) \[Est. CrCl

Based on modified Cockcroft-Gault equation using Adjusted Body Weight (if ht \> 60 in)\].

-OR-

\*\*\*Aminoglycoside Ordered\*\*\*

Aminoglycoside – est. CrCl: \<Unavailable\> (\<Results Not Found\>)  \[Est. CrCl

Based on modified Cockcroft-Gault equation using Adjusted Body Weight (if ht \> 60

The following information is displayed for the Dangerous Meds for Patient \>64 order check:

- Order Check Name
- Text message displaying a message if patient is greater than 64 and has been prescribed Amitriptyline

\*\*\*Dangerous Meds for Patient \>64\*\*\*

Patient is \<age\>.  Amitriptyline can cause cognitive impairment and loss of balance in older patients.  Consider other antidepressant medications on formulary.

-OR-

Text message displaying a message if patient is greater than 64 and has been prescribed Chlorpropamide

\*\*\*Dangerous Meds for Patient \>64\*\*\*

Patient is \<age\>.  Older patients may experience hypoglycemia with Chlorpropamide due do its long duration and variable renal secretion. They may also be at increased risk for Chlorpropamide-induced SIADH.

-OR-

Text message displaying a message if patient is greater than 64 and has been prescribed Dipyridamole

\*\*\*Dangerous Meds for Patient \>64\*\*\*

Patient is \<age\>.  Older patients can experience adverse reactions at high doses of Dipyridamole (e.g., headache, dizziness, syncope, GI intolerance.)  There is also questionable efficacy at lower doses.

The following information is displayed for the Glucophage Lab Results order check:

- Order Check Name
- Text message displaying a serum creatinine does not exist or it is greater than 1.5

\*\*\*Metformin Lab Results\*\*\*

Metformin - no serum creatinine within past 60 days.

-OR-

\*\*\*Metformin Lab Results\*\*\*

Metformin – Creatinine results: \<creatinine greater than 1.5 w/in past \<x\> days\>

Examples of CPRS Order Checks

<span id="Page_103" class="anchor"></span>New Order Entry – Backdoor – Dangerous Meds for Patient \> 64 for Dipyridamole

Select Action: Quit// NO New Order

Eligibility: NSC

RX PATIENT STATUS: OPT NSC//

DRUG: DIPYRIDAMOLE

Lookup: GENERIC NAME

1 DIPYRIDAMOLE 25MG TAB BL117

2 DIPYRIDAMOLE 50MG TAB BL117

CHOOSE 1-2: 1 DIPYRIDAMOLE 25MG TAB BL117

\*\*\*DANGEROUS MEDS FOR PATIENT \>64\*\*\*

Patient is 78. Older patients can experience adverse reactions at high doses of Dipyridamole (e.g., headache, dizziness, syncope, GI intolerance.) There is also questionable efficacy at lower doses.

VERB: TAKE

There are 2 Available Dosage(s):

1\. 25MG

2\. 50MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 25MG

You entered 25MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// 1

Dosage Ordered: 25MG

NOUN: TABLET

ROUTE: PO//

Renewing an Order – Dangerous Meds for Patient \>64 for Chlorpropamide

Rx \#: 2613\$

\(1\) \*Orderable Item: CHLORPROPAMIDE TAB

\(2\) Drug: CHLORPROPAMIDE 25OMG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 250 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/25/08 (7) Fill Date: 03/25/08

Last Fill Date: 03/25/08 (Mail)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// RN Renew

FILL DATE: (3/25/2008 - 3/26/2009): TODAY// (MAR 25, 2008)

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Now Renewing Rx \# 2613 Drug: CHLORPROPAMIDE 25OMG TAB

\*\*\*DANGEROUS MEDS FOR PATIENT \>64\*\*\*

Patient is 78. Older patients may experience hypoglycemia with Chlorpropamide due do its long duration and variable renal secretion. They may also be at increased risk for Chlorpropamide-induced SIADH.

2613A CHLORPROPAMIDE 25OMG TAB QTY: 60

\# OF REFILLS: 3 ISSUED: 03-25-08

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

Creating New Order from Edit – Glucophage Lab Results for Metformin

\*(1) Orderable Item: METFORMIN TAB,ORAL

\(2\) Drug: METFORMIN 500MG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 500 (MG)

Verb: TAKE

ED Edit FN Finish

Select Item(s): Next Screen// NEXT SCREEN

BY Bypass DC Discontinue

Pending OP Orders (ROUTINE) Mar 25, 2008@15:33:47 Page: 2 of 3

PSOPATIENT,NINE \<A\>

PID: 000-00-0000 Ht(cm): 177.80 (10/14/2005)

DOB: JAN 1,1930 (78) Wt(kg): 136.36 (10/14/2005)

\+

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: Q12H

\(4\) Pat Instruct:

Provider Comments:

Instructions: TAKE ONE TABLET PO Q12H

SIG: TAKE ONE TABLET BY MOUTH EVERY 12 HOURS

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: MAR 25,2008 (7) Fill Date: MAR 25,2008

\(8\) Days Supply: 30 (9) QTY (TAB): 60

Provider ordered 2 refills

\(10\) \# of Refills: 2 (11) Routing: MAIL

\(12\) Clinic: BARB'S CLINIC

\+ Enter ?? for more actions

ED Edit FN Finish

Select Item(s): Next Screen// ED Edit

\* Indicates which fields will create an new Order

Select Field to Edit by number: (1-15): 3

Press Return to :

There are 2 Available Dosage(s):

1\. 500MG

2\. 1000MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 500MG// 2 1000MG

You entered 1000MG is this correct? Yes// YES

VERB: TAKE// TAKE

DISPENSE UNITS PER DOSE(TABLETS): 2// 2

Dosage Ordered: 1000MG

NOUN: TABLETS// TABLETS

ROUTE: ORAL// ORAL

Schedule: Q12H// QHS

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QHS QHS AT BEDTIME

...OK? Yes// (Yes)

(AT BEDTIME)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Pending OP Orders (ROUTINE) Mar 25, 2008@15:34:08 Page: 1 of 3

PSOPATIENT,NINE \<A\>

PID: 000-00-0000 Ht(cm): 177.80 (10/14/2005)

DOB: JAN 1,1930 (78) Wt(kg): 136.36 (10/14/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

CPRS Order Checks:

Duplicate drug class order: ORAL HYPOGLYCEMIC AGENTS,ORAL (CHLORPROPAMIDE

TAB 250MG TAKE ONE TABLET BY MOUTH TWICE A DAY \[PENDING\])

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: testing

Metformin - no serum creatinine within past 60 days.

Overriding Provider: PSOPROVIDER,TEN

Overriding Reason: testing

\*(1) Orderable Item: METFORMIN TAB,ORAL

\(2\) Drug: METFORMIN 500MG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 1000 (MG)

Verb: TAKE

\+ This change will create a new prescription!

AC Accept ED Edit DC Discontinue

Select Item(s): Next Screen// AC Accept

\*\*\*Metformin Lab Results\*\*\*

Metformin - no serum creatinine within past 60 days. 

Rx \# 2614 03/25/08

PSOPATIENT,NINE \#1440

TAKE TWO TABLETS BY MOUTH AT BEDTIME

METFORMIN 500MG TAB

PSOPROVIDER,TEN PSOPHARMACIST,22

\# of Refills: 2

Are you sure you want to Accept this Order? NO// YES

Nature of Order: SERVICE CORRECTION//

Copying an Order – Aminoglycoside Ordered - Gentamicin

Select Action: Next Screen// CO CO

OP Medications (ACTIVE) Mar 25, 2008@15:46:18 Page: 1 of 2

PSOPATIENT,NINE \<A\>

PID: 000-00-0000 Ht(cm): 177.80 (10/14/2005)

DOB: JAN 1,1930 (78) Wt(kg): 136.36 (10/14/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

Rx \#: 2616\$

\(1\) \*Orderable Item: GENTAMICIN INJ,SOLN

\(2\) Drug: GENTAMICIN 40MG/ML 2ML VI

Verb: INJECT

\(3\) \*Dosage: 80MG

\*Route: INTRAMUSCULAR

\*Schedule: Q8H

(4)Pat Instructions:

SIG: INJECT 80MG IM EVERY 8 HOURS

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 03/25/08 (7) Fill Date: 03/25/08

Last Fill Date: 03/25/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 04/24/08 MFG:

\+ Enter ?? for more actions

AC Accept ED Edit

New OP Order (COPY) Mar 25, 2008@15:46:18 Page: 1 of 2

PSOPATIENT,NINE \<A\>

PID: 000-00-0000 Ht(cm): 177.80 (10/14/2005)

DOB: JAN 1,1930 (78) Wt(kg): 136.36 (10/14/2005)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.78

Orderable Item: GENTAMICIN INJ,SOLN

\(1\) Drug: GENTAMICIN 40MG/ML 2ML VI

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: MAR 25,2008 (4) Fill Date: MAR 25,2008

Verb: INJECT

\(5\) Dosage Ordered: 80MG

Route: INTRAMUSCULAR

Schedule: Q8H

(6)Pat Instruction:

SIG: INJECT 80MG IM EVERY 8 HOURS

\(7\) Days Supply: 10 (8) QTY (VI): 10

\(9\) \# of Refills: 0 (10) Routing: WINDOW

\(11\) Clinic: SHIRL-2

\(12\) Provider: PSOPROVIDER,TEN (13) Copies: 1

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

\*\*\*Aminoglycoside Ordered\*\*\*

 

Aminoglycoside - est. CrCl: \<Unavailable\> (\<Results Not Found\>)  \[Est.

CrCl based on modified Cockcroft-Gault equation using Adjusted Body

Weight (if ht \> 60 in)\]

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 2617 03/25/08

PSOPATIENT,NINE \#10

INJECT 80MG IM EVERY 8 HOURS

GENTAMICIN 40MG/ML 2ML VI

PSOPROVIDER,TEN PSOPHARMACIST,22

\# of Refills: 0

Is this correct? YES//

Reinstating a Discontinued Order – Glucophage Lab Results for Metformin

                Rx \#: 2614\$                                                    

 (1) \*Orderable Item: METFORMIN TAB,ORAL                                        

 (2)            Drug: METFORMIN 500MG TAB 

                 NDC: 00056-0176-75                                    

 (3)         \*Dosage: 1000 (MG)                                                

                Verb: TAKE                                                      

      Dispense Units: 2                                                        

                Noun: TABLETS                                                  

              \*Route: ORAL                                                      

           \*Schedule: QHS                                                      

 (4)Pat Instructions:                                                          

                 SIG: TAKE TWO TABLETS BY MOUTH AT BEDTIME                      

 (5)  Patient Status: OPT NSC                                                  

 (6)      Issue Date: 03/25/08               (7)  Fill Date: 03/25/08          

      Last Fill Date: 03/25/08 (Mail)                                           
+         Enter ?? for more actions                                            

DC   Discontinue          PR   (Partial)            RL   Release

ED   (Edit)               RF   (Refill)             RN   Renew

Select Action: Next Screen// DC   Discontinue 

Are you sure you want to Reinstate? NO// YES

Comments: TESTING

Nature of Order: SERVICE CORRECTION//        S

================================================================================ 2614 METFORMIN 500MG TAB

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

\*\*\*Metformin Lab Results\*\*\*

Metformin – Creatinine results: \<creatinine greater than 1.5 w/in past \<7\> days\>

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please wait...

Prescription \#2614 REINSTATED!

   Prescription \#2614

Filled: MAR 25, 2008    Printed: MAR 25, 2008      Released:

     Either print the label using the reprint option

       or check later to see if the label has been printed.

The list of available possible dosages shown after order checks is linked to the drug ordered. One of the dosages listed may be chosen or a different, free text dosage may be entered. Confirmation of the dosage is required and the value entered is displayed again to allow the user to confirm that it is correct.

With patch PSO\*7\*402, there were changes made to the display of the available dosage list to break only after the third dosage. Text changes were also made to existing prompts (with or without a page break) to inform a user of the number of dosages defined for the drug selected and that more dosages exist should a break occur. Text changes were also made when no dosages are available.

<span id="Page_108" class="anchor"></span>Example: Entering a New Order (continued)

There are 3 Available Dosage(s):

1\. 250MG

2\. 500MG

3\. 1000MG

Select from list of Available Dosages (1-3), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 3 500MG

You entered 500MG is this correct? Yes// \<Enter\> YES

Break only after 3 dosages with text changes

There are 5 Available Dosage(s):

       1. 10MG
       2. 20MG
       3. 40MG

Enter RETURN to view additional dosages or ‘^’ to exit list of dosages:

-----------------------------\<Page Break\>------------------------------------

       4. 80MG
       5. 120MG

Select from list of Available Dosages (1-5), Enter Free Text Dose

or Enter a Question Mark (?) to view list:

<u>No Available Dosages</u>

There are NO Available Dosage(s).

Please Enter a Free Text Dose:

For numeric dosages, the Dispense Units Per Dose value is calculated based on the strength of the dosage ordered divided by the strength of the medication ordered. The 500 mg dosage ordered will require two 250 mg capsules. The Dosage Ordered is re-displayed after the Dispense Units to allow the entry to be double-checked.

DISPENSE UNITS PER DOSE(CAPSULES): 2// \<Enter\> 2

Dosage Ordered: 500MG

If a Route has not been associated with the Dispense Drug, the default Route of PO or Oral will be displayed. A different Route can be entered or it can be deleted at this point if needed. The Route is not required to complete a prescription. If the abbreviation entered is in the stored list of possible routes, the entry will be expanded in the Sig.

ROUTE: PO// \<Enter\> ORAL PO MOUTH

or

ROUTE: PO// @ \<Enter to delete\>

A default schedule associated with the drug ordered is displayed. The default can be accepted or a different free text schedule can be entered. Free text entries cannot contain more than two spaces or be more than twenty characters long. Entries will be compared against a list of common abbreviations and expanded if the entry matches. Any entry not found in the list of common abbreviations will be displayed in the Sig as entered.

With patch PSO\*7\*402, the user will be informed from which file the schedule selection is made and if the value entered will be considered as free text. The NAME, OLD SCHEDULE NAME(S) fields will be used for lookup from the ADMNISTRATION SCHEDULE file. The NAME, SYNONYM and OLD MED INSTRUCTION NAME(S) fields will be used for lookup from the MEDICATION INSTRUCTION file. The user will first be presented with selections from the ADMINISTRATION SCHEDULE file based on the value entered at the schedule prompt. If the user selects an entry, the lookup is complete. If the user chooses not to select a value from the ADMINISTRATION SCHEDULE file, the software displays selections from the MEDICATION INSTRUCTION file. If a selection is made, the lookup is complete. If the user chooses not to select a value, the software informs the user that the value as entered will be accepted at the schedule prompt as a free text entry.

> Schedule: BID

> Now searching ADMINISTRATION SCHEDULE (#51.1) file...

> BID BID TWICE A DAY

> ...OK? Yes// N (No)

> 1 BID EXCLUDE MDD BID

> 2 BID PRN BID

> 3 BID-AM BID

> 4 BID-NOON BID

> 5 BID-W/MEAL BID

> Press \<Enter\> to see more, '^' to exit this list, OR

> CHOOSE 1-5:

> 6 BID2 PRN BID

> CHOOSE 1-6:

> Now searching MEDICATION INSTRUCTION (#51) file...

> BID TWICE A DAY

> ...OK? Yes// N (No)

> AP BIDAP TWICE A DAY IN MORNING AND EVENING

> ...OK? Yes// N (No)

> Free text 'BID' entered for schedule (TWICE A DAY)

The LIMITED DURATION field is used only when a medication should be taken for a limited period of time. Days are assumed for numeric entries. Follow the number with an “H” to specify hours or an “M” to specify minutes.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/035.png)

> **NOTE:** Do not use this field for Days Supply.

Example: Entering a New Order (continued)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 10 (DAYS)

The CONJUCTION field is used to join dosing sequences in complex orders. Entries are limited to AND or <span id="p477_116_Remove_Except_ref" class="anchor"></span>THEN. AND is used for concurrent doses, such as “Take 1 tablet every morning AND take 2 tablets at bedtime.” THEN is used for consecutive doses, such as “Take 2 tablets daily for one week THEN take 1 tablet for five days.” See Chapter 2 in the *User Manual - Supplemental* for examples.

CONJUNCTION: \<Enter\>

Any entry in the PATIENT INSTRUCTIONS field will first be checked to see if it contains any abbreviations that can be expanded. The entry will be added to the end of the Sig, after the dosing information, and the entire Sig will be displayed.

PATIENT INSTRUCTIONS: WF WITH FOOD

(TAKE TWO CAPSULES BY MOUTH FOUR TIMES A DAY FOR 10 DAYS WITH FOOD)

OTHER PATIENT INSTRUCTIONS: WF CON ALIMENTO

Patch PSS\*1\*47 adds two new optional fields, OTHER LANGUAGE PREFERENCE and PMI LANGUAGE PREFERENCE in the PHARMACY PATIENT file (#55) that stores if a patient has another language preference and if the patient’s PMI sheets should print in English or Spanish at the CMOP. The CMOP functionality was requested for future CMOP use. When printing locally from Outpatient Pharmacy this parameter is not used. These fields are accessed through the option Update Patient Record \[PSO PAT\] and the protocol Patient Record Update \[PSO PATIENT RECORD UPDATE\]. If the other language preference is indicated for a patient, the user will be prompted to enter OTHER PATIENT INSTRUCTIONS after selecting the PATIENT INSTRUCTIONS field to enter/edit. If a quick code is entered at the OTHER PATIENT INSTRUCTIONS prompt, the expansion entered at the OTHER PATIENT INSTRUCTIONS EXPANSIONS will print on the prescription label.

A default value for Days Supply based on patient status is displayed. A default quantity is calculated when possible. See Chapter 2 in the *User Manual - Supplemental* for more information on this calculation.

DAYS SUPPLY: (1-90): 30// 10  
QTY ( CAP ) : 80// \<Enter\> 80

Example: Entering a New Order (continued)

COPIES: 1// \<Enter\> 1

\# OF REFILLS: (0-11): 11// 0

PROVIDER: OPPROVIDER4,TWO

CLINIC: OUTPT NURSE GREEN TEAM

MAIL/WINDOW: WINDOW// \<Enter\> WINDOW

METHOD OF PICK-UP: \<Enter\>

REMARKS: \<Enter\>

ISSUE DATE: TODAY// \<Enter\> (MAY 30, 2001)

FILL DATE: (5/30/2001 - 6/9/2001): TODAY// \<Enter\> (MAY 30, 2001)

Nature of Order: WRITTEN// ??

Require Print Print on

Nature of Order Activity E.Signature Chart Copy Summary

------------------------ ----------- ---------- --------

WRITTEN x

VERBAL x x x

TELEPHONED x x x

SERVICE CORRECTION

POLICY x x

DUPLICATE

SERVICE REJECT x x

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO// y YES

WAS COUNSELING UNDERSTOOD: NO// y YES

An option to add a progress note has been added. If “Yes” is entered at this prompt, the progress note entry will begin after the order information has been displayed and confirmed. The order is redisplayed, along with information on any service-connected disabilities on record.

Do you want to enter a Progress Note? No// \<Enter\>

Rx \# 503906 05/30/01

OPPATIENT16,ONE \#80

TAKE TWO CAPSULES BY MOUTH FOUR TIMES A DAY FOR 10 DAYS WITH FOOD

AMPICILLIN 250MG CAP

OPPROVIDER4,TWO OPPHARMACIST4,THREE

\# of Refills: 11

SC Percent: 40%  
Disabilities: NONE STATED  
  
Was treatment for Service Connected condition? NO

To determine if the order should be charged copay, eligible copay exemptions for the order are prompted one at a time. In this example, the user is prompted if the order is being prescribed for any of the service-connected conditions displayed. If any other service connected conditions apply to the patient, questions for each would appear. In this example, the patient is enrolled for Service Connection and Agent Orange exposure. Each applicable copay exemption prompt will appear no matter what is answered previously.

Example: Entering a New Order (continued)

Was treatment related to Agent Orange exposure? NO<u>  
</u>  
Is this correct? YES// \<Enter\>

Another New Order for OPPATIENT16,ONE? YES//

<span id="Page_111" class="anchor"></span>Medications with non-numeric dosages, such as ointments and creams, will display non-numeric possible default dosages. Because the dosage is non-numeric, values for dispense units per dose and quantity cannot be calculated.

DRUG: HYDROCORTISONE 0.5% CREAM DE200 VISN FORM; 30 GM/TUBE (IEN)

...OK? Yes// (Yes)

Now doing order checks. Please wait...

There are 4 Available Dosage(s):

1\. SMALL AMOUNT

2\. MODERATE AMOUNT

3\. LIBERALLY

4\. LARGE AMOUNT

Select from list of Available Dosages (1-4), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 MODERATE AMOUNT

You entered MODERATE AMOUNT is this correct? Yes// \<Enter\> YES

ROUTE: TOPICAL// TOPICAL

A default quantity cannot be calculated for complex orders containing the conjunction “Except.”

#### Displaying a Patient’s Remote Prescriptions

If RDI is active and a patient has prescriptions at another location, when the user selects the patient to enter a new order from Patient Prescription Processing, the following message appears.

REMOTE PRESCRIPTIONS AVAILABLE!

Display Remote Data? N//

If the user responds NO, then the normal procedure occurs for entering prescriptions. If the user responds YES, the “Remote Facilities Visited” screen appears such as the following example.

Remote Facilities Visited Dec 30, 2008@17:26:47 Page: 1 of 1

Patient: PSOPATIENT,ONE (000-00-0000) DOB: 01/02/1967

Station

HDR CHEYENNE

Enter ?? for more actions

DR Display Remote Pharmacy Data DB Display Both Pharmacy Data

Action:Quit//DR

To display the prescriptions at the remote pharmacy location, enter DR at the “Action” prompt. The “Medication Profile – Remote” screen appears such as the following example.

Medication Profile - Remote Dec 30, 2008@17:29:43 Page: 1 of 2

Patient: PSOPATIENT,ONE (000-00-0000) DOB: 01/02/1967

RX# DRUG ST QTY ISSUED LAST FILLED

HDR CHEYENNE

712885 AMOXICILLIN TRIHYDRATE 250MG CAP A 90 11/06/08 11/06/08

SIG: TAKE ONE CAPSULE BY MOUTH THREE TIMES A DAY

PROVIDER: MCKAY,ELMER

712886 DILTIAZEM (INWOOD) 240MG CAP,SA A 30 11/28/08 11/28/08

SIG: TAKE ONE CAPSULE BY MOUTH EVERY DAY

PROVIDER: MCKAY,ELMER

712888 LABETALOL HCL 200MG TAB A 60 12/30/08 12/30/08

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

PROVIDER: MCKAY,ELMER

712887 SIMVASTATIN 20MG TAB A 15 12/09/08 12/09/08

SIG: TAKE ONE-HALF TABLET BY MOUTH EVERY EVENING TESTING

FOR PATTESTING FOR PATIENT TESTING FOR PATTESTING

FOR PATIENTENT INTRUCTION ON SIG1 TESTING FOR

PATIENT INTRUCTION ON SIG1 TESTING FOR PATIENT

REPLACE IENT WITH IENT TESTING FOR PATIENT

\+ Enter ?? for more actions

Select Action:Next Screen//

### Entering a New Order – ePharmacy (Third Party Billable)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For patients who have third party insurance and have the appropriate eligibility requirements, the software will create an ePharmacy order upon finishing of the prescription entry.

After a WINDOW order is entered and finished, the billing data is sent to the Electronic Management Claims Engine (ECME). ECME sends messages back to Outpatient Pharmacy displaying the status of the claim. For MAIL orders, the communication between Outpatient Pharmacy and ECME happens either during the Local Mail Label Print or during the CMOP transmission.

The following example shows the creation of a new WINDOW order starting with the “DRUG:” prompt.

Example: Entering a New Order for ePharmacy Billing

DRUG: PREDNISONE

Lookup: GENERIC NAME

1 PREDNISONE 1MG TAB HS051

2 PREDNISONE 20MG S.T. HS051

3 PREDNISONE 5MG TAB HS051

CHOOSE 1-3: 3 PREDNISONE 5MG TAB HS051

Now doing order checks. Please wait...

Previously entered ICD diagnosis codes: \<Enter\>

Select Primary ICD Code: \<Enter\>

VERB: TAKE

There are 2 Available Dosage(s):

1\. 20MG

2\. 40MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 20MG

You entered 20MG is this correct? Yes// \<Enter\> YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET): 1// \<Enter\> 1

Dosage Ordered: 20MG

NOUN: TABLET

ROUTE: PO// \<Enter\>

1 PO ORAL (BY MOUTH) PO

2 PO ORAL PO

CHOOSE 1-2: 2 ORAL PO BY MOUTH

Schedule: TID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

TID TID THREE TIMES A DAY

...OK? Yes// (Yes)

(THREE TIMES A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 10 (DAYS)

CONJUNCTION: \<Enter\>

PATIENT INSTRUCTIONS: WF

WITH FOOD

(TAKE ONE TABLET BY BY MOUTH THREE TIMES A DAY FOR 10 DAYS WITH FOOD)

Example: Entering a New Order for ePharmacy Billing (continued)

DAYS SUPPLY: (1-90): 30// \<Enter\>

QTY ( TAB ) : 30// \<Enter\> 30

COPIES: 1// \<Enter\> 1

\# OF REFILLS: (0-5): 5// \<Enter\>

PROVIDER: OPPROVIDER4,TWO

CLINIC: \<Enter\>

MAIL/WINDOW: WINDOW// \<Enter\> WINDOW

METHOD OF PICK-UP: \<Enter\>

REMARKS: \<Enter\>

ISSUE DATE: TODAY// \<Enter\> (NOV 02, 2005)

FILL DATE: (11/2/2005 - 11/3/2006): TODAY// \<Enter\> (NOV 02, 2005)

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO// YES

WAS COUNSELING UNDERSTOOD: NO// YES

Do you want to enter a Progress Note? No// \<Enter\> NO

Rx \# 100003840 11/02/05

OPPATIENT,FOUR \#30

TAKE ONE TABLET BY BY MOUTH THREE TIMES A DAY FOR 10 DAYS WITH FOOD

PREDNISONE 5MG TAB

OPPROVIDER4,TWO OPPHARMACIST4,THREE

\# of Refills: 5

Is this correct? YES// \<Enter\> YES

Veteran Prescription 100003840 successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Gathering claim info

IN PROGRESS-Packet being built

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

E PAYABLE

Another New Order for OPPATIENT,FOUR? YES// NO

View of RX:

Medication Profile Nov 02, 2005@07:33:29 Page: 1 of 1

OPPATIENT,FOUR

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 100003840e PREDNISONE 5MG TAB 30 A\> 11-02 11-02 5 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

If a new order is rejected due to a Drug Utilization Review (DUR), Reject Resolution Required, or Refill Too Soon, the prescription will be marked as “REJECTED”, and the user will have the opportunity to resolve before continuing.

The following example displays a sample ECME transmission rejection, and how to resolve the rejection error.

Example: Handling a Rejected New Order for ePharmacy Billing

Veteran Prescription 999999 successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

E REJECTED

\*\*\* VETERAN - REJECT RECEIVED FROM THIRD PARTY PAYER \*\*\*

----------------------------------------------------------------------

Division : ALBANY NCPDP: 123456789 NPI#: 39393939

Patient : OPPATIENT,FOUR(000-01-1322P) Sex: M DOB: JAN 13,1922(83)

Prescription : 99999999/0 - TESTOSTERONE (ANDROD ECME#: 000001234567

Reject Type : 88 - DUR REJECT received on FEB 27, 2006@10:58:25

Payer Message: DUR Reject Error

Reason : ER (OVERUSE PRECAUTION)

DUR Text : ANDRODERM DIS 5MG/24HR

Insurance : EMDEON Contact: 800 555-5555

Group Name : RXINS Group Number: 12454

Cardholder ID: 000011322P

-------------------------------------------------------------------------

Select one of the following:

O (O)VERRIDE - RESUBMIT WITH OVERRIDE CODES

I (I)GNORE - FILL Rx WITHOUT CLAIM SUBMISSION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(O)verride,(I)gnore,(Q)uit: Q// O OVERRIDE

When a claim is rejected, typically the Payer provides a “Reason for Service Code”, which displays on the reject as “Reason”. The user can use this reason to then select which code is entered for “Professional Service Code” and “Result of Service Code”. To see a list of service codes, enter ? at the specified prompt.Example: Handling a Rejected New Order for ePharmacy Billing (continued)

Reason for Service Code : ER - OVERUSE

Professional Service Code: RT RECOMMENDED LABORATORY TEST

Result of Service Code : 1G FILLED, WITH PRESCRIBER APPROVAL

Reason for Service Code : ER - OVERUSE

Professional Service Code: RT - RECOMMENDED LABORATORY TEST

Result of Service Code : 1G - FILLED, WITH PRESCRIBER APPROVAL

Confirm? ? YES// \<Enter\>

Veteran Prescription 99999999 successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Packet being built

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Waiting to process response

E PAYABLE

For Refill Too Soon rejects, the same choices apply.

Example: Handling a Reject Resolution Required rejected New Prescription for ePharmacy Billing

For VETERAN prescriptions, a reject code can be specified in the Reject Resolution Required section of the ePharmacy Site Parameter screen to stop a prescription from being filled. The Reject Resolution Required reject codes will prevent a a prescription from being filled during any claims processing under the following conditions:

- VETERAN eligibility
- The prescription is an original fill
- The prescription is not released
- The reject is on the Reject Resolution Required list for the division
- The total gross amount of the prescription is at or above the specified threshold amount

For VETERAN prescription rejections that have Reject Resolution Required rejects, the user will be able to select from (I)gnore, which bypasses claims processing and allows the prescription to be filled, or (Q)uit which sends it to the Third Party Payer Rejects – Worklist. Prescriptions with these type rejects cannot be filled until the reject is resolved. Example:

Example: Handling a Reject Resolution Required rejected New Order for ePharmacy Billing (continued)

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Building the HL7 packet

IN PROGRESS-Transmitting

IN PROGRESS-Processing response

E REJECTED

\*\*\* VETERAN - REJECT RECEIVED FROM THIRD PARTY PAYER \*\*\*

-------------------------------------------------------------------------

Division : ALBANY NPI: 123456789 NCPDP: 4150001

Patient : OP,FOUR(000-01-1322P) Sex: M DOB: JAN 13, 1922(83)

Rx/Drug : 99999999/0 – TESTOSTERONE (ANDROD ECME#: 000001234567

Reject(s): 76 - Plan Limitations Exceeded Received on JUN 07, 2013@11:26:05

Payer Message: DAYS SUPPLY IS MORE THAN ALLOWED BY PLAN

Insurance : TEST INS Contact: 800-555-5555

Group Name : RXINS Group Number: 12454

Cardholder ID: 0000011322P

Reject Resolution Required

Gross Amount Due (\$34.42) is greater than or equal to

Threshold Dollar Amount (\$0)

Please select Quit to resolve this reject on the Reject Worklist.

-------------------------------------------------------------------------

Select one of the following:

I (I)GNORE - FILL Rx WITHOUT CLAIM SUBMISSION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(I)gnore,(Q)uit: Q//

Example: Handling a TRICARE Rejected New Order for ePharmacy Billing

Rejected TRICARE claims will be denoted with “TRICARE” during submission to ECME and within the subsequent reject notification screen. Also, the reject codes will be displayed in both places. The following example shows a prescription being submitted to ECME and this process occurs directly following the “Is this correct? YES//” prompt during finish. Where DUR or RTS are one of the reject codes, the user will be able to select from (D)iscontinue the prescription, submit (O)verride codes, or (Q)uit which sends the rejection to the Third Party Payer Rejects - Worklist. A TRICARE rejection may not be (I)gnored.

TRICARE Prescription 101110 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Processing response

E REJECTED

79 - Refill Too Soon

14 - M/I Eligibility Clarification Code

\*\*\* REJECT RECEIVED FOR TRICARE PATIENT \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPTRICARE,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101110/0 - NAPROXEN 250MG S.T. ECME#: 000000112303

Reject(s): REFILL TOO SOON (79), 14 - M/I Eligibility Clarification Code (14).

Received on MAR 03, 2008@14:40:57.

Insurance : TRICARE Contact:

Group Name : TRICARE PRIME Group Number: 123123

Cardholder ID: SI9844532

-------------------------------------------------------------------------

Select one of the following:

O (O)VERRIDE - RESUBMIT WITH OVERRIDE CODES

D (D)iscontinue - DO NOT FILL PRESCRIPTION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(O)verride,(D)iscontinue,(Q)uit: Q//

Example: Handling a non-DUR/RTS or non-clinical TRICARE rejected New Order for ePharmacy Billing

For TRICARE prescription rejections that have non-DUR/RTS or non-clinical rejects, the user will be able to select from (D)iscontinue the prescription or (Q)uit which sends it to the Third Party Payer Rejects - Worklist. TRICARE prescriptions with these type rejects cannot be filled until the rejection is resolved. Example:

TRICARE Prescription 101113 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Building the HL7 packet

IN PROGRESS-Transmitting

E REJECTED

07 - M/I Cardholder ID Number

14 - M/I Eligibility Clarification Code

\*\*\* REJECT RECEIVED FOR TRICARE PATIENT \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPTRICARE,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101113/0 - SIMETHICONE 40MG TAB ECME#: 000000112306

Reject(s): M/I Eligibility Clarification Code (14), M/I Cardholder ID

Number (07). Received on MAR 03, 2008@14:43:42.

Insurance : TRICARE Contact:

Group Name : TRICARE PRIME Group Number: 123123

Cardholder ID: SI9844532

-------------------------------------------------------------------------

Select one of the following:

D (D)iscontinue - DO NOT FILL PRESCRIPTION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(D)iscontinue,(Q)uit: Q//

For non-billable TRICARE prescriptions, an abbreviated version of the reject notification screen will be displayed. Because the prescription is non-billable, the insurance and ECME information that's currently provided for DUR/RTS rejects will not be displayed (i.e. insurance, group name, group \#, ECME \#, contact, cardholder ID). In this case, the prescription must be discontinued.

Is this correct? YES// ...

\*\*\* TRICARE - NON-BILLABLE \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#:

Patient : OPTRICARE,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 102058/0 - ABSORBABLE GELATIN S

Date/Time: AUG 27, 2008@16:49:46

Reason : Drug not billable.

-------------------------------------------------------------------------

This is a non-billable TRICARE prescription. It cannot be filled or sent

to the reject worklist. It must be discontinued.

Press \<RETURN\> to continue...

Nature of Order: SERVICE CORRECTION// S

Requesting PROVIDER: OPHARM OPPHARM,ONE OO

Labels will not print for discontinued TRICARE prescriptions, and reprint label will not be allowed for TRICARE rejected prescriptions.

Select Rx (Prescriptions) Option: REPrint an Outpatient Rx Label

Reprint Prescription Label: 101113 SIMETHICONE 40MG TAB

Number of Copies? : (1-99): 1//

Print adhesive portion of label only? ? No// NO

Do you want to resend to Dispensing System Device? No// NO

Comments: REPRINT

Rx \# 101113 03/03/08

OPTRICARE,ONE \#180

ONE MOUTH TWICE A DAY

SIMETHICONE 40MG TAB

OPPHARM,ONE OPPHARM,ONE

\# of Refills: 3

Select LABEL DEVICE: NULL Bit Bucket

No Label(s) printed.

Reprint Prescription Label:

Suspended TRICARE prescriptions will remain on suspense when a reject occurs, when the prescription is non-billable, or when the third party claim remains in an 'IN PROGRESS' status in ECME. Labels will not print. Once the reject is resolved, the user may pull the prescription early from suspense or wait for the next scheduled Print from Suspense option runs at which time labels will print accordingly. This includes CMOP and local suspense.

TRICARE Prescription 101607 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

\*\*\*TRICARE - 'IN PROGRESS' ECME status \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPTRICARE,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101607/0 - ACETAZOLAMIDE 250MG

Date/Time: APR 20, 2008@20:11:17

Reason : ECME Status is in an 'IN PROGRESS' state and cannot be filled

-------------------------------------------------------------------------

This prescription will be suspended. After the third party claim is resolved,

it may be printed or pulled early from suspense.

Press \<RETURN\> to continue...

A rejected TRICARE prescription may not have a partial fill ordered until the reject is resolved.

OP Medications (SUSPENDED) Apr 18, 2008@19:10:16 Page: 1 of 2

OPTRICARE,ONE

PID: 666-55-4789 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: OCT 18,1963 (44) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 101526e

\(1\) \*Orderable Item: ACETAZOLAMIDE PILL

\(2\) Drug: ACETAZOLAMIDE 500MG SEQUELS

Verb: TAKE

\(3\) \*Dosage: 1 PILL

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE 1 PILL BY MOUTH TWICE A DAY

\(5\) Patient Status: OTHER FEDERAL

\(6\) Issue Date: 04/18/08 (7) Fill Date: 04/19/08

Last Fill Date: 04/19/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 04/19/09 MFG:

\+

DC Discontinue PR Partial RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen// p Partial

OP Medications (SUSPENDED) Apr 18, 2008@19:10:16 Page: 1 of 2

OPTRICARE,ONE

PID: 666-55-4789 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: OCT 18,1963 (44) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 101526e

\(1\) \*Orderable Item: ACETAZOLAMIDE PILL

\(2\) Drug: ACETAZOLAMIDE 500MG SEQUELS

Verb: TAKE

\(3\) \*Dosage: 1 PILL

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE 1 PILL BY MOUTH TWICE A DAY

\(5\) Patient Status: OTHER FEDERAL

\(6\) Issue Date: 04/18/08 (7) Fill Date: 04/19/08

Last Fill Date: 04/19/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 04/19/09 MFG:

\+ Partial cannot be filled on TRICARE non-payable Rx

DC Discontinue PR Partial RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen//

If ECME's status on the claim remains in an "In Progress" state past the processing timeout during finish of the prescription, TRICARE prescriptions will not be allowed to be filled. Instead it will be placed on suspense until the rejection is resolved. Below is an example of this screen:

TRICARE Prescription 101607 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

\*\*\* TRICARE - 'IN PROGRESS' ECME status \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPTRICARE,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101607/0 - ACETAZOLAMIDE 250MG

Date/Time: APR 20, 2008@20:11:17

Reason : ECME Status is in an 'IN PROGRESS' state and cannot be filled

-------------------------------------------------------------------------

This prescription will be suspended. After the third party claim is resolved,

it may be printed or pulled early from suspense.

Press \<RETURN\> to continue...

If a pharmacy is active for ePharmacy processing but an insurance plan is not linked or not active, TRICARE prescription will be allowed to be filled without third party claim submission. The phrase "Inactive ECME TRICARE" will be displayed during Finish and an ECME log entry will be added stating such.

Example of message during finish:

Do you want to enter a Progress Note? No// NO

Rx \# 102046 08/27/08

OPTRICARE,TEST \#180

ONE MOUTH TWICE A DAY

DANTROLENE 25MG CAP

OPPROVIDER,ONE OPPHAR,ONE

\# of Refills: 3

Is this correct? YES// ...

-Rx 101921 has been discontinued...

Inactive ECME TRICARE

Example of ECME Activity Log entry:

ECME Log:

\# Date/Time Rx Ref Initiator Of Activity

===============================================================================

1 8/27/08@11:07:45 ORIGINAL OPPHARM,ONE

Comments: TRICARE-Inactive ECME TRICARE

Example: Handling a CHAMPVA Rejected New Order for ePharmacy Billing

Rejected CHAMPVA claims will be denoted with “CHAMPVA” during submission to ECME and within the subsequent reject notification screen. Also, the reject codes will be displayed in both places. The following example shows a prescription being submitted to ECME and this process occurs directly following the “Is this correct? YES//” prompt during finish. Where DUR or RTS are one of the reject codes, the user will be able to select from (D)iscontinue the prescription, submit (O)verride codes, or (Q)uit which sends the rejection to the Third Party Payer Rejects - Worklist. A CHAMPVA rejection may not be (I)gnored.

CHAMPVA Prescription 101110 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Processing response

E REJECTED

79 - Refill Too Soon

14 - M/I Eligibility Clarification Code

\*\*\* REJECT RECEIVED FOR CHAMPVA PATIENT \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021 NCPDP:1234567

Patient : OPCHAMPVA,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101110/0 - NAPROXEN 250MG S.T. ECME#: 000000112303

Reject(s): REFILL TOO SOON (79), 14 - M/I Eligibility Clarification Code (14).

Received on MAR 03, 2008@14:40:57.

Insurance : CHAMPVA Contact:

Group Name : CHAMPVA PRIME Group Number: 123123

Cardholder ID: SI9844532

-------------------------------------------------------------------------

Select one of the following:

O (O)VERRIDE - RESUBMIT WITH OVERRIDE CODES

D (D)iscontinue - DO NOT FILL PRESCRIPTION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(O)verride,(D)iscontinue,(Q)uit: Q//

Example: Handling a non-DUR/RTS or non-clinical CHAMPVA rejected New Order for ePharmacy Billing

For CHAMPVA prescription rejections that have non-DUR/RTS or non-clinical rejects, the user will be able to select from (D)iscontinue the prescription or (Q)uit which sends it to the Third Party Payer Rejects - Worklist. CHAMPVA prescriptions with these type rejects cannot be filled until the rejection is resolved. Example:

CHAMPVA Prescription 101113 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Building the HL7 packet

IN PROGRESS-Transmitting

E REJECTED

07 - M/I Cardholder ID Number

14 - M/I Eligibility Clarification Code

\*\*\* REJECT RECEIVED FOR CHAMPVA PATIENT \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPCHAMPVA,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101113/0 - SIMETHICONE 40MG TAB ECME#: 000000112306

Reject(s): M/I Eligibility Clarification Code (14), M/I Cardholder ID

Number (07). Received on MAR 03, 2008@14:43:42.

Insurance : CHAMPVA Contact:

Group Name : CHAMPVA PRIME Group Number: 123123

Cardholder ID: SI9844532

-------------------------------------------------------------------------

Select one of the following:

D (D)iscontinue - DO NOT FILL PRESCRIPTION

Q (Q)UIT - SEND TO WORKLIST (REQUIRES INTERVENTION)

(D)iscontinue,(Q)uit: Q//

For non-billable CHAMPVA prescriptions, an abbreviated version of the reject notification screen will be displayed. Because the prescription is non-billable, the insurance and ECME information that's currently provided for DUR/RTS rejects will not be displayed (i.e. insurance, group name, group \#, ECME \#, contact, cardholder ID). In this case, the prescription must be discontinued.

Is this correct? YES// ...

\*\*\* CHAMPVA - NON-BILLABLE \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#:

Patient : OPCHAMPVA,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 102058/0 - ABSORBABLE GELATIN S

Date/Time: AUG 27, 2008@16:49:46

Reason : Drug not billable.

-------------------------------------------------------------------------

This is a non-billable CHAMPVA prescription. It cannot be filled or sent

to the reject worklist. It must be discontinued.

Press \<RETURN\> to continue...

Nature of Order: SERVICE CORRECTION// S

Requesting PROVIDER: OPHARM OPPHARM,ONE OO

Labels will not print for discontinued CHAMPVA prescriptions, and reprint label will not be allowed for CHAMPVA rejected prescriptions.

Select Rx (Prescriptions) Option: REPrint an Outpatient Rx Label

Reprint Prescription Label: 101113 SIMETHICONE 40MG TAB

Number of Copies? : (1-99): 1//

Print adhesive portion of label only? ? No// NO

Do you want to resend to Dispensing System Device? No// NO

Comments: REPRINT

Rx \# 101113 03/03/08

OPCHAMPVA,ONE \#180

ONE MOUTH TWICE A DAY

SIMETHICONE 40MG TAB

OPPHARM,ONE OPPHARM,ONE

\# of Refills: 3

Select LABEL DEVICE: NULL Bit Bucket

No Label(s) printed.

Reprint Prescription Label:

Suspended CHAMPVA prescriptions will remain on suspense when a reject occurs, when the prescription is non-billable, or when the third party claim remains in an 'IN PROGRESS' status in ECME. Labels will not print. Once the reject is resolved, the user may pull the prescription early from suspense or wait for the next scheduled Print from Suspense option runs at which time labels will print accordingly. This includes CMOP and local suspense.

CHAMPVA Prescription 101607 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

\*\*\*CHAMPVA - 'IN PROGRESS' ECME status \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPCHAMPVA,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101607/0 - ACETAZOLAMIDE 250MG

Date/Time: APR 20, 2008@20:11:17

Reason : ECME Status is in an 'IN PROGRESS' state and cannot be filled

-------------------------------------------------------------------------

This prescription will be suspended. After the third party claim is resolved,

it may be printed or pulled early from suspense.

Press \<RETURN\> to continue...

A rejected CHAMPVA prescription may not have a partial fill ordered until the reject is resolved.

OP Medications (SUSPENDED) Apr 18, 2008@19:10:16 Page: 1 of 2

OPCHAMPVA,ONE

PID: 666-55-4789 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: OCT 18,1963 (44) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 101526e

\(1\) \*Orderable Item: ACETAZOLAMIDE PILL

\(2\) Drug: ACETAZOLAMIDE 500MG SEQUELS

Verb: TAKE

\(3\) \*Dosage: 1 PILL

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE 1 PILL BY MOUTH TWICE A DAY

\(5\) Patient Status: OTHER FEDERAL

\(6\) Issue Date: 04/18/08 (7) Fill Date: 04/19/08

Last Fill Date: 04/19/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 04/19/09 MFG:

\+

DC Discontinue PR Partial RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen// p Partial

OP Medications (SUSPENDED) Apr 18, 2008@19:10:16 Page: 1 of 2

OPCHAMPVA,ONE

PID: 666-55-4789 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: OCT 18,1963 (44) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 101526e

\(1\) \*Orderable Item: ACETAZOLAMIDE PILL

\(2\) Drug: ACETAZOLAMIDE 500MG SEQUELS

Verb: TAKE

\(3\) \*Dosage: 1 PILL

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE 1 PILL BY MOUTH TWICE A DAY

\(5\) Patient Status: OTHER FEDERAL

\(6\) Issue Date: 04/18/08 (7) Fill Date: 04/19/08

Last Fill Date: 04/19/08 (Window)

Last Release Date: (8) Lot \#:

Expires: 04/19/09 MFG:

\+ Partial cannot be filled on CHAMPVA non-payable Rx

DC Discontinue PR Partial RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen//

If ECME's status on the claim remains in an "In Progress" state past the processing timeout during finish of the prescription, a CHAMPVA prescription will not be allowed to be filled. Instead it will be placed on suspense until the rejection is resolved. Below is an example of this screen:

CHAMPVA Prescription 101607 submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

\*\*\* CHAMPVA - 'IN PROGRESS' ECME status \*\*\*

-------------------------------------------------------------------------

Division : ALBANY ISC NPI#: 5000000021

Patient : OPCHAMPVA,ONE(666-55-4789) Sex: M DOB: OCT 18,1963(44)

Rx/Drug : 101607/0 - ACETAZOLAMIDE 250MG

Date/Time: APR 20, 2008@20:11:17

Reason : ECME Status is in an 'IN PROGRESS' state and cannot be filled

-------------------------------------------------------------------------

This prescription will be suspended. After the third party claim is resolved,

it may be printed or pulled early from suspense.

Press \<RETURN\> to continue...

If a pharmacy is active for ePharmacy processing but an insurance plan is not linked or not active, the CHAMPVA prescription will be allowed to be filled without third party claim submission. The phrase "Inactive ECME CHAMPVA" will be displayed during Finish and an ECME log entry will be added stating such.

Example of message during finish:

Do you want to enter a Progress Note? No// NO

Rx \# 102046 08/27/08

OPCHAMPVA,TEST \#180

ONE MOUTH TWICE A DAY

DANTROLENE 25MG CAP

OPPROVIDER,ONE OPPHAR,ONE

\# of Refills: 3

Is this correct? YES// ...

-Rx 101921 has been discontinued...

Inactive ECME CHAMPVA

Example of ECME Activity Log entry:

ECME Log:

\# Date/Time Rx Ref Initiator Of Activity

===============================================================================

1 8/27/08@11:07:45 ORIGINAL OPPHARM,ONE

Comments: CHAMPVA -Inactive ECME CHAMPVA

### NDC Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial validation of the NDC can be performed by a pharmacy technician. This functionality only applies to local fills that are not sent to OPAI. This function provides a pharmacy technician the ability to manually enter or scan the bar code of the existing prescription label and then manually enter or scan the NDC of the stock bottle used to fill the prescription. When the system matches the NDC, confirmation is provided to the pharmacy tech and allows the technician to continue processing. However, if the system detects a mismatch and the NDC of the stock bottle has an associated entry in the synonym file, the NDC will be updated in Prescription file (#52) for the fill. The system will then prompt the technician to press enter to continue, a new label will be printed, the original electronic claim reversed, and a new claim submission will be transmitted with the new NDC. In the event that the revised NDC prompts a RTS/DUR rejection or a Reject Resolution Required rejection, the system will immediately send the item to the Reject Worklist.

In a case where the NDC entered is not defined for the drug, the system prompts the technician that a mismatch has occurred and the prescription needs to be validated by a pharmacist. The system notes that the NDC had not been validated and allows the pharmacy tech to move to the next prescription. In the event of a change of NDC prompting a rejection, the system immediately sends the item to the Reject Worklist.

The releasing pharmacist will receive a notation that NDC has been validated by the technician when processing. If the NDC change has prompted a claim reversal and produced a RTS/DUR rejection or a Reject Resolution Required rejection, the pharmacist will be presented with a Reject Processing screen at release.

Example: Matched NDC:

Select ePharmacy Menu Option: NV  NDC Validation

 

WAND BARCODE or enter Rx#: 2054787B

 

Rx: 2054787B        Fill: 0             Patient: OPPATIENT,TWO               

Drug: AMOXICILLIN 250MG CAP             NDC: 00003-0101-60                   

 

\*\* This NDC has not been validated.

 

 

PRODUCT NDC: 00003-0101-60// 00003-0101-60

 

NDC match confirmed.

 

 

WAND BARCODE or enter Rx#:  

Example: Changed NDC or Modified NDC:

Select ePharmacy Menu Option:  NDC Validation

 

WAND BARCODE or enter Rx#: 

 

Rx: 102009          Fill: 0             Patient: OPPATIENT,ONE               

Drug: BIPERIDEN 2MG TAB                 NDC: 00044-0120-04                    

 

\*\* This NDC has not been validated.

 

 

PRODUCT NDC: 00044-0120-04// 00044-0120-05 00044-0120-05

 

 

Veteran Prescription 102009 successfully submitted to ECME for claim generation.

 

Claim Status:

Reversing and Rebilling a previously submitted claim...

IN PROGRESS-Waiting to start

IN PROGRESS-Building the transaction

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

E REVERSAL ACCEPTED

IN PROGRESS-Building the claim

IN PROGRESS-Building the HL7 packet

IN PROGRESS-Transmitting

E PAYABLE

 

 

NDC match confirmed.

 

 

WAND BARCODE or enter Rx#:

## Using the Copy Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/036.png) If the order utilizes the <span id="p477_133_Except_no_copy_ref" class="anchor"></span>EXCEPT conjunction, copy will no longer be allowed. The message bar will display: Cannot COPY. Invalid ‘except’ conjunction!

If a double question mark (??) is entered at the “Select Action” prompt, the hidden actions on the following page will display in the action area.

The following actions are also available:

AL Activity Logs (OP) REJ View REJECT DN Down a Line

VF Verify (OP) VER View ePharmacy Rx FS First Screen

CO Copy (OP) RES Resubmit Claim GO Go to Page

TR Convert Titration Rx REV Reverse Claim LS Last Screen

TM Titration Mark/UnmarkIN Intervention Menu PS Print Screen

RP Reprint (OP) DA Display Drug AllergiesPT Print List

HD Hold (OP) DIN Drug Restr/Guide (OP) QU Quit

UH Unhold (OP) + Next Screen RD Re Display Screen

PI Patient Information - Previous Screen SL Search List

PP Pull Rx (OP) \< Shift View to Left UP Up a Line

IP Inpat. Profile (OP) \> Shift View to Right

OTH Other OP Actions ADPL Auto Display(On/Off)

Use the Copy action to make a duplicate order. Any field of the newly created order can be edited. The original order will remain active, but the duplicate order check will be processed before the new order can be accepted.

Example: Using the Copy Action

Medication Profile Jun 12, 2001 14:39:11 Page: 1 of 1

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 503904\$ AMPICILLIN 250MG CAP 80 E 05-25 05-25 0 10

2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

3 503916 NADOLOL 40MG TAB 60 A\> 06-12 06-12 11 30

----------------------------------DISCONTINUED---------------------------------

4 503902 ACETAMINOPHEN 500MG TAB 60 DC\>05-22 05-22 3 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// SO Select Order

Select Orders by number: (1-4):3

The Order Number can be entered at the “Select Action” prompt instead of “SO”.

Once an order is selected, the Copy action can be used.

OP Medications (ACTIVE) Jun 12, 2001 14:42:17 Page: 1 of 2

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

Rx \#: 503916

\(1\) \*Orderable Item: NADOLOL TAB \*\*\*(N/F)\*\*\*

\(2\) CMOP Drug: NADOLOL 40MG TAB \*\*\*(N/F)\*\*\*

NDC: 00056-0176-75

\(3\) \*Dosage: 40 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: BID

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

\(5\) Patient Status: SERVICE CONNECTED

\(6\) Issue Date: 06/12/01 (7) Fill Date: 06/12/01

Last Fill Date: 06/12/01 (Window)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// CO COPY

After “CO” is entered, the heading on the screen changes to “New OP Order (COPY)” and the available actions are limited to “Accept” or “Edit”.

(New Order (Copy) screen displays merged to save space)

Example: Using the Copy Action (continued)

New OP Order (COPY) Jun 12, 2001 14:47:53 Page: 1 of 2

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

Orderable Item: NADOLOL TAB \*\*\*(N/F)\*\*\*

\(1\) CMOP Drug: NADOLOL 40MG TAB \*\*\*(N/F)\*\*\*

\(2\) Patient Status: SERVICE CONNECTED

\(3\) Issue Date: JUN 12,2001 (4) Fill Date: JUN 12,2001

\(5\) Dosage Ordered: 40 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

Route: ORAL

Schedule: BID

(6)Pat Instruction:

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

\(7\) Days Supply: 30 (8) QTY (TAB): 60

\(9\) \# of Refills: 11 (10) Routing: WINDOW

\(11\) Clinic: OUTPT NURSE BLUE TEAM

\(12\) Provider: OPPROVIDER4,TWO (13) Copies: 1

\(14\) Remarks: New Order Created by copying Rx \# 503916.

Entry By: OPPROVIDER4,TWO Entry Date: JUN 12,2001 14:47:53

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 503916

Drug: NADOLOL 40MG TAB

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

QTY: 60 Refills remaining: 11

Provider: OPPROVIDER4,TWO Issued: 06/12/01

Status: Active Last filled on: 06/12/01

Processing Status: Released locally on 06/12/01@11:34:13 (Mail)

Days Supply: 30

------------------------------------------------------------------------------

Discontinue Rx \# 503916 NADOLOL 40MG TAB Y/N? YES

Rx \# 503916 NADOLOL 40MG TAB will be discontinued after the acceptance of the new order.

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

Now doing order checks. Please wait...

Nature of Order: WRITTEN// ??

Require Print Print on

Nature of Order Activity E.Signature Chart Copy Summary

------------------------ ----------- ---------- --------

WRITTEN x

VERBAL x x x

TELEPHONED x x x

SERVICE CORRECTION

POLICY x x

DUPLICATE

SERVICE REJECT x x

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO// \<Enter\>NO

Do you want to enter a Progress Note? No// \<Enter\> NO

Rx \# 503919 06/12/01

OPPATIENT16,ONE \#60

TAKE ONE TABLET BY MOUTH TWICE A DAY

NADOLOL 40MG TAB

OPPROVIDER4,TWO OPPHARMACIST4,THREE

\# of Refills: 11

Is this correct? YES// \<Enter\>...

-Duplicate Drug Rx \#503916 NADOLOL 40MG TAB has been discontinued...

SC Percent: 20%

Disabilities:

KNEE CONDITION 10% - SERVICE CONNECTED

TRAUMATIC ARTHRITIS 10% - SERVICE CONNECTED

TRAUMATIC ARTHRITIS 0% - SERVICE CONNECTED

SEPTUM, NASAL, DEVIATION OF 0% - SERVICE CONNECTED

RESIDUALS OF FOOT INJURY 0% - SERVICE CONNECTED

Was treatment for Service Connected condition? NO

The Medication Profile screen is redisplayed at this point. Note that the orders tagged for patient copay charges have a dollar sign (\$) after the RX \#.

Medication Profile Jun 12, 2001 15:03:10 Page: 1 of 1

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.09

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 503904\$ AMPICILLIN 250MG CAP 80 E 05-25 05-25 0 10

2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

3 503919\$ NADOLOL 40MG TAB 60 A\> 06-12 06-12 11 30

----------------------------------DISCONTINUED---------------------------------

4 503902 ACETAMINOPHEN 500MG TAB 60 DC\>05-22 05-22 3 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

### Copying an ePharmacy Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When copying an ePharmacy order, upon acceptance of the copied order the original prescription will be discontinued and a new order created. If the latest fill of the original order has not been released and is E Payable, the claim for that fill will be reversed. A new claim is submitted for the new prescription.

Patient Information Nov 04, 2005@09:19:26 Page: 1 of 1

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Eligibility: NSC, VA PENSION

Disabilities:

123123 A

BIRMINGHAM PHONE: (205)4444444

ALABAMA 35235

Prescription Mail Delivery: Regular Mail

Allergies:

Adverse Reactions:

Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Quit// \<Enter\> QUIT

Medication Profile Nov 04, 2005@09:23:47 Page: 1 of 1

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 100003852e PREDNISONE 5MG TAB 30 A\> 11-04 11-04 5 30

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// 1

Medication Profile Nov 04, 2005@09:24:04 Page: 1 of 1

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

OP Medications (ACTIVE) Nov 04, 2005@09:24:17 Page: 1 of 3

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 100003852e

\(1\) \*Orderable Item: PREDNISONE TAB

\(2\) CMOP Drug: PREDNISONE 5MG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 20 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: QID

\*Duration: 30 (DAYS)

(4)Pat Instructions: WITH FOOD AVOIDING DAIRY FOODS

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY FOR 30 DAYS

WITH FOOD AVOIDING DAIRY FOODS

\(5\) Patient Status: OPT NSC

Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// CO CO

Once “Copy” is entered, the heading on the screen changes to “New OP Order (COPY)” and the available actions are limited to “Edit” or “Accept.”

New OP Order (COPY) Nov 04, 2005@09:24:17 Page: 1 of 2

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Orderable Item: PREDNISONE TAB

\(1\) CMOP Drug: PREDNISONE 5MG TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: NOV 4,2005 (4) Fill Date: NOV 4,2005

\(5\) Dosage Ordered: 20 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

Route: ORAL

Schedule: QID

\*Duration: 30 (DAYS)

(6)Pat Instruction: WITH FOOD AVOIDING DAIRY FOODS

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY FOR 30

DAYS WITH FOOD AVOIDING DAIRY FOODS

\+ Enter ?? for more actions

AC Accept ED Edit

Select Action: Next Screen// AC Accept

Example: Copying an ePharmacy Order (continued)

-------------------------------------------------------------------------------

Duplicate Drug in Local Rx:

Rx \#: 100003852

Drug: PREDNISONE 5MG TAB

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY FOR 30

DAYS WITH FOOD AVOIDING DAIRY FOODS

QTY: 30 Refills remaining: 5

Provider: OPPROVIDER4,TWO Issued: 11/04/05

Status: Active Last filled on: 11/04/05

Processing Status: Released locally on 11/04/05@11:34:13 (Mail)

Days Supply: 30

------------------------------------------------------------------------------

Discontinue Rx \# 100003852 PREDNISONE 5MG TAB Y/N? YES

Rx \# 100003852 PREDNISONE 5MG TAB will be discontinued after the acceptance of the new order.

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO// YES

WAS COUNSELING UNDERSTOOD: NO// YES

Do you want to enter a Progress Note? No// \<Enter\> NO

Rx \# 100003853 11/04/05

OPPATIENT,FOUR \#30

TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY FOR 30 DAYS WITH FOOD

AVOIDING DAIRY FOODS

PREDNISONE 5MG TAB

OPPROVIDER4,TWO OPPHARMACIST4,THREE

\# of Refills: 5

Is this correct? YES// YES...

Reversing prescription 100003852.

Claim Status:

Reversing and Rebilling a previously submitted claim...

Reversing...

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Waiting to process response

E REVERSAL ACCEPTED

-Duplicate Drug Rx \#100003852 PREDNISONE 5MG TAB has been discontinued...

Veteran Prescription 100003853 successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

E PAYABLE

View of RX:

Medication Profile Nov 04, 2005@09:25:14 Page: 1 of 1

OPPATIENT,FOUR

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE------------------------------------

1 100003853e PREDNISONE 5MG TAB 30 A\> 11-04 11-04 5 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

### Holding and Unholding a Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a double question mark (??) is entered at the “Select Action” prompt, the hidden actions on the following page will display in the action area.

The following actions are also available:

AL Activity Logs (OP) REJ View REJECT DN Down a Line

VF Verify (OP) VER View ePharmacy Rx FS First Screen

CO Copy (OP) RES Resubmit Claim GO Go to Page

TR Convert Titration Rx REV Reverse Claim LS Last Screen

TM Titration Mark/UnmarkIN Intervention Menu PS Print Screen

RP Reprint (OP) DA Display Drug AllergiesPT Print List

HD Hold (OP) DIN Drug Restr/Guide (OP) QU Quit

UH Unhold (OP) + Next Screen RD Re Display Screen

PI Patient Information - Previous Screen SL Search List

PP Pull Rx (OP) \< Shift View to Left UP Up a Line

IP Inpat. Profile (OP) \> Shift View to Right

OTH Other OP Actions ADPL Auto Display(On/Off)

Use the Hold (HD) action to put a prescription on hold. Use the Unhold (UH) action to remove a prescription from hold.

Only key holders of the PSORPH security key or the PSO TECH ADV security key can hold or unhold a prescription.

PSORPH security key holders are allowed to put a prescription on hold using the following HOLD reasons:

> 1 INSUFFICIENT QTY IN STOCK

> 2 DRUG-DRUG INTERACTION

> 4 PROVIDER TO BE CONTACTED

> 6 ADVERSE DRUG REACTION

> 7 BAD ADDRESS

> 8 PER PATIENT REQUEST

> 9 CONSULT/PRIOR APPROVAL NEEDED

> 98 OTHER/TECH (NON-CLINICAL)

> 99 OTHER/RPH (CLINICAL)

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/037.png)

> **NOTE:** HOLD reasons 98 and 99 require the user to enter a HOLD comment.

PSO TECH ADV security key holders are allowed to put a prescription on hold using the following HOLD reasons:

> 1 INSUFFICIENT QTY IN STOCK

> 7 BAD ADDRESS

> 8 PER PATIENT REQUEST

> 98 OTHER/TECH (NON-CLINICAL)

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/038.png)

> **NOTE:** HOLD reason 98 requires the user to enter a HOLD comment.

While PSORPH security key holders are allowed to remove a prescription from HOLD under any HOLD reason, PSO TECH ADV security key holders are only allowed to remove a prescription from HOLD under the above HOLD reasons (reasons 1,7, 8, and 98).

Example: HOLD with PSORPH Security Key or PSO TECH ADV Security Key

OP Medications (SUSPENDED) May 11, 2012@10:12:56 Page: 1 of 3

PAGPATNM,M \<A\>

PID: 666-00-0286 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: DEC 1,1900 Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 100002926

\(1\) \*Orderable Item: FLUOXETINE CAP,ORAL

\(2\) CMOP Drug: EFFEXOR

NDC: 00056-0176-75

\(3\) \*Dosage: 10 (MG)

Verb: TAKE

Dispense Units: 1

Noun: CAPSULE

\*Route: ORAL

\*Schedule: QAM

(4)Pat Instructions:

SIG: TAKE ONE CAPSULE MOUTH EVERY MORNING

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 02/14/12 (7) Fill Date: 05/09/12

Last Fill Date: 05/29/12 (Mail)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen// HD HD

Nature of Order: WRITTEN// W

If the user has the PSORPH security key, the following HOLD reasons are available:

HOLD REASON: ?

Enter reason medication is placed in a 'Hold' status.

Choose from:

1 INSUFFICIENT QTY IN STOCK

2 DRUG-DRUG INTERACTION

4 PROVIDER TO BE CONTACTED

6 ADVERSE DRUG REACTION

7 BAD ADDRESS

8 PER PATIENT REQUEST

9 CONSULT/PRIOR APPROVAL NEEDED

98 OTHER/TECH (NON-CLINICAL)

99 OTHER/RPH (CLINICAL)

If the user has the PSO TECH ADV security key, the following HOLD reasons are available:

HOLD REASON: ?

Enter reason medication is placed in a 'Hold' status.

Choose from:

1 INSUFFICIENT QTY IN STOCK

7 BAD ADDRESS

8 PER PATIENT REQUEST

98 OTHER/TECH (NON-CLINICAL)

The same conditions apply for Unholding a prescription. Users with the PSORPH security key can unhold for the following reason:

1 INSUFFICIENT QTY IN STOCK

2 DRUG-DRUG INTERACTION

4 PROVIDER TO BE CONTACTED

6 ADVERSE DRUG REACTION

7 BAD ADDRESS

8 PER PATIENT REQUEST

9 CONSULT/PRIOR APPROVAL NEEDED

98 OTHER/TECH (NON-CLINICAL)

99 OTHER/RPH (CLINICAL)

Users with only the PSO TECH ADV security key can unhold for the following reasons:

1 INSUFFICIENT QTY IN STOCK

7 BAD ADDRESS

8 PER PATIENT REQUEST

98 OTHER/TECH (NON-CLINICAL)

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/039.png)

> **NOTE:** If a user does not have a PSORPH security key and tries to unhold a prescription, the message “The HOLD can only be removed by a pharmacist” is displayed.

Each time a user holds or unholds a prescription, an entry is created in the Activity Log. These entries include HOLD COMMENTS and the HOLD REASON when a prescription is placed on HOLD and UNHOLD COMMENTS when the prescription is removed from HOLD. Again, HOLD reasons 98 and 99 require the user to enter a HOLD comment.

Example: Activity Log with HOLD/UNHOLD Comments

Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

...

8 05/10/12 HOLD REFILL 1 USER,PHARMACY

Comments: Rx placed on HOLD (Reason: BAD ADDRESS) and removed from

SUSPENSE - HOLD COMMENTS ENTERED BY THE USER MANUALLY.

...

9 05/10/12 UNHOLD REFILL 1 USER,PHARMACY

Comments: Rx Removed from HOLD - UNHOLD COMMENTS ENTERED BY THE USER

WHEN REMOVING THE RX FROM HOLD.

## Renewing a Prescription 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows the pharmacy technician to process renewals for existing orders.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/040.png) If the order utilizes the <span id="p477_143_Except_no_copy_ref" class="anchor"></span>EXCEPT conjunction, renew will no longer be allowed. The message bar will display: Cannot be renewed – invalid Except conjunction

Example: Renewing a Prescription

*\[This example begins after an order has been selected from the Medication Profile screen.\]*

OP Medications (ACTIVE) Jun 12, 2001 15:08:43 Page: 1 of 3

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/1999)

DOB: APR 3,1941 (60) Wt(kg): 90.45 (02/08/1999)

SEX: MALE

CrCL: 78.1(est.) (CREAT:1.0mg/dL 2/19/99) BSA (m2): 2.08

Rx \#: 503886\$

\(1\) \*Orderable Item: DIGOXIN CAP,ORAL

\(2\) CMOP Drug: DIGOXIN (LANOXIN) 0.2MG CAP

NDC: 00056-0176-75

\(3\) \*Dosage: .2 (MG)

Verb: TAKE

Dispense Units: 1

Noun: CAPSULE

\*Route: ORAL (BY MOUTH)

\*Schedule: Q12H

(4)Pat Instructions: TAKE AFTER MEALS

Provider Comments: TAKE AFTER MEALS

SIG: TAKE ONE CAPSULE BY MOUTH EVERY 12 HOURS TAKE AFTER MEALS

\(5\) Patient Status: SERVICE CONNECTED

\(6\) Issue Date: 05/07/01 (7) Fill Date: 05/07/01

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// RN Renew

FILL DATE: (6/12/2001 - 6/13/2002): TODAY// \<Enter\>  
MAIL/WINDOW: WINDOW// \<Enter\> WINDOW

METHOD OF PICK-UP: \<Enter\>

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO// Y ES

WAS COUNSELING UNDERSTOOD: NO// Y ES

Do you want to enter a Progress Note? No// \<Enter\> NO

Now Renewing Rx \# 503886 Drug: DIGOXIN (LANOXIN) 0.2MG CAP

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

503886A DIGOXIN (LANOXIN) 0.2MG CAP QTY: 60

\# OF REFILLS: 5 ISSUED: 06-12-01

SIG: TAKE ONE CAPSULE BY MOUTH EVERY 12 HOURS TAKE AFTER MEALS

FILLED: 06-12-01

ROUTING: WINDOW PHYS: OPPROVIDER4,TWO

Edit renewed Rx ? Y// \<Enter\> ES

At this point, the order can be edited as discussed in the Editing a New Order example. If the order is not edited, the order is renewed and the display returns to the Medication Profile screen.

The user may renew more than one order on the same patient by typing the desired order numbers separated by a comma (for example: 1,3, and 5).

After the edits are made, the order is redisplayed and it can be re-edited or accepted.

If an order was entered before patch PSO\*7\*46 update, the user will be prompted to fill in any missing dosing information needed as illustrated in this example.

Example: Renewing a Prescription (continued)

Edit renewed Rx ? Y// NO

Dosing Instruction Missing!!  
  
Drug: CALCIUM CARBONATE 650MG TAB

TAKE 1 TABLET(S) BY MOUTH THREE TIMES A DAY

FILLED: 04-02-01

ROUTING: WINDOW PHYS: OPPROVIDER29,TWO

Edit renewed Rx ? Y// \<Enter\> ES

There are 2 Available Dosage(s):

1\. 650MG

2\. 1300MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 650MG

You entered 650MG is this correct? Yes// \<Enter\> YES

DISPENSE UNITS PER DOSE(TAB): 1// \<Enter\> 1

Dosage Ordered: 650MG

ROUTE: PO// \<Enter\> ORAL PO MOUTH

Schedule: TID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

TID TID THREE TIMES A DAY

...OK? Yes// (Yes)

(THREE TIMES A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): \<Enter\>

CONJUNCTION: \<Enter\>

PATIENT INSTRUCTIONS: \<Enter\>

(TAKE ONE TAB BY MOUTH THREE TIMES A DAY)

1460971A CALCIUM CARBONATE 650MG TAB QTY: 100

\# OF REFILLS: 10 ISSUED: 04-02-01

SIG: TAKE ONE TAB BY MOUTH THREE TIMES A DAY

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/041.png)

Original Provider Comments are not carried over to any renewals in Outpatient Pharmacy.

### Renewing an ePharmacy Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When renewing an ePharmacy order, upon acceptance of the renewed order the original prescription will be discontinued and a new order created. If the latest fill of the original order has not been released and is E Payable, the claim for that fill will be reversed. A new claim is submitted for the new prescription.

*\[This example begins after an order is selected from the Medication Profile screen.\]*

OP Medications (ACTIVE) Nov 04, 2005@11:48:14 Page: 1 of 3

OPPATIENT,FOUR

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: NOV 12,1975 (29) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 100003642\$e

(1) \*Orderable Item: SIMETHICONE TAB,CHEWABLE

\(2\) Drug: SIMETHICONE 40MG TAB

NDC: 00056-0176-75

\(3\) \*Dosage: 40 (MG)

Verb: CHEW

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: TID

(4)Pat Instructions:

SIG: CHEW ONE TABLET BY BY MOUTH THREE TIMES A DAY

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 08/11/05 (7) Fill Date: 08/11/05

Last Fill Date: 08/11/05 (Window)

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// RN Renew

FILL DATE: (11/4/2005 - 11/5/2006): TODAY// \<Enter\> (NOV 04, 2005)

MAIL/WINDOW: WINDOW// \<Enter\>WINDOW

METHOD OF PICK-UP: \<Enter\>

Nature of Order: WRITTEN// \<Enter\> W

WAS THE PATIENT COUNSELED: NO//\<Enter\> NO

Now Renewing Rx \# 100003642 Drug: SIMETHICONE 40MG TAB

Now doing remote order checks. Please wait...

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please Wait...

100003642A SIMETHICONE 40MG TAB QTY: 90

\# OF REFILLS: 5 ISSUED: 11-04-05

SIG: CHEW ONE TABLET BY BY MOUTH THREE TIMES A DAY

FILLED: 11-04-05

ROUTING: WINDOW PHYS: OPPROVIDER4,TWO

Edit renewed Rx ? Y// \<Enter\> ES

Example: Renewing an ePharmacy Order (continued)

\[To save space, only the second Prescription Renew screen is displayed in this example.\]

Prescription Renew Jun 04, 2001 16:18:17 Page: 2 of 2

OPPATIENT,FOUR

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: NOV 12,1975 (29) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

\+

Days Supply: 30

QTY ( ): 90

\(3\) \# of Refills: 5

\(4\) Routing: WINDOW

\(5\) Clinic:

\(6\) Provider: OPPROVIDER4,TWO

\(7\) Copies: 1

\(8\) Remarks: RENEWED FROM RX \# 100003642

Entry By: OPPHARMACIST4,THREE Entry Date: NOV 4,2005 11:56:31

Enter ?? for more actions

AC Accept DC Discontinue

BY Bypass ED Edit

Select Item(s): Quit// 5

CLINIC: 3EN

Prescription Renew Jun 04, 2001 16:24:32 Page: 2 of 2

OPPATIENT,FOUR

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: NOV 12,1975 (29) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

\+

Days Supply: 30

QTY ( ): 90

\(3\) \# of Refills: 5

\(4\) Routing: WINDOW

\(5\) Clinic:

\(6\) Provider: OPPROVIDER4,TWO

\(7\) Copies: 1

\(8\) Remarks: RENEWED FROM RX \# 100003642

Entry By: OPPHARMACIST4,THREE Entry Date: NOV 4,2005 11:56:31

Enter ?? for more actions

AC Accept DC Discontinue

BY Bypass ED Edit

Select Item(s): Quit// AC Accept

SC Percent: 40%

Disabilities: NONE STATED

Was treatment for Service Connected condition? NO// \<Enter\>

Reversing prescription 100003642.

Claim Status:

Reversing and Rebilling a previously submitted claim...

Reversing...

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Waiting to process response

E REVERSAL ACCEPTED

-Rx 100003642 has been discontinued...

Veteran Prescription 100003642A successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Packet being built

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Receiving response

E PAYABLE

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/042.png)

Original Provider Comments are not carried over to any renewals in Outpatient Pharmacy.

# Chapter 10: Pull Early from Suspense

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options used for handling suspended prescriptions.

# Pull Early from Suspense

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO PNDRX\]

This option is used to pull a specific prescription or all prescriptions for a patient early. If a prescription is pulled early using this option, it will not be associated with any printed batch, and the user will not be able to reprint a label with the *Reprint Batches from Suspense* option. Since prescriptions that are pulled early from suspense do not belong to any printed batch and cannot be reprinted from suspense, there is no reason to leave them in suspense.

The user may also edit the “Method of Pickup”. For the prompt "Pull Rx(s) and delete from Suspense", the user should answer YES to pull the prescriptions.

If the Label Long indicates that a Label has already printed for this prescription and fill, then the user is asked whether to continue. If the user chooses “No”, the label will not print. In addition, the prescription shall be removed from Suspense unless the suspense queue indicates that a user has previously requested a reprint of the suspended prescription. If the user chooses “Yes”, the prescription shall continue and will print the label. In the example below, the label will not print but the Prescription will be left on Suspense.

Label for Rx#104872 Fill#0 has already been printed

Do you want to continue? No// No

Reprint Flag is on. Prescription left on suspense.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/043.png)If the patient has remote prescriptions, then the text “THIS PATIENT HAS PRESCRIPTIONS AT OTHER FACILITIES” will appear on the report as shown in the following example.

PRESCRIPTION PROFILE AS OF 12/30/2008

NAME: PSOPATIENT,ONE

ID# : 000-00-0000

THIS PATIENT HAS PRESCRIPTIONS AT OTHER FACILITIES

PHARMACIST: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ DATE: \_\_\_\_\_\_\_\_

If a prescription is determined to be an ePharmacy prescription (e.g., third party electronically billable), an electronic claim will be sent by ECME to the third party payer. The communication events between Outpatient Pharmacy and ECME are recorded in the ECME Log section of each prescription. The ECME log can be viewed in the patient Medication Profile screen (Activity Log option - AL) and also from the View Prescriptions option. If the claim submission returns a Refill Too Soon (79), Reject Resolution Required or Drug Utilization Review (88) reject, the label is not printed for the prescription and it is moved to the Refill Too Soon/DUR section of the patient Medication Profile screen until the user resolves the reject. The prescription will also display on the Third Party Payer Reject Worklist. If the claim submission returns a Reject Resolution Required reject, the label is not printed for the prescription and it is moved to the Reject Resolution Required section of the Third Party Payer Reject Worklist.

# Chapter 11: Queue CMOP Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the option for suspending prescriptions for mail-routed CMOP drugs.

# Queue CMOP Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO RX QUEUE CMOP\]

The *Queue CMOP Prescription* option allows the users (including pharmacy technicians) to put mail-routed prescription(s) for CMOP drugs on suspense for CMOP.

Example: Queue CMOP Prescription

Select Suspense Functions Option: QUEUE CMOP Prescription

Enter the Rx \# to queue to CMOP: 300486

If the prescription does not have a routing of Mail, has already been released, or is not for a CMOP drug, and does not pass all the other normal checks for CMOP, it will not be put on suspense for CMOP.

(*This page included for two-sided copying.)*

# Chapter 12: Releasing Medication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the option used for releasing medications.

# Release Medication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO RELEASE\]

The *Release Medication* option is used at the time the prescription is filled and ready to be given to the patient. Inventory is decreased, certain fields in the file are updated, and a copay is generated if the action is applicable to the prescription. With this option, prescriptions can be batch processed. Communication is made with the Integrated Funds Control, Accounting and Procurement (IFCAP) and Integrated Billing (IB) software to generate copay charges. IFCAP and IB software handle patient billing, tracking of charges, and payment received.

The copay status of a prescription is re-evaluated whenever a fill is released. Various actions can occur based on changes to the criteria that determine the copay status of a prescription. The actions that may result at the time a fill is released are described below.

1.  No action is taken. No changes to the criteria that determine copay status of a prescription have occurred.
2.  The copay status of the prescription is automatically reset and an entry is placed in the Copay activity log.Example: The drug for which the prescription is written is no longer marked for investigational use. The copay status of the prescription is reset from No Copayment to Copay.

> 3\. The copay status of the prescription is automatically reset, an entry is placed in the Copay activity log, and a MailMan message is generated detailing missing information required for user follow-up.Example: The drug for which the prescription is written is no longer marked for investigational use. The copay status of the prescription is reset from No Copayment to Copay. The patient has been documented as being exposed to Southwest Asia Conditions (SWAC) during Persian Gulf War service since the last fill. A MailMan message will be generated informing the user that the ‘Is this Rx for treatment related to service in SW Asia?’ question must be addressed and documented using the *Reset Copay Status/Cancel Charges* option.

4.  A MailMan message is generated detailing missing information required for user follow-up.Example: A Veteran is documented as having Agent Orange exposure. Refill \#2 for a prescription entered into the system before the new medication copay exemptions took effect on January 1, 2002 is released. The prescription is copay eligible. A MailMan message will be generated informing recipients that the ‘Is this Rx for treatment of Vietnam-Era Herbicide (Agent Orange) exposure?’ question must be addressed. The copay status of the prescription may change based on the response entered using the *Reset Copay Status/Cancel Charges* option.

If a MailMan message is generated at the time a prescription fill is released, the recipients of the message will be the provider of record, the pharmacy user who finished the order, and holders of the PSO COPAY key. The message lists the patient name, prescription number, and medication ordered, current copay status, and applicable copay exemption questions that need addressing to determine the prescription’s copay status. The *Reset Copay Status/Cancel Charges* option must be used to enter the responses to the medication copay exemption questions listed in the MailMan message. If responses are not entered for the applicable medication copay exemption questions, any subsequent refills when released for this prescription and possibly other prescriptions for this patient will continue to generate the same MailMan message.

Example: MailMan Message

Subj: PRESCRIPTION QUESTIONS REVIEW NEEDED (500) \[#30364\] 10/11/05@19:56

35 lines

From: OUTPATIENT PHARMACY PACKAGE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

OPPATIENT29,ONE (6543P) CHEYENNE VAM&ROC

Eligibility: SC LESS THAN 50% SC%: 20

REIMBURSABLE INSURANCE

Disabilities: ARTHRITIS-10%(SC), FOREARM CONDITION-5%(NSC),

FOREARM CONDITION-4%(NSC), BENIGN EYE GROWTH-0%(NSC),

LOSS OF FIELD OF VISION-20%(SC),

Rx# 101906 (1) COPAY

ALBUTEROL SO4 0.083% INHL 3ML

Due to a change in criteria, additional information listed below is needed

to determine the final VA copay and/or insurance billable status for this Rx

so that appropriate action can be taken by pharmacy personnel.

Is this Rx for a Service Connected Condition?

Is this Rx for treatment related to service in SW Asia?

This message has been sent to the provider of record, the pharmacist who

finished the prescription order, and all holders of the PSO COPAY key.

Enter RETURN to continue or '^' to exit: \<Enter\>

Subj: PRESCRIPTION QUESTIONS REVIEW NEEDED (500) \[#30364\] Page 2

-------------------------------------------------------------------------------

Providers:

Please respond with your answer to the question(s) as a reply to this

message. The prescription will be updated by the appropriate staff.

Staff assigned to update the Prescription responses:

Please use the RESET COPAY STATUS/CANCEL CHARGES option to enter the responses

to the questions above, which may result in a Rx copay status change and/or

the need to remove VA copay charges or may result in a charge to the patient's

insurance carrier.

> **NOTE:** The SC question is now asked for Veterans who are SC\>49% in order to

determine if the Rx can be billed to a third party insurance. These Veterans

will NOT be charged a VA copay.

Supply and investigational drugs are not charged a VA copay but could be

reimbursable by third party insurance.

Enter message action (in IN basket): Ignore//

An annual copayment cap is applied to patients in specific priority enrollment groups. Once a patient reaches the annual copayment cap, no further medication copay charges will be billed for the calendar year. An entry to that effect is made to the Copay Activity Log. The ‘\$’ indicator remains next to the prescription number to indicate that the prescription is still copay eligible.

Integrated Billing software keeps track of all prescription fills not billed due to the annual cap.

Example: Copay Activity Log When Annual Cap Reached

Copay Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

===============================================================================

1 10/23/01 ANNUAL CAP REACHED ORIGINAL OPPROVIDER11,TWO

Comment: NO BILLING FOR THIS FILL

If for whatever reason (e.g. prescription fill is returned to stock and copay charges cancelled), a patient falls below the annual copayment cap, the Integrated Billing package can initiate copay charges to bring the patient back up to the annual copayment cap. Integrated billing software will go back and bill a copay charge for those fills previously not charged due to the annual cap, bringing the patient’s total copayment up to the cap. Whenever this occurs an entry will be placed in the Copay activity log.

Example: Copay Activity Log with IB-Initiated Charge

Copay Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

===============================================================================

1 10/23/01 ANNUAL CAP REACHED ORIGINAL OPPROVIDER11,TWO

Comment: NO BILLING FOR THIS FILL

2 10/23/01 IB-INITIATED COPAY ORIGINAL OPROVIDER11,TWO

Comment: PARTIAL CHARGE

If a prescription is <u>not</u> in a releasable status, the user will be given an error message, such as:

- Prescription has a status of (status) and is not eligible for release.
- Prescription was deleted.
- Improper barcode format.
- Non-existent prescription.

Copay is not charged for a partial fill.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/044.png)Important: This is a mandatory function that the pharmacy must use.

## Fixed Medication Copayment Tiers (FMCT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*460 introduces copay tiers for drugs. The Chief Business Office (CBO) requests updating IT systems to conform with changes to qualified prescription medications within VistA and VA National and Local Drug Files, to establish fixed copayment amounts depending on the class of medication (Tier 1, Tier 2, or Tier 3) while still maintaining the utility of the \$700 copayment cap per calendar year for PG 2-8, as applicable, on an individual Veteran basis. The PBM is requesting the addition of Tier 0 for excluded and exempt products with no copayment. Changes to Outpatient Pharmacy will be seen in the copay activity log.

Rx \#: 100002266   Original Fill Released: 08/23/16                             

Routing: Window      Finished by: CROSSMAN,PAMELA                              

                                                                                

Copay Activity Log:                                                            

\#   Date        Reason               Rx Ref         Initiator Of Activity      

===============================================================================

1   08/23/16    COPAY RESET          ORIGINAL       CROSSMAN,PAMELA            

Comment: Copay Tier 1  Old value=No Copay   New value=Copay                    

## Changes to Releasing Orders Function - Digitally Signed Orders Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release function in the *Patient Prescription Processing* option has been modified with patch PSO\*7\*131 to require that all digitally signed orders for Schedule II controlled substances (CSII orders) be released through the *Outpatient Rx’s* option in the *ControlledSubstances* (CS) menu. If DEA/PKI is activated and an order is digitally signed, the user is advised that the order must be released through the *Outpatient Rx’s* option in the *ControlledSubstances* (CS) menu. The same message displays if a user attempts to release a digitally signed CSII order during Speed Release or when using the *Release Medication* option.

A new security key named "PSDRPH", was introduced by the Controlled Substances patch PSD\*3\*76 that authorizes pharmacists to finish/verify digitally signed Schedule II-V CS orders placed via CPRS.

When processing a digitally signed pending order, the integrity of the original order placed in CPRS is now being checked to ensure that the data fields listed below are not altered from the time the order is signed in CPRS and later selected for processing in backdoor pharmacy. This is done by passing the data elements listed below to a Kernel Application Programming Interface (API), Integration Control Registration (ICR) \#3539 along with the CPRS hash count provided by ICR \#5709. The Kernel API compares these two hash values and returns an "OK" if the pending order is unaltered; otherwise, a "-1^error code^error message" is returned.

Example: "-1^89802016^Mismatched digital signature hash values."

The following fields are used in the hash check:

- Date of Issuance
- Full Name and Address of the Patient
- Drug Name
- Quantity Prescribed
- Directions for Use
- Prescriber Name
- Prescriber Address (site address)
- Prescriber DEA / VA Registration Number
- Order Number (CPRS)

The Kernel API will also check for the validity of the DEA certificate. If the certificate is revoked or expired, the API will return the appropriate error code. If the error code is related to hash mismatch, or the DEA certificate is revoked, the following events will be triggered during pending order processing:

- The order will be auto discontinued.
- First line of the pending order screen will have the message "Digital Signature Failed: Corrupted (Hash mismatch)" or "Certificate revoked" concatenated with "Order Auto Discontinued", and the message will be highlighted.
- The status bar of the screen will have the message "Signature Failed: Corrupted (Hash mismatch)" or Certificate revoked."

A mail message will be generated to the holders of the PSDMGR key notifying that the order has been auto-discontinued (similar to the example listed below). If the discontinuation is due to a hash mismatch as a result of altering one of the fields listed above, the mail message will show the altered fields with the discrepancies as shown in the following example.

Example: Mail Message of Discontinuation Due to Hash Mismatch

Subj: DIGITALLY SIGNED NEW ORDER AUTO DISCONTINUED \[#196353\]

03/20/12@17:1024 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------

Following order was auto discontinued when finishing a pending order

due to Corrupted (Hash mismatch) - 89802016

Division : GREELEY CLINIC

CPRS Order \# : 5587651

Issue Date : MAR 7,2012

Patient : TEST,PATIENT (0908)

Address : P.O. BOX 31

LAPORTE, CA 95981

Drug : CODEINE SULFATE 60MG TAB

Dosage Ordered: 120(MG)

Dosage Form : TABLETS

Quantity : 54

Provider : TEST,PROVIDER

DEA# : TA1234563

Site Address : 2360 E PERSHING BLVD

2360 East Pershing Boulevard

CHEYENNE

Differences in CPRS and Pharmacy Pending File

Data Name CPRS File Pharmacy Pending File

--------- --------- ---------------------

QTY PRESCRIBED 15 30

If the error code is related to 'certificate expired', the pending order will be processed (will not be auto-discontinued), and a notification will be sent to the provider with the message "DEA certificate expired. Renew your certificate."

The following changes have been made for finishing a CS order:

- When finishing a pending CS order, if the user does not hold the new PSDRPH security key, the order will be marked as 'Non-Verified'. To verify a 'Non-Verified' CS order, the PSDRPH security key is now required. To discontinue a pending CS order, the PSDRPH security key is now required.
- The pending order screen will now display the provider's DEA/VA \#, the DETOX# (if available), and the site address.
- When finishing a new pending CS order, the dosage, provider name, or the number of refills will not be allowed editing; however, the user will be allowed to select other possible dosages for the same drug if available. If the changes to the dispense drug results in creating a new order, the user will be notified by the message " Digitally Signed Order - No such changes allowed." If pharmacy wants to make such changes, then they have to discontinue (DC) the pending order and start a new order. However, the user will be allowed to select other possible dosages for the same drug that does not change the prescribed dosage.
- When finishing a new pending CS order, the day supply or the quantity will not be allowed to increase but can be decreased. If the day supply is decreased, the number of refills will also be adjusted accordingly depending on the drug setup (maximum refills, not refillable, etc.). The quantity may be auto-calculated to a higher quantity by the system only when the dosage remains the same, but the dispense drug strength is changed – i.e. 2mg tablets \#30 is changed to 1mg tablets, the Sig is updated, and the system changes the quantity to 60. A manual change to a higher quantity is not allowed.
- When finishing a pending CS order or verifying a CS order by the PSDRPH key holder, any edit to some of the key fields, such as dispense drug, dosage, dispense units, issue date, day's supply, quantity or number of refills, will now be captured and stored in the activity log.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/045.png)Note: In patch PSO\*7\*99, a change was made for pending orders not to recalculate the quantity for CS drugs on selecting a different strength of the same drug and resulting in the same prescribed dosage. This change is removed in patch PSO\*7\*391.

## Changes to Releasing Orders Function - ScripTalk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release function in the *Patient Prescription Processing* option has been modified to display a message to the user when the site is using a Bingo Board and when the patient is enrolled in ScripTalk. This message will alert the user that the patient is enrolled in ScripTalk and may need to have a verbal announcement that the prescription(s) is ready, instead of a visual announcement.

Example: Releasing Medication to a ScripTalk Patient

Prescription Number 400693 Released

No Refill(s) to be Released

No Partial(s) to be Released

OPPATIENT16,ONE added to the WAITING display.

This patient is enrolled in ScripTalk and may benefit from

a non-visual announcement that prescriptions are ready.

Press Return to Continue:

## Changes to Releasing Orders Function – Signature Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Patch PSO\*7\*385, the release function in the *Patient Prescription Processing* option has been modified to display a message to the user when an ECME-billable prescription is being released as a window fill. This message will alert the user that the patient’s signature must be obtained. The user is not required to press \<Enter\> to continue or respond to the alert in any other manner.

Example: Releasing an ePharmacy Window Fill

Prescription Number 100003853 Released

No Refill(s) to be Released

No Partial(s) to be Released

ePharmacy Rx – Obtain Signature

## Changes to Releasing Orders function – HIPAA NCPDP Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release function has been modified with patch PSO\*7\*148 to perform National Drug Code (NDC) validation for ePharmacy prescriptions. These changes also affect the Controlled Substance prescription release, which is performed through the Controlled Substances package.

The user releasing the third-party electronically billable prescription will be prompted for the NDC for the drug being dispensed to the patient. The NDC code previously retrieved when the prescription was finished will be presented as the current (default) NDC for the prescription. The other possible values that the user will be able to choose from are:

- NDC field value in the DRUG file, if valid and different than the current prescription NDC.
- LAST LOCAL NDC field value in NDC BY OUTPATIENT SITE sub-file in the DRUG file for the division filling the prescription, if valid and different that the current prescription NDC.
- NDC CODE field values in the SYNONYM sub-file in the DRUG file, if valid and different that the current prescription NDC.

If the NDC dispensed is not on the list to select, the user must contact the ADPAC or other designated person to add the NDC in a synonym multiple for that drug in the DRUG file.

If the NDC code selected matches the current NDC in the prescription no further NDC processing is required. However, if the user selects a different NDC, the following steps will occur:

1.  Outpatient Pharmacy V. 7.0 will instruct the Electronic Claims Management Engine (ECME) to reverse the previous claim for the previous NDC code and submit a new claim for the newly selected NDC code.
2.  The newly selected NDC code will be saved in the LAST LOCAL NDC field in NDC BY OUTPATIENT SITE sub-file in the DRUG file for the division filling the prescription.

The following examples show the new prompt for NDC validation during the release process. For ePharmacy prescriptions, the releasing pharmacist will receive a notation as to whether the NDC was previously validated. If prior validation of the NDC resulted in a third party claims rejection, the pharmacist will be presented with a Reject Processing screen at release.

Example: Releasing an ePharmacy Order – Selecting Default NDC

Select Outpatient Pharmacy Manager Option: RELEASE Medication

Enter PHARMACIST: OPPHARMACIST4,THREE

Enter/Wand PRESCRIPTION number: 100003853

\*\* The following NDC was validated on SEP 19, 2008@16:21:23 by OPTECH,ONE.

NDC: 00580-0277-10// ?

Select one of the following valid NDC code(s) below:

1 - 00580-0277-10

NDC: 00580-0277-10// \<Enter\> 00580-0277-10

Prescription Number 100003853 Released

No Refill(s) to be Released

No Partial(s) to be Released

ePharmacy Rx – Obtain Signature

Example: Releasing an ePharmacy Order – Selecting Different NDC

Select Outpatient Pharmacy Manager Option: RELEASE Medication

Enter PHARMACIST: OPPHARMACIST4,THREE

Enter/Wand PRESCRIPTION number: 100003853

NDC: 00580-0277-10// ?

Select one of the following valid NDC code(s) below:

1 - 00580-0277-10

2 - 00580-0277-14

NDC: 00580-0277-10// 2 00580-0277-14

Veteran Prescription 100003853 successfully submitted to ECME for claim generation.

Claim Status:

Reversing and Rebilling a previously submitted claim...

Reversing...

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

Resubmitting...

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Waiting to process response

E PAYABLE

Prescription Number 100003853 Released

No Refill(s) to be Released

No Partial(s) to be Released

# Chapter 13: Updating a Patient’s Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the option used for updating a patient’s record.

# Update Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO PAT\]

Use this option to update the patient information currently in the computer and to update patient records being viewed by using the *Patient Record Update* screen action. If implementing Other Language Modifications, use either to set a patient’s other language preference.

In support of Registration patch DG\*5.3\*522, the Outpatient Pharmacy software provides for the automatic population of city, state, and county based on entry of a zip code.

Example: Updating a patient record

Bingo Board Display: OUTPATIENT// \<Enter\>

Update Patient Record

Select Patient: OPPATIENT,ONE 12-4-53 000007890 YES SC VETERAN

OPPATIENT, ONE ID#: 000-00-7890

4500 S MAIN ST DOB: DEC 4,1953

ADDRESS LINE2

LINE 3 OF ADDRESS

MADISON PHONE: 555-555-1653

WISCONSIN 53705 ELIG: SC LESS THAN 50%

SC%: 10

WEIGHT(Kg): HEIGHT(cm):

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2):

DISABILITIES: ARTHRITIS-10% (SC), FOREARM CONDITION-5% (NSC),

FOREARM CONDITION-4% (NSC), BENIGN EYE GROWTH-0% (NSC),

LOSS OF FIELD OF VISION-20% (SC),

ALLERGIES:

ADVERSE REACTIONS:

If the PSO site parameter is set to allow editing of patient data, this prompt, “Do you want to update the Permanent address/phone? //N”, is displayed. If the user enters “NO”, then the software will not allow the user to update the permanent address and Bad Address Indicator fields.

Do you want to update the address/phone? NO// YES

Update (P)ermanent address, (T)emporary, or (B)oth: BOTH// PERMANENT

STREET ADDRESS \[LINE 1\]: 4500 S MAIN ST// 4800 S MAIN ST

STREET ADDRESS \[LINE 2\]: ADDRESS LINE2// \<Enter\> ADDRESS LINE2

STREET ADDRESS \[LINE 3\]: LINE 3 OF ADDRESS// \<Enter\> LINE 3 OF ADDRESS

ZIP+4: 53705// \<Enter\> 53705

Select one of the following:

1 MADISON\*

CITY: MADISON// \<Enter\> \*

STATE: WISCONSIN

COUNTY: DANE

PHONE NUMBER \[RESIDENCE\]: 555-555-1653// 555-555-1653

PHONE NUMBER \[WORK\]:

BAD ADDRESS INDICATOR: ?

Please enter 1 if the address is 'UNDELIVERABLE', 2 if the patient

is 'HOMELESS', or 3 for 'OTHER' bad address reasons.

Choose from:

1 UNDELIVERABLE

2 HOMELESS

3 OTHER

Are you sure that you want to save the above changes? YES

Change saved.

Changes to the permanent address/Bad Address Indicator will not be saved until the prompt “Are you sure that you want to save the above changes?” is answered YES.

Press ENTER to continue: \<Enter\>

Temporary Address:

TEMPORARY ADDRESS ACTIVE?: NO// \<Enter\> NO

Press Return to continue: \<Enter\>

PHONE NUMBER \[CELLULAR\]: \<Enter\>

CNH CURRENT: \<Enter\>

FEE HOSPITAL I.D.: \<Enter\>

REMARKS: \<Enter\>

\>\>PHARMACY PATIENT DATA\<\<

CAP: \<Enter\>

MAIL: \<Enter\>

MAIL STATUS EXPIRATION DATE: \<Enter\>

DIALYSIS PATIENT: \<Enter\>

NARRATIVE: \<Enter\>

Eligibility: COLLATERAL OF VET. \<Enter\>

Disabilities: \<Enter\>

PATIENT STATUS: SERVICE CONNECTED// \<Enter\>

COMMUNITY NURSING HOME: \<Enter\>

NURSING HOME CONTRACT: \<Enter\>

LAST DATE OF CONTRACT: \<Enter\>

RESPITE PATIENT START DATE: \<Enter\>

RESPITE PATIENT END DATE: \<Enter\>

OTHER LANGUAGE PREFERENCE: \<Enter\>

PMI LANGUAGE PREFERENCE: \<Enter\>

# # Chapter 14: Meds by Mail – Virtual Pharmacy Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because Virtual Pharmacy Services (VPS) users have to sign into multiple VistA systems across the nation to support the Meds by Mail (MBM) program, a Class I menu option was delivered with patch PSO\*7\*630 to improve and standardize processing outpatient pending prescription queues regardless of the facility assigned.

The MbM-VPS Pharmacy Users Menu \[PSO MBM-VPS PHARMACY MENU\] and the MbM-VPS Productivity Report \[PSO MBM-VPS PRODUCTIVITY RPT\] were delivered with patch PSO\*7\*630. With the exception of the MbM-VPS Productivity Report, the other 4 options listed under this menu are pre-existing options.

Example of new menu and options:

MbM-VPS Pharmacy Users Menu PSO MBM-VPS PHARMACY MENU M

bM-VPS Pharmacy Users Menu

C Complete Orders from OERR

P Patient Prescription Processing

V View Prescriptions

L Lookup into Dispense Drug File

R MbM-VPS Productivity Report

Selecting R MbM-VPS Productivity Report allows the user to run the new report. The following are more details of the report implementation:

- User is prompted for beginning and ending FINISH DATE/TIME
- The resulting report is created per date range provided and includes columns for Finishing Person and Prescriptions Finished.
  1.  Selected date range is shown at the top of the report.
  2.  Result is sorted by Finishing Person.
  3.  Grand total of all Prescriptions Finished is provided at the bottom of the report.

Example of running the MbM-VPS Productivity Report:

Select MbM-VPS Pharmacy Users Menu \<TEST ACCOUNT\> Option: R MbM-VPS Productivit

y Report

This report prints a listing of people who finished the order in pharmacy

in the user-selected date range.

Starting with Date: 1/1 (JAN 01, 2021)

Ending with Date: TODAY (MAY 06, 2021)

DEVICE: HOME// ;;999 Linux Telnet /SSh

VPS Productivity Report Run Date: MAY 06, 2021@15:51

Rx Orders finished from JAN 01, 2021 through MAY 06, 2021 Page: 1

Prescriptions

Finishing Person Finished

-------------------------------------------------------------------------------

PHARMACIST,ONE 13

PHARMACIST,TWO 2

PHARMACIST,THREE 33

PHARMACIST,FOUR 11

PHARMACIST,FIVE 6

PHARMACIST,SIX 14

PHARMACIST,SEVEN 63

======

Grand Total: 142

# Chapter 15: CPRS Order Checks: How They Work

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during the ordering session and is driven by responses entered by the ordering provider. Order Check messages are displayed interactively in the ordering session.

Order Checks review existing data and current events to produce a relevant message, which is presented to patient caregivers. Order Checks use the CPRS Expert System (OCX namespace), to define logical expressions for this evaluation and message creation. In addition to the expert system Order Checks have some hard-coded algorithms. For example, the drug-drug interaction order check is made via an entry point in the pharmacy package whereas Renal Functions for Patients 65 and Over is defined as a rule in the CPRS Expert System.

## Order Check Data Caching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data caching was recently added to improve the speed of order checks. Before data caching, order checks could be slow because each order check retrieved data from the other VISTA packages—even if the order checks used the same data. With data caching, the first order check in an ordering session retrieves data from other VISTA packages, uses the data to evaluate whether it should display a warning, and then stores the retrieved data in the ^XTMP(“OCXCACHE” global for five minutes. The order checks that occur in the next five minutes can use the cached data, if it is the appropriate data, instead of retrieving data from the other packages. After five minutes, the cached data expires, and order checks must retrieve new data from the VISTA packages.

For example, before data caching was implemented, if an order check took 3 seconds to retrieve data from other VISTA packages, and there were 12 order checks, clinicians might wait 36 seconds to sign orders. With data caching, the first order check might take 3 seconds to retrieve the data, but subsequent order checks could use the cache and might take only .03 seconds each. That would be 3.33 seconds compared to 36 seconds. The numbers in this example are for illustration only and do not reflect real system speed. However, data caching should speed up order checks.

To avoid using all available disk space for storing data from order checks, there are several ways to clear the ^XTMP(“OCXCACHE” global. ORMTIME removes data from the global when it runs. The suggested frequency for running ORMTIME is every 30 minutes, but not every site runs it that frequently. Kernel clean up utilities also remove data from the cache when they run, which is usually every 24 hours. If needed, users that have access to the programmer’s prompt can manually clear the cache from that prompt by using PURGE^OCXCACHE.

## Hash Counts and DEA Certification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When processing a digitally signed pending order, the integrity of the original order placed in CPRS is now being checked to ensure that the data fields listed below are not altered from the time the order is signed in CPRS and later selected for processing in backdoor pharmacy. This is done by passing the data elements listed below to a Kernel Application Programming Interface (API), Integration Control Registration (ICR) \#3539 along with the CPRS hash count provided by ICR \#5709. The Kernel API compares these two hash values and returns an "OK" if the pending order is unaltered; otherwise, a "-1^error code^error message" is returned.

Example: "-1^89802016^Mismatched digital signature hash values."

The following fields are used in the hash check:

- Date of Issuance
- Full Name and Address of the Patient
- Drug Name
- Quantity Prescribed
- Directions for Use
- Prescriber Name
- Prescriber Address (site address)
- Prescriber DEA / VA Registration Number
- Order Number (CPRS)

The Kernel API will also check for the validity of the DEA certificate. If the certificate is revoked or expired, the API will return the appropriate error code. If the error code is related to hash mismatch, or the DEA certificate is revoked, the following events will be triggered during pending order processing:

- The order will be auto discontinued.
- First line of the pending order screen will have the message "Digital Signature Failed: Corrupted (Hash mismatch)" or "Certificate revoked" concatenated with "Order Auto Discontinued", and the message will be highlighted.
- The status bar of the screen will have the message "Signature Failed: Corrupted (Hash mismatch)" or Certificate revoked."

A mail message will be generated to the holders of the PSDMGR key notifying that the order has been auto-discontinued (similar to the example listed below). If the discontinuation is due to a hash mismatch as a result of altering one of the fields listed above, the mail message will show the altered fields with the discrepancies as shown in the following example.

Example: Mail Message of Discontinuation Due to Hash Mismatch

Subj: DIGITALLY SIGNED NEW ORDER AUTO DISCONTINUED \[#196353\]

03/20/12@17:1024 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------

Following order was auto discontinued when finishing a pending order

due to Corrupted (Hash mismatch) - 89802016

Division : GREELEY CLINIC

CPRS Order \# : 5587651

Issue Date : MAR 7,2012

Patient : TEST,PATIENT (0908)

Address : P.O. BOX 31

LAPORTE, CA 95981

Drug : CODEINE SULFATE 60MG TAB

Dosage Ordered: 120(MG)

Dosage Form : TABLETS

Quantity : 54

Provider : TEST,PROVIDER

DEA# : TA1234563

Site Address : 2360 E PERSHING BLVD

2360 East Pershing Boulevard

CHEYENNE

Differences in CPRS and Pharmacy Pending File

Data Name CPRS File Pharmacy Pending File

--------- --------- ---------------------

QTY PRESCRIBED 15 30

If the error code is related to 'certificate expired', the pending order will be processed (will not be auto-discontinued), and a notification will be sent to the provider with the message, "DEA certificate expired. Renew your certificate."

The following changes have been made for finishing a CS order:

- When finishing a pending CS order, if the user does not hold the new PSDRPH security key, the order will be marked as 'Non-Verified'. To verify a 'Non-Verified' CS order, the PSDRPH security key is now required. To discontinue a pending CS order, the PSDRPH security key is now required.
- The pending order screen will now display the provider's DEA/VA \#, the DETOX# (if available), and the site address.
- When finishing a new pending CS order, the dosage, provider name, or the number of refills will not be allowed editing; however, the user will be allowed to select other possible dosages for the same drug if available. If the changes to the dispense drug results in creating a new order, the user will be notified by the message "Digitally Signed Order - No such changes allowed." If pharmacy wants to make such changes, then they have to discontinue (DC) the pending order and start a new order. However, the user will be allowed to select other possible dosages for the same drug that does not change the prescribed dosage.
- When finishing a new pending CS order, the day supply or the quantity will not be allowed to increase but can be decreased. If the day supply is decreased, the number of refills will also be adjusted accordingly depending on the drug setup (maximum refills, not refillable, etc.). The quantity may be auto-calculated to a higher quantity by the system only when the dosage remains the same, but the dispense drug strength is changed – i.e. 2mg tablets \#30 is changed to 1mg tablets, the Sig is updated, and the system changes the quantity to 60. A manual change to a higher quantity is not allowed.
- When finishing a pending CS order or verifying a CS order by the PSDRPH key holder, any edit to some of the key fields, such as dispense drug, dosage, dispense units, issue date, day's supply, quantity or number of refills, will now be captured and stored in the activity log.

![](outpatient-pharmacy-version-7-technician-user-manual-updated-pso-7-630/046.png)Note: In patch PSO\*7\*99, a change was made for pending orders not to recalculate the quantity for CS drugs on selecting a different strength of the same drug and resulting in the same prescribed dosage. This change is removed in patch PSO\*7\*391.

# Chapter 16: Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Information

The text in the error message and reason column will be displayed to the user. The type of error is displayed in column 1.

Three Levels of Error Messages

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>System</strong></th>
<th>When such an error occurs, no Drug Interaction, Duplicate Therapy, or Dosing order checks will be performed. Other order checks that do not use the COTS database (FDB) will still be performed such as allergy/ADRs, duplicate drug (for outpatient only) and new CPRS order checks, etc.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Drug</strong></td>
<td><p>The second error level is for the drug and no Drug Interaction/Duplicate Therapy or Dosing order checks will be performed for a specific drug. Drug level errors can occur for the prospective drug (drug being processed) or the profile drug. If a drug level error occurs on the prospective drug, no profile drug errors will be displayed. The only exception to this is when you are processing an IV order with multiple prospective drugs (i.e. multiple IV Additives). Profile drug level errors will only be shown once per patient session.</p>
<p>There are two reasons that a drug level error is generated; the drug is not matched to NDF or the drug is matched to NDF, but the VA Product to which it is matched does not have a GCNSEQNO assigned or the GCNSEQNO assigned does not match up to the GCNSEQNO in the COTS database. The latter (GCNSEQNO mismatch) is rare.</p></td>
</tr>
<tr class="even">
<td><strong>Order</strong></td>
<td>The third error level is for the order. Order level errors will only occur with dosing order checks. Please see the <a href="http://vaww.oed.portal.va.gov/projects/pre/PRE_TW/MOCHA%20v2x%20PDFs/Assignments%20and%20Schedule/Kiley&#39;s%20Assignments/Dosing_Order_Check_User_Manual.doc"><em>Dosing Order Check User Manual</em></a> for more information.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 20%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
<th><strong>Why message is being displayed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>Vendor Database cannot be reached.</td>
<td>The connectivity to the vendor database has gone down. A MailMan message is sent to the G. PSS ORDER CHECKS mail group when the link goes down and when it comes back up.</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>The connection to the vendor database has been disabled.</td>
<td>A user has executed the Enable/Disable Vendor Database Link [PSS ENABLE/DISABLE DB LINK] option and disabled the interface.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>Vendor database updates are being processed</td>
<td>The vendor database (custom and standard data) is being updated using the DATUP (Data Update) process.</td>
</tr>
<tr class="even">
<td>System</td>
<td>“Signature Failed- Order Auto Discontinued”</td>
<td>Hash Mismatch</td>
<td>Original digitally signed CS order placed in CPRS is checked to ensure data fields are not altered from the time the order is signed in CPRS and later selected for processing in backdoor pharmacy.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>“DEA certificate expired. Renew your certificate.”</td>
<td>Validity of the DEA certificate.</td>
<td>Kernel API check for the validity of the DEA certificate. If certificate is revoked or expired, the API will return the appropriate error code.</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>An unexpected error has occurred</td>
<td>There is a system network problem and the vendor database cannot be reached or a software interface issue.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Dosing Order Checks can be performed</td>
<td>Dosing Order Checks are disabled</td>
<td>A user has executed the <em>Enable/Disable Dosing Order Checks</em> [PSS Dosing Order Checks] option.</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Local or Local Outpatient Drug: &lt;DRUG NAME&gt;</td>
<td>Drug not matched to NDF</td>
<td>The local drug being ordered/ or on profile has not been matched to NDF. Matching the drug to a VA Product will eliminate this message.</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td><p>Order Checks could not be done for Remote Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>Remote order indicator</p></td>
<td></td>
<td>If this error message is displayed, it means that the VA product that the local or remote drug being ordered/or on the local or remote profile does not have a GCNSEQNO or in rare cases, the GCNSEQNO assigned to the VA Product does not match up with a GCNSEQNO in the vendor database.</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Orderable Item: &lt;OI NAME&gt;</td>
<td>No active Dispense Drug found</td>
<td>Highly unlikely that this error would be seen. At the time the order check was being performed the orderable item did not have an active dispense drug associated.</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions for common acronyms and terms used in this manual.
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym/Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Action Profile</td>
<td>A list of all active and recently canceled or expired prescriptions for a patient sorted by classification. This profile also includes a signature line for each prescription to allow the physician to cancel or renew it.</td>
</tr>
<tr class="even">
<td>Activity Log</td>
<td>A log, by date, of changes made to or actions taken on a prescription. An entry is made in this log each time the prescription is edited, canceled, reinstated after being canceled, or renewed. An entry will be made into this log each time a label is reprinted. A CMOP activity log will contain information related to CMOP dispensing activities.</td>
</tr>
<tr class="odd">
<td>Allergy/ADR Information</td>
<td>Includes non-verified and verified allergy and/or adverse reaction information as defined in the Adverse Reaction Tracking (ART) package. The allergy data is sorted by type (DRUG, OTHER, FOOD). If no data is found for a category, the heading for that category is not displayed.</td>
</tr>
<tr class="even">
<td>Allergy Order Checks</td>
<td>The process that compares the drugs prescribed for a patient against that patient’s recorded allergies</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="even">
<td>Answer Sheet</td>
<td>An entry in the DUE ANSWER SHEET file. It contains the questions and answers of a DUE questionnaire. This term is also used to refer to the hard copy representation of a DUE ANSWER SHEET entry.</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Programming Interface<strong>s</strong></td>
</tr>
<tr class="even">
<td>APSP</td>
<td>Originally Indian Health Service Pharmacy's name space now owned by the Outpatient Pharmacy software.</td>
</tr>
<tr class="odd">
<td>BSA</td>
<td><p>Body Surface Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:</p>
<p>BSA (m²) = 0.20247 x Height (m)<sup>0.725</sup> x Weight (kg)<sup>0.425</sup></p>
<p>The equation is performed using the most recent patient height and weight values that are entered into the vitals package.</p>
<p>The calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td>Bypass</td>
<td>Take no action on a medication order.</td>
</tr>
<tr class="odd">
<td>CHAMPVA</td>
<td>CHAMPVA (Civilian Health and Medical Program of the Department of Veterans Affairs) is a cost-shared health benefits program established for the dependents and survivors of certain severely disabled and/or deceased Veterans.</td>
</tr>
<tr class="even">
<td>Clinical Reminder Order Checks (CROC)</td>
<td>CPRS Order Checks that use Clinical Reminder functionality, both reminder terms and reminder definitions, to perform checks for groups of orderable items.</td>
</tr>
<tr class="odd">
<td>CMOP</td>
<td>Consolidated Mail Outpatient Pharmacy.</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System. CPRS is an entry point in VistA that allows the user to enter all necessary orders for a patient in different packages (e.g., Outpatient Pharmacy, Inpatient Pharmacy, etc.) from a single entry point.</td>
</tr>
<tr class="odd">
<td>CrCL</td>
<td><p>Creatinine Clearance. The CrCL value which displays in the pharmacy header is identical to the CrCL value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p>Modified Cockcroft-Gault equation using<br />
Adjusted Body Weight in kg (if ht &gt; 60in)</p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td>Critical</td>
<td>Interactions with severe consequences that require some type of action (finding facts, contacting prescribers) to prevent potential serious harm.</td>
</tr>
<tr class="odd">
<td>DATUP</td>
<td>Data Update (DATUP). Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out VA custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the production and pre-production centralized MOCHA databases at Austin and Philadelphia.</td>
</tr>
<tr class="even">
<td>DEA</td>
<td>Drug Enforcement Agency</td>
</tr>
<tr class="odd">
<td>DEA Special Handling</td>
<td>The Drug Enforcement Agency special Handling code used for drugs to designate if they are over-the counter, narcotics, bulk compounds, supply items, etc.</td>
</tr>
<tr class="even">
<td>DHCP</td>
<td>See VistA</td>
</tr>
<tr class="odd">
<td>DIF</td>
<td>Drug Information Framework</td>
</tr>
<tr class="even">
<td>Dispense Drug</td>
<td>The Dispense Drug name has the strength attached to it (e.g., Acetaminophen 325 mg). The name alone without a strength attached is the Orderable Item name.</td>
</tr>
<tr class="odd">
<td>DoD</td>
<td>Department of Defense</td>
</tr>
<tr class="even">
<td>Dosage Ordered</td>
<td>After the user has selected the drug during order entry, the dosage ordered prompt is displayed.</td>
</tr>
<tr class="odd">
<td>Drug/Drug Interaction</td>
<td>The pharmacological or clinical response to the administration of a drug combination different from that anticipated from the known effects of the two agents when given alone.</td>
</tr>
<tr class="even">
<td>DUE</td>
<td>Drug Usage Evaluation</td>
</tr>
<tr class="odd">
<td>Enhanced Order Check</td>
<td>Drug – Drug Interaction, Duplicate Therapy, and Dosing order checks that are executed utilizing FDB’s MedKnowledge Framework APIs and database.</td>
</tr>
<tr class="even">
<td>ETC</td>
<td>Enhanced Therapeutic Classification system</td>
</tr>
<tr class="odd">
<td>Expiration/Stop</td>
<td>The date on which a prescription is no longer active. Typically, this date is 30 days after the issue date for narcotics, 365 days after the issue date for other medications and 365 days after the issue date for supplies.</td>
</tr>
<tr class="even">
<td>FDB</td>
<td>First DataBank</td>
</tr>
<tr class="odd">
<td>Finish</td>
<td>Term used for completing orders from Order Entry/Results Reporting V. 3.0.</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Acronym for Graphical User Interface.</td>
</tr>
<tr class="odd">
<td>Issue Date</td>
<td>The date on which the prescription was written. This date is usually, but not always, the same as the first fill date. This date cannot be later than the first fill date.</td>
</tr>
<tr class="even">
<td><strong>HDR/CDS</strong></td>
<td>Health Data Repository/Clinical Data Services Repository</td>
</tr>
<tr class="odd">
<td>HDR-Hx</td>
<td>Health Data Repository Historical</td>
</tr>
<tr class="even">
<td>HDR-IMS</td>
<td>Health Data Repository- Interim Messaging Solution</td>
</tr>
<tr class="odd">
<td>HFS</td>
<td>Host File Server.</td>
</tr>
<tr class="even">
<td>Health Insurance Portability and Accountability Act of 1996 (HIPAA)</td>
<td>A Federal law that makes a number of changes that have the goal of allowing persons to qualify immediately for comparable health insurance coverage when they change their employment relationships. Title II, Subtitle F, of HIPAA gives HHS the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information. Also known as the Kennedy-Kassebaum Bill, the Kassebaum-Kennedy Bill, K2, or Public Law 104-191.</td>
</tr>
<tr class="odd">
<td>JCAHO</td>
<td>Joint Commission on Accreditation of Healthcare Organizations</td>
</tr>
<tr class="even">
<td>Label/Profile Monitor</td>
<td>A file for each printer which records, in the order in which they were printed, the last 1000 labels or profiles printed on that printer. This allows a rapid reprint of a series of labels or profiles that were damaged by a printer malfunction or other event.</td>
</tr>
<tr class="odd">
<td>Local Possible Dosages</td>
<td>Free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="even">
<td>Medication Instruction File</td>
<td>The MEDICATION INSTRUCTION file is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.</td>
</tr>
<tr class="odd">
<td>Medication Order</td>
<td>A prescription</td>
</tr>
<tr class="even">
<td>Medication Profile</td>
<td>A list of all active or recently canceled or expired prescriptions for a patient sorted either by date, drug, or classification. Unlike the action profile, this profile is for information only and does not provide a signature line for a physician to indicate action to be taken on the prescription.</td>
</tr>
<tr class="odd">
<td>Medication Routes File</td>
<td>The MEDICATION ROUTES file contains medication route names. The user can enter an abbreviation for each route to be used at the local site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="even">
<td>Med Route</td>
<td>The method in which the prescription is to be administered (e.g., oral, injection).</td>
</tr>
<tr class="odd">
<td>NCCC</td>
<td>National Clozapine Coordinating Center.</td>
</tr>
<tr class="even">
<td>Non-Formulary Drugs</td>
<td>The medications, which are defined as commercially available drug products not included in the VA National Formulary.</td>
</tr>
<tr class="odd">
<td>Non-VA Meds</td>
<td>Term that encompasses any Over-the-Counter (OTC) medications, Herbal supplements, Veterans Health Administration (VHA) prescribed medications but purchased by the patient at an outside pharmacy, and medications prescribed by providers outside VHA. All Non-VA Meds must be documented in patients’ medical records.</td>
</tr>
<tr class="even">
<td><strong>OneVA Pharmacy</strong></td>
<td>Prescriptions that originated from another VistA instance other than the site dispensing the prescription.</td>
</tr>
<tr class="odd">
<td>Order</td>
<td>Request for medication.</td>
</tr>
<tr class="even">
<td>Order Check</td>
<td>Order checks (drug-allergy/ADR interactions, drug-drug, duplicate drug, duplicate therapy, and dosing) are performed when a new medication order is placed through either the CPRS or Outpatient Pharmacy applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Outpatient Pharmacy. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="odd">
<td>Orderable Item</td>
<td>An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="even">
<td>Partial Prescription</td>
<td>A prescription that has been filled for a quantity smaller than requested. A possible reason for a partial fill is that a patient is to return to the clinic in ten days but the prescription calls for a thirty-day supply. Partials do count as workload but do not count against the total number of refills for a prescription.</td>
</tr>
<tr class="odd">
<td>Payer</td>
<td>In health care, an entity that assumes the risk of paying for medical treatments. This can be an uninsured patient, a self-insured employer, or a health care plan or Health Maintenance Organization (HMO).</td>
</tr>
<tr class="even">
<td>Pending Order</td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished the order, it will become active.</td>
</tr>
<tr class="odd">
<td>Pharmacy Narrative</td>
<td>OUTPATIENT NARRATIVE field that may be used by pharmacy staff to display information specific to the patient.</td>
</tr>
<tr class="even">
<td>Polypharmacy</td>
<td>The administration of many drugs together.</td>
</tr>
<tr class="odd">
<td>POE</td>
<td>Pharmacy Ordering Enhancements (POE) project.<br />
Patch PSO*7*46 contains all the related changes for Outpatient Pharmacy.</td>
</tr>
<tr class="even">
<td>Possible Dosages</td>
<td>Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the DRUG file. The DRUG file entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="odd">
<td>Prescription</td>
<td>This term is now referred to throughout the software as medication orders.</td>
</tr>
<tr class="even">
<td>Prescription Status</td>
<td><p>A prescription can have one of the following statuses.</p>
<p><strong>Active -</strong> A prescription with this status can be filled or refilled.</p>
<p><strong>Canceled -</strong> This term is now referred to throughout the software as Discontinued. (See Discontinued.)</p>
<p><strong>Discontinued -</strong> This status is used when a prescription was made inactive either by a new prescription or by the request of a physician.</p>
<p><strong>Discontinued (Edit) -</strong> Discontinued (Edit) is the status used when a medication order has been edited and causes a new order to be created due to the editing of certain data elements.</p>
<p><strong>Deleted -</strong> This status is used when a prescription is deleted. Prescriptions are no longer physically deleted from the system, but marked as deleted. Once a prescription is marked deleted no access is allowed other than view.</p>
<p><strong>Expired -</strong> This status indicates the expiration date has passed.</p>
<p>*Note: A prescription that was canceled or has expired more recently than the date specified by the cutoff date, typically 120 days in the past, can still be acted upon.</p>
<p><strong>Hold -</strong> A prescription that was placed on hold due to reasons determined by the pharmacist.</p>
<p><strong>Non-verified -</strong> There are two types of non-verified statuses. Depending on a site parameter, prescriptions entered by a technician do not become active until a pharmacist reviews them. Until such review, they remain non-verified and cannot be printed, canceled or edited except through the <em>Verification</em> menu.<br />
The second non-verified status is given to prescriptions when a drug/drug interaction is encountered during the new order entry or editing of a prescription.</p>
<p><strong>Pending -</strong> A prescription that has been entered through OERR.</p>
<p><strong>Refill -</strong> A second or subsequent filling authorized by the provider.</p>
<p><strong>Suspended -</strong> A prescription that will be filled at some future date.</p></td>
</tr>
<tr class="odd">
<td>Progress Notes</td>
<td>A component of Text Integration Utilities (TIU) that can function as part of CPRS.</td>
</tr>
<tr class="even">
<td>Provider</td>
<td>The person who authorized an order. Only users identified as providers who are authorized to write medication orders may be selected.</td>
</tr>
<tr class="odd">
<td>Reprinted Label</td>
<td>Unlike a partial prescription, a reprint does not count as workload.</td>
</tr>
<tr class="even">
<td>Questionnaire</td>
<td>An entry in the DUE QUESTIONNAIRE file. This file entry contains the set of questions related to a DUE as well as the drugs being evaluated.</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>The frequency by which the doses are to be administered, such as Q8H, BID, NOW, etc.</td>
</tr>
<tr class="even">
<td>Sig</td>
<td>The instructions printed on the label.</td>
</tr>
<tr class="odd">
<td>Significant</td>
<td>The potential for harm is either rare or generally known so that it is reasonable to expect that all prescribers have taken this information into account.</td>
</tr>
<tr class="even">
<td>Speed Actions</td>
<td>See Actions</td>
</tr>
<tr class="odd">
<td>Suspense</td>
<td>A prescription may not be able to be filled on the day it was requested. When the prescription is entered, a label is not printed. Rather, the prescription is put in the RX SUSPENSE file to be printed at a later date.</td>
</tr>
<tr class="even">
<td><strong>Third (3<sup>rd</sup>) Party Claims</strong></td>
<td>Health care insurance claims submitted to an entity for reimbursement of health care bills.</td>
</tr>
<tr class="odd">
<td>Time In</td>
<td>This is the time that the patient's name was entered in the computer.</td>
</tr>
<tr class="even">
<td>Time Out</td>
<td>This is the time that the patient's name was entered on the bingo board monitor.</td>
</tr>
<tr class="odd">
<td>TRICARE</td>
<td><p>TRICARE is the uniformed service health care program for:</p>
<ul>
<li><p>active duty service members and their families</p></li>
<li><p>retired service members and their families</p></li>
<li><p>members of the National Guard and Reserves and their families</p></li>
<li><p>survivors, and</p></li>
<li><p>others who are eligible</p></li>
</ul>
<p>There are differences in how prescriptions for TRICARE beneficiaries are processed versus how prescriptions are processed for Veterans.</p></td>
</tr>
<tr class="even">
<td>TIU</td>
<td>Text Integration Utilities; a package for document handling, that includes Consults, Discharge summary, and Progress Notes, and will later add other document types such as surgical pathology reports. TIU components can be accessed for individual patients through the CPRS, or for multiple patients through the TIU interface.</td>
</tr>
<tr class="odd">
<td>Titration</td>
<td>Titration is the process of gradually adjusting the dose of a medication until optimal results are reached.</td>
</tr>
<tr class="even">
<td>Units per Dose</td>
<td>The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted for medications that can be split.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).</td>
</tr>
<tr class="even">
<td>Wait Time</td>
<td>This is the amount of time it took to fill the prescription. It is the difference between Time In and Time Out. For orders with more than one prescription, the wait time is the same for each.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Allergy/ADR Order Check Display, 84
B
Batch Print Questionnaires, 26
Bingo Board User, 18
C
Check Drug Interaction, 24
Clinical Alerts, 6
Clinical Reminder Order Checks, 56
Clinical Reminders, 56
CPRS Order Checks, 106
CPRS Order Checks: How They Work, 161
D
DEA Certification, 162
Display Patient's Name on Monitor, 19
Dosing Order Checks, 106
DUE User, 26
Duplicate Drug Order Check, 61
E
Edit an Existing Answer Sheet, 26
Enhanced Drug-Drug Interactions, 57
Enter a New Answer Sheet, 26
Enter New Patient, 18
Entering a New Order, 77
Entering Actions, 8
Error Information, 165
Error Messages, 165
H
Hash Counts, 162
I
Introduction, 1
L
List Manager, 3
M
Medication Profile, 29
N
NDC Validation, 131
Non-VA Meds Usage Report, 9
O
OneVA Pharmacy and the Medication Profile, 31
OneVA Pharmacy Processing within Patient Prescription Processing, 44
Order Check Data Caching, 161
Other Outpatient Pharmacy ListMan Actions, 12
Other Screen Actions, 12
Outpatient Pharmacy Hidden Actions, 9
P
Patient Demographics, 6
Patient Lookup, 15
Patient Prescription Processing, 36
Processing a Prescription, 36
Pull Early from Suspense, 146, 148
Q
Queue CMOP Prescription, 148
R
Reject Resolution Required reject, 121
Release Medication, 150
Reminders, 56
Remove Patient's Name from Monitor, 19
S
Speed Actions, 11
Status of Patient's Order, 19
T
Therapeutic Duplication, 87
Titration, 76
Two Levels of Error Messages, 165
U
Update Patient Record, 159
Using List Manager with Outpatient Pharmacy, 7
Using the Bingo Board, 18
