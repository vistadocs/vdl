---
title: PSO*7*200/PSS*1*122 FY07 QTR 2 Release Notes - FY07 Q2
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*200
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - address
  - scriptalk
  - pharmacy
  - label
  - device
  - printer
  - enhancements
  - print
page_count: 0
word_count: 1250
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p200_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p200_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-200-pss-1-122-fy07-qtr-2-release-notes-fy07-q2/001.png)

PHARMACY FY07 Q2

> RELEASE NOTES

> PSO\*7\*200 PSS\*1\*122

> Version 7.0

> Version 1.0

> April 2007

> Department of Veterans Affairs

> VistA Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
- [OPAI Enhancements](#opai-enhancements)
  - [Example:](#example)
  - [When the permanent address is active:](#when-the-permanent-address-is-active)
  - [When the temporary address is active:](#when-the-temporary-address-is-active)
  - [When the address is flagged as BAI:](#when-the-address-is-flagged-as-bai)
- [Laser Label Enhancements](#laser-label-enhancements)
- [Miscellaneous Enhancements](#miscellaneous-enhancements)
  - [Example activity log entry:](#example-activity-log-entry)
  - [Example:](#example-1)
- [Pharmacy Data Management V. 1.0](#pharmacy-data-management-v-10)
- [PDM Enhancements](#pdm-enhancements)
> The Pharmacy Fiscal Year 2007 Quarter 2 (FY07 Q2) release includes updates in PSO\*7\*200 and PSS\*1\*122. These patches include software enhancements and defect fixes.
> For installation instructions, see the patch description for the appropriate package.
> *(This page included for two-sided copying.)*

# Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The FY07 Q2 release includes updates for Outpatient Pharmacy Automation Interface (OPAI), Laser Labels, defect fixes, and other miscellaneous enhancements.

# OPAI Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Outpatient Pharmacy software is modified to use the new commercial warning label source to send the warning label text to the automated filling equipment. The OPAI WARNING LABEL SOURCE field (#16.2) in the PHARMACY SYSTEM file (#59.7) must be set to “N” for “New” to send the warning labels from the new commercial data source to OPAI. It can be set by using the *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] option.

## Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The warning text is sent as one record per warning.
- The text is sent in English or Spanish, depending on the patient’s other language settings.
- If the DEA, SPECIAL HDLG field (#3) in the DRUG file (#50) begins with numbers 1,2,3,4, or 5, the NO TRANSFER warning text from the RX CONSULT file (#54) entry number 20 is automatically sent as one of the first 5 warnings when the OPAI WARNING LABEL SOURCE is set to “New”.

> If the BAD ADDRESS INDICATOR (BAI) field (#.121) of the PATIENT file (#2) is set, the text “VAB” concatenated with the BAI code is sent in the Address field of the PID segment of the HL7 message to the filling equipment.

> Here are some examples of this field:

## When the permanent address is active:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PADD-1~PADD-2~SPRING~TX~77379\~~P~PADD-3~201^\~~""~""\~\~~N\|""\|\|\|\|\|\|\|

> \|

## When the temporary address is active:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PADD-1~PADD-2~SPRING~TX~77379\~~P~PADD-3~201^\~~""~""\~\~~N^TADD-1~TADD-2

> TADD-3~PLANO~TX~12345\~~C\~~""\~\~~

## When the address is flagged as BAI:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PADD-1~PADD-2~SPRING~TX~77379\~~VAB1~PADD-3~201^\~~""~""\~\~~N\|""\|\|\|\|\|\|

> \|\|\|

> “VAB1” - indicates Bad Address Indicator and 1 is for UNDELIVERABLE (2 for HOMELESS, 3 for OTHER)

# Laser Label Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following changes were made to the Outpatient Pharmacy V. 7.0 software.

- Print the last 4 digits of the Social Security Number (SSN) instead of the last 6 digits.
- Change the name on the mailing label back to Last name,First name format.
- On the Pharmacy Fill Card portion of the label, replace the text “Mfr ” with:

> NDC/MFR (for non-ePharmacy sites) or

> NDC nnnnn-nnnn-nn (for ePharmacy sites)

- Signature log enhancements include:
  - Print current date at top
  - Do not print user name (if more than 1 prescription was included to be signed, the user name could be different for each one).
  - Correct the spacing and continuation paging issues if one or more of the prescriptions has been discontinued before printing the signature log.
  - Add a barcode to enable scanning to remove the patient's name from the Bingo Board.
  - Add as much of the drug name as will fit on the label.
  - While printing original labels (not reprint of the signature log), if all of the fills have a routing of mail, the signature log will not be printed.
  - The line "Relationship Counseled? " is changed to "Relation Counseling Refused Accepted ".
- When a fill is released, if the BAI is no longer set or there is an active temporary address, the "B" is removed from the status column of the patient profile. (This is removed by making an additional entry in the label log. The "B" comes from the "last" entry having a bad address condition at the time the label printed).

# Miscellaneous Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To address ELECTRONIC Error & Enhancement Report (E3R) 19820, the following code changes are included:

- Added the capability to tie a ScripTalk® printer to regular Pharmacy label printer(s) to control where the ScripTalk labels print for multi-divisional sites. The new SCRIPTALK PRINT DEVICE MAPPING multiple (#47) in PHARMACY SYSTEM file (#59.7) has been created to store this information in Pharmacy Data Management patch PSS\*1\*122. The multiple contains LABEL PRINTER TO BE MAPPED field (#.01) and SCRIPTALK DEVICE field (#.02).

> The added functionality works in conjunction with the existing ScripTalk divisional functionality, so a divisional ScripTalk device must be defined. If no mapping is defined in the new fields, ScripTalk labels will continue to print on the printer defined for the division. If a pharmacy printer is mapped to a ScripTalk printer, the ScripTalk label will automatically be printed on the mapped ScripTalk printer.

- Modify the *ScripTalk Device Definition Enter/Edit* \[PSO SCRIPTALK DEVICE DEF'N\] option to allow definition of printer mapping for ScripTalk devices.

> The user will be prompted to define the ScripTalk printer by division or by printer mapping. After selecting D for division, the divisional definition has not changed.

> After selecting P for printer mapping, the user will be prompted "LABEL PRINTER TO BE MAPPED". The device entered into this field corresponds to the label printer selected during Pharmacy login and/or the printer selected during print from suspense functions.

> Next, "SCRIPTALK DEVICE" will be prompted, and this field should contain the ScripTalk printer to be mapped to the regular label printer.

> The following enhancements are included in the FY07Q2 release:

- A new field FINISH DATE/TIME field (#38.3) is added to the PRESCRIPTION file (#52).
- When using the *Print from Suspense File* \[PSO PNDLBL\] option, if the routing is not WINDOW and the BAD ADDRESS INDICATOR (#.121) field of the PATIENT file (#2) is set (value of 1=UNDELIVERABLE, 2=HOMELESS, 3=OTHER) and the patient does not have an active temporary address, the prescription fill will not be sent to automated filling equipment and/or to the label printer.

> Also, if the fill’s routing is mail and the patient’s MAIL field (#.03) in the PHARMACY PATIENT file (#55) is set to "DO NOT MAIL" and the current date is before the MAIL STATUS EXPIRATION DATE field (#.05) in the PHARMACY PATIENT file (#55), the label will not print and the fill will not be sent to the automated filling equipment.

> The first time a prescription is not sent/label printed, a MailMan message will be generated to the user who queued the print from suspense and the members of the PSO EXTERNAL DISPENSE ALERTS mail group. An entry will also be set in the PRESCRIPTION file (#52) activity log.

## Example activity log entry:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example MailMan message:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 51%" />
<col style="width: 5%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="2"></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th colspan="2"><p>Subj: 500 BAD ADDRESS SUSPENSE NOT PRINTED [#169828] 02/26/07@07:30</p>
<p>lines</p>
<p>From: OUTPATIENT PHARMACY PACKAGE In 'IN' basket. Page 1</p></th>
<th><blockquote>
<p>11</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><p>The following prescriptions with a routing of mail were not printed/sent to external interface due to the BAD ADDRESS INDICATOR being set and</p>
<p>no active temporary address or patient has an active MAIL status of DO NOT MAIL:</p></th>
</tr>
<tr class="odd">
<th colspan="3"><p>OPPATIENT,ONE 000001234 (BAD ADDRESS INDICATOR) 100002608 (1) A AND Z OINTMENT</p>
<blockquote>
<p>100002609 (0) ASPIRIN 325MG TABS</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3">OPPATIENT,FOUR 000004321 (DO NOT MAIL) 100002654A (0) BACITRACIN OINTMENT 1OZ</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Modify the report from the *Bad Address Suspended List* \[PSO BAI SUSPENDED\] option to allow printing by more than one division and also include prescriptions suspended for Consolidated Mail Outpatient Pharmacy (CMOP). This report is also changed to not prompt for a start date.

## Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Suspense bad address report - division = ALL for suspense dates through MAR 01, 2007</th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="3"><p>OPPATIENT,TEN (00-0187)</p>
<p>MAR 01, 2007 Rx#: 301054 CIMETIDINE 200MG TAB</p>
<p>MAR 01, 2007 Rx#: 301055 COAL TAR 5% GEL 3 OZ TUBE</p></th>
</tr>
<tr class="header">
<th colspan="3"><p>OPPATIENT,FIVE (00-0773)</p>
<p>FEB 27, 2007 Rx#: 100002655 BACITRACIN OINTMENT 1OZ</p></th>
</tr>
<tr class="odd">
<th colspan="3"><p>End of Report.</p>
<p>Press Return to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- At the request of the Computerized Patient Record System (CPRS) package development team, the following were added to the Application Program Interface (API) PSOHCSUM:
  - PLACER ORDER \# field (#39.3) of the PRESCRIPTION file (#52)
  - Letter "R" when the original fill is returned to stock

> For more details please see the IA (Integration Agreement) \#330.

# Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The FY07 Q2 release includes updates for OPAI through the patch PSS\*1\*122.

# PDM Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following data dictionary additions are included for PHARMACY SYSTEM file (#59.7) and supports modifications made in Outpatient Pharmacy patch PSO\*7\*200.

- SCRIPTALK PRINT DEVICE MAPPING multiple (#47) - adds the capability to tie a ScripTalk printer to regular Pharmacy label printer(s) to control where the ScripTalk labels print for multi- divisions. Multiple print devices may be mapped to a ScripTalk printer, and any device defined must have a subtype prefixed with "P-". This prefix in the subtype indicates that the device is a printer. If no data is defined in this multiple, the ScripTalk printer tied to the division will be used. The use of this multiple builds upon existing ScripTalk functionality, so a divisional ScripTalk device must be defined for the mapped device functionality to work properly and to have a default device defined.

> Updated fields include:

- LABEL PRINTER TO BE MAPPED field (#.01) - This field contains the Pharmacy label printer(s) that the ScripTalk device is mapped. When the printer device defined in this field is selected as the Pharmacy print device by the user, ScripTalk labels will print on the corresponding mapped ScripTalk device.
- SCRIPTALK DEVICE field (#.02) - This field contains the ScripTalk print device that will be tied to regular Pharmacy label device(s) defined in the LABEL PRINTER TO BE MAPPED field (#.01).

> *(This page included for two-sided copying.)*