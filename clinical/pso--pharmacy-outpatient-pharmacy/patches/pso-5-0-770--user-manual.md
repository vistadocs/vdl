---
title: Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) User Guide Version 5.0 (Unit 7 Part 2) Updated PSO*7.0*770
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: (Unit 7 Part 2) Updated PSO*7.0*770
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 5.0
patch_id: PSO*5.0*770
group_key: "PSO:PSO:5.0"
file_numbers: []
security_keys: []
menu_options: 1
description: - Inbound eR<sub>X</sub> VistA Holding Queue Edits and Accept Validation options - Inbound eR<sub>X</sub> VistA Outpatient Profile - Complete Orders from Order Entry/Results Reporting (OERR) and Patient Prescription Processing
audience: 
keywords: 
  - strong
  - provider
  - patient
  - table
  - colgroup
  - tbody
  - thead
  - drug
  - vista
  - validation
page_count: 0
word_count: 30585
section_count: 14
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PSO_7_0_P770_UM_72.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PSO_7_0_P770_UM_72.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 5.0

  User Guide
---

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/001.png)

July 2025

Version 5.0 (Unit 7 Part 2)

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
<td>06/04/2025</td>
<td>5.0</td>
<td><p>PSO*7*770</p>
<ul>
<li><p><a href="#erx-pending-order-suggested-fill-date-auto-calculation-1">eRx Pending Order Suggested Fill Date Auto Calculation</a></p></li>
<li><p><a href="#Patient_Address_Difference">Patient address will ignore differences between similar words</a></p></li>
<li><p><a href="#Provider_Auto_Validation_for_CS_Drugs">Provider Auto-Validation for CS Drugs</a></p></li>
<li><p><a href="#patient-auto-match-in-the-processing-hub">Patient</a>, <a href="#provider-auto-match">Provider</a> and <a href="#vista-drugsig-drug-auto-match-from-a-suggestion">Drug/SIG</a> auto-matching based on suggestions</p></li>
<li><p><a href="#View_RX">New value for ACTION on SUGGESTION prompt: (V) VIEW RX</a></p></li>
<li><p><a href="#copy-patient-instructions-prompt">Patient Instructions Prompt</a></p></li>
<li><p><a href="#future-fill-hold-hff">HFF for Un-Accept and Un-Remove will now ask for Future Fill Date</a></p></li>
<li><p><a href="#jump-to-erx-patient-from-backdoor">Jump to eRx (JE) action modification at the Patient level</a></p></li>
<li><p><a href="#Park_Functionality">Park Functionality in the eRx Holding Queue</a></p></li>
<li><p><a href="#Provider_Inactive">No auto-match if Provider is inactive</a></p></li>
<li><p><a href="#Indication">Indication functionality added to eRx Holding Queue</a></p></li>
</ul>
<h4 id="erx-pending-order-suggested-fill-date-auto-calculation"><a href="#erx-pending-order-suggested-fill-date-auto-calculation-1">eRx Pending Order Suggested Fill Date Auto Calculation</a></h4></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>07/01/2024</td>
<td>5.0</td>
<td><p>PSO*7*746</p>
<ul>
<li><p>Added new hidden action:</p></li>
</ul>
<ul>
<li><p>View Suggestions for <a href="#view-suggestions-vs-hidden-action">Patient</a>, <a href="#view-suggestions-vs-hidden-action-1">Provider</a> and <a href="#view-suggestions-vs-hidden-action-2">Drug</a></p></li>
<li><p><a href="#jump-to-erx-patient-from-backdoor">Jump to eRx Patient from Backdoor</a></p></li>
</ul>
<ul>
<li><p><a href="#erx-pending-order">Pending Order Suggested Fill Date auto calculation</a></p></li>
<li><p><a href="#vista-dispense-drug-auto-match">Updated the Drug Auto-Match to Remove the Vista Drug Selection Restriction</a></p></li>
<li><p><a href="#provider-auto-validation">Updated Provider Auto-Validation</a></p></li>
<li><p><a href="#provider-manual-validation-screen-overview">Clinic name in the Validate Provider Screen</a></p></li>
<li><p><a href="#future-fill-hold-hff">Hold for Future Fill Functionality</a></p></li>
<li><p><a href="#erx-pending-order-1">eRx Meds on File notification</a></p></li>
<li><p><a href="#printing-in-the-erx-holding-queue">Updated the Print action to include the Prescriber Drug Use Evaluation (DUE) Information</a></p></li>
<li><p><a href="#_Batch_Removing_eRX">Batch eRx Remove</a> and <a href="#batch-un-removing-erx-in-the-erx-holding-queue">Un-Remove</a> Functionality</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>05/20/2024</td>
<td>5.1</td>
<td><p>PSO*7*743</p>
<ul>
<li><p><a href="#provider-auto-match">Provider Auto-Match</a></p></li>
<li><p>Updated notes: <a href="#NOTE1_p25"><strong><u>Error! Bookmark not defined.</u></strong></a>, <a href="#NOTE_p27"><strong><u>Error! Bookmark not defined.</u></strong></a>, <a href="#NOTE_p29"><strong><u>Error! Bookmark not defined.</u></strong></a>, <a href="#NOTE_p47"><strong><u>Error! Bookmark not defined.</u></strong></a>, <a href="#NOTE_p50"><strong><u>Error! Bookmark not defined.</u></strong></a></p></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>11/30/2023</td>
<td>5.0</td>
<td><p>PSO*7*700:</p>
<ul>
<li><p>New menu option: <em>eRx Holding Queue Processing</em> [PSO ERX QUEUE PROCESSING]</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
</tbody>
</table>

This table displays the revision history providing the date, version number and description details.

Table of Contents

