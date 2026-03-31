---
title: PSN*4*108 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: PSN
app_name: "Pharmacy: National Drug File (NDF)"
section: CLI
app_status: active
pkg_ns: PSN
patch_ver: 4
patch_id: PSN*4*108
group_key: "PSN:PSN:4"
file_numbers: []
security_keys: []
menu_options: 1
description: - [Version 4.0](#version-40) - [Revision History](#revision-history) - [Files](#files) - [Routines](#routines) - [Exported Options](#exported-options) - [National Drug File V. 4.0 Menu](#national-drug-file-v-40-menu) - [Archiving and Purging](#archiving-and-purging) - [Callable Routines](#callable-r
audience: 
keywords: 
  - blockquote
  - class
  - table
  - contents
  - strong
  - added
  - style
  - width
  - routines
  - even
page_count: 0
word_count: 1658
section_count: 8
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/psn_4_p108_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/psn_4_p108_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=89"
---

> ![](psn-4-108-technical-manual-security-guide-change-pages/001.png)

NATIONAL DRUG FILE (NDF)

> TECHNICAL MANUAL

# Version 4.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Version 4.0](#version-40)
- [Revision History](#revision-history)
  - [Files](#files)
  - [Routines](#routines)
  - [Exported Options](#exported-options)
    - [National Drug File V. 4.0 Menu](#national-drug-file-v-40-menu)
  - [Archiving and Purging](#archiving-and-purging)
  - [Callable Routines](#callable-routines)
  - [External Interfaces](#external-interfaces)
    - [<u>Package</u> <u>Minimum Version Needed</u>](#upackageu-uminimum-version-neededu)
  - [Glossary](#glossary)
> October 1998
> (Revised May 2010)
> Department of Veterans Affairs Office of Enterprise Development

# Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below lists changes made since the initial release of this manual. Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.

> Note: The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/10</td>
<td><p>i-ii, <a href="#_bookmark0"><u>6</u>,</a> <a href="#_bookmark1"><u>7</u>,</a> <a href="#_bookmark2"><u>17-</u></a></p>
<p><a href="#_bookmark2"><u>18</u></a></p></td>
<td><blockquote>
<p>PSN*4*108</p>
</blockquote></td>
<td><p>Added routines PSNFDAMG, and PSNMEDG to the list of routines. Routine PSNAPIS was modified.</p>
<p>Added new option Display FDA Medication Guide [PSN MED GUIDE].</p>
<p>Added FDA Medication Guide to the Glossary.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/09</td>
<td><p>6, 10, 10b,</p>
<p>12e-f</p></td>
<td><blockquote>
<p>PSN*4*169</p>
</blockquote></td>
<td><p>Added routines PSNEN169 and PSNPO169. Described section added to the VA Product message as part of an NDF Management System change.</p>
<p>Updated Notes Regarding Patches section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/06</td>
<td>6</td>
<td><blockquote>
<p>PSN*4*109</p>
</blockquote></td>
<td>Added routine PSN5067 to the list of routines. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/05</td>
<td><p>iii, 6, 10b,</p>
<p>12c-d, 15, 21,</p>
<p>22</p></td>
<td><blockquote>
<p>PSN*4*101</p>
</blockquote></td>
<td>Added routines PSNVUID and PSNPREDS, an explanation of the data standardization project in a new section called Notes regarding Patches; moved changes to CS Federal Schedule field (patch PSN*4*65) to new section; updated Table of Contents, Glossary and Index. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/04</td>
<td>i, 2, 6, 8</td>
<td><blockquote>
<p>PSN*4*80</p>
</blockquote></td>
<td><p>Added routines and a reference to the <em>Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy</p>
<p>Re-Engineering (PRE) project Encapsulation cycle 1</p></td>
</tr>
<tr class="even">
<td>09/03</td>
<td>7</td>
<td><blockquote>
<p>PSN*4*70</p>
</blockquote></td>
<td>-Added two new options to the list of exported options.</td>
</tr>
<tr class="odd">
<td>07/03</td>
<td><p>Title Page,</p>
<p>i-ii, 10b</p></td>
<td><blockquote>
<p>PSN*4*65</p>
</blockquote></td>
<td>- Noted changes to CS Federal Schedule field.</td>
</tr>
<tr class="even">
<td>04/03</td>
<td><p>Title Page,</p>
<p>i, 15</p></td>
<td><blockquote>
<p>PSN*4*20</p>
</blockquote></td>
<td>-Changed the RD access on several files.</td>
</tr>
<tr class="odd">
<td>04/03</td>
<td><p>Title Page,</p>
<p>i, 6</p></td>
<td><blockquote>
<p>PSN*4*68</p>
</blockquote></td>
<td>-Added the PSNPPIO routine to the list of routines.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/03</td>
<td><blockquote>
<p>Title Page, i-iv,</p>
<p>4a-4d, 6</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*62</p>
</blockquote></td>
<td><p>-Replaced the Title Page, Revision History Page, and Table of Contents.</p>
<p>-Added the Patient Medication Information (PMI) Sheet enhancement files and printer set-up.</p>
<p>-Added print routine to the list of routines.</p></td>
</tr>
<tr class="even">
<td>10/02</td>
<td><blockquote>
<p>Title Page, i-iv,</p>
<p>12, 12a, 12b</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*64</p>
</blockquote></td>
<td><p>-Replaced the Title Page (and associated blank page) and the Revision History Page (and associated blank page).</p>
<p>-Added page numbers to the Revision History Pages and Table of Contents Pages.</p>
<p>- Updated the Electronic MailMan Messages for Drugs Unmatched from the National Drug File.</p></td>
</tr>
<tr class="odd">
<td>10/02</td>
<td><blockquote>
<p>Title Page 10, 10a, 10b,</p>
<p>11, 12, 12a,</p>
<p>12b</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*58</p>
</blockquote></td>
<td><ul>
<li><p>Replaced the Title Page (and associated blank page) and the Revision History page (and associated blank page after it.)</p></li>
<li><p>Updated the Electronic MailMan Messages for Data Update for NDF, Updated Interactions, and Drugs Unmatched from National Drug File. This included new screen captures and required the</p></li>
</ul>
<p>addition of new pages.</p></td>
</tr>
<tr class="even">
<td>09/01</td>
<td><blockquote>
<p>Title Page 10-12</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*53</p>
</blockquote></td>
<td><ul>
<li><p>Replaced the Title Page (and associated blank page) and the Revision History page (and associated blank page after it.)</p></li>
<li><p>Added a new Electronic Mail Message for Updated Interactions and added new screen captures for the Electronic Mail Messages for Data Update and Drugs Unmatched from National Drug File.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>02/00</td>
<td><blockquote>
<p>6,7,9</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*22</p>
</blockquote></td>
<td>Added a new option called <em>Inquire to National Files.</em></td>
</tr>
<tr class="even">
<td>10/98</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NATIONAL DRUG file (#50.6) has been redesigned from a file seven multiples deep to a new file structure of four separate files. The new files are the VA PRODUCT file (#50.68), the NDC/UPN file (#50.67), the VA DISPENSE UNIT file (#50.64), and File \#50.6, which is now the VA GENERIC file.

> The files required to run the NDF software are listed below.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE # NAME</th>
<th>UP DATE DD</th>
<th>SEND SEC. CODE</th>
<th>DATA COMES W/FILE</th>
<th><blockquote>
<p>SITE DATA</p>
</blockquote></th>
<th><blockquote>
<p>RSLV PTS</p>
</blockquote></th>
<th>USER OVER RIDE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>50.416 DRUG INGREDIENT</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td>50.6 VA GENERIC</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.605 VA DRUG CLASS</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td><p>50.606 DOSAGE FORM</p>
<p>Partial DD: subDD 50.606 fld: .01</p></td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="odd">
<td>50.607 DRUG UNITS</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td>50.608 PACKAGE TYPE</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="odd">
<td>50.609 PACKAGE SIZE</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td>50.612 NATIONAL DRUG TRANSLATION</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.64 VA DISPENSE UNIT</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td>50.67 NDC/UPN</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.68 VA PRODUCT</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>51.2 MEDICATION ROUTES</p>
<p>Partial DD: subDD 51.2 fld: .01</p></td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td><blockquote>
<p>MERG</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>YES</td>
</tr>
<tr class="odd">
<td>55.95 DRUG MANUFACTURER</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="even">
<td>56 DRUG INTERACTION</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td><blockquote>
<p>OVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="odd">
<td><p>59.7 PHARMACY SYSTEM</p>
<p>Partial DD: subDD 59.7 fld: 10</p>
<blockquote>
<p>fld: 10.1</p>
<p>fld: 10.2</p>
<p>fld: 11</p>
<p>fld: 12</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Templates

| Sort      | File |
|-----------|------|
| PSNFRMSRT | 50   |

| Print     | File   |
|-----------|--------|
| PSNFRMPRT | 50     |
| PSNHEAD   | 50     |
| PSNLDG1   | 50     |
| PSNPRINT  | 50.605 |
| PSNRPT4   | 50     |
| PSNACTION | 56     |

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of routines you will see for NDF when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (*First Line Routine Print*) to print a list of just the first line of each PSN\* routine.

| PSN4P4   | PSN4POST                                             | PSN4PRE  | PSN50612 | PSN50625 |
|----------|------------------------------------------------------|----------|----------|----------|
| PSN50626 | PSN50627                                             | PSN5067  | PSN50P41 | PSN50P4A |
| PSN50P6  | PSN50P65                                             | PSN50P67 | PSN50P68 | PSN56    |
| PSNACT   | PSNAPIS                                              | PSNAUTO  | PSNBLD   | PSNCLPR  |
| PSNCLS   | PSNCMOP                                              | PSNCOMP  | PSNDDI1  | PSNDEA   |
| PSNDEX   | PSNDI                                                | PSNDINT  | PSNDRUG  | PSNEN169 |
| PSNEXC   | <span id="_bookmark0" class="anchor"></span>PSNFDAMG | PSNFRMLY | PSNHEADR | PSNHELP  |
| PSNHELP1 | PSNHFRM                                              | PSNHFRM1 | PSNHIT   | PSNLDG   |
| PSNLOOK  | PSNMCLS                                              | PSNMEDG  | PSNMRG   | PSNNDC   |
| PSNNDC1  | PSNNFL                                               | PSNNFL1  | PSNNGR   | PSNOCLS  |
| PSNONDF  | PSNOUT                                               | PSNPFN   | PSNPO169 | PSNPPIO  |
| PSNPPIP  | PSNPPIP1                                             | PSNPRE   | PSNPRE1  | PSNPREDS |
| PSNPSS   | PSNPST                                               | PSNQA    | PSNRPT   | PSNRPT2  |
| PSNRPT3  | PSNSTCK                                              | PSNSTCL  | PSNSUPLY | PSNTER   |
| PSNUPN   | PSNVAGN                                              | PSNVER   | PSNVFY   | PSNVIEW  |
| PSNVUID  | PSNXREF                                              |          |          |          |

> 77 Routines

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File \[PSNMGR\] menu, assigned to all users, contains two locked options — *Allow Unmatched Drugs to Be Classed* \[PSNSTCL\] and *Formulary Report* \[PSNFRMLY\]. These options are unlocked by the PSNMGR key. This key must be assigned to the package coordinator or his/her designee. Only users having this key will see these options on their menu.

> The following are the options exported with NDF version 4.0:

### National Drug File V. 4.0 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REMA Rematch/Match Single Drugs \[PSNDRUG\] VER Verify Matches \[PSNVFY\]

> SVER Verify Single Match \[PSNVER\]

> MERG Merge National Drug File Data Into Local File \[PSNMRG\] AUTO Automatic Match of Unmatched Drugs \[PSNAUTO\]

> CLAS Allow Unmatched Drugs to be Classed \[PSNSTCL\] \[Locked: PSNMGR\]

> RPRT National Drug File Reports \[PSNSUBM\] LDF Local Drug File Report \[PSNLDG\]

> VAGN Report of VA Generic Names from National Drug \[PSNVAGN\] ATMP Report of Attempted Match Drugs \[PSNEXC\]

> PROD VA Product Names Matched Report \[PSNPFN\]

> NOCL Local Drugs with No VA Drug Class Report \[PSNOCLS\] CLVA VA Drug Classification \[PSNCLS\]

> DFL NDF Info from Your Local Drug File \[PSNRPT\] SUPL Supply (XA000) VA Class Report \[PSNSUPLY\] MANC Manually Classed Drugs Report \[PSNMCLS\]

> NMAT Local Drugs with NO Match to NDF Report \[PSNONDF\]

> \*LOCF Local Formulary Report \[PSNFRMLY\] \[Locked: PSNMGR\] NATF National Formulary Report \[PSNNFL\]

> DDIN Drug-Drug Interaction Report \[PSNTER\]

> CMOP VA Products Marked for CMOP Transmission \[PSNCMOP\] PNCL VA Product Names By Class Report \[PSNCLPR\]

> LDRG Local Drugs Excluded from Drug-Drug Interactions \[PSNODDI\]

> VDRG VA Products Excluded from Drug-Drug Interactions \[PSNEXMPT\] INQ Inquiry Options \[PSNQUER\]

> LINQ Inquire to Local Drug File \[PSNVIEW\]

> \*\*PNIN Inquire to VA Product Info For Local Drug \[PSNLOOK\] NDCU NDC/UPN Inquiry \[PSNUPN\]

> NAT Inquire to National Files \[PSNACT\] PMIS Print a PMI Sheet \[PSNPMIS\]

> <span id="_bookmark1" class="anchor"></span>FDA Display FDA Medication Guide \[PSN MED GUIDE\]

> \* Formerly *Formulary Report*

> \*\* Formerly *Lookup National Drug Info in Local File.*

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NDF software contains no archiving or purging capabilities. It is recommended that National Drug File remain online.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File contains one callable routine at the present time. This routine, PSNNGR, is used by the Allergy Tracking System software package. The routine is the actual point of entry.

> This routine is to be used in conjunction with the allergies package. It expects an input of PSNDA=internal number in File 50.6 (VA GENERIC file). The routine returns ^TMP("PSN",\$J,IFN)=Primary Ingredient. The IFN is the Internal number from File \#50.416 (DRUG INGREDIENTS file) of Primary Ingredient. If PSNDA doesn’t exist, PSNID and ^TMP("PSN",\$J) are killed. The variables X,J,K,PSNPN are used and are killed before exiting.

> For detailed information on all supported National Drug File APIs, see the *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual* posted on the VistA Documentation Library (VDL) at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/).

## External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File V. 4.0 relies (minimum) on the following external packages. This software is not included in this package and must be installed before this version of NDF is completely functional.

### <u>Package</u> <u>Minimum Version Needed</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA FileMan 21.0

> Kernel 8.0

> MailMan 7.1

> Pharmacy Data Management 1.0

> National Drug File 3.18

> Adverse Reaction Tracking 4.0

> Consolidated Mail Outpatient Pharmacy 2.0

> Decision Support System 3.0

> Drug Accountability 3.0

> Immunology Case Registry 2.1

> Inpatient Medications 4.5 or greater

> Order Entry/Results Reporting 2.5 or greater

> Outpatient Pharmacy 6.0 or greater

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Automatic Match by NDC Matching Pairing of a drug from the local DRUG
> file (#50) with a drug in the National Drug File with the same NDC number. This matching will be accomplished when the option *Automatic Match of Unmatched Drugs* is executed for the first time.
> Active Drug Drugs which contain no inactivation date in the INACTIVE DATE field (#100) local DRUG file (#50).
> API Application Programmer Interface.
> DEA, SPECIAL HDLG Field Field \#3. A field in the local DRUG file
> (#50). It contains one or more codes representing special characteristics of a product.
> DRUG File See Local DRUG file.
> DRUG INGREDIENTS File File \#50.416. A file that contains
> individual generic drugs which are components of various drug products.
> Error In the National Drug File (NDF) software, an error is an entry in the NATIONAL DRUG TRANSLATION file
> (#50.12) that does not have a match in the local DRUG file (#50).
> <span id="_bookmark2" class="anchor"></span>FDA Medication Guide Paper handouts that come with many prescription medicines given to the patient. The guides address issues that are specific to particular drugs and drug classes, and contain FDA-approved information that can help patients avoid serious adverse events.
> FSN Federal Stock Number. A unique
> identifying number assigned by the Federal Supply System to a product
> (drug, supply, food item, etc.) for ordering and accounting purposes. Synonymous with the National Stock Number (NSN). This is one of the fields in the local DRUG file (#50).
> Local DRUG File (#50) This file contains the local GENERIC NAME (#.01), INACTIVE DATE (#100), DEA, SPECIAL HDLG (#3), and NDC
> fields, as well as others. NDF software attempts to match products from this file with products in the VA GENERIC file (#50.6) and the VA PRODUCT file (#50.58).
> Manually Classed Drug A drug from the local DRUG file (#50) which could not be matched, but has been assigned a VA Drug Classification through the use of the *Allow Unmatched Drugs to Be Classed* menu option.
> Manufacturer Code The first portion of the NDC Number (the first 4-6 digits). Identifies the manufacturer of the product.
> NATIONAL DRUG File (#50.6) This file contains a list of available drug
> products. It includes specific information for each product, including trade name, NDC number, manufacturer, VA Drug Class code, dosage form, route of administration, strength, units, ingredients, ingredient strength and units, package code, package size, package type, VA Product Name, and VA generic name. NDF software attempts to match products from this file with products in the local DRUG file (#50).
> National Drug Identifier A unique, HL7 compatible code assigned to all products marked for CMOP transmission. This code is utilized to transmit VA Print name and dispense unit from VistA to the vendor system.
