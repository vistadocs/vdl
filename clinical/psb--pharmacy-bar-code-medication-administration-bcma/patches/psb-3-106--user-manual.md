---
title: BCMA Version 3 Pharmacy CHUI User Manual (PSB*3*106)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Pharmacy CHUI  (PSB*3*106)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*106
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 2
description: - [Revision History](#revision-history) - [# INTRODUCTION](#introduction) - [What is BCMA?](#what-is-bcma) - [Features of BCMA](#features-of-bcma) - [# About This Manual](#about-this-manual) - [Special Notations—Documentation Conventions](#special-notationsdocumentation-conventions) - [Package Conve
audience: 
keywords: 
  - report
  - medication
  - prompt
  - press
  - pharmacy
  - dose
  - administration
  - bcma
  - patient
  - drug
page_count: 0
word_count: 7824
section_count: 22
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_0_P106_pharm_chui_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_0_P106_pharm_chui_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

PHARMACY CHUI USER MANUAL

February 2004

(Revised July 2021)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [# INTRODUCTION](#introduction)
  - [What is BCMA?](#what-is-bcma)
  - [Features of BCMA](#features-of-bcma)
  - [# About This Manual](#about-this-manual)
  - [Special Notations—Documentation Conventions](#special-notationsdocumentation-conventions)
  - [Package Conventions](#package-conventions)
  - [Intranet Documentation](#intranet-documentation)
  - [On-line Help](#on-line-help)
- [# BCMA Menu—Pharmacy Option](#bcma-menupharmacy-option)
  - [Using the Medication Administration Menu Pharmacy Option](#using-the-medication-administration-menu-pharmacy-option)
  - [Using ScreenMan Format to Request a Report](#using-screenman-format-to-request-a-report)
  - [Medication Administration Log Report](#medication-administration-log-report)
  - [Missed Medications Report](#missed-medications-report)
  - [Due List Report](#due-list-report)
  - [Medication Administration History (MAH) Report](#medication-administration-history-mah-report)
  - [Missing Dose Request](#missing-dose-request)
  - [Missing Dose Followup](#missing-dose-followup)
  - [Missing Dose Report](#missing-dose-report)
  - [Label Print](#label-print)
  - [Drug File Inquiry](#drug-file-inquiry)
  - [Bar Code Label Print](#bar-code-label-print)
  - [BCMA Drug IEN Synonym Check](#bcma-drug-ien-synonym-check)
  - [Report for Respiratory Therapy Medications](#report-for-respiratory-therapy-medications)
- [glossary](#glossary)
- [# INDEX](#index)
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2021</td>
<td><u>34b</u></td>
<td>PSB*3*106</td>
<td>Added an exhibit of <a href="#exhibit-26c-sample-unit-dose-bar-code-label-with-haz-information">a bar code label</a> for a drug that is Hazardous to Handle and Hazardous to Dispose.</td>
</tr>
<tr class="even">
<td>01/2019</td>
<td><a href="#PSB_103_Exhibit1ScreenChange"><u>5</u></a>, <a href="#report-for-respiratory-therapy-medications">35</a> - <a href="#Rep_for_Resp_Therapy_sectionend">36</a></td>
<td>PSB*3*103</td>
<td><p>Added Section 3.14 regarding the new Report for Respiratory Therapy Medications [PSB RPT RESP THERAPY MEDS] option. Updated Section 3.1 to reference the new option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/2018</td>
<td><a href="#PSB_3_100">21</a></td>
<td>PSB*3*100</td>
<td><p>Added note on selecting divisions at a multidivisional site for Missing Dose Followup.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2016</td>
<td><p>iii-iv, 5</p>
<p>34c, 42</p></td>
<td>PSB*3*88</td>
<td><p>Section 3.1 – Exhibit 1 screen updated</p>
<p>Section 3.13 – Added BCMA Drug IEN Synonym Check [PSB DRUG IEN CHECK] option</p></td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td>21</td>
<td>PSB*3*83</td>
<td><p>Removed <em>Missing Dose Request</em> option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/2008</td>
<td>iii-iv<br />
5, 31-32,<br />
34 a-b, 41</td>
<td>PSB*3*2</td>
<td><p>Section 3.1 – Exhibit 1 screen updated (p. 5).</p>
<p>Section 3.10 - References to Zebra printers restored (p. 31); sample barcode screens deleted (p. 32).</p>
<p>Section 3.12 added, references to “Dosage” changed to “Dose” and space between colon and dose measurement deleted (pp. 34 a-b).</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/2006</td>
<td><p>iv,</p>
<p>31- 32</p></td>
<td>PSB*3*2</td>
<td><p><strong><u>Note</u></strong>: The functionality listed below will be activated with the release of PSB*3*2.</p>
<p>– Updated Table of Exhibits to include Exhibits 22a and 22b. (p. iv)</p>
<p>– Updated Section 3.10, Label Print. Removed specific references to the Zebra printer to accommodate new feature to support multiple bar code printers, and updated instructions for creating a bar code label. Included new sample bar code label samples for Unit Dose and Ward Stock labels. (p. 31-32)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/2004</td>
<td>19, 20</td>
<td>PSB*3*5</td>
<td><p>– Updated the second paragraph to include the “Allergies” information.<br />
(p. 19)</p>
<p>– Updated the “Exhibit 12: Medication Administration History Report by Patient” to show the removal of the Reactions header and the inclusion of the ADRs header and the Allergies header. (p. 20)</p></td>
</tr>
<tr class="odd">
<td>02/2004</td>
<td></td>
<td></td>
<td>Original Released BCMA V. 3.0 Pharmacy CHUI User Manual.</td>
</tr>
</tbody>
</table>

# # INTRODUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is BCMA?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bar Code Medication Administration (BCMA) V. 3.0 software includes routines and files, Phase Release changes for BCMA V. 2.0, maintenance fixes, and enhancements. The enhancements are a direct result of feedback from the BCMA Workgroup and our many end users.

BCMA software is designed to improve the accuracy of the medication administration process. By automating this process, Department of Veterans Affairs Medical Centers (VAMCS) can expect enhanced patient safety and patient care.

As each patient wristband and medication is scanned with a bar code scanner, BCMA validates that the medication is ordered, timely, and in the correct dosage — as well as electronically updates the patient’s Medication Administration History (MAH) Report.

The electronic information provided by BCMA V. 3.0 improves the clinician’s ability to administer medications safely and effectively to patients on wards during their medication passes. It also helps to improve the daily communication that occurs between Nursing and Pharmacy staffs.

## Features of BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 provides the following features:

- Increases medication administration accuracy.
- Improves the efficiency of the medication administration process by capturing drug accountability data.
- Records Unit Dose, IV Push (IVP), IV Piggyback (IVPB), and large-volume IVs administered to patients.
- Provides the CPRS Med Order Button, a “link” to the Computerized Patient Record System (CPRS) for electronically ordering, documenting, reviewing, and signing verbal- and phone-type STAT and NOW (One-Time) orders for Unit Dose and IV medications already administered to patients.
- Increases the information available to nursing staff at the patient point of care.
- Reduces wasted medications.
- Improves communication between Nursing and Pharmacy staffs.
- Provides a real-time Virtual Due List (VDL) of orders for medication administration.
- Records missing doses and sends the requests electronically to the Pharmacy.
- Provides a point-of-care data entry/retrieval system.
- Provides full compatibility with the existing VistA system.
- Identifies Pro Re Nata (PRN) entries that require Effectiveness comments.
- Replaces the manual Medication Administration Record (MAR) with a Medication Administration History (MAH) to provide an automatic record of a patient’s medication administration information.
- Provides a list of variances that identify Early or Late medication administrations and late PRN Effectiveness entries.
- Provides the ability to document the patient’s pain score in BCMA and store it in the Vitals package.

## # About This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual contains a description of the Character-based User Interface (CHUI) BCMA options for the Pharmacy user. It is organized around the Medication Administration Menu Pharmacy Options. It explains how to access and use each option, and provides sample screen captures and reports. An Index and a Glossary are available at the back of this manual.

## Special Notations—Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Responses in boldface type indicate what you should type at your computer screen. Example: At the “Patient/Ward:” prompt, type P for Patient or W for Ward.

Text centered between arrows represents a keyboard key that needs to be pressed for the system to capture a user response or move the cursor to another prompt. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed. Example: Press \<Tab\> to move the cursor to the next prompt. Enter Y for Yes or N for No, and then press \<Enter\>.

- Indicates especially important or helpful information.

## Package Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Up-arrow (caret or a circumflex)

In CHUI BCMA, you can move back to a previous screen by entering a ^ and then pressing \<Enter\>. Repeat this process until you locate the desired screen.

## Intranet Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can locate this and other BCMA-related documentation on the Intranet, from the VA Software Document Library (VDL), at the following address. It provides background, technical information, and important user documentation.

<http://www.va.gov/vdl>

\* Remember to bookmark this site for future reference.

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

?, ??, ???  
On-line help is available by entering one, two, or three question marks at a prompt. One question mark elicits a brief statement of what information is appropriate for the prompt; two question marks elicits more help, plus the hidden actions shown above; and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

# # BCMA Menu—Pharmacy Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using the Medication Administration Menu Pharmacy Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA Pharmacy Option Menu, as illustrated in Exhibit 1, lets Pharmacy personnel access information that has been entered via the BCMA Graphical User Interface (GUI) VDL. Because BCMA operates in real time, scanned information is available as soon as the scan is successfully completed. You can access the Pharmacy Option Menu from any VistA-enabled terminal within the VAMC.

\* Several of these options are available under both the Nursing and the Pharmacy menu options. The options that are unique to Pharmacy include Missing Dose Followup, Missing Dose Report, Label Print, Barcode Label Print, BCMA Drug IEN Synonym Check, and Report for <span id="PSB_103_Exhibit1ScreenChange" class="anchor"></span>Respiratory Therapy Medications.

#### Exhibit 1: BCMA Pharmacy Option Menu Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/002.png)

To select a Pharmacy option:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, enter the number of the desired option.
2.  Press \<Enter\> to display the Sort Screen for the option chosen.

## Using ScreenMan Format to Request a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many of the Pharmacy options use a common screen to define selection criteria for reports, as illustrated in Exhibit 2, Report Request Using ScreenMan Format Screen. Other options use specific screens. This section explains the screen prompts for all reports using the Report Information Sort Screen and gives instructions for entering information. Following this section are sample reports that you can run from each of the Medication Administration Menu Pharmacy options.

#### Exhibit 2: Report Request Using ScreenMan Format Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/003.png)

Many of the reports can be sorted and printed in the following ways:

- By patient. The information will display chronologically.
- By ward. The system can sort the information by patient or room/bed, and display it chronologically within each patient.

To request a report using ScreenMan:

1.  At the “Start Date:” prompt, type the start date of the report, and then press \<Enter\>.  
    Note: The cursor moves to the next prompt each time that you press \<Enter\>.
- To display a list or a standard date and time format, enter a ? in any date or time prompt, and then press \<Enter\>.
2.  At the first “At:” prompt, type the start time of the report (in HHMM format), and then press \<Enter\>.
3.  At the “Stop Date:” prompt, type the stop date, and then press \<Enter\>.
4.  At the second “At:” prompt, type the stop time (in HHMM format), and then press \<Enter\>.
5.  At the “Run by Patient or Ward:” prompt, type P for Patient or W for Ward, and then press \<Enter\>.
- If you are sorting the report by ward, at the “Ward Location:” prompt, type the ward designation, and then press \<Enter\>. At the “Sort by Pt or Room-Bed:” prompt, type P for Patient or R for Room, and then press \<Enter\>.
- If you are sorting the report by patient, at the “Patient Name:” prompt, type the patient’s name or Social Security Number (SSN), and then press \<Enter\>.

\* To display a list or a standard format, enter a ? at any “Patient Name:” prompt, and then press \<Enter\>.

6.  At the “Include Comments:” prompt, enter Y for Yes or N for No, and then press \<Enter\>.

\* If a “Yes/No” prompt is blank, press \<Enter\> to respond No.

7.  At the “Include Audits:” prompt, enter Y for Yes or N for No, and then press \<Enter\>.
8.  At the “Print to Device:” prompt, type a valid printer, and then press \<Enter\>.
9.  At the “Queue to Run At:” prompt, press \<Enter\> to accept the date displayed, or enter a date and time, and then press \<Enter\>. The report will print at the time and date entered.
10. At the “\<RET\> Re-Edit:” prompt, press PF1 (or Num Lock), followed by E, to submit this report for printing. (Other available actions at this prompt are PF1-Q to Quit or PF1-R to refresh the screen.)

The screen clears and the following message displays:

> Submitting Your Report Request to Taskman…Submitted!

> Your Task Number Is: XXXX

- Depending on how your division is configured, either the PF1 key or Num Lock will be active. For consistency, this manual refers to the PF1 convention, but users are advised that PF1 is the same as Num Lock, if that is the active function at your VAMC.

## Medication Administration Log Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Medication Administration Log* \[PSBO ML\] option lets Pharmacy personnel print the Medication Administration Log Report, which displays detailed administration information for a specified date/time range. The report can be sorted and printed by patient or by ward, as illustrated in Exhibit 3. When printed by ward, you may sort the view by patient or room/bed. With this sort, the drug administration information will be printed chronologically within each patient.

The Medication Administration Log Report prints in a 132-column output. Exhibit 4, Medication Administration Log Report by Patient, and Exhibit 5, Medication Administration Log Report by Ward, show examples of both Medication Administration Log Reports.

- Throughout this manual, the reports shown are provided for illustrative purposes only. Actual reports may be longer.

To print a Medication Administration Log Report:

1\. At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 1, and then press \<Enter\> to access the *Medication Administration Log* \[PSBO ML\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Medication Administration Log Report.

#### Exhibit 3: Medication Administration Log Report Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/004.png)

#### Exhibit 4: Medication Administration Log Report by Patient

#### Exhibit 5: Medication Administration Log Report by Ward

## Missed Medications Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Missed Medication* \[PSBO MM\] option lets Pharmacy personnel print the Missed Medications Report, which includes Continuous and One-Time Unit Dose and IV Piggyback medications that were *not* administered to a patient during a medication pass. This report also includes patient demographics data, adverse drug reaction (ADR) information, ward/bed location, administration date/time, order number from Inpatient Medications V. 5.0, and the medication type of the missed medication. (Self-medications do *not* display on the report.) The report can be sorted and printed by ward or patient, and you can specify the date and time that the report covers, as illustrated in Exhibit 6.

- Information that may display on this report includes medications that were scheduled to be administered, but were *not* marked as Given, Held, or Refused. It may also include medications that have been renewed or expired shortly after the scheduled administration time, and medications requested from the Pharmacy as Missing Dose Requests. Medications placed “On Hold” and taken “Off Hold” via the Computerized Patient Record System (CPRS) or Inpatient Medications V. 5.0 will display on this report with the Hold information below the medication. The Hold information applies only to administrations due within the Hold timeframe.  
    
  The “Order Num” column on the report, shown in Exhibit 7, lists the actual order number and order type (i.e., Unit Dose or IV). This information is quite helpful when troubleshooting problem with BCMA.

To print a Missed Medications Report:

1\. At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 2, and then press \<Enter\> to access the *Missed Medications* \[PSBO MM\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Missed Medications Report.

The reports will print in a 132-column output. Exhibit 7, Missed Medications Report by Patient, and Exhibit 8, Missed Medications Report by Ward, show examples of both Missed Medications Reports.

- You should run the Missed Medications Report by Ward after each scheduled admin time to ensure that all entries listed on this report are resolved.

#### Exhibit 6: Missed Medications Report Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/005.png)

#### Exhibit 7: Medications Report By Patient

#### Exhibit 8: Missed Medications Report By Ward

## Due List Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Due List* \[PSBO DL\] option lets Pharmacy personnel display the Due List Report in CHUI BCMA, which displays the information available from the VDL within GUI BCMA. It provides detailed information about active and future Unit Dose and IV medication orders that are “due” for administering to a patient — during a timeframe that you specify — within a 24-hour period. Within the date/time range, the report may be printed by patient or by ward, and include the following:

- Continuous, PRN, On-Call, and One-Time Schedule Types
- Unit-Dose or IV medications
- Addendums

The Due List Report includes patient demographics data, ADR information, plus detailed information about an order, such as whether (or *not*) the medication is a self-med; the medication type, schedule, dose, and route; Special Instructions; administration times; Last Given date and time; Start/Stop date and time; and the individual(s) who verified the order.

\* Only medications active at the time the Due List is printed will display on the report. The printed Due List and the VDL within GUI BCMA may *not* match if orders have been added, discontinued, or renewed after printing.

Complete the steps on the next page to enter information on the screen illustrated in Exhibit 9, Due List Report Request Screen.

#### Exhibit 9: Due List Report Request Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/006.png)  
To Print a Due List Report:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 3, and then press \<Enter\> to access the *Due List* \[PSBO DL\] option.
2.  At the “Start Date:” prompt, type the date, and then press \<Enter\>.
3.  At the “Start Time:” prompt, type the time, and then press \<Enter\>.
4.  At the “Stop Time:” prompt, type a date, and then press \<Enter\>.
5.  At the “Run by Patient or Ward:” prompt, type P for Patient or W for Ward, and then press \<Enter\>.
- If you are sorting the report by patient, at the “Patient Name:” prompt, type the patient's name or SSN, and then press \<Enter\>.
- If you are sorting the report by ward, in the ward location, type the ward designation, and then press \<Enter\>. At the “Sort by Pt or Room-Bed:” prompt, type P for Patient or R for Room/Bed, and then press \<Enter\>.
6.  At the “Include Schedule:” prompts, enter Y for Yes for the desired Schedule Type(s) and N for No the others and, then press \<Enter\>.
7.  At the “Include Order Types:” prompts, enter Y for Yes or N for No at the “IV:” prompt and “Unit Dose:” prompt, and then press \<Enter\>. If you enter N for No at both prompts, no orders will print on the report.
8.  At the “Include Addendums:” prompt, enter Y for Yes or N for No, and then press \<Enter\>. When Y is entered, an additional section called Changes/Addendums to Orders will print at the bottom of the report. You can use this section of the report to manually record information about a medication administration.
9.  At the “Print to Device:” prompt, type the desired printer, and then press \<Enter\>.
10. At the “Queue to Run At:” prompt, type the date you want to run a report, and then press \<Enter\>. If you press \<Enter\>, the system defaults to the current date and time.
11. At the “\<Ret\> Re-Edit:” prompt, press the PF1 key followed by E (Exit) to submit the request for printing. (Other available actions at this prompt are PF1 - Q to Quit, or PF1-R to refresh the screen.)

The screen clears and the following message displays:

> Submitting Your Report Request to Taskman…Submitted!

> Your Task Number Is: XXXX

The reports will print in a 132-column output. Exhibit 10, Due List Report by Patient, and  
Exhibit 11 Due List Report by Ward, show examples of both Due List Reports.

#### Exhibit 10: Due List Report by Patient

#### Exhibit 11: Due List Report by Ward

## Medication Administration History (MAH) Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Medication Administration History* (MAH) \[PSBO MH\] option lets Pharmacy personnel print an MAH Report for Unit Dose and IV medication orders. This report lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (\*\*\*) to indicate that a medication was not due. This information is also noted in the Legend at the bottom of the MAH Report.

An MAH Report also includes patient demographics data, allergies and ADR information, plus detailed information about the order, such as the drug/additive/solution; the medication schedule, dose, route, and injection site; the actual administration times; the name and initials of the clinician who administered the medication; and the individuals who verified the order. It also includes information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.

- If no parameter is defined in CPRS, the maximum date range defaults to a seven-date range. For example, a report would list the Sunday proceeding, and the Saturday following, the date that you selected for the report.
- When a student nurse is administering medications under the supervision of an instructor, and both individuals hold the appropriate security keys (i.e., PSB STUDENT and PSB INSTRUCTOR), an asterisk prints next to the student’s initials on the MAH. A legend prints at the bottom of the MAH to indicate the date/time the medication was given, along with the names of the student and the instructor.

To print an MAH Report:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 4, and then press \<Enter\> to access the *Medication Administration History (MAH)* \[PSBO MH\] option.
2.  See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting an MAH Report. Exhibit 12, MAH Report by Patient, shows an example of the MAH Report.

#### Exhibit 12: Medication Administration History Report by Patient

## Missing Dose Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Missing Dose Request* \[PSB MISING DOSE REQUEST\] option was removed by patch PSB\*3\*70.

## Missing Dose Followup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Missing Dose Followup* \[PSB MISSING DOSE FOLLOWUP\] option lets Pharmacy personnel electronically respond to a Missing Dose Request submitted by nursing using the VDL in GUI BCMA. Pharmacy can enter a reason that the dose was missing, the time the dose was delivered, and the name of the individual who delivered the dose.

To create a Missing Dose follow-up message:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 6, and then press \<Enter\> to access the *Missing Dose Followup* \[PSB MISSING DOSE FOLLOWUP\] option. The Missing Dose Request Screen, and the prompts you will complete, is shown in Exhibit 16.

> **NOTE:** <span id="PSB_3_100" class="anchor"></span> If your site is defined as multidivisional in the MAS PARAMETER (#43) file, then you will be prompted to select one or all divisions at your site. If you enter “O” (One) at the “Do you want ‘A’ll Divisions or just ‘O’ne Division:” prompt, then VistA displays the “Select Division:” prompt with your login division as the default. You can accept the default or enter “?” to choose from a list of site divisions. After you select a division, the system displays missing dose requests for that division on the screen below, and the division name is shown in the screen heading. If you select all divisions, then requests will be shown for all divisions at your site.

2.  At the “Select Missing Dose Request \# (\<RET\> to continue, ‘^’ to quit): (1-7):” prompt, type the number opposite the Missing Dose that you want to create a follow-up message for, and then press \<Enter\>. The Missing Dose Request Pharmacy Follow-up Information Screen, shown in Exhibit 17, then displays.

#### Exhibit 16: Missing Dose Followup Request Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/007.png)

#### Exhibit 17: Missing Dose Request Pharmacy Follow-up Information Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/008.png)

3.  At the “Dose Delivered:” prompt, enter Y for Yes, and then press \<Enter\>. If a medication is no longer active or will *not* be delivered, enter N for No at this prompt.
- There may be instances where a missing dose is requested for an item that is no longer active. If the medication is no longer an active order or will *not* be delivered, enter N for No at this prompt.
4.  At the “Delivery Date/Time:” prompt, enter N (for Now) or the date and time that the dose was delivered, and then press \<Enter\>.
5.  At the “Pharmacy Reason Needed:” prompt, type the number that corresponds to your selection in Exhibit 18 Pharmacy Reasons Needed Selection Table.

#### Exhibit 18: Pharmacy Reasons Needed Selection Table

| 1   | WS/FILL ON REQUEST        |
|-----|---------------------------|
| 2   | FOUND IN DRAWER           |
| 3   | PHARMACIST ERROR          |
| 4   | EXPIRED/NO ORDER          |
| 5   | ATC ERROR                 |
| 6   | NOT ENOUGH PRNS           |
| 7   | TECHNICIAN ERROR          |
| 8   | ON PRE-EXCHANGE/PICK LIST |
| 9   | PATIENT TRANSFERRED       |
| 10  | NURSE ADMIN ERROR         |

6.  At the “COMMAND:” prompt, perform one of the following actions:
- Type S, and then press \<Enter\> to save the information that you entered for the Missing Dose Request selected.
- Type E, and then press \<Enter\> to exit the Followup Information Screen.
- Type R, and then press \<Enter\> to refresh the Followup Information Screen.
- If you try to exit the screen without saving the data, the system displays the “Save changes before leaving form (Y/N)?” prompt. Enter N for No, or Y for Yes, and then press \<Enter\>. The system confirms that the data has been saved, and returns you to the “Select Bar Code Medication Administration Manager Option:” prompt.

## Missing Dose Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Missing Dose Report* \[PSBO MD\] option provides information about Missing Doses that were submitted by a ward or for all wards. This report displays the total number of Missing Doses submitted for each ward location selected, the dispense drug requested, and the total number of Missing Dose Requests submitted for the dispensed drug within the selected date range.

To print a Missing Dose Report:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 7, and then press \<Enter\> to access the *Missing Dose Report* \[PSBO MD\] option. The Missing Dose Report Request Screen will display, as shown in Exhibit 19.
2.  At the “Start Date:” prompt, type the start date of the report, and then press \<Enter\>. The Missing Dose Request Pharmacy Follow-up Information Screen then displays. Note: The cursor moves to the next prompt each time that you press \<Enter\>.

\* To display a list or a standard date and time format, enter a ? in any date or time prompt, and then press \<Enter\>.

#### Exhibit 19: Missing Dose Report Request Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/009.png)

3.  At the first “At:” prompt, type the start time of the report (in HHMM format), and then press \<Enter\>.
4.  At the “Stop Date:” prompt, type the stop date, and then press \<Enter\>.
5.  At the second “At:” prompt, type the stop time (in HHMM format), and then press \<Enter\>.
6.  At the “Ward (Return for ALL):” prompt, press \<Enter\> to display a list of all wards, or enter the ward for which you want to run a report.
7.  At the “Print to DEVICE:” prompt, type a valid printer, and then press \<Enter\>.
8.  At the “Queue to Run At:” prompt, press \<Enter\> to accept the date displayed, or enter a date and time, and then press \<Enter\>. The report will print at the time and date entered.
9.  At the “\<RET\> Re-Edit:” prompt, press PF1 (or Num Lock), followed by E, to submit this report for printing. (Other available actions at this prompt are PF1-Q to Quit or PF1-R to refresh the screen.)
- Depending on how your division is configured, either the PF1 key or Num Lock will be active. For consistency, this manual refers to the PF1 convention, but users are advised that PF1 is the same as Num Lock, if that is the active function at their VAMC.

The screen clears and the following message displays:

> Submitting Your Report Request to Taskman…Submitted!

> Your Task Number Is: XXXX

A sample report is shown in Exhibit 20, Missing Dose Report.

#### #### Exhibit 20: Missing Dose Report

## Label Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *Label Print* \[PSBO BL\] option for printing individual or batch Unit Dose bar code labels. It is specifically coded to the Zebra-brand printers using the Zebra Programming Language (ZPL). Model 105SE was used in the development of the labels. Routine \[PSBOBL\] uses site-specific printers or terminals to produce labels.

#### Exhibit 21: Bar Code Label Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/010.png)

To create bar code labels:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 8, and then press \<Enter\> to access the *Label Print* \[PSBO BL\] option. The Bar Code Label Screen will display, as shown in Exhibit 21.
2.  At the “Drug Name:” prompt, enter the drug name and then press \<Enter\>.
3.  At the “Lot \#:” prompt, enter the Lot \#, and then press \<Enter\>.
4.  At the “Expiration Date:” prompt, enter a date, and then press \<Enter\>.
5.  At the “Manufacturer:” prompt, enter the manufacturer's name, and then press \<Enter\>.
6.  At the “Quantity:” prompt, enter a quantity between 0.25 and 9999 (up to two decimal places), and then press \<Enter\>.
7.  At the “Filled By:” prompt, type the initials of the person who filled the order, and then press \<Enter\>.
- If it is unknown, leave the field blank by pressing \<Enter\>. This will provide space for another individual to initial the label at a later time.
8.  At the “Checked By:” prompt, type the initials of the person who will check the order, and then press \<Enter\>.
- If it is unknown, leave the field blank by pressing \<Enter\>. This will provide space for another individual to initial the label at a later time.
9.  At the “# Labels:” prompt, type the number of labels needed between 1 and 999, and then press \<Enter\>.
10. At the “Patient Name:” prompt, type the patient’s name, and then press \<Enter\>.
- If preparing a Ward Stock label, leave the field blank by pressing \<Enter\>.
11. At the “Dosage:” prompt, enter a dosage and then press \<Enter\>.
- The “Dosage:” prompt will accept entries from two to 30 alpha/numeric characters.
12. At the “Print to Device:” prompt, type the bar code printer assigned to the ward, and then press \<Enter\>.
13. At the “Queue to Run:” prompt, enter a date and time, and then press \<Enter\>.
14. At the “\<RET\> Re-Edit:” prompt, press PF1 - E to print the label, PF1 - Q to Quit or PF1 - R to refresh the screen.

## Drug File Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Drug File Inquiry* \[PSB DRUG INQUIRY\] option lets Pharmacy personnel check the bar-coded Internal Entry Number (IEN) Code listed on dispensed Unit Dose medications. This is particularly useful in helping resolve discrepancies when the incorrect bar code is affixed to a medication.

On a medication bar code, the IEN appears on the first line next to the Drug name. Any additional synonyms loaded into Pharmacy Data Management V. 1.0 also appear under the Synonym heading of this option.

To run a drug file inquiry:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 9, and then press \<Enter\> to access the *Drug File Inquiry* \[PSB DRUG INQUIRY\] option.
2.  At the “Select DRUG:” prompt, as shown in Exhibit 23, Drug File Inquiry Screen 1, type the name and dosage of the drug, and then press \<Enter\>.
- You can display a list or a standard format by entering a ? at the “Select DRUG:” prompt, and then pressing \<Enter\>. The Drug File information will display, as illustrated in Exhibit 24, Drug File Inquiry Screen 2.

#### Exhibit 23: Drug File Inquiry Screen 1

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/011.png)

#### Exhibit 24: Drug File Inquiry Screen 2

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/012.png)

- The IEN displays on the first line, to the right of the Drug Name. The IEN is unique to this drug file entry. In most cases, it is the bar-coded number on the Unit Dose packages that are created in the Pharmacy. Manufacturers’ National Drug Code (NDC) bar codes may display at the “SYNONYMS:” prompt of this display. If the drug is Non-Formulary (N/F), the “Non-Formulary:” prompt will be set to N/F.

## Bar Code Label Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *Barcode Label Print* \[PSBO BZ\] option for printing individual or batch Unit Dose bar code labels. This option allows the user to have the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBZ uses site-specific printers or terminals to produce labels.

#### Exhibit 25: Bar Code Label Print Screen

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/013.png)

To print bar code labels:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 10, and then press \<Enter\> to access the *Barcode Label Print* \[PSBO BZ\] option. The Bar Code Label Print Screen will display, as shown in Exhibit 25.
2.  At the “Drug Name:” prompt, enter the drug name and then press \<Enter\>.
3.  At the “Lot \#:” prompt, enter the Lot \#, and then press \<Enter\>.
4.  At the “Expiration Date:” prompt, enter a date, and then press \<Enter\>.
5.  At the “Manufacturer:” prompt, enter the manufacturer's name, and then press \<Enter\>.
6.  At the “Quantity:” prompt, enter a quantity between 0.25 and 9999 (up to two decimal places), and then press \<Enter\>.
7.  At the “Filled By:” prompt, type the initials of the person who filled the order, and then press \<Enter\>.
- If it is unknown, leave the field blank by pressing \<Enter\>. This will provide space for another individual to initial the label at a later time.
8.  At the “Checked By:” prompt, type the initials of the person who will check the order, and then press \<Enter\>.
9.  If it is unknown, leave the field blank by pressing \<Enter\>. This will provide space for another individual to initial the label at a later time.
10. At the “# Labels:” prompt, type the number of labels needed between 1 and 999, and then press \<Enter\>.
11. At the “Patient Name:” prompt, type the patient’s name, and then press \<Enter\>.
- If preparing a Ward Stock label, leave the field blank by pressing \<Enter\>.
12. At the “Dosage:” prompt, enter a dosage and then press \<Enter\>.
- The “Dosage” prompt will accept entries between 1-22 alphanumeric characters.
13. At the “Print to Device:” prompt, type the name of the bar code printer assigned to the ward, and then press \<Enter\>.
- To view all available printers, type a question mark (?) and then press \<Enter\>. Type the number of the printer and then press \<Enter\>. The printer name populates the field
14. At the “Queue to Run At:” prompt, enter a date and time, and then press \<Enter\>.

    At the “\<RET\> Re-Edit:” prompt, press PF1 - E to print the label, PF1 - Q to Quit or PF1 - R to refresh the screen. Sample labels are shown in the Exhibits below

#### Exhibit 26a: Sample Unit Dose Bar Code Label

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/014.png)

#### Exhibit 26b: Sample Ward Stock Bar Code Label

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/015.png)

#### Exhibit 26c: Sample Unit Dose Bar Code Label with \<\<HAZ\>\> Information

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/016.png)

## BCMA Drug IEN Synonym Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *BCMA Drug IEN Synonym Check* \[PSB DRUG IEN CHECK\] option checks a specific drug in the DRUG (#50) file by using its IEN to search for other entries that match or contain the IEN as its synonym.

#### Exhibit 27: BCMA Drug IEN Synonym Check 

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/017.png)

To run the BCMA Drug IEN Synonym Check option:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 11, and then press \<Enter\> to access the *BCMA Drug IEN Synonym Check* \[PSB DRUG IEN CHECK\] option. The “Scan Medication” prompt will display, as shown in Exhibit 27.
2.  At the “Scan Medication:” prompt, enter the Drug IEN and then press \<Enter \> OR scan the barcode.

## Report for Respiratory Therapy Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Report for Respiratory Therapy Medications* \[PSB RPT RESP THERAPY MEDS\] option enables Respiratory Therapists to generate the Respiratory Therapy Medications report, which identifies patients who need administration of orderable items that have been classified as Respiratory Therapy Drugs. These medications are classified in the Pharmacy Data Management package using the *Edit Orderable Items* \[PSS EDIT ORDERABLE ITEMS\] option. Refer to the *Pharmacy Data Management User Manual* for more information on classifying Respiratory Therapy Drugs.

The Respiratory Therapy Medications report lists the order number, patient name and location, medication name and dosage, and administration date and time, thus allowing Respiratory Therapists to easily locate each patient so that they can administer treatment at the appropriate time. Multi-divisional sites have the option to select a single division to include in the report, or to include all divisions.

> **NOTE:** PRN orders will not be displayed in the Respiratory Therapy Medications report, since PRN items do not have a defined administration time.

To run the Report for Respiratory Therapy Medications:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, type 12 and then press \<Enter\>.
2.  At the "Do you want (A)ll Divisions or just (O)ne Division: (A/O): O//" prompt, press \<Enter\> if you wish to generate the report for one division. You are prompted to select a division; the default response is the division to which you are assigned in the NEW PERSON file (#200).

> At a multi-divisional site, type A and then press \<Enter\> if you wish to generate the report for all divisions.

3.  At the "Select date of Respiratory Therapy Meds Report (e.g., T or T-1, etc.):" prompt, enter the date the report will cover and then press \<Enter\>.
4.  At the "DEVICE: //" prompt, type “q” and then press \<Enter\> to queue the report to print to a local printer, or just press \<Enter\> to print to the screen. If you choose to queue the report, type the printer name at the second “DEVICE: //” prompt and then press \<Enter\>. If you choose to print to the screen, the “RIGHT MARGIN: 80//” prompt displays. Type “132” and then press \<Enter\> for the report to display on the screen.

#### Exhibit 28: Report for Respiratory Therapy Medications Option

Select OPTION NAME: PSB PHARMACY       Medication Administration Menu Pharmacy

   1      Medication Administration Log

   2      Missed Medications (INPATIENT ONLY)

   3      Due List (INPATIENT ONLY)

   4      Medication Administration History (MAH)

   6      Missing Dose Followup

   7      Missing Dose Report

   8      Label Print

   9      Drug File Inquiry

   10     Barcode Label Print

   11     BCMA Drug IEN Synonym Check

   12     Report for Respiratory Therapy Medications

Select Medication Administration Menu Pharmacy \<TEST ACCOUNT\> Option: 12  Report

for Respiratory Therapy Medications

Report for Respiratory Therapy Medications

Do you want (A)ll Divisions or just (O)ne Division:  (A/O): O// ne Division

Select Division: CASPER// ?

    Answer with MEDICAL CENTER DIVISION NUM, or NAME, or FACILITY NUMBER, or

        TREATING SPECIALTY

   Choose from:

   1            CHEYENNE VAMROC     442

   2            CASPER     442GA

   3            FORT COLLINS     442GC

<span id="Rep_for_Resp_Therapy_sectionend" class="anchor"></span>   4            GREELEY     442GD

   5            SIDNEY     442GB

   6            CHEYENNE MOC     442HK

  

Select Division: CASPER//        442GA

Select date of Respiratory Therapy Meds Report (e.g., T or T-1, etc.): T  (JUN 12,

2018\)

Please choose a 132 character printer

Queuing of this report is recommended

DEVICE: //

#### Exhibit 29: Example Report for Respiratory Therapy Medications 

![](bcma-version-3-pharmacy-chui-user-manual-psb-3-106/018.png)

# glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains definitions for acronyms and terms used throughout this manual.

#### Acronyms

| ADR   | Adverse Drug Reaction.                                                       |
|-------|------------------------------------------------------------------------------------------|
| BCMA  | Bar Code Medication Administration.                                      |
| CHUI  | Character-based User Interface.                                              |
| CPRS  | Computerized Patient Record System.                                      |
| GUI   | Graphical User Interface.                                                    |
| IEN   | Internal Entry Number.                                                       |
| IV    | Intravenous.                                                                     |
| MAH   | Medication Administration History.                                           |
| MAR   | Medication Administration Record.                                            |
| N/F   | Non-formulary                                                                    |
| NDC   | National Drug Code.                                                          |
| PRN   | Pro Re Nata, or “as needed.”                                                 |
| VDL   | Virtual Due List.                                                            |
| VistA | Veterans Health Information Systems and Technology Architecture. |

#### Terms

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>ADR</th>
<th>Adverse Drug Reaction. Any response to a drug which is noxious and unintended, and which occurs at doses normally used in humans for treatment, diagnosis, or therapy of a disease, or for modifying physiological functions, including toxicity caused by overdose, drug interaction, drug abuse, drug withdrawal, significant failure of expected action, food-drug interaction, or allergy.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Administration History Report</td>
<td>A report in CPRS that lists the date, time, and orderable item of a medication highlighted on the CPRS Meds Tab. This report is called “Medication History Report” in BCMA.</td>
</tr>
<tr class="even">
<td>Audits</td>
<td>The process that tracks the activities of nurses administering medications, by recording selected types of events in the patient’s Medication Log.</td>
</tr>
<tr class="odd">
<td>BCMA</td>
<td>A VistA software application used in VAMCs for validating patient information and medications against active medication orders <em>before</em> being administered to a patient.</td>
</tr>
<tr class="even">
<td>Clinician</td>
<td>VAMC personnel who administer active medication orders to patients on a ward. In a VAMC, a number of teams may be assigned to take care of one ward, with specific rooms and beds assigned to each team.</td>
</tr>
<tr class="odd">
<td>Completed</td>
<td>This status for an IV bag indicates that the infusion has been completed, and the bag is being taken down or replaced with a new bag. No additional actions may be taken on a bag marked as “Completed,” other than to enter comments.</td>
</tr>
<tr class="even">
<td>Continuous Order</td>
<td>A medication given continuously to a patient for the life of the order, as defined by the order Start and Stop Date/Time.</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td>A VistA software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, managers, quality assurance staff, and researchers use this integrated record system.</td>
</tr>
<tr class="even">
<td>Dispensed Drug</td>
<td>A drug whose name has the strength associated with it (e.g., Acetaminophen 325 mg). The name without the strength is called the “Orderable Item Name.”</td>
</tr>
<tr class="odd">
<td>Due List Report</td>
<td>A report that provides detailed information about active <em>and</em> future Unit Dose and IV medication orders that are “due” for administering to a patient during a time frame that you specify within a 24-hour period.</td>
</tr>
<tr class="even">
<td>Given</td>
<td>When a medication is administered to a patient, it is considered to be “Given” and marked as such (with a “G”) in the Status column of the VDL.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface. The type of interface chosen for BCMA.</td>
</tr>
<tr class="even">
<td>Held</td>
<td>When a medication is not actually taken by a patient, it is considered to be “Held” and marked as such (with an “H”) in the Status column of the VDL. Reasons might include the patient being temporarily off the ward. You can select and mark multiple medications as Held on the VDL using the Right Click drop-down menu. In the case of IV bags, this status indicates that the dose was Held. The only actions available for this type of IV bag are to mark the bag as Infusing or Refused, or to submit a Missing Dose Request to the Pharmacy.</td>
</tr>
<tr class="odd">
<td>Hold</td>
<td>To display a medication order grayed out on the VDL until its Stop Date/Time or until it is Given. Some medical centers require that a nurse mark these order types as “Held,” although it is <em>not</em> necessary that they do so.</td>
</tr>
<tr class="even">
<td>IEN Code</td>
<td>The internal entry drug number entered by Pharmacy personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</td>
</tr>
<tr class="odd">
<td>IV</td>
<td>A medication given intravenously (within a vein) to a patient from an<br />
IV Bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</td>
</tr>
<tr class="even">
<td>MAH</td>
<td>A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</td>
</tr>
<tr class="odd">
<td>Medication Administration History Report</td>
<td>Also called “MAH,” A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</td>
</tr>
<tr class="even">
<td>Medication History Report</td>
<td>A report in BCMA that lists the date, time, and orderable item of a medication selected on the VDL. This report is called “Administration History Report” in CPRS.</td>
</tr>
<tr class="odd">
<td>Medication Log Report</td>
<td>Also called “Med Log,” a report that lists every action taken on a medication order within a specified 24-hour period. You can choose to include Comments and Audits performed on the patient’s medication orders.</td>
</tr>
<tr class="even">
<td>Missing Dose</td>
<td>A medication considered “Missing.” BCMA automatically marks this order type (with an “M”) in the Status column of the VDL after you submit a Missing Dose Request to the Pharmacy. If an IV bag displayed in the IV Bag Chronology display area of the VDL is <em>not</em> available for administration, you may mark the IV bag as a “Missing Dose” using the Missing Dose button or by right clicking the IV bag and selecting the Missing Dose command in the Right Click drop-down menu.</td>
</tr>
</tbody>
</table>
| Missed Medications Report     | A report that lists information about Continuous and One-Time Unit Dose and IV Piggyback medications that were *not* administered to a patient.                                                                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| National Drug Code            | Also called “NDC,” the number assigned by a manufacturer to each item/medication administered to a patient.                                                                                                                                                                                                                  |
| Not Given                     | The status that a scanned medication marked as “Given,” but *not* actually taken by a patient, is changed to on the VDL. The administration will display on the VDL as it appeared *before* it was marked as “Given.” BCMA notes the status change only in the Audit Trail section of the Medication Log (*not* on the VDL). |
| NOW Order                     | A medication order given ASAP to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.                                                                                                      |
| On-Call Order                 | A specific order or action dependent upon another order or action taking place *before* it is carried out. For example, “Cefazolin 1gm IVPB On Call to Operating Room.” Since it may be unkn when the patient will be taken to the operating room, the administration of the On-Call Cefazolin is dependent upon that event. |
| One-Time Order                | A medication order given one time to a patient such as a STAT or NOW a order. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time or until it is Given.                                                                                                         |
| Orderable Item                | A drug whose name does NOT have the strength associated with it (e.g., Acetaminophen 325 mg). The name with a strength is called the “Dispensed Drug Name.”                                                                                                                                                                  |
| PRN Effectiveness List Report | A report that lists PRN medications administered to a patient that needs Effectiveness comments.                                                                                                                                                                                                                             |
| Provider                      | Another name for the “Physician” involved in the presecription of a medication (i.e., Unit Dose or IV) to a pateint.                                                                                                                                                                                                         |
| PSB INSTRUCTOR                | The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.                                                                                                                                                               |
| PSB STUDENT                   | The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options with BCMA V. 3.0. This key requires that a nursing instructor sign on to BCMA V. 3.0.                                                                                           |
| Refused                       | The status for an IV bag or Unit Dose to indicate that the patient refused to take the dose.                                                                                                                                                                                                                                 |
| Removed                       | The status for a patch (i.e., Nitroglycerin, Fentanyl, or Nicotine) to indicate that it has been removed from a patient. Once removed, the letters “RM” (for “Removed”) display in the Status column of the VDL.                                                                                                             |
| Schedule         | The frequency at which a medication is administered to a patient. For example, QID, QD, QAM, Q4H.                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schedule Type    | Identifies the type of schedule (i.e., Continuous, PRN, On-Call, and One-Time) for the medication being administered to a patient.                                                                                                                                                                                                     |
| Security Keys    | Used to access specific options within BCMA that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.                                                                                                                                                                         |
| Start Date/Time  | The date and time that a medication is scheduled for administration to a patient.                                                                                                                                                                                                                                                      |
| STAT Order       | A medication order given immediately to a patient, entered as a One-Time order by providers and pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.                                                                                                         |
| Status           | A code used to inform a clinician about the condition or progress of a medication order. For Unit Dose and IVP/IVPB orders, status codes include G=Given, H=Held, R=Refused, M=Missing, and RM=Removed (patch removal only). For IV orders, status codes include I=Infusing, H=Held, R=Refused, S=Stopped, C=Completed, and M=Missing. |
| Stop Date/Time   | The date and time that a medication order will expire, and should no longer be administered to a patient.                                                                                                                                                                                                                              |
| Unit Dose        | A medication given to a patient, such as tablets or capsules.                                                                                                                                                                                                                                                                          |
| VDL              | An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA.                                                                                                                                         |
| Verify           | When a nurse or a pharmacist confirms that a medication order is accurate and complete, according to the information supplied by the provider.                                                                                                                                                                                         |
| Virtual Due List | Also called “VDL,” an on-line list used by clinicians when administering active medication orders to a patient. This is the Main Screen in BCMA.                                                                                                                                                                                       |

# # INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acronyms, 37

Bar Code Label, Sample, 32

Barcode Label Print, 31

BCMA, 1

On-line Help, 3

BCMA Menu, 5

Documentation Conventions, 3

Drug File Inquiry, 29

Due List Report, 15

Glossary, 37

GUI Options, 5, 15

Missing Dose Report, 24

Pharmacy Option Menu, 5

Pharmacy Reasons Needed Selection Table, 23

Sample reports

Missing Dose Report, 26

Sample reports

Due List Report by Patient, 17, 18

Medication Administration History Report by Patient, 20

Medication Administration Log Report by Patient, 9

Medication Administration Log Report by Ward, 10

Missed Medications by Ward Report, 14

Missed Medications Report by Patient, 13

Missed Medications Report Screen, 12

Missing Dose Report, 25

Sample reports

Report for Respiratory Therapy Medications, 36

Sample screens

Bar Code Label Print Screen, 31, 33, 34b

Drug File Inquiry Screen 1, 29

Drug File Inquiry Screen 2, 30

Due List Report Request Screen, 15, 21

Missing Dose Follow Up Request Screen, 21

Missing Dose Request Pharmacy Follow-up Information Screen, 22

Sample Screens

BCMA Pharmacy Option Menu Screen, 5

Medication Administration Log Report Screen, 8

Using ScreenMan Format to Request a Report, 6

Sample Unit Dose Bar Code Label, 32

Sample Ward Stock Bar Code Label, 32

Terms, 38

Using the Pharmacy Menu Options

Request a Report, 6

Using the Pharmacy Menu Options

Medication Administration Log, 8

Using the Pharmacy Menu Options

Medication Administration Log, 8

Using the Pharmacy Menu Options

Missed Medications Report, 11

Using the Pharmacy Menu Options

Missed Medications, 11

Using the Pharmacy Menu Options

Due List, 15

Using the Pharmacy Menu Options

Medication Administration History (MAH), 19

Using the Pharmacy Menu Options

Missing Dose Follow-up, 21

Using the Pharmacy Menu Options

Missing Dose Report, 24

Using the Pharmacy Menu Options

Drug File Inquiry, 29