# – Part 2: Matching, Validations and Acceptance of an eRx and Pending Order Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [– Part 2: Matching, Validations and Acceptance of an eRx and Pending Order Overview](#part-2-matching-validations-and-acceptance-of-an-erx-and-pending-order-overview)
  - [Introduction](#introduction)
  - [Purpose of eR<sub>X</sub> Matching](#purpose-of-ersubxsub-matching)
  - [Reverse Vs. Highlight Video](#reverse-vs-highlight-video)
  - [Manual Validation](#manual-validation)
    - [Validate Patient](#validate-patient)
    - [Validate Provider](#validate-provider)
    - [Validate Drug/SIG](#validate-drugsig)
  - [Accepting eR<sub>X</sub>](#accepting-ersubxsub)
  - [Rejecting eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#rejecting-ersubxsub-in-the-ersubxsub-holding-queue)
  - [Do Not Fill](#do-not-fill)
  - [Printing in the eR<sub>X</sub> Holding Queue](#printing-in-the-ersubxsub-holding-queue)
  - [Placing eR<sub>X</sub> on Hold in the eR<sub>X</sub> Holding Queue](#placing-ersubxsub-on-hold-in-the-ersubxsub-holding-queue)
    - [Future Fill Hold (HFF)](#future-fill-hold-hff)
  - [Un Hold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#un-hold-ersubxsub-in-the-ersubxsub-holding-queue)
  - [Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#removing-ersubxsub-in-the-ersubxsub-holding-queue)
    - [Batch Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#batch-removing-ersubxsub-in-the-ersubxsub-holding-queue)
  - [Un Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#un-removing-ersubxsub-in-the-ersubxsub-holding-queue)
    - [Batch Un Removing eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue](#batch-un-removing-ersubxsub-in-the-ersubxsub-holding-queue)
  - [eR<sub>X</sub> in the Backdoor Pharmacy Pending Queue](#ersubxsub-in-the-backdoor-pharmacy-pending-queue)
    - [Patient Medication Profile](#patient-medication-profile)
    - [eRx Pending Order](#erx-pending-order)
    - [Renewal eRx Pending Order](#renewal-erx-pending-order)
    - [eRx Pending Order](#erx-pending-order-1)
    - [Jump to eRx Patient from Backdoor](#jump-to-erx-patient-from-backdoor)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound eR<sub>X</sub> VistA Outpatient Pharmacy is comprised of two sections:

- Inbound eR<sub>X</sub> VistA Holding Queue Edits and Accept Validation options
- Inbound eR<sub>X</sub> VistA Outpatient Profile - Complete Orders from Order Entry/Results Reporting (OERR) and Patient Prescription Processing

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

2.  Memorize the VistA patient when eRx is selected (\<SPACE BAR\>)

> When the user selects an eRx that has a VistA Patient matched to it, the VistA patient will now be memorized as the last patient accessed by the user, therefore when the user type \<SPACE BAR\> at a VistA PATIENT prompt, it will automatically select the VistA Patient matched to the eRx.

| VISTA PATIENT: Xxxx,Xxxxxxxxxxx |
|-------------------------------------|

3.  Lowercase and Uppercase discrepancies are ignored:

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

4.  Special characters, including blank spaces are ignored:

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

5.  Dates formatted differently are ignored:

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

6.  Only the first 5 digits of a Zip Code is compared:

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

7.  <span id="Patient_Address_Difference" class="anchor"></span>Patient address will ignore differences between similar words. The comparison of patient addresses between eRx and VistA will disregard variations in similar words mentioned below, omitting reverse video if these are the sole differences in the addresses. Below are a few examples:

> DR = DRIVE APT = APARTMENT STE = SUITE

> AVE = AVENUE W = WEST S = SOUTH

> ST = STREET NW = NORTHWEST SW = SOUTHWEST

> HGWY = HIGHWAY NE = NORTHEAST SE = SOUTHEAST

> BLVD = BOULEVARD CT = COURT RD = ROAD

> TER = TERRACE PKY = PARKWAY

8.  If either a non-numeric text on the left or on the right contains the other side text, it is ignored as well (exception: MALE & FEMALE):

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

9.  In the case of phone numbers, if the same number is found on different fields (e.g., Cell Phone for one record and Home Number for another) it is ignored as well:

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

10. Allergy information comparison is performed the following way:

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

11. Fields without a corresponding value on the other side will not reverse video:

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

12. Substitution field exception. Although there is no equivalent VistA value for this field, it will always reverse video if the value is NO to alert users that no substitution is allowed:

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

13. SIG field exception. Since the VistA SIG is automatically composed by the dosage fields along with the VistA patient instructions, it becomes extremely hard to match it letter-by-letter with the SIG sent in by the outside prescriber; therefore, the SIG field value will never reverse video:

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

14. DEA EXP field exception. This DEA Expiration Date for the VistA Provider will display in reverse video when it is expired:

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

## Manual Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to accepting a fillable eR<sub>X</sub> \<AC\> and moving the eR<sub>X</sub> to Pending Outpatient Orders file, the VistA patient, provider, and drug/SIG must be validated. The eR<sub>X</sub> is then further processed using Complete Orders from OERR \[PSO LMOE FINISH\] or Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\].

The validation process begins by selecting one of the validate actions from the Single eRx View/Display screen. For training, the sections further will show examples of NewRx processing. The remaining inbound fillable prescriptions follow the same workflow.

> **NOTE:** Before the Drug/SIG on an eR<sub>X</sub> can be manually validated, the eR<sub>X</sub> Patient must have a linked VistA patient. The \<VD\> (Validate Drug/SIG) action has parentheses around the action to signify this action is not available until a VistA patient is linked, as illustrated in the figure below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> May 16, 2025@10:37:33 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>6791230457</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/10/25</strong></p>
<p>eRx Status: <strong>PR - PROCESSED</strong></p>
<p><u>ERX | VISTA</u></p>
<p><u>PATIENT AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21</u></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXX</strong></p>
<p>DOB : <strong>XXX 01, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>XXX 1,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: 555-555-55555 |Phone: 555-555-5555</p>
<p><strong>STREET ADDRESS LNE1 STREET ARL...76017</strong>| <strong>STREET ADDRESS LNE1 STREET ARL...76017</strong></p>
<p><u>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21:52</u></p>
<p>Name: <strong>YYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYY,YYYYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> Phone: |NPI : <strong>9999999999</strong> Phone: <strong>(222) 222-2222</strong></p>
<p>DEA : <strong>XX99999999</strong> |DEA :</p>
<p>Clinic: <strong>EXTERNAL PHARMACY</strong> |Class: <strong>PHYSICIAN</strong></p>
<p><u>DRUG/SIG SUGGESTED | VALIDATED by USER,USER on 3/13/25@17:29:10</u></p>
<p>Drug: LEVOTHYROXINE NA (SYNTHROID) 50MC|<u>1)</u>Drug: LEVOTHYROXINE NA (SYNTHROID) 300</p>
<p>G TAB | MCG TAB</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; VA STND DRUG</strong></p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET MOUTH EVERY DAY</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>| <strong>BEFORE MEAL FOR THYROID HORMONE</strong></p>
<p>| <strong>REPLACEMENT - TAKE AT LEAST AN HOUR</strong></p>
<p>| <strong>BEFORE FOOD OR OTHER MEDICATIONS</strong></p>
<p>Prescriber Drug Use Evaluation: |<u>2)</u> Dosage: <strong>50 (MCG)</strong></p>
<p><strong>None</strong> | Verb: <strong>TAKE</strong></p>
<p>|Disp. Units: <strong>1</strong></p>
<p>| Noun: <strong>TABLET</strong></p>
<p>| Route: <strong>ORAL (BY MOUTH)</strong></p>
<p>| Schedule: <strong>ONCE DAILY-AC</strong></p>
<p>|</p>
<p>|<u>3)</u>Patient Instructions:</p>
<p>| <strong>FOR THYROID HORMONE REPLACEMENT - TAKE</strong></p>
<p>| <strong>AT LEAST AN HOUR BEFORE FOOD OR OTHER</strong></p>
<p>| <strong>MEDICATIONS</strong></p>
<p>Provider Notes/Comments: |<u>4)</u>Provider Comments:</p>
<p><strong>DISREGARD, IT TESTING.</strong> | <strong>DISREGARD, IT TESTING.</strong></p>
<p>|<u>5)</u>Pat. Status: <strong>SERVICE CONNECTED</strong></p>
<p>|</p>
<p>Quantity: <strong>30</strong> |<u>6)</u>Quantity: <strong>30</strong></p>
<p>Dispense Unit: | Dispense Unit: <strong>TAB</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>3</strong> |<u>7)</u>Days Supply: <strong>30</strong> <u>8)</u>Refills: <strong>3</strong></p>
<p>|<u>9)</u>Routing: <strong>MAIL</strong></p>
<p>|<u>10)</u>Clinic: <strong>CHY TEST 2 PRE-VISIT</strong></p>
<p>Written: <strong>03/10/25</strong> Effective: |</p>
<p>Primary Dx: |<u>11)</u>Indications:</p>
<p><strong><u>ICD-10 A01.01 TYPHOID MENINGITIS</u></strong> | <strong>INDICATION TESTING</strong></p>
<p><strong>TESTING PRIMARY DIAGNOSIS</strong> |</p>
<p>Secondary Dx: |</p>
<p><strong><u>ICD-10 E11.21 TYPE 2 DIABETES MELLITUS</u></strong>|</p>
<p><strong><u>WITH DIABETIC NEPHROPATHY</u></strong> |</p>
<p><strong>TESTING SECONDARY DIAGNOSIS</strong> |</p>
<p>Primary Dx: |</p>
<p><strong><u>ICD-10 I10 TYPHOID MENINGITIS</u></strong> |</p>
<p><strong>TESTING ANOTHER PRIMARY DIAGNOSIS</strong> |</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
<p>| LIMA BEANS</p>
<p>|Adverse Reactions:</p>
<p>| <u>Verified:</u></p>
<p>| ABROCITINIB</p>
<p>_______________________________________|_____________________________________</p>
<p><strong>eRx Received on 12/12/23@15:47 - Accepted by USER,USER on 6/05/24@11:12</strong></p>
<p>+ Enter ?? for more actions</p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Single eRx View/Display

### Validate Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient must be matched and validated before a fillable eR<sub>X</sub> can be accepted. Information about the Patient Validation screen and editing the patient information is described in the following sections.

To match and validate patient information, type \<VP\> VALDIATE PATIENT from the Single eRx View/Display screen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen// VP VALIDATE PATIENT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Validate Patient

#### Patient Auto-Match in the Processing Hub

The following outlines the scenarios for a patient auto-match in the Inbound ePrescribing (IEP) Processing Hub before being sent down to VistA:

Patient Match - Primary Hub

1.  Master Veteran Index (MVI) Check - receive Integrated Control Number (ICN) and Social Security Number (SSN) from MVI if successful:
1.  If SSN is sent on a NewRx, then the SSN is used in the auto-match with the MVI along with Last Name, First Name, Date of Birth (DOB), Gender, Address Line 1, and Home Telephone Number. If Home Telephone Number is not sent, Primary Telephone is used.
2.  If SSN is not sent on the NewRx, then the match is done with MVI against Last Name, First Name, DOB, Gender, Address Line 1, and Home Telephone Number. If Home Telephone Number is not sent, Primary Telephone is used.
3.  Since only the Last Name, First Name, DOB, and Gender are mandatory on a fillable prescription, the match is done against all the data pieces that are received.
4.  When a patient is successfully matched, the patient registration at the sites is checked.
2.  Eligibility and Enrollment (E&E) Check - Then E&E Services is checked to see if the patient is both enrolled and eligible to their system to receive pharmacy benefits (This is done using ICN retrieved from MVI).

Patient Secondary Match in VistA

- Case 1: Patient Auto match successful (MVI record found, E&E check passed, and Patient Site Registration passed).
1.  Use the ICN received from MVI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
2.  If ICN check fails, use the SSN received from MVI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
- Case 2: MVI Match successful, but E&E check failed at the Hub:
1.  Use the ICN received from MVI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
2.  If ICN check fails, use the SSN received from MVI and check against the local Patient file entry; if passed, then link this VistA patient to eR<sub>X</sub> Patient.
- Case 3: MVI match unsuccessful at the Hub:
1.  No secondary match.

> **NOTE:** When the patient is not auto-matched at the hub and there is a VistA patient suggestions on file, the suggestion will be used to auto-match.

| MbM Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Upon arrival from the eRx Hub the eRx will be checked whether the VistA Patient was auto-matched or not. If it was successfully matched, the software will then check if the patient is eligible for ChampVA Rx benefit, if not, the software will automatically hold the eRx with an HEL (PATIENT ELIGIBILITY ISSUE). If eligible, the software will then check if the patient has an Allergy Assessment on file, if not, the software will automatically hold the eRx with an HAL (NO PATIENT ALLERGY ASSESSMENT). |     |

#### Patient Manual Matching Screen Overview

The header of the Patient Validation screen contains the eR<sub>X</sub> Reference \# and the Status. Below the header is the eR<sub>X</sub> and VistA information for the patient, including any known allergies where applicable.

If the patient was not auto-matched at the eR<sub>X</sub> Hub, the screen looks similar to the below figure. The Status field has “NOT MATCHED” in the header. No VistA patient information displays.

> **NOTE:** The Status will not contain validation details until the user Accepts Validation (AV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> May 16, 2025@11:25:30 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>99999999</strong></p>
<p>Status: <strong>NOT MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>SSN : <strong>999999999</strong> |SSN :</p>
<p>Sex : <strong>MALE</strong> |Sex :</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> |</p>
<p><strong>XXXXXXXX,XX 99999</strong> |</p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Edit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Screen Display - Patient Not Auto Matched/Not Validated

If the patient was auto-matched at the eR<sub>X</sub> Hub the Status in the header will show “AUTO-MATCHED” and the header will look similar to the below figure. In this case, the information for the VistA Patient will display on the right side. The reverse video on a field value indicates a discrepancy between the two records.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> May 16, 2025@11:47:12 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong><mark>1234 ERX TEST ROAD</mark></strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: (<strong>999) 999-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> | <strong>NO ALLERGY ASSESSMENT</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Height(cm): |Height(cm):</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Screen Display – Patient Auto-Matched/Not Validated

Once the Patient has been validated by using the Accept Validation (AV) action, the Status in the header will show “AUTO-MATCHED \| VALIDATED by ” with the user who performed the validation and date/time stamp.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> May 16, 2025@11:59:40 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED | VALIDATED by USER,USER on 9/21/23@11:59:38</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : MALE</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong><mark>1234 ERX TEST ROAD</mark></strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: (<strong>999) 999-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> | <strong>NO ALLERGY ASSESSMENT</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Height(cm): |Height(cm):</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Screen Display – Patient Auto-Matched/Validated

If the patient was not auto-matched at the eR<sub>X</sub> Hub, the user can choose the Edit (E) action to select a Vista Patient to manually match. If the eR<sub>X</sub> Patient has never been matched to a VistA Patient, the screen looks similar to the below figure. After the eR<sub>X</sub> is matched to a VistA patient, the Status in the header shows “MANUALLY-MATCHED”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> May 16, 2025@12:33:23 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>99999999</strong></p>
<p>Status: <strong>NOT MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>SSN : <strong>999999999</strong> |SSN :</p>
<p>Sex : <strong>MALE</strong> |Sex :</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> |</p>
<p><strong>XXXXXXXX,XX 99999</strong> |</p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone:</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Height(cm): |Height(cm):</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Edit// E Edit</p>
<p>VISTA PATIENT: <strong>XXXXX,XXXXXXXXXX</strong> 99/99/9999 999999999 XXXXXXXXXX,XX</p>
<p>Enrollment Priority: Category: NOT ENROLLED End Date:</p>
<p>ERX PATIENT VISTA PATIENT</p>
<p>________________________________________________________________________________</p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>________________________________________|_______________________________________</p>
<p>Would you like to use this patient? NO// YES</p>
<p><u><strong>Patient Validation</strong> Sep 21, 2023@12:37:52 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999999</strong> Eligibility: <strong>NON-SERVICE CONNECTED</strong></p>
<p>Status: <strong>MANUALLY-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: (<strong>999) 999-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong><mark>NO ALLERGY INFORMATION RECEIVED</mark></strong> | <strong>NO KNOWN ALLERGIES</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Height(cm): |Height(cm):</p>
<p>_______________________________________|_______________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Screen Display – Patient Manually-Matched/Not ValidatedPatient Auto-suggestion

When the user chooses the Edit (E) action to select a Vista Patient, if the eR<sub>X</sub> Patient has been previously matched to a VistA Patient, the user will be prompted for the VistA entry, and they will be presented with a suggestion based on the following logic below.

- Once a VistA Patient is matched and later validated to an eR<sub>X</sub> Patient it is then “remembered”.
- When a new eR<sub>X</sub> prescription is received for the same eR<sub>X</sub> Patient the “remembered” VistA Patient(s) are then presented as suggestions for the user to select.
- When there is only one suggestion the user is given 3 options: (A)ccept, (F)orget or (E)xit the suggested VistA record.
  - (A)ccept effectively matches the suggest VistA Patient with the eR<sub>X</sub>
  - (F)orget removes the VistA Patient as a valid suggestion for the eR<sub>X</sub> Patient so it is no longer presented in the future for any user
  - (E)xit Exits and proceed to match the VistA Patient manually
- If more than one suggestion exists, an additional action is presented:
  - (N)ext ignores the suggestion and moves on the next suggestion

Below is an example of auto-suggestion and prompting for the VistA patient. The suggestions will be numbered (i.e. 1 of 1) and it will also display the eR<sub>X</sub> \# from the previously matched eR<sub>X</sub>.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 18, 2023@11:42:32 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>99999999</strong></p>
<p>Status: <strong>NOT MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name:</p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB :</p>
<p>SSN : <strong>999999999</strong> |SSN :</p>
<p>Sex : <strong>MALE</strong> |Sex :</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> |</p>
<p><strong>XXXXXXXX,XX 99999</strong> |</p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: (<strong>999) 999-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><strong>NO ALLERGY INFORMATION RECEIVED</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>Height(cm): |Height(cm):</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Edit// E Edit</p>
<p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>10/04/23</strong>|</p>
<p>ERX PATIENT VISTA PATIENT |From eRx#: <strong>123444</strong> |</p>
<p>________________________________________________________________________________</p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong><mark>1234 ERX TEST ROAD</mark></strong></p>
<p><strong>XXXXXXXXXXX,XX 99999</strong> | <strong>XXXXXXXXXXX,XX 99999</strong></p>
<p>________________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (A)CCEPT (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Screen Display – Auto-Suggestion

The suggestion above is presented to the user because another eR<sub>X</sub> (#123444) was received in the past for the exact same eR<sub>X</sub> Patient and it was matched to the VistA Patient on the right and validated.

> **NOTE:** The software limits the number of distinct suggestions to 3. The order in which the suggestions are presented are from the newest (most recently “remembered”) to the oldest (last “remembered”).

Patient Allergies

If the VistA patient has known allergies, verified allergies are displayed in the Allergies section.

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
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>Primary Phone: <strong>9999999999</strong> |</p>
<p>Home Phone: |Home Phone: (<strong>999) 999-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

VistA Patient with Known Allergies

A hidden action is available on the Patient Validation screen that allows the user to display the Patient Allergies in greater detail. This hidden action can be invoked from the following screens listed below:

- Patient Validation screen
- Drug Validation screen
- eR<sub>X</sub> Holding Queue Display screen
- Pending Orders screen (Backdoor Outpatient Pharmacy)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>PA Patient Allergies DN Down a Line PT Print List</p>
<p>VS View Suggestion(s) FS First Screen SL Search List</p>
<p>+ Next Screen LS Last Screen QU Quit</p>
<p>- Previous Screen GO Go to Page</p>
<p>UP Up a Line PS Print Screen</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When the user selects the Patient Allergies (PA) hidden action from the Patient Validation screen, a new screen displays titled Patient Allergies. The Patient Allergies screen was created to show the eR<sub>X</sub> patient allergies side-by-side with the VistA patient allergies in detail.

The Patient Allergies screen also contains a new action called VistA Patient Allergies (VPA). The VPA action invokes a new screen titled Detailed Allergy List and this screen allows the user to edit allergy data.

> **NOTE:** A VistA Patient must be matched to use the VistA Patient Allergies (VPA) action.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Allergies</strong> Oct 18, 2023@14:18:39 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | <u>Verified:</u></p>
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

The actions at the bottom of the Patient Validation screen include:

- \<P\> Print – Prints display of the eR<sub>X</sub> for printing to network or local printer.
- \<H\> Hold – Places an eR<sub>X</sub> on hold.
- \<E\> Edit – User edits if the information is empty or incorrect.
- \<AV\> Accept Validation – User accepts the validation if information is correct.
- \<RJ\> Reject – Rejects the eR<sub>X.</sub>

#### Edit Patient

1.  Enter \<E\> Edit to edit the patient information.
2.  If a VistA patient already exists for the eR<sub>X</sub>, the system displays a message confirming the edit.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Quit// E Edit</p>
<p>Current Vista patient: MBMONE,TESTONE TEST</p>
<p>This Patient has already been validated.</p>
<p>Would you like to edit the patient? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Edit Patient on a VistA Match

> ‘This Patient has already been validated.’ – This verbiage only displays if the user attempts to edit a patient who has been previously validated.

3.  If a VistA patient match does not exist, the system the software will look for any existing suggestion and will auto-match to the latest VistA suggestion on file. The user can then Accept, Forget, or Exit the patient’s name suggestion screen.

> If the user selects the Exit option, the system will prompt to enter/select patient at the “VISTA PATIENT:” prompt. The partial or full name of the patient, DOB or SSN can be entered.

> If the Date of Birth (DOB) of the eRx Patient does not match the DOB of the VistA Patient, the warning below will be displayed:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* WARNING(S) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patient DOB mismatch (eRx: 02/02/1975 \| VistA: 12/23/1984)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4.  Select the correct patient and press \<Enter\>.
5.  A message displays confirming the patient selection. Enter \<Y\> Yes.
6.  The select patient information populates the VistA Patient fields on the Patient Validation screen.

CS NOTE: For Controlled Substance eR<sub>X</sub> records, an additional check is performed for the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL for patients residing abroad. If not found, the message below will be displayed.

#### Selected Patient Warnings

The following checks will be performing, and the warnings below will display when the patient is selected, if applicable:

- VistA Patient does not have an Allergy Assessment.

VistA Patient does not have a current mailing or residential address on file. (Digitally Signed eR<sub>X</sub> only)

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
<td colspan="2"><p><strong><u>Additional Warnings</u></strong></p>
<p>For MbM, two additional warnings will be performed:</p>
<ul>
<li><p>VistA Patient is not eligible for ChampVA Rx Benefit.</p></li>
<li><p>The following VistA Patient(s) has been identified as potential duplicate(s):</p></li>
</ul>
<blockquote>
<p>XXXXXXXX,XXXXXX XXX 99,9999 999-99-9999 XXXXXXXXXXX,XX</p>
</blockquote>
<p><strong><u>Duplicate Patient</u></strong></p>
<p>The criterion for a duplicate patient is determined the following way:</p>
<p>Full Name matches exactly</p>
<p>OR</p>
<p>Last Name matches exactly + First letter of First Names matches + Dates of Birth matches</p>
<p><strong><u>Eligibility</u></strong></p>
<p>For MbM the ChampVA Eligibility is currently being checked by a Class 3 API ($$CHVAELIG^PSOZRXU0), which can return one of the following values:</p>
<ul>
<li><p>ELIGBILE</p></li>
<li><p>NOT ELIGIBLE</p></li>
<li><p>SB (SPINA BIFIDA)</p></li>
</ul></td>
</tr>
</tbody>
</table>

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
<td colspan="2"><p>When a VistA Patient that is not eligible for ChampVA benefit is matched to an eR<sub>X</sub> the software will first warn the user before the confirming the match:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Edit// E Edit</p>
<p>VISTA PATIENT: <strong>XXXXX,XXXXXXXXXX</strong> 99/99/9999 999999999 XXXXXXXXXX,XX</p>
<p>Enrollment Priority: Category: NOT ENROLLED End Date:</p>
<p>ERX PATIENT VISTA PATIENT</p>
<p>________________________________________________________________________________</p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>________________________________________|_______________________________________</p>
<p> WARNING(S) *</p>
<p>VistA Patient is not eligible for ChampVA Rx Benefit.</p>
<p></p>
<p>Would you like to use this patient? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>If the user confirms the selection above the current eR<sub>X</sub> will automatically be put on Hold with the HEL (ELIGIBILITY ISSUE) hold code. Furthermore, all the other prescriptions for the same eR<sub>X</sub> Patient (if any) will also be put on hold with the same Hold code:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>...</p>
<p>Would you like to use this patient? NO// Y YES</p>
<p>Updating...</p>
<p>This eRx has been put on Hold (HEL) because the VistA Patient (XXXXX,XXXXXXXXXX)</p>
<p>is not Eligible for ChampVA Rx Benefit.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p>The following eRx record(s) have been put on Hold (HEL) because the VistA</p>
<p>Patient (XXXXX,XXXXXXXXXX) is not Eligible for ChampVA Rx Benefit.</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>---------------------------------------------------------------------------</p>
<p>11142 BENAZEPRIL HCL 40MG TAB XXXXXXXX,XXXXX MD HEL</p>
<p>11143 SERTRALINE HCL 50MG TAB XXXXXXXX,XXXXX MD HEL</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
</tr>
</tbody>
</table>

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
<td colspan="2"><p><strong><u>No Allergy Assessment</u></strong></p>
<p>For MbM the fact that a VistA patient does not have an allergy assessment presents a risk; therefore, all the prescriptions matched to this VistA patient are automatically put on Hold right after the VistA patient w/out an allergy assessment is selected.</p></td>
</tr>
</tbody>
</table>

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
<td colspan="2"><p>When a VistA Patient that does not have an allergy assessment on file is matched to an eR<sub>X</sub> the software will first warn the user before the confirming the match:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Edit// E Edit</p>
<p>VISTA PATIENT: <strong>XXXXX,XXXXXXXXXX</strong> 99/99/9999 999999999 XXXXXXXXXX,XX</p>
<p>Enrollment Priority: Category: NOT ENROLLED End Date:</p>
<p>ERX PATIENT VISTA PATIENT</p>
<p>________________________________________________________________________________</p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX X</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> | <strong>1234 ERX TEST WAY</strong></p>
<p><strong>XXXXXXXX,XX 99999</strong> | <strong>XXXXXXXX,XX 99999</strong></p>
<p>________________________________________|_______________________________________</p>
<p> WARNING(S) *</p>
<p>VistA Patient does not have an Allergy Assessment.</p>
<p></p>
<p>Would you like to use this patient? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>If the user confirms the selection above the current eR<sub>X</sub> will automatically be put on Hold with the HAL (NO ALLERGY ASSESSMENT) hold code. Furthermore, all the other prescriptions for the same eRx Patient (if any) will also be put on hold with the same Hold code:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>...</p>
<p>Would you like to use this patient? NO// Y YES</p>
<p>Updating...</p>
<p>This eRx has been put on Hold (HEL) because the VistA Patient (XXXXX,XXXXXXXXXX)</p>
<p>does not have an Allergy Assessment...</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p>The following eRx record(s) have been put on Hold (HAL) because the VistA</p>
<p>Patient (XXXXX,XXXXXXXXXX) does not have an Allergy Assessment.</p>
<p>ERX ID DRUG NAME PROVIDER STS</p>
<p>---------------------------------------------------------------------------</p>
<p>11142 BENAZEPRIL HCL 40MG TAB XXXXXXXX,XXXXX MD HAL</p>
<p>11143 SERTRALINE HCL 50MG TAB XXXXXXXX,XXXXX MD HAL</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### Patient Accept Validation

Once the patient information has been edited and reviewed for accuracy, the validation needs to be accepted on the Patient Validation screen.

1.  Select \<AV\> Accept Validation on the Patient Validation screen to accept the patient validation.

> If the Date of Birth (DOB) of the eRx Patient does not match the DOB of the VistA Patient, the warning below will be displayed:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* INVALID PATIENT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patient DOB mismatch (eRx: 02/02/1975 \| VistA: 12/23/1984)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

2.  A message displays confirming whether to mark the patient as validated. Enter \<Y\> Yes.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// AV Accept Validation</p>
<p>Would you like to mark this patient as VALIDATED?</p>
<p>Enter Yes or No: NO// YES</p>
<p>Patient Match Validated!!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Confirm Acceptance of Patient Validation

If the validation is successful, a message ‘Patient Matched Validated!!’ indicating that the validation was updated.

The Status changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/time stamp.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> May 23, 2025@11:13:58 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>202504090002</strong> ChampVA Rx Benefit: <strong>ELIGIBLE</strong></p>
<p>Status: <strong>AUTO-MATCHED | VALIDATED by USER,USER R on 5/23/25@11:13:58</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In the Single eRx View/Display , after the patient has been validated using the Accept Validation (AV) action, the patient header will be appended with “VALIDATED" along with the user who performed the validation and the date/time stamp.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> May 22, 2025@18:01:07 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2025052200001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>05/22/25</strong></p>
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
<td>PATIENT AUTO-MATCHED | VALIDATED by USER,USER R on 5/22/25@17:52</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 99, 9999</strong> SSN : 999999999 |DOB : <strong>FEB 99,9999</strong> SSN : 999999999</p>
<p>Phone: |Phone: 5551112222</p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Complete: Single eRx View/Display Screen

Additionally, a “V” is displayed to the PT column on the eRx Single Patient Queue screen to indicate that the patient has been validated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Single Patient Queue</strong> May 22, 2025@18:04:50 Page: 1 of 1</u></p>
<p>eRx PATIENT: <strong>MBMONE,TESTONE TEST</strong> SEX: <strong>M</strong> DOB: <strong>02/99/99(50)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>999-99-9999</strong> MATCHING</p>
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
<p>1. 2025052200001 LEVOTHYROXINE NA (SYNT KURIHARA,ESTER 05/22/25 I AV A<strong>V</strong> M</p>
<p>2. 2025052200002 LEVOTHYROXINE NA (SYNT KURIHARA,ESTER 05/22/25 N</p>
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

Patient Validation Complete: eRx Single Patient Queue Screen Indicator

CS NOTE: For Controlled Substance eRx records, the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE for patients residing abroad will be required. If not found, the message below will be displayed, and the user will not be able to proceed with the Validation as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 19, 2023@09:35:15 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>9999999</strong> Eligibility:</p>
<p>Status: <strong>MANUALLY-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p>1234 ERX TEST WAY |</p>
<p>XXXXXXXX,XX 99999 |</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| EGG PRODUCTS,PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p><u>+ Enter ?? for more actions</u></p>
<p>P Print H Hold RJ Reject</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// AV Accept Validation</p>
<p>Unable to validate - VistA Patient does not have a current mailing</p>
<p>or residential address on file.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Unable To Validate Address Warning

#### Batch Patient Validation

When a patient validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub> in the Holding Queue for the same patient, received on the same day, a message displays asking if the patient validation should be applied to the other eR<sub>X</sub>. Error! Reference source not found. If the user selects \<Y\> Yes, the system links and applies the patient validation for the eR<sub>X</sub> currently in the Holding Queue for that patient.

> **NOTE:** Automatic Patient Validation is only available for NewRx.

The determination of the same patient is based on unique records from the ERX EXTERNAL PATIENT file (#52.46). The system only validates the same patients on eR<sub>X</sub> that are currently in the ERX HOLDING QUEUE file (#52.49) received at the time of the automatic patient validation. Patient validation is not applied for eR<sub>X</sub> received for that patient after the auto validation is applied. For example, if VA receives six eR<sub>X</sub> for the same patient on the same day, the user only has to validate the patient once. If eR<sub>X</sub> are received later that same day, those eR<sub>X</sub> need to be revalidated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// AV Accept Validation</p>
<p>Would you like to mark this patient as VALIDATED?</p>
<p>Enter Yes or No: NO// YES</p>
<p>Patient Match Validated!!</p>
<p>This patient has other prescriptions for: Oct 04, 2023</p>
<p>Patient: XXXXXXXXXXXXX,XXXXXXXXXX</p>
<p>DRUG PROVIDER STA REC DATE</p>
<p>-------------------------------------------------------------------------------</p>
<p>1.) OXYCODONE 5MG ACETAMINOPHEN 325MG T XXXXXXXXX,XXXXX XX I 10/04/23</p>
<p>2.) CLINDAMYCIN HCL 150MG CAP XXXXXXXXX,XXXXX XX I 10/04/23</p>
<p>3.) CYANOCOBALAMIN 1000MCG/ML INJ XXXXXXXXX,XXXXX XX I 10/04/23</p>
<p>Would you like to apply the above validation to these prescriptions?</p>
<p>Enter Yes or No: N//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Patient Validation

To apply patient validation to other eR<sub>X</sub> in the Holding Queue for the same patient, received on the same day:

1.  The system asks the user if the previous validation should be applied to the other eR<sub>X</sub> received for the patient.
2.  Enter Y for Yes to apply the validation to the other eR<sub>X</sub> for the patient. After selecting Yes, the patient validation is applied to the other eR<sub>X</sub>. As previously noted, any eR<sub>X</sub> received after this action will not be validated.
3.  A message displays indicating that the patient match was validated.
4.  The Status field changes to “VALIDATED” on the Patient Validation screen, along with the user who performed the validation and date/time stamp. This occurs for all the eR<sub>X</sub> validated via the automatic patient validation process.
5.  In the Single eRx View/Display , after the patient has been validated using the Accept Validation (AV) action, the patient header will be appended with “VALIDATED" along with the user who performed the validation and the date/time stamp.
6.  A “V” is displayed to the PT column on the eRx Single Patient Queue screen to indicate that the patient has been validated.
7.  The statuses on all eR<sub>X</sub> validated by the automatic patient validation process changes to “I” for In Process.

> **NOTE:** When doing a batch validation for a patient, it is possible that one or more of the records for the patient is for Controlled Substance which requires the presence of at least a ZIP CODE for a patient residing in the US or a POSTAL CODE if they reside abroad. So, a check will be performed for such records and if the requirement is not fulfilled, the record will not be validated. The message below will be displayed for each record with this issue:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Patient Validation</strong> Oct 19, 2023@09:35:15 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>9999999</strong> Eligibility:</p>
<p>Status: <strong>MANUALLY-MATCHED</strong></p>
<p><u>ERX PATIENT | VISTA PATIENT</u></p>
<p>Name: <strong>XXXXX,XXXXXXXXXX</strong> |Name: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p>1234 ERX TEST WAY |</p>
<p>XXXXXXXX,XX 99999 |</p>
<p>_______________________________________|________________________________________</p>
<p>|Pharmacy Narrative:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| EGG PRODUCTS,PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Weight(kg): |Weight(kg):</p>
<p><u>+ Enter ?? for more actions</u></p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// AV Accept Validation</p>
<p>Unable to validate - VistA Patient does not have a current mailing</p>
<p>or residential address on file.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Patient Validation Unable To Validate Address Warning

#### View Suggestion(s) (VS hidden action)

This hidden action allows users to view and manage existing VistA Patient suggestions at any time, before or after the eRx has been accepted/processed, including “forgetting” erroneous suggestions. When viewing suggestions, the (A)ccept option is not available because this action is not supposed to be used for matching the patient, only to view and manage suggestions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// VS</p>
<p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>03/07/24</strong>|</p>
<p><mark>ERX PATIENT</mark> <mark>VISTA PATIENT</mark> |From eRx#: <strong>111001</strong> |</p>
<p>_________________________________________________________________________</p>
<p>Name: <strong>TEST,PATIENT A</strong> |Name: <strong>TEST,PATIENT A</strong></p>
<p>DOB : <strong>XXX 99, 9999</strong> |DOB : <strong>XXX 99, 9999</strong></p>
<p>SSN : <strong>999999999</strong> |SSN : <strong>999-99-9999</strong></p>
<p>Sex : <strong>MALE</strong> |Sex : <strong>MALE</strong></p>
<p>Address: |Address:</p>
<p><strong>123 FAKE AVE</strong> | <strong>123 FAKE ST</strong></p>
<p><strong>XXXXXXXXX, XX 999999</strong> | <strong>XXXXXXXXX, XX 999999</strong></p>
<p>Primary Phone: <strong>5184724307</strong> | ________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Validate Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provider must be validated before a fillable eR<sub>X</sub> can be accepted.

To validate provider information, from the Summary/Details screen, type \<VM\> VALIDATE PROVIDER. The eR<sub>X</sub> Provider Validation screen displays.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen// VM VALIDATE PROVIDER</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Summary/Details Screen Action - Validate Provider

Information about the Validate Provider display and editing the provider information is described in the following sections.

#### Provider Auto-Match

The auto-match on an external provider is based upon the NPI of the prescriber coming in on the new eR<sub>X</sub>. The NPI is matched against the VistA instance’s NEW PERSON file (#200) entry. If the NPI matches and if the Provider is marked “Authorized to Write Meds” that is considered a match. Upon a successful match, the VistA provider is linked with the incoming provider’s record in VistA.

#### Provider Auto-Validation

The auto-matched VistA Provider will also be auto-validated if the following conditions are met:

- VistA Provider was auto matched
- Last name of eRx Provider matches exactly to the last name of VistA Provider
- First letter of first name of eR<sub>X</sub> Provider matches with the first letter of the first name of VistA Provider
- The first 5 digits of eR<sub>X</sub> Provider zip code match with the first 5 digits of the VistA Provider zip code.
- <span id="Provider_Auto_Validation_for_CS_Drugs" class="anchor"></span>Provider Auto-Validation for Controlled Substance (CS) Drugs - the VA provider must have a valid DEA# on file that matches the DEA# sent with the eRx.

This implies that users will not need to manually validate the VistA Provider (AV action) to accept the eR<sub>X</sub> (AC action).

#### Provider Manual Validation Screen Overview

The Provider Validation screen show the eR<sub>X</sub> Provider and VistA Provider side-by-side and identify discrepancies in the data with reverse video.

The header of the Provider Validation screen contains the eR<sub>X</sub> Reference \# and the Status. Below the header is the eR<sub>X</sub> and VistA information for the provider, where applicable.

If a match was NOT found for the eR<sub>X</sub> provider, the screen looks similar to the below figure. The Status field has “NOT MATCHED” in the header. No provider information displays.

> **NOTE:** The Status will not contain validation details until the user Accepts Validation (AV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Oct 19, 2023@09:54:27 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>999999</strong> eRx Patient: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Status: <strong>NOT-MATCHED</strong></p>
<p><u>ERX PROVIDER | VISTA PROVIDER</u></p>
<p>Name: <strong>XXXXXXXX,XXXXX X</strong> |Name:</p>
<p>NPI : <strong>9999999999</strong> |NPI :</p>
<p>DEA : <strong>XX9999999</strong> |DEA :</p>
<p>Clinic : TEST CLINIC NAME |Class: _______________________________________|________________________________________</p>
<p>Address: |Address:</p>
<p><strong>1234 ERX TEST WAY</strong> |</p>
<p><strong>XXXXXXXX,XX 99999</strong> |</p>
<p>Tel: |Tel:</p>
<p>Fax: |Fax:</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Provider Not Auto Matched / Not Validated

If an auto-match is found, the Status in the header will show “AUTO-MATCHED” and the header will look similar to the below figure.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Oct 19, 2023@12:57:41 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>999999</strong> eRx Patient: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PROVIDER | VISTA PROVIDER</u></p>
<p>Name: <strong>XXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Address: |Address:</p>
<p><strong>99999 ERX TEST ST</strong> | <strong>99999 ERX TEST ST</strong></p>
<p><strong>XXXXXXX,XX 99999-9999</strong> | <strong>XXXXXXX,XX 99999</strong></p>
<p>Tel: <strong>888-888-8888</strong> |Tel: <strong>888-888-8888</strong></p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Provider Not Auto Matched / Not Validated

#### Edit Provider

To edit the provider information:

1.  Press the \<E\> Edit action on the Provider Validation screen.
1.  If no VistA provider information is in the system for the eR<sub>X</sub>, the system will look for any existing suggestion and will auto-match to the latest VistA suggestion on file. The user can then Accept, Forget, or Exit the provider’s name suggestion screen.
2.  If the user selects the Exit option, the system will prompt to enter/select provider at the “VISTA PROVIDER:” prompt. Enter either the partial name or full name of the provider or the NPI of the Provider, or DEA of the Provider. If multiple providers exist with the same name , a list of providers is provided with additional identifying information (e.g., middle initial, mail code, and title, where applicable, etc.).
3.  Select the provider.
2.  If a VistA provider is currently linked for the eR<sub>X</sub>, the system will ask if the current provider should be modified.
1.  Enter \<Y\> Yes.
2.  Enter either the partial name or full name of the provider at the “VISTA PROVIDER:” prompt.
3.  Select the provider.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER,TESTONE TEST</p>
<p>This Provider has already been validated.</p>
</blockquote>
<p>Would you like to edit the Provider? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Modify Current VistA Provider

> ‘This Provider has already been validated.’ – This verbiage only displays if the user attempts to edit a patient who has been previously validated.

4.  Once the VistA provider is selected, the VistA provider fields populate on the Provider Validation screen, along with information whether the DEA of the Provider has expired or not.
5.  The next step in the provider validation process is to accept the validation, which is described in the next section.

> **NOTE:** The DEA Expiration Date is displayed next to the DEA \# for the VistA Provider, and it will display in reverse video when the DEA \# of the selected VistA Provider has expired in File \#200. See below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Oct 19, 2023@10:21:35 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>9999999</strong> eRx Patient: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Status: <strong>AUTO-MATCHED</strong></p>
<p><u>ERX PROVIDER | VISTA PROVIDER</u></p>
<p>Name: <strong>XXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999 DEA EXP.: <mark>12/12/20</mark></strong></p>
<p>_______________________________________|________________________________________</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Warning for Expired DEA#

CS NOTE: The following message displays upon selecting the Provider if the Provider’s DEA date is expired.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider NPI mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p>eRx Written Date/Issue Date is after the VistA Provider DEA expiration date (May 25,2019) </p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider DEA Expiration Date Message

CS NOTE: The following block message displays upon selecting the Provider if the Provider’s eR<sub>X</sub> DEA number is missing.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Missing eRx Provider DEA# </p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Missing DEA Number Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Provider does not have a valid DEA number on file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>VistA Provider does not have a valid DEA# on file.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VistA Provider Missing DEA Number Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the eR<sub>X</sub> Provider does not have a valid DEA number on file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>eRx Provider does not have a valid DEA# on file.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select eRx Provider Missing DEA Number Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the eR<sub>X</sub> Provider’s DEA number does not match the VistA DEA number on file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider DEA mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider DEA Number Mismatch Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Drug selected is a Controlled Substance, but the VistA Provider is not authorized to write for the Schedule of the Drug.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>VistA Provider PROVIDER, TEST ONE is NOT authorized to write to the schedule ([C</p>
<p>-V]) of the VistA Drug selected.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VistA Provider Not Authorized Warning Message

CS NOTE: The following warning message displays upon selecting the Provider if the VistA Drug selected is a detox Drug and the VistA Provider does not have a valid detox number on file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>VistA Provider PROVIDER, TEST ONE does not have a valid DETOX#.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VistA Provider Missing DEA Number Warning Message

Provider Auto-Suggestion

When the user chooses the Edit (E) action to select a Vista Provider, if the eR<sub>X</sub> Provider has been previously matched to a VistA Provider, the user will be prompted for the VistA entry, and they will be presented with a suggestion based on the following logic below.

- Once a VistA Provider is matched and later validated to an eR<sub>X</sub> Provider it is then “remembered”.
- When a new eR<sub>X</sub> prescription is received for the same eR<sub>X</sub> Provider the “remembered” VistA Provider (s) are then presented as suggestions for the user to select.
- When there is only one suggestion the user is given 3 options: (A)ccept, (F)orget or (E)xit the suggested VistA record.
  - (A)ccept effectively matches the suggest VistA Provider with the eR<sub>X</sub>
  - (F)orget removes the VistA Provider as a valid suggestion for the eR<sub>X</sub> Patient so it is no longer presented in the future for any user
  - (E)xit Exits and proceed to match the VistA Provider manually
- If more than one suggestion exists, an additional action is presented:
  - (N)ext ignores the suggestion and moves on the next suggestion

Below is an example of auto-suggestion and prompting for the VistA Provider. The suggestions will be numbered (i.e. 1 of 1) and it will also display the eR<sub>X</sub> \# from the previously matched eR<sub>X</sub>.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER,TEST</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>05/22/25</strong>|</p>
<p>ERX PROVIDER VISTA PROVIDER|From eRx#: <strong>20241028318</strong> |</p>
<p>________________________________________________________________________________</p>
<p>Name: <strong>PROVIDER,TEST</strong> |Name: <strong>PROVIDER,TEST</strong></p>
<p>NPI : <strong>1366412157</strong> |NPI : <strong>1366412157</strong></p>
<p>DEA : <strong>FB5656802</strong> |DEA :</p>
<p>Clinic: |Class: <strong>NURSE PRACTITIONER</strong></p>
<p>________________________________________|_______________________________________</p>
<p>Address: |Address:</p>
<p><strong>900 CEDAR STREET</strong> | <strong>900 CEDAR STREET</strong></p>
<p><strong>JULESBURG,CO 80737</strong> | <strong>JULESBURG,CO 80737</strong></p>
<p>Tel: |Tel: (000) 000-0000</p>
<p>Fax: |Fax: (111) 111-1111</p>
<p>________________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (A)CCEPT (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Provider Validation Screen Display – Auto-Suggestion

The suggestion above is presented to the user because another eR<sub>X</sub> (#20241028318) was received in the past for the exact same eR<sub>X</sub> Provider and it was matched to the VistA Provider on the right and validated.

| NOTE: The software limits the number of distinct suggestions to 3. The order in which the suggestions are presented are from the newest (most recently “remembered”) to the oldest (last “remembered”). |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Accept Provider Validation

Once the correct provider has been selected and reviewed for accuracy, the next step is to accept the validation using the following steps.

1.  Select \<AV\> ACCEPT VALIDATION on the Provider Validation screen to accept the provider validation.

> **NOTE:** The following warning message displays upon selecting the validation if there is a DEA \# and/or NPI mismatch.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>* WARNING(S) </p>
<p>Provider NPI Mismatch.</p>
<p>Provider DEA Mismatch.</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Warning Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s Vista DEA number is missing.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider NPI mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p>Missing Vista Provider DEA#</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Missing VistA DEA Number Message

CS NOTE: The following block message displays upon selecting the validation if the Provider’s not authorized to write a scheduled Controlled Substance prescription.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider NPI mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p>VistA Provider PROVIDER, TEST ONE is NOT authorized to write to the schedule (2)</p>
<p>of the VistA Drug selected.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Not Authorized Message

CS NOTE: The following warning message displays upon selecting the validation if the eR<sub>X</sub> Provider does not have a valid DEA number and the Drug is not selected or the Drug selected is a Non-Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>eRx Provider does not have a valid DEA# on file.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select eRx Provider Missing DEA Number Warning Message

> **NOTE:** The following warning message displays upon selecting the validation if the VistA Provider does not have a valid DEA number on file and Drug is not selected or Drug selected is a Non-Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
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
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider NPI mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p>VistA Provider does not have a valid DEA# on file.</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VistA Provider Missing DEA Number Warning Message

> **NOTE:** The following block message displays upon selecting the validation if the eR<sub>X</sub> Provider’s DEA number does not match the VistA DEA number and Drug is not selected or Drug selected is a Non-Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th> Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>Provider DEA mismatch (eRx: 1366412157 | VistA: 1215926985)</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider DEA Mismatch Message

CS NOTE: The following block message displays upon selecting the validation if the VistA Drug selected is a Controlled Substance, but the VistA Provider is not authorized to write for the Schedule of the Drug.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th> Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>VistA Provider PROVIDER, TEST ONE is NOT authorized to write to the schedule ([C-V]</p>
<p>Of the VistA Drug selected.</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Not Authorized Message

CS NOTE: The following block message displays upon selecting the validation if the VistA Drug selected is a detox Drug, but the VistA Provider does not have a valid Detox number on file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th> Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit// E Edit</p>
<p>Current Vista Provider: PROVIDER, TEST ONE</p>
<p>Would you like to edit the Provider? NO// YES</p>
<p><em>&lt;a provider’s suggestion screen will appear here, if there are any&gt;</em></p>
<p>VISTA PROVIDER: PROVIDER, TEST ONE</p>
<p>* WARNING(S) *</p>
<p>VistA Provider PROVIDER, TEST ONE does not have a valid DETOX#.</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VistA Provider Invalid Detox Number Message

A message displays confirming whether to mark the provider as validated.

2.  Enter \<Y\> Yes.
3.  If the validation is successful, a message displays indicating that the validation was updated. Type \<Enter\> to continue or \<Shift\><sub>+</sub>\<^\> to Quit.

> **NOTE:** If there are other eR<sub>X</sub> for the patient, written by the same provider, received on the same day for that patient, a message displays asking if the provider validation should be applied to those eR<sub>X</sub>.

- The Status field changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/time stamp displays to the right of “VALIDATED”.
- In the Single eRx View/Display , after the patient has been validated using the Accept Validation (AV) action, the patient header will be appended with “VALIDATED" along with the user who performed the validation and the date/time stamp.
- A “V” is displayed to the PT column on the eRx Single Patient Queue screen to indicate that the patient has been validated.

> **NOTE:** The Status will not contain validation details until the user Accepts Validation (AV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Oct 19, 2023@11:25:44 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>99999999</strong> eRx Patient: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Status: <strong>NOT MATCHED</strong></p>
<p><u>ERX PROVIDER | VISTA PROVIDER</u></p>
<p>Name: <strong>XXXXXXXX,XXXXXXX</strong> |Name:</p>
<p>NPI : <strong>9999999999</strong> |NPI :</p>
<p>DEA : <strong>XX9999999</strong> |DEA :</p>
<p>_______________________________________|________________________________________</p>
<p>Address: |Address:</p>
<p><strong>123 FAKE STREET</strong> |</p>
<p><strong>PLANO,TX 75024</strong> |</p>
<p>Tel: |Tel:</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Edit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Before Provider Validation (Validate Provider Screen)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Provider Validation</strong> Oct 19, 2023@11:31:16 Page: 1 of 1</u></p>
<p>eRx Reference #: <strong>99999999</strong> eRx Patient: <strong>XXXXX,XXXXXXXXXX</strong></p>
<p>Status: <strong>MANUALLY-MATCHED | VALIDATED by XXXXXXXX,XXXX on 10/19/23@11:31:15</strong></p>
<p><u>ERX PROVIDER | VISTA PROVIDER</u></p>
<p>Name: <strong>XXXXXXXX,XXXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Address: |Address:</p>
<p><strong>123 FAKE STREET</strong> | <strong>123 FAKE STREET</strong></p>
<p><strong>PLANO,TX 75024</strong> | <strong>PLANO,TX 75024</strong></p>
<p>Tel: |Tel:</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After Provider Validation (Validate Provider Screen)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> May 16, 2025@10:37:33 Page: 1 of 5</u></p>
<p>eRx Patient: <strong>XXXXXXXXX,XXXXXXXX</strong> eRx Reference #: <strong>6791230457</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>03/10/25</strong></p>
<p>eRx Status: <strong>PR - PROCESSED</strong></p>
<p><u>ERX | VISTA</u></p>
<p><u>PATIENT AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21</u></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXX</strong></p>
<p>DOB : <strong>XXX 01, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>XXX 1,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: 555-555-55555 |Phone: 555-555-5555</p>
<p>STREET ADDRESS LNE1 STREET ARL...76017| STREET ADDRESS LNE1 STREET ARL...76017</p>
<p><u>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21:52</u></p>
<p>Name: <strong>YYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYY,YYYYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> Phone: |NPI : <strong>9999999999</strong> Phone: <strong>(222) 222-2222</strong></p>
<p>DEA : <strong>XX99999999</strong> |DEA :</p>
<p>Clinic: <strong>EXTERNAL PHARMACY</strong> |Class: <strong>PHYSICIAN</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>+ Enter ?? for more actions</p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After Provider Validation (Single eRx View/Display Screen)

#### Batch Provider Validation

When a provider validation is accepted on one eR<sub>X</sub> and there are additional eR<sub>X</sub> in the Holding Queue for the same patient by the same provider, received on the same day, a message displays asking if the other eR<sub>X</sub> for the patient written by the provider should be validated. If the user selects \<Y\> Yes, the system links and applies the provider validation for the eR<sub>X</sub> currently in the Holding Queue for the patient by the same provider.

> **NOTE:** Automatic Provider Validation is available only for NewRx and non-controlled substances.

The determination of the same provider is based on unique records from the ERX EXTERNAL PERSON file (#52.48). The system only validates the same provider on eR<sub>X</sub> that are currently in the ERX HOLDING QUEUE file (#52.49) for the same patient received on the same date. Provider validation is not applied for the same provider received after the auto validation is applied once. For example, if VA receives six eR<sub>X</sub> for the same patient on the same day from the same provider, the user only has to validate the provider once; however, if eR<sub>X</sub> are received after the automatic provider validation is applied (e.g., later that same day by that provider), the provider for those eR<sub>X</sub> needs to be validated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Would you like to mark this provider as VALIDATED?</p>
<p>Enter Yes or No: NO// y YES</p>
<p>Provider Match Validated!!</p>
<p>There are other prescriptions for this patient, written by this provider on</p>
<p>Oct 04, 2023</p>
<p>Provider: XXXXXXXX,XXXXX</p>
<p>Patient: XXXXXXXXXXX,XXXXXXXXXX</p>
<p>DRUG PROVIDER STA REC DATE</p>
<p>-------------------------------------------------------------------------------</p>
<p>1.) LORATADINE 10MG TAB XXXXXXXX,XXXXX I 10/04/23</p>
<p>Would you like to apply the above validation to these prescriptions?</p>
<p>Enter Yes or No: N//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Batch Provider Validation

To apply the provider validation to the other eR<sub>X</sub> enter \<Y\> Yes. A message displays indicating that the validation was updated.

- The Status field on all the eR<sub>X</sub>, where the provider validation has been applied, changes to “VALIDATED” on the Provider Validation screen and the user who accepted the validation and date/time stamp displays to the right of “VALIDATED”.
- In the Single eRx View/Display , after the patient has been validated using the Accept Validation (AV) action, the patient header will be appended with “VALIDATED" along with the user who performed the validation and the date/time stamp.
- A “V” is displayed to the PT column on the eRx Single Patient Queue screen to indicate that the patient has been validated.
- The statuses on all eR<sub>X</sub> validated by the automatic provider validation process changes to “I” for In Process.

#### View Suggestion(s) (VS hidden action)

This hidden action allows users to view and manage existing VistA Provider suggestions at any time, before or after the eRx has been accepted/processed, including “forgetting” erroneous suggestions. When viewing suggestions, the (A)ccept option is not available because this action is not supposed to be used for matching the provider, only to view and manage suggestions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>05/02/25</strong>|</p>
<p><mark>ERX PROVIDER</mark> <mark>VISTA PROVIDER</mark>|From eRx#: <strong>123431</strong> |</p>
<p>___________________________________________________________________________</p>
<p>Name: <strong>PROVIDER,TEST</strong> |Name: <strong>PROVIDER,TEST</strong></p>
<p>NPI : <strong>9999999999</strong> |NPI : <strong>9999999999</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>Clinic: <strong>TEST CLINIC NAME</strong> |Class: <strong>PHYSICIAN</strong></p>
<p>___________________________________|_______________________________________</p>
<p>Address: |Address:</p>
<p><strong>9876 HEALTH CIR</strong> | <strong>9876 HEALTH CIR</strong></p>
<p><strong>XXXXXXXXXXXX,XX 99999</strong> | <strong>XXXXXXXXXXXX,XX 99999</strong></p>
<p>Tel: <strong>999-999-9999</strong> |Tel: <strong>999-999-9999</strong></p>
<p>___________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Validate Drug/SIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The drug/SIG information on the eR<sub>X</sub> must be validated before a fillable eR<sub>X</sub> can be accepted.

> **NOTE:** A VistA patient must be linked (matched) before the Validate Drug/SIG action is available.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>To validate drug/SIG information for the eR<sub>X</sub>, type &lt;<strong>VD</strong>&gt; Validate Drug/SIG from the Single eRx View/Display screen. The Drug Validation screen displays and is described in the following sections. VP VALIDATE PATIENT VM VALIDATE PROVIDER VD (VALIDATE DRUG/SIG)</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Validate DRUG/SIG

#### VistA Dispense Drug Auto-Match

The preconditions for a VistA dispense drug auto-match are that the drug should be Active and should be marked for Outpatient use in the local DRUG file (#50).

First, the drug description on the new eR<sub>X</sub> is matched against the Drug Generic Name entry in the VistA instance’s DRUG file (#50). If successful, the match stops right here, and the drug is linked in VistA.

If the match is not successful, the drug description is then matched against the VA Product Name entry in the VistA instance’s VA PRODUCT file (#50.68). Then a drug in local DRUG file (#50) for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

If the match is not successful, the NDC is used to match against the VistA instance’s NDC/UPN file (#50.67). Using the VA Product Name identified at this step, a drug in the local file for the matched VA Product Name is identified, which should satisfy the preconditions. If the match is successful, the drug is linked in VistA.

> **NOTE:** The NDC is an optional field and may or may not be included with the new eR<sub>X</sub>. For a supply, if UPC is sent, it is not matched against the NDC/UPN file (#50.67). Only the Drug Description match is attempted.

#### VistA Drug/SIG Drug Auto-Match from a Suggestion

The preconditions for pre-population of all VistA fields related to the Drug (SIG, Dosage, Days Supply, \# of Refills, Quantity) from an existing suggestion when the eRx is received are:

- The eRx must have a successful VistA Dispense Drug auto-match (described above)
- There has to be at least one suggestion on file for the Drug/SIG (VistA Rx)

> The VistA Dispense Drug in the suggestion must match the VistA Dispense Drug previously auto-matched.

#### Drug/SIG Manual Validation Screen Overview

The Drug/SIG Validation screen show the eR<sub>X</sub> Drug and VistA Drug side-by-side and identify the discrepancies in the data with reverse video.

The header of the Drug/SIG Validation screen contains the eR<sub>X</sub> Reference \#, eRx Patient , Date Written, Effective Date, and the Status. Below the header is the eR<sub>X</sub> and VistA information for the drug/SIG, where applicable.

If a match was NOT found for the VistA drug, the screen looks similar to the below figure. The Status field has “NOT MATCHED” in the header. The other VistA drug/SIG fields may or may not be populated.

> **NOTE:** The Status will not contain validation details until the user Accepts Validation (AV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Drug Validation</strong> May 19, 2025@12:10:49 Page: 1 of 2</u></p>
<p>eRx Reference #: <strong>99999999</strong> eRx Patient: <strong>MBMONE,TESTONE TEST</strong></p>
<p>Date Written : <strong>10/18/23</strong> Effective Date:</p>
<p>Status: <strong>NOT MATCHED</strong></p>
<p><u>ERX MED | VISTA MED</u></p>
<p>Allergy: |Allergy:</p>
<p><mark>NO ALLERGY INFORMATION RECEIVED</mark> | NO KNOWN ALLERGIES</p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>ACETAMINOPHEN 325MG TAB</strong> |<u>1)</u>Drug:</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY FOUR HOURS</strong> |</p>
<p><strong>AS NEEDED</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Prescriber Drug Use Evaluation: |2) Dosage:</p>
<p>Co-Agent: Nsaids (Non-Steroidal Anti-In|</p>
<p>flammatory Drug) |3)Patient Instructions:</p>
<p>Reason: Drug-Allergy |</p>
<p>Result: Prescribed w/ acknowledgements |</p>
<p>Acknowledgement: Previously Tolerated |</p>
<p>_______________________________________|________________________________________</p>
<p>Provider Notes/Comments: |4)Provider Comments:</p>
<p>|<u>5)</u>Pat. Status:</p>
<p>_______________________________________|________________________________________</p>
<p>Quantity: <strong>30</strong> |<u>6)</u>Quantity:</p>
<p>Dispense Unit: | Dispense Unit:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>11</strong> |<u>7)</u>Days Supply: <u>8)</u>Refills:</p>
<p>_______________________________________|________________________________________</p>
<p>|<u>9)</u>Routing:</p>
<p>_______________________________________|________________________________________</p>
<p>|<u>10)</u>Clinic:</p>
<p>_______________________________________|________________________________________</p>
<p>Primary Dx: |<u>11)</u>Indications:</p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Edit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation Screen Display - VistA Drug Not Validated / Not Auto Matched

If a VistA match was found for the drug where the dispense drug matches exactly (Drug Name, NDC, SIG, Quantity, Days Supply, \# of

Refills and Substitution allowance ), the screen looks similar to the figure below. The Status field has “SUGGESTED”, with VistA drug/SIG information displaying in the VistA Drug field (#1).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Drug Validation</strong> May 19, 2025@12:47:59 Page: 1 of 3</u></p>
<p>eRx Reference #: <strong>99999999</strong> eRx Patient: <strong>MBMONE,TESTONE TEST</strong></p>
<p>Date Written : <strong>10/18/23</strong> Effective Date:</p>
<p>Status: <strong>SUGGESTED</strong></p>
<p><u>ERX MED | VISTA MED</u></p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| EGG PRODUCTS,PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>ACETAMINOPHEN 325MG TAB</strong> |<u>1)</u> Drug: <strong>ACETAMINOPHEN 325MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; DU: INCREMENTS OF 100 ONLY</strong></p>
<p>| <strong>* TCGRx &amp; SCRIPTPRO *</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY FOUR HOURS</strong> |</p>
<p><strong>AS NEEDED</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>|<u>2)</u> Dosage:</p>
<p>_______________________________________|</p>
<p>|<u>3)</u>Patient Instructions:</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation Screen Display - VistA Drug Auto Matched / Not Validated

If a VistA match was identified solely in cases where the dispensed drug is already prepopulated, the screen looks similar to the figure below. The Status field has “MANUALLY-MATCHED”, with VistA drug/SIG information displaying in the VistA Drug field (#1).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Drug Validation</strong> May 19, 2025@12:47:59 Page: 1 of 3</u></p>
<p>eRx Reference #: <strong>202505270001</strong> eRx Patient: <strong>TESTTWO,MBMTWO</strong></p>
<p>Date Written : <strong>5/27/25</strong> Effective Date:</p>
<p>Status: <strong>MANUAL ENTRY</strong></p>
<p><u>ERX MED | VISTA MED</u></p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| EGG PRODUCTS,PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>SIMVASTATIN 80MG TAB</strong> |<u>1)</u>Drug: <strong>SIMVASTATIN 80MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM *TABS SPLIT*</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE-HALF TABLET MOUTH EVERY DAY</strong> |</p>
<p>_______________________________________|________________________________________</p>
<p>Prescriber Drug Use Evaluation: |<u>2)</u> Dosage:</p>
<p><strong>None</strong> |</p>
<p>|<u>3)</u>Patient Instructions:</p>
<p>| <strong>FOR CHOLESTEROL</strong></p>
<p>_______________________________________|________________________________________</p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation Screen Display - VistA Drug Manually Matched / Not Validated

#### Drug Suggestion

This functionality was designed for two purposes: 1) Save the users time and; 2) Improve accuracy of the VistA fields entered to match the incoming eR<sub>X</sub>. It works by first creating a “memory” of how each incoming eR<sub>X</sub> are being translated into a VistA prescription. This memory is recorded at the moment the corresponding Pending Order of an eR<sub>X</sub> is finished and becomes an Active (or Suspended) VistA prescription (when a record is created in the PRESCRIPTION file (#52)). At this point the software will gather the following field values from the incoming eR<sub>X</sub> record:

- Drug Name
- Drug NDC Code
- Quantity
- Substitutions Allowed?
- Days Supply
- Number of Refills
- SIG

If Drug Name, Drug NDC Code or Quantity are not present the software will not proceed.

The software then generates a long number composed of the following numbers concatenated:

NDC Code_Drug Hash (Name+SIG)\_Subs_Quantity_Days Supply_Number of Refills

| Drug Hash is a number generated by summing the ASCII values of the Drug Name concatenated with the SIG, where each letter/number on the string are multiplied by their position on the string with an ascending and then a descending order. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The result of the algorithm above is a unique long number for the specific eR<sub>X</sub> received from outside, which is recorded on the eR<sub>X</sub> record as a cross-reference.

At the moment that the user selects to edit the Drug for another eR<sub>X</sub>, the same long number is generated for the eR<sub>X</sub> and is checked against the database to find if matches with a previous eR<sub>X</sub> that was already completed and finished. If a perfect match is found, then the software will retrieve the information from the VistA Prescription and will present it to the user as an option to automatically pre-fill all the fields related to the drug, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>06/11/23</strong>|</p>
<p>ERX MED VISTA MED |From Rx#: <strong>9999999</strong> |</p>
<p>________________________________________________________________________________</p>
<p>Drug: <strong>Meloxicam 15mg Tablet</strong> |Drug: <strong>MELOXICAM 7.5MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>________________________________________|_______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY SIX HOURS</strong> | <strong>TAKE TWO TABLETS BY MOUTH ONCE EVERY</strong></p>
<p><strong>AS NEEDED</strong> | <strong>SIX HOURS</strong> <strong>WITH FOOD - IF SPLITTING</strong></p>
<p>| <strong>TABLET, SPLIT JUST PRIOR TO USE</strong></p>
<p>________________________________________|_______________________________________</p>
<p>|Patient Instructions:</p>
<p>| <strong>- IF SPLITTING TABLET, SPLIT JUST</strong></p>
<p>| <strong>PRIOR TO USE</strong></p>
<p>________________________________________|_______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>|</p>
<p>________________________________________|_______________________________________</p>
<p>Quantity: 90 |Quantity: 180</p>
<p>Dispense Unit: |Dispense Unit: <strong>TAB</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>| <strong><u>TEST DISPENSE MESSAGE</u></strong></p>
<p>________________________________________|_______________________________________</p>
<p>Days Supply: 90 Refills: 3 |Days Supply: 30 Refills: 11</p>
<p>________________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT// ?</p>
<p><span id="View_RX" class="anchor"></span>VIEW RX - View VistA Rx where the suggestion is coming from</p>
<p>ACCEPT - Accepts the suggested data (right column) and pre-populates the</p>
<p>VistA fields</p>
<p>NEXT - Ignores the current suggestion and view the next one</p>
<p>FORGET - Forgets the current suggestion so that it is not presented again</p>
<p>in the future to any user</p>
<p>EXIT - Exits and continue to filling the VistA fields manually</p>
<p>Select one of the following:</p>
<p>V VIEW RX</p>
<p>A ACCEPT</p>
<p>N NEXT</p>
<p>F FORGET</p>
<p>E EXIT</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** The software limits the number of distinct suggestions to 3. The order in which the suggestions are presented are from the newest (most recently “remembered”) to the oldest (last “remembered”).

If more than one distinct suggestion exists, the software will display slightly different. It will start with the latest matched VistA Rx and will go back to the previous ones, one by one if the user selects NEXT below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|Sugg. <strong>1</strong> of <strong>2</strong> - <strong>06/11/23</strong>|</p>
<p>ERX MED VISTA MED |From Rx#: <strong>9999999</strong> |</p>
<p>________________________________________________________________________________</p>
<p>Drug: Meloxicam 15mg Tablet |Drug: <strong>MELOXICAM 15MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>________________________________________|_______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY SIX HOURS</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE EVERY</strong></p>
<p><strong>AS NEEDED</strong> | <strong>SIX HOURS</strong> <strong>WITH FOOD - IF SPLITTING</strong></p>
<p>| <strong>TABLET, SPLIT JUST PRIOR TO USE</strong></p>
<p>________________________________________|_______________________________________</p>
<p>|Patient Instructions:</p>
<p>| <strong>- IF SPLITTING TABLET, SPLIT JUST</strong></p>
<p>| <strong>PRIOR TO USE</strong></p>
<p>________________________________________|_______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>|</p>
<p>________________________________________|_______________________________________</p>
<p>Quantity: 90 |Quantity: 30</p>
<p>Dispense Unit: |Dispense Unit: <strong>TAB</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>| <strong><u>TEST DISPENSE MESSAGE</u></strong></p>
<p>________________________________________|_______________________________________</p>
<p>Days Supply: 90 Refills: 3 |Days Supply: 30 Refills: 11</p>
<p>________________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (N)EXT (F)ORGET (E)XIT: NEXT// ?</p>
<p>VIEW RX - View VistA Rx where the suggestion is coming from</p>
<p>ACCEPT - Accepts the suggested data (right column) and pre-populates the</p>
<p>VistA fields</p>
<p>NEXT - Ignores the current suggestion and view the next one</p>
<p>FORGET - Forgets the current suggestion so that it is not presented again</p>
<p>in the future to any user</p>
<p>EXIT - Exits and continue to filling the VistA fields manually</p>
<p>Select one of the following:</p>
<p>V VIEW RX</p>
<p>A ACCEPT</p>
<p>N NEXT</p>
<p>F FORGET</p>
<p>E EXIT</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (N)EXT (F)ORGET (E)XIT: NEXT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user selects VIEW above, allow the user to view the VistA Rx information before accepting it. If the user select V a notice will be displayed before taking the user to view the Suggested VistA Rx detail.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT// V VIEW RX</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>NOTICE</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>You will be taken to the VistA Rx#9999999 that was entered in the past for the</p>
<p>same Product (NDC/SIG/Qty/Days Supply/# of Refills/Substitution) for a different</p>
<p>eRx. This VistA Rx may or may not be for the same patient in this erx being</p>
<p>processed.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user selects ACCEPT above, the VistA fields for the drug will be auto-populated and the users will be taken back to the Validate Drug/SIG where they can edit the fields manually by selecting each field number.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT// ACCEPT</p>
<p>Updating...done.</p>
<p><u><strong>Drug Validation</strong> Nov 11, 2023@14:21:45 Page: 1 of 3</u></p>
<p>eRx Reference #: <strong>9999999</strong> eRx Patient: <strong>XXXXXXXXX,XXXXXXXXXX</strong></p>
<p>Date Written : <strong>6/10/23</strong> Effective Date:</p>
<p>Status: <strong>MANUALLY-MATCHED</strong></p>
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
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| <mark>ABOLENE</mark>,<mark>ACEBUTOLOL</mark>,<mark>MOLD</mark>,<mark>POLLEN</mark></p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>Meloxicam 15mg Tablet</strong> |1)Drug: <strong>MELOXICAM 15MG TAB</strong></p>
<p>Substitution? <strong><mark>NO</mark></strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY SIX HOURS</strong> | <strong>TAKE ONE TABLET BY MOUTH EVERY SIX</strong></p>
<p><strong>AS NEEDED</strong> | <strong>HOURS - IF SPLITTING TABLET, SPLIT</strong></p>
<p>| <strong>JUST PRIOR TO USE</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Prescriber Drug Use Evaluation: |2) Dosage: <strong>15 (MG)</strong></p>
<p>None | Verb: <strong>TAKE</strong></p>
<p>|Disp. Units: <strong>1</strong></p>
<p>| Noun: <strong>TABLET</strong></p>
<p>| Route: <strong>ORAL</strong></p>
<p>| Schedule: <strong>Q6H</strong></p>
<p>|</p>
<p>|3)Patient Instructions:</p>
<p>| <strong>- IF SPLITTING TABLET, SPLIT JUST</strong></p>
<p>| <strong>PRIOR TO USE</strong></p>
<p>___________________________________|___________________________________</p>
<p>Provider Notes/Comments: |4)Provider Comments:</p>
<p>|</p>
<p>___________________________________|___________________________________</p>
<p>|5)Pat. Status: <strong>SC LESS THAN 50%</strong></p>
<p>___________________________________|___________________________________</p>
<p>Quantity: <mark>90</mark> |6)Quantity: <mark>30</mark></p>
<p>Dispense Unit: <strong>Tablet</strong> | Dispense Unit: <strong>TAB</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |</p>
<p>___________________________________|___________________________________</p>
<p>Days Supply: <mark>90</mark> Refills: <mark>3</mark> |7)Days Supply: <mark>30</mark> 8)Refills: <mark>11</mark></p>
<p>___________________________________|___________________________________</p>
<p>|9)Routing: <strong>MAIL</strong></p>
<p>___________________________________|___________________________________</p>
<p>|10)Clinic: <strong>CC CLINIC</strong></p>
<p>___________________________________|___________________________________</p>
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
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user selects FORGET the following message will be presented:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT// FORGET</p>
<p>Are you sure this suggestion match should be forgotten? NO// ?</p>
<p>This suggestion originated from a VistA Rx previously dispensed for an</p>
<p>eRx with the exact Drug Name, NDC, SIG, Quantity, Days Supply, # of</p>
<p>Refills and Substitution allowance. Once you forget this match it will</p>
<p>no longer be suggested as a match for future eRx's with the same fields.</p>
<p>Select one of the following:</p>
<p>Y YES</p>
<p>N NO</p>
<p>Are you sure this suggestion match should be forgotten? NO// YES</p>
<p>Forgetting...Ok.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** If the user chooses YES to forget the entry it will no longer be presented as a suggestion to any user when a similar prescription to this eR<sub>X</sub> is received again in the future.

If no perfect match exists for the number generated, the user will be prompted to enter the drug manually, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Edit// Edit</p>
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
<p>eRx Drug : <strong>LEVOTHYROXINE NA (SYNTHROID) 50MCG TAB</strong></p>
<p>eRx SIG : <strong>TAKE ONE TABLET MOUTH EVERY DAY</strong></p>
<p>eRx Notes: <strong>TEST.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>30</strong> Days Supply: <strong>30</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: LEVOTHYROXINE NA (SYNTHROID) 300MCG TAB</p>
<p>Select DRUG GENERIC NAME: LEVOTHYROXINE NA (SYNTHROID) 300MCG TAB//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If the user selects EXIT, the user will be prompted to enter the drug information manually:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT// EXIT</p>
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
<p>eRx Drug : <strong>LEVOTHYROXINE NA (SYNTHROID) 50MCG TAB</strong></p>
<p>eRx SIG : <strong>TAKE ONE TABLET MOUTH EVERY DAY</strong></p>
<p>eRx Notes: <strong>TEST.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>30</strong> Days Supply: <strong>30</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: LEVOTHYROXINE NA (SYNTHROID) 50MCG TAB</p>
<p>Select DRUG GENERIC NAME: LEVOTHYROXINE NA (SYNTHROID) 50MCG TAB//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Edit Drug/SIG

1.  To edit the drug/SIG information, use the \<E\> Edit action on the Drug Validation screen.
2.  If the VistA drug/SIG information has been linked for the eR<sub>X</sub>, the edit drug/SIG sequence prompts the user to select a field or select All fields.
    - Select Item (s): Quit// \<E\> Edit or enter the field(s) at this prompt (i.e. 1, 1-3, etc.)
    - Which fields (s) would you like to edit? (1-10) or “A” 11: A//
3.  Under Single eR<sub>X</sub> View/Display \> VALIDATE DRUG/SIG screen \> Edit, if a drug is already matched in the hub, that drug is displayed at the “select” prompt. The user is still allowed to change the drug by entering the drug name.
7.  Under Single eR<sub>X</sub> View/Display \> VALIDATE DRUG/SIG screen \> Edit, if a drug is not matched in the hub, at the “select” prompt, it is blank wherein the user can enter the drug name.
8.  When a Yes/No confirmation is asked for the selected drug, if the user hits enter or selects “No”, the control comes out of Edit mode back to VD screen.

> **NOTE:** The eR<sub>X</sub> Drug/SIG information from the external provider displays throughout the edit drug/SIG process as reference.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Current Vista Drug: MELOXICAM 7.5MG TAB</p>
<p>Select DRUG GENERIC NAME: MELOXICAM 7.5MG TAB// MS102 NATL FORM (2/10)</p>
<p>You have selected: MELOXICAM 7.5MG TAB</p>
<p>Would you like to use this drug/supply?</p>
<p>Enter Yes or No: YES</p>
<p><u><strong>ORIGINAL ERX</strong> _</u></p>
<p>eRx Drug : <strong>MELOXICAM 7.5MG TAB</strong></p>
<p>eRx SIG : <strong>Take two tabs by mouth daily</strong></p>
<p>eRx Notes: <strong>Take with food</strong></p>
<p>Drug Form: <strong>Tablet</strong> Strength: <strong>7.5MG</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure: <strong>Tablet</strong></p>
<p>Qty: <strong>30</strong> Days Supply: <strong>30</strong> Refills: <strong>11</strong> Substitutions: <strong>YES</strong></p>
<p><u>__________________________________________________________________________________</u></p>
<p>There are 2 Available Dosage(s):</p>
<p>1. 7.5MG</p>
<p>2. 15MG</p>
<p>Select from list of Available Dosages (1-2), Enter Free Text Dose</p>
<p>or Enter a Question Mark (?) to view list: 1 7.5MG</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Display during Edit Drug/SIG

9.  Next, enter the Dosage. Either enter a free text dose or enter a question mark \<?\> to view a list of available dosages. The system prompts the user to confirm the selected dosage.
1.  Enter the Verb, Route, and Schedule.
2.  Patient Instructions are default/consistent instructions that come from the Orderable Item. VA Patient Instructions are auto populated when either a drug is auto matched or manually matched, or the drug’s Pharmacy Order Item has an entry for those instructions. If it is blank, enter VA Patient Instructions. If it needs to be edited, use the Replace function. Even abbreviated Patient Instructions from Medication Instruction files are allowed, which expand upon saving. This field holds the patient instructions for an eR<sub>X</sub>. This field is transferred to the Pending Queue upon acceptance of an eR<sub>X</sub>.
3.  Provider Comments are additional free text comments that the provider may enter. The VA Provider Comments field contains the eR<sub>X</sub> Notes from the external provider and can be edited by entering \<Replace\>. Even abbreviated Provider Comments from Medication Instruction files are allowed, which expand upon saving. This field is transferred to the Pending Queue upon acceptance of an eR<sub>X</sub>.
4.  Enter Patient Status and edit the Patient Status as required.
5.  Enter/edit VistA Quantity, VistA Days Supply, and VistA Renewals as needed.

> **NOTE:** The Vista Days Supply prompt is pre-populated with an auto-calculated value given to the user as a suggested value for the Days Supply prompt. This value is displayed as \[DAYS SUPPLY:(1-90): 90//\], with suggested value behind two forward slashes. This value is derived from the values entered by the user in the Quantity prompt, the Units Per Dose prompt, and the Schedule prompt. The auto-calculated value is the result of dividing the Quantity by the Units Per Dose, then dividing the resulting value by the Schedule (Units Per Dose/Quantity/Schedule). This auto-calculated value is only a suggested entry for the user. The user can enter any amount that fits within the Days Supply range supplied by the eRX software.

When editing the Quantity field after the VistA drug has been linked, the Vista Quantity prompt is pre-populated with an auto-calculated value as a suggested value to the user. This value is displayed as \[QTY:(1-90): 90//\], with the suggested value behind two forward slashes. This value is derived from the values entered by the user in the Days Supply prompt, the Units Per Dose prompt, and the Schedule prompt. The auto-calculated value is the result of dividing the Days Supply by the Units Per Dose, then dividing the resulting value by the Schedule (Units Per Dose/Days Supply/Schedule). This auto-calculated value is only a suggested entry for the user. The user can enter any amount that fits within the Quantity range supplied by the eRX software.

6.  <span id="Park_Functionality" class="anchor"></span>Enter Routing. Either \<M\> for Mail, \<W\> for Window or \<P\> for Park.
7.  The system displays the Default eR<sub>X</sub> Clinic setup by the site. If it is not configured, this field is blank. The user can select a clinic as required in either case.

> **NOTE:** Setting up the Default eR<sub>X</sub> Clinic is optional. Sites are encouraged to edit their OUTPATIENT SITE file (#59) to define the default eR<sub>X</sub> clinic. The following field is added to the OUTPATIENT SITE file (#59): DEFAULT ERX CLINIC field (#10).

Please reference the Implementation Guide – Inbound ePrescribing (PSO\*7.0\*p581) on the VA Documentation Library (VDL) at the following link for details on setting up the default eR<sub>X</sub> clinic for a site.

Outpatient Pharmacy VDL URL: <https://www.va.gov/vdl/application.asp?appid=90>

8.  <span id="Indication" class="anchor"></span>Enter the Indication for Use (Optional). This field works similarly to Backdoor Pharmacy.
9.  Once all the drug/SIG fields have been edited and the drug/SIG sequence is complete, the edited information displays on the Drug Validation screen.
10. The next step is to accept the validation \<AV\>, which is described in the next section.
11. If you have to edit after this, you can pick the fields:
    - Select Item (s): Quit// E Edit
    - Which fields (s) would you like to edit? (1-11) or “A” 11: A//

> **NOTE:** If the Default eR<sub>X</sub> Clinic is changed from the one that is configured with the NPI Institution, of the receiving Pharmacy, the eR<sub>X</sub> may not show up in OERR when processed. Refer to the Implementation Guide – Inbound ePrescribing (PSO\*7.0\*p581) on the VA Documentation Library (VDL) for details on setting up the Default eR<sub>X</sub> Clinic for a site.

CS NOTE: The following block message displays upon selecting the Drug validation if the Provider is not authorized to write a scheduled Controlled Substance prescription.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/002.png)

Select Provider Not Authorized Message

CS NOTE: The following warning message displays upon selecting the validation if the Provider does not have a valid Detox number.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// E Edit</p>
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
<p>eRx Drug : LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>eRx SIG : TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Notes: This is a TEST NOTE.</p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: Original Quantity Qty Unit of Measure:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3 Substitutions: YES</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: LORAZEPAM 2MG/ML ORAL CONCENTRATE [C-IV]*(N/F)*</p>
<p>Select DRUG GENERIC NAME: LORAZEPAM 2MG/ML ORAL CONCENTRATE// CN302</p>
<p>N/F NATL N/F; 30 mL/BT (CS MENU) NON CMOP DRUG</p>
<p>*INVALID DRUG</p>
<p>VistA Provider TEST,PROVIDER does not have a valid DETOX#.</p>
<p>*</p>
<p>Press Return to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Provider Missing Valid Detox Number Warning Message

CS NOTE: The following block message displays upon selecting the Drug validation if the eR<sub>X</sub> is Non-Controlled Substance and the VistA drug is a Controlled Substance. The Accept Validation will be blocked.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ED Edit</p>
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
<p>eRx Drug : IBUPROFEN 200MG TAB</p>
<p>eRx SIG : TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Notes: This is a TEST NOTE.</p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: Original Quantity Qty Unit of Measure:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3 Substitutions: YES</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: IBUPROFEN 200MG TAB</p>
<p>Select DRUG GENERIC NAME: IBUPROFEN 200MG TAB// LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>CN302 N/F NATL N/F; 30 mL/BT (CS MENU) NON CMOP DRUG</p>
<p>*INVALID DRUG</p>
<p>eRx is not digitally signed and VistA Drug is not matched to an NDF item marked with a CS Federal Schedule but is locally marked as a controlled substance ([C-IV]).</p>
<p>*</p>
<p>Press Return to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Blocked Accept Validation Message

CS NOTE: The following warning message displays upon selecting an eRx that is a Controlled Substance, but the VistA drug selected is a Non-Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// E Edit</p>
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
<p>eRx Drug : LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>eRx SIG : TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Notes: This is a TEST NOTE.</p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: Original Quantity Qty Unit of Measure:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3 Substitutions: YES</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: LORAZEPAM 2MG/ML ORAL CONCENTRATE [C-IV]*(N/F)*</p>
<p>Select DRUG GENERIC NAME: LORAZEPAM 2MG/ML ORAL CONCENTRATE// IBUPROFEN 100MG/5ML SUSP MS102 NATL FORM; 120 ML/BT DOD VHA TRANS</p>
<p>* WARNING(S) </p>
<p>eRx was digitally signed by the prescriber and VistA Drug selected is Non-CS. Please, review and make sure you selected the correct drug.</p>
<p>*</p>
<p>You have selected: IBUPROFEN 100MG/5ML SUSP</p>
<p>Would you like to use this drug/supply?</p>
<p>Enter Yes or No:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation Warning Message

CS NOTE: The following block message displays upon selecting an eR<sub>X</sub> that is not digitally signed, and the VistA drug is a Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ED Edit</p>
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
<p>eRx Drug : IBUPROFEN 200MG TAB</p>
<p>eRx SIG : TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Notes: This is a TEST NOTE</p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: Original Quantity Qty Unit of Measure:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3 Substitutions: YES</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: IBUPROFEN 200MG TAB</p>
<p>Select DRUG GENERIC NAME: IBUPROFEN 200MG TAB// LORAZEPAM 2MG/ML ORAL CONCENTRATE</p>
<p>CN302 N/F NATL N/F; 30 mL/BT (CS MENU) NON CMOP DRUG</p>
<p>*INVALID DRUG</p>
<p>eRx is not digitally signed and VistA Drug is marked as CS ([C-IV]).</p>
<p>*</p>
<p>Press Return to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation eRx without DS Message

> **NOTE:** The following block message displays upon selecting an eRx that is digitally signed, and the VistA drug is a Non-Controlled Substance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// ED Edit</p>
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
<p>eRx Drug : IBUPROFEN 200MG TAB</p>
<p>eRx SIG : TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</p>
<p>eRx Notes: This is a TEST NOTE</p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: Original Quantity Qty Unit of Measure:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3 Substitutions: YES</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Current Vista Drug: IBUPROFEN 200MG TAB</p>
<p>Select DRUG GENERIC NAME: IBUPROFEN 200MG TAB// CODEINE SULFATE 30MG TAB</p>
<p>CN101 NATL FORM *TABS SPLIT* DOD VHA TRANS</p>
<p>*INVALID DRUG</p>
<p>eRx is not digitally signed and VistA Drug is marked as CS ([C-II]).</p>
<p>*</p>
<p>Press Return to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug Validation eRx without DS Message

CS NOTE: The following block message displays upon selecting an eR<sub>X</sub> that does not have a valid DEA number on file for the eR<sub>X</sub> Provider.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/003.png)

Drug Validation eRx with Invalid eRx Provider DEA Number Message

CS NOTE: The following block message displays upon selecting an eRx that doesn’t have a valid DEA number on file for the VistA Provider.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/004.png)

Drug Validation eRx with Invalid VistA Provider DEA Number Message

> **NOTE:** The following block message displays upon selecting an eR<sub>X</sub> that has a mismatched DEA number on file for the Provider.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/005.png)

Drug Validation eRx with Provider DEA Number Mismatch Message

CS NOTE: The following warning message displays upon selecting an eR<sub>X</sub> that was written or issues after the VistA Provider’s DEA number has expired.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/006.png)

Drug Validation eRx Written After VistA Provider DEA Expiration Warning Message

CS NOTE: The following block message displays upon selecting an eR<sub>X</sub> that does not have a valid VistA Provider detox number on file.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/007.png)

