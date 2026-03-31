---
title: Controlled Substances Version 3 Package Security Guide (Updated PSD*3*82)
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Package  (Updated PSD*3*82)
app_code: PSD
app_name: "Pharmacy: Controlled Substances"
section: CLI
app_status: active
pkg_ns: PSD
patch_ver: 3
patch_id: PSD*3
group_key: "PSD:PSD:3"
file_numbers: []
security_keys: []
menu_options: 15
description: ![](controlled-substances-version-3-package-security-guide-updated-psd-3-82/001.png)
audience: 
keywords: 
  - strong
  - class
  - security
  - tech
  - naou
  - package
  - report
  - pharmacy
  - controlled
  - table
page_count: 0
word_count: 1284
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_cssecuri_r0618.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_cssecuri_r0618.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=86"
---

![](controlled-substances-version-3-package-security-guide-updated-psd-3-82/001.png)

CONTROLLED SUBSTANCESPackage Security Guide

Version 3.0.

March 1997

(Revised June 2018)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revised Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>06/2018</td>
<td><a href="#PSD_3_82"><u>2</u></a></td>
<td>PSD*3*82</td>
<td><p>Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2013</td>
<td>i, ii, 2-3</td>
<td>PSD*3*76</td>
<td><p>Added description of patch’s new security key PSDRPH</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>2-3</td>
<td>PSD*3*71</td>
<td><p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td>1-2</td>
<td>PSD*3*69</td>
<td><p>Added description of patch’s new security key PSD TECH ADV. Added Revision History.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Package Security Guide.</td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*Package Security
The Controlled Substances module does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the CS files. Security with respect to standard options in the module is implemented by carefully assigning option to users and through the use of security keys.
Options
All pharmacy personnel can be assigned the *PSD MENU* option as the primary menu option.
Nursing personnel can be assigned the *PSD NURSE MENU* option.
Controlled Substances Inspectors can be assigned the *PSD INSPECTOR MENU* option.
Some stations design their own menus for individual users. If this is the case, then the top level CS menu must contain the following entry and exit code in the OPTION file (#19):
ENTRY ACTION: I’\$D(PSDSITE) D ^PSDSET
EXIT ACTION: K PSDSITE
This entry and exit code must be present because the PSDSITE variable is set as users enter the package. If the Kernel’s ^OPTION NAME feature is used to jump directly into lower levels of the CS package, then the “Inpatient Site Name” prompt must be answered in order to define the PSDSITE variable. All options are independently invocable, however, if the instructions above are not followed, users will be repeatedly asked to select an inpatient site if there are two or more sites flagged for CS use.
Keys
After the users are assigned the primary menu option, it is necessary to give the appropriate security keys to each user as required. There are ten keys associated with CS.
<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PSD ERROR</strong></th>
<th>This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, holders of this key receive electronic mail messages created using the TRAKKER.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PSD NURSE</strong></td>
<td>This key should be allocated to nurses, usually LPNs, who can only receive and administer controlled substances but cannot place the order requests.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>PSD PARAM</strong></td>
<td>This key should be allocated <strong>only</strong> to the Inpatient Pharmacy Package Coordinator or his/her designee. This key controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).</td>
</tr>
<tr class="even">
<td><strong>PSD TECH</strong></td>
<td>Allocate this key to control substance technicians. This key controls access to the <em>List On-Hand Amounts</em> [PSD ON-HAND TECH], <em>Transfer Drugs between Dispensing Sites Report</em> [PSD PRINT VAULT TRANSFERS TECH], and the <em>Daily Activity Log (in lieu of VA FORM 10-2320)</em> [PSD DAILY LOG TECH] options on the Technician (CS Pharmacy) Menu [PSD PHARM TECH].</td>
</tr>
<tr class="odd">
<td><strong>PSD TECH</strong> <strong>ADV</strong></td>
<td>Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the <em>Receipts Into Pharmacy</em> [PSD RECEIPTS MENU], <em>Dispensing Menu</em> [PSD DISPENSING MENU], <em>Destructions Menu</em> [PSD DESTROY MENU], <em>Manufacturer, Lot #, and Exp. Date - Enter/Edit</em> [PSD MFG/LOT/EXP], <em>Outpatient Rx's</em> [PSD OUTPATIENT], <em>Complete Green Sheet</em> [PSD COMPLETE GS], <em>Destroyed Drugs Report</em> [PSD DEST DRUGS REPORT], <em>DEA Form 41 Destroyed Drugs Report</em> [PSD DESTROY DEA41], <em>Destructions Holding Report</em> [PSD DESTRUCTION HOLDING], <em>Add Existing Green Sheets at Setup</em> [PSD EXISTING GS], <em>Green Sheet Transfer Between NAOUs Report</em> [PSD GS TRANSFER (NAOU) REPORT], <em>NAOU</em> <span id="PSD_3_82" class="anchor"></span><em>Usage Report</em> [PSD NAOU USAGE], <em>Transfer Drugs between Dispensing Sites</em> [PSD TRANSFER VAULT DRUGS] options on the <em>Technician (CS Pharmacy) Menu</em> [PSD PHARM TECH]. The CS technician may perform all functions of the <em>Outpatient Rx’s</em> [PSD OUTPATIENT] option except releasing prescriptions.</td>
</tr>
<tr class="even">
<td><strong>PSD TRAN</strong></td>
<td>This key should be allocated <strong>only</strong> to the Inpatient Pharmacy Package Coordinators. This key controls access to the <em>NAOU to NAOU Transfer Stock Entries</em> [PSD TRANSFER NAOU] option. Users can copy the stock entries from one NAOU into other NAOUs or from AR/WS AOU into an NAOU.</td>
</tr>
<tr class="odd">
<td><p><strong>PSDMGR</strong></p>
<p><strong>PSDRPH</strong></p>
<p><strong>PSJ PHARM TECH</strong></p>
<p><strong>PSJ RNURSE</strong></p></td>
<td><p>Allocate this key to the Inpatient Pharmacy Coordinators. This key controls the editing of CS files for package set up and it locks the <em>Supervisor (CS) Menu</em> option.</p>
<p>This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.</p>
<p>This key should be allocated to pharmacy technicians handling narcotic orders.</p>
<p>This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>PSJ RPHARM</strong></td>
<td>This key should be allocated to pharmacists dispensing and receiving narcotic orders.</td>
</tr>
</tbody>
</table>
Hardware Requirements
The following equipment is recommended to successfully implement Version 3.0
Intermec TRAKKER 9440 (Barcode Reader)
HP LaserJet III (or any compatible laser printer)
VT320 (bi-directional only) or any bi-directional flow CRT
The laser single sheet feed printer is required to print the VA FORM 10-2638 and barcode ID labels. It is recommended that the printer be physically located in the narcotic vault for efficiency and security.
*(This page included for two-sided copying.)*
