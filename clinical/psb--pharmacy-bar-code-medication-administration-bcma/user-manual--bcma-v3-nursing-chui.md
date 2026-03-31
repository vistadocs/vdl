---
title: BCMA Version 3 Nursing CHUI User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Nursing CHUI
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - medication
  - report
  - administration
  - patient
  - date
  - ward
  - prompt
  - time
  - press
  - span
page_count: 0
word_count: 9190
section_count: 23
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_nurse_chui_r1216.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_nurse_chui_r1216.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](bcma-version-3-nursing-chui-user-manual/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

NURSING CHUI USER MANUAL

February 2004

(Revised December 2016)

Office of Information & Technology (OI&T)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [introduction](#introduction)
  - [What is BCMA?](#what-is-bcma)
  - [Features of BCMA](#features-of-bcma)
- [About This Manual](#about-this-manual)
  - [Special Notations—Documentation Conventions](#special-notationsdocumentation-conventions)
  - [Package Conventions](#package-conventions)
  - [Intranet Documentation](#intranet-documentation)
  - [On-line Help](#on-line-help)
- [# BCMA Menu—Nursing Option](#bcma-menunursing-option)
  - [Using the Medication Administration Menu Nursing Option](#using-the-medication-administration-menu-nursing-option)
  - [Using ScreenMan Format to Request a Report](#using-screenman-format-to-request-a-report)
  - [Medication Administration Log Report](#medication-administration-log-report)
  - [Missed Medications Report](#missed-medications-report)
  - [Edit Medication Log](#edit-medication-log)
  - [Ward Administration Times Report](#ward-administration-times-report)
  - [Due List Report](#due-list-report)
  - [PRN Effectiveness List Report](#prn-effectiveness-list-report)
  - [Enter PRN Effectiveness](#enter-prn-effectiveness)
  - [Manual Medication Entry](#manual-medication-entry)
  - [Medication Administration History (MAH) Report](#medication-administration-history-mah-report)
  - [Missing Dose Request](#missing-dose-request)
  - [## Medication Variance Log Report](#medication-variance-log-report)
  - [Drug File Inquiry](#drug-file-inquiry)
- [# glossary](#glossary)
  - [Acronyms](#acronyms)
  - [Terms](#terms)
- [INDEX](#index)
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
<td>11/2016</td>
<td><p><a href="#revision-history">i</a>-<a href="#toc">iv</a></p>
<p><a href="#features-of-bcma">1</a></p>
<p><a href="#p5">3</a></p>
<p><a href="#p9">7</a>-<a href="#missed-medications-report">9</a></p>
<p><a href="#page10">10</a>-<a href="#missedmedreportbyward">12</a></p>
<p><a href="#ward-administration-times-report">13</a>-<a href="#admin_times_reportbypatient">14</a></p>
<p><a href="#p17">15</a>, <a href="#p19">17</a>-<a href="#duelistreportby_ward">18</a></p>
<p><a href="#p23">21</a></p>
<p><a href="#man_medication_entry">24</a>-<a href="#p29">27</a></p>
<p><a href="#med_admin_history_report_bypatient">29</a></p>
<p><a href="#med_variance_log_report">30</a></p>
<p><a href="#index">40</a></p></td>
<td>PSB*3*83</td>
<td><p>Updated Revision History and TOC.</p>
<p>Added new removal information for medications requiring removal.</p>
<p>Updated BCMA Nursing Option Menu Screen.</p>
<p>Added explanations and new screen prints for BCMA reports containing medications requiring removal changes: Medication Administration Log,</p>
<p>Updated Missed Medications.</p>
<p>Updated Ward Administration Times Report and Administration Times Report by Patient screens.</p>
<p>Updated Due List Report section and screens.</p>
<p>Updated Patient Selection Screen.</p>
<p>Updated Manual Medication Entry and screen.</p>
<p>Updated Administration Time Selection and Medication Log Manual Entry screens.</p>
<p>Updated Medication Administration History Report by Patient screen.</p>
<p>Updated Medication Variance Log Report screen.</p>
<p>Updated Index.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2015</td>
<td><a href="#missing-dose-request">31-35</a></td>
<td>PSB*3*70</td>
<td><p>Removed <em>Missing Dose Request</em> [PSB MISING DOSE REQUEST] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/2004</td>
<td><p>iii-iv,</p>
<p>5</p>
<p>14-18,</p>
<p>50</p>
<p>53-54</p></td>
<td>PSB*3*3</td>
<td><p>– Added a note in the Table of Contents and Table of Exhibits about section 3.5 and Exhibits 7-10 being moved to the GUI BCMA pkg./manual. (p. iii-iv)</p>
<p>– Removed the reference to the Edit Medication Log in the second paragraph, and updated Exhibit 1: BCMA Nursing Option Menu Screen. (p. 5)</p>
<p>– Removed section 3.5 and Exhibits: 7-10 and replaced with blank pages, since the Edit Medication Log functionality was removed from the CHUI BCMA and incorporated into the GUI BCMA package and the associated user manual. (p. 14-18)</p>
<p>-- Updated definition of “Not Given” and fixed typos on page. (p. 50)</p>
<p>– In the Index, under the “Sample Screens” and “Using the Medication Administration Menu Nursing Options” sections removed references to pages 14-18 since the Edit Medication Log functionality was removed from the CHUI BCMA and this user manual. (p. 53-54).</p></td>
</tr>
<tr class="even">
<td>07/2004</td>
<td>36, 37</td>
<td>PSB*3*5</td>
<td><p>– Updated the second paragraph to include the “Allergies” information.<br />
(p. 36)</p>
<p>– Updated the “Example 25: Medication Administration History Report by Patient” to show the removal of the Reactions header and the inclusion of the ADRs header and the Allergies header. (p. 37)</p></td>
</tr>
<tr class="odd">
<td>02/2004</td>
<td></td>
<td></td>
<td>Original Released BCMA V. 3.0 Nursing CHUI User Manual.</td>
</tr>
</tbody>
</table>
TABLE OF CONTENTS
<span id="toc" class="anchor"></span>TABLE OF EXHIBITS

# introduction

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
- Provides full compatibility with the existing V*IST*A system.
- Identifies Pro Re Nata (PRN) entries that require Effectiveness comments.
- Replaces the manual Medication Administration Record (MAR) with a Medication Administration History (MAH) to provide an automatic record of a patient’s medication administration information.
- Provides a list of variances that identify Early or Late medication administrations and late PRN Effectiveness entries.
- Provides the ability to document the patient’s pain score in BCMA and store it in the Vitals package.
- Includes removal information for medications requiring removal in addition to existing administration information.
- 

# About This Manual

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

You can locate this and other BCMA-related documentation on the Intranet, from the V*IST*A Documentation Library (VDL), at the following address. It provides background, technical information, and important user documentation.

<http://www.va.gov/vdl>

Remember to bookmark this site for future reference.

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

?, ??, ???  
On-line help is available by entering one, two, or three question marks at a prompt. One question mark elicits a brief statement of what information is appropriate for the prompt; two question marks elicits more help, plus the hidden actions shown above; and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

# # BCMA Menu—Nursing Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using the Medication Administration Menu Nursing Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA Nursing Option Menu, as illustrated in Exhibit 1, lets Nursing personnel access information that has been entered via the BCMA Graphical User Interface (GUI) VDL. Because BCMA operates in real time, scanned information is available as soon as the scan is successfully completed. You can access the Nursing Option Menu from any V*IST*A-enabled terminal within the VAMC.

Several of these options are available under both the Nursing and the Pharmacy menu options. The options that are unique to Nursing include Ward Administration Times, PRN Effectiveness List, Enter PRN Effectiveness, Manual Medication Entry, and Medication Variance Log.

<span id="p5" class="anchor"></span>Exhibit 1: BCMA Nursing Option Menu Screen

> ![](bcma-version-3-nursing-chui-user-manual/002.png)

To select a Nursing option:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, enter the number of the desired option.
2.  Press \<Enter\> to display the Sort Screen for the option chosen.

## Using ScreenMan Format to Request a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many of the Nursing options use a common screen to define selection criteria for reports, as illustrated in Exhibit 2, Report Request Using ScreenMan Format. Other options use specific screens. This section explains the screen prompts for all reports using the Report Information Sort Screen and gives instructions for entering information. Following this section are sample reports that you can run from each of the Medication Administration Menu Nursing options.

<span id="_Toc456062586" class="anchor"></span>Exhibit 2: Report Request Using ScreenMan Format Screen

![](bcma-version-3-nursing-chui-user-manual/003.png)

Many of the reports can be sorted and printed in the following ways:

- By patient. The information will display chronologically.
- By ward. The system can sort the information by patient or room/bed, and display it chronologically within each patient.

To request a report using ScreenMan:

1.  At the “Start Date:” prompt, type the start date of the report, and then press \<Enter\>.  
    Note: The cursor moves to the next prompt each time that you press \<Enter\>.

To display a list or a standard date and time format, enter a ? at any date or time prompt, and then press \<Enter\>.

2.  At the first “At:” prompt, type the start time of the report (in HHMM format), and then press \<Enter\>.
3.  At the “Stop Date:” prompt, type the stop date, and then press \<Enter\>.
4.  At the second “At:” prompt, type the stop time (in HHMM format), and then press \<Enter\>.
5.  At the “Run by Patient or Ward:” prompt, type P for Patient or W for Ward, and then press \<Enter\>.
- If you are sorting the report by ward, at the “Ward Location:” prompt, type the ward designation, and then press \<Enter\>. At the “Sort by Pt or Room-Bed:” prompt, type P for Patient or R for Room, and then press \<Enter\>.
- If sorting the report by patient, at the “Patient Name:” prompt, type the patient’s name or Social Security Number (SSN), and then press \<Enter\>.

To display a list, enter a ? at any “Patient Name:” prompt, and then press \<Enter\>.

6.  At the “Include Comments:” prompt, enter Y for Yes or N for No, and then press \<Enter\>.

If a “Yes/No” prompt is blank, press \<Enter\> to respond No.

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

The *Medication Administration Log* \[PSBO ML\] option lets Nursing personnel create the Medication Administration Log Report, which provides detailed administration information and removal information for medications requiring removal for a specified date/time range. The report can be sorted and printed by patient or by ward. When printed by ward, you may sort the view by patient or room/bed. With this sort, the drug administration information will be printed chronologically within each patient.

The Medication Administration Log Report prints in a 132-column output. Exhibit 3, Medication Administration Log Report by Patient, and Exhibit 4, Medication Administration Log Report by Ward, show examples of both Medication Administration Log Reports.

- Throughout this manual, the reports shown are provided for illustrative purposes only. Actual reports may be longer.

To print a Medication Administration Log Report:

1\. At the Medication Administration Menu Nursing Option:” prompt, type 1, and then press \<Enter\> to access the *Medication Administration Log* \[PSBO ML\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Medication Administration Log Report.

  
<span id="p9" class="anchor"></span>Exhibit 3: Medication Administration Log Report by Patient

================================================================================================================================

Medication Log Report for May 10, 2016@00:01 to May 20, 2016@24:00

Include Inpatient and Clinic Orders

Continuing/PRN/Stat/One Time Medication/Treatment Record (Detailed Log) (VAF 10-2970 B, C, D)

Run Date: MAY 20, 2016@14:49

Log Type: INDIVIDUAL PATIENT Page: 1

Patient: TESTPATNM,TWO SSN: 666-23-2323 DOB: DEC 12,1955 (60)

Sex: MALE Hit/Wt: \*/\* Ward: GEN MED Rm:

Dx: AGITATED Last Mvmt: DEC 16,2015@17:48:10 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: No Known Allergies

================================================================================================================================

Location

Activity Date Orderable Item Action Action

Start Date\> \[Dose/Sched/Route/Body Site\] By Date/Time Drug/Additive/Solution U/Ord U/Gvn Unit

Stop Date\<

--------------------------------------------------------------------------------------------------------------------------------

GEN MED B-4

05/11/16 17:55 ASPIRIN \[325MG Q4H PO\] NSS 05/11/16 17:55

Given

5/11/16 10:00\> ASPIRIN BUFFERED 325MG TAB 1.00 1.00 CAP,ORAL

Comments: 05/11/16 17:55 NSS Test comment

5/16/16 18:14:07\<

Audits: 05/11/16 17:55 NSS Field: ACTION DATE/TIME Set to 'MAY 11, 2016@17:55:49'.

05/11/16 17:55 NSS Field: ACTION STATUS Set to 'GIVEN' by 'NSS'.

05/11/16 17:55 NSS Field: DOSES GIVEN Set to '1'.

05/11/16 17:55 NSS Field: UNIT OF ADMINISTRATION Set to 'CAP,ORAL'.

--------------------------------------------------------------------------------------------------------------------------------

GEN MED B-4

05/11/16 18:06 SELEGILINE \[13J ONCE Derm

Site: ARM, LEFT UPPER\] NSS 05/11/16 18:07

Removed

NSS 05/11/16 18:06

Given

5/11/16 13:00\> SELEGILINE 12MG/24HR PATCH 1.00 1.00 PATCH

Comments: 05/11/16 18:07 NSS Removed: TEST

5/11/16 18:06:09\<

Audits: 05/11/16 18:06 NSS Field: ACTION DATE/TIME Set to 'MAY 11, 2016@18:06:09'.

05/11/16 18:06 NSS Field: ACTION STATUS Set to 'GIVEN' by 'NSS'.

05/11/16 18:06 NSS Field: DOSES GIVEN Set to '1'.

05/11/16 18:06 NSS Field: UNIT OF ADMINISTRATION Set to 'PATCH'.

05/11/16 18:07 NSS Field: ACTION DATE/TIME 'MAY 11, 2016@18:06:09' deleted.

05/11/16 18:07 NSS Field: ACTION DATE/TIME Set to 'MAY 11, 2016@18:07:06'.

05/12/16 18:01 NSS Field: ACTION STATUS Set to 'REMOVED' by 'NSS'.

--------------------------------------------------------------------------------------------------------------------------------

Exhibit 4: Medication Administration Log Report by Ward

================================================================================================================================

Medication Log Report for May 11, 2016@00:01 to May 12, 2016@24:00

Include Inpatient and Clinic Orders

Continuing/PRN/Stat/One Time Medication/Treatment Record (Detailed Log) (VAF 10-2970 B, C, D) Run Date: MAY 20, 2016@16:46

LOG TYPE: WARD Page: 1

Ward Location: GENERAL MED Division: ALBANY

================================================================================================================================

Location

Activity Date Orderable Item Action Action

Start Date\> \[Dose/Sched/Route/Body Site\] By Date/Time Drug/Additive/Solution U/Ord U/Gvn Unit

Stop Date\<

-------------------------------------------------------------------------------------------------------------------------------

TESTPATNM,TWO (000000000)

Ward: GEN MED Rm-Bed: \*\*\*

-------------------------------------------------------------------------------------------------------------------------------

GEN MED

05/11/16 21:02 ACETAMINOPHEN \[325MG Q8H PO\] LM 05/11/16 21:02

Given

5/11/16 13:00\> ACETAMINOPHEN 325MG TABLET 1.00 1.00 TAB

---------------------------------------------------------------------------------------------------------------------------------

GEN MED B-4

05/11/16 18:26 NICOTINE \[1 Q8H Derm Site:

BACK, MIDDLE\] NSS 05/12/16 08:41

Removed

NSS 05/11/16 18:26

Given

5/11/16 12:30\> NICOTINE 11MG/24HR PATCH 1.00 1.00 PATCH

--------------------------------------------------------------------------------------------------------------------------------

TESTPATNM,THREE (000000000)

Ward: GEN MED Rm-Bed: B-4

GEN MED B-4

05/12/16 08:42 LIDOCAINE \[1 Q24 Derm Site:

ARM, LEFT UPPER\] NSS 05/12/16 08:42

Given

5/11/16 18:01\> LIDOCAINE 5% PATCH 1.00 1.00 PATCH

## Missed Medications Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="page10" class="anchor"></span>The *Missed Medications* \[PSBO MM\] option lets Nursing personnel print a Missed Medications Report, which includes Continuous or One-Time Unit Dose and IV Piggyback medications that were *not* administered to a patient during a medication pass. This report also includes patient demographics data, adverse drug reaction (ADR) information, ward/bed location, administration date/time, removal date/time for medications requiring removal, order number from Inpatient Medications V. 5.0, and the medication type of the missed medication. (Self-medications do *not d*isplay on the report.) The report can be sorted and printed by ward or patient, and you can specify the date and time that the report covers.

- Information that may display on this report includes medications that were scheduled to be administered, but were *not* marked as Given, Held, or Refused. It may also include medications that have been renewed or expired shortly after the scheduled administration time, and medications requested from the Pharmacy as Missing Dose Requests. Medications placed “On Hold” and taken “Off Hold” via the Computerized Patient Record System (CPRS) or Inpatient Medications V.5.0 will display on this report with the Hold information below the medication. The Hold information applies only to administrations due within the Hold timeframe.  
    
  The “Order Num” column on the report, shown in Exhibit 6, lists the actual order number and type (i.e., Unit Dose or IV). This information is quite helpful when troubleshooting problems with BCMA.

To print a Missed Medications Report:

1\. At the “Select Medication Administration Menu Nursing Option:” prompt, type 2, and then press \<Enter\> to access the *Missed Medications* \[PSBO MM\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Missed Medications Report.

The reports will print in a 132-column output. Exhibit 5, Missed Medications Report by Patient, and Exhibit 6, Missed Medications Report by Ward, show examples of both Missed Medications Reports.

- You should run the Missed Medications Report by Ward after each scheduled admin time to ensure that all entries listed on this report are resolved.

  
Exhibit 5: Missed Medications Report by Patient

===============================================================================================================

MISSED MEDICATIONS REPORT for May 11, 2016@00:01 to May 14, 2016@24:00

Run Date: MAY 20, 2016@15:48

Include Inpatient Orders Only

Order Status(es): Active / DC'd / Expired Page: 1

Admin Status(es): Missing Dose / Held / Refused

Include Comments/Reasons

Patient: TESTPAT, THREE : 000-00-0000 DOB: JAN 22,1972 (44)

Sex: FEMALE Ht/Wt: \*/\* Ward: GEN MED Rm: B-4

Dx: Undetermined back pain Last Mvmt: SEP 28,2015@11:48:24 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: STRAWBERRIES

===============================================================================================================

Order Status Ver Missed Date/Time Medication Order Stop Date

---------------------------------------------------------------------------------------------------------------

Active \*\*\* 05/11/2016@0500 NIACIN INJ,SOLN 05/11/2016@1813

Active \*\*\* 05/12/2016@0600 SELEGILINE PATCH 12/03/2016@0700

Admin. Status: (Refused)

Comment: Refused: Nausea

Active \*\*\* 05/12/2016@2040 LIDOCAINE PATCH 12/01/2016@0600

(Remove)

Active \*\*\* 05/13/2016@2100 ASPIRIN CAP,ORAL 07/01/2016@0800

  
<span id="missedmedreportbyward" class="anchor"></span>Exhibit 6: Missed Medications Report by Ward

==============================================================================================================

MISSED MEDICATIONS REPORT for May 11, 2016@00:01 to May 12, 2016@24:00

Run Date: MAY 20, 2016@15:53

Include Inpatient Orders Only

Order Status(es): Active / DC'd / Expired Page: 1

Admin Status(es): Missing Dose / Held / Refused

Include Comments/Reasons

Ward Location: GENERAL MED Division: ALBANY

===============================================================================================================

Order Status Ver Room-Bed Patient Missed Date/Time Medication

---------------------------------------------------------------------------------------------------------------

DC'd (Edit) \*\*\* B-4 TESTPAT,THREE (2223) 05/11/2016@0900 ASPIRIN CAP,ORAL

DC'd \*\*\* B-4 TESTPAT,THREE (2223) 05/11/2016@0900 NIACIN INJ,SOLN

Active \*\*\* B-4 TESTPAT,THREE (2223) 05/11/2016@2100 LIDOCAINE PATCH

(Remove)

Active \*\*\* B-4 TESTPAT,THREE (2223) 05/11/2016@2100 LIDOCAINE PATCH

Active \*\*\* \*\* TESTPATNM,TWO (2123) 05/12/2016@0100 ACETAMINOPHEN TAB

Active \*\*\* \*\* TESTPATNM,TWO (2123) 05/12/2016@0900 NITROGLYCERIN

Active \*\*\* \*\* TESTPATNM,TWO (2123) 05/12/2016@0900 SELEGILINE PATCH

## Edit Medication Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pages 14-18 referred to functionality that is no longer available in the CHUI BCMA package  
and has been incorporated into the GUI BCMA package and the associated user manual.

## Ward Administration Times Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Ward Administration Times* \[PSBO WA\] options lets Nursing personnel print the Ward Administration Times Report, which lists current medications, administration times, and removal times for medications requiring removal (from the earliest to the latest) due, depending on the sort criteria that you determine. This report includes patient demographics data; ADR information; plus detailed information about the order such as the medication type, dose, and route; and the administration time. It is particularly helpful to Nursing personnel to help determine when medications are administered to patients, and the frequency and number of medications administered and removed during a particular date/time.

The Ward Administration Times Report can be sorted and printed in the following ways:

- By patient. Each scheduled medication due to a patient and the related administration time is listed.
- By ward. The total number of medications due at each administration time is listed for each patient, including the number scheduled for each hour and 24-hour totals for the entire ward.

You can use the Ward Report for determining workloads on a ward.

To print a Ward Administration Times Report:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 4, and then press \<Enter\> to access the *Ward Administration Times* \[PSBO WA\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Ward Administration Times Report.

The printed report is formatted as shown in Exhibit 11, Administration Times Report by Patient, and Exhibit 12, Administration Times Report by Ward.

<span id="admin_times_reportbypatient" class="anchor"></span>Exhibit 4: Administration Times Report by Patient

PATIENT ADMINISTRATION TIMES Run Date: MAY 23, 2016@13:09

Include Inpatient Orders Only

ADMINISTRATION DATE: MAY 23, 2016 to MAY 23, 2016

Page: 1

Patient: TESTPAT,THREE SSN: 000-00-0000 DOB: JAN 22,1972 (44)

Sex: FEMALE Ht/Wt: \*/\* Ward: GEN MED Rm: B-4

Dx: Undetermined back pain Last Mvmt: SEP 28,2015@11:48:24 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: BEE STING

===============================================================================================================

Date/Time Self Med Medication Dose/Route

---------------------------------------------------------------------------------------------------------------

MAY 23, 2016

1:00a ASPIRIN CAP,ORAL Dosage: 325MG Route: ORAL

6:00a FENTANYL PATCH Dosage: 1 PATCH Route: TRANSDERMAL

6:00a SELEGILINE PATCH Dosage: 1 Route: TRANSDERMAL

7:00a ASPIRIN CAP,ORAL Dosage: 325MG Route: ORAL

12:00n (RM) SELEGILINE PATCH Dosage: 1 Route: TRANSDERMAL

1:00p ASPIRIN CAP,ORAL Dosage: 325MG Route: ORAL

===============================================================================================================

TESTPAT,THREE 666-12-2223 Ward: GEN MED Room-Bed: B-4

<span id="_Toc459639951" class="anchor"></span>Exhibit 5: Administration Times Report by Ward

## Due List Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Due List \[PSBO DL\]* option lets Nursing personnel print the Due List Report in CHUI BCMA, which displays the information available from the VDL within GUI BCMA. It provides detailed information about active and future Unit Dose and IV medication orders that are “due” for administering to a patient <span id="p17" class="anchor"></span>or removal for medications requiring removal — during a timeframe that you specify — within a 24-hour period. Within the date/time range, the report may be printed by patient or by ward, and include/exclude the following:

- Continuous, PRN, On-Call, and One-Time Schedule Types
- Unit-Dose or IV medications
- Addendums

The Due List Report includes patient demographics data, ADR information, plus detailed information about an order, such as whether (or *not*) the medication is a self-med; the medication type, schedule, dose, and route; Special Instructions; administration times; remove time; Last Given date and time; Start/Stop date and time; and the individual(s) who verified the order.

- Only medications active at the time the Due List is printed will display on the report. The printed Due List and the VDL within GUI BCMA may *not* match if orders have been added, discontinued, or renewed after printing.

Complete the steps on the next page to enter information on the screen illustrated in Exhibit 13, Due List Report Request Screen.

<span id="_Toc454692568" class="anchor"></span>Exhibit 6: Due List Report Request Screen

![](bcma-version-3-nursing-chui-user-manual/004.png)

To print a Due List Report:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 5, and then press \<Enter\> to access the *Due List \[PSBO DL\]* option.
2.  At the “Start Date:” prompt, type the date, and then press \<Enter\>.
3.  At the “Start Time:” prompt, type the time, and then press \<Enter\>.
4.  At the “Stop Date:” prompt, type a date, and then press \<Enter\>.
5.  At the “Run by Patient or Ward:” prompt, type P for Patient or W for Ward, and then press \<Enter\>.
- If you are sorting the report by patient, at the “Patient Name:” prompt, type the patient's name or SSN, and then press \<Enter\>.
- If you are sorting the report by ward, in the ward location, type the ward designation, and then press \<Enter\>. At the “Sort by Pt or Room-Bed:” prompt, type P for Patient or R for Room/Bed, and then press \<Enter\>.
6.  At the “Include Schedule:” prompts, enter Y for Yes for the desired Schedule Type(s) and N for No for the others and, then press \<Enter\>.
7.  At the “Include Order Types:” prompts, enter Y for Yes or N for No at the “IV:” prompt and “Unit Dose:” prompt, and then press \<Enter\>. If you enter N for No at both prompts, no orders will print on the report.
8.  At the “Include Addendums:” prompt, enter Y or N, and then press \<Enter\>. When Y is entered, an additional section called Changes/Addendums to Orders will print at the bottom of the report. You can use this section of the report to manually record information about a medication administration.
9.  At the “Print to Device:” prompt, type the desired printer, and then press \<Enter\>.
10. At the “Queue to Run At:” prompt, type the date you want to run a report, and then press \<Enter\>. If you press \<Enter\>, the system defaults to the current date and time.
11. At the “\<Ret\> Re-Edit:” prompt, press the PF1 (or Num Lock), followed by E (Exit) to submit the request for printing. (Other available actions at this prompt are PF1 - Q to Quit, or PF1-R to refresh the screen.)

The screen clears and the following message displays:

> Submitting Your Report Request to Taskman…Submitted!

> Your Task Number Is: XXXX

The reports will print in a 132-column output. Exhibit 14, Due List Report by Patient, and Exhibit 15, Due List Report by Ward, show examples of both Due List Reports.

<span id="p19" class="anchor"></span>Exhibit 7: Due List Report by Patient

================================================================================================================================

MEDICATION DUE LIST for MAY 12, 2016@0200 to MAY 12, 2016@2400 Run Date: MAY 12, 2016@02:05

Include Inpatient Orders Only

Schedule Type(s): Continuous / PRN / OnCall / OneTime Page: 1

Order Type(s): IV / Unit Dose / Future Orders

Patient: TESTPAT,THREE : 666-12-2223 DOB: JAN 22,1972 (44)

Sex: FEMALE Ht/Wt: \*/\* Ward: GEN MED Rm: B-4

Dx: Undetermined back pain Last Mvmt: SEP 28,2015@11:48:24 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: STRAWBERRIES

=================================================================================================================================

Start Stop

Self Last Date Date Verifying

Med Sched Medication Dose Route Given @Time @Time Rph/Rn

--------------------------------------------------------------------------------------------------------------------------------

Administration Date: MAY 12, 2016

UD-C ASPIRIN CAP,ORAL Give: 325MG Q4H ORAL 05/11/16@1817 5/11/16 7/1/16 NSS/\*\*\*

@12:00 @08:00

\*ASPIRIN BUFFERED 325MG TAB Admin Times:

0900-1300-1700-2100

UD-C NICOTINE PATCH Give: 1 Q24 TRANSD

ERMAL 05/12/16@0842 5/11/16 12/1/16 NSS/\*\*\*

@18:01 @06:00

\* NICOTINE 7MG/24HR PATCH Admin Times: 0900

Remove Time: 2100

---------------------------------------------------------------------------------------------------------------------------------

Changes/Addendums to orders

-------------------------------------------------------------------------------------------------------------------------------

CON \_\_\_ PRN \_\_\_ Drug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Give: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Start: \_\_\_\_\_\_\_\_\_ Stop: \_\_\_\_\_\_\_\_\_

Remove: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Spec

OT \_\_\_ OC \_\_\_ Inst: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Initials: \_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_

--------------------------------------------------------------------------------------------------------------------------------

CON \_\_\_ PRN \_\_\_ Drug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Give: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Start: \_\_\_\_\_\_\_\_\_ Stop: \_\_\_\_\_\_\_\_\_

Remove: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Spec

OT \_\_\_ OC \_\_\_ Inst: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Initials: \_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_

================================================================================================================================

TESTPAT,THREE 666-12-2223 Ward: GEN MED Room-Bed: B-4

<span id="duelistreportby_ward" class="anchor"></span>Exhibit 8: Due List Report by Ward

================================================================================================================================

MEDICATION DUE LIST for MAY 23, 2016@0400 to MAY 23, 2016@2400 Run Date: MAY 23, 2016@16:02

Include Inpatient Orders Only

Schedule Type(s): Continuous / PRN / OnCall / OneTime Page: 1

Order Type(s): IV / Unit Dose / Future Orders

Ward Location: GENERAL MED

Patient: TESTPATIENT,ZERO : 666-11-2348 DOB: JUL 10,1997 (18)

Sex: MALE Ht/Wt: \*/\* Ward: GEN MED Rm:

Dx: TRAUMA TO HEAD Last Mvmt: JUN 29,2015@12:55:52 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: No Known Allergies

================================================================================================================================

Start Stop

Self Last Date Date Verifying

Med Sched Medication Dose Route Given @Time @Time Rph/Rn

--------------------------------------------------------------------------------------------------------------------------------

Administration Date: MAY 23, 2016

UD-C ASPIRIN CAP,ORAL Give: 325MG Q4H ORAL 05/23/16@1252 5/11/16 7/1/16 NSS/\*\*\*

@12:00 @08:00

\*ASPIRIN BUFFERED 325MG TAB Admin Times:

0500-0900-1300-1700-2100

--------------------------------------------------------------------------------------------------------------------------------

UD-C FENTANYL PATCH Give: 1 PATCH BID TRANSD

ERMAL 05/23/16@1054 5/11/16 8/9/16 RG/\*\*\*

@09:00 @24:00

\*FENTANYL 100MCG/HR PATCH Admin Times: None

Remove Time: 2100

---------------------------------------------------------------------------------------------------------------------------------

Changes/Addendums to orders

-------------------------------------------------------------------------------------------------------------------------------

CON \_\_\_ PRN \_\_\_ Drug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Give: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Start: \_\_\_\_\_\_\_\_\_ Stop: \_\_\_\_\_\_\_\_\_

Remove: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Spec

OT \_\_\_ OC \_\_\_ Inst: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Initials: \_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_

--------------------------------------------------------------------------------------------------------------------------------

CON \_\_\_ PRN \_\_\_ Drug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Give: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Start: \_\_\_\_\_\_\_\_\_ Stop: \_\_\_\_\_\_\_\_\_

Remove: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Spec

OT \_\_\_ OC \_\_\_ Inst: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Initials: \_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_

================================================================================================================================

TESTPATIENT,ZERO 666-11-2348 Ward: GEN MED Room-Bed: B-2

## PRN Effectiveness List Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *PRN Effectiveness List* \[PSBO PE\] option lets Nursing personnel print the PRN Effectiveness List Report, which lists PRN medications administered to a patient that require an Effectiveness comment.  
It also includes patient demographics data, ADR information, plus the PRN medication, administration date and time, and the individual(s) who administered the order. You can print the report by patient or by ward.

The system files the Effectiveness comment, after you make an entry using the *PRN Effectiveness List* \[PSBO PE\] option, and then select one of the medications listed on the following report. The entry will not display on the PRN Effectiveness List Report the next time that it is printed.

You can print a PRN Effectiveness List Report after a patient has been discharged.

To print a PRN Effectiveness List Report:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 6, and then press \<Enter\> to access the *PRN Effectiveness List* \[PSBO PE\] option.

2\. See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a PRN Effectiveness List Report.

The printed reports are formatted as shown in Exhibit 16, PRN Effectiveness List Report by Patient and Exhibit 17, PRN Effectiveness List Report by Ward.

<span id="_Toc459639955" class="anchor"></span>Exhibit 9: PRN Effectiveness List Report by Patient

<span id="_Toc459639956" class="anchor"></span>Exhibit 10: PRN Effectiveness List Report by Ward

## Enter PRN Effectiveness

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Enter PRN Effectiveness* \[PSB MED LOG PRN EFFECT\] option lets Nursing personnel enter Effectiveness comments for PRN medications that were administered to a patient.

To enter PRN Effectiveness comments:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 7, and then press \<Enter\> to access the *Enter PRN Effectiveness* \[PSB MED LOG PRN EFFECT\] option. Additional information entry prompts will display, as illustrated in Exhibit 18, Patient Selection Screen, provided below.
2.  At the “Select Patient Name:” prompt, type the patient’s name or SSN, and then press \<Enter\>.
3.  At the “Select Date to Begin Searching Back From:” prompt, press \<Enter\> to select today’s date.
- If the medication was not administered today, a screen message will display, asking if you would like to move back one day. Press \<Enter\> to do so. This process will continue until the system reaches a date on which medications were administered. At that time, the list of medications will display as shown in Exhibit 19, Medication Selection Screen.

<span class="mark">  
</span><span id="p23" class="anchor"></span>Exhibit 11: Patient Selection Screen

![](bcma-version-3-nursing-chui-user-manual/005.png)

<span id="_Toc459639958" class="anchor"></span>Exhibit 12: Medication Selection Screen

![](bcma-version-3-nursing-chui-user-manual/006.png)

4.  At the “Enter a number (1-5):” prompt, type the number corresponding to the medication needing an Effectiveness comment, and then press \<Enter\>. The Effectiveness Comments Entry Screen displays, as shown in Exhibit 20, PRN Effectiveness Entry Screen.

<span id="_Toc459639959" class="anchor"></span>Exhibit 13: PRN Effectiveness Entry Screen

![](bcma-version-3-nursing-chui-user-manual/007.png)

5.  At the “PRN Effectiveness:” prompt, type a comment (up to 150 characters), and then press \<Enter\>.
6.  At the “COMMAND:” prompt, type S for Save, E to Exit, or R for Refresh, and then press \<Enter\>. When you save the comments, the system adds them to the PRN Effectiveness List Report.
- If you try to exit the screen and the data has not been saved, the system will display the “Save changes before leaving form (Y/N)?” prompt. If you enter N for No, the data will not be saved. If you enter Y for Yes, the changes will be saved.

## Manual Medication Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Manual Medication Entry* \[PSB MED LOG NEW ENTRY\] option lets Nursing personnel manually create a medication administration entry for any medication order. This option will also display orders that have expired or been discontinued on the date selected. Entries for expired and discontinued orders are sometimes necessary if a patient has been transferred or discharged before the administration documentation process has been completed.

- Medication orders will not be electronically validated with the *Manual Medication Entry* \[PSB MED LOG NEW ENTRY\] option. However, the Medication Log will include comments and audits for any order that was entered using the *Manual Medication Entry* \[PSB MED LOG NEW ENTRY\] option. You should limit the use of this option.

<span id="man_medication_entry" class="anchor"></span>Removal Times display after the Admin Times when the medication being manually administered and selected in the Manual Medication Entry screen for the patient is a medication requiring removal, as shown in Exhibits 22-24.

To manually create a medication administration entry for an active order:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 8, and then press \<Enter\> to access the *Manual Medication Entry* \[PSB MED LOG NEW ENTRY\] option. Additional information entry prompts will display, as illustrated in Exhibit 21, Manual Medication Entry Patient Selection Screen, provided below.
2.  At the “Select PATIENT:” prompt, type the patient’s name or SSN, and then press \<Enter\>.

<span id="_Toc459639960" class="anchor"></span>Exhibit 14: Manual Medication Entry Patient Selection Screen

![](bcma-version-3-nursing-chui-user-manual/008.png)

3.  At the “Select Orders From Date: Today//” prompt, press \<Enter\> to select today's date, or enter a date and then press \<Enter\>. A list of orders for this patient will display, as shown in Exhibit 22, Manual Medication Entry Medication Selection Screen.
4.  At the “Enter RETURN to continue or '^' to exit:” prompt, press \<Enter\> to continue with the entry.
- You can return to the Main Options Menu by entering ^, and then pressing \<Enter\>.

<span id="p33" class="anchor"></span>Exhibit 15: Manual Medication Entry Medication Selection Screen

Manual Medication Entry

\# Sc Medication St

--------------------------------------------------------------------------------

1\. C ACETAMINOPHEN TAB (A) Start: 01/10/2016 0800

Stop: 01/15/2016 2300

Admin Times: 0800-1600-2400

2\. C CAPSAICIN PATCH (A) Start: 01/08/2016 0900

Stop: 01/18/2016 2300

Admin Times: 0900

Removal Times: 1700

3\. C CONCENTRATED INSULIN INJ (A) Start: 01/10/2016 1200

Stop: 01/18/2016 2300

Admin Times: 0600-1200-1800-2400

4\. C GENTAMICIN INJ,SOLN (A) Start: 01/06/2016 1200

Stop: 01/18/2016 2300

Admin Times: 0100-0500-0900-1300-1700-2100

5\. C NICOTINE PATCH (A) Start: 01/12/2016 0800

Stop: 01/18/2016 2300

Admin Times: 0900

Removal Times: 2100

6\. O ACETAMINOPHEN TAB (E) Start: 12/08/2015 1324

Stop: 12/13/2015 2300

Enter a number (1-6): 5

5.  At the “Enter a number (1-6):” prompt, type the number that corresponds to the medication in the list, and then press \<Enter\>. The screen illustrated in Exhibit 23, Administration Time Selection Screen, will display.

<span id="p34" class="anchor"></span>Exhibit 16: Administration Time Selection Screen

Order: 66U

Medication: NICOTINE PATCH

Dosage: ONE PATCH

Schedule: QDAY

Admin Times: 0900

Removal Times: 2100

Is this the correct Order? Yes// (Yes)

Enter the DATE the medication was administered: //y ??

Enter the DATE the medication was administered: //t (JAN 12, 2016)

Select one of the following:

1 0900

Select Administration Time: 1 0900

Create an administration for JAN 12, 2016@09:00? Yes// (Yes)

6.  At the “Is this the correct Order? Yes//” prompt, press \<Enter\> to accept the order.
- If you enter N for No, the screen reverts to the Manual Medication Entry Medication Selection Screen, shown in Exhibit 22.
- A brief Administration History for PRN medications displays up to the last four actions for the selected orderable item.
7.  At the “Create an administration for this order? Yes//” prompt, press \<Enter\> if you want to create an administration for the PRN medication. Then enter a PRN Reason (1-30 characters) at the prompt that displays, and then press \<Enter\>.
8.  At the “Select Administration Time:” prompt, type the number of the desired administration time from the list provided, and then press \<Enter\>. The administration date and time will display at the “Create An Administration:” prompt.
- If the date and time are correct, press \<Enter\>.
- If the date and time are not correct, enter N for No at the “Create An Administration:” prompt. The screen will revert to the Manual Medication Entry Medication Selection Screen, as shown in Exhibit 22. The manual entry screen displays, as shown in Exhibit 24, Medication Log Manual Entry Screen.

<span id="p29" class="anchor"></span>Exhibit 17: Medication Log Manual Entry Screen

Medication Log Manual Entry - Unit Dose Order

--------------------------------------------------------------------------------

Patient: BCMAPATIENT,FOUR SSN: 000000404

<u>Medication</u>: NICOTINE

<u>Admin Status</u>: GIVEN <u>Admin Date/Time</u>: JAN 12,2016@19:30:21

Injection Site:

Dermal Site:

PRN Reason:

PRN Effectiveness:

Dispense Drugs...

<u>Comment (Required)</u>:

Administered as scheduled

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9.  At the “Admin Status:” prompt, type G for Given, H for Held, or R for Refused, and then press \<Enter\>.
10. At the “Admin Date/Time:” prompt, enter the actual administration date and time, and then press \<Enter\>.
11. At the “Injection Site:” prompt, enter a free-text comment, and then press \<Enter\>. This is required if the Medication Route for the medication order is defined to prompt for injection site in BCMA.
12. At the “Dermal Site:” prompt, enter a free-text comment, and then press \<Enter\>. This is required if the orderable item for the medication order is defined as a medication requiring removal, i.e., has “Prompt for Removal in BCMA” set to a value of 1, 2, or 3.
13. At the “PRN Reason:” prompt, enter a free-text comment, and then press \<Enter\>.
14. At the “PRN Effectiveness:” prompt, enter a free-text comment, and then press \<Enter\>.
15. At the “Dispense Drugs…” prompt, press \<Enter\>. A Dispense Drugs Popup Box will display the Dispense Drug(s) associated with this order, the number of units ordered and actually administered, and a description of the dispensed units associated with the drug name.
16. Perform the following actions:
- Change the dispense drug if desired, and then press \<Enter\>.
- At the “Units Given:” prompt, type a number between 0 and 50, and then press \<Enter\>.
- At the “Units” prompt, type the formbeing dispensed, such as Tablet, Capsule, or Liquid. This is a free-text entry prompt used to enter the units.
- After the Dispense Drugs information is complete, press \<Enter\> twice.
- At the “COMMAND: Close” prompt, press \<Enter\> again to close the Dispense Drugs Popup Box.
17. At the “Comment (Required):” prompt, type a free-text comment (up to 150 characters), and then press \<Enter\>. This is a required prompt anytime an entry is creating using the *Manual Medication Entry* \[PSB MED LOG NEW ENTRY\] option. You must enter the reason the medication entry is being edited. This information displays on the Medication Administration Log when a user requests an audit.
18. At the “COMMAND:” prompt, type S for Save, E for Exit, or R for Refresh, and then press \<Enter\>.
- If E is selected, and the data has not been saved, the system will display the “Save changes before leaving form (Y/N)?” prompt. If you enter N for No, the data will not be saved. If you enter Y for Yes, the changes will be saved.
19. The screen will display the “Enter RETURN to continue or '^' to exit” prompt.
- To edit another medication administration entry, press \<Enter\> twice.
- To return to the Main Options Menu, enter ^, and then press \<Enter\>.

## Medication Administration History (MAH) Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Medication Administration History (MAH)* \[PSBO MH\] option lets Nursing personnel print an MAH Report for Unit Dose and IV medication orders. This report lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (\*\*\*) to indicate that a medication was not due. This information is also noted in the Legend at the bottom of the MAH Report.

An MAH Report also includes patient demographics data, allergies and ADR information, plus detailed information about the order, such as the drug/additive/solution; the medication schedule, dose, route, and injection site; the actual administration times; removal times for medications requiring removal; the name and initials of the clinician who administered the medication; and the individuals who verified the order. It also includes information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.

- If no parameter is defined in CPRS, the maximum date range defaults to a seven-date range. For example, a report would list the Sunday proceeding, and the Saturday following, the date that you selected for the report.
- When a student nurse is administering medications under the supervision of an instructor, and both individuals hold the appropriate security keys (i.e., PSB STUDENT and PSB INSTRUCTOR), an asterisk prints next to the student’s initials on the MAH. A legend prints at the bottom of the MAH to indicate the date/time the medication was given, along with the names of the student and the instructor.

To print an MAH Report:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 9, and then press \<Enter\> to access the *Medication Administration History (MAH)* \[PSBO MH\] option.
2.  See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting an MAH. Exhibit 25, MAH Report by Patient, shows an example of the MAH Report.

  
<span id="med_admin_history_report_bypatient" class="anchor"></span>Exhibit 18: Medication Administration History Report by Patient

===============================================================================================================

MEDICATION ADMINISTRATION HISTORY for May 11, 2016@00:01 to May 12, 2016@09:00

Include Inpatient and Clinic Orders

Continuing/PRN/Stat/One Time Medication/Treatment Record (VAF 10-2970 B, C, D) Run Date: MAY 20, 2016@16:14

Page: 1

Patient: TESTPAT,NSTHREE SSN: 666-12-2223 DOB: JAN 22,1972 (44)

Sex: FEMALE Ht/Wt: \*/\* Ward: GEN MED Rm: B-4

Dx: Undetermined back pain Last Mvmt: SEP 28,2015@11:48:24 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: STRAWBERRIES

\*\* INPATIENT ORDERS \*\*

===============================================================================================================

Location \| \| \|

Start Date Stop Date \| Admin \| \|

and Time and Time \| Times \| 05/11/2016 \| 05/12/2016

INPATIENT \| \| \|

05/11/2016 06/01/2016 \| 0100 \| \| H0101 KRG

@12:00 @08:00 \| 0500 \| G0459 NSS \|

\| 0900 \| G0917 NSS \|

ASPIRIN CAP,ORAL \| 1300 \| G1312 LM \|

ASPIRIN BUFFERED 325MG TAB \| 1700 \| G1658 GRB \|

Give: 325MG PO Q4H \| 2100 \| G2100 GRB \|

\| \| \|

RPH: NSS RN: \| \| \|

-------------------------------------------------------------------------------------------------

INPATIENT \| \| \|

05/11/2016 05/23/2016 \| 0600 \| G0609 NSS \| G0559 KRG

@09:00 @15:44 \| 1800 \| RM1803 GRB \| RM1801 PRV

\| \| \|

FENTANYL PATCH \| \| \|

FENTANYL 12MCG/HR PATCH \| \| \|

Give: 1 PATCH Q12H \| \| \|

\| \| \|

Removal Times: 1800 \| \| \|

0600 \| \| \|

RPH: NSS RN: \| \| \|

---------------------------------------------------------------------------------------------------------------------------------

INPATIENT \| \| \|

03/28/2016 05/11/2016 \| 0100 \| G0100 NSS \| G0110 NSS

@11:00 @18:13 \| 0700 \| G0659 NSS \| G0701 NSS

\| 1300 \| G1258 LMN \| G1310 LMN

NIACIN INJ,SOLN \| 1900 \| G1805 PQR \| G1755 PQR

NIACIN 100MG/ML INJ Give: \| \| \|

7.5mg Q6H \| \| \|

\*\*\*DISCONTINUED BY PHARMACIST \| \| \|

NSS MAY 11, 2016@18:13:44 \| \| \|

RPH: NSS RN: \| \| \*\*\* \| \*\*\*

---------------------------------------------------------------------------------------------------------------------------------

Initial - Name Legend

Status Codes

C - Completed

G - Given

H - Held

I - Infusing

M - Missing Dose Requested

R - Refused

RM - Removed

S - Stopped

\> - Scheduled administration times for the order have been changed

\*\*\* - Medication Not Due

## Missing Dose Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Missing Dose Request* \[PSB MISING DOSE REQUEST\] option was removed by patch PSB\*3\*70.

## ## Medication Variance Log Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the *Medication Variance Log* \[PSBO MV\] option, Nursing personnel can print or display exceptions to the medication administration and removal process. The report can be run by patient, or by ward, as shown in Exhibit 29, Medication Variance Log Report by Patient, and Exhibit 30, Medication Variance Log Report by Ward.

- This report provides users with more “event” information within a selected date range, such as the type and number of events, and the total percentage of events that occurred. A variance preceded by a minus sign (such as –24) indicates the number of minutes a medication was given *before* the administration time.

To print a Medication Variance Log Report:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 11, and then press \<Enter\> to access the *Medication Variance Log* \[PSBO MV\] option.
2.  See Section 3.2, “Using ScreenMan Format to Request a Report,” for instructions about requesting a Medication Variance Log.

<span id="med_variance_log_report" class="anchor"></span>Exhibit 19: Medication Variance Log Report by Patient

================================================================================================================================

MEDICATION VARIANCE LOG for May 11, 2016@00:01 to May 13, 2016@24:00 Run Date: MAY 20, 2016@16:20

Include Inpatient Orders Only Page: 1

Patient: TESTPATIENT,FOUR : 666-12-2223 DOB: JAN 22,1972 (44)

Sex: FEMALE Ht/Wt: \*/\* Ward: GEN MED Rm: B-4

Dx: Undetermined back pain Last Mvmt: SEP 28,2015@11:48:24 Type: ADMISSION

ADRs: No ADRs on file.

Allergies: BEE STING

================================================================================================================================

Event Date/Time Event Var Medication

--------------------------------------------------------------------------------------------------------------------------------

MAY 11, 2016@17:55:49 EARLY/LATE DOSE 175 ASPIRIN

Ward: GEN MED B-4

Comments: 05/11/16 17:55 By: NSS TEST

MAY 11, 2016@11:56:10 EARLY/LATE REMOVE 86 SELEGILINE

Ward: GEN MED B-4

Comments: 03/28/16 13:39 By: NSS TEST

05/11/16 17:56 By: NSS Removed: TEST

MAY 11, 2016@07:56:07 EARLY/LATE REMOVE -59 SCOPOLAMINE

Ward: GEN MED B-4

Comments: 02/29/16 14:23 By: NSS TEST

05/11/16 17:56 By: NSS Removed: TEST

MAY 12, 2016@O9:16:55 EARLY/LATE DOSE 199 NICOTINE

Ward: GEN MED B-4

Comments: 05/11/16 18:16 By: NSS test

05/11/16 18:23 By: NSS Removed: SET

MAY 12, 2016@18:17:16 EARLY/LATE DOSE -163 ASPIRIN

Ward: GEN MED B-4

Comments: 05/12/16 18:17 By: NSS test

MAY 13, 2016@12:17:38 EARLY/LATE DOSE 43 ASPIRIN

Ward: GEN MED B-4

Comments: 05/11/16 18:17 By: NSS test

Comments: 05/12/16 08:42 By: NSS test

05/13/16 18:22 By: NSS Removed: TEST

MAY 13, 2016@08:42:27 EARLY/LATE DOSE -128 LIDOCAINE

Ward: GEN MED B-4

Comments: 05/12/16 08:42 By: NSS test

Total Number of Events for the reporting period is: 7.

Total number of EARLY/LATE DOSE events is 5.

Percentage of Total Events: 71%

Total number of EARLY/LATE REMOVE events is 2.

Percentage of Total Events: 29%

================================================================================================================================

TESTPAT,THREE 666-12-2223 Ward: GEN MED Room-Bed: B-4

<span id="_Toc459639966" class="anchor"></span>Exhibit 20: Medication Variance Log Report by Ward

## Drug File Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Drug File Inquiry* \[PSB DRUG INQUIRY\] option lets Nursing and Pharmacy personnel check the bar-coded Internal Entry Number (IEN) Code listed on dispensed Unit Dose medications. This is particularly useful in helping resolve discrepancies when the incorrect bar code is affixed to a medication.

On a medication bar code, the IEN appears on the first line next to the Drug name. Any additional synonyms loaded into Pharmacy Data Management V. 1.0 also appear under the Synonym heading of this option.

To run a drug file inquiry:

1.  At the “Select Medication Administration Menu Nursing Option:” prompt, type 12, and then press \<Enter\> to access the *Drug File Inquiry* \[PSB DRUG INQUIRY\] option.
2.  At the “Select DRUG:” prompt, as shown in Exhibit 31, Drug File Inquiry Screen 1, type the name and dosage of the drug, and then press \<Enter\>.
- You can display a list by entering a ? at the “Select DRUG:” prompt, and then pressing \<Enter\>. The Drug File information will display, as illustrated in Exhibit 32, Drug File Inquiry Screen 2.

<span id="_Toc454692582" class="anchor"></span>Exhibit 21: Drug File Inquiry Screen 1

![](bcma-version-3-nursing-chui-user-manual/009.png)

<span id="_Toc454692583" class="anchor"></span>Exhibit 22: Drug File Inquiry Screen 2

![](bcma-version-3-nursing-chui-user-manual/010.png)

- The IEN displays on the first line, to the right of the Drug Name. The IEN is unique to this drug file entry. In most cases, it is the bar-coded number on the Unit Dose packages that are created in the Pharmacy. Manufacturers’ National Drug Code (NDC) bar codes may display at the “SYNONYMS:” prompt of this display. If the drug is Non-Formulary (N/F), the “Non-Formulary:” prompt will be set to N/F.

# # glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains definitions for acronyms and terms used throughout this manual.

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|       |                                                                                          |
|-------|------------------------------------------------------------------------------------------|
| ADR   | Adverse Drug Reaction.                                                       |
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

## Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ADR</td>
<td>Adverse Drug Reaction. Any response to a drug which is noxious and unintended, and which occurs at doses normally used in humans for treatment, diagnosis, or therapy of a disease, or for modifying physiological functions, including toxicity caused by overdose, drug interaction, drug abuse, drug withdrawal, significant failure of expected action, food-drug interaction, or allergy.</td>
</tr>
<tr class="even">
<td>Administration History Report</td>
<td>A report in CPRS that lists the date, time, and orderable item of a medication highlighted on the CPRS Meds Tab. This report is called “Medication History Report” in BCMA.</td>
</tr>
<tr class="odd">
<td>Audits</td>
<td>The process that tracks the activities of nurses administering medications, by recording selected types of events in the patient’s Medication Log.</td>
</tr>
<tr class="even">
<td>BCMA</td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> software application used in VAMCs for validating patient information and medications against active medication orders <em>before</em> being administered to a patient.</td>
</tr>
<tr class="odd">
<td>Clinician</td>
<td>VAMC personnel who administer active medication orders to patients on a ward. In a VAMC, a number of teams may be assigned to take care of one ward, with specific rooms and beds assigned to each team.</td>
</tr>
<tr class="even">
<td>Completed</td>
<td>This status for an IV bag indicates that the infusion has been completed, and the bag is being taken down or replaced with a new bag. No additional actions may be taken on a bag marked as “Completed,” other than to enter comments.</td>
</tr>
<tr class="odd">
<td>Continuous Order</td>
<td>A medication given continuously to a patient for the life of the order, as defined by the order Start and Stop Date/Time.</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, managers, quality assurance staff, and researchers use this integrated record system.</td>
</tr>
<tr class="odd">
<td>Dispensed Drug</td>
<td>A drug whose name has the strength associated with it (e.g., Acetaminophen 325 mg). The name without the strength is called the “Orderable Item Name.”</td>
</tr>
<tr class="even">
<td>Due List Report</td>
<td>A report that provides detailed information about active <em>and</em> future Unit Dose and IV medication orders that are “due” for administering to a patient during a time frame that you specify within a 24-hour period.</td>
</tr>
<tr class="odd">
<td>Given</td>
<td>When a medication is administered to a patient, it is considered to be “Given” and marked as such (with a “G”) in the Status column of the VDL.</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphical User Interface. The type of interface chosen for BCMA.</td>
</tr>
<tr class="odd">
<td>Held</td>
<td>When a medication is not actually taken by a patient, it is considered to be “Held” and marked as such (with an “H”) in the Status column of the VDL. Reasons might include the patient being temporarily off the ward. You can select and mark multiple medications as Held on the VDL using the Right Click drop-down menu. In the case of IV bags, this status indicates that the dose was Held. The only actions available for this type of IV bag are to mark the bag as Infusing or Refused, or to submit a Missing Dose Request to the Pharmacy.</td>
</tr>
<tr class="even">
<td>Hold</td>
<td>To display a medication order grayed out on the VDL until its Stop Date/Time or until it is Given. Some medical centers require that a nurse mark these order types as “Held,” although it is <em>not</em> necessary that they do so.</td>
</tr>
<tr class="odd">
<td>IEN Code</td>
<td>The internal entry drug number entered by Pharmacy personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</td>
</tr>
<tr class="even">
<td>Infusing</td>
<td>This status, for an IV bag, indicates that the bag is actively being infused. A nurse can enter a comment by right clicking on the bag. If an IV bag is scanned, the only allowable actions are to mark the IV bag as Stopped or Completed.</td>
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
</tbody>
</table>

|                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Missing Dose                  | A medication considered “Missing.” BCMA automatically marks this order type (with an “M”) in the Status column of the VDL after you submit a Missing Dose Request to the Pharmacy. If an IV bag displayed in the IV Bag Chronology display area of the VDL is *not* available for administration, you may mark the IV bag as a “Missing Dose” using the Missing Dose button or by right clicking the IV bag and selecting the Missing Dose command in the Right Click drop-down menu. |
| Missed Medications Report     | A report that lists information about Continuous and One-Time Unit Dose and IV Piggyback medications that were *not* administered to a patient.                                                                                                                                                                                                                                                                                                                                       |
| National Drug Code            | Also called “NDC,” the number assigned by a manufacturer to each item/medication administered to a patient.                                                                                                                                                                                                                                                                                                                                                                           |
| Not Given                     | The status that a scanned medication marked as “Given,” but *not* actually taken by a patient, is changed to on the VDL – by using the “Undo-Given” option. The administration will display on the VDL as it appeared *before* it was marked as “Given.” BCMA notes the status change only in the Audit Trail section of the Medication Log (*not* on the VDL).                                                                                                                       |
| NOW Order                     | A medication order given ASAP to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.                                                                                                                                                                                                                                                               |
| On-Call Order                 | A specific order or action dependent upon another order or action taking place *before* it is carried out. For example, “Cefazolin 1gm IVPB On Call to Operating Room.” Since it may be unknown when the patient will be taken to the operating room, the administration of the On-Call Cefazolin is dependent upon that event.                                                                                                                                                       |
| One-Time Order                | A medication order given one time to a patient such as a STAT or NOW order. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time or until it is Given.                                                                                                                                                                                                                                                                    |
| Orderable Item                | A drug whose name does NOT have the strength associated with it (e.g., Acetaminophen 325 mg). The name with a strength is called the “Dispensed Drug Name.”                                                                                                                                                                                                                                                                                                                           |
| PRN Effectiveness List Report | A report that lists PRN medications administered to a patient that needs Effectiveness comments.                                                                                                                                                                                                                                                                                                                                                                                      |
| Provider                      | Another name for the “Physician” involved in the presecription of a medication (i.e., Unit Dose or IV) to a pateint.                                                                                                                                                                                                                                                                                                                                                                  |
| PSB CPRS MED BUTTON           | The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and medication orders using the CPRS Med Order Button on the BCMA VDL.                                                                                                                                                                                                                                                                                                        |

|                 |                                                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSB INSTRUCTOR  | The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.                                                                                                                                                                         |
| PSB MANAGER     | The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.                                                                                                                                                                                                        |
| PSB STUDENT     | The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options with BCMA V. 3.0. This key requires that a nursing instructor sign on to BCMA V. 3.0.                                                                                                     |
| Refused         | The status for an IV bag or Unit Dose to indicate that the patient refused to take the dose.                                                                                                                                                                                                                                           |
| Removed         | The status for a patch (i.e., Nitroglycerin, Fentanyl, or Nicotine) to indicate that it has been removed from a patient. Once removed, the letters “RM” (for “Removed”) display in the Status column of the VDL.                                                                                                                       |
| Schedule        | The frequency at which a medication is administered to a patient. For example, QID, QD, QAM, Q4H.                                                                                                                                                                                                                                      |
| Schedule Type   | Identifies the type of schedule (i.e., Continuous, PRN, On-Call, and One-Time) for the medication being administered to a patient.                                                                                                                                                                                                     |
| Security Keys   | Used to access specific options within BCMA that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.                                                                                                                                                                         |
| Start Date/Time | The date and time that a medication is scheduled for administration to a patient.                                                                                                                                                                                                                                                      |
| STAT Order      | A medication order given immediately to a patient, entered as a One-Time order by providers and pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.                                                                                                         |
| Status          | A code used to inform a clinician about the condition or progress of a medication order. For Unit Dose and IVP/IVPB orders, status codes include G=Given, H=Held, R=Refused, M=Missing, and RM=Removed (patch removal only). For IV orders, status codes include I=Infusing, H=Held, R=Refused, S=Stopped, C=Completed, and M=Missing. |
| Stop Date/Time  | The date and time that a medication order will expire, and should no longer be administered to a patient.                                                                                                                                                                                                                              |
| Stopped         | This status, for an IV bag, indicates that the IV bag was scanned as Infusing, but was then stopped by a nurse. An IV bag may be stopped and restarted for a variety of reasons. The only actions allowed on a “Stopped” IV bag is to mark the bag as Infusing, Completed, Held, or Refused.                                           |
| Unit Dose       | A medication given to a patient, such as tablets or capsules.                                                                                                                                                                                                                                                                          |
| VDL             | An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA.                                                                                                                                         |

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Verify           | When a nurse or a pharmacist confirms that a medication order is accurate and complete, according to the information supplied by the provider.   |
| Virtual Due List | Also called “VDL,” an on-line list used by clinicians when administering active medication orders to a patient. This is the Main Screen in BCMA. |

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA
On-line Help, 3
GUI Options, 5, 17
<span class="smallcaps">Sample reports</span>
<span class="smallcaps">Administration Times report by Patient</span>, 16
<span class="smallcaps">Administration Times report by Ward</span>, 16
<span class="smallcaps">Due List Report by Patient</span>, 19, 20
Medication Administration History Report by Patient, 31
<span class="smallcaps">Medication Administration Log Report by Patient</span>, 9
Medication Administration Log Report by Ward, 10
Medication Variance Log Report by Patient, 32
Medication Variance Log Report by Ward, 33
Missed Medications Report by Patient, 13
Missed Medications Report by Ward, 14
PRN Effectiveness List Report by Patient, 21
PRN Effectiveness List Report by Ward, 22
Sample screens
Administration Time Selection Screen, 28
BCMA Nursing Option Menu, i, 5
Drug File Inquiry Screen 1, 34
Drug File Inquiry Screen 2, 35
<span class="smallcaps">Due List Report Request Screen</span>, 17
Manual Medication Entry Medication Selection Screen, 27
Manual Medication Entry Patient Selection Screen, 26
Medication Log Manual Entry Screen, 29
Medication Selection Screen, 24
Patient Selection Screen, 23
PRN Effectiveness Entry Screen, 25
<span class="smallcaps">Using ScreenMan Format to Request a Report</span>, 6
Using the Nursing Menu Options
Drug File Inquiry, 34
Due List, 17
Edit Medication Log, 14
Enter PRN Effectiveness, 22
Manual Medication Entry, 26
Medication Administration History (MAH), 30
Medication Administration Log, 8
Medication Administration Log Report, 8
Medication Variance Log, 32
Missed Medications, 12, 13, 14
Missed Medications Report, 12
PRN Effectiveness List Report, 21
Ward Administration Times, 5
Ward Administration Times Report, 15