Drug Validation eRx VistA Provider Invalid DEA Number Message

CS NOTE: The following warning message displays upon selecting an eR<sub>X</sub> that does not have a valid VistA Provider authorization to write the drug schedule.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/008.png)

Drug Validation eRx VistA Provider Not Authorized Warning Message

CS NOTE: The following warning message displays upon selecting an eR<sub>X</sub> that is written/issued after the VistA Provider’s DEA expiration date.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/009.png)

Drug Validation eRx VistA Provider Not Authorized Warning Message

#### View Suggestion(s) (VS hidden action)

This hidden action allows users to view and manage existing VistA Drug suggestions at any time, before or after the eRx has been accepted/processed, including “forgetting” erroneous suggestions. When viewing suggestions, the (A)ccept option is not available because this action is not supposed to be used for matching the drug information, only to view and manage suggestions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// VS</p>
<p>|Sugg. <strong>1</strong> of <strong>1</strong> - <strong>03/19/24</strong>|</p>
<p><mark>ERX MED</mark> <mark>VISTA MED</mark> |From Rx#: <strong>2298007</strong> |</p>
<p>___________________________________________________________________________</p>
<p>Drug: <strong>DOCUSATE CA 240MG CAP</strong> |Drug: <strong>DOCUSATE CA 240MG CAP</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (09/01) (INCREMENT OF</strong></p>
<p>| <strong>100s)</strong></p>
<p>___________________________________|_______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>1 CAP PO DAILY</strong> | <strong>TAKE ONE CAPSULE BY MOUTH ONCE DAILY</strong></p>
<p>___________________________________|_______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p>|</p>
<p>___________________________________|_______________________________________</p>
<p>Quantity: <strong>30</strong> |Quantity: <strong>30</strong></p>
<p>Dispense Unit: |Dispense Unit: <strong>CAP</strong></p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>| <strong>CAP (INCREMENTS OF 100)</strong></p>
<p>___________________________________|_______________________________________</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>11</strong> |Days Supply: <strong>30</strong> Refills: <strong>11</strong></p>
<p>___________________________________|_______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (F)ORGET (E)XIT: EXIT//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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

