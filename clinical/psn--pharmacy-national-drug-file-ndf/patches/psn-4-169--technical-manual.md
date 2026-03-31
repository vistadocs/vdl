---
title: PSN*4*169 Technical Manual / Security Guide Change Pages (Pre/Pre Release)
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
patch_id: PSN*4*169
group_key: "PSN:PSN:4"
file_numbers: []
security_keys: []
menu_options: 0
description: > ![](psn-4-169-technical-manual-security-guide-change-pages-pre-pre-release/001.png)
audience: 
keywords: 
  - blockquote
  - class
  - table
  - contents
  - colspan
  - header
  - style
  - width
  - strong
  - mailman
page_count: 0
word_count: 2777
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/psn_4_p169_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/psn_4_p169_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=89"
---

> ![](psn-4-169-technical-manual-security-guide-change-pages-pre-pre-release/001.png)

NATIONAL DRUG FILE (NDF)

> TECHNICAL MANUAL

# Version 4.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Version 4.0](#version-40)
- [Revision History](#revision-history)
  - [Files](#files)
    - [Templates](#templates)
  - [Routines](#routines)
  - [External Relations](#external-relations)
    - [Data Base Integration Agreements (DBIAs)](#data-base-integration-agreements-dbias)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
  - [Electronic MailMan Messages](#electronic-mailman-messages)
    - [MailMan Message 1: Data Update for NDF](#mailman-message-1-data-update-for-ndf)
    - [MailMan Message 1: Data Update for NDF (continued)](#mailman-message-1-data-update-for-ndf-continued)
    - [MailMan Message 1: Data Update for NDF (continued)](#mailman-message-1-data-update-for-ndf-continued-1)
> October 1998
> (Revised February 2009)
> Department of Veterans Affairs Office of Enterprise Development

# Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below lists changes made since the initial release of this manual. Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.

> Note: The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 55%" />
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
<td>02/09</td>
<td><p>6, 10, 10b,</p>
<p>12e-f</p></td>
<td><blockquote>
<p>PSN*4*169</p>
</blockquote></td>
<td><blockquote>
<p>Added routines PSNEN169 and PSNPO169. Described section added to the VA Product message as part of an NDF Management System change.</p>
<p>Updated Notes Regarding Patches section.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/06</td>
<td>6</td>
<td><blockquote>
<p>PSN*4*109</p>
</blockquote></td>
<td><blockquote>
<p>Added routine PSN5067 to the list of routines. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/05</td>
<td><p>iii, 6, 10b,</p>
<p>12c-d, 15, 21,</p>
<p>22</p></td>
<td><blockquote>
<p>PSN*4*101</p>
</blockquote></td>
<td><blockquote>
<p>Added routines PSNVUID and PSNPREDS, an explanation of the data standardization project in a new section called Notes regarding Patches; moved changes to CS Federal Schedule field (patch PSN*4*65) to new section; updated Table of Contents, Glossary and Index. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/04</td>
<td>i, 2, 6, 8</td>
<td><blockquote>
<p>PSN*4*80</p>
</blockquote></td>
<td><blockquote>
<p>Added routines and a reference to the <em>Pharmacy Re- Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re- Engineering (PRE) project Encapsulation cycle 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/03</td>
<td>7</td>
<td><blockquote>
<p>PSN*4*70</p>
</blockquote></td>
<td><blockquote>
<p>-Added two new options to the list of exported options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/03</td>
<td><p>Title Page,</p>
<p>i-ii, 10b</p></td>
<td><blockquote>
<p>PSN*4*65</p>
</blockquote></td>
<td><blockquote>
<p>- Noted changes to CS Federal Schedule field.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>04/03</td>
<td><p>Title Page,</p>
<p>i, 15</p></td>
<td><blockquote>
<p>PSN*4*20</p>
</blockquote></td>
<td><blockquote>
<p>-Changed the RD access on several files.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/03</td>
<td><p>Title Page,</p>
<p>i, 6</p></td>
<td><blockquote>
<p>PSN*4*68</p>
</blockquote></td>
<td><blockquote>
<p>-Added the PSNPPIO routine to the list of routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>02/03</td>
<td><blockquote>
<p>Title Page, i-iv,</p>
</blockquote>
<p>4a-4d, 6</p></td>
<td><blockquote>
<p>PSN*4*62</p>
</blockquote></td>
<td><blockquote>
<p>-Replaced the Title Page, Revision History Page, and Table of Contents.</p>
<p>-Added the Patient Medication Information (PMI) Sheet enhancement files and printer set-up.</p>
<p>-Added print routine to the list of routines.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 55%" />
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
<tr class="even">
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
<li><p>Updated the Electronic MailMan Messages for Data Update for NDF, Updated Interactions, and Drugs Unmatched from National Drug File. This included new screen captures and required the addition of new pages.</p></li>
</ul></td>
</tr>
<tr class="odd">
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
<tr class="even">
<td>02/00</td>
<td><blockquote>
<p>6,7,9</p>
</blockquote></td>
<td><blockquote>
<p>PSN*4*22</p>
</blockquote></td>
<td>Added a new option called <em>Inquire to National Files.</em></td>
</tr>
<tr class="odd">
<td>10/98</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>
## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NATIONAL DRUG file (#50.6) has been redesigned from a file seven multiples deep to a new file structure of four separate files. The new files are the VA PRODUCT file (#50.68), the NDC/UPN file (#50.67), the VA DISPENSE

> UNIT file (#50.64), and File \#50.6, which is now the VA GENERIC file.

> The files required to run the NDF software are listed below.

<table style="width:100%;">
<colgroup>
<col style="width: 48%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
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
<th rowspan="16"></th>
</tr>
<tr class="odd">
<th>50.416 DRUG INGREDIENT</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th>50.6 VA GENERIC</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>50.605 VA DRUG CLASS</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th><p>50.606 DOSAGE FORM</p>
<p>Partial DD: subDD 50.606 fld: .01</p></th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="odd">
<th>50.607 DRUG UNITS</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th>50.608 PACKAGE TYPE</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="odd">
<th>50.609 PACKAGE SIZE</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th>50.612 NATIONAL DRUG TRANSLATION</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>50.64 VA DISPENSE UNIT</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th>50.67 NDC/UPN</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>50.68 VA PRODUCT</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><p>51.2 MEDICATION ROUTES</p>
<p>Partial DD: subDD 51.2 fld: .01</p></th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th><blockquote>
<p>MERG</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>YES</th>
</tr>
<tr class="odd">
<th>55.95 DRUG MANUFACTURER</th>
<th>YES</th>
<th>YES</th>
<th>YES</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="header">
<th>56 DRUG INTERACTION</th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th><blockquote>
<p>OVER</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
<th>NO</th>
</tr>
<tr class="odd">
<th><p>59.7 PHARMACY SYSTEM</p>
<p>Partial DD: subDD 59.7 fld: 10</p>
<blockquote>
<p>fld: 10.1</p>
<p>fld: 10.2</p>
<p>fld: 11</p>
<p>fld: 12</p>
</blockquote></th>
<th>YES</th>
<th>YES</th>
<th>NO</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSN4P4</p>
</blockquote></th>
<th><blockquote>
<p>PSN4POST</p>
</blockquote></th>
<th><blockquote>
<p>PSN4PRE</p>
</blockquote></th>
<th><blockquote>
<p>PSN50612</p>
</blockquote></th>
<th><blockquote>
<p>PSN50625</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSN50626</p>
</blockquote></td>
<td><blockquote>
<p>PSN50627</p>
</blockquote></td>
<td><blockquote>
<p>PSN5067</p>
</blockquote></td>
<td><blockquote>
<p>PSN50P41</p>
</blockquote></td>
<td><blockquote>
<p>PSN50P4A</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSN50P6</p>
</blockquote></td>
<td><blockquote>
<p>PSN50P65</p>
</blockquote></td>
<td><blockquote>
<p>PSN50P67</p>
</blockquote></td>
<td><blockquote>
<p>PSN50P68</p>
</blockquote></td>
<td><blockquote>
<p>PSN56</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNACT</p>
</blockquote></td>
<td><blockquote>
<p>PSNAPIS</p>
</blockquote></td>
<td><blockquote>
<p>PSNAUTO</p>
</blockquote></td>
<td><blockquote>
<p>PSNBLD</p>
</blockquote></td>
<td><blockquote>
<p>PSNCLPR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNCLS</p>
</blockquote></td>
<td><blockquote>
<p>PSNCMOP</p>
</blockquote></td>
<td><blockquote>
<p>PSNCOMP</p>
</blockquote></td>
<td><blockquote>
<p>PSNDDI1</p>
</blockquote></td>
<td><blockquote>
<p>PSNDEA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNDEX</p>
</blockquote></td>
<td><blockquote>
<p>PSNDI</p>
</blockquote></td>
<td><blockquote>
<p>PSNDINT</p>
</blockquote></td>
<td><blockquote>
<p>PSNDRUG</p>
</blockquote></td>
<td><blockquote>
<p>PSNEN169</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNEXC</p>
</blockquote></td>
<td><blockquote>
<p>PSNFRMLY</p>
</blockquote></td>
<td><blockquote>
<p>PSNHEADR</p>
</blockquote></td>
<td><blockquote>
<p>PSNHELP</p>
</blockquote></td>
<td><blockquote>
<p>PSNHELP1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNHFRM</p>
</blockquote></td>
<td><blockquote>
<p>PSNHFRM1</p>
</blockquote></td>
<td><blockquote>
<p>PSNHIT</p>
</blockquote></td>
<td><blockquote>
<p>PSNLDG</p>
</blockquote></td>
<td><blockquote>
<p>PSNLOOK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNMCLS</p>
</blockquote></td>
<td><blockquote>
<p>PSNMRG</p>
</blockquote></td>
<td><blockquote>
<p>PSNNDC</p>
</blockquote></td>
<td><blockquote>
<p>PSNNDC1</p>
</blockquote></td>
<td><blockquote>
<p>PSNNFL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNNFL1</p>
</blockquote></td>
<td><blockquote>
<p>PSNNGR</p>
</blockquote></td>
<td><blockquote>
<p>PSNOCLS</p>
</blockquote></td>
<td><blockquote>
<p>PSNONDF</p>
</blockquote></td>
<td><blockquote>
<p>PSNOUT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNPFN</p>
</blockquote></td>
<td><blockquote>
<p>PSNPO169</p>
</blockquote></td>
<td><blockquote>
<p>PSNPPIO</p>
</blockquote></td>
<td><blockquote>
<p>PSNPPIP</p>
</blockquote></td>
<td><blockquote>
<p>PSNPPIP1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNPRE</p>
</blockquote></td>
<td><blockquote>
<p>PSNPRE1</p>
</blockquote></td>
<td><blockquote>
<p>PSNPREDS</p>
</blockquote></td>
<td><blockquote>
<p>PSNPSS</p>
</blockquote></td>
<td><blockquote>
<p>PSNPST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNQA</p>
</blockquote></td>
<td><blockquote>
<p>PSNRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSNRPT2</p>
</blockquote></td>
<td><blockquote>
<p>PSNRPT3</p>
</blockquote></td>
<td><blockquote>
<p>PSNSTCK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSNSTCL</p>
</blockquote></td>
<td><blockquote>
<p>PSNSUPLY</p>
</blockquote></td>
<td><blockquote>
<p>PSNTER</p>
</blockquote></td>
<td><blockquote>
<p>PSNUPN</p>
</blockquote></td>
<td><blockquote>
<p>PSNVAGN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSNVER</p>
</blockquote></td>
<td><blockquote>
<p>PSNVFY</p>
</blockquote></td>
<td><blockquote>
<p>PSNVIEW</p>
</blockquote></td>
<td><blockquote>
<p>PSNVUID</p>
</blockquote></td>
<td><blockquote>
<p>PSNXREF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 75 Routines

> The build will check to make sure that the site has the following patches installed:

> <u>Package</u> <u>Patch Needed</u>

> Adverse Reaction Tracking V. 4.0 GMRA\*4\*13 Consolidated Mail Outpatient Pharmacy V. 2.0 PSX\*2\*18 Decision Support System V. 3.0 ECX\*3\*10

> Drug Accountability V. 3.0 PSA\*3\*8

> Immunology Case Registry V. 2.1 IMR\*2.1\*3

> Inpatient Medications V. 4.5 PSJ\*4.5\*59

> Inpatient Medications V. 5.0 PSJ\*5\*11, PSJ\*5\*14 Order Entry/Results Reporting V. 3.0 OR\*3\*33 *\[CPRS sites only\]* Outpatient Pharmacy V. 6.0 PSO\*6\*173

> Outpatient Pharmacy V. 7.0 PSO\*7\*10, PSO\*7\*11

> Pharmacy Data Management V. 1.0 PSS\*1\*29

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Base Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> National Drug File (NDF) V. 4.0 has Data Base Integration Agreements (DBIAs) with the packages listed above. For complete information regarding the DBIAs for NDF V. 4.0, please refer to the *DBA* \[DBA\] menu option on FORUM and then the *Integration Agreement Menu* \[DBA IA ISC\].

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the National Drug File software package options have been designed to stand-alone.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File routines do not use package-wide variables.

## Electronic MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the data patches have been sent, you and holder(s) of the PSNMGR key will receive Mailman messages similar to the following examples.

> The first MailMan message lists new VA products that have been added to the National Drug File, the active VA products that are unmarked for CMOP, the VA products for which the National Formulary Indicator is changed, and the VA products that have had the OVERRIDE dosage form excluded from dosage checks flag edited. The second MailMan message lists the interactions that have been added, edited, or inactivated in the National Drug File. The third MailMan message contains a list of drugs unmatched from the National Drug File.

### MailMan Message 1: Data Update for NDF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 67%" />
<col style="width: 22%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Subj: DATA UPDATE FOR NDF [#112345] 03 May 02 11:31</th>
<th><blockquote>
<p>420 lines</p>
</blockquote></th>
<th rowspan="32"></th>
</tr>
<tr class="odd">
<th>From: NDF MANAGER In 'IN' basket. Page 1</th>
<th></th>
</tr>
<tr class="header">
<th colspan="2">The following VA Products have been added to the National</th>
</tr>
<tr class="odd">
<th colspan="2">Drug File. You may wish to review, then match or unmatch</th>
</tr>
<tr class="header">
<th colspan="2">local drug file entries based on this updated information.</th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>ACCU-CHEK ACTIVE (GLUCOSE) TEST STRIP</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>(CMOP - XZ355) (DISPENSE UNIT - EA)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>050924-0681-01 050924-0475-50</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>BOSENTAN 125MG TAB</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>(CMOP - B0477) (DISPENSE UNIT - TAB)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>066215-0102-06</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>CHONDROITIN NA 40MG/HYALURONATE 30MG/ML INJ,OPH,SYRINGE,0.75ML</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>(CMOP - C1041) (DISPENSE UNIT - SYRINGE)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>008065-1839-75</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>DIGOXIN (LANOXIN) 0.125MG TAB</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>(CMOP - D0080) (DISPENSE UNIT - TAB)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>000173-0242-75 000173-0242-30 000173-0242-55</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>ESTRADIOL 25MCG TAB,VAG,APPLICATOR</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>(CMOP - E0335) (DISPENSE UNIT - EA)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>000009-5173-03 000009-5173-02 000009-5173-04</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>FERROUS SO4 325MG TAB,EC,UD</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>(CMOP - F0297) (DISPENSE UNIT - TAB)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>000574-0608-11</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>GLYCERIN 3%/SODIUM CL 0.75% SOLN,NASAL</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>(CMOP - G0220) (DISPENSE UNIT - ML)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>050930-0280-50 050930-0280-32</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>HYDROGEN PEROXIDE 1.5% RINSE,ORAL</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>(CMOP - H0408) (DISPENSE UNIT - ML)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>010310-3186-00 038341-0800-80 038341-0801-60</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>IBRITUMOMAB TIUXETAN IN-111 INJ,KIT</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>(CMOP - I0336) (DISPENSE UNIT - KIT)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>064406-0104-04</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> report continues

### MailMan Message 1: Data Update for NDF (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Formulary Indicator has changed for the following

> VA Products. The National Formulary Indicator will automatically be changed in your local DRUG file (#50). Please review the

> VISN and Local Formulary designations of these products and make appropriate changes.

> FORMULARY ITEMS

> ACCU-CHEK ACTIVE (GLUCOSE) TEST STRIP

> AL OH 500MG/MG OH 400MG/SIMETHICONE 40MG/5ML LIQUID(ML) ALBUTEROL SO4 0.5% SOLN,INHL,5ML

> CLARITHROMYCIN 500MG TAB,SA,PKT,14 EFAVIRENZ 600MG TAB

> ENOXAPARIN 120MG/0.8ML INJ,SYRINGE,0.8ML FOLIC ACID 1MG TAB,UD

> GUAIFENESIN 100MG/5ML (AF) LIQUID

> HEPATITIS A 720 EL.U/HEPATITIS B 20MCG/1ML VACCINE INJ HEPATITIS A 720 EL.U/HEPATITIS B 20MCG/ML VACCINE INJ,SYR,1ML

> NON-FORMULARY ITEMS OPIUM 10% TINCTURE

> PROCAINAMIDE HCL 1000MG TAB,SA PROCAINAMIDE HCL 250MG CAP PROCAINAMIDE HCL 250MG TAB

> The following active VA Products are no longer marked for CMOP. All local drug file entries matched to these VA Products will be UNMARKED for CMOP. In order to have these entries dispensed by CMOP any local DRUG file (#50) entries matched to these

> products must be re-matched to another VA product that is actively marked for CMOP dispensing.

> ANTI-THYMOCYTE GLOBULIN (RABBIT) 25MG/VIL INJ A1108 BANDAGE,PROFORE FOUR LAYER SYSTEM,S-N \#66000016 XX199 ISOTRETINOIN 10MG CAP I0085

> ISOTRETINOIN 20MG CAP I0086 ISOTRETINOIN 40MG CAP I0087

> The National Formulary Restriction has changed for the following VA Products.

> MONTELUKAST NA 10MG TAB

> Refer to leukotriene inhibitor criteria for use. MONTELUKAST NA 10MG TAB,UD

> Refer to leukotriene inhibitor criteria for use. PROCAINAMIDE HCL(PROCANBID)500MG TAB,SA

> Refer to Procainamide drug monitoring recommendations.

### MailMan Message 1: Data Update for NDF (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note regarding Patch PSN\*4\*169

> This patch makes these corrections to the INQUIRE TO VA PRODUCT INFO FOR LOCAL DRUG \[PSNLOOK\] option:

> Problem: Sometimes the Active Ingredients would not display. Solution: The Active Ingredients will now always display.

> Problem: Sometimes the Strength that is displayed next to the Active Ingredient is actually the Strength of the VA Product.

> Solution: The Strength of the Active Ingredient will now accurately display.

> Problem: The Drug Unit was not always displaying. Solution: The Drug Unit will now always display.

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will now display.

> Problem: When displaying the Active Ingredients, the text (Primary) will no longer display next to an Active Ingredient that is a Primary Ingredient.

> Solution: The Primary Ingredient will now display if the Ingredient of the VA Product has a Primary Ingredient.

> This patch makes these corrections to the INQUIRE TO NATIONAL FILES \[PSNACT\] option:

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will now display.

> Problem: The National Formulary Restriction display was being truncated after one line if it was two or more lines in length.

> Solution: The entire text entered for the National Formulary Restriction will now display.

> February 2009 National Drug File V. 4.0 12e

> (This page included for two-sided copying.)