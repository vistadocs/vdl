---
title: PSB*3*2 BCMA Version 3 Pharmacy CHUI User Manual Change Pages
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: BCMA Version 3 Pharmacy CHUI  Change Pages
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*2
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 1
description: - [Revision History](#revision-history) - [BCMA Menu—Pharmacy Option](#bcma-menupharmacy-option) - [Using the Medication Administration Menu Pharmacy Option](#using-the-medication-administration-menu-pharmacy-option) - [Using ScreenMan Format to Request a Report](#using-screenman-format-to-request-a
audience: 
keywords: 
  - report
  - label
  - exhibit
  - prompt
  - press
  - pharmacy
  - dose
  - strong
  - code
  - table
page_count: 0
word_count: 2358
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p2_chui_um_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p2_chui_um_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

PHARMACY CHUI USER MANUAL

February 2004

(Revised March 2008)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [BCMA Menu—Pharmacy Option](#bcma-menupharmacy-option)
  - [Using the Medication Administration Menu Pharmacy Option](#using-the-medication-administration-menu-pharmacy-option)
  - [Using ScreenMan Format to Request a Report](#using-screenman-format-to-request-a-report)
  - [Label Print](#label-print)
  - [Barcode Label Print](#barcode-label-print)
- [INDEX](#index)
Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revised Pages</td>
<td>Patch Number</td>
<td>Description</td>
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
TABLE OF CONTENTS
1 INTRODUCTION 1
1.1 What is BCMA? 1
1.2 Features of BCMA 1
2 About This Manual 3
2.1 Special Notations—Documentation Conventions 3
2.2 Package Conventions 3
2.3 Intranet Documentation 3
2.4 On-line Help 3
3 BCMA Menu—Pharmacy Option 5
3.1 Using the Medication Administration Menu Pharmacy Option 5
3.2 Using ScreenMan Format to Request a Report 6
3.3 Medication Administration Log Report 8
3.4 Missed Medications Report 11
3.5 Due List Report 15
3.6 Medication Administration History (MAH) Report 19
3.7 Missing Dose Request 21
3.8 Missing Dose Followup 25
3.9 Missing Dose Report 28
3.10 Label Print 31
3.11 Drug File Inquiry 33
3.12 Barcode Label Print 34a
glossary 35
INDEX 41
TABLE OF EXHIBITS
Exhibit 1: BCMA Pharmacy Option Menu Screen 5
Exhibit 2: Report Request Using ScreenMan Format Screen 6
Exhibit 3: Medication Administration Log Report Screen 8
Exhibit 4: Medication Administration Log Report by Patient 9
Exhibit 5: Medication Administration Log Report by Ward 10
Exhibit 6: Missed Medications Report Screen 12
Exhibit 7: Missed Medications Report By Patient 13
Exhibit 8: Missed Medications Report By Ward 14
Exhibit 9: Due List Report Request Screen 15
Exhibit 10: Due List Report by Patient 17
Exhibit 11: Due List Report by Ward 18
Exhibit 12: Medication Administration History Report by Patient 20
Exhibit 13: Missing Dose Request Screen 21
Exhibit 14: Missing Dose Request Confirmation Screen 23
Exhibit 15: Missing Dose E-mail Notification 24
Exhibit 16: Missing Dose Followup Request Screen 25
Exhibit 17: Missing Dose Request Pharmacy Follow-up Information Screen 26
Exhibit 18: Pharmacy Reasons Needed Selection Table 27
Exhibit 19: Missing Dose Report Request Screen 28
Exhibit 20: Missing Dose Report 30
Exhibit 21: Bar Code Label Screen 31
Exhibit 23: Drug File Inquiry Screen 1 33
Exhibit 24: Drug File Inquiry Screen 2 34
Exhibit 25: Bar Code Label Print Screen 34a
Exhibit 26a: Sample Unit Dose Bar Code Label 34b
Exhibit 26b: Sample Ward Stock Bar Code Label 34b

# BCMA Menu—Pharmacy Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using the Medication Administration Menu Pharmacy Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA Pharmacy Option Menu, as illustrated in Exhibit 1, lets Pharmacy personnel access information that has been entered via the BCMA Graphical User Interface (GUI) VDL. Because BCMA operates in real time, scanned information is available as soon as the scan is successfully completed. You can access the Pharmacy Option Menu from any VistA-enabled terminal within the VAMC.

Several of these options are available under both the Nursing and the Pharmacy menu options. The options that are unique to Pharmacy include Missing Dose Follow-up, Missing Dose Report, Label Print, and Barcode Label Print.

#### <span class="smallcaps">Exhibit 1: BCMA Pharmacy Option Menu Screen</span>

![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/002.png)

To select a Pharmacy option:

1.  At the “Select Medication Administration Menu Pharmacy Option:” prompt, enter the number of the desired option.
2.  Press \<Enter\> to display the Sort Screen for the option chosen.

## Using ScreenMan Format to Request a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many of the Pharmacy options use a common screen to define selection criteria for reports, as illustrated in Exhibit 2, Report Request Using ScreenMan Format Screen. Other options use specific screens. This section explains the screen prompts for all reports using the Report Information Sort Screen and gives instructions for entering information. Following this section are sample reports that you can run from each of the Medication Administration Menu Pharmacy options.

#### <span class="smallcaps">Exhibit 2: Report Request Using ScreenMan Format Screen</span>

![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/003.png)

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

## Label Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *Label Print* \[PSBO BL\] option for printing individual or batch Unit Dose bar code labels. It is specifically coded to the Zebra-brand printers using the Zebra Programming Language (ZPL). Model 105SE was used in the development of the labels. Routine \[PSBOBL\] uses site-specific printers or terminals to produce labels.

#### ![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/004.png)<span class="smallcaps">Exhibit 21: Bar Code Label Screen</span>

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

## Barcode Label Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 includes the *Barcode Label Print* \[PSBO BZ\] option for printing individual or batch Unit Dose bar code labels. This option allows the user to have the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBZ uses site-specific printers or terminals to produce labels.

#### <span class="smallcaps">Exhibit 25: Bar Code Label Print Screen</span>

![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/005.png)

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
15. At the “\<RET\> Re-Edit:” prompt, press PF1 - E to print the label, PF1 - Q to Quit or PF1 - R to refresh the screen. Sample labels are shown in the Exhibits below.

#### <span class="smallcaps">Exhibit 26a: Sample Unit Dose Bar Code Label</span>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Drug: BACLOFEN 10MG TABS (Qty: 1)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dose:25MG</strong></td>
<td rowspan="2"><p><strong>Patient: BCMAPATIENT,ONE</strong></p>
<p><strong>Ward: GEN MED</strong></p>
<p><strong>Lot: 123141</strong></p>
<p><strong>Exp: 4/5/2006 Mfg: DRUGCO</strong></p>
<p><strong>Filled/Checked By: XX/XX</strong></p></td>
</tr>
<tr class="even">
<td><p>![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/006.png)</p>
<p>*500-2564*</p></td>
</tr>
</tbody>
</table>

#### <span class="smallcaps">Exhibit 26b: Sample Ward Stock Bar Code Label</span>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Drug: BACLOFEN 10MG TABS (Qty: 1)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dose:25MG</strong></td>
<td rowspan="2"><p><strong>Patient:</strong></p>
<p><strong>Ward:</strong></p>
<p><strong>Lot: 123141</strong></p>
<p><strong>Exp: 4/5/2006 Mfg: DRUGCO</strong></p>
<p><strong>Filled/Checked By:_______/_______</strong></p></td>
</tr>
<tr class="even">
<td><p>![](psb-3-2-bcma-version-3-pharmacy-chui-user-manual-change-pages/007.png)</p>
<p>*500-2564*</p></td>
</tr>
</tbody>
</table>

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acronyms, 35
Bar Code Label, Sample, 34b
Barcode Label Print, 34a
BCMA, 1
On-line Help, 3
BCMA Menu, 5
Documentation Conventions, 3
Drug File Inquiry, 33
Due List Report, 15
Glossary, 35
GUI Options, 5, 15
Missing Dose E-mail Notification, 24
Missing Dose Report, 28
Pharmacy Option Menu, 5
Pharmacy Reasons Needed Selection Table, 27
Sample reports
Due List Report by Patient, 17, 18
Medication Administration History Report by Patient, 20
Medication Administration Log Report by Patient, 9
Medication Administration Log Report by Ward, 10
Missed Medications by Ward Report, 14
Missed Medications Report by Patient, 13
Missed Medications Report Screen, 12
Missing Dose Report, 29, 30
Sample screens
Bar Code Label Print Screen, 34a
Drug File Inquiry Screen 1, 33
Drug File Inquiry Screen 2, 34
Due List Report Request Screen, 15, 25
Missing Dose Follow Up Request Screen, 25
Missing Dose Request Confirmation Screen, 23
Missing Dose Request Pharmacy Follow-up Information Screen, 26
Missing Dose Request Screen, 21
BCMA Pharmacy Option Menu Screen, 5
Medication Administration Log Report Screen, 8
Using ScreenMan Format to Request a Report, 6
Sample Unit Dose Bar Code Label, 34b
Sample Ward Stock Bar Code Label, 34b
Terms, 36
Using the Pharmacy Menu Options
Request a Report, 6
Medication Administration Log Report, 8
Missed Medications Report, 11
Due List, 15
Medication Administration History (MAH), 19
Missing Dose Request, 21, 28
Missing Dose Follow-up, 25
Drug File Inquiry, 33