#### Copy Patient Instructions Prompt

After accepting the suggested Rx on the eRx Drug Validation Edit action screen, the user will be prompted to see whether they want to copy the patient instructions from the suggested Rx into the eRx, as shown below. The default for this prompt is 'NO'.

> **NOTE:** The prompt below will only appear if the Pharmacy Orderable Item for the drug does not have Patient Instructions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// e Edit</p>
<p>|Sugg. <strong>1</strong> of <strong>2</strong> - <strong>03/11/25</strong>|</p>
<p>ERX MED VISTA MED |From Rx#: <strong>3059546</strong> |</p>
<p>_______________________________________________________________________________</p>
<p>Drug: LEVOTHYROXINE NA (SYNTHROID) 50MC |Drug: LEVOTHYROXINE NA (SYNTHROID) 50M</p>
<p>G TAB | CG TAB</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; VA STND DRUG</strong></p>
<p>________________________________________|______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET MOUTH EVERY DAY</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>| <strong>BEFORE MEAL FOR THYROID HORMONE</strong></p>
<p>| <strong>REPLACEMENT - TAKE AT LEAST AN HOUR</strong></p>
<p>| <strong>BEFORE FOOD OR OTHER MEDICATIONS</strong></p>
<p>________________________________________|______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p><strong>TESTING FOR ERX BATCH CHANGE REQUEST.</strong> | <strong>TESTING FOR ERX BATCH CHANGE REQUEST.</strong></p>
<p>________________________________________|______________________________________</p>
<p>Quantity: <strong>30</strong> |Quantity: <strong>30</strong></p>
<p>Dispense Unit: |Dispense Unit: <strong>TAB</strong></p>
<p>________________________________________|______________________________________</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>3</strong> |Days Supply: <strong>30</strong> Refills: <strong>3</strong></p>
<p>________________________________________|______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (N)EXT (F)ORGET (E)XIT: NEXT// ACCEPT</p>
<p>Rx #<strong>3059546</strong> PATIENT INSTRUCTIONS:</p>
<p><strong>FOR THYROID HORMONE REPLACEMENT - TAKE AT LEAST AN HOUR BEFORE FOOD OR OTHER</strong></p>
<p><strong>MEDICATIONS</strong></p>
<p>Copy PATIENT INSTRUCTIONS from Rx #<strong>3059546</strong>? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1)  If YES is chosen by the user, all fields on the eRx Drug Validation screen will have its fields updated with any available data.
2)  If NO is chosen by the user, all fields on the eRx Drug Validation screen will have its fields updated with any available data, with the exception of the Patient Instruction field. The user can manually edit the field as they currently do.
3)  When the user inputs the up-caret symbol (^), no changes are made.

#### Accept Drug/SIG Validation

Once the VistA Drug/SIG information has been edited and reviewed for accuracy, the next step is to accept the validation \<AV\> on the Drug Validation screen. The system prompts the user to confirm the validation. After entering \<Y\> Yes, a message displays that the drug validation has been updated.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen// AV Accept Validation</p>
<p>Would you like to mark this drug as VALIDATED?</p>
<p>Enter Yes or No: YES//</p>
<p>Drug/SIG Match Validated!!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Confirm Acceptance of Drug / SIG ValidationCS NOTE: The following block message displays upon selecting an eR<sub>X</sub> that does not have a valid VistA Provider authorization to write the drug schedule.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/010.png)

Drug Accept Validation eRx VistA Provider Not Authorized Block Message

CS NOTE: The following block message displays upon selecting an eR<sub>X</sub> that is written/issued after the VistA Provider’s DEA expiration date.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/011.png)

Drug Accept Validation eRx VistA Provider Not Authorized Block Message

The Status changes to “VALIDATED” on the Drug Validation screen, along with the user who performed the validation and date/time stamp. “\[v\]” also displays to the right of the VistA Drug field on the Summary/Details screen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Drug Validation</strong> May 27, 2023@13:43:44 Page: 1 of 3</u></p>
<p>eRx Reference #: <strong>99999999</strong> eRx Patient: <strong>MBMONE,TESTONE TEST</strong></p>
<p>Date Written: <strong>10/18/23</strong> Effective Date: <strong>10/18/23</strong></p>
<p>Status: <strong>SUGG | VALIDATED by USER,USER on 10/19/23@13:43:36</strong></p>
<p><u>ERX MED | VISTA MED</u></p>
<p>Allergy: |Allergy:</p>
<p>NO ALLERGY INFORMATION RECEIVED | Verified:</p>
<p>| EGG PRODUCTS,PEANUTS</p>
<p>_______________________________________|________________________________________</p>
<p>Drug: <strong>ACETAMINOPHEN 325MG TAB</strong> |<u>1)</u>Drug: <strong>ACETAMINOPHEN 325MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; DU: INCREMENTS OF 100 ONLY</strong></p>
<p>| <strong>* TCGRx &amp; SCRIPTPRO *</strong></p>
<p>_______________________________________|________________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET PO EVERY FOUR HOURS</strong> | <strong>TAKE ONE TABLET PO EVERY FOUR HOURS AS</strong></p>
<p><strong>AS NEEDED</strong> | <strong>NEEDED</strong></p>
<p>_______________________________________|________________________________________</p>
<p>|<u>2)</u> Dosage: <strong>325 (MG)</strong></p>
<p>| Verb: <strong>TAKE</strong></p>
<p>|Disp. Units: <strong>1</strong></p>
<p>+ Enter ?? for more actions</p>
<p>P Print H Hold UH Un Hold</p>
<p>E Edit AV Accept Validation</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug / SIG Validation Complete (Validate Drug / SIG Screen)

The modified VistA Drug/SIG information populates on the Drug/SIG Validation screen.

Press \<Enter\> to display Pages 2 and 3 of the Drug/SIG Validation screen.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 15, 2024@09:54:39 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>TEST,PATIENT</strong> eRx Reference #: <strong>99999999</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>06/17/24</strong></p>
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
</tbody>
</table>
<p><strong><u>PATIENT AUTO-MATCHED | VALIDATED by USER,NAME on 6/17/24@16:23:30 _</u></strong></p>
<p>Name: TEST,PATIENT |Name: TEST,PATIENT</p>
<p>DOB : JUL 99, 9999 SSN : <strong>66613456</strong> |DOB : JUL 99, 9999 SSN : <strong>666-13-4567</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017 <strong><u>PROVIDER AUTO-MATCHED | VALIDATED by PSOAPPLICATIONPROXY on 6/17/24@16:10 __</u></strong></p>
<p>Name: <strong>TEST,PROVIDER</strong> |Name: <strong>TEST,PROVIDER</strong></p>
<p>NPI : <strong>1234567890</strong> Phone: |NPI : <strong>1234567890</strong> Phone: (888) 888-8888</p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong> DEA EXP: <strong>02/01/31</strong></p>
<p>Clinic: <strong>CLINIC NAME</strong> |Class:</p>
<p><strong><u>DRUG/SIG SUGGESTED | VALIDATED by USER,NAME on 6/17/24@16:23:30 _</u></strong></p>
<p>Drug: <strong>MELOXICAM 7.5MG TAB</strong> | <u>1)</u>Drug: <strong>MELOXICAM 7.5MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>|</p>
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
<p>P VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Drug / SIG Validation Complete (Summary/Details Screen)

#### Wait Status Flag “W”

When the user completes validating Patient, Provider and Drug/SIG for an eR<sub>X</sub>, the status of the prescription changes from “I” In Process to “W” Wait in the Holding Queue’s list view.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 15, 2024@09:54:39 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>TEST,PATIENT</strong> eRx Reference #: <strong>99999999</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>06/17/24</strong></p>
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
</tbody>
</table>
<p><strong><u>PATIENT AUTO-MATCHED | VALIDATED by USER,NAME on 6/17/24@16:23:30 _</u></strong></p>
<p>Name: <strong>TEST,PATIENT</strong> |Name: <strong>TEST,PATIENT</strong></p>
<p>DOB : <strong>JUL 99, 9999</strong> SSN : <strong>66613456</strong> |DOB : <strong>JUL 99, 9999</strong> SSN : <strong>666-13-4567</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017 <strong><u>PROVIDER AUTO-MATCHED | VALIDATED by PSOAPPLICATIONPROXY on 6/17/24@16:10 __</u></strong></p>
<p>Name: <strong>TEST,PROVIDER</strong> |Name: <strong>TEST,PROVIDER</strong></p>
<p>NPI : <strong>1234567890</strong> Phone: |NPI : <strong>1234567890</strong> Phone: (888) 888-8888</p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong> DEA EXP: <strong>02/01/31</strong></p>
<p>Clinic: <strong>CLINIC NAME</strong> |Class:</p>
<p><strong><u>DRUG DRUG/SIG SUGGESTED | VALIDATED by USER,NAME on 6/17/24@16:23:30 _</u></strong></p>
<p>Drug: <strong>MELOXICAM 7.5MG TAB</strong> | <u>1)</u>Drug: <strong>MELOXICAM 7.5MG TAB</strong></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM (2/10)</strong></p>
<p>|</p>
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
<p>P VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eR<sub>X</sub> Holding Queue Summary/Details Screen with Validations Complete

“W” can now be seen in the status column.

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
<p>1. XXXXXXXXXXX,XXXXXXXX 07/10/33 ACETAMINOPHEN 325MG TA XXXXXXX,XXX W 10/04/23</p>
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

eR<sub>X</sub> Holding Queue List View with eR<sub>X</sub> Record in “W” Status

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

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen// AC Validate &amp; Accept eRx</p>
<p>Patient has not been validated!</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p>Validating Provider...</p>
<p>Vista provider has not been matched. Cannot manually validate.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p>
<p>Validating Drug/SIG...</p>
<p>Vista drug has not been matched. Cannot manually validate.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRX - Sample Validation Errors

After all the above preconditions have been met, to Accept an eR<sub>X</sub> \<AC\> from the Summary/Details screen, complete the following steps.

From the Summary/Details screen, type \<AC\> Accept eR<sub>X</sub>.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen// AC Validate &amp; Accept eRx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Accept eRXes

A message displays notifying the user that the eR<sub>X</sub> was sent to Pending Outpatient Orders for further processing.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/012.png)

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

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/013.png)

Rejecting an eR<sub>X</sub>

Once the eR<sub>X</sub> is rejected, the details of the reject message are available in the IEP Processing Hub as reference. Error! Reference source not found.![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/014.png)

Reject Message in Processing Hub

## Do Not Fill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a record contains a value of ‘E’, the following message will display to inform the user that this is a DO NOT FILL record per the Provider.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> May 27, 2025@16:34:25 Page: 1 of 3</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2025052200002</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> ERX HAS DO NOT FILL INDICATOR PER PROVIDER</p>
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
</tbody>
</table>
<p><u>PATIENT AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21</u></p>
<p>Name: <strong>XXXXXXXXX,XXXXXXXX</strong> |Name: <strong>XXXXXXXXX,XXXXXXXX</strong></p>
<p>DOB : <strong>XXX 01, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>XXX 1,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: 555-555-55555 |Phone: 555-555-5555</p>
<p><strong>STREET ADDRESS LNE1 STREET ARL...76017</strong>| <strong>STREET ADDRESS LNE1 STREET ARL...76017</strong></p>
<p><u>PROVIDER AUTO-MATCHED | VALIDATED by USER,USER on 3/13/25@17:21:52</u></p>
<p>Name: <strong>YYYYYYYYY,YYYYYYY</strong> |Name: <strong>YYYYYYYYY,YYYYYYY</strong></p>
<p>NPI : <strong>9999999999</strong> Phone: |NPI : <strong>9999999999</strong> Phone: <strong>(222) 222-2222</strong></p>
<p>DEA : <strong>XX99999999</strong> |DEA :</p>
<p>Clinic: <strong>EXTERNAL PHARMACY</strong> |Class: <strong>PHYSICIAN</strong></p>
<p><u>DRUG/SIG SUGGESTED | VALIDATED by USER,USER on 3/13/25@17:29:10</u></p>
<p>Drug: LEVOTHYROXINE NA (SYNTHROID) 50MC|<u>1)</u>Drug: LEVOTHYROXINE NA (SYNTHROID) 300</p>
<p>G TAB | MCG TAB</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; VA STND DRUG</strong></p>
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
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

eRx has Do Not Fill Indicator Per Provider

The user will be prompted to select REMOVE or REJECT actions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
<p>Select Item(s): Next Screen// H Hold</p>
<p>This is a DO NOT FILL record. The only actions available are REMOVE or REJECT.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Do Not Fill Error Message

## Printing in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Single eRx View/Display screen and from any of the validate screens, the \<P\> Print action is available to print the eR<sub>X</sub>. \<P\> Print action is available for all records in the Holding Queue.

1.  Enter \<P\> Print.
2.  Enter the Device (local or network printer) and press \<Enter\>.

The print display of the eR<sub>X</sub> prints to the selected printer.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PHARMACY INFORMATION</p>
<p>CHEYENNE VAM ROC</p>
<p>Address: P.O. BOX 20350</p>
<p>CHEYENNE, WYOMING 820037008</p>
<p>Primary Phone: 3077787524 NCPDP: 5203651</p>
<p>*PRESCRIBER INFORMATION*</p>
<p>Name: TEST,PROVIDER</p>
<p>Address: 123 FAKE FOREST ST</p>
<p>APT 9999</p>
<p>NEW YORK, NEW YORK 99999</p>
<p>NPI: 1234567890 DEA: XX9999999 State Lic:</p>
<p>Primary Phone: Fax:</p>
<p>PATIENT INFORMATION*</p>
<p>Name: TEST,PATIENT</p>
<p>DOB: XXX 99, 9999 Sex: MALE Primary Phone: 999-999-9999 SSN: 999999999</p>
<p>Address: 9999 FAKE AVE</p>
<p>CITYNAME, NEW YORK 99999</p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>PRESCRIPTION INFORMATION</p>
<p>eRx Drug: MELOXICAM 7.5MG TAB</p>
<p>NDC: 00378106601 Written Date: JUN 17, 2024 Issue Date:</p>
<p>Qty: 30 Days Supply: 30 Refills: 11</p>
<p>Code List Qualifier: Original Quantity</p>
<p>Drug Form: Tablet</p>
<p>Strength: 7.5MG</p>
<p>Substitutions?: YES Prohibit Renewals: No</p>
<p>eRx Sig:</p>
<p>Take two tabs by mouth daily</p>
<p>Provider Comments: Provider Notes for Patient 5</p>
<p>*PRESCRIBER DRUG USE EVALUATION*</p>
<p>Co-Agent: Nsaids (Non-Steroidal Anti-Inflammatory Drug)</p>
<p>Reason: Drug-Allergy</p>
<p>Result: Prescribed w/ acknowledgements</p>
<p>Override: Previously Tolerated</p>
<p>*DIAGNOSIS INFORMATION</p>
<p>Primary Dx:</p>
<p>ICD-10 A99.99 INFLAMATION OF JOINTS</p>
<p>CHRONIC JOINT INFLAMATION</p>
<p>eRx Reference #: 123075 Message ID: 442.123454.3230617.16044</p>
<p>*END OF eRx*</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Print Display of an eRx

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

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/015.png)

Select Hold Reason Code

The Hold Status, Hold Reason, and the user placing the eR<sub>X</sub> on hold display below the VistA Drug section on the Summary/Details screen.

![](pharmacy-reengineering-pre-inbound-eprescribing-iep-user-guide-version-5-0-unit-/016.png)

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
<p>H Hold RM Remove eRx AC Validate &amp; Accept eRx</p>
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

## Un Hold eR<sub>X</sub> in the eR<sub>X</sub> Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

eR<sub>X</sub> may be removed from a hold by typing \<UH\> Un Hold. Users who see the Un Hold function in parentheses “()” are not able to remove an eR<sub>X</sub> from a hold.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// UH UH</p>
<p>Additional Comments (Optional): TEST</p>
<p>A change request has been generated for this NewRx record.</p>
<p>Are you sure you like to unhold this prescription?</p>
<p>Enter Yes or No: Y// ES</p>
<p>eRx removed from hold status, and moved to 'Wait'.</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Un Hold ErxNOTE: When a user exercises Un Hold option on a NewR<sub>X</sub> record that is in one of the Hold statuses, if all the 3 validations (Patient, Provider, and Drug/SIG) are complete, the eR<sub>X</sub> record’s status changes to “W” (Wait). When a user exercises Un Hold option on a NewR<sub>X</sub> record that is in one of the Hold statuses, if all the 3 validations (Patient, Provider, and Drug/SIG) are not complete, the eR<sub>X</sub> record’s status changes to “I” (In Process).

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
- REM92 - Other
- REM09 - ERX Issue not resolved - Provider contacted
- REM81 - Prior Authorization Denied
- REM82 - No Community Care Authorization for this Prescription
- REM83 - Patient Not Found in Local VA Database

  Type additional comments as to why the eR<sub>X</sub> is being removed and press \<Enter\>. These comments are optional.

Once the eR<sub>X</sub> is removed, the status changes to “RM” and it no longer displays in the default Holding Queue List; however, the eR<sub>X</sub> can be accessed via the search action from the main Holding Queue List screen using one or more of the search criteria.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// RM Remove eRx</p>
<p>Select REMOVAL reason code: REM82 No Community Care Authorization for this</p>
<p>Prescription</p>
<p>Additional Comments (Optional): For User Manual Updates</p>
<p>Would you like to 'Remove' eRx #2025010620? Y// ES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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
<p>DOB : <strong>XXX 99,9999</strong> SSN : <strong>9999999999</strong> |DOB : <strong>XXX 99,9999</strong> SSN : <strong>9999999999</strong></p>
<p>Phone: |Phone: 555-2222</p>
<p><strong>72017 LAKE TAHOE DIRECTORY DR ...76016</strong>| <strong>72017 LAKE TAHOE DIRECTORY DR ...76016</strong></p>
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
<p>NPI : <strong>1234567890</strong> Phone: |NPI : <strong>1234567890</strong> Phone: (888) 888-8888</p>
<p>DEA : |DEA :</p>
<p>Clinic: <strong>TEST NAME</strong> |Class:</p>
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
<p>Drug: IBUPROFEN |<u>1)</u>Drug: IBERET-FOLIC-500 TAB</p>
<p>Substitution? Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; TAB (100/BT ONLY)</strong></p>
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
<p>SEX: MALE</p>
<p>CrCL: &lt;Not Found&gt; (CREAT: Not Found) BSA (m2): _______</p>
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
<p>| <strong>ALLEGRA, LANSOPRAZOLE CRITERIA MET-2-23</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Allergy: |Allergy:</p>
<p><mark>NO ALLERGY INFORMATION RECEIVED</mark> | Verified:</p>
<p>| <mark>ALBUTEROL</mark>,<mark>EGG PRODUCTS</mark>,<mark>HONEY</mark></p>
<p>| <mark>IBUPROFEN</mark>,<mark>PEANUTS</mark>,<mark>PERCODAN</mark></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>PROVIDER AUTO-MATCHED | VALIDATED by PSOAPPLICATIONPROXY on 9/20/23@11:44:29</u></strong></p>
<p>Name: <strong>XXXXXXXX,XXXXXX</strong> |Name: <strong>XXXXXXXX,XXXXXX</strong></p>
<p>NPI : <strong>9999999999</strong> Phone: |NPI : <strong>9999999999</strong> Phone: <strong>(888) 888-8888</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>Clinic: <strong>TEST CLINIC</strong> |Class: <strong>NURSE PRACTITIONER</strong> _______________________________________|________________________________________</p>
<p><strong><u>DRUG/SIG SUGGESTED | VALIDATED by XXXXX,XXXXXXX on 9/20/23@11:48:05</u></strong></p>
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
<p>Reason: Drug-Allergy | <strong>WITH FOOD FOR PAIN/INFLAMMATION</strong></p>
<p>Result: Prescribed w/ acknowledgements |Indications:</p>
<p>Acknowledgement: Previously Tolerated | <strong>TEST</strong></p>
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

#### eRx Pending Order Suggested Fill Date Auto Calculation

In most of the pending orders originated from the eRx Holding Queue (from outside prescribers) the Fill Date field is set to the current date. In some cases this is not ideal because the patient might still have enough medication to last a few more days and a future fill date, based on the last fill for the medication might be more appropriate. Therefore, using the logic below the software may suggest an alternative Fill Date in the future:

<u>Requirement</u>:

\- A previous prescription for the exact same drug must be found on the

patient's profile

\- The SIG from the previous prescription must match exactly with the

SIG for the new eRx Pending Order

<u>Suggested Future Fill Date determination</u>:

\- If the Last Fill in the in the existing prescription is released and the Release Date + Days Supply results in a future date, this calculated future date will be suggested as the Fill Date for the eRx Pending Order.

\- If the CMOP Transmission status for the Last Fill is TRANSMITTED or RE-TRANSMITTED, the Fill Date for the eRx Pending Order will be today's date + Days Supply for the Suspended fill.

\- If Last Fill is Suspended with a future Fill Date this future date will be suggested as the Fill Date for the eRx Pending Order.

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
<p>... |</p>
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
<p>Date Written: <strong>JUN 18, 2025</strong> |<u>1)</u> Issue Date: <strong>JUN 18,2025</strong></p>
<p>Effective Date: |<u>2)</u> Fill Date: <strong>JUL 18, 2025</strong></p>
<p>|Prior: <strong>99999999/R,04/18/25,Q:90,D:90</strong></p>
<p>_______________________________________|________________________________________</p>
<p>Days Supply: <mark>30</mark> |Days Supply: <mark>90</mark></p>
<p>_______________________________________|________________________________________</p>
<p>Quantity: <mark>30</mark> |QTY (TAB): <mark>90</mark></p>
<p>Dispense Unit: |</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> |QTY Dispense Message:</p>
<p>|</p>
<p>_______________________________________|________________________________________</p>
<p><strong>eRx Received on 06/18/25@11:44 | Accepted by XXXXXX,XXXXXXX on 06/18/25@10:30</strong></p>
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

Legend for Prior:

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 22%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>99999999/R,MM/DD/YY</strong></p>
<p>99999999 – Rx Number</p>
<p>R – Released</p>
<p>T – Transmitted to CMOP</p>
<p>S – Suspended</p>
<p>MM/DD/YY – Release Date (R);Date Transmitted to CMOP (T);Suspense/Fill Date (S)</p></th>
<th><p><strong>Q:999</strong></p>
<p>Q – Quantity</p></th>
<th><p><strong>D:999</strong></p>
<p>D – Days Supply</p></th>
</tr>
</thead>
<tbody>
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
<p>NPI : <strong>9999999999</strong> Phone: |NPI : <strong>9999999999</strong> Phone: <strong>(888) 888-8888</strong></p>
<p>DEA : <strong>XX9999999</strong> |DEA : <strong>XX9999999</strong></p>
<p>Clinic: <strong>TEST CLINIC</strong> |Class: <strong>NURSE PRACTITIONER</strong></p>
<p>_______________________________________|________________________________________</p>
<p><strong><u>DRUG/SIG SUGGESTED/VALIDATED (RENEWAL)</u>_______________</strong></p>
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

Users can jump to eRx Single Patient Queue from the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option. It will be available in the Patient Information screen as well as in the Medication Profile screen. This action include all variations of the eRx Patient that are matched to the same VistA Patient. The user will now be taken to the eRx Medication Queue with the VistA Patient filter automatically set with the patient that was selected in Backdoor Pharmacy. Therefore, the list items will include all eRx's from all eRx Patients that have been matched to the VistA Patient.

The option will work independently if the patient has an actionable eRx or not. However, the patient must have had at least one eRx received in the past.

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
<th><p><u><strong>eRx Medication Queue</strong> May 28, 2025@09:00:17 Page: 1 of 1</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>FILTERED BY: <strong>PATIENT(TEST,PATIENTONE TEST)</strong></p>
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
<p>1. TEST,PATIENTONE T 03/01/70 IBUPROFEN 200MG TAB YYYYY,PROVI HFF 01/06/25</p>
<p>2. TEST,PATIENTONE T 03/01/70 ROSUVASTATIN CA 40MG YYYYY,PROVI PR 01/06/25</p>
<p>3. TEST,PATIENTONE T 03/01/70 LISINOPRIL 20MG TAB YYYYY,PROVI I 01/06/25</p>
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
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>